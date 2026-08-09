---
title: State Machine
concept: state-machine
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A state machine is a control structure in which a system is defined at any instant by a single named state, with transitions between states triggered by events or conditions. It appears in embedded engineering both as a way of organising firmware and as a hardware construct implemented directly in logic.[711] Its principal virtue in software is that it makes a system's condition finite and nameable, so that a given state can be reproduced exactly for testing, which is what makes state-by-state quality assurance possible at all.[711] In hardware, the same structure is what sequences devices that execute no instructions at all, from early display drivers to the control logic inside modern switching regulators.[180][196]

## As a firmware structure

Event-driven logic written as nested conditionals degenerates quickly: the if-else testing needed to work out what a button-triggered device is currently doing becomes unreadable even for simple behaviour, which is the concrete argument for imposing a state machine from the outset.[711] The same reasoning applies at industrial scale, where sequencing logic of the kind that runs conveyors and assembly lines is a large state machine at heart; writing the equivalent behaviour as a pile of if-statements is possible but becomes too much to maintain.[385] In that domain, software design patterns can in principle be applied to ladder logic, but the deployed reality on factory floors is a large quantity of poor code, and the very simplicity of the ladder representation acts as a defence by limiting how badly a corner case can be buried.[385]

A state machine can legitimately constitute the bulk of a firmware code base. One production battery and power-negotiation firmware was structured around a single machine with roughly twenty-nine states, and that machine alone accounted for some 1,500 to 2,000 lines, the majority of the code.[340]

### Handling cross-cutting conditions

Conditions that do not belong to any single state are best fed into the machine rather than scattered through the code. In vehicle drivetrain control, cross-cutting conditions are handled as inhibit events: a lean-angle limit raises an inhibit that changes the sequence or blocks a shift, and a flag must be clear before the machine will enter the engagement state.[426]

An alternative is to express the machine in a language of its own. The Paparazzi autopilot describes flight behaviour as blocks, sequences of instructions in a domain-specific language in which sensor readings crossing a threshold cause a jump to another block; this is a state machine expressed as a small concurrent language rather than as hand-written control flow, and it lets the airframe reason about what it is doing rather than merely follow waypoints.[356]

Interactive engineering applications share a common architecture built around the same idea: a command queue that receives commands raised by user-interface events, a UI toolkit that renders the front end, an underlying state machine that processes the queued commands, and a data model that holds the design in memory and on disk.[471]

## Relationship to real-time operating systems

The first question to ask before reaching for a real-time operating system is whether a plain state machine would meet the requirement; for a small and well-bounded application it is the better option, and the decision is easier to make when the minimum requirements are known before the code base exists rather than being retrofitted to inherited firmware.[581] The choice is not binary, since a range of scheduling structures exists between a bare state machine and a full real-time operating system, and picking a point on that range keeps the system's behaviour knowable.[584]

Threads are the right tool for behaviour that does not belong to any one state: a heartbeat LED that must keep blinking regardless of what the device is doing is awkward to express inside a pure state machine and natural as a separate thread under a scheduler, which is the boundary at which an operating system starts to earn its place.[711]

### State machine frameworks

Some real-time operating systems ship a state machine framework alongside the scheduler, which is redundant in the sense that a machine can always be hand-written in a super loop; the framework earns its cost only where the structure it imposes is worth the memory it consumes, on the order of a hundred bytes.[653] The point at which a framework beats a hand-written switch-case is where behaviour grows beyond simple parsing: once conditions such as geofence entry and exit, a graphical interface and business rules all hang off the same machine, describing it explicitly in the framework is easier to follow than raw switch-case code.[653]

Such frameworks can be moving targets. The input syntax of one changed within a release series, which is the practical reason to pin builds to specific SDK and toolkit versions in continuous integration, since a nominally minor version bump can carry a major update to a package underneath.[711]

Machines that already exist elsewhere are not worth rewriting. Protocol parsing already written and maintained in an operating system subsystem, such as a generic NMEA driver under a GNSS subsystem, adds no value when hand-rolled in application code and adds a state machine that must then be maintained locally.[653]

## Testing and verification

Firmware becomes testable off-target when hardware-dependent calls are confined to a driver layer instead of being scattered through the code; a decoding pipeline and the state machine that handles decoded messages can then be exercised on a host with an input data array, with no radio or target board present.[556] A practical way to build such a fixture is to capture real traffic once off the hardware, store it as a C array in the test build, and replay it through the layers above the driver, which turns an intermittent over-the-air test into a repeatable one.[556]

### Formal verification in silicon

A state machine that can reach a stalled or blocked state with no path out is a catastrophic defect in an ASIC, because there is no field fix: recovering means a new mask and a new spin at a cost in the region of ten million dollars, which is why formal verification is concentrated in designs where failure cannot be tolerated or cannot be corrected afterwards.[467]

Formal verification is an exercise in choosing the right property rather than in exhaustively describing the design. A whole command-dispatch pipeline may need only the single assertion that the read and write lines are never asserted at the same time, and a violation of that one property leads back to the bug in the dispatcher.[467] Verifying a non-trivial block often requires building a second state machine whose job is to drive the formal testing of the first, so that different assumptions and assertions apply depending on the operating state the design under test is currently in.[467]

## Implementation in logic

