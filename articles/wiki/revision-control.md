---
title: Revision Control
concept: revision-control
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Revision control is the practice of recording the successive states of a design or code base so that any earlier state can be identified and recovered. In electronics it spans software-derived systems such as Git and Subversion, the dated-archive and numbered-folder conventions that precede them, and the product lifecycle management tools that add change orders and controlled distribution on top.[67][273][577] Its application to hardware is constrained by file format: Git is as effective for hardware as for software on the condition that the ECAD package stores its designs in a text-based format, so the tool's usefulness is set by the format rather than by the domain.[161] Storing engineering work in a version control system long predates cloud-hosted design tools, going back to RCS.[471]

## Mechanisms

Git records history in terms of the change between one version and the next rather than as a complete copy per revision, which keeps repository size manageable and distinguishes it from Subversion; it is designed around plain ASCII text files.[505] Cloning a repository retrieves the entire history into the local .git directory rather than only the current files, so every past state and every change is available offline to whoever holds a clone.[505]

The practical difference between a centralised system such as Subversion and a distributed one such as Git for an open project is the direction of contribution: with Git an outside contributor publishes their own commits for the maintainer to pull, rather than mailing a patch or requesting write access to the central repository.[125] What a board designer typically wants from either is the ability to return to specific identified points in a design's history, addressed by commit hash, in place of copying whole project folders into rev1 and rev2 directories.[162]

Commit messages written at the time of each change accumulate into a record of why a design took the form it did, a form of documentation produced as a by-product of the work, though obtaining that value depends on the discipline of writing a real reason each time.[289] Committing and pushing at the end of each working session also replaces physical transfer of files between machines, since the other machine pulls the current state instead of receiving a copy on removable media.[315]

## File formats and diffing

Demand from users for open, text-based ECAD file formats has been driven largely by revision control, because an XML or other plain-text project format can be diffed and its changes tracked where a proprietary binary format cannot; binary formats can be versioned, but not compared usefully.[67] A naive byte-wise diff of a binary design file is close to useless, since inserting a single byte shifts everything after it and makes the entire remainder of the file appear changed.[67] Git additionally degrades on large binary files, so a hardware project tracked in Git gets the history and the backup but not most of the tool's other benefits.[577]

The gain from a text format is nonetheless partly theoretical in day-to-day work: a text-based ECAD format such as KiCad's makes the files legible to version control where a binary format such as Altium's does not, but engineers still do not in practice compare two revisions of a board by reading the file diff.[317] Mainstream repository hosting is built around linear, text-based version control, while a schematic or layout is a graph rather than a sequence of lines, so problems that look like text version control belong in a general host while graph-structured design data needs different handling.[163]

Capturing a design as HDL rather than as a schematic makes both large architectural changes and revision control substantially easier, because a textual description can be diffed and restructured in ways a drawing cannot.[181] Regulatory treatment can push in the opposite direction: in markets such as medical devices, source code is subject to different rules from schematics, which has led companies to enter designs as schematics that generate HDL rather than writing the HDL directly.[181]

FPGA work is particularly resistant. Vendor toolchains have not built revision control into the design environment, so tracking HDL sources and generated bitstreams has to be done with external tools chosen by the user.[67] The working tree also contains vendor binaries and encrypted proprietary blocks alongside the HDL sources, so much of the project cannot be diffed or merged at all.[152]

## Merging and collaboration

Merging is the point at which revision control breaks down for hardware. Two engineers working on separate schematic pages can be reconciled, but simultaneous edits to the same page or the same layout cannot be merged automatically and one set of work must be redone.[230] For CAD files a revision control system therefore operates at whole-file granularity, with a revision taken or not taken; since the case for a full version control system rests on merging, that case is weaker for a solo CAD user than for a software team.[287]

The usual way of dividing schematic work between engineers is to give each person separate pages or sheets, and the difficult part is reintegrating those pages afterwards, which is why hardware design teams stay small.[67] The prevailing collaboration model on small teams is single-authorship with review: one person makes substantially all the edits while two or three others act as reviewers, arguing architecture and part choice rather than editing the files themselves.[161] Design review on a hardware repository is anchored to a specific tag or commit identifier, with reviewers pulling that exact state, examining it and discussing it by reference, even where the tool provides no mechanism for proposing changes back.[163]

Because design files cannot be merged, small teams avoid conflicts socially rather than technically, by announcing that a revision has been pushed and agreeing not to touch the files while another engineer works on them.[230] The inability to merge matters less in practice than it appears, since hardware work is generally organised as sequential hand-offs of a block of work rather than as simultaneous editing, and that pattern is well served by revision control.[422]

Open projects use the same machinery for outside contribution. One workable governance model for a small open-hardware project is to grant commit access to anyone who asks and review after the fact, with the maintainer receiving an email for every commit and raising problems as they appear, on the reasoning that correcting a contributor's style costs less than gatekeeping.[125] Publishing a company's ECAD parts library in a public repository likewise lets outside users contribute symbols and footprints for older products that were never added to the library, submitted as pull requests and merged so that every user gets them.[157] A published hardware repository often contains only design sources and no generated manufacturing files, and an outside user can fork it, add an outputs subdirectory containing those generated files and offer the change back as a pull request without touching the source design at all.[530] Users of a public design repository build from tagged releases rather than arbitrary commits, because the tip of a working branch may contain unfinished circuits that were never intended to function.[251]

