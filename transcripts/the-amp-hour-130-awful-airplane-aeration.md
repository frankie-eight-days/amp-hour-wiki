---
episode: 130
title: Boeing, PCBs & Startups - Awful Airplane Aeration
url: https://theamphour.com/the-amp-hour-130-awful-airplane-aeration/
---

**Chris Gammell:** This episode of The Amp Hour is brought to you by Electronicsurplus.com. From vacuum tubes to semiconductors, Electronicsurplus offers a huge selection of current and legacy products that integrate into your next design. Electronicsurplus also specializes in hard-to-find replacement components and off-the-wall parts you can't find anywhere else, all offered at some of the lowest prices on the Internet. To learn more about Electronicsurplus and to support the show, go to theamphour.com slash es and you'll be whisked away to an online marketplace of weird and wonderful things. This is The Amp Hour Podcast. Recorded January 28th, 2013. Episode 130. Awful. Airplane. Aeration.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Dave Jones:** Hey, Chris. It's just us again.

**Chris Gammell:** Yep. Back to us. The dynamic duo.

**Dave Jones:** After our big guest last week.

**Chris Gammell:** Yeah. That was a good interview.

**Dave Jones:** We are still trying to alternate, aren't we? We're still trying to do the alternating thing. Yeah. It's been working out okay. Oscillating pattern of, yeah.

**Chris Gammell:** Got to like it. A couple more guests lined up out there. And actually, people have been adding to the list of, we have a guest suggestion page and people have been nice enough to be adding stuff to that. So if people want to, if you look on, don't add stuff if you already see them on there. But yeah, there's probably people that aren't on that list that you might want to add. So it's pretty easy to do.

**Dave Jones:** And we'll try and get like, you know, the President of the United States or all the was, which of course is more important. Yeah. Yeah. Or someone like that. Yeah. So put the name on there and we'll just get them using our vast...

**Chris Gammell:** Right. Networking abilities.

**Dave Jones:** Power of, yeah, networking.

**Chris Gammell:** Well, I do have a Twitter account, you know.

**Dave Jones:** Yeah. Yeah. Woohoo. Yeah.

**Chris Gammell:** I mean, I'm pretty important.

**Dave Jones:** Oh boy. Okay. We've got some news. That's The Amp Hour teletype there. Breaking news coming in. Well, it's not breaking. You know, it's a week. Oh, we've got a week lag here on the show. So it's pretty lame. But anyway, we treat it as just coming through. National Instruments Acquired, DigiLent. Yeah. Yay.

**Chris Gammell:** I guess.

**Dave Jones:** Does anyone care? I mean, would DigiLent be good? DigiLent's big enough for anyone to care.

**Chris Gammell:** Yeah, they were the ones that did that analog discovery kit. Aren't they the ones that did that with EDI? Yes.

**Dave Jones:** And which I've still got in my mailbag unopened. Oh, okay. Yeah. Yeah. And that was a good, I think, because they've been teeing up for a long time, I think. There's been various, like, you know, national... Like, I think some of the DigiLent staff have had National Instruments drivers or something like that. I don't know. I could be talking out my ass. But yeah, it's, you know, it's a natural fit, I guess. Yeah. Well... Because National Instruments are into all that sort of educational, you know, stuff and development stuff.

**Chris Gammell:** And, well... Yeah. Well, it's nice because, I mean, NI kind of has the... They have a lot of, like, you know, quick start kind of stuff. So you can... Maybe not quick. I mean, you have to install a lot of drivers and stuff. But, you know, they're friendly. Oh, but it's still, yeah. It's friendly stuff. Yeah. So that's nice for getting people started. I know they have that MyDAC, the data acquisition system. That's okay.

**Dave Jones:** It's, you know... But... Well, it's great. I mean, it works, you know, you pay an arm and a leg for it. But... Yeah, that's the part I don't like. That's the idea, right? You pay an arm and a leg and it works and they support it. Yeah. And they support it for a long time. And, you know, heck, I was still using National Instruments boards on, you know, Windows 3.1.

**Chris Gammell:** Oh, yeah?

**Dave Jones:** 3.11, right? And they still supported...

**Chris Gammell:** Wow.

**Dave Jones:** You know, they'd still sell you the boards and stuff for a lot, you know, for more than a decade. It was fantastic.

**Chris Gammell:** Oh, that's pretty nice.

**Dave Jones:** Yeah. But you pay for it, right? That's the sort of thing you pay for. Yeah.

**Chris Gammell:** Yeah. That's the hope is that, you know, there's two things. It's one that it doesn't... I don't think they would, but that they wouldn't mandate, you know, that you have to use NI. But I don't think... I think, if anything, they'd use it as a sales tool to be like, and here you can talk to with NI stuff, you know, instead of, you must use it, right? Yeah, yeah, of course. No, no. But then just the other thing is working with other people. But I think NI already works with analog devices and a couple other people anyways.

**Dave Jones:** Oh, they work with a whole bunch of companies, yeah.

**Chris Gammell:** Because I think the ADI SPICE simulator, is it theirs or maybe it's... Yeah, no, I think it is theirs. I think it's actually based on the NI SPICE engine. I've only used it once. I don't know. I've never used it. Yeah, it's surprising. Like, all of the... You know, a lot of the big companies have their own SPICE engine. Like, TI has Tina, T-I-N-A. And then ADI has this one that's, I think, the joint venture with National Instruments. Linear Tech obviously has LT SPICE. Yep. I guess National used to have WebBench. I wouldn't really call that SPICE, but no, they're TI. All right. Rest in peace, National Instruments. Consolidation.

**Dave Jones:** Well, I've always hoped that National Instruments would buy Altium, you know? Oh, yeah. Because they do have like a PCB schematic tool with that simulation. You know, they've bought various... I can't remember the name. Yeah. Multi-SIM or something they bought, something like that. Yeah.

**Chris Gammell:** That's the one I'm thinking of. That's the one that the ADI worked with, I think. Right.

**Dave Jones:** Okay. Yeah. Right. Yeah. And they bought all that. And, well, you know, it's just like aimed at like the education market. And they're like, I don't see the point of that. Yeah. Oh, look, here's a nice PCB schematic tool for education. Yeah, great. But, well, you're just going to ditch it when you go into the real world, right?

**Chris Gammell:** Here's another thing that'll set you back as an academic when you're getting into the working world. Let's learn Pascal, folks. What do you mean we don't simulate everything?

**Dave Jones:** Oh, that's too bad. And we do all our programming in Pascal. Yeah, in MATLAB.

**Chris Gammell:** I know. Nobody's sick any dogs on me. I know people use MATLAB and everything else.

**Dave Jones:** Oh, that's huge.

**Chris Gammell:** No, MATLAB's huge in the industry. What are you talking about? I know. But I don't know. I see that as like a... I don't use it, but it is huge. But you see that as a programming language, right? It is a programming language. But it's like, you know, you're not going to be programming micros with it. Or maybe you are, and I'm going to be told off later at some later date.

**Dave Jones:** No, it's high level stuff. The thing with MATLAB is that they have a library for everything, right? So if you want to do a fast-forward transform, you just go FFT, you know, like just call up the library and just use it, right? Bang. Done.

**Chris Gammell:** Yeah, I think the real thing is people that are doing MATLAB stuff are so far out of my sphere of knowledge. They're just like in the stratosphere. And I'm just like, hey, I flip it sometimes.

**Dave Jones:** It does have that smell of academia to it, you know?

**Chris Gammell:** Well, yeah, yeah. It's just like you said, it's high level, right? I mean, it's very cerebral and you're doing huge data sets, right? It's like big data type stuff.

**Dave Jones:** Yeah, exactly. Yeah, it's analyzing big data. Yeah. You know.

**Chris Gammell:** It's very important for certain things, but nothing I've touched in a very long time.

**Dave Jones:** Exactly. And it's a bit before my time. We never really used MATLAB.

**Chris Gammell:** Yeah, exactly. Well, and since then, since I don't have a license now, I just use Octave. There's another one out there that's like a freer version, but then those are kind of crippled as well. Oh, okay. You never used Octave before?

**Dave Jones:** Never even heard of it.

**Chris Gammell:** Oh, yeah. It's like a, I don't think it's open source, but it's like a free version of a mathematics type program. It might be open source. I'll have to look into that. Right. But, yeah, it's good stuff. If you need it, it's there.

**Dave Jones:** I've always sort of like rolled my own, you know. I've ever rolled my own in like Visual Basic or I've rolled it in LabWindows CVI, which is a national instruments thing or, you know, something like that.

**Chris Gammell:** Just like heavy duty math operations?

**Dave Jones:** Yeah. You know, if I need to do, you know, FFTs or do something, you know, variant control algorithms, all sorts of things. Yeah, I just sort of rolled my own over the years. But, yeah, I'm sure it's technically much easier in MATLAB or something, you know, if you're a MATLAB script kitty. Yeah. Then I'm sure it's real easy. No, it's just something I've never really used. I've always used different tools. Whereas I'm sure that, you know, everyone studying in the last 10 years would have used MATLAB.

**Chris Gammell:** Right. Or Python or other high level stuff like that.

**Dave Jones:** Or something other high level stuff. Yeah. Yeah.

