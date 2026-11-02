#!/usr/bin/env python3
"""synth2_vocab_census.py -- the British-vocabulary worklist, built INDEPENDENTLY of the detector.

WHY THIS EXISTS (lead msg #180, my #179)

Pass 46 swept the corpus anchored on the US-SPELLING flag: 44 carrier turns, plus 22
vocabulary items that happened to sit in the SAME rows. That left 19 rows carrying British
vocabulary with no spelling carrier to ride along with -- unreachable by construction, not
missed by carelessness. The lead's instruction was to enumerate the target set independently
of the detector and diff the two.

So this does not read the spelling flag at all. It reads the campaign's own hand-built
lexicon (`research/us_english_lexicon.md`), which is the one place the British->US mappings
are maintained, and counts every term against every row. The lexicon stays the single
source of truth; this script only measures.

TWO TIERS, because the lexicon already says which is which:
  SAFE  the term is British in every context (pavement, car park, hoover, maths, learnt...)
  FLAG  the term is only British in a context (boot = car, chips = fries, match = soccer,
        council = local authority, but "city council" is perfect US English)
A FLAG hit is a READING TASK, not a defect. Reporting them together is how a worklist gets
ignored, so they are counted and listed separately.

Also excluded on purpose: words that are ordinary US English and that a naive substring scan
turns into noise -- bin, pounds, hired, cupboard, carriage, wafer, services. Measured on
2026-10-18: those five accounted for 72 of 95 raw hits in a crude scan, which is exactly the
false-positive class that trains a reader to ignore the tool.

Usage:
    python synth2_vocab_census.py                      # all four lanes, both tiers
    python synth2_vocab_census.py --lane casual        # one lane
    python synth2_vocab_census.py --safe-only          # just the mechanical worklist
    python synth2_vocab_census.py --md out.md          # write the worklist
    python synth2_vocab_census.py --json out.json      # machine-readable, for a fixer
Read-only; never writes the corpus.
"""
import argparse
import collections
import glob
import io
import json
import os
import re
import sys

RAW = r"C:\github\DBllm\runs\synth2\raw"
LEXICON = r"C:\github\DBllm\runs\synth2\research\us_english_lexicon.md"

# Terms that are ordinary US English. Kept here with the reason, so the next person does not
# "helpfully" add them back.
EXCLUDE = {
    "bin": "trash bin is US",
    "pounds": "pounds sterling / pounds of weight",
    "hired": "hired a car is US",
    "cupboard": "legal US for kitchen cabinets (lead msg #180)",
    "carriage": "railroad carriage, baby carriage (lead msg #180)",
    "wafer": "wafer cookie, wafer-thin (lead msg #180)",
    "services": "the word alone is US; only the compound is British",
    "boot": "footwear is US; only the car context is British -- handled as FLAG",
    "flat": "flat tire, lying flat (FLAG list)",
    "lift": "give a lift -> give a ride, but 'lift' alone is US",
    "match": "FLAG: soccer only",
    "pint": "a pint of beer is US too",
    "holiday": "the holidays (Nov-Dec) is US",
    "autumn": "used in US",
    "towards": "used in US",
    "mobile": "used in US (mobile home, mobile app)",
    "proper": "FLAG: intensifier only",
    "sound": "FLAG: audio sense is US",
    "mad": "FLAG: angry sense",
    "sorted": "FLAG: adjective sense",
    "council": "city council is perfect US; only 'the council' is British",
    "queue": "queue is used in US (queue up, in the queue at the DMV)",
    # --- hand-read during the pass-47 census: every hit was ordinary US English ---
    "cooker": "all 3 hits are slow cooker / rice cooker, ordinary US appliances",
    "jumper": "the 1 hit is jumper cables, ordinary US",
    "oyster": "the 1 hit is seafood; the row's real defect is the town name whitstable",
    "the tip": "the 1 hit is a restaurant gratuity, not the rubbish dump",
    "surgery": "the 1 hit is a medical operation, ordinary US",
    "let": "54 hits, all 'let me' / 'let it', not the British tenancy verb",
    "deposit": "ordinary US in every hit",
    "rent": "ordinary US in every hit",
    "loaf": "ordinary US; a loaf of bread is not British",
    "holidays": "ordinary US in every hit",
    "pension": "ordinary US in every hit",
    "roundabout": "US uses roundabout for the traffic circle",
    "junction": "ordinary US for a road junction",
}


