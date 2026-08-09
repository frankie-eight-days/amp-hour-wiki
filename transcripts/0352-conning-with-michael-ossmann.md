---
episode: 352
title: Conning with Michael Ossmann
url: https://theamphour.com/352-conning-with-michael-ossmann/
---

**Chris Gammell:** This is the Amp Hour Podcast. Released July 17th, 2017. Episode 352. Conning with Michael Osman. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Michael Osman of Great Scott Gadgets. Welcome back, Mike. How are you doing? I'm doing very well, Chris. It's a pleasure to be here, as always. Well, we always love having you on. We're going to talk a little bit of security and radios and all the usual stuff, I'm sure. But we're going to start with something you didn't know. Uh-oh. Oh, you have a HackRF subreddit. That's what we found out like five minutes prior to this. Right. That's exciting.

**Dave Jones:** To know.

**Chris Gammell:** Yeah. Look at all of the things you've spawned without even knowing about it.

**Dave Jones:** Yeah. So if anyone's wondering about why I never answer questions on the HackRF subreddit, because I didn't know it existed.

**Chris Gammell:** Which leads to the question, how do you interact with people for HackRF these days? I mean, is there a separate forum or is it direct or what?

**Dave Jones:** Well, there's a mailing list.

**Chris Gammell:** Okay.

**Dave Jones:** And there's IRC. Ah, okay. And that's pretty much it. We actually do probably the majority of our support via IRC.

**Chris Gammell:** Okay.

**Dave Jones:** Which for some people is really super convenient. And for other people, they're like, what's IRC?

**Chris Gammell:** And you're like, you damn kids, get off my lawn. Yeah, exactly.

**Dave Jones:** Yeah. So we do have like a link, a live link to the IRC from our website. So you can just click a link and have it in a web browser. So even if you have never used IRC before and don't have an IRC client installed or anything like that.

**Chris Gammell:** Oh, it's one of the web app things. Yeah. Yeah.

**Dave Jones:** So it's relatively easy for even somebody new to IRC to come chat with us.

**Chris Gammell:** I have to say, every time I keep trying, I keep trying to go back to it. I'm just like, oh, yeah, my IRC client's been running for four days and I haven't touched it. Oh, I guess I should do that. So I guess it's just like what you're used to, right? I mean, like that's, I don't know.

**Dave Jones:** Yeah, definitely. And, you know, we have multiple channels on Freenode. There's a HackerRF channel and an UberTooth channel and so forth. And, you know, we started using Freenode some years ago because Freenode makes services available specifically for open source projects. And we started using it mostly for internal stuff, you know, development and collaborating with other developers. But it kind of ended up being the primary way we communicate with users as well.

**Chris Gammell:** Well, if you're already there, why not, right? I mean, like if everybody's already in there, it's like, come on in. Or do you have separate channels for dev versus support? No, it's all one. Oh, it is. Yeah. So, well, hopefully it's not so much support traffic that you can't get anything else done either, right? Right. Yeah, it really isn't. Yeah. Yeah, I don't know. I just can't seem to keep locked onto it. But I guess there's a thousand things online these days, including Reddit and everything else. Yes. It's just you got to go where the people are. I remember I was trying to get a hold of Randall Munro at one point for like to be a judge of the Supercon. Or not Supercon, of the Hackaday Prize. Oh, right. And that's the only way to get a hold of him is IRC. Oh, no kidding. Didn't know that. Yeah. Well, he declined. Yeah. Unsurprisingly. Yeah. Yeah. But there is that. He did a comic about Slack, I think. And it was about like. Oh, yeah. Like doing like a bot that would tie over between Slack and IRC and stuff like that. And it's how it's people are going to be asking to tie into IRC for the rest of time or something like that.

**Dave Jones:** Right.

**Chris Gammell:** Yeah.

**Dave Jones:** I really like the one he did that was like sort of a Venn diagram of all the different ways that he communicates with different groups of people.

**Chris Gammell:** Yeah. I don't remember. Could you. Sorry. Can you keep going with that? I don't remember.

**Dave Jones:** I was just like, you know, there's this group that you communicate with via IRC. And there's this group that you communicate via Slack. And there's this group that you communicate with via SMS. And there's this group that you communicate with. Was there no crossover though? Twitter or whatever. And there's very little crossover. Yeah. Right. Right. But it was it was pretty interesting. Like how the diverse modes of communication that we have these days. And and the fact that you end up with relationships with people that are that often are exclusive to one mode of communication.

**Chris Gammell:** No, that is crazy. Because like you think about it, like I often think like, where the hell are people online talking about certain subjects? And it's not that they don't exist sometimes. It's just that you don't know where they are. Right. I mean, for the longest time, I was like, where like talking to people about KiCad. Right. I mean, it was like where I mean, there was the Yahoo mailing list. And then there was like, but then there was an IRC channel that I didn't know about. And and that's where some of the devs hung out. And that's where a bunch of users hung out and stuff like that. And and, you know, they're they're kind of everywhere there. They are spread out now, too. Obviously, it's a little bit more than it used to be. But but yeah, if you can't find them, then it's like, oh, it feels like a wasteland. But it's it's just that you're you're not looking behind the right curtain, you know? Yeah, exactly. Yeah. Well, how speaking of KiCad, how's your how's your KiCad these days? How what's what's going on with that?

**Dave Jones:** Oh, it's actually I haven't been doing a whole lot of electronics design in the last few weeks, but I've been doing a little and trying to get some other folks in the lab doing stuff.

**Chris Gammell:** Oh, yeah. You have you said you have interns.

**Dave Jones:** Yeah. How's that going?

**Chris Gammell:** It's going pretty well.

**Dave Jones:** We decided to hire an intern for the summer and we ended up hiring three. They're so cheap. It's a little crazy. But but it's worked out pretty well there. It's a good group of people and and they're doing some good some some good projects for us. Focusing on software development, though, not hardware.

**Chris Gammell:** OK. Yeah.

**Dave Jones:** We figured it would be hard to, you know, a to find people like, you know, mid mid undergrad level. Yeah. Yeah. Who could really help us with hardware design, especially when like the the just getting familiar with the tool chain, like getting familiar with. Sure. Right. Right. Right. Yeah. It takes a huge amount of time. And and we have so many software projects that we want to do or we have half finished. And we thought, you know, we could probably find we're more likely to find candidates kind of in that experience range who could help us with some software projects. So that's what we focused on. And we have three software developers for the summer.

**Chris Gammell:** Nice.

**Dave Jones:** It's been fun.

**Chris Gammell:** Do they do they have RF knowledge? Are you teaching that stuff, too?

**Dave Jones:** No, they don't. And they're learning a little bit, but not too much.

**Chris Gammell:** The they keep using the hack RF subreddit. Nobody answers.

**Dave Jones:** No, it's just that the projects we have them on don't really require them to be using using the tools. Yeah. In terms of like over the air stuff. So we have two kind of traditional college age students who are doing mostly Python development for us for a project that Dominic and I will be talking about a black hat coming up here. Nice. Currently. And then after a black hat, they'll be working on something else. I'm not sure what yet. And then we also have a more senior intern who came to us sort of out of the blue, who's a super interesting guy, Mike Nabarezny. He I can point you to his I should put it in the show notes. He has some really interesting resources on the 6502. Oh, yeah. So like if you find his 6502.org. Oh, that's his. Oh, cool. His website. Oh, cool. Yeah. And he has a bunch of other interesting, really interesting projects that he's done. But anyway, he's he's a much more senior software developer. He has a lot of experience. And he but he went back to school recently to focus on embedded.

**Chris Gammell:** Oh, nice.

**Dave Jones:** And he contacted us. He was like, I want to be a suburb intern and just do embedded development for you because I need embedded experience. And we're like, OK.

**Chris Gammell:** Yep. If you want to. And that, folks, is the way you do it. It won't always work. But especially with like small organizations where you can actually get a hold of the people. Yeah.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** It's like, oh, I'll work for peanuts. Cool. All right. Good. Yeah. Yeah.

**Dave Jones:** So he's he's doing a bunch of great fat development. Awesome. It's really good. And so we're trying to we're trying to give him projects that are all focused on embedded C because he's a super experienced Python and Ruby developer. He's probably a better Python developer than me or Dominic. But he but he wants to do more embedded projects. Yeah. Yeah. Yeah. So we're giving him embedded projects. Yeah. Yeah. That's cool.

**Chris Gammell:** That's great. That's great. How's how's the how's the great fat going? I mean, pretty well.

**Dave Jones:** Yeah. We have a lot of software still that we want to do for it, but it's super close to being ready to ship.

**Chris Gammell:** And can you give people a reminder about what that project is if they haven't heard of this? I mean, we were actually looking at you got you and Dimitri were talking about that last time you were on, which is we went and looked and it was October of 2016. But right.

**Dave Jones:** Yeah, that was the last time I was on. It's a sort of general purpose hardware hacking tool, USB connected. The main idea is that it gives you a very large number of pins that you can control over USB. And architecturally, it's basically just a big microcontroller that's USB connected. And then it breaks out everything, all the different peripherals and everything out of that microcontroller. But we kind of envision it being used for things that are similar to the GoodFet of Travis Goodspeed or similar to the Bus Pirate that a lot of people know. And it has an expansion interface. So we envision having a lot of different expansion boards, kind of similar to Arduino shields, except the development model is that instead of doing embedded development, you're doing like you're interacting with it in a Python environment.

**Chris Gammell:** Hardware API, right? Yeah. Yeah.

**Dave Jones:** It also has a secondary USB port, so you can use it for some fun USB things like probing another USB host, stuff like that.

**Chris Gammell:** See, now this is, I mean, and this seems like it's almost thematic for GreatSket Gadgets. Gadgets, rather. It's like you guys are giving software interfaces to the real world, right? So it's either RF or, in this case, just physical interfaces for, you know, blipping digits or blipping bits, rather.

**Dave Jones:** That's really good. I'm writing this down because this should be part of our marketing. Software interfaces for the real world. Yeah.

**Chris Gammell:** I mean, and that's what, I mean, but like this is, this is the trends that I, that I see a lot as well, because it's like, you know, there's, there, there are gobs of software people. Hello to all our software listeners, right? It's like, there's, because there's, there's money in it and there's, there's just expertise around it. And there's, you know, there's all these things that need software. And so there's all these software people now, they want to get back into hardware or they need to do another thing, right? This is how you got started too, right? So people that don't remember your origin story, but it was like, yeah, you were trying to get Bluetooth access, right? From the software level. That's what Ubertooth was, right? Totally. Yeah. So I'm glad I, you know, I'll, I'll send you an invoice by the way, for that brilliant, brilliant marketing on the spot marketing.

**Dave Jones:** But yeah, I mean, that's just registered it with USBTO. So unless you've got it before me. Okay. Right.

**Chris Gammell:** Always register before talking to Osman. Okay. Okay. Cool. Lesson learned, you know, that will be an expensive one, but a lesson learned. Yeah, no, I mean, but I think that's, that's super powerful too. I mean, that's, that's the basis of what Arduino does that too. And, you know, you think about Raspberry Pi, anything like that is people just want, and they don't, now from my perspective, I know that they, most of them don't give a shit about learning how a transistor works until it's necessary. Right. It's like, I want to, I want to do a thing. And if there's a software interface to do that, it's going to be a lot faster to do that thing. And it's probably faster to just to buy, to buy the thing that gives me that interface. Right. Right. Right. Yeah. Right.

**Dave Jones:** Excellent. And of course, everything we do is open source hardware and we encourage people to build their own and modify things and get into the hardware design. But in reality, that's, it's such a small percentage of folks who want to do that, which is how we stay in business.

**Chris Gammell:** Right. Right. Do you have an estimate on what that percentage would be?

