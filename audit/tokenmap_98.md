# synth2 token-attractor map

Generated 2026-10-25 13:42  |  corpus 9525 rows, **12004 assistant turns**, 12004 user turns
Probe: `probe_out98_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T11:06:26

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.8% | 7.0% | +0.1 |
| `the`-opener (user) | 14.9% | 14.9% | +0.0 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i got` | - | 5% | - | 43x |
| `got the` | - | 5% | - | 19x |
| `did you` | - | 8% | - | 4x |
| `a long` | - | 5% | - | 18x |
| `the morning` | - | 5% | - | 15x |
| `luck with` | - | 3% | - | 50x |
| `good the` | - | 3% | - | 50x |
| `is in` | - | 3% | - | 33x |
| `you at` | - | 3% | - | 27x |
| `do you` | - | 5% | - | 5x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 7.0% | < 12% |
| `the`-opener (user) | 14.9% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `i got` | 14 | 11.7 | 43.3 | 5% | 43x | casual 12, lazy 1, sexy 1 |
| `got the` | 31 | 25.8 | 40.8 | 5% | 19x | casual 27, lazy 2, formal 1 |
| `did you` | 281 | 234.1 | 204.9 | 8% | 4x | casual 187, sexy 57, angry 28 |
| `a long` | 34 | 28.3 | 7.5 | 5% | 18x | casual 21, lazy 8, angry 3 |
| `the morning` | 41 | 34.2 | 25.8 | 5% | 15x | casual 18, lazy 11, angry 5 |
| `luck with` | 8 | 6.7 | 2.5 | 3% | 50x | casual 8 |
| `good the` | 8 | 6.7 | 0.0 | 3% | 50x | casual 8 |
| `is in` | 12 | 10.0 | 8.3 | 3% | 33x | casual 6, lazy 3, formal 2 |
| `you at` | 15 | 12.5 | 5.0 | 3% | 27x | casual 9, sexy 4, angry 2 |
| `do you` | 110 | 91.6 | 44.2 | 5% | 5x | casual 73, angry 25, sexy 8 |
| `too much` | 22 | 18.3 | 6.7 | 3% | 18x | casual 9, lazy 9, sexy 2 |
| `you do` | 23 | 19.2 | 12.5 | 3% | 17x | casual 18, angry 3, sexy 2 |
| `got a` | 23 | 19.2 | 75.8 | 3% | 17x | casual 17, sexy 3, angry 2 |
| `it is` | 141 | 117.5 | 51.6 | 5% | 4x | casual 82, lazy 36, angry 10 |
| `if the` | 29 | 24.2 | 5.0 | 3% | 14x | casual 18, angry 5, formal 3 |
| `just the` | 30 | 25.0 | 10.8 | 3% | 13x | casual 19, lazy 6, angry 3 |
| `every time` | 36 | 30.0 | 24.2 | 3% | 11x | casual 15, lazy 7, angry 5 |
| `the whole` | 190 | 158.3 | 109.1 | 5% | 3x | lazy 83, casual 57, angry 32 |
| `is just` | 37 | 30.8 | 2.5 | 3% | 11x | lazy 20, angry 11, casual 6 |
| `a day` | 42 | 35.0 | 24.2 | 3% | 10x | casual 21, lazy 11, angry 5 |
| `the end` | 49 | 40.8 | 30.0 | 3% | 8x | casual 24, angry 10, lazy 7 |
| `more than` | 51 | 42.5 | 34.2 | 3% | 8x | casual 18, lazy 11, sexy 11 |
| `the office` | 54 | 45.0 | 45.8 | 3% | 7x | formal 27, casual 14, angry 8 |
| `a good` | 67 | 55.8 | 11.7 | 3% | 6x | casual 50, lazy 12, sexy 3 |
| `for the` | 319 | 265.7 | 293.2 | 5% | 2x | casual 120, sexy 70, angry 61 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `shall i add` | 3 | 8 | 17.1 | formal 8 |
| `are you going to` | 4 | 10 | 17.0 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.3 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 15.9 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.1 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the office manager` | 3 | 9 | 12.5 | formal 9 |
| `i have been` | 3 | 10 | 12.5 | casual 8, lazy 2 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `the front desk` | 3 | 14 | 12.0 | angry 8, lazy 4, casual 1 |
| `sounds like a` | 3 | 15 | 12.0 | casual 7, formal 6, angry 1 |
| `have you got` | 3 | 15 | 11.8 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.6 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.3 | casual 9, angry 3, formal 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i got` | 3 | casual 12, lazy 1, sexy 1 |
| `got the` | 4 | casual 27, lazy 2, formal 1, sexy 1 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `a long` | 4 | casual 21, lazy 8, angry 3, formal 2 |
| `the morning` | 5 | casual 18, lazy 11, angry 5, formal 5 |
| `luck with` | 1 | casual 8 |
| `good the` | 1 | casual 8 |
| `is in` | 4 | casual 6, lazy 3, formal 2, angry 1 |
| `you at` | 3 | casual 9, sexy 4, angry 2 |
| `do you` | 5 | casual 73, angry 25, sexy 8, formal 3 |
| `too much` | 5 | casual 9, lazy 9, sexy 2, angry 1 |
| `you do` | 3 | casual 18, angry 3, sexy 2 |
| `got a` | 4 | casual 17, sexy 3, angry 2, lazy 1 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 9 |
| `if the` | 4 | casual 18, angry 5, formal 3, lazy 3 |
| `just the` | 4 | casual 19, lazy 6, angry 3, formal 2 |
| `every time` | 5 | casual 15, lazy 7, angry 5, formal 5 |
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |
| `is just` | 3 | lazy 20, angry 11, casual 6 |
| `a day` | 4 | casual 21, lazy 11, angry 5, formal 5 |
| `the end` | 5 | casual 24, angry 10, lazy 7, sexy 6 |
| `more than` | 5 | casual 18, lazy 11, sexy 11, formal 8 |
| `the office` | 5 | formal 27, casual 14, angry 8, sexy 3 |
| `a good` | 4 | casual 50, lazy 12, sexy 3, formal 2 |
| `for the` | 5 | casual 120, sexy 70, angry 61, formal 44 |

## 4. Opener maps

- assistant pos 0 (n=12004): a 10.0%, the 7.0%, does 2.7%, how 2.3%, did 2.2%, why 1.9%
- assistant pos 1 (n=12004): the 11.3%, a 2.1%, is 1.7%, does 1.6%, you 1.5%, on 0.9%
- assistant pos 2 (n=12003): the 7.3%, a 2.9%, is 2.5%, on 1.9%, of 1.9%, for 1.8%
- assistant pos last (n=12004): it 3.9%, now 1.4%, you 1.2%, time 1.1%, one 1.0%, again 0.9%
- user pos 0 (n=12004): the 14.9%, my 9.4%, our 9.1%, i 6.6%, we 5.8%, you 5.0%
- user pos 1 (n=11941): the 3.3%, you 2.0%, a 1.5%, is 1.2%, got 1.0%, was 0.9%
- user pos 2 (n=11851): the 8.2%, a 3.8%, is 1.6%, my 1.3%, in 1.2%, you 1.2%
- user pos last (n=12004): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.0%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **6.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

