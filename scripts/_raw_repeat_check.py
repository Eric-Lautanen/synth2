#!/usr/bin/env python3
"""Raw-level confirmation that the b2750 duplicated-question defect is gone.

Word-level mirror of the packed-split check in split_audit.py: an assistant turn
that contains a 5-gram twice is a target that teaches clause repetition.
Run:  python runs/synth2/scripts/_raw_repeat_check.py [path]
"""
import json
import re
import sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "runs/synth2/raw/small_talk_casual.jsonl"


def toks(s):
    return re.findall(r"[a-z']+", s.lower())


hits = []
rows = 0
for ln in open(PATH, encoding="utf-8"):
    ln = ln.strip()
    if not ln:
        continue
    r = json.loads(ln)
    rows += 1
    for t in r["turns"]:
        if t["role"] != "assistant":
            continue
        w = toks(t["text"])
        g = [tuple(w[i:i + 5]) for i in range(len(w) - 4)]
        if len(g) != len(set(g)):
            hits.append((r["id"], t["text"]))

print("file %s" % PATH)
print("rows %d" % rows)
print("assistant turns with an internal repeated 5-gram (word-level): %d" % len(hits))
for i, t in hits:
    print("   %s | %s" % (i, t))
