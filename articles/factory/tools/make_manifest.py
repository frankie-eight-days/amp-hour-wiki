#!/usr/bin/env python3
"""Roll the per-bundle rows from build_bundles.py into _manifest.json and
_factory_report.md."""
import json, os, statistics, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from timing import summarize as timing_summary, TIMING

ROOT = "/Users/frankwalsh/Documents/vibecoding/amp_hour_wiki"
FAC = os.path.join(ROOT, "articles/factory")
ROWS = json.load(open(os.path.join(FAC, "_manifest_rows.json")))
THIN = 10

rows = sorted(ROWS, key=lambda r: r["rank_by_score"] or 10**6)
pas = [r["passages"] for r in rows]
byt = [r["bundle_bytes"] for r in rows]
capped = [r for r in rows if r["capped"]]
thin = [r for r in rows if r["passages"] < THIN]
relaxed = [r for r in rows if r["gate_relaxed"]]

totals = {
    "bundles": len(rows),
    "passages_total": sum(pas),
    "passages_available_pre_cap": sum(r["total_available"] for r in rows),
    "passages_min": min(pas), "passages_max": max(pas),
    "passages_mean": round(statistics.mean(pas), 1),
    "passages_median": statistics.median(pas),
    "capped_bundles": len(capped),
    "thin_risk_bundles": len(thin),
    "gate_relaxed_bundles": len(relaxed),
    "explains_total": sum(r["explains"] for r in rows),
    "opinions_total": sum(r["opinions"] for r in rows),
    "episodes_covered_union": None,      # filled below
    "bundle_bytes_total": sum(byt),
    "bundle_bytes_max": max(byt),
    "passages_with_unreliable_attribution":
        sum(r["unreliable_attribution_passages"] for r in rows),
    "cap": 250, "neighbor_weight_floor": 4, "thin_threshold": THIN,
}

eps = set()
for r in rows:
    b = json.load(open(os.path.join(ROOT, r["bundle"])))
    eps |= {p["episode"] for p in b["passages"]}
totals["episodes_covered_union"] = len(eps)

json.dump({"_meta": {"generated": "2026-08-08",
                     "source": "articles/factory/tools/build_bundles.py",
                     "census": "census/union", "cap": 250,
                     "neighbor_weight_floor": 4},
           "totals": totals, "bundles": rows},
          open(os.path.join(FAC, "_manifest.json"), "w"), indent=1)


def buckets(vals, edges):
    out = Counter()
    for v in vals:
        for lo, hi in edges:
            if lo <= v <= hi:
                out[f"{lo}-{hi}" if hi < 10**6 else f"{lo}+"] += 1
                break
    return out


EDGES = [(0, 9), (10, 24), (25, 49), (50, 99), (100, 149), (150, 199),
         (200, 249), (250, 10**6)]
dist = buckets(pas, EDGES)

L = []
L.append("# Factory prep report — evidence bundles\n")
L.append(f"Generated 2026-08-08 from `census/union` (717 episodes) for the "
         f"{len(rows)} `status=article` concepts in `articles/candidates.json`.\n")
L.append("## Method\n")
L.append("For each article concept the evidence cluster is: the concept plus every "
         "alias that canonicalises to it (core); every concept whose suggested parent "
         "is it (children); and every graph co-occurrence neighbour with edge weight "
         "≥ 4 whose own status is not `article` (neighbours). Core passages are kept "
         "unconditionally; child and neighbour passages are kept only when the ±1 "
         "paragraph window carries a lexical hit for the concept itself, so borrowed "
         "material has to actually be about the subject. Passages are `explains` or "
         "`opinion` depth only, deduplicated per (episode, paragraph), capped at 250 "
         "with all `explains` first and `opinion` filled in by speaker diversity then "
         "recency.\n")
L.append("## Totals\n")
L.append("| Metric | Value |")
L.append("| --- | --- |")
for k in ("bundles", "passages_total", "passages_available_pre_cap",
          "passages_median", "passages_mean", "passages_min", "passages_max",
          "capped_bundles", "thin_risk_bundles", "gate_relaxed_bundles",
          "episodes_covered_union", "passages_with_unreliable_attribution",
          "bundle_bytes_total"):
    L.append(f"| {k.replace('_', ' ')} | {totals[k]} |")
