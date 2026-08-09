---
episode: 650
title: Accessible ASICs with Andreas Olofsson
url: https://theamphour.com/650-accessible-asics-with-andreas-olofsson/
---

**Andreas Olofsson:** This is The Amp Hour Podcast. Released November 12th, 2023. Episode 650. Accessible ASICs with Andreas Olofsson.

**Chris Gammell:** Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics. I'm Andreas Olofsson from Zero ASIC. Welcome back, Andreas. How are you? Thank you, Chris. I'm good. I was re-listening this morning to our last time you were on the show. Episode, I should have this up here, 254. Different times, different companies, different life stages we're all at. So I'm glad to have you back. You've been doing some very impressive things in the meantime.

**Parallela:** Yeah, thanks, Chris. Yeah, I was kind of blocked out from appearing for a while, but it's been a long ride.

**Chris Gammell:** I would love to hear about some of the reasons for being blocked out from appearing, because I think it's actually pretty interesting. You're in between your current thing and the thing you were on last time for. Let's talk about the last time, though. So last time you were on, you were on for the Parallela, which was your company was making. Adeptiva was your Adeptiva. Sorry, am I spelling it wrong? I may have spelled it wrong on the show notes. Adeptiva. Adeptiva. Yeah, I spelled it wrong on the show notes. It's been wrong. I'll correct that later. But that was a project that you would discuss spinning out for parallelization of mathematical operations, if I'm remembering the recording correctly from this morning. Yeah, that's right. Great. How did it all go? I mean, you're not doing that anymore, so I assume it went okay?

**Parallela:** I mean, yeah, people ask me that. Was that a success? Was it a failure? I chalk it up as a success, even though everybody wants to be ARM, NVIDIA, Intel, right? If you set the bar that high, you're definitely going to fail. But we shipped devices. So just rolling back that story, right? In 2008, I started a parallel processor company, which was 15 years ago. It was in the Great Recession. Great time to start a company.

**Chris Gammell:** Yeah. Yeah.

**Parallela:** Semiconductor. It was the ice age of semiconductor. And I was able to raise a little bit of money, but I didn't raise enough to really grow a semiconductor company. So I thought, let's try something different. Let's try to actually open up the specs, be more transparent with the community. And let's see if we can work with the community to create a platform instead of just trying to create everything ourselves and then just push it on everybody. So we did the Kickstarter with Parallela, open source board, made our manuals available, open source drivers and all of that. And I think it almost worked. I think the timing was off. We kept getting these questions and I, you know, going to customers and asking, you know, well, how are we going to program this thing? And a lot has happened in the last 15 years.

**Chris Gammell:** Yeah.

**Parallela:** Yeah.

**Chris Gammell:** Yeah.

**Parallela:** And I think it was just, it was too early. Didn't raise enough money, but we still shipped 10,000, 20,000 eval boards to 10,000 customers.

**Chris Gammell:** Wow. Yeah.

**Parallela:** That's very impressive.

**Chris Gammell:** Yeah.

**Parallela:** And, you know, we shipped these all over the world. We were in 200 universities. You know, a bunch of people used the parallel boards for publications because it was accessible and open. I think that it was also cited academically fairly well, right? Because it was significant work. So I'm proud of the work we did there. It was good.

**Chris Gammell:** That's great. Yeah. And so, again, I was re-listening this morning and you, back on the last show, you kind of described it as a math coprocessor. And what popped into my head was kind of thinking, I mean, around a lot of the growth of, there's other parallelization that has been happening. Specifically, I think about the NVIDIA, how that's, you know, massively parallel as well. Is it kind of hitting that same space? Was it kind of targeting the same stuff there as just a framing?

**Parallela:** Yeah, for sure. And, you know, it comes down to, you know, you have to have the full solution and you have to work with your community. But we were definitely, I was watching everything that NVIDIA was doing at the time and taking notes. You know, they're still doing great things in terms of growing a community around the platform. Yeah, true. Engaging with people. You know, CUDA and research and just lowering the barrier for adoption in AI and machine learning. They get it. And it's just, I think, I don't know how many billions of dollars they've spent, but it's a lot, right, to get there. Sure, sure.

**Chris Gammell:** Yeah, I was actually just, I was just thinking about the actual architectural differences, if there were any. Like, you know, I'm going to once again play ignorant on, you know, computer architecture side of things here, though. You know, you mentioned it as a math coprocessor when we recorded, you know, kind of handing off operations that are heavy math intensive things. And then what little I know about, like, GPUs is that they, a lot of cores, you know, splitting up a lot of tasks amongst cores. But it felt like there was maybe more stuff happening at each individual core. Like, there's more command handling. I don't know. I'm terrible at this stuff.

**Parallela:** Yeah. I know. Yeah. We can get, you know, dig down as much as we want here. But I think one of the things that NVIDIA has done that's really amazing with the GPUs, right? First of all, GPUs are available everywhere, right? So now you have the access part. It was always a big deal. And then you go, okay, how easy is it to use? And that's where their abstraction and their computer architecture model has really clicked with the community. Right? Yeah. They produce some software stack that really works. And I think, you know, one of the things that was different between the GPU and SIMD, which they're using, or SIMT, SIM threads, and our multi-core CPU approach is that, you know, we kind of had a modest number of CPU cores. You know, 16, 64, and then eventually 1,000. But that meant that the user or the programmer had to really kind of think about how they partitioned the problems. Right. And with the GPU today, you just kind of say like, all right, we've got sort of 1,000 or 10,000 parallel threads. And then the programmer, you just have to make sure you have hundreds of thousands of threads. And then you have a kind of a scheduler in the middle to make sure that that connection is done effectively. But it, you know, and I'm simplifying here, but it gave a good abstraction model for the user that the programmer could use effectively. With a multi-core, the way we were doing it, and I think a lot of AI companies are doing today, that abstraction is still too plunky.

**Chris Gammell:** Got it. So it's like kind of a don't make me think model. That's what NVIDIA is going towards, and it's just like it just becomes a software problem versus more of a bespoke hardware, like having to understand the underlying. Like one thing we talked about in that last episode, too, in 2015 was like kind of comparing it to FPGAs as well and just thinking like, you know, the promise of FPGAs has been floating in the air for many, many, many, many, many, many years. And it's like, but there is so much knowledge required at that level, I feel like to have, you know, you're building your own architecture, you're building your own stuff happening under the hood. And then most software people, I feel like, don't want to deal with that. They just want to, they want to push data through. Is that, is that fair?

**Parallela:** Yeah. I mean, every, every, every software developer is different, right? You have people doing, you know, JavaScript and Python and people doing C++ code. So I think it's, but I think, I think in general, Verilog is harder than, than Python. I think that's a pretty good. Yes, I agree with that. Yes. But even, even, I think actually the Verilog abstraction has been incredible, or VHL abstraction has been incredibly successful over many decades. And, you know, it's, you know, I can write Verilog code in, if I don't use IP blocks from a specific vendor, I can kind of push the button through and it just works. If I wrote the right RTL code and I can run that on a, you know, different vendors, FPGA devices, even if I'm careful, take the same Verilog code and, and use an ASIC without, you know, without changing anything. So I think there is, you know, I think Verilog and VHDL gets a bad rap sometimes. I think it's, it's one of the true universal standards, but it is definitely more difficult than, than Python.

**Chris Gammell:** Yeah. Yeah. It is interesting as well. So another kind of theme that I was hearing in that last episode was kind of the unit economics that felt like that was a thing that's kind of gone through the, it's like a through line theme for a lot of the stuff that you were, you were talking about then. And I, I'm guessing some of the stuff we're talking about now with zero ASIC as well, but like, how does, how has that changed? Is there, I mean, we've seen some of the PDKs opening up, but I'm not sure if that's as, as effective at the, you know, the bleeding edge side of things. You know, it's not like TSMC is opening up. So like, has the unit economics changed in any appreciable way from, from what you're seeing aside from just general Moore's law shrinking?

