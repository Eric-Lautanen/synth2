"""Build a synth2 batch JSON from hand-written text files, with the hygiene
asserts, the three scans and both dials -- the whole pre-flight companion.

Text format: one row per line, turns split on " | ", alternating user/assistant.
`turn_structure` and `length_bucket` are DERIVED, never declared.

    python synth2_build.py --src a.txt b.txt --out batch.json \
        [--live small_talk_sexy.jsonl] [--pad pad.json] [--convert convert.json]

--live   the raw/*.jsonl this batch targets. Scan (b) compares the batch's
         first-word histogram at EVERY turn position against that file's, which
         is the correct reference once the file has rows. Omit it and (b) falls
         back to the corpus aggregate (only right when the file is empty).
--pad    JSON list of [old, new] pairs applied to the concatenated text with a
         count==1 assert -- the atomic way to fix a collision.
--convert JSON object {first_turn_text: [riposte, closer]} that upgrades a
         2-turn row into a 4-turn chain in place. Use it to pull the multi dial,
         but note it can duplicate advice across A1 and A2 -- scan (a) finds it.
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

BANNED = ["-", "\u2013", "\u2014", "\u2015", "\u2012"]
FLOOR = 8.0     # a first word at or above this %, where the reference is 0%, is drift
RATIO = 3.0     # ... or this many times the reference rate


def words(t):
    return re.sub(r"[^a-z0-9 ]", " ", t.lower()).split()


def grams(t, n):
    w = words(t)
    return [" ".join(w[i:i + n]) for i in range(len(w) - n + 1)]


def fw(t):
    m = re.findall(r"[a-z0-9']+", t.lower())
    return m[0] if m else ""


def flat(row):
    return [t[1] for t in row["turns"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--live", default=None)
    ap.add_argument("--raw", default=r"C:\github\DBllm\runs\synth2\raw")
    ap.add_argument("--pad", default=None)
    ap.add_argument("--convert", default=None)
    ap.add_argument("--max-rows", type=int, default=0)
    a = ap.parse_args()

    text = ""
    for p in a.src:
        assert os.path.exists(p), p
        text += open(p, encoding="utf-8").read() + "\n"

    if a.pad:
        for old, new in json.load(open(a.pad, encoding="utf-8")):
            assert text.count(old) == 1, \
                f"PAD anchor not unique ({text.count(old)}x): {old[:70]!r}"
            text = text.replace(old, new)

    lines = [l.strip() for l in text.split("\n")]
    lines = [l for l in lines if l]

    rows = []
    for ln, line in enumerate(lines, 1):
        parts = [p.strip() for p in line.split(" | ")]
        for p in parts:
            assert p, f"line {ln}: empty turn"
            assert p.isascii(), f"line {ln}: non-ascii {p!r}"
            for b in BANNED:
                assert b not in p, f"line {ln}: banned {b!r} in {p!r}"
        assert len(parts) % 2 == 0, f"line {ln}: odd segment count {len(parts)}"
        assert 2 <= len(parts) <= 10, f"line {ln}: {len(parts)} segments"
        rows.append({"turns": [["user" if i % 2 == 0 else "assistant", t]
                               for i, t in enumerate(parts)]})

    if a.convert:
        conv = json.load(open(a.convert, encoding="utf-8"))
        used = set()
        for ln, r in enumerate(rows, 1):
            if len(r["turns"]) != 2:
                continue
            k = "#%d" % ln
            if k not in conv:
                k = r["turns"][0][1]
            if k in conv:
                riposte, closer = conv[k]
                r["turns"].append(["user", riposte])
                r["turns"].append(["assistant", closer])
                used.add(k)
        left = set(conv) - used
        assert not left, f"CONVERT keys never matched ({len(left)}): {sorted(left)[:3]}"

    if a.max_rows:
        rows = rows[:a.max_rows]

    print(f"rows read: {len(rows)}")

    # (a) advice given twice -- A1 vs the closing assistant turn
    dup = []
    for i, r in enumerate(rows, 1):
        f = flat(r)
        if len(f) >= 4:
            ov = set(grams(f[1], 4)) & set(grams(f[-1], 4))
            if ov:
                dup.append((i, sorted(ov)[:3]))
    print(f"(a) rows whose A1 and last A share a 4-gram: {len(dup)}")
    for i, ov in dup:
        print(f"    {i}: {ov}")

    # (c) repeated assistant 5-grams
    seen = collections.defaultdict(list)
    for i, r in enumerate(rows, 1):
        for j in range(1, len(r["turns"]), 2):
            for g in grams(r["turns"][j][1], 5):
                seen[g].append((i, j))
    rep = {g: v for g, v in seen.items() if len(v) > 1}
    print(f"(c) repeated assistant 5-grams: {len(rep)}")
    for g, v in sorted(rep.items(), key=lambda kv: -len(kv[1])):
        print(f"    {len(v)}x  {g}  {v}")

    # (b) opener histogram vs the live file (or the corpus aggregate)
    ref, label = [], "corpus"
    if a.live:
        p = os.path.join(a.raw, a.live)
        ref = [[t["text"] for t in json.loads(l)["turns"]]
               for l in open(p, encoding="utf-8") if l.strip()]
        label = a.live
    else:
        for p in sorted(glob.glob(os.path.join(a.raw, "*.jsonl"))):
            for line in open(p, encoding="utf-8"):
                if line.strip():
                    ref.append([t["text"] for t in json.loads(line)["turns"]])

    flagged = 0
    for pos in range(0, 4):
        br = [flat(r)[pos] for r in rows if len(r["turns"]) > pos]
        rr = [f[pos] for f in ref if len(f) > pos]
        if not br or not rr:
            continue
        bc = collections.Counter(fw(t) for t in br)
        rc = collections.Counter(fw(t) for t in rr)
        note = "  (n<30, ratio unstable)" if len(rr) < 30 else ""
        print(f"(b) {'user ' if pos % 2 == 0 else 'assist'} turn {pos + 1}: "
              f"n={len(br)}  ref={label} n={len(rr)}{note}")
        for w, k in bc.most_common(9):
            bs = 100 * k / len(br)
            rs = 100 * rc[w] / len(rr)
            over = (rs > 0 and bs > RATIO * rs and bs >= FLOOR) or (rs == 0 and bs >= FLOOR)
            if over:
                flagged += 1
            print(f"      {w:<11} {k:>4} {bs:5.1f}%   ref {rs:5.1f}%"
                  + ("  <-- OVER" if over else ""))

    # dials
    tp = collections.Counter(len(r["turns"]) for r in rows)
    struct = collections.Counter("short_multi_turn" if len(r["turns"]) >= 4
                                 else "single_turn" for r in rows)
    buckets = collections.Counter()
    longs, near = [], []
    for i, r in enumerate(rows, 1):
        longest = max(len(words(t[1])) for t in r["turns"])
        b = "short" if longest < 15 else ("medium" if longest < 60 else "long")
        buckets[b] += 1
        if b == "long":
            longs.append((i, longest, flat(r)[0][:50]))
        elif 55 <= longest <= 59:
            near.append((i, longest, flat(r)[0][:50]))

    multi = struct["short_multi_turn"]
    print(f"turns-per-row: {dict(tp)}")
    print(f"structure: {dict(struct)}  multi share {100 * multi / len(rows):.1f}%")
    print(f"buckets: {dict(buckets)}")
    print(f"long rows: {len(longs)}")
    for i, n, s in longs:
        print(f"    {i:>4} {n:>3}w {s}")
    print(f"NEAR MISS 55-59: {len(near)}")
    for i, n, s in near:
        print(f"    {i:>4} {n:>3}w {s}")
    print(f"flagged positions: {flagged}")

    json.dump(rows, open(a.out, "w", encoding="utf-8"), ensure_ascii=True)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
