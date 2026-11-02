# synth2 token-attractor map

Generated 2026-10-17 08:40  |  corpus 6002 rows, **8197 assistant turns**, 8197 user turns
Probe: `probe_out44_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-17T06:09:23

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.0% | +0.0 |
| `the`-opener (user) | 13.0% | 13.1% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `it a` | - | 5% | - | 10x |
| `i will` | - | 5% | - | 9x |
| `that too` | - | 3% | - | 34x |
| `i am` | 5% | 5% | 7x | 7x |
| `an hour` | - | 5% | - | 7x |
| `was it` | - | 5% | - | 6x |
| `for three` | - | 3% | - | 18x |
| `how far` | - | 3% | - | 16x |
| `up to` | - | 3% | - | 14x |
| `three days` | - | 3% | - | 13x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 13.1% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 34 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `it a` | 40 | 48.8 | 11.0 | 5% | 10x | casual 34, lazy 4, angry 2 |
| `i will` | 45 | 54.9 | 9.8 | 5% | 9x | casual 31, lazy 14 |
| `that too` | 8 | 9.8 | 0.0 | 3% | 34x | casual 7, lazy 1 |
| `i am` | 56 | 68.3 | 43.9 | 5% | 7x | casual 44, lazy 11, angry 1 |
| `an hour` | 62 | 75.6 | 76.9 | 5% | 7x | casual 34, lazy 16, angry 12 |
| `was it` | 69 | 84.2 | 25.6 | 5% | 6x | casual 65, angry 4 |
| `for three` | 15 | 18.3 | 19.5 | 3% | 18x | angry 7, casual 7, lazy 1 |
| `how far` | 17 | 20.7 | 2.4 | 3% | 16x | casual 14, angry 3 |
| `up to` | 19 | 23.2 | 22.0 | 3% | 14x | casual 18, angry 1 |
| `three days` | 21 | 25.6 | 19.5 | 3% | 13x | angry 9, casual 8, lazy 4 |
| `you are` | 22 | 26.8 | 1.2 | 3% | 12x | casual 12, lazy 8, angry 2 |
| `to be` | 23 | 28.1 | 19.5 | 3% | 12x | casual 13, lazy 8, angry 2 |
| `what did you` | 27 | 32.9 | 39.0 | 3% | 10x | casual 26, lazy 1 |
| `is a real` | 27 | 32.9 | 1.2 | 3% | 10x | casual 16, angry 7, lazy 4 |
| `got the` | 29 | 35.4 | 47.6 | 3% | 9x | casual 27, lazy 2 |
| `the morning` | 35 | 42.7 | 25.6 | 3% | 8x | casual 17, lazy 11, angry 7 |
| `do it` | 35 | 42.7 | 8.5 | 3% | 8x | casual 24, lazy 11 |
| `is just` | 37 | 45.1 | 3.7 | 3% | 7x | lazy 20, angry 11, casual 6 |
| `it the` | 39 | 47.6 | 13.4 | 3% | 7x | casual 34, lazy 4, angry 1 |
| `like a` | 54 | 65.9 | 79.3 | 3% | 5x | casual 31, lazy 18, angry 5 |
| `a good` | 55 | 67.1 | 13.4 | 3% | 5x | casual 43, lazy 12 |
| `worth it` | 58 | 70.8 | 11.0 | 3% | 5x | casual 42, lazy 15, angry 1 |
| `about the` | 60 | 73.2 | 40.3 | 3% | 5x | casual 33, angry 25, lazy 2 |
| `out of` | 63 | 76.9 | 80.5 | 3% | 4x | casual 34, angry 15, lazy 14 |
| `and the` | 65 | 79.3 | 170.8 | 3% | 4x | casual 38, lazy 15, angry 12 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.3 | casual 10, lazy 1 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `feels like a` | 3 | 8 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `fell asleep` | 2 | 8 | 12.2 | casual 4, lazy 4 |
| `an hour of` | 3 | 10 | 12.0 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `a phone call` | 3 | 8 | 11.6 | casual 5, lazy 2, angry 1 |
| `for an hour` | 3 | 10 | 11.6 | casual 8, angry 1, lazy 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `how long did` | 3 | 12 | 11.1 | casual 9, angry 3 |
| `has it been` | 3 | 8 | 11.1 | casual 8 |
| `did you find` | 3 | 9 | 10.9 | casual 9 |
| `and i am` | 3 | 8 | 10.8 | casual 7, lazy 1 |
| `did you get` | 3 | 44 | 10.8 | casual 40, angry 2, lazy 2 |
| `why would a` | 3 | 8 | 10.5 | angry 8 |
| `are you going` | 3 | 17 | 10.4 | casual 15, angry 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `it a` | 3 | casual 34, lazy 4, angry 2 |
| `i will` | 2 | casual 31, lazy 14 |
| `that too` | 2 | casual 7, lazy 1 |
| `i am` | 3 | casual 44, lazy 11, angry 1 |
| `an hour` | 3 | casual 34, lazy 16, angry 12 |
| `was it` | 2 | casual 65, angry 4 |
| `for three` | 3 | angry 7, casual 7, lazy 1 |
| `how far` | 2 | casual 14, angry 3 |
| `up to` | 2 | casual 18, angry 1 |
| `three days` | 3 | angry 9, casual 8, lazy 4 |
| `you are` | 3 | casual 12, lazy 8, angry 2 |
| `to be` | 3 | casual 13, lazy 8, angry 2 |
| `what did you` | 2 | casual 26, lazy 1 |
| `is a real` | 3 | casual 16, angry 7, lazy 4 |
| `got the` | 2 | casual 27, lazy 2 |
| `the morning` | 3 | casual 17, lazy 11, angry 7 |
| `do it` | 2 | casual 24, lazy 11 |
| `is just` | 3 | lazy 20, angry 11, casual 6 |
| `it the` | 3 | casual 34, lazy 4, angry 1 |
| `like a` | 3 | casual 31, lazy 18, angry 5 |
| `a good` | 2 | casual 43, lazy 12 |
| `worth it` | 3 | casual 42, lazy 15, angry 1 |
| `about the` | 3 | casual 33, angry 25, lazy 2 |
| `out of` | 3 | casual 34, angry 15, lazy 14 |
| `and the` | 3 | casual 38, lazy 15, angry 12 |

## 4. Opener maps

- assistant pos 0 (n=8197): a 7.9%, the 3.0%, did 2.7%, how 2.5%, was 2.1%, that 2.0%
- assistant pos 1 (n=8197): the 11.8%, a 2.4%, is 2.1%, you 2.0%, does 1.4%, it 1.0%
- assistant pos 2 (n=8196): the 6.2%, a 3.2%, is 3.1%, are 2.1%, of 1.7%, for 1.7%
- assistant pos last (n=8197): it 4.2%, now 1.4%, time 1.3%, you 1.1%, one 1.0%, again 0.9%
- user pos 0 (n=8197): the 13.1%, my 10.8%, our 8.3%, i 6.5%, they 3.4%, did 3.2%
- user pos 1 (n=8134): the 3.9%, you 2.8%, a 2.2%, was 1.3%, did 1.2%, is 1.1%
- user pos 2 (n=8045): the 6.7%, a 2.9%, is 2.1%, you 1.6%, and 1.4%, my 1.3%
- user pos last (n=8197): again 2.6%, it 1.9%, now 1.5%, week 1.5%, night 1.3%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.3%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| lazy | 1 / 2155 |

