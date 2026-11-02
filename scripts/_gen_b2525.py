#!/usr/bin/env python3
"""Hand-written b2525 rewrites -> audit/changes_magpie29.json, then self-validate."""
import json

C = {
 "1349": {"0": "sensible, did the boiler service find anything before the cold snap?",
          "1": "a worn valve replaced for fifty quid, the autumn service pays off."},
 "1350": {"0": "proper job, did the chimney sweep find much on the first visit?"},
 "1351": {"0": "a proper winter fuel strategy, how much did the log store take?"},
 "1352": {"0": "good timing, was the antifreeze or the screenwash low first?",
          "1": "haha the screenwash got winter strength after you learned it the hard way."},
 "1353": {"0": "that time of year, did the summer tyres go to winters yourself?"},
 "1354": {"1": "two emails and a phone call later it was filled, persistence pays."},
 "1355": {"0": "pre season buy, wise, plastic or the metal edge on the shovel?"},
 "1356": {"0": "old person purchase, ice grippers for the shoes at last, respect.",
          "1": "walked the lane in yesterday's ice like july, the grippers win."},
 "1357": {"2": "internal clocks no vet can explain, so you coexist, half four is brutal."},
 "1358": {"0": "six thirty sunrise and no clouds, was it worth being up?"},
 "1359": {"0": "does the dog wait by the door when your alarm sounds?",
          "1": "haha half four with the tail going, the cat replaced as chief waker."},
 "1360": {"1": "held a parcel for a whole week in all weather, an unsung institution."},
 "1362": {"0": "every time, that morning bakery smell ambush gets me too."},
 "1364": {"0": "a podcast for the commute, what are you replacing the era with?"},
}

path = "audit/changes_magpie29.json"
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
