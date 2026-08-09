# Prior Art: Wikis and Knowledge Bases Built from Podcast Transcripts

*Research report prepared for the Amp Hour wiki project — 2026-08-07*

## Short answer

Nobody has built the thing you're describing for a technical podcast, but every ingredient has been built separately, and one project — `huberman.wiki` — is a near-exact structural match for a different podcast. The gap you'd fill is real: **synthesized, cross-episode, topic-first articles over a deep technical corpus, with episode citations**. What exists instead is (a) fan wikis that catalog *episodes* rather than *knowledge*, (b) search/Q&A products that retrieve rather than compile, and (c) a very recent wave of "LLM wiki" tooling that does compile but has almost no track record at 10M-word scale.

---

## 1. Direct prior art: wikis built from podcast content

### Huberman Lab Wiki — the closest match

- **URL**: https://huberman.wiki/
- **What it is**: An unofficial, topic-first wiki over the Huberman Lab podcast. Six "foundation hubs" (Brain & Nervous System, Sleep, Focus/Learning, Mood, Hormones/Metabolism, Physical Performance), plus core protocol pages, condition-specific pages, and per-episode pages with full transcripts, video embeds, and clickable timestamps.
- **Methodology** (stated on its own about page): semantic chunking of transcripts → AI-assisted transcript polishing → automatic entity and concept extraction. Published with **Quartz v4.5** (the Obsidian-vault-to-static-site generator), which gives it backlinks and a graph view for free.
- **Status**: Live, anonymous author, no stated update cadence. Notable: the homepage claims 137 episodes while the about page says 55 — and Huberman Lab has well over 250. **Coverage is partial and the numbers don't reconcile**, which is itself the most useful signal here.
- **Takeaway**: This is your project's structural template, and you should steal the architecture wholesale — Quartz + Obsidian-style markdown gives you wikilinks, graph view, and full-text search with zero infrastructure. It also demonstrates the failure mode: an anonymous, un-versioned AI-built wiki with unclear coverage is hard to trust and hard to contribute to.

### Braggoscope (BBC *In Our Time*) — the best-documented precedent

