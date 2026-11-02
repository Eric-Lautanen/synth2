"""CROSS-STAGED SCAN -- run BEFORE every stage, not just after.

Why this exists (lead msg #174, my #173): every other gate compares a batch to
the CORPUS in raw/. A staged batch is not in raw/ yet, so with two or more
batches staged at once, nothing compares them to EACH OTHER. b4135 and b4145
shipped a verbatim duplicate row that way -- both gates were green, because
b4135 was not in the corpus when b4145 was gated.

What it reports
  1. per-file shape (rows, turns)
  2. pairwise shared 5-grams on ANY turn role, with row numbers on both sides
  3. near-duplicate row pairs across the whole staged queue (3-shingle Jaccard)
  4. combined user turn-1 opener spread, so a queue cannot drift on one opener
     even when each batch looks fine alone

Read-only. Exit code 1 if any shared 5-gram or near-dup is found, so it can be
used as a preflight gate rather than a report you have to read.

Usage
  python synth2_crossstaged.py                 # auto: repo tmp_b4*.txt + %TEMP%
  python synth2_crossstaged.py a.txt b.txt ...  # explicit
  python synth2_crossstaged.py --near 0.5       # looser near-dup threshold
"""
import argparse
import glob
import itertools
import os
import re
import sys
from collections import defaultdict

REPO = r"C:\github\DBllm"
TEMP = os.environ.get("TEMP", r"C:\Users\ericl\AppData\Local\Temp")


def words(t):
    return re.findall(r"[a-z0-9']+", str(t).lower())


def grams(t, n):
    w = words(t)
    return [" ".join(w[i:i + n]) for i in range(len(w) - n + 1)]


def load(path):
    """-> [(row_no, 'u'|'a', text)] in file order."""
    out = []
    for i, line in enumerate(open(path, encoding="ascii"), 1):
        line = line.strip()
        if not line:
            continue
        for j, f in enumerate([x.strip() for x in line.split("|")]):
            out.append((i, "u" if j % 2 == 0 else "a", f))
    return out


def auto_files():
    """One file per batch number, preferring %TEMP% (the writer's live copy).

    Only exact tmp_b<digits>.txt counts: the rewrite-pass outputs
    (tmp_b4085_rewritten.txt etc.) are not staged batches and must not be
    cross-checked as if they were.
    """
    pat = re.compile(r"^tmp_b(\d+)\.txt$")
    best = {}
    for d in (REPO, TEMP):
        for p in sorted(glob.glob(os.path.join(d, "tmp_b*.txt"))):
            m = pat.match(os.path.basename(p))
            if not m:
                continue
            n = int(m.group(1))
            # temp wins ties: it is the copy the writer is still editing
            if n not in best or os.path.normcase(d) == os.path.normcase(TEMP):
                best[n] = p
    return [best[k] for k in sorted(best)]


def rows_of(data):
    """group turns back into (file, rowno, user_text, assistant_text)."""
    rows = []
    for f, turns in data.items():
        cur = {}
        for r, role, t in turns:
            cur.setdefault(r, {"u": [], "a": []})[role].append(t)
        for r in sorted(cur):
            rows.append((f, r, " ".join(cur[r]["u"]), " ".join(cur[r]["a"])))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--near", type=float, default=0.60,
                    help="3-shingle Jaccard threshold for a near-dup row")
    ap.add_argument("--top", type=int, default=15)
    a = ap.parse_args()

    files = a.files or auto_files()
    if len(files) < 2:
        print("fewer than two staged batches; nothing to cross-check")
        return 0

    data = {os.path.basename(f): load(f) for f in files}
    print("staged batches:")
    for f, turns in data.items():
        print(f"  {f:<18s} {len({r for r, _, _ in turns}):3d} rows  {len(turns):4d} turns")

    # ---- 1. pairwise 5-grams, any role -----------------------------------
    print("\n=== shared 5-grams between staged batches ===")
    idx = {}
    for f, turns in data.items():
        d = defaultdict(list)
        for r, role, t in turns:
            for g in set(grams(t, 5)):
                d[g].append((r, role))
        idx[f] = d
    bad = 0
    for x, y in itertools.combinations(sorted(data), 2):
        shared = set(idx[x]) & set(idx[y])
        if not shared:
            continue
        bad += len(shared)
        print(f"\n  {x} x {y}: {len(shared)} shared")
        for g in sorted(shared)[:a.top]:
            print(f"    {g!r}")
            print(f"        {x} {idx[x][g][:3]}   {y} {idx[y][g][:3]}")
    if not bad:
        print("  none")

    # ---- 2. near-duplicate rows across the queue -------------------------
    def sh(t):
        w = words(t)
        return {" ".join(w[i:i + 3]) for i in range(len(w) - 2)}

    allrows = rows_of(data)
    near = 0
    for (f1, r1, u1, a1), (f2, r2, u2, a2) in itertools.combinations(allrows, 2):
        s1, s2 = sh(u1 + " " + a1), sh(u2 + " " + a2)
        if not s1 or not s2:
            continue
        j = len(s1 & s2) / len(s1 | s2)
        if j >= a.near:
            near += 1
            print(f"\n  {j:.2f}  {f1} row {r1}  vs  {f2} row {r2}")
            print(f"        {u1[:76]}")
            print(f"        {u2[:76]}")
    print(f"\n=== near-dup row pairs (>={a.near:.2f}): {near} "
          f"across {len(allrows)} staged rows ===")

    # ---- 3. combined opener spread ---------------------------------------
    print("\n=== combined user turn-1 opener spread ===")
    first = defaultdict(int)
    for f, r, u, _ in allrows:
        w = words(u)
        if w:
            first[w[0]] += 1
    total = sum(first.values()) or 1
    for k, v in sorted(first.items(), key=lambda kv: -kv[1])[:8]:
        print(f"  {k:<10s} {v:3d}  {100.0 * v / total:4.1f} pct")
    print(f"  rows {total}  (cap is 18 of 62 per batch, so ~29 pct on a queue)")

    print("\n==== CROSSSTAGED ====")
    print(f"files={len(data)} rows={len(allrows)} shared_5grams={bad} near_dups={near}")
    ok = (bad == 0 and near == 0)
    print("VERDICT: CLEAN" if ok else "VERDICT: COLLISION")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
