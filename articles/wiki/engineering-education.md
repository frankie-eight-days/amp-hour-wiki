---
title: Engineering Education
concept: engineering-education
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Engineering education is the body of instruction — university degrees, technician programmes, apprenticeships, and employer training — through which people acquire the knowledge and skills of engineering practice.[497][588] A persistent structural tension runs through it: degree programmes deliver a theoretical foundation while practical capability is largely acquired afterward, on the job, a division of labour that industry treats as a basic fact and builds its own training programmes around.[241][721] The field is further shaped by a zero-sum curriculum problem — the amount of material worth teaching grows every year while the length of the degree does not, so adding anything means removing something else.[306]

## Curriculum structure and constraints

An engineering curriculum is zero-sum: the amount of material worth teaching grows annually while the degree length stays fixed, and each addition displaces something. Processor-level instruction on hardware trainers, worth a semester in the late 1980s, is among the material that has been displaced.[306]

The conventional sequence front-loads calculus and physics, which produces heavy attrition: roughly half of an engineering intake is lost in the first two years.[251] Building a curriculum from first principles upward — starting at what an electron is and working toward circuits — loses students continuously before they reach anything resembling what they came to do.[116] The early theory sequence functions as a weed-out and deters students who arrived interested in electronics but without a background in it; the proposed alternative is to open with a course in which something is built.[83] The selection effect runs against the field's interests: the first two years favour the mathematically inclined, while students who were repairing electronics at twelve often find them hardest and drop out.[560]

Teaching material also lags practice for structural reasons. Writing good course material is a large effort, and institutions buy equipment and then amortise it, so microprocessor courses persisted well after microcontrollers had become the working part.[413] When Clint Cole, returning from industry, evaluated a department, he found the curriculum unchanged since he had been a student — the same topics, the same designs, the same textbooks — despite a decade of change in what industry needed.[302]

Even courses advertised as practically oriented can be paced for a non-technical intake. A student arriving from a vocational school where he had already repaired radios and designed op-amp circuits sat through a first year that began at Ohm's law and was still on diodes by mid-year.[169]

## Theory and practice

### Gaps in the degree

Printed circuit design — controlled impedance, spacing, stackups — is absent from many electronics degrees while vector calculus is proved in detail; the answer given by department heads is that students will pick it up over time.[573] Soldering and the use of laboratory instruments are generally not taught and are assumed to be picked up incidentally; a student whose project work is software-oriented can complete a degree without going near a circuit board and then take a job requiring both.[588] Wholly theoretical programmes exist at well-regarded schools: describing his own electrical engineering degree, Jeremy Blum noted that no course at Cornell had a student pick up a soldering iron or take a board from schematic to layout, with hands-on work happening only through a laboratory job or a senior project.[43]

### The case for theory

Theory earns its place in producing new schemes rather than in daily practice: working out something like frequency modulation required the mathematics first, but once a scheme is understood it can be simplified into a form a practising engineer can use.[165] Practising engineers rarely evaluate the integrals taught in the degree; the working method is rules of thumb, with the theory serving as the conceptual base underneath.[33] Courses are pitched to the highest level partly so students can discover whether they want to continue into the fields that use it, and so that some of them return to teach it; the number who use that material daily is very small.[33] On this view, education should carry more practical material than it does, and universities generally take the opposite position.[165]

Tom Lee has framed the teaching aim as intellectual scaffolding rather than tactics: what matters is the invariants a designer can rely on as technology changes, not the procedure for completing today's design.[459]

### Ordering of theory and practice

The order in which theory and practice arrive matters. Coming to the material through mathematics first and then working toward the practical is hard; the students who did best had built things, then knew why they wanted the mathematics. A good instructor has command of the mathematics and knows when not to use it.[459] A hobby background before formal study leaves a body of scattered, half-understood practical knowledge that falls into place when the theory arrives, and supplies the motivation to care about it.[512]

