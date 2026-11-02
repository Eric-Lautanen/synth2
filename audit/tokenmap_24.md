# synth2 token-attractor map

Generated 2026-10-15 00:18  |  corpus 3254 rows, **5233 assistant turns**, 5233 user turns
Probe: `probe_out24_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-14T23:02:14

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.7% | 2.7% | -0.0 |
| `the`-opener (user) | 9.0% | 9.4% | +0.4 |
| copula-only | 0.5% | 0.5% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the neighbor` | - | 5% | - | 26x |
| `i have` | 5% | 7% | 6x | 8x |
| `to be` | - | 5% | - | 15x |
| `this morning` | 3% | 5% | 8x | 12x |
| `on the` | - | 8% | - | 2x |
| `the rain` | - | 5% | - | 10x |
| `of the` | - | 7% | - | 3x |
| `a bit` | - | 5% | - | 7x |
| `out of` | - | 5% | - | 6x |
| `the bed` | - | 3% | - | 22x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 9.4% | n/a |
| copula-only turns | 0.5% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
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
| `the neighbor` | 10 | 19.1 | 7.6 | 5% | 26x | casual 9, lazy 1 |
| `i have` | 46 | 87.9 | 99.4 | 7% | 8x | casual 35, lazy 11 |
| `to be` | 18 | 34.4 | 22.9 | 5% | 15x | casual 13, lazy 5 |
| `this morning` | 22 | 42.0 | 110.8 | 5% | 12x | casual 21, lazy 1 |
| `on the` | 176 | 336.3 | 301.9 | 8% | 2x | casual 151, lazy 25 |
| `the rain` | 25 | 47.8 | 28.7 | 5% | 10x | casual 21, lazy 4 |
| `of the` | 103 | 196.8 | 149.1 | 7% | 3x | casual 84, lazy 19 |
| `a bit` | 39 | 74.5 | 61.2 | 5% | 7x | casual 39 |
| `out of` | 42 | 80.3 | 82.2 | 5% | 6x | casual 34, lazy 8 |
| `the bed` | 8 | 15.3 | 5.7 | 3% | 22x | casual 4, lazy 4 |
| `luck with` | 8 | 15.3 | 5.7 | 3% | 22x | casual 8 |
| `of those` | 9 | 17.2 | 9.6 | 3% | 19x | casual 7, lazy 2 |
| `nothing on` | 9 | 17.2 | 1.9 | 3% | 19x | casual 8, lazy 1 |
| `i am` | 55 | 105.1 | 61.2 | 5% | 5x | casual 44, lazy 11 |
| `it's been` | 10 | 19.1 | 9.6 | 3% | 17x | casual 10 |
| `was a` | 11 | 21.0 | 26.8 | 3% | 16x | casual 11 |
| `good luck` | 11 | 21.0 | 0.0 | 3% | 16x | casual 9, lazy 2 |
| `a two` | 11 | 21.0 | 9.6 | 3% | 16x | casual 8, lazy 3 |
| `with the` | 63 | 120.4 | 97.5 | 5% | 4x | casual 54, lazy 9 |
| `the first` | 63 | 120.4 | 91.7 | 5% | 4x | casual 40, lazy 23 |
| `there a` | 14 | 26.8 | 1.9 | 3% | 12x | casual 13, lazy 1 |
| `my mom` | 14 | 26.8 | 19.1 | 3% | 12x | casual 14 |
| `i got` | 14 | 26.8 | 55.4 | 3% | 12x | casual 13, lazy 1 |
| `a saturday` | 14 | 26.8 | 3.8 | 3% | 12x | casual 13, lazy 1 |
| `have you` | 80 | 152.9 | 42.0 | 5% | 3x | casual 80 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 10 | 17.9 | casual 7, lazy 3 |
| `are you going to` | 4 | 8 | 16.4 | casual 8 |
| `every single time` | 3 | 9 | 16.0 | lazy 7, casual 2 |
| `an early night` | 3 | 10 | 15.1 | casual 10 |
| `best kind of` | 3 | 12 | 14.3 | casual 8, lazy 4 |
| `at this point` | 3 | 9 | 13.9 | lazy 5, casual 4 |
| `have you tried` | 3 | 15 | 13.4 | casual 15 |
| `for an hour` | 3 | 9 | 12.7 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `i have been` | 3 | 11 | 12.0 | casual 9, lazy 2 |
| `a couple of` | 3 | 11 | 11.6 | casual 11 |
| `how long did` | 3 | 9 | 11.5 | casual 9 |
| `the best kind` | 3 | 15 | 11.5 | casual 12, lazy 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `did you find` | 3 | 9 | 11.3 | casual 9 |
| `did you get` | 3 | 42 | 11.2 | casual 40, lazy 2 |
| `has it been` | 3 | 8 | 10.9 | casual 8 |
| `a lot of` | 3 | 8 | 10.4 | casual 7, lazy 1 |
| `and i am` | 3 | 8 | 10.3 | casual 7, lazy 1 |
| `are you going` | 3 | 15 | 10.2 | casual 15 |
| `what did you` | 3 | 27 | 10.1 | casual 26, lazy 1 |
| `do you go` | 3 | 8 | 10.1 | casual 8 |
| `a bit of` | 3 | 15 | 10.0 | casual 15 |
| `earn their` | 2 | 13 | 9.9 | lazy 12, casual 1 |
| `post office` | 2 | 8 | 9.8 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the neighbor` | 2 | casual 9, lazy 1 |
| `i have` | 2 | casual 35, lazy 11 |
| `to be` | 2 | casual 13, lazy 5 |
| `this morning` | 2 | casual 21, lazy 1 |
| `on the` | 2 | casual 151, lazy 25 |
| `the rain` | 2 | casual 21, lazy 4 |
| `of the` | 2 | casual 84, lazy 19 |
| `a bit` | 1 | casual 39 |
| `out of` | 2 | casual 34, lazy 8 |
| `the bed` | 2 | casual 4, lazy 4 |
| `luck with` | 1 | casual 8 |
| `of those` | 2 | casual 7, lazy 2 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `i am` | 2 | casual 44, lazy 11 |
| `it's been` | 1 | casual 10 |
| `was a` | 1 | casual 11 |
| `good luck` | 2 | casual 9, lazy 2 |
| `a two` | 2 | casual 8, lazy 3 |
| `with the` | 2 | casual 54, lazy 9 |
| `the first` | 2 | casual 40, lazy 23 |
| `there a` | 2 | casual 13, lazy 1 |
| `my mom` | 1 | casual 14 |
| `i got` | 2 | casual 13, lazy 1 |
| `a saturday` | 2 | casual 13, lazy 1 |
| `have you` | 1 | casual 80 |

## 4. Opener maps

- assistant pos 0 (n=5233): a 7.4%, that 2.8%, the 2.7%, haha 2.5%, i 1.8%, did 1.2%
- assistant pos 1 (n=5233): the 10.0%, is 2.5%, a 2.4%, you 1.6%, it 1.4%, and 1.1%
- assistant pos 2 (n=5232): the 6.5%, is 4.1%, a 2.3%, are 2.1%, of 1.7%, for 1.3%
- assistant pos last (n=5233): it 5.6%, now 1.7%, time 1.5%, one 1.3%, then 1.1%, again 1.0%
- user pos 0 (n=5233): the 9.4%, my 6.8%, i 5.9%, our 4.9%, did 4.5%, a 3.3%
- user pos 1 (n=5170): the 5.7%, you 4.0%, a 3.4%, was 1.8%, did 1.8%, to 1.7%
- user pos 2 (n=5081): the 6.8%, a 3.4%, you 2.3%, and 2.0%, is 1.9%, in 1.3%
- user pos last (n=5233): again 2.5%, it 2.1%, now 1.7%, week 1.6%, today 1.5%, weekend 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **8.4%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 1352 |