**Parallela:** Yeah. That's, that's a, that's a great question. Cause you know, having two companies, right. One in start in 2008 and one in 2020 you can take a snapshot and say, right. What has changed, right. Yeah. Two semi-connected companies. So, okay. Where to start? I think first thing is open source is a lot more developed these days than it was 2008.

**Chris Gammell:** At all, at all levels, at all levels of like chip, chip design, software design, all of those.

**Parallela:** Yeah. Yeah. I mean, if you really think back to 2008, I mean, people are still using CVS or SVN or, you know, Yeah. It's all Git, right. Yeah. And on the, on the EDA side, when I started Adaptiva, right. I used Verilator and that's still great today. It's much better today, but it was great back then too. But that was pretty much the only tool available that was good enough to use. And, uh, and today, I mean, I, I have a, now I have a meta repo on GitHub that just tracks open source projects. And it's, it's like 400 projects on there. That's great. And, uh, so that is just, and it keeps growing. So I think, you know, open source hardware, open source EDA, different components. It is absolutely night and day. So that's one thing I've changed.

**Chris Gammell:** What do you think is driving the, so the, you know, there's a culture piece and like you said, get, get hub and things like that. You know, maybe more accessible sharing tools I'm guessing, but like from a, again, like a unit economic, sorry, this is not a unit economic, maybe like people economic piece. Is there something in the ecosystem that's allowing more people to contribute to open source? You know, like just from a, people got to feed, feed themselves.

**Parallela:** I, I think it's a, um, a cultural drag along type effect. Oh, okay. You know, soft, soft, soft, soft, soft started first. Yeah. So after it started first, right. And so you had, you know, the GCC, Stallman, Linus, right. All, you know, they, they, they were the, the, the pathbreaking, you know, revolutionaries, right. Eighties and nineties. Sure. And, uh, and then, you know, it was a fight, right. Yes. Some of the big vendors to the death and open source one. And then, uh, you know, kind of been in the same fight in hardware. It's not, it's, it's, you know, open source is the thing that lifts all ships. Yeah. And I, you know, I, and I've been, I've been seeing this for 15 years now and it's, uh, it's tiring to be honest with you. It's like when Steve Ballmer, I think he says something like open source is a cancer or something to the effect. Right. You know, I feel like we're still having those conversations today in hardware and like, come on. It's yeah. Can we move past this? Right. Yeah.

**Chris Gammell:** Get on the good foot folks. Come on. Yeah. Figure it out. Yeah. Yeah. The chip companies being like, we were doing something radical. We're going to do open source. It's like, oh, oh, cool. Yeah. Yeah. So yeah. It's just about like where it hits and when it hits that sort of thing. Yeah. It's a, it's a really interesting piece. So open source is a big one. Uh, some tooling sounds like, what about, what about like the fab level economics?

**Parallela:** So, uh, fab, uh, I mean, I mean, I'm, I'm an advanced digital person. So if we look at, you know, analog, right. You know, different, different criteria, older nodes, like one 30 and, you know, one 80, but for, for digital, it is incredibly expensive. So if you track 15 years, there's less fabs today than there were in 2008. Interesting. And, you know, and it's, it's just, it gets more expensive. Mask sets are, you know, in 10 to $20 million per, per tape out. Uh, and, uh, you know, IP has gone through the roof as well. Design tools are increasing and there's less fabs to talk to. It's harder to get into those fabs as a startup. So, and of course, I mean, they know, right. They, they're not going to take, they're going to, if, if the tape out is $20 million, why would they talk to somebody coming in who clearly doesn't have $20 million?

**Chris Gammell:** Yeah.

**Parallela:** Yeah.

**Chris Gammell:** They, they clock you walking through the door, huh? Yeah. The, uh, the, the, the Silicon, the Silicon country clubs, as it were. Oh, you don't have the entry fee, sir, or nor the jacket required.

**Parallela:** So, so that is, uh, that is definitely, uh, a huge barrier and that, that needs to change. Um, so I think right now, uh, I, I gave a talk, uh, last week that I called the semiconductor singularity, uh, which, uh, I'm people have talked about singularity before, but to me, that means that as we scale towards one, you know, zero nanometer, the, the cost and complexity goes to infinity. Yeah. And that's sort of where we're trending towards, right. That the, you know, there may only be one, one project left because that product is going to cost a billion dollars to, to do. Yep. It's probably for a smartphone or maybe for a data center. And there'll be one fab left because, you know, when every EUV machine costs $300 million and, uh, you need a bunch of them to stay competitive. There's like one fab left that can do that.

**Chris Gammell:** Maybe. Yeah. Yep. Yeah. Yeah. It does make you wonder how the, uh, ASML salesperson, uh, you know, going into TSMC, they're like, what else are you going to buy? I'm going to make my quota this month because of course I am. Uh, well, I guess I'm in the wrong business. Uh, yeah, that's, that's really interesting. So is anything going to change? I mean, like, are you seeing anything else shake up in the market then? I mean, uh, I've seen some, some stuff and some, like, like, for example, uh, past guest of the show, Sam's the roof. He's working on an atomic lab, Silicon, right? Like that's, you know, trying to do small scale, but that's not going to be like leading node and nothing's with a leading node. So, or is it just going to be the, the, anyone who wants to be competitive has to pay the toll to, to get to the front of the line?

**Parallela:** So no, the, the answer is chiplets, chiplets, chiplets, chiplets, chiplets, chiplets. Okay. Okay. I'm going to keep saying that word, right? And then I'm going to define what it means, but basically that is the savior.

**Chris Gammell:** Great. Yeah. Right. And that, and spoiler alert folks, you know, usually we, we come to things later, but that is, that is what zero ASIC is all about, right?

**Parallela:** Yeah, that's right.

**Chris Gammell:** Yeah. Cool. Okay. Quick interlude because I like to, uh, you know, keep people in suspense a little bit about the current stuff. I'd love to hear about your, your interlude in between Adaptiva and zero ASIC. What were you doing then? Whatever you're allowed to talk about, I suppose.

**Parallela:** Yeah. Yeah. Sure. I mean, uh, most of the stuff I talked about was, was public. Right. And, uh, I just have to preface with that. Anything I say is my own personal opinion. Sure. Does not represent the U S government. Right. I'm no longer, I'm long gone from, from DARPA and U S government and all of that. Right. So I think, you know, the reason I went to DARPA was first of all, somebody gave me the opportunity. They tapped my shoulder and say, Hey, are you interested? But my mission there was to really reduce the barrier to design. So I, you can imagine, right. I, I basically killed myself for nine years at Adaptiva with, uh, raised $7 million to do five generations of microprocessors where, you know, Intel would have spent a billion. Yeah. And so I was working, you know, 80 hour weeks, uh, and the team was as well, and it was just a losing battle. So I was, I was frustrated. And so I, I decided I wasn't going to go to DARPA and, you know, fix the high cost of design. It should be possible for three smart people to design a chip without having to do all the other crap that you have to, sorry, all the other stuff that you. Crap's okay. Okay. So, but yeah, it, it, you know, it should be, you know, because in software, right. In Python, JavaScript, or in the C++, you know, you can get pretty far with three really smart people.

**Chris Gammell:** Yeah.

**Parallela:** And, uh, and in hardware that's in chip design, that's not even close. Right. So, so I went to DARPA to try to reduce the barrier to Silicon. That was my mission.

**Chris Gammell:** Um, I have to say, when I saw on LinkedIn that a former guest had gone to DARPA, I was like, whoa, that is obviously you couldn't talk about it at the time, but like, that was, that's super cool. I mean, like, and so you came in with that, that actual, with that, uh, that mission, like that they brought you into, to, to work on lowering costs of chips. Uh, yep. That's right. Cool. Go DARPA.

