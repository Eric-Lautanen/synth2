"""Pre-check candidate user first turns against the corpus BEFORE composing rows.

Batch 3245 lost 21 whole rows because two blocks were written against premises
another writer had already voiced. The build-time pre-flight found it, but by then
the rows were written. This runs first, on a plain list of candidate lines.

usage:
  python synth2_premisecheck.py candidates.txt [--live small_talk_sexy.jsonl]
                                               [--near 8] [--batch built.json]

candidates.txt -- one candidate first turn per line, blank lines ignored.
Exit code 1 if any candidate is HIT or NEAR (so it can gate a script).
"""
import argparse, collections, glob, json, os, re, sys

RAW = r"C:\github\DBllm\runs\synth2\raw"


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
    ap.add_argument("--live", default=None, help="file to compare against as a whole file")
    ap.add_argument("--near", type=int, default=8, help="shared 6-gram count that means NEAR")
    ap.add_argument("--batch", default=None, help="also check in-batch repeats against this JSON")
    a = ap.parse_args()

    turns = {}                      # normalised turn text -> [(file, line, id)]
    rows = []                       # (file, line, id, [turn texts])
    for p in sorted(glob.glob(os.path.join(RAW, "*.jsonl"))):
        base = os.path.basename(p)
        for n, line in enumerate(open(p, encoding="utf-8"), 1):
            if not line.strip():
                continue
            j = json.loads(line)
            t = [x["text"] for x in j["turns"]]
            rows.append((base, n, j.get("id", "?"), t))
            for x in t:
                turns.setdefault(norm(x), []).append((base, n))

    print(f"corpus: {len(rows)} rows, {len(turns)} distinct turn texts")

    cands = []
    for line in open(a.candidates, encoding="utf-8"):
        line = line.strip()
        if line:
            cands.append(line)

    seen = collections.Counter(norm(c) for c in cands)
    bad = 0
    for c in cands:
        nc = norm(c)
        where = None
        if len(nc.split()) >= 3 and nc in turns:
            where = ("HIT", turns[nc][0])
        else:
            cg = grams(c)
            if cg:
                best = []
                for base, n, rid, t in rows:
                    og = set()
                    for x in t:
                        og |= grams(x)
                    ov = len(cg & og)
                    if ov >= a.near:
                        best.append((ov, base, n))
                if best:
                    best.sort(reverse=True)
                    where = ("NEAR", best[0][1:])
        if seen[nc] > 1:
            where = ("DUP-IN-BATCH", (seen[nc],))
        if where:
            bad += 1
            print(f"  {where[0]:14s} {where[1]}  {c[:72]}")

    print(f"candidates: {len(cands)}   flagged: {bad}")
    print("VERDICT: " + ("BLOCKED -- rewrite these premises" if bad else "CLEAN"))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
