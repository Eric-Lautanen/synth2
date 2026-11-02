#!/usr/bin/env python3
"""Hand-written b2165 rewrites -> audit/changes_magpie19.json, then self-validate."""
import json

C = {
 "514": {"0": "wasn't it just, that gig on friday was brilliant from the off.",
         "1": "keep an eye on the listings, i'm in unless it's a work night."},
 "515": {"1": "start with the second one, that should sort my commute out."},
 "516": {"0": "gutting, were the headphones the expensive ones or the trusty pair?"},
 "517": {"0": "what time does the band kick off at the joiners?",
         "1": "perfect, doors at seven means we're home before the last bus."},
 "518": {"0": "no way, a whole box of old cds in the loft, anything embarrassing?",
         "1": "you have to play one of those forgotten albums next time i'm round."},
 "519": {"0": "oh no, drum lessons next door, how's the noise situation?",
         "1": "very civilized, practicing after school and stopping by six is lucky."},
 "520": {"0": "birthday shopping for a mum who buys herself everything, i know the type.",
         "1": "then a cookbook for the kitchen and a book token, thoughtful and easy."},
 "521": {"0": "ahead of schedule, all the christmas presents wrapped already, well done."},
 "522": {"0": "who did you draw in the office secret santa, someone good?",
         "1": "then ask the new guy what he drinks and buy the good one."},
 "524": {"0": "don't tell me the number, is that electricity bill the winter jump?"},
 "525": {"0": "old school, twenty quid a week in a jar, what's it for?",
         "1": "a proper holiday next summer, if you don't see the money it stays."},
 "526": {"0": "did you ring them, that insurance went up again, threaten to leave."},
 "527": {"0": "does that budgeting app actually work or does it just guilt trip you?"},
 "528": {"0": "nice one, did the old bike go for a fair price online?"},
 "529": {"0": "round two of the january promise, which gym did you join?"},
 "530": {"0": "was it the legs or the head that quit on that run?"},
 "531": {"0": "mine too, i've started resenting a wristband that tells me to stand.",
         "1": "nine hours sitting, ignoring the watch entirely is one way to win."},
 "532": {"0": "proper life skill, did changing the tyre go smoothly or was there blood?"},
 "533": {"0": "oh no, what did the car fail its mot on, big or small?",
         "1": "brake pads and a bulb is medium, at least it's driveable stuff."},
 "534": {"0": "how long is the delay on the bypass since the works started?"},
 "535": {"0": "third time this month, my internet dying again, ring them.",
         "1": "forty minutes of hold music for a restart you'd already done, classic."},
 "536": {"0": "was the phone in a case, those things survive everything now?",
         "1": "ha, careful about the screen and no case, did the phone live?"},
 "537": {"0": "twelve thousand photos is chaos, do you ever look back at them?"},
 "538": {"0": "how far into the spanish, i gave up at the word for bread?"},
 "539": {"0": "actually, what have you made in the woodwork class so far?"},
 "540": {"0": "did you try the wheel or the hand building with your sister?"},
 "541": {"0": "good on you, is the food bank volunteering sorting donations or frontline?",
         "1": "sorting and doing the tea rounds, busy but calming after a loud week."},
 "543": {"0": "is a five year old laptop worth fixing or is that the end?",
         "1": "a repair quote near the price of new, so it's the backup machine."},
 "544": {"0": "how is your daughter taking big school, has she settled?",
         "1": "she marched in without looking back and you cried in the car park."},
 "545": {"0": "was it the roadworks again, a forty minute school run is rough."},
 "548": {"0": "no nasty surprises at parents evening then, glad it went fine."},
 "549": {"0": "we need a fourth for the thursday pub quiz, are you free?"},
 "550": {"0": "can't tonight, i'm picking my mum up, but a pint tomorrow works.",
         "1": "same place at sevenish works, and i'll get the first round."},
 "551": {"0": "first sunny weekend of the year, that beer garden will be packed."},
 "552": {"0": "was it the little wine bar with the chairs that are too small?",
         "2": "surprisingly reasonable then, we're going back for the free olives."},
 "553": {"1": "ate on the seafront with coats on, still the best meal in weeks."},
 "554": {"0": "free entry at the museum this month, a good excuse to finally go."},
 "555": {"0": "good call, walking the long way home on purpose is underrated.",
         "1": "a stretch by the golf course with nobody around, that's the reset route."},
 "557": {"0": "does the washing machine still wash, mine makes a noise like that too."},
 "558": {"0": "how many bin bags did clearing out the wardrobe produce?",
         "2": "a single ice skate from a charity shop, best thing all week."},
}

path = "audit/changes_magpie19.json"
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
