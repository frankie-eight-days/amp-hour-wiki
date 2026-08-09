---
episode: 501
title: Discussing the Open Source PDK with Tim Ansell
url: https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/
---

**Tim Ans:** This is The Amp Hour Podcast, released July 19th, 2020. Episode 501, discussing the open source PDK with Tim Ansell. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics. Hi, I'm Tim Ansell from Google. Hey, Tim. Welcome back. This is your third appearance on The Amp Hour. I believe so. Yeah. So the first time we talked just kind of about you and your projects and the Tomu and the USB to HDMI and some of the other projects you've been working on. Last time we talked, it was at Chaos Camp in 2019, and that was when Sean Cross was also there, or Zobs. And that was about the FOMU and you guys working on that together. And now we're talking about something that's exciting. We mentioned last week on the show, and we've been seeing headlines about it. There is big news that is Google, who's your employer, and Skywater, not Skywalker, is doing an open source PDK. So what's up with that?

**Sean:** There's actually kind of a really interesting connection to the other kind of reasons I've been on The Amp Hour here. If you kind of look at it, the first time I was here, I was talking about taking a microcontroller and making a device out of that. And then the second time I was on here, we were talking about doing an FPGA-based system, which had a microcontroller running inside it. And now I've gone even another step lower and started looking at how do we create a ESIC or a FPGA from transistor level stuff.

**Tim Ans:** So your fourth time on, you're going to be talking about how to create atoms from scratch and building up from the basic building blocks of the universe. Because at some points it's got to stop, right? I mean...

**Sean:** Yeah, I think I'm probably at the bottom. The people behind a group called Libra Silicon want to go even a step further and release all the information on how to actually do the manufacturing. I don't know how you pronounce his last name, but Sam Zelouf?

**Tim Ans:** Yeah, Sam Zelouf. Yep. Yeah.

**Sean:** Yeah, he was a high school student doing transist manufacturing in his garage, right?

**Tim Ans:** Yep. Past guest of The Amp Hour. Yep. Yep.

**Sean:** Ah, he, you know, has gone much lower than I have. I have no plans to go anywhere near that stuff. Okay. Okay. I'm quite happy with stuff that I can do on my computer.

**Tim Ans:** Right, right. That software-based development of hardware.

**Sean:** Yes. And that's kind of why I like collaborating with Sean and Bunny and those guys. It's because it lets me take all that physical stuff and stop worrying about it and have them take care of all the soldering. I can solder, but I don't find it particularly fun.

**Tim Ans:** Right. So when it comes to bits or atoms, you choose the bits and let someone else take care of the atoms.

**Sean:** Yes. And actually, I think me and Bunny gave a talk at one of the chaos congresses actually about this idea that I'm very much a software developer at heart and Bunny is a hardware developer at heart. Mm-hmm.

**Tim Ans:** So I think it's like software and revision control and fast iteration and stuff like that. But what would be the analogy for thinking about software like hardware?

**Sean:** So Bunny is probably a better person to explain this being a hardware person. But I think it's more about thinking about things like your device is likely to have a longer lifetime as a piece of hardware than, you know, software is obsolete probably by the time you release it. Whereas hardware is a lot of things like that. Whereas hardware has, you know, hardware has a real physical lifetime. And you need to be able to have ways of dealing with the fact that your device isn't going to be 100% reproducible in a way that software is. And so how do you apply a lot of the quality engineering and a lot of the thinking that hardware people take around statistics and quality engineering to software, which is generally a much easier process where you don't have so much random errors caused by things like canicle fatigue and things like that.

**Tim Ans:** I got it.

**Tim Ans:** Okay. Yeah, we'll try and find that talk and link it in. That'd be great. That seems like a great, great topic. Yep. So on the, so the news itself though, is that there's an open source PDK now. What, what does that actually mean? So someone's listening to it. They're like, okay, I like open source. That first half sounds good. But what is, what is a PDK and how does it actually impact people that might be listening to this?

**Sean:** So I'm only new to the kind of IC design world. And when coming into IC design, what I discovered is that there's kind of three main components to building an IC. The first thing was the stuff I was most familiar with from the FPGA world, which was the actual design. This is kind of, if you're in the software world, you can kind of think of as the code. It's the RTL, the stuff you write in kind of Verilog or VHDL or my case, MeGen and the Python based stuff. So there's that, the kind of design of what you want the thing to do. Then there's the tools, which in the software world would be considered things like the compiler or the interpreter that take your design and convert it into something that can be executed on whatever system you're running on. And in the software world and FPGA world, that's kind of where you stop. But it turns out in the IC world, there's an actual third part you need, which is how does the physics and the devices actually work? Because ultimately you have to convert this into something that's manufacturable. People listening to your show is probably fairly familiar with a lot of things around PCB design. There's a lot of parallels with that around how does your PCB board perform? Yeah. And how is it kind of made? What is like the layers? What are the connections? What is the metal? What are the minimum distances between metal? It's like another really important thing. And in the ASIC design world, this is called the PDK, the Process Design Kit. And this contains all that information in machine readable form. Unlike PCB design, where you can mostly for most of the time not worry about the fact that your traces are actually, you know, capacitive plates.

**Tim Ans:** Well, yeah, I mean, no, that's not really true, though. But I think that as it becomes more important, right? So as you go up in speed, you're starting to do RF or high-speed digital or something like that, you definitely, you can't just send it to just any old fab, you know, to board, fab house, rather, for the PCB. You need to know the stack up and you need to know the material capabilities and things like that. And that sounds like that actually is the parallel to the PDK. It's not like published in a machine readable format, but it is a, you know, you might care that it's, you know, if it's an RF thing, you might be like, oh, it needs to be Rogers type material. And I need to have this thickness of the stack up. And then you specify that. It seems like in this case, the fab is instead pushing it back to you and saying, okay, here's what you get. Now, here's what the physical properties are because of that. You get the thicknesses like you're talking about and the oxides and the metallization and all that.

**Sean:** Yep. And so this is kind of where as a, both a digital person who likes to ignore all the analog problems and a software person who likes to ignore physics full stop, I'm quite out of my depth.

**Tim Ans:** I bet you love doing physics based Python things though, right? You probably love writing Python to solve physics problems.

**Sean:** I like using Python to hide the fact there's physics problems involved. Abstraction. Software is all about abstraction. And so if I can get the physicists to write all the physics stuff so that I can just call a function and get an answer back. Right. That's what I kind of like.

**Tim Ans:** You need like a MyGen that can just go generate a universe, right? That's what you really need. Yep.

**Sean:** And it's kind of interesting to see at KyCon. I forget his name was presenting that kind of Python based schematic capture stuff.

**Tim Ans:** Oh, that was past guest of the show, Dave Vandenbout. Yeah, that's the, I forget what he called it though. Damn. I'll post the link to the talk. Skittle, I think. Oh, that's right. Skittle.

**Sean:** That's the ideal.

**Tim Ans:** That's right. Yep. Yep.

**Sean:** So a lot of these type of things are strongly parallel with the type of things that need to be done in IC design. But unlike PCB design, if you're doing something that's, you know, running at a couple of megahertz, you can kind of ignore all these problems, right?

**Tim Ans:** Hand-waving. Hand-waving is the name of the game.

**Sean:** And you have so much margin in most of the cases that it's not a problem. In the ASIC world, pretty much you have to worry about them all the time, which is also why it's really important to have machine readable versions of all this information because you can't get away with ignoring them. And so you need to be able to do things like accurate SPICE simulations of the transistors and accurate modeling of capacitance and stuff like this if you want your circuit to actually work. That's right. And so you need the things like the capacitance in a machine readable format. And this is kind of what the PDK provides is it frequently provides a lot of documentation, but it also provides things like SPICE models of how the transistor works. And it applies SPICE models of the capacitance of the various layers and the coupling between the various layers and all this type of stuff. And again, you probably understand this a lot better than I do just from having done SPICE simulations more regularly than I have.

**Tim Ans:** Yeah. I mean, I guess I get it at the SPICE level and people that have listened to the show before. We've had people like Michael Englehart on the show who was for a long time the guy running and creating LT SPICE. And that's a nutty episode to listen to just to hear what's running under the hood to make all that. Talk about someone who's making the physics engine for all of us users. It's crazy. But it's always been kind of like the gap for me is like, okay, I get that every transistor has capacitance. And if you look at a SPICE model of a transistor, there's all these different thresholds you can set. And they're built into SPICE specifically, but I just never really understood what I would go and set for those various values. There's constants that are built into the SPICE model that I just don't know how to tweak them effectively. So it sounds like some of what's being handed to you through the PDK is those coefficients and the constants that are going into the SPICE model.

**Sean:** That's kind of my understanding. But again, this is not an area that I'm an expert on. I'm hoping that by having a lot more of this stuff open, traditionally, all this stuff has been the way you get access to it is you have to sign an NDA with the foundry that says, thou shall not share information about how this works.

**Tim Ans:** And why is that? Why is it because of process secrets? They don't want you to go and be able to shop your stuff around? Is that really what the thought is there?

**Sean:** I don't necessarily understand why they want this. I come from a very open source background where if this stuff was shared, it would be a lot more usable. And so they would have a lot more people using their manufacturing process.

**Tim Ans:** Right. You become the de facto standard because it's available to every college kid that also ends up growing up to become the chip designer. And then, you know, like, yeah, if you need some special thing, maybe you have to go and sign the NDA with someone, TSMC or someone. But yeah, if it's just the default, then why not just start from there then?

**Sean:** And it's kind of interesting, like, in the software world, copying software is free, right? But to set up a foundry is, you know, a very capital intensive process.

**Tim Ans:** Right.

**Sean:** Even if all the information is 100% out there, it's still quite a expensive process to replicate it, right?

**Tim Ans:** Yeah. You're not going to reverse engineer, like, every machine that is running. And so as someone who used to work in a fab, too, right, you might, I'm taking some liberties here and making some assumptions. But even if you have the stack up and you're saying, okay, well, you know, on layer four, when we're doing, you know, the etch layer for the gate or something like that, and you're saying, oh, we're, you know, we're etching it to a tolerance of 10% on a 120 nanometer spacing or something like that. That doesn't mean crap for the actual recipe that's going into that machine that's doing the etch, right? That's what I used to run was the machines that did the etch. You can't go, I mean, you could go and maybe tell that to a vendor and say, I need to have 10% tolerance here. But like, there's so much magic in the process specificity and like the replicability, if that's a word, replicability over time to like, that is decoupled from this high level information. So yeah, it seems like it might just be cultural that it's, you know, everything's locked down in the semiconductor industry, it feels like.

**Sean:** Yeah, and I think there's a parallel universe where, like back in the 1980s, it's my understanding that a lot of this stuff was very open and shared wildly, because people were just still trying to make anything work. And then somewhere along the lines, the semiconductor industry took this kind of right turn into, well, if I made it work, I can capture the entire business space. And hence, I don't want anybody else to know how it works.

**Tim Ans:** Yeah. I mean, it may have been tied into venture stuff too, like, you know, so capital intensive, like you're saying. And so if you have money behind it, I can imagine, you know, VCs, even still today, they don't want you to be open source, they want you to have defendable patents and all this other stuff. So that could just as easily been part of it. You know, if you are taking money from someone, they're gonna be like, no, no, no, I want to own this. And that requires you to close down, not be open source.

**Sean:** Yep. And so I'm getting on these days, I was around when, you know, Linux was starting to become successful. And like back in the 1990s, if you had told me that in 2019, Microsoft would be one of the biggest proponents of open source and own, you know, the company where like a huge percentage of open source is hosted. I would say that's like, I would put money against that.

