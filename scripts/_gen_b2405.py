#!/usr/bin/env python3
"""Hand-written b2405 rewrites -> audit/changes_magpie30.json, then self-validate."""
import json

C = {
 "1182": {"0": "good stuff, was the flu jab at the pharmacy this year?",
          "1": "haha no appointment, out in ten minutes, the pharmacist deserves a knighthood.",
          "2": "punched by a very small professional, it'll settle by tomorrow."},
 "1183": {"0": "six donations is proper commitment, did the blood tea live up to it?"},
 "1185": {"0": "did the first physio round help the back at all?"},
 "1186": {"0": "prescription sunglasses at last, how are the new ones treating you?",
          "1": "haha the squint reveal, didn't realise how much until you stopped.",
          "2": "two hundred for bifocals and sunglasses, one purchase, two problems."},
 "1187": {"0": "all of them at once, the travel injections for the trip?"},
 "1188": {"0": "one everyone puts off, but did the practice nurse make it easy?"},
 "1189": {"0": "hearing aids at last after years of shouting, the tv must be quieter."},
 "1190": {"0": "after how many winters of random radiators, the heating timer cracked?"},
 "1191": {"0": "towels do breed in there, has the airing cupboard reached capacity?",
          "2": "haha two black bags and the door shuts, the best kind of victory."},
 "1194": {"0": "after that wet summer, no surprise the roof is green with moss.",
          "1": "three hundred for a professional scrape, and honest advice on the moss."},
 "1195": {"0": "they never give up, are the driveway weeds a water or chemical job?"},
 "1197": {"2": "haha one afternoon and a lot of tea, a fence that lasts decades."},
}

path = "audit/changes_magpie30.json"
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
