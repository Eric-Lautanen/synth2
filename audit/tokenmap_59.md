# synth2 token-attractor map

Generated 2026-10-19 05:33  |  corpus 7056 rows, **9336 assistant turns**, 9336 user turns
Probe: `probe_out59_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-19T02:58:19

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.8% | 3.9% | +0.0 |
| `the`-opener (user) | 13.9% | 13.9% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i got` | - | 5% | - | 31x |
| `are you` | - | 7% | - | 5x |
| `a bit` | - | 5% | - | 12x |
| `and it` | - | 5% | - | 11x |
| `how long` | - | 5% | - | 9x |
| `a good` | - | 5% | - | 8x |
| `nothing on` | 3% | 3% | 34x | 35x |
| `is a` | - | 8% | - | 2x |
| `what you` | - | 3% | - | 24x |
| `i do` | - | 3% | - | 24x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.9% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 34 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `i got` | 15 | 16.1 | 49.3 | 5% | 31x | casual 13, lazy 1, sexy 1 |
| `are you` | 114 | 122.1 | 71.8 | 7% | 5x | casual 92, angry 12, sexy 9 |
| `a bit` | 40 | 42.8 | 34.3 | 5% | 12x | casual 38, angry 1, lazy 1 |
| `and it` | 43 | 46.1 | 60.0 | 5% | 11x | casual 36, lazy 5, sexy 2 |
| `how long` | 53 | 56.8 | 16.1 | 5% | 9x | casual 30, sexy 13, angry 9 |
| `a good` | 58 | 62.1 | 15.0 | 5% | 8x | casual 43, lazy 12, sexy 3 |
| `nothing on` | 9 | 9.6 | 1.1 | 3% | 35x | casual 8, lazy 1 |
| `is a` | 454 | 486.3 | 63.2 | 8% | 2x | angry 208, casual 120, lazy 115 |
| `what you` | 13 | 13.9 | 3.2 | 3% | 24x | casual 9, angry 2, sexy 2 |
| `i do` | 13 | 13.9 | 13.9 | 3% | 24x | lazy 7, casual 5, sexy 1 |
| `coffee is` | 13 | 13.9 | 5.4 | 3% | 24x | lazy 8, casual 5 |
| `which is` | 20 | 21.4 | 36.4 | 3% | 16x | lazy 11, casual 8, angry 1 |
| `up to` | 20 | 21.4 | 21.4 | 3% | 16x | casual 18, angry 1, sexy 1 |
| `is the` | 422 | 452.0 | 73.9 | 7% | 1x | casual 250, lazy 116, angry 49 |
| `get the` | 28 | 30.0 | 20.4 | 3% | 11x | casual 17, lazy 8, angry 2 |
| `got the` | 29 | 31.1 | 48.2 | 3% | 11x | casual 27, lazy 2 |
| `were you` | 32 | 34.3 | 0.0 | 3% | 10x | sexy 14, angry 12, casual 6 |
| `the house` | 35 | 37.5 | 22.5 | 3% | 9x | lazy 18, casual 15, angry 1 |
| `the rain` | 38 | 40.7 | 33.2 | 3% | 8x | casual 21, lazy 8, angry 6 |
| `did you get` | 44 | 47.1 | 45.0 | 3% | 7x | casual 40, angry 2, lazy 2 |
| `the day` | 46 | 49.3 | 21.4 | 3% | 7x | lazy 22, casual 17, angry 4 |
| `i have` | 51 | 54.6 | 83.5 | 3% | 6x | casual 35, lazy 12, sexy 4 |
| `for the` | 261 | 279.6 | 258.1 | 5% | 2x | casual 135, angry 64, sexy 38 |
| `has the` | 77 | 82.5 | 4.3 | 3% | 4x | angry 56, casual 20, lazy 1 |
| `do you` | 108 | 115.7 | 56.8 | 3% | 3x | casual 73, angry 26, sexy 8 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `on the first try` | 4 | 8 | 16.6 | lazy 5, sexy 2, casual 1 |
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.2 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.3 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.0 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `fell asleep` | 2 | 9 | 11.6 | casual 4, lazy 4, sexy 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `for an hour` | 3 | 12 | 11.5 | casual 8, sexy 2, angry 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `ice cream` | 2 | 9 | 11.5 | lazy 6, sexy 2, casual 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `how long did` | 3 | 13 | 11.0 | casual 9, angry 3, sexy 1 |
| `a couple of` | 3 | 12 | 10.9 | casual 11, angry 1 |
| `did you find` | 3 | 10 | 10.8 | casual 9, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i got` | 3 | casual 13, lazy 1, sexy 1 |
| `are you` | 4 | casual 92, angry 12, sexy 9, lazy 1 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `and it` | 3 | casual 36, lazy 5, sexy 2 |
| `how long` | 4 | casual 30, sexy 13, angry 9, lazy 1 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 11 |
| `what you` | 3 | casual 9, angry 2, sexy 2 |
| `i do` | 3 | lazy 7, casual 5, sexy 1 |
| `coffee is` | 2 | lazy 8, casual 5 |
| `which is` | 3 | lazy 11, casual 8, angry 1 |
| `up to` | 3 | casual 18, angry 1, sexy 1 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 7 |
| `get the` | 4 | casual 17, lazy 8, angry 2, sexy 1 |
| `got the` | 2 | casual 27, lazy 2 |
| `were you` | 3 | sexy 14, angry 12, casual 6 |
| `the house` | 4 | lazy 18, casual 15, angry 1, sexy 1 |
| `the rain` | 4 | casual 21, lazy 8, angry 6, sexy 3 |
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `the day` | 4 | lazy 22, casual 17, angry 4, sexy 3 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `for the` | 4 | casual 135, angry 64, sexy 38, lazy 24 |
| `has the` | 3 | angry 56, casual 20, lazy 1 |
| `do you` | 4 | casual 73, angry 26, sexy 8, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=9336): a 8.5%, the 3.9%, did 2.4%, how 2.2%, was 1.9%, that 1.9%
- assistant pos 1 (n=9336): the 11.4%, a 2.3%, you 1.9%, is 1.9%, does 1.3%, your 1.1%
- assistant pos 2 (n=9335): the 6.6%, a 3.0%, is 2.8%, are 1.8%, for 1.7%, of 1.7%
- assistant pos last (n=9336): it 4.1%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9336): the 13.9%, my 10.2%, our 8.2%, i 6.5%, we 4.8%, you 3.9%
- user pos 1 (n=9273): the 3.5%, you 2.5%, a 2.0%, was 1.2%, did 1.1%, got 1.0%
- user pos 2 (n=9184): the 7.2%, a 3.1%, is 1.9%, you 1.6%, my 1.4%, was 1.3%
- user pos last (n=9336): again 2.4%, it 2.0%, now 1.4%, week 1.3%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.7%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1139 |
| lazy | 1 / 2155 |

