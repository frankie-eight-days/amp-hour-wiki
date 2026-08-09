---
episode: 423
title: Open FPGA Toolchains at 35c3
url: https://theamphour.com/423-open-fpga-toolchains-at-35c3/
---

**Chris Gammell:** Hey guys, happy new year from the Amp Hour. We hope this is your best year ever for electronics. This is a special presentation. This is actually not Dave or I actually recording the Amp Hour. This is our first time ever having a correspondent for the Amp Hour. This is former guest and friend, Pietro Ezrin-Temsky, or Peter, and he is out at Chaos Communication Congress. He was there doing some presentations on his new product, and I asked him to sit down with some of the people doing open source FPGA tool chains because I think it's one of the most exciting things happening in the electronics world right now. So I hope you enjoy this. This is our first correspondent, and hopefully more of this in the future. This is the Amp Hour podcast. Released January 1st, 2019. Episode 423. Open FPGA tool chains at 35c3.

**Pietro Ezrin-Temsky:** Hi, I'm Pietro Ezrin-Temsky as a remote correspondent for Amp Hour. I'm reporting here from 35c3 in Leipzig, Germany. And I'm here with some friends.

**David Shah:** Hi, I'm David Shah. I'm a low-level developer on the open source FPGA tools. I've been working on NextPNR, which is a generic multi-platform place and root tool that's intended to be a replacement for a tool some of you may know, ArachnePNR. Unlike ArachnePNR, it's intended to give much better quality results and also be a platform for future development. Alongside that, I've been working on open source tools for a new FPGA family, the Lattice ECP5, which open up much bigger applications than the ICE40s that we've targeted in the past.

**Clifford Wolf:** And my name is Clifford Wolf of Joses and NextPNR, formerly OpenScut and Symbiotic DA.

**Pietro Ezrin-Temsky:** That's awesome. Nice to have you here. We are making an experiment here for the first time, a remote correspondent for Amp Hour. And I'm happy to do that about FPGAs. You were interviewed by Chris, I think, last year, around that time?

**Clifford Wolf:** Yeah, maybe. Maybe around, I think, in January or something like that, if I remember correctly. I'm not quite sure.

**Pietro Ezrin-Temsky:** Yeah, so what happened since then? What was happening in the FPGA world since you last talked?

**Clifford Wolf:** Yeah, I mean, I guess one of the most interesting developments is that you developed a board. And, of course, also, arguably more interesting is that they did the ECP5. I'm not quite sure. Was this most of this this year or did you actually start last year? I'm confused.

**David Shah:** So, I opened my first ECP5-Bitstream file, I think, in early March this year. But large-scale development on the project didn't really start until early May.

**Pietro Ezrin-Temsky:** So, you also implemented, so you, Dave, implemented also the ICE40 app support for?

**David Shah:** Yeah, so I added the Ultra Plus support. Well, most of the work was done in around autumn 2017. So, I had most of the Ultra Plus functionality working, I think, around this time last year. Because I remember talking to it to people at CCC. Because immediately after CCC, I went to Vienna with Clifford. And we sketched out the plans for the Icebreaker Development Board.

**Pietro Ezrin-Temsky:** That's pretty much a similar timeframe where I visited you in Vienna to start sketching actually the design in January then to create the Icebreaker, right?

**Clifford Wolf:** Yeah, I think so. Literally, Dave was in Vienna. We sketched out the requirements. And then a few days later, you were there. And I was like, here's a list of requirements. Do you want to make that board? And you said yes.

**Pietro Ezrin-Temsky:** Yeah, so that's, what, 11 months later and we have the crowdfunding campaign for this?

**Clifford Wolf:** Oh, yeah.

**Pietro Ezrin-Temsky:** Yeah, so that is going pretty well. It's going still mid-January. It's exciting actually how people were saying or repeating that 2018 will be the year of open source FPGA becoming really, really big. What are your thoughts about that?

**Clifford Wolf:** Yeah, I personally am not a big fan of this year of something. Because we're still waiting, like, for the year of the Linux desktop, for example. And I'm convinced at one point in the future, it will be the norm to have a Linux desktop. And we will all be wondering, okay, so when was the year of the Linux desktop exactly? And I think we have a similar development here that certainly there's more going on in the open source FPGA world now than a year ago. And a year ago, more was going on than the year before. So, yeah, we are at one point at a curve. I don't want to make any predictions of when the peak will be or something like that.

**Pietro Ezrin-Temsky:** Yeah, I like that.

