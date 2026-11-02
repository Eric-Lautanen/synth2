# pass 49, chunk five -- angry 34 and lazy 2

The last of the class. With all six change files applied, `synth2_parrotscan.py`
returns **0 rows in every lane**.

**Files:** `audit/changes_pass49_chunk5_angry.json` (34 rows),
`audit/changes_pass49_chunk5_lazy.json` (2 rows)
**Apply:** `python scripts/apply_rewrites.py <file> --dry`, then drop `--dry`.
Pass `--file raw/small_talk_angry.jsonl` / `raw/small_talk_lazy.jsonl` -- the
default target is casual and would silently do nothing useful.

## Result

| lane | before | after | rows edited |
|---|---|---|---|
| casual | 238 | 0 | 253 rows in four chunks, 241 of them parrot rows (3 rows needed a second touch, so 238 distinct) |
| angry | 34 | 0 | 34 |
| lazy | 2 | 0 | 2 |
| sexy | 0 | 0 | -- |

Simulated end to end, every file applied in order to a copy of its lane:

    casual  PARROT: 0 rows at 6+ grams
    angry   PARROT: 0 rows at 6+ grams
    lazy    PARROT: 0 rows at 6+ grams

346 edited lines across all six files, scanned against each other: 0 shared
5-grams, 0 near-dups at Jaccard 0.60.

## The angry register

Angry replies are a different animal from casual and I nearly got it wrong. The
corpus band is **strictly 10-13 words in angry** (2161 turns, no exceptions, and
the mode is 10), so the band carries over unchanged. What does not carry over is
the shape: the casual mold is echo, comma, question, and the angry mold is
echo-as-indignant-rhetorical-question -- `how do you put snow tires on the wrong
wheels?`, `who decided to cut the late night service entirely?`.

That mold is the parrot. Restating the complaint back as an incredulous question
is exactly a 6-gram restatement with a question mark on it. So the rewrites keep
the indignation and move it off the restatement: name the failure instead of
repeating the complaint.

    before  u: they padlock the good machines every weekend.
            a: why do they padlock the good machines every single weekend?
    after   a: padlocking the good machines each weekend is a strange kind of management.

Two structural habits in the chunk: `X is not Y, it is Z` and `X is a failure,
not bad luck`. Both are load-bearing for the register, but they are also frames
that repeat, so the cross-line scan was the check that mattered here.

Question share in the 39 edited assistant turns drops 17 -> 5, which looks
alarming and is not: the lane as a whole goes 52.8 to 52.2 pct, because the
questions being removed are the rhetorical echo. The lane still asks more than
half its replies as questions.

## Lazy

Two rows, band 10-13 as well (the lane runs 8-16 in the raw corpus, mode 11-12).
Register is unhurried and practical, so the rewrites are one flat instruction
plus a reason.

## What the gate caught in this chunk

Five lines, four of them mine:

- `a week to settle into` vs `casual:811` (chunk four)
- `minutes of hold music and` vs `casual:535`
- `is a choice not an` vs `angry:1289`
- `at the end is a` vs `angry:778`, twice -- my first two attempts both kept it
- `three in the morning is` shared between my casual `001450` and my angry
  `001006`, which no per-lane check could see

That last one is the argument for the cross-file scan in one line: the same
phrase, in two different lanes, written by me, on the same day.

## Pass 49 is done

274 rows, six files, 0 parrots. Nothing here touches the scene, so pass 50's
87 rows are still the next job and they are now clean on this class, which means
they can be relocated without rewriting them twice.
