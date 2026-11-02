#!/usr/bin/env python3
"""Hand-written b2870 rewrites -> audit/changes_magpie9.json, then self-validate.
Frame law: KEEP the noun echo, VARY the frame -- never open with 'the <noun>'.
1864|1 is UNFIXABLE (user turn 'what is it?' has no content words) -> left alone."""
import json

C = {
 "1853": {"0": "week is treating me alright, busy but in the good kind of way.",
          "1": "nice that you have friday off, are you doing anything with it?",
          "2": "nothing at all sounds like a solid plan, enjoy every minute."},
 "1854": {"0": "breakfast was toast and a banana, exciting stuff i know.",
          "1": "coffee and regret still counts as breakfast on some days."},
 "1855": {"0": "kids settled into school mostly, my youngest cries at the gate.",
          "1": "it is hard, but the teacher sends a photo of him smiling later."},
 "1856": {"0": "knee is better thanks, i can walk properly again now.",
          "1": "physio helped loads, i should have gone months ago instead of hoping."},
 "1857": {"0": "watching a documentary about fishing boats, it is dead relaxing."},
 "1858": {"0": "swimming once last week, i did two lengths and felt like a champion."},
 "1859": {"0": "flatmate situation is good, she has finally learned to wash up.",
          "1": "what changed was one pointed note on the fridge, very polite."},
 "1860": {"0": "lunch is the soup place, if the queue is not mad.",
          "1": "get there before twelve then, i will leave right now actually."},
 "1861": {"0": "watched the news last night but it was all just arguing.",
          "1": "i have given up on it too, just headlines and then animals."},
 "1862": {"0": "running is going up to five k now, i nearly died at three.",
          "1": "proper progress, it does not feel like it at the time though."},
 "1863": {"0": "plan for christmas is mine this year, everyone brings a dish."},
 "1864": {"0": "still doing the crossword every day, stuck on one clue this morning.",
          "2": "chanterelle has ten letters, that is a good try though."},
 "1865": {"0": "meal out was lovely, bit loud but the food made up for it.",
          "1": "ended up at a spanish place, the patatas bravas were incredible."},
 "1866": {"0": "car washed, i did it myself and saved a tenner.",
          "1": "it did not survive the rain, it rained the second i finished."},
 "1867": {"0": "nothing new, though i have started making my own bread.",
          "1": "how's the bread going, first was a brick, third was good."},
}

path = "audit/changes_magpie9.json"
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
