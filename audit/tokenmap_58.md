# synth2 token-attractor map

Generated 2026-10-19 02:58  |  corpus 6994 rows, **9269 assistant turns**, 9269 user turns
Probe: `probe_out58_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-19T00:47:39

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.8% | 3.8% | +0.1 |
| `the`-opener (user) | 13.9% | 13.9% | -0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `for the` | - | 10% | - | 4x |
| `is the` | - | 10% | - | 2x |
| `to do` | 3% | 5% | 12x | 19x |
| `did not` | - | 5% | - | 18x |
| `do it` | 5% | 5% | 13x | 13x |
| `for one` | - | 5% | - | 11x |
| `up before the` | - | 3% | - | 39x |
| `do that` | - | 3% | - | 39x |
| `week and` | - | 3% | - | 34x |
| `nothing on` | - | 3% | - | 34x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.8% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
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
| `for the` | 259 | 279.4 | 257.8 | 10% | 4x | casual 135, angry 64, sexy 36 |
| `is the` | 422 | 455.3 | 74.4 | 10% | 2x | casual 250, lazy 116, angry 49 |
| `to do` | 25 | 27.0 | 24.8 | 5% | 19x | casual 21, angry 2, lazy 1 |
| `did not` | 26 | 28.1 | 31.3 | 5% | 18x | casual 12, lazy 6, angry 4 |
| `do it` | 35 | 37.8 | 7.6 | 5% | 13x | casual 24, lazy 11 |
| `for one` | 42 | 45.3 | 12.9 | 5% | 11x | angry 21, lazy 12, casual 7 |
| `up before the` | 8 | 8.6 | 2.2 | 3% | 39x | casual 3, lazy 3, angry 2 |
| `do that` | 8 | 8.6 | 2.2 | 3% | 39x | casual 7, sexy 1 |
| `week and` | 9 | 9.7 | 8.6 | 3% | 34x | casual 9 |
| `nothing on` | 9 | 9.7 | 1.1 | 3% | 34x | casual 8, lazy 1 |
| `out in` | 11 | 11.9 | 15.1 | 3% | 28x | casual 10, angry 1 |
| `full of` | 11 | 11.9 | 19.4 | 3% | 28x | casual 6, lazy 3, angry 1 |
| `no idea` | 12 | 12.9 | 8.6 | 3% | 26x | casual 10, lazy 2 |
| `i've been` | 14 | 15.1 | 18.3 | 3% | 22x | casual 14 |
| `did you` | 268 | 289.1 | 266.5 | 7% | 2x | casual 192, sexy 43, angry 28 |
| `out of the` | 18 | 19.4 | 17.3 | 3% | 17x | casual 13, lazy 3, angry 2 |
| `oh no` | 18 | 19.4 | 7.6 | 3% | 17x | casual 18 |
| `in the end` | 20 | 21.6 | 11.9 | 3% | 15x | casual 14, angry 5, lazy 1 |
| `off the` | 21 | 22.7 | 23.7 | 3% | 15x | casual 7, sexy 6, angry 5 |
| `the store` | 22 | 23.7 | 12.9 | 3% | 14x | angry 13, lazy 7, casual 1 |
| `it is` | 126 | 135.9 | 56.1 | 5% | 4x | casual 79, lazy 36, angry 7 |
| `to be` | 26 | 28.1 | 19.4 | 3% | 12x | casual 13, lazy 8, sexy 3 |
| `as a` | 32 | 34.5 | 24.8 | 3% | 10x | sexy 11, casual 9, lazy 7 |
| `next time` | 35 | 37.8 | 2.2 | 3% | 9x | casual 15, lazy 11, sexy 7 |
| `the whole` | 177 | 191.0 | 126.2 | 5% | 3x | lazy 83, casual 55, angry 32 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `on the first try` | 4 | 8 | 16.6 | lazy 5, sexy 2, casual 1 |
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.1 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.1 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.2 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `for an hour` | 3 | 12 | 11.6 | casual 8, sexy 2, angry 1 |
| `fell asleep` | 2 | 9 | 11.6 | casual 4, lazy 4, sexy 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `ice cream` | 2 | 8 | 11.5 | lazy 6, casual 1, sexy 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.1 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `a couple of` | 3 | 12 | 10.9 | casual 11, angry 1 |
| `did you find` | 3 | 10 | 10.8 | casual 9, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `for the` | 4 | casual 135, angry 64, sexy 36, lazy 24 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 7 |
| `to do` | 4 | casual 21, angry 2, lazy 1, sexy 1 |
| `did not` | 4 | casual 12, lazy 6, angry 4, sexy 4 |
| `do it` | 2 | casual 24, lazy 11 |
| `for one` | 4 | angry 21, lazy 12, casual 7, sexy 2 |
| `up before the` | 3 | casual 3, lazy 3, angry 2 |
| `do that` | 2 | casual 7, sexy 1 |
| `week and` | 1 | casual 9 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `out in` | 2 | casual 10, angry 1 |
| `full of` | 4 | casual 6, lazy 3, angry 1, sexy 1 |
| `no idea` | 2 | casual 10, lazy 2 |
| `i've been` | 1 | casual 14 |
| `did you` | 4 | casual 192, sexy 43, angry 28, lazy 5 |
| `out of the` | 3 | casual 13, lazy 3, angry 2 |
| `oh no` | 1 | casual 18 |
| `in the end` | 3 | casual 14, angry 5, lazy 1 |
| `off the` | 4 | casual 7, sexy 6, angry 5, lazy 3 |
| `the store` | 4 | angry 13, lazy 7, casual 1, sexy 1 |
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 4 |
| `to be` | 4 | casual 13, lazy 8, sexy 3, angry 2 |
| `as a` | 4 | sexy 11, casual 9, lazy 7, angry 5 |
| `next time` | 4 | casual 15, lazy 11, sexy 7, angry 2 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 7 |

## 4. Opener maps

- assistant pos 0 (n=9269): a 8.3%, the 3.8%, did 2.4%, how 2.3%, was 1.9%, that 1.9%
- assistant pos 1 (n=9269): the 11.5%, a 2.3%, you 1.9%, is 1.9%, does 1.3%, your 1.1%
- assistant pos 2 (n=9268): the 6.6%, a 3.0%, is 2.8%, are 1.8%, for 1.7%, of 1.7%
- assistant pos last (n=9269): it 4.1%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9269): the 13.9%, my 10.2%, our 8.2%, i 6.5%, we 4.7%, you 3.8%
- user pos 1 (n=9206): the 3.5%, you 2.5%, a 2.0%, was 1.2%, did 1.1%, got 1.0%
- user pos 2 (n=9117): the 7.2%, a 3.0%, is 1.9%, you 1.6%, my 1.4%, was 1.3%
- user pos last (n=9269): again 2.4%, it 2.0%, now 1.4%, week 1.3%, night 1.2%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.8%**; model outputs: **13.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1072 |
| lazy | 1 / 2155 |