**David Shah:** It is a slow development and there are a lot of myths about open source FPGA tools that still need quashing. And having support for some bigger FPGAs and some fancier features will definitely help dispel those myths. So, once we have the ECP5 support a bit more stable, we can build things that people said very, very, very recently that you could never build with open source FPGA tools. Like PCI Express controllers, DDR3 memory interfaces. Even if you told me a year ago we'd be building them with open source tools, I probably would have laughed. So, things move on and over time they will just become more and more significant.

**Clifford Wolf:** Yeah, I think the whole story of this project is essentially people telling us that we can't do it and then we just do it.

**Pietro Ezrin-Temsky:** Yeah, this is pretty amazing because I think we met four years ago and you released Joses for the first time and this was going on since then.

**Clifford Wolf:** Well, Joses started in 2012 but that was Project iStorm. So, originally you couldn't do much with Joses. I mean, all the functionality was there but you always needed like a commercial backend like a PlaySendRoute tool or a ASIC backend flow. So, yeah, then we wanted to go the FPGA route. For years I tried to convince the vendors that they should just release documentation of how to create bit streams for the devices. And the answer pretty much was always they are not going to do that because even if they would, we would not have the ability to write tools that create those bit streams. So, we first had to document one of those bit streams ourselves. Then we had to write our own first PlaySendRoute tool which was Aachne P&R. And now this year we started our next generation PlaySendRoute tool, next P&R, timing driven, retargetable. So, and hopefully in a couple of years there will be many, many projects based on that for different architectures because people will just use the framework that is there. And if they want to write a proprietary or open source PlaySendRoute tool, it would be ridiculous to start from scratch. You just use the infrastructure that we built.

**Pietro Ezrin-Temsky:** Wasn't there like news very recently that some Chinese manufacturers started using Joses? Is that right?

**Clifford Wolf:** Yeah, I mean, I don't know when they started using that, but someone on Twitter got their hands on their tools. And it turns out that this tool package contains Joses as a synthesis tool. But I think you can't even like download them. You have to like email it and then they send you a download link.

**David Shah:** Someone on Twitter put a link to a Baidu download page where if you know Chinese and you have a Baidu account and a Chinese telephone number, you can download it. And I spent a couple of hours wrangling with that and I did manage to download it in the end. But they don't even have a public link on their website. So I don't know where that even came from.

**Clifford Wolf:** I see. I see.

**Pietro Ezrin-Temsky:** Yeah, I also got taught today that open source tools in even commercial FPGA tools is not, is actually going on for much longer. Because I think you told me that.

**David Shah:** Yes, so ABC, Barclay ABC has been inside both Vivado and Quartus for a long time. And it's very much the industry standard and that is an permissively licensed open source tool.

**Clifford Wolf:** And I mean the place and route engine in Quartus is essentially a fork of VPR from like 20 years ago or something. So in a way, we always had open source components. But yeah. Not a complete flow, basically. Yes.

**Pietro Ezrin-Temsky:** What do you think are the new things besides we have NextPNR? That's one new thing. We have more vendors like another vendor using another part of what we create. What do you think? So besides the ECP5 coming as a next platform, what do you think will happen like next year, for example?

**Clifford Wolf:** Well, I mean, we are going to improve the tools a lot. We have to-do lists on top of to-do lists for everything. So we are not going to get bored. But I think one thing that I would be hoping for to see soon, maybe next year, is support for architectures that the vendor actually wants us to do that and then supplies us with information and maybe even funding to do this kind of work. So I think we are now at the point of that curve. But that would be a natural next step.

**Pietro Ezrin-Temsky:** Okay. So if people want to start getting involved, there are a lot of people that do a lot of software but don't know much about FPGAs. What is your recommendation of getting started, maybe, and learning about FPGAs?

**David Shah:** So, of course, I think we have to mention, first of all, the Icebreaker. It's a really brilliant board to start with. We have run quite a few FPGA workshops. We have looked at what is wrong with a lot of existing development boards and we have fed that into the Icebreaker as a great place to start. And then, to be honest, I think a lot of the tutorials out there don't necessarily teach the best ferrolog. So I think we might have to fix that before we can really, really recommend a particular tutorial.

**Pietro Ezrin-Temsky:** Yes. And also for ECP5, like bigger designs, are there boards or stuff that you should use for that? What is the status of ECP5 support, basically?

