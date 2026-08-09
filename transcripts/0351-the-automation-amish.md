---
episode: 351
title: The Automation Amish
url: https://theamphour.com/351-the-automation-amish/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released July 10th, 2017. Episode 351. The Automation Amish.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. I'm back. What's up, nerd? Oh, my God. I hate computers. Um, well, I'm not sure they're fond of you either.

**Dave Jones:** Eh, bastards. Like, everything's failing at the moment.

**Chris Gammell:** Yeah, you're like in that cycle of like, oh, time to buy new ones or do the resets.

**Dave Jones:** No, just a death spiral of bloody computer issues. Like, my main machine, like, I've been tweeting like crazy about all the shit that's happening.

**Chris Gammell:** I've seen it, yes.

**Dave Jones:** Yeah, my main computer, like, my main editing dual Xeon beast here is like, um, my, it looked like, I thought my hard drives were failed. Like, my heart, my main render hard drive was, had failed. No, turned out to be the SATA cable, giving smart data errors. As in smart, smart, the acronym, smart, the hard disk, yeah, thing. As I'm sure most people know about. Um, yeah, pain in the ass. Yeah, turned out to be the bloody SATA cable. Nothing wrong with my drive at all. Um, and then my lab machine died. Windows, like a Windows 10 update just killed my lab machine. I can't even repair it. Windows 10 repair doesn't work. So I've got to nuke that machine. Okay. Um, and then my internet at the lab doesn't work, or it's on the blink. It's intermittent for some bloody reason I haven't figured out yet.

**Chris Gammell:** Oh, man. So what are you going to do about it, man? Switch to Linux?

**Dave Jones:** I don't know. Linux ain't going to work if your internet's on the blink either.

**Chris Gammell:** No, that's true. Uh, but you could, you could start to, um. Everyone said that. I mean, you've over, overclocked everything, right? Or you, you have like really over-specced machines, right?

**Dave Jones:** No. No. Oh, no?

**Chris Gammell:** Oh. Nope. I was going to say, if you did, you could go and just use it all with, uh, virtual machines and then.

**Dave Jones:** Oh, right. No, no.

**Chris Gammell:** If you have a problem, you just wipe it out and reload it. You know, that kind of thing.

**Dave Jones:** All the Linux fanboys come out of the bloody woodwork. Just stop it. Half of my shit works on Windows. I've been using Windows for 20 years. It's been working just fine. This is the first time ever that I've, like, a machine is like.

**Chris Gammell:** That's, that's, that is incorrect. What? You've, you've literally started another show the exact same way. I hate computers. Yeah. Oh, yeah. I don't remember what show.

**Dave Jones:** Yeah, but it's usually like printers or some other shit. No. Windows has never.

**Chris Gammell:** We've done this before. We've done, no. We've totally done this one before. No, no, no. I know it. No. Okay. I'm going to go listen to every, uh, first three minutes of every episode. You go back and find. Just to go prove you wrong. Do it.

**Dave Jones:** Where, find where I can say that Windows has completely ruined my machine that it can't even recover. I bet you it's, it's, it's, I can never recall it happening. And Linux has its own bunch of crap.

**Chris Gammell:** Of course. It is not, no, that is, that is not the answer. You're, you're right. Yeah. Exactly. But I'm just saying this is not the first time you've complained about this stuff.

**Dave Jones:** No, I hate computers. They, they always suck ass.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, also what sucks ass, I'm trying to get this bloody thing working. I got one of these, I, we've talked about this in the past. A, um, TI sent me this, um, uh, kilometer wave radar thing. Oh, yeah. Right? Yeah. I got one of those eval kits. Right? And, um, yeah. I thought, oh, that's exciting. I want to play with this thing. It works at 80 gig. Right? It's a, you know, this whiz bang chip. It's like chip of the week. It's absolutely killer. Right? And, um, and at a bloody well, does it work? I follow their all the-

**Chris Gammell:** So is it like the dev kit doesn't work or what?

**Dave Jones:** No, the dev kit does not work out of the box. I swear. I've tried on two different machines, um, and, and two different operating systems.

**Chris Gammell:** Got any PebCab going on there? No? No. PebCab?

**Dave Jones:** I followed their instructional video to the letter. I followed their instructional guide to the letter. So what's the, uh, what's the, like, just- Like, the first issue was that it doesn't detect the serial ports properly because it generates two serial ports. One's for data and one's for, like, comms and stuff. And then it talks to, like, a, uh, a web-based app, like a cloud-based demo app. And, um-

**Chris Gammell:** Oh, I see. So their software guys are all writing JavaScript and their hardware guys are all writing serial terminals. Yeah. Right.

**Dave Jones:** The serial, yeah. And, like, it can't even detect, like, Windows can't even detect the ports properly. Like, it's just, oh, my God.

**Chris Gammell:** I've had the, those, those are the most frustrating ones because it's like, well, it happens on every system where it's like, it just doesn't detect it. You probably don't have drivers installed. Usually that's the answer, right?

**Dave Jones:** No, no, no. I managed to get the drivers working. I managed to get the app to communicate. So I thought, yes, problem solved, right? So I managed to actually solve that issue temporarily. Anyway. And, and then, no. Like, and it talked to the, it said connected to the board. Everything's fine. I'm running their cloud app. I connected to the cloud app. Everything's working. And then there's just no data coming out of the thing. So it's like, oh, my God.

**Chris Gammell:** You can just start sending, like, a $50 tablet with the, with the heart, with the e-mail hardware. With the e-mail hardware. Yeah, exactly. It's made for some crap-ass media tech processor, $50 tablet. And it just, yeah. Yeah, but it'll work. It'll work for the first, you know, two hours of operation. And that's what most people use the demos for anyways. You'll go, oh, that's interesting. Moving on.

**Dave Jones:** So anyway, I went on the support forum and I haven't, I've, they now want me to provide screenshots of what the dumps of what the serial thing.

**Chris Gammell:** Don't you have, like, a young Padawan that could be doing all this stuff for you?

**Dave Jones:** Yeah, I do. But he tried it as well and it failed for him. Oh, man.

**Chris Gammell:** Maybe you made the wrong hire there. You got to get a different Padawan.

**Dave Jones:** No, he's just busy doing shit at the moment, you know. Yeah. Like, it's a low priority thing.

**Chris Gammell:** That is a common thing with DevKit specifically. I mean, because, actually, I was talking to someone today about, you know, the software side from chip companies, right? Each, what did you, he said something like, each dollar you spend on the software is a dollar is taken away from the margin on the hardware, right? Right. So, and especially like, you know, like a big chip maker, right? They are, they are focused on the margin around the chip itself, right? Any support activity.

**Dave Jones:** Well, that's their business. They make money from selling chips, right?

**Chris Gammell:** And they make good money from it, right? And so, anything that erodes that, it's, you know. And I say good money in that they have priced in the margin or, you know, supposed to be high just because they have a lot of support, you know, support the fab, support the sales staff, whatever. So, yeah. So, yeah. It's, it's, it's very common for people that don't regularly use dev boards, right? Especially if you're like buying them off, you know, you know, you buy them from an online distributor. It's surprising how many times they still show up with a DB9 port on them. And you're like, uh, okay, where do I plug this in? I, my, my MacBook doesn't even have regular USBs anymore. So, it's like, you know, I got to.

**Dave Jones:** Well, this one actually forces you to use the Chrome browser. So, too bad if you don't like Chrome. Like, because it uses a Chrome plugin. You've got to install a Chrome plugin to work. Oh, really? Oh, yeah, yeah, yeah. You've got to install two different plugins before you can get the thing to talk to the TI cloud. Oh, wow. Yeah.

**Chris Gammell:** That is interesting, too, that I think that a lot of the, you know, a lot of the technology, it follows, it follows the, the trend of available software engineers as much as anything else, right? And so, that'll continue to happen, I think, in that, you know, it might have been in the past, you would have some application built for your, you know, so enough people are using Windows, and you build this thing in Java, because you can get Java programmers, no big deal. And now, it's like, well, it's a lot easier to get a lot of, you know, JavaScript developers, and then you just get that one guy that ties the JavaScript implementation or the, you know, the browser-based implementation over to the hardware. Right. And if that breaks, you're, you're up crazy, you know? It's crazy. Yeah.

**Dave Jones:** Anyway, I'm totally deflated now. I was very excited. I plugged it in, and I thought, oh, yeah, I'll do a quick video on this, and nah, nah. It's going to take days to solve this problem.

**Chris Gammell:** I've spent, you know, two or three days getting a dev kit off the ground. Yeah. And that's like, that's just to, to blinky or just to, you know, just to, you know, Yeah, yeah, yeah, of course.

**Dave Jones:** Yeah, mine is just running the out-of-the-box demo. Like, it's supposed to work out of the box. And I almost went down the wrong rabbit hole, right? Because I, like, because I opened the box, you know, and it gives you a nice little card, which gives you a link to the, you know, the quick installation guide or the install, you know, the dev kit manual or whatever. So I'm reading the dev kit manual. It says, oh, it's got all these demos and stuff. Right. And I go, great. This is exactly what I want. And I want to be able to, like, just a quick demo to see the radar system working. I can wave my hands in front of it.

**Chris Gammell:** Yeah, right. Yeah, right. Yeah, that's the thing they show that the software guy, or sorry, the sales guy show off, right? That's what they want to do.

**Dave Jones:** So it's talking about all this stuff. And then it's, it's going, oh, it's available in the dev kit software. So I go look at the dev kit software and I'm going, oh, shit, look at all this. It's, so I downloaded it and it's all the source code. Like, there's no executable to run. And then I'm going, shit, I've got to install Code Composer, which is TIA's, you know, thing to do this. And I thought, you know, this can't be right. And I eventually stumbled upon a demo video that they had online of this thing and show you how the out-of-the-box experience works. And they go, oh, just go to this web address and you use this online cloud thing and it just works. And it's a serial port. You don't have to install the Code Composer and all that. And I went, dole. That wasn't clear out of the box.

**Chris Gammell:** Right, right, exactly.

**Dave Jones:** I think it might be one tiny line in the installation manual or something, but it's like, it's not obvious. So I almost went down the rabbit hole of installing Code Composer and running, you know, compiling code and doing all sorts of stuff when I didn't have to.

**Chris Gammell:** And that's what it is. It's like, I've been in that situation too, where it's like, you basically like, you flail and then you look for, you know, you start Googling, you start, you find a forum post, you're like, oh, that's close enough.

