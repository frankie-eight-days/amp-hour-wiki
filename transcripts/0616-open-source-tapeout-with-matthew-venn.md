---
episode: 616
title: Open Source Tapeout with Matthew Venn
url: https://theamphour.com/616-open-source-tapeout-with-matthew-venn/
---

**Matthew Venn:** This is The Amp Hour Podcast. Released January 22nd, 2023. Episode 616. Open Source Tape Out with Matthew Venn.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Matt Venn. And these days I'm mostly focusing on open source EDA.

**Matthew Venn:** Silly whiz. Silly whiz. I want to do the silly whiz. I love the silly whiz sound. Well, we'll get into that, of course. Welcome back, Matt. You were last on the show in 2019 at Supercon.

**Chris Gammell:** Yeah.

**Matthew Venn:** I guess that would be episode 467.

**Chris Gammell:** That's right.

**Matthew Venn:** We were talking about different things around verification.

**Chris Gammell:** Yeah, I think that one was about formal verification. And I'm still involved. Now the company is called EOSYS HQ.

**Matthew Venn:** Right. Exactly. So let's... Well, people probably have seen you around for your iconic hat, if nothing else, which has migrated off just your head, but also your different things. Maybe people saw you at Supercon this past year, 2022, rocking a silicon wafer around your neck as well. Yeah. So really blinging it. But I'd say you're representing a lot of the interesting new developments in accessible silicon. So what's the latest? There's a small task. Just give us a rundown of the entire industry. Yeah, yeah. Two minutes.

**Chris Gammell:** Okay. Well, the latest shuttle that was taped out on the Google-sponsored open-source MPW, multi-project wafer, was MPW-8. And MPW-9 is going to tape out in April. And the first Global Foundry... So that Global Foundry is 180. It's the second open-source PDK. And that taped out in... I think that was November last year. So that was new. That was quite a big deal. And this year, we're expecting another two open-source PDKs.

**Matthew Venn:** Oh, wow.

**Chris Gammell:** Another one from Skywater, Sky90. Wow.

**Matthew Venn:** Yeah.

**Chris Gammell:** More dense, a lot smaller. Yeah. So it's like one of those things where, because everything is kind of two-dimensional, you get the square law. So if you half the size, you actually get four times more density. Yep. And then there's also the first European open-source PDK coming from IHP. And I'm hoping to tape out on that as well.

**Matthew Venn:** Wow.

**Chris Gammell:** Yeah.

**Matthew Venn:** Awesome. Awesome. Well, that's a lot of stuff going on there. So we've had a lot of people on the show in the past, including yourself, that have talked about kind of custom silicon and the progress of accessibility of the silicon process to kind of normies. And maybe, could you give us a little idea of like, why is this happening? Right? You said this is Shuttle 9, MPW, multi- Project. Project Wafer. Yeah. Nine. So there's been nine kind of like group orders there, kind of like Osh Park for silicon. Yeah. But why is this happening? Why is there more availability here? Yeah.

**Chris Gammell:** It's a really good question. I think, I mean, open-source EDA and EDA4, I mean, I think, you know, especially you're used to KiCad, which I think we can put in the EDA category.

**Matthew Venn:** Sure. Yeah.

**Chris Gammell:** But we also have EDA for FPGAs and we have EDA for silicon for ASICs as well, which share quite a lot in common. And, you know, there's like the very early tools like Magic, for example, which started out 40 years ago and was in use then and is still in use now. A lot of the open-source tools were kind of bought out or kind of merged into the kind of the main big three proprietary companies now. But it's been going on all the time. I think we've, the main, the big reason we've seen a uptick recently is because of the Google sponsoring the lottery shuttle.

**Matthew Venn:** Got it. Okay.

**Chris Gammell:** So just for people who don't know what the shuttle is or an NPW, it's basically like even an old process like Sky 130, which is about 20 years old, the mask cost is about $200,000. So you have to put this huge amount of money. And then once you've done that, then the cost per wafer and the cost per die is much lower.

**Matthew Venn:** So Google's paying that, they're paying that mask cost and then everything you're paying kind of the subsequent cost. And the wafer cost, yeah.

**Chris Gammell:** Oh, they're paying for everything.

**Matthew Venn:** Yeah.

**Chris Gammell:** All you need to do is submit a design that is open-source and then you get a ticket to the lottery.

**Matthew Venn:** Got it. So they're basically Willy Wonka-ing the silicon process. Yeah.

**Chris Gammell:** Yeah. And yeah, so we're up to nine on Sky 130 and we've had the first GF 180 and that's all being covered by Google and Tim Ansell is driving that. And he's already been on the podcast a few times, I think. 501 might have been the last one.

**Matthew Venn:** Mm-hmm. Yeah. Yeah. He's due to come back, but we're talking to you instead. Come on. Yeah. Matt over to Tim. No, I'm just kidding. Tim is supposed to come back on. Tim's got a lot of things going on and this is one of the many things he drives. Yeah.

**Chris Gammell:** Yeah. It's great. Yeah. So I was kind of in the right place at the right time because I had a fair amount of FPGA experience.

**Matthew Venn:** Mm-hmm.

**Chris Gammell:** I saw Tim Edwards from EFABLUS presenting an open source chip that was using the Pico RV32 RISC-V processor designed by Claire Wolf, who you've also had on a few times. And I just, I had no idea that they were open source chip design tools. So I took one of my FPGA designs and ran it through and got the fancy GDS files out the end. Those are the kind of, if you're familiar with PCBs, they're like the Gerber file equivalent.

**Matthew Venn:** The Gerbers of PCBs. Yep. Yeah. For foundries, for chip factories. Are they as old and stodgy as Gerbers are? Yeah.

**Chris Gammell:** I think probably more so.

**Matthew Venn:** Well, I don't know. Yeah.

**Chris Gammell:** I had one of the people I met at Supercon, a guy I know called Dan Burke, who was like involved in the Valley back in the day. And I was talking to him about the, where does the terminology tape out come from? Because there's like a bit of, what do you call it when people disagree on that meaning? Debate. Bit of a debate. Yeah. Some people say it's because you used to put the designs on magnetic tapes and then you take the tapes out to the mask factory.

**Matthew Venn:** Oh, interesting.

**Chris Gammell:** And other people are like, no, no, we used to use crepe tape, like actual, for doing PCBs.

**Matthew Venn:** On like the big light tables, right? Yeah. And PCBs. That's like the iconic photos of like Weidler and leaning over these huge light tables and

**Chris Gammell:** they actually were like the masks. Yeah. And that came from PCB layout technology and PCB, all of that stuff came way before magnetic tape. So tape out really comes from carrying your masks out and the masks have been made with crepe tape that then moved on to Ruby lift. Anyway, I did a little interview with Dan Burke and put it on my YouTube channel. So if you're interested to hear what someone who was there.

**Matthew Venn:** Immediately link people to the YouTube channel. What is it? It's Zero to ASIC. That's Zero to ASIC course.

**Chris Gammell:** Yeah.

**Matthew Venn:** Zero to ASIC course.

**Chris Gammell:** Yeah. Yeah. I'm careful to make it different. There's a company called Zero ASIC, which has got nothing to do with the Zero to ASIC course. Got it. Got to be careful there. Although. Right. They do a lot of good stuff. They're in the same domain. Oh, interesting. One of their main things is a, another RTL to GDS flow. So you put in your design and outcomes to GDS ready to send to the factory.

**Matthew Venn:** Yeah. That's awesome. So it sounds like kind of a confluence of the evolution of these open source tools. It sounds like the Google sponsoring the shuttle runs and then also driving some of the open PDKs as well. Because I remember when Tim was on the show, he was talking about the Skywater thing. And I didn't really, at the time, I didn't really grok what the deal was. I was like, oh, well, can't anyone get access to these PDKs? And the answer was not, not really. You used to work in a, in a foundry, didn't you? I worked at, not a foundry at, at Samsung. I used to work at Samsung, but I never had any exposure to the masks or any of the design. I was, I was a, basically just a process engineer. So I just worked in the fab.

**Chris Gammell:** Yeah. Which is cool when it sounds right, but very different. All of that stuff they don't want to share, you know, so they do this huge amount of R&D development on the next process. And then that is part of their intellectual property and their advantage in the market. So they want to keep that secret, but they still need to let people design chips for their process. So traditionally you have to sign an NDA, then you get given the PDK. Right.

**Matthew Venn:** And because all the, we will sue the crap out of you if you, if you let this loose kind of thing.

**Chris Gammell:** Right. And that's like one of the key things about making things like lowering the barrier to entry and being able to do things like training or like online training. Right. If you have to make everybody on the training course sign an NDA before they can even start using the tools, that's, that's not, that's not a great start.

