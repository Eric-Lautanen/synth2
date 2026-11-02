#!/usr/bin/env python3
"""Hand-written b2675 rewrites -> audit/changes_magpie24.json, then self-validate."""
import json

C = {
 "1607": {"0": "oh the seasonal swap, did the big duvet go in the loft bag?",
          "1": "up the ladder and back covered in fluff and regret, that loft trip."},
 "1608": {"0": "sensible timing, what does the winter car check actually cover?"},
 "1609": {"0": "oh the annual ceremony, did the heating behave on its first run?"},
 "1610": {"0": "is it the overnight kettle fill that saves the fortune?"},
 "1611": {"0": "oh the platform sprint, caught the early train with seconds spare?"},
 "1612": {"0": "oh the unreliable friend, cancelled twice this week, how did you get in?",
          "1": "leaving twenty minutes earlier is the only sanity, good buffer."},
 "1613": {"0": "a proper milestone, what did the family do for the seventieth?"},
 "1615": {"0": "a dog opening the back door is a milestone with consequences."},
 "1617": {"2": "haha he escapes on purpose and returns to the boot, homesick for us."},
 "1618": {"0": "a drop of oil, finally fixed the squeaky gate, why wait so long?"},
 "1619": {"0": "oh the big switchover, did the warm LEDs fill the dark corners?"},
 "1620": {"0": "oh the frugal miracle, what went into the leftover roast soup?",
          "1": "parsnips and carrot in the leftover soup, cost nothing and beat a carton."},
 "1622": {"1": "faintly on the hour, that silence was strange for a year, missed it."},
}

path = "audit/changes_magpie24.json"
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
