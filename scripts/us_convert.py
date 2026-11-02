#!/usr/bin/env python3
"""us_convert.py -- assemble the British->US conversion change list.

Reads the hand-built lexicon (research/us_english_lexicon.md), scans the live
corpus, and emits a changes.json for scripts/apply_rewrites.py. It NEVER writes
the corpus -- it only proposes. Fable #726 item 2: lexicon -> changes.json ->
apply_rewrites.py (safe editor) -> spot-checks -> gates.

MAPPINGS
  * Only AUTO-table rows whose notes do NOT say "hand-read" are applied.
  * A row with a FLAG note still applies its base pair, but EVERY occurrence is
    listed in the FLAG report for a hand read (Fable's protocol step 3).
  * One single-pass alternation regex, longest term first, so a replacement can
    never cascade into another term. Word-boundary, case-preserving.

MERGING (Fable #726 item 3)
  A row that also has a hand-written frame-opener fix
  (JSON: {"<line>": {"<asst_idx>": "new text"}}) gets ONE combined edit: the
  hand-written text WINS for that turn and is not re-substituted, so a US swap
  and a frame fix never run as two campaigns. The script asserts the hand-written
  text carries no AUTO term (it must already be US English).

Usage (from the synth2 dir):
  python scripts/us_convert.py                                  # report only
  python scripts/us_convert.py --out-prefix audit/changes_us    # write changes
  python scripts/us_convert.py --frame-fixes audit/frame_fixes.json
  python scripts/us_convert.py --emit-frame-template            # fill-in sheet
  python scripts/us_convert.py --lines 1-200                    # subset (test)
"""
import argparse
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
RAW = os.path.join(ROOT, "raw")
LEXICON = os.path.join(ROOT, "research", "us_english_lexicon.md")
FRAME_284 = os.path.join(ROOT, "audit", "frame_opener_284.txt")

CORPUS_FILES = ["small_talk_casual.jsonl", "small_talk_ghetto.jsonl"]


# --------------------------------------------------------------------------
# THE INFLECTION GAP (posted #738)
# --------------------------------------------------------------------------
# build_regex is `\b(term)\b` over the EXACT AUTO strings, so `neighbour` does
# NOT match `neighbours` (no word boundary between r and s): every inflected form
# of every AUTO term is left British. Measured on the live corpus: 182 genuine
# occurrences / 34 distinct forms ON TOP OF the ~920 the AUTO table already
# applies. These two tables close it. BOTH ARE OFF BY DEFAULT -- the default
# output stays byte-identical to before this change.
#
# INFLECT_APPLY = mechanical, unambiguous; safe to auto-apply (`--inflect`).
INFLECT_APPLY = [
    ("neighbours", "neighbors"), ("neighbours'", "neighbors'"),
    ("neighbourhood", "neighborhood"), ("neighbourly", "neighborly"),
    ("tyres", "tires"), ("favourite", "favorite"), ("favourites", "favorites"),
    ("organised", "organized"), ("organising", "organizing"), ("organises", "organizes"),
    ("realised", "realized"), ("realising", "realizing"), ("realises", "realizes"),
    ("civilisation", "civilization"),
    ("queues", "lines"), ("queued", "lined up"),
    ("colours", "colors"), ("jumpers", "sweaters"), ("biscuits", "cookies"),
    ("blokes", "guys"), ("programmes", "programs"), ("centres", "centers"),
    ("torches", "flashlights"), ("cookers", "stoves"), ("pints", "beers"),
    ("takeaways", "takeouts"), ("nappies", "diapers"),
    ("honours", "honors"), ("labours", "labors"),
    ("cancelled", "canceled"), ("cancelling", "canceling"),
    ("defence", "defense"), ("licence", "license"),
    ("practising", "practicing"), ("practises", "practices"), ("practised", "practiced"),
    ("hoovering", "vacuuming"), ("hoovered", "vacuumed"),
    ("car parks", "parking lots"), ("pavements", "sidewalks"),
    ("maths", "math"), ("hoover", "vacuum"),
    ("wellingtons", "rain boots"), ("wellies", "rain boots"),
    ("draught", "draft"), ("towards", "toward"),
    # the rest of the -our family (all unambiguous; the AUTO table only had
    # colour/favour/neighbour, so flavour/honour/labour/behaviour/humour were
    # left British)
    ("flavour", "flavor"), ("flavours", "flavors"),
    ("behaviour", "behavior"), ("behaviours", "behaviors"),
    ("humour", "humor"), ("rumour", "rumor"), ("rumours", "rumors"),
    ("odour", "odor"), ("armour", "armor"), ("savour", "savor"),
    ("endeavour", "endeavor"), ("watercolours", "watercolors"),
    ("honoured", "honored"), ("honouring", "honoring"),
    ("neighbouring", "neighboring"),
]

