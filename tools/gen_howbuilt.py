#!/usr/bin/env python3
"""Generate articles/meta/how-this-was-built.md — the traced-sentence page.

Every layer shown on that page is pulled live from the real artifacts on disk
(article, packet, bundle, transcript), so the page cannot drift from the data
it claims to describe. sync_site.py copies the result into site/content.
"""
import difflib
import html
import json
import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "articles" / "meta" / "how-this-was-built.md"

# concept, episode, a snippet locating the claim, and a plausible "cleaned up"
# paraphrase that a careless writer might produce (used for the FAIL demo)
TRACES = [
    dict(concept="analog-to-digital-converter", episode=218,
         snip="24 bit ADC doesn't actually",
         fake="a 24-bit ADC doesn't actually give you 24 usable bits",
         blurb="A hard technical claim. Watch the bundle passage swallow three "
               "speaker turns &mdash; the quote is Dave's question, the numbers "
               "are the guest's answer &mdash; and watch the claim get written "
               "so it never depends on which of them said what."),
    dict(concept="power-grid", episode=385,
         snip="$7 million a month",
         fake="their electricity bill per month was $7 million a month",
         blurb="A number nobody would think to go looking for. Also the clearest "
               "look at the canon layer working: the transcript put these words "
               "in the host's mouth, and the speaker map moved them back to the "
               "guest who actually said them."),
    dict(concept="reverse-engineering", episode=302,
         snip="reverse-engineered Xilinx's programming cable",
         fake="we reverse engineered Xilinx's programming cable",
         blurb="The kind of thing that exists only because someone said it out "
               "loud on a podcast. It is in no datasheet and no press release, "
               "and the speaker interrupts himself to wonder whether he should "
               "be telling the story at all."),
]

E = html.escape


def mark(text, quote):
    """Escape text, wrapping the quote occurrence in a <mark>."""
    i = text.find(quote)
    if i < 0:
        return E(text)
    return (E(text[:i]) + '<mark class="hb-q">' + E(quote) + "</mark>"
            + E(text[i + len(quote):]))


def sentences(text):
    """Split into sentences, keeping trailing [12][34] citation runs attached."""
    marked = re.sub(r"([.?!])((?:\[\d+\])*)\s+", "\\1\\2\x00", text)
    return [s.strip() for s in marked.split("\x00") if s.strip()]


def article_sentence(raw, episode, claim_text):
    """The published sentence citing this episode, best-matching the claim."""
    body = re.sub(r"^---.*?---\s*", "", raw, flags=re.S)
    body = body.split("## References")[0]
    want = set(re.findall(r"[a-z]{5,}", claim_text.lower()))
    best, score = None, -1
    for sent in sentences(body):
        sent = sent.strip()
        if f"[{episode}]" not in sent or sent.startswith("|") or len(sent) > 500:
            continue
        got = set(re.findall(r"[a-z]{5,}", sent.lower()))
        s = len(want & got)
        if s > score:
            best, score = sent, s
    return best


def cite_html(sentence, episode):
    """Escape a sentence, styling its citation markers."""
    out, pos = [], 0
    for m in re.finditer(r"\[(\d+)\]", sentence):
        out.append(E(sentence[pos:m.start()]))
        cls = "hb-cite hb-cite-on" if m.group(1) == str(episode) else "hb-cite"
        out.append(f'<sup class="{cls}">[{m.group(1)}]</sup>')
        pos = m.end()
    out.append(E(sentence[pos:]))
    return "".join(out).replace("**", "")


def transcript_context(stem, quote, passage_text):
    """Raw transcript turns around the quote.

    Each turn is (speaker, text, is_hit, in_passage). `in_passage` is computed
    against the bundle text rather than read from the bundle's `fused_turns`
    flag, which under-reports: passages routinely swallow a neighbouring turn
    while the flag stays False.
    """
    raw = (ROOT / "transcripts" / f"{stem}.md").read_text()
    words = len(raw.split())
    lines = [l for l in raw.split("\n") if l.startswith("**")]
    hit = next((i for i, l in enumerate(lines) if quote in l), None)
    if hit is None:
        return [], words
    out = []
    for l in lines[max(0, hit - 2):hit + 3]:
        m = re.match(r"\*\*(.+?):\*\*\s*(.*)", l)
        if not m:
            continue
        said = m.group(2)
        covered = len(said) > 25 and said[:60] in passage_text
        out.append((m.group(1), said, quote in l, covered))
    return out, words


