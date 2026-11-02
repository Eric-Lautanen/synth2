#!/usr/bin/env python3
"""synth2 pre-flight -- the whole checklist in one command, before you append.

Every check here is one this campaign has been bitten by: a batch that was
78.7% multi when the law wants ~50%, six rows written as a single turn, 28% of
assistant turns opening on `and`, 22% of questions with no `?`, a premise
repeated four times that no gate reads. Each of those cost a separate fix pass
and a separate round trip, because they were being run as one-off scripts.

Three of them are NOT the obvious thing, and are the reason this file exists:

1. THE REFERENCE IS NOT THE LIVE FILE. If the target file contains other
   writers' machine output, its opener histogram is that template and copying
   it will light the build's own scan immediately. `--ref` therefore measures
   the reference's CLEAN SUBSET -- the batches of that file that do not trip
   the generator-shape test in `integrity.py` -- and prints which ones it
   skipped so you can check its judgement.
2. `?` IS A GATE. A turn that opens with a question word and does not end with
   `?` is malformed against the schema. Both directions are checked.
3. COUNT EVERY POSITION, EVERY PASS. Fixing position n's template moves it to
   position n+1; only a per-position histogram catches that.

Usage:
  python runs/synth2/scripts/preflight.py my_batch.txt \
      --ref runs/synth2/raw/small_talk_nostalgic.jsonl

Read-only except for one call to `add_rows.py --dry-run` (which writes
nothing) so the near-dup gate is part of the same command. Exit code 1 on any
FAIL, so it can gate a pipeline. Warnings do not fail the run.
"""
import argparse
import collections
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.normpath(os.path.join(HERE, "..", "raw"))
sys.path.insert(0, HERE)

from integrity import FUNC, read_rows  # noqa: E402  (shared logic)

# Aux-initial openers are reliably direct questions in chat. Wh-initial ones are
# not: `when the old man died the street went quiet` and `which happened three
# times and then stopped` are statements that merely START with a question word
# -- the same false-positive class `qmark.py` records (ANY_OPEN + relative
# clause). So wh-initial only FAILS when the turn is short enough to be a direct
# question, and is otherwise a WARN for a human to read.
AUX_OPEN = set("""did does do is are was were am can could shall should will would
may might must have has had""".split())
WH_OPEN = set("what when where who whom whose why how which".split())
WH_DIRECT_MAX_WORDS = 5

MULTI_TARGET = 50.0        # the law: roughly half of every file
MULTI_TOL = 5.0
OPENER_FACTOR = 3.0        # flag a token at >=3x the reference
OPENER_FLOOR = 8.0         # ...and at least this share of the position
CHAR_CAP = 4000


def words(text):
    return re.findall(r"[a-z']+", str(text).lower())


def load_pipe(path):
    with open(path, encoding="utf-8") as fh:
        lines = [ln for ln in fh.read().split("\n") if ln.strip()]
    return [ln.split(" | ") for ln in lines]


def batches_of(path):
    """{batch_no: [[turn, ...], ...]} plus the set of batches missing ids.

    A row with no `id` bypassed `add_rows.py`, and in this campaign every
    no-`id` block has turned out to be machine output -- so those batches are
    excluded from the reference as well as the shape test.
    """
    _, rows, _ = read_rows(path)
    out = collections.defaultdict(list)
    noid = set()
    for r in rows:
        out[r.get("batch_no")].append([t.get("text", "") for t in r.get("turns", [])])
        if "id" not in r:
            noid.add(r.get("batch_no"))
    return out, noid


def shape(turns):
    asst = [t for i, t in enumerate(turns) if i % 2 == 1]
    toks = [words(t) for t in asst]
    toks = [t for t in toks if t]
    if not toks:
        return 99.0, 0.0
    return (sum(len(t) for t in toks) / len(toks),
            100.0 * sum(1 for t in toks if not (set(t) & FUNC)) / len(toks))


