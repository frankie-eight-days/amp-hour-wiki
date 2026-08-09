---
episode: 514
title: Focus, Dammit
url: https://theamphour.com/514-focus-dammit/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released October 25th, 2020. Episode 514. Focus, Stammas.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Focus, damn it.

**Chris Gammell:** You're saying that to me? You talking to me? You talking to me?

**Dave Jones:** You talking to me? I've already decided that that probably should be the title and the first thing we talk about. We just got into this before the show. You're already disagreeing with me, weren't you? You're about to launch into it.

**Chris Gammell:** No, no, I have points of disagreement only because I'm going to try and defend myself. But I think actually your premise is right. So this all came up because...

**Dave Jones:** But hang on. I am one of you, though. Remember that. I am one of you. I am one of these generalists. Okay.

**Chris Gammell:** Right, right. Yeah, so we're going to get back to that generalist versus specialization. That's kind of the discussion that's coming here. So yeah, bingo cards out.

**Dave Jones:** Anyway, how did this come about?

**Chris Gammell:** Yeah, so I have been working with this guy, Bilal, on firmware stuff. And he's a young guy, found him on Upwork, really, really great developer. And he got my ABC board up and running on Zephyr in two weeks, three weeks. It's been a really, really great experience. And he's been doing Zephyr for most of his career. So Zephyr is a new thing, but he's really into it. And so Dave brought this up. He's like, well, yeah, he's focused on this one thing and he's really good at it. And it's like, oh, yeah, you know, like, and I think that is a strong point in, or that's a strong, in strong favor of focusing. I just, I'm not usually like that. So that's why I'm like against the focus, dammit idea.

**Dave Jones:** We're both pretty much generalists, aren't we? I would consider myself, I would definitely consider myself a generalist. Even when I was a full-time PCB designer, right? Right. And that's pretty much mostly all I was doing every day was PCB design. Right. I still consider myself a generalist. Right.

**Chris Gammell:** Well, you didn't stay doing PCB design. You didn't, you know, do only PCB design prior to that. Right. But that's like what a super focused person would do. Right. They were like, well, I just, I do this one thing and like, I'm great at it. Like I will, I will kill it. But like, yeah, that's all I do. And I think, I think that is actually one of the arguments against it in the beginning is because you get pigeonholed a little bit, you know, like if you can't, so like assume, so like Bilal is a great example of like picking this thing that's up and coming and he's a really good at it. And like, I'm very excited for him. I think it's actually gonna be very, a great path because it seems like, like Zephyr, you know, obviously I'm, no one's surprised here. If you've been listening to the past shows, I'm very excited about Zephyr, right?

**Dave Jones:** Well, actually, can you explain? I have no idea what Zephyr is. I've heard lots of people actually, I've seen quite a few people say, oh yeah, I'm a Zephyr specialist. What, what the hell is it? I don't know.

**Chris Gammell:** It's a, it's a, it's a real-time operating system, right? So like FreeRTOS or like Thread, no, not ThreadX, NutX or like, I don't know, MicroCOS2 or MicroC Linux. No, what was that? Micrium, whatever Micrium made and they've been since bought, right? Yep. And so like, they're all basically real-time OSs are smaller versions of operating system. Usually you, it's not full-blown Linux. We were talking, we'll talk a little bit about Jay Carlson's thing a little later, but like, it's not full-blown Linux. It's real-time. So usually it's deterministic. There's semaphores and mutexes and all these different things. I've been talking about this, this RTOS book that I've been reading and it's been really great. But the idea is Zephyr is a, I'm going to probably botch this too. So one of the Zephyr people was actually unembedded. Well, I'll link that in. And she talked about it a bunch. She was great. And so basically, Zephyr is kind of like among different groups now. So like Nordic supports it, ST supports it. There's basically, it pulls in the SDKs from all these different companies, right? So ST, Nordic, Intel. Actually, so this all started because Intel bought Wind River, I think. And whatever the thing was, whatever it was called before that, that's where the core of this started. Then the Linux Foundation got involved. And the idea is basically it's a, it's a open source shared ecosystem now. So now Intel makes a board support package and all the SDK stuff that goes along with it. Nordic does the same thing. ST does the same thing. And now when I go in and, basically when I go and I compile a Blinky example, right? So this is something I just did the other day and I was very excited about it. I compile a Blinky example. All I say is target the Nordic NRF 52840 DK, like the development kit board. And it knows everything to pull in because there's all of these, there's all of this like abstraction layers on top of it. It knows everything to pull in.

**Dave Jones:** Yeah.

**Chris Gammell:** The Blinky, the Blinky file is all the same, right? It's, it's, it's talking to LED zero, right? And LED zero is mapped to the pin on NRF 52840 DK.

**Dave Jones:** Yeah.

**Chris Gammell:** Pin 13 or whatever, but it might be pin 475 on an Intel board. It might be pin 37 on an ST board. But the idea is that it's all abstracted out of there. So LED zero is, is already, it's under the hood. And then it compiles all the required stuff. It pulls in all the SDKs that are required, builds everything up, all of the object files, it links it all together. It builds this thing. There's even a, it even could tie into the flash loader that's in there. You type in this, you know, this high level West build and it does the build. You type in West flash and it downloads it to your board. Now, of course, this is, if you have everything set up and, you know, we'll just ignore that for now. But the idea is that it's at the, at the level, at the application level of like writing a blinky program, it's the same, right? And now you go and write a Bluetooth program and it's the same. And you, you know, and this is very, very high level and, you know, optimistic, but there's a lot of work to get it.

**Dave Jones:** Well, this sounds like, what are you talking about? It has nothing to do with a real-time operating system. It's a cross hardware platform extraction, abstraction layer. Pretty much. The fact that it's a real-time operating system is, is doesn't really come into it.

**Chris Gammell:** I think the reason, I mean, there are very much elements in there, right? So you're doing a Bluetooth thing now and you, you need to have all of the RTOS elements in there, right? So the semaphores and the, you know, the scheduling of threads and all this stuff. And, and that, that's what I think of when I think of like RTOS is, is basically all of the scheduling and the things that need to happen.

**Dave Jones:** Is there any point of using Zephyr if you don't use the real-time aspects to it? That's a good question.

**Chris Gammell:** I don't know. I, so like the reason I look at it, I'm just looking at purely at popularity, right? This is me, this is me hitching my wagon to the, to the cool kid at school. You know, like this is, that's literally all I, that was like the majority of my, you know, I'm interested in generally, but like kind of looking at support and looking at all the things, looking at momentum, where things are going. That's why I'm interested in it. It's very, very possible at some point in the future, it's going to take a right turn, you know, Nordic bails, Intel bails, all these people bail and it just flops, right? That has happened before it could happen again, but I'm optimistic. You know, this is Chris. I'm always optimistic. And so the fact that it's not like that, I don't need an RTOS in a blinky example. It doesn't mean that I won't need one in the future. And when Eli was on the show a couple of weeks ago, you know, he was talking about like, he, he had, he had been sat down at a conference and someone said, look, you can, you know, if you have, I think the example was like a one stoplight town. It's not a big deal, but if you have thousands of people now, you need more traffic lights. You need more. I think that was the analogy he gave, which is great. Right. I mean, because like, yeah, I mean, you can handle all the stuff when it's blinky and it's simple and it's like low level. Yeah, that's fine. But you start doing wifi and Bluetooth and cellular and Laura and all this other crap. And it's like, okay, you need more stuff there. The wheels start falling off the billy cart. Yeah, exactly. And like, so I've used, what's the board called? I have it up there somewhere. It's called a Pycom. So Pycom is like a micro Python based, you know, it's on ESP 32 and it's got all this other stuff and it's kind of, it's not bolted together, but it's like, it's this really high level language and it's really nice for demos, but then like to explore it and use it in a product. It's like, okay, now it's like you're using something that's not designed for that system. Whereas like an RTOS, like Zephyr or something similar, again, please excuse my lack of knowledge. I'm kind of learning this as we go along, but with Zephyr, it's kind of designed for your specific hardware, but that the high level application level layer rather is more customizable. I think.

**Dave Jones:** Right.

**Chris Gammell:** Did any of that make sense?

**Dave Jones:** Yes, it does. Totally.

**Chris Gammell:** Okay,

**Dave Jones:** great. It's just that that's like, I thought it was just an RTOS. And then all of a sudden you went off on this huge tangent about how it's a multi cross platform hardware abstraction layer tool.

**Chris Gammell:** Right. And that's, I think that's the, that's probably is a good, a good delineation too, because that's the reason that, you know, that that's where the momentum comes from is like, okay, Nordic's throwing a bunch of engineers at it and ST is throwing a bunch of engineers at it. And like always NXP has a bunch of engineers thrown at it. And it's like, so you start to have this, like all of these people that are jumping in and kind of contributing to it. It's like, you're going to get other features built into it. And so in RTOS, like free RTOS, right. You can pull in an SD card reader, right. That's like a simple kind of thing. You can set up a fat file system. You can pull that in. But it's not as vetted and it's not as like kind of out there. It's not as like improved upon. And like, you know, you're, you're pulling in this thing. Yeah. You get the SD card reader for quote unquote free, but like, it's not vetted by all of the different vendors and it's, you know, you might have to port it to your system. And whereas if the underneath layer, it's all abstracted, the highlights, I want to write to an SD card underneath layer. Yeah.

