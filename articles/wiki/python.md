---
title: Python
concept: python
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Python is an interpreted high-level programming language created in the early 1990s, descended from system-administration languages such as Perl but built on the opposing principle that there should be one obvious way to do a thing rather than ten.[323] It has grown well beyond conventional software engineering into scientific and engineering work, because it is accessible to people whose job is not programming, and teaching institutions have moved introductory courses onto it in place of Scratch, Java or C++.[383] Its characteristic role in hardware and embedded engineering is as glue: joining subsystems written in other languages, scripting quick tasks, and handling the small jobs that surround a product, alongside C or C++ for firmware that must be controlled directly.[355]

## History and design principles

Python was created in the tradition of system administration languages such as Perl, but on the opposing design principle: where Perl encourages many ways to accomplish a task, Python holds that things are meant to be obvious and easy, with only one way to do it, which is what makes it comparatively easy to learn while remaining capable enough for large production systems.[323] The language grew into scientific and engineering domains rather than remaining confined to conventional software engineering because of that accessibility, and the same accessibility drove teaching institutions to adopt it for introductory courses.[383]

The argument for putting a high-level language of this kind on a small platform at all is that it lets people work in the language they already know rather than forcing everyone onto C or assembler—the same logic that justifies any development platform aimed at an existing community.[172]

## Language design

The reference implementation used on the desktop is CPython, so called because the core of the language is written in C.[323] Performance-sensitive numerical libraries are likewise C implementations exposed through a Python interface, so that a Fourier transform is called as a Python function while executing as native code; the language is therefore designed to be extended in C wherever optimisation is required.[323]

The native dictionary type is what makes Python economical for structured data: parsing a JSON document yields a dictionary that can be operated on immediately, whereas the equivalent in C requires either a library or a hand-written parser with buffer-length checking, turning a few lines into ten or twenty.[323] The default numeric type is an arbitrary-precision integer, a choice that suits an environment where memory is effectively unlimited but is not performant for small arithmetic; in C, by contrast, the width of the chosen integer type determines how many registers and processor operations an operation consumes, and therefore its speed.[323]

Python's dynamism—in which attributes can be added to and removed from an object at run time—is what makes compiling it to native code harder than compiling an earlier interpreted language such as BASIC, where compilers were straightforwardly retrofitted.[323] Object-oriented code also resists static reading in a way procedural C does not: the sequence in which pieces execute cannot be seen from the page, whereas a C program can be traced as a chain of calls from a starting point, and this difference is the main obstacle for hardware engineers moving from C into Python libraries and drivers.[422]

Because desktop Python is closely integrated with C, the struct module unpacks a byte string according to a declared C type, so a sixteen-bit unsigned register read from hardware is converted to a Python integer simply by naming the corresponding format character.[383]

## Embedded implementations

### MicroPython

MicroPython is an implementation of Python for microcontrollers and other memory-constrained environments.[323] The core language syntax is unchanged, so a loop blinking an LED is written exactly as it would be on the desktop; the divergence is in the libraries, because the desktop standard library, which carries a module for nearly every task, cannot be fitted into a small chip.[323] Firmware is built separately for each target, so the language is available only on the handful of platforms that have a maintained port, which makes chipset choice a constraint on using it at all.[329]

The design pattern that makes an embedded Python port useful on real products is mixing languages by layer: the mundane, non-real-time work such as talking to web services, authenticating and processing text is written in Python, while register access and timing-critical signal generation are added as C functions exposed to the interpreter through a macro syntax and compiled into a rebuilt firmware image; the Python code calls them as ordinary functions without knowing they are native.[323] One microcontroller port goes further and accepts a decorator marking a function body as ARM assembly, which is compiled during the firmware build into an optimised routine, although C is close enough to assembly that the facility is rarely needed.[323]

The interactive prompt is the practical difference from a compiled embedded workflow: variables can be assigned and printed, functions and classes defined at the prompt, and a two-line sequence will turn a display fully on and off with immediate feedback and no build step.[323] A browser-based remote prompt can also copy files onto the board's own filesystem, so a missing library or a data file is transferred without physically moving the board, and the file is then read from Python with the ordinary open, read and write calls.[323]

### CircuitPython

CircuitPython diverged from MicroPython by deliberately choosing to be less performant in order to behave more like desktop CPython, on the reasoning that conformance lets the language's existing documentation and community resources apply directly to the embedded environment.[383] Its design decisions are aimed at people who have never programmed: the board reloads code automatically when the file is saved, and the entry-point file may be named code.txt as well as code.py, because a newcomer is unlikely to know what a main function is but will recognise the word code.[383]