def reference_openers(ref_path):
    """First-word share per position over the reference file's CLEAN batches."""
    by, noid = batches_of(ref_path)
    kept, skipped = {}, []
    for b, rows in by.items():
        if b in noid:
            skipped.append((b, len(rows), -1.0, -1.0))   # -1 marks 'no id'
            continue
        asst = [t[1::2] for t in rows]
        flat = [t for row in asst for t in row]
        toks = [words(t) for t in flat]
        toks = [t for t in toks if t]
        m = sum(len(t) for t in toks) / max(1, len(toks))
        nf = 100.0 * sum(1 for t in toks if not (set(t) & FUNC)) / max(1, len(toks))
        if m < 6.2 and nf > 40.0:
            skipped.append((b, len(rows), round(m, 2), round(nf, 1)))
            continue
        kept[b] = rows
    pos = {0: collections.Counter(), 1: collections.Counter(),
           2: collections.Counter(), "last": collections.Counter()}
    denom = collections.Counter()
    for rows in kept.values():
        for r in rows:
            idxs = [(0, r[0]), (1, r[1] if len(r) > 1 else None)]
            if len(r) > 2:
                idxs.append((2, r[2]))
            if r:
                idxs.append(("last", r[-1]))
            for k, t in idxs:
                if t is None:
                    continue
                denom[k] += 1          # rows that HAVE this position
                w = words(t)
                if w:
                    pos[k][w[0]] += 1
    return pos, denom, skipped, len(kept)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch", help="pipe-format batch file (turns joined by ' | ')")
    ap.add_argument("--ref", help="raw file to take the opener reference from")
    ap.add_argument("--no-ref", action="store_true", help="skip opener comparison")
    ap.add_argument("--skip-dry-run", action="store_true")
    args = ap.parse_args()

    segs = load_pipe(args.batch)
    fails, warns = [], []

    def fail(msg):
        fails.append(msg)

    def warn(msg):
        warns.append(msg)

    print("=" * 78)
    print("PRE-FLIGHT  %s  --  %d row(s)" % (os.path.basename(args.batch), len(segs)))
    print("=" * 78)

    # --- 1. structure -------------------------------------------------------
    bad = [i + 1 for i, s in enumerate(segs) if len(s) % 2]
    if bad:
        fail("odd turn count on row(s): %s (start user, end assistant)" % bad[:12])
    empty = [(i + 1, k) for i, s in enumerate(segs) for k, t in enumerate(s) if not t.strip()]
    if empty:
        fail("empty turn(s): %s" % empty[:8])
    print("turns/row: %s" % dict(collections.Counter(len(s) for s in segs)))

    multi = sum(1 for s in segs if len(s) > 2)
    share = 100.0 * multi / max(1, len(segs))
    if abs(share - MULTI_TARGET) > MULTI_TOL:
        fail("multi %.1f%% is outside %.0f-%.0f%% (the law wants ~half)"
             % (share, MULTI_TARGET - MULTI_TOL, MULTI_TARGET + MULTI_TOL))
    print("multi: %d/%d = %.1f%%" % (multi, len(segs), share))

    # --- 2. buckets, exactly as add_rows derives them -----------------------
    buckets = collections.Counter()
    for s in segs:
        longest = max(len(t.split()) for t in s)
        buckets["short" if longest < 15 else ("medium" if longest < 60 else "long")] += 1
    n = max(1, len(segs))
    print("buckets: %d/%d/%d = %.1f/%.1f/%.1f (short/medium/long)"
          % (buckets["short"], buckets["medium"], buckets["long"],
             100.0 * buckets["short"] / n, 100.0 * buckets["medium"] / n,
             100.0 * buckets["long"] / n))
    if buckets["long"] == 0:
        fail("no long rows -- every file must have them")
    if buckets["short"] < 0.5 * n:
        warn("short is under half the batch; shorts crowd out mediums unless written on purpose")

    # --- 3. character rules -------------------------------------------------
    raw = open(args.batch, encoding="utf-8").read()
    if "-" in raw:
        fail("%d row(s) contain a hyphen (the '-' character is banned)"
             % sum(1 for s in segs if any("-" in t for t in s)))
    for name, ch in (("en dash", "\u2013"), ("em dash", "\u2014")):
        if ch in raw:
            fail("%s present" % name)
    na = [(i + 1, k) for i, s in enumerate(segs) for k, t in enumerate(s)
          if any(ord(c) > 127 for c in t)]
    if na:
        fail("non-ASCII in row/turn: %s" % na[:6])
    longt = [(i + 1, k, len(t)) for i, s in enumerate(segs) for k, t in enumerate(s)
             if len(t) > CHAR_CAP]
    if longt:
        fail("turn(s) over the %d char cap: %s" % (CHAR_CAP, longt[:4]))

    # --- 4. the '?' rule, both directions ----------------------------------
    missing, maybe, spurious = [], [], []
    for i, s in enumerate(segs, 1):
        for k, t in enumerate(s):
            toks = words(t)
            if not toks:
                continue
            ends = t.strip().endswith("?")
            aux = toks[0] in AUX_OPEN
            wh = toks[0] in WH_OPEN
            if not ends and (aux or (wh and len(toks) <= WH_DIRECT_MAX_WORDS)):
                missing.append((i, k, t[:48]))
            elif not ends and wh:
                maybe.append((i, k, t[:48]))
            elif ends and not aux and not wh:
                spurious.append((i, k, t[:48]))
    if missing:
        fail("%d question(s) with no '?': %s" % (len(missing), missing[:6]))
    if maybe:
        warn("%d wh-initial turn(s) with no '?' -- read each, they may be statements: %s"
             % (len(maybe), maybe[:8]))
    if spurious:
        warn("%d turn(s) end with '?' but read as statements: %s" % (len(spurious), spurious[:6]))
    print("'?' rule: %d missing, %d to read, %d suspicious"
          % (len(missing), len(maybe), len(spurious)))

    # --- 5. openers per position, vs the reference's CLEAN subset ----------
    if not args.no_ref and args.ref:
        pos, denom, skipped, kept = reference_openers(args.ref)
        print("\nreference: %s -- %d clean batch(es) kept, %d skipped as generator-shaped"
              % (os.path.basename(args.ref), kept, len(skipped)))
        for b, cnt, m, nf in sorted(skipped, key=lambda x: (x[0] if isinstance(x[0], int) else 0)):
            if m < 0:
                print("   skipped b%s (%d rows, no id -- bypassed the one door)" % (b, cnt))
            else:
                print("   skipped b%s (%d rows, %.2f words, %.1f%% no-func -- generator shape)"
                      % (b, cnt, m, nf))
        mine = {0: collections.Counter(), 1: collections.Counter(),
                2: collections.Counter(), "last": collections.Counter()}
        for s in segs:
            for k, t in ((0, s[0]), (1, s[1] if len(s) > 1 else ""), ("last", s[-1])):
                w = words(t)
                if w:
                    mine[k][w[0]] += 1
            if len(s) > 2:
                w = words(s[2])
                if w:
                    mine[2][w[0]] += 1
        print("\n  %-6s %-42s %s" % ("pos", "batch (top 5)", "reference top 3"))
        for k in (0, 1, 2, "last"):
            d = max(1, denom.get(k, 0))
            red = max(1, len(segs) if k != 2 else multi)
            # denom[k] is a row count, so both sides are shares of rows.
            print("  %-6s %-42s %s"
                  % (k, "  ".join("%s %.1f%%" % (w, 100.0 * c / red)
                                  for w, c in mine[k].most_common(5)),
                     "  ".join("%s %.1f%%" % (w, 100.0 * c / d)
                               for w, c in pos[k].most_common(3))))
            for w, c in mine[k].most_common(8):
                share_b = 100.0 * c / red
                ref = 100.0 * pos[k][w] / d
                if share_b >= OPENER_FLOOR and share_b > OPENER_FACTOR * ref:
                    fail("position %s: opener '%s' at %.1f%% vs reference %.1f%% (%.1fx)"
                         % (k, w, share_b, ref, share_b / max(ref, 0.1)))
    elif not args.no_ref:
        warn("no --ref given, openers were not compared (recommended)")

    # --- 6. repeats ---------------------------------------------------------
    mine_text = [t.strip().lower() for s in segs for t in s]
    dup = {k: v for k, v in collections.Counter(mine_text).items() if v > 1}
    if dup:
        fail("turn text repeated inside the batch: %s" % list(dup)[:6])

    corpus = {}
    for name in sorted(os.listdir(RAW)):
        if not name.endswith(".jsonl"):
            continue
        _, rows, _ = read_rows(os.path.join(RAW, name))
        for r in rows:
            for t in r.get("turns", []):
                corpus.setdefault(t.get("text", "").strip().lower(), (name, r.get("batch_no")))
    hits = [(t, corpus[t]) for t in mine_text if t in corpus]
    if hits:
        fail("turn text already in the corpus: %s"
             % [(t[:40], c[0], c[1]) for t, c in hits[:6]])

    g = collections.Counter()
    for s in segs:
        for t in s[1::2]:
            w = words(t)
            for i in range(len(w) - 4):
                g[" ".join(w[i:i + 5])] += 1
    rep = sorted(((k, v) for k, v in g.items() if v > 1), key=lambda x: -x[1])
    if rep:
        bad5 = [(k, v) for k, v in rep if v > 2]
        if bad5:
            fail("assistant 5-gram repeated >2x: %s" % bad5[:5])
        elif len(rep) > 8:
            warn("%d repeated assistant 5-grams (pairs are fine, read them)" % len(rep))
    print("repeats: %d in-batch dup turn(s), %d corpus collision(s), %d repeated 5-gram(s)"
          % (len(dup), len(hits), len(rep)))

    # --- 7. the near-dup gate, via the one door ----------------------------
    if not args.skip_dry_run:
        script = os.path.join(HERE, "add_rows.py")
        r = subprocess.run([sys.executable, script, "--rows-file", os.path.abspath(args.batch),
                            "--dry-run"], capture_output=True, text=True)
        out = (r.stdout or "") + (r.stderr or "")
        tail = out.strip().splitlines()
        ok = [ln for ln in tail if ln.startswith("DRY RUN ok")]
        skips = [ln for ln in tail if "SKIP" in ln]
        if not ok:
            fail("add_rows --dry-run rejected the batch: %s"
                 % (tail[-3:] or ["(no output, exit %s)" % r.returncode]))
        else:
            print("\n%s" % ok[0])
        if skips:
            fail("near-dup SKIP line(s): %s" % skips[:6])

    # --- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    for w in warns:
        print("WARN  %s" % w)
    for f in fails:
        print("FAIL  %s" % f)
    print("%s  (%d fail, %d warn)" % ("CLEAN" if not fails else "NOT CLEAN",
                                      len(fails), len(warns)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
