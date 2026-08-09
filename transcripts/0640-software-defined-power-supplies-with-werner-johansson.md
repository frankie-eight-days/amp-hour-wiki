---
episode: 640
title: Software Defined Power Supplies with Werner Johansson
url: https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/
---

**Werner:** This is The Amp Hour Podcast. Released July 25th, 2023. Episode 640. Software-defined power supplies with Werner Johansson.

**Werner:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Werner Johansson from Koitech. Hey, Werner. How are you? I'm doing well. How are you? I have brought up your talk multiple times. I'll get to the point here in a second. But I brought up your talk multiple times. And I keep thinking every time I bring up something that I remember you talking about, I keep going to the Amp Hour and searching Werner and seeing like, wait, he hasn't been on the show yet. It's actually you had given a talk at hardware developer Didactic Galactic the meetup I used to do in San Francisco. And I bring up that talk multiple times on the show. And I'm really glad you're here now so that I can bring up this show instead of just that talk.

**Bluetooth:** Yeah, it's been a continuing thing of mine that designing power supplies apparently has become something I do a lot. And I like them to be software-defined.

**Werner:** Ah, yes, yes. So that is the talk that you gave at HDDG all those years ago. And I remember it was, I think it was a pretty simple microcontroller you were talking about that was actually doing the power supply control in software.

**Bluetooth:** I've been using the Atmel NowMicroship XMega line for a lot of that. That's what it was. Yeah. Because of its ADC. Because it was in a class of its own, a two mega sample SAR ADC. Oh, wow. Yeah. That's basically an ADC with a micro attach, right? Yeah. So unfortunately, all of those are successive approximation, but that's what you get in that price. But it's a 12-bit really fast ADC for a microcontroller. So you get a fairly short lag between the actual sample, and then you make a regulation decision, and then you have a DAC on the output or PWM.

**Werner:** Yeah.

**Bluetooth:** Nice.

**Werner:** So that's where I started. Got it. Yeah. And so since that time, so that was San Francisco. Since that time, you have started working at Koitek. And what is Koitek?

**Bluetooth:** So Koitek is a spinoff from the old Sony Mobile, the cell phone company that very few people heard of these days. We were internally, because I have an 11-year-old history at Sony Ericsson and then Sony Mobile, both in Sweden and in the US. We were looking into PowerSave and measure the actual power consumption of the cell phones. And there were some tools available, and they were all missing one or two other features that we wanted. I started looking into that because we were using this when I was doing Linux mainlining, trying to do automation. So we really didn't care about the high-accuracy current measurements. We just wanted to see that, okay, does it draw 300 milliamps? Does it draw 20? But we also wanted to have serial port control and some keyboard emulations. We could press certain keys to enter service mode, DFU mode, that kind of things, reflash automatically. So I did that project. And that's the CDB Assist, which is also from this timeframe, right around the talk, which must have been 2016, right? Yeah. It's something like that.

**Werner:** That sounds right, yeah. I can pull that up to double-check, but make sure it's still on the internet, too. That's the other thing, you know? These things disappear sometimes.

**Bluetooth:** So that's an open-source thing that's actually not... Well, it was initially based on Xmega, and then it did a version based on the Cypress, now Infineon, PSoC 5LP, which is a really interesting piece of microcontroller slash programmable logic.

**Werner:** Oh, yeah. Yep.

**Bluetooth:** And analog programmable stuff.

**Werner:** Yeah. Yeah, it's got like the switchable... You can switch in like op amps, like nothing... I remember the profile on those is like, none of the parts were great, but you had a lot of them and you could make them configurable, which is like super awesome.

**Bluetooth:** So it's like a CPLD, not an FPGA, but the CPLD and then some programmable switch cap filters.

**Werner:** Yeah, yeah.

**Bluetooth:** A reasonable 24-bit Delta Sigma ADC, actually. Not super great, but it wasn't bad. But it's an insanely expensive microcontroller.

**Werner:** Yeah. Yeah, and there was a Bluetooth version as well that was even more, right? Or is that when they went to 6? That's the problem,

**Bluetooth:** that they actually lost more or less everything that was reprogrammable in that. They significantly shrunk all that great stuff that the PSOCK 3 and 5 had. But the PSOCK 6 is the one with the dual core and the Bluetooth. And then there's the PSOCK 4 that's basically just a Cortex-M0 with Bluetooth. That's nothing really special. Now, the PSOCKs were interesting. Ah, I see. We're actually still using that in production fixtures because it has an insane amount of analog I.O. And it can drive an external CPLD for muxing because it comes in a 100-pin package. So it has a lot of I.O. But that was the initial thing. And it got me started into the whole programmable digital hardware as well. The CPLD stuff.

**Werner:** Right. So I think my first exposure to the Cortex stuff, I think you had sent me, you and I met each other at the San Francisco thing, and we kept in touch. The old one. I think you had sent me the actual unit. I actually have one of the ARCs. Yeah, the ARC. Yeah. So you had sent me one of those, and I tried that out. And that was 2019, maybe? So maybe describe what the box looks like. People might recognize it when they hear the description.

**Bluetooth:** Yep. So it's an aluminum extrusion, black standardized. And it's basically one large heatsink because of the electronic load capabilities inside. So it's a functional design. Even though I like the design. It's an engineering design. So it's a small box with a USB port and a DC jack on the back, banana plugs, and an expansion connector on the front. That's basically it. It's a completely headless multi-instrument.

**Werner:** Yeah. Yep. And that one was basically a pass-through style, right? So basically, I needed to power that externally. Is that correct? Or maybe I'm misremembering?

