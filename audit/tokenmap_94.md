# synth2 token-attractor map

Generated 2026-10-25 00:47  |  corpus 9288 rows, **11748 assistant turns**, 11748 user turns
Probe: `probe_out94_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-24T21:17:28

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.0% | 6.1% | +0.1 |
| `the`-opener (user) | 14.8% | 14.8% | -0.0 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `get it` | - | 5% | - | 35x |
| `did you` | - | 8% | - | 3x |
| `are the` | - | 7% | - | 5x |
| `get an` | - | 3% | - | 49x |
| `i will` | 3% | 5% | 7x | 9x |
| `a meeting` | - | 3% | - | 44x |
| `i am` | - | 5% | - | 9x |
| `how did` | - | 5% | - | 8x |
| `is in` | - | 3% | - | 33x |
| `do the` | - | 5% | - | 7x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.1% | < 12% |
| `the`-opener (user) | 14.8% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 38 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `get it` | 17 | 14.5 | 2.6 | 5% | 35x | casual 11, lazy 3, sexy 2 |
| `did you` | 281 | 239.2 | 209.4 | 8% | 3x | casual 187, sexy 57, angry 28 |
| `are the` | 163 | 138.7 | 13.6 | 7% | 5x | lazy 92, casual 61, angry 5 |
| `get an` | 8 | 6.8 | 0.0 | 3% | 49x | casual 5, formal 1, lazy 1 |
| `i will` | 64 | 54.5 | 7.7 | 5% | 9x | casual 31, lazy 14, sexy 10 |
| `a meeting` | 9 | 7.7 | 9.4 | 3% | 44x | formal 4, angry 3, lazy 2 |
| `i am` | 68 | 57.9 | 35.8 | 5% | 9x | casual 46, lazy 11, sexy 10 |
| `how did` | 72 | 61.3 | 8.5 | 5% | 8x | casual 29, sexy 18, angry 17 |
| `is in` | 12 | 10.2 | 8.5 | 3% | 33x | casual 6, lazy 3, formal 2 |
| `do the` | 83 | 70.7 | 9.4 | 5% | 7x | formal 31, casual 28, sexy 13 |
| `it just` | 14 | 11.9 | 3.4 | 3% | 28x | casual 8, formal 3, angry 2 |
| `the job` | 16 | 13.6 | 5.1 | 3% | 24x | casual 6, angry 5, formal 3 |
| `i know` | 19 | 16.2 | 12.8 | 3% | 21x | casual 15, lazy 2, sexy 2 |
| `this morning` | 20 | 17.0 | 67.2 | 3% | 20x | casual 16, angry 2, lazy 1 |
| `three days` | 27 | 23.0 | 18.7 | 3% | 15x | angry 9, casual 8, lazy 4 |
| `the right` | 30 | 25.5 | 4.3 | 3% | 13x | casual 20, angry 4, sexy 3 |
| `and the` | 172 | 146.4 | 208.5 | 5% | 3x | formal 81, casual 55, lazy 15 |
| `is the` | 509 | 433.3 | 79.2 | 7% | 2x | casual 292, lazy 116, angry 50 |
| `or is` | 50 | 42.6 | 5.1 | 3% | 8x | formal 28, casual 17, angry 5 |
| `a full` | 52 | 44.3 | 24.7 | 3% | 8x | lazy 17, sexy 12, angry 11 |
| `you get` | 55 | 46.8 | 42.6 | 3% | 7x | casual 45, angry 5, lazy 5 |
| `that's the` | 60 | 51.1 | 17.9 | 3% | 7x | casual 60 |
| `and i` | 66 | 56.2 | 86.8 | 3% | 6x | casual 31, lazy 25, sexy 6 |
| `on the` | 396 | 337.1 | 327.7 | 5% | 1x | casual 138, sexy 111, lazy 51 |
| `are you` | 114 | 97.0 | 57.9 | 3% | 3x | casual 91, angry 12, sexy 10 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.9 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.3 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 16.0 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `the front desk` | 3 | 14 | 12.2 | angry 8, lazy 4, casual 1 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `how long has` | 3 | 9 | 12.0 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 15 | 11.9 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `in front of` | 3 | 8 | 11.1 | sexy 6, angry 1, formal 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `get it` | 4 | casual 11, lazy 3, sexy 2, angry 1 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `are the` | 5 | lazy 92, casual 61, angry 5, formal 3 |
| `get an` | 4 | casual 5, formal 1, lazy 1, sexy 1 |
| `i will` | 4 | casual 31, lazy 14, sexy 10, formal 9 |
| `a meeting` | 3 | formal 4, angry 3, lazy 2 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `how did` | 4 | casual 29, sexy 18, angry 17, formal 8 |
| `is in` | 4 | casual 6, lazy 3, formal 2, angry 1 |
| `do the` | 5 | formal 31, casual 28, sexy 13, angry 6 |
| `it just` | 4 | casual 8, formal 3, angry 2, sexy 1 |
| `the job` | 5 | casual 6, angry 5, formal 3, lazy 1 |
| `i know` | 3 | casual 15, lazy 2, sexy 2 |
| `this morning` | 4 | casual 16, angry 2, lazy 1, sexy 1 |
| `three days` | 5 | angry 9, casual 8, lazy 4, sexy 4 |
| `the right` | 5 | casual 20, angry 4, sexy 3, lazy 2 |
| `and the` | 5 | formal 81, casual 55, lazy 15, angry 13 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 35 |
| `or is` | 3 | formal 28, casual 17, angry 5 |
| `a full` | 5 | lazy 17, sexy 12, angry 11, casual 9 |
| `you get` | 3 | casual 45, angry 5, lazy 5 |
| `that's the` | 1 | casual 60 |
| `and i` | 4 | casual 31, lazy 25, sexy 6, formal 4 |
| `on the` | 5 | casual 138, sexy 111, lazy 51, angry 50 |
| `are you` | 4 | casual 91, angry 12, sexy 10, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=11748): a 10.2%, the 6.1%, does 2.5%, how 2.3%, did 2.2%, why 1.9%
- assistant pos 1 (n=11748): the 11.2%, a 2.1%, is 1.8%, does 1.7%, you 1.6%, on 0.9%
- assistant pos 2 (n=11747): the 7.4%, a 3.0%, is 2.6%, on 1.9%, of 1.9%, for 1.8%
- assistant pos last (n=11748): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 0.9%, again 0.9%
- user pos 0 (n=11748): the 14.8%, my 9.5%, our 8.9%, i 6.6%, we 5.9%, you 5.1%
- user pos 1 (n=11685): the 3.2%, you 2.0%, a 1.6%, is 1.1%, got 1.0%, was 1.0%
- user pos 2 (n=11595): the 7.9%, a 3.8%, is 1.6%, my 1.3%, you 1.3%, in 1.2%
- user pos last (n=11748): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.1%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.6%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

