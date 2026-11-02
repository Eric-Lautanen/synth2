# synth2 token-attractor map

Generated 2026-10-21 16:11  |  corpus 7862 rows, **10207 assistant turns**, 10207 user turns
Probe: `probe_out72_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-21T13:32:48

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.4% | 4.4% | +0.0 |
| `the`-opener (user) | 13.9% | 13.9% | +0.0 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `no idea` | - | 7% | - | 57x |
| `it is` | 5% | 8% | 4x | 6x |
| `is good` | - | 5% | - | 43x |
| `we are` | - | 5% | - | 24x |
| `on the` | 8% | 8% | 2x | 3x |
| `then it` | 3% | 3% | 42x | 43x |
| `a good` | - | 5% | - | 8x |
| `for a` | - | 7% | - | 3x |
| `to get` | - | 3% | - | 31x |
| `the desk` | - | 3% | - | 26x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.4% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 42 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `no idea` | 12 | 11.8 | 7.8 | 7% | 57x | casual 10, lazy 2 |
| `it is` | 131 | 128.3 | 51.9 | 8% | 6x | casual 84, lazy 36, angry 7 |
| `is good` | 12 | 11.8 | 2.0 | 5% | 43x | casual 11, lazy 1 |
| `we are` | 21 | 20.6 | 28.4 | 5% | 24x | sexy 13, casual 5, lazy 2 |
| `on the` | 340 | 333.1 | 281.2 | 8% | 3x | casual 142, sexy 97, lazy 51 |
| `then it` | 8 | 7.8 | 2.9 | 3% | 43x | lazy 5, casual 3 |
| `a good` | 63 | 61.7 | 13.7 | 5% | 8x | casual 48, lazy 12, sexy 3 |
| `for a` | 206 | 201.8 | 162.6 | 7% | 3x | angry 93, casual 68, lazy 23 |
| `to get` | 11 | 10.8 | 9.8 | 3% | 31x | casual 7, lazy 2, angry 1 |
| `the desk` | 13 | 12.7 | 14.7 | 3% | 26x | casual 5, angry 4, lazy 4 |
| `bit of` | 17 | 16.7 | 8.8 | 3% | 20x | casual 16, angry 1 |
| `a real` | 102 | 99.9 | 43.1 | 5% | 5x | casual 79, angry 13, lazy 10 |
| `last night` | 19 | 18.6 | 50.9 | 3% | 18x | casual 16, angry 2, lazy 1 |
| `the same` | 114 | 111.7 | 104.8 | 5% | 4x | angry 36, casual 35, lazy 29 |
| `on my` | 20 | 19.6 | 45.1 | 3% | 17x | sexy 8, casual 7, lazy 5 |
| `got a` | 23 | 22.5 | 80.3 | 3% | 15x | casual 17, sexy 3, angry 2 |
| `that is` | 148 | 145.0 | 12.7 | 5% | 3x | casual 82, lazy 26, sexy 25 |
| `is the` | 464 | 454.6 | 67.6 | 7% | 1x | casual 283, lazy 116, angry 49 |
| `the way` | 32 | 31.4 | 23.5 | 3% | 11x | casual 20, sexy 7, lazy 4 |
| `of the` | 179 | 175.4 | 125.4 | 5% | 3x | casual 81, lazy 39, sexy 30 |
| `for you` | 39 | 38.2 | 5.9 | 3% | 9x | casual 13, sexy 13, angry 10 |
| `the worst` | 51 | 50.0 | 8.8 | 3% | 7x | casual 26, lazy 17, angry 6 |
| `the car` | 52 | 50.9 | 43.1 | 3% | 7x | casual 29, sexy 13, lazy 9 |
| `i will` | 55 | 53.9 | 7.8 | 3% | 6x | casual 31, lazy 14, sexy 10 |
| `you get` | 57 | 55.8 | 50.0 | 3% | 6x | casual 47, angry 5, lazy 5 |

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
| `an early night` | 3 | 10 | 13.9 | casual 9, lazy 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `the front desk` | 3 | 13 | 13.0 | angry 8, lazy 4, casual 1 |
| `never stood a` | 3 | 8 | 13.0 | sexy 7, casual 1 |
| `was it worth the` | 4 | 8 | 12.8 | casual 7, sexy 1 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `the gift shop` | 3 | 9 | 12.2 | sexy 8, casual 1 |
| `an hour of` | 3 | 14 | 12.1 | angry 6, casual 3, sexy 3 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `have you got` | 3 | 16 | 11.7 | casual 16 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 11 | 11.2 | lazy 6, casual 4, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `no idea` | 2 | casual 10, lazy 2 |
| `it is` | 4 | casual 84, lazy 36, angry 7, sexy 4 |
| `is good` | 2 | casual 11, lazy 1 |
| `we are` | 4 | sexy 13, casual 5, lazy 2, angry 1 |
| `on the` | 4 | casual 142, sexy 97, lazy 51, angry 50 |
| `then it` | 2 | lazy 5, casual 3 |
| `a good` | 3 | casual 48, lazy 12, sexy 3 |
| `for a` | 4 | angry 93, casual 68, lazy 23, sexy 22 |
| `to get` | 4 | casual 7, lazy 2, angry 1, sexy 1 |
| `the desk` | 3 | casual 5, angry 4, lazy 4 |
| `bit of` | 2 | casual 16, angry 1 |
| `a real` | 3 | casual 79, angry 13, lazy 10 |
| `last night` | 3 | casual 16, angry 2, lazy 1 |
| `the same` | 4 | angry 36, casual 35, lazy 29, sexy 14 |
| `on my` | 3 | sexy 8, casual 7, lazy 5 |
| `got a` | 4 | casual 17, sexy 3, angry 2, lazy 1 |
| `that is` | 4 | casual 82, lazy 26, sexy 25, angry 15 |
| `is the` | 4 | casual 283, lazy 116, angry 49, sexy 16 |
| `the way` | 4 | casual 20, sexy 7, lazy 4, angry 1 |
| `of the` | 4 | casual 81, lazy 39, sexy 30, angry 29 |
| `for you` | 4 | casual 13, sexy 13, angry 10, lazy 3 |
| `the worst` | 4 | casual 26, lazy 17, angry 6, sexy 2 |
| `the car` | 4 | casual 29, sexy 13, lazy 9, angry 1 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `you get` | 3 | casual 47, angry 5, lazy 5 |

## 4. Opener maps

- assistant pos 0 (n=10207): a 10.0%, the 4.4%, did 2.2%, how 2.1%, that 1.8%, was 1.7%
- assistant pos 1 (n=10207): the 10.6%, a 2.0%, is 1.8%, you 1.8%, does 1.1%, on 1.0%
- assistant pos 2 (n=10206): the 6.9%, a 2.9%, is 2.6%, of 2.0%, for 1.9%, on 1.8%
- assistant pos last (n=10207): it 3.8%, now 1.6%, you 1.3%, time 1.2%, again 0.9%, one 0.9%
- user pos 0 (n=10207): the 13.9%, my 10.0%, our 8.0%, i 6.0%, we 5.8%, you 5.3%
- user pos 1 (n=10144): the 3.2%, you 2.3%, a 1.8%, was 1.1%, got 1.0%, did 1.0%
- user pos 2 (n=10055): the 7.6%, a 3.2%, is 1.7%, you 1.4%, my 1.4%, was 1.3%
- user pos last (n=10207): again 2.2%, it 2.0%, now 1.3%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.3%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 429 / 3881 |
| sexy | 5 / 2010 |
| lazy | 1 / 2155 |

