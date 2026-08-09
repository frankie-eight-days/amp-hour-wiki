---
title: CircuitPython
concept: circuitpython
generated: 2026-08-08
model: kimi-k3
spec: knowledge-only-v3
---

CircuitPython is a fork of MicroPython created by Adafruit, motivated by the absence of a consistent hardware API across the boards MicroPython supported; the fork's stated goal was a uniform hardware foundation across every target platform.[383] MicroPython is a Python implementation for microcontrollers; Adafruit compiled it specifically for the Atmel SAMD family and renamed the result, giving it a more hardware-specific focus.[400]

CircuitPython boards enumerate as USB mass-storage devices carrying editable code; saving an edited file runs it immediately.[383][377] The design optimizes iteration time rather than execution speed, and the project targets people who have never programmed rather than users arriving from Arduino, MicroPython, or C.[383]

## Design goals

CircuitPython deliberately accepts lower execution performance than MicroPython in exchange for closer CPython compatibility, so that existing Python documentation and idioms transfer.[383] The entry file is named `code.py`, and `code.txt` is also accepted, on the assumption that target users may not know what Python or a main function is.[383]

From 2018 the project was defined to include its guides, API reference documentation, driver support, Discord community, and code of conduct, not only the installed runtime.[383]

## Workflow

CircuitPython compiles source to bytecode once, up front, rather than reinterpreting source at runtime.[383] The binary flashed to a board is machine code containing the virtual machine plus the board's pin data structures; per-board builds are published as GitHub releases.[383]

The edit-save-run loop replaces the compile-and-upload cycle, with the board soft-rebooting on save; because code is interpreted on the device, iteration does not require erasing the entire chip, compiling, and uploading it all back.[377][383]

Storing source on the device itself removes the loss mode in which an undo-less editing session leaves a previously working project unrecoverable — the failure where a project worked the first thirty times and an unremembered change on the thirty-first edit cannot be reversed.[383] Removing the IDE and driver installation eliminates the most common category of beginner support request, since installation and COM-port problems dominate vendor support email.[458]

## Hardware support

Hardware support began with the Atmel SAMD21 and SAMD51 and extended to Nordic nRF51 and nRF52 parts.[422] By 2022 CircuitPython ran on Espressif's ESP32-S2 breakout boards, which also removed the need for an external USB-to-UART converter.[578]

## Code portability

CircuitPython libraries can run unmodified on a desktop host — Windows, Mac, or Linux — and then be redeployed to a Raspberry Pi or a CircuitPython board.[461]

## Selection guidance and practical considerations

Code-generation wizards of the Atmel Start or STM32Cube type are unsuited to CircuitPython, because the runtime is dynamic and neither user code nor pin assignment is known at build time.[383]

The similarity between the MicroPython and CircuitPython names is itself a schedule risk: confusing the two cost a deadline on an RP2040 project when the distinction between the implementations was discovered too late.[550]

Reality Instruments' commercial boards were built on CircuitPython specifically so that end users would find them easy to program.[441]

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
|---------|-------|-----|
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ |
| 441 | Motivational Speaker | https://theamphour.com/441-motivational-speaker/ |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ |
| 578 | Histogrammic or Histomagraphical | https://theamphour.com/578-histogrammic-or-histomagraphical/ |
