#!/usr/bin/env python3
"""dependence_gate.py -- the generation-time gate for the synth2 data pilot.

Fable #709 addition (a): the dependence gate's shared token must be a CONTENT
word (the user's noun), never a function word -- a reply sharing only "the" or
"is" passes a token gate while teaching nothing. This gate therefore reuses
conditioning.py's EXACT content-word definition (lowercased [a-z']+ tokens minus
its stopword list), so "content word" means the same thing here as in the
instrument that measures the finished model.

It also runs the OTHER campaign laws a generated file can silently break, so a
file that passes is a file that could actually be appended:

  * CRLF only (a bare LF makes qmark.py abort corpus-wide)
  * JSON parseable, ids present and unique, structural alternation
  * ASCII only (subsumes emoji and non-ASCII dashes), no ASCII hyphen
  * assistant turns 10-13 words (the medium-reply law)
  * qmark: mirror qmark.py's OWN verdict -- a turn that reads as a question
    (qmark.asks) must carry terminal punctuation. Reuse the authority; never
    out-run it with a raw first-token rule (that rule flagged 70 live turns
    qmark.py flags 0 of -- all declaratives that merely OPEN on a wh/aux word).
  * frame finding: no assistant reply opens on its own noun
  * DEPENDENCE: every (user, assistant) pair shares >= 1 content word

Exit code 1 on any FAIL so it can gate a pipeline. Read-only.

Usage:
  python scripts/dependence_gate.py gen/ranting_worked.jsonl
  python scripts/dependence_gate.py gen/ranting_worked.jsonl --sample 12
"""
import argparse
import collections
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from conditioning import content_words, STOP  # noqa: E402  (the shared definition)

# The campaign law itself. We CALL qmark.asks() rather than re-deriving what
# "asks" means: a hand-rolled first-token rule drifts from the authority, and a
# lens is a finder, never a verdict. qmark.py imports add_rows at module load
# (its own lock/paths setup) but has no side effects at import.
_qspec = importlib.util.spec_from_file_location("qmark", os.path.join(HERE, "qmark.py"))
qmark = importlib.util.module_from_spec(_qspec)
_qspec.loader.exec_module(qmark)

ASST_MIN, ASST_MAX = 10, 13


def words(text):
    return re.findall(r"[a-z']+", text.lower())


