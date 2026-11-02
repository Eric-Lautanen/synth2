# Research brief for synth2 (Fable #694) — 2026-10-10

Scope: 7 questions. Deliverable: ranked 3-5 concrete testable changes for THIS model
(vocab 4096 / d96 / L6 / ffn 384 / 1,281,516 params / seq 512 / 122K-token corpus / 64 epochs),
each with evidence + URL, plus a "do not bother" section.

HARD CONSTRAINT (from Fable): any train-crate change must keep synth1 and the other synths
byte-identical on their existing flags. Every proposal below is an OPT-IN FLAG or a
separate analysis binary. No existing default changes.

GROUNDING FACTS MEASURED OFF THE LIVE ARTIFACT (2026-10-10 17:00 ET):
- `runs/synth2/config.txt`: vocab_size=4096, hidden_size=96, num_layers=6, ffn_hidden=384,
  params=1281516, seq_len=512, epochs=64, total_tokens=121992.
- Tied embedding matrix = 4096 x 96 = 393,216 = **30.7% of all 1,281,516 parameters.**
- Corpus passes = 64 epochs x 121,992 tokens = ~7.81M token-passes over a 122K corpus.
- `train/src/deltanet.rs` already carries `LayerArch::{Delta, DeltaConv}`; DeltaConv adds a
  3-tap depthwise causal conv (CONV_TAPS=3, init as identity, tap0=1). `--arch <name>` selects it.
- `train/src/model.rs` already carries `tie_depth_weights()` / `tie_depth_grads()` behind `--tie-depth`.

---

## Q1. Tiny-LM architecture: linear attention (DeltaNet/Mamba/GLA) vs softmax at 0.5-2M params

Linear attention's deficit is NOT the kernel — it is two structural properties, both fixable:

- **Non-injectivity.** Linear attention provably is not injective: different queries map to the
  same attention weights -> semantic confusion. Fix: replace division normalization with
  **subtractive normalization**. Paper: "Bridging the Divide: Reconsidering Softmax and Linear
  Attention" (InLine, LeapLab THU) — https://arxiv.org/html/2412.06590v1 . With injectivity +
  local modeling, linear attention matches/beats softmax at lower cost.
- **Weak local modeling.** Softmax attention is strong at LOCAL modeling, linear attention is not.
  Their fix is an MLP residual / local term. **Our DeltaConv 3-tap depthwise causal conv is exactly
  a local-modeling term** — so the arch we already have is the right instinct; it just needs to be
  measured as an ablation (Delta vs DeltaConv) on the generation instrument, not just the loss.
- **Head-level competition.** "Softmax Linear Attention: Reclaiming Global Competition"
  (2026-02-02) — https://arxiv.org/abs/2602.01744 — lifts softmax from token level to HEAD level:
  attention heads act as coarse semantic slots with competitive (winner-take-all) gating. Reports
  consistent gains over RetNet / GLA / **GDN** on retrieval-heavy long-context. Cheap to add as a
  head-gate on top of the existing delta-rule recurrence.
- **Erase/write decoupling.** Gated DeltaNet-2 (NVIDIA, 2026-05)
  https://research.nvidia.com/publication/2026-05_gated-deltanet-2-decoupling-erase-and-write-linear-attention
  — separates the erase gate from the write gate in the delta rule. Most relevant if we keep
  pushing the recurrence; lower priority at seq_len 512.

Verdict: stay on linear/delta attention. The two levers with real evidence at small scale are
(a) injective (subtractive) normalization and (b) local modeling — and (b) is already shipped.

## Q2. Depth vs width at fixed tiny params (d64 L12 vs d96 L6 vs d128 L4)

- **Best evidence: "The Model Shape Behind Scaling Laws: A Gradient Superposition Perspective"**
  (2026-05-27, v2 2026-10-03) — https://arxiv.org/abs/2605.27989 . Pretrains LMs across shapes and
  budgets; finds the loss/F relationship among the BEST shapes selected by validation loss, and
  frames allocation as "preserve task-relevant computation while reducing amplification of error
  responses". Takeaway: shape selection should be driven by an observable (their F = Frobenius norm
  of the input AGOP), not by folklore ratios. Abstract-level only — no drop-in number.
