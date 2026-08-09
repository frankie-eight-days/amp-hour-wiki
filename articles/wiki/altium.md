---
title: Altium
concept: altium
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Altium is an electronic design automation (EDA) software company whose flagship product, the Altium Designer printed circuit board (PCB) design package, holds the small and medium-sized company segment of the professional PCB tool market.[505] The company descends from Protel, a DOS-based PCB editor written by Nick Martin at the University of Tasmania in 1985, and its Protel 99 SE release remained an industry standard for roughly twenty years.[659] The company listed on the stock market around 1999, relocated its base several times across three continents, and in 2024 was acquired by Renesas in the largest Japanese acquisition of an Australian-listed company.[659][197]

## History

### Protel origins

Protel was written in Borland Turbo Pascal as a DOS PCB editor by Nick Martin at the University of Tasmania in 1985; the companion schematic tool followed two to three years later, and a lower-cost edition, Easy Tracks, shipped with a hardware dongle.[659] Protel for Windows, released in the early 1990s, was among the first PCB tools written for Windows, at a time when it was not settled whether Windows or the Mac OS would become the dominant desktop platform.[659] Protel 99 SE, released around the company's 1999 stock-market listing, remained an industry standard for roughly twenty years and was used by practically every development house in China.[659] Like any long-lived design tool, it accumulated a stable set of known defects that experienced designers catalogued and routed around rather than awaiting fixes; twelve documented defects in Protel 99 SE were handled this way.[659]

### From Protel to Altium

The rename from Protel to Altium in the early 2000s resolved internal competition between the PCAD and Protel product lines, which were sold at similar price points to overlapping users; PCAD's strength was PCB and Protel's was schematic, and the two were hybridised into Altium Designer.[471] In an overnight repricing announced to staff by founder Nick Martin, the package was cut roughly 80 percent, from around eight to ten thousand dollars to a flat two thousand dollars, framed internally as irreversible: "we are burning our bridges. We can't go back to high price software".[593] Customers who had recently paid the old price were left holding it.[593]

### FPGA diversification

After its stock-market listing the company redirected its product strategy around FPGAs on the premise that FPGAs would displace microcontrollers, a decision driven personally by the founder in a flat organisation where nothing proceeded without his approval.[555] The NanoBoard NB2, a four-thousand-dollar FPGA development board bundled with a licence that deliberately excluded the PCB tool, was built on the premise that customers would assemble products from prebuilt modules and never lay out a custom board again; it did not sell, distributor stock was returned, and the successor NanoBoard 3000 was priced an order of magnitude lower at around three hundred dollars.[555] The FPGA tooling let a designer drag in vendor-portable blocks including processor cores and included C-to-HDL synthesis, so a simple application could be built without writing Verilog or VHDL; it worked well at that level of abstraction and obstructed work on serious projects that needed access to the underlying detail.[449]

### Leadership change and relocations

Founder Nick Martin was removed by the board in 2012 while remaining the company's largest single shareholder with roughly a quarter of its stock, after a decade in which the company had repeatedly taken losses on ventures outside its core PCB and schematic product line.[118] The company relocated its base repeatedly: to San Jose in the 1990s and back to Sydney, to China around 2012, and to San Diego in 2014, with a substantial share of development carried out in Ukraine after the China move.[197] A design-tool vendor's country of R&D is a procurement constraint for defence customers, and after the relocation of headquarters and R&D to China the company was reported to be losing United States military-sector business under rules governing dealings with companies based there.[197]

### Acquisitions and the Renesas takeover

Octopart and Ciiva were acquired to serve as the component database and library back end for CircuitMaker, with the same infrastructure intended to feed Altium Designer.[264] Octopart is one of the two major cross-distributor part search engines alongside FindChips, giving the vendor a pricing and availability data source inside its own tools.[659] Renesas acquired Altium at sixty-eight Australian dollars a share, roughly a third above the prevailing market price and about twenty-four times revenue, in the largest Japanese acquisition of an Australian-listed company; at the time the company was debt-free and, despite a United States headquarters, remained Australian-registered.[659]

## Product family

### CircuitMaker

