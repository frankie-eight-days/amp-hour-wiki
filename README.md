# The Amp Hour Wiki

**16 years of electronics oral tradition — indexed.**

A topic-first, citation-backed wiki distilling practical engineering knowledge
from 719 episodes of [The Amp Hour](https://theamphour.com) podcast. Every
claim in every article traces to a verbatim quote in a specific episode
transcript — no claim ships without a citation that survives byte-level
verification.

**Live site:** [amphour-wiki.vercel.app](https://amphour-wiki.vercel.app)

## How it works

```
transcripts/  →  census  →  canon  →  graph  →  bundles  →  packets  →  articles  →  site
 719 episodes    197k       alias     concept   evidence     verified     lint-       Quartz
                 mentions    tables    graph     per topic    claims +     checked     + Vercel
                                                              quotes       markdown
```

1. **Census** — every concept mention across all 719 transcripts (~197k mentions).
2. **Canonicalization** (`canon/`) — alias tables fold surface forms into canonical concepts; a speaker map repairs attribution.
3. **Graph** (`graph/graph.json`) — co-occurrence and hierarchy edges between concepts; communities drive the topics page.
4. **Bundles** (`articles/factory/bundles/`) — deterministic evidence packs: every relevant transcript passage for one concept.
5. **Packets** (`articles/factory/packets/`) — the judgment layer: an extraction pass reads the bundle and produces structured claims, each pinned to a verbatim quote. `verify_packet.py` rejects any quote that doesn't match the transcript exactly.
6. **Articles** (`articles/wiki/`) — written from the packet only (the writer never sees raw transcripts), then checked by `lint.py`: every paragraph cited, every citation resolvable, no editorializing.
7. **Site** (`site/`, `tools/`) — Quartz 5 static build, deployed to Vercel.

## Contributing

Yes please — see [CONTRIBUTING.md](CONTRIBUTING.md). Three lanes: fix or
improve articles, extract packets for the ~200 concepts still unwritten, or
hack on the site itself. PRs are lint-checked automatically.

Spotted an error on the site? Highlight the text and hit **Report** — it
opens a prefilled GitHub issue here.

## Licensing & attribution

The Amp Hour podcast is published by Chris Gammell and Dave Jones under a
Creative Commons license. Transcripts in `transcripts/` are machine-generated
(ASR) from those episodes and carry their errors; the wiki articles are
derivative works and are likewise offered under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), with
attribution to The Amp Hour and the speakers quoted. Code (everything under
`tools/`, `articles/factory/tools/`, `site/` build config) is MIT.

This is a fan project, not affiliated with or endorsed by The Amp Hour.
If you're Chris or Dave and want anything changed or removed, open an issue —
it'll be handled immediately.