**David Shah:** So at the moment, we have quite a significant number of features supported in the ECP5 tools but it is rough around the edges and there are certainly bugs in there. And if you use it, you will find bugs. And that's great. And that's one of the things you can really do to help is run it, find those bugs, report the issues, and we'll try and fix them. In terms of development boards, there are a few projects out there but a lot of them are not particularly available yet. The ULX3S is available in limited quantities. Otherwise, you want to be looking at the official lattice development boards and they have some on DigiKey. There's the ECP5 evaluation board for $100, which is a very good place to start. That's an 85,000 logic element FPGA. So the biggest FPGA with decent open source tool support as it stands.

**Pietro Ezrin-Temsky:** So basically, also using the tools and writing bug reports is what you're mostly looking for besides maybe developers?

**David Shah:** Yes, but that's just a really good place to start. Particularly if you have designs already that you've got. Even if it's quite poor quality code, that's often the best way of finding issues in our tool flow is testing that and seeing what happens.

**Pietro Ezrin-Temsky:** So the next thing I want to ask is we have several other also development boards. There's FOMO, I think, also coming up from Tim Ansel or Mythro, correct?

**Clifford Wolf:** Yes.

**Pietro Ezrin-Temsky:** And there's, well, the Icebreaker, we already talked about that, but then we have ECP5 boards that are coming up. What is the status of the Xilinx stuff? I think you talked with Chris about Xilinx. I think he asked you about that.

**Clifford Wolf:** Oh, I don't really quite remember because it's a year ago. But yeah, we are looking at Xilinx as well. So Yozuz can do synthesis for Xilinx 7 series for a long time, forever, essentially. The only big issue that's left is place and route. So what you already can do is you can use Yozuz as a synthesis frontend and then use Yozuz to write an edif file. And then you can read that edif file in Vivado and use Vivado for place and route. And many people might ask, well, why don't you just use synthesis in Vivado as well? It's not a full open source flow and they might be correct. But if you would like to experiment with that and if you would like to improve stuff, then this is a possible setup. So the thing we are working on now on the Xilinx side is, of course, place and route. And there are different directions that are taken here. There is a group of people that is looking at getting VPR running for the Xilinx devices.

**Pietro Ezrin-Temsky:** What is VPR again?

**Clifford Wolf:** A VPR is versatile place and route, right? Yes. Yes.

**David Shah:** Part of the Verilog to routing project.

**Clifford Wolf:** Yes. So it is an open source place and route too. But it's like 20 years old. It is timing driven. That's a good thing. It is fairly retargetable so that you can change it to target one architect to another. However, the kind of architectures it can target are a little bit artificial and virtual. So they have mock-up equivalents. So they have mock-up equivalents of certain existing real-world parts. But they are not exactly the same parts. So when you do research into placement algorithms, if you do research into routing algorithms, then they might be a close enough approximation that you can evaluate your algorithms. But if you would like to do place and route for an actual device so you can generate a bit stream and then program that device with that bit stream, then you don't need something that's like a close approximation. You need a model of the real thing.

**David Shah:** I think even in the academic world, I think there have been questions in research papers certainly looking at whether those approximations are even really good enough to make good assumptions about QOR, quality of results and the like. Yes.

**Clifford Wolf:** So what we are doing with Next P&R is we try to build another open source framework for doing place and route. But this time targeted real-world devices so that we can actually do all those stuff and generate a bit stream. And in Next P&R, right now, the officially supported, if you will, architectures are IS40 and ECP5. But we also have experimental code that is using a library called Torque to target Xilinx devices. So with this setup, we can already place and route designs for certain Xilinx parts. But still in this flow, the output generated would then be an XDL file, the Xilinx design language. It's an ASC format that Xilinx defined. And then you can use ISE to read this XDL files and generate bit streams. So we still have a piece of Xilinx software in there, but we have shifted enough into our open source world so that we have a platform to test and evaluate algorithms. And in parallel to that, we have efforts trying to build our independent device databases that do not depend on Torque.

**Pietro Ezrin-Temsky:** That's awesome. Who are the people you should contact, like if you want to go help with that and make that better? Or is it already covered? There is enough people working on this?

**Clifford Wolf:** No, there are never enough people working on something like that. So, David, what's the best way to reach out to us?

**David Shah:** So, if you're on IRC, then the IOSIS channel on Freenode is a great place to come and ask questions. And normally, at least one of us is online at any time. You can come there and maybe mention what you're interested in. We'll almost certainly find something for you to do. Or you can take a look at open GitHub issues on IOSIS or Next P&R and see if there's something that you're interested in looking into.

