---
title: Github
concept: github
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

GitHub is a hosted service built on top of the Git version control system, which originated in Linux development; the service supplies the social, online layer around the underlying tool and thereby became the default place to share designs.[230] Although Git is nominally a distributed system, it is used centrally in practice: when every participant pulls from the same host, that host functions as the authoritative copy, with local copies reconciling once it is reachable again.[396] The platform provides code review and collaboration to small teams without requiring them to maintain any infrastructure of their own.[422] Its contribution mechanism is built on forking a line of work and merging it back, a model that distinguishes it from the centralised version control systems that preceded it.[152]

## Relationship to Git

Git and GitHub are distinct things: Git is the version control tool that came out of Linux development, while GitHub is the hosted, social layer on top of it.[230] The generational difference from earlier systems is the branching model. Centralised version control was typically used through a graphical client integrated into the file manager, whereas the Git model is built on forking a line of work and merging it back together.[152]

Because the design is distributed, organisations that need a guarantee of availability run their own instance rather than depending on the hosted service, which is what the distributed architecture was intended to support.[396] Nonetheless, when every collaborator pulls from the same GitHub host, that host is the centralised copy in practice.[396]

## Collaboration model

### Forks and pull requests

The contribution mechanism is fork then request: forking copies a repository into the contributor's own account as it stood at that instant, changes are made in that copy, and the contributor then asks the original maintainer whether the changes should be merged back.[530] The review interface shows exactly what changed with colour-coded indicators, pulls in test results from the automated build beside the change, and consolidates everything in one place so an approver can review it quickly.[577]

Maintainer review time is the scarce resource in this model, so mechanical objections are best automated away: a maintainer spending time telling a contributor to change tabs to spaces is friction that accumulates into the "death by a thousand paper cuts" that kills participation in a project.[383] Project management can run through the same issue tracker, with a subset of issues explicitly labelled as suitable for a first contribution so that newcomers have an identified way in.[383]

The chat layer is a separate choice from the repository. A chat service tightly integrated with the repository gives change history in the channel but leaves the boundaries of the space vague, whereas a general chat platform supplies channels, a code of conduct and moderation, which is what a community actually needs.[383]

### History capture

Two models of capture exist. Continuous tracking records every component move from one coordinate to another and can replay all of it; GitHub's snapshot-and-commit model records only the differences the author chose to mark, which keeps the history readable when the author saves compulsively.[122]

A client that draws the commit tree makes the branching model comprehensible, turning merges from an abstraction into something legible in a way the standard reference book does not, because that book is written for software developers.[230] Beyond visualisation, the tool is learned by use: running it a few times and breaking it a few times is what actually teaches it.[230]

## Publishing and editing without local tooling

Publishing a one-off project does not require learning the tool. The web interface accepts a new repository and dragged-in files in tens of seconds, leaving the work somewhere others can clone and branch from.[621] For a fragment rather than a project, a paste service on the same site (Gist) keeps revisions and supports forks without installing anything locally; it is indexed separately, so a search of the main site does not reach it, and the published fragment gets a generated identifier rather than a meaningful project name.[158] Pressing the full-stop key while viewing a repository opens an editor on it in the browser.[612]

A development container defined alongside the code removes environment setup from collaboration entirely: the toolchain is pre-installed in the container, and a collaborator opening the shared link gets the code and toolchain already configured rather than a remote desktop to someone else's machine.[654]

Project documentation is increasingly written in a lightweight markup language and kept in the repository beside the design rather than in a separate document system.[232] A site generated from a repository inverts the load model of a dynamic site: committing to the main branch triggers a build that emits a static HTML page per document, where a dynamically generated site rebuilds every page from the database on every request, which becomes the bottleneck under load.[656]

## Use in hardware design

The platform is built for linear, text-based version control and its front end is very good at exactly that; hardware design files are graph-based rather than linear, which is a different revision-control problem. On the Upverter project, founder Zach Homet framed the consequence as a division of labour: work that looks like text belongs in Git, and work that looks like hardware belongs in a tool built for it.[163]

### Limits of the diff

For board files, the difference between two revisions is largely opaque: an ASCII-format design lets some changes be discerned by eye, but for the most part the diff only reports that the file changed.[315] Library structure therefore decides whether revision control says anything useful. Storing one footprint or one schematic symbol per file, with the directory acting as the library, makes each addition visible as its own change.[370] The alternative produces a useless record: a monolithic library file reports only that it grew from about two thousand characters to two thousand one hundred, forcing someone to open the file and find what actually changed.[370]

Forking works for hardware in one direction only: a published design can be forked into a derivative and taken anywhere, but reintegration is the hard part, and at the board level it does not work at all.[154] Dependency updates are similarly one-directional. A software library pulled in dynamically can be updated and the breakage inspected; a footprint committed to a board that has been fabricated cannot be updated at all, which is why footprints must be checked before the board is sent.[186]

### Hardware workflows on the platform

Hardware groups use the same machinery for design review even without an automatic merge path, referring to a specific tag or commit number as the thing under review.[163] Design tools followed the platform: storing part libraries in a repository means a symbol or footprint is pulled from the network when it is placed, rather than from a local cache or mirror.[167] The open question for a shared parts library is organisational rather than technical: whether a contributed set of parts should be merged into the existing library for that manufacturer or kept as the contributor's own, a choice that decides how the collection can be used later.[88]

Treating the schematic as the control document makes the repository useful downstream: fit and no-fit status carried as a schematic attribute can be propagated programmatically into a spreadsheet the purchasing side will actually read, and the method only works if it is adopted completely.[174]

