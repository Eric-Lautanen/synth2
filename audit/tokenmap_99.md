# synth2 token-attractor map

Generated 2026-10-25 16:11  |  corpus 9575 rows, **12058 assistant turns**, 12058 user turns
Probe: `probe_out99_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T13:42:15

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 7.0% | 7.4% | +0.4 |
| `the`-opener (user) | 14.9% | 14.9% | +0.0 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | - | 7% | - | 22x |
| `in that` | - | 5% | - | 26x |
| `it is` | 5% | 7% | 4x | 6x |
| `the rain` | - | 5% | - | 14x |
| `so the` | - | 5% | - | 13x |
| `get out` | - | 3% | - | 50x |
| `of the` | - | 7% | - | 4x |
| `off and` | - | 3% | - | 33x |
| `is in` | 3% | 3% | 33x | 33x |
| `did you` | 8% | 7% | 4x | 3x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 7.4% | < 12% |
| `the`-opener (user) | 14.9% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `a bit` | 36 | 29.9 | 26.5 | 7% | 22x | casual 34, angry 1, lazy 1 |
| `in that` | 23 | 19.1 | 4.1 | 5% | 26x | angry 7, casual 7, sexy 5 |
| `it is` | 141 | 116.9 | 51.4 | 7% | 6x | casual 82, lazy 36, angry 10 |
| `the rain` | 43 | 35.7 | 28.2 | 5% | 14x | casual 23, lazy 8, angry 6 |
| `so the` | 45 | 37.3 | 16.6 | 5% | 13x | casual 21, angry 11, formal 10 |
| `get out` | 8 | 6.6 | 5.0 | 3% | 50x | casual 5, angry 2, lazy 1 |
| `of the` | 211 | 175.0 | 141.0 | 7% | 4x | casual 80, lazy 39, sexy 35 |
| `off and` | 12 | 10.0 | 5.8 | 3% | 33x | casual 8, lazy 4 |
| `is in` | 12 | 10.0 | 8.3 | 3% | 33x | casual 6, lazy 3, formal 2 |
| `did you` | 281 | 233.0 | 204.0 | 7% | 3x | casual 187, sexy 57, angry 28 |
| `is the right` | 14 | 11.6 | 0.0 | 3% | 29x | casual 14 |
| `is one` | 14 | 11.6 | 6.6 | 3% | 29x | lazy 8, casual 3, angry 2 |
| `again is` | 15 | 12.4 | 0.0 | 3% | 27x | casual 9, angry 5, lazy 1 |
| `the job` | 16 | 13.3 | 5.0 | 3% | 25x | casual 6, angry 5, formal 3 |
| `bit of` | 16 | 13.3 | 7.5 | 3% | 25x | casual 15, angry 1 |
| `is always` | 24 | 19.9 | 12.4 | 3% | 17x | casual 15, lazy 7, angry 2 |
| `is a real` | 26 | 21.6 | 0.8 | 3% | 15x | casual 15, angry 7, lazy 4 |
| `you go` | 28 | 23.2 | 6.6 | 3% | 14x | casual 27, lazy 1 |
| `just the` | 30 | 24.9 | 10.8 | 3% | 13x | casual 19, lazy 6, angry 3 |
| `going to` | 32 | 26.5 | 11.6 | 3% | 13x | casual 18, angry 6, lazy 5 |
| `way to` | 36 | 29.9 | 2.5 | 3% | 11x | casual 17, angry 11, lazy 6 |
| `the morning` | 41 | 34.0 | 25.7 | 3% | 10x | casual 18, lazy 11, angry 5 |
| `and then` | 41 | 34.0 | 24.9 | 3% | 10x | casual 15, angry 12, lazy 8 |
| `a whole` | 49 | 40.6 | 24.9 | 3% | 8x | angry 19, lazy 16, casual 10 |
| `with no` | 56 | 46.4 | 28.2 | 3% | 7x | angry 34, sexy 11, formal 7 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 17.0 | casual 8, angry 2 |
| `shall i add` | 3 | 8 | 17.0 | formal 8 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.3 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 15.9 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.1 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `i will bring` | 3 | 9 | 13.5 | formal 4, casual 3, lazy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.6 | angry 4, casual 4 |
| `i have been` | 3 | 10 | 12.4 | casual 8, lazy 2 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `the office manager` | 3 | 9 | 12.4 | formal 9 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 15 | 12.0 | casual 7, formal 6, angry 1 |
| `the front desk` | 3 | 14 | 11.9 | angry 8, lazy 4, casual 1 |
| `have you got` | 3 | 15 | 11.8 | casual 15 |
| `without a single` | 3 | 10 | 11.7 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.4 | casual 8, sexy 3, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `in that` | 5 | angry 7, casual 7, sexy 5, formal 3 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 9 |
| `the rain` | 5 | casual 23, lazy 8, angry 6, formal 3 |
| `so the` | 4 | casual 21, angry 11, formal 10, sexy 3 |
| `get out` | 3 | casual 5, angry 2, lazy 1 |
| `of the` | 5 | casual 80, lazy 39, sexy 35, angry 31 |
| `off and` | 2 | casual 8, lazy 4 |
| `is in` | 4 | casual 6, lazy 3, formal 2, angry 1 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `is the right` | 1 | casual 14 |
| `is one` | 4 | lazy 8, casual 3, angry 2, formal 1 |
| `again is` | 3 | casual 9, angry 5, lazy 1 |
| `the job` | 5 | casual 6, angry 5, formal 3, lazy 1 |
| `bit of` | 2 | casual 15, angry 1 |
| `is always` | 3 | casual 15, lazy 7, angry 2 |
| `is a real` | 3 | casual 15, angry 7, lazy 4 |
| `you go` | 2 | casual 27, lazy 1 |
| `just the` | 4 | casual 19, lazy 6, angry 3, formal 2 |
| `going to` | 5 | casual 18, angry 6, lazy 5, sexy 2 |
| `way to` | 4 | casual 17, angry 11, lazy 6, sexy 2 |
| `the morning` | 5 | casual 18, lazy 11, angry 5, formal 5 |
| `and then` | 5 | casual 15, angry 12, lazy 8, formal 4 |
| `a whole` | 5 | angry 19, lazy 16, casual 10, formal 3 |
| `with no` | 5 | angry 34, sexy 11, formal 7, casual 2 |

## 4. Opener maps

- assistant pos 0 (n=12058): a 10.0%, the 7.4%, does 2.7%, how 2.3%, did 2.2%, why 1.9%
- assistant pos 1 (n=12058): the 11.2%, a 2.1%, is 1.7%, does 1.6%, you 1.5%, on 0.9%
- assistant pos 2 (n=12057): the 7.3%, a 2.9%, is 2.5%, on 1.9%, of 1.8%, for 1.8%
- assistant pos last (n=12058): it 3.9%, now 1.4%, you 1.2%, time 1.1%, one 1.0%, again 0.9%
- user pos 0 (n=12058): the 14.9%, my 9.4%, our 9.1%, i 6.6%, we 5.8%, you 4.9%
- user pos 1 (n=11995): the 3.3%, you 2.0%, a 1.5%, is 1.2%, got 1.0%, was 0.9%
- user pos 2 (n=11905): the 8.2%, a 3.8%, is 1.6%, my 1.3%, in 1.2%, you 1.2%
- user pos last (n=12058): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.0%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