**Matthew Venn:** Yep. Yep. And I mean, it sounds like it's also having this kind of domino effect. I'm sure that Tim is behind the scenes and others as well, like encouraging other fabs to do the same, but I could see it as a, you know, other people look at Skywater and I'm sure they're like, oh, look, more business, more marketing, all of that kind of, you know, like open source as marketing is kind of an interesting thing as well. And now, like you said, there's two, you said global foundries, which is a really big name doing it at 180. And then what was the, the, the European one? IHP. IHP.

**Chris Gammell:** Okay. Yeah. There's like a small research fab in Germany, but yeah, I've been talking to them for a while. They're really good people. I'm actually hoping to go and visit them soon to make some videos about the process. Oh, that'd be awesome.

**Matthew Venn:** Yeah. I'd love to see that. Yeah. It does seem like there's one, one additional piece in here that you did mention that I'd like to also add to the, to the list of four, four things influencing this, which would be the rise of risk five. I feel like that, that is having kind of unknown, untold, unbelievable effects on the industry as well. Like I'm, I'm just continually amazed to see what's happening with the risk five.

**Chris Gammell:** Yeah. Yeah. And I think, um, one of the things that we'll see coming out of this is things like SOC builders, something like LightX that lets you kind of snap together some bits and pieces and then be able to run it on an FPGA or tape it out. Like, can you, you can imagine like a website with a bunch of toggle switches down the side and you're like, yeah, I want, you know, eight kilobytes of SRAM and I want eight A to Ds and four serial ports, a dual core risk five. And then you press a button that says, it's going to be like $1 apart in minimum order quantity of 10,000 or something.

**Matthew Venn:** Well, and, and we had, um, oh, I should look up his name. Um, the chiplets guy, I'm going to look him up real quick, but they kind of were talking about that where it was kind of like a click. Yeah. That, the company is, has unfortunately not, not continued on, but.

**Chris Gammell:** That whole thing is definitely going to be a big deal though. And I think also like one of the things people say is like, what is the point of these, of these open source PDKs are so old? What can you do with them? Because everyone is focused at the absolute bleeding edge and the latest thing out of TSMC. Yeah. But, you know, you worked in Samsung, they have a very different process for memory. And that is a completely different process. It's optimized very differently for something like logic. And if you're doing analog or radio, then you also want a different process. And analog and radio mix signal works better at larger nodes. Analog designers have told me, I'm not an analog designer, but they've told me they prefer working. Yeah.

**Matthew Venn:** Something about capacitance and stuff like that. Yeah. Yeah.

**Chris Gammell:** Or just like, you know, when, when FinFET was introduced, it was introduced because they, their transistors were getting so small. They were having like weird leakage effects. Yeah. And that's not something you want as an analog designer.

**Matthew Venn:** Yep.

**Chris Gammell:** Yeah. So maybe a chiplet where you have, you know, some modern process from TSMC or anywhere else for your logic. Then you've got some, some other process for your memory, but then you've got something else that could be a much older, even open source process for your radio.

**Matthew Venn:** Yeah. Right. Right. Right. Yeah. And, and, and they're on the shelf and they're tested as well. I think that's the, that's the key thing there. Yeah. And it was Ming, Ming Zhang who's on the show talking about Zglue. That was the chiplet thing.

**Chris Gammell:** Yeah. I remember that episode. Really cool idea though.

**Matthew Venn:** That's great. Yeah.

**Chris Gammell:** FPGA fabric that you can just drop your chiplets on top of.

**Matthew Venn:** Yeah, exactly. And I think it was like the, the automated assembly, not the assembly, but the kind of the layout between the chip puts as well. So then you have kind of low, low impedance connections between the, the various elements.

**Chris Gammell:** Yeah. He even mentioned there was like, you have special wires just for radio.

**Matthew Venn:** Yep.

**Chris Gammell:** Yep.

**Matthew Venn:** One of the things that I wanted to, you know, kind of talk about here is because like, so like you mentioned the, the, the, the, the, the chooser tool, I forget what you called it, but like the config. It's like a configurator style, like web tool. Yeah.

**Chris Gammell:** I don't have a name for it, but I've been thinking I should mock something up like that.

**Matthew Venn:** That would be a great idea. I think the, the thing that I always come to there though, is the, is the volume problem, right? This, this always kind of like everything in the chip industry, every, every industry really is like customization is great, but the, the volume is really what's going to smack you in the face. I feel like, and so when I look at like the, the open PDKs and these tools and really just the thought of, you know, just getting the activation energy to even try this out. I think to myself, well, I don't have anything that needs the volume here. So why should I build something custom? It's better for me to spend my time going and like learning what's in the marketplace already.

**Chris Gammell:** Yeah.

**Matthew Venn:** I think that as an assumption is changing, but I'd love to hear like how you see people using this and what is their motivation to kind of, to start this process, to get that activation energy. Because I think a lot of the people listening would, would be on the cusp of that, right? They'd be like, oh yeah, that would be cool. But like, there might be a reason that they should just try it.

**Chris Gammell:** Well, maybe we can split that up into two things. Cause the first one is, is like, yeah, the volume thing. So on the, on the NPW, or if you're paid, like, if you want to avoid the lottery, you can just pay eFabulous $10,000 and you get your 300 chips. So you've got like for low volume for prototyping or for short runs of products, it could work. But then there is, I think, and I think there still is like a gap between 300 and 10,000. So what do you do there? And it's the same with packaging as well. It's not just the chip is like actually getting things packaged. Everyone is set up for these long runs. And if you don't fall into the, what they're expecting, then things get expensive quickly. So I do think that's something that probably needs to get worked out. I know that Global Foundries are very keen on seeing like an encouraging the first volume run of an open source design, whatever that will be. And that that's maybe something that's going to happen in the next couple of years. Oh, that'd be great. The person I've spoken to there at Global Foundries, Karthik, he's very happy to assist with silicon and support and stuff like that.

**Matthew Venn:** Yeah. So like kind of taking it out of the academic, maybe academic is the wrong term probably, but like low volume experimental type things to things that are actually like, that have enough of a, you know, a gripping use case that like people are like, yeah. I would either buy that off the shelf or I need this for my product that already has the volume associated with it.

**Chris Gammell:** Yeah. Because at 10,000 for 300 parts, that's still like $30 a part. So sure. Sure. You'd have to have a good reason for doing it other than kind of proving something out before you do a volume run. So then to go on to your second part of your question, that was like, why someone's on the cusp of doing this? Why should they get involved? Or what will, or like, what have I seen when people come on my course, for example? Sure.

**Matthew Venn:** Yeah. Well, we should mention here too, if people don't know, Matt has a course where he teaches people, you know, it's a paid course. It's very guided. You basically get through and like, he'll walk you all the way through to getting a taped on chip. Yeah, exactly. So like, yeah, it's called Zero to ASIC, the Zero to ASIC course. That's right. Perfect. Good callback. Yeah. And I think that like, people are deciding to sign up for the course and deciding to get to the end because they have something in mind. What is that? I'm sure you've talked to them the most.

**Chris Gammell:** Well, one thing I started, because it's only been running for two years. We've had like nearly 300 people on it now. And I've, I started off with a kind of a face to face live onboarding one to one to kind of welcome people onto the course and set expectations. And right at the beginning to say, you know, thanks for supporting. And you're like one of the first people to test this out. So if, you know, encourage people to give feedback and not worry if there's some rough edges here and there, set expectations and so on. But I kept doing it because I really enjoyed meeting the people and asking them, you know, what, what do you want to get out of it? And why do you want the course? Where do you hear about it? That kind of stuff. And I'd say good kind of 30 to 50% of people just want to understand between the silicon and running a program. So they already like maybe call themselves a full stack engineer or they kind of, you know, that's very well known, isn't it? Full stack engineer. You know, that's one of your running jokes on the, on the, the podcast as well.

**Matthew Venn:** Got to get into the silicon in order to really say you're full stack. Yeah. Yeah.

**Chris Gammell:** Now you do. Now you've got to, now you've got to start with your and gates and your or gates. If you're going to call yourself full.

**Matthew Venn:** It's all, it's all driven from like, like nerd credit, Silicon Valley cocktail parties, I'm guessing. Right.

