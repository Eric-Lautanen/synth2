#!/usr/bin/env python3
"""Hand-written b2645 rewrites -> audit/changes_magpie15.json, then self-validate.
Also lifts the terse-7.5 DRIFT (all replies 10-13 words)."""
import json

C = {
 "1555": {"0": "watched the match on saturday, terrible game, who was playing?"},
 "1556": {"0": "joined a darts league at the pub, are you any good?"},
 "1557": {"0": "son started playing rugby, is he enjoying it so far?"},
 "1558": {"0": "tickets for the cricket in july arrived, a whole day of it?"},
 "1559": {"0": "playing chess online most evenings now, are you winning any games?"},
 "1560": {"0": "football called off for rain, did you travel far for it?",
          "1": "forty minutes each way then called off ten before kick off, gutting."},
 "1561": {"0": "started watching the cycling tour, do you follow it properly?"},
 "1562": {"0": "table tennis table at work now, does anyone actually use it?"},
 "1563": {"0": "went to the snooker club with your dad, is he still playing?",
          "1": "twice a week and he still beats you comfortably, he has had practice."},
 "1564": {"0": "team lost on penalties again, did you watch it live?"},
 "1565": {"0": "trying to learn the rules of american football, how is that going?",
          "1": "badly, you understand the running and not much else, it takes a while."},
 "1566": {"0": "played rounders with the kids in the park, win or lose?"},
 "1567": {"0": "started a new series last night, what is it about?",
          "1": "detective in a small town, seen the plot before but do not mind."},
 "1568": {"0": "cinema for the first time in ages, did you see anything good?"},
 "1569": {"0": "podcast backlog got out of hand, how far behind are you?"},
 "1570": {"0": "book you are reading has stalled, is it not gripping you?"},
 "1571": {"0": "cancelled the show you liked, was it left on a cliffhanger?",
          "1": "mid story with no ending, just gone, cancellations like that are infuriating."},
 "1572": {"0": "listening to a lot of old music lately, which era is it?",
          "1": "things from school, pure nostalgia and you know it, nothing wrong with that."},
 "1573": {"0": "radio in the car stuck on one station, can you not change it?",
          "1": "knob came off months ago and you never got round to it."},
 "1574": {"0": "watched a documentary about deep sea fish, learn anything new?",
          "1": "fascinating and slightly horrifying, some of them look made up."},
 "1575": {"0": "rewatching a comedy from years ago, does it still hold up?",
          "1": "mostly, though a few jokes have not aged well, happens to the best."},
 "1576": {"0": "new record player for your birthday, have you got many records?"},
 "1577": {"0": "film was three hours long, was it worth the length?",
          "1": "hour could have gone and nothing lost, three hours needs to earn it."},
 "1578": {"0": "got into watching old quiz shows, are they on in the afternoon?",
          "1": "answering out loud and getting most wrong, shouting at the telly is fun."},
 "1579": {"0": "big shop this morning then, was it busy in there?"},
 "1580": {"0": "returned a coat that did not fit, any trouble with the refund?",
          "1": "none at all, they did not even ask why, how it should be."},
 "1581": {"1": "either ugly or costing a fortune, boots are always one or the other."},
 "1582": {"0": "charity shop had a real bargain today, did you come away with much?"},
 "1583": {"0": "spent ages in the queue at the post office, big parcel?"},
 "1584": {"0": "trolley had a wobbly wheel, did you swap it at the end?",
          "1": "not until the end and by then too committed, wobbly trolley all round."},
 "1585": {"0": "ordered some bits for the garden, from a proper nursery?"},
 "1586": {"0": "supermarket out of the bread you like, did you get a substitute?"},
 "1587": {"0": "always forgetting something on the list, which one this time?"},
 "1588": {"0": "had your shoes repaired instead of replacing them, was that cheaper?",
          "1": "fifteen pounds against eighty for new ones, no contest, worth repairing."},
 "1589": {"0": "market was heaving on saturday, did you get much there?"},
 "1590": {"0": "slowly replacing things with second hand stuff, bought anything nice?"},
}

path = "audit/changes_magpie15.json"
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
