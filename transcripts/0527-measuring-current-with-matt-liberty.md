---
episode: 527
title: Measuring Current with Matt Liberty
url: https://theamphour.com/527-measuring-current-with-matt-liberty/
---

**Matt Liberty:** This is The Amp Hour Podcast. Released January 24th, 2021. Episode 527. Measuring Current with Matt Liberty. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Matt Liberty:** And I'm Matt Liberty, the creator of Julescope.

**Matt Liberty:** Hey, Matt. How are you? Doing great. How about you, Chris? I'm real great. I'm excited to talk about the Julescope. In fact, this is really good timing because I was going to call you anyways. I have a lot of questions about Julescope. I have some testing coming up from the board I've been working on. And I wanted to measure some low currents. And I was like, well, yeah, I'm going to call Matt anyway. So let's get him on the Amp Hour. And of course, I want to hear about this. And of course, well, not of course on this one. But Matt has also been documenting a lot of his product progress on the Contextual Electronics Consulting Forum. And that has been really useful. So let's start with what is the Julescope?

**Matt Liberty:** Well, the Julescope is a product that I created to measure really high dynamic range currents and voltage so that you could determine the power consumption and energy consumption of your product. So as you're designing a project, you have this test instrument that is Julescope in between your normal power supply and your device. And it tells you everything you need to know about how your device is functioning both as like a multimeter, but also as a waveform viewer over time for your current power, voltage, and energy and charge as well.

**Matt Liberty:** And why is that tough? I think that whenever I tell people about the Julescope or similar instruments, they're like, well, I'll just use my DMM or something like that. Or I'll use my scope. What is the actual hard part there?

**Matt Liberty:** Well, you certainly can. A lot of people get started out by trying to use their DMM or an oscilloscope with a shunt resistor. The problem with modern electronics, though, is that we typically have a very high normal operating current. So you turn on a radio or blink some LEDs. And then in order to manage power, it goes to sleep. And the difference between that active current, which is typically milliamps or even amps, then drops all the way down to microamps. That huge range is very difficult to measure. So if you think about number of bits and precision, it way exceeds what you can normally afford as far as an ADC.

**Matt Liberty:** And I think the thing I always think about is like, well, I used to work on electrometers when I was at Keithley. And so that's like really, really small currents. But the way that it would do it is like literally they would switch. You know, it was like the topology is really simple. It's actually just like a it's like a non or sorry, it's an inverting amplifier effectively. And you just switch in larger and larger resistors. And it's like in an electrometer, it's literally huge resistors, like terra ohm resistors. And then you switch them in with these monster relays as well. And I always think about that going from like super, super small currents like nanoamps up to like an amp. Well, that feedback resistor is completely different in terms of construction, in terms of its actual resistance, other, you know, parasitics and stuff like that. And it's just it's a nightmare to deal with. It's all in the switching, it feels like. Yeah.

**Matt Liberty:** Yeah. And the thing about it is it sounds really simple because it's just, you know, with with Julescope, it's a shunt ammeter, which means it's doing exactly what you're saying. It's using a resistor and then using the voltage over that resistor to estimate current. So Ohm's law. And as you go from those very high currents, it's using like a 0.01 ohm resistor. And then if you go all the way down to the lowest, it has a 1k resistor for the most sensitive range. But again, switching through all of those is not as easy as you sound, especially when you want it to be accurate. You want to have low burden voltage. So that's the voltage over that resistor. The higher it is, the more problems that you have with your target system. You can cause brownout and your target can misbehave. And typical DMMs can have burden voltage ratings of like 0.6 volts or even higher, which if you're talking about, you know, 3.3 volts or even 2.5 or 1.8 volt supplies to your board, that's crazy.

**Matt Liberty:** Yeah. You're going to have a bad time.

**Matt Liberty:** Exactly. Bad things happen. So Julescope is designed to make sure that that is always very small, 20 millivolts across the shunt resistor, and still have the full dynamic range by switching seamlessly. So it ends up being a very difficult problem when you're going through that whole range. And this is something that I've faced throughout my career, and there just really wasn't an easy way to do it. So I ended up taking some of my consulting time, spending it on my own product, and then developing Julescope so that, you know, I'd solve my own problem, but also help a lot of other people that are out there that are designing products have quantifiable ways of measuring what they care about.

**Matt Liberty:** And now you're doing it full time. I am. Support mad. Buy a Julescope, folks. Okay, well, let's talk about, okay, let's talk about how I'm going to try and paint a picture for what I want to do here. And maybe then just, I think it's actually going to be really simple in terms of like what the Julescope offers, but maybe just to help visualize what we're going to be looking at here. I'll explain the problem. We can talk through some of the measurement solutions. I'm going to get a little bit of benefit here. Yes, of course, folks, I'm going to be a little selfish with my benefit of having the creator of the device explain it to me, but hopefully you benefit from it as well. So I have this board, the ABC board, and the big thing is it's got a cellular modem and which takes a ton of current. So like upwards of, you know, an amp or two, you know, at peak times. And then it's, but it's all being controlled with an NRI-52, which is, you know, a Cortex-M4 Bluetooth modem, but it's got a lot of sleep modes and lots of, you know, very, very low sleep currents. And so what I want to do is measure each of the different phases there that each of the different, you know, lifecycle phases of modem on in steady state, modem on in transmitting, modem in sleep state, modem completely shut off, and then NRI-52 in normal operating state, and NRI-52 with everything shut off except maybe like a real-time clock. So how do I go about like starting to plug all this stuff together?

**Matt Liberty:** Well, it depends upon where you're starting from. So a lot of times in the design cycle, you start by planning, right? So it sounds like you're a little beyond that right now. Whoa, I don't do that. Yeah. Yeah, but I mean, what you've talked about are several different states that your system's in, right? So you can kind of estimate just from the design phase of what you think it should be spending as far as current or energy power in each of those modes. And then you know how long each of those modes are typically on, and you can kind of work up a budget. Ideally, you have a budget so that you just don't start measuring things and say, yeah, that looks good. You want to ideally check against what you think is right.

**Matt Liberty:** Got it.

**Matt Liberty:** You know, it helps make sense of the situation, right? So if you think you're supposed to be in your low current and it's supposed to draw 10 microamps and you're finding that it draws 20 microamps, if you hadn't done the budget, you might say, yeah, that's probably good. But if you have done your budget, you now know that there's probably, you know, a 10K resistor, a 100K resistor that is partially on or something like that. So you can use the JouleScope to just measure your device once it's built, and that allows you to check it. So you can, depending upon your system, there's lots of ways of going about it, right? But you can connect this up to your device. And if you know the state of your device and can actually put it into a mode, that's one way to actually confirm things. The other is that, you know, JouleScope has two general purpose inputs. So a lot of times you can toggle a GPIO line, and that will tell you, when you look at the JouleScope waveform, which state your device is in. So from that, you can actually chop out that area you care about and compute either the charge or the energy that you spent in that state. And then you can build up your same model from that. You know how many times you're going to be in a state per unit times, per day, per hour, whatever you care about. So you can then work your model from there.

**Matt Liberty:** Yeah, that's a great point. And I think the idea of the GPIO is good, too, because if you think about all these different operating modes, it's all been driven by firmware. And so when I go to transmit an MQTT packet over cellular, that's going to be some subroutine that's running. And I can just throw in a GPIO toggle in there as well, maybe even just as a debug thing. And then now that GPIO toggle's high and the JouleScope knows, hey, Chris is about to try and throw some stuff to the network and see what that looks like.

**Matt Liberty:** Exactly. And you can just drop in the JouleScope software, you can drop into dual markers, you know, and one on each end of that transition. And it will tell you essentially what your energy or charge is.

**Matt Liberty:** Okay. And then so in terms of the actual like plugging in, I mean, is it just going to be USB? Does it act as a battery? Like what is the actual I mean, so I know that I'm going to try and measure current, but I have to try and measure current as some kind of input. So what does that usually look like? Like how am I interfacing the JouleScope to the product normally?

**Matt Liberty:** Right. So JouleScope sits just in the middle of what your normal supply would be and your target board. So JouleScope is just an instrument. So it's not actually a power supply. And it has two inputs. It has an in positive and in negative that go to your battery or bench supply or wall wart, whatever you normally use. And then on the other side, it has out plus and out minus that just go to your target. Yeah. JouleScope comes with a banana jack by default, but it has different front panels and you can even design your own. It's open source and you can have a USB one that we offer off the shelf. We have binding posts and then people have created a few other ones that are out there on the web.

**Matt Liberty:** Oh, cool. Like what are some of the examples of the weird ones?

**Matt Liberty:** Well, there's one general one. I know that there's one that has just headers for in and out. I have one that's unfortunately that was given to me, but was never released as open source. That's USB 3 and it mostly works. USB 3 super speed. But when you start talking about interrupting a super speed bus, that signaling gets a little dodgy unless you have a repeater and that board does not have a repeater.

**Matt Liberty:** Got it. Yeah.

**Matt Liberty:** I know Colin O'Flynn made one that has party time for the LED that hooks up to his stuff.

