---
episode: 254
title: An Interview with Andreas Olofsson - Adapteva's Ampliative Abacus
url: https://theamphour.com/254-an-interview-with-andreas-olofsson-adaptevas-ampliative-abacus/
---

**Andreas Olofsson:** This is the Amp Hour Podcast. Recorded June 16th, 2015. Episode 254 with guest Andreas Olofsson. Adaptivas Amplitive Abacus.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics.

**Andreas Olofsson:** And I'm Andreas Olofsson from Adaptiva.

**Dave Jones:** Hey Andreas, thanks for joining us.

**Andreas Olofsson:** Thank you so much for inviting me.

**Dave Jones:** And you're in Boston.

**Andreas Olofsson:** Yes, just outside.

**Dave Jones:** Have you always been in Boston? Or is this just where you're living and working now?

**Andreas Olofsson:** No, I came here in 2006. But I've been, you know, I'm from Sweden originally. And I've been in and out of the U.S. since 1998.

**Chris Gammell:** And so if people don't know, you are the founder of Adaptiva. And the name that people might know more in the home is the Parallelo, which is a large, well, not a large, just a small computer that has large capabilities basically doing parallel computing. So can you tell us a little bit about how that all got started? Maybe the lead up to the whole project?

**Andreas Olofsson:** Yeah, yeah, yeah. So I started this company at Adaptiva in 2008. And, you know, the premise behind the company was that all of the computing is going to be parallel someday. And I came to that conclusion while working at Analog Devices for 10 years, working with some big honking iron DSPs, one of them called Tiger Shark DSP. And it was a good processor. But it was too big, too power inefficient. So it lost the battle to ASICs and FPGAs. And we ended up spending like $100 million. And at the end of the day, I was laid off and then rehired to work on something else. But...

**Dave Jones:** So the Tiger Shark was even less power efficient than an FPGA?

**Andreas Olofsson:** Oh, yeah. Not even... It wasn't even close. Really? Why was that? Was... Well, so, I mean, FPGAs are quite efficient if you customize your code to the problem.

**Dave Jones:** Right. Of course.

**Andreas Olofsson:** Right. So if you take something like wireless communication, where the Tiger Shark was supposed to go, if you want to look at forward error correction, like Turbo, Viterbi, Reed Solomon, it's all bit quiddling. And the floating point performance of the Tiger Shark was useless for those things. Ah, got it. Interesting. So there were some things that it was pretty good at, but it was trying to do everything, you know, in the kitchen sink pretty much, right? It was a video processor, a floating point processor. It ran an operating system. And when you add all that up, it just is very inefficient. And so, yeah, the FPGA was definitely winning.

**Dave Jones:** Ah, interesting. So was this like a management thing where they kept trying to pile on requirements for this new Tiger Shark processor? Or can we go into that?

**Andreas Olofsson:** I think it's a pretty common microprocessor or chip design issue or disease. Disease. Yeah. Yeah. Right. That feature creep, you decide, you know, what we need is one feature. And the problem is that every feature on its own looks great. Right. And the architect or the manager will say, you know, this is going to win us a socket because it gives us 10x on this, you know, kernel. And then before you know it, you have 100 of those fiends, you're cheaters, each giving 10x on a certain kernel. But in aggregate, they destroy the whole product.

**Dave Jones:** Got it. Got it. So what would have been the comparison with, like, say, the Tiger Shark, for example, if you tried to duplicate the equivalent general purpose functionality inside an FPGA, the Tiger Shark would still be more efficient, wouldn't it? Because it's dedicated silicon. Yeah.

**Andreas Olofsson:** Yeah. Yeah. No doubt. Right. If you look at, I mean, that's an FPGA versus anything, right? Right. If you take a function like a Resolment, right, or a turbo decoder, right, if you put that in FPGA versus making an ASIC for that, you're probably talking about 20x. Oh, wow. Oh, okay. 20 times. Wow. Yeah. Maybe even more. So ASICs are always going to win. The problem is nobody can afford to spin them. Right.

**Chris Gammell:** Right. Because it has to be so perfectly formed to an application. If it's not a huge application, you'll never make your money back, right? Right. Exactly.

**Andreas Olofsson:** But it's a really, really fascinating optimization problem because if you look at where FPGAs are going today and where all the application-specific processors, it's kind of hitting the sweet spot between programmability and flexibility and performance. So there are two opposite forces pulling it.

**Dave Jones:** Right. With regards to the ASIC side of things, do you, from your experience, do you see it getting worse and worse, like more expensive to spin custom ASICs? Or is there anything out there that's looking promising in terms of people being able to spin ASICs relatively cheaply?

**Andreas Olofsson:** Oh, yeah. I mean, I've been writing about this for a while. In some sense, it's actually cheaper than ever to spin an ASIC.

**Dave Jones:** Really? Okay. Why is that?

**Chris Gammell:** Just like on a per-logic-gate kind of pricing basis or what?

**Andreas Olofsson:** Yeah. Well, per-engineer basis. You know, when I started out in 1996, we were still doing schematics. And we were just starting with logic synthesis. Oh, really? So synopsis tools and cadence tools. Wow. Okay. And to make it go fast, we were doing a lot of silly stuff like custom design and dynamic logic and transfer gate-based logic. Yeah. Right. So it was really slow, really costly. And today, if you take the right approach and you target a certain market, you get free libraries from the foundry. So, you know, you don't have to design anything below metal. Basically, what you're doing is you're connecting transistors with metal wires. So my design approach, for example, I never go below the first metal layer. So when you design an ASIC, you will have anywhere from five to nine metal layers to hook up the gates with. But the gate library, somebody else did for you. And so it's actually, you know, quite simple.

**Chris Gammell:** Yeah. It's just kind of like calling functions basically on a higher level program type thing, right? Exactly.

**Andreas Olofsson:** I always program at a higher level of tracking. So I'll write Verilog code and then, you know, push that in to a synopsis tool together with Tickle script. Yeah.

**Chris Gammell:** Chip designers love Tickle.

**Andreas Olofsson:** I know that one. And so, I mean, I can, the flow I have for doing FPGA design or chip design is very similar. It's just, you know, different Tickle scripts, different tools, a few more steps on chip design for sure. But you can, today, I mean, case in point, we did all of our chips with less than three designers per chip. Oh, wow. Nice. Yep. And some of those chips, like the latest one we did at 28 nanometer is 200 million transistors that we did in 12 weeks with three engineers. Oh, wow.

**Dave Jones:** Because that's just right in top level code, right? Yeah. You don't have to worry too much about the silicon level or even at all. Perhaps you don't have to worry about it.

**Andreas Olofsson:** No, there's some tricks to it. You have to be very careful and you have to have the right methodology and take a lot of margins. We're definitely not designing close to the edge like somebody like Intel would do. Right. You know, we're not pushing the envelope at all. But if you stay straight down the middle and you have experience in doing chips before, it's absolutely easier than ever. Hmm.

