#!/usr/bin/env python3
"""Hand-written b2480 rewrites -> audit/changes_magpie27.json, then self-validate."""
import json

C = {
 "1281": {"0": "camping in october against all advice, did the tent survive?"},
 "1282": {"0": "van life, was the caravan roomy enough for the week on the coast?",
          "1": "a dog with opinions about the caravan layout, that is a first."},
 "1283": {"1": "a proper coffee machine and working wifi, that beats a hotel."},
 "1284": {"0": "paris for two nights is the quick version, sights or just food?",
          "2": "ninety minutes reading and the city appears, can't face airports now."},
 "1285": {"1": "egg and cress wrapped in foil, train sandwiches taste better at speed."},
 "1286": {"0": "packing cubes for the first time, did they change your life?"},
 "1287": {"2": "haha learned nothing and never will, at least the tradition holds."},
 "1289": {"0": "brilliant, what has the local history group dug up so far?",
          "2": "one historian who knows everything, they adopted you within two weeks."},
 "1290": {"1": "proper heritage work, wiping buses and talking old routes for four hours.",
          "2": "an old driver correcting your speech notes, that is a living archive."},
 "1291": {"0": "good on you all, how much litter did the street pick collect?"},
 "1292": {"0": "how many trees went in with the rangers on saturday?"},
 "1293": {"0": "after all that fundraising, how does the community garden look?"},
 "1295": {"0": "what a find, does the fountain pen still write, any ink?",
          "1": "haha a new ink cartridge and it writes beautifully, heavy like a tool."},
 "1296": {"0": "proper old school, did the morocco postcards beat you home?"},
}

path = "audit/changes_magpie27.json"
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