**Matt Liberty:** Great job, Colin. Great job.

**Chris Gammell:** Doing the Lord's work.

**Matt Liberty:** That's awesome. Yeah. Okay, cool. Yeah. And so in my case, I would say that the way that I'm going to probably hook this up then is I'm going to take one of the leads to really cut down on any kind of outside weirdness. So like if I could power, I could pass through the USB-C that's going to this board, but I think it'd probably be easier to just do the battery and just interrupt the battery like positive line and pass that through the through the dual scope. Because then there's no possibility that any of the USB is going to charge the battery because of like trickle charging or something like that. It's just just coming straight off the battery through the PMID through the PMIC rather into the board. I think that would probably be the simplest.

**Matt Liberty:** Yeah, that works. And you can also use dual scope to measure the charge and discharge cycles of your system. It's not totally symmetric, but it's symmetric enough that it can measure battery discharge and recharge.

**Matt Liberty:** And how do you and that would be like if it was going through the USB or the actual battery itself?

**Matt Liberty:** It's up to you either way.

**Matt Liberty:** Okay, cool. Yeah. Great, great, great, great. Okay, so now I'm going to go trigger a measurement and I look at this thing. And I remember when Dave did a review of the dual scope, he was a little confounded by it, but I didn't find it that confusing. What do people expect to see when they're starting to actually look at measurements?

**Matt Liberty:** And it varies. So I've had a number of different customers. Some are very, you know, into this. They know exactly what they're looking for. They may have used high-end equipment that does similar things. So they're very adept at it. So they just want to get to see the waveform. Dual scope has that waveform view. But when you start the software by default, it comes up in a multimeter view because a lot of people are very familiar with multimeters, even more so than like a waveform and oscilloscope. And it will just update every half second, two hertz, and display. If that all you want is just what's going on in human timescale, that's a great way to do it.

**Matt Liberty:** Yeah, right. So you're not going to catch like the super peaky stuff, like a huge slug of current or anything. But you'll probably see steady state and maybe a little bit of variations because of things asking for more current at any given time.

**Matt Liberty:** Exactly. And as a developer, a lot of times you'll want to see, oh, I shortened this routine by 10 milliseconds or three milliseconds. And I expect to see my power go down. And dual scope in the waveform view can do that. And you can see it and actually quantify it because dual scope sampling at two million times a second, it makes it really easy to see. But if all you care about is long term energy consumption, and this happens typically after you've done product design, right? You want to actually now see how your device is going to behave in the field, how it's going to...

**Matt Liberty:** Right, right. How long will it last when it's not transmitting or if it's in different modes and trying to do a power save or whatever?

**Matt Liberty:** Exactly. And you don't care about the detailed waveform at the time. You care about collecting hours, days, months worth of data. You know, dual scope is able of doing that too with either through the UI or through scripts.

**Matt Liberty:** Got it. Cool. What, you know, so I know the NRF 52 is like a, you know, it's low power, but it's, you know, not going to be like sipping current. What is, what is like the low end? What, what, what's the kind of the lowest amount of current that you'd expect I could resolve? With the dual scope?

**Matt Liberty:** Well, our minimum resolution goes down to about one nanoamp.

**Matt Liberty:** Okay. And so that'd be like the end of the, that's like the, the, the least significant bit type of thing, right? Like the furthest digit to the right.

**Matt Liberty:** Yeah. Yeah. So that's, that's, it's resolution. The actual accuracy in that range is 30 nanoamps, plus or minus 30 nanoamps.

**Matt Liberty:** Okay.

**Matt Liberty:** You know, there's a difference between resolution, which is the, the smallest change it can detect versus accuracy. Um, and this happens with every single test instrument. This is not unique to dual scope. So you, a lot of times people get confused by that of what is the accuracy versus what can I actually see a change? And sometimes you just care about a change. If you make us a small amount of variation, but you know, you really don't care about that. A dual scope is more than accurate enough for that. So if you want to measure your sleep mode current and it goes down to a microamp, um, or even less a hundred mil nanoamps, dual scope's able to resolve that and measure it accurately.

**Matt Liberty:** Okay. That's great. Yeah. I always point people at the, uh, the bullseye, uh, example for like accuracy, precision and resolution. I guess resolution is usually not at least accuracy versus precision. Maybe there's a third one on there, but, but yeah, it'd be like, uh, I think that I always feel like that was the one that kind of helped me understand it of like throwing darts at a dartboard and accuracy is like all the darts are centered around the bullseye. Precision is like all the darts are centered in one area, but not necessarily the bullseye. And then I don't remember the last one was, it was just like, maybe resolution was like two darts next to each other and you can tell it's two darts instead of one. I don't know. It's how blurry your eyesight is, I guess. That's right. Right. It's worse every day. Worse every day. Okay, cool. So what are some pitfalls? Like what are, what should I expect to run into?

**Matt Liberty:** Well, the biggest pitfalls actually are not with just the measurement, but it's more with just understanding your design. When you, when you actually start measuring it's any complicated system, it's hard to separate things out. So if you have different microcontrollers, different subsystems, and it's not behaving like you expect, let's say it's consuming more current than you think, which is the typical case. Yeah. Tracing, tracing that down is, is not something that any instrument's going to help you with. Right. At least, you know, on your design for your board. And it's really easy to make very simple mistakes like backpowering a pin. You know, you shut down a subsystem and now you're, you're leaking a little current through a pin. You have a resistor that's slightly turned on or a pull-up that is engaged. Lots of things like that that can happen at the hardware level that it's really up to you to track down. But, you know, Julescope and, you know, other equipment that's like Julescope gives you the ability to at least see and quantify that value. But it's really up to you to figure out what's going on. And there's, there's a lot of things you have to check to make sure you've done them right when you're talking about really low power design.

**Matt Liberty:** I mean, what is the expected standard these days? I guess I always like see products being like 10 years on a coin cell or 10 years on this thing. And I'm just like, okay, well, that is like a, I guess, kind of a soft, soft goal, but it's, it's not well quantified. So like, what do you expect modern low power systems to be able to do relatively? I mean, like, you know, again, it's going to be soft, but what would, yeah.

**Matt Liberty:** Yeah. I mean, that's the thing that low power means different things to different people. So if you're in Linux and you're running something that is low power. Only 150 milliamps. Right. I mean, my, my mobile phone, even if I have it in sleep mode, you know, last for what, two days maybe.

**Matt Liberty:** Yeah.

**Matt Liberty:** So that, that's, that is a device where power is actually very important. It's just different from a sensor that's out there that someone has to drive to a remote location to upgrade the battery or replace the battery. So the products really determine the cost and benefit of battery life. So if you have a battery and it's something that you can put on your charging stand every day, like a mobile phone, then it's not so bad. You need it to last for the day. If it's something that is out in the field, let's say, you know, the whole internet of things push where you have battery powered things everywhere. Well, if you have a thousand things and the battery lasts for a year, on average, you're going to be replacing three batteries a day. Right.

**Matt Liberty:** That's right. Yeah. Yeah. So technicians are going to hate you.

**Matt Liberty:** Exactly. Well, there's a cost to it, right? Maybe there are some applications where that cost is, is justified and that's the best you can get. Yeah.

**Matt Liberty:** Or if things are like coming back through for routine maintenance anyways, it's like, okay, well, now we've got a system for doing that sort of thing.

**Matt Liberty:** Right. And this is the thing with internet of things. What is the internet of things? What battery life is appropriate? And it really depends upon the thing. But yeah, a lot of people are targeting one to two year battery lives. Some things, you know, up to 10. I haven't heard much that goes beyond that. And there's a lot of challenges even with, you know, battery self discharge once you get to that type of duration. It's not even about your design necessarily. It's about selecting a battery that can even last that long on its own.

**Matt Liberty:** Right. Commissioning systems that can last for 20, 25 years. You know, so I used to, I was just actually just looking at some of my old stuff that I was, I was replacing old like industrial systems and power plants. And those are like 30 year lifespans and it's like, okay, 30 year lifespans and they're supposed to work for 30 years, but they're not going without like monitoring without like technicians checking in on things, you know, like, yeah, the board itself is supposed to last 30 years, but like they're not powered from batteries. You know, it's like there's, and they're like these big beefy components that are just, you know, super over spec'd. So yeah, I just, I, I, I think it, it does require an overall system view in order to, to have a realistic, realistic viewpoint on everything. Yeah.

**Matt Liberty:** Yeah. And, but that said there, we're at a time in history right now where low power design is easier than it's ever been. There are a lot of low power microcontrollers, you know, the, the NRF family that you're talking about is definitely one of them. Ambic, you know, is another company out there that's really focused on low power, but even, you know, the, the normal chip manufacturers, the STs and NXPs of the world have a great portfolio of low power devices. So we have the ability with microcontrollers now to go out and design something that has a 10 microamp sleep current or 20 microamp sleep current without too much real hard design work.

**Matt Liberty:** Well, hell let's, let's pull a little current news into the, to the fray too. Even Raspberry Pi is getting into the microcontroller game. So yeah, microcontrollers everywhere, apparently.

