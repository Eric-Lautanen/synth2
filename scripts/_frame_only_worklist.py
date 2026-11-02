#!/usr/bin/env python3
"""Build the worklist for the FRAME-OPENER-ONLY rows: the 284 violations minus
the 63 that already ride the US conversion (audit/changes_us_merged.json).

Those 63 are DONE (audit/frame_merge_fixes.json -> changes_us_merged.json). What
is left is every violation line whose line number is NOT in the US change list.

Read-only. Writes audit/frame_only_worklist.json in the exact shape
apply_rewrites.py's compile_changes accepts:

    {"<line>": {"a": {"<assistant_idx>": ""}}}   <- blank = hand-write here

A line can carry TWO violation turns (19 lines in the full 284 do), so this
groups by line FIRST and blanks every violation turn, exactly like the merge
worklist builder -- a flattened dump would silently leave the second turn broken.

Also verifies, against the live corpus text, that the assistant index in the
284 file really is the assistant-list index for that row (the column that was
WRONG in my first dump and right in the raw file).
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import us_convert as uc                                   # noqa: E402

# British forms NOT in the AUTO table but still British: if the PAIRED USER turn
# carries one, the assistant cannot echo a US reply, so that row needs a merged
# user+assistant edit. (conditioning.content_words does no stemming, so
# `neighbours` != `neighbors`.)
GAP = [r"\bneighbours\b", r"\bneighbourhood\b", r"\bneighbourly\b", r"\btyres\b",
       r"\bfavourite\b", r"\bfavourites\b", r"\borganised\b", r"\bcivilisation\b",
       r"\bqueues\b", r"\bqueued\b", r"\bbiscuits\b", r"\bcolours\b", r"\bjumpers\b",
       r"\bblokes\b", r"\bprogrammes\b", r"\bfortnightly\b", r"\bhonour\b",
       r"\blabour\b", r"\bcancelled\b", r"\bdefence\b", r"\blicence\b",
       r"\bpractising\b", r"\bpractises\b", r"\bmaths\b", r"\bhoover\b",
       r"\bhoovering\b", r"\bcar park\b", r"\bwellies\b", r"\bwellingtons\b",
       r"\bdraught\b", r"\bpavement\b", r"\bautumn\b", r"\bburnt\b", r"\bskip\b",
       r"\bsellotape\b", r"\ballotment\b"]
_pairs, _flags, _sk = uc.parse_lexicon(uc.LEXICON)
_rx, _table = uc.build_regex(_pairs)

ROOT = os.path.normpath(os.path.join(HERE, ".."))

merged = json.load(open(os.path.join(ROOT, "audit", "changes_us_merged.json"),
                        encoding="utf-8"))
raw = open(os.path.join(ROOT, "raw", "small_talk_casual.jsonl"), "rb").read()
rows = [json.loads(l) for l in raw.split(b"\r\n") if l.strip()]

frame = []
for ln in open(os.path.join(ROOT, "audit", "frame_opener_284.txt"), encoding="utf-8"):
    if not ln.strip() or ln.startswith("#"):
        continue
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6:
        continue
    frame.append({"line": int(f[0]), "pair": int(f[2]), "noun": f[3],
                  "user": f[4], "assist": f[5]})

by_line = {}
for e in frame:
    by_line.setdefault(e["line"], []).append(e)

out = {}
report = []
for ln in sorted(by_line):
    if str(ln) in merged:
        continue                      # the merge half already owns this line
    entries = by_line[ln]
    row = rows[ln - 1]
    asst = [t["text"] for t in row["turns"] if t["role"] == "assistant"]
    user = [t["text"] for t in row["turns"] if t["role"] == "user"]
    entry = {"a": {}}
    for e in entries:
        entry["a"][str(e["pair"])] = ""            # blank -> hand-write
        ok = e["pair"] < len(asst) and asst[e["pair"]] == e["assist"]
        report.append((ln, e["pair"], e["noun"], ok, len(row["turns"]),
                       e["user"], e["assist"]))
        # merged case: the paired USER turn is itself British -> needs a US edit
        i = e["pair"]
        u = user[i] if i < len(user) else ""
        if _rx.search(u) or any(re.search(p, u, re.I) for p in GAP):
            entry.setdefault("u", {})[str(i)] = ""
    out[str(ln)] = entry

p = os.path.join(ROOT, "audit", "frame_only_worklist.json")
with open(p, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)

print(f"wrote {p}")
print(f"  lines: {len(out)}   violation turns: {len(report)}")
bad = [r for r in report if not r[3]]
print(f"  violation-turn index verified against the corpus: "
      f"{len(report) - len(bad)}/{len(report)}")
if bad:
    print("  MISMATCHES:", bad[:5])
two = [ln for ln, es in by_line.items() if len(es) > 1 and str(ln) not in merged]
print(f"  lines with TWO violation turns (frame-only): {len(two)}  {sorted(two)}")
print()
print("  L    idx noun          turns  USER -> (bad) ASSISTANT")
for r in report[:12]:
    print(f"  {r[0]:<5d} {r[1]}  {r[2]:<12s}  {r[4]}   {r[5]!r}")
    print(f"        {'':<12s}      {r[6]!r}")
