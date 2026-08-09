---
title: How this wiki was built
---

<div class="hb">

<p class="hb-lede">Every sentence on this wiki can be traced to a human being
saying it out loud, on a specific date, into a microphone. That is the whole
premise, and it is checkable rather than promised &mdash; so instead of
describing the pipeline, this page takes one real sentence from a live article
and follows it all the way down to the audio.</p>

<div class="hb-bleed">
<div class="hb-tabs"><button class="hb-tab hb-on" data-tab="0" type="button"><span>Analog to Digital Converter</span><small>ep 218 &middot; practice</small></button><button class="hb-tab" data-tab="1" type="button"><span>Power Grid</span><small>ep 385 &middot; numbers</small></button><button class="hb-tab" data-tab="2" type="button"><span>Reverse Engineering</span><small>ep 302 &middot; history</small></button></div>
<div class="hb-trace" data-trace="0">
  <div class="hb-pin">
    <div class="hb-pin-lbl">tracing this sentence &mdash; Analog to Digital Converter</div>
    <div class="hb-pin-txt">The nominal bit count of a converter does not equal its usable resolution: a 24-bit part in a handheld power-measurement instrument returned roughly 18 effective bits at its highest sample rate and little more than 19 when slowed down.<sup class="hb-cite hb-cite-on">[218]</sup></div>
  </div>
  <div class="hb-blurb">A hard technical claim. Watch the bundle passage swallow three speaker turns &mdash; the quote is Dave's question, the numbers are the guest's answer &mdash; and watch the claim get written so it never depends on which of them said what.</div>
  <div class="hb-descent">
    <div class="hb-wire"><i class="hb-probe"></i></div>
    <div class="hb-layers"><section class="hb-layer" data-layer="05">
  <div class="hb-layer-head">
    <span class="hb-num">05</span>
    <span class="hb-name">Article</span>
    <span class="hb-scale">1 sentence</span>
    <span class="hb-gauge"><i style="width:3.0%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-doc"><div class="hb-doc-title">Analog to Digital Converter</div><p class="hb-sentence">The nominal bit count of a converter does not equal its usable resolution: a 24-bit part in a handheld power-measurement instrument returned roughly 18 effective bits at its highest sample rate and little more than 19 when slowed down.<sup class="hb-cite hb-cite-on">[218]</sup></p><div class="hb-note">The citation is a promise. Everything below is the receipt.</div></div></div>
</section><section class="hb-layer" data-layer="04">
  <div class="hb-layer-head">
    <span class="hb-num">04</span>
    <span class="hb-name">Packet &mdash; where judgment happens</span>
    <span class="hb-scale">1 of 96 claims</span>
    <span class="hb-gauge"><i style="width:28.2%"></i></span>
  </div>
  <div class="hb-layer-body"><pre class="hb-json"><span class="hb-k">"kind"</span>: <span class="hb-badge">practice</span>,
<span class="hb-k">"claim_text"</span>: "The bit count on a converter&#x27;s part number is not the number of usable bits. A 24-bit converter in a handheld power-measurement instrument returned roughly 18 effective bits at its highest sample rate and a little over 19 when slowed down.",
<span class="hb-k">"quote_verbatim"</span>: "<mark class="hb-q">a 24 bit ADC doesn&#x27;t actually give you 24 usable bits out</mark>",
<span class="hb-k">"speaker"</span>: "Dave Jones",
<span class="hb-k">"episode"</span>: 218</pre><div class="hb-note">An extraction pass read all 242 passages below and wrote this. It is the only layer where a machine makes a judgment &mdash; so it is the layer that gets verified.</div></div>
</section><div class="hb-verify" data-real="a 24 bit ADC doesn&#x27;t actually give you 24 usable bits out">
  <div class="hb-verify-head"><span class="hb-vtitle">verify_packet.py</span>
    <span class="hb-vsub">byte-compare &middot; packet quote vs. transcript</span></div>
  <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip" data-role="a"></code></div>
  <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip" data-role="b"></code></div>
  <div class="hb-verdict" data-role="v"></div>
  <button class="hb-fail-btn" type="button">Now try a quote that was tidied up &rarr;</button>
  <div class="hb-fail" hidden>
    <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip">a 24<span class="hb-bad">-</span>bit ADC doesn&#x27;t actually give you 24 usable bits<span class="hb-bad" title="text dropped">&#9251;</span></code></div>
    <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip">a 24 bit ADC doesn&#x27;t actually give you 24 usable bits out</code></div>
    <div class="hb-verdict hb-v-fail">&#10007; FAIL &mdash; quote not found in transcript. Build rejected.</div>
    <div class="hb-note">A hyphen added, a filler word dropped, a contraction
    expanded: all of it fails. This is why nothing on this wiki is
    &ldquo;cleaned up.&rdquo;</div>
  </div>
