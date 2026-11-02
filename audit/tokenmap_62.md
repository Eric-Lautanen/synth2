# synth2 token-attractor map

Generated 2026-10-20 05:10  |  corpus 7242 rows, **9537 assistant turns**, 9537 user turns
Probe: `probe_out62_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-19T09:57:33

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.0% | 4.1% | +0.1 |
| `the`-opener (user) | 14.0% | 14.0% | +0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `is a` | 8% | 12% | 2x | 2x |
| `i have` | - | 7% | - | 12x |
| `have been` | - | 5% | - | 25x |
| `it is` | - | 7% | - | 5x |
| `a bit` | - | 5% | - | 12x |
| `the whole` | - | 7% | - | 4x |
| `just for` | - | 3% | - | 40x |
| `it still` | - | 3% | - | 40x |
| `been a` | - | 3% | - | 40x |
| `the long` | - | 3% | - | 26x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.1% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
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
| `is a` | 455 | 477.1 | 62.9 | 12% | 2x | angry 208, casual 120, lazy 115 |
| `i have` | 51 | 53.5 | 81.8 | 7% | 12x | casual 35, lazy 12, sexy 4 |
| `have been` | 19 | 19.9 | 41.9 | 5% | 25x | casual 13, lazy 4, angry 1 |
| `it is` | 126 | 132.1 | 55.6 | 7% | 5x | casual 79, lazy 36, angry 7 |
| `a bit` | 40 | 41.9 | 33.6 | 5% | 12x | casual 38, angry 1, lazy 1 |
| `the whole` | 178 | 186.6 | 126.9 | 7% | 4x | lazy 83, casual 55, angry 32 |
| `just for` | 8 | 8.4 | 3.1 | 3% | 40x | angry 3, casual 3, lazy 2 |
| `it still` | 8 | 8.4 | 3.1 | 3% | 40x | casual 5, lazy 2, angry 1 |
| `been a` | 8 | 8.4 | 5.2 | 3% | 40x | casual 7, angry 1 |
| `the long` | 12 | 12.6 | 9.4 | 3% | 26x | casual 7, lazy 3, angry 2 |
| `in my` | 14 | 14.7 | 35.7 | 3% | 23x | lazy 6, sexy 4, casual 3 |
| `bit of` | 17 | 17.8 | 9.4 | 3% | 19x | casual 16, angry 1 |
| `and a` | 101 | 105.9 | 92.3 | 5% | 5x | casual 60, lazy 32, sexy 8 |
| `a two` | 21 | 22.0 | 13.6 | 3% | 15x | angry 8, casual 8, lazy 4 |
| `i did` | 24 | 25.2 | 34.6 | 3% | 13x | casual 19, lazy 4, sexy 1 |
| `going to` | 29 | 30.4 | 14.7 | 3% | 11x | casual 18, angry 6, lazy 5 |
| `for you` | 35 | 36.7 | 6.3 | 3% | 9x | casual 12, angry 10, sexy 10 |
| `the good` | 43 | 45.1 | 17.8 | 3% | 7x | lazy 26, casual 14, sexy 2 |
| `this time` | 51 | 53.5 | 17.8 | 3% | 6x | casual 42, angry 6, lazy 2 |
| `or just` | 52 | 54.5 | 3.1 | 3% | 6x | casual 36, angry 9, sexy 7 |
| `a good` | 58 | 60.8 | 14.7 | 3% | 5x | casual 43, lazy 12, sexy 3 |
| `or the` | 60 | 62.9 | 2.1 | 3% | 5x | casual 49, angry 4, sexy 4 |
| `worth it` | 65 | 68.2 | 11.5 | 3% | 5x | casual 42, lazy 15, sexy 7 |
| `the one` | 65 | 68.2 | 24.1 | 3% | 5x | lazy 34, casual 23, angry 6 |
| `did the` | 306 | 320.9 | 73.4 | 5% | 2x | angry 130, casual 125, sexy 48 |

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
| `an hour of` | 3 | 13 | 12.1 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 13 | 11.6 | casual 8, sexy 3, angry 1 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `fell asleep` | 2 | 9 | 11.4 | casual 4, lazy 4, sexy 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |
| `falling asleep` | 2 | 9 | 10.9 | sexy 8, lazy 1 |
| `a couple of` | 3 | 12 | 10.9 | casual 11, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 12 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `have been` | 4 | casual 13, lazy 4, angry 1, sexy 1 |
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 4 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 8 |
| `just for` | 3 | angry 3, casual 3, lazy 2 |
| `it still` | 3 | casual 5, lazy 2, angry 1 |
| `been a` | 2 | casual 7, angry 1 |
| `the long` | 3 | casual 7, lazy 3, angry 2 |
| `in my` | 4 | lazy 6, sexy 4, casual 3, angry 1 |
| `bit of` | 2 | casual 16, angry 1 |
| `and a` | 4 | casual 60, lazy 32, sexy 8, angry 1 |
| `a two` | 4 | angry 8, casual 8, lazy 4, sexy 1 |
| `i did` | 3 | casual 19, lazy 4, sexy 1 |
| `going to` | 3 | casual 18, angry 6, lazy 5 |
| `for you` | 4 | casual 12, angry 10, sexy 10, lazy 3 |
| `the good` | 4 | lazy 26, casual 14, sexy 2, angry 1 |
| `this time` | 4 | casual 42, angry 6, lazy 2, sexy 1 |
| `or just` | 3 | casual 36, angry 9, sexy 7 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |
| `or the` | 4 | casual 49, angry 4, sexy 4, lazy 3 |
| `worth it` | 4 | casual 42, lazy 15, sexy 7, angry 1 |
| `the one` | 4 | lazy 34, casual 23, angry 6, sexy 2 |
| `did the` | 4 | angry 130, casual 125, sexy 48, lazy 3 |

## 4. Opener maps

- assistant pos 0 (n=9537): a 8.7%, the 4.1%, did 2.3%, how 2.2%, was 1.8%, that 1.8%
- assistant pos 1 (n=9537): the 11.2%, a 2.3%, you 1.9%, is 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=9536): the 6.7%, a 3.0%, is 2.7%, are 1.8%, of 1.8%, for 1.7%
- assistant pos last (n=9537): it 4.1%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9537): the 14.0%, my 10.2%, our 8.2%, i 6.4%, we 5.0%, you 4.2%
- user pos 1 (n=9474): the 3.4%, you 2.4%, a 1.9%, was 1.2%, got 1.1%, did 1.1%
- user pos 2 (n=9385): the 7.3%, a 3.1%, is 1.8%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9537): again 2.4%, it 2.0%, now 1.4%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.6%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1340 |
| lazy | 1 / 2155 |

