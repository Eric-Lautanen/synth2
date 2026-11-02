#!/usr/bin/env python3
"""Hand-written b2615 rewrites -> audit/changes_magpie13.json, then self-validate."""
import json

C = {
 "1483": {"0": "dentist tomorrow morning, is it a checkup or something giving trouble?"},
 "1484": {"0": "finally registered with a doctor near the new flat, did they have space?"},
 "1485": {"0": "forty minutes past your appointment at the clinic, did they say why?"},
 "1486": {"0": "hay fever back with a vengeance this week, has the chemist anything?"},
 "1487": {"0": "blood test booked for friday, first one in years, anything worrying you?"},
 "1488": {"0": "twisted your ankle on the stairs last night, is it swollen?",
          "1": "puffy but walkable, ice pack out, keep it rested a day or two."},
 "1489": {"0": "optician said your eyes have barely changed, new glasses anyway?",
          "1": "same prescription, come back in two years unless anything shifts, cheap visit."},
 "1490": {"0": "sitting badly all week and a stiff back, desk chair or the sofa?",
          "1": "slouching on the laptop in the evening, a cushion behind you helps."},
 "1491": {"0": "had to cancel your physio because of work, was there a fee?",
          "1": "they were fine about it and rebooked you next tuesday, decent of them."},
 "1492": {"0": "flu jab at the chemist on saturday, quick job or a long queue?"},
 "1493": {"0": "waiting three weeks for a hospital letter, have you chased them?",
          "1": "rang twice, it is in the post, still nothing through the door."},
 "1495": {"0": "got a parking ticket this morning, where did you leave the car?",
          "1": "single yellow outside the shop, only in there five minutes, harsh that."},
 "1496": {"0": "passed your driving test first time today, was it the same examiner?"},
 "1497": {"0": "car making a funny noise when you brake, squealing or grinding?",
          "1": "grinding and worse off the motorway sounds like the pads to me."},
 "1498": {"0": "an hour of traffic on the ring road, accident or the usual crawl?",
          "1": "roadworks with one lane shut for resurfacing, nobody knew how to merge."},
 "1499": {"0": "free parking spot right outside for once, should have bought a lottery ticket."},
 "1500": {"0": "sat nav sent you down a farm track, useful or a dead end?",
          "1": "dead end in the dark with an unimpressed farmer watching, nightmare."},
 "1501": {"0": "nearly ran out of petrol on the way home, cutting it fine?"},
 "1502": {"0": "someone parking in your space again, have you left a note?"},
 "1503": {"0": "stuck behind a tractor for ten miles today, any chance to overtake?",
          "1": "not one straight bit long enough, so you enjoyed the view instead."},
 "1504": {"0": "insurance up forty quid this year, did you shop around first?",
          "1": "shopped around, all roughly the same, felt like a rip off either way."},
 "1505": {"0": "teaching your daughter to drive, is she getting on with the clutch ok?"},
 "1506": {"0": "roads empty at half six this morning, worth getting up early then?",
          "1": "at work before seven with a coffee in peace, sounds like a win."},
 "1507": {"0": "back at the gym after two months off, was the first session tough?",
          "1": "half your usual weights and still ached for three days, brutal first week."},
 "1508": {"0": "started swimming on your lunch break, lengths or just a paddle?"},
 "1509": {"0": "new running shoes arrived today, were they fitted properly for you?"},
 "1510": {"0": "gym raised its prices again, is it much of a rise?"},
 "1511": {"0": "first park run on saturday, what was the crowd like?",
          "1": "friendly and middle of the pack, nobody cared about the time, no pressure."},
 "1512": {"0": "pulled something in your shoulder lifting, did you warm up first?",
          "1": "straight for the heavy stuff like an idiot, we have all done it."},
 "1513": {"1": "harder than it looks and the balance ones make you wobble, that works."},
 "1514": {"0": "step counter says twelve thousand today, was that walking or running?",
          "1": "walking, the school run on foot then the shops, it adds up fast."},
 "1515": {"1": "eight of us with a coach watching your form, worth it for that."},
 "1516": {"0": "tried a pull up today and failed completely, none at all?"},
 "1517": {"0": "knees hurt after every run lately, are the shoes past their best?",
          "1": "two years and you had not thought about it until now, worth replacing."},
 "1518": {"0": "joined a five a side team at work, what position do you play?"},
}

path = "audit/changes_magpie13.json"
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