**Bluetooth:** No. Well, you need power available, but there is a power supply inside. Oh, it's self-large? It's a two-quadrant power supply. So it will source positive voltage, and it will sink negative current. So basically, if you have a positive voltage on the outside, you can sink that into a negative voltage into the electronic load. So that's what it does. And so it has a DC jack, or if you're only going to power small things like coin cell-based devices, you don't need any other power supply than the actual USB port. So that one goes. It will deliver 500 millivolts to 5 volts, depending on how it's been configured. Due to the old design that that one has, it's a design that started way back in 2000, late 15 or 16. So if you're USB powered in maximum accuracy mode, you can output up to 3.75 volts because of all the burden voltage drops inside. Because we only have 5 volts, there are no step-up DC-DC.

**Werner:** Ah, right, right, right, right. Yeah, makes sense. And it's not USB-C, so you can use the PD and get higher voltages to step down later, right?

**Bluetooth:** Unfortunately, not at the time. It's something that was designed for single-cell lithium-ion, basically. Again, we're back to cell phones. That's where it started. And that's what we had in most things, except the tablets in certain cases. Yeah. So it's up to 5 volts. And unfortunately, due to us not having a negative enough voltage, the common mode voltage on the instrumentation amplifiers doesn't allow us to go lower than 500 millivolts on the output. Ah, yeah, yeah.

**Werner:** That makes sense. Yeah. I have to ask, were you dismayed by the Keithley 2306? Was that your previous thing that you had been using on cell phone stuff? I know that was on a lot of cell phone stands.

**Bluetooth:** We use that a lot, actually, for initial bring-up of charging circuitry, etc. But it's a less than ideal instrument to try to automate. I know that it has GPIB, but it's still a mess to actually try to get the...

**Werner:** I don't know, man. There's a 2x16 LCD display on the front. What else could you need? And a couple of arrows.

**Bluetooth:** Then you try to explain that to the normal software developer that has to deal with this, and then it just question marks. It's just blank stare. And the whole thing about compliance voltages and all, it's a very, very complicated thing to explain to somebody that does not have the slightest of interest in learning all about an SMU. So this is half an SMU, basically, but with a lot easier user interface because all you do is you interact with the PC software. Yeah.

**Werner:** Cool. Yeah, that's great. I mean, I came from Keithley, and I was kind of indoctrinated into like, no, you need a front panel. No, you need to have buttons and interactive, whatever. But I am 100% in the headless these days. I mean, like, I'm Analog Discovery 3, Analog Discovery 2 and 3, and like Koitek and Jewelscope and all these things. Like, it's just, first off, I think portability, second off, scripting. Right. Third off, I don't know, like just size on my bench. You know, I don't have room for these huge half-rack boxes anymore. Even if I did have room, it's not a great use of space. I'm sure Dave, if he was listening, would be shaking his head. But I just, for me and my current lifestyle of IoT devices, headless is the way to go.

**Bluetooth:** So basically, the whole thing is, I have the same thing, that I don't have infinite amount of space. And ergonomics-wise, if you have a lot of instruments mounted on shelves, several stacks high, you need to get to it as well, which is not great. If all you have is a large-ish screen and the keyboard and mouse or some other input method, it's a lot more convenient. So I'm thinking, no, I'm not 100% headless because I have some keysight DMM and a large electronic load and a signal generator. But I don't really use the front panel, but it's there. It's all Ethernet connected. So it's all remote controlled anyway, because we're using the high-end keysight DMMs to do calibration of the Koitek stuff in the factory as well.

**Werner:** Yeah, and I think that's the other thing too, is once you have the tooling in place, it's just a different mode of operating. And I think it's kind of bench side versus computer side, right?

**Bluetooth:** Yeah, and then how often are you actually at your desk doing testing? I mean, we have people doing lots and lots of field testing in cars, in, I mean, IoT devices, they tend to move around at least some classes of it. So you actually need to do measurements on the go. Oh yeah, okay. So that's one way of doing it. I mean, it's...

**Werner:** Yeah, right, right. It's easy enough

**Bluetooth:** to just throw in your bag, the Koitek instruments in that case. If you have a reasonable USB port with a new version, the OTAs, you get up to 15 watts in most laptops these days. Unfortunately, not more, but that's what you're getting, 5 volts, 3 amps.

**Werner:** Yeah.

**Bluetooth:** It's still pretty good. We're using some of it, and there is some conversion losses, but you can power some... Which is still, I mean, pretty good. Most battery powered equipment, I would say, but not all. Yeah. So there is still DC adapter available because the new version of this box can output a lot more power if it has power available either through USB-C or the DC jack because it actually has a proper PD modem so you can negotiate up to 20 volts, 3 amps. But no computer will give you that yet. No hub will give you that.

**Werner:** Oh, wow. Okay. What will? Do you have to have like a dongle plugged in on the wall or something or a wall jack?

**Bluetooth:** Basically, what I had to do is that I had to splice together the CC pins and VBUS and ground from a USB PD adapter and then ground and USB data pins go into the PC. Three to one, two to one USB-C adapter. I got inspired by the Google Twinkie PD analyzer that I found but I couldn't source so I had to build my own off. Yeah. When is that? A month ago, basically. What's it called? A USB Twinkie? I've never heard of that. It's a USB PD analyzer

**Werner:** so that you can actually

**Bluetooth:** analyze the communication over the control channel on the USB-C link. So you have the two CC pins, CC1 and 2. Either you connect resistors to so you get the voltage so that gives you a rough idea. Are you a host? Are you a device? Basically, source or sync? Who's in charge here? Who's in charge? And then you can start doing the modem thing and actually do communication and then decide, no, I want to switch roles. I want to switch to a different contract. Actually getting the source and the sync to decide on the best contract to use. So it will say I can output 20 volts, 3 amps. I can output 15, 9, and 5.

**Werner:** You know what would be useful in the field? I'm just staring at my laptop as we talk about this stuff. So I have a USB-C charger and those things, yeah, the chargers are actually beefy. I can do 100 watts. But what if there was like an inline before the computer, right? So I go USB charger at 100 watts into like some interstitial and then from the interstitial that negotiates the 100 watts there. Some of that goes out to my Koitech and some of that goes to the computer. Is that possible, you think?