</div><section class="hb-layer" data-layer="03">
  <div class="hb-layer-head">
    <span class="hb-num">03</span>
    <span class="hb-name">Bundle &mdash; the evidence pack</span>
    <span class="hb-scale">1 of 242 passages</span>
    <span class="hb-gauge"><i style="width:33.9%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-tags"><span class="hb-tag">paragraph 455</span><span class="hb-tag">depth: explains</span><span class="hb-tag">guest: Eric Van Wyk</span><span class="hb-tag hb-warn">spans 3 speaker turns &mdash; Chris Gammell + Dave Jones + Eric Van Wyk</span></div><p class="hb-passage">Uh, because data. I could talk about that in future shows if we&#x27;d like. And of course you&#x27;re, and of course you discovered that <mark class="hb-q">a 24 bit ADC doesn&#x27;t actually give you 24 usable bits out</mark>. Sure. Of course, uh, we&#x27;ve been pulling, uh, in, in our highest speed settings, maybe 18 effective, um, and, and nudging a little bit over 19, uh, when we slow down and, and pay attention a little bit more.</p><div class="hb-note">Deterministic collection, no judgment: every passage in the corpus that touches this concept, gathered in one file for the extraction pass to read.</div></div>
</section><section class="hb-layer" data-layer="02">
  <div class="hb-layer-head">
    <span class="hb-num">02</span>
    <span class="hb-name">Census &amp; canon &mdash; finding it at all</span>
    <span class="hb-scale">486 mentions of this concept</span>
    <span class="hb-gauge"><i style="width:38.2%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-grid2"><div><div class="hb-lbl">surface forms folded into one concept</div><div class="hb-fold"><code class="hb-alias">adc</code><code class="hb-alias">adcs</code><code class="hb-alias">analog-to-digital-converter</code><code class="hb-alias">custom-analog-to-digital-converter</code></div></div><div><div class="hb-lbl">this concept across the corpus</div><div class="hb-stat">211 episodes &middot; 486 mentions &middot; 239 explanatory</div></div></div><div class="hb-note">270,979 mentions were logged across the whole corpus, then folded down a 90,150-entry alias table so that &ldquo;ADC&rdquo;, &ldquo;A to D&rdquo; and &ldquo;analog to digital&rdquo; all land on one concept.</div></div>
</section><section class="hb-layer" data-layer="01">
  <div class="hb-layer-head">
    <span class="hb-num">01</span>
    <span class="hb-name">Transcript &mdash; raw ASR</span>
    <span class="hb-scale">16,283 words in this episode</span>
    <span class="hb-gauge"><i style="width:59.8%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-transcript"><div class="hb-turn"><span class="hb-spk">Eric Van Wyk</span><span class="hb-said">I don&#x27;t see why they do that, but.</span></div><div class="hb-turn hb-cov"><span class="hb-spk">Chris Gammell</span><span class="hb-said">Uh, because data. I could talk about that in future shows if we&#x27;d like.</span></div><div class="hb-turn hb-hit hb-cov"><span class="hb-spk">Dave Jones</span><span class="hb-said">And of course you&#x27;re, and of course you discovered that <mark class="hb-q">a 24 bit ADC doesn&#x27;t actually give you 24 usable bits out</mark>.</span></div><div class="hb-turn hb-cov"><span class="hb-spk">Eric Van Wyk</span><span class="hb-said">Sure. Of course, uh, we&#x27;ve been pulling, uh, in, in our highest speed settings, maybe 18 effective, um, and, and nudging a little bit over 19, uh, when we slow down and, and pay attention a little bit more.</span></div><div class="hb-turn"><span class="hb-spk">Dave Jones</span><span class="hb-said">At the full, what? 8 K sample rate?</span></div></div><div class="hb-note">Machine transcription, errors and filler intact. Nothing here was corrected &mdash; correcting it would break the verification above. The rail marks how far the bundle passage above reached &mdash; 3 turns, more than one speaker. The packet's <code>speaker</code> field records who said the <em>quote</em>, not who supplied every detail in the claim, which is why a claim is written to stand on its evidence rather than on attribution.</div></div>