**Dave Jones:** If somebody let, let's say somebody from Nordic writes an SD card layer, because they have an SD card thing on their dev kit or whatever. Right. And then, and then it's implemented into Zephyr. If I'm using the correct terminology. Right. So then all these, so then technically it's available, but then how does that, and then it become auto magically available on the other hardware platforms. Does then do then all the other vendors have to go,

**Dave Jones:** Nordic's added ST is gone. Oh, Nordic's added this. I need to make sure it's compatible. That SD library is compatible with our things. How does it all like.

**Chris Gammell:** So like the management at the, so there's like, you know, there's an actual project and a foundation that's like, there's like the Zephyr project that does all this stuff. Okay. Someone is in control of all the, the pull requests. So like today, so Bilal has been working on this BG 95, which is the modem I have on board, right? There's no support for it, but he was able to find some code that was out there that was used for another thing. And he pulled it in. And he's porting it to Zephyr, right? Today he submitted a pull request and that functionality will actually at a pretty high level, I think we'll get pulled up, you know, the pull request for Zephyr. And it's possible that now the work that he's doing will be reusable by other people. So now they try and implement, you know, an interface to a BG 95 modem. All they have to do is say, Hey, here's my serial port that I'm talking to this modem with. And like, that's, that's the quote unquote magic. It's not actually magic, but there's, there's a lot of troubleshooting there, but, this is how I understand it so far.

**Dave Jones:** Okay. But you know,

**Chris Gammell:** it's like you're pointing at peripherals that are like, so in the SD card example, right? Usually SD cards are spy based, right? Not always, but the way I've seen them, right? And so you would point, you'd say like, okay, I have my SD.

**Dave Jones:** For example, probably.

**Chris Gammell:** Yeah. So like the fat file system, I think would be higher. And then I think it would be like, okay, your fat file system is talking to the actual SD card. You do that at the spy layer. And so you'd be like, Oh, spy is on pins, you know, 13, 14, 15, 16, right? Four pins for spy.

**Dave Jones:** And everyone's going to have support for spy. Right. Exactly.

**Chris Gammell:** Yep.

**Dave Jones:** Right.

**Chris Gammell:** And you might have special pins there and you have to deal with that.

**Dave Jones:** But so then that's how it becomes auto magically available across all platforms. Yeah.

**Chris Gammell:** Yes. Yep. Got it. So my first exposure to this was actually a different project, which I'm also very excited about. I was, I helped with the hardware initially and it's public enough now that I think I can talk about it. If not, we're going to be editing this out. But BeagleBoard is working on a Zephyr port as well for one of the TI chips and for a very exciting thing for a gray bus. So I think they've said enough out there that I can talk about that. If not, like I said, I'll be. Hey, who's gray bus. Gray bus is from, remember project aura? No. Remember, it was like the Google phone where you like plug on modules.

**Dave Jones:** Oh God. Oh yes. Yeah. Right. It flopped. It's like a, like it's a cool concept,

**Chris Gammell:** but like from an actual hardware perspective, it's really tough because like the cost of doing that interoperability, whatever. So the idea is basically you have this interoperable bus that basically kind of just self configures. And that's about as much as I understand about it. I'll have Jason back on. So Jason Kreitner is the head of BeagleBoard. I'll have him back on to talk about all this, but it's very, very exciting. And if people are interested in Zephyr and all that stuff, I'll point them at BeagleBoard. And that's probably all I should say, because otherwise we'll cut out too much of the episode.

**Speaker ?:** All right.

**Dave Jones:** So back to focus. Yes.

**Chris Gammell:** Which we've been so focused. Yeah. Right. Focus. Damn it. And. So what about it? I mean, well, the whole way. I'm saying you should have said focus. Damn it to me.

**Dave Jones:** You were saying we're talking about finding like a one in a thousand person who's like, you know, better than a thousand other people. Right. They're so good at something at this one specific thing. And I'm going, right. You probably can't get to that level. And being a generalist, like doing it part time, you have to be hyper focused on that. I'd say it's pretty rare for an individual to be that one in a thousand.

**Chris Gammell:** Yeah. I think almost, almost by definition, right. It's like, you know, how are you going to stand out from other people? You're going to practice it more unless you're like so naturally gifted that like, but I feel like that's, you know, if you read that book grit, it's not,

**Dave Jones:** but it's not a guarantee just being focused. I know people who are a hundred percent focused on something. That's all they do all day, every day. And they still, well, I'm not going to say they suck at it, but they're not hyper productive.

**Chris Gammell:** They're not the top. What is, what is the area of a specialization?

**Dave Jones:** What?

**Chris Gammell:** Is it like something where the field is so big that they couldn't get to the top anyways? Like there's, you know, billions of people doing it. Like what is the.

**Dave Jones:** No, it's just like, I know PCB layout people who are, that's their hyper, that's all they ever do, but they're just not, you know, I wouldn't say they're a standout at it or they're not particularly quick at it. They're not efficient at it. They're not, you know, it doesn't just because you do something every day, it doesn't make you, it means you can do it. Right. But it doesn't make you that one in a thousand hyper productive individual.

**Chris Gammell:** Yeah. All I'm thinking right now, Dave is like, is like you're leading me right into like me talking about my self-help books. Oh man. Like, this is just like, this is like a Venus fly trap for their self-help books. Yeah. It was bad.

**Dave Jones:** Yeah. No, it's like, yeah, it doesn't automatically, you know, you can, you can program every day. It doesn't mean that you're a world-class programmer, right? You can just be a mediocre programmer and that's your job. Right. It's like, yeah, it requires a different level of abstractive thinking. You can play chess every day of your life, practice 10 hours a day. You're not going to beat Gary Kasparov, right?

**Chris Gammell:** That's right. I mean,

**Dave Jones:** it's just, you know, it's one of those things.

**Chris Gammell:** And let me tell you, Gary Kasparov is in a lot of these self-help books that I. Yeah,

**Dave Jones:** of course. Yep. Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Yes. He's in there for a reason. And, but, but on the opposite, on the flip side of that, I, you know, I don't think you're going to become those one, that one in a thousand hyper productive, productive person without doing it every day.

**Chris Gammell:** Yeah. I don't know if that's the other end of the spectrum, but I, I mean, I think, yeah, I think you're right. I think they are, they are very concurrent.

**Dave Jones:** Just because you've done something. Yeah. Just because you've done something a couple of times or you've, you know, it doesn't, you know, even if you're right, like super, you know, your IQ is off the charts and you just absolutely, you know, it's just, yeah. You know?

**Chris Gammell:** Yeah. I think, I think it's like, I think it's targeted, targeted improvement. Right. So like, I feel like I use Greg Davil as an example a lot, but Greg Davil, let me tell you, that guy is really good at assembly. I called him the MJ of home assembly the other day. Right. Michael Jordan. And, but like Greg is practicing all the time. Right. And, and, and, and improving, you know, like he's not like, so I, I wouldn't say rest, you know, people don't necessarily, like, so the, the layout example you gave, like there's like, are they going to classes and trying to get better or faster or like targeted practice at, at that one thing? I would think that that would be the thing that would, if they're doing that targeted practice and then they're still not improving and they're still not moving towards the top, whatever that, you know, top is, that would then be surprising at me. But if you just do it every day,

**Dave Jones:** I don't know. But I'm also talking about productivity as well. There's like, you know, there's this, um, theory out there. I can't, uh, remember who it's, you know, ascribed to or whatever, but, uh, basically says that, you know, like the top, you know, 5% of people, you know, in a company do like 90% of the work or something, you know, it's, it's, it's some enormous thing.

**Chris Gammell:** Oh, this is like the, uh, the 10 X engineer. That's, I think that that's what you're going towards. The 10 X engineer is a, is a fun meme on Twitter.

**Dave Jones:** Okay. Oh, I haven't seen it. Cause they're always a holes, you know, that's,

**Chris Gammell:** that's usually the, you know, so like, so they talk about that. This is a big thing in like software. They talk about the 10 X engineer of like one, you know, like one X engineer has the output of 10 other engineers, right? Sometimes there are these people, but the way it's become a meme is just that it's like, everybody thinks that they're that person. And usually they're not, they're just an a, they're usually,

**Dave Jones:** they're just ordinary. And it's, yeah, that's due to, and I don't think you can, I'm not going to say you can't learn to become that, but it's more like it's inherent in your nature that you're going to be. That sort of hyperproductive person, right? Not everyone, even though you've got the same amount of experience, you've gone the same courses, you've learned the same stuff, you've had the same experience. Someone is just going to be 10 times more productive than you are because you're, I don't know, you're inherently lazier. You're inherently less focused. You're still very good, but you're not as productive as that other person. Right. Even though you can be on the same skill level, someone can actually just be more productive at it than you. So. Yeah. Yeah.

**Chris Gammell:** Yeah. I guess, yeah, I guess, I guess it is, it comes down to like footing, right? Like, so like if you're starting from, so like, okay, you and I assume you and I are working together, right? Yeah. And someone says to us, Dave, Chris, can you both go and do this layout and see who's done first? I would assume that you would be done first. Like I just, I would assume that because you've just done, you have that experience and you have that. Whatever. Right now.

**Dave Jones:** When I was, yeah. When I was doing it every day. Oh yeah. Absolutely. Yeah.

**Chris Gammell:** Absolutely. Right. Right. But so that's like the same output. So I would say that I could potentially do the same kind of like final output. Right. So say we're doing like some, you know, controlled impedance routing of this thing. Right. I could do it maybe slower than you, but I think what you're saying is the, the same two people could have the same output, but one of them will do it more efficiently, faster, that kind of thing.

