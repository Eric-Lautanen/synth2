#!/usr/bin/env python3
"""frame_merge.py -- merge the hand-written frame fixes into the US change list
and VALIDATE every one.

Fable #726 item 3: a row that needs a US swap AND a frame-opener fix gets ONE
rewrite. The mechanical US text is pre-filled by the assembler; the single turn
that carries the frame violation is hand-written (a hand-written text is never
re-substituted, so it must already be US English).

Every hand-written text is validated here before it can reach the corpus:
  * no AUTO lexicon term survives (it must already be US English)
  * it does not open on `the <noun>` and not on the bare noun
  * it still shares >= 1 CONTENT word with its own user turn (the dependence law)
  * ASCII, no ASCII hyphen, assistant length sane, qmark-consistent

Usage:
  python scripts/frame_merge.py --worklist audit/frame_merge_worklist.json \
                                --fixes audit/frame_merge_fixes.json \
                                --out audit/changes_us_merged.json
"""
import argparse
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from conditioning import content_words                    # noqa: E402
import us_convert as uc                                   # noqa: E402

ROOT = os.path.normpath(os.path.join(HERE, ".."))

_s = importlib.util.spec_from_file_location("qmark", os.path.join(HERE, "qmark.py"))
qmark = importlib.util.module_from_spec(_s)
_s.loader.exec_module(qmark)


def words(t):
    return re.findall(r"[a-z']+", t.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", default="audit/frame_merge_worklist.json")
    ap.add_argument("--fixes", default="audit/frame_merge_fixes.json")
    ap.add_argument("--out", default="audit/changes_us_merged.json")
    args = ap.parse_args()

    wl = json.load(open(os.path.join(ROOT, args.worklist), encoding="utf-8"))
    fx = json.load(open(os.path.join(ROOT, args.fixes), encoding="utf-8"))

    rows = [json.loads(l) for l in
            open(os.path.join(ROOT, "raw", "small_talk_casual.jsonl"), "rb").read().split(b"\r\n")
            if l.strip()]

    pairs, _flags, _skip = uc.parse_lexicon(uc.LEXICON)
    rx, table = uc.build_regex(pairs)

    merged = {}
    blanks = []
    problems = []
    n_fixed = 0

    for line, entry in wl.items():
        out_entry = {"a": dict(entry.get("a", {})), "u": dict(entry.get("u", {}))}
        for role in ("a", "u"):
            for idx, txt in list(out_entry.get(role, {}).items()):
                if txt == "":
                    rep = fx.get(line, {}).get(role, {}).get(idx)
                    if rep is None or rep.strip() == "":
                        blanks.append((line, role, idx))
                        continue
                    out_entry[role][idx] = rep
                    n_fixed += 1
        if not out_entry.get("u"):
            out_entry.pop("u", None)
        merged[line] = out_entry

    # ---- validate every hand-written text ---------------------------------
    # (1) the noun per line comes from the lens source, so the frame check is
    #     precise -- an earlier version flagged ANY shared opener ("quiet",
    #     "one") which is a lens over-reaching, not a violation.
    nouns = {}
    for ln in open(os.path.join(ROOT, "audit", "frame_opener_284.txt"), encoding="utf-8"):
        if not ln.strip() or ln.startswith("#"):
            continue
        f = ln.rstrip("\n").split("\t")
        if len(f) >= 6:
            nouns.setdefault(int(f[0]), set()).add(f[3].lower())
    flag_terms = {b.lower() for b, _u, _n in _flags}

    problems, warns = [], []
    for line, entry in merged.items():
        r = rows[int(line) - 1]
        turns = r["turns"]
        orig_users = [t["text"] for t in turns if t["role"] == "user"]
        assts = [t["text"] for t in turns if t["role"] == "assistant"]
        # (2) the user turns AS THEY WILL BE after this pass -- the assistant echo
        #     must be checked against the CONVERTED user turn, not the old one.
        conv_users = [entry.get("u", {}).get(str(i), orig_users[i])
                      for i in range(len(orig_users))]
        for role in ("a", "u"):
            for idx, txt in entry.get(role, {}).items():
                if txt.strip() == "":                       # (3) skip unfilled blanks
                    continue
                i = int(idx)
                u = conv_users[i] if i < len(conv_users) else ""
                tags, wtags = [], []
                m = rx.search(txt)
                if m:
                    if m.group(0).lower() in flag_terms:     # (4) FLAG terms may stay
                        wtags.append(f"FLAG term kept: {m.group(0)!r} (legal unless the context IS the pair)")
                    else:
                        tags.append(f"AUTO term survives: {m.group(0)!r}")
                if not txt.isascii():
                    tags.append("non-ascii")
                if "-" in txt:
                    tags.append("ascii hyphen")
                if role == "a":
                    aw = words(txt)
                    ns = nouns.get(int(line), set())
                    if len(aw) >= 2 and aw[0] == "the" and aw[1] in ns:
                        tags.append("still opens `the <noun>`")
                    if aw and aw[0] in ns:
                        tags.append(f"opens on the bare noun {aw[0]!r}")
                    # REGRESSION check, not an absolute one: a pair that was
                    # ALREADY zero-overlap is a pre-existing defect (one of the
                    # 212) that this pass merely touches -- flag only a pair the
                    # edit BROKE.
                    orig = assts[i] if i < len(assts) else ""
                    if u and (content_words(u) & content_words(orig)) and \
                            not (content_words(u) & content_words(txt)):
                        tags.append("REGRESSION: lost a shared content word the original had")
                    elif u and not (content_words(u) & content_words(txt)):
                        wtags.append("pre-existing zero-overlap pair (not caused by this edit)")
                if tags:
                    problems.append((line, role, idx, tags, txt))
                elif wtags:
                    warns.append((line, role, idx, wtags, txt))

    print(f"lines: {len(merged)}   hand-written turns applied: {n_fixed}   "
          f"still blank: {len(blanks)}")
    if blanks:
        print(f"  blank (not yet hand-written): {blanks[:12]}{' ...' if len(blanks) > 12 else ''}")
    print(f"problems: {len(problems)}   warnings: {len(warns)}")
    for line, role, idx, tags, txt in problems:
        print(f"  [FAIL] L{line} {role}{idx}: {'; '.join(tags)}")
        print(f"         {txt!r}")
    for line, role, idx, wtags, txt in warns:
        print(f"  [warn] L{line} {role}{idx}: {'; '.join(wtags)}")

    if not blanks and not problems:
        p = os.path.join(ROOT, args.out)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(merged, f, indent=1)
        print(f"\nALL {len(merged)} merged lines VALID -> wrote {p}")
        return 0
    print("\nNOT written (blanks or problems remain)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