</section><section class="hb-layer hb-last" data-layer="00">
  <div class="hb-layer-head">
    <span class="hb-num">00</span>
    <span class="hb-name">The episode</span>
    <span class="hb-scale">1 of 719 episodes</span>
    <span class="hb-gauge"><i style="width:40.6%"></i></span>
  </div>
  <div class="hb-layer-body"><a class="hb-episode" href="https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/" target="_blank" rel="noopener"><span class="hb-epnum">218</span><span class="hb-epmeta"><strong>An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter</strong><span>September 29, 2014 &middot; two engineers talking &middot; listen &rarr;</span></span></a><div class="hb-note">Bottom of the stack. A person said this out loud, once, years ago, and now it is a citable sentence.</div></div>
</section></div>
  </div>
</div><div class="hb-trace" data-trace="1" hidden>
  <div class="hb-pin">
    <div class="hb-pin-lbl">tracing this sentence &mdash; Power Grid</div>
    <div class="hb-pin-txt">John Davis described an aluminium smelter paying seven million dollars a month for electricity, which carried monitoring on its incoming supply because a large motor going to ground could force the shutdown of a substantial fraction of that state&#x27;s grid.<sup class="hb-cite hb-cite-on">[385]</sup></div>
  </div>
  <div class="hb-blurb">A number nobody would think to go looking for. Also the clearest look at the canon layer working: the transcript put these words in the host's mouth, and the speaker map moved them back to the guest who actually said them.</div>
  <div class="hb-descent">
    <div class="hb-wire"><i class="hb-probe"></i></div>
    <div class="hb-layers"><section class="hb-layer" data-layer="05">
  <div class="hb-layer-head">
    <span class="hb-num">05</span>
    <span class="hb-name">Article</span>
    <span class="hb-scale">1 sentence</span>
    <span class="hb-gauge"><i style="width:3.0%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-doc"><div class="hb-doc-title">Power Grid</div><p class="hb-sentence">John Davis described an aluminium smelter paying seven million dollars a month for electricity, which carried monitoring on its incoming supply because a large motor going to ground could force the shutdown of a substantial fraction of that state&#x27;s grid.<sup class="hb-cite hb-cite-on">[385]</sup></p><div class="hb-note">The citation is a promise. Everything below is the receipt.</div></div></div>
</section><section class="hb-layer" data-layer="04">
  <div class="hb-layer-head">
    <span class="hb-num">04</span>
    <span class="hb-name">Packet &mdash; where judgment happens</span>
    <span class="hb-scale">1 of 29 claims</span>
    <span class="hb-gauge"><i style="width:20.8%"></i></span>
  </div>
  <div class="hb-layer-body"><pre class="hb-json"><span class="hb-k">"kind"</span>: <span class="hb-badge">numbers</span>,
