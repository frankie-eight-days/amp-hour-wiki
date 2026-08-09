---
episode: 228
title: An Interview with Shahriar from The Signal Path - Quisquous Quivering Quadripole
url: https://theamphour.com/228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole/
---

**Shariar:** This is The Amp Hour Podcast, recorded December 16th, 2014. Episode 228, with guest Shariar from The Signal Path. Quisquis, quivering, quadrupole.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics.

**Shariar:** Hi, and I'm Shariar from The Signal Path. Hey, Shariar, thanks for joining us. Well, thanks for having me. I appreciate it.

**Dave Jones:** This is the first time we've chatted.

**Chris Gammell:** Yeah, test equipment greets mashing together on The Amp Hour. That's good.

**Shariar:** Yeah, I'm really excited. I've been looking forward to this for some time now. Awesome.

**Dave Jones:** And tell us what you do for those who don't know. But I'm sure everyone's seen your video blog, surely.

**Chris Gammell:** And if they don't, they should go and pause right now and subscribe and go watch videos and then come back.

**Shariar:** Thanks, Guy. Well, I do basically two things. Professionally, I'm the ASIC's design manager, technical manager at Bell Laboratories, which is part of Alcataluson. I work here in the U.S. in the Murray Hill building, the famous Murray Hill building, where the transistor was invented and the laser was invented and so on. And I do ASIC design for whole different kind of applications, millimeter wave transmitters for wireless and for wireline of octoelectronics and so on.

**Dave Jones:** Oh, so you're in the whole group. Sorry. You're in the whole. So you're like ASIC for the entire Bell Labs? I thought you were more like a specialized in one group or something in sort of like the RF millimeter wave.

**Shariar:** Yeah. So Bell Labs has a few places around the world that works on ASIC specifically for this very, very high-end application. So for us in our Murray Hill, New Jersey building, yeah, there's a reasonably small group because we do very specialized type of work. But yeah, I kind of run that team here as about six of us or so. And yeah, we design ASICs for crazy stuff. We do crazy things.

**Dave Jones:** Only six of you design the ASICs?

**Shariar:** Yeah, there's only six of us. We're trying to expand our group, actually. You'd be surprised how hard it is to find millimeter wave designers.

**Dave Jones:** Once you ask on the amp air, it's not hard at all. Oh, I don't know, man. Yeah, I know. This is pretty specialized.

**Chris Gammell:** Look at these papers. I'm like, how many gigahertz?

**Dave Jones:** That's a lot of gigahertz. Terahertz, dude. Terahertz.

**Speaker ?:** Oh, yeah.

**Dave Jones:** It's not this gigahertz rubbish. That's DC. Gigahertz is DC to this guy. Yeah, gigahertz DC.

**Shariar:** That's true. It's funny that you say that too. Really? Oh, Jesus. Yeah, it's a famous thing that people doing millimeter wave always say. My old supervisor at my university used to say this. Gigahertz, that's DC. What is that even worth talking about?

**Dave Jones:** Oh, I love it. Good Lord. Oh, goodness. We've entered another stratosphere, folks.

**Chris Gammell:** Oh, man. I don't even... And so, what are some of the geometries and stuff like that that you have to use to get... What is the magical bits that make an ASIC go that fast?

**Shariar:** Well, generally, they refer to kind of work that I do as millimeter wave. They typically refer to anything above 30 gigahertz as millimeter wave simply because the wavelength becomes less than 10 millimeters or so. So, that's why they call it that. So, in the frequency range that I work, you know, somewhere around, let's say, 100 gigahertz, there the dimensions are really, really, really, really small. So, in silicon, you're talking about hundreds of micron for wavelengths, basically. Oh, wow. No, but at one point... I believe at 1.6 millimeter, it would be 90 gigahertz in silicon with an electric constant of 4.2. So, that's kind of the dimensions you're looking at. Now, the thing that makes devices work that fast is simply has been due to scaling. So, devices have scaled as time passes. Their intrinsic parasitic capacidences and unwanted components as part of devices have shrunk down and become so small that the devices become really, really fast. So, making a transistor that is capable of generating signals in the hundreds of gigahertz is now a trivial matter. Trivial. Trivial. Wow. Trivial. By the standards of, you know, the state-of-the-art silicon process.

**Dave Jones:** State-of-the-art, you're talking terahertz, right?

**Shariar:** Yeah. So, even, you know, if you look at what Intel makes their processors out of, Intel, the next generation processors being made, you know, in 22 nanometer, 14 nanometer. Yeah. 14 nanometer CMOS process, those devices themselves, each individual one has an FT, which is the maximum current gain of a device, in the hundreds of gigahertz, 200, 300 gigahertz easily. But, of course, a microprocessor is a very complex structure. That's not going to run at that speed. But if you were to make analog circuits, if you give me a state-of-the-art CMOS process, I can make you an amplifier that works at 100 gigahertz.

**Chris Gammell:** And that would be like a commoditized hundreds of gigahertz transistor kind of thing at that point?

**Shariar:** Yeah, it would be. I mean, if you just give me a basic CMOS process, you know, basic 22 nanometer CMOS process, making a 100 gigahertz amplifier out of it is possible. I'm not saying it's easy, but it's possible. And it's already been demonstrated. Wow.

**Dave Jones:** Can you do that? Can you make a flip-flop, for example, like a single flip-flop that works at several hundred gig? Or is it purely the analog domain?

**Shariar:** No, no, no, you can. In fact, I published a paper back in, I think it was in 2000. It was a long time ago, maybe six or seven years ago. That was an 81 gigabit per second retimer, which is a flip-flop. But that flip-flop doesn't look like a traditional CMOS flip-flop you would see with digital, you know, zeros and ones. It's a CML type circuit, which is a current mode logic type circuit.

**Dave Jones:** Yeah, right. Yeah.

**Shariar:** So that works at 81 gigabit per second. That was in a 65 nanometer CMOS process.

**Dave Jones:** So you couldn't actually get a real, like a real in quote marks, digital flip-flop, like even at a low voltage level, like with a 0.8 volt, 0 to 0.8 volts or something.

**Shariar:** I would imagine that for something like that, with a 0.8, if you go to state-of-the-art CMOS, you probably can make a 10 to 15 gigabit per second flip-flop using regular CMOS. Probably if you hand lay it out, custom lay it out yourself. Got it. Yeah. I think that's possible. I've never tried, but I think that's possible. That's awesome.

**Dave Jones:** So there's the upper limit, folks. That's probably, yeah. That's why these Intel processors still work at, you know, two, three, four gig. Because as you said, they're incredibly complex, right?

**Shariar:** Yes, they're extremely complex. Yeah. And they have thousands of digital lines where you have to meet specific timings on. So that's what limits your speed there. So maybe you can make one individual flip-flop or 10, 20 of them, so on. You know, run at 10. But to build a system out of that is a whole different problem.

**Dave Jones:** With a billion.

**Shariar:** With a billion devices. Yeah. It's a very different problem.

**Chris Gammell:** If you run away from a bear, you only have to be faster than your slowest friend kind of problem, right? Yeah. That's true.

**Dave Jones:** Now, you're like an expert in this, you know, ASIC high-speed, you know, gigahertz, hundreds of gigahertz ASIC area. Does it still impress you that Intel are able to actually design and lay out these, you know, a billion transistors operating at four gig?

**Shariar:** Yeah. Pretty high.

**Dave Jones:** Yeah, that's child's play.

**Shariar:** Oh, no, no. Not at all. It's definitely not child's play. Because the complexity of such a system alone, just to be able to design and simulate and create such a massive system is extremely impressive. And obviously, this is an evolutionary work. Oh, of course. It obviously didn't get there in one day. It took many decades. But the issue of having a billion devices, now that's a yield issue once you build a billion.

**Dave Jones:** For starters, right?

**Shariar:** Yeah, then you run into this idea of being able to actually build that many devices that work. I mean, there are some redundancies and so on, obviously, in there that allow some percentage of yield to be acceptable. But it's extremely impressive. The lithography dimensions. A device, a CMOS transistor at 22 nanometer, for example, is a far, far more complex device than it used to be when it was a 0.35 micron device. Everything about it has changed. The physics which goes into it is far more complex. They have a whole variety of different types of elements that go into it. The CMOS transistor is almost barely is made of silicon anymore. It has so many other things in it. So, they have germanium and they strain the channel and they do just crazy, crazy things. And the lithography itself is ingenious. And yeah, it's very tough. And there's only really two main players in the world or two or three main players in the world that do that kind of stuff. You know, it's Intel. It used to be IBM, which now lost its foundries, unfortunately. And there's a CMOS electronics.

**Dave Jones:** They sold them, didn't they?

**Shariar:** Well, they actually paid to give it away.

**Dave Jones:** Oh, that's right. Who actually got those in the end? I can't remember.

**Shariar:** I think Global Foundries took it.

**Chris Gammell:** Yeah, it was Global.

**Shariar:** Yeah, Global Foundries took, I think they paid $1.5 billion to give it away.

**Chris Gammell:** And Global used to be AMD's foundries, right? Isn't that right?

**Shariar:** Yes, I believe so. I'm not sure now who is. Maybe it's TSMC now. I'm not 100% sure who makes their digital circuits now.

**Dave Jones:** And who's the third one?

**Shariar:** For Intel STMicroelectronics, which is a company in France. They have a state-of-the-art STMicroelectronics.

**Dave Jones:** Oh, okay. I didn't know they were that state-of-the-art in the silicon space. Yeah, yeah. They have the SOI process. Sorry, the wafer manufacturing space.

**Shariar:** Yes, yes. They have some of the most advanced silicon germanium CIGI by CMOS process. Actually, they have the most advanced CIGI by CMOS process in the world. I didn't know. Oh, okay. Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** So, who makes your stuff? You know, you've come up with a new circuit. You want a circuit. You know, like, geez, like you're soldering some axial resistors to an FR4. Anyway, you've come up with a new circuit in quote marks. Do you have a kit we can build? The 10 gigahertz kit?

**Shariar:** Yeah, but that demo is set up in a lab, actually. But for the stuff that I published, I can tell you that it's, because it's in the paper already, it's done by Tower Jazz, which is an American company. Oh, never heard of them. And it's an American-Israeli company. It was jazz semiconductors, and they kind of combined with Tower, and it became Tower Jazz and so on. They have their own history there. But yeah, they do that.

**Dave Jones:** So, they've got their own wafer fab.

**Shariar:** Yes, yes, absolutely. And they make their wafers. And one of the reasons why some of our work is with them is because it's a certified process in the U.S. So, if you make stuff for the government, for government customers, and it cannot leave the country. So, it has to be manufactured in the United States. So, we can't go and use somewhere in Asia, for example.

**Dave Jones:** Got it. Yeah. Got it. That's cool. And, of course, the government have their own wafer fab. And they say hi to the NSA, who's obviously listening in. They've got their own wafer fab. Why are they done with the other?

**Shariar:** Yeah, I don't know. The government has historically been very focused on 3.5, indium phosphide and gas type devices. Because they, you know, for making radars and amplifiers and weaponry and things like that, those devices have been traditionally used because of, you know, their properties and so on. So, the United States has rather advanced 3.5 and gas processes for that reason. Even though we don't make microprocessors from them, we kind of have handed that market to Asia.

**Dave Jones:** What is that actual 3.5 and gas? What is that process?

**Shariar:** Oh, the 3.5 refers to the elements used in the semiconductor being from the third and fifth group in the periodic table. So, indium phosphide, gallium arsenide, those type of material. Oh, right.

**Dave Jones:** So, they're a group of, right, elements.

**Shariar:** Exactly. Got it. Yeah. So, that type of semiconductor has certain properties that distinguishes it from, let's say, CMOS or silicon germanium. Indium phosphide and gallium arsenide and gallium nitride processes have, very, very high breakdown and they are very, very, very fast. So, you can make really high power amplifiers at high frequencies with them. Ah, right. But you can build very complex circuits from them. You can only make very, rather simple circuits from them.