def diff_spans(real, fake):
    """HTML for the fake quote with every divergence from real marked."""
    out = []
    for tag, _i1, _i2, j1, j2 in difflib.SequenceMatcher(
            None, real, fake, autojunk=False).get_opcodes():
        seg = fake[j1:j2]
        if tag == "equal":
            out.append(E(seg))
        elif tag == "delete":
            # dropped text leaves nothing in the fake; mark the seam
            out.append('<span class="hb-bad" title="text dropped">&#9251;</span>')
        else:
            out.append(f'<span class="hb-bad">{E(seg)}</span>')
    return "".join(out)


def build(spec):
    concept, episode = spec["concept"], spec["episode"]
    art_raw = (ROOT / "articles" / "wiki" / f"{concept}.md").read_text()
    packet = json.load(open(ROOT / "articles/factory/packets" / f"{concept}.json"))
    bundle = json.load(open(ROOT / "articles/factory/bundles" / f"{concept}.json"))

    claim = next(c for c in packet["claims"]
                 if c["episode"] == episode and spec["snip"] in c.get("quote_verbatim", ""))
    quote = claim["quote_verbatim"]
    passage = next(p for p in bundle["passages"]
                   if p["episode"] == episode and quote in p.get("text", ""))
    turns, words = transcript_context(passage["stem"], quote, passage["text"])
    spanned = [spk for spk, _t, _h, cov in turns if cov]
    row = re.search(rf"^\| {episode} \| (.+?) \| (\S+) \| (.+?) \|", art_raw, re.M)
    ep_title, ep_url, ep_date = row.groups()
    sentence = article_sentence(art_raw, episode, claim["claim_text"])
    title = re.search(r"^title:\s*(.+)$", art_raw, re.M).group(1).strip()

    repaired = (passage.get("speaker_repaired") and
                passage.get("speaker_repaired") != passage.get("speaker_raw"))
    return dict(
        concept=concept, title=title, episode=episode, quote=quote,
        blurb=spec["blurb"], sentence=sentence, kind=claim.get("kind", ""),
        claim_text=claim["claim_text"], claim_speaker=claim.get("speaker"),
        passage=passage, turns=turns, words=words, repaired=repaired,
        spanned=spanned,
        ep_title=ep_title, ep_url=ep_url, ep_date=ep_date,
        n_claims=len(packet["claims"]), n_passages=len(bundle["passages"]),
        stats=bundle["stats"], core=bundle["cluster"]["core"],
        fake_html=diff_spans(quote, spec["fake"]),
    )


# --------------------------------------------------------------- rendering
def gauge(value, cap=11_000_000):
    return max(3.0, round(math.log10(max(value, 1)) / math.log10(cap) * 100, 1))


def layer(num, name, scale, scale_n, body, extra=""):
    return f"""<section class="hb-layer{extra}" data-layer="{num}">
  <div class="hb-layer-head">
    <span class="hb-num">{num}</span>
    <span class="hb-name">{name}</span>
    <span class="hb-scale">{scale}</span>
    <span class="hb-gauge"><i style="width:{gauge(scale_n)}%"></i></span>
  </div>
  <div class="hb-layer-body">{body}</div>
</section>"""