**Chris Gammell:** But like, say, say you're like a front end UI person, that's your specialty. But you know, in your, in your hobbies, you do websites or you like set up a Linux server or a cloud instance or something. Or you get into Arduino or Raspberry Pis or something. It's like the door is opened or the curtain is lifted onto, well, how does that stuff work? Like going to the next level down. And I think there's just, there's a lot of curiosity about how it actually works. And I was a contracting engineer for 10 or 15 years. And I never really thought about how the chips work that I use. I just read the data sheets and wrote the programs and they worked. Right. And I never thought that I would design my own chips or that I would, I don't know, it all just felt like a black box. Yeah. Literally, literally a tiny, tiny black box. Tiny, tiny, tiny, tiny black box. Yeah. Silvery, silvery gold. That's right. Tiny rainbow colored box. Yeah. So a lot of people just want to fill in the details. I get like recently quite a, quite a few universities because they're a lot, a lot of universities are starting to switch over to the open source tools because it's easier for doing the training or like. That's great. Yeah. Because a lot of times they, they use like gifted stuff from like. The proprietary vendors. Yeah.

**Matthew Venn:** The big three, right? Yeah.

**Chris Gammell:** But you only, you only get those deals if you're a big enough university with enough. Ah. With enough. Clout. With enough clout. Exactly. And if you're like a really small university or no one's heard of you, then you don't get a very good deal. And these tools are extremely expensive. Interesting. It's like the long tail in action, huh? Absolutely. Yeah. The long tail. The long tail.

**Matthew Venn:** Serving the long tail.

**Chris Gammell:** Yeah. Yeah. Totally.

**Matthew Venn:** That's great.

**Chris Gammell:** And so now it's all of a sudden a thing that you can do. And so I'm getting universities sending their professors on the course and then they go away and they make a VLSI course that involves a tape out.

**Matthew Venn:** So that's how it starts, man. Like that's, I keep hoping that, you know, Kaikad gets into universities too, because why not? You know, like that's how these sort of things spread.

**Chris Gammell:** Yeah. Definitely. Yeah. Kaikad's another amazing tool.

**Matthew Venn:** What is the, so you said 30 to 50% want to understand Silicon. Universities are sending professors.

**Chris Gammell:** Yeah.

**Matthew Venn:** Are there any that are like commercial?

**Chris Gammell:** Yeah. I've got maybe like 20 or 30% are people from a company. Like someone will buy a ticket. I'll get the notification of their email and whatever. And I'll often, before the onboarding interview, I'll just look up their domain name if it's a corporate domain name. And there's a lot of small companies that are starting to consider custom Silicon or at least using the open source tools as a way of proving a concept. Aha. Yeah. Cheaply doing a cheap tape out. Because even like $10,000 for a tape out is, is very cheap for, you know, a small to medium enterprise. Sure. And then once they've proven something that works and they've maybe characterized it, then they, then at that point, maybe they sign an NDA with a, with a bigger foundry for a smaller process. And they license the tools and.

**Matthew Venn:** Yeah. They really dig in at that point. Sort of. Yeah.

**Chris Gammell:** They kind of like tweak it all up and get it ready to, to sell. You know, there's a big difference between a proof of concept and a product you can sell. As I, as I'm sure you and everyone listening to this is aware of.

**Matthew Venn:** Uh-huh. Yeah. So like kind of just thinking through some of the reasons that a company might be interested in, I would imagine, uh, proprietary like algorithms, things they don't want people to be able to extract without really digging in, you know, slicing off the silicon and do an X-ray type stuff. I'd imagine lower power. I'd imagine lower space, like the smaller, maybe environmental type stuff. And then maybe sourcing, but I feel like that would be kind of a, a fool's errand really because of the timelines involved.

**Chris Gammell:** Yeah. Although, you know, there was a time when we were, would have been quicker to have designed your own RISC-V SOC and had it fabricated than wait for some STM32s to come in. Yeah. Yeah. That's true. Yeah. You'd have to really know what you're doing.

**Matthew Venn:** I think we might be on the other side of that, but. I hope so. Yeah. Yeah. That's, it is interesting too. Like the, the RISC-V thing, like it's still just, it, it boggles my mind to, to, to think of all these people, you know, like the, just the, the ping ponging of, of it's on a longer time scale, but like for a long time, people would be like, oh, I'm going to design my own processor. And then it was like, well, why wouldn't you just go with ARM? And now it's, it's moving back to like, well, yeah, I'm going to design my own processor. I need, I really, really need these peripherals or this feature set or this custom instruction or whatever it is. And it is possible now.

**Chris Gammell:** Yeah. Yeah. Although I would say that's more like SOC though, because there's still like not a great argument to design your own processor and SS for a learning exercise. You should just use one of the many RISC-V processes that are like available off the shelf.

**Matthew Venn:** Well, I meant like, uh, like the ones that are going big, like you mentioned, the ones that are buying tools and, you know, for whatever reason, right. You know, the, the one of like, maybe the secretive nature of it or the custom peripheral needs, like they, they might not do it through these, these open source tools, but they might. It's still go RISC-V. You know, I'm sure there's many in, in flight RISC-V processes or processors right now that, that we're going to see in products in two to three years.

**Chris Gammell:** Yeah. I'm sure. Yeah. And there's a lot of very big names like Western Digital who are kind of on the, on the RISC-V bandwagon. Yeah.

**Matthew Venn:** Uh, well, let's also level set on, on the capabilities here. Right. So, uh, cause then I, I want to definitely get into tiny tape out as well. So in these, in the open PDK and the, the, the multi-project wafers type things, like how big is the silicon? And like, what could you fit in there at the, at the various process nodes? Yeah. Like what are the maximums?

**Chris Gammell:** So on the NPW from, uh, eFabulous and Skywater and Google, uh, you have about 3.3 millimeters by 2.8 millimeters. Just that's nearly right. It's not exactly right. It adds up to about 10 square millimeters. And that's a lot for some stuff. Like all of my FPGA designs that I was kind of working and learning with, I could fit them all in. Like under one, under one wafer? Yeah. That was one of the reasons why I like very early on started by inviting other people to join with me and put like multi, multi-project wafer. So we put, um, nine designs on my exception wafer. Yeah. Yeah. Doing that kind of even lower level integration and more designs. If you're used to FPGAs, you're kind of used to every logic element has a lookup table that you can model logic with and a flip-flop and a carry chain and whatever. So you're used to getting a flip-flop on every logic tile, but with an ASIC, that's not the case. You have like a blank slate and you put down whatever it is that you need. And at that point you realize how much more huge a flip-flop is compared to an inverter. It's like six or eight times bigger.

**Matthew Venn:** Yeah.

**Chris Gammell:** So it really depends on what your application is and how much logic and how much flip-flops you've got. One of the big problems or one of the challenges I'd say is like memory density. So you don't need to use a flip-flop. If you want high density memory, you can use like a bit cell, which is a special foundry cell that is like the smallest they've possibly been able to squeeze it for their PDK. And you can use like a tool like OpenRAM where you can say, I want a kilobyte and it will build to you like an SRAM block that you can drop in. That's nice. But if you use the entire area, that whole 10 square millimeters and filled it with SRAM blocks, you might only get like 25 or 30 kilobytes. So. Uh-huh. Okay.

**Matthew Venn:** That's, that's, that's a good, actually really good. Cause I feel like that's a good level set for what people expect out of a microcontroller. Like, so that's before. Yeah.

**Chris Gammell:** It's microcontroller level, but not like enough cache to run Linux. You know, you could, you could definitely put a, like a risk-like processor on there that could definitely run Linux, but you would have to have off-board memory and then you would have a, a bandwidth issue going through the iOS to the memory and that would be slow. Right. Okay. So it's more like microcontroller.

**Matthew Venn:** Yeah. Got it. That is interesting too, because I, you know, I always complain about, you know, I'm so used to like the, the growing flash size on a lot of like modern microcontrollers.

**Chris Gammell:** Yeah.

**Matthew Venn:** Like, I'm just like, oh, why don't they give us more memory? And the answer is because it's expensive in geography. Right. You know, even, even when you're shrinking it down.

**Chris Gammell:** And, and, you know, there's still like, I never really got into the ESP32. Does that use external flash still? It has onboard, some onboard stuff, but it does use external SRAM. Yeah. Because the 8266, you know, you had to have that external flash.

**Matthew Venn:** Yeah. Yeah.

**Chris Gammell:** And isn't the RP2040 external flash? That's definitely external as well. Yeah. I know that. Yeah. So it's, it's still a thing. It's like, you burn so much area and that's why things like advanced packaging and flip chip is, is interesting because you use one process that's optimized for logic for the logic. Yeah. And then using other processes optimized for memory, but you slap them together with some interposer or whatever that gives you, that means that you don't lose out on the bandwidth and the signal integrity of having it all so close together. Right.

