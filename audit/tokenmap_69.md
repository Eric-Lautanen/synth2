# synth2 token-attractor map

Generated 2026-10-21 01:19  |  corpus 7676 rows, **10006 assistant turns**, 10006 user turns
Probe: `probe_out69_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-20T21:57:41

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.3% | 4.3% | +0.1 |
| `the`-opener (user) | 13.9% | 13.8% | -0.1 |
| copula-only | 0.5% | 0.5% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `is a` | 5% | 10% | 1x | 2x |
| `just the` | - | 5% | - | 18x |
| `is it` | 3% | 7% | 3x | 6x |
| `or just` | - | 5% | - | 9x |
| `luck with` | - | 3% | - | 42x |
| `i've got` | - | 3% | - | 42x |
| `good luck` | - | 3% | - | 28x |
| `for two` | - | 3% | - | 21x |
| `get it` | - | 3% | - | 20x |
| `then the` | - | 3% | - | 16x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.3% | < 12% |
| `the`-opener (user) | 13.8% | n/a |
| copula-only turns | 0.5% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 42 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `is a` | 458 | 457.7 | 60.0 | 10% | 2x | angry 208, casual 120, lazy 115 |
| `just the` | 28 | 28.0 | 11.0 | 5% | 18x | casual 19, lazy 6, angry 3 |
| `is it` | 111 | 110.9 | 22.0 | 7% | 6x | casual 100, angry 7, sexy 4 |
| `or just` | 53 | 53.0 | 3.0 | 5% | 9x | casual 36, angry 9, sexy 8 |
| `luck with` | 8 | 8.0 | 3.0 | 3% | 42x | casual 8 |
| `i've got` | 8 | 8.0 | 11.0 | 3% | 42x | casual 8 |
| `good luck` | 12 | 12.0 | 0.0 | 3% | 28x | casual 9, lazy 2, angry 1 |
| `for two` | 16 | 16.0 | 36.0 | 3% | 21x | angry 5, casual 5, sexy 4 |
| `get it` | 17 | 17.0 | 2.0 | 3% | 20x | casual 11, lazy 3, sexy 2 |
| `then the` | 21 | 21.0 | 10.0 | 3% | 16x | casual 15, lazy 5, sexy 1 |
| `in the` | 368 | 367.8 | 335.8 | 7% | 2x | casual 169, angry 69, lazy 68 |
| `it is` | 126 | 125.9 | 53.0 | 5% | 4x | casual 79, lazy 36, angry 7 |
| `a two` | 23 | 23.0 | 14.0 | 3% | 15x | angry 8, casual 8, lazy 4 |
| `two hours` | 27 | 27.0 | 32.0 | 3% | 12x | angry 12, casual 7, lazy 5 |
| `i keep` | 27 | 27.0 | 30.0 | 3% | 12x | casual 17, lazy 6, sexy 4 |
| `going to` | 30 | 30.0 | 14.0 | 3% | 11x | casual 18, angry 6, lazy 5 |
| `a long` | 32 | 32.0 | 7.0 | 3% | 10x | casual 21, lazy 8, angry 3 |
| `the way` | 33 | 33.0 | 24.0 | 3% | 10x | casual 21, sexy 7, lazy 4 |
| `a day` | 35 | 35.0 | 20.0 | 3% | 10x | casual 19, lazy 11, angry 5 |
| `and then` | 38 | 38.0 | 22.0 | 3% | 9x | casual 15, angry 13, lazy 8 |
| `a bit` | 40 | 40.0 | 32.0 | 3% | 8x | casual 38, angry 1, lazy 1 |
| `did it` | 43 | 43.0 | 13.0 | 3% | 8x | casual 34, lazy 4, sexy 3 |
| `the car` | 50 | 50.0 | 44.0 | 3% | 7x | casual 27, sexy 13, lazy 9 |
| `i will` | 55 | 55.0 | 8.0 | 3% | 6x | casual 31, lazy 14, sexy 10 |
| `a good` | 58 | 58.0 | 14.0 | 3% | 6x | casual 43, lazy 12, sexy 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `an early night` | 3 | 11 | 14.0 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 12.9 | casual 7, sexy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `ten minutes of` | 3 | 11 | 12.7 | sexy 8, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `in ten minutes` | 3 | 8 | 12.0 | casual 5, sexy 3 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
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
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 15 |
| `just the` | 3 | casual 19, lazy 6, angry 3 |
| `is it` | 3 | casual 100, angry 7, sexy 4 |
| `or just` | 3 | casual 36, angry 9, sexy 8 |
| `luck with` | 1 | casual 8 |
| `i've got` | 1 | casual 8 |
| `good luck` | 3 | casual 9, lazy 2, angry 1 |
| `for two` | 4 | angry 5, casual 5, sexy 4, lazy 2 |
| `get it` | 4 | casual 11, lazy 3, sexy 2, angry 1 |
| `then the` | 3 | casual 15, lazy 5, sexy 1 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 62 |
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 4 |
| `a two` | 4 | angry 8, casual 8, lazy 4, sexy 3 |
| `two hours` | 4 | angry 12, casual 7, lazy 5, sexy 3 |
| `i keep` | 3 | casual 17, lazy 6, sexy 4 |
| `going to` | 4 | casual 18, angry 6, lazy 5, sexy 1 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `the way` | 4 | casual 21, sexy 7, lazy 4, angry 1 |
| `a day` | 3 | casual 19, lazy 11, angry 5 |
| `and then` | 4 | casual 15, angry 13, lazy 8, sexy 2 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `did it` | 4 | casual 34, lazy 4, sexy 3, angry 2 |
| `the car` | 4 | casual 27, sexy 13, lazy 9, angry 1 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |

## 4. Opener maps

- assistant pos 0 (n=10006): a 9.4%, the 4.3%, did 2.2%, how 2.1%, was 1.7%, that 1.7%
- assistant pos 1 (n=10006): the 10.8%, a 2.2%, you 1.8%, is 1.7%, does 1.2%, your 1.0%
- assistant pos 2 (n=10005): the 6.8%, a 2.9%, is 2.6%, of 1.9%, for 1.8%, on 1.8%
- assistant pos last (n=10006): it 3.9%, now 1.6%, time 1.2%, you 1.2%, one 0.9%, again 0.9%
- user pos 0 (n=10006): the 13.8%, my 10.0%, our 8.0%, i 6.1%, we 5.6%, you 5.1%
- user pos 1 (n=9943): the 3.3%, you 2.3%, a 1.9%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=9854): the 7.6%, a 3.2%, is 1.7%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=10006): again 2.3%, it 2.0%, now 1.3%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.4%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1809 |
| lazy | 1 / 2155 |