<span class="hb-k">"claim_text"</span>: "Industrial loads reach a scale where a single site is a grid-level actor: an aluminium smelter paying seven million dollars a month for electricity had monitoring on its incoming supply because a large motor going to ground could force the shutdown of a substantial fraction of that state&#x27;s grid.",
<span class="hb-k">"quote_verbatim"</span>: "<mark class="hb-q">their electricity bill per month was, uh, $7 million a month</mark>",
<span class="hb-k">"speaker"</span>: "John Davis",
<span class="hb-k">"episode"</span>: 385</pre><div class="hb-note">An extraction pass read all 89 passages below and wrote this. It is the only layer where a machine makes a judgment &mdash; so it is the layer that gets verified.</div></div>
</section><div class="hb-verify" data-real="their electricity bill per month was, uh, $7 million a month">
  <div class="hb-verify-head"><span class="hb-vtitle">verify_packet.py</span>
    <span class="hb-vsub">byte-compare &middot; packet quote vs. transcript</span></div>
  <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip" data-role="a"></code></div>
  <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip" data-role="b"></code></div>
  <div class="hb-verdict" data-role="v"></div>
  <button class="hb-fail-btn" type="button">Now try a quote that was tidied up &rarr;</button>
  <div class="hb-fail" hidden>
    <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip">their electricity bill per month was<span class="hb-bad" title="text dropped">&#9251;</span> $7 million a month</code></div>
    <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip">their electricity bill per month was, uh, $7 million a month</code></div>
    <div class="hb-verdict hb-v-fail">&#10007; FAIL &mdash; quote not found in transcript. Build rejected.</div>
    <div class="hb-note">A hyphen added, a filler word dropped, a contraction
    expanded: all of it fails. This is why nothing on this wiki is
    &ldquo;cleaned up.&rdquo;</div>
  </div>
</div><section class="hb-layer" data-layer="03">
  <div class="hb-layer-head">
    <span class="hb-num">03</span>
    <span class="hb-name">Bundle &mdash; the evidence pack</span>
    <span class="hb-scale">1 of 89 passages</span>
    <span class="hb-gauge"><i style="width:27.7%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-tags"><span class="hb-tag">paragraph 230</span><span class="hb-tag">depth: explains</span><span class="hb-tag">guest: John Davis</span><span class="hb-tag hb-warn">spans 3 speaker turns &mdash; John Davis + Chris Gammell</span></div><p class="hb-passage">But probably your, your powers, your power supply is not going to be happy wherever the hell that is. Right. And like, yeah. Uh, more like your power plant. There was a, um, wow. Yeah. One of the companies we were talking to, they do aluminum smelting and, uh, yeah, those guys. Yeah. Yeah. They, <mark class="hb-q">their electricity bill per month was, uh, $7 million a month</mark>, but they, um, they had a situation. They had some special monitoring on their, their, uh, their input to the plant. But either way at the substation, if, if they went to ground and they shorted, like if one of the big, big motors went to ground, um, they could actually shut down, uh, I won&#x27;t say where it is cause it&#x27;ll give it away. Cause I mean, there&#x27;s only like seven of these places in the U S but it would like shut down half of that state&#x27;s electrical grid because they would have to kill the, yeah. I mean, it&#x27;s insane. It&#x27;s just, you basically start to overtax the, uh, the generators, right? Because it&#x27;s probably generated with steam and the generate, you know, like, yeah, like all that stuff, you know, it&#x27;s all tied back somewhere. Yeah, man.</p><div class="hb-note">Deterministic collection, no judgment: every passage in the corpus that touches this concept, gathered in one file for the extraction pass to read.</div></div>
</section><section class="hb-layer" data-layer="02">
  <div class="hb-layer-head">
    <span class="hb-num">02</span>
    <span class="hb-name">Census &amp; canon &mdash; finding it at all</span>
    <span class="hb-scale">121 mentions of this concept</span>
    <span class="hb-gauge"><i style="width:29.6%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-grid2"><div><div class="hb-lbl">surface forms folded into one concept</div><div class="hb-fold"><code class="hb-alias">electric-grid</code><code class="hb-alias">electrical-grid</code><code class="hb-alias">electricity-grid</code><code class="hb-alias">power-grid</code></div></div><div><div class="hb-lbl">this concept across the corpus</div><div class="hb-stat">48 episodes &middot; 121 mentions &middot; 54 explanatory</div></div></div><div class="hb-repair"><span class="hb-rx">Chris Gammell</span><span class="hb-arrow">&rarr;</span><span class="hb-rok">John Davis</span><span class="hb-note hb-inline">the transcript labelled this turn with the wrong voice; the speaker map repaired it</span></div><div class="hb-note">270,979 mentions were logged across the whole corpus, then folded down a 90,150-entry alias table so that &ldquo;ADC&rdquo;, &ldquo;A to D&rdquo; and &ldquo;analog to digital&rdquo; all land on one concept.</div></div>
