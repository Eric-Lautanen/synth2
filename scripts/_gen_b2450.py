#!/usr/bin/env python3
"""Hand-written b2450 rewrites -> audit/changes_magpie14.json, then self-validate."""
import json

C = {
 "1230": {"0": "watched the match last night, did you stay up or catch the highlights?",
          "1": "full ninety minutes and paying for it this morning, worth it though."},
 "1231": {"0": "five a side team lost again, sixth week running, still enjoying it?",
          "1": "chips after explains the loyalty, do you play the same night weekly?"},
 "1232": {"0": "little one into snakes and ladders, has he learned to lose yet?",
          "1": "flipped the board on tuesday, i remember that stage well, play again now?"},
 "1233": {"0": "word game on your phone eating the evenings, much progress on it?"},
 "1234": {"0": "brother talked you into the fantasy league again, any better this year?"},
 "1235": {"0": "kids to the park for a kickabout, did they outlast you this time?",
          "1": "outlasted you by a mile, on the bench by the end, about right."},
 "1236": {"0": "started that new series everyone keeps going on about, any good so far?",
          "1": "two episodes in and not sure yet, it might be a slow burn."},
 "1237": {"1": "comfort watching, you knew every line and still enjoyed it, which one?"},
 "1238": {"0": "podcast backlog out of control, are you far behind on it?",
          "1": "forty and still adding more is a losing battle, commute listening?"},
 "1239": {"0": "book club picked one you cannot get into, which is it this month?",
          "1": "long one about a family in the war, two hundred pages in, lost."},
 "1240": {"0": "rewatching old sitcoms instead of anything new, same one again?"},
 "1241": {"0": "mum got you into a quiz show, the general knowledge one?",
          "1": "shouting answers at the telly, we do the same, does she win more?"},
 "1242": {"0": "back at the gym after three weeks off, how did it feel?",
          "1": "brutal, barely doing what you used to, a break sets you back."},
 "1243": {"0": "lunch breaks are walks instead of the canteen, does it wake you up?",
          "1": "three miles round the park leaves you sharper, decent walk that."},
 "1244": {"0": "knees started complaining about the running, how long have you been at it?"},
 "1246": {"0": "sister got you doing her workout video, worth it or a fad?"},
 "1247": {"0": "hit your step goal every day this week, how did you manage seven?"},
 "1249": {"0": "someone in the block keeps leaving bags in the hallway, anyone say anything?",
          "1": "all just stepping round them, classic standoff, will you mention it?"},
 "1250": {"0": "a piano upstairs now, oh no, how bad is it really?"},
 "1251": {"0": "bins not collected again this week, no excuse given this time?",
          "1": "none given and the whole road overflowing, same here last month."},
 "1252": {"0": "old couple opposite moved out, after how many years were they there?"},
 "1253": {"0": "shared garden fence finally being replaced, who is paying for it?"},
 "1254": {"0": "spent twenty minutes looking for a space in town, multi storey again?"},
 "1255": {"0": "car failed its mot on the brakes, that is going to sting."},
 "1257": {"0": "motorway closed on the way home, were you stuck for long?",
          "1": "hour and a half barely moving, then a coffee, same as me."},
 "1258": {"0": "dad teaching your nephew to drive, is it going well?"},
 "1259": {"0": "cycling to work to dodge the traffic, how is the route?"},
 "1260": {"0": "flat week with nothing specific, has anything helped or just one of those?",
          "1": "fresh air and an early night, mostly, good to hear it is passing."},
 "1261": {"0": "snapped at someone at work today, what set you off?",
          "1": "simple question and you bit their head off, we have all done it."},
 "1262": {"0": "sleeping badly all week and it is showing, stress or something else?",
          "1": "a fortnight of it and running on fumes, that is a long time."},
 "1263": {"0": "felt really good after the walk this morning, was today any different?"},
 "1264": {"0": "putting off a big decision for weeks now, something holding you back?",
          "1": "changing your mind every time you think about it, those take a while."},
 "1265": {"0": "everything got a bit much last week, did anything help at all?",
          "1": "crossing things off a list one at a time, is it shorter now?"},
}

path = "audit/changes_magpie14.json"
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