**Dave Jones:** Is that because of the, why is that, why is that limitation?

**Shariar:** That limitation is part of the processing limitation of this type of process itself, where the yield will become extremely poor if you start making very complex devices with them.

**Dave Jones:** As in large or just physically, physically small?

**Shariar:** Both physically large as well as having many devices in it.

**Dave Jones:** Right.

**Shariar:** Yeah. So, the yield will drop. So, you can make anything with it. Yeah.

**Chris Gammell:** There's not as much research into that because there's just not as much volume. That kind of is weird that, like, you get to play in the, I mean, you're doing some CMOS, but you also said you're doing gallium arsenide stuff now too, right?

**Shariar:** No, no, I actually haven't done any gallium arsenide, but don't underestimate them because you cannot buy a cell phone without those type of amplifiers in it. Oh, really? Because you cannot make, well, you cannot make an amplifier to transmit the type of power you want in silicon easily. There's actually, as far as I know, there's only one company in the world that's ever produced PAs for cell phones in silicon, in CMOS, and that's a very specific niche thing they've done. Every cell phone you buy, every Wi-Fi chip, everything that you have eventually that does this transmit as this type of power, you need that type of, you need those devices, you need those type of PAs in those exciting materials.

**Dave Jones:** Are they silicon on sapphire? Because we do that here in Australia. There's our only wafer fab here, I think, does silicon, specializes in silicon on sapphire RF stuff.

**Shariar:** Yeah, that's another very, very niche type of application, silicon on sapphire. I haven't done any work with it at all myself. I just know that the wafers are really pretty because they're transparent.

**Chris Gammell:** Oh, cool.

**Shariar:** Awesome. Yeah, because they're on sapphire. But yeah, I haven't done any work with that. That has its own very high breakdown material. So you can, again, do, if you want to make, let's say, a 10-watt amplifier, right? A 10-watt amplifier into 50 ohm is going to require signal swings that are multiples of the power supply CMOS even has to begin with. So obviously, your devices will break down long before they would ever be able to produce such power. Okay. So you need a device that has, you know, 10-volt breakdown. And the breakdown of a deep sub-micron CMOS device is, you know, 0.8 volts. So you can imagine why the limitation is there.

**Dave Jones:** How many broad groups are there of manufacturing technologies for, you know, chips in general? Is it like dozens and dozens and don't even ask? Or can they just be broken down into like three or four major process technologies?

**Shariar:** Yeah. I mean, they would typically be broken into mainly three. It would be all the CMOS. That includes, you know, regular vanilla type CMOS, which is very basic bulk CMOS. And then it would be thin fits and so on. And then under that category, you would have silicon and insulator SOI process and so on. So that would be all CMOS and there is silicon. Yeah, there'll be silicon germanium, which is still a silicon process and silicon by CMOS, which is a combination of silicon germanium bipolars as well as CMOS. That would be, I would say, another. It would still fit under silicon. And then there's a whole 3-5 category, like I said, gallium nitride, gallium arsenide, indium phosphide. So it's CMOS 3-5? Yeah, there will be a CMOS 3-5 and I guess you could say CIGI by CMOS. But really, it's just silicon and 3-5. That's what you can do. Right. And there's also this whole carbon nanotube stuff, which of course is another thing on its own. But we don't have really any main circuits with those yet. They're really research experimental. But they are promising, but experimental.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. How long does it typically take to go from promising to you can buy chips?

**Shariar:** Honestly, that depends on what you can sell with it. Yeah, right. Yeah. I mean, the only reason CMOS is where it is, is because we continue to demand more from our electronics. We demand more storage. We demand more processing power. We demand lower power. So they keep scaling CMOS aggressively because there's a lot of money driving it. If you remove the driving behind it, obviously nothing will happen. So that's basically really what it, I mean, there's obviously some physics involved and there's some limitations. And even with CMOS too, once you hit about eight nanometer devices and you have to perhaps do something different. Although people have been saying this for, I don't know, 10 years. But the cost also is another issue. You know, the fab cost. You know, this whole Moore's Law business they have.

**Dave Jones:** We were going to ask about this. Yeah. So there's a whole... Is it already over?

**Shariar:** No, I don't think it's over. You got to sometimes still to go. But, you know, if you think also, there is also a paradigm shift here, right? So at some point, again, everything is economical at the end of the day. And then the physics also play a role in that. So it's true that you have this doubling of processing computation and circuit complexity every 18 months or so. But the fabrication cost has the inverse slope of that. So the fabrication cost of deep sub-micron CMOS process is also doubling, going up very, very rapidly. So these things do become extremely expensive to manufacture. The only reason you can go out and buy the next Intel processor in 22 nanometer, 24 nanometer, pick it up for a couple of hundred dollars is because the market is absolutely massive. Right. If you want to make... If I want to go... If you want to go right now and do a tape out, which is what is referred to submitting your design for fabrication, and you want to say, I want to tape out instead of the RCMOS, you're looking at three or four million dollars for one mask set. Yep. So one wafer, right? Yep. So that's the kind of... And the fab to be able to produce that would have cost two billion dollars to bank.

**Chris Gammell:** Oh, I think Samsung just announced a ten billion dollar one. They just announced ten billion for their newest one.

**Shariar:** Yeah, that's because this has a huge capacity, an enormous capacity. And Samsung is in the memory business, essentially. So what is driving it is that they want to put more and more and more memory.

**Dave Jones:** Right. So that's the reason it costs so much, is just because they've got a larger throughput, larger capacity, rather than the technology itself.

**Shariar:** Yeah, I would imagine that a ten billion dollar fab is not simply ten billion dollars just because it's the state of the RCMOS. I think you can probably make a fab with less than that, but it must have an enormous capacity.

**Chris Gammell:** Oh, yeah, it does. They're building a whole new city around it, basically. Yeah. A whole city, yeah.

**Shariar:** That's crazy. I mean, they provide memory chips to everybody. So, I mean, all these SSD drives, I mean, how many years did it take for SSDs to essentially become the de facto? I mean, that's the driving force behind it. So that you can imagine if that's how fast it grows. That's why Moors Light is where it is.

**Chris Gammell:** The amp hour server is now on an SSD drive somewhere in New York. So, yeah. Perfect. Servers drive a lot of stuff. What about the actual, when you do research on this kind of stuff, I mean, this is awesome. Do you basically have to dig into, like, the design packages and, like, kind of start tweaking stuff and simulation? Or how does that stuff work?

**Shariar:** So, generally, for analog design in general, this is probably true. For millimeter wave design, there's some extra complexities that comes along with that. But normally, you know, if I were to get a design kit that I have never used before, let's say a new technology.

**Chris Gammell:** That comes from, like, a fab? That's like a design kit?

**Shariar:** Yeah. The fab will provide you with a design kit. And after you've signed the appropriate NDAs, then they give you the design kit. And then, you know, as a designer who's, let's say, hasn't used this new technology, you start experimenting with the devices to see how fast they are, you know, measure, simulate their FD and their FMAX and look at their layout and how complex they look, simulate some of their critical analog and RF performances. And then you start creating blocks that you want to, you know, do certain things with. Let's say I want to make an LNA, a low noise amplifier, or I want to make a PA. Then I go ahead and put together one and then start tweaking it and playing around with it. But when you start doing things in millimeter wave design at 90 or 100 gigahertz or even above that, then you're starting to run into some really weird things that devices do. All their imperfections are now right there. And you have to, if you don't model them. So, one of the things I did when I was a student a while back is that I designed this 160 gigahertz PLL. It's a phase lock loop that has an output at 160 gigahertz. It's intended for use for medical imaging.

**Chris Gammell:** Okay.

**Shariar:** So, at 160 gigahertz, a line, a metal line that you draw, anything that you draw that's more than a few micrometers in length is now an inductor. That is very important.

**Chris Gammell:** Yep. Right? That is so cool. So, you have to... No, it's not. No, it's not. I mean, it's... No, it's not. I'm just saying, what I'm trying to say is physics rocks unless it's stopping you from

**Dave Jones:** graduating. Physics is a pain in the ass, Chris. That's...

**Shariar:** And it's... And, you know, I have made capacitors in silicon that have a dimension of three micrometer by three micrometer. That's a capacitor.

**Dave Jones:** And how many puff is that?

**Shariar:** That's usually... That would be... Depending on the metallization, that's something around the order of 12, 15 femtoferret.

**Dave Jones:** FemtoPuff, yeah. Yeah.

**Shariar:** So, 0.015 picofarret. Yeah. Very, very, very, very small. Nice. Yeah. So, I mean, that is a... If you calculate the impedance of, you know, let's say 10 femtoferret at 160 gigahertz, it's significant. Yeah. It's right there. Absolutely. It's what you would need to match an amplifier to 50 ohms. That's all you might need. Yeah. Yeah. So... Oh, goodness. That is so crazy.

**Shariar:** This is ridiculous.

**Shariar:** So, these things start to become... So, we do complete 3D EM simulation with specialized software to electromagnetically fully simulate these components up to those frequencies before we put them back in the design and model them. And because all these are custom hand-drawn and hand-laid out, the process is iterative and time-consuming because you draw something and then you simulate it and you go back, put it in the circuit. Now, you find some result and you go back and you change it. You do this over and over and over again until you get what you're looking for.

**Dave Jones:** Now, I can imagine that the software tools and the simulators are actually more... There's probably more science that goes into those than the manufacturing technology. Would I be wrong?

**Shariar:** Well, there's certainly... I'm not sure if it's more that goes into manufacturing. I completely agree that they're extremely complex. But the only reason I'm reluctant to say that there is more in there is because manufacturing covers several classes of science at the same time. Of course. Yeah, I know. It's a totally different ballgame. You can't compare them, really.

**Dave Jones:** Yeah, but it's extremely expensive. My point is that they're ridiculously in common. Yeah, because how many people would they have working developing those software packages

**Shariar:** and simulators? I mean, huge. If you look at Cadence, right? Cadence is enormous. And they are really the only player in this game where they do complete top-down. Oh, really? The only one? Yeah. If you want to do complete top-down design, meaning that if you want to be able to do transistor-level layout all the way up to full system simulation, Cadence covers that entire range.

**Chris Gammell:** Wow.

**Shariar:** So, that's why they are the de facto software in the industry, right? And most people use that. But even for a group of, let's say, five or six designers, our CAD tool costs are maybe $300,000 or $400,000, maybe even $500,000 a year.

**Speaker ?:** Yep.

**Dave Jones:** I'm surprised it's that cheap, actually. Yeah, I can't hear it. Seriously, because there's, you know.

**Shariar:** That's only Cadence. That's only Cadence simulation layout and EM. Yeah.

**Chris Gammell:** Yeah. That's bonkers.

**Shariar:** It's very, very expensive.

**Dave Jones:** Imagine how many people they've got working on those tools. Oh, my God. It must be huge. And are there, like, do you find bugs and go, well, look, this just, you know, look, this simulator said it worked and we paid $3 million for our bloody solder mask and we made our chip and your simulator's wrong. Is that? Well, that's it.

**Shariar:** You know, no one's going to take responsibility if your simulations are wrong. But design kits change all the time, especially at, if you design something at 2 gigahertz, okay, and by now, let's say you pick up a fairly advanced silicon germanium process, let's say, and you design something at 2 gigahertz, it should be really, really, really well modeled. But if you start using those devices at 100 gigahertz, now you have to give the foundry a little bit of a leeway because they can't really completely model those things really well at 100 gigahertz. First of all, measuring a device up to 100 gigahertz is very difficult.

**Dave Jones:** Yeah, it's hard enough.

