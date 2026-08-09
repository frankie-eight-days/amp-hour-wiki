#!/usr/bin/env python3
"""Write one wiki article from an extraction packet, via Kimi k3.

Generalises scratchpad/kimi_write_v4.py: any concept, any packet, spec text
either the locked default below or a file supplied by the caller.

  python3 kimi_write.py --packet articles/factory/packets/altium-v4.json \
                        --out articles/factory/articles/altium.md

Optional:
  --further PATH   further-reading JSON ([{title,url,episode}, ...]); defaults to
                   <packet-dir>/<concept>.further_reading.json when present
  --spec-file PATH override the locked spec; {title} {concept} {date} {model}
                   {spec_id} are substituted
  --title / --concept   override what the packet declares
  --model k3       Kimi model
  --max-tokens     default 32000
  --dry-run        build the prompt, write it next to --out, do not call the API

The packet must be {"concept": ..., "claims": [{claim_text, quote_verbatim,
speaker, episode, episode_title, episode_url, depth_regraded, kind}, ...]};
extra keys are ignored. Episode titles, URLs and dates are resolved from
census/union and the transcript show-opens and handed to the model so it cannot
invent them.
"""
import argparse, datetime, json, os, re, sys, time, urllib.error, urllib.request

ROOT = "/Users/frankwalsh/Documents/vibecoding/amp_hour_wiki"
SCRATCH = ("/private/tmp/claude-501/-Users-frankwalsh-Documents-vibecoding-amp-hour-wiki/"
           "2439d3fc-e7b7-42c1-90da-27b1ddd5fa6c/scratchpad")
KEY_PATH = os.environ.get("KIMI_KEY_PATH", os.path.join(SCRATCH, "kimi_key"))
URL = "https://api.kimi.com/coding/v1/messages"
SPEC_ID = "knowledge-only-v4-cluster"

SPEC = """You are writing an encyclopedia article for a technical reference wiki. Write it the way a Wikipedia article on the subject would be written.

The subject is: {title}

REGISTER AND VOICE
- Encyclopedic, neutral, third person. State claims as knowledge, not as things someone said.
- Every factual sentence carries a bracketed episode citation drawn from the source packet, e.g. "The tool emits inner planes as negative images.[434]" Stack citations when several claims support one statement: "...[400][404]".
- Use named attribution ONLY where the identity of the practitioner is itself the content: a personal practice anchored to a specific project or role. Write those with their anchoring context, e.g. "On the Steam Controller programme, Keyzer's team froze the CAD version for the duration.[523]" Do not attribute ordinary technical facts to whoever happened to say them.
- ZERO meta commentary. Never mention a podcast, an archive, episodes-as-episodes, hosts, this article, this page, the reader, coverage, or discussion. The bracketed numbers are the only trace of provenance. Never write "the archive", "the show", "this article", "the hosts", "the takeaway".
- NEVER write a Reception section, and never write reception or adoption material anywhere in the article: no sentences about how a product was received, who came around to it, who dismissed it, what users felt, whether opinion was divided, or how popular something became. Market-structure facts (segment shares, which segment a tool holds) are permitted as facts; sentiment about them is not.
- Direct quotation is rare. Quote only when the exact phrasing is itself the artifact. Any quoted string must appear VERBATIM inside a quote_verbatim field of the packet. Otherwise paraphrase.

STRUCTURE
- Open with a Wikipedia-style lead: 2-4 cited sentences summarising what the subject is and why it matters. No heading on the lead. The lead must be neutral and fully cited.
- Then ## sections, created only where the packet has the material to fill them. Let the material dictate the sections; do not force a template. ### subsections are allowed where a section has genuine internal structure.
- Then "## Further reading", a bullet list built ONLY from the FURTHER READING list supplied below, formatted "- [title](url) — via #episode". Omit the section entirely if that list is empty.
- End with "## References": a markdown table with columns Episode | Title | URL | Date, one row per episode cited anywhere in the article, ordered by episode number. Use the EPISODE METADATA table supplied below for titles, URLs and dates; leave the Date cell empty where the metadata gives no date. Never invent a date.
- Output markdown with YAML frontmatter at the very top:
---
title: {title}
concept: {concept}
generated: {date}
model: {model}
spec: {spec_id}
---

SOURCING RULES (strict)
- The packet JSON below is the ONLY permitted source material. Every claim in the article must trace to a specific packet claim and must cite that claim's episode number.
- Do not import outside knowledge about the subject, even if you know it. Do not invent facts, dates, names, numbers or URLs.
- Only cite episode numbers that appear in the packet.
- Every episode cited in the article must appear in the References table, and every row of the References table must be cited in the article.

LENGTH
- Use the material. The packet is dense; a thorough article is expected. Do not pad, and do not drop substantive claims to hit a length.

Output the article and nothing else. No preamble, no explanation, no code fences around the whole document."""