Students do not converge on one explanation: some grasp an operational amplifier from the intuitive model — that the difference between the inputs is zero and everything follows — and others need the equations written out before it makes sense.[560] Hands-on time with an instrument likewise builds mental models that theoretical treatment does not: watching a spectrum change as something is varied converts an abstract topic into something that can be visualised and reasoned about.[470] Ladder logic taught on classroom trainers with pneumatic cylinders and variable-speed drives did not click for one student until it was seen running on a plant floor, where the physical motion and the sound of things going right and wrong supplied the feedback the trainer could not.[620]

## Teaching practice

### Project-based structures

Larry Sears's analogue and mixed-signal course for juniors and seniors uses a project-per-week structure: a topic is taught and a working artefact using those parts is then required — analogue switches followed by building a function generator, or a motor whose speed is regulated from an encoder input, one week each.[109] Teaching laboratories in that programme are deliberately better equipped than the workplaces students will enter; the point is not that they will see that equipment on the job but that it introduces them to how the work is done.[109]

Clint Cole's grading scheme ties the mark to iteration rather than to a finished result: one prototype earns a D, two a C, three a B, four an A, on the principle that demonstrated progress is what is being assessed.[302] A complementary scheme caps the required projects at a middling grade and awards the rest for something the student conceives themselves, with no guidance because nobody has done it before; it is slow and difficult to assess, and it is what instils the tenacity the assessment is really after.[302] Teaching reasoning requires problems whose success or failure is evident to the student as well as the instructor; an essay cannot be marked down for insufficient thinking in a way the student can act on.[302]

Frequent low-stakes assignments serve as attendance and engagement instrumentation as much as assessment: they take minutes, they show the student their marks accumulating, and they let the instructor see in the grade book which students are fading and reach out before they are lost.[497] Distributing notes in advance and recording lectures changes what a lecture is for: an hour spent transcribing equations leaves very little taken in, and a recording that can be paused removes the pressure to keep up in real time.[579]

One course opens not with technical content but with mindset — what approach the student is going to take when something is not working — since nothing about the subject is easy or simple.[276]

### Tools and frameworks

Tool choice in teaching is an employability decision: a free design flow lacks process design kits for smaller nodes and is not what industry uses, so students are taught the commercial tool even where the free one is a good tool.[297] The standard objection to teaching with industrial tools is that the tools will become outmoded.[497] Higher-level frameworks — a Python interface to FPGA hardware, for instance — are used heavily in teaching because they lower the barrier to entry, where a twelve-week course cannot start at the transistor and build to a Linux system on custom hardware.[466] Silicon itself can be designed with education as a stated purpose: the RISC-V cores in the RP2350 microcontroller were included largely for their educational value, both for users of the chip and for the design team learning to implement a new architecture inside a familiar system.[687]

### Instructors

A class taught by someone from industry hones in on how the theory is actually used in one company's work, and in particular on CAD tools — how they process information and what assumptions they make — which is how engineering is actually done and is not conveyed by paper-and-pencil theory.[497] Kent Lundberg, who teaches half time and consults the rest, brings the practice into the classroom — build the hardware, make it work, and do the theory and the analysis as well — an approach some faculty look down on.[119]

Students are generally unaware that at a research university the professor's primary job is research rather than teaching, which explains a great deal about availability that is otherwise read as indifference.[283] A modern class is interactive in a way earlier ones were not: a room of students with computers pushes back on points and checks claims during the lecture, which requires the instructor to know the material rather than deliver it.[113] Students who do not yet know that something is impossible generate ideas that more often than not turn out to be achievable, where someone with years in industry would have been hardened out of proposing them.[113]

Teaching well requires re-entering the beginner state, and the part hardest to reconstruct is not the missing knowledge but the feeling of not knowing where to turn or what to search for; writing down what one struggled with at the time does not fully preserve it.[472] Teaching a subject is also how one comes to know it: an instructor drafted to cover a computer architecture course had done poorly in that course as an undergraduate and knew it backwards by the time the semester ended.[250]

