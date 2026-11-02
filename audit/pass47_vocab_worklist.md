# British-vocabulary census (pass 47 worklist)

Built by `scripts/synth2_vocab_census.py` from `research/us_english_lexicon.md`.
Independent of the US-spelling flag, which is why it reaches rows pass 46 could not.

lanes: casual, lazy, angry, sexy | rows: 6746 | lexicon terms: 89

**SAFE = mechanical substitution, no judgement needed.** Every hit below was read in
context before it entered this list; the false positives are in the EXCLUDED table at
the bottom so nobody re-litigates them.

## SAFE tier -- 29 terms, 88 rows

| term | US | rows | ids |
|---|---|---|---|
| high street | main street | 9 | st2_casual_000023, st2_casual_000041, st2_casual_000640, st2_casual_001092, st2_casual_001126, st2_casual_001131, st2_casual_001417, st2_casual_001875, st2_casual_001951 |
| charity shop | thrift store | 7 | st2_casual_000558, st2_casual_000790, st2_casual_000939, st2_casual_001479, st2_casual_001576, st2_casual_001582, st2_casual_001732 |
| fiver | five | 7 | st2_casual_000828, st2_casual_000939, st2_casual_001270, st2_casual_001638, st2_casual_001874, st2_casual_001951, st2_casual_001956 |
| roadworks | road construction | 7 | st2_casual_000041, st2_casual_000380, st2_casual_000545, st2_casual_000608, st2_casual_001011, st2_casual_001463, st2_casual_001498 |
| school run | school drop-off | 7 | st2_casual_000343, st2_casual_000545, st2_casual_001076, st2_casual_001199, st2_casual_001201, st2_casual_001514, st2_casual_001786 |
| tenner | ten | 6 | st2_casual_000946, st2_casual_000949, st2_casual_001179, st2_casual_001352, st2_casual_001417, st2_casual_001866 |
| car park | parking lot | 5 | st2_casual_000544, st2_casual_000616, st2_casual_000673, st2_casual_001494, st2_casual_001944 |
| gran | grandma | 4 | st2_casual_001118, st2_casual_001131, st2_casual_001225, st2_casual_001646 |
| half six | six thirty | 4 | st2_casual_000155, st2_casual_000288, st2_casual_000408, st2_casual_001506 |
| car boot | trunk | 3 | st2_casual_000791, st2_casual_000940, st2_casual_001932 |
| council tax | property tax | 3 | st2_casual_001073, st2_casual_001436, st2_casual_001520 |
| pavement | sidewalk | 3 | st2_casual_001199, st2_casual_001782, st2_angry_000454 |
| bin bag | trash bag | 2 | st2_casual_000558, st2_casual_001421 |
| chemist | pharmacy | 2 | st2_casual_001486, st2_casual_001492 |
| payslip | pay stub | 2 | st2_casual_000763, st2_casual_001711 |
| pence | cents | 2 | st2_casual_000796, st2_casual_001421 |
| retail park | strip mall | 2 | st2_casual_001104, st2_casual_001644 |
| traffic warden | parking enforcement | 2 | st2_casual_000640, st2_casual_001938 |
| caravan | trailer | 1 | st2_casual_000815 |
| chap | guy | 1 | st2_casual_001194 |
| chuffed | thrilled | 1 | st2_casual_001949 |
| crisps | chips | 1 | st2_casual_000646 |
| dual carriageway | divided highway | 1 | st2_casual_000643 |
| faff | hassle | 1 | st2_casual_001159 |
| hob | stovetop | 1 | st2_casual_000171 |
| loo | bathroom | 1 | st2_casual_000834 |
| number plate | license plate | 1 | st2_casual_001944 |
| satnav | gps | 1 | st2_casual_001013 |
| village hall | community center | 1 | st2_casual_000813 |

## SAFE detail -- the exact turn to rewrite

### high street -> main street  (9 rows)

- `st2_casual_000023` b2015 **assistant**: yeah, a good weekend. we tried that new cafe on the high street.
- `st2_casual_000041` b2030 **user**: did you hear about the roadworks on the high street?
- `st2_casual_000640` b2195 **user**: that traffic warden on high street is relentless.
- `st2_casual_001092` b2345 **user**: got a parking ticket on the high street.
- `st2_casual_001126` b2375 **user**: book it. it's the cheapest confidence boost on the high street.
- `st2_casual_001126` b2375 **assistant**: booked for thursday then, the cheapest confidence boost on the high street.
- `st2_casual_001131` b2375 **user**: down half a size. my gran's ring, so i want someone careful, not the cheapest high street chain.
- `st2_casual_001417` b2570 **user**: my butcher on the high street does a deal on tuesdays.
- `st2_casual_001875` b2885 **user**: new cafe opened on the high street.
- `st2_casual_001951` b2945 **user**: tried a new bakery on the high street this morning.
- `st2_casual_001951` b2945 **assistant**: tried a new bakery on the high street, what did you pick up?

