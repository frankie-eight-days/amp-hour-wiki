---
episode: 356
title: An Interview with Piotr Esden-Tempski
url: https://theamphour.com/356-an-interview-with-piotr-esden-tempski/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released August 20th, 2017. Episode 356. An interview with Piotr Ezdintensky. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Piotr Ezdintensky:** And I'm Piotr Ezdintensky from One Bit Squared. Welcome. How are you doing? Very good. Thank you very much for having me.

**Chris Gammell:** Well, I feel a little embarrassed now. I was like, oh, I've been calling him Peter. But that's not right.

**Piotr Ezdintensky:** Oh, no, that's totally fine. I'm actually totally fine with being called Peter. That's totally fine with me because it makes everything easier. And I don't mind.

**Chris Gammell:** So you were pronouncing it in Polish. Is that right? That's correct. Yeah. And we met at DEF CON a couple weeks ago. And we were hanging out, obviously. But people in the audience probably have heard us talking about your projects. But maybe you could give me a little bit of background on where you're coming from and what you've been working on in the past couple years.

**Piotr Ezdintensky:** So, well, it's difficult to decide where to start with things. But I think the interesting thing is where the current stuff that I'm working on basically started. I was designing autopilots for UAV. Actually, at the very beginning where the UAV and drone stuff was coming about.

**Chris Gammell:** Okay. And what's beginning? Like, give us a year.

**Piotr Ezdintensky:** 2004? 2004? Somewhere around that? Sure. Yeah. So I was involved in it more for hobby reasons and then eventually got a job. And then through different channels, I eventually started designing my own autopilots. And that was around 2009, somewhere around that time. And eventually, after moving to the US and moving to Oregon, I founded OneWidSquared, where we basically built electronics for UAV that are open hardware and open source for mostly targeting paparazzi UAV. It's pretty much the grandfather of all open source UAV autopilot systems. Really? Okay. That's awesome. It was started in 2003 by a few guys at ENAC. It's Ecole Nationale de l'Aviation Civile.

**Chris Gammell:** It sounds French. Yeah.

**Piotr Ezdintensky:** Yes, it is very French. Yeah, they are in Toulouse in France. And these two guys wanted to compete in a competition for autonomous robotic UAV. And they basically said, well, let's build something. And this is where it started. And yeah, and they published everything they made because European researchers, that's how they roll.

**Chris Gammell:** Good for them.

**Piotr Ezdintensky:** Yeah. And eventually, that became paparazzi UAV. And much, much, much later, I joined that group and was helping out and building some autopilots for those guys.

**Chris Gammell:** And so, how do you define an autopilot? I guess we've talked about drones on here. And we've had Chris Anderson on in the past. And I guess maybe a couple other drone people. But how do you define an autopilot? Like what its function is?

**Piotr Ezdintensky:** So, for me, it is if it can fly itself completely autonomously without human interaction, that's an autopilot.

**Chris Gammell:** So, like you don't even have to give it a – it's just like powered on and it goes kind of thing or what?

**Piotr Ezdintensky:** Pretty much, yeah.

**Chris Gammell:** Okay. Yeah.

**Piotr Ezdintensky:** There is many definitions and really depends on the person you ask. It's like you have a room of 100 people. You ask them the question and you get 100 answers, right? But for us, especially because paparazzi is such a university and research-driven environment, that is the definition that in that group we would use.

**Chris Gammell:** Okay. Cool.

**Piotr Ezdintensky:** Yeah.

**Chris Gammell:** I mean, yeah. And you have to kind of put a line in the sand somewhere, right? Because I'm guessing if you kind of move back in the definitions a little bit, it's like, well, does it self-stabilize or does it just do waypoints or does it do all this? Yeah. Yeah. There's like lots of different steps that it can – where you can define it, right?

**Piotr Ezdintensky:** Yeah. Yeah. Yeah. That's right. This is the interesting thing. So, there is also many levels on the autonomy scale. For example, a lot of the UAV autopilot systems that are quite widespread, you might be able to set it in hover mode. It will stay in a position or it will be able to go through waypoints that you set on some tablet or something. What, for example, paparazzi is really setting itself off from other platforms is the fact that it can actually reason about what it is doing. Interesting. Okay. So, the cool thing is you have the so-called blocks and the blocks is like a sequence of instructions that are written in a domain-specific language where you can say and give it like definitions when it should do what. For example, you can read out sensors from the aircraft and tell it when the sensors reach a certain threshold, then jump to another block. So, basically, like a very simplified and very concurrent programming language.

**Chris Gammell:** Okay. Almost like a state machine almost? Yes.

**Piotr Ezdintensky:** Yes.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** Yeah. And because usually you just set a few waypoints and if you want to fly more than one aircraft, then you have to set the waypoints to all of them and then you press a button on all of them, then they take off simultaneously. But if you have a tree in front of you and then you will not be able to adapt the flight plan. Of course, these things are changing. And like, for example, DJI is making their aircraft and they have eyes now and they see obstacles and can avoid them. But it is not a very flexible system. The paparazzi thing is meant to be modified.

**Chris Gammell:** And you said it's mostly research-based or is it actually being implemented in commercial drones as well?

**Piotr Ezdintensky:** I know that there are commercial drones, but they are rarely admitting that they use it.

**Chris Gammell:** Right. Borrowing heavily from – they're heavily inspired by the code base?

**Piotr Ezdintensky:** Yeah. Yeah, you could say that. Yeah.

**Chris Gammell:** Okay. And so how does – I mean, it sounds like that's a very software-intensive kind of – maybe firmware-intensive kind of enterprise. But what does that look like on the hardware side?

**Piotr Ezdintensky:** Well, yeah. So, yeah, the software is the heavy part. But on the hardware side, what we try to do is provide the necessary interfaces and sensors that the people using the software would need. For example, having a CAN bus on the aircraft or on the autopilot because they want a secure communication between the subsystems. So, yeah, this is something we added very early on before there came about standards for the UAV CAN bus communications. Then we switched to STM32. I think – I wouldn't bet my money on it, but we were, if not the first one, very early on with this switch, going away from Arduino and AVR. We dropped it. I think this happened like in 2008. We dropped AVR support because you barely could run any – like you had to really disable most of the functionality to be able to put it on that platform.

**Chris Gammell:** Got it. Okay. But it's still an embedded platform as well.

**Piotr Ezdintensky:** Yeah, yeah, yeah. Okay. So, this is also interesting. So, Paparazzi is very flexible. We support a ton of different platforms. We have AVR and we have LPC. We have STM32, F4, F3, and now F7. And there is also a Linux version of it. So, you can run it on some drones that just run Linux on them. So, it's quite a flexible platform.

**Chris Gammell:** Yeah, that sounds like a headache to maintain though.

**Piotr Ezdintensky:** Well, headache, yes. In a sense, yes. But on the other hand, the architecture was meant to do that for a very long time.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** So, we have all the abstractions.

**Chris Gammell:** Hardware abstraction layers and stuff.

**Piotr Ezdintensky:** Exactly. Yeah. We have the abstractions. We have the interface. So, we have the APIs. We have the unit testing and continuous integration stuff running. So, if things break here or you add some feature that breaks somewhere else, then we are trying to be able to automatically find this regression. Got it.

**Chris Gammell:** Okay. Oh, that's great. I mean, that's the right way. That sounds like it's not really an academic kind of situation. Sorry, that sounds bad.

**Piotr Ezdintensky:** Yeah. Yeah. No. The people that are running the project, Felix Rues, who is the maintainer currently, he's doing an amazing job to keep this like a standard to all our code base and all our additions and where it goes at a very high level.

**Chris Gammell:** Yeah. I can imagine that running away. I mean, like anytime you can support multiple process architectures too, it can get pretty messy pretty quick, right?

**Piotr Ezdintensky:** Yeah. But eventually, that's why eventually we also say, okay, we have to drop this. Barely anyone is using that anymore. Right. Yeah. Let's get rid of that part. But yeah. Right.

**Chris Gammell:** And then is it like selectively integrating for whatever peripherals you have on hand? Is that kind of how that works? Sure.

**Piotr Ezdintensky:** So we have, so these are the airframe files. So we have this like XML definition file. It's like, yeah, it is XML. I know. But it is pretty readable. So you can add and remove features and switch between modules that you load. So you can configure the whole thing, what you compile into your autopilot software based on that. So you can, and we are trying to make it as intelligent without being too intelligent. Right.

**Chris Gammell:** Where it's like when you try and add a new piece of hardware, then it's like you're trying to bolt that on because it's intelligence is actually just really customized for whatever setup you had.

**Piotr Ezdintensky:** Yeah. Yeah. Yeah. Correctly. And it is all C code. So besides the generated stuff, there's like also layers of code generation that are happening, but we are trying to keep it simple enough that you can understand what is actually going on in the system. That's great. It has a steeper learning curve than something that is just one directory with a few files, but you pay always a price for flexibility and capability with complexity. So we are trying to walk this fine line of where it makes sense.

**Chris Gammell:** Right. Yeah. So how does it actually work then? Is it a real-time operating system or is it just a super loop?

**Piotr Ezdintensky:** So, yeah. So that's a great question because there is a complicated answer for that. Let me guess.

**Chris Gammell:** Wait, wait, wait. You invented something new that's halfway between those two things. We support both. Oh, that's even worse.

**Piotr Ezdintensky:** So what happened is originally it was basically prioritized like task switcher, something similar to what you had on the Apollo missions where you had tasks that there is a timer that is running at a certain frequency. Let's say 512 hertz because it's easy to divide them. But anyways, so then you have that and this is calling a main function that is calling tasks one after another that are based on their priority. And if the time runs out, the other tasks don't get executed.

**Chris Gammell:** Got it.

**Piotr Ezdintensky:** It's very robust and very easy to understand. So the only really big disadvantage is that if you have an estimator, estimator meaning you take sensor data and you want to calculate the attitude or position of the aircraft and that attitude estimator takes longer than one cycle, we cannot divide it. We cannot divide it out. You would need preemption for this.

**Chris Gammell:** Can you explain what that means?

**Piotr Ezdintensky:** So it means while you're running the algorithm that is calculating the attitude. So you have a magnetometer and you have gyroscopes, you have accelerometers. So you take all that sensor data in and based on that sensor data, you are trying to figure out am I level? Am I like tilted 45 degrees or what's going on with me in the real world? So for that, you use an estimator. And there are many different calculations that you can do. One of them is just complementary filters that are very easy to calculate. And then you can go into extended Kalman filters that are very complicated.

**Chris Gammell:** Right. And probably as the complication goes up, the number of crunching you have to do. Yeah, exactly. It's crazy.

**Piotr Ezdintensky:** Yeah. And then you have like quaternion based extended Kalman filter with 12 states. And then suddenly this takes longer than one 500th of a second.

**Chris Gammell:** Right. Right. Exactly. Right. All of the cycles get to go towards that thing, huh?