Students are trained to ask questions in order to be given the answer rather than out of inquisitiveness, so part of the teaching task is pushing them to work it out themselves.[127] Asking what project to work on is asking someone else to do part of the work: choosing the problem is the skill, and years of being handed assignments is what leaves people unable to choose one.[669]

## Alternative and supplementary pathways

### Institutional experiments

One engineering-only college treats its own students as the experiment: the institution's principal research output is attempts at new ways to educate engineers.[218] That faculty was assembled from local engineering colleges and from people specifically interested in researching how others learn, rather than from a single disciplinary pipeline.[218] Its offerings include a one-credit seminar covering product safety — the regulatory process, what a hipot test is as distinct from an ESD test, why one grounds — the kind of course that conventional programmes do not contain at all.[218]

Dave Young's summer engineering programme for school students is designed around the experience of having made something work: students are at a soldering iron within an hour of arriving on the first day, choosing from about 130 projects or designing their own, and spending the following six weeks doing whatever it takes to make it work.[305] Each student chooses their own project, and the programme runs at a three- or four-to-one student-to-staff ratio, which is necessary precisely because the staff have not built those projects themselves and are working them out alongside the student.[601] The rationale is that showing school students the joy of creating something new changes what they choose to do with their free time, which is what actually determines whether they enter the field.[305]

Mark Palmeri's programme addressed the gap between analytic problem sets and practical building by creating an opt-in elective track of courses built around practical skill building, testing and analysis, intended to make students feel competent to advertise themselves as engineers and to execute what a team asks of them.[711]

### Vocational routes and co-operative education

British apprentice schemes take students directly from school and train them for three years in soldering, board assembly, mechanical assembly and machining. Some become technicians; some go on to engineering degrees, and an engineer who came up that way — hands first, theory afterwards — is among the most valuable, because they carry the reference points for why a one-millimetre plastic sidewall or an unmachinable part is a mistake.[588]

Not every engineer needs a doctorate. If the definition of the work is taking knowledge from the scientists and creating and maintaining systems that benefit society, vocational training reaches it; the objective is more routes in — a two-year degree, a one-year certificate — rather than one education fitted to everybody.[497] Don Wilcher's two-year technician programme, staffed by instructors holding master's degrees in physics, electrical engineering and mathematics, delivered analysis and critical thinking alongside the practical qualification, which carried through into subsequent degree study.[620]

A co-operative education placement adds a semester or so to a degree but supplies both a large correction to how much the student actually knows and paid work; the four-year length of a degree is itself arbitrary.[508]

### Bootcamps and self-directed learning

Beginner programmes and bootcamps are stepping stones rather than substitutes: they get someone past the point of self-motivation, and real engineering is learned on the job, from a course, a bootcamp or a degree alike.[233] Beginner classes convert into project work far less often than expected: after running beginner classes and open build sessions at one fabrication laboratory, the overlap ran the opposite way — people came to the open sessions first and then took the classes.[550]

Intimidating concepts — real-time operating system primitives, machine learning — are best approached against a problem the learner actually has; read cold, without a use case, they do not stick.[653]

## The transition to industry

It is treated as a basic fact of the industry that a graduate emerges with a foundation and essentially no ability to do practical work, which is why companies need their own training programmes.[241] What a degree should leave a graduate with is the tools to go and learn, plus enough confidence to believe they can do a thing — a belief that will be wrong many times and remains useful.[194] On-the-job training has thinned because companies decided to rely on schools to provide it, even though what schools provide is the theoretical side.[124] The division of labour between school and job is that school builds the model of how a processor works and why the constraints led the hardware to evolve as it did, and the specific numbers — a three-cycle cache budget, say — are learned on the job while trying to build one.[721] Being able to build things does not make someone a strong academic engineer, and the gap between solving equations in an examination and working in the field persists in both directions.[712]

