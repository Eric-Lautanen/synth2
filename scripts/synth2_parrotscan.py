#!/usr/bin/env python3
"""synth2 parrot scan -- assistant turns that restate their own user turn.

WHY THIS EXISTS
`synth2_stagecheck.py` already measures this class (`[PARROT]`, 6+ shared grams),
but it only ever sees a STAGED BATCH. It cannot see the landed corpus, so a batch
that was staged before the screen tightened keeps its parrots forever and every
later gate stays green. Measured 2026-10-18 over the 6746 landed rows:

    casual 242 / 2000 (12.1%)   lazy 2 / 2000   angry 34 / 2000   sexy 0 / 620

Casual is the oldest lane and carries almost all of it: the two-part mold (echo
clause, comma, question) is house style, and in casual the echo clause grew from a
content token into a whole restatement. The row below is the archetype:

    u: gone by ten like it was never there. the whole morning felt like a dream.
    a: gone by ten like it was never there, the whole morning a dream.

Not a duplicate, not a near-dup, not a restatement of the opener -- the two gates
that exist are blind to it, which is exactly why it survived to the corpus.

THE MEASURE
Deliberately the SAME rule as the stagecheck, so the two agree and neither can
drift: lowercased alphanumeric word 6-grams, assistant turn against the user turns
of its OWN row, any overlap counts. Keep this in sync with synth2_stagecheck.py
line ~442. If they disagree on the same input, the gate is right.

USAGE
    python runs/synth2/scripts/synth2_parrotscan.py --corpus
    python runs/synth2/scripts/synth2_parrotscan.py --corpus --lane casual --ids
    python runs/synth2/scripts/synth2_parrotscan.py %TEMP%/tmp_b4190.json
Exits 1 if any row breaches, so it can gate a pass.
"""
import argparse
import io
import json
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw")
LANES = ["casual", "lazy", "angry", "sexy"]
N = 6


def grams(s, n=N):
    w = re.findall(r"[a-z0-9']+", s.lower())
    return set(" ".join(w[i:i + n]) for i in range(len(w) - n + 1))


def pairs(turns):
    """Normalise both row shapes in this repo: the corpus stores
    {"role":..,"text":..} dicts, a BUILT batch stores ["user","text"] pairs."""
    for t in turns:
        if isinstance(t, dict):
            yield t["role"], t["text"]
        else:
            yield t[0], t[1]


def row_parrots(turns):
    """Return [(turn_index, shared_6gram)] for assistant turns echoing the user."""
    t = list(pairs(turns))
    us = [txt for role, txt in t if role == "user"]
    out = []
    for j, (role, txt) in enumerate(t):
        if role != "assistant":
            continue
        g = grams(txt)
        sh = set()
        for u in us:
            sh |= (g & grams(u))
        if sh:
            out.append((j, sorted(sh)[0]))
    return out


def scan_corpus(lanes):
    bad, per = [], {}
    for lane in lanes:
        p = os.path.join(RAW, "small_talk_%s.jsonl" % lane)
        if not os.path.exists(p):
            continue
        n = 0
        for ln, line in enumerate(io.open(p, encoding="utf-8"), 1):
            if not line.strip():
                continue
            r = json.loads(line)
            ph = row_parrots(r["turns"])
            if ph:
                n += 1
                bad.append(dict(lane=lane, line=ln, id=r["id"], batch=r.get("batch_no"),
                                hits=ph))
        per[lane] = n
    return bad, per


def scan_file(path):
    bad = []
    if path.endswith(".jsonl"):
        rows = [json.loads(l) for l in io.open(path, encoding="utf-8") if l.strip()]
    else:
        rows = json.load(io.open(path, encoding="utf-8"))
        if isinstance(rows, dict):
            rows = rows.get("rows", [])
    for i, r in enumerate(rows, 1):
        ph = row_parrots(r["turns"])
        if ph:
            bad.append(dict(lane="batch", line=i, id=r.get("id", "row%d" % i),
                            batch=r.get("batch_no"), hits=ph))
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch", nargs="?", help="a built batch .json or a raw .jsonl")
    ap.add_argument("--corpus", action="store_true", help="scan the landed corpus")
    ap.add_argument("--lane", action="append", default=None)
    ap.add_argument("--ids", action="store_true", help="list every breaching row id")
    a = ap.parse_args()

    if a.corpus:
        lanes = a.lane or LANES
        bad, per = scan_corpus(lanes)
        total = sum(per.values())
        print("rows scanned: %d" % sum(
            1 for lane in lanes
            for l in io.open(os.path.join(RAW, "small_talk_%s.jsonl" % lane), encoding="utf-8")
            if l.strip()))
        for lane in lanes:
            print("  %-7s %4d breaching" % (lane, per[lane]))
        print("PARROT: %d rows at %d+ grams" % (total, N))
    elif a.batch:
        bad = scan_file(a.batch)
        print("PARROT: %d rows at %d+ grams  (%s)" % (len(bad), N, a.batch))
    else:
        ap.error("give a batch file or --corpus")

    for b in bad[:15]:
        print("   %s b%s  turn %d  %s" % (b["id"], b["batch"],
                                          b["hits"][0][0], b["hits"][0][1]))
    if len(bad) > 15 and not a.ids:
        print("   ... %d more (--ids for the full list)" % (len(bad) - 15))
    if a.ids:
        for b in bad:
            print(b["id"])
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