**Matt Liberty:** Definitely. Yeah. That's, that's really cool with the Raspberry Pi thing there. The PIO stuff looks really cool.

**Matt Liberty:** Yeah.

**Matt Liberty:** Yeah. The whole microcontroller market right now is such a diverse and, you know, so you have lots of choices about, you know, everything from lots of processing down to little teeny low power stuff. It enables a whole bunch of designs.

**Matt Liberty:** Yeah. I mean, personally, I look at it, you know, again, selfishly, I look at it and it's like, there's a lot of work to be done there too. You know, like obviously, you know, you need to be able to write firmware, but also then do things like, like we're talking about here, optimizing low power design and like understanding segmenting off design and being able to, you know, turn power on and off external to a chip, internal to a chip. And, and there's just a lot of, a lot of optimization that can be done. And, and yet at the same time, things are moving really quickly outside of, you know, any, any one project.

**Matt Liberty:** Yeah, definitely. And there's some projects that battery life or energy consumption is a primary concern.

**Chris Gammell:** Yeah.

**Matt Liberty:** It's part of what makes the product. Right. And there's some things where it's just kind of a nice to have. So if you think about a kid's toy, you know, it's nice to have long battery life, but is anyone going to really complain too much if it's, you know, $10? Would they buy it if it had to be $50 and you got twice the battery life? Maybe not because, you know, having battery life and being really miserly on energy consumption oftentimes requires better engineering and better component selection. And that costs money.

**Matt Liberty:** You know, I've seen my nephews, their toys and they're loud and blinky and whatever. I feel like the short battery life is one of the benefits, you know? Oh, sorry. The battery's dead. Guess, guess that police car is not going to be making that really loud siren noise anymore, kids. We're fresh out of batteries. Yeah. Well, sorry. I guess I shouldn't have thrown all those batteries in the trash right before I knew that thing was dying. Oh, yes. Yeah. Cool. Well, I mean, so it seems like it's a pretty straightforward process on the actual using of the Julescope. I mean, have you seen them being used in unexpected ways from when you started designing this thing?

**Matt Liberty:** Yeah, there have been a few applications that have been interesting. So people have tried to use it more as an electrometer, you know, going back to your history, because those devices are extremely expensive and Julescope is not. That's right.

**Matt Liberty:** Yeah, I think Julescope is about a tenth the price, rather, of an electrometer.

**Matt Liberty:** Yeah, even the starting baseline stuff. So I've had a few people use it that way. And within reason, it does the job. I mean, if you're trying to measure picoamps or femtoamps, you're out of luck with Julescope. But that's probably one of the more interesting. I've had some people use it for more science-y base things, which I really didn't intend. You know, the target market was really people doing product design or their own microcontroller-based designs. But people have used it for other things. It's also been picked up for a lot of testing. So the QA departments for some larger companies have started using it to qualify, you know, not just the single unit during development, but across their units as they're preparing them for deployment. And this is true of, you know, any product. You want to make sure that it works before it goes out. And power, if that's one of the things you care about, it's one of the things you have to measure.

**Matt Liberty:** So people are doing that as like a factory test calibration type step? They're making sure it's low power enough?

**Matt Liberty:** There's that. That actually wasn't what I was talking about with this one. But yes, there's also the QA side, the quality assurance. So as it moves from engineering before production, there are companies that'll put, you know, 50 or even 100 units through their soak testing, usually over temperature, environment conditions, you know, temperature, humidity, voltage. And they'll be measuring power and making sure the device continues to function through that whole time.

**Matt Liberty:** I guess I wouldn't have expected like, I mean, I expect component drift to impact things, but I guess I didn't think about it in terms of leakage currents and just battery life and things like that. What is the relative complexity of these types of things that are doing that? Is it like tiny, like sensor node type of thing? Yeah.

**Matt Liberty:** Yeah. So if you're designing a little IoT node or a module, like an RF module, and you spec it over, you know, let's say the industrial temperature range, full industrial, so minus 40 to 125, your current consumption of your device is going to vary dramatically. You know, so at 125 degrees, it's going to spend a lot more energy because it's just not as efficient at the temperature.

**Matt Liberty:** I feel like my inner industrial guys, like, wait, no, I can't afford that. That's automotive temperatures. Isn't industrial 85? I thought industrial is 85, automotive is 125.

**Matt Liberty:** Yeah, automotive is 125. Yeah, 85 is industrial. Yeah.

**Matt Liberty:** I can't do 125, Matt. I don't know what the hell to do over that range. Like, man, that's like boiling, you know? That's crazy.

**Matt Liberty:** Yeah. A lot of parts now on the microcontroller side are all rated out to that. Oh, yeah.

**Matt Liberty:** I mean, like, if you're going to have to sell into the automotive market anyways, I guess they probably can't get the margin to do that extra testing. So they're just like, yep, we tested at 125.

**Matt Liberty:** Yep. Yep. And, you know, if you work out to that, it's even better, right? You know that you're going to easily pass at 85, right?

**Matt Liberty:** Yeah, totally. Bathtub curves all day. That's cool. So are people using this? So you kind of, what it kind of sounded like you were talking about, but maybe I'm putting words in your mouth here. Is anyone using this in, like, a continuous integration type of setup or scripting type of setup?

**Matt Liberty:** Well, definitely scripting. So Jewelscope itself has a full Python library on the host side that's open source.

**Matt Liberty:** Cool.

**Matt Liberty:** Actually, two parts. There's a Python driver, essentially, for the Jewelscope and a user interface for it that are two separate repos. And there's also an examples library that uses the driver and does a whole bunch of different things. So it gives you examples for how to set things up and capture data and record data. And I know people have used that for their own automated testing. So one of the choices that I had making Jewelscope is open source versus closed source versus, you know, sharing. How, where's that right balance? The test instrument industry is often very closed. Yeah. You know, we have Skippy and, you know, the way of hooking up a national instrument stuff. GPIB. HPIB. Yeah. The GPIB and LXI is the other one. Yeah. Yeah. So all these different standards. But when you talk about streaming data, they're all pretty poor. Right? They were pretty written in the 80s. Exactly.

**Matt Liberty:** Well, LXI is newer, I should say. That is late 90s, early 2000s, I think. It is.

**Matt Liberty:** Yeah. So it does streaming data somewhat. Yeah. But a lot of the test instrument mentality is that you capture a buffer, then transfer the buffer. Capture buffer, transfer buffer. Whereas Jewelscope, because it's always measuring power, you know, so it has to always be on. It can't miss a part. So it's a fully continuous streaming segment that never has a gap. There's no window like you think of with an oscilloscope. So because of that, we just ended up implementing our own Python library that allows you to hook it up to pretty much anything you want. So you can write a little Python script, and it's just another instrument that you can script in Python.

**Matt Liberty:** Yeah. It kind of sounds like that's kind of how the HackRF does it as well, where they, so Osman and crew, the Great Scott crew, they basically pipe all the data back. And then they lean on the computer to do more of the actual heavy lifting. Is it similar for Jewelscope?

**Matt Liberty:** It is. Yeah. And there's a whole class of USB-connected devices. They're one, you know, the Salier Logic stuff is another one, right? So they do the exact same thing. They just ship all the data back over to the host computer and do whatever they need to over there.

**Matt Liberty:** Right. And I think that cuts, so like, that's a great example of the scope, I think, a traditional oscilloscope. Like, basically, there's an embedded computer in there. There's a full computer in there, right? It's just like, yeah, because it's capturing that data. It needs to display that data. But now we have these smaller devices, headless effectively. So all of the, everything else is now pushed to the computer, which is already doing everything else, right? It's a general purpose machine anyways.

**Matt Liberty:** Yeah, exactly. Yeah.

**Matt Liberty:** Cool. So, I mean, are there risks with that, though? Like streaming missing packets or anything like that? I mean, with streaming versus buffering?

**Matt Liberty:** Yeah, definitely. So USB is a notorious protocol for being a little flaky. So it was designed to be low cost and move data reliably. But moving data reliably with a deadline is not something that it's ever done that great. So there is an isochronous mode in USB.

**Matt Liberty:** A what mode?

**Matt Liberty:** Isochronous or isochronous, depending upon your pronunciation. So it means that you end up budgeting a certain amount of the bandwidth of USB in this mode for your device.

**Matt Liberty:** Is that starting with an A, like asynchronous? No, I. I. Isochronous. Okay. I'm very, my brain was just like, is he saying it wrong? Like, I might be. No, no. I mean, I just, so it actually starts with a isochronous. Okay. I'll have to look that up. I've never heard of that before. Okay. So.