**Piotr Ezdintensky:** Yeah. Yeah. Yeah. Yeah. That's well, that's these kinds of things also ask for more powerful processors eventually. And if you start adding vision, things really go nuts. Right. So let's say we want to do such a calculation and we still want to run our control loop that is telling either the servos of the aircraft or the motors on a quadrocopter to adjust fast. And you still want to run that loop fast. And it is not, depending on the situation, you sometimes don't have to calculate the altitude every cycle, but you would want to distribute it between the cycles that you adjust your actuators. That's the word. That's what I was looking for. Gotcha. Okay. And when that happens, you need to basically interrupt the calculation, run this task that is setting the actuators and then come back to calculating your attitude.

**Chris Gammell:** And why do you need to interrupt for that?

**Piotr Ezdintensky:** Because it takes longer than the one 500th of a second.

**Chris Gammell:** Oh, I see. Okay. Okay. So, and that's just because mechanically it takes a while to actually turn a servo to its new position or what?

**Piotr Ezdintensky:** For example, there are many reasons you might want to like do a feed forward control and you want to adjust it like smoothly into the future or something like that. Okay.

**Chris Gammell:** So, it's just balancing the chunks of time that you have allotted and you never try and squeeze more than one task into that one 512th of a second, right?

**Piotr Ezdintensky:** Yes, that's correct. And then this is where an RTOS is very useful to have.

**Chris Gammell:** Okay. Because it doesn't wait for the one 512th. It just goes to the next thing.

**Piotr Ezdintensky:** Yeah, yeah. It can then interrupt the task that is running at the moment with a higher priority task that would be the actuator task. And yeah, and the estimator task would just be interrupted. And that's why eventually there is an option for using GBOS instead. Oh, I have another idea. It's like one other thing that also got added was, for example, logging to an SD card. This can take forever. Okay, just to write all the data. Yeah, SD cards are very unpredictable. Got it. So, yeah, that's a simpler example, actually.

**Chris Gammell:** Yeah, right. Just because it's a number of bits you might have to write or whatever, right? It just takes longer than...

**Piotr Ezdintensky:** Yeah, it is also buffering, and if you have flash, flash is unpredictable how long it will take because they have, like, load balancing stuff inside the SD cards. Yep, yep. So, we're leveling. So, especially if you have a FAT file system, that can take also time when you have to rewrite the FAT table or something. I've seen really weird stuff happening where the whole SD card is just freezing for 200 milliseconds because it's thinking.

**Chris Gammell:** Too smart, huh? It's too smart. Yeah, yeah, yeah. So, okay. So, you guys write either... So, you have these two different flavors of controlling the system. But how do you actually then... So, okay, I come in and I say, I want to use Paparazzi UAV, and I buy one of your boards, and I have... And I want to, like, then integrate a new sensor into it. What's the steps then?

**Piotr Ezdintensky:** That depends if the sensor is already supported or not.

**Chris Gammell:** Let's assume not.

**Piotr Ezdintensky:** Let's assume not. Yeah, so usually that also brings the next question is the peripheral that you're using to attach the sensor with supported yet. Got it.

**Chris Gammell:** So, like if it's on CAN bus or SPY or whatever, right?

**Piotr Ezdintensky:** Yeah. If it is on SPY or CAN, then we have already the hardware abstraction layer for it. Or if you're using chibi OS, you can use the how from there. Okay. And then you just write your C file and hook it in with another task, basically. Or, like, you hook it into this, like, repetitive loop, either with updates or you write an interrupt handler for it. And you add it to the collection of drivers. And then you go into the XML file, add it, please include my new shiny thing. Right. And it is added.

**Chris Gammell:** So, like most other systems, it's easier just to buy a pre-finished module and just plug it in, huh?

**Piotr Ezdintensky:** Yeah, no, that's pretty much. This is, you saying that, that makes me chuckle because I ran many times into the situation where I was, oh, I need to show a GPS position from the, like, ship that I'm sitting on, for example. Uh-huh. And I was like, oh, now I have to write a module that is a plug-in paparazzi. Then I just grepped for it and it turned out someone already wrote one.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** That happened to me so many times.

**Chris Gammell:** That's great. Because the code base is so vast. Yeah, a big community especially, right? Yeah. Yeah. Yeah. That's awesome. And then what, you went out and just, did you, so what is the actual physical interface then? Is it like, I'm looking at a picture of what I think one is one, autopilot Chimera?

**Piotr Ezdintensky:** Oh, Chimera, that's the new thing. Yeah. That's the guys in Etenac have done. Yeah. The autopilots that I made is the Lisa M and Lisa NX as well as the Lisa S. Okay. So, yeah, their autopilot basically is based on their requirements for include everything. That's why it's called Chimera.

**Chris Gammell:** Got it.

**Piotr Ezdintensky:** It has SD cards and STM32F7 and tons of connections and tons of interfaces.

**Chris Gammell:** UARTs, SPYs, I2C.

**Piotr Ezdintensky:** Yeah, so it basically should cover everything. And also because it's made by the university for the university, price doesn't matter for them.

**Chris Gammell:** Uh-huh.

**Piotr Ezdintensky:** In a sense, in quotes, because they're making their own hardware and it has to basically cover all the bases. Got it. If I tried to make an autopilot that does everything, it would be very difficult to provide it for any reasonable price.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** Right.

**Chris Gammell:** Just you mean with margins and everything too. They might not be trying to make a ton of margin to cover their...

**Piotr Ezdintensky:** Yeah. There is a reseller in France that is making them as far as I know. But they have some local just a relationship with them, which is great.

**Chris Gammell:** Cool. So, but most of the time it's like a standard pinout header kind of thing or how does that work?

**Piotr Ezdintensky:** So, for example, the Lisa M, it has a bunch of Molex picoblade connectors. This is something we standardized to use for like a very long time. And then for the servos, it has the standard three pin connectors that you have for RC modeling.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** And then it has also a USB interface where you can plug in a cable to either upload a new firmware or get the telemetry out. But where usually it's... Most people actually have a Blackmagic probe, for example, to program this thing over the JTEC interface.

**Chris Gammell:** Got it. Oh, yeah. And I just found the... There's a big wiki page around the Lisa M. So, I just finally found that. I see what you're talking about. So, these kind of like beige looking connectors are the standardized ones you're talking about?

**Piotr Ezdintensky:** Yeah, yeah, yeah. Okay. So, yeah, this is picoblade. It's a Molex connector.

**Chris Gammell:** Yeah, I mean, this is a really... Wow, that chip set on there is tiny. Is it the chip on the back? The chip must be on the back, right?

**Piotr Ezdintensky:** The chip is on the back and the IMU is on the back. In the past, we had the IMU on a separate daughter board. I changed that recently, five years ago. Oh, I see.

**Chris Gammell:** Time flies. Time flies.

**Piotr Ezdintensky:** Yeah, time flies. No, it was like, I think, three or four years ago where I integrated the IMU. Because originally when I made it in around 2009, the early Lisa M's, the GPS... Oh, not GPS. The IMU was on a daughter board so I could re-spin the board more often while we are finding new sensors and better sensors and without having to update the whole board.

**Chris Gammell:** So, this looks like it's... I mean, is it space constrained because of weight or why is it such a tight build as well?

**Piotr Ezdintensky:** Oh, it's mostly weight, yeah. Okay. It's weight and also size. So, you see the Lisa M is like lengthy shaped. Yeah, yeah. The reason is so that it fits in small foam airplane cockpits.

**Chris Gammell:** Oh, okay, okay. So, like, not just quadcopters but also... Yeah.

**Piotr Ezdintensky:** Yeah, Apparazzi grew out of the airplane UAV field. So, that was the stuff that it supported first. Got it. So, if you start using the ground station, there is still some references that are a little bit odd for a quadrocopter because they are terminology that is useful for airplanes. It still applies for quadrocopters but it is the other projects. Very often they created their own lingo, I would say. Got it. And this is based on the airplane terminology. Mm-hmm.

**Chris Gammell:** And this is the F105 family, STM32, F105. What made you choose that?

**Piotr Ezdintensky:** That was an F105. Yeah. So, Lisa M was F105. Lisa M is an F4.

**Chris Gammell:** What makes you choose one or the other? I mean, is there memory size, processing power, is it peripherals? All the above.

**Piotr Ezdintensky:** When I designed the F1 in, there was no F4s.

**Chris Gammell:** Oh, that'll do it.

**Piotr Ezdintensky:** Yeah. So, that was before... Roughly around that time, they started expanding into the F2. Mm-hmm. F2 is also still a Cortex-M3. Like, this is all weird. ST is an interesting company, how they are naming their products. It's a little bit misleading. So, they have this lineup of STM32, F, and then a number. And the F1 is actually a Cortex-M4 core.

**Chris Gammell:** Oh, really? I didn't know that. Okay.

**Piotr Ezdintensky:** No, Cortex-M3, I'm so sorry. Cortex-M3 core. And then the F4 is a Cortex-M4 core, which makes sense. Mm-hmm. But then you have the F3. It's also a Cortex-M4 core.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** And then F2 is Cortex-M3 core. Right. It's a little bit weird. But if you look at the list...

**Chris Gammell:** It felt like they were kind of just doing it by generations, almost. Like, I've used the F0, which is an M0 family, and that works out. But then the F1 is next. M3, F2, M3, F3, M4. Yeah, you're right. It sucks. Yeah.

**Piotr Ezdintensky:** But... But yeah. Sometimes it aligns, sometimes it doesn't.

**Chris Gammell:** Okay. Well, this is... I mean, it seems like this got a ton of stuff on here. How much... Like, how do you track adoption? How do you know where this is? I mean, I guess you're selling these boards, so that helps, huh? Yeah.

**Piotr Ezdintensky:** Yeah. Yeah. It's difficult to say. So, Lisa M was going up and down, and the whole UAV stuff. It's interesting that we ended up talking mostly about the UAV autopilot, because I'm still doing it quite a lot, and it's great. And especially the Lisa S, that is really, really tiny, is doing very well, and people really like it, because it's a 20 by 20 millimeter board. Yeah. This is very tiny. And it has GPS built in, and it has all the sensors you need for autonomous flight. And then it has, like, a tiny daughter board for all the RC remote control stuff and telemetry. Yeah. I hear you searching for it.

**Chris Gammell:** No, no, I'm just typing. I'm just making sure I keep notes on this stuff, because... But, yeah, this is crazy tiny on it. And so, it's just using a GPS module in the back. But so, how does this work, then, with just the... So, this one has just edge connectors, it looks like. These aren't... Are these actual connectors on there, or is it... They look like point one.

**Piotr Ezdintensky:** So, originally, when I was designing it, I was actually thinking about putting just pads on there. So, you solder it in. Yeah. But to make things a little bit easier for... To make it easier for a broader audience to use, the 0.05-inch pitch connectors are already paining their ass enough. So, yeah, I added some breakout boards. So, you have connectors for, like, a brushed quadrocopter, for example. There's, like, a special breakout board for this. Got it. So, you can just plug it in. It's not... It's trading off weight versus ease of use. And that's why the Lisa S, if you look at the board, the tabs around it are perforated. So, you can break them off in case you want to save a few grams more. Got it. Like, milligrams, actually.

