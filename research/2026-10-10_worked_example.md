# Worked example -- ONE category end to end (ranting)

Fable #709 decision 1: generator + dependence gate + diversity instrument, gates
green, numbers posted, BEFORE any volume. This is that readout.

**Category:** the `ranting` register (families commute + delivery) -- a complaint
about a CONCRETE thing. Chosen deliberately: the dependence we want is LEXICAL,
so a complaint about a thing makes the noun echo natural.

**Artifacts**
| file | what |
|---|---|
| `scripts/gen_worked.py` | the generator (seeded, deterministic, writes only into `gen/`) |
| `scripts/dependence_gate.py` | the generation-time gate (dependence + every corpus law) |
| `scripts/diversity.py` | the mode-collapse guard (fixed this session: see below) |
| `gen/ranting_worked.jsonl` | the output, 1200 rows, batch_no 9000, ids `st2_genrant_*` |

---

## 1. The structural dependence

The assistant template contains the SAME surface form `{f}` the user template
introduced -- the identical token, not a lemma (`commitment` != `committed`).
So every pair shares >=1 content word **by construction**. The gate verifies it
rather than trusting it.

## 2. Gates -- ALL GREEN

`dependence_gate.py gen/ranting_worked.jsonl`:

```
[PASS] CRLF only (no bare LF)            0 bare LF
[PASS] JSON parseable                    0 bad lines
[PASS] ids present and unique            1200 rows, 1200 unique
[PASS] structural alternation            0 bad rows
[PASS] ASCII only                        0 turns
[PASS] no ASCII hyphen                   0 turns
[PASS] assistant 10-13 words             0 turns
[PASS] qmark law both directions         0 turns
[PASS] no reply opens with `the <noun>`  0 rows
[PASS] no reply opens on its own noun    0 rows
[PASS] every pair shares >=1 CONTENT word  0/1200 zero-share
VERDICT: ALL GATES GREEN
```

**The shared token IS the noun**, not a function word (Fable addition (a)):

```
top shared content words: shipment 76, parcels 74, packages 73, delivery 73,
commute 72, bus 72, train 70, orders 69, package 68, line 67, tram 66,
courier 65, tube 65, service 60, parcel 60, consignment 58, order 57, journey 55
```

`conditioning.py`'s own stopword list already excludes function words, so a
reply sharing only "the"/"is" cannot pass; the histogram confirms the noun is
what carries the overlap. (Note: `up` is a content word under that definition
and leaks into a few pairs via "drive me up the wall" -- mean shared 1.10 vs a
1.00 floor.)

**The real near-dup gate, corpus-wide** (live 2001 + generated 1200 = 3201 rows,
`_neardup_replicate.py`, the same 3-shingle Jaccard distance < 0.60 prepare.rs
enforces): **0 near-dup pairs.**

**Integrity lenses** (`integrity.py`): 10.55 mean assistant words, 0.0%
no-function-word, opener share 27.2%. Not flagged. 10.55 sits inside the
[8, 30] drift band; 0.0% is nowhere near the 40% generator-shape floor.

## 3. THE CONSTRAINT THAT MATTERS: the near-dup gate eats 60% of the output

A naive slot-filler produces rows that are 60-70% shingle-similar and would be
dropped en masse. Measured yield:

```
candidates tried 3699 -> rows accepted 1200  (yield 32.4%)
rejected: 315 length/frame, 12 exact-duplicate convo, 2172 near-dup (dist < 0.6)
```

**2,172 of 3,699 candidates (59%) died on the near-dup gate alone.** The
generator survives only because it (a) spreads >=2 independent slots through the
sentence and (b) greedily filters every candidate through the EXACT gate logic
before accepting it. The yield is the honest measure of how much of the template
space is usable -- and it is a third.

## 4. THE VERDICT: the diversity guard FAILS, and it fails on volume

`diversity.py`, size-matched (Fable addition (b) -- both sides at 1200 rows):

| observable | generated | live baseline (1200 rows) |
|---|---|---|
| opener entropy | **2.994 bits** (9 distinct openers) | 7.685 bits (636 distinct) |
| distinct-1 | 0.007 | 0.131 |
| distinct-3 | 0.047 | 0.934 |
| distinct-5 | **0.087** | 0.998 |
| type/token | 0.007 | 0.131 |
| dup-5-gram mass | **0.913** | 0.002 |

**91.3% of the generated file's 5-grams are repeats, against 0.002 in the live
corpus -- a ~450x gap that survives size-matching.** This is the exact
mode-collapse risk named in the data plan, now measured rather than feared.

**The collapse is a function of volume, and it is monotone:**

| generated rows | assistant turns | distinct-5 | dup-5-gram mass |
|---|---|---|---|
| 60 | 60 | 0.536 | 0.464 |
| 150 | 150 | 0.390 | 0.610 |
| 400 | 400 | 0.237 | 0.763 |
| 1200 | 1200 | 0.087 | 0.913 |

12 assistant frames at 1200 rows = **100 uses per frame**. distinct-5 falls
roughly as 1/rows: the frame inventory is FIXED, so the distinct 5-gram count
grows sublinearly while the total grows linearly. Extrapolating to the 10K-pair
pilot: to hold dup-5-gram mass near the live corpus's 0.002 the assistant side
needs **effectively one novel frame per row** -- i.e. no template reuse at all.

