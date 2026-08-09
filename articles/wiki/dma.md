---
title: DMA
concept: dma
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**Direct memory access** (DMA) is a hardware mechanism by which dedicated transfer logic moves data between a system's memory and its peripherals, or between memory regions, without routing each word through processor registers.[278] By relieving the CPU of per-byte transfer work, DMA frees the processor for computation, allows peripherals to be serviced while the core sleeps, and enables sustained data rates that software loops cannot meet.[340][95] A correctly written DMA driver can speed a program by orders of magnitude, whereas an engineer unaware of the mechanism may conclude that a processor is too slow and pay for a faster one.[672]

## Operation

A DMA transfer funnels data directly between memory and an I/O peripheral, bypassing the processor's registers entirely.[278] Transfers are typically structured as blocks: the controller can be programmed with a fixed transfer block size matching a peripheral's response length, and once the controller has collected the full block it raises a completion signal that releases a task to process the data, so the CPU never handles an individual byte.[581] Because the transfer engine drives the full bus width per cycle in the background, pixel or sample data leaves memory without any per-word CPU involvement.[356]

DMA controllers and hardware peripherals give a single-core microcontroller a form of genuine parallelism, but the parallelism is limited to moving data over communication interfaces rather than to computation; the corresponding design pattern is to make every communication path DMA-driven and reserve the core for application work.[581]

### Bus arbitration and failure modes

Because a DMA-capable peripheral can act as a bus master, its interaction with other system state must be managed. On the Commodore 128 programme, a reset line asserted while the bus-mastering VIC video chip was in the middle of a DMA cycle crashed the machine, because the video chip did not respond to reset and kept the bus while the processor tried to start fetching from it.[222] The fix, implemented by Bil Herd's team, was a latch made from back-to-back open-collector gates that held the processor in reset until the DMA cycle finished and then released it, rather than any change to the video chip itself.[222] The improvised logic reflected a late-stage constraint: keeping the change within a class 1 permissive change avoided restarting FCC certification, and missing that window meant missing the retail ship date that followed a January trade show, so the fix was wired together from whatever logic parts remained on the board.[222]

## Applications

### Displays and LED arrays

Commodity RGB LED panels present a shift-register interface, so a small CPLD placed between the microcontroller and the panel can translate a SPI packet into the parallel shift-register signalling the panel expects; once the interface is reduced to a SPI stream, the frame can be pushed out by a DMA transfer, leaving nearly all CPU time free for the application instead of bit-banging pixel data. Jason Cerundolo used this CPLD-plus-DMA arrangement in his own panel-driving project.[340] In a DMA-driven display pipeline the CPU only has to produce the frame buffer: in one animated pattern demonstrated by Piotr Esden-Tempski, rendering consumed about a third of the frame time and the processor was free for the remaining two thirds while the transfer ran.[356]

Driving commodity 32-by-32 RGB LED matrix panels from a microcontroller became practical when the Teensy 3.2 shipped with mature DMA-based driver code for those panels, handling refresh timing that would otherwise dominate the firmware.[403] The resolution of such a panel is sufficient to hold an entire classic coin-op arcade playfield—roughly 30 by 26 tiles—provided sprite detail is dropped and each element is reduced to a single coloured dot, an approach Mike Szczys used to run arcade games on a single panel.[403] DMA-based libraries similarly remove the timing and throughput problem of driving addressable WS2812 LEDs, because the transfer engine generates the pulse-width-encoded bitstream without the CPU meeting each bit deadline; the OctoWS2811 library applies this to push a frame buffer out to the LEDs.[403] Large arrays of such devices carry a separate quiescent-current penalty: about a thousand WS2812 devices drew roughly 900 milliamps with every LED commanded off, because each device's controller draws current regardless of the displayed colour.[403]

Smooth multiplexed LED fading can require several rounds of iteration; on one of Kerry Scharfglass's badge projects, moving the bus traffic onto DMA was what finally made the refresh fast enough that the multiplexing became invisible to the eye, with an I2C-driven LED controller at 400 kHz proving adequate for visually smooth fades once the update path was optimised.[487]

### Audio

Real-time audio processing on a microcontroller became feasible only once parts combined a DMA-fed I2S interface with a hardware floating-point unit, as on the Cortex-M4; earlier microcontrollers could not sustain the sample stream and the arithmetic together.[513] A real-time audio product built on a Cortex-M4 can therefore be written without a real-time operating system, using interrupts alone, with the I2S path to the ADC and DAC handled entirely by DMA so that sample-rate deadlines are met by hardware rather than by scheduling.[513]

