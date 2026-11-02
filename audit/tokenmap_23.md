# synth2 token-attractor map

Generated 2026-10-14 23:02  |  corpus 3129 rows, **5098 assistant turns**, 5098 user turns
Probe: `probe_out23_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-14T21:58:01

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.7% | 2.7% | +0.0 |
| `the`-opener (user) | 9.0% | 9.0% | +0.1 |
| copula-only | 0.5% | 0.5% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the day` | - | 7% | - | 13x |
| `it a` | - | 7% | - | 9x |
| `an early night` | - | 5% | - | 25x |
| `the new` | - | 7% | - | 8x |
| `i've been` | - | 5% | - | 17x |
| `it is` | 7% | 7% | 3x | 3x |
| `are the` | 5% | 7% | 2x | 3x |
| `this time` | - | 5% | - | 6x |
| `i have` | - | 5% | - | 6x |
| `back on` | - | 3% | - | 21x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 9.0% | n/a |
| copula-only turns | 0.5% | < 4% |
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
| `the day` | 26 | 51.0 | 19.6 | 7% | 13x | casual 16, lazy 10 |
| `it a` | 38 | 74.5 | 15.7 | 7% | 9x | casual 34, lazy 4 |
| `an early night` | 10 | 19.6 | 5.9 | 5% | 25x | casual 10 |
| `the new` | 44 | 86.3 | 90.2 | 7% | 8x | casual 35, lazy 9 |
| `i've been` | 15 | 29.4 | 31.4 | 5% | 17x | casual 15 |
| `it is` | 114 | 223.6 | 90.2 | 7% | 3x | casual 79, lazy 35 |
| `are the` | 129 | 253.0 | 19.6 | 7% | 3x | lazy 70, casual 59 |
| `this time` | 44 | 86.3 | 27.5 | 5% | 6x | casual 42, lazy 2 |
| `i have` | 46 | 90.2 | 102.0 | 5% | 6x | casual 35, lazy 11 |
| `back on` | 8 | 15.7 | 13.7 | 3% | 21x | casual 7, lazy 1 |
| `a known` | 8 | 15.7 | 0.0 | 3% | 21x | lazy 6, casual 2 |
| `up on` | 9 | 17.7 | 11.8 | 3% | 19x | casual 9 |
| `a nightmare` | 9 | 17.7 | 5.9 | 3% | 19x | casual 9 |
| `as always` | 10 | 19.6 | 3.9 | 3% | 17x | casual 10 |
| `five minutes` | 11 | 21.6 | 11.8 | 3% | 15x | casual 10, lazy 1 |
| `a quiet` | 13 | 25.5 | 5.9 | 3% | 13x | casual 12, lazy 1 |
| `you will` | 14 | 27.5 | 0.0 | 3% | 12x | casual 9, lazy 5 |
| `my mom` | 14 | 27.5 | 19.6 | 3% | 12x | casual 14 |
| `a big` | 14 | 27.5 | 7.8 | 3% | 12x | casual 14 |
| `is not` | 15 | 29.4 | 5.9 | 3% | 11x | casual 12, lazy 3 |
| `a real` | 88 | 172.6 | 84.3 | 5% | 3x | casual 82, lazy 6 |
| `is it` | 100 | 196.2 | 39.2 | 5% | 3x | casual 100 |
| `this morning` | 22 | 43.2 | 113.8 | 3% | 8x | casual 21, lazy 1 |
| `a day` | 22 | 43.2 | 25.5 | 3% | 8x | casual 18, lazy 4 |
| `is the` | 336 | 659.1 | 121.6 | 7% | 1x | casual 252, lazy 84 |

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
| `best kind of` | 3 | 12 | 14.2 | casual 8, lazy 4 |
| `at this point` | 3 | 9 | 13.9 | lazy 5, casual 4 |
| `have you tried` | 3 | 15 | 13.4 | casual 15 |
| `for an hour` | 3 | 9 | 12.7 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `i have been` | 3 | 11 | 12.0 | casual 9, lazy 2 |
| `the best kind` | 3 | 15 | 11.6 | casual 12, lazy 3 |
| `a couple of` | 3 | 11 | 11.5 | casual 11 |
| `how long did` | 3 | 9 | 11.5 | casual 9 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `did you find` | 3 | 9 | 11.2 | casual 9 |
| `did you get` | 3 | 42 | 11.2 | casual 40, lazy 2 |
| `has it been` | 3 | 8 | 10.8 | casual 8 |
| `a lot of` | 3 | 8 | 10.3 | casual 7, lazy 1 |
| `and i am` | 3 | 8 | 10.2 | casual 7, lazy 1 |
| `are you going` | 3 | 15 | 10.2 | casual 15 |
| `what did you` | 3 | 27 | 10.1 | casual 26, lazy 1 |
| `do you go` | 3 | 8 | 10.1 | casual 8 |
| `a bit of` | 3 | 15 | 10.0 | casual 15 |
| `post office` | 2 | 8 | 9.8 | casual 8 |
| `earn their` | 2 | 10 | 9.8 | lazy 9, casual 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the day` | 2 | casual 16, lazy 10 |
| `it a` | 2 | casual 34, lazy 4 |
| `an early night` | 1 | casual 10 |
| `the new` | 2 | casual 35, lazy 9 |
| `i've been` | 1 | casual 15 |
| `it is` | 2 | casual 79, lazy 35 |
| `are the` | 2 | lazy 70, casual 59 |
| `this time` | 2 | casual 42, lazy 2 |
| `i have` | 2 | casual 35, lazy 11 |
| `back on` | 2 | casual 7, lazy 1 |
| `a known` | 2 | lazy 6, casual 2 |
| `up on` | 1 | casual 9 |
| `a nightmare` | 1 | casual 9 |
| `as always` | 1 | casual 10 |
| `five minutes` | 2 | casual 10, lazy 1 |
| `a quiet` | 2 | casual 12, lazy 1 |
| `you will` | 2 | casual 9, lazy 5 |
| `my mom` | 1 | casual 14 |
| `a big` | 1 | casual 14 |
| `is not` | 2 | casual 12, lazy 3 |
| `a real` | 2 | casual 82, lazy 6 |
| `is it` | 1 | casual 100 |
| `this morning` | 2 | casual 21, lazy 1 |
| `a day` | 2 | casual 18, lazy 4 |
| `is the` | 2 | casual 252, lazy 84 |

## 4. Opener maps

- assistant pos 0 (n=5098): a 7.6%, that 2.9%, the 2.7%, haha 2.6%, i 1.8%, did 1.2%
- assistant pos 1 (n=5098): the 10.2%, is 2.5%, a 2.5%, you 1.6%, it 1.5%, and 1.2%
- assistant pos 2 (n=5097): the 6.6%, is 4.3%, a 2.3%, are 2.2%, of 1.7%, for 1.4%
- assistant pos last (n=5098): it 5.5%, now 1.7%, time 1.6%, one 1.3%, then 1.1%, again 1.1%
- user pos 0 (n=5098): the 9.0%, my 6.6%, i 5.7%, did 4.5%, our 4.4%, a 3.3%
- user pos 1 (n=5035): the 5.9%, you 4.1%, a 3.5%, was 1.9%, did 1.8%, to 1.7%
- user pos 2 (n=4946): the 6.6%, a 3.5%, you 2.3%, and 2.1%, is 1.9%, in 1.4%
- user pos last (n=5098): again 2.6%, it 2.2%, week 1.6%, now 1.6%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **8.6%**; model outputs: **16.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 1217 |

