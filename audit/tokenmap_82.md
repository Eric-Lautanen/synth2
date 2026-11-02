# synth2 token-attractor map

Generated 2026-10-23 06:13  |  corpus 8482 rows, **10877 assistant turns**, 10877 user turns
Probe: `probe_out82_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-23T02:17:39

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.3% | 5.4% | +0.1 |
| `the`-opener (user) | 14.4% | 14.4% | +0.0 |
| copula-only | 0.7% | 0.8% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i've been` | - | 7% | - | 52x |
| `you going` | - | 7% | - | 43x |
| `did not` | - | 7% | - | 29x |
| `are you` | - | 8% | - | 8x |
| `i have been` | - | 5% | - | 54x |
| `to do` | 3% | 5% | 15x | 23x |
| `i did` | - | 5% | - | 22x |
| `the whole` | - | 7% | - | 4x |
| `up or` | - | 3% | - | 45x |
| `a new one` | - | 3% | - | 45x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.4% | < 12% |
| `the`-opener (user) | 14.4% | n/a |
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
| `i've been` | 14 | 12.9 | 15.6 | 7% | 52x | casual 14 |
| `you going` | 17 | 15.6 | 4.6 | 7% | 43x | casual 15, angry 2 |
| `did not` | 25 | 23.0 | 31.3 | 7% | 29x | casual 10, lazy 6, angry 4 |
| `are you` | 114 | 104.8 | 62.5 | 8% | 8x | casual 91, angry 12, sexy 10 |
| `i have been` | 10 | 9.2 | 24.8 | 5% | 54x | casual 8, lazy 2 |
| `to do` | 24 | 22.1 | 21.1 | 5% | 23x | casual 20, angry 2, lazy 1 |
| `i did` | 25 | 23.0 | 30.3 | 5% | 22x | casual 20, lazy 4, sexy 1 |
| `the whole` | 186 | 171.0 | 117.7 | 7% | 4x | lazy 83, casual 57, angry 32 |
| `up or` | 8 | 7.4 | 0.0 | 3% | 45x | casual 5, formal 2, angry 1 |
| `a new one` | 8 | 7.4 | 3.7 | 3% | 45x | casual 6, angry 1, lazy 1 |
| `the free` | 9 | 8.3 | 4.6 | 3% | 40x | casual 3, sexy 3, angry 2 |
| `because the` | 9 | 8.3 | 5.5 | 3% | 40x | formal 4, angry 3, casual 1 |
| `how did` | 67 | 61.6 | 8.3 | 5% | 8x | casual 29, sexy 18, angry 17 |
| `i am` | 68 | 62.5 | 35.9 | 5% | 8x | casual 46, lazy 11, sexy 10 |
| `coffee and` | 10 | 9.2 | 8.3 | 3% | 36x | casual 6, lazy 3, sexy 1 |
| `or the` | 75 | 69.0 | 2.8 | 5% | 7x | casual 51, formal 12, sexy 5 |
| `good luck` | 12 | 11.0 | 0.0 | 3% | 30x | casual 9, lazy 2, angry 1 |
| `i know` | 19 | 17.5 | 12.0 | 3% | 19x | casual 15, lazy 2, sexy 2 |
| `is it` | 125 | 114.9 | 22.1 | 5% | 4x | casual 103, formal 11, angry 7 |
| `or did` | 22 | 20.2 | 0.9 | 3% | 16x | casual 10, formal 8, angry 3 |
| `in the` | 384 | 353.0 | 354.9 | 7% | 2x | casual 164, sexy 73, angry 67 |
| `and the` | 155 | 142.5 | 195.8 | 5% | 4x | formal 64, casual 55, lazy 15 |
| `going to` | 32 | 29.4 | 12.9 | 3% | 11x | casual 18, angry 6, lazy 5 |
| `the morning` | 38 | 34.9 | 24.8 | 3% | 10x | casual 18, lazy 11, angry 5 |
| `the room` | 40 | 36.8 | 22.1 | 3% | 9x | sexy 19, formal 8, angry 6 |

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
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `the front desk` | 3 | 13 | 12.6 | angry 8, lazy 4, casual 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `counts as a` | 3 | 12 | 12.4 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 16 | 12.2 | angry 6, casual 3, sexy 3 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i've been` | 1 | casual 14 |
| `you going` | 2 | casual 15, angry 2 |
| `did not` | 5 | casual 10, lazy 6, angry 4, sexy 4 |
| `are you` | 4 | casual 91, angry 12, sexy 10, lazy 1 |
| `i have been` | 2 | casual 8, lazy 2 |
| `to do` | 4 | casual 20, angry 2, lazy 1, sexy 1 |
| `i did` | 3 | casual 20, lazy 4, sexy 1 |
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |
| `up or` | 3 | casual 5, formal 2, angry 1 |
| `a new one` | 3 | casual 6, angry 1, lazy 1 |
| `the free` | 4 | casual 3, sexy 3, angry 2, formal 1 |
| `because the` | 4 | formal 4, angry 3, casual 1, sexy 1 |
| `how did` | 4 | casual 29, sexy 18, angry 17, formal 3 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `coffee and` | 3 | casual 6, lazy 3, sexy 1 |
| `or the` | 5 | casual 51, formal 12, sexy 5, angry 4 |
| `good luck` | 3 | casual 9, lazy 2, angry 1 |
| `i know` | 3 | casual 15, lazy 2, sexy 2 |
| `is it` | 4 | casual 103, formal 11, angry 7, sexy 4 |
| `or did` | 4 | casual 10, formal 8, angry 3, lazy 1 |
| `in the` | 5 | casual 164, sexy 73, angry 67, lazy 67 |
| `and the` | 5 | formal 64, casual 55, lazy 15, angry 13 |
| `going to` | 5 | casual 18, angry 6, lazy 5, sexy 2 |
| `the morning` | 5 | casual 18, lazy 11, angry 5, formal 2 |
| `the room` | 5 | sexy 19, formal 8, angry 6, casual 6 |

## 4. Opener maps

- assistant pos 0 (n=10877): a 10.0%, the 5.4%, did 2.3%, how 2.2%, that 1.7%, does 1.7%
- assistant pos 1 (n=10877): the 11.0%, a 1.9%, is 1.8%, you 1.7%, does 1.2%, on 0.9%
- assistant pos 2 (n=10876): the 7.1%, a 2.8%, is 2.7%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10877): it 3.9%, now 1.6%, you 1.3%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10877): the 14.4%, my 9.8%, our 8.4%, i 6.2%, we 6.1%, you 5.5%
- user pos 1 (n=10814): the 3.2%, you 2.1%, a 1.7%, was 1.0%, got 1.0%, did 0.9%
- user pos 2 (n=10724): the 7.8%, a 3.5%, is 1.7%, my 1.4%, you 1.4%, was 1.2%
- user pos last (n=10877): again 2.2%, it 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.9%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

