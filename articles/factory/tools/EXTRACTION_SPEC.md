# Extraction spec — bundle to packet (knowledge-only-v4-cluster)

You turn one evidence bundle into one extraction packet. The packet is the sole
source a writer model is given, so anything not in the packet cannot appear in
the article, and anything wrong in the packet becomes a wrong article.

## Input

`articles/factory/bundles/<concept>.json` — 250 passages, each with `episode`,
`episode_title`, `episode_url`, `speaker_repaired`, `attribution_reliable`,
`fused_turns`, `depth` (`explains`/`opinion`), `concept_source`, and `text`
(the ±1 paragraph window). `text` is what you read; it is the only text that
counts as evidence.

Read **every** passage. Do not sample. Read them in chunks if you must, but no
passage may go unread.

## THE KNOWLEDGE-ONLY RULE

KEEP only transferable engineering knowledge — something a working engineer
could act on, check, or be warned by:

- practices, and the **rationale** for them (a practice with no stated reason is
  half a claim; find the reason in the passage or state the practice tightly)
- numbers, thresholds, tolerances, prices, dates, part numbers, process nodes
- failure modes and their mechanisms
- procedures and sequences of steps
- tool, vendor, standard and product history where it is **decision-relevant**
  (why a tool is the way it is, what changed, what that costs a user today)
- practitioner judgments that are anchored in stated experience — keep the
  anchoring context ("on a seven-person consultancy with a booked backlog...",
  "after shipping X in volume...")

KILL, without exception:

- reception, adoption, popularity, sentiment: how something was received, who
  came around to it, who dismissed it, what people felt, whether opinion was
  divided, how popular it got, market enthusiasm
- meta: anything about a podcast, show, episode-as-episode, hosts, listeners,
  guests-as-guests, interviews, "we talked about"
- banter, anecdote with no transferable content, speculation with no grounding,
  news-of-the-week with no lasting engineering fact
- pure preference with no reason ("I like X better") — unless a reason is given,
  in which case the reason is the claim
- anything you cannot support from the passage text in front of you

Market-structure **facts** (segment shares, which segment a tool holds, price
points, who owns whom) are knowledge and are kept. Sentiment about them is not.

## Claim schema

Write `articles/factory/packets/<concept>.json`:

```json
{"concept": "<slug>", "spec": "knowledge-only-v4-cluster",
 "scope": {...}, "capped": true,
 "claims": [{
   "claim_text": "...",
   "quote_verbatim": "...",
   "speaker": "Dave Jones",
   "episode": 659,
   "episode_title": "Altium...Acquired!",
   "episode_url": "https://theamphour.com/659-altium-acquired/",
   "depth_regraded": "explains",
   "kind": "history"
 }],
 "attribution_notes": ["..."]}
```

- `claim_text` — the knowledge, written as encyclopedic third-person prose, as a
  standalone fact. Not "Dave says that...". Not a summary of a conversation. It
  should read like a sentence you could drop into Wikipedia. One to three
  sentences. Merge several passages that say the same thing into one strong
  claim rather than emitting near-duplicates.
- `quote_verbatim` — a short span copied **character-for-character** out of that
  passage's `text`. This is checked mechanically against the bundle; a quote
  that is not a literal substring of the passage fails the packet. Pick a span
  that carries the load of the claim. Never stitch two spans together, never
  fix grammar, never add ellipses.
- `speaker` — `speaker_repaired`. Where `attribution_reliable` is false,
  attribute by content if the content identifies the person unambiguously (and
  record why in `attribution_notes`), otherwise use `null`.
- `episode`, `episode_title`, `episode_url` — copied exactly from the passage.
  Passages whose `episode` is null cannot be cited; drop them.
- `depth_regraded` — your own grading: `explains` for transferable mechanism or
  fact, `opinion` for an anchored practitioner judgment. Regrade freely; the
  bundle's `depth` is a weak prior.
- `kind` — short label, free text but be consistent within the packet. Useful
  ones: `history`, `mechanism`, `practice`, `failure-mode`, `numbers`,
  `market-structure`, `practitioner-judgment`, `procedure`, `tradeoff`.
- `attribution_notes` — one line per episode where you overrode or declined a
  speaker label, saying what you did and why.
- `scope` / `capped` — copy `cluster`, `stats`, `cap`, `capped`,
  `total_available` from the bundle into `scope` (verbatim is fine).

## Calibration

The reference packet is `articles/factory/packets/_reference-altium-v4.json`
(88 claims from 250 passages) and the article it produced is
`articles/pilot/kimi-v4/altium.md`. Read a dozen of those claims before you
start; match that density and that voice.

Expect roughly 60–110 kept claims from 250 passages. Coverage matters as much as
selectivity: the article can only have a section where the packet has claims, so
work across the whole cluster rather than mining a few rich episodes. If a
subtopic appears in ten passages, it deserves claims proportionate to that.

## Self-check before you write the file

Run `python3 articles/factory/tools/verify_packet.py <concept>` and fix every
failure. It checks quote verbatimness, episode metadata agreement, required
fields, and reception language. Report the final verifier output.
