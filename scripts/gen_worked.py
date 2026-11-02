#!/usr/bin/env python3
"""gen_worked.py -- ONE-category GENERATOR (the worked example).

Fable #709 decision 1: build ONE category end to end -- generator + dependence
gate + diversity instrument -- gates green, numbers posted, BEFORE any volume.

CATEGORY: the `ranting` register (families commute + delivery) -- a complaint
about a CONCRETE thing. Chosen deliberately: the dependence we want the model to
learn is LEXICAL, so a complaint about a thing makes the echo natural.

THE STRUCTURAL DEPENDENCE (the whole point): the assistant template contains the
SAME surface form `{f}` the user template introduced. Not a lemma, not a synonym
-- the identical token, because the echo law is exact-token (`commitment` !=
`committed`). So every pair shares >=1 content word BY CONSTRUCTION, and the only
open question is whether the SURFACE is varied enough to pass the real gates.

THE REAL CONSTRAINT IS THE NEAR-DUP GATE, not the dependence. prepare.rs drops
any pair whose 3-shingle Jaccard distance < 0.60 (similarity > 0.40) over the
joined conversation. A naive slot-filler (one user frame x one noun) produces
rows that are 60-70% similar and would be dropped en masse. So this generator
(a) uses MULTIPLE independent slots spread through the sentence so any two rows
differ in >=2 shingle positions, and (b) GREEDILY filters candidates through the
EXACT gate logic (`_neardup_replicate.shingle_set`) before accepting one. The
YIELD (candidates tried -> rows accepted, with rejection reasons) is the honest
measure of how much of the template space actually survives.

Deterministic: seeded RNG, so the same command writes the same file.
Read-only outside runs/synth2/gen/ (my claimed dir). Does NOT touch raw/.

Usage:
  python scripts/gen_worked.py --target 1200 --out gen/ranting_worked.jsonl
"""
import argparse
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Reuse the EXACT gate logic the Rust prepare.rs mirrors, and the EXACT
# content-word definition conditioning.py uses. Re-implementing either would let
# this script and the gate drift apart -- and a generator graded by its own
# private rule is not graded at all.
import _neardup_replicate as nd          # noqa: E402
from conditioning import content_words   # noqa: E402

# --- the category: `ranting` (commute + delivery) -------------------------
# `forms` are the surface nouns of complaint. ONE is drawn per row and used in
# BOTH turns, so the echo is the identical token.
FAMILIES = {
    "commute": ["bus", "train", "tube", "tram", "commute", "journey", "line", "service"],
    "delivery": ["parcel", "parcels", "package", "packages", "delivery", "courier",
                 "order", "orders", "consignment", "shipment"],
}
FORMS = [(fam, f) for fam, fs in FAMILIES.items() for f in fs]

# Single-word LEADING openers only: a multi-word opener adds its own content
# words and muddies the "which word is shared" read. These are function-ish /
# register words the assistant frames never use, so the ONLY shared content word
# is the noun. All are attested leading in the live corpus (and 6, so 18, look 2,
# right 5, honestly 6) or are plain casual English; "mate" is NOT, because a
# vocative cannot open a bare clause.
PRE = ["honestly", "look", "and", "so", "right", "god", "blimey",
       "seriously", "anyway"]

# TRAILING tags for the "... , {tag}" frame. The leading list CANNOT be reused
# here -- ", and." / ", so." / ", look." are not English (they cost 85 of 1200
# user turns in the first build) and a tag question takes "?". The live corpus
# writes ", honestly." (12x) and ", right?" (3x) and NEVER ", right.". Each tag
# therefore carries its own terminal punctuation, so the frame stays one format.
TAGS = ["honestly.", "mate.", "right?"]

PROB = ["was late again", "let me down again", "did not turn up", "broke on me",
        "went missing", "was a shambles", "played up", "let me down",
        "was cancelled again", "turned up damaged", "never arrived",
        "was two hours late"]

WHEN = ["this morning", "all week", "again today", "last night", "on monday",
        "for a fortnight", "since tuesday", "every single day", "twice this week",
        "this afternoon"]

# User frames: each has >=2 independent slots spread through the sentence, so
# two rows off the same frame still differ in >=2 shingle positions.
USER_FRAMES = [
    "{pre} the {f} {prob} {when}.",
    "{pre} my {f} {prob} {when}.",
    "{pre} that {f} {prob} {when} again.",
    "the {f} {prob} {when}, {tag}",
    "{pre} i am so fed up with the {f}.",
    "i have had enough of the {f}, {prob} {when}.",
]

