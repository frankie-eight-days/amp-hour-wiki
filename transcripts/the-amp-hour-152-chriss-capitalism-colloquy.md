---
episode: 152
title: Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy
url: https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/
---

**Chris Gammell:** This episode of the Amp Hour is brought to you by NetBurner. Have you ever bought an embedded development kit that took a day or weeks to get to Hello World? Are there endless libraries requiring build after build? And do you find yourself banging on your desk, waiting for your application to compile and download, when all you want to do is test your code and get it out the door? NetBurner provides the easiest way to develop and deploy network-connected embedded devices. With a complete solution of hardware, software, and development tools, your prototype will be up and running in no time. For more info and a special listener offer, go to netburner.com slash theamphour.

**SPEAKER_01:** This is the Amp Hour Podcast. Recorded July 1st, 2013. Episode 152. Chris's Capitalism. Coloquy.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Hello, David. Welcome back to another episode of the Amp Hour Electronics Podcast.

**Dave Jones:** Thank you very much for having me.

**Chris Gammell:** It's always a pleasure. Right.

**Dave Jones:** Yeah. Come on. Admit it. You're sick of me. After what? Well, only had 152 episodes. Two and a half, three years. Yeah, 152 episodes. Three.

**Chris Gammell:** Three years. Three years in August. Yep. Yeah. Yeah. We're just sick of each other. Three years. Yep. Yep. Yeah. The magic is gone, folks. We'll just sell it and start afresh. We should. Yeah. We could probably get...

**Dave Jones:** We'll just sell it and part our ways. Yeah.

**Chris Gammell:** Yeah. Yeah. Just like Hackaday.

**Dave Jones:** Hackaday just announced that they're...

**Dave Jones:** News. Hang on. It's coming through the Amp Hour teletype. Sorry.

**Chris Gammell:** It still makes me laugh, but for all the wrong reasons.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Yeah. So...

**Dave Jones:** News of the day is, yes.

**Chris Gammell:** Yeah. Well, we just saw this. This just popped up, but, you know, Hackaday, obviously, a lot of people read that. Even, you know, people not necessarily just interested in electronics. Hmm. And, yeah, they're looking...

**Dave Jones:** It's a very popular place to... If you've done, like, a, you know, like a project, you know, if you've hacked a project or something, it's, you know, if you get listed on there, it's good because you get a lot of traffic.

**Chris Gammell:** Yeah. Yeah. Yeah. Same, I mean, same for us when we've been listed on there, you know, we've had lots of visitors. Maybe some of our listeners now even found us through that, so...

**Dave Jones:** What do you call a website like that? It's like a... Sort of like a news gathering kind of...

**Chris Gammell:** Yeah, like an aggregator.

**Dave Jones:** An aggregator. That's the technical word I was looking for. There you go.

**Chris Gammell:** Yeah. And it's, I mean, it's kind of a community, too, except I don't know if they...

**Dave Jones:** It's a community in the way YouTube is a community. You know, you have people who just love to leave comments, you know, that's... Yeah. Sort of just watch it, you know, all day long and leave good and bad comments.

**Chris Gammell:** Yeah. It's been through its ups and downs of nice and not so nice comments. So, yeah. But it was started by Phil, who's now at Adafruit. So, it's cool. Hey, Phil. If he's listening.

**Dave Jones:** I'm sure he's too busy to listen.

**Chris Gammell:** Probably. Those guys are busy. So, yeah. It's interesting, though, because Jason Kalkanis, the guy that owns the site, is actually, like, you know, gives figures and everything about, you know, how many people look at the site every day, which you don't always see about sites. And how much they earn.

**Dave Jones:** Yeah. Which is interesting. Yeah.

**Chris Gammell:** Yeah. It's all there. It's all pretty open. Yeah. And they're looking for a new editor if they do get bought. Because Caleb, the current editor, who's done some cool videos and stuff, he's leaving too.

**Dave Jones:** So, yeah. They're going to do another website startup-y thingy. Yeah.

**Chris Gammell:** My Bob. Yeah. Yeah. Thingy-my-bob.

**Dave Jones:** Yeah.

**Chris Gammell:** I don't know.

**Dave Jones:** So, they don't have time to run it anymore. So, yeah.

**Chris Gammell:** Right. Yeah. You'd think with all the people in the world, there'd be, you know, there's probably a couple out there that want to be working on this kind of thing. So, if people are interested.

**Dave Jones:** That's the thing. I mean, this is the kind of, this aggregator thing is the kind of stuff you can, you know, hire someone to do. Versus a gaggle. Versus, say, me, for example. You keep telling me to, oh, go hire someone to edit your videos and do that sort of jazz for you. Oh, right. You know, it's not quite the same. You know, this is something that doesn't really, I mean, you don't know the person who owns the site, really.

**Chris Gammell:** I get you. Right, right. It's not personality-based.

**Dave Jones:** It's not personality-based. It's just pure information-based, really.

**Chris Gammell:** Right, right, right. Yeah, a lot of administrative stuff. Yep. Yeah, that's a lot of publishing these days, really. Publishing is weird. It's really weird. And I doubt our audience really cares about it, so. Nothing. Well, they may not give a toss about Hackaday either. Yeah, yeah. Yeah, so what else is new? MakerBot's broken, I saw.

**Dave Jones:** My MakerBot? Oh, yeah, yeah. It's been broken for a long time. Bloody thing. Yeah. Yeah. Yeah. Yeah. These tools just don't work. I've said it before, and I'll say it again. They're just not ready for mainstream consumer consumption.

**Chris Gammell:** Yeah. Well, you do have an older one, but.

**Dave Jones:** Yeah, which actually does work a bit better, you know.

**Chris Gammell:** Right, right.

**Dave Jones:** Go figure, you know. But no, the firmware update procedure is retarded in it, and I bricked it. I bricked my MakerBot, so, you know, it's just sitting there and just goes, duh, and just turns on the, you know, the LCD just pops up with the black squares of death, you know. Yeah. So.

**Chris Gammell:** Oh, that's why. That's right. I saw you were trying to get, like, AVR dude, right, to flash me firmware.

**Dave Jones:** Now, can I have a little impromptu rant? What?

**Chris Gammell:** A whinge?

**Dave Jones:** Yes. God, I hate.

**Chris Gammell:** I saw your thing about that with the EXEs and everything.

**Dave Jones:** Like, why can't these tools just work, right? I, you know, because normally I use AVR, Atmel AVR Studio, right? Yeah. And, of course, my machine wasn't set up for that, so I dragged out my Odin notebook. I had it installed, and I hooked it up to my AVR Studio dongle, which has its own issues with bloody installing that thing. Oh, the Jungo driver, serial driver needs to be installed before this other driver needs to be installed, and they conflict, blah, blah, blah. Bloody hell. And, anyway, so I got talking to my chip, you know, AVR Studio talking to the chip, and then I go, right, I can download. I finally found the firmware image file. I think I've got the correct one. It's not obvious from the MakerBot website. Well, no, sorry, from the GitHub repository. And I try to install it. No, wah. No, hex file not compatible with AVR Studio. Oh, far out.

**Chris Gammell:** Oh.

**Dave Jones:** Oh. So everyone craps on it. Well, MakerBot suggests using AVR Dude, and everyone craps on about AVR Dude. I've never used it. So I'll go to the AVR Dude website. Okay, there's a website there. And there's a download page. Great, I'll go to the download page. Great, they're all out of order, but I can figure it out. I can read dates. Okay, here's the latest version. I download and install it. Well, unzip it. And there's no XE in there. It's the bloody source code. Oh, yeah? Do they tell you that anywhere on there? You know, it'd help. Like, there's not much on the main webpage for AVR Dude. It's like, here's AVR Dude. Here's the download page. And a few other things. And you'd think they would tell you, you cannot download the XE from this site. If you want the executable, go somewhere else. And it's like, oh, far out. Give me a break. Why can't these tools just work?

**Chris Gammell:** It's just crap. It's this kind of thing where it could be, you know, it could be PebCAC, right? It could be that you're not doing it quite right.

**Dave Jones:** It could be. Well, no, but apparently that is correct. There's no executable on the website or in the download.

**Chris Gammell:** Right, right.

**Dave Jones:** And it does tell you that somewhere if you go deep down in the manual and read it.

**Chris Gammell:** Yeah, exactly. I mean, that happens in a lot of tools. You know, it's just a matter of your target audience. You know, they figure that if people really want to program something, they're going to go figure it out. And so, it's like that with a lot of different kits and, you know, programmers and stuff. That kind of stuff just gets kicked down the road because it's like, well, we could fix this, but maybe 95% of our audience or our customers get it to work and they know the flow. And it's like, whatever. You know, and it's the same thing with it. And the funny thing about it then is that some customers will then, they'll fight tooth and nail to keep the flow the same because they already know it, right? Or they've written scripts to deal with that kind of stuff. And that's when it gets really funny because you see people fighting for this stuff. You know, they say, no, no, no, you can't change anything. It's like, well, I want to make it better. No.