**Shariar:** Yeah. Yeah. So, yeah, so it's kind of your, it's a designer's responsibility to appreciate the limitations and work around them or build around them or have to take that into consideration. But, yeah, but, you know, we've had fairly good matching between simulation and measurements. You can see that in some of my papers, too, because we show both. But if you do good modeling, good simulation, good extraction of parasitics with the devices and all that, usually pretty close up to 100 gigahertz, I would say.

**Chris Gammell:** Do you ever get to see the release notes when the design kits change? Is it like, we did testing, but Morty was standing in the room and we didn't think he was standing in the room, so now it's a different...

**Dave Jones:** And somebody farted in the next room and it's, yeah.

**Shariar:** No, they do tell you. And our model's all wrong. No, they tell you, they tell you that, hey, you know, we remeasured some things and we found this and, you know, here's the new model. And you go to the simulator and say, damn, everything's different. After things change. It's happened before. But normally, you know, you have to keep in mind, once you start working with these things, you also... I know it seems like a kind of like a black hole where you don't know what's going on, but you tend to develop an intuitive understanding of what things are probably limited on the modeling side. So you take that into account. So you know that some things, you know, let's say the transconductance of the device, the GM of the device, that's probably accurate. That's a DC characteristic. It's a DC property. Yeah. So that's probably accurate. But, you know, let's say the capacity and the exact capacitance of the collector of the device up to, you know, down to 0.1 FF at 100 gigahertz, maybe that's not so accurate.

**Chris Gammell:** Yeah.

**Shariar:** So, you know. Right. So you work around, basically. But yeah, you're right. I mean, it does end up being a challenge.

**Dave Jones:** And those simulator tools, they would be an evolving process, of course. Like, you know, when a new manufacturing technology comes out, a new process technology, I can sort of imagine the models not being that accurate. But over time, they would build and build and build. Yeah, absolutely. You'll build up more trust in them over time. Yeah, yeah.

**Shariar:** Absolutely. I mean, a brand new design coming out, a brand new technology coming out is always going to be risky the very first time we're designing it, for sure. And of course, typically, also, when a new design kit comes in, especially in CMOS, the very first thing that comes out is the digital design kit intended for digital synthesis, which is what the whole process is geared toward. And then after that, the analog performance of the devices become refined and better and better. And then eventually becomes an RF process as well as a digital process. This is normal. It happens all the time in the state of the art. That's one of the reasons sometimes manufacturers are reluctant to build something, especially an analog circuit, right off the bat in the latest technology, because it is a little bit of a gamble, but you don't know exactly. And then by the time the process matures, the models become better. Right. And then you can count on them.

**Chris Gammell:** And that benefits, too, because the manufacturing costs usually could drop a little bit because you start using older technologies for analog stuff. Oh, yeah, yeah. Absolutely.

**Shariar:** But it's always at the deep submicron, the very, very latest technology is always on that exponential price curve. Yep. Yep. Where, you know, we're going down one technology node. Yeah. It will double or triple the cost, but it wouldn't necessarily double the performance, but it will double the price. Right.

**Dave Jones:** So, who develops these models? Is it the fabs? The fabs, too. The fabs, too. Yes, the fabs, too.

**Speaker ?:** Right.

**Dave Jones:** So, like, this is the thing that's always puzzled me. How do they develop these models and test them against an actual manufactured wafer when it's like three million bucks a pop to do a mask? Or is there a sort of a quick, cheap process they can use to sort of spin a little test circuit to check their models?

**Shariar:** Well, they are in the business of creating a process. So, for them, the cost of creating experimental processes internally, where they tweak all the knobs and tweak all the compositions of the devices in order to get what they're looking for, is part of the development cost of the whole thing. But, yeah, they do exactly what you're saying. They come up with a device architecture, device physics, which is an evolution on the old one. They scale it. They scale it. They make all the changes they think is necessary. And they do several different runs, different corners, and different process splits of what they think will happen. They have some models, which is also the evolution of the old model. And then they do some measurements and compare them with the models, and they tweak the models and so on. These models that I'm talking about for process like CMOS and silicon germanium or so, they are different types, like BC models and so on. These are standardized models that plug into the simulators. So, everybody has to create them. So, the foundry will have to do that if they want to basically sell their process as something that anyone can use. So, that's a typical thing. And they do that over and over. And once they're happy with it, they release it. And then once they're really, really happy with it, then it becomes a production run where basically everybody starts using. But if you're doing research, you typically... When I was at university, I had a really good opportunity because both of my supervisors actually had a really good relationship with foundries because they were really good at what they did. And foundries typically gave us process, experimental process before they were even released, long before they were released. And we would make some, you know, state-of-the-art record circuit in their process and there will be a feather in their cap and say, look, you know, our new process, somebody built 160 gigahertz PLL in it or somebody built a whole, you know, 200 gigahertz sensor in it. And you look what our process can do. So, it's a mutual relationship from that perspective.

**Chris Gammell:** Yeah. Got it. First time for free, next time you pay. Yeah. That's a nice thing.

**Shariar:** And this is another reason why it's so hard for me to find millimeter wave designers is because to be trained to be a millimeter wave designer is an extremely expensive thing. And not all universities even engage in... There's only a handful of universities around the world that do real millimeter wave design where the students, you know, make something at 100 gigahertz, measure it, and it's their thesis. And then they come out and they have now an experience which is really rare and it's very hard to get those people to... Well, it's hard to get them to come to New Jersey for one thing. Oh, right. It's also hard to find them. Yeah. No, for sure.

**Dave Jones:** So, how did you get into this? Did you just stumble upon it or did you go, I want to go to that university because I want to get into millimeter wave, you know, ASIC design? How did you... Tell us the story.

**Shariar:** Well, when I initially moved to Canada, which was about 20 years ago or so, then... From? From Iran. From where? I was born in Iran.

**Shariar:** Yeah. So, then I moved to Canada and, you know, being a wonderful country that it is, accepted us as immigrants and then as citizens. And so, then I went to University of Toronto for my bachelor's degree. I actually did my bachelor's degree in computer engineering and not in electrical engineering. And then I switched to electronics in my master's and then finally my PhD. And yeah, like I said, part of it is indeed luck that I got happened to start working with professors who were into very, very high speed millimeter wave design. And once I kind of got a taste of it, I didn't want to do anything else. And so, I got involved in doing that and I started working on millimeter wave data converters many, many years ago and that ultimately became my PhD thesis. Right. And then, while I was finishing my PhD, I did an internship at Bell Labs because our director who back then used to do what I used to do, he was a technical manager when I was doing my PhD, he invited us, a friend of mine and myself, to be an intern. And then we did our internship there and it was very exciting to see doing research, especially because at those times, there were very few places left in the industry that actually did research at all. Yeah. Because of the problems that they kind of, that's the very first thing that goes, right? Is that research is the thing that goes. Yeah, of course. So, Bell Labs is one of the very few places left that you could do something like that. And now, and then that, and also you could publish. And I really wanted to do those things. And that really kind of got me to go back and be there and engage in this type of research and be able to work on, you know, one day I work on phased arrays and the next day I work on circuits for optoelectronics, which are really two ends of the spectrum for, as far as ASIC design is. So, it's very exciting to be able to do that.

**Chris Gammell:** Could you explain the difference between those two and why they are so different real quick?

**Shariar:** Well, because one is for, essentially for wireless applications, doing phased arrays, you know, completely a wireless system, these up converters and down converters, very, very different than what you would build when you want to build an optoelectronic circuit, circuits for optical communication, where you have CDRs and TIAs and, you know, drivers and so on, where you're doing a very, very different type of circuit. One is a broadband application, one is a narrowband application. Oh, okay. Very, very, very different design, quite, quite different systems, in fact. And there are obviously a lot of commonalities, but... I was going to say, still things moving fast, right? Yeah, I mean, you can think about it in terms of somebody designing a circuit for a USB 3.0 chipset versus somebody designing a circuit for a Wi-Fi chipset. Right. Yep. Right. Quite different.

**Dave Jones:** And you were talking about the research side of things, how that's the first thing to go. Yeah. Like, do you find that, like, well, governments are probably too stupid, but, you know, like, just in general, people are realizing, oh, that was, like, a mistake. That was a bad thing. So, do you see, like, research coming back into the country, or... Well, it is a shame. You're right. People just don't care.

**Shariar:** Yeah, well, you know, the reason research goes out of the door right away in many situations is not necessarily because the people who make those decisions don't appreciate the importance of research, but it's because the system under which the performance of these things are evaluated, and these systems are typically short-term. Yes, always. And, yeah, so if you want to meet a bottom line at the end of your quarter, if you cut $3 million from research, that's going to look good, right? But it's not going to look good in five years. It's certainly going to look good in one year. No, that's right. Yeah. So, in some ways, you're forced to do that in order to be able to meet a certain thing. And in some other cases, some other companies, it might very well be the difference between going under or being able to actually survive for a little bit longer. So, it's difficult to say what is what. Bell Labs has this long legacy. And if you were to cut Bell Labs completely, yeah, you might save money. But because it has such a long legacy and because it has such a big impact and has such a big name associated to it, it would actually damage Akatelusen quite a bit. Oh, totally. Yeah. So, obviously, nobody would think of it. And Bell Labs produces so many patents and so much technology and has such a history of doing that. And from many, many different categories, not just from silicon. You know, we have physics discovering the cosmic background radiation. We have software, Unix and so on. Then there's lasers and transistors and, you know, a whole bunch of different things. And so, you don't want to get rid of them. That's why I love Bell Labs. You know, you always, in one way or another.

**Dave Jones:** Well, you hope because you could have said the same thing about IBM, right? And they just pissed it away. Yeah. I can't argue with that completely. IBM had almost as big a reputation as Bell Labs in terms of research.

**Shariar:** Yeah. I mean, the TJ Watson Center, which some of my colleagues from my PhD were there. Yeah. I mean, and I'm sure they will continue to do work. But yeah, it really is a shame where their process, what happened to their foundry situation. Yeah. It's all finance, you know. It's all finance. Yep. Yeah. At the end of the day. But having said that, I was thinking before we were going to record, I was thinking about this whole idea of having this access. And given everything that's happening, I was reflecting on the fact that right now as we speak, there are places in the world where people, children are regularly killed for wanting to pursue education. And at the same time, we have here and other places in the world, children that have the entire collective human knowledge on their fingertip. Yep. This is an absolutely inconceivable gap between these two points. And the only way that gap is ever going to go away is by creating education, by making it more available, by disseminating this knowledge. And this is a really big part of what you do, Dave, and what other people like you do as well. Because I think a good education system is probably one of the greatest human inventions that we can ever think of. And this research and all these things tied together from my perspective to be such an important part of who we are as a species, not just as researchers.

**Dave Jones:** Hence why your video blogs are almost 100% sort of educational focused.

**Shariar:** Yeah, absolutely. I mean, the signal pad, obviously, my attempts at creating that has been my way of giving back to the community, has been my way of being able to show and express not just what I know about the subject, but also my passion for the subject. To give somebody a great gift to give somebody is this sense of curiosity, is to want to know how things work. Things are just so much more beautiful when you understand how they work. And this is my goal for the signal pad and the time and the effort that goes into it. Obviously, as you know, I mean, I have a whole new job. So for me, the signal pad kind of always loses money. So it doesn't really, it's not intended to make money. So it's not a financial endeavor by any means. I am, again, I'm privileged to be able to do that. I consider myself highly, highly privileged to be able to have the resources and the time and the people who support it and enjoy it so much to be able to give back to the community in this way.

**Dave Jones:** And how long does it take you to produce one of those, you know, educational videos? I'm talking about, you know, one-on-ones with, you know, you set up all the elaborate tests and the test gear and the test plans and all the documentation and everything else.

**Shariar:** Yeah. So usually I think about what I'm going to do, you know, either when I'm driving or when I'm taking a shower or something like that. I usually build it up in my head first. But if I were to talk about specifically the time invested in making it, I think for every one hour of video that's produced, I think it takes about, I would say, about six hours to go from recording it and then putting it up on the website and writing a description, making a documentation. It's about one to six ratio, I think.