## Substitutes and predecessors

Before CAD, revision control was a paper procedure: work was recorded on ruled A3 sheets in per-project ring binders under a company numbering system, each page hand-written, signed and dated, and a new revision was created by photocopying the previous one, marking the changes by hand, signing it and labelling it as the next revision.[273] Designs predating routine version control can survive only as scanned documents; for some long-lived semiconductor parts the CAD files no longer exist, and the reference PCB layout has to be recovered by toner-transferring the artwork out of a scanned application note.[270]

Teams without a version control system still practise revision control in weaker forms, such as zipping the project with a date appended or keeping a text file describing what changed and why, the text file performing the function of a change log; any such scheme is only as good as the consistency with which it is used.[317] The dated-archive method is justified on the grounds that storage costs almost nothing while losing a design is expensive, its weakness being that a set of such archives becomes unmanageable as revisions accumulate.[67] A common substitute on solo projects is a fixed directory convention: one subdirectory per project, split into firmware and hardware, holding the current working files plus a backup subdirectory, with the whole tree covered by a routine backup.[67]

These substitutes degrade in characteristic ways. Hand-rolled folder-copy versioning produces ad-hoc naming schemes such as 1A and 1B whose meaning cannot be reconstructed later, so the history exists but is not interpretable.[162] Filename-based versioning on a shared project produces a proliferating set of near-identical files, with sequential numbers followed by further suffixes for individual fixes and no record of what distinguishes them.[230] Firmware written before version control was in use carried its history inline, under house rules requiring every added line to be commented with the version in which it was added, so the comments recorded version bookkeeping instead of explaining the code; the same era copied whole code bases from one product to the next.[522]

A file synchronisation service is backup rather than revision control, since it preserves the files but not an intentional record of states and the reasons for moving between them.[230] It can still serve as a second, independent recovery path while an engineer is learning the version control commands, because a destructive command that discards local work can be undone from the sync history.[315]

## Use in hardware practice

Software practice is to create the repository before writing any code, whereas hardware teams typically begin in CAD, do several design iterations with local file revisions on a laptop, and retrofit revision control or a PLM system only after they recognise the risk they are carrying.[577] Hardware groups inside software companies were among the earliest to put ECAD work under revision control; Altium's hardware engineers used Subversion through the TortoiseSVN graphical client.[230] Being required to work on daily builds of the design tool forces fluency in revision control, and that group's own protection was to agree informally on one standardised tool version for work that had to be delivered.[724]

The learning curve is a real and persistent barrier for practising hardware engineers, many of whom use only clone for years before understanding the rest of the tool, with the command line remaining the intimidating part.[670] For engineers who are not software developers, a graphical client displaying the linear progression of commits has been what made distributed version control comprehensible, giving a visible model of the history before any command-line use.[162] There is also a standing argument against putting personal projects under revision control, weighing overhead against project size: an engineer working alone on small designs may judge that the setup and daily cost exceeds what the history is worth.[300]

Software development methods have moved into firmware and are now moving into hardware tooling, with cloud-connected ECAD offering revision control built into the design tool itself rather than bolted on, which mainly speeds collaboration with other people.[601] Attempts to add hardware version control by layering it onto existing CAD packages, including gEDA, Cadence and Altium, and by adapting Git to their file formats, were tried before anyone built a new CAD tool for the purpose, and those attempts failed, which is what motivated ground-up tools.[163]

## Everyday practice

Committing or saving on a fixed short interval bounds the work lost when a design tool crashes or an operation destroys the file, and making it a scheduled habit rather than a reaction is what makes it effective.[244] The measurable benefit of routine commits during ECAD work is that loss is bounded to an hour or a day of work rather than weeks.[422] A single structural edit, such as adding a hierarchical sheet, can corrupt an ECAD project beyond the user's ability to undo it, and without any prior copy the work is unrecoverable, which is the failure that motivates even file-sync-level backup.[230]

Fast iterative debugging is where revision control is most often abandoned and most needed, since after dozens of small undocumented edits there is no way back to the last state that worked, because the change that broke it is no longer remembered.[383] Code generators overwrite what they produced previously, so hand edits to generated files are destroyed on the next run, and committing before regenerating is what makes those edits recoverable.[661] Commented-out code is deleted rather than left in place, because the version control system already preserves it and can return it on demand, while leaving it in the source only obscures what the program currently does.[187]

One failure mode is outside the system's reach: revision control does not protect against a design tool that silently changes its file format. If a week of commits was made with a newer build and the files then have to be opened with the older stable release, the committed history is unreadable and the work is lost anyway, so the defence is a known-good tool version rather than more commits.[543]

## Libraries and component data