**Parallela:** Yeah. Yeah. So, so this was, you know, my, my, my boss at the time, Bill Chappell, who, uh, just a incredible visionary, uh, when, you know, I actually came in, I was presenting at Optiva and parallel and some ideas I had to, uh, to the group there and didn't even know who he was at the time. He was the director of MTO and, uh, he was, you know, peppering me with questions. And then basically after the presentation, he came out and asked me, have you ever thought about working for the government? And, uh, that was it. That was, I was hooked. So, and then he asked me to come up with a mission and, uh, and I pitched the mission to him and he said, sounds great. When are you ready to come? So.

**Chris Gammell:** That's great. That's like the, uh, I saw the, you know, they started that digital agency a couple of years back for like people that come to do service, like, uh, healthcare.gov and like helping all the, what do they call it? A digital something, I don't remember in the U S government, at least. And I always thought it was like, like, as a, you know, you do a couple of years service and I was like, there's nothing I could do there, but like, I'm not saying I could do what you did, but like a little bit closer to like, I can't write JavaScript, but I could maybe, you know, talk about chips for a little bit and that would be fun. So that's cool. That's really cool.

**Parallela:** Yeah. And I mean, it's, it's, I mean, just to, uh, you know, talk about the article, but it's a absolutely unique place, right? You, you come in there, uh, you're, you're, you have an expiration date on your badge when you come in. Oh, interesting. It's like milk, right? You're, you're, you're expired after two years. Can you re-up?

**Chris Gammell:** Can you, can you get a new refresh badge or no?

**Parallela:** If, yeah, if you, if you do well, right, if you start a new program, then you can get re-upped, but then after like four or five years, they definitely kick you out. There's no, it doesn't matter how good you are. You're up. Oh, yeah. They almost had to carry people out of the building because they didn't want to go and they're like, no, sorry. Right, right. Yeah.

**Chris Gammell:** That level of access and like the smart people you probably get to talk to. Yeah. That's gotta be intoxicating. Yeah. Did you have to work in DC though? Is that, that, that's probably the, that's probably the big downside.

**Parallela:** Yeah. So I, uh, that was, that was a bit of a downside. I was, uh, living, uh, in Boston and flying down every week to, to DC. Oh, wow.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah.

**Parallela:** So I had, uh, you know, 50, 50 round trips per year. Uh, my gosh.

**Chris Gammell:** Yeah. That's, that's a lot.

**Parallela:** That's a lot. But it was, it was awesome. I wouldn't, I wouldn't trade it for anything. I think, uh, you know, the DARPA programs, you don't really know how, how impactful they're going to be probably for five to 10 years. Cause they are looking at them in the future. But I think there are some things we did there that will have an impact or even have an impact today. I mean, you look at like the open road project. Yeah.

**Chris Gammell:** Okay. Yeah. I would love to get a quick rundown of like the, cause I'm sure some of the things we've talked about in here and we didn't even know they were DARPA based projects. Yeah. Yeah.

**Parallela:** I mean, I think, I think probably open road is the most well-known one here. I mean, cause you know, they're, that's been used by the e-fabless and the Google shuttles and all of that. Right. And that was, that was a, that's a big, we've talked about that a lot. Yes. Yeah. Yeah.

**Chris Gammell:** Tim, Tim's come on and talked about that and Mohammed and yeah, just a lot of people. So, yeah.

**Parallela:** So yeah. So, I mean, the way I kind of structured my programs, uh, around things that would help reduce the barriers. So there was a program, uh, around chiplets and to try to chipletize design. Uh, there was a program on trying to make automated compilers. So kind of like Silicon compilers. So open road was part of that effort. And then it was a program to see if we can make hardware more like open source where we have an ecosystem, uh, of sharing and vetting. So that was posh. So it was posh ID and chips were the three big programs that I, I ran. Yeah. There was definitely some, some good outcomes from that.

**Chris Gammell:** That is awesome. What about the, um, what about the, so you mentioned chips and chips is also used in the chips act. Was it tied to that? I mean, like how much exposure was there around the funding sort of thing? I mean, like anything tied to that or not necessarily the chips act.

**Parallela:** Uh, that, that name is just name conflict to the, to the fourth degree. Right? Like chips, there's a chips alliance and there's the chips act in Europe, checks out in the U S but Hey, we were first.

**Chris Gammell:** Okay. Great. I mean, yeah, you have to imagine like what, what a politician is going to understand. Like, oh, chips. Yeah. I get chips. Yeah. Yeah.

**Parallela:** Let's call them that, you know, acronym name chips. It works.

**Chris Gammell:** Yep. Okay, cool. I mean, that, that is awesome. I, yeah. So I think many of the, so now, now that we're backdating all of this stuff that we've talked about on the show is because it's because of you. That's that. Thank you for that. That's been great. There's been a lot of great content on here and a lot of cool things that people are doing. I mean, I think, I think we're also seeing the trailing edge of it too. Like, I mean, so like, so Matt Venn's been on here a couple of times and just like seeing the shuttle runs and then the shuttle runs getting the MPW type things. And then Matt then splits them up for the, uh, whatever that other thing is, whatever Matt's open ASIC. Tiny tape out. Yeah. And then tiny tape on top of that. And it's just like, and now it's just becomes like an educational tool all the way back to like making it more and more accessible. So that's, that's gotta, that's gotta feel good. I mean, like that's, that's great.

**Parallela:** Yeah. Yeah. I mean, that's the way it's supposed to work, right? That's how software and sharing and development works. You stand on the, on the shoulders of others. Right. Yeah. And so, you know, we, we, we did, you know, we, I mean, in my part in this, of course, I didn't know technical work at DARPA. The only, my only responsibility was, was funding, selecting the people doing the work. Right. So.

**Chris Gammell:** Huh.

**Parallela:** No, the, you know, yeah. So, yeah. So just, I can take no credit for the technical aspects of open road. The only thing I did was get the program approved. Sure. That's great.

**Chris Gammell:** I mean, that's an important thing too, you know, that's. Yeah.

**Parallela:** But, but, but, you know, Andrew Kang at UC San Diego, right. Was the lead for that, what that effort, open road. And he's the one who made it happen. And, and his team, of course. Right.

**Chris Gammell:** Got it. What I'm really hearing here, Andreas, is I'm going to pick your brain after the show's over. I'm going to be like, I'm going to get a whole list of guests that I, I haven't talked to yet. And we're going to get more people on here talking about this stuff. Oh, for sure.

**Parallela:** Yeah. Please do.

**Chris Gammell:** Yeah. That'll be great. Okay. Yes. We found, we found the node. We found the, we found the connector node and we will, we will find other people through Andreas as well. Hmm. Okay. How can I make this an analogy to Andreas is the, the substrate that'll allow us to talk to many different people in different fields, like chiplets on a substrate. Is that, was that a good one? Is that a good transition there? That was pretty terrible, but let's talk about chiplets. Let's talk about zero ASIC and chiplets.

**Andreas Olofsson:** Yeah.

**Chris Gammell:** Cause one thing, one thing you did mention, I forget, Oh, I was thinking I was on the, I was on the treadmill this morning and I was listening and I was thinking, Oh, this is going to be so clever, but you were talking about one thing and I forgot it now, but like one thing around, it was around the unit economics. And it was like, it was something where chiplets just popped out as an, a natural thing. And I, and I thought, wow, that's what he's actually doing now in 20, 2015, you were talking about it, but now you're, you're proselytizing for chiplets and using them in the zero ASIC process project rather. So how did we get to where we are, I suppose, with chiplets?

