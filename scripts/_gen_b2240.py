#!/usr/bin/env python3
"""Hand-written b2240 rewrites -> audit/changes_magpie23.json, then self-validate."""
import json

C = {
 "801": {"0": "how long did the passport renewal take, finally arrived then?"},
 "802": {"0": "was it the york hotel with the four poster beds, lovely?",
         "2": "full english and proper coffee, ate enough to skip lunch entirely."},
 "803": {"0": "do you still need players, i've missed five a side since the break?"},
 "804": {"0": "you, joined a running club, the taxi to the shop person?",
         "1": "more of a chat with light jogging, the best kind of club.",
         "2": "by the park gates on tuesdays, i might join you one week."},
 "805": {"2": "week two is where i peaked, that's the encouragement you need."},
 "806": {"0": "what's the order, chippy tea on a decided whim tonight?"},
 "807": {"0": "really, the chippy near the station gone downhill, that is a shame."},
 "808": {"2": "a literary one about a family falling apart, bleak but good."},
 "809": {"0": "show off, three books ahead of your reading target, best one so far?"},
 "810": {"0": "oh no, the bookshop closing down, that place has been there forever."},
 "811": {"0": "worse or just different, has the glasses prescription changed much?",
         "1": "slightly worse, blamed on screens or on being forty, fair enough."},
 "812": {"0": "for your sister's sake, a drum kit at christmas, hope she says no.",
         "1": "haha electronic with headphones, the family survives and he's happy."},
 "813": {"0": "big fancy do or the village hall, cousin's wedding in june?",
         "2": "then you're covered, a mum as stylist knows what suits you."},
 "814": {"0": "ten years, isn't it, what's the plan for the anniversary next week?"},
 "815": {"0": "was the leaving do emotional, margaret retiring from accounts then?"},
 "816": {"0": "are you doing the induction for the new starter on monday?",
         "2": "coffee move works every time, that's how you survived week one."},
 "817": {"0": "how late did the work night out go, out of hand then?",
         "2": "stays at a temperature nobody likes forever, same row next year."},
 "818": {"0": "what's your chess rating, be honest, playing online at lunch?"},
 "819": {"0": "any good birds, up at six to watch the garden, dedication?"},
 "820": {"0": "what's visiting the bird feeders, paying off nicely this winter?",
         "1": "a gang of twelve long tailed tits and a robin that bullies everyone."},
 "821": {"0": "how's the knitting going with your aunt, any scarves yet?"},
 "822": {"0": "a secondhand guitar, the midlife instrument move, how bad does it sound?",
         "2": "fingertips filing complaints already, they'll unionise if you keep this up."},
 "823": {"0": "how's the puppy doing at training class, terror or star?"},
 "824": {"0": "impressive, the dog shaking a paw, what's next in the repertoire?"},
 "826": {"0": "fostering a guide dog puppy for six weeks, heartbreak at the end.",
         "1": "enjoy the handover day and cry later, that's a good way."},
 "827": {"0": "air in the system, have you bled the radiators before, gurgling again?",
         "1": "watched a video and bought the key, tonight is the night then."},
 "828": {"0": "before you call anyone, has the kitchen drain had the soda trick?",
         "2": "dignity is your most disposable resource, then the drain snake it is."},
 "829": {"0": "oh classic, fell asleep in the sun, how red are we talking?",
         "1": "nose and shoulders, a person who makes poor choices, that is fair."},
 "830": {"0": "was the car iced up, first frost of the year this morning?",
         "1": "proper iced, scrapers out and the breath doing the full fog routine."},
 "831": {"0": "snow for the weekend, i'll get the sled out if it settles."},
 "832": {"0": "was the drive to the reservoir worth it, picnic in hand?"},
 "833": {"0": "are you going then, the wedding rsvp came through at last?",
         "1": "a plus one means clear your saturday, count me in for the meal."},
 "834": {"0": "nightmare job, that seating plan, good luck with the politics."},
 "835": {"0": "oh no, a whole family group chat, how bad is it?",
         "1": "sixty messages before nine and half about a dog video, chaos."},
 "836": {"0": "nice one, did the kitchen cupboards hide ancient things at the back?"},
 "838": {"0": "a chirping smoke alarm all night is maddening in the dark.",
         "1": "couldn't find which alarm it was for an hour, they coordinate."},
}

path = "audit/changes_magpie23.json"
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
