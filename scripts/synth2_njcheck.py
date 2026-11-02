# -*- coding: utf-8 -*-
"""Check candidate turns against the whole synth2 corpus:
   - exact raw-string occurrences
   - max punctuation-stripped word-set Jaccard (both turns >=6 words)"""
import io, os, re, sys, glob, json

RAW = r"C:\github\DBllm\runs\synth2\raw"

def norm(s):
    return set(re.sub(r"[^a-z0-9 ]", " ", s.lower()).split())

def jac(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

corpus = []   # (file, line, role, text)
rawset = {}
for p in sorted(glob.glob(os.path.join(RAW, "*.jsonl"))):
    fn = os.path.basename(p)
    for i, line in enumerate(io.open(p, encoding="utf-8"), 1):
        line = line.strip()
        if not line: continue
        r = json.loads(line)
        for t in r["turns"]:
            txt = t["text"]
            rawset.setdefault(txt, []).append((fn, i))
            corpus.append((fn, i, t["role"], txt))

print("corpus turns:", len(corpus))

for cand in sys.argv[1:]:
    cn = norm(cand)
    nw = len(cand.split())
    hits = []
    if nw >= 6:
        for fn, i, role, txt in corpus:
            if len(txt.split()) < 6: continue
            j = jac(cn, norm(txt))
            if j >= 0.60:
                hits.append((j, fn, i, role, txt))
    hits.sort(reverse=True)
    ex = rawset.get(cand, [])
    print("\nCAND: %s" % cand)
    print("  exact raw match:", ex if ex else "none")
    for j, fn, i, role, txt in hits[:3]:
        print("  J=%.3f %s L%d %s :: %s" % (j, fn, i, role, txt))
    if not hits:
        print("  no J>=0.60 hit")