# PHRASE_LEVEL = AUTO rows whose note prescribes a PHRASE, not the bare word, so
# the single-word AUTO value emits a fragment: "a fiver" -> "a five" (note says
# "five bucks"), "a tenner" -> "a ten" ("ten bucks"), "by the pint" -> "by the
# beer" ("grab a pint" -> "grab a beer"), "the mobile one" (a camera) -> "the
# cell one" (note says "mobile phone" -> "cell phone"). Dropped by
# --flag-report-only alongside the FLAG rows; measured 18 broken "a five"/"a ten"
# + 1 "by the beer" + 1 "the cell one" on the live corpus.
PHRASE_LEVEL = ["fiver", "tenner", "pint", "mobile"]

# SCAN_REPORT = context-sensitive judgement calls; REPORT ONLY (`--scan-report`).
# autumn->fall collides with the verb; burnt->burned is optional in US; "dialogue"
# is accepted in US; "skip" is a verb as often as a dumpster; "sellotape" and
# "allotment" need a phrase-level rewrite, not a word swap.
SCAN_REPORT = [
    (r"\bautumn\b", "fall", "collides with the verb 'fall'"),
    (r"\bburnt\b", "burned", "optional in US"),
    (r"\bdialogue\b", "dialog", "accepted in US"),
    (r"\bskip(s)?\b", "dumpster(s)", "verb 'skip' is standard US"),
    (r"\bsellotape\b", "scotch tape", "brand; phrase-level"),
    (r"\ballotment(s)?\b", "community garden(s)", "phrase-level"),
    (r"\blicence\b", "license", "phrase changes: 'driving licence' -> 'driver's license'"),
    (r"\bfortnightly\b", "every two weeks", "phrase-level"),
]


# --------------------------------------------------------------------------
# lexicon
# --------------------------------------------------------------------------
def parse_lexicon(path):
    """-> (pairs, flags, skipped) where pairs = [(british, us, notes)]."""
    pairs, flags, skipped = [], [], []
    in_auto = False
    for line in open(path, encoding="utf-8"):
        s = line.strip()
        if s.startswith("## "):
            in_auto = s.lower().startswith("## auto")
            continue
        if not in_auto or not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 3:
            continue
        b, u, note = cells[0], cells[1], cells[2]
        if b.lower() in ("british", "") or set(b) <= set("-: "):
            continue
        low = note.lower()
        if "hand-read" in low:
            skipped.append((b, u, note))
            continue
        if u.lower() == b.lower() or u.lower().startswith("keep"):
            skipped.append((b, u, note))
            continue
        pairs.append((b, u, note))
        if "flag" in low:
            flags.append((b, u, note))
    return pairs, flags, skipped


def build_regex(pairs):
    """One alternation, longest first, so 'the tip' beats 'tip' and no cascade."""
    terms = sorted({b for b, _, _ in pairs}, key=len, reverse=True)
    rx = re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b", re.I)
    table = {b.lower(): u for b, u, _ in pairs}
    return rx, table


def match_case(src, repl):
    if len(src) > 1 and src.isupper():
        return repl.upper()
    if src[:1].isupper():
        return repl[:1].upper() + repl[1:]
    return repl


def sub_text(text, rx, table, hits):
    def cb(m):
        key = m.group(0).lower()
        us = table.get(key)
        if us is None:
            return m.group(0)
        hits[key] += 1
        return match_case(m.group(0), us)
    return rx.sub(cb, text)


# --------------------------------------------------------------------------
# corpus
# --------------------------------------------------------------------------
def load_rows(path):
    return [json.loads(l) for l in open(path, "rb").read().split(b"\r\n") if l.strip()]


