---
episode: 721
title: Chip Design for Fun (and Waffles) with Julia Desmazes
url: https://theamphour.com/721-chip-design-for-fun-and-waffles-with-julia-desmazes/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released April 8th, 2026. Episode 721. Chip designed for fun and waffles with Julia Desmasis. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Julia Desmazes:** And I'm Julia Desmazes, and I build ASICs for fun.

**Chris Gammell:** Yes, and that is exactly what we're going to be talking about here. Julia, thanks for being here. I read your two weeks till tape out. It's going to be the top link on this episode. People need to go read it. They can be reading it while we're talking about it here, but also all the other things you're building. So ASICs for fun, how did we get to that point?

**Julia Desmazes:** Well, it's possible. There's been a silent and absolutely massive revolution that has made open source silicon actually possible. You've had a couple of guests on the show which have been absolutely instrumental to making this a reality and building up the stack to a point where random people can actually have all the tools, all the NDAs that are no longer NDAs accessible, and the ways of actually taping out their own custom silicon.

**Chris Gammell:** Yeah, that's wild. And one thing that you and I talked about before we started recording is that you are a user and dare I say, a advanced user of some of these open processes because you're building things that are, I mean, maybe at the limits of what some of these open MPWs are running and are available. Is that a fair assumption?

**Julia Desmazes:** I think I'm definitely one of the more advanced users. That being said, I hope to be pushing the limits, but I think there's more to go than where I am pushing it now.

**Chris Gammell:** Said like a person who pushes the limits, by the way. Yeah, yeah. No, no, no. Push further. Absolutely. You can do it.

**Julia Desmazes:** Exactly. We can push further, and I'm honestly really interested to see where this is going, but I definitely hope that I'm contributing to pushing it further and seeing just how far we can go with this.

**Chris Gammell:** Yeah. Okay.

**Julia Desmazes:** So a little bit of context. As I said, I'm Julia. I have a background in CPU design and RTL design, and I've been doing this professionally. Right now, I'm enjoying and taking full advantage of the OpenTour Silicon tools to try and make full custom chips for different accelerators that I think about that are kind of weird and kind of out there, and I'm doing this through the Tiny Tape Out program that McVern has been doing for the past few years, which allows random people to, for a very, very small cost, which is a big thing in ASIC design, be able to submit their own design and have some silicon area to work with, which is quite substantial and can be quite substantial in order to actually build things, and then in a couple of months, you get your ASICs back on your own death boards, and then you see if they work or if they don't work, and then you do it again.

**Chris Gammell:** I actually, so it's interesting pointing out the accelerator piece. I mean, that's what the Do We Still Tape Out was about, but when Matt has been on the show talking about Tiny Tape Out and Uri's been on the show too, it's like, well, we can make a, you know, like, how about this? When Matt's pitched me on doing it, he's like, you know, you can just make a counter and put that into silicon. I'm like, yeah, that's about the level I could do. So then let's scale from a counter to AI accelerator and maybe even define AI accelerator because I don't really get what they are. Like, I see all the Googles and the Microsofts and everybody making these things, Tensor this, blah, blah, blah, that. What is an AI accelerator in this context?

**Julia Desmazes:** So we're talking about the type of accelerator I did in the two weeks until tape outs. And essentially, it's something we call a systolic array, which is just a really interesting architecture, octro-chartel way of doing matrix-matrix multiplication. And at the end of the day, most of these AI accelerators are just really, really fancy matrix operations. And so the heart of it, the part that occupies the greatest area is going to be just a massive matrix-matrix multiplication. And then you have like some smaller units to do some other type of computation that you might also need, but that is really the heart of it. And so I'm not really building an AI accelerator per se, because there are lots of smaller parts that need to make it a true AI accelerator, but it's definitely the heart of it. Now, that being said, that two weeks until tape out, and this is something that I joke about in the article, I wasn't going to build an AI accelerator. Like the AI accelerator is just a sacrificial hardware to test the actual design, which is the G-tag. And that is so underwhelming for most people,

**Chris Gammell:** but... And yet we use it every day.

**Julia Desmazes:** Yet we use it every day. And I think it's interesting to take a step back and where we are in open source silicon for listeners here. Right now, we have access to the tooling, which has been started and really provided with something called the Open Road Project, funded by DARPA. Thank you very much, DARPA. And with people like Andreas Olsen really contributing to pushing that forward, we have Google's work with Tim Ansell that has provided us with PDKs, which are the cell libraries that allow us to say, okay, like this is an AND gate for a certain process node. So process node is like, if I go to this fab and I want these type of registers, I need the cell library to express like, okay, these are all the AND gates and these are all the OR gates and these are what the flip-flops looks like. And then a third part is actually being able to send that to the fab. And so for that, we have the tiny tape-out program with MadThern, but also the newer wafer space with Tim Ansell again, which both allows you to tape out chips, the wafer space being full chips and tiny tape-outs being like, hey, I don't want to commit to a full chip, but like the cheaper part of it. So now it's possible, but now we need some actual infrastructure to make it possible. There's a secret of chip design is that your first chip is always broken. It doesn't matter. It doesn't matter how much work you put into the verification. Everyone's first chip is a bust.

**Chris Gammell:** But you still hang it on the wall, right?

**Julia Desmazes:** Yeah, of course. You hang it on the wall like this is your first chip. Right, right. First child. You never do that to your first child. Okay, now your first child comes back and it's dead. Now that that's out of the way, you need to figure out what went wrong in silicon. And it's not like software. You can't put breakpoints there. It's crystal. It's done. And so for that, you need in silicon observability debug infrastructure. And so the two weeks until tape-out was actually building that in silicon debugging infrastructure. But now that you've built the debug infrastructure and you can plug in a G tag and inspect internal registers, you need something to inspect. And so I was like, hey, I've got 10 days because two weeks actually I procrastinated. So I've got 10 days. What can I build in 10 days? One of us.

**Chris Gammell:** One of us.

**Julia Desmazes:** Exactly. So I do not recommend doing this at work. This is a horrible timeline. This is not how chip design is supposed to be done. I was like, hey, I'm going to build the heart of the AI accelerator. This is still like a ray. And just slap that in there and have something to debug. And so that's the origin story of that.

**Chris Gammell:** It sounds like you should be sponsored by an energy drink company. That's what it sounds like. If there was like an energy drink for, well, I guess if you met Tim, you know that Red Bull would be the energy drink of Tim. That guy drinks more Red Bull than I've ever seen.

**Julia Desmazes:** Maybe, maybe. But personally, I think I want to be sponsored by Waffle House.

