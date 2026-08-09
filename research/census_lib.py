"""Deterministic toolkit for the Amp Hour concept-census pipeline.

Parsing, indexing, offset computation, validation, repair and reporting for the
JSON censuses produced by an LLM against transcripts in `transcripts/`.

This module contains no semantic extraction logic whatsoever: concept discovery
is done by the model, everything here is mechanical and reproducible.

Spec: research/census_prompt_v2.md (sections "Input format", "Field rules",
"Coverage rules").
"""

from __future__ import annotations

import copy
import os
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

__all__ = [
    "Paragraph",
    "Transcript",
    "Issue",
    "RepairAction",
    "VALID_TYPES",
    "VALID_DEPTHS",
    "CONCEPT_RE",
    "MAX_SNIPPET_LEN",
    "parse_transcript",
    "validate",
    "repair",
    "report",
]


# --------------------------------------------------------------------------
# Constants from the spec
# --------------------------------------------------------------------------

#: The exact sixteen types of the spec's type table.
VALID_TYPES = frozenset(
    {
        "component",
        "technique",
        "tool-equipment",
        "software",
        "company-product",
        "standard-protocol",
        "manufacturing",
        "career",
        "business-model",
        "industry-economics",
        "engineering-practice",
        "community-event",
        "media-resource",
        "person",
        "concept-principle",
        "other",
    }
)

#: The three depth values, in descending order of informativeness.
VALID_DEPTHS = frozenset({"explains", "opinion", "mention"})

#: lowercase, ASCII, hyphen-separated.
CONCEPT_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

MAX_SNIPPET_LEN = 100

#: Spec: "Expect 150-300 mentions for a typical hour-long episode".
MENTION_BAND = (150, 300)

#: Spec: "roughly a quarter to a third of mentions to be `explains`".
EXPLAINS_BAND = (0.25, 0.33)

REQUIRED_HEADER_KEYS = (
    "episode",
    "title",
    "url",
    "file",
    "main_topics",
    "guest_name",
    "guest_affiliation",
    "notes",
    "mentions",
)

REQUIRED_MENTION_KEYS = (
    "concept",
    "type",
    "speaker",
    "paragraph_index",
    "char_start",
    "depth",
    "context_snippet",
)

_SPEAKER_RE = re.compile(r"^\*\*(.+?):\*\*")
_PARA_SPLIT_RE = re.compile(r"\n\n+")


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Paragraph:
    """One non-empty, blank-line-delimited paragraph of the transcript body."""

    index: int
    start: int
    end: int
    text: str
    speaker: Optional[str]
    speech: str

    def contains_span(self, start: int, length: int) -> bool:
        """True when [start, start+length) lies inside this paragraph."""
        return start >= self.start and (start + length) <= self.end


@dataclass
class Transcript:
    path: str
    file: str
    episode: Optional[int]
    title: Optional[str]
    url: Optional[str]
    frontmatter: Dict[str, str]
    body: str
    paragraphs: List[Paragraph] = field(default_factory=list)

    def paragraph_at(self, offset: int) -> Optional[Paragraph]:
        """Paragraph whose span contains `offset`, or None (inter-paragraph)."""
        for p in self.paragraphs:
            if p.start <= offset < p.end:
                return p
        return None


@dataclass(frozen=True)
class Issue:
    severity: str  # "error" | "warn"
    code: str
    mention_index: Optional[int]
    detail: str


@dataclass(frozen=True)
class RepairAction:
    mention_index: int
    strategy: str  # see repair() docstring
    detail: str
    old_char_start: Any = None
    new_char_start: Any = None


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------


def _parse_frontmatter(lines: List[str]) -> Tuple[Dict[str, str], int]:
    """Return (mapping, index of line after the closing '---').

    `lines` are the raw file lines *without* trailing newlines. The file must
    begin with a line that is exactly '---'; the closing delimiter is the next
    line that is exactly '---'.
    """
    if not lines or lines[0].strip() != "---":
        raise ValueError("file does not begin with a '---' frontmatter delimiter")

    close = None
    for i in range(1, len(lines)):
        if lines[i] == "---":
            close = i
            break
    if close is None:
        raise ValueError("frontmatter is never closed by a line that is exactly '---'")

    fm: Dict[str, str] = {}
    for raw in lines[1:close]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            continue
        key, _, value = raw.partition(":")
        key = key.strip()
        value = value.strip()
        # Unquoted scalars, but tolerate a stray wrapping quote.
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        if key:
            fm[key] = value
    return fm, close + 1


