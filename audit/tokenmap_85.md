# synth2 token-attractor map

Generated 2026-10-23 17:01  |  corpus 8668 rows, **11078 assistant turns**, 11078 user turns
Probe: `probe_out85_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-23T13:22:20

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.5% | 5.5% | +0.0 |
| `the`-opener (user) | 14.4% | 14.5% | +0.0 |
| copula-only | 0.8% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `you get` | - | 8% | - | 17x |
| `i get` | - | 5% | - | 55x |
| `get to` | - | 5% | - | 50x |
| `and i` | - | 7% | - | 12x |
| `i am` | 5% | 7% | 8x | 11x |
| `the whole` | - | 8% | - | 5x |
| `what did` | - | 7% | - | 10x |
| `is the` | - | 10% | - | 2x |
| `did you` | - | 8% | - | 3x |
| `i will` | - | 5% | - | 10x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.5% | < 12% |
| `the`-opener (user) | 14.5% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `you get` | 55 | 49.6 | 45.1 | 8% | 17x | casual 45, angry 5, lazy 5 |
| `i get` | 10 | 9.0 | 8.1 | 5% | 55x | sexy 6, casual 4 |
| `get to` | 11 | 9.9 | 1.8 | 5% | 50x | casual 5, angry 4, sexy 2 |
| `and i` | 62 | 56.0 | 89.4 | 7% | 12x | casual 31, lazy 25, sexy 6 |
| `i am` | 68 | 61.4 | 35.2 | 7% | 11x | casual 46, lazy 11, sexy 10 |
| `the whole` | 188 | 169.7 | 117.3 | 8% | 5x | lazy 83, casual 57, angry 32 |
| `what did` | 75 | 67.7 | 37.0 | 7% | 10x | casual 41, angry 19, sexy 12 |
| `is the` | 494 | 445.9 | 79.4 | 10% | 2x | casual 292, lazy 116, angry 50 |
| `did you` | 280 | 252.8 | 222.1 | 8% | 3x | casual 187, sexy 57, angry 28 |
| `i will` | 55 | 49.6 | 8.1 | 5% | 10x | casual 31, lazy 14, sexy 10 |
| `not much` | 8 | 7.2 | 2.7 | 3% | 46x | casual 6, angry 1, lazy 1 |
| `been a` | 8 | 7.2 | 4.5 | 3% | 46x | casual 7, angry 1 |
| `did i` | 10 | 9.0 | 0.0 | 3% | 37x | sexy 9, casual 1 |
| `time to` | 11 | 9.9 | 3.6 | 3% | 34x | lazy 5, angry 3, casual 3 |
| `a week` | 79 | 71.3 | 56.0 | 5% | 7x | casual 35, lazy 22, angry 10 |
| `well done` | 12 | 10.8 | 0.9 | 3% | 31x | casual 12 |
| `i had` | 12 | 10.8 | 17.2 | 3% | 31x | casual 10, lazy 2 |
| `point of` | 13 | 11.7 | 0.0 | 3% | 28x | lazy 5, casual 4, sexy 2 |
| `the job` | 14 | 12.6 | 5.4 | 3% | 26x | casual 6, angry 5, formal 1 |
| `week of` | 15 | 13.5 | 3.6 | 3% | 25x | lazy 7, casual 5, angry 3 |
| `had a` | 17 | 15.3 | 82.1 | 3% | 22x | casual 9, sexy 5, formal 2 |
| `get it` | 17 | 15.3 | 1.8 | 3% | 22x | casual 11, lazy 3, sexy 2 |
| `whole_thing` | 19 | 17.2 | 18.1 | 3% | 19x | casual 9, lazy 8, angry 1 |
| `up to` | 22 | 19.9 | 19.9 | 3% | 17x | casual 18, sexy 2, angry 1 |
| `the time` | 22 | 19.9 | 6.3 | 3% | 17x | casual 12, lazy 6, angry 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.8 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.7 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `the front desk` | 3 | 14 | 12.5 | angry 8, lazy 4, casual 1 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `an hour of` | 3 | 18 | 12.4 | angry 6, formal 4, casual 3 |
| `counts as a` | 3 | 12 | 12.3 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `feels like a` | 3 | 8 | 12.0 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `you get` | 3 | casual 45, angry 5, lazy 5 |
| `i get` | 2 | sexy 6, casual 4 |
| `get to` | 3 | casual 5, angry 4, sexy 2 |
| `and i` | 3 | casual 31, lazy 25, sexy 6 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |
| `what did` | 5 | casual 41, angry 19, sexy 12, formal 2 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 20 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `not much` | 3 | casual 6, angry 1, lazy 1 |
| `been a` | 2 | casual 7, angry 1 |
| `did i` | 2 | sexy 9, casual 1 |
| `time to` | 3 | lazy 5, angry 3, casual 3 |
| `a week` | 5 | casual 35, lazy 22, angry 10, formal 10 |
| `well done` | 1 | casual 12 |
| `i had` | 2 | casual 10, lazy 2 |
| `point of` | 5 | lazy 5, casual 4, sexy 2, angry 1 |
| `the job` | 5 | casual 6, angry 5, formal 1, lazy 1 |
| `week of` | 3 | lazy 7, casual 5, angry 3 |
| `had a` | 4 | casual 9, sexy 5, formal 2, lazy 1 |
| `get it` | 4 | casual 11, lazy 3, sexy 2, angry 1 |
| `whole_thing` | 4 | casual 9, lazy 8, angry 1, sexy 1 |
| `up to` | 4 | casual 18, sexy 2, angry 1, formal 1 |
| `the time` | 3 | casual 12, lazy 6, angry 4 |

## 4. Opener maps

- assistant pos 0 (n=11078): a 10.2%, the 5.5%, did 2.3%, how 2.3%, does 1.9%, that 1.7%
- assistant pos 1 (n=11078): the 10.9%, a 2.0%, is 1.8%, you 1.6%, does 1.3%, on 0.9%
- assistant pos 2 (n=11077): the 7.2%, a 2.9%, is 2.7%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=11078): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11078): the 14.5%, my 9.7%, our 8.4%, i 6.3%, we 6.1%, you 5.4%
- user pos 1 (n=11015): the 3.2%, you 2.1%, a 1.7%, got 1.0%, was 1.0%, is 1.0%
- user pos 2 (n=10925): the 7.8%, a 3.5%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11078): it 2.1%, again 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.8%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