**Dave Jones:** So with targeting either an FPGA or an ASIC, what are the major differences there between targeting them? Would you target an FPGA first to actually trial your chip or you wouldn't bother? You'd just shoot for silicon?

**Andreas Olofsson:** No, we definitely prototyped everything in FPGAs first. Because it's, you can run things fast. You can actually validate with complete test suites or kernel loads. So it gives you the confidence of running enough clock cycles that it works. It's another synthesis tool. So sometimes the tools will find and uncover different problems. They shouldn't, but sometimes they do. And I mean, the FPGA, you can spin that in a couple of hours or minutes, whereas the chip takes you five or six months. And that's the killer for ASICs, really. It's not even the cost. It's the time lost.

**Chris Gammell:** So when you are prototyping on FPGAs then as well, so does that mean that you also have those libraries from the foundries and such to actually push down to the FPGA? Or is it like you have to customize that kind of stuff and do high-level logic with error? Or that's...

**Andreas Olofsson:** No, I mean, we write our code in Verilog, you know, vanilla generic Verilog. And so it's really just a matter of feeding that into either a logical synthesis step to map to an ASIC library or to map to the real inside the FPGA.

**Chris Gammell:** Cool. Yeah, that's good. And so when you're targeting... So I don't actually know. So 200 million gates, I really don't have any kind of measure on what that would actually be these days. What does that mean for... If you have to target an FPGA that's a similar size that could fit the same design in it, what kind of size FPGA do you have to target to match that same 200 million gate thing?

**Andreas Olofsson:** I mean, it's a big one. It's an enormous one, right? Think of the one of the...

**Dave Jones:** Is it a single FPGA or is it one of those huge, big boards with like 20 FPGAs on them that are designed for ASIC prototyping?

**Andreas Olofsson:** No, we couldn't afford one of those. Remember, we're... Oh, right.

**Dave Jones:** Because they're very... How expensive are they?

**Andreas Olofsson:** You know, I knew that I wasn't rich enough to ask. So I didn't. But I can imagine them being, you know, $100,000 range or something like that.

**Dave Jones:** Ooh, yeah.

**Andreas Olofsson:** Wowza.

**Dave Jones:** Because each FPGA on there is like $5,000, right? Yeah. If you have to ask, you can't afford it. Yeah. So could you fit everything on the one FPGA or would you just do, well, let's just do a little block we've got?

**Andreas Olofsson:** So, yeah. So because our design is very tiled, it's very encapsulated, we felt that, you know, taking a couple of tiles would be enough. So we actually took a modest-sized FPGA and pushed some tiles in there. I think we were up to four at maximum inside the tile, and we had a 16-core chip being taken. So... And it was, yeah, it wasn't perfect. It did flush out almost all the bugs.

**Dave Jones:** Right. Okay. But did you end up, did you get first spin on your ASIC silicon? Did you get it first go or did you have to go, oops, we forgot something, and re-spin it? Barge wire.

**Andreas Olofsson:** So we've had four versions of the chip. The first one was something I did at my basement and definitely a prototype. The first one was really just to get enough money so I can get a team together. So I would call that an intentional punt, right? Prototype. That was version zero. And then version one was supposed to be a product, but one of our vendors made a mistake, and so we had to spin it. But, you know, it happens, right? You're only as strong as your weakest link, and in this case it was our partner. And so we got retribution for that. I was going to say, did the partner pick up the bill? Did they have to pay for it? Right. Yeah, they did. They always wanted to. They did.

**Dave Jones:** Ouch. So is a goof-up like that common? Is that something that the vendor factors into there, you know, oh, look, we're going to screw up one out of every ten times, and it's going to cost us?

**Andreas Olofsson:** I think most people expect some kind of spin, but it depends on how you schedule it and if you can work around it. Pretty catastrophic. So, yeah, it's hard to afford those kinds of things when the margins are pretty slim. So I wouldn't say they build the pricing or anything. This was pretty unusual. I don't want to go into it too much, but so, yeah, so that first one, you know, I call it Rev 1, did not make into production, but Rev 2 did, and Rev 2 is the one that now is shipped to tens of thousands of parallel boards. So there was just kind of really one mess up there.

**Dave Jones:** And so this is the one you ship for the Kickstarter project? That's right, yeah.

**Chris Gammell:** Could you tell us some more about the actual architecture? So you told us before the show started that this is a completely new architecture, and you said that one of the thinking behind it was that you're not necessarily going to be able to compete with ARM in the marketplace for a consumer level, but from a massively parallel level, you will. So could you tell us, like, how it's different than some of the architectures that people might already know?

**Andreas Olofsson:** Yeah. So it's, so the idea was that besides being parallel, the future of computing is really heterogeneous, meaning that there's no one tool that will solve all problems, and that you really have to have three tools in your toolbox, and one being a microprocessor that runs the operating system, the general purpose cleanup. And, you know, x86 in ARM is fantastic at that. It's, you know, extremely well-positioned machine. But if you're talking about high-performance math, all that baggage that's in the processor architecture, I mean, the same baggage that I found in the Tiger Shark, it's there, which means that you're never really going to reach the top level performance that you need for certain applications. So you need something else that's more specialized.

**Dave Jones:** Right. So what sort of functionality would you put inside, well, what functionality did you put inside your core, which is called the epiphany? Is that correct? Yeah. What sort of functionality did you put inside that to go, go, right, this is going to be highly optimized and also kind of universal enough so that it's good enough for a lot of different applications? Is it, you know, floating point matrix stuff? What sort of, you know, functionality is in there?

**Andreas Olofsson:** So first thing, we threw out everything. That was the major realization. That throw out everything and then take pieces in one at a time. And so basically things have been accumulating since the day one of processor architectures. And some of the things that were put in in the 1980s are not necessarily relevant today. Like what? So, you know, take, for example, the cost equation for how much does an instruction cost versus how much does a data movement cost. Or on the compiler side, is it good to have a few registers or a lot of registers? And, you know, what kind of optimizations, especially what kind of optimizations can be done in the compiler? And so, you know, I looked at all the RISC architectures, including ARM and MIPS and the PowerPC, the Spark, some of the DSP stuff. And I realized that, you know, the majority of the instructions aren't needed. And certainly not needed if you want to do a math coprocessor. And in a way, it's kind of retro going back to where the DSP, the digital signal processor came from in the 1980s. It started out as a multiply-accumulate unit. And then they tried to make that a little bit programmable. So they started bolting on feature after feature. And before you knew it, when they ended with the tiger shark, it was a, you know, full-blown microprocessor built around a multiply-accumulate, grown up in the weirdest way. So now we go back and say, let's see.

**Dave Jones:** That's funny to visualize. I'm sorry. It's just, you know, like this multi-armed beast. Yeah, right.

**Chris Gammell:** The hydra of the computing world, right?

**Dave Jones:** I love it. So this is basically just a math coprocessor. That's it. Yes. It's not really useful for general-purpose computing as such.

**Andreas Olofsson:** That's right.

**Dave Jones:** And what sort of stuff works best on it? Is it matrix math? Is it, you know, what from a math point of view?