**Dave Jones:** Knowledge kicks in, right? Then your technical knowledge kicks in. Well, not always for me, buddy. Yes, right.

**Chris Gammell:** Oh, like that, you mean? Oh, yeah.

**Dave Jones:** Yeah. Like it goes, oh, yeah, it must be this. It must be this, right?

**Chris Gammell:** I can do this. I've seen this one before. This looks, yeah, you start pattern matching. You're like, oh, this is probably, I probably have to rebuild the Windows kernel.

**Dave Jones:** Yeah, yeah, right. Or something like, yeah, you just like, your mind just goes to the most complex issue it could be, you know, because you're a technical person and that just instantly pops into your head. You get all these technical things that can go wrong and you think it must be that and you go down that rabbit hole and you just go insane. Yeah, they put you in a straitjacket. Anyway.

**Chris Gammell:** So, I've had a fun side project as you've been talking here too. I found five separate tweets where you're talking about how Windows 10 borked your computer. Don't say Chris Gammell doesn't follow up on things, folks. Yes, but never has it not recovered.

**Dave Jones:** Never.

**Chris Gammell:** Right, right, right.

**Dave Jones:** Never has it totally nuked my hard drive that I cannot even repair it.

**Chris Gammell:** Wait, let's see. Let's see. I can find that one.

**Dave Jones:** There's been quite a few Windows issues over the years.

**Chris Gammell:** I tried to update Windows 10 and we couldn't. Wait, is this recent? No, this is August 2015.

**Dave Jones:** Oh, yeah, that was on my, yeah. Yeah, I tried to update Windows 10 on my Xeon machine here and it doesn't support my board. It doesn't support my dual Xeon motherboard.

**Chris Gammell:** Oh, man.

**Dave Jones:** Which is not surprising. I don't blame it for that.

**Chris Gammell:** Twitter. Yeah, good old Twitter.

**Dave Jones:** I was just having a bitch because I wasted half a day trying to do it, you know.

**Chris Gammell:** Okay, don't worry. I'm not going to hold it against you. Well, we all know that, you know, using a computer and high-level software is not as simple as blinking a light bulb. No.

**Dave Jones:** How do you blink a light bulb? You can't do it mechanically, I've heard.

**Chris Gammell:** Yeah, so we were, before the show, we were watching Krasnow's latest video and then we found all the other entries. This is a weird-ass prize, but I kind of love it. I mean, it's just like, it's reminiscent of... Tell us the contest, son. Yeah, it's the Flashing Light Prize 2017. I have no idea who started this. I probably should have read this.

**Dave Jones:** Right, it's probably in the FAQ or something, you know.

**Chris Gammell:** A grand prize of 200 pounds. So, obviously, they're pommies.

**Dave Jones:** And they're flashing systems on Twitter. That's all we know.

**Chris Gammell:** Brock Craft, Peter Knight, and James Larson will be the judges. These are all the things that we're literally reading off the website right now. But what we've been seeing is we've been seeing a lot of fun projects pop up. And it's making me reminisce for the days of the 555 contest.

**Dave Jones:** Yeah, the 555 contest that I told you would be a...

**Chris Gammell:** What? A bitch and a half to...

**Dave Jones:** A bitch and a half to... To administer, yeah. To manage. And you admitted I was right in the end.

**Chris Gammell:** Yeah, you were right in the end. That is correct. There's one for you, buddy. There's one. But already there's been...

**Dave Jones:** Sorry, who are the judges? Peter Knight and James Larson. They don't ring a bell. I'm sorry if you should ring a bell.

**Chris Gammell:** I'll try and find them on Twitter later. Right.

**Dave Jones:** Yep.

**Chris Gammell:** But yeah, so we found this because... Well, I've seen people intermittently talking about it on Twitter.

**Dave Jones:** The only reason I found this is because it popped up on Mike. Mike did a video and then...

**Chris Gammell:** Yeah, Mike was doing one. Right, exactly.

**Dave Jones:** And then Applied Science, Ben Krasnow, popped up.

**Chris Gammell:** Right, right. I went, what's this? Yeah, so lots of fun entries. And we found out it's going until August 1st. So if you're listening to this and it's not August 1st, 2017, you too can flash the light bulb. So we were trying to figure out... So you said no mechanicals, right?

**Dave Jones:** Apparently, you're not allowed to do it mechanically. It has to be electrically done. Right.

**Chris Gammell:** Yes.

**Dave Jones:** And I think I saw... I haven't watched all of Mike's video, but I think he used a relay. So I'm not sure if that's allowed.

**Chris Gammell:** Right.

**Dave Jones:** Or not.

**Chris Gammell:** Well, they're saying no shutters, though, too. So you can't just block the light and then move it, right?

**Dave Jones:** Yes, you can't block the light. The filament has to go off and on. It's got to be a filament, none of this lead rubbish.

**Chris Gammell:** Right. Right. It's got to... Yeah. Too modern. Too modern. Well, you had an interesting idea. I... Yeah, like... Maybe we don't want to say give this away, huh?

**Dave Jones:** No, I'm going to give it away. I'm going to blow my wad here. I mean, where are you going to get one, right? Where are you going to get one? Yeah, I'm going to blow my wad here. Okay. Jesus. Like, I thought it was too easy to make it small... Too easy and obvious to make it the world's smallest or the world's lowest part count.

**Chris Gammell:** Yeah, you didn't watch Ben's video.

**Dave Jones:** Right. You know, but, like, that was just too obvious, right? So I would go for, like, the biggest or the most complicated. So I had an idea. Find an abandoned lighthouse and then flash that sucker at, like, a half a hertz. Come on, Andy.

**Chris Gammell:** Come on, photonic induction. Yeah, I know. We know you're out there.

**Dave Jones:** It's totally a photonic induction. Yeah. Yeah. Or make it, like, the most ridiculously complex way to flash a filament bulb possible.

**Chris Gammell:** Right, like a Rube Goldberg style. Yeah, yeah, yeah.

**Dave Jones:** Rube Goldberg style flasher. Yeah, but then that's going to be mechanical.

**Chris Gammell:** So it'd have to be an electrical Rube Goldberg. Maybe you could, like, have it, like, hop from a...

**Dave Jones:** Or whether or not it can be mechanical and then the actual flashing is electrical. That might be allowed, you see.

**Chris Gammell:** See, this is why it's hard to run contests, because then a-holes like us, we go and ask these questions. Yeah, I know.

**Dave Jones:** We just want to...

**Chris Gammell:** You've got to really plan for every contingency and every...

**Dave Jones:** Every stupid idea, yeah. Like, that comes from people like us, you know.

**Chris Gammell:** Yep, yep. Yeah. Well, it was really fun, though. So I'm looking forward to seeing all these prizes. There's quite a few entries already, so... Yeah. Yeah. Well, don't get, you know, don't get discouraged. I think the thing that I like about this, and whenever I talk about contests, right, like, the thing that I always think is... The reason the 555 contest was even remotely interesting, and it was Jerry's idea in the first place, right? So... Right. I take no credit. I just tell...

**Dave Jones:** Yeah, we discussed it on the Amp Hour. Didn't we come up with the idea on the Amp Hour or something, or after an Amp Hour episode or something?

**Chris Gammell:** I don't remember. I just credit it all to Jerry. Right. And so the thing that's interesting about it is just that, like, having, like, one simple constraint like that, right? So that's great. And then I think Hackaday did a one... Was it one square millimeter? No, not square millimeter. The square centimeter contest or something like that. Square inch contest. Right. Yeah.

**Dave Jones:** And we always wanted to do the 1K code contest.

**Chris Gammell:** The 1K... And I think someone did something like that.

**Dave Jones:** I think someone might have eventually done one, but we've been wanting to do that since, like, we first started the show. I think we had the idea for that. Right, right. Give us your best project in 1K of code. Right. You know. And if other people want to do it, they are there. Yeah, David, he is nodding his head. David over here, he's going, yep, I'll enter that. Employees of EEVBlog are not allowed to enter if I run it. Oh, sad face.

**Chris Gammell:** No, I think Hackaday would do one of these too. Let's see. Right. Yeah.

**Dave Jones:** Yeah, but... 1K code. And, of course, you have to do it in Assembler because, like, there's no other way to fit. You don't have to.

**Chris Gammell:** You're not going to do as much interesting things. Oh, well, yeah. You probably can't do as much stuff. Right. So.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. So those kind of, like, constraints are really fun.

**Dave Jones:** Yeah, I love the constraint-based contests are good.

**Chris Gammell:** Yeah. Yeah, because, like, the ones where it's, like, super open, like, the... I mean, even, I guess, an XPRIZE is, you know, constrained. It's just a ridiculous constraint of, like, you know, go to the moon or whatever they... They're doing the Lunar XPRIZE, stuff like that. The Lunar XPRIZE, yeah. Kind of. Yeah. The other extreme.

**Dave Jones:** Which they failed, unfortunately. The one that I was involved with, which was the Audi Lunar Quattro one. You remember it came to my lab. They actually bought the actual Lunar Rover to my lab. The huge Lunar Rover. Oh, yeah. That's right. Yeah, yeah, yeah. Right? And, yeah, they finally had to pull out. Oh, no. It was... Yeah, yeah. That was, like, six months ago or something. They had to... Yep. So, sadly... I think it's still... Technically, it goes until the end of this year, doesn't it? The... I thought it went until... Or the end of next year or something.

**Chris Gammell:** I thought it was, like, in a trust. I thought it went until it went. You know what I mean? Like, until someone got it.

**Dave Jones:** No, no, no. I think there was a deadline. Oh, okay. Whether or not they're going to extend it, I'm not sure. But we'll have to check the Lunar XPRIZE website. We haven't kept up the date on it.

**Chris Gammell:** There are different XPRIZE as well. Yeah. Oh, yeah. You can go to XPRIZE.org and then there's Active Prizes. So, there's Google Lunar XPRIZE. You get $30 million for five teams. They're in the testing and certification phase. There's the Learning XPRIZE. Oh, wow. These are cool. The...

**Dave Jones:** Yeah, they... The Adult Literacy XPRIZE. The Audi Quattro won one of those prizes. It was, like, it won one of the stage prizes or something.

**Chris Gammell:** Oh, man. I'm going to have to spend some time on this. This is cool. Yeah. So, we'll put a link in. There's a bunch of active stuff. They're in different phases, though, and stuff like that. Boy. There's a lot of money here. What am I doing talking to you, man? We should go build something, yeah? Oh, yeah.