**Dave Jones:** Yeah, I don't understand these open source tools, right, that insist on not having an official executable. And, yeah, I know there's a whole philosophy thing behind it and, you know, all that sort of crap. And, oh, you know, no, the source code is, you know, the holy grail and all that sort of stuff. The problem is, right, if there's no official or de facto standard, at least, executable, then how do you support this shit, right? I mean, people, you know, you leave it up to the community and forums and stuff to, you know, to support all this. Well, somebody says, oh, my AVR dude doesn't work. Well, what version of the executable are you running? Well, I don't know. I compiled it myself. Well, there you go. You know, I mean, how do you know? Yeah, like there's no standard baseline, right?

**Chris Gammell:** It opens you up to a ton of variability. That's definitely true. Exactly. But I think, again, it's the same thing of, you know, well, first off, it's a, I don't know if it's open source, but it's, you know, it's a community project. So that always hurts too, right, when there's no centralized body to yell at. Yeah, yeah.

**Dave Jones:** But somebody wrote this thing. You think they would at least put on the website, well, here, look, I don't create the exhibit. Here's someone that has, and look, everyone used this as a baseline, you know? Yeah. And, like, there's a lot of people that said, oh, there's a copy of AVR dude executable in the Arduino tools or something. So, you know, well, bloody hell. Yeah. It just bugs me. It really does. Right. You know, because especially in tools, like, that you just want to work, right? It's a tool. You know, you just want to install it, run it, and program your chip.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? You know, that's it. You don't want to be dicking around.

**Chris Gammell:** No, I agree. I agree.

**Dave Jones:** I've done a rant on this before about, you know, the Picatmel AVR, you know, the tools, you know, microcontroller development tools. If you buy one of these third-party programmers, right, I'm a big fan of choosing the official programmer, right? Because at least you've got baseline hardware and baseline software to work with, right? So when you go and get support, it's like, you know, there's more chance of it working. You know, if it's the official manufacturer's tools rather than some AVR dude programmer that somebody somewhere in their basement wrote. But, you know, I mean, yeah. I think there might be a difference in mindset, though, too.

**Chris Gammell:** I think that's, you know, a programmer's mindset, right, is to do continuous builds, to have source code in a repository somewhere, right? And then to do updates like that versus a hardware person, right? You and I are used to, all right, Rev1 is this board. Rev2 is this board. It's like there is no…

**Dave Jones:** And you set a baseline each time.

**Chris Gammell:** Yeah, there's no 1.5, or if it is 1.5, you can look at it and tell because you've got 30-gauge wire and jumper all over the place and little cuts to your traces, right? Yeah, that's a big deal. You know, that is a difference in mindset. And I think as people move into, like, from software to hardware, they have to deal with that, too, because it's tough to know when… Not only, like, changing your mindset, but if you are moving into the hardware world from a software background, like, knowing when to pull the trigger, right? Because you can't just incrementally change stuff. You're right. You do need a baseline. You need to know that I have this BOM, I have this, you know, this layout, and this is RevA, right? There's nothing else to it. Maybe you can change parts and stuff for the BOM, but, yeah, that's a tough thing to deal with when you're trying to bridge that gap between software and hardware.

**Dave Jones:** And I think for development tools like this that beginners are potentially using, right, I think it's just completely wrong. I mean, I see it all the time, right? Beginners ask a question. Oh, you know, how do I… You know, I'm starting out with AVR chips. How do I program it? Oh, go and use AVR, dude. Right? Yeah. And it's like, well, bullshit. I think that's the worst possible advice. You can give someone…

**Chris Gammell:** Well, I think a lot of people are basing that on the Arduino system, though. I mean, that's the thing. Like, you see it compiling each time in Arduino, right? It says AVR, dude.

**Dave Jones:** Yeah, but you don't know it's using AVR, dude. Do you? Sure do.

**Chris Gammell:** It's been a long time.

**Dave Jones:** Yeah, no, no.

**Chris Gammell:** If you use the verbose output, it shows all the… Oh, right, the verbose, right, yeah. Yeah, it's just part of the… And that's another thing, right? That's a… AVR, dude's fine. It works well. Right? But it's part of a flow, and people don't want to change that then, right? So, you know, it's just an exposure thing of if you're exposed to it and you get used to that flow, then you're going to want to keep it the same, and you're going to suggest it to others. Because then you can support them.

**Dave Jones:** Yeah, but the Arduino is a bit different because they do set a baseline, right? They go, here's version… You know, you download version X of the Arduino tools from their website. That's true. And it includes one… You know, it includes the build of AVR, dude, that they've done, right? It's not like you've got to go and install AVR, dude, separately. It's already handled, you know, and baselined for you. Right. So, you know, that's… Yeah.

**Chris Gammell:** Yeah, I think sometimes you do get that. I mean, you do get that choice sometimes, right? I think about it like KiCad, right? So, KiCad, you can actually get, like, nightly builds of KiCad so that you're…

**Dave Jones:** Right, yeah, yeah, yeah.

**Chris Gammell:** …rebuilds every night or whatever. Or you can pull stable releases, and that's kind of the idea we're talking about, right? Yeah. A PCB rev-A would be a stable build. Yep. Regardless of how unstable the hardware might actually be. But, yeah, I mean, it's just a mindset change, and you have to have…

**Dave Jones:** I've got experience with that, working at a software company, right? Yeah. You know, Altium, right? Yeah. …Cad tool, very complex. You know, we're talking, like, you know, 10 million lines of code all up or something, right? And, yeah, we would get that daily build thing. And, you know, everyone was encouraged to use the latest daily build. So, some, you know, in some cases, yes, we were updating our tools daily, you know, straight from the, you know, overnight build. Yeah, it ran overnight. Well, let's see, you know, and then word quickly spreads through the office. Oh, that build was shit. Something went horribly wrong. Yeah. Oh, no, I just installed it.

**Dave Jones:** I just did real work with that. You know? Yeah. So, we were actually trying to do real work, you know, because I was in the hardware group, and we were developing real products. Yeah. You know, laying out real, in some cases, very complex boards, and using these daily builds. And it was a nightmare.

**Chris Gammell:** Yeah, that's tough, man. I've never tried. I've never had the gumption to try that. It scares me too much. It's scary. Because there's so many other things that can go wrong in any project, right? It's like, I mean, I know that that's the basis behind a lot of, like, software people always talk about, like, test-driven development. And it's because of that, right? So, then, when you do these builds, you have this standard battery of tests you run and everything. And that makes a lot of sense. That's a good way to deal with it. But it's like, man, that's not – can I just avoid that altogether?

**Dave Jones:** And that's what we did in the end. Can you just tell me when it works? Yeah. That's what you had to do. Because sometimes my files would be corrupted, right? My PCB file would be corrupted. And then I'd have to go to the guys who wrote the PCB core and go, look, this is a really valuable file. Can you recover it for me? And they'd, you know, write a little script that would, you know, undo all the crap that happened, you know. And they'd – yeah. Yeah, they'd ultimately – so, I don't think I ever lost anything. But the amount of time we lost just, you know, dicking around with unstable builds and non-baseline builds was incredible. Yeah. But it had its advantages when you're internal to the company. It means you flesh out any errors pretty quick, you know, any major showstoppers pretty quick, you know. Yeah. That's why they liked using us as guinea pigs because we were using it to design a real board. So, hey, let's use the hardware group as guinea pigs to, you know, see if there's any showstoppers.

**Chris Gammell:** I've heard that referred to as eating your own dog food. I think that's what – I forget where I – it's like a software phrase, I guess. Yep. But, yeah. Yep. You know, making sure that it still works because you're a regular user. That's it. That's it. So, there's pros and cons. Yeah. We had some – open source hardware junkie on Reddit actually was asking about firmware version control because this is kind of like – basically, this is all built into version control stuff, right? So, we're talking about the versions of software and, you know, being able to pull from a repository and stuff. And so –

**Dave Jones:** Yeah, we're talking about GitHub and Subversion. Yeah, right. All that, you know, all that sort of jazz.

**Chris Gammell:** Yeah. I haven't – I haven't jumped into GitHub. I know a lot of people use it and –

**Dave Jones:** Yeah, I've never – well, we used Subversion at work before and I kind of liked it. I got used to it. I thought it was really quite neat and the Tortoise plug-in which allows you to just, you know – from – and it all worked from Windows Explorer, right? So, I could just, you know – Yeah. It worked really well. It was – I really liked the way – Right.

**Chris Gammell:** You're going to get creamed for that. You know that, right? Everyone listening right now is like, no! No! You're going to use it? I know. Basically, everyone I've talked to says, no, no, no. I've used Subversion before too and basically the difference is, you know, the way the branching. And the trees and all that other crap. That's like – I don't personally – I still think of everything like you do with like directories and, you know, backing up individual files. Yeah, yeah. Yeah, same here. Yep. And the Git style of things is like, you know, actually like forking different pieces of code and then being able to merge it all back together. And what I've come to determine is I could learn – learning Git seems like if you're working from a command line and you're building like that, you're doing your own make files and everything for firmware. That's when it's like – I know there's other reasons to use it as well. But like the people that really use it, you know, well are doing stuff from the command line. They're, you know, they're doing immediate pulls from – they're cloning from Git and everything. And yeah, that's fine. I just – I haven't done it.

