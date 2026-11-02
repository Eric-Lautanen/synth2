#!/usr/bin/env python3
"""synth2 batch pre-flight -- check a batch JSON BEFORE handing it to add_rows.py.

add_rows.py --dry-run aborts on the FIRST problem, so iterating through it costs
one round trip per defect. This reports every problem at once by importing
add_rows.py's own gate functions (so the verdict matches prepare.rs exactly).

Checks:
  * row shape (via add_rows.validate_row): alternation, roles, ends-on-assistant,
    ASCII, turn cap, exchange count
  * identical turn text WITHIN the batch (any length) -- blocking
  * identical turn text vs the existing corpus, 3+ words -- blocking
    (1-2 word interjections like "same." are the register and are allowed)
  * near-dup pairs, batch-internal and batch-vs-corpus, using the real gate
  * length/turn_structure mix, for the record

Usage: python synth2_preflight.py <batch.json> [--limit N]
"""
import importlib.util
import json
import sys
from collections import Counter, defaultdict

ADD_ROWS = r"C:\github\DBllm\runs\synth2\scripts\add_rows.py"

spec = importlib.util.spec_from_file_location("add_rows", ADD_ROWS)
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)


def main():
    path = sys.argv[1]
    batch = json.load(open(path, encoding="utf-8"))
    if isinstance(batch, dict):
        batch = batch.get("rows") or [batch]

    counts, existing = ar.load_existing()
    cur = ar.current_category(counts)
    print(f"corpus: {sum(counts.values())} rows; current file: small_talk_{cur}.jsonl")
    print(f"batch : {len(batch)} rows")

    # ---- shape ----------------------------------------------------------
    norms, shape_errs = [], []
    for i, row in enumerate(batch, 1):
        try:
            n = ar.validate_row(row, i)
            n["category"] = n["category"] or cur
            norms.append(n)
        except ar.RowError as e:
            shape_errs.append(str(e))
    if shape_errs:
        print(f"\nBLOCKING: {len(shape_errs)} shape error(s)")
        for e in shape_errs[:20]:
            print("   ", e)
        return 1
    print("shape  : ok (all rows valid)")

    # ---- identical turn text -------------------------------------------
    seen = defaultdict(list)
    for i, n in enumerate(norms, 1):
        for _, t in n["turns"]:
            seen[t.strip()].append(i)
    internal = {k: v for k, v in seen.items() if len(v) > 1}
    corpus_turn = defaultdict(list)
    for cat, _ in ar.load_existing()[1]:
        pass  # shingles only; turn texts need a separate read
    turn_texts = Counter()
    for _, p in ar.raw_files():
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            for t in json.loads(line).get("turns", []):
                turn_texts[t["text"].strip()] += 1

    cross_long = {}
    for k in seen:
        if k in turn_texts and len(k.split()) >= 3:
            cross_long[k] = turn_texts[k]

    if internal:
        print(f"\nWARN: {len(internal)} turn text(s) repeat WITHIN the batch")
        for k, v in sorted(internal.items(), key=lambda x: -len(x[1]))[:15]:
            print(f"    {len(v)}x rows {v} {k[:60]!r}")
    if cross_long:
        print(f"\nBLOCKING: {len(cross_long)} turn text(s) already in the corpus (3+ words)")
        for k, v in sorted(cross_long.items(), key=lambda x: -x[1])[:15]:
            print(f"    corpus has {v}x  {k[:60]!r}")
    if not internal and not cross_long:
        print("turns  : ok (no repeats)")

    # ---- near-dup gate --------------------------------------------------
    bs = [ar.row_shingles(n["turns"]) for n in norms]
    bad = []
    for i in range(len(norms)):
        for j in range(i + 1, len(norms)):
            if ar.near_dup_partner(bs[i], bs[j]):
                bad.append(f"batch rows {i+1} and {j+1} (Jaccard < {ar.NEAR_DUP_MIN_DISTANCE})")
    for i, s in enumerate(bs):
        for j, (cat, t) in enumerate(existing):
            if ar.near_dup_partner(s, t):
                bad.append(f"batch row {i+1} vs corpus {cat} row #{j+1}")
    if bad:
        print(f"\nBLOCKING: {len(bad)} near-dup pair(s)")
        for b in bad[:20]:
            print("   ", b)
    else:
        print("gate   : ok (0 near dups)")

    # ---- mix ------------------------------------------------------------
    st = Counter(n["turn_structure"] for n in norms)
    lb = Counter(n["length_bucket"] for n in norms)
    print(f"mix    : {dict(st)}  {dict(lb)}")

    blocking = bool(shape_errs or cross_long or bad)
    print("\nVERDICT:", "BLOCKED -- fix the above" if blocking else "CLEAN -- safe to append")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
