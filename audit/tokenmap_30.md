# synth2 token-attractor map

Generated 2026-10-15 14:30  |  corpus 4498 rows, **6572 assistant turns**, 6572 user turns
Probe: `probe_out30_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T12:25:24

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.1% | 3.2% | +0.1 |
| `the`-opener (user) | 11.4% | 11.7% | +0.3 |
| copula-only | 0.5% | 0.6% | +0.1 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `no idea` | - | 7% | - | 37x |
| `to be` | - | 7% | - | 20x |
| `is the` | 7% | 12% | 1x | 2x |
| `i had` | - | 5% | - | 27x |
| `the worst` | 5% | 7% | 7x | 9x |
| `i've been` | - | 5% | - | 22x |
| `whole_thing` | - | 5% | - | 19x |
| `bit of` | 3% | 5% | 13x | 19x |
| `going to` | 3% | 5% | 9x | 13x |
| `a bit` | 7% | 5% | 11x | 8x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.2% | < 12% |
| `the`-opener (user) | 11.7% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 36 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `no idea` | 12 | 18.3 | 12.2 | 7% | 37x | casual 10, lazy 2 |
| `to be` | 22 | 33.5 | 21.3 | 7% | 20x | casual 13, lazy 8, angry 1 |
| `is the` | 390 | 593.4 | 103.5 | 12% | 2x | casual 251, lazy 116, angry 23 |
| `i had` | 12 | 18.3 | 19.8 | 5% | 27x | casual 10, lazy 2 |
| `the worst` | 49 | 74.6 | 10.7 | 7% | 9x | casual 26, lazy 17, angry 6 |
| `i've been` | 15 | 22.8 | 24.3 | 5% | 22x | casual 15 |
| `whole_thing` | 17 | 25.9 | 19.8 | 5% | 19x | casual 8, lazy 8, angry 1 |
| `bit of` | 17 | 25.9 | 13.7 | 5% | 19x | casual 17 |
| `going to` | 26 | 39.6 | 21.3 | 5% | 13x | casual 18, lazy 5, angry 3 |
| `a bit` | 40 | 60.9 | 48.7 | 5% | 8x | casual 39, lazy 1 |
| `for three` | 8 | 12.2 | 15.2 | 3% | 27x | casual 7, lazy 1 |
| `been a` | 8 | 12.2 | 6.1 | 3% | 27x | casual 7, angry 1 |
| `same as` | 9 | 13.7 | 3.0 | 3% | 24x | casual 8, lazy 1 |
| `point of` | 9 | 13.7 | 0.0 | 3% | 24x | lazy 5, casual 4 |
| `my sister` | 9 | 13.7 | 28.9 | 3% | 24x | casual 8, lazy 1 |
| `it gets` | 9 | 13.7 | 7.6 | 3% | 24x | casual 9 |
| `was it` | 67 | 101.9 | 32.0 | 5% | 5x | casual 65, angry 2 |
| `good luck` | 12 | 18.3 | 0.0 | 3% | 18x | casual 9, lazy 2, angry 1 |
| `is going` | 13 | 19.8 | 6.1 | 3% | 17x | casual 11, lazy 2 |
| `of course` | 14 | 21.3 | 3.0 | 3% | 16x | casual 7, angry 6, lazy 1 |
| `you do` | 18 | 27.4 | 22.8 | 3% | 12x | casual 17, angry 1 |
| `what is` | 27 | 41.1 | 18.3 | 3% | 8x | casual 23, angry 2, lazy 2 |
| `all day` | 29 | 44.1 | 25.9 | 3% | 8x | lazy 15, casual 11, angry 3 |
| `the whole` | 157 | 238.9 | 141.5 | 5% | 2x | lazy 83, casual 55, angry 19 |
| `at the` | 163 | 248.0 | 238.9 | 5% | 2x | casual 104, lazy 52, angry 7 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.6 | casual 10, lazy 1 |
| `at this point` | 3 | 9 | 13.8 | lazy 5, casual 4 |
| `have you tried` | 3 | 22 | 13.7 | casual 15, angry 7 |
| `the front desk` | 3 | 8 | 13.1 | lazy 4, angry 3, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `for an hour` | 3 | 9 | 12.3 | casual 8, lazy 1 |
| `i have been` | 3 | 11 | 12.3 | casual 9, lazy 2 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `how long did` | 3 | 12 | 11.6 | casual 9, angry 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.1 | casual 9 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.5 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `group chat` | 2 | 8 | 10.3 | lazy 4, angry 2, casual 2 |
| `a lot of` | 3 | 10 | 10.3 | casual 7, lazy 3 |
| `do you go` | 3 | 8 | 10.1 | casual 8 |
| `what did you` | 3 | 27 | 10.0 | casual 26, lazy 1 |
| `earn their` | 2 | 15 | 10.0 | lazy 14, casual 1 |
| `a bit of` | 3 | 15 | 10.0 | casual 15 |
| `washing machine` | 2 | 12 | 9.9 | casual 11, lazy 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `no idea` | 2 | casual 10, lazy 2 |
| `to be` | 3 | casual 13, lazy 8, angry 1 |
| `is the` | 3 | casual 251, lazy 116, angry 23 |
| `i had` | 2 | casual 10, lazy 2 |
| `the worst` | 3 | casual 26, lazy 17, angry 6 |
| `i've been` | 1 | casual 15 |
| `whole_thing` | 3 | casual 8, lazy 8, angry 1 |
| `bit of` | 1 | casual 17 |
| `going to` | 3 | casual 18, lazy 5, angry 3 |
| `a bit` | 2 | casual 39, lazy 1 |
| `for three` | 2 | casual 7, lazy 1 |
| `been a` | 2 | casual 7, angry 1 |
| `same as` | 2 | casual 8, lazy 1 |
| `point of` | 2 | lazy 5, casual 4 |
| `my sister` | 2 | casual 8, lazy 1 |
| `it gets` | 1 | casual 9 |
| `was it` | 2 | casual 65, angry 2 |
| `good luck` | 3 | casual 9, lazy 2, angry 1 |
| `is going` | 2 | casual 11, lazy 2 |
| `of course` | 3 | casual 7, angry 6, lazy 1 |
| `you do` | 2 | casual 17, angry 1 |
| `what is` | 3 | casual 23, angry 2, lazy 2 |
| `all day` | 3 | lazy 15, casual 11, angry 3 |
| `the whole` | 3 | lazy 83, casual 55, angry 19 |
| `at the` | 3 | casual 104, lazy 52, angry 7 |

## 4. Opener maps

- assistant pos 0 (n=6572): a 7.4%, the 3.2%, that 2.4%, haha 2.0%, did 2.0%, i 1.7%
- assistant pos 1 (n=6572): the 10.3%, a 2.2%, you 2.2%, is 2.1%, it 1.3%, and 1.0%
- assistant pos 2 (n=6571): the 6.1%, is 3.9%, are 2.6%, a 2.3%, of 1.5%, for 1.2%
- assistant pos last (n=6572): it 4.9%, now 1.6%, time 1.5%, one 1.2%, again 1.0%, you 0.9%
- user pos 0 (n=6572): the 11.7%, my 9.2%, our 7.4%, i 7.3%, did 3.9%, we 3.0%
- user pos 1 (n=6509): the 4.8%, you 3.4%, a 2.7%, was 1.5%, did 1.5%, is 1.4%
- user pos 2 (n=6420): the 7.1%, a 3.1%, is 2.5%, you 2.0%, and 1.7%, has 1.2%
- user pos last (n=6572): again 2.9%, it 1.9%, now 1.6%, week 1.6%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.7%**; model outputs: **18.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