**Dave Jones:** No, I don't – well, I don't need to. There's no – you know, I still don't use Subversion. I just, you know, there's my – my projects aren't that complex. There are a couple of C files and a couple of PCB files. You know, it's not rocket science, you know.

**Chris Gammell:** Right, right. Yeah, I've had this discussion – maybe we've had it not here before, but – Probably. I've definitely had it with other people before too. And it's like – even with like big FPGA projects, like just the nature of the files, you know, like actually because there's a lot of binaries and like encrypted stuff because it's, you know, there's a lot of proprietary code with the vendor zone. And that sometimes it's just like – I had this big argument with someone I was working on FPGA project with before and they're like, no, just zip it all up. Number 72. And now you move to 73. You know, it's just like – well, that's one way to do revision control. It's not very good, but –

**Dave Jones:** No, no, it works. It gets you back to a baseline, you know. Yeah, well, yeah.

**Chris Gammell:** And that's – I guess that's eventually it. Right. Yeah. You could always just, you know, keep switching computers, right? Right. Oh, boy. You know your software will stay the same too.

**Dave Jones:** No doubt we'll get taken to task over this.

**Chris Gammell:** Oh, yeah. Yeah. I mean, yeah. Us hardware hacks, you know. Anyone with any kind of software experience, you know, they almost always –

**Speaker ?:** Yeah, yeah.

**Chris Gammell:** They just tell you. Right about now. Yeah. Right. Yeah. Nah, nah, nah, nah, nah. You can't talk back right now.

**Dave Jones:** But at least we know what GitHub is. Right. Exactly.

**Chris Gammell:** Yeah. We are doing better. I mean, I'm interested with people – you know, some people put their – their PCB projects up in GitHub. And I haven't – Right. I haven't figured that one out yet either.

**Dave Jones:** I see that. Yep.

**Chris Gammell:** Yeah. So it's on my to-do list for sure. But – Right. Yeah. But I think the thing that this comes down to, though, is that, you know, like, obviously hardware is very different than software and firmware, right? And hardware is hard, right? It is. Hardware is hard. Yeah.

**Dave Jones:** Beautiful segue.

**Chris Gammell:** Thank you. Yeah. So you posted this article about – it was from LinkedIn. Did I? Talking about – Yeah. I think you basically reposted right after I did, but – Ah, right. Well, there you go. Yeah, but basically they're talking about Remotive, which is a little iPhone robot that went commercial. And it's just, you know, they're talking – you know, they talk about the difficulties of moving from Kickstarter over to actual manufacturing, and then manufacturing and volume and everything. And it's –

**Dave Jones:** Well, by volume, they're talking about Kickstarter volume, which is like – they're talking like 4,000 units or something. I mean, this ain't volume. This is just, you know, this is amateur hours still, right? Yeah. Yeah.

**Chris Gammell:** I mean, zero to 4,000 is tough, right? I mean, like, it's not easy, but it's no –

**Dave Jones:** Like, a 100,000 would be serious production, right? I agree. I mean, 4,000 is still – you know, you can do everything the old-fashioned way, you know? So, and, yeah, it's not that, you know – it takes half a day to run it, you know, or a day to run through 4,000 boards through an SMD line, you know? It's not, you know? Yeah. It's not rocket science. But then, again, if you get something wrong, yeah, it's, you know, you've got 4,000 boards. So, you do your standard, you know, let's run a pre-production panel through the machine first to, you know, to make sure everything's right. Oh, the machine's set up, okay, and you quickly test the board, and, oh, everything's fine, okay. And then you press the big red button, and your 4,000 boards pop out.

**Chris Gammell:** Yeah. So, yeah, there's a few issues there, but it's not – You've got to help you if your revet isn't right still, you know? If it's a systemic error in your actual layout or something. Oh.

**Dave Jones:** But it's hardly – like, this is not huge volume. Once again, you know, the volume people will back me up. They'll go, ah, that's just, you know – you know, it's like the RF guys saying, you know, 100 megahertz is DC, you know? Right, yeah. Ah, this is practically DC volume, you know?

**Chris Gammell:** Yeah, it's all relative stuff, right? Yeah, but I think the thing is we're going to continue to see a trend of, you know, people who are, you know, getting into manufacturing and saying that, yeah, I want to make stuff. I want to produce things and sell hardware. And then it's just going to be this – it's going to be a continual shock to the system for people that are jumping into it, you know? Right. Because it's hard, you know? Yes, hardware is hard. Hardware is hard. Yes, it is. I was talking to my wife about different industries over the weekend. And, you know, like hardware came up as like an industry that's not particularly profitable, right? I mean, you look at like software, you know, there's no – Hang on a sec. Okay.

**Dave Jones:** Hang on a sec. Like you were talking to your wife about different types of industries like this. Does she care or were you talking to – or were you talking to her? Or were you just, you know, and she was just rolling her eyes?

**Chris Gammell:** She was probably nodding her head mostly, but – Right, okay. I was just – we got talking about mining, right? I mean, obviously mining is huge in Australia too, right? Yeah, yeah. And, you know, just like mining and oil and just industries that are big, big industries, right? I mean, like big stuff and just like where the capital cost is. I mean, she's studying accounting too. So it's like, you know, like she has some interest in some of this stuff. And – but, you know, it's just interesting from a – you know, software, right? I put software in the same field as like – as mining. I mean, obviously there's still capital costs involved with both, but, you know, mining is –

**Dave Jones:** Are you serious?

**Chris Gammell:** Yeah. Come on.

**Dave Jones:** What's the difference? Software is – software, the only capital cost is jolt cola and pizza. And they're not capital. They're consumer. They're, you know, consumables.

**Speaker ?:** Yeah, that's true.

**Dave Jones:** That's true.

**Chris Gammell:** I mean, yes, I know there's a lot of – a lot of – a lot of initial investment in mining. But like in terms of like the actual per unit cost of moving from one unit to a 10,000 like we were just talking about. Like there's very little relative to the outcome, right? So like mining is mostly buying your equipment, buying the land, and then pulling stuff out of it, right? And software is –

**Dave Jones:** Well, it becomes an operational production issue then. Yeah. Because mining is mining production. I mean, it is a production optimization issue. Yeah. Essentially.

**Chris Gammell:** Hmm. Well, I'm probably out of my league on all that stuff, especially talking to an Aussie. But –

**Dave Jones:** Well, no, well, I – see, I come from the oil exploration and mining business.

**Chris Gammell:** Right, right.

**Dave Jones:** I know how much money and capital goes into it. It's phenomenal. Hmm.

**Chris Gammell:** See, I guess I was thinking about – you know, it seemed like an initial investment and then mostly, you know, mostly a harvesting of value then, right? And the same kind of thing with –

**Dave Jones:** Well, that's the idea, yeah.

**Chris Gammell:** Yeah. Right. And then – but the difference being like with hardware, right? You have an initial investment for tooling and then you have a pretty significant capital cost per unit, right? So if I'm making a board that's – you know, I can sell for $100, it's going to have $20 or $30 of parts in it, right? Right, of course. And the PCB and everything else, right? And there is that chunk of cost. You can only make so much more past that. There's a fixed margin.

**Dave Jones:** It becomes a fixed margin, you know?

**Chris Gammell:** Right, right, right.

**Dave Jones:** And there's no – and there's almost no magical limit where it suddenly becomes, you know, an order of magnitude cheaper. Right, right, yeah. You know, if you jump from 10,000 units to 100,000 units, it doesn't necessarily – you know, it's not like your base cost drops by an order of magnitude.

**Chris Gammell:** Right. Yeah, it's still that initial cost.

**Dave Jones:** It's like a gradual – yeah, it's like a gradual decline, you know? Yeah, it might gradually get cheaper as you go up in volume, but – Yeah.

**Chris Gammell:** So I was looking at all these different industries, though, you know, just thinking about that kind of stuff. And the same kind of thing for, like, just where – mostly what I was doing is I was looking at the uber-rich, right? And just wondering where uber-rich people's money comes from. And wondering when you'll be uber-rich. There may have been that, yeah. Right. But no, that's not what drives me. It's more curiosity. I mean, like, honestly, like, looking at that, right? So, I mean, software is an obvious one, right? There's – because – and there's a lot of value. They're creating a lot of value with minimal unit cost. Mining is a lot of value with a large upfront cost but minimal unit cost. Brands, right? Brands are worth, like, looking at – so then looking at Apple, right? They might have a computer with $200 worth of parts that someone else could sell for $800 and they're selling for $2,000, right? And that difference there is brand, right? So, brand is minimal per unit cost. And that seems like what I – that's basically what I came up with. Like, anyone in any kind of economics 101 or, you know, business course is like a duh. But I don't know. It was just interesting because then, you know, like, comparing the two, right? As people start looking at hardware companies and because hardware is getting more focused these days, it's just going to be this big smack in the face for a lot of people that aren't used to upfront costs. So –

