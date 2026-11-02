#!/usr/bin/env python3
"""gen_compose.py -- the SAME category, with a COMPOSITIONAL assistant grammar.

The #714 worked example established the diagnosis: a bank of 12 FIXED assistant
frames collapses on volume (dup-5-gram mass 0.913 at 1200 rows). The #715 pool
experiment gave the law: distinct-5 = P(1 - e^(-N/P)) / N, so the surface space
P must be ~10x the row count (P ~ 100,000 for a 10K pilot).

This script tests the cheap fix for that: keep the category, the user grammar
and the dependence gate EXACTLY as they were, and replace the fixed assistant
bank with a COMPOSITIONAL assistant grammar. Each skeleton carries 3 independent
slots plus the noun, so the surface space is the PRODUCT of the slot banks:

    op(10) x verb(10) x tail(10) x noun(18) x 4 skeletons  =  72,000 surfaces

That is ~60x the 1200 rows generated here, i.e. P/N ~ 60, far past the P ~ 10N
that the occupancy law says is needed for a low dup-5-gram mass.

CAVEAT the experiment is designed to expose: the occupancy law assumed each
surface contributes its own 5-grams. A compositional grammar SHARES tails and
verb phrases across skeletons, so the distinct 5-gram count is smaller than the
surface count and the measured mass should come out WORSE than the law predicts.
That gap is the thing worth knowing -- it is the difference between "enough
surfaces" and "enough surfaces whose n-grams do not overlap".

Same dependence as gen_worked: the assistant contains the SAME surface form the
user introduced. Same gates, same instruments. Deterministic (seeded).
Writes only into runs/synth2/gen/.
"""
import argparse
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import _neardup_replicate as nd          # noqa: E402
from gen_worked import (FORMS, USER_FRAMES, PRE, TAGS, PROB, WHEN,  # noqa: E402
                        ASST_MIN, ASST_MAX, wc, bound, passes)

# --- the compositional assistant grammar ---------------------------------
OPS = ["honestly", "god", "mate", "seriously", "blimey", "look", "right",
       "crikey", "ugh", "wow"]

V3 = ["drives me mad", "gets me down", "winds me up", "ruins my day",
      "wrecks my week", "makes me cross", "boils my blood", "wears me out",
      "gets to me", "does me in"]

V4 = ["drive me up the wall", "do my head in", "get right on my nerves",
      "ruin my whole day", "wreck my morning", "make me see red",
      "be an absolute nightmare", "be a right pain", "try anyone's patience",
      "get right to me"]

V6 = ["kick off", "go mad", "lose it", "ring them up", "chase it up",
      "give up", "make a fuss", "start again", "take it back", "let it go"]

TAILS = ["every single time", "i tell you", "without fail", "i swear",
         "believe me", "time and again", "and it always does", "so it does",
         "honestly", "no word of a lie"]

# Each skeleton carries 3 independent slots plus {f}. Every one keeps the noun
# echo, none opens on the noun, and the questions end on "?".
SKELETONS = [
    lambda r: f"{r['op']} a {r['f']} like that {r['v3']} {r['t']}",
    lambda r: f"{r['op']} that {r['f']} would {r['v4']} {r['t']}",
    lambda r: f"{r['op']} i would {r['v6']} about the {r['f']} {r['t']}",
    lambda r: f"{r['op']} you should {r['v6']} about the {r['f']} {r['t']}",
]


def surface_space():
    """The size of the assistant surface space, as a product of the slot banks."""
    per_skel = len(OPS) * len(TAILS) * len(FORMS)
    # each skeleton pairs 2 of the verb banks, so average their sizes
    per_skel *= (len(V3) + len(V4) + 2 * len(V6)) / 4.0
    return int(per_skel * len(SKELETONS))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="gen/ranting_compose.jsonl")
    ap.add_argument("--target", type=int, default=1200)
    ap.add_argument("--candidates", type=int, default=40000)
    ap.add_argument("--seed", type=int, default=20261010)
    ap.add_argument("--batch-no", type=int, default=9001)
    args = ap.parse_args()

    out = args.out if os.path.isabs(args.out) else os.path.join(HERE, "..", args.out)
    out = os.path.normpath(out)
    rng = random.Random(args.seed)

    rows, accepted, seen = [], [], set()
    tried = rej_len = rej_dup = rej_near = 0

    while tried < args.candidates and len(rows) < args.target:
        tried += 1
        _, f = rng.choice(FORMS)
        u = rng.choice(USER_FRAMES).format(pre=rng.choice(PRE), tag=rng.choice(TAGS),
                                           f=f, prob=rng.choice(PROB),
                                           when=rng.choice(WHEN))
        r = {"op": rng.choice(OPS), "f": f, "v3": rng.choice(V3),
             "v4": rng.choice(V4), "v6": rng.choice(V6), "t": rng.choice(TAILS)}
        a = rng.choice(SKELETONS)(r)

        if not (ASST_MIN <= wc(a) <= ASST_MAX):
            rej_len += 1
            continue
        if a.split()[0].lower() in (f.lower(), "the"):
            rej_len += 1
            continue
        convo = f"{u} {a}"
        if convo in seen:
            rej_dup += 1
            continue
        sh = nd.shingle_set(convo)
        if not passes(sh, len(sh), accepted):
            rej_near += 1
            continue
        seen.add(convo)
        accepted.append((sh, len(sh)))
        total = wc(u) + wc(a)
        rows.append({
            "id": "st2_gencomp_%06d" % (len(rows) + 1),
            "batch_no": args.batch_no,
            "category": {"interaction_type": "small_talk", "tone": "warm_casual",
                         "turn_structure": "single_turn",
                         "length_bucket": "short" if total < 20 else "medium"},
            "turns": [{"role": "user", "text": u}, {"role": "assistant", "text": a}],
        })

    os.makedirs(os.path.dirname(out), exist_ok=True)
    blob = b"\r\n".join(json.dumps(r, ensure_ascii=False).encode("utf-8")
                        for r in rows) + b"\r\n"
    open(out, "wb").write(blob)

    print(f"COMPOSITIONAL assistant: 4 skeletons x op({len(OPS)}) x verb(~{len(V3)}) "
          f"x tail({len(TAILS)}) x noun({len(FORMS)}) = ~{surface_space():,} surfaces")
    print(f"candidates tried {tried}  ->  rows accepted {len(rows)}  "
          f"(yield {100.0 * len(rows) / max(1, tried):.1f}%)")
    print(f"rejected: {rej_len} length/frame, {rej_dup} exact-dup, {rej_near} near-dup")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
