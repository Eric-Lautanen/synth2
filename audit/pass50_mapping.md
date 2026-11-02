# pass 50 -- the relocation map

Decisions that have to be made once, before any row is rewritten. Written so
that 86 rows do not become 86 separate judgement calls.

**The set:** 86 rows -- casual 84, angry 1, sexy 1. See
`pass50_britain_worklist.md` for the row list and the two corrections that got
it there (63 -> 85 -> 87 -> 86).

## The thing that makes this pass different from pass 49

Pass 49 changed assistant turns only, and left every user turn untouched, so the
echo it verified stayed valid. **Pass 50 changes user turns.** That re-opens the
guarantee pass 49 just established:

    u: the school run took forty minutes today.
    a: a slow crawl then, was anything blocked?        <- echoes "slow"? no: "school", "minutes"

Relocate the user turn and the assistant echo can evaporate. So the rule for this
pass is not "swap the token" -- it is **rewrite the user turn, then re-derive the
assistant turn from it**, and re-run `synth2_changefile_check.py` on every row,
including the ones where only a user turn changed. A relocation chunk is not a
search-and-replace, and treating it as one is how pass 47 manufactured a
duplicate out of two rows that were already close.

## Two classes, and the order they run in

**Class A -- word swap.** The referent exists in the US under another name. The
scene survives; one or two tokens change. Mechanical, reviewable in bulk.

**Class B -- scene change.** There is no US referent, because the thing is a UK
institution or calendar event. The scene itself has to become a different scene,
which means the row is rewritten rather than edited. These are the ones to look
at one by one.

Run A first. It is most of the set and it does not disturb the topic.

## Class A -- the mapping

| term | rows | US rendering | note |
|---|---|---|---|
| mot | 8 | state inspection | `failed its inspection`; keep the cost and the inconvenience, drop the acronym |
| trolley | 6 | cart | shopping cart; the wobbly wheel survives |
| allotment | 6 | community garden | keeps the plot, the neighbours, the vegetables |
| optician | 4 | eye doctor | `optometrist` is correct but stiffer in speech |
| dressing gown | 4 | robe | |
| washing up | 3 | the dishes | `do the dishes`, `the dishes are still there` |
| bypass | 3 | the highway / the loop | depends on whether the row is about traffic or a route |
| airing cupboard | 3 | hall closet | the joke is a warm cupboard a pet sleeps in; a linen closet keeps it |
| wheelie bin | 3 | trash can | `rolling bin` if the row is about the wheels |
| bank holiday | 2 | long weekend | |
| snooker | 2 | pool | |
| joiner | 2 | carpenter | |
| school fete | 2 | school fair | |
| pub quiz | 2 | trivia night | |
| dales | 2 | the hills | |
| the rec | 2 | the park | |
| washing line | 2 | clothesline | |
| boxing day | 2 | the day after christmas | class A borderline: works if the row is about leftovers and lounging |
| surgery (the doctor) | 1 | doctor's office | |
| lake district | 1 | the mountains | or a named US range |
| full english | 1 | big breakfast | |
| hen do / stag do | 1 + 1 | bachelorette / bachelor party | |
| sports day | 1 | field day | |
| primary school | 1 | elementary school | |
| hmrc | 1 | the irs | |
| clocks going back | 1 | when daylight saving ends | US says daylight saving, not clocks |
| premium bonds | 1 | savings bonds | |
| single yellow | 1 | a no parking stretch | the marking is UK-only, the annoyance is not |
| bin collection | 1 | trash pickup | |
| mates rates | 1 | the friend price | |
| rounders | 1 | kickball | same playground game, same improvised rules |
| uni | 1 | college | |
| hire car | 1 | rental car | |
| milk float | 1 | milk delivery truck | the electric dawn delivery still exists in parts of the US |
| wellington | 1 | rain boot | |
| queue | 6 | line | word-level, not scene; kept out of the 86 on purpose |
| parish | 1 | the town / the church | weak either way; judge the row |

## Class B -- no referent, change the scene

| term | rows | what to do |
|---|---|---|
| bonfire night | 3 | no US equivalent. Nearest honest move: a backyard bonfire, or the fourth of july if the row is about fireworks and crowds |
| guy fawkes | 1 | same row family as bonfire night; goes with it |
| pancake day | 1 | no US equivalent. A pancake breakfast fundraiser keeps the food and the community |
| harvest festival | 1 | no US equivalent. A food drive keeps the function |
| national trust | 1 | a historic house / a preserved estate |
| paddington | 1 | swap for a US children's character; the row is about a beloved fictional bear |
| half term | 3 | borderline: `the kids are off school` covers it without naming a UK calendar |
| britain / british | 2 | one is a character doing an accent (legitimate, excluded); the other needs the sentence rebuilt |

## Place names -- decide once, not per row

Eleven rows carry a UK place. The corpus should not read as if every American
lives in a different city, and it should not read as if they all live in the same
one. Proposal: map to a small pool and reuse it, so the corpus has a consistent
geography rather than eleven one-offs.

| uk | us |
|---|---|
| bristol | portland |
| brighton | santa cruz |
| whitstable | cape may |
| doncaster, leeds | dayton, akron |
| liverpool | cleveland |
| glasgow | pittsburgh |
| skye, the dales, lake district | the adirondacks, the blue ridge |
| scotland | the pacific northwest |

## What does not change

Everything pass 49 established still holds after relocation: 10-13 words on
every assistant turn, lowercase, ASCII, no apostrophes, no hyphens, echo from the
turn immediately before, no 6-gram with any user turn in the row, no 5-gram with
the corpus outside the row, and no collision between the lines this pass writes.

The last two are the ones to watch, because this pass touches user turns as well,
so the edited-line count roughly doubles and the cross-line scan has twice as
much to compare.

## Sequencing

**Pass 49 must land before pass 50 is authored, not just before it applies.**
21 of the 86 rows are already rewritten by pass 49:

    000450 000802 000965 001031 001201 001255 001428 001489 001495 001527 001541
    001563 001566 001584 001617 001744 001868 001874 001941 001961 001965

`apply_rewrites.py` aborts on a text mismatch, so a pass 50 file written against
today's raw corpus will refuse to apply to those 21 rows the moment pass 49
lands. Write pass 50 against the post-pass-49 text: `old` must be what pass 49
left behind. That is also why the two passes cannot be interleaved.

Then:

1. Class A, in three chunks of about 25 rows, casual only.
2. Class B, one chunk, read row by row.
3. The two singletons (angry, sexy).
4. Re-run `synth2_changefile_check.py` on each chunk with the right `--lane`.
5. Final cross-file scan over every edited line from every pass, pass 49 included.
   For the 21 overlapping rows, compare only the pass 50 text -- the pass 49 text
   for those rows will no longer exist in the corpus.