**Dave Jones:** Right.

**Chris Gammell:** That's going to be the main thing.

**Dave Jones:** And that's why Kickstarter came along. Right. Because people can't afford the upfront cost. Yeah. So they have to get the money upfront in order to pay the upfront costs.

**Chris Gammell:** Exactly. Exactly.

**Speaker ?:** Hmm.

**Chris Gammell:** And you can fund some crazy things, right? I mean, we've seen that, right? For things that are unbelievable projects, right? Like, oh, I don't know, a space telescope. A space telescope. Or as I wrote, a frigging space telescope.

**Dave Jones:** This is very cool. Why did I not hear about this? I probably would have backed it so I could get my photo in space. Yeah. Right. Yeah.

**Chris Gammell:** So if people haven't heard, what they're doing is basically they'll upload your photo and then I guess somehow they'll frame the Earth in the background. So they'll –

**Dave Jones:** Yep.

**Chris Gammell:** Personally, Photoshop sounds a little easier to me, but – But yeah, it's a cool project. I've seen this mentioned. I've definitely seen the name because I always think – I look at it and I think it says Ackroyd. You know, like the Dan Ackroyd. Yeah, but it's Arkid. Arkid, yeah. A-R-K-Y-D.

**Dave Jones:** I wouldn't have guessed that pronunciation.

**Chris Gammell:** Yeah. But yeah, they raised a million and a half bucks and so they're going to send hardware up to space, right? I mean, like, that's pretty cool.

**Dave Jones:** Have you watched the video? I assume you have. They're a very impressive list of people in there that they had back in this thing.

**Chris Gammell:** Yeah, right. Right. And I'm not sure how I didn't really hear about it either. And I'm sure a lot of people have. But yeah, it's cool if people haven't seen it yet.

**Dave Jones:** Now I can't get my selfie photo in space.

**Chris Gammell:** Now you'll just have to pay 20 million and go up to space, right?

**Dave Jones:** Right. Yeah. Yeah.

**Chris Gammell:** You'll get there. Don't worry.

**Dave Jones:** If I'm in the software industry, yeah.

**Chris Gammell:** Yeah, exactly. Well, yeah, right? I mean, like, is Richard Branson the one sending people up there, right?

**Dave Jones:** No, but the first Microsoft, the Microsoft head architect. No, no. Not Paul Allen. Oh, what's his name? Mental Block. He was the chief architect of the Office products. Oh.

**Chris Gammell:** Oh. Those names all run together for me.

**Dave Jones:** Yep. Yep. Anyway, he was the, I'm not sure if he was the first paid space tourist, but he was one of the early ones.

**Chris Gammell:** Oh, he paid the Russians, right?

**Dave Jones:** Yeah, he paid the Russians and went up to space. Yeah. He used his, you know, it cost him 20 million bucks or something. But hey, you know, that's nothing compared to all the Microsoft shares he had during the boom years. Yeah, that's crazy. Ah. Ah.

**Chris Gammell:** Ah, money. Money's stupid. Some days.

**Dave Jones:** I've got, Charles Simonyi. Goodness sake. Charles, yeah, he's Hungarian. Yes. Charles Simonyi. I don't know. Thank you very much.

**Chris Gammell:** Yes. So you asked Google who the Microsoft founder was?

**Dave Jones:** No, no, he wasn't a founder. He was just one of the early employees.

**Chris Gammell:** Gotcha.

**Dave Jones:** And Bill Gates, if my memory, computer history serves me correctly, Bill Gates hired him because he did a software thesis on the best way to develop software. You know, like he developed his own technique for developing software. And Bill Gates thought that was the greatest thing ever and hired him as chief, you know, one of the software architects and tried to use the, I think they call it the Simonyi method or something. Or anyway, something like that. And to develop their software. And it didn't quite work that well, but still, he was a really smart dude and was the architect of a lot of the main Microsoft products you see today.

**Speaker ?:** So.

**Dave Jones:** That's pretty cool. Yeah. Yeah. And there you go. In 2009, he went aboard Soyuz to the International Space Station. Yeah. That's all. Yeah. No. Sorry. In 2000, he's been twice. Oh, two sucks of the sav. In 2007, he went up on, yeah, and then four trips later, he went up again in 2009, went to the International Space Station. But hey, his net worth is a billion dollars. So, you know.

**Chris Gammell:** Yeah. Well, at that point. Yeah. Have you heard the phrase, software is eating the world? Have you heard that?

**Dave Jones:** No.

**Chris Gammell:** No. It's kind of like a, I think the idea behind it is basically just that, you know, everything that can be optimized by software is slowly being optimized. The point that, you know, it's hurting jobs, hurting everything else, right? I mean, like, it's just, it's just affecting everything.

**Dave Jones:** It's also creating a new field of jobs. Also, you know, a lot of people say, oh, you know. Yeah, it's taking jobs away. But it's also creating jobs in a different space.

**Chris Gammell:** So, yeah. That's true. And yeah, and then he basically anytime anyone says, you know, they took our germs. Yeah, there usually is that other side of things. And yeah, I mean, like, so Paul Graham wrote an essay recently about investing trends, right? In software and hardware and everything else, too. And he said the same thing, right? But basically that there's a consolidation of everything. Basically, he's saying that there's going to be more startups around a lot of this software explosion. Continued software explosion, of course. Not like it's new. I don't think it started in the late 70s. Yeah. Yeah. Have you heard about this software? It's going to be pretty big, Dave. We should get in on this. It kind of rings a bell. Yeah. Yeah. Yeah.

**Dave Jones:** I've heard a couple of people have made some bucks from it. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Speaking of which, we need to make some bucks.

**Chris Gammell:** Ooh. Yes, we do. And we have a new sponsor.

**Dave Jones:** We do. Yay.

**Chris Gammell:** So we are happy to announce. Netburner.com. And welcome, Netburner. Yeah. They have a wide range of stuff to get you online quickly. Get your projects up and running Ethernet-based hardware very quickly.

**Dave Jones:** With minimal capital outlay.

**Chris Gammell:** Are you reading that up? I think Dave just made that up. Yeah.

**Dave Jones:** I did.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, they've got lots of, yeah, net-based boards, you know, so to get your project modules and things, to get your projects on the web, online, networked.

**Chris Gammell:** Yeah. And the thing that they really like is getting your stuff up in less than a day. That's kind of the big thing. And so Tom was actually nice enough to send both Dave and I a board to try out. And we both were able to, you know, basically.

**Dave Jones:** It took me about five minutes. And I was talking to this thing on my Ethernet connection. You know, it's not.

**Chris Gammell:** Yeah. Yeah. The hardest part for me was I put in the license key wrong. And then I kind of did a head bump. Yeah.

**Dave Jones:** I put the license key in wrong too. And, yep. That fooled me for about a minute. And then. Yep. But once you figure that out. Then we're on.

**Chris Gammell:** Yeah. It's basically there's a tool that allows you to go out. It'll even discover the stuff on your network if you're on the same Ethernet network or if you've got a crossover cable. And then you can just start talking to, you know, there's just like an embedded web server in there. It serves up pages. And you can kind of start toddling hardware.

**Dave Jones:** There's embedded Twitter clients and all sorts of jazz. All the usual fare for network stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** And the other thing I found interesting is that they not only just sell the products, but they also have, I believe, consulting services. Where if you need somebody to, you know, write your, you know, if you've got a brilliant idea for some new whiz-bang gadget you want to put on Kickstarter, but you don't know anyone to write the software for it, you can actually hire these guys to do all your high-level intelligence net programming and get your widget online.

**Chris Gammell:** Yeah. Yeah. Basically, you can buy the kit from them, turn around, and pull their design files into your design and have this kind of module sitting in there. Or even on the one that we have, it's actually pluggable. It's got like, you know, 0.1-inch headers, similar to like, you know, a lot of dev boards out there. But you could take that and then plug it into your design if you wanted to. And it's just, it's sitting there. It's got a cold-fire processor. It's got memory on board. And it could just sit there and then you could pass commands to it. And, yeah, it's pretty good from that perspective to get up and running quickly.

**Dave Jones:** I've got a sitting, it's staring at me right now. It's got some leads. I'm flicking some dip switches. Yep, yep. I was playing a game on it before.

**Chris Gammell:** Tic-tac-toe, yeah, I was doing that too.

**Dave Jones:** Tic-tac-toe, I was playing tic-tac-toe. Yeah. You can't win.

**Chris Gammell:** I never win, yeah.

**Dave Jones:** But you can stop nuclear Armageddon with tic-tac-toe.

**Chris Gammell:** Oh, that's right. What's that, War Games? Is that the Matthew Broderick movie? War Games. Is that what it was? Absolutely. Would you like to play a game? Yeah.

**Dave Jones:** Shall we play a game? Yep. Sorry, I can't do the Joshua voice.