</section><section class="hb-layer" data-layer="01">
  <div class="hb-layer-head">
    <span class="hb-num">01</span>
    <span class="hb-name">Transcript &mdash; raw ASR</span>
    <span class="hb-scale">17,479 words in this episode</span>
    <span class="hb-gauge"><i style="width:60.3%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-transcript"><div class="hb-turn"><span class="hb-spk">Chris Gammell</span><span class="hb-said">Yeah.</span></div><div class="hb-turn hb-cov"><span class="hb-spk">John Davis</span><span class="hb-said">But probably your, your powers, your power supply is not going to be happy wherever the hell that is. Right. And like, yeah.</span></div><div class="hb-turn hb-hit hb-cov"><span class="hb-spk">Chris Gammell</span><span class="hb-said">Uh, more like your power plant. There was a, um, wow. Yeah. One of the companies we were talking to, they do aluminum smelting and, uh, yeah, those guys. Yeah. Yeah. They, <mark class="hb-q">their electricity bill per month was, uh, $7 million a month</mark>, but they, um, they had a situation. They had some special monitoring on their, their, uh, their input to the plant. But either way at the substation, if, if they went to ground and they shorted, like if one of the big, big motors went to ground, um, they could actually shut down, uh, I won&#x27;t say where it is cause it&#x27;ll give it away. Cause I mean, there&#x27;s only like seven of these places in the U S but it would like shut down half of that state&#x27;s electrical grid because they would have to kill the, yeah. I mean, it&#x27;s insane.</span></div><div class="hb-turn hb-cov"><span class="hb-spk">John Davis</span><span class="hb-said">It&#x27;s just, you basically start to overtax the, uh, the generators, right? Because it&#x27;s probably generated with steam and the generate, you know, like, yeah, like all that stuff, you know, it&#x27;s all tied back somewhere. Yeah, man.</span></div><div class="hb-turn"><span class="hb-spk">Chris Gammell</span><span class="hb-said">It trips the breaker. Yeah. Really big breaker. Yeah.</span></div></div><div class="hb-note">Machine transcription, errors and filler intact. Nothing here was corrected &mdash; correcting it would break the verification above. The rail marks how far the bundle passage above reached &mdash; 3 turns, more than one speaker. The packet's <code>speaker</code> field records who said the <em>quote</em>, not who supplied every detail in the claim, which is why a claim is written to stand on its evidence rather than on attribution. The speaker labels here are the raw ASR ones; the repair shown in layer 02 is what the pipeline actually uses.</div></div>
</section><section class="hb-layer hb-last" data-layer="00">
  <div class="hb-layer-head">
    <span class="hb-num">00</span>
    <span class="hb-name">The episode</span>
    <span class="hb-scale">1 of 719 episodes</span>
    <span class="hb-gauge"><i style="width:40.6%"></i></span>
  </div>
  <div class="hb-layer-body"><a class="hb-episode" href="https://theamphour.com/385-an-interview-with-john-davis/" target="_blank" rel="noopener"><span class="hb-epnum">385</span><span class="hb-epmeta"><strong>An Interview with John Davis</strong><span>March 25, 2018 &middot; two engineers talking &middot; listen &rarr;</span></span></a><div class="hb-note">Bottom of the stack. A person said this out loud, once, years ago, and now it is a citable sentence.</div></div>
</section></div>
  </div>
</div><div class="hb-trace" data-trace="2" hidden>
  <div class="hb-pin">
    <div class="hb-pin-lbl">tracing this sentence &mdash; Reverse Engineering</div>
    <div class="hb-pin-txt">On Digilent&#x27;s low-cost development boards, the team reverse engineered the Xilinx programming cable and integrated it onto the boards, because a seventy-nine-dollar board could not be sold alongside a three-hundred-dollar programming cable; equivalent cables of Digilent&#x27;s own design followed.<sup class="hb-cite hb-cite-on">[302]</sup></div>
  </div>
  <div class="hb-blurb">The kind of thing that exists only because someone said it out loud on a podcast. It is in no datasheet and no press release, and the speaker interrupts himself to wonder whether he should be telling the story at all.</div>
  <div class="hb-descent">
    <div class="hb-wire"><i class="hb-probe"></i></div>
    <div class="hb-layers"><section class="hb-layer" data-layer="05">
  <div class="hb-layer-head">
    <span class="hb-num">05</span>
    <span class="hb-name">Article</span>
    <span class="hb-scale">1 sentence</span>
    <span class="hb-gauge"><i style="width:3.0%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-doc"><div class="hb-doc-title">Reverse Engineering</div><p class="hb-sentence">On Digilent&#x27;s low-cost development boards, the team reverse engineered the Xilinx programming cable and integrated it onto the boards, because a seventy-nine-dollar board could not be sold alongside a three-hundred-dollar programming cable; equivalent cables of Digilent&#x27;s own design followed.<sup class="hb-cite hb-cite-on">[302]</sup></p><div class="hb-note">The citation is a promise. Everything below is the receipt.</div></div></div>
