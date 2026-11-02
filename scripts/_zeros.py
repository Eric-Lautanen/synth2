#!/usr/bin/env python3
"""_zeros.py <batch_no> [corpus] -- print the ZERO-overlap pairs of one batch, compact.
Format: line|assistant_index|USER text|ASSISTANT text  (only pairs with empty overlap)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conditioning import content_words, load_rows, pairs_of

b = int(sys.argv[1])
corpus = sys.argv[2] if len(sys.argv) > 2 else "raw/small_talk_casual.jsonl"
rows = load_rows(corpus)
z = []
for ri, r, pi, uw, aw, al in pairs_of(rows):
    if r["batch_no"] != b: continue
    if uw & aw: continue
    z.append((ri + 1, pi))
print(f"batch {b} zero pairs: {len(z)}")
for ln, pi in z:
    ts = rows[ln - 1]["turns"]
    print(f"{ln}|{pi}|{ts[pi*2]['text']}|{ts[pi*2+1]['text']}")