### charity shop -> thrift store  (7 rows)

- `st2_casual_000558` b2165 **user**: a single ice skate. one. from a charity shop trip i have no memory of.
- `st2_casual_000558` b2165 **assistant**: a single ice skate from a charity shop, best thing all week.
- `st2_casual_000790` b2225 **user**: dropped some things at the charity shop.
- `st2_casual_000790` b2225 **assistant**: what did you take down to the charity shop then?
- `st2_casual_000939` b2270 **user**: the charity shop on church street is a goldmine now.
- `st2_casual_000939` b2270 **assistant**: what did you find in that goldmine of a charity shop?
- `st2_casual_001479` b2600 **user**: one perfectly good ladder, now mine, and a wardrobe that went to the charity shop by lunchtime.
- `st2_casual_001576` b2645 **user**: thirty odd, mostly from charity shops. they are cheap and sound great.
- `st2_casual_001576` b2645 **assistant**: charity shops are a goldmine for vinyl. what did you play first?
- `st2_casual_001582` b2645 **user**: the charity shop had a real bargain today.
- `st2_casual_001582` b2645 **assistant**: charity shop had a real bargain today, did you come away with much?
- `st2_casual_001732` b2765 **user**: found a real bargain in the charity shop.
- `st2_casual_001732` b2765 **assistant**: what was the charity shop bargain, anything good this time?

### fiver -> five  (7 rows)

- `st2_casual_000828` b2240 **assistant**: then it's the wire snake or the plumber. the snake costs a fiver and a bit of dignity.
- `st2_casual_000939` b2270 **user**: a real wool coat for a fiver and a framed print that i've hung in the hall already.
- `st2_casual_000939` b2270 **assistant**: a fiver for a wool coat, that's a steal. i keep walking past that one, i'm going in.
- `st2_casual_001270` b2465 **user**: yes, forty prints for a fiver in the sale, and they arrived quick and bright.
- `st2_casual_001270` b2465 **assistant**: forty prints for a fiver deserves a quiet celebration. which frames next?
- `st2_casual_001638` b2705 **user**: the carvery near work does a midweek one for a fiver.
- `st2_casual_001638` b2705 **assistant**: a fiver carvery, that's practically a public service. how's the meat?
- `st2_casual_001874` b2885 **assistant**: washing line snapped in the wind? a new one is a fiver, get the thicker cord.
- `st2_casual_001951` b2945 **user**: three bucks, which stings, but the whole thing came in under a fiver.
- `st2_casual_001951` b2945 **assistant**: under a fiver for breakfast out is winning these days. i'll try the seven o'clock shift.
- `st2_casual_001956` b2945 **assistant**: worth a go before buying new, a fiver of descaler saves forty bucks.

### roadworks -> road construction  (7 rows)

- `st2_casual_000041` b2030 **user**: did you hear about the roadworks on the high street?
- `st2_casual_000041` b2030 **assistant**: yeah, the roadworks started monday. the bus now takes about ten years.
- `st2_casual_000380` b2105 **assistant**: trip home was slow. roadworks, nearly an hour. i just put a podcast on.
- `st2_casual_000545` b2165 **assistant**: was it the roadworks again, a forty minute school run is rough.
- `st2_casual_000608` b2180 **user**: town still a mess with the roadworks?
- `st2_casual_000608` b2180 **assistant**: town is still a mess with the roadworks, they closed the other end.
- `st2_casual_001011` b2300 **user**: roadworks everywhere this week.
- `st2_casual_001011` b2300 **assistant**: leave earlier or find a way around the roadworks each day.
- `st2_casual_001463` b2585 **user**: commute has got longer with the roadworks.
- `st2_casual_001463` b2585 **assistant**: commute longer with the roadworks, how much extra time each way?
- `st2_casual_001498` b2615 **user**: roadworks. one lane shut for resurfacing and nobody knew how to merge.
- `st2_casual_001498` b2615 **assistant**: roadworks with one lane shut for resurfacing, nobody knew how to merge.

### school run -> school drop-off  (7 rows)