**Chris Gammell:** So, people should check out netburner.com slash theamphour. Netburner's actually giving the Amp Hour listeners a 20% discount on kits. And if you're interested, they're also doing, they have a bounty for writing up articles, basically. They'll pay you to write articles for them. So, yeah. Netburner.com slash theamphour. And thank you to Netburner for helping us out. So, definitely be sure to check out their stuff.

**Dave Jones:** Keeping us in business. Yeah. So, that Chris can become filthy rich and sit on a throne of cash he's always dreamed of.

**Chris Gammell:** I'm going for the golden toilet, Dave. That's the real thing.

**Dave Jones:** Right. Golden toilet. Yeah. Yeah. Oh, boy. Yep. Telling you, you just got to, I don't know. Well, you can always do it the old-fashioned way. You know? Gun, mask, bank. You know? Still works these days. Yeah, I suppose so.

**Speaker ?:** That's the thing.

**Dave Jones:** Nobody expects that anymore. You know? That's right. They'll never see it coming. All of the criminals are working in finance now, you know? And, right. That's where the real, that's where the smart criminals are. But you still do it the old-fashioned way. Nobody expects that anymore.

**Chris Gammell:** Yeah, I never see it coming. You know? No, I never see it coming. Well, you can build a robot to do it, right? I mean, you could.

**Dave Jones:** We could do an old-fashioned heist, you know?

**Chris Gammell:** Yeah. Pick somewhere in the middle. Go rob a bank in Hawaii. Hawaii, right. Okay. Some country we can't get extradited to, right? Right. Oh, yeah. Yeah.

**Dave Jones:** You've already been flagged for analysis by the NSA. Oh, yeah. Oh, yeah.

**Chris Gammell:** I'm toast. Just for talking to you, really. Yeah, exactly. That's the worst thing.

**Dave Jones:** You're talking to somebody who's no doubt on a no-fly list somewhere. Oh, yeah.

**Chris Gammell:** Yeah. Yeah, and if people are listening to this, like, years down the road, sorry. I'll just say, we're sorry now. Please get us out of jail, you know?

**Dave Jones:** As we're rattling our, you know, tin can on the bars. Right, right.

**Chris Gammell:** Let me out. Right. Well, I was looking at our stuff the other day, and I saw that, like, 80 people had listened to our first episode last month. And it's like... Oh, really? Wow. Oh, crap. Yeah, people are like, yeah, they're still, you know, kind of catching up or going back and listening to old stuff. So, whenever you are listening to this throughout time, welcome.

**Dave Jones:** You can check out how much our first show sucked.

**Chris Gammell:** Oh, God. It was terrible. It was so terrible.

**Dave Jones:** Mind you, we haven't improved much. No, no, no, no. Well, we'd have to practice. It's still the same crap format. Yeah. You know, we just make stuff up and...

**Chris Gammell:** Yeah. Yep. So, what have you been working on lately, man? How's your power supply project going? Is that... No? Surely you jest. I do. Well, no, I don't, actually. Is that...

**Dave Jones:** I keep saying that I'll just sit down and do a whole bunch of videos, get them out of the way, and then I'll have two weeks free to work on stuff, and it's like, eh, it never happens.

**Chris Gammell:** Right, right. Forum's always calling your name. It's tough to do that, you know, to work ahead like that, you know, it's like...

**Dave Jones:** Yeah, yep. In regular work, too. But there are some people who actually can do that. That's natural to them. For me, it's not, you know, I don't... Yeah. I'm not a big plan ahead guy.

**Chris Gammell:** Well, yeah, if you have, like, a deadline coming up, right, if you were going on a... If you were on a trip where you couldn't have internet, right, you'd have that kind of thing.

**Dave Jones:** Oh, I've done that before. Yeah, when we've gone on holidays, I've got, well, you know, yeah, okay, we've got a deadline, I have to shoot four videos before I leave, you know, and edit them and upload them, and yeah, and nobody knew I was gone, you know, and here I was from my hotel room overlooking the beach with my feet up or, you know, and in a swimming pool, a tablet comes out and boom, enable a video.

**Chris Gammell:** And... Well, it's the same kind of thing as, like, when you have, you know, like, when you have deadline of work, right, it's like... Right. I've had a deadline, I have a deadline coming up, and it's just, you know, it's not like I'm doing... I wasn't doing work before, but it's, you know, like, the nature of the work changes, right? You have that... Right. Of course. ...that shift in desperation. That's desperation.

**Dave Jones:** Desperation. Yeah.

**Chris Gammell:** Desperation is a stinky cologne. Oh, boy.

**Dave Jones:** Yeah.

**Chris Gammell:** So, you know, you know how it goes, though. You know, you have the last-minute changes and the cuts and the jumps and the late-night soldering sessions, and it's... I'm telling you, quit. Quit? Oh, yeah? Is it... Quit? Well, you can... Dave's...

**Dave Jones:** Well, you're going to have your million-dollar business soon, aren't you?

**Chris Gammell:** Yeah, sure.

**Dave Jones:** Come on! You put it on here. You put it on the list. It was the perfect segue.

**Chris Gammell:** Oh, that one. Oh, I was like, what are you talking... I was like, what the hell are you talking about? Yes, that is a... That is a rising trend. I know, right? That is a rising trend.

**Dave Jones:** Yes, a Forbes article you put on here because you lust after this stuff. You're just there. No. Search in there all night. Oh, I had to be rich. No.

**Chris Gammell:** Dave, you make me...

**Dave Jones:** Yes, you are.

**Chris Gammell:** No, this was on Reddit. Come on, let's be honest here. I guess, yes, I was on Reddit and... Oh, look at this.

**Dave Jones:** The rise of the million-dollar one-person business. Right. Article in Forbes magazine. So it must be true.

**Speaker ?:** Yeah.

**Chris Gammell:** I think it's interesting just because it shows... I mean, it's the same trend that we see in a lot of other places, right, of just smaller and smaller businesses, right? I mean, like, you're a one-person business. You refuse to be anything but a one-person business, right?

**Dave Jones:** Well, I don't refuse. By the nature of my business, it's very difficult to do anything but. Right. I heard refuse.

**Chris Gammell:** Yes. But, you know, I see this, too, in electronics, right? I mean, like, they even talk about the different categories and everything like that. They kind of move through the different, you know, levels. And this is just based on U.S. tax returns, and I think they did some surveying and stuff. But, you know, like, a lot of it in there is consulting-type stuff, right? And working on electronic... Or working on, like, scientific and engineering consulting.

**Dave Jones:** Well, they said most of it was finance. Finance consulting and stuff like that, which isn't surprising. In the 5 million bracket, like, they actually break it down. These are interesting numbers. Yeah, yeah. There are 1.6 million, as we call them here, sole trader, same as I am, you know, and same as you are, right? 1.6 million sole traders in the U.S. earning between $100,000 and a quarter of a million.

**Chris Gammell:** Right. That's a lot. That's a lot.

**Dave Jones:** That's a lot. And there's 26,000 of them between 1 million and 2.5 million.

**Chris Gammell:** Yeah. That's a lot, too.

**Dave Jones:** And they do actually say, where is it, the next highest one in the bracket was the entertainment business. I think they're talking about the YouTube, sort of, you know, the newfangled YouTube entertainment business. Oh, yeah.

**Chris Gammell:** Well, it could be that, or it could be, you know, like just a personality, you know, like a TV show, right? If you incorporate it as a person or whatever. But, yeah, I mean, but the point I was trying to get with all this is that, you know, it's getting to the point, though, where even in a small-scale manufacturing type thing, right? I mean, getting to $200,000, right? I mean, this survey is talking about receipts, basically. That's revenue. And so there's a lot of cost in there. They're not profiting $200,000, right? But the business is making $200,000. And, like, yeah, that's, I mean, like, that's a lot of money, but it is doable, right? If you are a small-time, you know, a small business person, you're working, even if you're fabbing in your house, right? You know, if you think, if you're selling a $200 kit and you sell $1,000 a year, that's, there it is, right? I mean, like.

**Dave Jones:** It's $200,000, yeah. Yeah, exactly. You know, I know somebody who has that mythical $1 million a year business, you know, selling hardware stuff. But, you know, they, the margins are very slim because of the area that they operate in. And, you know, he dreams about earning the same amount I do, you know? It's like, oh, you know, and yet he's a million-dollar business. So, yeah, it's all about margins.

**Chris Gammell:** 5% margin is, what, $50,000 a year, right? So, that's effectively what he would be taking home and then taxes and everything else. But, yeah, this is what I was getting at before, right? That's the same kind of thing of hardware being a, you know, a high-capital business, right? Because he's got to pay $950,000 a year in hardware costs and shipping. And, really, this isn't one-person businesses. That's the other point of the article. It's like, it's not really one person, right? It's one person listed. And then you have an accountant, you have a lawyer, you have maybe even, you know, like a part-time assembly person. The lawyer, come on.

