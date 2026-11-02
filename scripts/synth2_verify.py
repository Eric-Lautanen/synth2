#!/usr/bin/env python3
"""Post-append verification for a synth2 raw file.

Byte-level hygiene (CRLF / ASCII / control chars) plus the structural mix the
campaign cares about (turn_structure, length_bucket, batch_no, turns/exchange).

Usage: python synth2_verify.py [small_talk_ghetto]
"""
import json
import re
import sys
from collections import Counter

RAW = r"C:\github\DBllm\runs\synth2\raw"
name = sys.argv[1] if len(sys.argv) > 1 else "small_talk_ghetto"
path = rf"{RAW}\{name}.jsonl"

CR = b"\r\n"
LF = b"\n"
raw = open(path, "rb").read()

crlf = raw.count(CR)
bare_lf = raw.count(LF) - crlf
nonascii = [(i, b) for i, b in enumerate(raw) if b > 0x7E or (b < 0x20 and b not in (9, 10, 13))]
lines = [l for l in raw.split(CR) if l.strip()]

rows = [json.loads(l) for l in lines]

print(f"file        : {path}")
print(f"rows        : {len(rows)}")
print(f"line endings: {crlf} CRLF / {bare_lf} bare LF")
print(f"non-ascii   : {len(nonascii)}")

# ---- schema / mix ------------------------------------------------------
st, lb, bn, tone, itype = Counter(), Counter(), Counter(), Counter(), Counter()
exch, bad = Counter(), []
emoji = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF]")
dashes = 0
for i, r in enumerate(rows, 1):
    c = r.get("category", {})
    st[c.get("turn_structure")] += 1
    lb[c.get("length_bucket")] += 1
    tone[c.get("tone")] += 1
    itype[c.get("interaction_type")] += 1
    bn[r.get("batch_no")] += 1
    t = [(x["role"], x["text"]) if isinstance(x, dict) else (x[0], x[1])
         for x in r["turns"]]
    exch[(len(t) + 1) // 2] += 1
    for role, text in t:
        if emoji.search(text):
            bad.append((i, "emoji"))
        if "\u2014" in text or "\u2013" in text:
            dashes += 1
        if role == "user" and text.strip().endswith("?") is False and False:
            pass
    if t[0][0] != "user" or t[-1][0] != "assistant":
        bad.append((i, "role order"))
    for j, (role, _) in enumerate(t):
        want = "user" if j % 2 == 0 else "assistant"
        if role != want:
            bad.append((i, f"alternation at turn {j}"))

words = [len(text.split()) for r in rows
         for x in r["turns"]
         for text in [(x["text"] if isinstance(x, dict) else x[1])]]
user_words = [len(text.split()) for r in rows
              for x in r["turns"]
              for role, text in [((x["role"], x["text"]) if isinstance(x, dict) else (x[0], x[1]))]
              if role == "user"]

print(f"tone        : {dict(tone)}")
print(f"itype       : {dict(itype)}")
print(f"turn_struct : {dict(st)}")
print(f"length      : {dict(lb)}")
print(f"exchanges   : {dict(sorted(exch.items()))}")
print(f"batch_nos   : {sorted(bn)}")
print(f"words       : {sum(words)} total, mean {sum(words)/len(words):.1f}/turn, "
      f"user mean {sum(user_words)/len(user_words):.1f}")
print(f"em/en dash  : {dashes}")
print(f"defects     : {bad if bad else 'none'}")

multi = st.get("short_multi_turn", 0)
print(f"\nmulti share : {multi}/{len(rows)} = {100*multi/len(rows):.1f}%  (target ~50%)")
