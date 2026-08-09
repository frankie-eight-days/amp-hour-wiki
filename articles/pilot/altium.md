---
title: Altium
concept: altium
episodes: 226
guests: 36
explains: 41
opinion: 62
generated: 2026-08-08
model: claude-opus-5 (pilot batch, pipeline steps 6-8)
---

<!--
PRODUCTION NOTES (not for readers)
Gather: 606 census mentions across 226 episodes -> 200 pinned explains/opinion
passages after paragraph-level dedupe, CAPPED at 150 (all explains kept; opinion
selected by recency + speaker diversity, non-host speakers first).
Re-grade: of the 150 examined, 103 retained as substantive (41 explains, 62
opinion) and 47 discarded. Note the shape: unlike the tool concepts this one is
mostly opinion and corporate history rather than technique, because Dave Jones
worked at the company for four years and narrated it thereafter. Named attribution
is heavier here than in the other pilots because the who genuinely is the content.
Evidence packet: _packets/altium.json (59 claims, 4 disagreement groups).
ATTRIBUTION - the worst of the five concepts:
 * Eps 472 and 523 label their guest's turns "Chris Gammell", but the speaker
   describes working at Valve on the Steam Controller and selling a Geiger counter
   kit. That is Jeff Keyzer. Reassigned by content.
 * Ep 59 labels "Chris Gammell" saying he was laid off when Altium moved to China.
   That is Dave Jones, who worked there. Reassigned.
 * Ep 555 fuses and swaps the two hosts mid-exchange: the pro-Altium argument is
   labelled Chris Gammell but is answered by a turn labelled Dave Jones saying
   "Dave's working from old knowledge". Reassigned by content. Ep 555 is NOT in the
   144-file suspect list, because that detector only catches host/guest swaps - it
   cannot see host-to-host swaps. See _pilot_report.md.