**Chris Gammell:** Yeah. Yeah. Yeah, these are... I mean, this is already pretty small and lightweight. So, I mean, I guess they're just... People are really, really trying to optimize this stuff.

**Piotr Ezdintensky:** Yeah, yeah. It's used on a flapping wing, really tiny, like, flapping wing aircraft sometimes. So, really, a milligram counts there.

**Chris Gammell:** Yeah. That's crazy. Well, so, you mentioned... I mean, you mentioned the Blackmagic probe. And I saw the header that looked familiar on the Lisa M, right? Mm-hmm. That 5-pin or 10-pin JTAG that you put on there. But why don't we transition into talking about that? I mean, so, that's the main way that... That's where... Is this where the project grew out of? People probably have heard us talking about the Blackmagic on here in the past. But is this what it grew out of? And then, kind of, what is it?

**Piotr Ezdintensky:** So, in a sense, yeah. So, just before I moved to the US, I was working at the robotics lab at TU Munich. And while I was there... So, I was actually hired to write Common Lisp for them. But... So, I was doing mostly software stuff. But... I did.

**Chris Gammell:** I was listening to your... So, well, you were on Embedded back in December. And you mentioned that as your favorite programming language, too. Which is weird. And... But...

**Piotr Ezdintensky:** It's not weird if you realize how amazing it is. Right.

**Chris Gammell:** Okay. Well, we'll leave that conversation for Embedded. That seems like... Yeah.

**Piotr Ezdintensky:** Yeah, no. So, basically, I was already very interested in hardware back then. And... At the lab, we were building our own robots. And one of the researchers was looking for a hardware that he could use to read out mouse sensors that he could embed into the fingers of the robot. So that they can do vision recognition of the surfaces.

**Chris Gammell:** Oh, wow. Okay.

**Piotr Ezdintensky:** So, I designed a board that could connect to those sensors. And I designed an STM32 board to connect with it. And we needed a JTEC programmer. So I designed Floss JTEC. That was basically an FTDI chip on a board.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** And that board had already the form factor that is now... When you look at the Blackmagic probe, that's the same form factor. But...

**Piotr Ezdintensky:** After doing this, I was still interested in all stuff JTEC and debugging and programming our microcontrollers. And also, while doing all that, I was not very happy with the licensing that ST had for their programming libraries. So, with a friend of mine, with Uwe Hermann, we started the project called LibOpenCM3. Okay.

**Chris Gammell:** Okay. Okay. Okay.

**Piotr Ezdintensky:** And, again, through that project, Gareth McMullen, who also was scratching his own itch, namely, that OpenOCD was not... Like, it was difficult for him to use because it couldn't detect the target itself. You had to dig through config files and then have the man in the middle and so on and so forth. And so on and so forth. And he decided, let me see how hard it would be to implement a JTEC debugger that has a GDB interface directly built in. And so he started writing that software and realized, oh, the specifications are all out there. It's not that complicated. Let me implement that. And he somehow decided to use LibOpenCM3 for it.

**Chris Gammell:** Ah, interesting.

**Piotr Ezdintensky:** And he contacted me and was, oh, you guys don't have a USB stack yet. Here, take this.

**Chris Gammell:** That's a good way to make friends, I think. Yeah. Well, before we keep going into that, though, can you kind of break down why some of this stuff was tough in the past, right? So I felt the OpenOCD and GDB stuff, the pain of that in the past. But maybe, you know, like what was so painful that made you guys jump into this as well instead of using an existing solution? I know you said licensing, but...

**Piotr Ezdintensky:** So LibOpenCM3, it's basically low-level hardware library. So the ST stuff was licensed in a way where it was not compatible with open source projects. They improved things, as far as I know. So the headers are actually more of a BSD license type of thing these days. But when you start browsing through their libraries, you still find some junk where it says, you must not use this header file that is specific to our peripherals on someone else's hardware, which is quite silly, too, because it's their specific hardware. Right. But this clause of being discriminatory, quote unquote, is incompatible with open source licenses. Right. Just blanket statement here. And so this was a very sticking point for us. Also, we were finding a bunch of bugs in their libraries. And there was no good way. And still, as far as I know, I'm hoping that maybe someone who is listening to the podcast will tell me that I'm wrong. That there's no good way of contributing changes and fixes to the ST libraries back. Right. It's not like a Git repository where you can send a pull request and say, look, here is a back. I fixed it.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** So all that put together, we were both of us, Uwe and I grew up writing and using open source software. So we were used to the way how to interact with the software we are using by being able to contribute back to it, to modify it, to fix it when we need to, need to make sure that it works. And that's why that was out of all those reasons we decided to venture into this massive project of writing a low-level hardware library, which is very silly when you think about it. But we felt that this would be useful. I thought we were writing it for ourselves.

**Chris Gammell:** Right. Right. Of course.

**Piotr Ezdintensky:** Right. But then, to our big surprise, people started coming in and contributing and using it and liking it.

**Chris Gammell:** And just to be clear, this is for STM parts specifically, right?

**Piotr Ezdintensky:** It used to be. By now, it's not anymore. Oh, interesting. Okay. So it started out as actually LibOpenSTM. So that changed. We changed the name of the project already once. That's why it is called LibOpenCM3, which should probably be called now LibOpenCortex or something like that. Right. Because now we support all the different vendor. Oh, CM3.

**Chris Gammell:** I just got it. CM3 is Cortex-M3. Yeah.

**Piotr Ezdintensky:** Yeah.

**Chris Gammell:** Got it.

**Piotr Ezdintensky:** So we have support for a lot of Cortex-based chips. And we don't have Cortex-A stuff as far as I know yet, but a lot of Cortex-M stuff.

**Chris Gammell:** And so when you say low-level, what are you actually implementing? You are abstracting out pieces like hardware registers and stuff like that? Yeah.

**Piotr Ezdintensky:** Yeah. That's basically half of it is. So there are several corner cases. So in essence, it is a lot of header files that have defines that define where in memory are the memory-mived IO registers to configure the hardware.

**Chris Gammell:** Right. So you want to find the spy port on the F105 or whatever it is, the SD32F105.

**Piotr Ezdintensky:** Yeah, it is a set address like 0x4000200 or something. Right.

**Chris Gammell:** And that is what – yeah, you're right. A lot of the vendors will give you that stuff sometimes. Well, usually. Yeah. Yeah. They should.

**Piotr Ezdintensky:** They usually also do or generate it or you can buy it or whatever. And the problem with SD at that time was that these headers had like a weird license. Got it. Got it. So the other thing that it does, it has the initialization code. So basically the vector table definition and the startup code that you need to get the chip up and running.

**Chris Gammell:** Okay. So that's like – is that the stuff that's usually written in assembly and stuff like that?

**Piotr Ezdintensky:** Yeah, that's – yeah.

**Chris Gammell:** Like the bootstrapping and all that stuff?

**Piotr Ezdintensky:** Yeah, yeah. That's usually in assembly. We wrote everything in C because we could. Oh, cool. It was – it's basically the arm – the more modern arm chips. They are nice in that respect that you can actually write that stuff in C. Yeah. So you don't have any assembly there.

**Chris Gammell:** My experience with that is – well, not writing it, but looking at it at least. And it was all for all the older freescale stuff, the Coldfire family. Coldfire.

**Piotr Ezdintensky:** I am not familiar enough with that family, but I know that in the past you needed some specific assembly instructions to get a chip. Right.

**Chris Gammell:** You're trying to like go to the beginning of the memory map or go to this address or whatever. Like jump here, jump there, do this thing, push this there, that kind of stuff, right?

**Piotr Ezdintensky:** Yeah. Or call specific instructions that are initializing the vector table and enabling the interrupts and doing the stuff like that.

**Chris Gammell:** Right, right, right, right. Yeah. Yeah. Yeah. And flipping all the switches.

**Piotr Ezdintensky:** Yeah, exactly. And the third part of LipOvenCM is like a thin layer of beautification, I would call it. It's convenience functions, how we call it.

**Chris Gammell:** Okay. Macros or like actual functions?

**Piotr Ezdintensky:** No, actual functions, actual code that are not – so instead of twiddling bits in registers, you can call those functions to do the same thing.

**Chris Gammell:** How about a simple example?

**Piotr Ezdintensky:** So GPIO set then brackets GPIO a bank and GPIO 13 for the pin instead of writing – Right.

**Chris Gammell:** And or whatever or the – Or – Oring in a mask or something like that. Correct. Yes. Yeah, like – sorry. Yeah.

**Piotr Ezdintensky:** Yeah, no, that's exactly right. Yeah. So instead of doing bit operations and shifting the bit to the right position and setting it into the register, you can just call a function with two parameters. It's the bank and the GPIO pin and then it will set it or reset it or toggle it.

**Chris Gammell:** And that kind of thing actually doesn't – at the end of the day, that takes up more code space, but it doesn't actually – when it actually compiles down, it kind of goes away, right? I mean, like it's – Yeah. If you're using that kind of thing, it just – the compiler figures out, oh, you're trying to do this other operation that happened anyways.

**Piotr Ezdintensky:** Yeah, today's C compilers are pretty smart. And I'm running less and less into people that say that I can write more efficient assembly than the C compiler can generate, which is true. You have to be – there is still situations where you want to write assembly, for example, to do the SIMD instructions in – so single instruction, multiple data stuff. You still, in many cases, want to write it by hand because there are not really good triggers from C to do that. But this is a very specific application and very specific situations. A friend of mine who you met, Jared Boone.

**Chris Gammell:** Oh, yeah.

**Piotr Ezdintensky:** Yeah. He is writing his radio filters with SIMD instructions to accelerate them. Got it.

**Chris Gammell:** Yeah, I think the main thing that – again, I don't do this often, but the people that I've observed, it's like you at least need to be able to look at the generated assembly after the compiler goes through and then be like, okay, that looks right enough, right? So it's like recognizing when it's doing something really dumb and then fixing it and not letting it balloon out your code before you don't – Yeah.

**Piotr Ezdintensky:** Another thing to say is early optimization is the root of all evil. Right. And so if you write something in C or some other language, even if it is not very efficient, but you can write that code quickly and get to a certain spot faster that way. That works enough. And then realize – yeah, that works enough. And then realize where the issues are and bottlenecks and start addressing those. You still probably will end up with the result you are looking for faster, hopefully. And it is almost most definitely easier to maintain than a lot of assembly code.

**Chris Gammell:** Yeah, exactly. I kind of think of it the difference between like prototype and production, right? At prototype stage, you should be not necessarily slapping stuff together, but you should be getting stuff working and then refining that. But then if it's in production and you need it to be like cheap and you need it to be fast and you need it to be super efficient, that's when you spend the time actually rejigging all the code in order to get that stuff.

**Piotr Ezdintensky:** Yeah, exactly. Exactly right. Yeah. So you build a quick prototype. You figure out if it is even feasible what you are trying to do and then start optimizing.

**Chris Gammell:** Got it. Okay. So you met Gareth.

**Piotr Ezdintensky:** We went off on a tangent there.