**Matt Liberty:** Yeah. So USB as a protocol is actually really interesting. They have a few different ways of moving data. Bulk is what most people are familiar with. If you have a mass storage device, it's using this and it does guaranteed delivery. So if there's a problem over USB, it just tries again. Then there is your interrupt mode coming in, which if you have data like from a mouse or something, it can periodically tell your computer, hey, pay attention to me. Right. Then there's your control endpoint, which is the basic of all, before all of this, of just talking to that device over control. And then there's isochronous, which is having a stream of data where you have dedicated bandwidth. The problem with isochronous is if you lose something, you lose it. The problem with bulk is if you lose something, it's going to retry, but may not retry fast enough and it doesn't guarantee bandwidth. So there's no nice thing when USB to high speed, at least, that allows you to have something that is somewhat guaranteed bandwidth and guaranteed-ish delivery that makes sense. Right. So USB is not a great protocol for streaming, but it's not terrible. It's pretty reliable. And as long as you follow some basic guidelines and don't put too much bandwidth over your USB bus, then you'll be okay.

**Matt Liberty:** Right. So don't have like four webcams plugged into your computer at the same time and all running

**Matt Liberty:** at the same time as Julescope, something like that. Exactly. Or don't plug four Julescopes into the same USB root hub because it won't work.

**Matt Liberty:** Yeah.

**Matt Liberty:** This is something that people have tried to do. And you have a limit to how many Julescopes you can have at the full data rate going back to your single root hub.

**Matt Liberty:** Let's talk about the... So you mentioned low cost from the beginning. What are you up against here? What else is kind of in the marketplace?

**Matt Liberty:** There are a few other things that are out there. The biggest competitors are ones that cost 10 times the price, really. And that's what I wanted to compete against. And then on the lower end, there are things starting from the microcurrent, which your co-host designed a number of years ago.

**Matt Liberty:** That's right. Yeah.

**Matt Liberty:** Yeah. So there... And then there's the current Ranger, which was released, oh, two or three years ago. But it does similar type of things, but slower and has some issues. And then at the low end, there's another product that came out not too long ago called NanoRanger, I think. And it's a little slow, but it's more of the multimeter style thing. And then you hop up. There's a product that's in a similar price range as Julescope that is called the OD-Arc. They have great software. Their hardware, Julescope outperforms it by quite a bit. And then there's a small Indian company that has a few products that are on the market, but I don't know too much about them.

**Matt Liberty:** The one that I'm actually interested in, too, is I keep seeing all these chip manufacturers doing it, too. So mentioning Nordic, Nordic started being like, well, we just... I think it's Nordic, but it's basically on a dev board. They have these current monitoring kind of situations. I have not tried them yet, but it seems like that's something that they're trying to do is value add from chip manufacturers as well.

**Matt Liberty:** Right. Yeah. So Nordic has their... I think it's the Power Profiler Kit 2 now that just came out.

**Matt Liberty:** Yeah, that's it. Yeah.

**Matt Liberty:** Yeah. And it's like a $100 thing. And it's... Well, it's 20% accurate. So it gives you a relative sense of things, but it's 20% accurate. It's better than nothing. But if you actually want to measure something with 0.25% accuracy, you step up to Julescope.

**Matt Liberty:** Yeah. Yeah. Yeah. And so I guess that is kind of comes down to like, what is the... So the value add, it sounds like so far, you know, hearing this stuff is software layer for sure in all this. But then accuracy. So just like the base level components, the calibration, all the other things. What else is in there? Like, what is it? User experience? Is it... You know, like maybe comparing just at the higher end too. So you're kind of straddling the two, you know, between this, you know, like a key site, whatever, whatever, and something at the very, very bottom, like a Nano Ranger. And so like, is it just lower cost, but same accuracy when you're playing against the big guys like key sites?

**Matt Liberty:** Yeah. I mean, the goal of Julescope is to be every bit as accurate as, you know, those $10,000, things that start at $10,000.

**Matt Liberty:** Yeah. Before add-ons. Don't forget the add-ons.

**Matt Liberty:** Exactly. Before you add the board that you need. Yeah. So, and I've gotten a lot of feedback from people that have those pieces of equipment and have used Julescope and those pieces of equipment end up sitting in the lab and Julescope sits on their desk and gets used. So the whole idea with Julescope is to be very simple to use. And it's, you know, I'm not the first person to create an instrument with that type of mentality. You know, the Salier guys did a great job. And they've done an awesome job. So there's a lot of similarities between what I've tried to do with Julescope as to what they did with the logic analyzer market.

**Matt Liberty:** You know, there's certain things. So Dave and I have talked on the show before about like wanting to have an oscilloscope. I feel like that's a very certain thing at the bench, you know, being tied to a computer. It's like, eh, it's not, it's not undoable. I personally, I use like the analog discovery too for, for stuff when I'm on the road or if I'm in a pinch and like, it's not terrible actually, you know, using a computer based type of thing there. But that's because I'm so like ingratiated with, to a oscilloscope and the knobs and like the tactile feedback and all that stuff. When you start getting into like things that are naturally scripted anyways, if you're running a script to tell when a microcontroller is in a certain mode, it's like, all right, well, why not just use a thing that's plugged into the computer that's running the script as well? So I just feel like some of that stuff is natural.

**Matt Liberty:** Oh, definitely. And I think there, there is a difference between people that grew up with knobs and dials and, you know, people that are coming up and, you know, just seeing these devices like the CELA Logic that don't have anything. I mean, really they have nothing. There's no, no buttons, no switches, no barely one LED, right?

**Matt Liberty:** Click and drag, click and drag. Exactly.

**Matt Liberty:** And, and for me, you know, I have, and I think this is true of a lot of engineers. Now you have a computer at your desk, you have a computer in the lab. You, you don't have to go far from a computer. So just plugging something in is somewhat natural and you get a lot better experience, at least in my opinion. So the, the knobs and clicky things, yeah, they, they scale to a point, but eventually they just get hard to use. And the goal is not to have lots of knobs and dials and clicky things. The goal is to have none ideally and just have it work.

**Matt Liberty:** Right. Right. To just give you the answer, right? That's the best case scenario.

**Matt Liberty:** And that's really what I'm focusing on and trying to get to with Julescope. And we're not all the way there yet, but it's most of the way.

**Matt Liberty:** So what I'm hearing here, Matt, is that you're implementing an AI that's going to be like, hello, Matt, your reading is 4.4 nano amps.

**Matt Liberty:** Right. Right.

**Matt Liberty:** You should think of removing that 10 K pull-up resistor. Now it would be pretty cool if it could tell you that. Yeah. Yeah. Yeah. I mean, that would, that would be great that I, I would be less interested because I think I'd, I wouldn't have a job anymore. So a little less interested, but you know, lower costs for the clients. So that's, that's good.

**Matt Liberty:** Oh, you'd still have a job. There'd just be other things you'd be doing. You wouldn't have to worry about that 10 K resistor anymore. You have to be worrying about that, the parts selection. And if the parts are all working together.

**Matt Liberty:** Right. I'd just be writing the code and everybody would be happy with that. I'm sure. Well, let's actually, let's, let's, let's hop to the code real quick. So, so, I mean, interacting. So you have a firmware background, I should say as well. I mean, like you've been doing firmware a long time. I would, I don't know if you'd refer to yourself more as a firmware engineer, but I've kind of thought about that from the, from the fact of where you, you've started stuff. Is it an accurate characterization of you?

**Matt Liberty:** I'm kind of all over the place. You know, so I, I started out, uh, graduated with electrical engineering degree and, uh, did a lot of my initial work with, uh, some circuit board design, but a lot of FPGA design, um, early in my career. Then I went back to doing more algorithms and firmware, um, and inertial sensing stuff. And then, uh, for my consulting jobs, it's mostly been firmware. So over the last, oh, 10, a little over 10 years now, I've been mostly focused on firmware.

**Matt Liberty:** Yeah. Yeah. I think that, I think that's probably because I, I met you because of consulting. And, and things like that and hearing you in embedded FM, which is another good, good episode. Uh, I'll link people into as well. Uh, I guess that probably the embedded FM thing locked me in. I'm like, oh, well, yeah, Matt's on embedded FM. He's, he's a firmware person. Yeah. Uh, you're on it. That's a good point. I had not thought about that. So, so now we're, we're doing stuff with firmware. How do you actually start to, so you, you have a dual scope in front of you. You start to see some spikes. You've verified it's maybe not pull-ups. It's not, you know, leaky parts on the board or anything like that. What do you start to do when you are trying to improve power profiles in the firmware side of things?

**Matt Liberty:** Right. So, I mean, the first step is to figure out where your power is going. And it's, it, depending upon what you're tracking, that can be easy or hard. So if you know that you're only making one change and you see your power change, that's easy. But a lot of times it's actually not quite that simple because you have a part of your firmware that goes and does a bunch of the turns on a radio, it turns on this subsystem clocking, turns on this other peripheral. So it's just if in your normal software, it's hard to figure out what is consuming what amount of power. Okay.

**Matt Liberty:** Okay. So maybe I can make it selfish again. So I'm using Zephyr and it's a real-time operating system. And so there's going to be like a sleepy mode and there's going to be a, you know, a MQTT, you know, all these different threads that are happening. Is it harder or easier to do it when you're using RTOS and trying to profile that kind of power?