**Dave Jones:** Oh, maybe 1%. Really? Okay. Yeah. In terms of like, I mean, if I think about all the people who've bought an Uber tooth versus all the people who've built an Uber tooth, it's probably less than 1%. Yeah. They've actually built one.

**Chris Gammell:** But if you, if you, if it was a different pitch parts, that might be also, that might change the story a little bit, right? Maybe. Maybe not. Yeah. You're right. I guess people aren't building Arduinos as much as they're buying them. Right. So that's, that's large scale, simple stuff. So. Right. Yeah. Hmm. Well, you know, bully for you. That's good for business.

**Dave Jones:** It is good for business, but that doesn't mean I don't want people to build their own. It really does excite me when, when, when I meet somebody who shows me like one of my designs that they've built or done something interesting. Right. You know, made a variant of that's, that's super cool. Yeah. Yeah. Like that radio badge at, uh, yeah.

**Chris Gammell:** I was going to mention that, that, that had like, it was amazing. It was HackRF on it, right? Like. Yeah. How did that end up going? I don't know. Did we talk about that last time or the time before?

**Dave Jones:** Ah, we probably, we probably did talk about it, but I forget. Uh, but, but yeah, just for the people don't know, it was a, a variant of HackRF1 that was, um, that, that, that was put into the form of a conference badge for the chaos communication. And so low cost. Oh goodness. It was not low cost at all, but I mean, it became lower cost because, they got a lot of parts donated by chip vendors and. Which is the way to do it.

**Chris Gammell:** Right.

**Dave Jones:** Yeah, it totally is. And so they made 5,000 of the things and gave them away to people who came to the camp. And, uh, it was a terrific time. A lot of people were doing fun stuff at the camp and people continue today to use the, I mean, I was just chatting with, on IRC, like yesterday with somebody who was doing a project with a radio badge. Interesting.

**Chris Gammell:** Okay. So that's, that's always my question about badges. I, I, you know, because DEF CON is coming up, which we'll talk about here in a bit, but like also because super cons happening again and I'm helping with that and we're talking about badges and it's like, do people actually use these things after the fact? I, I, my thesis is no, but maybe it's just because most badges aren't HackRFs built in,

**Dave Jones:** you know, that, yeah, that's kind of my impression too, is that it depends a lot on the sophistication of the, of the badge and the, uh, generally the overall usefulness of the badge and what kind of support there is for it.

**Chris Gammell:** Yeah, true. And I guess having 5,000 in the field too, that just increases the number that are out there. So that's, you know, it's, if it's one, if it's 0.1%, you still have five people doing it then. Right. Right. Right. Yeah. Versus, you know, 300 badges, like, well, 0.3 people probably aren't reusing a badge, right? Right.

**Dave Jones:** And one of the nice things about the radio badge is that since it is based on our product that we support, uh, it's relatively easy, you know, and that, that increases if you, if you add up all the people who have other HackRFs, uh, the, the total number of people who have something vaguely similar that can help you out or collaborate on things is a very large group. Right. And, uh, and also the, the folks from the Munich, uh, CCC group that put the badge, the radio badge together, uh, they've continued to, to support the badge. Ah, okay. Yeah. Like a core group. Yep. Yeah. So it, it really has, has a, had a lot of momentum behind it for something that's two years old. It's pretty awesome that people are still using it.

**Chris Gammell:** Yeah. The tool chain is the same you're saying though too, for that kind of thing.

**Dave Jones:** Oh yeah. Okay. Yeah. And we've actually, uh, it didn't happen right away because the radio badge was, was kind of a, uh, a last, uh, there was a kind of a mad rush to get the, the firmware all working for it and everything. So it took us a while, but we did end up integrating and pulling all their code into the main HackRF tree. Oh, wow. Okay. So, so like it's the same code base. Uh, we all work together out of the same, uh, the same code base and, and, uh, you can download, uh, you know, the, the, or, you know, clone our Git repo and compile firmware for either the HackRF one or the radio badge.

**Chris Gammell:** Was it just like a hash to find or something?

**Dave Jones:** Yeah, pretty much. It's a little bit more complicated, uh, of a mod than, um, than it could have been largely because they, they made some changes just to accommodate the, what parts they were able to get donated.

**Chris Gammell:** Oh, I see. Yeah.

**Dave Jones:** Right. So it's a bit more, uh, there's a fair bit to the, uh, the changes that they had to make to the firmware. Right. Um, but we were actually like accessing different registers and stuff like that, right?

**Chris Gammell:** Like, yeah.

**Dave Jones:** Well, they have completely different chips, uh, in some cases, like they're, they're kind in the, in the analog RF section, like the front end mixer and frequency synthesizer are completely different than we have on HackRF one. So like the whole, all the stuff with tuning and, and, and configuring the frequency synthesizer and stuff like that, it is entirely different for theirs, but they, but they were able to fit it into the functions that we had already with hash defines and it works.

**Chris Gammell:** Nice. That's good. I mean, in my, my former days of, uh, you know, sustaining engineering, we would call that a bad idea, but, um, when there's a, you know, a willing group, then yeah, it sounds like it works.

**Chris Gammell:** Right.

**Dave Jones:** And the, uh, and the folks who created that badge and created that firmware are still active in the HackRF IRC channel, for example.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** So they're around and they're, they're, um, they help us out and every once in a while we'll make a change, uh, that we'll forget to test on radio badge and they'll tell us. Uh, so it works, it works pretty well. That's great. That's great.

**Chris Gammell:** So, well, speaking of badges, let's, let's, let's switch over to a conference mode because I know that you were always, I'm actually, I was surprised that we were able to chat. Um, it seems like you're always running around during conference season. So you've got a little bit of time at home, at least you are at home, right? You're not at the hotel.

**Dave Jones:** Yeah. Yeah. I'm at home for like a month.

**Chris Gammell:** Whoa. I know. Slacking off, Osman. What's going on?

**Dave Jones:** Uh, it's just that we have a lot of work to do to get ready for the next round of conferences. Yeah.

**Chris Gammell:** So you mentioned, uh, Black Hat and then DEF CON, which I'll be at DEF CON as well. Uh, excellent. What else is on your, on your docket in the coming days?

**Dave Jones:** Well, of course there's Black Hat and DEF CON and now B-Sides, which is a younger conference, but is also an excellent event that goes on that week in Las Vegas. Um, and, uh, Dominic Spill and I have various things going on at, at all three of those events actually. And, uh, then that's, that's kind of it for, um, for a little while. Oh, okay. I think my next conference after that will be Tour Con in San Diego, which this year, is in late August, has previously been for, for as long as I've been going, I think it's, it's always been in October.

**Chris Gammell:** Oh, okay. Yeah.

**Dave Jones:** Now it's going to be like the end of August or very beginning of September.

**Chris Gammell:** Luckily in San Diego, the weather is the same all year round, which is gorgeous. So it doesn't matter.

**Dave Jones:** Yeah. We want, the only difference is there won't, there will be fewer Halloween costumes.

**Chris Gammell:** Right. And more tourists probably, but yeah. Maybe. Yeah. But yeah, that's cool. That's great. Um, uh, what are you, do you reveal anything about what you're working on before you, or is it like you show up and you, you display what you've been working on as these, these are like hacks that you're just, um, that you're presenting or how does this work?

**Dave Jones:** So, uh, I only have one, um, well, I guess I have two talks. Uh, one is, uh, talk that Dominic and I are doing at Black Hat on spectrum monitoring tools.

**Speaker ?:** Cool.

**Dave Jones:** And the other one is one that I'm doing at the wireless village at DEF CON on reverse engineering, direct sequence spread spectrum radio systems. Ooh, that sounds cool. Uh, and that's actually a talk that I have given once before, uh, at recon in Montreal last month. And, uh, that's a kind of fun project. But, uh, the, the one we're doing at Black Hat is, uh, is on spectrum monitoring tools and, and we've, we've been doing a lot of software work. Some of it's firmware work for HackRF, but a lot of it is software work, uh, on the host computer side for like rapid sweeping, like using a software defined radio platform more like a spectrum analyzer. Yeah. Right.

**Chris Gammell:** Cause I remember, I remember Jared had that on the, uh, on the display that he built for it. I forget what that's called. The port-a-pack? Port-a-pack. Yeah.

**Dave Jones:** Yeah. So he has a really nice, uh, waterfall plot on the port-a-pack and that, but it, it's limited to a little less than 20 megahertz of bandwidth. Right. That's visible at a time. Right. So what we're working on now is sweeping across the full six gigahertz of tuning range. Yeah. Yeah. Yeah. And we can sweep across the, by, by doing the tuning in firmware instead of doing it on the host computer. Right. We avoid like the USB latency with every tuning command.

**Chris Gammell:** Right.

**Dave Jones:** And we're-

**Chris Gammell:** Normally you'd be saying like, okay, just for a simple example, send out one hertz, send out 10 hertz, send out a hundred hertz, right? Each time you have the overhead of all the USB stuff and then also getting the data back. Right. Right. So now what you're thrown into firmware, you say you send a sweep command with some kind of parameters and it just does that for you and then sends back a stream of data or what? Exactly. Okay.

**Dave Jones:** And, uh, so we're getting six gigahertz of sweep in three quarters of a second. Uh, so it's, it's like an eight gigahertz per second sweep rate, uh, which, which is kind of ridiculous for, um, like nobody's ever done anything near that fast before with kind of a general purpose. And how do you, how do you view the data then? I mean, like, well, that's exactly what we're working on now. Yeah. Uh, so we have-

**Chris Gammell:** This is the software interns, huh? Exactly.

**Dave Jones:** Yeah. Uh, they're doing little pieces of it, but kind of the, the main, the main, most, most important elements are things that we've done already. Uh, but, uh, we're trying to add some extra features and get it polished in time for black hat. Uh, but the, um, there are a few different tools available for actually visualizing that, that information. Um, one of them is, uh, a piece of software that we kind of found in the early days of working on this sweep stuff called Q spectrum analyzer. And it's a software tool that specifically designed for, uh, it was originally designed for RTL SDR. Okay. That makes sense. Yep. But it's specifically designed for using an RTL SDR as a spectrum analyzer. Uh, and since it's- But that's gotta be super slow, right? It is super slow. Yeah. It has a sweep rate. Uh, I don't even know what the sweep rate is, but it's like probably at least two orders of magnitude slower than what we have. Right. And, uh, but it's, it, it's still useful for some things. Right. And so we kind of took that and said, Hey, we can, we can fairly easily integrate that with our sweep method and, and make it go a whole lot faster. And so that was kind of the first tool that we had working. Cool. And, and that was pretty useful. We, we liked that a lot, but, uh, but it has, uh, the, but there are some other benefits to some other tools that exist or other methods of visualization that exist that we wanted to kind of take advantage of. And so one thing we've done is this crazy trick that, um, uh, is a little hard to explain because, uh, it involves the FFT and the inverse FFT. Uh, but of course these, these, uh, like the FFT, the fast Fourier transform is the algorithm that's, that's used to take the time domain information that comes over the USB cable from an SDR platform and turned it into frequency domain information that you like visualize in a waterfall or something like that.

**Chris Gammell:** I was actually just, uh, just, I just explained that FFTs are more specifically Fourier transforms are the entire reason behind, uh, the name contextual electronics. Oh, no kidding. Yeah. Uh, tell me more. Uh, well, I, I explained it, I was, I've been streaming lately, so I explained it on there, but basically the short version of it, and I may have explained it on here before, uh, is basically after three weeks of 40 hour homeworks in my signals class and not understanding what it was or why it was, well, they told us what it was, right? Going between time and frequency domain, but I didn't understand why that was important. And after the three weeks and I finally figured it out, I was like, why the hell didn't they just show us a spectrum analyzer? Right. That would have been context. So, and so many words, like, God damn it. Like, why didn't they do that? They should have just done that. That would have been, it was like, oh, that's why it's important right there. He's like, oh, a sine wave. Look, a sine wave, single line on a spectrum chart. Right. And now I'll go and do the math and I'll care about it. But God damn it. Like that was terrible. Yeah. Yep. So yeah. Uh, that's cool. So, uh, fast Fourier transforms and inverse fast Fourier transforms. So you're just talking about going between the two, between the two domains, right?