**Andreas Olofsson:** So since it's a coprocessor mostly, you generally want a problem that is compute intensive. So you're looking at a class of problems like matrix multiplication, linear algebra, filters, convolutions, things that are, you know, n squared or n cubed in complexity. Right. Because if they're not, if they're data limited, then you're always going to be IO limited. And there's really no purpose for this math coprocessor. So there has to be something extremely compute intensive. And so that's where we're coming from. And there's no... So that's a lot of like telecom, stuff like that? Yeah. So, I mean, so wireless communication is a prime example. That's really where I came from. And that was a great fit. Imaging applications, another great application area. Whether it be medical imaging or video analysis or the kind of machine vision that's getting really popular today.

**Dave Jones:** What about compression and Bitcoin mining and all that sort of jazz?

**Andreas Olofsson:** So we try to stay away from things that were standards-based. Because in a lot of application areas, those become ASICs. Got it.

**Dave Jones:** Yep.

**Andreas Olofsson:** And this is why I really like the imaging space is because there are no standards, right? There's no limit to how innovative scientists and computer programs can be on the computer vision side. Versus, let's say, an H.264 is a solved problem, right? People banging into a little IP block or an ASIC. And it's not going to be faster than that. Now, sometimes there's an advantage to have programmability. Because you can do multi-standards. And if the standard is involving. But that's kind of a second order concern.

**Dave Jones:** Right. Now, you mentioned the data. Like it's sort of computational intensive stuff instead of data. Intensive stuff. But ultimately, you've got to have like some data in there. So like what's like the size of your onboard? I'm sorry, but, you know, both Chris and I are like, you know, CPU architecture dummies here. So we're probably going to make fools of ourselves here. But what is sort of like the on-chip cache or the on-core cache memory? How much data can it actually, you know, process without having to go to external memory? If you know what I mean.

**Andreas Olofsson:** Yeah. So we have on the chip that we ship with Parallel, we have a half a megabyte of on-chip SRAM.

**Dave Jones:** Is that general purpose or is that like, is that spread across each core?

**Andreas Olofsson:** Yeah. That's spread out into a number of banks. So there is actually 64 banks. So, you know, that half a megabyte is split into 64, 8 kilobyte banks.

**Dave Jones:** Okay. So each core, because you've got 64 cores, each core has its own dedicated bank, does it?

**Andreas Olofsson:** Yeah. Now, I was actually referring to the 16-core chip now. So, but each core has four banks. So there's 64 banks in total. Got it. And the, you know, which is, you know, so lots of small banks, but each bank with enormous amount of bandwidth. So, because all those 64 banks can now be accessed simultaneously.

**Dave Jones:** Oh, nasty. Okay.

**Andreas Olofsson:** So, so it's, you know, it's, it's the, it's the curse and the power that you have in FPGA as well. In FPGA, you have all these block ramps. And if you design your, your system correctly, that thing will fly. And if, if you, you know, but it takes a lot of love and care to get it to work like that.

**Dave Jones:** So with these, you know, supercomputer multi-core processor chips, it's all about the flops per watt, right? Or gigaflops per watt, is it not? And is that where yours currently leads? Is world leading? Is that right? At 50 gigaflops per watt? Or have you done, actually, if you've ever got a new one that's actually more powerful than that now?

**Andreas Olofsson:** No, so yeah, definitely the gigaflops per watt is, is the metric. It's just, you know, you have to be very careful how you count it. And so, are you, are you counting at the, at the core level, at the chip level, at the system level? Are you counting for an application or some data sheet number and so forth? It's so hard to compare. And that's why you always have to take it with a grain of salt. But I think the true number that you can always look at is how many square millimeters of silicon are people using? That one is really hard to cheat. And...

**Dave Jones:** Got it. Because I, I'm looking at a table here where yours is twice the gigaflops per watt of, say, an NVIDIA, you know, GT 630 processor or something like that. Like, you know, video processor. Is that right? Because they're, they're like huge dyes, aren't they? They're massive bits of silicon.

**Andreas Olofsson:** Yeah. So then they have more performance, but they have more power as well, for sure. And it's, I mean, it's a, it's a tight race for sure. And, and the key...

**Dave Jones:** Is that something you're deliberately targeting? Is the, like, is the per watt thing, the smallest thing per watt?

**Andreas Olofsson:** Yeah, that's the metric. That's not, that's not necessarily even targeting. That's a byproduct of the architecture. Right. So the, the idea is that anything that runs off a battery or wants to be small, energy efficiency is the only thing that matters going forward.

**Dave Jones:** And is yours well placed in that respect? Who are your major competitors in that field in terms of, you know, energy efficiency?

**Andreas Olofsson:** So it's, it's, it's kind of everybody. It's, FPGAs can be very energy efficient. GPUs can be very energy efficient. And ARM certainly has been, been pushing their energy efficiency versus other processors in the data center space. But they're dominating the smartphone space. And they, they got there by being the most efficient. On the wireless communication side, all the base stations have their own ASICs. So there, we, we compete with ASICs as well. So it's, it's, it's, it's an all out war with everyone, everyone versus everyone.

**Speaker ?:** Right.

**Dave Jones:** Right. So, so what is, what is your ultimate business model? Is it to be like ARM and actually sell your core and, and actually, sorry, license your core out? Is that the goal or do you want to make chips? What do you want to do?

**Andreas Olofsson:** So we, yeah, we're definitely open for licensing and, and that has been our business model. And, but what we found was that it's very hard to do the licensing of a processor architecture without having the software to go with it. You can license the solution.

**Dave Jones:** As in the software as in the compiler.

**Andreas Olofsson:** No, that, that we have. I mean, the whole application stack.

**Dave Jones:** Right. Oh, the application space. Of course. Nobody wants it. It's a chicken and egg thing. Nobody wants to use, no manufacturer wants to use your processor if there's no software, if there's no apps for it.

**Andreas Olofsson:** Right. And nobody's going to build software for a processor that doesn't sell a billion smartphones. Right.

**Chris Gammell:** Yeah. Money. Oh, goodness. Well, and it's, it's almost like how, how you were saying that, you know, you, you guys take advantage of the software coming from the foundries. That's kind of what people are also looking forward in order to shorten their development cycle so that they can have a three person team and develop some, you know, consumer level product or some other type of product there. Yep.

**Andreas Olofsson:** That's right.

**Chris Gammell:** Huh.

**Dave Jones:** What is, what is the difference between, well, the sort of efficiency is probably not the right word, but you'll understand in a second, between actually doing a supercomputer with separate chips, you know, be they 64 cores each. And then how, or between the cores on the chip itself. Is it better to go for a larger and larger silicon and have more and more cores on there? Or is it better to have, or is it more efficient, cheaper, whatever, to have multiple chips with only a smaller number of cores? What's the trade-off there?