- **Recurrent / weight-tied depth: Tiny Recursive Model** (Jolicoeur-Martineau, 2025-10-06)
  https://arxiv.org/abs/2510.04871 — a SINGLE 2-layer network recursed at different frequencies,
  7M params, beats LLMs on ARC-AGI-1/2. Evidence that effective depth >> physical depth at tiny
  parameter counts. We already have the mechanism: `--tie-depth`.
- **Weak / do-not-cite: "Depth vs Width Tradeoff in MLPs Under Fixed Parameter Budgets"**
  (clawrxiv 2603.00406) — https://www.clawrxiv.io/api/abs/2603.00406 — MLPs, no skip connections,
  5K/20K/50K params, single seed, synthetic tasks; concludes "2 hidden layers is a robust default".
  Toy evidence, does not transfer to a 6-layer transformer with residual streams. Listed so nobody
  cites it as authority.
- Nonuniform width is real but out of reach: "> <former" variable-width (arXiv 2606.18246) —
  wider early/late, narrower middle, beats parameter-matched uniform baselines at 200M-2B. At 1.28M
  params the accounting overhead of a resize mechanism likely eats the gain. Park it.

Verdict: our current d96/L6 is a defensible shape. The cheap, on-premise test is `--tie-depth`
(recurrent depth) BEFORE spending on a d128/L4 arm.

## Q3. Data-constrained training / many-epoch guidance (newer than Muennighoff 2023)

- Muennighoff et al., "Scaling Data-Constrained Language Models", now JMLR v26 (2025)
  https://jmlr.org/papers/volume26/24-1000/24-1000.pdf (orig. arXiv 2305.16264).
  Core results: **up to ~4 epochs of repeated data yields negligible change vs unique data**; beyond
  that the marginal value of a repeated token decays — the paper's repetition-decay term R_D, with
  R_D -> 0 meaning repeated tokens are worthless and R_D -> 1 meaning they are worth ~fresh.
  Their effective-data form: D' = U_D + R_D * U_D * (R_D * N_E - 1).
- Applied to us, directionally (their fit is LLM-scale, flag it): U_D = 122K, N_E = 64.
  With R_D ~ 0.4: D' ~= 122K + 0.4*122K*(0.4*64 - 1) ~= 1.32M effective tokens from ~7.81M passes.
  So 64 epochs is worth roughly ~11 epochs of fresh data — far better than 1 epoch, but ~17%
  efficient. **More epochs is the wrong lever; fresh/diverse rows are the right lever.**
- This directly supports the existing law that ADDING rows is allowed. It also means: if a run is
  going to be spent, spend it on NEW content, not on bumping `--epochs` again.

Verdict: do not raise epochs. If we want more capability per run, add fresh rows (or a second
distinct corpus slice) rather than re-consuming the same 122K.

## Q4. Generation pathologies: token loops / attractor collapse, 2025-2026 causes and fixes

Two 2026 papers, both directly applicable:

- **FOCUS & RePAIR: Mitigating Text Degeneration via Token-Level Guidance** — ICML 2026 **Spotlight**
  (2026-08-27) — https://arxiv.org/abs/2608.26676 . Mechanism: decoding is a dynamical process that
  enters and persists in a small set of recurrent contexts. They split the failure into **loop entry
  risk** and **loop persistence**, and show persistence is controlled by the **"escape mass"** assigned
  to plausible alternatives in the sampling set.
  - FOCUS: reweight distillation toward high-confidence teacher regions to suppress leakage.
  - **RePAIR: onset-centered positive/negative continuation pairs + a margin loss**, to promote
    plausible alternatives and prevent early commitment to a repetition loop. **This is a
    TRAINING-TIME objective**, not an inference hack.
- **One-neuron repetition surgery** (Gemma 4, arXiv 2606.13705, June 2026), writeup:
  https://groundy.com/articles/can-editing-one-neuron-fix-llm-repetition-loops/ . Repetition loops
  localize to a small set of **MLP neurons** (as few as ONE sign-inverted neuron in the E2B variant)
  and are removed by a one-time static weight edit with benchmark scores holding. Method = per-layer
  ablation -> per-neuron attribution -> confirm with full-generation sweeps (not a proxy metric).
  Trigger for the loops: **long bounded enumeration prompts** that force distinct tokens past any
  natural stopping point. Weight edits do NOT fix "doom loops" (self-correction over a fact the
  model never learned) — that is a knowledge problem, not a circuit.
  At our scale the sweep is trivial: 6 layers x 384 ffn_hidden = 2,304 neurons.

