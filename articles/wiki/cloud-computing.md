---
title: Cloud Computing
concept: cloud-computing
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**Cloud computing** is the delivery of computing services — processing, storage, and software — over the internet from infrastructure operated by a provider, typically on an elastic, pay-per-consumption basis. The defining economic property is the ability to spin up a virtual server on demand, scale it down again, and pay only for what is used, which allowed small companies to do work that previously required buying a server and renting co-location space.[271] The model creates a structural trade: hosted services offer scale, collaboration, and operational visibility, but any product or tool whose function depends on a vendor-operated service inherits that vendor's lifespan, and such a service is unlikely to survive ten years and will almost certainly not survive twenty, at which point dependent hardware simply stops working.[296]

## The elastic infrastructure model

The core of cloud infrastructure is elasticity: virtual servers can be provisioned on demand, scaled up or down, and billed by consumption rather than owned outright.[271] For small services, rented virtual server space is cheap enough that owning hardware is not a consideration.[272] Renting many machines for a few minutes each at well under a dollar apiece converts slow batch tools into interactive ones: a five-hour autorouting run competes with doing layout by hand, while a one-minute run supports tweak-and-rerun iteration, so the change in wall-clock time changes the workflow itself.[469]

Elastic hosting has historically been the answer to scale ceilings on cheaper options. Shared hosting stops coping somewhere around a terabyte of monthly transfer, where the symptom is intermittent dropouts rather than outright failure, and that threshold has historically forced a move to elastic hosting.[2] The economics reverse with scale, however: renting makes sense early and makes progressively less sense as the workload grows, and on-premises infrastructure persists for concrete reasons — data integrity, data privacy law, and raw latency — rather than as conservatism.[590]

The major infrastructure services are built for power users rather than beginners; the barrier to using them is learning them, not obtaining them, and the dozens of separate offerings are themselves part of the difficulty.[271]

## Service dependence and longevity

A product whose function depends on a vendor-operated service inherits that vendor's lifespan: the service is unlikely to survive ten years and will almost certainly not survive twenty, at which point the hardware stops working.[296] The standard defence against tool obsolescence — keeping an old CAD package or compiler alive on a preserved machine — has no equivalent when the processing happens on the vendor's servers, so a hosted tool cannot be archived alongside the design it produced.[139]

Running a design tool online creates two dependencies at once: the user's internet connection and the provider's infrastructure. The model works at the scale of a major mail provider, while smaller companies lack the resources to make it equally robust.[317] Hosted design tools have produced multi-week lockouts in practice — one user reported being unable to export schematics for over eighteen days with no support response — and during such an outage the work is neither editable nor retrievable.[317]

The same exposure applies to material rather than tools: anything hosted, including one's own site and documentation, can disappear, so material worth keeping needs to be both archived and spread across enough independent copies that no single service's failure removes it.[609]

## Hosted design and engineering tools

The test for whether a browser-based tool is genuinely a hosted service is whether it needs live internet access while the work is in progress: if the application and the file can be kept locally and run offline, it is a desktop application that happens to render in a browser and carries none of the dependency risk.[145]

Policy excludes hosted tooling in much of the engineering world regardless of technical merit: a substantial number of engineering companies still do not permit internet access on design workstations at all.[163] The vendor counter-argument is that a hosted provider fields a team working full time on protecting stored files, while almost nobody does the equivalent for an individual workstation, and that a breach is existential for the vendor in a way it is not for the customer.[163]

In manufacturing software, an outage is a payroll problem rather than an inconvenience once a shop's machines depend on the tool. John Saunders, whose shop used hosted CAM tooling, valued the collaboration features — shared tool libraries across every machine in the shop — but maintained that an operator would still take the local option if given the choice, because a business with payroll and machines to run cannot tolerate the service going down.[379]

### Semiconductor and FPGA workflows

Long FPGA and ASIC builds can be partitioned into chunks and run in parallel on disposable compute, which breaks the assumption that the only way to speed up hardware development is to buy a bigger workstation.[547] Continuous integration platforms are dimensioned for software build times and software memory footprints; hardware tools with very large RAM requirements need custom runners on the user's own or rented machines, with the platform reduced to orchestration.[547]

