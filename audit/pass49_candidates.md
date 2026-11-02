# pass 49 candidates -- three classes the current gates cannot see

Measured 2026-10-20 against the live corpus: **7676 rows**.
Instruments: `scripts/synth2_parrotscan.py`, `scripts/synth2_vocab_census.py`.
Every row below was read in context; the false positives are listed at the bottom.

## 1. PARROT -- the screen only ever sees staged batches

`synth2_stagecheck.py` hard-fails a batch on a 6-gram parrot, and the lead verify does
the same (`errors.append(...verbatim 6-gram parrot...)`). Both only see a batch at
staging time, so every batch staged before the rule tightened kept its parrots and no
later gate can see them. **274 landed rows breach today's rule.**

| lane | rows | share |
|---|---|---|
| casual | 238 | 11.9% |
| lazy | 2 | 0.1% |
| angry | 34 | 1.7% |
| sexy | 0 | 0.0% |
| **total** | **274** | **3.6%** |

Rule check: identical count under the stagecheck rule (any user turn in the row) and
the lead-verify rule (the immediately preceding user turn only) -- 274 either way, so the
number does not depend on which variant is canonical. Instrument agreement: 0 on
`tmp_b4415` (lead-verified green), 274 on the corpus.

Ids:

```
st2_casual_000266
st2_casual_000450
st2_casual_000457
st2_casual_000467
st2_casual_000482
st2_casual_000514
st2_casual_000525
st2_casual_000544
st2_casual_000555
st2_casual_000560
st2_casual_000608
st2_casual_000613
st2_casual_000638
st2_casual_000642
st2_casual_000645
st2_casual_000648
st2_casual_000652
st2_casual_000682
st2_casual_000693
st2_casual_000703
st2_casual_000717
st2_casual_000720
st2_casual_000748
st2_casual_000802
st2_casual_000804
st2_casual_000807
st2_casual_000808
st2_casual_000812
st2_casual_000817
st2_casual_000819
st2_casual_000826
st2_casual_000827
st2_casual_000829
st2_casual_000830
st2_casual_000882
st2_casual_000903
st2_casual_000904
st2_casual_000925
st2_casual_000927
st2_casual_000938
st2_casual_000939
st2_casual_000945
st2_casual_000949
st2_casual_000955
st2_casual_000956
st2_casual_000957
st2_casual_000965
st2_casual_001031
st2_casual_001035
st2_casual_001042
st2_casual_001043
st2_casual_001076
st2_casual_001099
st2_casual_001109
st2_casual_001111
st2_casual_001118
st2_casual_001126
st2_casual_001137
st2_casual_001150
st2_casual_001157
st2_casual_001164
st2_casual_001169
st2_casual_001171
st2_casual_001174
st2_casual_001177
st2_casual_001182
st2_casual_001187
st2_casual_001189
st2_casual_001194
st2_casual_001197
st2_casual_001212
st2_casual_001220
st2_casual_001231
st2_casual_001232
st2_casual_001235
st2_casual_001236
st2_casual_001237
st2_casual_001239
st2_casual_001240
st2_casual_001242
st2_casual_001247
st2_casual_001249
st2_casual_001254
st2_casual_001255
st2_casual_001257
st2_casual_001260
st2_casual_001261
st2_casual_001262
st2_casual_001263
st2_casual_001264
st2_casual_001265
st2_casual_001271
st2_casual_001274
st2_casual_001284
st2_casual_001286
st2_casual_001289
st2_casual_001304
st2_casual_001315
st2_casual_001317
st2_casual_001318
st2_casual_001320
st2_casual_001321
st2_casual_001323
st2_casual_001324
st2_casual_001325
st2_casual_001326
st2_casual_001327
st2_casual_001332
st2_casual_001333
st2_casual_001334
st2_casual_001335
st2_casual_001337
st2_casual_001341
st2_casual_001344
st2_casual_001346
st2_casual_001347
st2_casual_001348
st2_casual_001352
st2_casual_001354
st2_casual_001356
st2_casual_001357
st2_casual_001415
st2_casual_001421
st2_casual_001424
st2_casual_001428
st2_casual_001431
st2_casual_001436
st2_casual_001442
st2_casual_001448
st2_casual_001449
st2_casual_001450
st2_casual_001453
st2_casual_001455
st2_casual_001457
st2_casual_001461
st2_casual_001466
st2_casual_001470
st2_casual_001484
st2_casual_001486
st2_casual_001487
st2_casual_001488
st2_casual_001489
st2_casual_001490
st2_casual_001492
st2_casual_001493
st2_casual_001495
st2_casual_001499
st2_casual_001500
st2_casual_001501
st2_casual_001503
st2_casual_001504
st2_casual_001506
st2_casual_001507
st2_casual_001512
st2_casual_001516
st2_casual_001517
st2_casual_001518
st2_casual_001520
st2_casual_001521
st2_casual_001522
st2_casual_001523
st2_casual_001527
st2_casual_001529
st2_casual_001532
st2_casual_001533
st2_casual_001534
st2_casual_001537
st2_casual_001539
st2_casual_001540
st2_casual_001541
st2_casual_001548
st2_casual_001549
st2_casual_001550
st2_casual_001551
st2_casual_001555
st2_casual_001556
st2_casual_001558
st2_casual_001559
st2_casual_001562
st2_casual_001563
st2_casual_001565
st2_casual_001566
st2_casual_001567
st2_casual_001568
st2_casual_001572
st2_casual_001573
st2_casual_001574
st2_casual_001575
st2_casual_001577
st2_casual_001578
st2_casual_001580
st2_casual_001582
st2_casual_001583
st2_casual_001584
st2_casual_001585
st2_casual_001588
st2_casual_001590
st2_casual_001611
st2_casual_001617
st2_casual_001622
st2_casual_001669
st2_casual_001679
st2_casual_001680
st2_casual_001683
st2_casual_001689
st2_casual_001691
st2_casual_001692
st2_casual_001693
st2_casual_001694
st2_casual_001695
st2_casual_001696
st2_casual_001699
st2_casual_001700
st2_casual_001702
st2_casual_001744
st2_casual_001749
st2_casual_001812
st2_casual_001834
st2_casual_001843
st2_casual_001868
st2_casual_001874
st2_casual_001881
st2_casual_001883
st2_casual_001888
st2_casual_001926
st2_casual_001941
st2_casual_001948
st2_casual_001950
st2_casual_001951
st2_casual_001952
st2_casual_001957
st2_casual_001958
st2_casual_001960
st2_casual_001961
st2_casual_001962
st2_casual_001964
st2_casual_001965
st2_casual_001992
st2_lazy_000761
st2_lazy_001901
st2_angry_000175
st2_angry_000590
st2_angry_000616
st2_angry_000644
st2_angry_000707
st2_angry_000818
st2_angry_000888
st2_angry_000905
st2_angry_000930
st2_angry_001006
st2_angry_001012
st2_angry_001016
st2_angry_001102
st2_angry_001194
st2_angry_001232
st2_angry_001416
st2_angry_001609
st2_angry_001694
st2_angry_001737
st2_angry_001816
st2_angry_001831
st2_angry_001861
st2_angry_001864
st2_angry_001870
st2_angry_001873
st2_angry_001879
st2_angry_001883
st2_angry_001884
st2_angry_001887
st2_angry_001889
st2_angry_001903
st2_angry_001954
st2_angry_001958
st2_angry_001978
```

