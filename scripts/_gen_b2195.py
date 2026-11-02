#!/usr/bin/env python3
"""Hand-written b2195 rewrites -> audit/changes_magpie21.json, then self-validate."""
import json

C = {
 "632": {"0": "has it been two years since the optician, thursday sneaks up.",
         "1": "putting it off for three years, no wonder your eyes blur at night."},
 "633": {"0": "is the new takeaway any good, corner places are hit or miss?"},
 "634": {"0": "your dad's team doing well, cricket all weekend in the house?",
         "1": "haha nobody else gets the channel until monday, the seasonal takeover."},
 "635": {"1": "grown men in fancy dress and the commentary is pure drama, brilliant."},
 "636": {"0": "muddy fields or proper showers, festival tickets for june then?"},
 "637": {"0": "swimming twice a week since may, best part of my summer day.",
         "1": "bed always wins, come join me at the lido on a saturday."},
 "638": {"0": "you're joking, a parking ticket outside your own house, the cheek.",
         "2": "ha, forty quid says they say no, then you get to be annoyed."},
 "639": {"0": "where did the keys turn up, a full day is a long panic?"},
 "640": {"0": "is it the one who sprints between cars, relentless warden?"},
 "641": {"0": "classic umbrella death in the wind, how old was it?"},
 "642": {"0": "did you find shelter from the downpour or just accept the soaking?",
         "1": "ten minutes under a bakery awning with strangers, that's solidarity.",
         "2": "one man said well this is nice and we all laughed, comedy gold."},
 "643": {"0": "how did the first cycle to work go, was the morning kind?"},
 "644": {"1": "haha everyone watched you struggle past the pub, the walk of shame."},
 "645": {"0": "what was the film, a proper movie night with blankets sounds ideal?",
         "1": "haha fell asleep at the good bit, the blanket coma gets everyone."},
 "646": {"0": "what are we playing at game night, i'm owed a trivia rematch."},
 "647": {"0": "did you catch anything fishing with your uncle on sunday?",
         "1": "two tiddlers and six hours of silence, that was the part you needed."},
 "648": {"1": "took home one and returned two, technically winning, that's control."},
 "649": {"0": "how many spare screws are left after the flat packed bookshelf?"},
 "650": {"0": "full tour then, parents visiting means rooms cleaned and food planned?"},
 "651": {"0": "did the weather hold for the bbq, sounds like a saturday success?"},
 "652": {"0": "just because, a plate of scones from the neighbour, no reason?",
         "1": "now you owe her a favour of unknown size, probably the recycling bins."},
 "653": {"0": "how's that going, a week at the kitchen table, back holding up?"},
 "654": {"0": "proper monitor and everything, the home office setup sounds done."},
 "655": {"0": "candles and cold beans, a power cut during dinner is a classic.",
         "1": "playing cards by torchlight, funny how a power cut forces a good night."},
 "656": {"0": "paper ones or the digital mountain, photo albums are a project."},
}

path = "audit/changes_magpie21.json"
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
