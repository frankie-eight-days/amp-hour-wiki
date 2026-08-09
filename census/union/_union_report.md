# Census union: pass 1 + pass 2

Two independent extractions of the same 717 transcripts with the same model
(`gpt-5.6-luna`, effort `low`) and the same prompt (`census_prompt_v3_chunk.md`).
Extraction is stochastic, so pass 2 surfaces mentions pass 1 missed and vice
versa; this layer keeps the union of the two.

## Pass 2 run

| metric | pass 1 | pass 2 |
| --- | ---: | ---: |
| episodes | 717 | 717 |
| chunks | 6,585 | 6,585 |
| raw mentions | 218,202 | 219,541 |
| kept mentions | 197,424 | 198,464 |
| rejected | 17,851 | 18,164 |
| overlap dupes dropped | 2,927 | 2,915 |
| failed chunks | 26 | 13 |
| suspect-sparse chunks | 4 | 4 |
| retries | 537 | 505 |
| input tokens | 61,276,728 | 60,958,708 |
| output tokens | 12,665,024 | 12,647,105 |
| reasoning tokens | 2,053,028 | 2,036,457 |
| wall minutes | 13.6 | 0.5 |
| **cost (USD)** | **$27.45** | **$27.37** |

Pass-2 rejects break down as 18,155 snippet-not-found, 7 bad paragraph index, 2 malformed.
13 chunks never returned parseable JSON after all retries (pass 1: 26) -- half
pass 1's rate, which is consistent with the same sporadic malformed-JSON failure
mode rather than anything new.

The pass-2 wall figure is not comparable to pass 1: one worker wedged on a single
episode (726, Massimo Banzi) roughly 14 minutes in, past the 240s request timeout,
with the other 716 episodes already written. The run was killed and resumed; the
resume redid 7 episodes in 0.5 min, and that is the number the manifest records.
End-to-end pass 2 took about 35 minutes of wall time for ~14 minutes of work. The
7 redone episodes were billed twice, so true pass-2 spend is roughly $0.30 above
the manifest figure.

## Union totals

| | mentions | share of union |
| --- | ---: | ---: |
| pass 1 total | 197,424 | |
| pass 2 total | 198,464 | |
| **union total** | **270,979** | |
| found by both | 123,766 | 45.7% |
| unique to pass 1 | 73,088 | 27.0% |
| unique to pass 2 | 74,125 | 27.4% |

**Recall lift: union / pass 1 = 1.373x (+37.3% over pass 1).**

Agreement between the two passes is 45.7% of the union. Put the other way: of the
196,854 distinct mentions pass 1 found, pass 2 independently re-found 62.9% of them,
so roughly a third of what either pass sees, the other pass misses. Pass 1 alone
recovered 72.9% of what the two passes jointly find.

Collapsed by canonicalization within a single pass (two surface strings folding
to one canonical in the same paragraph): 570 in pass 1, 123 in pass 2.

## Incremental canonicalization

Pass 2 emitted 67,700 distinct concept strings, of which 22,839 were absent from the
pass-1 alias table.

| method | strings | share of new |
| --- | ---: | ---: |
| deterministic fold (case/hyphen/plural) | 230 | 1.0% |
| embedding, cosine >= 0.85 + type match | 3,318 | 14.5% |
| new canonical singletons | 19,291 | 84.5% |

1,834 strings cleared the cosine threshold but were blocked by a type mismatch and
became singletons rather than being merged across types.

Alias table grew from 67,311 entries (`canon/alias_table.json`) to 90,150
(`canon/alias_table_v2.json`). The delta alone is in
`canon/alias_table_pass2_extension.json`. The pass-1 table is unmodified.

Highest-volume embedding merges:

| new string | mapped to | cosine | mentions |
| --- | --- | ---: | ---: |
| t-shirt-merchandise | t-shirt-merchandising | 0.865 | 11 |
| electric-delivery-van | electric-delivery-truck | 0.929 | 7 |
| pcb-assembly-line | pcb-assembly-automation | 0.883 | 5 |
| product-refresh | product-refresh-cycle | 0.890 | 5 |
| tpic-6595 | tpic6595 | 0.948 | 5 |
| 14-bit-adc | 16-bit-adc | 0.886 | 4 |
| automotive-infotainment-system | automotive-infotainment | 0.945 | 4 |
| dc-circuit-analysis | ac-circuit-analysis | 0.853 | 4 |
| digital-advertising | online-advertising | 0.852 | 4 |
| epcot | epcot-center | 0.897 | 4 |
| event-organisation | event-organization | 0.933 | 4 |
| five-nanometer-process-node | five-nanometer-process | 0.889 | 4 |

Embedding merges at this threshold are mostly spelling, plural and word-order
variants, but cosine similarity does not distinguish antonyms or adjacent numeric
variants: `14-bit-adc` -> `16-bit-adc` and `dc-circuit-analysis` ->
`ac-circuit-analysis` are both wrong merges that cleared 0.85. They affect single-
digit mention counts here, but the same failure would matter more if the threshold
were lowered.

## Altium cluster, before and after

`altium` and the 13 child concepts, with the v2 alias table applied. *Before* is
the pass-1 census; *after* is the union. Both are counted from their own files, so
the `explains` columns reflect each layer's own depth labels.

| concept | mentions before | mentions after | delta | explains before | explains after |
| --- | ---: | ---: | ---: | ---: | ---: |
| altium | 606 | 702 | +96 | 52 | 75 |
| hiring | 79 | 115 | +36 | 13 | 30 |
| software-maintenance | 25 | 36 | +11 | 13 | 18 |
| software-subscription | 26 | 39 | +13 | 13 | 19 |
| parametric-modeling | 16 | 18 | +2 | 13 | 16 |
| altium-designer | 48 | 63 | +15 | 12 | 17 |
| switching-cost | 13 | 16 | +3 | 12 | 13 |
| eda | 49 | 77 | +28 | 11 | 16 |
| software-bug | 32 | 48 | +16 | 10 | 21 |
| upverter | 57 | 74 | +17 | 10 | 20 |
| cad-software | 56 | 90 | +34 | 9 | 15 |
| pcb-rework | 16 | 19 | +3 | 8 | 10 |
| onshape | 30 | 35 | +5 | 8 | 13 |
| autorouter | 39 | 60 | +21 | 6 | 12 |
| **cluster total** | **1092** | **1392** | **+300** | **190** | **295** |

Cluster mentions grew 27.5% and `explains`-depth mentions grew 55.3%.

---

Generated from `census/luna-v3/`, `census/luna-v3-pass2/` and `census/union/`.