**Bluetooth:** Yes. And it's definitely possible and I've been very, very close more than once to design a hub like that.

**Werner:** Okay. I think it would be useful for a lot of things. I mean, like I'm just powering so many things off USB-C these days too. Like I mentioned, I have an Analog Discovery 3. I have other USB-C stuff kind of all running there and just having that power available. It's almost like we'd have to kind of like hijack

**Bluetooth:** the high power. Yeah. The main thing is that you need a very beefy USB power supply to begin with if you're going to do that and actually have some, I mean, the USB-PD EPR, the extended power range, and now that can go up to 48 volts, 5 amps. So you get 240 watts out of USB-C port. Whoa. Really? Wow. That's the latest stuff. It requires specific cables which are electronically marked, which is the fancy way of saying that, yes, there is at least one microcontroller that can be reprogrammed in the cable. Uh-huh. I mean, it's insane when you think about it, how cheap and small those things have been so that you can just shove one or two in the cable and then get it hijacked and get malware stored into it somewhere. Well, that's a different problem. It's a different problem. It's just that I have the background from security, so you always think about that.

**Werner:** Yeah. Unfortunately. See, episode, I don't even remember what it was, MG from the OMG cable. Have you seen that thing? Oh, boy. It's creepy. I mean, Mike's awesome, but that device and just the fact that I think about this every time I plug in a cable these days of just, you know, you think about these USB jacks that are at airports and, you know, these charge boxes and just, what are you plugging into? You know, just like, people should always be asking this stuff and I still love it. Yeah,

**Bluetooth:** it's trust no one. That's, you just, you don't. So, this is the problem where previously, with a USB-A, a regular USB 2.0 USB-A cable, it's four pins plus a shield. So, you have the ground and the V bus and D plus and D minus. There is nothing else. If you isolate D plus and D minus, you're good because there is power. It's five volts always. On USB-C, it's a lot more complicated because you actually need the USB-C, CC pins for communication. an ideal source will give you zero volts on V bus until it actually detected that there is a device connected on CC. The 5K1 pulldown on one of the CC pins indicates that there is a device connected. And, if you provide that, then the source will start communicating over that line. It will actually superimpose a digital communication like modem on top of that. So, there is really, it's a lot more difficult to isolate yourself completely because the computer, the Apple MacBook I use, it has the new 140 watt power adapter. So, it actually uses the 28 volt 5 amps setting. So, it talks a lot. It's an insane amount of chatter on the CC pin before you actually get to 28 volts.

**Werner:** Yeah.

**Bluetooth:** Yeah. And, it identifies the serial number of the charger. It identifies the serial number of the cable. There is a lot of things that you can buffer overflow, I'm fairly sure. So, it's just one of the other attack vectors and it's good because USB-C is the ubiquitous adapter of choice and it's starting to get really useful when you can get up to 240 watts. But, going back to the whole hub thing that you would need, it's perfectly possible to do something like that but you end up with a power brick for that like the docking stations. I have a Dell docking station with a 240 watt power supply, I think. It's a fairly hefty power supply. And,

**Werner:** that's not USB though, you're saying?

**Bluetooth:** That's, no, it's one of those barrel plug, really large laptop style

**Werner:** things. Some of it I do wonder about like the just the amount of copper, you know, just current going over these copper connections, you get some build up on these things over time. It's like, you know, the USB-C is an interesting thing and there are multiple pins that are dedicated to power but they're not big. There's not a ton of copper there.

**Bluetooth:** There is not a ton of copper and I mean, that's the reason why they topped out at 5 amps. But 5 amps is a substantial amount of current and now when they've gone to 48 volts, the tip of those contacts have a very, very specific shape so that you can direct where the arc will go because there will be an arc when you unplug at full load if you're not, you want the CC pins to disconnect first and then you want the voltage to drop very, very quickly when you unplug under full load because otherwise you're getting a sustained arc because it's DC. This is the problem with 48 volt DC systems that when you get an arc, it's a very large arc. So it's an interesting problem and that's why most of the USB-C pin, USB-C connectors that you find, they're still only rated for 20 volts.

**Werner:** Yeah, yeah. That's why we should switch back to DB25 for everything and then you can just put a couple of those pins, put the 48 volts on the left side, you put the ground on the far right side and you're good.

**Bluetooth:** They were also not designed for

**Werner:** that plug. Not ideal. I know. Can you imagine though, it feels like someone just the anti-Apple method, just like, you know what, screw it, we're going back to DB25.

**Bluetooth:** it's going to be interesting to see what Apple comes out with when it comes to cell phones because they're still holding out with the whole lightning connector on the phones, but they move to USB-C most everywhere else.

**Werner:** So I'd love to get back to that idea of software defined power supplies that you talked about in that HDDG talk, which of course I'll be linking in.

**Bluetooth:** Right. More power supplies in more ways than one. So it's a thing that keeps coming back, doing everything from the world's first wireless tattoo machine, for instance, also using that same power supply. That was featured in that talk. It's been remodeled in a new version as well. Cool. What we have been using is Coitech ARC and now ACE programmable power supplies, electronic load and precision current measurement. We actually started that way back in 2011 as a side project where we started experimenting with battery powered rotary tattoo machines. Cool. And you had some really interesting design requirements that it could only weigh half of the cable. Oh, wow. Because that's the cable that normally hangs off of your tattoo machine and then into the floor, down into the floor. That's the weight that the cable adds when you're holding it. So 64 grams, if I remember correctly, was the total amount of weight for the battery and the electronics. So it's radio controlled over 802.15.4. Not Zigbee, but the same radio. So that's the first place where this power supply actually got used. The idea of having a completely software-defined buck boost regulator. Because the other solution we had from Linear was an IC with an H-bridge in it. And we kept destroying that when we stopped the motor because of the back EMK. Because the back EMF. Yeah, right. It completely killed that ship. It didn't survive. So we needed bigger MOSFETs. And the smallest way to build this was with the Atmel now Microchip X-Mega microcontroller because it had the fast 2-Mega sample ADC. So we could actually do constant current constant voltage regulation in firmware.

