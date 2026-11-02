# synth2 token-attractor map

Generated 2026-10-22 06:54  |  corpus 8110 rows, **10475 assistant turns**, 10475 user turns
Probe: `probe_out76_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-22T02:56:55

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.5% | 4.6% | +0.1 |
| `the`-opener (user) | 14.0% | 14.1% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a time` | - | 5% | - | 44x |
| `i got` | - | 5% | - | 37x |
| `of the` | - | 8% | - | 5x |
| `got the` | - | 5% | - | 17x |
| `instead of` | - | 5% | - | 16x |
| `it was` | - | 5% | - | 13x |
| `it a` | - | 5% | - | 12x |
| `or just` | - | 5% | - | 10x |
| `was fine` | 3% | 3% | 43x | 44x |
| `i am` | - | 5% | - | 8x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.6% | < 12% |
| `the`-opener (user) | 14.1% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
| probe outputs carrying a top attractor | 37 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a time` | 12 | 11.5 | 2.9 | 5% | 44x | lazy 5, casual 4, sexy 2 |
| `i got` | 14 | 13.4 | 45.8 | 5% | 37x | casual 12, lazy 1, sexy 1 |
| `of the` | 186 | 177.6 | 126.0 | 8% | 5x | casual 80, lazy 39, sexy 35 |
| `got the` | 30 | 28.6 | 45.8 | 5% | 17x | casual 27, lazy 2, sexy 1 |
| `instead of` | 32 | 30.5 | 27.7 | 5% | 16x | casual 16, angry 10, sexy 6 |
| `it was` | 40 | 38.2 | 55.4 | 5% | 13x | casual 26, sexy 7, lazy 5 |
| `it a` | 44 | 42.0 | 11.5 | 5% | 12x | casual 35, lazy 4, sexy 3 |
| `or just` | 55 | 52.5 | 2.9 | 5% | 10x | casual 38, angry 9, sexy 8 |
| `was fine` | 8 | 7.6 | 3.8 | 3% | 44x | casual 6, lazy 2 |
| `i am` | 68 | 64.9 | 35.3 | 5% | 8x | casual 46, lazy 11, sexy 10 |
| `is a` | 502 | 479.2 | 58.2 | 8% | 2x | angry 222, casual 147, lazy 116 |
| `is fine` | 14 | 13.4 | 4.8 | 3% | 25x | casual 8, lazy 5, angry 1 |
| `did you` | 279 | 266.3 | 234.8 | 7% | 3x | casual 187, sexy 57, angry 28 |
| `yeah the` | 17 | 16.2 | 1.9 | 3% | 21x | casual 16, lazy 1 |
| `the weekend` | 19 | 18.1 | 37.2 | 3% | 18x | casual 14, lazy 4, sexy 1 |
| `on purpose` | 28 | 26.7 | 12.4 | 3% | 12x | sexy 18, lazy 4, angry 3 |
| `a long` | 32 | 30.5 | 6.7 | 3% | 11x | casual 21, lazy 8, angry 3 |
| `a bit` | 36 | 34.4 | 30.5 | 3% | 10x | casual 34, angry 1, lazy 1 |
| `the whole` | 185 | 176.6 | 121.2 | 5% | 3x | lazy 83, casual 57, angry 32 |
| `the rain` | 41 | 39.1 | 31.5 | 3% | 9x | casual 23, lazy 8, angry 6 |
| `did it` | 41 | 39.1 | 12.4 | 3% | 9x | casual 32, lazy 4, sexy 3 |
| `the end` | 47 | 44.9 | 31.5 | 3% | 7x | casual 24, angry 10, lazy 7 |
| `i have` | 50 | 47.7 | 78.3 | 3% | 7x | casual 34, lazy 12, sexy 4 |
| `how long` | 57 | 54.4 | 14.3 | 3% | 6x | casual 31, sexy 15, angry 9 |
| `and i` | 62 | 59.2 | 88.8 | 3% | 6x | casual 31, lazy 25, sexy 6 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.7 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `the front desk` | 3 | 13 | 13.0 | angry 8, lazy 4, casual 1 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 15 | 12.1 | angry 6, casual 3, sexy 3 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `have you got` | 3 | 15 | 11.6 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 11.0 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `are you going` | 3 | 17 | 10.5 | casual 15, angry 2 |
| `did you get` | 3 | 41 | 10.5 | casual 37, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a time` | 4 | lazy 5, casual 4, sexy 2, angry 1 |
| `i got` | 3 | casual 12, lazy 1, sexy 1 |
| `of the` | 5 | casual 80, lazy 39, sexy 35, angry 31 |
| `got the` | 3 | casual 27, lazy 2, sexy 1 |
| `instead of` | 3 | casual 16, angry 10, sexy 6 |
| `it was` | 4 | casual 26, sexy 7, lazy 5, angry 2 |
| `it a` | 4 | casual 35, lazy 4, sexy 3, angry 2 |
| `or just` | 3 | casual 38, angry 9, sexy 8 |
| `was fine` | 2 | casual 6, lazy 2 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `is a` | 5 | angry 222, casual 147, lazy 116, sexy 15 |
| `is fine` | 3 | casual 8, lazy 5, angry 1 |
| `did you` | 5 | casual 187, sexy 57, angry 28, lazy 5 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `the weekend` | 3 | casual 14, lazy 4, sexy 1 |
| `on purpose` | 4 | sexy 18, lazy 4, angry 3, casual 3 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `the whole` | 4 | lazy 83, casual 57, angry 32, sexy 13 |
| `the rain` | 5 | casual 23, lazy 8, angry 6, sexy 3 |
| `did it` | 4 | casual 32, lazy 4, sexy 3, angry 2 |
| `the end` | 4 | casual 24, angry 10, lazy 7, sexy 6 |
| `i have` | 3 | casual 34, lazy 12, sexy 4 |
| `how long` | 5 | casual 31, sexy 15, angry 9, formal 1 |
| `and i` | 3 | casual 31, lazy 25, sexy 6 |

## 4. Opener maps

- assistant pos 0 (n=10475): a 10.2%, the 4.6%, did 2.2%, how 2.1%, that 1.7%, was 1.6%
- assistant pos 1 (n=10475): the 10.5%, a 1.9%, is 1.8%, you 1.7%, does 1.1%, on 1.0%
- assistant pos 2 (n=10474): the 6.9%, a 2.9%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=10475): it 3.8%, now 1.6%, you 1.3%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10475): the 14.1%, my 9.8%, our 8.1%, we 6.1%, i 6.0%, you 5.7%
- user pos 1 (n=10412): the 3.2%, you 2.2%, a 1.8%, was 1.1%, got 1.0%, did 1.0%
- user pos 2 (n=10322): the 7.8%, a 3.3%, is 1.6%, you 1.4%, my 1.4%, was 1.3%
- user pos last (n=10475): again 2.2%, it 2.0%, now 1.2%, week 1.2%, night 1.1%, morning 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.0%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