**Chris Gammell:** Oh, really? Oh, absolutely. Tell me more.

**Julia Desmazes:** So I have an ongoing tradition is that every time I finish a certain type of project, like a certain scale project, I go to Waffle House for waffles. And I get their 275 unlimited drip coffee.

**Chris Gammell:** Not good coffee. If my Waffle House experience has any...

**Julia Desmazes:** It's tradition. It's, yeah, definitely not the prime roast, but you don't go there for prime roast. You go there because you stayed up for 48 hours in order to make the tape out deadline. And you submitted your design at 4.30 a.m. And then your best idea your brain could come up with is like, hey, let's go for Waffle House and get unlimited coffee and stay up until like 8 p.m. the next day.

**Chris Gammell:** That's a good tradition. Although I have to say the best thing in the menu at Waffle House is the fights that always happen in the parking lot outside the Waffle House.

**Julia Desmazes:** Interesting. I've not been privy to that tradition, but I look forward to it.

**Chris Gammell:** Yeah, I think by 4.30 all of the people from the bars have already gone home and you're already into the breakfast crowd. So it's good that the tape out took a little bit longer.

**Julia Desmazes:** You know, totally. No, but generally I'm pretty, I wait until 8 because my significant other, I can't expect to wake him up at 4.30 and say, hey, let's go to Waffle House. He's very patient with me, but I don't think he's going to like that very much. Though I haven't tried to eat.

**Chris Gammell:** There's always the next tape out.

**Julia Desmazes:** Absolutely. So, systolic arrays, heart of the AI accelerators, and there's been a couple of people taping out TPU-like chips on tiny tape out. It's definitely something that is possible. Now, the big difference between the TPUs that you would tape out on something like tiny tape out in the open-source silicon trails and the big boy TPUs that consume a couple of hundred watts and Google run is the size of the matrix multiplication. The fact that we are doing it mostly on, at least my implementation was on signed integers, and they're doing it on fancy floating point maps, which is a whole other ballgame. And then, the size, of course, of the matrices you can multiply because, well, we're doing two-by-two matrices, and they're doing four times 128 by 128 or 256 by 256 by 256, different leaks. And then, the last thing is AI accelerators are very interesting because they can crank huge amounts of data. That's why they're designed. And because of that, the pipes to feed them are absolutely massive. Otherwise, your accelerator will essentially starve and not have anything to do. That's a problem where, at least I am pushing against, I'm hitting with a tiny tape out, is that we have this in-silicon area, but you need to get the data into the silicon. And our interfaces to do so are quite small. And so, even with my very, very small systolic arrays, they're already getting starved. So, that are some of the differences that you have to think about.

**Chris Gammell:** So, now you have a magic wand and the tiny tape out thing could change. What would it take to actually make it so that you could feed enough data into this sort of thing?

**Julia Desmazes:** So, the real dream would be to have, it's called the SIRDIS, serializer, deserializer. And it's a type of analog component that would allow you to have really, really high-speed differential pairs get connected then to your logic to feed in massive amounts of data. And my dream would be to have 10 gigabits SIRDIS, to be able to build a 10 gigabit internet or some high-speed PCIe on open-source silicon. Now, a little bit of context. The nodes we're dealing with were prime technology in 2000, 2001 era. And at that point, we were starting to have the first 10 gigabits interfaces come in to like...

**Chris Gammell:** Like leading-edge, kind of like Cisco was doing that with this crazy... So,

**Julia Desmazes:** it is technically possible. These SIRDIS require massive amounts of power. They would have downstream impacts in the way you would design your chip, but that would be the dream. And then at that point, then you could, building like the 10 gigabit physical layer to like just plug in your 10 gigabit internet, that would be the easy part. Then that would probably keep it fed until I ran out of area to build my systolic arrays.

**Chris Gammell:** Yeah, that is really interesting that that is the limiting factor there. But I guess in any kind of chip design like this, you're going to run into something that is like a true constraint from the hardware side versus like...

**Julia Desmazes:** Something people don't really realize is that the computation when you're at the ASIC level, computation is cheap. Moving data is extremely expensive. And when you were asking earlier about how to design an AI accelerator, or how to think about it, that is really the most important idea is that you do massive amounts of computation but that's the cheap part and the moving the data around is the most expensive part. And so the entire AI accelerator systolic array thinking is based around that idea is like how can we with the less data movement do the most compute and do the most efficient compute? And in my article two weeks until tape out I kind of without trying not to go too much into detail, I lay out the case when you look about it just from a power utilization perspective. Like the cost in power of moving data versus the cost compute is really, really massive.

**Chris Gammell:** Is that why like on a just to take it back to like consumer level things, like when they talk about like the cache on a CPU because of like sending data all the way out to the bus versus just having it right there like on scratch area?

**Julia Desmazes:** Yeah, yeah. When you're designing CPUs, I think most of your audience know this but I'm just going to say it again. You basically have like your CPU core where all the number cranking happens and then you've got multiple level of cache. So you've got the L1 cache which is like really, it's not small but for most applications it's kind of small and really, really fast. And then you've got the L2 cache which is bigger and less fast and then you've got this giant L3 cache which is massive and really, really not fast. And then you've got RAM which is, yeah, once you're hitting RAM, it's like...

**Chris Gammell:** Not anymore we don't because all the AI people.

**Julia Desmazes:** Yes. Granted. And the reason you have this hierarchy is because you're trying to minimize the cost of moving memory around and generally in the CPU you've got pretty good locality. So spatial and temporal locality. What that means is you're computing a value and you're using some data. The probability that you're going to be reusing that data within the same program context pretty soon is really, really high. And so you can utilize that to say, hey, we're just like keep the data around and that way once you need the data you don't have to get it from that far away. The problem with AI accelerators is you don't have locality.

**Chris Gammell:** Because it's not natively happening right there, it's like being sent in from somewhere else. Is that the thinking?

**Julia Desmazes:** There's that, but there's also the fact that you, when you have incoming data into like an accelerator, you don't really reuse that data that much. The weights you reuse, the weights you can like keep in place, but the data actually gets used pretty quickly and then discarded and you can't like reuse it that much. And so because of that, the way of thinking about it is different. But yeah, and so in your CPU when you do a load, you want to minimize the cost of that load as much as possible because actually, and this is something most people don't know, how quickly you can get a load value back to the core is one of the best predictors, or is a very, very good predictor of your performance. So it's highly correlated. So let's say I do a load. If my minimum time to get the data back from my L1 cache is three cycles or four cycles is going to make a massive difference.