- `st2_casual_000343` b2090 **user**: how was the school run this morning?
- `st2_casual_000343` b2090 **assistant**: chaotic as always, the school run. my youngest lost a shoe.
- `st2_casual_000545` b2165 **user**: the school run took forty minutes today.
- `st2_casual_000545` b2165 **assistant**: was it the roadworks again, a forty minute school run is rough.
- `st2_casual_001076` b2345 **user**: we were forty minutes on the school run this morning.
- `st2_casual_001076` b2345 **assistant**: forty minutes on the school run is a rough start, it eases.
- `st2_casual_001199` b2420 **user**: wore the wrong shoes for the school run today.
- `st2_casual_001201` b2420 **user**: that low sun at five o'clock is blinding on the school run.
- `st2_casual_001514` b2615 **user**: walking, all of it. i did the school run on foot and then the shops.
- `st2_casual_001514` b2615 **assistant**: walking, the school run on foot then the shops, it adds up fast.
- `st2_casual_001786` b2795 **user**: noticeably. the school run is no longer in full darkness and the birds have started up again.

### tenner -> ten  (6 rows)

- `st2_casual_000946` b2270 **user**: down about a tenner a month, mostly from the heating timer being honest at last.
- `st2_casual_000946` b2270 **assistant**: about a tenner a month less just for staring at a screen. that's a genuine result.
- `st2_casual_000949` b2270 **user**: i won a tenner on a scratch card.
- `st2_casual_000949` b2270 **assistant**: great start, a tenner on a scratch card, did you reinvest it?
- `st2_casual_001179` b2390 **user**: subscription i forgot about took another tenner.
- `st2_casual_001179` b2390 **assistant**: a subscription you forgot about taking a tenner, which one was it? do you remember signing up?
- `st2_casual_001352` b2525 **user**: never again. twenty minutes and a tenner for a full winter of clear glass.
- `st2_casual_001352` b2525 **assistant**: twenty minutes and a tenner for a full winter of clear glass, best value job there is.
- `st2_casual_001417` b2570 **user**: any three joints for a tenner, and he throws in bones for the dog. our tuesday roasts have improved beyond measure.
- `st2_casual_001866` b2870 **assistant**: car washed, i did it myself and saved a tenner.

### car park -> parking lot  (5 rows)

- `st2_casual_000544` b2165 **user**: she marched in without looking back and i cried in the car park like an idiot.
- `st2_casual_000544` b2165 **assistant**: she marched in without looking back and you cried in the car park.
- `st2_casual_000616` b2180 **assistant**: parking was a nightmare, took me three laps of the car park.
- `st2_casual_000673` b2210 **user**: car park was full so i circled three times.
- `st2_casual_001494` b2615 **user**: both, really. i said i would drive her and wait in the car park.
- `st2_casual_001944` b2930 **user**: car park at the leisure center now has number plate recognition.

### gran -> grandma  (4 rows)

- `st2_casual_001118` b2360 **user**: run walk, and i'm not ashamed. my sister and i are doing it for the hospice that looked after our gran.
- `st2_casual_001118` b2360 **assistant**: run walk for the hospice that looked after your gran, good cause.
- `st2_casual_001131` b2375 **user**: down half a size. my gran's ring, so i want someone careful, not the cheapest high street chain.
- `st2_casual_001131` b2375 **assistant**: gran's ring down half a size, use careful jewellers, not a chain.
- `st2_casual_001131` b2375 **user**: initials inside, so they've promised to protect them. i'm trusting strangers with my gran, essentially.
- `st2_casual_001225` b2435 **user**: we do a jigsaw with my gran every visit now.
- `st2_casual_001225` b2435 **assistant**: gran sky empire, every jigsaw has one. how many pieces is the current one?
- `st2_casual_001646` b2705 **user**: lifted and boxed in the shed, wrapped in newspaper like my gran taught me. fingers crossed they survive the loft.

### half six -> six thirty  (4 rows)

- `st2_casual_000155` b2060 **assistant**: half six, which is far too early a time for a saturday.
- `st2_casual_000288` b2075 **assistant**: a lie in, lucky you. i was up at half six.
- `st2_casual_000408` b2105 **assistant**: no lie in. the cat woke me at half six wanting breakfast, and once i'm up i'm up.
- `st2_casual_001506` b2615 **user**: roads were empty at half six this morning.
- `st2_casual_001506` b2615 **assistant**: roads empty at half six this morning, worth getting up early then?

### car boot -> trunk  (3 rows)