An FPGA is a natural home for state machines, since the fabric implements transition logic directly in parallel hardware; conversely an FPGA carrying nothing but a soft processor core spends die area, package, cost and power to do what a microcontroller would have done, so the fabric should be earning its keep with logic such as state machines written in VHDL or Verilog.[141]

A simple CPU is not much more than a datapath plus sequencing control, so an engineer who has built a full adder and a state machine in a hardware description language already has the two ingredients and is roughly halfway to a working processor.[672] The proportions bear this out: in one minimal RISC-V implementation the load-store logic is about twelve lines and the state machine that drives it about twenty, alongside the ALU and the address generation.[644]

Before committing a maths-heavy algorithm to silicon it is worth prototyping it in fixed point to establish what precision and how many operations are actually required, since the result can be modest enough that an eight-bit CPU sequenced by a small state machine can grind through the arithmetic.[173]

## Fixed-function state machines in devices

Some early LCD driver parts were not processors at all but hardwired state machines: the chip sequenced the display directly without executing instructions, which is why it needed no program memory or instruction set.[180] Early consumer sound-playback chips had almost no logic either, with the triggering behaviour selected by ticking options on a paper form that the vendor turned into mask configuration; the parts that followed were sequencers rather than true microcontrollers, closer to a state machine with fixed options than to a programmable CPU.[424]

The control logic inside a modern switching regulator is likewise built from state machines rather than a processor, and in a four-switch buck-boost part that logic runs to many thousands of gates, every one of which is doing something. The complexity comes from coordinating N-channel FETs whose floating gate drivers need bootstrap voltages above the input or output rail depending on the operating mode.[196] Such a bootstrapped high-side gate driver cannot hold its boost capacitor charged if the converter stays in one steady switching mode, so the control state machine periodically forces a refresh: in one four-switch buck-boost part every tenth cycle commutates all four MOSFETs purely to recharge the boost capacitors.[196]

The fixed nature of these machines constrains how they must be driven. Many bus-attached peripheral devices are not intelligent controllers but fixed state machines behind a set of registers, so they will neither recover from nor report an out-of-sequence access; the master must drive the documented sequence exactly, because there is nothing on the far end capable of interpreting intent.[396]

A state machine can also stand in for computation the processor cannot afford. Speaker-independent voice recognition was shipped in 1988 on a 6804 microcontroller with only one to one and a half kilobytes of memory by moving the analysis off the part: the spectral work was done in advance and reduced to tables burned into the device, leaving the runtime code as a state machine that compares incoming data against those tables.[236] A microcontroller with no analogue-to-digital converter could still take in an audio signal, provided the signal was squared up externally into a pulse-width-modulated square wave, so that timing edges rather than sample amplitudes became the input to the recognition machine.[236]

## Configurable state machine peripherals

Some microcontrollers expose configurable state-machine peripherals, such as an SGPIO block or a state configurable timer, which run independently of the CPU and make their own decisions on bit patterns; this effectively allows software-defined peripherals, a small machine inside the larger part, without consuming processor cycles.[265] Programmable I/O blocks of this kind are small state machines rather than ALUs, each with its own architecture and its own assembly language, so using them means writing to a second instruction set alongside the main processor's.[595] The programmable I/O peripheral on the Raspberry Pi microcontrollers is a genuine state machine processor with its own tiny program store, holding on the order of thirty-two bytes of machine code, which is enough to implement a serial protocol listener that runs without the main core.[713]

The same construct has been proposed for memory access. A microcontroller whose boot vector points at address zero should include a hardwired state machine that fetches transparently from an external SPI ROM, so that off-chip program storage looks like on-chip memory to the running code; without it, the external-memory case has to be handled explicitly by the software.[713]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 141 | FPGAs, Robots & Thermocouples - Wampum's Wavering Worth | https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/ | April 15, 2013 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25, 2013 |
| 180 | An Interview with Dave Taylor - Multi-talented Meter Maker | https://theamphour.com/180-an-interview-with-dave-taylor-multi-talented-meter-maker/ | January 13, 2014 |
| 196 | An Interview with Mike Engelhardt (Re-broadcast) | https://theamphour.com/196-an-interview-with-mike-engelhardt-re-broadcast/ | April 28, 2014 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 385 | An Interview with John Davis | https://theamphour.com/385-an-interview-with-john-davis/ | March 25, 2018 |
| 396 | The Synergy Bus | https://theamphour.com/396-the-synergy-bus/ | June 10, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 426 | An Interview with Dean Pick | https://theamphour.com/426-an-interview-with-dean-pick/ | January 20, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 581 | Real Time Operating Systems with Brian Amos | https://theamphour.com/581-real-time-operating-systems-with-brian-amos/ | March 13, 2022 |
| 584 | Software for Rockets with Charles Aylward | https://theamphour.com/584-software-for-rockets-with-charles-aylward/ | April 3, 2022 |
| 595 | Trade Show or Conference? | https://theamphour.com/595-trade-show-or-conference/ | July 10, 2022 |
| 644 | Garbage Ninjas | https://theamphour.com/644-garbage-ninjas/ | August 28, 2023 |
| 653 | Benjamin Cabé Nose Zephyr | https://theamphour.com/653-benjamin-cabe-nose-zephyr/ | December 11, 2023 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 711 | Medical Electronics Education with Mark Palmeri | https://theamphour.com/711-medical-electronics-education-with-mark-palmeri/ | December 21, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