**Dave Jones:** You don't have a lawyer. You have an accountant, yes, and you have an assembly person and you maybe have a contractor who does some work for you, you know? Yeah. So, yeah, I mean, it is hard to, you know, make that million dollars as, you know, a true one-person entity, really. I wouldn't put the accountant in the same, you know, accountant, like, you know, I wouldn't count that. But certainly somebody who does work for you or something like that, you know, some contract design work or, you know. Oh, right, right, right, right, right. Right.

**Chris Gammell:** Well, I mean, it's just getting, I mean, it is getting easier to do this kind of stuff. This is the rise in a lot of these, you know, smaller startups as well, right? And I think another thing that is driving a lot of this is just, like, the fact that so much stuff gets pulled in to chips, right? This is the stuff that I've mentioned before with, you know, just the systemization of chips, right? Right. And we've seen this, like, the CC2500 series from TI, right? That's some of their wireless things. And there was another one here that was released recently by a company I've never heard of, but the actual, the chip itself looks interesting. It's called Dialog Semiconductor. And basically it's another, it's just another small, a very, very small Bluetooth system on chip. And it's, I mean, it's just, like, these kind of things, like, basically it's, you know, it's a little arm. It's got SRAM on it. It's got baseband type stuff. It's got encoding. It's got radio circuitry and everything like that. And basically then it has stuff that you can talk to remote stuff with, right? So if you want to talk spy and, you know, you can have the ARM processor actually, you know, talk to other chips. It's like, you know, you can make little sensor boards, right? And that is a lot of what we're seeing in the hardware startup space of, you know, network sensors and stuff. This is the reason that the Internet of Things will happen. Not because of anything else. It's not software, I don't think. I think this stuff and what TI is doing and Nordic Semiconductor and all those others, like, that is the final piece, really. I think it's always been about the wireless. And this is another one. Basically, this is another one. And they're saying it's low cost, too. I don't really know the cost because it just came out.

**Dave Jones:** Well, it's low energy. It does the 4.0 Bluetooth low energy thing. Yeah. Right. So, yeah. Yeah, so it's a cool little part. Although it needs 3.8 milliamps for receiving and TX.

**Chris Gammell:** That's not very high, though. I mean, honestly, for radio, that's not bad at all. I mean, so it's, you know, it's, this is what I was pointing out, though. It's just like, this is the, this is what's driving a lot of that other stuff. And it's what's going to drive, I mean, this is what's going to change the nature of hardware, I think, too, right? This is the trend I've seen. And, you know, it's like, from an analog perspective, I've seen a lot of the systemization of chips where, you know, you get more and more stuff pulled into either onto the silicon or into the packaging. Because if you even just look at this block diagram, right? People can go to the site and look at the block diagram. And it's similar for the TI parts and everybody else. But, I mean, like, okay, so there's a processor. There's, there's SRAM inside. There's, I guess that's crystal. But there's RF circuitry. There's clock management. And then there's, there's like, you are type stuff.

**Dave Jones:** There's a buck boost DC to DC converter. There's LDOs built in.

**Chris Gammell:** Yeah. Like, all that stuff. You don't need. You think about the former cost, right? It starts to balloon, right? Yeah, yeah. It's like, to use your Back to the Future favorite thing, right? It's like when Doc rebuilds the microcontroller that, on the hood of the DeLorean, right? And it's all tubes. Right. And everything else. And, I mean, it's the same kind of thing, though, right? It's just, that's what it used to be. And then if you think about how many people used to be designing each of those components, it's like, no, no. It's just commoditization. And, you know, basically you have these building blocks and you just drop them into different pieces of silicon and away you go. And this is not a big part either.

**Dave Jones:** I mean, this is actually a crazy chip. Yeah. Is this a chip of the week? I think this is a chip of the week. Sure.

**Chris Gammell:** Sure. Chip of the week. I mean, we don't know if this works yet.

**Dave Jones:** Well, it's got a 10-bit ADC in there. It's got a quadrature encoder. I squared C, SPY, UART. It's got two UARTs. It's got timers. It's got an ARM Cortex M0. Which is neat. It's got encryption built in, right? Yeah. It's got the radio transceiver, of course. And, as I said, it's got the, you know, all the DC to DC converter stuff. So, you don't even need your external power supply. You need some components, obviously.

**Chris Gammell:** You probably, yeah. It probably doesn't have an integrated FET, but just because of the size. I mean, it's tiny. It's low power, too. So, I mean, that's pretty crazy, too.

**Dave Jones:** Unfortunately, it's a little pain in the ass BGA. Well, no, they have QF as well. 2.5 millimeters by 2.0. Oh, do they? Oh, okay. All right. All they show is a photo of the BGA.

**Chris Gammell:** Yeah. Yeah, BGA is kind of, yeah.

**Dave Jones:** Evil. But this is, yeah, this is really cool. This is amazing. Makes me want to go out there and design something.

**Chris Gammell:** Well, there you go. I mean, that's the thing. And it's like, that's the other side of it, right? I mean, like, I could complain about the systemization all day long. But at the other end, it's like, you know, I look at me, and I could go and turn around and pick a module type chip, or SOC type chip like this off the shelf. It's like, oh, I, you know, I could use example code from them, and I could basically, I know how to, you know, use spy ports and, you know, talk to other chips that have spy ports or SOC. It's like, it's within the realm of possibility that I could do something like that, and that should be scaring people.

**Speaker ?:** Right.

**Dave Jones:** And within six months of just having, you know, seeing this chip, you can have your million dollar business.

**Chris Gammell:** Well, yeah. Via, I don't know. Yeah.

**Dave Jones:** Kickstarter or something else. Well, maybe. Grow. Yeah.

**Chris Gammell:** No, but I mean, like, yeah, maybe, but I mean, that's the difference between going from one to, you know, 4,000, right? You know, you...

**Dave Jones:** Well, no, you can get the money without having to do that. That's true. You can get the money, and then you've got to figure out how to do it.

**Chris Gammell:** Yeah.

**Dave Jones:** There's the kicker. No pun intended.

**Chris Gammell:** Why would that be, uh...

**Dave Jones:** See what I did there?

**Chris Gammell:** No. Kickstarter. Got it. Kickstarter. I got it, folks. Right. We're cool. We're cool. I got it. All right. Ah, yeah.

**Dave Jones:** Oh, dearity.

**Chris Gammell:** I mean, that's not the only thing either, right? I mean, like, so, so, like, TI mentioned with the CC2500 series, but they, you know, they have a lot of this stuff that's out there, too, right? They released this, what is this, Precision Design Library, right? I mean, like, and again, this is the thing where, if people excuse my ego a little bit, right? It's like, you know, as an analog designer, I look at this, and I'm like, oh, man, they're doing all the fun stuff, right? Right. And then practical guy who's on a deadline chirps, and he's like, dude, just shut up and use it, you know? Just go. Exactly. Right? There's still going to be tons and tons of problems, and even if you drop this in, then there's going to be issues over there, right? It's like...

**Dave Jones:** Oh, of course. Yeah, yeah, yeah. Exactly. Yeah. Murphy gets you any way you go. Oh, yeah, it does.

**Chris Gammell:** Murphy's an ass. Bastard. Yeah.

**Dave Jones:** The thing I don't like about all these new system-on-chip, and it's been happening for 20 years, right? I'll see a neat chip come out, you know, and I'll go, oh, that's so cool, and then I'll get a project idea, and then I drop my current project I'm working on and never finish it, because I've just started another bloody project with the latest whiz-bang frickin' chip to come along. It's a pain in the ass. We said stop it. Yeah, I think... Or maybe I should just stop looking.

**Chris Gammell:** Yeah, maybe that's one thing. I think the currency of the future will be how fast you can iterate a design, right? I mean, maybe even to the point of... Oh, yeah. You know, there are design houses out there that'll do, you know, like, I guess... We've already... We see that a lot, too, with, like, the computer industry, right? I mean, like, they'll get pre-information about, like, a new Intel processor, but then, you know, they turn stuff pretty darn fast, you know? It's incredible. Yeah. And they throw people at it, and they throw a lot of money at it, because you have to do quick turns on a lot of PCBs and stuff, but, you know, like, that's... It's not like a new phenomenon, but I think it's going to be increasingly that the constraints on engineers of the future will be, you know, faster, faster, faster, right?

**Dave Jones:** It's time, like it always hasn't, you know? Yeah. I don't know, though. Yeah, it's always time, but, you know... Yeah, but these days, in terms of, you know, in terms of seeing the number of people, right, a new chip comes out like this, right? And bingo, you'll instantly see, you know, within, you know, a month, you'll see, you know, maybe two or three projects on Kickstarter, and you go, oh, no, I've missed the boat, you know? And it's like, oh... Yeah. Before, that thing couldn't happen, right? You could take, oh, a new chip comes out, but you could take your time getting your, you know, project up and running, and, you know, it was pretty rare that somebody else would come out and scoop you, but now it's just every man and his dog has the tools to...

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** ...and the platforms to come out and gazump you, so...

