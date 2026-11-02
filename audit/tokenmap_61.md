# synth2 token-attractor map

Generated 2026-10-19 09:57  |  corpus 7180 rows, **9470 assistant turns**, 9470 user turns
Probe: `probe_out61_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-19T07:41:10

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.9% | 4.0% | +0.0 |
| `the`-opener (user) | 14.0% | 13.9% | -0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a long` | - | 7% | - | 20x |
| `it a` | - | 5% | - | 12x |
| `is a` | - | 8% | - | 2x |
| `a couple of` | - | 3% | - | 26x |
| `was it` | - | 5% | - | 6x |
| `the walk` | - | 3% | - | 23x |
| `is fine` | - | 3% | - | 23x |
| `worth every` | - | 3% | - | 19x |
| `on the` | - | 7% | - | 2x |
| `a real` | - | 5% | - | 5x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.0% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 40 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a long` | 32 | 33.8 | 7.4 | 7% | 20x | casual 21, lazy 8, angry 3 |
| `it a` | 41 | 43.3 | 9.5 | 5% | 12x | casual 34, lazy 4, angry 2 |
| `is a` | 455 | 480.5 | 63.4 | 8% | 2x | angry 208, casual 120, lazy 115 |
| `a couple of` | 12 | 12.7 | 5.3 | 3% | 26x | casual 11, angry 1 |
| `was it` | 80 | 84.5 | 22.2 | 5% | 6x | casual 65, sexy 11, angry 4 |
| `the walk` | 14 | 14.8 | 8.4 | 3% | 23x | casual 7, lazy 4, sexy 2 |
| `is fine` | 14 | 14.8 | 4.2 | 3% | 23x | casual 8, lazy 5, angry 1 |
| `worth every` | 17 | 18.0 | 9.5 | 3% | 19x | sexy 9, casual 4, lazy 4 |
| `on the` | 309 | 326.3 | 286.2 | 7% | 2x | casual 151, sexy 57, lazy 51 |
| `a real` | 105 | 110.9 | 46.5 | 5% | 5x | casual 82, angry 13, lazy 10 |
| `get a` | 22 | 23.2 | 7.4 | 3% | 14x | casual 15, sexy 4, lazy 3 |
| `a phone` | 23 | 24.3 | 11.6 | 3% | 14x | angry 10, casual 6, lazy 5 |
| `the night` | 27 | 28.5 | 13.7 | 3% | 12x | lazy 9, casual 7, sexy 6 |
| `is worth` | 34 | 35.9 | 4.2 | 3% | 9x | casual 23, angry 5, lazy 5 |
| `the next` | 35 | 37.0 | 14.8 | 3% | 9x | casual 17, lazy 8, sexy 6 |
| `with no` | 39 | 41.2 | 28.5 | 3% | 8x | angry 33, sexy 3, lazy 2 |
| `did you get` | 44 | 46.5 | 44.4 | 3% | 7x | casual 40, angry 2, lazy 2 |
| `a whole` | 48 | 50.7 | 24.3 | 3% | 7x | angry 20, lazy 16, casual 11 |
| `does it` | 56 | 59.1 | 4.2 | 3% | 6x | casual 44, lazy 5, angry 4 |
| `for the` | 264 | 278.8 | 258.7 | 5% | 2x | casual 135, angry 64, sexy 41 |
| `a good` | 58 | 61.2 | 14.8 | 3% | 5x | casual 43, lazy 12, sexy 3 |
| `out of` | 66 | 69.7 | 82.4 | 3% | 5x | casual 34, angry 15, lazy 14 |
| `from the` | 74 | 78.1 | 101.4 | 3% | 4x | casual 25, sexy 24, angry 13 |
| `in the` | 357 | 377.0 | 336.9 | 5% | 1x | casual 169, angry 69, lazy 68 |
| `before the` | 100 | 105.6 | 60.2 | 3% | 3x | angry 33, casual 26, sexy 21 |

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
| `did they say` | 3 | 8 | 12.3 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `an hour of` | 3 | 13 | 12.1 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 13 | 11.6 | casual 8, sexy 3, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `fell asleep` | 2 | 9 | 11.5 | casual 4, lazy 4, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.0 | sexy 8, lazy 1 |
| `a couple of` | 3 | 12 | 10.9 | casual 11, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `it a` | 4 | casual 34, lazy 4, angry 2, sexy 1 |
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 12 |
| `a couple of` | 2 | casual 11, angry 1 |
| `was it` | 3 | casual 65, sexy 11, angry 4 |
| `the walk` | 4 | casual 7, lazy 4, sexy 2, angry 1 |
| `is fine` | 3 | casual 8, lazy 5, angry 1 |
| `worth every` | 3 | sexy 9, casual 4, lazy 4 |
| `on the` | 4 | casual 151, sexy 57, lazy 51, angry 50 |
| `a real` | 3 | casual 82, angry 13, lazy 10 |
| `get a` | 3 | casual 15, sexy 4, lazy 3 |
| `a phone` | 4 | angry 10, casual 6, lazy 5, sexy 2 |
| `the night` | 4 | lazy 9, casual 7, sexy 6, angry 5 |
| `is worth` | 4 | casual 23, angry 5, lazy 5, sexy 1 |
| `the next` | 4 | casual 17, lazy 8, sexy 6, angry 4 |
| `with no` | 4 | angry 33, sexy 3, lazy 2, casual 1 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `a whole` | 4 | angry 20, lazy 16, casual 11, sexy 1 |
| `does it` | 4 | casual 44, lazy 5, angry 4, sexy 3 |
| `for the` | 4 | casual 135, angry 64, sexy 41, lazy 24 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |
| `out of` | 4 | casual 34, angry 15, lazy 14, sexy 3 |
| `from the` | 4 | casual 25, sexy 24, angry 13, lazy 12 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 51 |
| `before the` | 4 | angry 33, casual 26, sexy 21, lazy 20 |

## 4. Opener maps

- assistant pos 0 (n=9470): a 8.7%, the 4.0%, did 2.3%, how 2.2%, was 1.8%, that 1.8%
- assistant pos 1 (n=9470): the 11.3%, a 2.3%, you 1.9%, is 1.8%, does 1.2%, your 1.1%
- assistant pos 2 (n=9469): the 6.7%, a 3.0%, is 2.7%, are 1.8%, for 1.7%, of 1.7%
- assistant pos last (n=9470): it 4.1%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9470): the 13.9%, my 10.2%, our 8.2%, i 6.4%, we 5.0%, you 4.1%
- user pos 1 (n=9407): the 3.4%, you 2.4%, a 2.0%, was 1.2%, got 1.1%, did 1.1%
- user pos 2 (n=9318): the 7.3%, a 3.1%, is 1.8%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9470): again 2.4%, it 2.0%, now 1.4%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.7%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1273 |
| lazy | 1 / 2155 |

