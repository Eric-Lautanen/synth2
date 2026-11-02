# synth2 token-attractor map

Generated 2026-10-15 02:37  |  corpus 3630 rows, **5634 assistant turns**, 5634 user turns
Probe: `probe_out25_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T00:18:07

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.7% | 2.9% | +0.2 |
| `the`-opener (user) | 9.4% | 10.1% | +0.7 |
| copula-only | 0.5% | 0.6% | +0.1 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | 5% | 12% | 7x | 17x |
| `the heating` | - | 5% | - | 23x |
| `bit of` | - | 5% | - | 17x |
| `going to` | - | 5% | - | 13x |
| `it the` | - | 5% | - | 7x |
| `a new` | - | 5% | - | 6x |
| `staring at` | - | 3% | - | 23x |
| `you get` | - | 5% | - | 5x |
| `up and` | - | 3% | - | 19x |
| `new one` | - | 3% | - | 19x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.9% | < 12% |
| `the`-opener (user) | 10.1% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
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
| `a bit` | 39 | 69.2 | 56.8 | 12% | 17x | casual 39 |
| `the heating` | 12 | 21.3 | 17.7 | 5% | 23x | casual 10, lazy 2 |
| `bit of` | 17 | 30.2 | 16.0 | 5% | 17x | casual 17 |
| `going to` | 22 | 39.0 | 21.3 | 5% | 13x | casual 18, lazy 4 |
| `it the` | 38 | 67.4 | 16.0 | 5% | 7x | casual 34, lazy 4 |
| `a new` | 46 | 81.6 | 85.2 | 5% | 6x | casual 37, lazy 9 |
| `staring at` | 8 | 14.2 | 1.8 | 3% | 23x | casual 8 |
| `you get` | 54 | 95.8 | 88.7 | 5% | 5x | casual 49, lazy 5 |
| `up and` | 10 | 17.7 | 16.0 | 3% | 19x | casual 10 |
| `new one` | 10 | 17.7 | 16.0 | 3% | 19x | casual 7, lazy 3 |
| `into a` | 12 | 21.3 | 10.6 | 3% | 16x | casual 8, lazy 4 |
| `had a` | 12 | 21.3 | 67.4 | 3% | 16x | casual 11, lazy 1 |
| `a good` | 76 | 134.9 | 17.7 | 5% | 4x | casual 69, lazy 7 |
| `there a` | 14 | 24.8 | 1.8 | 3% | 13x | casual 13, lazy 1 |
| `the park` | 14 | 24.8 | 31.9 | 3% | 13x | casual 11, lazy 3 |
| `years of` | 15 | 26.6 | 24.8 | 3% | 13x | casual 14, lazy 1 |
| `i've been` | 15 | 26.6 | 28.4 | 3% | 13x | casual 15 |
| `when the` | 17 | 30.2 | 3.5 | 3% | 11x | lazy 10, casual 7 |
| `i know` | 17 | 30.2 | 23.1 | 3% | 11x | casual 16, lazy 1 |
| `are you` | 93 | 165.1 | 110.0 | 5% | 3x | casual 92, lazy 1 |
| `the weekend` | 18 | 31.9 | 60.3 | 3% | 10x | casual 15, lazy 3 |
| `is there` | 19 | 33.7 | 0.0 | 3% | 10x | casual 18, lazy 1 |
| `the morning` | 21 | 37.3 | 24.8 | 3% | 9x | casual 17, lazy 4 |
| `kind of` | 24 | 42.6 | 7.1 | 3% | 8x | casual 14, lazy 10 |
| `got the` | 29 | 51.5 | 67.4 | 3% | 6x | casual 27, lazy 2 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 12 | 18.0 | casual 7, lazy 5 |
| `are you going to` | 4 | 8 | 16.4 | casual 8 |
| `every single time` | 3 | 9 | 15.9 | lazy 7, casual 2 |
| `an early night` | 3 | 11 | 15.0 | casual 10, lazy 1 |
| `best kind of` | 3 | 14 | 14.4 | casual 8, lazy 6 |
| `at this point` | 3 | 9 | 13.9 | lazy 5, casual 4 |
| `have you tried` | 3 | 15 | 13.6 | casual 15 |
| `the post office` | 3 | 8 | 13.3 | casual 7, lazy 1 |
| `for an hour` | 3 | 9 | 12.6 | casual 8, lazy 1 |
| `that is the whole` | 4 | 11 | 12.4 | lazy 9, casual 2 |
| `i have been` | 3 | 11 | 12.2 | casual 9, lazy 2 |
| `fell asleep` | 2 | 8 | 12.1 | casual 4, lazy 4 |
| `feel like a` | 3 | 9 | 11.7 | lazy 6, casual 3 |
| `a couple of` | 3 | 11 | 11.6 | casual 11 |
| `how long did` | 3 | 9 | 11.6 | casual 9 |
| `the best kind` | 3 | 17 | 11.5 | casual 12, lazy 5 |
| `have you got` | 3 | 16 | 11.5 | casual 16 |
| `did you find` | 3 | 9 | 11.4 | casual 9 |
| `did you get` | 3 | 42 | 11.2 | casual 40, lazy 2 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `the whole point` | 3 | 8 | 10.7 | casual 4, lazy 4 |
| `and i am` | 3 | 8 | 10.4 | casual 7, lazy 1 |
| `a lot of` | 3 | 9 | 10.4 | casual 7, lazy 2 |
| `what did you` | 3 | 27 | 10.3 | casual 26, lazy 1 |
| `are you going` | 3 | 15 | 10.2 | casual 15 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 1 | casual 39 |
| `the heating` | 2 | casual 10, lazy 2 |
| `bit of` | 1 | casual 17 |
| `going to` | 2 | casual 18, lazy 4 |
| `it the` | 2 | casual 34, lazy 4 |
| `a new` | 2 | casual 37, lazy 9 |
| `staring at` | 1 | casual 8 |
| `you get` | 2 | casual 49, lazy 5 |
| `up and` | 1 | casual 10 |
| `new one` | 2 | casual 7, lazy 3 |
| `into a` | 2 | casual 8, lazy 4 |
| `had a` | 2 | casual 11, lazy 1 |
| `a good` | 2 | casual 69, lazy 7 |
| `there a` | 2 | casual 13, lazy 1 |
| `the park` | 2 | casual 11, lazy 3 |
| `years of` | 2 | casual 14, lazy 1 |
| `i've been` | 1 | casual 15 |
| `when the` | 2 | lazy 10, casual 7 |
| `i know` | 2 | casual 16, lazy 1 |
| `are you` | 2 | casual 92, lazy 1 |
| `the weekend` | 2 | casual 15, lazy 3 |
| `is there` | 2 | casual 18, lazy 1 |
| `the morning` | 2 | casual 17, lazy 4 |
| `kind of` | 2 | casual 14, lazy 10 |
| `got the` | 2 | casual 27, lazy 2 |

## 4. Opener maps

- assistant pos 0 (n=5634): a 7.1%, the 2.9%, that 2.6%, haha 2.4%, i 1.8%, did 1.1%
- assistant pos 1 (n=5634): the 9.4%, is 2.3%, a 2.3%, you 1.5%, it 1.3%, and 1.1%
- assistant pos 2 (n=5633): the 6.3%, is 4.1%, are 2.5%, a 2.1%, of 1.6%, on 1.3%
- assistant pos last (n=5634): it 5.4%, now 1.7%, time 1.5%, one 1.3%, again 1.0%, then 1.0%
- user pos 0 (n=5634): the 10.1%, my 7.4%, i 6.9%, our 6.2%, did 4.3%, a 3.1%
- user pos 1 (n=5571): the 5.5%, you 3.8%, a 3.2%, was 1.7%, did 1.7%, to 1.6%
- user pos 2 (n=5482): the 7.5%, a 3.3%, you 2.1%, is 2.1%, and 2.0%, got 1.3%
- user pos last (n=5634): again 2.5%, it 2.0%, now 1.6%, week 1.6%, today 1.5%, morning 1.2%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **7.8%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 1753 |

