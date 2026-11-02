#!/usr/bin/env python3
"""Hand-written b2375 rewrites -> audit/changes_magpie31.json, then self-validate."""
import json

C = {
 "1125": {"0": "how bad on the scale, a trim that became a whole new haircut?",
          "1": "haha shorter than asked but the household voted, hats in the meantime."},
 "1126": {"2": "booked for thursday then, the cheapest confidence boost on the high street."},
 "1127": {"0": "lucky, are the new walking shoes comfy or need breaking in?"},
 "1128": {"0": "cheeky, a button missing after the dry cleaner, did you ring them?"},
 "1130": {"1": "five minutes at the counter for tiny tools and steady hands, fair."},
 "1131": {"0": "careful job, is the heirloom ring going up or down a size?",
          "1": "gran's ring down half a size, use careful jewellers, not a chain."},
 "1132": {"0": "haha the daily hunt for the glasses, where did they turn up?"},
 "1133": {"0": "oh no, did you miss a bin collection in the christmas shuffle?"},
 "1134": {"0": "every first tuesday, did the fire alarm make you jump your coffee?",
          "1": "coffee survived and the whole floor went quiet, one shared jump."},
 "1135": {"0": "did the wifi extender fix the dead zone or just move it?",
          "2": "a dead zone costing meetings twice a week had to go, worth it."},
 "1136": {"0": "mine does that too, a smart speaker answering questions you didn't ask."},
 "1137": {"2": "check the hose, if it's a sock you owe the vacuum an apology."},
 "1138": {"0": "same in ours, nobody irons, do you just not own wrinkly clothes?"},
}

path = "audit/changes_magpie31.json"
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