**Dave Jones:** I would have thought it would be more than that because some of your test setups are quite elaborate. Yeah, I have to write software. You've got to draw documentation.

**Shariar:** Yeah, I mean, the test itself, I kind of conceive in my head. I'm not counting the time, you know, driving around thinking about it. So that part is not there. But also, you know, I'm really, really used to building setups all the time. Right. So I have an advantage of just being able to do it reasonably quickly simply because I do it all the time.

**Dave Jones:** Sure.

**Shariar:** But yeah, I mean, yes.

**Dave Jones:** That makes a huge difference, doesn't it? For those who don't realize, you know. Oh, my God, yes. No, absolutely. It makes a massive difference.

**Shariar:** Yeah. And I honestly don't think you can really, really learn electronics without learning how to test. It's such a huge part of it. I mean, there's the things you pick up when you build something. It doesn't even compare to the additional experience you get by doing that from just looking at it from a theoretical perspective. Not that the theory is not valuable. They have to go hand in hand, which is why I spend a lot of my videos. I say, look, here's the theory. Here's the calculation. And here's the circuit. And here's the measurement. This is how you measure it. This is how you design it. And this whole picture is the whole experience. And I hope people do spend the time to try and build it.

**Chris Gammell:** Yeah, because the theory without the – there's some phrase about that, too, where it's like theory without practice is something. I don't know. But, I mean, basically, I think about my days of, like, starting on electronics and not having the theory and just kind of, like, you know, trying this, pushing this wire here, trying this, trying that. And that causes just as much confusion as never trying it at all and, you know, going through a simulator and being like, oh, well, the answer is a giga amp. That doesn't work either. Yes, yes, a giga amp.

**Shariar:** I'd like to see what problem you've solved when a giga amp was the answer. Yeah, well, you know, this place was not always my friend. But – Yeah, you know, I was actually listening to what Dave was talking about recently when he was talking about, you know, what qualifies as a hobbyist and what skills you should have as a hobbyist. Yeah, right, yeah. And I know people are, you know, people are discussing and giving sometimes Dave, you know, a hard time or you're being too tough. And the thing is, my perspective is, yeah, you have to have those skills. I mean, you need those skills. You need those skills. First of all, you need those skills to distinguish yourself. If everybody is going to – Of course. If everyone is going to be able to – Everyone is going to play with an Arduino, how are you going to be the person who does more? You have to know more. There's no question about it. And the second thing is that – I mean, I like the whole – the fact that Arduino has made so many things, you know, available to people and people can build all these complicated and wonderful things. This is great. My only fear and my only concern with this Arduino ecosystem is that sometimes it can give the people the wrong impression that they have accomplished something. Right. But in reality, you – but in reality, they haven't, even though the outcome is very impressive. But that's not – they didn't do that. The outcome is just a part of the ecosystem they became a part of. That's not what they did. And it's very easy to tell, you know, just wire up your microcontroller once. Just do it yourself. Just put it on a breadboard, put your crystal, put your decoupling, put your – and just find out how many problems you're going to run into. And, you know, you'll see the difference then.

**Dave Jones:** That's – it's exactly like building up a kit and it works first go. Yeah. What have you learned? Yeah. Well, you've learned how to build a kit. You've learned, you know, like apart from that, you've learned nothing. Yes.

**Shariar:** No, it's not that – I mean, the experience is rewarding and there is definitely learning. Of course. But, yeah, I mean, if you want to really – you have to be careful to distinguish what should make us feel satisfied at the end of a project. What is that sense of – what exactly have you gotten out of it? And that's why I mentioned this in one of the videos before. It's essentially in agreement with what you were saying is that I have learned so much from messing things up and things not working. Yeah. Yeah. Make things that don't work. Totally. So, you can learn something from it. Yeah. Yeah. So, that's my only goal. To make an LED blink on a microcontroller was a colossal undertaking 20 years ago for me. Yeah. That's right. I know. So, now it's just – yeah, you just plug it in. It's there. It's – yeah. And it's great. I think it's – it's the fact that it's so available and then so many people are using it and there's so many amazing things people do with it. It's wonderful. I would never take anything away from that. I just want to make sure that people don't underestimate and eliminate that foundation that is needed to really feel like you've done something.

**Chris Gammell:** So, what I'm hearing here is that you need to jump into analog to really feel accomplished. Is that what I'm really hearing?

**Shariar:** No, no, no, no. It doesn't have to be analog. You just have to – you have to build a couple of things from scratch. If you have an Arduino setup, I should be able to come and ask you 10 questions about exactly how something works and you should be able to know those answers and you should ask yourself those questions. And that would be great and I hope that people continue to do that.

**Dave Jones:** But we've always said here on The Amp Hour that I think we're pretty much in agreement here that we don't care how people get into the hobby or get into the field as long as they do. Yes, yes. So, that's the beauty of the whole hacker maker, you know, slash Arduino thing is that there's so many more people actually getting in there and playing. Yeah, I mean, this was inconceivable before. Yeah, it's – I know. It's not the ideal way that we'd like it to happen. But the fact that it's happening is, you know, brilliant.

**Shariar:** Yeah, absolutely. I really, really am amazed of what has happened with this Arduino ecosystem and the things that you can do that – yeah, I mean, it was completely impossible before. It is amazing. I appreciate the whole thing.

**Dave Jones:** And it's nothing actually to do with the Arduino hardware or software itself. It's just the ecosystem which is – and the community which has built up around it.

**Shariar:** Yep, yep, exactly.

**Dave Jones:** You know, I mean, there's – yeah. It's just absolutely remarkable. Yep, yeah. I mean, this, you know, this hardware and software ecosystem has been there for 20 plus years. Absolutely. You know, 30 years. I mean, there's been these development boards and easy-to-use, you know, development environments around for a long time. But, yeah, for some reason, it's just sort of – boom, it's exploded.

**Shariar:** Yeah, absolutely. Absolutely. It's great. It is. It's definitely – no complaint from me.

**Chris Gammell:** So, you mentioned that the – you know, you're really big on the education, especially that kind of reaching into, you know, helping people that are less privileged in terms of, like, background and stuff like that. Have you had any experiences with that where you've heard from users in, you know, that have been like, because of your videos, I'm now working on millimeter wave craziness like you are, that kind of thing?

**Shariar:** I'm not capable of capable than any specific lesson that I can give anyone. I have, you know, I have people who have done this for me in my past. My uncle, for example, my uncles, both of them are brilliant, brilliant men. And they taught me so much. They gave me this sense of curiosity. I remember one of my earlier memories was, I don't remember even how old I was. Might have been six or seven. My uncle told me that, remember that if a day passes where you learned nothing new, is a day where you have been dead.

**Chris Gammell:** I like that.

**Shariar:** You haven't been alive in that day. I mean, that is a really, really powerful message. And to follow and take that to heart, I think can be. And I'm in his debt for giving me that perspective. It's all about perspective. It's how you look at the world and how you look at everything that happens around you. And this is a very beautiful lesson to be able to teach somebody, especially at the language.

**Dave Jones:** Yeah. It's a very interesting point you raised there because I see the same thing. I don't see the actual video. I might do a whiteboard tutorial on op amps or something. Right. And it's not necessarily that I'm teaching people that particular thing. Right. It's that I'm encouraging them to be interested in it. And so that's why I don't necessarily care what style of video I do as long as I keep it interesting and entertaining and enthusiastic. And people have said that. That's what they've said. It wasn't one video. It's just your attitude that got me back into it.

**Dave Jones:** Yes. You know, I was a hobbyist 30 years ago and I gave it up. And now you've sparked my interest again. And, you know, there's countless people who have said that. It's not the specific video. And I think you've seen the same thing. It's not, you know, a specific thing that you're actually teaching them. It's more of a general, you know, getting people interested.

**Shariar:** Yes, yes. I mean, it's in your voice. It's in your mannerism. I mean, passion exudes itself. Yeah, totally. You can detect it as soon as somebody is passionate about something. It really, really. And it really shows. And it's a wonderful thing.

**Dave Jones:** So that's why I consider myself more of a, you know, entertainer than an educator. Yeah, you do that too. People might, yeah, people might learn, you know, stuff on the side by watching my videos. But that's not the whole intent of my videos is not to, you know, just teach, you know, everything. It's just, yeah, give people something they can watch that's better than some soap opera, perhaps.

**Shariar:** Yeah, I mean, it's quite, I mean, compared to obviously your work, you have so many, many, many episodes. You know, I must be almost 700 by now, if I'm not mistaken. Yeah, yeah. Yep, pretty darn close. Yeah, so, I mean, I have only about 40-something episodes. So it's not even close. It's an order of magnitude off already.

**Dave Jones:** But it doesn't matter. It's the fact that, you know, it's the fact that you have the same type of enthusiasm. And yours are highly technical educational content compared to mine. I mean, you know, there's quite a big difference there between your educational ones and my attempted educational ones. You know, purely from your background.

**Chris Gammell:** I have to say that the cryogenic stuff, that was one of my favorite of yours. That was stuff that I just never even knew about after, you know, undergraduate degrees. Yeah, yeah, that's cool. Very cool.

**Shariar:** That's cool. Yeah, I have, I mean, I do want to do, sometimes I do want to do more things related to physics as well. Because it is something that I am interested in. And sometimes I dive a little bit into things that are a little different than electronics. Like when I did, you know, the monochromator experiments or when I talk about wavelength meters and things like that. Those are free space optics stuff. It's pretty interesting. It's not my expertise, but it is, you know, something that I've always enjoyed. And I like definitely like making those videos. And of course, I like playing with test gear. Who doesn't like to play with test gear? Yeah, exactly.

**Dave Jones:** I know.

**Shariar:** So, you know.

**Dave Jones:** We can be accused of being test gear freaks. Oh my God, yeah. Absolutely.

**Shariar:** And I mean, at work, I have, you know, I have basically the state of the art of anything that you can imagine at work. So, I'm surrounded by wonderful, wonderful test gear all the time.

**Dave Jones:** How much custom test gear do you have to build? I can imagine you're building custom jigs and interfaces and front ends, perhaps. Do you have to build any complex test gear yourself?

**Shariar:** Yeah, I mean, some things are, has to be complex and custom. For example, you know, just give you a simple example there. Let's say you want to generate a signal at 100 gigahertz to test an amplifier that you have at 100 gigahertz, right? And then you want to measure its linearity. You want to measure how linear is this amplifier at 100 gigahertz. Now, if you want to measure how linear something is at 1 gigahertz, it's fairly straightforward. But at 100 gigahertz, you're going to have to generate two tones, two tones of signal that are, you know, separate by certain frequencies so that you can do intermodulation product tests and things like that. Generating two tones next to each other at 100 gigahertz? Well, not so easy. So you'll have to kind of, you have to put together a bunch of microwave components to be able to combine different signals, you know, and then put attenuers and so on and combine them and then get two tones. And nowadays, of course, more and more and more equipment is available at 100 gigahertz up to 5 terahertz even of test equipment is reasonably possible to do. And they all operate on the same principle, basically. I mean, network analyzers up to several terahertz are now pretty easy to make nowadays. More complex. Really? Yeah, because they all operate on the same principle of operation. They all have.

**Dave Jones:** Right, of course.

**Shariar:** They all use, you know, signal multiplication and they all use detectors and so on. And so they're easy to buy. When I say easy, I mean, they're very expensive, but they're.

**Chris Gammell:** You took your money quickly, huh? Yeah.