**Chris Gammell:** No, no, that's good. No, that's good. You met Gareth and he was working on this OpenOCD GDB stuff. I actually met – you had luckily had mentioned to Gareth that he should show up at the Auckland meetup. So I got to meet him as well. And I was like, oh, okay. Well, hello. That was great. Hello to all the Aucklanders, Aucklandites. But what is – so why is it better to use like the libopencm3 versus – it was just because it was faster and accessible? Is that kind of the thing or because it wanted to be open or what?

**Piotr Ezdintensky:** He wanted it to be open. He designed it from beginning to be open source because he sees it as a tool for himself. And that's how we continue seeing it and that it is a tool that we were using. That's why I started using it for all the autopilot stuff myself and then stopped making the Floss JTAG. Okay. Because it was better. It was easier to use. You just plug it in. You don't have to every few months send another patch that will take weeks to get incorporated into OpenOCD. And it just worked. That was the amazing part. Gareth did such an amazing job with his tool that I was amazed how easy to just plug it in and do your thing that you actually want to do, namely debug the thing that is not working.

**Chris Gammell:** Right, right.

**Piotr Ezdintensky:** Instead of fixing the tool to debug it with.

**Chris Gammell:** Right. Which is what happens with OpenOCD a lot. Unfortunately. Yeah. It says, what kind of error is it throwing? Oh, yeah. You need to just like reinstall the full thing again. You'll be fine.

**Piotr Ezdintensky:** But I have to moderate my statement about this a little bit. OpenOCD is amazing regarding the fact how much different hardware it supports.

**Chris Gammell:** Oh, interesting.

**Piotr Ezdintensky:** It's a huge, huge accomplishment of that project that it supports so many probes, so many targets. And it's a vast repository of knowledge that is assembled in there. So I don't want to be too harsh on OpenOCD because they have their place. They are doing an amazing job. And but for...

**Chris Gammell:** I can complain about KiCat and yet still like, I mean, I'm worthless without it. So like, yeah, it still helps me every single day. So yeah, that's fine. Yeah. I just wanted to mention that. Got it. Yeah. You're so ungrateful, man. What up? What up with that?

**Piotr Ezdintensky:** Yeah. Yeah. So we are learning from them too. And yeah. So OpenOCD has its place and it's doing a great job. But if I have the choice between using OpenOCD or Blackmagic Probe, if Blackmagic Probe supports that specific tool, then I will go for Blackmagic Probe because I will plug it in, plug it into my computer. And I will just show two generic serial ports. I start GDB or some other tool that has GDB built in, the GNU debugger from the open source tool chain. And so just to clarify and go into GDB, say target extended remote, the first serial port and I'm in.

**Chris Gammell:** Oh, wow. Okay.

**Piotr Ezdintensky:** That ain't bad. And also because these are generic serial ports, it works on pretty much everything. Right. And you go to a comp and also the tool chains for ARM, they are available on a lot. So thanks to the ARM company that they got a few developers to work on a genuine bare metal tool chain to release. It's the GCC ARM embedded. And because I was maintaining my own tool chain before that too. So thank God I don't have to do that part anymore. Yeah.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** But...

**Chris Gammell:** Okay. So let's take one step back again. Sure, sure. So first off, OneBitsy versus Blackmagic Probe, they are different things. You saw both of them, obviously. What is the main difference?

**Piotr Ezdintensky:** Oh, so Blackmagic Probe is a tool to... Basically, it's a brain tap into the CPU and the OneBitsy is an evaluation board. It's like a board that has the CPU on it, all the peripherals that you need to get it running. And then you can build and prototype your project around it. It's basically like an Arduino with JTAC interface exposed.

**Chris Gammell:** Got it.

**Piotr Ezdintensky:** Okay. And it is meant to run very well together with the Blackmagic Probe. That is the debugger part of it.

**Chris Gammell:** Got it.

**Piotr Ezdintensky:** So this was also a conscious decision to not integrate Blackmagic Probe into the OneBitsy because a lot of the dev boards have their debugger on board. Yeah.

**Chris Gammell:** It has like a separate chipset or something where it's like flowing through that, right?

**Piotr Ezdintensky:** Yeah, that's right. And the problem, I wanted to do it differently than others for a reason because I think a good debugger needs a certain amount of parts on it, making the bill of materials higher than you would want.

**Chris Gammell:** Pay more so you're not dragging that bomb cost with you to every new project, right? Yes. Yes.

**Piotr Ezdintensky:** You are basically with every new project you are buying another JTAC debugger. Right. That is mediocre or good. Right.

**Speaker ?:** Whatever.

**Piotr Ezdintensky:** It does the job.

**Chris Gammell:** That's like on the discovery board, right? So it has two STM32 F0 family parts on there, right? One is the programmer debugger. The other one is the actual target chip. And it's fine and it's cheap, but I think the part that's doing the debugging is not very powerful. That's the thing. It's not doing a lot.

**Piotr Ezdintensky:** Yeah. Yeah, no, that's correct. And so even on the discovery boards, this is just to mention, the people did port Blackmagic probe firmware to the discovery board ST link chip.

**Chris Gammell:** Oh, interesting. Okay.

**Piotr Ezdintensky:** So if you are using the open source tools like GCC and GDB and use make files, command line or whatever, you might want to reflash your ST link on your discovery board with the Blackmagic probe firmware.

**Chris Gammell:** That's interesting. Okay. Yeah, that's great. And that's a great, I mean, like, I mean, I think that the stuff that you guys have is very affordable. But if you wanted to do it for like 10 bucks too, to try it out, that's a really cheap way to try it out.

**Piotr Ezdintensky:** Yeah. You can also buy an ST link to clone from China and flash Blackmagic probe on that one too.

**Chris Gammell:** If you want to. So it's even less risk to flash. Yeah.

**Piotr Ezdintensky:** Yeah. You can try it out and see if you like it. But just to make clear, the Blackmagic probes, besides having certain hardware, I can tell you what that is. But the nice thing about the Blackmagic probe and us selling it through OneBitSquared is that it is financing a lot of the further development of the project.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** So people were asking me a few times or even criticizing that we are selling the Blackmagic probe for $60 for the hardware.

**Chris Gammell:** Right. And then you sent them to all the vendor pages and you're like, yeah, okay, well, it's not $10,000 or $5,000. So how about you shut the hell up? You do that, right? That's what you told them? You're like...

**Piotr Ezdintensky:** No, I'm trying to be nicer than that. But yeah.

**Chris Gammell:** I wouldn't take no gruff.

**Piotr Ezdintensky:** Yeah. So the main thing is, it seems that a lot of people think that if something is open source, it means it should be free. And that no one spent any time developing it. Right. And no one is spending time maintaining it. And we are doing it at night just for the fun of it because we love doing it.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** In a sense, it's true. But on the other hand, I would like to...

**Chris Gammell:** You are working at night. You do enjoy it.

**Piotr Ezdintensky:** But you also like food. I also like food. I like having a roof over my head. Yeah. I like having internet connection. Right. So...

**Chris Gammell:** See, I think that people ignore that too. Like, they'll be like, ah, whatever. That's on you, man. But I think it's like, if you do that comparison cost of like, no, seriously, debuggers are expensive from the traditional vendors. It's like, oh, wow. This is like a 20th of the cost. That's crazy.

**Piotr Ezdintensky:** Yeah. No, that's correct. Also, because of the cost that includes some development costs in it, we can continue evolving and making it better over time.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** We are spending time writing software, writing more unit tests, making it more stable, more like better. We are working on new hardware for the future. It all costs a huge amount of money to prototype hardware.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** So... We know that one here. Yeah. So, yeah. So, we had... If you like Blackmagic Probe, you flashed it on your discovery board, just consider... It's like, if you really don't want to buy the hardware, that's fine. Maybe you donate some money on the website. That's great too. But buying the hardware, you get something for it. I think it is pretty decent. Hoping. And...

**Chris Gammell:** Well, like, maybe that's a good thing to compare too. So, like, okay. So, between flashing it onto like a discovery board, ST-Link chip, and then using the Blackmagic Probe, what do you gain from using the discrete hardware?

**Piotr Ezdintensky:** So, the discrete hardware, first of all, you can plug it into your project. That's one. But you could do that with the cheap ST-Link too. But what I did is I added dual supply transceivers on the front end. So, it allows translation of the signals down to 1.7 volts and up to 5 volts. Oh, that's nice. So, you can... It will work with more projects than just the 3.3 volt system of the discovery board. And you can use also low power targets that are this like STM32L zeros.

**Chris Gammell:** Oh, yeah. Right, right, right. Like the super sipping the power kind of project stuff.

**Piotr Ezdintensky:** Yeah, yeah. You can use that for this really low power, low voltage systems. Also, it has a bunch of additional LEDs so you know what is going on on it. It has a function where you can power the target. So, you go in GDB and you run monitor t-power enable and it will power your target using the power reference pin of the JTAG interface. And it has a built-in UART to serial. So, USB to serial adapter on the back of the board. So, it's actually more useful than one would think to have it in one package. So, you can just plug it in and have serial while you also have JTAG or SWD. We support both.

**Chris Gammell:** That's great.

**Piotr Ezdintensky:** Yeah. So, yeah. That's pretty much it. I might be forgetting something, but...

**Chris Gammell:** Well, let's talk through the actual process too. I mean, like so people who haven't done... So, I think the interesting thing for me is that a lot of people come from the world of Arduino, right? For better or worse, I think it's great that they start like stepping in it. They're like, all right, I want to make a more complex project. I need to peer into the processor like you're talking about. So, people that are just getting started from that step, what are they going to see when they start hooking up a Blackmagic probe? Like what are they peering into then? Okay.

**Piotr Ezdintensky:** Okay. So, the analogy I'm trying to make... So, if you have an Arduino project, you might run into some issue where you are not calculating the right thing and you don't know what is going on that is causing it. So, what you usually do, you add a print line somewhere or you blink an LED to measure or toggle a pin to connect to your oscilloscope or logic analyzer to try to figure out what this thing is doing. And this still is like tapping somewhere in the darkness, trying to realize what is going on inside the chip without actually seeing what the chip is doing. So, with the Blackmagic probe and you connect GDB to it, it will interrupt the program. So, stop it. Like basically stop the clock of the chip. And then you can step through it saying, please run one instruction more through the code and now tell me what is in this variable A, B, C, D. And then you run another step and you see how this variable starts changing or not. And then you see that, oh, my calculation was off by one.

**Chris Gammell:** Oh, right. It's zero reference, not one reference. So, whatever other mistake that I always make.

**Piotr Ezdintensky:** Yeah, exactly. Or just recently I was writing some sprite rendering stuff and I was incrementing a pointer to a list in the wrong direction. It was crashing.

**Chris Gammell:** Yep, yep.

**Piotr Ezdintensky:** So, basically if you have an embedded system, what happens? You blank screen, nothing is happening. Right. So, where do you start debugging this? It's like normally what I would do in the past is start adding printf and connecting a serial interface and seeing when do I see the printf? And then basically bisect the code half by half by half by half until you find the spot where it is crashing.

**Chris Gammell:** Yep, yep. That's good.

