#!/usr/bin/env python3
"""Symmetric Jaccard near-dup scan: batch turns vs a file or the whole corpus.

The two shipped dup gates are EXACT only -- synth2_preflight.py compares exact
strings, synth2_premisecheck.py compares punctuation-stripped strings. Neither
can see a paraphrase. This compares punctuation-stripped WORD SETS, both sides
>= --minw words, Jaccard >= --thresh, using an inverted index on the
candidate's rarest words so it stays fast on a 100k-turn corpus.

Batch 6050 found FOUR same-file near-verbatim openers this way (J 0.75-0.80),
each one function word off a row already in the file -- and BOTH built-in gates
had read CLEAN. Fix by CHANGING THE SCENARIO: a one-word swap still lands at
J ~ 0.75.

NOTE the bar is the file's own texture, not zero: cross-register repeats are
sanctioned by the corpus law (a register is a VOICE for the same ground), so
only SAME-FILE near-verbatim is a real defect.

usage:
  synth2_nearjaccard.py <batch.json> [--file small_talk_x.jsonl | --aggregate]
  synth2_nearjaccard.py <batch.json> --aggregate --thresh 0.75
"""
import argparse, collections, glob, json, os, re, sys

RAW = r"C:\github\DBllm\runs\synth2\raw"


def toks(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower()).split()


def pairs(turns):
    """Turns come in TWO shapes: the CORPUS jsonl uses {"role","text"} DICTS,
    the BUILD batch.json uses ["role", text] LISTS. Unpacking a dict with
    `for role, txt in ...` yields the KEY STRINGS ("role","text"), so every
    corpus turn collapsed to the 1-word token "text" and was dropped by the
    --minw filter -- the tool then reported 0 hits UNCONDITIONALLY (a batch's
    own rows in --file failed to self-match at J=1.0, which is how the bug was
    caught). Handle both shapes."""
    for t in turns:
        if isinstance(t, dict):
            yield t.get("role"), t.get("text", "")
        else:
            yield t[0], t[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch")
    ap.add_argument("--file", default=None)
    ap.add_argument("--aggregate", action="store_true")
    ap.add_argument("--thresh", type=float, default=0.70)
    ap.add_argument("--minw", type=int, default=6)
    a = ap.parse_args()

    batch = json.load(open(a.batch, encoding="utf-8"))
    bturns = [(i, role, txt) for i, r in enumerate(batch, 1) for role, txt in pairs(r["turns"])]

    if a.file:
        paths = [os.path.join(RAW, a.file)]
    else:
        paths = sorted(glob.glob(os.path.join(RAW, "*.jsonl")))

    corpus = []
    for p in paths:
        base = os.path.basename(p)
        for ln, line in enumerate(open(p, encoding="utf-8"), 1):
            if not line.strip():
                continue
            for role, txt in pairs(json.loads(line)["turns"]):
                corpus.append((base, ln, role, txt))

    idx = collections.defaultdict(list)
    df = collections.Counter()
    for cid, (_, _, _, txt) in enumerate(corpus):
        for w in set(toks(txt)):
            idx[w].append(cid)
            df[w] += 1

    hits = 0
    for i, role, txt in bturns:
        ws = set(toks(txt))
        if len(ws) < a.minw:
            continue
        rare = sorted(ws, key=lambda w: df.get(w, 0))[:4]
        cand = set()
        for w in rare:
            cand.update(idx.get(w, []))
        best = (0.0, None)
        for cid in cand:
            cs = set(toks(corpus[cid][3]))
            if len(cs) < a.minw:
                continue
            j = len(cs & ws) / len(cs | ws)
            if j > best[0]:
                best = (j, corpus[cid])
        if best[0] >= a.thresh:
            hits += 1
            b, ln, crole, ctxt = best[1]
            print("J=%.3f  batch row %d %s :: %s" % (best[0], i, role, txt[:68]))
            print("          %s L%d %s :: %s" % (b, ln, crole, ctxt[:68]))

    print("corpus turns: %d  batch turns: %d  near-dup hits (J>=%.2f, both>=%dw): %d"
          % (len(corpus), len(bturns), a.thresh, a.minw, hits))


if __name__ == "__main__":
    main()
