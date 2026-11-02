# synth2 token-attractor map

Generated 2026-10-07 15:51  |  corpus 1606 rows, **3040 assistant turns**, 3040 user turns
Probe: `probe_out8.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T15:29:20

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 6.3% | 11.3% | +5.0 |
| `the`-opener (user) | 7.5% | 7.8% | +0.2 |
| copula-only | 1.1% | 1.3% | +0.2 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `the one` | 25% | 20% | 26x | 23x |
| `you get` | 13% | 22% | 10x | 15x |
| `on the` | 8% | 23% | 3x | 10x |
| `the whole` | 25% | 20% | 19x | 16x |
| `to be` | 5% | 13% | 10x | 27x |
| `it's been` | 7% | 13% | 11x | 24x |
| `i'm not` | 15% | 12% | 48x | 39x |
| `i've been` | 7% | 13% | 7x | 15x |
| `did you` | - | 20% | - | 4x |
| `the first` | - | 13% | - | 13x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 11.3% | < 12% |
| `the`-opener (user) | 7.8% | n/a |
| copula-only turns | 1.3% | < 4% |
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
| `the one` | 27 | 88.8 | 36.2 | 20% | 23x | casual 27 |
| `you get` | 45 | 148.0 | 118.4 | 22% | 15x | casual 45 |
| `on the` | 72 | 236.8 | 309.2 | 23% | 10x | casual 72 |
| `the whole` | 39 | 128.3 | 102.0 | 20% | 16x | casual 39 |
| `to be` | 15 | 49.3 | 26.3 | 13% | 27x | casual 15 |
| `it's been` | 17 | 55.9 | 0.0 | 13% | 24x | casual 17 |
| `i'm not` | 9 | 29.6 | 6.6 | 12% | 39x | casual 9 |
| `i've been` | 27 | 88.8 | 39.5 | 13% | 15x | casual 27 |
| `did you` | 159 | 523.0 | 384.9 | 20% | 4x | casual 159 |
| `the first` | 31 | 102.0 | 88.8 | 13% | 13x | casual 31 |
| `a bit` | 38 | 125.0 | 82.2 | 10% | 8x | casual 38 |
| `i've got` | 17 | 55.9 | 29.6 | 8% | 15x | casual 17 |
| `and it's` | 12 | 39.5 | 36.2 | 7% | 17x | casual 12 |
| `the way` | 14 | 46.1 | 36.2 | 7% | 14x | casual 14 |
| `on it` | 15 | 49.3 | 13.2 | 7% | 14x | casual 15 |
| `going to` | 16 | 52.6 | 16.4 | 7% | 13x | casual 16 |
| `and i'm` | 16 | 52.6 | 19.7 | 7% | 13x | casual 16 |
| `of the` | 58 | 190.8 | 171.1 | 8% | 4x | casual 58 |
| `a week` | 24 | 78.9 | 42.8 | 7% | 8x | casual 24 |
| `got a` | 25 | 82.2 | 105.3 | 7% | 8x | casual 25 |
| `the time` | 11 | 36.2 | 6.6 | 5% | 14x | casual 11 |
| `be the` | 12 | 39.5 | 3.3 | 5% | 13x | casual 12 |
| `get a` | 13 | 42.8 | 9.9 | 5% | 12x | casual 13 |
| `a good` | 53 | 174.3 | 26.3 | 7% | 4x | casual 53 |
| `to do` | 19 | 62.5 | 26.3 | 5% | 8x | casual 19 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `an early night` | 3 | 8 | 16.3 | casual 8 |
| `that is a good` | 4 | 8 | 13.0 | casual 8 |
| `have you tried` | 3 | 15 | 12.8 | casual 15 |
| `one of those` | 3 | 10 | 12.3 | casual 10 |
| `a couple of` | 3 | 8 | 11.5 | casual 8 |
| `are you going` | 3 | 14 | 10.6 | casual 14 |
| `have you got` | 3 | 13 | 10.6 | casual 13 |
| `did you get` | 3 | 32 | 10.5 | casual 32 |
| `a lot of` | 3 | 8 | 10.3 | casual 8 |
| `do you go` | 3 | 11 | 9.9 | casual 11 |
| `what did you` | 3 | 22 | 9.5 | casual 22 |
| `did you go` | 3 | 12 | 9.4 | casual 12 |
| `that's the best` | 3 | 8 | 9.4 | casual 8 |
| `in the end` | 3 | 16 | 9.3 | casual 16 |
| `twenty minutes` | 2 | 20 | 9.0 | casual 20 |
| `do you have` | 3 | 8 | 8.7 | casual 8 |
| `an hour` | 2 | 24 | 8.6 | casual 24 |
| `the end of` | 3 | 9 | 8.4 | casual 9 |
| `give it a` | 3 | 10 | 8.3 | casual 10 |
| `in the morning` | 3 | 8 | 8.2 | casual 8 |
| `sounds like` | 2 | 8 | 8.1 | casual 8 |
| `my mum` | 2 | 11 | 8.1 | casual 11 |
| `cheaper than` | 2 | 10 | 8.0 | casual 10 |
| `same here` | 2 | 10 | 8.0 | casual 10 |
| `tell me` | 2 | 8 | 7.9 | casual 8 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `the one` | 1 | casual 27 |
| `you get` | 1 | casual 45 |
| `on the` | 1 | casual 72 |
| `the whole` | 1 | casual 39 |
| `to be` | 1 | casual 15 |
| `it's been` | 1 | casual 17 |
| `i'm not` | 1 | casual 9 |
| `i've been` | 1 | casual 27 |
| `did you` | 1 | casual 159 |
| `the first` | 1 | casual 31 |
| `a bit` | 1 | casual 38 |
| `i've got` | 1 | casual 17 |
| `and it's` | 1 | casual 12 |
| `the way` | 1 | casual 14 |
| `on it` | 1 | casual 15 |
| `going to` | 1 | casual 16 |
| `and i'm` | 1 | casual 16 |
| `of the` | 1 | casual 58 |
| `a week` | 1 | casual 24 |
| `got a` | 1 | casual 25 |
| `the time` | 1 | casual 11 |
| `be the` | 1 | casual 12 |
| `get a` | 1 | casual 13 |
| `a good` | 1 | casual 53 |
| `to do` | 1 | casual 19 |

## 4. Opener maps

- assistant pos 0 (n=3040): the 11.3%, a 3.9%, haha 2.9%, that 2.5%, how 2.3%, yeah 2.1%
- assistant pos 1 (n=3011): the 6.5%, it 5.0%, is 3.9%, a 3.1%, you 3.0%, did 1.5%
- assistant pos 2 (n=2933): the 5.5%, is 3.7%, a 3.4%, it 2.1%, i 1.8%, you 1.7%
- assistant pos last (n=3040): it 6.6%, now 1.8%, time 1.5%, again 1.4%, you 1.3%, one 1.2%
- user pos 0 (n=3040): the 7.8%, i 4.6%, did 4.0%, a 3.6%, my 3.5%, how's 2.3%
- user pos 1 (n=2977): the 7.4%, a 4.3%, you 3.6%, did 1.8%, is 1.7%, was 1.6%
- user pos 2 (n=2894): the 6.2%, a 4.1%, and 2.7%, is 1.8%, you 1.8%, i 1.6%
- user pos last (n=3040): again 2.4%, it 2.2%, week 1.9%, today 1.8%, now 1.6%, weekend 1.5%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **16.3%**; model outputs: **51.7%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 496 / 3040 |

