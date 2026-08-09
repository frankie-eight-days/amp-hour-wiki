---
title: Soldering Iron
concept: soldering-iron
generated: 2026-08-08
model: kimi-k3
writer-bakeoff: true
---

The soldering iron is the hand tool used to melt solder and form electrical and mechanical joints between components and circuit boards. Although its operation is simple in principle, effective use depends on understanding heat transfer, thermal mass, and the distinction between tip temperature and joint temperature, all of which are common sources of beginner error.[183][329] The tool occupies a durable position in electronics practice, and it is frequently invoked as a benchmark of technological stability against the rapid churn of software tooling.[298][407]

## Joint technique

The standard technique for forming a joint is to place the tip against both the pad and the component lead and then feed solder into the heated joint, rather than melting solder onto the tip first and carrying it to the work.[329] The characteristic beginner failure is attempting to hold the component, the board, the iron, and the solder simultaneously, instead of preparing and securing the work so that the hands are free to control heat and solder feed.[413]

Where an oversized component covers its pad, the technique adapts: heat is applied to the lead so that the pad beneath is heated through it.[488]

Flux is frequently learned late by self-taught practitioners, and neglecting it produces intermittent rather than obvious failures, which makes the omission difficult to diagnose.[137]

## Temperature and thermal mass

A persistent point of confusion concerns the apparent contradiction between hand-soldering tip temperatures of 700–800 degrees Fahrenheit and reflow profiles that specify far lower peak temperatures, on the order of 450 degrees. This is the most common question beginners raise about soldering temperature.[183] The resolution is that a reflow profile describes mass reflow of an entire assembly, whereas a hand iron must compensate for heat conducted away from the joint during the soldering operation; tip temperature is not joint temperature.[183]

Thermal mass determines the required tool. Desoldering older through-hole assemblies calls for a high-wattage iron, on the order of 100 watts, because the joint must be brought to temperature against substantial copper mass.[110] Legacy tip-over-element irons perform adequately on low-thermal-mass work but not on high-thermal-mass joints, a limitation that cartridge tips address.[716]

## Tip technology

Two broad tip architectures are in use. In conventional designs, the tip sits over a separate heating element and a controller regulates temperature. In cartridge systems, the heating element and sensor are integrated into the tip itself, and temperature is a property of the tip rather than of the controller: the purchase selects a tip type and a temperature band, which Thermaltronics encodes as a colour.[528] Cartridge and induction irons are driven by an RF amplifier and shut down automatically when returned to the cradle, reheating quickly enough to be ready by the time the iron reaches the work.[528]

The fixed-temperature design means that multiple working temperatures require owning an array of tips, since there is no temperature control on the station itself.[528] Tip design also involves an inherent trade-off: tip life and thermal performance are opposed goals, set by the cladding material and the thermal resistance it adds, and manufacturers target one or the other rather than both.[528]

## Working practice

Two irons are treated as the working minimum on an equipped bench, because opposing irons applied to either end of a surface-mount part allow it to be lifted off the board cleanly. The recommendation has been restated flatly: a practitioner should not have only one iron.[528][534]

Surface-mount assembly is widely and wrongly assumed to require an iron, which makes it appear more intimidating to newcomers than it is; solder-paste methods, whether hot air or reflow, are substantially easier for beginners.[454] This assumption has consequences in board design: castellated edge headers provide value only to builders working with an iron rather than hot air, which is why some designs omit them.[723]

## History and market development

The Hakko 926 and 936 were long-lived bench standards; the FX888 succeeded them, and the analog knob-controlled variant was eventually discontinued in favour of the digital FX888D.[122] The discontinuation drew objection on ergonomic rather than nostalgic grounds—the digital readout was accepted, but the loss of a physical adjustment knob was not.[122]

By 2021, cartridge tips had become the default for new purchases among working practitioners.[528] At the low end, the market shifted as well: a 30-dollar USB-powered portable iron was found to work acceptably, and the low-cost portable category developed competing partisan followings.[633] USB-connected irons with firmware updates have also appeared, complicating the tool's traditional status as update-free equipment.[298]

## Reception and debate

### Does equipment quality matter for beginners?

