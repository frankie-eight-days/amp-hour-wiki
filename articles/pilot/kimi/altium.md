---
title: Altium
concept: altium
generated: 2026-08-08
model: kimi-k3
writer-bakeoff: true
---

Altium is an electronic design automation (EDA) software package for schematic capture and printed circuit board layout, developed by the Australian company of the same name.[659][471] The product descends from Protel, a PCB design tool founded in Tasmania in 1985, and it holds a dominant position among small and medium-sized hardware companies, with market share estimated at roughly 30 percent.[659][505][531] Its high licence cost, pronounced switching costs, and decades-long continuity of file formats and keyboard commands make it a recurring reference point in debates about EDA tool economics and competition from open-source alternatives such as KiCad.[523][154][549]

## History

The company was founded in Tasmania in 1985 by Nick Martin under the name Protel.[659] Protel 99 SE became an industry standard for roughly twenty years and was near-universal in Chinese development houses, to the point that satisfied users would not purchase upgrades, making new licences difficult to sell.[659] The Protel and PCAD product lines, which competed internally, were merged, combining PCAD's PCB strengths with Protel's schematic strengths, and the company rebranded as Altium in the early 2000s.[471] The new name was drawn from a trademark portfolio acquired alongside IBM-originated technology and was chosen because the trademark was already owned, rather than for any intrinsic meaning.[164]

Founder Nick Martin was later removed by the board.[118] The successor strategy emphasised a return to core EDA functionality and away from the company's Internet of Things work.[124] The company pursued a modular-block and all-FPGA design vision in which engineers would no longer lay out boards, a strategy Jones has argued failed because engineering does not compose that way.[267] He has also credited the same FPGA toolchain as technically effective at a high level—vendor-agnostic, with drag-in processor cores and C-to-HDL synthesis—while failing on serious projects.[449]

The company attempted a move to San Jose in the 1990s, relocated research and development to China, and in 2014 relocated again to San Diego, accompanied by an admission that the Internet of Things strategy had failed.[197] US military business was reported lost over the China-based R&D.[197] The relocation to China was abrupt enough internally that Jones, then an employee, learned of it and of his own redundancy only when handed his final pay.[59]

Ben Jordan, who worked at the company, has described uniformly high technical staff quality there, in contrast to previous employers.[593] He has characterised founder Nick Martin's approach as running the company as a hobby rather than to maximise returns, a characterisation Jones has echoed in describing Altium as a publicly traded hobby.[593]

The company was eventually acquired at 68 dollars per share, an increase Jones has deflated against a float price of a few dollars roughly 24 years earlier.[659] Gammell noted that acquisitions of this kind are frequently blocked by regulators.[659] During Jones's earlier employment, shares had fallen to ten cents, a position he has calculated would later have been worth 13.7 million dollars.[659]

## Design and workflow

Altium's intended workflow places all part, supplier, and fit/no-fit data in the schematic and propagates it forward to generated bills of materials; partial adoption of the method yields none of its benefit.[174] An OutJob is a scripted output definition that produces identical manufacturing file sets across projects, making fabrication output reproducible.[434] Because output is scripted, however, a misconfigured OutJob fails silently: in one case a user exported only two layers of a four-layer board without any error being raised.[434]

Altium renders internal plane layers as negative images, which some fabricators reject; the workaround is to implement inner planes as flooded signal layers instead.[434] KiCad generates positive images for plane layers, so the same fabricator issue does not arise in that tool.[434] Altium's board outline layer also differs from other tools' conception of an outline and is typically not contiguous, which fabricators must accommodate.[299]

Schematic and PCB differencing is built into the tool and highlights changes, presented as the requirement for version control on hardware.[67] Files created in newer versions can be opened in older versions, a property described as essential for professional PCB work.[555] The file format proved robust across unstable daily builds, with no corruption of saved work.[543] Keyboard shortcuts and commands were preserved from the 1985 DOS-era Protel releases for roughly three decades.[523]

Altium supports several incompatible approaches to library management and never settled on one, leaving the choice to each user group.[543] Both Altium and KiCad decouple the symbol, footprint, and 3D model from one another, in contrast to an atomic model that binds them to a single manufacturer part number.[508]

## Practice and use

The built-in panelisation tool works but is imprecise enough that manual copy-paste panelisation is often preferred, even by users who hold a licence for the tool.[415]

On the Steam Controller project, Keyzer's team version-locked Altium 12 for the duration of the programme, importing a semiconductor-industry practice of freezing tool versions across long programmes to prevent CAD defects from disrupting schedule.[523] Keyzer has reported that the Altium 17/18 interface overhaul destroyed accumulated expertise, describing the experience of returning to a tool as a former expert and being ineffective, and he has judged much of the interface change unjustified while questioning the aggregate productivity cost to established users.[523]

## Market position

