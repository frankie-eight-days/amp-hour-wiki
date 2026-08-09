---
title: EAGLE
concept: eagle
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**EAGLE** is a proprietary electronic design automation program for schematic capture and printed circuit board layout, developed originally by a German company and subsequently owned in turn by an electronics distributor and a mechanical CAD vendor.[306] A free edition limited to two layers, a single schematic sheet and a bounded board size made it the default design tool of the open hardware community, whose shared component libraries then entrenched that position.[366][333][49] The standalone product was eventually discontinued in favour of the electronics module inside its acquirer's mechanical CAD package.[636]

## Licensing and pricing

The free edition of EAGLE is limited by board geometry rather than by output quality: designs are restricted to two copper layers and a single schematic sheet within a bounded board area, but the files it produces carry no watermark and are not otherwise crippled.[366] The size limit is dimensional rather than computed by area, so a long, thin board whose total area is smaller than the permitted rectangle still exceeds the free licence and forces a paid upgrade.[191] The licence tiers step steeply: exceeding two layers or the free board size costs several hundred dollars, and the unrestricted edition ran to a thousand dollars or more, arithmetic that determines whether a hobby project can grow inside the tool.[191]

Commercial use requires a paid licence at any scale, which prevents a design produced in the free edition from being straightforwardly reproducible by anyone who receives its files.[213] One proposed test of whether a published design is genuinely open is whether one other person anywhere can build it; under that test, a design whose files can only be opened by buying an expensive licence fails regardless of what licence terms are attached to it.[213] A rival free offering took the opposite approach to its free tier, imposing no size or layer restrictions at all but requiring that every project be made public, trading a geometric constraint for a disclosure one.[251]

## Market position

The vendor's own position was that EAGLE did not compete with high-end packages and deliberately served the low end of the market, a positioning consistent with what practitioners encounter when routing large ball-grid-array parts that need many layers.[19] The free edition is what made the tool the default in open hardware, and the community libraries that grew on top of it are what kept designs there afterwards.[333] Free tools without size limits subsequently appeared and did not displace it, because entrenchment in an existing user base and its libraries outweighs a better free tier for designers who already hold designs in a format.[49]

One component-library service reported its downloads running at roughly 30 percent for the leading professional tool, about 25 percent for EAGLE, and around 15 percent each for three other packages, a proxy for what designers actually have installed.[531] At Laen's low-volume board house, the incoming order mix inverted over a few years: almost entirely EAGLE at the outset with a small share of the open-source alternative, then the open tool rising to around three quarters, and later a broader mix as professional firms began sending boards.[149] Both EAGLE and the leading professional package carry high unlicensed use, with the professional package effectively the standard in one large market almost entirely without payment.[149] A mid-priced competitor positioned at three to four thousand dollars occupied what was described as "the no man's land of CAD pricing" between the free tier and the professional tools, attracting neither, and was later cut to nine hundred and ninety-five dollars with a hundred and twenty-five dollar annual maintenance fee.[306]

Inside large companies holding only a handful of floating seats of the official tool, engineers use the cheap package for small adapter boards, because going through the sanctioned channel can take weeks merely to have a footprint defined.[472] Equipment vendors integrate with whichever tool holds the hobby market: one desktop milling machine shipped software that went directly from EAGLE files to board routing, because that was where its customers' designs already were.[199]

## Capabilities and limitations

The tool changed remarkably little across roughly fifteen years: a licence holder from 2010 found the current release essentially the same product, with awkward operations such as changing annular ring sizes on a per-component basis still unaddressed.[523] Dense boards carrying two or three ball-grid-array packages have been built in it, so the constraint at the high end is effort rather than capability; four-layer work is possible but is the hard way to do it.[162] Design rule checking is not enforced as part of the flow, so a board can be sent to fabrication without ever having been checked, a class of error the tool does not prevent.[347]

### Autorouting

Autorouting effort is dominated by setup rather than by the run: roughly nine tenths of the work is configuring constraints and one tenth is pressing the button and tidying afterwards, and there is a case that a low-end package should spend its development effort on the layout editor instead.[46] An external open-source, web-based router exists that links into EAGLE and several other packages as their autorouter, so the capability does not have to be built into each tool.[203] A single-connection routing command was later added deliberately as groundwork rather than as a general autorouter: once one connection can be routed and length-tuned on command, a rip-up-and-reroute-device command becomes possible, and from there a mechanical engineer moving a connector can have the affected connections rerouted automatically.[471]

## Libraries and footprints

Bundled footprints are the tool's weakest component: the supplied library parts are oversized and unreliable enough that experienced users generate essentially all of their own footprints by hand.[29] The standards body's recommended land patterns follow a formula based on the component's geometry together with the statistical variation of placement accuracy, which can be reduced to a spreadsheet for chip resistors and capacitors; anything more complex sends the designer back to a generator or to the specification itself.[29] A defective footprint in a widely copied library propagates into assembly defects: one 0402 land pattern from the standard library produced tombstoning and head-in-pillow failures at a contract assembler often enough that the assembler wrote and circulated a corrected replacement.[411]

EAGLE's library model binds a package to each device variant, so choosing a part in the schematic already fixes its footprint, whereas other tools carry only the symbol into the schematic and assign the footprint at layout; the same librarian work happens either way, but at different points in the flow.[131] At SparkFun, where the vendor maintains a public library, user-contributed parts are accepted by pull request, which is what keeps coverage current for boards old enough that their components were never added.[157] Generating library parts in a neutral format and exporting per tool works for ordinary symbols and pads but breaks on features the tools represent differently; slotted holes are the hard case, and in EAGLE they must be drawn on the milling layer because the program has no slotted-hole primitive at all.[531]