The original CircuitMaker plan was a free base package with capabilities bought as needed, on the order of fifty dollars to unlock eight layers for a month; the product shipped instead as entirely free with no feature limits.[251] Its free terms required published projects, but a project stays private until it is committed and a local copy is held on disk, so the publication requirement applies at commit rather than at every edit.[251] CircuitMaker was deliberately degraded with a random sleep routine so that it would not compete with the paid product; the vendor's public account attributed slowdowns to designs above roughly five thousand connections, while users reported the degradation regardless of size, along with parts disappearing or relocating during drag operations as side effects of the deliberate routine rather than ordinary defects.[400] Upverter was subsequently acquired and made free, and CircuitMaker was folded into it as Upverter Desktop, the offline-capable counterpart to the browser-based Upverter Online.[400]

### Circuit Studio

Circuit Studio originated at Element14's request so the distributor would have its own higher-end tool to sell after Eagle became its low-end offering; it was distributed exclusively through Element14 and priced around three thousand dollars at introduction.[242][659] It was made deliberately file-incompatible with Altium Designer so that a company could not buy a small number of full seats and staff the rest of the work on cheap ones.[316] The launch price of three to four thousand dollars sat between the free and professional tiers and attracted neither — described as "the no man's land of CAD pricing" — and was later cut to nine hundred and ninety-five dollars with a hundred and twenty-five dollar annual maintenance.[306] The product was then left without upgrades for around five years while paying customers continued to hold licences.[659]

The differentiation between the free and professional products was drawn on productivity rather than capability: the cheaper tool remains able to do the work but takes longer, so daily layout work justifies the paid seat on time alone.[216] Shipping a separate simplified product rather than a feature-limited build of the main one commits the vendor to maintaining two code bases, a permanent tax on engineering capacity.[213]

### Altium 365

Altium 365 is the vendor's cloud design-review and collaboration layer; it stores designs in its own workspace rather than integrating with GitHub, GitLab or Bitbucket, which is the operative constraint for teams whose review process is already anchored on one of those services.[505] It was positioned as shared, in-browser access to a design in the way a document is shared — "like Google Docs for PCB design" — and brought that capability to mid-market teams for whom the previous route was a substantially more expensive enterprise licence.[718] The cloud layer was made optional rather than mandatory, so a shop that declines it keeps working locally, a distinction from competitors who removed the local-only path.[601] The platform allows a manufacturer to annotate a design in place with process-specific feedback — for example, that a BGA sits close enough to a capacitor to cause thermal shadowing — turning fabrication review into feedback during layout rather than after release.[545] Later pricing restructured around this shared workspace, with author seats at thirteen hundred dollars a year plus collaborator seats, spreading licence cost across everyone in the value chain who touches the design rather than concentrating it on the layout engineer.[707]

### SolidWorks PCB

SolidWorks PCB is a rebadged Altium product, so a shop nominally standardised on the SolidWorks ECAD tool is on the same underlying package.[546]

## Licensing and pricing

List pricing has moved by large multiples over time: a roughly seventy percent cut from about twelve thousand dollars to three or four thousand in the early 2010s, and a return to eight to ten thousand dollars in the United States within a few years.[316] Reported pricing settled around five thousand dollars for an initial seat with fifteen hundred to two thousand dollars a year for maintenance.[574] Altium does not publish its pricing; figures circulating among users were around six thousand dollars a seat with about twenty-five hundred a year for maintenance, and letting maintenance lapse stops the tool working under the newer terms.[659]

The list price is negotiable and varies with the sales cycle; approaching a representative near the end of a quota period improves the outcome.[671] A practical negotiating method for expensive design-tool seats is to name a price to the representative, stay civil, and be willing to wait a year rather than close, since representatives hold latitude and will return if they can meet the number.[472]

### Perpetual and term licensing

A perpetual licence is a requirement in the professional ECAD market rather than a preference, because a design that has been released must remain openable in the tool version that produced it.[333] Archiving the tool alongside the design at each release is sound engineering practice, and is only possible where a perpetual licence exists.[333] Under perpetual licensing the burden falls on the vendor to justify each upgrade, and the user can decline a direction they dislike by staying on the version they own; under subscription the same user has no lever and absorbs each change.[333] Altium withdrew the perpetual licence in favour of term-based licensing, which users reported as roughly doubling the annualised cost.[671]

### Lock-in and switching costs

Committing to a PCB package is effectively a ten-year decision because the accumulated design corpus is locked into that tool's format, and vendors price and negotiate in the knowledge that the transaction cost of leaving is high.[154] Inside established companies nobody is rewarded for evaluating tools, so a better tool does not displace an incumbent on merit; the investment already sunk into the incumbent decides the outcome.[286] On Charles Alexanian's shop floor, the tool history ran from HighWire through DipTrace and Eagle to Altium, with the move triggered when Eagle went to online subscription and Altium halved its price to capture the displaced users — a competitor's licensing change, not a feature comparison.[429] Altium's licence enforcement watches the client address, so a shop whose internet connection presents several rotating IP addresses triggers licence-compliance contact from the vendor, a practical constraint on network design at the customer site.[429]