**Matthew Venn:** Right. And I think that, yeah, that's a really good point. And, you know, you let the, you let the people that are doing, you know, the Samsung's of the world that are optimizing at the furthest node. Like you don't need 10 nanometer flash memory. You know, you're not going to get access to the 10 nanometer node. Probably definitely not with these, these processes yet. I wouldn't, but they are, and you can just buy that and interface to it. So like if the, if, if you said like, if the IO doesn't matter that much, which flash is not as big a deal as, as Ram. Right. So like you could, you can kind of glue stuff together that way. Mm-hmm. Okay. So you could get, so you, and you could, and you are seeing small microcontroller designs on there. Again, I'm just trying to kind of give people a kind of a general idea of what's, what's possible. What's, what's been seen on there.

**Chris Gammell:** I've got, I've actually got recently started a hashtag on Twitter and Mastodon called open source ASIC highlight. We don't have that much stuff on there. I think it's only been done like four or five times, but some of the most interesting stuff is like FPGA fabric. There was a dual RISC-V core with a built-in radio. The radio. Wow. Yeah.

**Matthew Venn:** Whew.

**Chris Gammell:** Yeah. I know. Yeah. Very impressive. I'm still waiting for that interview. They, when I contacted them, they're like, no, it's not good enough yet. And I was like, mate, definitely, definitely worth.

**Matthew Venn:** I was going to say, I, I, I, I had a quick moment of panic there. I was like, oh crap. Did Matt tell me I should interview someone? And I'm like, oh no, Matt does interviews. So that's, that's much better. Yeah. Yeah. Yeah. That's good. You should be talking to them. Cause I have no idea who they are first off.

**Chris Gammell:** Yeah. And if you go on the eFabulous websites, you can like scroll through thousands of, entries to the lottery. Not all of them get taped out, but you can see the kind of stuff that people get up to.

**Matthew Venn:** Yes. And I shouldn't mention we had Muhammad on the show as well from eFabulous. Yeah. Number 503. I haven't caught up with him in a while.

**Chris Gammell:** Yeah. Yep. So prepared.

**Matthew Venn:** Yeah. That's, that would have been like me furiously typing for like, like two minutes. Matt's just like, yeah, I made this. I made a, I made a sheet for it. So yeah. Thank you, Matt. You're very organized. You're very organized and both in your, your course and your just the, I really loved your recap video. You did a recap video of 2022. Yeah. And like, it really highlights there's, there's a lot going on in this space. It's great.

**Chris Gammell:** Yeah. Yeah. I had to really trim it down as well. I had to like throw out the least good half and it was hard. Oh shoot. Now people are listening to like, oh, I didn't make the video. No.

**Matthew Venn:** Yeah. Yeah. So much stuff is happening. It is. And like, and people are excited about it too. It's, it's great. I mean, like, it's really great. It's, is there going to be like a, I don't know, like a conference around this sort of thing is other conferences. I know there's like a risk five kind of thing, but not.

**Chris Gammell:** I did one last year called open tape out. Okay. And I was thinking of doing another one. I'm now a board member of the Fosse foundation. And I brought it up in the most recent meeting saying, why don't we do like, cause there's now conferences are kind of coming back up. There's like, there's latch up. Oh yeah. Well, Fosstem is really soon, but there's not so much hardware in Fosstem. Then there's latch up. There's OSDA and date and there's more stuff coming up. But I like online conferences because they're much easier and cheaper to organize.

**Matthew Venn:** And yeah. But they're less engaging.

**Chris Gammell:** That's the downside. They're less engaging. Yeah. That is the downside. I agree. There's like less opportunity for networking, but yeah, they've got ups and downsides.

**Matthew Venn:** Who goes to conferences for the talks, Matt? Come on. Like.

**Chris Gammell:** Yeah. You just watch the screen later. Go to conferences for the hallway. Yeah, exactly.

**Matthew Venn:** Exactly. You know, you. Yeah. Fosse is free and open source silicon. Is that right?

**Chris Gammell:** Yeah. That's right. Okay. Yeah. It's a foundation.

**Matthew Venn:** Yeah. That's cool.

**Chris Gammell:** And we were thinking of maybe like running, running a, an online conference. Because there's like a, the, the face-to-face one in, on the West coast, uh, coming up, uh, latch up, but I won't make it. And I won't make it because it's like too far to go basically. So. Yes. You are based in Spain, correct? Yeah. I'm based on the East coast of Spain in a city called Valencia and online conferences. Yeah. I mean that people can attend all over the world, even if they don't have the ability or the money or they don't want to travel.

**Matthew Venn:** Sometimes you just got to get up at three in the morning, you know? Yeah.

**Chris Gammell:** Or watch it when it's streamed. Yeah. Yeah. I don't know. I find, um, 6 PM central European time quite good because that works for Indian time. And there's a lot of stuff going on in India as well in this space.

**Matthew Venn:** Oh, interesting.

**Chris Gammell:** And, but it also works for Pacific time.

**Matthew Venn:** Yeah. Yeah. That's like 9 AM Pacific.

**Chris Gammell:** Sorry, Australians. Sorry, Greg.

**Matthew Venn:** Yeah. Yeah. That is the, the, the most common webinar time I see is like, they're always doing 9 AM. Yeah. Yeah. Yeah.

**Chris Gammell:** And I, for the, the weekly calls for my course, we do it at six. Yeah. Yeah.

**Matthew Venn:** Yeah. Yeah. What's going on in India?

**Chris Gammell:** Well, I mean, India has been like a place where loads of chip design work has been outsourced to. So you, you might have like a design team in California, but you might have the verification team, which might be even like the same number or double the number of people working out of India. And I think, you know, we're not there yet. Like it's no one should think that the open source tools are kind of capable of challenging the proprietary ones. They've had like 20 years lead and like hundreds of billions of dollars poured into them. Yeah. It's going to be a while. Yeah. But that doesn't mean there's not niches now that can still work. For example, education. And there'll be, there'll be more stuff coming online. And what I think one of the exciting things is you could come from a place where you don't have the resources for these expensive tools and you could do something creative and groundbreaking that nobody had thought of because you've got availability to the tools in a way that you never had before.

**Matthew Venn:** Yeah.

**Chris Gammell:** Or you train up and you know what you're doing and then that makes it easier for you to land a job in one of these bigger companies.

**Matthew Venn:** Yeah. I think that's right. Yeah. And I mean, like accessibility is really important in these cases. And I think about like the, you know, we're in the hardware industry broadly, right? You know, calling the PCB, you know, system level down to silicon level. It's, it's weird because it's, it's further, it started sooner and yet it's much further behind the software world, you know, in terms of open source and accessibility and stuff like that. Yeah. But I think it's, I think because of just the investment required, right? Like the.

**Chris Gammell:** The money investment.

**Matthew Venn:** Yeah, exactly. I mean, there's, there's hard, hard money investments that had to happen. And as a result, there's a culture of secrecy, like you had mentioned earlier, but what we're seeing now is one, I think the software industry is leaking into the hardware world, right? That's, that's thanks to folks like Tim and, and his coworkers at Google. And, and they see business benefits from doing that sort of thing. This is like, you know, this is off the cuff as well, like we usually do here. But I think then as well, we see an excess of capabilities, right? So like these fabs, even though you mentioned like it's 180 nanometer fab, which is, I don't know what, 20, 20 generations behind. I don't know what the generation number. Yeah. It's 20 generations behind the, or I guess that would be divided by 1.5. So say 12 generations behind the leading edge, which global foundries also does. Right. And it's like, but they still keep it running because there's, because it's already been paid for. And so now that becomes excess capacity. So it's like, it's not zero marginal cost. Like I think some of the software stuff gets, which is an oversimplification as well, but it is excess capacity that, that then there's other benefits to having the marketing and the, and just opening it up to new business as well. Yeah.

**Chris Gammell:** And seeing what happens. Yeah. Yeah, exactly. I mean, I, I know after education, which, you know, I don't know how big that market really is or how many wafers education would buy. But I think another one that is likely to happen, it will be in the security space where you want transparency and inspectability. So if you think about all the cloud services that is being offered, people like Amazon or Microsoft or whatever, they're even building their own servers. And what they want to guarantee you as someone that runs a software as a service company or something is that you control it all the way down and it's only going to be running your software and there's no kind of man in the middle between you and the hardware.

**Matthew Venn:** Right.

**Chris Gammell:** And so they do these things with these little route of trust authentication chips. Yep. And it doesn't matter if those are old or big. What matters is that you trust them. If there was like an open source design for a route of trust chip that everyone could inspect and then it was made, the GDS was made with an open source inspectable tool chain, and then it was taped out on a, on like an open source PDK. And then someone even like imaged a few of the chips to prove that they were the same thing that was sent in. Then you've got, you've really got like a level of trust and inspectability that is difficult to get otherwise. And that kind of thing might be a good, like one of the niches where open source chips will actually start to have a market share.

