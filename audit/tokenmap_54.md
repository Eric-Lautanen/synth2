# synth2 token-attractor map

Generated 2026-10-18 15:34  |  corpus 6746 rows, **9001 assistant turns**, 9001 user turns
Probe: `probe_out54_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-18T11:35:40

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.7% | 3.7% | +0.0 |
| `the`-opener (user) | 13.8% | 13.9% | +0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `did you` | 10% | 12% | 4x | 4x |
| `is a` | - | 12% | - | 2x |
| `you get` | 5% | 7% | 8x | 10x |
| `going to` | - | 5% | - | 16x |
| `is it` | - | 7% | - | 6x |
| `a bit` | - | 5% | - | 11x |
| `a win` | - | 3% | - | 25x |
| `the front desk` | - | 3% | - | 23x |
| `i got` | - | 3% | - | 21x |
| `does not` | - | 3% | - | 20x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.7% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 39 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `did you` | 251 | 278.9 | 274.4 | 12% | 4x | casual 192, angry 28, sexy 26 |
| `is a` | 451 | 501.1 | 65.5 | 12% | 2x | angry 208, casual 121, lazy 115 |
| `you get` | 59 | 65.5 | 56.7 | 7% | 10x | casual 49, angry 5, lazy 5 |
| `going to` | 29 | 32.2 | 15.6 | 5% | 16x | casual 18, angry 6, lazy 5 |
| `is it` | 109 | 121.1 | 24.4 | 7% | 6x | casual 100, angry 7, sexy 2 |
| `a bit` | 40 | 44.4 | 35.6 | 5% | 11x | casual 38, angry 1, lazy 1 |
| `a win` | 12 | 13.3 | 4.4 | 3% | 25x | casual 10, lazy 1, sexy 1 |
| `the front desk` | 13 | 14.4 | 5.6 | 3% | 23x | angry 8, lazy 4, casual 1 |
| `i got` | 14 | 15.6 | 50.0 | 3% | 21x | casual 13, lazy 1 |
| `does not` | 15 | 16.7 | 10.0 | 3% | 20x | casual 6, angry 5, lazy 4 |
| `is your` | 16 | 17.8 | 14.4 | 3% | 19x | casual 10, angry 4, sexy 2 |
| `are just` | 18 | 20.0 | 2.2 | 3% | 17x | lazy 14, angry 3, casual 1 |
| `a real` | 105 | 116.7 | 48.9 | 5% | 4x | casual 82, angry 13, lazy 10 |
| `just a` | 33 | 36.7 | 22.2 | 3% | 9x | casual 22, angry 7, lazy 4 |
| `or a` | 34 | 37.8 | 1.1 | 3% | 9x | casual 25, lazy 4, sexy 3 |
| `a month` | 34 | 37.8 | 37.8 | 3% | 9x | casual 20, lazy 7, angry 6 |
| `way to` | 35 | 38.9 | 2.2 | 3% | 9x | casual 17, angry 11, lazy 6 |
| `is just` | 37 | 41.1 | 3.3 | 3% | 8x | lazy 20, angry 11, casual 6 |
| `the good` | 42 | 46.7 | 18.9 | 3% | 7x | lazy 26, casual 14, angry 1 |
| `i have` | 51 | 56.7 | 86.7 | 3% | 6x | casual 35, lazy 12, sexy 4 |
| `is the` | 421 | 467.7 | 76.7 | 5% | 1x | casual 250, lazy 116, angry 49 |
| `with a` | 102 | 113.3 | 81.1 | 3% | 3x | casual 40, lazy 34, angry 24 |
| `are you` | 113 | 125.5 | 74.4 | 3% | 3x | casual 92, angry 12, sexy 8 |
| `they do` | 8 | 8.9 | 4.4 | 2% | 19x | casual 5, angry 2, lazy 1 |
| `the wait` | 8 | 8.9 | 8.9 | 2% | 19x | lazy 4, casual 3, sexy 1 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.4 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.1 | casual 10, lazy 1 |
| `at this point` | 3 | 12 | 13.9 | lazy 5, casual 4, sexy 2 |
| `have you tried` | 3 | 15 | 13.7 | casual 15 |
| `the front desk` | 3 | 13 | 13.2 | angry 8, lazy 4, casual 1 |
| `the post office` | 3 | 8 | 12.9 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.6 | casual 9, lazy 2 |
| `did they say` | 3 | 8 | 12.4 | angry 4, casual 4 |
| `feels like a` | 3 | 9 | 12.3 | casual 3, lazy 3, angry 2 |
| `two hours of` | 3 | 10 | 12.2 | angry 4, lazy 4, casual 2 |
| `an hour of` | 3 | 12 | 12.1 | angry 6, casual 2, lazy 2 |
| `did they really` | 3 | 11 | 11.9 | angry 11 |
| `fell asleep` | 2 | 8 | 11.6 | casual 4, lazy 4 |
| `for an hour` | 3 | 12 | 11.6 | casual 8, sexy 2, angry 1 |
| `have you got` | 3 | 16 | 11.6 | casual 16 |
| `ice cream` | 2 | 8 | 11.6 | lazy 6, casual 1, sexy 1 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `a phone call` | 3 | 8 | 11.5 | casual 5, lazy 2, angry 1 |
| `falling asleep` | 2 | 9 | 11.3 | sexy 8, lazy 1 |
| `has it been` | 3 | 8 | 11.2 | casual 8 |
| `feel like a` | 3 | 10 | 11.2 | lazy 6, casual 3, sexy 1 |
| `how long did` | 3 | 13 | 11.2 | casual 9, angry 3, sexy 1 |
| `a couple of` | 3 | 12 | 11.0 | casual 11, angry 1 |
| `did you find` | 3 | 9 | 10.8 | casual 9 |
| `did you get` | 3 | 44 | 10.6 | casual 40, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `did you` | 4 | casual 192, angry 28, sexy 26, lazy 5 |
| `is a` | 4 | angry 208, casual 121, lazy 115, sexy 7 |
| `you get` | 3 | casual 49, angry 5, lazy 5 |
| `going to` | 3 | casual 18, angry 6, lazy 5 |
| `is it` | 3 | casual 100, angry 7, sexy 2 |
| `a bit` | 3 | casual 38, angry 1, lazy 1 |
| `a win` | 3 | casual 10, lazy 1, sexy 1 |
| `the front desk` | 3 | angry 8, lazy 4, casual 1 |
| `i got` | 2 | casual 13, lazy 1 |
| `does not` | 3 | casual 6, angry 5, lazy 4 |
| `is your` | 3 | casual 10, angry 4, sexy 2 |
| `are just` | 3 | lazy 14, angry 3, casual 1 |
| `a real` | 3 | casual 82, angry 13, lazy 10 |
| `just a` | 3 | casual 22, angry 7, lazy 4 |
| `or a` | 4 | casual 25, lazy 4, sexy 3, angry 2 |
| `a month` | 4 | casual 20, lazy 7, angry 6, sexy 1 |
| `way to` | 4 | casual 17, angry 11, lazy 6, sexy 1 |
| `is just` | 3 | lazy 20, angry 11, casual 6 |
| `the good` | 4 | lazy 26, casual 14, angry 1, sexy 1 |
| `i have` | 3 | casual 35, lazy 12, sexy 4 |
| `is the` | 4 | casual 250, lazy 116, angry 49, sexy 6 |
| `with a` | 4 | casual 40, lazy 34, angry 24, sexy 4 |
| `are you` | 4 | casual 92, angry 12, sexy 8, lazy 1 |
| `they do` | 3 | casual 5, angry 2, lazy 1 |
| `the wait` | 3 | lazy 4, casual 3, sexy 1 |

## 4. Opener maps

- assistant pos 0 (n=9001): a 8.1%, the 3.7%, did 2.4%, how 2.3%, was 1.9%, that 1.9%
- assistant pos 1 (n=9001): the 11.7%, a 2.4%, you 2.0%, is 1.9%, does 1.3%, your 1.1%
- assistant pos 2 (n=9000): the 6.2%, a 3.0%, is 2.9%, are 1.9%, of 1.7%, for 1.7%
- assistant pos last (n=9001): it 4.0%, now 1.6%, time 1.2%, you 1.2%, one 1.0%, again 1.0%
- user pos 0 (n=9001): the 13.9%, my 10.3%, our 8.2%, i 6.7%, we 4.3%, you 3.2%
- user pos 1 (n=8938): the 3.6%, you 2.6%, a 2.1%, was 1.2%, did 1.1%, is 1.0%
- user pos 2 (n=8849): the 7.1%, a 2.9%, is 1.9%, you 1.6%, my 1.5%, and 1.3%
- user pos last (n=9001): again 2.5%, it 2.0%, now 1.4%, week 1.4%, night 1.3%, morning 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.9%**; model outputs: **6.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 437 / 3881 |
| sexy | 5 / 804 |
| lazy | 1 / 2155 |

