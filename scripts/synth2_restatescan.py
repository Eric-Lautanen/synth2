#!/usr/bin/env python3
"""synth2 restatement scan -- find user turns that re-tell their own opener.

WHY THIS EXISTS
No gate in the suite can see this class. A row whose SECOND user turn is a clause
lifted out of its FIRST user turn reads as a stalled exchange: the model is being
taught to answer a probe by repeating the opener. Every gate stays green while it
happens -- `repair` 0 dup / 0 near dup, `qmark` 0 unmarked, `synth2_verify`
`defects: none` -- because the two turns are not identical text, so neither the
duplicate gate nor the near-dup gate fires.

Measured 2026-09-19, gossip batch 3 (b5105, 150 rows). Four rows stalled this way
and all four passed the whole suite:

    u0: ... and he told me mine had been there since the spring ...
    a1: and you never told him?
    u2: he said mine had been there since the spring      <-- 7-word lift
    a3: he keeps a list

    u0: ... the bowls team has a new member ... no one has asked him where from ...
    u2: no one has asked him where from                   <-- 7-word lift

    u0: ... and the singer said so in the paper ...
    u2: the singer said so in the paper                   <-- 7-word lift

    u0: ... four people gave me the same number ...
    u2: four people gave me the same number               <-- 7-word lift

THE MEASURE
Longest shared word run between turn 2 and turn 0, on lowercased alphanumeric
tokens. Flag at >= 5 words. 4 words is ordinary lexical overlap in a short
register; 7 words is a lifted clause.

WHAT IS NOT A DEFECT
Assistant turn 1 ECHOING a key word from the opener is the register, not a bug --
`a tin with a lid?`, `years?`, `every room?`, `wrong?` are the incredulous probe,
and they are exactly how this corpus's short replies work. Only USER turns are
checked, because only a user turn must ADVANCE the exchange.

Usage:
  python synth2_restatescan.py <batch.json> [--min 5]
  python synth2_restatescan.py <raw/small_talk_x.jsonl> [--min 5]

Exit code 1 if anything is flagged, so it can gate a script.
"""
import argparse
import json
import re
import sys


def toks(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower()).split()


def longest_common_run(a, b):
    """Longest run of identical tokens in order (not necessarily contiguous)."""
    best, best_s = 0, ""
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            if k > best:
                best, best_s = k, " ".join(a[i:i + k])
    return best, best_s


def turn_text(t):
    """`turns` is [role, text] pairs in a built batch, dicts in a raw file."""
    return t["text"] if isinstance(t, dict) else t[1]


def load(path):
    """Accept a built batch (.json) or a raw corpus file (.jsonl)."""
    if path.endswith(".json"):
        batch = json.load(open(path, encoding="utf-8"))
        if isinstance(batch, dict):
            batch = batch.get("rows") or [batch]
        return [[turn_text(t) for t in r["turns"]] for r in batch]
    rows = []
    with open(path, encoding="utf-8", newline="") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append([turn_text(t) for t in json.loads(line)["turns"]])
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch", help="built batch .json or raw .jsonl")
    ap.add_argument("--min", type=int, default=5,
                    help="shared word run that counts as a restatement (default 5)")
    a = ap.parse_args()

    rows = load(a.batch)
    print(f"file : {a.batch}  ({len(rows)} rows)")

    hits = 0
    for i, turns in enumerate(rows, 1):
        if len(turns) < 4:
            continue
        run, txt = longest_common_run(toks(turns[0]), toks(turns[2]))
        if run >= a.min:
            hits += 1
            print(f"\nSTALL row {i}  shared run {run} words: {txt!r}")
            print(f"   u0: {turns[0][:110]}")
            print(f"   a1: {turns[1]}")
            print(f"   u2: {turns[2]}")
            print(f"   a3: {turns[3]}")

    print(f"\nuser-turn restatements (>= {a.min} words): {hits}")
    if hits:
        print("Rewrite turn 2 so it ADVANCES the exchange instead of re-telling "
              "turn 0, then re-run.")
    else:
        print("ok: no user turn re-tells its own opener.")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