**Chris Gammell:** You ever looked at Project Euler? Is it Euler? It's Euler, right? I always say Euler, but that's not right. Never heard of that one either. E-U-L-E-R. It's like, it's supposed to be like... Oh, Euler. Yeah, yeah. I thought it was Euler. Euler.

**Dave Jones:** I thought it was Euler.

**Chris Gammell:** Hold on, Wikipedia. Decide that later.

**Dave Jones:** Here's this pronunciation thing. Yeah. All the people who come out of the woodwork now, this is how you pronounce it because it says so on Wikipedia, you know. Rubber, rubber, rubber, rubber.

**Chris Gammell:** Yeah, that's a cool thing too. Like if you're, you know, bored on a Saturday and you want to do some math. Yeah. Woo-hoo. It's good. No, it is really good though. Like if people don't know, it's a way that you can, there's like a bunch of problems that are increasing in difficulty and basically you can use programming to solve these problems. That's the idea is to practice programming for these math problems. And like they've been solved by lots and lots of people. Like the number one problem there has been solved by 266,000 people. So I'm making fun of people, but obviously I'm, you know, very alone in that, right? Mostly I'm making fun of myself because I can't do it.

**Dave Jones:** So you can upload your solution. Is that how it works? I don't know. I think you might just say... You pose a question and people...

**Chris Gammell:** No, no, no. So there's a set question. There's set questions. Right now they're up in the 400. And they're just like, they're like, it's kind of like brain teasers, but they're like math brain teasers. Got it. So how do you... Here's an example. What is the 10,001st prime number? Right. And you could write all that out. Right. Or you could do it programmatically and then, you know, calculate primes and, you know, get to the 10,000.

**Dave Jones:** And there's a thousand math nerds out there of who will think they've got the best algorithm for doing that. Yeah.

**Chris Gammell:** Well, that's a good way to say it's like algorithm practice. Right. Practice is important. So if you're a math person or a programming person, it's a good site for that kind of thing, which I am not.

**Dave Jones:** I've kind of been a bit into that over the years, but... Yeah, you said you had your software. It comes and goes.

**Chris Gammell:** You had your software things going on.

**Dave Jones:** Yeah, I had my software phase where, you know, a friend and I, we'd just be competing about who can write the tightest, fastest algorithm, you know, and to do something. And, you know, eh, it was fun. Back in the day. Back in the day.

**Chris Gammell:** Yeah. I kind of missed out on that whole thing. Not that I couldn't have done it. It was just a...

**Dave Jones:** Right.

**Chris Gammell:** It was just a timing thing, I guess, or laziness or whatever it was.

**Dave Jones:** Well, this is all part of the, you know, I'm talking late 80s here, right? Right. I'm talking, you know, the microcomputer revolution and fat.

**Chris Gammell:** Right, and build your own 6502 and then write assembly for it, right?

**Dave Jones:** Exactly. And, you know, back when it was just cool to work on that. And that sucked a lot of people away from electronics, right? Like me, it sucked me away from electronics for many years. I was, you know, working on computer stuff and programming and all that sort of stuff

**Chris Gammell:** because it was the latest cool fad. Yeah, but at that point, I mean, that's still pretty close to the metal still, I think. Like, I mean, if you get someone programming an assembly these days, you know, you say they're bare metal programming, right? It's like...

**Dave Jones:** Yeah, yeah, exactly.

**Chris Gammell:** Yep.

**Dave Jones:** And sometimes you'd have to go down to the assembly, you know, we're writing at the assembly level to get the tightest, fastest algorithm, right?

**Chris Gammell:** Yeah.

**Dave Jones:** All that sort of jazz. And, yeah, you know. And then you start getting ideas for what you can program. Oh, I've got an idea for a game. I'll program that and spend a couple of months writing a game, you know? Yeah.

**Chris Gammell:** Well, I do remember programming in BASIC. Like, I did that in the computer I had in my room. Right, yep. I don't miss that. Yeah.

**Dave Jones:** PASCAL was one of my favorite languages back then. Yeah, yeah.

**Chris Gammell:** Never got into PASCAL.

**Dave Jones:** Power BASIC, Quick BASIC 4.5. Some people must be... Basic PDS 7.1, if anyone remembers that. Oh, that was the best.

**Chris Gammell:** So some people must be, like... Sorry. Like, nostalgic for that, right? I mean, I guess there's...

**Dave Jones:** Yeah, yeah, of course.

**Chris Gammell:** Yeah. I guess people are still building 6502s.

**Dave Jones:** And, of course, this is all for the internet, right? So we... Yeah. Oh, yeah, they're still doing it for fun. But now everyone's working on their Arduino, you know? Yeah. So... Yeah, people are making their boards and stuff. And then you didn't have the distractions you do these days with the internet, right? There's so much going on. Oh, there's a new fad every week, right?

**Chris Gammell:** That's true.

**Dave Jones:** Whereas back then, it was, you know... Yeah. I mean, you just look... Every time I check out the internet here, oh, there's this new thing. You know? Oh, that'd be fun to work on. If I only had time. So I don't end up having any time to work on anything. Yeah. Because I'm too busy, you know, finding new things to work on. Yeah. It's crazy.

**Chris Gammell:** Yeah.

**Dave Jones:** Hate the internet.

**Chris Gammell:** Oh, yeah. It pulls you in every direction, right? It does. Yeah. I know.

**Dave Jones:** I can't focus on anything.

**Chris Gammell:** I was listening to an interview with Seth Godin, that marketing guru guy. And he's like, yeah, you know, you'd think a marketing guy would be like online all the time. He's like, no, I just ignore Twitter. I ignore Facebook. And basically, he's like, yeah, I just kind of go and do stuff. And I was like, oh, that hurts. There you go. That stings. I know. Yeah. Yeah. Ouch. Because we aren't smart enough to do that. We just get sucked into the... There's so many shiny things on Twitter. I mean, honestly, that's how I find links for the show. And it's like, ah, you know. Yeah. I want to keep in touch with things. But I find out about things that are cool, right? So, okay. So I want to talk about this thing this week. There is a new startup, which I found out later is a Y Combinator sponsored startup. Y Combinator being the one of the... I think I mentioned it last week, actually. It's like an incubator out in Silicon Valley. Right. But it allows you to... So it's called Circuit Hub. And it allows you to search out footprints. And then it uses Dropbox to sync with your folder structure and your computer. So it uses the native thing that your CAD program is already using. So when I saw that, at first I'm like, oh, footprint program. Okay. You know. And then I saw Dropbox and I'm like, oh, my God. Right.

**Dave Jones:** They've integrated with Dropbox.

**Chris Gammell:** Yeah. So they have like... I think they're working with, what, Altium, Cadence, and Eagle right now.

**Dave Jones:** I'll say up front, there's a grand total of 158 parts on there. Right.

**Chris Gammell:** Well, this is, yeah, it's a critical math problem, right?

**Dave Jones:** Right. And that's spread across all the packages, right?

**Chris Gammell:** Yeah, yeah, yeah. You're not... Yeah. If you see one, like if you see this BSS84 from Fairchild, it only has footprints. It has the data sheet, but it doesn't... It only has footprints from... I don't even know which ones. Let's see. Right. Footprints, no footprints.

**Dave Jones:** Yeah. So this... But it looks like pretty... Have you actually used it? Have you actually connected using your Dropbox account?

**Chris Gammell:** Yes, I have. And I've pulled... Oh, okay. I've pulled footprints. Is it easy? Oh, yeah. It's super easy. It's like... It's not even like... Right. You know, some of them are like where you're, okay, collect them all up and then hit them all at once. Like there was another one on the list from a couple weeks ago, actually, that someone had built... One of our listeners actually built, which was pretty cool. It was KiCad. It was KiCad based. And it was like that where, you know, it's like you have collect them all up and you say download all at once in a zip file. Right. This is... This is like that except it's just instant. It just zips it right... It just sends it right to your Dropbox file. So... Right. And...

**Dave Jones:** And then you can work on that file live.

**Chris Gammell:** Exactly. Exactly.

**Dave Jones:** Right. But then what happens if somebody changes that part?

**Chris Gammell:** Yes. That's a good question. So it's not like... It's not like you're... It's not like a living copy.

**Dave Jones:** Is that even possible? After it's been updated, can you... No.

**Chris Gammell:** No, no, no.

**Dave Jones:** Yeah. But if you're using the library directly from your Dropbox, you know...

**Chris Gammell:** No, no. It's like a pull. So it's like every time... So the very first time... So you find a 2N3904 footprint, right? And you pull that once. Yeah. It'll sit in your library forever. Now, I'm not sure about how it looks... How it does like comparisons against, you know, existing stuff. It shows up updates and stuff like that. But... Mm-hmm. Yeah. It's... Got it. Yeah. So for right now, though...

**Dave Jones:** And you only connect it to your public Dropbox account, right? Exactly. Exactly.

**Chris Gammell:** So what you would do is like an Eagle or an Altium, you would... You would actually set that as a secondary folder, right? You'd have a main folder for your parts. Actually, I don't know how Altium works. I haven't used it in a while. But, you know, you'd set this as a secondary folder, and then it would pull in from there.

**Dave Jones:** Right.

**Chris Gammell:** You might not use it for all your stuff at first, but I think eventually I could see it as this thing gets populated. I mean, like, if you look at how... So I've been talking to Andrew, the guy that's one of the guys that started this. And if you... I mean, like, it's just like really strong back end. It's just like really...