**Shariar:** So they're, you know, people make them all the time. Several, there are several manufacturers that do it. And yeah, go ahead. Who's this? I mean, Vidya, Virginia Diode makes them. OML makes them Agilent or Keysight, which rebrands, I believe, other people's extenders. Because for a company like VDI, Virginia Diode, that makes extenders up to, you know, a couple of terahertz or so, they don't make network analyzers themselves. That doesn't make any sense. So they make the extenders, which attach to network analyzers. Then the whole system can then now measure S-parameters in a particular band. Let's say 110 to 170 or 270 to 400 and so on. So then they make those extenders for Keysight or for Enritsu and so on and on. And so they do it. So now, you know, we can do that fairly easy. But sometimes some tests will be more difficult. Now I would say making tests. When I was a student, making tests at 110 gigahertz was, yeah, it was pretty tough. Nowadays, making tests at 500 gigahertz would be equivalent. You know, it just keeps moving. Kids these days, right? Kids these days. Yeah, yeah. And the terahertz transmitters, yeah. Yeah, seriously.

**Dave Jones:** In their mom's basement. Yeah, yeah.

**Shariar:** So nowadays, you can do these kind of... And people underestimate. I mean, generating a signal at 100 gigahertz is tough for sure. But I think even from eBay, you might be able to pick up some stuff to ultimately generate 100 gigahertz. Yeah, probably. But the thing is that because of... In the United States, it might be a little bit easier. But other countries, it's very tough because there are very strict regulations on how much power you can transmit, be able to generate and transmit above 90 gigahertz or so because of military restrictions.

**Chris Gammell:** Yeah, ITAR.

**Shariar:** Yeah, ITAR.

**Dave Jones:** Just remember, kids, it's only illegal if you get caught, okay? If you get caught... If you get caught... If you get caught... If you get caught...

**Chris Gammell:** If you get caught... Dave does not speak for me. As someone who's easier to get to, Dave does not speak for me. Yes, yes.

**Shariar:** And this is one of the things that I have, you know, strictly tried to adhere to is that everything that I do on the signal path is 100% separated from everything that I do from professionally. Yeah. The signal path stuff is completely isolated. All my test gear is completely separate. All my own test gear, nothing to do with Bell Labs at all. So, you know, that way there's a good distinction which is very important.

**Dave Jones:** Okay. So, you wouldn't... So, you would... Even if you were allowed to, you would feel... You wouldn't feel right using Bell Labs Teske.

**Shariar:** Oh, yeah, yeah. For sure. I mean, there's completely... Complete separation from that perspective. Even when... For example, I did a tutorial and demonstration of the Keysight's Agilent's 62 gigahertz oscilloscope, which is a... Which...

**Dave Jones:** I assume that you got that from Bell Labs.

**Shariar:** No, no, no. That's directly loaned to me from Agilent. That's not... That's not from Bell Labs. Yeah, yeah. No, I would not... I would not take that from... I wouldn't take that out of the building. That's a half a million dollar equipment.

**Chris Gammell:** Yeah. Oops, I dropped it.

**Shariar:** Yeah. So, yeah. So, you know, it's a... Every time, even if you ever see gear that, you know, is really, really high end, it's directly loaned to me by the manufacturer. Yeah. Yeah. It's never from Bell Labs.

**Dave Jones:** But you've got the contacts in them to go, hey, you know.

**Shariar:** Yeah, they know me and, you know, they've seen videos and obviously they know the kind of work that I do. So, they don't mind, you know, loaning it to me for a really, really high end gear. Obviously, I can't hold on to it for three months, but I can hold on to it for a couple of days. No, no, that's right. Because even just to rent a 62 gigahertz, half a million dollar scope for a week, it will cost you 10 grand. Holy crap. I know. Totally.

**Dave Jones:** Yeah. At minimum. Yeah, at least. And some people have asked me, oh, why don't I get a scope like that here in the lab? I'm going, well, there's probably not even one in this country. You know, like, these things aren't just left lying around the, you know, the demo showroom floor. No, no.

**Shariar:** I mean, it's a very, very specific, extremely specific application. There's really very few places where you would need a 62 gigahertz or 100 gigahertz of stiloscope. I mean, the only reason you would ever pick up a 100 gigahertz of stiloscope is because you're doing study art, up-electronic experiments. Yeah.

**Dave Jones:** And they wouldn't even keep it in stock. They were, you order one and they'll build it for you.

**Shariar:** Yeah, absolutely.

**Dave Jones:** You know, that's, I think that's how it works.

**Shariar:** And that's another example of, for example, somewhere where three, five technologies come into play. So the 62 gigahertz scope from Keysight, it has a front end, which they call real edge, which is their frequency stitching, their own frequency stitching stuff, which they talk about in the data sheet of the instrument. That's a three-five technology component. Yeah. Yeah. Right. Oh, okay. So they make, you know, a hundred of them and then they measure them and maybe one or two of them will fit what they're looking for. Oh, interesting. Yeah.

**Dave Jones:** That's why these things cost, yeah. That's why they cost half a million bucks.

**Shariar:** Because you don't need to make them for volume. You make one or two, you know, every couple of months maybe. And then these things take, I mean, the calibration, the factory calibration of that scope must be, you know, maybe 10 hours. I know. It must be insane.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Wow. Do you think that that'll change in the future? So like, I mean, I see all these scope makers, they're all moving up market in terms of like, you know, everybody's going to higher frequency stuff. But like, do you think that as someone working on millimeter wave stuff, is the general technology moving all that way too? I mean, are there going to be necessary for more, is it just going to continue to spread or will the bulk of people keep moving up in frequency to need those kind of higher end scopes?

**Shariar:** Well, so the scope is an interesting thing because there is, you are fighting physics at some point. There is an issue of ultimately running into a jitter noise floor of a sampling system. I mean, you can, there is a very simple equation that relates jitter of a clock of a converter to the maximum effective number of bits you can ever achieve. I mean, if you don't have the jitter, you don't have the bits. End of story. And it's like, it's almost like the Shannon's limit, you know, you have to create, you have to be able to create, or you have to be able to de-imbed that jitter somehow by having some correlated source and so on. It's very complex. So you will run into some floor. This rapid move that you see in scope performance is happening because ASICs around 5 or 6 or 10 gigasample per second are becoming more and more common, especially in CMOS because you can make very sophisticated, dense calibration algorithms and mechanism in a CMOS process and then you can make ADCs using that. But once you're talking about, you know, 160 gigasample per second or 240 gigasample per second, like LeCroix stuff, those are really, really, really specialized. But anyhow, once you hit 110 gigahertz bandwidth, then you are out of connectors type. You are at a one millimeter connector and that's that. The only way you can go higher, you can maybe go to 140 gigahertz by using that proprietary Anruitsu 0.8 millimeter connector, which is supposed to have 180 gigahertz coaxial bandwidth. But let's put that aside. At 110 gigahertz, your connector, one millimeter connector is no longer 50 ohms. You hit the mode of the connector. So you hit the mode of the connector. So now you don't have DC to 110 anymore. Yeah, you can make, you can start digitizing things in bands of frequency. Now you would go from 110 to 170, which is a D band. But, you know, the question is why you just, why don't you just find a way to down convert that back down to the, yeah. So it really, I don't see, I'm sure they'll find, I'm sure there's something will come up. If I could digitize 110 gigahertz or 200 gigahertz straight up by an A2D converter, I mean, that's, that's insane, right? What we're saying is that you can connect. Even with the Agilent 62 gigahertz coaxial, what are we really saying? We're saying that you can take a horn antenna or an antenna and connect directly to the scope input. And then you can receive 60 gigahertz radio straight up with nothing else, right? That's just crazy. If you think about it, 10 years ago, people would have laughed at you. I know.

**Chris Gammell:** Well, and that's what I'm thinking though. Like maybe in 10 years we'll listen to this and be laughing. I mean, maybe, I mean, obviously there's some limits there, but maybe there's other things, right?

**Shariar:** Again, because some, some physics are at play here. So yes, you're right. It will get better. It will get cheaper. That's one thing, right? It will get, become more accessible, more available and perhaps, you know, higher and higher at some point. But there is going to be, again, this is also driven by finance too, right? There has to be somebody who needs it. That will make sense. Remember these scopes, the 100 gigahertz scopes or so on, they're intended for optoelectronic for broadband application where you need to receive DC to 110 at the same time because you have a fiber channel that supports that kind of data rate and so on. Now, that's, that's the drive. That's really one of the main reasons why they're making these things. And if you look at Bell Labs regularly publishes papers with a state-of-the-art oscilloscope. Every time a new oscilloscope comes out, Bell Labs has a new paper showing, you know, a next highest ever achieved data rate through fiber. Why? Because now they can receive it before they couldn't receive it. That's really the limitation because transmitting is a lot easier than receiving.

**Chris Gammell:** Right. Right. You can be throwing garbage to the universe. You just don't know what you're doing. Yeah.

**Shariar:** So to generate 100 gigabit per second is very, very different than to receive 100 gigabit per second. It's a very different problem. So as a result of that, that's why every time a new scope comes out, there is new publications in that field is because people can now actually do it. But whether it's going to go above that, you know, the connector is an issue, the market is an issue, the physics is a problem. But even then, even now, you know, I have to admit, thinking that 100, 200 gigabit per second was going to happen so quickly, I was skeptical. Yeah. Especially because I built millimeter wave data converters when I was a student. That was my thesis. So I appreciate the remarkable complexity and the extremely impressive accomplishment that's gone into it.

**Dave Jones:** If you're talking general purpose scopes, then they're always going to be limited to 500 or one gig. Why? It's the probing solutions, right? Passive probes that people are so used to, like, you know, 500. You can get ones that go to a gig in a passive scope. But then, you know, like, it's just, no, it's, you know, just for your average general use, you know, even if the technology is there, they're still going to be limited to like 500 or one gig.

**Chris Gammell:** Just because you need to get like sub 10 gigahertz kind of probes in and stuff and crazy.

**Dave Jones:** Well, you've got to go to your active probes or your handmade probes, right? Your custom made probes for your, you know. So, yeah, and people don't want to do that. People just want to use their general purpose scope. So, you know, it doesn't matter how good the data converters get and everything else. Okay, you might be able to have a two or three gigahertz bandwidth front end scope. But, you know, like, what's the point for general use unless, you know, unless you've got the, unless you're able to probe signals with it.

**Shariar:** Yeah, yeah, that's basically a limitation. And, you know, the way people tend to sometimes get around that issue is by creating scopes where they say, you know, up to a gigahertz or up to 500 megahertz or so, you're a passive probe. But if you want to go more than that, we're going to switch to 50 ohm. Yeah. And now you have, now you can use connected active passive probe and you need an active probe. But yeah, I mean, there's only so much you can do. Again, that's, you know, this physics is time constant. There's nothing you can do about it. You're stuck. No, exactly. Yeah, you're stuck at 500 megahertz. So, it doesn't matter how fast the technology changes. It's a matter of physics.

**Dave Jones:** But I think, like, we're already seeing that scopes, you know, they actually design the front ends for 500 meg and they sell them as a 100 meg software limited bandwidth scope. You know, it's like we're already seeing that.

**Shariar:** Yeah, I mean, Agile and Keysight is famous for that. They built their scopes. Essentially, there's only one hardware they sell. And they sell keys, licensed keys that can cost, you know, 50, 100, 200, even thousand dollars to unlock a feature that's already there in hardware.

**Dave Jones:** Because it pays them to do that. Like, within the last 10 years, we've seen a shift from, okay, it was difficult and expensive to roll a 500 megahertz front end to actually manufacture one. Now, it's like, you know, anyone can buy chips from, you know, anyone can almost go out and design their own 500 megahertz front end scope. Yeah, I mean, because... You know, using just chips you can buy from mouse or a digi key, right? It's, you know... Yeah, nowadays, it's... It's not that hard.

**Shariar:** Yeah, exactly. And it makes sense for them to have one type of hardware. It's cheaper to develop, cheaper to produce. They have one part number, one bill of material, one design, one PCB. Yeah. And then they just do that. And then they just say, you know, yeah, we may sell, let's say, the one gigahertz model at a 5% loss or breakeven. But when we sell the 8 gigahertz one, we'll make enough to compensate for the whole thing. And the whole project has profit. That's kind of how it works out at the end of the day. Yeah.

