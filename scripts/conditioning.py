#!/usr/bin/env python3
"""conditioning.py -- measure how much each assistant reply depends on its user turn.

The run-10 finding: turn_delta tracks the corpus's own conditioning. A reply that
shares ZERO content words with its own user turn teaches the model the input does
not matter. This tool measures that share so rewrites can target the worst blocks.

Usage (from the synth2 dir):
  python scripts/conditioning.py                     # whole live casual file
  python scripts/conditioning.py --file raw/small_talk_ghetto.jsonl
  python scripts/conditioning.py --worst 25          # top-N worst batches
  python scripts/conditioning.py --rows 40           # top-N worst single rows

Overlap = |content words(user turn) & content words(reply)|, content words being
lowercased word tokens minus a stopword list. A LENS IS A FINDER, NEVER A VERDICT:
hand-read hits before acting.
"""
import argparse
import json
import re
from collections import defaultdict

STOP = set("""a an the and or but if then than so as of to in on at for with from by about into over after
is are was were be been being am do does did doing have has had having i you he she it we they me him her them
my your his its our their this that these those there here what which who whom when where why how not no nor
too very can will just should now would could oh ok okay yeah hey hi uh um well really much more most
get got go going went gone do done make made""".split())


def content_words(text):
    return set(w for w in re.findall(r"[a-z']+", text.lower()) if w not in STOP and len(w) > 1)


def load_rows(path):
    return [json.loads(l) for l in open(path, "rb").read().split(b"\r\n") if l.strip()]


def pairs_of(rows):
    """Yield (row_index, row, pair_index, user_words, asst_words, asst_len)."""
    for ri, r in enumerate(rows):
        turns = r["turns"]
        for i in range(0, len(turns) - 1, 2):
            u, a = turns[i], turns[i + 1]
            if u["role"] != "user" or a["role"] != "assistant":
                continue
            yield ri, r, i // 2, content_words(u["text"]), content_words(a["text"]), len(a["text"].split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="raw/small_talk_casual.jsonl")
    ap.add_argument("--worst", type=int, default=20, help="top-N worst batches to list")
    ap.add_argument("--rows", type=int, default=0, help="top-N worst single rows to list")
    args = ap.parse_args()

    rows = load_rows(args.file)
    batch_writer = {}
    st = json.load(open("scripts/status.json", encoding="utf-8"))
    for h in st["history"]:
        batch_writer[h["batch_no"]] = h["writer"]

    pairs = list(pairs_of(rows))
    n = len(pairs)
    zero = sum(1 for p in pairs if not p[3] & p[4])
    ge2 = sum(1 for p in pairs if len(p[3] & p[4]) >= 2)
    mean_ov = sum(len(p[3] & p[4]) for p in pairs) / n
    mean_len = sum(p[5] for p in pairs) / n
    print(f"file: {args.file}  rows: {len(rows)}  pairs: {n}")
    print(f"zero-overlap: {zero / n * 100:.1f}%  >=2: {ge2 / n * 100:.1f}%  mean_ov: {mean_ov:.2f}  mean_asst_words: {mean_len:.2f}")

    by_writer = defaultdict(lambda: [0, 0, 0, 0.0, 0.0])
    for ri, r, pi, uw, aw, al in pairs:
        w = batch_writer.get(r["batch_no"], "?")
        d = by_writer[w]
        d[0] += 1
        ov = len(uw & aw)
        d[1] += ov == 0
        d[2] += ov >= 2
        d[3] += ov
        d[4] += al
    print("\nby writer:")
    for w, d in sorted(by_writer.items()):
        print(f"  {w:14s} n={d[0]:5d} zero={d[1] / d[0] * 100:5.1f}%  ge2={d[2] / d[0] * 100:5.1f}%  mean_ov={d[3] / d[0]:.2f}  mean_len={d[4] / d[0]:.2f}")

    by_batch = defaultdict(lambda: [0, 0, 0.0])
    for ri, r, pi, uw, aw, al in pairs:
        d = by_batch[r["batch_no"]]
        d[0] += 1
        d[1] += not uw & aw
        d[2] += len(uw & aw)
    worst = sorted(((v[1] / v[0], k, v[0], batch_writer.get(k, "?")) for k, v in by_batch.items() if v[0] >= 8), reverse=True)
    print(f"\nworst {args.worst} batches by zero-overlap share (min 8 pairs):")
    for z, k, cnt, w in worst[:args.worst]:
        print(f"  b{k} ({w:13s}) n={cnt:3d} zero={z * 100:5.1f}%")

    if args.rows:
        by_row = defaultdict(lambda: [0, 0])
        for ri, r, pi, uw, aw, al in pairs:
            d = by_row[ri]
            d[0] += 1
            d[1] += not uw & aw
        worst_rows = sorted(((v[1] / v[0], k) for k, v in by_row.items()), reverse=True)[:args.rows]
        print(f"\nworst {args.rows} rows by zero-overlap share:")
        for z, k in worst_rows:
            r = rows[k]
            print(f"  line {k + 1} b{r['batch_no']} ({batch_writer.get(r['batch_no'], '?')}) zero={z * 100:.0f}%")


if __name__ == "__main__":
    main()