**Parallela:** So how I started back in 2015 was the high cost of IP. So when you, you know, you go take something very valuable and this is not necessarily what other people are doing or what we should be doing, but back then, at least the cost of licensing a piece of IP was very expensive. I mean, we're talking millions of dollars. If you want to get a good CPU core or an IO interface memory or certes. Sure.

**Chris Gammell:** And, and you actually, you know, sorry. We talked to the Raspberry Pi folks last week or two weeks ago, rather, and they were talking about just the, you know, obviously they're a big operation, but they were also licensing a bunch of IP. And I thought that was, that was interesting too. Cause I didn't, I didn't realize that like the RP 2040 and all the new chips that they're doing custom in house are also, you know, just buying off the shelf IP for, for peripherals, but it's a common thing. And like you're saying expensive.

**Parallela:** Yeah. I mean, it's expensive because it's, it's hard to do, right? If, uh, if you say build versus buy, if I were to, uh, uh, go out and design a 30s PCI express 30s, I would have to probably hire 10 people and, uh, you know, spend two years doing it. So if you look at us salaries, you know, say $200,000 per engineer times 10 times two, you're you're, you're, you know, it takes you two years, you lost, lost time, and then you don't come out ahead in terms of cost. So it's just, it's just expensive. Uh, it's not like you're designing a UART or a spy controller, right? Where one person can hack it in a couple of weeks. It's it's, this is, this is hard stuff. So, so I think that that's where, you know, the IP is there to stay. That transition happened a long time ago. Like when I, when I started out at animal devices, we were designing all of our own IP, our own IO libraries, PLLs, memory compilers, standard cells from the transistor up. And we had big teams doing that. And then, you know, 20 years later, it's just gotten worse. You need even bigger teams and it's more expensive. So that's why the outsourcing that development to IP vendors makes sense.

**Chris Gammell:** Hmm.

**Parallela:** Yeah.

**Chris Gammell:** And, and so, well, you mentioned kind of like the scale differences there too. Does it still make sense to do like the, the lower level things or is it also from a standardization and just a speed thing? Cause like the last week they were talking about, or sorry, last show where the Raspberry Pi guys were doing it. They, they were grabbing a lot of these off the shelf, you know, spy, I squared C, whatever. So they could have made them, but is there like a standardization argument there too? Standardization around IP or. Yeah. Yeah. Just like using someone else's work. So you don't have to go and re-implement it. Like you said, you could go re-implement it, but just like an efficiency of, of work. Yeah.

**Parallela:** I mean, it would be more expensive to do it yourself. Sure. Yeah. Okay. Got it. So I think the, the pricing tends to be set in such a way that it's, it's not too high. Right. If they were to say, oh, I'm going to charge a hundred million dollars, right. For this IP, there'd be no market. People will go build it themselves. If they set it at zero, they make no money. So there's an optimal point in the middle there where it's incentivizes buying it versus building it. Got it. That makes sense.

**Chris Gammell:** Okay. Okay. So then one thing that I, so we've had, uh, Ming Zhang on the show talking about chiplets in the past. I think he's the only other chiplet person we've had on so far. And I, I think Z glue is no longer around, but I know Ming's still doing lots of cool stuff. The thing that popped out from that show that I remember is like process differences also were a big advantage with chiplets because it's like the thing you're going to put into your Bluetooth transceiver, the process you're going to use for that is going to be different than the analog part on your board is going to be different than the, you know, the crazy digital, uh, fanciness that's on your board too. Is that a big piece of it or is it more just the IP? It can be a big part. It depends on how you use it.

**Parallela:** So let's first go back and define the chiplet, right?

**Chris Gammell:** Sure. Okay. Yeah. You did, you did kind of hedge before you were like chiplet, whatever that means. Right. You, uh, seems like it's a, is a contentious term. Is that, is that part of the problem? Yeah.

**Parallela:** Cause, cause you, as you, as you mentioned right now, uh, you mentioned Z glue and I think the question is what is a chiplet, right? Is it just a, a silicon die that's small, right? Some people would say that I don't think that's a sufficient condition. Some people call chiplets these giant SOCs, uh, in a package, right? Like AMD and others. Right. So I would say a chiplet is a die with a IO interface that has very short reach that only goes inside the package. So it's designed for in package integration. That's a chiplet to me. Yeah. Is, uh, you know, it implies sort of a disaggregation of the chip. So you chip, you shadow the chip into chiplets, each one with a little specialized IO interface. That's to me is a chip. Cause that's kind of, maybe not the most elegant definition, but that's, that's the chiplet to me.

**Andreas Olofsson:** Okay.

**Chris Gammell:** The way, the way I had thought about it is kind of like, I kind of visualize, like if I have a PCB and it's got a bunch of. Like SOICs on it, QFNs, whatever. I'm kind of visualizing a chiplet as that, you know, set of QFNs that might be on a PCB. And then the substrate is actually the PCB itself. And it's just kind of like a shrunk down version of that is so like, is that a good, you know, like the function specific to.

**Parallela:** Some, some people would agree with you. I disagree. Right. Okay. So there's been this, uh, multi-chip modules for decades now. IBM had them back in the eighties where they literally would just take a bare silicon die, a bunch of them, put them on a, on an organic substrate or ceramic or something inside the package. And I would call that MCM. And that's basically a tiny PCB. Yeah. Right. Okay. Okay. So that's been around for a long time, but then, but they were just, you know, there was, it was just smaller. There was nothing different about the die itself. And, uh, and with chiplets, the idea is that we're going to actually co-design it so that it's those IO, IO drivers can only drive other chips that are within a few millimeters or a few, a few hundred microns. Right. So they're kind of like they're, they're, they're co, uh, co-designed or, you know, they're similar. Okay. Okay. Yeah. Right. Okay. As opposed to just taking a silicon die and repackaging it.

**Chris Gammell:** So what is the, what is the benefit then to not? So if you're going to have like, so we're going to have chiplet A and chiplet B and chiplet A, what let's make up functions for it. So chiplet A does the math functions and chiplet B does the, the memory handling or something like that, and they're going to be talking to each other designed to talk to one another over this bespoke bus with bespoke drivers that are locked together. Why not just smush them together in, in the silicon in the, sorry, in the, in the design going to the fab and making it one contiguous piece of silicon.

**Parallela:** Ah, so that, yeah. So that's what Moore's law, right? Everybody's been doing that for 50 years. Right. So just integrating on, on one chip and the, that's, that's the performance optimal version. Cause then you get like 13 layers of metal, the distances can probably be in the hundreds of microns. Yeah. And you know, each, each wire is like a hundred nanometer pitch, right? So the energy efficiency, the cost, the bandwidth, everything is awesome, but you get no modularity, right? You basically compile one function into one thing and it has zero reuse factor, right? Unless you can take that thing as is. And so, I mean, software, we have, you know, libraries and we have a concept of stacks and abstractions and, and you know, like you, you take Python, right? You've got dependencies and, and it goes very, very deep and you can do very modular design very quickly. You know, imagine if you had to like these statically compiled programs without any possible of, of linking in other libraries, it'd be pretty inefficient. Yeah. Yeah. In software. So in hardware, we, we have that equivalent. It's just stovepiped binary blobs, every chip. And so, yeah, the chip lets you get the modularity of, of software basically. Okay.

**Chris Gammell:** So the, the disconnect for me is I'm imagining again, like a chiplet being like a single function, you know, the things are meant to be right next to one another, then how do you actually connect them?