A microcontroller audio chain is structured as a set of buffers rather than a stream of samples: DMA fills a buffer from the ADC, the contents are moved into a ring buffer, the filter reads one ring buffer and writes another, and the output side returns the processed data to the DAC.[560] In such a real-time filter chain roughly 90 percent of execution time is spent inside the biquad section, so the hand-optimised biquad is the first thing to port to a new platform and everything around it is comparatively cheap housekeeping.[560] A biquad is a universal filtering block with programmable coefficients, so a single optimised implementation plus a set of coefficients covers most of the filtering a platform needs; building on ARM's CMSIS DSP library supplies an already-optimised biquad and helper routines that can be linked pre-compiled or taken as source and tuned further.[560]

Multi-channel audio hardware is easier to use than a generic parallel capture port because the peripheral itself recognises the frame marker identifying the first word of the stream, and can then DMA each channel straight into its own buffer in internal memory instead of the CPU continuously commanding transfers.[640]

### Radio and wireless

A low-cost software-defined transmitter dongle stores no samples of its own: the host holds the waveform in RAM and the device acts only as a conduit, with a DMA path carrying data from host memory through the DAC and out to the antenna.[391] A dongle built around a VGA display driver chip contains only a DAC, so it can transmit but has no analog-to-digital path and cannot capture a received signal.[391]

On the ESP8266, driving the I2S engine by DMA can send and receive bit streams at around 80 MHz using roughly a kilobyte of code, once the vendor operating system layer is removed and the hardware is no longer restricted to the uses the SDK assumes; CNLohr demonstrated this by stripping the vendor stack from the part.[637] Removing that SDK frees enough flash and RAM for the whole program to execute from RAM, dropping the flash-and-boot cycle to about half a second and making the compile-test loop effectively instant, and outside the vendor stack's constraints the part runs reliably at about 380 MHz rather than its nominal 80 or 160 MHz.[637] Espressif's original non-OS SDK for the ESP8266 provided only timers and malloc, with the Wi-Fi and LWIP stacks layered on top, and it booted faster and was leaner than the later FreeRTOS-based SDK.[637]

On the ESP32, the Wi-Fi radio is reached as a memory-mapped peripheral: the driver writes each Wi-Fi frame into a linked list of DMA buffers and then signals the peripheral to transmit, so an emulator such as Wokwi must model the buffer descriptor chain rather than any Wi-Fi instruction.[599] Reverse engineering the closed Wi-Fi driver blob for that emulation took Uri Shaked about a month, with the hardest part being the undocumented magic constants that convert a Wi-Fi channel number into the radio's internal frequency setting rather than the DMA data path itself.[599] Software radio protocol libraries that bit-bang a link keep the CPU polling; the same protocol can be offloaded to a Nordic part's DMA hardware, and a commercial fork of one such library did exactly that, but no open-source stack takes advantage of the host hardware in that way.[667]

### Sensor acquisition

Peripheral-driven DMA lets a microcontroller run autonomous hardware agents that poll a serial sensor such as a GPS receiver and deposit the returned bytes directly into system memory or a register, so a system with many sensors collects data without the CPU servicing each transfer.[395] A peripheral-triggered DMA channel that carries analog-to-digital converter results straight into RAM likewise turns a microcontroller into a data logger that runs with the CPU core powered down entirely, waking the processor only when the buffer needs handling.[95]

## Low-power design

On Energy Micro's low-power microcontrollers, a low-baud-rate serial port can stay active while the part draws roughly one microamp, with received bytes moved into memory by DMA rather than by the core, so a slow link can be serviced continuously without leaving deep sleep.[95] Whether such DMA-driven autonomous peripheral operation saves power depends entirely on the duty cycle of the application: where a sensor is sampled continuously while the core would otherwise be idle, the saving can be orders of magnitude, and where the core has to run anyway it saves nothing.[95]