**Chris Gammell:** Yeah. Yeah, all told, it's a good thing, right? I mean, it's an access... Oh, of course. It's really an access thing. Yeah, exactly. I mean, like, you have, if you have 100 people looking at a chip, and then 10 say, I'm going to use this chip, and then 3 actually go and do it quickly, yeah, I mean, like, that's just an access thing, whereas before, maybe out of that 100 who saw the chip, only, you know, only 5 could actually afford the tools or get the tools up and running or... Yeah, right, right. ...had access to the data sheets or whatever else, so... Yeah, I mean, overall, it's a good thing. From a marketplace perspective, it's a very good thing. I think from a, you know, I think what it... It's this weird blending of, like, needing to specialize, but also being general, right? You need to have something that you're really focusing on, right? So if you're really into, I don't know, like, you're really good at making baby monitors or something like that, you know, like, you could take this chip and then drop it in and just go, right? If you already had, like, another idea, that's probably a bad example, but, you know, some kind of core technology, but then you bolt these other things on there quickly, right? And then you're willing to pay, you know, you're willing to pay people for their support or for the chip's expertise, right? Or, you know, like, even, like, our sponsor, like, Netburner, right? You're willing to pay just for this quick, quick turnaround of... Yeah. ...go, right? I just need it. I need it. Here's the truck money. Exactly. That's it. Get out of my hair. Yep. And I don't want to see it again. And so I think there is... It's... The downside to it all, I think, is that it gets kind of... It's strangely exciting and boring, right? I mean, you have to be really good at one thing, but because you have to be good at one thing, you have to kind of continue to kind of fend off and protect yourself from other people, right? If you want to actually have a business there, you need to be really good at that one thing and then quickly pull in other technologies and go, right? It's a weird... It's a weird dichotomy because it's... It's exciting and scary and boring all at the same time.

**Dave Jones:** And how many times have we discussed this now? A hundred?

**Chris Gammell:** 152. There we go. Yeah. I think... I mean, the other thing, too, is that, you know, you're going to stack software on top of it, too, right? That's the other thing. Yeah, yeah, yeah. Right. You know, like... So, like, SparkFun, Mike Hord at SparkFun. He tore apart a Leap Motion, right? Which is that really cool hand controller for computers and everything. And I thought it was going to be this crazy hardware. It turns out, though, it was just infrared LEDs and then a lot of fancy software. Yeah. Right? And so... I don't know. I thought it was going to be all hardware, though, because it seems like that could be an interesting hardware phenomenon, but it turns out, nope. Yeah.

**Dave Jones:** Apparently, you're a former employer.

**Chris Gammell:** Yeah. Yeah. Oh, well... The owner of my former employer.

**Dave Jones:** The owner... Well... I suppose... Yeah. Sorry. Duh. Okay. You used to work for Keithley, but... Yeah. This is Tektronix. They're all under the same group. They're all owned by the E. Will Danaher Group. And they're talking about looking at some really schmicko 350 gig...

**Chris Gammell:** Yeah. That's a lot of speed. Yep.

**Dave Jones:** Silicon germanium stuff from IBM, of course, who do a lot of the research on this.

**Chris Gammell:** Yeah.

**Dave Jones:** Well...

**Chris Gammell:** Let's take a second to stop. Obviously, a lot of people know what that means, but that means in the span of one second, up and down, 350 billion times. That's a lot.

**Dave Jones:** And if you get down to the deep physics of it, I mean, how do the electrons even have time to... Well, how many electrons are you talking about? You know?

**Chris Gammell:** Yeah.

**Dave Jones:** Nafor.

**Chris Gammell:** Yeah.

**Dave Jones:** That's...

**Chris Gammell:** Yeah. It's... Yeah. It's ridiculous. The physics of it is way outside my scope. But the thing that's interesting about this stuff is, you know, you've... So when you did those reviews of the... What's that chip in the Agilent scopes? The real-time something-something.

**Dave Jones:** Oh, that was a similar thing. It was a silicon germanium thing, wasn't it?

**Chris Gammell:** Right. Front-end hybrid? Yeah, my point is that, I mean, in terms of the actual A to D, though, and the core in there, that is basically the scope, right? We're talking about systems on chip. Oh, yeah, yeah, yeah. No, no. The rest is just the PC. Yeah.

**Dave Jones:** They bolt a PC onto this hybrid front-end, and that's it.

**Chris Gammell:** Yeah. You know? Right. And, yeah. And so, yeah, this is like the ultimate system on chip, right? It's... And, you know, they'll carry with it for years and years and years, because you need to get... You need to amortize it all out, right, over time, because it's... Silicon germanium's not cheap, and nowhere's the verification of these crazy-ass ADDs and

**Dave Jones:** everything, but... And they're talking about real-time bandwidth scopes of 70 gig, which is needed for 400 gig bit per second optical links, and then they're talking about one terabit optical links, measurement tools for that. I mean, just... Yeah. Unbelievable. I mean... Right.

**Chris Gammell:** Right. Yeah, it makes me feel guilty about...

**Dave Jones:** How many of these scopes are they going to sell? You know? Ten? You know? Like...

**Chris Gammell:** Yeah, and they're not going to be cheap. Wow.

**Dave Jones:** No, no, exactly.

**Chris Gammell:** I mean, everything's getting faster, right? But that's just the diversification in the industry, too, of, right? I mean, you and I are talking about, you know, a single Bluetooth chip, right? But that's not where the hard problems are anymore, right? Because it's been commoditized. No, no, no.

**Dave Jones:** It's trivial, because, yeah, some poor bastard has had to use this half-million-dollar scope to actually develop this. Yeah. And we just go, I'll buy that for five bucks a digi-key. Thank you very much.

**Chris Gammell:** Yeah. And then we'll complain about it, too. Yeah.

**Dave Jones:** Yeah, yeah, of course. We're sorry.

**Chris Gammell:** I'm not sorry. I don't really care. Well, someone on your forum was asking about that, too, right? Of actually working in an IC fab, right? And it's like, that is the new frontier of, you know, like, we've known this. We've talked about this, especially from an analog perspective, right? If you want to get rich in analog, you go work at a fab. I mean, you're not going to get rich, but, you know, if you're a good analog designer, you will get paid well, because it is not easy, right?

**Dave Jones:** No, it's very specialized. Right.

**Chris Gammell:** And then, basically, your output gets sold over and over again, because it's regular and proven.

**Dave Jones:** Yeah. Well, should we talk about this? Because this person, I forget their name because I don't have the page open. Anyway, they have their degree in software, right? They didn't do an EE degree. But their dream job, his dream job, is to become a chip designer, right?

**Chris Gammell:** Yeah, I'd question that. I'd question that if they... I don't know where the dream came from, but...

**Dave Jones:** Well, yeah, I don't know. Well, fine. Okay, he's got a dream. And then, you know, and there's, like, a few people, including myself on the forum, that says, look, I'm sorry, but, you know, it's incredibly difficult. Here's why. And how it's nothing like electronics, you know? Oh, yeah, you do some hobby electronics. You build stuff up on breadboards, and you design boards, and everything's hunky-dory. Yeah, you could be a really... Could be one of the world's best electronics design engineers. Practical electronics design engineers. Doesn't mean that you can become a chip designer. And he's, like, asking, like, oh, what books can I read so I can go to my job interview and, you know, and get a job so that I can pass the job interview for a chip designer. Well, unfortunately, it's orders of magnitude more difficult than reading a few books, designing some boards, and becoming an electronics designer, which you can do, you know? Right, right. It basically comes down to the old thing of, well, if you can bring it, you know, you prove, can you do it? So you bring your stuff along to your job interview. And sure, if you bought your, you know, 20 nanometer chip that you designed along to a job interview, right, that'd probably hire you.

**Chris Gammell:** Dave, if you brought a 20 nanometer chip along to your job interview, they would pay you to teach them how to make 20 nanometer chips, because that's the leading edge technology right now. But anyways, geometries aside, what's a couple nanometers among friends, right? Right.

**Dave Jones:** And, of course, the difference here is that it's cheap and easy for anyone to learn electronics and build stuff and get experience and then get a job if you so desire, you know? But it just doesn't work the same for designing chips. It just doesn't. Right, right. Because the tools are almost, you know, unobtainium. You cannot get them, you know? Or even if you can, it's like, you know, you can't get chips fabbed. You know, you've got to be a millionaire to get, you know, your own chips fabbed. Yes, you can do it for a couple of thousand dollars or something. You know, you can get one of those pool services. But, look, it's just, you know, it's not the same.

**Chris Gammell:** It's not in the realm of hobbyists for sure, right? No, no. Maybe super rich student.

**Dave Jones:** It's not in the affordable realm.

**Chris Gammell:** Yeah.

**Dave Jones:** Maybe, but then you've got the time because you'll have to wait, oh, three months for your chip to come back or something, you know?

**Chris Gammell:** Right, right.

**Dave Jones:** Like, and, well, I goof something up. And as we all know, we've talked about goofing up is the only way to learn, right?

**Chris Gammell:** Yes.

**Dave Jones:** So you've got to goof that up either at your own expense or someone else's expense. And really, oh, so I hate to burst his dream, you know? I hate to burst his bubble.

