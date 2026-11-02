#!/usr/bin/env python3
"""synth2 integrity instrument -- the checks the structural gates cannot see.

Three failure classes are live in `raw/` that `repair`, `qmark` and `verify` all
pass, and that this script is built to catch:

1. DOOR BYPASS.  `add_rows.py` is the one door into `raw/` and it stamps `id` on
   every row it writes.  A row with no `id` was appended by something else, and
   in this campaign every such block has been machine output.
2. LINE ENDING.  A block appended with bare LF makes `qmark.py` abort
   corpus-wide.  Counting bare LF is the cheapest early warning.
3. GENERATOR SHAPE.  The suffixer maximises 3-shingle distance, so the near-dup
   gate never fires.  Two lenses separate it from hand-written rows, both
   calibrated here against the file's own clean batches:
     - mean assistant words per turn,
     - share of assistant turns containing NO function word at all.
   Hand-written batches read ~5-14 words at 0.7-15% no-function-word; generator
   batches read 4.9-5.8 words at 39-71%.  Nothing sits in between.

4. DRIFT (added 2026-10-07).  The generator-shape verdict only sees the TERSE +
   no-function corner.  A hand-written file that slides terse or verbose one
   green batch at a time -- or over-uses a single opener frame -- passes it
   green, which is exactly the early drift the operator named.  The two-sided
   band below fires on BOTH ends of the length distribution plus a single
   opener frame over 30% of a batch.  These are FINDERS, NOT VERDICTS (a lens
   is a finder, never a verdict): a flagged batch is HAND-READ, never
   auto-rejected.  A legitimately terse category (sullen: "fine.") can trip the
   low floor -- look at the rows before you act on it.

The batch table read top-to-bottom IS the file-level trend view (is the file
getting terser batch over batch?); the `clean baseline` line is the file's own
median to read each batch against.

Usage:
  python runs/synth2/scripts/integrity.py              # all files
  python runs/synth2/scripts/integrity.py -f gossip    # one file (substring)
  python runs/synth2/scripts/integrity.py --rows 5030  # sample a batch
Exit code is 1 when any batch is flagged, so it can gate a pipeline.
"""
import argparse
import collections
import json
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw")
RAW = os.path.normpath(RAW)

FUNC = set(
    "a an the i you he she it we they and or but if so of to in on for with is "
    "was were be been am are do did does not no yes my your his her that this "
    "there what when who how why".split()
)

# Documented thresholds. Both must trip before a batch is called generator
# shaped: a terse batch can be low-words without being machine output.
WORD_CEIL = 6.2
NOFUNC_FLOOR = 40.0
OPENER_CEIL = 30.0

# Two-sided DRIFT band (the ADD-time finder the generator-shape verdict cannot
# make). Calibrated 2026-10-07 against casual's 9 live batches: it fires on
# exactly the two batches that had to be fixed by hand (b2075 at 6.17 words,
# b2060 at 32.1% one opener) and on nothing else. FINDERS, not verdicts.
DRIFT_WORD_LO = 8.0
DRIFT_WORD_HI = 30.0


def words(text):
    return re.findall(r"[a-z']+", str(text).lower())


def read_rows(path):
    """Tolerant reader: splits on \\n and strips \\r, so bare-LF rows are seen.

    The CRLF-only splitter is what silently hid 40 rows of nostalgic b4925 from
    the 2026-09-20 quarantine pull. Never reintroduce it here.
    """
    with open(path, "rb") as fh:
        blob = fh.read()
    rows, bad = [], 0
    for line in blob.split(b"\n"):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line.decode("utf-8")))
        except Exception:
            bad += 1
    return blob, rows, bad


def batch_stats(rows):
    asst_words, nofunc, total_asst = [], 0, 0
    for row in rows:
        for turn in row.get("turns", []):
            if turn.get("role") != "assistant":
                continue
            toks = words(turn.get("text", ""))
            if not toks:
                continue
            total_asst += 1
            asst_words.append(len(toks))
            if not (set(toks) & FUNC):
                nofunc += 1
    n = max(1, len(asst_words))
    u0 = collections.Counter()
    for row in rows:
        for turn in row.get("turns", []):
            if turn.get("role") != "user":
                continue
            toks = words(turn.get("text", ""))
            if toks:
                u0[toks[0]] += 1
            break
    return {
        "n": len(rows),
        "words": sum(asst_words) / n,
        "nofunc": 100.0 * nofunc / n,
        "asst": total_asst,
        "u0": u0,
        "top_share": 100.0 * u0.most_common(1)[0][1] / max(1, sum(u0.values())) if u0 else 0.0,
    }