**Tim Ans:** I just saw an article the other day, too, that they're getting into Android now, too. It's like, what is happening here?

**Sean:** We've just kind of seen that open source has kind of won in the software world. And a lot of the arguments that people were having in the 1990s about how open source, like if this stuff was open source, would destroy the software industry and make us all low paid people. None of that happened. And a thing that I was involved with is you might have seen recently that QuickLogic have the first FPGA vendor to start officially supporting open source tools for their FPGA. Oh, I didn't see that. The data is from 2016. There were 700k software engineers in the US. And that number was growing by 30%. If you compare that to the number of hardware people, then there were 50k hardware engineers growing at 7%.

**Tim Ans:** Wow. We got to do better, man. We got to get more hardware people.

**Sean:** And so when you look at that, it's kind of like, why am I focusing so hard on a market that is significantly smaller than this other potential market? Like if I only get 10% of the software people, I've still probably got a significantly bigger market than if I capture 100% of the hardware people, right? Which you won't.

**Sean:** Capturing 100% of the hardware market is impossible, right?

**Tim Ans:** Where were those numbers from? The 700k and 50k? I'd be curious about that.

**Sean:** So the CEO of QuickLogic did a blog post about why he decided that the open source story here makes sense and why he wants to be a leader in that space. So if you go to the QuickLogic site, there's actually a link to a blog post from him, a guy called Brian Faith. I actually recommend you see if you can get him onto The Amp Hour. I think it'd be quite interesting to chat to him, especially around this idea that, you know, he was in the category of thinking, well, if we open this up, it's going to be a negative impact to our company and having his thinking evolve towards actually, no, this is a huge opportunity that we're totally ignoring.

**Tim Ans:** Yeah.

**Sean:** And that's actually very connected to what I'm seeing in the Foundry and the ASIC space is that if we look at things like RISC-V, we're seeing this massive explosion of people trying things in this space, thanks to having a ISA, an instruction set architecture that doesn't require you to license it. It doesn't require you to ask for permission to do things.

**Tim Ans:** That's right. There's no centralized body. Well, I guess there is a centralized body, but it's, that's just on the standard. It's not like you don't have to say, you know, mother, may I? It's, it's instead it's, here's what I did. And it conforms to the standard that the standard body set.

**Sean:** Yep. And this is kind of the secret power of open source is that it means engineers can, don't have to spend time talking to lawyers. I think lawyers are a totally underappreciated profession personally. And the software people don't appreciate how hard it is to be a lawyer.

**Tim Ans:** Oh yeah. Yeah.

**Sean:** And so.

**Tim Ans:** And the jokes are just so good. They just kind of write themselves. So there's that. Somewhat. Yeah.

**Sean:** But the thing about open source, right, is it's effectively standardized a whole bunch of what were previously very hard legal equations, right? Every piece of proprietary software has its unique own set of conditions. Whereas every piece of open source software that uses an Apache 2 license has identical conditions. So the lawyer only has to review Apache 2 once, and then you can use every piece of Apache 2 license on the license stuff on the planet. And if you've got really good lawyers, what they'll do is they'll see that, you know, there's a lot of commonality between different open source licenses. And we'll start looking to things like, I forgot the OSI, the people who own open source.org. They have, you know, a clear set of guidelines of what it means to be an open source license. And through that, it gets the lawyers very comfortable with being able to review open source licenses very quickly and to have a lot of confidence that actually, you know what, if my engineers are using code from under these licenses, I don't need to worry. And that's actually like lawyers have a lot of stuff to worry about. And it takes a lot of time to deal with that, right? It takes real time and real, you know, human effort to comb through a license and check there isn't a clause in there that says, you know, the person who you're buying the software from now owns your firstborn child or things like that, right?

**Tim Ans:** Right. Yeah. And it is interesting to watch a lawyer coma contract too, because like they'll usually call out things that are like questionable and then they'll review it. And like, and really the, you know, and you look at like law school too, and like how that, like the skills that are learned there. And it is a lot of that, paying attention to the small details and understanding these structures. And it is kind of interesting how you said it's like a program. You said, or so it says it's an equation. You said it's open source standardized, there's the legal equation. It is like this, the set of rules or equations that are like, that they, they are kind of comparing against their mental models. And that's what a good lawyer does.

**Sean:** Yep. And like the thing that software people don't understand quite a lot is that this model is continually evolving as various court cases happen. And the interesting thing is that more and more stuff that happens around a certain, area, the more and more confidence a lawyer has that their interpretation of what these words mean is the right interpretation. And so actually having a really large body of stuff around a single license means that there's a lot more opportunity to test what does these words actually mean? Engineers kind of think words have a concrete fixed meaning in the legal sense. They're often very fluid. And so this is something that even my employer who have very good lawyers who are very, you know, incentivized to help us be successful is like, well, if we have to get lawyers involved in a project, all of a sudden the project can have a minimum timeline of, you know, six months because that type of combing stuff has a real physical time. Whereas if it's open source, you know, the engineers can send an email, the lawyer can respond in, you know, generally a couple of minutes and the project just starts going forward. Right.

**Tim Ans:** Wow. Well, yeah, that's, that's a stark difference for sure. Especially like, because, because the implications are like the financial implications are so strong if they don't do that. I imagine that then it's like this rubber stamp of approval, sort of, like you said, it's an evolving thing, but it's because it's well understood. You can kind of move forward with the knowledge that like, okay, we understand the rules of the game at least without having someone comb those rules of the game and make sure that we're absolutely okay and not going to get sued in A, B, C, and D in ways.

**Sean:** And the ASIC industry was, is even worse in this case, because it's hard enough to get an agreement between two groups of lawyers. But in many cases in the ASIC world, because of the frequently all three of these parts is proprietary, you need a three or four way NDA to get the data. Um, and so you have to have a negotiation between four different parties who all have different

**Tim Ans:** sets of priorities and, and lawyers who charge $800 an hour times, you know, however big their team is. And yeah, it's, it's pricey.

**Sean:** This means that only ideas which people are extremely confident about actually get explored, right? If you have this idea where you go, well, I actually have like a 10% confidence this, this will work, but it would double, you know, the compute power of the system. You're probably not going to investigate that because the amount of effort is huge because you have to go and get all these legal stuff signed. But if you can just try it because all the stuff is open source and there that dramatically changes, um, the willingness to try things. And that's really where, um, uh, I'm coming from is that we want to see more innovation in this space because with Moore's law starting to slow down, um, and compute demand continuing to grow, uh, extremely quickly. We're going to need more new people in this space thinking about how to solve these problems in more innovative ways and to try these things that might seem crazy. Um, there's this kind of idea in Silicon Valley and in venture capitalists that, you know, it's really hard to tell the difference between a really, really good idea and a really, really bad idea. Because if it, if it was obvious, somebody would have already done the idea, right?

**Tim Ans:** Right, right.

**Sean:** The reason that, you know, there's the opportunity here is because most people consider it a bad idea. And this is kind of the space that the ASIC people have been working on in is that, um, taking risks is very, very hard because of all these roadblocks.

**Tim Ans:** Yeah.

**Sean:** And so, uh, we've seen that like the risk five has opened up the ISA space in a way that has allowed a lot of people to start exploring ideas in the ISA space that lots of people have written off as bad ideas. And, you know, most of these are going to be bad ideas.

**Tim Ans:** Right.

**Sean:** But the good ideas are going to eventually come back and, um, improve, uh, the whole space. And this kind of idea that, you know, maybe one in a hundred ideas is a good idea. Yeah. So if you're only exploring a hundred ideas every year, you're only going to get one good idea a year. But if you're exploring, you know, 10,000 ideas a year, you're going to have a lot more good ideas each year. And so a lot of that is what's driving, um, the stuff I'm doing at the moment is how do we increase the number of people that can try things? And most of the people are going to try and they're going to discover actually the reason that's not done. There's a very good reason, but some people are going to discover actually, Hey, wait a sec. Um, our thinking around this space is wrong and we should be doing things differently here.

**Tim Ans:** So you, you mentioned the, the Moore's law slowing down. We've mentioned that on the show a ton, but you actually gave some numbers to that on the FOSI dial up, which is how this all got announced. FOSI is what the Silicon free of open source software, Oh, free and open source Silicon rather SI is Silicon, right? But you had shown some numbers and that, you know, see Moore's law is usually plotted on a log chart going, you know, it's a straight line going up to the right in a log way. But you mentioned, you showed how it started to bend and how we're losing that edge. And that's really basically Moore's law tailing off. What is the projection there? And then what is, what are the needs and like, how does it all kind of come together and like what's being done about it?

**Sean:** It's an extremely complicated problem. If you look at that, uh, graph, there's a lot of interesting things going on there. Um, one of them is that the traditional, um, specification of Moore's law around transistors is still actually somewhat surviving. The number of transistors every year is doubling. Um, but how those transistors are being used and how they can take a benefit of them has been changing. We've kind of hit the ceiling in single threaded performance. The number of cores has increased.

**Tim Ans:** And if people are following along at home too, you can, you can look at about the seven minute mark of this, this, uh, video to see the chart that Tim's talking about here. And it does have like, it's a, it's a mapping of, we have transistors, single thread performance, frequency, typical power, and number of logical cores all mapped against over time. And so it's, yeah. So it's that the single thread is, is that the important one that we're talking about here? That's flattening out.

**Sean:** So that's flattened out for about 10 years now, I think.

**Tim Ans:** Oh, wow.

**Sean:** Uh, and which is why, you know, um, nobody advertises a CPU on gigahertz these days. Right. Um, uh, back in the 1990s, there was always the gigahertz war or like the megahertz wars back then, hundreds of megahertz. The first gigahertz microcontroller was like super, um, you know, uh, interesting. But with that having, um, slowed down, now it's all about the number of cores you've got. There's open questions like, um, if you have this many cores, you need the memory bandwidth to feed it. Um, and how do you get the data in and out fast enough? So those cores aren't sitting there unused. Um, there's also, um, a bunch of issues around power consumption. You know, the more transistors you have in a small space, the more power that space consumes and the more you kind of have to extract the heat from it. Um, that's a serious problem in a lot of applications these days.

**Tim Ans:** Yeah. And are you, are you looking, I mean, so you're kind of tied to the, I don't know your exact team at Google, but some of it is server-based stuff, right? When you say compute, you're talking about large scale, like data centers and like just raw power because the cloud is not going away anytime soon. And like, I've seen some of the data centers, actually Google has some interesting like photos and stuff, the data center, but it's always shocking to me. Like, it's really just about like power in how much, you know, what's the efficiency and then how much can you just crank through these things?

**Sean:** I'm actually part of a Google, um, that focuses on developer productivity. The organization I'm part of is how do we make the engineers at Google more efficient and able to do more cool stuff faster with less resources and across the whole of Google. And so, um, people who sit near me work on things like LVM and all the compiler infrastructure and, you know, shared libraries and they do stuff like, uh, implement optimizations that shave 1% off memory allocation algorithms, which you then apply across the whole Google fleet is a massive savings.

**Tim Ans:** Yeah. Right. That's crazy.

**Sean:** And so, um, uh, that are really interesting to talk to, um, because, uh, some of them are thinking at like the lowest level about how, like, which order these assembly instructions should, um, be issued. Whereas other of them are looking at like, well, how do we distribute the load between our data center, you know, take advantage of, uh, various things like, um, the current climate conditions to, um, get more efficiency that way and other things like that.

**Tim Ans:** Like it's a cloudy day in Oregon. And so we can ramp up by another 5% or something at the Oregon data center or something like that.

