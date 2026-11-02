# synth2 token-attractor map

Generated 2026-10-18 05:45  |  corpus 6560 rows, **8800 assistant turns**, 8800 user turns
Probe: `probe_out51_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T02:53:32

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.5% | 3.6% | +0.2 |
| `the`-opener (user) | 13.6% | 13.6% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `is the` | 7% | 10% | 1x | 2x |
| `a long` | - | 5% | - | 14x |
| `been a` | 3% | 3% | 36x | 37x |
| `anything good` | - | 3% | - | 33x |
| `is a` | - | 8% | - | 2x |
| `i am` | - | 5% | - | 7x |
| `no idea` | 3% | 3% | 24x | 24x |
| `with the` | - | 5% | - | 5x |
| `on the` | - | 7% | - | 2x |
| `you need` | - | 3% | - | 18x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.6% | < 12% |
| `the`-opener (user) | 13.6% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 41 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `is the` | 418 | 475.0 | 78.4 | 10% | 2x | casual 250, lazy 116, angry 49 |
| `a long` | 32 | 36.4 | 8.0 | 5% | 14x | casual 21, lazy 8, angry 3 |
| `been a` | 8 | 9.1 | 4.5 | 3% | 37x | casual 7, angry 1 |
| `anything good` | 9 | 10.2 | 3.4 | 3% | 33x | casual 7, lazy 2 |
| `is a` | 449 | 510.2 | 67.0 | 8% | 2x | angry 208, casual 121, lazy 115 |
| `i am` | 64 | 72.7 | 40.9 | 5% | 7x | casual 44, lazy 11, sexy 8 |
| `no idea` | 12 | 13.6 | 9.1 | 3% | 24x | casual 10, lazy 2 |
| `with the` | 91 | 103.4 | 75.0 | 5% | 5x | casual 55, angry 18, lazy 12 |
| `on the` | 273 | 310.2 | 281.8 | 7% | 2x | casual 151, lazy 51, angry 50 |
| `you need` | 16 | 18.2 | 1.1 | 3% | 18x | casual 10, lazy 5, angry 1 |
| `next week` | 16 | 18.2 | 17.0 | 3% | 18x | casual 15, lazy 1 |
| `you can` | 18 | 20.5 | 1.1 | 3% | 16x | casual 10, angry 5, lazy 3 |
| `for once` | 19 | 21.6 | 10.2 | 3% | 15x | casual 17, lazy 2 |
| `before it` | 23 | 26.1 | 6.8 | 3% | 13x | casual 12, lazy 6, angry 5 |
| `it is` | 125 | 142.0 | 59.1 | 5% | 4x | casual 79, lazy 36, angry 7 |
| `did not` | 24 | 27.3 | 30.7 | 3% | 12x | casual 12, lazy 6, angry 4 |
| `a lot` | 24 | 27.3 | 13.6 | 3% | 12x | casual 15, lazy 7, angry 2 |
| `as a` | 28 | 31.8 | 21.6 | 3% | 10x | casual 9, lazy 7, sexy 7 |
| `for you` | 32 | 36.4 | 5.7 | 3% | 9x | casual 12, angry 10, sexy 7 |
| `of the` | 162 | 184.1 | 125.0 | 5% | 3x | casual 84, lazy 39, angry 29 |
| `what is` | 35 | 39.8 | 13.6 | 3% | 8x | casual 23, angry 9, lazy 2 |
| `not a` | 35 | 39.8 | 10.2 | 3% | 8x | angry 16, casual 11, lazy 7 |
| `the whole` | 175 | 198.9 | 131.8 | 5% | 3x | lazy 83, casual 55, angry 32 |
| `did it` | 40 | 45.5 | 14.8 | 3% | 7x | casual 34, lazy 4, angry 2 |
| `a bit` | 40 | 45.5 | 36.4 | 3% | 7x | casual 38, angry 1, lazy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.2 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.9 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `fell asleep` | 2 | 8 | 11.6 | casual 4, lazy 4 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `for an hour` | 3 | 11 | 11.6 | casual 8, angry 1, lazy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `falling asleep` | 2 | 9 | 11.3 | sexy 8, lazy 1 |
| `a couple of` | 3 | 12 | 11.3 | casual 11, angry 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `did you find` | 3 | 9 | 10.8 | casual 9 |
| `did you get` | 3 | 44 | 10.7 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 9 | 10.6 | casual 7, lazy 1, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 3 |
| `a long` | 3 | casual 21, lazy 8, angry 3 |
| `been a` | 2 | casual 7, angry 1 |
| `anything good` | 2 | casual 7, lazy 2 |
| `is a` | 4 | angry 208, casual 121, lazy 115, sexy 5 |
| `i am` | 4 | casual 44, lazy 11, sexy 8, angry 1 |
| `no idea` | 2 | casual 10, lazy 2 |
| `with the` | 4 | casual 55, angry 18, lazy 12, sexy 6 |
| `on the` | 4 | casual 151, lazy 51, angry 50, sexy 21 |
| `you need` | 3 | casual 10, lazy 5, angry 1 |
| `next week` | 2 | casual 15, lazy 1 |
| `you can` | 3 | casual 10, angry 5, lazy 3 |
| `for once` | 2 | casual 17, lazy 2 |
| `before it` | 3 | casual 12, lazy 6, angry 5 |
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 3 |
| `did not` | 4 | casual 12, lazy 6, angry 4, sexy 2 |
| `a lot` | 3 | casual 15, lazy 7, angry 2 |
| `as a` | 4 | casual 9, lazy 7, sexy 7, angry 5 |
| `for you` | 4 | casual 12, angry 10, sexy 7, lazy 3 |
| `of the` | 4 | casual 84, lazy 39, angry 29, sexy 10 |
| `what is` | 4 | casual 23, angry 9, lazy 2, sexy 1 |
| `not a` | 4 | angry 16, casual 11, lazy 7, sexy 1 |
| `the whole` | 4 | lazy 83, casual 55, angry 32, sexy 5 |
| `did it` | 3 | casual 34, lazy 4, angry 2 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |

## 4. Opener maps

- assistant pos 0 (n=8800): a 7.9%, the 3.6%, did 2.5%, how 2.4%, was 2.0%, that 1.9%
- assistant pos 1 (n=8800): the 11.6%, a 2.4%, you 2.0%, is 2.0%, does 1.3%, your 1.1%
- assistant pos 2 (n=8799): the 6.2%, a 3.0%, is 2.9%, are 1.9%, of 1.7%, for 1.6%
- assistant pos last (n=8800): it 4.1%, now 1.6%, time 1.2%, you 1.2%, again 1.0%, one 1.0%
- user pos 0 (n=8800): the 13.6%, my 10.4%, our 8.1%, i 6.7%, we 3.9%, they 3.2%
- user pos 1 (n=8737): the 3.7%, you 2.6%, a 2.1%, was 1.2%, did 1.1%, is 1.0%
- user pos 2 (n=8648): the 6.9%, a 3.0%, is 2.0%, you 1.7%, my 1.5%, and 1.3%
- user pos last (n=8800): again 2.5%, it 2.0%, now 1.5%, week 1.4%, night 1.3%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.0%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 603 |
| lazy | 1 / 2155 |

