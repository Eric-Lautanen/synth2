# synth2 token-attractor map

Generated 2026-10-25 04:51  |  corpus 9400 rows, **11869 assistant turns**, 11869 user turns
Probe: `probe_out95_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T00:47:27

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.1% | 6.3% | +0.2 |
| `the`-opener (user) | 14.8% | 14.8% | +0.0 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the whole` | - | 10% | - | 6x |
| `you want` | - | 5% | - | 42x |
| `on saturday` | - | 5% | - | 37x |
| `to do` | - | 5% | - | 25x |
| `the first` | - | 7% | - | 7x |
| `a long` | - | 5% | - | 17x |
| `is long` | - | 3% | - | 44x |
| `the last` | - | 5% | - | 9x |
| `or the` | - | 5% | - | 8x |
| `want to` | - | 3% | - | 33x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 6.3% | < 12% |
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
| `the whole` | 190 | 160.1 | 110.4 | 10% | 6x | lazy 83, casual 57, angry 32 |
| `you want` | 14 | 11.8 | 10.1 | 5% | 42x | casual 8, lazy 4, angry 1 |
| `on saturday` | 16 | 13.5 | 24.4 | 5% | 37x | casual 14, sexy 2 |
| `to do` | 24 | 20.2 | 19.4 | 5% | 25x | casual 20, angry 2, lazy 1 |
| `the first` | 118 | 99.4 | 82.6 | 7% | 7x | lazy 38, casual 36, sexy 22 |
| `a long` | 34 | 28.6 | 7.6 | 5% | 17x | casual 21, lazy 8, angry 3 |
| `is long` | 9 | 7.6 | 1.7 | 3% | 44x | casual 6, lazy 2, formal 1 |
| `the last` | 69 | 58.1 | 59.0 | 5% | 9x | sexy 28, casual 22, lazy 10 |
| `or the` | 79 | 66.6 | 4.2 | 5% | 8x | casual 51, formal 16, sexy 5 |
| `want to` | 12 | 10.1 | 48.0 | 3% | 33x | casual 7, sexy 4, angry 1 |
| `my mom` | 14 | 11.8 | 14.3 | 3% | 28x | casual 14 |
| `last one` | 15 | 12.6 | 3.4 | 3% | 26x | lazy 8, casual 4, sexy 2 |
| `i know` | 19 | 16.0 | 12.6 | 3% | 21x | casual 15, lazy 2, sexy 2 |
| `a very` | 19 | 16.0 | 5.9 | 3% | 21x | lazy 12, angry 4, casual 1 |
| `so far` | 25 | 21.1 | 9.3 | 3% | 16x | casual 17, lazy 4, angry 2 |
| `you have` | 28 | 23.6 | 12.6 | 3% | 14x | casual 18, lazy 5, angry 2 |
| `but the` | 29 | 24.4 | 49.7 | 3% | 14x | casual 21, lazy 4, sexy 2 |
| `to be` | 30 | 25.3 | 19.4 | 3% | 13x | casual 13, lazy 8, sexy 4 |
| `just the` | 30 | 25.3 | 11.0 | 3% | 13x | casual 19, lazy 6, angry 3 |
| `would a` | 32 | 27.0 | 0.0 | 3% | 12x | formal 20, angry 11, sexy 1 |
| `a quiet` | 33 | 27.8 | 4.2 | 3% | 12x | casual 13, formal 7, lazy 7 |
| `way to` | 36 | 30.3 | 2.5 | 3% | 11x | casual 17, angry 11, lazy 6 |
| `that's the` | 60 | 50.6 | 17.7 | 3% | 7x | casual 60 |
| `means the` | 64 | 53.9 | 1.7 | 3% | 6x | lazy 36, angry 10, formal 10 |
| `are a` | 67 | 56.4 | 7.6 | 3% | 6x | lazy 45, angry 11, casual 8 |

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
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the office manager` | 3 | 8 | 12.5 | formal 8 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `the front desk` | 3 | 14 | 12.1 | angry 8, lazy 4, casual 1 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.0 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 15 | 11.9 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.8 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |
| `you want` | 4 | casual 8, lazy 4, angry 1, sexy 1 |
| `on saturday` | 2 | casual 14, sexy 2 |
| `to do` | 4 | casual 20, angry 2, lazy 1, sexy 1 |
| `the first` | 5 | lazy 38, casual 36, sexy 22, formal 15 |
| `a long` | 4 | casual 21, lazy 8, angry 3, formal 2 |
| `is long` | 3 | casual 6, lazy 2, formal 1 |
| `the last` | 5 | sexy 28, casual 22, lazy 10, angry 5 |
| `or the` | 5 | casual 51, formal 16, sexy 5, angry 4 |
| `want to` | 3 | casual 7, sexy 4, angry 1 |
| `my mom` | 1 | casual 14 |
| `last one` | 4 | lazy 8, casual 4, sexy 2, formal 1 |
| `i know` | 3 | casual 15, lazy 2, sexy 2 |
| `a very` | 5 | lazy 12, angry 4, casual 1, formal 1 |
| `so far` | 5 | casual 17, lazy 4, angry 2, formal 1 |
| `you have` | 5 | casual 18, lazy 5, angry 2, sexy 2 |
| `but the` | 5 | casual 21, lazy 4, sexy 2, angry 1 |
| `to be` | 5 | casual 13, lazy 8, sexy 4, formal 3 |
| `just the` | 4 | casual 19, lazy 6, angry 3, formal 2 |
| `would a` | 3 | formal 20, angry 11, sexy 1 |
| `a quiet` | 4 | casual 13, formal 7, lazy 7, angry 6 |
| `way to` | 4 | casual 17, angry 11, lazy 6, sexy 2 |
| `that's the` | 1 | casual 60 |
| `means the` | 5 | lazy 36, angry 10, formal 10, casual 7 |
| `are a` | 4 | lazy 45, angry 11, casual 8, sexy 3 |

## 4. Opener maps

- assistant pos 0 (n=11869): a 10.1%, the 6.3%, does 2.7%, how 2.3%, did 2.3%, why 1.9%
- assistant pos 1 (n=11869): the 11.3%, a 2.1%, is 1.7%, does 1.6%, you 1.6%, on 0.9%
- assistant pos 2 (n=11868): the 7.4%, a 3.0%, is 2.5%, on 1.9%, of 1.9%, for 1.8%
- assistant pos last (n=11869): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11869): the 14.8%, my 9.5%, our 8.9%, i 6.6%, we 5.9%, you 5.0%
- user pos 1 (n=11806): the 3.3%, you 2.0%, a 1.6%, is 1.2%, got 1.0%, was 1.0%
- user pos 2 (n=11716): the 8.0%, a 3.9%, is 1.6%, my 1.3%, you 1.2%, in 1.2%
- user pos last (n=11869): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.1%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