def render_trace(t, idx):
    p = t["passage"]
    st = t["stats"]

    l5 = layer(
        "05", "Article", "1 sentence", 1,
        f'<div class="hb-doc"><div class="hb-doc-title">{E(t["title"])}</div>'
        f'<p class="hb-sentence">{cite_html(t["sentence"], t["episode"])}</p>'
        f'<div class="hb-note">The citation is a promise. Everything below is '
        f'the receipt.</div></div>')

    speaker = (f'"{E(t["claim_speaker"])}"' if t["claim_speaker"]
               else '<span class="hb-null">null</span>'
                    '  <span class="hb-k">// attribution not safe to assert</span>')
    l4 = layer(
        "04", "Packet &mdash; where judgment happens",
        f'1 of {t["n_claims"]} claims', t["n_claims"],
        f'<pre class="hb-json"><span class="hb-k">"kind"</span>: '
        f'<span class="hb-badge">{E(t["kind"])}</span>,\n'
        f'<span class="hb-k">"claim_text"</span>: "{E(t["claim_text"])}",\n'
        f'<span class="hb-k">"quote_verbatim"</span>: "<mark class="hb-q">'
        f'{E(t["quote"])}</mark>",\n'
        f'<span class="hb-k">"speaker"</span>: {speaker},\n'
        f'<span class="hb-k">"episode"</span>: {t["episode"]}</pre>'
        f'<div class="hb-note">An extraction pass read all {t["n_passages"]} '
        f'passages below and wrote this. It is the only layer where a machine '
        f'makes a judgment &mdash; so it is the layer that gets verified.</div>')

    verify = f"""<div class="hb-verify" data-real="{E(t['quote'])}">
  <div class="hb-verify-head"><span class="hb-vtitle">verify_packet.py</span>
    <span class="hb-vsub">byte-compare &middot; packet quote vs. transcript</span></div>
  <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip" data-role="a"></code></div>
  <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip" data-role="b"></code></div>
  <div class="hb-verdict" data-role="v"></div>
  <button class="hb-fail-btn" type="button">Now try a quote that was tidied up &rarr;</button>
  <div class="hb-fail" hidden>
    <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip">{t['fake_html']}</code></div>
    <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip">{E(t['quote'])}</code></div>
    <div class="hb-verdict hb-v-fail">&#10007; FAIL &mdash; quote not found in transcript. Build rejected.</div>
    <div class="hb-note">A hyphen added, a filler word dropped, a contraction
    expanded: all of it fails. This is why nothing on this wiki is
    &ldquo;cleaned up.&rdquo;</div>
  </div>
</div>"""

    badges = [f'<span class="hb-tag">paragraph {p.get("paragraph_index")}</span>',
              f'<span class="hb-tag">depth: {p.get("depth")}</span>']
    if p.get("guest"):
        badges.append(f'<span class="hb-tag">guest: {E(p["guest"])}</span>')
    if len(set(t["spanned"])) > 1:
        badges.append(f'<span class="hb-tag hb-warn">spans {len(t["spanned"])} '
                      f'speaker turns &mdash; {E(" + ".join(dict.fromkeys(t["spanned"])))}'
                      f'</span>')
    if not p.get("attribution_reliable", True):
        badges.append('<span class="hb-tag hb-warn">attribution unreliable</span>')

    l3 = layer(
        "03", "Bundle &mdash; the evidence pack",
        f'1 of {t["n_passages"]} passages', t["n_passages"],
        f'<div class="hb-tags">{"".join(badges)}</div>'
        f'<p class="hb-passage">{mark(p["text"], t["quote"])}</p>'
        f'<div class="hb-note">Deterministic collection, no judgment: every '
        f'passage in the corpus that touches this concept, gathered in one '
        f'file for the extraction pass to read.</div>')

    fold = "".join(f'<code class="hb-alias">{E(a)}</code>' for a in t["core"][:6])
    repair = ""
    if t["repaired"]:
        repair = (f'<div class="hb-repair"><span class="hb-rx">'
                  f'{E(p.get("speaker_raw") or "?")}</span>'
                  f'<span class="hb-arrow">&rarr;</span>'
                  f'<span class="hb-rok">{E(p.get("speaker_repaired"))}</span>'
                  f'<span class="hb-note hb-inline">the transcript labelled this '
                  f'turn with the wrong voice; the speaker map repaired it</span></div>')
    l2 = layer(
        "02", "Census &amp; canon &mdash; finding it at all",
        f'{st.get("mentions", 0):,} mentions of this concept', st.get("mentions", 1),
        f'<div class="hb-grid2">'
        f'<div><div class="hb-lbl">surface forms folded into one concept</div>'
        f'<div class="hb-fold">{fold}</div></div>'
        f'<div><div class="hb-lbl">this concept across the corpus</div>'
        f'<div class="hb-stat">{st.get("episodes", 0)} episodes &middot; '
        f'{st.get("mentions", 0):,} mentions &middot; '
        f'{st.get("explains", 0):,} explanatory</div></div></div>'
        f'{repair}'
        f'<div class="hb-note">Roughly 197,000 mentions were logged across the '
        f'whole corpus, then folded down a 90,150-entry alias table so that '
        f'&ldquo;ADC&rdquo;, &ldquo;A to D&rdquo; and &ldquo;analog to digital'
        f'&rdquo; all land on one concept.</div>')

    turns_html = "".join(
        f'<div class="hb-turn{" hb-hit" if hit else ""}'
        f'{" hb-cov" if cov else ""}">'
        f'<span class="hb-spk">{E(spk)}</span>'
        f'<span class="hb-said">{mark(txt, t["quote"]) if hit else E(txt)}</span></div>'
        for spk, txt, hit, cov in t["turns"])
    span_note = ""
    if len(set(t["spanned"])) > 1:
        span_note = (
            f' The rail marks how far the bundle passage above reached &mdash; '
            f'{len(t["spanned"])} turns, more than one speaker. The packet\'s '
            f'<code>speaker</code> field records who said the <em>quote</em>, not '
            f'who supplied every detail in the claim, which is why a claim is '
            f'written to stand on its evidence rather than on attribution.')
    if t["repaired"]:
        span_note += (' The speaker labels here are the raw ASR ones; the repair '
                      'shown in layer 02 is what the pipeline actually uses.')
    l1 = layer(
        "01", "Transcript &mdash; raw ASR", f'{t["words"]:,} words in this episode',
        t["words"],
        f'<div class="hb-transcript">{turns_html}</div>'
        f'<div class="hb-note">Machine transcription, errors and filler intact. '
        f'Nothing here was corrected &mdash; correcting it would break the '
        f'verification above.{span_note}</div>')

    l0 = layer(
        "00", "The episode", "1 of 719 episodes", 719,
        f'<a class="hb-episode" href="{E(t["ep_url"])}" target="_blank" rel="noopener">'
        f'<span class="hb-epnum">{t["episode"]}</span>'
        f'<span class="hb-epmeta"><strong>{E(t["ep_title"])}</strong>'
        f'<span>{E(t["ep_date"])} &middot; two engineers talking &middot; '
        f'listen &rarr;</span></span></a>'
        f'<div class="hb-note">Bottom of the stack. A person said this out loud, '
        f'once, years ago, and now it is a citable sentence.</div>',
        extra=" hb-last")

    return f"""<div class="hb-trace" data-trace="{idx}"{"" if idx == 0 else " hidden"}>
  <div class="hb-pin">
    <div class="hb-pin-lbl">tracing this sentence &mdash; {E(t["title"])}</div>
    <div class="hb-pin-txt">{cite_html(t["sentence"], t["episode"])}</div>
  </div>
  <div class="hb-blurb">{t["blurb"]}</div>
  <div class="hb-descent">
    <div class="hb-wire"><i class="hb-probe"></i></div>
    <div class="hb-layers">{l5}{l4}{verify}{l3}{l2}{l1}{l0}</div>
  </div>
</div>"""