**Dave Jones:** We'll just start from scratch and build it.

**Chris Gammell:** We'll just, you know, just jump in whenever. A lunar.

**Dave Jones:** Yeah. Rover.

**Chris Gammell:** Blah, blah, blah. Send something to the moon. No problem. Yeah. Peace, guys. Yeah. Yeah. Well, good luck to people doing the flashing lights thing. You can win not millions, but hundreds of pounds.

**Dave Jones:** Fortune and glory, kid. Fortune and glory. That's right. Fortune.

**Chris Gammell:** That's right. Yep. Great stuff. Well, we should mention as well, since I brought up the 555 contest and Jerry, the unfortunate but true news. It has been verified.

**Dave Jones:** Well, it's about a week and a bit old now.

**Chris Gammell:** Yeah, of course.

**Dave Jones:** Because we didn't do a show last week, we probably could have, and we would have been Johnny on the spot with the news, but it's old news now.

**Chris Gammell:** We've never really been that timely, you know?

**Dave Jones:** No. No, we haven't. Stupid weekly schedule, you know? Like, five companies go bust in a week. Right, exactly. In our industry, you know?

**Chris Gammell:** It's like, we can't even keep up.

**Dave Jones:** Yeah, sadly, Cast AR, Jerry's company, Technical Illusions, or formerly Technical Illusions, has shut its doors. It's insolvent. It's just, bam, Gonski.

**Chris Gammell:** Gonski, yep.

**Dave Jones:** Yeah, and based on Jerry, well, I haven't actually spoken to her apart from a tweet that she replied to me. Right, she said she has free time now, so. She has free time, so presumably she was marched out the door with the rest of them.

**Chris Gammell:** Oh, I don't think there's that. No, come on.

**Dave Jones:** Well, no, no, no. Like, she's still a shareholder, right?

**Chris Gammell:** She's still, like, a huge shareholder. But it takes a while to shut that stuff down.

**Dave Jones:** Yeah, but obviously, based on her tweet, they're probably not still working on stuff. I think they're-

**Chris Gammell:** No, I can't imagine there. I'm sure they're just shopping it around.

**Dave Jones:** They're shopping the company around. Right. But whether or not, it sounds like, see, there's two ways to shop a company around. You shop the company, which is just the IP, right? Right. Which is just the patents that they have. Yeah. Which she took from Valve. You know, Valve gave it to her in a nice gesture and said, here you go. They're your patents. And which, of course, she would have had to, which she has signed over the rights to when she took all the investment capital in. Right. So, Jerry doesn't own the patents anymore. She's just a shareholder in the company.

**Chris Gammell:** Right. Any kind of, yeah. And that's how it's designed, too. So that- Yeah, exactly. They can't go after them, right? Yeah, yeah. Right.

**Dave Jones:** So, the company owns the patents. So, the company owns the IP, and Jerry's just now a shareholder in the company, just like, you know, a bunch of others. And so, yeah. So, there's two ways to shop a company. Either shop it just based on its IP. Like, that's the only thing that people want, the IP. To sell the patents, sell any other tech, which you may have prototypes or systems or whatever, code or whatever. And the other is to sell the talent or a combination of both. Right.

**Chris Gammell:** An acqui-hire, as they call it.

**Dave Jones:** An acqui-hire. Or is that what it's called?

**Chris Gammell:** Oh, yeah. Usually, that's when there's less than valuable IP, but you really want to get the employees. You want to get the employees, yeah. So, another company will buy it for a token amount with the, you know, basically, like, an employment contract that incentivizes people to stay.

**Dave Jones:** So, whether or not, I'd be interested to know whether or not, like, Jerry is done with it or whether or not, like, she would go with the company. Right. Or other talent, you know, Rick and other talent would go with the company if they were able to sell it for presumably pennies on the dollar because maybe. Because they're in desperate straits, like, they're out of business. So, you know, it's not like they're in a commanding position to, you know, sell the company. It's basically entering a formal liquidation. So, presumably, some sort of firm will come in and manage the sale of the assets, be they IP and or talent, I guess. But, I don't know. It's complex legal stuff, I'm sure. Right, right, right, right. Which we have no idea about.

**Chris Gammell:** Well, and another thing about companies, too, is that sometimes when the corporate structure is set up and all the funding is set up, the people that are doing the funding get their money back first, that kind of thing.

**Dave Jones:** Oh, yeah, right. I'm sure that. But they don't have any money. Well, yes. So, when they sell it off, if they just sell off the IP, then the money goes to the, yeah, the original investors first. Yep. So, that'll all be in the contracts and whatnot. But as well as the firm who's managing the liquidation, they take their million dollar chunk, probably. You know, they take their big, very lucrative to, you know. I joked on Twitter the other day, somebody who was shutting down, Theranos, was it Theranos? The, they were, who was?

**Chris Gammell:** Snake Oil.

**Dave Jones:** Yeah. Anyway, it was one of those, you know, ridiculous companies that were going to fail anyway. And they were, there's this company that specializes in just selling the assets. Oh, that's right. Like the chairs. And they had like 500 chairs and 500 monitors and like desks and stuff.

**Dave Jones:** And that's the thing.

**Chris Gammell:** Like that's one of the, they said that was like one of the hottest startups in the, in Silicon Valley is the, is the people who liquidate startups that fail.

**Dave Jones:** Yes. Yes. So, I tweeted that and yeah, I thought that was, yep.

**Chris Gammell:** Yep. Hmm. That's fun. Yep. Yeah. Well, I mean, I saw a bunch of the people that were Cast AR folks. They came to my meetup that was out. Oh, okay. I mean, the meetup that I run out in San Francisco. And so I got to talk to some of them, but you know, sounded like it was unfortunate and, but not wholly unexpected from what I could tell, you know?

**Dave Jones:** I, I, I, my spot, unfortunately my spidey sense was saying they would, it was just too long without hearing anything. I can understand the stealth aspect of it, but it was just, I don't know. I always wonder about that kind of stuff. Yeah. Yeah. But like, I was hoping obviously that, oh, that magically, you know, at the end of the end of it come out with this, you know, they'd win and, but yeah, I, but they simply ran out of money and that's what happens. Like once the, like the money literally runs out overnight or, you know, like we've, we've got a week's worth of money left and there's no more investment. Runway.

**Chris Gammell:** It's called Dave. Runway.

**Dave Jones:** Runway. Yes. Right. And, and they don't, and that's the problem with a company that's not actually selling anything that doesn't have any income stream. It's just, everything's outgoing. You know, they're, they're just bleeding cash until they either get bought out or they win. Or they win. Or they win.

**Dave Jones:** Or they win.

**Speaker ?:** Or they win.

**Dave Jones:** Or they win.

**Chris Gammell:** Or they win. Or they win. Or they win. Right.

**Dave Jones:** But I don't think they had any income, right?

**Chris Gammell:** No, no, I can't, no. No, no.

**Dave Jones:** No. So, yeah. Hmm.

**Chris Gammell:** Well, we'll try and get Jerry on again at some point in the future. Yeah. Yeah.

**Dave Jones:** That'd be cool. Yep. So, to find out all the gory details of that. That's a shame. So.

**Chris Gammell:** Yep. That's, that's what happens with the old raising money and stuff.

**Dave Jones:** Yeah. Once the money runs out, game over. Game over, man. Game over. Sorry, I can't do the, I can't do the accent.

**Chris Gammell:** What's that from?

**Dave Jones:** Aliens. Alien.

**Chris Gammell:** Oh, I've never seen it.

**Dave Jones:** Game over, man. What? You've never seen Alien?

**Chris Gammell:** Nope.

**Dave Jones:** Oh, what?

**Chris Gammell:** Sorry. Oh. I don't like Alien movies.

**Dave Jones:** Oh, what? Yeah. What is wrong with you?

**Chris Gammell:** I just, they, they freak me out, so. Oh, God.

**Dave Jones:** Oh. You'll gotta cop a bunch of abuse over that.

**Chris Gammell:** Well, I can always edit it out, maybe. Right. Yeah. Anyway. So, you know what doesn't scare me? What? This is a terrible segue coming. Cheaper cables. I'm actually really interested in this. So, Ian, who we've had on the show before, from Dangerous Prototypes, he's been living in Shenzhen for a couple years now. Yeah. And they keep kind of busting out new services, kind of interfacing the maker world to the Shenzhen world.

**Dave Jones:** To the Shenzhen world. Yep.

**Chris Gammell:** Yeah, and this is another, so they've got like dirty PCBs and dirty laser cuts and I forget what they call them.

**Dave Jones:** Oh, I didn't know they did dirty PCBs. I didn't know they.

**Chris Gammell:** Yeah, yeah, yeah. That's all Dangerous Prototypes. Oh, right. They do dirty PCBs. They have like a 3D printing service. And I think they have a laser cutter service. Right. And maybe even stencils or something. Right. But just, you know, basically taking advantage of the super low cost, on-site manufacturing capabilities and then interfacing it to the rest of the world, handling logistics and shipping and all that other stuff.

**Dave Jones:** So, this new one solves a big pain point.

**Chris Gammell:** Exactly. And this is what I'm most interested in is because, well, it's not even, I guess this has been about a month, a little bit, well, a couple weeks old now. But it's called Dirty Cables. And basically, you can go and spec out a cable type and then they'll get it made. And, well, yeah, like you alluded to, the pain point is just handling cabling is, I mean, I used to do that too. And it's terrible.

**Dave Jones:** You want a custom cable in your product. You want a custom board-to-board interconnect cable. You know, it's got like a Molex connector on each end and you want it a specific length and colors and, you know, number of wires and everything. Like, you can't buy them off the shelf usually. You know?

**Chris Gammell:** Right. Yeah. Well, there are. And I think we've talked about it in the past. We have. I was doing, I was buying the Seed Studio ones with the Grove connector, which is a four-pin JST 2mm.

**Dave Jones:** But Murphy will ensure that it's not suitable for your particular project and you've got to go custom, right?

**Chris Gammell:** Oh, maybe. I mean, I designed literally around that, though. Like, that was the idea. Not around the connector, but around the cable, the assembled cable, which you could buy. Yeah, because you could buy it for 50 cents or whatever. Exactly. And, like, it was a SKU on the shelf. Like, that's what I targeted because, like you said.