**Dave Jones:** Yeah, exactly. And so what we do when we're in sweep mode, we get a short burst of time domain samples at every step along a, a, a, a, a wide range of frequencies. And so each one of those bursts, we, we run the FFT on and we get some frequency domain information. Yeah. And then what, then what we do is we take an entire sweep worth of this FFT output and concatenate, concatenate it together as if all of those, all of those frequency domain bins had come from a single FFT. Okay. And then we run the inverse FFT on that. Wow. Okay. So what that, what that ends up producing, we're basically, we pretend that all of these frequency hops were captured simultaneously, but they really weren't. Right. Of course. Uh, and then, uh, but then we, we take the inverse FFT and that gives us a larger chunk of, uh, like simulated very high sample rate time domain samples.

**Chris Gammell:** Right. Cause what you really care about is you don't have all the data that's contained within each frequency hop, right? Cause each frequency hop has some encoded data in there, but you want it, you want it at least in the baseline, you want to know what the frequencies are and where it's hopping to. Right. Yeah. Yeah. But you know, do you know, do you know the order as well? I mean, don't you need that? Um, the order of hops? Yeah. I mean, it's algorithmic, right? Isn't it like, uh.

**Dave Jones:** I mean, we're all, we're kind of at this, if we're using this inverse FFT trick, which we don't all the time, it's just one trick we use for visualization. Uh, if we're using the inverse FFT trick, we're really just pretending that all of these hops happened at the same time. And that can result in some, in some artifacts. Um, but if you're kind of aware that that trick is in use, it's a super useful trick. And, and so we kind of, we just totally ignore the fact that they, they did not, they did not occur at the exact same time. Right. Um, but we combine them together and then we get this like, so if we're sweeping across six gigahertz, we get this simulated six giga sample per second time domain signal. Uh, except that it has, it has like a big gap. It's a, it's a very short burst of six giga sample per second. And then there's a little, then there's a gap to the next sweep. Yeah. And then there's another short burst at six giga samples per second. And because we have these, these bursts at six giga samples per second simulated, we can pipe them into all kinds of other tools that have the ability to do analysis or visualization, uh, of time domain signals.

**Chris Gammell:** Huh. Yeah.

**Dave Jones:** And, uh, and we found that this is a very useful trick for, uh, kind of, kind of wedging our sweep solution into a bunch of existing software tools for visualization. Oh, interesting. Yeah. Without having to actually modify those tools.

**Chris Gammell:** Got it. That's interesting. Yeah. So like the, the thing I wonder about is like, so when I was asking about visualization of this stuff is just, it's like a, it's a, what's it called? Dynamic range problem. Right? So if you're looking at six gigahertz and you see a spike at five gigahertz, if you're looking at the full spectrum of six gigahertz and you see a spike at five gigahertz, you don't necessarily have any detailed information about that spike. That's kind of the resolution problem, right? Or sorry, the dynamic range problem.

**Dave Jones:** Uh, I don't know. Uh, I don't think the dynamic range really, uh, I don't think there's anything different about the dynamic range that we get using this sweep trick versus the dynamic range we get using other methods.

**Chris Gammell:** Well, okay. So what I'm saying is, okay, so now assuming there's a spike at five gigahertz, right? You don't know if it's happening at 5.1 or 5 or 4.9, right? Because you don't have that range there.

**Dave Jones:** Oh, right. Well, we, we actually do, um, it, it may take more CPU time to, to process, to get that, um, that frequency, uh, resolution. But, uh, but we do have the data that, that shows us, um, I don't want to say arbitrarily narrow frequency resolution, but the, the, the amount of, the amount of frequency resolution we get is, uh, or how fine that resolution is, is proportional to the number of samples that we capture at every, at any individual hop.

**Chris Gammell:** Right, right. And then, but that's just a display problem too, I'm saying. Like, so, right. So if you're sampling, so the way I think about it, right, you're sampling zero, one, two, three, four, five, six gigahertz, right? Just saying at each frequency, you're outputting this frequency, you're seeing what comes back in terms of amplitude, you map it on a plot, right? Right. But in order to get resolution around the five, where you see the spike around five, you would need to, to then sample 4.8, 4.9, 5, 5.1, 5.2, 5.3, and then see, oh, well that energy is actually at 4.9 instead of five, right?

**Dave Jones:** Right. And that's actually, that's really related to the thing that we're working on now, the thing that isn't quite complete, but that we're hoping to show at Black Hat, is we're taking an interesting web-based SDR software tool called Shiny SDR, and we're modifying it so that it kind of has the ability to go back and forth between sweep mode and kind of normal capture, like narrowband capture mode. Right, right, right. And so you can, you can drill down into things really easily, and then zoom back out into sweep mode. Oh, cool.

**Chris Gammell:** And that will actually control the radio eventually as well, so it'll like just change the sweep frequencies? Exactly.

**Dave Jones:** Oh, yeah, that'll be really cool. Yeah, so that's, that's the, that's the part of this project that's still in progress, but, you know, we have a couple weeks left. We'll be fine.

**Chris Gammell:** Yeah, no problem. What are you trying to solve with this though? What do you, I mean, are you trying, so you mentioned spread spectrum, is it because of that? Is it the tools are insufficient for that or something else?

**Dave Jones:** No, that's kind of a completely different project, although maybe related in certain cases. Sure. But we've been doing kind of SDR within the security space for a long time. And, and when people from the information security world kind of learn about SDR, one of the frustrations that, that they often have, or what, or I should say, actually, one of the things they get excited about at first is that they think that this is going to be an easy way for them to start, start detecting and analyzing radio signals that they never had visibility to before. Uh-huh. So like, what if you're, you're in charge of security for, for a facility or something where you, you have a building?

**Chris Gammell:** What if you're at a conference and you're trying to look for the pineapples that are, are hanging out all over? Did you watch that episode of, uh, of Silicon Valley?

**Dave Jones:** Uh, actually, no, I haven't. Oh, okay. Uh, yeah. I, I stopped having a TV before that episode came out. Got it.

**Chris Gammell:** Right. But, uh. HBO, HBO now, man. HBO now. That's. Yeah. That's the way to do it. All right. Or your, or your local, uh, torrent if you, if you're, if you're.

**Dave Jones:** It's a good show, though. Yeah. But I know, uh, you know, I know what that episode was based on. Yeah. Right. Exactly. Right. But, uh, like, even going beyond Wi-Fi shenanigans. Mm-hmm. Um, there, like, we, we have pretty good tools in those, in the information security world for dealing with Wi-Fi. Um. Sure. Right. We don't have good tools for dealing with your random internet of things. Pirate signals. Wireless interfaces. Right. Right. Rogue devices. That's right. That somebody brings into your building.

**Chris Gammell:** It's not 900 megahertz. It's 800 megahertz. Bum, bum, bum. Oh.

**Dave Jones:** Yeah. Well, it's amazing. Like, just, just doing a simple variation like that. You could take some off the shelf, uh, really easy to detect, uh, an interface with kind of radio solution and make some tiny little tweak, like just run it on a different frequency.

**Chris Gammell:** And you say change the inductor and, uh, yeah.

**Dave Jones:** And you'd be amazed by, like, how blind people are to, you know, to it. Like, they'll never find it. Yeah. Uh, unless you use something like a spectrum analyzer or some kind of spectrum monitoring solution.

**Chris Gammell:** Yeah. But doesn't this throw so many false positives for people that are getting started where they're like, oh no, there's, there's a signal on three gigahertz. It's like, yeah, well, it's a satellite or whatever, you know, like. Absolutely. Yeah. Or, or like, that's your CPU clock. Yeah. Right. I mean, it's calm down, Fritz. You're fine. Yeah.

**Dave Jones:** And that, and so that's a real challenge for people who are new to this. If they, if they want to use these tools to try to detect like signals that shouldn't be there, uh, first of all, they have to have some way to get a baseline and detect signals that should be there. And so one of the things that we're really focusing on in shiny SDR is that, um, and our, our interns, Ellie and Jacob are working on this right now. Is enhancing the, the method of annotation that's available within shiny SDR. So you can.

**Chris Gammell:** Like an overlay of a, of a spectrum chart.

**Dave Jones:** Yeah, exactly. So you can map things out. And so if you find something and you figure out what it is, you can annotate it and then it'll show up annotated the next time you look at it.

**Chris Gammell:** Oh, there's no like, like encyclopedia lookup though, or anything like that.

**Dave Jones:** Well, we're kind of working on that side too, which is, which is being able to pull in information more easily from public data sources to have, you know, information about spectrum usage. Uh, so it's a combination of getting, uh, kind of open source intelligence, uh, like, uh, published information about spectrum usage. And then also combining that with, uh, you know, your own annotations that you, you can make. Yeah. Like this, this is something that we have in our facility and it's noisy at 900 megahertz and you can keep track of that thing.

**Chris Gammell:** Yeah. So that means at some point there's going to be like a, a, uh, annotated version of, uh, the annotated RF version of test post, please ignore. Is that kind of a, it's like, yeah, probably we know this device is crap. Please ignore it. It's fine. Yeah, yeah, exactly. Wow. That's interesting. So, and so this isn't, cause what I was thinking about is like, I thought you were talking about it in terms of spread spectrum, because one of the problems with that, as far as I understand it, is that first you have to know where all the hops are going. And then what you'd really want to do is like kind of camp out on those, on those hops and try and catch the information that's happening as it, as that goes. Right.

**Dave Jones:** Yeah. And there are, there are a few different forms of spread spectrum communication that are popular. And the one you're mentioning, uh, sounds like frequency hopping spread spectrum. Yeah. Right. Which is, which is what Bluetooth famously does. And there are a number of other systems that use frequency hopping as well. Um, and, but the other very popular method of spread spectrum is direct sequence spread spectrum, which stays on the same frequency the whole time, but has a really wide bandwidth, uh, signal. And, and so, um, you don't have to tune around to different frequencies, but you do have to capture kind of a wide range of frequencies all at once.

**Chris Gammell:** Oh, so you change your filter internally instead of changing your whole tuning front end type thing. Yeah, basically.

**Dave Jones:** And I mean, the way, the way that direct sequence spread spectrum works in a nutshell is it takes advantage of the fact that as you increase the data rate of a signal, like the number of bits per second that you send, the bandwidth of the signal, the width in Hertz actually, uh, is proportional to that.

**Chris Gammell:** So, so, so, so faster signal, tighter, uh, narrower bandwidth.

**Dave Jones:** No, faster signal, wider bandwidth.

**Chris Gammell:** Really? Wait, how does that work then? Doesn't that clog up the, that, that block that you're talking about?

**Dave Jones:** Uh, it uses more bandwidth if you increase the data rate of a signal.

**Chris Gammell:** Oh, interesting.

**Dave Jones:** So what, what, what people do to, to, if you're designing a spread, a direct sequence spread spectrum system, what you do is you artificially inflate the data rate. So instead of transmitting like one symbol for every bit, you transmit a whole bunch, like a big pattern of symbols for every bit, for every data bit that you want to transmit. And, and so it becomes like every time you want to transmit a data one, you transmit a long pattern of symbols. And if you want to transmit a data zero, you transmit the inverse pattern. And so you're constantly transmitting these patterns and the, and the pattern has a, a bit rate, well, we call it a chip rate, um, that is much, much faster than the actual data rate. And that means that the resulting signal has much, much more bandwidth.

**Speaker ?:** Interesting.

