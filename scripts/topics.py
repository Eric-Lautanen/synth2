"""Topic/family classifier for the synth2 corpus.

Directional, not exact: each row is classified by the FIRST family whose
keywords appear in the row's first user turn. Counts are for navigation
(which family is thin), so compare the ORDER of the table, not the deltas.

MATCHING IS WHOLE WORD. Every keyword is compiled to \\b<keyword>\\b, so a
keyword can only fire on a complete word. Plain substring matching made one
family's keyword fire inside another family's ordinary vocabulary, and it did
so on roughly a quarter of the corpus: `ate` inside "roommate" and "updated",
`body` inside "nobody", `eat` inside "sweater" and "theater", `fee` inside
"coffee", `app` inside "appointment", `mall` inside "small", `tow` inside
"towel", `shed` inside "vanished", `nap` inside "snapped", `tax` inside
"taxi", `bus` inside "bush", `ref` inside "reference", `rain` inside "train",
`form` inside "platform" and "performance", `wind` inside "window".

Because the old table relied on that accident for its inflections, the
inflections it was really matching are now written out in full (guilty,
felt, dogs, booked, charged, diagnoses, recycling, ...). Adding a word here
is safe; relying on the substring is not.
"""
import json, os, re, collections

RAW = r"C:\github\DBllm\runs\synth2\raw"

