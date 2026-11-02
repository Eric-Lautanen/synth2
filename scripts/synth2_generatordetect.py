"""Detect machine-generated (suffixer / slot-fill) rows in a synth2 raw file.

WHY THIS EXISTS
No gate in the suite can see this class. Measured 2026-09-19 on the poisoned
corpus: `repair.exe` read `0 duplicates, 0 near dups` and `spread=1.000`;
`qmark.py` read 0 unmarked; `synth2_verify` read `defects: none`. The generator
MAXIMISES 3-shingle distance, so the one diversity metric the campaign owns
reads PERFECT on machine slop. Every turn text is unique, every row is ASCII,
CRLF, hyphen-free, question-marked. It passes all of it.

The rows look like this:

    remember the school bell that rang five minutes early on Fridays?
      | Friday bells still ring in dreams of summer
      | dreamed summers smell of cut grass
      | grassed smelled runs all holidays

    do you miss the milk crates stacked outside classroom doors?
      | doored stacked still chills all thirds
      | thirded chilled drinks all straws
      | strawed drunk recycles all bottles

TWO INDEPENDENT INSTRUMENTS -- run both, they fail differently.

1. FRAME. An assistant turn ending in `all <noun>`. The generator's closer is
   always `... <verb>s all <plural-or-abstract>`. Hand-written batches in this
   corpus measure 0-3% on this test (the residue is real English: `that is
   all`, `after all`). A generator measures 24-95%. High recall, and the
   ramp across batches is visible, which is how you find where it started.

2. NOVELTY. Share of assistant tokens absent from a reference vocabulary built
   from the registers you trust. Hand-written batches measure 0.00-0.4%. A
   generator measures 7-16%, and the out-of-vocabulary tokens ARE its coinages:
   `kitchened`, `houred`, `sunbeamed`, `lessoned`, `plained`, `shyly`,
   `treed`, `sunned`, `copperplated`, `plasticked`. Highest precision, and it
   names the mechanism. Use it to CONFIRM what the frame test flags.

Do NOT use an "assistant reuses a verb from the user's turn" test. Normal
English does that constantly (`walk` -> `walked`); measured, it flags
hand-written batches at 60%.

Usage:
    python synth2_generatordetect.py <raw-dir>
    python synth2_generatordetect.py <raw-dir> --file small_talk_gossip.jsonl
    python synth2_generatordetect.py <raw-dir> --rows <batch_no>   # triage a MIXED batch

<raw-dir> MUST be the campaign's real runs/synth2/raw. The trusted registers are
read from that same directory, so pointing it at a scratch or single-file folder
gives an empty reference vocabulary and a false SLOP on hand-written rows. The
script now refuses to judge below VOCAB_FLOOR types instead of guessing.
"""

import collections
import glob
import io
import json
import os
import re
import sys

FRAME = re.compile(r"\ball \w+[.!]?$")
TOKEN = re.compile(r"[a-z']+")
# The novelty test is meaningless without a reference vocabulary, and an empty one
# makes EVERY token novel -- so a hand-written batch reads `novel 50%, carry 100%,
# SLOP`. That false alarm is worse than no detector at all: it invites quarantining
# good rows. Below this many types we refuse to emit a verdict.
VOCAB_FLOOR = 500


def turns_of(row):
    """Yield (role, text) from either {role,text} dicts (raw files) or
    [role, text] pairs (synth2_build.py output)."""
    out = []
    for t in row.get("turns", []):
        if isinstance(t, dict):
            out.append((t.get("role"), t.get("text", "")))
        elif isinstance(t, (list, tuple)) and len(t) == 2:
            out.append((t[0], t[1]))
        else:
            raise SystemExit("unreadable turn %r in row %r" % (t, row.get("id")))
    return out