## File format and interoperability

The move to an open XML file format was the change that made EAGLE design data portable, because other tools could then read it directly rather than through reverse-engineered importers.[106] That portability allowed competing tools to accept the files natively, and by the time one open-source tool reached its fifth version its import was solid enough to bring in whole projects including libraries.[251] In practice conversion still fails in specific ways: an import of a published design produced errors and left power planes unconnected, and users have written their own import scripts to work around gaps in the supplied one.[530] A perfect importer is not to be expected; conversion work that does not appear in redrawing appears instead in verifying that what came across is correct.[380] Import damage also persists beyond the conversion, because the library comes across with the design: a component that arrives carrying twelve layers it does not need puts those layers on every future board that uses it.[601] Older designs can become unopenable as versions move on, which is the archival argument for keeping the tool that produced a design alongside the design itself.[442]

Starting a derivative board from a published design's own files rather than from its documentation removes a class of error, because header positions and board outline taken directly from the source design cannot be transcribed wrongly.[378] Assembly services can extract most of what they need from the native files of EAGLE and the other common tools, but at Macrofab, paste aperture centres for a dispenser are a separate output that the design files do not directly provide.[243]

## Development under later ownership

Under Matt Berggren, the interface was reorganised from grouping commands by kind to ordering them by workflow — set up layers, define the board outline, place components, route them, pour polygons, then rip up and rework — arranged left to right in the order most users proceed.[471] Electrical and mechanical integration was built by inserting the board into the mechanical model's timeline as a sketch that is then extruded into the board shape, rather than by exchanging static geometry through a neutral format; the difference matters because downstream mechanical operations recalculate when the board changes.[471] Reusable schematic blocks were added in response to the observation that engineers solve the same small problems repeatedly in isolated environments with no way to pass the solutions between them, a design-reuse emphasis Berggren pulled into the program.[611]

## Ownership and discontinuation

Ownership moved twice: the distributor that had bought the original German company sold it on for a reported figure in the region of twenty million dollars, after which it passed to a mechanical CAD vendor.[306] The move to online subscription licensing caused Charles Alexanian's working shop to leave, and a competitor cut its price sharply at the same moment specifically to capture users displaced by the licensing change, so that switch was driven by a competitor's terms rather than by a feature comparison.[429] The withdrawal of the perpetual licence was the specific trigger for Dave Young's consultancy to move its new work elsewhere while deliberately retaining the old licence to support legacy designs.[601]

The end state was announced years later: the standalone product was discontinued in favour of the electronics module inside the acquirer's mechanical CAD package, which descends from it, with disagreement among practitioners about how much of the original code carried over as against a rewrite.[636] A mechanical CAD vendor acquiring an electronics tool has no interest in serving a hobby market, which is the structural reason such a product gets folded into a larger suite rather than kept as a cheap standalone.[636]

## Migration and legacy practices

The standard practice for retired toolchains is to freeze the old tool with the old work: keep the perpetual licence and the designs it produced together as an archive, and send only new projects to the replacement tool, rather than attempting to convert a back catalogue.[333] Changing design tools is not a decision made on a whim; it usually requires an external trigger such as leaving a job and the licence behind, because the relearning cost falls entirely on the designer.[306] The cost of switching is a deliberate period of reduced output: an experienced user opening the alternative finds nothing where expected, and the change only happens if the designer accepts that performance hit knowingly.[555]

Vincent Himpe held the opposing position on tool economics — that a free base version from any vendor is adequate to get a board made is true, but time spent troubleshooting a tool's own defects is time not spent on the board — and bought a professional licence at twenty-five hundred dollars, justified against revenue from books whose boards it produced.[169] The upgrade case elsewhere is made on time rather than features: one team doing four-layer flex work, bill-of-materials management and scripted output generation found the hours lost fighting the tool exceeded the price difference, switching at a point where the cheaper package cost about eight hundred dollars against roughly twenty-two hundred a year for the professional one.[537]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 19 | CAD programs, Systems Design and Renewable Energy | https://theamphour.com/the-amp-hour-19-cad-programs-systems-design-and-renewable-energy/ | |
| 29 | DJ and Jazzy Jeff | https://theamphour.com/the-amp-hour-29-dj-and-jazzy-jeff/ | |
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ | |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 131 | An Interview with Andrew Seddon - Necessary Networked Novelty | https://theamphour.com/the-amp-hour-131-necessary-networked-novelty/ | February 4, 2013 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 157 | An Interview with the SparkFun Team - Efficacious Engineering Ensemble | https://theamphour.com/the-amp-hour-157-efficacious-engineering-ensemble/ | August 5, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 199 | The 2014 Maker Faire Show - Traveling Technology Trangam | https://theamphour.com/199-the-2014-maker-faire-show-traveling-technology-trangam/ | May 19, 2014 |
| 203 | Tesla, Checklists and Bullies - Emerging External Eupsychics | https://theamphour.com/203-tesla-checklists-and-bullies-emerging-external-eupsychics/ | June 16, 2014 |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ | |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ | July 6, 2016 |
| 333 | Science, Not Silence | https://theamphour.com/333-science-not-silence/ | January 25, 2017 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 380 | Just Terrestrial and Space Things | https://theamphour.com/380-just-terrestrial-and-space-things/ | February 18, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 429 | An Interview with Charles Alexanian | https://theamphour.com/429-an-interview-with-charles-alexanian/ | February 10, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ | December 27, 2020 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15, 2021 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ | April 5, 2021 |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ | August 30, 2021 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 611 | Grad School Time Capsule with Joshua and Zach | https://theamphour.com/611-grad-school-time-capsule-with-joshua-and-zach/ | December 4, 2022 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
