#!/usr/bin/env python3
"""Hand-written b2360 rewrites -> audit/changes_magpie26.json, then self-validate."""
import json

C = {
 "1105": {"1": "haha the invisible glass stage, it lasts three days before rain evens it.",
          "2": "haha rains within the week every time, a scheduling genius, that."},
 "1106": {"0": "after how long of the sheets situation, curtains at last?"},
 "1108": {"0": "least glamorous job going, how thick did the loft insulation go?",
          "1": "haha two hundred millimetres in the dark, your arms won't forgive you.",
          "2": "recovering under the duvet is part of the job description, fair."},
 "1109": {"0": "a draught under the back door, brush strip or the old sausage dog?"},
 "1110": {"0": "do you actually stand at the standing desk or just rest coffee?",
          "2": "secondhand for ninety quid and the motor works, well earned."},
 "1111": {"2": "four hundred quid and a fishing trip fund, nineteen years deserves tears."},
 "1112": {"0": "a full early finish at three on friday, what prompted that?"},
 "1113": {"0": "four weeks of notice left, how's the mood in the office?",
          "1": "like being a ghost, handing everything over, anything lined up next?"},
 "1114": {"0": "good, did you actually rest on the mental health day or do chores?"},
 "1115": {"0": "did the old games console from the loft still work, any luck?",
          "2": "setting a limit, word for word what your parents said, it happens."},
 "1116": {"0": "what time does the sunday video call with australia land for you?",
          "2": "fifteen minutes of wavering then chaos, every long distance call."},
 "1117": {"0": "after how long, an old school friend out of the blue, lovely?"},
 "1118": {"0": "running the charity ten k properly or the run walk strategy?",
          "1": "run walk for the hospice that looked after your gran, good cause."},
 "1120": {"0": "open mic kind or a proper act at the arts centre, comedy night?"},
 "1121": {"0": "oh he's behind you, how was the panto with the kids?"},
 "1122": {"0": "well done, two streaming services cancelled, did you miss any?"},
 "1123": {"0": "music or the talk station, the radio on all day here?",
          "2": "naming a song that didn't exist and feeling no shame, confident."},
 "1124": {"0": "is there a fun fair with the winter lights switch on, good night?"},
}

path = "audit/changes_magpie26.json"
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