Cross-confirmation of our own CHECKPOINT LAW: the same writeup states plainly that "degeneration is
not an undertraining artifact — reducing model loss does not fix it and can make it worse", which is
exactly the heldout(macro) anti-correlation we already select against.

Verdict: our degenerate probe (51/60 attractor loops) is the real target, and there are two concrete,
cheap, independent attacks — one training-time (RePAIR margin loss) and one post-hoc (neuron sweep).

## Q5. Tied embeddings at vocab 4096 + head designs

- **"Weight Tying Biases Token Embeddings Towards the Output Space"** — Findings of ACL 2026
  (Lopardo et al.) — https://aclanthology.org/2026.findings-acl.2027/ (arXiv 2603.26663,
  summary with numbers: https://www.emergentmind.com/papers/2603.26663).
  Findings with numbers:
  - Tied matrix aligns with the OUTPUT (unembedding) space, not the input space: after optimal
    linear alignment, per-token cosine 0.719 (output) vs 0.525 (input) in OLMo-1B.
  - **>70% of the early learning signal through the tied matrix comes from the output pathway**
    (first 1000 steps).
  - Early layers pay a "first layer penalty": 2+ bit tuned-lens KL gap at the input layer vs untied.
  - Causally confirmed by scaling INPUT gradients 5x during training, which shifts the matrix away
    from output structure toward input structure.
  - IMPORTANT CAVEAT, stated by the authors: the 5x input-gradient scaling "does not consistently
    improve downstream performance" — it is a hard zero-sum representational trade-off, not a free win.
  - Their own framing for us: at small scale "embedding parameters constitute a large fraction of
    total parameters — over 70% in 70M models — justifying weight tying for efficiency"; untied wins
    at scale (Llama 3, OLMo-2/3, Qwen3 8B+ are untied).
- For OUR numbers: embeddings are 30.7% of 1.28M params, so we sit squarely in the "tying is
  defensible for efficiency" regime — but 30.7% is high enough that the representational penalty is
  plausible. Untying costs +393K params (+31%), which fights the "smallest model" premise.

Verdict: the on-premise lever is **input-gradient scaling** (a scalar on the input-embedding
gradient, opt-in), measured on the generation instrument — NOT untying. Treat the paper's own caveat
as the prior: expect a small or null downstream effect, and let the measurement decide.

## Q6. muP / muTransfer for width stepping d48 -> d64 -> d96

- **"mupscaling small models: Principled warm starts and hyperparameter transfer"** — ICML 2026
  (arXiv 2602.10545, 2026-02-11, v2 2026-07-02) — https://arxiv.org/abs/2602.10545 .
  Proposes width upscaling that, like Net2Net, copies and perturbs weights but with
  **theoretically grounded, width-dependent scalings for the perturbation noise AND the optimizer
  hyperparameters**. Two proved/derived properties:
  1. Under ZERO perturbation the upscaled model is **functionally equivalent to the base model
     throughout training** (so the warm start cannot be worse at step 0).
  2. Extends muP to give **hyperparameter transfer for upscaled models**, greatly cutting tuning cost.
  This maps EXACTLY onto our tier ladder: we stepped d64 -> d96 cold. A warm start would initialize
  d96 from the trained d64 checkpoint with width-scaled noise and transfer lr/init.
- Prior art for the general idea: u-muP / unit-scaled maximal update parametrization, ICLR 2025
  (arXiv 2407.17465) — https://arxiv.org/abs/2407.17465 .

Verdict: the single most directly reusable paper for our workflow. `--init-from <ckpt> --upscale-width`
as an opt-in flag; test whether d96-from-d64 beats cold d96 at equal steps.

## Q7. Anything new in 2026 that materially beats the above at this scale