</section><section class="hb-layer" data-layer="04">
  <div class="hb-layer-head">
    <span class="hb-num">04</span>
    <span class="hb-name">Packet &mdash; where judgment happens</span>
    <span class="hb-scale">1 of 64 claims</span>
    <span class="hb-gauge"><i style="width:25.7%"></i></span>
  </div>
  <div class="hb-layer-body"><pre class="hb-json"><span class="hb-k">"kind"</span>: <span class="hb-badge">history</span>,
<span class="hb-k">"claim_text"</span>: "Reverse engineering has been used as a deliberate market entry route: a vendor&#x27;s programming cable was reverse engineered and integrated onto low-cost development boards, because a seventy-nine dollar board could not be sold alongside a three-hundred-dollar programming cable. Equivalent cables of the entrant&#x27;s own design followed, and after several years of demonstrated reliability the original vendor&#x27;s tools began supporting that hardware.",
<span class="hb-k">"quote_verbatim"</span>: "<mark class="hb-q">we reverse-engineered Xilinx&#x27;s programming cable</mark>",
<span class="hb-k">"speaker"</span>: "Clint Cole",
<span class="hb-k">"episode"</span>: 302</pre><div class="hb-note">An extraction pass read all 138 passages below and wrote this. It is the only layer where a machine makes a judgment &mdash; so it is the layer that gets verified.</div></div>
</section><div class="hb-verify" data-real="we reverse-engineered Xilinx&#x27;s programming cable">
  <div class="hb-verify-head"><span class="hb-vtitle">verify_packet.py</span>
    <span class="hb-vsub">byte-compare &middot; packet quote vs. transcript</span></div>
  <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip" data-role="a"></code></div>
  <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip" data-role="b"></code></div>
  <div class="hb-verdict" data-role="v"></div>
  <button class="hb-fail-btn" type="button">Now try a quote that was tidied up &rarr;</button>
  <div class="hb-fail" hidden>
    <div class="hb-row"><span class="hb-rl">packet</span><code class="hb-strip">we reverse<span class="hb-bad"> </span>engineered Xilinx&#x27;s programming cable</code></div>
    <div class="hb-row"><span class="hb-rl">source</span><code class="hb-strip">we reverse-engineered Xilinx&#x27;s programming cable</code></div>
    <div class="hb-verdict hb-v-fail">&#10007; FAIL &mdash; quote not found in transcript. Build rejected.</div>
    <div class="hb-note">A hyphen added, a filler word dropped, a contraction
    expanded: all of it fails. This is why nothing on this wiki is
    &ldquo;cleaned up.&rdquo;</div>
  </div>
</div><section class="hb-layer" data-layer="03">
  <div class="hb-layer-head">
    <span class="hb-num">03</span>
    <span class="hb-name">Bundle &mdash; the evidence pack</span>
    <span class="hb-scale">1 of 138 passages</span>
    <span class="hb-gauge"><i style="width:30.4%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-tags"><span class="hb-tag">paragraph 49</span><span class="hb-tag">depth: opinion</span><span class="hb-tag">guest: Clint Cole</span><span class="hb-tag hb-warn">spans 2 speaker turns &mdash; Chris Gammell + Clint Cole Of Digilent</span></div><p class="hb-passage">Okay. Yeah, and it had – it was the first board with an onboard programming circuit. So <mark class="hb-q">we reverse-engineered Xilinx&#x27;s programming cable</mark>. I don&#x27;t know if I should say this – oh, well, too late. But we reverse-engineered theirs, stuck it on our board. Nobody said anything. So that was good because you only needed the board and a cable and nothing else. Nice. See, but that&#x27;s good though too because that means that ultimately that – what they really want is to sell more parts. So what – I mean, I&#x27;m sure that&#x27;s in spades, right?</p><div class="hb-note">Deterministic collection, no judgment: every passage in the corpus that touches this concept, gathered in one file for the extraction pass to read.</div></div>