**Dave Jones:** SKU, for those who don't know, SKU, stock keeping unit. It means basically an in-stock item that you can just buy off the shelf.

**Chris Gammell:** Well, yeah. It's like a unique identifier of a product that someone's making. And it means when someone says off the shelf, it's going to have an SKU, right?

**Dave Jones:** So, you can specify that in your bill of materials. You just go, it's this manufacturer, this part number, this SKU number. Right.

**Chris Gammell:** And if you go and make your own cable and then you sell it to someone else, you're going to also give it an SKU because you want to. Yeah. So, anyways, but I think that is totally, you know, it's not always the right solution, right? Sometimes you will have a custom cabling need, but you're going to pay for it in pain. And, like, AutoCAD drawings.

**Dave Jones:** Right, you've just got to deal with the company and you've got to, yeah, yeah.

**Chris Gammell:** Well, and stateside, trying to get, like, a cable manufacturing stateside. I mean, this is just a really intensive amount of work, right? And so, people that don't know, like, if you want to get a cable made, usually you've got to go and find someone with the right cable crimping machine, right? Crimping is, like, the people have probably done that before. You could buy a hand crimper, but your forearm will quickly cramp up. Crimper becomes cramper. That was terrible. And then you have, like, a special type of metal crimp that basically mechanically bonds to the wires because you're creating a pressure seal between the metal of the crimp and the metal of the wire. And then once you do that, you have to then go and insert that now crimped wire end or wire ends, more likely, into some kind of housing that will actually end up being the plug. So, like, all those actions, it's just, it's terrible. It's really, really terrible. And so, they're starting.

**Dave Jones:** So, you want someone to do all that crap. You don't want to be dope. If you're crimping your own cables, you're doing it wrong. Right.

**Chris Gammell:** Right. Well, I mean, it's okay for one prototype, but if you can design in. Right. No, no. Yeah. You can design in the cables.

**Dave Jones:** Maybe if you're making 10 units or something, it's okay, but, you know.

**Chris Gammell:** Right. Or if you have, like, really custom, like, if you, yeah, if you have, like, a really custom need, like, say you need a cable run that's, like, 200 meters, right? You probably are willing to put the stuff on the end because you're not going to be able to buy some off-the-shelf 200-meter cable with, like, a, you know, a four-pin JST.

**Dave Jones:** We had to do that all the time when I was working in our production environments. Like, we'd have all these customized test jigs with these massive hundred-way cables, and we'd have to do our own cable looms and solder on the cable connectors. And I have fond memories of doing that. Oh, yeah. And then getting your hundred-way connector backwards. Right. Because you use the left-facing diagram instead of the right-facing diagram.

**Chris Gammell:** Right. And what's the most important piece of equipment in that scenario? Time. No, a label maker. A label maker. Yeah, man, label every single wire. Each wire has its own label.

**Dave Jones:** Which means jack shit if you get it back to front.

**Chris Gammell:** That's true. Yes. You're right.

**Dave Jones:** Oh, man. It was like, you know, like, because we had lived. Oh, anyway.

**Chris Gammell:** Any industrial field engineers, like, they know, they're cringing in pain right now, too. They're all nodding their head. Yeah, right, yeah. Yeah, been there, done that.

**Dave Jones:** Yep. Soldered that D25 backwards. Yep. Yep.

**Chris Gammell:** So, anyways, this is exciting. I'd love to hear if people have done this. I haven't tried it yet. I will at some point, so.

**Dave Jones:** I'm sure it just happens very smoothly. It pays you money and you get your cables. You give them a diagram and, you know.

**Chris Gammell:** Well, you actually, there's an online, like, builder, basically. Oh, online builder. Oh, I got it. It's like a drag and drop.

**Dave Jones:** Wow. Fancy, fancy.

**Chris Gammell:** So, yeah, this is exciting, seeing, you know, we'll need to try it out. And, like I said, if anyone's tried it out already, we'd love to hear about it. There is a sample kit as well. Yeah. There's a sample kit available in the store for $9.95. So, if you want to see what you can actually get in terms of, like, it.

**Dave Jones:** So, can they do any type of connector you like? Can you just specify? No. No, no, no. Right.

**Chris Gammell:** There's a fixed menu. Oh, okay. But that's the best thing, man. I mean, like, you should really.

**Dave Jones:** Yeah, no, because your decision's made for you, right?

**Chris Gammell:** Right. Exactly. It's a constraint system, right? That's what you really want. Right. So, yeah. Yeah. Cool. Well, I wish them the best. Excellent. What else is on the list? Well, once your cable's done, what else do you need? Dave. I don't know. You're going to tell us, obviously. You need an on-device voice assistant.

**Dave Jones:** No, you don't. No, you don't. Pretty much the same.

**Chris Gammell:** No, you don't. No? No. This is interesting. This is a new one. No. We had talked about, what was it called? It was called Jarvis, I think. There was a Jarvis one. It was based on Raspberry Pi or installed on Raspberry Pi. And this is another one called SNPs. I don't know what the hell it stands for. Probably some kind of acronym. But basically, the interesting thing about this, right? So this kind of gets back to what I ended up talking to John Oxer about with security and with connecting all over the world. You know, if you want... So say you, you personally, Dave, you, were going to get an Alexa. Right? All these internet-connected whatever Alexa is.

**Dave Jones:** Why the hell would I get one of those?

**Chris Gammell:** Just play along for a second. No. But say you were going to... All right. I'm going to get an Alexa, right? Thank you. I'm going to get a... Whatever, the Echo or the... There's a new one. The screen that kind of looks like the chumby. But basically, you know, you say like... Oh, I'm going to mess with people now. Alexa, turn on the light, right? Or Alexa, buy a dollhouse.

**Dave Jones:** Flash my filament bulb at 0.5 hertz.

**Chris Gammell:** Oh, there you go. Yeah, right. Alexa, turn on. Alexa, turn off. We just won the contest. Sorry to anyone who actually has one in their vicinity. But the idea being that... Okay, so like following the chain of like... So you're talking to the device. It's listening for the trigger word. Here's the trigger word on device. You know, it has probably some kind of chip on device listening for that trigger word. And then it sends off a request to the cloud. The cloud then talks back down to your Philips Hue bulb or whatever it is. And then... Exactly. Right. Is there a point here? The problem is that... It's just stupid. It's what John talked about is when the internet goes out, your bulb doesn't work, which is stupid. Yes, you were correct about that. But the idea is if you're going to build an in-house assistant, right? So again, this is what we were talking to John about a bunch. I was talking to John about. Someone did skip the show. So then you can create like a more local network, right? So then basically you could just go over Wi-Fi. And that's really the idea is that's what needs to happen for faster response time. The difference being that, you know, if you have... If you need to get some kind of like neuro-linguistic processing NLP unit on board, it's not going to be as good as something that's trained against lots and lots of different words, like a Google assistant or an Alexa assistant or whatever. So that's the whole point.

**Dave Jones:** It's also not going to be as good as just a mechanical switch.

**Chris Gammell:** Yeah, that's true. Who did I talk to about that? I met up with someone. It was someone in San Francisco. They said they were installing a new thing in their house. Oh, it was Joe. One of the guys who's giving a bunch of talks out there. He was saying he just installed a bunch of new stuff. He's like, yeah, and I just did it with digital stuff. I'm like, you're going to rue that day.

**Dave Jones:** Can you foresee a future where, you know, all the self-driving cars and all this Alexa bloody voice commanded... Computer. ...lights bullshit. Computer.

**Speaker ?:** Right?

**Chris Gammell:** Hello, computer.

**Dave Jones:** Can you envisage a future where there will be a whole community of people who will just like not want to do this out of like principle? Just because it's like, I don't know, they might be called old schoolers or something. I don't know. They might be just like resist all this automation shit because it's just like...

**Chris Gammell:** You mean like the Amish?

**Dave Jones:** I don't know. What? The new modern version of the digital Amish.

**Chris Gammell:** The digital Amish. I like that.

**Dave Jones:** TM. There's a T-shirt. Digital Amish. TM. I'm a digital Amish. Yeah, right, right. All right. No, I'm an automation Amish or something. There you go. Yeah. Right. Like I can picture people... Of course.

**Chris Gammell:** I mean, it already is happening, right?

**Dave Jones:** Well, it's already... You know, like giving an interface or whatever. Yeah, I mean, there's probably examples out there that aren't immediately coming to mind. I'm sure there's people who, you know, don't just, you know, like are refusing to use technology just because like even though they can, it's like they just don't want to and it's just becoming too much and like they just like the feel of... I think they're called old people, Dave.

**Chris Gammell:** Old people.

**Dave Jones:** No, no, no.

**Chris Gammell:** You're rapidly entering this group. I mean, there are some benefits to it, but yeah, I know what you mean. I mean, like I don't... I don't know. I don't think it's going to be any kind of like groundswell thing. I think it'll just be like, yeah, some people will, some people won't. The ones... The things that are actually useful, yeah, they'll, you know, they'll... You know, there is benefit to doing some of this stuff.

**Dave Jones:** I think it's unavoidable for the things that are genuinely universally useful and it's just stupid to do it any other way but automated. Then it, you know, it'll win out. But, you know, I think there will be a lot of stuff that will be, you know, people will just want to do it the old-fashioned way because it's just better and simpler. Like, a light switch will always, always be better, simpler, cheaper, more reliable than any automation system in the future. Any. I don't argue with that. There will always be value in the light switch, for example. Like, I cannot envisage a future where an automated light switch is so fundamentally better concept that you'd just be dumb to use a light switch.

**Chris Gammell:** I think the main thing being that... I can't see it. It's like, it's because we're thinking in terms of, like, systems that we know now, right? You can't imagine a... I don't know. What would be a good example? You can't imagine, you know, using a PC when using, you know, one of those paper reel calculators work great, right? Because the paper on the paper reel calculator is always cheaper than buying a new computer. However, most people don't use a computer to do, you know, adding sums and stuff like that for accounting. Hmm. It's the idea is that it's just going to open... It's going to be some new opportunity is going to make it... You know, I think the thing is that the actual opportunity... We're thinking in terms of light switches, but the actual opportunity in, say, lighting is probably stuff that we haven't thought of yet. I don't know what that would be, but I assume that most of the applications that will actually make anything like this catch on have not been invented yet and or have not hit the mainstream yet.

**Dave Jones:** Hmm.

