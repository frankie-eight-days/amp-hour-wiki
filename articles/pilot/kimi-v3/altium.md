---
title: Altium
concept: altium
generated: 2026-08-08
model: kimi-k3
spec: knowledge-only-v3
---

Altium Designer is a professional printed-circuit-board EDA package descended from Protel, founded in Tasmania in 1985 by Nick Martin.[659] The Altium name followed a merger of the internally competing Protel and PCAD product lines, combining PCAD's PCB strengths with Protel's schematic strengths, in a rebranding of the company in the early 2000s.[471] Protel 99 SE remained an industry standard for roughly twenty years and was near-universal in Chinese development houses, to the point that satisfied users would not buy upgrades and salespeople found new licenses difficult to sell.[659] Keyboard shortcuts and commands were preserved from the 1985 DOS-era Protel releases for roughly three decades.[523]

Altium's intended workflow places all part, supplier and fit/no-fit data in the schematic and propagates it forward to generated bills of materials; applying the method partially yields none of its benefit.[174] The tool decouples symbol, footprint and 3D model rather than binding them to a single manufacturer part number in an atomic component model, an approach it shares with KiCad.[508]

## Output generation and fabrication

An OutJob is a scripted output definition that produces identical manufacturing file sets across projects, making fabrication output reproducible.[434] Because output is scripted, a misconfigured OutJob fails silently: in one instance two layers of a four-layer board were exported without any error being raised, and the misconfiguration took time to identify.[434]

Altium renders internal plane layers as negative images, which some fabricators reject; the workaround is to implement inner planes as flooded signal layers instead.[434] KiCad generates positive images for plane layers, so the same fabricator issue does not arise there.[434] Altium's board outline layer also differs from other tools' conception of an outline and is typically not contiguous, which fabricators must accommodate.[299]

The built-in panelisation tool works but is imprecise enough that manual copy-paste panelisation is often preferred, including by users who hold a licence for the tool.[415]

## Versioning, file format, and libraries

Schematic and PCB differencing is built into the tool and highlights changes, providing the diff capability required for version control on hardware designs.[67] Files created in newer versions can be opened in older versions, a property treated as essential for professional PCB work.[555] The file format proved robust across unstable daily builds, with no corruption of saved work.[543]

Altium supports several incompatible approaches to library management and never settled on one, leaving the choice to each user group.[543]

## Version policy on long programmes

On the Steam Controller project, Keyzer's team version-locked Altium 12 for the duration of the programme, importing a semiconductor-industry practice of freezing tool versions across long programmes to prevent CAD defects from disrupting schedule.[523] Keyzer has reported that the Altium 17/18 interface overhaul destroyed accumulated expertise, returning a former expert to ineffectiveness in the tool, and he has judged much of the interface change unjustified given the aggregate productivity cost to established users.[523]

## Cost, lock-in, and selection

The decisive property of an EDA package is switching cost: committing to a package is effectively a ten-year decision because the existing design corpus is locked into the format, and vendors are aware of this.[154] Pricing has been reported at roughly 5,000 dollars initially with 1,500 to 2,000 dollars annually for maintenance.[574] The cost is justified against billable time: one practitioner migrated from Eagle when fighting the tool began consuming hours, and a single day of output-generation trouble avoided repays the difference.[537] Board complexity is the applicable test; Raspberry Pi-class designs do not require the tool.[574]

Market share has been estimated at roughly 30 percent for Altium and 25 percent for Eagle, with KiCad, OrCAD and Allegro near 15 percent each.[531] The market segments by company size: larger and older firms run Cadence, while Altium holds the small and medium segment.[505] Altium has held decades-long dominance of Australian student licensing, which creates a hiring-side cost problem when graduates arrive trained only on a tool the employer does not own.[231]

## Adjacent products

CircuitMaker is a free cloud-only tool with no local file saving; the risk of a free product with no revenue model is that its vendor's board of directors can discontinue it at any time.[216][251] Circuit Studio is deliberately incompatible with Altium Designer to prevent firms substituting cheap seats for full licences; it offers good value at its price point.[316]

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
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ |
| 543 | Cassette decks have browsers? | https://theamphour.com/543-cassette-decks-have-browsers/ |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ |
| 659 | Altium...Acquired! | https://theamphour.com/659-altium-acquired/ |
