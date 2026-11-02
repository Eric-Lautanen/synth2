# synth2 token-attractor map

Generated 2026-10-20 16:15  |  corpus 7490 rows, **9805 assistant turns**, 9805 user turns
Probe: `probe_out66_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-20T13:46:58

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.2% | 4.2% | +0.0 |
| `the`-opener (user) | 14.0% | 14.0% | -0.0 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a day` | - | 7% | - | 19x |
| `i have been` | - | 5% | - | 45x |
| `of the` | - | 8% | - | 5x |
| `a bit` | - | 5% | - | 12x |
| `are easy` | - | 3% | - | 36x |
| `it's been` | - | 3% | - | 33x |
| `not the` | - | 3% | - | 30x |
| `the quiet` | - | 3% | - | 25x |
| `in it` | - | 3% | - | 22x |
| `did you` | 5% | 7% | 2x | 2x |

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
| `a day` | 35 | 35.7 | 20.4 | 7% | 19x | casual 19, lazy 11, angry 5 |
| `i have been` | 11 | 11.2 | 24.5 | 5% | 45x | casual 9, lazy 2 |
| `of the` | 174 | 177.5 | 128.5 | 8% | 5x | casual 84, lazy 39, angry 29 |
| `a bit` | 40 | 40.8 | 32.6 | 5% | 12x | casual 38, angry 1, lazy 1 |
| `are easy` | 9 | 9.2 | 1.0 | 3% | 36x | lazy 4, casual 3, angry 1 |
| `it's been` | 10 | 10.2 | 5.1 | 3% | 33x | casual 10 |
| `not the` | 11 | 11.2 | 6.1 | 3% | 30x | casual 8, lazy 2, sexy 1 |
| `the quiet` | 13 | 13.3 | 1.0 | 3% | 25x | casual 7, lazy 5, angry 1 |
| `in it` | 15 | 15.3 | 20.4 | 3% | 22x | casual 13, lazy 1, sexy 1 |
| `did you` | 281 | 286.6 | 251.9 | 7% | 2x | casual 192, sexy 56, angry 28 |
| `all week` | 22 | 22.4 | 22.4 | 3% | 15x | casual 13, angry 4, lazy 3 |
| `did not` | 26 | 26.5 | 31.6 | 3% | 13x | casual 12, lazy 6, angry 4 |
| `that is` | 142 | 144.8 | 13.3 | 5% | 3x | casual 76, lazy 26, sexy 25 |
| `but the` | 27 | 27.5 | 53.0 | 3% | 12x | casual 21, lazy 4, angry 1 |
| `a long` | 32 | 32.6 | 7.1 | 3% | 10x | casual 21, lazy 8, angry 3 |
| `this week` | 36 | 36.7 | 47.9 | 3% | 9x | casual 26, angry 4, lazy 4 |
| `the next` | 36 | 36.7 | 16.3 | 3% | 9x | casual 17, lazy 8, sexy 7 |
| `is just` | 37 | 37.7 | 3.1 | 3% | 9x | lazy 20, angry 11, casual 6 |
| `is not` | 45 | 45.9 | 10.2 | 3% | 7x | angry 27, casual 12, lazy 6 |
| `the day` | 46 | 46.9 | 20.4 | 3% | 7x | lazy 22, casual 17, angry 4 |
| `the end` | 48 | 49.0 | 33.7 | 3% | 7x | casual 26, angry 10, lazy 7 |
| `a good` | 58 | 59.2 | 14.3 | 3% | 6x | casual 43, lazy 12, sexy 3 |
| `you get` | 59 | 60.2 | 52.0 | 3% | 6x | casual 49, angry 5, lazy 5 |
| `and i` | 60 | 61.2 | 89.8 | 3% | 5x | casual 29, lazy 25, sexy 6 |
| `the same` | 114 | 116.3 | 106.1 | 3% | 3x | angry 36, casual 36, lazy 29 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.5 | lazy 5, sexy 2, casual 1 |
| `an early night` | 3 | 11 | 14.0 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 12.9 | casual 7, sexy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `ten minutes of` | 3 | 10 | 12.6 | sexy 7, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.3 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `in ten minutes` | 3 | 8 | 12.1 | casual 5, sexy 3 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `fell asleep` | 2 | 9 | 11.4 | casual 4, lazy 4, sexy 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a day` | 3 | casual 19, lazy 11, angry 5 |
| `i have been` | 2 | casual 9, lazy 2 |
| `of the` | 4 | casual 84, lazy 39, angry 29, sexy 22 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `are easy` | 4 | lazy 4, casual 3, angry 1, sexy 1 |
| `it's been` | 1 | casual 10 |
| `not the` | 3 | casual 8, lazy 2, sexy 1 |
| `the quiet` | 3 | casual 7, lazy 5, angry 1 |
| `in it` | 3 | casual 13, lazy 1, sexy 1 |
| `did you` | 4 | casual 192, sexy 56, angry 28, lazy 5 |
| `all week` | 4 | casual 13, angry 4, lazy 3, sexy 2 |
| `did not` | 4 | casual 12, lazy 6, angry 4, sexy 4 |
| `that is` | 4 | casual 76, lazy 26, sexy 25, angry 15 |
| `but the` | 4 | casual 21, lazy 4, angry 1, sexy 1 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `this week` | 4 | casual 26, angry 4, lazy 4, sexy 2 |
| `the next` | 4 | casual 17, lazy 8, sexy 7, angry 4 |
| `is just` | 3 | lazy 20, angry 11, casual 6 |
| `is not` | 3 | angry 27, casual 12, lazy 6 |
| `the day` | 4 | lazy 22, casual 17, angry 4, sexy 3 |
| `the end` | 4 | casual 26, angry 10, lazy 7, sexy 5 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `and i` | 3 | casual 29, lazy 25, sexy 6 |
| `the same` | 4 | angry 36, casual 36, lazy 29, sexy 13 |

## 4. Opener maps

- assistant pos 0 (n=9805): a 9.1%, the 4.2%, did 2.2%, how 2.1%, was 1.8%, that 1.8%
- assistant pos 1 (n=9805): the 11.0%, a 2.2%, you 1.8%, is 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=9804): the 6.8%, a 3.0%, is 2.6%, of 1.9%, for 1.8%, are 1.7%
- assistant pos last (n=9805): it 4.0%, now 1.6%, you 1.2%, time 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9805): the 14.0%, my 10.1%, our 8.1%, i 6.2%, we 5.5%, you 4.7%
- user pos 1 (n=9742): the 3.3%, you 2.4%, a 1.9%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=9653): the 7.5%, a 3.1%, is 1.8%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9805): again 2.3%, it 2.0%, now 1.3%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.5%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1608 |
| lazy | 1 / 2155 |