**Werner:** That is super cool. And actually this came up again. I was thinking about this when Cian Lohr was on the show recently and he was talking about this new CH32V003, the little Tencent microcontroller from a VS5 microcontroller. And he was building his own buck converter out of it. And I was like, I actually knew someone who did that with a different part obviously. And it kind of had me calling back to this HDDG talk back in the day.

**Bluetooth:** Yeah. For the normal control loops, it's actually easier to get it stable than trying to make it analog. Why is that? Because of the phase relationship is basically you only need to know what's the latency from me sending a new command to the DAC or to the PWM until you actually see the change back into your ADC conversion, which is very, very easy to measure. And then it's very, very easy just to add that delay. You don't need to switch out components. You don't need to do any of that because you tune it completely digitally.

**Werner:** What about the external? Like one of the things with control systems though is that you have external capacitance or just delay in the system because you're powering something out in the world. So how do you deal with that

**Bluetooth:** then? Yeah. Then you can have a dynamic delay if you encounter this. So you can have a longer delay if you encounter that it takes too long for this change to show up on the output. I've been doing this for LED lighting control as well where you drive a system into constant current. and this is always a problem when you're in constant current and you lose regulation because you disconnect the LEDs. They tend to shoot that up to maximum voltage possible. Right. Yeah. So you need to detect that as well and immediately cut the power and then do a slow start when you detect that you actually have something connected to it. So all of that is way easier to do in a digital control loop than the analogs.

**Werner:** So do you keep a local variable of last known delay? Is that how you

**Bluetooth:** deal with that? I have been doing it. Most of the time we haven't had the need to actually tune it because it's been stable enough. For the cortex stuff it's now these days it's actually a hybrid of an analog control loop and a digital one. So it's an interesting thing because it is difficult to get short circuit protection working reliably when you have a digital control loop because you can't react fast enough because the AGC has a certain amount of latency before you even get to seeing the numbers and you can make a decision based out of it. So you need basically a two-step process. You have an analog cutoff when you know that there is a short circuit or severe overload and then you can react in firmware to take control of that and make a nicer regulation when it comes to constant current for instance. So it's best of both worlds in that case because in some cases you don't want your current sensing burden voltage to be seen on the output of the power supply. So then you actually have your sense your analog remote sense on the output of the power supply which means that you need a fairly fast potentially unstable regulation to make sure that you have the correct voltage on the output and then you can slow that down digitally.

**Werner:** Got it. Yeah. Okay. So you kind of you have to really kind of maintain the state of your control or what's it called your phase state space or something like that?

**Bluetooth:** Basically your phase margin if you look at it from the mathematical point of view. The main reason why there is both analog and digital control in some cases is the fact that there is no ADC converter and front end with that low latency. I mean the X mega was the fastest one I could find and it took I think it was one clock cycle per bit plus an additional one so it took 13 clock cycles at up to 2 megahertz that was the latency and then every clock cycle you got a new sample but it was 13 cycles delayed right yeah like a pipeline almost huh yes so it was that that's why that ADC was so fast because it was pipelined no other MCU that I found at that time in that small of a form factor had a pipelined ADC which could also do differential measurements ! actually which is kind other quirks but it's a really good ADC for the time and I still

**Werner:** see it being it everything in this space is interesting to me because it's like I guess the other one that I think about obviously a very different kind of problem space is like real-time audio processing type stuff where again you're pipelining stuff you're taking a reading you're trying to get something back out around the loop so that people hear it so like digital guitar pedals and things like that you can't just delay it forever and sit on the data and process it because the people want to hear it they're expecting some kind of real-time they're used to the analog side of things but there's also that same delay problem

**Bluetooth:** I was involved in another project with real-time audio actually when is that

**Bluetooth:** two years ago now the Elk audio guys has a product where you can play together with your band and practice over the internet oh yeah yeah that was huge during the pandemic right yeah exactly this came out on the tail end of the pandemic due to component shortages and whatnot they have a bridge with an IMX8 Linux system with a real-time processing on the side and an FPGA

**Bluetooth:** dealing with the local audio codec and ADAT support in the FPGA and then just sending that in as TDM into the IMX audio system so they have a very low local latency so basically you just add the internet latency on top of it so you can do real-time jamming sessions from Stockholm down into Italy which is that's pretty cool hundreds and hundreds of miles yeah

**Werner:** how do you deal with the delay then because like it's like that there's also like the brain processing right so like I want to have a reactive kind of like I hear that my drummer is doing something and I want to react to that quote unquote real-time human real-time right here's the

**Bluetooth:** thing that if you're used to playing on a stage you need to take speed of sound into account

**Werner:** yeah

**Bluetooth:** right

**Werner:** right

**Bluetooth:** so you have those milliseconds of latency to play with

**Werner:** it's

**Bluetooth:** a few tens of milliseconds that's all you have then you're gonna start to lose your sense of this it no longer makes sense

**Werner:** I

**Bluetooth:** would say that you have around 30 milliseconds or so and it also depends on how fast you play

**Werner:** true right yeah do you dream different than someone playing a ballad right

**Bluetooth:** exactly so it's a very interesting space when it comes to audio processing that needs to happen fast and you need to have it pipelined but you can't delay it forever it needs to be done and you need to be able to set it out yeah we have the exact same problem in the the new hardware because interestingly enough the IMX8M nano has the Cortex-M7 which is a beast on its own by the way it's a very useful real-time system that's exactly the core that we're using in the Cortex-Ace the RT-1060 series yeah yeah that's

**Werner:** great which is the same as the Teensy as well we were just talking about that in the last show that was just released

**Bluetooth:** yes and it's due to Mr. PJRC himself Paul when I was in discussion with him during the last maker fair in Bay Area in 2019 that it is the 1060 that actually sits in the Ace and not the 1050 that I was initially looking at