def _split_paragraphs(body: str) -> List[Paragraph]:
    paragraphs: List[Paragraph] = []
    cursor = 0
    idx = 0
    for chunk in _PARA_SPLIT_RE.split(body):
        start = body.index(chunk, cursor) if chunk else cursor
        end = start + len(chunk)
        cursor = end
        if not chunk.strip():
            continue
        # The spec-correct body retains exactly one leading newline (see
        # parse_transcript), so the FIRST chunk is "\n**Speaker:** ...".
        # That newline is not part of the paragraph: skip past it and move
        # `start` with it, so the invariant body[start:end] == text still
        # holds, "**Name:**" still parses, and no spurious empty paragraph 0
        # is created. Only leading newlines are trimmed; trailing text is
        # left exactly as the split produced it.
        lead = len(chunk) - len(chunk.lstrip("\n"))
        if lead:
            start += lead
            chunk = body[start:end]
        m = _SPEAKER_RE.match(chunk)
        if m:
            speaker = m.group(1)
            speech = chunk[m.end():].lstrip()
        else:
            speaker = None
            speech = chunk
        paragraphs.append(
            Paragraph(
                index=idx,
                start=start,
                end=end,
                text=chunk,
                speaker=speaker,
                speech=speech,
            )
        )
        idx += 1
    return paragraphs


def parse_transcript(path: str) -> Transcript:
    """Parse a transcript markdown file into a `Transcript`.

    Offsets are measured into `body`. Per the spec (research/census_prompt_v2.md,
    "Input format"):

        "The **body** is everything after the closing `---` of the frontmatter,
         with the single newline that follows it stripped."

    Read literally: "the closing `---`" is the three-character delimiter itself.
    What follows it in the file is "\\n\\n**Chris Gammell:** ...", and stripping
    *the single newline that follows it* removes exactly ONE newline. The body
    therefore STARTS WITH A NEWLINE: "\\n**Chris Gammell:** ...".

    DO NOT "tidy" this into `.lstrip("\\n")`. Stripping all leading newlines
    shifts every offset down by one and makes spec-correct censuses validate as
    100% invalid. This was a real, load-bearing bug.
    """
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()

    lines = raw.split("\n")
    fm, body_line = _parse_frontmatter(lines)

    # Character offset in `raw` of the start of line `body_line`, i.e. of the
    # first character after the closing "---" delimiter and its own newline.
    # Consuming that delimiter-terminating newline IS the "single newline that
    # follows it" the spec strips; everything from here on is the body verbatim,
    # blank line included. No lstrip, no strip of any kind.
    body_offset = sum(len(line) + 1 for line in lines[:body_line])
    body = raw[body_offset:]

    if not body.startswith("\n**"):
        preview = body[:80].replace("\n", "\\n")
        raise ValueError(
            "body of %s does not start with the spec-mandated single newline "
            "followed by a '**Speaker:**' label (expected '\\n**'); got %r"
            % (os.path.basename(path), preview)
        )

    episode: Optional[int] = None
    if "episode" in fm:
        try:
            episode = int(str(fm["episode"]).strip())
        except (TypeError, ValueError):
            raise ValueError(
                "frontmatter 'episode' of %s is not an integer: %r"
                % (os.path.basename(path), fm["episode"])
            )

    tr = Transcript(
        path=os.path.abspath(path),
        file=os.path.basename(path),
        episode=episode,
        title=fm.get("title"),
        url=fm.get("url"),
        frontmatter=fm,
        body=body,
        paragraphs=_split_paragraphs(body),
    )

    # Hard invariant: paragraph spans index back into the body exactly.
    for p in tr.paragraphs:
        assert tr.body[p.start:p.end] == p.text, (
            "paragraph %d of %s does not round-trip through its offsets"
            % (p.index, tr.file)
        )
    return tr


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------


def _offset_ok(body: str, char_start: Any, snippet: Any) -> bool:
    if not isinstance(char_start, int) or isinstance(char_start, bool):
        return False
    if not isinstance(snippet, str) or not snippet:
        return False
    if char_start < 0 or char_start + len(snippet) > len(body):
        return False
    return body[char_start:char_start + len(snippet)] == snippet