**Sean:** I have no idea. Um, there's a lot of different things happening here. Um, and, uh, this is all like about making developers more productive. And what we've discovered in this space is that the time between, uh, finding a problem and fixing a problem, um, is really important to productivity. And when you have complete control over the tool chain, you can dramatically increase the speed that you can do that. Um, which is why we're heavily contributing to things like LLVM is because it enables us to, uh, fix bugs in the compiler, uh, much faster. It allows us to deploy optimizations that we do much, much faster. If we had to, uh, coordinate with an external company to do these changes, um, even if that company was very incentivized to work with us, there's still a lot of overhead there. Whereas with the open source nature, um, Yeah.

**Tim Ans:** Like the lawyers would be back in again. Right. I mean, like you, like you said, I mean, you'd have to make an agreement and you'd have to come to terms on the agreement, figure out who's paying whom. And then, yeah, that's crazy.

**Sean:** And so I believe this is a fairly well-known fact these days, but, um, Google tends to run on, um, it has a single shared code base that is always being built at what would be considered tip of tree. This is kind of the latest version of everything. And we have the same, um, approach with the compiler. So this frequently scares, uh, people when, uh, you talk to them is like, we're running, uh, head of LLVM effectively and compiling things like our ad server that make us, uh, substantial, uh, amount of money. But we have a lot of confidence in this because the problem is, is if you find a bug and it takes a long time to fix, then that's a substantial issue if it's in your ad server. Right.

**Tim Ans:** Yeah. Yeah. Yeah. So you're saying like someone checks in a change in LLVM, it's not tested for some unknown reason, because that's very obviously not going to be the case here. And then it ripples all the way through the system because Google's using it at the, at the, the latest change. So Chris checks in a piece of crap code. Google uses that the next day or hour or minute or whatever. And then it breaks Google ad servers and the price drops of their stock.

**Sean:** That's kind of what people are scared of, right? Like, um, but what actually happens is, um, software developers, um, have bad days all the time. And so humans are very bad at writing software. And so there are bugs going into the code base all the time, no matter how good you are. Um, and so what becomes important is your ability to find those bugs as quickly as possible and then fix those bugs really quickly. The problem isn't that the bug got in in the first place so much is, is if the bug gets in and it then takes two years to fix the bug, if the bug gets in, but it's fixed 10 minutes later, it has very little impact.

**Tim Ans:** Right. Yep.

**Sean:** And so the speed and ability to fix bugs and then deploy those fixes is really important. Um, and this is also really important for security, right? Um, the amount of time between when you discover the fix and you deploy the fix is a really strong aspect of, um, security, right? Uh, because during that period is a period that you can be, uh, successfully attacked. And so you want that period to be as short as possible. And so this is also another reason that, uh, people like Google like this, uh, tip of tree development, uh, style. This is totally, um, the opposite to how ASICs work. ASICs tend to have, you know, um, five year development cycles and then five years to deploy them.

**Tim Ans:** Yeah. And if you've got some kind of like, uh, some security vulnerability that set like the, you know, at the, the, what is it? The, uh, SSL, the tier was a teardrop or tier something, whatever that was, you know, and then it's like in all of your servers, how long does it take to replace all of those? It's crazy. It would be a crazy amount of time to do that.

**Sean:** Um, and so, uh, this isn't my team at all. Um, this is a totally separate other team at Google. Um, I pretty much know only about the public announcements of how this was done. Um, but if you go and look at the ideas around an area, Google has been very successful in creating hardware accelerators is, uh, machine learning, uh, the TPU. Um, and, uh, the development time for the TPU, um, was very, very short and they were, um, able to, uh, deliver very big improvements over a short period of time. Um, and that's the type of thing we'd like to see happen more often. Um, and there's a bunch of different groups at Google trying different approaches to this problem. Um, and, um, my team having a very strong, uh, look at how do we make it, uh, better across the whole of Google has kind of come down to the same conclusion. This quick logic CEO came down to is that, uh, you know, the software engineers at Google outnumber hardware engineers, I don't know, um, a hundred to one or something like that. Um, I don't know what the actual numbers are. That's just totally made up. What we need is our software engineers to be able to do hardware accelerator development just as a part of the everyday jobs in the same way they, you know, do front-end development, back-end development. Um, they're kind of starting to do ML development now. I bet you five years from now, every piece of software is going to have ML in it and it's just going to be a normal part of development in the same way that, uh, you know, um, people have to think about storage of their data. Uh, and that's not a particularly exciting, interesting thing, except for people who are really excited and interested about it.

**Tim Ans:** Right. Or if you're, I mean, well, if you're, or if your job is dependent on pond storing exabytes of data too, then that really matters just because of the scale. I mean, that's really what pushes all of this is like the scale at Google is really driving a lot of this.

**Sean:** It seems like, uh, yeah. And a lot of this is though, um, there's kind of idea that every time, um, something has to scale up a hundred X, you need to rethink how you do it. Whether that's a hundred X in size or a hundred X and load or a hundred X, whatever that really hasn't happened in the ASIC world. We're still designing a lot of these, um, CPUs and chips and stuff using, uh, a lot of the same ideas and methodologies that we were back in, you know, the late 1990s. And we've just kind of relied on Moore's law to enable us to get faster. Um, and, um, you know, the other people at Google trying to solve this in totally other ways, you know, um, I believe we're quite strong in quantum computing, you know, maybe that will make all the stuff I'm doing a hundred percent obsolete because, uh, they just turn out to be able to solve, you know, um, NP hard problems in constant time and stuff like that. Um, sure. I'm not a quantum computing expert, uh, but you know, uh, my group is taking a very approach of how do we get the same type of gains in productivity by making everything into software. Um, and so that's also why we're looking very heavily at the FPGA space because FPGAs give a software style deployment, I can deploy worldwide in, you know, minutes instead of years. Um, and the thing is though, that FPGAs pay a pretty high cost for that configurability.

**Tim Ans:** Right. Yeah.

**Speaker ?:** Yeah.

**Sean:** Compared to ASICs. And so you kind of want to be able to dial that knob back and forth between how much of your design is an ASIC and like can't change and how much of your design is a FPGA and can change. But the traditional kind of model is that, um, you design on FPGA and then you harden your whole design into an ASIC and then you stop. Whereas what we'd like to see is, well, and more incremental approach where maybe you start with something that's fully FPGA and once that's deployed in production, um, you take the parts that aren't evolving and convert them into hardened logic and get, you know, performance gains like that. But there's also going to be parts that are still evolving very quickly. And so you want to keep them in FPGAs and judicial mindset that, you know, um, FPGA vendors have, it doesn't allow you to do that. They want you to keep using and buying their FPGAs. They don't want you to take a design, um, and using like their PCI express controller and harden the PCI express controller into an ASIC, uh, because you're no longer using their parts.

**Tim Ans:** Right. They're, they're magical, uh, the magic sauce that they put into them and charge premium for and all that stuff.

**Speaker ?:** Yeah.

**Sean:** Yeah. And so, um, this is kind of why we're looking at ASICs and why we're looking at a lot more ability to make it easier to move between the two. Like, um, and the only way to do that is to have a thriving open source ecosystem that, um, happens in, uh, both the design and the tooling and how you can make it. Um, and so that kind of what's driving this open source PDK effort is how do we get to a world where, uh, people can make these decisions, uh, dynamically as needed for their application rather than having to just choose off the shelf. Um, whatever was thought to be the good mix five years ago.

**Tim Ans:** Right.

**Sean:** And so there's definitely, um, a lot of interesting stuff happening here.

**Tim Ans:** So, well, can we, can we get back to the actual, the, um, the, the PDK itself as well? Cause you have some other slides that you show in the, about the process itself. And that might be interesting to talk about. I know that you're, you know, you're not super deep into the, you know, process side of things and the physical side of things, but this is probably a good lead back in. And then because the people did ask some questions on the subreddit and on Twitter that we should also get to. So, uh, about the 26 minute mark, you actually have a, uh, uh, slide about the process node itself. And it's higher than I would have guessed, but probably not that high given the fact that it's, you know, it's not like bleeding edge TSMC four nanometer, five nanometer type of thing. So like 130 nanometer is what this is at. What, what is like the level people could use that for?

**Sean:** Um, so 130 nanometers is, uh, 20 year old technology. I think, um, 1999 was when it was first, the first commercial chip, uh, based on 130 nanometers was, uh, released since then. Obviously, uh, the high performance, uh, people have continued to rush down, uh, the transistor size stack. Um, and so what 130 nanometers is kind of used for now is areas where, um, cost is much more important than, uh, performance. And so that tends to fall into, uh, the kind of internet of things space. Um, and so 130 nanometers is thought of by, um, many people as being a, uh, something you should do, um, only microcontroller stuff in it. Um, but back in the 1990, late, late 1990s, early 2000s, uh, people were definitely showing you could do, you know, a processor that run at a couple of gigahertz on 130 nanometers. Obviously that's going to use a lot more power and not be as performant as something on, you know, seven nanometers by almost order of magnitude. What happens if you don't think of, okay, I don't need a full CPU, but I just need, you know, um, the multiply and accumulate unit, or I just need some part that could run at these very high speeds and a bunch of, um, IOT level functionality. Um, we were kind of having a discussion before, um, this recording, um, happened and you brought up the BeagleBone and the fact that, uh, inside the BeagleBone, there's like the main processor, but there's also these, um, RPU units that, uh, let you do effectively, um, software defined real time bit banging type stuff. At least that's my understanding. I've never actually used it. Yeah.

**Tim Ans:** Yeah. Like you could set up like a, a thing that's like watching on a spy bus or serial bus. And you basically say, Hey, once you get the string, you know, throw an interrupt and basically it's, it's actually sitting there and watching or handling, handling like the, the real time bit banging like you're talking about, but it's inside a tiny processor that's on the RTU. Yeah.

**Sean:** Yep. So there's definitely a lot of interesting things you could do around there on this type of process node. Um, especially if you're concerned about power, like the more transistors you have switching, the more power hungry it is. But on the flip side, um, if your peripheral is software defined, um, it doesn't matter that you only have one type of peripheral. It can be an I squared C peripheral. It can be a spy peripheral. It can be a cam peripheral. It can be all these other things defined by what software you load into the little processor. Um, and so I think there's a lot of interesting things that could be done with more, um, approaches to this rather than just say, well, what we're going to do is put a risk five core on it. Why don't we put, you know, a bunch of really minimal risk five cores, one per IO pin, and then a, you know, much more powerful supervisor risk five that is responsible for, um, the compute type thing. Um, or, um, there's a lot of other potential approaches. What happens if instead of having a processor, we have a little FPGA, maybe that's a good way to solve these problems. Um, but there's a huge space of possibilities here that everybody's kind of ignored. Because, well, why would I bother doing this? Because I can just go to a smaller transistor, um, and get increased performance that way.

**Tim Ans:** Right. Right. But then it requires the, the same level of integration. You have to wait for a chip company that's going to be willing to put an FPGA fabric or willing to put six different micros to monitor a bunch of small things. So you really just, you're handcuffed by what's out there. Yeah, of course.

**Sean:** And so as you go down the stack, you become less willing to try more interesting things. Um, and so 130 nanometers is kind of, uh, somewhat a sweet spot where, um, it's old enough that, um, at least Skywater was interested in, um, talking to us about doing this open source PDK, but it's also kind of new enough that you can still do plenty of interesting things with it. Um, it's kind of old enough that a lot of the problems you have to worry about when you're in like seven nanometers, uh, you can totally ignore. Um, and it's kind of got a nice, uh, position for doing analog stuff. Um, as I said, I'm totally out of my depth with analog, uh, but a lot of things like, um, uh, RF things like Bluetooth and, um, Zigbee and stuff like that, all that should be quite doable on 130 nanometers. And, um, it's a lot easier to do it on 130 nanometers than it is to do on 45 nanometers because, um, your transistors are more well behaved and, um, it's easier to understand a lot of, uh, what's going on in the space. There's less variability because the transistors are so large, uh, compared to what is available now. Um, and so I'm also very excited to see people explore that.