- **URL**: https://www.braggoscope.com/ · methodology write-up: https://interconnected.org/home/2023/02/07/braggoscope
- **What it is**: Matt Webb's alternative interface to ~1,000 episodes of *In Our Time*, browsable by Dewey Decimal classification, by guest, and by semantic similarity, with extracted reading lists.
- **Methodology**: Scrape BBC pages → minified HTML straight into GPT-3.5 with a TypeScript type definition in the prompt to force structured JSON out (temperature 0) → GPT assigns Dewey codes and finds similar episodes → embeddings (`bge-base-en-v1.5`) for semantic search via a Cloudflare Worker → Whisper transcribes Melvyn Bragg's intros → Google Books API validates the ~4,600 extracted book references (88% match rate) → static site on GitHub Pages.
- **Cost**: roughly **$30 total** for the extraction pass over 1,000 episodes, replacing "several days of manual coding."
- **Status**: Live, self-labeled v0.2, actively discussed (Simon Willison covered it; HN thread at https://news.ycombinator.com/item?id=35073603).
- **Criticism from the HN thread**: visible classification errors (plumbing filed under agriculture, Plato's Atlantis under computer science) and the observation that any imposed taxonomy encodes bias — Dewey gave 90 slots to European history and 3 to African history.
- **Takeaway**: The single most transferable precedent. Two lessons: schema-constrained extraction at temperature 0 is cheap and reliable enough to be boring, and **a rigid pre-existing taxonomy will fight your corpus**. For electronics you'd want a taxonomy derived from the corpus, not imported.

### Knowledge Fight Wiki

- **URL**: https://knowledgefight.wiki/
- **What it is**: A MediaWiki fan wiki for the Knowledge Fight podcast, organized by episode number/title, with topic and person lookup done via MediaWiki's "What Links Here" backlinks.
- **Methodology**: Hybrid. Episode metadata scraped from Libsyn; transcription via otter.ai with spaCy processing; **articles written by community volunteers**. Last edited December 2025; the podcast itself ended May 2026.
- **Takeaway**: Shows the manual-curation ceiling. Even with automated transcription feeding it, the synthesis was human, and the structure stayed episode-centric rather than concept-centric. Backlinks did the topic-navigation work that a hand-built topic hierarchy would have cost enormous effort.

### Fandom-hosted podcast wikis (MBMBaM, No Such Thing As A Fish)

- **URLs**: https://mbmbam.fandom.com/ · https://nstaaf.fandom.com/
- **What they are**: Episode catalogs, running-bit indexes, character/person pages. Entirely human, entirely episode-indexed.
- **Takeaway**: These are the "not what you want" baseline — they answer "what happened in episode 412" rather than "what does this community know about ground loops." Confirms the gap.

### Encyclopedia Exandria (Critical Role) — the adjacent gold standard

- **URL**: https://criticalrole.miraheze.org/
- **What it is**: 5,444 volunteer-written articles distilled from hundreds of hours of livestreamed conversational audio, hosted on Miraheze (ad-free, non-profit). Fans also maintain separate full transcripts and a transcript search tool.
- **Takeaway**: Proof that a deep, genuinely synthesized wiki over conversational audio is achievable — but it took a large obsessive volunteer community years, and it fled Fandom for a community-controlled host. If your wiki is good, plan for the possibility that people want to edit it.

### EEVblog Electronics Resource Wiki — the cautionary tale in your own community

- **URL**: https://www.eevblog.com/wiki/
- **What it is**: Dave Jones's (Amp Hour co-host) community wiki of electronics resources — books, tools, distributors, manufacturers, tutorials. About 25 resource categories.
- **History**: An earlier version was **killed by spam plus, in Dave's own words, "lack of enthusiasm on my part to fix it."** Relaunched November 2011 with math CAPTCHAs, with the explicit goal of archiving useful forum discussions systematically. Main page last edited **September 2023**.
- **Takeaway**: The most directly relevant lesson you'll find. The exact community you're serving already tried a wiki, twice, and it decayed into a link directory both times. The failure wasn't the idea — it was that link-list wikis have no compounding value and manual upkeep collapses. A generated-and-regenerable wiki sidesteps the maintenance-enthusiasm problem entirely, which is arguably your strongest justification for the project.

---

## 2. Products and tooling in this space

### Dexa

- **URL**: https://dexa.ai/ · TechCrunch: https://techcrunch.com/2024/02/05/dexa-aims-to-get-more-out-of-podcasts-with-ai-powered-search/
- **What it is**: AI search and Q&A over 120+ podcasts, answers cited to the exact moment/chapter in an episode. Also shipped expert-specific bots (e.g., an official Huberman Lab assistant at ai.hubermanlab.com).
- **Methodology**: AssemblyAI for transcription with **speaker diarization** and **automatic chapter detection** as the topic segmentation layer; answers link to the source timestamp. Over **3 million hours** of audio processed.
- **Status**: **Alive but small** — 6 employees as of January 2026, $6M seed (Feb 2024; Maple VC, Abstract Ventures, The General Partnership), no follow-on round found. Growth came organically from podcasters promoting it after Dexa indexed them, rather than from formal licensing deals.
- **Takeaway**: The strongest evidence that *retrieval* over podcasts is solved and *commercially underwhelming*. Dexa answers questions; it never compiles a persistent artifact you can browse, link to, or hand to a beginner. That distinction is the whole case for a wiki. Also note their growth path — podcasters became advocates once indexed, which is a plausible model for getting Chris Gammell and Dave Jones on side rather than annoyed.

### Snipd

- **URL**: https://www.snipd.com/
- **What it is**: AI podcast player where you tap your headphones to capture a "snip" (audio + transcript + AI summary), building a personal knowledge feed that exports to Notion, Obsidian, Readwise, Logseq, Bear, or markdown. Premium adds chat-with-podcast.
- **Status**: Active, well-reviewed, on both app stores.
- **Takeaway**: Solves *personal* capture at listen-time. Nobody's snips become a shared public artifact. Its export formats are worth matching — markdown out to Obsidian is the interchange format this whole ecosystem has converged on.

### Podcast Notes

- **URL**: https://podcastnotes.org/
- **What it is**: A decade-old, human-written archive of detailed episode notes across hundreds of shows, with topical collections (33 of them) and curated cross-episode compilations like a 200+ book list assembled from mentions across many episodes. Freemium: free newsletter, paid premium collections and e-books.
- **Takeaway**: The book-collection page is the single best demonstration of the value you're chasing — a **cross-episode synthesis artifact** that no individual episode contains. That's exactly the kind of page ("every scope/logic analyzer ever recommended," "every consulting-rate discussion") that would justify your wiki on day one.

### Other tooling

- **Podscribe / PodScript / hubermantranscripts.com** — transcript generation and hosting, no synthesis layer.
- **Shortform** — human-written podcast summaries with commentary (covers Acquired, among others); subscription, episode-scoped.
- **Metacast** — AI-enhanced podcast app in the same category as Snipd.

---

## 3. The 2026 "LLM Wiki" wave — the pattern you're actually building

This is new and directly relevant. In late 2025 Karpathy published a gist describing the "LLM Wiki" pattern (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), and a cluster of implementations followed within months.

**The pattern**: three layers — immutable raw sources, an LLM-maintained interlinked markdown wiki, and a schema config. Three operations — **ingest** (LLM reads a source, extracts takeaways, updates entity pages, records contradictions, typically touching 10–15 pages per source), **query** (search the wiki, synthesize with citations, file discoveries back), and **lint** (periodic health check for contradictions, stale claims, orphan pages, missing cross-references). Two navigation files: `index.md` (categorical catalog) and `log.md` (append-only chronological record).

Karpathy's own caveat is the one that should govern your design: *compiled wikis answer more confidently than raw retrieval, which decouples confidence from accuracy — and fabrications can get filed as "sources" if unreviewed.*

**Implementations found:**

| Project | URL | Note |
|---|---|---|
| mcptube | https://github.com/0xchamin/mcptube | Karpathy pattern applied to YouTube. Most sophisticated design found. |
| llm-wiki (lucasastorian) | https://news.ycombinator.com/item?id=47656181 | Open-source Karpathy implementation, MCP + virtual filesystem for Claude. Early, low engagement. |
| llm-wiki-agent | https://github.com/SamurAIGPT/llm-wiki-agent | Self-maintaining wiki via Claude Code / Codex / Gemini CLI. |
| llm-wiki-compiler | https://github.com/atomicstrata/llm-wiki-compiler | "Raw sources in, interlinked wiki out." |
| nashsu/llm_wiki | https://github.com/nashsu/llm_wiki | Desktop app, two-phase pipeline: extract concepts, then generate typed pages. |

**mcptube deserves the closest read** — its page-type model is the best-designed thing found for this problem:

- **Four page types**: Video (write-once, immutable), Entity (append-only — new references added, never overwritten), Topic and Concept (synthesis rewritten, but per-source contributions immutable).
- **CRDT-like append model** so re-ingestion merges rather than clobbers; version history on all non-immutable pages.
- Explicit goal: ten talks on one topic should produce **one coherent article**, not ten unconnected transcript chunks.
- It also does scene-change frame extraction with a vision model to recover on-screen code and diagrams the transcript misses — irrelevant for audio-only Amp Hour, but the underlying insight (transcripts lose the non-verbal signal) applies to your corpus in a different way: part numbers, schematics, and URLs get mangled or lost in ASR.
- **Caveats**: local-only MCP server, no published cost figures, no reported scale testing.

Also relevant: **CocoIndex's podcast-to-knowledge-graph pipeline** (https://cocoindex.io/blogs/podcast-to-knowledge-graph/) documents a bootstrapping problem you will hit. Diarization gives you "Speaker A" and "Speaker B," but good statement extraction requires knowing *who* is speaking. Their fix is two-stage: resolve speaker labels to real names using episode metadata first, then re-extract with real names attached. They enforce that entities be "self-contained" — never pronouns, never speaker labels, never contextual references — and deduplicate with embedding similarity (FAISS, cosine < 0.3) followed by an LLM confirmation step, so the expensive model only adjudicates near-matches. Their schema: Session, Statement, Person, Tech, Org nodes with attribution, participation, and mention edges.

---

## 4. Academic and research work

- **Spotify Podcast Dataset / TREC Podcasts Track (2020, 2021)** — https://trecpodcasts.github.io/ · 2020 overview: https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf · 2021 overview: https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf. 105,360 episodes from 18,376 shows with audio, metadata, and ASR transcripts. Two tasks: **segment retrieval** (find the specific part of the episode, not just the episode) and **summarization**. The track framing itself is your evidence base: podcasts, unlike broadcast news or meetings, present a *diverse, informal linguistic substrate — multiple speakers, conversational style, advertisements, variable structure*. The consensus finding across participants was that **concatenating extracted utterances does not produce a usable summary** because of disfluency and redundancy in unplanned spontaneous speech; the winning systems (CUED_speech) used staged pipelines — select salient spans first, then run abstractive generation. Notably, the best system scored 1.777 on the EGFB human scale versus **1.291 for the podcast creators' own episode descriptions** — machine summaries beat human show notes.
- **KGGen** — https://arxiv.org/pdf/2502.09956 — LLM knowledge-graph extraction from plain text, with clustering to normalize entity names.
- **wav2graph** — https://arxiv.org/html/2408.04174v1 — supervised KG learning directly from speech.
- **Evidence-Grounded Multimodal KG Construction for Multi-Lecture Reasoning** — https://arxiv.org/abs/2608.03161 — lecture-series analog: transcribe, pick semantic anchors, OCR, and extract *only* concepts and typed relations that are supported by transcript/OCR/visual evidence. The evidence-grounding constraint is the anti-hallucination mechanism worth copying.
- **SocraticKG** — https://arxiv.org/pdf/2601.10003 — QA-driven fact extraction as a KG construction strategy.
- **"Why They Disagree: Decoding Differences in Opinions about AI Risk on the Lex Fridman Podcast"** — https://arxiv.org/pdf/2512.06350 — an actual scholarly analysis of one podcast corpus, focused on mapping *disagreement* between speakers. Directly applicable: The Amp Hour is two opinionated engineers who disagree, and modeling disagreement rather than flattening it is a genuine design question for you.

---

## 5. Adjacent precedents worth knowing

- **Dan Shipper's Huberman chatbot** — https://every.to/chain-of-thought/i-trained-a-gpt-3-chatbot-on-every-episode-of-my-favorite-podcast — early embed-and-retrieve bot over podcast transcripts. His postmortem: answers were subtly wrong and vague, and his stated fix was **to clean the transcripts first — define terms, group related concepts — rather than embed raw ASR output**, plus add citations so readers can verify. That's an argument for a compiled wiki over RAG, written before the wiki pattern existed.
- **Lennyhub RAG** — https://github.com/traversaal-ai/lennyhub-rag — production-grade knowledge-graph RAG over 297 Lenny's Podcast transcripts, with graph and metadata in the storage layer. Closest thing to a serious KG over a single podcast.
- **The Changelog transcripts** — https://github.com/thechangelog/transcripts — an engineering podcast that publishes its full transcripts as markdown in a public repo. Useful as a licensing/norms precedent when you approach the Amp Hour hosts.
- **Golden** — https://golden.com/ — the "AI-built Wikipedia for tech," a16z/Founders Fund-backed, $14.5M Series A in 2020. It built one of the largest self-constructing knowledge graphs, then **abandoned the consumer wiki and was acquired by ComplyAdvantage in 2024**, where the graph now serves financial-crime intelligence. No public postmortem, but the trajectory is the lesson: the auto-generated general-purpose wiki did not find an audience; the narrow, high-value vertical application did.
- **Fandom's genAI push (2025–26)** — Fandom rolled out AI-generated translations and creator tools over loud objections from wiki editors, who argued AI misses fandom-specific nuance and floods wikis with content "no human can sort through or evaluate." Wikipedia similarly halted AI plans after editor revolt. These are the community-reception risks for an AI-built wiki aimed at a proud, expert, skeptical audience — and EEVblog readers are exactly that audience.

---

## Synthesis

### What's been tried

1. **Human fan wikis over podcasts** — common, but almost always episode-indexed catalogs, not knowledge syntheses. The exceptions (Encyclopedia Exandria) required years of volunteer obsession.
2. **AI search and Q&A over podcast corpora** — solved technically (Dexa, Snipd, dozens of RAG demos), commercially thin, and produces nothing persistent or browsable.
3. **Structured extraction over a single podcast archive** — Braggoscope proved this works beautifully and costs ~$30, but it extracted *metadata* (guests, books, classifications), not *claims*.
4. **Knowledge graphs from transcripts** — well-studied academically and in a handful of repos; the recurring hard problems are speaker attribution and entity deduplication.
5. **The compiled LLM wiki** — the exact pattern you want, formalized less than a year ago, with implementations that are days-to-months old and no published results at your scale.

### The gap you'd fill

Nobody has built a **synthesized, topic-first, citation-backed knowledge wiki over a deep technical corpus.** Every adjacent project is either metadata-only, episode-indexed, retrieval-only, or aimed at self-help/entertainment content where claims are soft and verification is optional. Electronics is different: "which current-sense amp for a 100A shunt," "why your ground plane split made EMI worse," "what a reasonable contract rate was in 2013 versus now" are *checkable*, they *accumulate*, and they're *exactly* the tribal knowledge that dies in an audio archive nobody can search. 719 episodes over ~15 years also gives you something none of the precedents have: **longitudinal depth**, where the same topic recurs across a decade and the interesting artifact is how the answer changed.

### Five concrete lessons

**1. Compile claims, not summaries — and make evidence-grounding a hard constraint.** TREC's central finding was that stitching together extracted utterances yields garbage; the winners used staged extraction-then-synthesis. The multi-lecture KG paper's rule is the one to enforce in your prompts: emit only concepts and relations *supported by cited transcript evidence*. Karpathy's own caveat is that compiled wikis sound more confident than retrieval, so fabrications get laundered into the record. Every claim on every page needs an episode + timestamp anchor, and unsupported claims should fail the lint pass rather than get softened.

**2. Steal mcptube's page-type model and the immutability discipline.** Distinguish immutable per-episode extractions (write once, never rewritten) from append-only entity pages (a part number or person accumulates references) from rewritable synthesis pages (topics and concepts). This is what lets you re-run the pipeline on an improved prompt without losing provenance, and it's what makes ten mentions of buck converters across a decade merge into one article instead of ten fragments.

**3. Solve speaker attribution before extraction, not after.** CocoIndex's two-stage approach exists because "Speaker A said X" is useless and misattribution is worse than omission. You have an advantage: two consistent hosts across most episodes, with guests identifiable from show notes. Resolve names from metadata first, then extract with real names in context, and require self-contained entity strings with no pronouns or contextual references. Then deduplicate with embeddings plus LLM confirmation on near-matches only — an electronics corpus will generate enormous surface variation on the same part ("LM317", "the 317", "an LM 3 17" out of ASR).

**4. Let the taxonomy emerge from the corpus; don't impose one.** Braggoscope's most-cited flaw was Dewey filing plumbing under agriculture, and the taxonomy's own historical bias showed through in the coverage distribution. Huberman.wiki's six hubs work because they were derived from what the podcast actually covers. Derive your hubs from clustered extractions, and lean on wikilinks and backlinks — which Quartz gives you free — to carry navigation load that a rigid hierarchy would handle badly.

**5. Ship it as a regenerable artifact, and get the hosts on your side early.** The EEVblog wiki died twice from spam and maintainer fatigue in this exact community — a generated wiki that can be rebuilt from source on demand is immune to that failure, and that's the honest pitch. But Fandom's and Wikipedia's editor revolts show that skeptical expert communities react badly to AI-written reference material presented as authoritative. Be explicit about provenance and method on every page, mark AI-synthesized text as such, and follow Dexa's playbook: podcasters became their best advocates once their content was indexed well. Chris Gammell and Dave Jones going from "who is this" to "have you seen this" is worth more than any distribution strategy, and it's also your cleanest answer to the licensing question, which nobody in this space has resolved cleanly — Dexa operates on informal goodwill rather than formal licenses, and that's the norm, not a settled legal position.

### Two practical notes on your corpus specifically

- The Amp Hour has **no public transcripts** — only the official episode listing at https://theamphour.com/episodes/ (grouped by category, split into guest and non-guest shows) and show notes in the feed. You're generating the primary source yourself, which means diarization quality and technical-term ASR accuracy are your foundation, and errors there propagate into every article. Budget for a term-correction pass (part numbers, company names, jargon) before extraction — that's Shipper's lesson from 2022 and it still holds.
- Braggoscope's ~$30 for 1,000 episodes of *metadata* extraction is not your budget. Claim-level extraction plus synthesis plus lint passes over 10M words is a different order of magnitude — closer to mcptube's "invest tokens upfront so retrieval is cheap" framing, and mcptube conspicuously declines to publish its numbers. Run the full pipeline on 20 episodes and extrapolate before committing to all 719.

---

## Sources

- Huberman Lab Wiki — https://huberman.wiki/
- Braggoscope — https://www.braggoscope.com/about
- Matt Webb on Braggoscope — https://interconnected.org/home/2023/02/07/braggoscope
- Simon Willison on Braggoscope — https://simonwillison.net/2023/Feb/13/braggoscope/
- HN: Braggoscope — https://news.ycombinator.com/item?id=35073603
- Knowledge Fight Wiki — https://knowledgefight.wiki/index.php/Main_Page
- Encyclopedia Exandria — https://criticalrole.miraheze.org/wiki/Main_Page
- MBMBaM Wiki — https://mbmbam.fandom.com/wiki/My_Brother,_My_Brother_and_Me_Wiki
- No Such Thing As A Fish Wiki — https://nstaaf.fandom.com/wiki/No_Such_Thing_As_A_Fish_Wiki
- EEVblog Electronics Resource Wiki — https://www.eevblog.com/wiki/index.php?title=Main_Page
- EEVblog wiki revival thread — https://www.eevblog.com/forum/news/the-eevblog-electronics-resource-wiki-is-back!/
- Dexa — https://dexa.ai/introducing-dexa
- Dexa on TechCrunch — https://techcrunch.com/2024/02/05/dexa-aims-to-get-more-out-of-podcasts-with-ai-powered-search/
- AssemblyAI Dexa case study — https://www.assemblyai.com/customers/dexa-customer-story
- Dexa on Tracxn — https://tracxn.com/d/companies/dexa/__aRudphPx5CazFoChxLfX6MCotafUC3JqzOxhKhoY77k
- Snipd — https://www.snipd.com/
- Podcast Notes — https://podcastnotes.org/
- Karpathy's LLM Wiki gist — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- mcptube — https://github.com/0xchamin/mcptube
- HN: mcptube — https://news.ycombinator.com/item?id=47754559
- HN: LLM Wiki open-source — https://news.ycombinator.com/item?id=47656181
- llm-wiki-agent — https://github.com/SamurAIGPT/llm-wiki-agent
- llm-wiki-compiler — https://github.com/atomicstrata/llm-wiki-compiler
- nashsu/llm_wiki — https://github.com/nashsu/llm_wiki
- CocoIndex podcast knowledge graph — https://cocoindex.io/blogs/podcast-to-knowledge-graph/
- Lennyhub RAG — https://github.com/traversaal-ai/lennyhub-rag
- Spotify Podcast Dataset — https://engineering.atspotify.com/2020/04/introducing-the-spotify-podcast-dataset-and-trec-challenge-2020
- TREC Podcasts Track — https://trecpodcasts.github.io/
- TREC 2020 overview — https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.P.pdf
- TREC 2021 overview — https://trec.nist.gov/pubs/trec30/papers/Overview-Pod.pdf
- CUED_speech at TREC 2020 — https://arxiv.org/pdf/2012.02535
- KGGen — https://arxiv.org/pdf/2502.09956
- wav2graph — https://arxiv.org/html/2408.04174v1
- Evidence-Grounded Multimodal KG Construction — https://arxiv.org/abs/2608.03161
- SocraticKG — https://arxiv.org/pdf/2601.10003
- Lex Fridman AI-risk disagreement paper — https://arxiv.org/pdf/2512.06350
- Dan Shipper's podcast chatbot — https://every.to/chain-of-thought/i-trained-a-gpt-3-chatbot-on-every-episode-of-my-favorite-podcast
- The Changelog transcripts — https://github.com/thechangelog/transcripts
- Golden — https://golden.com/
- Golden Series A — https://techcrunch.com/2020/09/30/golden-series-a/
- Fandom AI backlash — https://community.fandom.com/f/p/4400000000003824457
- The Amp Hour episode listing — https://theamphour.com/episodes/