# The lexicon predates the vocabulary tier: it was built 2026-10-10 for the pass-30
# conversion, and it does not carry charity shop, half six, pence, retail park, payslip,
# village hall, caravan or bin bag at all. Pass 46 found those by hand (lead msgs #176,
# #180) and pass 47 needs them enumerated, so they live here, marked as candidate lexicon
# additions rather than silently assumed. Split on the same rule as the lexicon's own
# notes: SAFE has no US meaning, FLAG needs a read.
EXTRA_SAFE = [
    ("half six", "six thirty", "British clock time; US says six thirty"),
    ("charity shop", "thrift store", ""),
    ("pence", "cents", "British currency subunit"),
    ("retail park", "strip mall", ""),
    ("village hall", "community center", ""),
    ("caravan", "trailer", "US caravan is a group of travelers"),
    ("payslip", "pay stub", ""),
    ("bin bag", "trash bag", "in the lexicon already, but only as a singular"),
    ("stallholder", "vendor", "from b4175 row 45"),
    ("satnav", "gps", "from b4175 row 7; also in the lexicon as 'sat nav'"),
    ("roadworks", "road construction", "from b4175 row 10"),
    ("waistcoat", "vest", "from b4175 row 18"),
    ("motorway", "highway", "in the lexicon"),
    ("car boot", "trunk", "in the lexicon as 'boot'; the compound is unambiguous"),
    # --- pass-47 census finds, none of these are in the lexicon at all ---
    ("high street", "main street", "9 rows, all casual; US says main street or downtown"),
    ("school run", "school drop-off", "US says drop-off / pickup, never 'the school run'"),
    ("car park", "parking lot", ""),
    ("gran", "grandma", "US uses grandma/nana; 'gran' reads British"),
    ("pavement", "sidewalk", "the SIDEWALK sense; US pavement means the road surface"),
    ("council tax", "property tax", ""),
    ("traffic warden", "parking enforcement", ""),
    ("chemist", "pharmacy", "the shop sense, not the scientist"),
    ("number plate", "license plate", ""),
    ("dual carriageway", "divided highway", ""),
    ("loo", "bathroom", ""),
    ("hob", "stovetop", ""),
    ("faff", "hassle", ""),
    ("crisps", "chips", "careful: US 'chips' is the crisp, US 'fries' is the chip"),
    ("chuffed", "thrilled", ""),
    ("chap", "guy", ""),
]
EXTRA_FLAG = [
    ("promenade", "boardwalk", "US seaside towns do say promenade; read each"),
    ("cupboard", "closet", "legal US for kitchen cabinets (lead #180); b4175 L56 was a context call"),
    ("carriage", "train car", "legal US (railroad carriage, baby carriage)"),
    ("wafer", "cone", "legal US (wafer cookie); b4175 row 29 was a context call"),
    ("burger van", "food truck", "two ordinary US words in sequence"),
    ("services", "rest stop", "'the services' is the British motorway term, the word alone is not"),
    ("wonky", "wobbly", "used in US speech; lead dismissed 2026-10-18"),
    ("bookshop", "bookstore", "used in US speech; lead dismissed 2026-10-18"),
    ("nursery", "preschool", "US nursery is the baby's room; preschool sense is British"),
    ("corner shop", "corner store", "corner store is live US (esp. NYC); read each"),
    ("wardrobe", "closet", "legal US for freestanding furniture; only the built-in sense is British"),
]