**Tim Ans:** So we had some questions about that, uh, flying flux on Twitter. It asks about what's the plan for custom analog right now. It seems like it's not out there. And then like transistor level design asked about, and then are there any open source EDA tools for that sort of thing? And generally I'm kind of interested in the tool chain, what the expect expectation is for generating, generating stuff like this.

**Sean:** So because I have a much more digital background, um, the first thing I wanted to get released was, um, what are called the digital standard cells. These are kind of like the building blocks of building digital circuits. And so, um, they have been published. Um, we definitely want to publish the low level transistor models, um, and what are called parametric models, which is like, well, um, I need a capacitor of this capacitance. Um, how do you build that structure in, uh, the integrated circuit, like metal stack? Um, we want to release all those types of stuff.

**Tim Ans:** Okay.

**Sean:** But, uh, that's mainly blocked on my ability to, uh, finish the work of getting it ready to be released. Um, uh, uh, uh, deal with, um, Skywater only allows us to release certain, uh, stuff. Um, but there's not necessarily a clear boundary in the data that we were provided in the data we have to release. And so there's a process that, um, being a software engineer, I've tried to automate, uh, quite heavily, um, of auditing and, you know, teasing apart, uh, what we can and can't release.

**Tim Ans:** Okay. So that's a, that's a, something that's coming, but it's not quite there yet, but there is plan, there are plans to do, to have analog blocks that are available. Okay. And then what about on the software side? So like magic is one of them. Like, so when I think about like actually processing, I think, you know, like cadence tools and, you know, just huge, I think we mentioned it last week too. Like just, I think I said $50,000 and Dave laughed at me and like just the, the software costs for working with these kind of, uh, making actual chip design. What, what is out there? Do you know what tools are available to people if they're, even if they're just using the digital blocks?

**Sean:** Uh, that's again, why we, um, focused on the digital side first is that the digital open source ecosystem is a lot, uh, stronger than the analog, uh, uh, open source ecosystem. And so, um, and it has a lot more overlap with the areas I'm much more familiar with, like the FPGA tool chain side. Uh, for example, um, the first step in both, um, uh, FPGA, um, compiling and ASIC compiling is a thing called synthesis. And, um, um, at the moment, the best state of the art tool for that, um, is Yosis who's developed by, um, Claire Wolf and Symbiotic EDA. Um, and that is the synthesis front end that, um, targets both, you know, the open source FPGA effort and the open source ASIC effort. Um, the same kind of initial, uh, input, uh, after Yosis, it kind of starts to diverge. Um, place and route for FPGAs is actually, uh, quite different for, than, uh, place and route for ASICs. Um, in some ways it's much harder. In some ways it's, um, uh, much easier with kind of ASIC place and route. Um, you have a lot more freedom about where you place things like your and gates and all this type of stuff, right? If, um, if you need to insert an and gate, you can kind of push the other and gates slightly out of the way and like drop it in. Um, whereas in FPGA place and route, you only have, uh, what is available in the FPGA. Right.

**Tim Ans:** You're just reconfiguring the LUTs and telling you, Hey, you're, you know, you and you and you with your flip-flops and your logic function, you're now an and gate.

**Sean:** And so it's very much a much more discrete optimization problem with very huge cliffs. Like if you move something, um, it generally, you know, increases the delay by significant, uh, values. Whereas if you move something in the ASIC world, it generally only increases it by a little bit and you can kind of move only a little bit or a long way. Um, and so, um, place and route are very different between the two.

**Tim Ans:** So it's more like, uh, um, so like with a place and route for a FPGA, it's like, uh, trying to optimize the number of boxes you can fit into a UPS truck. And with a place and route for an ASIC, it's more like how much liquid can I fit in this bowl?

**Speaker ?:** Yeah.

**Sean:** Yes. That's kind of a interesting analogy. Um, but, uh, that's why we've kind of focused on the digital world is because YoSys is actually, uh, a very great tool that is a long way along, um, to being, uh, a very high quality tool in both the FPGA and the ASIC space. Um, there's still a lot of work, uh, that to be done with, you know, new advanced optimizations and, um, uh, uh, we've actually, um, my employer has actually been funding a bunch of work to do things like, uh, DSP inference in, um, YoSys. Uh, um, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh And so one of the hopes is by getting a lot of people to do ASIC design through things like the Skywater PDK, we will start to understand where Yosis needs to improve.

**Tim Ans:** Got it. So what is, after Yosis, what, so the PNR, the place and route for the open source stuff for FPGA is like NextPNR. That's like Dave and FPGA Dave.

**Sean:** So there's, for FPGA place and route, there's currently two options. There's NextPNR, which is FPGA Dave, Dave Shah, and there's VPR. Both those tools have their pros and cons. NextPNR is a really, I'm amazed at how good NextPNR is. Given the amount of developer resources that go into that. Next, sorry, Dave Shah is like an amazing developer.

**Tim Ans:** A 10x developer.

**Sean:** Yeah, if there ever is a 10x developer, he is a 10x developer.

**Tim Ans:** Yes. And people can support him on Patreon if they're interested.

**Sean:** Yes. Apparently that became a joke at one of the super cons due to some of my slides encouraging people to do that. But NextPNR takes a very code-based approach to FPGAs, whereas VPR takes a very data description-based approach. It's been around a lot longer. It's actually the grandfather of Quartus 2, which Intel is. Oh, interesting.

**Tim Ans:** Okay.

**Sean:** So it has a long history. That is both good and bad. It's good because there's definitely been a lot of work to show that VPR can be turned into what's considered a commercial quality tool. But it's also showing its age in some of the code. But I definitely think it's one of the best things to happen to GCC is having LLVM be a viable competitor. If you look at, for example, the way GCC improved their error messages once LLVM was a potential competitor to it. Like GCC error messages, if you haven't used a more recent GCC lately, it definitely rivals LLVM for providing decent error messages for C++. It actually does a better job in a bunch of cases. So I actually think there's actually room for both NextPNR and VPR in the ecosystem. And I'm actually working on a project to enable stronger mixing and matching between those two tools, better interchange format for getting data in efficient ways between those two tools. So that's kind of the place and route in the FPGA world. And in the ASIC world, up until a couple of years ago, a guy called Tim Edwards developed a system around Qflow. That was kind of the state of the art a couple of years ago. And then DARPA launched this program called IDEA where they wanted to create a viable place and route alternative for doing ASIC place and route with a strong focus on the place and route tool producing stuff that is manufacturable. So one of the things I found amazing about what I would consider a compile step. So one of the things I found amazing about ASIC design is that at the end of your what I would consider a compile step, the design comes out and probably has, you know, a couple of thousand errors in the outputs that have to be fixed manually. So if you've gone, done PCB design, you know, this design rule check.

**Tim Ans:** Yes. And the page that pops up and says, you're going to be here a while, Chris. Yes. I know that one. I know that one well, Tim.

**Sean:** Yeah. So you have a similar type of thing in ASIC design. The rules are quite a lot more complicated, but at the end of most of the commercial tools runs is that they produce a result that has DRC result, like DRC errors in it. And then you have to pay somebody to go and manually fix all these DRC errors. Oh, okay. To me, this is kind of like your compiler, like spitting out semi-working assembly instructions. Right. Exactly. So you have to go and fix.

**Tim Ans:** Right. And it's different. It's different than the errors that might be because it's not syntax errors. It's not like your code's bad. It's literally that it didn't finish compiling it properly. It didn't. It's like, yeah, actually, I don't know where that jump instruction was supposed to go. Sorry, man. You can go fix it. Hire an assembly programmer. What's your problem? That's crazy.

**Sean:** And so DARPA realized that this was a huge impact to its ability to iterate on designs. And so started this program as part of IDEA. A guy called Andreas Olofsson, I think that's how you pronounce his name, was the program manager who kicked off this. Right.

**Tim Ans:** Andreas has been on the show before as well. He's the parallela. Yep. He's the former project of his. And now he was doing the DARPA stuff. Yep.

**Sean:** Yep. He's no longer at DARPA. He's got a new project now. But he kicked off this effort. And a project called the Open Road Project was started a couple of years ago. And now that is probably the best open source ASIC place and route. Even Tim Edwards, who developed Qflow, is now a strong believer in Open Road. And Open Road is what you should definitely use if you want to do stuff in the open source place and route for the digital stuff.

**Tim Ans:** Yeah. So let's do a quick recap. So someone has a design. They go and pull down a RISC-V core from, say, a GitHub repo. They put some stuff around it. They write their Verilog. They put it through Iosis. That has synthesis output. It goes through Open Road for place and route. Then what happens to that? Is that now a file that can be sent to Skywater to be manufactured?

**Sean:** That's the theory. The output of the whole compile flow is a thing called GDS. GDS could be thought as being equivalent to Gerber files in that it's a bunch of shapes with a little bit of annotation. And in theory, you can send that off to be manufactured. If everything is working correctly, my statement is true. There's still a lot of work to make the theory and practice converge. Like, you can't use the Open Road project to do any of the analog stuff. And so in an ASIC, you're going to need various things for the power supply. And the IO pins are generally considered to be an analog circuit. And so if you already have those ready for you and you place them in the GDS, the rest of the Open Road flow should work for you. But that's kind of one of the holes that exists in this program at the moment is that we don't have any things like analog to digital converters or level shifters or any of this type of stuff. And so we need people to go out and release them as open source so that they can be integrated into this flow and that they can be automatically placed around as part of your design. If you're just doing a CPU, a CPU by itself is probably going to work at the moment. But when people think of a CPU these days, they think of a CPU plus a bunch of peripherals, right? And so the peripheral stuff is kind of where there's quite a bit lacking at the moment.

**Tim Ans:** Well, I even think about having a PLL internally. You know, that's analog. Yeah, there's a ton of analog stuff you have to have there. So I did want to call out. So there's a couple of really good questions here on the subreddit. But before we do that, the same person, Sine Oscillator looks like, on Reddit said, mentioning some of the free software for IC design that's out there. So this is IC layout, DRC and LVS is Magic, LASI, L-A-S-I and Electric VLSI.

**Sean:** Magic would be a parallel between PCB new. It's the type of thing that you draw rectangles in.

**Tim Ans:** Yeah, yeah. Yeah, like standard cells, you're saying, right?

**Sean:** Yeah. You can do analog design that way by drawing, you know, the various rectangles that correspond to your transistors. Magic also does effectively the design rule checking, the DRC step. And so generally, you could kind of think of it like your Gerber viewer as well. Once the place and route has done, you load the Gerber into Magic and Magic runs and verifies that you haven't violated any of the design rules. Magic is actually probably the oldest piece of software I've ever gotten patches into it. It's so old, it's older than I am. How old is it? I'd have to go and look it up, but I think it's like 1981 was when it was first released. It is so old that it predates things like the BSD license. Like, this kind of threw me for a loop because I was kind of looking at the license file for it and going, this kind of looks like a BSD license, but it's not a BSD license. And so I sent it to the lawyers to like, because it's a separate license, they have to go and review it. And they're like, yeah, this kind of looks like a BSD license. What's going on here? Why isn't it just a standard BSD license? And it turns out it predates the standard BSD license. So that's pretty amazing.

**Tim Ans:** Has it been like updated though? Like, I mean, is it, so if someone goes and uses it, does it feel like it's software from 1981 or like?

**Sean:** It depends on what you think software from 81 looks like. It definitely looks a bit dated.

