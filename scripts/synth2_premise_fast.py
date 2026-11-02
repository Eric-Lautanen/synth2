#!/usr/bin/env python3
"""Fast premise check over the WHOLE synth2 corpus.

The shipped synth2_premisecheck.py is O(candidates x corpus) and times out on a
150-candidate batch. This builds a 6-gram inverted index once, then probes only
the candidate's own grams, so a whole-corpus HIT + NEAR pass runs in seconds.

  HIT  = the candidate, normalised (punctuation stripped, whitespace collapsed)
         and 3+ words, is an EXACT existing turn text.
  NEAR = the candidate shares >= --near six-grams with one existing row.

Batch 6065: this caught one genuine duplicate premise (a long shopping row
sharing 8 six-grams -- the whole "list in aisle order" beat -- with an existing
supportive row) that BOTH exact dup gates read as CLEAN.

usage:
  synth2_premise_fast.py candidates.txt [--near 8] [--raw <raw dir>]

candidates.txt: one candidate first-user-turn per line.
exit code 1 if anything is flagged.
"""
import argparse, collections, glob, json, os, re, sys

RAW_DEFAULT = r"C:\github\DBllm\runs\synth2\raw"


def norm(s):
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s.lower()).split())


def grams(s, n=6):
    w = norm(s).split()
    if len(w) < n:
        return set()
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidates")
    ap.add_argument("--near", type=int, default=8)
    ap.add_argument("--raw", default=RAW_DEFAULT)
    a = ap.parse_args()

    turns = collections.defaultdict(list)
    rowgrams = []
    for p in sorted(glob.glob(os.path.join(a.raw, "*.jsonl"))):
        base = os.path.basename(p)
        for ln, line in enumerate(open(p, encoding="utf-8"), 1):
            if not line.strip():
                continue
            j = json.loads(line)
            ts = [x["text"] for x in j["turns"]]
            for x in ts:
                turns[norm(x)].append((base, ln))
            g = set()
            for x in ts:
                g |= grams(x)
            rowgrams.append((base, ln, g))

    gidx = collections.defaultdict(list)
    for rid, (_, _, g) in enumerate(rowgrams):
        for gg in g:
            gidx[gg].append(rid)

    cands = [l.strip() for l in open(a.candidates, encoding="utf-8") if l.strip()]
    bad = 0
    for c in cands:
        nc = norm(c)
        if len(nc.split()) >= 3 and nc in turns:
            bad += 1
            print("  HIT           %s  %s" % (turns[nc][0], c[:72]))
            continue
        cg = grams(c)
        if not cg:
            continue
        hits = collections.Counter()
        for gg in cg:
            for rid in gidx.get(gg, ()):
                hits[rid] += 1
        if hits:
            rid, ov = hits.most_common(1)[0]
            if ov >= a.near:
                bad += 1
                print("  NEAR ov=%-3d  %s  %s" % (ov, rowgrams[rid][:2], c[:72]))

    print("corpus rows: %d   candidates: %d   flagged: %d" % (len(rowgrams), len(cands), bad))
    print("VERDICT: " + ("BLOCKED -- rewrite these premises" if bad else "CLEAN"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