</section><section class="hb-layer" data-layer="02">
  <div class="hb-layer-head">
    <span class="hb-num">02</span>
    <span class="hb-name">Census &amp; canon &mdash; finding it at all</span>
    <span class="hb-scale">194 mentions of this concept</span>
    <span class="hb-gauge"><i style="width:32.5%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-grid2"><div><div class="hb-lbl">surface forms folded into one concept</div><div class="hb-fold"><code class="hb-alias">reverse-engineer</code><code class="hb-alias">reverse-engineering</code></div></div><div><div class="hb-lbl">this concept across the corpus</div><div class="hb-stat">107 episodes &middot; 194 mentions &middot; 102 explanatory</div></div></div><div class="hb-repair"><span class="hb-rx">Chris Gammell</span><span class="hb-arrow">&rarr;</span><span class="hb-rok">Clint Cole</span><span class="hb-note hb-inline">the transcript labelled this turn with the wrong voice; the speaker map repaired it</span></div><div class="hb-note">270,979 mentions were logged across the whole corpus, then folded down a 90,150-entry alias table so that &ldquo;ADC&rdquo;, &ldquo;A to D&rdquo; and &ldquo;analog to digital&rdquo; all land on one concept.</div></div>
</section><section class="hb-layer" data-layer="01">
  <div class="hb-layer-head">
    <span class="hb-num">01</span>
    <span class="hb-name">Transcript &mdash; raw ASR</span>
    <span class="hb-scale">20,688 words in this episode</span>
    <span class="hb-gauge"><i style="width:61.3%"></i></span>
  </div>
  <div class="hb-layer-body"><div class="hb-transcript"><div class="hb-turn"><span class="hb-spk">Chris Gammell</span><span class="hb-said">Yeah, and I think having a dedicated signal source that they could wrap their brain around and manipulate in real time was a good teaching thing. So then from that only – we made like 30 or 40 of those for just my class. The first board that really made it out of our little department was – we call it the XLA board. And it was a – boy, the first Spartan FPGA. Oh, wow.</span></div><div class="hb-turn"><span class="hb-spk">Clint Cole Of Digilent</span><span class="hb-said">Okay.</span></div><div class="hb-turn hb-hit hb-cov"><span class="hb-spk">Chris Gammell</span><span class="hb-said">Yeah, and it had – it was the first board with an onboard programming circuit. So <mark class="hb-q">we reverse-engineered Xilinx&#x27;s programming cable</mark>. I don&#x27;t know if I should say this – oh, well, too late. But we reverse-engineered theirs, stuck it on our board. Nobody said anything. So that was good because you only needed the board and a cable and nothing else.</span></div><div class="hb-turn hb-cov"><span class="hb-spk">Clint Cole Of Digilent</span><span class="hb-said">Nice. See, but that&#x27;s good though too because that means that ultimately that – what they really want is to sell more parts. So what – I mean, I&#x27;m sure that&#x27;s in spades, right?</span></div><div class="hb-turn"><span class="hb-spk">Chris Gammell</span><span class="hb-said">Well, it just made it really convenient to own and to use. Yeah. And then it had a breadboard on it so you could put little like whatever 7400 circuit chips in there or something. And then nuisance things like buttons and switches and LEDs that everybody needs and wants, but you didn&#x27;t want to make them wire it up in a breadboard. Right.</span></div></div><div class="hb-note">Machine transcription, errors and filler intact. Nothing here was corrected &mdash; correcting it would break the verification above. The rail marks how far the bundle passage above reached &mdash; 2 turns, more than one speaker. The packet's <code>speaker</code> field records who said the <em>quote</em>, not who supplied every detail in the claim, which is why a claim is written to stand on its evidence rather than on attribution. The speaker labels here are the raw ASR ones; the repair shown in layer 02 is what the pipeline actually uses.</div></div>