**Chris Gammell:** Yet to make a difference. I have to apologize as well. Apparently, the fireworks here is July 5th and apparently the fireworks are not over. Either that or it's just the usual Chicago gunfire. One of the two.

**Dave Jones:** Right. It's that semi-automatic fireworks.

**Chris Gammell:** You're right. I was thinking about... So, you know, like... You know, Chicago has a legitimate gun problem, which I don't joke about. It's really actually really bad.

**Chris Gammell:** It's one of the highest... Yeah, it's really bad. But I was thinking about... So, Alicia from Embedded, she used to work on the ShotSpotter, right? Which was like this cool system that would just, you know, record instances of like high impulse sound. Oh, I see that.

**Dave Jones:** It's a website, right? And it maps it, doesn't it?

**Chris Gammell:** It maps it, but there's hardware involved as well. Right. But I was just thinking about like, man, around this time of year, it's got to just be going nuts. Like talk about false positives.

**Dave Jones:** Isn't there like an app on your phone or something that you can tie... I think I saw this just recently. App on your phone that can tie into that ShotSpotter or something. Oh, probably. But then, like if there's a, you know, like a public shooting incident, like everyone, like your app kicks in and it tells you where the gunshots are coming from. Oh, interesting. I don't know. Well, that would be good.

**Chris Gammell:** Yeah. Like kind of like one of those alerts that your phone can't ignore. That'd be good. Only in America. Sadly, yes. Pretty much. But we'll move on from that. Anyway. But yeah, just false positives. Right. So, yeah. So, I don't know. I just think... So, this kind of system is interesting because it seems pretty accessible. You know, I've seen... Well, we've had... Were you on the show when Gerald and Bertrand were on? They were... Audeem. Do you remember them?

**Dave Jones:** Well, I don't know. We've done too many shows.

**Chris Gammell:** Well, we had those guys on, on the show. And they were doing a similar thing where it was like... It was on... I think it was a MediaTek processor. Maybe... What's the other cheaper one? It's either MediaTek or the other cheap one, like the BM, whatever, Broadcom or someone else. But it was like an A11, A13 processor. And basically, they had put some of this stuff onto hardware.

**Dave Jones:** All winner, perhaps. Maybe it's the all winner.

**Chris Gammell:** Oh, it might have been all... Yeah, you're right. It might have been all winner. That's the other one. And yeah. So, I don't know. Like, it's... I think there is lots of... I think there is a lot of value, rather, to, you know, doing this stuff on hardware. If you're going to do voice, I think it is good to put it locally in terms of whether or not voice is actually needed. I... That's a different question, right? So, like you said, there are always going to be the digital Amish. I'm sure that I'm talking to one of them. But I think, you know, like, the more I use it, the more it's... There are some nice uses, you know? Not like the very first world problems that I'm solving, right? Like, oh, I've got avocado on my hand and I need to turn on the radio or turn on my podcast, right? It's like, okay, come on, Chris. Yeah. But, I mean, at the same time, it's nice. I get a lot less avocado on my phone.

**Dave Jones:** Smashed avocado, first world problem.

**Chris Gammell:** Yes, right. Avocado toast. Sorry, we... The scourge of the Aussies.

**Dave Jones:** Right, that's a... That's why you can't afford real estate in Australia. Yes, you know all about it. Yeah, yeah. It's an Aussie smashed avocado. Yeah. Aussies will get the joke. Yeah.

**Chris Gammell:** Yes. Oh, they talk about it here now, too. I see it all over the end. Oh, really? Really? Okay. It's stupid.

**Dave Jones:** Right, it sort of made its way over the pond.

**Chris Gammell:** Yeah. Yep.

**Dave Jones:** All right.

**Chris Gammell:** Yep, indeed.

**Dave Jones:** It's a great metric, you know? Yeah. Google it. Smashed avocado on houses. Can we stop talking about freaking automated voice command crap? Sure. What else? It makes me want to go and re-watch Firefox. Is it Firefox?

**Chris Gammell:** Firefly?

**Dave Jones:** With the movie, Firefox.

**Chris Gammell:** Firefox.

**Dave Jones:** Firefox with... Oh, goodness.

**Chris Gammell:** This is why he's in the old group, folks.

**Dave Jones:** Clint Eastwood. Clint Eastwood. Firefox.

**Chris Gammell:** Firefox.

**Dave Jones:** 1982, where he's a pilot and he goes and steals this Russian, you know, this new Russian jet or a new Russian spy plane and he has to command it and he's got to think. Like, it's all this super automated thing and it's like, it could read, like, you've got to think to turn left and it turns left, you know, kind of, yeah. And he had to think in Russian to be able to actually, you know, so that the system would, you know. Because he couldn't think in English and then translate it.

**Speaker ?:** Of course.

**Dave Jones:** He had to think in Russian and that's the only way to, you know, this helmet super automated plane. Anyway. Yep. Gotta watch that again. Firefox.

**Chris Gammell:** Firefox. Classic.

**Dave Jones:** Yep. Anyway, that was, yeah. Yes, that was a very, that was very high-tech, like, very futuristic at the time to think, Of course. Right, right, right. You can control an aircraft with your thoughts, you know. That was, like, you know, really, yeah, really beyond its time. So, anyway.

**Chris Gammell:** Well, let's talk about more shit shutting down, huh?

**Dave Jones:** Oh, yeah. Why not? Yeah. Doom and gloom in the industry. Here we go. Come on. That's what we need.

**Chris Gammell:** Well, Intel killed all their stuff. Did you see that stuff? No. Again, this is old news.

**Dave Jones:** Oh, yes, yes. Intel killed all their Internet of Things dev boards. They realized Internet of Things was full of shit and they went, nah, we're just getting out of this business. This is embarrassing.

**Chris Gammell:** Right. So, Jewel, Galileo, Edison.

**Dave Jones:** I don't want to put, did you find out why they did? What's the reason? Because all I heard is that they shut down, yeah, the Intel, Edison, all their Internet of Things development boards. You know, they made a big splash a couple of years ago. We now no doubt talked about it and said, wow, Intel are getting into this Internet of Things and now they've gone, nope.

**Chris Gammell:** I'm guessing the answer is money. Money and lack of adoption. Right. Lack of adoption. Lack of adoption. Nobody could use the Galileo and the Edison. It's like these. All right. Here's my thing. I was thinking about this today. Intel has gotten in and out of the embedded business like five times. And I don't know if you would call this in the embedded business.

**Dave Jones:** Intel started in the embedded business. Sure. Right. But they also got out of it. A lot of people don't realize that.

**Chris Gammell:** They will get. And here's the thing. They're going to do this again. Yeah, of course they will. In a couple years. Five years down the track, they'll be back in. They're going to do it again, right? Especially with ARM doing as well as it has been doing.

**Dave Jones:** We'll be in our twilight years and we'll still be talking about them doing it.

**Chris Gammell:** But here's the thing. It's great. I knew this was going to happen as soon as I saw they had all this stuff out. They threw a lot of money at this. And to their credit, they tried. They supported.

**Dave Jones:** They did it really well. They did it. They made it Arduino. Windows compatible Arduino thing or something. It was like, really? They put a lot of effort into it. Sure.

**Chris Gammell:** Yeah. But this is going to happen again. And you're going to get taken again. Sorry to people who did it, right? And the thing is, they went after people that were software people that were looking to get into hardware. And so they could put Windows 10 on it. And that made a lot of sense, too.

**Dave Jones:** It was another bandwagon that they wanted to jump on. Because somebody at Intel wanted to justify their job. And, oh, let's jump on this bandwagon. And they got big pat on the back and a pay rise. And they're probably off to some other shit now. Right.

**Chris Gammell:** Well, I talked earlier about the margin of a chip company, right? And you get into these small things. Like, people making ARM chips are not making a ton of margin, right? Oh, no. That's what's crazy. It's a cutthroat business. And Intel is used to making a ton of margin. And this, again, I will give my prediction like I always do. This is the only prediction I consistently make. Intel is going to break off their server business. Sorry, their chip making business from everything else. Because I just think that if they ever want to do anything else from an IP basis, especially doing like taking on ARM, which they'll have to eventually do.

**Dave Jones:** The board of directors will eventually kill it because it's not making enough margin. Exactly. Compared to all the other business units. It's like you compare the old business to the new business.

**Chris Gammell:** You say, why aren't you like that? And it's like, well, I can't be like that because it's not the 90s.

**Dave Jones:** That happens in every business. Right. That happens in every big business. Because the board of directors, they look at all the business. You know, when you've got a company this big, you've got business units.

**Chris Gammell:** Dave's about to say fiduciary. He's going to say fiduciary.

**Dave Jones:** They do have fiduciary responsibility. That is correct.

**Chris Gammell:** Every time. Every freaking time. He loves saying it.

**Dave Jones:** Yeah. Because it's the way of the world. It's why companies, you know, run like they are. Because it's run for the shareholder benefit. It's not run for the public good. It's not run for feel good. If you want to run a feel good company, you don't go public. Right. You don't have shareholders.

**Chris Gammell:** Right. Right.

**Dave Jones:** Otherwise, it's a legal responsibility. I'll go through it again. No, please don't. Please don't.

**Chris Gammell:** Please don't. Anyway.

**Dave Jones:** Look at Google. It's fiduciary responsibility.

**Chris Gammell:** Right. Yes.

**Dave Jones:** And if you want to know why this shit happens.

**Chris Gammell:** We should also say that there's no news about the Curie. So we're just reading off Hackaday here. I thought it was all of them. No, Curie's still. No announcement on the demise of Curie.

**Dave Jones:** Anyway, they didn't just abandon it. They actually give you, it's been phased out by the end of the year and they do actually have a last buy. So they are doing it properly. They are phasing it. Oh, yeah. Last buys on these boards. You can buy 100,000 of these development boards. We'll make them for you. Just give us the order. You know.

**Chris Gammell:** Right.

**Dave Jones:** Yep. Wouldn't it be ironic if the last orders came in and actually made it viable?

**Chris Gammell:** That's how it usually goes, right? And then they go, oh, wait a second. Hmm.

**Dave Jones:** It wouldn't be the first time, yeah. A chip company's gone, last buys on this chip. Yeah. You know, we're shutting this down and then all of a sudden they get an order for 10 million chips. Right, right. And it's back in business. It's popular again. Right. And we'll keep that one in stock. Yeah.