The design file format is binary and undocumented, so importers in other tools are written against reverse-engineered structure and cannot be relied upon.[660] Converting boards from Eagle into Altium produced poor results, and the damage persists beyond the conversion because imported library parts carry the defects forward: a component that arrives with twelve unnecessary layers puts those layers on every future board that uses it.[601]

### Access and market position

Altium has supplied university licences for decades, so graduates arrive trained on it; for a small employer that does not hold a seat, this converts into a hiring cost — either buy another expensive seat or retrain the new engineer onto the tool the company owns.[231] The licence cost puts the tool out of reach of an engineer without an employer, which makes capable open-source packages an accessibility requirement rather than a preference.[549] Board complexity, not professional status, is the test for whether the expense is justified; designs at the size and complexity of a Raspberry Pi do not require it.[574] On large designs the money buys automation and polish rather than capability that is otherwise unreachable, and on smaller designs the same automation has little to act on, which is the shape of the buy-or-not decision.[671]

The professional PCB tool market segments by company size and age: long-established larger firms run Cadence, while Altium holds the small and medium segment.[505] Export analytics from a cross-tool component library service put Altium at roughly thirty percent of downloads, Eagle at about twenty-five percent, and KiCad, OrCAD and Allegro at roughly fifteen percent each.[531] Altium dominated Chinese board design for years largely through unlicensed copies, which is why files arriving from that supply chain are overwhelmingly in its format.[685]

## Design workflow

### Libraries and component data

Altium and KiCad place only the schematic symbol at capture time and defer footprint assignment to layout, whereas Eagle binds a package to each device variant in the library; the consequence is that the designer, not the library, owns footprint correctness, and unprepared footprints turn a layout task into library work.[131] Professional-tier tools assume a librarian produces correct part data before schematic capture begins, so the work of getting symbols and footprints in order is front-loaded and typically consumes weeks before layout starts.[131] Altium supports several incompatible approaches to library management and never settled on one, leaving each group to choose a method and enforce it internally.[543] Generating library parts once in a neutral format and exporting per tool works for symbols and ordinary pads but breaks down on features the tools represent differently; slotted holes are the hard case, since Eagle requires the milling layer, some tools have no slotted-hole primitive at all, and KiCad only gained the shape relatively recently.[531]

Maintaining a mechanically accurate library was a staffed function inside Altium, with mechanical engineers and dedicated library staff producing precise 3D models for every part so designers could request a model and receive it within the hour.[508] The tool also includes an IPC footprint generator: the dimensions from the data sheet are entered and the footprint is produced to IPC standards, rather than being drawn by hand or taken from a vendor library.[29] An individual placed instance can have its pads edited without changing the library component, which is fast for prototyping when a nearly-correct footprint needs a slightly larger hole or pad, and dangerous because it silently breaks the correspondence between the known-good library footprint and what is fabricated.[162]

### Schematic-driven flow

The intended method treats the schematic as the control document: part numbers, supplier data and fit/no-fit attributes all live in the schematic and are pushed forward to generate bills of materials in whatever templates are needed, and adopting the method partially yields none of its benefit.[174] Scripting against the tool's bill of materials data allows the whole procurement step to be automated — quantities in, current vendor pricing pulled, purchase orders emitted in each vendor's required template — and run at design time the same pipeline turns a component substitution into an immediate readout of manufacturing cost and lead time.[342]

Reusable schematic blocks are a capability Altium supported and KiCad long lacked, which made block-level reuse a live design decision in one tool and not the other.[645] At Scott Williams's consultancy, whole schematic blocks could be reused but deliberately are not — components are reused but blocks are not — because each application varies the input voltage and output current enough that copying carries a design across without its derivation; traceability and design notes are the stated reason, and the practical reason templates never get built is that billable backlog crowds them out.[645] Reusable blocks reached KiCad in its version 10 previews, closing that gap.[707]

### Layout and rule checking