**Werner:** interesting interesting

**Bluetooth:** he strongly discouraged me from selecting the the 1050

**Werner:** series Paul if you're listening he's not listening but he's on my list of guests that I refer to as white whales because I've tried to get him on the show multiple times and he still refuses but I'm going to keep trying oh

**Bluetooth:** yeah he's great that was a very good decision looking at the errata that you could see for the 1050 when you looked into it so back in 2019 it was a very short lift of Cortex M7 to choose from there was a Sam something from Microchip slash Atma which had like 20 pages of errata and there was the NXP part the 1062 1060 series and then there was an ST Micro where you couldn't get Ethernet and high speed USB in the same silicon for some odd reason I was looking into that we wanted to have the possibility to have an Ethernet port and high speed USB so there was just two of them left one of them was the Sam with a huge errata and then the 1060 series from NXP so that's how I ended up with the 1050 and then talking to Paul and then it's a 1060 so that's the one that's on the teensy 4 I believe

**Werner:** yeah 4 on the 4.1

**Bluetooth:** we're using the slightly larger footprint though because our board is fairly large you don't want to manufacture that as a high DPI board

**Werner:** if you

**Bluetooth:** can

**Werner:** avoid it well let's talk a little bit more about the ACE is the new one could you explain what the Coitech problem space is solving

**Bluetooth:** yeah what we're trying to solve is people wanting to make their battery powered IoT devices last longer so you want to optimize your hardware you want to optimize your firmware and traditionally optimizing firmware has been kind of difficult because you need to involve somebody that can do high accuracy power measurements and then you need to do that together with somebody that actually knows how the firmware works it would be ideal if the firmware could actually do this themselves a regular instrument to do this will be too complicated to figure out for software developers you want the UI that is more software developer friendly basically so we're trying to make it as easy as possible to do power energy current measurements together with GPIO and serial port inputs so you can trace what you're doing and record that together with the analog measurement so you can actually get it synced so if you have a trace output from your firmware you can immediately see what's happening during certain parts of the current consumption

**Werner:** so

**Bluetooth:** that's the super simple problem space we're trying to solve and what it actually is is that it's a programmable power supply which is two quadrant so we can source positive voltage and we can sync the negative current coming back so that means that we can discharge a battery creating a battery profile and then you can emulate that battery back because we have programmable output impedance or resistance on the output so that it behaves like a battery again coming back to the whole software defined power supply it's very much completely up to the firmware slash gateway to do that so that's a great part

**Werner:** yeah and so the one we're talking about as well the ACE is the successor to the ARC is that right yeah so

**Bluetooth:** basically the same concept applies it's just that the voltages and in some cases the currents have changed the initial ARC that's been out since 2017 has an output voltage of 500 billivolts to 5 volts at

**Bluetooth:** the highest range with a maximum output current of 5 amps it can sync up to minus 2.5 amps the new ACE is 0 to 25 volts output and it is plus minus 5 amps

**Werner:** yes

**Bluetooth:** and so

**Werner:** now I can blow up blow up devices with abandon so

**Bluetooth:** here's the thing that we had that scenario in mind so the software will actually have a preference setting of the highest available output voltage so that people don't make that mistake most people don't want 25 volts on the output right you gotta click a couple buttons to get there I hope at least need to go into the preferences and set I want more than 5 and a half volts so you need to select your maximum voltage I know that this is gonna mess some stuff up yeah I mean 25 volts is a lot yeah and the interesting thing is that we've gotten some questions that okay but I'm powering it from my 5 volt USB yeah it doesn't really matter because there is an isolated power supply inside that will generate plus minus 30 volts

**Bluetooth:** I mean it's a fairly simple construction but with some quirks because it has three isolation domains I mean the interface the USB and DC jack on the back is chassis ground referenced and then you have the main terminals the banana plugs on the front those are isolated and then you have the expansion port which contains the serial port all of that and additional sense inputs that's also isolated from both chassis and domains three completely separate isolation domains

**Werner:** yeah why did you make the expansion port separate I would expect that to be on the same ground as the output so

**Bluetooth:** there is a ! the

**Speaker ?:** reason

**Bluetooth:** is when you design battery powered devices and you have a column counter or just current shunt it's much easier to put that shunt in the negative terminal on the battery because then it's ground referred then you don't do high side current sensing

**Werner:** which

**Bluetooth:** also means when we are replacing the battery our minus terminal is no longer system ground so that's why it needs to be separated in the original arc there is no isolation we actually had this problem a couple of times ago you accidentally short out your column counter on your device basically it believes it draws no current at all right that's the result of it which also means that it's difficult to charge a chargeable battery if you're using that shunt to control current

**Werner:** yeah so

**Bluetooth:** and that's the the simplest reason why you can actually connect several of these aces in series if you want to generate even higher than 25 volts of current as well oh stack them up huh yeah that's pretty cool up to 200 volts

**Bluetooth:** difference is and

**Werner:** that's limited based on the isolation of the transformer internally

**Bluetooth:** isolation of the transformer capacitors I mean decoupling capacitors from ground plane to ground plane and just general sanity check that most of these instruments will not let you lift ground off system ground more than one or 200 volts I mean looking at the general DMMs from Keysight or any of the other known brands they also have very specific markings that your minus terminal can be a maximum of one or 200 or 250 volts from ground

**Werner:** yeah and if you don't know what Werner is talking about right now this is not a feature for you when you start floating grounds and then you and then you're like huh I think I should measure something on my laptop which is chassis grounded or my desktop I mean it's

**Bluetooth:** complicated yeah I mean unfortunately that's how the first design was done because it was the easiest to get going and looking back doing type approval of a device that has two isolation domains it's very difficult to not have some interesting harmonics show up on your cables which have very little ground return

**Werner:** yeah right right exactly yeah that current wants to get back somehow but it's not the traditional path

