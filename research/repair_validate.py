#!/usr/bin/env python3
"""Validate and repair concept-census JSON against Amp Hour transcripts.

Usage:
    python3 research/repair_validate.py \
        --census-dir  research/bakeoff/haiku \
        --transcript-dir transcripts \
        --out-dir research/bakeoff/haiku_repaired \
        --report research/bakeoff/haiku_validation_report.json

Without --out-dir nothing is written: the run validates and reports only.
Exits non-zero when any file still has unresolvable mentions after repair.

`--selftest` runs a self-contained correctness check with planted defects and
exits 0/1 on pass/fail.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from typing import Any, Dict, List, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from census_lib import (  # noqa: E402
    STRATEGY_UNRESOLVED,
    Transcript,
    parse_transcript,
    repair,
    report,
    validate,
)


# --------------------------------------------------------------------------
# Transcript lookup
# --------------------------------------------------------------------------


def build_transcript_index(transcript_dir: str) -> Dict[str, str]:
    """Map basename and stem -> absolute path for every .md in the directory."""
    index: Dict[str, str] = {}
    for name in sorted(os.listdir(transcript_dir)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(transcript_dir, name)
        if not os.path.isfile(path):
            continue
        index[name] = path
        index.setdefault(os.path.splitext(name)[0], path)
    return index


def locate_transcript(
    census: Dict[str, Any], census_path: str, index: Dict[str, str]
) -> Optional[str]:
    """Find the transcript for a census: `file` field first, then basenames."""
    candidates: List[str] = []
    declared = census.get("file")
    if isinstance(declared, str) and declared:
        base = os.path.basename(declared)
        candidates += [base, os.path.splitext(base)[0]]
    census_base = os.path.basename(census_path)
    candidates += [
        os.path.splitext(census_base)[0] + ".md",
        os.path.splitext(census_base)[0],
    ]
    for c in candidates:
        if c in index:
            return index[c]
    return None


# --------------------------------------------------------------------------
# Per-file processing
# --------------------------------------------------------------------------


def offset_valid_count(census: Dict[str, Any], tr: Transcript) -> int:
    from census_lib import _offset_ok

    mentions = census.get("mentions") or []
    return sum(
        1
        for m in mentions
        if isinstance(m, dict)
        and _offset_ok(tr.body, m.get("char_start"), m.get("context_snippet"))
    )


def issues_to_dicts(issues) -> List[Dict[str, Any]]:
    return [
        {
            "severity": i.severity,
            "code": i.code,
            "mention_index": i.mention_index,
            "detail": i.detail,
        }
        for i in issues
    ]


def process_file(
    census_path: str, index: Dict[str, str], out_dir: Optional[str]
) -> Dict[str, Any]:
    with open(census_path, "r", encoding="utf-8") as fh:
        census = json.load(fh)

    tpath = locate_transcript(census, census_path, index)
    if tpath is None:
        return {
            "census_file": os.path.basename(census_path),
            "status": "transcript-not-found",
            "declared_file": census.get("file"),
        }

    tr = parse_transcript(tpath)

    before_issues = validate(census, tr)
    before_valid = offset_valid_count(census, tr)
    n = len([m for m in (census.get("mentions") or []) if isinstance(m, dict)])

    repaired, actions = repair(census, tr)

    # Idempotency guard: repairing the repaired copy must be a fixed point.
    twice, _ = repair(repaired, tr)
    idempotent = twice == repaired

    after_issues = validate(repaired, tr)
    after_valid = offset_valid_count(repaired, tr)

    strategies: Dict[str, int] = {}
    for a in actions:
        strategies[a.strategy] = strategies.get(a.strategy, 0) + 1
    unresolvable = [a for a in actions if a.strategy == STRATEGY_UNRESOLVED]

    rep = report(repaired, tr)
    rep_before = report(census, tr)

    written = None
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        written = os.path.join(out_dir, os.path.basename(census_path))
        with open(written, "w", encoding="utf-8") as fh:
            json.dump(repaired, fh, indent=2, ensure_ascii=False)
            fh.write("\n")

    return {
        "census_file": os.path.basename(census_path),
        "status": "ok",
        "transcript_path": tr.path,
        "transcript_file": tr.file,
        "episode_frontmatter": tr.episode,
        "paragraphs": len(tr.paragraphs),
        "body_chars": len(tr.body),
        "mentions": n,
        "offset_valid_before": before_valid,
        "offset_valid_after": after_valid,
        "unresolvable": len(unresolvable),
        "unresolvable_mentions": [
            {"mention_index": a.mention_index, "detail": a.detail} for a in unresolvable
        ],
        "repair_strategies": strategies,
        "repair_idempotent": idempotent,
        "errors_before": len([i for i in before_issues if i.severity == "error"]),
        "errors_after": len([i for i in after_issues if i.severity == "error"]),
        "errors_by_code_before": rep_before["errors_by_code"],
        "errors_by_code_after": rep["errors_by_code"],
        "issues_after": issues_to_dicts(after_issues),
        "report_before": rep_before,
        "report_after": rep,
        "written_to": written,
    }


def fmt_shares(shares: Dict[str, float]) -> str:
    order = ["explains", "opinion", "mention"]
    keys = [k for k in order if k in shares] + [k for k in sorted(shares) if k not in order]
    return " ".join("%s=%.2f" % (k, shares[k]) for k in keys)


def print_summary(r: Dict[str, Any]) -> None:
    if r["status"] != "ok":
        print("%-64s  %s (declared file=%r)" % (r["census_file"], r["status"], r.get("declared_file")))
        return
    rep = r["report_after"]
    print("%s" % r["census_file"])
    print(
        "  mentions=%-4d offsets %d -> %d  unresolvable=%d  coverage=%d/%d (%.3f) "
        "max_para=%s/%d"
        % (
            r["mentions"],
            r["offset_valid_before"],
            r["offset_valid_after"],
            r["unresolvable"],
            rep["paragraphs_covered"],
            rep["paragraphs_total"],
            rep["coverage_fraction"],
            rep["max_paragraph_index"],
            rep["paragraphs_total"],
        )
    )
    print(
        "  depth %s  explains_in_band=%s  mentions_in_band=%s  distinct=%d  asr_suspect=%d"
        % (
            fmt_shares(rep["depth_shares"]),
            rep["explains_in_band"],
            rep["mentions_in_band"],
            rep["distinct_concepts"],
            rep["asr_suspect_count"],
        )
    )
    if r["repair_strategies"]:
        print(
            "  repairs: "
            + ", ".join("%s=%d" % kv for kv in sorted(r["repair_strategies"].items()))
        )
    before = r["errors_by_code_before"]
    after = r["errors_by_code_after"]
    print(
        "  errors before: %s"
        % (", ".join("%s=%d" % kv for kv in sorted(before.items())) or "none")
    )
    print(
        "  errors after:  %s"
        % (", ".join("%s=%d" % kv for kv in sorted(after.items())) or "none")
    )
    if not r["repair_idempotent"]:
        print("  !! repair is NOT idempotent for this file")


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

SELFTEST_BODY = """**Chris Gammell:** Welcome back. Today we are talking about the solder paste stencil and how it changes assembly yield in a real way.

