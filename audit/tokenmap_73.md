# synth2 token-attractor map

Generated 2026-10-21 19:49  |  corpus 7924 rows, **10274 assistant turns**, 10274 user turns
Probe: `probe_out73_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-21T16:11:59

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.4% | 4.5% | +0.1 |
| `the`-opener (user) | 13.9% | 14.0% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i am` | - | 8% | - | 13x |
| `before the` | - | 8% | - | 7x |
| `then the` | - | 5% | - | 27x |
| `means you` | - | 3% | - | 38x |
| `i should` | - | 3% | - | 38x |
| `new place` | - | 3% | - | 34x |
| `it gets` | - | 3% | - | 34x |
| `as well` | - | 3% | - | 34x |
| `is good` | 5% | 3% | 43x | 29x |
| `was not` | - | 3% | - | 26x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.5% | < 12% |
| `the`-opener (user) | 14.0% | n/a |
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
| `i am` | 68 | 66.2 | 35.0 | 8% | 13x | casual 46, lazy 11, sexy 10 |
| `before the` | 116 | 112.9 | 74.0 | 8% | 7x | sexy 37, angry 33, casual 26 |
| `then the` | 19 | 18.5 | 9.7 | 5% | 27x | casual 13, lazy 5, sexy 1 |
| `means you` | 9 | 8.8 | 0.0 | 3% | 38x | lazy 5, sexy 2, angry 1 |
| `i should` | 9 | 8.8 | 2.9 | 3% | 38x | casual 8, sexy 1 |
| `new place` | 10 | 9.7 | 7.8 | 3% | 34x | casual 7, lazy 2, angry 1 |
| `it gets` | 10 | 9.7 | 4.9 | 3% | 34x | casual 9, sexy 1 |
| `as well` | 10 | 9.7 | 4.9 | 3% | 34x | casual 8, angry 1, lazy 1 |
| `is good` | 12 | 11.7 | 1.9 | 3% | 29x | casual 11, lazy 1 |
| `was not` | 13 | 12.7 | 4.9 | 3% | 26x | casual 7, sexy 4, angry 1 |
| `the job` | 13 | 12.7 | 4.9 | 3% | 26x | casual 6, angry 5, lazy 1 |
| `are the best` | 14 | 13.6 | 1.0 | 3% | 24x | casual 7, lazy 7 |
| `the work` | 15 | 14.6 | 2.9 | 3% | 23x | lazy 8, casual 6, angry 1 |
| `the winter` | 18 | 17.5 | 9.7 | 3% | 19x | casual 11, lazy 7 |
| `the store` | 24 | 23.4 | 12.7 | 3% | 14x | angry 13, lazy 7, casual 2 |
| `how is` | 27 | 26.3 | 10.7 | 3% | 13x | angry 17, casual 7, sexy 3 |
| `what did you` | 33 | 32.1 | 31.1 | 3% | 10x | casual 26, sexy 6, lazy 1 |
| `a month` | 34 | 33.1 | 34.1 | 3% | 10x | casual 19, lazy 7, angry 6 |
| `what is` | 36 | 35.0 | 11.7 | 3% | 10x | casual 22, angry 9, sexy 3 |
| `a bit` | 36 | 35.0 | 31.1 | 3% | 10x | casual 34, angry 1, lazy 1 |
| `the phone` | 38 | 37.0 | 29.2 | 3% | 9x | casual 14, lazy 12, angry 10 |
| `the morning` | 38 | 37.0 | 22.4 | 3% | 9x | casual 18, lazy 11, angry 7 |
| `than the` | 40 | 38.9 | 66.2 | 3% | 9x | casual 15, sexy 12, lazy 8 |
| `i will` | 55 | 53.5 | 7.8 | 3% | 6x | casual 31, lazy 14, sexy 10 |
| `a new` | 62 | 60.3 | 61.3 | 3% | 6x | casual 33, angry 13, lazy 11 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.7 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `the front desk` | 3 | 13 | 13.0 | angry 8, lazy 4, casual 1 |
| `was it worth the` | 4 | 8 | 12.8 | casual 7, sexy 1 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `an hour of` | 3 | 14 | 12.1 | angry 6, casual 3, sexy 3 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `have you got` | 3 | 16 | 11.7 | casual 16 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.3 | lazy 6, sexy 3, casual 1 |
| `feel like a` | 3 | 11 | 11.2 | lazy 6, casual 4, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.0 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 11.0 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `did you get` | 3 | 43 | 10.6 | casual 39, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `before the` | 4 | sexy 37, angry 33, casual 26, lazy 20 |
| `then the` | 3 | casual 13, lazy 5, sexy 1 |
| `means you` | 4 | lazy 5, sexy 2, angry 1, casual 1 |
| `i should` | 2 | casual 8, sexy 1 |
| `new place` | 3 | casual 7, lazy 2, angry 1 |
| `it gets` | 2 | casual 9, sexy 1 |
| `as well` | 3 | casual 8, angry 1, lazy 1 |
| `is good` | 2 | casual 11, lazy 1 |
| `was not` | 4 | casual 7, sexy 4, angry 1, lazy 1 |
| `the job` | 4 | casual 6, angry 5, lazy 1, sexy 1 |
| `are the best` | 2 | casual 7, lazy 7 |
| `the work` | 3 | lazy 8, casual 6, angry 1 |
| `the winter` | 2 | casual 11, lazy 7 |
| `the store` | 4 | angry 13, lazy 7, casual 2, sexy 2 |
| `how is` | 3 | angry 17, casual 7, sexy 3 |
| `what did you` | 3 | casual 26, sexy 6, lazy 1 |
| `a month` | 4 | casual 19, lazy 7, angry 6, sexy 2 |
| `what is` | 4 | casual 22, angry 9, sexy 3, lazy 2 |
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `the phone` | 4 | casual 14, lazy 12, angry 10, sexy 2 |
| `the morning` | 4 | casual 18, lazy 11, angry 7, sexy 2 |
| `than the` | 4 | casual 15, sexy 12, lazy 8, angry 5 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `a new` | 4 | casual 33, angry 13, lazy 11, sexy 5 |

## 4. Opener maps

- assistant pos 0 (n=10274): a 10.2%, the 4.5%, did 2.2%, how 2.1%, that 1.8%, was 1.7%
- assistant pos 1 (n=10274): the 10.5%, a 2.0%, is 1.8%, you 1.8%, does 1.1%, on 1.0%
- assistant pos 2 (n=10273): the 6.9%, a 2.9%, is 2.6%, of 2.0%, on 1.9%, for 1.9%
- assistant pos last (n=10274): it 3.8%, now 1.6%, you 1.3%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10274): the 14.0%, my 9.9%, our 8.0%, i 6.0%, we 5.9%, you 5.5%
- user pos 1 (n=10211): the 3.2%, you 2.2%, a 1.8%, was 1.1%, got 1.0%, did 1.0%
- user pos 2 (n=10122): the 7.7%, a 3.2%, is 1.7%, you 1.4%, my 1.4%, was 1.3%
- user pos last (n=10274): again 2.2%, it 2.0%, now 1.3%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.2%**; model outputs: **6.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 425 / 3881 |
| sexy | 5 / 2077 |
| lazy | 1 / 2155 |