**Matt Liberty:** Well, if you're just trying to profile it and not trying to figure out where it's really going, it's relatively easy, right? So you can just see where your code is spending its time, you know, during this segment that you care about, like this MQTT message send, right? So you say start of message, end of message, and then great. If that meets your goal, then you're fine. Now, the hard part is when it doesn't. Because now you have to figure out where you should be spending your time, right? You don't want to spend your time optimizing 1% of the current consumption when there's this low-hanging fruit that's consuming half of it. So optimizing that half is going to be way better return than spending your time on that 1%, where even if you optimize it, you're still consuming 99% of your power, right? So finding the things that are consuming power can be a little more exploratory typically. So you take your firmware and you chop out something. So instead of turning on the sensor, you just make up a message, right? So now you know how much your sensor contributed.

**Matt Liberty:** Ah, okay. So kind of like profiling one thing at a time and building up like a characteristic curve of how much power a certain task takes.

**Matt Liberty:** Exactly. In the real world, you want to divide and conquer, right? So you want to figure out, you know, where things are going. So a common way of doing that is just don't do something and see the difference, right? Looks like you're taking a lot of power.

**Chris Gammell:** Have you thought about not doing that?

**Matt Liberty:** Works for the short term, but not the long term, right? Yeah. You eventually have to put it back in and hopefully optimize. That's right. Right, right, right. Yeah. And the other part that gets really hard is the sleep currents because everything's shut off. And unless you've built features into your design to actually physically disable things, you know, disconnect them electrically.

**Matt Liberty:** Yeah, power switches and things like that.

**Matt Liberty:** Exactly. Yeah. Then you really don't know where things are going unless you start doing that manually.

**Matt Liberty:** And by manually, I mean getting out a hot air pencil and taking parts off the board.

**Matt Liberty:** Yeah. Well, even before you do that, one easy thing that's a really simple trick is you just go with a multimeter and measure the voltage across every resistor in your sleep mode.

**Matt Liberty:** Yeah.

**Matt Liberty:** There should be no voltage across the resistor. If there's voltage across the resistor, you're wasting power. So it's a really easy check. Capacitors have voltage across them. For your bypass caps, resistors don't.

**Matt Liberty:** Yep. Great. That's, yeah. And you can just start multiplying or dividing by resistances, right? So get your currents and start to figure out what the hell's going on there. I think, yeah, like especially for pull-up resistors, that's a great one.

**Matt Liberty:** Yeah. And if you have any pull-up resistors that are active in your sleep mode and you're thinking about battery life in terms of years, you're out of luck, right? You can't be powering any type of resistor in a sleep mode.

**Matt Liberty:** So it sounds like then you have to take a step back into the system design side of things. So when you're designing systems that are super, super low power now, what do you usually prescribe for doing that? Are you putting in a separate pull-up rail that you can shut off in a sleep mode?

**Matt Liberty:** Yeah. So if you have pull-ups that normally need to be activated, you have to make sure that they're off. So there's a few ways of doing that. One, they just are pulled to ground. A lot of historically, pull-ups were to VCC, right? Your power rail. That's just really bad when you start talking about low power design, because that means when your chip powers down, unless you can keep that pin high, it's consuming current. Now, a lot of times, if you power down a segment and you have a pull-up on the line, you're now back-powering something through that resistor. So that's also bad. So pull-ups in general are just a challenge for low power design. So yes, you have to figure out some way if they're-

**Matt Liberty:** You heard it here first, folks. Matt Liberty hates I2C. He just hates it.

**Matt Liberty:** Yeah. You have to turn them off. So basically, you have to shut off power to the I2C bus or have all the devices still remain powered, but in a low power state.

**Matt Liberty:** So you send a command over I2C and there's maybe some internal register that puts it in a mode that's low power or something like that?

**Matt Liberty:** Yeah. So a lot of things like accelerometers and sensors will have a very low power mode that they can go into. But if you're talking to a microcontroller over I2C, it doesn't necessarily have that. You may want to shut that entire subsystem off, which means you now have some load switch that goes to that target part of the design and you shut the whole thing down, but now you have to worry about back-powering it.

**Matt Liberty:** Yeah, definitely have done that one. Yeah. It's a stinker.

**Matt Liberty:** Yeah. I don't think I explained. So back-powering, so if you have an IC that's turned off and you have any type of thing driving a high level, a lot of times what happens is it will go into the chip and the chip has protection diodes on every IO. And what happens is that it goes in and actually powers up slightly the power rail inside the chip. That's what back-powering means for everyone.

**Matt Liberty:** Right. Yeah. Because basically the sensor that's out there hanging off this line, its power has been cut off, but it's still, quote unquote, asking for power. And so it's going to try and get it from somewhere. In this case, it's the diode on the other side of things.

**Matt Liberty:** Exactly. Yeah. And that's a big problem because now your resistor is dissipating that energy and your chip is now in an undefined state where who knows what it's doing when it's partially powered. Right.

**Matt Liberty:** Then you start doing silly things like putting your, or reconfiguring your pins before you go into sleep mode on the micro. And then that's also not, not, not good. Not good.

**Matt Liberty:** It's not bad. It's kind of par for the course. It's what you have to do in order to get to those extremely low currents. So you, you do need to think about the voltage level for each pin. And most ICs these days now have recommendations for the lowest power configuration for those pins. Usually, usually it's ground, right? So usually making them an output to ground, logic level zero is the lowest power, but data sheets can vary and parts can vary. So you have to, you have to look at each data sheet.

**Matt Liberty:** Yeah. Yeah. You got to read the, the page 542 of the data sheet, not just the first page folks.

**Matt Liberty:** Eventually when you get to the low power stuff. Yes.

**Matt Liberty:** Yeah. Yeah. I mean, so, and you mentioned, you know, kind of low hanging fruit. I mean, when you're, when you're starting to really, really get to the, to the bottom of the barrel there. Right. And I guess the high, high hanging fruit instead of the low hanging fruit, rather. What, what are some of the things that you think about in that case? So like, what, what are some of the things that are like the last, the last parts of, of a low power design? The last things that you've been chasing in your past?

**Matt Liberty:** Oh, it's really varied. I mean, some of the more challenging ones that I had, I, I, I had one case where flux residue was actually causing more current consumption than I thought.

**Matt Liberty:** Hmm. That's a good one. Yeah.

**Matt Liberty:** Yeah. That was a weird one. Um, and that was a, it was just a, it was a little messy and sloppy on the board and that was ended up washing the board and it went away. So that was a weird one.

**Matt Liberty:** Did you mention that on embedded FM? I think I remember hearing something about this somewhere. Maybe it was on the forum as well.

**Matt Liberty:** I did. Yeah. So I'm not sure. I've talked about this one before because it was one of those. Oh my. Yeah.

**Matt Liberty:** So that's a story you'll tell a bunch. I mean, yeah, it's so weird, right?

**Matt Liberty:** It is weird. One that I've heard from people that I've never had is bypass capacitors. So most of the reputable brands have very good characteristics. So the thing about components, right, is there's no ideal component. So every capacitor you're getting for free, a resistor, a capacitor, an inductor, another resistor that's all built into this one device. Whether you want it or not. Right. So the idea, though, is the resistor that goes across the capacitor should be very high impedance. So there should be almost no current that goes through that. So the capacitor is really two plates and nothing that jumps between them.

**Matt Liberty:** Especially DC. Yeah, exactly.

**Matt Liberty:** Yeah, exactly. But it does happen. So I've heard stories of people buying particularly off-brand capacitors or just bulk source capacitors. And they've had major leakage problems for people that are doing low power design. So you do have to be concerned about that with bypass capacitors even.

**Matt Liberty:** Hmm. And we thought we could trust the bypass capacitors. It's lurking everywhere, folks. This current is going to bite you. It's a vampire current. It'll bite you. Yeah, that's a good one. Yeah, I like that. So noticeably absent from this is like, you know, kind of, at least from this list, maybe it is a problem, though. It's like, you know, I think about like, oh, well, I should go and read about the lowest power mode that, you know, all these different things. So like thinking about the ST parts, STM32s have like all the clock trees and you can selectively power things up and down. And there's a lot of stuff, a lot of problems getting those powered up the first time, but then you can go and shut stuff off. You didn't say any of those, though. Like, I mean, or is that kind of just because you're using APIs that are naturally putting them into low power modes?

**Matt Liberty:** No, you definitely need to do that during the design phase. So what I tend to do, though, is think if I can, I'm lazy on power management as much as possible. The best way to make your life easy is to do something, do it quickly, and then go back to sleep, right? So you don't want to beat the microcontroller to be hanging around waiting for stuff or, you know, going out and doing a few sensors and then pausing and waiting for another round of sensor data while still active. So you want to have the firmware turn on, do its task, and go back to sleep. And if you can actually do that, you can make your power management thing lifecycle much easier. So you can turn on everything, do your thing, and then turn off everything. And as long as everything is needed in that time, you're not really wasting much power. So you could argue that maybe if I turned off, you know, I'm dealing with the spy sensor, for example, if I turned on the spy subsystem, did my transaction, then turned it off, I might save a little bit more power. And that's something to consider. But a lot of times that savings in that short burst is so small that it's easier just to do a single on and off for that mode. And if you have several different modes in your product, you have those different on and off segments for each mode. And that just makes your life a lot more sane. If you're really trying to get to that last bit, though, of optimization, you might have to do a little bit more.