**Chris Gammell:** Wow. Okay. And that's like the thing you spend time optimizing, that sort of thing?

**Julia Desmazes:** You would spend time optimizing, yeah, pretty heavily.

**Chris Gammell:** And is that at the software level or like I said, opcode level versus the hardware level? Because like there's, is it like physical constraint or software constraint or where is that constraint?

**Julia Desmazes:** You mean the three cycle constraints?

**Chris Gammell:** Yeah, exactly. Like what is, what's defining that?

**Julia Desmazes:** So what would be defining that is basically you're going to model like my program performance on this CPU. And then you're going to say, hey, if I make this three cycles or four cycles, like how much does that impact the overall execution performance? So that's how you would model it. And then the way you would implement it would be really at the hardware level. So at the hardware level, you're going to make it so that you can squeeze request furlough hitting the, the L1 cache data getting sent back in three cycles.

**Chris Gammell:** What is the trade-off that is not always one cycle? Why not just juice it all the time? You know, like that sort of thing.

**Julia Desmazes:** So when you're designing hardware, you are bounded by how fast your signal can propagate. And so when you run your CPU, you run it at a certain frequency and that frequency tells you how much time you have in a cycle. And in that time, you need your signal to go from basically start points, which is first flop, so signal getting released through all of the hardware logic, so all of the gates and everything to another flop.

**Chris Gammell:** So is that like place and route timing, like making timing to each?

**Julia Desmazes:** Yes, exactly. Making timing to each and then propagating through all of the gates and all of the wire, all of the wire links. And then maybe say you're going to L1 cache, you're going to like access some SRAM. So accessing the SRAM and propagating the signal, say, hey, I'm going to read this address and like getting all that is also going to use up time, essentially. And so there's a minimum time at which you can really squeeze it to make everything pass. And a sweet spot for that is three cycles because if you don't have three cycles, it's really, really, really hard to make it fit. So it's, why is it three cycles? Physical constraints. And if you can make it faster, but then you need to make all of the logic faster and maybe that's going to require like more power and sacrificing other things on the path that you actually want. And so it's always a trade-off. And so that's why it's being like, okay, this is the current sweet spot and maybe in newer generations, we're going to say, actually, the new sweet spot is two cycles or five cycles and we're going to design it through that.

**Chris Gammell:** Where did you learn this stuff? Like, I just think about like the amount of accumulated knowledge you have in this is fantastic. But like, was this classes I should have taken that I didn't take or is this on site, on job learning? Like, where was this? Where did all this come from? Because I'm asking dumb questions as I have no knowledge.

**Julia Desmazes:** That's a very good question. You know those little kids that look at you and say,

**Chris Gammell:** I have some myself, yes. Yeah.

**Julia Desmazes:** Perfect. Okay. So they go like, how does this work? And they look at you and you answer the question and then they look at you and say, perfect, how does that work? And they go deeper and deeper and deeper and deeper until they're like, hey, how does the transistor work? And you're like,

**Chris Gammell:** I don't know, kid, get out of here. Go watch some TV. I don't do that, but yeah, right, do something else. Okay.

**Julia Desmazes:** I was that, I was that kid. And so of course I ended up in a hardware design.

**Chris Gammell:** You had no choice.

**Julia Desmazes:** I had no choice. No, more seriously, a little bit was you build the foundations through school. You model your brain. You're like, hey, this is like high level, how a CPU works and why we design in this way. And these are like the constraints and these constraints led to this, the way the hardware would evolve this way to respond to the constraints and in doing so they introduced this new constraint. So you kind of built the basic of thinking about like CPUs in school and then you get on the job. And so for example, this whole discussion about L1 caches and the three cycle constraint that was on the job, things that you learn because you're trying to build them out and in doing so you're acutely aware of the constraints and how they come into play and how everything is connected.

**Chris Gammell:** Like because all your coworkers are talking about it and you're like, I got to learn about this sort of thing like that?

**Julia Desmazes:** Because you need to build it.

**Chris Gammell:** Got it, got it. Okay.

**Julia Desmazes:** Yeah, that's really, the best way to learn about something is to try and build it and understand the problem because once you're building something, you're not just understanding the solution, you're understanding the problem that led to the solution and that is as valuable as the solution itself.

**Chris Gammell:** Right, it kind of goes back to your point about like the low cost and the ability of the people to do this with Tiny Tape Out and other tools. It's like, actually you can do it before you get to industry, right? Like you, people could follow along and do this in some level.

**Julia Desmazes:** Absolutely.

**Chris Gammell:** I do think people in the future are going to point back to the things you've been talking about and like the tooling that's been popped up and they're just gonna be like, well, the reason we can still, like, I think about like the contrast, this is probably like too pundit-y, but like LLMs do math for me and yeah, we are talking about a significant amount of math and like just all the training that you've had and all that other stuff and like people are gonna need to build this in the future too. So like, how do we keep people excited? Well, one, we find more Julia's out in the world, of course, but then also then they have access to tooling to build it up themselves and you know.

**Julia Desmazes:** There's definitely that. Tiny Tape Out has a very strong, getting people interested in hardware and getting people to build up the skills in hardware and the open source silicon flow is very different from the industry flow in the sense that it's extremely transparent into what is happening and it's a really, really good learning device. That being said, it's accessible in the same sense as running a half marathon is accessible because you can, because everyone can get running shoes.

**Chris Gammell:** Because you can, yeah, you go sign up for a bib, no problem. Exactly. You get the hundred bucks, you get the bib, yeah.

**Julia Desmazes:** Exactly. And you can just like, okay, put the timer on, put Strava.

**Chris Gammell:** Yeah, no problem.

**Julia Desmazes:** Do 20, 21, 22K, no problem. The problem is that you need some background and you need to build up that background and that takes time. Tiny Tapeout is definitely, and the open source silicon tools are definitely a good way to build that. But that's the same way as telling someone to learn Linux, install Arch.

**Chris Gammell:** Ouch.

**Julia Desmazes:** It works.

**Chris Gammell:** Don't do that. Don't do that, folks. Exactly. It works,

**Julia Desmazes:** but it's extremely, it's extremely painful.

**Chris Gammell:** Yeah. Yeah. And you have a ton of fallout from the crowd. Just they're like, well, no, this isn't for me. Right. You want to keep people like interested enough. Exactly.

**Julia Desmazes:** Going back to your point about how do we build for Julius. If people are interested in hardware, firstly, nothing's going to stop them. But secondly, like it's tackling harder and harder problems. So for example, I would take a problem that I know I can tackle today and then I would take the next problem that's just like slightly out of the range of what I can do. But I know that this is the next problem I need to tackle if I want to get to the next level. And once I've tackled that problem, then I can put another problem and build on top.

