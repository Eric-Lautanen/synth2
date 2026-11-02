#!/usr/bin/env python3
"""pilot_gate.py -- ONE accept/reject verdict for a candidate batch.

The campaign now has three separate instruments and a pilot that needs all of
them on every batch:

    dependence_gate.py     structural laws + the dependence gate
    _neardup_replicate.py  the 3-shingle Jaccard gate prepare.rs enforces
    diversity.py           the mode-collapse guard

Running three scripts by hand per batch is how a batch slips through with one of
them skipped. This fuses them into a single verdict, and it is SOURCE-AGNOSTIC:
it does not care whether the rows were hand-written, grammar-generated or
model-generated. That is deliberate -- Fable #709 puts the dependence gate on
every source, so the gate must not be able to tell them apart.

Checks, in order, all against the LIVE corpus where that is the right reference:
  1. structural + dependence   -> shells out to dependence_gate.py (exit code)
  2. near-dup                  -> every candidate row vs the LIVE corpus AND vs
                                  the rest of the batch (the gate is corpus-wide)
  3. diversity                 -> size-matched against a stride subsample of the
                                  live corpus (Fable #709 addition (b))

Exit 0 only when all three pass, so it can gate a pipeline.

Usage:
  python scripts/pilot_gate.py gen/ranting_compose.jsonl
  python scripts/pilot_gate.py candidate.jsonl --live raw/small_talk_casual.jsonl
"""
import argparse
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import _neardup_replicate as nd   # noqa: E402  (the exact gate logic)
import diversity                  # noqa: E402


def load(path):
    return [json.loads(l) for l in open(path, "rb").read().split(b"\r\n") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    ap.add_argument("--live", default="raw/small_talk_casual.jsonl")
    ap.add_argument("--max-dup", type=int, default=0,
                    help="allowed near-dup pairs (default 0 -- the gate is hard)")
    args = ap.parse_args()

    cand = load(args.candidate)
    live = load(args.live)
    print(f"pilot_gate: candidate {args.candidate} ({len(cand)} rows) "
          f"vs live {args.live} ({len(live)} rows)")
    verdicts = []

    # ---- 1. structural + dependence (dependence_gate.py owns these) --------
    print("\n[1] structural + dependence")
    r = subprocess.run([sys.executable, os.path.join(HERE, "dependence_gate.py"),
                        args.candidate], capture_output=True, text=True)
    tail = [l for l in r.stdout.splitlines() if l.startswith("  [")]
    for l in tail:
        print(l)
    ok_dep = r.returncode == 0
    verdicts.append(("structural + dependence", ok_dep))

    # ---- 2. near-dup, corpus-wide (live + within-batch) --------------------
    print("\n[2] near-dup gate (3-shingle Jaccard dist < %.2f)" % nd.MIN_DIST)
    # Shingle sets are computed ONCE per row. Recomputing them inside the pair
    # loop would be ~1.4M redundant builds for a 1200-row batch.
    cand_sh = [(nd.shingle_set(nd.convo_text(c)),) for c in cand]
    cand_sh = [(s, len(s)) for (s,) in cand_sh]
    live_sh = [(nd.shingle_set(nd.convo_text(x)),) for x in live]
    live_sh = [(s, len(s)) for (s,) in live_sh]

    def too_close(a, b):
        sa, na = a
        sb, nb = b
        mn, mx = min(na, nb), max(na, nb)
        if mx > nd.bound(mn):
            return False
        u = len(sa | sb)
        return bool(u) and 1.0 - len(sa & sb) / u < nd.MIN_DIST

    pairs = 0
    for i, a in enumerate(cand_sh):
        hit = any(too_close(a, x) for x in live_sh)
        if not hit:
            hit = any(too_close(a, b) for j, b in enumerate(cand_sh) if j != i)
        if hit:
            pairs += 1
    ok_dup = pairs <= args.max_dup
    print(f"  [{'PASS' if ok_dup else 'FAIL'}] near-dup pairs {pairs} "
          f"(allowed {args.max_dup}) over {len(cand_sh)} candidate rows")
    verdicts.append(("near-dup", ok_dup))

    # ---- 3. diversity, size-matched (Fable #709 addition (b)) --------------
    # ---- 3. diversity, size-matched (Fable #709 addition (b)) --------------
    n = min(len(cand), len(live))
    csub = cand[::max(1, len(cand) // n)][:n] if len(cand) > n else cand
    lsub = live[::max(1, len(live) // n)][:n] if len(live) > n else live
    pc, pl = diversity.profile(csub), diversity.profile(lsub)
    print(f"  candidate  ({len(csub)} rows): opener {pc['opener_entropy']:.3f} bits, "
          f"distinct-5 {pc['distinct'][5]:.3f}, dup-5 mass {pc['dup5_mass']:.3f}")
    print(f"  live       ({len(lsub)} rows): opener {pl['opener_entropy']:.3f} bits, "
          f"distinct-5 {pl['distinct'][5]:.3f}, dup-5 mass {pl['dup5_mass']:.3f}")
    # The bar is NOT "as diverse as the whole live corpus" -- a single category is
    # legitimately narrower. The bar is that the candidate must not be COLLAPSING:
    # dup-5-gram mass has to stay in the same order of magnitude as the live file.
    ok_div = pc["dup5_mass"] <= max(0.05, pl["dup5_mass"] * 20)
    print(f"  [{'PASS' if ok_div else 'FAIL'}] dup-5 mass {pc['dup5_mass']:.3f} "
          f"vs live {pl['dup5_mass']:.3f} (bar {max(0.05, pl['dup5_mass'] * 20):.3f})")
    verdicts.append(("diversity", ok_div))

    # ---- 3b. opener guard (Fable #765) --------------------------------------
    # The run-11 monoculture class, one position over: a green dup-5 gate hid a
    # 57% two-word opener monoculture ("that" + "a") in the pilot 150. Bars are
    # GENERATION bars and may exceed gold (live150's top opener sits ~17%):
    # top-opener share <= 15%, H >= 5.0 bits once the candidate is large enough
    # for 5.0 to be reachable (below ~100 turns the H bar scales with
    # log2(turns) so a small batch is not auto-failed).
    n_turns = max(1, sum(pc["openers"].values()))
    top_w, top_c = (pc["openers"].most_common(1) or [("-", 0)])[0]
    top_share = top_c / n_turns
    h_bar = min(5.0, 0.9 * math.log2(max(2, n_turns)))
    ok_op = top_share <= 0.15 and pc["opener_entropy"] >= h_bar
    print(f"  [{'PASS' if ok_op else 'FAIL'}] opener guard: top '{top_w}' "
          f"{top_share:.1%} (bar 15%), H {pc['opener_entropy']:.3f} "
          f"(bar {h_bar:.3f} at {n_turns} turns)")
    verdicts.append(("opener guard", ok_op))

    print("\nVERDICT: " + ("ACCEPT" if all(v for _, v in verdicts)
                           else "REJECT -- " + ", ".join(n for n, v in verdicts if not v)))
    sys.exit(0 if all(v for _, v in verdicts) else 1)


if __name__ == "__main__":
    main()