**Tim Ans:** Not much graphics wise. I think a lot of terminal or like terminal manipulation type stuff.

**Sean:** And it's definitely always been a graphics tool. The, you know, X and graphics stuff like X has been around for quite a long time. I have no idea when that was added to magic. So maybe magic started as a terminal tool. I, you know, I was a baby when these things were probably being developed. But magic is definitely continue to be developed. We use magic to, for example, render SVGs of the standard cells. So like SVG is a modern web standard and it can output that. The alternative to magic at the moment is another thing called K layout. K layout is a much younger project. It uses the QT library. It's definitely a much more modern tool. I've never used K layout. So I don't know what stage it is, but I've heard lots of good things about it. Okay. And so that's also another alternative. We would like to get better K layout support into the PDK, but nobody's had the time to do that. And obviously Tim Edwards has been highly involved in this effort and he's the developer of magic. So magic support has been the first priority.

**Tim Ans:** Got it. Okay. So other things that are on this list of circuit simulation are then, so you'd mentioned simulation as well. And obviously that's going to be a huge thing. LTSpice, Zeiss, XYCE, NG Spice, and MicroCap. And then parasitic extraction is FastCap and FastHenry. And then finally, digital placement route is Qflow.

**Sean:** So the digital placement route would be open road. For simulation, for analog simulation, you'd be using some type of spice. This is where, again, I'm out of my depth. And in many ways, you probably have more experience here in that the spice you use for doing IC design should in many ways be the same and share a lot of commonalities with the spice you do when building analog circuits on PCBs. It's just the whole thing is a lot smaller.

**Tim Ans:** Yeah, calling back to that Mike Englehart episode, he did mention that when linear was linear, they actually, the developers used that spice engine to develop the actual chips that linear was making. So that was shocking to me at the time and still kind of feels shocking. But yeah, it's the same physics that's happening. It's just usually smaller and you have more control over the actual cells that are in there as far as I can understand it.

**Sean:** Yep. But you also have to worry more about a couple of milliamp makes a huge difference when your transistor is working at the microamp level.

**Tim Ans:** Yeah, right.

**Sean:** And you have to worry about things like noise that previously you didn't. And so I would love to see a lot more happening in that space. Schematic capture. Schematic capture. I don't know if there is a good tool for doing schematic capture. That's, you know, drawing the resistors and the transistor layout of, you know, from a human point of view, like this resistor is at the gate of this transistor and that type of thing. And it's of this value. It might actually make sense for something like KiCad to be used as the schematic capture. And maybe something like KiCad could export the right details to do the simulation of the actual transistors.

**Tim Ans:** Yeah. So ng-spice is now built into KiCad as well. So that's another thing. So you could actually, you could use, you know, at least I haven't, I honestly haven't used it yet, but you could use, you could capture the schematic and you could do some simulation inside of KiCad right now. So I'm still, I'm still an LTSpice man myself, but, but yeah, there's, there are plans to further that as well inside the KiCad project. So.

**Sean:** So the last time I ran spice to try and do anything was probably like 2005 ish.

**Tim Ans:** It feels the same, honestly. It's yeah, it's still very netlist based.

**Sean:** I would not say I'm very, I was very successful back then. And so I'd love to see people explore this a lot more. Um, I think you mentioned Zeiss. Zeiss is a very fast, um, spice simulator that is targeted at the type of simulations that you do inside, um, ESICs. It's also funded as part of these, uh, DARPA ERI initiative. Um, the only thing about Zeiss is that it's not, it's more of a, um, code dumping type project in that, uh, all the primary developers work for Sandia labs and, um, it gets updates all the time and everything like that, but it's not some, a project that you can really contribute to easily. Um, that's apparently because, uh, you know, there are national security concerns around it because it's used, used for doing things like nuclear simulations as well.

**Tim Ans:** Yeah. Yep. Yep.

**Sean:** But it is an open source software, um, in the sense you can go and download it and compile it and apply patches to it under a, uh, open source approved license. And it'll be interesting to see what's, uh, uh, you know, people can do with these tools. Now they have the data available to, uh, run these tools and build ecosystems around these tools. Um, something that like things like electric really struggled with is that how do you write a tutorial for using electric for analog ASIC design? If you have to sign an NDA to get access to the data required to do the tutorial.

**Tim Ans:** Right. Right. Yeah. And it does seem like gluing all this stuff together is, is kind of tough. So I want to talk a little bit more about that, but before we do that, I want to talk about the fact that there was a post that Google is actually funding people to, to make some of these chips. And so there's some questions about that. Uh, first off, like what, what is the criteria for, so Google's going to fund a shuttle run of chips for people. I think it was like up to 50 chips for design. How, how does someone qualify? So they go through all the steps. They have a chip they want to get made. They send it to Google. It's all open source, but like, what, what is the requirement to get it made? And then how is it chosen or not chosen?

**Sean:** So that is still, um, evolving. The general idea is, um, uh, to be clear, you won't be sending it to Google at all. Um, you'll be sending it to, um, a company called eFabulous. Um, eFabulous is in charge of taking, um, these 40 designs, uh, and putting them together into the shuttle and then getting back the, um, uh, ICs back to the people and, you know, making sure people get their right design back. Um, that's all going to be handled by eFabulous.

**Tim Ans:** Will they come back as, uh, bonded to packages or will people have to work with them at the silicon level as well?

**Sean:** So the current goal is that, um, you'll get back a wafer chip scale package. Um, that's probably around four millimeters by four millimeters, um, roughly. And it'll probably have about, uh, 50 IO on there of which about 40 will be, um, for a person's, uh, design. The other 10 will be, you know, power supply and a bunch of, um, uh, supervisor, um, related stuff.

**Tim Ans:** Okay.

**Sean:** And so, um, I know wafer chip scale packages are frequently quite scary to hobbyists. And I know I was quite scared of them for a long time. Um, and then at some point I was forced to use them and discovered that, uh, they are much easier to use than QFN parts.

**Tim Ans:** Yeah. That is consistent with what I've heard as well.

**Sean:** Basically, it turns out, uh, when things at that size, uh, solder surface tension is magic. Um, I'm sure people have seen this with, you know, resistors. If you get the resistor pretty much anywhere generally in the vicinity, it just kind of snaps into place. Um, wafer chip scale packages will do that as well. You basically get them mostly aligned and then surface tension sucks them right into being perfectly aligned. Right. Uh, whereas like QFNs always have that giant ground pad that is super hard to, um, you know, heat up enough that the, um, solder reflows correctly.

**Tim Ans:** Right. Well, if you put too much solder there too, then it's like swimming in that sea of center pad solder. And then you might have one side that's higher than another and yada, yada, yada. Yeah.

**Sean:** Um, and so I won't even deal with QFN parts anymore. Um, I have, you know, probably a 50% rate failure rate on my ability to, um, solder QFNs and like maybe an 80% success rate on, um, uh, soldering, uh, WCSP packages. And some of that as well is that the package is so small, it doesn't have a lot of thermal mass. So it heats up really quickly as well. Um, and it reflows really easy. Um, I think once people start doing, um, wafer chip scale packages, they quickly, um, stop fearing them.

**Tim Ans:** Yeah.

**Sean:** And especially like, uh, bull grid arrays are a bit different. Uh, bull grid arrays start to get, um, big enough that the surface tension doesn't help you as much. Whereas because, um, WCSP packages are so small and so light and the surface tension is so strong. Um, they act much more like you're soldering things like resistors than they do, uh, things like, um, you know, big IC components. Um, so, um, the other, uh, thing we're trying to do is make sure that there's a very good selection of, uh, breakout boards. Um, so that you'll be able to, um, and we may even go as far as having you get back a bunch of, um, your ICs pre-mounted on these breakout boards that do things like expand it out to a cast related edged, uh, module, or maybe even a dip package. Uh, so that's still all open and we're currently, you know, exploring, um, uh, what the correct optimization function to do there is.

**Tim Ans:** Okay. How about, how about the choosing of the, so you said 40 projects. Yep. What is the requirement that gets someone on that list?

**Sean:** So the first requirement is that your design has to be under one of the approved open source licenses. Um, that list hasn't been published yet. If you're making a, if you don't care about what your stuff is licensed under, just choose Apache 2. Okay. Because that will a hundred percent be on the list. There are a whole bunch of other ones which will be on the list, but we haven't published that yet.

**Tim Ans:** Okay.

**Sean:** Uh, GPL will be fine. Um, a GPL will not be.

**Tim Ans:** Yeah. We, that's, that's a, for whoever's listening to do that. So then, okay. So it's got an Apache 2 license.

**Sean:** Yep.

**Tim Ans:** What else?

**Sean:** Is that it? It needs to pass the design rule checks.

**Tim Ans:** Okay. And are those published, someone else asked about that. Are those published anywhere? Because actually that sign oscillator on Reddit asked about that as well.

**Sean:** Yep. Um, there's, uh, versions of those getting published in the official PDK repo. There will be, um, those design rule checks once, um, we're happy with them will be available there. Um, there's a couple of, um, work in progress, uh, versions floating around, um, that if you go on the, um, the skywater PDK Slack channel, you can, uh, find, uh, people using them there. And, um, once we've got confidence that those design rules cover everything that we need them to do, um, they'll be included in the official, um, upstream, uh, repo. Um, um, they're still evolving, um, but, uh, we're pretty confident in them at the moment. Um, there's still just a few more checks we want to do before we release those.

**Tim Ans:** Okay. Great. Great. But then is it just first come first serve after that? So passes DRC. So it's open source passes DRC.

**Sean:** Yep. If we get more than 40 submissions, then we will figure out our criteria to do that. Um, it will probably be a lottery system initially, but, uh, we're still working out what the details there are. It is very unclear to me whether there will be 40 submissions or not, especially 40 submissions by, um, basically mid November. Um, so you haven't got a lot of time to do it.

**Tim Ans:** Okay.

**Sean:** We will be doing, uh, more runs after the November run. Um, this isn't a once off thing. Um, we want to see people iterate. And so if we do come up with some type of criteria, it's mostly probably going to be, uh, focused around people who are doing experimentation, like having, um, multiple versions of the same thing in their design, uh, so that they can evaluate trade-offs.

**Tim Ans:** So not just, not just like test elements you're saying, but more like having, uh, implementing four different risk five cores, five different risk five cores and seeing which one is the most, the efficient or power or something like that.

**Sean:** Yep. Um, if we're coming back to analog stuff, um, implementing a variety of different ADCs or DACs, um, uh, would be very interesting. Um, that's also why we're looking at things like, um, analog generators, uh, because we would like to see a lot more experimentation in the analog space. Um, it's reasonably easy to do that, uh, five different risk five cores experiment. Um, it's much harder to do the five different ADC experiments.

**Tim Ans:** Yeah. Yeah. Right. Cause you're hand placing things and you're dealing with it like that. What about the, like, okay, so it has to pass DRC, but there's no guarantee that it's going to work. I mean, like, and I guess that's an okay thing, but is there any kind of like human involved checking to be like, well, why did you hook up the ADC to nothing? Or, you know what I mean? Like there's no ERC effectively. That's all kind of on the designer ERC being electric rules checking. It's like the actual A is hooked up to B correctly, B is hooked up to C correctly as, as you expect it to be.

**Sean:** Um, there is a lot of, um, ERC like stuff in the DRC. Um, there's also, um, what's called LVS, um, which is layout versus schematic.

