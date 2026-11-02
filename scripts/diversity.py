#!/usr/bin/env python3
"""diversity.py -- the MODE-COLLAPSE instrument.

WHY THIS EXISTS. The binding constraint is data volume, and the plan for it is
generation at scale. The failure mode of every generated corpus is the same:
it converges on a handful of shapes. Volume metrics look excellent while the
model gets MORE ungrounded, because a corpus that says the same thing ten
thousand ways teaches the conditional no better than one that says it once.

Nothing in this campaign measured that. `conditioning.py` measures how much a
reply depends on its user turn; `openers.py` measures how concentrated ONE
opener word is; `integrity.py` measures length and function-word shape. None of
them sees "every row is now the same joke with different nouns". This does.

FOUR OBSERVABLES, all computed over ASSISTANT turns (the text the model is
trained to produce):

  opener entropy   Shannon entropy, in bits, of the first word of each assistant
                   turn, plus the normalised value H/log2(V) where V is the
                   number of distinct openers. Higher = more varied. The
                   normalised form is the one to compare across corpora of
                   different sizes.
  distinct-n       for n = 1..5, |distinct n-grams| / |total n-grams|. Falls as
                   a corpus repeats itself. distinct-5 is the sensitive one.
  type/token       |distinct words| / |words|.
  dup-5-gram mass  share of 5-gram occurrences that are NOT the first occurrence
                   of that 5-gram. This is the number that goes up first when
                   generation starts recycling.

Baseline is printed for the LIVE corpus so a generated file can be compared to
it directly. A GENERATED FILE THAT DOES NOT BEAT THE BASELINE ON THESE IS NOT
AN IMPROVEMENT, whatever its row count says.

*** SIZE MATTERS -- READ THIS BEFORE COMPARING TWO FILES. *** distinct-n and
type/token fall as a corpus grows (more text repeats itself), and opener entropy
RISES with size. So comparing a 130K-row generated file against a 2K-row
baseline will show the generated file looking worse on distinct-n for reasons
that have nothing to do with quality. Use `--sample-rows N` to compare at
MATCHED SIZE, or compare only the NORMALISED opener entropy. This was caught by
running the tool on two real files of very different sizes, not by reasoning
about it.

Usage (from the synth2 dir):
  python scripts/diversity.py                                  # live casual file
  python scripts/diversity.py --file raw/generated_x.jsonl
  python scripts/diversity.py --file a.jsonl --compare raw/small_talk_casual.jsonl
  python scripts/diversity.py --file big.jsonl --sample-rows 2001   # size-matched
  python scripts/diversity.py --per-batch 20                   # worst batches by entropy

A LENS IS A FINDER, NEVER A VERDICT: a low-entropy batch is hand-read, never
auto-rejected. A register whose answers legitimately open the same way (sullen:
"fine.") can sit low on purpose.
"""
import argparse
import collections
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conditioning import load_rows  # noqa: E402

WORD = re.compile(r"[a-z']+")


def words(text):
    return WORD.findall(text.lower())


def asst_turns(rows):
    """(row_index, batch_no, text) for every assistant turn, in file order."""
    for ri, r in enumerate(rows):
        b = r.get("batch_no")
        for t in r["turns"]:
            if t.get("role") == "assistant":
                yield ri, b, t["text"]


def ngrams(seq, n):
    return [tuple(seq[i:i + n]) for i in range(len(seq) - n + 1)]


def entropy(counts):
    total = sum(counts.values())
    if total <= 0:
        return 0.0
    h = 0.0
    for c in counts.values():
        p = c / total
        h -= p * math.log2(p)
    return h


def profile(rows):
    """All four observables for one corpus."""
    openers = collections.Counter()
    words_all = []
    per_n = {n: collections.Counter() for n in (1, 2, 3, 4, 5)}
    per_batch = collections.defaultdict(collections.Counter)
    n_turns = 0
    for _, b, text in asst_turns(rows):
        w = words(text)
        if not w:
            continue
        n_turns += 1
        openers[w[0]] += 1
        per_batch[b][w[0]] += 1
        words_all.extend(w)
        for n in per_n:
            per_n[n].update(ngrams(w, n))

    h = entropy(openers)
    v = len(openers)
    norm = h / math.log2(v) if v > 1 else 0.0
    distinct = {}
    for n, c in per_n.items():
        tot = sum(c.values())
        distinct[n] = len(c) / tot if tot else 0.0
    tot5 = sum(per_n[5].values())
    dup5 = (tot5 - len(per_n[5])) / tot5 if tot5 else 0.0
    ttr = len(set(words_all)) / len(words_all) if words_all else 0.0
    return {
        "turns": n_turns,
        "openers": openers,
        "opener_entropy": h,
        "opener_norm": norm,
        "distinct": distinct,
        "ttr": ttr,
        "dup5_mass": dup5,
        "per_batch": per_batch,
    }