## 2. Vocabulary residual after pass 47

Pass 47 cut the SAFE tier from 88 rows to 18. These are the terms it did not reach

| term | US | rows | ids |
|---|---|---|---|
| school run | school drop-off | 7 | st2_casual_000343, st2_casual_000545, st2_casual_001076, st2_casual_001199, st2_casual_001201, st2_casual_001514, st2_casual_001786 |
| gran | grandma | 4 | st2_casual_001118, st2_casual_001131, st2_casual_001225, st2_casual_001646 |
| satnav | gps | 1 | st2_casual_001013 |
| traffic warden | parking enforcement | 1 | st2_casual_001938 |
| chap | guy | 1 | st2_casual_001194 |
| dual carriageway | divided highway | 1 | st2_casual_000643 |
| faff | hassle | 1 | st2_casual_001159 |
| hob | stovetop | 1 | st2_casual_000171 |
| loo | bathroom | 1 | st2_casual_000834 |

`satnav` is 1 row but 4 turns (`st2_casual_001013`), which is why the lead's b4175 patch
and the corpus row both needed all turns touched.

## 3. Currency -- 21 rows, all sterling, none of them weight

`pounds` is legal US for weight, so a bare term match is useless. All 21 rows are
currency (`forty five pounds`, `twelve pounds return`), so the class is clean:

