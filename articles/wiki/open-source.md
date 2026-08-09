---
title: Open Source
concept: open-source
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

Open source is an ecosystem rather than a technology: the code is the smaller half of what a project is, and treating it as only a technical artefact is the mistake newcomers most often make.[123] The underlying arrangement is social — pulling together a team and creating an architecture of participation, with the technical output following from that rather than the other way round.[105] The practice long predates the terminology: before open licences existed, the way to open a design was to publish a full construction article in a hobbyist magazine.[10] Open source is one development and distribution model among several rather than the only legitimate one, and something challenging it is not automatically wrong.[54]

## History

Before open licences existed, publishing a full construction article in a hobbyist magazine was how a design was opened, a practice that long predates the terminology.[10] Ready-made licences made the modern practice viable at scale: previously a developer either wrote custom terms or paid a lawyer thousands of dollars, and being able to pick a defensible licence off the shelf is arguably a precondition for the field's existence.[4]

Some open ecosystems formed before any official openness existed. Early community work on one wireless platform ran on a leaked vendor software development kit rather than on anything the vendor published; the community formed before the openness did.[359]

## The ecosystem and its social structure

The practical form of engaging with the ecosystem is physical: conferences, user groups and hackerspaces. The people who wrote widely used projects are directly accessible in a way that authors inside a corporation never are, so a newcomer can end up talking with them without realising who they are.[123]

Community norms run stricter than the licence and cover things the licence deliberately does not. Hardware licences permit essentially everything as a matter of legal text, so the expectation that a derivative work credits and interoperates with the original author exists only as an unwritten rule.[123]

People arrive at open source for genuinely incompatible reasons — political, commercial and practical — and coalesce around the term while expecting different things from it; disagreements about what openness requires usually trace back to that divergence.[162] Openness is uneven even among its advocates: research presented at open conferences is routinely published in closed journals, and documentation frequently is not published at all, which makes the useful question how open a source actually is rather than whether it is open.[162]

## Project governance

Large volunteer projects converge on conventional structure. One project that began deliberately loose and emergent ended up with roles, responsibilities, team leads, interviews before people join, version control and code review — something resembling a corporate organisation chart.[105] The one thing that does not transfer from a company is coercion: volunteers need more careful and attentive management than employees, not less, because an unhappy volunteer simply stops showing up.[105]

Governing a distributed volunteer project carries every conflict a company has — between developers, users and support — with the additional constraints that nobody can be paid and the team is entirely remote.[381]

### Maintainer transitions and structural gaps

A maintainer transition can be handled deliberately rather than by collapse. When one project's long-serving maintainer stepped back, the project leader recruited a group of officers given explicit authority — described as "blessed autonomy" — to drive the areas they cared about.[381] The structural gap that made those appointments necessary is a common one: most contributions come from people who need one specific change for their work or research and then return to their day jobs, leaving few people working on the underlying architecture or reviewing anyone else's contributions.[381]

### Contribution mechanics

The naive assumption worth discarding early is that declaring a project open will summon contributors; people's time is constrained, and openness on its own changes nothing about that.[198] The concrete way to unblock contribution is to write the work down publicly: posting an issue listing every repository that needs the same change lets people who offered help simply start checking items off, which is far more effective than an open invitation.[383] The obligation that comes with accepting help is to respect that contributors are giving their own time and to let them get over the hurdles they hit at their own pace; treating volunteer effort as free labour destroys the supply of it.[383]

A persistent misconception is that free to use implies nobody spent time building the work and nobody is spending time maintaining it; maintainers are frequently doing the work at night, unpaid, for their own reasons.[356]

## Tooling and recruitment

Running a hardware project with the full apparatus of a software project — public repositories, wikis, mailing lists and chat channels — is what converts users into contributors; the tooling is not incidental but what makes participation possible at all.[161] On Michael Ossmann's projects, that apparatus doubles as a hiring pipeline: his entire recruiting method is taking volunteers already known to do good work and offering them paid contract work once funding exists.[161] Ossmann pays contributors by milestone rather than by time, which shifts estimation risk onto them and works because the people taking that risk are contributing partly for reasons unrelated to the money.[198]

Hiring from a project's own forum works unusually well: candidates already know the work inside out because everything is public, the employer has seen what they can do before making an offer, and there is nothing to train them on.[125]

