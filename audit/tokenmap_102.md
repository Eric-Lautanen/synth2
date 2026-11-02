# synth2 token-attractor map

Generated 2026-10-26 01:04  |  corpus 9675 rows, **12166 assistant turns**, 12166 user turns
Probe: `probe_out102_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T21:14:03

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 7.9% | 8.2% | +0.2 |
| `the`-opener (user) | 15.0% | 15.0% | +0.0 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `get to` | - | 5% | - | 47x |
| `this week` | - | 5% | - | 16x |
| `it is` | 3% | 7% | 3x | 6x |
| `i have` | - | 5% | - | 12x |
| `i've got` | - | 3% | - | 51x |
| `i am` | - | 5% | - | 9x |
| `my mom` | - | 3% | - | 29x |
| `and i'm` | - | 3% | - | 29x |
| `you actually` | - | 3% | - | 23x |
| `than you` | - | 3% | - | 23x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 8.2% | < 12% |
| `the`-opener (user) | 15.0% | n/a |
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
| `get to` | 13 | 10.7 | 1.6 | 5% | 47x | casual 5, angry 4, formal 2 |
| `this week` | 37 | 30.4 | 45.2 | 5% | 16x | casual 22, formal 5, angry 4 |
| `it is` | 141 | 115.9 | 51.0 | 7% | 6x | casual 82, lazy 36, angry 10 |
| `i have` | 50 | 41.1 | 75.6 | 5% | 12x | casual 34, lazy 12, sexy 4 |
| `i've got` | 8 | 6.6 | 9.0 | 3% | 51x | casual 8 |
| `i am` | 68 | 55.9 | 34.5 | 5% | 9x | casual 46, lazy 11, sexy 10 |
| `my mom` | 14 | 11.5 | 14.0 | 3% | 29x | casual 14 |
| `and i'm` | 14 | 11.5 | 9.9 | 3% | 29x | casual 13, sexy 1 |
| `you actually` | 18 | 14.8 | 3.3 | 3% | 23x | casual 11, lazy 5, angry 2 |
| `than you` | 18 | 14.8 | 0.8 | 3% | 23x | lazy 9, casual 6, sexy 2 |
| `here too` | 18 | 14.8 | 0.0 | 3% | 23x | casual 17, sexy 1 |
| `are just` | 18 | 14.8 | 1.6 | 3% | 23x | lazy 14, angry 3, casual 1 |
| `the weekend` | 19 | 15.6 | 32.1 | 3% | 21x | casual 14, lazy 4, sexy 1 |
| `have been` | 20 | 16.4 | 36.2 | 3% | 20x | casual 12, lazy 4, sexy 2 |
| `to you` | 23 | 18.9 | 0.8 | 3% | 18x | angry 9, sexy 7, formal 4 |
| `is the` | 510 | 419.2 | 77.3 | 7% | 2x | casual 292, lazy 116, angry 50 |
| `needs a` | 36 | 29.6 | 36.2 | 3% | 11x | casual 11, formal 9, angry 6 |
| `to the` | 195 | 160.3 | 169.3 | 5% | 3x | casual 70, sexy 34, formal 32 |
| `the morning` | 41 | 33.7 | 25.5 | 3% | 10x | casual 18, lazy 11, angry 5 |
| `did you get` | 41 | 33.7 | 33.7 | 3% | 10x | casual 37, angry 2, lazy 2 |
| `more than` | 51 | 41.9 | 33.7 | 3% | 8x | casual 18, lazy 11, sexy 11 |
| `and it` | 51 | 41.9 | 69.0 | 3% | 8x | casual 40, lazy 5, formal 4 |
| `the car` | 53 | 43.6 | 40.3 | 3% | 8x | casual 26, sexy 14, lazy 9 |
| `this time` | 56 | 46.0 | 15.6 | 3% | 7x | casual 43, angry 6, sexy 3 |
| `a good` | 67 | 55.1 | 11.5 | 3% | 6x | casual 50, lazy 12, sexy 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 17.0 | casual 8, angry 2 |
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
| `counts as a` | 3 | 12 | 12.2 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `the office manager` | 3 | 9 | 12.1 | formal 9 |
| `sounds like a` | 3 | 15 | 12.0 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.8 | casual 15 |
| `the front desk` | 3 | 14 | 11.7 | angry 8, lazy 4, casual 1 |
| `without a single` | 3 | 10 | 11.7 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.3 | casual 9, angry 3, formal 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `get to` | 4 | casual 5, angry 4, formal 2, sexy 2 |
| `this week` | 5 | casual 22, formal 5, angry 4, lazy 4 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 9 |
| `i have` | 3 | casual 34, lazy 12, sexy 4 |
| `i've got` | 1 | casual 8 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `my mom` | 1 | casual 14 |
| `and i'm` | 2 | casual 13, sexy 1 |
| `you actually` | 3 | casual 11, lazy 5, angry 2 |
| `than you` | 4 | lazy 9, casual 6, sexy 2, angry 1 |
| `here too` | 2 | casual 17, sexy 1 |
| `are just` | 3 | lazy 14, angry 3, casual 1 |
| `the weekend` | 3 | casual 14, lazy 4, sexy 1 |
| `have been` | 5 | casual 12, lazy 4, sexy 2, angry 1 |
| `to you` | 5 | angry 9, sexy 7, formal 4, casual 2 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 36 |
| `needs a` | 5 | casual 11, formal 9, angry 6, sexy 6 |
| `to the` | 5 | casual 70, sexy 34, formal 32, lazy 32 |
| `the morning` | 5 | casual 18, lazy 11, angry 5, formal 5 |
| `did you get` | 3 | casual 37, angry 2, lazy 2 |
| `more than` | 5 | casual 18, lazy 11, sexy 11, formal 8 |
| `and it` | 4 | casual 40, lazy 5, formal 4, sexy 2 |
| `the car` | 5 | casual 26, sexy 14, lazy 9, formal 3 |
| `this time` | 5 | casual 43, angry 6, sexy 3, formal 2 |
| `a good` | 4 | casual 50, lazy 12, sexy 3, formal 2 |

## 4. Opener maps

- assistant pos 0 (n=12166): a 9.9%, the 8.2%, does 2.7%, how 2.2%, did 2.2%, why 1.8%
- assistant pos 1 (n=12166): the 11.2%, a 2.1%, is 1.7%, does 1.6%, you 1.5%, on 0.9%
- assistant pos 2 (n=12165): the 7.3%, a 2.9%, is 2.5%, on 1.9%, of 1.8%, for 1.8%
- assistant pos last (n=12166): it 3.9%, now 1.4%, you 1.2%, time 1.1%, one 1.0%, again 0.9%
- user pos 0 (n=12166): the 15.0%, my 9.4%, our 9.2%, i 6.5%, we 5.7%, you 4.9%
- user pos 1 (n=12103): the 3.4%, you 1.9%, a 1.5%, is 1.2%, got 0.9%, was 0.9%
- user pos 2 (n=12013): the 8.3%, a 3.8%, is 1.6%, my 1.3%, in 1.2%, you 1.2%
- user pos last (n=12166): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.0%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