**Dave Jones:** And that makes it more immune to noise and interference because, uh, you don't have to capture one individual chip. You just have to sort of do a pattern match and recognize that something that vaguely looks like the pattern that represents a one occurred versus the inverse pattern that represents a zero. Okay. So it's, it's a completely different sort of technology than frequency hopping spread spectrum, but they both result in using a wider bandwidth in Hertz and the radio spectrum than you would use with, uh, uh, sort of a, uh, more naive, uh, narrow brand approach.

**Chris Gammell:** And so is that chip, uh, code? So if the code is, if I send Chris Gammell is one and Mike Osman is a zero, right? Is it like, is it? I don't like where you're going with this. What's that? You're calling me a zero. Oh, sorry. Mike Osman's a one and Chris Gammell's a zero. Yeah, you're right. I should have, I'm a terrible host. I should have, I should have made you a one. Mike, you know what? You are, you are a one. I'm sorry. You're a one too, Chris. Oh, thanks. But you know what? Now we don't have any data. So, all right. So Mike Osman's a one and Chris Gammell's a zero. And, uh, is the idea basically like, because I'm sending that faster and faster and faster, eventually that even though it looks like Chris Schmormer, that like you at least see the Chris. And so like, because not all the data gets through, it looks enough like Chris rather than Mike.

**Dave Jones:** It looks more like Chris than Mike. And so you, so the receiver knows that it was a one.

**Chris Gammell:** Interesting. No, that's really cool. Actually. That's, it's like data or information theory type stuff or what? Very much so.

**Dave Jones:** Yes. Uh, in fact, the, uh, the fact that bandwidth is proportional to data rate comes from, uh, the Shannon theorem.

**Chris Gammell:** Claude Shannon. That guy's a badass. Was a badass.

**Dave Jones:** Yeah, man. Yeah. Yeah. Yeah. So that's the, uh, the, the theorem that describes, uh, the theoretical limit of how much of channel capacity, like how, how many bits per second you can fit through a channel of given bandwidth at a given signal to noise ratio? Right. Right. Right.

**Chris Gammell:** Cause if you, if you, if you know, you're going to go really fast and what you do is a zero would be Chris Gammell is a one, but we're going to use his name as a zero. And then the one would be Mike Osmond's always a one. He'll always be a one folks. Come on. That would be like, you would just make the word longer, right? That's the idea.

**Dave Jones:** Right. Right. Yeah. The longer your word is or the longer your code is, uh, then the easier it is for the receiver to detect that pattern, uh, which means that you're more immune to noise and interference. Um, and you can have a signal to noise ratio that is extremely poor. In fact, oftentimes in these kinds of systems, you have a negative signal to noise ratio.

**Chris Gammell:** Really? Wow. Yeah. Yeah. That's crazy. And so, uh, doesn't that take, I mean, so I guess you're, you're clocking it through faster, but it's all going, I mean, radio is serial, right? I mean, like you're still, is that right? Or I guess you could have it, you don't encode it in the frequency. Do you?

**Dave Jones:** No, not typically. I mean, it is possible to have, um, um, uh, well, actually that's an interesting question. I never really thought about it.

**Chris Gammell:** I'm just wondering like when you, when you process this, this code word, as I'm going to call it, even though I know it's a chip or whatever, uh, is it going through a shift register or is it doing something more paralleled?

**Dave Jones:** Uh, so it's typically going through, uh, the correlation algorithm, uh, which is a multiply accumulate function.

**Chris Gammell:** Oh, like an FPGA. Okay. So then that probably has some, some parallel components to it. It might not be all parallel, but it's. Right.

**Dave Jones:** Because it's going to be analyzing like, uh, what it receives over a chunk of time. Sure. Uh, uh, like a, uh, not just an instance, but, uh, but a period of time. Yeah. Uh, to see if what it received during that window of time, uh, looks like the pattern that it's, it's looking for.

**Chris Gammell:** Right. Yeah. And then it outputs like some stochastic, like this is a 15% likelihood of being a one or a 99% likelihood of being a one or whatever. Right.

**Dave Jones:** And if the transmitter is clocking out these, these codes at a reg, at a periodic, uh, interval, then the receiver is going to start seeing that there are these spikes in correlation at that, uh, expected period and kind of lock onto those. This is, this is how GPS works by the way.

**Chris Gammell:** Oh really? I didn't know that actually.

**Dave Jones:** Yeah. Like the, you know, that those GPS, uh, signals come from satellites that are a long way away from you and they have a very limited power budget. Yeah. I didn't know that. And so there's like a bunch of them too. Like that's what's crazy too. Yeah. And so the receiver, uh, that's how they overcome the fact that they have such a terrible signal to noise ratio at the receiver is that they transmit, uh, every time they want to transmit one bit of information, they actually transmit 1023 chips. And the receiver is correlating to try to do a pattern match and detect, uh, those 1023 chips. That's cool.

**Chris Gammell:** And that's obviously done in, I mean, that's not done in FPGAs these days. There's custom silicon for that kind of stuff, but. Sure. What is that?

**Dave Jones:** But I've definitely seen it done in FPGAs, but. Sure. Yeah. Yeah. Yeah. Yeah. Or actually on host computers, like there, there's SDR software you can use to, to do GPS. Oh, cool. Receiving, um, or GPS simulation, which is a lot of fun.

**Chris Gammell:** Um, like, like messing with people's GPS or what? Uh. I guess you're not outputting the frequency that's necessary.

**Dave Jones:** Well, you could be, um, that's, that's become rather popular. Uh. Really?

**Chris Gammell:** Oh, that's like, that's like in Goldeneye. Oh my God, we're there. Yeah. Yeah.

**Dave Jones:** The normal people are, are, are steering the shifts off course now, huh? I mean, have you seen, uh, Pokemon Go?

**Chris Gammell:** Yeah.

**Dave Jones:** Sure. So, the, I'll just say that, uh, GPS simulation software for SDR became a lot more popular when Pokemon Go came out.

**Chris Gammell:** Those fat asses that don't want to get up and walk around. What the hell? Is that seriously why? Oh, yeah. Yeah. Wow. I mean, there, there are plenty of other uses for it. Never underestimate the depths of human laziness. And seriously, like, though, like Pokemon Go. Okay, I didn't really enjoy it that much myself. But, like, the fact, like, all the stories you heard about, like, I walked 14 miles yesterday and, like, people, like, losing 50 pounds because they're just, like, walking around playing Pokemon. Like, that's, that's great.

**Dave Jones:** That was pretty awesome.

**Chris Gammell:** Yeah. Except for the kid that walked, there was some people that, like, walked into dangerous places or off cliffs or something. That was sad. But, but otherwise, you know, healthy.

**Dave Jones:** You know, to a certain extent, that's going to happen just when people get out more. That's true. Right. Like, right. I wouldn't necessarily blame Pokemon for that, but. That's a good point. Yeah. Yeah. Yeah. So, there are a lot of interesting things that folks do with GPS. There was a really cool paper, by the way, a few years ago that was one of my favorite papers in the field of wireless security called GPS Software Attacks that showed, that showed how you could, like, spoof a GPS signal and cause that to affect a GPS receiver in some interesting ways. And, and what they did was they, they, they made a, the reason I like this paper is because they make a very good distinction, a very clear distinction between kind of a, a RF level attack versus a software attack. And in that, like, if you just think about GPS, GPS spoofing as an RF level attack, you can think, okay, I can make a receiver think it's somewhere on the earth where it's not. But if you go beyond that, you can use this technique to exploit software bugs in the GPS receiver. So, for example, they found that they could spoof a GPS signal that looked like it had an elevation of zero, meaning that the GPS receiver thinks it's at the center of the earth. And when they did this, they actually got a GPS receiver software to crash. Because it did like a division by zero or something.

**Chris Gammell:** Right, exactly. Or the QA team probably didn't think to check that kind of thing, right? Exactly.

**Dave Jones:** Yeah.

**Chris Gammell:** Wow.

**Dave Jones:** And so they found that there were these software bugs that they were able to exploit beyond just fooling the thing to think it's in a different location.

**Chris Gammell:** Jeez. It's pretty cool. Okay. Now here's an interesting loopback question for you. Since Great Scott Gadgets is enabling the software people to talk to the world, does this mean that software people are going to introduce more bugs into the real world because you're giving access to software interfaces to real things? Is that a concern of yours?

**Dave Jones:** Well, it depends on what you mean by producing bugs. Everyone who produces software produces bugs. That's just the way of the world.

**Chris Gammell:** I don't. Sure you don't. No, no. I just don't produce software, so that helps. Oh, okay.

**Dave Jones:** Yeah, there you go. Yeah. But the folks that I hang out with and who give talks at HackerCons and stuff, even if they're talking about vulnerabilities and things that they've discovered, it's important to realize that they're not breaking things. They're just pointing out how things were already broken. Hmm. Hmm.

**Chris Gammell:** This is part of the ethics conversation, I think, again, right? I think so. Yeah. When Fitz was on, we were talking about this stuff. Sure. Yeah, Fitz was on a couple weeks ago. Right. A couple months ago, whatever.

**Dave Jones:** Yeah. Yeah. Speaking of Joe Fitzpatrick, I think he mentioned the training that he's doing this fall, hardwaresecurity.training. Yeah. So, Dimitri. Dimitri was the salesman on that whole thing. Yeah.

**Chris Gammell:** So, anyway, I wanted to mention this because I joined their group. I heard. Yeah. So, now it's become like the hardware security mafia. Yeah.

**Dave Jones:** Yeah. So, and it's kind of a fun group because there are five of us and every single one of us has been a guest on the Amp Hour.

**Chris Gammell:** Oh, I know. I've taken, you know, I basically put that whole thing together, you know. Again, the invoice is in the mail, Osman. Okay. Yeah. Cool. Yeah.

**Dave Jones:** So, Joe Fitzpatrick, Dimitri Nodosposov, Joe Grand, Colin O'Flynn, and myself, we're all doing this thing. And one of the, it's in November in San Francisco. And so, these are classes that we've all done at various events in the information security community. But we just decided to put on our own event. And I think largely Joe Fitz was the ringleader of it and maybe Dimitri too. But anyway, the five of us are collaborating. And we, one of the things that, one of the recent developments here, apart from me joining that group, is that we have a call for papers. What?

**Chris Gammell:** Oh, it's turning into a conference. Don't do it.

**Dave Jones:** It's sort of a mini conference, but only for people who are attending our training. Oh, interesting. Okay. So, the way we're doing it is we're doing our trainings together over a four-day period. And we're all going to have lunch together. And during the lunch hour, we're going to have somebody give a talk.

**Chris Gammell:** Ah, okay.

**Dave Jones:** And so, if you want to give a talk, those are four slots, I think, to give a talk.

**Chris Gammell:** Ah.

**Dave Jones:** And if we select your talk, we'll let you come to one of our trainings for free.

**Chris Gammell:** Nice. So. This is like a raffle, but a raffle based on awesome papers. Right.

**Dave Jones:** Yeah. So, hopefully this means we'll have some really great talks from some cool people who want to come do our trainings for free. And so, if folks have interesting projects, especially projects that are hardware security related, then go to hardwaresecurity.training and you can pitch your talk to us and maybe get one of our trainings for free.

**Chris Gammell:** Nice. Well, I would be remiss if I didn't mention the conference that exists the weekend after your training. I'm going from one straight to the other. Yeah. Hackaday Supercon, which is up in LA. I'm down in LA, I suppose, from San Francisco, where you'll be. Yeah. We're looking for speakers as well. So, that was a good time last year. You didn't get it. No, you were at some other conference last year. Yeah.

**Dave Jones:** I couldn't go last year, but two years ago, I had a great time.

**Chris Gammell:** Oh, yeah. Because that was the one in San Francisco, right? Right. Yeah. That was excellent. Yeah. No, it's a good group and I'm excited about it. So, if people are interested, there are also CFP for that is out. So, cool.

**Dave Jones:** Yeah. That's going to be an interesting burst of travel for me. But, hey, San Francisco and LA are not too far apart.

