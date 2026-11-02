# synth2 token-attractor map

Generated 2026-10-18 00:17  |  corpus 6436 rows, **8666 assistant turns**, 8666 user turns
Probe: `probe_out49_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-17T20:57:47

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.2% | 3.3% | +0.1 |
| `the`-opener (user) | 13.4% | 13.5% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the whole` | 5% | 8% | 2x | 4x |
| `after a` | - | 5% | - | 13x |
| `this time` | 3% | 5% | 6x | 9x |
| `i will` | - | 5% | - | 8x |
| `you get` | - | 5% | - | 7x |
| `day and` | - | 3% | - | 32x |
| `to get` | - | 3% | - | 29x |
| `as always` | - | 3% | - | 29x |
| `a week` | - | 5% | - | 6x |
| `one you` | - | 3% | - | 26x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.3% | < 12% |
| `the`-opener (user) | 13.5% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 35 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `the whole` | 175 | 201.9 | 130.4 | 8% | 4x | lazy 83, casual 55, angry 32 |
| `after a` | 33 | 38.1 | 15.0 | 5% | 13x | angry 16, casual 12, lazy 4 |
| `this time` | 50 | 57.7 | 18.5 | 5% | 9x | casual 42, angry 6, lazy 2 |
| `i will` | 52 | 60.0 | 9.2 | 5% | 8x | casual 31, lazy 14, sexy 7 |
| `you get` | 59 | 68.1 | 58.9 | 5% | 7x | casual 49, angry 5, lazy 5 |
| `day and` | 9 | 10.4 | 4.6 | 3% | 32x | casual 6, lazy 2, angry 1 |
| `to get` | 10 | 11.5 | 11.5 | 3% | 29x | casual 7, lazy 2, angry 1 |
| `as always` | 10 | 11.5 | 2.3 | 3% | 29x | casual 10 |
| `a week` | 69 | 79.6 | 60.0 | 5% | 6x | casual 36, lazy 22, angry 10 |
| `one you` | 11 | 12.7 | 1.2 | 3% | 26x | casual 9, lazy 2 |
| `with your` | 16 | 18.5 | 4.6 | 3% | 18x | casual 10, angry 4, sexy 2 |
| `then the` | 21 | 24.2 | 11.5 | 3% | 14x | casual 15, lazy 5, sexy 1 |
| `the weather` | 21 | 24.2 | 13.8 | 3% | 14x | casual 18, lazy 3 |
| `you got` | 22 | 25.4 | 6.9 | 3% | 13x | casual 21, angry 1 |
| `a quiet` | 25 | 28.8 | 3.5 | 3% | 12x | casual 12, lazy 7, angry 6 |
| `the night` | 26 | 30.0 | 13.8 | 3% | 11x | lazy 9, casual 7, angry 5 |
| `to the` | 141 | 162.7 | 153.5 | 5% | 3x | casual 75, lazy 32, angry 27 |
| `of it` | 37 | 42.7 | 28.8 | 3% | 8x | casual 30, angry 4, lazy 3 |
| `your own` | 38 | 43.8 | 2.3 | 3% | 8x | angry 24, casual 11, lazy 3 |
| `on the` | 268 | 309.3 | 280.4 | 5% | 2x | casual 151, lazy 51, angry 50 |
| `i am` | 62 | 71.5 | 41.5 | 3% | 5x | casual 44, lazy 11, sexy 6 |
| `the first` | 88 | 101.5 | 71.5 | 3% | 3x | casual 40, lazy 38, angry 7 |
| `with the` | 90 | 103.9 | 75.0 | 3% | 3x | casual 55, angry 18, lazy 12 |
| `is the` | 418 | 482.3 | 79.6 | 5% | 1x | casual 250, lazy 116, angry 49 |
| `have you` | 107 | 123.5 | 27.7 | 3% | 3x | casual 80, angry 27 |

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
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `fell asleep` | 2 | 8 | 11.7 | casual 4, lazy 4 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `for an hour` | 3 | 11 | 11.5 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `a couple of` | 3 | 12 | 11.3 | casual 11, angry 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `did you find` | 3 | 9 | 10.8 | casual 9 |
| `did you get` | 3 | 44 | 10.7 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 9 | 10.6 | casual 7, lazy 1, sexy 1 |
| `why would a` | 3 | 8 | 10.5 | angry 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 5 |
| `after a` | 4 | angry 16, casual 12, lazy 4, sexy 1 |
| `this time` | 3 | casual 42, angry 6, lazy 2 |
| `i will` | 3 | casual 31, lazy 14, sexy 7 |
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `day and` | 3 | casual 6, lazy 2, angry 1 |
| `to get` | 3 | casual 7, lazy 2, angry 1 |
| `as always` | 1 | casual 10 |
| `a week` | 4 | casual 36, lazy 22, angry 10, sexy 1 |
| `one you` | 2 | casual 9, lazy 2 |
| `with your` | 3 | casual 10, angry 4, sexy 2 |
| `then the` | 3 | casual 15, lazy 5, sexy 1 |
| `the weather` | 2 | casual 18, lazy 3 |
| `you got` | 2 | casual 21, angry 1 |
| `a quiet` | 3 | casual 12, lazy 7, angry 6 |
| `the night` | 4 | lazy 9, casual 7, angry 5, sexy 5 |
| `to the` | 4 | casual 75, lazy 32, angry 27, sexy 7 |
| `of it` | 3 | casual 30, angry 4, lazy 3 |
| `your own` | 3 | angry 24, casual 11, lazy 3 |
| `on the` | 4 | casual 151, lazy 51, angry 50, sexy 16 |
| `i am` | 4 | casual 44, lazy 11, sexy 6, angry 1 |
| `the first` | 4 | casual 40, lazy 38, angry 7, sexy 3 |
| `with the` | 4 | casual 55, angry 18, lazy 12, sexy 5 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 3 |
| `have you` | 2 | casual 80, angry 27 |

## 4. Opener maps

- assistant pos 0 (n=8666): a 8.0%, the 3.3%, did 2.5%, how 2.4%, was 2.0%, that 2.0%
- assistant pos 1 (n=8666): the 11.7%, a 2.4%, you 2.0%, is 2.0%, does 1.4%, your 1.1%
- assistant pos 2 (n=8665): the 6.2%, a 3.1%, is 3.0%, are 2.0%, of 1.7%, for 1.6%
- assistant pos last (n=8666): it 4.1%, now 1.5%, time 1.3%, you 1.2%, again 1.0%, one 1.0%
- user pos 0 (n=8666): the 13.5%, my 10.5%, our 8.1%, i 6.7%, we 3.6%, they 3.2%
- user pos 1 (n=8603): the 3.7%, you 2.7%, a 2.1%, was 1.3%, did 1.1%, is 1.0%
- user pos 2 (n=8514): the 6.8%, a 3.0%, is 2.0%, you 1.7%, my 1.5%, and 1.4%
- user pos last (n=8666): again 2.6%, it 2.0%, now 1.5%, week 1.4%, night 1.2%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.1%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 469 |
| lazy | 1 / 2155 |