**Pietro Ezrin-Temsky:** So, another thing that I just remembered while we were talking is that the experience I had with using the IOSIS tools already and running into any issues with them. The exciting thing is how fast you actually are patching this stuff. And that is pretty awesome and that helps a lot. It's like I even am doing some consulting work using the IOSIS tools, actually making real designs for a project and a product. So, these tools, from my perspective, are already good enough for a lot of stuff. Not only teaching, not only as an experimental thing, but actually to build products with it.

**Clifford Wolf:** Yeah. I even know of a few companies that build test and measurement equipment and stuff like that, that used ICE40 in some of their products. Specifically because they said we want to use this open source toolchain that fits much better in our workflow. So, I at least know that there are a couple of cases where commercial products ended up with those FPGAs in there because the vendor wanted to use the open source tools and not the vendor tools.

**Pietro Ezrin-Temsky:** Yeah. This is something I hear even from friends that are designing products that are thinking it's like, so which FPGA should I use for this? I need an FPGA. So, several were already switching over. So, I know that the Xilinx stuff will come eventually, but at the moment, its ECP5, for example, is already more along, further along. So, they are switching from some Xilinx 7 series chip and saying, well, actually, the design or the thing that I'm building would work on an ECP5 too. So, I'm switching to a lattice part from Xilinx because the tools are available. As well as another good reason for those tools from what I've heard here, especially at CCC, is the tooling. So, basically, building it into your automated tests or automated generation because equipping the commercial tools or automating them is quite difficult.

**David Shah:** And also, you don't have things in the vendor tools you often have, even if it's a free license, it's still locked to a particular MAC address. So, you can't, for example, build like a Docker image or something that you can just run anywhere without doing things that might even break the license agreement. Or you suddenly get into paid licenses and then that could get very expensive. Not to mention the fact that they're often quite hard to automate. They're often quite GUI-based.

**Clifford Wolf:** Yeah, so, I think make file integration or having something that works easily from a make file is something very important for people that come from the software side of things. And people who, like, have been in hardware for a long time, they don't really use this kind of methods to manage their projects. And I think that there are a lot of people out there who come from the software side, try to get into hardware, but they're frustrated very quickly by how these tools work and how they look because it's so different from the techniques that have evolved in the software world for managing really large projects. And when you look at people at the workshops that we do here, these are people that come from the software side and they are super excited when they can see, oh, this is just the make file. It's just a couple of command line tools that when executed in sequence will get you from Verilog to a Bitstream.

**Pietro Ezrin-Temsky:** Yeah, this is, for example, being able to put a complete build system and an exercise thing on, like, Raspberry Pi is not very fast, but for a small thing it will be okay. So you can basically put it on a small embedded computer and try getting vendor tools run on an arm. Or, for example, the workshop, we are actually making people install the tool chain on all the laptops. I have seen only like two people of the 30, no, 80 people that we had on the workshop that had actually Windows machines only. Everyone was actually Linux or a Mac. And there is the interesting part. On Mac, you need a virtual machine to run the vendor tools because you need a Windows or Linux machine at best. And running the tools on Mac is completely impossible directly. And so we had several people with Macs and they were able to compile the tools on there and run them, which is very exciting for those that are using that platform.

**Clifford Wolf:** Imagine every one of those 80 people had to download a 21 gigabyte tab or fast to get started.

**Pietro Ezrin-Temsky:** And it's on a conference where you don't really expect to have a good internet. Well, it's 35C3 or the CCC organizing it. They figured out how to get the internet working pretty well. But downloading such a huge installer, you would really not like that as well. You would have to provide a USB stick or something to install this stuff. We definitely learned some dependency stuff. And you learn from this kind of workshops where you have a lot of people try to install the software. But overall, I think the trouble they had was like, oh, I didn't install one package, one dependency. It was much less painful than I actually expected.

**David Shah:** I mean, to put things in perspective, Xilinx Vivado on modern Linux distributions for many years were just segmentation fault when you run synthesis. And it's a closed source tool. It's segmentation faulting. Effectively, there's nothing you can do. Whereas with the open source tools, there's a community that will actually support individual users. And you can even go in there and look at it yourself if you want to.

**Pietro Ezrin-Temsky:** Yeah, that's apropos that. That's very exciting because I gave Silverman now, the TNT, one of my icebreaker boards. And he wanted to implement video on a LED panel, like a huge LED panel. And to do that, he wanted to stream video over USB, over SPI to the FPGA at 30 megahertz. And there were some issues. Maybe Dave, you remember what the patches were. But he basically went and wrote the patches for himself to do that and implemented the 30 megahertz SPI. And he could develop that. And only a few days later, it was merged upstream, which is awesome. So what was that?

