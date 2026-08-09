---
title: PCB Design
concept: pcb-design
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

Printed circuit board (PCB) design is the engineering activity of turning a circuit schematic into a physical, manufacturable board: capturing and sharing a circuit is comparatively easy, and the remaining effort of producing the actual board is where the work lies.[106][626] It is a learned skill acquired by doing rather than by study — certification courses exist, but they certify knowledge the designer already possesses rather than teaching it, so experience has to come first.[8] The craft admits no unique solution: the same design handed to twenty designers produces twenty different layouts, which is why it is taught by experience rather than by rule.[16] Despite being central to building anything physical, board design is frequently absent from university curricula, and many engineers first encounter it at work or in a hobby project.[573]

## The craft and its acquisition

Board design proficiency is built through practice rather than formal instruction.[8] Reaching genuine fluency in a professional board tool takes roughly a year of fairly intensive use, a figure that makes interface churn expensive because a working designer cannot absorb months of reduced effectiveness.[523] Fluency is also perishable: a former full-time designer loses speed and needs days or weeks of daily work to recover it, even though the underlying judgment remains.[682] Keeping a hand in is cheaper than recovering the skill later; reading datasheets and doing occasional small work between projects is enough to hold competence in place through months without a design.[342] A related habit is passive accumulation of process knowledge — consuming factory and process material as a mental library of things worth considering the next time a similar design comes up, rather than for immediate application.[718]

Because the skill is learned by doing, sustained personal projects are a recognised route into it. Aedan Cullen's four-year personal AR headset project, spanning four complete redesigns, took him from having done nothing beyond simple through-hole boards — he had not even assembled a BGA — to confidently taking a set of requirements through to a working, software-running board with fine-pitch parts.[638]

The work itself has an uneven texture. Greg Davill, a designer known for photographically finished boards, notes that designing boards and assembling them are separate tasks that appeal to different people, that plenty of excellent designers would never assemble anything themselves, and that design has days that simply do not flow — a condition he compares to writer's block.[473]

## Workflow and process

On one experienced view, board design is ninety percent placement and setup, where setup means establishing the rules, clearances and outlines before any routing starts; once the constraints are in place, routing is comparatively free.[482] Speed and thoroughness are a project-level trade rather than a personal virtue: some projects genuinely need only what is good enough, others justify spending a week choosing the correct screw, and recognising which project one is on is the engineering judgment.[514] Where board revisions are expensive and faults are hard to track down, six months for a single revision can be the rational choice, the schedule following from the cost structure rather than from slowness.[514] The effort is routinely underestimated from outside; a genuinely complex product board that must fit a mechanical envelope can absorb a month of full-time work at a competent pace.[516]

### Verification

Checklists help but cannot be complete: every board carries its own unique issues, and a checklist capturing every problem ever found would grow long enough that nobody would work through it.[287] What supplements the checklist is unstructured inspection — spending a full day panning around the finished board in different views, particularly the three-dimensional view, checking silkscreen, polarity marks and connector orientation — which catches the class of error no list anticipated.[287] A cheap habit worth building in is indicator LEDs on the power rail and on a spare digital output, which immediately expose conditions that are otherwise invisible, such as a part being powered parasitically through one of its I/O pins.[287]

### Panelisation

Two workable panelisation approaches exist: use a tool that duplicates the boards from a linked source file while the designer manually draws the rails, fiducials and mounting holes around them, or simply copy the whole board within one file; the linked approach guarantees the copies match.[400]

## Components, footprints, and libraries

Part data is harder than it appears because one logical component is several physical ones: a 10K resistor in an 0603 size still has three different land patterns in the standards, so choosing the part does not finish the decision.[445] Two workflows follow, and neither is correct: either create every variant as its own part with its own number, or keep one or two and adjust on the board; adjusting on the board suits a small company buying from distributors, while scale makes the formal approach unavoidable.[445] On-demand symbol and footprint services exist to absorb this work for a fee, but they do not resolve the underlying problem — everything remains custom, merely faster and done by someone else.[445]

Footprints shipped with a design tool are frequently unusable and tend to be oversized, which is why a working designer may end up building close to all of them by hand from the published standards mixed with personal convention.[29] Even a borrowed footprint usually gets rebuilt, because the silkscreen outline is treated as part of the component rather than as decoration, and another person's choices there rarely match.[29] The library burden drops sharply once the common passives and standard small-outline packages exist, but it never reaches zero: every project turns up some obscure part needing a new footprint or at least a tweak to an existing one.[29]