**Tim Ans:** Like, I'm just saying that like, if someone, if someone draws, you know, something stupid as, as someone who's drawn a lot of stupid things, Tim, you know, I can do, I can do DRC all day long and it can look great. But if I didn't actually hook up, you know, if I just hooked up the, uh, what's the, what's the one I always seem to do? Oh, it's like, there's no error because the power input, the, you know, the three, 3.3 volt rail is hooked to a capacitor and which is hooked to ground. And because there's no dangling nets there, right. Pin one is hooked and connected to pin two DRC is happy. But I, since I didn't source any power line to it, yep, nothing's driving it. You know what I mean? Like, so, and then, and then that's a bodge wire. There's no bodge wires here, so there's nothing at that level though, right?

**Sean:** This is an open question.

**Tim Ans:** Okay. All right.

**Sean:** It's much more a problem for the analog people, um, because, you know, uh, the digital design tools do that type of verification. They do the check that, you know, all the power pins are connected to the power rail and they actually go as far as checking that, you know, um, there should be enough current available at that point. Uh-huh. To drive the transistor because, um, you know, resistances of a couple of ohms can make big differences when you're talking about micro apps again.

**Tim Ans:** Sure, sure.

**Sean:** And so, and so, a lot of these tooling, I believe, exists and is checked by a lot of these stuff. Um, and my general goal is, uh, very similar to the DARPA goal is I don't want a human to have to review it. Um, I want a computer to do all the checks it can automatically. And this is actually why I think, um, uh, I want more software developers involved because, uh, this is a software problem. Writing, um, a piece of software that understands that actually that capacitor that you connected doesn't satisfy your ERC rules is something you could do. Uh, it's just somebody needs to write that. Yeah.

**Tim Ans:** And I mean, if you're using something like, you know, the schematic capture, like e-schema for KiCAD, there are rules in there like that, of course. I'm just saying that, like, there's, there's nothing gating the DRC because that's, uh, that's done at the fab level. It's saying, Hey, if you're not doing all of these things, you need to within the standard blocks, or if you're not using the standard blocks, then you have these set of rules that are governing, like, you know, how big your transistors are. There's minimums, maximums, whatever. But there's nothing at the end of the day saying you have to pass because there's no standardized schematic capture. There's nothing that says you have to pass ERC, just like the board house, you know, you know, PCB way or Osh Park. They don't care. As long as I pass, as long as my, you know, via isn't too close to my, my trace, they don't care if the trace goes nowhere, right? They don't care about that. They just care that the, the things that they can check in the physical realm are checked and work, work as expected. And so it just, it's not a question of whether or not it's right or wrong. I'm just saying that there's, there is no check right now. And so I think it's more of a warning to listeners that it's like, if you're going to do this, the ERC is on you and there are tools for it. But again, this is an open, this is an open design notebook and you can, you can scribble all you want, but you better make sure your, your lines connect.

**Sean:** Yep. And, um, I would definitely like to see people describing, um, uh, best practices on how to deal with things like, actually we screwed up this part of the chip. How do we isolate that? Um, like I have actually no idea how, um, uh, you set up multiple power domains that you can easily isolate. However, one of the things we're trying to do with this is that, um, the silicon, uh, is probably going to be somewhere about four millimeters by four millimeters, but only 10 millimeters of that is going to be available to the user. The other six millimeters is going to be, um, what we're calling the harness and the harness is going to have a little risk five core in it. It's going to have some memory. It's going to have a couple of other things in it. And the idea is that, um, we've gone through the verification process of making sure that this risk five core actually, you know, works and boots and all these types of things. And it can be used to probe other parts of the chip and turn on and off other parts of the chip as a piece of software. And so you can kind of imagine that this, uh, harness risk five will have a bunch of virtual GPIO pins that you can connect to various things in your design to turn them on and off. Or, um, another thing we'd like to see is, um, 10 millimeters squared is actually quite a lot of silicon space. Um, you could probably fit, uh, 10 risk five processes on there fairly easily, but you don't have enough pins to effectively have, um, you know, each risk five have its own dedicated set of pins. So, um, what we want to do is people to put MUXs on the IO pins that let people select between the different projects, maybe that the, or the different designs that put inside.

**Tim Ans:** Right.

**Sean:** Their, um, space and have the, um, the harness CPU able to configure that. And this probably won't happen in the first version of the harness, but in future versions of the harness, um, we also want to have things like internal ADC sensors. Yeah. Current measuring. And so you can do internal current measuring because like you said, um, it's very hard to, uh, do bodge wires on an ASIC. Um, it's not impossible. I have seen people do, uh, crazy things like that. Um, it's not something I would ever do. So, um, we want to be able to give people the ability to understand when their stuff fails, why it's failing, and then improve on it. Because we want people to iterate. Uh, we don't want people to go, well, the designs taped out. We're never going to change it again. We would like to see people go, well, we got this quality at this point. How do we improve it and make it better? Yeah. How do I take somebody else's IP and make my own IP and cross compare the two with the same input and show that, uh, my version is better. And how do I make that reproducible? One of the things that, um, has the EDA industry has struggled with is because of all these NDAs, how do you reproduce, um, you know, somebody's research? If you need to sign an NDA with three different companies to even start getting close to, um, getting the raw data they have. And so, um, this is kind of stunted people's ability to try things and actually show that, well, their way of designing the ADC is better.

**Tim Ans:** Yeah. Yeah. Yeah. So like you're saying, like experimental test setups that are described in papers, they're just theoretical at this point because you can't, you can't replicate it exactly.

**Sean:** Yep. Um, and that's also why, um, one of the other things we're doing, like normally in these, um, multi-project wafer programs, you maybe get back five copies of your project, uh, like five ICs.

**Tim Ans:** You're saying like MOSIS or something like that, MOSIS project?

**Sean:** Yeah. Things like MOSIS or Europractice or that type of thing. Uh-huh. Um, they come back, they're probably raw silicon. So then you have to go and figure out how to package them. And then once you get them back, you maybe mount one or two of them and they become the most precious things on the planet, right? Like you don't want your lab partner sneezing anywhere near it because you only have one that works. Instead, what we're trying to do is get people back, you know, um, hundreds of ICs in ready to go, uh, form factor that enables you, like you might personally only need a couple, but if somebody else wants to reproduce your work, you can just go, okay, here's.

**Tim Ans:** Yeah. Ship one or something. Yeah, exactly.

**Sean:** Ship five. Like you don't want to ship one because, you know, maybe that's a dud one. Um, you know, ship five and it shouldn't be an issue. And so like definitely looking at, oh, a hundred, it may be as many as, oh, like 400, depending on how things work out.

**Tim Ans:** Okay.

**Sean:** And that also enables people to share much more readily. Like if you're getting back five chips and you've got five projects, each person only gets one chip. If you've got a hundred things back, each person gets 20 chips. So, um, that's also driving some of our philosophy of how we're looking at this program is, um, and why the type of decisions we're making don't look a lot like the traditional Euro practice or Moses decisions here.

**Tim Ans:** Yeah. Yeah. I mean, yeah, at a 400 chips, at 400 chips, you could do, I mean, you could do a Kickstarter. You could, you could actually, you know, like you said, you could send it out. You could have a store of them so that when you publish your paper, you could send any, you could, you know, say, we'll send you a chip to verify it, that kind of thing. Speaking of the Kickstarter thing, that idea, like, so it's open source, of course, but is there any, like, this can't be a commercial entity or can it be companies? Does it have to be nonprofit type of thing?

**Sean:** Nope. As long as your design is open source, there's no other conditions at the moment. Um, obviously, you know, um, I'm not a lawyer and I don't, uh, get to make all the legal agreements that go in place here. Yeah. The lawyers know what my goals are and have been very supportive of this. Uh, we're trying to build an open ecosystem. We're trying to build an ecosystem where people can do things like find ways to do this full time, um, as their day job and to, uh, you know, make new companies out of that. This, like, that is very important part of a thriving open source ecosystem is having those commercial entities contributing to the ecosystem and building out, uh, some of the less fun parts of doing this. Right. Um, uh, and we see this in open source, like, um, you know, uh, lots of companies contribute to the Linux kernel, lots of companies contribute to LLVM and GCC, um, because it's in their best interest too. And I'd like to see that happen here as well. We'd love to see, uh, companies investing in the open road project because it makes their ICs better.

**Tim Ans:** Yeah.

**Sean:** Right. Like if you could improve open roads, um, you know, performance by 10%, it's like, maybe that gets your, um, integrated circuits to be 10% better.

**Tim Ans:** Yeah.

**Sean:** And, you know, that adds up, you know, 10 companies make, um, the tooling 10% better that quickly starts making the tool substantially better and able to do substantially, um, uh, bigger and more impressive things.

**Tim Ans:** Yeah. Yeah.

**Sean:** There's kind of this feedback loop here, right? Like the more, um, the tool is able to do, the more people who use it and contribute it to it, the more things it can do. And this is kind of gives, uh, that kind of exponential growth we're seeing with software, right? Like, and the open source world, it's always kind of slow to start. Um, but this feedback loop means as it gets going, it gets going faster. And then that makes it go faster, which makes it go faster.

**Tim Ans:** It's not a reason to do it, but it's interesting too. Like, so like up until, well, I, I think that like, so we've had guests on the show who are doing Silicon startups and it's just like, it was nearly impossible that, you know, the fundraising had to do and just the, the difficulty of doing all that stuff. You know, you could send out for a, you know, a shuttle run, like a TSMC or whatever. You could do that kind of thing. But like running, like starting a chip company is one of the hardest companies to start just because of the capital requirements, even if you're just doing a fabulous model. And like, like this could, like you said, it could open up the idea for a lot of new companies and, you know, a lot of innovation and like, I'm sure we'll talk about it next week, but like there is more consolidation than ever. And so like, this could be an actual thing that helps to move the whole industry forward as well. And, um, yeah, so that's, that's really, really cool.

**Sean:** Yeah. And I think, um, there's a joke that people say here. It's like in the software world, a startup is, you know, anybody with a laptop and $50 of AWS credits. A startup in the hardware world is a company with 50 employees and a hundred million dollars worth of capital.

**Tim Ans:** That's right. Yeah. Cause you just need it, you know, you need to do that sort of thing. And so, yeah, um, you'd mentioned a, uh, uh, uh, you know, the collaboration aspect. Is there, so two questions here and then we should probably start to wrap up. Uh, first off, is there anywhere to go and collaborate or maybe that's a good second question. And then is there a good starter project to even look at? Is there like a chip that people can go and look at all of the files? So you can go and download the PDK and we'll have links to that, of course. But is there an example project just because I would be wondering about what are the files look like? What are the block diagrams look like? You know, is there something where someone could go and grab part of it and refactor just the digital component of it? You know, so like it has all the, the tooling for the analog, the IOs, all that. Does that exist yet? And could people go and just rip out the digital and put their own digital section in there?

**Sean:** So I'm going to answer the questions in the order you asked them. Damn. So, uh, there's, um, a Slack, um, workspace, uh, skywater dash PDK, um, Slack channel that has at the moment, uh, seems about like two or 300 people, um, on that channel discussing various things. Um, you're quite welcome, uh, to join that Slack and to start discussing your project ideas and to start, um, forming teams. Uh, there are groups that have already created their own channels for various areas that interested in, like there's a group, um, a channel for, um, a project called open FPGA, um, that's done out of the university of Utah, um, that is trying to build a, uh, open FPGA on the skywater process.

**Tim Ans:** Huh.

**Sean:** And so, uh, there's a bunch of people looking at that. There's a channel dedicated to people doing risk five processes on skywater. There's a channel dedicated to people who are using VHDL. Um, I'm not a VHDL person. I don't care about VHDL at all. Um, but there's a thriving community there of people who do care about VHDL. Um, uh, there's a thing called J core, which is, uh, um, super hadashi or SH based processor that a bunch of people, uh, looking at trying to, um, tape out. Okay. You might've also seen that, uh, IBM has made power and open ISA. Oh yeah.