**Chris Gammell:** Oh, dear. Well, sorry. Sorry to anyone who's developing on that. But, I mean, this is, I mean, I guess it's a good time to bring up. It's not just Intel, right? It's not like, oh, Intel shot this. Chip companies do this stuff all the time. And you should always be cognizant of it. And, you know, I always tell the people that I'm teaching on my course, I'm like, look, it's always going to be a guessing game.

**Dave Jones:** Chip companies are better than this. They're not as fickle as this. I mean, this almost comes into the fickle territory. You know, it's only been two years or something.

**Chris Gammell:** I don't really know. Is it only, Ben? Are you sure? I don't know. It feels like longer.

**Dave Jones:** I'm probably not too far off.

**Chris Gammell:** But anyway. Let's see what the old wiki has to say. Yeah. I think that, I don't know. You should always be careful with this stuff, right? Any line can shut down. And like I said, I always try and teach students that, like, you're going to do a best guess, right? You try and go for a popular part that might not be shut down. And you can, well, when we had Bunny on the first time, right? He always talked about, like, trying to design stuff in that was an iPhone 4 because that lowered the cost. But again, there's no guarantee that certain parts won't get replaced with other ones and whatever, right? There's always a chance of an obsolescence. So, you know, make your code portable. That's a good way to, as much as you can, right? Document your projects as much as you can. Yeah.

**Dave Jones:** But the problem is, like, the modern computing architectures like the Edisons and everything else, right? The Raspberry Pis and all the rest of them, right? They're so powerful that you're crazy not to use these in your product. Actually, in your product to, you know, if you've got a real power-hungry, like, you know, internet-connected product, like, it makes sense to use these boards. But the problem in your final, like, if you're, you might build a whole company around the fact that you're going to put a Raspberry Pi in something and you've got some neat application that runs on the Raspberry Pi, right? You can build a $10 million business making these things, right? But you're totally reliant upon the continued manufacturer of that board. And I, like, and if they're not completely open source, like the Raspberry Pi is not open source, for example, if they suddenly stop making it or abandon that version of the product and you can't port it over something, you know, you're forced to port it over or you're forced to go out of business.

**Chris Gammell:** Yeah.

**Dave Jones:** Because you can't get that board anymore. You've based your product around that module. It's no different to basing your product around some custom whiz-bang chip from Texas Instruments or somebody else, right?

**Chris Gammell:** Yeah. I'd say the only difference is that at least with a board, if you're doing it at a board level, you can maybe have a connector and that becomes your, you know, your interface. That's your abstraction is through the connector. That's probably one of the better things about, you know, things like an Arduino or, you know, even like a, you know, a Teensy is a different version.

**Dave Jones:** So you have a daughter board that's the same, so it doesn't matter whether there's a Raspberry Pi on there or there's an Arduino or there's something else.

**Chris Gammell:** You can always redesign it with some other chip in the future onto a board that plugs in, but then the trade-off there is...

**Dave Jones:** Is increased cost and complexity. Exactly.

**Chris Gammell:** Or size too, right? Or size as well. Of course.

**Dave Jones:** Yeah. You've got, you know, you've got these big pin headers or whatever.

**Chris Gammell:** Yeah. I mean, this is literally a decision that had me, that I made for the header that I talked about a couple, well, many episodes ago now. Just because it, you know, it future-proofs you a little bit. It's never going to be completely future-proof, but it, you know, by dumbing down the features a little bit and by, you know, reducing the number of features rather, and then putting it through some kind of simple interface, then you can at least rework it later. Right. But I can't tell you the number of projects that I, when I was working on obsolete products, it's like, yeah, your best case scenario is you put, you put some kind of landing pads around that chip you're trying to replace. You, and then as that, you know, especially like that's an intermediate step, right? So you have a chip and then you have the headers around the chip or the pin landings around the chip. And then eventually, you know, you, you make, you make two boards, right? You make two full products and then you put them side by side and the old product has the old chip and the new product has that plugged in board. And that's how you test that it does the exact same thing because that's all that really matters and keeping those things alive.

**Dave Jones:** You know, it's safe to do these things with some things like, for example, an ESP8266 module, right? Cause they're so ubiquitous every, like you can buy them from every man and his dog. Right. And that, you know, like that's something you don't really have to worry about. And of course you can duplicate the board yourself as long as you can still get the actual chip. Like the, you know, buying the module is nothing. Cause you can always relay out that module yourself and just buy the chip and get it sold and made. But is the, are the Intel boards open? I can't even remember if they're open source or are they open source enough that people could actually take the Intel Atom processor and actually make their own Intel Edison board? Like, is it, are they that?

**Chris Gammell:** Uh, you know, prototype with open source hardware and software. I'm just looking on here. Honestly, I have no idea.

**Dave Jones:** Right.

**Chris Gammell:** Um, open source is mentioned once. So. Oh, right. Okay. Yeah. Right. I mean like all these things are built for, so they have a standardized header, it looks like as well. So, I mean, in the worst case scenario, you buy what looks like a Samtech header and you do a replacement there.

**Dave Jones:** Yeah, yeah, yeah, exactly. And you put a new, and you put your own Intel Atom processor on there or whatever's in the Edison and, you know.

**Chris Gammell:** Yeah. Right. Right.

**Dave Jones:** Hmm.

**Chris Gammell:** Yep. The only constant, Dave, in our lives is change.

**Dave Jones:** Except for the triple five timer.

**Chris Gammell:** Except for the triple five. Oh, nice one. Yeah. Uh, well, it does change a little bit, it looks like.

**Dave Jones:** Apparently there's enough margin in the triple five timer, probably the most ubiquitous chip in the world, for fakes.

**Chris Gammell:** Right. Right. Yeah. So Zepto Bars is doing some, uh, one of our favorite capturers of. We love Zepto Bars website. Of die shots and everything. Yeah.

**Dave Jones:** They're the masters of the die shot.

**Chris Gammell:** Yes. And, uh, apparently, yeah, there are fakes, but man, how much, yeah, how much can they be making on this, right?

**Dave Jones:** I don't know. Well, that's the thing, right? Not only are they fake, but they, they, they actually brand them as TI. They're like, they brand them as genuine TI. It's like, wow.

**Chris Gammell:** Well, a bit of silk screen is pretty cheap, so that, that purchases it. Oh, yeah, yeah, yeah, it is.

**Dave Jones:** But like, like, why wouldn't, you know, if you're going to. Right, build your own brand. Build your own 555 brand, right? It's like, you know, there can't be that many people out there desperate. Oh, I must specify in the Texas Instruments 555, you know.

**Chris Gammell:** You know, and things like this make me think too, that like, I haven't been desperate. I have not made a low enough cost design to be this desperate, right? Because you know that the, the low cost things that we're seeing on eBay, right? That's, and that's where this came from is they were looking at eBay parts. That's actually coming from, you know, they're just getting put on the, on eBay from the markets probably, which means.

**Dave Jones:** Oh, and there's a thousand time markup on eBay price compared to what they're buying them for.

**Chris Gammell:** There's someone that's going between like, you know, three RMB and two RMB, right? But that is such a critical, you know, amount of currency for this one project that like, Right. That's, that's the thing. That's the thing you got to do, right? And it's like, damn, that's crazy. I mean, they're probably buying reels and whatever, but yeah. Yeah. Reels?

**Dave Jones:** None of that real rubbish. This is dip. Tubes, man.

**Chris Gammell:** Oh, tubes. You're right. Of course.

**Dave Jones:** Hey.

**Chris Gammell:** Why would you dip parts? Oh, man.

**Dave Jones:** But yes.

**Chris Gammell:** Yeah. You still love them, huh? Oh, it's cool. Still, still love the dip parts.

**Dave Jones:** Still love them. Yep. Even when they embed in my foot.

**Chris Gammell:** Yeah. Oh. Dip parts and Legos.

**Dave Jones:** Yeah, right. Oh, man. Speaking of Zepto bars.

**Chris Gammell:** Yeah, there was another one.

**Dave Jones:** They have finally torn down the Batteriser. Batteroo. Asic chip.

**Chris Gammell:** I haven't heard of this chip before. I don't really know what you're. No, no. They actually did. I've never heard you say this word Batteriser before.

**Dave Jones:** Oh, right. Yeah, probably not. It turns out they did actually, they weren't lying. They did actually make their own custom chip. Well, no. I read this, though, too.

**Chris Gammell:** I thought they were doing. What? There is a custom chip. It doesn't mean they made it, though.

**Dave Jones:** Oh, no, no, no. Right? They could have just contracted one. I'm not sure who actually designed it. They probably contracted out one of the. Well, they. You'd be crazy if you didn't go to one of the. They actually have contacts. In fact, I traced down that the CEO of Batteriser used to work with somebody who's now the head of the DC to DC boost converter at some company. I forget their name. I posted on the forum. Oh, wow. Okay. Yeah. So they probably used their contacts there to get them to design this custom variant of probably an existing part they had. It's probably, you know, I don't know. But anyway, it's actually pretty cool chip. It has very limited use.

**Chris Gammell:** Dave Jones just said something nice about Batteriser. Look at that.

**Dave Jones:** No, I've said it quite a few times on the forum. There's nothing new about this.

**Chris Gammell:** Gotcha.

**Dave Jones:** And everyone's saying the same thing. It's actually a nice solution for what it is. It's actually a really. It's probably the world's best chip at what it does. Right. It's the lowest quiescent current, et cetera, you know, blah, blah, blah. But it's limited in its use. It's, you know, their application is still complete and utter impractical. And it's basically a boost converter. That's the idea, right?

**Chris Gammell:** It was like a two-stage boost converter or something like that.

**Dave Jones:** It's a synchronous two-phase boost. Yeah. Yeah. Not stage phase.

**Chris Gammell:** Right.

**Dave Jones:** So, yeah. Okay. Anyway, yeah. And they've got like a data sheet for it now. And apparently, I don't know if you talk to them, you could buy it if you needed a single-cell boost converter.

**Chris Gammell:** You might be able to buy it on the market on eBay for cheaper at some point.

**Dave Jones:** Yeah, right. Yeah, someone will rip this off. Because there's such a need for a single-cell boost converter. Right. It would have. And a lot of people on the forum are talking about, why didn't they just design it to make it a bit more universal? A tiny bit more universal voltage range. And it would have been more useful.

**Chris Gammell:** Oh, like a commercial product at that point, right? Yeah. Yeah.