The contrast with chip design is sharp: on silicon there may be a hundred qualified device types known to work, whereas a board designer selects among millions of parts and may be using a footprint of entirely unknown provenance.[579] Chip and board design are nonetheless ultimately the same activity of putting shapes on a planar surface, and closer integration between the two toolchains would remove a familiar compromise — adding board layers purely because the pin needed is on the wrong side of the die.[703]

## Tools and toolchains

### Tool choice and switching

An experienced designer learning a new package is only learning the mechanics of that software; the underlying skill of knowing how a board should be built is already present, which is why the second board in a new tool is faster than the first.[404] Switching nonetheless makes an expert temporarily slow and generates false defect reports, because a menu one cannot find feels exactly like a bug, and convention absorbed from one package gets mistaken for correctness.[198] Moving a design between packages means recreating it rather than converting it; one tool migration meant redoing five or six complete boards from scratch, which is the real cost of a tool decision.[83] Long-lived designs become unmaintainable through their tools in a related way: working files end up in CAD packages that no longer exist, turning a routine revision into a recreation exercise.[16]

For professionals, buggy tools are genuinely unacceptable when board design is how one earns a living; frustration with defects is a working constraint rather than preciousness.[198] One deliberate position, held by open-source hardware practitioners such as Mike Ossmann, is to use open-source design tools to support open-source hardware even where they are not the easiest choice for the job, requiring collaborators to do the same and accepting the friction as the cost of keeping the project accessible.[198] The opposing professional view holds that the open-source tools, however capable for ordinary work, still lack specific features needed at the high end — an assessment its holder explicitly flags as based on older knowledge, the appropriate caveat for any tool comparison.[555]

Because proficiency takes about a year to build, the argument follows that vendors should keep interfaces stable with an option to revert; mechanical CAD is the comparison, where the fundamental interaction model has barely changed in a very long time and users remain effective across releases.[523] One structural way a CAD vendor keeps contact with real use is an in-house hardware team designing real products on every daily build, so the tool is exercised by people whose actual output depends on it.[523] Publishing design files in a proprietary format matters less than the argument suggests, because only a small percentage of people ever rebuild a board from source, and for a design of twenty or thirty parts redrawing it in one's own package takes a few hours.[191]

### Mechanical co-design

Electrical and mechanical co-design has become part of the board designer's job, which exposes a gap for anyone who has always worked in two dimensions: comfort at board level does not transfer to three-dimensional modelling, and closing that gap has to be deliberate.[472] Jeff Keyzer, whose career spans board design at multiple hardware companies, describes the route into mechanical competence as making bad parts — the first brackets he modelled were not mechanically sound, and building unsound parts is what taught the principles that made later ones good.[472] Mechanical CAD choice follows the ecosystem rather than the feature comparison: whichever package has more use where mechanical work meets board design is the one a practitioner is more likely to meet at a client, which outweighs a free licence for many.[472]

### Artistic and scripted approaches

Treating board design as a drawing exercise changes which tool is appropriate: a real drawing package makes alignment, whole buses and arbitrary curves easy because that is what it was built for, whereas producing artwork inside an EDA tool is, in Saar Drimer's phrase, like "screwing in a screw with a knife."[286] Drimer's own tool design refuses a graphical interface entirely, on the argument that the "GUI is where good ideas go to die"; the tradeoff is a steeper entry in exchange for scriptability and precision.[286]

### Automation

Autorouters are advanced tools for advanced designers rather than a shortcut for beginners, because using one before being able to do the job manually removes the feedback that teaches what a good board looks like.[46] Sergiy Nesterenko's stated goal for automated board design is a compiler analogy: take the schematic, extract everything that defines what the board must do, and emit a manufacturable board verified against physics and design rules without human routing.[626] The precedent making that plausible is FPGA place and route, where designers stopped drawing logic by hand once the tool produced a timing report that could be trusted, and where compute could simply be thrown at a cluster for faster turns.[626] The disanalogy is visibility: board layout is intensely visual in a way that programmable logic place and route is not, which is a real obstacle to accepting a result one cannot inspect the same way.[626]

A point-and-click board configurator that assembles known modules onto one board has a narrow but real market: someone who needs twenty of something, has no interest in electronics, and does not want to hand-wire twenty assemblies.[516] Compared against hiring, such a service looks expensive — a competent engineer could do the same design in roughly twenty hours — but what is actually being sold is avoided activation energy, since finding, briefing and taking the risk on that engineer is itself work.[516]

## Specialised design concerns

### Flexible and rigid-flex boards

