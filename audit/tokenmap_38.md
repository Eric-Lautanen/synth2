# synth2 token-attractor map

Generated 2026-10-16 10:45  |  corpus 5366 rows, **7510 assistant turns**, 7510 user turns
Probe: `probe_out38_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T09:13:15

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 2.9% | -0.0 |
| `the`-opener (user) | 12.8% | 12.9% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | - | 8% | - | 15x |
| `here too` | - | 5% | - | 22x |
| `every time` | - | 5% | - | 15x |
| `is it` | 5% | 7% | 3x | 5x |
| `the morning` | - | 5% | - | 12x |
| `it is` | 5% | 7% | 3x | 4x |
| `i have` | 3% | 5% | 5x | 8x |
| `same here` | - | 3% | - | 28x |
| `is there a` | - | 3% | - | 28x |
| `is a` | 7% | 8% | 1x | 1x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.9% | < 12% |
| `the`-opener (user) | 12.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
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
| `a bit` | 41 | 54.6 | 42.6 | 8% | 15x | casual 39, angry 1, lazy 1 |
| `here too` | 17 | 22.6 | 0.0 | 5% | 22x | casual 17 |
| `every time` | 25 | 33.3 | 25.3 | 5% | 15x | casual 15, lazy 7, angry 3 |
| `is it` | 106 | 141.1 | 29.3 | 7% | 5x | casual 100, angry 6 |
| `the morning` | 32 | 42.6 | 25.3 | 5% | 12x | casual 17, lazy 11, angry 4 |
| `it is` | 118 | 157.1 | 69.2 | 7% | 4x | casual 79, lazy 36, angry 3 |
| `i have` | 47 | 62.6 | 87.9 | 5% | 8x | casual 35, lazy 12 |
| `same here` | 9 | 12.0 | 5.3 | 3% | 28x | casual 9 |
| `is there a` | 9 | 12.0 | 0.0 | 3% | 28x | casual 6, angry 2, lazy 1 |
| `is a` | 420 | 559.3 | 73.2 | 8% | 1x | angry 157, casual 147, lazy 116 |
| `a good` | 85 | 113.2 | 14.6 | 5% | 4x | casual 69, lazy 16 |
| `the same` | 90 | 119.8 | 90.5 | 5% | 4x | casual 36, lazy 29, angry 25 |
| `bit of` | 17 | 22.6 | 12.0 | 3% | 15x | casual 17 |
| `two hours` | 19 | 25.3 | 30.6 | 3% | 13x | angry 7, casual 7, lazy 5 |
| `to be` | 23 | 30.6 | 20.0 | 3% | 11x | casual 13, lazy 8, angry 2 |
| `worth the` | 34 | 45.3 | 10.7 | 3% | 7x | casual 21, lazy 13 |
| `the only` | 34 | 45.3 | 9.3 | 3% | 7x | casual 15, lazy 14, angry 5 |
| `it the` | 39 | 51.9 | 14.6 | 3% | 6x | casual 34, lazy 4, angry 1 |
| `the car` | 41 | 54.6 | 46.6 | 3% | 6x | casual 31, lazy 9, angry 1 |
| `a whole` | 42 | 55.9 | 26.6 | 3% | 6x | lazy 16, angry 15, casual 11 |
| `for the` | 211 | 281.0 | 262.3 | 5% | 2x | casual 135, angry 51, lazy 25 |
| `i am` | 56 | 74.6 | 45.3 | 3% | 4x | casual 44, lazy 11, angry 1 |
| `a week` | 66 | 87.9 | 65.2 | 3% | 4x | casual 37, lazy 22, angry 7 |
| `do you` | 88 | 117.2 | 69.2 | 3% | 3x | casual 74, angry 13, lazy 1 |
| `that is` | 114 | 151.8 | 13.3 | 3% | 2x | casual 80, lazy 26, angry 8 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `were you able to` | 4 | 8 | 22.6 | angry 8 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `were you able` | 3 | 8 | 15.7 | angry 8 |
| `an early night` | 3 | 11 | 14.4 | casual 10, lazy 1 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 22 | 13.9 | casual 15, angry 7 |
| `the front desk` | 3 | 12 | 13.3 | angry 7, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `did they say` | 3 | 8 | 12.8 | angry 4, casual 4 |
| `i have been` | 3 | 11 | 12.5 | casual 9, lazy 2 |
| `two hours of` | 3 | 9 | 12.4 | lazy 4, angry 3, casual 2 |
| `you able to` | 3 | 8 | 12.3 | angry 8 |
| `fell asleep` | 2 | 8 | 12.2 | casual 4, lazy 4 |
| `a phone call` | 3 | 8 | 12.0 | casual 5, lazy 2, angry 1 |
| `for an hour` | 3 | 10 | 11.9 | casual 8, angry 1, lazy 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `feel like a` | 3 | 9 | 11.4 | lazy 6, casual 3 |
| `how long did` | 3 | 12 | 11.4 | casual 9, angry 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `has it been` | 3 | 8 | 10.9 | casual 8 |
| `and i am` | 3 | 8 | 10.7 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.4 | casual 15, angry 2 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 3 | casual 39, angry 1, lazy 1 |
| `here too` | 1 | casual 17 |
| `every time` | 3 | casual 15, lazy 7, angry 3 |
| `is it` | 2 | casual 100, angry 6 |
| `the morning` | 3 | casual 17, lazy 11, angry 4 |
| `it is` | 3 | casual 79, lazy 36, angry 3 |
| `i have` | 2 | casual 35, lazy 12 |
| `same here` | 1 | casual 9 |
| `is there a` | 3 | casual 6, angry 2, lazy 1 |
| `is a` | 3 | angry 157, casual 147, lazy 116 |
| `a good` | 2 | casual 69, lazy 16 |
| `the same` | 3 | casual 36, lazy 29, angry 25 |
| `bit of` | 1 | casual 17 |
| `two hours` | 3 | angry 7, casual 7, lazy 5 |
| `to be` | 3 | casual 13, lazy 8, angry 2 |
| `worth the` | 2 | casual 21, lazy 13 |
| `the only` | 3 | casual 15, lazy 14, angry 5 |
| `it the` | 3 | casual 34, lazy 4, angry 1 |
| `the car` | 3 | casual 31, lazy 9, angry 1 |
| `a whole` | 3 | lazy 16, angry 15, casual 11 |
| `for the` | 3 | casual 135, angry 51, lazy 25 |
| `i am` | 3 | casual 44, lazy 11, angry 1 |
| `a week` | 3 | casual 37, lazy 22, angry 7 |
| `do you` | 3 | casual 74, angry 13, lazy 1 |
| `that is` | 3 | casual 80, lazy 26, angry 8 |

## 4. Opener maps

- assistant pos 0 (n=7510): a 7.9%, the 2.9%, did 2.5%, that 2.2%, was 2.1%, how 1.9%
- assistant pos 1 (n=7510): the 12.1%, a 2.3%, you 2.2%, is 2.1%, it 1.1%, does 0.9%
- assistant pos 2 (n=7509): the 5.9%, is 3.4%, a 3.0%, are 2.3%, of 1.7%, for 1.3%
- assistant pos last (n=7510): it 4.4%, now 1.4%, time 1.4%, one 1.0%, you 0.9%, again 0.9%
- user pos 0 (n=7510): the 12.9%, my 10.6%, our 8.3%, i 6.7%, did 3.4%, a 2.9%
- user pos 1 (n=7447): the 4.2%, you 3.0%, a 2.4%, was 1.4%, did 1.3%, is 1.2%
- user pos 2 (n=7358): the 6.6%, a 2.9%, is 2.2%, you 1.7%, and 1.5%, got 1.3%
- user pos last (n=7510): again 2.7%, it 1.8%, now 1.6%, week 1.5%, today 1.3%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.8%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