def validate(census: Dict[str, Any], tr: Transcript) -> List[Issue]:
    """Check a census against its transcript. Returns a list of `Issue`."""
    issues: List[Issue] = []

    def err(code: str, detail: str, mi: Optional[int] = None) -> None:
        issues.append(Issue("error", code, mi, detail))

    def warn(code: str, detail: str, mi: Optional[int] = None) -> None:
        issues.append(Issue("warn", code, mi, detail))

    if not isinstance(census, dict):
        err("header-not-object", "census is %s, not an object" % type(census).__name__)
        return issues

    # ---- header -----------------------------------------------------------
    for key in REQUIRED_HEADER_KEYS:
        if key not in census:
            err("header-missing-key", "missing required header key %r" % key)

    if "episode" in census and census["episode"] != tr.episode:
        err(
            "header-episode-mismatch",
            "census episode %r != transcript frontmatter %r"
            % (census["episode"], tr.episode),
        )
    if "title" in census and census["title"] != tr.title:
        err(
            "header-title-mismatch",
            "census title %r != transcript title %r" % (census["title"], tr.title),
        )
    if "url" in census and census["url"] != tr.url:
        err(
            "header-url-mismatch",
            "census url %r != transcript url %r" % (census["url"], tr.url),
        )
    if "file" in census and census["file"] != tr.file:
        err(
            "header-file-mismatch",
            "census file %r != transcript file %r" % (census["file"], tr.file),
        )

    mentions = census.get("mentions")
    if not isinstance(mentions, list):
        err(
            "mentions-not-list",
            "'mentions' is %s, not a list" % type(mentions).__name__,
        )
        mentions = []

    concepts_present = {
        m.get("concept")
        for m in mentions
        if isinstance(m, dict) and isinstance(m.get("concept"), str)
    }

    topics = census.get("main_topics")
    if not isinstance(topics, list):
        err(
            "main-topics-not-list",
            "'main_topics' is %s, not a list" % type(topics).__name__,
        )
    else:
        if not 2 <= len(topics) <= 3:
            err(
                "main-topics-count",
                "main_topics has %d entries, spec requires 2-3" % len(topics),
            )
        for t in topics:
            if not isinstance(t, str):
                err("main-topics-not-string", "main_topics entry %r is not a string" % (t,))
            elif t not in concepts_present:
                err(
                    "main-topic-not-a-mention",
                    "main_topic %r does not appear as any mention's concept" % t,
                )

    # ---- per mention ------------------------------------------------------
    seen_pairs: Dict[Tuple[Any, Any], int] = {}
    npara = len(tr.paragraphs)

    for mi, m in enumerate(mentions):
        if not isinstance(m, dict):
            err("mention-not-object", "mention is %s" % type(m).__name__, mi)
            continue

        for key in REQUIRED_MENTION_KEYS:
            if key not in m:
                err("mention-missing-key", "missing required key %r" % key, mi)

        concept = m.get("concept")
        if not isinstance(concept, str) or not CONCEPT_RE.match(concept):
            err(
                "concept-format",
                "concept %r is not lowercase ASCII hyphen-separated" % (concept,),
                mi,
            )

        mtype = m.get("type")
        if mtype not in VALID_TYPES:
            err("type-enum", "type %r is not one of the 16 valid types" % (mtype,), mi)

        depth = m.get("depth")
        if depth not in VALID_DEPTHS:
            hint = ""
            if isinstance(depth, str) and depth.rstrip("s") + "s" == depth:
                singular = depth[:-1]
                if singular in VALID_DEPTHS:
                    hint = " (looks like a pluralised %r)" % singular
            err(
                "depth-enum",
                "depth %r is not one of explains/opinion/mention%s" % (depth, hint),
                mi,
            )

        if "asr_suspect" in m and m["asr_suspect"] is not True:
            err(
                "asr-suspect-value",
                "asr_suspect is %r; it must be omitted unless exactly true"
                % (m["asr_suspect"],),
                mi,
            )

        snippet = m.get("context_snippet")
        snippet_ok = isinstance(snippet, str) and len(snippet) > 0
        if not snippet_ok:
            err("snippet-empty", "context_snippet is empty or not a string", mi)
        elif len(snippet) > MAX_SNIPPET_LEN:
            err(
                "snippet-too-long",
                "context_snippet is %d chars, max %d" % (len(snippet), MAX_SNIPPET_LEN),
                mi,
            )

        pidx = m.get("paragraph_index")
        pidx_ok = isinstance(pidx, int) and not isinstance(pidx, bool) and 0 <= pidx < npara
        if not pidx_ok:
            err(
                "paragraph-index-range",
                "paragraph_index %r is not an int in [0, %d)" % (pidx, npara),
                mi,
            )

        cs = m.get("char_start")
        offset_ok = snippet_ok and _offset_ok(tr.body, cs, snippet)
        if not offset_ok:
            if not isinstance(cs, int) or isinstance(cs, bool):
                err("char-start-type", "char_start %r is not an int" % (cs,), mi)
            else:
                found = tr.body.find(snippet) if snippet_ok else -1
                err(
                    "offset-mismatch",
                    "body[%d:%d] != context_snippet%s"
                    % (
                        cs,
                        cs + (len(snippet) if snippet_ok else 0),
                        "" if found < 0 else " (snippet does occur at %d)" % found,
                    ),
                    mi,
                )

        if pidx_ok and offset_ok:
            p = tr.paragraphs[pidx]
            if not p.contains_span(cs, len(snippet)):
                err(
                    "containment",
                    "span [%d,%d) is outside paragraph %d [%d,%d)"
                    % (cs, cs + len(snippet), pidx, p.start, p.end),
                    mi,
                )

        if pidx_ok:
            expected_speaker = tr.paragraphs[pidx].speaker
            if m.get("speaker") != expected_speaker:
                err(
                    "speaker-mismatch",
                    "speaker %r != paragraph %d label %r"
                    % (m.get("speaker"), pidx, expected_speaker),
                    mi,
                )

        pair = (concept, pidx)
        if pair in seen_pairs:
            err(
                "duplicate-concept-paragraph",
                "concept %r already emitted for paragraph %r at mention %d"
                % (concept, pidx, seen_pairs[pair]),
                mi,
            )
        else:
            seen_pairs[pair] = mi

    return issues