**Dave Jones:** Hmm.

**Chris Gammell:** I was actually talking to him. He's an embedded guy. And then he started, like, web programming. And so, like, he actually knows about electronics. Right. Which was like, whoa. Because usually people go the other direction, right? Usually they're programming like, oh, I want to do hardware. And now he's doing really high-level software stuff like this fancy UI stuff, whereas he used to do electronics for a long time. So he actually knows what he wanted. So, yeah. That's a good thing. So I'm a very big fan of this so far. All right. The only thing I don't like... Oh, I'm like, give it a try. And I've told him many times over that there's no KiCat support, but apparently that's on its way, so... Right. Because, you know, the nice thing about that, too, is you get automatic libraries because of stuff that's already out there. I guess Altium and Eagle and Orcat...

**Dave Jones:** Can you just, like, subscribe to, like, the Altium part of it? Because, like, there's no point. Looking at any other parts in some other system, right? If you're using Altium or you're using KiCat, that's all you care about.

**Chris Gammell:** Right. Right, exactly.

**Dave Jones:** Is there a way to just filter out everything else and say, I use, you know...

**Chris Gammell:** No, I haven't used it that much yet.

**Dave Jones:** I use Altium and that's it. Bugger off. Everyone else, you know... I don't want to see a single footprint that's for some other package.

**Chris Gammell:** I don't know. I haven't used it that much. At the moment. I haven't used it that much.

**Dave Jones:** Like, it just tells me there's all these parts here and it doesn't even tell me what package they're for and I can't see any way to subcategorize into the packages. Yeah. The software packages. So, hmm. Anyway.

**Chris Gammell:** Hmm. Yes, indeed.

**Dave Jones:** I do like the concept of integrating with Dropbox, though. That's... Yeah.

**Chris Gammell:** I think...

**Dave Jones:** That's good.

**Chris Gammell:** Yeah. I think that was one of those little lights popping on. That's the thing I liked about it because... Oh, crap. You know, you...

**Dave Jones:** Otherwise, it would have been yawn worthy, right?

**Chris Gammell:** Right. Yeah. Because, I mean, there's another one out there that's like a library manager.

**Dave Jones:** I forgot what it's... Oh, someone else. I'm sure there's quite a few.

**Chris Gammell:** Yeah, but it was like a subscription base, you know, and it was like updated. Right, yeah, yeah, yeah. But it's like these big chunk updates, right? And there's something to be said for that, too, right? Because then you know I'm at rev A, now I go to rev B, and all the parts can potentially be different. Of course, and bang, I've got all the latest ones. Yeah. So there needs to be like... You need to be careful with that kind of thing, right? Because you don't want to get sniped by someone updating... You pulling apart, assuming it's the same, and then, you know, like some pins flopped, right? And then, you know... Yeah, yeah. Exactly. And then you're driving current. You're driving your op amp output into ground or something. Yep. But, yeah, I just think it's cool. I think it's... I don't know why... It's one of those things where it's like, oh, why didn't I think of that, you know? Of course, I say that a lot, so... Okay. Because I don't think of much.

**Dave Jones:** Right. Oh, boy. There you go. All right. Well, I'll give that one a try.

**Chris Gammell:** Yeah, I'm sure.

**Dave Jones:** Speaking of impractical ideas, I don't even have to look at this one.

**Speaker ?:** Okay.

**Chris Gammell:** Oh, that one. Well, kind of impractical idea, because some of them are impractical.

**Dave Jones:** Oh, how about speaking of startups, too, right?

**Chris Gammell:** So CircuitHub is a startup.

**Dave Jones:** Speaking of startups and impracticality, you put this one on here. Right. It's called FounderDating.com. And I have not tried this yet. Exactly what you think.

**Chris Gammell:** I have not tried this yet.

**Speaker ?:** Right.

**Dave Jones:** No, no, but I... Does that mean you're going to try it? I've thought about it.

**Chris Gammell:** I don't know. I saw this because someone posted it. You know, they said, oh, well, we have 50% engineers, right? Which is, I think, with, like, founder dating and talking about startups, that's like the equivalent of saying, you know, we have women on our dating site, you know? Free for women to register. But, you know, if you're an MBA, you have to pay.

**Dave Jones:** Right. And it's exactly what you think, right? They try and match, yeah, they try and match you up with other... Is there any matching algorithm in this thing? Like, can you... Like, what are the search criteria? I haven't even used...

**Chris Gammell:** No, I think it's like you go out, you search for your own. It's like a dating site, you know, like a match.com.

**Dave Jones:** It's like a dating site, except the idea is, you know, you're trying to find a, you know, a partner for a business.

**Chris Gammell:** Right. Hopefully you're not looking for anyone to screw over. Right.

**Dave Jones:** Right. Bazinga! High quality. Everybody's screened by knowledgeable, experienced managing directors. Right.

**Chris Gammell:** Well, and I'm sure, you know, some of it's going to be tough, right? It's like if you're in, like, the middle of Kansas, right? Or in the middle of Wyoming, you know, and you're, like, looking for someone local. Yeah, you're pretty desperate, right? Meet local singles online. Meet local founders online.

**Dave Jones:** We'll take anyone with a pulse.

**Chris Gammell:** Yeah, right. But I was having it out with Dave before the show because I'm like, Dave's like, oh, this is total BS. And I'm like, Dave, you're the king of online dating, right? You have that book for online nerd dating or whatever. I've written a book.

**Dave Jones:** I've written the biggest, yes.

**Chris Gammell:** I think.

**Dave Jones:** I've written the world's number one read book on internet dating.

**Chris Gammell:** I think you could very easily turn that around and just change it from, you know, just change it to, you know, how for nerds to date online or whatever it was to how to find founders online. Yep. Well. I'm sure many of the same things apply, you know. Start slow. Get coffee first. They do. Right? You know.

**Dave Jones:** No, it all starts with the search. You don't waste your time on people who, you know, who have obvious things that you don't like or, you know, stuff like that. Or crack profile pictures. Oh, this person looks hot, but they smoke. You know, I don't like smokers, but I'll meet them anyway. It's like, no, don't waste your time.

**Chris Gammell:** Oh, I think I could giggle about this for like 20 minutes, you know. Why not? It is silly to think of it, but I think at the core of it, it's an interesting idea because you could potentially, you know, if you're in the market, right, say you're looking, maybe you're looking for work or maybe you're just, you know, bored with your job. Like maybe this could, maybe you're in a relationship you don't like currently and you're trying to get out of, you're trying to get out of that LLC you got stuck in, right? Right. But I mean, so it could work, but I think, I personally, I don't know what works for founders, right? I mean, you look at like historically, like, like what, Jobs and Was, right? They were, they were just like hacker friends, right? I mean, there's, there's no formula to it, you know? You need chemistry with founders, but it just as easily could be that if you, if you, if you meet someone that you really like, you know, like that, that you click with as a friend, you know, that could be really bad for a, for a founder relationship, right? If you're trying to start a startup, you know, if you're, if you're not able to be frank with the other person because you're trying to be nice to them, it's like, man, that's not going to work. You know, you have to be able to get in arguments, you know? That's what I look for in dating sites is people to argue with.

**Dave Jones:** And, and, and you meet up and you talk about all your bad experiences, all your previous dates. Yeah.

**Chris Gammell:** Then I went to this one startup and that guy was a total jerk.

**Dave Jones:** Man. And he had green hair and he, I couldn't believe it.

**Chris Gammell:** I know. Well, well, I mean, I mean, startups are, I mean, especially for hardware, right? I mean, I've, I've, I've seen, so, so Nick Pinkston is a guy that runs the, the hardware startup subreddit. And he also does a software or he does, he does start a startup meetups, right? There's, there's hardware, hardware meetups. There's one in Austin now. There's one in San Francisco. I think there's one in Chicago maybe, but there's, there's like more starting up all over the place for people actually, you know, they have startups, they get together, they drink beers and they kind of just, they do like, they do like a rapid fire talks. And, you know, if you're in those locations, it's kind of cool. You know, I'd love to go to one, but I don't think Cleveland's going to have one anytime soon.

**Dave Jones:** Well, it's the same thing with this, same thing with meetup.com, right? If you've ever used that, if you've been to one of those, they get people together at these, you know, and there's tons of them that get all, you know, they, they get entrepreneurs together, you know, so it's a local entrepreneurs meetup group and you meet with them and I've been to one of them. Oh my God, I regretted that.

**Chris Gammell:** Be careful there, buddy. They might be listening. They might know where you live.

**Dave Jones:** Well, no. No, you know, it was like, no, it was, okay. I didn't regret going, right? Because I wanted to find out what it was like. No, it wasn't, you know, yeah. Was it a networking event? Is that the problem?

**Chris Gammell:** Was that the, uh.

**Dave Jones:** It was a network, yeah, it was a networking event. Yeah. Right? It's one of, you know, local entrepreneurs, right? And it was just around the corner. So I thought, oh, okay, you know, I'll go, maybe I'll meet some interesting people or something like that. And I did. Yeah. Right? So it was fine from that aspect. Right. So I guess regret is the bad. No, I don't know what you mean.