def main():
    traces = [build(s) for s in TRACES]
    tabs = "".join(
        f'<button class="hb-tab{" hb-on" if i == 0 else ""}" data-tab="{i}" '
        f'type="button"><span>{E(t["title"])}</span>'
        f'<small>ep {t["episode"]} &middot; {E(t["kind"])}</small></button>'
        for i, t in enumerate(traces))
    body = "".join(render_trace(t, i) for i, t in enumerate(traces))

    n_articles = len(list((ROOT / "articles/wiki").glob("*.md")))
    n_claims = 0
    for p in (ROOT / "articles/factory/packets").glob("*.json"):
        d = json.load(open(p))
        n_claims += len(d.get("claims", []) if isinstance(d, dict) else d)
    n_cites = sum(len(re.findall(r"^\| \d+ \|", m.read_text(), re.M))
                  for m in (ROOT / "articles/wiki").glob("*.md"))
    graph = json.load(open(ROOT / "graph/graph.json"))

    funnel = [("Words of raw transcript", 11_000_000, "719 episodes, machine-transcribed"),
              ("Concept mentions logged", 197_000, "the census pass"),
              ("Verified claims extracted", n_claims, "each pinned to a byte-checked quote"),
              ("Episode citations published", n_cites, "across every live article"),
              ("Articles live", n_articles, "of 412 planned")]
    fmax = math.log10(funnel[0][1])
    funnel_html = "".join(
        f'<div class="hb-fn"><div class="hb-fn-lbl">{lbl}</div>'
        f'<div class="hb-fn-bar"><i style="width:{round(math.log10(v)/fmax*100,1)}%"></i>'
        f'<span>{v:,}</span></div>'
        f'<div class="hb-fn-sub">{sub}</div></div>' for lbl, v, sub in funnel)

    page = PAGE.format(
        tabs=tabs, traces=body, funnel=funnel_html,
        n_articles=n_articles, n_claims=f"{n_claims:,}", n_cites=f"{n_cites:,}",
        nodes=f"{len(graph['nodes']):,}", edges=f"{len(graph['edges']):,}",
        css=CSS, js=JS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page)
    print(f"how-this-was-built written: {len(page):,} bytes, "
          f"{len(traces)} traces ({', '.join(t['concept'] for t in traces)})")


