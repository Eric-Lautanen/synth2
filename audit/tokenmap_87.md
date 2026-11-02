# synth2 token-attractor map

Generated 2026-10-23 23:45  |  corpus 8792 rows, **11212 assistant turns**, 11212 user turns
Probe: `probe_out87_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-23T20:12:48

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.5% | 5.6% | +0.1 |
| `the`-opener (user) | 14.5% | 14.6% | +0.0 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i have` | - | 7% | - | 15x |
| `a good` | 3% | 7% | 6x | 11x |
| `have a` | - | 5% | - | 15x |
| `the phone` | - | 5% | - | 14x |
| `is not` | - | 5% | - | 11x |
| `been a` | - | 3% | - | 47x |
| `and i` | - | 5% | - | 9x |
| `runs out` | - | 3% | - | 42x |
| `nothing on` | - | 3% | - | 42x |
| `time for` | - | 3% | - | 37x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.6% | < 12% |
| `the`-opener (user) | 14.6% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 36 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `i have` | 50 | 44.6 | 78.5 | 7% | 15x | casual 34, lazy 12, sexy 4 |
| `a good` | 67 | 59.8 | 12.5 | 7% | 11x | casual 50, lazy 12, sexy 3 |
| `have a` | 37 | 33.0 | 16.9 | 5% | 15x | sexy 17, casual 11, lazy 7 |
| `the phone` | 41 | 36.6 | 26.8 | 5% | 14x | casual 14, lazy 12, angry 10 |
| `is not` | 51 | 45.5 | 8.9 | 5% | 11x | angry 30, casual 13, lazy 6 |
| `been a` | 8 | 7.1 | 4.5 | 3% | 47x | casual 7, angry 1 |
| `and i` | 62 | 55.3 | 88.3 | 5% | 9x | casual 31, lazy 25, sexy 6 |
| `runs out` | 9 | 8.0 | 8.0 | 3% | 42x | casual 4, formal 3, lazy 2 |
| `nothing on` | 9 | 8.0 | 0.9 | 3% | 42x | casual 8, lazy 1 |
| `time for` | 10 | 8.9 | 1.8 | 3% | 37x | casual 6, lazy 2, sexy 2 |
| `an early` | 12 | 10.7 | 4.5 | 3% | 31x | casual 10, lazy 2 |
| `did you` | 280 | 249.7 | 219.4 | 7% | 3x | casual 187, sexy 57, angry 28 |
| `the first` | 113 | 100.8 | 82.9 | 5% | 5x | lazy 38, casual 36, sexy 22 |
| `have been` | 20 | 17.8 | 38.4 | 3% | 19x | casual 12, lazy 4, sexy 2 |
| `the store` | 25 | 22.3 | 11.6 | 3% | 15x | angry 13, lazy 7, casual 3 |
| `a long` | 33 | 29.4 | 8.0 | 3% | 11x | casual 21, lazy 8, angry 3 |
| `it was` | 41 | 36.6 | 54.4 | 3% | 9x | casual 26, sexy 7, lazy 5 |
| `keep the` | 45 | 40.1 | 5.4 | 3% | 8x | lazy 24, casual 16, formal 3 |
| `the end` | 49 | 43.7 | 31.2 | 3% | 8x | casual 24, angry 10, lazy 7 |
| `you get` | 55 | 49.1 | 44.6 | 3% | 7x | casual 45, angry 5, lazy 5 |
| `at the` | 266 | 237.2 | 230.1 | 5% | 2x | casual 98, sexy 67, lazy 52 |
| `for the` | 295 | 263.1 | 268.5 | 5% | 2x | casual 120, sexy 70, angry 61 |
| `was it` | 83 | 74.0 | 18.7 | 3% | 5x | casual 68, sexy 11, angry 4 |
| `the best` | 92 | 82.1 | 35.7 | 3% | 4x | casual 53, lazy 26, sexy 12 |
| `in a` | 112 | 99.9 | 84.7 | 3% | 3x | casual 29, angry 27, lazy 22 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.8 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 8 | 15.9 | angry 4, lazy 2, casual 1 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the front desk` | 3 | 14 | 12.4 | angry 8, lazy 4, casual 1 |
| `an hour of` | 3 | 18 | 12.4 | angry 6, formal 4, casual 3 |
| `counts as a` | 3 | 12 | 12.2 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `feels like a` | 3 | 8 | 12.0 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `feel like a` | 3 | 11 | 11.0 | lazy 6, casual 4, sexy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i have` | 3 | casual 34, lazy 12, sexy 4 |
| `a good` | 4 | casual 50, lazy 12, sexy 3, formal 2 |
| `have a` | 4 | sexy 17, casual 11, lazy 7, formal 2 |
| `the phone` | 5 | casual 14, lazy 12, angry 10, formal 3 |
| `is not` | 4 | angry 30, casual 13, lazy 6, formal 2 |
| `been a` | 2 | casual 7, angry 1 |
| `and i` | 3 | casual 31, lazy 25, sexy 6 |
| `runs out` | 3 | casual 4, formal 3, lazy 2 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `time for` | 3 | casual 6, lazy 2, sexy 2 |
| `an early` | 2 | casual 10, lazy 2 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `the first` | 5 | lazy 38, casual 36, sexy 22, formal 10 |
| `have been` | 5 | casual 12, lazy 4, sexy 2, angry 1 |
| `the store` | 4 | angry 13, lazy 7, casual 3, sexy 2 |
| `a long` | 4 | casual 21, lazy 8, angry 3, formal 1 |
| `it was` | 5 | casual 26, sexy 7, lazy 5, angry 2 |
| `keep the` | 4 | lazy 24, casual 16, formal 3, angry 2 |
| `the end` | 5 | casual 24, angry 10, lazy 7, sexy 6 |
| `you get` | 3 | casual 45, angry 5, lazy 5 |
| `at the` | 5 | casual 98, sexy 67, lazy 52, angry 38 |
| `for the` | 5 | casual 120, sexy 70, angry 61, lazy 24 |
| `was it` | 3 | casual 68, sexy 11, angry 4 |
| `the best` | 4 | casual 53, lazy 26, sexy 12, angry 1 |
| `in a` | 5 | casual 29, angry 27, lazy 22, sexy 18 |

## 4. Opener maps

- assistant pos 0 (n=11212): a 10.2%, the 5.6%, how 2.3%, did 2.3%, does 1.9%, why 1.7%
- assistant pos 1 (n=11212): the 10.9%, a 2.0%, is 1.8%, you 1.6%, does 1.4%, on 0.9%
- assistant pos 2 (n=11211): the 7.3%, a 3.1%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=11212): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11212): the 14.6%, my 9.6%, our 8.6%, i 6.5%, we 6.1%, you 5.3%
- user pos 1 (n=11149): the 3.1%, you 2.1%, a 1.7%, got 1.0%, is 1.0%, was 1.0%
- user pos 2 (n=11059): the 7.9%, a 3.6%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11212): it 2.2%, again 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.8%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

