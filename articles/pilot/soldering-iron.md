---
title: Soldering iron
concept: soldering-iron
episodes: 109
guests: 45
explains: 12
opinion: 14
generated: 2026-08-08
model: claude-opus-5 (pilot batch, pipeline steps 6-8)
---

<!--
PRODUCTION NOTES (not for readers)
Gather: 147 census mentions across 109 episodes -> 42 pinned explains/opinion
passages after paragraph-level dedupe. NOT capped (cap is 150).
Re-grade: census reported 17 explains / 25 opinion; re-graded to 12 / 14. Sixteen
passages discarded - most were the soldering iron appearing as scenery in a story
about something else (a logo description, a MacGyver'd 24V supply, a guns tangent),
which the census graded "explains" on keyword proximity alone. Thin concept: 109
episodes mention an iron, few stop to teach one. Article is short because the data
is short.
Evidence packet: _packets/soldering-iron.json (39 claims, 3 disagreement groups).
DROPPED FOR ATTRIBUTION: ep 158 (speaker is the placeholder SPEAKER_01), ep 38
(labels suspect and content contradicts the label), and one anecdote from "The
Chinese Clairvoyancy", which has no episode number and so cannot be cited.
One claim in the packet is marked unattributed: ep 288 fuses both hosts' turns in
a single paragraph, so the service-life framing cannot be assigned to either.
-->

The soldering iron is the hand tool for forming and reworking solder joints. Technique guidance around it is sparse and largely settled, while purchasing advice is contested across the full price range. Two substantive technical claims recur — that bench tip temperatures of 700-800 °F are correct despite reflow profiles specifying far lower peaks, because a hand iron must compensate for heat conducted away from the joint,[183] and that cartridge and induction irons achieve fast readiness by shutting down in the cradle rather than idling hot.[528] The equipment consensus is narrow: temperature control is the threshold below which results suffer and above which they largely do not improve,[413] and spending past four figures is treated as outside hobbyist scope.[528][606]

## Technique

The standard joint is formed by heating the pad and lead with the tip and feeding solder to both, rather than melting solder onto the tip first.[329] The characteristic beginner failure is attempting to hold component, board, iron and solder at once instead of preparing the work and relying on heat transfer.[413] Flux is typically learned late, and neglecting it produces intermittent joints rather than obvious failures, which is what makes the lesson slow to arrive.[137]

Hand-soldering temperature is the most common source of confusion. Reflow profiles in component datasheets specify peaks far below normal iron settings, but the two numbers describe different processes: the profile governs mass reflow, whereas a hand iron must compensate for heat conducted away from the joint. Tip temperature is not joint temperature.[183]

Thermal mass determines tool selection. Desoldering older through-hole assemblies calls for a high-wattage iron,[110] and legacy tip-over-element irons remain adequate for low-thermal-mass work while falling short on heavier joints, which is the case for cartridge tips.[716] Where an oversized component covers its own pad, heat is applied to the lead so that the pad is heated through it.[488]

Two irons are treated as the working minimum, since opposing irons at either end of a part allow it to be lifted off.[528][534]

An iron is not the surface-mount tool most newcomers assume. The belief that surface-mount assembly requires one makes the process appear more intimidating than it is, when [[solder-paste]] methods are substantially easier for a beginner — the step that removes the iron from the process entirely being reflow, whether by [[pick-and-place-machine]] line or hotplate.[454] The same distinction governs one board-design decision: castellated edge headers earn their cost only for builders working with an iron rather than hot air.[723]

## Equipment

Cartridge and induction irons are driven by an RF amplifier and shut down while seated in the cradle, reheating fast enough to be ready by the time the iron reaches the work.[528] Temperature in these systems is a property of the tip rather than of a controller, so a purchase selects a tip geometry and a temperature band, with at least one manufacturer encoding the band as a colour.[528] The consequence is that several working temperatures require several tips, since there is no controller to adjust.[528]

Tip life and thermal performance are opposed design goals, determined by the cladding material and the thermal resistance it adds; manufacturers target one or the other rather than both.[528]

## Market and purchasing debate

Whether equipment quality changes a beginner's results was argued directly and resolved narrower than either opening position. Chris Gammell credited decent gear for good results, contrasting it with the low-end irons most people start on; Dave Jones rejected the framing outright.[413] Gammell then narrowed the claim to a floor rather than a ceiling — the problem case being an abused event iron that no longer melts solder reliably — and Jones conceded exactly that much, holding that any temperature-controlled iron performs equivalently above it.[413]

At the top of the market Gammell and Jones agree, and neither buys. Gammell treats the thousand-dollar tier as out of scope on price alone,[528] and Jones reached the same verdict about a high-wattage Hakko at roughly a thousand US dollars.[606] They differ on the middle: Gammell defends a Metcal-clone Thermaltronics iron as the one above-average bench purchase he would repeat.[606] Asked to advise on a $300 iron, Jones ranked the premium field with JBC at the top of the price range,[288] and the same exchange reframed the decision as one of intended service life rather than price.[288]

The sharpest disagreement is with an outside voice. Dave Jones ran a Hakko-versus-Weller comparison of conventional irons and defended the classics as still worth buying; Louis Rossmann responded publicly that the technology is obsolete and that a Shenzhen clone of the newer cartridge type is preferable to a genuine older design at the same price. Jones conceded the argument holds specifically for high-throughput repair work.[384]

The iron also serves as a benchmark for tolerable software churn, both in a relayed comparison of software frameworks against the iron as the more stable of the two,[407] and in the rhetorical question of whether firmware updates would be tolerated on one — to which the answer is that USB-connected irons shipping firmware updates already exist.[298]

## Chronology

Through 2012 the reference bench iron was the Hakko 926 and its 936 successor, displaced by the FX888; the analog knob-controlled model was discontinued in favour of the digital FX888D, a change objected to on ergonomic rather than nostalgic grounds, the digital readout being acceptable and the loss of a knob not.[122] By 2021 cartridge tips had become the default for new purchases, and the earlier argument about controls had disappeared entirely.[528] By 2023 the low-cost floor had dropped to a $30 USB-powered portable iron judged to work acceptably, a category that had by then developed competing partisan followings.[633]

## Notable instances

A soldering contest at Toorcamp was deliberately run on poor-quality irons, the point being to demonstrate what is achievable with the worst available tool.[410] Against the upgrade treadmill, twenty legacy irons remain in teaching service, low-thermal-mass student work being the case where old tip technology holds up.[716]

Two career notes attach to the tool directly: Ian Johnston left a non-electronics desk job to return to repair work, citing the iron specifically — "I missed the soldering iron. That's what it basically came down to."[643] Sam Zeloof, describing the background preceding garage semiconductor fabrication, dated it to "since I could walk, basically, I've had a soldering iron in my hand".[390]

## Further reading

- [Hakko has decided to retire the FX-888](http://www.eevblog.com/forum/general-chat/hakko-fx-888-soldering-station-discontinued/) — via #122
- [Curious Inventor videos on YouTube](https://www.youtube.com/user/CuriousInventor) — via #183
- [There was a soldering competition at IP capex Expo](http://www.ipcapexexpo.org/html/expo/hand-soldering-competition-championship.htm) — via #410
- [IPC standard pad sizes](https://electronics.stackexchange.com/questions/244475/ipc-specification-for-pad-width-vs-pin-width-smd) — via #488
- [The Pine-cil soldering iron](https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/) — via #633

## References

| Ep | Title | URL | Date |
|---|---|---|---|
| 110 | Armstrong, Camenzind & Museums - Outstanding Oneirophoros Obituaries | https://theamphour.com/the-amp-hour-110-outstanding-oneirophoros-obituaries/ | August 26th, 2012 |
| 122 | Processors, CEOs & Soldering irons - Plentiful Perfunctory Programs | https://theamphour.com/the-amp-hour-122-plentiful-perfunctory-programs/ | November 19th, 2012 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19th, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3rd, 2014 |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ | February 24th, 2016 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11th, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ | 2017 |
| 384 | A++++++ Will Buy Again | https://theamphour.com/384-a-will-buy-again/ | 2018 |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ | April 29th, 2018 |
| 407 | Gregory Charvat and Three New Companies | https://theamphour.com/407-gregory-charvat-and-three-new-companies/ | September 16th, 2018 |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ | October 7th, 2018 |
| 413 | A House of FR4 | https://theamphour.com/413-a-house-of-fr4/ | October 28th, 2018 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 488 | Sowing Discord | https://theamphour.com/488-sowing-discord/ | April 12th, 2020 |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ | January 31st, 2021 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14th, 2021 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23rd, 2022 |
| 633 | Engineering Optimization | https://theamphour.com/633-engineering-optimization/ | May 22nd, 2023 |
| 643 | Calibration & Repair with Ian Johnston | https://theamphour.com/643-calibration-repair-with-ian-johnston/ | August 22nd, 2023 |
| 716 | Electronics Manufacturing History with David Ray | https://theamphour.com/716-electronics-manufacturing-history-with-david-ray/ | 2026 |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ | May 7th, 2026 |