Community contribution converts into employment through a recognisable path. Jeroen Domburg wrote a missing piece a vendor had on its roadmap but no time for, out of self-interest, which led to the vendor's chief executive making contact and eventually to a job.[359] Domburg initially declined payment for that work because being paid converts a voluntary interest into an obligation to keep developing something one may stop caring about — a real cost to the contributor.[359]

## Careers and entry into the profession

The standard advice for someone with no professional experience is to contribute to an open project, because it supplies what a first job would: someone architecting the design, mentors who have to help, grunt work that teaches the flow, and a great deal of self-directed learning.[56] From the hiring side, demonstrated initiative on a public project is what a manager is actually looking for, and candidates who claim no experience while having done nothing publicly are choosing that position.[79]

The opportunity for a newcomer is in neglected projects: many languish because nobody is working on them, so someone with time and moderate skill can contribute most of the remaining effort and have that be genuinely valuable.[79] Reading other people's published work is itself a route into the profession: Samy Kamkar learned how things worked from open projects, which made it possible to write his own software and get a paid programming job as a teenager.[308]

## Licences and legal context

Ready-made licences are the precondition for the field at scale, removing the choice between writing custom terms and paying a lawyer thousands of dollars.[4]

Vendor library licences can be incompatible with open projects through discriminatory clauses, such as forbidding use of a header on anyone else's hardware; that single restriction is enough to force a complete reimplementation.[356] The other half of the problem is the absence of a return path: finding bugs in a vendor library is useless if there is no mechanism to submit the fix, so every user repairs the same defects privately and forever.[356]

A platform hosting open designs can reasonably decline to police licences at all — letting users declare whichever licence they want while neither tracking nor enforcing it — on the grounds that tracking derivation across forks is an impossible problem and enforcement is not the business the platform is in.[163] A counterweight on formality comes from Clint Cole, who ships open designs commercially: putting the files out freely with no binding agreement is enough, people will find them, and open communities can become unhelpfully particular about certification and labelling.[302]

Non-disclosure agreements are the concrete barrier that openness removes. Bunnie Huang observes that many engineers will refuse a part outright if the datasheet requires signing an NDA, regardless of how cheap or good the part is.[84]

Publishing functions as a defence rather than a giveaway: an idea that is published enters the prior art, so it cannot later be patented and used against its originator, which makes publication the cheapest available protection for an idea its author cannot afford to patent.[10]

## Economics and business models

When everything is published, competitive advantage moves to what cannot be copied from a file: volume, manufacturing efficiency and how the business is run, which is why opening a design costs less than it appears to.[203] The reciprocity claim from decades of practice, as Bob Davidson puts it, is that publishing details and helping people returns more than it costs; practitioners trained to patent everything and keep it secret consistently fail to see how that could be true.[232]

The pragmatic case for publishing a schematic specifically is that withholding it protects nothing: anyone sufficiently motivated can reverse engineer a schematic in a day, so the only thing secrecy costs is the goodwill of the people who wanted it.[298] The marketing effect of openness is real even when nobody exercises it: Dave Jones notes that labelling a product open and publishing the firmware sells additional units because buyers value the option, and most of them never modify anything.[298]

Some platforms invert the usual arrangement with a default-public model in which everything a user creates is open unless they pay for privacy, making openness the path of least resistance rather than a deliberate act.[217]

A promise to open something later should be treated as equivalent to closed: the waiting usually does not end, and the incentive to withhold until shipping is real enough that the promise should carry no weight in a decision.[198]

## Fragmentation and wrong openness

There is a wrong kind of openness: publishing a self-invented protocol and specification instead of adopting an existing open approach multiplies incompatible standards under an open banner and leaves integration harder than before.[295] The reason this keeps happening is commercial rather than technical: it rarely makes business sense for a large vendor to join someone else's ecosystem when they need to sell a complete solution, so the decision is made by marketing even where the engineers would prefer interoperation.[295]

An aggregator that requires sign-up or payment before releasing the source of a contributed project is gating something its author gave away; adding value with better presentation is defensible, but withholding the source behind a login is a different act.[15]

## Failure modes

The recurring disappointment for users is that a project with a proper licence and a tidy repository frequently does not build: missing files or an incomplete release mean nobody has run it successfully since the author last did.[318] That failure is silent and self-reinforcing — rather than reporting the problem, the user gives up and writes their own version, so the defect stays in place and the effort is duplicated.[318]

The characteristic waste in hardware is starting from scratch, or privately modifying something that already worked without contributing the improvement back, so the original never improves and the next person repeats the work.[375]