**Caveat, stated honestly:** the live baseline's 67 batches span 30 registers
(`prompt_eval.py`), so some of the live file's diversity is register breadth a
single-category generator cannot have. That is a real part of the gap. But a
0.913 repeat mass is a TEMPLATE signature -- 12 frames used 100 times each --
not a register effect, and the monotone volume curve (0.464 -> 0.913 as rows go
60 -> 1200) is the template running out of surface, not the category running
out of topics.

## 5. Two instrument defects found by running this

1. **`diversity.py --sample-rows` did not apply to `--compare`.** It reported the
   1200-row generated file against the FULL 2001-row baseline and charged the
   pure size effect to the generator -- the very error Fable addition (b) exists
   to prevent. FIXED: when `--compare` is present both sides are subsampled to
   the smaller (or `--sample-rows`) size.
2. **The normalised opener entropy is misleading during collapse.** The
   generated file scores 0.944 normalised vs the baseline's 0.825 -- it looks
   MORE diverse -- because `H / log2(V)` has a tiny `log2(V)` when only 9
   openers exist. The absolute bits (2.994 vs 7.685) and dup-5-gram mass are the
   honest signals; the normalised column should never be read alone.

A third, from the opener histogram: the **near-dup filter biases the surviving
distribution**. The user opener "the" is 27.2% of the generated file (vs 16.7%
if the 6 user frames were uniform), because frame 4 (`the {f} ...`) differs most
in word ORDER from frames 1-3 and so survives the shingle gate more often. The
filter that enforces diversity on one axis concentrates it on another. At 27.2%
it is already near integrity.py's 30% opener ceiling.

## 6. What this means for the pilot

- The dependence gate and the structural laws are SOLVED -- they are green and
  they are cheap to keep green.
- The near-dup gate is survivable but costs two-thirds of a naive generator's
  output.
- **Diversity is the binding constraint, and it is not a tuning problem.** A
  fixed frame inventory cannot produce pilot volume; the assistant side needs
  per-row novelty. Template generation with 12 frames gets ~1200 rows before it
  is 91% repeats.
- Therefore the pilot generator must either (a) carry a very large frame
  inventory (order 10K distinct assistant surfaces), or (b) generate surface
  with a model rather than a template -- with the dependence gate applied to
  every row regardless of source. The gate is source-agnostic and stays.

---

# ADDENDUM -- the compositional generator, and the correction to my own law

`scripts/gen_compose.py`, `gen/ranting_compose.jsonl`. Same category, same user
grammar, same gate; only the assistant changed: 12 FIXED frames -> 4 skeletons x
op(10) x verb(10) x tail(10) x noun(18) = ~72,000 surfaces.

| observable | fixed-12 | compositional | live (1200 rows) |
|---|---|---|---|
| opener entropy | 2.994 | 3.316 | 7.685 |
| distinct-5 | 0.087 | **0.297** | 0.998 |
| dup-5-gram mass | 0.913 | **0.703** | 0.002 |
| near-dup rejections | 2,172 | **95** | -- |
| yield | 32.4% | **82.2%** | -- |

All gates green; dependence slightly better (mean shared 1.10 -> 1.24).

## The #715 occupancy law was about the wrong quantity

#715 measured `distinct-5 = P(1 - e^(-N/P))/N` against the number of distinct
SURFACES. For P = 72,000 it predicts distinct-5 ~ 1.000. Measured: 0.297.

The law is correct but the metric counts **5-grams**, and a compositional grammar
SHARES its banks, so the 5-gram space is not the surface product:

```
distinct 5-grams  ~  S skeletons x SUM over shingle positions of
                     (product of the banks that position spans)
```

Verified: fixed-12 = 684 distinct 5-grams; compositional = 2,557; live at 1200
rows = ~10,400. Predicted for the skeleton (4 x ~850) = ~3,400.

## How big it has to be

Need ~10x the total 5-gram count in DISTINCT 5-grams. At the 10K pilot that is
~63,000, i.e. `S x 6s^2 >= 63,000`. Synthetic-bank diagnostic (filler tokens,
diversity only, calibrated against the real file -- one skeleton at banks of 10
predicts 0.068, four gives the measured 0.297):

| all banks size s | distinct-5 (1200 rows, 1 skeleton) |
|---|---|
| 10 | 0.068 |
| 20 | 0.257 |
| 30 | 0.445 |
| 50 | 0.637 |
| 100 | 0.765 |

Enlarging ONE bank is nearly useless (tail 10 -> 100 moved 0.108 -> 0.207);
EVERY bank must be large, because a 5-gram only varies if two large banks fall
inside its 5-token window. Pilot working point: ~12 skeletons x banks of ~100
-> distinct-5 ~ 0.95. That is ~400-500 hand-authored phrases plus ~12 skeletons,
and the bar rises again with every volume step.

## Conclusion

(a) is viable but is a treadmill -- rebuild the generator larger for each volume
step. (b) model-generated surface gets per-row novelty for free. The binding
quantity is the DISTINCT 5-GRAM COUNT, and hand-written text is the only thing
here that clears it without a per-volume rebuild. Recommendation: (b), with the
dependence gate and diversity guard applied to every row as they are now.