Whether a better iron makes a beginner produce better joints is contested. Chris Gammell has argued that equipment quality affects beginner outcomes, contrasting decent gear with the low-end irons most people start on.[413] Dave Jones has rejected the claim that a good iron explains good results, attributing outcomes to skill.[413] The exchange converged on a narrower position: Gammell reduced his claim to a floor rather than a ceiling, the problem case being an abused iron that no longer melts solder reliably, while Jones conceded that temperature control is the threshold requirement, above which equipment differences do not change results.[413]

### Conventional versus cartridge technology

A related dispute concerns whether conventional temperature-controlled irons remain worth buying against inexpensive clones of newer cartridge technology. Jones conducted a Hakko-versus-Weller comparison of conventional irons and defended the classic designs as still worth buying.[384] Louis Rossmann argued in a public response that conventional irons are obsolete and that a clone of the newer cartridge technology is preferable to a genuine older design at the same price.[384] Jones conceded that the counter-argument holds specifically for high-throughput repair work, where tip-change speed and thermal recovery dominate.[384]

### Market tiers and spending

Practitioners broadly agree that the top of the market is out of scope for non-professionals on price alone, with thousand-dollar stations—including a high-wattage Hakko—judged unsuitable for hobbyist purchase.[528][606] The mid tier has defenders: Gammell names a Metcal-clone Thermaltronics iron as the one above-average bench purchase he considers justified.[606] Jones has ranked the premium field for buyers considering a roughly 300-dollar iron, placing JBC at the top of the price range with Weller as a sound choice below it, and has reframed the purchase decision as one of intended service life—whether the tool is meant to be a ten-year, five-year, or two-week iron—rather than price as such.[288]

## In practice and culture

The tool's forgivingness relative to its reputation has been demonstrated deliberately: a soldering contest at Toorcamp was run on poor-quality irons, the point being to show the results achievable with the worst available tool.[410] Legacy irons also remain in active service; David Ray keeps twenty legacy tip-over-element irons in use, three of them on his bench, and employs them for teaching, low-thermal-mass student work being the case where old tip technology remains adequate.[716]

The soldering iron also functions as a cultural reference point within electronics. Bunnie Huang has compared software frameworks with the soldering iron, the iron being the more stable of the two.[407] The iron serves as the benchmark for tolerable software churn in the rhetorical question of whether practitioners would accept soldering irons that required updates—an obligation that has since partially arrived with USB-connected, firmware-updatable models.[298] For individual practitioners the tool carries personal weight: Ian Johnston left a non-electronics desk job to return to repair work, citing the soldering iron specifically, and Sam Zeloof describes a lifelong hands-on background, with an iron in hand since childhood, preceding his garage semiconductor fabrication work.[390][643]

## Further reading

- [Hakko has decided to retire the FX-888](http://www.eevblog.com/forum/general-chat/hakko-fx-888-soldering-station-discontinued/) — via #122
- [Curious Inventor videos on YouTube](https://www.youtube.com/user/CuriousInventor) — via #183
- [There was a soldering competition at IP capex Expo](http://www.ipcapexexpo.org/html/expo/hand-soldering-competition-championship.htm) — via #410
- [The Pine-cil soldering iron](https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/) — via #633
- [IPC standard pad sizes](https://electronics.stackexchange.com/questions/244475/ipc-specification-for-pad-width-vs-pin-width-smd) — via #488

## References

| Episode | Title | URL |
|---------|-------|-----|
| 110 | Armstrong, Camenzind & Museums - Outstanding Oneirophoros Obituaries | https://theamphour.com/the-amp-hour-110-outstanding-oneirophoros-obituaries/ |
| 122 | Processors, CEOs & Soldering irons - Plentiful Perfunctory Programs | https://theamphour.com/the-amp-hour-122-plentiful-perfunctory-programs/ |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ |
| 384 | A++++++ Will Buy Again | https://theamphour.com/384-a-will-buy-again/ |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ |
| 407 | Gregory Charvat and Three New Companies | https://theamphour.com/407-gregory-charvat-and-three-new-companies/ |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ |
| 413 | A House of FR4 | https://theamphour.com/413-a-house-of-fr4/ |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ |
| 488 | Sowing Discord | https://theamphour.com/488-sowing-discord/ |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ |
| 633 | Engineering Optimization | https://theamphour.com/633-engineering-optimization/ |
| 643 | Calibration & Repair with Ian Johnston | https://theamphour.com/643-calibration-repair-with-ian-johnston/ |
| 716 | Electronics Manufacturing History with David Ray | https://theamphour.com/716-electronics-manufacturing-history-with-david-ray/ |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ |
