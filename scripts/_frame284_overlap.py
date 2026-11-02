#!/usr/bin/env python3
"""Which of the 284 frame-opener rows ALSO carry a US conversion? (Fable #726 item 3:
merge those into ONE rewrite.) Read-only."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))

us = json.load(open(os.path.join(ROOT, "audit", "changes_us_casual.json"), encoding="utf-8"))
us_lines = {int(k) for k in us}

frame = []
for ln in open(os.path.join(ROOT, "audit", "frame_opener_284.txt"), encoding="utf-8"):
    if not ln.strip() or ln.startswith("#"):
        continue
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6:
        continue
    frame.append({"line": int(f[0]), "batch": f[1], "pair": int(f[2]),
                  "noun": f[3], "user": f[4], "assist": f[5]})

both = [e for e in frame if e["line"] in us_lines]
only_frame = [e for e in frame if e["line"] not in us_lines]
print(f"284 rows: {len(frame)}")
print(f"  ALSO in the US change list (MERGE into one rewrite): {len(both)}")
print(f"  frame-opener only                                  : {len(only_frame)}")
print()
print("the merge set, with the US edit that shares the row:")
for e in both[:40]:
    ch = us[str(e["line"])]
    asst = ch.get("a", ch) if isinstance(ch, dict) else {}
    print(f"  L{e['line']} b{e['batch']} pair{e['pair']} noun={e['noun']}")
    print(f"     US edit present for asst idx: {sorted(asst.keys())}")
print(f"  ... ({len(both)} total)")
