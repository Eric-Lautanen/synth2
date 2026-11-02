#!/usr/bin/env python3
"""Per-position first-word histogram for a synth2 register, WITH the cap the
build/preflight actually applies:  cap = max(3 x ref_share, 8.0%)

Why this exists: the opener gate is `share > 3 x live AND share > 8% absolute`,
so on a 150-row batch most positions CANNOT flag at all. Compute the caps from
the reference BEFORE composing or rebalancing -- aiming at zero wastes rewrites
and can create new collisions. Batch 6065 learned this the hard way.

usage:
  synth2_caps.py --aggregate                # the whole corpus (default)
  synth2_caps.py --file small_talk_lazy.jsonl
  synth2_caps.py --file <abs path>
  synth2_caps.py --aggregate --rows 150     # also print the per-batch row cap
"""
import argparse, collections, glob, json, os, sys

RAW = r"C:\github\DBllm\runs\synth2\raw"


def load(paths):
    rows = []
    for p in paths:
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            j = json.loads(line)
            rows.append([t["text"] for t in j["turns"]])
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=None)
    ap.add_argument("--aggregate", action="store_true")
    ap.add_argument("--rows", type=int, default=150, help="batch size, for the row cap")
    a = ap.parse_args()

    if a.file:
        p = a.file if os.path.isabs(a.file) else os.path.join(RAW, a.file)
        paths = [p]
        label = os.path.basename(p)
    else:
        paths = sorted(glob.glob(os.path.join(RAW, "*.jsonl")))
        label = "corpus aggregate (%d files)" % len(paths)

    rows = load(paths)
    pos = collections.defaultdict(collections.Counter)
    pn = collections.Counter()
    for r in rows:
        for j, t in enumerate(r):
            w = t.strip().split(" ")[0].lower()
            pos[j][w] += 1
            pn[j] += 1

    print("reference: %s   rows: %d" % (label, len(rows)))
    print("cap = max(3 x share, 8.0%%);  a 150-row batch flags only above the cap AND >8% abs\n")
    for j in sorted(pn):
        print("pos%d  n=%d   (a %d-row batch: pos n=%d)" % (j, pn[j], a.rows, a.rows if j < 2 else 0))
        for w, c in pos[j].most_common(12):
            share = 100.0 * c / pn[j]
            cap = max(3.0 * share, 8.0)
            print("    %-14s %6.2f%%   cap %6.2f%%" % (w, share, cap))
        print()


if __name__ == "__main__":
    main()