**Chris Gammell:** No, it's like, it's like networking events. The people that go to networking events are often people looking for content. Like the people that you really want to talk to don't go to networking events, right? Because, because they're so busy doing stuff. I mean, it's just, it's just a reality. Yeah, that's right. And, um. Yep. Because I thought about going to them before and it's like, well, who am I going to? I mean, but the thing is you still make good connections because you might meet someone who's on the verge of doing something cool, right? Or you could work with them.

**Dave Jones:** That's right. That's the idea.

**Chris Gammell:** Yeah. And that's what, that's what you have to expect because you can't go there and make these, you know, like these very, uh, what's it called? Like false connection, not false connections. What am I trying to say? Yeah. Superficial connections, right? It's like, oh, well, you know, what's your job? Like, and, you know, like, you know, like very, very superficial. You have to make actual connections with people in order to, you know, work with them. So, which might also be the downfall of, of a founder dating site, right? It's like, if you, if you're just going based on criteria like that, you know, you might have to go through a lot of people to see if, if you actually want to work together and it's not like a one-sided relationship.

**Dave Jones:** Oh, you could spend all your time looking for people instead of actually doing something. Right. And, and then usually these days, if you're doing something, people will approach you. Right. You know, you put it out there, what you're doing and they'll go, oh, I know how to do that. I think you can help this out. I think we should team up. Right. Especially if you're building community, right? It's very hit and miss. Yeah. Yeah. Right.

**Chris Gammell:** Yeah. I mean, if you're, if you're like part of DIY drones community or, you know, Arduino community, like there are, there are other people out there. If you're talking about it already, as long as you're not trying to be super secretive, then yeah, of course you're going to find people that, you know, want to do the same kind of thing. And maybe then you say, okay, yeah, let's try this together. You know, that's, that's, I think maybe that's the way it works in the best case scenario, because you have just have common, common interests and goals. And then you kind of work from there.

**Dave Jones:** Yeah. The problem with the one I went to was that the guy who ran it was, you know, one of these, you know, he loves giving talks about how to be an entrepreneur. You know, it's all he talked about. Oh, I just came back from my six month trip around the world because I'm, you know, I follow all my own business practices. And I'm one, wouldn't you love to live a wonderful lifestyle like I do? I know. Yeah. You know, and oh, like, oh, my face palm. Right. Like, yeah.

**Chris Gammell:** I think I've heard the term entrepreneurs. I think that's the term.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** That's a good term. I like that term.

**Dave Jones:** And, you know, just because, yes, he did happen to set up a company that was actually his dad's company, which he inherited. Oh, yeah. And Andy, yeah, he made some money from it. And now he tries to make money by telling you how to make money. Yeah, that's rough. And it's like, nah. Right. That's like, yeah. It's like, nah.

**Chris Gammell:** Yeah. It's like, you know, like social media consultants like that kind of thing. And, you know, make money online. Pay me $800 and I'll tell you how I make money online. Oh, I make money online, but you pay me $800.

**Speaker ?:** That's right.

**Chris Gammell:** Whoa. That was a hard, hard lesson learned. It's kind of like multi-level marketing at that point.

**Dave Jones:** Yeah, I know. So it was bad. So that's what I didn't like about it. Right. But there are local meetup type things. So is this, like, website, like, is this idea kind of doomed to failure almost? I don't know either. But I kind of get that inkling that it's just not going to work. I think people should just sign up for it.

**Chris Gammell:** I mean, there's no reason not to sign up for it. You don't have to respond to people, right? I think, you know, if you're interested in that kind of thing, right? And I'd love to hear if people do sign up for it. It'd be interesting to hear back if they actually do get contacted. How quality it is, right? Because at the same time, you know, like, it could very easily be that you get 10 requests for, you know, ridiculous. You know, some people are out there looking for, like, solutions to problems that don't need to be solved. Like, usually anyone, anytime someone says that they have an energy generation idea for, you know, I'm like, oh. Run!

**Dave Jones:** Oh, boy. Yeah.

**Chris Gammell:** But there could be some genuine stuff out there.

**Dave Jones:** And there's, you know, and there's just the people with ideas who have no idea. So they want you to, well, sorry, they have the idea, but they have no idea how to actually do it. Right. Right. They have no skills and no talent to actually do any part of it themselves. Right. And they just want you to, you know, do everything. They want to find someone who just does everything for them. Yeah. You know, they think that their big contribution is the idea. I get these kind of emails all the time. Right. These people, oh, look, I'm giving you the idea. That's my contribution. Here you go. You do all the rest and we'll make a billion dollars. You know, blow it at your ass.

**Chris Gammell:** Yeah.

**Dave Jones:** Ideas are worthless.

**Chris Gammell:** Well, I think, you know, people probably, I'm sure our audience gets that too. And if they get that and you say, all right, well, here's my hourly rate and I want nothing of the profits. I just want you to pay my hourly rate. And it's like, okay, if you can't do that.

**Dave Jones:** And then it just becomes a contracting side. So it's defeated the whole purpose.

**Chris Gammell:** No, but that's how you, that's usually people clam up at that point. You know, it's just like, oh, well, we were going to give equity. Oh, I've got to spend money, do I? I thought you'd do it for free. We'd give you 20% equity and we would get the 80%. Yeah.

**Dave Jones:** Yeah. I don't know. Yeah. Yeah. Anyway, I don't think that's going to work very well. But you never know. I'll, well, yeah. Are lithium batteries inherently dangerous?

**Chris Gammell:** Yes. Asks F Kitsch. Are, are, are, are scissors inherently dangerous? I mean, yes, they are.

**Dave Jones:** And of course, everyone knows what we're talking about. We're talking about the Boeing 787 Dreamliner. Yeah. Right.

**Chris Gammell:** I haven't been following this story very well, personally. I mean, other than I know that they got grounded.

**Dave Jones:** I followed a bit of it. Yeah.

**Chris Gammell:** You sure are grounded.

**Dave Jones:** A battery, which came from my old company, Tally's. Oh, really? Apparently, Tally's made. Yeah. They're the ones who made the whole battery. Like, it's not just a battery, right? It's like all these battery cells in a huge battery management box, right? A big steel box with all the battery management and protection circuitry and all that. Yeah. And apparently, it didn't manage or protect it very well because the thing blew up and caught on fire and completely melted. Yeah. Which is something you don't want when you're flying 30,000 feet up in a steel tube at 800 kilometers an hour, right? Right. You don't want a fire on that. No. Inside that steel tube.

**Chris Gammell:** It's not good. Especially when you want that air just as much as that fire wants the air. That's bad. Right. Yeah, yeah. That's bad.

**Dave Jones:** Oh, boy. Yes. And apparently, it's the second time it's happened, like, in as many months or something. Yeah. So, like, one of them didn't happen in the air. It happened on the ground, on the tarmac, you know. They just, you know, everyone just shuffled off the plane and everything was right. But the other one happened in the air. They started smelling something in the cockpit. What's that? You know? Right. Imagine, you know, is there anything worse than the captain accidentally leaving his intercom switch on and going, hey, what's that? Can you smell something?

**Chris Gammell:** Ask that flight attendant if they left the coffee on again. It smells like crap in here. It's either someone's burning coffee or the batteries are about to explode.

**Dave Jones:** Right. So, this thing completely melted down. You can see the photos. Absolutely, you know, phenomenal. Yeah. This thing. How the fire was contained in the steel case. Anyway, so there's much talk about, you know, what the fault is. And the battery management protection didn't do its job. Right? It didn't protect these batteries and shut them down. But they don't know whether it's a system level thing. Right? Because, like, apparently the battery wasn't able to shut off its own current. So, because that wasn't in the design spec for that battery module. The plane was supposed to have that elsewhere in the system.

**Chris Gammell:** Right?

**Dave Jones:** And so, it all becomes a big complex systems engineering thing. Right? And, like, oh, which system was supposed to automatically shut down the battery when there's a fault? Oh, I don't know. Throw your hands up in the air and, you know, it's not my fault. You know, I just made the battery.

**Chris Gammell:** I cannot possibly. So, like, you know, I work on systems. Right? And we all work on systems at some scale. Right? Yep. But, you know, there's just so many things. Even on small devices, there's just so many things and so many interactions to think of. I cannot even fathom. And that's all within one company, right? Oh, doing plane. Yeah. I can't even fathom working in an aerospace company where there's tons of regulations and just so many subcontras and everything else. Like, I'm not saying that this should have happened, but, oh, man, I can sure as hell imagine how it happened. You know? Like, it's just.

**Dave Jones:** Yeah, I know. It's just so big. I don't know how these things get designed in the first place. They're so big, so complex. In fact, somebody, I think, posted maybe in the EV blog forum thread or something. I'll have to find it. Somebody posted the wiring, the power system block diagram of the Boeing 787. They actually found it. And you see how many subsystems are involved and all interconnected. Yeah. And that's only, like, top level, you know, top level block diagram. And it's like, oof. Anyway. Yeah, so it comes down to, right, what was at fault? Did the actual cell have an internal failure? Because there's always that. There's always been, you know, nobody knows whether it's an urban myth or whether it's true or, you know, maybe it is. But, like, lithium-ion batteries can inherently get little micro failures in them, which then can short out. And the battery can actually fail internally, right? With no physical abuse, no overcurrent abuse, all that sort of stuff. Right. Right? They can actually just inherently fail internally due to, you know, like, physics, right? The physics of how these things are manufactured. There's so fine tolerance and all that sort of jazz. Right.