**Dave Jones:** That's what I'm saying. Yes.

**Chris Gammell:** Right. And, and it's the focus you're saying, it's the focus of that task, that specific task, that gives that advantage.

**Dave Jones:** I'm not necessarily, I'm not saying it, that you can't just focus on it and become that person. That's what I'm saying. But it is a requirement to have that focus.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Right. The focus is not the guarantee of you becoming that 10 times one in a thousand or one in a hundred engineer or whatever, who's hyperproductive. I think that's a part of that is inherent in your nature. Some people just aren't built that way. So maybe. Yeah. Yeah. Yeah.

**Chris Gammell:** Now it's different. You know, if you, if you haven't realized, people are totally different. You're right. Right.

**Dave Jones:** Even though they have the same skill and education level, they can be totally different.

**Chris Gammell:** Right. I think you're totally right. And I think it's, you know, it's also drive and it's also, you know, like why, why are you moving faster? Right. Are you trying to, so like, so I've been talking to Jeff Kaiser a lot lately because he's been doing consulting stuff. And like, Jeff is like the most meticulous engineer I have ever met. And like, I might be faster than him, but, but it's kind of like those stitch in nine saves time kind of thing. Like Jeff might spend more time on it upfront, but it's going to be right. You know? And like, I might get it done faster, but then like, is it done done? You know what I mean? Like that's, so that's kind of the, that's the, the, the might, might be different. And it might be, there's trade-offs as well that like, maybe the speed is more important or more than maybe the quality is more important. Like I think about at Keith Lee, when I was there, you know, some of these engineers would spend six months on a board land because the revs were so expensive. And the, you know, it was so important to get it right. It was so hard to track these things down. It was like six months to do a single rev of a board because you had to, you had to get it right. Of course. Like that's crazy, but that's crazy to me. Like now, like you're thinking about it now. And, but it's just like different inputs, different outputs kind of thing.

**Dave Jones:** Well, that's the art of engineering because the art of engineering is, is trading off, you know, like, is it, do we just need good enough? Like for one project to the next can be very different. I've worked on projects where good enough is good enough. Sure. Right. Whereas like, no others require absolute, absolute perfection. And you need to spend a week choosing the correct screw.

**Chris Gammell:** That's right.

**Dave Jones:** Right. Like seriously, you know, otherwise it's otherwise the whole thing's just going to fall apart. Right. So it's, yeah, you know, that is the art of engineering. So there's no general rule. There's no general, you know, or which is the best approach. It's always the art of, you know, choosing the most appropriate, but.

**Chris Gammell:** Yeah. Yeah. Let's see books, books that I like here, books that I like here. Let's, let's, let's just do a little, a little commercial brought to you by Chris's reading list. Ultra learning by Scott young. That's a good one. Basically, if you're trying to get better at something like, and you want to like meta analysis of like how to like get better and like targeted improvement. That's great. A book that I, I did not like that. A lot of people recommended to me was range. Why generalists triumph in the specialized world. So this might be an argument for this conversation of like focus. I thought the range, the range book was just like, it was blather. I mean, it was just like, Oh, look at tiger woods versus blah, blah, blah, blah, blah. It's like, come on, just give it, give me a point here. You know, I love books that are like super prescriptive. Ultra learning was one of them. Range was not. So, uh, first 20 hours. That's another like fast learning kind of book by Josh Kaufman. And what was the last one I was going to put? I'm just looking at my, my Amazon list here. Uh, I don't remember. Where'd it go? Ah, mastery by George Leonard. That's another good one. So like, that's about like how to, you know, work towards becoming like a master in something, right? You need to have targeted practice, that kind of thing. So yeah, those are my book recommendations for this week. Okay. Thank you very much. Let's cut you off. What were you going to say?

**Dave Jones:** I can't remember now what I was going to say. Sorry. Sorry. Oh, anyway, that's it. More books for me.

**Speaker ?:** No,

**Chris Gammell:** I mean, I think, I think this is a good discussion, but like, I think, uh, I think it's tough. It's endless.

**Dave Jones:** It's endless.

**Chris Gammell:** Of course. Of course. But I think the tough thing is like, so, okay. So now someone younger is listening to us saying this and we're like, yeah, you got to focus if you want to be really, really successful. And it's like, you know, there are risks to that. Right. Oh,

**Dave Jones:** I can remember what I was going to say. Okay. The, the victor is the one, the victor in engineering is the one who gets the job done. I think that's right. Yeah. I mean, Oh, ultimately like whether or not that is the long game or the short game, like the, the, the long game could be the person who got it done. And then there were no issues six, you know, six months later, whereas the victor, you know, it could be,

**Dave Jones:** the person who got it done this week for the trade show. Holy shit. Done. You're a genius. Right. Right. Yeah.

**Chris Gammell:** What's done. Right. Define done. I think that's a great, that's a great point.

**Dave Jones:** Yeah. So, but often that's only with hindsight. Cause as I said, like you could like design something, get it done. And then six months when it's out in the field in six months,

**Chris Gammell:** your boss is like, Hey, we're going to production. And you're like, Oh, that, that we shouldn't have done that.

**Dave Jones:** Yeah. No. And it's like, why did you do that? Like, why didn't you see this? It's like, you know, like then you're, then you're public enemy. Number one, you're the worst engineer ever. It's this fundamental thing. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** Because you were too hyper-focused on something else or whatever.

**Chris Gammell:** Right. So have we gotten to the point of, do, should people focus, damn it or no?

**Dave Jones:** I'm saying it's a requirement to become that. If you have aspirations of being that one in a thousand hyper-productive person, you can't do it without the focus. That's what I'm saying. Yeah. But focus does not guarantee that you'll become really exceptional at something.

**Chris Gammell:** Right. I think that's right. And I, yep. One of the things I think was in that grit or in that, that, uh, one of the books, it was like giving like Tom Brady as an example of like, Oh, well, he didn't play Tom Brady. Tom Brady is a football, sorry, American football quarterback, very famous, a lot of super bowls. And it was like, Oh, well, he didn't focus on football as a kid. He didn't start playing until he was like late in high school. And yet he was like one of the best quarterbacks ever. I'm sorry for anyone who hates the Patriots. I don't care. Um, right. And, uh, uh, and, but yeah, so that's kind of like a counter example there. But at the same time, like when he was into it, he was like really into it. And I think that's another point that brings it up too. Right. Is. So you listen to podcasts with Tom Brady and he's like, Hey, look, I may not have been the best at the beginning, but I kept working on it. And I think that's another thing too. It's like, you think about the incremental progress. If you keep getting better and better, you know, if you keep spending time, like refocusing on your, your, you know, home assembly or your layout or your programming or whatever, you are going to get better over time. And it's, you know, small steps, you know,

**Dave Jones:** but it doesn't guarantee you're going to be the best.

**Chris Gammell:** Never. Yeah.

**Dave Jones:** I don't think anything guarantees that because a lot of that, a lot of that, uh, athletics, you know, when you're talking about athletes of any, almost any description, you know, it comes down to innate talent, not only innate talent, but also innate physiology as well.

**Chris Gammell:** Luck, you know, like they talk about,

**Dave Jones:** you know, how many people are going to beat Usain Bolt, right? Right. No, there's a physiological reason why the man runs as fast as he does. It's not just because he was, you know, right. I know. I agree.

**Chris Gammell:** There was actually another example. There was another example of that too. I forget what book it was in, but it was, I think this might've been an audio book. That's why I'm not seeing it, but it was giving the example of like, if you look at Michael Phelps versus the, I forget the guy's name who won like the 5,000 meter, whatever, you know, like physiologically, they are very different. Michael Phelps is just like, you know, he's the swimmer, sorry, the gold medal swimmer, swimmer from the U S he's like won a ton of medals. He is like all, you know, super short legs, super long torso. Right. And then you compare him to this like marathon runner guy or long distance runner guy. And like, he's just all legs, you know, like, and they're the same height or something like that. It was like some like really great comparison. So, yeah.

**Dave Jones:** Right. I've got a great example. Nick Kyrgios, who's an Australian tennis player. Have you, have you heard of him? Uh, sounds familiar. Not really into tennis. Anyway, he's like one of the world's best tennis players. Like he's up in probably the top 10 at the moment or something. And I think, don't quote me on this, but he was on the Joe Rogan podcast recently or something. I don't know. Anyway, he was, he was talking about how he just basically, he does not have a coach, right? Where he's in the top 10 in the world in tennis. He does not have a coach. He is not stretched in 10. He doesn't do any stretching in tennis. 10 years. This is like unheard of. Right. And the guy, the guy basically just goes out there and does it. Right. And he's top 10 in the world and doesn't even have a coach. Right. Imagine how good he could be.

**Chris Gammell:** I feel like that's a counter example though. Right. I mean, like that's, no,

**Dave Jones:** it's because he's physiologically, you know, gifted. Like he's built to play tennis, you know? Yeah. And, and there's always,

**Chris Gammell:** there's always sub stories there though. You know what I mean? Like there's always sub stories. Yeah. Right. It's not like he's just like walking on the court. He's not like happy Gilmore, like walking on the golf course and hitting a 400 yard drive. Right. Adam Sandler movie. Yeah.