**David Shah:** He just needed some finer grained control over the synthesis tool as to how exactly it merged parts of logic together, basically. So I think there was one other bug to do with a really weird edge case that, again, when he was manually placing a load of parts of the FPGA, happened to come up.

**Pietro Ezrin-Temsky:** Yeah, this is where really the open source stuff shines. When you run into issues and you can really address them, either yourself or get the help. You had experiences with writing bug reports for Xilinx and Quartus, I think, because you had some tests running for the Verilog or something?

**Clifford Wolf:** Yeah, I don't want to get too much into traditional vendor bashing. Yeah, sorry, sorry. But yeah, so I wrote a thing called Vloghammer, which is a tool that will generate random Verilog designs and then run it through my tool and through tools from different vendors and then compare the recites. So for synthesis tools, it would do a formal equivalence check afterwards. It would also do random input simulation using some of the simulators. And my aim was that I wanted to find the bugs in my synthesis tool. And indeed, I found and later fixed a lot of bugs in my synthesis tool with that. But as a side benefit, I also found a lot of bugs in the traditional vendors tools. And it was very interesting to see that in some cases, those bugs still remain in there like four years or something like that later.

**Pietro Ezrin-Temsky:** I think for them, some of those bugs is like the reason to keep them in is that they are documented and there are workarounds for them. And if they fix them, some designs will break. Is that what the reason is?

**David Shah:** That sounds a bit like the Microsoft Excel story, to be honest.

**Clifford Wolf:** No, but I really don't think that it's that. Because some of those bugs, in my opinion, are really bad bugs where the tool generates just wrong synthesis results. And I can't really imagine a case where someone would use it in a way so that accidentally it does the right thing. And in part, this is because Xilinx, they have like three different tools. They have ISE, they have Vivado, and so Vivado synthesis. And then they have Exim, which is like Vivado simulation. And Exim is just a newer version of iSIM, which was the old simulation tool. And usually, the bug would only affect one of those three tools. And the other two would do the right thing. So, I think in a case where two tools from the same vendor already disagree on the behavior, there is not really much room for making an argument that, in fact, this is the way it should behave.

**Pietro Ezrin-Temsky:** Yeah. There was a talk at 35C3 by Tim, who wasn't able to join us here for this session. But he was talking about SymbiFlow. Maybe you can talk a little bit about that. So, basically, it's a higher level tool that is basically combining more things together.

**Clifford Wolf:** I really feel uncomfortable talking about like... Tim stuff. Tim stuff. But SymbiFlow is more like an umbrella for different projects. So, for example, we're looking at creating open source FPGA tools that will reach larger, better devices, will make it easier for users to use it. And in some cases, there is overlap. So, they use Yozis and we use Yozis. And in some cases, there are different approaches. So, for example, they try to use VPR and make VPR back on Sylinx. And we wrote our next P&R tool. And I think this is a very good thing. Because if we want to really get next P&R to the point that we wanted, we need something else that we can benchmark against. And nothing is better here than a little bit of competition between two open source projects. So, at least from my side, this competition is very welcome.

**Pietro Ezrin-Temsky:** Yeah, of course. And I hope that there will be more open source tools on different layers of the whole stack that will come out. And I think one thing that I'm quite excited about is the fact that there are quite a lot of RISC-V soft cores coming out. There was a competition this year that had quite a good attendance, creating different, even crazy cores that are like processing one bit at a time.

**Clifford Wolf:** Yeah, RISC-V is really getting off the ground now. So, there was the RISC-V summit just a few weeks ago in the Bay Area. And it had over 1,000 attendees, more than 80 speakers, I think. Maybe I'm mixing up now. Maybe more than 80 companies that were on the exhibition floor and I forget the number of speakers. Something like that. A lot of people, a lot of companies, a lot of speakers, a lot of talks. So, this is now a real big thing. And many companies are building their own cores. Some of them are open source, some of them are not. So, I'm also very excited about that. So, Western Digital, for example, announced the core at the RISC-V summit. And this is going to be an open source core. And they promised to release it soonish. So, we will see.

**Pietro Ezrin-Temsky:** I think they also said that they are committing to shipping some ridiculous number of cores.

**Clifford Wolf:** I think 2 billion per year, something like that.