**Chris Gammell:** I was going to say, at least it's not the desert for two weeks.

**Speaker ?:** Right.

**Chris Gammell:** Speaking of, so what should I expect from DEF CON this year? I actually was surprised there's no badge this year. There's no official badge, rather.

**Dave Jones:** Right. Well, I don't know what they're doing for, I mean, I assume they'll have something like a paper badge or something.

**Chris Gammell:** Yeah, whatever.

**Dave Jones:** But they, I guess, had some plans for an electronic badge that fell through.

**Chris Gammell:** Yeah, something that I saw the person who was doing, I think they had family things come up. So, I mean, it's not like I'm super, I was never that into those badges anyways. I was. Really?

**Dave Jones:** Especially during the years that Joe Grand was doing them.

**Chris Gammell:** Oh, sure. Well, I was never at those though. Yeah.

**Dave Jones:** Uh, those were in the years when I was just first getting interested in hardware. Uh-huh. And like, and getting to, getting to hack on that badge every year was a big part of how I got into hardware.

**Chris Gammell:** Really? Interesting. Yeah. Yeah. That was propellers usually, wasn't it? Isn't that what Joe usually uses? Propellers? Uh, he used. Sorry, not propellers, the parallax stuff though, right?

**Dave Jones:** Yeah, he's done a lot of parallax stuff. But in those years, like I remember a couple of, or two or three years that there were some, uh, free scale chips. Okay. Uh, like there was a, there were two years in a row where he used this free scale DSP chip. And, uh, that was super interesting. That was, that was really right around the time when I was learning hardware hacking and, um, and I did some stuff like I tried to compete in the, like the badge hacking contest, but I was a newbie and I didn't do very well. Uh, but like the second year he had that DSP chip I did, or maybe, yeah, I think it was the second year I did. Uh, I tried to turn my toy guitar into a, like a digital electric guitar.

**Chris Gammell:** Nice.

**Dave Jones:** Uh, and, uh, I never really finished that project. I only got as far as, as getting the built-in, uh, uh, stroboscopic tuner working, which, which was super fun. Yeah, no, that's great. It was like, I had an RGB LED under each of the six strings, like mounted in the guitar. Uh, and then the, the, the, uh, red, green and blue would flash, uh, in, you know, in a, one at a time at the rate that the string is vibrating or supposed to be vibrating. Uh, so you can see like a circle of these three colors kind of rotate around each other. Uh, like then they rotate faster, the further the string is out of tune. Right. Which is like how the old, the old tuners worked anyways.

**Chris Gammell:** Right. That was like the, yeah.

**Dave Jones:** Yeah. Yeah. So anyway, that was, that was one of my early, early hardware hacking projects was doing that with one of Joe Grant's, uh, DEF CON batches.

**Chris Gammell:** Well, that is, I suppose, is a vector for software people to get into hardware. So I can't, I can't argue with that. Yeah. Yeah. I saw that new, uh, I, I have to say I'm in love with the, uh, the, uh, and, and not XOR, however you say it. Yeah. That's one of the groups they, they have, they did Bender last year. The Bender. Yeah. Yeah. And this year it's Bender though, as, uh, as the doctor, not as a doctor. As, as, uh, Hunter S. Thompson in Fear and Loathing. Uh, so he's got like the cigarette coming out of his mouth. He looks like Hunter S. Thompson. So it's, it's just really good design. I love it. It's so, it's so funny. So. Nice. Yeah.

**Dave Jones:** Uh, yeah. Yeah. There's going to be a, a lot of interesting stuff at DEF CON, of course. Of course. Anything in particular you're looking forward to?

**Chris Gammell:** That's the thing. I, I, I, I know I'm going now. Um, I, I know it's in a different venue than before, so that's kind of interesting. I hate Vegas. Uh, that's the thing. Oh yeah. I really, really don't like Vegas. And, uh, but I want to go to Vegas for about 24 hours.

**Dave Jones:** Sure. Yeah. Right. At the end of like day nine, I'm pretty down on Vegas.

**Chris Gammell:** I mean, just like the sound of slot machines really gets me.

**Dave Jones:** Ugh. Mm.

**Chris Gammell:** Yeah. I don't like it. Um, and I should say, I, I love gambling. That's part of the problem. Like, like, oh, I hate losing. Uh, that's the, that's the other problem. Uh, so anyways, yeah, I, I just don't, I don't like going there anymore. Um, but yeah, so, uh, I guess I'm interested. I'm going to go to hardware hacking village. I don't think I'm going to do, I, I was talking to Crux about, uh, the dark net badge and dark net as in general, I didn't quite get that in previous years, but it seems like that's actually an educational program. Like it goes, it takes you through. Right. What, like, what, what does it do? Like soldering? And then is there any SDR stuff or no?

**Dave Jones:** Honestly, I've never done it. Okay. Um, but it looks super cool. Yeah. Uh, and they've been doing it for a few years now. Um, maybe three ish, something like that. And, um, and I know that there's a series of challenges. Uh, and I think they're going even kind of bigger this year because it seems like they're starting some, I'm seeing some things on Twitter that like, uh, the there's, they're starting the challenge even before DEF CON starts, I think.

**Chris Gammell:** Oh, really? Okay.

**Dave Jones:** Uh, so it looks really interesting. Uh, I would definitely recommend people check that out because it, it, it relates like hardware hacking and software hacking and kind of, uh, privacy and, um, dark network kind of like, uh, covert communication. Right. Right, right, right, right. Yeah.

**Chris Gammell:** And it seems, it seems like it's like education, but that's the secondary thing that happens. It's more like people are doing it for the challenges and to get through it. Um, and I guess that's kind of like how I've started to view DEF CON as well. It, it almost seems like it's like, uh, like an MMORPG or whatever that's called, whatever, whatever, uh, uh, uh, World of Warcraft is right. Where you have like, you have all these different missions going on anyways, right. You can't, you can't do all of it. You can't go to all the talks. You can't do all the demos. You can't, you know, do everything there, but most people just pick one and focus on it that year. Yeah. Like, uh, I remember like Alvaro, he did that. Are they still do laser shooting or no? Like there was like robots that were, uh, target practicing or something. Right. Yeah.

**Dave Jones:** Alvaro was really into that. Um, and I don't recall, uh, seeing it. I don't know if they're still doing that, but, um, I wouldn't be surprised at all if there's still a, uh, robot auto targeting challenge of some sort.

**Chris Gammell:** Yeah. And so, I mean, but even like, so like hardware hacking village kind of stands on its own now as well, right? Yep.

**Dave Jones:** That's a thing. Uh, so I, I sometimes hang out in the hardware hacking village, sometimes hang out in a wireless village. Um, there's an interesting, uh, thing that some hardware folks might be interested in, which is the, uh, the ICS village, the industrial control systems village.

**Chris Gammell:** Oh, I'm definitely going there.

**Dave Jones:** Yeah. Yeah. That's a cool, that's a cool program.

**Chris Gammell:** Oh, Dimitri was doing a bunch of stuff with what that was, isn't he? Like, wasn't he consulting on ICS type stuff?

**Dave Jones:** Uh, yeah, he's definitely done a lot of that kind of work.

**Chris Gammell:** Uh, and, and personally, I think, I think that stuff is super important because, well, first off, I've worked, I've worked at an industrial controls company and I know I've heard conversations and I've, the security is not a huge focus. Let me just say that. And it should be because it's like, like controls your water and your power and your, you know, your sewer and like everything is, you know, SCADA systems are big and, uh, yeah, there's a lot of money and or problems there. So.

**Dave Jones:** Yeah, definitely. It's a, it's a major area of, of focus for the whole hardware security community. Yeah. Definitely.

**Chris Gammell:** What about, um, automotive? Is there an automotive village or no?

**Dave Jones:** Uh, you know, I don't recall if there's an automotive village, uh, but there will certainly be a talk or two on automotive stuff. Yeah. Uh, in fact, uh, there's one, um, let me see if I can find it here. Um.

**Chris Gammell:** I was going to say, how do you, how do you pick out your talks and stuff too? Like, because there usually are pretty big lines for talks and stuff. You usually have to get their early lineup, that kind of thing, right?

**Dave Jones:** Yeah. Yeah. Yeah. So anyway, this one is called driving down the rabbit hole. Um, I like that. By some folks that I know in, um, from Portland, uh, Mickey and Jesse and Alex, uh, Alex, actually is one of the chip sec guys. Oh, cool. Um, and anyway, they're doing a talk on, um, kind of automotive security research that I'm looking forward to, but, uh, I choose talks. Well, I, uh, one of the problems with DEF CON is also one of the great things about DEF CON is that there's so much going on that it's sometimes hard to know what you want to do. Uh, and like, you cannot see all the talks. And if you even try to see a good number of talks, then you'll miss out on a bunch of other interesting activities. And so you have to, you have to kind of accept the fact that you're not going to do it all and just find one or two things that really interest you and roll with that. Um, and if that's going to talks, then great. Um, and, uh, so oftentimes, and also I have a lot of things going on. Um, so like I might have a talk or I might have, uh, uh, I'm not doing a, uh, regular talk at DEF CON this year, but I'm doing a talk in the wireless village. And I also am showing a couple of things at the DEF CON demo labs, uh, which is like a, uh, you know, a couple, a couple hours where you have a demo table to show people things.

**Chris Gammell:** Oh, cool. Okay.

**Dave Jones:** And so I'm doing those things and maybe some other things and I have other things going on in Vegas that week. So like a black hat.

**Chris Gammell:** And so it's just be in your room napping at some point. Exactly.

**Dave Jones:** It's a busy time and I'm there for 10 days. And like, sometimes I just have to say, you know what this afternoon I need to go hang out by the pool.

**Chris Gammell:** Yep.

**Dave Jones:** Uh, and that's totally fine. But, um, but I do like to try to see some talks and, and it is hard to get into talks sometimes. And this may change depending now that it's in a bigger venue, it might be easier to get into talks, but I'm sure it'll still be hard to get into some of the more popular.

**Chris Gammell:** There will at least be long lines at the very least, right?

**Dave Jones:** Probably. Yeah. Uh, but there's a great trick. If you are staying in the conference hotel or know somebody who's staying in the conference hotel, DEF CON has done this for many years. There's, uh, this wonderful thing called DEF CON TV where they give a live feed of all of their lecture halls on different, each one is on a different TV channel that you can get in the hotel room. And so.

**Chris Gammell:** Did you see how much it costs to stay at the frigging Roman village, whatever they call it?

**Dave Jones:** I bet you know somebody who has a room at Caesars. Got it. Caesars. So, so what you do is you like offer that person beer and you say, let's go hang out in your room and watch these, these talks that I really want to see.

**Chris Gammell:** It's like, Hey, let's go hang out in your room. I brought beer. Oh yeah. I'm sorry. I'm sorry.

**Dave Jones:** That was Dominic. Constantly gives me shit about that because, uh, like the, the way we, we met on the internet

**Chris Gammell:** and like, uh, unintentional DEF CON dating. That's what it is.

**Dave Jones:** The first time we met in person, like pretty much the first thing I talked to him is, Hey, you want to go up to my hotel room so we can work on our talk for tomorrow? And like, he's, he's always reminding me that, uh, that like the first thing I did when I met him was invite him to my hotel room.

**Chris Gammell:** Solicit him for, for, yeah. Yeah. Yeah. Yeah. Oh no, no. That's I, I, I got some of the creepy looks and I'm like, yeah, no, no, no. I'm me, me and my co-host have never met. So I'm flying down to Australia to meet him. Right. Okay, Chris. Yeah. Well, hope you don't get hacked to pieces. I didn't. Dave's, Dave's fine. He's fine. That's good. I'm glad you're still alive. Yeah, exactly. Me too. You know what? Me too. I'm actually a ghost. Oh no.