DATE_RE = re.compile(
    r"(?:recorded|release[d]?)[:\s]+"
    r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+(\d{1,2})\w*,?\s+(\d{4})", re.I)

_census = None


def census_index():
    global _census
    if _census is None:
        _census = {}
        cdir = os.path.join(ROOT, "census/union")
        for fn in os.listdir(cdir):
            if fn.startswith("_") or not fn.endswith(".json"):
                continue
            d = json.load(open(os.path.join(cdir, fn)))
            if d.get("episode"):
                _census[d["episode"]] = (d.get("title"), d.get("url"), fn[:-5])
    return _census


def episode_meta(episodes, claims):
    """Episode | title | url | date rows; packet values win, census fills gaps."""
    cen = census_index()
    from_packet = {}
    for c in claims:
        if c.get("episode_title") or c.get("episode_url"):
            from_packet.setdefault(c["episode"],
                                   (c.get("episode_title"), c.get("episode_url")))
    rows = []
    for e in sorted(episodes):
        ctitle, curl, stem = cen.get(e, (None, None, None))
        ptitle, purl = from_packet.get(e, (None, None))
        date = ""
        if stem:
            path = os.path.join(ROOT, "transcripts", stem + ".md")
            if os.path.exists(path):
                m = DATE_RE.search(open(path, encoding="utf-8").read()[:2500])
                if m:
                    date = f"{m.group(1).capitalize()} {int(m.group(2))}, {m.group(3)}"
        rows.append({"episode": e, "title": ptitle or ctitle,
                     "url": purl or curl, "date": date})
    return rows


def call_kimi(prompt, model="k3", max_tokens=32000, timeout=1800, retries=2):
    """Returns (response, elapsed_seconds, attempts). Elapsed spans every
    attempt, so a retried call reports the wall time the run actually spent."""
    key = open(KEY_PATH).read().strip()
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    last = None
    t0 = time.monotonic()
    for attempt in range(retries + 1):
        req = urllib.request.Request(URL, data=body, headers={
            "content-type": "application/json", "x-api-key": key,
            "anthropic-version": "2023-06-01"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                resp = json.loads(r.read())
            return resp, round(time.monotonic() - t0, 3), attempt + 1
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            print(f"  kimi call failed ({exc}); attempt {attempt + 1}", file=sys.stderr)
    raise SystemExit(f"kimi call failed after {retries + 1} attempts "
                     f"in {time.monotonic() - t0:.1f}s: {last}")


def build_prompt(packet, further, spec_text, title, concept, model):
    claims = packet["claims"]
    eps = {c["episode"] for c in claims}
    rows = episode_meta(eps, claims)
    further = [f for f in (further or []) if f.get("episode") in eps]
    spec = spec_text.format(title=title, concept=concept, model=model,
                            date=datetime.date.today().isoformat(), spec_id=SPEC_ID)
    return (spec
            + "\n\nEPISODE METADATA (episode | title | url | date):\n"
            + json.dumps(rows, indent=1)
            + "\n\nFURTHER READING:\n" + json.dumps(further, indent=1)
            + "\n\nSOURCE PACKET (JSON) - claims are the sole source:\n"
            + json.dumps({"concept": concept, "claims": claims}, indent=1)), len(eps), len(further)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--packet", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--further")
    ap.add_argument("--spec-file")
    ap.add_argument("--title")
    ap.add_argument("--concept")
    ap.add_argument("--model", default="k3")
    ap.add_argument("--max-tokens", type=int, default=32000)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-timing", action="store_true",
                    help="skip the _timing.jsonl append")
    a = ap.parse_args()

    packet = json.load(open(a.packet))
    concept = a.concept or packet["concept"]
    title = a.title or packet.get("name") or concept.replace("-", " ").title()

    further_path = a.further
    if not further_path:
        guess = os.path.join(os.path.dirname(a.packet),
                             concept + ".further_reading.json")
        further_path = guess if os.path.exists(guess) else None
    further = json.load(open(further_path)) if further_path else []

    spec_text = open(a.spec_file).read() if a.spec_file else SPEC
    prompt, n_eps, n_fr = build_prompt(packet, further, spec_text, title,
                                       concept, a.model)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out + ".prompt.txt", "w").write(prompt)
    if a.dry_run:
        print(json.dumps({"concept": concept, "claims": len(packet["claims"]),
                          "episodes": n_eps, "further_reading": n_fr,
                          "prompt_chars": len(prompt), "dry_run": True}, indent=1))
        return

    ts_start = datetime.datetime.now().astimezone().isoformat()
    resp, t_kimi_s, attempts = call_kimi(prompt, model=a.model,
                                         max_tokens=a.max_tokens)
    txt = "".join(b.get("text", "") for b in resp.get("content", [])
                  if b.get("type") == "text").strip()
    if not txt:
        raise SystemExit(f"empty response from kimi: {json.dumps(resp)[:500]}")
    open(a.out, "w").write(txt + "\n")
    words = len(txt.split())
    usage = resp.get("usage", {})
    json.dump({"usage": usage, "t_kimi_s": t_kimi_s, "attempts": attempts,
               "model": a.model, "ts_start": ts_start,
               "prompt_chars": len(prompt), "words_out": words},
              open(a.out + ".usage.json", "w"), indent=1)

    if not a.no_timing:
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from timing import append_timing
            append_timing(concept, {"t_kimi_s": t_kimi_s, "article_words": words,
                                    "ts_start": ts_start})
        except Exception as exc:                # timing must never fail a write
            print(f"  timing not recorded: {exc}", file=sys.stderr)

    print(json.dumps({"concept": concept, "out": a.out,
                      "claims": len(packet["claims"]), "episodes": n_eps,
                      "further_reading": n_fr, "prompt_chars": len(prompt),
                      "words_out": words, "t_kimi_s": t_kimi_s,
                      "attempts": attempts, "usage": usage}, indent=1))


if __name__ == "__main__":
    main()
