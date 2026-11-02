# synth2 token-attractor map

Generated 2026-10-20 08:02  |  corpus 7304 rows, **9604 assistant turns**, 9604 user turns
Probe: `probe_out63_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-20T05:10:01

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.1% | 4.1% | +0.1 |
| `the`-opener (user) | 14.0% | 14.0% | -0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i would` | - | 5% | - | 30x |
| `the end` | - | 5% | - | 10x |
| `it still` | 3% | 3% | 40x | 40x |
| `be a` | - | 3% | - | 40x |
| `this weekend` | - | 3% | - | 19x |
| `is the whole` | - | 3% | - | 17x |
| `is it` | - | 5% | - | 4x |
| `in the` | - | 7% | - | 2x |
| `it is` | 7% | 5% | 5x | 4x |
| `you go` | - | 3% | - | 12x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.1% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
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
| `i would` | 16 | 16.7 | 4.2 | 5% | 30x | casual 8, angry 4, lazy 2 |
| `the end` | 46 | 47.9 | 33.3 | 5% | 10x | casual 26, angry 10, lazy 7 |
| `it still` | 8 | 8.3 | 3.1 | 3% | 40x | casual 5, lazy 2, angry 1 |
| `be a` | 8 | 8.3 | 2.1 | 3% | 40x | casual 4, lazy 2, sexy 2 |
| `this weekend` | 17 | 17.7 | 30.2 | 3% | 19x | casual 14, lazy 2, sexy 1 |
| `is the whole` | 19 | 19.8 | 3.1 | 3% | 17x | casual 8, lazy 7, angry 4 |
| `is it` | 111 | 115.6 | 22.9 | 5% | 4x | casual 100, angry 7, sexy 4 |
| `in the` | 358 | 372.8 | 337.4 | 7% | 2x | casual 169, angry 69, lazy 68 |
| `it is` | 126 | 131.2 | 55.2 | 5% | 4x | casual 79, lazy 36, angry 7 |
| `you go` | 27 | 28.1 | 8.3 | 3% | 12x | casual 26, lazy 1 |
| `for it` | 35 | 36.4 | 17.7 | 3% | 9x | casual 24, lazy 7, angry 2 |
| `a bit` | 40 | 41.6 | 33.3 | 3% | 8x | casual 38, angry 1, lazy 1 |
| `the good` | 43 | 44.8 | 17.7 | 3% | 7x | lazy 26, casual 14, sexy 2 |
| `i have` | 51 | 53.1 | 81.2 | 3% | 6x | casual 35, lazy 12, sexy 4 |
| `or just` | 52 | 54.1 | 3.1 | 3% | 6x | casual 36, angry 9, sexy 7 |
| `i will` | 55 | 57.3 | 8.3 | 3% | 6x | casual 31, lazy 14, sexy 10 |
| `and i` | 60 | 62.5 | 91.6 | 3% | 5x | casual 29, lazy 25, sexy 6 |
| `i am` | 66 | 68.7 | 37.5 | 3% | 5x | casual 44, lazy 11, sexy 10 |
| `and the` | 71 | 73.9 | 153.1 | 3% | 5x | casual 38, lazy 15, angry 12 |
| `what did` | 72 | 75.0 | 42.7 | 3% | 4x | casual 41, angry 19, sexy 11 |
| `and a` | 103 | 107.2 | 91.6 | 3% | 3x | casual 60, lazy 32, sexy 10 |
| `the same` | 113 | 117.7 | 105.2 | 3% | 3x | angry 36, casual 36, lazy 29 |
| `worth it for` | 8 | 8.3 | 0.0 | 2% | 20x | casual 5, lazy 3 |
| `will never` | 8 | 8.3 | 2.1 | 2% | 20x | casual 4, lazy 3, sexy 1 |
| `the order` | 8 | 8.3 | 1.0 | 2% | 20x | angry 6, casual 1, lazy 1 |

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
| `was it worth the` | 4 | 8 | 13.0 | casual 7, sexy 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `did they say` | 3 | 8 | 12.3 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `in ten minutes` | 3 | 8 | 12.2 | casual 5, sexy 3 |
| `an hour of` | 3 | 13 | 12.1 | angry 6, sexy 3, casual 2 |
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
| `falling asleep` | 2 | 9 | 10.9 | sexy 8, lazy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i would` | 4 | casual 8, angry 4, lazy 2, sexy 2 |
| `the end` | 4 | casual 26, angry 10, lazy 7, sexy 3 |
| `it still` | 3 | casual 5, lazy 2, angry 1 |
| `be a` | 3 | casual 4, lazy 2, sexy 2 |
| `this weekend` | 3 | casual 14, lazy 2, sexy 1 |
| `is the whole` | 3 | casual 8, lazy 7, angry 4 |
| `is it` | 3 | casual 100, angry 7, sexy 4 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 52 |
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 4 |
| `you go` | 2 | casual 26, lazy 1 |
| `for it` | 4 | casual 24, lazy 7, angry 2, sexy 2 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `the good` | 4 | lazy 26, casual 14, sexy 2, angry 1 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `or just` | 3 | casual 36, angry 9, sexy 7 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `and i` | 3 | casual 29, lazy 25, sexy 6 |
| `i am` | 4 | casual 44, lazy 11, sexy 10, angry 1 |
| `and the` | 4 | casual 38, lazy 15, angry 12, sexy 6 |
| `what did` | 4 | casual 41, angry 19, sexy 11, lazy 1 |
| `and a` | 4 | casual 60, lazy 32, sexy 10, angry 1 |
| `the same` | 4 | angry 36, casual 36, lazy 29, sexy 12 |
| `worth it for` | 2 | casual 5, lazy 3 |
| `will never` | 3 | casual 4, lazy 3, sexy 1 |
| `the order` | 3 | angry 6, casual 1, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=9604): a 8.8%, the 4.1%, did 2.3%, how 2.2%, was 1.8%, that 1.8%
- assistant pos 1 (n=9604): the 11.2%, a 2.2%, you 1.9%, is 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=9603): the 6.8%, a 3.0%, is 2.7%, of 1.8%, are 1.8%, for 1.7%
- assistant pos last (n=9604): it 4.0%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9604): the 14.0%, my 10.1%, our 8.1%, i 6.3%, we 5.2%, you 4.4%
- user pos 1 (n=9541): the 3.4%, you 2.4%, a 1.9%, was 1.2%, got 1.1%, did 1.1%
- user pos 2 (n=9452): the 7.4%, a 3.1%, is 1.8%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9604): again 2.4%, it 2.0%, now 1.3%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.6%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1407 |
| lazy | 1 / 2155 |