A browser front end to a remote tool is a remote display and nothing more, so the engineering problem is network latency to the data centre; where that latency is high, design size has to be capped because the view refreshes too slowly to work with. Mohamed Kassem characterised the browser in such systems as "a delivery window" — a remote display — in the context of cloud-hosted chip design.[503] Putting design software, IP, and foundry access behind one portal is straightforward to state and close to impossible inside the traditional licensed ecosystem, because each of the three is separately gated, which is why the open flow had to be assembled rather than bought.[503]

Hosted access also changes how chips are evaluated before purchase. Buying a conventional chip means buying a datasheet with no way to verify its claims until parts are on a board; hosted access to the register-transfer source lets a customer run their own code against the actual design before silicon exists.[650] Andreas Olofsson's ASIC operation used machines costing roughly one to ten dollars an hour for this kind of interactive evaluation, making hands-on access for prospective customers a bounded cost-of-sales line rather than an open-ended commitment.[650] Hosted evaluation functions as a distribution strategy as much as a technical one: reaching ten thousand prospects is impossible through a sales force unless each deal is worth a million dollars, and self-serve access is what makes the smaller deal viable.[650]

### Reproducible development environments

Storing the environment definition alongside the source — the prerequisites and toolchain install steps as a script in the repository — lets a hosted development environment reproduce the build machine on demand, up to throwing thirty-two cores at a compile.[612]

## Edge versus remote processing

A decision that concerns only local state should be made locally; sending the data out, processing it remotely, and sending the result back adds layers without adding capability. Remote monitoring of that same system is a separate and legitimate feature.[272]

Both poles are defensible depending on the workload, and the split follows the algorithm rather than a principle.[371]

- **Edge processing.** The device does the interpretation and sends events rather than raw data upward, leaving aggregation as the remote system's job, which collapses both bandwidth and storage cost against streaming everything. Joe Bamberg's monitoring systems work this way, with most processing in the box and events sent to the cloud.[371]
- **Remote processing.** When the algorithm is complex and changes often, the sensor data can be reduced just enough on device while the real algorithm runs remotely; firmware becomes dramatically simpler, and the analysis can be re-run over the same recorded dataset as many times as needed instead of going through a download-test-wait cycle. Eli Hughes used this split for fermentation monitoring, on the basis that hosted computing is nearly free and that users do not want sensor readings — they want the conclusion drawn from them, which is what determines where the interpretation layer has to live rather than any principle about edges and centres.[511]

The durable division of labour for machine learning on small devices is to train remotely and infer locally: hosted tooling consumes labelled sensor data and emits inference models sized to run on a resource-constrained microcontroller, so the developer never has to be a data scientist. Brian Faith's QuickLogic used this pattern for its sensor-processing toolchain.[525]

### Voice interfaces

A voice-controlled device runs a wake-word detector locally, then sends the request to a remote service which in turn commands the target device, so a single spoken command traverses the internet twice before a light changes state.[351] Keeping voice processing on a local network buys response time and removes the internet dependency, but a model that fits on the device will not match one trained against a far larger corpus — the trade is accuracy against latency and autonomy, not a free win.[351]

Local voice processing is viable but hardware-bound. Keith Burzinski's home automation work found that on an older single-board computer a response can take around ten seconds, while routing the same request to a hosted service returns essentially instantly — the practical reason people give up local processing.[657] Historically, offloading the heavy processing also kept the on-device application small, which is why speech recognition shipped an audio file to a server rather than carrying the model.[225]

## Connected devices and fleet operations

Cheap compute and ubiquitous connectivity make it possible to put a radio on anything, and the characteristic failure is starting from that possibility rather than from the value the connection is supposed to deliver.[327]

Many companies commissioning connected products treat the hardware as a necessary evil and want only the resulting data, but somebody still has to own the firmware, the electrical and mechanical design, the radios, and the security before any of that data reaches anywhere useful — the gap Scott Miller's product-development practice was built to fill.[451]

The operational value of a hosted component for deployed hardware is fleet visibility and controlled rollout: how many units exist, how many are active, which firmware revision each is running, and the ability to stage a migration rather than push to everything at once.[310] Over-the-air update is two problems, not one: the firmware needs hooks capable of rewriting itself, and a server component has to exist to drive it — and the second half is frequently outside the skill set of the person who built the device.[422]