**Piotr Ezdintensky:** With the black magic probe, I just plugged it in. I started the code. GDB immediately jumped out, said sec fault. I ran backtrace and it said where it crashed.

**Chris Gammell:** Really?

**Piotr Ezdintensky:** Including the parameters to the function that I called and it took me, I don't know, a few minutes to figure out. Right. Versus a day and a half, right? Which is totally possible.

**Chris Gammell:** Oh, man. Yeah. People that are debugging. Hello, anyone who's listening while debugging. Hello. We feel your pain, man. We feel it. There's a black magic probe with your name on it. Mutually beneficial here. Yeah, that's great. So, why aren't people using these more already? I mean, not the black magic, but like why? Debuggers in general? Yeah, in general. I guess, I mean, is it just because of support or because of tool chains or what?

**Piotr Ezdintensky:** So, I'm being told, I'm asking that question quite often myself. And I think a lot of people, so if you came from software development area, you will be looking forward to having those tools because this is normal to have on a normal desktop to be able to debug and step through your code. It's nothing special. But in the Arduino world, I think a lot of people are not aware that this exists in software. And the AVR is, I'm being taught, well, I used AVR in the past and I wish it had proper debugging myself. But some people are saying, oh, it is so simple that it is pretty easy to debug it without it.

**Chris Gammell:** Well, that works until it doesn't, right?

**Piotr Ezdintensky:** Yeah, but I was running into day-long bonanzas of trying to figure out why something is crashing on AVR 2.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** So, I'm not really buying that argument, but this is the excuse that I hear.

**Chris Gammell:** Well, I think it's easier to keep doing what you're doing, right? That's probably one reason.

**Piotr Ezdintensky:** But staying with AVR in general, that's probably what is going on. I think a lot of people are being introduced to Arduino using the AVR. And they are just used in evil, you know. Right.

**Chris Gammell:** Well, yeah, we kind of talked about that earlier too, right? It's like I need to get to the point where it's the firmware that works, right? And the same thing happens with, you know, some hardware that just works.

**Piotr Ezdintensky:** Right.

**Chris Gammell:** Well, it's great until it doesn't, right?

**Piotr Ezdintensky:** Yeah, no, that's exactly right. And Arduino does a really good job to onboard people that have no technical background, which is awesome.

**Chris Gammell:** Yep, I agree.

**Piotr Ezdintensky:** We need more hardware developers. I think the more the merrier.

**Chris Gammell:** Yep, I agree. I'm trying to make more.

**Piotr Ezdintensky:** Yeah, that's exactly right. But I wish that world was a little bit more open to providing tools that are actually good.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** And so that people are not learning bad habits. And this is the perfect example is for anyone who grew up somewhere in the 80s or 90s is if you learned basic, you probably acquired some horrible, nasty habits. Go to 10. Go to 10. Go to 10. Yeah. Yeah. And anyone who I know who learned basic and then had to unlearn those would agree with me.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** And this is the same thing here. It's like you have the Arduino and you learn some habits. It's great because it's easy to start with. But if you actually then need to fix something, then you have to start digging. What I like to say about this is a lot of these platforms, and I'm not saying specifically Arduino, I think it is going through the whole embedded system stuff too, is they are trying to gloss over complexity in false indication of simplicity. So basically trying to make things look easy. Oh, use our product. It's so easy to use. Here, have an example. You flash it, it works.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** And then when you start actually trying to use it and make it into the thing that you envisioned, things become difficult. So the learning curve, embedded system learning curve is quite steep, in my opinion. And if you really want to learn how to use this stuff, you should try to understand how it works. And having all those abstraction layers that are hiding that complexity is making it even harder.

**Chris Gammell:** Right. Right. Right.

**Piotr Ezdintensky:** At least to me. But, yeah.

**Chris Gammell:** Well, I mean, but at a certain level, you stop as well because, like you said, you prettified some of that code. You make sure that it's not all super rough to do. But it's just a balance of, you know, how much do you abstract away and how much do you, you know, ask the people dive in and kind of understand what's going on underneath the hood, right?

**Piotr Ezdintensky:** Yeah. But the example is, for example, the SD libraries. The SD libraries, the stuff, how the functions are called, or even on the register level stuff, they are called differently than in the data sheet. And you're like, what are you people doing? How am I supposed to figure it out when something breaks?

**Chris Gammell:** Right. Yeah. And that's always the problem, especially when it's like bouncing you between 40 different, you know, reference file or source files and header files and everything. Right. And you're like, where is it defined?

**Speaker ?:** Yeah.

**Piotr Ezdintensky:** Or a stack of PDFs that are cross-referencing themselves. Right. That happens too.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** Fortunately, SD's data sheets are quite decent, I would say. They are not the worst. Seen worse.

**Chris Gammell:** I'm sure of all the things that people are going to, you know, leave in the comments section, there will be some very strong opinions about how sufficient the SD parts or the data sheets are. Oh, yeah. No, of course.

**Piotr Ezdintensky:** People hate the SD parts, people hate other parts too. Right. I am biased because I started with the SD parts. Right. I am aware of it and I know it. And I know that, for example, LPC has really wonderful peripherals. For example, the super flexible serial interface that it has is really awesome. But there is this activation energy barrier where you start a project and you are weighing your cost of switching to a new part and learning a new system versus the amount of time you want to spend on it. And I try to be aware of what features the alternatives have in case I have a project where I will realize I have to use that other part because it will save me a ton of time.

**Chris Gammell:** Yeah. Right. Exactly. And that's when you go learn it, which is always the wrong time to do it. But it's like you're going to do it anyways. Right. Yeah. Same thing with like learning debugging as a standalone skill. It's tough to do that when you should do it. When you should be doing it is before you're actually debugging. Most people learn it, learn it when they're like, oh, crap, I need to learn how to debug this thing right now.

**Piotr Ezdintensky:** Yeah. No. Yeah. Exactly. And you end up trying to learn how to use GDB the night before release of the thing you have to deliver or something. Oh, God. It's terrible. Right. Been there, done that.

**Chris Gammell:** Oh, man. That's funny. Yeah. Yeah. So I had two questions about this. One is, you're doing all your development with make files and command line and stuff like that? Yeah. Yeah. Okay. So the next question is, how do you usually suggest that people go and start with this stuff? So you were doing a class at DEF CON, but how else should people get to know the Blackmagic probe and actually using this in a real world situation?

**Piotr Ezdintensky:** That really depends on the person. I just had an apropos conversation today. Every person is learning in a different way. So it really depends on what type of learning one prefers. There are really good books that can be picked up about GCC, GDB stuff. So maybe let me rewind a little bit. So I am of the opinion that if you are actually interested in embedded systems and you want to learn this stuff, try to learn it from bottom up. So try to understand how the registers work, how this stuff works. That's a separate thing from learning how to program.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** You might want to learn how to do basic stuff in C or Python or stuff like that first, or even use Arduino to get going in programming. Right. But if you want to learn about embedded systems and actually become fast at what you're doing, you want to understand the tools bottom up. You don't have to get there then later. But if you know what is going on under the hood, it's much easier to reason about it when it is not doing what you think it should.

**Chris Gammell:** So do you mean, so what is the depth of understanding under the hood? So is it memory is a physical thing and you're actually flipping transistors, which represents bits, which represents that? Or is it like, I need to understand the data flow all the way through the processor?

**Piotr Ezdintensky:** Data flow through the processor. Interesting. I'm personally interested also in how the bits are being flipped or going even on silicon level. I think the RISC-V stuff is just, it's super exciting. The open source, the V5? The V5, yeah. Okay. What is the company called? Sci-5? Yeah. These guys are doing an amazing job of making it, like you can read the HDL code of it and actually dig into that. But it's a completely separate thing. Now there's a Saturday night, guys. Yeah. This is what you do to go to read before sleep.

**Chris Gammell:** Oh, yeah. Right. Exactly. Yeah.

**Piotr Ezdintensky:** Anyways, but for embedded programming, you want to understand how a machine works. In a sense.

**Chris Gammell:** And so, when should that happen, though? Like, again, in terms of sequence, you said learn Python first, learn some programming stuff, maybe even dive into the hardware, software barrier. Maybe with Rint, we know if you don't put too much of that.

**Piotr Ezdintensky:** Yeah. I don't think these days you really have to learn assembly immediately either. Okay. I don't think this is that far that you have to go with it. But understanding how the mechanics work, how interrupts are being triggered.

**Chris Gammell:** Oh, that's interesting. Yeah.

**Piotr Ezdintensky:** How.

**Chris Gammell:** Because it's actually bouncing out. It's like doing it. So, an interrupt is a physical thing, but then it also moves to a different memory location, all that kind of stuff. Yeah.

**Piotr Ezdintensky:** Or using a separate set of registers, depending on the architecture you're using. Sure.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** Having some understanding of that will save you a lot of headaches later on. Because if you don't, then you will have to learn it eventually because you will run into those issues.

**Chris Gammell:** I'm 33. I will not have to. I should, but I don't think I'll have to. Maybe.

**Piotr Ezdintensky:** It depends on what level of development you are working on, too. And also.

**Chris Gammell:** If you want to write anything fast, how about that? If you want to write anything fast or good or reliable, probably, yeah.

**Piotr Ezdintensky:** Yeah. So, going from there, so going on that end of things, you want to go from A to B faster. What I usually do is go on the OneBitC website. So, let's put it in the framework of this stuff that I'm using. So, take a OneBitC, go on the OneBitC website. There is a GitHub repository that you can just clone that contains a ton of examples. Just take those examples and start modifying them. That's how I, I think, learned how to program in the first place is using other people's code and modifying it.

**Chris Gammell:** So, you're saying, like, take a OneBitC, which is the hardware. Mm-hmm. Clone this thing. Get it built up. And then actually plug in. So, like, I'm looking at the repository. It looks like there's a LCD driver, right? Right. So, hook up a driver with the pins where they're supposed to be and then go drive that LCD with this code, you're saying, and make it actually hello world to the display.

**Piotr Ezdintensky:** So, in the OneBitC-examples repository, if you go in there, there are, like, how to send data over UART, how to use SPI, how to blink an LED, how to read out a button, how to send data over USB. It's like, for example, USB. You could go start understanding the whole protocol and the whole stack. You don't really have to do that.

**Chris Gammell:** No, no, I'm not going to do that.

**Piotr Ezdintensky:** That's not what I was trying to say with the bottom-up approach. Right. It's more on the level of learn at least the part, how do you toggle a GPIO. Oh, okay. Now I understand roughly how this, like, interaction of the gears looks like. It will be in some similar way also with USB with much more code and much more complicated than this.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** So, okay.

**Chris Gammell:** And, yeah, so looking at your readme on this example thing, too, you're also showing, like, how do you build this thing, right? How do you get all the necessary includes in there, right? So, you've got all that stuff in there. And you're saying that, so this almost reminds me of, like, so to use an analogy, this almost feels like people who are using Arduino, they go and click on the examples tab, and then they go and select some sketch that exists already, and they go change the blink frequency, right? Yeah, of course. In this case, you're doing the same thing, but you're actually just building the project with the make files and all that other stuff, and then, again, blinking the LED at maybe a different frequency.