**Chris Gammell:** But at the same time, it's probably, like, it's probably not that, right? I mean, it's probably something system fault, human error, that kind of thing. Like, honestly, like, the small sometimes errors like that, they have to cascade in order to make big, big, boomy, explodey, smoky errors. Sometimes.

**Dave Jones:** But the problem with lithium batteries is they're exothermic.

**Chris Gammell:** Right. Right?

**Dave Jones:** So they get into thermal... Thermal...

**Chris Gammell:** Runaway.

**Dave Jones:** Runaway, right? Thermal runaway. So they, you know, so once you have something that starts it, it might be a little internal short inside the battery, bingo. You get exothermic reaction and you can't stop it, you know?

**Chris Gammell:** I honestly, I don't know much about lithium-ion batteries.

**Dave Jones:** Well, I do know that much, that they're exothermic, right? So, which is bad. That is, yeah, that is bad. And they've been banned on planes up until now. But the Boeing, for the 787, they got a waiver to use them. Oh, man, that hurts even more. Yeah, exactly. Who signed off on that one? Yeah. Right. So...

**Chris Gammell:** Yep.

**Speaker ?:** Oh, man.

**Chris Gammell:** How much power was it? I guess I should have read about this more, huh?

**Dave Jones:** Oh, these batteries are massive amount of power. I don't know the figure. Oh, yeah, yeah. They can, you know, supply hundreds of amps. 65 amp hour batteries?

**Chris Gammell:** Whoa.

**Dave Jones:** And they're individual cells, and then they have them in series parallel combinations, right?

**Chris Gammell:** That's one cell that's 65 amp hour. 65 amp hours is more than a year, Dave.

**Speaker ?:** Right.

**Chris Gammell:** Pause for a fact. Yeah.

**Dave Jones:** Anyway, they are, yeah, big, high-capacity batteries, right? And there's multiple units of these. Of course. Right. The subsystems and whatnot. But, yeah, it's... I don't know. My guess is that it has something to do with the fact that they're going through thermal and pressure cycling.

**Chris Gammell:** Yeah.

**Dave Jones:** Every time the plane goes up and comes down, thermal and pressure. Thermal pressure. Thermal pressure. Up, down. Up, down. Up, down. Yeah. And my guess is that's what did it in. In some respect. That had some aspect to it, I'm sure.

**Chris Gammell:** Yeah. Well, that's a lot of stress. I mean, even just the forces that are... That's, yeah. ...you know, landing and getting jostled around. I'm sure a lot of that stuff's designed for it, but...

**Dave Jones:** And...

**Chris Gammell:** Yeah, if it's a whole new system, you'd think, man, that's crazy.

**Dave Jones:** How do you test it for that, right? You can't... You can go stick it on a 737. Accelerated life test. Yeah, exactly. You go stick it on a 787 and see if it fails, right?

**Chris Gammell:** You put one in every seat, right? And you serve it little trays of dried up chicken. Throw peanuts at it, yeah. Keep it watered down, vodkas. Yeah. Yeah.

**Dave Jones:** So, anyway, it's real. There's lots of info out there. There's lots of technical info now on this battery fire, and there's lots of people investigating. And it's really fascinating if you're into that sort of thing to follow it. So... Yeah. We'll put the various links in there and, yeah. Definitely. It's good. But my money's on the cycling.

**Chris Gammell:** Yeah. We should take a break for our sponsor this week. We do have a sponsor. Again, they came back. Should we mention the giveaway? Oh, yeah. So, first off, the sponsor is electronicsurplus.com. They were two weeks ago. They're our sponsor. But they are doing a giveaway. States only, unfortunately, because they're stateside. Yep. Sorry. Sorry about that.

**Dave Jones:** It just costs too much to ship these things, right?

**Chris Gammell:** Yeah.

**Dave Jones:** It costs more than...

**Chris Gammell:** Yep. Yep. Yeah. But it's a cool little item. It's a 40-character two-line display. It's a little bit older Hitachi model.

**Dave Jones:** But those 40-character Y ones are bloody useful.

**Chris Gammell:** Yeah.

**Dave Jones:** I really like the 40-character wide ones. What do you... Have you put those in some before? They're not common. Like the 16x2s. I've used them in a few things before, but they're just really handy when they're completely wide. Yeah. Yeah. You don't have to scroll as much, right?

**Chris Gammell:** You can get a bigger block of text in there. So, yeah.

**Dave Jones:** Text on there, you know. Better than the standard 16 or 20x2 display.

**Chris Gammell:** Yeah.

**Dave Jones:** And it uses the standard Hitachi chipset, of course. And if people don't know, the Hitachi chipset, by default, actually supports 40-character displays. Oh, cool. That's why when you talk to a Hitachi... That's when you talk to... Even if you've got like a 16 or 8-line by 2, 8-character by 2 display, the memory is always mapped in 40-character lines. Oh. So, even a 16x2 display, you have to start at address... You know, if you want to put the character on line 1, you know, character position 1, okay, you do that. But if you want to put it on line 2, you've got to jump to address 40. Oh. Because it's... The chipset handles up to 40-character displays. Huh. So, yeah, 40-character wide. So, even on your 16x2, your second-line address is address 40, not address 16. Yeah. Oh, 8. Yeah, 16. Sorry.

**Chris Gammell:** So, there you go. Well, that's cool. A little known fact. I did not. I'm sure everyone knew that. I didn't know that. I hardly do anything with displays. I'm never talking to displays, so...

**Dave Jones:** Right.

**Chris Gammell:** That's cool.

**Dave Jones:** Right.

**Chris Gammell:** Yep. So, yeah, electronicsurplus.com, thanks to them. Just check out their site. People should... We talked about it two weeks ago, but they have a bunch of other... A lot of surplus gear, a lot of great stuff for mechanical, a lot of, you know, like switches and rotary dials, stuff like that. But, stepper motors. But, yeah. And what do you have to do to get it? Oh, well, I'm sorry. Do you have to send them an email? That's right. I should probably tell people that, huh? So, if you go to theamphour.com slash es, there will be a sign-up page there. It'll just be a Google form. You know, the owner, Steve, he's an electronic hobbyist himself. He just wanted to give these away. He had extra stock of them, and he's not looking for, like, addresses or emails or anything like that. So... Right. So, you're not being siphoned into the funnel. Right. Exactly. The sales funnel. Right. No. So, yeah. There's a limited amount, so it'll be first come, first serve on the sign-up. But, hopefully, who wants one will get one in the States. So, thanks to them. Cool. And if people can... You can also click through from theamphour.com slash es. You can click through to their site, and then that actually lets them know. That actually helps support the show, because, yeah, we track clicks on who goes through to their site. So, we appreciate everybody who does that. It's very helpful for the show. We do. Thank you. Yeah. Speaking of stepper motors, did you see my little Twitter video the other day?

**Dave Jones:** I haven't seen the video yet. Sorry. I... But you got it working, apparently. Yeah. Did you do a little dance?

**Chris Gammell:** I was dancing on camera, even. Oh, right. Okay. Yeah. So, I got all three stepper motors going. And what did this thing do? Oh, nothing. What did it actually do? It does nothing. Oh, right. I'm jogging stepper motors. Come on, man. This is like I'm celebrating me turning Allen wrench screws. You know? Like, this is not... This is advanced for mechanical idiots like me. It's not advanced for anyone else. Okay. But, you know, like from a system level, there's just so many steps. Not just steps, but just it's... There's a lot of layers in it, you know, to get to...

**Dave Jones:** But I thought the reason that you bought this thing is that you just assemble it and it just works. Yeah. Like, you seem to be doing a lot of low-level dicking around.

**Chris Gammell:** I am, yeah. Well, I'm trying to... Why is that? ...make sure it's precise. And eventually I got to the point... So, like, I was, like, leveling out, like, the gib and all these different things to try and get it really precise. And then eventually I'm like, this is stupid. I'm going to mess it up. You know, I'm going to run the XY table into something and it's just going to knock everything off anyway. So, I got it pretty good, I think. It's probably within a couple of foul tolerance, you know? And now I'm just going to mess it up and get cutting stuff. Right. Yeah. No, I know what you mean, though. I'm taking forever. I'm nervous, too. I'm a really nervous project person. I always get nervous I'm going to break stuff because I always strip out screws. I'm always really bad about that kind of stuff.

**Dave Jones:** Right. Yep. Yep. I don't know. I can appreciate that. Yeah.

**Chris Gammell:** So, it's been good, though, so far. If people want to see videos, they can go to chrisgammel.com. But they're kind of boring so far. I really want to cut stuff soon, so. Yeah.

**Dave Jones:** I would love to promote my own videos, but they're boring. Good one, Chris.

**Chris Gammell:** Well, they are. You had a good video. I liked your video today that looking at the old electronics.

**Dave Jones:** See, I thought that one was boring because I was supposed to take like 20 minutes to do that. It ended up being like a 50-minute video.

**Chris Gammell:** Oh, I skipped through it. Don't worry about me. Right.

**Dave Jones:** Yeah, I'm sure most people do.

**Chris Gammell:** Yawn. Yeah. I really want to get like old. I think I romanticize it a little too much, but I really like the idea of like old electronic ads, like the old advertising, you know, written by ad men. Yep. And I really want to get one of those like really big blown up and like put them around the lab and stuff. And I haven't really seen them anywhere. People know where I can find those. I think that'd be really cool. But, and I know I'm not going to do it myself.