**Dave Jones:** And it means the smaller players, Rygold and, you know, those that are up and coming, they can design, you know, the chips are out there. Because they don't roll their own custom silicon. They're just using off-the-shelf devices like anyone else could. I mean, anyone else, anyone in theory can come along and design a Rygold level, you know, 500 megahertz scope, for example. Yeah, it's all off the shelf. All the parts are out there.

**Chris Gammell:** Yeah, it's all off the shelf. Well, we were talking a little before the show about that too, right? I mean, Shari already said that you liked how that's kind of opening up the market too and kind of accessibility, stuff like that.

**Shariar:** Yeah. I mean, it's always, again, it's always good to have manufacturers like Rygold or Siglent or other people in the same ecosystem space to do that because it does two things. A, it makes cheaper instruments available. And it gives the higher guys a run for their money. Now, they have to either drop their prices or do something to stay competitive in that space, right? And this is, of course, as long as manufacturers are fighting each other, it's good for the consumers. It's a known fact. So, you know, let them fight. It's a good thing. It's a good thing. Yeah.

**Dave Jones:** Even five years ago, you know, like it's unheard of the scopes that you can get these days for the price that you couldn't get five years ago, let alone 10 years ago, you know? And in the scheme of things, that's not a long time.

**Shariar:** I know. I was cleaning up the lab the other day at work and I was just throwing away all these old scopes, you know, the CRT scopes. I was like, oh my God, you know, these things must have cost a fortune at the time. You know, remember those gigantic Tektronix mainframes, those huge, huge ones with a lot of like... The 5,000 and 7,000 series. Yeah, but you know, they have to throw those away and recycle them and so on. I'm like, wow, these things must have cost a fortune now. That David like go dumps it out in there. Yeah. Yeah. They're too old actually even for, I think, even for... They're enormous. I mean, this thing is like the size of a stove. Oh, yeah. Where are you going to put that?

**Chris Gammell:** Eat your house.

**Shariar:** Yeah, it would eat your house too because it's just that thing must burn so much power.

**Chris Gammell:** Yeah. Nice and linear there, right? Oh, goodness. Yeah, yeah. Nice and linear there.

**Dave Jones:** We were talking also before the show about your publications, which we'll link in. Yeah. But we can only read the abstracts. And you were saying before the show that you don't hold the copyright on these anymore. You effectively give that to the IEEE. Yeah. Can you tell us how that works, how you're affiliated with the IEEE and how they get your content?

**Shariar:** Well, of course, I'm an IEEE member myself and IEEE Solid State Society member and so on. IEEE is a non-for-profit organization. As far as I know, I hope I'm correct about that. They're non-for-profit.

**Dave Jones:** I think you are correct.

**Shariar:** Yeah, but that doesn't mean they're non-for-profit. It doesn't mean they're non-profit. They still probably make money. Of course, yeah. There's a difference. And they do.

**Dave Jones:** They have to stay viable. Yes. They've got to run by. And they employ a lot of people. That means they have to make a profit.

**Shariar:** Yeah, and they employ a ton of people. And every time there's a conference, various conferences that I attend, like the ISCCC, which is the biggest one in my field, or SISICC, where I'm the chair of one of the millimeter wave and terahertz sessions, or RFIC, and so on. These conferences are all associated with, connected to IEEE. So they live in the ecosystem of IEEE in one way or another. So because IEEE is essentially responsible for distributing journals and publications, contents, once you publish something with IEEE and then have it show up on their system and then take care of everything, you give the copyright of the paper to them. You're giving, obviously the work is yours. And they're not giving away the work. Just the publication, the paper itself, the right of that is there. So I believe that if I were to put my own papers on somewhere where people can download the whole content, I believe I'd be violating some IEEE regulation, if I'm not mistaken. I don't think I can just do that. Yeah, so you have to be an IEEE member. But if you're not an IEEE member, if you're a student, you have to be an IEEE member. First of all, it's really cheap for students. And also, it shows up once you graduate how many years you've been an IEEE member. And that's an important thing. If somebody comes along and they're trying to hire you and they look at your resume and say, well, this guy's been an IEEE member for 10 years and he's just coming out of university, that's good. That's impressive. It means that right when you started your undergraduate degree, you already had a vision of what this whole ecosystem was about.

**Dave Jones:** I lost that because I used to be a student member way, you know, 20 years ago. Way back, folks. Back in the day. Yeah, way back. And then, yeah, I just didn't bother. And then I only joined again the IEEE like, you know, seven years ago or something. Yes, yes. You know, so, yeah. So, my little card says, yeah, you're only a seven-year member, you know.

**Shariar:** Yeah, it's okay. I mean, that doesn't – it's still seven years. It's still quite a long time. I think 10 years, depending on, I think, the publications and so on, you have to be an active researcher. But then you can become a senior member and so on. And then there's also IEEE Fellows, which is a whole different story, becoming one of those. But, yeah, I mean, it's – and you're – for – depending on which magazines and so on you subscribe to, it's a different price. It can be pretty expensive. You know, I think I paid something like $250 a year or something to be a member.

**Dave Jones:** Yeah, your basic subscription to IEEE without any of the, you know, any of the optional, you know, mags, you know, like the – what's the correct term? The journal papers. Journals.

**Shariar:** Journals, yeah.

**Dave Jones:** Journals, journals, right. Yeah, you can join – you know, they've got like 50 different, you know, journals you can sign up to. Yeah, the basic price is like 100 – I don't know, 120 or 150 a year or something. Yeah, yeah.

**Shariar:** It's, you know, still not that, but less than $10 a month.

**Dave Jones:** Right. So they – is there any other place you would publish anything?

**Shariar:** Besides IEEE?

**Dave Jones:** Are there any other journals?

**Shariar:** Yeah. No, I don't think so. I mean, for – you normally – typically, in my field at least, the way it works is that we generally publish something at a conference. Right. And if, you know, if the paper is well-received and it's good technical content, then it gets typically invited for a journal publication. And that can either be a journal publication at the Solid State Circuit. Oh, okay. Right.

**Dave Jones:** So it's a two-step thing. Yeah, usually. So you can't go straight to journal? No, you can. No, you can.

**Shariar:** You can submit your work directly to the journal. Right. Sometimes it's advantageous to be invited because the review process for a journal when it's invited is typically a little bit shorter because there's a deadline for where the special issue of the journal comes out for that particular publication for the public conference. So it's a little bit faster. But because this is a very involved review process, you know, you submit it and it's heavily peer-reviewed. It gets sent to, you know, several experts. They read your paper and they grill you on it and they send you all their questions. Really? Okay.

**Dave Jones:** So, but what I've always wondered about is what if you are the expert on it? Who is going to peer review you? You know, if you're at the bleeding edge, who is going to?

**Shariar:** It's almost, yeah, it's almost impossible to be the only person that has an expert at a particular topic. But even if you're not an expert.

**Dave Jones:** But how many people have they got willing to be peer? Oh, they ask.

**Shariar:** They ask, you know, usually what they do is they ask people who are famous in that research or they ask people who are referencing the paper. I have done many, many paper reviews myself. Yeah. So I get, you know, requests from the editor of the particular journal if I want to review it. And then I have a timeline to review it. And then I have to write all the questions and so on. Obviously, the person who wrote the paper doesn't know who I am. They don't know who the reviewers are. Of course. It's not double blind. It's only half blind, I guess.

**Dave Jones:** So is this a paid thing? Do they pay you to review the paper or is it just you do it because you're part of the society?

**Shariar:** Yeah, you do it because you're part of the ecosystem. Yeah. No, it's not paid at all. And it is thing. The reviews take quite a long time too. It's not something you do in 10 minutes. You know, it's hours and hours because you really have to understand what the person has done and look into it. Because this is a scientific endeavor, essentially. You want to make sure that the science is correct. That's the whole point of the peer review. So you have to be very critical and be very careful about what's out there and what people are saying.

**Dave Jones:** So if you've got questions, do you funnel it back through the IEEE and remain totally anonymous or would you contact the author? No, no, you don't contact them. Say, I'm a reviewer. No, you don't.

**Shariar:** Because the author is never supposed to know who the reviewer is. But you type your questions and you submit it to the editor of the journal. Yeah, he or she will take care of it.

**Dave Jones:** And they would be full-time employees, the journal editors, I would assume. It would be a lot of work.

**Shariar:** Well, the editors rotate around. They're not employees. Typically, they're professors or professionals and so on. Oh, okay. I've never been an editor myself. It's actually quite a lot of work too if you are...

**Dave Jones:** I was going to say, I'm assuming that would be a paid position somehow. I don't know. I wonder. Or is your university expected to allow you time? It's like, yeah, you have to go to jury duty. Okay, you've got to go to... You've got to spend some time peer reviewing or being an editor.

**Shariar:** I'm pretty sure that professors at universities are granted and, in fact, encouraged to be. I mean, to be an editor of, let's say, Journal of Solid State Circus for particular issues is an honor.

**Dave Jones:** Yes.

**Shariar:** Yes. Yeah. Totally. That's quite an accomplishment.

**Chris Gammell:** Another feather in their cap as well. Yeah, absolutely. I don't know. How do you feel about the whole publishing? I mean, because I read a lot about... Obviously, I've never done it. So, that's my big, you know, disclaimer. Same. But how do you feel about the whole process? I mean, maybe it's different with this kind of stuff, but some of it seems like the publisher parish kind of model seems like it's kind of constrained and forced. Has it worked out well for you or what's your take?

**Shariar:** Well, for me, in terms of my performance from my work, obviously, publications are a good thing. But, you know, sometimes the model for the company changes a little bit and there's more product development in mind. And as soon as things become product development, then you're not really allowed to publish. I have a lot of work right now that, unfortunately, I cannot publish because they're secret or they are product-oriented and we don't want to give away the secrets in a way, right? So, then I can't publish, even though I really like the idea of publishing. I like the idea of being involved in that. So, I have been, unfortunately, a little bit out of the picture in the last couple of years because of that. But hopefully, I'll have some new stuff coming up later. But in terms of one of the things that I sometimes don't like is that sometimes because having many, many publications tends to be important, people break up a work. Into many papers. Even though it's supposed to really be just one paper, you know? Yeah, yeah. Like that phased array. I can get five out of this. Yes! And sometimes it works like that. You know, like my other work, the phased array chipset. Yeah, I probably could have written three or four papers with it. But, you know, we just wrote one. Because, and I think that people do recognize that, you know, they pick up a paper and say, wow, this is really a complete system. And there's just one paper and it's everything. And it works, right? That's impressive that people do pay attention to that. But it's sometimes, occasionally, they can become a games number, a numbers game. So, then, you know, you have 300 publications or 200 publications. And there are, by the way, people in my field with that many publications where each publication is something important. So, don't get me wrong. Oh, yeah, right, right. Yeah, yeah, of course. There is no shortage of brilliant researchers in my field, that's for sure. And so, yeah, that's definitely possible. But sometimes people break it up.

**Dave Jones:** Is there, you mentioned like the, sometimes the pressure from, say, Bell Labs, for example, for, you know, keeping things secret because this is going to be a commercial thing or whatever. Is there a temptation for a company like Bell Labs to sort of fall into the trap of, well, everything is secret and then not publish damn well anything because they get so paranoid that, oh, this could make us a buttload of money so we won't publish it.