**Dave Jones:** But they were so tied in with their, you know, they were so obsessed with their ridiculous false idea that, you know, everyone needed that this batterizer thing was going to save the world. You know, they were so obsessed with that. That was, that they didn't make the design universal enough to be, to make it a, you know, otherwise it'd be a reasonably, it could be a reasonably successful chip. So anyway, yeah, there's a die shot. Yeah. Oh, we've got other ones too. Prove that it is custom.

**Chris Gammell:** There's another one. There was the, Zepto Bars has been busy and or we haven't checked very often apparently.

**Dave Jones:** Right, yeah.

**Chris Gammell:** The Power NPN BJT, did you see that one? No. So I've been posting all these as I, as I see them pop up on Twitter basically, you know. Right. But this one is actually really, it's gorgeous design. It's really just the metal layer shown.

**Speaker ?:** Oh, yeah, yeah.

**Dave Jones:** I've seen it. Oh, yeah, yes. I did see that. Yeah. Yeah. Yeah, yeah. It's, I just love the symmetrical layer. I mean, it looks like, it looks like art.

**Chris Gammell:** It really does.

**Speaker ?:** Like.

**Dave Jones:** Oh, yeah.

**Chris Gammell:** It's beautiful. And this is just metal layer though.

**Dave Jones:** Oh, no, but there'd be a technical reason why. Can, can that photo of that die, that Power BJT die be the photo for this episode or whatever?

**Chris Gammell:** Because that's really cool. Well, we don't have the license for it, but maybe.

**Dave Jones:** Oh, they won't mind. Zepto bars are cool. They won't mind us.

**Chris Gammell:** We'll send them some traffic. It'll be great.

**Dave Jones:** We'll send them traffic. Reciprocal links, you know. Oh, yeah.

**Chris Gammell:** Yeah, that's how the internet works, man. Yep. I send you traffic. You send me traffic. We're all friends now. Yeah.

**Dave Jones:** And, but there's probably a technical reason why that symmetry and that layout works, you know. Yeah. Like in, in terms of like, cause we're with BJTs on silicon. I'm probably starting to talk out my ass here. In fact, I guarantee I am. Right, right, right. Yeah. Now we're in. That's when it started. Yeah. It's, it's like, you know, surface area and, and efficiency of surface area and all sorts of symmetry in surface area. And, you know, which. Honestly, I still have trouble looking at this stuff. Because I was actually reading the other day. I, I, I went down a rabbit hole here the other day and, and found that the thermal transfer rate across a die is, if memory serves me correctly, from the other night, I was reading this late at night, is one micrometer per microsecond. That is how fast a, when, when you heat up, I can find the reference for it.

**Chris Gammell:** So if you have like a point source of heat, you're saying.

**Dave Jones:** When you, like, if there's an individual transistor that you're overloading on a die or is heating up on a die, right. How fast does that heat spread across the die? Right. And it turns out it's like one micrometer per microsecond or something.

**Chris Gammell:** And that's regardless of like heat sinking or anything else you're saying?

**Dave Jones:** Yeah, no, no, that, that makes no difference. Like it's, you know, well, because it's got a, the heat's got to spread across the die in order to get out of the package, in order to get to the thermal pad in order, like to get out. Right. So it's all to do with.

**Chris Gammell:** Any idea if that was at the, at the silicon layer, if that was like a higher up in the substrate?

**Dave Jones:** No, no, no, no, no, no. This is silicon layer. This is how it spreads across the silicon. Ah, interesting. Okay. So if you heat up an individual, like it was to do with overloading an individual output transistor. Right. Because then it would. You know, like a totem pole output. Right.

**Chris Gammell:** If the heat, if the heat starts to spread, because there's really the heat would start to spread and then it would, the ions would start to migrate because of the heat starting to release some of their bonds and stuff like that. Right. Right. And that's really.

**Dave Jones:** All that physics stuff. Right. Yada, yada, yada.

**Chris Gammell:** Ion implantation. Pretend Chris remembers anything from a silicon dish.

**Dave Jones:** Right. Yeah, right. And I thought that was fascinating. I never actually.

**Chris Gammell:** That really is. Yeah.

**Dave Jones:** I had never heard that figure stated before for the heat transfer rate across the surface of an encapsulated die.

**Chris Gammell:** Dude, that would be a good video. I'm saying if you could find more about that. I know. I know. That would be good.

**Dave Jones:** Like to get a thought. I do actually have that new thermal, FLIR thermal camera, but A, it wouldn't be fast enough. Right. And B, it wouldn't be lower resolution enough.

**Chris Gammell:** As I was going to say, it doesn't work through a microscope, does it?

**Dave Jones:** Well, no. And no, exactly. I would have to have specific thermal, germanium macro lenses.

**Chris Gammell:** Or a lot of tiny, tiny, tiny thermocouples.

**Dave Jones:** Google it. Google it. Can you buy a germanium thermal macro lens?

**Chris Gammell:** Here we go. Because you're saying it would pass through?

**Dave Jones:** Live Googling. Live Googling.

**Chris Gammell:** You're saying that because it would pass through, the IR would pass through?

**Dave Jones:** Yes. Yeah. They make these lenses. Lenses in thermal cameras are made out of germanium, typically. Because it passes thermal.

**Chris Gammell:** $40 lens gives your FLIR higher clarity, according to Hackaday.

**Dave Jones:** What?

**Chris Gammell:** A $40 lens gives your FLIR higher clarity. For the E4 thermal camera, they put some lens on it.

**Dave Jones:** Oh, I've got one. Show you. Send me the link. I've got the E8.

**Chris Gammell:** Okay. Well, there you go. Maybe that'll help. Look at that. Live Googling works. Yeah. No, that's interesting. So you're just saying that it helps to actually focus the IR or what?

**Dave Jones:** Well, yeah. Thermal cameras are no different to regular cameras. You've got to have a lens system on there that focuses a wide field view onto your particular die surface area. It's got to be the focal length. The optics are all the same. Except it's passing heat. Right. It's just a different wavelength. Right. It's a different wavelength. Yeah. So they've got to make them out of germanium or some other material that can pass thermal.

**Chris Gammell:** Interesting.

**Dave Jones:** Right? So, yeah. Yeah.

**Chris Gammell:** Well, that's cool. Hmm. Well, I hope to see that soon. Cool. One last die-based item from our list. Electron Update. We did a teardown look at the 6502 CMOS version, which I didn't realize was a different thing. I mean, you know, my silicon history is pretty lame. Yeah. You suck at it. Yeah. Just don't bother. So, anyways, a, you know.

**Dave Jones:** Anyway, we've had Chuck Peddle on the show.

**Chris Gammell:** Right. We should, yes. We should refer people back to that. That was a great episode. That was great.

**Dave Jones:** And this is a great video. We'll link this one in. Yeah. Yeah. And it's just basically a teardown and explanation of the 6502 die.

**Chris Gammell:** Right. I'm amazed people are still doing this stuff. The 65CO2. Right. Right. They're still building stuff. Like, people are, there's still like a huge community around that, the whole vintage thing. You know? They love it. Simple instruction set, I suppose. And peeking and poking.

**Dave Jones:** Because the CMOS die would be totally, the 65CO2, entirely different die, entirely different technology to the, presumably bipolar 6502.

**Chris Gammell:** I guess it would have been. Yeah. I don't even know. Whatever. You know. Yeah. Right. But as, we didn't talk to Chuck about that. It probably was, right?

**Dave Jones:** Right. I, yeah, I don't remember.

**Chris Gammell:** No, it wouldn't have been BJT. It's, well, maybe.

**Dave Jones:** Well, what, you know, it's, it's not a CMOS. It was, whatever the opposite to the CMOS process. Instead of. Moss or whatever. Yeah. Or, I, I, no, no, no, no, no, no. It's. Yeah. No, no, no, no, no. It's gotta be like a.

**Chris Gammell:** Now we're talking to her ass.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. I'm looking it up again.

**Dave Jones:** I'm, I'm looking it up again. Furiously.

**Chris Gammell:** Look, we're at 351 episodes, folks. Give us a break. Give us a goddamn break. Also, we don't really know what we're talking about. Yeah. Yeah, this is actually confusing.

**Dave Jones:** This CMOS version was done by the Western, Western Design Center. Was done by a different group. So. Anyway.

**Chris Gammell:** I'm going to throw myself on the altar of, of embarrassment here. I actually, I don't get it. I don't. What. You don't get what. What's the difference?

**Dave Jones:** What, what between a CMOS processor and a, and a regular processor at the time. Back in the day, dude. This is really important. All of the notebooks back in the day. Right. Using the CMOS version of the 6502 would allow you not only to get a lower power CPU for a given clock speed. So important in battery powered, like the early notebooks. Oh. They weren't called notebooks. Well, whatever they were.

**Chris Gammell:** Okay.

**Dave Jones:** You know. Like the Tandy Radio Shack. Right. The Trash 100, for example. Right. Okay. Sorry for those TRS fanboys. I'm using the trash term trash for TRS. Oops. Okay. So I, I found, I found what I was looking for here. Anyway. So there. Yeah. So what they, not only do they give you slower rate, but you can actually slow them down to an arbitrarily slow clock speed. Right. So if you're just a lot of the old computers that were battery powered would dynamically slow down to like, you know, 10 kilohertz or something. If you're just waiting for key presses. Right. And then once it's doing processing, it'll start up again at, at the four megahertz rate or whatever the processor would, two megahertz or whatever the processor was capable of. Right. Because you wouldn't want to always run at two megahertz. If you're just sitting there waiting for it, scanning for a key press, for example. Okay. And also, so not only could you arbitrarily slow them down to an arbitrarily slow clock speed, like one hertz, you could slow them down to zero hertz and put the processor in, like freeze. You just stop the clock and it just stays there. It stays in that state. And that was a big thing. So all of the, you know, a lot of the early computers, you would, when you shut them down, they'd simply freeze the processor. Everything's still in memory. The processor still has all its registers. And when you turn it back on, boom, the processor just starts up again instantly where it's left off. It's no, it's no loading an image back off a drive or something.

**Chris Gammell:** Right.

**Dave Jones:** You know, that modern bloody computers do.

**Chris Gammell:** Yeah.

**Dave Jones:** It was, yeah, it was a big deal.

**Chris Gammell:** Okay. So, but the thing that I was confused about is like CMOS versus what? That's, that's really what I was confused about. Okay. And then, and I remember, yeah, that's what Chuck was talking about. Remember he talked about, this is a while ago now, but he was talking about, remember they only had one type of transistor? And so that was, that was NMOS. So depletion load NMOS. That's what they were using on the 6502. C is complimentary, right? So you have N channel and P channel.