def scan(path):
    blob, rows, bad = read_rows(path)
    bare = blob.count(b"\n") - blob.count(b"\r\n")
    no_id = sum(1 for r in rows if "id" not in r)
    by_batch = collections.defaultdict(list)
    for r in rows:
        by_batch[r.get("batch_no")].append(r)
    stats = {b: batch_stats(v) for b, v in by_batch.items()}
    return {
        "path": path,
        "rows": len(rows),
        "bare": bare,
        "no_id": no_id,
        "unparseable": bad,
        "stats": stats,
    }


def verdict(st):
    """A batch is suspicious only when BOTH shape lenses trip."""
    return st["words"] < WORD_CEIL and st["nofunc"] > NOFUNC_FLOOR


def drift(st):
    """Two-sided length + opener concentration. FINDERS, not verdicts.

    Guarded at n >= 10 rows so a handful of hand samples cannot trip it. The
    low floor can fire on a legitimately terse category (sullen) -- hand-read.
    """
    if st["n"] < 10:
        return []
    out = []
    if st["words"] < DRIFT_WORD_LO:
        out.append("terse %.1f words" % st["words"])
    elif st["words"] > DRIFT_WORD_HI:
        out.append("verbose %.1f words" % st["words"])
    if st["top_share"] > OPENER_CEIL:
        out.append("one opener %.0f%%" % st["top_share"])
    return out


def report(scan_res, rows_arg=None, verbose=False):
    name = os.path.basename(scan_res["path"])
    flagged = False
    print("=" * 78)
    print("%s  %d rows" % (name, scan_res["rows"]))
    notes = []
    if scan_res["bare"]:
        notes.append("%d BARE LF (qmark.py will abort corpus-wide)" % scan_res["bare"])
    if scan_res["no_id"]:
        notes.append("%d rows with no id (bypassed add_rows.py)" % scan_res["no_id"])
    if scan_res["unparseable"]:
        notes.append("%d unparseable lines" % scan_res["unparseable"])
    if notes:
        print("  !! " + "; ".join(notes))
    if not scan_res["stats"]:
        return False

    stats = scan_res["stats"]
    clean = [s for s in stats.values() if not verdict(s)]
    if clean:
        base_words = sorted(s["words"] for s in clean)[len(clean) // 2]
        base_nofunc = sorted(s["nofunc"] for s in clean)[len(clean) // 2]
        print("  clean baseline: %.2f words, %.1f%% no-function-word (%d batches)"
              % (base_words, base_nofunc, len(clean)))
    print("  %-8s %5s %8s %9s %9s %8s  %s"
          % ("batch", "rows", "words", "noFunc%", "opener%", "id", "verdict"))
    for b in sorted(stats, key=lambda x: (x if isinstance(x, int) else 0)):
        st = stats[b]
        d = b in scan_res.get("noid_batches", ())
        bad = verdict(st)
        drifts = drift(st)
        tails = []
        if bad:
            tails.append("GENERATOR SHAPE")
            flagged = True
        if drifts:
            tails.append("DRIFT: " + ", ".join(drifts))
            flagged = True
        if d:
            tails.append("no id")
            flagged = True
        print("  %-8s %5d %8.2f %9.1f %9.1f %8s  %s"
              % ("b%s" % b, st["n"], st["words"], st["nofunc"], st["top_share"],
                 "MISSING" if d else "ok", ", ".join(tails)))
        if (bad or drifts or verbose) and st["n"]:
            print("        top openers: %s"
                  % ", ".join("%s %.0f%%" % (w, 100.0 * c / max(1, sum(st["u0"].values())))
                              for w, c in st["u0"].most_common(4)))
    return flagged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="only files whose name contains this")
    ap.add_argument("--rows", type=int, help="dump samples from this batch_no")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    names = sorted(n for n in os.listdir(RAW) if n.endswith(".jsonl"))
    if args.file:
        names = [n for n in names if args.file in n]
    if not names:
        print("no raw files matched")
        return 2

    total_bad = 0
    for name in names:
        path = os.path.join(RAW, name)
        res = scan(path)
        # batches that contain at least one door-bypassing row
        res["noid_batches"] = set()
        for line in open(path, "rb").read().split(b"\n"):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line.decode("utf-8"))
            except Exception:
                continue
            if "id" not in r:
                res["noid_batches"].add(r.get("batch_no"))
        if report(res, verbose=args.verbose):
            total_bad += 1

    if args.rows is not None:
        print("\n" + "=" * 78)
        print("samples for batch %d" % args.rows)
        for name in names:
            _, rows, _ = read_rows(os.path.join(RAW, name))
            hit = [r for r in rows if r.get("batch_no") == args.rows]
            if not hit:
                continue
            print("  %s: %d rows" % (name, len(hit)))
            for r in hit[:6]:
                print("    " + " | ".join(t.get("text", "") for t in r.get("turns", []))[:150])

    print("\n%d file(s) with findings" % total_bad)
    return 1 if total_bad else 0


if __name__ == "__main__":
    sys.exit(main())
