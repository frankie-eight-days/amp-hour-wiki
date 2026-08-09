# Amp Hour Wiki — Design Document

*2026-08-07. Status: plan agreed, census spot-check in progress.*

## Goal

Distill the tribal knowledge in 719 episodes (~10M words) of The Amp Hour into a
topic-first, citation-backed wiki. Not an episode catalog, not a summarizer, not
RAG — a compiled, browsable knowledge artifact.

The existing prototype at https://amphour-wiki.vercel.app (built 2026-08-06,
source not on this machine) is treated as a visual/structural reference only.
This build starts from first principles.

## Source corpus

- `transcripts/` — 719 official speaker-labeled transcripts scraped from
  theamphour.com (Hugo static site, transcripts embedded per episode page).
- 27 episodes genuinely lack transcripts (see `transcripts/_missing.txt`),
  including #730 (not yet published). Scraper is idempotent; re-run to pick up
  new episodes.

## Core principles

1. **Mine claims, not topics.** The value is nuggets — heuristics, opinions,
   war stories — extracted with speaker + episode + verbatim quote. Articles
   are syntheses of nugget clusters.
2. **Skip the encyclopedia intro.** An "Oscilloscopes" article never defines an
   oscilloscope; it goes straight to the tribal knowledge.
3. **Every claim carries a verifiable citation** (episode + speaker + quote).
   Unsupported claims fail lint; they don't get softened. (Karpathy caveat:
   compiled wikis sound confident regardless of accuracy.)
4. **Notability floor:** a topic earns an article at ≥3 episodes and ≥3
   distinct *guests* (hosts count once total). Real threshold is nugget
   density — enough substantive nuggets to be worth reading; thin topics fold
   into their parent as sections.
5. **Taxonomy emerges from the corpus** (co-occurrence graph communities), not
   imposed (Braggoscope's Dewey mistake).
6. **Layered immutability** (mcptube pattern): per-episode extractions are
   immutable; topic articles are regenerable syntheses. Pipeline can be re-run
   with better prompts without losing provenance.
7. **Provenance shown openly** — method + AI-generated disclosure on every
   page. Audience is skeptical expert engineers.

## Article types (deliberately minimal)

- **Topic articles** — ~90% of the wiki (Oscilloscopes, PCB layout, China
  manufacturing, Consulting rates, KiCad…). War stories, tool opinions, and
  lore live as sections inside topics.
- **Saga articles** — rare multi-episode stories promoted out of a topic when
  they outgrow it (Rigol hacking, Arduino schism).
- No guest articles. Guests are a citation attribute (+ maybe an auto-generated
  claims-by-person index).

## Article anatomy

1. Title + **infobox** (top right): mentions-over-time sparkline (2010→2026),
   episode count, guest count, first/last episode, most-cited speakers,
   related topics. Data, not decoration — no AI hero images.
2. **Lead** — Wikipedia-style: 2–4 sentences neutrally summarizing the
   subject's key substance, cited. (Frank 2026-08-08: the earlier
   "hook, not a definition" rule is revoked.) ZERO meta commentary anywhere:
   the article never references itself, the archive, the show's coverage, or
   the reader ("clearest case in the archive", "one takeaway" = banned).
