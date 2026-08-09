---
title: Virtual Machine
concept: virtual-machine
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A **virtual machine** (VM) is a software-defined computing environment that runs inside a host system, ranging from a complete guest operating system image to a bytecode interpreter executing inside firmware.[144][383] In engineering practice, virtual machines serve two broad purposes: preserving and reproducing complete tool environments so that long-lived projects can be resumed or transferred intact, and providing a portable execution layer so that code behaves identically across different hardware.[512][383] The same isolation that makes images useful for preservation also makes them useful for containment of untrusted or autonomous software.[720]

## Development environment preservation

A development environment is destroyed by ordinary events — a machine reinstall between one phase of a project and the next — and the loss often only becomes visible when a client returns months later expecting work to resume immediately.[512] Assigning every client project its own virtual machine addresses this: the cost is disk space, which is effectively free, and a project paused for months can be resumed by starting an image rather than rebuilding a development environment from memory.[512]

An image captures the whole ecosystem — compiler, drivers and configuration — so that booting it returns the identical system rather than an approximation of it; the costs are that anything emulated inside runs slower and that debug hardware must be passed through to the guest.[144] Version drift in teaching and long-lived projects is precisely what images and containers address, since booting into a controlled environment removes the problem of every participant having a slightly different install.[497]

### Toolchain freezing

Keeping an image loaded with an old toolchain ready to start at any moment is a deliberate strategy, because updated compilers and place-and-route tools do not necessarily handle older designs as well as the versions those designs were built with.[181] Declining to upgrade a working toolchain is defensible when the old version is sealed in an image that never has to change; the counter-argument — that the newest version supports the newest operating system — only matters if the environment is expected to move, and an image is exactly the way to stop it moving.[546]

When a vendor introduces a major version migration in its firmware tooling, installing the relied-upon version into an image locks it down before the upgrade path becomes mandatory, a defensive move that matters especially on client work, where the timing of the next build cannot be controlled.[524] Travis Goodspeed has argued that the durable case for open tools is access rather than ideology: an old image running an old version of a design tool such as KiCad 5 can still be started thirty years later, with no licence server to contact and no licence left to expire.[442]

### Conflicting and obsolete requirements

Vendor software that demands an obsolete operating system can be given its own image, which solves two problems at once: the obsolete requirement is satisfied, and the installation cannot collide with another copy of the same package already on the machine.[144] Some vendor toolchains cannot run natively on a Mac at all, making an image hosting Windows or Linux the only path rather than a preference — a practical constraint when planning a workshop where participants bring their own laptops.[423]

Stacking a Windows program under a compatibility layer, inside a Linux guest, inside an image on a Mac is defensible on one ground: the result is identical to the machine at home, and consistency across machines is worth more than any single layer costs.[234]

## Hardware passthrough

Hardware passthrough is the part of desktop virtualisation that practitioners expect to fail and in practice is solid: a USB debug adapter or serial converter handed to the guest works well enough to develop against real boards from inside an image.[512] Virtualisation products differ specifically in how well they handle low-level device passthrough, which is the criterion that matters for embedded work — enough to justify paying for one product over a free alternative that handles it less reliably.[534]

A practical recovery from an unusable native Linux install is to host the distribution in an image on a working machine and pass the debug cable through to it; the toolchain then talks to the board with no change to how the work is done.[510] Compatibility layers that run a Linux userland on a Windows host handle terminals and files easily but have historically failed exactly at the hardware boundary — the path from software all the way down to the USB port.[576]

## Distribution and transfer

A per-client image is transferable: handing over the file gives the client the entire working environment, functionally equivalent to shipping a configured laptop, and removes any argument about what was installed.[520] Vendors have distributed complete images with the compiler and SDK preinstalled, which solves the setup problem entirely while leaving the recipient with whatever licensing terms attach to the contents.[359]

### Teaching environments

Distributing a prepared image on USB sticks for a workshop has broken on machines with newer Apple processors, and the per-participant remediation required made the experience worse than having everyone install locally; the approach fails precisely where the audience's hardware is least uniform.[675] The ideal teaching distribution is a single image everyone can run, but it fails on licensing economics rather than technology — redistributing commercial virtualisation to students is not realistic — which pushes courses toward browser-hosted environments instead.[675]

Browser-hosted environments suit toolchains that are mostly compilation and poorly suit graphics-heavy work such as CAD, which needs GPU support to be usable at all, so the appropriate hosting model follows from what the tool actually does.[675] Running a full toolchain inside a processor simulator in the browser works but is unusable in practice: compiling a trivial Arduino sketch takes around two minutes, and the environment itself is tens of megabytes to download before compilation begins.[599] The workable split, as implemented in Uri Shaked's Wokwi simulator, is to compile in a remote container and execute the result locally in the browser, putting the resource-hungry step on a machine that can do it and leaving the interactive part where the user is.[599]

## Lightweight alternatives