**Dave Jones:** The ads are some of the most fascinating stuff. And that's pretty much what I looked at. Yeah. I looked at the ads for, you know, multimeters and scopes and other test gear. Yeah. And over 35 years. Right. And.

**Chris Gammell:** Well, some of the projects you'd be like, wow, we don't do that anymore. You know, that is not a good idea anymore. Yeah.

**Dave Jones:** Hmm. And I found a really fascinating one, a bit of retro test gear.

**Chris Gammell:** Oh, really? Which one?

**Dave Jones:** It's the, yes, it's the Hioki 3208.

**Speaker ?:** Oh, that one.

**Dave Jones:** Yeah. They're still around these days, right? They're still making, this was like, I think the late 80s, this thing came out. And it's the Hioki 3208. And it's the CalQ High Tester. So it's a CalQ Tester. It's exactly what the name says. It's a combination calculator and multimeter. And I think it's the most pornographic thing ever. It's weird. Because I'm a multimeter nerd and I'm a calculator nerd. Well, that's true. Yeah.

**Chris Gammell:** I guess it kind of hits all the high points for you. Yeah. Yeah.

**Dave Jones:** It hits all the buttons. No pun intended. So Hioki's still around though? The company's still around? Oh, yeah. Yeah. They still specialize in multimeters. They still sell analog and digital. They've moved into digital now. They used to be number one in Japan in terms of analog meters. And oh, yeah. They were one of the world's leading meter manufacturers.

**Chris Gammell:** They do like panel meters and stuff too, huh? This is like a...

**Dave Jones:** Oh, I'm sure they do. I love that. Yeah. Huh. But no, they're still making multimeters.

**Chris Gammell:** That always amazes me when I find out of a company. I'm just like, really? Sometimes it just amazes me how much is out there that I've never heard of. You know? Because you hear about the big names, right? But then something like this comes along. And it's like, what? What are they... Oh, they make this stuff too? Okay. That's cool. You know? It's like... It just shows how broad the market can be. And...

**Dave Jones:** Yeah. Well, I found an interesting ad that... From Tektronix, right? Yeah. Tektronix in Australia, but they were distributing another company's product. And another company's oscilloscope. Oh, yeah. I think it was Leader or somebody. Yeah, I saw that part of the thing. Yeah. Yeah. Tektronix Australia were actually selling some other brands, company, oscilloscope. Yeah. Go figure. Here's Tektronix, the leading oscilloscope manufacturer in the world at the time. Yeah. Right? By far.

**Chris Gammell:** But that could have been a... They were. You know, it could have been something where it was... They were distributing because they're smaller in Australia, right?

**Dave Jones:** Yeah. Well, they're the local distributor and they call themselves Tektronix, but they're kind of sort of not really... Yeah, they're a licensee. They're kind of like an independent body. They're a licensee and they're probably using the name or something like that. Right. So, anyway, I just found that fascinating. So, hmm. Yeah. I love those old ads. I want to go through and, like, get a collection of, like, all the Fluke ads and then all the Tektronix ads. Oh, that'd be cool. You know, over time and stuff like that. Yeah. So, I really want to devote some hours to scanning some of those ads. So, you know, would you be willing to de-bind it?

**Chris Gammell:** That would probably be the fastest way, right? Because if you rip the binding off all of it and you could scan them all in real fast by using one of those sheet scanners. If you don't want to...

**Dave Jones:** Oh, yeah. Well, but then it's got to be like an A3 sheet scanner. Nah, you know, I've got a very fast scanner here, which can, you know, scan and convert and automatically crop a page in 10 seconds.

**Chris Gammell:** It's all about your time, though. You know, it's not about...

**Dave Jones:** Oh, yeah, yeah. No, but, you know, I... But the thing with these magazines is back in the old days, they used to have an advertiser's index, right?

**Chris Gammell:** Yeah.

**Dave Jones:** So, you don't have to flick through every page. All you do is go to the advertiser's index, which was either at the front or the back, right? And you'd go, oh, Fluke. There we go. Boom. Page 35. Whoop. You know, and bang. Well, I think they still have that, actually.

**Chris Gammell:** It's just no one looks for it anymore. No one bothers anymore, but, you know... Well, I mean, I talk to people about that, or maybe it was even you. You know, they're talking about looking for... Maybe. ...looking for the actual ads because it was exciting because you weren't exposed to it otherwise. Yeah, yeah. That was probably you. What am I saying? Who else do I talk to? I don't talk to anyone. I talk to my dogs most of the time, you know? Right.

**Dave Jones:** Wife, don't talk to her. She yells at me. She yells at you and you just go, yes, dear. Yes, dear. Yes, dear. That's pretty much the end of the conversation. I am learning quickly. Yep.

**Chris Gammell:** No, she's great. Come on. She let me buy a CNC machine.

**Dave Jones:** How awesome is that? I know. That's very cool. Yeah, yeah. Oh, boy. And, yeah, anyway, this combined multimeter calculator, you know, it's totally impractical, right? Right. So it ends up being a shit multimeter and probably a shit calculator, right? Yeah, right. But, you know, this was the era when they did that sort of stuff. You know, they would combine, yeah, let's combine a fax machine, a PDA and a cigarette lighter and we'll combine it with everything, right? They'd jam everything into the one product and it ended up just being absolutely useless. Yeah. Right? Because it'd be shit at everything it tried to do. And they're still trying to do that sort of stuff today with phones. You know, they want to put, you know, little Pico projectors in phones. They want to put little Pico printers in there. They, you know, they're shoving everything in there. Yeah.

**Chris Gammell:** It's like they're making stuff for CES instead of actual consumers, right? That's the idea.

**Dave Jones:** Exactly. And in the end, the most practical item will always win out. Always. Yeah.

**Chris Gammell:** Or cost effective or whatever people actually need, right?

**Dave Jones:** That's... Whatever. Yeah. Exactly.

**Chris Gammell:** The best product for the job. Hopefully.

**Dave Jones:** For the job. Yes. Exactly.

**Chris Gammell:** Hopefully.

**Dave Jones:** And, yeah, and people don't want to compromise with, you know, they don't want everything with the kitchen sink and everything else. It just doesn't work. Be it CAD tools, Altium. Yeah. Or, you know, just anything. It's... No, it's the best product for the job. Yeah.

**Chris Gammell:** Well, it's like you were saying... Speaking of which... You had a battery life on multimeters, right? You were saying that that...

**Dave Jones:** Oh, it's... Yeah.

**Chris Gammell:** It's the same kind of thing, right? It's shit. Sometimes people value that a lot.

**Dave Jones:** They haven't improved.

**Chris Gammell:** Well, it's...

**Dave Jones:** I don't know. I just think, why haven't they improved, right? Fluke, the original Fluke 27, right? It had 1,000 hours battery life from a 9-volt battery, right? That was 20, what, 20, 25 years ago or something. And since then, no other multimeter has touched that, right? They haven't got 1,000 hours. Why not? Because are they lazy? Are the designers lazy? Are they, you know... What's going on?

**Chris Gammell:** Well, you know, a lot of people have... It's part of the consolidation of the chip industry, I think. You know, like, there's... You can get a lot cheaper of a chip. You know, so like an off-the-shelf chip, you can get for $2 versus an ASIC, which you can get for maybe $1, but no one wants to put that money up front anymore, right? So back in the day, you'd have companies that were shelling out, you know, 500 grand NRE, non... What is it? Non-recurring engineering costs. So they'd shell out 500 grand, but then they'd get dollar chips for the rest of the time. Well, until the fab shut down. But, yeah, of course. But companies don't want to do that anymore, so I think that's part of the problem. You know, you can actually optimize for... You can optimize a lot in an ASIC. And when...

**Dave Jones:** Yeah, but you don't have to go to an ASIC to get low power these days. I mean, everyone's using like an MSP4... Even Fluke are using MSP430 processors in their meters, right? The Fluke 87 using MSP430, right? Really... I didn't know that. Pretty darn low power. That's pretty cool. Processor, right? Yeah. Yeah. Yeah, they are switched. Well, it depends, though.

**Chris Gammell:** I mean, so like MSP430 is low power. It is low power, but it also is low power because of sleep modes, right? So, I mean, is the 1,000 hour that you're quoting on the Fluke 27, is that when it's on? Or is that just all told?

**Dave Jones:** Yeah, yeah. That's... No, that's when it's on. The operational life is 1,000 hours, right? And then... But, you know, like often they'll still stick with using 9-volt batteries, right? Instead of using... You know, why don't... Yeah, go rechargeable. ...to sort of somehow package the meter so that it uses C cells or double A's or, you know, a D cell or something like that if it's a thick meter.

**Chris Gammell:** I hear those are reliable.

**Dave Jones:** Those are super reliable. You can put them in a metal box. Yeah, you will. And shake them. I'm sure it'd be intrinsically safe, right? Yeah.

**Chris Gammell:** Toss them up in the air and then drop them and toss them up in the air and drop them. Yeah, well, and, you know, another thing with measurement... I don't know. I just thought that the most... Measurement is op amps. It's a lot of, you know, it's continuous current kind of stuff, right? And you trade off...

**Dave Jones:** Oh, yeah, but it's pissant current. Come on.

**Chris Gammell:** Not if you're doing... If you're doing precision, maybe... I don't know the specs on a Fluke 27.

