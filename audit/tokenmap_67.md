# synth2 token-attractor map

Generated 2026-10-20 18:37  |  corpus 7552 rows, **9872 assistant turns**, 9872 user turns
Probe: `probe_out67_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-20T16:15:08

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.2% | 4.2% | +0.0 |
| `the`-opener (user) | 14.0% | 13.9% | -0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a long` | 3% | 5% | 10x | 15x |
| `the same` | 3% | 7% | 3x | 6x |
| `a bit` | 5% | 5% | 12x | 12x |
| `did it` | - | 5% | - | 11x |
| `in the` | - | 8% | - | 2x |
| `i have` | - | 5% | - | 10x |
| `i will` | - | 5% | - | 9x |
| `it or` | - | 3% | - | 30x |
| `no idea` | - | 3% | - | 27x |
| `i can` | - | 3% | - | 27x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.2% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 36 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a long` | 32 | 32.4 | 7.1 | 5% | 15x | casual 21, lazy 8, angry 3 |
| `the same` | 114 | 115.5 | 105.3 | 7% | 6x | angry 36, casual 36, lazy 29 |
| `a bit` | 40 | 40.5 | 32.4 | 5% | 12x | casual 38, angry 1, lazy 1 |
| `did it` | 43 | 43.6 | 13.2 | 5% | 11x | casual 34, lazy 4, sexy 3 |
| `in the` | 367 | 371.8 | 338.3 | 8% | 2x | casual 169, angry 69, lazy 68 |
| `i have` | 51 | 51.7 | 79.0 | 5% | 10x | casual 35, lazy 12, sexy 4 |
| `i will` | 55 | 55.7 | 8.1 | 5% | 9x | casual 31, lazy 14, sexy 10 |
| `it or` | 11 | 11.1 | 1.0 | 3% | 30x | casual 8, sexy 2, lazy 1 |
| `no idea` | 12 | 12.2 | 8.1 | 3% | 27x | casual 10, lazy 2 |
| `i can` | 12 | 12.2 | 15.2 | 3% | 27x | casual 9, lazy 3 |
| `bit of` | 17 | 17.2 | 9.1 | 3% | 19x | casual 16, angry 1 |
| `if it` | 19 | 19.2 | 6.1 | 3% | 17x | casual 14, lazy 3, angry 2 |
| `i was` | 19 | 19.2 | 46.6 | 3% | 17x | casual 14, sexy 3, lazy 2 |
| `buy the` | 22 | 22.3 | 1.0 | 3% | 15x | lazy 13, casual 5, sexy 3 |
| `it is` | 126 | 127.6 | 53.7 | 5% | 4x | casual 79, lazy 36, angry 7 |
| `and still` | 23 | 23.3 | 13.2 | 3% | 14x | angry 12, casual 9, lazy 1 |
| `so far` | 26 | 26.3 | 11.1 | 3% | 13x | casual 19, lazy 4, angry 2 |
| `about it` | 28 | 28.4 | 29.4 | 3% | 12x | casual 19, lazy 4, sexy 3 |
| `got the` | 30 | 30.4 | 48.6 | 3% | 11x | casual 27, lazy 2, sexy 1 |
| `is a` | 458 | 463.9 | 60.8 | 7% | 1x | angry 208, casual 120, lazy 115 |
| `all day` | 31 | 31.4 | 19.2 | 3% | 11x | lazy 15, casual 10, angry 4 |
| `the morning` | 37 | 37.5 | 23.3 | 3% | 9x | casual 17, lazy 11, angry 7 |
| `and then` | 38 | 38.5 | 22.3 | 3% | 9x | casual 15, angry 13, lazy 8 |
| `did you get` | 44 | 44.6 | 42.5 | 3% | 7x | casual 40, angry 2, lazy 2 |
| `how many` | 56 | 56.7 | 6.1 | 3% | 6x | casual 33, angry 13, sexy 8 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `an early night` | 3 | 11 | 14.0 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `was it worth the` | 4 | 8 | 12.9 | casual 7, sexy 1 |
| `i have been` | 3 | 11 | 12.7 | casual 9, lazy 2 |
| `ten minutes of` | 3 | 11 | 12.7 | sexy 8, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `in ten minutes` | 3 | 8 | 12.0 | casual 5, sexy 3 |
| `an hour of` | 3 | 13 | 12.0 | angry 6, sexy 3, casual 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `fell asleep` | 2 | 9 | 11.4 | casual 4, lazy 4, sexy 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `the same` | 4 | angry 36, casual 36, lazy 29, sexy 13 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `did it` | 4 | casual 34, lazy 4, sexy 3, angry 2 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 61 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `it or` | 3 | casual 8, sexy 2, lazy 1 |
| `no idea` | 2 | casual 10, lazy 2 |
| `i can` | 2 | casual 9, lazy 3 |
| `bit of` | 2 | casual 16, angry 1 |
| `if it` | 3 | casual 14, lazy 3, angry 2 |
| `i was` | 3 | casual 14, sexy 3, lazy 2 |
| `buy the` | 4 | lazy 13, casual 5, sexy 3, angry 1 |
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 4 |
| `and still` | 4 | angry 12, casual 9, lazy 1, sexy 1 |
| `so far` | 4 | casual 19, lazy 4, angry 2, sexy 1 |
| `about it` | 4 | casual 19, lazy 4, sexy 3, angry 2 |
| `got the` | 3 | casual 27, lazy 2, sexy 1 |
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 15 |
| `all day` | 4 | lazy 15, casual 10, angry 4, sexy 2 |
| `the morning` | 4 | casual 17, lazy 11, angry 7, sexy 2 |
| `and then` | 4 | casual 15, angry 13, lazy 8, sexy 2 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `how many` | 4 | casual 33, angry 13, sexy 8, lazy 2 |

## 4. Opener maps

- assistant pos 0 (n=9872): a 9.2%, the 4.2%, did 2.2%, how 2.1%, was 1.8%, that 1.8%
- assistant pos 1 (n=9872): the 10.9%, a 2.2%, you 1.8%, is 1.8%, does 1.2%, your 1.0%
- assistant pos 2 (n=9871): the 6.8%, a 2.9%, is 2.6%, of 1.9%, for 1.8%, on 1.7%
- assistant pos last (n=9872): it 4.0%, now 1.6%, you 1.2%, time 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9872): the 13.9%, my 10.0%, our 8.1%, i 6.2%, we 5.5%, you 4.8%
- user pos 1 (n=9809): the 3.3%, you 2.3%, a 1.9%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=9720): the 7.5%, a 3.1%, is 1.7%, you 1.5%, my 1.4%, was 1.3%
- user pos last (n=9872): again 2.3%, it 2.0%, now 1.3%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.5%**; model outputs: **8.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1675 |
| lazy | 1 / 2155 |

