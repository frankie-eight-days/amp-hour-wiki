---
title: CircuitPython
concept: circuitpython
generated: 2026-08-08
model: kimi-k3
writer-bakeoff: true
---

CircuitPython is a fork of the MicroPython programming environment created by Adafruit, originally motivated by the absence of a consistent hardware API across the boards MicroPython supported.[383] Its stated goal is a uniform hardware foundation across every target platform it runs on.[383] The project is defined to include not only the installed runtime but also its guides, API reference documentation, driver support, Discord community, and code of conduct.[383] It is designed principally for people who have never programmed, and its decisions are not optimised for users arriving from Arduino, MicroPython, or C.[383]

## Origin

MicroPython is a Python implementation for microcontrollers; Adafruit began by compiling it for the Atmel SAMD family and renamed the result, adopting a more hardware-specific focus.[400] Scott Shawcroft created the fork after concluding that MicroPython did not present a consistent story across all the boards it supported.[383] Hardware support began with the Atmel SAMD21 and SAMD51 and subsequently extended to Nordic nRF51 and nRF52 parts.[422]

Adafruit's leadership, Limor Fried and Phil Torrone, committed to MicroPython and CircuitPython as the company's future platform direction, a commitment Shawcroft characterised as a strategic bet.[383]

## Execution and development model

CircuitPython compiles source code to bytecode once, up front, rather than reinterpreting source at runtime.[383] The binary flashed to a board is machine code containing the virtual machine together with the board's pin data structures, and per-board builds are published as GitHub releases.[383]

The user-facing development model dispenses with the conventional compile-and-upload cycle. A CircuitPython board enumerates as a USB mass-storage device carrying editable example code; editing and saving the file runs the program, with no separate flashing step.[383] In practice the user opens the file, edits it, and saves, at which point the board soft-reboots.[377] Because code is interpreted on the device, iteration does not require erasing and reprogramming the chip.[383]

The entry file is named code.py, and code.txt is also accepted, on the assumption that target users may not know what Python or a main function is.[383] Storing source on the device itself also removes a failure mode familiar to embedded developers: an undo-less editing session in which a previously working project becomes unrecoverable after a forgotten change.[383]

## Design philosophy

CircuitPython deliberately accepts lower execution performance than MicroPython in exchange for closer CPython compatibility, so that existing Python documentation and idioms transfer to the embedded environment.[383] The design optimises iteration time rather than execution speed, on the argument that short iteration cycles are what beginners need.[383]

Code-generation wizards of the Atmel Start or STM32Cube type are unsuited to CircuitPython, because the runtime is dynamic and neither the user's code nor the pin assignments are known at build time.[383] Removing the IDE and driver installation also eliminates the most common category of beginner support request, since installation and COM-port problems dominate vendor support email.[458]

## Portability and hardware support

CircuitPython libraries can run unmodified on a desktop host—Windows, macOS, or Linux—and then be redeployed to a Raspberry Pi or a CircuitPython board.[461] The Adafruit Trinket M0 ships with CircuitPython preinstalled.[377] By 2022, CircuitPython ran on Espressif's ESP32-S2 breakout boards, which additionally removed the need for an external USB-to-UART converter.[578]

## Adoption

CircuitPython has been adopted in commercial products. Reality Instruments' commercial boards were built on CircuitPython specifically so that end users would find them easy to program.[441] By 2021, CircuitPython was in use in United States middle-school technology teaching.[561]

Adoption has not been frictionless. The similarity between the MicroPython and CircuitPython names is itself a practical hazard: confusing the two cost one practitioner a deadline on an RP2040 project.[550]

## Reception and debate

Whether CircuitPython should be adopted for real work has divided practitioners. Dave Jones dismissed it on first mention as one more entrant in a crowded field, calling it roughly the fiftieth development platform to appear in five years.[364] Jones later declined to learn it altogether, arguing that doing so would dissipate the enthusiasm that starts a project.[530]

Chris Gammell recommended CircuitPython from early on, while acknowledging that doing so contradicted his own prior position against interpreted languages on hardware.[364] By the following year he expressed confidence in CircuitPython and MicroPython for real work, a reversal of his earlier stance.[389] Gammell also revised a long-held dismissal of simplified programming interfaces, conceding that each new platform imposes a fresh learning cost on its users.[395] His position eventually extended to practice, shipping commercial products built on the platform.[441] Ken Burns has supported CircuitPython as a market observation about non-engineer users rather than a personal preference, describing himself as an embedded developer who would personally choose C.[458]

A separate question concerns the fork's motivation. Gammell had assumed the fork was driven by hardware focus, but the stated motive was the audience mission: providing an excellent experience for people who have never programmed in their life.[383]


## Further reading

- [Circuit Python 2.1 is out!](https://blog.adafruit.com/2017/10/17/circuit-python-2-1-0-released/) — via #364
- [adafruit's Trinket M0](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/overview) — via #377
- [JLink (edu) debugger that Chris got from Adafruit](https://www.adafruit.com/product/1369) — via #383
- [Tannewt](http://tannewt.org/) — via #383
- [micropython](https://micropython.org/) — via #383
- [SAMD21](http://ww1.microchip.com/downloads/en/DeviceDoc/40001884A.pdf) — via #383
- [python](https://en.wikipedia.org/wiki/Python_(programming_language)) — via #383
- [Automate The Boring Stuff book](https://automatetheboringstuff.com/) — via #383
- [Interpreted vs compiled languages](https://en.wikipedia.org/wiki/Interpreted_language) — via #383
- [Machine code vs byte code](https://www.quora.com/What-is-the-difference-between-byte-code-and-machine-code-and-what-are-its-advantages) — via #383
- [MicroPython vs CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython) — via #383
- [SAMD51](https://www.microchip.com/wwwproducts/en/ATSAMD51N19A) — via #383
- [nRF52](https://www.nordicsemi.com/Products/nRF52-Series-SoC) — via #383
- [The python struct library](https://docs.python.org/3.0/library/struct.html) — via #383
- [Scott has a great tutorial about using a JLink debugger](https://learn.adafruit.com/debugging-the-samd21-with-gdb) — via #383
- [Microtrace buffer](https://learn.adafruit.com/debugging-the-samd21-with-gdb/micro-trace-buffer) — via #383
- [You can download the latest CircuitPython release for various adafruit boards.](https://github.com/adafruit/circuitpython) — via #383
- [Adafruit has a Discord server where they discuss CircuitPython](http://adafru.it/discord) — via #383
- [The Adafruit CircuitPython group does a weekly voice meeting on Discord](https://blog.adafruit.com/2018/02/05/circuitpython-weekly-meeting-adafruit-circuitpython/) — via #383
- [A blog post about the plans for CircuitPython in 2018](https://blog.adafruit.com/2018/01/29/circuitpython-in-2018/) — via #383
- [CircuitPython 3](https://blog.adafruit.com/2018/07/09/circuitpython-3-0-0-released-adafruit-circuitpython/) — via #400
- [ESP32-S2](https://www.espressif.com/en/products/socs/esp32-s2) — via #578

## References

| Episode | Title | URL |
|---|---|---|
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ |
| 441 | Motivational Speaker | https://theamphour.com/441-motivational-speaker/ |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ |
| 578 | Histogrammic or Histomagraphical | https://theamphour.com/578-histogrammic-or-histomagraphical/ |