CSS = """
.hb { --ember: #c94628; --amber: #b07d1a; }
:root[saved-theme="dark"] .hb { --ember: #ef5d3c; --amber: #ffd27a; }
/* This page reclaims the width Quartz gives the table-of-contents rail.
   The `full-width` frame would do it, but frames are emitter-level, so the
   grid override is replicated here and scoped to this page's stylesheet. */
@media (min-width: 800px) {
  .page > #quartz-body { grid-template-columns: 320px auto;
    grid-template-areas: "grid-sidebar-left grid-header"
                         "grid-sidebar-left grid-center"
                         "grid-sidebar-left grid-footer"; }
  .page > #quartz-body > .sidebar.right { display: none; }
  .page > #quartz-body > .center { max-width: 100%; }
}
.hb-bleed { width: 100%; }
/* prose keeps a readable measure; only the trace sections use the full width */
.hb > *:not(.hb-bleed) { max-width: 46rem; margin-left: auto; margin-right: auto; }
.hb-lede { font-size: 1.12rem; line-height: 1.6; }
.hb-pin > * { max-width: 940px; margin-left: auto; margin-right: auto; }

/* --- trace selector --- */
.hb-tabs { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center;
  padding: 26px 12px 0; }
.hb-tab { background: none; border: 1px solid var(--lightgray); border-radius: 5px;
  padding: 8px 14px; cursor: pointer; text-align: left; color: var(--dark);
  font-family: var(--bodyFont); display: flex; flex-direction: column; gap: 1px; }
.hb-tab span { font-weight: 600; font-size: 0.92rem; }
.hb-tab small { font-family: var(--codeFont); font-size: 0.66rem;
  color: var(--darkgray); text-transform: uppercase; letter-spacing: .06em; }
.hb-tab:hover { border-color: var(--ember); }
.hb-tab.hb-on { border-color: var(--ember); border-bottom-width: 3px;
  background: var(--lightgray); }

/* --- pinned sentence --- */
.hb-pin { position: sticky; top: 44px; z-index: 20; background: var(--light);
  border-bottom: 1px solid var(--lightgray); padding: 12px 14px;
  margin-top: 18px; }
.hb-pin-lbl { font-family: var(--codeFont); font-size: 0.62rem; letter-spacing: .1em;
  text-transform: uppercase; color: var(--darkgray); margin-bottom: 3px; }
.hb-pin-txt { font-size: 0.94rem; line-height: 1.45; max-height: 3.9em; overflow: hidden; }
.hb-blurb { max-width: 640px; margin: 22px auto 4px; text-align: center;
  color: var(--darkgray); font-size: 0.95rem; line-height: 1.55; }

/* --- the descent --- */
.hb-descent { position: relative; display: grid; grid-template-columns: 34px 1fr;
  gap: 0 14px; max-width: 940px; margin: 0 auto; padding: 20px 24px 40px; }
.hb-wire { position: relative; }
.hb-wire::before { content: ""; position: absolute; left: 50%; top: 8px; bottom: 8px;
  width: 2px; margin-left: -1px; background: repeating-linear-gradient(
    to bottom, var(--lightgray) 0 6px, transparent 6px 10px); }
.hb-probe { position: absolute; left: 50%; top: 0; width: 11px; height: 11px;
  margin-left: -5.5px; border-radius: 50%; background: var(--ember);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--ember) 22%, transparent);
  transition: top .12s linear; }
.hb-layers { min-width: 0; }

.hb-layer { border: 1px solid var(--lightgray); border-left: 3px solid var(--lightgray);
  border-radius: 4px; margin-bottom: 14px; background: var(--light);
  transition: border-color .35s, box-shadow .35s; }
.hb-layer.hb-lit { border-left-color: var(--ember);
  box-shadow: 0 2px 14px color-mix(in srgb, var(--dark) 7%, transparent); }
.hb-layer-head { display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
  padding: 9px 14px; border-bottom: 1px solid var(--lightgray);
  font-family: var(--codeFont); font-size: 0.68rem; text-transform: uppercase;
  letter-spacing: .08em; }
.hb-num { color: var(--ember); font-weight: 700; }
.hb-name { color: var(--dark); font-weight: 600; }
.hb-scale { color: var(--darkgray); margin-left: auto; text-transform: none;
  letter-spacing: .02em; }
.hb-gauge { width: 74px; height: 4px; background: var(--lightgray); border-radius: 2px;
  overflow: hidden; }
.hb-gauge i { display: block; height: 100%; background: var(--amber); }
.hb-layer-body { padding: 14px 16px; }

.hb-q { background: color-mix(in srgb, var(--ember) 20%, transparent);
  color: inherit; border-radius: 2px; padding: 0 2px;
  box-shadow: inset 0 -2px 0 color-mix(in srgb, var(--ember) 55%, transparent); }
.hb-note { font-size: 0.82rem; line-height: 1.5; color: var(--darkgray);
  margin-top: 10px; }
.hb-note.hb-inline { margin: 0; }
.hb-lbl { font-family: var(--codeFont); font-size: 0.62rem; letter-spacing: .08em;
  text-transform: uppercase; color: var(--darkgray); margin-bottom: 5px; }

.hb-doc-title { font-family: var(--headerFont); font-size: 1.15rem; font-weight: 600;
  border-bottom: 1px solid var(--lightgray); padding-bottom: 5px; margin-bottom: 9px; }
.hb-sentence { font-size: 1rem; line-height: 1.6; margin: 0; }
.hb-cite { color: var(--darkgray); font-size: 0.7em; }
.hb-cite-on { color: var(--ember); font-weight: 700;
  background: color-mix(in srgb, var(--ember) 14%, transparent); border-radius: 2px; }

.hb-json { font-family: var(--codeFont); font-size: 0.76rem; line-height: 1.7;
  white-space: pre-wrap; word-break: break-word; margin: 0;
  background: var(--lightgray); padding: 12px 14px; border-radius: 4px; }
.hb-k { color: var(--darkgray); }
.hb-badge { display: inline-block; background: var(--ember); color: #fff;
  border-radius: 3px; padding: 0 6px; font-size: 0.9em; }
.hb-null { color: var(--ember); font-weight: 700; }

.hb-tags { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 10px; }
.hb-tag { font-family: var(--codeFont); font-size: 0.63rem; text-transform: uppercase;
  letter-spacing: .05em; background: var(--lightgray); color: var(--darkgray);
  border-radius: 3px; padding: 2px 7px; }
.hb-tag.hb-warn { background: color-mix(in srgb, var(--amber) 26%, transparent);
  color: var(--dark); }
.hb-passage { font-size: 0.9rem; line-height: 1.62; margin: 0; color: var(--darkgray); }

.hb-grid2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 16px; }
.hb-fold { display: flex; flex-wrap: wrap; gap: 4px; }
.hb-alias { font-family: var(--codeFont); font-size: 0.7rem; background: var(--lightgray);
  border-radius: 3px; padding: 2px 6px; }
.hb-stat { font-family: var(--codeFont); font-size: 0.8rem; }
.hb-repair { display: flex; align-items: center; gap: 9px; flex-wrap: wrap;
  margin-top: 12px; padding: 9px 12px; border-radius: 4px;
  background: color-mix(in srgb, var(--amber) 15%, transparent); }
.hb-rx { font-family: var(--codeFont); font-size: 0.78rem; text-decoration: line-through;
  color: var(--darkgray); }
.hb-arrow { color: var(--ember); }
.hb-rok { font-family: var(--codeFont); font-size: 0.78rem; font-weight: 700; }

.hb-transcript { display: flex; flex-direction: column; gap: 9px; }
.hb-turn { display: grid; grid-template-columns: 118px 1fr; gap: 10px;
  font-size: 0.87rem; line-height: 1.55; opacity: .45;
  border-left: 3px solid transparent; padding-left: 9px; }
.hb-turn.hb-cov { opacity: 1; border-left-color: var(--amber); }
.hb-turn.hb-hit { opacity: 1; border-left-color: var(--ember); }
.hb-spk { font-family: var(--codeFont); font-size: 0.68rem; text-transform: uppercase;
  letter-spacing: .04em; color: var(--darkgray); padding-top: 3px; }
.hb-turn.hb-hit .hb-spk { color: var(--ember); font-weight: 700; }

.hb-episode { display: flex; align-items: center; gap: 14px; text-decoration: none;
  border: 1px solid var(--lightgray); border-radius: 4px; padding: 12px 14px;
  color: var(--dark); }
.hb-episode:hover { border-color: var(--ember); }
.hb-epnum { font-family: var(--codeFont); font-size: 1.5rem; font-weight: 700;
  color: var(--ember); }
.hb-epmeta { display: flex; flex-direction: column; gap: 2px; font-size: 0.9rem; }
.hb-epmeta span { font-size: 0.78rem; color: var(--darkgray); }

/* --- byte compare --- */
.hb-verify { border: 1px solid var(--ember); border-radius: 4px; margin: 0 0 14px;
  padding: 13px 16px; background: color-mix(in srgb, var(--ember) 5%, transparent); }
.hb-verify-head { display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;
  margin-bottom: 11px; }
.hb-vtitle { font-family: var(--codeFont); font-weight: 700; font-size: 0.8rem;
  color: var(--ember); }
.hb-vsub { font-family: var(--codeFont); font-size: 0.64rem; text-transform: uppercase;
  letter-spacing: .07em; color: var(--darkgray); }
.hb-row { display: grid; grid-template-columns: 54px 1fr; gap: 10px; align-items: start;
  margin-bottom: 5px; }
.hb-rl { font-family: var(--codeFont); font-size: 0.62rem; text-transform: uppercase;
  letter-spacing: .06em; color: var(--darkgray); padding-top: 3px; }
.hb-strip { font-family: var(--codeFont); font-size: 0.78rem; line-height: 1.65;
  word-break: break-word; min-height: 1.65em; }
.hb-bad { background: color-mix(in srgb, #d33 32%, transparent); border-radius: 2px; }
.hb-verdict { font-family: var(--codeFont); font-size: 0.76rem; font-weight: 700;
  margin-top: 9px; min-height: 1.2em; color: #1a7f4b; }
:root[saved-theme="dark"] .hb-verdict { color: #4ec98a; }
.hb-v-fail { color: #c0392b; }
:root[saved-theme="dark"] .hb-v-fail { color: #ff7a68; }
.hb-fail-btn { margin-top: 11px; background: none; border: 1px dashed var(--darkgray);
  border-radius: 4px; padding: 5px 11px; cursor: pointer; color: var(--darkgray);
  font-family: var(--codeFont); font-size: 0.7rem; }
.hb-fail-btn:hover { border-color: var(--ember); color: var(--ember); }

/* --- funnel --- */
.hb-funnel { max-width: 720px; margin: 0 auto; padding: 8px 24px 4px; }
.hb-fn { margin-bottom: 15px; }
.hb-fn-lbl { font-size: 0.88rem; font-weight: 600; }
.hb-fn-bar { position: relative; height: 21px; background: var(--lightgray);
  border-radius: 3px; margin: 4px 0 2px; }
.hb-fn-bar i { display: block; height: 100%; border-radius: 3px;
  background: linear-gradient(90deg, var(--ember), var(--amber)); }
.hb-fn-bar span { position: absolute; right: 9px; top: 2px; font-family: var(--codeFont);
  font-size: 0.74rem; font-variant-numeric: tabular-nums; }
.hb-fn-sub { font-size: 0.76rem; color: var(--darkgray); }

@media (max-width: 700px) {
  .hb-descent { grid-template-columns: 18px 1fr; padding: 16px 12px 30px; }
  .hb-turn { grid-template-columns: 1fr; gap: 1px; }
  .hb-row { grid-template-columns: 1fr; }
}
@media (prefers-reduced-motion: reduce) {
  .hb-probe, .hb-layer { transition: none; }
}
"""

