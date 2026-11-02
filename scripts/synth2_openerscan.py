#!/usr/bin/env python3
"""synth2 opener scan -- the instrument that catches the drift no gate can see.

Usage:
    python synth2_openerscan.py <batch.json|batch.txt> [live_file]

No live_file -> compare against the CORPUS AGGREGATE (all raw/*.jsonl), which is
the right reference for the first batch of a fresh file. Pass a sibling file
name to compare against that register instead.

Prints, for EVERY turn position, the first-word histogram of the batch next to
the same histogram for the live file the batch is about to join, and flags any
word the batch over-uses.

Why this exists
---------------
Three consecutive batches for `small_talk_angry` pre-flighted CLEAN and passed
`repair`, `verify` and `qmark`, and each one was a template in the one place
nobody looks:

    3155   82% of closers opened on the literal token `then `   (file: 17%)
    3185   89% of user turns opened on `the`                    (file: 57.5%)
    3200   84% of user turns opened on `the`  AND
           57% of 4-turn assistant turns opened on `did`        (file: 3.7%)

Every one of those was found only by counting the first word of every turn and
comparing it to the LIVE FILE, never to zero. Run this on the BUILT batch, before
the pre-flight, and again after every fix pass -- fixing one template reliably
surfaces the next (3200 traded `did you ...?` for `a X is a Y` and needed four
passes).

Reading the output
------------------
`OVER` marks a word the batch uses at more than `--ratio` times the live rate
AND above `--floor` absolute share -- a word can be 5x the live rate and still
be fine if the live rate is 0.2%. The absolute share is what a reader notices.
Turn positions that are too rare in the live file to give a stable rate are
marked `(n<30)`; use judgement there rather than the ratio.
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

RAW_DIR = r"C:\github\DBllm\runs\synth2\raw"
STOP = {"", "the", "a", "an", "i", "you", "it", "and", "to", "of", "in", "is", "was"}


def first_word(text):
    m = re.findall(r"[a-z0-9']+", text.lower())
    return m[0] if m else ""


def load(path):
    """Accept a built batch (.json array, or .jsonl), or a text batch
    (.txt, one row per line, turns split on ` | `)."""
    low = path.lower()
    if low.endswith(".jsonl"):
        rows = []
        for line in open(path, encoding="utf-8"):
            if line.strip():
                rows.append([t["text"] for t in json.loads(line)["turns"]])
        return rows
    if low.endswith(".json"):
        data = json.load(open(path, encoding="utf-8"))
        return [[t["text"] if isinstance(t, dict) else t[1] for t in row["turns"]]
                for row in data]
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line:
            rows.append([p.strip() for p in line.split(" | ")])
    return rows


def histogram(rows, pos):
    c = collections.Counter()
    n = 0
    for r in rows:
        if len(r) > pos:
            c[first_word(r[pos])] += 1
            n += 1
    return c, n


def role_of(pos):
    return "user" if pos % 2 == 0 else "assist"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch")
    ap.add_argument("live", nargs="?", default=None,
                    help="sibling file name or path; default: the corpus aggregate")
    ap.add_argument("--ratio", type=float, default=3.0,
                    help="flag when batch share > ratio x live share (default 3.0)")
    ap.add_argument("--floor", type=float, default=8.0,
                    help="ignore flags under this absolute share, %% (default 8.0)")
    ap.add_argument("--top", type=int, default=8)
    a = ap.parse_args()

    live_path = a.live
    if not live_path:
        # TRAP (fixed 2026-09-25): the default used to be `sorted(...)[0]`, i.e.
        # small_talk_angry.jsonl -- one arbitrary sibling, while the help text
        # promised "the CURRENT file per add_rows.py". That silently compared a
        # fresh batch against a register it was not joining and reported phantom
        # OVER flags (angry uses `then`/`a` at pos3 far more than the corpus).
        # The honest fallback is the corpus aggregate, which is exactly what
        # synth2_build.py scan (b) uses when the target file has no rows yet, so
        # the two instruments now agree.
        live_path = None
    elif not os.path.isabs(live_path):
        live_path = os.path.join(RAW_DIR, live_path)
        if not os.path.splitext(live_path)[1]:
            live_path += ".jsonl"

    batch = load(a.batch)
    if live_path:
        live = load(live_path)
        label = live_path
    else:
        live = []
        for f in sorted(glob.glob(os.path.join(RAW_DIR, "*.jsonl"))):
            live.extend(load(f))
        label = "corpus aggregate (all raw/*.jsonl)"
    print(f"batch: {a.batch}  ({len(batch)} rows)")
    print(f"live : {label}  ({len(live)} rows)")

    positions = sorted({len(r) - 1 for r in batch} | {len(r) - 1 for r in live})
    flagged = 0
    for pos in range(0, max(positions) + 1):
        bc, bn = histogram(batch, pos)
        lc, ln = histogram(live, pos)
        if bn == 0:
            continue
        label = f"{role_of(pos):<6} turn {pos}"
        note = "" if ln >= 30 else f"  (live n={ln}, rate unstable)"
        print(f"\n--- {label}   batch n={bn}{note}")
        for word, k in bc.most_common(a.top):
            bshare = 100 * k / bn
            lshare = 100 * lc.get(word, 0) / ln if ln else 0.0
            flag = ""
            if (lshare > 0 and bshare > a.ratio * lshare and bshare >= a.floor) or \
               (lshare == 0 and bshare >= a.floor):
                flag = "  <-- OVER"
                flagged += 1
            print(f"    {word:<12} {k:>4}  {bshare:5.1f}%   live {lshare:5.1f}%{flag}")

    print(f"\nflagged positions: {flagged}")
    if flagged:
        print("Rewrite by LINE NUMBER in the text batch, then re-run this scan.")
        print("Do not fix one template by introducing another -- check the NEW top "
              "word after every pass.")
    else:
        print("every turn position matches the live file's shape.")


if __name__ == "__main__":
    main()
