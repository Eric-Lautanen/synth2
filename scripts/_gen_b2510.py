#!/usr/bin/env python3
"""Hand-written b2510 rewrites -> audit/changes_magpie17.json, then self-validate."""
import json

C = {
 "1313": {"0": "parcel meant to arrive tuesday and still not here, what does tracking say?"},
 "1314": {"0": "driver left your parcel behind the bin again, did they even knock?"},
 "1315": {"0": "takeaway turned up an hour late and cold, did you ring the restaurant?",
          "1": "rang them and they sent a fresh one without charging for the first."},
 "1316": {"0": "supermarket substituted half your order again, what did they swap this time?"},
 "1317": {"0": "delivery for next door while they were out, did you take it in?",
          "1": "sitting in the hall and you keep forgetting it, neighbourly thing to do."},
 "1318": {"0": "grocery order coming between eight and ten tonight, did you pick that slot?",
          "1": "all that was left and watching the door like a hawk, long wait."},
 "1319": {"0": "pizza place started charging for delivery, how much are they adding on?"},
 "1320": {"0": "ordered a birthday present and it arrived broken, was the box damaged?",
          "1": "box fine so packed badly, that is on them not the courier."},
 "1321": {"0": "corner shop started doing deliveries now, will they come out this far?",
          "1": "brought milk round in twenty minutes last night, quicker than expected."},
 "1322": {"0": "coffee order turned up the wrong roast, keep it or send it back?"},
 "1323": {"0": "delivery driver asked you to come down to the street, nowhere to park?"},
 "1324": {"0": "food order came with someone else's receipt, did it have their card details?",
          "1": "last four digits and their name, not great, careless of them."},
 "1325": {"0": "good mood all week for no real reason, has anything been different?",
          "1": "nothing to put your finger on but sleeping well, maybe that explains it."},
 "1326": {"0": "really annoyed at a tiny thing this morning, what set it off?"},
 "1327": {"0": "restless all day and cannot settle, is there something you are waiting on?",
          "1": "cannot sit still with anything for long, you have too much on."},
 "1328": {"0": "quite proud of yourself for finishing that course, how long did it take?"},
 "1330": {"0": "feel better after talking to your sister yesterday, what did you talk about?"},
 "1331": {"0": "avoiding a phone call you need to make, is it a tricky one?"},
 "1332": {"0": "tearful at a film last night, which one was it?",
          "1": "old one you have seen before, no idea why it got you today."},
 "1333": {"0": "a really flat couple of days, has anything helped at all?"},
 "1334": {"0": "oddly nervous about a meeting tomorrow, is it a big one?"},
 "1335": {"0": "really irritable since the clocks changed, the darker evenings do that to people."},
 "1336": {"0": "calmer after writing everything down, was it a list or a diary?"},
 "1337": {"0": "boiler making a noise like a kettle, still heating the water properly?",
          "1": "noise getting louder so you booked someone for friday, better before it stops."},
 "1338": {"0": "plumber quoted two hundred for the leak, does that include the parts?"},
 "1339": {"0": "need a new electrician after yours retired, did he recommend anyone?"},
 "1340": {"0": "painter starting on the hallway monday, how long will it take?"},
 "1341": {"0": "window firm never turned up for the measuring, was there any warning?",
          "1": "waited in all morning for nothing, annoying that, have you rung them?"},
 "1342": {"0": "second quote for the bathroom was half the price, same job or less?",
          "1": "checked the list twice, same work, so the first quote was greedy."},
 "1343": {"0": "your gutter man is retiring, will anyone take over the round?",
          "1": "son has been doing it for years, good way to hand it over."},
 "1344": {"0": "fence people want a deposit before they start, how much are they asking?"},
 "1345": {"0": "odd job man put his prices up, big rise or a little one?"},
 "1346": {"0": "chimney sweep came round this morning, was it as messy as you feared?"},
 "1347": {"0": "call back from the heating firm, have they been in touch yet?"},
 "1348": {"0": "decorator left a tin of paint behind, have you told him?"},
}

path = "audit/changes_magpie17.json"
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