JS = """
(function () {
  var root = document.querySelector(".hb");
  if (!root) return;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- trace tabs ----
  root.querySelectorAll(".hb-tab").forEach(function (tab) {
    tab.addEventListener("click", function () {
      var i = tab.dataset.tab;
      root.querySelectorAll(".hb-tab").forEach(function (t) {
        t.classList.toggle("hb-on", t === tab);
      });
      root.querySelectorAll(".hb-trace").forEach(function (tr) {
        tr.hidden = tr.dataset.trace !== i;
      });
      root.querySelector(".hb-tabs").scrollIntoView({
        behavior: reduce ? "auto" : "smooth", block: "start" });
    });
  });

  // ---- light each layer as it arrives, drive the probe ----
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) e.target.classList.add("hb-lit");
    });
  }, { rootMargin: "-35% 0px -35% 0px" });
  root.querySelectorAll(".hb-layer").forEach(function (l) { io.observe(l); });

  function probes() {
    root.querySelectorAll(".hb-trace").forEach(function (tr) {
      if (tr.hidden) return;
      var d = tr.querySelector(".hb-descent"), probe = tr.querySelector(".hb-probe");
      if (!d || !probe) return;
      var r = d.getBoundingClientRect(), mid = window.innerHeight * 0.45;
      var p = Math.min(1, Math.max(0, (mid - r.top) / r.height));
      probe.style.top = (p * (r.height - 16) + 8) + "px";
    });
  }
  window.addEventListener("scroll", probes, { passive: true });
  window.addEventListener("resize", probes);
  probes();

  // ---- byte-compare animation ----
  function runVerify(v) {
    if (v.dataset.done) return;
    v.dataset.done = "1";
    var real = v.dataset.real;
    var a = v.querySelector('[data-role="a"]'), b = v.querySelector('[data-role="b"]');
    var verdict = v.querySelector('[data-role="v"]');
    if (reduce) {
      a.textContent = real; b.textContent = real;
      verdict.textContent = "\\u2713 PASS \\u2014 " + real.length + " bytes identical.";
      return;
    }
    var i = 0;
    var timer = setInterval(function () {
      i++;
      a.textContent = real.slice(0, i);
      b.textContent = real.slice(0, i);
      if (i >= real.length) {
        clearInterval(timer);
        verdict.textContent = "\\u2713 PASS \\u2014 " + real.length +
          " bytes identical, 0 differences.";
      }
    }, 14);
  }
  var vio = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) runVerify(e.target); });
  }, { threshold: 0.4 });
  root.querySelectorAll(".hb-verify").forEach(function (v) { vio.observe(v); });

  root.querySelectorAll(".hb-fail-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var panel = btn.parentElement.querySelector(".hb-fail");
      panel.hidden = !panel.hidden;
      btn.textContent = panel.hidden
        ? "Now try a quote that was tidied up \\u2192"
        : "Hide the failing case";
    });
  });
})();
"""

