# synth2 token-attractor map

Generated 2026-10-21 23:40  |  corpus 7986 rows, **10341 assistant turns**, 10341 user turns
Probe: `probe_out74_final.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-21T19:49:42

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 4.5% | 4.5% | +0.0 |
| `the`-opener (user) | 14.0% | 13.9% | -0.1 |
| copula-only | 0.6% | 0.6% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a bit` | 3% | 5% | 10x | 14x |
| `it is` | - | 7% | - | 5x |
| `on the` | - | 8% | - | 2x |
| `i have` | - | 5% | - | 10x |
| `time is` | - | 3% | - | 38x |
| `the one` | - | 5% | - | 8x |
| `is a` | - | 8% | - | 2x |
| `the apartment` | - | 3% | - | 29x |
| `did you` | - | 7% | - | 2x |
| `yeah the` | - | 3% | - | 20x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 4.5% | < 12% |
| `the`-opener (user) | 13.9% | n/a |
| copula-only turns | 0.6% | < 4% |
| registers carrying a top attractor | 4 / 4 | n/a |
| probe outputs carrying a top attractor | 42 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a bit` | 36 | 34.8 | 30.9 | 5% | 14x | casual 34, angry 1, lazy 1 |
| `it is` | 133 | 128.6 | 51.3 | 7% | 5x | casual 83, lazy 36, angry 10 |
| `on the` | 347 | 335.6 | 281.4 | 8% | 2x | casual 138, sexy 108, lazy 51 |
| `i have` | 50 | 48.4 | 75.4 | 5% | 10x | casual 34, lazy 12, sexy 4 |
| `time is` | 9 | 8.7 | 0.0 | 3% | 38x | casual 4, lazy 3, angry 2 |
| `the one` | 64 | 61.9 | 22.2 | 5% | 8x | lazy 34, casual 22, angry 6 |
| `is a` | 500 | 483.5 | 58.0 | 8% | 2x | angry 222, casual 147, lazy 116 |
| `the apartment` | 12 | 11.6 | 13.5 | 3% | 29x | casual 7, sexy 4, lazy 1 |
| `did you` | 280 | 270.8 | 238.9 | 7% | 2x | casual 190, sexy 57, angry 28 |
| `yeah the` | 17 | 16.4 | 1.9 | 3% | 20x | casual 16, lazy 1 |
| `was the` | 309 | 298.8 | 92.8 | 7% | 2x | angry 120, casual 92, sexy 91 |
| `have been` | 19 | 18.4 | 38.7 | 3% | 18x | casual 12, lazy 4, sexy 2 |
| `is it` | 113 | 109.3 | 21.3 | 5% | 5x | casual 102, angry 7, sexy 4 |
| `always the` | 20 | 19.3 | 1.0 | 3% | 17x | casual 17, lazy 3 |
| `there a` | 23 | 22.2 | 1.0 | 3% | 15x | casual 14, angry 5, sexy 3 |
| `three days` | 25 | 24.2 | 18.4 | 3% | 14x | angry 9, casual 8, lazy 4 |
| `you have` | 26 | 25.1 | 14.5 | 3% | 13x | casual 17, lazy 5, angry 2 |
| `all the` | 27 | 26.1 | 10.6 | 3% | 13x | casual 10, angry 8, sexy 7 |
| `going to` | 31 | 30.0 | 13.5 | 3% | 11x | casual 18, angry 6, lazy 5 |
| `of the` | 183 | 177.0 | 124.7 | 5% | 3x | casual 80, lazy 39, sexy 33 |
| `what is` | 36 | 34.8 | 11.6 | 3% | 10x | casual 22, angry 9, sexy 3 |
| `through the` | 39 | 37.7 | 37.7 | 3% | 9x | sexy 15, casual 13, angry 7 |
| `should i` | 40 | 38.7 | 5.8 | 3% | 9x | sexy 40 |
| `did it` | 41 | 39.6 | 12.6 | 3% | 8x | casual 32, lazy 4, sexy 3 |
| `it the` | 45 | 43.5 | 11.6 | 3% | 8x | casual 35, sexy 5, lazy 4 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `are you going to` | 4 | 10 | 16.7 | casual 8, angry 2 |
| `on the first try` | 4 | 8 | 16.4 | lazy 5, sexy 2, casual 1 |
| `have you tried` | 3 | 15 | 13.9 | casual 15 |
| `an early night` | 3 | 10 | 13.8 | casual 9, lazy 1 |
| `at this point` | 3 | 12 | 13.8 | lazy 5, casual 4, sexy 2 |
| `the front desk` | 3 | 13 | 13.0 | angry 8, lazy 4, casual 1 |
| `was it worth the` | 4 | 8 | 12.8 | casual 7, sexy 1 |
| `ten minutes of` | 3 | 12 | 12.8 | sexy 9, casual 2, lazy 1 |
| `i have been` | 3 | 10 | 12.6 | casual 8, lazy 2 |
| `did they say` | 3 | 8 | 12.5 | angry 4, casual 4 |
| `two hours of` | 3 | 11 | 12.3 | angry 4, lazy 4, casual 2 |
| `feels like a` | 3 | 8 | 12.1 | casual 3, lazy 3, angry 1 |
| `an hour of` | 3 | 14 | 12.0 | angry 6, casual 3, sexy 3 |
| `did they really` | 3 | 11 | 12.0 | angry 11 |
| `have you got` | 3 | 16 | 11.7 | casual 16 |
| `sounds like a` | 3 | 9 | 11.6 | casual 7, angry 1, sexy 1 |
| `for an hour` | 3 | 13 | 11.5 | casual 8, sexy 3, angry 1 |
| `ice cream` | 2 | 10 | 11.3 | lazy 6, sexy 3, casual 1 |
| `feel like a` | 3 | 11 | 11.2 | lazy 6, casual 4, sexy 1 |
| `how long did` | 3 | 13 | 11.1 | casual 9, angry 3, sexy 1 |
| `falling asleep` | 2 | 9 | 11.0 | sexy 8, lazy 1 |
| `and i am` | 3 | 11 | 11.0 | casual 9, lazy 1, sexy 1 |
| `did you find` | 3 | 10 | 10.9 | casual 9, sexy 1 |
| `a couple of` | 3 | 11 | 10.8 | casual 10, angry 1 |
| `did you get` | 3 | 43 | 10.6 | casual 39, angry 2, lazy 2 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 3 | casual 34, angry 1, lazy 1 |
| `it is` | 4 | casual 83, lazy 36, angry 10, sexy 4 |
| `on the` | 4 | casual 138, sexy 108, lazy 51, angry 50 |
| `i have` | 3 | casual 34, lazy 12, sexy 4 |
| `time is` | 3 | casual 4, lazy 3, angry 2 |
| `the one` | 4 | lazy 34, casual 22, angry 6, sexy 2 |
| `is a` | 4 | angry 222, casual 147, lazy 116, sexy 15 |
| `the apartment` | 3 | casual 7, sexy 4, lazy 1 |
| `did you` | 4 | casual 190, sexy 57, angry 28, lazy 5 |
| `yeah the` | 2 | casual 16, lazy 1 |
| `was the` | 4 | angry 120, casual 92, sexy 91, lazy 6 |
| `have been` | 4 | casual 12, lazy 4, sexy 2, angry 1 |
| `is it` | 3 | casual 102, angry 7, sexy 4 |
| `always the` | 2 | casual 17, lazy 3 |
| `there a` | 4 | casual 14, angry 5, sexy 3, lazy 1 |
| `three days` | 4 | angry 9, casual 8, lazy 4, sexy 4 |
| `you have` | 4 | casual 17, lazy 5, angry 2, sexy 2 |
| `all the` | 4 | casual 10, angry 8, sexy 7, lazy 2 |
| `going to` | 4 | casual 18, angry 6, lazy 5, sexy 2 |
| `of the` | 4 | casual 80, lazy 39, sexy 33, angry 31 |
| `what is` | 4 | casual 22, angry 9, sexy 3, lazy 2 |
| `through the` | 4 | sexy 15, casual 13, angry 7, lazy 4 |
| `should i` | 1 | sexy 40 |
| `did it` | 4 | casual 32, lazy 4, sexy 3, angry 2 |
| `it the` | 4 | casual 35, sexy 5, lazy 4, angry 1 |

## 4. Opener maps

- assistant pos 0 (n=10341): a 10.3%, the 4.5%, did 2.2%, how 2.1%, that 1.8%, was 1.7%
- assistant pos 1 (n=10341): the 10.5%, a 2.0%, is 1.8%, you 1.7%, does 1.1%, on 1.0%
- assistant pos 2 (n=10340): the 6.9%, a 2.9%, is 2.6%, of 1.9%, for 1.9%, on 1.9%
- assistant pos last (n=10341): it 3.8%, now 1.6%, you 1.3%, time 1.2%, one 1.0%, again 0.9%
- user pos 0 (n=10341): the 13.9%, my 9.9%, our 8.1%, we 6.0%, i 6.0%, you 5.6%
- user pos 1 (n=10278): the 3.2%, you 2.2%, a 1.8%, was 1.1%, got 1.1%, did 1.0%
- user pos 2 (n=10189): the 7.8%, a 3.2%, is 1.7%, you 1.4%, my 1.4%, was 1.3%
- user pos last (n=10341): again 2.2%, it 2.0%, now 1.2%, week 1.2%, night 1.2%, today 1.1%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **4.2%**; model outputs: **11.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 425 / 3881 |
| sexy | 5 / 2144 |
| lazy | 1 / 2155 |