**Matthew Venn:** Yeah. That's really interesting. That's, I mean, the route of trust stuff, that's what we had Laura from Oxide talking

**Chris Gammell:** about a little bit. Yeah, exactly. Yeah. That was a, that was a great episode. And she discovered like a whole bunch of problems in that chip that they reported back to NXP. I think it was. That's right. Yeah. Yeah. Yeah. I reached out after that episode and was like, Hey, do you fancy making your own one next time?

**Matthew Venn:** That'd be great. Yeah. Yeah. Yeah. If they do, that'd be, I'm sure that like, yeah, like you said, that's, it is interesting to think about like, I mean, you and I are talking right now on across hundreds, thousands of miles of just computer infrastructure. Right. And you don't think about the stuff that's down below, but there are people that are like, that need to understand that entire chain because of, because at some point there is a critical, there's critical pieces of the infrastructure that if they, if they don't understand that, that they, they literally don't have the keys to their own kingdom.

**Chris Gammell:** Yeah.

**Matthew Venn:** And I think you're right about the niche piece as well. I think it's, I don't expect DSMC to dive into this anytime soon because there's just

**Chris Gammell:** so much money involved. And DSMC actually have a great educational program running already. I found out. Oh yeah. Yeah. When I spoke to a Taiwanese professor, they have like, if you're at university doing VLSI in Taiwan, you basically get free silicon. Wow. That's great. Yeah.

**Matthew Venn:** Yeah. Yeah. And I, I think that, that is, you know, that's how you make a company that lasts for many, many years. And you, you basically build your own pipeline of, of, of engineers. Yeah. Yeah. Engineers. Yeah. Yeah. That's great. Let's talk about tiny tape out. So now let's, so now we're, we're basically like, uh, uh, you know, going down into the quantum quantum realm, right. In terms of the, the size of chips that people are making. Yeah.

**Chris Gammell:** We should make sure we get some time to mention as well. Um, yeah. And those are tied together. Yeah. Well, they, they're kind of, um, complimentary. So yeah. Tiny tape out. I can't totally recall where the idea came from, but it's an extension of the work that I do in my course where we get like 10 or 12 people's designs and join them all together using a tri-state bus and then put that all into one chip and tape that one chip out. So then we only have to make one application or pay for one chip. And then we get, then we share the, the results back between the course members. Can you explain the tri-state bus real quickly? So you just, you basically have like a chip select for each design or how does that work? Yeah. Yeah. Just like SPI. Like if you've got like a bunch of SPI devices, they've each got an active line and normally their inputs and outputs are high, high Z as you say in America. I've actually been converting myself to American English. It's an interesting one. I mean, I, it's like, I stopped spelling analog, analog, G-U at the end. Um, and then I was just wondering, where does it end? Am I going to like, I mean, American English is what the world speaks, isn't it? It's not English English. It's American English.

**Matthew Venn:** So, well, have you started, have you started saying y'all yet?

**Chris Gammell:** Y'all. We use high Z inputs y'all.

**Matthew Venn:** Well, I mean, you're in Spain as well. So interesting. I'm, I'm, I'm speaking of education. I'm taking a Spanish tutoring.

**Chris Gammell:** Oh yeah. Como es?

**Matthew Venn:** The vosotros form, right? So vosotros is like how you say plural version of you. And there's not really that, you know, in, in English, it's like you guys or, you know, all of you, but the best, I think the best translation is y'all. So Spain, which uses vosotros in Latin America doesn't normally use vosotros or most, some of Latin America doesn't. Yeah. You already have y'all. It's vosotros.

**Chris Gammell:** Yeah. So we have all these designs, um, tri-stated and they only come, they only kind of activate their, their outputs once they've got the active line.

**Matthew Venn:** Great.

**Chris Gammell:** And then they have control of the, uh, 38 IOs the chip has. Cool.

**Matthew Venn:** So then do you have to route the, how do you, how do you route the actual IOs to each individual chip then? It's just like. The auto-router does it. Oh yeah. Really? Yeah. What is, what is the, um, I guess I, I haven't, I haven't tried this yet. You know, like I said, I, I haven't felt the pull to do it yet, but how much is their automation in there? Right. Is it all like, are people mostly. Yeah. Yeah.

**Chris Gammell:** The digital side is, is really automated. So you take your harder description language. Like Verilog or VHDL are really popular common ones. And you throw it in one end of one of these tool flows, uh, like open lane is the one I use most often. And that's the one that's developed by e-fabulous. The core of open lane is formed by open road, which is a separate project. They used to be DARPA funded. Yeah. Yeah. And, uh, they do a lot of good work. Open road, check them out.

**Matthew Venn:** I think when, uh, Muhammad was on the show, he mentioned that he explained a bunch of that. Yeah.

**Chris Gammell:** He mentioned that. Yeah. So, yeah. Yeah. So open road kind of forms the core tooling, like the, the place, the placement and the, uh, the STA, the static timing analysis tools and this kind of stuff. But like the number of tools involved in the flow is, I don't know, maybe between 10 and 20 different tools. Wow. So kind of all like plugged together in a long line. And if everything goes well, you put your, your Verilog in and at the end you get your GDS out. Awesome. So you don't do any manual routing. It like, it does it all for you. And then you get to visualize it as well, right? You get to visualize like. Yeah. You can then look at it. Yeah. And do a 3d render and post it on Twitter. Yeah. That's what you gotta do. Right. Yeah. If you try tiny tape out, we also have like a really cool 3d viewer that runs in the browser. So you can kind of zoom in on the standard cells and see how the, the, all the, the wires are connected.

**Matthew Venn:** So what is the difference then? So in tiny tape out, you are not writing Verilog or you are writing Verilog.

**Chris Gammell:** So the target audience of tiny tape out is like absolute beginners. People not even like most of the people on my course have like use a computer or have done some programming. I mean, the idea with tiny tape out is we have enough learning resources for people that have never, never done digital design before. And I'm collaborating with Uri.

**Matthew Venn:** Yes.

**Chris Gammell:** From Wokwe. You had him on in number 599. That's right.

**Matthew Venn:** Yeah.

**Chris Gammell:** That's right.

**Matthew Venn:** I think Uri might be the, the, I don't think he sleeps. He just seems like he's, he's just always making new things. It's a. He's a, yeah.

**Chris Gammell:** He's very good fun to work with because I can like come up with ideas in a spec and then like a few hours later or minutes sometimes. Yeah. I've got something that I can experiment with and play with and we'll get onto tiny tape on a, sorry, silly was in a bit, but we're using Wokwe. And that was one of the things you spoke about with him in that episode, which is a really nice interactive browser-based tool where you can build, like you can drop an Arduino in, put your LCD in your button, write some firmware and then simulate the whole thing.

**Matthew Venn:** I think the thing is it, it presents as an Arduino simulator, but it's just like the most powerful engine underneath. It's like, it's like a Ferrari engine underneath like one of those like play school plastic toys that my daughter rides in, you know, like the little cars, you know, it has a really good

**Chris Gammell:** model of, of the chips. And I met him in one of the Hackaday remote times and he did a talk about when he added the RP 2040 to Wokwe. So then you can run your designs on that. So we basically added a set of 10 components and gates, all gates, flip-flops, that kind of stuff, and you build your digital design out of those. You can use LEDs and whatnot to kind of debug the state of various things. And then we added a, an API, not really an API, but a way of requesting it to give, to dump you a net list in a Verilog format. So then it tells you here are all the gates. Here's what they are. Here's how they're connected in between that kind of input and an output plate that gives you eight ins and eight outs. And then we have a GitHub action. So you create a, you template my GitHub repository. It's got an info.yaml file. And then you change the Wokwe ID to your ID. It fetches the Verilog net list, runs it through OpenMain and the open source PDK and generates you GDS and a kind of report file. Yeah. And in the report file, you've got a list of the standard cells that were used and a 3D model of the, of the little design, which tiny tape out one, I think was 120 by 120 microns. So it was like enough room for kind of five or 600 standard cells.

**Matthew Venn:** So that's actually a really good, a good kind of like audio visualization I hear, I feel like too, right? So, so people start with just like an inverter and a NOR gate and an AND gate connected together however they want. But the inverter has a set of transistors that are defined in the standard cell, right? And basically because you know the abstracted inverter shape or inverter function, you can then assign that to all of these gates that it represents. And then you tie that to the set of gates that represent the NOR gate. However, people are connecting these things together. And then it just kind of processes all the way through, right? The, I feel like that's kind of the, the, the abstraction layers are, are deep on this one, you know?