3. TOC.
4. **Knowledge sections** (only those with content): Practice / Rules of
   thumb / Failure modes / Tool history / Selection guidance.
   KNOWLEDGE-ONLY RULE (Frank, 2026-08-08, supersedes "Opinions & debates"):
   every claim's payload must transfer to the reader's own work — practices +
   rationale, numbers, failure modes, procedures, decision-relevant history,
   and practitioner judgments ANCHORED in stated experience (named with
   anchoring context: "On the Steam Controller project, Keyzer's team
   version-locked Altium 12..."). KILL reception narratives, adoption arcs,
   host-vs-host framing, sentiment ("came around by 2019"). Felt ≠ learned.
   Shorter and denser beats longer. No "Reception and debate" section, ever.
5. **References** — bracketed episode citations Wikipedia-style: claims stated
   as knowledge, cited [NNN] (stacking [383][422]); reference list maps episode
   → title + URL, with text-fragment deep links (`#:~:text=`) to the on-site
   transcript. VOICE (Frank, 2026-08-08, after pilot review): encyclopedic
   register — never "X explains that..."; named attribution only where the who
   IS the content (host positions, debates), in Wikipedia's "Jones has
   argued...[502]" form. Direct quotes rare; the evidence packet keeps them.
   VISUAL: Wikipedia's information design in Amp Hour brand colors — cream
   #f6eedb / #efe7d5 grounds, warm brown-black #3a352c / #16140d ink, ember
   #ef5d3c accent, amber #ffd27a highlights (pulled from theamphour.com CSS).
6. **Further reading** — auto-harvested external links from cited episodes'
   show notes.

## Pipeline

1. **Census pass** (all 719 eps, cheap model): tag every concept mention
   `{concept, type, speaker, paragraph, substantive?, snippet}`.
   Spot-check on 5 episodes first (in progress → `research/census_spotcheck/`).
2. **Canonicalize** concepts: embedding clustering + LLM adjudication of
   near-matches only (CocoIndex approach). Expect heavy surface variation
   ("scope"/"oscilloscope"/"DSO").
3. **Graph + communities**: co-occurrence scored within paragraph windows (not
   whole episodes); Louvain/Leiden communities propose categories.
4. **Score & rank candidates**: episodes × guests × sampled substantive-density.
   Output: ranked candidate article list with suggested parent/child structure.
5. **Human curation of the article list** — the editorial moment. Merge/split/
   rename/kill before any synthesis is generated.
6. **Deep claim extraction** per approved article (gather all cited passages,
   extract full nuggets with verbatim quotes).
7. **Synthesis** → articles per the anatomy above; wiki-style crosslinks on
   canonical concepts.
8. **Lint pass**: citation verification (quote actually appears in transcript;
   every cited episode backed by a verified packet claim), contradiction
   surfacing, orphan pages, missing crosslinks, meta-commentary tripwire.
8b. **Further-reading pass** (final enrichment, pipeline-owned): fetch show
   notes for every episode cited anywhere in the wiki (one fetch per episode,
   cached), extract external links, strip sponsor/UTM/subscribe junk,
   relevance-filter per article, append identical "## Further reading"
   sections ("- [Title](url) — via #NNN"). Runs after synthesis; re-runnable
   without touching prose.

## Stack

- **Quartz** (Obsidian-flavored markdown → static site): wikilinks, backlinks,
  graph view, full-text search for free. Validated by huberman.wiki.
- **Required site pages** (Frank 2026-08-08): full-text search enabled (Quartz
  built-in flexsearch); index/home page = 26 communities as sections listing
  their articles + corpus stats + links to graph Explore page and "how this
  was built"; per-community category index pages; all-articles listing.
- Deploy to Vercel over the existing `amphour-wiki` project
  (amphour-wiki.vercel.app) when ready.
- Interactive concept graph as an "Explore" page.

## Meta page: "How this wiki was built"

A first-class page on the wiki documenting the full pipeline: corpus (official
transcripts, what's missing), the model bake-off and the chunking discovery,
the extraction schema, verification rules (verbatim-quote string-matching,
yield checks, lint), costs, and known limitations (ASR errors, speaker-label
repairs, episodes without transcripts). Provenance transparency is the trust
strategy for a skeptical engineering audience — this page is its centerpiece.
Raw material: research/bakeoff/ reports + the bake-off writeup artifact.

## Prior art

See `research/prior_art_report.md`. Headlines: nobody has done
synthesized/topic-first/cited over a technical podcast; Dexa proved retrieval
alone is commercially thin; EEVblog's own wiki died twice of maintainer
fatigue — regenerability is the antidote; get the hosts on side early (Dexa
playbook: indexed podcasters became advocates).