**Dave Jones:** But you just get exceptional people like that who can do it without seemingly without the hard. Well, I'm not saying he hasn't worked hard. Right. But there's others that work 10 times harder. They've got coaches for every aspect of their performance. They're trying to nail down each 0.1 percentage improvement. Right. He's doesn't care.

**Chris Gammell:** Right. Chris Gammell, the aspirational figure skater is never going to be a top. Right. You know, I started, you know, my current age and start doing it. It's like, yeah, I might get decent, but I'm not, yeah, you're right. I'm not going to be a top figure skater. And I think. No, yeah. And it's like, he,

**Dave Jones:** he just doesn't care. He just like, he simply seems to just turn up, you know, he is, has fun and turns up and he wins. Like,

**Chris Gammell:** I don't think that's a great example. I think that's a, yeah, that's, that is an example. I think that's like one of those ones where it's outlier type thing, you know?

**Dave Jones:** Well, that's why I pointed out because it's an outlier. It's because, you know, it's like, like he didn't get there by hyper focusing and being, you know, trying to improve every single, aspect of every single part of the game.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. He, he got there.

**Chris Gammell:** I'm going to rename this show from focus. Damn it. To Chris and Dave talk sports.

**Dave Jones:** Right. Oh boy. Anyway.

**Chris Gammell:** Yeah. It's an interesting topic. I think. Yeah. I think, I think your premise is great. I'm going to keep trying to improve myself.

**Dave Jones:** Oh yeah. I'm not saying don't improve yourself. Yeah. Like, holy crap. You know, that's not what I'm saying at all.

**Chris Gammell:** I think the, I think the interesting thing is like expectation to like that top in the world. Like, okay.

**Dave Jones:** Exceptional people exist. Just accept it. Right. Yeah. Totally.

**Chris Gammell:** Yeah. And work on yourself. I think,

**Dave Jones:** I think that's as hard as you try, you, you may not be, you know, odds are you're not going to be that, you know, Elon Musk. You're not going to be that exceptional person.

**Chris Gammell:** This is actually exactly the thing that I said online today is I'm not going to become Greg Davil, right? At home assembly. I'm going to be Chris Gammell getting better at home assembly. That's what I said. But I think it's important to like, especially in the internet, I think it's really important because, you know, it's easy, you know, Greg, I use as an example because, you know, he's great. Right. But like that, it's so easy to see like all these projects online, all these people doing all these things. And it's like, you know, you don't always see the whole story behind it. And so it's easy to kick yourself and say, Oh, I'm never going to be like that. It's like, well, no, it's just work towards it. Work on, you know, small, you know, small improvements. And I think that, yeah, I think that's, it is possible. It's just, you know, you got to then find your way towards it. Right.

**Dave Jones:** Of course.

**Chris Gammell:** Yeah. Yep. As an example of this, our guest next week, something we already brought up here is Jay Carlson. And Jay Carlson is a bit of, so if people don't know, he was the one who did the $1 microcontroller and he just released an amazing article called, so you want to build an embedded Linux system. And holy moly, he built 10 embedded Linux systems and he talks through all of the pluses and minuses of these different chipsets. And like, he built them all up and he built like 35 prototypes and yeah, we'll be talking to him next week, but like it is.

**Dave Jones:** Oh, I didn't see that. He actually physically built the, oh, yeah. Right. Yeah.

**Chris Gammell:** Yeah. And he talks about the routing of the memory and stuff like that. Well, as, as an example, Jay was supposed to be on the show mid August and he just finished.

**Dave Jones:** Right. I was, I was going to say like, yeah. How long did it take to write, just, just write the article, let alone do all the stuff, like all the hardware and software behind this required. Yeah. Holy shit. Does he have a point of doing this? Is this his like day job? Because this is like just the sheer amount of work. I'm stunned.

**Chris Gammell:** Oh, it's, it's a ton of work. I mean, like I, I don't know. Well, I'll ask him next week. It's, and I guess people can submit questions. We'll put up a question thread too. It, I think was just because it was the next thing to do. You know, like I, I mean, he's built, he says at the beginning of the article, like he's building more and more throwing more Linux systems at problems. Right. Like, and I think from an industrial perspective, it's actually great. I got to ask some questions to him, you know, on a consulting forum and like it, yeah, it's just, you know, when you have, everything has a display, everything has a, whatever, and you need to keep it cost constrained. And, you know, he's actually kind of does not like a lot of the modules you can buy, like the industrial modules he said, aren't worth it. And it's like, Oh, well I disagree personally. Cause the cost of it, but I'll ask him about it next week, but like, and it's kind of like the cost of ownership type thing, but like at the same time, I don't have the skills that he has. So there would be a ton of costs that would be overhead to get to the point where he is. Maybe.

**Dave Jones:** Oh yeah. God, no, I'd, I'd happily pay for some, you know, I'd happily pay 500 bucks for some module that just worked. Right. Right. If I, no, yeah. Serial. Like, even if I'm making a hundred or something, right. If it's a specialized industrial thing, we've talked about this many times over the years is that you can, you know, it's worth paying the money.

**Chris Gammell:** Yeah. You're talking about making test stands, right. That was a, that was a great, great example. Yeah,

**Dave Jones:** exactly. You know, you're, you're making, you know, 10 or a hundred of these items. Yes.

**Chris Gammell:** I think this is moving into production, moving into thousand, 10, thousand. Oh no. Yeah. Of course. Industrial volumes can get there. Of course. So yeah, I think that's, that's a great, great question to have. Like why do this versus that other thing? Because basically I always say like when you're buying a module or you're buying a product off the shelf like that, you're basically paying for someone to yell at, you know?

**Dave Jones:** Right. Target market matters.

**Chris Gammell:** Yeah, totally. Totally. Yeah.

**Dave Jones:** You know, it's, it's everything.

**Chris Gammell:** Yeah.

**Dave Jones:** You wouldn't do, you wouldn't go to, you know, this effort using one of these, if you just wanted, you know, to build one or, you know, a few of, well, he built one. Yeah. Yeah.

**Chris Gammell:** Right. Yeah. If you're not doing for the academic exercise, right. You know, you would buy it off the shelf or whatever. Yeah. I think, I think that's, that's a great point. Anyways, it is extremely long. I found a plugin that I love. It's a, a Chrome plugin called send a Kindle. This worked great with it. And it generates about 130 Kindle pages as like a, as, as an example. And I've been reading at night and it just working through it. And it's been, yeah, it's really, it's really cool.

**Dave Jones:** So you sent this article to your Kindle.

**Chris Gammell:** Yeah. It's cool.

**Dave Jones:** Oh, right. Okay. A hundred and, and it turned into 130 pages.

**Chris Gammell:** That's right. I think they're Kindle pages. So they're short, but like, yeah, it's still like, Oh my God. Yeah. Yeah. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. It's, it's nice too. Cause the plugin will like the, or the, yeah, the Chrome plugin, it'll, it'll like generate most web pages into, into a actual like Moby or whatever the dot E pub thing is. So it'll actually be like Kindle readable, which is nice.

**Dave Jones:** Right. She's just, yeah, that's just nuts. Yeah. He's, he said like, he's setting himself up to be the guy,

**Chris Gammell:** the expert. Oh yeah, that. Yeah, exactly. I mean, when I tweeted about this, it was basically like, this is going to be the document. Anytime someone says Linux for the next five years, I'm going to point them to this. Just like I've been pointing them to the $1 microcontroller thing for the past.

**Dave Jones:** Right.

**Chris Gammell:** How many, two years, two years it's been out or whatever. Yeah. Jay's been on, uh, embedded FM twice. Yep. I think I've talked about it on here. I was very mad that Alicia and Chris asked him back again before we got him on here. So I, I actually had written to him the way I knew that this article was coming as I wrote to him. And I said, do not go back on embedded until you've been on the empire. And he said, okay, I have, I have an article coming out in August. I'll come on then. I said, that's great. So. Wow.

**Dave Jones:** And, and he knows this too, because if you go to his website, there's like four links up the top. It has home about microcontrollers, which is the, the microcontroller article you're talking about that everyone, you know, he explores 21 different microcontrollers or less than a dollar. And now he's added this embedded Linux page. And that is, that is the page we're talking about now.

**Chris Gammell:** Yeah.

**Dave Jones:** And it's just like, you know, Oh yeah,

**Chris Gammell:** it is the microcontroller page is amazing. Like I, that's how I ended up. I used one of the recommended on there, the EFM eight L B one, the laser B.

**Dave Jones:** Yep.

**Chris Gammell:** Nice little part. Yeah.

**Dave Jones:** I suspect though, that the microcontroller page is possibly going to have longer longevity than the embedded Linux page. Yeah. That's a great point. Because there's people are bringing out new modules all the time. It's like, you know, I actually tweeted this the other day because, you know, Raspberry Pi, it's on our list, isn't it? Sure. Yeah. They have released their new compute module four, right? It's been many years, I think, since they had released the last compute module.

**Chris Gammell:** Yeah. I think it's been, no, I think many would be a two, I think two or two or three, I think. Yeah. Yeah.

**Dave Jones:** Two or three years or something. Anyway, if you don't know the, the compute module is just a, a sort of more industrial stripped down version of the Raspberry Pi. So it doesn't have headers. In this case, it's got a high speed board to board interconnects that, you know, you can just plug this module into a, you know, it's designed to be used as an industrial controller. That's right.