**Andreas Olofsson:** It depends on the architecture. Sure. In our case, definitely the bigger we can make the chips, the more we gain. We get kind of like a super linear speed up because if we put lots of small chips on a board, we're going to be IO limited. Because the, you know, let's say you have a BGA with a one millimeter pitch. There are only so many traces you can fit on that board. On the, inside the chip, a wire might be, you know, 0.1 microns. So it's tiny. You can fit thousands of wires.

**Dave Jones:** So what's the current limit to what size you can make your die? I mean, like you can't make it the size of a 300 millimeter wafer because it's, there's a thing where it gets like yield versus, you know, cost and all that sort of thing, isn't it? Yeah.

**Andreas Olofsson:** So the, the, the, the max die size has stayed pretty constant for forever, pretty much. And it's kind of tightly related to process scaling and Moore's law in that you go to the next process node when it's mature enough. And so we talk. And, and what is that size? What is that size limit? Let's say around five to 600 square millimeters. So like 25 by 25. So, so if you can, if you can, by, by maximizing the size of the die, you can fit more memory on the die, which means that you can solve a bigger problem. And if you have a problem that scales as N squared or N tubed, you've gained, right? Because that means that you, you, you, you, you got your gap between bringing data in and out versus computing grows. I see.

**Chris Gammell:** And what are, what is an example of a problem that would scale like that? I mean, again, I've, I, I'm going to show my naivety here. I don't know what people would push to a cluster of supercomputers like this. I mean, what, what would, what would scale like that square or cube like that, what you said?

**Andreas Olofsson:** So, I mean, one, one classic one is let's say you're doing some image processing on a, on a video stream. Um, if you can fit the whole frame and made, or maybe a frame and reference frame on the silicon die, you can crunch your wave on that for a pretty long time without everything having to go off chip. Uh-huh. Yeah. But, um, if you, let's say you could only fit a fraction of that on chip, then you, but it can be constantly shuffling, shuffling temporary results on and off chip.

**Chris Gammell:** I gotcha. Right. And then reconstructing and all the other stuff that goes along, all the other overhead that goes along with that then, right? Yeah.

**Andreas Olofsson:** Yeah. So all the, all that temporary data, you're going to have to put in DRAM somewhere and, uh, you're going to end up with, you know, multiples of the, uh, of the bandwidth that you need for the actual, uh, video frame in and out.

**Dave Jones:** Does that mean like, is video sort of like the killer, uh, app for parallel processing? It seems to be, uh, because, you know, we go into like 4k resolution stuff, you know, crazy resolution, crazy color depth, you know, like absolutely phenomenal stuff. So, and, and you want to process it at, you know, 60 frames per second these days and all that sort of stuff. Is that the killer app you're looking for? Hopefully that might, um, sell your core.

**Andreas Olofsson:** Unfortunately not because the, uh, the, you know, the, the TVs are all going to be standards. So, you know, 4k resolution is, is just drawing pixels on a screen.

**Dave Jones:** And they're going to enhance once a standard comes along, they spin an ASIC for it. That's right. Right. Damn.

**Andreas Olofsson:** But I mean, there, there, there are, there are plenty of examples of, of super, um, uh, challenging applications that can't be solved today. Uh, you know, the one that I, one of the ones that I liked the most are, uh, if you look at all the drones today that are really taking off, um, we know that there's no, nobody today that can do, uh, autonomous navigation and autonomous obstacle avoidance properly. And the reason for that is there's just nearly, not nearly enough processing power. Um, you have, let's say a 50 gram payload or something, maybe a hundred grams. And, uh, you might be able to do it if you had a big honking Intel processor sitting in your laptop.

**Dave Jones:** But that's taking, you know, a hundred watts. Yeah. Yeah.

**Andreas Olofsson:** But you can't do it with a, with a little tiny processor there right now. So to me, that, that's an example of, um, in order to fly fast with a drone, you might be flying 20, 30 miles an hour. And, you know, what if you want to fly through trees? Yep. Oh yeah. Uh, you don't want to hit any trees. You need to make those decisions in milliseconds. That's, that's a tough problem.

**Chris Gammell:** Yeah. Right. Right. Cause it's not just bringing in the frames and, and crunching on them. It's also processing on them and doing all of the detection and the, and then reacting and all that other stuff. Yeah.

**Andreas Olofsson:** You have to filter, you have to detect objects. You have to make sense of the objects. It's a very, very tough problem.

**Chris Gammell:** Yeah. So how do people, okay. So people can obviously buy this as a very, very affordable. It's a, I'm amazed at how accessible this is. Actually. Um, I was mentioning before the show as well, just even having like a zinc on board, that's amazingly accessible as well for the price. Um, but if someone did get this, where do they normally start? Is it like, start with, uh, like some kind of Python programming on like the, like a higher, like an OS running on the ARM processor? Or is it, uh, what, what's it normally running? What, what can, what can you really do when you're for someone that's getting started with it?

**Andreas Olofsson:** So, um, you, the people who get started, it will, will, will start with, you know, reading through the manuals, look at our SDK. Okay. And, and, and, and think, right. How do I, how do I make use of this thing? How do I send out? They think of each processor as its own core. Um, and, uh, and then you'd start on the ARM. You have some problem, the application code that you want to work on. And, um, then you take some part of that application. That's the bottleneck. You'll send out, you, you'll divide that up into 16 work threads. You'll send each thread to, uh, to an epiphany core. And there's your, you know, your initial speed up. And if you're lucky enough, you don't have any communication between the threads. Ah, okay. Right. If you, if you do have communication between the threads, things all of a sudden got a lot more complicated, but that's no different from any other parallel programming problem. Well, it is, it is a little more bare metal here. So it's going to be harder, uh, with, with this architecture until now. Okay. But it's, um, it's kind of a general problem. So I found is that the people who have really done well here are people come in with all the experience in parallel programming already. And they just kind of have to frame, you know, uh, adopt that experience to the epiphany platform. Um, the, the, the people who have struggled more have been people who don't have the parallel programming experience. And this is their first, you know, kind of first try. That's been, that's been rough.

**Chris Gammell:** Oh, people that are used to just a micro and, and basically like sequential programming, just kind of chunking through a task, that kind of idea.

**Dave Jones:** Yeah. Have you got any real good, uh, examples of, uh, acceleration where people have actually used it in a real application? What sort of performance increase they got by actually shuffling off the ARM processor and onto the, uh, core?

**Andreas Olofsson:** Yeah. And we, we, we've done it all with things, uh, single processing kernels like matrix multiplication, FFTs. Um, some other people have done it with, um, various, um, compute intensive applications like, uh, password cracking, for example. Right. Yes. Uh, one, one student, um, uh, sponsored by, uh, these guys in Russia who have a very well-known, um, package called bcrypt. Uh, they, they did a project for Google Summer of Code and they got amazing speedups. Um, have you got a number? Can you throw a number at us? Um, 25X. Whoa. Right.

**Chris Gammell:** Yeah. That'll, that'll do it. Man, that's nuts.

**Dave Jones:** So can people actually buy your, the chip on its own or, or do they have to buy the development board?