The design rule system distinguishes via-level clearance from track-level clearance, which is what allows a dense board to be routed without relaxing the track rules globally.[482] Before automatic length matching existed, matched-length routing was done by reading the reported trace length and manually shuffling segments to add or remove the needed distance.[177] On Lukas Henkel's first HDI designs, the 3D stack-up visualisation was used heavily to reason about layer transitions; the need for it falls away once the designer has built an internal model of the stack, so the feature matters most during the transition into high-density work.[681] The enclosure model can be imported and the board inserted into it, and the tool runs a design rule check on the mechanical fit, highlighting a connector that does not line up with its panel cutout.[34]

### Manufacturing outputs

An OutJob is a scripted output definition, and a company-standard OutJob produces an identical set of manufacturing files across every project regardless of who ran it.[434] Because output generation is scripted, a misconfigured OutJob fails silently; in one case a four-layer board was exported with only two layers and the fault was found only after the fabricator's upload preview disagreed with the design.[434] Altium treats plane layers differently from signal layers and emits inner planes as negative images, which some fabricators will not render or accept; the workaround is to build inner planes as flood-filled signal layers instead, which produces positive artwork and avoids the problem entirely.[434] KiCad emits positive artwork even for plane layers, so a four-layer board exported from it does not raise the negative-plane issue at the fabricator.[434] Altium's conception of a board outline layer differs from that of other tools and the outline is typically not contiguous, which fabricators have to accommodate on the receiving end.[299] Fabricator upload tools recognise Altium's Gerber file-extension convention, such as .gbl for bottom copper, and assign layers automatically from the file names.[96]

Two panelisation methods are available and they trade differently: the built-in tool copies the source board file so every layer is duplicated faithfully, while manual copy-and-paste panelisation also works but risks omitting a selection, and design-rule checking a hand-built panel is much harder, so it demands manual verification or a check at the Gerber stage.[400] Release is structured as a procedure rather than a habit: run the design rule check, generate the Gerbers and the bill of materials, then check the design in.[287] Silkscreen bitmap import is not a built-in feature but a long-lived community script, which is representative of how much of the tool's peripheral functionality is delivered: the documented method is to run a script.[209]

### Versioning and collaboration

Schematic and PCB differencing is built into the tool and highlights what changed, which is the capability version control of hardware designs depends on; where it is absent, revision control of a design is impractical.[67] Files written by a newer version can be opened in an older one, a property the vendor maintained for decades and which professional users treat as essential.[523] On the Steam Controller programme, Jeff Keyzer's team froze the CAD version at Altium 12 for the duration, importing a semiconductor-industry practice of locking tool and design-rule versions across a long project so that a defect in the CAD cannot disrupt the schedule.[523] Sharing a complete project — schematic and layout together — through a browser link is used in consulting practice as evidence of prior work when winning a client, without requiring the client to hold a licence.[635]

### Interface stability and upgrade dynamics

The interface overhaul between versions 16 and 19 removed menu items and reorganised the interaction model, returning an expert user to being slow and ineffective; reaching genuine proficiency takes about a year of intensive use, so an interface change of that size is a schedule cost to every established user rather than a preference question.[523] Falling back to an older version as a crutch after an interface change is a decaying strategy: supplier search and manufacturing-parameter features in old versions stop working as distributors change their APIs, and those versions do not receive the updates.[523] SolidWorks holds its interaction model stable across releases, and the contrast grounds the argument that a professional design tool should either preserve its interface or allow the old one to be restored, because a designer earning a living in the tool cannot absorb months of reduced effectiveness.[523] Sales experience inverted the expected difficulty: converting a user from a competing package was easier than persuading an existing user to move to the next version, because the incumbent version's bugs and quirks were already known and worked around.[555]

The in-house hardware group was required to design real products on the latest daily build, so that user-facing defects were found by engineers doing production work rather than by customers.[724] Designing production work on daily builds did occasionally corrupt the file format mid-project, but because the developers were in the same building they wrote conversion scripts on request and no work was lost; the practice is only survivable where that recovery path exists.[213]

## Further reading