**Piotr Ezdintensky:** The biggest difference is that instead of using the Arduino IDE, you use your own text editor that you like or hate.

**Chris Gammell:** Right.

**Piotr Ezdintensky:** So, that's the biggest difference there. It's you, and you go on the command line to run the commands. Yeah. There is, I know for a fact that this stuff also works with Eclipse, and the problem is I'm not a Windows user or an Eclipse lover. A UI user? So, I'm a little bit dragging my feet on documenting how to do that. I'm aware of that. I have been screamed at enough already about this.

**Chris Gammell:** Okay. So, please don't leave the comments in the comment section on the amp hour. Please. We'll give you an email address that you can, at the end of the show, you can email.

**Piotr Ezdintensky:** So, I'm actually looking forward to someone who really uses that stuff to step up and join the project and maintain that documentation, because I know these things are changing over time.

**Chris Gammell:** Yeah. So, we were doing that. So, for contextual electronics, we did some Eclipse stuff, and the embedded guys that were working with me did a really good job, I thought. But it was like, even within the amount of time when we started and finished, Eclipse changed enough that the menu options all changed and all that other stuff. And it's so dependent on...

**Piotr Ezdintensky:** All the screenshots you made for which menu to go to will be outdated within a few months. Exactly.

**Chris Gammell:** And it's like, I think building from the command line is its own skill. And yes, it is confusing, I think, at first. But, you know, especially people that aren't... Well, obviously, Dave isn't here, but he's not a big Unix-based building and stuff. Anyone could follow directions, but it's just confusing, right? You see, like, make. What does it even mean, right? It's like, okay, I get it, but it took a while.

**Piotr Ezdintensky:** No, I understand that. But that's why I think IDEs have their place, too.

**Chris Gammell:** Yeah. Right, right, right.

**Piotr Ezdintensky:** So, that's why we also have preliminary platform I.O. support.

**Chris Gammell:** Oh, yeah. You were telling me about this at DEF CON, weren't you? I think you were really excited about this. Yeah, yeah. Someone was recently.

**Piotr Ezdintensky:** Yeah. So, platform I.O. is also actually a command line tool. But these guys created a set of plugins for the Atom text editor.

**Chris Gammell:** Yep.

**Piotr Ezdintensky:** And we wrote a board support file repository thingy to support OneBitC in platform I.O. Cool. So, that makes things a little bit easier because you have all the buttons and the shortcuts to run, make, just like in Eclipse. Yeah. And as far as I know, so, just until recently, there was no GDB debugging capability within the platform I.O. thing. But I think they added it not so long ago. Okay. We had, Gareth wrote actually a plugin for Atom to do GDB debugging with monitoring variables. This is where UI has. Oh, that's nice actually. Yeah. Yeah. This is where the UI has totally a place is being able to visualize the data.

**Chris Gammell:** Multiple windows. Yeah, exactly. You're seeing like, oh, like, variable one is set to 13 currently when I do a breakpoint or when I'm stepping through code. You just kind of watch the value change.

**Piotr Ezdintensky:** Yeah. Yeah. And there is a window that has all the watch variables. So, you run your code and you see the variables changing on the fly. And then you see all the breakpoints that you have set and so on and so forth. So, that's great. There is also some text interfaces for GDB that you can put on top of GDB that are really good, very powerful. There is also Radara 2 that we are working on getting support into to do live debugging. That's not fully finished, but we have a quite dedicated guy working on this. Then, also, Platform.io got support or has plugins for Visual Studio Code now. Okay. And yet, don't mistake it for Visual Studio. These are two different things.

**Chris Gammell:** Is this like how Windows or, sorry, Microsoft open source some of the stuff?

**Piotr Ezdintensky:** So, Visual Studio Code is basically a modern age text editor just like Sublime Text is or Atom is.

**Chris Gammell:** Oh, okay. So, like formatting around, I understand that this is a variable or this is a type or whatever, that kind of thing?

**Piotr Ezdintensky:** No, no. A text editor for files, for like programming and writing text files.

**Chris Gammell:** Right. But when I type import into, if it knows that it's a C file and I type import, it's like it calls that out with a different color or something. Oh, yeah. That's what I mean. Like that kind of stuff.

**Piotr Ezdintensky:** Yeah. This is the modern stuff and having plugins and having like a store basically to add plugins into your text editor. Right, right. That's, as far, I think this started earlier than that, but something that I used first that had that very strongly integrated was Sublime Text.

**Chris Gammell:** Yep. Yeah.

**Piotr Ezdintensky:** I really love Sublime. I still use it.

**Chris Gammell:** I'm taking notes on it right now. It always reminds me that I should still buy a license and I should.

**Piotr Ezdintensky:** I bought a license. Good, good. I can pat myself on the shoulder on that one.

**Chris Gammell:** I don't write that much code. I mostly keep notes in it.

**Piotr Ezdintensky:** Yeah, no, no. That's totally fine. And I think Sublime, this is the problem with Sublime. Why we focused on Atom was the fact that you need a license and that it has the nag screens and it's not completely open source. It would be a little bit hypocritical if we said, oh, this is the way to go. Still, I know that people are using Sublime with the whole setup that OneBitC has. So this is the nice thing. At OneBitC, you can program it in so many ways because it is just requiring the low-level command line stuff. And so you want to use the, what is the Windows Text Editor to program your code? TextEdit. TextEdit. Notepad. Notepad. You're welcome to. And so you can use almost the tools that you want. And I did hear that the Eclipse stuff, people are having sometimes trouble with it, but we will eventually have that too. And I know that it works because several people managed to set it up.

**Chris Gammell:** Okay. Oh, cool. At the end of the day, it's just talking. I mean, it's really just a pretty face on the same thing that's happening behind the scenes, right? Of doing new files, building, you know, calling these different functions or whatever's happening or scripts and then building up the stuff you need. Yeah, that's correct. Yeah. I had a question about the, so the actual physical thing that's happening as well. So when I started up GDB and it's talking to the Blackmagic probe and it's actually, you know, stepping through code, that's all happening through the JTAG interface? That's right?

**Piotr Ezdintensky:** Yes. Or SWD.

**Chris Gammell:** Or SWD. So, but the question I had about it is, so you mentioned like watch variables and if I'm watching 10 different variables. Mm-hmm. And so it's actually going in and probing and saying, so when it's stepping to the next instruction or whatever's happening, right? It's saying I've got these 10 variables. It's actually going, looking those up in memory, pulling those back out and then doing all these other things. But that's all happening over JTAG or SWD?

**Piotr Ezdintensky:** Yeah, that's all happening over that interface. So GDB itself actually is issuing a lot of commands with every step that it is. So, and it is sending it to the remote target. So the interesting thing here is to understand what the like chain of command here is. So GDB is... That's a good way to say it. I like that. It is the driving force of the kind of everything. It's the general. It's the general, yeah. Well, depends on if you go to layer eight, the guy between chair and keyboard.

**Chris Gammell:** Poor lady. No, the pebcacable client that you're talking about there is... I don't know what it would be. The dunce or the joker? Yeah.

**Piotr Ezdintensky:** Yeah. So basically GDB is generating commands. It is sending it over the serial interface to the Blackmagic probe. And the Blackmagic probe is taking those commands and converting them to JTAG commands. And this is, again, also a layered onion of stuff. JTAG is as much of a standard as XML is a standard.

**Chris Gammell:** Right. Is that saying that it is or it isn't? Because XML, I'm not sure if you're like being disparaging again.

**Piotr Ezdintensky:** Yeah, no. In this case, I'm being disparaging, yes. Okay, yes. Because JTAG is mostly just a signal layer definition. Okay. And then you have the state machine of the, what is it called? DAP, debug access port. And there is a state machine where you shift in bits into like a shift register. Then you issue commands with and run the state machine inside the device. But the state machine, again, in itself, the amount of commands that the state machine then interprets is depending on the device that you have connected there. So the interesting thing is that the reason why Blackmagic Probe mostly supports only ARM Cortex strips, like Cortex-M mostly, and we have some alpha support for Cortex-A, is that all that stuff is defined by the ARM debug interface version 5, ADF 5.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** It's a pretty large document that is specifying more layers of the complexity how the JTAG interface works or the SWD interface works. Because whatever it is, JTAG or SWD, the commands that are running on top of that are pretty much the same.

**Chris Gammell:** Okay. So are you basically, did you have to then go and implement this ADF inside the processor on the Blackmagic Probe? Is that the idea?

**Piotr Ezdintensky:** Yes. Yes. Okay. So it has to know how to translate the commands from GDB, read memory address so-and-so into the correct ADF 5 commands to read out from the matrix or from the... Okay.

**Chris Gammell:** And so does that mean that the Blackmagic Probe is primarily acting as a translator between GDB and the commands that talk through the JTAG port? Is that... Yeah.

**Piotr Ezdintensky:** That's kind of... Exactly right. So the easy thing to say would be it is a GDB remote protocol to JTAG converter.

**Chris Gammell:** Okay.

**Speaker ?:** Yeah.

**Chris Gammell:** You should have used that as a name. It's catchy, man. Oh, yeah. That really sounds... Or whatever you just said.

**Piotr Ezdintensky:** Yeah. It really sounds like a good title for a scientific paper.

**Chris Gammell:** Yeah. Right. Or you could have just made it an acronym and it would have been like the Fluffenwurr. You know what I mean?

**Piotr Ezdintensky:** Perfect. I love that.

**Chris Gammell:** Yeah. Right. Right. Yes. That would work. Yeah. Okay. That's interesting. But that means that you and Gareth and I forget your other collaborator, Uwe?

**Piotr Ezdintensky:** Uwe. Yeah. Uwe was library staff for the low-level staff. And Gareth is the genius who came up with the whole translation layer and the whole firmware for the Blackmagic Probe.

**Chris Gammell:** So that means you guys have to actually speak both languages, quote unquote languages or command sets, I suppose, is the best way to say it. So like if someone puts a GDB command output in front of you, you kind of know what it's saying to do? Or is it actually readable enough?

**Piotr Ezdintensky:** It is quite readable. I personally have to admit that I'm not as fluent in that as Gareth is. But there is a special command in GDB where you tell it to print exactly what it is sending over the serial interface. This is very useful when you're debugging stuff and stuff doesn't do the right thing.

**Chris Gammell:** Or something?

**Piotr Ezdintensky:** Yeah. It's set debug something one. It's somewhere in the wiki. I always forget. But I have it in my config file just commented out when I need it. That's good. That's good. Yeah. And he's able to pretty quickly get behind what's going on in there. There is a document. So GDB itself has an official document that is specifying the remote protocol. Okay. The interesting tidbit here is they're defining the server part, meaning the Blackmagic probe, what it has to implement, but not vice versa.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** So the problem with that is when you have, for example, a tool like Radara2 that is like a disassembler and you can do... It's basically IDA, but open source and with Python scripts and whatever. Got it. Got it. Anyway, so they have to implement what GDB sends to the remote target. And because that site is not properly specified, it is still doing some weird stuff that the Blackmagic probe is not accepting sometimes.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** So because we implemented the specification of the client, but the specification is a little bit loose on one end or is implementing things or we are expecting certain things to come from GDB. So in most cases it is, oh, you implemented it not the way GDB would do that. I don't think this is right. You should fix that in Radara2.

