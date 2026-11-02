# synth2 token-attractor map

Generated 2026-10-17 12:55  |  corpus 6188 rows, **8398 assistant turns**, 8398 user turns
Probe: `probe_out45_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-17T08:40:50

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.0% | 3.0% | +0.0 |
| `the`-opener (user) | 13.1% | 13.2% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | - | 8% | - | 17x |
| `has been` | - | 5% | - | 35x |
| `is usually` | - | 5% | - | 26x |
| `bit of` | - | 5% | - | 25x |
| `did you` | - | 8% | - | 3x |
| `did it` | - | 5% | - | 10x |
| `i've got` | - | 3% | - | 35x |
| `good one` | - | 3% | - | 35x |
| `been a` | - | 3% | - | 35x |
| `you get` | - | 5% | - | 7x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.0% | < 12% |
| `the`-opener (user) | 13.2% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 38 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a bit` | 40 | 47.6 | 38.1 | 8% | 17x | casual 38, angry 1, lazy 1 |
| `has been` | 12 | 14.3 | 75.0 | 5% | 35x | casual 10, lazy 2 |
| `is usually` | 16 | 19.1 | 0.0 | 5% | 26x | casual 12, lazy 4 |
| `bit of` | 17 | 20.2 | 10.7 | 5% | 25x | casual 16, angry 1 |
| `did you` | 230 | 273.9 | 294.1 | 8% | 3x | casual 192, angry 28, lazy 5 |
| `did it` | 40 | 47.6 | 15.5 | 5% | 10x | casual 34, lazy 4, angry 2 |
| `i've got` | 8 | 9.5 | 13.1 | 3% | 35x | casual 8 |
| `good one` | 8 | 9.5 | 3.6 | 3% | 35x | casual 7, lazy 1 |
| `been a` | 8 | 9.5 | 4.8 | 3% | 35x | casual 7, angry 1 |
| `you get` | 59 | 70.3 | 60.7 | 5% | 7x | casual 49, angry 5, lazy 5 |
| `i am` | 59 | 70.3 | 42.9 | 5% | 7x | casual 44, lazy 11, sexy 3 |
| `it will` | 10 | 11.9 | 3.6 | 3% | 28x | casual 10 |
| `in my` | 11 | 13.1 | 38.1 | 3% | 25x | lazy 6, casual 3, angry 1 |
| `will not` | 12 | 14.3 | 17.9 | 3% | 23x | casual 6, lazy 5, angry 1 |
| `is one` | 12 | 14.3 | 7.1 | 3% | 23x | lazy 7, casual 3, angry 2 |
| `for that` | 12 | 14.3 | 2.4 | 3% | 23x | casual 7, angry 4, lazy 1 |
| `i've been` | 14 | 16.7 | 20.2 | 3% | 20x | casual 14 |
| `get it` | 15 | 17.9 | 2.4 | 3% | 19x | casual 11, lazy 3, angry 1 |
| `down the` | 15 | 17.9 | 10.7 | 3% | 19x | casual 10, lazy 5 |
| `the same` | 102 | 121.5 | 102.4 | 5% | 4x | angry 36, casual 36, lazy 29 |
| `the store` | 20 | 23.8 | 13.1 | 3% | 14x | angry 13, lazy 7 |
| `all the` | 20 | 23.8 | 8.3 | 3% | 14x | casual 10, angry 8, lazy 2 |
| `the time` | 21 | 25.0 | 6.0 | 3% | 13x | casual 11, lazy 6, angry 4 |
| `a walk` | 21 | 25.0 | 14.3 | 3% | 13x | casual 16, angry 2, lazy 2 |
| `that is` | 121 | 144.1 | 15.5 | 5% | 3x | casual 76, lazy 26, angry 15 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.3 | casual 10, lazy 1 |
| `at this point` | 3 | 11 | 13.9 | lazy 5, casual 4, angry 1 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 11 | 12.1 | angry 6, casual 2, lazy 2 |
| `fell asleep` | 2 | 8 | 11.9 | casual 4, lazy 4 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 11 | 11.7 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.6 | casual 5, lazy 2, angry 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `a couple of` | 3 | 12 | 11.4 | casual 11, angry 1 |
| `feel like a` | 3 | 10 | 11.3 | lazy 6, casual 3, sexy 1 |
| `has it been` | 3 | 8 | 11.1 | casual 8 |
| `how long did` | 3 | 12 | 11.1 | casual 9, angry 3 |
| `did you find` | 3 | 9 | 10.9 | casual 9 |
| `did you get` | 3 | 44 | 10.8 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.6 | casual 7, lazy 1 |
| `why would a` | 3 | 8 | 10.5 | angry 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `has been` | 2 | casual 10, lazy 2 |
| `is usually` | 2 | casual 12, lazy 4 |
| `bit of` | 2 | casual 16, angry 1 |
| `did you` | 4 | casual 192, angry 28, lazy 5, sexy 5 |
| `did it` | 3 | casual 34, lazy 4, angry 2 |
| `i've got` | 1 | casual 8 |
| `good one` | 2 | casual 7, lazy 1 |
| `been a` | 2 | casual 7, angry 1 |
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `i am` | 4 | casual 44, lazy 11, sexy 3, angry 1 |
| `it will` | 1 | casual 10 |
| `in my` | 4 | lazy 6, casual 3, angry 1, sexy 1 |
| `will not` | 3 | casual 6, lazy 5, angry 1 |
| `is one` | 3 | lazy 7, casual 3, angry 2 |
| `for that` | 3 | casual 7, angry 4, lazy 1 |
| `i've been` | 1 | casual 14 |
| `get it` | 3 | casual 11, lazy 3, angry 1 |
| `down the` | 2 | casual 10, lazy 5 |
| `the same` | 4 | angry 36, casual 36, lazy 29, sexy 1 |
| `the store` | 2 | angry 13, lazy 7 |
| `all the` | 3 | casual 10, angry 8, lazy 2 |
| `the time` | 3 | casual 11, lazy 6, angry 4 |
| `a walk` | 4 | casual 16, angry 2, lazy 2, sexy 1 |
| `that is` | 4 | casual 76, lazy 26, angry 15, sexy 4 |

## 4. Opener maps

- assistant pos 0 (n=8398): a 8.0%, the 3.0%, did 2.6%, how 2.5%, was 2.1%, that 2.0%
- assistant pos 1 (n=8398): the 11.8%, a 2.4%, is 2.1%, you 2.0%, does 1.4%, your 1.0%
- assistant pos 2 (n=8397): the 6.2%, a 3.1%, is 3.1%, are 2.0%, of 1.7%, for 1.6%
- assistant pos last (n=8398): it 4.2%, now 1.4%, time 1.3%, you 1.1%, one 1.0%, again 1.0%
- user pos 0 (n=8398): the 13.2%, my 10.7%, our 8.2%, i 6.8%, they 3.3%, did 3.1%
- user pos 1 (n=8335): the 3.8%, you 2.7%, a 2.2%, was 1.3%, did 1.2%, is 1.1%
- user pos 2 (n=8246): the 6.8%, a 2.9%, is 2.0%, you 1.6%, my 1.4%, and 1.4%
- user pos last (n=8398): again 2.6%, it 2.0%, now 1.5%, week 1.4%, night 1.3%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.3%**; model outputs: **15.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 4 / 201 |
| lazy | 1 / 2155 |