**Bluetooth:** it will find a really annoying way back to system ground and it tends to show up on emission measurements especially when you are also doing simultaneous sampling so that's another feature that we increase the sample rate a lot from our four and one kilo sample a second in arc to 250 kilo sample a second on the ace and it's simultaneous sampling ADC so we have eight ADCs well it's two four channel AD converters doing simultaneous 250 kilo sample conversion

**Werner:** and you do it do you do like the step offset thing where each one is just like a sample or two behind the other

**Bluetooth:** nope there are actually zero samples ! identical sigma delta modulators and filters in those chips so why do you do it all at the same time then?

**Werner:** was there a benefit for that?

**Bluetooth:** because you want to make sure that voltage being measured and the current are from the same time otherwise you can't properly calculate power

**Werner:** okay

**Bluetooth:** those samples need to be from exactly the same time

**Werner:** okay

**Bluetooth:** so it's it's calculating the power on a sample basis and then you average it out for energy consumption over time

**Werner:** got it

**Bluetooth:** so this all gets mangled from the two ADCs into two FPGAs which turns it into audio signals for the IMX RT-1060 so I can use the the great serial audio interfaces on the IMX to retrieve all these 32-bit samples

**Werner:** yeah okay interesting and there's there's additional software or sorry there's additional silicon on those parts that is beneficial that it's an audio versus just kind of like raw data format

**Bluetooth:** yeah because otherwise you have to basically do SPI

**Werner:** uh-huh

**Bluetooth:** or some parallel access if you're gonna just capture data but then you need to be constantly talking to that peripheral saying I want to transfer all these data it's a lot easier for the audio hardware to recognize the frame marker to know which which word is which so which is the first word of this multi-channel audio stream and then just DMA that straight into their own separate buffers in internal memory

**Werner:** interesting and so then are there eight DMAs going into eight sections of memory as well

**Bluetooth:** it's only it's only three separate DMAs which which does that it's due to the fact that it's three separate interfaces on this RT-1060 you don't have an eight-channel audio interface and on the other side because of the isolation between the main side and the expansion side there's four channels coming from one ADC on one isolation domain there's four others coming from the other isolation domain so it's four plus four

**Werner:** and their sample

**Bluetooth:** locked to the same oscillator and this comes back to emissions there is one single reference driving every single thing in this design and it cannot be spread spectrum because it's the Sigma Delta modulators they really dislike frequency variations because it creates noise it needs to be a very very sharp spike which is very bad for emissions and you

**Werner:** send that across an isolation barrier as well yes using an opto or something else

**Bluetooth:** it's one of those really small isolation gap transformer RF thingies on semi has a few of those and TI has a few of those yeah I was going

**Werner:** to say TI TI does those too yeah okay so like basically like the digital isolators it's digital isolators you're saying a pulse over digital isolator and you do you have to characterize the delay in that as well then or is it you just assume it's the same across because you're using the same isolator

**Bluetooth:** they are specified to be isolated to isolator within a few nanoseconds

**Bluetooth:** 100 to 150 megabits per second yeah yeah those are expensive yeah they're not cheap ones and they're also one of those that were slightly unobtainium during ship shortage that and the ADCs yeah

**Werner:** the problem there is that all the car people like those too yeah yeah they like the high speed

**Bluetooth:** across barriers yeah yeah the good thing is that they tend to use the slightly slower ones but yeah we had problems with car people and the RT1060 series because we're using the the larger pitch the 0.8 millimeter pitch BGA because we didn't want to do a high density board on a board that's 140 by 100 millimeters so it's a standard I mean it's one of the things that our favorite prototyping PCB places can do without even flinching yeah exactly yeah they're like oh just that

**Werner:** oh no

**Bluetooth:** problem right exactly it's one of those so if you keep to 0.8 instead of 0.4 65 yeah it's not 4 it's a lot more same than that it's slightly smaller it's the one that's on the TNCE4 I think it's 0.65 I can't remember it was a bit more difficult when you needed some specific pins because this has been carefully chosen so that I'm getting access to all of the audio subsystem pins

**Werner:** yep yep totally

**Bluetooth:** and it required some very particular pin maxing in this I mean it's still 196 balls and it still was difficult to actually get all of that out together with USB and Ethernet and two SPI buses and an I2C bus so there is quite a bit of interfacing going on because you do housekeeping with the ADCs over SPI and you also bootstrap the FPJs over SPI so there is one SPI bus going to each isolation domain so you can do that in parallel and then you have all the audio interfaces of data coming back yeah

**Werner:** huh

**Bluetooth:** so it's an interesting setup it's basically a very large audio interface

**Werner:** huh that's really interesting idea I like how you did that it's one of those !

**Werner:** one thing that you had actually sent me one of the ARCs way back in the day and I've had that on my bench for a long time and doing measurements and stuff and then I got to hang out with you and Vanya your CEO and some of the teammates at Embedded World this past year and I got to see a demo of the new functions which are actually something I had not seen on any of the other products because this is a popular space I feel like the high dynamic range low super low current all the way up to transmit power type of stuff there's a lot of stuff out there including the low medium and high end solutions that are out there but I had not seen the battery stuff can you explain that yeah

**Bluetooth:** so basically because we have the ability

**Bluetooth:** to do current battery and then perform a discharge cycle at varying levels of current measuring the voltage when we have put this load on and basically recreating the internal resistance of the battery at each state of charge this has been done by Keith Lee as you're very familiar with many years ago they tend to have fewer steps typically it's one one step per percent because that's what you can possibly manage with the small display simple keyboard if you're not doing remote management of it so that's the still expensive test equipment that we were using and the battery guys were using at Sony when this was initially conceived because we needed to do power measurements power optimizations closer to the firmware guys and they just couldn't figure out the whole thing about battery simulators ! battery emulators

**Bluetooth:** With a lot of these settings just to get it to sync current you need to make sure that you have the compliance voltage set up correctly otherwise output voltage might go negative it's it's a very very different world when you're entering ! proper SMUs and it's difficult to explain to people that's not really interested in battery technology but you need the technology to be able to measure the impact of firmware because looking at it firmware has a huge impact on battery life if you missed out to turn off peripherals you forgot to go to sleep all these super simple things that it's going to be very difficult to have a discussion between the expert of power measurements and the people doing firmware one