**Dave Jones:** Oh, yeah, okay. But, no, precision, right? No, the Fluke 27, like, it's only 0.1%, right? Oh, okay. It's not like you have to run a heated bloody... Yeah, reference or anything. ...temperature reference or something, right? So...

**Chris Gammell:** Yeah, that's true. Because that would take a lot. I mean, yeah, you're right. You're right. Yeah. But op amps... Op amps are nothing to trifle with, right? I mean, obviously, we just talked to a company last week that has low-power op amps, but I don't think Fluke 27 is using those. And even those are limited. You know, like, the touchstone part, I've looked at it before. It's a cool little part, that TS-1001 that... Wasn't that... Yeah, yeah. Jared... Yeah, stupidly. Your own is the one who designed it, right? That's what they were saying. Yeah. Yeah. And it's really, really low power, but it's, you know, it's low input voltages, right? And so, like, you know, there are restrictions on this kind of thing.

**Dave Jones:** Yeah, but it's just... I'm sorry. It just hasn't advanced in 25 years and it pisses me off.

**Chris Gammell:** Well, I think this is a good video series, Dave. You try and create a Fluke 27 that beats the battery life, right? You don't even have to run it for 1,000 hours. You could just get the current consumption.

**Dave Jones:** Well, I can do it, right? I can take an existing multimeter that's got good battery life, like 500, 600 hours, and I can replace the 9-volt battery with four double A's and bang, I'm going to get four times and I'm going to get my 2,000 hours or 3,000 hours, right? But they don't do that because they're lazy bastards. No, maybe. Right? It could be that people just don't care.

**Chris Gammell:** At 1,000 hours, you just pull the battery. Who cares, right? I mean, do you have to get it recalibrated at that point?

**Dave Jones:** I don't know.

**Chris Gammell:** I think you're just whining. You're whinging.

**Dave Jones:** No.

**Chris Gammell:** Have a little whinge.

**Dave Jones:** I'm sorry that I want good battery life out of a battery-powered product.

**Chris Gammell:** You and your requirements. I'm a fool. You're a marketer's worth nightmare. Anyway. So this is an interesting, this kind of feeds into a question that my friend had for us this week. So, like, where to draw the line on designs? Nice. So we were just talking about where to draw the line on, that's really more than where to draw the line on marketing. Battery life. Yeah, battery life, specs, all that kind of thing. But where do you draw the line on the actual design of a product, right? So here's the situation. So my friend is working at a company, and they outsource the entire design and manufacture of this subsystem. And when it comes back, he's just, he has to deal with it, right? And so what his question was is, you know, how do you actually make that decision? Because the caveat to all that is everyone goes, oh, well, you just don't do it. But there are times when it makes sense to do that. So when do you decide when to do that kind of thing?

**Dave Jones:** I have found often it works backwards. You have an end date when something needs to be done, and then you need to draw up the lines where you need to draw the line in the sand where, well, I have to do this by this date. So therefore, this is the only method available to me. Bang, that's the line drawn in the sand. It decides itself. Ideally, if I had infinite time, infinite money, right, I would have drawn the line somewhere else.

**Chris Gammell:** Right.

**Dave Jones:** Right?

**Chris Gammell:** Okay.

**Dave Jones:** But, you know, so that's one way to look at it, I guess, is often things are, you know, your hands are tied a lot. You can't just draw the line anywhere, you know, in the best location possible.

**Chris Gammell:** Yeah, because I think many engineers would say, I know personally, I would say, well, I want, you know, I want to do it all, right? And that is sometimes a recipe for disaster, right? Especially if you don't have anything scaled up yet. If you don't have, you know, other engineers to work with, if you don't have manufacturing in-house, if you don't even have manufacturing partners yet, there are, there's a lot of crap there, right? I mean, it sounds, I think we talk about manufacturing a lot and how hard it is, but, you know, it always seems like it's going to be easy at the beginning until you realize, holy crap, eight week lead times are going to like, you know, shoot me in the foot, you know? Yeah. So, yeah, it's a tough question. And I think, I think even more, I think the reality of it is, you know, as engineers, we hardly ever have the choice, right? It's almost always left up to management or executive committee kind of stuff. And that has its own bit of silliness to it. But I was, I was trying to tell him, you know, like he is interested in bringing it back in, which I think is good, at least on some, some aspects, you know, at least if you have to support it long-term, I think you should at least be able to shoot yourself in the foot, you know? It's really tough to try and support someone else's design long-term without being, having a hand in the process and knowing why they make decisions. So at least being able to design it, if not, you know, then turning it over to someone to actually do like design for manufacturing and then actually doing manufacturing. That's a, that's a better scenario, but.

**Dave Jones:** Face it, us engineers are just oompa loompas.

**Chris Gammell:** Sometimes it feels like that. I don't like it.

**Dave Jones:** That's what Sheldon says. Oh, engineers, they're the oompa loompas of the science world. Yep. That sounds about right. Yeah. Oh. All we can do is dance around and wave our hands and, and sing songs and produce.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh boy.

**Chris Gammell:** Well, sometimes you get to be, you get to be creative with stuff, right? There's a, there was a, there was a, there was a really cool post this week. I'm not, I'm not sure about the practicality of it, but a site called Boldport, they wrote a script called PCB mod E. And I'm not sure what that stands for, but basically it's a script software where you put in, you put in placement information and you put in like a weird, weird looking board outline file. And basically it outputs this absolutely gorgeous SVG of like your top level, uh, Gerber file for a PCB. And people can see, uh, what, what was actually output here. I mean, it turns it basically into art.

**Dave Jones:** Uh, right.

**Chris Gammell:** I'm not sure if people actually want that kind of thing.

**Dave Jones:** So it's, so it's, so it's an artistic auto router place or is it?

**Chris Gammell:** Yeah, exactly. It's, it's, it would be like if you had like a ton of board space, if you're going to hit the auto route button anyways, and the auto route's not even going to have any problem with it and you really want it to look cool, this would be it. This is really cool. I mean like, it's just a really cool piece of software. Um, it's, it's a, it's still fledgling, right? There's no DRC for anything. So, you know, you, I'm, I'm, I'm just shaking my head. Sorry. If you're thinking about manufacturability, but if you want it to look cool, I'm horrified. Oh, come on. I think it's cool. This is what Oompa Loompas can do to keep, to get themselves going through the day, you know?

**Speaker ?:** Right.

**Chris Gammell:** I mean, I wouldn't do layout in an Inkscape editor anyways, but it, you know, if you're going to do that kind of thing, or it could even just, you know, you can use it as a generation tool and then you could try and replicate it in layout if you wanted to. I don't know. It's.

**Dave Jones:** Oh, no. You know, you don't see PCBs as art, Dave? No. Do facepalms work on radio?

**Chris Gammell:** Maybe. How do you do a radio facepalm? I think it'd be a facemike. Yeah, there you go. Oh, boy. No. Okay. Well, Dave will not be using that, but people can go check it out. I think it's kind of interesting. Whatever. Right. I saw it on Twitter. I like it. Next. Okay. Well, we probably don't have time for too many more. We could talk about how the chip industry is shrinking. That's something new.

**Dave Jones:** We could talk about how Intel sees some like motherboards. No, no, no.

**Chris Gammell:** This is what we got to talk about. So, a previous guest on the show, Bunny Huang and then Akiba from Freak Labs and the MIT Media Lab. So, MIT's Media Lab is like a cross-platform kind of like development group of designers and stuff. They all toured around Shenzhen and Akiba did this awesome. He's just been writing these awesome, awesome blog posts about all these different places they go to. And basically, Bunny and some company they're working with has set up all these interviews. They're not interviews. They're like site visits. They're tours for everything. And it is amazing. I have been enjoying the hell out of these things. And I really encourage people to go check these out. Let me see if I can find all these. Oh, shoot. How do I get to it?

**Dave Jones:** I can't even find the link. I have to look at this.

**Chris Gammell:** Yeah, it's really good. So, here's some of the places they went to. They went to a contract manufacturing place, a connector manufacturing. That one was really interesting.

**Dave Jones:** Oh, yeah. That would be nice. Yep.

**Chris Gammell:** Next page. They went to Lotus Motors, which is a small DC motor factory, a fabric mall. They went to a sanitary napkin and diaper manufacturing facility, which is like, whoa. Oh, yeah. A lot of different contract manufacturers, a bunch of plastic stuff. Excuse me. I've been getting into plastic stuff recently, just kind of looking at that because of the mill and everything else. I think that is so... If I had to do it over, I might get into plastics. I don't know if I actually would because it's a really hard market to get into and you spend a lot of time in China. But seeing injection molding machines is so cool. And the molds they use and everything.

**Dave Jones:** So, are these video tours? No, no, no.

**Chris Gammell:** No, it's photos and then Akiba wrote everything up. Right. Okay. Really good stuff. But really good detail, too. They went to Huawei. I think that's how you say it. Huawei. H-U-A-W-E-I. They make a lot of networking equipment and stuff like that.

**Dave Jones:** Yes. Oh, they're like second biggest in the world, like behind Cisco or something. Yeah, exactly.

