# run 14 --sample-sweep vs run 13 (NOISE-FLOOR read)

run 13 = best.bin sha256 `821c9cfe...` (pre-run-14 reference)
run 14 = best.bin sha256 `748b63b5...` (final step 16596; best.bin == final.bin)

Run 14 is a REPEAT of run 13's config on the b2750-fixed corpus. Every
difference below is therefore NOISE, and its SIZE is the floor any real
effect must clear.

## Greedy baseline (the apples-to-apples cell)

| observable | run 13 | run 14 | delta |
|---|---|---|---|
| loops | 3 | 8 | +5 |
| of 60 | 60 | 60 | +0 |
| eos | 59 | 60 | +1 |
| echo | 0.097 | 0.096 | -0.001 |
| selfrep | 0.019 | 0.013 | -0.006 |

## Per-cell echo (sampled decoding, 16 cells)

| temp/topk | run 13 | run 14 | delta |
|---|---|---|---|
| 0.00 / - | 0.097 | 0.096 | -0.001 |
| 0.50 / 0 | 0.088 | 0.088 | +0.000 |
| 0.50 / 10 | 0.090 | 0.102 | +0.012 |
| 0.50 / 100 | 0.087 | 0.098 | +0.011 |
| 0.50 / 40 | 0.096 | 0.099 | +0.003 |
| 0.70 / 0 | 0.087 | 0.093 | +0.006 |
| 0.70 / 10 | 0.092 | 0.088 | -0.004 |
| 0.70 / 100 | 0.097 | 0.091 | -0.006 |
| 0.70 / 40 | 0.093 | 0.080 | -0.013 |
| 0.90 / 0 | 0.077 | 0.091 | +0.014 |
| 0.90 / 10 | 0.093 | 0.093 | +0.000 |
| 0.90 / 100 | 0.093 | 0.088 | -0.005 |
| 0.90 / 40 | 0.087 | 0.096 | +0.009 |
| 1.00 / 0 | 0.076 | 0.075 | -0.001 |
| 1.00 / 10 | 0.084 | 0.082 | -0.002 |
| 1.00 / 100 | 0.081 | 0.078 | -0.003 |
| 1.00 / 40 | 0.086 | 0.096 | +0.010 |

mean |delta echo| = **0.0059**, max = **0.014**

## Best cell (selected by the tool)

- run 13: temp 0.70 topk 100 -> echo 0.097
- run 14: temp 0.50 topk 10 -> echo 0.102

## VERDICT

- **echo is STABLE**: greedy 0.097 -> 0.096 (delta -0.001) on two same-config runs.
  So the ~90% ungrounded gap is NOT noise -- it is a real property of the model.
- **loops is NOT stable**: greedy 3/60 -> 8/60 (+5) on the SAME config. On n=60 that
  is the floor: a loop-count change must exceed ~5 probes to be visible at all.
  DO NOT rank runs or interventions on loop count alone (this is the third time this
  has bitten: run 13's own sweep found `loops` had 3 distinct values across 2,304 neurons).
- **selfrep is noisy at this scale**: 0.019 -> 0.013 (+-0.006 on the same config).
- **The winning CELL is noise-driven**: run 13 picked 0.70/100, run 14 picked 0.50/10.
  Which cell 'wins' carries no information at this sample size.
- The decoded samples are the SAME failure mode in both runs (word salad, e.g.
  'do the gardenenenenenengege anything good then, then?'). The b2750 fix changed nothing
  measurable -- consistent with run 13 vs 14 being a genuine noise-floor pair.