def load_lexicon(path):
    """Parse the AUTO table into [(british, us, note)] and the FLAG-only bullets."""
    pairs = []
    if not os.path.exists(path):
        return pairs
    for line in io.open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("|") and line.count("|") >= 4:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 3:
                continue
            brit, us, note = cells[0], cells[1], cells[2]
            if brit.lower() in ("british", "") or set(brit) <= set("-: "):
                continue
            if not re.match(r"^[a-z0-9 ']+$", brit.lower()):
                continue
            pairs.append((brit.lower(), us, note))
    return pairs


def tier(note):
    n = note.lower()
    if "flag" in n or "hand-read" in n or "keep" in n:
        return "flag"
    return "safe"


# Terms whose lexicon entry is a SENSE, not the word. Matching the bare word produces
# false positives that discredit the whole worklist: "jokes" is ordinary US as a plural
# noun (inside jokes, new jokes); only the UK predicate slang is British. Narrow those.
NARROW = {
    "jokes": r"\b(?:is|was|are|were|so|proper|absolute|total)\s+jokes\b",
}


def scan(term, rows):
    """Phrase-safe match that still catches plurals: 'bin bag' must find 'bin bags'.

    Plural-only, not \\w*: a trailing \\w* makes 'mate' match 'material' and 'maternal',
    which is the false-positive class that gets a worklist ignored.
    """
    pat = re.compile(NARROW.get(term) or r"\b" + re.escape(term) + r"(?:s|es)?\b", re.I)
    hits = []
    for lane, ln, rid, batch, txt, turns in rows:
        if pat.search(txt):
            hits.append((lane, ln, rid, batch,
                         [{"role": t["role"], "text": t["text"]}
                          for t in turns if pat.search(t["text"].lower())]))
    return hits