**Andreas Olofsson:** Um, it's, it's open for buying. It's not in production yet. It's sampling. Okay. Uh, and so, uh, right now people have to reach out, reach out to us. We're, we're, we're trying to get into, uh, DigiKey and RS components channels. Um, and, uh, but yeah. It's certainly available. We got, uh, tens of thousands of them built up waiting to, uh, waiting to be shipped.

**Dave Jones:** Excellent. Can you, can you tell us about your, your Kickstarter campaign? Cause this was what three, was it three years ago? Almost.

**Andreas Olofsson:** It was quite a fall 2012.

**Dave Jones:** Wow. Okay. Can you tell us about, uh, that? Did you ship on time? Did you have any major issues? What happened? Did it all fall apart? Did you end up losing money and go, oh, never again? Um, so yeah, I think we all know the answer to that one. Um, well tell us, we, we, we love to hear these horror stories. Come on. No, not horror stories. Opportunities for learning. That's what it does. Right.

**Chris Gammell:** Yeah. Yeah. Okay. We're living vicariously through others.

**Andreas Olofsson:** So, um, so, um, so we, you know, two, summer 2012, I just come off a, um, a bunch of trips to, uh, you know, all over to try to license our architecture, uh, to the smartphone manufacturers and, uh, you know, without software application, it wasn't going to happen. Um, so, and around that time too, uh, Raspberry Pi had just launched and been hugely successful. Um, and, uh, there was also the, um, the, uh, gaming platform and Pebble. I mean, Kickstarter was, was hot and I thought, wow, this is fantastic. I mean, these people, here's a, here's, are these, um, consumer applications and they sell 10 million. And, uh, I thought if we, if we have the, you know, the best processor born, you know, on the planet, we'll sell more than that. That was my, that was my incredibly naive thought. And so I decided that we should launch. Um, and, um, uh, we did, but I mean, we, we made all kinds of mistakes. Um, it wasn't, it wasn't nearly polished as some of the other platforms or, um, our, our, our marketing kind of failed. The, I did not understand that Kickstarter really is about a, a, a finished device that consumers can use. It's not about selling platforms, right? It's not for developers and programmers. The size of the developer market is a tiny, tiny fraction of the size of the consumer market.

**Dave Jones:** The, the funny thing is though, that's what Kickstarter is really for. It's for building businesses and, and up from that sort of ground up. You know, it's not to sell a Polish finished product or that was never its intention anyway.

**Andreas Olofsson:** Um, and so, yeah, so, so the, the, the fact was that the market wasn't nearly as big as I thought it was. Uh, and we, I think we raised like a hundred thousand dollars on the first day, uh, which is great, but it's not nearly enough to build a chip on or to get a chip into production and build a board, um, and sell it for $99. So, um, so we, we knew we were kind of in trouble, but, uh, we, um, we really wanted this to work. And so we worked hard for 30 days, uh, kept working on material, disclosing more information. We opened our data sheets and reference manuals and, uh, and, and worked, worked very hard. So I think we, we did that right. But, uh, after 30 days.

**Dave Jones:** And you managed to get your goal. Your goal was 750,000 and you got nine, almost 900.

**Andreas Olofsson:** Yeah. Yeah. I mean, towards, towards the end there, it, um, uh, we released a new video, right. That was less academic, more consumer oriented where we, we showed off, you know, the, the prototype system headboard, uh, or no, it wasn't even a Zedboard. I think it was a Zing 706. We had, we had both that we were playing with and, uh, and an FMC with our chip on it. I mean, this was a, uh, uh, you know, complete prototype. Uh, and so we, we showed what we had and we showed, told everybody where we wanted to get. Um, but even now looking back, that, those are some pretty, pretty lofty goals. Say, you know, here you have an eval kit that costs a thousand dollars and that's, you know, like a, um, uh, uh, regular sheet paper, right. Um, a, um, and then we're going to take that, all that electronics and turn it into a credit card and get the price down by a factor of 10 to $99. It was, it was very aggressive. Um, and so.

**Dave Jones:** Did you ultimately do it though? Yeah, we did. Excellent.

**Andreas Olofsson:** Uh, sounds like it worked. We, we did.

**Dave Jones:** So, so you actually raised enough money to just enough money to do it in the end or?

**Andreas Olofsson:** No, we didn't raise nearly enough money, but we did it anyway. Right, right. Okay. So, so we, in the end, I mean, the, the, um, on the, on the business side, I made a lot of mistakes, uh, in, you know, pricing it too low. Um, right. So, you know, on its own, it didn't become a viable business. Um, and I don't think we're the only ones from Kickstarter campaigns to do that. In fact, I think the, the more money you raise on Kickstarter with a lower price, the more trouble you get yourself into. Um, and, uh, and so for us, you know, if, if we would have set the price at $200, there's no way we would have met our goal. Right. Right. At least that's my feeling.

**Dave Jones:** You think, you think psychologically people, people wouldn't have bought it. You think that $99 goal, that $99 price was a psychological thing where people, you get, oh yeah, it's only 99 bucks. Oh, here's my credit card.

**Andreas Olofsson:** I, yeah, I, I still think that's, you know, the, the price has a lot to do with it. And he, I mean, look at the success of the, the new computer, the chip computer.

**Dave Jones:** The $9 one. Yeah, exactly. Cause it's $9. People don't care. Yeah.

**Andreas Olofsson:** Right. I think that the magical market now is not 25, it's $25, $99, $25, right? That you need to be below 25 to really reach the consumers. Um, yep. And to be an impulse buy. Which is so nuts.

**Dave Jones:** But, but, but you weren't targeting consumers though, were you? Or was that your intention to sort of get one into every home, like the Raspberry Pi kind of, you know, thing? Oh, the whole world needs to learn. Every grandmother needs to learn about supercomputer programming.

**Andreas Olofsson:** No, we were, we were, um, targeting hackers and developers, but you know, really targeting people new at a program. Right. And, and, and I, yeah, I, you know, thought there would be more people like that. I mean, there's probably 20 million programmed. So that was our market. Uh, but, um, it's, uh, so we got, let's say 5,000. Um, and, um, it's, um, I mean, it's a pretty good number, but it's not, it's not quite enough.

**Dave Jones:** Right. Yeah. I, I think that was a realistic number. I mean, you know, to get 5,000 backers, for example, that's a lot in the, in, you know, for a product like this, I think. So, so I think you did really well to actually get that many.

**Andreas Olofsson:** Yeah, no, I think so. I mean, I just respect that we, we, we did great. Um, it just, the sad part is that it's, it still wasn't enough. Right. Um, and so, uh, so we, we started, you know, we started building and in the beginning things were going well. Um, um, in, you know, I think the, the major obstacle was that the, the $99 price point we set, we started the campaign. And since we didn't have a board build out yet, we could have no way of knowing what the pricing would be for the chips and the components on the board. So, so we didn't have anything pre-negotiated with any of the vendors on the board. In fact, we didn't even have all the components picked out yet.

**Speaker ?:** Right.