**Pietro Ezrin-Temsky:** Yeah, that's a pretty large number.

**Clifford Wolf:** Well, it's essentially the number of cores that they already ship each year. But not all of them. Well, they are not RISC-V cores now. But they will be all RISC-V cores in the future. Again, speaking like for other people and repeating the things that I have learned at the conference. But one of the ideas here seems to be that they actually want to open up the processors that you find on a storage device. So that the user can actually run their own code on that. And that might not be so interesting for like home users or workstations. But in a data center scenario, there are a lot of things that you could do apparently with that. And this is not something that they can do with like different proprietary ISAs that they might change from one batch of hard disk with the same model name maybe to the next one. So, they need to standardize on something so that they can then build a platform that users can write code for. And RISC-V seems to be the obvious choice in the current environment, I guess.

**Pietro Ezrin-Temsky:** There used to be an argument from a lot of vendors that opening up this kind of chips inside is a security issue. As we know from anyone you talk to in the security community, security by obscurity never works. So, opening up those cores might also lead to an improvement in security maybe even.

**Clifford Wolf:** Yeah. So, I'm sure that security is a big topic in this context. Because of course, that was my first thought. Well, if I can upload code to my hard disk, can someone else upload code to my hard disk?

**David Shah:** To be honest, uploading code to an existing hard disk sounds like a classic CCC talk.

**Clifford Wolf:** Yeah.

**David Shah:** I don't know. I remember a few years ago, Bunny did a talk about uploading code to SD cards, for example. Yeah.

**Clifford Wolf:** So, I think one of the biggest...

**David Shah:** If you can upload code to it, then people will.

**Clifford Wolf:** So, I think one of the biggest arguments here is exactly that. That maybe you can already do it with all the devices out there. The only difference is now it's not really a platform. You can't do it in a portable way. Okay. So, all they are going to do is make it so that if there is a serious issue, it now affects all the hard disks. Well, that didn't sound that great. But you know what I mean.

**David Shah:** For example, Bunny found those SD cards were using like an 8051 with 32-bit extensions. And clearly, that's not something you want to be providing to large numbers of end users. Whereas RISC-V is a much, much better target and has very, very rapidly improving compiler support in GCC and Clang and LLVM.

**Clifford Wolf:** So, you mentioned the soft core competition. And I have to admit, when I first heard about that, I was not sure how this is going to work out. But I think in the end, it was very successful. I'm very impressed by all the costs that were entered to the competition. And some of them are ridiculously small and some other weird design corner. But I think overall, the competition has shown how small you can make a 32-bit RISC processor. And I think that's very exciting for the FPGA work that we are doing. Because the Icebreaker board, for example, has a fairly small FPGA, about 5,000 logic elements. But nevertheless, if you want to build a 32-bit processor for it, it maybe takes up half of the space. And you still have half of the space left for your custom peripherals and other stuff you want to have there.

**Pietro Ezrin-Temsky:** Yeah, this is pretty impressive. And I really like that. Because there's another... So, FOMO, the FPGA from Tim, for example, is exactly meant for experimenting with soft cores. So, you can... It has also the Ice40 Up5K, the same one as on the Icebreaker. And probably on several other boards. But you basically plug it into your USB port and you can experiment with different soft cores. I think the people that took the competition, they were getting some evaluation boards. I'm not sure if FOMO was part of that. I don't think so. I don't know.

**David Shah:** I think it was some micro-semi boards and the Lattice Ice40 mobile development kit, something like that.

**Pietro Ezrin-Temsky:** Yeah, right, right. And, yeah, anyways, at the end, I was very excited to see that happen.

**David Shah:** I think another exciting thing with RISC-V that's happening at the moment is improvements in terms of RISC-V for Linux and RISC-V for Linux on FPGAs. And that ties in really nicely with the work I'm doing on the open source tools for the ECP-5. Because the ECP-5 is at a great size for Linux-based SOCs. So, I've already built a demo using the fully open source flow of an open RISC-based SOC running on the ECP-5, booting into a simple Linux system, using BusyBox shell to blink some LEDs just to prove that it's working. And it would be really nice to move that demo to a RISC-V processor to maybe VEXR-V.

