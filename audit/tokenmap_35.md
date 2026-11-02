# synth2 token-attractor map

Generated 2026-10-16 05:36  |  corpus 5056 rows, **7175 assistant turns**, 7175 user turns
Probe: `probe_out35_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T04:11:38

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.1% | 3.1% | -0.0 |
| `the`-opener (user) | 12.5% | 12.5% | -0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `too much` | - | 5% | - | 20x |
| `a good` | 8% | 7% | 7x | 6x |
| `is it` | - | 7% | - | 5x |
| `it the` | - | 5% | - | 9x |
| `did you get` | - | 5% | - | 8x |
| `to work` | - | 3% | - | 30x |
| `luck with` | - | 3% | - | 30x |
| `point of` | - | 3% | - | 27x |
| `by the` | - | 5% | - | 6x |
| `whole day` | - | 3% | - | 24x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.1% | < 12% |
| `the`-opener (user) | 12.5% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 39 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `too much` | 18 | 25.1 | 8.4 | 5% | 20x | casual 9, lazy 9 |
| `a good` | 85 | 118.5 | 15.3 | 7% | 6x | casual 69, lazy 16 |
| `is it` | 106 | 147.7 | 30.7 | 7% | 5x | casual 100, angry 6 |
| `it the` | 39 | 54.4 | 15.3 | 5% | 9x | casual 34, lazy 4, angry 1 |
| `did you get` | 44 | 61.3 | 58.5 | 5% | 8x | casual 40, angry 2, lazy 2 |
| `to work` | 8 | 11.1 | 12.5 | 3% | 30x | casual 7, lazy 1 |
| `luck with` | 8 | 11.1 | 4.2 | 3% | 30x | casual 8 |
| `point of` | 9 | 12.5 | 0.0 | 3% | 27x | lazy 5, casual 4 |
| `by the` | 59 | 82.2 | 69.7 | 5% | 6x | casual 31, lazy 21, angry 7 |
| `whole day` | 10 | 13.9 | 5.6 | 3% | 24x | casual 4, lazy 4, angry 2 |
| `was it` | 68 | 94.8 | 29.3 | 5% | 5x | casual 65, angry 3 |
| `good luck` | 12 | 16.7 | 0.0 | 3% | 20x | casual 9, lazy 2, angry 1 |
| `take it` | 13 | 18.1 | 2.8 | 3% | 18x | casual 13 |
| `the first` | 83 | 115.7 | 79.4 | 5% | 4x | casual 40, lazy 38, angry 5 |
| `i was` | 16 | 22.3 | 34.8 | 3% | 15x | casual 14, lazy 2 |
| `in the` | 282 | 393.0 | 349.8 | 7% | 2x | casual 171, lazy 68, angry 43 |
| `oh no` | 18 | 25.1 | 9.8 | 3% | 13x | casual 18 |
| `have been` | 18 | 25.1 | 39.0 | 3% | 13x | casual 13, lazy 4, angry 1 |
| `all week` | 18 | 25.1 | 25.1 | 3% | 13x | casual 13, lazy 3, angry 2 |
| `a real` | 103 | 143.6 | 61.3 | 5% | 3x | casual 82, angry 11, lazy 10 |
| `this morning` | 22 | 30.7 | 93.4 | 3% | 11x | casual 21, lazy 1 |
| `it is` | 116 | 161.7 | 69.7 | 5% | 3x | casual 79, lazy 36, angry 1 |
| `and then` | 23 | 32.1 | 25.1 | 3% | 10x | casual 15, lazy 8 |
| `is a` | 379 | 528.2 | 73.9 | 7% | 1x | casual 147, angry 116, lazy 116 |
| `a month` | 31 | 43.2 | 33.4 | 3% | 8x | casual 20, lazy 7, angry 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `were you able to` | 4 | 8 | 22.7 | angry 8 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `were you able` | 3 | 8 | 15.7 | angry 8 |
| `an early night` | 3 | 11 | 14.5 | casual 10, lazy 1 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 22 | 13.8 | casual 15, angry 7 |
| `the front desk` | 3 | 12 | 13.4 | angry 7, lazy 4, casual 1 |
| `did they say` | 3 | 8 | 12.9 | angry 4, casual 4 |
| `the post office` | 3 | 8 | 12.8 | casual 7, lazy 1 |
| `two hours of` | 3 | 8 | 12.4 | lazy 4, angry 2, casual 2 |
| `you able to` | 3 | 8 | 12.3 | angry 8 |
| `i have been` | 3 | 11 | 12.3 | casual 9, lazy 2 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `for an hour` | 3 | 10 | 12.1 | casual 8, angry 1, lazy 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `how long did` | 3 | 12 | 11.5 | casual 9, angry 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `has it been` | 3 | 8 | 10.8 | casual 8 |
| `and i am` | 3 | 8 | 10.6 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `group chat` | 2 | 8 | 10.2 | lazy 4, angry 2, casual 2 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `too much` | 2 | casual 9, lazy 9 |
| `a good` | 2 | casual 69, lazy 16 |
| `is it` | 2 | casual 100, angry 6 |
| `it the` | 3 | casual 34, lazy 4, angry 1 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `to work` | 2 | casual 7, lazy 1 |
| `luck with` | 1 | casual 8 |
| `point of` | 2 | lazy 5, casual 4 |
| `by the` | 3 | casual 31, lazy 21, angry 7 |
| `whole day` | 3 | casual 4, lazy 4, angry 2 |
| `was it` | 2 | casual 65, angry 3 |
| `good luck` | 3 | casual 9, lazy 2, angry 1 |
| `take it` | 1 | casual 13 |
| `the first` | 3 | casual 40, lazy 38, angry 5 |
| `i was` | 2 | casual 14, lazy 2 |
| `in the` | 3 | casual 171, lazy 68, angry 43 |
| `oh no` | 1 | casual 18 |
| `have been` | 3 | casual 13, lazy 4, angry 1 |
| `all week` | 3 | casual 13, lazy 3, angry 2 |
| `a real` | 3 | casual 82, angry 11, lazy 10 |
| `this morning` | 2 | casual 21, lazy 1 |
| `it is` | 3 | casual 79, lazy 36, angry 1 |
| `and then` | 2 | casual 15, lazy 8 |
| `is a` | 3 | casual 147, angry 116, lazy 116 |
| `a month` | 3 | casual 20, lazy 7, angry 4 |

## 4. Opener maps

- assistant pos 0 (n=7175): a 7.7%, the 3.1%, did 2.6%, that 2.3%, was 2.2%, haha 1.9%
- assistant pos 1 (n=7175): the 12.4%, a 2.4%, you 2.3%, is 2.0%, it 1.2%, and 0.9%
- assistant pos 2 (n=7174): the 5.8%, is 3.6%, a 2.4%, are 2.4%, of 1.7%, for 1.3%
- assistant pos last (n=7175): it 4.6%, now 1.5%, time 1.4%, one 1.1%, again 1.0%, day 0.9%
- user pos 0 (n=7175): the 12.5%, my 10.3%, our 8.5%, i 6.8%, did 3.6%, a 3.0%
- user pos 1 (n=7112): the 4.4%, you 3.1%, a 2.5%, was 1.4%, did 1.4%, is 1.3%
- user pos 2 (n=7023): the 6.7%, a 2.9%, is 2.3%, you 1.8%, and 1.6%, got 1.4%
- user pos last (n=7175): again 2.8%, it 1.8%, now 1.7%, week 1.6%, today 1.4%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.1%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

