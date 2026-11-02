# synth2 token-attractor map

Generated 2026-10-19 07:41  |  corpus 7118 rows, **9403 assistant turns**, 9403 user turns
Probe: `probe_out60_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-19T05:33:03

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.9% | 3.9% | +0.1 |
| `the`-opener (user) | 14.0% | 14.0% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the one` | - | 7% | - | 10x |
| `worth the` | - | 5% | - | 12x |
| `the whole` | - | 7% | - | 4x |
| `is the` | 7% | 8% | 1x | 2x |
| `and i` | - | 5% | - | 8x |
| `one you` | - | 3% | - | 28x |
| `was not` | - | 3% | - | 26x |
| `no idea` | - | 3% | - | 26x |
| `first time` | - | 3% | - | 24x |
| `i've been` | - | 3% | - | 22x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.9% | < 12% |
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
| `the one` | 65 | 69.1 | 23.4 | 7% | 10x | lazy 34, casual 23, angry 6 |
| `worth the` | 40 | 42.5 | 8.5 | 5% | 12x | casual 21, lazy 13, sexy 6 |
| `the whole` | 177 | 188.2 | 126.6 | 7% | 4x | lazy 83, casual 55, angry 32 |
| `is the` | 425 | 452.0 | 73.4 | 8% | 2x | casual 250, lazy 116, angry 49 |
| `and i` | 60 | 63.8 | 93.6 | 5% | 8x | casual 29, lazy 25, sexy 6 |
| `one you` | 11 | 11.7 | 1.1 | 3% | 28x | casual 9, lazy 2 |
| `was not` | 12 | 12.8 | 5.3 | 3% | 26x | casual 7, sexy 3, angry 1 |
| `no idea` | 12 | 12.8 | 8.5 | 3% | 26x | casual 10, lazy 2 |
| `first time` | 13 | 13.8 | 39.3 | 3% | 24x | casual 11, lazy 2 |
| `i've been` | 14 | 14.9 | 18.1 | 3% | 22x | casual 14 |
| `one is` | 19 | 20.2 | 10.6 | 3% | 16x | casual 13, lazy 4, sexy 2 |
| `is it` | 111 | 118.0 | 23.4 | 5% | 4x | casual 100, angry 7, sexy 4 |
| `too much` | 21 | 22.3 | 8.5 | 3% | 15x | casual 9, lazy 9, sexy 2 |
| `to do` | 25 | 26.6 | 24.5 | 3% | 13x | casual 21, angry 2, lazy 1 |
| `that is` | 141 | 150.0 | 13.8 | 5% | 3x | casual 76, lazy 26, sexy 24 |
| `you have` | 29 | 30.8 | 16.0 | 3% | 11x | casual 20, lazy 5, angry 2 |
| `just a` | 33 | 35.1 | 21.3 | 3% | 9x | casual 22, angry 7, lazy 4 |
| `way to` | 36 | 38.3 | 3.2 | 3% | 9x | casual 17, angry 11, lazy 6 |
| `the good` | 42 | 44.7 | 18.1 | 3% | 7x | lazy 26, casual 14, angry 1 |
| `it the` | 42 | 44.7 | 12.8 | 3% | 7x | casual 34, lazy 4, sexy 3 |
| `a good` | 58 | 61.7 | 14.9 | 3% | 5x | casual 43, lazy 12, sexy 3 |
| `i am` | 66 | 70.2 | 38.3 | 3% | 5x | casual 44, lazy 11, sexy 10 |
| `and the` | 71 | 75.5 | 151.0 | 3% | 4x | casual 38, lazy 15, angry 12 |
| `in the` | 354 | 376.5 | 338.2 | 5% | 1x | casual 169, angry 69, lazy 68 |
| `an hour` | 79 | 84.0 | 87.2 | 3% | 4x | casual 34, sexy 17, lazy 16 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `on the first try` | 4 | 8 | 16.5 | lazy 5, sexy 2, casual 1 |
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.1 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `was it worth the` | 4 | 8 | 13.0 | casual 7, sexy 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.3 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 13 | 12.1 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `fell asleep` | 2 | 9 | 11.5 | casual 4, lazy 4, sexy 1 |
| `for an hour` | 3 | 12 | 11.5 | casual 8, sexy 2, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `ice cream` | 2 | 9 | 11.5 | lazy 6, sexy 2, casual 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.0 | sexy 8, lazy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |
| `a couple of` | 3 | 12 | 10.9 | casual 11, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the one` | 4 | lazy 34, casual 23, angry 6, sexy 2 |
| `worth the` | 3 | casual 21, lazy 13, sexy 6 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 7 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 10 |
| `and i` | 3 | casual 29, lazy 25, sexy 6 |
| `one you` | 2 | casual 9, lazy 2 |
| `was not` | 4 | casual 7, sexy 3, angry 1, lazy 1 |
| `no idea` | 2 | casual 10, lazy 2 |
| `first time` | 2 | casual 11, lazy 2 |
| `i've been` | 1 | casual 14 |
| `one is` | 3 | casual 13, lazy 4, sexy 2 |
| `is it` | 3 | casual 100, angry 7, sexy 4 |
| `too much` | 4 | casual 9, lazy 9, sexy 2, angry 1 |
| `to do` | 4 | casual 21, angry 2, lazy 1, sexy 1 |
| `that is` | 4 | casual 76, lazy 26, sexy 24, angry 15 |
| `you have` | 4 | casual 20, lazy 5, angry 2, sexy 2 |
| `just a` | 3 | casual 22, angry 7, lazy 4 |
| `way to` | 4 | casual 17, angry 11, lazy 6, sexy 2 |
| `the good` | 4 | lazy 26, casual 14, angry 1, sexy 1 |
| `it the` | 4 | casual 34, lazy 4, sexy 3, angry 1 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |
| `i am` | 4 | casual 44, lazy 11, sexy 10, angry 1 |
| `and the` | 4 | casual 38, lazy 15, angry 12, sexy 6 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 48 |
| `an hour` | 4 | casual 34, sexy 17, lazy 16, angry 12 |

## 4. Opener maps

- assistant pos 0 (n=9403): a 8.6%, the 3.9%, did 2.3%, how 2.2%, was 1.8%, that 1.8%
- assistant pos 1 (n=9403): the 11.4%, a 2.3%, you 1.9%, is 1.9%, does 1.2%, your 1.1%
- assistant pos 2 (n=9402): the 6.6%, a 3.0%, is 2.8%, are 1.8%, for 1.7%, of 1.7%
- assistant pos last (n=9403): it 4.1%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9403): the 14.0%, my 10.2%, our 8.2%, i 6.5%, we 4.9%, you 4.0%
- user pos 1 (n=9340): the 3.5%, you 2.5%, a 2.0%, was 1.2%, got 1.1%, did 1.1%
- user pos 2 (n=9251): the 7.2%, a 3.1%, is 1.8%, you 1.6%, my 1.4%, was 1.3%
- user pos last (n=9403): again 2.4%, it 2.0%, now 1.4%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.7%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1206 |
| lazy | 1 / 2155 |