**Chris Gammell:** And it just works better article. They talk about like, that's, this is how a lot of Raspberry Pi foundation makes their money, right? That higher volume, they crank out a lot of chips, like there are a lot of boards.

**Dave Jones:** Well, I think, didn't they say I read somewhere that like 80% of Raspberry Pis are used in industrial applications. It's like some huge percentage. Yeah. It's some massive percentage. It's like, that's where most of them are used.

**Chris Gammell:** Yeah. Oh, let's see. Oh, it says over half, over, over half of the 7 million Raspberry Pi. Over half. Right.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. 7 million a year. Wow. That's great.

**Dave Jones:** Yeah. Wow. That's, that's enormous volumes. And yeah, that's not just going to hobbyists, you know, that's yeah. They're using a metric crap ton of these in industrial applications. And if you're embedding it in, you're going to use this, something like the compute module. And anyway, I tweeted, the interesting thing about this is that they specifically advertise right up front that it's going to have an eight year production life. Yes. Yes. Right. And that is one of the major things. It's like, we've discussed this over the years as well. When you design a chip into your system, be it a microcontroller or a, or an FPGA or something like that. Right. Often like if you're a huge organization, you know, not, not just the apples of the world, but if you're some other huge,

**Chris Gammell:** I'd say small business too. Why not? Right.

**Dave Jones:** Oh, well, yeah, but you don't have the same, you know, if you're a small business, right, you're not going to be able to go to the manufacturer and say, right, I want a guaranteed in writing by your CEO that this part will be available for the next 12 years.

**Chris Gammell:** Right. Right. But I think that's, that's more of a reason to try and chase down a module maker that will do that. Right. You need to try and like bundle volume. I mean, we're saying the same thing actually. Yeah,

**Dave Jones:** but I'm going down to the chip level, right? Because we'll get into the chip versus system thing in a minute, but at the chip level, right, I've worked at companies where, yeah, we need a written guarantee from the company, from the board of directors, right? Signed by the board of directors at, at TI or who, whoever it is that they will guarantee this part in production for 12 years, because we have government contracts that stipulate that we have to be able to do that. We're going to supply this for, you know, 10 or 12 years or something. And then these companies have to put their ass on the line and say, yes, we will produce it for the next 12 years. So Raspberry Pi are now coming out and saying, they, they know that this is a thing in the industrial space, right? A lot of companies want this guarantee. Otherwise they won't use your module, your, your, your chip or whatever it is.

**Chris Gammell:** That's right. Yep.

**Dave Jones:** Now the issue though, with Raspberry Pi doing this is that, well, they're dependent on the suppliers of the components used on the module. Raspberry Pi might say, Oh yeah, we'll make this for the next eight years. But if all we know is, is it an all winner processor? What does it know? It's a, a Broadcom, right? So Broadcom say, Oh no, we're not going to make that part anymore or whatever happens. Right. And there's no substitute or they can't easily engineer a direct equivalent substitute. Then, um, yeah, they're up shit Creek and that's right. You, the customer are up shit Creek as well. So anyway, it's good that they do that.

**Chris Gammell:** That is an argument. I think against, against what Jay was saying, right? Like, yeah, you're paying more. Yeah. You're dealing with other stuff here, but you're basically getting that, you know, maybe volume, but really just some, like I said, you get to yell at someone, they're yelling at the chip vendor because they might be bundling more volume. That's what I, that's how I see it at least.

**Dave Jones:** Right.

**Chris Gammell:** So, yeah.

**Dave Jones:** But then it puts, of course, somebody at Raspberry Pi has to be in charge of, uh, ensuring that eight year supply time. Right. So they've actually got a, a tie usually, um, you know, so you've got to tie into the obsolescence notices, the end of life notices for all your parts. Right. So if you want to do this properly, if you're Raspberry Pi and you're making this module, it needs to be somebody's job. And you've got to have a system in place where every single part on that board. Has, you know, a, I, ideally multiple vendors for a start. Right. And then it's got to have, and then you've got to tie into the vendors systems so that you automatically get notified if there's an end of life notice. Yeah. Right. So then you can do a last buy. Right. Then you can potentially,

**Chris Gammell:** nothing makes a component engineer sweat more than a last time buy notice.

**Dave Jones:** Last time buy notice. Yeah, exactly. And then Raspberry Pi then to guarantee to their customers that they've, you know, they've actually promised this eight year lifetime. They might have to buy, you know, if a chip goes, you know, and tits up tomorrow, they will have to buy. And if they can't engineer an equivalent, find an equivalent, they have to buy an eight year supply of it.

**Chris Gammell:** That's right. Yep.

**Dave Jones:** I mean, because that's what they promised. So, you know, it's, it's, it's an interesting aspect of the industry that not a lot of people will ultimately get involved in, but it exists and it's vitally important.

**Chris Gammell:** Yeah. I think it's, it's a grind. I mean, like, so I worked adjacent to the, the, when I was doing like, like sustaining engineering effectively, like we've talked about in the show.

**Dave Jones:** Components, obsolescence engineering. Yes. Seriously. We've, we, we had a component obsolescence engineer at our company.

**Chris Gammell:** Yeah. It's like, you know,

**Dave Jones:** the world's most glamorous title.

**Chris Gammell:** Yeah. Surely it's rough, but, but like, yeah, it's super valuable. And like, and it's, it's, it's, it's not great work, but it's, it's very vital work, I think. So if you have a obsolescence engineer at your, at your company, go and give them a hug or, you know, send them a message on, I guess, no hugs right now. Send them a message and say, you, I appreciate you, damn it. So,

**Dave Jones:** yeah.

**Chris Gammell:** Hug,

**Dave Jones:** hug your component obsolescence engineer day. Yeah.

**Bilal:** Right. Right.

**Dave Jones:** Anyway, yes, very important part of the business that not a lot of people give any thought to at all, because we live in such a, you know, a fast, because everything you see, a lot of people forget, you know, every, every, all these consumer things are being churned over every, you know, 18 months tops or, or whatever, you know, every couple of years. And people don't give a thought to, yep, people still running windows 3.11 on a, you know, some, some industrial computer somewhere. And you know, that, that's a big deal.

**Chris Gammell:** This is kind of, so just to tie it back to the Zephyr thing, this is kind of a reason. So say you are in a consumer environment, right? I am not, not most of the people using Zephyr will not be, but like if you were, and you were, you were on a six month design cycle, it's like, Hey, six months from now, this chip's gone. I know it's gone. We're going to be under the next thing. You know, basically you're writing software at that higher level, firmware software at the higher level. Now, basically you just go and develop the new board support package. You test it for all of the hooks that need to be tested for. And now you have the blinky app should work the same on, you know, the AM three, three, five, eight is the AM three, three, five, nine and AM three, three, six, zero. You know what I mean? And like, you can kind of start to abstract that stuff out. It doesn't always work. And it's kind of, you know, it's its own tough work, but that's the reason to do it. I think as an example,

**Dave Jones:** right?

**Chris Gammell:** Yeah. I think there's probably an argument in the other direction too. Like sometimes I forget. I was reading something earlier this week and it was like, sometimes people, I think maybe it was a hacker news thread, but sometimes people, like over optimize too early and you know, try and make things too abstract. Right. Yes. Depends on the, on the, the task. Right. So like you were saying, like if it's a super tiny little task and whatever, yeah, throw, you know, throw a microcontroller at it, write bare metal code, do this, you know, small thing. So we had a, what was the link on here? I just saw something for like a, there is a, where did it go? Oh man, it's gone. It was on our list, but it was like a, you know, like little tiny, you know, tiny AVR processor that's doing this one little thing. Oh, here we go. Bare metal programming and tiny, tiny AVR zero microcontrollers, right? There's an OMSLow link that we'll link in, you know, that might be the right solution, you know? And like Dave always says, it's like right tool for the job kind of thing of like, that might be it. And you get to the next thing in three years and you can't buy that part anymore. Okay. Rewrite it for the other, you know, the next part that's available. Right. It's like, and that's just part of your, that's, that's how you're doing sustaining engineering is you're just rewriting it every three years. It might not be the most like software-y kind of thing, but it might be the right, the right solution for your company. If you're small, if you, you know, not using much things. Yeah.

**Dave Jones:** Right. Of course.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Cool.

**Chris Gammell:** Are you, are you distracted right now, Dave? Are you distracted by the fact that I tweeted back at you because you tweeted a link to her in the middle of our program.

**Bilal:** What's wrong with you? There you go. Must be excited. He tweeted in the middle of recording.

**Chris Gammell:** This frigging guy. Yeah. Yeah. But he's right. Sorry. I didn't see. Oh boy. All right. What else is on here? Oh, I thought I was surprised you didn't see, I could tell that. So if people haven't seen Dave's video, he goes through his, his office and he's like digging through all this stuff. Oh my God.

**Dave Jones:** Come on.

**Chris Gammell:** You have so much. Here's the, here's how I know that you have so much stuff on your plate right now. And that you're so busy is that you did not see this link. New Zealand startup to build first long range commercial wireless power transmitter.

**Dave Jones:** This is, this is old. This is old.

**Chris Gammell:** This is old. Oh, okay. I didn't think. Yep. Wait, August 10,

**Dave Jones:** August 10. Yeah. Everyone was all over this when it came. I'm behind it. I got it. Yeah. You're behind it. No, it's like, yeah, there's a company called M. It's not on the subreddit. It doesn't exist. You know, yeah, there's a company called N M rod. And they've got some New Zealand government contract to do wireless power. And it's like, yeah, no, no, it's going to change the world. Right. And I get it.