One passage (Altium's 2011 move to Shanghai) is uncitable: its episode has no
episode number in the corpus.
-->

Altium is a commercial PCB design package, originally released as Protel by a company founded in Tasmania in 1985 and renamed in the early 2000s after a merger of its competing Protel and PCAD product lines.[659][471] Its design model places part, supplier and fit data in the schematic and propagates it forward to generated manufacturing outputs, a method that yields little benefit unless adopted completely.[174] It holds roughly 30 percent of the PCB design market and dominates the small-to-medium company segment, with larger firms running Cadence.[531][505] Its corporate history is unusually turbulent for an incumbent tool — a founder removed by his own board, two headquarters relocations, an abandoned FPGA strategy, a rejected Autodesk approach and a 2024 acquisition.[118][197][267][546][659]

## Design model and file behaviour

The intended workflow places all part numbers, supplier information and fit/no-fit status in the schematic, from which bills of materials are generated; partial adoption of the method yields none of its benefit.[174] Schematic and PCB differencing is built into the tool and highlights changes, which is presented as the precondition for version control on hardware designs.[67]

Manufacturing output is scripted through an OutJob, a definition that produces identical file sets across projects.[434] The reproducibility cuts both ways: a misconfigured OutJob fails silently, in one case exporting two layers of a four-layer board without error.[434] A second export behaviour causes recurring fabricator problems — Altium renders internal plane layers as negative images, which some fabricators reject, the workaround being to implement inner planes as flooded signal layers instead.[434] KiCad generates positive plane images and does not raise the same issue.[434] Altium's board outline layer likewise differs from other tools' conception of an outline and is typically not contiguous, which fabricators must accommodate.[299]

File compatibility is unusually strong in two respects. Files created in newer versions can be opened in older ones, described as an essential property for professional work,[555] and the format proved robust across unstable daily builds without corrupting saved work.[543] Library management is the opposite case: the tool supports several incompatible approaches and never settled on one, leaving the choice to each user group.[543] Both Altium and [[kicad]] decouple symbol, footprint and 3D model, in contrast to an atomic model binding them to a single manufacturer part number.[508] The panelisation tool works but is imprecise enough that manual copy-paste is often preferred even by licensed users.[415]

Keyboard shortcuts and commands were preserved from the 1985 DOS-era Protel releases for roughly three decades, which is what made the later interface overhaul consequential.[523]

## Cost, adoption and market position

Tool choice is governed by switching cost rather than by feature comparison. Adoption is effectively a ten-year commitment because the existing design corpus is locked into the format, a dependency vendors are held to understand and price against.[154] Jeff Keyzer characterises the resulting attachment as allegiance rather than evaluation, and attempts at conversion as unproductive;[472] Chris Gammell stopped advocating tool changes on the grounds that the decision turns on willingness to pay rather than on features.[298] Change therefore requires an external trigger such as leaving a job and its licence, which produces a circularity for individuals — learning the tool speculatively is the only way to win contracts that require it.[306] Charles Alexanian's shop migrated for exactly such a trigger, when [[eagle]] moved to subscription licensing and Altium halved its price to capture displaced users.[429]

Whether the licence is worth its price divides along professional lines. Dave Jones declines to buy at five to six thousand dollars, having ceased daily layout work,[277][306] and proposes board complexity as the test, holding that Raspberry Pi-class designs do not need the tool.[574] Reported pricing is roughly 5,000 dollars initially with 1,500 to 2,000 dollars annually for maintenance.[574] The counter-argument is billable time: Chris Gammell migrated from Eagle when fighting the cheaper tool began consuming hours, and holds that a single day of avoided output-generation trouble repays the difference.[537] Shrouk El Attar supplies the access argument, noting the licence is unaffordable without an employer and framing open-source alternatives as an accessibility requirement.[549]

Market share is estimated at roughly 30 percent for Altium and 25 percent for Eagle, with KiCad, OrCAD and Allegro near 15 percent each.[531] Segmented by company size, larger and older firms run Cadence while Altium holds the small-to-medium segment,[505] and for small consumer-hardware companies it is described as effectively the only option.[505] Dave Jones characterises the landscape as Altium and everyone else,[482] and attributes part of the position to decades of dominance in Australian student licensing — which creates a hiring cost, since each new employee needs a seat.[231]

Whether KiCad threatens that position was disputed directly. Dave Jones holds it is not yet a professional-grade tool and remains far from challenging Altium in high-end work; Chris Gammell responded that the assessment rests on outdated familiarity, while allowing it may have been correct when formed.[555]

## Corporate history

The company was founded in Tasmania in 1985 by Nick Martin, trading as Protel.[659] Protel 99 SE became the industry standard for around twenty years and was near-universal in Chinese development houses, to the degree that satisfied users would not buy upgrades — a sales problem created by the product's own longevity.[659] The Altium name arrived in the early 2000s with a merger of the internally competing Protel and PCAD lines, combining PCAD's PCB strengths with Protel's schematic strengths.[471] The name itself was salvage, taken from a trademark portfolio acquired with IBM-originated technology and chosen because the trademark was already owned.[164]

A strategy built on FPGAs and modular block design followed, on the premise that board layout would become unnecessary. Dave Jones argues it failed because engineering does not compose that way,[267] while separately crediting the toolchain as technically effective at a high level — vendor-agnostic, with drag-in processor cores and C-to-HDL synthesis — and as failing only when projects became serious.[449]

The company relocated to Shanghai around 2011, with layoffs.[59] Founder Nick Martin was subsequently removed by the board,[118] and the successor strategy was a return to core EDA functionality and away from Internet of Things work.[124] A further relocation to San Diego in 2014 was accompanied by an admission that the Internet of Things strategy had failed; it followed an earlier unsuccessful move to San Jose in the 1990s, and US military business was reported lost over China-based R&D.[197]

Two attempts at a low-cost tier followed. CircuitMaker was free but cloud-only with no local file saving, and was predicted to fail on release;[216] the specific risk identified was abandonment, a free cloud tool with no revenue model having nothing to prevent its cancellation.[251] Circuit Studio, the paid low-cost tier, was rated good value at its price point but deliberately kept incompatible with Altium Designer to prevent firms substituting cheap seats.[316]

By 2021 the company was publicly signalling willingness to be acquired, with long-standing unfixed defects cited as the one argued benefit of an Autodesk takeover.[546] The acquisition completed at 68 dollars per share, an increase Dave Jones deflates against a float price of a few dollars roughly 24 years earlier.[659]

## Working conditions and internal assessment

Two former employees describe the company's technical staff as uniformly strong, Ben Jordan contrasting it with previous employers where competence was uneven.[593] Jordan characterises the founder's approach as running the company as a hobby rather than to maximise returns, a reading Dave Jones concurs with in the phrase "a publicly traded hobby".[593] Jones learned of the relocation to China, and of his own redundancy, when handed his final pay,[59] and notes that shares fell to ten cents during his employment — a position that would later have been worth 13.7 million dollars.[659]

Jeff Keyzer's account of the Altium 17/18 interface overhaul is the most detailed user impact recorded. He had version-locked Altium 12 for the duration of the Steam Controller project, importing a semiconductor-industry practice of freezing tool versions across long programmes so that CAD defects cannot disrupt schedule.[523] Returning after a break, he found the interface rewritten and his accumulated expertise void, describing the experience of being a former expert rendered ineffective.[523] His objection is not to change as such but to its justification: much of it appeared unnecessary, and he questions the aggregate productivity cost to established users.[523]

## Notable positions

Altium is reported to have delayed a product launch after a critical public video and revised its direction.[213] Dave Jones states he no longer receives a licence from the company,[627] and by 2021 reported a loss of interest in it altogether.[546] On the 2024 acquisition, Chris Gammell noted that deals of that kind are frequently blocked by regulators.[659]

## Further reading

- [EAGLE 6 soon](http://www.cadsoftusa.com/eagle-pcb-design-software/new-in-v6/?language=en) — via #67
- [Altium is moving again](http://www.eetimes.com/document.asp?doc_id=1322173) — via #197
- [Dave wrote a forum post translating press release](http://www.eevblog.com/forum/altium/altium-moves-again!/) — via #197
- [CircuitMaker](http://www.circuitmaker.com/#why_circuitmaker) — via #251
- [the backwards nature of the EDA industry](http://www.boldport.com/blog/2013/09/engineers-assemble.html) — via #267
- [reduced the price on Circuit Studio, which puts it into competitive territory.](http://www.eevblog.com/forum/eda/circuit-studio-reboot/) — via #306
- [CadSoft EAGLE](https://en.wikipedia.org/wiki/EAGLE_%28program%29) — via #471
- [PCAD with Accel EDA](https://en.wikipedia.org/wiki/P-CAD) — via #471
- [Protel became Altium](https://en.wikipedia.org/wiki/Altium) — via #471
- [the EAGLE acquisition](https://hackaday.com/2016/06/29/the-eagle-has-landed-at-autodesk/) — via #471
- [Altium365](https://www.altium.com/altium-365) — via #505
- [SnapEDA](https://www.snapeda.com/) — via #531
- [external plugins for Altium and KiCad.](https://www.snapeda.com/plugins/) — via #531
- [Solidworks rebadges Altium as "Solidworks PCB"](https://www.solidworks.com/product/solidworks-pcb) — via #546
- [Altium Buys Morfik in 2010](https://www.edn.com/eeek-altium-is-going-to-buy-morfik/) — via #659
- [Altium bought Octopart in 2017](https://octopart.com/pulse/p/octopart-is-joining-altium-2) — via #659
- [History of Protel / Altium](https://en.wikipedia.org/wiki/Altium_Designer) — via #659
- [Nick booted out](https://www.eevblog.com/forum/altium/nick-martin-booted-out-as-altium-ceo/) — via #659

## References

| Ep | Title | URL | Date |
|---|---|---|---|
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ | - |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ | - |
| 118 | Kickstarter, Open Source RC & Modelsource - Facinorous Financial Foulness | https://theamphour.com/the-amp-hour-118-facinorous-financial-foulness/ | October 21st, 2012 |
| 124 | SpaceX, Enclosures & Startups - Urging Unemployment Ullagone | https://theamphour.com/the-amp-hour-124-urging-unemployment-ullagone/ | December 3rd, 2012 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16th, 2013 |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ | September 23rd, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2nd, 2013 |
| 197 | Spacing Out On Space - Dave's Dongle Designing | https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/ | May 5th, 2014 |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ | 2014 |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15th, 2014 |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ | January 6th, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26th, 2015 |
| 267 | Standing With Ahmed | https://theamphour.com/267-standing-with-ahmed/ | September 16th, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9th, 2015 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11th, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18th, 2016 |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ | July 6th, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21st, 2016 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 429 | An Interview with Charles Alexanian | https://theamphour.com/429-an-interview-with-charles-alexanian/ | 2019 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17th, 2019 |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ | June 30th, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22nd, 2019 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1st, 2020 |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ | August 16th, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13th, 2020 |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ | December 27, 2020 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | - |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ | April 5th, 2021 |
| 543 | Cassette decks have browsers? | https://theamphour.com/543-cassette-decks-have-browsers/ | - |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21st, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11th, 2021 |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ | August 30th, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23rd, 2022 |
| 593 | Publicly Traded Hobby with Ben Jordan | https://theamphour.com/593-publicly-traded-hobby-with-ben-jordan/ | June 14th, 2022 |
| 627 | Works on my machine | https://theamphour.com/627-works-on-my-machine/ | April 9th, 2023 |
| 659 | Altium...Acquired! | https://theamphour.com/659-altium-acquired/ | - |
