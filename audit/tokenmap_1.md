# synth2 token-attractor map

Generated 2026-10-07 13:21  |  corpus 558 rows, **791 assistant turns**, 791 user turns
Probe: `probe_out1.txt` (60 outputs)

**FINDER, NOT VERDICT (L2).** Every phrase below is a CANDIDATE to
hand-read. Nothing here is deleted; nothing here is written to `raw/`.

## Headline

| metric | value | target |
|---|---|---|
| `the`-opener (assistant) | 3.3% | < 12% |
| `the`-opener (user) | 4.9% | n/a |
| copula-only turns | 0.3% | < 4% |
| registers carrying a top attractor | 1 / 1 | n/a |
| probe outputs carrying a top attractor | 1 / 60 | 0 |

## 1. Attractors (corpus says it vs model repeats it)

Ranked by priority = model share x (1 + log2(amplification)), so a
phrase must BOTH be over-represented AND actually be emitted to rank
high. `n` is the raw count of assistant turns containing it, `corpus/10k`
per 10,000 assistant turns, `user/10k` per 10,000 user turns (a phrase
high on both is a shared frame), `model%` the share of probe outputs
containing it, `amplify` = model share / corpus share. One row per family.

| phrase | n | corpus/10k | user/10k | model% | amplify | files (top 3) |
|---|---|---|---|---|---|---|
| `a bit` | 23 | 290.8 | 37.9 | 2% | 1x | casual 23 |

## 2. Over-used n-grams (ranked by PMI, count >= 8)

PMI = how much more often the phrase occurs than its parts predict. This
finds phrases the corpus over-uses that may not have surfaced in the
probe yet.

| n-gram | n | count | PMI | files (top 3) |
|---|---|---|---|---|
| `twenty minutes` | 2 | 13 | 8.7 | casual 13 |
| `an hour` | 2 | 13 | 8.7 | casual 13 |
| `oh no` | 2 | 9 | 6.9 | casual 9 |
| `not bad` | 2 | 8 | 6.7 | casual 7 |
| `most of` | 2 | 8 | 6.2 | casual 8 |
| `which is` | 2 | 23 | 6.2 | casual 23 |
| `i've been` | 2 | 21 | 5.8 | casual 21 |
| `on sunday` | 2 | 8 | 5.8 | casual 8 |
| `not really` | 2 | 9 | 5.5 | casual 9 |
| `i've got` | 2 | 17 | 5.5 | casual 17 |
| `i keep` | 2 | 14 | 5.1 | casual 14 |
| `i think` | 2 | 13 | 4.9 | casual 13 |
| `a bit` | 2 | 23 | 4.8 | casual 23 |
| `it's been` | 2 | 16 | 4.8 | casual 16 |
| `i know` | 2 | 16 | 4.8 | casual 16 |
| `did you` | 2 | 9 | 4.7 | casual 9 |
| `and then` | 2 | 21 | 4.4 | casual 21 |
| `to do` | 2 | 8 | 4.4 | casual 8 |
| `a proper` | 2 | 12 | 4.3 | casual 12 |
| `i'm not` | 2 | 8 | 4.1 | casual 8 |
| `i had` | 2 | 9 | 3.9 | casual 9 |
| `i did` | 2 | 16 | 3.8 | casual 16 |
| `the weekend` | 2 | 8 | 3.8 | casual 7 |
| `than i` | 2 | 9 | 3.8 | casual 9 |
| `by the` | 2 | 9 | 3.7 | casual 9 |

## 3. Attractor fan-out (which registers carry each top attractor)

A phrase in one register is a voice; a phrase in twenty is the fan-out
that leaks into unrelated prompts.

| attractor | registers | worst registers |
|---|---|---|
| `a bit` | 1 | casual 23 |

## 4. Opener maps

- assistant pos 0 (n=791): yeah 7.6%, i 4.4%, not 4.3%, the 3.3%, no 3.3%, a 2.7%
- assistant pos 1 (n=787): i 3.9%, the 3.7%, and 2.5%, it 2.5%, did 2.5%, a 2.3%
- assistant pos 2 (n=779): the 5.5%, i 5.3%, it 2.7%, a 1.7%, in 1.5%, and 1.5%
- assistant pos last (n=791): it 5.6%, again 2.1%, you 2.0%, now 1.5%, me 1.5%, day 1.3%
- user pos 0 (n=791): did 12.8%, you 8.7%, how's 8.6%, what 6.3%, how 5.1%, the 4.9%
- user pos 1 (n=788): you 12.7%, the 12.4%, was 3.8%, are 3.2%, your 2.9%, did 2.5%
- user pos 2 (n=760): you 6.4%, the 6.3%, get 2.6%, for 2.4%, a 2.2%, it 1.3%
- user pos last (n=791): today 3.5%, weekend 2.5%, going 2.4%, it 2.0%, up 2.0%, alright 1.8%

## 5. Style leak: contractions

Corpus assistant turns with a contraction: **37.3%**; model outputs: **100.0%**. The corpus keeps them almost entirely in two registers -- if the model uses them everywhere, the register boundary has leaked (the same failure as a frame fan-out, one level down: style, not phrase).

| register | turns with a contraction |
|---|---|
| casual | 295 / 791 |