**Chris Gammell:** Tackling this particular problem too is interesting. So you needed a target for the JTAG, but why the JTAG? Like have other people not done kind of core JTAG debuggers that need to go onto chips, that sort of thing?

**Julia Desmazes:** So this is actually a really interesting question. I think it goes down to design, to an engineering philosophy. I am not making these chips because I want the chip. I am making this chip because I want the knowledge that comes with doing the chip.

**Chris Gammell:** Well, I guess I was going to say the SEGGER debugger is probably not something you're going to plug into a silicon thing, but like you need something like that, right?

**Julia Desmazes:** No, no, I actually am plugging in a SEGGER debugger to the FGA emulating the chip. So yeah, totally, it's getting a SEGGER debugger on its ass. But there are open source JTAGs, hardware JTAGs out there that I could just take, use and plug them in and it would work. But at that point, I've not fully understood how to design a JTAG or I've not fully understood the spec and I'm not fully interested like how JTAG works and I've not fully understood the capabilities of how further I can push it. And so that's why I'm going to rebuild it myself in order to fully understand that. And then once I need the other thing that this existing hardware doesn't do, then I can easily add it on. So for example, the JTAG I built for C is a very good exercise in actually understanding how JTAGs work because you think you understand it.

**Chris Gammell:** I have no idea actually how it works. It's just magic. Every time I'm just like, yeah, it's probably talking to a register somewhere, you know?

**Julia Desmazes:** Exactly.

**Chris Gammell:** There's all those pins like SWO trace. I'm just like, someone needs this. It's not me, you know?

**Julia Desmazes:** Exactly. And I was kind of like that and I was like, okay, I already had a good understanding of like, this is how the JTAG protocol kind of works. And so I built my hardware and I built my test benches and my simulator and I simulated it and it's like, okay, this is how it's supposed to behave and everything works. And then I plugged the actual server. I plugged the actual JTAG probe there and it doesn't work. I'm like, ah, yes. Okay. Now I actually need to rethink about all of this because this preconception I had was wrong. So now I've got to fix it.

**Chris Gammell:** Yeah. Building and testing mental models effectively, right?

**Julia Desmazes:** Exactly. Building and correcting mental models. And that's why, for example, the emulation part in the design flow is so great because then you actually try your hardware against reality and reality tells you if it's failing or not because reality is always right. Like you can't argue with reality. Pretty sad.

**Chris Gammell:** I've been trying. I'm going to continue to try to fight that one, but.

**Julia Desmazes:** Yeah. So I've got my working JTAG and now I want to say, okay, now that I've deeply understood the JTAG spec, I know that I can add custom features to JTAG which are going to be useful for debugging my weird hardware carrying case. And so I can just like slap those in. And so now it's basically an iteration of like, what is the next weird feature I need on my JTAG to debug my hardware? I'm just going to slap that in.

**Chris Gammell:** So just to step back a little bit. So you said when you're testing it for reality as well, was that the flow where you're pushing your, so you've simulated on the machine, you've placed and routed it, you've put it into an FPGA and then you've tested the JTAG. Is that right?

**Julia Desmazes:** Exactly. That's exactly what happens.

**Chris Gammell:** There's a lot of other tools that are like in there. How do you know those are all working when the, you know, your part isn't working?

**Julia Desmazes:** It's basically a leap of trust. And this is why tooling is so important. I trust that the tooling on which I am building is reliable. And I trust, for example, for testing JTAG, I was using a great tool called OpenOCD, which is an open source JTAG server, which has support for lots of different debug protocols and it has like JTAG support and it has support for the communicating with whatever JTAG probe I'm using at the moment. And I trust all of that works. And so when those, when OpenOCD tells me, ah, something weird is happening here, then I'm in the wrong. But maybe OpenOCD might be in the wrong. And then my assumption is wrong because now I'm, I'm designing for what OpenOCD thinks JTAG is supposed to be and not actually what JTAG is supposed to be. There's always the risk of a breakdown there.

**Chris Gammell:** And I'm guessing you probably have some known good working models that go on the FPGA that you can like test and make sure the, the, the rest of the tool chain is working good too?

**Julia Desmazes:** Uh, no.

**Chris Gammell:** Oh no?

**Julia Desmazes:** Um, no, no. Um, a little, a little bit, but not as much as what I would like to tell you.

**Chris Gammell:** I see. I see. Got it.

**Julia Desmazes:** Like, so yes, of course I've got perfectly working models, which emulated JTAG and like this, uh, this soft CPU is supposed to work perfectly, but no, no, I don't.

**Chris Gammell:** Nah, not so much. No, not so much. How does the interplay work then? Okay. So again, as a, as someone who's someday going to be building a counter that might go on tiny tape out, where the FPGA piece and like how you make that all work. So you're writing Verilog, you're validating valid Verilog, and then you're placing and routing for, uh, uh, like a Xilinx part or something like that. Like how can you kind of step us through those pieces as well?

**Julia Desmazes:** Okay. Um, so I'm going to take a step back and step you through the entire flow and it's going to include your response, of course. So firstly, there's what we call the design phase. So the design phase starts with boring pen and paper. What am I going to build? What are the constraints of the system that are going to be imposing on how I'm going to think about my design? Say for example, tiny tape out has n number of pins and these pins can work at this frequency. And so I'm going to use from that. Okay. So this is, for example, going to be my IO interfaces and this is going to be my target frequency, which is going to depend on like how fast I can get the data in because there's no use like running my internal logic faster than I can feed it. It's just going to start even worse. So constraints of the system are in place. And then I'm going to start pen and paper designing what I'm going to build, how I'm going to build it. Okay. Let's say IO is this size, but I need like more data. So I'm going to have like something between IO and my systolic array to accumulate data to be able to like feed it. And then I'm going to need something to take the data out of my systolic array and then feed it back through the IO. So all of that pen and paper. Then once you've got a good model of how everything fits together and what you want to build at a higher level, you go to the Verilog or system Verilog. And system Verilog is basically language representations of how logic gates are connected. It's actually a very, very simple language. And so I'm going to build it and it's going to be broken and I'm going to know it's going to be broken because I'm going to write simulators. So simulators are test benches that are basically going to say, here's an input to my simulated logic and read the output and like compare it to an expected output. So these simulators, you've got a bunch of open source simulators and then over that, they're, and for Tiny Tape Out, they use a Python wrapper. So all the test benches are actually written in Python. Though for personal projects, I use other things, but we're not going to get into that right now. So I've got my simulation and I'm going to-