**Chris Gammell:** Yeah. But in a way you're, you're like, you're, if you're using Walkoo, you're actually closer to the hardware than you are if you're using a hardware description language, because you are actually drawing a schematic with components. And I think that's actually a good way to start because if you're a programmer, one of the hard things about coming to a hardware description language is, especially one like Verilog, where it kind of has a C like syntax. It's not really describing all that much hardware, right?

**Matthew Venn:** It is, but it's not.

**Chris Gammell:** Yeah. You're writing a program that's going to be executed on a general purpose computer, one line at a time, or like one instruction. However, that line is broken down into its instructions. When you're designing hardware, you are designing that machine and that machine. If you need something to be done sequentially, you have to first build a sequencer. Otherwise everything's just going to happen all at once. Just like an electrics and electronic circuit. Yeah. You know, it's all happening at once. So yeah. With Tiny Tape Out, that's the idea is that you, you start your, it's like for real beginners, people who've never done any digital design. But for Tiny Tape Out 1, we actually ended up with maybe 30 or 40% of the designs were in some HDL or other. And we ended up changing the, the GitHub action so that there was like one version for Verilog and one version for Amaranth and one version for VHDL or whatever.

**Matthew Venn:** What's Amaranth?

**Chris Gammell:** It's a, like what's called an HLS high level synthesis. So it's like a bit higher up than something like Verilog. Oh, interesting.

**Matthew Venn:** So you kind of said, you said LightX earlier. Is that, is that the level Amarax?

**Chris Gammell:** Yeah, that kind of level. Yeah. Yeah. There's another one called Chisel.

**Matthew Venn:** You know, it'd be useful is to, to draw a map. Is there a map of all of these different tools of like what, what's built on what? Cause if not, that would be really useful. So yeah, that's a good idea.

**Chris Gammell:** I'll write it down.

**Matthew Venn:** That's yeah. That's, that's really good actually, because I feel like people do kind of, they want to operate at different levels, right? Some people say, I just want to blink an LED. Some people say, I want to actually see, I want to control which inverters are involved in blinking that LED. And yeah, right. And there's reasons to learn each of them, I think. Yeah.

**Chris Gammell:** And you know, one of these kinds of arguments you see all the time is like, oh, to be a real programmer, you've got to understand the full stack, which I think is nonsense. But I think if you want to be like a master programmer, then it can help to understand more of what's above you, who's consuming what you're doing and what's below you, what the abstractions that you're basing your work on are based on, because a deeper understanding of those things is going to, on one side, mean that you deliver better stuff to the people that you're using your, your output. And on the other side, you're making better use of whatever is you're standing on. But yeah, it's like, I can explain how a computer works down to a standard cell or a MOSFET, but I can't actually explain to you the quantum effects of how electrons tunnel in a flash cell. So, you know, life is too short. Do you even electron volt, bro? Come on. Yeah. Yeah. You've got to, time is like the most valuable resource. You've got to choose where you're going to spend it. And when I was young, I had infinite time and no money. So I just did everything from scratch to learn it. And now I have infinite money and no time. Yeah, it is. I, I feel the pull.

**Matthew Venn:** I feel that same pull these days.

**Chris Gammell:** I don't know if I would say I have infinite money, but, but, but yeah, you've got to choose. You've got to be wise about where you spend your, your effort. Yeah.

**Matthew Venn:** It is. One thing that I've seen is that the people that, the people that do understand more of the stack, like above and below them, like you mentioned, kind of looking up, looking down, it may not be critical for design, but it damn sure helps for troubleshooting.

**Chris Gammell:** It's like, yeah. You just like aware of like, cause those abstractions break. Yeah. You know, it's like, oh, it doesn't work like this. I always, I thought, I thought, you know, it was just digital zero and digital one. And there was, you know, like in between things, it actually is a real voltage that might not be exactly one or the other. Yeah.

**Matthew Venn:** Yeah. All kinds of problems. It is a smack. And it's the, that's the 2am problem right there. When you're like, what am I looking at right now?

**Chris Gammell:** Yeah. And it makes no sense with the abstractions that you're used to. And you have to break your mental model.

**Matthew Venn:** Then you have to reconstruct your mental model. And yeah, it's a, oh, what fun learning. Didn't learning fun, Matt.

**Chris Gammell:** But, you know, I think that, you know, we're like, we're all drawn to solving puzzles in this area. That's like one reason why we're here so that we stay up till two in the morning trying to solve it. Yep. So, okay. So tiny tape out, basically people can, can they still do it? Yeah. So tiny tape out makes it even easier to submit a design onto the shuttle. And the other thing is we're not using the lottery shuttle. So, cause I think one of the things that is starting to become frustrating is like the last shuttle, there was a one to three contention ratio. So you could put a lot of work in, submit your design, and then you're not even, not even guaranteed that you're going to get it made.

**Matthew Venn:** Got it.

**Chris Gammell:** With tiny tape out, we have like the, for tiny tape out too, we had 250 slots and we sell those slots. So you can, all the educational material is there and you can use it and you can learn everything, all the content is free and not behind a paywall. Unlike my course.

**Matthew Venn:** How much does it cost for a tiny tape out slot?

**Chris Gammell:** We've got two different price levels. One is design only, which is $25 or was. Yeah. I don't know. We may need to change the price. We'll have to see what, what, what happens. And then a hundred dollars gets you your design on the chip on a PCB.

**Matthew Venn:** Oh, nice.

**Chris Gammell:** So you get the whole thing and it's kind of being tested. And the other nice thing with tiny tape out is you've got all the other designs.

**Matthew Venn:** So you get to play around and see what other people did.

**Chris Gammell:** Yeah. And when you submit your design, you have to like have some basic documentation in place and then we aggregate that all together into a kind of custom data sheet for the chip. So when you get your PCB with your chip on it, you've also got like a basic understanding of how all the other designs work and how to test them and what to expect.

**Matthew Venn:** So then, okay. So they get the PCB with the chip on it. Is it activated for their specific chip? Like, is there like a pull down for their, for their chip select or what?

**Chris Gammell:** There's, uh, there's a little eight pin dip switch and you set it to the ID of your project. Yeah.

**Matthew Venn:** 250 slots. And that activates that one. I guess there's six, six extras in there doing some controlling, huh? Yeah. Yeah. Don't set it to those or it'll blow up. Yeah. Oh, that's super cool. Wow.

**Chris Gammell:** Yeah. If you go on the tiny tape out, uh, runs page, I'll just paste that in the, um, the message here. You've got a picture of the die. So you can kind of see how we've fitted them all together and you can see the ones with a lot of purple. That's rooting on a higher metal level. So it gives you an idea of like the more dense designs.

**Matthew Venn:** Yeah. Cause some of these are really, really simple things like blinkers and similar type of thing. Right. But some people are also.

**Chris Gammell:** Yeah. Some might have like, I had like a system on there. So if there were less than 10 standard cells, it would be like a warning that I would have to wave. So I would check out their design and be like, yeah, they really just have got an end gate in there. Fine. That's cool. They just want to, they just want to have an end gate. Yeah. Fine. I have no problem with that. And then another one, they're really struggling to fit it all in. Like we had some, we had a risk five processor on here, Chris. No way. Wow. Yeah. Do you know Olof Kingren? Oh, the name, the name sounds familiar. He's an award winning hardware designer. Okay. Here we go. And yeah, so he, he made serve, which was like an, which won a kind of a risk five prize. They run, they ran a competition a while back and it was like the smallest risk five process. It's a bit serial. So it executes serially. So it has a one bit wide register. So you have to execute 16 times. It's like a reverse pipelining. Yeah. But so it's, it's very slow, but it's very small. So Greg Davil actually mentioned him earlier, took serve and adapted it for this and taped it out on tiny tape out too. Yeah.

**Matthew Venn:** That's awesome.

**Chris Gammell:** Yeah.

**Matthew Venn:** It's almost like a, like a tiny Kickstarter, right? Like you get like the, you get the, the token, which is the, the end chip and the, you know, you're working on a board, but then you also get like the, the kind of we're all this in this together sort of thing. That's, that's pretty great. Yeah.

**Chris Gammell:** Yeah. It was really fun doing it. We have a discord, the tiny tape discord, and it's that really kind of pops off when it's getting close to tape out time. Yeah. Great. People helping each other out. Really cool to see that.

