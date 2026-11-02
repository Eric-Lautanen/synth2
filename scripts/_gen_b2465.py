#!/usr/bin/env python3
"""Hand-written b2465 rewrites -> audit/changes_magpie25.json, then self-validate."""
import json

C = {
 "1266": {"0": "with proper chisels and everything, wood carving is serious kit?"},
 "1268": {"0": "proper wool ones itch at first, that icelandic jumper will soften.",
          "1": "haha the itch fades, two wears in and you're warmer already, right?",
          "2": "hand washed with special soap and dried flat, not a millimetre lost."},
 "1269": {"0": "old treadle one or the electric portable, which sewing machine?"},
 "1270": {"0": "from which years, are the printed photos for the frames recent?",
          "1": "a beach photo from 2016, accidental and the best you ever took."},
 "1271": {"0": "rematch won then, did the wallpaper bubbles behave this attempt?",
          "1": "bubble war won, after much smoothing and one small swear, triumph."},
 "1272": {"0": "fancy, does the heated towel rail actually get warm, worth it?"},
 "1273": {"0": "bouncy life suits her, is she good at trampoline already?"},
 "1274": {"0": "is that the climbing wall up at the leisure centre, good club?",
          "2": "superb, they belay carefully and shout encouragement, that makes a club.",
          "3": "loves going up and whines coming down, that's the climber's disease."},
 "1275": {"0": "big milestone, first guide camp away, how did she come back?"},
 "1276": {"0": "what did he go with for his first proper word, the classic?"},
 "1277": {"0": "a toddler narrating everything, what is the material like now?",
          "2": "talks himself unconscious by half seven, very efficient, be grateful."},
 "1278": {"0": "aw big moment, did the first tooth come out clean at school?"},
 "1279": {"1": "neon one from the party bag, at least the photo is a story.",
          "2": "smallest package is the learned move, big packs sit unloved in drawers."},
}

path = "audit/changes_magpie25.json"
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