**Chris Gammell:** Were you going to say tickle? Because I feel like every chip designer eventually says tickle.

**Julia Desmazes:** I'm going to say tickle, but not right now. But don't worry, tickle's coming.

**Chris Gammell:** That's like my one input from like a long ago FPGA stuff. It's just like tickle. Everything's tickle.

**Julia Desmazes:** Tickle's coming. So I've got my simulator and I know that based on like what I think the input and outputs are going to be, my hardware works. So at that point, you're a couple of weeks in and you have not enough time for doing all the rest, but you're good. Okay. So now I have this mental model. Given these mental model inputs, mental model outputs represented by my test bench, I think this works. Because my hardware doesn't exist in a vacuum. It's going to want to talk to something else because these are accelerators we're building. And so they're basically going to be slaves to some kind of micro control. That is going to like send them work to do and then get the response back and then send that maybe to like a bigger system. At that point, I want to talk to this microcontroller and make sure that the parallel port that I've designed that goes between my custom accelerator and this microcontroller actually works. So now I need to build two parts. First is the firmware that is going to go on my microcontroller and it's going to talk to the ASIC. Second part, I need the model for my ASIC because it's going to take nine months for my ASIC to come back from the fab. So I want something that is usable now and that's where the FPGAs come in. So FPGAs, what I'm going to do is I'm going to take my RTL design that I've validated kind of works according to my simulator and then I'm going to port that to an FPGA and I'm going to make like some kind of wrappers around it to basically have all of the IO wrote through the FPGA's expected pins and then I'm going to build that for my FPGA and like flash my FPGA with my design and then have it talk to my microcontroller with also like my firmware and that's where Tickle comes in. So I basically have like a Tickle flow which is going to take my hardware and then build the firmware equivalent. We call it a bitstream that is then going to go on my FPGA and at that point I'm just going to like strap debuggers all around the place and try and figure out why the two aren't talking together correctly. And at that point once I validated both the firmware and the hardware emulated on the FPGA at that point I can do the hardening so basically take okay I know this RTL is good so the very log is good very log code so hardware code and now I'm going to translate it to what it's actually going to look like on the ASIC for the final time. Now I abstracted away a little bit of the complexity there because in reality you're constantly making sure that your design can actually be implemented on the ASIC because you need to make sure that for example you're hitting the target frequency that you set for yourself or that you fit into the area but that would be like the general flow.

**Chris Gammell:** Iterative process and all that back and forth. Yeah interesting. So in that case that actually is good context too of having the microcontroller having something that can like stimulate the design that sort of thing. So now we're talking about within that that blob that's inside the FPGA then so now there were two pieces in there is that right because there's the accelerator plus the JTAG piece?

**Julia Desmazes:** Exactly. So in the case of the two weeks until tape out there was both the accelerator and the JTAG and so for example for verifying my JTAG then I stuck a second JTAG G-dink sorry so which is like the JTAG device on there and I was sending it data and making sure the communication was working as expected.

**Chris Gammell:** Got it. So that was in the FPGA context that would have just been like a secondary set of pins like you're routing that out to IO and then you're plugging that IO into the SEGR and that's how you validate that it's actually like seeing the data flowing through. Absolutely. Interesting.

**Julia Desmazes:** And so it was a really fun setup because you had like Raspberry Pi Silicon on one hand so it was like a Raspberry Pico something FPGA and then you had like two JTAG debuggers sticking out to it.

**Chris Gammell:** Yeah. There's so many pieces all talking to each other too.

**Julia Desmazes:** Absolutely.

**Chris Gammell:** Are you doing physical measurement of that as well or are you just kind of trusting like transitions and all the you know like this kind of the scope level digital digital logic analyzer logic analyzer I suppose.

**Julia Desmazes:** Yes. I do have a very very trusted probe sitting sitting in my living room which has gotten a lot of use during debugging because things never go as expected.

**Julia Desmazes:** Right.

**Chris Gammell:** Everything's analog eventually right?

**Julia Desmazes:** Absolutely. And half of the time it doesn't work because once you get like to once you hit a certain frequency certain behaviors become problematic and so often when I'm doing the FPGA emulation I drop the frequency a little bit in order that my terrible wiring doesn't cause any issues.

**Chris Gammell:** Yeah. I love these kind of scenarios too because I am daily using things that I have no idea how they work under the hood. Right. And I'm just like depending on like you said JTAG the you know the SEGUR emulator SEGUR SEGUR debugger rather and just all the stuff all the stacks and stacks and stacks and stacks. So when you do something like this and you're just like you're literally splaying it out in your in your living room you're helping to expose all the things that are there and you're also modifying and making it new things as well.

**Julia Desmazes:** Absolutely. And this is why open source is so great is because when something inevitably goes bad I can actually go in and figure out what went wrong. So for example open OCD and the underlying libraries to talk to my very specific GTAC probe those are all visible to me and I have like compiled custom versions of them and I know that if I need anything I can put them in debug mode put the put a debugger on them like GDB and figure out what's going on and that level of transparency is absolutely necessary because things will go wrong eventually they always do. That's also true for the entire ASIC flow is when something goes wrong or when there's not documentation on like this very specific feature that I kind of want and there are three other people that are using it then I can go into the code and figure out how to make it work and that wouldn't be possible.

**Chris Gammell:** So I have a friend that takes things back to first principles and that's kind of like his default but then he kind of gets stuck in rabbit holes sometimes. He's so good at everything anyways it's just like you know to me it looks like magic but like do you do you get caught on rabbit holes as a result?

**Julia Desmazes:** Absolutely. So I'm actually just emerging from a month long rabbit hole right now.

**Speaker ?:** Okay.

**Chris Gammell:** I hear a blog post coming. There is absolutely a blog post coming.

**Julia Desmazes:** So a little bit of context to explain this rabbit hole. A couple of years ago I got my ass absolutely handed to me by floating points. So we all know like floating points floats. Scientific notations on your computer allows you to do zero dot something that isn't an integer. And so floating point maths going into this my belief was there are only three types of people that actually know how floating points work. The people writing the spec for floating points so that I triple E people. The PhD in math that are actually designing the next generation of floating points and the people implementing floating point hardware. So this is like the level of complexity that we're dealing with. And so a couple of years ago I was like hey floating points everyone uses it. It's all around the place. It shouldn't be that hard. It's everywhere. Exactly. So I tried to do an addition.

**Chris Gammell:** Does it matter how many bits or it doesn't even matter? It doesn't

