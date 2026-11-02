#!/usr/bin/env python3
"""Hand-written b2945 rewrites -> audit/changes_magpie16.json, then self-validate."""
import json

C = {
 "1950": {"0": "loft hatch open all week, did much warmth escape the house?",
          "1": "bedroom an icebox so plenty, at least your husband goes up the loft.",
          "2": "took the ladder away as a protest, one way to stop being asked.",
          "3": "shut within the hour and the bedroom habitable again, victory at last."},
 "1951": {"0": "tried a new bakery on the high street, what did you pick up?",
          "2": "croissant was worth it, the wait was not, go at seven next time."},
 "1952": {"0": "recycling collection changed colour, blue bin only now, what about the green ones?",
          "1": "collected separately since the council split the contract, nobody told you.",
          "2": "two weeks running and the neighbours very patient, they did not report you."},
 "1953": {"0": "front door lock sticking every damp morning, try graphite powder not oil.",
          "1": "opposite of what you assumed, any hardware shop, a few quid for graphite."},
 "1954": {"0": "neighbour's kid started a car washing round, how much is he charging?",
          "2": "saturday morning and the car not that clean since last summer, good lad."},
 "1955": {"0": "chimney smoke from next door already, they are keen, it is barely october.",
          "2": "lovely and the woodpile stacked in september, they deserve the smoke."},
 "1956": {"1": "boiling water trick versus citric acid, mine preferred the citric acid treatment.",
          "2": "worth a go before buying new, a fiver of descaler saves forty quid."},
 "1957": {"0": "winter duvet out of the vacuum bags, the changeover weekend, a milestone.",
          "1": "smells of the loft, a day on the line sorts it, drying weather?"},
 "1958": {"0": "lost the tv remote for three days, how did you survive?"},
 "1959": {"0": "clock change next weekend and already dreading it, dark afternoons are the worst.",
          "1": "night by half four so a daylight lamp, do they actually work?"},
 "1960": {"1": "asked to join the teachers' team, intimidating, they will have all the answers.",
          "2": "geography teacher put lisbon in spain last year, legendary, you could win."},
 "1961": {"0": "car booked for its mot four days before, cutting it fine.",
          "2": "next week and both bulbs and the wiper replaced, veteran owner strategy."},
 "1962": {"0": "daughter wants to learn the guitar, how old is she?"},
 "1963": {"1": "four buttons and none labelled, manual in a drawer somewhere, ours too."},
 "1964": {"0": "mum doing her christmas shopping already in october, she does this every year.",
          "1": "everything wrapped by november, she calls it stress avoidance, sounds like wisdom.",
          "2": "never noticing the cost in small slices, there is a lesson in that."},
 "1965": {"0": "fog came down thick this morning, was it the same your way?",
          "1": "forty metres visibility on the bypass, everyone crawling together, oddly calm.",
          "2": "gone by ten like it was never there, the whole morning a dream."},
}

path = "audit/changes_magpie16.json"
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
