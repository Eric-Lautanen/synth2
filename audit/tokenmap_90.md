# synth2 token-attractor map

Generated 2026-10-24 08:17  |  corpus 8978 rows, **11413 assistant turns**, 11413 user turns
Probe: `probe_out90_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-24T05:24:29

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.8% | 5.9% | +0.1 |
| `the`-opener (user) | 14.7% | 14.7% | +0.1 |
| copula-only | 0.8% | 0.7% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `going to` | - | 7% | - | 24x |
| `i am` | - | 7% | - | 11x |
| `is a` | - | 10% | - | 2x |
| `the same` | 5% | 7% | 5x | 6x |
| `the morning` | - | 5% | - | 15x |
| `when does` | - | 3% | - | 48x |
| `to sleep` | - | 3% | - | 48x |
| `no shame` | - | 3% | - | 48x |
| `much better` | - | 3% | - | 42x |
| `how many` | - | 5% | - | 9x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.9% | < 12% |
| `the`-opener (user) | 14.7% | n/a |
| copula-only turns | 0.7% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `going to` | 32 | 28.0 | 12.3 | 7% | 24x | casual 18, angry 6, lazy 5 |
| `i am` | 68 | 59.6 | 35.0 | 7% | 11x | casual 46, lazy 11, sexy 10 |
| `is a` | 522 | 457.4 | 66.6 | 10% | 2x | angry 222, casual 147, lazy 116 |
| `the same` | 126 | 110.4 | 120.9 | 7% | 6x | angry 34, casual 34, lazy 29 |
| `the morning` | 39 | 34.2 | 25.4 | 5% | 15x | casual 18, lazy 11, angry 5 |
| `when does` | 8 | 7.0 | 0.0 | 3% | 48x | formal 4, angry 2, sexy 2 |
| `to sleep` | 8 | 7.0 | 7.9 | 3% | 48x | angry 3, casual 2, lazy 2 |
| `no shame` | 8 | 7.0 | 1.8 | 3% | 48x | lazy 4, sexy 3, casual 1 |
| `much better` | 9 | 7.9 | 0.9 | 3% | 42x | casual 7, formal 1, lazy 1 |
| `how many` | 65 | 57.0 | 7.0 | 5% | 9x | casual 35, angry 13, sexy 8 |
| `is the` | 497 | 435.5 | 77.1 | 8% | 2x | casual 292, lazy 116, angry 50 |
| `for a` | 225 | 197.1 | 168.2 | 7% | 3x | angry 93, casual 66, lazy 23 |
| `a gift` | 14 | 12.3 | 1.8 | 3% | 27x | casual 5, lazy 5, angry 2 |
| `a time` | 16 | 14.0 | 3.5 | 3% | 24x | lazy 5, casual 4, formal 4 |
| `you going` | 17 | 14.9 | 4.4 | 3% | 22x | casual 15, angry 2 |
| `the weekend` | 19 | 16.6 | 34.2 | 3% | 20x | casual 14, lazy 4, sexy 1 |
| `i know` | 19 | 16.6 | 13.1 | 3% | 20x | casual 15, lazy 2, sexy 2 |
| `this morning` | 20 | 17.5 | 65.7 | 3% | 19x | casual 16, angry 2, lazy 1 |
| `is it` | 125 | 109.5 | 23.7 | 5% | 5x | casual 103, formal 11, angry 7 |
| `just the` | 30 | 26.3 | 10.5 | 3% | 13x | casual 19, lazy 6, angry 3 |
| `get the` | 30 | 26.3 | 18.4 | 3% | 13x | casual 16, lazy 8, angry 2 |
| `that is` | 166 | 145.4 | 12.3 | 5% | 3x | casual 96, lazy 26, sexy 25 |
| `to the` | 182 | 159.5 | 165.6 | 5% | 3x | casual 70, sexy 34, lazy 32 |
| `way to` | 36 | 31.5 | 2.6 | 3% | 11x | casual 17, angry 11, lazy 6 |
| `the whole` | 188 | 164.7 | 113.9 | 5% | 3x | lazy 83, casual 57, angry 32 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.9 | casual 8, angry 2 |
| `faster than any` | 3 | 8 | 16.6 | lazy 6, angry 1, formal 1 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `in the middle of` | 4 | 9 | 16.0 | angry 4, formal 2, lazy 2 |
| `have you tried` | 3 | 15 | 14.0 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `the front desk` | 3 | 14 | 12.4 | angry 8, lazy 4, casual 1 |
| `an hour of` | 3 | 18 | 12.4 | angry 6, formal 4, casual 3 |
| `two hours of` | 3 | 11 | 12.1 | angry 4, lazy 4, casual 2 |
| `counts as a` | 3 | 12 | 12.1 | formal 5, casual 2, lazy 2 |
| `feels like a` | 3 | 9 | 12.1 | casual 3, lazy 3, angry 1 |
| `did they really` | 3 | 11 | 12.1 | angry 11 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `sounds like a` | 3 | 11 | 11.8 | casual 7, formal 2, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `without a single` | 3 | 10 | 11.6 | angry 5, formal 5 |
| `ice cream` | 2 | 10 | 11.5 | lazy 6, sexy 3, casual 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.2 | sexy 8, lazy 1 |
| `feel like a` | 3 | 11 | 11.0 | lazy 6, casual 4, sexy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `going to` | 5 | casual 18, angry 6, lazy 5, sexy 2 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `is a` | 5 | angry 222, casual 147, lazy 116, formal 22 |
| `the same` | 5 | angry 34, casual 34, lazy 29, formal 15 |
| `the morning` | 5 | casual 18, lazy 11, angry 5, formal 3 |
| `when does` | 3 | formal 4, angry 2, sexy 2 |
| `to sleep` | 4 | angry 3, casual 2, lazy 2, sexy 1 |
| `no shame` | 3 | lazy 4, sexy 3, casual 1 |
| `much better` | 3 | casual 7, formal 1, lazy 1 |
| `how many` | 5 | casual 35, angry 13, sexy 8, formal 7 |
| `is the` | 5 | casual 292, lazy 116, angry 50, formal 23 |
| `for a` | 5 | angry 93, casual 66, lazy 23, sexy 23 |
| `a gift` | 4 | casual 5, lazy 5, angry 2, sexy 2 |
| `a time` | 5 | lazy 5, casual 4, formal 4, sexy 2 |
| `you going` | 2 | casual 15, angry 2 |
| `the weekend` | 3 | casual 14, lazy 4, sexy 1 |
| `i know` | 3 | casual 15, lazy 2, sexy 2 |
| `this morning` | 4 | casual 16, angry 2, lazy 1, sexy 1 |
| `is it` | 4 | casual 103, formal 11, angry 7, sexy 4 |
| `just the` | 4 | casual 19, lazy 6, angry 3, formal 2 |
| `get the` | 5 | casual 16, lazy 8, angry 2, formal 2 |
| `that is` | 5 | casual 96, lazy 26, sexy 25, angry 17 |
| `to the` | 5 | casual 70, sexy 34, lazy 32, angry 27 |
| `way to` | 4 | casual 17, angry 11, lazy 6, sexy 2 |
| `the whole` | 5 | lazy 83, casual 57, angry 32, sexy 13 |

## 4. Opener maps

- assistant pos 0 (n=11413): a 10.2%, the 5.9%, how 2.4%, does 2.2%, did 2.2%, why 1.8%
- assistant pos 1 (n=11413): the 11.1%, a 2.0%, is 1.7%, you 1.6%, does 1.6%, on 0.9%
- assistant pos 2 (n=11412): the 7.4%, a 3.0%, is 2.6%, on 2.0%, of 1.9%, for 1.8%
- assistant pos last (n=11413): it 3.8%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11413): the 14.7%, my 9.7%, our 8.8%, i 6.6%, we 6.0%, you 5.2%
- user pos 1 (n=11350): the 3.1%, you 2.0%, a 1.6%, got 1.0%, is 1.0%, was 1.0%
- user pos 2 (n=11260): the 7.9%, a 3.7%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11413): it 2.2%, again 2.1%, now 1.2%, week 1.2%, morning 1.0%, night 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.7%**; model outputs: **5.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

