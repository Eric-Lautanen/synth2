#!/usr/bin/env python3
"""Hand-written b2315 rewrites -> audit/changes_magpie22.json, then self-validate."""
import json

C = {
 "1028": {"0": "how did the first parkrun on saturday go, still standing?",
          "2": "see you down there saturday, i'll be walking the last stretch."},
 "1029": {"0": "which stretch of the river, a morning walk clears the head."},
 "1030": {"0": "any left after all that blackberry picking down the lane?",
          "2": "a scratch or two is the price of free fruit, worth it."},
 "1031": {"0": "bonfire night plans, the big display at the rec for us too.",
          "2": "deal, two hot dogs is the correct number, see you on the field."},
 "1032": {"0": "how far did the halloween decorations go this year, lights and all?"},
 "1033": {"0": "what are they showing at the outdoor cinema in the park?"},
 "1034": {"0": "brilliant, did you win anything at the bingo night for the roof fund?"},
 "1035": {"0": "same here every year, have you knocked about the hedge over the path?",
          "1": "waiting to see if she trims it before being that person, good plan."},
 "1036": {"0": "real coach or an app thing, how were the tennis lessons?"},
 "1037": {"0": "isn't bowls more of a summer thing, opened early this season?",
          "1": "ha, undefeated through october, let your dad have his autumn."},
 "1038": {"0": "are the big conkers out, season in full swing by the memorial?",
          "2": "a scientific test proving the vinegar conker beats the plain one."},
 "1039": {"0": "evidence then, autumn has properly arrived, what is the proof?"},
 "1040": {"0": "what do you do with an apple tree that went mad, cider?",
          "2": "ancient trees always outproduce the young ones, keep a jar for me."},
 "1041": {"0": "how far is the route for the saturday walking group?",
          "2": "exactly, nobody walks four miles for health alone, what time?"},
 "1042": {"0": "did you end up running a stall at the church fete again?",
          "2": "haha always rigged, the good prizes go to whoever donated them."},
 "1043": {"0": "did the neighbours come to the garage sale or total strangers?",
          "2": "a hundred and twenty quid, half the junk gone, three new neighbours."},
}

path = "audit/changes_magpie22.json"
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