**Chris Gammell:** I would think, so looking at this from a very far away, right, and just from the information supply, I would tend to guess that he has an interview already with a chip company and his dream job is based on the salary. I don't want to make any assumptions. No, I just made a ton of assumptions.

**Dave Jones:** No, I don't think that's the case. There's no indication of that.

**Chris Gammell:** Okay. Well, anyways, yeah.

**Dave Jones:** I think he just goes, oh, chips are cool. I want to design them. And, well, okay. They are cool.

**Chris Gammell:** But, you know, I had some classmates that went to go work for Intel. And I actually interviewed with Intel, too, and they didn't want me. And rightfully so, right? Because, you know, hearing about it after they came back from co-ops and stuff, I mean, a lot of it, you know, verification and stuff like that, actual, like, digital chip design, man, some of that stuff is like, it's very Verilog heavy. You know, they're moving into system Verilog, system C, a lot of the higher level languages now. And it's, I'll take board levels. I'll take solder smoke any day.

**Dave Jones:** Yeah. And we're just talking the digital domain there, right? We're talking, yeah, okay, maybe you can get in the back door of a chip design company, right? By going, oh, yeah, look, I know some VHDL or I know some Verilog. Oh, look, I know how to do test benches, right? So you might sort of sneak in the back door that way. Kind of, you know, they might be the, they might be the janitors of the chip design world, right? Well, I mean, that's, I mean, Jerry said she worked up like that, right?

**Chris Gammell:** She worked up from mentoring and everything else, but.

**Dave Jones:** Yeah, I use the example of Jerry and how, well, she had developed IP, which was in an FPGA when a game company approached her.

**SPEAKER_01:** Right, yeah.

**Dave Jones:** And then she just went, oh, yeah, I'll design a chip for you, you know? Yeah, you know, she just went and did it. It's not like she sort of, you know, showed her Fabina transistor or something. I don't know if that was pre or post, that sort of thing. And then she went to a chip company and said, look, I could Fab my own transistor. Can I have a job designing chips? You know, it's just not going to happen.

**Chris Gammell:** Yeah, that wasn't the flow. No, it was definitely driven by other stuff. No, no, it was the other way.

**Dave Jones:** And that's what I'm saying. You can actually get in through the back door that way and then work your way up. Once you're in the company, then you can sort of go, you know, and you might write some test benches and then you might get involved in some, you know, Fab testing or something and then blah, blah, blah, and you can maybe work your way up. But otherwise, it's just, you know, it's just not going to happen. And then if you start talking, right, there's that designing a digital chip, for example, where it's all high level. You don't, well, you do care about the process, but it's all about simulation and verification and all that sort of jazz.

**Chris Gammell:** Right, because, yeah, what you said with making a mistake, no, you're not allowed to do that.

**Dave Jones:** Well, you generally, well, it generally is less risk of that, for example, if you're developing a, you know, purely just a digital chip, for example, right? There is less chance of going wrong. But if you think you're going to score a job, you know, that's a totally different world to say working for linear technology or something, developing the latest, you know, ultra low offset op amp. Right. Or something, right? Or, you know, ultra gigahertz bandwidth, you know, amplifier or something. Yeah, yeah, I've talked to you. And with that, analog domain is totally different world.

**Chris Gammell:** Right, if you remember Flying Flux, he was a blogger for a while. And, yeah, so him and I used to talk a lot about his stuff. He designed a lot of analog stuff. And, you know, just hearing about the flow there, because I was relatively naive about it, too. But, you know, it's a lot of physics knowledge and really actually tweaking the tools, too. Because when you think about these chip companies are actually working with, like, a mentor graphics or someone, they have these models that are from the fab, right? And then, so there's all these different layers of abstraction. And knowing, like, the parameters and being able to basically tweak stuff and then test it on the bench then eventually, right? You know, it's like, and simulation, simulation, simulation. So, yeah, once I learned what it really was, it's like, eh, maybe I don't want to do that. But there's no reason to discourage people from it. Obviously, there's a lot of interesting stuff there.

**Dave Jones:** No, no, no, if you want to. No, I highly encourage you to get in through the back door, you know, learn some Verilog or something like that and learn some test benching. And, you know, you can probably get a test bench job somewhere at some company. You know, they're always looking for people, I think, for stuff like that, aren't they?

**Chris Gammell:** So, I don't know.

**Dave Jones:** Well, anyway, no, it wasn't. Didn't we famously say that microchip, was it? No, TI had more jobs advertised for, you know, engineers at TI than all of Australia had for electronics engineering jobs at one point, right? That was just one company in the US, you know? Right, right. I distinctly remember that. They had like 50 or 60 jobs, you know? There's not like 50 or 60 jobs going in this whole country, let alone at one chip company, you know? Yeah. So, yeah, get a job like that. Get a foot in the door and, you know, maybe you can work your way up from janitor to, you know, chip designer.

**Chris Gammell:** I suppose so.

**Dave Jones:** It's possible, but you've got to do it at someone else's expense, you know?

**Chris Gammell:** Right. Yeah, so I guess the original question was how easy is it to get a job? I'd say not that easy. Incredibly difficult. If you have the right pieces of paper and you know the right people and you have the right experience, then easier than if you're starting from a janitor, I think. It rot. But like anything else, I mean, I think the more and more as I'm in the working world, right, I point to people. I don't actually point at them, but my whole mental construct is I'm basically like targeting people and saying, I don't want to be like, I don't want that job. I don't want that job over there either, you know? Like that is a big part of, especially when you're starting out, right? That's a big deal, right? You have to try and figure out do you want the job or not? Because say this person talking about chip design didn't know what it was all about. If you get in there and you do get the job, it's like you don't want to turn around two weeks later and be like, oh, this sucks, you know? Or two years later or 20 years later, right? I mean, like, you know, like you need to quickly try and figure out if you like it or not, even just from talking to people or, you know, interviewing people or however you can do it. Yeah. You know, listening to amp our interviews, listening to me and Dave guess about what the actual situation is.

**Dave Jones:** Even though we have no experience in it. Yeah.

**Chris Gammell:** Don't base your decisions. Don't base life decisions on me and Dave. That is a terrible, terrible idea. Oh, boy. Yeah.

**Dave Jones:** Ah, no. That's it. Come on. Let's just stop before we dig our hole even deeper.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Okay. And so many people's lives are ruined by our horrible advice.

**Chris Gammell:** Speaking of ruining lives, I found out I will not be in New York City next weekend. I will actually be in New York City the weekend of the 20th. And so I'm tentatively planning a meetup in New York City July 19th at a local beverage facility somewhere near the island of Manhattan. Establishment. Either on or around the island of Manhattan. So, yes, if you are in the area, I will have details and further shows and on the website. So keep an eye out. And we can drink beers.

**Dave Jones:** And you're going to fork over your $1,500 for your Google Glass?

**Chris Gammell:** Oh, I already did. Yeah. It's already paid up.

**Dave Jones:** Oh, right. Oh, it's already paid up. Oh.

**Chris Gammell:** That was a tough button to push. Yeah. Oh, yeah. That is the reason I'll be in town. I won't have Glass when the event goes off. I'm getting that on Saturday.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Oh, that's the other thing I was going to mention, too. Sorry. So we did have some people that submitted stories this week. The new thing for T-shirts. I was thinking about T-shirts, right, and wearing a T-shirt to the event and everything. But if people want to potentially win a T-shirt every single week, we have, obviously, the subreddit we talk about. If you submit a story to the subreddit, either a link or an idea that you'd like us to discuss on air, which you can do by submitting a text post. If you do that, among all the people that do it for a week, we will pick one of them and send them a code for a T-shirt. So that is a way to win a T-shirt each and every week. So, yes.

**Dave Jones:** How do we pick one? How do we pick one? Is it random? Yeah.

**Chris Gammell:** It'll be random amongst the people we actually talk about.

**Dave Jones:** You still haven't explained how it's picked.

**Chris Gammell:** Yeah. So this week, we talked about Open Source Hardware Junkies' topic and Russ Ramirez's topic. You're naming people, but who's the winner?

**Dave Jones:** And how do you pick it?

**Chris Gammell:** Oh, that's a good question. I didn't think about that one. We will pick it after the show this week. But we will have a process for it next week. Damn it, Dave. You put me on the spot. That's my job. You know what? This week, we'll just give them to both. How about that? That's easier for this week. Ugh. Yeah. That's a cop-out. So thank you to everyone who submitted stories. We will try and get to more stories next week. Yeah. So submit stories. And it doesn't have to be just be stories, too. That's the other thing I wanted to stress. If you just have something you want us to talk about, submit a text post, and that's the way to do it.

**Dave Jones:** All right. Awesome.

**Chris Gammell:** Cool. We'll see you next week. Bye.

**Chris Gammell:** Bye. This episode was brought to you by NetBurner. NetBurner allows you to get your embedded network solution up and running quickly, so you can get your prototype or your final product out the door faster than any other solution available today. To hear more about the hardware, software, and friendly build environment, and to get a listener discount, go to netburner.com slash the Ampho. administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered
