# D2 — per-neuron MLP ablation sweep, run 13 (d96) — RESULT

**VERDICT: the ungrounded "word salad" is DISTRIBUTED across the MLP, not localized to a
circuit. No neuron-surgery fix exists for it.**

Tool: `eval/src/bin/neuron_sweep.rs` (eval-only; `cargo build --release -p eval` does not touch
`train.exe`). Mode `zero`: each of 6 layers x 384 ffn neurons = **2,304 ablations**, applied in
memory and restored from a pristine snapshot before the next probe, so the loaded weights are
byte-identical at exit and the sweep is order-independent.

- Screen: 8 probes x 20 tokens. Confirm: all 60 probes x 32 tokens.
- Baseline off `runs/synth2/best.bin` (run 13), read independently three times:
  `loops 3/60, eos 59/60, echo 0.0970, selfrep 0.019`

## 1. `loops` is no longer a usable ranker

| observable | distinct values across 2,304 neurons | range |
|---|---|---|
| `loops` | **3** (2,117 zeros, 182 ones, 5 twos) | 0–2 |
| `eos` | 5 | 4–8 |
| **`echo`** | **516** | 0.016–0.120 |
| `selfrep` | 16 | 0–0.056 |

Ranking on `loops` produced a "top 20" that was literally layer-0 neurons 0–19 in index order —
zero information. The sweep was re-ranked on `echo` (fraction of generated tokens that also appear
in the prompt), which is the observable the D1 top-k readout says now matters.

## 2. The ranking was validated with a contrast group, not assumed

A ranking is only evidence if the other end behaves differently. The **bottom-20 by screen echo**
(all 20 in layer 3) was confirmed too:

| group | confirm mean echo | sd | range |
|---|---|---|---|
| TOP-20 by screen echo | 0.1007 | 0.0052 | 0.093–0.112 |
| BOTTOM-20 by screen echo | 0.0930 | 0.0060 | 0.083–0.101 |
| baseline | 0.0970 | — | — |

`top − bottom = +0.0077`, **Cohen d = 1.38** — the screen is a valid instrument and the effect is
real, not noise.

## 3. But the effect ceiling is tiny

- Best single neuron of all 2,304: **layer 1 neuron 51, echo 0.1120 = +0.0150 (+15.5%)**.
- Best-20 beat worst-20 by only **+0.0077 (+8%)**.
- Baseline echo 0.097 means **90.3% of generated tokens are not grounded in the prompt**.
  A +0.015 ceiling accounts for ~1.7% of that gap.

You cannot ablate your way out of a 90% gap with a 1.5% lever.

## 4. Structure it did reveal

- **Layer 3 is pro-grounding.** The entire bottom-20 is layer 3; zeroing them *lowers* echo below
  baseline. Layer 3's screen mean echo (0.0402) is the lowest of the six layers.
- **Layers 0–2 carry mildly anti-grounding neurons.** Zeroing them *raises* echo; layer 2 has the
  highest screen mean (0.0700) and supplies 111 of the top 200.
- Net: the grounding signal is smeared across the stack with no single carrier. That *is* the
  distributed signature.

## 5. The loops, however, ARE localizable

Separate from grounding, the degenerate `sateateateate...` output (D1's case: p=0.0156, H=7.2) is
broken by single neurons:

- **L2 neuron 14**: `"the good bag sateateateateate..."` → `"the good bag fete then. was the car a
  big chaos?"` (echo 0.110, eos 60, selfrep 0.003)
- **L0 neuron 59**: same loop broken (echo 0.102, eos 60)

So loop circuits are real, local and removable — they are simply not what is failing now, exactly
as the D1 readout predicted.

## 6. Decision consequences

- **No neuron-surgery fix for grounding.** Do not fund one.
- **T1 (RePAIR margin loss) stays parked** — independently confirmed: a persistence-targeting loss
  against a non-localized, non-persistent failure has nothing to bite on.
- **T2 (Delta vs DeltaConv on generation) keeps a low prior** — local modeling is a capacity
  question, and the failure is conditional sharpness.
- The levers consistent with *both* the D1 read and this one: **(a) more fresh data** — the corpus
  is 121,992 tokens against 1,281,516 parameters, ~10x smaller than the model — and **(b) training
  or capacity changes that sharpen the conditional directly.**

## Artifacts

- `audit/neuron_sweep13_zero.tsv` — all 2,304 neurons x 4 observables
- `audit/neuron_sweep13_zero.log` — screen + loops-ranked confirm
- `audit/neuron_sweep13_echo.log` — top-20 by echo, with base-vs-edit generations
- `audit/neuron_sweep13_contrast_out.tsv` — the contrast group
- `eval/src/bin/neuron_sweep.rs` — now with `--confirm-from <tsv>`, which re-ranks a saved sweep by
  any observable without re-running the 38-minute screen

## Limits

- The confirm covers the top-20 and bottom-20 only. A full-population confirm was not run; the
  conclusion rests on the *ceiling* (+0.015), which no selection over the remaining 2,264 neurons
  can exceed by much given the screen's own maximum was 0.120.
- `echo` is a lexical proxy for grounding, not a semantic one. It cannot see a reply that is
  grounded in meaning but shares no surface token — which is exactly why the corpus campaign's
  zero-overlap metric exists alongside it.