**Chris Gammell:** Right. It'll look something like the, the zinc development board, but cheaper. Yeah. Right. Exactly. Yeah. Whatever it needs to do. Cheaper.

**Andreas Olofsson:** Um, and so, um, and so, um, and so, um, and so, um, and so, um, and so, um, and so, so, uh, so when we started negotiating pricing, it was, it was hard. I mean, uh, it was, um, nobody's going to give their stuff away for free. So it was a lot of convincing that this was going to be a, you know, very big effort and open source, open source helped a huge amount because it became a kind of reference design for a lot of these chips on the board. Oh, right. Right. Yeah. So that really helped, that really helped drive the, the, the prices down. Um, and, um, you know, raspberry pie certainly helped. We were, we were going to be the next raspberry pie. Um, and, uh, so that helped convince people that they needed to give us the pricing that, that could get us $99. Got it.

**Dave Jones:** And you're currently selling it on digi key for, depends on the type. You currently sell it for 126 to 264. Is that right?

**Andreas Olofsson:** Yeah. Yeah. So we have, I mean, those are distributed pricing. Um, we have our official list pricing on, um, on Amazon. So we have a 99, 149 and 249.

**Dave Jones:** Right. So, so you ultimately in after three years, you ultimately can sell it for $99 and make a viable business out of that. Or is it still sort of, oh, we're sort of, you know, selling it at cost kind of thing or at a loss to.

**Andreas Olofsson:** No, we're making money on every board, uh, gross profit. Um, but, uh, I think the, and I, I, you know, I, I, I think this is pretty common for, for people, you know, the hundreds of people who, uh, who built single board computers is unless you get to a hundred thousand boards or above, um, and, or working out of your basement in your free time, you can't make a living. Right. Yeah. Yeah. Right. Of course. Because, because, you know, an engineer in the U S, um, you know, if, if you're not making a hundred thousand dollars somewhere, it might be, you're probably underpaid. Right. So you have to figure you, your cost is a hundred thousand dollars. And so, um, that's for one engineer. So if we sell 10,000 boards, which we have and making $10 per board, we just made a hundred thousand dollars in profit. Um, that pays for less than one engineer with healthcare and everything else.

**Chris Gammell:** Yeah. I was going to say, usually I put it, I pick it at 200 K for overhead and everything else. That's usually a safe bet, but yeah. And that's, yeah.

**Dave Jones:** And, and it's like that $9 chip computer. I was reading, uh, you know, article, who was it? Oh, we talked about it last week. Yeah, we did. Olimax. Yeah. Where they can't pot. Yeah. They can't possibly make that a viable business. They can't. It's just not possible. Right.

**Chris Gammell:** But it almost becomes like a, like all of this almost is like a, marketing platform for the, for the chip on board. For them, it's, they're obviously, they don't, they're not running the, the, the chip. That's an all win or whatever, all winner. Uh, but for your stuff, it's, you know, this is, this is actually, I think, brilliant marketing for, for the, for the epiphany and for, and, and like you said, for, for the zinc and other things, you know, where it's accessible. And if there's a community around it, much like BeagleBone and, uh, not like anyone's going to be able to get a Broadcom chip, but you know, the Raspberry Pi as well, there's communities around it. And that, that is a net positive for the platform.

**Andreas Olofsson:** Yeah. No, absolutely.

**Dave Jones:** Would your holy grail be to get one of these in every smartphone? Because smartphone is the consumer platform of choice, right? It's, you know, it's just what everyone has in their pocket. Would, would, would that be of, is that a goal that's even possible to get the manufacturers to go, well, let's, you know, we don't know yet, but let's stick this chip in here and, you know, and the capabilities there for running all this energy efficient, you know, parallel processing in a phone. Because phones are doing some very heavy duty processing these days and it's, you know, becoming a big, uh, uh, problem to get, you know, um, and to get performance while maximizing the life of the battery.

**Andreas Olofsson:** Um, yeah. Uh, and so I, I think the, the phone, the biggest platform, the most prolific, uh, prevalent platform is going to win because that's where all the money is. Um, and so it used to be the PC. Now it's the phone and in the future, it, if you follow Bell's law, it might be something even smaller. So, you know, maybe it's a watch or maybe some other wearable device.

**Dave Jones:** Right. But then IO becomes the issue, you know, it's the user interface and all that sort of jazz.

**Andreas Olofsson:** Yeah. Yeah.

**Dave Jones:** But is it possible to sort of get one of these, is it possible to convince one of the manufacturers to put one of these in your, you know, like maybe a high end phone and it's a marketing thing. Woohoo. Look, it's got a parallel computer in it, you know, but if there's no apps to utilize it, then I guess the answer is no, right?

**Andreas Olofsson:** You have to come with a solution. Um, and, uh, and so our, the approach was if we keep working with, uh, universities and, and, and the community and everybody else, eventually we'll, we'll lock onto one of these killer applications. And then we'll work with people to create the, um, create the whole solution that then could go into a smartphone.

**Chris Gammell:** So I'm curious about, you know, speaking of solutions and stuff like that, uh, and, and, and the universities. So on the software level and, and, you know, you'd mentioned kind of getting started on the arm side, but what are people, I mean, how much is the flexible part of the zinc, which is like a FPGA core around it? How much is that getting used? And then how much, like, what, what is the breakout? Like, uh, as you dive down through, through abstraction layers to the kind of, to the bare metal, where, where do, where do people go after just the arm core? You'd mentioned the breakup on the, the epiphany, but.

**Andreas Olofsson:** Yeah. So, so the, um, there's, there's definitely, um, a smaller community that uses the FPGA logic, but it's, it's completely accessible. You, you know, you download the free web tools from Xilinx and you, you burn a bit stream, you put that on the SD card and you have your own custom FPGA logic. So we've seen a few people blogging about it and trying ideas. Uh, the guys doing the, um, that password cracking one, they actually ran it on the zinc as well as on the epiphany. And the zinc was actually the, the winner over the epiphany even. So, so in terms of writing was FPGA was number one epiphany. Um, cause it was, uh, you know, uh, it's all bit level shuffling stuff, right? Um, it's, uh, it's doing a bunch of XORs on, and, on, uh, um, and, and you don't need 32 bit math for it.

**Dave Jones:** Right. So it's not really, yeah, it's not, it's not really math, right? It's not matrix operations and all that sort of jazz.

**Andreas Olofsson:** So, so they, they, they did a whole, uh, whole writeup on it and a whole design, uh, which is, you know, open sourced and up on our Git repo. Um, and, uh, but I would say that the majority of people use the arm cause that's the easiest and then they use the epiphany. And then third, some of the people use the FPGA as well.

**Chris Gammell:** You also mentioned, uh, community and stuff. Is it mostly through Git or is there, uh, are there other resources that people can kind of access on the, on the getting started side?