# --------------------------------------------------------------------------
# Repair
# --------------------------------------------------------------------------

STRATEGY_OK = "already-valid"
STRATEGY_IN_PARAGRAPH = "exact-in-stated-paragraph"
STRATEGY_SAME_SPEAKER = "exact-in-same-speaker-paragraph"
STRATEGY_GLOBAL_UNIQUE = "exact-globally-unique"
STRATEGY_WHITESPACE = "whitespace-tolerant-unique"
STRATEGY_UNRESOLVED = "unresolvable"


def _find_in_span(body: str, snippet: str, start: int, end: int) -> int:
    """First exact occurrence of `snippet` fully inside [start, end), else -1."""
    pos = body.find(snippet, start, end)
    if pos == -1:
        return -1
    if pos + len(snippet) > end:
        return -1
    return pos


def _all_occurrences(body: str, snippet: str, limit: int = 3) -> List[int]:
    out: List[int] = []
    pos = body.find(snippet)
    while pos != -1 and len(out) < limit:
        out.append(pos)
        pos = body.find(snippet, pos + 1)
    return out


def _whitespace_tolerant_matches(
    body: str, snippet: str, limit: int = 3
) -> List[Tuple[int, int]]:
    """Spans matching `snippet` with each whitespace run relaxed to \\s+."""
    parts = re.split(r"\s+", snippet.strip())
    parts = [p for p in parts if p]
    if not parts:
        return []
    pattern = r"\s+".join(re.escape(p) for p in parts)
    try:
        rx = re.compile(pattern)
    except re.error:
        return []
    spans: List[Tuple[int, int]] = []
    for m in rx.finditer(body):
        spans.append((m.start(), m.end()))
        if len(spans) >= limit:
            break
    return spans


