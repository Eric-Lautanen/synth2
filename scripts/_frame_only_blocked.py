#!/usr/bin/env python3
"""Find frame-only rows that CANNOT be fixed in the frame-only pass.

A frame fix must keep a shared CONTENT word with its own user turn, and the
validator forbids an AUTO term in the new text. conditioning.content_words does
no stemming, so `neighbours` != `neighbors`. Therefore a row whose noun IS a
British term has no frame-only solution: keeping the British word fails the AUTO
check, and writing the US word loses the echo.

Those rows must be routed through the US pass WITH a user-turn edit (the merge
case) -- i.e. they are victims of the plural gap in us_convert.py.

Read-only.
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import us_convert as uc          # noqa: E402
from conditioning import content_words   # noqa: E402

ROOT = os.path.normpath(os.path.join(HERE, ".."))
pairs, flags, skipped = uc.parse_lexicon(uc.LEXICON)
rx, table = uc.build_regex(pairs)
flag_terms = {b.lower() for b, _, _ in flags}

# British forms NOT in the AUTO table (from the gap scan) -- still British, so a
# US reply must not echo them.
GAP = [r"\bneighbours\b", r"\bneighbourhood\b", r"\bneighbourly\b", r"\btyres\b",
       r"\bfavourite\b", r"\bfavourites\b", r"\borganised\b", r"\bcivilisation\b",
       r"\bqueues\b", r"\bqueued\b", r"\bbiscuits\b", r"\bcolours\b", r"\bjumpers\b",
       r"\bblokes\b", r"\bprogrammes\b", r"\bfortnightly\b", r"\bhonour\b",
       r"\blabour\b", r"\bcancelled\b", r"\bdefence\b", r"\blicence\b",
       r"\bpractising\b", r"\bpractises\b", r"\bmaths\b", r"\bhoover\b",
       r"\bhoovering\b", r"\bcar park\b", r"\bwellies\b", r"\bwellingtons\b",
       r"\bdraught\b", r"\bpavement\b", r"\bautumn\b", r"\bburnt\b", r"\bskip\b",
       r"\bsellotape\b", r"\ballotment\b", r"\bdame\b"]

wl = json.load(open(os.path.join(ROOT, "audit", "frame_only_worklist.json"), encoding="utf-8"))
rows = [json.loads(l) for l in
        open(os.path.join(ROOT, "raw", "small_talk_casual.jsonl"), "rb").read().split(b"\r\n")
        if l.strip()]

blocked, clean = [], []
for line in sorted(wl, key=int):
    row = rows[int(line) - 1]
    users = [t["text"] for t in row["turns"] if t["role"] == "user"]
    for idx in sorted(wl[line]["a"], key=int):
        i = int(idx)
        u = users[i] if i < len(users) else ""
        m = rx.search(u)
        gap = next((p for p in GAP if re.search(p, u, re.I)), None)
        if m or gap:
            blocked.append((line, i, m.group(0) if m else gap, u))
        else:
            clean.append((line, i, u))

print(f"frame-only turns: {len(blocked) + len(clean)}")
print(f"  CLEAN (fixable frame-only): {len(clean)}")
print(f"  BLOCKED (user turn is British -> needs a user-turn edit too): {len(blocked)}")
print()
cnt = collections.Counter(b[2].lower() for b in blocked)
print("  blocked by term:", dict(cnt))
print()
for line, i, term, u in blocked:
    print(f"    L{line} a{i}  term={term!r}  USER={u!r}")