**Clifford Wolf:** Yeah, so this is definitely something that we are going to work on in the next year. So, we are probably not going to build our own design. Instead, we've been reaching out to a couple of different groups who build RISC-V-based Linux SOCs. And we are trying to pick one and build a demonstrator using that. Yeah, that's very exciting to see. One thing that I'd really like to underline is just what we have now, not including the improvements we are going to make in the next year. With the ICE40 and the ECP-5, it covers a really huge dynamic range. So, I think maybe people have grown a little bit numb because of the number of logic elements and stuff like that you have on the largest of the largest FPGAs. But when you look at the things that you can do in the 85-kilo logic elements ECP-5, 20 years ago, they have been ASICs with far less functionality in there than the thing that we can build now with that FPGA.

**David Shah:** So, I mean, to put some numbers to it, in a 16,000 logic element, quite an old Altera FPGA, I was doing real-time augmented reality, rendering like a Minecraft-style grid over a camera feed at 135 frames per second. And that was fitting comfortably in that. So, you could certainly push the resolution higher, push the features higher on an ECP-5. You could even be running multi-call and access OCs on the 85-k ECP-5 easily.

**Clifford Wolf:** Or just have six instances of that. Yep.

**Pietro Ezrin-Temsky:** You also told me that this was like low latency stuff because we were talking with someone regarding modifying a desktop camera-based microscope because a big problem with those is the latency of the video that you get out of those. Because if you move your soldering iron, if you want to work on this, it's like you move your soldering iron and you see a latency of, I don't know, 500 milliseconds before you see that your soldering iron is actually reaching this spot. And FPGAs might help with that.

**David Shah:** My particular interest of mine, in fact, is looking at doing video processing without frame buffers on FPGAs, so purely using line buffers. And that way you really get the latency down because you have pixels coming in, pixels going out, and it's rare to see a latency above a couple of microseconds. I wrote a custom high-level synthesis tool for that project a couple of years ago. And it was a real mess. It was just a quick hack to get that project working that took a C-like language. Unfortunately, it was to VHDL, not Verilog, because that's what I was using at the time. But next year, I'd really like to find just a couple of weeks to get that into a state where I can publish a useful tool just to get a few more demos building along those lines of doing low-latency video processing. Because it's somewhere where FPGAs can really shine, even compared to GPUs where you tend to have a certain minimum latency.

**Pietro Ezrin-Temsky:** Yeah, so that leads me to another question. Because the question we get quite a lot building FPGAs is, so what are the applications that I can't do on a microcontroller that I would even want to use an FPGA? So besides high-speed video processing, wide data bus access, do you have other examples for interesting things?

**Clifford Wolf:** There are many obvious examples like that, where of course you would like to use an FPGA, but usually they're fairly complex. Like you could do cryptocurrency stuff. You can do software-defined radio, all kinds of fun things. But none of that is something that you would like to get started with, right? It's like that's the kind of stuff that you do after you made your Hello World projects, after you learned how to use the languages. The thing that I really like for learning FPGA stuff and for this simple project is anything that has an LED matrix. Because driving LED matrices is something that becomes pretty hairy when you use a microcontroller fairly quickly. Because usually you have a whole bunch of pins that you would like to drive in parallel. You have to bit bank a more or less involved protocol. And it must be pretty quickly. And interestingly, the same thing is very, very easy with an FPGA. Because the FPGA doesn't care if you want to do a couple of things in parallel. You can just have parallel units that do all those things at the same time in parallel as you would want to have it. So I think those kind of projects are things where FPGAs can really, really shine without being like PhD-level projects where you can easily spend a year or two just getting your head around the basics of the field that your project is sitting in.

**Pietro Ezrin-Temsky:** Someone came to me today and was also saying, besides LED matrices, as in those video wall tiles, they wanted to drive the WS2812s or APA121, I think they're called, these intelligent LEDs. You can drive quite a lot of them with a microcontroller. But he was saying, oh, I can drive a huge amount of them and actually involve them in sculptures, in actual art installations that really have to drive a huge amount of them very easily with an FPGA. And especially for people that are not comfortable with the state of the art FPGA development and making it easy and having higher level languages like MyGAN, for example, which are Python-based and you can just create your design in MyGAN. It is much more approachable for someone who is not basically already an FPGA developer.

**Clifford Wolf:** So especially with the soft course, there's a completely new field now where you just take an existing system on a chip. You don't need to write your own processor. You don't need to write your own memory interface. All you do is you add one custom peripheral. And essentially, instead of looking for a microcontroller that has just the right number of UARTs and just the few interfaces that you would like to interface directly with, instead you just build one or two missing peripherals yourself and you pack it all together. And now you have a microcontroller that just happens to have exactly the kind of peripherals you want. And instead of writing extremely complex firmware that tries to use DMA controllers and other tricks to speed up bit banging, you end up with something that is a very, very simple firmware because it happens to have the exactly right peripheral for the job.