</section><section class="hb-layer hb-last" data-layer="00">
  <div class="hb-layer-head">
    <span class="hb-num">00</span>
    <span class="hb-name">The episode</span>
    <span class="hb-scale">1 of 719 episodes</span>
    <span class="hb-gauge"><i style="width:40.6%"></i></span>
  </div>
  <div class="hb-layer-body"><a class="hb-episode" href="https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/" target="_blank" rel="noopener"><span class="hb-epnum">302</span><span class="hb-epmeta"><strong>An Interview with Clint Cole of Digilent</strong><span>June 8, 2016 &middot; two engineers talking &middot; listen &rarr;</span></span></a><div class="hb-note">Bottom of the stack. A person said this out loud, once, years ago, and now it is a citable sentence.</div></div>
</section></div>
  </div>
</div>
</div>

## What the descent shows

The pipeline runs in the opposite direction to the way you just read it. Raw
transcripts are swept for concept mentions; an alias table folds surface forms
together and a speaker map repairs attribution; a graph of 4,016 concepts and
12,776 edges decides what deserves an article and which passages belong to it;
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

<div class="hb-fn"><div class="hb-fn-lbl">Words of raw transcript</div><div class="hb-fn-bar"><i style="width:100.0%"></i><span>11,000,000</span></div><div class="hb-fn-sub">719 episodes, machine-transcribed</div></div><div class="hb-fn"><div class="hb-fn-lbl">Concept mentions logged</div><div class="hb-fn-bar"><i style="width:77.2%"></i><span>270,979</span></div><div class="hb-fn-sub">the census pass</div></div><div class="hb-fn"><div class="hb-fn-lbl">Verified claims extracted</div><div class="hb-fn-bar"><i style="width:59.1%"></i><span>14,400</span></div><div class="hb-fn-sub">each pinned to a byte-checked quote</div></div><div class="hb-fn"><div class="hb-fn-lbl">Episode citations published</div><div class="hb-fn-bar"><i style="width:55.9%"></i><span>8,633</span></div><div class="hb-fn-sub">across every live article</div></div><div class="hb-fn"><div class="hb-fn-lbl">Articles live</div><div class="hb-fn-bar"><i style="width:32.9%"></i><span>208</span></div><div class="hb-fn-sub">of 412 planned</div></div>

</div></div>

## What this guarantees &mdash; and what it doesn't

**Guaranteed:** every claim traces to a real, verbatim, byte-checked passage in
a real episode you can go listen to. Nothing is sourced from a model's general
knowledge of electronics, from the web, or from vibes. 14,400 claims across
the wiki carry a quote that has passed this check, and 8,633 citations
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
| Concept mentions in the census | 270,979 |
| Alias table entries | 90,150 |
| Concept graph | 4,016 nodes, 12,776 edges |
| Verified claims extracted | 14,400 |
| Articles live | 208 of 412 planned |
| Episode citations published | 8,633 |

Everything &mdash; transcripts, census, bundles, packets, tools, this site
&mdash; is in the [public repo](https://github.com/frankie-eight-days/amp-hour-wiki).
If you want to build a piece of it yourself, start at
[How to contribute](./contribute).

*The Amp Hour is Chris Gammell and Dave Jones, and it is theirs &mdash; this is
an unaffiliated fan project built out of admiration for the show, quoting
briefly and always with a link home. Go listen to
[the real thing](https://theamphour.com).*

</div>

<style>
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
.hb-pin { position: sticky; top: var(--amp-nav, 43px); z-index: 20;
  background: var(--light);
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
</style>
<script>
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
      verdict.textContent = "\u2713 PASS \u2014 " + real.length + " bytes identical.";
      return;
    }
    var i = 0;
    var timer = setInterval(function () {
      i++;
      a.textContent = real.slice(0, i);
      b.textContent = real.slice(0, i);
      if (i >= real.length) {
        clearInterval(timer);
        verdict.textContent = "\u2713 PASS \u2014 " + real.length +
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
        ? "Now try a quote that was tidied up \u2192"
        : "Hide the failing case";
    });
  });
})();
</script>