**Dave Jones:** That's right. Okay.

**Chris Gammell:** And then the other one is HMOS, I'm reading. That was later. That's what they use for high density short channel MOS, HMOS. That's what Intel started with.

**Dave Jones:** Yeah, I don't remember that being hugely popular, was it?

**Chris Gammell:** Or am I wrong? HMOS, oof. Again, we're looking all this stuff up live. Anyway, yes. I feel like we shouldn't be embarrassed about this stuff at a certain point. I know. Who's going to remember all this stuff? But anyways, HMOS was later and then by CMOS, that was in the later on after that. There's just a lot of different MOS types.

**Dave Jones:** And now they've got 20 million different variants of processes. Right. I mean, yeah.

**Chris Gammell:** What's the BCD? What's that one? Bipolar, CMOS, DMOS, or something like that? I don't remember. I remember BCD process, but that's like a combined process.

**Dave Jones:** We were talking about that Intel 5 nanometer thing, weren't we? Or the, sorry, the IBM 5 nanometer thing the other week. Right, we were. And it would use some whiz-bang new bloody process.

**Chris Gammell:** Well, that was not the, so like the CMOS versus the NMOS, as far as I can tell, though, is the, it's actually how you're building each gate, right? So in the NMOS, you're building with three gate, three transistors, but there's not different doping like you need with CMOS, right? So you have an N channel, P channel, you actually turn them on. You know, that's like the, what'd you call it? Totem pole, right? So that's like the thing you were talking about. And then that's like CMOS, right? Where you basically turn it on and off like an inverter, right? And then NMOS, though, I'm not sure how that worked, but that was what the 6502 was originally. So that's.

**Dave Jones:** Right, well, a CMOS inverter is simply two gates. Right. And you just, two MOSFETs and you tie the input gates together and tie the outputs together. And that's like in a totem pole configuration. It literally is just two, one, one totem pole and you feed the signal into the two gates.

**Chris Gammell:** But isn't one an N and one is a P, right?

**Dave Jones:** Yeah. And it's. Yeah. And then when you tie the gates together, when you input a higher load or a gate, it turns one transistor on or the other, you know, it literally is that easy.

**Chris Gammell:** Yeah. So. Yes. That sounds right. And if not, I'm sure our people forget. We have a comment section, so you can come and tell us how stupid we are. Yeah, tell us that we're wrong because we always are. Like usual. Yep. There was one other thing I wanted to mention because there was another thing about on our list about process stuff.

**Dave Jones:** Oh, yes. And NMOS, sorry. Yes. An NMOS inverter uses, it doesn't use a totem pole arrangement. It uses a pull up, effectively a pull up resistor.

**Chris Gammell:** Oh, interesting. Okay.

**Dave Jones:** Yes. So it might use another transistor as a resistor, right?

**Chris Gammell:** Uh-huh.

**Dave Jones:** I don't know the physical implementation of the resistor on the die, but that's the difference. It's the NMOS, so an NMOS inverter is like using a single transistor with a pull up resistor.

**Chris Gammell:** Oh, interesting. Okay. That's the difference. And so that's going to be a higher power burn, that kind of thing, right?

**Dave Jones:** And higher power burn and all that sort of thing. Right.

**Chris Gammell:** And slower because of capacitance built in, you get an RC effect, that kind of thing, right?

**Dave Jones:** Exactly. And so that's why CMOS is, yeah. Right. CMOS killed it overnight.

**Chris Gammell:** We don't even need to freaking think about this stuff anymore, you know? It's like.

**Dave Jones:** Yeah, I know. It's just like.

**Chris Gammell:** It's just like, oh, okay. Well, I guess that it's just digital work, whatever. Yeah. Anyway. Yeah. So there was a thing about, I saw seven nanometers on our list here somewhere. Seven nanometers. Can't find it. Of course. Oh, here we go. Global foundries. So yeah. Oh yeah. Global foundries, who is what, basically global foundries is what AMD did, which I think Intel will eventually do. They split out the fab, right? From AMD. Right. Right. So basically they're already preparing for seven nanometers. So we talked about the IBM five nanometer before. Global is just going straight for it for production. So that's crazy.

**Speaker ?:** Yeah.

**Dave Jones:** It's getting to a point where I simply will not trust these chips. You know? Like, surely. I mean, come on, man.

**Chris Gammell:** We can't see them now. We're not going to be able to see them then. It doesn't matter.

**Dave Jones:** I don't know. It's. Oh.

**Chris Gammell:** Just hope they test it. Gives me the heebie-jeebies. Yeah. Well, you can always go back and, you know, you can go back to basics, Dave. Right. With this. To my Amish. No, with this lovely kit from SparkFun. I don't know if you saw this one. They started selling it again. I mean, I don't know if it ever stopped being sold, but I didn't see them for a while. SparkFun's selling the 130 in one kits. Oh, right.

**Dave Jones:** Nice. Oh, made by Elenco. Right. Yep.

**Chris Gammell:** I didn't. So those have been made for. I didn't know they were still making them.

**Dave Jones:** Oh, yeah. No, no. They've been still making them. I don't think they've ever stopped. There's always been a company that's made them.

**Chris Gammell:** Yeah. Okay. I thought they could discontinue.

**Dave Jones:** Like, you know, Radio Shack slash Tandy stopped making them, but other companies picked them up. Other companies just copied the form factor.

**Chris Gammell:** Yeah, just springs and cardboard, basically.

**Dave Jones:** Yeah, springs and cardboard and chips put on the. I love it.

**Chris Gammell:** I love that they're selling this. It's like 50 bucks, too. Like, that's a great thing for, like, you know, buying for an Eastern FU and, you know, just. Yeah. Yeah.

**Dave Jones:** I'll be doing that. I'll be dragging out my 30-year-old one and actually play it with Sagan and we'll build it up. And we'll build up a. That'd be fun. Yeah, a circuit on there. Right. Totally.

**Chris Gammell:** That's how a lot of people got started. So, you can still buy them. That's great.

**Dave Jones:** Yep. And what are the chips on there now? It's got to be, like, the same. Like, there's a couple of treadies on there. There's a bunch of green caps by the looks of it. There's some, you know. And there's a couple of, like, NAND gates.

**Chris Gammell:** Yeah, it says integrated circuits NAND gates.

**Dave Jones:** And the old AM antenna rod. Oh, yeah. Because the value in these is the, not so much the physical platform as such, but the manual. Like, you know, the circuits and the manual and the schematics and the information that goes along with it.

**Chris Gammell:** Not really the fact that you just can wire stuff together. I mean, like, it's like, there's no soldering required. Even, like, even bending leads isn't required. Yeah. And it's pretty much just point to point. Yeah. This plugs into here. This plugs into there. And you're off to the races. This is a dopamine generator. That's what you want. That is the best part for getting started in electronics, is a dopamine generator. Cool.

**Dave Jones:** Well, that's our show, isn't it?

**Chris Gammell:** Oh, by far.

**Dave Jones:** We're Dunski.

**Chris Gammell:** Yeah. Anyone else wants to, they can go and see our subreddits, which has many more links and continues to throughout the weeks. Oh, I had a chip for the week. I don't know if that was...

**Dave Jones:** We already had a chip for the week. You had a chip for the week. Yeah, I had a chip for the week.

**Chris Gammell:** You didn't have the part number for it, though, did you? You said the TI 80 gigahertz something something?

**Dave Jones:** Yeah, something rather. I've got it right in front of me. They can't see it because it's so bloody small.

**Chris Gammell:** Yeah, right. Exactly.

**Dave Jones:** Need a microscope and the light at the right angle to, you know.

**Chris Gammell:** Well, I was going to recommend the CSR 8645, which is a crazy... So, it's Qualcomm, but it's a... You just look at what's in this thing, you're like, what the hell? And it's like a dollar. But basically, this is like the design that's in like every... You know when you get your email for... You want Bluetooth speaker? What I didn't realize is that Bluetooth speaker is actually reference design speaker. Ah, right. So, this is what's in a lot of them. And basically, it acts as a... It can act as the speaker or it can act as the headset. And that's what's crazy. So, it's got a microphone. It's got a DAC. So, it's got an ADC, a DAC. It's got a DSP on board. It's got battery charging and tons and tons and tons of stuff.

**Dave Jones:** And it's got the Bluetooth interface, does it? Or is that a separate chip?

**Chris Gammell:** Yeah, yeah. It's a 4.1 Bluetooth. So, like... Right. Yeah. So, it's all in this one thing, right? This kind of reminds me of...

**Dave Jones:** It's a complete custom ASIC solution for a product. It's specifically tailored for Bluetooth headsets. Right, exactly.

**Chris Gammell:** This is a Bluetooth headset thing that... Yeah, you... It's awesome.

**Dave Jones:** And it's probably even got battery charging circuitry and all sorts of crap in. Right? Oh, yeah. Yeah.

**Chris Gammell:** Right. Yeah. And this kind of reminded me of what... Single chip. We talked to... I don't remember if you were on the show with us. With Juergen. Yeah. Who did this for the audio stuff for...

**Dave Jones:** I think I was. I do remember that.

**Chris Gammell:** Yeah. For hearing aids. Yeah, yeah. You were. Yeah. No, you weren't.

**Dave Jones:** Were not? Anyway, I do remember it.

**Chris Gammell:** Yeah. So, anyways. Yes. Anyway, very cool. Yeah. That kind of stuff where it's just like these super, super integrated things. So, we go from 130 in one kits to completely integrated single chip solutions.

**Dave Jones:** Yeah.

**Chris Gammell:** That's probably in some pain in the ass flip chip. Oh, yeah. Bloody bullshit package, you know. You will not have a good time soldering this. Yeah. Where is it? Package. 5.5 by 5.5 millimeter, 0.5 millimeter pitch.

**Dave Jones:** Oh, massive pin pitch at 0.5 millimeter.

**Chris Gammell:** Oh, yeah. Right. You get more than 0.4. Oh, yeah.

**Dave Jones:** No, it's 0.4 rubbish.

**Chris Gammell:** Right, right. 0.8. What's that for? Giants?

**Dave Jones:** Oh, dear.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway.

**Chris Gammell:** All right, man. That's it. We'll talk to you next week. Catch you next time. Catch you next week.