L.append("")
L.append("## Bundle size distribution (passages)\n")
L.append("| Passages | Bundles |")
L.append("| --- | --- |")
for lo, hi in EDGES:
    lbl = f"{lo}-{hi}" if hi < 10**6 else f"{lo}+"
    L.append(f"| {lbl} | {dist.get(lbl, 0)} |")
L.append("")
big = sorted(rows, key=lambda r: -r["total_available"])[:15]
small = sorted(rows, key=lambda r: r["passages"])[:15]
L.append("## Biggest 15 (by evidence available before the cap)\n")
L.append("| Concept | Passages kept | Available | Episodes | Children | Neighbours |")
L.append("| --- | --- | --- | --- | --- | --- |")
for r in big:
    L.append(f"| {r['concept']} | {r['passages']} | {r['total_available']} | "
             f"{r['episodes']} | {r['children']} | {r['neighbors']} |")
L.append("")
L.append("## Smallest 15\n")
L.append("| Concept | Passages | Episodes | Explains | Opinions |")
L.append("| --- | --- | --- | --- | --- |")
for r in small:
    L.append(f"| {r['concept']} | {r['passages']} | {r['episodes']} | "
             f"{r['explains']} | {r['opinions']} |")
L.append("")
L.append(f"## Capped bundles ({len(capped)})\n")
if capped:
    L.append("| Concept | Kept | Available | Discarded |")
    L.append("| --- | --- | --- | --- |")
    for r in sorted(capped, key=lambda r: -r["total_available"]):
        L.append(f"| {r['concept']} | {r['passages']} | {r['total_available']} | "
                 f"{r['total_available'] - r['passages']} |")
else:
    L.append("None.")
L.append("")
L.append(f"## Thin-risk bundles (< {THIN} passages)\n")
if thin:
    L.append("| Concept | Passages | Episodes |")
    L.append("| --- | --- | --- |")
    for r in sorted(thin, key=lambda r: r["passages"]):
        L.append(f"| {r['concept']} | {r['passages']} | {r['episodes']} |")
else:
    L.append(f"None — every bundle carries at least {min(pas)} passages.")
L.append("")
lean = [r for r in rows if THIN <= r["passages"] < 20]
L.append(f"## Lean bundles (10–19 passages, {len(lean)})\n")
L.append(", ".join(f"{r['concept']} ({r['passages']})"
                   for r in sorted(lean, key=lambda r: r["passages"])) or "None.")
L.append("")
if relaxed:
    L.append(f"## Gate relaxed ({len(relaxed)})\n")
    L.append("Lexical gating on child/neighbour passages was dropped for these "
             "because it would have left the bundle under the thin threshold.\n")
    L.append(", ".join(r["concept"] for r in relaxed))
    L.append("")
ts = timing_summary()
if ts.get("articles"):
    L.append(f"## Run timing ({ts['articles']} articles recorded)\n")
    L.append("From `_timing.jsonl`. Seconds unless noted.\n")
    L.append("| Phase / metric | n | total | mean | median | min | max |")
    L.append("| --- | --- | --- | --- | --- | --- | --- |")
    labels = {"t_gather_s": "gather", "t_extract_s": "extract",
              "t_kimi_s": "kimi call", "t_lint_s": "lint",
              "t_total_s": "total per article", "passages_in": "passages in",
              "claims_kept": "claims kept", "claims_killed": "claims killed",
              "article_words": "article words", "revisions": "revisions"}
    for k, lbl in labels.items():
        s = ts.get(k)
        if s:
            L.append(f"| {lbl} | {s['n']} | {s['total']} | {s['mean']} | "
                     f"{s['median']} | {s['min']} | {s['max']} |")
    if "claim_keep_rate" in ts:
        L.append(f"\nClaim keep rate: {ts['claim_keep_rate']:.1%}.\n")
    if ts.get("slowest"):
        L.append("\nSlowest articles: "
                 + ", ".join(f"{r['concept']} ({r['t_total_s']}s)"
                             for r in ts["slowest"]) + "\n")
elif os.path.exists(TIMING):
    L.append("## Run timing\n")
    L.append("`_timing.jsonl` exists but holds no usable records yet.\n")
open(os.path.join(FAC, "_factory_report.md"), "w").write("\n".join(L) + "\n")
print(json.dumps(totals, indent=1))
