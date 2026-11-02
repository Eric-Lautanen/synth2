#!/usr/bin/env python3
"""Pre-build diagnostic for a hand-written synth2 batch source (pipe format).

Reads a pipe-format .txt (one row per line, turns split on " | ", alternating
user/assistant starting with user) and reports everything you need BEFORE the
build:

  * row count and per-row segment-count histogram (must be even, 2..10)
  * U0 family vs the intended block family, and -- for a miss -- WHICH substring
    of an earlier family hijacked it.  This is the instrument for the substring
    trap: topics.classify() is first-match over 23 ordered regexes and matches
    ANYWHERE in the string, so a keyword is only safe if no earlier family is a
    substring of it (`appointment` contains `app`; tech #5 beats health #9).
  * length buckets, long rows, turns/row, multi share
  * per-position first-word histogram (compare to synth2_caps.py)
  * nonascii / hyphen / apostrophe counts
  * AUX rule: any turn whose FIRST word is an auxiliary must end with '?'

usage:
  synth2_diagnose.py <src.txt> --blocks "family A,family B,family C,..."
        (blocks are EQUAL-SIZED slices of the file, in order)

  synth2_diagnose.py <src.txt> --blocks "driving + parking,home + chores + repairs"
"""
import argparse, collections, os, re, sys

sys.path.insert(0, r"C:\github\DBllm\runs\synth2\scripts")
from topics import FAMILIES, classify

AUX = {"is", "are", "was", "were", "am", "be", "been", "do", "does", "did",
       "have", "has", "had", "can", "could", "will", "would", "shall", "should",
       "may", "might", "must", "can't", "won't", "don't", "doesn't", "didn't",
       "isn't", "aren't", "wasn't", "weren't", "hasn't", "haven't", "hadn't"}


def matched_family(opener):
    t = " " + opener.lower() + " "
    for name, pat in FAMILIES:
        m = re.search(pat, t)
        if m:
            return name, m.group(0)
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--blocks", required=True,
                    help="comma-separated family names, one per EQUAL slice of the file")
    a = ap.parse_args()

    blocks = [b.strip() for b in a.blocks.split(",") if b.strip()]
    rows = [l.rstrip("\n") for l in open(a.src, encoding="utf-8") if l.strip()]
    n = len(rows)
    per = n // len(blocks)
    if per * len(blocks) != n:
        print("WARN: %d rows do not split evenly into %d blocks" % (n, len(blocks)))

    def want(i):
        k = min((i - 1) // per, len(blocks) - 1)
        return blocks[k]

    segs = collections.Counter()
    miss = []
    buckets = []
    longs = []
    turnsper = collections.Counter()
    pos = collections.defaultdict(collections.Counter)
    nonascii = hyphen = apo = 0
    auxbad = []

    for i, line in enumerate(rows, 1):
        parts = [p.strip() for p in line.split(" | ")]
        segs[len(parts)] += 1
        if len(parts) % 2 or not (2 <= len(parts) <= 10):
            print("BAD SHAPE row %d: %d segments" % (i, len(parts)))
        turnsper[len(parts)] += 1
        for j, p in enumerate(parts):
            w = p.split(" ")[0].lower()
            pos[j][w] += 1
        u0 = parts[0]
        got = classify(u0)
        w = want(i)
        if got != w:
            name, hit = matched_family(u0)
            miss.append((i, w, got, hit, u0))
        longest = max(len(p.split()) for p in parts)
        b = "short" if longest < 15 else ("medium" if longest < 60 else "long")
        buckets.append(b)
        if b == "long":
            longs.append((i, longest))
        for j, p in enumerate(parts):
            if j % 2 == 1 and p.split(" ")[0].lower() in AUX and not p.rstrip().endswith("?"):
                auxbad.append((i, j, p))
        if any(ord(c) > 127 for c in line):
            nonascii += 1
        if "-" in line:
            hyphen += 1
        if "'" in line:
            apo += 1

    print("rows %d" % n)
    print("segments: %s" % dict(sorted(segs.items())))
    print("U0 misses: %d" % len(miss))
    for i, w, got, hit, u0 in miss:
        print("   row %3d want %-26s got %-26s hit=%-10r :: %s" % (i, w, got, hit, u0[:70]))
    bc = collections.Counter(buckets)
    tot = sum(bc.values())
    print("buckets s/m/l: %d/%d/%d  (%.1f/%.1f/%.1f)"
          % (bc["short"], bc["medium"], bc["long"],
             100.0 * bc["short"] / tot, 100.0 * bc["medium"] / tot, 100.0 * bc["long"] / tot))
    print("long rows: %d  %s" % (len(longs), [x[0] for x in longs]))
    print("turns-per-row: %s" % dict(sorted(turnsper.items())))
    multi = sum(v for k, v in turnsper.items() if k >= 4)
    print("multi: %d / %d = %.1f%%" % (multi, n, 100.0 * multi / n))
    print()
    for j in sorted(pos):
        nn = sum(pos[j].values())
        top = "  ".join("%s %.1f" % (w, 100.0 * c / nn) for w, c in pos[j].most_common(10))
        print("pos%d (n=%d): %s" % (j, nn, top))
    print()
    print("nonascii: %d  hyphen: %d  apostrophe: %d" % (nonascii, hyphen, apo))
    print("AUX rule violations: %d" % len(auxbad))
    for i, j, p in auxbad:
        print("   row %d pos%d :: %s" % (i, j, p[:80]))


if __name__ == "__main__":
    main()