**Matthew Venn:** Community and culture, like that stuff, it matters, you know, like you had a, that's how you keep people interested and that's how people learn from one another, I feel like too. So that's great. Yeah. No, you don't burn out trying to run these projects. Yeah. So let's get to SillyWiz. What is, so SillyWiz is now separate from. SillyWiz. Yeah.

**Chris Gammell:** Yeah. So SillyWiz is designed to fill in the gap. So tiny tape outs, if you follow the lesson plans, it builds you up from like the most basic digital logic to like simple machines, like a padlock that only opens if you set the code right. And SillyWiz aims to kind of explain how, like from silicon to an inverter, a CMOS inverter. So how do you draw a resistor or a capacitor or a MOSFET or an N type inverter or a CMOS inverter?

**Matthew Venn:** So it's like another, it's another abstraction layer down. Now we're actually building, building a standard cell or modulating a standard cell basically. Right.

**Chris Gammell:** Yeah. Yeah. So you have like your canvas and then you can draw shapes on that canvas in a number of different layers like metal, polysilicon, N diffusion, P diffusion. And by combining shapes and patterns, you build up these little functional blocks that form the basis of all digital logic design. Awesome.

**Matthew Venn:** Yeah. I think we mentioned on the show and like the fact that there's sliders on there is like, I think I said this when we talked about on the show, but just like the being able to modulate and like change your environment and see what the result is without having to like redraw. Man, I still remember my analog course where it was like we were drawing with colored pencils on, not graph paper, like the tiny box, like the one millimeter by one millimeter box of paper. It's just like the worst way to learn, not the worst way, but it was just so inaccessible for me personally. And this would have been, I don't know, it's just, I have a lot more knowledge now, but it's just, it's really much more accessible.

**Chris Gammell:** Yeah. So it's in, it's in the browser. So you don't have to download anything and you can do and undo. So that's nice. And you can turn on and off layers. So it's less confusing, but you're right. The thing that makes it like feel amazing to play with if you've ever, and probably a lot of people haven't, but the people who are listening, who have spent time kind of drawing something out with cadence or K layout or magic or, and then extracting the circuits and then simulating it and then getting the graph up. Is that all that, like each bit takes a bit of time and there's, you have to learn each tool and you have to sequence them. And with silly whiz, you can increase the length of the gate on a MOSFET and you can, and it just within milliseconds, like not even a noticeable amount of latency, really. You see the graph changing and that gives much more of an opportunity for learning intuitively how these things work. And I think that that is really important for making it easier to learn things.

**Matthew Venn:** Definitely.

**Chris Gammell:** Yes. Yeah. Quick feedback. Yeah. It's kind of ironic that the thing that you're designing then takes like at least six months for you to get back in your hands.

**Matthew Venn:** Yeah. Why, why does that take longer? I mean, so like it, I'm just going to couch this in my experiences at Samsung, you know, wafer into wafer out was 30 days. What is the six month aspect? Like where is the largest chunk of that being spent?

**Chris Gammell:** Well, one part of it is you have to wait for the MPW to be ready to run because they don't run them all the time. You have to catch the right shuttle. And you normally would run them like four times a year. Okay. And then it's going to be one of their low priority jobs. Got it.

**Matthew Venn:** Okay. So it's, it's, it's in the holding cell whenever, whenever anybody else comes through.

**Chris Gammell:** Yeah. Cause they're probably only going to run like a lot of 20 wafers for an MPW. Cause it's just for hardly any parts. Skywater is slow.

**Matthew Venn:** Slower. I think, I think these are not like, you know, in the timescales we're talking about, this is an amazing, this is a miracle. These things happen at all, but like, yeah. But like compared to a high volume kind of thing. Yeah.

**Chris Gammell:** Yeah. It's not like a big, this, this, the skywater shuttles. I think that's like a kind of a fairly low priority for them. The, the, the global foundries one should take six weeks for wafers out.

**Matthew Venn:** Got it.

**Chris Gammell:** But packaging takes the same amount of time. Ah, interesting. So then you've got to ship it to get packaged and it's got to get packaged and then it's got to be like mounted onto PCBs and tested and then it's got to be shipped. Yeah. So with global foundries, it's conceivable to think that you could get your chips back in three months. Oh, okay. And I sincerely hope that that will start happening soon.

**Matthew Venn:** Yeah. Right. Cause these are innovation cycles as well. Right. So if someone was designing, you know, a commercial product, they would want to be, you know, like the cycle time really does matter for being able to try different things, optimize, update all of the things that you want to PCB.

**Chris Gammell:** I mean, ideally you want that result back so that you can learn from it before you send the next one. I need to see all the mistakes I made. Yeah. On my bench. A lot of people don't have the luxury to do that. You've got to like send off your next iteration and you may, you may have errors that you don't know about. Yeah. And you know, that's something that really bit us hard with the Google Skywater shuttles and PW1 to 4 because there was this critical problem, a hold violation problem. And if you're a chip designer, you know that a hold violation is not something you can solve by turning the speed down or anything. It's really difficult to work around if not impossible.

**Matthew Venn:** Yeah. And you, you did manage to get yours blinking. I remember you.

**Chris Gammell:** Yeah, but it was a real, I mean, it was like a reverse engineering contest to capture the flag, you know, it's definitely. I wouldn't have done it if I hadn't had so much kind of not exactly riding on it, but by that time I'd kind of, you know, the course went so well that between the course and the other contracting jobs I did, I'm just kind of doing full time open source CDA now. Awesome. And I really, really wanted it to work. So I was willing to pour hours into it. Yeah. But if you'd done this as a kind of hobby in your evenings and then you got chips back that were really difficult to bring up, I'm not surprised that not many people managed it. Yep. And I was really only, I mean, I might've worked out on my own, but it was really Sylvain Manot's work, TNT, who kind of, he made a really fancy system that used an FPGA to model the memory that the Pico RV32 RISC-V processor on the ASIC executed out of. And then by counting the number of instructions executed, you could see how well it was running. Wow. And then it can modulate the core voltage. So he could plot a histogram of core voltage versus how many instructions the Pico RV32 managed to run. And then you could choose like an undervaulted amount that had enough instructions that could then execute enough instructions to set up the GPIOs correctly. Oh, wow. That was only half the story. Oh my God. But that was, yeah, that's really good engineering efforts on his behalf that kind of, I've got that board on my desk right now. It's like, instead of just being one PCB in an ASIC, it's like a layer of four different PCBs.

**Matthew Venn:** The monster grows. Yes. Sylvain was also on 467, the first show that you were on. Yeah.

**Chris Gammell:** He's actually working on Tiny Tape Out 3 at the moment. Oh, awesome. We're taking some of the money from Tiny Tape Out 2 and paying Sylvain to help execute an upgrade so we can run the whole thing faster. Awesome.

**Matthew Venn:** Yeah, I mean, yeah. All right, real quick, I want to talk about SillyWiz a little bit more, and then I'd like to ask her about the tape out process. Yeah, we've been going for a while, haven't we? We have, yeah. Yeah. Yeah. So SillyWiz, there's the video. You have to be part of Tiny Tape Out, the course in order to access it? Because I remember I saw a link of it at SuperCon, and I was like, oh my God, everybody needs to see this. But now it's part of the course for sure.

**Chris Gammell:** It will be available free, open source, definitely. Uh-huh. Don't worry. Got it. It's just that without knowing what you're doing, it's difficult to drive, and it needs some extra support or it's going to be frustrating. Got it. Yep. So we're doing like another round of UI tweaks, and I'm writing the lesson plan material at the moment with support from some analog IC gangsters I know. That's great. And then when that's ready, we'll launch it. And we will launch it first to Tiny Tape Out and Zero to Asic Course. Yes. People as – it's one of these kind of things that you have to get into if you're like doing – if you're like self-employed. You know, it's like you have your patrons and you give people a reason to patronize you by having advanced access to things. Yes.

**Matthew Venn:** I think people should go to tinytapeout.com and subscribe to the email list so that you can hear about the Silly Wiz first and then also hear about Tiny Tape Out 3 when that's ready. Yeah. And then you'll also get some helpful emails about going through the course, the free course stuff, and then maybe also Matt's more advanced course. Yeah, exactly. Yeah.

**Chris Gammell:** Sign up for the mailing list. That would be great. And then you'll be the first to get access to Silly Wiz when it's available. Yeah.

**Matthew Venn:** All right. So we've been talking – like you said, we've been talking for like an hour plus now. I do want to ask real quick about like the tape out process, right? Because it's not like – so if I submitted a design, click done, you know, I'm happy. I just wait my six months and I get a chip. You have other stuff you have to do with it, right? So like the actual like buttoning up a design and like sending it off to the fab, that's non-trivial. Break it down a bit more for me, Chris. Well, like – so what does it involve? So when you say tape out, what is that actually – what is the actual – you know, so I think about sending off a PCB.