**Chris Gammell:** Ah, I see. Okay. So like translation errors kind of.

**Piotr Ezdintensky:** Yeah. It's like, well, in Radara at the moment, the biggest bug that is stopping the show is that with every screen refresh, it is sending a ton of read memory commands.

**Chris Gammell:** Oh.

**Piotr Ezdintensky:** And when the application is running, you can't read memory. So it's like, I can't give you that memory and everything just goes nuts. So yeah, that's a bug we have to sort out. But anyways, eventually we will get that.

**Chris Gammell:** Okay. That's good.

**Piotr Ezdintensky:** Just a side note. Haha. Okay.

**Chris Gammell:** Okay. So yeah. So, so walking down the chain against GDB, talking to Blackmagic, Blackmagic outputs, JTAG commands, JTAG commands are then probing internally to the registers that are on the chip and then pulling those data, the data back out, pushing it back up to GDB and then it shows it to you. That's kind of the idea.

**Piotr Ezdintensky:** Yeah, that's, that's correct. And you can do magical things with this. It's, there is so-called semi-hosting, for example, and this is your application. Uh, triggering, uh, an exception within the chip, like a hardware exception and then GDB, uh, catching that and seeing and executing commands on the host computer. So for example, you can do print devs from the target into GDB by it basically making a system call into the host GDB or opening a file, reading a file. You can do these things. It's very useful and very powerful because then you can, for, for example, you are testing a device and you need a ton of data within your, your, uh, embedded device and you don't have an SD card, you don't have an interface, but you have JTAG that you just use to flash the firmware.

**Chris Gammell:** Right. So say you wanted to like have like a, uh, a small audio file or something.

**Piotr Ezdintensky:** For example, or you have some, uh, uh, test patterns for the pins that you are using. Sure.

**Chris Gammell:** That makes a lot more sense. Yeah.

**Piotr Ezdintensky:** Then you just, in your firmware and your target firmware, you just run open file name and this file is on the PC or on the computer where GDB is running. You open that file, read that data and execute your thing and you're done. Wow. So, uh, this is one of the many reasons and also GDB being, being possible to script a lot. It makes it an amazing tool for those people that are building test checks in factories.

**Chris Gammell:** Mm-hmm. Yeah.

**Piotr Ezdintensky:** Uh, so yeah, I've seen that happen quite a lot.

**Chris Gammell:** That is awesome. Uh, and I think that's another step that people don't think about is that, you know, like that, those kind of like, uh, kind of towards the production side of things, but man, that is, uh, once you don't want to learn that one when it's the night before either.

**Piotr Ezdintensky:** Yeah, no. So, um, someone mentioned that and I don't exactly remember who said that. Basically, if you have a big project, you have to allocate the same amount of time you spend on developing the hardware on developing the tools that will be used to test the hardware in production.

**Chris Gammell:** Yeah. That sounds about right. Unless you don't care if your project works. Yeah. Yeah.

**Piotr Ezdintensky:** Sure. You can also just design something, uh, on paper and send this thing to the factory and, and sell the thing that they sent back.

**Chris Gammell:** Right. Yeah. Then take your money and run. Yeah. Yeah. Um, so, uh, I wanted to ask. You won't do it very often. Right. Yeah. The, um, when we saw each other at DEF CON, you were, you were wearing a custom badge, one of three. Um, and, uh, why don't you tell me about that real quick and then we probably should wrap up.

**Piotr Ezdintensky:** Sure. Sure. So, um, when I was developing the OneBitC, I, I was thinking about some example projects for it. So, uh, one thing that I came up with, with, uh, a friend of mine, Bob Miller was to attach a display to it because he was developing, uh, like a, uh, very cool synthesizer himself and with display and stuff. Yeah. So, uh, we came up with the idea of connecting an LCD to the OneBitC over parallel and using a DMA to, um, send the data to the display because it has much higher bandwidth than SPI, what usually people are using.

**Chris Gammell:** Right. Right.

**Piotr Ezdintensky:** So this is where it started. And I was like, well, now we have a display. What can we do with a display? And, um, as there's a big movement of, uh, like a retro hardware nostalgia stuff going on that I also got sucked into. Um, and, uh, I, as a kid, I had a Game Boy and Game Boy and DMG, the like gray and square one. So I was like, you know what? I want to build a Game Boy. So, uh, I started designing stuff around it, uh, game pad and ideas, how to connect all that stuff together and basically use a OneBitC in the center of it. Uh, I wanted to do that. But I got, uh, to a certain point and then, uh, I had to stop because we were running the Kickstarter for the OneBitC and Blackmagic Pro. Uh, so I was very busy with that and fulfillment and all that stuff. So it was sitting there. And just after the Kickstarter, I, I was thinking I need, uh, I need to play with something that I'm just intrinsically motivated to work on and decided to, uh, put an arbitrary deadline for Defcon that I will make that Game Boy like thing work. So the OneBitC, OneUp, that's how it is called. And it can be found on Hackaday.io. Um, um, I managed to actually get the three prototypes assembled and working for Defcon. And, uh, um, I think people really liked what they saw. It is pretty cool. It can display, uh, video or, uh, generated like animated video with almost 80 frames per second. That's what I was getting towards.

**Chris Gammell:** Is it? And yeah, so you said it's 80 frames per second, which is crazy. And then you also said that that was still only running like some small percentage of the processor, right?

**Piotr Ezdintensky:** Yeah. For, so the pixel generation takes about it with the, what you saw was, uh, probably the, uh, tile, uh, based, uh, like, yeah, it looked like a Mandelbrot sort of, but like a modified that the Mandelbrot thing, uh, is, uh, actually called munching square.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** Uh, so Bob Miller, who, uh, was writing a lot of the code for the display, he, uh, came up with that. I had no idea what that was until I Googled for it. And it turns out this is one of the earliest graphics demos. It was found. It was found art. Oh, cool. Basically it's an XOR function on the pixels and it is completely surface filling and it was found on the PDP one.

**Chris Gammell:** Oh, that's right. Yeah. You told me that when we were hanging out. Yeah. That's crazy.

**Piotr Ezdintensky:** And all we did is basically with each iteration of that, uh, that weird psychedelic pattern that it is generating is rotate the pattern, the palette of colors. So it is fading and like moving and changing. And this, uh, takes about, um, like one third of the frame time to render. So you basically spent one third of the times the CPU spends on creating the pixels and all the rest of the time, it's not doing anything. It's in the background. The DMA interface is just blasting the bits out to the display.

**Chris Gammell:** Yep. Yep. Right. And that's why the parallel interface, the DMA going through the parallel is, is powerful because it just goes, here's all your bits at once. Yeah.

**Piotr Ezdintensky:** I seriously was not expecting that it will be that fast. Um, we were very concerned about this. Well, concerned in the sense, oh, we will never reach the 80 frames per second. So the interesting thing is all the ILI based displays internally, they have a clock that is running the display and refreshing the screen. And it runs roughly, uh, roughly around 80 frames per second. So what we wanted to get is actually Vsync because so that it doesn't have tearing when you animate. Yep. Um, and the problem was, well, we will never be able to get the pixels fast enough to the display. So let's not bother, but now we will be able to do it, which is pretty awesome.

**Chris Gammell:** Vsync is you dump all the pixels and then the sync signal actually just turns them on to switch over. Is that the idea?

**Piotr Ezdintensky:** No, no, no. It's, uh, it's actually, uh, we, we, there is a line coming from the display that is saying when the virtual beam is racing back to the top of the display.

**Chris Gammell:** Okay. Okay.

**Piotr Ezdintensky:** Uh, and, uh, when we read this out, we can, uh, synchronize the dump of data to the display with the refresh rate of the display itself.

**Chris Gammell:** Oh, I see. I see. So you, you kind of dump it in the interim. Is that kind of the idea? Yes. Like as it's, it's like the type site type typewriter reset, right? When you push the, boy, there's an old, there's an old reference. Yeah. You see kids what a typewriter is. Yeah.

**Piotr Ezdintensky:** The other term that, uh, people are using is beam racing. Right.

**Chris Gammell:** That's from CRTs, right? Yes. Yes.

**Piotr Ezdintensky:** And in a sense, we have to do that here too, because, uh, the, um, even though the STM32 on the one bits, he has a lot of Ram, it's like 192 kilobytes of Ram, but it doesn't, still doesn't have enough Ram to have a full frame buffer in there.

**Chris Gammell:** Ah, got it.

**Piotr Ezdintensky:** So what we do is, uh, we use some of the memory, uh, that is accessible by the DMA, uh, to, uh, allocate blocks of pixels basically. And we fill those pixels with data, give it to the DMA and take another small chunk of memory, fill that with data.

**Chris Gammell:** It's a bucket brigade.

**Piotr Ezdintensky:** Yes, exactly. And while the one is being sent to the display, we are rendering the next one and so on and so forth. Yeah. So, uh, this is, this is pretty cool in the sense that, uh, well, we could also go just refresh sections of the screen and so on and so forth.

**Chris Gammell:** But sure. Sure.

**Piotr Ezdintensky:** Um, yeah, where I was getting with it. Um, I somehow lost the train of thought, but, um, well, yeah, so you, the, we were mostly

**Chris Gammell:** talking about the performance of it. Oh yeah. Yeah. Yeah. Yeah.

**Piotr Ezdintensky:** So, so, so, uh, it is basically beam racing with bigger chunks of memory. That's what I wanted to get. Got it.

**Chris Gammell:** Okay. Yeah. All right. That's cool. That's really cool. And so what, where else are you seeing people use the one bit C like what, what is, what's a good, I mean, it seems kind of like a teensy sort of, I mean like maybe similar.

**Piotr Ezdintensky:** Uh, you know, well, uh, uh, I know Paul who designed the teensy. I think the teensy is an awesome device. I really like it. Uh, and yes, uh, the one bit C is inspired. It's definitely inspired by the teensy. Uh, I really like the form factor.

**Chris Gammell:** So, uh, and the teensy uses a free scale parts as well. Right. So it's using free scale.

**Piotr Ezdintensky:** Yeah. Different family or different manufacturer, but also cortex M three's and fours, uh, or zeros, depending on which one you get. Uh, so it, it is an awesome device. The problem is it doesn't have the JTAC interface exposed. Got it. Got it. I would probably not have made the one bit C if the teensy had the JTAC interface exposed.

**Chris Gammell:** Interesting. Okay. And so, uh, if, if, so, uh, black magic probe could work on a teensy, but it just doesn't have that interface at all. Yeah.

**Piotr Ezdintensky:** So, so this is the interesting design decision that Paul made. He, where the SWD interfaces or the JTAC debugger is, he put his own chip in there and it is hardwired in there.

**Chris Gammell:** So, oh, it's the bootloader chip, right?

