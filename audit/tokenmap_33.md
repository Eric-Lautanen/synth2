# synth2 token-attractor map

Generated 2026-10-16 02:48  |  corpus 4870 rows, **6974 assistant turns**, 6974 user turns
Probe: `probe_out33_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T18:03:17

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.2% | 3.1% | -0.1 |
| `the`-opener (user) | 12.0% | 12.2% | +0.2 |
| copula-only | 0.7% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `going to` | - | 7% | - | 18x |
| `the whole` | - | 8% | - | 4x |
| `the first` | - | 7% | - | 6x |
| `just a` | - | 5% | - | 11x |
| `is it` | - | 7% | - | 4x |
| `the day` | - | 5% | - | 9x |
| `i have` | 8% | 5% | 12x | 7x |
| `the book` | - | 3% | - | 29x |
| `is the` | - | 8% | - | 1x |
| `who is` | - | 3% | - | 26x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.1% | < 12% |
| `the`-opener (user) | 12.2% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 37 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `going to` | 26 | 37.3 | 20.1 | 7% | 18x | casual 18, lazy 5, angry 3 |
| `the whole` | 158 | 226.6 | 136.2 | 8% | 4x | lazy 83, casual 55, angry 20 |
| `the first` | 81 | 116.1 | 80.3 | 7% | 6x | casual 40, lazy 38, angry 3 |
| `just a` | 32 | 45.9 | 21.5 | 5% | 11x | casual 22, angry 6, lazy 4 |
| `is it` | 106 | 152.0 | 31.5 | 7% | 4x | casual 100, angry 6 |
| `the day` | 40 | 57.4 | 21.5 | 5% | 9x | lazy 22, casual 16, angry 2 |
| `i have` | 47 | 67.4 | 91.8 | 5% | 7x | casual 35, lazy 12 |
| `the book` | 8 | 11.5 | 10.0 | 3% | 29x | casual 5, lazy 3 |
| `is the` | 397 | 569.3 | 97.5 | 8% | 1x | casual 251, lazy 116, angry 30 |
| `who is` | 9 | 12.9 | 1.4 | 3% | 26x | casual 7, angry 2 |
| `not the` | 10 | 14.3 | 7.2 | 3% | 23x | casual 8, lazy 2 |
| `a nightmare` | 10 | 14.3 | 5.7 | 3% | 23x | casual 9, angry 1 |
| `to get` | 11 | 15.8 | 11.5 | 3% | 21x | casual 7, angry 2, lazy 2 |
| `is good` | 12 | 17.2 | 2.9 | 3% | 19x | casual 11, lazy 1 |
| `hours of` | 13 | 18.6 | 12.9 | 3% | 18x | lazy 8, casual 3, angry 2 |
| `of course` | 14 | 20.1 | 2.9 | 3% | 17x | casual 7, angry 6, lazy 1 |
| `a good` | 85 | 121.9 | 15.8 | 5% | 4x | casual 69, lazy 16 |
| `the game` | 16 | 22.9 | 25.8 | 3% | 15x | casual 12, lazy 4 |
| `you going` | 17 | 24.4 | 7.2 | 3% | 14x | casual 15, angry 2 |
| `whole_thing` | 17 | 24.4 | 20.1 | 3% | 14x | casual 8, lazy 8, angry 1 |
| `in the` | 277 | 397.2 | 355.6 | 7% | 2x | casual 171, lazy 68, angry 38 |
| `too much` | 18 | 25.8 | 8.6 | 3% | 13x | casual 9, lazy 9 |
| `out the` | 22 | 31.5 | 35.8 | 3% | 11x | lazy 11, casual 9, angry 2 |
| `to the` | 118 | 169.2 | 169.2 | 5% | 3x | casual 75, lazy 32, angry 11 |
| `part of` | 24 | 34.4 | 4.3 | 3% | 10x | lazy 13, casual 11 |

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
| `have you tried` | 3 | 22 | 13.8 | casual 15, angry 7 |
| `at this point` | 3 | 9 | 13.7 | lazy 5, casual 4 |
| `the front desk` | 3 | 8 | 13.1 | lazy 4, angry 3, casual 1 |
| `the post office` | 3 | 8 | 13.1 | casual 7, lazy 1 |
| `did they say` | 3 | 8 | 13.0 | angry 4, casual 4 |
| `you able to` | 3 | 8 | 12.4 | angry 8 |
| `i have been` | 3 | 11 | 12.4 | casual 9, lazy 2 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `for an hour` | 3 | 9 | 12.0 | casual 8, lazy 1 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `how long did` | 3 | 12 | 11.5 | casual 9, angry 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `has it been` | 3 | 8 | 10.9 | casual 8 |
| `and i am` | 3 | 8 | 10.6 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `group chat` | 2 | 8 | 10.3 | lazy 4, angry 2, casual 2 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |
| `a lot of` | 3 | 10 | 10.2 | casual 7, lazy 3 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `going to` | 3 | casual 18, lazy 5, angry 3 |
| `the whole` | 3 | lazy 83, casual 55, angry 20 |
| `the first` | 3 | casual 40, lazy 38, angry 3 |
| `just a` | 3 | casual 22, angry 6, lazy 4 |
| `is it` | 2 | casual 100, angry 6 |
| `the day` | 3 | lazy 22, casual 16, angry 2 |
| `i have` | 2 | casual 35, lazy 12 |
| `the book` | 2 | casual 5, lazy 3 |
| `is the` | 3 | casual 251, lazy 116, angry 30 |
| `who is` | 2 | casual 7, angry 2 |
| `not the` | 2 | casual 8, lazy 2 |
| `a nightmare` | 2 | casual 9, angry 1 |
| `to get` | 3 | casual 7, angry 2, lazy 2 |
| `is good` | 2 | casual 11, lazy 1 |
| `hours of` | 3 | lazy 8, casual 3, angry 2 |
| `of course` | 3 | casual 7, angry 6, lazy 1 |
| `a good` | 2 | casual 69, lazy 16 |
| `the game` | 2 | casual 12, lazy 4 |
| `you going` | 2 | casual 15, angry 2 |
| `whole_thing` | 3 | casual 8, lazy 8, angry 1 |
| `in the` | 3 | casual 171, lazy 68, angry 38 |
| `too much` | 2 | casual 9, lazy 9 |
| `out the` | 3 | lazy 11, casual 9, angry 2 |
| `to the` | 3 | casual 75, lazy 32, angry 11 |
| `part of` | 2 | lazy 13, casual 11 |

## 4. Opener maps

- assistant pos 0 (n=6974): a 7.6%, the 3.1%, did 2.4%, that 2.3%, haha 1.9%, was 1.6%
- assistant pos 1 (n=6974): the 11.6%, a 2.3%, you 2.3%, is 2.0%, it 1.2%, and 0.9%
- assistant pos 2 (n=6973): the 5.9%, is 3.6%, are 2.4%, a 2.3%, of 1.6%, for 1.2%
- assistant pos last (n=6974): it 4.7%, now 1.5%, time 1.5%, one 1.1%, again 1.0%, day 0.9%
- user pos 0 (n=6974): the 12.2%, my 10.0%, our 8.3%, i 7.0%, did 3.7%, a 3.1%
- user pos 1 (n=6911): the 4.5%, you 3.2%, a 2.6%, was 1.5%, did 1.4%, is 1.3%
- user pos 2 (n=6822): the 6.8%, a 2.9%, is 2.3%, you 1.8%, and 1.6%, got 1.3%
- user pos last (n=6974): again 2.8%, it 1.9%, now 1.6%, week 1.6%, today 1.4%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.3%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