**Parallela:** Yeah. So that's the, that's the tricky part, right? So in, uh, when you're on chip, you use something like Axie or AXI, where it's this, uh, you know, there's actually streaming and, and memory mapped, uh, but the memory map abstraction is like, okay, you've got a read and a write, you get a, an address map. And, uh, then when you have a transaction, that's how you talk to other devices on the bus. And then, you know, then how is that done? It's usually done with a set of channels, which are, you know, parallel in fashion. You got, you know, read request, write request, you've got data coming back and acknowledges. And, and that's how, that's how communication is done on chip. Uh, but we're talking about hundreds and hundreds of wires here with just inverters and buffers driving it. When you want to drive on a board, if you're going to drive like GPIO signals, you know, you're, you're off by a factor of a thousand or 10,000 compared to the on chip, right? So you go, Hmm. Okay. Whatever worked on chip really doesn't work anymore. My environment's completely different. So I need to take a different approach. So, so usually on a board, if you're driving a very specific interface, like a memory, you might get away with, with driving things in parallel, but if you want to write, drive it distance fast, then you probably want to use a 30s and 30s are they're power hungry, the long latency. So now you've got other problems coming in. Yeah. So with chiplets in package, you can't, it's a new domain. It's not on chip where you got 13 layers at a hundred nanometer. It's not PCB where you got really long distances. So there's a new paradigm. So, yeah.

**Chris Gammell:** And that's what I'm getting at is like, is it, are the chiplets tiny pieces of silicon mounted to other pieces of silicon or are they mounted on a substrate or they mounted in free air with just dangling wires?

**Parallela:** No, it's, it's, there's some kind of connectivity. Okay. Usually some kind of bump with a solder cap on it. So they're soldered together. They're soldered together.

**Chris Gammell:** Really?

**Parallela:** Yep. Oh. So you can have, you know, there, there are many ways of doing this. I mean, there's a whole, whole field, right? You can have an organic substrate, which is sort of like a PCB.

**Chris Gammell:** Yeah.

**Parallela:** That you would solder these chiplets onto. And that's usually not that dense. It's not like silicon, right? So it's kind of like a miniaturized PCB. You could use a silicon passive interposer, which would be more like a silicon wafer, but just wiring, no active devices. And then you get better density. The type of bump pitches that we're talking about is on the order of like 55 or 45 microns. Usually if you're advanced and 110 micron, if you're not so advanced. And what size soldering iron do I use to solder those, to solder those bumps? Tiny, tiny ones. Yeah. Yeah. So, so the, I mean, it's, it's a reflow process usually, right? So you, you, you, you bond it, you very accurately bond the chiplets onto whatever interposer substrate you have. And then you use heat and or pressure to, to do the final bond.

**Chris Gammell:** Huh. And then, okay. So then, so now these things are connected in a variety of ways. What do you call the output of that? When you assemble them together?

**Parallela:** Yeah. So some people call them a system and package.

**Chris Gammell:** Yeah. Okay.

**Parallela:** That's, you know, if you come from the packaging industry, you probably call it system and package. I think some, you know, some, some larger vendors might just call it a chip.

**Andreas Olofsson:** Okay.

**Parallela:** You know, I think, you know, when people from a customer's perspective, you know, they don't really care how it was constructed. They care about what chips. And, and once you package together, what the customer sees is a plastic package or with the heat. Right. Exactly. Black blob. Right. With one millimeter pitch ball grid array underneath. Right. Right. Right. Right. So. Right.

**Chris Gammell:** I look at a one millimeter pitch ball grid array and I'm like, oh, that's so small. And then you look at a one millimeter pitch ball grid array and you're like, oh my God, that's massive. You know, it's just scale differences are great. It's, it's nuts. That's so, okay. And interesting. And then, so then what's this? So I've also heard some like system on module and I'm sure there's other, I'm sure there's umpteen at acronyms here, but is some another term or not a use?

**Parallela:** Yeah. So, so, so let me kind of, that's to, you know, to me, the step up after system and package. So you've got, you know, maybe a, it's basically a regular PCB with, with limited IO functionality. So, you know, you can imagine, you know, like for example, Raspberry Pi has a song for their processor. So instead of putting, you know, all the connectors, like a, you know, USB ethernet and everything, which takes up a lot of space and, and, uh, and maybe application or system specific, you, you focus on like, okay, how do you integrate Silicon devices into a nice abstraction? Right. You might want the, and, and, and, and take away the hard piece, right. Laying out a, a high speed DDR memory interface is always a hassle. So by creating a song, you can kind of create this coupled unit between the memory interface, memory device, and the CPU, and then have maybe a high speed connector to the, all the other stuff, right. The low speed, annoying stuff that sits on a, on a carrier. So that's a song to me.

**Chris Gammell:** Okay.

**Parallela:** That makes sense.

**Chris Gammell:** Well, let's talk about then. So zero ASIC is the company. Yeah. You haven't been in stealth, but you, you're, you said you've been talking to more people. Now I saw you on a couple of other podcasts and newsletters and things like that too. So, you know, you're, you're hitting all the very important things like the amp hour, I'm sure is a top of the list. Uh, what is, what are you going for them with zero ASIC? Obviously chiplets, but like, what is, what is the differentiator then?

**Parallela:** So, yeah. So, so I think we, we, we've done some things publicly. We had a, you know, we had the Silicon compiler project that we started two years ago and really even released two years ago that, but that wasn't our product. That was sort of a teaser. But now we, you know, two weeks ago, we came up with our, what we're actually want to do with details about our platform. And it's, it's all about chiplets. So, so like our business model is to, to go, you know, take system customers who want to build something. They would go up to our website and they would select from our portfolio of chiplets, uh, using this drag and drop GUI in the, in the web browser. And, uh, they select what they want and that's basically their ASIC and we, we assemble it for them.

**Chris Gammell:** Faster, cheaper, more flexible, that sort of thing. Huh? It's just like, uh, it's a, it's a drag and drop to, to have a custom functionality, that sort of idea.

**Parallela:** Yeah. Yeah. It's a, it's a block based ASIC builder, right? No code. I mean, think about it. Like even, you know, even we've talked about like open source ASICs or anything, you still have to wait for the ASICs to come back.

**Chris Gammell:** Right.

**Parallela:** Which is, uh, you know, it could be a year, it could be many months. Yeah. When you've got a, all the chips are prefabbed and even the package substrate is, is a prefab, you can assemble it in a few weeks. I mean, if you compare that to a PCB assembly house, if I've got the green PCB in, in, in stock and I've got all the devices in stock, I can probably build that up in 24 hours.

**Chris Gammell:** Right.

**Parallela:** Yep. But if I, you know, if I'm out of stock of one of the devices, then it could be six months.

**Chris Gammell:** Yep. That, uh, longer, longer during the chip shortage. I just, uh, interesting. Okay. And then you guys are leaning into the ASIC term a little heavily then, aren't you? I guess it is application specific, but it's, uh, I don't know. I feel like there's a new acronym needed and I know it's zero ASIC, but still ASIC. Yeah. ASIC is, uh, it feels like there'd be a, you know, a little quote fingers around it. Yeah.

**Parallela:** Well, I mean, in a, in a, in a way, I mean, it is, is the true ASIC, right? If a customer can, can dial up and say, I want to build this thing. And that thing that the building is a unique combination out of a billion possible combos, that's a pretty specific device they're building. So I think the term kind of fits.

**Chris Gammell:** I'm not worried about it. Like, you know, there's a big conversation here, but yeah, no, it is, it is interesting.

**Parallela:** I mean, it's, uh, it's, uh, you know, it's, it's a valid point. Uh, I, uh, coming up with a new term, uh, use the old term. People get confused. You come up with a new term, people get confused. So yeah, totally.

**Chris Gammell:** Totally. Totally. Okay. Interesting. So, uh, who, who, uh, of our listening audience right now, who would you think, oh yeah, they're, they're the ones that should use this. Who's your customer? We like customers with money. Ah, yes. I see you've done business before. Ha ha business.

