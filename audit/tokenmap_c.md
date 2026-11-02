# synth2 token-attractor map

Generated 2026-10-07 16:01  |  corpus 1637 rows, **3109 assistant turns**, 3109 user turns
Probe: `probe_out8.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 10.6% | < 12% |
| `the`-opener (user) | 7.8% | n/a |
| copula-only turns | 1.2% | < 4% |
| registers carrying a top attractor | 1 / 1 | n/a |
| probe outputs carrying a top attractor | 54 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `the one` | 28 | 90.1 | 35.4 | 20% | 22x | casual 28 |
| `you get` | 47 | 151.2 | 115.8 | 22% | 14x | casual 47 |
| `on the` | 72 | 231.6 | 312.0 | 23% | 10x | casual 72 |
| `the whole` | 39 | 125.4 | 106.1 | 20% | 16x | casual 39 |
| `to be` | 15 | 48.2 | 25.7 | 13% | 28x | casual 15 |
| `it's been` | 17 | 54.7 | 0.0 | 13% | 24x | casual 17 |
| `i'm not` | 9 | 28.9 | 9.6 | 12% | 40x | casual 9 |
| `i've been` | 27 | 86.8 | 41.8 | 13% | 15x | casual 27 |
| `did you` | 165 | 530.7 | 376.3 | 20% | 4x | casual 165 |
| `the first` | 32 | 102.9 | 90.1 | 13% | 13x | casual 32 |
| `a bit` | 38 | 122.2 | 83.6 | 10% | 8x | casual 38 |
| `i've got` | 17 | 54.7 | 28.9 | 8% | 15x | casual 17 |
| `and it's` | 12 | 38.6 | 38.6 | 7% | 17x | casual 12 |
| `the way` | 14 | 45.0 | 35.4 | 7% | 15x | casual 14 |
| `on it` | 15 | 48.2 | 12.9 | 7% | 14x | casual 15 |
| `going to` | 16 | 51.5 | 16.1 | 7% | 13x | casual 16 |
| `and i'm` | 16 | 51.5 | 19.3 | 7% | 13x | casual 16 |
| `of the` | 59 | 189.8 | 180.1 | 8% | 4x | casual 59 |
| `a week` | 24 | 77.2 | 41.8 | 7% | 9x | casual 24 |
| `got a` | 25 | 80.4 | 106.1 | 7% | 8x | casual 25 |
| `the time` | 11 | 35.4 | 6.4 | 5% | 14x | casual 11 |
| `be the` | 12 | 38.6 | 3.2 | 5% | 13x | casual 12 |
| `get a` | 14 | 45.0 | 9.6 | 5% | 11x | casual 14 |
| `a good` | 55 | 176.9 | 28.9 | 7% | 4x | casual 55 |
| `to do` | 19 | 61.1 | 25.7 | 5% | 8x | casual 19 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `an early night` | 3 | 8 | 16.4 | casual 8 |
| `that is a good` | 4 | 8 | 12.9 | casual 8 |
| `have you tried` | 3 | 15 | 12.9 | casual 15 |
| `one of those` | 3 | 10 | 12.3 | casual 10 |
| `the best kind` | 3 | 8 | 11.7 | casual 8 |
| `a couple of` | 3 | 8 | 11.5 | casual 8 |
| `are you going` | 3 | 14 | 10.6 | casual 14 |
| `have you got` | 3 | 13 | 10.6 | casual 13 |
| `did you get` | 3 | 34 | 10.5 | casual 34 |
| `a lot of` | 3 | 8 | 10.3 | casual 8 |
| `do you go` | 3 | 11 | 9.9 | casual 11 |
| `what did you` | 3 | 24 | 9.5 | casual 24 |
| `did you go` | 3 | 13 | 9.5 | casual 13 |
| `that's the best` | 3 | 9 | 9.4 | casual 9 |
| `in the end` | 3 | 16 | 9.3 | casual 16 |
| `at the end` | 3 | 8 | 8.9 | casual 8 |
| `twenty minutes` | 2 | 20 | 8.9 | casual 20 |
| `do you have` | 3 | 8 | 8.7 | casual 8 |
| `an hour` | 2 | 24 | 8.6 | casual 24 |
| `give it a` | 3 | 10 | 8.2 | casual 10 |
| `the end of` | 3 | 8 | 8.2 | casual 8 |
| `sounds like` | 2 | 9 | 8.2 | casual 9 |
| `in the morning` | 3 | 8 | 8.1 | casual 8 |
| `my mum` | 2 | 11 | 8.1 | casual 11 |
| `same here` | 2 | 10 | 8.1 | casual 10 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the one` | 1 | casual 28 |
| `you get` | 1 | casual 47 |
| `on the` | 1 | casual 72 |
| `the whole` | 1 | casual 39 |
| `to be` | 1 | casual 15 |
| `it's been` | 1 | casual 17 |
| `i'm not` | 1 | casual 9 |
| `i've been` | 1 | casual 27 |
| `did you` | 1 | casual 165 |
| `the first` | 1 | casual 32 |
| `a bit` | 1 | casual 38 |
| `i've got` | 1 | casual 17 |
| `and it's` | 1 | casual 12 |
| `the way` | 1 | casual 14 |
| `on it` | 1 | casual 15 |
| `going to` | 1 | casual 16 |
| `and i'm` | 1 | casual 16 |
| `of the` | 1 | casual 59 |
| `a week` | 1 | casual 24 |
| `got a` | 1 | casual 25 |
| `the time` | 1 | casual 11 |
| `be the` | 1 | casual 12 |
| `get a` | 1 | casual 14 |
| `a good` | 1 | casual 55 |
| `to do` | 1 | casual 19 |

## 4. Opener maps

- assistant pos 0 (n=3109): the 10.6%, a 4.3%, haha 3.1%, that 2.5%, how 2.2%, yeah 2.1%
- assistant pos 1 (n=3080): the 7.0%, it 4.9%, is 3.8%, a 3.1%, you 2.9%, did 1.5%
- assistant pos 2 (n=3002): the 5.6%, is 3.6%, a 3.4%, it 2.1%, i 1.7%, you 1.7%
- assistant pos last (n=3109): it 6.6%, now 1.9%, time 1.4%, again 1.4%, you 1.4%, one 1.2%
- user pos 0 (n=3109): the 7.8%, i 4.5%, did 3.9%, a 3.7%, my 3.6%, how's 2.3%
- user pos 1 (n=3046): the 7.4%, a 4.3%, you 3.5%, did 1.8%, is 1.7%, was 1.5%
- user pos 2 (n=2963): the 6.1%, a 4.2%, and 2.8%, is 1.8%, you 1.7%, i 1.6%
- user pos last (n=3109): again 2.3%, it 2.2%, week 1.9%, today 1.8%, now 1.7%, weekend 1.5%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **16.5%**; model outputs: **51.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 513 / 3109 |