def repair(
    census: Dict[str, Any], tr: Transcript
) -> Tuple[Dict[str, Any], List[RepairAction]]:
    """Return (deep-copied repaired census, actions taken).

    For each mention whose `char_start` fails the offset check, the following
    strategies are tried in order:

    1. `exact-in-stated-paragraph` — exact snippet occurrence inside the span of
       the paragraph named by `paragraph_index` (first, if several).
    2. `exact-in-same-speaker-paragraph` — exact occurrence in any paragraph
       whose speaker matches the mention's, nearest by paragraph index.
    3. `exact-globally-unique` — exactly one occurrence in the body.
    4. `whitespace-tolerant-unique` — a unique match with whitespace runs
       relaxed; `context_snippet` is replaced with the true verbatim text.
    5. `unresolvable` — the mention is left exactly as it was.

    When a repair lands the mention in a different paragraph, `paragraph_index`
    and `speaker` are resynced to that paragraph. No snippet is ever invented.
    The operation is idempotent.
    """
    out = copy.deepcopy(census)
    actions: List[RepairAction] = []

    mentions = out.get("mentions")
    if not isinstance(mentions, list):
        return out, actions

    body = tr.body
    npara = len(tr.paragraphs)

    for mi, m in enumerate(mentions):
        if not isinstance(m, dict):
            continue
        snippet = m.get("context_snippet")
        if not isinstance(snippet, str) or not snippet:
            actions.append(
                RepairAction(mi, STRATEGY_UNRESOLVED, "no usable context_snippet")
            )
            continue

        cs = m.get("char_start")
        pidx = m.get("paragraph_index")
        pidx_ok = isinstance(pidx, int) and not isinstance(pidx, bool) and 0 <= pidx < npara

        if _offset_ok(body, cs, snippet):
            # Already anchored. Still resync the paragraph/speaker if the
            # offset says the mention lives elsewhere -- keeps repair a fixed
            # point and keeps containment/speaker consistent.
            _resync(m, tr, cs, len(snippet), actions, mi, moved_only=True)
            continue

        new_start = -1
        new_snippet = snippet
        strategy = STRATEGY_UNRESOLVED
        detail = ""

        # 1. inside the stated paragraph
        if pidx_ok:
            p = tr.paragraphs[pidx]
            pos = _find_in_span(body, snippet, p.start, p.end)
            if pos != -1:
                new_start, strategy = pos, STRATEGY_IN_PARAGRAPH
                detail = "found in stated paragraph %d" % pidx

        # 2. nearest paragraph with the same speaker
        if new_start == -1:
            speaker = m.get("speaker")
            if isinstance(speaker, str):
                anchor = pidx if pidx_ok else 0
                cands = [p for p in tr.paragraphs if p.speaker == speaker]
                cands.sort(key=lambda p: (abs(p.index - anchor), p.index))
                for p in cands:
                    pos = _find_in_span(body, snippet, p.start, p.end)
                    if pos != -1:
                        new_start, strategy = pos, STRATEGY_SAME_SPEAKER
                        detail = "found in paragraph %d with matching speaker %r" % (
                            p.index,
                            speaker,
                        )
                        break

        # 3. globally unique exact occurrence
        if new_start == -1:
            occ = _all_occurrences(body, snippet, limit=2)
            if len(occ) == 1:
                new_start, strategy = occ[0], STRATEGY_GLOBAL_UNIQUE
                detail = "unique exact occurrence in body at %d" % occ[0]

        # 4. whitespace-tolerant unique match
        if new_start == -1:
            spans = _whitespace_tolerant_matches(body, snippet, limit=2)
            if len(spans) == 1:
                s, e = spans[0]
                if e - s <= MAX_SNIPPET_LEN:
                    new_start, strategy = s, STRATEGY_WHITESPACE
                    new_snippet = body[s:e]
                    detail = "unique whitespace-tolerant match at %d; snippet rewritten" % s
                else:
                    detail = (
                        "whitespace-tolerant match at %d spans %d chars (>%d); rejected"
                        % (s, e - s, MAX_SNIPPET_LEN)
                    )

        if new_start == -1:
            actions.append(
                RepairAction(
                    mi,
                    STRATEGY_UNRESOLVED,
                    detail or "snippet not found in body by any strategy",
                    cs,
                    cs,
                )
            )
            continue

        m["char_start"] = new_start
        if new_snippet != snippet:
            m["context_snippet"] = new_snippet
        actions.append(RepairAction(mi, strategy, detail, cs, new_start))
        _resync(m, tr, new_start, len(new_snippet), actions, mi, moved_only=False)

    return out, actions


