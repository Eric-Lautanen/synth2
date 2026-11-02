#!/usr/bin/env python3
"""Hand-written b2270 rewrites -> audit/changes_magpie20.json, then self-validate."""
import json

C = {
 "921": {"0": "nightmare, four hours delayed, how did you fill the time?"},
 "922": {"0": "nerves holding up, is the driving test soon for your daughter?",
         "1": "you need the test more than she does, roundabout rules at dinner."},
 "923": {"0": "brilliant, passed first time as well, how's the insurance quote looking?",
         "1": "worth every penny, the car is hers and the bank account yours."},
 "924": {"0": "did you escape the room, or did saturday beat you?"},
 "925": {"0": "did you sing at the karaoke or spectate, good birthday?",
         "1": "a duet of that one song we all know, committed fully, brilliant.",
         "2": "even the tone deaf got applause, that tells you about the drinks."},
 "926": {"0": "what's the plan for the hen do, quiet spa or full chaos?"},
 "927": {"0": "that printer knows when you're in a hurry, three reports eaten.",
         "1": "haha printed the same document four times, that's the magic of it."},
 "928": {"0": "what triggered resetting every password on a monday, bad timing?",
         "1": "sixteen new passwords with symbols, are you using a manager now?"},
 "929": {"0": "panic mode, a cat sitter cancelling last minute before the trip?"},
 "930": {"0": "was it an automatic, a hired car for the trip north?"},
 "931": {"0": "a soft play birthday party, twelve children and one enormous ball pit."},
 "932": {"0": "what was the school play this year, any good last night?",
         "2": "your secret is safe, i cried at the school play too once."},
 "933": {"0": "did they move sports day into the shade, that heat is brutal?",
         "2": "haha the parents race, a pulled muscle you didn't know existed."},
 "934": {"0": "a civilized stag do in brighton or the traditional loss of dignity?"},
 "935": {"1": "thirty people of varying ability sounding amazing, that's what choirs are.",
         "2": "by the second song nobody listens to individuals, that's the trick."},
 "936": {"1": "right behind the goal and a fair price, three months of excitement."},
 "937": {"0": "her first tattoo, and on a saturday, how did it go?",
         "3": "haha over the phone and audibly, the mum faint is final approval."},
 "938": {"0": "big purchase, a new sofa at last, did you go soft or firm?"},
 "939": {"0": "what did you find in that goldmine of a charity shop?",
         "2": "going tomorrow morning then, the good stuff moves fast on a saturday."},
 "940": {"0": "selling or buying at the car boot sale, how was the first one?"},
 "941": {"0": "did you work from home or fight the buses through the strike?",
         "1": "two hours each way on the buses, that's a proper endurance event."},
 "942": {"0": "how far did the packing get before you gave up on the trip?",
         "1": "a half full suitcase of things you won't wear, everyone packs that way."},
 "943": {"0": "brutal, the jetlag had me awake at four making toast in the dark.",
         "1": "held on till nine after that four am toast, first human week."},
 "944": {"0": "of course, i did bring you back chocolate and a magnet.",
         "1": "proper local chocolate and not the airport version, good work.",
         "2": "best traveller you know, next trip i'll aim for a keyring then."},
 "945": {"0": "by hand or the machine, did the car take long to wash?",
         "2": "haha an hour and a half and then it rained the next morning."},
 "946": {"0": "are you watching that smart meter like a hawk now, honest?",
         "1": "turning off lights to watch the number dip, everyone does that at first."},
 "947": {"0": "god, those double glazing lads, how long did the salesman stay?"},
 "948": {"0": "from the ancient one, finally upgraded the phone, worth it?"},
 "949": {"0": "great start, a tenner on a scratch card, did you reinvest it?",
         "1": "a coffee and save the rest, that's the responsible play with a win."},
 "950": {"0": "two episodes in one sitting, that nature series is worth a sunday."},
}

path = "audit/changes_magpie20.json"
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