**Parallela:** Uh, no, I, I think if you, if you look at realistically who would want to use this product, there are, you know, there are people out there designing systems who are perfectly happy with what's on the market today. Uh, you know, I mean, there's like literally thousands of great products in the market, FPJs, microcontrollers. And if that is good enough, then that's the right answer. So that's, that's not our market. I mean, it'd be silly to try to go and make somebody who's happy, happier. And at the top end, if people are only doing smartphones or, you know, they have infinite money, they're probably just going to go away and build an ASIC. They don't care about money.

**Chris Gammell:** It's around a thousand person design center, right? They, they're, they're already on the path. Yeah.

**Parallela:** And so, so, but, but in the middle, when you, you have people who don't have infinite money and they actually care about performance and they need something specialized, that's sort of our, our, our, our mark. And so, so I kind of like, if you look at some of those markets, I mean, the one that's funded us so far, aerospace and defense, that's a market that has high value applications, size, weight and power constrained, but actually don't have infinite money to do chips. I mean, it's actually very cost constrained. So, so that's on the engineering expenses.

**Chris Gammell:** I feel like I should make a joke here about, about military spending, but I, I don't have one at hand. So I'll just leave that be. Yeah, no, that makes sense. And so I am in the zeroasic.com slash emulation menu right now, because who doesn't love a live, live demo where someone's talking and clicking around. Uh, I do note a lot of ML blocks in there, uh, kind of, so that also kind of leads me to believe there would be a lot of that machine learning piece that, you know, maybe putting a, uh, putting a Jetson on board is not, is not, uh, is not practical, but you still need some kind of, uh, specialized algorithmic, uh, learning on your, on your device.

**Parallela:** Yeah. I mean, the CPU is just not going to be good enough.

**Chris Gammell:** Yeah.

**Parallela:** And so if you want to do anything that's, you know, massive matrix multiplication, uh, you need an accelerator on there and, you know, ML is just too ubiquitous to ignore. So yeah, ML is a core component.

**Chris Gammell:** Oh, I'm trying, Andreas. I'm trying. And, uh, yeah, it keeps, it keeps popping up.

**Parallela:** Yeah. So we, so, so the thing about chiplets is sort of like, you know, uh, if you can imagine having an infinite number of chiplets, obviously you can create almost anything. Right. And, and so the, the, the trick becomes what, how do you order all the functions you might want to do because there's only so much time and money to do it. So we kind of, you know, say, okay, here's the, all the tips we want to do. And then we're going to start with the most important ones first. So the most important one we did was a CPU. So we did a quad core risk five CPU. And then the second one after that was the FPGA. So we, we, we bootstrapped an FPGA architecture. And then the third one was the, was the machine learning.

**Chris Gammell:** Um, I have to say, I'm a, I'm a bit surprised from, you know, the IP discussion we said earlier. I, I'm surprised that you are building these things. I kind of, I kind of assumed that it would be kind of off the shelf. You buying chiplets from someone else, but I guess like you're saying they have to be, you said they, these are specialized enough because of the, uh, the interface between them. Well, yeah. Is that why you're building them yourself?

**Parallela:** Exactly. So there are no chiplets. There are chips out there. Yeah. Okay.

**Chris Gammell:** So back, back, back to terminology here. Okay. Yes. Makes sense.

**Parallela:** Well, yeah. And really like, so these, so if you, if you were to buy an off the shelf FPGA, first of all, it would become packaged, right? Not, not a die. And so.

**Chris Gammell:** I think you could buy die, like dies of FPGAs. Is that, is that a bad assumption on my part?

**Parallela:** Uh, no, it's a, it's a, it's true that you can buy a die, but it's not generally available. Okay. Yeah. I couldn't buy one, but maybe you could. Yeah. With a fairly high price. Sure. Yeah. Yeah. Yeah. It would be like a, you would have to sign a contract that would be pretty significant. Yeah.

**Chris Gammell:** Yeah. Okay. All right. So in the short term, zero ASIC is making these as well to just, I mean, I can imagine you're kind of bootstrapping the market as well, right? You're saying like, well, we have to have these things available. So we'll make the first ones. And then maybe in the future, there could be a marketplace type play where other people might make IP or other vendors might be like, yeah, we can make it compatible or lower our minimums. If you're going through zero ASIC, that sort of thing. Once you've captured the entire market and become the next arm or NVIDIA, right?

**Parallela:** Well, so, so we, I mean, so one of the things we had to do was, uh, I mean, we, we really are trying to bootstrap an ecosystem here.

**Chris Gammell:** Yeah.

**Parallela:** Yeah.

**Chris Gammell:** Not, not a small task. Yeah.

**Parallela:** And so, uh, so for example, one of the things we had to come up with was this chiplet standard. Uh, what is that going to be? Okay. And, uh, so, cause otherwise the chiplets have to be able to talk to each other and, and Arm did the same thing with, with Axie or an AMBA. They had a processor. They thought it was a good idea for that processor to be able to talk to other IP blocks. So they came up with AMBA and that's been incredibly successful in, uh, in the SOC world. And in the, in the chiplet world, you know, there's been lots of efforts to date. So when I was at DARPA, there was this AIB out of Intel. So the Stratix 10 had this AIB interface on it. And, uh, uh, as part of the chips program, they open sourced it as part, not part of the chips Alliance, but it wasn't sufficient. It only had an electrical interface. It didn't have a protocol defined and it didn't have a pin out. So it wasn't like a Lego block. Hmm. And so that was, so that was, uh, that falls short. So with, uh, what we're trying to do here is a full stack chiplet interface. So like a JEDEC type, you know, all the pins are defined, locations are defined, you know, abstraction layer, electrical, everything. Right. So it's just plug and play like USB or PCI express.

**Chris Gammell:** Right. Well, and I, I mean, as in any standard too, like it honestly doesn't matter until the second person joins in. Right. Yep. Yeah. That's, uh, you can, you know, I could make a standard for myself. That's like, you know, the PCB standard and I've, you know, I made pin outs that are standard, but you know, I'm not, uh, I'm not Arduino and I'm not, uh, I'm not Raspberry Pi. So nobody cares about the 25 pin connector layout that I did. Like that's just the Chris Gammell standards still like, okay. It's the second person that cares about it or the ecosystem that drives it. Right.

**Parallela:** Yeah. And it's, it's really, really hard to come up with a successful standard and you can, you can kind of, you can get in a room and talk about a standard and that usually takes a very long time and it's hard to get right because you have too many people talking and too many opinions. A lot of cooks. Yeah. And, uh, or, you know, if you're very successful like Arduino or, you know, with USB or PC express, you can have one big company just build something and it becomes the de facto standard.

**Chris Gammell:** Yeah. I, I squared C, right. I mean, that's a, what Phillips was them. Uh, yeah. So yeah, it's, it's good to be King, you know, like that's the way to do it. Right. Yeah. So, yeah, that's.

**Parallela:** So we, so, but we, we, so we decided we're gonna, we're gonna go for it. We're gonna create, uh, we're gonna work on a standard cause technically it was, uh, we had the right people to, with the skills to review it in house. So, uh, so we did it, we built chips with it and then we're gonna open it up in a couple of weeks time. Yeah. So, and then, and then, like you said, we'll see, maybe we'll be alone standing with our standard. Yeah.

**Chris Gammell:** I mean, you literally can't know it until you try it. So like, it's good that you're, I mean, you, you gotta take a shot. Right. I mean, the, I think it also comes down to like strategy at the next step with all apologies to community driven efforts. Like, you know, like I feel like a lot of people fall into the, the, the, the, the hoping the community is going to drive a lot of that stuff, but it's really, it's going to be like whoever's the most driven towards getting this thing done. And sometimes it does work out that it's community based things, but it's like, if you can have other people joining in on the standard because they have a business reason as well, or, you know, just a, a shared goal, I guess maybe shared goal is the better way to say it. That's all often. I think the thing is going to drive the highest amount of adoption.