Recruiting for applications and systems work is done by hiring from industry and by seating people who have the basic skills next to people with practical experience so they learn from them; what a degree supplies is the ability to learn the practical material afterwards.[185] A first job that requires error and power budgets across all parts teaches something a build-it-and-see approach does not: how to know in advance whether the design will meet its specification over the whole population, rather than assuming that because the first one worked the thousandth will.[305] Trade-off balancing — more power means more heat, less power means a more expensive part — is central to the work and is not exercised by recipe-style laboratory classes, only by project work where the design is genuinely open.[366] The engineers who did best were not distinguished by their grasp of physics but by building relationships with field applications engineers and salespeople, getting early information, navigating meetings and constructing project schedules — none of which universities teach well.[512]

### Hiring signals

A demanding practical course becomes a hiring signal that industry recognises, and the recognition attaches to the accomplishment in the application space rather than to having completed the problem sets.[711] The signal can be strong enough to hire on directly: a candidate who took a particular demanding project course, struggled with it and enjoyed it, is hireable on that basis alone.[132] Candidates who can describe only the class project everyone else also did are indistinguishable at a recruiting event; anything outside the required curriculum — a co-op placement, a project of one's own — is what differentiates a graduate.[262] Short courses on a résumé show that someone is proactive about learning, but count for very little once there is experience to look at instead.[512]

Small undergraduate engineering colleges function as concentrated recruiting grounds, and regional employers claim their graduates early, which is why their alumni are numerous in one industrial region and unfamiliar elsewhere.[437]

The material a designer most needs and is least likely to have been taught is basic electromagnetic compatibility and the mental models of how electricity actually moves; vendors have progressively taken over that education because they need engineers capable of using their products.[718]

## Access and regional variation

Access to engineering study is not uniform. Asylum seekers in the United Kingdom were unable to enter engineering courses for about six years, and a campaign directed at vice chancellors and parliament secured equal access at more than seventy-five universities.[549] The vocabulary barrier can be more fundamental than not knowing what to search for: sign languages developed without words for resistors and the rest of the electronics vocabulary, so a deaf engineering student and instructor face a gap in the shared language itself.[400]

Regional practice differs in what engineering is for: in several Asian countries engineering is treated as a step to management, and remaining an engineer after ten years is read as a failure rather than as expertise.[54] Educational emphasis differs as well: teaching in Asia was observed to be more practical, with less of the theoretical basis, while European students would openly challenge an error deliberately planted in an equation where American audiences did not.[54]

