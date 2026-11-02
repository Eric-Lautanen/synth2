# synth2 token-attractor map

Generated 2026-10-18 22:01  |  corpus 6870 rows, **9135 assistant turns**, 9135 user turns
Probe: `probe_out56_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T19:08:23

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.7% | 3.8% | +0.0 |
| `the`-opener (user) | 14.0% | 13.9% | -0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `in my` | - | 5% | - | 33x |
| `a week` | 3% | 7% | 4x | 9x |
| `is a` | - | 10% | - | 2x |
| `how much` | - | 5% | - | 16x |
| `of it` | - | 5% | - | 12x |
| `the worst` | 3% | 5% | 6x | 9x |
| `of the` | - | 7% | - | 4x |
| `it take` | - | 3% | - | 38x |
| `is the` | - | 8% | - | 2x |
| `as long` | - | 3% | - | 34x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.8% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 44 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `in my` | 14 | 15.3 | 37.2 | 5% | 33x | lazy 6, sexy 4, casual 3 |
| `a week` | 70 | 76.6 | 58.0 | 7% | 9x | casual 36, lazy 22, angry 10 |
| `is a` | 452 | 494.8 | 64.6 | 10% | 2x | angry 208, casual 120, lazy 115 |
| `how much` | 29 | 31.7 | 4.4 | 5% | 16x | casual 25, angry 3, sexy 1 |
| `of it` | 39 | 42.7 | 28.5 | 5% | 12x | casual 31, angry 4, lazy 3 |
| `the worst` | 50 | 54.7 | 8.8 | 5% | 9x | casual 26, lazy 17, angry 6 |
| `of the` | 165 | 180.6 | 124.8 | 7% | 4x | casual 84, lazy 39, angry 29 |
| `it take` | 8 | 8.8 | 1.1 | 3% | 38x | casual 8 |
| `is the` | 422 | 462.0 | 75.5 | 8% | 2x | casual 250, lazy 116, angry 49 |
| `as long` | 9 | 9.9 | 2.2 | 3% | 34x | casual 4, lazy 3, angry 1 |
| `out of` | 65 | 71.2 | 76.6 | 5% | 7x | casual 34, angry 15, lazy 14 |
| `an hour` | 74 | 81.0 | 86.5 | 5% | 6x | casual 34, lazy 16, angry 12 |
| `want to` | 12 | 13.1 | 60.2 | 3% | 25x | casual 7, sexy 4, angry 1 |
| `good luck` | 12 | 13.1 | 0.0 | 3% | 25x | casual 9, lazy 2, angry 1 |
| `in a` | 84 | 92.0 | 73.3 | 5% | 5x | casual 28, angry 27, lazy 21 |
| `you already` | 14 | 15.3 | 9.9 | 3% | 22x | angry 10, lazy 2, casual 1 |
| `that one` | 15 | 16.4 | 4.4 | 3% | 20x | casual 8, sexy 5, angry 1 |
| `the week` | 17 | 18.6 | 13.1 | 3% | 18x | lazy 11, casual 5, angry 1 |
| `i was` | 19 | 20.8 | 46.0 | 3% | 16x | casual 14, sexy 3, lazy 2 |
| `has a` | 19 | 20.8 | 28.5 | 3% | 16x | lazy 7, angry 5, sexy 4 |
| `back to` | 19 | 20.8 | 15.3 | 3% | 16x | casual 10, angry 6, lazy 2 |
| `the same` | 109 | 119.3 | 104.0 | 5% | 4x | angry 36, casual 36, lazy 29 |
| `in the` | 337 | 368.9 | 335.0 | 7% | 2x | casual 169, angry 69, lazy 68 |
| `you got` | 22 | 24.1 | 7.7 | 3% | 14x | casual 21, angry 1 |
| `it is` | 126 | 137.9 | 56.9 | 5% | 4x | casual 79, lazy 36, angry 7 |

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
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `fell asleep` | 2 | 8 | 11.7 | casual 4, lazy 4 |
| `ice cream` | 2 | 8 | 11.6 | lazy 6, casual 1, sexy 1 |
| `for an hour` | 3 | 12 | 11.6 | casual 8, sexy 2, angry 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `sounds like a` | 3 | 9 | 11.5 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `has it been` | 3 | 8 | 11.3 | casual 8 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |
| `a couple of` | 3 | 12 | 11.0 | casual 11, angry 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `in my` | 4 | lazy 6, sexy 4, casual 3, angry 1 |
| `a week` | 4 | casual 36, lazy 22, angry 10, sexy 2 |
| `is a` | 4 | angry 208, casual 120, lazy 115, sexy 9 |
| `how much` | 3 | casual 25, angry 3, sexy 1 |
| `of it` | 4 | casual 31, angry 4, lazy 3, sexy 1 |
| `the worst` | 4 | casual 26, lazy 17, angry 6, sexy 1 |
| `of the` | 4 | casual 84, lazy 39, angry 29, sexy 13 |
| `it take` | 1 | casual 8 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 7 |
| `as long` | 4 | casual 4, lazy 3, angry 1, sexy 1 |
| `out of` | 4 | casual 34, angry 15, lazy 14, sexy 2 |
| `an hour` | 4 | casual 34, lazy 16, angry 12, sexy 12 |
| `want to` | 3 | casual 7, sexy 4, angry 1 |
| `good luck` | 3 | casual 9, lazy 2, angry 1 |
| `in a` | 4 | casual 28, angry 27, lazy 21, sexy 8 |
| `you already` | 4 | angry 10, lazy 2, casual 1, sexy 1 |
| `that one` | 4 | casual 8, sexy 5, angry 1, lazy 1 |
| `the week` | 3 | lazy 11, casual 5, angry 1 |
| `i was` | 3 | casual 14, sexy 3, lazy 2 |
| `has a` | 4 | lazy 7, angry 5, sexy 4, casual 3 |
| `back to` | 4 | casual 10, angry 6, lazy 2, sexy 1 |
| `the same` | 4 | angry 36, casual 36, lazy 29, sexy 8 |
| `in the` | 4 | casual 169, angry 69, lazy 68, sexy 31 |
| `you got` | 2 | casual 21, angry 1 |
| `it is` | 4 | casual 79, lazy 36, angry 7, sexy 4 |

## 4. Opener maps

- assistant pos 0 (n=9135): a 8.1%, the 3.8%, did 2.4%, how 2.3%, was 1.9%, that 1.9%
- assistant pos 1 (n=9135): the 11.6%, a 2.4%, you 1.9%, is 1.9%, does 1.3%, your 1.1%
- assistant pos 2 (n=9134): the 6.4%, a 3.0%, is 2.8%, are 1.9%, for 1.7%, of 1.7%
- assistant pos last (n=9135): it 4.1%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9135): the 13.9%, my 10.2%, our 8.2%, i 6.6%, we 4.5%, you 3.5%
- user pos 1 (n=9072): the 3.6%, you 2.5%, a 2.0%, was 1.2%, did 1.1%, got 1.0%
- user pos 2 (n=8983): the 7.2%, a 3.0%, is 1.9%, you 1.6%, my 1.5%, and 1.3%
- user pos last (n=9135): again 2.5%, it 2.0%, now 1.4%, week 1.3%, night 1.2%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.8%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 938 |
| lazy | 1 / 2155 |

