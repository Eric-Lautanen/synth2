#!/usr/bin/env python3
"""Hand-written b2345 rewrites -> audit/changes_magpie7.json, then self-validate."""
import json

C = {
 "1065": {"0": "was the post office queue for a parcel or sending something?"},
 "1066": {"0": "a cat adopts your garden and stays, that is how it works."},
 "1067": {"0": "how old is the kettle, they do not last forever?"},
 "1068": {"0": "bags and bags from the wardrobe clear out, i bet."},
 "1069": {"0": "for the stiff back, have you tried the physio exercises?"},
 "1071": {"0": "with the coffee machine broken, just use the instant instead."},
 "1072": {"0": "did you say anything about the party, or let it go?"},
 "1073": {"0": "has the council tax bill gone up again, for what exactly?"},
 "1074": {"0": "an update always lands right in the middle of your work."},
 "1075": {"0": "has your sister dropped any birthday hints at all yet?"},
 "1076": {"0": "forty minutes on the school run is a rough start, it eases."},
 "1077": {"0": "if the dog needs to lose weight, a few less treats helps."},
 "1078": {"0": "was the hall painting one coat or two in the end?"},
 "1079": {"0": "a brake light on the car mot is a cheap one at least."},
 "1080": {"0": "at least the train signal fault was not in the rain."},
 "1081": {"0": "renew the passport before the summer rush, it runs out next year."},
 "1082": {"0": "have you tried the new bakery bread yet, is it good?"},
 "1083": {"0": "was the recycling bin out in time to be emptied?",
          "1": "out at seven the night before, so ring the council about it."},
 "1084": {"0": "ours dropped out the same evening, it is so annoying.",
          "1": "if the whole road went down, just wait it out then."},
 "1085": {"0": "a case is worth it after a cracked phone screen.",
          "1": "a cheap case did nothing, worth paying more for the next one."},
 "1086": {"0": "self checkout machines do that with loose veg every single time.",
          "1": "waiting for the assistant is the worst part of it."},
 "1087": {"0": "my loyalty points are still just sitting unused at home.",
          "1": "twelve pounds off is a decent win, better than nothing."},
 "1088": {"0": "check the washing machine feet, they walk when one is missing.",
          "1": "if one foot is gone, a card under it will sort it."},
 "1089": {"0": "when did the optician last give you a glasses test?",
          "1": "four years is well overdue, no wonder things looked blurry."},
 "1090": {"0": "go on then, what happened in the weird dream last night?",
          "1": "being late for a train you cannot find is a common dream."},
 "1091": {"0": "how far out of date was the fridge milk, a day or more?"},
 "1092": {"0": "was the parking ticket for over the line or out of time?",
          "1": "two minutes over the hour is harsh, they give no leeway."},
 "1093": {"0": "did you shop around for the insurance renewal or just take it?",
          "1": "half elsewhere shows a phone call is always worth it."},
 "1094": {"0": "was the bank card text a scam or a real charge?",
          "1": "good thing the bank confirmed it early, they get clever."},
 "1095": {"0": "have you tried wiggling the headphones cable for the ear?",
          "1": "if wiggling brings it back, it is a loose wire."},
 "1096": {"0": "is the christening a big do or just close family?",
          "1": "a church hall buffet, keep expectations low and you will enjoy it."},
 "1097": {"0": "what is your son reading from the library at the moment?",
          "1": "dinosaurs phase lasts a good while, enjoy the quiet while it does."},
 "1098": {"0": "are the hostas in the garden still standing against the slugs?",
          "1": "they shredded every leaf, hostas are just their favourite, sadly."},
 "1099": {"0": "was the flat pack wardrobe build a nightmare at the weekend?",
          "1": "four hours and one missing screw, there is always one missing."},
 "1100": {"0": "what day is the tip open, or weekends at all?",
          "1": "weekdays only, so the rubbish sits in the boot all week.",
          "2": "good luck with the tip queue on your day off."},
 "1101": {"0": "any nerves about the driving lesson tomorrow, this time round?",
          "1": "better than last week is good, it gets easier honestly.",
          "2": "roundabouts are the worst at first, you will get there."},
 "1102": {"0": "did you make the platform change, or was it a sprint?",
          "1": "so it was your weekly sprint to the platform, at a run.",
          "2": "if it keeps you fit, that is one way to look at it."},
 "1103": {"0": "did you make the flight after the security queue in the end?",
          "1": "ten minutes is too close for comfort, i would be a wreck."},
 "1104": {"0": "what are they quoting for the car service this time?",
          "1": "more than last year is right, it never goes down.",
          "2": "that place by the retail park is worth a call, usually cheaper."},
}

path = "audit/changes_magpie7.json"
json.dump(C, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

lines = [l for l in open("raw/small_talk_casual.jsonl", "rb").read().split(b"\r\n") if l.strip()]
issues = []; n = 0
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
print(f"wrote {path}: rows={len(C)} replies={n}")
print("issues:", len(issues))
for it in issues: print("  ", it)