A plain flexible board is essentially no different to design or order than a rigid one: the designer specifies flex and a thin stack-up instead of standard laminate, and everything else is unchanged; the complexity begins only when flex and rigid layers are combined in one part.[468]

### Radio and antennas

A radio section that has passed certification is reusable capital: once a design works, the antenna section is left untouched while sensors and interfaces change around it, and the next product has a good chance of passing compliance on the same basis.[549] Antennas have to be considered at the start of a design rather than at the end; left until last, the antenna gets a poor location with insufficient clearance, and by then nobody will fund the changes that would fix it.[678] For common 2.4 GHz modules, the published guidelines are forgiving enough that a non-specialist can place the antenna correctly by following them, while anything more complex than a standard inverted-F warrants an antenna engineer and simulation.[678]

Module abstraction is also a supply-risk strategy. Lukas Henkel, designing compact high-speed open hardware, standardises on one open module footprint chosen for easy routing at a comfortable 0.8 millimetre pitch, so the processor underneath can change without a redesign of the carrier board or an expensive stack-up.[681]

### Precision and prototyping constraints

At the precision extreme the board becomes part of the measurement: voltage reference designs use exotic cutouts so that thermal expansion of the laminate cannot put uneven tension on the package leads, because that stress alone shifts the output by fractions of a part per million.[558] Desktop trace-printing machines are not a press-print path from an existing design: the board has to be redesigned around the machine's limits, components cannot go on the second side, and an existing layout has to be redone entirely.[236] Understanding electromagnetic compatibility improves board design, product design and firmware simultaneously, partly because some compatibility problems turn out to be fixable in firmware once the mechanism is understood.[472]

## The profession

The generalist-versus-specialist question resolves differently by employer: one person is now expected to cover layout, sourcing, mechanical modelling and test, largely as a cost measure, but a designer who goes deliberately narrow will still find work.[19] That expectation does not extend upward — a large, expensive product will not be handed to a single person covering every discipline, and where it is, the compensation should reflect it.[19] The scope of the role has also widened beyond the board itself: a designer is now frequently expected to handle programming, the broader product design and even the surrounding web presence, because the available tools make it possible to ask.[606]

Board work has an awkward duty cycle for an independent designer: once files go out there is a gap that nothing fills unless the next project happens to start exactly then, whereas firmware work is continuous because there is always another improvement to make.[601] The open question that follows is one of scope — how large a combined hardware and firmware task a single fully utilised person can carry before a two-person team becomes more efficient, since adding a person costs coordination but buys specialisation.[601]

For hiring, demonstrated work outweighs credentials: being able to show boards one designed and built, and to bring the hardware itself to the interview, is what makes the educational background secondary.[189] The advice for changing roles is to commit to one substantial project with real money and real months behind it; the object can be pointless, but the effort must be serious enough to function as example work.[288] A specific way to approach a design engineer whose job one wants is to take one of their products apart, obtain the schematic, and ask why they made a particular choice — design engineers will talk at length about their own designs, which turns an awkward request into a technical conversation.[288]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 8 | Layouts and Design-Outs | https://theamphour.com/the-amp-hour-8-layouts-and-design-outs/ | |
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ | |
| 19 | CAD programs, Systems Design and Renewable Energy | https://theamphour.com/the-amp-hour-19-cad-programs-systems-design-and-renewable-energy/ | |
| 29 | DJ and Jazzy Jeff | https://theamphour.com/the-amp-hour-29-dj-and-jazzy-jeff/ | |
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ | |
| 83 | Aggravating Agersia Agiotage | https://theamphour.com/the-amp-hour-83-aggravating-agersia-agiotage/ | February 19, 2012 |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 198 | Mike Ossmann Returns! - Planetic Portalab Packaging | https://theamphour.com/198-mike-ossmann-returns-planetic-portalab-packaging/ | May 12, 2014 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ | February 24, 2016 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ | |
| 404 | Proof Of Blink | https://theamphour.com/404-proof-of-blink/ | August 26, 2018 |
| 445 | Ludicrously High Frequency Interference | https://theamphour.com/the-amp-hour-445-ludicrously-high-frequency-interference/ | June 2, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 514 | Focus, Dammit | https://theamphour.com/514-focus-dammit/ | October 25, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ | December 27, 2020 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ | August 30, 2021 |
| 558 | Toasted Marshmallow Connectors | https://theamphour.com/558-toasted-marshmallow-connectors/ | September 19, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 678 | All About Antennas with Katerina Galitskaya | https://theamphour.com/678-all-about-antennas-with-katerina-galitskaya/ | September 30, 2024 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