Portability was addressed architecturally by factoring the shared API implementation out of the individual chip ports so that it is identical across all of them, with port-specific C beneath; supporting a new microcontroller family then requires only implementing a set of C functions, and the Python interface comes with it, which keeps written tutorials valid when the processor changes.[383] Without that factoring, code written for one chip carries no guarantee of running on another.[383]

### Trade-offs

The cost of an interpreted language on a microcontroller is paid in memory, interpreter overhead, battery performance and ultimately capability: the same part running Python does a fraction of what it would do in C, and takes longer to do it.[271] Choosing it optimises for the start of the project rather than for the shipped product, on the same pattern as using a development board in a commercial design.[271] The failure mode of that choice is discovering it late: a team that optimises repeatedly and still misses its target has already committed the hardware, and ends up writing everything in C anyway; the corresponding safeguard is to evaluate the performance and memory envelope before the board exists.[383]

The position taken by the maintainers is that an embedded Python port is not intended to replace C but to be one more tool, and that rejecting it on grounds of insufficient performance or excessive memory use is a legitimate outcome of evaluation; there is no universal best programming tool, and the language a practitioner already knows is a real input to the decision.[323] Where the objective is simply to get a microcontroller-class system working, C is the wrong choice and a higher-level language is the better fit, because the depth of control C provides is not needed.[329]

## Role in hardware and embedded engineering

### Glue language

Writing software is treated as a required tool in a hardware engineer's kit rather than a separate discipline, with C or C++ as the baseline for firmware that must be controlled directly and a scripting language for everything around it.[355] Python's characteristic role is as glue: joining subsystems written in other languages, scripting quick tasks and handling the small jobs that surround a product.[355] A single-board product with a custom Linux kernel typically spans the full language range at once: C for the low-level drivers and kernel work, Python to glue components together, and shell scripting optimised to shorten a boot that would otherwise take a minute.[258]

### Host-side hardware control

General-purpose hardware hacking adapters invert the usual embedded model: the device is a microcontroller that exposes its peripherals over USB, and the development work is done in a Python environment on the host rather than as embedded firmware, giving script-level access to SPI, I2C and JTAG.[352] The earlier generation of such tools communicated over a serial interface primarily because of the driver situation rather than by preference; once libusb and libftdi abstracted the drivers away, writing host-side Python that toggles pins and moves raw bits directly became straightforward and portable across operating systems.[318]

A productive development sequence for hardware protocol work is to implement the whole function in host-side Python first, exercising the device's registers until the behaviour is understood, and only then migrate it piece by piece into C running standalone on battery power.[442]

### Software-defined radio

In software-defined radio the graphical flow-graph editor is a front end that generates Python, and reading that generated code is the recommended way for an existing programmer to learn the framework and reuse its signal-processing blocks directly.[161] The framework's layering is deliberate: the core processing blocks are written in C++ because sample rates in commercial and research systems demand direct access to the architecture for optimisation, while a Python layer provides the user-facing interface on top.[381]

### Test, measurement and instrumentation

Bench instruments are increasingly shipped with an open-source host-side Python library alongside the graphical interface, which turns the instrument into something scriptable and lets an entire laboratory be driven from one desk without touching each instrument.[527] Where an instrument streams continuously rather than capturing and transferring a buffer, the conventional instrument-control stack does not fit, and the vendor implements its own Python library instead; building the low-level driver in C and providing bindings, rather than writing the driver in Python, allows the same interface to be offered to several languages and an older API to be preserved through an adapter layer.[527]

A production test tool is made integrable by offering two independent control paths, a Python library for direct integration and a plain ASCII command interface over a serial port usable from any language; the pattern being avoided is an API that can only be reached by linking a Windows DLL or only from C, which ties the factory floor to one operating system.[461] Older laboratory equipment with instrument-bus interfaces remains usable because its awkward command language can be wrapped in Python, which is what makes second-hand instruments worth acquiring given that their measurement performance has often not been superseded.[455]

Processing manufacturing test data in Python and exporting it into a statistics package or spreadsheet is the combination that makes production data usable for histograms and process capability analysis; the precondition is a production tester designed before the line starts, focused on the major features, the parts most likely to fail and the headline performance metrics, because a team that waits for a failure before instrumenting has no data at the moment it is needed.[328] Notebook environments that interleave Python code, results and plots take over data collection, analysis and visualisation tasks historically done in proprietary instrumentation software, and are used the same way in teaching, where a circuit is solved analytically, then in simulation, then numerically, so that disagreements between the three become the lesson.[450]