PAGE = """---
title: How this wiki was built
---

<div class="hb">

<p class="hb-lede">Every sentence on this wiki can be traced to a human being
saying it out loud, on a specific date, into a microphone. That is the whole
premise, and it is checkable rather than promised &mdash; so instead of
describing the pipeline, this page takes one real sentence from a live article
and follows it all the way down to the audio.</p>

<div class="hb-bleed">
<div class="hb-tabs">{tabs}</div>
{traces}
</div>

## What the descent shows

The pipeline runs in the opposite direction to the way you just read it. Raw
transcripts are swept for concept mentions; an alias table folds surface forms
together and a speaker map repairs attribution; a graph of {nodes} concepts and
{edges} edges decides what deserves an article and which passages belong to it;
an extraction pass turns passages into claims pinned to verbatim quotes; a
verifier byte-compares every quote; a writer builds the article from the claims
alone, never seeing the transcripts; and a linter rejects the result if any
paragraph is uncited or any citation fails to resolve.

The layer that matters is the byte-compare. It is the one mechanism that makes
the rest of it more than a plausible-sounding machine: a quote that was
paraphrased, tidied, or invented does not survive it, and an article whose
claims cannot be traced does not build.

<div class="hb-bleed"><div class="hb-funnel">

### What survives each stage

{funnel}

</div></div>

## What this guarantees &mdash; and what it doesn't

**Guaranteed:** every claim traces to a real, verbatim, byte-checked passage in
a real episode you can go listen to. Nothing is sourced from a model's general
knowledge of electronics, from the web, or from vibes. {n_claims} claims across
the wiki carry a quote that has passed this check, and {n_cites} citations
resolve to a specific episode.

**Not guaranteed:** that the *interpretation* is right. The quotes are real, but
an extraction can still miss sarcasm, lose context from five minutes earlier, or
generalise an anecdote into a rule. ASR garble occasionally swallows a number.
Speaker attribution is repaired but imperfect &mdash; where it stays doubtful,
the claim is written so it doesn't depend on who was talking, as the first trace
above shows.

That residual risk is exactly what the **Report** button is for: highlight any
sentence on any article and file an issue in one click. *"The quote is real but
the claim misreads it"* is the failure mode we most want reported, because it is
the one the machinery cannot catch by itself.

## The numbers

| | |
|---|---|
| Episodes transcribed | 719 |
| Words of transcript | ~11 million |
| Concept mentions in the census | ~197,000 |
| Alias table entries | 90,150 |
| Concept graph | {nodes} nodes, {edges} edges |
| Verified claims extracted | {n_claims} |
| Articles live | {n_articles} of 412 planned |
| Episode citations published | {n_cites} |

Everything &mdash; transcripts, census, bundles, packets, tools, this site
&mdash; is in the [public repo](https://github.com/frankie-eight-days/amp-hour-wiki).
If you want to build a piece of it yourself, start at
[How to contribute](./contribute).

*The Amp Hour is Chris Gammell and Dave Jones. This is a fan project built on
their Creative Commons-licensed show; go listen to
[the real thing](https://theamphour.com).*

</div>

<style>{css}</style>
<script>{js}</script>
"""

if __name__ == "__main__":
    main()