def parse_range(spec, n):
    if not spec:
        return set(range(1, n + 1))
    out = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out |= set(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return {i for i in out if 1 <= i <= n}


# --------------------------------------------------------------------------
# frame-opener worklist (the 284)
# --------------------------------------------------------------------------
def load_frame_fixes(path):
    """{"<line>": {"<asst_idx>": "new text"}} -> {(line, idx): text}."""
    if not path or not os.path.exists(path):
        return {}
    payload = json.load(open(path, encoding="utf-8"))
    out = {}
    for line, ch in payload.items():
        for idx, txt in ch.items():
            if txt.strip():
                out[(int(line), int(idx))] = txt
    return out


def emit_frame_template():
    """A fill-in sheet for the 284, with the correct assistant index per row."""
    fixes = {}
    for ln in open(FRAME_284, encoding="utf-8"):
        if not ln.strip() or ln.startswith("#"):
            continue
        f = ln.rstrip("\n").split("\t")
        if len(f) < 6:
            continue
        line, _batch, pair_idx, noun, user, asst = f[0], f[1], f[2], f[3], f[4], f[5]
        fixes.setdefault(line, {})[pair_idx] = ""
    out = os.path.join(ROOT, "audit", "frame_fixes_template.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(fixes, fh, indent=1)
    print(f"wrote {out}  ({sum(len(v) for v in fixes.values())} rows to hand-write)")
    return out


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lexicon", default=LEXICON)
    ap.add_argument("--out-prefix", default="", help="e.g. audit/changes_us -> changes_us_casual.json")
    ap.add_argument("--frame-fixes", default="", help="hand-written frame-opener rewrites (JSON)")
    ap.add_argument("--emit-frame-template", action="store_true")
    ap.add_argument("--lines", default="", help="subset, e.g. 1-200")
    ap.add_argument("--inflect", action="store_true",
                    help="ALSO apply the mechanical inflected forms (INFLECT_APPLY). "
                         "Default off -> output is byte-identical to before.")
    ap.add_argument("--flag-report-only", action="store_true",
                    help="Do NOT auto-apply the 10 FLAG rows (flat/lift/holiday/chips/"
                         "boot/cheers/mate/proper/sound/match). The lexicon's FLAG-ONLY "
                         "list says 'never auto-replace; script lists occurrences, human "
                         "rewrites'. Default off -> output is byte-identical to before.")
    ap.add_argument("--scan-report", action="store_true",
                    help="ALSO list the context-sensitive SCAN_REPORT terms (report only).")
    args = ap.parse_args()

    if args.emit_frame_template:
        emit_frame_template()
        return 0

    pairs, flags, skipped = parse_lexicon(args.lexicon)
    n_auto = len(pairs)
    n_flag_dropped = 0
    if args.flag_report_only:
        fset = {b.lower() for b, _, _ in flags} | set(PHRASE_LEVEL)
        n_flag_dropped = sum(1 for b, _, _ in pairs if b.lower() in fset)
        pairs = [(b, u, n) for b, u, n in pairs if b.lower() not in fset]
    if args.inflect:
        pairs = pairs + [(b, u, "inflection (INFLECT_APPLY)") for b, u in INFLECT_APPLY]
    rx, table = build_regex(pairs)
    frame_fixes = load_frame_fixes(args.frame_fixes)
    print(f"lexicon: {n_auto} AUTO pairs applied, {len(flags)} FLAG pairs "
          f"(applied + reported), {len(skipped)} hand-read/keep skipped"
          + (f" + {len(INFLECT_APPLY)} INFLECTED forms (--inflect)" if args.inflect else "")
          + (f" - {n_flag_dropped} FLAG pairs made REPORT-ONLY (--flag-report-only)"
             if args.flag_report_only else ""))
    print(f"frame-opener fixes supplied: {len(frame_fixes)}")
    print()

    flag_hits = collections.Counter()
    flag_examples = collections.defaultdict(list)
    term_hits = collections.Counter()
    grand = collections.Counter()

    for fn in CORPUS_FILES:
        path = os.path.join(RAW, fn)
        rows = load_rows(path)
        keep = parse_range(args.lines, len(rows))
        changes = {}
        touched_rows = set()
        by_role = collections.Counter()
        n_sub = 0

        for ln, row in enumerate(rows, start=1):
            if ln not in keep:
                continue
            per_role = collections.defaultdict(dict)
            ui = ai = 0
            for t in row["turns"]:
                role = t["role"]
                idx = ui if role == "user" else ai
                if role == "user":
                    ui += 1
                else:
                    ai += 1
                old = t["text"]

                # frame-opener hand fix wins for that assistant turn
                if role == "assistant" and (ln, idx) in frame_fixes:
                    new = frame_fixes[(ln, idx)]
                    if rx.search(new):
                        print(f"  [WARN] frame fix line {ln} asst {idx} still carries "
                              f"an AUTO term: {rx.search(new).group(0)!r}")
                    if new != old:
                        per_role[role][idx] = new
                        by_role[role] += 1
                        touched_rows.add(ln)
                    continue

                hits = collections.Counter()
                new = sub_text(old, rx, table, hits)
                if new != old:
                    per_role[role][idx] = new
                    by_role[role] += 1
                    touched_rows.add(ln)
                    n_sub += sum(hits.values())
                    term_hits.update(hits)

            if per_role:
                # legacy digit form when only assistant turns change (max compat),
                # explicit a/u form otherwise.
                if set(per_role) == {"assistant"}:
                    changes[str(ln)] = {str(i): v for i, v in per_role["assistant"].items()}
                else:
                    entry = {}
                    for role, key in (("assistant", "a"), ("user", "u")):
                        if per_role.get(role):
                            entry[key] = {str(i): v for i, v in per_role[role].items()}
                    changes[str(ln)] = entry

            # flag contexts, on the ORIGINAL text
            for t in row["turns"]:
                for b, u, note in flags:
                    for m in re.finditer(r"\b" + re.escape(b) + r"\b", t["text"], re.I):
                        flag_hits[b] += 1
                        if len(flag_examples[b]) < 6:
                            s = max(0, m.start() - 30)
                            flag_examples[b].append(f"L{ln} {t['role']}: ...{t['text'][s:m.end()+30]}...")

        grand["rows"] += len(touched_rows)
        grand["user"] += by_role["user"]
        grand["asst"] += by_role["assistant"]
        grand["subs"] += n_sub
        print(f"== {fn}: {len(rows)} rows, {len(changes)} rows to rewrite "
              f"(user turns {by_role['user']}, assistant turns {by_role['assistant']}), "
              f"{n_sub} substitutions")
        if args.out_prefix:
            stem = os.path.splitext(fn)[0].split("_")[-1]
            out = os.path.join(ROOT, f"{args.out_prefix}_{stem}.json")
            with open(out, "w", encoding="utf-8") as fh:
                json.dump(changes, fh, indent=1)
            print(f"   wrote {out}")

    print()
    print(f"TOTAL: {grand['rows']} rows, {grand['user']} user turns, "
          f"{grand['asst']} assistant turns, {grand['subs']} substitutions")
    print()
    print("top substituted terms:")
    for k, v in term_hits.most_common(25):
        print(f"   {v:5d}  {k} -> {table[k]}")
    print()
    print("FLAG report (apply + hand-read every one, protocol step 3):")
    for b, u, note in flags:
        c = flag_hits[b]
        if c:
            print(f"   {c:5d}  {b} -> {u}   [{note[:60]}]")
            for ex in flag_examples[b][:2]:
                print(f"            {ex}")

    if args.scan_report:
        print()
        print("SCAN report (context-sensitive -- REPORT ONLY, never auto-applied):")
        for pat, us, why in SCAN_REPORT:
            n, ex = 0, []
            for fn in CORPUS_FILES:
                rows = load_rows(os.path.join(RAW, fn))
                for ln, row in enumerate(rows, start=1):
                    for t in row["turns"]:
                        for m in re.finditer(pat, t["text"], re.I):
                            n += 1
                            if len(ex) < 3:
                                s = max(0, m.start() - 25)
                                ex.append(f"L{ln} {t['role']}: ...{t['text'][s:m.end()+25]}...")
            if n:
                print(f"   {n:5d}  {pat[2:-2]:<14s} -> {us:<18s} [{why}]")
                for e in ex:
                    print(f"            {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