**Chris Gammell:** They're really big. Chip on board, bear die assembly place or attachment places. Nice. Yeah. They went to Accelerator. Speaker factories. Like, tons of really good stuff. I was just looking at these and just so jealous. You know? I just said, I want to go. Why am I not there? Oh, well. Maybe next time. Yep. But. Sure. Yeah. I mean, and they give a good example, like actually interacting with factory owners and stuff like that. And to be honest, what this feels like is what like a Accelerator program goes through, right? You know, they actually get interacting with a lot of factories. And I forget which one it was. I think, oh, it was the speaker factory one. It was just so striking. You know, how many, how many, like how big the market is there? Obviously, like it's, that is a stupid statement to say, right? Everybody knows that it's a big market. Of course. But at the same time, you don't really, I don't think you, even reading this, this scale isn't there because, you know, they're so specialized on like one type of speaker. Was it speakers? Maybe one's speakers. Whatever it was. It was so special. Oh, no, it was the motor factory. It was so specialized that they, you know, they would just, they would make you custom stuff immediately. Like on site, you would, they would just wind you motors on site. So I don't know that, that just kind of really hit me. It's awesome. And just the costs are plummeting. I mean, like it's even more. I don't know how much lower it can go and I think it's going to hurt on the way back up, but for now it's, it's pretty great. Yeah.

**Dave Jones:** Ah, yes. All the exploited labor in China.

**Chris Gammell:** It's great. No, the exploiting is not good, but the, but the, the ecosystem is just so cool. I mean, like, so like here's, there's another thing I had on the list this week for, um, it was, uh, it was a little quadcopter, right? And it really. Yeah. I was saying this. You saw that one, right?

**Dave Jones:** What is it? 50 bucks. 50 bucks.

**Chris Gammell:** It's a PCB, right? So it's nothing fancy.

**Dave Jones:** Well, they, they, they haven't actually done it yet. Oh, that's true. Yeah.

**Chris Gammell:** They say MSRP is, is 50 bucks and they're talking about having a camera on there and everything else. So, so yeah, it does sound like it could be, um, you know, kind of fluffy, but, uh, but you know, like when you look at the board, it's just two chips. And when you think about it like that, when you start pulling everything on chip like that, you know, you have basically one huge sensor unit for all the IMU stuff, all the inertial measurement, and then all the processing. And then you just need motors and you could put the drivers out with the motors and, you know, at that point, damn.

**Dave Jones:** Well, that's, it's a classic example of when you engineer something for volume, right? They're engineering this for volume. That's how they're going to get the $49 price point. Right. You, you, you know, they're putting a lot of, it looks like they're putting a lot of effort. I don't know if it's custom silicon or something in there or, you know, I, I don't know what it is, but it's, um, no, probably not, but they're putting, right. But they're putting a lot of effort to do everything in the one or these two main chips. Right. Right. And then that's it. And they're really trying to bang the cost down on this. Yeah. So.

**Chris Gammell:** Yeah. Low cost is a very, I don't think I've ever really played it in a low cost. Um, I've never really done that. So I really don't understand. I mean, I, I know the, I've seen the formulas before and I get that.

**Dave Jones:** Well, I've, I've done it on some, some level and it's, you know, it's, it's basic math. If you're measuring, you know, if you're making a million of something and each, uh, you know, and if you can lower, you know, the part by a cent or something like that, you know, you've instantly saved, you know, if you can save one cent off your bomb, you've instantly saved 10 grand. So it's worth you spending, uh, what, you know, how many hours of time trying to reduce your bomb by one cent. Right. If a new chip comes out and you rip everything up. It's worth $10,000 of your time. Yeah.

**Chris Gammell:** If you rip everything up because you're going to save five bucks, then of course you do it. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. So it's worth you spending a week just trying to shave, save one cent off a bomb. Right. So, you know, that's, it's just the basic math of it.

**Chris Gammell:** Yeah.

**Dave Jones:** And that's not even getting into all the high volume discount stuff. That's just, you know, that's just your regular engineering bomb cost saving loop that most engineers will end up doing.

**Chris Gammell:** See, the thing that always strikes me is because I was talking about injection molding before and that, that's what always, that's what always gets me is, you know, like you look at like, I look at like a vacuum cleaner, right? It's like a $80 vacuum cleaner that you might see at like Target or, you know, some other store that you go to. And it's like, there is literally like, honestly, the most expensive thing in there is probably the copper windings inside the motor. And like the plastic on it is, is that's, that's, what's crazy to me is like, you know, you get injection molding plastic at like, you know, million, million shot molds, you know, like you're going to pay like a dollar, you know, like, it's just like, it seems so bulky for not much at all. And that's what, that's what always gets me about, about injection molding is just the, once you get past that, that mold cost, it's so incredibly cheap that it's just, it's unbelievable to me.

**Dave Jones:** And I don't know why it's that cheap because making plastics is not easy. They use petrochemicals, right? So it all comes back to, well, you know, you've got to like go and search for oil, which is the industry I used to be in, right? You've got to go do that.

**Chris Gammell:** Well, yeah, but that's all, I mean, that's the thing.

**Dave Jones:** $50 billion and it's all got a, you know, it's all got a scale together. It's all got a, you know, join up together and, and, you know.

**Chris Gammell:** Well, there wouldn't be a plastics injury if you didn't have like a, you know, a transportation industry, right?

**Dave Jones:** Well, exactly.

**Chris Gammell:** Because there's no motivation for that volume. But yeah, that's, that's still crazy.

**Dave Jones:** I know. It all ties together and you end up with your, you know, buying your farting novelty toy for 50 cents, you know? Yeah. It's just, it's incredible.

**Chris Gammell:** Farting novelty toy. But yeah. I guess the interesting question will be if it will go up eventually. You know, there's another, there's another article.

**Dave Jones:** Well, it's got to. I think it's unsustainable. Well, yeah.

**Chris Gammell:** I mean, and, and there's a New York Times article about, about Mexico being the new China. And it's like, of course they're going to keep chasing new markets, right? I think, you know, the Mexico article is actually about, you know, bringing stuff back domestically closer to the U.S. with lower costs still. But, you know, they're always going to keep, they've already started this stuff, right? It's like China stuff's moving to Laos and Vietnam and everything else for textiles and stuff. But eventually they're going to run out or they're going to loop back, right? It's like, oh, well, you know, America's broke. We'll go manufacture there again. You know, it's like. Right. We're going to Greenland and import people as well as materials. Sorry to all our Greenland listeners if they exist. I'm sorry. Yeah. I don't know. That'd be interesting to know. What, if we have any? Are you from Greenland? We have a listener from, so you can see it from our Libsyn. We actually distribute the show and I could see where people are coming from. There's some interesting ones. I mean, there's like, I think there's one in Afghanistan. There's a couple in Iraq. And I think some of those might actually be service people that are overseas for the U.S. at least. Right. Okay. Other countries that I've just, like, I think Mongolia is on there. You know, it's just like, what? So hello to everyone on the far. If you are from a weird place, not weird. Weird is the wrong word. I'm sorry I said weird. If you are from a remote location, we would love to hear from you. I think that is so cool that there's people really far out. I know I shouldn't be...

**Dave Jones:** Did I mention this the other week?

**Chris Gammell:** What?

**Dave Jones:** On the show that I got an email from the head of the electrical engineering department at a university in Baghdad.

**Chris Gammell:** Really? That's cool.

**Dave Jones:** Yeah.

**Chris Gammell:** Free trip. I know. No? Are they going to send you out there?

**Dave Jones:** I think I said, I'm sure I'm big in Baghdad, right? Yeah. That's cool. I'd be mobbed if I turned up.

**Chris Gammell:** Yeah. I only give negative feedback T-shirt. Feedback T-shirt. Yeah.

**Dave Jones:** That's great, man. That's really cool. I mean, yeah, that's really cool. They love my anti-American rhetoric. Oh, there you go.

**Speaker ?:** Right.

**Chris Gammell:** With everyone who is listening in remote locations, I think that's really cool you guys listen. And we really appreciate it. It's really cool. We'd love to hear from you. We should probably get going for now, though.

**Dave Jones:** We should. We're way over. Yes.

**Chris Gammell:** Next week, Mike Harrison of Mike's Electric Stuff will be on the show.

**Dave Jones:** And unfortunately, I may not.

**Chris Gammell:** We're hoping Dave may, but he may not.

**Dave Jones:** Yeah, we're not. Because I am, yeah, I'm almost booked to be in Melbourne. Yes. I'll be in Melbourne next week. Yes. Tuesday, Wednesday, Thursday next week. So that means probably no teardown video either. So no amp hour, no teardown. Yeah.

**Chris Gammell:** You better be making something good out there. We'll see. We'll see whatever it is. Suspense is killing me. Boy. Yeah.

**Dave Jones:** Oh, boy. Anyway, if you have any ideas of what I can blog in Melbourne, because I do have a free day there. Oh, okay. so I'm spending two days doing something else and then shooting a thing and then I'll have a day free where I can blog something else so if you have any ideas let me know cool yeah

**Chris Gammell:** alright well we'd love to hear from you if you're from a remote region or otherwise you can always reach us at theamphour at gmail.com I think that's good alright cool well we'll see you next week or maybe not Dave alright see ya this episode of the Amp Hour was sponsored by electronicsurplus.com electronicsurplus.com not only has hard to find components to put into your next designs they also buy old components so whether you need to liquidate your inventory or need to restock those hard to find components go to theamphour.com slash es

**Speaker ?:** x
