---
title: CircuitPython
concept: circuitpython
episodes: 24
guests: 8
explains: 16
opinion: 7
generated: 2026-08-08
model: claude-opus-5 (pilot batch, pipeline steps 6-8)
---

<!--
PRODUCTION NOTES (not for readers)
Gather: 48 census mentions across 24 episodes -> 29 pinned explains/opinion passages
after paragraph-level dedupe. NOT capped (cap is 150).
Re-grade: 6 passages discarded as trivial or as questions mis-graded as opinion;
1 strong passage (ep 383 para 87) added by hand after reading context - the census
missed it. Census reported 20 explains / 9 opinion; re-graded to 16 / 7.
Evidence packet: _packets/circuitpython.json (30 claims, 2 disagreement groups).
ATTRIBUTION: ep 383 is one of 144 corpus files whose host/guest speaker labels are
swapped (the show-open boilerplate is attached to the guest's label). Every ep 383
attribution was assigned by CONTENT, not by transcript label. Ep 651 was dropped
entirely: all 190 of its turns carry a single label, so nothing in it can be safely
attributed.
-->

CircuitPython is a fork of [[micropython]], maintained by [[adafruit]], that runs Python on microcontrollers and presents the board to a host computer as a USB mass-storage device holding an editable source file.[383] The fork was motivated by the absence of a consistent hardware API across the boards MicroPython supported, and its design consistently favours beginner iteration speed over execution speed, including an explicit decision to run slower than MicroPython in exchange for closer CPython compatibility.[383] Support began on Atmel SAMD parts and later extended to Nordic nRF and Espressif silicon.[422][578] Adoption among its early commentators was contested: Chris Gammell shipped commercial products on it within two years of first encountering it, while Dave Jones declined to learn it as late as 2021.[441][530]

## Design and operation

The fork descends from MicroPython by way of Adafruit's work compiling it for the Atmel SAMD family, after which it was renamed and given a more hardware-specific focus.[400] The trigger was structural rather than commercial: the hardware API underneath MicroPython's drivers did not present a consistent story across supported boards, and CircuitPython was intended to provide a uniform foundation across every target platform.[383]

Execution is interpreted, but source is translated to bytecode once at load rather than reinterpreted continuously.[383] What is flashed to a board is a compiled binary containing the virtual machine together with the data structures describing that board's pins; per-board builds are distributed as GitHub releases.[383]

The distinguishing workflow property is that the board enumerates as a USB drive carrying its own source code. Editing the file and saving it causes a soft reboot and re-run, with no compile or flash step, and therefore no erase-and-reprogram cycle between edits.[383][377] Because the source resides on the device, a project resumed after an interruption still carries its last working code, which removes a common loss mode in which an undo-less editing session leaves previously working code unrecoverable.[383]

Several interface decisions follow from the target audience. The entry file is named `code.py`, and `code.txt` is also accepted, on the reasoning that a user who has never programmed may not know what Python is or what a `main` function means.[383] More consequentially, the project accepts lower execution performance than MicroPython in order to remain closer to CPython, so that existing Python documentation and idioms transfer intact.[383] The stated justification is that iteration time, not throughput, is the binding constraint for beginners.[383]

The dynamic runtime is incompatible with the code-generation wizards used by vendor toolchains such as Atmel Start and STM32Cube, because neither the user's code nor the intended pin assignment is known at build time.[383]

Hardware support began on the Atmel SAMD21 and SAMD51, extended to Nordic nRF51 and nRF52 parts by late 2018,[422] and later reached the RP2040 and the ESP32-S2.[550][578] Libraries can also run unmodified on a desktop host and then be redeployed to a Raspberry Pi or an embedded CircuitPython board without modification.[461]

From 2018 the project was defined to encompass its guides, API reference documentation, driver support, Discord community and code of conduct, rather than the installed runtime alone.[383]

## Reception and debate

Adoption divided Chris Gammell and Dave Jones, and the division persisted across seven years without resolving. Dave Jones dismissed CircuitPython at its first mention as one more entrant in a crowded field, characterising it as the fiftieth development platform in five years,[364] and in 2021 still declined to learn it, on the grounds that doing so would dissipate the enthusiasm that starts a project.[530] Chris Gammell recommended it in that same 2017 episode while conceding that it contradicted his own prior position against interpreted languages on hardware,[364] reported growing confidence in it the following year,[389] and by 2019 was building commercial boards on it specifically so that end users would find them easy to program.[441] His stated reason for revising a long-held dismissal of simplified programming interfaces generalises beyond this tool: each new platform imposes a fresh learning cost, which raises the value of a simple interface.[395]

The motivation for the fork was itself disputed. Chris Gammell entered the 2018 interview expecting hardware focus to be the explanation and was corrected: the project's goal is a good experience for people who have never programmed, and its decisions are explicitly not optimised for users arriving from [[arduino]], MicroPython or C.[383] Scott Shawcroft characterised Adafruit's leadership as having committed to MicroPython and CircuitPython as the company's future platform.[383]

Vendor support was argued on commercial rather than aesthetic grounds. Ken Burns, whose company added CircuitPython support, described himself as an embedded developer who would personally choose C, and justified the decision by support volume: installation and COM-port problems are the most common category of question vendors receive, and a board that mounts as a drive eliminates that category.[458]

## Chronology

CircuitPython was first discussed in October 2017, raised alongside an admission that it undercut a previously stated position, and dismissed on the spot.[364] By January 2018 the workflow had produced a conversion, with a recommendation to try it attached to a description of the Trinket M0 edit-save-run loop.[377] In March 2018 Scott Shawcroft set out the project's design rationale in detail, covering interpretation and compilation, the fork's justification, the beginner-first mission, and the decision to treat documentation and community as part of the project.[383] Cautious commitment followed in April,[389] and hardware coverage widened past SAMD by the end of the year.[422]

Commercial and third-party adoption arrived through 2019: products shipped on it,[441] a hardware vendor added support,[458] and an instrument maker wrote a driver so that desktop and embedded targets could share libraries.[461] The disagreement over adoption remained unresolved in February 2021.[530] Thereafter CircuitPython appears as infrastructure rather than as news: as a schedule hazard when confused with MicroPython on an RP2040 project,[550] as the tool a middle-school technology teacher was using,[561] and as something an ESP32-S2 breakout simply runs.[578]

## Notable formulations

The performance trade is stated most directly as a decision to be "explicitly chosen to be less performant than MicroPython in order to be more similar to Python".[383] The name collision with MicroPython is offered as an instance of the single small misunderstanding that wrecks a schedule: "I didn't know circuit Python and micro Python were different. So I just blew my deadline."[550]


## Further reading

- [Circuit Python 2.1 is out!](https://blog.adafruit.com/2017/10/17/circuit-python-2-1-0-released/) — via #364
- [adafruit's Trinket M0](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/overview) — via #377
- [A blog post about the plans for CircuitPython in 2018](https://blog.adafruit.com/2018/01/29/circuitpython-in-2018/) — via #383
- [Adafruit has a Discord server where they discuss CircuitPython](http://adafru.it/discord) — via #383
- [Automate The Boring Stuff book](https://automatetheboringstuff.com/) — via #383
- [Interpreted vs compiled languages](https://en.wikipedia.org/wiki/Interpreted_language) — via #383
- [JLink (edu) debugger that Chris got from Adafruit](https://www.adafruit.com/product/1369) — via #383
- [Machine code vs byte code](https://www.quora.com/What-is-the-difference-between-byte-code-and-machine-code-and-what-are-its-advantages) — via #383
- [MicroPython vs CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython) — via #383
- [Microtrace buffer](https://learn.adafruit.com/debugging-the-samd21-with-gdb/micro-trace-buffer) — via #383
- [SAMD21](http://ww1.microchip.com/downloads/en/DeviceDoc/40001884A.pdf) — via #383
- [SAMD51](https://www.microchip.com/wwwproducts/en/ATSAMD51N19A) — via #383
- [Scott has a great tutorial about using a JLink debugger](https://learn.adafruit.com/debugging-the-samd21-with-gdb) — via #383
- [Tannewt](http://tannewt.org/) — via #383
- [The Adafruit CircuitPython group does a weekly voice meeting on Discord](https://blog.adafruit.com/2018/02/05/circuitpython-weekly-meeting-adafruit-circuitpython/) — via #383
- [The python struct library](https://docs.python.org/3.0/library/struct.html) — via #383
- [You can download the latest CircuitPython release for various adafruit boards.](https://github.com/adafruit/circuitpython) — via #383
- [micropython](https://micropython.org/) — via #383
- [nRF52](https://www.nordicsemi.com/Products/nRF52-Series-SoC) — via #383
- [python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) — via #383
- [CircuitPython 3](https://blog.adafruit.com/2018/07/09/circuitpython-3-0-0-released-adafruit-circuitpython/) — via #400
- [ESP32-S2](https://www.espressif.com/en/products/socs/esp32-s2) — via #578

## References

| Ep | Title | URL | Date |
|---|---|---|---|
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22nd, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28th, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11th, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22nd, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3rd, 2018 |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ | May 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 441 | Motivational Speaker | https://theamphour.com/441-motivational-speaker/ | May 5th, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15th, 2019 |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ | October 6th, 2019 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15th, 2021 |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ | July 18th, 2021 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10th, 2021 |
| 578 | Histogrammic or Histomagraphical | https://theamphour.com/578-histogrammic-or-histomagraphical/ | February 20th, 2022 |