**Julia Desmazes:** matter. Like the complexity is still there whether you're doing eight or 64 bits. And so I tried to do my addition and normally you just invest time and a problem and eventually you figure it out. I did not figure out and it was the first time I got my ass that badly handed to me by something. And I keep the scar. So now we're doing systolic arrays and my next tape out is also a systolic array but this time it's in order to get my revenge on floating points. So doing the floating point math. But this time this is V2 so I've learned since then. I decided I'm going to understand floating point math. And so I spent about a little under two weeks just trying to understand floating points from first principles and reading papers on floating points. And then I implemented another. And it took me 27 days from start to finish to implement an other. And I have never been so proud of

**Chris Gammell:** another before. And if I

**Julia Desmazes:** just wanted like floating point I could probably have found somebody else's floating point math. And maybe it wouldn't have been the very specific floating point format that I really want to use for my very specific needs of a systolic array. But it would have been good enough. But here we are.

**Chris Gammell:** I only have one. All of my FPGA stuff comes from 2004. So please excuse that. And it was when I was an intern. So again, further explanation. But here's another one. I was learning with Simulink which was basically like a block generator. It was like generating code for me. And I just remember there was like a problem where we were like we were like trying to solve some math we're doing everything fixed point. And there was literally a checkbox in Simulink. It was like, oh, do you want to do this in like floating point? And I clicked it and my boss was like, oh, we don't do that. He's like, you will, everything will get much bigger and you don't need it. And you should just learn how to deal with fixed point because you're going to have to deal with fixed point anyways. You're in a chip, right?

**Julia Desmazes:** So, according to the IEEE spec, you have multiple different rounding modes.

**Chris Gammell:** Which one do you want? With multiple different behaviors? So, choose your own adventure. How many days do you want to burn on this next one? Right? Absolutely. So, I think

**Julia Desmazes:** it's a hard for people to imagine from the outside. There is so much nuance and beauty to it. Don't you just like round it off? You just like throw away some bits and you're fine? Sorry, these are like triggering words

**Julia Desmazes:** I was like,

**Speaker ?:** what? So, according to

**Chris Gammell:** the IEEE spec, you have multiple

**Chris Gammell:** Which one do you want?

**Julia Desmazes:** Absolutely. But the thing is, once you've understood it from first principles, then you know exactly what you need for your use case and hardware is all about constraints and optimization. So, you know exactly, I'm going to use this format and I'm going to use this rounding mode and I'm going to implement it this way so I can squeeze the absolute maximum performance out of it.

**Chris Gammell:** Because it takes nine months to get new silicon.

**Julia Desmazes:** Yeah, yeah. There's that. There's that. And there's also the fact, so let's think about going back to our TPU discussion. Let's say you're a giant, like you're actually making a giant TPU. You're going to make a 256 by 256 multiplier, a matrix matrix multiplier. That means you're going to have 256 times 256 multipliers and 256 times 256 additions. So that's on the order of 64k of each. Once you're replicating it that much, you want your FPU to be as optimized as possible. And in order to do that, some choices that you make in your floating point designs are going to be extremely impactful. But you're only going to know of those choices if you've implemented it or if you understand it from first principles. And so that's also one of the things. Once you've built it and you've seen all the complexity, you know how your choices are going to impact your hardware and you know how to optimize it further. And there's going to be actually downstream a pretty big difference between different choices you can make on floating points. So for example, there is the B float 16 format and the normal float 16 format. Talking about it this way, like, ah, they're like both 16 bits. They sound kind of the same. They're very, very different. One of them is going to be way more expensive to implement in hardware. But that's something you're going to see once you've understood all the underlying problematics and pain and suffering.

**Chris Gammell:** So one thing I remember from that long ago was like, all of the additional, you know, basically two floating point numbers make a lot of remainder down the line. And you have to have like kind of like not that useful registers there to hold those values. Is that part of it? Or like what is the actual implementation like detail that requires such a difference?

**Julia Desmazes:** Float 16 and in B floats 16?

**Chris Gammell:** Yeah. Like what is driving these decisions? So you said one is much more efficient than another. But what is the efficiency translate to? It's just gates like silicon?

**Julia Desmazes:** Yep. So for example, the way you would do a multiplication in floating point means that you will need to build a multiplication for your mantissas. And so if your mantissas are smaller, you have a smaller multiplier. And multipliers like they're... They scale fast,

**Chris Gammell:** right?

**Julia Desmazes:** They scale very, very fast based on the size of the mantissa. And so if your mantissa is small, that is going to result in a much smaller multiplier, which is like going to be a massive amount, a massive bit of logic compared to if it's large. So that's, for example, between floats, one of the biggest differences. Another difference is float 16, it has a spec and it has things you need to implement. And like you need all the different fancy rounding modes, for example. And if you want to implement a spec, you need to implement like all these different things. And if you're doing float 16, like you're in the wild west, there's no spec. You can do what the hell you want. Implementation defined. And so you can basically pick and choose, okay, like, you know, this rounding mode there, it's actually going to translate into way more logic where I really, really, really don't want it for timing. So let's just use this other rounding mode, which is actually like way, way better in logic and maybe it's going to save like, I don't know, 10 or 20% power compared to this other rounding mode. And this is just a rounding mode. Like minute choices can have absolutely massive impacts, especially once you're scaling something to the size. Whereas say, for example, you do one floating point operation as part of some really, really bigger logic, you don't have 64k iterations of this. It's not going to make that much difference whether you use like float 16 or even like float 64.

**Chris Gammell:** got it.

**Chris Gammell:** Yeah. I'm kind of thinking of like, you know, that saying they say we're like, you only use like 10% of your brain sort of thing. Kind of like feels like you're only using like 10% of your chip because you have all this support circuitry to satisfy the spec. And like you're saying, you'll be able to just like wipe it out and be like, nah, we're not doing that. So that part of the chip. So you save that silicon, you save that power, you save it. Like that all stacks up, right?

**Julia Desmazes:** Exactly. And that's one of the very interesting pieces of making custom accelerators and why open source silicon is actually so interesting. It's because when you're making a custom accelerator, like normally you would make it run on the CPU and your CPU would, it's not even like it's using 10% of its brain. It's like using 5% maybe of the actual power and complexity and silicon. And most of the silicon is just there to support this like 5% of the, I want to. Yeah.

**Chris Gammell:** The heat map is very centralized, right? Exactly. And then everything else is just like once in a while. Yeah.

