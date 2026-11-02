# synth2 token-attractor map

Generated 2026-10-20 10:36  |  corpus 7366 rows, **9671 assistant turns**, 9671 user turns
Probe: `probe_out64_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-20T08:02:07

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.1% | 4.2% | +0.0 |
| `the`-opener (user) | 14.0% | 14.0% | +0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `it is` | 5% | 8% | 4x | 6x |
| `no idea` | - | 5% | - | 40x |
| `i have` | 3% | 7% | 6x | 13x |
| `is fine` | - | 5% | - | 35x |
| `is worth the` | - | 3% | - | 40x |
| `could not` | - | 3% | - | 40x |
| `is a` | - | 8% | - | 2x |
| `it's been` | - | 3% | - | 32x |
| `a win` | - | 3% | - | 27x |
| `have been` | - | 3% | - | 17x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.2% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
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
| `it is` | 126 | 130.3 | 54.8 | 8% | 6x | casual 79, lazy 36, angry 7 |
| `no idea` | 12 | 12.4 | 8.3 | 5% | 40x | casual 10, lazy 2 |
| `i have` | 51 | 52.7 | 80.7 | 7% | 13x | casual 35, lazy 12, sexy 4 |
| `is fine` | 14 | 14.5 | 4.1 | 5% | 35x | casual 8, lazy 5, angry 1 |
| `is worth the` | 8 | 8.3 | 1.0 | 3% | 40x | casual 8 |
| `could not` | 8 | 8.3 | 17.6 | 3% | 40x | casual 3, sexy 3, angry 2 |
| `is a` | 457 | 472.5 | 62.0 | 8% | 2x | angry 208, casual 120, lazy 115 |
| `it's been` | 10 | 10.3 | 5.2 | 3% | 32x | casual 10 |
| `a win` | 12 | 12.4 | 4.1 | 3% | 27x | casual 10, lazy 1, sexy 1 |
| `have been` | 19 | 19.6 | 41.4 | 3% | 17x | casual 13, lazy 4, angry 1 |
| `the weekend` | 20 | 20.7 | 40.3 | 3% | 16x | casual 15, lazy 4, sexy 1 |
| `i know` | 20 | 20.7 | 13.4 | 3% | 16x | casual 16, lazy 2, sexy 2 |
| `day is` | 20 | 20.7 | 2.1 | 3% | 16x | lazy 9, angry 6, casual 5 |
| `the coffee` | 25 | 25.9 | 17.6 | 3% | 13x | lazy 12, casual 7, sexy 5 |
| `is the` | 430 | 444.6 | 71.3 | 7% | 1x | casual 250, lazy 116, angry 49 |
| `the way` | 32 | 33.1 | 23.8 | 3% | 10x | casual 21, sexy 6, lazy 4 |
| `next time` | 35 | 36.2 | 2.1 | 3% | 9x | casual 15, lazy 11, sexy 7 |
| `the whole` | 181 | 187.2 | 125.1 | 5% | 3x | lazy 83, casual 55, angry 32 |
| `of it` | 41 | 42.4 | 26.9 | 3% | 8x | casual 31, angry 4, lazy 3 |
| `did it` | 42 | 43.4 | 13.4 | 3% | 8x | casual 34, lazy 4, angry 2 |
| `a full` | 44 | 45.5 | 21.7 | 3% | 7x | lazy 17, angry 12, casual 9 |
| `the day` | 46 | 47.6 | 20.7 | 3% | 7x | lazy 22, casual 17, angry 4 |
| `for one` | 46 | 47.6 | 15.5 | 3% | 7x | angry 21, lazy 12, casual 7 |
| `means the` | 51 | 52.7 | 2.1 | 3% | 6x | lazy 36, angry 8, casual 6 |
| `and i` | 60 | 62.0 | 91.0 | 3% | 5x | casual 29, lazy 25, sexy 6 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `on the first try` | 4 | 8 | 16.5 | lazy 5, sexy 2, casual 1 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.1 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 13.0 | casual 7, sexy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `two hours of` | 3 | 11 | 12.4 | angry 4, lazy 4, casual 2 |
| `ten minutes of` | 3 | 8 | 12.3 | sexy 5, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.3 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `in ten minutes` | 3 | 8 | 12.1 | casual 5, sexy 3 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 13 | 11.6 | casual 8, sexy 3, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `fell asleep` | 2 | 9 | 11.5 | casual 4, lazy 4, sexy 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 4 |
| `no idea` | 2 | casual 10, lazy 2 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `is fine` | 3 | casual 8, lazy 5, angry 1 |
| `is worth the` | 1 | casual 8 |
| `could not` | 3 | casual 3, sexy 3, angry 2 |
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 14 |
| `it's been` | 1 | casual 10 |
| `a win` | 3 | casual 10, lazy 1, sexy 1 |
| `have been` | 4 | casual 13, lazy 4, angry 1, sexy 1 |
| `the weekend` | 3 | casual 15, lazy 4, sexy 1 |
| `i know` | 3 | casual 16, lazy 2, sexy 2 |
| `day is` | 3 | lazy 9, angry 6, casual 5 |
| `the coffee` | 4 | lazy 12, casual 7, sexy 5, angry 1 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 15 |
| `the way` | 4 | casual 21, sexy 6, lazy 4, angry 1 |
| `next time` | 4 | casual 15, lazy 11, sexy 7, angry 2 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 11 |
| `of it` | 4 | casual 31, angry 4, lazy 3, sexy 3 |
| `did it` | 4 | casual 34, lazy 4, angry 2, sexy 2 |
| `a full` | 4 | lazy 17, angry 12, casual 9, sexy 6 |
| `the day` | 4 | lazy 22, casual 17, angry 4, sexy 3 |
| `for one` | 4 | angry 21, lazy 12, casual 7, sexy 6 |
| `means the` | 4 | lazy 36, angry 8, casual 6, sexy 1 |
| `and i` | 3 | casual 29, lazy 25, sexy 6 |

## 4. Opener maps

- assistant pos 0 (n=9671): a 8.9%, the 4.2%, did 2.3%, how 2.2%, was 1.8%, that 1.8%
- assistant pos 1 (n=9671): the 11.1%, a 2.2%, you 1.8%, is 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=9670): the 6.8%, a 3.0%, is 2.7%, of 1.8%, are 1.8%, for 1.7%
- assistant pos last (n=9671): it 4.0%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9671): the 14.0%, my 10.1%, our 8.1%, i 6.3%, we 5.3%, you 4.5%
- user pos 1 (n=9608): the 3.4%, you 2.4%, a 1.9%, was 1.1%, got 1.1%, did 1.1%
- user pos 2 (n=9519): the 7.4%, a 3.1%, is 1.8%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9671): again 2.4%, it 2.0%, now 1.3%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.6%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1474 |
| lazy | 1 / 2155 |

