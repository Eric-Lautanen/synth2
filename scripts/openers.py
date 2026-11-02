#!/usr/bin/env python3
"""openers.py -- per-batch first-word audit of assistant turns.

The run-11 finding: the conditioning campaign's echo pattern over-used
"the <noun>..." openers, the corpus the-opener rose 8.1% -> 13.4%, and the
model followed (6.7% -> 13.2%, over the 12% ceiling). This tool finds where
openers concentrate so re-heading can target the worst batches.

Usage (from the synth2 dir):
  python scripts/openers.py                          # per-batch "the" share
  python scripts/openers.py --word the --top 20      # another first word
  python scripts/openers.py --list b2210             # dump the-opener turns of a batch
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conditioning import load_rows  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="raw/small_talk_casual.jsonl")
    ap.add_argument("--word", default="the")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--list", default="", help="batch number: dump that batch's hits")
    args = ap.parse_args()

    rows = load_rows(args.file)
    hits = {}
    tot = {}
    for ri, r in enumerate(rows):
        b = r["batch_no"]
        tot[b] = tot.get(b, 0) + 0
        for k, t in enumerate(r["turns"]):
            if t["role"] != "assistant":
                continue
            tot[b] = tot.get(b, 0) + 1
            w = t["text"].split()
            if w and w[0].lower() == args.word:
                hits.setdefault(b, []).append((ri + 1, k // 2, t["text"]))

    n_all = sum(tot.values())
    n_hit = sum(len(v) for v in hits.values())
    print(f"file: {args.file}  assistant turns: {n_all}  '{args.word}'-openers: {n_hit} ({n_hit / n_all * 100:.1f}%)")

    if args.list:
        b = int(args.list)
        for ln, ai, text in hits.get(b, []):
            print(f"  L{ln} A{ai}: {text}")
        return

    ranked = sorted(((len(hits.get(b, [])) / n, b) for b, n in tot.items() if n >= 16), reverse=True)
    print(f"\nworst {args.top} batches by '{args.word}'-opener share (min 16 turns):")
    for z, b in ranked[:args.top]:
        print(f"  b{b}  {z * 100:5.1f}%  ({len(hits.get(b, []))}/{tot[b]})")


if __name__ == "__main__":
    main()
