# Factory tooling

Deterministic prep for the 412-article run. Nothing here makes article
judgments; extraction agents do that between the bundle and the packet.

```
bundle  ->  (extraction agent)  ->  packet  ->  kimi_write.py  ->  article.md  ->  lint.py
                                                      |                              |
                                                      +--------> timing.py <---------+
```

## build_bundles.py

Rebuilds every evidence bundle from `census/union`, `canon/alias_table_v2.json`,
`canon/speaker_map.json`, `graph/graph.json` and `articles/candidates.json`.
Full run takes about three seconds; a single concept can be rebuilt with
`python3 build_bundles.py <concept>`. Writes `articles/factory/bundles/<concept>.json`
plus the intermediate `articles/factory/_manifest_rows.json`.

## make_manifest.py

Rolls those rows into `articles/factory/_manifest.json` and
`articles/factory/_factory_report.md`. Run it after any bundle rebuild.

## Bundle schema

| Field | Meaning |
| --- | --- |
| `concept` | slug, matches the candidates.json concept |
| `name` | display title for the article frontmatter |
| `cluster.core` | the concept plus every alias canonicalising to it |
| `cluster.children` | concepts whose suggested parent is this concept |
| `cluster.neighbors` | `{concept, weight}` co-occurrence neighbours, weight ≥ 4, not article-status |
| `stats` | `episodes`, `mentions`, `explains`, `opinions` over the whole cluster, plus gating and speaker breakdowns |
| `capped` / `total_available` | whether the 250 cap bit, and how many passages existed before it |
| `passages[]` | the evidence |

Each passage carries `episode`, `episode_title`, `episode_url`, `stem`, `guest`,
`paragraph_index`, `depth` (`explains` or `opinion`), `speaker_raw`,
`speaker_repaired`, `attribution_reliable`, `fused_turns`, `concept_source`
(`core`, `child:<name>` or `neighbor:<name>`), `concept_sources` for paragraphs
that hit several cluster members, `paragraph_text`, `context_before`,
`context_after`, and `text` — the ±1 paragraph window as one string.

`attribution_reliable: false` means the episode is on the speaker map's
unreliable list: the words are right but the name on them may not be, so
attribute by content or not at all. `fused_turns: true` means turn boundaries in
that transcript are unreliable.

## kimi_write.py

```
python3 kimi_write.py --packet <packet.json> --out <article.md> [--title "Name"] \
                      [--further <further_reading.json>] [--spec-file <spec.txt>] \
                      [--model k3] [--max-tokens 32000] [--dry-run]
```

The packet must be `{"concept": ..., "claims": [{claim_text, quote_verbatim,
speaker, episode, episode_title, episode_url, depth_regraded, kind}, ...]}`.
Episode titles, URLs and dates are resolved from `census/union` and the
transcript show-opens and handed to the model, so it cannot invent them. The
locked `knowledge-only-v4-cluster` spec is built in; `--spec-file` overrides it
and gets `{title} {concept} {date} {model} {spec_id}` substituted. The prompt is
always saved next to the output as `<out>.prompt.txt`, token usage as
`<out>.usage.json`. Failed API calls retry twice. Key path defaults to the
scratchpad `kimi_key`, overridable with `KIMI_KEY_PATH`.

## lint.py

```
python3 lint.py --article <article.md> --packet <packet.json> [--json] [--record-timing]
```

Exit 1 on any failure. Checks citations trace to packet claims, References and
in-text citations agree in both directions, the References table is well formed
and ordered with no invented dates, every quoted string of 12+ characters is
verbatim in a `quote_verbatim`, no reception language or meta commentary
anywhere, every prose line is cited, and frontmatter concept matches the packet.
Warns (does not fail) when more than 40% of packet episodes go uncited. Reports
its own `t_lint_s`; `--record-timing` appends that and the body word count.

## timing.py

Per-article timing, appended as JSON lines to `articles/factory/_timing.jsonl`.
One call is all an extraction agent needs:

```python
import sys; sys.path.insert(0, "articles/factory/tools")
from timing import append_timing

append_timing("altium", {
    "t_extract_s": 412.5,      # your reading + packet assembly wall time
    "passages_in": 250, "claims_kept": 88, "claims_killed": 162,
    "revisions": 1,
})
```

Every field is optional; `concept`, `ts_start`, `t_gather_s` (0.0 — bundles are
prebuilt) and `t_total_s` (summed from the phases) fill themselves in. Shell
callers can use `python3 timing.py --concept altium --t-extract-s 412.5
--claims-kept 88` instead, and `python3 timing.py --summary` prints the
aggregate.

**You do not need to record `t_kimi_s`, `t_lint_s` or `article_words`** —
`kimi_write.py` appends the API duration and `lint.py --record-timing` appends
the lint duration, both automatically. Records for one concept are partial by
design; `load()` and `summarize()` merge them, last non-null value winning,
except `ts_start`, which keeps the earliest. Record what you alone know:
`t_extract_s`, `passages_in`, `claims_kept`, `claims_killed`, `revisions`.

Writes are single `O_APPEND` calls, so parallel agents cannot interleave lines —
verified with 20 concurrent writers. `FACTORY_TIMING` overrides the file path if
you want a run kept separate. `make_manifest.py` folds `summarize()` into a
"Run timing" section of `_factory_report.md` whenever the file has records.