**Piotr Ezdintensky:** That's the bootloader chip. Right, right, right, right. So there is a tiny chip that is using the JTAC interface to, uh, load a little bit snippet of Ram executed code into the chip. This is what makes it, uh, work as well as it does because it doesn't occupy any memory on the target chip compared to some other arm based, uh, Arduino compatible stuff.

**Chris Gammell:** And then it's not like, it's not, uh, segmenting it all out. So it's not sharing even the memory space. There's no way to like overwrite one or the other, that kind of thing. No.

**Piotr Ezdintensky:** Yeah. And it's genius. I think it is an awesome solution. The problem is that, uh, the older teensies didn't have any access to those pins. The newer stuff has the pads there. So you can try to get to the JTAC interface by, you can disable the bootloader chip using like some reset line and then you can solder some wires to get to it. But, uh, I, it's, it's great to have that now, but I wanted something that is really easy to use with the black magic probe. I wanted something.

**Chris Gammell:** It's like a target platform almost, you know?

**Piotr Ezdintensky:** Yeah. So the idea was I needed something to, uh, be able to tell people, look, you want to play with the black magic probe and try it out. So either you get the discovery board or you get the one bit C and the black magic probe and you're good to go. And I will continue adding more documentation and stuff like that. So that's where it started. And this is where it is moving and, uh, doing other stuff where it is useful. Uh, I think there's a lot of, um, uh, opportunity for, um, uh, audio related stuff with it because it has two built-in DAC outputs.

**Chris Gammell:** Oh, nice.

**Piotr Ezdintensky:** Um, then there is, uh, an interesting stuff one could do with USB because it's a it has two USB interfaces.

**Chris Gammell:** Oh, so like, uh, doing like a pass through or something like that.

**Piotr Ezdintensky:** Yeah. And, uh, and so the secondary USB interface is a high speed capable, but it needs an external file. So that's, that's the two, two add on boards that I really looking forward to get, uh, put together is one is a SD card because this, this part is easy to hook into it.

**Chris Gammell:** And yeah.

**Piotr Ezdintensky:** Yeah. And also the, uh, one bitsy has all the pins for the full SD IO interface. So high speed, I, uh, um, um, SPI, uh, not SPI SD card interface. Okay. Not this SPI one where it's a little bit slower, but like additional pins, more data lines.

**Chris Gammell:** And so is there like a, is there like a hardware driver inside the chip that actually handles that stuff?

**Piotr Ezdintensky:** Yeah. It has the peripheral built in.

**Chris Gammell:** Got it. That's yeah. That's nice too. Cause then the, it's faster, but the function is probably simpler too. And well, maybe not simpler, but it's designed for that one thing. Right.

**Piotr Ezdintensky:** Yeah. And the next thing is, I think the, because the one bitsy is completely open hardware, the design files in key cut are in the repository. So if you prototype something with the one bitsy, uh, at the end, you can just copy and paste the design into your thing that you're making and just use it. Yep. So, uh, I also have the key cut, uh, footprints for the teens, uh, one bitsy. Uh, so you can just, uh, put the footprint in your design too, and use the, um, uh, one bitsy in, in your, uh, project. So I'm trying to make it as accessible as possible. And by completely making it open hardware, I think it is, uh, a nice way to play with a smaller board because the discovery boards are usually very large.

**Chris Gammell:** They are. Yeah, you're right. You're right. And yeah, and when you're like, you wouldn't try and like shoe, I mean, yes, you have access to pins whenever, but you wouldn't want to shoot, try and shoehorn that into a project unless you have a lot of, a lot of space on board. Like you wouldn't put it in a drone, for example. Yeah. Yeah.

**Piotr Ezdintensky:** Yeah. So yeah, you, you, it has its place. I think it's, uh, also it's an STM 32 instead of some other stuff. So if you want to play with an STM 32 versus, uh, other fruit, I think is selling, uh, the, um, some chips. So if you like, uh, the 21 Ds.

**Chris Gammell:** Yep. Yep. Yeah.

**Piotr Ezdintensky:** You could, uh, you could get it either from other fruit or from, uh, spark fun. I think they're selling those. So, yeah.

**Chris Gammell:** So, and, and just to clarify, so you said the, the teen C, the, the Adafruit, uh, SAM 21 Ds, the, all this stuff, it just has to be Cortex M three or four. Right.

**Piotr Ezdintensky:** There, there, there are some specific ones that we don't have the ID in, uh, in the firmware of the black magic probe, but that's an easy ad.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** Uh, we are regularly getting new people come in and it's like, oh, I don't, it black magic probe doesn't seem to recognize my chip. And, uh, it, uh, it takes, doesn't take very long time. The easiest, if it is something more, very, more different than, uh, our rule is basically, uh, if you want it added, then, uh, send a dis, uh, like evaluation board of it to Gareth and me, and we will probably add it.

**Chris Gammell:** Awesome.

**Piotr Ezdintensky:** And if you are, uh, if you have a real time constraint and stress, then you can also pay us to make it even faster.

**Chris Gammell:** What, what a convenient offering. Uh, speaking of, uh, so, okay. So people can buy, can buy these boards over on one bits squared.com. Is there a pack? Is there like a combo package so they can buy the black magic and the one bit C together?

**Piotr Ezdintensky:** Yeah. On the one bit C website, you can choose an option, uh, to get the black magic probe with it.

**Chris Gammell:** Nice. Okay. So one bit C one bit C.org, the number one bit C number one bit C.org. Right. And then, uh, pre pre pre order. Why is there a pre order link? Oh, this is still, oh, this is a Kickstarter. Of course. That was the Kickstarter.

**Piotr Ezdintensky:** Yeah. I have to change that link to go directly to the store now.

**Chris Gammell:** Yeah.

**Piotr Ezdintensky:** Yeah.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** The Kickstarter still has a few like, uh, documentation things that, uh, yeah, I, I, I, I'm pretty sure I transferred everything into the wiki on GitHub, uh, of black magic probe. So it should be all synchronized.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** Yeah. I, I, the link will eventually get you there. It's like, there is a link to Kickstarter and then on Kickstarter, there's a link to the product page. But I, uh, now after the podcast, I probably will fix that.

**Chris Gammell:** Well, you got, you got time. Don't worry. I'm slow at editing. Uh, that's great. And, and Kickstarter went well. I guess I didn't even ask that. I do remember coming there seeing it, you know, but.

**Piotr Ezdintensky:** Oh yeah. It went great. Uh, it was, uh, it was really, really good. Uh, a lot of people were interested and, um, the main thing that I was most excited about was the fact that a lot of people that got the black magic probe also appeared in the Gitter chat channel.

**Chris Gammell:** Right. And building community around it. That kind of thing.

**Piotr Ezdintensky:** Yes. Yes. The community was not really growing, um, for a while. And now suddenly there's several new people. One of like someone is, uh, uh, writing a tracing code so that we can get real time tracing for the chips. And, uh, someone is working on the Radara 2 stuff after the Kickstarter. Uh, some people are adding additional documentation or chips and stuff like that. It's just, just so awesome to see the community grow.

**Speaker ?:** Yeah.

**Chris Gammell:** That's great. So, uh, we're, I guess that, that leads right into it. So where can people find you and the community online to, to join in?

**Piotr Ezdintensky:** So, uh, probably going on, uh, black dash magic.org will lead you to the GitHub page.

**Chris Gammell:** Okay.

**Piotr Ezdintensky:** It's currently a redirect. Eventually there will be a proper website, hopefully. Uh, but yeah, that, that will direct you to the black magic probe project. Uh, then one bit squared. So the number one bit squared.com, uh, is my company's page. Um, then there is also one bit squared.de. That's the German store. So, uh, if you are in Europe, uh, you can buy from there and you, it will be faster there.

**Chris Gammell:** And, uh, that's already taken care of that kind of stuff.

**Piotr Ezdintensky:** Yeah. Yeah. Yeah. Yeah. So you don't, you don't have to deal with customs and stuff like that, which can take a while.

**Chris Gammell:** Cool. That's great. And you're on Twitter as Esden, right? Yeah.

**Piotr Ezdintensky:** I'm on Twitter as Esden. And, uh, also if you want to just chat, just come on, uh, um, gitter.im and there is a link on the project page.

**Chris Gammell:** Great. Yeah. I, I didn't realize that was, how long has that been around? I, I keep seeing Gitter links. I don't really get them.

**Piotr Ezdintensky:** Sorry. So Gitter, Gitter is basically Slack for open source projects.

**Chris Gammell:** Oh, okay.

**Piotr Ezdintensky:** That's how I would define it. And it is integrating very deeply with, uh, GitHub and it can scale for really large communities.

**Chris Gammell:** And it free or not free?

**Piotr Ezdintensky:** It's free. Okay. And it is now recently being bought by, uh, GitLab, making it, uh, like they are completely open sourcing the complete platform.

**Chris Gammell:** Oh, wow. That's, that's fantastic.

**Piotr Ezdintensky:** That is really fantastic. Uh, they are also doing a great job. This is a quite a stable platform by now. There is, uh, also an app for your phone as always. Of course.

**Chris Gammell:** You need it. Gotta, gotta, gotta check the, uh, the repo pals while you're sitting on the can, right? Yeah.

**Piotr Ezdintensky:** Or, or stuck on the airport. Well, that one's a little bit more legit. Yeah. So, yeah. And, uh, Gitter is, uh, I, the, the guys that are running the whole project are very communicative. You go into the Gitter, uh, HQ channel and you can actually talk directly with the developers. That's really nice. That's really nice. And, um, uh, they are trying really their best and they are worth supporting.

**Chris Gammell:** Yeah. Cool.

**Piotr Ezdintensky:** And, and because it integrates with GitHub so well, you get the complete history of stuff changing in your repository, uh, all the updates and when, and there is markdown in the, if you write your stuff, but it is very similar on that end for to, uh, Slack, if you are familiar with that.

**Chris Gammell:** Yeah. Right. It's just, well, Slack.

**Piotr Ezdintensky:** But yeah. And, and this is open. You can just go there and join the channel. You don't have to be invited or find the right server of Slack or whatever.

**Chris Gammell:** It's a Heroku app that, uh, you know, has something that invites you or whatever.

**Piotr Ezdintensky:** Yeah. Yeah. And you can search the complete platform for channels for different projects. It's, uh, it's meant for open and welcoming communities.

**Chris Gammell:** That's nice. Well, the amp hour will not have a chat channel because me and Dave both don't chat, but, uh, but it's good for, it's good for people that are working on that stuff every day. Yeah. Yeah. It's good for communication. Awesome. Well, thank you for coming on and communicating with us today. It has been really cool hearing about this stuff and diving into the, the world of debugging. I think that people shift. They're not already doing, I think that this is a great way to get started and actually figure out some methods for, you know, some, some better embedded, um, code writing and debugging and everything.

**Piotr Ezdintensky:** Yeah. Thank you. Thank you so much for having me. This is, uh, a lot of fun. We had so much fun talking at, uh, DEF CON. I'm glad we can do it in this venue too. Yeah. And, uh, yeah. Thank you so much for having me.

**Chris Gammell:** I'm sure we'll talk soon.

**Piotr Ezdintensky:** Thanks a lot. Have a good one. Bye.