**Chris Gammell:** I press the record button on my reel-to-reel recording. And then –

**Matthew Venn:** And then the magnetics.

**Chris Gammell:** Yeah. And they just take – Magnetic tapes and then I send them to Skywater. Right, right. And that's called a tape out. Right. Exactly.

**Matthew Venn:** You just say, first there's an inverter and then next to the – actually, no, below that there's a NAND gate and then NOR.

**Chris Gammell:** No, because what I'm really doing is I've got a big light box here and I'm using very fine tape. I've taped up the whole design. I send that to Skywater. I'm an artisanal taper. I'm an artisanal taper. Okay. I only use the most black of black tapes. That's right. Right. And the whitest of white backgrounds.

**Matthew Venn:** So, like, when I think about the PCB process, right, it's gotten easier and easier to send off a PCB – a set of Gerbers, right? I zip them up, send them off to the JLC or whoever and they tell me if I do something wrong. Is it the same for sending it to Skywater or what does it take to actually get that last step done?

**Chris Gammell:** Yeah. And there's abstraction here as well, right? Because if you were, say, going on a shuttle, a TSMC shuttle or a Global Foundry shuttle, that you were just interfacing directly with them or you were going through an intermediary like Europractice, then you would need your design. But you would also need it to be in a pad ring of all the GPIOs and the ESD protection and whatnot. There's a little bit more extra stuff. And then you've got to, like, depending on the packaging of your chip, like the NPWs that we've got access to, a wafer-level chip scale package. So they're like little BGA. So you need a little bit of extra information about how the packaging and the balls are bonded and all this kind of stuff. But for us, all of that stuff is handled by eFabulous. So the bit that we submit is just the 10 square millimeters that fits into a standardized harness. And that harness is called Caravelle. And that has, like, the pad ring, the GPIO, the ESD protection, the layout for the balls of the package and everything else. So for me, Tapeout is a bit easier than if I was interfacing directly with Global Foundries because I don't have to deal with that stuff.

**Matthew Venn:** Okay. Yeah, that's an interesting... Okay. So that's kind of what I was... I'm really just trying to make, like, in my mind, like an analogy for, like I said, PCBs. So in this case, eFabulous is acting like the boardhouse. And then the equivalent of, like, the people that are actually doing the silicon is, like, the people that are dipping the boards at the boardhouse, right? They're, like, actually imaging and, you know, you think about the process of making a PCB. And that's now the silicon processing through all the machines and all the steps that happen there.

**Chris Gammell:** Yeah. I mean, have you ever visited a PCB house? Only through Scotty's videos. Okay. Because one thing I was surprised at when I visited one is that they don't just take your file and, like, slap them straight on the masks or whatever. They inspect everything and they make little changes. Oh, yeah. Yeah. Like, move stuff around or they might, like, PCB way especially are pretty good at spotting errors and feeding back. So you could maybe say that, like, eFabulous are like that. They're kind of...

**Matthew Venn:** Yeah, yeah, yeah.

**Chris Gammell:** Dotting the I's and crossing the T's and then they send it off to Skywater and Skywater is the actual, the people that make the chips.

**Matthew Venn:** Yeah, the dipping of the stuff into the cupric chloride, right? Like, that's... Yeah. It is, it is at a board house. Usually they're together, right? Whereas in this case, there is like a... eFabulous is like the front of house kind of dealing with the digital files. And then the actual process control, that's just at the fab.

**Chris Gammell:** Yeah. And you'd have to be quite big if you wanted to deal with someone like TSMC. Yeah, right. Normally you have to go through an NPW service. It's run by an intermediary like Europractice and they... Oh, there's others. Yeah.

**Matthew Venn:** Okay.

**Chris Gammell:** Yeah. They will help, like, to kind of do the aggregation and help with the packaging and help with a bunch of other stuff. Yeah.

**Matthew Venn:** Got it. Yeah. Because a full lot of, like, you know, like, I think about, like, even 10 by 10 millimeter wafers or, sorry, chips, you could fit a lot of those onto a 300 millimeter wafer. And then the lot size is usually, like you said, 20 to 25. Like, that's 25 fits in a foop, I think. And then, like, and then just, there's just so much. That's so many chips to get through, you know? Like, that's just a really big order.

**Chris Gammell:** But, yeah. So, but for an NPW, they're all, like, that's, it's split between 40 people.

**Matthew Venn:** And so an NPW would be, would that be multiple designs on one wafer? And then you have 25 of those wafer? Yeah, exactly. That's exactly what it is. Okay.

**Chris Gammell:** So it means you only make one mask. Got it. Of, that includes all 40 people's designs. Right, right, right. So you split that 200 grand across 40 people.

**Matthew Venn:** Right. You wouldn't want to have, yeah, that makes sense. You wouldn't want to have one design replicated many, many times across one wafer. You'd want to have all of this IP shared on a mask because each wafer is getting a shot of that, of that mask. Exactly. Yeah. Yeah. Or probably being stepped multiple times. Yeah. Right. That makes sense. Okay. Yeah. Okay. Yeah. Huh. And then when they dice it up then, so the slicing and the dacing, it's just like they have to be able to, within the now larger unit cell, right? The lot of-

**Chris Gammell:** Which one is whose and then package them up so that I just get mine and not yours. That's right. Yeah. Okay. All right. That makes sense. And then what we've done with tiny tape out is like the next level down. Yeah. So in our one slot on an MPW, we have 250 slots.

**Matthew Venn:** So how long until I can buy a single transistor on a single wafer that I get delivered to my house? Well, if you'd have put in an order on- The finest artisanal NMOS.

**Chris Gammell:** Well, if you want to talk about the finest artisanal most NMOSes, and you're talking to the wrong guy. You want to talk to Sam Zalouk about that.

**Matthew Venn:** Uh-huh. That's right. Yeah. Yeah. And you got to hang out with Sam at Supercon, right? At Supercon. Yeah. I gave him one of my hats. I saw that. I saw that. Those are a fun- That is a fine hat. I like- Like I said, I like the culture that you're building around this. It's weird. It's fun. It's cool. I like it. Exclusive because it's difficult to understand. But it's totally like- But that's what we're trying to change. That's right. Exactly. And to this audience, the people that are listening right now, you could totally do this. Like, I think I could do it too. I'm just lazy. Yeah. You definitely- Yeah. You definitely could do it, Chris. Yeah. And one more time, can you give a pitch for like, why someone might want to learn this stuff? Like, just help people dream right now, Matt. Because you- Like I said, you know, we are Willy Wonka-izing this process. So who are the dreamers of the dreams? To quote Gene.

**Chris Gammell:** Yeah. Well, anyone that is interested to kind of know how deep the rabbit hole goes with how electronics and chips work, and anyone who thinks that open source is going to eventually dominate chip design, just like it's dominated software, and they want to be like on the early wave, now is the time to start.

**Matthew Venn:** Okay. I like it. Matt, is there anything else that we missed that we definitely should have mentioned? Let me look through my very organized list of notes. I mean, it is a really good list. I will drop other links. Matt sent me a bunch of links too. Like I said, like he said, he linked me to all of the relevant shows. Like, this is next level guest, folks. This is like, Matt has his stuff together. If I ever make a chip design, I dream of getting asked to be on the Zero to ASIC show. I have no reason to be interviewed on there, but if I ever am, I just, I can't even imagine- You're just like a special guest. Yeah, yeah. I'm just the tourist.

**Chris Gammell:** No, I think that's it.

**Matthew Venn:** I think it was, yeah.

**Chris Gammell:** We covered everything.

**Matthew Venn:** Awesome. Yeah.

**Chris Gammell:** Yeah. Subscribe to my YouTube channel and don't miss the X-ray tomography that we're doing at the Zurich particle accelerator next year.

**Matthew Venn:** Whoa. This year. Awesome. Awesome. Yeah. Yeah. Teaser. I cannot wait. I think if anyone's going to start anywhere, I will directly link people to the video that Matt did of 2022, like the recap. If you watch that and you're not excited about open source silicon, I'm going to say you're not enough of a nerd and you should introspect. You should get excited about open source silicon because of the stuff that Matt and all the other people in the community are doing. It's really, really exciting. Thanks, Chris. Thanks for being here, Matt. We'll talk to you soon.

**Chris Gammell:** Yeah. Cheers. Bye.

**Chris Gammell:** Bye.

**Chris Gammell:** Bye.

**Speaker ?:** Bye. Bye. Bye. Bye. Bye. Thank you.