# Novelty is the DISCRIMINATOR, the frame is the LOCATOR. Either alone misfires:
# the frame test flags hand-written batches at 5-6% (real English: `that is all`,
# `after all`, `we split it all`) and novelty alone needs a trusted vocabulary.
# Measured baseline: hand-written = novel 0.00-0.4%; generator = novel 7.3-15.6%.
NOVEL_ALARM = 2.0       # % of out-of-vocabulary assistant tokens
FRAME_STRONG = 10.0     # % of rows with the template closer, when novelty is nonzero
FRAME_FLOOR = 1.0       # % novelty that makes the frame test meaningful
# CONCENTRATION -- how much of the novelty is in how few rows. This is what
# separates "the whole batch is slop" from "a few rows are slop" from "clean,
# but this is a register we have never opened so its period vocabulary is
# legitimately absent from the trusted registers". Measured 2026-09-19:
#   generator   : 58-82% of rows carry novelty, max 3-6 tokens in one row
#   hand-written:  1-2%  of rows carry novelty, max 1
#   mixed batch : 22.6% of rows, max 3   <- b4955, nostalgic
# A register-opening file (small_talk_nostalgic, opened at b4925) inflates the
# bare novelty rate on its own: eiderdown / clothes horse / fretwork / verrucas
# are ordinary words that the ten trusted registers never use. The tell for a
# generator is CONCENTRATION plus the coinages, not the bare rate.
CARRY_WHOLE = 40.0      # % of rows carrying novelty -> the batch is the generator
# Registers with a clean hand-written baseline. Everything else is measured
# against them, so never put a suspect file in this list.
TRUSTED = ["casual", "ghetto", "lazy", "angry", "sexy", "formal",
           "sarcastic", "excited", "gloomy", "anxious"]


def load(path):
    out = []
    for line in io.open(path, encoding="utf-8"):
        if line.strip():
            out.append(json.loads(line))
    return out


