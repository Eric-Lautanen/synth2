#!/usr/bin/env python3
"""Dump the 63 merge rows (frame-opener + US conversion) with full text."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
us = json.load(open(os.path.join(ROOT, "audit", "changes_us_casual.json"), encoding="utf-8"))

frame = []
for ln in open(os.path.join(ROOT, "audit", "frame_opener_284.txt"), encoding="utf-8"):
    if not ln.strip() or ln.startswith("#"):
        continue
    f = ln.rstrip("\n").split("\t")
    if len(f) < 6:
        continue
    frame.append({"line": int(f[0]), "pair": int(f[2]), "noun": f[3],
                  "user": f[4], "assist": f[5]})

both = [e for e in frame if str(e["line"]) in us]
print(f"{len(both)} merge rows\n")
for e in both:
    ch = us[str(e["line"])]
    asst = ch.get("a") or {k: v for k, v in ch.items() if k.isdigit()}
    idx = sorted(asst.keys())
    print(f"L{e['line']} pair{e['pair']} idx{idx} noun={e['noun']}")
    print(f"  U: {e['user']}")
    print(f"  A: {e['assist']}")
    print(f"  -> US would be: {asst.get(str(e['pair']), '(none for this idx)')}")