**Andreas Olofsson:** And so we have, we have a forum that's fairly active about 10 posts a day. Um, and, uh, um, people usually start, we encourage people to start out there because we have a good mix of senior people and beginners. Um, and, uh, besides that, you know, they, uh, um, between, uh, everything else, uh, Git and, um, and, you know, Twitter email and so forth. Uh, I think, I think we're, we're doing okay.

**Chris Gammell:** Great. That's great. Where do you, where do you see all this stuff going in the future? I mean, uh, you'd mentioned the, the, um, the academic side of things. I mean, do you see it kind of just kind of cranking on math stuff or where, where, where would be the ultimate, the ultimate new application? Is that quadcopter or are there other things out there that people might be, that might tickle people's brains into using this thing?

**Andreas Olofsson:** So, yeah, so we, we, we worked very hard on the, on the parallel programming side for, um, for last year. Um, and, and actually that, that is the place where most of the work has been done so far from the community. And it makes sense. It's the, um, kind of the plumbing layer and the infrastructure layer. And so we've had people work on tools and, um, uh, and frameworks, things like open MP, MPI, open CL, Erlang, um, Python wrappers. Uh, even a basic for parallel. Um, so that, you know, there's about 12 different pro basic, which is very cool. Um, there, so there's about 12 different programming frameworks that have grown up organically from the community that we had nothing to do with really except support them. Um, but, so that, that part, I would say you can give a, definitely give a great A, um, where, where we now need to, um, put our focus is, uh, two application areas and it's, uh, it's imaging we talked about. So the, the drones and the robotics, um, and there, um, we, we just need to make sure we have the hardware and drivers in place to enable that kind of like what the Raspberry Pi did with the, um, the camera board. Um, and, um, um, and then the second one is, uh, software defined radio.

**Chris Gammell:** Ah, the realm of, of the Ostmans of the world, Mike Ostman and the, and Jared and all them, all the, all the people that like that stuff. Yeah. That's, uh, that's some crazy stuff they do. And it's all, a lot of that's done with the, the low level. It, it seems like they're DVI chips, right? So the, the digital video thing. So they have the big multipliers. It seems like this would only, only accelerate that ability.

**Andreas Olofsson:** Yeah. Yeah. Uh, we have many people who think that the parallel is, is the perfect or a very good SDR platform in terms of the, what it provides. I mean, and it's a combo of, uh, the arm, the zinc, like the FPGA and the epiphany. Uh, so they're coming back to the heterogeneous computing. You need all three to, to make a good platform. Um, not everybody wants to do an SDR in FPGA logic. It's just, it's just hard. I mean, some of, some of these algorithms are tricky and, and you'd rather write them in C code than in Verilog. Cause you can iterate that much faster.

**Chris Gammell:** Yeah. Especially people coming from the DSP, the, the DSP processor world, right. Versus the FPGA side of things where there are tools that can convert that stuff, but that's more like high level math, trying to convert it into, to, um, logic that that's a, that's a different, different beast altogether.

**Andreas Olofsson:** And, and yet at the same time, you definitely need the FPGA for all the connectivity, hooking up to the RFICs, doing some of the front end filtering. Uh, so I, I think it's a, it's a, it's a great fit to have all three working on that, uh, you know, jointly as a good solution.

**Dave Jones:** Um, are you actually working on a, a new, more powerful core or are you going to run with your current, uh, what is it? The epiphany three or have you, no, you've done the four. Yeah.

**Andreas Olofsson:** So we did, we did the four, uh, as a shuttle, uh, at 20 nanometer. So that was the 64 core. Um, unfortunately it would have cost $3 million to get that into production. Um, so you can do a shuttle, uh, shuttle basically low volume production at, uh, at a couple hundred thousand dollars, uh, to go into volume production, you, you have to, you know, put in another three or so. Um, so we, we didn't have that. Um, and when we ran the Kickstarter campaign, we were hopeful that, you know, we put $3 million as a reach goal to get in there, but, uh, we didn't get it. And so we, and we couldn't raise the money on the side to enable that either.

**Dave Jones:** Are you still looking to raise money on the side, venture capital and angels and all that sort of jazz? Have you got any outside investment at the moment?

**Andreas Olofsson:** Oh yeah, no, definitely. We, so we, um, we had, um, when we ran into trouble with the Kickstarter campaign, it was, uh, it was, uh, a Swedish company, a big base station company named Ericsson and, um, and a VC that saved us. So we, we would have, we would have gone, we would have gone bankrupt if it wasn't for them.

**Chris Gammell:** That's stupid. I mean, that's good they were there. Uh, but that, uh, yeah, that's always rough because then it means you kind of give up some control as well. Right.

**Andreas Olofsson:** Yeah. It's, um, you know, it is what it is as I say in Boston. Right. Um, so, uh, I mean, if you, if you need to, if, if, if you need millions of dollars to reach a product and an ecosystem, it's hard to do that. Just bootstrapping. Um, so, uh, uh, so in, in this case, um, with, uh, between the, uh, the parallel production and the chip design and the, um, um, and the, even the Epiphany three production, um, there was just no, I, I didn't see any way around it. Um, so yeah, so that, that's, that's what we've taken into date. And, uh, um, right now, um, you know, the parallel ecosystem is growing nicely. Um, and I think it's really going to take off once we have the, uh, the SDR and the imaging, um, solutions so that people can have everything they need to, to really go after those ones. I mean, one of the things we found is that a board by itself without the daughter cards is still a zero score, right? So it's a, it's an end operation. You need all the things in place to make a successful sale. Um, and, uh, and we started off with a, with a parallel board thinking that there's going to be a daughter card ecosystem, um, or around this, like there has been for the Arduino or the Beagle board or, or the Raspberry Pi, but, um, you definitely need a big, uh, customer base to make that happen. You know, again, I kind of have to follow the money. Absolutely.

**Dave Jones:** I think you are on, I think you are on the winner there by trying to focus on like imaging or SDR or something like that. And, you know, getting a real building a successful product around a core market like that.

**Chris Gammell:** Agree. Yeah. What about like a, a neural processing? I mean, that seems like something that I always see for parallel, like neural networks and stuff like that. And artificial intelligence, is there any, is there anything in the community about that right now? Or is there interest in that in the research sector?

**Andreas Olofsson:** Uh, there is, there is definitely interest from, from many different camps in the research part. Um, but it's research. It's not necessarily going to sell a lot of boards. So, you know, you might sell. Ah, true. Yep. 16 or 20 to one university. Um, or, or they might even put, uh, builder, their own board with a bunch of epiphany chips on it. But, um, it's, it's, yeah, it's until that becomes a usable application by others or a programmable platform by others. It, it's kind of a dead end. Um, so, you know, where, as compared to, let's say an imaging where you say, how many people have bought drones out there and how many people would want those drones to be, um, be able to avoid the telephone poles around in front of them. So they don't have to, you know, buy a new $700 drone. Right.

**Chris Gammell:** It'll be worth the $100 board or whatever.

**Dave Jones:** So do you have any major, uh, competitors coming up with, uh, similar, uh, cores like this that can be used in supercomputer applications? Are you guys still ahead of the curve there?

