# synth2 token-attractor map

Generated 2026-10-16 09:13  |  corpus 5242 rows, **7376 assistant turns**, 7376 user turns
Probe: `probe_out37_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T07:20:00

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.0% | -0.1 |
| `the`-opener (user) | 12.7% | 12.8% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `or just` | - | 7% | - | 11x |
| `in the` | - | 10% | - | 3x |
| `the end` | - | 5% | - | 9x |
| `time for` | - | 3% | - | 31x |
| `is long` | - | 3% | - | 31x |
| `and i am` | - | 3% | - | 31x |
| `an hour` | - | 5% | - | 7x |
| `is the` | 8% | 8% | 2x | 2x |
| `worth it` | 5% | 5% | 6x | 6x |
| `no idea` | - | 3% | - | 20x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 12.8% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 46 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `or just` | 45 | 61.0 | 4.1 | 7% | 11x | casual 36, angry 9 |
| `in the` | 285 | 386.4 | 349.8 | 10% | 3x | casual 171, lazy 68, angry 46 |
| `the end` | 40 | 54.2 | 35.2 | 5% | 9x | casual 26, angry 7, lazy 7 |
| `time for` | 8 | 10.8 | 2.7 | 3% | 31x | casual 6, lazy 2 |
| `is long` | 8 | 10.8 | 1.4 | 3% | 31x | casual 6, lazy 2 |
| `and i am` | 8 | 10.8 | 6.8 | 3% | 31x | casual 7, lazy 1 |
| `an hour` | 55 | 74.6 | 71.9 | 5% | 7x | casual 34, lazy 16, angry 5 |
| `is the` | 403 | 546.4 | 93.5 | 8% | 2x | casual 251, lazy 116, angry 36 |
| `worth it` | 58 | 78.6 | 12.2 | 5% | 6x | casual 42, lazy 15, angry 1 |
| `no idea` | 12 | 16.3 | 10.8 | 3% | 20x | casual 10, lazy 2 |
| `is your` | 12 | 16.3 | 17.6 | 3% | 20x | casual 10, angry 2 |
| `early night` | 12 | 16.3 | 4.1 | 3% | 20x | casual 11, lazy 1 |
| `a good` | 85 | 115.2 | 14.9 | 5% | 4x | casual 69, lazy 16 |
| `night is` | 17 | 23.0 | 2.7 | 3% | 14x | casual 9, angry 4, lazy 4 |
| `the weekend` | 19 | 25.8 | 51.5 | 3% | 13x | casual 15, lazy 4 |
| `is it` | 106 | 143.7 | 29.8 | 5% | 3x | casual 100, angry 6 |
| `it is` | 116 | 157.3 | 69.1 | 5% | 3x | casual 79, lazy 36, angry 1 |
| `got a` | 24 | 32.5 | 105.7 | 3% | 10x | casual 21, angry 2, lazy 1 |
| `is a` | 404 | 547.7 | 73.2 | 7% | 1x | casual 147, angry 141, lazy 116 |
| `the whole` | 158 | 214.2 | 128.8 | 5% | 2x | lazy 83, casual 55, angry 20 |
| `the last` | 34 | 46.1 | 35.2 | 3% | 7x | casual 21, lazy 10, angry 3 |
| `it the` | 39 | 52.9 | 14.9 | 3% | 6x | casual 34, lazy 4, angry 1 |
| `the day` | 40 | 54.2 | 20.3 | 3% | 6x | lazy 22, casual 16, angry 2 |
| `did you get` | 44 | 59.7 | 56.9 | 3% | 6x | casual 40, angry 2, lazy 2 |
| `i have` | 47 | 63.7 | 89.5 | 3% | 5x | casual 35, lazy 12 |

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
| `have you tried` | 3 | 22 | 13.8 | casual 15, angry 7 |
| `the front desk` | 3 | 12 | 13.3 | angry 7, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `did they say` | 3 | 8 | 12.8 | angry 4, casual 4 |
| `i have been` | 3 | 11 | 12.4 | casual 9, lazy 2 |
| `two hours of` | 3 | 9 | 12.4 | lazy 4, angry 3, casual 2 |
| `you able to` | 3 | 8 | 12.3 | angry 8 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `for an hour` | 3 | 10 | 12.0 | casual 8, angry 1, lazy 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `how long did` | 3 | 12 | 11.4 | casual 9, angry 3 |
| `feel like a` | 3 | 9 | 11.4 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 44 | 10.9 | casual 40, angry 2, lazy 2 |
| `has it been` | 3 | 8 | 10.9 | casual 8 |
| `and i am` | 3 | 8 | 10.7 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |
| `a lot of` | 3 | 10 | 10.1 | casual 7, lazy 3 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `or just` | 2 | casual 36, angry 9 |
| `in the` | 3 | casual 171, lazy 68, angry 46 |
| `the end` | 3 | casual 26, angry 7, lazy 7 |
| `time for` | 2 | casual 6, lazy 2 |
| `is long` | 2 | casual 6, lazy 2 |
| `and i am` | 2 | casual 7, lazy 1 |
| `an hour` | 3 | casual 34, lazy 16, angry 5 |
| `is the` | 3 | casual 251, lazy 116, angry 36 |
| `worth it` | 3 | casual 42, lazy 15, angry 1 |
| `no idea` | 2 | casual 10, lazy 2 |
| `is your` | 2 | casual 10, angry 2 |
| `early night` | 2 | casual 11, lazy 1 |
| `a good` | 2 | casual 69, lazy 16 |
| `night is` | 3 | casual 9, angry 4, lazy 4 |
| `the weekend` | 2 | casual 15, lazy 4 |
| `is it` | 2 | casual 100, angry 6 |
| `it is` | 3 | casual 79, lazy 36, angry 1 |
| `got a` | 3 | casual 21, angry 2, lazy 1 |
| `is a` | 3 | casual 147, angry 141, lazy 116 |
| `the whole` | 3 | lazy 83, casual 55, angry 20 |
| `the last` | 3 | casual 21, lazy 10, angry 3 |
| `it the` | 3 | casual 34, lazy 4, angry 1 |
| `the day` | 3 | lazy 22, casual 16, angry 2 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `i have` | 2 | casual 35, lazy 12 |

## 4. Opener maps

- assistant pos 0 (n=7376): a 7.8%, the 3.0%, did 2.6%, that 2.2%, was 2.2%, haha 1.8%
- assistant pos 1 (n=7376): the 12.2%, a 2.3%, you 2.2%, is 2.1%, it 1.1%, and 0.9%
- assistant pos 2 (n=7375): the 5.9%, is 3.5%, a 2.7%, are 2.3%, of 1.7%, for 1.3%
- assistant pos last (n=7376): it 4.5%, now 1.5%, time 1.4%, one 1.0%, again 0.9%, you 0.9%
- user pos 0 (n=7376): the 12.8%, my 10.4%, our 8.3%, i 6.8%, did 3.5%, a 3.0%
- user pos 1 (n=7313): the 4.3%, you 3.1%, a 2.5%, was 1.4%, did 1.3%, is 1.2%
- user pos 2 (n=7224): the 6.7%, a 2.9%, is 2.2%, you 1.7%, and 1.5%, got 1.3%
- user pos last (n=7376): again 2.8%, it 1.8%, now 1.6%, week 1.5%, today 1.4%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.0%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