**Matt Liberty:** Yeah. Yeah. I think in a best case scenario, I just put a bigger battery on there. If you can do that, that's the easier solution. Yeah. I think the real question, Matt, is when are batteries going to get better? Because, man, they don't, yeah, not fast enough.

**Matt Liberty:** They are getting better, but not fast. Yeah. There's a certain energy density that is just hard. You know, things tend to explode if you put too much energy in a small space.

**Matt Liberty:** Yeah. Yeah. And now the gasoline-powered electronics.

**Matt Liberty:** Fusion. Fusion.

**Matt Liberty:** Yeah. You're right. Tiny fusion bombs in our wristwatches. Ah, yes. I remember having a hand on my right hand. Okay. So we've talked about the dual scope. We talked about low power design. One thing I also wanted to talk to you about is just kind of, well, two other things, actually. One would be the product design and actually the product design process. And then kind of consulting in general. I think those are both relevant things. The first being that, you know, you've been writing these really brilliant posts on the consulting forum that are just about the process of getting this thing out in the world. I mean, what are some of the struggles that you've gone through?

**Matt Liberty:** Yeah. It's certainly a process. So just to give a background here, I was doing consulting as more or less a solo consultant. I worked with some other people on and collaborated on some projects. But I started that back in 2011 and kind of always had my mindset on building a product someday as part of my company. And back in 2017, I started being a little bit more serious about that and settled on designing what became JewelScope. And the advantage of being a consultant and starting this path is that you kind of already are carving out your time for different projects, right? So different clients. So I carved out a little bit of time to start working on what will become my product and treated it just like any of my other clients, although it was really the lowest priority client, right? You're paying customers come first.

**Matt Liberty:** I feel like it's a double whammy because one, you're not getting paid for the work. And two, you're also giving up time that you would be, you know, like doing otherwise. Maybe that's double counting. I don't know. But I just feel like it's a tough mental model because it's like, man, I could be making money for someone else right now, you know?

**Matt Liberty:** Right. And you definitely can. Cash in the bank, right? Versus spending your bankroll.

**Matt Liberty:** Yeah, right.

**Matt Liberty:** But, you know, it's something that I always wanted to do. I wanted to develop my own product. So it was more of a... Why?

**Matt Liberty:** Why is that? Yeah.

**Matt Liberty:** That's a good question.

**Matt Liberty:** You've got the sickness like others who have been on the show before? Is that what it is?

**Matt Liberty:** Perhaps. Yeah. I mean, that's definitely part of it. Part of it is that you, you know, I particularly had a motivation to create something that was leveraging me as my time, not necessarily spending it on someone else. Believing that I could deliver the company and the value. And it was also a great challenge for me. Something that I wanted to take the adventure of launching a product company, which there's a lot of things that go into that. You know, I was not blind coming into it. But I certainly didn't necessarily know everything that was going to have to happen either.

**Matt Liberty:** Yeah. There's a lot of everything else, right? I mean, that's what you wrote about, too. I think the marketing and the production and the shipping and all the other things that go into it. It's just, it's a lot of things that you probably didn't learn when you were going to school to become a double E, right?

**Matt Liberty:** Correct. Yeah. So, I mean, everything from the very mundane of how do you ship things? I mean, this is actually a huge problem. Shipping lots of stuff is, especially internationally, is just a pain and a nightmare. It just takes time.

**Matt Liberty:** Mm-hmm.

**Matt Liberty:** To things like, you know, how do you get customers? You know, the whole marketing side of things. To production. Who do I select as my production partner when I'm not going to be building a million of something, right? I'm only going to be building a small amount. It's not worth going to Asia for manufacturing. So, finding a good partner. And one of the things that I've done and I enjoy is finding small companies to partner with that they may not be the cheapest, but they focus on quality and on helping you achieve success rather than just some nameless big corporation.

**Matt Liberty:** Right. So, you can actually get some face-to-face time. You can resolve issues a little easier, maybe time zone differences. A lot of the, I think a lot of the usual benefits for domestic in general are there. But with the known trade-off of higher cost.

**Matt Liberty:** Oh, definitely. Yeah. My CM is 15 minutes up the road from me.

**Matt Liberty:** Oh, that's nice.

**Matt Liberty:** So, it makes it really convenient. And Julescope as a product is a high-touch product that has a few calibration or factory test stages, including calibration, that are a little touchy. So, having that closeness and knowing that they're capable, that there's one guy there that really knows what he's doing as far as this all the time, really helps me be confident that the product's being built right. So, by going with that local route and exploring all the other routes as well, and then finally picking that was something I really didn't see and envision from the beginning, but it's definitely part of the process.

**Matt Liberty:** Yeah, you mentioned the calibration. I don't know if I've seen you write or talk about that much. I mean, it seems like that could be, I guess my experience with calibration was when I was at Keithley, we had like a temperature-controlled room where there were a couple technicians or calibration experts that knew what they were doing, basically. And they ran, you know, they put the boxes, plugged them in, and they ran through all their cal cycles, whatever. But I guess I never really thought about actually standing up a scenario like that at a CM. What was that like?

**Matt Liberty:** So, I designed all the test stations. So, we have three different test stations that are there. A factory programming test station, the calibration station, and then I have a final test just to make sure nothing went wrong in any of the other steps just as a last sanity check. So, just in case anything ever slipped through the cracks. I had experience designing test stations for manufacturing in Asia through a prior job. So, I kind of used the same mentality there. You know, keep it very simple. Red, green, pass, fail. And it's all computer-based because Julescope is computer-based. And just keep it simple. But there are a lot of things with calibration that can go wrong. You know?

**Matt Liberty:** Yes.

**Matt Liberty:** I mean, Julescope is an amazingly sensitive instrument. So, when you're talking about nanoamps, really washing these boards is actually a big deal. They have to be clean and pristine, and nothing can be really wrong with them. And if there is, it's picked up in calibration. So, having someone that's there that I've taught, you know, walked through the process, taught them what's going on, and being able to troubleshoot. This error means, like, this type of thing. So, go look at the board again and see in this area. This was valuable. I mean, there's an operator that's less trained normally that's running it. But when things go wrong, it's good to have someone that can take control.

**Matt Liberty:** So, is it, like, phone home when you have a bad unit? Or is it just someone on site actually, you're basically training out the CM and technicians there to deal with what you're working with, what you have on site?

**Matt Liberty:** I trained out the CMs, the technician there. So, he's pretty much on top of everything. You know, every now and again, I'll get a call about something. But for the most part, they're on top of it now.

**Matt Liberty:** Yeah, that's great. That's, like, a best-case scenario, I would imagine. Especially, you know, you're a small team, right? You said it was you and your wife working together on this and then some subcontractors. And that's kind of it, right?

**Matt Liberty:** Yeah. We're going to be growing a little bit, but mostly with contractors this year for both marketing and sales and engineering as well. But, yeah, we're still a small team. It's, you know, it's been really a... It's kind of hard. Is it a solo effort? No. It's been...

**Chris Gammell:** Sure.

**Matt Liberty:** I've relied on a lot of people. But really, it's been, you know, me leading the effort along with help from a number of other engineers on manufacturing, on some of the packaging. It's really weird nowadays because we rely on so many different suppliers and vendors and partners in order to produce anything. And it's amazing what is available when you actually leverage the power of the world. But at the same time, you know, someone has to get it all done, too.

**Matt Liberty:** So, yeah. Well, and then also, I think, you know, links to the chain are susceptible to, you know, issues, right? So, for example, I may have been searching for a certain boost converter that's very critical to my design yesterday. And it's out in the entire world. And there's a 35-week lead time. It's like, holy crap, man. Like, but that is... My choices are... Obviously, I can go design in another one. But, like, if I really step back and look at it, like, well, what am I going to do? Design my own boost converter, like, at the silicon level? No, of course not. This thing is tiny, you know? And it's like... So, even just that one small thing of, like, leaning on a silicon manufacturer to do that function, that is baked into the fabric of all these products that we're making. And it's very, very interconnected. And then you start thinking about all the people stuff to just get it out the door. That's a miracle of modern commerce, I think.

**Matt Liberty:** It is. And I had the same problem. So, I had a part that is in Jewelscope that is on allocation with an advertised of 52-week-plus lead time. Yikes. What kind of part? It was a microcontroller that would not have been fun to replace. So, unfortunately... Yeah, right. Right, exactly. Yeah. And it's just a problem with this part. And, you know, automotive manufacturers that spend way more money than I do are having problems getting this part. So, I went, actually, to the manufacturer and asked for some help. And they were awesome. So, actually, they supplied me my pittance of microcontrollers compared to everyone else in the world. To, like, we'll sweep the floor for you, Matt. Exactly. We could find these.

**Matt Liberty:** We could find these on this floor.