**Chris Gammell:** It's like electromagnetic and it's probably up on a pole. So, and it's a resonance system. It's probably a resonance system. Yeah. Great. But like, that's pretty close to Nimrod, you know, like, and I know that Nimrod actually means Hunter and like, it's not always, it hasn't always been a, uh, you know,

**Dave Jones:** no, it's just, yes, it works in quote marks, but it's not going to be revolutionary. Right. It's just, no,

**Chris Gammell:** at the bottom of the article, it says 2.4 gigahertz. And it's like, that seems like a really dumb frequency to be transmitting power over. It's like, yeah, of course it worked, but like, that's because it's beamed.

**Dave Jones:** Yeah. It's, you've got to use it in the middle of nowhere and it's beamed.

**Chris Gammell:** Right. Yeah. Yeah. And then they, well, they say microwave somewhere else too. It just, yeah, this is not a great article for it, but, uh,

**Dave Jones:** no, no, there's been better ones over the, when it came out, everyone was talking about it and everyone was tweeting. I'm sure it was discussed on the forum as well. It was like, and everyone's just going, yeah, you're, you know? And yep. Yep. Yep. But they were making big, you know, grandiose marketing claims. And of course, of course, of course they do. So, yep.

**Chris Gammell:** Next. Uh, this was an interesting, interesting one. So bare conductive, I don't know. Do you know who they are? The bare conductive folks?

**Dave Jones:** No, I don't, but I've seen this.

**Chris Gammell:** Okay. Yeah. So, uh, they do like conductive paint to, and then they route it to a circuit board. Uh, so Steven.

**Dave Jones:** Oh, I think they might've, um, I, I just didn't recognize the name. I think they might've been the one who sent, I think I've got some of this stuff.

**Chris Gammell:** Yeah, that, that seems right. And they were very targeted in the maker market, but they kind of branched out from that a little bit as well. Okay. Right. Some other things. I think I said Steven's name wrong. I'm sorry about that. DS Smith or Steven DS or whatever. Yeah. I'm trying to edit and post. Uh, but anyways, he's been on the show before and I'll link that into, uh, and so he works there and, uh, but they're talking about why they still have an office. And I thought it was kind of just an interesting, like, okay, so we're in the middle of COVID and it's like, how the hell do you do hardware? You know, this is kind of like the, the thing that we've been talking about a little bit, but like I, you know, you're remote, I'm remote, whatever. We're all remote, but some offices, it's tough, you know, like, and like, how do you actually do this? And so bare conductive wrote about like, Hey, we still have an office. We go in, we're safe, all this other things, but just like the importance of a centralized location when you are working on a physical product. I, I just, I feel for people that are doing it, but I don't know. I don't know how you do it otherwise. You know, like if you just had send everyone here, I guess, I don't know. Home labs are getting better and better. Do you have thoughts on the hardware remote versus a in person building up home offices in labs and stuff?

**Dave Jones:** It depends on where you're, well, what sort of stuff you're working on. I mean, you know, like anyone worth their salt is going to have their own home lab and you can get things done, right? You can power up your prototypes. You can test it with your scope and, you know, multi and logic analyze, you know, whatever.

**Chris Gammell:** DMM, power supply, small stuff. Buy it on Amazon, right? Yeah. Yeah.

**Dave Jones:** And you've probably got the development environment there, you know?

**Chris Gammell:** Yeah. J-Link programmer or whatever, right?

**Dave Jones:** So you can probably do most stuff. It's only like the bigger, harder, stuff. It's like, but like, I don't think it's that, like, I'm looking at their, the bear conduct is former. This is their pre, there's a photo of their pre COVID-19 office space. And it's like, oh my God, that's hideous. I couldn't imagine working in an environment like that. It's just like,

**Chris Gammell:** it is an open office plan is what Dave is saying.

**Dave Jones:** Open office plan. And they're just like, they've got one monitor and, and they're like sitting facing each other. Like no engineer wants to work in a, in, in that sort of environment.

**Chris Gammell:** Have you ever done it?

**Dave Jones:** Uh, no. Ooh, kind of at Altium was kind of like that, but the, the, the low walls, like, you know, you could, you could see other people, but you at least had the low dividing wall. If you know what I'm talking about. Yeah.

**Chris Gammell:** Yeah. Yeah. It's like a half cube.

**Dave Jones:** Yeah. And which is very popular in software circles. Um, because Altium was, you know, almost entirely a software company. Right. So us poor hardware team had to, you know, us poor, four, four guys sitting facing each other going, what the, you know, what the hell is this? You know, like, no,

**Chris Gammell:** please just let me. I'll send you a chat. I'll send you a chat. Yeah. Yeah. It's.

**Dave Jones:** Oh God. No, no, no, no, no,

**Chris Gammell:** Startups. I was in a startup. I was in a startup for about a year. And, uh, I think this is like this, you know, you walk around a, we work, you know, I hate we work with a passion,

**Dave Jones:** but this is the, this is what people think of as a startup, right?

**Chris Gammell:** This is bog standard. Yeah. We work in a glass cube. You're facing your coworkers. Everybody sees everybody like no privacy in a glass cube.

**Dave Jones:** That's luxury. That's luxury. No, no, no, no, the whole,

**Chris Gammell:** the whole office is one big glass. Oh,

**Dave Jones:** the whole office is one big glass. Have you,

**Chris Gammell:** have you been in a we work before?

**Dave Jones:** I've no, but I've been in similar spaces. Okay. Yeah.

**Chris Gammell:** We don't have,

**Dave Jones:** I don't think we have we work here. I don't think it's a thing.

**Chris Gammell:** Oh, I'm sure you do.

**Dave Jones:** We've, we've, we've got similar ones. I don't know if we actually have we.

**Chris Gammell:** I'm sure. Sorry. I'm sorry. Allow me to correct myself. I'm sure you did.

**Dave Jones:** Before that went tits up.

**Chris Gammell:** That's right. Yeah.

**Dave Jones:** No, they are in Sydney. Reworked. There you go.

**Speaker ?:** Yeah,

**Dave Jones:** exactly. You know, I like that's in the startup software wanker idea space, you know? Well,

**Chris Gammell:** and so this is so, uh, you know, there are even more expensive places in Sydney. Yes, they do have two,

**Dave Jones:** four, six, eight, nine in Sydney. That's a lot. That's a lot of space. But I am nowhere near, like I'm no, I very rarely go into the Sydney CBD. No. Like I'm just not there. Right. No. Yeah. So, yep.

**Chris Gammell:** No, Dave, it's for the, it's for the youngs. You were, you were moving towards the olds, you know? Yep.

**Dave Jones:** Yeah.

**Chris Gammell:** But, uh, yeah. So I think that is an interesting, you know, like, so specifically for like, you know, if you're in central London where they're, this office they're talking about is like, yeah, that's, you're trying to pack people in because you're trying to get more people and more done in a really, really expensive real estate area. Okay, fine. But now this is them reevaluating for this kind of thing. Could they do it remotely? Yeah, probably. But what they're talking about is like, you know, like the bare conductive is not a simple product, but it's, you know, it's not like a, it's not a thing controlling an F35 either. Right. So like there are, there are different levels of like how, how much, how much specialized equipment you need. What I think about is, so like I started saying like, well, you know, you could probably send everyone home with some equipment or whatever. And someone brought it to me like, look, I have a $50,000 VNA on my desk. I am not allowed to bring that home or maybe I am allowed to bring that home, but you know, my coworker uses it, you know, my other coworker uses it sometimes and it's just becomes really tough.

**Dave Jones:** Yeah. But in most cases it would actually work out being fairly generalized here, but in most cases it'd probably work out cheaper to buy everybody their own home lab than to rent a space. Right. Than to rent a big space for everyone and all the amenities and all the electricity costs and all the, you know, everything that goes along with renting a large office, commercial office space. Right. It's all, it wouldn't surprise me if it's cheaper.

**Speaker ?:** I think you're,

**Chris Gammell:** I think you are dead on. I think that's exactly where the, the general generic office world is going post COVID. Right. I mean, I think there will be centralization, but I think that companies are going to fall in love. They're like, Oh wow. We, we really don't have to pay much right now. Let's, we're going to share, we're going to hot desk. We're going to, you know, do all these other things. We're going to be at a coworking space, whatever. We're going to, you know, we're using, we work, whatever. And it's like, yeah, okay. That makes, that makes sense. A little bit less so maybe for hardware, but.

**Dave Jones:** I tweeted this the other day. We have hit peak secretary.

**Speaker ?:** Secretary.

**Dave Jones:** Peak secretary. It means that because the other day I was getting my car service. Right. So I was at the local, you know, car dealership. Oil change kind of thing. Yeah. No, no, no, I'm sorry. Oh man. Electric car.

**Chris Gammell:** Oil change. Chris, you're so one year ago.

**Dave Jones:** It's 1500 kilometer, you know, checkup. Right. To keep the warranty. Right. So anyway, there's not much you can do to check it. It's like, have the wheels fallen off? No. Right. You know, it's like,

**Chris Gammell:** there's still a battery and it's monitoring itself. Yeah. That's cool. Okay. Yeah. Guess we'll plug in the computer to the other computer.

**Dave Jones:** We updated the maps for you, you know? Okay. Yeah. Yeah. Anyway, the maps in that are pretty shit, by the way. Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. I just, no.