- `st2_casual_000791` b2225 **user**: doing a car boot on sunday.
- `st2_casual_000791` b2225 **assistant**: is it an early start for the car boot then?
- `st2_casual_000940` b2270 **user**: i did the car boot sale for the first time.
- `st2_casual_000940` b2270 **assistant**: selling or buying at the car boot sale, how was the first one?
- `st2_casual_001932` b2915 **assistant**: a car boot sale on saturday morning, that is the weekend plan.

### council tax -> property tax  (3 rows)

- `st2_casual_001073` b2345 **user**: the council tax bill came, it has gone up again.
- `st2_casual_001073` b2345 **assistant**: has the council tax bill gone up again, for what exactly?
- `st2_casual_001436` b2585 **user**: council tax letter came today.
- `st2_casual_001436` b2585 **assistant**: council tax letter today, the usual rise or has it gone up more?
- `st2_casual_001520` b2630 **user**: the council tax bill landed this morning.
- `st2_casual_001520` b2630 **assistant**: council tax bill landed this morning, is it up again this year?

### pavement -> sidewalk  (3 rows)

- `st2_casual_001199` b2420 **user**: smooth soled sneakers on a wet pavement. i did the penguin shuffle the whole way and still nearly went twice.
- `st2_casual_001782` b2795 **user**: a fortune, apparently, split with mathematical seriousness on the pavement. my daughter came home eleven pounds richer.
- `st2_casual_001782` b2795 **assistant**: eleven pounds of pavement math, a good night's work. were the carols tuneful?
- `st2_angry_000454` b3560 **user**: our dog cracked his paw pads on the hot pavement.

### bin bag -> trash bag  (2 rows)

- `st2_casual_000558` b2165 **assistant**: how many bin bags did clearing out the wardrobe produce?
- `st2_casual_001421` b2570 **assistant**: plain tin, same beans, the house survives. did you try the own brand bin bags too?

### chemist -> pharmacy  (2 rows)

- `st2_casual_001486` b2615 **assistant**: hay fever back with a vengeance this week, has the chemist anything?
- `st2_casual_001492` b2615 **user**: had my flu jab at the chemist on saturday.
- `st2_casual_001492` b2615 **assistant**: flu jab at the chemist on saturday, quick job or a long line?

### payslip -> pay stub  (2 rows)

- `st2_casual_000763` b2225 **assistant**: check your payslip, i hope the overtime is on there.
- `st2_casual_001711` b2750 **user**: got the first payslip call from my daughter about tax.
- `st2_casual_001711` b2750 **assistant**: that payslip shock call, every parent takes it. how did you explain?

### pence -> cents  (2 rows)

- `st2_casual_000796` b2225 **user**: twenty pence.
- `st2_casual_000796` b2225 **assistant**: twenty pence each way adds up, a monthly pass might be cheaper.
- `st2_casual_001421` b2570 **user**: forty pence a tin less, and the recipe review at home said identical. the tin looks plainer, that's all.

### retail park -> strip mall  (2 rows)

- `st2_casual_001104` b2345 **user**: i might try the place by the retail park.
- `st2_casual_001104` b2345 **assistant**: that place by the retail park is worth a call, usually cheaper.
- `st2_casual_001644` b2705 **user**: the van at the retail park does better coffee than the chains.

### traffic warden -> parking enforcement  (2 rows)

- `st2_casual_000640` b2195 **user**: that traffic warden on high street is relentless.
- `st2_casual_001938` b2930 **user**: got caught by the traffic warden while reading the parking sign.

### caravan -> trailer  (1 rows)

- `st2_casual_000815` b2240 **user**: a canal boat and a caravan. she's earned both.

### chap -> guy  (1 rows)

- `st2_casual_001194` b2405 **user**: quoted three hundred for a professional scrape. the chap said leave it alone unless it's blocking drainage, moss is mostly cosmetic.

### chuffed -> thrilled  (1 rows)

- `st2_casual_001949` b2930 **assistant**: a driving test passed first attempt, he must be chuffed.

### crisps -> chips  (1 rows)

- `st2_casual_000646` b2195 **assistant**: practicing! we'll see about that. i'll bring the good crisps and my finest useless facts.

### dual carriageway -> divided highway  (1 rows)

- `st2_casual_000643` b2195 **user**: brilliant but i need to learn the route properly. ended up on a dual carriageway for about ninety terrifying seconds.

### faff -> hassle  (1 rows)

- `st2_casual_001159` b2390 **assistant**: unpair it and pair it again, it is a faff but it works.

### hob -> stovetop  (1 rows)