Altium's market share has been estimated at roughly 30 percent, with Eagle near 25 percent and KiCad, OrCAD, and Allegro near 15 percent each.[531] The market segments by company size: larger and older firms run Cadence tools, while Altium holds the small and medium company segment.[505] Gammell has described Altium as effectively the only option for small consumer-hardware companies.[505] Jones has characterised the competitive landscape as Altium and everyone else.[482] In Australia, Altium has for decades dominated student licensing, producing a cost problem when employers hire graduates trained exclusively on it.[231]

## Adjacent products

Altium released CircuitMaker, a free tool that was cloud-only with no local file saving. Jones predicted it would fail, and later identified the abandonment risk inherent in a free cloud tool with no revenue model.[216][251] Gammell declined to adopt it, citing KiCad as a permanently free alternative.[216] Circuit Studio, a lower-priced offering, has been rated good value at its price point, though it was made deliberately incompatible with Altium Designer to prevent firms substituting cheap seats for full licences.[316]

## Reception and debate

### Cost and value

Licence pricing has been reported at roughly 5,000 dollars initially with 1,500 to 2,000 dollars annually for maintenance.[574] Jones has declined to buy a licence at five to six thousand dollars, having ceased daily layout work, and has stated he will not purchase a full licence because he does not need one.[277][306] He sets board complexity as the test, holding that Raspberry Pi-class designs do not require the tool.[574] Gammell has justified the cost by billable time, having migrated from Eagle when fighting the tool began consuming hours; a single day of output-generation trouble avoided repays the difference.[537] Shrouk El Attar has noted that the licence is unaffordable without an employer, framing open-source alternatives as an accessibility requirement.[549]

### Switching costs and tool choice

Gammell has argued that the decisive property of an EDA package is switching cost: adoption is effectively a ten-year commitment because the existing design corpus is locked into the format, and vendors are aware of this.[154] Keyzer has characterised EDA tool choice as a matter of allegiance rather than evaluation, and attempts to convert users as unproductive.[472] Gammell abandoned advocating tool changes on the grounds that the decision is made on willingness to pay rather than features, and has held that tool changes require an external trigger such as leaving a job and its licence, noting the circularity of learning a tool speculatively to win contracts that require it.[298][306] Charles Alexanian has described migrating to Altium when Eagle moved to subscription licensing and Altium halved its price to capture the displaced users.[429]

### Competition from KiCad

Jones has held that KiCad is not yet a professional-grade tool and remains far from challenging Altium in high-end PCB work.[555] Gammell has responded that the assessment rests on outdated familiarity, while allowing it may have been correct when formed.[555]

### Corporate conduct and commentary

Jones has reported that Altium delayed a product launch after a critical video, revising its direction.[213] He has stated that the company signalled publicly a willingness to be acquired, with long-standing unfixed defects—bugs in some cases twenty years old—cited as the one argued benefit of a potential Autodesk takeover.[546] After fourteen years of commentary on the company, he has stated a loss of interest in it, and he has reported no longer receiving a licence from the company.[546][627]

## Further reading

- [EAGLE 6 soon](http://www.cadsoftusa.com/eagle-pcb-design-software/new-in-v6/?language=en) — via #67
- [Altium is moving again](http://www.eetimes.com/document.asp?doc_id=1322173) — via #197
- [Dave wrote a forum post translating press release](http://www.eevblog.com/forum/altium/altium-moves-again!/) — via #197
- [CircuitMaker](http://www.circuitmaker.com/#why_circuitmaker) — via #251
- [the backwards nature of the EDA industry](http://www.boldport.com/blog/2013/09/engineers-assemble.html) — via #267
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

| Episode | Title | URL |
|---------|-------|-----|
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ |
| 118 | Kickstarter, Open Source RC & Modelsource - Facinorous Financial Foulness | https://theamphour.com/the-amp-hour-118-facinorous-financial-foulness/ |
| 124 | SpaceX, Enclosures & Startups - Urging Unemployment Ullagone | https://theamphour.com/the-amp-hour-124-urging-unemployment-ullagone/ |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ |
| 197 | Spacing Out On Space - Dave's Dongle Designing | https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/ |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ |
| 267 | Standing With Ahmed | https://theamphour.com/267-standing-with-ahmed/ |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ |
| 429 | An Interview with Charles Alexanian | https://theamphour.com/429-an-interview-with-charles-alexanian/ |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ |
| 543 | Cassette decks have browsers? | https://theamphour.com/543-cassette-decks-have-browsers/ |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ |
| 593 | Publicly Traded Hobby with Ben Jordan | https://theamphour.com/593-publicly-traded-hobby-with-ben-jordan/ |
| 627 | Works on my machine | https://theamphour.com/627-works-on-my-machine/ |
| 659 | Altium...Acquired! | https://theamphour.com/659-altium-acquired/ |