def _resync(
    m: Dict[str, Any],
    tr: Transcript,
    start: int,
    length: int,
    actions: List[RepairAction],
    mi: int,
    moved_only: bool,
) -> None:
    """Point paragraph_index/speaker at the paragraph actually containing the span."""
    p = tr.paragraph_at(start)
    if p is None:
        return
    # If the span straddles a paragraph boundary the containing paragraph of
    # its start is still the best locator available, so use it either way.
    changed = []
    if m.get("paragraph_index") != p.index:
        changed.append("paragraph_index %r -> %d" % (m.get("paragraph_index"), p.index))
        m["paragraph_index"] = p.index
    if m.get("speaker") != p.speaker:
        changed.append("speaker %r -> %r" % (m.get("speaker"), p.speaker))
        m["speaker"] = p.speaker
    if changed:
        actions.append(
            RepairAction(mi, "resync-paragraph", "; ".join(changed), start, start)
        )


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------


def report(census: Dict[str, Any], tr: Transcript) -> Dict[str, Any]:
    """Summary statistics for one census, with spec-band flags."""
    mentions = census.get("mentions")
    if not isinstance(mentions, list):
        mentions = []
    mentions = [m for m in mentions if isinstance(m, dict)]
    n = len(mentions)
    npara = len(tr.paragraphs)

    covered = set()
    max_pidx = None
    depth_counts: Dict[str, int] = {}
    type_counts: Dict[str, int] = {}
    speaker_counts: Dict[str, int] = {}
    concepts = set()
    asr_suspect = 0
    offset_valid = 0

    for m in mentions:
        pidx = m.get("paragraph_index")
        if isinstance(pidx, int) and not isinstance(pidx, bool):
            if 0 <= pidx < npara:
                covered.add(pidx)
            max_pidx = pidx if max_pidx is None else max(max_pidx, pidx)
        depth_counts[str(m.get("depth"))] = depth_counts.get(str(m.get("depth")), 0) + 1
        type_counts[str(m.get("type"))] = type_counts.get(str(m.get("type")), 0) + 1
        speaker_counts[str(m.get("speaker"))] = speaker_counts.get(str(m.get("speaker")), 0) + 1
        c = m.get("concept")
        if isinstance(c, str):
            concepts.add(c)
        if m.get("asr_suspect") is True:
            asr_suspect += 1
        if _offset_ok(tr.body, m.get("char_start"), m.get("context_snippet")):
            offset_valid += 1

    depth_shares = {k: (v / n if n else 0.0) for k, v in depth_counts.items()}
    explains_share = depth_shares.get("explains", 0.0)

    issues = validate(census, tr)
    errors_by_code: Dict[str, int] = {}
    warns_by_code: Dict[str, int] = {}
    for i in issues:
        bucket = errors_by_code if i.severity == "error" else warns_by_code
        bucket[i.code] = bucket.get(i.code, 0) + 1

    return {
        "file": tr.file,
        "episode": tr.episode,
        "mentions": n,
        "mention_band": list(MENTION_BAND),
        "mentions_in_band": MENTION_BAND[0] <= n <= MENTION_BAND[1],
        "offset_valid": offset_valid,
        "offset_valid_fraction": (offset_valid / n) if n else 0.0,
        "paragraphs_total": npara,
        "paragraphs_covered": len(covered),
        "coverage_fraction": (len(covered) / npara) if npara else 0.0,
        "max_paragraph_index": max_pidx,
        "max_paragraph_index_fraction": (
            (max_pidx + 1) / npara if (npara and max_pidx is not None) else 0.0
        ),
        "depth_histogram": depth_counts,
        "depth_shares": depth_shares,
        "explains_share": explains_share,
        "explains_band": list(EXPLAINS_BAND),
        "explains_in_band": EXPLAINS_BAND[0] <= explains_share <= EXPLAINS_BAND[1],
        "type_histogram": type_counts,
        "speaker_histogram": speaker_counts,
        "distinct_concepts": len(concepts),
        "asr_suspect_count": asr_suspect,
        "errors_by_code": errors_by_code,
        "warnings_by_code": warns_by_code,
        "error_count": sum(errors_by_code.values()),
    }