Where students live shapes how universities compete: in Australia students typically stay at home or nearby and choose among the universities in their city, rather than moving across the country to a school chosen for its reputation.[46] The Australian accreditation body encourages, without compelling, all universities to cover the same base material, so engineering courses there are fairly similar to one another.[46]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 33 | Bob Widlar, Electronic Design, FIRST Robotics - Monday, Meta Monday | https://theamphour.com/the-amp-hour-33-monday-meta-monday/ | |
| 43 | An Interview with Jeff Keyzer and Jeremy Blum - Audacious Arduino Arguments | https://theamphour.com/the-amp-hour-43-audacious-arduino-arguments/ | |
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ | |
| 54 | An Interview with Jack Ganssle - Embedded Elchee Epexegesis | https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/ | |
| 83 | Aggravating Agersia Agiotage | https://theamphour.com/the-amp-hour-83-aggravating-agersia-agiotage/ | February 19, 2012 |
| 109 | An Interview with Larry Sears - Hexagram Hardware Holism | https://theamphour.com/the-amp-hour-109-hexagram-hardware-holism/ | August 19, 2012 |
| 113 | An Interview with Scott Miller - Sudden SinoAmerican Synthesis | https://theamphour.com/the-amp-hour-113-sudden-sinoamerican-synthesis/ | September 16, 2012 |
| 116 | Distribution, Wozniak & Robots - Early Eight-bit Endgame | https://theamphour.com/the-amp-hour-116-early-eight-bit-endgame/ | October 7, 2012 |
| 119 | An Interview with Dr. Kent Lundberg - Luculent Linear Legacy | https://theamphour.com/the-amp-hour-119-luculent-linear-legacy/ | October 28, 2012 |
| 124 | SpaceX, Enclosures & Startups - Urging Unemployment Ullagone | https://theamphour.com/the-amp-hour-124-urging-unemployment-ullagone/ | December 3, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 132 | Melbourne, Hackerspace & Calibration - Vacuuous Vortex Verification | https://theamphour.com/the-amp-hour-132-vacuuous-vortex-verification/ | February 11, 2013 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 185 | An Interview with Hank Zumbahlen - Zoppa Zumbahlen Zateticism | https://theamphour.com/185-an-interview-with-hank-zumbahlen-zoppa-zumbahlen-zateticism/ | February 17, 2014 |
| 194 | An Interview With Todd Bailey - Embedded Embrasure Engineering | https://theamphour.com/194-an-interview-with-todd-bailey-embedded-embrasure-engineering/ | April 14, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 233 | Glass and Gongkai GSM - Unzymotic Ursidae Upbuilding | https://theamphour.com/233-glass-and-gongkai-gsm-unzymotic-ursidae-upbuilding/ | January 20, 2015 |
| 241 | An Interview With Chuck Peddle - Charismatic Chipmaking Coryphaeus | https://theamphour.com/241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus/ | March 18, 2015 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 262 | Jobs For Weirdos | https://theamphour.com/262-jobs-for-weirdos/ | August 12, 2015 |
| 276 | Eating An Elephant | https://theamphour.com/276-eating-an-elephant/ | December 2, 2015 |
| 283 | An Interview with Jonathan Ellis | https://theamphour.com/283-an-interview-with-jonathan-ellis/ | January 20, 2016 |
| 297 | An Interview with Jake Baker | https://theamphour.com/297-an-interview-with-jake-baker/ | May 4, 2016 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 305 | An Interview With Dave Young | https://theamphour.com/305-an-interview-with-dave-young/ | June 29, 2016 |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ | July 6, 2016 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ | |
| 413 | A House of FR4 | https://theamphour.com/413-a-house-of-fr4/ | October 28, 2018 |
| 437 | An Interview with Chrissy Meyer | https://theamphour.com/437-an-interview-with-chrissy-meyer/ | April 7, 2019 |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 466 | An Interview with Ryan Cousins | https://theamphour.com/466-an-interview-with-ryan-cousins/ | November 10, 2019 |
| 470 | Just Add Salt | https://theamphour.com/470-just-add-salt/ | December 8, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 497 | An Interview with Brock LaMeres | https://theamphour.com/497-an-interview-with-brock-lameres/ | June 21, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ | July 18, 2021 |
| 560 | High End Audio with Remco Stoutjesdijk | https://theamphour.com/the-amp-hour-560-high-end-audio-with-remco-stoutjesdijk/ | October 3, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 588 | Siloed Engineering with Leigh Brady | https://theamphour.com/588-siloed-engineering-with-leigh-brady/ | May 8, 2022 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 620 | Engineering Education with Dr Don Wilcher | https://theamphour.com/620-engineering-education-with-dr-don-wilcher/ | February 20, 2023 |
| 653 | Benjamin Cabé Nose Zephyr | https://theamphour.com/653-benjamin-cabe-nose-zephyr/ | December 11, 2023 |
| 669 | Freelance PCB Design with Petr Dvorak | https://theamphour.com/669-freelance-pcb-design-with-petr-dvorak/ | June 6, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 711 | Medical Electronics Education with Mark Palmeri | https://theamphour.com/711-medical-electronics-education-with-mark-palmeri/ | December 21, 2025 |
| 712 | Robots Everywhere with Aaed Musa | https://theamphour.com/712-robots-everywhere-with-aaed-musa/ | January 19, 2025 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
| 721 | Chip Design for Fun (and Waffles) with Julia Desmazes | https://theamphour.com/721-chip-design-for-fun-and-waffles-with-julia-desmazes/ | April 8, 2026 |
