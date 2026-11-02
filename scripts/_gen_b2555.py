#!/usr/bin/env python3
"""Hand-written b2555 rewrites -> audit/changes_magpie6.json, then self-validate."""
import json

C = {
 "1381": {"0": "how long has the dog been able to open the bin for?",
          "1": "for a week of yoghurt pots, get a bin with a clip lid."},
 "1382": {"0": "was everything alright with the cat at the vet then?",
          "1": "after the jabs did she sulk, or hide under the bed?"},
 "1383": {"0": "is that the third charger the puppy has chewed this month?",
          "1": "the fourth one, a drawer is good, or try bitter spray."},
 "1384": {"0": "is the dog sitting for your sister going ok so far?",
          "1": "half five is early, does he settle again after a walk?"},
 "1385": {"0": "can you still type on the keyboard around the cat?",
          "1": "with the right side all cat, i would move it to a shelf."},
 "1386": {"0": "what is holding you back from a second dog, the cost?",
          "1": "the cost and the toys are fair worries, could you foster first?"},
 "1387": {"0": "did you get the escaped rabbit back from the garden?"},
 "1388": {"0": "does the dog do a u turn at the door in the rain?",
          "1": "carrying him down the path means the dog trains us."},
 "1389": {"0": "so the cat is on a diet for the weight, then?",
          "1": "no table treats, so who gives in first, you or the cat?"},
 "1390": {"0": "have you found any rescue dogs online that you like yet?",
          "1": "a smaller breed suits a flat, how much room have you got?"},
 "1391": {"0": "is the green fish tank down to the light or the water?",
          "1": "if the light has been on too long, try a timer on it."},
 "1392": {"0": "did you allow the dog on the bed, or did he claim it?",
          "1": "he claimed the bed, so you have lost that battle now."},
 "1393": {"0": "so what are the new neighbours like then, friendly enough?"},
 "1394": {"0": "how loud is the loft conversion from where you are?",
          "1": "drilling from eight every morning is rough, how long will it take?"},
 "1395": {"0": "have you mentioned the parking across your drive at all?",
          "1": "to avoid falling out, a polite note first, then talk."},
 "1396": {"0": "did you sleep through the upstairs party until two, then?"},
 "1397": {"0": "handy of the neighbour to lend you the ladder today.",
          "1": "he offered before you asked, worth keeping on side, gutters done?"},
 "1398": {"0": "and how does your dog take the cat in the garden?"},
 "1399": {"0": "was the note about the bins from a neighbour or the council?",
          "1": "a polite neighbour note, was it about the recycling again?"},
 "1400": {"0": "do you check in on your unwell neighbour much, then?",
          "1": "taking her a paper most mornings is kind, family nearby?"},
 "1401": {"0": "are you sad to see the neighbours moving out next month?",
          "1": "good ones are hard to lose, hoping the next lot are easy."},
 "1402": {"0": "are the boxes in the hall blocking the way at all?",
          "1": "near the fire door is worth mentioning to the building manager."},
 "1403": {"0": "does their barking dog bother you at all when you leave?",
          "1": "when you come home late, have you tried saying hello first?"},
 "1404": {"0": "how is the shared fence with next door holding up?"},
 "1405": {"0": "how many tomatoes have the plants given you so far?",
          "1": "a dozen is nice, are the plants in the ground or pots?"},
 "1406": {"0": "did the roast go wrong again, or just a bit this time?",
          "1": "setting the timer then forgetting is common, is the roast edible?"},
 "1407": {"0": "which herbs on the windowsill have you got going now?",
          "1": "mint always goes mad, have you tried the basil and mint in tea?"},
 "1408": {"0": "is the weed on the allotment bad this year, then?",
          "1": "bindweed is relentless, are you digging it out of the corner?"},
 "1409": {"0": "and how did the new bread recipe turn out today?",
          "1": "the second loaf was usually better, what did you change?"},
 "1410": {"0": "have you had a look at the dripping kitchen tap?",
          "1": "if the washer is changed and it still drips, might be the seat."},
 "1411": {"0": "what bulbs did you plant in the front bed in the end?",
          "1": "tulips and daffodils will be lovely, did you mark where they went?"},
 "1412": {"0": "are the red chillies hot ones then, or just mild?",
          "1": "scared of the chillies is fair, wear gloves when you chop them."},
 "1413": {"0": "go on then, what kind of soup did you make?",
          "1": "leek and potato is good use of the veg, does it freeze well?"},
 "1414": {"0": "is the patchy lawn down to the heat or the dog?",
          "1": "a dog doing laps round the garden does not help, reseed in autumn?"},
 "1415": {"0": "is the oven noise a humming or a clicking, then?",
          "1": "a low hum when it heats could be the fan, cooking evenly?"},
 "1416": {"0": "is there much left in the freezer to use up now?",
          "1": "two years ago is quite a dig, was anything worth keeping?"},
}

path = "audit/changes_magpie6.json"
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