**Werner:** thing that really popped out to me is that you showed me on screen you have this characterization so you stick a battery on this thing so I go and buy a generic ! lithium ion pack from somewhere in China which I've done before and they tell me it's 850 milliamp hours whatever and you could characterize it not only the capacity but the actual curve all the way down you could start to average them and make you would show me a curve basically right

**Bluetooth:** yep basically you start at the fully charged battery either it's a rechargeable one or it's a primary cell the same procedure is applicable to both you will discharge the battery until you reach a certain cutoff voltage and stop the profiling and say I'm done I got this much capacity out of it basically the amount of charge you were able to extract from it so that would be columns or amp hours or energy as in watt

**Werner:** ! hours right but then the key thing for me was not just that because it seems ! there's a lot of

**Werner:** you can do that with a DMM and a timer right the key thing for me is that now you have this curve you

**Speaker ?:** could

**Werner:** replay it that I don't think I've seen that before maybe it exists other places but I had never seen that before personally

**Bluetooth:** we've actually had it for quite a few years on the arc as well the same concept applies it just that it's now more accurate because you can select the mode and select this profile and then you select where you want to start at which state of charge you want to start at the full battery you want to start at 50% depleted or close to empty and then you can choose whether it should track discharge which a normal battery would do or you can just say I want to stay right here and freeze so it's

**Werner:** a timeline too I'm assuming you could say do 175 50 25 0 and then you could see all of the different things of how your device might I just imagine I remember seeing this and thinking continuous integration testing is a great target for this sort of thing

**Bluetooth:** continuous integration testing of things like how does your device deal with battery is about to go empty exactly yep exactly and you want to replay the exact same scenario every time you want to start at 90% depleted and actually see that the device performs a graceful power off whatever it's supposed to do right right so yeah it's exactly that and for firmware development as well when you're actually developing these things you might actually want to have the battery freeze at a certain percentage

**Werner:** it's

**Bluetooth:** a very interesting thing which is a super super simple thing when you're looking at it as a feature but the gains is actually huge because you can do this yourself if you're fast enough with a regular power supply but it's not going to be as good because you need to be able to react fairly quickly to change it in load because that's what happens when the battery either gets depleted or it gets old because the more charging cycles you put on a lithium ion battery the higher the internal resistance will become or the impedance so that's what's killing the battery earlier and earlier typically for devices when the battery ages because you can't deal with this drop in voltage when you have a huge spike when your radio turns on for instance it just collapses

**Bluetooth:** what's happening because the internal resistance is nowhere near zero even though the lithium ion batteries are way better than coin cells you measure it in tens of ohms which is why you can't shove random transmitters on a coin cell because it doesn't work some of them like LoRa you can actually do on coin cell but maybe have a bunch of caps there too switch it over to a

**Werner:** super

**Bluetooth:** cap circuit or something like that and manage that yeah the problem with super caps is that they tend to leak a lot it's a lot of leakage current but there are some interesting battery types with low internal resistance and high cycle use which you can actually use

**Werner:** so

**Bluetooth:** it's very dependent on which battery you choose the whole cycling thing is something that is new and unique to the ACE actually so we can now do automated testing charging and discharging the battery in cycling as part of the advanced battery validation stuff

**Werner:** oh okay so you would actually so you you discharge the battery then use the power spline internally recharge it and then you kind of see it degrade over time yep oh cool

**Bluetooth:** it's a very simple way of doing it so basically think of it ! as an ! arbitrary waveform generator which is capable of setting a positive or negative current going in and out of the battery

**Werner:** oh you would do that it wouldn't just be a constant current you would actually oh you can pulse it you can actually

**Bluetooth:** you can you can you can categorize the battery even during charging by selecting two different or several different current levels during charging and you will get the same measurement of internal resistance there

**Werner:** huh yeah it is an interesting way to kind of think about it too because like my own migration of how I think I've thought about batteries over my career you know it's always voltage at first and it's like current but really thinking about resistance internal really impedance I suppose yeah of the battery is the best way to think about it because of how and really like during delivery of power

**Bluetooth:** back out and there is a simpler and a very much more complicated model of that impedance it's a complex impedance when you start to really drill down into it it's very complicated certain battery chemistries have a slow start for instance that you basically don't get any energy the first time when you start to discharge it and then it recovers coin cells are like that when they've been sitting around for a year or so you actually have a passivation layer on it that you need to burn off for it to actually generate current so like

**Werner:** if you manufacture and you stick it on a shelf somewhere you kind of have to have like a startup mode sort of thing

**Bluetooth:** basically if you if you're if you're doing the the non careful way of pulling it out of the package so that you actually touch both sides of it that discharge is typically high enough to trigger it but if you're careful not to touch it and you haven't actually measured the voltage it might take a while for it to to engage wake up so much yeah so this is why you have this the 10 mega ohm input resistance of a multimeter people tend to think that that's that's a lot but 10 mega ohms at 3 volts that's 300 nano amps right right so that's it's a sizable amount of current in this area and it depends on what you mean by low power right it means drastically different things to different people when you're talking to automotive it's low power seems

**Bluetooth:** to be milliamps whereas low power when you're talking coincell stuff it's sub microamp I mean it's several hundred nanoamps that's low power

**Werner:** yeah

**Bluetooth:** that's basically our limit today with microcontrollers and sleep I know that I had the Atmel Xmega thing sleeping at 250 nanoamps but that was without any way except either a GPIO trigger or a reset to wake it back up RTC added another 250 so it was like 500 nanoamps

**Werner:** yeah it's still not bad though it's

**Bluetooth:** still not bad but different people have different ideas I saw that Dave did the teardown of Keysight battery emulator the other day

**Werner:** that's

