# synth2 token-attractor map

Generated 2026-10-15 18:03  |  corpus 4622 rows, **6706 assistant turns**, 6706 user turns
Probe: `probe_out32_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-15T16:14:06

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 3.2% | 3.2% | -0.0 |
| `the`-opener (user) | 11.9% | 12.0% | +0.1 |
| copula-only | 0.7% | 0.7% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `did you get` | - | 8% | - | 13x |
| `i have` | 7% | 8% | 9x | 12x |
| `a good` | 5% | 8% | 4x | 7x |
| `for a week` | - | 5% | - | 42x |
| `ask for` | - | 5% | - | 37x |
| `did not` | - | 5% | - | 18x |
| `for two` | - | 3% | - | 28x |
| `been a` | - | 3% | - | 28x |
| `by the` | - | 5% | - | 6x |
| `now the` | - | 3% | - | 25x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.2% | < 12% |
| `the`-opener (user) | 12.0% | n/a |
| copula-only turns | 0.7% | < 4% |
| registers carrying a top attractor | 3 / 3 | n/a |
| probe outputs carrying a top attractor | 37 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `did you get` | 44 | 65.6 | 62.6 | 8% | 13x | casual 40, angry 2, lazy 2 |
| `i have` | 47 | 70.1 | 95.4 | 8% | 12x | casual 35, lazy 12 |
| `a good` | 85 | 126.8 | 16.4 | 8% | 7x | casual 69, lazy 16 |
| `for a week` | 8 | 11.9 | 16.4 | 5% | 42x | casual 4, lazy 3, angry 1 |
| `ask for` | 9 | 13.4 | 3.0 | 5% | 37x | angry 3, casual 3, lazy 3 |
| `did not` | 19 | 28.3 | 25.4 | 5% | 18x | casual 12, lazy 6, angry 1 |
| `for two` | 8 | 11.9 | 31.3 | 3% | 28x | casual 5, lazy 2, angry 1 |
| `been a` | 8 | 11.9 | 6.0 | 3% | 28x | casual 7, angry 1 |
| `by the` | 56 | 83.5 | 71.6 | 5% | 6x | casual 31, lazy 21, angry 4 |
| `now the` | 9 | 13.4 | 4.5 | 3% | 25x | casual 6, lazy 3 |
| `it's the` | 11 | 16.4 | 23.9 | 3% | 20x | casual 11 |
| `no idea` | 12 | 17.9 | 11.9 | 3% | 19x | casual 10, lazy 2 |
| `has been` | 12 | 17.9 | 58.2 | 3% | 19x | casual 10, lazy 2 |
| `one of` | 15 | 22.4 | 23.9 | 3% | 15x | casual 11, lazy 3, angry 1 |
| `on sunday` | 16 | 23.9 | 35.8 | 3% | 14x | casual 16 |
| `yeah the` | 17 | 25.4 | 3.0 | 3% | 13x | casual 16, lazy 1 |
| `whole_thing` | 17 | 25.4 | 19.4 | 3% | 13x | casual 8, lazy 8, angry 1 |
| `here too` | 17 | 25.4 | 0.0 | 3% | 13x | casual 17 |
| `a big` | 17 | 25.4 | 6.0 | 3% | 13x | casual 14, lazy 3 |
| `have a` | 18 | 26.8 | 19.4 | 3% | 12x | casual 11, lazy 7 |
| `all week` | 18 | 26.8 | 26.8 | 3% | 12x | casual 13, lazy 3, angry 2 |
| `a walk` | 19 | 28.3 | 17.9 | 3% | 12x | casual 16, lazy 2, angry 1 |
| `always the` | 20 | 29.8 | 1.5 | 3% | 11x | casual 17, lazy 3 |
| `this morning` | 22 | 32.8 | 99.9 | 3% | 10x | casual 21, lazy 1 |
| `i did` | 23 | 34.3 | 41.8 | 3% | 10x | casual 19, lazy 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.5 | casual 8, angry 2 |
| `an early night` | 3 | 11 | 14.6 | casual 10, lazy 1 |
| `have you tried` | 3 | 22 | 13.8 | casual 15, angry 7 |
| `at this point` | 3 | 9 | 13.8 | lazy 5, casual 4 |
| `the front desk` | 3 | 8 | 13.1 | lazy 4, angry 3, casual 1 |
| `the post office` | 3 | 8 | 13.0 | casual 7, lazy 1 |
| `i have been` | 3 | 11 | 12.3 | casual 9, lazy 2 |
| `for an hour` | 3 | 9 | 12.2 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `a couple of` | 3 | 12 | 11.6 | casual 11, angry 1 |
| `how long did` | 3 | 12 | 11.6 | casual 9, angry 3 |
| `have you got` | 3 | 16 | 11.4 | casual 16 |
| `feel like a` | 3 | 9 | 11.3 | lazy 6, casual 3 |
| `did you find` | 3 | 9 | 11.0 | casual 9 |
| `has it been` | 3 | 8 | 11.0 | casual 8 |
| `did you get` | 3 | 44 | 11.0 | casual 40, angry 2, lazy 2 |
| `and i am` | 3 | 8 | 10.5 | casual 7, lazy 1 |
| `are you going` | 3 | 17 | 10.3 | casual 15, angry 2 |
| `group chat` | 2 | 8 | 10.3 | lazy 4, angry 2, casual 2 |
| `do you go` | 3 | 8 | 10.2 | casual 8 |
| `a lot of` | 3 | 10 | 10.2 | casual 7, lazy 3 |
| `what did you` | 3 | 27 | 10.0 | casual 26, lazy 1 |
| `a bit of` | 3 | 15 | 10.0 | casual 15 |
| `washing machine` | 2 | 12 | 9.9 | casual 11, lazy 1 |
| `makes the whole` | 3 | 9 | 9.9 | lazy 6, casual 3 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `did you get` | 3 | casual 40, angry 2, lazy 2 |
| `i have` | 2 | casual 35, lazy 12 |
| `a good` | 2 | casual 69, lazy 16 |
| `for a week` | 3 | casual 4, lazy 3, angry 1 |
| `ask for` | 3 | angry 3, casual 3, lazy 3 |
| `did not` | 3 | casual 12, lazy 6, angry 1 |
| `for two` | 3 | casual 5, lazy 2, angry 1 |
| `been a` | 2 | casual 7, angry 1 |
| `by the` | 3 | casual 31, lazy 21, angry 4 |
| `now the` | 2 | casual 6, lazy 3 |
| `it's the` | 1 | casual 11 |
| `no idea` | 2 | casual 10, lazy 2 |
| `has been` | 2 | casual 10, lazy 2 |
| `one of` | 3 | casual 11, lazy 3, angry 1 |
| `on sunday` | 1 | casual 16 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `whole_thing` | 3 | casual 8, lazy 8, angry 1 |
| `here too` | 1 | casual 17 |
| `a big` | 2 | casual 14, lazy 3 |
| `have a` | 2 | casual 11, lazy 7 |
| `all week` | 3 | casual 13, lazy 3, angry 2 |
| `a walk` | 3 | casual 16, lazy 2, angry 1 |
| `always the` | 2 | casual 17, lazy 3 |
| `this morning` | 2 | casual 21, lazy 1 |
| `i did` | 2 | casual 19, lazy 4 |

## 4. Opener maps

- assistant pos 0 (n=6706): a 7.6%, the 3.2%, that 2.4%, did 2.1%, haha 2.0%, i 1.6%
- assistant pos 1 (n=6706): the 10.7%, you 2.2%, a 2.2%, is 2.1%, it 1.2%, and 1.0%
- assistant pos 2 (n=6705): the 6.1%, is 3.8%, are 2.5%, a 2.3%, of 1.5%, for 1.2%
- assistant pos last (n=6706): it 4.8%, now 1.6%, time 1.5%, one 1.1%, again 1.0%, day 0.9%
- user pos 0 (n=6706): the 12.0%, my 9.5%, our 7.7%, i 7.2%, did 3.9%, we 3.0%
- user pos 1 (n=6643): the 4.7%, you 3.4%, a 2.6%, was 1.5%, did 1.5%, is 1.4%
- user pos 2 (n=6554): the 7.0%, a 3.0%, is 2.4%, you 1.9%, and 1.6%, got 1.3%
- user pos last (n=6706): again 2.9%, it 1.9%, now 1.6%, week 1.6%, today 1.5%, night 1.3%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **6.5%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 438 / 3881 |
| lazy | 1 / 2155 |

