# synth2 token-attractor map

Generated 2026-10-07 14:35  |  corpus 1229 rows, **2185 assistant turns**, 2185 user turns
Probe: `probe_out5.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## 0. Change since 2026-10-07T14:08:44

| metric | was | now | delta |
|---|---|---|---|
| `the`-opener (assistant) | 7.0% | 10.7% | +3.7 |
| `the`-opener (user) | 7.0% | 7.3% | +0.3 |
| copula-only | 1.5% | 2.1% | +0.6 |

| attractor | model% was | model% now | amplify was | amplify now |
|---|---|---|---|---|
| `a good` | 55% | 60% | 26x | 31x |
| `the whole` | 23% | 55% | 14x | 38x |
| `whole_thing` | - | 42% | - | 114x |
| `it's been` | 12% | 28% | 12x | 36x |
| `the one` | 45% | 23% | 34x | 21x |
| `i'm not` | 47% | 17% | 90x | 40x |
| `on the` | 10% | 18% | 5x | 7x |
| `how many` | - | 13% | - | 18x |
| `or just` | - | 10% | - | 20x |
| `just a` | - | 10% | - | 14x |

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 10.7% | < 12% |
| `the`-opener (user) | 7.3% | n/a |
| copula-only turns | 2.1% | < 4% |
| registers carrying a top attractor | 1 / 1 | n/a |
| probe outputs carrying a top attractor | 58 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a good` | 42 | 192.2 | 32.0 | 60% | 31x | casual 42 |
| `the whole` | 32 | 146.5 | 82.4 | 55% | 38x | casual 32 |
| `whole_thing` | 8 | 36.6 | 13.7 | 42% | 114x | casual 8 |
| `it's been` | 17 | 77.8 | 0.0 | 28% | 36x | casual 17 |
| `the one` | 24 | 109.8 | 41.2 | 23% | 21x | casual 24 |
| `i'm not` | 9 | 41.2 | 9.2 | 17% | 40x | casual 9 |
| `on the` | 57 | 260.9 | 270.0 | 18% | 7x | casual 57 |
| `how many` | 16 | 73.2 | 9.2 | 13% | 18x | casual 16 |
| `or just` | 11 | 50.3 | 0.0 | 10% | 20x | casual 11 |
| `just a` | 16 | 73.2 | 22.9 | 10% | 14x | casual 16 |
| `a bit` | 37 | 169.3 | 45.8 | 12% | 7x | casual 37 |
| `of the` | 51 | 233.4 | 123.6 | 12% | 5x | casual 51 |
| `one of` | 14 | 64.1 | 41.2 | 8% | 13x | casual 14 |
| `that's the` | 32 | 146.5 | 68.6 | 10% | 7x | casual 32 |
| `not a` | 8 | 36.6 | 0.0 | 7% | 18x | casual 8 |
| `do it` | 25 | 114.4 | 13.7 | 8% | 7x | casual 25 |
| `i've been` | 26 | 119.0 | 54.9 | 8% | 7x | casual 26 |
| `they are` | 10 | 45.8 | 0.0 | 7% | 15x | casual 10 |
| `my mum` | 10 | 45.8 | 18.3 | 7% | 15x | casual 10 |
| `it's a` | 11 | 50.3 | 45.8 | 7% | 13x | casual 11 |
| `and it's` | 12 | 54.9 | 32.0 | 7% | 12x | casual 12 |
| `to do` | 14 | 64.1 | 32.0 | 7% | 10x | casual 14 |
| `i did` | 16 | 73.2 | 41.2 | 7% | 9x | casual 16 |
| `and i'm` | 16 | 73.2 | 13.7 | 7% | 9x | casual 16 |
| `you get` | 25 | 114.4 | 164.8 | 7% | 6x | casual 25 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `that is a good` | 4 | 8 | 13.4 | casual 8 |
| `the best kind` | 3 | 8 | 11.9 | casual 8 |
| `a couple of` | 3 | 8 | 11.4 | casual 8 |
| `did you get` | 3 | 20 | 11.3 | casual 20 |
| `have you got` | 3 | 8 | 11.1 | casual 8 |
| `are you going` | 3 | 8 | 11.0 | casual 8 |
| `did you go` | 3 | 10 | 10.5 | casual 10 |
| `what did you` | 3 | 11 | 10.0 | casual 11 |
| `in the end` | 3 | 11 | 9.2 | casual 11 |
| `twenty minutes` | 2 | 19 | 8.8 | casual 19 |
| `an hour` | 2 | 21 | 8.7 | casual 21 |
| `give it a` | 3 | 10 | 8.4 | casual 10 |
| `in the morning` | 3 | 8 | 8.3 | casual 8 |
| `same here` | 2 | 8 | 8.1 | casual 8 |
| `best kind` | 2 | 9 | 8.0 | casual 9 |
| `is the best` | 3 | 12 | 8.0 | casual 12 |
| `ten minutes` | 2 | 13 | 8.0 | casual 13 |
| `is the real` | 3 | 9 | 7.8 | casual 9 |
| `tell me` | 2 | 8 | 7.7 | casual 8 |
| `my mum` | 2 | 10 | 7.7 | casual 10 |
| `oh no` | 2 | 14 | 7.6 | casual 14 |
| `how many` | 2 | 16 | 7.6 | casual 16 |
| `early night` | 2 | 8 | 7.5 | casual 8 |
| `is the only` | 3 | 8 | 7.4 | casual 8 |
| `is a good` | 3 | 15 | 7.3 | casual 15 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a good` | 1 | casual 42 |
| `the whole` | 1 | casual 32 |
| `whole_thing` | 1 | casual 8 |
| `it's been` | 1 | casual 17 |
| `the one` | 1 | casual 24 |
| `i'm not` | 1 | casual 9 |
| `on the` | 1 | casual 57 |
| `how many` | 1 | casual 16 |
| `or just` | 1 | casual 11 |
| `just a` | 1 | casual 16 |
| `a bit` | 1 | casual 37 |
| `of the` | 1 | casual 51 |
| `one of` | 1 | casual 14 |
| `that's the` | 1 | casual 32 |
| `not a` | 1 | casual 8 |
| `do it` | 1 | casual 25 |
| `i've been` | 1 | casual 26 |
| `they are` | 1 | casual 10 |
| `my mum` | 1 | casual 10 |
| `it's a` | 1 | casual 11 |
| `and it's` | 1 | casual 12 |
| `to do` | 1 | casual 14 |
| `i did` | 1 | casual 16 |
| `and i'm` | 1 | casual 16 |
| `you get` | 1 | casual 25 |

## 4. Opener maps

- assistant pos 0 (n=2185): the 10.7%, a 3.8%, yeah 3.0%, haha 2.6%, that 2.4%, how 2.4%
- assistant pos 1 (n=2156): the 6.3%, it 5.4%, a 3.5%, is 3.4%, you 2.6%, i 1.7%
- assistant pos 2 (n=2087): the 5.3%, is 3.8%, a 3.4%, i 2.4%, it 2.4%, and 1.7%
- assistant pos last (n=2185): it 6.2%, now 1.6%, again 1.5%, you 1.3%, time 1.3%, one 1.3%
- user pos 0 (n=2185): the 7.3%, did 5.4%, i 4.3%, my 3.4%, a 3.2%, how's 3.2%
- user pos 1 (n=2122): the 8.4%, you 5.0%, a 3.8%, was 2.2%, is 1.8%, are 1.7%
- user pos 2 (n=2039): the 6.0%, a 4.2%, you 2.5%, and 2.1%, is 1.8%, in 1.5%
- user pos last (n=2185): again 2.2%, today 1.9%, week 1.9%, weekend 1.7%, it 1.7%, now 1.4%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **19.8%**; model outputs: **68.3%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 432 / 2185 |