Some components that look local are inherently central. Running a network server on a gateway is fine for bench testing but wrong for deployment, because multiple gateways all have to reach the same server. Richard Ginus applied this rule in deploying LoRa networks, where the gateway-resident server was a testing convenience only.[376]

Software running on rented infrastructure has known, measurable network characteristics; the same software deployed across customer premises does not, and that unpredictability is a different engineering problem rather than the same one at a smaller scale.[526] Access control built on hosted integrations has two independent failure paths: the building's connection dropping, and a vendor pushing an update that silently breaks an existing integration. Jonathan Beri's building-access systems answered both by adding edge computing to keep state synchronised locally.[526]

## Local-first design and privacy

A defensible rule for home automation is that the installation must never depend on an external service: if everything cannot be controlled locally while the house is offline, the design is wrong. Jon Oxer applied this rule to his own extensively automated house.[349] Telemetry leaving a home leaks occupancy whether or not that was the intent, so the security question is not only whether the data is protected in transit but what the pattern of the data reveals about the people generating it.[349]

## Manufacturing integration

Standardising the factory programming and test station as a Linux computer — carrying a programmable supply, a programmer, a meter, and network access in one box — is what lets test reports leave the line automatically rather than surviving as files on a factory PC. Pete Staples's manufacturing-standardisation work used this architecture to push test reports securely to hosted storage directly from the line.[544]

## Market structure

The large infrastructure providers are pushing their reach all the way down to the sensor, because owning the last link is what lets the connection be billed by the byte.[489] In semiconductors, self-serve hosted evaluation extends the market downward: deals too small to justify a sales force become viable when customers can evaluate the product themselves against the actual design.[650]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 2 | Critical Mass | https://theamphour.com/show-2-critical-mass/ |  |
| 139 | Google Glass & Adafruit - Obtaining Ostentatious Oculiforms | https://theamphour.com/the-amp-hour-139-obtaining-ostentatious-oculiforms/ | April 2, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 225 | Worktrips and Workspaces - Junket Jactation Jiltedness | https://theamphour.com/225-worktrips-and-workspaces-junket-jactation-jiltedness/ | November 25, 2014 |
| 271 | Amazon Moves In, Dave Says Run | https://theamphour.com/271-amazon-moves-in-dave-says-run/ | October 14, 2015 |
| 272 | An Interview With Luke Beno of Analog.io | https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/ | October 21, 2015 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 310 | Mergers and Acquiescence | https://theamphour.com/310-mergers-and-acquiescence/ | August 3, 2016 |
| 317 | A Decoupled Episode | https://theamphour.com/317-a-decoupled-episode/ | September 28, 2016 |
| 327 | An Interview with Avidan Ross | https://theamphour.com/327-an-interview-with-avidan-ross/ | December 14, 2016 |
| 349 | An(other) Interview with Jon Oxer | https://theamphour.com/349-another-interview-with-jon-oxer/ | June 25, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 371 | An Interview With Joe Bamberg | https://theamphour.com/371-an-interview-with-joe-bamberg/ | December 10, 2017 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 379 | An Interview with John Saunders | https://theamphour.com/379-an-interview-with-john-saunders/ | February 11, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 451 | An Interview with Scott Miller (2nd) | https://theamphour.com/451-an-interview-with-scott-miller-2nd/ | July 21, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 489 | An Interview with Jack Ganssle (2nd) | https://theamphour.com/489-an-interview-with-jack-ganssle-2nd/ | April 19, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 511 | Brewing Electronics with Eli Hughes | https://theamphour.com/511-brewing-electronics-with-eli-hughes/ | October 4, 2020 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 526 | Why IoT Is Difficult with Jonathan Beri | https://theamphour.com/526-why-iot-is-difficult-with-jonathan-beri/ | January 18, 2021 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 547 | Open Source Mindset with Michael Gielda | https://theamphour.com/547-open-source-mindset-with-michael-gielda/ | June 28, 2021 |
| 590 | Finding Hardware Flaws with Laura Abbott | https://theamphour.com/590-finding-hardware-flaws-with-laura-abbott/ | May 22, 2022 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 650 | Accessible ASICs with Andreas Olofsson | https://theamphour.com/650-accessible-asics-with-andreas-olofsson/ | November 12, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