**Dave Jones:** Yeah, the reflow oven profile matters more than people think, because the ramp rate sets the thermal shock on the parts.

**Speaker ?:** I penalized my board last week and the panelization saved me forty dollars per run.

**Parallela:** We taped out on a shuttle run, so the mask set cost was shared across everybody on that wafer.

**Chris Gammell:** Right.
"""

SELFTEST_FRONTMATTER = """---
episode: 999
title: Selftest Episode
url: https://theamphour.com/999-selftest/
---

"""


def _mk(concept, ctype, speaker, pidx, cs, depth, snippet, **extra):
    m = {
        "concept": concept,
        "type": ctype,
        "speaker": speaker,
        "paragraph_index": pidx,
        "char_start": cs,
        "depth": depth,
        "context_snippet": snippet,
    }
    m.update(extra)
    return m


def selftest() -> int:
    tmp = tempfile.mkdtemp(prefix="census-selftest-")
    try:
        tpath = os.path.join(tmp, "0999-selftest-episode.md")
        with open(tpath, "w", encoding="utf-8") as fh:
            fh.write(SELFTEST_FRONTMATTER + SELFTEST_BODY)

        tr = parse_transcript(tpath)
        body = tr.body

        # ---- parser invariants -------------------------------------------
        # REGRESSION GUARD. The spec's body keeps the single newline that sits
        # between the closing '---' and the first speaker label: it starts
        # "\n**", not "**". A body built with .lstrip("\n") would shift every
        # offset down by one and reject spec-correct censuses wholesale.
        assert body.startswith("\n**"), repr(body[:40])
        assert not body.startswith("\n\n"), "body kept more than one newline"
        assert tr.paragraphs[0].start == 1, tr.paragraphs[0].start
        assert len(tr.paragraphs) == 5, len(tr.paragraphs)
        for p in tr.paragraphs:
            assert body[p.start:p.end] == p.text, p.index
        assert [p.speaker for p in tr.paragraphs] == [
            "Chris Gammell",
            "Dave Jones",
            "Speaker ?",
            "Parallela",
            "Chris Gammell",
        ], [p.speaker for p in tr.paragraphs]
        assert tr.episode == 999 and tr.title == "Selftest Episode"
        assert tr.paragraphs[0].speech.startswith("Welcome back."), tr.paragraphs[0].speech[:30]

        def off(s: str) -> int:
            i = body.find(s)
            assert i != -1, "selftest fixture snippet not in body: %r" % s
            return i

        # ---- planted mentions --------------------------------------------
        s_good = "solder paste stencil and how it changes assembly yield"
        s_badoff = "reflow oven profile matters more than people think"
        s_offbyn = "panelization saved me forty dollars per run"
        s_ws = "mask  set   cost was shared across everybody"  # whitespace-mangled
        s_speaker = "the ramp rate sets the thermal shock"
        s_enum = "taped out on a shuttle run"
        s_long = body[tr.paragraphs[0].start:tr.paragraphs[0].start + 120]
        s_absent = "there is no such sentence anywhere in this transcript body"
        # Anchored at the very first character of paragraph 0, i.e. char_start
        # == 1 in the spec-correct body. Under the old lstrip("\n") convention
        # this snippet lived at 0, so this mention is the tripwire for the
        # off-by-one: validate() must accept it untouched.
        s_head = body[tr.paragraphs[0].start:tr.paragraphs[0].start + 31]
        assert s_head.startswith("**Chris Gammell:** Welcome"), s_head

        mentions = [
            # 0 clean baseline
            _mk("solder-paste-stencil", "tool-equipment", "Chris Gammell", 0,
                off(s_good), "explains", s_good),
            # 1 bad offset (wildly wrong) -- fixable in stated paragraph
            _mk("reflow-oven", "tool-equipment", "Dave Jones", 1, 3, "explains", s_badoff),
            # 2 off-by-N offset -- fixable in stated paragraph
            _mk("panelization", "manufacturing", "Speaker ?", 2,
                off(s_offbyn) + 7, "opinion", s_offbyn),
            # 3 whitespace-mangled snippet -- fixable by strategy 4
            _mk("mask-set-cost", "industry-economics", "Parallela", 3, 0, "explains", s_ws),
            # 4 wrong speaker, offset fine
            _mk("thermal-shock", "concept-principle", "Chris Gammell", 1,
                off(s_speaker), "explains", s_speaker),
            # 5 bad depth enum (offset fine)
            _mk("tape-out", "manufacturing", "Parallela", 3, off(s_enum), "mentions", s_enum),
            # 6 snippet > 100 chars (offset fine)
            _mk("assembly-yield", "manufacturing", "Chris Gammell", 0,
                tr.paragraphs[0].start, "opinion", s_long),
            # 7 duplicate of (concept, paragraph) with #0
            _mk("solder-paste-stencil", "tool-equipment", "Chris Gammell", 0,
                off(s_good), "mention", s_good),
            # 8 unresolvable: snippet is not in the body at all
            _mk("ghost-concept", "other", "Dave Jones", 1, 12, "mention", s_absent),
            # 9 bad type enum + bad concept format + illegal asr_suspect value
            _mk("Bad_Concept", "gizmo", "Dave Jones", 1, off(s_badoff), "opinion",
                s_badoff, asr_suspect=False),
            # 10 spec-correct offset at the head of paragraph 0 (char_start == 1).
            #    Must validate clean and survive repair byte-identical.
            _mk("amp-hour", "media-resource", "Chris Gammell", 0,
                tr.paragraphs[0].start, "mention", s_head),
        ]
        assert mentions[10]["char_start"] == 1, mentions[10]["char_start"]

        census = {
            "episode": 999,
            "title": "Selftest Episode",
            "url": "https://theamphour.com/999-selftest/",
            "file": "0999-selftest-episode.md",
            "main_topics": ["solder-paste-stencil", "not-a-mentioned-concept"],
            "guest_name": None,
            "guest_affiliation": None,
            "notes": None,
            "mentions": mentions,
        }

        # ---- validate flags exactly the planted defects --------------------
        issues = validate(census, tr)
        flagged = {(i.code, i.mention_index) for i in issues}

        expected = {
            ("main-topic-not-a-mention", None),
            ("offset-mismatch", 1),
            ("offset-mismatch", 2),
            ("offset-mismatch", 3),
            ("offset-mismatch", 8),
            ("speaker-mismatch", 4),
            ("depth-enum", 5),
            ("snippet-too-long", 6),
            ("duplicate-concept-paragraph", 7),
            ("type-enum", 9),
            ("concept-format", 9),
            ("asr-suspect-value", 9),
        }
        # mention 2's off-by-N span leaves the paragraph? no -- but 3's char 0 and
        # 8's char 12 land outside their stated paragraph, which is subsumed by
        # the offset error (containment is only checked when the offset holds).
        missing = expected - flagged
        assert not missing, "validate missed planted issues: %s" % sorted(missing)
        unexpected = flagged - expected
        assert not unexpected, "validate raised unplanted issues: %s" % sorted(unexpected)

        # depth enum message must call out the pluralisation explicitly
        depth_issue = next(i for i in issues if i.code == "depth-enum")
        assert "pluralised" in depth_issue.detail, depth_issue.detail

        # ---- repair fixes exactly the fixable ones ------------------------
        fixed, actions = repair(census, tr)
        assert census["mentions"][1]["char_start"] == 3, "repair mutated its input"

        by_idx: Dict[int, List[str]] = {}
        for a in actions:
            by_idx.setdefault(a.mention_index, []).append(a.strategy)

        assert "exact-in-stated-paragraph" in by_idx.get(1, []), by_idx.get(1)
        assert "exact-in-stated-paragraph" in by_idx.get(2, []), by_idx.get(2)
        assert "whitespace-tolerant-unique" in by_idx.get(3, []), by_idx.get(3)
        assert by_idx.get(8) == [STRATEGY_UNRESOLVED], by_idx.get(8)
        # 9 already had a valid offset, so repair must leave it entirely alone:
        # bad enums and concept format are validation errors, not repairs.
        assert 9 not in by_idx, by_idx.get(9)
        assert fixed["mentions"][9] == census["mentions"][9], fixed["mentions"][9]

        # mention 4 kept its (valid) offset but got its speaker resynced
        assert fixed["mentions"][4]["speaker"] == "Dave Jones", fixed["mentions"][4]
        assert fixed["mentions"][4]["char_start"] == census["mentions"][4]["char_start"]

        # whitespace repair rewrote the snippet to true verbatim text
        m3 = fixed["mentions"][3]
        assert body[m3["char_start"]:m3["char_start"] + len(m3["context_snippet"])] == \
            m3["context_snippet"], m3
        assert m3["context_snippet"] != s_ws, "whitespace snippet was not rewritten"
        assert m3["context_snippet"] == "mask set cost was shared across everybody", m3

        # unresolvable mention untouched
        assert fixed["mentions"][8] == census["mentions"][8], fixed["mentions"][8]

        # ---- off-by-one regression guard -----------------------------------
        # The spec-correct head mention must be accepted with zero offset errors
        # and must come through repair byte-identical (not even a resync).
        assert 10 not in by_idx or by_idx[10] == [], by_idx.get(10)
        assert fixed["mentions"][10] == census["mentions"][10], fixed["mentions"][10]
        assert not any(
            i.mention_index == 10 for i in issues
        ), [i for i in issues if i.mention_index == 10]
        # ...and the value the buggy lstrip("\n") convention would produce for
        # the same mention (one lower) must be REJECTED.
        buggy = json.loads(json.dumps(census))
        buggy["mentions"][10]["char_start"] = 0
        assert ("offset-mismatch", 10) in {
            (i.code, i.mention_index) for i in validate(buggy, tr)
        }, "off-by-one char_start was not caught"

        after = validate(fixed, tr)
        after_flagged = {(i.code, i.mention_index) for i in after}
        expected_after = {
            ("main-topic-not-a-mention", None),
            ("offset-mismatch", 8),
            ("depth-enum", 5),
            ("snippet-too-long", 6),
            ("duplicate-concept-paragraph", 7),
            ("type-enum", 9),
            ("concept-format", 9),
            ("asr-suspect-value", 9),
        }
        assert after_flagged == expected_after, (
            "post-repair issues differ: missing=%s unexpected=%s"
            % (sorted(expected_after - after_flagged), sorted(after_flagged - expected_after))
        )

        # ---- idempotence ---------------------------------------------------
        again, actions2 = repair(fixed, tr)
        assert again == fixed, "repair is not idempotent"
        third, _ = repair(again, tr)
        assert third == fixed, "repair is not idempotent on the third pass"

        # ---- report sanity --------------------------------------------------
        rep = report(fixed, tr)
        assert rep["mentions"] == 11, rep["mentions"]
        assert rep["mentions_in_band"] is False
        assert rep["paragraphs_total"] == 5
        assert rep["paragraphs_covered"] == 4, rep["paragraphs_covered"]
        assert abs(rep["coverage_fraction"] - 0.8) < 1e-9
        assert rep["max_paragraph_index"] == 3, rep["max_paragraph_index"]
        assert rep["distinct_concepts"] == 10, rep["distinct_concepts"]
        assert rep["asr_suspect_count"] == 0
        assert rep["errors_by_code"]["offset-mismatch"] == 1
        assert abs(sum(rep["depth_shares"].values()) - 1.0) < 1e-9

        # ---- header mismatch detection ------------------------------------
        bad_header = json.loads(json.dumps(fixed))
        bad_header["episode"] = None
        bad_header["file"] = "wrong.md"
        codes = {i.code for i in validate(bad_header, tr)}
        assert "header-episode-mismatch" in codes
        assert "header-file-mismatch" in codes
        del bad_header["url"]
        assert "header-missing-key" in {i.code for i in validate(bad_header, tr)}

        # ---- missing-episode frontmatter is legal --------------------------
        t2 = os.path.join(tmp, "legacy.md")
        with open(t2, "w", encoding="utf-8") as fh:
            fh.write("---\ntitle: Legacy\nurl: https://x/\n---\n\n" + SELFTEST_BODY)
        tr2 = parse_transcript(t2)
        assert tr2.episode is None
        c2 = {
            "episode": None, "title": "Legacy", "url": "https://x/", "file": "legacy.md",
            "main_topics": ["a-b", "c-d"], "guest_name": None,
            "guest_affiliation": None, "notes": None, "mentions": [],
        }
        codes2 = {i.code for i in validate(c2, tr2)}
        assert "header-episode-mismatch" not in codes2, codes2

        # ---- end-to-end through process_file -------------------------------
        cdir = os.path.join(tmp, "census")
        odir = os.path.join(tmp, "out")
        os.makedirs(cdir)
        cpath = os.path.join(cdir, "0999-selftest-episode.json")
        with open(cpath, "w", encoding="utf-8") as fh:
            json.dump(census, fh)
        r = process_file(cpath, build_transcript_index(tmp), odir)
        assert r["status"] == "ok"
        assert r["offset_valid_before"] == 7, r["offset_valid_before"]
        assert r["offset_valid_after"] == 10, r["offset_valid_after"]
        assert r["unresolvable"] == 1
        assert r["repair_idempotent"] is True
        with open(r["written_to"], "r", encoding="utf-8") as fh:
            reread = json.load(fh)
        assert reread == fixed

        print("selftest: PASS (%d paragraphs, %d planted issues verified)" % (
            len(tr.paragraphs), len(expected)))
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--census-dir", help="directory of *.json census files")
    ap.add_argument("--transcript-dir", help="directory of *.md transcripts")
    ap.add_argument(
        "--out-dir",
        default=None,
        help="write repaired JSON here; omit to validate/report only (writes nothing)",
    )
    ap.add_argument("--report", default=None, help="path for the JSON report")
    ap.add_argument("--selftest", action="store_true", help="run the built-in self-test and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    if not args.census_dir or not args.transcript_dir:
        ap.error("--census-dir and --transcript-dir are required (or use --selftest)")

    census_dir = os.path.abspath(args.census_dir)
    transcript_dir = os.path.abspath(args.transcript_dir)
    out_dir = os.path.abspath(args.out_dir) if args.out_dir else None
    if out_dir and os.path.abspath(census_dir) == out_dir:
        print("refusing to write repaired output over the census input directory", file=sys.stderr)
        return 2

    index = build_transcript_index(transcript_dir)
    files = sorted(f for f in os.listdir(census_dir) if f.endswith(".json"))
    if not files:
        print("no *.json census files in %s" % census_dir, file=sys.stderr)
        return 2

    results: List[Dict[str, Any]] = []
    for name in files:
        results.append(process_file(os.path.join(census_dir, name), index, out_dir))

    ok = [r for r in results if r["status"] == "ok"]
    agg = {
        "files": len(results),
        "files_ok": len(ok),
        "files_transcript_not_found": len(results) - len(ok),
        "mentions": sum(r["mentions"] for r in ok),
        "offset_valid_before": sum(r["offset_valid_before"] for r in ok),
        "offset_valid_after": sum(r["offset_valid_after"] for r in ok),
        "unresolvable": sum(r["unresolvable"] for r in ok),
        "errors_before": sum(r["errors_before"] for r in ok),
        "errors_after": sum(r["errors_after"] for r in ok),
        "all_repairs_idempotent": all(r["repair_idempotent"] for r in ok),
    }
    codes_after: Dict[str, int] = {}
    strategies: Dict[str, int] = {}
    for r in ok:
        for k, v in r["errors_by_code_after"].items():
            codes_after[k] = codes_after.get(k, 0) + v
        for k, v in r["repair_strategies"].items():
            strategies[k] = strategies.get(k, 0) + v
    agg["errors_by_code_after"] = codes_after
    agg["repair_strategies"] = strategies

    for r in results:
        print_summary(r)
        print()

    print("AGGREGATE")
    print(
        "  files=%d  mentions=%d  offsets %d -> %d  unresolvable=%d  errors %d -> %d"
        % (
            agg["files"],
            agg["mentions"],
            agg["offset_valid_before"],
            agg["offset_valid_after"],
            agg["unresolvable"],
            agg["errors_before"],
            agg["errors_after"],
        )
    )
    print(
        "  repairs: "
        + (", ".join("%s=%d" % kv for kv in sorted(strategies.items())) or "none")
    )
    print(
        "  remaining errors: "
        + (", ".join("%s=%d" % kv for kv in sorted(codes_after.items())) or "none")
    )
    if out_dir:
        print("  wrote repaired census files to %s" % out_dir)
    else:
        print("  (no --out-dir: nothing written)")

    if args.report:
        rpath = os.path.abspath(args.report)
        os.makedirs(os.path.dirname(rpath), exist_ok=True)
        payload = {
            "census_dir": census_dir,
            "transcript_dir": transcript_dir,
            "out_dir": out_dir,
            "aggregate": agg,
            "files": results,
        }
        with open(rpath, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print("  wrote report to %s" % rpath)

    return 1 if (agg["unresolvable"] or agg["files_transcript_not_found"]) else 0


if __name__ == "__main__":
    sys.exit(main())
