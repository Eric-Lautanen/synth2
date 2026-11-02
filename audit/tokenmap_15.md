# synth2 token-attractor map

Generated 2026-10-10 22:15  |  corpus 2063 rows, **4070 assistant turns**, 4070 user turns
Probe: `probe_out15_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-10T19:55:07

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 9.1% | 2.1% | -7.0 |
| `the`-opener (user) | 8.0% | 8.0% | +0.0 |
| copula-only | 1.6% | 0.2% | -1.4 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `did the` | - | 12% | - | 4x |
| `in the` | - | 10% | - | 2x |
| `did you` | - | 10% | - | 2x |
| `is it` | - | 8% | - | 3x |
| `the dog` | - | 5% | - | 10x |
| `a good` | 7% | 7% | 4x | 4x |
| `do you` | - | 7% | - | 4x |
| `how did` | - | 5% | - | 7x |
| `it the` | - | 5% | - | 6x |
| `did it` | 5% | 5% | 6x | 6x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.1% | < 12% |
| `the`-opener (user) | 8.0% | n/a |
| copula-only turns | 0.2% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
| probe outputs carrying a top attractor | 42 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `did the` | 125 | 307.1 | 98.3 | 12% | 4x | casual 125 |
| `in the` | 176 | 432.4 | 471.7 | 10% | 2x | casual 171, ghetto 5 |
| `did you` | 197 | 484.0 | 348.9 | 10% | 2x | casual 192, ghetto 5 |
| `is it` | 100 | 245.7 | 41.8 | 8% | 3x | casual 100 |
| `the dog` | 21 | 51.6 | 66.3 | 5% | 10x | casual 21 |
| `a good` | 70 | 172.0 | 22.1 | 7% | 4x | casual 69, ghetto 1 |
| `do you` | 75 | 184.3 | 17.2 | 7% | 4x | casual 74, ghetto 1 |
| `how did` | 31 | 76.2 | 22.1 | 5% | 7x | casual 31 |
| `it the` | 34 | 83.5 | 19.7 | 5% | 6x | casual 34 |
| `did it` | 34 | 83.5 | 17.2 | 5% | 6x | casual 34 |
| `the new` | 35 | 86.0 | 90.9 | 5% | 6x | casual 35 |
| `what did` | 41 | 100.7 | 51.6 | 5% | 5x | casual 41 |
| `my sister` | 8 | 19.7 | 44.2 | 3% | 17x | casual 8 |
| `much did` | 8 | 19.7 | 2.5 | 3% | 17x | casual 8 |
| `up the` | 15 | 36.9 | 24.6 | 3% | 9x | casual 15 |
| `next time` | 15 | 36.9 | 2.5 | 3% | 9x | casual 15 |
| `instead of` | 17 | 41.8 | 24.6 | 3% | 8x | casual 17 |
| `i keep` | 17 | 41.8 | 49.1 | 3% | 8x | casual 17 |
| `a long` | 21 | 51.6 | 14.7 | 3% | 6x | casual 21 |
| `at last` | 24 | 59.0 | 71.3 | 3% | 6x | casual 24 |
| `well the` | 25 | 61.4 | 0.0 | 3% | 5x | casual 25 |
| `from the` | 27 | 66.3 | 100.7 | 3% | 5x | casual 25, ghetto 2 |
| `how much` | 28 | 68.8 | 12.3 | 3% | 5x | casual 25, ghetto 3 |
| `and i` | 29 | 71.3 | 196.6 | 3% | 5x | casual 29 |
| `for the` | 138 | 339.1 | 334.2 | 5% | 1x | casual 135, ghetto 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 8 | 16.5 | casual 8 |
| `an early night` | 3 | 10 | 15.5 | casual 10 |
| `best kind of` | 3 | 10 | 14.2 | casual 8, ghetto 2 |
| `the post office` | 3 | 8 | 13.7 | casual 7, ghetto 1 |
| `have you tried` | 3 | 15 | 13.2 | casual 15 |
| `for an hour` | 3 | 8 | 12.8 | casual 8 |
| `i have been` | 3 | 9 | 11.6 | casual 9 |
| `the best kind` | 3 | 12 | 11.5 | casual 12 |
| `a couple of` | 3 | 11 | 11.5 | casual 11 |
| `how long did` | 3 | 9 | 11.0 | casual 9 |
| `have you got` | 3 | 16 | 11.0 | casual 16 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 40 | 10.9 | casual 40 |
| `has it been` | 3 | 8 | 10.6 | casual 8 |
| `are you going` | 3 | 15 | 10.5 | casual 15 |
| `these days` | 2 | 8 | 10.0 | casual 8 |
| `post office` | 2 | 9 | 9.9 | casual 8, ghetto 1 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `do you go` | 3 | 8 | 9.8 | casual 8 |
| `washing machine` | 2 | 11 | 9.6 | casual 11 |
| `what did you` | 3 | 26 | 9.5 | casual 26 |
| `on a saturday` | 3 | 9 | 9.4 | casual 9 |
| `did you go` | 3 | 13 | 9.4 | casual 13 |
| `was it worth` | 3 | 9 | 9.3 | casual 9 |
| `in the end` | 3 | 14 | 9.0 | casual 14 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `did the` | 1 | casual 125 |
| `in the` | 2 | casual 171, ghetto 5 |
| `did you` | 2 | casual 192, ghetto 5 |
| `is it` | 1 | casual 100 |
| `the dog` | 1 | casual 21 |
| `a good` | 2 | casual 69, ghetto 1 |
| `do you` | 2 | casual 74, ghetto 1 |
| `how did` | 1 | casual 31 |
| `it the` | 1 | casual 34 |
| `did it` | 1 | casual 34 |
| `the new` | 1 | casual 35 |
| `what did` | 1 | casual 41 |
| `my sister` | 1 | casual 8 |
| `much did` | 1 | casual 8 |
| `up the` | 1 | casual 15 |
| `next time` | 1 | casual 15 |
| `instead of` | 1 | casual 17 |
| `i keep` | 1 | casual 17 |
| `a long` | 1 | casual 21 |
| `at last` | 1 | casual 24 |
| `well the` | 1 | casual 25 |
| `from the` | 2 | casual 25, ghetto 2 |
| `how much` | 2 | casual 25, ghetto 3 |
| `and i` | 1 | casual 29 |
| `for the` | 2 | casual 135, ghetto 3 |

## 4. Opener maps

- assistant pos 0 (n=4070): a 7.8%, that 3.6%, haha 3.5%, the 2.1%, i 2.0%, is 1.5%
- assistant pos 1 (n=4070): the 12.0%, a 3.0%, is 2.8%, you 2.3%, it 1.7%, and 1.4%
- assistant pos 2 (n=4068): the 7.4%, is 4.1%, a 2.8%, of 1.9%, for 1.6%, and 1.5%
- assistant pos last (n=4070): it 5.5%, now 1.8%, one 1.6%, time 1.5%, then 1.4%, again 1.3%
- user pos 0 (n=4070): the 8.0%, i 4.0%, my 3.9%, a 3.6%, did 3.5%, how's 2.1%
- user pos 1 (n=4007): the 7.1%, a 4.4%, you 3.1%, did 1.8%, is 1.5%, was 1.4%
- user pos 2 (n=3921): the 6.1%, a 3.9%, and 2.7%, you 1.8%, is 1.7%, one 1.6%
- user pos last (n=4070): it 2.5%, again 2.1%, week 1.8%, now 1.7%, today 1.5%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **12.6%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| ghetto | 75 / 189 |