def build_vocab(raw_dir, trusted):
    vocab = set()
    for name in trusted:
        p = os.path.join(raw_dir, "small_talk_%s.jsonl" % name)
        if not os.path.exists(p):
            continue
        for row in load(p):
            for turn in row["turns"]:
                vocab.update(TOKEN.findall(turn["text"].lower()))
    return vocab


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    raw_dir = sys.argv[1]
    only = None
    if "--file" in sys.argv:
        only = sys.argv[sys.argv.index("--file") + 1]

    vocab = build_vocab(raw_dir, TRUSTED)
    files = sorted(glob.glob(os.path.join(raw_dir, "*.jsonl")))
    if only:
        files = [f for f in files if f.endswith(only)]

    # The novelty test is meaningless without a reference vocabulary, and an empty
    # one makes EVERY token novel -- so a hand-written batch reads `novel 50%,
    # carry 100%, SLOP`. That false alarm is worse than no detector at all: it
    # invites quarantining good rows. Refuse to judge below VOCAB_FLOOR types.
    # (--rows triage counts words, not vocabulary, so it does not need this.)
    if len(vocab) < VOCAB_FLOOR and "--rows" not in sys.argv:
        missing = [n for n in TRUSTED
                   if not os.path.exists(os.path.join(raw_dir, "small_talk_%s.jsonl" % n))]
        sys.exit(
            "REFUSING TO JUDGE: reference vocabulary is %d types (floor %d).\n"
            "  raw-dir: %s\n"
            "  missing trusted registers: %s\n"
            "The novelty test compares against the TRUSTED registers, which are read\n"
            "from the SAME directory you pass. Point this at the campaign's real\n"
            "runs/synth2/raw. A scratch or single-file directory yields an empty\n"
            "vocabulary, and every token then reads as novel -- which prints a\n"
            "confident and completely false SLOP verdict."
            % (len(vocab), VOCAB_FLOOR, raw_dir, ", ".join(missing) or "(none)"))

    # --oov <batch>: list the out-of-vocabulary tokens behind a novelty alarm.
    # This is the triage that actually decides SLOP vs register artefact. A
    # generator's OOV tokens are suffix-COINAGES (`grassed`, `houred`,
    # `sunbeamed`, `plasticked`). A register artefact's OOV tokens are ordinary
    # words the ten trusted registers happen not to use (`fretwork`, `lorries`,
    # `kippers`, `mantelpiece`). Read the list, do not trust the percentage.
    if "--oov" in sys.argv:
        want = int(sys.argv[sys.argv.index("--oov") + 1])
        for path in files:
            for row in load(path):
                if row.get("batch_no", 0) != want:
                    continue
                ts = turns_of(row)
                oov = sorted(set(
                    w for role, text in ts if role == "assistant"
                    for w in TOKEN.findall(text.lower())
                    if w not in vocab and len(w) > 3))
                if not oov:
                    continue
                print("%-28s b%-6d %s" % (os.path.basename(path), want, " ".join(oov)))
        return

    # --rows <batch>: triage a MIXED batch row by row. The generator's closer is
    # a SHORT frame (`<word>s all <noun>`, 4-6 words) built from a content word in
    # the user's turn; hand-written residue of the same shape sits inside a longer
    # clause (`no, they quit at the top like all greats`, 9 words). So print the
    # word count and the user turn beside every frame hit.
    if "--rows" in sys.argv:
        want = int(sys.argv[sys.argv.index("--rows") + 1])
        for path in files:
            for row in load(path):
                if row.get("batch_no", 0) != want:
                    continue
                ts = turns_of(row)
                last = ts[-1][1]
                if not FRAME.search(last):
                    continue
                wc = len(last.split())
                mark = "GENERATED?" if wc <= 6 else "real english"
                print("%-14s %2dw  %s" % (mark, wc, last))
                print("               <- user: %s" % ts[0][1][:110])
        return

    print("reference vocabulary: %d types from %d trusted registers"
          % (len(vocab), len(TRUSTED)))
    print()

    print("%-30s %-8s %5s %8s %8s %7s %4s  %s" %
          ("file", "batch", "n", "frame%", "novel%", "carry%", "max", "verdict"))
    alarms = []
    for path in files:
        name = os.path.basename(path)
        stats = collections.defaultdict(lambda: [0, 0, 0, 0, 0, 0])
        for row in load(path):
            ts = turns_of(row)
            s = stats[row.get("batch_no", 0)]
            s[0] += 1
            if FRAME.search(ts[-1][1]):
                s[1] += 1
            toks = [w for role, text in ts if role == "assistant"
                    for w in TOKEN.findall(text.lower())]
            s[2] += len(toks)
            nov = sum(1 for w in toks if w not in vocab and len(w) > 3)
            s[3] += nov
            if nov:
                s[4] += 1
                s[5] = max(s[5], nov)
        for b, (n, fr, toks, nov, carry, mx) in sorted(stats.items()):
            frate = 100.0 * fr / n
            nrate = 100.0 * nov / max(toks, 1)
            crate = 100.0 * carry / n
            alarm = (nrate >= NOVEL_ALARM
                     or (frate >= FRAME_STRONG and nrate >= FRAME_FLOOR))
            if not alarm:
                verdict = ""
            elif crate >= CARRY_WHOLE:
                verdict = "SLOP"          # the batch IS the generator
            else:
                verdict = "MIXED"         # a few rows; triage per row (--rows)
            if alarm:
                alarms.append((name, b, n, frate, nrate, verdict))
            print("%-30s b%-7d %5d %7.1f%% %7.2f%% %6.1f%% %4d  %s"
                  % (name, b, n, frate, nrate, crate, mx, verdict))

    print()
    if alarms:
        print("%d SUSPECT batch(es) -- %d rows total:"
              % (len(alarms), sum(a[2] for a in alarms)))
        for name, b, n, frate, nrate, verdict in alarms:
            print("  %-30s b%-7d %4d rows  frame %5.1f%%  novel %5.2f%%  %s"
                  % (name, b, n, frate, nrate, verdict))
        print()
        print("SLOP  = the batch is the generator; quarantine it whole.")
        print("MIXED = a few generated rows inside a hand-written batch. Do NOT")
        print("        quarantine the batch -- list its frame rows and judge them")
        print("        one at a time:  python %s <raw-dir> --rows <batch>"
              % os.path.basename(__file__))
        print()
        print("BEFORE pulling anything, read the tokens behind the alarm:")
        print("  python %s <raw-dir> --oov <batch>" % os.path.basename(__file__))
        print("A generator's novel tokens are suffix-COINAGES (grassed, houred,")
        print("sunbeamed, plasticked). A batch in a register outside the ten trusted")
        print("ones shows ordinary words instead (fretwork, lorries, kippers) --")
        print("that is a register artefact, NOT contamination, and it must not be")
        print("pulled. Measured 2026-09-19: nostalgic b4955 and gossip b4985/b5000")
        print("all read MIXED at 2.2-3.5% on entirely ordinary vocabulary.")
        print()
        print("These rows must NOT stay in raw/. Quarantine them (move, never")
        print("delete) outside runs/synth2/, then hand-review the mixed batches")
        print("before any salvage. Do not re-append salvaged rows by hand --")
        print("they go back in through scripts/add_rows.py.")
    else:
        print("no suspect batches")


if __name__ == "__main__":
    main()
