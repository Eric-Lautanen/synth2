# synth2 token-attractor map

Generated 2026-10-25 21:14  |  corpus 9650 rows, **12139 assistant turns**, 12139 user turns
Probe: `probe_out101_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T18:33:18

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 7.7% | 7.9% | +0.2 |
| `the`-opener (user) | 15.0% | 15.0% | +0.0 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `what's the` | - | 5% | - | 34x |
| `just the` | - | 5% | - | 20x |
| `are you` | - | 7% | - | 7x |
| `a good` | - | 5% | - | 9x |
| `the best` | - | 5% | - | 7x |
| `oh no` | - | 3% | - | 22x |
| `in a` | - | 5% | - | 5x |
| `a walk` | - | 3% | - | 18x |
| `did the` | - | 7% | - | 2x |
| `to do` | - | 3% | - | 17x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 7.9% | < 12% |
| `the`-opener (user) | 15.0% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 41 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `what's the` | 18 | 14.8 | 9.9 | 5% | 34x | casual 18 |
| `just the` | 30 | 24.7 | 10.7 | 5% | 20x | casual 19, lazy 6, angry 3 |
| `are you` | 114 | 93.9 | 56.0 | 7% | 7x | casual 91, angry 12, sexy 10 |
| `a good` | 67 | 55.2 | 11.5 | 5% | 9x | casual 50, lazy 12, sexy 3 |
| `the best` | 92 | 75.8 | 33.0 | 5% | 7x | casual 53, lazy 26, sexy 12 |
| `oh no` | 18 | 14.8 | 5.8 | 3% | 22x | casual 18 |
| `in a` | 118 | 97.2 | 84.9 | 5% | 5x | casual 29, angry 27, formal 22 |
| `a walk` | 22 | 18.1 | 10.7 | 3% | 18x | casual 16, angry 2, lazy 2 |
| `did the` | 387 | 318.8 | 57.7 | 7% | 2x | casual 132, angry 130, sexy 75 |
| `to do` | 24 | 19.8 | 18.9 | 3% | 17x | casual 20, angry 2, lazy 1 |
| `in the` | 426 | 350.9 | 403.7 | 7% | 2x | casual 164, sexy 73, angry 67 |
| `two hours` | 30 | 24.7 | 28.8 | 3% | 13x | angry 12, casual 7, lazy 5 |
| `that is` | 167 | 137.6 | 13.2 | 5% | 4x | casual 96, lazy 26, sexy 25 |
| `get a` | 31 | 25.5 | 12.4 | 3% | 13x | casual 17, sexy 6, formal 5 |
| `going to` | 32 | 26.4 | 11.5 | 3% | 13x | casual 18, angry 6, lazy 5 |
| `is just` | 37 | 30.5 | 2.5 | 3% | 11x | lazy 20, angry 11, casual 6 |
| `did you get` | 41 | 33.8 | 33.8 | 3% | 10x | casual 37, angry 2, lazy 2 |
| `it was` | 42 | 34.6 | 53.5 | 3% | 10x | casual 26, sexy 7, lazy 5 |
| `for the` | 320 | 263.6 | 300.7 | 5% | 2x | casual 120, sexy 70, angry 61 |
| `worth it` | 68 | 56.0 | 9.1 | 3% | 6x | casual 43, lazy 15, sexy 9 |
| `was it` | 84 | 69.2 | 18.1 | 3% | 5x | casual 68, sexy 11, angry 4 |
| `on the` | 408 | 336.1 | 332.8 | 5% | 1x | casual 138, sexy 111, formal 58 |
| `it is` | 141 | 116.2 | 51.1 | 3% | 3x | casual 82, lazy 36, angry 10 |
| `to sleep` | 8 | 6.6 | 7.4 | 2% | 25x | angry 3, casual 2, lazy 2 |
| `the ticket` | 8 | 6.6 | 4.9 | 2% | 25x | formal 3, angry 2, casual 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 17.0 | casual 8, angry 2 |
| `shall i add` | 3 | 8 | 16.9 | formal 8 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.3 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 16.0 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.1 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `i will bring` | 3 | 9 | 13.3 | formal 4, casual 3, lazy 2 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.6 | angry 4, casual 4 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `i have been` | 3 | 10 | 12.4 | casual 8, lazy 2 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.2 | formal 5, casual 2, lazy 2 |
| `the office manager` | 3 | 9 | 12.1 | formal 9 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 15 | 12.0 | casual 7, formal 6, angry 1 |
| `the front desk` | 3 | 14 | 11.8 | angry 8, lazy 4, casual 1 |
| `have you got` | 3 | 15 | 11.8 | casual 15 |
| `without a single` | 3 | 10 | 11.7 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `what's the` | 1 | casual 18 |
| `just the` | 4 | casual 19, lazy 6, angry 3, formal 2 |
| `are you` | 4 | casual 91, angry 12, sexy 10, lazy 1 |
| `a good` | 4 | casual 50, lazy 12, sexy 3, formal 2 |
| `the best` | 4 | casual 53, lazy 26, sexy 12, angry 1 |
| `oh no` | 1 | casual 18 |
| `in a` | 5 | casual 29, angry 27, formal 22, lazy 22 |
| `a walk` | 5 | casual 16, angry 2, lazy 2, formal 1 |
| `did the` | 5 | casual 132, angry 130, sexy 75, formal 47 |
| `to do` | 4 | casual 20, angry 2, lazy 1, sexy 1 |
| `in the` | 5 | casual 164, sexy 73, angry 67, lazy 67 |
| `two hours` | 5 | angry 12, casual 7, lazy 5, sexy 4 |
| `that is` | 5 | casual 96, lazy 26, sexy 25, angry 17 |
| `get a` | 4 | casual 17, sexy 6, formal 5, lazy 3 |
| `going to` | 5 | casual 18, angry 6, lazy 5, sexy 2 |
| `is just` | 3 | lazy 20, angry 11, casual 6 |
| `did you get` | 3 | casual 37, angry 2, lazy 2 |
| `it was` | 5 | casual 26, sexy 7, lazy 5, angry 2 |
| `for the` | 5 | casual 120, sexy 70, angry 61, formal 45 |
| `worth it` | 4 | casual 43, lazy 15, sexy 9, angry 1 |
| `was it` | 4 | casual 68, sexy 11, angry 4, formal 1 |
| `on the` | 5 | casual 138, sexy 111, formal 58, lazy 51 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 9 |
| `to sleep` | 4 | angry 3, casual 2, lazy 2, sexy 1 |
| `the ticket` | 5 | formal 3, angry 2, casual 1, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=12139): a 9.9%, the 7.9%, does 2.8%, how 2.2%, did 2.2%, why 1.8%
- assistant pos 1 (n=12139): the 11.2%, a 2.1%, is 1.7%, does 1.6%, you 1.5%, on 0.9%
- assistant pos 2 (n=12138): the 7.3%, a 2.9%, is 2.5%, on 1.9%, of 1.8%, for 1.8%
- assistant pos last (n=12139): it 3.9%, now 1.4%, you 1.2%, time 1.1%, one 0.9%, again 0.9%
- user pos 0 (n=12139): the 15.0%, my 9.4%, our 9.2%, i 6.5%, we 5.8%, you 4.9%
- user pos 1 (n=12076): the 3.4%, you 1.9%, a 1.5%, is 1.2%, got 0.9%, was 0.9%
- user pos 2 (n=11986): the 8.3%, a 3.8%, is 1.6%, my 1.3%, in 1.2%, you 1.2%
- user pos last (n=12139): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.0%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