SparkFun's migration of its product files onto the platform is an anchored example. The move solved a revision-control problem the company had struggled with for years and gave it a public-facing way to present the revision history of its boards.[157] Customers were then able to draw the missing library parts for boards several years old and submit them; after the maintainer merged the contribution it became available to everyone immediately, and the migration also changed how customer feedback was tracked alongside the documentation reorganisation it forced.[157]

### Documenting published hardware

A repository can carry a rendered page describing the project, and most published projects do not have one, so someone arriving has no way to see what the thing is without reading the source tree.[335] Pushing files to a repository can displace written documentation rather than supplementing it: schematics get dumped there and the write-up never happens.[416] For hardware, publishing the fabrication files and rendered PDFs alongside the sources, with a link to an online viewer, lets someone evaluate the board without owning the design tool.[395]

A repository is still several steps away from a manufactured board: the visitor must find the design, download it, identify the correct fabrication files, verify them, upload them, choose the process options and then order, where a prepared upload at a board house is one action.[453]

Publication order can be deliberate. Bunnie Huang's practice is to push everything to the repository before announcing a project, so the links are live and working by the time anyone follows them.[336] Where documentation lives determines whether it survives: reverse-engineering work that exists only inside a social platform is hostage to that platform, and moving it into a repository or a documentation archive is what keeps it available.[609]

## Individual publishing practices

Trammell Hudson's workflow is to stop at proof of concept and publish: photograph the result, write it up, push everything to a repository, and move to the next thing; over a decade this produces a body of work others pick up and extend, and its end state is handing the commit rights over to whoever wants to maintain the project and turn it into something better.[463] A project published this way is only useful if it is readable: Travis Goodspeed's practice is to keep the code, the hardware and the design documents all in the repository and properly commented, so that any individual application can be understood from two or three pages of C source.[442]

The operational habit that pays for itself is committing before regenerating anything, so that a wipe leaves the previous version recoverable.[661]

## Professional signalling

Employers came to treat a public profile as a curriculum vitae, expecting candidates to have one and to have contributed to some number of projects.[172] Recruiting on the count of projects a candidate has started has a perverse effect: it removes the incentive to join and improve someone else's project, which is most of what the ecosystem needs.[172] Commit frequency is a weak signal in the same way, since a profile can show an enormous number of commits that consist of repeatedly correcting the previous one.[231]

The signal that carries information is the pull request rather than the profile. Piotr Esden-Tempski's hiring practice is to read a candidate's submitted changes, which shows whether they understand version control, whether their code is legible, and whether they can discuss a change with other people; his corresponding advice is that a student should contribute to an open-source project before applying anywhere, because it is the one part of an application that demonstrates all of that at once.[409]

On a résumé a project line is worth more than unrelated employment history, and the way to acquire one is to take an existing project, modify it and document the work as it goes.[530] For someone who will not make videos or approach people directly, a repository or a project blog is the route to being known, since the work itself becomes the thing that circulates.[262]

Command-line fluency with version control, including judgement about when to commit, is treated as a skill hardware engineers are expected to have.[422] In software, nobody joining a company proposes building their own version control, because the tools are free, ubiquitous and shipped with the operating system; hardware change control has not reached the equivalent position, with the pull-request review interface standing as the model it lacks.[577]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 122 | Processors, CEOs & Soldering irons - Plentiful Perfunctory Programs | https://theamphour.com/the-amp-hour-122-plentiful-perfunctory-programs/ | November 19, 2012 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 157 | An Interview with the SparkFun Team - Efficacious Engineering Ensemble | https://theamphour.com/the-amp-hour-157-efficacious-engineering-ensemble/ | August 5, 2013 |
| 158 | Hyperloop, Upverter and Soldering - Unbelievable USB Ustulater | https://theamphour.com/the-amp-hour-158-unbelievable-usb-ustulater/ | August 12, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 186 | Someone is watching...we think - Horme Hostility Hypochondriac | https://theamphour.com/186-someone-is-watching-we-think-horme-hostility-hypochondriac/ | February 25, 2014 |
| 230 | Prepping For Hoverboards - Gallionic GitHub Gabble | https://theamphour.com/230-prepping-for-hoverboards-gallionic-github-gabble/ | December 30, 2014 |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ | January 6, 2015 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 262 | Jobs For Weirdos | https://theamphour.com/262-jobs-for-weirdos/ | August 12, 2015 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 335 | When the TV watches you | https://theamphour.com/335-when-the-tv-watches-you/ | February 8, 2017 |
| 336 | An Interview with Bunnie Huang (2nd) | https://theamphour.com/the-amp-hour-336-an-interview-with-bunnie-huang-2nd/ | |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 396 | The Synergy Bus | https://theamphour.com/396-the-synergy-bus/ | June 10, 2018 |
| 409 | Electronics Consultant Impedance Matching | https://theamphour.com/409-electronics-consultant-impedance-matching/ | September 30, 2018 |
| 416 | An Interview with James Bruton | https://theamphour.com/416-an-interview-with-james-bruton/ | November 18, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 453 | Vertically Integrated Design Engineering | https://theamphour.com/453-vertically-integrated-design-engineering/ | August 4, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15, 2021 |
| 577 | Product Lifecycle Management with Michael Corr | https://theamphour.com/577-product-lifecycle-management-with-michael-corr/ | February 13, 2022 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 621 | The Magic of Calipers | https://theamphour.com/621-the-magic-of-calipers/ | February 26, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 656 | Pneumatic Tubes, Straight To The Home | https://theamphour.com/656-pneumatic-tubes-straight-to-the-home/ | January 22, 2024 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
