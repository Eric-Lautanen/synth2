#!/usr/bin/env python3
"""Verify the 284 frame-opener list against its OWN definition.

The lens claims: "this assistant reply opens with `the <noun>`". A lens is a
finder, never a verdict -- so re-derive each row independently from the live
corpus and check (a) the assistant really does open `the <word>`, (b) <word> is
really a content word shared with its own user turn, and (c) whether <word> is
actually the NOUN or just the adjective in front of it (the label may be loose
while the fix is still right).

Read-only.
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from conditioning import content_words          # noqa: E402

ROOT = os.path.normpath(os.path.join(HERE, ".."))
LIST = os.path.join(ROOT, "audit", "frame_opener_284.txt")
RAW = os.path.join(ROOT, "raw", "small_talk_casual.jsonl")

# Words that are content words by the instrument's definition but are NOT nouns;
# if one lands in the noun slot the LABEL is loose (the fix still applies).
NOT_A_NOUN = {"new", "old", "same", "other", "last", "first", "next", "own",
              "one", "thing", "way", "time", "rest", "lot", "bit", "kind", "sort",
              "point", "matter", "whole", "left", "right", "best", "worst"}


def words(t):
    return re.findall(r"[a-z']+", t.lower())


rows = [json.loads(l) for l in open(RAW, "rb").read().split(b"\r\n") if l.strip()]

entries = []
for ln in open(LIST, encoding="utf-8"):
    if not ln.strip() or ln.startswith("#"):
        continue
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6:
        continue
    entries.append({"line": int(f[0]), "batch": f[1], "pair": int(f[2]),
                    "noun": f[3], "user": f[4], "assist": f[5]})

print(f"list rows: {len(entries)}")

bad_open = bad_share = bad_text = 0
loose = collections.Counter()
noun_counts = collections.Counter()

for e in entries:
    r = rows[e["line"] - 1]
    turns = r["turns"]
    # re-derive the pair independently
    ui = 2 * e["pair"]
    if ui + 1 >= len(turns) or turns[ui]["role"] != "user" or turns[ui + 1]["role"] != "assistant":
        bad_text += 1
        continue
    u, a = turns[ui]["text"], turns[ui + 1]["text"]
    if u != e["user"] or a != e["assist"]:
        bad_text += 1
        continue
    aw = words(a)
    if not (len(aw) >= 2 and aw[0] == "the"):
        bad_open += 1
        continue
    if aw[1] != e["noun"].lower():
        bad_open += 1
        continue
    if aw[1] not in content_words(u):
        bad_share += 1
        continue
    noun_counts[e["noun"]] += 1
    if e["noun"] in NOT_A_NOUN:
        loose[e["noun"]] += 1

print(f"  re-derived text mismatch (line/pair points at different text): {bad_text}")
print(f"  does NOT actually open `the <noun>`                           : {bad_open}")
print(f"  <noun> not a shared content word of its own user turn          : {bad_share}")
ok = (bad_text == 0 and bad_open == 0 and bad_share == 0)
print(f"  => LENS {'VALID' if ok else 'HAS FALSE POSITIVES'} on {len(entries) - bad_text - bad_open - bad_share} rows")
print()
print(f"loose labels (the slot holds a determiner/adjective, not the noun): {sum(loose.values())}")
for k, v in loose.most_common(12):
    print(f"   {v:4d}  {k}")
print()
print("most common nouns in the list:")
for k, v in noun_counts.most_common(12):
    print(f"   {v:4d}  {k}")
