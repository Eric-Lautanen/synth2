# synth2 token-attractor map

Generated 2026-10-07 14:08  |  corpus 1043 rows, **1738 assistant turns**, 1738 user turns
Probe: `probe_out4.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T13:57:11

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 7.0% | 7.0% | -0.0 |
| `the`-opener (user) | 7.4% | 7.0% | -0.4 |
| copula-only | 1.5% | 1.5% | -0.0 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `i'm not` | - | 47% | - | 90x |
| `a good` | - | 55% | - | 26x |
| `the one` | - | 45% | - | 34x |
| `the whole` | - | 23% | - | 14x |
| `you get` | - | 15% | - | 14x |
| `that's the` | - | 13% | - | 9x |
| `for it` | - | 12% | - | 14x |
| `it's been` | - | 12% | - | 12x |
| `to do` | - | 10% | - | 14x |
| `did you` | - | 13% | - | 5x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 7.0% | < 12% |
| `the`-opener (user) | 7.0% | n/a |
| copula-only turns | 1.5% | < 4% |
| registers carrying a top attractor | 1 / 1 | n/a |
| probe outputs carrying a top attractor | 57 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `i'm not` | 9 | 51.8 | 0.0 | 47% | 90x | casual 9 |
| `a good` | 37 | 212.9 | 34.5 | 55% | 26x | casual 37 |
| `the one` | 23 | 132.3 | 34.5 | 45% | 34x | casual 23 |
| `the whole` | 29 | 166.9 | 34.5 | 23% | 14x | casual 29 |
| `you get` | 19 | 109.3 | 207.1 | 15% | 14x | casual 19 |
| `that's the` | 25 | 143.8 | 69.0 | 13% | 9x | casual 25 |
| `for it` | 14 | 80.6 | 28.8 | 12% | 14x | casual 14 |
| `it's been` | 17 | 97.8 | 0.0 | 12% | 12x | casual 17 |
| `to do` | 12 | 69.0 | 40.3 | 10% | 14x | casual 12 |
| `did you` | 48 | 276.2 | 655.9 | 13% | 5x | casual 48 |
| `and i'm` | 15 | 86.3 | 5.8 | 8% | 10x | casual 15 |
| `on the` | 38 | 218.6 | 235.9 | 10% | 5x | casual 38 |
| `is still` | 9 | 51.8 | 0.0 | 7% | 13x | casual 9 |
| `get a` | 9 | 51.8 | 17.3 | 7% | 13x | casual 9 |
| `up and` | 10 | 57.5 | 11.5 | 7% | 12x | casual 10 |
| `i've been` | 26 | 149.6 | 57.5 | 7% | 4x | casual 26 |
| `is a` | 63 | 362.5 | 74.8 | 8% | 2x | casual 63 |
| `in it` | 9 | 51.8 | 11.5 | 5% | 10x | casual 9 |
| `and it's` | 12 | 69.0 | 28.8 | 5% | 7x | casual 12 |
| `of the` | 42 | 241.7 | 109.3 | 7% | 3x | casual 42 |
| `do it` | 20 | 115.1 | 11.5 | 5% | 4x | casual 20 |
| `is the` | 71 | 408.5 | 138.1 | 7% | 2x | casual 71 |
| `that is` | 40 | 230.1 | 23.0 | 5% | 2x | casual 40 |
| `will be` | 9 | 51.8 | 11.5 | 3% | 6x | casual 9 |
| `my mum` | 9 | 51.8 | 17.3 | 3% | 6x | casual 9 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `that is a good` | 4 | 8 | 13.9 | casual 8 |
| `did you get` | 3 | 14 | 11.4 | casual 14 |
| `what did you` | 3 | 8 | 10.3 | casual 8 |
| `twenty minutes` | 2 | 17 | 8.7 | casual 17 |
| `in the morning` | 3 | 8 | 8.6 | casual 8 |
| `an hour` | 2 | 20 | 8.5 | casual 20 |
| `is the best` | 3 | 9 | 8.5 | casual 9 |
| `give it a` | 3 | 10 | 8.5 | casual 10 |
| `same here` | 2 | 8 | 8.0 | casual 8 |
| `ten minutes` | 2 | 12 | 8.0 | casual 12 |
| `is a good` | 3 | 15 | 7.8 | casual 15 |
| `tell me` | 2 | 8 | 7.7 | casual 8 |
| `how many` | 2 | 12 | 7.7 | casual 12 |
| `oh no` | 2 | 13 | 7.5 | casual 13 |
| `my mum` | 2 | 9 | 7.5 | casual 9 |
| `at least` | 2 | 14 | 7.4 | casual 14 |
| `that is a` | 3 | 14 | 7.4 | casual 14 |
| `better than` | 2 | 13 | 6.9 | casual 13 |
| `too much` | 2 | 8 | 6.7 | casual 8 |
| `next time` | 2 | 13 | 6.7 | casual 13 |
| `more than` | 2 | 8 | 6.7 | casual 8 |
| `i've been` | 2 | 26 | 6.6 | casual 26 |
| `how far` | 2 | 8 | 6.6 | casual 8 |
| `couple of` | 2 | 8 | 6.5 | casual 8 |
| `much better` | 2 | 9 | 6.5 | casual 9 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `i'm not` | 1 | casual 9 |
| `a good` | 1 | casual 37 |
| `the one` | 1 | casual 23 |
| `the whole` | 1 | casual 29 |
| `you get` | 1 | casual 19 |
| `that's the` | 1 | casual 25 |
| `for it` | 1 | casual 14 |
| `it's been` | 1 | casual 17 |
| `to do` | 1 | casual 12 |
| `did you` | 1 | casual 48 |
| `and i'm` | 1 | casual 15 |
| `on the` | 1 | casual 38 |
| `is still` | 1 | casual 9 |
| `get a` | 1 | casual 9 |
| `up and` | 1 | casual 10 |
| `i've been` | 1 | casual 26 |
| `is a` | 1 | casual 63 |
| `in it` | 1 | casual 9 |
| `and it's` | 1 | casual 12 |
| `of the` | 1 | casual 42 |
| `do it` | 1 | casual 20 |
| `is the` | 1 | casual 71 |
| `that is` | 1 | casual 40 |
| `will be` | 1 | casual 9 |
| `my mum` | 1 | casual 9 |

## 4. Opener maps

- assistant pos 0 (n=1738): the 7.0%, yeah 3.7%, a 3.1%, i 2.8%, that 2.4%, how 2.4%
- assistant pos 1 (n=1709): the 6.1%, it 6.0%, a 3.9%, is 3.3%, i 2.0%, you 2.0%
- assistant pos 2 (n=1640): the 5.5%, is 3.4%, i 3.1%, a 3.1%, it 2.9%, in 2.0%
- assistant pos last (n=1738): it 6.5%, again 1.7%, now 1.4%, you 1.3%, time 1.3%, out 1.1%
- user pos 0 (n=1738): the 7.0%, did 6.6%, how's 4.0%, you 4.0%, i 3.9%, my 3.3%
- user pos 1 (n=1675): the 9.1%, you 6.3%, a 3.7%, was 2.7%, is 2.1%, are 2.0%
- user pos 2 (n=1593): the 5.9%, a 4.1%, you 3.1%, is 2.0%, for 1.5%, get 1.5%
- user pos last (n=1738): today 2.2%, weekend 2.0%, again 2.0%, week 1.8%, it 1.7%, up 1.6%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **23.3%**; model outputs: **83.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 405 / 1738 |