**Tim Ans:** Yeah. Yeah.

**Sean:** And so there's a bunch of people, um, looking to tape out power based chips, um, on skywater. Um, and actually, um, there was in, I have a document that's supposed to kind of, uh, give some inspiration for what could possibly done at 130 nanometers. I'm hoping Chris will include a link below, um, for the right price, Tim.

**Tim Ans:** I will. I think after all this, you know, you really gotta, of course I'll include it.

**Sean:** Yeah. And so that actually links to some of the IBM, uh, high performance processes and papers around those that were done on 130 nanometers back in the 90, like late 1990s. I wouldn't suggest trying to replicate what IBM did, but there could still be quite interesting, um, information in their paper about, you know, some of the techniques, uh, they did in this area. Um, and maybe those apply to some of your designs. There's definitely a lot of interesting literature out there that I would love people to reproduce. There's also mailing lists. Uh, the mailing lists are mostly fairly quiet at the moment, but definitely go and sign up for those, especially the announce mailing list, because, uh, the announcement mailing list, uh, will be the first place you hear about when, um, the exact criteria for, um, uh, the shuttle run is posted and you know, how to actually submit a design to that will also be posted to the, um, announcement list. So, uh, that's definitely a place you should go and sign up. Um, there's also IRC and maybe there should be a Reddit forum. I don't know. So that's kind of, there are plenty of places to go and talk about stuff in this thing.

**Tim Ans:** Do you need to get an invite to the Slack or is it just open?

**Sean:** Sadly, Slack doesn't seem to have a way to be just open, um, without paying absorbent amounts of money to that. Yeah.

**Tim Ans:** I've seen, uh, there's like Heroku apps that like you put in your email and then it'll send an invite, you know, it's just like a little thing that's been in there, but.

**Sean:** We need to set up that. Uh, there is an invite link on, uh, the announce list that will be valid for another, I think, 20 days and we'll try and make sure that there's always a invite link available somewhere.

**Tim Ans:** Okay.

**Sean:** And, you know, we'll probably set up a invite bot as well. Um, but I haven't had the time to do that yet.

**Tim Ans:** Okay.

**Sean:** You asked the question about having templates and preexisting stuff.

**Tim Ans:** Yeah. Like a good starting place, right? So like we've got the standard cells, we've got the digital stuff, but you mentioned all of the IO and kind of everything around it, power supplies. It would be great if there was like a starter ship that you could just go and, like I said, just rip the guts out. That's digital. And then you just kind of go hook into that.

**Sean:** So if you look at the, uh, Fosse foundation's dial up talk series, you will see, uh, that one of the next upcoming talks is from, uh, guy called Muhammad Shalan. Um, and he will be talking about the open, uh, road being used on Skywater 130 nanometers. And as part of that, there will be a bunch of, uh, demo risk five chips that are actually out for manufacturing, um, released. Um, they may be released slightly before that, uh, but they're quickly running out of time. Um, and these should fulfill that, uh, template requirement. I had hoped they would, uh, be in a position to release them earlier. Um, but, uh, they didn't get their act together, uh, quickly enough. Um, uh, but there's definitely, we want, uh, those things to be available. Um, but we're also looking to the community to, um, build up resources in this area. I'm not, uh, ASIC designer by heart. Um, I, there are a lot of areas where this is just as new to me as it is to everybody else. Um, and I would love to see tutorials, for example, on how to use magic and how to use K layout, how to do analog transistor design. Um, all these types of topics, uh, things at the moment, I know nothing about, and I'm really excited to see, um, some of the later talks, uh, in this Fosse dial-up series, um, that go into detail about, um, how various things like that are done. Um, there's one from a guy called James Stein, who has actually been designing a totally new set of standard cells for the skywater process.

**Tim Ans:** Hmm.

**Sean:** And, uh, the reason we funded him to do that was we wanted to prove that there was enough tooling and, um, uh, data available in the PDK to enable people to explore new standard cell design. Generally standard cell design is a specialized, uh, process. In, uh, this case, we want to see people, uh, explore new types of standard cells and new ways of optimizing standard cells. Do you want to optimize for power performance area, some other type of, um, uh, criteria? I don't know. Um, maybe the standard cells we have there are actually the best that ever going to exist, but I kind of doubt that given, um, what I've seen the open source world do.

**Tim Ans:** Right. Right. Well, like you said, if there's different requirements or it might be different optimizations, so it would be good to be able to tweak things and dial different knobs.

**Sean:** Yep. And I think there's also, um, co-evolution of the tooling, um, like standard cell design currently is very much optimized for the existing, uh, closed source proprietary tooling. What happens if you're able to, uh, change the place and route tools to better enable different styles of standard cells and evolve those two together rather than evolving them separately. Um, we've definitely seen that, um, that is super powerful. There's kind of this idea in software engineering that like every problem in software engineering is solved by either adding a level of abstraction or removing a level of abstraction. And this all being open source allows you to add levels of abstraction, but also remove levels of abstraction. And maybe that will enable new interesting things that, um, uh, previously have been discounted as being impossible. Uh, there's a really cool example of this is the, um, uh, project from, uh, the university of Michigan, um, called FASOC. And what FASOC tries to do is treat analog design like digital design, um, where you have a bunch of standard cells that you effectively use place and route to layout. If anybody who is an analog designer is listening to that, I'm, uh, most certainly sent jewels down their spine.

**Tim Ans:** They're screaming, they're screaming inside their heart as the, uh, as the Japanese have advised people to do on roller coasters. Yep.

**Sean:** Um, but, uh, if you start enabling the place and route to understand some of the requirements that, um, uh, analog placement and routing has like, you know, the relationship between placing cells, things like, uh, place and route do start to see like it could be possible. It's also, um, potential that is not, um, but we can explore that space now, whereas previously we couldn't. And that's what's getting me super excited about this.

**Tim Ans:** Yeah. Yeah. Yeah. I think rules-based, I mean, like just like, you know, there's some, some, uh, auto placing, auto routing type things can work. I think there's like a balance between, you know, how, uh, how well your rules are defined and then, you know, what you're willing to give up. Like if you're willing to give up more space, then you, you can probably have a more, uh, a more easily, like, uh, you know, a place and route could, could move stuff around easily. You don't need to pack it in as tightly. You don't need to know every, you know, there's not, not as much interaction between these standard analog cells, but if you can't do that because you're space constrained, then you have to start doing some hand, hand construction and more attention to detail on each, each individual element that you're putting in there.

**Sean:** The great thing about computers is though they've gotten significantly faster, um, over the last 10 years and you can try a lot more things if you have an automated approach, right? Um, that's true. You can, uh, in some ways try the brute force approach. Well, let's just do a thousand variants of this and run it on, you know, cloud and, uh, have it, uh, do the simulation and pick whichever one matches what you wanted best. Yeah.

**Tim Ans:** Yeah. And actually if people go back and listen to when Craig Bishop was on the show, he talked about that at the PCB level, he's actually making some tiny PCB type things for chiplets for his job. And he was talking about doing that like iteration and basically just trying to make the best connection many, many times over. So yeah, it's definitely something where you could throw just horsepower at it.

**Sean:** Um, and I think you've previously had a guy on The Amp Hour who was doing things like, uh, PCB antennas and a lot of things like that, that also falls into this category of very similar type of thing where a lot of the case you want to do a lot of variants because, um, uh, you want to be able to try a lot of different things to get stuff to work.

**Speaker ?:** Yeah.

**Tim Ans:** Yeah, exactly. Yeah. You know, that's, it is interesting. It feels like right now this would be, so again, if we're going to equate the silicon process to like the PCB process, it feels like right now this would be, you go through, you make your, your schematic, you make your layout. And then, you know, it's, it's a very, very expensive process to go and get the quote unquote boards made. Google's picking up, you know, the first 40 that are out there. That's nice. But even still there's, you know, it's, it's also going to take months to get your board, your quote unquote boards back. Yep. But when Adrian Tang was on the show, Adrian was the NASA designer who was doing chip design. It was interesting hearing him talk about the, the level of, he was talking about the different tool set. I think, I think he was talking about cadence, but he was saying that if you have the PDK and if you're using tools that are well-known, that basically the simulation just doesn't really differ that much. And that's an interesting idea to me, like that it is such a controlled environment and that like these PDK process variables are so, so well characterized that like you could get a, get away with just simulating and then expecting very similar behavior. It's not like you're going to get a chip back and be like, well, the simulation said it was going to be, you know, 1 milliamp and it ended up being 4,000 milliamps, you know, or something like that. It's like that it does match it well. And so in terms of like the flow and moving people towards doing this sort of thing, it, it seems like if people are comfortable simulating, if the tooling set up so that you could validate your, the process that it could move us towards a scenario where the hobbyist or someone who's just on their own could potentially make a design that just works now, you know, as far as that phrase.

**Sean:** Yep. It's kind of interesting because these things are so small, um, frequently physics works, uh, much more ideally at that space.

**Tim Ans:** Yeah. Yeah.

**Sean:** Space. There isn't a lot of, uh, variables because, uh, or like the speed of light, you know, is an important variable. Um, but it's such a huge difference that, you know, these simulations can be built to be very accurate. Um, yeah, this is all again, beyond, uh, I always find this super interesting, but I've never had any time to explore it or understand it. Yeah. And I'd love people to do that.

**Tim Ans:** Yeah. Well, I think people can, people can think about that too, but just like from like chip scale package versus like a, a dip package, right? Like just thinking about like the bond wires to go from a piece, you know, it's still got a piece of silicon internally. It's got to come out the bond wire, go to the chip leg, go down to the chip leg. If you plugged it into a breadboard, you know, you've got to go across the metal thingy up to the, the wire. And just like thinking about all of the, all of the weird stuff that that signal encounters between it. And then now, you know, like the last two episodes ago we had, um, we had Ming on talking about chiplets and that, you know, basically takes it down where now your interconnect layers also in silicon and you can, but, but like what you're saying now is now shrinking that down and not doing it between chiplets, but actually keeping it on silicon and just thinking, yeah, like how much shorter that path is and how much more optimized it is. And there's a ton more overhead, like we've talked about this in this episode, but because you've removed a lot of that, you can, like you said, it's, it's much more closer to the ideal than it might be. If you're going through a dip package to a, through a breadboard, through a jumper wire, my God, like the fact that it works at all, when you start to look at it like that is really amazing.

**Sean:** Yep. Um, I also remember back when, um, people were saying that, you know, PCB, uh, development would never really be within, uh, the capabilities of hobbyists and would never be like, um, uh, you know, cheap enough to do. Accessible. And like, I can now get what was like previous generation mobile phone technology, um, PCBs for, you know, uh, less than a couple of hundred dollars, um, shipped to me. It's just amazing. Um, uh, what happens when you have a lot of competition in the market and when you have a lot of, um, people wanting the, um, uh, to do this stuff, um, like Osh Park was really important in enabling an ecosystem to start to exist. Um, which then meant, uh, other people could start saying, well, look, I see what Osh Park are doing, but I think I can do it better or I can do it cheaper. Um, and so that's when, you know, all these other competitors started coming into the area and Osh Park still do a very good job at what they do, but there's a lot more options out there. Um, and I'm hoping what we can do is see the same thing, uh, in the EDA and the ASIC design industry. Um, and it's very easy for me to justify, um, you know, if we get 10,000 design submitted to, uh, this program, um, you know, there's a strong justification. We should be taping out more than 40 of them.

**Tim Ans:** I mean, hell, at that point you should be, Google should be starting a fab, you know, like that's, it's like, that's a lot of, that's a lot of people that there's like pent up demand. And like you were saying at the beginning of the show, the potential for innovation is really there because it's now just been unlocked. There's just been this gate in the way.