**Julia Desmazes:** Exactly. Now, actually like this once in a while happens a lot, but the computation that you care about is actually really, really small. And if you have a very, very well-defined use case, you can say, hey, I'm just going to like rip out everything I don't absolutely need. And I don't care if it doesn't do if branches. And I don't even care if I can't program it. It's just going to be like hard-coded to do one thing, but it's going to do that one thing extremely well. And so the thing is, once you're making custom accelerators, you can be very, very efficient. The problem was making custom accelerators was really expensive. But now that you have open source silicon and you have, let's say you want to make like a full custom chip, you can go to Tim Ansel's Wafer Space and you can drop 8.5k for a thousand parts of 20 millimeters squared, which is kind of nice. It's like, it's a pretty big amount of logic. You can build a bunch of custom cryptographic accelerators. There are no problem. And you have all the

**Chris Gammell:** secrets away in the magic sand.

**Julia Desmazes:** Exactly. Lock all your secrets away and you have all the tools and the cost of making your weird custom accelerator is actually accessible even to individuals. And at that point, well, what's stopping you? Of course, what is stopping you is the knowledge. Yeah, the knowledge.

**Chris Gammell:** Julia, you and I are very different in that you have such awesome knowledge here. I don't know. Also, I'd like to pause and just say when I first asked Julia to be honest, she's like, I don't know. Do you think people want to hear like, so I'd like people to judge right now. Like, do you want to people, do you want people to like, do you think we'll have stuff to talk about? And I was like, yes, of course. I knew that from one blog post. Of course. Yes.

**Julia Desmazes:** So, yeah. Thank you very much.

**Chris Gammell:** Can we actually talk a little bit about that, that, that super application specific, like ripping stuff out? Because we talked about that a little bit before the show of like, like your work doing CPUs versus doing this like super highly specialized, just an accelerator part. And some of your, some of your other work that you've done in the past too, like just the, how that changes constraints as well.

**Julia Desmazes:** So let's say you're building a CPU. So what is a CPU? CPU is a general purpose hardware. It needs to take pretty much everyone's code and execute it pretty well. So when I was working at ARM, we were working on embedded devices. So now you have the additional constraints of not only the power envelope, because you don't want someone's battery to, phone battery to instantly die. So you need to keep the power consumption kind of under wraps, but you also have area constraints because how big you make your CPU cores is going to directly translate into manufacturing costs. And so the cost of the chip and the cost of the device. So you're working within those constraints. So what you're going to build is going to be something that is going to be great for most use cases. It's going to be conformed to the architecture. So we have a contract which is going to say, hey, this is going to run the ARM architecture v9.something and it's going to have all these features and you need to implement these features and make them so that this is going to be pretty well performant for most of the users out there. And in doing so, you're actually, if you were talking about this in car analogy, you're building Toyota Corolla. It has great mileage, great power efficiency. It's super reliable. It's street legal. It's cheap. It's great car. It's a sedan, like it's a eco sedan. Now, let's say you have your custom use case and you know your use case and you just want to make it fast. And you don't care about if it's compatible with legacy code. You don't even care if it's compatible with code. You just have one goal. And so what you can do is you can build a specialized chip for it. And the analogy here would be you're making a Formula One car. It's going to do your thing really, really fast. It's going to be super expensive to build. It's going to have lots of custom parts. No one's going to know how to drive it. The turning radius is going to be awful and it's absolutely not street legal.

**Chris Gammell:** And it's going to be awesome. It's going to be awesome. Yeah.

**Julia Desmazes:** And these are the two ways of kind of thinking about hardware. And they're very, very different ways. And they're very interesting ways. Even if underneath, you may be wanting to do the same use case.

**Chris Gammell:** Yeah. Yeah. It is interesting. I remember talking with Matt too, when Matt and Ben was on the show about like, well, aren't people building, you know, like RISC-V processors and stuff like that into Tiny Tape Out? And he's like, well, that's not really the point. You know, like it's because like even just to zoom back up to the level you're talking about, it's like, why wouldn't you go buy that Toyota Corolla or that ARM processor? Like just doesn't, you know, RISC-V is enabling more things, but it's not necessarily the same application space.

**Julia Desmazes:** Absolutely. Most people, most students will go build on Tiny Tape Out or maybe most hobbyists will want to do the cool, shiny projects. And the cool, shiny project for a while was CPU cores, RISC-V CPU cores. They're super exciting. Everyone wants to build their custom CPU. Like imagine how cool it is to boot Linux on your own custom CPU. That's awesome.

**Chris Gammell:** Especially because you don't have to write. I feel like the big thing with RISC-V too is it's like because of the common ISA, it's like, okay, I don't have to write. I don't also have to write my whole coding language, you know, like all the op codes, all the language stuff, all that OS stuff. It's like I can actually have like a translation layer there. Like that's the power of both.

**Julia Desmazes:** Exactly. But in parallel to like the CPU cores, you have lots of small, weird accelerators that you can build that no one else has ever built before and that are maybe less exciting for most people, like telling them, hey, I built an accelerator for Blake 2 hashing. And they're like, what is that? But it really allows you to flex your muscles and build something that maybe won't be competitive with running the same hashing algorithm on a high-end CPU, but you can build something that is going to be pretty, pretty good, especially considering you're using 25-year-old technology. There's also something else. We don't often think about how much the underlying hardware shapes what we do with it. So say, for example, I'm not an AI fangirl, but I'm going to use AI for this example. How much of what is currently the state-of-the-art network architecture is actually derived or was actually selected by what the hardware can run well versus what is actually the best architecture or the best, could be the best architecture going forward. Basically, what you can build is going to be shaped by the hardware that you have around you.

**Chris Gammell:** Sorry, network architecture in that case is like unship network architecture or something?

**Julia Desmazes:** No, no, sorry, not network. Compute architecture, I was saying.

**Chris Gammell:** Oh, sure, okay.

**Julia Desmazes:** My bad. And so maybe let's say you build like this new network, a neural network type. The thing is, your neural network won't shine compared to the existing widely deployed neural networks because all the existing ones are really tailored for the existing hardware. And so they have access to way more compute, underlying compute that you have for your network. And so at some point you'd be like, okay, well, what if I had a specialized chip to do my hardware? Or what if the barrier to entry was lower? Maybe I could have my specialized chip and would actually allow me to reveal this entirely new space of neural network architectures that couldn't exist or couldn't shine previously. That's what I mean by we don't realize how much our underlying hardware shapes what we do with it.

**Chris Gammell:** Got it. Got it. So like the hardware drives the architecture, the architecture drives the implementation on top of that architecture. And then ultimately, but it's almost kind of moot too, right? Because it's like, it's also like economics plays into the, like we're dealing with what we have and it's like people are going to design for what's available.

