#!/usr/bin/env python3
"""Quantify the PLURAL/INFLECTED gap in the AUTO conversion.

us_convert.build_regex is `\b(term)\b` over the exact lexicon terms, so a
lexicon entry `neighbour` does NOT match `neighbours` (no word boundary between
`r` and `s`). Every inflected British form is therefore left British while its
singular is converted -- an inconsistent register the operator's directive was
meant to remove.

This is a FINDER. It reports every corpus token that (a) is not itself a
lexicon term, (b) has a lexicon term as a strict prefix, and (c) is NOT matched
by the live regex. Some hits are genuine English that is not the British sense
(`sounds` from audio `sound`, `matches` from the noun) -- the point is the list,
a human reads it.

Read-only.
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import us_convert as uc  # noqa: E402

ROOT = os.path.normpath(os.path.join(HERE, ".."))
pairs, flags, skipped = uc.parse_lexicon(uc.LEXICON)
rx, table = uc.build_regex(pairs)

# every single-word british term, so a token's prefix can be looked up
terms = sorted({b.lower() for b, _, _ in pairs if " " not in b}, key=len, reverse=True)
flag_terms = {b.lower() for b, _, _ in flags}

tokens = collections.Counter()
where = collections.defaultdict(list)
for fn in uc.CORPUS_FILES:
    rows = uc.load_rows(os.path.join(ROOT, "raw", fn))
    for ln, row in enumerate(rows, start=1):
        for t in row["turns"]:
            for w in re.findall(r"[a-z']+", t["text"].lower()):
                if w in table or w in terms:
                    continue                       # exact term -> already handled
                for b in terms:                    # longest first
                    if len(w) > len(b) and w.startswith(b):
                        # confirm the live regex really misses it
                        if not re.search(r"\b" + re.escape(b) + r"\b", w):
                            tokens[w] += 1
                            if len(where[w]) < 4:
                                where[w].append(f"L{ln}")
                        break

print(f"inflected forms the AUTO regex MISSES (term -> count, base term):")
print()
tot = 0
for w, c in tokens.most_common():
    base = next((b for b in terms if w.startswith(b) and len(w) > len(b)), "?")
    mark = "  [FLAG]" if base in flag_terms else ""
    print(f"  {c:5d}  {w:<20s} (base {base} -> {table.get(base,'?')}){mark}   {where[w]}")
    tot += c
print()
print(f"TOTAL missed occurrences: {tot}   distinct forms: {len(tokens)}")
print()
print("Genuine-British candidates (exclude words that are ordinary US English):")
# crude filter: show forms whose base is NOT a common US word (heuristic list)
common_us = {"sound", "match", "mad", "tip", "boot", "pint", "curry", "order", "party"}
print("  (the caller must read the list; no auto-verdict)")