**Andreas Olofsson:** So in the supercomputer space, it's mostly the big guys. Um, it's Nvidia, it's, uh, Xilinx, Altera, it's Intel, it's ARM. Um, and, uh, you know, those are all formidable opponents. Um, in the, um, and, uh, you know, in terms of startups, um, the, you know, one of the problems we had in raising more money is that there are very few investors investing in chip companies because the returns have been really poor in the last 15 years. Yes. So, you know, everyone who's been burned once is going to think twice before they invest again. And some people have been burned literally hundreds of millions of dollars. I mean, you look at things like CalcSATA or Tabula between those two companies, there's $300 million wasted. Oh, ouch. And, uh, it's, you know, it's not, not any fault of the, of the engineers on those, in those companies. It just happened. But, uh, for the investors, it was their money, right?

**Dave Jones:** I don't envy you at all getting into the semiconductor space.

**Andreas Olofsson:** No, it's, it's all right. I mean, it's, it's what I do. I'm a, I'm a chip guy. I've always been one for me to do anything else.

**Dave Jones:** You'll, you'll pry this chip from my cold dead hands.

**Andreas Olofsson:** That's right.

**Dave Jones:** Oh goodness.

**Chris Gammell:** I love it. Is it, is it, is it tough to, uh, to catch the attention of like the, the, the chip fabs these days? I mean, there is that, is that pretty standard, you know, interfacing with a TSMC or someone similar like that? I mean, is it hard for that kind of stuff? It's, it's not easy.

**Andreas Olofsson:** They would definitely prefer you to, uh, to work through a, an aggregator. You know, there are design firms or design servers that they want you to work through. Um, and a lot of times the problem is that everybody wants their margin. And so when I started going through some of these design firms, the prices they wanted was completely out of my league. And so, especially when I was working on my own, I mean, some of, some of the quotes were, you know, million dollars for a test chip.

**Andreas Olofsson:** Oof.

**Andreas Olofsson:** Dang. And, uh, uh, uh, and, and I was like, well, I, that's great, but I, I can't afford that. So I'll do, I guess I'll do myself. So I, um, I got a, a good deal on EDA tools, um, um, um, kind of special startup deal at, um, that then, you know, once we raised funding became a normal EDA tool. So, but, um, uh, with, with those tools and hard work, we were able to do a chip on less than $200,000, what, what everybody else quoted a million dollars.

**Chris Gammell:** Wow.

**Andreas Olofsson:** So, so it's, and so, and then I worked directly with the foundry, but I also got lucky in that I got into a second kind of a, not TSMC. I couldn't get into TSMC at the time, but I got into a, you know, one rung below that was hungry for business. And, um, and so, and once we, once I was in, I was able to keep moving with that foundry as they buy global foundries and then as they move forward. Um, cause I, it's, yeah, it's, it's not easy, but it's possible. Um, it depends on which vendor and the timing.

**Chris Gammell:** Yeah. Well, that's, that's, uh, it's a crazy experience, but I think it's, you know, it sounds like, it sounds like for these kinds of things, like you mentioned with the, the, the calculations per watt, it's like, that's where it really, that's where it really is needed. That's where the, that's where the rubber hits the road kind of thing.

**Dave Jones:** Right. So are you guys set for the future? You are like, or are you sort of running out of cash? Do you need another investment round? You got another Kickstarter going considering that you love Kickstarter so much? What's, what's the future? What's the next step?

**Andreas Olofsson:** There's definitely no more Kickstarter in the future. Um, we, uh, we've, uh, we've stayed pretty lean, small team. So, uh, we're, we're close to break even, which is a good thing. Uh, and, uh, uh, uh, yeah. Um, and, uh, you know, there, there are some things working right now that are looking pretty good, um, on the commercial side. And, uh, so yeah, all in all things are pretty good. Awesome. Um, it's, uh, you know, I would say that, you know, almost there might be some great things towards the end of this year. I'm cautiously optimistic.

**Dave Jones:** Oh, excellent. Excellent.

**Chris Gammell:** Well, yeah, we'll definitely keep an eye out for that. We're never allowed to ask the really, the really fun questions of what is it? But you know, I'm sure that it's, it's going to be great. Yeah, no. Whatever it will be. We can have you.

**Dave Jones:** Right. But yeah, I would hate to see another startup semiconductor company fail, you know, because they're just like, yeah, it's just a bit depressing to see. So we wish you all the success.

**Andreas Olofsson:** Oh, thank you. Oh, thank you. I, I, uh, it's, um, it's been a wild ride, but, um, we're, we're going to, we're going to stick it out another couple of years at least.

**Chris Gammell:** Yeah. And I highly recommend that people, uh, I was reading some of the, the blog posts you have before, like, this is a great one. The introduction to semiconductor economics. I think that's awesome just to have, uh, you know, a kind of a breakdown on what's actually in the costs based around it. You know, like that's just a lot of people don't ever do that. I mean, my, me and Dave included, we're just, just, we never really experienced that. And it's so easy to think, oh, well I could buy a chip for $3. Why, why do I have to care about the, you know, what, what are, what did it take to get it here? So, um, that, that's really cool to see that stuff, even though it seems to be painful.

**Andreas Olofsson:** Yeah. I, I, I, I mean, I, I think I actually might do a new one on Kickstarter economics. Um, just so that, uh, so that, that people just understand what, what, what goes into running a Kickstarter campaign. Um, yeah, definitely.

**Dave Jones:** That would be very well received. I suspect.

**Chris Gammell:** That's great. Well, Andreas, thank you so much for, uh, for being on the show. We really do appreciate hearing about this stuff. And I think that, you know, a lot of people in our audience are, you know, they're, they're the people that are down in the trenches kind of working on this stuff. I think, I think that this, the parallel could be a really good fit for, for some of the new vision applications, stuff like that.

**Andreas Olofsson:** No, it was really, I, it was a great call.

**Chris Gammell:** I, uh, it was fun.

**Dave Jones:** Excellent. And where can people, uh, follow you, contact you? Are you on Twitter?

**Andreas Olofsson:** Are you hiring? Um, we are not now, uh, unfortunately. Um, but, uh, uh, I mean, if you can, we, the, the one thing that I'm always open to are, are collaborations or partnerships. Um, and, uh, if, uh, we, um, I'm always open to, uh, we, um, I'm always open to uh, to queries, uh, either by email or Twitter. Okay. Excellent.

**Dave Jones:** And we will, um, put a link to the parallel board down below because at 99 bucks, it's pretty much a bargain. You get the zinc processor with the arm and the FPGA and the parallel, uh, boy and the, um, and the, uh, supercomputer chip as well. Fantastic. Yeah. 16 core or beautiful. And you can start developing apps. Yeah.

**Chris Gammell:** Well, thanks again for being on. We really do appreciate it.

**Andreas Olofsson:** Oh, thank you. Thank you, Chris. Thank you, Dave. Okay. Talk to you soon. No worries, Mike. Catch you next time.

**Speaker ?:** Outro Music