**Dave Jones:** I haven't actually seen you in person since then.

**Chris Gammell:** That's a good point. I, I might, I, I don't even know if I exist. Come on, man. Yeah.

**Dave Jones:** Uh, is there, look for talks that you want to see. And if you're concerned about actually getting into them, see if you can catch them on DEF CON TV or catch them, you know, when they're published online afterwards.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. Although that, that has a hazard that you might forget.

**Chris Gammell:** Sure. Right. Um, what about, so this is, I'm looking at the main DEF CON schedule. Is there a separate schedule just for like the talk you're doing at like at, uh, Harbor Village? Is there, does Harbor Village have its own site?

**Dave Jones:** Hardware Village. I don't know. Um, they at least have a forum in the DEF CON forums. Okay. Um, I don't know if they have their own website. Uh, the wireless village has it, which is where I'm doing a talk has, uh, a site, which is wireless village dot ninja. As you do. Yeah. Uh, and the schedule's up there. There are some interesting talks going on there. And in addition to talks, uh, one of the, one of the highlights of the wireless village is that they have this wireless CTF, which is a, um, a game, like a competition that goes throughout the weekend. That's a whole lot of fun. I definitely recommend people check that out. And, um, yeah, there, there are all these different things going on and they're not necessarily all going to show up on the DEF CON website.

**Chris Gammell:** Right, right, right, right. And that's one thing that, so like last time I went, I was kind of just like, oh, I'll just kind of see what happens. And it felt like I, uh, I missed some things just cause I didn't plan at all. And this year I'm going to plan a little bit better and try and be at certain places. Like I would walk in the heart, the, the hacking village. Right. And it'd be like, there's like no one in here or there's nothing going on. Right. And so it just, it was hard to tell when there was activity in certain areas. So.

**Dave Jones:** Yeah. Yeah. Yeah. It definitely is a good idea to go through the schedule and, and look for things ahead of time. So you, uh, you know, you have the opportunity then to pick out the things that are most important to you to find. And, and if you, if you do one or two things that you're really excited about and then you wander the rest of the time, you'll probably have a great time.

**Chris Gammell:** Yep. And I did find the hardware hacking villages, dchhv.org. So that is just listening and not clicking on link. We'll have all this stuff in the link in the show notes too. So.

**Dave Jones:** Fantastic. Yeah. Oh, I forgot. I was just looking at the, um, DEF CON schedule as we were talking here and I forgot that, uh, Nate is giving a talk, um, from SparkFun. Oh, really? Cool. At DEF CON this year. Open source safe cracking robots. Oh, that sounds hilarious.

**Chris Gammell:** Yeah. Yeah. Uh, well, we've had, uh, you know, a decent number of, of security people on the show before, so hopefully they'll all be there.

**Dave Jones:** Um, yeah, I know Joe's giving a talk, uh, Joe Fitzpatrick and, um, uh, let's see. I'm not sure how many of your other former guests, uh, I know Dimitri said he wouldn't be there, but, uh, Joe, uh, Joe Grand is usually there, but I don't know if he has a talk. Uh, Colin O'Flynn has a talk at, uh, Black Hat that looks pretty good. Yeah. And, uh, and that's, um, also happens to be on, uh, on locks, not safe cracking, but electronic door locks.

**Chris Gammell:** Oh, cool. Uh, like, uh, those, uh, like Lockatron and stuff. Yeah. Stuff like that. Oh, cool.

**Dave Jones:** So he's doing some kind of attacks on those, uh, that I presume uses side channel analysis. Right. Uh, since that's his area of expertise.

**Chris Gammell:** The thing is about electronic door locks is even better than side channel analysis. Usually side window analysis usually, uh, you know, lets you into the place faster. Yeah. Yeah. That's interesting. I don't know. It's yeah. Are you, um, are you going to, do you bring, do you like, do you watch the spectrum as you're there? Like, do you ever do stuff like that or no?

**Dave Jones:** Not much. Uh, unless I have a particular thing going on, like I'm working on a contest or something. Gotcha.

**Chris Gammell:** Yeah.

**Chris Gammell:** It's, I, I, the, I've been watching all these badges come out and it's like everybody threw an ESP 8266 on there. So I think it'll be extra interesting watching, watching what happens and just in terms of like traffic on the networks and stuff like that, there will be a lot of, I think there'll be a lot more small devices on the network or, or even probably more likely, you know, outputting their own, uh, access point information. Um, so it'll be, it'll be interesting to see all that stuff this year and in subsequent years is there's just, you know, wifi chips are all over the place.

**Dave Jones:** Yeah, totally. Yeah. Yeah. It's kind of amazing how, how that has exploded in the last couple of years.

**Chris Gammell:** Are you doing anything with those chips or no?

**Dave Jones:** Not currently. Uh, there, there, there are some fairly limited options I think for using those really low cost wifi implementations, uh, to do things that are more interesting with wifi, like, uh, raw frame injection and monitor mode and stuff that, that folks can do with off the shelf wifi cards and a laptop, for example. Oh, gotcha. Okay. So for, as a security researcher, those parts aren't particularly interesting except in the way that you mentioned that they kind of affect the overall landscape of what wifi devices are out there.

**Chris Gammell:** Right. Right. Right. Yeah. There'd be a lot of tiny, tiny honeypot set up, right? Yeah.

**Dave Jones:** That's entirely possible. Yeah.

**Chris Gammell:** It's like, Oh, I attacked this device and there was barely a file system on there. Yeah. Yeah. Yeah. And of course I should, I should say that I'm some, for some reason I'm thinking about like, I mean, not some reason I'm, I, I will be on VPNs and you know, all that stuff. I don't know if there's actually ever any reason to worry about that. I know that I've read, I've read in both directions. It's like, don't, don't bother, you know? Yeah. But then there's always, yeah.

**Dave Jones:** People aren't going to earn their Oday on you at DEF CON. Right. Most likely. Probably not. Right. But you do need to take, you know, precautions that you would take anywhere. Certainly.

**Chris Gammell:** See, and that's the big difference. I think Fitz mentioned that too, that he was talking about the, oh yeah. Cause he mentioned he turned off his VPN to be on the show, which is, and obviously you have as well. Cause your audio quality is very good. Osman is vulnerable. Get him. I've been attacking your network this whole time. Mike, you never saw me coming. This is, this is for stealing that phrase that I gave you. Yeah. But I mean, yeah, you probably should be on VPNs these days and yeah. You don't do like Tor stuff, do you? Occasionally. Really? I never, I never did that. I mean, I've done VPNs a lot, but never Tor. So I never quite figured that out.

**Dave Jones:** Um, uh, I think that or is very interesting. I'm, I'm more interested in it from an academic standpoint than I am as a user. Uh, what, in what way? Um, well it's like, no one's really been able to prove one way or another, whether or not, um, whether or not it's possible for Tor to really work. Like, I mean, Tor does, Tor does work to a great extent. Right. But to what extent?

**Chris Gammell:** But until it's been broken and until someone's like, nope, I broke it. You don't know what the limits are, right?

**Dave Jones:** Well, I mean, uh, there's a, there's a theoretical problem that is kind of more interesting to me than the practical problem, I guess, which is like, is it, is it possible in theory to actually anonymize internet traffic? Uh, just like going back to information theory again? Yeah, very much so. Um, but, but more focused on like, if, if you assume that your, um, if you, if you assume that your adversary has the ability to monitor the network in multiple places, then, uh, it's, it's very, very difficult to come up with a method that would, that would kind of make your internet traffic immune, uh, to being detected or being picked out as being yours. And, um, it, it's an interesting, it's a very interesting problem, I think.

**Chris Gammell:** But it's like if, so if, uh, a bad actor was hanging out at McDonald's and at Burger King and I'm wearing a mask that makes me look different, but then they see the guy with the same mask at the McDonald's and the Burger King, you're saying that eventually they're just going to follow the guy with the mask back to his house.

**Dave Jones:** Is that kind of the idea? Exactly. Yeah. Yep. Yeah. That's, that's basically it. that, that, that it's, there's a lot of ability to kind of correlate, um, different events at different times at different places with each other. Right.

**Chris Gammell:** And, and the problem seems like it's like, oh, well, who would do that? Or we don't have enough processing power for that. But at a certain point, certain state actors probably have more than enough of both. Right. Right. Exactly. Oh, uh, as much computer power as you can buy. Sure. We've got that. We've got stuff you don't even know about.

**Dave Jones:** Yeah. Yeah. Yeah.

**Chris Gammell:** So anyway, I think Tor is really interesting.

**Dave Jones:** I'm just not a regular Tor user. Right.

**Speaker ?:** Yeah.

**Dave Jones:** But, uh, you know, getting back to, uh, Vegas, there's a lot of interesting stuff going on, not just at Defcon, but also at Black Hat and B-Sides. Mm-hmm. Um, in particular, a whole bunch of interesting hardware related things are being presented at Black Hat this year. Okay. So I would recommend that people check that out. Um, not just that talk from Colin, um, but there are some interesting talks on things like, um, here's one on breaking radiation monitoring devices. Uh, here's one on...

**Chris Gammell:** As you do, right? Of course. Why wouldn't you? Here's one... You know what I need? I need more, uh, gamma rays. Yeah, totally. Alpha particles. Whatever.

**Dave Jones:** Uh, there's a really interesting looking one on, uh, from some Chinese researchers on attacking, uh, MEMS sensors with ultrasound. Oh.

**Chris Gammell:** So like you can... Like vibrating the accelerometer out of a shell or something like that?

**Dave Jones:** Well, it's like, um, I, I, I haven't read anything from them yet, but I would guess that they're doing things like, um, by introducing, uh, an ultrasonic frequency, uh, you can cause the MEMS sensor to detect something at a much lower frequency to erroneously detect something at a lower frequency. Right.

**Chris Gammell:** It's like a sampling problem. What's it called? Aliasing. Aliasing, right. Yeah. Yeah. So... Oh, cool.

**Dave Jones:** Aliasing may be one of the approaches that they're using. Uh, I'm not sure. Uh, but it's, it's certainly, uh, you know, something that they probably considered at least. Um, so I'm really interested in, in that one. And there are a whole bunch of things. There's, there's one, um, uh, from Marina Crotofill. I don't know if I pronounce her last name correctly, but she's a really cool, uh, hardware hacker and she is doing something on, um, uh, kind of maybe vaguely related to that in that ultrasound thing, uh, that has something to do with sensors in fluid and how she's able to introduce bubbles via cavitation, uh, that mess with the sensors. Uh, so there are all kinds of weird, uh, esoteric, uh, hardware things that are not necessarily just your traditional, um, traditional hardware hacking where you're like interfacing with a piece of electronics, but, but things where you may be taking, exploiting some kind of physical process, uh, to interfere with or affect the behavior of some kind of system.

**Chris Gammell:** Right. Yeah. If you can't interrupt the bit stream of the sensor, just change what's the sensor sensing, right? Exactly. Yeah. That's cool.

**Dave Jones:** Yeah. There was a really cool, uh, couple of talks. I think Marina actually contributed, uh, to this research, um, uh, by a Russian researcher, um, that I met a couple of times last year. Um, and, uh, he, um, he did, he did some really interesting work on, uh, the, just focusing on, uh, analog to digital converters in sensors. And, um, and like, there are a lot of people who've done work on how to spoof different types of sensors, but, uh, but this, this researcher, Alexander Bolshev, uh, had done, he, he sort of reduced sensors down to their most important element, which is usually an analog to digital converter. And just like focused on that, like what ways are there fundamentally to fool analog to digital converters?

**Chris Gammell:** And, you know, like not, not all sensors are digital output. I'm just saying. Well, that's true. My analog internals are screaming right now. Yeah. Okay. You're, you're right. Right. But yes, I understand what you mean. Like you're saying that if you, if you attack that part of a digital sensor, it's, it's good.

