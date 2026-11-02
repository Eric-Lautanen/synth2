# synth2 token-attractor map

Generated 2026-10-18 19:08  |  corpus 6808 rows, **9068 assistant turns**, 9068 user turns
Probe: `probe_out55_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T15:34:26

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.7% | 3.7% | +0.0 |
| `the`-opener (user) | 13.9% | 14.0% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `same as` | - | 5% | - | 50x |
| `do not` | - | 5% | - | 16x |
| `it a` | - | 5% | - | 11x |
| `was fine` | - | 3% | - | 38x |
| `a good` | - | 5% | - | 8x |
| `day and` | - | 3% | - | 34x |
| `are a` | - | 5% | - | 7x |
| `is always the` | - | 3% | - | 30x |
| `first try` | - | 3% | - | 30x |
| `the apartment` | - | 3% | - | 25x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.7% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 31 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `same as` | 9 | 9.9 | 2.2 | 5% | 50x | casual 8, lazy 1 |
| `do not` | 28 | 30.9 | 6.6 | 5% | 16x | casual 13, lazy 12, angry 3 |
| `it a` | 41 | 45.2 | 9.9 | 5% | 11x | casual 34, lazy 4, angry 2 |
| `was fine` | 8 | 8.8 | 4.4 | 3% | 38x | casual 6, lazy 2 |
| `a good` | 57 | 62.9 | 15.4 | 5% | 8x | casual 43, lazy 12, sexy 2 |
| `day and` | 9 | 9.9 | 3.3 | 3% | 34x | casual 6, lazy 2, angry 1 |
| `are a` | 62 | 68.4 | 7.7 | 5% | 7x | lazy 45, angry 11, casual 6 |
| `is always the` | 10 | 11.0 | 0.0 | 3% | 30x | casual 8, lazy 2 |
| `first try` | 10 | 11.0 | 8.8 | 3% | 30x | lazy 7, sexy 2, casual 1 |
| `the apartment` | 12 | 13.2 | 15.4 | 3% | 25x | casual 8, sexy 3, lazy 1 |
| `phone call` | 12 | 13.2 | 5.5 | 3% | 25x | casual 7, lazy 4, angry 1 |
| `give it` | 16 | 17.6 | 4.4 | 3% | 19x | casual 14, lazy 1, sexy 1 |
| `are they` | 16 | 17.6 | 3.3 | 3% | 19x | casual 14, angry 2 |
| `on my` | 19 | 21.0 | 47.4 | 3% | 16x | casual 7, sexy 7, lazy 5 |
| `a phone` | 22 | 24.3 | 11.0 | 3% | 14x | angry 10, casual 6, lazy 5 |
| `part of` | 26 | 28.7 | 4.4 | 3% | 12x | lazy 13, casual 11, sexy 2 |
| `a long` | 32 | 35.3 | 7.7 | 3% | 9x | casual 21, lazy 8, angry 3 |
| `the good` | 42 | 46.3 | 18.7 | 3% | 7x | lazy 26, casual 14, angry 1 |
| `did you get` | 44 | 48.5 | 46.3 | 3% | 7x | casual 40, angry 2, lazy 2 |
| `the day` | 46 | 50.7 | 22.1 | 3% | 7x | lazy 22, casual 17, angry 4 |
| `the worst` | 50 | 55.1 | 8.8 | 3% | 6x | casual 26, lazy 17, angry 6 |
| `this time` | 51 | 56.2 | 17.6 | 3% | 6x | casual 42, angry 6, lazy 2 |
| `or just` | 51 | 56.2 | 3.3 | 3% | 6x | casual 36, angry 9, sexy 6 |
| `the new` | 60 | 66.2 | 78.3 | 3% | 5x | casual 35, angry 12, lazy 11 |
| `a week` | 70 | 77.2 | 58.4 | 3% | 4x | casual 36, lazy 22, angry 10 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `on the first try` | 4 | 8 | 16.6 | lazy 5, sexy 2, casual 1 |
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.1 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.9 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `fell asleep` | 2 | 8 | 11.7 | casual 4, lazy 4 |
| `for an hour` | 3 | 12 | 11.6 | casual 8, sexy 2, angry 1 |
| `ice cream` | 2 | 8 | 11.6 | lazy 6, casual 1, sexy 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `has it been` | 3 | 8 | 11.3 | casual 8 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `a couple of` | 3 | 12 | 11.0 | casual 11, angry 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `same as` | 2 | casual 8, lazy 1 |
| `do not` | 3 | casual 13, lazy 12, angry 3 |
| `it a` | 4 | casual 34, lazy 4, angry 2, sexy 1 |
| `was fine` | 2 | casual 6, lazy 2 |
| `a good` | 3 | casual 43, lazy 12, sexy 2 |
| `day and` | 3 | casual 6, lazy 2, angry 1 |
| `are a` | 3 | lazy 45, angry 11, casual 6 |
| `is always the` | 2 | casual 8, lazy 2 |
| `first try` | 3 | lazy 7, sexy 2, casual 1 |
| `the apartment` | 3 | casual 8, sexy 3, lazy 1 |
| `phone call` | 3 | casual 7, lazy 4, angry 1 |
| `give it` | 3 | casual 14, lazy 1, sexy 1 |
| `are they` | 2 | casual 14, angry 2 |
| `on my` | 3 | casual 7, sexy 7, lazy 5 |
| `a phone` | 4 | angry 10, casual 6, lazy 5, sexy 1 |
| `part of` | 3 | lazy 13, casual 11, sexy 2 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `the good` | 4 | lazy 26, casual 14, angry 1, sexy 1 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `the day` | 4 | lazy 22, casual 17, angry 4, sexy 3 |
| `the worst` | 4 | casual 26, lazy 17, angry 6, sexy 1 |
| `this time` | 4 | casual 42, angry 6, lazy 2, sexy 1 |
| `or just` | 3 | casual 36, angry 9, sexy 6 |
| `the new` | 4 | casual 35, angry 12, lazy 11, sexy 2 |
| `a week` | 4 | casual 36, lazy 22, angry 10, sexy 2 |

## 4. Opener maps

- assistant pos 0 (n=9068): a 8.1%, the 3.7%, did 2.4%, how 2.3%, was 1.9%, that 1.9%
- assistant pos 1 (n=9068): the 11.6%, a 2.3%, you 2.0%, is 1.9%, does 1.3%, your 1.1%
- assistant pos 2 (n=9067): the 6.3%, a 3.0%, is 2.9%, are 1.9%, for 1.7%, of 1.7%
- assistant pos last (n=9068): it 4.0%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9068): the 14.0%, my 10.3%, our 8.1%, i 6.7%, we 4.4%, you 3.3%
- user pos 1 (n=9005): the 3.6%, you 2.5%, a 2.0%, was 1.2%, did 1.1%, is 1.0%
- user pos 2 (n=8916): the 7.1%, a 2.9%, is 1.9%, you 1.6%, my 1.5%, and 1.3%
- user pos last (n=9068): again 2.5%, it 2.0%, now 1.4%, week 1.3%, night 1.3%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.9%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 871 |
| lazy | 1 / 2155 |