**Bluetooth:** a low power version according to them it's less than 200 watts yeah

**Werner:** I mean when you're used to building things for the bench it's a little different I suppose

**Bluetooth:** it is I thought it was funny it's low power but it can deliver 200 watts so yeah it's in comparison with their other stuff which is larger so it's I'm not surprised but you can clearly see that it's not only low power when you see bus bars really really thick bus bars inside then you know there's a lot of power yeah we've made the design on a single PCB so that we actually don't need any connecting bus bars or wires inside

**Werner:** yeah from a manufacturing standpoint that's always the best

**Bluetooth:** from a manufacturing standpoint when you're not making tens of thousands in each batch it's way way easier if you can have a single board we can test that single board we can calibrate that single board in one fixture yep and then you perform final testing and get the labels and everything printed

**Werner:** yeah I just

**Bluetooth:** think too of the

**Werner:** anytime there's cabling or someone tightening a screw down or any any kind of manual assembly it's just the cost just and complexity too right and other things that can go wrong I don't know like I come from the space of boxes that were for some reason the users needed to have a front and back control on everything so that means cables and yeah it really does complicate things

**Bluetooth:** the main thing with the traditional way of building in the in the DMM form factor like the key fleece as well is that you have a front panel with a circuit board behind that entire front panel and then you need to get that into a base board that sits in the bottom of the box and they tend to be fairly deep so they're large boards they're really large boards and that as well so when you tried something for the desktop we wanted it to be fanless so that you don't have any annoying fans and therefore it's designed like a heatsink functional design so that's why we're limited to around 15 watts of dissipation on the electronic load so you can't discharge at high power continuously it's just not designed for that

**Werner:** where do you see the ACE and I guess the ARC in the old days

**Bluetooth:** where are these being used mostly they're being used for field testing they're being used in production they're being used for automated testing and we have this in-house example of we're using the devices to manufacture the new devices ah yes the 3D printer style which is a good test of dogfooding I mean you're testing that your scripting stuff works so it's in the loop but in order not to introduce generational degrade there is a least traceable calibrated multimeter in series so that we're using that to to calibrate the units but everything is controlled by the expansion port and the main terminals of of an ACE in the ACE fixture and with an ARC in the ARC fixture

**Werner:** yeah it is the generational degrades kind of the Xerox effect is that kind of the thing there

**Bluetooth:** yeah so you cannot trust I mean when you're 10 generations out you can be way off that's just not how you can't do it

**Werner:** that way this traceable is important it is I mean at the end of it there's a fluke calibrator somewhere I know that you go far enough back in the chain and there's a 1980s fluke calibrator that some metrology engineer will not let you have unless you pry it from their cold dead fingers yeah

**Bluetooth:** it's interesting that for many years the the key site or it was probably even named agilent the 8 and a half

**Werner:** yes

**Bluetooth:** it was unavailable in the EU because it it wasn't ROHS compliant so it took them years and I actually saw the new the dark version at embedded world they had one of those on display in the key site booth so now it's back

**Werner:** and it's equally expensive you know what you had to do is you just got to sneak an 87.53 under your shirt when you go through customs anything to declare whoa did I have a big meal on the flight nope it was very square very very square yeah why am I feeling one you today

**Bluetooth:** that's a big multimeter those are I mean it has some significant limitations on what you can actually measure but it measures very very well it's not something that you want to shove 10 amps through I mean that's not what it does but 10 nano amps sure so it's I like the agilent key site SMUs those are in the Picoamp current with guard terminals and all that that's that's slightly I mean that's not where we're trying to go we're not trying to categorize silicon for instance I mean that's that's when you need those two channel SMUs with Picoamp of resolution I mean we still have a very very high dynamic range on both ARC and ACE we're measuring single-edit nano amps up to 5 amps so it's at least a billion to one

**Werner:** yeah

**Bluetooth:** I mean the steps the step size on the ACE is 400 and something Picoamps per step in that ADC I always caution people

**Werner:** I'm like if you think you need you know Picoamps just go check the price of the thing that measures it first I guess maybe not the ARC or the ACE but like you know square your monetary expectations towards your measurement needs and right size yourself you know you should always right size your measurement needs I mean

**Bluetooth:** it's more or less no for electronics design you don't need for semiconductor design yes maybe so that's it's in that ballpark so it's very important and we've had this discussion before when it comes to sample rate that we're replacing the battery on your device and what's the first thing you typically encounter on the PCB there is a bulk cap

**Werner:** dumping current right into that

**Bluetooth:** which will inherently yeah you drop it right into that and you've automatically created a really nice low pass filter so we're sampling at 250 kilo samples a second we're actually only presenting 50 kilo samples a second at the moment as the maximum number of samples that you can see so they're all averaged out 5x5 because most of the time you don't even need that measuring sleep currents you want even less I mean you want hundreds of samples a second or even one per second just to measure a sleep current and when something happens that's when you want the full high speed mode you want to go hyper

**Werner:** measure at that point right yeah turbo mode the turbo

**Bluetooth:** button basically that's what you're after because it creates quite a bit of data if you're going to do this for a month or so so you're limited by hard drive space only in this case and if you're recording both voltage and current and you can record an additional subsystem measurement as well using the expansion port there is an additional ADC plus and minus pin which you can connect a shunt over and then you can measure voltage on ADC plus to ground for your voltage measurement and then current is the voltage across ADC plus and minus and then you tell the software which shunt resistor you have and then you're getting that current in amps as well so there's a secondary channel

**Werner:** for that well Werner I would love to hear more about this in the future where can people check out the Coitech OTR or an ACE rather so

**Bluetooth:** you can check it out at coitech.com it's Q-O-I-T-E-C-H dot com and it's available on DigiKey and the usual distributors for immediate dispatch you can get one tomorrow morning if you need which is great

**Werner:** yeah that's awesome that's awesome all right well Werner thanks so much for joining

**Werner:** me and we'll chat soon thanks for having me