Storing each footprint and each schematic symbol as its own file inside a directory that constitutes the library makes library changes visible to revision control at the level of the individual part, and lets parts be copied between libraries individually.[370] Component libraries can be version controlled in the same repository system as the designs; a four-person hardware group put its component libraries under Subversion via TortoiseSVN rather than keeping library files local to each project.[543] Parts specific to a company need a centralised component database rather than per-project libraries, but running one carries real overhead: at one company a dedicated librarian maintained it, and the approval path for admitting a new part governed how quickly purchasing could buy it.[543]

Pulling library dependencies from an upstream repository lets a project take updates and observe what they break, but the analogy stops at fabrication, since a board that has been built cannot be updated from upstream, so footprints must be checked before the design is committed to manufacture.[186]

## Design data as controlled source

Treating the schematic as the control document means encoding manufacturing data such as populate or do-not-populate as component attributes in the schematic and generating the purchasing spreadsheet and assembly documents from it, since purchasing staff and contract manufacturers work from a spreadsheet and will not open a schematic.[174] Scripted plugins that export schematic fields to a spreadsheet and write the edited values back, such as KiCost and KiField, are what let the schematic remain the single tracked source for costing and part data while the people who work in spreadsheets still get a spreadsheet.[364]

Per-seat CAD licence cost is a direct obstacle to that arrangement: at several thousand dollars a seat only the licensed designer can open and change the file, whereas a low-cost or open tool lets a production engineer make a change and put it through revision control and approval at the schematic level.[243] Floating licensing weakens the headcount argument, since a company does not need a seat per employee, only enough concurrent licences for the people using the tool simultaneously.[364]

Hosted repositories, whether Git-based or Perforce, concentrate a company's most valuable intellectual property with a third party, which makes the choice of hosting and its terms an engineering-management decision rather than a convenience one.[471]

## Beyond the design repository

Schematic and layout carry their own revisions and can decouple, because a layout change need not imply a schematic change, and assembly variants such as alternative populated parts add a further dimension that neither document's revision letter captures.[174] A project whose hardware, embedded firmware and host-side software must interoperate is best versioned as a unit, so that the version numbers of the three parts advance together and any checked-out state is internally consistent.[161] A repository per board likewise stops being sufficient once a product is an assembly of interacting boards, because a change to one affects the other and what has to be tracked is which revisions were sent to the manufacturer and which pair was fastened together and shipped to a customer.[577]

Traceability at the unit level is a distinct problem from revision control of the design: for a complex assembly it means being able to say which revisions of which sub-assemblies went into each individual serial number, which does not fall out of a design repository.[546] Production test assets are versioned and shipped as releases, with a firmware version, its matching test plan and any label configuration packaged together and deployed to the production line testers, using separate deployment groups so a release can be put on staging before it reaches the line and identical lines in different factories updated at once.[544]

Product lifecycle management is the product category covering bill-of-materials and CAD file management, revision control, part number generation, and controlled distribution of design content to team members and suppliers, with change orders as the mechanism for making a revision official.[577] Released data has to have one designated authoritative location, whether the schematic or a PLM system; once many copies of a BOM are circulating with different vendors, the only defensible position is that the nominated source is definitive and copies are not.[577] Change notifications accordingly carry a link to the controlled revision rather than an attached copy of the Gerbers or BOM, because an attachment persists in recipients' mailboxes indefinitely and will eventually be used after it has been superseded.[577] The hardware data tool chain of CAD, PDM, PLM, ERP, MES and inventory systems was designed as separate products decades apart and does not interoperate out of the box, so it is common for a hardware company to spend six months or more configuring the tool chain before it can manage its data properly.[577]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ |  |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 157 | An Interview with the SparkFun Team - Efficacious Engineering Ensemble | https://theamphour.com/the-amp-hour-157-efficacious-engineering-ensemble/ | August 5, 2013 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ |  |
| 186 | Someone is watching...we think - Horme Hostility Hypochondriac | https://theamphour.com/186-someone-is-watching-we-think-horme-hostility-hypochondriac/ | February 25, 2014 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 230 | Prepping For Hoverboards - Gallionic GitHub Gabble | https://theamphour.com/230-prepping-for-hoverboards-gallionic-github-gabble/ | December 30, 2014 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 244 | The Art Of Staying Interested In Electronics - Exponible Electronics Ennui | https://theamphour.com/244-the-art-of-staying-interested-in-electronics-exponible-electronics-ennui/ | April 7, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 273 | Part Choice Triathlon | https://theamphour.com/273-part-choice-triathlon/ | October 28, 2015 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ | March 2, 2016 |
| 300 | Three Hundred Down, Three Hundred To Go | https://theamphour.com/300-three-hundred-down-three-hundred-to-go/ | May 25, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ |  |
| 317 | A Decoupled Episode | https://theamphour.com/317-a-decoupled-episode/ | September 28, 2016 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ | August 16, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15, 2021 |
| 543 | Cassette decks have browsers? | https://theamphour.com/543-cassette-decks-have-browsers/ | May 23, 2020 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 577 | Product Lifecycle Management with Michael Corr | https://theamphour.com/577-product-lifecycle-management-with-michael-corr/ | February 13, 2022 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 670 | Engineering Careers with Circuit Break & James Lewis | https://theamphour.com/670-engineering-careers-with-circuit-break-james-lewis/ | June 14, 2024 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