Ranked by likely payoff for a 1.28M-param, 122K-token model:
1. RePAIR-style onset margin loss (Q4) — attacks our measured failure directly.
2. One-neuron / per-neuron ablation sweep (Q4) — cheap, no retrain, gives an interpretability readout.
3. mupscaling warm start (Q6) — improves every future tier step.
4. Input-gradient scaling for the tied embedding (Q5) — cheap, evidence-backed, honest prior = small.
5. Injective (subtractive) normalization + measure Delta vs DeltaConv (Q1) — expressivity of the
   linear attention we already run.
6. Head-level competitive gating (SLA, Q1) / Gated DeltaNet-2 erase-write decoupling (Q1) — real but
   second-order at seq_len 512.

---

# RANKED, CONCRETE, TESTABLE CHANGES FOR THIS MODEL

All are opt-in flags or a separate analysis binary; no default changes; synth1 byte-identical.

### 1. RePAIR-style onset-centered margin loss (train-time repetition fix)
- Evidence: FOCUS & RePAIR, ICML 2026 Spotlight — https://arxiv.org/abs/2608.26676
- What: build onset-centered (positive, negative) continuation pairs from the corpus — onset = the
  point in a reply where it would begin to loop; positive = a plausible alternative continuation,
  negative = the repeated continuation. Add a margin loss that raises the escape mass on the
  positive. Flag: `--repair-margin <w>` (default 0 = off, bit-identical).
- Measure: probe loop rate (currently 51/60 attractor loops) + generation overlap. Not loss.

### 2. Per-neuron MLP ablation / attribution sweep for the loop circuit
- Evidence: arXiv 2606.13705, writeup https://groundy.com/articles/can-editing-one-neuron-fix-llm-repetition-loops/
- What: a separate analysis binary that zeroes (and sign-flips) each of the 2,304 ffn neurons
  (6 layers x 384) and re-runs a fixed probe set, ranking neurons by loop-rate delta. Confirm
  candidates with full generation sweeps, not a proxy. If a few neurons carry the attractor, a
  static weight edit removes it with no retraining.
- Measure: probe loop rate before/after; also verify general generations do not degrade.

### 3. mupscaling warm start for the tier ladder
- Evidence: arXiv 2602.10545 (ICML 2026) — https://arxiv.org/abs/2602.10545 ; u-muP arXiv 2407.17465
- What: `--init-from <ckpt> --upscale-width <d>` — copy+perturb the trained d64 into d96 with
  width-dependent noise scaling, and transfer lr/init. Property (1) guarantees functional
  equivalence at zero perturbation, so this cannot be worse at step 0.
- Measure: d96-from-d64 vs cold d96 at equal steps, on generation overlap + probe.

### 4. Input-gradient scaling on the tied embedding
- Evidence: arXiv 2603.26663 / Findings ACL 2026 — https://aclanthology.org/2026.findings-acl.2027/
- What: scalar multiplier on the input-embedding gradient path only. Flag: `--in-grad-scale <s>`
  (default 1.0 = bit-identical). Sweep s in {1, 2, 5} — 5x is the paper's intervention point.
- Measure: generation overlap + probe. Prior from the paper: expect small/null downstream effect;
  the value is that it is cheap and it settles the tied-vs-untied question without +31% params.

### 5. Injective normalization + measure the DeltaConv local-modeling term
- Evidence: InLine "Bridging the Divide" — https://arxiv.org/html/2412.06590v1 ; SLA —
  https://arxiv.org/abs/2602.01744
- What: (a) add a new opt-in `LayerArch` variant using **subtractive** normalization (instead of
  division) to restore injectivity; (b) run the Delta vs DeltaConv ablation we already have the
  switch for, measured on generation, not just loss. Additive enum arm keeps `Delta` checkpoints
  byte-identical.
- Measure: generation overlap + probe; loss is secondary.

---

# DO NOT BOTHER (with reasons)

- **Inference-time repetition penalties / n-gram blocking.** Loops "survive most sampling
  adjustments" (groundy.com, citing arXiv 2606.13705); by the 3rd-4th repetition almost any
  non-blocking intervention is insufficient. Symptom, not cause. We already know this.
- **Raising `--epochs` again.** Data-constrained law: ~4 epochs ~= unique data; beyond that,
  repetition decay. We are at 64 epochs over 122K = ~17% efficient (Q3). Add fresh rows instead.
