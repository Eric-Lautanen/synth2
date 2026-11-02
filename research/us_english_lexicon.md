# US English conversion lexicon (operator directive 2026-10-10 23:04 UTC)

Operator: "switch it to US english style. Not sure why it went br5ittish."
Scope: the whole live corpus (casual 2001 + ghetto 29) and every future row.
Method: script assembles a changes.json from these mappings -> apply_rewrites.py
applies (safe editor, asserts every old text) -> hand spot-checks -> all gates
-> conditioning.py + diversity.py re-verify. Word-boundary, case-preserving
matching (Mom if sentence-initial, etc.).

## AUTO pairs (unambiguous, mechanical)

| british | us | notes |
|---|---|---|
| mum | mom | also mum's -> mom's |
| mums | moms | |
| neighbour | neighbor | |
| colour | color | |
| favour | favor | |
| realise | realize | |
| organise | organize | |
| centre | center | |
| grey | gray | |
| tyre | tire | |
| kerb | curb | |
| aluminium | aluminum | |
| programme | program | |
| whilst | while | |
| fortnight | two weeks | adds a token; safe direction |
| flat | apartment | FLAG if "flat tire"/"flat battery" -- see FLAG list |
| lift | elevator | FLAG if "give you a lift" -> "give you a ride" |
| rubbish | trash | |
| brolly | umbrella | |
| telly | TV | |
| mobile | cell | "mobile phone" -> "cell phone" |
| holiday | vacation | FLAG if "the holidays" (keep) |
| torch | flashlight | |
| motorway | highway | |
| petrol | gas | "petrol station" -> "gas station" |
| sat nav | GPS | |
| postcode | zip code | |
| jumper | sweater | |
| trainers | sneakers | |
| trousers | pants | |
| chips | fries | FLAG: "bag of chips" context; "fish and chips" -> "fish and fries" |
| biscuit | cookie | |
| bin bag | trash bag | |
| bin day | trash day | |
| the tip | the dump | "run to the tip" -> "run to the dump" |
| quid | bucks | "three quid" -> "three bucks"; "fifty quid" -> "fifty bucks" |
| fiver | five | "a fiver" -> "five bucks" preferred |
| tenner | ten | "a tenner" -> "ten bucks" preferred |
| pint | beer | "grab a pint" -> "grab a beer" |
| queue | line | "in the queue" -> "in line" |
| cooker | stove | |
| windscreen | windshield | |
| boot | trunk | FLAG: car context only ("in the boot" -> "in the trunk") |
| nappy | diaper | |
| postie | mail carrier | |
| council | city | "the council" -> "the city"; "council flat" -> "city apartment"? hand-read |
| oyster | transit card | |
| five a side | pickup game | "five a side friday" -> "pickup game friday" |
| takeaway | takeout | |
| dodgy | sketchy | |
| skint | broke | |
| gutted | bummed | |
| knackered | beat | |
| bloke | guy | |
| geezer | old guy | hand-read; can be affectionate |
| cheers | thanks | FLAG: "cheers" as toast keeps; as thanks -> "thanks" |
| mate | man | FLAG: "mate" -> "man"/"dude" by rhythm; ghetto rows -> "bro" |
| lads | guys | "the lads" -> "the guys"/"the boys" |
| lad | guy | |
| mad | crazy | "went mad" -> "went crazy"; "are you mad" -> "are you crazy" |
| petrol prices | gas prices | |
| proper | really | FLAG: intensifier only ("proper good" -> "really good"); "proper noun" never appears |
| sound | cool | FLAG: "sound enough" -> "cool enough"; "the sound" (audio) keeps |
| sorted | handled | "it's sorted" -> "it's handled"/"all set" |
| innit | right? | ghetto register |
| bruv | bro | ghetto register |
| m8 | man | ghetto register |
| unc | unc | US street also uses "unc"; keep |
| fam | fam | US street uses "fam"; keep |
| allow it | forget it | ghetto register |
| say less | say less | US street uses this; keep |
| dead up | no cap | ghetto register; hand-read each |
| graft | grind | "that's graft" -> "that's grind"? hand-read |
| peng | fire | hand-read; rare |
| banging | fire | hand-read ("banging tunes" -> "fire tracks") |
| jokes | hilarious | "that was jokes" -> "that was hilarious" |
| tesco | the store | hand-read each ("beats the tesco ones" -> "beats the ones at the store") |
| kebab | gyro | hand-read ("kebab shop" -> "gyro spot") |
| curry | curry | keep the word; "going for a curry" -> "grabbing Indian food" hand-read |
| match | game | FLAG: "the match" (soccer) -> "the game"; only in soccer rows |
| derby | rivalry game | "derby day" -> "rivalry game day"? hand-read |
| estate | the block | hand-read ("the estate" -> "the block"/"the hood" by register) |
| payday | payday | same in US; keep |
| post office | post office | same in US; keep |
| motorway services | rest stop | hand-read |
| MOT | inspection | hand-read ("MOT test" -> "inspection") |
| the tube | the subway | hand-read |
| bus pass | bus pass | keep |
| rubbish tip | dump | covered by "the tip" |