The cheapest entry into automated firmware testing is a Python script that opens a serial connection to a command shell already present on the device, issues commands and checks the responses; it works because most projects already have such an interface, and it sidesteps the difficulty of untangling hardware dependencies to run code on a development machine.[556]

### Signal processing and data recovery

Algorithm development on sampled real-world data depends on fast iteration in a scripting language: a year of repeatedly processing recorded waveform data in Python made a signal-processing algorithm tractable, where writing code and testing it against physical sources each cycle would not have converged at all.[513] Filter design work that was historically done in a proprietary numerical environment is now done with the Python numerical and scientific libraries, which cover the same filtering tools.[513] Recovering data from an instrument that exports only an undocumented binary file or a badly formatted spreadsheet is done by opening the binary in a hex editor, identifying repeating patterns, and writing a Python decoder that converts it into a usable log format.[363]

### Design-tool scripting and visualisation

Design tools expose Python scripting interfaces that let a board be rendered as an image: a script generates a stack of coloured SVG layers from the layout and exports a PNG that is applied to a mechanical model as a decal, reaching eighty to ninety percent of a photorealistic board while omitting the material properties of real laminate.[473] Board costing is a standard scripting target: a script takes a target build quantity, queries distributor pricing for every line on the bill of materials and returns a comparative cost estimate, which is the class of automation that in-tool scripting languages were used for before Python integration existed.[181]

An open tool chain at the bottom of the stack is what makes the Python layer above it possible, because modifying the tool or manipulating its files becomes tractable; the same argument applies from open synthesis tools up to open board design software.[449] Python is used as the connective layer between otherwise incompatible engineering tools: field-solver results exported in a standard interchange format are imported through the scripting console of a 3D package and rendered on top of the actual board design, and once that console exists, simple solvers can be implemented inside the visualisation tool itself for early concept work before returning to the professional solver.[695] The same kind of scripting interface converts simulation output into device data: a fluid simulation rendered in a 3D package was sliced by a rotating plane and imaged frame by frame through a script to produce the binary volume data played back on a volumetric display.[697]

### FPGA toolchains and accelerators

Python-to-hardware compilers exist alongside C-to-hardware compilers, aimed at the mathematically heavy signal-processing content that increasingly dominates FPGA designs, where coding every structure by hand in a hardware description language each time is uneconomic.[150] The Python layers built on open FPGA tool chains are templating and generation systems rather than translators: they emit a peripheral such as an SPI controller from a high-level description without the user working through its internals, and explicitly do not convert Python into hardware; the advantage over a vendor's graphical block-assembly tool is that the generated source is available.[375]

A host-to-FPGA bridge exposes the internal bus so that Python running on a workstation can read and write the registers of peripherals implemented in the fabric; because the register-access API is preserved, the same scripts can later run on a soft processor core inside the FPGA, where the bridge disappears and the calls become direct memory accesses, converting a tethered development setup into a standalone device without rewriting the code.[375] Software libraries for hardware accelerators are typically implemented in C or C++ with automatically built binaries for each platform, and language reach is added through bindings, commonly Python and a robotics middleware interface, with further bindings contributed by the community when the project is open.[517]

### Other applications

Game and machine rule logic can be lifted into Python entirely: a framework for electromechanical machines provides the base on which all rules are written in Python and run on the same controller board that could otherwise execute the original firmware images, which allows defects to be fixed and features added at the cost of introducing new ones.[485] Motion control mathematics such as converting polar to Cartesian coordinates is commonly prototyped as a Python script off the machine and then reimplemented to run in real time on the controller once a fast enough processor is available, so that the transformation happens as each line is received rather than in preprocessing.[438]

## Toolchain considerations and failure modes

Embedded build environments are fragile in a specific way: a build script depending on one Python version breaks silently when a different version is installed, or when a new team member arrives on a different operating system; putting the build environment in a container freezes the interpreter and compiler versions and ships them with the repository, so a fresh clone builds regardless of the host.[537] System integration failures usually trace to one specific assumption rather than to the whole project collapsing, and toolchain assumptions about a scripting language are a recurring example: expecting to cross-compile Python 3 into an embedded Linux distribution and finding the toolchain unusable can cost weeks, and the countermeasure is to attack every unknown and every step that worries anyone at the start of a prototype rather than at the end.[550]

