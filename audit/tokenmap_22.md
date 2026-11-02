# synth2 token-attractor map

Generated 2026-10-14 21:58  |  corpus 3067 rows, **5031 assistant turns**, 5031 user turns
Probe: `probe_out22_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-14T20:43:26

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.7% | 2.7% | +0.0 |
| `the`-opener (user) | 8.6% | 9.0% | +0.4 |
| copula-only | 0.5% | 0.5% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | 5% | 8% | 6x | 11x |
| `has been` | - | 5% | - | 23x |
| `at work` | - | 5% | - | 21x |
| `tried the` | - | 5% | - | 19x |
| `worth it` | 7% | 7% | 6x | 6x |
| `is there` | - | 5% | - | 13x |
| `is just` | - | 5% | - | 13x |
| `a good` | 8% | 7% | 6x | 5x |
| `you have` | - | 5% | - | 10x |
| `just a` | - | 5% | - | 10x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 9.0% | n/a |
| copula-only turns | 0.5% | < 4% |
| registers carrying a top attractor | 2 / 2 | n/a |
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
| `a bit` | 39 | 77.5 | 63.6 | 8% | 11x | casual 39 |
| `has been` | 11 | 21.9 | 49.7 | 5% | 23x | casual 10, lazy 1 |
| `at work` | 12 | 23.9 | 39.8 | 5% | 21x | casual 11, lazy 1 |
| `tried the` | 13 | 25.8 | 13.9 | 5% | 19x | casual 11, lazy 2 |
| `worth it` | 53 | 105.3 | 17.9 | 7% | 6x | casual 42, lazy 11 |
| `is there` | 19 | 37.8 | 0.0 | 5% | 13x | casual 18, lazy 1 |
| `is just` | 20 | 39.8 | 2.0 | 5% | 13x | lazy 14, casual 6 |
| `a good` | 73 | 145.1 | 19.9 | 7% | 5x | casual 69, lazy 4 |
| `you have` | 24 | 47.7 | 25.8 | 5% | 10x | casual 20, lazy 4 |
| `just a` | 25 | 49.7 | 25.8 | 5% | 10x | casual 22, lazy 3 |
| `it is` | 114 | 226.6 | 91.4 | 7% | 3x | casual 79, lazy 35 |
| `a new` | 43 | 85.5 | 93.4 | 5% | 6x | casual 37, lazy 6 |
| `not much` | 8 | 15.9 | 6.0 | 3% | 21x | casual 7, lazy 1 |
| `a week` | 54 | 107.3 | 61.6 | 5% | 5x | casual 37, lazy 17 |
| `on the` | 170 | 337.9 | 306.1 | 7% | 2x | casual 151, lazy 19 |
| `i have been` | 11 | 21.9 | 15.9 | 3% | 15x | casual 9, lazy 2 |
| `for you` | 11 | 21.9 | 6.0 | 3% | 15x | casual 11 |
| `with the` | 62 | 123.2 | 101.4 | 5% | 4x | casual 54, lazy 8 |
| `is not` | 15 | 29.8 | 6.0 | 3% | 11x | casual 12, lazy 3 |
| `bit of` | 17 | 33.8 | 17.9 | 3% | 10x | casual 17 |
| `are you` | 93 | 184.9 | 121.2 | 5% | 3x | casual 92, lazy 1 |
| `next time` | 25 | 49.7 | 2.0 | 3% | 7x | casual 15, lazy 10 |
| `are the` | 124 | 246.5 | 19.9 | 5% | 2x | lazy 65, casual 59 |
| `for it` | 27 | 53.7 | 23.9 | 3% | 6x | casual 24, lazy 3 |
| `the end` | 30 | 59.6 | 45.7 | 3% | 6x | casual 26, lazy 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 10 | 17.9 | casual 7, lazy 3 |
| `are you going to` | 4 | 8 | 16.3 | casual 8 |
| `every single time` | 3 | 9 | 16.0 | lazy 7, casual 2 |
| `an early night` | 3 | 10 | 15.1 | casual 10 |
| `best kind of` | 3 | 12 | 14.3 | casual 8, lazy 4 |
| `at this point` | 3 | 9 | 13.8 | lazy 5, casual 4 |
| `have you tried` | 3 | 15 | 13.4 | casual 15 |
| `for an hour` | 3 | 9 | 12.6 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `i have been` | 3 | 11 | 12.0 | casual 9, lazy 2 |
| `the best kind` | 3 | 15 | 11.6 | casual 12, lazy 3 |
| `a couple of` | 3 | 11 | 11.5 | casual 11 |
| `how long did` | 3 | 9 | 11.4 | casual 9 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `did you get` | 3 | 42 | 11.2 | casual 40, lazy 2 |
| `did you find` | 3 | 9 | 11.2 | casual 9 |
| `has it been` | 3 | 8 | 10.8 | casual 8 |
| `a lot of` | 3 | 8 | 10.3 | casual 7, lazy 1 |
| `and i am` | 3 | 8 | 10.2 | casual 7, lazy 1 |
| `are you going` | 3 | 15 | 10.2 | casual 15 |
| `do you go` | 3 | 8 | 10.1 | casual 8 |
| `what did you` | 3 | 27 | 10.0 | casual 26, lazy 1 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `post office` | 2 | 8 | 9.8 | casual 8 |
| `earn their` | 2 | 9 | 9.8 | lazy 8, casual 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 1 | casual 39 |
| `has been` | 2 | casual 10, lazy 1 |
| `at work` | 2 | casual 11, lazy 1 |
| `tried the` | 2 | casual 11, lazy 2 |
| `worth it` | 2 | casual 42, lazy 11 |
| `is there` | 2 | casual 18, lazy 1 |
| `is just` | 2 | lazy 14, casual 6 |
| `a good` | 2 | casual 69, lazy 4 |
| `you have` | 2 | casual 20, lazy 4 |
| `just a` | 2 | casual 22, lazy 3 |
| `it is` | 2 | casual 79, lazy 35 |
| `a new` | 2 | casual 37, lazy 6 |
| `not much` | 2 | casual 7, lazy 1 |
| `a week` | 2 | casual 37, lazy 17 |
| `on the` | 2 | casual 151, lazy 19 |
| `i have been` | 2 | casual 9, lazy 2 |
| `for you` | 1 | casual 11 |
| `with the` | 2 | casual 54, lazy 8 |
| `is not` | 2 | casual 12, lazy 3 |
| `bit of` | 1 | casual 17 |
| `are you` | 2 | casual 92, lazy 1 |
| `next time` | 2 | casual 15, lazy 10 |
| `are the` | 2 | lazy 65, casual 59 |
| `for it` | 2 | casual 24, lazy 3 |
| `the end` | 2 | casual 26, lazy 4 |

## 4. Opener maps

- assistant pos 0 (n=5031): a 7.7%, that 2.9%, the 2.7%, haha 2.6%, i 1.8%, did 1.2%
- assistant pos 1 (n=5031): the 10.4%, is 2.6%, a 2.5%, you 1.6%, it 1.5%, and 1.2%
- assistant pos 2 (n=5030): the 6.7%, is 4.3%, a 2.3%, are 2.1%, of 1.8%, for 1.4%
- assistant pos last (n=5031): it 5.5%, now 1.7%, time 1.6%, one 1.3%, then 1.1%, again 1.1%
- user pos 0 (n=5031): the 9.0%, my 6.4%, i 5.6%, did 4.6%, our 4.1%, a 3.3%
- user pos 1 (n=4968): the 6.0%, you 4.1%, a 3.5%, was 1.9%, did 1.8%, to 1.8%
- user pos 2 (n=4879): the 6.6%, a 3.5%, you 2.3%, and 2.1%, is 1.9%, in 1.4%
- user pos last (n=5031): again 2.6%, it 2.2%, week 1.7%, now 1.6%, today 1.5%, weekend 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **8.7%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 1150 |