**Shariar:** Yeah, I mean, they have to strike a balance between being, to maintain their presence in research and generating ideas where they are in the system all the time where they are at the top of the page. Yeah. And creating a situation where you are developing products where end up being, you know, something very valuable for the company. Sometimes papers from the industry tend to read like data sheet, which is kind of annoying. Oh, yeah. Where it's just like here, you know, here's what we got. I'm like, that's great, but how did you do that? You know, that's what. How did you do it? That's over the sauce, man. Yeah, that's what I wanted to see. So sometimes, and I understand why they do that. It's not like the person who wrote the paper necessarily says, oh, I'm not going to share this. It's because they can't. And sometimes, even when I write papers, sometimes I have to hold back some detail because, you know, otherwise it won't be released. Otherwise, the people in the company who look at it, it's like, oh, no, there's too much detail. Yeah. Yeah.

**Dave Jones:** And I was going to say the cynical side of me says, well, that means that always only the dregs are going to get published. All the really cool shit is going to be kept secret. I don't think so, Dave.

**Chris Gammell:** We're looking at a list of his papers here. These are amazing.

**Dave Jones:** Yeah, yeah, yeah. But I reckon there's some ultra cool stuff beyond that that he's not releasing.

**Shariar:** Yeah, I mean, compared to some of the other people doing Mini-Meter Wave, especially people in university, you know, my publications is tiny, tiny. There are some of my supervisors, my professors from, you know, the University of California, UCSC, and other people, they have a long list of incredible – their students obviously do the work, but they're the supervising entity. They're the leader.

**Dave Jones:** Ah, so their name gets up in lines.

**Shariar:** Yeah, and they are, of course, driving the ideas and constantly monitoring and supporting and creating, generating ideas with the students too. And they have tons of really amazing, impressive, impressive work. It's no shortage, like I said, no shortage of – there's a really good – even though I say that there are all these amazing people out there. Christopher Hitchens once said something that I think is brilliant. He said that even though I have met many, many people much smarter and more intelligent than myself, I have never met somebody who can say differently. And I think that's brilliant. Just essentially saying that, yeah, there's always brilliant, brilliant people out there, but no one's ever brilliant enough to not say that statement itself. Right. Yeah, it's a pretty nice way of putting it. But yeah, there's lots of great, great people whom I learn from continuously, and that's one of the reasons of being part of the IEEE is so important, because you stay up to date with the latest publications and ideas. Right. You don't reinvent the wheel. Otherwise, you end up reinventing the wheel.

**Chris Gammell:** Do you ever see people that are going to the – so did you say the – is it the ice cream conference? Is that the one that you go to, the ICSS or whatever it is?

**Shariar:** Yeah, I go to a couple of conferences. The ISSCC, that's one of them, the International Conference of Circuits and Systems Society.

**Chris Gammell:** Yeah, isn't that called ice cream sometimes? Do people call that? No? I don't know.

**Shariar:** I don't think anyone's ever called it that I know. But I'm going to start at that.

**Chris Gammell:** Well, there's some kind of acronym that looks like that, that someone called it the ice cream conference. That's why I called it that.

**Shariar:** I don't know, but from now on, that's what I'm going to call it. But yeah, there's that. There's the RFIC, which is a radio frequency integral circus. There's CISIX compound semiconductor circuits and systems and so on. Those are the main ones that I attend, which are all circuits conferences. And then there's conferences that cover more systems. And then there's conferences that cover optics and so on.

**Dave Jones:** So how many people would turn up to these – how big are these conferences?

**Shariar:** Well, some of them are something like the IMS conference. The IMS-RFIC combination has several thousands, you know, 5,000 maybe.

**Dave Jones:** Oh, wow.

**Shariar:** Some of their conferences are much smaller. That's huge. Like RIFIC and CISIX, for example. CISIX would be maybe about 250, 250 people. Yeah, depends. ISS is pretty big, several thousand also, 4,000 or 5,000 also.

**Dave Jones:** Now, would people actually rock up and show off their hardware? Check this out. Whip it out on the bench. Or is it just death by PowerPoint?

**Shariar:** There is definitely some hardware sometimes being demonstrated. But because these are all circuit conferences and they're all ASICs, there's really not much to show sometimes. But yeah, at IMS conference, there is an enormous industry show, which I think you would absolutely love. Because all this state-of-the-art instrument from every manufacturer is there. Yeah, yeah. Yeah. That's pretty awesome.

**Dave Jones:** Test equipment pool. Oh, my God. Yeah.

**Shariar:** I mean, you can spend four or five days just doing that.

**Chris Gammell:** That's awesome.

**Dave Jones:** Wow. Fantastic.

**Chris Gammell:** Can we hear a little bit more about some of your papers here, too? Because so you've shown some of these off at the conferences and stuff. But what are some of these used for as well? So we talked a little before the show about the phased array. And I mentioned that Greg Charvat, who we've had on the show, does some phased array stuff, too. But what is all this stuff?

**Shariar:** Well, like I said, I've done different things for different applications. I mentioned, let's say, the 160 gigahertz PLL that I did a while back when I was a student. That was potentially used for something like a medical imaging system, where at 160 gigahertz, some interesting properties come to play, where you can image tissue material, and you can find hidden weaponry and things like that by using millimeter wave images, which I'm sure you've seen at airports and so on. So that's that kind of application. The phased array stuff is interesting because essentially the idea of a phased array is a system where you can steer a beam, a pattern, by combining it in the air at a particular way. So it's basically constructive-destructive interference. And you can have an array, a grid of antennas, for example, and by spacing them and delaying the signal that gets into each of the elements appropriately, you can create constructive-destructive interferences in a particular way that you want, and you can actually have the beam to point in a certain direction, even though the antenna itself is not pointing in that direction. Yes. So why would that be useful? Well, there's many, many different reasons why. But let's say you make a phased array system of a mobile device, and then you're moving around, and you want the beam to track you so that you always have signal strength no matter where you go. Because at some of these higher frequencies, the attenuation and the signal losses are so large that you have to always be pointing to the person. Otherwise, there's no signal. There's no... So there you can use, for example, a phased array when a moving target is involved.

**Dave Jones:** And this works anywhere from ultrasonics. And I've done this at around about 1 meg, which is an underwater steered beam sonar system. And you can do this up in the hundreds of gigs.

**Shariar:** This is a wave property. So it will work at any frequency. The reason I work at 90 gigahertz for the phased array, where the carrier frequency, the RF carrier frequency of the signal is at 90 gigahertz. That's 9.0. The reason is because at 90 gigahertz, your relative bandwidth that's available to you to occupy the signal is much larger than it would be at 2.4 gigahertz. In 2.4 gigahertz, you're crowded with channels of different types of communications. So at 90 gigahertz, it's essentially quiet. There's nobody there. So... Why 90?

**Dave Jones:** Why not 80 or 70 or 50?

**Shariar:** All of those have applications. So 71 to 76, 81 to 86, for example, is a band called the eBand. And it's a recently opened band, reasonably recently opened band, where you can do telecommunication at that band. 60 gigahertz is an available, reasonably hot topic. And there have been products in there too. 60 gigahertz is interesting because 60 gigahertz starts interacting with water molecules in the air. So the loss is very high. So 60 gigahertz is good for short range. If you want to flood an environment with a whole bunch of different people communicating at 60 gigahertz, you can without them interfering with each other too much because the loss is so high. So people build systems there.

**Dave Jones:** So very, very, very short range. We're talking like meters or something like that. Yeah, meters, exactly.

**Shariar:** I mean, not that people do build 60 gigahertz systems for a long range with very high gain antennas too, but the loss is quite high. Right. So that's the advantage. So at 90 gigahertz is another interesting frequency because, again, it's open. It's losses are actually quite low at that frequency compared to 60 gigahertz. And you can do a lot of bandwidth. You have a lot of bandwidth. It's free space. It's a military who likes to use that because it's secure and so on. And that's the kind of reason why we went. But the paper targets really, really high bandwidth wireless systems. So where we send 10 gigabit per second through the air using a phased array at 90 gigahertz. It's just to show, demonstrate, look, you can do this. And this is with a complex constellation. This is a QAM, 16 QAM or 32 QAM constellation. So it's reasonably spectrally efficient. And that's kind of targeted for that. That's all wireless stuff. And then other things that I've done in the past that might be interesting is things like retimers and receivers for optoelectronic industry is that when you want to send data through a fiber channel, for example, you could use just digital ones and zeros, right? Very basic one zero serial data. So you can imagine what goes through USB, which is a differential serial data. I imagine that now going through light, through a fiber. And then you can put a crazy amount of data through fiber because the bandwidth, the optical bandwidth of fiber is so huge. How huge is it? It would be easily hundreds of gigahertz. But it depends on how far you go. Because if you go really, really far, just like anything, you get dispersion. These wavelengths start to separate from each other. Yes, that's right. So you're right into other problems. But compared to a copper wire, fiber is almost lossless.

**Dave Jones:** So fiber is still the best medium. I have a copper, air, wet string, anything. Fiber is still the best.

**Shariar:** No, but now I'm tempted to go and measure the S parameters of a wet string that you mentioned.

**Dave Jones:** String, I know. You've got to do a whole paper on it for the April edition, for the April edition of the journal.

**Shariar:** Yeah, it would be, that would put me on the map. So yeah, fiber is definitely, it would be the lowest loss. It's certainly, by far, I mean, you can go, you know, obviously thousands of kilometers.

**Dave Jones:** Lowest loss, yeah, lowest loss and widest bandwidth?

**Shariar:** Yeah, it is, it is the low, yeah, it's the lowest loss, widest, especially because fiber is not, I mean, fiber is not line of sight. So it's even more advantageous. We put it under the ocean, right? It goes 3,000 kilometers. Yeah, yeah, that's right. Not that those systems are not. That's how we're talking about Dave right now. Yeah, exactly.

**Dave Jones:** Yeah, but they have repeaters, like they, it's not a single fiber that goes 3,000 kilometers, right? They have repeaters every 10 Ks or something.

**Shariar:** Yeah, I mean, they have to, they have optical amplifiers, EDFAs in the way, they have repeaters where they go back to electrical, they do equalization, they do error correction and they retransmit. They have to do those things if they want to make it, you know, in those long, long, long distances, just long haul links.

**Dave Jones:** How do they get, I know, how do they get the power down there? Because like I've worked on 10 kilometer towed array systems and just getting the power down to all the modules, right? You know, I've actually modeled, you know, the transmission line, like the actual power transmission line system. And it's, you know, just for like 10 kilometers is complex. I can't imagine, you know, 3,000 kilometers.

**Shariar:** Yeah, I mean, they send, basically they send the power with the fiber, right? The cable that they've put, as for in some of the instances that I know is, the cable they put under the ocean is not just a tiny single fiber, obviously as many jackets and protectors and so on. Sometimes they send the power with the cable. So the power can make 3,000 kilometers because you're not sending data over the power line. So that's easy. Yeah, obviously, right? And then so that you can power the EDFAs, amplifiers and repeaters along the way to do that. But you can imagine if something like that breaks, it's a massive, massive problem.

**Dave Jones:** Yeah, but that's what I'm saying. Even to send the power that distance is a pain in the ass, trust me. It's like a difference, but like weight. But they don't have to care about buoyancy, I guess, whereas we had to care about buoyancy. So there was a trade-off between your power consumption versus the weight of your copper to carry the power, you know? And it was like, whereas these ones just sink to the bottom, I guess.

**Shariar:** Yeah, they go and they're well-protected. But, you know, the ships that carry those wires back, those things are enormous. And as they go forward, they obviously unload the cable on the bottom of the ocean as they travel across the ocean. And they have to take in water. Otherwise, the ship is too buoyant without the weight of the cable. They'll just topple over. Oh, really? Exactly. I know. Yeah. Yeah, it's a crazy, crazy investment. Again, it's money-driven, right? It pays to do that. So they do that. We do anything that's money-driven. And sometimes money is fear-driven, but mostly money-driven. Yeah, right.

**Dave Jones:** Is there anywhere else you would rather, like you dream about working? Well… Or is Bell Labs sort of like the pinnacle worldwide of, you know, this sort of stuff that you're working on?

