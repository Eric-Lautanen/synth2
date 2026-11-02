# synth2 token-attractor map

Generated 2026-10-15 04:25  |  corpus 3816 rows, **5835 assistant turns**, 5835 user turns
Probe: `probe_out26_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T02:37:09

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.9% | 3.1% | +0.1 |
| `the`-opener (user) | 10.1% | 10.5% | +0.4 |
| copula-only | 0.5% | 0.6% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `an hour` | - | 8% | - | 10x |
| `i know` | 3% | 7% | 11x | 22x |
| `the list` | - | 5% | - | 18x |
| `i did` | - | 5% | - | 13x |
| `on the` | - | 8% | - | 2x |
| `a new` | 5% | 5% | 6x | 6x |
| `whole day` | - | 3% | - | 24x |
| `know it` | - | 3% | - | 24x |
| `the afternoon` | - | 3% | - | 19x |
| `on your` | - | 3% | - | 18x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.1% | < 12% |
| `the`-opener (user) | 10.5% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
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
| `an hour` | 48 | 82.3 | 65.1 | 8% | 10x | casual 34, lazy 14 |
| `i know` | 18 | 30.8 | 22.3 | 7% | 22x | casual 16, lazy 2 |
| `the list` | 16 | 27.4 | 10.3 | 5% | 18x | casual 10, lazy 6 |
| `i did` | 23 | 39.4 | 42.8 | 5% | 13x | casual 19, lazy 4 |
| `on the` | 196 | 335.9 | 301.6 | 8% | 2x | casual 151, lazy 45 |
| `a new` | 48 | 82.3 | 85.7 | 5% | 6x | casual 37, lazy 11 |
| `whole day` | 8 | 13.7 | 5.1 | 3% | 24x | casual 4, lazy 4 |
| `know it` | 8 | 13.7 | 6.9 | 3% | 24x | casual 6, lazy 2 |
| `the afternoon` | 10 | 17.1 | 12.0 | 3% | 19x | casual 5, lazy 5 |
| `on your` | 11 | 18.9 | 10.3 | 3% | 18x | casual 11 |
| `the heating` | 12 | 20.6 | 17.1 | 3% | 16x | casual 10, lazy 2 |
| `has been` | 12 | 20.6 | 61.7 | 3% | 16x | casual 10, lazy 2 |
| `and i'm` | 13 | 22.3 | 20.6 | 3% | 15x | casual 13 |
| `to a` | 14 | 24.0 | 18.9 | 3% | 14x | casual 9, lazy 5 |
| `i got` | 14 | 24.0 | 51.4 | 3% | 14x | casual 13, lazy 1 |
| `yeah the` | 17 | 29.1 | 3.4 | 3% | 11x | casual 16, lazy 1 |
| `the coffee` | 17 | 29.1 | 15.4 | 3% | 11x | lazy 10, casual 7 |
| `a walk` | 18 | 30.8 | 20.6 | 3% | 11x | casual 16, lazy 2 |
| `for a` | 94 | 161.1 | 118.3 | 5% | 3x | casual 74, lazy 20 |
| `for one` | 19 | 32.6 | 1.7 | 3% | 10x | lazy 12, casual 7 |
| `got a` | 22 | 37.7 | 130.2 | 3% | 9x | casual 21, lazy 1 |
| `going to` | 22 | 37.7 | 24.0 | 3% | 9x | casual 18, lazy 4 |
| `of the` | 119 | 203.9 | 144.0 | 5% | 2x | casual 84, lazy 35 |
| `more than` | 25 | 42.8 | 25.7 | 3% | 8x | casual 17, lazy 8 |
| `just a` | 25 | 42.8 | 24.0 | 3% | 8x | casual 22, lazy 3 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 13 | 18.0 | casual 7, lazy 6 |
| `are you going to` | 4 | 8 | 16.3 | casual 8 |
| `every single time` | 3 | 10 | 15.8 | lazy 8, casual 2 |
| `an early night` | 3 | 11 | 14.8 | casual 10, lazy 1 |
| `best kind of` | 3 | 15 | 14.4 | casual 8, lazy 7 |
| `at this point` | 3 | 9 | 13.9 | lazy 5, casual 4 |
| `have you tried` | 3 | 15 | 13.6 | casual 15 |
| `the post office` | 3 | 8 | 13.4 | casual 7, lazy 1 |
| `for an hour` | 3 | 9 | 12.5 | casual 8, lazy 1 |
| `that is the whole` | 4 | 11 | 12.3 | lazy 9, casual 2 |
| `i have been` | 3 | 11 | 12.2 | casual 9, lazy 2 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `a couple of` | 3 | 11 | 11.6 | casual 11 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `the best kind` | 3 | 18 | 11.5 | casual 12, lazy 6 |
| `how long did` | 3 | 9 | 11.5 | casual 9 |
| `feel like a` | 3 | 9 | 11.5 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.4 | casual 9 |
| `did you get` | 3 | 42 | 11.2 | casual 40, lazy 2 |
| `has it been` | 3 | 8 | 11.1 | casual 8 |
| `the whole point` | 3 | 8 | 10.5 | casual 4, lazy 4 |
| `and i am` | 3 | 8 | 10.4 | casual 7, lazy 1 |
| `a lot of` | 3 | 9 | 10.3 | casual 7, lazy 2 |
| `what did you` | 3 | 27 | 10.3 | casual 26, lazy 1 |
| `are you going` | 3 | 15 | 10.2 | casual 15 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `an hour` | 2 | casual 34, lazy 14 |
| `i know` | 2 | casual 16, lazy 2 |
| `the list` | 2 | casual 10, lazy 6 |
| `i did` | 2 | casual 19, lazy 4 |
| `on the` | 2 | casual 151, lazy 45 |
| `a new` | 2 | casual 37, lazy 11 |
| `whole day` | 2 | casual 4, lazy 4 |
| `know it` | 2 | casual 6, lazy 2 |
| `the afternoon` | 2 | casual 5, lazy 5 |
| `on your` | 1 | casual 11 |
| `the heating` | 2 | casual 10, lazy 2 |
| `has been` | 2 | casual 10, lazy 2 |
| `and i'm` | 1 | casual 13 |
| `to a` | 2 | casual 9, lazy 5 |
| `i got` | 2 | casual 13, lazy 1 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `the coffee` | 2 | lazy 10, casual 7 |
| `a walk` | 2 | casual 16, lazy 2 |
| `for a` | 2 | casual 74, lazy 20 |
| `for one` | 2 | lazy 12, casual 7 |
| `got a` | 2 | casual 21, lazy 1 |
| `going to` | 2 | casual 18, lazy 4 |
| `of the` | 2 | casual 84, lazy 35 |
| `more than` | 2 | casual 17, lazy 8 |
| `just a` | 2 | casual 22, lazy 3 |

## 4. Opener maps

- assistant pos 0 (n=5835): a 7.2%, the 3.1%, that 2.6%, haha 2.3%, i 1.8%, did 1.1%
- assistant pos 1 (n=5835): the 9.2%, is 2.3%, a 2.2%, you 1.4%, it 1.3%, and 1.1%
- assistant pos 2 (n=5834): the 6.2%, is 4.2%, are 2.7%, a 2.1%, of 1.6%, for 1.3%
- assistant pos last (n=5835): it 5.4%, now 1.6%, time 1.5%, one 1.3%, again 1.0%, then 1.0%
- user pos 0 (n=5835): the 10.5%, my 7.8%, i 7.4%, our 6.3%, did 4.3%, a 3.0%
- user pos 1 (n=5772): the 5.3%, you 3.8%, a 3.0%, was 1.7%, did 1.6%, is 1.5%
- user pos 2 (n=5683): the 7.5%, a 3.2%, is 2.3%, you 2.2%, and 1.9%, in 1.2%
- user pos last (n=5835): again 2.6%, it 2.0%, now 1.6%, week 1.6%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **7.5%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 1954 |