**Pietro Ezrin-Temsky:** I think I saw very recently a video on YouTube of someone adding a WS2812 peripheral driver to a RISC-V running on an FPGA. Do you remember?

**David Shah:** Yes, that was Matt Venn. He was adding it to the Pico RV32 RISC-V processor, which is Clifford's processor, on the ICE 40 FPGA using the open source ICE 40 tools.

**Pietro Ezrin-Temsky:** Yeah, Matt, that's correct.

**Clifford Wolf:** And I think it was a pretty great video because it really demonstrated this point very well.

**Pietro Ezrin-Temsky:** Yeah, and I think I also, in the project that I'm doing as a consulting job, I have also a way where I have a central controller that has to output, I think, 32 UARTs out of the core unit. And try finding a microcontroller that has 32 UARTs in it. I think they might exist, but it is so much easier to just have an FPGA and drive the data into it and then split it out into so many UARTs to drive whatever you want, like a splitter, basically. Yes. All right. So any last thoughts? We are getting here to basically the end of this talk. And so what do you think? What should we leave the listeners with?

**David Shah:** I think keeping an eye out for what happens next year, I really hope we'll have some exciting stuff happening, both on the tools side, on the board side. There are some ECP5 development boards coming out next year that should really complement the development in open source tools. There's the ULX3S. There's the Tiny FPGA EX, which has a USB Type-C connector. And it's connected to the high-speed transceivers on the ECP5 FPGA, which I just added support to in the open source tools a few weeks ago. That will get you a USB 3.0 interface, 5 gigabits per second. And there's also the Philpnology MyStorm Black Edge board, which is going to have HDMI in and out, MIPI CSI camera interface. So that's going to be a great board for video processing projects like the low-latency stuff I talked about previously.

**Clifford Wolf:** Yeah. And I think with all those new boards that are targeted specifically at the open source tool chains and that are accompanied with things like tutorials, the documentation that tells you what kinds of tools do you need to install. I think there's really no excuse now for not having tried the open source tools yet.

**Pietro Ezrin-Temsky:** Awesome. That was great. Thank you very much for joining me in this experimental first remote correspondent podcast. And I see you hopefully soon, and I will give it back to Chris at Ampower.

**Chris Gammell:** Thanks.

**Clifford Wolf:** Thanks for having us.

**Chris Gammell:** All right. Thanks, guys. That was, I mean, that was fantastic. Obviously, I'm sitting here in Chicago as Peter was over there in Germany, and there's tons of other people over the Chaos Communication Congress. We've been posting some talks to the subreddit, and so you can check out more there. Sorry, Clifford gave a talk, and Tim gave a talk, and there's a bunch of other stuff as well. Since this is the Amp Hour, I will now talk for another 15 minutes about the things I don't know about FPGA tool chains. Not really. Sorry. But what I would say is that Peter does have a crowdfunding campaign going on right now that is the Icebreaker FPGA. I'm supporting it. You can go and see. There's just some fantastic demos from Micah and TNT and just basically LED breakouts just showing what you can do with an FPGA. It's a really great example there. So I do recommend you support it. I think that that supports also the EOSYS project and NextPNR like we just heard about. If you want to learn more about our speakers, obviously, you can go check out the show notes, but you can follow them on Twitter as well. You know, in an increasingly chaotic world, Twitter actually for the tech world can be kind of nice. As long as you filter it down, that's the key thing. So if you're not on Twitter currently, I do recommend you filter your feed very specifically. I use something called TweetDeck, which is part of Twitter. That helps me to just narrow it down to the people that I like. So you can follow FPGA underscore Dave. That's Dave who is on here. Clifford is OE1CXW. And Peter is Esden, E-S-D-E-N on Twitter. You can follow me, Chris underscore Gamble. And Dave, my wonderful co-host who is now on vacation, EEVblog on Twitter. And you can follow the Amp Hour or the Amp Hour subreddit. That's a great place to get your news. Thanks again for all of your listening in 2018. We're really looking forward to 2019. I already have a bunch of great guests scheduled. And thank you very much to all of our patrons. We really appreciate your support. That paid for specifically to get all those microphones to Peter last minute and to get him doing this show out in Germany. So thanks again. And we'll see you more in 2019.

**Speaker ?:** We'll see you in the next episode of YouTube. Bye. !
