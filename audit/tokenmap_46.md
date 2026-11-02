# synth2 token-attractor map

Generated 2026-10-17 15:06  |  corpus 6250 rows, **8465 assistant turns**, 8465 user turns
Probe: `probe_out46_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-17T12:55:25

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.0% | +0.0 |
| `the`-opener (user) | 13.2% | 13.3% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the end` | - | 7% | - | 13x |
| `a week` | - | 7% | - | 8x |
| `a long` | - | 5% | - | 13x |
| `is worth` | - | 5% | - | 12x |
| `do it` | - | 5% | - | 12x |
| `i will` | - | 5% | - | 8x |
| `is long` | - | 3% | - | 35x |
| `doing it` | - | 3% | - | 35x |
| `means you` | - | 3% | - | 31x |
| `worth it` | - | 5% | - | 7x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 13.3% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 33 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `the end` | 43 | 50.8 | 35.4 | 7% | 13x | casual 26, angry 10, lazy 7 |
| `a week` | 68 | 80.3 | 61.4 | 7% | 8x | casual 36, lazy 22, angry 10 |
| `a long` | 32 | 37.8 | 8.3 | 5% | 13x | casual 21, lazy 8, angry 3 |
| `is worth` | 34 | 40.2 | 4.7 | 5% | 12x | casual 23, angry 5, lazy 5 |
| `do it` | 35 | 41.3 | 8.3 | 5% | 12x | casual 24, lazy 11 |
| `i will` | 50 | 59.1 | 9.5 | 5% | 8x | casual 31, lazy 14, sexy 5 |
| `is long` | 8 | 9.5 | 1.2 | 3% | 35x | casual 6, lazy 2 |
| `doing it` | 8 | 9.5 | 4.7 | 3% | 35x | casual 8 |
| `means you` | 9 | 10.6 | 0.0 | 3% | 31x | lazy 5, sexy 2, angry 1 |
| `worth it` | 60 | 70.9 | 10.6 | 5% | 7x | casual 42, lazy 15, sexy 2 |
| `i am` | 60 | 70.9 | 42.5 | 5% | 7x | casual 44, lazy 11, sexy 4 |
| `of a` | 61 | 72.1 | 27.2 | 5% | 7x | casual 30, angry 15, lazy 15 |
| `at least` | 63 | 74.4 | 15.4 | 5% | 7x | casual 33, angry 20, lazy 9 |
| `the bed` | 12 | 14.2 | 5.9 | 3% | 24x | lazy 7, casual 4, angry 1 |
| `week of` | 14 | 16.5 | 1.2 | 3% | 20x | lazy 7, casual 4, angry 3 |
| `you will` | 15 | 17.7 | 0.0 | 3% | 19x | casual 9, lazy 5, angry 1 |
| `still a` | 15 | 17.7 | 3.5 | 3% | 19x | casual 8, lazy 4, sexy 2 |
| `one is` | 18 | 21.3 | 11.8 | 3% | 16x | casual 13, lazy 4, sexy 1 |
| `it and` | 23 | 27.2 | 23.6 | 3% | 12x | casual 11, lazy 10, angry 2 |
| `what did you` | 28 | 33.1 | 37.8 | 3% | 10x | casual 26, lazy 1, sexy 1 |
| `a single` | 28 | 33.1 | 21.3 | 3% | 10x | angry 27, casual 1 |
| `or a` | 33 | 39.0 | 1.2 | 3% | 9x | casual 25, lazy 4, angry 2 |
| `of it` | 37 | 43.7 | 29.5 | 3% | 8x | casual 30, angry 4, lazy 3 |
| `a full` | 38 | 44.9 | 18.9 | 3% | 7x | lazy 17, angry 12, casual 9 |
| `a bit` | 40 | 47.3 | 37.8 | 3% | 7x | casual 38, angry 1, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.3 | casual 10, lazy 1 |
| `at this point` | 3 | 11 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 11 | 12.1 | angry 6, casual 2, lazy 2 |
| `fell asleep` | 2 | 8 | 11.8 | casual 4, lazy 4 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 11 | 11.7 | casual 8, angry 1, lazy 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `a couple of` | 3 | 12 | 11.4 | casual 11, angry 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `feel like a` | 3 | 10 | 11.3 | lazy 6, casual 3, sexy 1 |
| `has it been` | 3 | 8 | 11.1 | casual 8 |
| `how long did` | 3 | 12 | 11.1 | casual 9, angry 3 |
| `did you find` | 3 | 9 | 10.9 | casual 9 |
| `did you get` | 3 | 44 | 10.8 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.6 | casual 7, lazy 1 |
| `why would a` | 3 | 8 | 10.5 | angry 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the end` | 3 | casual 26, angry 10, lazy 7 |
| `a week` | 3 | casual 36, lazy 22, angry 10 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `is worth` | 4 | casual 23, angry 5, lazy 5, sexy 1 |
| `do it` | 2 | casual 24, lazy 11 |
| `i will` | 3 | casual 31, lazy 14, sexy 5 |
| `is long` | 2 | casual 6, lazy 2 |
| `doing it` | 1 | casual 8 |
| `means you` | 4 | lazy 5, sexy 2, angry 1, casual 1 |
| `worth it` | 4 | casual 42, lazy 15, sexy 2, angry 1 |
| `i am` | 4 | casual 44, lazy 11, sexy 4, angry 1 |
| `of a` | 4 | casual 30, angry 15, lazy 15, sexy 1 |
| `at least` | 4 | casual 33, angry 20, lazy 9, sexy 1 |
| `the bed` | 3 | lazy 7, casual 4, angry 1 |
| `week of` | 3 | lazy 7, casual 4, angry 3 |
| `you will` | 3 | casual 9, lazy 5, angry 1 |
| `still a` | 4 | casual 8, lazy 4, sexy 2, angry 1 |
| `one is` | 3 | casual 13, lazy 4, sexy 1 |
| `it and` | 3 | casual 11, lazy 10, angry 2 |
| `what did you` | 3 | casual 26, lazy 1, sexy 1 |
| `a single` | 2 | angry 27, casual 1 |
| `or a` | 4 | casual 25, lazy 4, angry 2, sexy 2 |
| `of it` | 3 | casual 30, angry 4, lazy 3 |
| `a full` | 3 | lazy 17, angry 12, casual 9 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=8465): a 8.0%, the 3.0%, did 2.6%, how 2.5%, was 2.0%, that 2.0%
- assistant pos 1 (n=8465): the 11.8%, a 2.4%, is 2.1%, you 2.0%, does 1.4%, your 1.0%
- assistant pos 2 (n=8464): the 6.2%, a 3.1%, is 3.1%, are 2.0%, of 1.7%, for 1.7%
- assistant pos last (n=8465): it 4.2%, now 1.4%, time 1.3%, you 1.1%, one 1.0%, again 1.0%
- user pos 0 (n=8465): the 13.3%, my 10.6%, our 8.2%, i 6.7%, they 3.3%, we 3.1%
- user pos 1 (n=8402): the 3.8%, you 2.7%, a 2.2%, was 1.3%, did 1.2%, is 1.1%
- user pos 2 (n=8313): the 6.7%, a 3.0%, is 2.0%, you 1.7%, my 1.4%, and 1.4%
- user pos last (n=8465): again 2.6%, it 1.9%, now 1.5%, week 1.4%, night 1.3%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.2%**; model outputs: **15.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 4 / 268 |
| lazy | 1 / 2155 |