**Matt Liberty:** Yeah. But it was more than was available. So, things were... I sucked up the worldwide supply off Mouser and DigiKey. So, that left no one else with stuff. Yeah.

**Matt Liberty:** No, I think it's a weird time, man. It's a weird time for buying parts. And I think that's another thing, too, is, like, you're operating pretty much out of distribution, right? I'm guessing you're not putting in... Maybe, I don't know. Maybe are you putting in, like, larger orders to the point where you have to, you know, do wafer starts and everything?

**Matt Liberty:** Not right now. So, we're... Our lot size is still, you know, 500 or so.

**Matt Liberty:** Mm-hmm.

**Matt Liberty:** Hopefully, that'll go up here. But we're... You know, with 500, you can kind of get by under the radar. Yeah. Our annual volume is starting to get higher. So, I'm going to probably have to start managing a supply chain soon, which is a whole nother...

**Matt Liberty:** That's a whole nother blog post right there.

**Matt Liberty:** Exactly. I've been on that side of things before in my career. But it's... So far, it's been mostly just Mouser DigiKey.

**Matt Liberty:** Yeah. Yep. You've mentioned subcontractors, and I've also brought that up. And I did want to call out... You were on the Hello Blink show. And I was talking to Harris and Sean recently. And they're like, oh, yeah, Matt was on like two months ago. I'm like, god damn it. Oh, man, he was just on. But totally different topics. So, you can go and hear Matt talk about working with contractors. I thought that was a great show. I mean, what does that add or remove from the process? I mean, has it been tough for you to work in that world? Or is it kind of familiar because of your consulting time and having subcontractors?

**Matt Liberty:** Yeah. So, I have the advantage of having been a manager for a few years. So, back in my Hillcrest days, I did a lot of the initial technology development for what became FreeSpace, but then also led a team for a few years before deciding to go off and do my consulting business. So, that experience certainly helps with hiring other people. It's not necessary, but it certainly does help. Now, that said, I haven't been overly successful with the freelancer sites either. So, Upwork, Fiverr, freelancer.com. I've struggled. I've found some good things, but it's been spotty for my experience.

**Matt Liberty:** Yeah. Yeah. You can get really lucky. I got really lucky with Bilal, who I'm working with. But otherwise, yeah, I've had some duds prior to that. So, yeah, hit or miss. And I think it's just as much like if you put a job posting out there, you're going to get a lot of applications. Some are going to be perfect for the job, and some are going to be not even knowing what a microcontroller is. So, like, okay, well, that's fine. Somewhere in between, usually you just got to filter as much as you can.

**Matt Liberty:** And when you run a business, there's so many things other than what you're good at that you have to do. So, if I look at what I can deliver with lots of value, it's the engineering side, right? That's my background. I can do the management side. I can run a business. I can do marketing. I can do sales. I can do fulfillment. But really, I can also find people that can do that. So, talking about things like everything from logo design and the getting started guide for the Jewelscope insert, those are things I was easily able to go out and get someone to assist with. And they did a great job. Those are things that on the graphics side that I've had awesome luck with finding very capable people.

**Matt Liberty:** Yeah. Yeah, that's good. My own experience running a small business, it's like, I think letting go of control is really a tough thing to do at the beginning. And I think one of the remedies for me, at least, has just been being so busy. I'm like, well, I can't spend this time, figure out how to use Illustrator and making a shitty logo four times in a row and then finally handing off. I'm just going to do it from the beginning. Okay, cool. That's done. Yeah.

**Matt Liberty:** Program art is not going to impress anyone.

**Chris Gammell:** What if I did my initials, but in monotype? I hear just Comic Sans is still the thing, right?

**Matt Liberty:** Comic Sans, yeah. Who doesn't love a good Comic Sans? Let's talk a little bit more about the hardware. You mentioned you had FPGA background, but you also do have an FPGA on board of those things on the Jewelscope. So, how does that interact there? What is that actually handling inside the Jewelscope?

**Matt Liberty:** Yeah, there are actually two.

**Matt Liberty:** Oh, okay.

**Matt Liberty:** Two of the ICE 40. So, the Lattice ICE 40 family is a nice history with the open source community. I'm using one that was not as favored by the open source community at the time. It's the Ultra. And there's two things that it's doing. So, on the... Well, let me back up first. The Jewelscope itself is an isolated design. So, there's a very definite control side that talks to the host computer. And then there's a very definite sensor side. And those are electrically isolated through a transformer and decoupling for the signals that go through.

**Matt Liberty:** On the sensor side... So, you're not going to be like my oscilloscope that's like chassis grounded that I remember in a very, very brief instant as a spark burns my retinas? Oh, my gosh. How many times have I done that? Yeah. Yeah, exactly. So, Jewelscope is... Scopes are chassis grounded, folks. Yeah. Don't touch high voltage with them.

**Matt Liberty:** Or even your 5-volt rail or 3.3-volt rail. Things tend to be unhappy. It can take a lot of current. Yeah, that's true. Yeah. I don't want to admit how many times I've probably done that. So, with Jewelscope, the sensor side is completely isolated. So, that side has to do two things. First of all, it has to do the measurement. And then it has to communicate the data to the other side. The FPGA that's on that side runs the ADC, runs the algorithm for auto-ranging. And as of this past summer, also does the statistics computation on the instrument. So, it does a bunch of math. Yeah. So, there's some people that didn't want to be sending back the full sample data for some of the long-term testing. They just wanted to send back the summary every 2 hertz. And it now computes that on the FPGA.

**Matt Liberty:** And so, the summary would be like just the current is currently – every 2 hertz, it's saying the current is 45 microamps, 47 microamps, whatever. Like, that's the summary kind of data? Is that right? Yeah.

**Matt Liberty:** So, it currently gives you the mean, min, and max. Ah. Okay. The host side stuff gives you standard deviation, you know, variance. But it was a little too much to fit into that little teeny FPGA. Variance computation requires a lot more math and stuff. And that FPGA was pretty full already. So, kind of ran out of room there. So, it does just the mean, min, max. And then sends that data over the isolation barrier to another FPGA that receives it. And that FPGA is really pretty dumb. It's just receiving that data and sending it over to a microcontroller, which then forwards it out over USB.

**Matt Liberty:** Are you using FPGAs because you wanted to have that flexibility in the algorithm side? Or because you wanted to crank some crazy custom protocol that you've created?

**Matt Liberty:** No, it's not a crazy protocol. It's very spy-ish, but not entirely.

**Matt Liberty:** Oh, is it because it's one of those ADUM isolators that's a spy-based one? No.

**Matt Liberty:** Well, it's just digital lines. It's the Silicon Labs part. But, yeah. Oh, yeah. There's nothing special about that. It's just signal lines. So, the FPGA there is running the ADC. So, I have two external ADCs, and it keeps them completely in sync, which is something that would be very hard with a microcontroller. It also is very responsive. So, part of the challenge with an auto-ranging instrument like Julescope is to auto-range quickly. So, the target device all of a sudden jumps like your radio turns on, right, on your ABC project. It jumps from microamps to an amp in less than 100 microseconds, probably, when it turns on. So, that amount of jump, if you don't react quickly, will cause a voltage drop, burden voltage, over the sense resistor inside Julescope. And if it gets too big, it would brown out your device. So, this is something that's totally great about Julescope is that it auto-ranges in less than 1.2 microseconds, most, well, worst case, mostly under one microsecond. And the FPGA is really helping make sure that we hit that deadline. Hmm.

**Matt Liberty:** That's nice. Yeah, because I guess you'd have to... Well, are you doing it with, like, actual readings off the ADC, or are you just doing it with an overload type of scenario?

**Matt Liberty:** The ADC would be too slow. So, we actually have dedicated analog hardware that helps to do that. And there's also... It's more than just a threshold. We actually have an algorithm that does essentially a derivative to help predict where the next... Yeah, the next thing. And this is one of the things that we filed a provisional or patent on.

**Matt Liberty:** That's sweet, sweet IP. Yeah. For when Keysight tries to buy them in a couple years, folks, it's because of this patent. But seriously, Keysight, buy Julescope. I mean, it's... Destroy your own margins. Why not?

**Matt Liberty:** Or make a bigger market. I mean, that's what we're really finding. Yeah, that too. Right. The Keysight instrument and that quality of instrument with the testing that's behind it, a name brand that's behind it, that doesn't mean it's good, but it means it's like buying IBM.

**Matt Liberty:** Yeah.

**Matt Liberty:** Right? And I think there's...

**Matt Liberty:** And I think also if you're building into a system, if you're building, like, a rack design, then it makes a ton of sense. But if it's, like, an isolated thing on your bench, maybe less sense. You know, like, yeah.

**Matt Liberty:** Yep. And it's great to have multiple instruments so that when you come to a challenge that you don't know whether it's your device or the instrument, you can measure it with both. And you're like, oh, yeah, it probably is my device. Right there. Right there.