FAMILIES = [
    ("time + plans + routine", "monday|tuesday|wednesday|thursday|friday|saturday|sunday|mornings|morning|tonight|weekend|schedules|scheduled|scheduling|schedule|appointment time|alarm|alarms|clock|clocks|late|later|lately|early|earlier|earliest|plans|planned|planning|plan|calendars|calendar|routines|routine|every day|all day|last night|this week"),
    ("money + bills + fees", "bills|billed|billing|bill|fees|fee|charged|charges|charging|charge|invoices|invoiced|invoice|prices|pricing|price|costs|costing|cost|paid|pays|pay|payments|payment|refunded|refunds|refund|bank|banks|deposit|deposits|taxes|tax|rents|rented|renting|rental|rentals|rent|subscription|subscriptions|money|dollars|dollar|credits|credit|overdraft|overdrafts|interest"),
    ("food + drink + order", "coffee|pizza|sandwich|lunch|lunches|dinner|dinners|breakfast|restaurant|restaurants|menus|menu|order food|ordered|food|eats|eating|ate|eat|kitchens|kitchen|fridges|fridge|leftovers|leftover|grocery|groceries|snack|snacks|drinks|drink|beer|beers|bars|bar"),
    ("sleep + body + tired", "sleep|sleeps|sleeping|slept|nap|naps|bed|beds|tired|tiredness|exhausted|awake|insomnia|pillow|pillows|dream|dreams|snore|snores|bodies|body|sores|sore|headache|headaches|sick|flu|fever"),
    ("tech + phone + devices", "phones|phone|apps|app|wifi|internet|router|routers|password|passwords|logins|login|emails|email|text message|texted|updates|updated|update|downloads|downloaded|download|laptops|laptop|computers|computer|chargers|charger|batteries|battery|screens|screen|cameras|camera|printers|printer|streams|streaming|stream|devices|device"),
    ("work + office + job", "boss|bosses|manager|managers|offices|office|workers|worker|works|worked|working|work|coworkers|coworker|meetings|meeting|shifts|shift|jobs|job|clients|client|email at work|projects|project|deadlines|deadline|overtime|paychecks|paycheck|interviews|interview|resumes|resume|hires|hired|hire|cubicles|cubicle|team lead|standups|standup"),
    ("sports + games", "game|games|team|teams|coach|coaches|coached|playoff|playoffs|season|seasons|score|scores|scored|ref|league|leagues|player|players|bench|benches|stadium|stadiums|ticket price|match|matches|tournament|tournaments|practice|practices|tryout|tryouts|roster|rosters|franchise|franchises|halftime|innings"),
    ("weather + outdoors", "rain|rains|raining|rained|snow|snowing|snowed|cold|heat|heats|wind|winds|windy|storm|storms|humid|weather|sunny|sun|sunshine|freeze|freezes|freezing|frozen|ice|frost|hot out|outside|park|trail|trails|beach|beaches|garden|gardens"),
    ("health + appointments", "doctor|doctors|dentist|dentists|clinic|clinics|hospital|hospitals|pharmacy|pharmacies|prescription|prescriptions|insurance claim|appointment|appointments|checkup|checkups|x ray|waiting room|nurse|nurses|patient|patients|lab|labs|copay|copays|specialist|specialists|therapy|urgent care|vaccine|vaccines"),
    ("media + entertainment", "movie|movies|show|shows|showed|showing|series|episode|episodes|netflix|stream|album|albums|song|songs|book|books|booked|booking|bookings|podcast|podcasts|concert|concerts|theater|theaters|sequel|sequels|plot|plots|season finale|channel|channels|tv|tvs|game console|review|reviews"),
    ("admin + paperwork", "form|forms|paperwork|permit|permits|license|licenses|licences|registration|registrations|office said|certificate|certificates|notary|notaries|deadline|deadlines|application|applications|document|documents|stamp|stamps|records|bureau|bureaus|department|departments|county|counties|city hall|renew|renews|renewed|renewal|renewals|filing|filings|voter|voters"),
    ("travel + transport + transit", "flight|flights|airline|airlines|airport|airports|plane|planes|train|trains|bus|buses|subway|subways|commute|commutes|commuting|station|stations|platform|platforms|seats|boarding|layover|layovers|baggage|luggage|hotel|hotels|trip|trips|vacation|vacations|passport|passports|gate|gates|terminal|terminals"),
    ("pets + animals", "dog|dogs|cat|cats|puppy|puppies|kitten|kittens|vet|vets|pet|pets|leash|leashes|litter|litters|bark|barks|barking|shed|sheds|shedding|animal|animals|bird|birds|squirrel|squirrels|raccoon|raccoons|fish tank|paw|paws"),
    ("feelings + mood + self", "anxious|anxiety|sad|lonely|loneliness|angry|anger|mood|moods|feel|feels|felt|feeling|stress|stressed|stressing|overwhelmed|guilt|guilty|ashamed|shame|therapy|self|confidence|confident|jealous|jealousy|resent|resentment|resenting"),
    ("neighbours + building", "neighbor|neighbors|neighbour|neighbours|upstairs|downstairs|hallway|hallways|apartment|apartments|building|buildings|elevator|elevators|hoa|landlord|landlords|lease|leases|tenant|tenants|super|mailbox|mailboxes|lobby|lobbies|stairwell|stairwells|unit above|wall thin"),
    ("home + chores + repairs", "dishwasher|dishwashers|washer|washers|dryer|dryers|vacuum|vacuums|laundry|trash|recycle|recycled|recycling|cleans|cleaned|cleaning|cleaner|cleaners|clean|mop|mops|mopped|mopping|leak|leaks|leaked|leaking|faucet|faucets|toilet|toilets|sink|sinks|sinking|paint|paints|painted|painting|shelf|shelves|closet|closets|yard|yards|lawn|lawns|snow shovel|gutter|gutters|furnace|furnaces|water heater|fridge"),
    ("social + friends + family", "friend|friends|buddy|buddies|roommate|roommates|brother|brothers|sister|sisters|mother|mothers|father|fathers|mom|moms|dad|dads|cousin|cousins|aunt|aunts|uncle|uncles|wedding|weddings|birthday|birthdays|party|parties|group chat|dinner invite|coworker|family|families"),
    ("shopping + errands", "store|stores|shop|shops|shopper|shopping|checkout|checkouts|cashier|cashiers|receipt|receipts|return|returns|returned|returning|coupon|coupons|aisle|aisles|cart|carts|brand|brands|sale|sales|mall|malls|line at the|self checkout|rebate|rebates|warranty|warranties|exchange|exchanges"),
    ("driving + parking", "parking|parked|park|meter|meters|drives|drove|driven|driver|drivers|drive|driving|highway|highways|traffic|lane|lanes|light changed|intersection|intersections|merge|merges|merging|tailgater|tailgaters|commute traffic|car in front|speed|exit|exits|freeway|freeways|roundabout|roundabouts|tow|tows|towed|towing|windshield|windscreens|sweeper|sweepers|bus lane|bike lane"),
    ("trades + repairs + cars", "mechanic|mechanics|shop|shops|quote|quotes|quoted|quoting|estimate|estimates|estimated|estimating|repair|repairs|repaired|repairing|technician|technicians|plumber|plumbers|electrician|electricians|roofer|roofers|handyman|handymen|contractor|contractors|part|parts|installed|installing|installation|install|diagnose|diagnosed|diagnostic|diagnosis|oil change|brake|brakes|tire|tires|engine|engines|transmission|transmissions|alternator|alternators|labor|labors|labour|laboured|labouring|job took|fix|fixes|fixed|fixing|painter|painters"),
    ("service calls + phone", "called|call the|on hold|hold music|agent|agents|representative|representatives|extension number|customer service|hung up|transfer|transferred|transferring|transfers|escalate|escalated|escalating|escalation|callback|callbacks|recording says|automated menu|the menu|press zero"),
    ("delivery + food order", "delivery|deliveries|deliver|delivers|delivered|delivering|package|packages|shipped|tracking|courier|couriers|driver left|drop off|left at the door|missing box|app order|order arrived|arrived late|cold food"),
    ("gym + fitness", "gym|gyms|workout|workouts|lift|lifts|lifting|treadmill|treadmills|yoga|runs|running|weights|membership|memberships|class|classes|trainer|trainers|reps|locker|lockers|shower at the gym|cardio"),
]