**Dave Jones:** The interesting thing is if you figure out how to defeat an analog to digital converter, then you figured out how to defeat a huge range of sensors that use analog to digital converters, not just one type of sensor.

**Chris Gammell:** Hmm. So is it like, yeah, I guess, but it wouldn't actually be like an on hardware attack you're saying, right? It would be like messing with the ADC externally.

**Dave Jones:** Right. And so like the, the, um, aliasing sort of attack that I mentioned earlier with the ultrasound, that, that's something that can affect, uh, a wide variety of systems. And so. Right.

**Chris Gammell:** And you could probably do that outside the package, right? You vibrate the whole package at some frequency and that messes with the internal, uh, silicon and stuff. Exactly.

**Dave Jones:** Um, well, it may not, it may not necessarily, uh, have any physical effect on the silicon, but like if they haven't done their, uh, if they haven't sanitized their input properly, as we say in the security world. Um, and in this case that means by using good, uh, uh, anti-aliasing filter, uh, then you might be able to like vibrate a piece of equipment. I mean, just off the top of my head, let's say a centrifuge, um, at a very high rate that would not be detected by a sensor that is expecting to detect vibrations at a lower rate. Right. Yeah. Or, or you may be able to vibrate it at a high rate that makes it appear to be a vibration at a lower rate. If that's what you want to achieve.

**Chris Gammell:** Right. Yeah. It's like you want it to shut down. So you. Right. Yeah. Right. Interesting. Very interesting. Hmm. I suppose you need to still get to the, to the physical thing though, which is sometimes sometimes a problem, sometimes not. So yeah. Yeah. Yeah. Well, cool. Well, it sounds like, uh, quite, quite the, uh, quite the lineup coming up for, for all these things. And it's good. I mean, it's good that there's, there's, there's more interest in general. I'm sure you're, you're seeing lots of sales on the, the, the hardware side of things, people wanting to access hardware and RF and stuff like that. Right. So these are all good things for the hardware community. It seems like.

**Dave Jones:** I think so. There's definitely a, a, a, a growing, growing interest in hardware from the security side and, uh, maybe a growing interest in security from the hardware side. I'm not so sure about that.

**Chris Gammell:** I thought about it more than I had in the past. Um, yeah. You know, I talked to, to, to y'all, y'all more often than, than most maybe, but that doesn't mean that people listening aren't also thinking about it now. Uh, we'd love to hear from people if they are, if they are thinking about it more than they used to, um, I think it's probably really interesting is like the time when you really start to see that kind of change happening. It's like, if an executive is like, well, are we thinking about X, Y, Z that could happen? You know, if there's actual like people thinking about it as the products being designed, that's probably the biggest indication that it's, it's important to companies and they understand the continent. Usually it's only done when there's understanding of the consequences of not doing it. Right. So, yeah.

**Dave Jones:** Well, and that, and we've seen that across various industries that, you know, of course, first from the software industry, because this happened like more than a decade ago, but, um, you, you'll see an industry that kind of goes through the learning curve of, oh, our, our stuff is broken and we maybe should fix it. And how can we improve our security practices? And, and there's this whole learning curve. Um, and we're seeing that now in all kinds of industrial settings. Um, in particular, I know a lot of people who are focused on information security in the automotive industry.

**Chris Gammell:** Yeah.

**Dave Jones:** Uh, 10 years ago.

**Chris Gammell:** Recent stuff. Right. Yeah.

**Dave Jones:** They did not have those people 10 years ago. Right. But now they do. Uh, also the medical device industry, uh, the, um, the industrial control system industry, like all of these groups have security problems and they're also working on security solutions. And there are a lot of, uh, there are a lot of opportunities I think, uh, to kind of get into that, those, those industrial kinds of, uh, hardware security kinds of spaces these days. Right.

**Chris Gammell:** One, it, it almost seems like it's, I mean, it doesn't need to be a mature industry, but it does seem like that's once the industry and the stuff in that industry are prevalent enough, then they become attack vectors for, for bad actors. Right. And then it's like, okay, now it's worth, I mean, it's always worth thinking about it beforehand, but like there's actual consequences to not thinking about it at a certain point. So yeah, it's, that's why it seems like it, it, it usually goes to more mature industries because the hard part is getting the thing out there in the first place and then people start to break it.

**Dave Jones:** Yeah. Yeah. Yeah. Ooh, I just thought of something. Okay. Total change of subject. Sure. Did you see the article about Hacker F1 in the Daily Mail? I did not. Oh, it was amazing. Okay. What was it? It was this, this total hit job on.

**Chris Gammell:** In the Daily Mail? No. No way. I know.

**Dave Jones:** It's pretty, it was pretty hilarious. Uh, and, uh, so they did this article, was it a couple months ago? I think, uh, a hacking gadget that is a car thief's dream. And, uh, I think the best thing about it was the photographs that they took. Yeah. Uh, they took these amazing pictures of like the hacker in the hoodie breaking into cars. Oh my God.

**Chris Gammell:** I just saw it. Yep.

**Dave Jones:** Yeah. Isn't that phenomenal?

**Chris Gammell:** It's so bad.

**Dave Jones:** It's, it's horrific. I mean, it's just the worst thing ever. It's, but it's hilarious. Uh, yeah. Wow. Yeah. I particularly.

**Chris Gammell:** They have him wearing a hoodie, holding a laptop with the Hacker F on top of it. Yes. Like, and then opening the car door like, oh, now I can get in. Right. Yeah. You know, the brick also works. The brick also works.

**Dave Jones:** Yeah. Well, we, we, uh, we have discussed that at great length. Like the easiest way to break into a car into Hacker F is to put your Hacker F in a nice, uh, sturdy aluminum enclosure and throw it at the window. Let's slam it. Yep. Yeah.

**Chris Gammell:** Oh, wow. In 2015, more than 6,000 cars and vans were seized across the Capitol by gangs using key fobs that bypass vehicle security systems.

**Dave Jones:** Which has nothing to do with Hacker F.

**Chris Gammell:** That's right. Exactly.

**Dave Jones:** Because Hacker F is not a key fob.

**Chris Gammell:** That's right. Wow. Yeah. Okay. Well, I guess, I guess you take the good with the bad, huh, Mike? Yeah.

**Dave Jones:** I was kind of concerned about this article at first, but. Yeah.

**Chris Gammell:** And then you're like, and then everybody reads it and they're like, I want one. This is a great way to get potential, uh, uh, you know, thieves into the community. Uh, and, and, you know, just interested passers by as well.

**Dave Jones:** Well, I figure like, uh, the people who have seen this article, like, or pretty much anyone who looks at the Daily Mail and has half a brain realizes what the Daily Mail is. Uh, and.

**Chris Gammell:** Well, you can wipe your ass with it, right? Our market, right. Yeah.

**Dave Jones:** Our, our market consists of people with at least half a brain. So, I'm okay with that.

**Chris Gammell:** Right.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Andrew Miller, Chief Technical Officer of the Motor Insurance Center, Thatchum Research. Real, real brainiacs here, I'm sure. Most of these technologies are designed for only one purpose, which is to break into a car. Mike, I don't know if you know this, but all the hours and hours of software and flexibility you've designed into this thing. Right. They're just, they're just a show. They're all for show. It's actually, it's just, it's just for the cars. That's what it's been the whole time.

**Dave Jones:** Turns out that was my motivation all along.

**Speaker ?:** That's right.

**Dave Jones:** I just learned this by writing the words of some expert.

**Chris Gammell:** Mike, at, at every, every, every evening, Osman goes out and he breaks into cars throughout the, the greater Denver area. So, number one suspect. It's always, it's always Subarus. It's always Subarus and cars that smell really skunky for some reason. Who knows? That's the only kind of cars that are in Denver, so.

**Dave Jones:** Oh, I don't know about the skunky thing, but, well, we do have skunks.

**Chris Gammell:** I was talking about weed. I was talking about weed, Mike. Oh, that kind of skunk.

**Dave Jones:** See, I, that's the thing. I, I live up in the mountains. I'm, I'm isolated from.

**Chris Gammell:** As criminals do. Herb.

**Dave Jones:** I, I, I smell more actual skunks than skunky weed.

**Chris Gammell:** Than skunky weed? Yeah. Yeah. Rob, you buy, you buy the best, I'm sure. That's just my perspective. Yeah. This is a fantastic article, though. This is, this is really fun. Uh, when you're for sale on Amazon, how's that going?

**Dave Jones:** Uh, I don't know. One, one or more of my resellers sells things on Amazon. Oh, it's, uh, oh, it's not you. I don't have anything to do with that directly. Yeah.

**Chris Gammell:** No. Any other new, uh, any other new products in the pipeline or is it the, the hardware's, oh, actually we brought up Daisho when, when Fitz was on the show. How's, how's Daisho going these days? It's not really.

**Dave Jones:** Um, I mean, it's sitting on the shelf waiting for somebody to work on it some more, but, uh.

**Chris Gammell:** More interns, man. More interns.

**Dave Jones:** Yeah, maybe. Uh, it's one of those things where it's just a, it's just been a lower priority and we haven't had time to work on it because we have so many higher priorities. Uh, but there's still some cool aspects to that project that I think, um, are, are worth not forgetting about. Yeah. Um, the, the most significant of which is that we have an open source USB three device core, uh, that people can use on FPGAs. Right. And Daisho is kind of the main platform that someone could use to experiment with that. Uh, on a related note, there's an interesting project to, um, this device core has been ported from our Altera platform to, uh, Xilinx platform recently. Um, and this is, let's see if I can find it. It's, um, it's, um, it's this, uh, project, um, from a group that, uh, that has been, uh, Tim videos, uh, is the guy, Tim, his, his handle is myth row. And he is kind of leading this project to, uh, create a kind of an HDMI slinging platform. Oh, I've seen this thing.

**Chris Gammell:** Oh yeah. Yeah. Yeah. It's like a video switcher for HDMI, right? It's, uh, yeah, no, I did see this.

**Dave Jones:** He got into this, I think primarily because he's been part of the team to do, um, to do conference recordings, like video, video recording and streaming from like CCC events in Germany.

**Chris Gammell:** And this is why I got interested in it. Cause I've been looking at doing like a portable video recording rig. And, uh, I was looking for like what's out there for specifically for Linux because like, there's like capture cards, right? Like capture cards for Linux are, there are some, but they're not quite as prevalent. And, um, so I want to use like OBS and Linux and stuff like that, uh, to capture HDMI. And I think this was, this was one of the top ones that popped up, but it's, it's not, it's still kind of in development.

**Dave Jones:** Yeah. Yeah. The, um, a pneumato ops is, uh, it's actually on crowd supply. Oh. Um, and, uh, yeah, so we should link into that. It's a really cool, uh, platform. It's based on a Xilinx FPGA and it has like a bunch of different HDMI ins and outs that you can do really flexible things with. Yeah. Right.

**Chris Gammell:** And pass through, you can do, uh, you can send it off to a recorder. You can like inject in the stream, I think something like that. Right. Right.

**Dave Jones:** Right. And this is, this is something that was developed like just to support their conference video recording infrastructure at, uh, at hacker events, which is super cool. Uh, and anyway, this thing is, uh, kind of, uh, it, it had a life of its own before Daisho, but it, it kind of portions of it have kind of, um, forked off of Daisho, which is really cool that even though Daisho itself hasn't turned into a commercial product that, that we've been able to provide something that has helped other, another product become a reality, which is really, which is exactly what I want to see as an open source developer.

**Chris Gammell:** Right. Right. Right. Right. And also they have Tim's open FPGA expansion, which is then they link in that, uh, that XKCD comic about the 14, the 14 competing standards and you make a 15th. Oh, nice. One of my favorite, one of my favorite XKCDs. Yes. Totally.

