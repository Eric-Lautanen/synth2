#!/usr/bin/env python3
"""Dump the 221 frame-opener-ONLY violation turns with their user context, in a
form I can hand-write from. Read-only; writes audit/frame_only_dump.txt."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
wl = json.load(open(os.path.join(ROOT, "audit", "frame_only_worklist.json"), encoding="utf-8"))
rows = [json.loads(l) for l in
        open(os.path.join(ROOT, "raw", "small_talk_casual.jsonl"), "rb").read().split(b"\r\n")
        if l.strip()]

nouns = {}
for ln in open(os.path.join(ROOT, "audit", "frame_opener_284.txt"), encoding="utf-8"):
    if not ln.strip() or ln.startswith("#"):
        continue
    f = ln.rstrip("\n").split("\t")
    if len(f) >= 6:
        nouns.setdefault(int(f[0]), {})[int(f[2])] = f[3]

out = []
for line in sorted(wl, key=int):
    row = rows[int(line) - 1]
    users = [t["text"] for t in row["turns"] if t["role"] == "user"]
    asst = [t["text"] for t in row["turns"] if t["role"] == "assistant"]
    for idx in sorted(wl[line]["a"], key=int):
        i = int(idx)
        out.append(f"L{line} a{i} noun={nouns.get(int(line), {}).get(i, '?')}")
        out.append(f"   U{i}: {users[i] if i < len(users) else '?'}")
        out.append(f"   BAD: {asst[i]}")
        out.append("")
txt = "\n".join(out)
open(os.path.join(ROOT, "audit", "frame_only_dump.txt"), "w", encoding="utf-8").write(txt)
print(txt[:1500])
print(f"...\n[{len(wl)} lines / {sum(len(v['a']) for v in wl.values())} turns -> audit/frame_only_dump.txt]")