- `st2_casual_000171` b2060 **assistant**: cleaned the kitchen, yes. it took longer than i'd admit, mostly because of the hob.

### loo -> bathroom  (1 rows)

- `st2_casual_000834` b2240 **user**: thanks. two uncles who don't speak, one baby, and a great aunt who needs the loo nearby. it's a puzzle.

### number plate -> license plate  (1 rows)

- `st2_casual_001944` b2930 **user**: car park at the leisure center now has number plate recognition.
- `st2_casual_001944` b2930 **assistant**: number plate recognition at the leisure center, mine does that too.

### satnav -> gps  (1 rows)

- `st2_casual_001013` b2300 **user**: satnav sent me the wrong way.
- `st2_casual_001013` b2300 **assistant**: did the satnav send you the wrong way into a field?
- `st2_casual_001013` b2300 **assistant**: nearly is bad enough, update the satnav, the maps go stale.
- `st2_casual_001013` b2300 **assistant**: i never think to either, do the satnav before the long trip.

### village hall -> community center  (1 rows)

- `st2_casual_000813` b2240 **assistant**: big fancy do or the village hall, cousin's wedding in june?

## FLAG tier -- 16 terms, 84 rows, HAND-READ (not defects)

| term | US | rows | why it needs a read |
|---|---|---|---|
| curry | curry | 20 | keep the word; "going for a curry" -> "grabbing Indian food" hand-read |
| chips | fries | 9 | FLAG: "bag of chips" context; "fish and chips" -> "fish and fries" |
| post office | post office | 9 | same in US; keep |
| mot | inspection | 8 | hand-read ("MOT test" -> "inspection") |
| wardrobe | closet | 7 | legal US for freestanding furniture; only the built-in sense is British |
| corner shop | corner store | 5 | corner store is live US (esp. NYC); read each |
| nursery | preschool | 5 | US nursery is the baby's room; preschool sense is British |
| bus pass | bus pass | 4 | keep |
| mate | man | 4 | FLAG: "mate" -> "man"/"dude" by rhythm; ghetto rows -> "bro" |
| payday | payday | 3 | same in US; keep |
| wonky | wobbly | 3 | used in US speech; lead dismissed 2026-10-18 |
| banging | fire | 2 | hand-read ("banging tunes" -> "fire tracks") |
| estate | the block | 2 | hand-read ("the estate" -> "the block"/"the hood" by register) |
| bookshop | bookstore | 1 | used in US speech; lead dismissed 2026-10-18 |
| burger van | food truck | 1 | two ordinary US words in sequence |
| kebab | gyro | 1 | hand-read ("kebab shop" -> "gyro spot") |

## Excluded as ordinary US English -- 21 terms

| term | why it is not a defect |
|---|---|
| boot | footwear is US; only the car context is British -- handled as FLAG |
| carriage | railroad carriage, baby carriage (lead msg #180) |
| cooker | all 3 hits are slow cooker / rice cooker, ordinary US appliances |
| council | city council is perfect US; only 'the council' is British |
| cupboard | legal US for kitchen cabinets (lead msg #180) |
| flat | flat tire, lying flat (FLAG list) |
| holiday | the holidays (Nov-Dec) is US |
| jumper | the 1 hit is jumper cables, ordinary US |
| lift | give a lift -> give a ride, but 'lift' alone is US |
| mad | FLAG: angry sense |
| match | FLAG: soccer only |
| mobile | used in US (mobile home, mobile app) |
| oyster | the 1 hit is seafood; the row's real defect is the town name whitstable |
| pint | a pint of beer is US too |
| proper | FLAG: intensifier only |
| queue | queue is used in US (queue up, in the queue at the DMV) |
| services | the word alone is US; only the compound is British |
| sorted | FLAG: adjective sense |
| sound | FLAG: audio sense is US |
| the tip | the 1 hit is a restaurant gratuity, not the rubbish dump |
| wafer | wafer cookie, wafer-thin (lead msg #180) |

## Not vocabulary -- found while reading, needs your call

| where | what |
|---|---|
| `st2_casual_000553` | assistant says `oysters and wind, the full whitstable experience` -- **Whitstable** is a Kent oyster town, a UK place reference in a US-English corpus. `oyster` itself is fine. |
| `st2_casual_000544` | assistant echoes the user turn almost verbatim (`she marched in without looking back and you cried in the car park`) -- PARROT, not vocabulary. |
| `st2_casual_0001126` | assistant repeats `the cheapest confidence boost on the high street` from the user turn -- PARROT, 8 shared grams. |

