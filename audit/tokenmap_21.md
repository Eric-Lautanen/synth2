# synth2 token-attractor map

Generated 2026-10-14 20:43  |  corpus 2821 rows, **4765 assistant turns**, 4765 user turns
Probe: `probe_out21_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-14T19:27:25

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 2.7% | 2.7% | -0.0 |
| `the`-opener (user) | 8.6% | 8.6% | +0.0 |
| copula-only | 0.5% | 0.5% | +0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a good` | 8% | 8% | 6x | 6x |
| `out of` | 7% | 7% | 8x | 8x |
| `worth it` | 7% | 7% | 6x | 6x |
| `to do` | 5% | 5% | 11x | 11x |
| `of it` | 5% | 5% | 7x | 7x |
| `the car` | 5% | 5% | 7x | 7x |
| `a bit` | 5% | 5% | 6x | 6x |
| `the week` | 3% | 3% | 20x | 20x |
| `nothing on` | 3% | 3% | 18x | 18x |
| `i have been` | 3% | 3% | 14x | 14x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 2.7% | < 12% |
| `the`-opener (user) | 8.6% | n/a |
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
| `a good` | 72 | 151.1 | 21.0 | 8% | 6x | casual 69, lazy 3 |
| `out of` | 40 | 83.9 | 83.9 | 7% | 8x | casual 34, lazy 6 |
| `worth it` | 49 | 102.8 | 18.9 | 7% | 6x | casual 42, lazy 7 |
| `to do` | 22 | 46.2 | 37.8 | 5% | 11x | casual 21, lazy 1 |
| `of it` | 33 | 69.3 | 46.2 | 5% | 7x | casual 30, lazy 3 |
| `the car` | 35 | 73.5 | 58.8 | 5% | 7x | casual 31, lazy 4 |
| `a bit` | 39 | 81.8 | 67.2 | 5% | 6x | casual 39 |
| `the week` | 8 | 16.8 | 16.8 | 3% | 20x | casual 5, lazy 3 |
| `nothing on` | 9 | 18.9 | 2.1 | 3% | 18x | casual 8, lazy 1 |
| `i have been` | 11 | 23.1 | 16.8 | 3% | 14x | casual 9, lazy 2 |
| `good luck` | 11 | 23.1 | 0.0 | 3% | 14x | casual 9, lazy 2 |
| `early night` | 11 | 23.1 | 6.3 | 3% | 14x | casual 11 |
| `was it` | 65 | 136.4 | 23.1 | 5% | 4x | casual 65 |
| `in the` | 201 | 421.8 | 438.6 | 7% | 2x | casual 171, lazy 30 |
| `i got` | 13 | 27.3 | 56.7 | 3% | 12x | casual 13 |
| `it in` | 14 | 29.4 | 33.6 | 3% | 11x | casual 13, lazy 1 |
| `did not` | 14 | 29.4 | 16.8 | 3% | 11x | casual 12, lazy 2 |
| `i've been` | 15 | 31.5 | 33.6 | 3% | 11x | casual 15 |
| `on sunday` | 16 | 33.6 | 50.4 | 3% | 10x | casual 16 |
| `i was` | 16 | 33.6 | 48.3 | 3% | 10x | casual 14, lazy 2 |
| `the kids` | 20 | 42.0 | 50.4 | 3% | 8x | casual 16, lazy 4 |
| `keep the` | 20 | 42.0 | 0.0 | 3% | 8x | casual 16, lazy 4 |
| `i did` | 20 | 42.0 | 48.3 | 3% | 8x | casual 19, lazy 1 |
| `of the` | 100 | 209.9 | 157.4 | 5% | 2x | casual 84, lazy 16 |
| `is it` | 100 | 209.9 | 39.9 | 5% | 2x | casual 100 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `the best kind of` | 4 | 10 | 18.0 | casual 7, lazy 3 |
| `are you going to` | 4 | 8 | 16.2 | casual 8 |
| `every single time` | 3 | 8 | 15.9 | lazy 6, casual 2 |
| `an early night` | 3 | 10 | 15.3 | casual 10 |
| `best kind of` | 3 | 12 | 14.3 | casual 8, lazy 4 |
| `at this point` | 3 | 9 | 13.9 | lazy 5, casual 4 |
| `have you tried` | 3 | 15 | 13.3 | casual 15 |
| `for an hour` | 3 | 9 | 12.8 | casual 8, lazy 1 |
| `fell asleep` | 2 | 8 | 12.0 | casual 4, lazy 4 |
| `i have been` | 3 | 11 | 11.8 | casual 9, lazy 2 |
| `the best kind` | 3 | 15 | 11.7 | casual 12, lazy 3 |
| `a couple of` | 3 | 11 | 11.5 | casual 11 |
| `how long did` | 3 | 9 | 11.3 | casual 9 |
| `have you got` | 3 | 16 | 11.3 | casual 16 |
| `did you find` | 3 | 9 | 11.2 | casual 9 |
| `did you get` | 3 | 42 | 11.2 | casual 40, lazy 2 |
| `has it been` | 3 | 8 | 10.7 | casual 8 |
| `a lot of` | 3 | 8 | 10.3 | casual 7, lazy 1 |
| `are you going` | 3 | 15 | 10.2 | casual 15 |
| `and i am` | 3 | 8 | 10.1 | casual 7, lazy 1 |
| `do you go` | 3 | 8 | 10.0 | casual 8 |
| `what did you` | 3 | 27 | 9.9 | casual 26, lazy 1 |
| `a bit of` | 3 | 15 | 9.9 | casual 15 |
| `post office` | 2 | 8 | 9.9 | casual 8 |
| `these days` | 2 | 8 | 9.7 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a good` | 2 | casual 69, lazy 3 |
| `out of` | 2 | casual 34, lazy 6 |
| `worth it` | 2 | casual 42, lazy 7 |
| `to do` | 2 | casual 21, lazy 1 |
| `of it` | 2 | casual 30, lazy 3 |
| `the car` | 2 | casual 31, lazy 4 |
| `a bit` | 1 | casual 39 |
| `the week` | 2 | casual 5, lazy 3 |
| `nothing on` | 2 | casual 8, lazy 1 |
| `i have been` | 2 | casual 9, lazy 2 |
| `good luck` | 2 | casual 9, lazy 2 |
| `early night` | 1 | casual 11 |
| `was it` | 1 | casual 65 |
| `in the` | 2 | casual 171, lazy 30 |
| `i got` | 1 | casual 13 |
| `it in` | 2 | casual 13, lazy 1 |
| `did not` | 2 | casual 12, lazy 2 |
| `i've been` | 1 | casual 15 |
| `on sunday` | 1 | casual 16 |
| `i was` | 2 | casual 14, lazy 2 |
| `the kids` | 2 | casual 16, lazy 4 |
| `keep the` | 2 | casual 16, lazy 4 |
| `i did` | 2 | casual 19, lazy 1 |
| `of the` | 2 | casual 84, lazy 16 |
| `is it` | 1 | casual 100 |

## 4. Opener maps

- assistant pos 0 (n=4765): a 7.8%, that 3.1%, haha 2.8%, the 2.7%, i 2.0%, is 1.2%
- assistant pos 1 (n=4765): the 10.8%, a 2.7%, is 2.7%, you 1.7%, it 1.5%, and 1.2%
- assistant pos 2 (n=4764): the 6.8%, is 4.5%, a 2.5%, are 2.1%, of 1.8%, for 1.5%
- assistant pos last (n=4765): it 5.5%, now 1.7%, time 1.6%, one 1.3%, then 1.2%, again 1.1%
- user pos 0 (n=4765): the 8.6%, my 5.6%, i 5.4%, did 4.7%, a 3.3%, our 3.1%
- user pos 1 (n=4702): the 6.3%, you 4.3%, a 3.7%, was 2.0%, did 1.9%, to 1.9%
- user pos 2 (n=4614): the 6.5%, a 3.7%, you 2.4%, and 2.3%, is 1.9%, one 1.3%
- user pos last (n=4765): again 2.6%, it 2.3%, week 1.7%, now 1.5%, today 1.5%, weekend 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **9.2%**; model outputs: **21.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 439 / 3881 |
| lazy | 1 / 884 |

