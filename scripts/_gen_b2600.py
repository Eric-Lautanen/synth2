#!/usr/bin/env python3
"""Hand-written b2600 rewrites -> audit/changes_magpie32.json, then self-validate."""
import json

C = {
 "1469": {"0": "welcome to the other side, what sold you on the electronic reader?"},
 "1470": {"0": "modern waiting, do the smart tv apps load slower than old channels?",
          "2": "haha the family requests them back one by one, apps like weeds."},
 "1471": {"0": "a proper cross generational lobby, how did the video game go?",
          "1": "he narrated your failures with great kindness, the best coaching."},
 "1472": {"0": "that digital hoard of twelve thousand photos finally reached capacity, what now?"},
 "1474": {"0": "app controlled lighting era, do you use the smart bulb colours?"},
 "1477": {"0": "great recurring argument, what is the bin day flashpoint this time?"},
 "1478": {"0": "poor owner, any sightings of the lost cat near the post box?"},
 "1480": {"0": "back in tree negotiation round two, has the maple hit the shed again?"},
 "1481": {"0": "after all that, what finally sorted the noise from the flat above?",
          "1": "one calm conversation, rugs down the same weekend, that did it.",
          "2": "they asked to be told if it comes back, the real win."},
 "1482": {"0": "going with the old ways, what went in the welcome basket?"},
}

path = "audit/changes_magpie32.json"
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
