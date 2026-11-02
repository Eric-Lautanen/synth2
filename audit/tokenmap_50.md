# synth2 token-attractor map

Generated 2026-10-18 02:53  |  corpus 6498 rows, **8733 assistant turns**, 8733 user turns
Probe: `probe_out50_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T00:17:16

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.3% | 3.5% | +0.1 |
| `the`-opener (user) | 13.5% | 13.6% | +0.1 |
| copula-only | 0.6% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a couple of` | - | 5% | - | 36x |
| `you get` | 5% | 7% | 7x | 10x |
| `the weekend` | - | 5% | - | 23x |
| `the back` | - | 5% | - | 22x |
| `this time` | 5% | 5% | 9x | 9x |
| `of the` | - | 7% | - | 4x |
| `end of` | - | 3% | - | 36x |
| `been a` | - | 3% | - | 36x |
| `no plans` | - | 3% | - | 32x |
| `what did` | - | 5% | - | 7x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.5% | < 12% |
| `the`-opener (user) | 13.6% | n/a |
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
| `a couple of` | 12 | 13.7 | 5.7 | 5% | 36x | casual 11, angry 1 |
| `you get` | 59 | 67.6 | 58.4 | 7% | 10x | casual 49, angry 5, lazy 5 |
| `the weekend` | 19 | 21.8 | 44.7 | 5% | 23x | casual 15, lazy 4 |
| `the back` | 20 | 22.9 | 27.5 | 5% | 22x | casual 14, lazy 5, angry 1 |
| `this time` | 50 | 57.3 | 18.3 | 5% | 9x | casual 42, angry 6, lazy 2 |
| `of the` | 162 | 185.5 | 126.0 | 7% | 4x | casual 84, lazy 39, angry 29 |
| `end of` | 8 | 9.2 | 8.0 | 3% | 36x | lazy 4, casual 3, angry 1 |
| `been a` | 8 | 9.2 | 4.6 | 3% | 36x | casual 7, angry 1 |
| `no plans` | 9 | 10.3 | 1.1 | 3% | 32x | casual 7, lazy 2 |
| `what did` | 63 | 72.1 | 46.9 | 5% | 7x | casual 41, angry 19, sexy 2 |
| `no idea` | 12 | 13.7 | 9.2 | 3% | 24x | casual 10, lazy 2 |
| `have been` | 18 | 20.6 | 44.7 | 3% | 16x | casual 13, lazy 4, angry 1 |
| `i know` | 19 | 21.8 | 14.9 | 3% | 15x | casual 16, lazy 2, sexy 1 |
| `is it` | 109 | 124.8 | 25.2 | 5% | 4x | casual 100, angry 7, sexy 2 |
| `in the morning` | 22 | 25.2 | 18.3 | 3% | 13x | casual 10, angry 7, lazy 4 |
| `the way` | 26 | 29.8 | 21.8 | 3% | 11x | casual 21, lazy 4, angry 1 |
| `is the` | 418 | 478.6 | 79.0 | 7% | 1x | casual 250, lazy 116, angry 49 |
| `going to` | 29 | 33.2 | 16.0 | 3% | 10x | casual 18, angry 6, lazy 5 |
| `the rain` | 37 | 42.4 | 35.5 | 3% | 8x | casual 21, lazy 8, angry 6 |
| `did it` | 40 | 45.8 | 14.9 | 3% | 7x | casual 34, lazy 4, angry 2 |
| `a bit` | 40 | 45.8 | 36.6 | 3% | 7x | casual 38, angry 1, lazy 1 |
| `the car` | 41 | 46.9 | 43.5 | 3% | 7x | casual 31, lazy 9, angry 1 |
| `how long` | 46 | 52.7 | 16.0 | 3% | 6x | casual 30, angry 9, sexy 6 |
| `for the` | 237 | 271.4 | 255.4 | 5% | 2x | casual 135, angry 64, lazy 24 |
| `did you` | 242 | 277.1 | 282.8 | 5% | 2x | casual 192, angry 28, sexy 17 |

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
| `an hour of` | 3 | 12 | 12.2 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.8 | angry 11 |
| `fell asleep` | 2 | 8 | 11.7 | casual 4, lazy 4 |
| `for an hour` | 3 | 11 | 11.6 | casual 8, angry 1, lazy 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `sounds like a` | 3 | 8 | 11.4 | casual 6, angry 1, sexy 1 |
| `falling asleep` | 2 | 8 | 11.3 | sexy 7, lazy 1 |
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
| `a couple of` | 2 | casual 11, angry 1 |
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `the weekend` | 2 | casual 15, lazy 4 |
| `the back` | 3 | casual 14, lazy 5, angry 1 |
| `this time` | 3 | casual 42, angry 6, lazy 2 |
| `of the` | 4 | casual 84, lazy 39, angry 29, sexy 10 |
| `end of` | 3 | lazy 4, casual 3, angry 1 |
| `been a` | 2 | casual 7, angry 1 |
| `no plans` | 2 | casual 7, lazy 2 |
| `what did` | 4 | casual 41, angry 19, sexy 2, lazy 1 |
| `no idea` | 2 | casual 10, lazy 2 |
| `have been` | 3 | casual 13, lazy 4, angry 1 |
| `i know` | 3 | casual 16, lazy 2, sexy 1 |
| `is it` | 3 | casual 100, angry 7, sexy 2 |
| `in the morning` | 4 | casual 10, angry 7, lazy 4, sexy 1 |
| `the way` | 3 | casual 21, lazy 4, angry 1 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 3 |
| `going to` | 3 | casual 18, angry 6, lazy 5 |
| `the rain` | 4 | casual 21, lazy 8, angry 6, sexy 2 |
| `did it` | 3 | casual 34, lazy 4, angry 2 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `the car` | 3 | casual 31, lazy 9, angry 1 |
| `how long` | 4 | casual 30, angry 9, sexy 6, lazy 1 |
| `for the` | 4 | casual 135, angry 64, lazy 24, sexy 14 |
| `did you` | 4 | casual 192, angry 28, sexy 17, lazy 5 |

## 4. Opener maps

- assistant pos 0 (n=8733): a 7.9%, the 3.5%, did 2.5%, how 2.4%, was 2.0%, that 1.9%
- assistant pos 1 (n=8733): the 11.7%, a 2.4%, you 2.0%, is 2.0%, does 1.3%, your 1.1%
- assistant pos 2 (n=8732): the 6.2%, a 3.1%, is 3.0%, are 1.9%, of 1.7%, for 1.6%
- assistant pos last (n=8733): it 4.1%, now 1.5%, time 1.2%, you 1.2%, again 1.0%, one 1.0%
- user pos 0 (n=8733): the 13.6%, my 10.5%, our 8.1%, i 6.7%, we 3.7%, they 3.2%
- user pos 1 (n=8670): the 3.7%, you 2.6%, a 2.1%, was 1.3%, did 1.1%, is 1.0%
- user pos 2 (n=8581): the 6.9%, a 3.0%, is 2.0%, you 1.7%, my 1.5%, and 1.4%
- user pos last (n=8733): again 2.5%, it 2.0%, now 1.5%, week 1.4%, night 1.2%, today 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **5.1%**; model outputs: **6.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 536 |
| lazy | 1 / 2155 |

