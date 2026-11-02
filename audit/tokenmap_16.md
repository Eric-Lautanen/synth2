# synth2 token-attractor map

Generated 2026-10-11 13:01  |  corpus 2321 rows, **4225 assistant turns**, 4225 user turns
Probe: `probe_out16_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-10T22:15:33

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.1% | 2.7% | +0.5 |
| `the`-opener (user) | 8.0% | 7.9% | -0.1 |
| copula-only | 0.2% | 0.4% | +0.2 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `at all` | - | 7% | - | 8x |
| `it is` | - | 8% | - | 4x |
| `did you` | 10% | 10% | 2x | 2x |
| `that is` | - | 7% | - | 3x |
| `how many` | - | 5% | - | 6x |
| `it the` | 5% | 5% | 6x | 6x |
| `is the` | - | 8% | - | 1x |
| `the first` | - | 5% | - | 5x |
| `to do it` | - | 3% | - | 18x |
| `the long` | - | 3% | - | 18x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 7.9% | n/a |
| copula-only turns | 0.4% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
| probe outputs carrying a top attractor | 43 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `at all` | 36 | 85.2 | 33.1 | 7% | 8x | casual 36 |
| `it is` | 94 | 222.5 | 104.1 | 8% | 4x | casual 79, lazy 15 |
| `did you` | 192 | 454.4 | 489.9 | 10% | 2x | casual 192 |
| `that is` | 82 | 194.1 | 21.3 | 7% | 3x | casual 80, lazy 2 |
| `how many` | 34 | 80.5 | 4.7 | 5% | 6x | casual 33, lazy 1 |
| `it the` | 38 | 89.9 | 21.3 | 5% | 6x | casual 34, lazy 4 |
| `is the` | 264 | 624.9 | 125.4 | 8% | 1x | casual 252, lazy 12 |
| `the first` | 45 | 106.5 | 92.3 | 5% | 5x | casual 40, lazy 5 |
| `to do it` | 8 | 18.9 | 2.4 | 3% | 18x | casual 8 |
| `the long` | 8 | 18.9 | 14.2 | 3% | 18x | casual 7, lazy 1 |
| `anything else` | 8 | 18.9 | 2.4 | 3% | 18x | casual 7, lazy 1 |
| `you had` | 9 | 21.3 | 4.7 | 3% | 16x | casual 9 |
| `i am` | 54 | 127.8 | 66.3 | 5% | 4x | casual 44, lazy 10 |
| `with the` | 55 | 130.2 | 113.6 | 5% | 4x | casual 54, lazy 1 |
| `my mom` | 14 | 33.1 | 23.7 | 3% | 10x | casual 14 |
| `how far` | 14 | 33.1 | 2.4 | 3% | 10x | casual 14 |
| `have you` | 80 | 189.3 | 52.1 | 5% | 3x | casual 80 |
| `after the` | 16 | 37.9 | 16.6 | 3% | 9x | casual 16 |
| `i know` | 17 | 40.2 | 30.8 | 3% | 8x | casual 16, lazy 1 |
| `up to` | 18 | 42.6 | 37.9 | 3% | 8x | casual 18 |
| `it for` | 19 | 45.0 | 30.8 | 3% | 7x | casual 18, lazy 1 |
| `you got` | 21 | 49.7 | 11.8 | 3% | 7x | casual 21 |
| `worth the` | 21 | 49.7 | 11.8 | 3% | 7x | casual 21 |
| `got a` | 21 | 49.7 | 108.9 | 3% | 7x | casual 21 |
| `ten minutes` | 22 | 52.1 | 47.3 | 3% | 6x | casual 20, lazy 2 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 8 | 17.8 | casual 7, lazy 1 |
| `are you going to` | 4 | 8 | 16.5 | casual 8 |
| `an early night` | 3 | 10 | 15.3 | casual 10 |
| `best kind of` | 3 | 10 | 14.2 | casual 8, lazy 2 |
| `have you tried` | 3 | 15 | 13.1 | casual 15 |
| `for an hour` | 3 | 8 | 12.6 | casual 8 |
| `the best kind` | 3 | 13 | 11.7 | casual 12, lazy 1 |
| `i have been` | 3 | 10 | 11.5 | casual 9, lazy 1 |
| `a couple of` | 3 | 11 | 11.4 | casual 11 |
| `did you get` | 3 | 40 | 11.1 | casual 40 |
| `have you got` | 3 | 16 | 11.1 | casual 16 |
| `how long did` | 3 | 9 | 11.1 | casual 9 |
| `did you find` | 3 | 9 | 11.1 | casual 9 |
| `has it been` | 3 | 8 | 10.6 | casual 8 |
| `are you going` | 3 | 15 | 10.5 | casual 15 |
| `a lot of` | 3 | 8 | 10.3 | casual 7, lazy 1 |
| `and i am` | 3 | 8 | 10.1 | casual 7, lazy 1 |
| `do you go` | 3 | 8 | 9.9 | casual 8 |
| `post office` | 2 | 8 | 9.9 | casual 8 |
| `these days` | 2 | 8 | 9.9 | casual 8 |
| `a bit of` | 3 | 15 | 9.8 | casual 15 |
| `washing machine` | 2 | 11 | 9.8 | casual 11 |
| `what did you` | 3 | 26 | 9.7 | casual 26 |
| `did you go` | 3 | 13 | 9.6 | casual 13 |
| `on a saturday` | 3 | 9 | 9.4 | casual 9 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `at all` | 1 | casual 36 |
| `it is` | 2 | casual 79, lazy 15 |
| `did you` | 1 | casual 192 |
| `that is` | 2 | casual 80, lazy 2 |
| `how many` | 2 | casual 33, lazy 1 |
| `it the` | 2 | casual 34, lazy 4 |
| `is the` | 2 | casual 252, lazy 12 |
| `the first` | 2 | casual 40, lazy 5 |
| `to do it` | 1 | casual 8 |
| `the long` | 2 | casual 7, lazy 1 |
| `anything else` | 2 | casual 7, lazy 1 |
| `you had` | 1 | casual 9 |
| `i am` | 2 | casual 44, lazy 10 |
| `with the` | 2 | casual 54, lazy 1 |
| `my mom` | 1 | casual 14 |
| `how far` | 1 | casual 14 |
| `have you` | 1 | casual 80 |
| `after the` | 1 | casual 16 |
| `i know` | 2 | casual 16, lazy 1 |
| `up to` | 1 | casual 18 |
| `it for` | 2 | casual 18, lazy 1 |
| `you got` | 1 | casual 21 |
| `worth the` | 1 | casual 21 |
| `got a` | 1 | casual 21 |
| `ten minutes` | 2 | casual 20, lazy 2 |

## 4. Opener maps

- assistant pos 0 (n=4225): a 7.8%, that 3.5%, haha 3.1%, the 2.7%, i 2.1%, is 1.4%
- assistant pos 1 (n=4225): the 12.1%, a 2.9%, is 2.9%, you 1.9%, it 1.6%, and 1.3%
- assistant pos 2 (n=4224): the 7.3%, is 4.6%, a 2.7%, of 1.9%, for 1.6%, and 1.5%
- assistant pos last (n=4225): it 5.5%, now 1.8%, time 1.5%, one 1.4%, then 1.3%, again 1.2%
- user pos 0 (n=4225): the 7.9%, did 4.9%, i 4.4%, my 4.0%, a 3.5%, what 2.5%
- user pos 1 (n=4162): the 6.9%, you 4.6%, a 4.2%, did 2.0%, was 1.9%, to 1.9%
- user pos 2 (n=4076): the 6.4%, a 3.9%, and 2.5%, you 2.5%, is 1.8%, one 1.5%
- user pos last (n=4225): it 2.3%, again 2.2%, week 1.8%, now 1.6%, today 1.5%, weekend 1.5%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **10.4%**; model outputs: **16.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 344 |

