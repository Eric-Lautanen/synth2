# synth2 token-attractor map

Generated 2026-10-17 20:57  |  corpus 6374 rows, **8599 assistant turns**, 8599 user turns
Probe: `probe_out48_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-17T18:06:45

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.2% | +0.2 |
| `the`-opener (user) | 13.4% | 13.4% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `of it` | - | 7% | - | 15x |
| `for the` | - | 10% | - | 4x |
| `with a` | - | 7% | - | 6x |
| `of the` | - | 7% | - | 4x |
| `end of` | - | 3% | - | 36x |
| `a real` | - | 5% | - | 4x |
| `in the` | - | 7% | - | 2x |
| `up to` | - | 3% | - | 14x |
| `the store` | - | 3% | - | 14x |
| `was there` | - | 3% | - | 14x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.2% | < 12% |
| `the`-opener (user) | 13.4% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
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
| `of it` | 37 | 43.0 | 29.1 | 7% | 15x | casual 30, angry 4, lazy 3 |
| `for the` | 234 | 272.1 | 257.0 | 10% | 4x | casual 135, angry 64, lazy 24 |
| `with a` | 100 | 116.3 | 81.4 | 7% | 6x | casual 40, lazy 34, angry 24 |
| `of the` | 162 | 188.4 | 127.9 | 7% | 4x | casual 84, lazy 39, angry 29 |
| `end of` | 8 | 9.3 | 8.1 | 3% | 36x | lazy 4, casual 3, angry 1 |
| `a real` | 105 | 122.1 | 51.2 | 5% | 4x | casual 82, angry 13, lazy 10 |
| `in the` | 320 | 372.1 | 343.1 | 7% | 2x | casual 169, angry 69, lazy 68 |
| `up to` | 20 | 23.3 | 23.3 | 3% | 14x | casual 18, angry 1, sexy 1 |
| `the store` | 20 | 23.3 | 12.8 | 3% | 14x | angry 13, lazy 7 |
| `was there` | 21 | 24.4 | 1.2 | 3% | 14x | angry 11, casual 9, lazy 1 |
| `is a` | 449 | 522.2 | 68.6 | 7% | 1x | angry 208, casual 121, lazy 115 |
| `a long` | 32 | 37.2 | 8.1 | 3% | 9x | casual 21, lazy 8, angry 3 |
| `not a` | 34 | 39.5 | 9.3 | 3% | 8x | angry 16, casual 11, lazy 7 |
| `the whole` | 174 | 202.3 | 130.2 | 5% | 2x | lazy 83, casual 55, angry 32 |
| `a full` | 38 | 44.2 | 18.6 | 3% | 8x | lazy 17, angry 12, casual 9 |
| `did you get` | 44 | 51.2 | 48.8 | 3% | 7x | casual 40, angry 2, lazy 2 |
| `this time` | 50 | 58.1 | 18.6 | 3% | 6x | casual 42, angry 6, lazy 2 |
| `a good` | 55 | 64.0 | 14.0 | 3% | 5x | casual 43, lazy 12 |
| `and i` | 58 | 67.4 | 95.4 | 3% | 5x | casual 29, lazy 25, sexy 4 |
| `a new` | 62 | 72.1 | 73.3 | 3% | 5x | casual 37, angry 13, lazy 11 |
| `an hour` | 66 | 76.8 | 79.1 | 3% | 4x | casual 34, lazy 16, angry 12 |
| `when did` | 8 | 9.3 | 2.3 | 2% | 18x | casual 4, sexy 3, angry 1 |
| `three times` | 8 | 9.3 | 27.9 | 2% | 18x | angry 5, casual 2, lazy 1 |
| `three in` | 8 | 9.3 | 4.7 | 2% | 18x | casual 4, angry 2, lazy 2 |
| `the order` | 8 | 9.3 | 1.2 | 2% | 18x | angry 6, casual 1, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.2 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 14.0 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.2 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `fell asleep` | 2 | 8 | 11.8 | casual 4, lazy 4 |
| `for an hour` | 3 | 11 | 11.6 | casual 8, angry 1, lazy 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `a couple of` | 3 | 12 | 11.3 | casual 11, angry 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `did you find` | 3 | 9 | 10.8 | casual 9 |
| `did you get` | 3 | 44 | 10.7 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 9 | 10.7 | casual 7, lazy 1, sexy 1 |
| `why would a` | 3 | 8 | 10.5 | angry 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `of it` | 3 | casual 30, angry 4, lazy 3 |
| `for the` | 4 | casual 135, angry 64, lazy 24, sexy 11 |
| `with a` | 4 | casual 40, lazy 34, angry 24, sexy 2 |
| `of the` | 4 | casual 84, lazy 39, angry 29, sexy 10 |
| `end of` | 3 | lazy 4, casual 3, angry 1 |
| `a real` | 3 | casual 82, angry 13, lazy 10 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 14 |
| `up to` | 3 | casual 18, angry 1, sexy 1 |
| `the store` | 2 | angry 13, lazy 7 |
| `was there` | 3 | angry 11, casual 9, lazy 1 |
| `is a` | 4 | angry 208, casual 121, lazy 115, sexy 5 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `not a` | 3 | angry 16, casual 11, lazy 7 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 4 |
| `a full` | 3 | lazy 17, angry 12, casual 9 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `this time` | 3 | casual 42, angry 6, lazy 2 |
| `a good` | 2 | casual 43, lazy 12 |
| `and i` | 3 | casual 29, lazy 25, sexy 4 |
| `a new` | 4 | casual 37, angry 13, lazy 11, sexy 1 |
| `an hour` | 4 | casual 34, lazy 16, angry 12, sexy 4 |
| `when did` | 3 | casual 4, sexy 3, angry 1 |
| `three times` | 3 | angry 5, casual 2, lazy 1 |
| `three in` | 3 | casual 4, angry 2, lazy 2 |
| `the order` | 3 | angry 6, casual 1, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=8599): a 8.0%, the 3.2%, did 2.6%, how 2.4%, was 2.0%, that 2.0%
- assistant pos 1 (n=8599): the 11.7%, a 2.4%, is 2.0%, you 2.0%, does 1.4%, your 1.1%
- assistant pos 2 (n=8598): the 6.2%, a 3.1%, is 3.0%, are 2.0%, of 1.7%, for 1.7%
- assistant pos last (n=8599): it 4.2%, now 1.5%, time 1.3%, you 1.2%, again 1.0%, one 1.0%
- user pos 0 (n=8599): the 13.4%, my 10.6%, our 8.2%, i 6.7%, we 3.4%, they 3.2%
- user pos 1 (n=8536): the 3.7%, you 2.7%, a 2.2%, was 1.3%, did 1.1%, is 1.1%
- user pos 2 (n=8447): the 6.8%, a 3.0%, is 2.0%, you 1.7%, my 1.5%, and 1.4%
- user pos last (n=8599): again 2.6%, it 2.0%, now 1.5%, week 1.4%, night 1.3%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.2%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 402 |
| lazy | 1 / 2155 |

