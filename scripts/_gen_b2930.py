#!/usr/bin/env python3
"""Hand-written b2930 rewrites -> audit/changes_magpie18.json, then self-validate."""
import json

C = {
 "1933": {"0": "a freezing morning like that and my dog still wants out.",
          "1": "of course, a muddy puddle is a dog magnet, towel ready?"},
 "1934": {"1": "milk and one sugar, you remembered, how has the day been?",
          "2": "a long meeting that could have been an email, poor you."},
 "1935": {"2": "fed it and it bubbled overnight, that starter is tougher than it looks."},
 "1936": {"0": "three streaming services gone this year, is there any you miss?",
          "2": "resubscribe for the month it matters, that is the sensible way round."},
 "1937": {"0": "haha why have the robins picked you, of all the garden?",
          "2": "poor neighbour gets nothing, birds clearly keep score on that street."},
 "1938": {"1": "haha waiting that means no waiting, still a puzzle, did you appeal?",
          "2": "a photo at the sign is evidence enough, good luck with it."},
 "1939": {"0": "mine waits for june, so a hayfever spell this warm is early.",
          "1": "a week of gritty eyes, have you tried the own brand pollen tablets?"},
 "1940": {"1": "limescale on the heat exchanger, a rumble like that needs a plumber.",
          "2": "under a service plan, even better, boilers never fix themselves."},
 "1941": {"1": "a silent float feels wrong somehow, the clink is half the point.",
          "2": "double the supermarket, but the bottles going back makes it worth it."},
 "1942": {"0": "which shift tomorrow, the buses or the front desk at the museum?",
          "2": "a notebook is smart, thirty years of driving is history on two legs."},
 "1943": {"0": "about time, a shared tool shed fund settles whose strimmer goes missing.",
          "2": "ten quid a term covering servicing and handles, cheap at the price."},
 "1944": {"0": "number plate recognition at the leisure centre, mine does that too.",
          "2": "keep the photo evidence, the system knew the van and took the money."},
 "1945": {"2": "a new strategy every time and she counters it, she wrote the rules."},
 "1946": {"1": "short above the ears for the first time since school, brave move.",
          "2": "haha like your head lost a jumper, give it a week."},
 "1947": {"0": "did the blackcurrant jelly set on the very first attempt then?"},
 "1948": {"0": "a repair cafe at the library, ours runs the first saturday too.",
          "1": "a wobbly chair fixed with a wedge in ten minutes, pure magic.",
          "2": "better than new for a donation, i will bring my lamps next time."},
 "1949": {"0": "a driving test passed first attempt, he must be chuffed.",
          "1": "no more taxi mum duties, but the insurance quote will sting.",
          "2": "haha walked to work today, reality arrives fast but freedom is worth it."},
}

path = "audit/changes_magpie18.json"
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
