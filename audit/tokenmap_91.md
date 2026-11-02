# synth2 token-attractor map

Generated 2026-10-24 11:41  |  corpus 9040 rows, **11480 assistant turns**, 11480 user turns
Probe: `probe_out91_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-24T08:17:07

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.9% | 6.0% | +0.0 |
| `the`-opener (user) | 14.8% | 14.8% | +0.0 |
| copula-only | 0.7% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `in the` | - | 13% | - | 4x |
| `the end` | - | 7% | - | 16x |
| `end up` | - | 5% | - | 38x |
| `i would` | - | 5% | - | 36x |
| `a week` | - | 7% | - | 9x |
| `going to` | 7% | 5% | 24x | 18x |
| `not a` | - | 5% | - | 14x |
| `a full` | - | 5% | - | 11x |
| `is the` | 8% | 8% | 2x | 2x |
| `how long` | - | 5% | - | 8x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.0% | < 12% |
| `the`-opener (user) | 14.8% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 44 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `in the` | 401 | 349.3 | 371.1 | 13% | 4x | casual 164, sexy 73, angry 67 |
| `the end` | 49 | 42.7 | 30.5 | 7% | 16x | casual 24, angry 10, lazy 7 |
| `end up` | 15 | 13.1 | 4.4 | 5% | 38x | casual 7, angry 6, lazy 2 |
| `i would` | 16 | 13.9 | 3.5 | 5% | 36x | casual 8, angry 4, lazy 2 |
| `a week` | 83 | 72.3 | 55.7 | 7% | 9x | casual 35, lazy 22, formal 14 |
| `going to` | 32 | 27.9 | 12.2 | 5% | 18x | casual 18, angry 6, lazy 5 |
| `not a` | 42 | 36.6 | 8.7 | 5% | 14x | angry 21, casual 12, lazy 7 |
| `a full` | 50 | 43.6 | 23.5 | 5% | 11x | lazy 17, sexy 12, angry 11 |
| `is the` | 498 | 433.8 | 79.3 | 8% | 2x | casual 292, lazy 116, angry 50 |
| `how long` | 69 | 60.1 | 15.7 | 5% | 8x | casual 31, sexy 15, formal 13 |
| `is a` | 522 | 454.7 | 68.8 | 8% | 2x | angry 222, casual 147, lazy 116 |
| `start the` | 12 | 10.5 | 0.0 | 3% | 32x | lazy 7, angry 2, casual 2 |
| `lost to` | 12 | 10.5 | 3.5 | 3% | 32x | sexy 8, casual 2, angry 1 |
| `the book` | 13 | 11.3 | 11.3 | 3% | 29x | casual 5, formal 3, lazy 3 |
| `no idea` | 13 | 11.3 | 7.0 | 3% | 29x | casual 11, lazy 2 |
| `has it` | 16 | 13.9 | 2.6 | 3% | 24x | casual 16 |
| `to it` | 19 | 16.6 | 8.7 | 3% | 20x | casual 14, formal 2, lazy 2 |
| `of your` | 19 | 16.6 | 4.4 | 3% | 20x | angry 7, sexy 6, casual 5 |
| `keeps the` | 20 | 17.4 | 3.5 | 3% | 19x | formal 7, lazy 5, casual 3 |
| `up to` | 22 | 19.2 | 19.2 | 3% | 17x | casual 18, sexy 2, angry 1 |
| `it is` | 138 | 120.2 | 53.1 | 5% | 4x | casual 82, lazy 36, angry 10 |
| `on a` | 140 | 122.0 | 66.2 | 5% | 4x | angry 46, casual 40, formal 21 |
| `get the` | 30 | 26.1 | 20.0 | 3% | 13x | casual 16, lazy 8, angry 2 |
| `the way` | 33 | 28.7 | 21.8 | 3% | 12x | casual 20, sexy 7, lazy 4 |
| `did you get` | 41 | 35.7 | 35.7 | 3% | 9x | casual 37, angry 2, lazy 2 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.9 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 16.0 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the front desk` | 3 | 14 | 12.4 | angry 8, lazy 4, casual 1 |
| `an hour of` | 3 | 18 | 12.4 | angry 6, formal 4, casual 3 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `how long has` | 3 | 9 | 12.0 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 11 | 11.8 | casual 7, formal 2, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `feel like a` | 3 | 11 | 11.0 | lazy 6, casual 4, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `in the` | 5 | casual 164, sexy 73, angry 67, lazy 67 |
| `the end` | 5 | casual 24, angry 10, lazy 7, sexy 6 |
| `end up` | 3 | casual 7, angry 6, lazy 2 |
| `i would` | 4 | casual 8, angry 4, lazy 2, sexy 2 |
| `a week` | 5 | casual 35, lazy 22, formal 14, angry 10 |
| `going to` | 5 | casual 18, angry 6, lazy 5, sexy 2 |
| `not a` | 5 | angry 21, casual 12, lazy 7, formal 1 |
| `a full` | 5 | lazy 17, sexy 12, angry 11, casual 9 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 24 |
| `how long` | 5 | casual 31, sexy 15, formal 13, angry 9 |
| `is a` | 5 | angry 222, casual 147, lazy 116, formal 22 |
| `start the` | 4 | lazy 7, angry 2, casual 2, sexy 1 |
| `lost to` | 4 | sexy 8, casual 2, angry 1, lazy 1 |
| `the book` | 4 | casual 5, formal 3, lazy 3, sexy 2 |
| `no idea` | 2 | casual 11, lazy 2 |
| `has it` | 1 | casual 16 |
| `to it` | 4 | casual 14, formal 2, lazy 2, sexy 1 |
| `of your` | 4 | angry 7, sexy 6, casual 5, lazy 1 |
| `keeps the` | 5 | formal 7, lazy 5, casual 3, sexy 3 |
| `up to` | 4 | casual 18, sexy 2, angry 1, formal 1 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 6 |
| `on a` | 5 | angry 46, casual 40, formal 21, lazy 17 |
| `get the` | 5 | casual 16, lazy 8, angry 2, formal 2 |
| `the way` | 5 | casual 20, sexy 7, lazy 4, angry 1 |
| `did you get` | 3 | casual 37, angry 2, lazy 2 |

## 4. Opener maps

- assistant pos 0 (n=11480): a 10.2%, the 6.0%, how 2.4%, does 2.3%, did 2.3%, why 1.8%
- assistant pos 1 (n=11480): the 11.2%, a 2.0%, is 1.7%, you 1.6%, does 1.6%, on 0.9%
- assistant pos 2 (n=11479): the 7.4%, a 3.0%, is 2.6%, on 1.9%, of 1.9%, for 1.8%
- assistant pos last (n=11480): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11480): the 14.8%, my 9.6%, our 8.8%, i 6.6%, we 6.0%, you 5.2%
- user pos 1 (n=11417): the 3.1%, you 2.0%, a 1.6%, is 1.0%, got 1.0%, was 1.0%
- user pos 2 (n=11327): the 8.0%, a 3.7%, is 1.6%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11480): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.1%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.7%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

