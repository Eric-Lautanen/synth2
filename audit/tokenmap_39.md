# synth2 token-attractor map

Generated 2026-10-16 12:22  |  corpus 5490 rows, **7644 assistant turns**, 7644 user turns
Probe: `probe_out39_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-16T10:46:00

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.9% | 2.9% | -0.0 |
| `the`-opener (user) | 12.9% | 13.0% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a good` | 5% | 15% | 4x | 13x |
| `is a` | 8% | 13% | 1x | 2x |
| `the evening` | - | 5% | - | 32x |
| `you get` | - | 7% | - | 9x |
| `is the` | - | 10% | - | 2x |
| `a small` | - | 5% | - | 12x |
| `that is` | 3% | 7% | 2x | 4x |
| `how long` | - | 5% | - | 10x |
| `a bit` | 8% | 5% | 15x | 9x |
| `been a` | - | 3% | - | 32x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.9% | < 12% |
| `the`-opener (user) | 13.0% | n/a |
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
| `a good` | 85 | 111.2 | 14.4 | 15% | 13x | casual 69, lazy 16 |
| `is a` | 447 | 584.8 | 72.0 | 13% | 2x | angry 184, casual 147, lazy 116 |
| `the evening` | 12 | 15.7 | 7.8 | 5% | 32x | lazy 8, casual 4 |
| `you get` | 57 | 74.6 | 66.7 | 7% | 9x | casual 49, lazy 5, angry 3 |
| `is the` | 410 | 536.4 | 90.3 | 10% | 2x | casual 251, lazy 116, angry 43 |
| `a small` | 31 | 40.6 | 13.1 | 5% | 12x | lazy 16, casual 13, angry 2 |
| `that is` | 115 | 150.4 | 14.4 | 7% | 4x | casual 80, lazy 26, angry 9 |
| `how long` | 38 | 49.7 | 18.3 | 5% | 10x | casual 30, angry 7, lazy 1 |
| `a bit` | 41 | 53.6 | 41.9 | 5% | 9x | casual 39, angry 1, lazy 1 |
| `been a` | 8 | 10.5 | 5.2 | 3% | 32x | casual 7, angry 1 |
| `good one` | 9 | 11.8 | 3.9 | 3% | 28x | casual 8, lazy 1 |
| `i have been` | 11 | 14.4 | 22.2 | 3% | 23x | casual 9, lazy 2 |
| `for the` | 213 | 278.6 | 263.0 | 7% | 2x | casual 135, angry 53, lazy 25 |
| `well done` | 12 | 15.7 | 1.3 | 3% | 21x | casual 12 |
| `long did` | 12 | 15.7 | 6.5 | 3% | 21x | casual 9, angry 3 |
| `the best` | 79 | 103.3 | 37.9 | 5% | 5x | casual 53, lazy 26 |
| `is fine` | 14 | 18.3 | 5.2 | 3% | 18x | casual 8, lazy 5, angry 1 |
| `i've been` | 15 | 19.6 | 20.9 | 3% | 17x | casual 15 |
| `do you` | 94 | 123.0 | 68.0 | 5% | 4x | casual 74, angry 19, lazy 1 |
| `bit of` | 17 | 22.2 | 11.8 | 3% | 15x | casual 17 |
| `oh no` | 18 | 23.5 | 9.2 | 3% | 14x | casual 18 |
| `the school` | 19 | 24.9 | 26.2 | 3% | 13x | angry 10, casual 8, lazy 1 |
| `day is` | 19 | 24.9 | 2.6 | 3% | 13x | lazy 9, angry 5, casual 5 |
| `of the` | 146 | 191.0 | 128.2 | 5% | 3x | casual 84, lazy 39, angry 23 |
| `the whole` | 160 | 209.3 | 128.2 | 5% | 2x | lazy 83, casual 55, angry 22 |

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
| `have you tried` | 3 | 22 | 13.9 | casual 15, angry 7 |
| `at this point` | 3 | 10 | 13.9 | lazy 5, casual 4, angry 1 |
| `the front desk` | 3 | 12 | 13.3 | angry 7, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `did they say` | 3 | 8 | 12.8 | angry 4, casual 4 |
| `i have been` | 3 | 11 | 12.5 | casual 9, lazy 2 |
| `two hours of` | 3 | 9 | 12.3 | lazy 4, angry 3, casual 2 |
| `you able to` | 3 | 8 | 12.3 | angry 8 |
| `fell asleep` | 2 | 8 | 12.2 | casual 4, lazy 4 |
| `for an hour` | 3 | 10 | 11.8 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.7 | casual 5, lazy 2, angry 1 |
| `a couple of` | 3 | 12 | 11.5 | casual 11, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `feel like a` | 3 | 9 | 11.4 | lazy 6, casual 3 |
| `how long did` | 3 | 12 | 11.3 | casual 9, angry 3 |
| `did you find` | 3 | 9 | 11.1 | casual 9 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `did you get` | 3 | 44 | 10.9 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.7 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.4 | casual 15, angry 2 |
| `how do you` | 3 | 20 | 10.2 | angry 17, casual 2, lazy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a good` | 2 | casual 69, lazy 16 |
| `is a` | 3 | angry 184, casual 147, lazy 116 |
| `the evening` | 2 | lazy 8, casual 4 |
| `you get` | 3 | casual 49, lazy 5, angry 3 |
| `is the` | 3 | casual 251, lazy 116, angry 43 |
| `a small` | 3 | lazy 16, casual 13, angry 2 |
| `that is` | 3 | casual 80, lazy 26, angry 9 |
| `how long` | 3 | casual 30, angry 7, lazy 1 |
| `a bit` | 3 | casual 39, angry 1, lazy 1 |
| `been a` | 2 | casual 7, angry 1 |
| `good one` | 2 | casual 8, lazy 1 |
| `i have been` | 2 | casual 9, lazy 2 |
| `for the` | 3 | casual 135, angry 53, lazy 25 |
| `well done` | 1 | casual 12 |
| `long did` | 2 | casual 9, angry 3 |
| `the best` | 2 | casual 53, lazy 26 |
| `is fine` | 3 | casual 8, lazy 5, angry 1 |
| `i've been` | 1 | casual 15 |
| `do you` | 3 | casual 74, angry 19, lazy 1 |
| `bit of` | 1 | casual 17 |
| `oh no` | 1 | casual 18 |
| `the school` | 3 | angry 10, casual 8, lazy 1 |
| `day is` | 3 | lazy 9, angry 5, casual 5 |
| `of the` | 3 | casual 84, lazy 39, angry 23 |
| `the whole` | 3 | lazy 83, casual 55, angry 22 |

## 4. Opener maps

- assistant pos 0 (n=7644): a 8.0%, the 2.9%, did 2.5%, how 2.2%, that 2.1%, was 2.1%
- assistant pos 1 (n=7644): the 11.9%, a 2.3%, you 2.2%, is 2.2%, does 1.3%, it 1.1%
- assistant pos 2 (n=7643): the 6.0%, is 3.4%, a 3.3%, are 2.2%, of 1.7%, for 1.4%
- assistant pos last (n=7644): it 4.4%, now 1.4%, time 1.4%, one 1.0%, you 1.0%, again 0.9%
- user pos 0 (n=7644): the 13.0%, my 10.8%, our 8.3%, i 6.6%, did 3.4%, a 2.9%
- user pos 1 (n=7581): the 4.2%, you 3.0%, a 2.4%, was 1.3%, did 1.3%, is 1.2%
- user pos 2 (n=7492): the 6.5%, a 2.9%, is 2.2%, you 1.7%, and 1.5%, got 1.3%
- user pos last (n=7644): again 2.7%, it 1.8%, now 1.6%, week 1.5%, today 1.3%, night 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.7%**; model outputs: **16.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