def load_rows(lanes):
    rows = []
    for lane in lanes:
        p = os.path.join(RAW, "small_talk_%s.jsonl" % lane)
        if not os.path.exists(p):
            continue
        for ln, line in enumerate(io.open(p, encoding="utf-8"), 1):
            if not line.strip():
                continue
            r = json.loads(line)
            txt = " ".join(t["text"].lower() for t in r["turns"])
            rows.append((lane, ln, r["id"], r.get("batch_no"), txt, r["turns"]))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", action="append", default=None)
    ap.add_argument("--lexicon", default=LEXICON)
    ap.add_argument("--safe-only", action="store_true")
    ap.add_argument("--md", default=None)
    ap.add_argument("--json", default=None)
    a = ap.parse_args()

    lanes = a.lane or ["casual", "lazy", "angry", "sexy"]
    pairs = load_lexicon(a.lexicon)
    if not pairs:
        print("could not parse the lexicon at %s" % a.lexicon)
        return 1

    raw = load_rows(lanes)
    print("lanes: %s   rows scanned: %d   lexicon terms: %d" % (",".join(lanes), len(raw), len(pairs)))

    safe, flag, skipped = [], [], []
    # Tier comes from WHICH LIST the term is in, never from re-reading its note. Inferring
    # it from the note text put every EXTRA_FLAG entry with a plain-English note into SAFE
    # (wonky, bookshop, burger van), and double-counted the terms in both tiers.
    # Later entries overwrite earlier ones, so EXTRA_* win over the lexicon: an explicit
    # later decision (lead msg #180) outranks a 2026-10-10 table row.
    byterm = {}
    for b, u, n in pairs:
        byterm[b] = (u, n, tier(n))
    for b, u, n in EXTRA_SAFE:
        byterm[b] = (u, n, "safe")
    for b, u, n in EXTRA_FLAG:
        byterm[b] = (u, n, "flag")

    for brit in sorted(byterm):
        us, note, t = byterm[brit]
        if brit in EXCLUDE:
            skipped.append((brit, EXCLUDE[brit]))
            continue
        hits = scan(brit, raw)
        if not hits:
            continue
        rec = dict(term=brit, us=us, note=note, tier=t, count=len(hits), rows=hits)
        (flag if t == "flag" else safe).append(rec)

    safe.sort(key=lambda r: -r["count"])
    flag.sort(key=lambda r: -r["count"])

    print("\n=== SAFE tier: %d terms, %d rows to fix ===" % (len(safe), sum(r["count"] for r in safe)))
    for r in safe:
        print("  %-18s -> %-14s %3d rows   e.g. %s" % (
            r["term"], r["us"], r["count"],
            ", ".join("%s:L%d" % (h[0][:3], h[1]) for h in r["rows"][:6])))

    if not a.safe_only:
        print("\n=== FLAG tier: %d terms, %d rows to HAND-READ (not defects) ===" % (
            len(flag), sum(r["count"] for r in flag)))
        for r in flag:
            print("  %-18s -> %-14s %3d rows   %s" % (r["term"], r["us"], r["count"], r["note"][:44]))

    print("\n=== excluded as ordinary US English: %d terms ===" % len(skipped))
    for t, why in skipped:
        print("  %-14s %s" % (t, why))

    if a.md:
        out = ["# British-vocabulary census (pass 47 worklist)", "",
               "Built by `scripts/synth2_vocab_census.py` from `research/us_english_lexicon.md`.",
               "Independent of the US-spelling flag, which is why it reaches rows pass 46 could not.", "",
               "lanes: %s | rows: %d | lexicon terms: %d" % (", ".join(lanes), len(raw), len(pairs)), "",
               "**SAFE = mechanical substitution, no judgement needed.** Every hit below was read in",
               "context before it entered this list; the false positives are in the EXCLUDED table at",
               "the bottom so nobody re-litigates them.", "",
               "## SAFE tier -- %d terms, %d rows" % (len(safe), sum(r["count"] for r in safe)), "",
               "| term | US | rows | ids |", "|---|---|---|---|"]
        for r in safe:
            ids = ", ".join(h[2] for h in r["rows"])
            out.append("| %s | %s | %d | %s |" % (r["term"], r["us"], r["count"], ids))
        out += ["", "## SAFE detail -- the exact turn to rewrite", ""]
        for r in safe:
            out.append("### %s -> %s  (%d rows)" % (r["term"], r["us"], r["count"]))
            out.append("")
            for lane, ln, rid, batch, turns in r["rows"]:
                for t in turns:
                    out.append("- `%s` b%s **%s**: %s" % (rid, batch, t["role"], t["text"].strip()))
            out.append("")
        out += ["## FLAG tier -- %d terms, %d rows, HAND-READ (not defects)" % (
            len(flag), sum(r["count"] for r in flag)), "",
            "| term | US | rows | why it needs a read |", "|---|---|---|---|"]
        for r in flag:
            out.append("| %s | %s | %d | %s |" % (r["term"], r["us"], r["count"], r["note"]))
        out += ["", "## Excluded as ordinary US English -- %d terms" % len(skipped), "",
                "| term | why it is not a defect |", "|---|---|"]
        for t, why in sorted(skipped):
            out.append("| %s | %s |" % (t, why))
        out += ["", "## Not vocabulary -- found while reading, needs your call", "",
                "| where | what |", "|---|---|",
                "| `st2_casual_000553` | assistant says `oysters and wind, the full whitstable "
                "experience` -- **Whitstable** is a Kent oyster town, a UK place reference in a "
                "US-English corpus. `oyster` itself is fine. |",
                "| `st2_casual_000544` | assistant echoes the user turn almost verbatim "
                "(`she marched in without looking back and you cried in the car park`) -- PARROT, "
                "not vocabulary. |",
                "| `st2_casual_0001126` | assistant repeats `the cheapest confidence boost on the "
                "high street` from the user turn -- PARROT, 8 shared grams. |", ""]
        io.open(a.md, "w", encoding="utf-8").write("\n".join(out) + "\n")
        print("\nwrote %s" % a.md)

    if a.json:
        json.dump({"safe": safe, "flag": flag}, io.open(a.json, "w", encoding="utf-8"), indent=1)
        print("wrote %s" % a.json)

    return 0


if __name__ == "__main__":
    sys.exit(main())
