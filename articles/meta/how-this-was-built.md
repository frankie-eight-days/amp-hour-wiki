---
title: How this wiki was built
---

The Amp Hour Wiki is an experiment in distilling **oral tradition** — sixteen
years of two engineers (and hundreds of guests) saying out loud the things
that never make it into datasheets — into a citation-backed reference. This
page explains how it works by doing the most honest thing we can: taking one
real sentence from a live article and tracing it backwards, layer by layer,
until we hit the audio.

## The sentence

From the [Analog to Digital Converter](./analog-to-digital-converter) article:

> The nominal bit count of a converter does not equal its usable resolution:
> a 24-bit part in a handheld power-measurement instrument returned roughly
> 18 effective bits at its highest sample rate and little more than 19 when
> slowed down.<sup>[218]</sup>

That `[218]` is a promise: this claim came from episode 218, and the pipeline
can prove it. Let's cash the promise in.

## Layer 0 — the audio

Episode 218, September 29, 2014: [*An Interview with Eric VanWyk — Meiotic
Mountenance Mooshimeter*](https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/).
Eric built the Mooshimeter, a two-channel Bluetooth multimeter. About an hour
in, this exchange happens (from the machine transcript, errors and all):

<div style="background: var(--lightgray); border-left: 3px solid #c94628; padding: 12px 18px; border-radius: 4px; font-size: 0.92rem;">
<p><strong>Dave Jones:</strong> And of course you're, and of course you discovered that a 24 bit ADC doesn't actually give you 24 usable bits out.</p>
<p><strong>Eric Van Wyk:</strong> Sure. Of course, uh, we've been pulling, uh, in, in our highest speed settings, maybe 18 effective, um, and, and nudging a little bit over 19, uh, when we slow down and, and pay attention a little bit more.</p>
</div>

This is what the raw material actually looks like: automatic speech
recognition, filler words, false starts, and 719 files of it — roughly 11
million words. Nobody is reading that end to end. Everything below exists to
make this one exchange *findable, checkable, and citable*.

## Layer 1 — the census

First pass over all 719 transcripts: find every mention of every engineering
concept. The census logged about **197,000 mentions** and classified each
one — is the speaker merely *naming* the concept, or *explaining* something
about it, or *taking a position*? Our exchange gets logged as an
`explains`-depth mention of `analog-to-digital-converter`.

Raw census output is noisy: the same concept surfaces as "ADC", "A to D",
"A/D converter", "analog to digital". A canonicalization pass built alias
tables folding ~4,000 surface forms into canonical concepts, and a speaker
map repaired the transcript's frequently-wrong speaker labels. Then a graph
pass connected the concepts: **4,016 nodes and 12,776 edges** of
co-occurrence and hierarchy — that's what you see on the
[graph explorer](./explore), and it's how the wiki knows that `adc` should
also absorb mentions of `enob` and `delta-sigma`.

## Layer 2 — the bundle

For each concept ranked worth an article, a deterministic script gathers
**every relevant passage** into one evidence bundle. No judgment yet — just
collection. The ADC bundle holds 242 passages drawn from 211 distinct
episodes (486 mentions). Our exchange appears as passage `paragraph_index:
455`, and the bundle records something important about it:

```json
{
  "episode": 218,
  "stem": "0218-an-interview-with-eric-vanwyk-...",
  "guest": "Eric Van Wyk",
  "paragraph_index": 455,
  "speaker_raw": "Dave Jones",
  "fused_turns": true,
  "depth": "explains",
  "text": "... you discovered that a 24 bit ADC doesn't
           actually give you 24 usable bits out. Sure. Of
           course, uh, we've been pulling ... maybe 18
           effective ... over 19 ... when we slow down ..."
}
```

Notice the trap: the bundling fused Dave's question and Eric's answer into
one passage *labeled Dave Jones* — but the numbers were spoken by Eric. This
happens constantly, which is why the pipeline treats speaker labels as
unreliable by default. Watch how the next layer handles it.

## Layer 3 — the packet (where judgment happens)

An extraction pass — an LLM agent working under a
[written spec](https://github.com/frankie-eight-days/amp-hour-wiki/blob/main/articles/factory/tools/EXTRACTION_SPEC.md) —
reads all 242 passages and produces a **packet**: structured claims, each
tagged with one of ten kinds (practice, mechanism, tradeoff, numbers,
failure-mode, procedure, constraint, history, market-structure,
practitioner-judgment) and pinned to a quote **sliced programmatically from
the passage text, never retyped**. Our exchange became:

```json
{
  "claim_text": "The bit count on a converter's part number is
    not the number of usable bits. A 24-bit converter in a
    handheld power-measurement instrument returned roughly 18
    effective bits at its highest sample rate and a little
    over 19 when slowed down.",
  "quote_verbatim": "a 24 bit ADC doesn't actually give you
    24 usable bits out",
  "speaker": "Dave Jones",
  "episode": 218,
  "kind": "practice"
}
```

Two things to see here. The claim says *"a handheld power-measurement
instrument"* — not "the Mooshimeter said by Eric VanWyk" — because the
extraction knew the attribution across the fused turns was shaky and wrote
the claim so it doesn't depend on who said which half. And the quote is
verbatim ASR text, garble included.

Then a verifier (`verify_packet.py`) **byte-compares every quote against the
transcript**. A quote that was paraphrased, "cleaned up", or hallucinated
fails the build. The ADC packet carries 96 claims; across the wiki's 197
packets there are over 13,000 verified claims, and every single quote in
every one of them passes this check.

## Layer 4 — the article

A separate model writes the article **from the packet alone**. The writer
never sees the transcripts — the packet is the contract, so it can organize
and connect but cannot introduce facts. Claim + citation became the sentence
you started with, and the `[218]` link in the live article resolves to a
references row with the episode title, date, and URL.

A final lint pass enforces the contract mechanically: every paragraph cited,
every citation resolving to a packet claim, no editorializing beyond the
evidence, no fabricated consensus ("engineers agree..."). Fail the lint,
rewrite the article.

## What this buys you — and what it doesn't

**What the pipeline guarantees:** every claim traces to a real, verbatim,
byte-checked passage in a real episode you can go listen to. Nothing is
sourced from the writer's general knowledge, the internet, or vibes.

**What it can't guarantee:** that the *interpretation* is right. The quotes
are real, but an extraction can still misread sarcasm, miss context from
five minutes earlier, or build a general rule out of one anecdote. ASR
garble occasionally swallows a number. Speaker attribution, as you saw, is
repaired but imperfect — where it's doubtful we attribute to the content,
not the person.

That residual risk is exactly what the **Report** button is for: highlight
any sentence on any article and file an issue in one click. "The quote is
real but the claim misunderstands it" is the failure mode we most want
reported, because it's the one the machinery can't catch itself.

## The numbers

| | |
|---|---|
| Episodes transcribed | 719 |
| Words of transcript | ~11 million |
| Concept mentions in the census | ~197,000 |
| Graph | 4,016 concepts, 12,776 edges |
| Verified claims extracted | 13,000+ |
| Articles live | 153 (of 412 planned) |
| Episode citations across the wiki | 6,600+ |

Everything — transcripts, census, bundles, packets, tools, this site — is in
the [public repo](https://github.com/frankie-eight-days/amp-hour-wiki).
If you'd like to build a piece of it yourself, start at
[How to contribute](./contribute).

*The Amp Hour is Chris Gammell and Dave Jones. This is a fan project built
on their Creative Commons-licensed show; go listen to
[the real thing](https://theamphour.com).*