st2_casual_001064, st2_casual_001087, st2_casual_001194, st2_casual_001294, st2_casual_001305, st2_casual_001319, st2_casual_001356, st2_casual_001375, st2_casual_001422, st2_casual_001425, st2_casual_001428, st2_casual_001430, st2_casual_001431, st2_casual_001582, st2_casual_001588, st2_casual_001643, st2_casual_001649, st2_casual_001782, st2_casual_001806, st2_casual_001836, st2_casual_001962

## 4. UK setting -- 29 rows

Not stray vocabulary: these rows are *set* in Britain, and a lexicon cannot hold a
place name. The markers co-occur (L1206: leeds + doncaster + carriage; L1597: national
trust + paddington + britain), which is what a row written as England looks like.

| id | markers |
|---|---|
| st2_casual_000432 | bank holiday |
| st2_casual_000442 | lake district |
| st2_casual_000475 | bristol |
| st2_casual_000504 | bank holiday |
| st2_casual_000505 | allotment |
| st2_casual_000549 | pub quiz |
| st2_casual_000553 | whitstable |
| st2_casual_000643 | allotment |
| st2_casual_000802 | york, full english |
| st2_casual_000908 | pub quiz |
| st2_casual_000926 | hen do |
| st2_casual_000934 | brighton, stag do |
| st2_casual_000953 | pancake day |
| st2_casual_001031 | bonfire night |
| st2_casual_001124 | primary school |
| st2_casual_001176 | hmrc |
| st2_casual_001206 | leeds, doncaster, carriage |
| st2_casual_001305 | allotment |
| st2_casual_001408 | allotment |
| st2_casual_001597 | national trust, paddington, britain |
| st2_casual_001647 | bonfire night |
| st2_casual_001728 | allotment |
| st2_casual_001783 | boxing day |
| st2_casual_001805 | skye, glasgow, scotland, hire car |
| st2_casual_001806 | liverpool |
| st2_casual_001842 | boxing day |
| st2_casual_001913 | allotment |
| st2_casual_001923 | bonfire night |
| st2_casual_001943 | allotment |

## Excluded after reading -- do not re-litigate

| term | why it is not a defect |
|---|---|
| pavement (3 rows) | `wet pavement`, `hot pavement`, `on the pavement` are all idiomatic US; US pavement means the paved surface |
| cooker (3) | every hit is `slow cooker` / `rice cooker` |
| jumper (1) | `jumper cables` |
| stone (3) | pizza stone, curling stone -- the object, not the weight unit |
| tube (6) | bicycle inner tube |
| boots (17) | rain boots / walking boots, not the pharmacy chain |
| oyster (1) | seafood; the row's real defect is the town name |
| st2_sexy_000789 | `spoke in a british accent` -- a character imitating one, legitimate |

## Note

`st2_casual_001195` is in the UK set because the assistant calls a task `the most british
campaign there is` -- the voice identifying itself, not a place reference.