**Chris Gammell:** Throwback to really, really old episodes of the empire. What I said, we should just have like a interface and you plug in a tablet there, or I guess it would be wireless now, but like, why do you have, I mean, I know why they have it, but I've talked to people at Tesla. Like, why do you have like this specialized screen? It's like, why not make it a removable module? And they're like, well, we don't want to have third party people doing it.

**Dave Jones:** We don't want to have all these other things,

**Chris Gammell:** you know, like absolutely. There are reasons of course, but like,

**Dave Jones:** yep.

**Chris Gammell:** That means you're. Yeah.

**Dave Jones:** But I can like, I think is I would be much happier if they integrated a proper brand into it. Like, give me a Garmin, right? Give me a Garmin map. They should pay for the license for Garmin instead of, you know, or Tom Tom, or at least, you know, one of the big players instead of doing some, I don't know, some weird ass. Yeah. That's, you know, yeah, that's useless here in Australia. It doesn't know half the stuff, you know, it's like, yeah. Anyway, that's beside the point.

**Chris Gammell:** I'm just imagining Dave getting lost at a menu and like, he turns on the navigation. It's like, howdy partner, take a ride up top, you know? Oh boy. Dave, if you want me to do the voice for your navigation system, I'll do it.

**Dave Jones:** I did a voice. I did Dave voice for, I think, I think it was Garmin's way back in the day. I can't remember. I, I uploaded it somewhere and quite a few people downloaded it and put it on their GPSs.

**Chris Gammell:** Oh my God.

**Dave Jones:** So yeah, they've got David. There's a few people out there with Dave.

**Chris Gammell:** Are you an ultimate EV blog fan boy? We have a product for you.

**Dave Jones:** I should try and redo that. If it's like, cause they had like a tool you could download and you could actually, you know, you just had to say all these key phrases, you know, they were like a hundred key phrases or something. Turn right, turn left. Yeah. Turn left. Turn right. Chuckie, you at the servo, you know? And anyway, so peak secretary. It's like, right. So I was talking to the secretary there and you know, front, front day peak. Peak receptionist. Right. So front, front desk receptionist. Right.

**Chris Gammell:** I think peak secretary might've been like in the like late eighties. Sorry. Yeah. Yeah. But I think, I think you're right. Front, front desk for sure. It's like, Oh, you're going to be a tablet in a couple of years.

**Dave Jones:** Your job's gone to a tele present to a,

**Chris Gammell:** yeah, maybe anyway.

**Dave Jones:** Yeah. Yeah. To a Johnny cab, you know,

**Chris Gammell:** Johnny cab. That's right.

**Dave Jones:** Yeah. Johnny, Johnny, Johnny, Johnny receptionist. Anyway, so yeah. And like the conversation led to commercial office property and, um, how, yeah, like she was totally on top of, yeah, everyone's downsizing their commercial properties. Like I know X amount of people who are downsizing their commercial. This, the front desk receptionist knows about downsizing of commercial properties happening. And it's the thing. It's like,

**Chris Gammell:** I think Dave, that statement is a, is a, uh, is a truism. Uh, I think that, you know, front desk people and, you know, assistants are like the, they're the people that know everything because they have to, you know? Yeah. Yeah. Yeah.

**Dave Jones:** Yeah. But you know, it's, anyway,

**Chris Gammell:** and if you're young and you're listening to this and you're an engineer, be nice to that person because Holy crap. Well, they, they will ruin your life if they want to, but also they can make your life so much better. So, and they control the company credit card.

**Dave Jones:** So you the best gossip and they spread the best gossip, you know?

**Chris Gammell:** Well, I didn't mean gossip. I just mean like, they're like gatekeepers, but like, yeah, yeah. Sometimes in a good way, you know?

**Dave Jones:** Yeah. Yeah, exactly.

**Chris Gammell:** Anywho. Yeah, no, that I think you're right about the commercial real estate though. I think it's for sure. It's yeah. It's, it's going to be really interesting.

**Dave Jones:** I mean prices are going to plummet for those who like, like people say, Oh, why didn't I negotiate my lease in my hundreds? If my lease was up in my hundred square meter space, why didn't I negotiate re renegotiate my lease there? It's like, no, I'm not going to magically get it for half. Right. Like I'd be lucky if I got a 5% discount. Right.

**Chris Gammell:** It's just. Cause they got, they got a mortgage on that thing too. Yeah. You're not going to like. No,

**Dave Jones:** they're going to mortgage. And there's various reasons and there's various differences. You know, Sydney's here and Sydney's different. To the U S where they have, you know, CMBS is, which is commercial mortgage backed securities and all that. You know, I won't go into the, I won't turn it into a real estate podcast, but there are huge differences and you know, the prices aren't going to suddenly plummet. Right. Cause these, these properties are tied up in people's super funds. They're tied up in CCMBS is and they're tied up in other. Packages. So they're not just suddenly going to plummet. So.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And they can't just suddenly lower the rent. Right. It's, it's just not, you might pick up some bargains here or there, but in general, no, it's not going to happen. The market is still relatively strong here, so to speak, but everyone is downsizing. So it's like, you know, turtles all the way down. You wouldn't want to be the turtle on top. That's right. Yeah.

**Chris Gammell:** Because the person who rents to the turtle on top. Oh yes, exactly. Yeah. Oh boy. Yeah.

**Dave Jones:** So yeah, it's like, you know, I've, I've downsized, of course I'm, I'm recording this from my new down.

**Chris Gammell:** Dave is sweating. He is sweating his move.

**Dave Jones:** Right.

**Chris Gammell:** He's going to make it, but it's going to be, it's going to be a close one. I'm almost there.

**Dave Jones:** I'm almost there. Man,

**Chris Gammell:** you have so much stuff. I like, it didn't even realize like, oh man, it just is so massive. You need to hire a personal, like Marie Kondo. Does this DMM bring me joy? Does this, does this oscilloscope bring me joy? Like, I also,

**Dave Jones:** I tweeted this in your reply to this on Twitter somewhere or someone's reply. Does it bring me joy? What if the answer to every item is yes?

**Chris Gammell:** Then you got to buy more space. Then you've got problems. Yeah. I think there's a thing like, well, I mean, you better call your psychologist. You know, you don't be useful for you. You know, it'd be useful for you. Here's a product that you should build. That would be very useful for you.

**Dave Jones:** Yeah.

**Chris Gammell:** It plugs into the mains. It's in between your, your, your meter or your DMM, your scope, whatever, and the mains. And all it does is a little ticker and it just says,

**Bilal:** Oh,

**Chris Gammell:** I've used this one hour this month or one hour this year. Yep. Cause I bet some of them, it's zero. I bet a lot of them it's zero, you know? And then like, Oh yeah, this is the, this is, I mean, so this leads back to the, the, you know, having a home lab versus, you know, having just equipment in general. Right. It's like you are guaranteed to need that one thing. As soon as you get rid of it.

**Dave Jones:** Oh yeah. As soon as you get rid of it. Murphy's. Yeah.

**Chris Gammell:** That is the base level fear as well. Right. Yeah, exactly. Oh yeah. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. I, so I'm actually done. I didn't even tell you this. I'm downsizing too. Like I'm getting rid of my desk at M hub. Cause I just don't go in there anymore. Right. That's the space that I'm still going to be like a shop member, but like I had a cart there and I have a desk there and I just have so much craft and I'm now shoving into this home that I live in. And it's, you know, and my wife's just like,

**Dave Jones:** okay. Well, I was clearing out my bunker cause I need more storage space in my bunker. Right. And I'm, you know, clearing some instruments off the shelf and I'm going, Oh, a power vector, um, uh, video analyzer. It's like, you know, a huge, big old school, you know, vector, um, you know, analyzer. Yeah. Right. It's like, Oh God. It's like, yeah, I can, you know, and my mind just goes through of all the possible things that I could do with it. Right. And it's like, Oh yeah, I might need that one day. And ultimately I, I did decide, no, that one's being given away. That's yeah.

**Chris Gammell:** I think that's a good one. No.

**Dave Jones:** Right. It's, you know, it's an old pal video thing. It's like, but yeah, I might use it in the next 1000 videos. Right. Sometime in the next 1000. Oh, I go, Oh, I shouldn't have thrown that away. I need, you know,

**Chris Gammell:** I feel like one thing that would be helpful, like mentally would be one. I mean, you always could buy it back on eBay, right? You can buy it for someone else. Yeah, exactly. Two, you could always rent it or three, you know, a bunch of people around, you could probably be, right.

**Dave Jones:** I could probably get a loaner. Yeah.

**Chris Gammell:** That enough, enough should be like enough to get you past the, cause like, does anyone need more than like one scope? I mean, yes, some people do, but like the majority of people, you need a scope, maybe you need a DMM. Definitely. You need a power supply. Definitely.

**Dave Jones:** I've, you know how many scopes I've got, right?

**Chris Gammell:** Right.

**Dave Jones:** I, I, I, I have currently put three on my benches here. I put two main ones, right? And then I've got a smaller one that just moves around, right? Yeah. I've got the small little key site that just, you know, I love that little thing that moves around. It looks really good on camera. It's just, you know, one that I can physically remove around the other two. I've decided, no, they're going to be, I'm going to have two permanent set up on the bench, on the big bench. And that's it. Use everything else's. Yep. Yeah. Everything else's. Well, either go in or. Is still. Yeah. So, you know, yep. Hmm. Yeah. It's well, cause no one needs 20 scopes, you know? Yeah.

