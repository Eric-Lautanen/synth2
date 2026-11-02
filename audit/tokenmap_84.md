# synth2 token-attractor map

Generated 2026-10-23 13:22  |  corpus 8606 rows, **11011 assistant turns**, 11011 user turns
Probe: `probe_out84_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-23T09:45:34

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 5.5% | 5.5% | +0.0 |
| `the`-opener (user) | 14.4% | 14.4% | +0.0 |
| copula-only | 0.8% | 0.8% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a good` | - | 8% | - | 14x |
| `do it` | - | 5% | - | 15x |
| `did you get` | - | 5% | - | 13x |
| `one good` | - | 3% | - | 41x |
| `i am` | 5% | 5% | 8x | 8x |
| `and does anyone` | - | 3% | - | 37x |
| `of a` | - | 5% | - | 8x |
| `it or` | - | 3% | - | 31x |
| `the job` | - | 3% | - | 26x |
| `i've been` | - | 3% | - | 26x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 5.5% | < 12% |
| `the`-opener (user) | 14.4% | n/a |
| copula-only turns | 0.8% | < 4% |
| registers carrying a top attractor | 5 / 5 | n/a |
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
| `a good` | 66 | 59.9 | 12.7 | 8% | 14x | casual 50, lazy 12, sexy 3 |
| `do it` | 36 | 32.7 | 9.1 | 5% | 15x | casual 24, lazy 11, sexy 1 |
| `did you get` | 41 | 37.2 | 37.2 | 5% | 13x | casual 37, angry 2, lazy 2 |
| `one good` | 9 | 8.2 | 0.0 | 3% | 41x | lazy 6, casual 2, sexy 1 |
| `i am` | 68 | 61.8 | 35.4 | 5% | 8x | casual 46, lazy 11, sexy 10 |
| `and does anyone` | 10 | 9.1 | 0.0 | 3% | 37x | formal 10 |
| `of a` | 72 | 65.4 | 30.9 | 5% | 8x | casual 29, angry 15, lazy 15 |
| `it or` | 12 | 10.9 | 0.9 | 3% | 31x | casual 7, formal 2, sexy 2 |
| `the job` | 14 | 12.7 | 5.4 | 3% | 26x | casual 6, angry 5, formal 1 |
| `i've been` | 14 | 12.7 | 15.4 | 3% | 26x | casual 14 |
| `yeah the` | 17 | 15.4 | 1.8 | 3% | 22x | casual 16, lazy 1 |
| `here too` | 18 | 16.3 | 0.0 | 3% | 20x | casual 17, sexy 1 |
| `have you` | 111 | 100.8 | 21.8 | 5% | 5x | casual 80, angry 27, sexy 3 |
| `the same` | 122 | 110.8 | 118.1 | 5% | 5x | angry 34, casual 34, lazy 29 |
| `too much` | 22 | 20.0 | 7.3 | 3% | 17x | casual 9, lazy 9, sexy 2 |
| `got the` | 31 | 28.2 | 44.5 | 3% | 12x | casual 27, lazy 2, formal 1 |
| `instead of` | 33 | 30.0 | 30.0 | 3% | 11x | casual 16, angry 10, sexy 6 |
| `of the` | 195 | 177.1 | 129.9 | 5% | 3x | casual 80, lazy 39, sexy 35 |
| `did it` | 42 | 38.1 | 11.8 | 3% | 9x | casual 32, lazy 4, sexy 3 |
| `of it` | 44 | 40.0 | 26.3 | 3% | 8x | casual 32, sexy 5, angry 4 |
| `for the` | 287 | 260.6 | 270.6 | 5% | 2x | casual 120, sexy 70, angry 61 |
| `the last` | 68 | 61.8 | 56.3 | 3% | 5x | sexy 28, casual 22, lazy 10 |
| `at least` | 72 | 65.4 | 11.8 | 3% | 5x | casual 31, angry 20, sexy 12 |
| `a week` | 77 | 69.9 | 56.3 | 3% | 5x | casual 35, lazy 22, angry 10 |
| `on the` | 368 | 334.2 | 308.8 | 5% | 1x | casual 138, sexy 111, lazy 51 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.8 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `ten minutes of` | 3 | 12 | 12.7 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.7 | casual 8, lazy 2 |
| `the front desk` | 3 | 14 | 12.5 | angry 8, lazy 4, casual 1 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `an hour of` | 3 | 17 | 12.3 | angry 6, casual 3, formal 3 |
| `counts as a` | 3 | 12 | 12.3 | formal 5, casual 2, lazy 2 |
| `two hours of` | 3 | 11 | 12.2 | angry 4, lazy 4, casual 2 |
| `how long has` | 3 | 9 | 12.1 | formal 4, casual 3, angry 2 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `feels like a` | 3 | 8 | 12.0 | casual 3, lazy 3, angry 1 |
| `have you got` | 3 | 15 | 11.7 | casual 15 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.4 | lazy 6, sexy 3, casual 1 |
| `how long did` | 3 | 15 | 11.2 | casual 9, angry 3, formal 2 |
| `falling asleep` | 2 | 9 | 11.1 | sexy 8, lazy 1 |
| `feel like a` | 3 | 11 | 11.1 | lazy 6, casual 4, sexy 1 |
| `and i am` | 3 | 11 | 10.9 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a good` | 4 | casual 50, lazy 12, sexy 3, formal 1 |
| `do it` | 3 | casual 24, lazy 11, sexy 1 |
| `did you get` | 3 | casual 37, angry 2, lazy 2 |
| `one good` | 3 | lazy 6, casual 2, sexy 1 |
| `i am` | 4 | casual 46, lazy 11, sexy 10, angry 1 |
| `and does anyone` | 1 | formal 10 |
| `of a` | 5 | casual 29, angry 15, lazy 15, sexy 10 |
| `it or` | 4 | casual 7, formal 2, sexy 2, lazy 1 |
| `the job` | 5 | casual 6, angry 5, formal 1, lazy 1 |
| `i've been` | 1 | casual 14 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `here too` | 2 | casual 17, sexy 1 |
| `have you` | 4 | casual 80, angry 27, sexy 3, formal 1 |
| `the same` | 5 | angry 34, casual 34, lazy 29, sexy 14 |
| `too much` | 5 | casual 9, lazy 9, sexy 2, angry 1 |
| `got the` | 4 | casual 27, lazy 2, formal 1, sexy 1 |
| `instead of` | 4 | casual 16, angry 10, sexy 6, formal 1 |
| `of the` | 5 | casual 80, lazy 39, sexy 35, angry 31 |
| `did it` | 5 | casual 32, lazy 4, sexy 3, angry 2 |
| `of it` | 4 | casual 32, sexy 5, angry 4, lazy 3 |
| `for the` | 5 | casual 120, sexy 70, angry 61, lazy 24 |
| `the last` | 5 | sexy 28, casual 22, lazy 10, angry 5 |
| `at least` | 4 | casual 31, angry 20, sexy 12, lazy 9 |
| `a week` | 5 | casual 35, lazy 22, angry 10, formal 8 |
| `on the` | 5 | casual 138, sexy 111, lazy 51, angry 50 |

## 4. Opener maps

- assistant pos 0 (n=11011): a 10.1%, the 5.5%, did 2.3%, how 2.2%, does 1.8%, that 1.7%
- assistant pos 1 (n=11011): the 11.0%, a 2.0%, is 1.8%, you 1.7%, does 1.3%, on 0.9%
- assistant pos 2 (n=11010): the 7.1%, a 2.9%, is 2.6%, on 2.0%, of 1.9%, for 1.9%
- assistant pos last (n=11011): it 3.9%, now 1.5%, you 1.2%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=11011): the 14.4%, my 9.7%, our 8.4%, i 6.3%, we 6.1%, you 5.4%
- user pos 1 (n=10948): the 3.2%, you 2.1%, a 1.7%, got 1.0%, was 1.0%, is 1.0%
- user pos 2 (n=10858): the 7.8%, a 3.5%, is 1.7%, my 1.4%, you 1.3%, was 1.2%
- user pos last (n=11011): again 2.1%, it 2.1%, now 1.2%, week 1.2%, night 1.1%, morning 1.0%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **3.8%**; model outputs: **10.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 415 / 3881 |
| sexy | 5 / 2211 |
| lazy | 1 / 2155 |