**Julia Desmazes:** Like, exactly.

**Chris Gammell:** Like generic compute on AWS. Like people are just like, well, yeah, whatever works there because I can get a ton of it at super fast. Right. Like that's driving a lot of it.

**Julia Desmazes:** Exactly. And, and so now you've got like a, you've got a feedback loop, which you explained very clearly. And so the question is at some points to break the feedback loop, maybe I need something that is actually really cheap such that I can take a risk. And at that point you look at open source silicon, you're like, Hey, actually this is cheap enough that I can take a risk on it. And so I'm really excited to see how much interesting novel accelerators are actually going to be born because the barrier to entries has been lowered so much.

**Chris Gammell:** Have you had, so you're in your designing of the open source stuff. Have you gotten chips back yet? Are you still waiting on those?

**Julia Desmazes:** I'm still waiting on them. I'm so sad.

**Chris Gammell:** So which, which runs were you in?

**Julia Desmazes:** Skywater 25B. So Skywater 130 nanometers, a chip that was sent at the tail end of last year. Then I was going to global foundries 118 nanometers. So that was the two weeks until tape out the experimental tape out that was going through with the first run of wafer space. And now I am working on the next accelerator, which is going to go on AHP, which is a European fab.

**Chris Gammell:** Oh, cool.

**Speaker ?:** Okay.

**Julia Desmazes:** And that's closing in under 30 days.

**Chris Gammell:** Got it. So what I'm hearing here is Tim's like calling you up and being like, Julia, do you want some more space here to just try some crazy stuff? And yeah, that's great.

**Julia Desmazes:** So I actually have the dream of going to and getting myself a wafer space spot. The thing is it's 8.5 K.

**Chris Gammell:** Yeah, it's a lot.

**Julia Desmazes:** And I don't want to risk 8.5 K on a chip until I have acquired a certain amount of confidence in my ability to successfully pull it out of. And if I don't pull it off, to know exactly what went wrong.

**Chris Gammell:** Yeah, right.

**Julia Desmazes:** So I'm kind of dragging my feet on it and be like, actually, like tiny tape out is pretty good right now. Also, the fact that 20, the wafer space gives you a lot of silicon area to work with. And unless I just massively scale the systolic array, I'm not going to be able to use that much space. But if I scale the systolic array, then it's going to starve. And so I need to figure out the IO bottleneck. So a couple of constraints there.

**Chris Gammell:** In our last bit here, can you just explain the, so then you've kind of, you walked us through really well of like the testing all the way through the FPGA with the PICO, you know, stimulating the design and stuff like that. The PDK piece, right? The translation to gate logic. Oh, I always forget the name of, there's an acronym there, right? The, whatever the gate logic is, like the actual file they send to the fab. It's great. How, how is that for you as a user? Is it kind of just, is it just a click a button or is it like a more than that?

**Julia Desmazes:** There's actually an entire job category, which is called physical implementation, who specializes in this. And it's a very, very deep expertise. The tools that actually do like the flow, there, there are actually many smaller tools. So you've got open road, which is the heart of it, call it the, the one that actually does like placing on the ASICs. Then you've got YoSysh, which is like the synthesizer, which takes your logic and says, okay, this is going to be translated into these logic cells that correspond to this PDK. And then basically open road takes it and places it and like checks your timing and everything. And then maybe you're going to have like other issues, which are going to pop up. So let's say I can, I can run the tool suite by pressing a button, but that doesn't mean that my resulting GTS file. So the thing I'm going to send to the fab is actually going to be manufacturable. So maybe I'm going to have issues that are going to arise and these manufacturable issues are going to be caused by underlying behavior of the actual circuit. And so then I need to go and fix those. And so it's kind of a loop to answer your question. All of these tools to build this flow have been put together by a bigger tool called LiberLane, which I called the equivalent, the make file for ASICs. And LiberLane actually allows you to have a one command, which is like make ASIC, and that will run all the tools for you. So you have a default configuration that will make the flow. And then you have you on the other hand, which is then going to be responsible for fixing it so that what LiberLane does actually works.

**Chris Gammell:** I feel like there's, there's always these like great, like they're not perfect analogies, but like I always like map in my head to like, oh, that one's like DRC, that one's like Gerber's, that sort of thing. And LiberLane, I guess in this case is like, like, I don't even know. There's, there's really nothing like that for PCBs, it feels like, so we should get that.

**Julia Desmazes:** We should, we should get that. The, the KCAD, KCAD make file. Just take my skim out.

**Chris Gammell:** Maybe it's like a MCP on top of like KCAD these days would be nice or something like that. And then you just let Claude do it, you know, and just be like, Claude, yeah, go for it.

**Julia Desmazes:** Build it for me, please. Just do all the plays.

**Chris Gammell:** Yeah. It'd be great. YOLO.

**Julia Desmazes:** Yeah, no, the, the complexity of the tooling we have for OpenSource Silicon compared to the amount of people that are actually doing OpenSource Silicon in opposition to the people that are actually doing PCBs is absolutely crazy. The quality of the tools we have is, is something we, we, we are very, very happy for there before. Let's put it that way. Thank you.

**Chris Gammell:** I mean, thank, thank goodness software people got so interested, right? I mean, like it's like, it's so much software, right? It's, I, I just think about like, if a hardware person was tasked with doing this and there's also hardware people in the loop, but like not, not the software people are the, the superheroes. Yeah.

**Julia Desmazes:** There's a joke that hardware people don't know how to write software. It's partly, it's partly true.

**Chris Gammell:** I don't think it's a joke. I think it's just reality. I, I, hey, look, it me.

**Julia Desmazes:** I don't say that.

**Chris Gammell:** Yeah. Well, you know, Julia, where can people find you? First off, you got to come back and talk more about this stuff, especially as like chips show up. I want to see all your, you know, like how this worked out and hear about the B float 16 and where can people find you and, and follow your stuff?

**Julia Desmazes:** Well, I have a blog called tails on the wire, which is a GitHub, a GitHub blog, which you will link in the show notes. I have my GitHub at a S and C. And apart from that, they can find me on the tiny tape out discord. I'm pretty accessible. I go under the SN username and the people can just reach out or just YOLO and send me a mail, which is something that people used to do.

**Chris Gammell:** So you never know some, yeah. Sometimes you reach out and you say, Hey, this is a great blog post. Can you please explain how chip design works to me on The Amp Hour? And Julia responds. So thank you for being here. I'm really excited to see all the new things you built.

**Julia Desmazes:** It's a pleasure. Thanks for having me.

**Speaker ?:** Bye. Bye. ! administered administered administered
