#!/usr/bin/env python3
"""Cluster repeated assistant 5-grams into phrase FAMILIES and compare the count
to same-size slices of the LIVE file.

Why this exists: the opener scan is a FIRST-WORD histogram. It is structurally
blind to a construction that lives in the second word onward. Batch 3365 fixed
its pos1 openers exactly as designed and pushed 176 assistant turns into
`and i have <pp>` / `and you have <pp>` -- and the opener scan read 0 flagged the
whole time. This is the instrument that catches that.

Two traps it is built to avoid:
  1. RAW 5-GRAM COUNTS INFLATE ~2x. Overlapping grams of one phrase ("and i have
     a thing", "i have a thing and", "have a thing and i") are three grams of one
     sentence. So group by one-word overlap with union-find and count FAMILIES,
     not grams.
  2. NEVER COMPARE TO ZERO. A random live sample is diverse; a CONTIGUOUS live
     block is what a real authored batch looks like (it was written in one
     sitting, so it repeats itself). Print both. The honest question is not
     "does my batch repeat?" but "does it repeat more than a comparable slice
     of the file it is joining?"

usage:
  python synth2_families.py <batch.json> [small_talk_<name>.jsonl]
"""
import collections
import json
import os
import random
import re
import sys

RAW = r"C:\github\DBllm\runs\synth2\raw"

# the construction frame: "and <subject> have/had/did not <pp>"
NARROW = re.compile(r"\band (i|you|we|he|she) (have|have not|had|did not|didnt) \w+", re.I)


def grams(text, n=5):
    w = re.sub(r"[^a-z0-9 ]", " ", text.lower()).split()
    return [" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))]


def families(texts, min_count=2):
    """Union-find repeated n-grams by one-word overlap -> phrase families."""
    cnt = collections.Counter()
    for t in texts:
        cnt.update(set(grams(t)))
    rep = [g for g, c in cnt.items() if c >= min_count]
    parent = {g: g for g in rep}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i, a in enumerate(rep):
        wa = a.split()
        for b in rep[i + 1:]:
            wb = b.split()
            if wa[1:] == wb[:-1] or wb[1:] == wa[:-1]:
                union(a, b)

    fam = collections.defaultdict(list)
    for g in rep:
        fam[find(g)].append(g)
    out = []
    for root, gs in fam.items():
        total = sum(cnt[g] for g in gs)
        rep_txt = max(gs, key=lambda g: cnt[g])
        out.append((total, len(gs), rep_txt))
    out.sort(reverse=True)
    return out


def load_live(name):
    p = os.path.join(RAW, name)
    rows = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
    return [t["text"] for r in rows for t in r["turns"] if t["role"] == "assistant"]


def main():
    batch_path = sys.argv[1]
    live_name = sys.argv[2] if len(sys.argv) > 2 else None

    batch = json.load(open(batch_path, encoding="utf-8"))
    def turns_of(b):
        out = []
        for r in b:
            for t in r["turns"]:
                out.append(t[1] if isinstance(t, (list, tuple)) else t["text"])
        return out
    # assistant turns only (odd indices)
    aturns = [turns_of(batch)[i] for i in range(1, len(turns_of(batch)), 2)]

    print(f"batch: {batch_path}  ({len(batch)} rows, {len(aturns)} assistant turns)")

    fam = families(aturns)
    n_multi = sum(1 for _, k, _ in fam if k > 1)
    print(f"\nrepeated 5-gram families in BATCH: {len(fam)}  "
          f"({n_multi} of them multi-gram, i.e. real phrase templates)")
    for total, k, txt in fam[:12]:
        print(f"    x{total:<3} grams={k:<2}  {txt!r}")

    nf = sum(1 for t in aturns if NARROW.search(t))
    print(f"\nconstruction 'and X have/had/did not': {nf}/{len(aturns)} = "
          f"{100*nf/len(aturns):.2f}%")

    if not live_name:
        return
    live = load_live(live_name)
    n = len(aturns)
    print(f"\n--- control: same-size slices of {live_name} ({len(live)} assistant turns)")

    random.seed(11)
    for label, sample in (("random sample", random.sample(live, min(n, len(live)))),
                          ("contiguous block", live[:n]),
                          ("contiguous block (mid)", live[len(live)//2:len(live)//2 + n])):
        f = families(sample)
        nm = sum(1 for _, k, _ in f if k > 1)
        print(f"    {label:<22} families={len(f):<4} multi-gram={nm}")

    print("\nVERDICT: batch is a template if its multi-gram family count is far")
    print("above every contiguous block above -- not above the random sample.")


if __name__ == "__main__":
    main()