def _compile(pattern):
    """Compile a '|'-separated keyword list to whole word alternation.

    Each alternative is escaped and fenced with \\b so it can only match a
    complete word. 'drive' no longer fires on 'driver' by accident, and
    'mall' no longer fires on 'small'.
    """
    alts = [re.escape(a.strip()) for a in pattern.split("|") if a.strip()]
    return re.compile(r"|".join(r"\b" + a + r"\b" for a in alts))


_COMPILED = [(name, _compile(pat)) for name, pat in FAMILIES]


def classify(opener):
    t = opener.lower()
    for name, rx in _COMPILED:
        if rx.search(t):
            return name
    return None


def report(paths, label):
    counts = collections.Counter()
    per = collections.defaultdict(collections.Counter)
    total = 0
    for p in paths:
        fname = os.path.basename(p)
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            total += 1
            fam = classify(r["turns"][0]["text"])
            if fam:
                counts[fam] += 1
                per[fam][fname] += 1
    print(f"== {label}: {total} rows, {sum(counts.values())} classified "
          f"({sum(counts.values()) / total:.0%})")
    for name, _ in FAMILIES:
        print(f"  {counts[name]:5d}  {name}")
    return counts, per, total


if __name__ == "__main__":
    files = [os.path.join(RAW, f) for f in sorted(os.listdir(RAW)) if f.endswith(".jsonl")]
    report(files, "CORPUS WIDE")
    print()
    # The per-file section follows the CURRENT file, derived the same way
    # add_rows.py derives it (first category in plan order under MIN_ROWS).
    # It used to be hardcoded to small_talk_angry.jsonl, so it silently kept
    # reporting a closed file as "the current one" for every later session.
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "add_rows", os.path.join(os.path.dirname(os.path.abspath(__file__)), "add_rows.py"))
    ar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ar)
    cur = ar.current_category(ar.load_existing()[0])
    label = cur.upper()
    print(f"(current file: small_talk_{cur}.jsonl -- tone: {ar.TONES.get(cur, '?')})")
    report([os.path.join(RAW, f"small_talk_{cur}.jsonl")], label)