- [EAGLE 6 soon](http://www.cadsoftusa.com/eagle-pcb-design-software/new-in-v6/?language=en) — via #67
- [Altium is moving again](http://www.eetimes.com/document.asp?doc_id=1322173) — via #197
- [Dave wrote a forum post translating press release](http://www.eevblog.com/forum/altium/altium-moves-again!/) — via #197
- [CircuitMaker](http://www.circuitmaker.com/#why_circuitmaker) — via #251
- [reduced the price on Circuit Studio, which puts it into competitive territory.](http://www.eevblog.com/forum/eda/circuit-studio-reboot/) — via #306
- [the EAGLE acquisition](https://hackaday.com/2016/06/29/the-eagle-has-landed-at-autodesk/) — via #471
- [PCAD with Accel EDA](https://en.wikipedia.org/wiki/P-CAD) — via #471
- [Protel became Altium](https://en.wikipedia.org/wiki/Altium) — via #471
- [CadSoft EAGLE](https://en.wikipedia.org/wiki/EAGLE_(program)) — via #471
- [Altium365](https://www.altium.com/altium-365) — via #505
- [SnapEDA](https://www.snapeda.com/) — via #531
- [external plugins for Altium and KiCad.](https://www.snapeda.com/plugins/) — via #531
- [Solidworks rebadges Altium as "Solidworks PCB"](https://www.solidworks.com/product/solidworks-pcb) — via #546
- [History of Protel / Altium](https://en.wikipedia.org/wiki/Altium_Designer) — via #659
- [Nick booted out](https://www.eevblog.com/forum/altium/nick-martin-booted-out-as-altium-ceo/) — via #659
- [Altium Buys Morfik in 2010](https://www.edn.com/eeek-altium-is-going-to-buy-morfik/) — via #659
- [Altium bought Octopart in 2017](https://octopart.com/pulse/p/octopart-is-joining-altium-2) — via #659

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 29 | DJ and Jazzy Jeff | https://theamphour.com/the-amp-hour-29-dj-and-jazzy-jeff/ | |
| 34 | AD620, DesignSpark, Instrumentation Amplifier - The Rant Rhetorical | https://theamphour.com/the-amp-hour-34-the-rant-rhetorical/ | March 14, 2011 |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ | |
| 96 | Senseless Saccadic Shemozzle | https://theamphour.com/the-amp-hour-96-senseless-saccadic-shemozzle/ | |
| 118 | Kickstarter, Open Source RC & Modelsource - Facinorous Financial Foulness | https://theamphour.com/the-amp-hour-118-facinorous-financial-foulness/ | October 21, 2012 |
| 131 | An Interview with Andrew Seddon - Necessary Networked Novelty | https://theamphour.com/the-amp-hour-131-necessary-networked-novelty/ | February 4, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 177 | Discussing Innovation and the Future with Mike Ossmann - Fiesty Festivus Futurology | https://theamphour.com/177-discussing-innovation-and-the-future-with-mike-ossmann-fiesty-festivus-futurology/ | |
| 197 | Spacing Out On Space - Dave's Dongle Designing | https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/ | May 5, 2014 |
| 209 | Headless Units and Baseless Batteries - KiCad Kickoff Kopophobia | https://theamphour.com/209-headless-units-and-baseless-batteries-kicad-kickoff-kopophobia/ | July 28, 2014 |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ | |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15, 2014 |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ | January 6, 2015 |
| 242 | Can't We All Just Get Arduino? - Tardiloquent Trademark Tirade | https://theamphour.com/242-cant-we-all-just-get-arduino-tardiloquent-trademark-tirade/ | March 24, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ | July 6, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 333 | Science, Not Silence | https://theamphour.com/333-science-not-silence/ | January 25, 2017 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ | |
| 429 | An Interview with Charles Alexanian | https://theamphour.com/429-an-interview-with-charles-alexanian/ | February 10, 2019 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ | June 30, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ | August 16, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ | December 27, 2020 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 543 | Cassette decks have browsers? | https://theamphour.com/543-cassette-decks-have-browsers/ | May 23, 2020 |
| 545 | Fear of Banjos | https://theamphour.com/545-fear-of-banjos/ | June 6, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ | August 30, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 593 | Publicly Traded Hobby with Ben Jordan | https://theamphour.com/593-publicly-traded-hobby-with-ben-jordan/ | June 14, 2022 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 635 | Low Power Connected Devices with Andrea Longobardi | https://theamphour.com/635-low-power-connected-devices-with-andrea-longobardi/ | June 4, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 659 | Altium...Acquired! | https://theamphour.com/659-altium-acquired/ | February 20, 2024 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 671 | NDA Sideshow | https://theamphour.com/671-nda-sideshow/ | June 19, 2024 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 685 | Data Provenance in the Home, Server, and Fab | https://theamphour.com/685-data-provenance-in-the-home-server-and-fab/ | December 23, 2024 |
| 707 | Welding with an HDMI Cable | https://theamphour.com/707-welding-with-an-hdmi-cable/ | October 26, 2025 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
