#!/usr/bin/env python3
"""Replicate the Rust near-dup gate (prepare.rs) over a corpus file, optionally
with a compact changes file applied IN MEMORY. Reports every pair whose 3-shingle
Jaccard distance < 0.60 (grammar kinds exempt). Read-only: touches no corpus."""
import json, sys, math, os

GRAMMAR_KINDS = {"tools","memory","distillation","injection_resist","self_direction",
                 "succession","stream","emotion","identity","injection"}
MIN_DIST = 0.60

def load_lines(path):
    raw = open(path, "rb").read()
    return [p for p in raw.split(b"\r\n") if p.strip()]

def asst_texts(row):
    return [t["text"] for t in row["turns"] if t["role"] == "assistant"]

def convo_text(row):
    return " ".join(t["text"] for t in row["turns"] if t["text"])

def shingle_set(text):
    words = text.split()
    if len(words) < 3:
        return set(words)
    return set(" ".join(words[i:i+3]) for i in range(len(words)-2))

def bound(k):
    return max(0, math.ceil(k / (1.0 - MIN_DIST)) - 1)

def main():
    corpus = sys.argv[1]
    changes_path = sys.argv[2] if len(sys.argv) > 2 else None
    lines = load_lines(corpus)
    rows = [json.loads(l) for l in lines]

    applied = 0
    if changes_path:
        changes = json.load(open(changes_path, encoding="utf-8"))
        for key, ch in changes.items():
            ln = int(key)
            row = rows[ln - 1]
            k = 0
            for t in row["turns"]:
                if t["role"] == "assistant":
                    if str(k) in ch:
                        t["text"] = ch[str(k)]
                    k += 1
            applied += 1
    print(f"rows={len(rows)} edits_applied={applied}")

    # Build shingle sets for non-grammar rows only (as the gate does).
    idxs = [i for i, r in enumerate(rows)
            if r.get("category", {}).get("interaction_type", "") not in GRAMMAR_KINDS]
    sets = [shingle_set(convo_text(rows[i])) for i in idxs]
    sizes = [len(s) for s in sets]
    print(f"checked={len(idxs)} (grammar-exempt rows skipped: {len(rows)-len(idxs)})")

    pairs = []
    for a in range(len(idxs)):
        sa = sizes[a]
        for b in range(a):
            sb = sizes[b]
            mn = min(sa, sb)
            if max(sa, sb) > bound(mn):
                continue
            A, B = sets[a], sets[b]
            if not A and not B:
                d = 0.0
            else:
                inter = len(A & B)
                union = len(A | B)
                d = 1.0 - inter / union
            if d < MIN_DIST:
                pairs.append((idxs[b], idxs[a], round(d, 4)))

    print(f"near-dup pairs (dist<{MIN_DIST}): {len(pairs)}")
    for lo, hi, d in pairs[:40]:
        print(f"  line {lo+1} vs line {hi+1}  d={d}")

if __name__ == "__main__":
    main()
