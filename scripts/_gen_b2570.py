#!/usr/bin/env python3
"""Hand-written b2570 rewrites -> audit/changes_magpie28.json, then self-validate."""
import json

C = {
 "1419": {"0": "real craft, the reduced section, what did the yellow sticker reward?"},
 "1420": {"0": "a slow accumulation strategy, how long did the loyalty points take?"},
 "1421": {"0": "great substitution experiment, did the own brand beans drop in price?",
          "2": "haha some things earn their brand premium, there is always one."},
 "1423": {"0": "proper returns counter nerves, did they ask questions about the coat?",
          "1": "one question and a receipt, money back in two days, dread for nothing."},
 "1424": {"0": "chatted at by the self checkout, what did it actually say?"},
 "1425": {"0": "a good letter for once, how much did the direct debit drop?",
          "1": "eleven pounds straight into savings before it is missed, clever."},
 "1427": {"0": "better late than never, an ISA at thirty eight is still early."},
 "1428": {"0": "premium bonds as an experiment, have you won anything yet?",
          "1": "your aunt wins twenty quid twice a year, so the odds exist."},
 "1429": {"0": "an extended warranty is usually a waste, what changed your mind?"},
 "1430": {"0": "cashback finally paying out, how much had the site built up?",
          "2": "two years of clicking for one food shop, a small tax rebate."},
 "1431": {"2": "one paid the lot and we all transferred her, the modern way."},
}

path = "audit/changes_magpie28.json"
json.dump(C, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

lines = [l for l in open("raw/small_talk_casual.jsonl", "rb").read().split(b"\r\n") if l.strip()]
issues = []; n = 0; the_op = []
for key, ch in C.items():
    ln = int(key)
    row = json.loads(lines[ln - 1])
    asst = [t for t in row["turns"] if t["role"] == "assistant"]
    for idx, txt in ch.items():
        i = int(idx); n += 1
        w = len(txt.split())
        if not (10 <= w <= 13): issues.append((ln, i, "wordcount", w, txt))
        if any(ord(c) > 127 for c in txt): issues.append((ln, i, "nonascii", txt))
        if any(d in txt for d in ["\u2013", "\u2014", "\u2012", "\u2015"]): issues.append((ln, i, "dash", txt))
        if "-" in txt: issues.append((ln, i, "hyphen", txt))
        if any(0x2600 <= ord(c) <= 0x1FAFF for c in txt): issues.append((ln, i, "emoji", txt))
        if i >= len(asst): issues.append((ln, i, "index-oob", len(asst)))
        if txt.lower().startswith("the "): the_op.append((ln, i, txt))
print(f"wrote {path}: rows={len(C)} replies={n}")
print("issues:", len(issues))
for it in issues: print("  ", it)
print("the-openers:", len(the_op))
for it in the_op: print("  ", it)