Splitting hardware and software between two people creates a support asymmetry that can persist for years: in Dave Jones's case, the hardware author fielded every support query for a decade while the software author was largely insulated from them.[40] The argument that persuaded one designer not to open a product was support load rather than copying: publishing the firmware means fielding requests about every unofficial modification anyone makes, and those arrive at the original vendor regardless of who caused them.[347]

A standing risk in open tooling is loss of focus: a project with many contributors can drift toward being a jack of all trades, where one person with a clear idea would have produced a sharper tool for the specific job.[3]

## Measurement

Open projects have remarkably poor data on who uses them. The perverse consequence is that poor documentation is informative: it generates questions, and the questions reveal who is actually using the work and how deeply they have got into it.[374] In the absence of better data, repository watchers and stars serve as a crude floor on the interested population rather than a measure of use.[374]

## Open hardware

The scale limit specific to hardware is collaborative rather than legal: nothing exists on the scale of a large collaborative software project, because a single board with more than three or four designers working on it fragments rather than converges.[49]

A published hardware project should state the constraints behind its costs; someone comparing their own bill of materials against a project funded from a well-paid job needs that context, and hiding it makes the comparison misleading.[375] The collaboration openness enables is concrete rather than abstract: firmware developed for one project running on somebody else's board, with each side building on work the other inspired, across organisational boundaries that would otherwise prevent it entirely.[375]

Open projects attract adaptations their authors never planned: a stenography system published openly drew ports and new theories for other languages simply because people could ask questions and then build, which a closed project forecloses entirely.[314]

### Longevity

Opening a design at the end of its commercial life ensures its survival and lets users investigate it, which matters because the alternative is that the work disappears with the company.[219] Longevity is a legitimate purchase criterion alongside likelihood of success: for a connected product, whether a community-supported open alternative exists determines whether the device still works when the vendor's service goes away.[249] The same reasoning applies to development tools: choosing an established open toolchain over a vendor environment costs more effort up front and buys the assurance that it will still exist later — a trade worth making deliberately rather than by default.[249]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 3 | HP, IEEE, and Human Interface | https://theamphour.com/3-hp-ieee-and-human-interface/ | |
| 4 | Cultural Differences | https://theamphour.com/the-amp-hour-4-cultural-differences/ | |
| 10 | Open Hardware and Self Publishing | https://theamphour.com/the-amp-hour-10-open-hardware-and-self-publishing/ | |
| 15 | Analog Components, First Person Flying and Idea Ownership | https://theamphour.com/the-amp-hour-15-analog-components-first-person-flying-and-idea-ownership/ | |
| 40 | Adafruit, Chip heist, Hackerspaces - The Kit Conniption | https://theamphour.com/the-amp-hour-40-the-kit-conniption/ | |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | |
| 54 | An Interview with Jack Ganssle - Embedded Elchee Epexegesis | https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/ | |
| 56 | Open Orbific Oratiuncle | https://theamphour.com/the-amp-hour-56-open-orbific-oratiuncle/ | |
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 123 | An Interview with Jon Oxer - Innoxious Implant Innovator | https://theamphour.com/the-amp-hour-123-innoxious-implant-innovator/ | November 26, 2012 |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 198 | Mike Ossmann Returns! - Planetic Portalab Packaging | https://theamphour.com/198-mike-ossmann-returns-planetic-portalab-packaging/ | May 12, 2014 |
| 203 | Tesla, Checklists and Bullies - Emerging External Eupsychics | https://theamphour.com/203-tesla-checklists-and-bullies-emerging-external-eupsychics/ | June 16, 2014 |
| 217 | 3D Printed Shark Jumps - Edifying Edison's Energy | https://theamphour.com/217-3d-printed-shark-jumps-edifying-edisons-energy/ | September 22, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 249 | Wearables Might Have Limited Fashion Options - Lachrymogenic Lane Language | https://theamphour.com/249-wearables-might-have-limited-fashion-options-lachrymogenic-lane-language/ | May 12, 2015 |
| 295 | An Interview with Omer Kilic | https://theamphour.com/295-an-interview-with-omer-kilic/ | April 20, 2016 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11, 2016 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 314 | An Interview with Josh Lifton | https://theamphour.com/314-an-interview-with-josh-lifton/ | September 7, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 381 | An Interview with Derek Kozel | https://theamphour.com/381-interview-with-derek-kozel/ | February 25, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
