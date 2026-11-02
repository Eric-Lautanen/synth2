# synth2 token-attractor map

Generated 2026-10-21 13:32  |  corpus 7800 rows, **10140 assistant turns**, 10140 user turns
Probe: `probe_out71_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-21T10:54:09

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.4% | 4.4% | +0.0 |
| `the`-opener (user) | 14.0% | 13.9% | -0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `that works` | - | 5% | - | 56x |
| `is the` | - | 10% | - | 2x |
| `a long` | - | 5% | - | 15x |
| `on the` | - | 8% | - | 2x |
| `i will` | - | 5% | - | 9x |
| `then it` | - | 3% | - | 42x |
| `the whole` | - | 7% | - | 4x |
| `the real` | - | 5% | - | 9x |
| `i am` | - | 5% | - | 7x |
| `a week` | - | 5% | - | 7x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.4% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 45 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `that works` | 9 | 8.9 | 0.0 | 5% | 56x | lazy 5, casual 4 |
| `is the` | 457 | 450.7 | 68.0 | 10% | 2x | casual 276, lazy 116, angry 49 |
| `a long` | 34 | 33.5 | 6.9 | 5% | 15x | casual 23, lazy 8, angry 3 |
| `on the` | 341 | 336.3 | 281.1 | 8% | 2x | casual 145, sexy 95, lazy 51 |
| `i will` | 55 | 54.2 | 7.9 | 5% | 9x | casual 31, lazy 14, sexy 10 |
| `then it` | 8 | 7.9 | 3.0 | 3% | 42x | lazy 5, casual 3 |
| `the whole` | 186 | 183.4 | 124.3 | 7% | 4x | lazy 83, casual 58, angry 32 |
| `the real` | 59 | 58.2 | 10.8 | 5% | 9x | lazy 23, casual 22, sexy 11 |
| `i am` | 68 | 67.1 | 35.5 | 5% | 7x | casual 46, lazy 11, sexy 10 |
| `a week` | 69 | 68.0 | 53.3 | 5% | 7x | casual 35, lazy 22, angry 10 |
| `night before` | 11 | 10.8 | 4.9 | 3% | 31x | casual 6, angry 3, lazy 2 |
| `i do` | 13 | 12.8 | 12.8 | 3% | 26x | lazy 7, casual 5, sexy 1 |
| `it up` | 14 | 13.8 | 5.9 | 3% | 24x | casual 11, lazy 3 |
| `every week` | 14 | 13.8 | 6.9 | 3% | 24x | angry 5, casual 5, lazy 4 |
| `a real` | 104 | 102.6 | 43.4 | 5% | 5x | casual 81, angry 13, lazy 10 |
| `the same` | 114 | 112.4 | 104.5 | 5% | 4x | angry 36, casual 35, lazy 29 |
| `too much` | 21 | 20.7 | 7.9 | 3% | 16x | casual 9, lazy 9, sexy 2 |
| `it is` | 132 | 130.2 | 52.3 | 5% | 4x | casual 85, lazy 36, angry 7 |
| `and still` | 25 | 24.7 | 12.8 | 3% | 14x | angry 12, casual 11, lazy 1 |
| `the night` | 28 | 27.6 | 12.8 | 3% | 12x | lazy 9, sexy 8, casual 6 |
| `is a` | 465 | 458.6 | 59.2 | 7% | 1x | angry 208, casual 127, lazy 115 |
| `not a` | 35 | 34.5 | 8.9 | 3% | 10x | angry 16, casual 11, lazy 7 |
| `just a` | 35 | 34.5 | 22.7 | 3% | 10x | casual 24, angry 7, lazy 4 |
| `for you` | 38 | 37.5 | 5.9 | 3% | 9x | casual 13, sexy 12, angry 10 |
| `and then` | 38 | 37.5 | 21.7 | 3% | 9x | casual 15, angry 13, lazy 8 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `never stood a chance` | 4 | 8 | 25.8 | sexy 7, casual 1 |
| `stood a chance` | 3 | 8 | 16.8 | sexy 7, casual 1 |
| `are you going to` | 4 | 10 | 16.6 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.8 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `never stood a` | 3 | 8 | 13.0 | sexy 7, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 12.8 | casual 7, sexy 1 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `the gift shop` | 3 | 8 | 12.1 | sexy 7, casual 1 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `that works` | 2 | lazy 5, casual 4 |
| `is the` | 4 | casual 276, lazy 116, angry 49, sexy 16 |
| `a long` | 3 | casual 23, lazy 8, angry 3 |
| `on the` | 4 | casual 145, sexy 95, lazy 51, angry 50 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `then it` | 2 | lazy 5, casual 3 |
| `the whole` | 4 | lazy 83, casual 58, angry 32, sexy 13 |
| `the real` | 4 | lazy 23, casual 22, sexy 11, angry 3 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `a week` | 4 | casual 35, lazy 22, angry 10, sexy 2 |
| `night before` | 3 | casual 6, angry 3, lazy 2 |
| `i do` | 3 | lazy 7, casual 5, sexy 1 |
| `it up` | 2 | casual 11, lazy 3 |
| `every week` | 3 | angry 5, casual 5, lazy 4 |
| `a real` | 3 | casual 81, angry 13, lazy 10 |
| `the same` | 4 | angry 36, casual 35, lazy 29, sexy 14 |
| `too much` | 4 | casual 9, lazy 9, sexy 2, angry 1 |
| `it is` | 4 | casual 85, lazy 36, angry 7, sexy 4 |
| `and still` | 4 | angry 12, casual 11, lazy 1, sexy 1 |
| `the night` | 4 | lazy 9, sexy 8, casual 6, angry 5 |
| `is a` | 4 | angry 208, casual 127, lazy 115, sexy 15 |
| `not a` | 4 | angry 16, casual 11, lazy 7, sexy 1 |
| `just a` | 3 | casual 24, angry 7, lazy 4 |
| `for you` | 4 | casual 13, sexy 12, angry 10, lazy 3 |
| `and then` | 4 | casual 15, angry 13, lazy 8, sexy 2 |

## 4. Opener maps

- assistant pos 0 (n=10140): a 9.7%, the 4.4%, did 2.3%, how 2.1%, that 1.8%, was 1.7%
- assistant pos 1 (n=10140): the 10.7%, a 2.1%, is 1.8%, you 1.8%, does 1.2%, on 1.0%
- assistant pos 2 (n=10139): the 6.9%, a 2.9%, is 2.6%, of 1.9%, on 1.8%, for 1.8%
- assistant pos last (n=10140): it 3.9%, now 1.6%, you 1.3%, time 1.2%, again 0.9%, one 0.9%
- user pos 0 (n=10140): the 13.9%, my 10.0%, our 8.1%, i 6.1%, we 5.8%, you 5.2%
- user pos 1 (n=10077): the 3.2%, you 2.3%, a 1.8%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=9988): the 7.6%, a 3.2%, is 1.7%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=10140): again 2.3%, it 2.0%, now 1.3%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.3%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 429 / 3881 |
| sexy | 5 / 1943 |
| lazy | 1 / 2155 |