def report(name, p):
    print("  assistant turns        %6d" % p["turns"])
    # The normalised ratio H/log2(V) is NOT a collapse detector. V is the count
    # of DISTINCT openers, so when a corpus collapses onto a handful of openers
    # log2(V) shrinks with it and the ratio can read HIGHER during a collapse:
    # the 12-frame generator scored 0.944 against the live corpus's 0.825 while
    # being 91.3% repeated 5-grams. Only trust the ratio when V is large enough
    # for log2(V) to be a stable denominator; otherwise read the absolute bits
    # and dup-5-gram mass.
    v = len(p["openers"])
    if v >= 100:
        norm = "normalised %.3f of max, %d distinct openers" % (p["opener_norm"], v)
    else:
        norm = ("normalised n/a -- only %d distinct openers, so the ratio is "
                "UNRELIABLE; read the bits" % v)
    print("  opener entropy         %6.3f bits   (%s)" % (p["opener_entropy"], norm))
    print("  distinct-1/2/3/4/5     %s"
          % "  ".join("%.3f" % p["distinct"][n] for n in (1, 2, 3, 4, 5)))
    print("  type/token             %6.3f" % p["ttr"])
    print("  dup-5-gram mass        %6.3f  (share of 5-grams that are repeats)" % p["dup5_mass"])
    top = p["openers"].most_common(6)
    tot = sum(p["openers"].values()) or 1
    print("  top openers            %s"
          % ", ".join("%s %.1f%%" % (w, 100.0 * c / tot) for w, c in top))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="raw/small_talk_casual.jsonl")
    ap.add_argument("--compare", default=None,
                    help="a second corpus to print beside the first (usually the live baseline)")
    ap.add_argument("--per-batch", type=int, default=0,
                    help="list the N lowest-entropy batches (the collapse finder)")
    ap.add_argument("--sample-rows", type=int, default=0,
                    help="deterministically stride-subsample to ~N rows, so two "
                         "corpora of different sizes can be compared fairly "
                         "(distinct-n and type/token are size-dependent)")
    args = ap.parse_args()

    path = args.file
    if not os.path.exists(path):
        sys.exit("file not found: %s" % path)
    rows = load_rows(path)

    def subsample(rs, n):
        if n and len(rs) > n:
            stride = max(1, len(rs) // n)
            return rs[::stride][:n]
        return rs

    if args.compare and not os.path.exists(args.compare):
        sys.exit("compare file not found: %s" % args.compare)
    crows = load_rows(args.compare) if args.compare else []

    # Fable #709 addition (b): EVERY comparison runs at MATCHED SIZE. So when a
    # compare file is present the target is the SMALLER of the two (further
    # capped by --sample-rows) and BOTH sides are subsampled to it -- a
    # generated file is never judged against a full-size baseline. Applying
    # --sample-rows to only the primary file was a real defect: it reported the
    # 1200-row generated file against the full 2001-row baseline and attributed
    # the pure size effect to the generator.
    target = args.sample_rows
    if args.compare:
        target = min(target or 10 ** 9, len(rows), len(crows))
    if target:
        rows = subsample(rows, target)
        if args.compare:
            crows = subsample(crows, target)
        print("(stride-subsampled BOTH sides to %d rows for a size-matched read)" % len(rows))

    p = profile(rows)
    print("diversity: %s  (%d rows)" % (path, len(rows)))
    report(path, p)

    if args.compare:
        c = profile(crows)
        print()
        print("diversity: %s  (%d rows)  [BASELINE]" % (args.compare, len(crows)))
        report(args.compare, c)
        print()
        print("  DELTA (this - baseline):")
        print("    opener entropy   %+.3f bits" % (p["opener_entropy"] - c["opener_entropy"]))
        if len(p["openers"]) >= 100 and len(c["openers"]) >= 100:
            print("    opener normalised%+.3f" % (p["opener_norm"] - c["opener_norm"]))
        else:
            print("    opener normalised  n/a (fewer than 100 distinct openers on one side)")
        for n in (1, 2, 3, 4, 5):
            print("    distinct-%d       %+.3f" % (n, p["distinct"][n] - c["distinct"][n]))
        print("    type/token       %+.3f" % (p["ttr"] - c["ttr"]))
        print("    dup-5-gram mass  %+.3f  (negative is better)" % (p["dup5_mass"] - c["dup5_mass"]))
        worse = []
        if p["opener_entropy"] < c["opener_entropy"]:
            worse.append("opener entropy")
        if p["distinct"][5] < c["distinct"][5]:
            worse.append("distinct-5")
        if p["dup5_mass"] > c["dup5_mass"]:
            worse.append("dup-5-gram mass")
        print()
        print("  VERDICT: %s" % ("LESS DIVERSE than baseline on: " + ", ".join(worse)
                                 if worse else "no collapse detected against this baseline"))

    if args.per_batch:
        lows = []
        for b, c in p["per_batch"].items():
            lows.append((entropy(c), sum(c.values()), b, c.most_common(1)[0]))
        lows.sort()
        print()
        print("lowest-entropy batches (collapse finder -- HAND-READ, not a verdict):")
        print("  %-8s %6s %8s  %s" % ("batch", "turns", "entropy", "top opener"))
        for h, n, b, (w, cnt) in lows[:args.per_batch]:
            print("  %-8s %6d %8.3f  %s (%d)" % (b, n, h, w, cnt))


if __name__ == "__main__":
    main()