**Shariar:** Well, there's… One of the things that I've also wanted to do is just to be a full-time professor, to, you know, do research at a state-of-the-art university and, you know, have students and so on. That's also a really, really interesting and exciting endeavor for sure. And one of the reasons I chose Bell Labs is because it is in a way similar to that. And also, to get a professor position at one of these great universities that does many-middle research is extremely difficult. I mean, it's almost impossible. The people who work…

**Dave Jones:** Oh, okay. It's that because the standards are so…

**Shariar:** Yeah, but it's extremely competitive, right? It's extremely…

**Chris Gammell:** Yeah, it's like a pyramid scheme, right? Where it's like there's only so many professorships at the top. Yeah, I mean, I have many professors. Lots of grad students. Yeah, exactly.

**Shariar:** So you don't need them. And then they're very, very good at what they do. You know, so, yeah. So that's one of the reasons. But I always kind of joke about this is that if I ever won like a ridiculous lottery, something like, you know, $300 million, something ridiculous, something that is Powerball, whatever it is in the US that they have… Not that I play the lottery, by the way. Don't play the lottery.

**Dave Jones:** No, play the lottery. Scientist speaking. Chris and I, no, no. I don't play the lottery. If you guys don't get it, you're not buying the odds. You're buying the dreams. Yeah, of course.

**Chris Gammell:** Whatever, Dave.

**Dave Jones:** You see, each week I can dream about it. You guys can't, right? Because I'm in it. Whatever, man. You guys can't even dream about it.

**Chris Gammell:** I buy a dream every time I buy a beer. That's what you're buying.

**Shariar:** Yeah, that's true.

**Dave Jones:** No, no.

**Shariar:** I mean, of course, I understand that it's an entertainment value from the experience. There's no doubt about it. But, you know, there's statistics that you know better than anyone what the odds are. Of course.

**Dave Jones:** Right. I know the statistics. Yeah, yeah. Of course. I'm not buying the odds. Yeah, of course. I'm buying the dream.

**Shariar:** But I was saying, yeah, anyway, if I do win something crazy like that, or I had that much money, I would open a research center. I would hire, you know, great researchers. Cool. And I would tell them, do whatever you want. And, you know, pay them very competitively to all the other places. Just make whatever you can make. And then whatever you can make is now available for free to humanity. Everybody. Do you think that would work? Do you think that would... I am sure somebody will find a way to... It works until the money runs out.

**Chris Gammell:** No, no, I just mean like the... I mean, because, no, the motivating factor. I mean, that's really interesting. I would love that idea. I think that would be really great. But I think that that's always interesting, too, because I think Bell Labs, historically, right? I mean, like, there was a ton of innovation there, but it was also lots and lots of money behind it as well. And it was scale as much as anything else, right? I mean, like, that was...

**Dave Jones:** But they didn't just give it to humanity. Yeah. I mean, it was patented. And, no, yeah.

**Shariar:** Yeah. But I think that the problem that you may run into a scenario like that is that I think other manufacturers and other companies that do this will complain that you're playing an unfair game, in a way, because you're putting them out of business in some way. So, yeah. Right. What I'm saying is extremely idealistic, right? Well, top.

**Chris Gammell:** Of course. Of course.

**Shariar:** Yeah. Top. I love it. I think that's great. I mean, what I'm saying is so quesatic and so idealistic. It's just obviously has tremendous... Yeah. Yeah. No, I was more asking about the...

**Chris Gammell:** No, more the human nature aspect of things. I mean, like, kind of more of a question of what drives us and stuff like that. I think that, you know, people like you are very driven by curiosity, right? But then there is always that money aspect, right? That's still part of it. I mean, that affects all of us, I think. So, it's just an interesting question.

**Shariar:** Yeah. And I completely appreciate the difficulties that goes into... The practical difficulties that goes into really, you know, just generating knowledge. Obviously, there's a lot of... It's nice to think about it in an idealistic way. But yeah, there's limitations. And I appreciate that.

**Dave Jones:** I think you would... Yeah. Yeah. The classic example here is the Bill Gates Foundation, right? Yes. And Melinda Gates Foundation, right? He's given away his, you know, $300 billion or whatever. But have you seen his corporate headquarters? It requires... They had to build a dedicated building. They hire thousands of people just to give away money. Yeah, yeah. It's very complex. It's actually that complex. It's that complex. Yeah, I know. You know? So, yeah. In the end, you might find, oh, geez, this is a... Started out as a good idea, but it's actually not practical because it's just so involved to organize all this research and give it away.

**Shariar:** Yeah, you know, sometimes I feel like... I get very frustrated with some of the systems that are in play, you know, especially in the United States. And I'm not sure if it's because things are getting worse, but I just simply know more of what is going on. And that's why it makes me frustrated. But just some of the decisions, you know, the government makes, some of the disparity in resources that's available, how much of the recovery that, you know, the United States has done has gone to the top 2% or 1% of the population. How the system is so well geared for really rich people to tell the middle class to blame the poor people. It's just so well oiled, you know, this machine is so well oiled. And I don't know if it's because I'm just becoming cynical because I know more about it or is it just really getting worse or is it getting better? I know that humanity is getting better, obviously, but...

**Dave Jones:** No, it's not getting better because you yank, sorry, Chris, but didn't you just pass a spending bill, a trillion dollar spending bill that on page, four pages from the end, it says we're going to allow people to put money into politics. We're going to increase that tenfold. That's crazy to me.

**Chris Gammell:** Yeah.

**Dave Jones:** And they just snuck it. Yeah. So now you can give almost unlimited money to the politicians to buy the system even further. So instead of scaling it back, no, it's getting worse.

**Shariar:** It's probably one of the worst things that's ever happened to the US politics is the idea of being able to... Oh, I mean... Money in politics, yeah. That kind of defeats the purpose because the whole point is not to have that advantage. I mean, I don't know, maybe I'm naive and I'm being simplistic, but come on. I mean, what did you expect was going to happen if you allow that? I mean, what did you think was going to happen? All these extremely rich, powerful people are going to say, no, we're not going to do that because it's unethical. Of course not. I mean, but anyhow, that's a whole different story.

**Chris Gammell:** Well, and it stinks too because I'm sure that you see the effects of funding then being... Because then on the other end, it's like if that money goes away, then that money doesn't go towards research, that doesn't keep pushing the industry and stuff like that as well. I think when you're in the research side, you see that as much as anything else because I have friends that work with the NIH and stuff like that. And one guy is just like, yeah, that money is just gone, man. And that drives a lot of progress.

**Shariar:** Yeah. I mean, if you look at it just fundamentally, again, I don't want to take this into a political direction, but if you think about it fundamentally, what is the main three things a society should do in general, right? It should be able to keep its people healthy for free. It should be able to educate these people for free. And it should not have its legal and prison systems for profit, right?

**Chris Gammell:** Yeah.

**Shariar:** I mean, those three decisions to how to run the society are fundamental to the health of the society. And none of those are true. I mean, it's terrible. So, and there are people, by the way, this is, I'm talking about just from my understanding of the US, United States system, but there are many countries who accomplish that quite well and they're doing quite well indeed.

**Chris Gammell:** I think you used to live in one.

**Shariar:** Yes, yes. I mean, exactly. That's one of the great things and many good places in Europe as well. And that's true. So, yeah, there you go. So, you have to appreciate the importance of those things for your people. I understand, again, these are very complex issues and there are no straightforward answers to them, but there should be a striving force.

**Dave Jones:** Well, there are, but except when you've gone down the path of no return. Yeah, it's very hard. That's when it gets complicated, which the US has.

**Shariar:** The thing about our species is that it's very hard to take something back once it's given. All right? It's very different to never give it, but once you give it, it's very hard to take it away. And this relationship is not both ways. It's not symmetric. It's a hysteresis there. So, you got to watch out for that. Yeah.

**Dave Jones:** I love it. Well, thank you very much for joining us. Of course. It was a pleasure. Awesome. Yeah. And for the record, how do you pronounce your name? It's Sharia. Sharia.

**Shariar:** Perfect.

**Dave Jones:** That's how I thought it was. No, it wasn't. Don't worry.

**Chris Gammell:** We will repeat what Dave said when he signed on. I don't even know. I couldn't even repeat it. Sharia. Yeah, that's what it was.

**Dave Jones:** Sharia.

**Shariar:** It's a silent H. Second H. Yeah, if you were to pronounce it, you know, strictly in the Persian accent and you pronounce the H. But, you know, I've given up on that a long time ago. Oh, okay.

**Dave Jones:** Right. Interesting. All right. So, how... No, come on. Tell us. How would you actually say your name in the Persian?

**Shariar:** If you were to say it in Persian, it would be Sharia. Oh, cool. Yeah. Ah. It's quite different. But, like I said, I've been called every possible pronunciation of those letters together.

**Dave Jones:** I've been called everything out of the sun, too. My name's easy.

**Chris Gammell:** So, you had mentioned the difficulty with finding potential hires. Yes. Is there any skill set that should contact you?

**Shariar:** Oh, yeah. I mean, I didn't want to use this to somehow benefit myself. No. Of course you can. We'd love that. Yeah.

**Dave Jones:** Like, are you after, like, maybe someone who's not a researcher? Do you need, like, lab assistants, technicians, that kind of stuff?

**Shariar:** Well, it's difficult for us to get a head count to be able to hire. So, we would like someone who has a PhD degree and someone who wants to do research. And, you know, strictly speaking, kind of, you have to have a PhD to join Bell Labs. But, you know, you can also have a master's degree. And that's also acceptable. But, yeah, someone who can do...

**Dave Jones:** A lowly master's degree, just like the Big Bang Theory. Poor old man.

**Shariar:** I don't mean to devalue the degree at all. I mean, bachelor's degree is also quite valuable. But it's just that because it's research. So, you have to have experience writing a thesis and doing research. That's really the reason for it. But, yeah, someone who can do high-speed millimeter wave design, high-speed analog circuit design, who has experience, you know, with set-of-the-art CMOS or silicon-jury medium process. Yeah, just high. Yeah, that kind of expertise.

**Dave Jones:** So, all those who have flashed a lead with an Arduino, apply straight away. You're right up there.

**Chris Gammell:** Well, no, I think another good question, too, is that you said you look at certain schools. So, which schools, if people were... I mean, because I'm sure that we have younger listeners as well that would be like, yeah, I want to do that. Where should they look? Where should they look for programs?

**Shariar:** I mean, my old university in Canada is a good one. Universities in the United States, Columbia University in New York, University of Southern California, University of California, MIT, all those places that have a millimeter wave, high-frequency analog ASIC design team. Those are all really, really good universities. Those are, obviously, I named the best ones. But there are many places that you can get your degree from and do high-speed circuit design, of course. It's just those ones are one of the main ones.

**Dave Jones:** I don't think there's one here in Australia. Well, I'm probably talking out my ass, but I'd be surprised if there is one. But there could be.

**Shariar:** I'm trying to remember if I remember a publication from, let's say, University of Sydney or something recently, but I don't remember.

**Dave Jones:** Maybe the University of New South Wales would probably be the only one.

**Shariar:** Yeah.

**Dave Jones:** Because they do lots of ASIC. Yes, yes.

**Shariar:** I know that you guys do a lot of system work. So there is papers coming from the system perspective. But from specifically ASIC design, it probably is. I just have to be familiar. I doubt it. Yeah. That would be my suggestion. But anyhow, no matter what you do, go in it with a sense of curiosity to have the learning be its own reward. Yeah. Don't think about the job and the salary and so on. Not that that's not important. Of course. Yeah. Go with that intention.

**Chris Gammell:** Yeah, man. Every day you don't learn, you're not alive.

**Chris Gammell:** There you go. You did. That's a great message. I love that. That's it. Cool. Well, thanks again. We really appreciate it.

**Shariar:** Thank you. Thanks for having me. It was a blast talking to you guys. All right. Thanks, mate. See you. All right. Take care. Bye.

**Speaker ?:** x x x
