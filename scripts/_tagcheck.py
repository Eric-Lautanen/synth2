#!/usr/bin/env python3
"""Throwaway: verify trailing-tag surfaces after the generator fix."""
import collections
import json

for fn in ("gen/ranting_worked.jsonl", "gen/ranting_compose.jsonl"):
    rows = [json.loads(l) for l in open(fn, "rb").read().split(b"\r\n") if l.strip()]
    c = collections.Counter()
    for r in rows:
        u = r["turns"][0]["text"].strip()
        body = u.rstrip(".!?")
        if "," in body:
            c[body.split(",")[-1].strip() + " |" + u[-1]] += 1
    print("==", fn)
    for k, v in c.most_common(8):
        print("   %5d  %r" % (v, k))