**Dave Jones:** Yeah. Yeah. So that's a really cool, uh, platform. I definitely recommend people check that out. Uh, but we've been working a lot on, uh, on great vet stuff. Um, in particular working on some neighbors for great vet. Um, I've got, I'm, I'm working right now on a, a neighbor, which is an add on board that is a super flexible, uh, level shifting and multiplexing board. Oh, cool. Um, and so it allows you to like wire up to a bunch of test points on a target or something like that. And then, then you can do some fairly sophisticated automated probing to figure out what kind of interface you have there or multiplex to a different peripheral on the great vet's micro controller and stuff like that. And, and just do a level shifting to whatever target voltage you have.

**Chris Gammell:** So it's like hook it up once instead of like having jumper wires all over the place. You just hook as many wires as you can. Then you say you define which wire is which.

**Dave Jones:** Right. And if you're using, if you're using the great vet, even for something simple, like you just want to dump some flash memory or something like that. Uh, you may be trying to interface with something that has a different voltage than your great vet. Yeah. And that's all, that's been a challenge for a long time for things like good vet and bus pirate. Oh yeah. Um, that like the simpler lower cost platforms to do that tend to not have any kind of level shifting built in.

**Chris Gammell:** And you need to do that. Would you ever dump like a DDR? Is that why as well? So you can get like the, the various half voltage stuff or is, or is that not why?

**Dave Jones:** Uh, maybe down the road. Um, but, uh, and that's something that I'm looking at a little bit. Uh, right now I'm looking at, uh, thanks to a tip from David Karn. I'm looking at using the green pack chips. Oh, those are cool little chips. Yeah. Yeah. As my level shifting solution. Yeah. Uh, because there are these, they're just like a tiny. They ain't cheap.

**Chris Gammell:** I beg to differ. Really? Maybe you're buying in volume enough. I've wait.

**Dave Jones:** Like you can get, if you just buy their dev kit that comes with like, uh, uh, I forget like a hundred chips or something like that. Uh, uh, or tens of chips or something like that. Uh, that you can program, uh, the, the, they're at something like 60 cents a piece.

**Chris Gammell:** But is that, you need one pack per chip or per line rather, or what?

**Dave Jones:** No. And then I could do, I could do level shifting on like eight lines on one chip.

**Chris Gammell:** Oh, okay. I thought it was one per, per line. No.

**Dave Jones:** Sorry. So, um, and that's, you know, that's the hundred or less quantity pricing. So, um, I don't know what they're.

**Chris Gammell:** Right. So yeah, that'd be two and a half bucks for what? Four, for, for, for 32 bit network bus. Yeah, exactly. Yeah. Right. So less than two bucks, probably a quantity. Right. Right. Which I think is pretty reasonable. I was thinking per, per line. That's why. And that would get up there pretty fast. Right. Right. It would. 30, 30 at 60 cents each would be what? Like 18 bucks. Yeah. Yeah.

**Dave Jones:** No, but I, I can get one that has like eight in and eight out, um, for around that 60 cents or something like that. That's cool. At the, you know, fairly low volume price. The, and one of the interesting things about the green pack parts is that they, they never had a, uh, an HDL synthesis tool. They only had schematic entry, but they published their, um, they published their bitstream format. It's fully documented. Oh. Yeah. And so Andrew Zunnenberg has been working on an open source tool chain for it. And so you can do using Andrew's tool, you can use, uh, this open source HDL synthesis tool chain, which is super cool.

**Chris Gammell:** Yeah. Uh, and it enables. So if you had enough of these green packs on board, right, you could make a very, very, very large FPGA board. Oh, yeah. Something like that. Something like that, right? Yeah.

**Dave Jones:** Yeah. It wouldn't. I mean, the amount of logic per green pack chip is very small, but. Right. Right. Um, but one of the nice things about them is that they, they do, um, some analog stuff in addition to digital stuff. So there's an, like you can get a part that has an ADC in there that you can switch into any, any pin. Uh, you can get parts that have multiple DACs that you can switch into any pin. And the.

**Chris Gammell:** No, one of my friends in town here is doing that actually. Oh, really? The analog stuff. Yeah. Yeah. Nice. Yeah. He, he was the one who told me about these chips. I, I hadn't, I hadn't heard of them before that. So they're, they're, they're pretty fancy. I gotta say. Chip of the week. Chip of the week. King of the North. Sorry. I haven't watched a lot of HBO lately. I'm sorry. I've been really excited about what's it called coming back. Uh, yeah. Anyways. Uh, yeah. Chip of the week. Cool. Yeah. Green pack. They have more than, they just have the one or is that? Well, it's a whole series of parts.

**Dave Jones:** Yeah. Um. And it's Salego. Salego's a company. Yeah. Yeah. Green pack is the, the series of chips. Yeah. And, um, there's a whole bunch of them that have. Oh yeah. They're all kind of variations on a theme. Uh, they have like different amounts of pins or different types of logic inside them. Or like some of them are dual supply and others are single supply. I'm of course looking at the dual supply ones because I want to use it for level shifting. Yeah. Um, and, um, I got a little concerned when I was looking through the documentation for them because it's all talking about one time programming. Yeah. Yeah. And I'm like, that is not what I want. Right. Um, but there's this, um, there's this method that they use. Like it's hard to find in their documentation because it's not like, it's not what they consider to be their primary use case. They're considering their primary use case.

**Chris Gammell:** They're talking about production, right? Where it's like, you want to have a flexible, you know, tiny logic unit that can switch around as needed. Right.

**Dave Jones:** Well, but they, they, they assume that their customers are doing a one-time programming to configure it, uh, for a given design.

**Chris Gammell:** Right.

**Dave Jones:** And, uh, but they have a development method where you can basically load in a bit stream, uh, into RAM instead of into their one-time memory and just configure the thing on the fly. Uh, it means you have to load a bit stream every time you power it up, but it's super flexible and you can do that indefinitely, uh, instead of just one time. And they, they only document that as being like their, their development and test workflow. Um, not as like your final production workflow, but for my application, I would totally use that on an ongoing basis and never, uh, you know, never burn the one-time memory.

**Chris Gammell:** Right. This, this neighbor is always in development. Yes. Yeah, exactly. Uh, and where, and so that's in one of their manuals?

**Dave Jones:** Uh, yeah. Like if you, if you go through the data sheets for the parts. Okay. Um, you, you'll find.

**Chris Gammell:** Look for the development section.

**Dave Jones:** I can't remember what they call it. Uh, they call it like, oh, I think they might call it emulation. Like emulation. Yeah. Right. That's a poor name. It's on chip emulation. Hmm. Okay. Which, uh, it doesn't really fully describe, uh, on chip emulation what they're doing in my opinion. They call it on chip emulation, but really what it is is you're, you're fully configuring the device.

**Chris Gammell:** They should, they should call it shit. Don't work yet. Right. Yeah. Yeah, exactly. Oh, oh, oh, um, that's nice. Actually. They, they don't force you to give an email, but they do prompt you for one. I was just trying to get a data sheet. So.

**Dave Jones:** Yeah. Another neighbor we've been working on is, uh, this infrared hacking neighbor. That's a lot of fun. Uh, that lets you, it basically allows you to do a software defined radio approach to infrared transmit and receive.

**Chris Gammell:** Nice.

**Dave Jones:** And, uh, so we're doing, we're like sampling an incoming infrared signal at 20 million samples per second and things like that.

**Chris Gammell:** Right. For like a 32 kilohertz signal or whatever it is.

**Dave Jones:** Well, the thing is, it turns out there are a lot more interesting things in the world of infrared than just like. Oh, sure. Right. 38 kilohertz remote controls.

**Chris Gammell:** Yeah. But most of the off the shelf chips that you're going to get are going to be like pre-programmed at the 38 kilohertz, whatever. Right. So. Exactly.

**Dave Jones:** Yeah. Um, but you could do things with our platform like, uh, fingerprint the difference between multiple 38 kilohertz devices that are all in the same room.

**Chris Gammell:** Good Lord.

**Dave Jones:** Uh, and also we found some interesting target devices like, um, that are not 38 kilohertz infrared, but things like, uh, audio over infrared, um, both analog audio over digital infrared and digital audio over infrared. Oh my God.

**Chris Gammell:** I used to have a headset that did that. That was my first pair of wireless headphones.

**Dave Jones:** Yeah.

**Chris Gammell:** And I remember if you laid down on one side, even though it was a headphone, so it didn't feel good, it would like, it would just go staticky because you'd be blocking the signal. Yeah.

**Dave Jones:** And you know where there's a super popular now is in automobiles for the, the seat back, uh, entertainment systems.

**Chris Gammell:** Really?

**Dave Jones:** Yeah. They use almost all of those things. Oh my God. Infrared headphones.

**Chris Gammell:** Oh my God. Does that mean that you could eventually, you could pipe? No, it wouldn't go through a window though. That's the problem. So if someone had an open window though, and you, and you flooded the signal in there.

**Dave Jones:** Oh yeah, absolutely.

**Chris Gammell:** I've always wanted that. Like, that's what I've always wanted is like a car device so that I could basically like, if I knew what frequency their, their radio was tuned to, right? They were like 98.5, just like to hop on that and just be like, stop driving like an a-hole, a-hole. Yeah. Just to see their face. Hopefully they wouldn't go off the road, but you know, just like pirate, pirate, uh, inject, uh, my insult to them. I just want them to hear my insult as they're driving poorly. Right. Yeah. That is totally a thing. I have very simple needs here, you know? That's cool though.

**Dave Jones:** Yeah. And creepy. Uh, people have done that with Bluetooth, Bluetooth too, actually. Really? Yeah. Well, they just- Kind of in the early days of Bluetooth hacking, there were a lot of vulnerabilities in, um, like you could just connect to somebody's, uh, like on the very early days of, of like car kits, Bluetooth car kits. Oh, yeah, yeah, yeah. Uh, like they had-

**Chris Gammell:** Oh, yeah, it's like your iPod would hook into the RF, it would be like a Bluetooth to FM transmitter or something.

**Dave Jones:** They had like no security on the, um, uh, like car kits for, for mobile phones. Yeah, yeah. They had no security on like being able to pretend you're a phone and talk to the car and, uh, or talk to the car kit, which is often an aftermarket thing. And then- Got it, yeah. Uh, and then you could just talk to people while they're driving. Yeah.

**Chris Gammell:** Those were the days. Those were the days. When hacks were plentiful and cheap. But now they need other kits, so they can, they can buy them from, from you and buy a HackRF or a Great Fed or whatever and, and move, move on with their hacking. Uh, well, anything else we should know before we go? Because we should probably- Yeah, we probably should wrap up. We're like an hour and 45 minutes almost, so. Oh, goodness. We're pushing. Yeah. You know, you know how it is. Well, it's been fun, man. When Michael Osman is on the amp hour, it's, it's, it's like, uh, it's like old times, you know? It's what, their fifth, fifth appearance? Something like that.

**Dave Jones:** It's something like that. Yeah.

**Chris Gammell:** Yeah, it's been a good run. Is this the last one? No, I have no idea. Tonight we say farewell to Michael Osman.

**Dave Jones:** It's up to you, not me.

**Chris Gammell:** Cool. Well, I'll see you at, uh, DEF CON and hopefully at future conferences after that.

**Dave Jones:** Yeah, definitely at the, uh, at the Super CON. Yeah. And, uh, of course the Open Hardware Summit's coming up too.

**Chris Gammell:** Oh, also, yeah, in your neighborhood.

**Dave Jones:** That's right. It's going to be in Colorado this year, which I'm excited about.

**Chris Gammell:** Right. And they just published a schedule too. I, uh, I posted that on the subreddit, so. Excellent. People can check out the Open Hardware Summit schedule.

**Dave Jones:** Yeah.

**Chris Gammell:** Cool. Uh, well, thanks again, man. We'll talk to you soon.

**Dave Jones:** All right. Catch you next time. Bye.

**Speaker ?:** Bye.