On embedded Linux, timing-critical pin toggling cannot be done from a user-space Python script even on a processor fast enough to meet the timing, because the scheduler decides when the code runs; moving the routine into a kernel module gives nanosecond-resolution delays and direct GPIO calls.[515] Dependency weight is a practical cost of the ecosystem: pulling in the scientific stack to use one or two packages, such as an instrument-control module, has meant a download of over a gigabyte, which was nonetheless the easiest route to the required functionality.[472] Long-term-support distributions matter to anything built on an interpreter, because a vulnerability discovered years later is backported to the supported release rather than requiring a migration, with support periods of five years as standard and longer terms available commercially.[720] Custom scripting eventually loses to a maintained system for operational work: an inventory and build-forecasting workflow assembled from custom Python scripts depended on the owner being disciplined enough to run it, which meant it did not get run, and a service that is simply always running removes that friction.[722]

## Learning and pedagogy

A method for learning a language holds that reading someone else's code is insufficient and the material must be retyped, compiled and debugged so that the errors are found first-hand and the process becomes muscle memory; the same method transfers to electronics, where one replicates a demonstrated circuit, finds what was done wrong, and repeats.[127] A language is learned effectively through a project or a domain course that requires it rather than through a course about the language: taking a machine learning and computer vision course reduced the unknowns in an independent robotics project from roughly ninety-five percent to forty percent, a level at which the remainder can be searched for and read up on, and the Python competence came as a by-product.[373] Reading the code of an established project in one's domain corrects specific habits, such as inefficient ways of building and slicing lists, in a way that studying the language in isolation does not.[373]

Being handed a book and told to learn a language produces nothing without a task, whereas needing to talk to a sensor or drive an indicator produces working code quickly, which is the argument for organising beginner material around outputs rather than around language features.[323] Beginners do not want to run code; they want an output, a light that blinks or a motor that moves, and once they have obtained it once they begin investigating how to do it faster, better or at larger scale, which is the point at which the underlying electronics gets learned.[323] Guided wizards are a weaker answer to the beginner problem than worked examples, because a wizard conceals the underlying operation while asking the same questions in a different form; the concept to be understood, such as what a breakpoint is, is unchanged whether it is set by clicking a button or typing a command.[383] Documentation is consulted by searching for a specific question rather than read linearly, so an executable tutorial split into small findable chunks serves practitioners better than a single large document that is never opened.[181]

Graphical parallel programming environments used to introduce children to programming create a specific discontinuity when learners move on: everything in the graphical system happens concurrently by default, whereas achieving concurrency in a conventional scripting language requires deliberate use of libraries or threading.[467] Every abstraction leaks, at minimum through performance, so understanding what lies beneath the layer being worked in yields better decisions even for a programmer several levels of abstraction above the hardware.[444]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 150 | Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness | https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/ | June 17, 2013 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ | |
| 258 | An Interview with Bertrand Irrisou and Gerald Friedland of Audeme | https://theamphour.com/258-an-interview-with-bertrand-and-gerald-of-audeme/ | July 14, 2015 |
| 271 | Amazon Moves In, Dave Says Run | https://theamphour.com/271-amazon-moves-in-dave-says-run/ | October 14, 2015 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 328 | The Ghost of Keyzermas Past | https://theamphour.com/328-the-ghost-of-keyzermas-past/ | December 21, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ | |
| 352 | Conning with Michael Ossmann | https://theamphour.com/352-conning-with-michael-ossmann/ | July 17, 2017 |
| 355 | The Internet of Septage (with Akiba) | https://theamphour.com/355-the-internet-of-septage-with-akiba/ | August 13, 2017 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 381 | An Interview with Derek Kozel | https://theamphour.com/381-interview-with-derek-kozel/ | February 25, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 438 | An Interview with Bart Dring | https://theamphour.com/438-an-interview-with-bart-dring/ | April 14, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 444 | An Interview with Ben Eater | https://theamphour.com/444-an-interview-with-ben-eater/ | May 27, 2019 |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ | June 30, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 455 | Bill and Dave's Excellent Equipment | https://theamphour.com/455-bill-and-daves-excellent-equipment/ | August 19, 2019 |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ | October 6, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 513 | Audio DSP with Shannon Parks | https://theamphour.com/513-audio-dsp-with-shannon-parks/ | October 18, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ | April 5, 2021 |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ | July 18, 2021 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 695 | Making The Invisible, Visible with Sam Aldhaher | https://theamphour.com/695-making-the-invisible-visible-with-sam-aldahar/ | June 3, 2025 |
| 697 | LEDs Everywhere with Tim from Mitxela | https://theamphour.com/697-leds-everywhere-with-tim-from-mitxela/ | July 8, 2025 |
| 720 | Hyper Growth and OpenClaw Interns | https://theamphour.com/720-hyper-growth-and-openclaw-interns/ | March 31, 2026 |
| 722 | AI Tooling with Matt Liberty and Luke Beno | https://theamphour.com/722-ai-tooling-with-matt-liberty-and-luke-beno/ | April 22, 2026 |
