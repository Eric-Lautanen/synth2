# synth2 token-attractor map

Generated 2026-10-18 08:38  |  corpus 6622 rows, **8867 assistant turns**, 8867 user turns
Probe: `probe_out52_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T05:45:31

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.6% | 3.7% | +0.0 |
| `the`-opener (user) | 13.7% | 13.7% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `have you` | - | 7% | - | 6x |
| `is long` | - | 3% | - | 37x |
| `the job` | - | 3% | - | 25x |
| `week is` | - | 3% | - | 16x |
| `one is` | - | 3% | - | 16x |
| `just a` | - | 3% | - | 9x |
| `is just` | - | 3% | - | 8x |
| `the last` | - | 3% | - | 7x |
| `how long` | - | 3% | - | 6x |
| `i have` | - | 3% | - | 6x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.7% | < 12% |
| `the`-opener (user) | 13.7% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
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
| `have you` | 107 | 120.7 | 27.1 | 7% | 6x | casual 80, angry 27 |
| `is long` | 8 | 9.0 | 1.1 | 3% | 37x | casual 6, lazy 2 |
| `the job` | 12 | 13.5 | 4.5 | 3% | 25x | casual 6, angry 5, lazy 1 |
| `week is` | 18 | 20.3 | 0.0 | 3% | 16x | casual 10, angry 5, lazy 3 |
| `one is` | 18 | 20.3 | 11.3 | 3% | 16x | casual 13, lazy 4, sexy 1 |
| `just a` | 33 | 37.2 | 22.6 | 3% | 9x | casual 22, angry 7, lazy 4 |
| `is just` | 37 | 41.7 | 3.4 | 3% | 8x | lazy 20, angry 11, casual 6 |
| `the last` | 43 | 48.5 | 39.5 | 3% | 7x | casual 21, lazy 10, sexy 7 |
| `how long` | 47 | 53.0 | 15.8 | 3% | 6x | casual 30, angry 9, sexy 7 |
| `i have` | 51 | 57.5 | 88.0 | 3% | 6x | casual 35, lazy 12, sexy 4 |
| `for the` | 242 | 272.9 | 254.9 | 5% | 2x | casual 135, angry 64, lazy 24 |
| `a good` | 56 | 63.2 | 14.7 | 3% | 5x | casual 43, lazy 12, sexy 1 |
| `i am` | 64 | 72.2 | 40.6 | 3% | 5x | casual 44, lazy 11, sexy 8 |
| `about the` | 65 | 73.3 | 44.0 | 3% | 5x | casual 33, angry 25, sexy 5 |
| `and the` | 66 | 74.4 | 157.9 | 3% | 4x | casual 38, lazy 15, angry 12 |
| `in the` | 327 | 368.8 | 339.5 | 5% | 1x | casual 169, angry 69, lazy 68 |
| `was it` | 74 | 83.5 | 23.7 | 3% | 4x | casual 65, sexy 5, angry 4 |
| `is the` | 418 | 471.4 | 77.8 | 5% | 1x | casual 250, lazy 116, angry 49 |
| `a real` | 105 | 118.4 | 49.6 | 3% | 3x | casual 82, angry 13, lazy 10 |
| `you called` | 8 | 9.0 | 2.3 | 2% | 18x | angry 8 |
| `whole point` | 8 | 9.0 | 1.1 | 2% | 18x | casual 4, lazy 2, angry 1 |
| `what happened` | 8 | 9.0 | 5.6 | 2% | 18x | casual 6, angry 2 |
| `to go` | 8 | 9.0 | 24.8 | 2% | 18x | casual 6, angry 1, lazy 1 |
| `the season` | 8 | 9.0 | 6.8 | 2% | 18x | lazy 4, casual 3, sexy 1 |
| `the lamp` | 8 | 9.0 | 3.4 | 2% | 18x | lazy 5, casual 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.2 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.9 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `fell asleep` | 2 | 8 | 11.6 | casual 4, lazy 4 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `ice cream` | 2 | 8 | 11.6 | lazy 6, casual 1, sexy 1 |
| `for an hour` | 3 | 11 | 11.5 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `a couple of` | 3 | 12 | 11.1 | casual 11, angry 1 |
| `did you find` | 3 | 9 | 10.8 | casual 9 |
| `did you get` | 3 | 44 | 10.7 | casual 40, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `have you` | 2 | casual 80, angry 27 |
| `is long` | 2 | casual 6, lazy 2 |
| `the job` | 3 | casual 6, angry 5, lazy 1 |
| `week is` | 3 | casual 10, angry 5, lazy 3 |
| `one is` | 3 | casual 13, lazy 4, sexy 1 |
| `just a` | 3 | casual 22, angry 7, lazy 4 |
| `is just` | 3 | lazy 20, angry 11, casual 6 |
| `the last` | 4 | casual 21, lazy 10, sexy 7, angry 5 |
| `how long` | 4 | casual 30, angry 9, sexy 7, lazy 1 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `for the` | 4 | casual 135, angry 64, lazy 24, sexy 19 |
| `a good` | 3 | casual 43, lazy 12, sexy 1 |
| `i am` | 4 | casual 44, lazy 11, sexy 8, angry 1 |
| `about the` | 4 | casual 33, angry 25, sexy 5, lazy 2 |
| `and the` | 4 | casual 38, lazy 15, angry 12, sexy 1 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 21 |
| `was it` | 3 | casual 65, sexy 5, angry 4 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 3 |
| `a real` | 3 | casual 82, angry 13, lazy 10 |
| `you called` | 1 | angry 8 |
| `whole point` | 4 | casual 4, lazy 2, angry 1, sexy 1 |
| `what happened` | 2 | casual 6, angry 2 |
| `to go` | 3 | casual 6, angry 1, lazy 1 |
| `the season` | 3 | lazy 4, casual 3, sexy 1 |
| `the lamp` | 2 | lazy 5, casual 3 |

## 4. Opener maps

- assistant pos 0 (n=8867): a 8.0%, the 3.7%, did 2.5%, how 2.3%, was 2.0%, that 1.9%
- assistant pos 1 (n=8867): the 11.7%, a 2.4%, you 2.0%, is 2.0%, does 1.3%, your 1.1%
- assistant pos 2 (n=8866): the 6.2%, a 3.0%, is 2.9%, are 1.9%, of 1.7%, for 1.6%
- assistant pos last (n=8867): it 4.1%, now 1.6%, time 1.3%, you 1.2%, again 1.0%, one 1.0%
- user pos 0 (n=8867): the 13.7%, my 10.4%, our 8.1%, i 6.7%, we 4.1%, they 3.2%
- user pos 1 (n=8804): the 3.7%, you 2.6%, a 2.1%, was 1.2%, did 1.1%, is 1.0%
- user pos 2 (n=8715): the 6.9%, a 3.0%, is 1.9%, you 1.6%, my 1.5%, and 1.3%
- user pos last (n=8867): again 2.5%, it 2.0%, now 1.4%, week 1.4%, night 1.3%, morning 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.0%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 670 |
| lazy | 1 / 2155 |

