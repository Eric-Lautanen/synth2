#!/usr/bin/env python3
"""Hand-written b2765 rewrites -> audit/changes_magpie5.json, then self-validate."""
import json

C = {
 "1722": {"0": "did the bin men skip you again, or was it out too late?"},
 "1723": {"0": "have you met the new neighbours in number twelve yet?"},
 "1724": {"0": "is the dripping bathroom tap just a worn washer, a cheap fix?"},
 "1725": {"0": "is the hair cut going shorter this time, or the same as before?"},
 "1726": {"0": "is the dentist just a check up, or the clean you dread?"},
 "1727": {"0": "how many years is the anniversary this time, and do you forget it?"},
 "1728": {"0": "did the allotment go wild with weeds while you were away?"},
 "1729": {"0": "are the trains off again this weekend, bus replacement instead?"},
 "1730": {"0": "is the cracked phone screen bad, or just a small one?"},
 "1731": {"0": "will you get a refund for the late supermarket delivery?"},
 "1732": {"0": "what was the charity shop bargain, anything good this time?"},
 "1733": {"0": "was the post office queue out the door, did you give up?"},
 "1734": {"0": "is the wasp nest under the eaves small enough to leave alone?"},
 "1735": {"0": "do the new curtains need taking up, or were they the right length?"},
 "1736": {"0": "typical, did you cook the barbecue indoors when the rain came?"},
 "1737": {"0": "are the legs sore after the gym break, first week is worst?"},
 "1738": {"0": "has the library sent a letter about the overdue book yet?"},
 "1739": {"0": "which fruit went into the hedgerow jam, blackberries this year?"},
 "1740": {"0": "is the fridge not cooling at all, or just a bit warm?",
          "1": "still humming but warm usually means the thermostat, worth a look."},
 "1741": {"0": "is the thursday job interview somewhere you actually want to be?"},
 "1742": {"0": "did the power cut cost you anything in the freezer?",
          "1": "keeping the door shut is the trick, a full freezer holds cold."},
 "1743": {"0": "is the new hedge something evergreen, or does it drop leaves?",
          "1": "for a bare winter back, laurel would do it, slow but smart."},
 "1744": {"0": "did the car fail its mot on anything serious this morning?",
          "1": "just a tyre and a wiper is cheap, some years it is worse."},
 "1745": {"0": "is your son enjoying the swimming lessons so far, then?",
          "1": "a good age, once he loves the water he will never look back."},
 "1746": {"0": "what is your mum's favourite flavour for the birthday cake?"},
 "1747": {"0": "is the roof leaking from a tile or the flashing?",
          "1": "the chimney flashing is a common one, best done before the damp."},
 "1748": {"0": "did they say why the flight was pushed back four hours?",
          "1": "nothing to do about the weather, at least you were at home."},
 "1749": {"0": "is the new mattress firmer than the old one, then?",
          "1": "the mattress takes a week to get used to, give it a month."},
 "1750": {"0": "is the kitchen drawer jammed on the runner, or just too full?",
          "1": "if the drawer is too full, clear it out and it will slide."},
 "1751": {"0": "is the overflowing gutter blocked with leaves, or something worse?",
          "1": "after years it is worth clearing before winter, the gutter soaks the wall."},
 "1752": {"0": "is the charity run a ten k, or something longer?",
          "1": "further than before is a good stretch, build up slowly for the run."},
 "1753": {"0": "did it finally die, or did the toaster last a good while?",
          "1": "eight years is a good innings for a toaster, the new ones fail."},
 "1754": {"0": "does the neighbour tree drop much on your side of the fence?",
          "1": "you can cut the branch back to the boundary, but talk first."},
 "1755": {"0": "is it the wood on the side gate, or the hinge itself?",
          "1": "if the hinge is rusted through, new ones are cheap, do both."},
 "1756": {"0": "what recipe did you get off the neighbours, anything good?",
          "1": "a family secret curry is the best kind, did they share it all?"},
 "1757": {"1": "then wait for spring, settling for less than you want nags for years."},
}

path = "audit/changes_magpie5.json"
json.dump(C, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

lines = [l for l in open("raw/small_talk_casual.jsonl", "rb").read().split(b"\r\n") if l.strip()]
issues = []
n = 0
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