**Parallela:** Yeah. I mean, uh, it's softer standards comes down to contribution. It's, it's time from the right people. And, uh, yeah. Right. On that topic, that's sort of a, uh, sore, sore point for me. Uh, a lot of people make comparisons between software and hardware and like, let's, let's just do in hardware what we did in software. And one of the fundamental differences is that the hardware community is one thousandth the size, right. It was software. Yeah. And so, uh, so you're not going to have, you know, even one contributor in a certain

**Chris Gammell:** field, right. I know this pain, uh, personally, I know this pain personally where like, I look at like, uh, I was looking at this tool that had like this amazing documentation and like thousands of commits on GitHub and whatever. And then I like looked at like, you know, I was comparing it to the company I work for and trying to get people to like, again, jump in on hardware stuff and, and, you know, community based things. And like, literally it was installing, you know, like you like copy and paste a JavaScript tag into your, whatever you're doing. And it's like, you're, you're there, you're in your, you're a contributor. You're part of it. Like, and once that works for hardware, I'm all sign me up because like that, that, that's just like the, the startup time to get up and going and contributing to something is just, it feels massive. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Hopefully, hopefully a little easier for you, for you with, you know, maybe with Verilog, it's a little bit better, right. Uh, you know, like, or some digital tools around, or, you know, like you're in the hardware realm, but there are some software, there is some software tooling that hopefully people can contribute with. I would hope.

**Parallela:** Yeah. Yeah. No, I mean, I mean the, I w I would say the, the projects that we've run and I've run and quite a few and seen quite a few, you know, you're, you're very lucky if you can get an external contributor, uh, has to be the environment just has to be like, just perfect. That person has to be excellent, right. Have the technical skills in a very niche field and have the time. And usually time means they have a sponsor like, uh, you know, university or company or government entity that is willing to let that person contribute time out of the workday. Cause if it's on holidays and weekends, it's tough. Right.

**Chris Gammell:** Yeah. Right. Right. And, and then you, as the, the company being contributed to, it's like, it's like you, uh, you appreciate that, but you can't count on it either. Right. So it's also like, you know, trying to estimate when something's going to be pushed out and yeah. Yeah. I've seen, I've seen this with the key cat project as well. Right. I mean, like there's been so many great contributors and then it really started to accelerate once people were, like you said, sponsored either by companies or, or funding, whatever. So yeah, it's, it's tough. It's tough. It's a tough, tough problem to have.

**Parallela:** It's fun. I, I really, I mean, like I, I really enjoy the community. We, I gave a presentation at, um, at latch up, which is the, the, the, back in, uh, in, uh, in the spring. And it's just, just a great, great community. Just fun. Um, yeah, very, very friendly.

**Chris Gammell:** It is very interesting to hear people that are interested in, in custom Silicon as well, because they, they come from areas that I wouldn't have expected. I think some of it, I'm not sure what is the driving force on all of it. Uh, but, but it, it does seem like there's, uh, you know, backgrounds and different companies people work for, and I'm not sure what is the driving force. I mean, do you have a, an idea on where, what is driving people to, to get into the, into the space maybe, maybe like at latch up?

**Parallela:** Yeah. I, I think it's, I think it's personal passion. If I, that's absolutely the thread going through, uh, everybody there. They, uh, I think people want to make a difference and they, uh, it's like the, the, the true, like, let's, uh, I'm working on something cool. Let me share it. I want to see it used, right? I don't want to just do it for the sake of earning a salary or I don't know, for my own enjoyment, right? I enjoy it, but I want to see it used, make a difference. I think it's pretty pure.

**Chris Gammell:** That's great. That's really great. Cool. Well, uh, you have, so again, I'm on the zero asic.com slash emulation page. I do recommend people check this out. What else, what else should people check out on the site? If they're like, you know, so they're hearing this, they're like, oh, this actually might be a good fit for, for me. Like where, where do you expect, you know, so like, could I go and click a button to order this right now? Or is it, what is, what is the output of this? I guess. So, yeah.

**Parallela:** So, so, so what you can do, right. Is you can, you can press the emulate button and actually run a, you know, I mean, this is kind of mind blowing, right? You know, those devices that we have, the, the chiplets that you can select the ML, the AI, the FPGA and the CPU. Those are actual, you know, RTL of the, of the chips that we've designed. So when, when you do emulate those, those designs get sent up to AWS to their FPGA instances. Really? Bitstreams get loaded up and then, you know, you get a terminal coming back that will let you interact in real time with an ASIC that you basically configured real time, right? Three minutes, right? So you like select the blocks. We should have led with this Andreas. That is so cool. That is, yeah, that is really, really cool. I mean, you think about like that's, there's like a lot of moving pieces there. I, you know, it's just, it's really incredible team, but work by the team here with a lot of tech underneath.

**Chris Gammell:** Huh.

**Parallela:** And so the, the idea here is that when you think about how, like how, how different that is, right. When you buy a chip from, from big company, right. You're basically buying a data sheet. Yeah. Right. You go up to DigiKey or Mouser, right. And you, you search the part you want and they give you a data sheet and say it's 10 bucks and they ship you a part. You have, you know, you have no idea what's going on underneath. Right. And you have no proof that it's actually doing what you're buying, except when you put it on the board, right. And it's actually executing. But here, the idea is that you can actually, you know, get the ground truth, the RTL code of the data sheet and run code on that in the cloud before you get the chip back.

**Chris Gammell:** That is really cool. Yeah. I just got a Linux terminal. Mine's mine is emulating. So I'm, I'm, I'm up and running in the amount of time from the click. So that is, wow. That is super cool. How much is it, I mean, hosting costs for that sort of thing? Does that, is that a, is that a big chunk of, uh, you're just letting people spin up AWS servers for you?

**Parallela:** Is that, uh, we, we, we have a, we have a hard limit on our budget there, but basically, yeah, we're spinning up servers that are like a buck to 10 bucks a minute. Sorry, an hour, an hour.

**Chris Gammell:** Oh, okay. That's yeah.

**Chris Gammell:** I mean, it'll add up too. If like, if you don't have the auto shutdown type of things, uh, but, uh,

**Parallela:** no, we, we, we do, right. We have, but, uh, you know, so if you imagine like if it's a dollar an hour, right. You give somebody 25 credits, you just gave somebody $25.

**Chris Gammell:** Yeah. Yeah. The cost of acquisition. So, uh, yeah.

**Parallela:** So, but it's, it's okay. We know we want to, we want to show it off. Right. And it is a cost of sales, but, uh, I mean, cloud is amazing, right? It's, uh, if you want to reach 10,000 people, you, you can't do that with a Salesforce of 10,000 people, right? I mean, yeah. Unless each customer is like a million dollars. So this is a way of, uh, reaching like as many people as possible.

**Chris Gammell:** Yeah. I mean, and, and immediately getting them into it too, right? That's kind of like what I was saying about dropping in a, a JavaScript thing. Like the sooner you can get someone like actively trying something. As long as they know what they're doing, which I do not currently, uh, then you can like get, like get the dopamine hits as fast as possible as well. And, uh, I mean, this is cool just that it is booting up the, the whole, the whole thing. And I can, I can see it here. If I knew it was actually going on under the hood, I would, if I could actually use this in a appreciable way with like the ML blocks that are designed into this one, that would be even cooler. So I, I need to, uh, need to learn more about how to use this, but I'll click shut down for now. So saving you money, I will save you some money there. Yeah. So, and there are, I mean, there are other things in here as well. So it says there's a, there's a pre-trained model on the ML chiplet as well. Yeah. Yeah. Yeah.