- **Swapping the delta-rule recurrence for full softmax attention.** At seq_len 512 / d96 the
  quadratic term is irrelevant, and the measured linear-attention deficits (injectivity, local
  modeling) are addressable in place — local modeling is already shipped as DeltaConv.
- **The clawrxiv MLP depth-vs-width sweep (2603.00406) as authority.** Toy MLPs, no skip
  connections, 5K-50K params, one seed, synthetic tasks. Do not import its "2 hidden layers" rule.
- **Blind width widening on the tier ladder.** mupscaling (2602.10545) says upscaling needs
  principled warm starts + hyperparameter transfer; widening cold is leaving value on the table.
- **Untying the embeddings outright.** +393K params (+31%) for a trade-off the source paper itself
  says is not consistently a downstream win at small scale. Try input-gradient scaling first.

---

---

# ADDENDUM (verified against the live code, 2026-10-10 ~17:15 ET)

## The width ladder constrains the Q3 recommendation — read this before any epoch or corpus change

Source: `train/src/prepare.rs` (`shape_for_corpus_ffn`, `param_count_for`, `epochs_for_chinchilla`)
and `train/src/bin/train.rs`.

- Ladder: `WIDTH_RUNGS = [48, 64, 96]`, `MIN_PLANNED_TPP = 6.0`.
  `planned_tpp = train_tokens * epochs_for_chinchilla(tokens, params) / params`, where
  `epochs_for_chinchilla = clamp(ceil(20*params/tokens), 4, 64)`.
- `param_count_for = vocab*d + layers*(4d^2 + 6d + 2 + 3*d*ffn) + d`. This reproduces
  `config.txt` exactly (d96 -> 1,281,516), which is what makes the table below trustworthy.
- `chosen` starts at D_MIN=48 and is overwritten as each rung passes; the loop BREAKS on the first
  failure — so the survivor is the LAST rung that passed, not the first failure.

| rung | params | epochs at 121,992 tok | planned_tpp | verdict |
|---|---|---|---|---|
| d48 | 419,580 | 64 | 18.61 | PASS |
| d64 | 657,740 | 64 | 11.87 | PASS |
| d96 | 1,281,516 | 64 | **6.09** | PASS (marginal) |
| d128 | 2,101,900 | 64 | 3.71 | FAIL (matches the "d128 withheld" comment) |

Two consequences that correct a common misreading:

1. **`--epochs` cannot collapse the ladder.** Shape resolves first (train.rs prints the `tier:` line
   ~line 270); the `--epochs` override is applied later (line 1161); and the ladder uses its OWN
   `epochs_for_chinchilla(tokens, params)` — a function of PARAMS, not of the override.
2. **Falling off d96 lands on d64, not d48.** d48 requires tokens < 61,664.

**LIVE RISK: d96 holds only while `train_tokens >= 120,143`. We are at 121,992 — 1,849 tokens
(1.52%) of headroom.** Any corpus operation that deletes or trims rows below that silently demotes
the run to d64 with no error. Operational rule: gate row-DELETING corpus ops on a token recount
against 120,143; in-place rewrites are safe; adding rows is safe and also pulls `epochs` off the
clamp cap of 64 toward the 20:1 plan (the Q3 direction).

---

# HONESTY / LIMITS

- Several search hits resolved to Chinese-language SEO mirrors; the URLs above are the English
  primary sources (arXiv / ACL Anthology / JMLR / NVIDIA / ICML) and were fetched directly.
- 2605.27989 (depth-width shape) is abstract-level here — no drop-in number extracted.
- 2602.10545's "functionally equivalent under zero perturbation" is a proof about THEIR upscaling
  operator; adopting it means adopting their noise/optimizer scalings, not a hand-rolled widen.
- The Muennighoff D' arithmetic in Q3 is directional: their R_D is fit at LLM scale, ours is a
  1.28M-param model whose corpus is smaller than its parameter count. Treat it as "fresh data beats
  more epochs", not as a precise effective-token count.
- None of the above has been tested on our artifact yet. Each item is a hypothesis with a named
  instrument; the file, not the note, decides.