# Assistant frames: 10-13 words (checked below), plain English, every one
# contains `{f}`, and NONE opens on the noun (the run-11 frame finding).
ASST_FRAMES = [
    "honestly a {f} like that would drive me up the wall.",
    "have you actually tried ringing them about the {f} yet?",
    "i would be fuming about the {f} as well, no wonder.",
    "what did they actually say about the {f} in the end?",
    "you have every right to be annoyed about the {f}.",
    "does the {f} do that every morning or just some days?",
    "i had the same trouble with the {f} last month, maddening.",
    "what is the plan for the {f} now then?",
    "i would honestly just stop relying on that {f} altogether.",
    "how long has the {f} been like this for you?",
    "a {f} like that sounds like a right pain, honestly.",
    "next time leave the {f} where it is and walk away.",
]

ASST_MIN, ASST_MAX = 10, 13


def wc(text):
    return len(text.split())


def bound(k):
    """The same size-prune _neardup_replicate uses: a pair whose sizes are too
    far apart cannot reach the similarity threshold, so skip it."""
    return max(0, math.ceil(k / (1.0 - nd.MIN_DIST)) - 1)


def passes(sh, size, accepted):
    """True if this shingle set is >= MIN_DIST away from every accepted row."""
    for (sa, sz) in accepted:
        mn, mx = min(size, sz), max(size, sz)
        if mx > bound(mn):
            continue
        union = len(sh | sa)
        d = 0.0 if union == 0 else 1.0 - len(sh & sa) / union
        if d < nd.MIN_DIST:
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="gen/ranting_worked.jsonl")
    ap.add_argument("--target", type=int, default=1200)
    ap.add_argument("--candidates", type=int, default=40000)
    ap.add_argument("--seed", type=int, default=20261010)
    ap.add_argument("--batch-no", type=int, default=9000)
    args = ap.parse_args()

    out = args.out if os.path.isabs(args.out) else os.path.join(HERE, "..", args.out)
    out = os.path.normpath(out)

    rng = random.Random(args.seed)

    rows, accepted, seen_convo = [], [], set()
    tried = 0
    rej_len = rej_dup = rej_near = 0

    while tried < args.candidates and len(rows) < args.target:
        tried += 1
        fam, f = rng.choice(FORMS)
        u = rng.choice(USER_FRAMES).format(pre=rng.choice(PRE), tag=rng.choice(TAGS),
                                           f=f, prob=rng.choice(PROB),
                                           when=rng.choice(WHEN))
        a = rng.choice(ASST_FRAMES).format(f=f)

        # The 10-13 word law, enforced at generation so it is green by construction.
        if not (ASST_MIN <= wc(a) <= ASST_MAX):
            rej_len += 1
            continue
        # The frame finding: never open a reply on the noun.
        if a.split()[0].lower() in (f.lower(), "the"):
            rej_len += 1
            continue

        convo = f"{u} {a}"
        if convo in seen_convo:
            rej_dup += 1
            continue

        sh = nd.shingle_set(convo)
        if not passes(sh, len(sh), accepted):
            rej_near += 1
            continue

        seen_convo.add(convo)
        accepted.append((sh, len(sh)))
        total = wc(u) + wc(a)
        rows.append({
            "id": "st2_genrant_%06d" % (len(rows) + 1),
            "batch_no": args.batch_no,
            "category": {
                "interaction_type": "small_talk",
                "tone": "warm_casual",
                "turn_structure": "single_turn",
                "length_bucket": "short" if total < 20 else "medium",
            },
            "turns": [
                {"role": "user", "text": u},
                {"role": "assistant", "text": a},
            ],
        })

    os.makedirs(os.path.dirname(out), exist_ok=True)
    blob = b"\r\n".join(json.dumps(r, ensure_ascii=False).encode("utf-8")
                        for r in rows) + b"\r\n"
    with open(out, "wb") as fh:
        fh.write(blob)

    print(f"category: ranting (commute+delivery)  forms={len(FORMS)}  "
          f"user_frames={len(USER_FRAMES)}  asst_frames={len(ASST_FRAMES)}")
    print(f"candidates tried {tried}  ->  rows accepted {len(rows)}  "
          f"(yield {100.0 * len(rows) / max(1, tried):.1f}%)")
    print(f"rejected: {rej_len} length/frame, {rej_dup} exact-duplicate convo, "
          f"{rej_near} near-dup (Jaccard dist < {nd.MIN_DIST})")
    print(f"wrote {out} ({len(blob)} bytes, CRLF)")


if __name__ == "__main__":
    main()
