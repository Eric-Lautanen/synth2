#!/usr/bin/env python3
"""dump_worklist.py -- print corpus rows in a compact form for hand rewriting.

Prints, per row: line number, batch, writer, per-pair user/assistant turns with
word counts and the content-word overlap, so the rewriter can see exactly which
replies are unconditioned (overlap 0) and how long they are. The output is a
WORKLIST, not an edit list: every rewrite is hand-written against it, then fed
to scripts/apply_rewrites.py as {"<line>": {"<asst_idx>": "new text"}}.

Usage (from the synth2 dir):
  python scripts/dump_worklist.py --batches 2210,2225
  python scripts/dump_worklist.py --lines 12,34,56
  python scripts/dump_worklist.py --worst-batches 8     # 8 worst batches
  python scripts/dump_worklist.py --file raw/small_talk_ghetto.jsonl --batches 2975
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conditioning import content_words, load_rows, pairs_of  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="raw/small_talk_casual.jsonl")
    ap.add_argument("--batches", default="")
    ap.add_argument("--lines", default="")
    ap.add_argument("--worst-batches", type=int, default=0)
    args = ap.parse_args()

    rows = load_rows(args.file)
    batch_writer = {}
    st = json.load(open(os.path.join(HERE, "status.json"), encoding="utf-8"))
    for h in st["history"]:
        batch_writer[h["batch_no"]] = h["writer"]

    want_lines = set()
    if args.lines:
        want_lines = {int(x) for x in args.lines.split(",")}
    want_batches = set()
    if args.batches:
        want_batches = {int(x) for x in args.batches.split(",")}
    if args.worst_batches:
        from collections import defaultdict
        bb = defaultdict(lambda: [0, 0])
        for ri, r, pi, uw, aw, al in pairs_of(rows):
            bb[r["batch_no"]][0] += 1
            bb[r["batch_no"]][1] += not uw & aw
        ranked = sorted(((v[1] / v[0], k) for k, v in bb.items() if v[0] >= 8), reverse=True)
        want_batches = {k for _, k in ranked[:args.worst_batches]}
        print(f"# worst {args.worst_batches} batches: {sorted(want_batches)}")

    for ri, r in enumerate(rows):
        ln = ri + 1
        if want_lines and ln not in want_lines:
            continue
        if want_batches and r["batch_no"] not in want_batches:
            continue
        if not want_lines and not want_batches:
            continue
        w = batch_writer.get(r["batch_no"], "?")
        turns = r["turns"]
        print(f"== line {ln} b{r['batch_no']} [{w}]")
        ai = 0
        for i in range(0, len(turns) - 1, 2):
            u, a = turns[i], turns[i + 1]
            uw, aw = content_words(u["text"]), content_words(a["text"])
            ov = sorted(uw & aw)
            print(f"U: {u['text']}")
            print(f"A{ai}: {a['text']}   [{len(a['text'].split())}w ov={ov}]")
            ai += 1
        print()


if __name__ == "__main__":
    main()
