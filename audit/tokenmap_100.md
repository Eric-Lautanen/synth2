# synth2 token-attractor map

Generated 2026-10-25 18:33  |  corpus 9625 rows, **12112 assistant turns**, 12112 user turns
Probe: `probe_out100_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-25T16:11:28

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 7.4% | 7.7% | +0.4 |
| `the`-opener (user) | 14.9% | 15.0% | +0.0 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a real` | - | 7% | - | 8x |
| `clean the` | - | 3% | - | 50x |
| `i am` | - | 5% | - | 9x |
| `the apartment` | - | 3% | - | 34x |
| `do the` | - | 5% | - | 7x |
| `a time` | - | 3% | - | 25x |
| `for me` | - | 3% | - | 18x |
| `enough to` | - | 3% | - | 17x |
| `i did` | - | 3% | - | 16x |
| `kind of` | - | 3% | - | 16x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 7.7% | < 12% |
| `the`-opener (user) | 15.0% | n/a |
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
| `a real` | 98 | 80.9 | 33.0 | 7% | 8x | casual 75, angry 13, lazy 10 |
| `clean the` | 8 | 6.6 | 1.7 | 3% | 50x | lazy 3, casual 2, formal 2 |
| `i am` | 68 | 56.1 | 34.7 | 5% | 9x | casual 46, lazy 11, sexy 10 |
| `the apartment` | 12 | 9.9 | 11.6 | 3% | 34x | casual 7, sexy 4, lazy 1 |
| `do the` | 91 | 75.1 | 9.9 | 5% | 7x | formal 39, casual 28, sexy 13 |
| `a time` | 16 | 13.2 | 3.3 | 3% | 25x | lazy 5, casual 4, formal 4 |
| `for me` | 23 | 19.0 | 12.4 | 3% | 18x | casual 9, lazy 9, sexy 4 |
| `enough to` | 24 | 19.8 | 6.6 | 3% | 17x | casual 7, lazy 6, formal 5 |
| `i did` | 25 | 20.6 | 28.1 | 3% | 16x | casual 20, lazy 4, sexy 1 |
| `kind of` | 26 | 21.5 | 4.1 | 3% | 16x | casual 7, lazy 6, angry 5 |
| `and still` | 26 | 21.5 | 10.7 | 3% | 16x | angry 12, casual 11, formal 1 |
| `is the` | 510 | 421.1 | 77.6 | 7% | 2x | casual 292, lazy 116, angry 50 |
| `a bit` | 36 | 29.7 | 26.4 | 3% | 11x | casual 34, angry 1, lazy 1 |
| `the whole` | 190 | 156.9 | 108.2 | 5% | 3x | lazy 83, casual 57, angry 32 |
| `do we` | 40 | 33.0 | 19.0 | 3% | 10x | sexy 28, formal 11, casual 1 |
| `for it` | 41 | 33.9 | 16.5 | 3% | 10x | casual 23, lazy 7, formal 6 |
| `that's a` | 50 | 41.3 | 6.6 | 3% | 8x | casual 50 |
| `i have` | 50 | 41.3 | 76.0 | 3% | 8x | casual 34, lazy 12, sexy 4 |
| `and i` | 67 | 55.3 | 84.2 | 3% | 6x | casual 31, lazy 25, sexy 6 |
| `what did` | 75 | 61.9 | 33.9 | 3% | 5x | casual 41, angry 19, sexy 12 |
| `is a` | 528 | 435.9 | 73.5 | 5% | 1x | angry 222, casual 147, lazy 116 |
| `it is` | 141 | 116.4 | 51.2 | 3% | 3x | casual 82, lazy 36, angry 10 |
| `yet the` | 8 | 6.6 | 0.0 | 2% | 25x | casual 6, lazy 2 |
| `the best part` | 8 | 6.6 | 1.7 | 2% | 25x | casual 4, lazy 3, sexy 1 |
| `same day` | 8 | 6.6 | 2.5 | 2% | 25x | casual 3, formal 2, lazy 2 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 17.0 | casual 8, angry 2 |
| `shall i add` | 3 | 8 | 16.9 | formal 8 |
| `faster than any` | 3 | 8 | 16.5 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.3 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 16.0 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.1 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `i will bring` | 3 | 9 | 13.4 | formal 4, casual 3, lazy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.6 | angry 4, casual 4 |
| `i have been` | 3 | 10 | 12.4 | casual 8, lazy 2 |
| `an hour of` | 3 | 19 | 12.4 | angry 6, formal 5, casual 3 |
| `did they really` | 3 | 11 | 12.2 | angry 11 |
| `the office manager` | 3 | 9 | 12.2 | formal 9 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.2 | formal 5, casual 2, lazy 2 |
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
| `a real` | 3 | casual 75, angry 13, lazy 10 |
| `clean the` | 4 | lazy 3, casual 2, formal 2, angry 1 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `the apartment` | 3 | casual 7, sexy 4, lazy 1 |
| `do the` | 5 | formal 39, casual 28, sexy 13, angry 6 |
| `a time` | 5 | lazy 5, casual 4, formal 4, sexy 2 |
| `for me` | 4 | casual 9, lazy 9, sexy 4, formal 1 |
| `enough to` | 5 | casual 7, lazy 6, formal 5, angry 3 |
| `i did` | 3 | casual 20, lazy 4, sexy 1 |
| `kind of` | 5 | casual 7, lazy 6, angry 5, formal 4 |
| `and still` | 5 | angry 12, casual 11, formal 1, lazy 1 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 36 |
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |
| `do we` | 3 | sexy 28, formal 11, casual 1 |
| `for it` | 5 | casual 23, lazy 7, formal 6, sexy 3 |
| `that's a` | 1 | casual 50 |
| `i have` | 3 | casual 34, lazy 12, sexy 4 |
| `and i` | 4 | casual 31, lazy 25, sexy 6, formal 5 |
| `what did` | 5 | casual 41, angry 19, sexy 12, formal 2 |
| `is a` | 5 | angry 222, casual 147, lazy 116, formal 28 |
| `it is` | 5 | casual 82, lazy 36, angry 10, formal 9 |
| `yet the` | 2 | casual 6, lazy 2 |
| `the best part` | 3 | casual 4, lazy 3, sexy 1 |
| `same day` | 4 | casual 3, formal 2, lazy 2, angry 1 |

## 4. Opener maps

- assistant pos 0 (n=12112): a 9.9%, the 7.7%, does 2.8%, how 2.2%, did 2.2%, why 1.8%
- assistant pos 1 (n=12112): the 11.2%, a 2.1%, is 1.7%, does 1.6%, you 1.5%, on 0.9%
- assistant pos 2 (n=12111): the 7.3%, a 2.9%, is 2.5%, on 1.9%, of 1.8%, for 1.8%
- assistant pos last (n=12112): it 3.9%, now 1.4%, you 1.2%, time 1.1%, one 0.9%, again 0.9%
- user pos 0 (n=12112): the 15.0%, my 9.4%, our 9.2%, i 6.5%, we 5.8%, you 4.9%
- user pos 1 (n=12049): the 3.3%, you 2.0%, a 1.5%, is 1.2%, got 0.9%, was 0.9%
- user pos 2 (n=11959): the 8.3%, a 3.8%, is 1.6%, my 1.3%, in 1.2%, you 1.2%
- user pos last (n=12112): it 2.2%, again 2.1%, week 1.2%, now 1.2%, morning 1.0%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.5%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