**Parallela:** So you can, you know, you can actually go in and, uh, you know, upload an image, right? You know, try, try something. Uh, like I, I did my, my son is a, is a big Corgi fan, right? So, uh, dog breed. Yeah. And so I uploaded a Corgi image, right? And it ran through the, uh, the detection and it's like, oh, this is a, a dingo. Well, dog is dogish, you know, It's not perfect, but Hey, we didn't, we didn't do that part of the work. Right. We just did the hardware. This is not a hardware problem. This is a, uh, a model problem. So it wasn't trained on Corgis, I guess.

**Chris Gammell:** Got it. Got it. Yeah. As long as you're not introducing a dingo to another dingo and one of them is actually a Corgi, that would, that would be a messy output. But, um, otherwise I think, I think, I think it's safe. Yeah. That the, the benefits of simulation, I suppose.

**Parallela:** And I mean, and the, and the really cool part about this is that you, you get a terminal into the risk five processor.

**Chris Gammell:** Yeah.

**Parallela:** With, with an internet connection. And so people can, you know, pip install, get clone, whatever they want to start hacking away at it.

**Chris Gammell:** Yeah. Is it running, is running Linux by default? Yeah. We use a Yocto. Yocto. Cool. Yeah. I guess it makes sense if you're. So then you, you have to dynamically configure based on the chiplet or is it like enough of a standardized interface? Like all of them have to have a CPU. So you're at least have that as the Yocto input.

**Parallela:** Yeah. Yeah. So, so we kind of, we made our life a little bit easier by always having a risk five processor running there. Got it. So we have that as a base, but then the other chiplets, that's where we have the pretty cool auto device tree configuration. Right. So that we can actually, you know, basically build everything on the fly for whatever configuration people put in.

**Chris Gammell:** Yeah. That is, that is very cool. And then again, like thinking about how you'd expect people to utilize this sort of thing. So they could try it out. They can get in there, try out the ML models and things like that. The Verilog is not available or it is available. I'm not sure. Actually. Yeah. It wouldn't be able to replicate it locally. Yeah.

**Parallela:** The Verilog is not open source. Okay. Except for the libraries that we use that are open source. Right. So we, but, but yeah, the chiplets themselves, right. That's what we're going to be shipping. So at the end of the day, you know, this model we have, people play around with it, right. They drag and drop their, their components as they want. They test it out by logging into it and running their own workload. And then eventually, you know, once we're open for business, we'll have a buy button where people can literally order the device and we'll ship it to them.

**Chris Gammell:** And that'll be like a couple of weeks versus six month tape out sort of thing. Yeah, exactly. Yeah. Wow. That is very, very cool. As we get towards the end here, I suppose we should call out the career opportunities page on your site as well, because I'm sure a lot of people would be interested in working in this sort of thing.

**Parallela:** Definitely. You know, anybody's interested should reach out. We've got, got an amazing team right now. Yeah. It's, it's the best team I've ever worked with.

**Chris Gammell:** Right. All, all based in Boston or all remote? How does that work?

**Parallela:** No, all over. We've got, most people are in Boston, some people in California. We've got, you know, Canada represented, Sweden, Ireland, UK. So we're, we're pretty spread out.

**Chris Gammell:** That's great. Yeah. That's, that is the modern, the modern dream to be able to work, work on hardware all over the place. But I mean, if you can just get straight to a, I'm sure the tooling is even cooler. If you're, you're on the inside, you can get to, you don't have to go through the web browser to get to the configurable AWS terminal. You just get to go straight in. I bet you get, I bet you get SSH keys when you join. Yeah.

**Parallela:** Yeah. We, we, we do try to, to dog food as much as we can. Right. So we have any project that we have that's public. We try to use the way the public would use it. So, so like for our, our chip tape outs, this is another project, the Silicon compiler for all the chip tape outs we do. We use Silicon compiler, for example, which is also available as an open source repo. Oh, that was the thing you mentioned you released two years ago, right? Yeah. Yeah. Yeah. So that's the one that's, you know, basically, you know, Python based chip design. You do a pip install Silicon compiler and then you're good to go. Awesome.

**Chris Gammell:** Okay. Just as a quick callback. So I had asked earlier about the types of interconnect and you do have your own e-fabric active interposer. That's, that is how you're actually making this all happen. So, so it's kind of a customized, you know, we call it a breadboard somewhere I saw.

**Parallela:** Yeah. So it's a, that's a good analogy, right? It's a, it's a fixed grid connection device. And so you can, you can take these chiplets, these, we call them e-bricks. And then you can basically have a finite number of places to put those on like a grid. So the, uh, these e-fabrics come in small, medium, large, and extra large. And you would, uh, you know, pick the device that is suitable for your market, right? Or your application. The bigger, the bigger they are, the more expensive they are. Sure. And, uh, and so if you take, for example, something with a, a four by four grid on it, right, you have 16 locations to put your, your, your bricks. I'm not going to use that word that starts with L because I don't want to get in trouble.

**Chris Gammell:** I was going to say, yeah, I made a joke about not using the term ASIC, but I was worried the Danes might come after your head if you started violating trademark on bricks.

**Parallela:** No, I, I, I'm sorry.

**Chris Gammell:** I, I'm willing to die on that hill. Bricks is. Bricks is okay. Lego is not. Yeah. Okay. I said it. I said it. There's Chris saying it. Not, not them. Yeah. It's dangerous, right? I mean, it's such a, such a good example, right? But, uh, yeah. Yeah. Yeah.

**Parallela:** I, I, I, I, I've been, I've been tempted, but I'm going to stay away from that.

**Chris Gammell:** You know, what you should do is you should offer them a reduced price on a custom silicon to put into their Lego bricks, you know, cause they do electronics now too. And then boom, you know, a little, little cross cross branding. And, uh, and maybe, maybe you'll be able to put exactly Lego, Lego on your site once. They'll be like, yeah, you can use it once as long as you give us free silicon. Yeah. That's cool. So, yeah.

**Parallela:** So, yeah. So the, like, uh, like a decent, one of these breadboards, right? 16 sites and you put your bricks on top of there and that's sort of how it works.

**Chris Gammell:** Cool. Cool. And that, and that's those, those, uh, solder droplets you kind of talked about before. Those would then line up with a lot of this as well, right?

**Parallela:** Yeah. Those solder also sit between the e-fabric and the bricks themselves.

**Chris Gammell:** Got it. Okay, cool. Yeah, that's great. That's great. And, and then the, that's then also the standard that you mentioned defining would be how to make, so if I, if Chris Gammell decided to go and make my own chiplet that I wanted to put into some future marketplace type of thing, it would have to match that standard. Is that, is that a fair assumption? Yeah.

**Parallela:** Yeah. So for example, right. The, our, our standard relies on a two millimeter pitch. And so, uh, your chip or a chiplet would need to be two by two millimeters or a multiple thereof.

**Chris Gammell:** I mean, we're in the U S so shouldn't it be 2.54 millimeters? Sorry. Bad joke. Bad joke. I don't, I'd never do that. That would be terrible. You'd be wrong. I know it would be wrong. And also I feel like that would be like a good, like April fool's joke. That would be like, you know, we're going to switch and switch to 2.54 to be. Yeah. Anyways. It would be. Yeah. Silly. Well, Andreas, thank you for coming back and telling us about this stuff. You, uh, you have had a very interesting, uh, journey to where you are now. And I can only imagine where, where all this stuff is going with zero ASIC. Uh, I'm, I'm hoping it does get to the level of, of the arm and the, uh, and the NVIDIAs of the world, just because it's going to enable low cost and faster, faster iteration in the technology space.

**Parallela:** Yeah. We're going to, we're definitely going to keep trying.

**Chris Gammell:** Great. Great. Well, people should check out zeroASIC.com and, uh, we'll ask Andreas back here in eight years or less at least. Thanks for being here today. Thanks, Chris.

**Speaker ?:** Bye. Bye. administered administered administered
