# synth2 token-attractor map

Generated 2026-10-24 21:17  |  corpus 9226 rows, **11681 assistant turns**, 11681 user turns
Probe: `probe_out93_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-24T14:33:22

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.0% | 6.0% | +0.1 |
| `the`-opener (user) | 14.7% | 14.8% | +0.1 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `this time` | - | 7% | - | 14x |
| `you got` | - | 5% | - | 29x |
| `a week` | - | 7% | - | 9x |
| `week and` | - | 3% | - | 49x |
| `much better` | - | 3% | - | 43x |
| `four days` | - | 3% | - | 32x |
| `the hour` | - | 3% | - | 30x |
| `are worth` | 3% | 3% | 30x | 30x |
| `in this` | - | 3% | - | 28x |
| `than a` | - | 3% | - | 24x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.0% | < 12% |
| `the`-opener (user) | 14.8% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 32 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `this time` | 56 | 47.9 | 15.4 | 7% | 14x | casual 43, angry 6, sexy 3 |
| `you got` | 20 | 17.1 | 12.8 | 5% | 29x | casual 19, angry 1 |
| `a week` | 86 | 73.6 | 57.4 | 7% | 9x | casual 35, lazy 22, formal 17 |
| `week and` | 8 | 6.8 | 13.7 | 3% | 49x | casual 7, formal 1 |
| `much better` | 9 | 7.7 | 0.9 | 3% | 43x | casual 7, formal 1, lazy 1 |
| `four days` | 12 | 10.3 | 10.3 | 3% | 32x | casual 4, angry 3, lazy 3 |
| `the hour` | 13 | 11.1 | 6.0 | 3% | 30x | sexy 5, casual 4, formal 2 |
| `are worth` | 13 | 11.1 | 0.0 | 3% | 30x | lazy 6, casual 3, sexy 3 |
| `in this` | 14 | 12.0 | 11.1 | 3% | 28x | angry 4, lazy 4, casual 3 |
| `than a` | 16 | 13.7 | 7.7 | 3% | 24x | casual 8, formal 5, lazy 3 |
| `too much` | 22 | 18.8 | 6.8 | 3% | 18x | casual 9, lazy 9, sexy 2 |
| `got a` | 23 | 19.7 | 77.9 | 3% | 17x | casual 17, sexy 3, angry 2 |
| `faster than` | 24 | 20.5 | 8.6 | 3% | 16x | lazy 12, formal 6, sexy 3 |
| `going to` | 32 | 27.4 | 12.0 | 3% | 12x | casual 18, angry 6, lazy 5 |
| `is the` | 509 | 435.8 | 79.6 | 7% | 2x | casual 292, lazy 116, angry 50 |
| `a long` | 34 | 29.1 | 7.7 | 3% | 11x | casual 21, lazy 8, angry 3 |
| `a day` | 41 | 35.1 | 23.1 | 3% | 9x | casual 21, lazy 11, angry 5 |
| `not a` | 42 | 36.0 | 8.6 | 3% | 9x | angry 21, casual 12, lazy 7 |
| `it was` | 42 | 36.0 | 55.6 | 3% | 9x | casual 26, sexy 7, lazy 5 |
| `the rest` | 45 | 38.5 | 15.4 | 3% | 9x | lazy 16, casual 15, sexy 7 |
| `or is` | 50 | 42.8 | 4.3 | 3% | 8x | formal 28, casual 17, angry 5 |
| `i will` | 55 | 47.1 | 7.7 | 3% | 7x | casual 31, lazy 14, sexy 10 |
| `the real` | 63 | 53.9 | 10.3 | 3% | 6x | lazy 23, casual 22, sexy 12 |
| `means the` | 64 | 54.8 | 1.7 | 3% | 6x | lazy 36, angry 10, formal 10 |
| `the one` | 68 | 58.2 | 22.3 | 3% | 6x | lazy 34, casual 23, angry 6 |

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
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.0 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 15 | 11.9 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `in front of` | 3 | 8 | 11.1 | sexy 6, angry 1, formal 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `this time` | 5 | casual 43, angry 6, sexy 3, formal 2 |
| `you got` | 2 | casual 19, angry 1 |
| `a week` | 5 | casual 35, lazy 22, formal 17, angry 10 |
| `week and` | 2 | casual 7, formal 1 |
| `much better` | 3 | casual 7, formal 1, lazy 1 |
| `four days` | 4 | casual 4, angry 3, lazy 3, formal 2 |
| `the hour` | 5 | sexy 5, casual 4, formal 2, angry 1 |
| `are worth` | 4 | lazy 6, casual 3, sexy 3, formal 1 |
| `in this` | 5 | angry 4, lazy 4, casual 3, sexy 2 |
| `than a` | 3 | casual 8, formal 5, lazy 3 |
| `too much` | 5 | casual 9, lazy 9, sexy 2, angry 1 |
| `got a` | 4 | casual 17, sexy 3, angry 2, lazy 1 |
| `faster than` | 5 | lazy 12, formal 6, sexy 3, angry 2 |
| `going to` | 5 | casual 18, angry 6, lazy 5, sexy 2 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 35 |
| `a long` | 4 | casual 21, lazy 8, angry 3, formal 2 |
| `a day` | 4 | casual 21, lazy 11, angry 5, formal 4 |
| `not a` | 5 | angry 21, casual 12, lazy 7, formal 1 |
| `it was` | 5 | casual 26, sexy 7, lazy 5, angry 2 |
| `the rest` | 5 | lazy 16, casual 15, sexy 7, formal 4 |
| `or is` | 3 | formal 28, casual 17, angry 5 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `the real` | 5 | lazy 23, casual 22, sexy 12, angry 3 |
| `means the` | 5 | lazy 36, angry 10, formal 10, casual 7 |
| `the one` | 5 | lazy 34, casual 23, angry 6, formal 3 |

## 4. Opener maps

- assistant pos 0 (n=11681): a 10.2%, the 6.0%, does 2.5%, how 2.3%, did 2.2%, why 1.9%
- assistant pos 1 (n=11681): the 11.2%, a 2.1%, is 1.8%, does 1.7%, you 1.6%, on 0.9%
- assistant pos 2 (n=11680): the 7.4%, a 3.0%, is 2.6%, on 1.9%, of 1.9%, for 1.8%
- assistant pos last (n=11681): it 4.0%, now 1.5%, time 1.2%, you 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11681): the 14.8%, my 9.5%, our 8.9%, i 6.6%, we 5.9%, you 5.1%
- user pos 1 (n=11618): the 3.1%, you 2.0%, a 1.6%, is 1.1%, got 1.0%, was 1.0%
- user pos 2 (n=11528): the 7.9%, a 3.8%, is 1.7%, my 1.4%, you 1.3%, in 1.2%
- user pos last (n=11681): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.1%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.6%**; model outputs: **1.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