**Sean:** Yep. And, you know, um, Google does have a long-term mindset and is interested in how, uh, these industries can change. Um, and so, um, I'm excited that they're willing to let me experiment in this space and see what we can do. Um, we're also open to actually, maybe we're wrong here. Um, you know, maybe this is a lot harder and we'll get two designs and neither will work. I don't think we're wrong. Um, we have a lot of proof that we're not wrong. Yeah.

**Tim Ans:** I think, I think even if you just look at the academic sphere, you know, and like you look at the amount of people that are still using Moses with all the other stuff that's in the, all the other barriers that are in the way, it's like that alone will be, we'll fill up that shuttle run. I think, you know, like just thinking about all of the grad students that are out there. Um, but now they might be able to make the second chip that they've, they thought was commercially viable and might be the startup that they couldn't have made otherwise.

**Sean:** I was talking to a academic the other day and, um, he has a class of a hundred, um, ish students that he teaches ASIC design to every year. And, uh, the problem he has is only the top three students or four students get to see the results of their work. Um, everybody else, uh, like effectively only ever does theory. Um, and I was discussing with him and it's like, well, it's actually, if you have a hundred students and you're going to do this every year, it's potentially possible to like get everyone of those students back a couple of hundred chips for a couple of hundred dollars each.

**Tim Ans:** Yeah.

**Sean:** You know, um, definitely, uh, it's not with on, uh, it's not beyond reason that by increasing the number of people in this area and like driving down the cost of the tools and the accessibility of it, that all these things get orders of magnitude cheaper.

**Tim Ans:** Yeah.

**Sean:** And, you know, um, have you seen a project called chips for makers?

**Tim Ans:** I have not, no.

**Sean:** Uh, so chips for makers is, uh, run by a guy called staff and he is trying to develop effectively the Osh park for, um, ASICs. Um, and so I talked to him frequently and, uh, he's been working with us to, um, help, uh, build out this ecosystem. Um, and so, um, I think that's very interesting. He has some certain approaches that are different to the approaches I'm taking, but that's good. Um, he wants to concentrate on like retro computing. And so wants a lot of IO pins and, um, uh, actually wants to, uh, be on older process nodes than what we're looking at, uh, because, uh, that drives the cost down even further. And so, uh, I think that's kind of interesting.

**Tim Ans:** Um, yeah, that could be like a feed. That could be like a feeder group. You know, that could be the, the single a baseball team that leads into the triple a baseball team or a double a or whatever. Yeah. And I think, you know, like watching KiCat and just to have how that has, you know, the improvements over time in terms of the software itself, but then also the enabling of more people, not like there was a shortage of software, but the stuff that happened around it. Right. So like the thing I really love about the project is the plugins that I get access to and the people that are writing like Python scripting around it. Don't get me wrong. I love the tooling itself, but like, like the, the fact that there is that openness and people are willing to kind of just jump in and be like, oh, actually, you know, I just fixed this thing. And like that, that happening over and over again has enabled more than I would have expected.

**Sean:** Yeah. I think KiCat is in the position that people are going to start saying, you know, KiCat is an overnight success of how many people are doing it when it's, you know, started in 96. Yeah. Overnight success, 10 years in the making. That's right. But this is kind of what you see with projects like KiCat and things like RISC-V and this type of thing that kind of have these exponential growth curves is that they seem to be going nowhere for a long, long time. And then you look away for a day or two and you come back and all of a sudden go, holy crap, there's more stuff than I can keep up with.

**Tim Ans:** Then there's a RISC-V in your, in your Western digital hard drive or whatever that is, you

**Sean:** know, like, it's like, oh my God, it's crazy. Yeah. Um, it's, and like, I think, uh, KiCat has kind of hit that point is I can't keep up with all the cool and new things that seem to be happening in the KiCat community, uh, these days. I like, there's just too much cool stuff. If I, uh, look into that community, uh, nowadays, um, I lose days worth of, uh, you know, time.

**Tim Ans:** Yeah. Down the rabbit hole you go. Yeah.

**Sean:** Yeah. Um, so I've actually started to avoid that in some ways, um, so I can get other work done. Um, but the thing is like, if I come back to it, um, all that stuff is going to be a full be so much better. Like I did a board back with DDR back before they had, uh, you know, length matching or push and shove routing and any of these other things. Yeah. And, you know, it took months to do that board. Now, um, you could probably do it in, you know, a day or two.

**Tim Ans:** I think, uh, Greg Davil just cranks one out every other weekend. So, yeah. Yeah.

**Sean:** He is definitely very good at doing that. He is. Yeah.

**Tim Ans:** Yeah.

**Sean:** It's, it's very impressive.

**Tim Ans:** And his pictures are amazing, right? I know. Yeah. Well, yeah. He's, he's a favorite around here. Uh, yeah. So, okay. So Tim, what I hesitate to ask, but what else should people know about this? We are now at two 15 in, uh, so we should probably try and make it before two 30. What do you think? Can we do it?

**Sean:** Yeah, I think we can.

**Tim Ans:** Okay.

**Sean:** I think, um, what we are trying to do here is an experiment. Um, we're trying to seed and build an ecosystem. When you think about it that way, um, the things that are going to be most successful in this space, things which build on top of other stuff and work together. Uh, yeah. If you're coming from a traditional ASIC background, um, you should flip all your assumptions about how you should do something. Uh, you should release it early. You should publish it openly. You should, um, you know, shout it from the rooftop before it's been taped out in silicon.

**Tim Ans:** Yeah.

**Sean:** You know, all these types of things that your gut is telling you, I don't do this. And even simple stuff, like, um, there are so many people, um, I've talked to in this space who are like, oh yeah, that's so easy. And I'm like, that seems like almost impossible to me. Uh, why don't you share how to do it? Um, you know, things like a simple eight bit ADC. I've talked to some analog designs, designers who are like, yeah, I could do that in my sleep without thinking about it. And I like, I have no idea how to do that. Why, why isn't this documented as a tutorial that I can follow and these types of things. So write that down and publish it or like publish your designs.

**Tim Ans:** Yeah. And I think, well, I think there might be one, one pushback I could, I could see. And I'm sure that this is like, as the software, you know, folks moved into the open source world as well was like, yeah. But if I do that, if I, you know, put my design out there, I'll never make any money because I'm just giving away the farm. And it's like, uh, yeah, that might be the case, but, uh, more likely you will actually bring notoriety to yourself and you'll be asked to do the next interesting thing. You know, it's like, there's that always that push pull of like gatekeeping and, you know, like worrying about like working yourself out of a job. But like, there's just so much to do. It doesn't seem like that would be likely.

**Sean:** Uh, yes. And, you know, um, uh, IBM just recently bought Red Hat for some massive amount of money. Above 30 billion, I think. Yeah, it was a lot of money. And so it definitely shows there is a lot of ways to make money from, uh, open source software. And I think open source hardware actually, um, has a lot of potential there. I think a lot of the potential though is in what it enables for companies like Google. Um, and this is my personal opinion, not Google's opinion, um, is that things like Linux enable Google to do things. And, you know, Google is a very successful, profitable company. Um, but it's only able to do the things it does is because this ecosystem exists.

**Tim Ans:** Ecosystems, I think too, because it's not just Linux. It's also all the other tools that are built around it. Right.

**Sean:** And the internet, right? Like, uh, the internet is an open collaborative space in many ways. Right. Um, if you think about back when the internet was coming, uh, into its own, there were, commercial closed networks like, um, what was it? Something like CompuShare or something and AOL and, um, CompuServe. CompuServe.

**Tim Ans:** Yeah.

**Sean:** And what happens?

**Tim Ans:** Oh, AOL days. Yeah. Those suck. Well, there's still a lot of angry people that have the email addresses, I'm sure. But, uh, you know.

**Sean:** Yeah. Um, and so, um, you know, doing new hardware design to enable you to build a company that does like solves some real world problem where it doesn't matter that the hardware, like the hardware is a means to an end. It's not the thing you're trying to do. Mm-hmm. I think there's going to be a lot more of that. And I'd like to see a lot more of that. Um, there's a bunch of people at Google who talk about, uh, the next wave of software is software and where the and is something else like software and medicine or software and

**Tim Ans:** education. Yeah. Yeah.

**Sean:** Yeah. And I would like to see, you know, hardware and in many ways, or, uh, design your own hardware. And, uh, the hardware is just a means to an end, a tool to get you to do things. And because there's a lot of things which are still computationally too hard to do. You just don't have enough, uh, computation to do that. And hopefully by designing hardware, you'll be able to solve this. You know, you'll be able to reduce power requirements so that the thing does run on a coin cell battery now. Mm-hmm. So, um, another thing is, uh, don't listen to people that tell you you can't do things would be the other stuff. Like there's a lot of potential negativity in the ASIC space around, oh yeah, somebody tried that and it never worked. Mm-hmm. They may be right, but, uh, don't necessarily assume they know better than you. Um, listen to them, uh, get their feedback, but also verify. Maybe some type of condition has changed since they made that experiment. This was clearly a case in, uh, FPGA place and route is that a lot of the experiments were done back in like the early 2000s. Since then, computation power has gotten so much better that, uh, problems that were considered intractable back then, uh, easy to do now.

**Tim Ans:** Interesting.

**Sean:** Uh, so, you know, um, I think there's a lot of interesting stuff in this space as well that could, uh, fall into that category. Uh, try stuff. Don't be afraid to fail. Share your failure is the other thing. Um, you learn a lot more from when things don't go correctly. So, and other people in this space could learn from that. So publish your failures.

**Tim Ans:** Right. And I think, I think they often pop out of the woodwork and often offer to help them too. Like that, like people that you might not know are watching and might have expertise that you didn't know about. And then, you know, but publishing about it definitely can help gather people to, to your cause and your next, your next, uh, trial.

**Sean:** And people can solve problems you thought were impossible to solve, um, and help you do that if they know you're struggling with it. Right. Um, if they don't know you're struggling, they can't offer the help.

**Tim Ans:** Yeah.

**Sean:** That's a good point.

**Tim Ans:** Tim, where can people reach out to talk to you if they want to?

**Sean:** So, uh, you can contact me at, uh, my email address. It's T Ansell, A-N-S-E-L-L at google.com. Um, I'm obviously getting a lot of email at the moment. Uh, so, uh, please, uh, forgive me if it takes a while to respond. Um, you're much more likely to, uh, have more success by going on the Slack channel and asking the community because, uh, there's a lot more people in the community that can, uh, answer your questions and, uh, if you've got the question, um, you're, it's likely somebody else has already asked the question. And so, uh, other people can probably answer it for me. Um, and that's the only way, you know, this will scale, um, is if people help other people, uh, don't be afraid to ask questions. Uh, but do, uh, try and ask questions in a way that allows more than just me to answer them.

**Tim Ans:** Yep. Okay. Well, Tim, this has been great. I'm glad that you came back to talk about this. Like I said, in the fourth, when you're coming back to the Amp Hour next time, remember you have to be putting together basic matter, some kind of matter compiler in order to, you know, that's the next level down. So remember that's, that's your next, your next goal, uh, for the next time you're on the Amp Hour.

**Sean:** 3D printing transistors, maybe.

**Tim Ans:** We, apparently we're not allowed to talk about that around here, but yeah, that, that would be, that would be the next step, I suppose.

**Sean:** Okay. All right. I think I've got my work cut out for me for a while yet. Yeah, I think you do.

**Tim Ans:** We'll talk to you soon.

**Sean:** Yeah. It was nice to talk to you too. Thanks, Tim.

**Speaker ?:** Bye.
