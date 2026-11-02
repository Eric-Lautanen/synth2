# synth2 token-attractor map

Generated 2026-10-16 15:45  |  corpus 5614 rows, **7778 assistant turns**, 7778 user turns
Probe: `probe_out41_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T14:00:52

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.9% | 3.0% | +0.1 |
| `the`-opener (user) | 13.0% | 12.8% | -0.2 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a real` | - | 12% | - | 9x |
| `did you` | - | 8% | - | 3x |
| `how did` | - | 5% | - | 10x |
| `the car` | - | 5% | - | 9x |
| `i have` | 5% | 5% | 8x | 8x |
| `how you` | - | 3% | - | 32x |
| `you get` | - | 5% | - | 7x |
| `the apartment` | - | 3% | - | 29x |
| `not much` | - | 3% | - | 29x |
| `at least` | - | 5% | - | 6x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 12.8% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
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
| `a real` | 105 | 135.0 | 56.6 | 12% | 9x | casual 82, angry 13, lazy 10 |
| `did you` | 222 | 285.4 | 316.3 | 8% | 3x | casual 192, angry 25, lazy 5 |
| `how did` | 38 | 48.9 | 11.6 | 5% | 10x | casual 31, angry 7 |
| `the car` | 41 | 52.7 | 45.0 | 5% | 9x | casual 31, lazy 9, angry 1 |
| `i have` | 47 | 60.4 | 86.1 | 5% | 8x | casual 35, lazy 12 |
| `how you` | 8 | 10.3 | 1.3 | 3% | 32x | casual 5, lazy 3 |
| `you get` | 58 | 74.6 | 65.6 | 5% | 7x | casual 49, lazy 5, angry 4 |
| `the apartment` | 9 | 11.6 | 14.1 | 3% | 29x | casual 8, lazy 1 |
| `not much` | 9 | 11.6 | 3.9 | 3% | 29x | casual 7, angry 1, lazy 1 |
| `at least` | 62 | 79.7 | 16.7 | 5% | 6x | casual 33, angry 20, lazy 9 |
| `the plan` | 11 | 14.1 | 23.1 | 3% | 24x | casual 5, angry 4, lazy 2 |
| `of those` | 11 | 14.1 | 6.4 | 3% | 24x | casual 7, angry 2, lazy 2 |
| `no idea` | 12 | 15.4 | 10.3 | 3% | 22x | casual 10, lazy 2 |
| `a slow` | 13 | 16.7 | 10.3 | 3% | 20x | casual 7, lazy 4, angry 2 |
| `every morning` | 14 | 18.0 | 11.6 | 3% | 19x | casual 6, lazy 5, angry 3 |
| `of them` | 16 | 20.6 | 21.9 | 3% | 16x | casual 11, lazy 4, angry 1 |
| `here too` | 17 | 21.9 | 0.0 | 3% | 15x | casual 17 |
| `have been` | 18 | 23.1 | 37.3 | 3% | 14x | casual 13, lazy 4, angry 1 |
| `is it` | 106 | 136.3 | 28.3 | 5% | 4x | casual 100, angry 6 |
| `a phone` | 21 | 27.0 | 12.9 | 3% | 12x | angry 10, casual 6, lazy 5 |
| `is always` | 24 | 30.9 | 12.9 | 3% | 11x | casual 16, lazy 7, angry 1 |
| `at last` | 24 | 30.9 | 37.3 | 3% | 11x | casual 24 |
| `but the` | 26 | 33.4 | 60.4 | 3% | 10x | casual 21, lazy 4, angry 1 |
| `you have` | 27 | 34.7 | 16.7 | 3% | 10x | casual 20, lazy 5, angry 2 |
| `just the` | 28 | 36.0 | 12.9 | 3% | 9x | casual 19, lazy 6, angry 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `were you able to` | 4 | 8 | 22.5 | angry 8 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `were you able` | 3 | 8 | 15.7 | angry 8 |
| `an early night` | 3 | 11 | 14.4 | casual 10, lazy 1 |
| `have you tried` | 3 | 22 | 13.9 | casual 15, angry 7 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `the front desk` | 3 | 12 | 13.3 | angry 7, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.8 | casual 7, lazy 1 |
| `did they say` | 3 | 8 | 12.7 | angry 4, casual 4 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `you able to` | 3 | 8 | 12.3 | angry 8 |
| `fell asleep` | 2 | 8 | 12.2 | casual 4, lazy 4 |
| `two hours of` | 3 | 9 | 12.2 | lazy 4, angry 3, casual 2 |
| `an hour of` | 3 | 8 | 11.8 | angry 4, casual 2, lazy 2 |
| `for an hour` | 3 | 10 | 11.8 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.7 | casual 5, lazy 2, angry 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `feel like a` | 3 | 9 | 11.4 | lazy 6, casual 3 |
| `how long did` | 3 | 12 | 11.3 | casual 9, angry 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `did you get` | 3 | 44 | 10.9 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.8 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.4 | casual 15, angry 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a real` | 3 | casual 82, angry 13, lazy 10 |
| `did you` | 3 | casual 192, angry 25, lazy 5 |
| `how did` | 2 | casual 31, angry 7 |
| `the car` | 3 | casual 31, lazy 9, angry 1 |
| `i have` | 2 | casual 35, lazy 12 |
| `how you` | 2 | casual 5, lazy 3 |
| `you get` | 3 | casual 49, lazy 5, angry 4 |
| `the apartment` | 2 | casual 8, lazy 1 |
| `not much` | 3 | casual 7, angry 1, lazy 1 |
| `at least` | 3 | casual 33, angry 20, lazy 9 |
| `the plan` | 3 | casual 5, angry 4, lazy 2 |
| `of those` | 3 | casual 7, angry 2, lazy 2 |
| `no idea` | 2 | casual 10, lazy 2 |
| `a slow` | 3 | casual 7, lazy 4, angry 2 |
| `every morning` | 3 | casual 6, lazy 5, angry 3 |
| `of them` | 3 | casual 11, lazy 4, angry 1 |
| `here too` | 1 | casual 17 |
| `have been` | 3 | casual 13, lazy 4, angry 1 |
| `is it` | 2 | casual 100, angry 6 |
| `a phone` | 3 | angry 10, casual 6, lazy 5 |
| `is always` | 3 | casual 16, lazy 7, angry 1 |
| `at last` | 1 | casual 24 |
| `but the` | 3 | casual 21, lazy 4, angry 1 |
| `you have` | 3 | casual 20, lazy 5, angry 2 |
| `just the` | 3 | casual 19, lazy 6, angry 3 |

## 4. Opener maps

- assistant pos 0 (n=7778): a 8.2%, the 3.0%, did 2.4%, how 2.2%, that 2.1%, was 2.1%
- assistant pos 1 (n=7778): the 11.7%, a 2.3%, you 2.1%, is 2.1%, does 1.3%, it 1.1%
- assistant pos 2 (n=7777): the 6.0%, is 3.3%, a 3.1%, are 2.2%, of 1.7%, for 1.6%
- assistant pos last (n=7778): it 4.4%, now 1.4%, time 1.3%, one 1.0%, you 1.0%, again 0.9%
- user pos 0 (n=7778): the 12.8%, my 10.7%, our 8.2%, i 6.6%, did 3.3%, a 2.8%
- user pos 1 (n=7715): the 4.1%, you 2.9%, a 2.4%, was 1.3%, did 1.3%, is 1.2%
- user pos 2 (n=7626): the 6.7%, a 2.9%, is 2.1%, you 1.7%, and 1.5%, got 1.3%
- user pos last (n=7778): again 2.6%, it 1.9%, now 1.6%, week 1.5%, today 1.3%, night 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.6%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| lazy | 1 / 2155 |