## FLAG-ONLY list (never auto-replace; script lists occurrences, human rewrites)

- "flat" in "flat tire", "flat battery", "lying flat" -- keep
- "lift" in "give a lift", "lift share" -- "give a ride", "carpool"
- "chips" vs "crisps" -- British "chips" = fries; a "bag of chips" in US = crisps; hand-read
- "first floor" -- British ground+1 = US second floor; hand-read
- "football" -- corpus soccer rows: US "soccer" or reframe as "the game"; hand-read
- "holiday" in "the holidays" (Nov-Dec season) -- keep
- "trainers" as verb -- not present, but check
- "tip" as gratuity vs the dump -- hand-read
- "boot" as footwear -- hand-read
- "cheers" as a toast -- keep
- "proper" as "correct" -- hand-read
- "sound" as audio -- keep
- "mad" as angry (British) vs crazy -- "are you mad?" -> "are you crazy?" (US) usually; hand-read
- "sorted" as adjective for a person ("he's sorted") -- hand-read
- "quid" inside quotes/idioms -- always -> bucks
- "pants" (British: underwear) -- not present; the reverse mapping (trousers->pants) is safe
- "fag/f*g" -- not present (and stays out)
- "pavement" -> "sidewalk" -- scan for it
- "car park" -> "parking lot" -- scan for it
- "ring you" -> "call you" -- scan for it
- "mobile" as adjective ("mobile phone") -- "cell phone"
- "whilst" -> "while" -- auto
- "amongst" -> "among" -- scan
- "towards" -> "toward" -- optional; scan and decide
- "autumn" -> "fall" -- scan; "fall" collides with the verb, hand-read
- "biscuits and tea" -- cookie context
- "wellingtons/wellies" -> "rain boots" -- scan
- "jumper leads" -> "jumper cables" -- scan
- "hoover" -> "vacuum" -- scan
- "ice lolly" -> "popsicle" -- scan
- "full stop" -> "period" -- scan
- "zed" -> "zee" -- scan
- "maths" -> "math" -- scan
- "learnt" -> "learned", "dreamt" -> "dreamed", "spilt" -> "spilled", "burnt" -> "burned" -- scan (t-forms)
- "-ise" verbs generally (recognise, apologise, prioritise) -> "-ize" -- scan with the realise rule

## Register notes

- GHETTO (street_raw): British slang -> US street: bruv->bro, m8->man, innit->right?/no cap,
  allow it->forget it, dead up->no cap, fam/unc/say less keep, quid->bucks, estate->the block,
  peng/banging->fire, graft->grind. Keep profanity in-register; no slurs (protected groups) stays.
- CASUAL: mate->man/dude, bloke->guy, lads->guys, cheers->thanks, quid->bucks, pint->beer,
  takeaway->takeout, curry rows -> hand-read, match->game (soccer rows).
- The voice target is unchanged: plain everyday US English, the words a normal
  American actually types to a friend. Same naturalness test, US register.

## Verification protocol (per batch of conversions)

1. Script assembles changes.json (old text from the corpus, never typed by hand).
2. apply_rewrites.py --dry first, then apply (asserts every old; backs up outside raw/).
3. Hand-read 10 random changed rows per 100 + every FLAG-list rewrite in full.
4. Gates: repair --locations (0/0/1.000), integrity.py, qmark.py.
5. conditioning.py (zero-overlap must not regress; the noun echo survives the swap),
   diversity.py --sample-rows (matched size vs the pre-conversion backup).
6. Token recount vs the d96 floor 120,143 (additions are the safe direction; verify anyway).
7. Record the pass in the CORPUS CURATION LOG (README.md).