def pairs_of(row):
    """EVERY (user, assistant) pair in the row.

    The live corpus is majority multi-turn (1420 short_multi_turn vs 581
    single_turn), so checking only turns[0]/turns[1] would silently ignore most
    of it -- and the generated files are single-turn, so the defect would never
    show up on them. Every dependence check below runs over this list.
    """
    t = row.get("turns", [])
    out = []
    for i in range(0, len(t) - 1, 2):
        if t[i].get("role") == "user" and t[i + 1].get("role") == "assistant":
            out.append((t[i]["text"], t[i + 1]["text"]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--sample", type=int, default=0, help="print N rows verbatim")
    args = ap.parse_args()

    blob = open(args.path, "rb").read()
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print(f"dependence_gate: {args.path}")

    # --- encoding / framing ------------------------------------------------
    bare = blob.count(b"\n") - blob.count(b"\r\n")
    check("CRLF only (no bare LF)", bare == 0, f"{bare} bare LF")
    lines = [l for l in blob.split(b"\r\n") if l.strip()]
    rows, unparseable = [], 0
    for l in lines:
        try:
            rows.append(json.loads(l.decode("utf-8")))
        except Exception:
            unparseable += 1
    check("JSON parseable", unparseable == 0, f"{unparseable} bad lines")
    ids = [r.get("id") for r in rows]
    check("ids present and unique", all(ids) and len(set(ids)) == len(ids),
          f"{len(rows)} rows, {len(set(ids))} unique")

    # --- structural --------------------------------------------------------
    bad_struct = 0
    for r in rows:
        t = r.get("turns", [])
        if not t or t[0]["role"] != "user" or t[-1]["role"] != "assistant":
            bad_struct += 1
            continue
        for i, turn in enumerate(t):
            want = "user" if i % 2 == 0 else "assistant"
            if turn["role"] != want or not turn.get("text", "").strip():
                bad_struct += 1
                break
    check("structural alternation", bad_struct == 0, f"{bad_struct} bad rows")

    # --- character / length laws ------------------------------------------
    nonascii = hyphen = 0
    bad_len = 0
    for r in rows:
        for turn in r["turns"]:
            s = turn["text"]
            if not s.isascii():
                nonascii += 1
            if "-" in s:
                hyphen += 1
            if turn["role"] == "assistant" and not (ASST_MIN <= len(s.split()) <= ASST_MAX):
                bad_len += 1
    check("ASCII only", nonascii == 0, f"{nonascii} turns")
    check("no ASCII hyphen", hyphen == 0, f"{hyphen} turns")
    check(f"assistant {ASST_MIN}-{ASST_MAX} words", bad_len == 0, f"{bad_len} turns")

    # --- qmark law: MIRROR THE AUTHORITY, never out-run it -----------------
    # qmark.py IS the campaign law, and its verdict is fix_line()'s marking set:
    # a turn is "unmarked" only when it carries NO terminal punctuation at all
    # ("?" anywhere, or a trailing "." / "!") AND qmark.asks() reads it as a
    # question. An earlier version of this gate used a raw "first token in
    # WH|AUX" rule, which flagged 70 LIVE turns that qmark.py flags 0 of -- all
    # declaratives that merely OPEN on a wh/aux word:
    #   "had a nightmare getting home"  "will do, and she sends her best"
    #   "was thinking of a quick pint"  "could not put it down"
    # Found by diffing my rule against qmark.asks() directly (scripts/_qmark_diff.py).
    # The hard FAIL is now EXACTLY the authority's verdict, so a green gate means
    # "qmark.py --fix would change nothing". The other two directions are clearly
    # labelled FINDERS (informational), because a lens is a finder, never a verdict.
    unmarked = []   # verdict: qmark.py --fix WOULD mark these -> FAIL
    q_period = 0    # finder only: reads as a question but ends on "." (legal)
    q_odd = 0       # finder only: carries "?" without reading as a question
    for r in rows:
        for turn in r["turns"]:
            s = turn["text"].strip()
            if not s:
                continue
            terminal = "?" in s or s.endswith("!") or s.endswith(".")
            if qmark.asks(s):
                if not terminal:
                    unmarked.append(s)
                elif s.endswith("."):
                    q_period += 1
            elif "?" in s:
                q_odd += 1
    check("qmark law (no unmarked question -- qmark.py's own verdict)",
          not unmarked, f"{len(unmarked)} turns" +
          (f" e.g. {unmarked[:3]}" if unmarked else ""))
    if q_period:
        print(f"  [warn] {q_period} turns read as a question but end on '.' "
              f"(qmark.py tolerates these; a generator should not emit them)")
    if q_odd:
        print(f"  [warn] {q_odd} turns carry '?' without reading as a question "
              f"(legal -- qmark.py never flags these)")

    # --- frame finding: never open a reply on its own noun ------------------
    # The run-11 finding is precise: never lead a reply with `the <noun>`.
    # A naive "first token is a shared word" test FALSE-POSITIVES on discourse
    # openers: a reply can legitimately start on "honestly" when the user turn
    # also did, and that is not the noun. So the check is self-calibrating --
    # a shared word only counts as the NOUN if it never opens a turn anywhere
    # in the file (an opener vocabulary is built from the file itself).
    # --- EVERY (user, assistant) pair, not just the first -------------------
    pairs = []  # (row_index, pair_index, user_text, asst_text)
    for i, r in enumerate(rows):
        for pi, (u, a) in enumerate(pairs_of(r)):
            pairs.append((i, pi, u, a))

    # Built from USER turns ONLY. The previous loop added EVERY turn's first word
    # -- including the very assistant turn it was about to test -- so the
    # `aw[0] not in opener_vocab` condition below was ALWAYS false and this check
    # could never fire (found 2026-10-10; it was dead assurance for the whole
    # campaign). A user-turn opener vocabulary is the honest proxy for "this word
    # is a discourse opener, not the noun": if a shared word never opens a user
    # turn, a reply that opens on it IS leading with the noun.
    opener_vocab = set()
    for r in rows:
        for turn in r["turns"]:
            if turn["role"] != "user":
                continue
            w = words(turn["text"])
            if w:
                opener_vocab.add(w[0])
    noun_first = []
    the_noun = 0
    for i, pi, u, a in pairs:
        aw = words(a)
        shared = content_words(u) & content_words(a)
        if len(aw) >= 2 and aw[0] == "the" and aw[1] in shared:
            the_noun += 1
        if aw and aw[0] in shared and aw[0] not in opener_vocab:
            noun_first.append((i, pi))
    check("no reply opens with `the <noun>`", the_noun == 0, f"{the_noun} pairs")
    check("no reply opens on its own noun", not noun_first,
          f"{len(noun_first)} pairs" + (f" e.g. {noun_first[:5]}" if noun_first else ""))

    # --- THE DEPENDENCE GATE ----------------------------------------------
    shared_sets = [content_words(u) & content_words(a) for _, _, u, a in pairs]
    zero = [k for k, s in enumerate(shared_sets) if not s]
    check("every pair shares >=1 CONTENT word", not zero,
          f"{len(zero)}/{len(pairs)} zero-share" +
          (f" e.g. {[(pairs[k][0], pairs[k][1]) for k in zero[:5]]}" if zero else ""))

    n = max(1, len(pairs))
    ge2 = sum(1 for s in shared_sets if len(s) >= 2)
    mean_ov = sum(len(s) for s in shared_sets) / n
    print(f"\n  pairs {len(pairs)}  zero-share {100.0 * len(zero) / n:.2f}%  "
          f">=2 shared {100.0 * ge2 / n:.1f}%  mean shared content words {mean_ov:.2f}")

    freq = collections.Counter(tok for s in shared_sets for tok in s)
    print("  top shared content words (is the shared token the NOUN?):")
    print("    " + ", ".join(f"{w} {c}" for w, c in freq.most_common(18)))

    # A shared word that is itself a stopword would mean the definition leaked.
    leaked = [w for w in freq if w in STOP]
    check("no stopword counted as shared", not leaked, f"{leaked[:5]}")

    if args.sample:
        print(f"\n  sample of {args.sample} rows:")
        for r in rows[:args.sample]:
            u, a = r["turns"][0]["text"], r["turns"][1]["text"]
            print(f"    U: {u}")
            print(f"    A: {a}   shared={sorted(content_words(u) & content_words(a))}")

    print(f"\nVERDICT: {'ALL GATES GREEN' if not fails else 'FAILED: ' + ', '.join(fails)}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