**Matt Liberty:** It means that he is truly a doubly at heart because he's saying, I can just fix this by buying more gear. A firmware person would say, I can fix this by writing more code or testing more code or whatever. But a hardware person says, I can just buy more gear to test it better. Yeah. Your true colors have been shown, Matt. Exactly. It's fine. You're in good company. It's a safe space here, Matt. It's fine. You're among hardware friends. We all have hardware addictions.

**Matt Liberty:** Yeah. Surrounded by gear and eval boards. That's right. Yeah. Yeah. Yeah. Yeah.

**Matt Liberty:** That's great. So back to FPJs, are you using the open tool chain or are you using more of the vendor tools?

**Matt Liberty:** No, I started using the vendor tools. So when I started DualScope development was three years ago. So that was the very beginning of a lot of the open source tools. They're just starting maybe a year before that. But I went ahead and used the Lattice ICE software, which there's nothing to write home about, but it gets the job done.

**Matt Liberty:** Yeah. Right. I mean, honestly, that's how I love the open source stuff, but people are getting FPGA designs done for a long time. They're nasty. Some of them are just like gross tool chains and IDEs and stuff, but must be doing something. You know, they're at least outputting bit streams that work somehow. So, yeah.

**Matt Liberty:** No, but what's been happening with the open source FPGA tools have been awesome. They're now doing much faster place and route than the vendor tools and much easier, more maintainable tool set. So it's really cool.

**Matt Liberty:** Yeah. No, I'm really excited about it. So you mentioned this is on... So when we talked a little bit about what we were going to talk about here was FPGAs on... And you keep saying the JS110, which is the current one. That makes me think there's going to be other devices out there. What else are you planning to build in the future?

**Matt Liberty:** Yeah. So the Julescope, as it is today, is a great instrument, but you always learn something when you design a product. And there's new things that we now know that we can do to make things even better, both from lower cost, which is one approach, and also better performance. So two entirely different directions. We also have some requests to make more module products. So getting all the goodness of Julescope, except as a module. So you think about products that are on the market. You can go out and buy a current sense amplifier. Like pick your favorite TI, INA part, right?

**Matt Liberty:** 219, yeah.

**Matt Liberty:** That's it, yeah. Or 190 or whatever it is. And they're great parts, but they don't do high dynamic current range. Yeah. Right? So they have a lot of architectures that solve some of the basic current monitoring problems. Like they have good CMLR, common mode rejection ratio, so that they can operate over the voltage. And all these things that you need in order to do good, accurate measurement, but they don't have the dynamic range. What if you could up to a module that is a Julescope module for those cases when you need it? So that's one potential product that's on our list. And those other, you know, both lower cost and a little bit higher performance are also on our market. We're working on our roadmap. We're working on those now, but they're still quite a ways out. It's still very early.

**Chris Gammell:** Yeah.

**Matt Liberty:** You know, the initial Julescope took me, what, over two years to develop. I'm hoping to cut that this time, but we'll see.

**Matt Liberty:** Yeah. I mean, hopefully you can build on it. I mean, it seems like given your experience building these things as well, you could grab different blocks, system blocks off of the existing JS110 and then reuse it and then not have to think about it in certain ways. You know, like, so maybe the host side is ready to go and you just build a different sensor side or whatever that you call the other side of the isolation barrier and you just rework it from that perspective.

**Matt Liberty:** There'll be some like that, but I think a lot of it is going to be redesigned. Unfortunately, I'm not enamored with the USB chip that I used, the USB side chip. That chip has an errata that we've worked around, but really I would not want to design it into a new product. So, unfortunately, we can use some of the ideas and the concepts and some of the code, but not the same chip. And likewise, on the sensor side, there's enough that's going to be changing that the architecture is going to be different.

**Matt Liberty:** Got it. Oh, OK. All right. Yeah, it's crazy how that stuff does kind of carry forward. Like, it's like, you know, you're not going to go and replace all the Julescopes that are out there, you know, but then you have to support multiple versions and software kind of starts to like this branching tree of things that need to be supported. It's always frustrating from that perspective.

**Matt Liberty:** Yeah. I mean, one of the things that we have is a good definition layer for Julescope. The software itself is architected in a way that we will be able to support multiple instruments going forward.

**Matt Liberty:** Oh, that's good.

**Matt Liberty:** Yeah. So, it can be painful if you don't think about that first. We kind of thought about it. There'll be work that we need to do, obviously, but it will fit into the existing Julescope UI and existing scripts.

**Matt Liberty:** What about on the scripting side? I mean, that's all Python-based, but, like, is there anything people should know about that side of things, of, like, actually writing scripts or using other people's scripts?

**Matt Liberty:** Yeah, we have examples. I mean, Python, if you're... This is kind of an aside. Python is a great programming language for just putting things together. So, I have my entire lab, actually, you know, all my stuff, all scripted using Python. So, I can sit at my desk and control the instruments all around with scripts or just manually even from my computer. And that makes things really nice. And Julescope fits into that model.

**Matt Liberty:** I mean, have you heard about rotating desk chairs, Matt? I mean, this is just...

**Matt Liberty:** Well, if you're scripting something, right? So, if you want to do a procedure on something, and this happens, obviously, with Julescope, I do this for calibration and such, but it happens with other tests as well. You know, if you're developing a product, you just want to do something in the same order. And if you're doing that manually, that's just a pain. And why do that when you can write a script in, you know, the same time that it would take, and now you can run it all the time?

**Matt Liberty:** Yeah, that's a good point.

**Matt Liberty:** So, yeah, I have all my lab equipment hooked up just through Ethernet to the computer, and it works great.

**Matt Liberty:** And I was going to say, and you couldn't remember GPIB, though? I mean, surely some of those are talking over GPIB.

**Matt Liberty:** No, I have nothing left.

**Matt Liberty:** None of the GPIB to Ethernet converters? Oh, wow. No. You must have fancy new equipment, not fancy 30-year-old equipment like I'm using.

**Matt Liberty:** I mean, even Regal's stuff has Ethernet now.

**Matt Liberty:** Oh, yeah, but that's fancy and new. I mean, that's got the benefit of new technology, you know, using like a KeyFleet 2000 DMM that was built in 1990, you know?

**Matt Liberty:** Nope, don't have that.

**Matt Liberty:** Yeah. Well, what else should we know about the Jewelscope before we wrap up here?

**Matt Liberty:** Yeah, you can visit Jewelscope.com, check it out. And if you have any questions, there's a contact form there on the website. You know, Jewelscope as a product was something that I started out because I had this problem a lot of times during my career of trying to measure, you know, the high dynamic current range and do low power design. So it was really designed from that need to scratch my own itch, but also make sure that it was something that's very valuable to a lot of people that are out there. So check it out. And if you have any questions, feel free to contact me.

**Matt Liberty:** What is the Jewelscope retail for these days?

**Matt Liberty:** $7.99 US dollars.

**Matt Liberty:** US dollars. Okay. All right. You have a global audience. Nice. Yeah, that's no, that is a good point. And you do ship everywhere, as you mentioned. Now that you've had to figure out the international shipping, it is a capability. So are you, do you have distributors overseas?

**Matt Liberty:** We do. We have two distributors now and we're working on joining the DigiKey marketplace as well.

**Matt Liberty:** Oh, cool. Okay. Yeah, that's nice. I always wondered, like, I talked to some of the DigiKey folks about that. I was like, why do you, why, why is this a thing? Right. You know, like why, but some companies, I didn't realize that some of the companies, like big companies where it's tough to get things bought, they just have like a blanket PO with DigiKey to like, yeah, fine, whatever, buy whatever on here. It's like, oh, that, that makes sense then. Cause if I wanted to go buy a Jewelscope, it might be within the, you know, my boss says fine and anything under a thousand dollars is fine. But if I have to add Jetperch as a, your company is the, as like a vendor, that's a lot different than like, I just got it on DigiKey. No big deal. You know, that. That makes a lot of sense.

**Matt Liberty:** Yep. All the whole AVL, we've, you know, we've gone through that with a bunch of companies and it just takes time and is a barrier. So if you can just buy something online from a approved vendor, it just makes the whole process smoother.

**Matt Liberty:** Yeah. Yep. Ah, business. Isn't business fun? And Matt, where can people find you if they're looking to chat with you on, on the internets?

**Matt Liberty:** Um, so I'm on Twitter. So I'm Liberty one at Twitter and, uh, you can link it to my LinkedIn page on the show notes.

**Matt Liberty:** Okay. Definitely. Cool. All right. Well, thanks, Matt. I'm sure we're going to have you back on here at some point in the future so that I can ask you about my future current measurement needs or whatever, whatever the next thing you build is. So thanks for joining us.

**Matt Liberty:** Definitely. Well, happy to help out. And thanks for having me on the show.

**Matt Liberty:** All right. Talk to you soon.

**Matt Liberty:** Bye.

**Matt Liberty:** While Matt's Jewelscope can help you count each slug of current and additional bundle of electrons, we're counting on our patrons to help support the show and send microphones to guests like Matt. You can join our mighty band of electronic ruffians at patreon.com slash the amp hour and we'll let you into the discourse clubhouse. We'll see you soon.