**Chris Gammell:** Right. And we are very lucky, you know, we both get stuff sent to us. It's very nice of these companies to do that. I think that's not the normal case, but like there is always that fear of like, what if I need it? Right. Well,

**Dave Jones:** that's the thing for me. I've always said, and I actually have this on my page. It said, I need to hoard and collect this equipment. Cause I do equipment review comparisons, right. Where I compare one scope, one brand to another. Right. And it's like, I often need to do that on a whim. Oh, and it's like, well, if I don't keep that tektronic scope, how am I going to compare the tektronics brand? It's like,

**Chris Gammell:** well,

**Dave Jones:** you know, but I, but I never use the tektronics otherwise.

**Chris Gammell:** Right. You don't need to keep it out. And it's like, right. No, no,

**Dave Jones:** I don't need to keep it out, but should I keep it stored or should I just get rid of it? Right. Right. It's like, Oh, I don't know.

**Chris Gammell:** It's like,

**Dave Jones:** you know? Yeah. Very tough.

**Chris Gammell:** Yeah. The comparison thing is, yeah. You have some unique constraints, I'd say, you know,

**Dave Jones:** I've, I've got some pretty unique requirements. Yeah. Running a video log. So, you know, your mileage may vary, but, yep. Yeah. Anyway. So, but I'm, I'm stuff is going. I now, I now have a pile of stuff that is being given away. You know, I'm going to call people in this week and well, this next week. Cause I've got one week left. I've got like, until like next Friday to get the heck out of there. So it's like, yeah. Oh boy. Yeah. Not scary. It was just like three months ago. I was saying, Oh, I'm sure I was telling you like three months. Oh, I better start three months ahead. Right. Cause I don't want to leave it to the last minute. And, and I kind of sort of did. Right. I was, you know, three months ago, I started moving benches into here. I shot the odd, you know, video in here and stuff like that. And it's like, still doing it. It's like, Oh geez. Anyway. Yep. So head down, bum up for the next week. Yep. Engineers always get it done on the deadline though. That's right. That's right. We know this. It's a universal fact. Right. I mean, you would probably stretch this out for years if you didn't have.

**Chris Gammell:** Oh yeah.

**Dave Jones:** No, totally. If we didn't have an actual deadline where somebody is going to beat you out, you know? Yep. Yep. Yeah. And I want my $10,000 back. Sure. Right. Right. Yeah. Right. It's $10,000 bond on that place. Right. That's $10,000 dead money.

**Chris Gammell:** That's like a bond is like a deposit. Sorry.

**Dave Jones:** It's like a deposit. So, so you don't trash the place, you know? So,

**Chris Gammell:** right.

**Dave Jones:** Yep.

**Chris Gammell:** There you go. Don't trash the place.

**Dave Jones:** Yeah. Anyway. So yeah. I want my damn money back.

**Speaker ?:** Please. Thank you.

**Chris Gammell:** That'll be a nice boost. Go buy more scopes with it, man. Come on. Go buy more scopes.

**Dave Jones:** Exactly. No, although I am, I'll, you know, I'll give a tour when I'm done, but I've, you know, like I had instruments like scattered all out before, like all around the place before. Now I have just two shelves of instruments that are permanently set up there and I'm not going to move them. Damn it.

**Chris Gammell:** Are they super glued to the shelf, Dave?

**Dave Jones:** Well, no, but I'm like, I might put in K like, I might go cable tie crazy. Right. And, and do various things. It's like, yeah. Yeah. So like, cause I'm, I've said this many times over the years is I can't, as I couldn't, the excuse I made myself is I couldn't keep a properly set up lab. Cause I was always moving the equipment to the bench so I could get it in the shot. Right. It was all about, you know, the camera shot, the framing. Right. It was like, no, I'm going to change. I'm going to change the way I do things. I'm going to bring the product to the bench where I have the instruments. I'm not going to bring the instrument to the blank bench where I'm shooting the video.

**Chris Gammell:** I mean, is there anything sadder than walking into a, a workshop that has like, you know, like the pegboard and then like the person's like outlined all the tools and then none of the tools are actually on the pegboard.

**Bilal:** And not another tools are on the pegboard. Yeah.

**Chris Gammell:** I'm just imagining this with like the outline of scopes and DMMs and everything else. And it's just empty.

**Dave Jones:** Yep. That's why I think I'm going to start cabling, tie stuff, you know, cable, tying stuff down. So at least I have to get out a pair of side cutters to.

**Chris Gammell:** Yeah, exactly. Yeah. You need that little thing.

**Dave Jones:** That little extra barrier there. So, yeah, no, but I'm, you know, it's, it's, I can see the light at the end of the tunnel. I'm going to, I've ordered some custom storage things like custom wood. I tweeted out this website that allows me to build, these custom wood storage things. So I've got these pullout trays. I've bought a whole bunch of trays and I design rather than just like sit them on a makeshift shelf. I went, no, I'm going to build proper custom, like wood shells for these things. So they just fit in there and, you know, and they all just,

**Chris Gammell:** I have a lot of things to move and to do. I'm going to go build some shelves.

**Speaker ?:** Yep.

**Dave Jones:** Yep. So I just custom ordered these and yeah, it was great. Well, I haven't, they haven't turned up yet. They're still being manufactured, but you know, just local, you know, local company that, you know, they've got these, like you can just choose your different type of thing that you want, you know, different type of cabinet or whatever it is you want, and then just tell them the dimensions and then they put it into their CNC machine. And it just magically spits out this fully customized cabinet. You know, it's great.

**Chris Gammell:** That's awesome.

**Dave Jones:** Anyway.

**Chris Gammell:** All right. Well, we'll, we'll look, we'll look forward to the, to the walkthrough when you're, when you're ready for it.

**Dave Jones:** To the walkthrough when I'm done and fully set up. Yeah. Yep.

**Chris Gammell:** Yep.

**Dave Jones:** Although yeah, my, my lights are done. My lights are finished. I'm happy with that. So yeah. And benches are all, you know, Oh, I'm going to get new ESD material. Speaking of which we can segue in this in the last second. And I posted a video from 19, early 1980s.

**Chris Gammell:** Oh yeah. I didn't get a chance to watch this yet, but it looks cool.

**Dave Jones:** It's a, it's an hour and 20 minutes of the guy who invented. Oh, hang on. I'll pull it up. You've used, you saw it though. You actually saw. I haven't watched it yet. No, no, no, no. I mean, I saw it. But you haven't watched it, but you saw it. Yeah, no. Yeah.

**Bilal:** Yeah.

**Dave Jones:** And it's to, Oh God, I got hit my second channel. Unbelievable. Bloody YouTube. I got too many channels. So many channels. What?

**Chris Gammell:** What?

**Dave Jones:** It's on my second channel.

**Chris Gammell:** It's on your second channel. Oh, that's what you're saying. I was just like clicking the link on the subreddit, you know?

**Dave Jones:** Anyway. Yeah. Dan Anderson from Anderson effects. He's the guy who invented the pink poly ESD bag. Right. You know, this is back in the 1960s. It had to do with rockets blowing up and everything. And anyway, he's, he gives this lecture of what is ESD. It's one of the best. What if, and, and practical demo. Those of ESD you'll, you'll ever see.

**Chris Gammell:** Yeah.

**Dave Jones:** Although he's a classic old school character. I'll just leave it at that. So it's almost a standup comedy routine with lots of innuendo and all sorts of stuff in it. It's, you know, he's, he's really old school. So, and he even smokes, you know, he's like, it's unheard of these days, but here he's smoking in this lecture. Right. You know, it's like, it's absolutely hilarious.

**Chris Gammell:** I thought it was a piece of chalk. He's holding it. He's holding a cigarette. No,

**Dave Jones:** no, he's holding a cigarette. Yeah. And he's just like, it's, it's almost a standup comedy routine. And anyway, he's a real character. He's not around anymore, but yeah, somebody sent me this and originally comes from an old, uh, beta max tape and it's him explaining ESD. Anyway. Okay. Yeah. It's great. It's absolutely hilarious. Yeah. Okay.

**Chris Gammell:** Great. And you posted another, uh, video to the 345 kilovolt substation walkthrough. I haven't watched that yet, but that looks.

**Dave Jones:** Yes. Yes. And there's a, I follow up to that, uh, which is the lower voltage section of the substation as well. If you're interested, I, I haven't watched the lower voltage one yet, but yeah, it's this guy who works at a high voltage, you know, a 330 kilovolt substation and he takes you through every, you know, step-by-step walkthrough of the substation. So if you're into the power stuff,

**Chris Gammell:** no touch,

**Dave Jones:** no touch. Yeah. Um, don't get too close. Yeah.

**Chris Gammell:** That's right.

**Dave Jones:** Yeah. It's cool. It's just very interesting. I've never seen a walkthrough before. So that was fascinating. So there you go. Anyway, our amp power is well and truly up.

**Chris Gammell:** It is. All right, man. Well, good luck with the move. Thank you very much. I'll talk to you next week. Catch you next time. Today's episode was produced by Analog Life LLC and was brought to you by, well, some view. Join the other amp power patron sponsors at patreon.com slash the amp power. You'll get a discord invite to chat directly with the listeners of the show. A special thanks today to our corporate sponsor. Me in here.

**Speaker ?:** administered administered administered administered administered in administered Thank you.