DMA is not inherently low power: on an ordinary part the bus and peripheral clocks still have to run for a transfer to proceed, so replacing a CPU loop with DMA saves energy only if the clocks the transfer needs are cheaper than the ones the core would need.[614] Some newer parts address this directly; the STM32U5 provides a low-power DMA controller that continues transfers while the processor is in stop mode, allowing most of the clock tree to stay powered down while a peripheral keeps filling a buffer.[614] Such unusual low-power DMA features are generally absent from vendor configuration tooling and hardware abstraction layers, so using them means writing custom register-level code and giving up the portability that made the abstraction layer worth using.[614]

The trade-off extends to whole-system architecture: keyword spotting on a bare-metal Cortex-M7 requires threshold-based wake from the ADC, a DMA channel filling a memory buffer, and the neural network ported down to bare-metal C—plumbing far more laborious than running the equivalent as a Python script in user space on embedded Linux, with the justification being sleep current in the microamps.[515]

## Security implications

Unrestricted DMA from an expansion slot defeats software security, because being able to read and write live system memory allows a lock screen to be bypassed and a running kernel to be modified in place unless the platform has separate protections against it. An off-the-shelf PCI Express controller can be programmed to issue arbitrary DMA accesses, so a card built around one becomes a general-purpose reader and writer of a host machine's memory once plugged into a slot; Joe FitzPatrick built security research hardware on exactly this principle.[346] The same exposure exists inside integrated devices: a modern phone contains several processors beyond the application core that run firmware nobody outside the vendor can inspect while holding DMA access to the rest of the system, so trusting that the sensors behave as documented is an assumption rather than something the owner can verify.[487]

DMA is the hardest peripheral to secure under a TrustZone-style split, because it performs memory accesses on another master's behalf and therefore has to carry that master's security state rather than its own.[687] Privilege in a bus fabric must be monotonic: a transfer programmed by a processor can be less privileged than that processor but must never be more privileged, and a DMA channel programmed from non-secure code is the classic place where that rule gets broken by accident.[687] The RP2350 addresses this by tagging every bus access with the originating security state and filtering it per peripheral, so each UART or I2C can be declared secure or non-secure and the processor's claimed state is checked against that list at every access.[687]

## DMA and soft peripherals

Some microcontrollers pair DMA with programmable I/O logic that behaves like a hardware peripheral. The PIO block in the RP2040 and RP2350 is a set of stripped-down processors good only at deterministic high-speed bit banging; the timing-critical part of a software peripheral is offloaded onto a PIO core and the main processors then talk to it through FIFOs and DMA exactly as if it were a hardware peripheral.[687] Because a PIO state machine can be fed by DMA, protocols such as the pulse-width-encoded WS2812 LED serial format run with zero processor overhead, and the same soft resource can instead be committed to extra UARTs or I2C ports that the silicon does not provide in hardware.[687]

## Development practice

When a bare-metal project needs output waveforms faster than the instruction loop can toggle them, the first thing to check in a part's architecture is whether it has a DMA path feeding data from memory straight to the I/O peripheral.[278] The STM8 Discovery board ships a waveform-generator demo that drives the output DAC through DMA, making it a working reference for how a bare-metal DMA-to-DAC path is set up rather than only a description of one; a usable function generator is not purely digital even when the waveform is produced by direct digital synthesis, since the output stage still needs DC offset injection, attenuators, amplifiers and reconstruction filters on the analog side.[278]

Vendor configuration tools that expose every peripheral register as a dropdown do not help with a task such as setting up DMA to a QSPI flash interface, because the difficulty is the ordering and combination of registers rather than the meaning of any one of them; worked examples plus documentation are what make the peripheral usable.[383] A practical way to catch a DMA transfer that never completes is to spin in a loop reading the completion or interrupt status register and then halt the target from the debugger with a keyboard interrupt, which locates the hang without setting a breakpoint at all.[383]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 95 | An Interview with Øyvind Janbu - Feracious Fabless Facilitator | https://theamphour.com/the-amp-hour-95-feracious-fabless-facilitator/ | |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 278 | Our Second Callin Show(ish) | https://theamphour.com/278-our-second-callin-showish/ | December 16, 2015 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 513 | Audio DSP with Shannon Parks | https://theamphour.com/513-audio-dsp-with-shannon-parks/ | October 18, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 560 | High End Audio with Remco Stoutjesdijk | https://theamphour.com/the-amp-hour-560-high-end-audio-with-remco-stoutjesdijk/ | October 3, 2021 |
| 581 | Real Time Operating Systems with Brian Amos | https://theamphour.com/581-real-time-operating-systems-with-brian-amos/ | March 13, 2022 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
