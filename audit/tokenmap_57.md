# synth2 token-attractor map

Generated 2026-10-19 00:47  |  corpus 6932 rows, **9202 assistant turns**, 9202 user turns
Probe: `probe_out57_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T22:01:35

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.8% | 3.8% | +0.0 |
| `the`-opener (user) | 13.9% | 13.9% | -0.0 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i will` | - | 7% | - | 11x |
| `is how` | - | 5% | - | 29x |
| `i am` | - | 7% | - | 9x |
| `just a` | - | 5% | - | 14x |
| `do it` | - | 5% | - | 13x |
| `me at` | - | 3% | - | 38x |
| `a good` | - | 5% | - | 8x |
| `day and` | - | 3% | - | 34x |
| `coffee and` | - | 3% | - | 31x |
| `how you` | - | 3% | - | 28x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.8% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
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
| `i will` | 55 | 59.8 | 8.7 | 7% | 11x | casual 31, lazy 14, sexy 10 |
| `is how` | 16 | 17.4 | 0.0 | 5% | 29x | angry 7, casual 5, lazy 4 |
| `i am` | 66 | 71.7 | 39.1 | 7% | 9x | casual 44, lazy 11, sexy 10 |
| `just a` | 33 | 35.9 | 21.7 | 5% | 14x | casual 22, angry 7, lazy 4 |
| `do it` | 35 | 38.0 | 7.6 | 5% | 13x | casual 24, lazy 11 |
| `me at` | 8 | 8.7 | 23.9 | 3% | 38x | casual 4, sexy 3, lazy 1 |
| `a good` | 58 | 63.0 | 15.2 | 5% | 8x | casual 43, lazy 12, sexy 3 |
| `day and` | 9 | 9.8 | 3.3 | 3% | 34x | casual 6, lazy 2, angry 1 |
| `coffee and` | 10 | 10.9 | 7.6 | 3% | 31x | casual 6, lazy 3, sexy 1 |
| `how you` | 11 | 12.0 | 1.1 | 3% | 28x | casual 5, lazy 3, sexy 3 |
| `at the` | 224 | 243.4 | 229.3 | 7% | 3x | casual 104, lazy 52, angry 38 |
| `the job` | 12 | 13.0 | 4.3 | 3% | 26x | casual 6, angry 5, lazy 1 |
| `early night` | 12 | 13.0 | 3.3 | 3% | 26x | casual 11, lazy 1 |
| `a couple of` | 12 | 13.0 | 5.4 | 3% | 26x | casual 11, angry 1 |
| `with the` | 93 | 101.1 | 73.9 | 5% | 5x | casual 55, angry 18, lazy 12 |
| `i would` | 16 | 17.4 | 4.3 | 3% | 19x | casual 8, angry 4, lazy 2 |
| `at that` | 16 | 17.4 | 4.3 | 3% | 19x | casual 9, angry 6, lazy 1 |
| `night is` | 21 | 22.8 | 3.3 | 3% | 15x | angry 8, casual 7, lazy 4 |
| `to do` | 25 | 27.2 | 25.0 | 3% | 12x | casual 21, angry 2, lazy 1 |
| `you go` | 27 | 29.3 | 8.7 | 3% | 11x | casual 26, lazy 1 |
| `a long` | 32 | 34.8 | 7.6 | 3% | 10x | casual 21, lazy 8, angry 3 |
| `for it` | 33 | 35.9 | 17.4 | 3% | 9x | casual 24, lazy 7, angry 2 |
| `the whole` | 176 | 191.3 | 127.1 | 5% | 3x | lazy 83, casual 55, angry 32 |
| `do the` | 41 | 44.6 | 8.7 | 3% | 7x | casual 28, angry 6, lazy 5 |
| `for a` | 202 | 219.5 | 168.4 | 5% | 2x | angry 93, casual 71, lazy 23 |

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
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.3 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `fell asleep` | 2 | 9 | 11.6 | casual 4, lazy 4, sexy 1 |
| `for an hour` | 3 | 12 | 11.6 | casual 8, sexy 2, angry 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `ice cream` | 2 | 8 | 11.6 | lazy 6, casual 1, sexy 1 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `a couple of` | 3 | 12 | 11.0 | casual 11, angry 1 |
| `did you find` | 3 | 10 | 10.8 | casual 9, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i will` | 3 | casual 31, lazy 14, sexy 10 |
| `is how` | 3 | angry 7, casual 5, lazy 4 |
| `i am` | 4 | casual 44, lazy 11, sexy 10, angry 1 |
| `just a` | 3 | casual 22, angry 7, lazy 4 |
| `do it` | 2 | casual 24, lazy 11 |
| `me at` | 3 | casual 4, sexy 3, lazy 1 |
| `a good` | 3 | casual 43, lazy 12, sexy 3 |
| `day and` | 3 | casual 6, lazy 2, angry 1 |
| `coffee and` | 3 | casual 6, lazy 3, sexy 1 |
| `how you` | 3 | casual 5, lazy 3, sexy 3 |
| `at the` | 4 | casual 104, lazy 52, angry 38, sexy 30 |
| `the job` | 3 | casual 6, angry 5, lazy 1 |
| `early night` | 2 | casual 11, lazy 1 |
| `a couple of` | 2 | casual 11, angry 1 |
| `with the` | 4 | casual 55, angry 18, lazy 12, sexy 8 |
| `i would` | 4 | casual 8, angry 4, lazy 2, sexy 2 |
| `at that` | 3 | casual 9, angry 6, lazy 1 |
| `night is` | 4 | angry 8, casual 7, lazy 4, sexy 2 |
| `to do` | 4 | casual 21, angry 2, lazy 1, sexy 1 |
| `you go` | 2 | casual 26, lazy 1 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `for it` | 3 | casual 24, lazy 7, angry 2 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 6 |
| `do the` | 4 | casual 28, angry 6, lazy 5, sexy 2 |
| `for a` | 4 | angry 93, casual 71, lazy 23, sexy 15 |

## 4. Opener maps

- assistant pos 0 (n=9202): a 8.3%, the 3.8%, did 2.4%, how 2.3%, was 1.9%, that 1.9%
- assistant pos 1 (n=9202): the 11.5%, a 2.3%, you 1.9%, is 1.9%, does 1.3%, your 1.1%
- assistant pos 2 (n=9201): the 6.5%, a 3.0%, is 2.8%, are 1.8%, for 1.7%, of 1.7%
- assistant pos last (n=9202): it 4.1%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9202): the 13.9%, my 10.2%, our 8.2%, i 6.6%, we 4.6%, you 3.6%
- user pos 1 (n=9139): the 3.5%, you 2.5%, a 2.0%, was 1.2%, did 1.1%, got 1.0%
- user pos 2 (n=9050): the 7.2%, a 3.0%, is 1.9%, you 1.6%, my 1.5%, was 1.3%
- user pos last (n=9202): again 2.5%, it 2.0%, now 1.4%, week 1.3%, night 1.2%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.8%**; model outputs: **6.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 1005 |
| lazy | 1 / 2155 |