Storing the toolchain with the source solves the same problem an image does at far lower cost: an image drags an entire operating system and its interface along with the compiler, whereas a build definition carries only what is needed to reconstruct the environment.[612] Committing the toolchain definition as another file in the repository means nothing is installed on the developer's machine — the hosted environment reads the file, builds the environment and runs the work, so a new contributor is one clone away from a working setup.[627]

Continuous integration applies the same mechanism on a schedule: spin up a clean environment, install the dependencies, pull the code, run the tests and report the result, with the value coming from the environment being clean every time rather than from the automation itself.[627]

## Process virtual machines on microcontrollers

An on-device Python implementation ships the tools rather than the output: the firmware finds the source file, converts it to bytecode held in memory, and a virtual machine written in C interprets that bytecode; saving the file again stops the machine and repeats the cycle, which is why there is no compile-and-flash step.[383] The point of the bytecode layer is that nobody porting to a new microcontroller has to understand it — the machine behaves identically everywhere, so the work of supporting a new part is confined to the hardware layer beneath it.[383]

Writing a device library in an interpreted on-device language works when code runs against the firmware's own I2C, SPI and digital interfaces, and stops working where timing is tight: reading a converter's register occasionally is fine, but sustaining a fast continuous transfer is not.[323] Anything running in a virtual machine — any dynamic language — is harder to prove correct and harder to test than compiled code, which is a real objection to shipping that stack in a commercial embedded product however good the surrounding testing frameworks become.[295]

Waking a device, bringing up an operating system, starting a virtual machine and executing interpreted code takes around 50 milliseconds — far longer than bare hardware needs, though irrelevant in a design where the device wakes, captures an event and then waits on a network connection anyway.[202] Bytecode on a microcontroller repeats what portable bytecode did for the browser and inherits the same objection in a new form: the abstraction costs cycles, and on a battery-powered device cycles are energy.[723]

Console backward compatibility across an architecture change has been achieved by translating code as it executes rather than by emulating the old machine, which allows software built for one instruction set to run at usable speed on a completely different one.[490]

## Server and infrastructure virtualisation

In a server, the host processor runs a hypervisor whose only job is to host customer machines, so the workloads a customer cares about never touch the hardware directly and the platform beneath them can be maintained independently.[590] A virtualisation layer installed just above the firmware lets one physical machine carry several independent systems, which is how two instances of the same appliance software can run side by side on hardware that would otherwise host one.[685]

Running an autonomous agent inside an image with its own account is a containment measure rather than a compatibility one: the isolation is what stops software acting on its own initiative from reaching the rest of the machine.[720]

## Machine control

In machine control, the term refers to something else entirely: every axis, heater and sensor is a node on a machine network with a corresponding object in software, and motion happens by calling functions on those nodes directly instead of streaming a command language to a controller that interprets it.[208] Nadya Peek's work on modular machine control showed that this representation makes machine topology cheap to change — extending a machine from three axes to four required connecting one more node and composing two compound nodes in software, where a command-language toolchain would have needed the whole interpretation layer reworked.[208]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 144 | An Interview with Bob Davidson - Hoodied HP Hijinks | https://theamphour.com/the-amp-hour-144-hoodied-hp-hijinks/ | May 7, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ | |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 208 | An Interview With Nadya Peek - Gallant Gcode Gerontology | https://theamphour.com/208-an-interview-with-nadya-peek-gallant-gcode-gerontology/ | July 21, 2014 |
| 234 | We'll Believe It When We See It - Hiring Hypercatalectic Helpelp | https://theamphour.com/234-well-believe-it-when-we-see-it-hiring-hypercatalectic-helpelp/ | January 27, 2015 |
| 295 | An Interview with Omer Kilic | https://theamphour.com/295-an-interview-with-omer-kilic/ | April 20, 2016 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 423 | Open FPGA Toolchains at 35c3 | https://theamphour.com/423-open-fpga-toolchains-at-35c3/ | January 1, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 497 | An Interview with Brock LaMeres | https://theamphour.com/497-an-interview-with-brock-lameres/ | June 21, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 576 | A literal trainwreck | https://theamphour.com/576-a-literal-trainwreck/ | February 6, 2022 |
| 590 | Finding Hardware Flaws with Laura Abbott | https://theamphour.com/590-finding-hardware-flaws-with-laura-abbott/ | May 22, 2022 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 627 | Works on my machine | https://theamphour.com/627-works-on-my-machine/ | April 9, 2023 |
| 675 | Changing Course with Shawn Hymel | https://theamphour.com/675-changing-course-with-shawn-hymel/ | August 8, 2024 |
| 685 | Data Provenance in the Home, Server, and Fab | https://theamphour.com/685-data-provenance-in-the-home-server-and-fab/ | December 23, 2024 |
| 720 | Hyper Growth and OpenClaw Interns | https://theamphour.com/720-hyper-growth-and-openclaw-interns/ | March 31, 2026 |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ | May 7, 2026 |
