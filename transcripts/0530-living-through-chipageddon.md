---
episode: 530
title: Living Through Chipageddon
url: https://theamphour.com/530-living-through-chipageddon/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released February 15th, 2021. Episode 530. Living Through Chippageddon.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Live in video, staring at each other again. Well, not live. Live, well, you know.

**Chris Gammell:** We could do live, but we don't do live, yeah.

**Dave Jones:** We're real-time, real-time connected. Using Zencaster Video Beta. Anyway, we won't crap on more about that. There will be...

**Chris Gammell:** Yeah, there's a video Dave did where we tried this out, so you can go and watch that if you want to.

**Dave Jones:** Yes, you can watch that. So we decided, well, this Amp Hour episode, we will record video of as well. So if you want to see our talking heads while we're doing the Amp Hour, it'll be up on the YouTubes, I guess.

**Chris Gammell:** Yeah, you gotta get that Rogan money.

**Dave Jones:** Yeah. So I guess there'll be two versions of this on our YouTube channel, because we do have a YouTube channel, the Amp Hour YouTube channel.

**Chris Gammell:** Yeah, no, that's actually really useful, too. The thing that was nice about that, last week someone was on Twitter and they were deep linking to a point in the Raspberry Pi conversation. They were wondering, like, oh, where was this... I think it was Arturo on Twitter and he was talking about something that some of the Raspberry Pi folks said and then he could just deep link to the actual thing.

**Dave Jones:** Right. I actually forgot my headphones. We were too busy dicking around trying to set this thing up. Hang on, this is quality. This is...

**Chris Gammell:** Yeah, classic. Yeah.

**Dave Jones:** It's already impacted the quality of our show. There we go.

**Chris Gammell:** Yeah, well, you know. A little pebcack right there.

**Dave Jones:** Right. Yeah. It's unbelievable. Anyway. Right. The real Amp Hour, the audio Amp Hour, which is what podcasting's all about, right? If it's video, it's not a podcast anymore, right?

**Chris Gammell:** I don't know. I don't know. I guess we'll hear from our audience if they care. I mean, we'll see who cares about it.

**Dave Jones:** Got it. All right. We have to talk about Chippageddon because it's Chippageddon and it sounds so cool.

**Chris Gammell:** The BBC. The BBC deciding to bestow quite a term on Chippageddon.

**Dave Jones:** Chippageddon. It's great. I just love the term. So, yeah, it's imminent disaster. You know, it's like, yep, bunker down.

**Chris Gammell:** I mean, I've been talking about the last time I, no, not the last time. The first time I brought this up about three, four weeks ago. No, maybe six weeks ago. You're like, oh, there's no problem. People want to hear about parts. And I was like, okay. Did I?

**Dave Jones:** I didn't say that.

**Chris Gammell:** Oh, yeah. No, we have recorded evidence of that. Really? Okay. That's recorded. Damn it. It just keeps getting worse though. I mean, like the things for me are just like TI, TI regulators. For some reason, I just can't, like I, you know, I designed some in and they're like, oh, two, three years ago even. And that's not available. I don't know. It's just, and it's not like these are footprint drop in place, replacements. These are like, you know, super specialized footprints, even though they're not like super fancy parts, they're super specialized. And yeah, I just, I'm stuck with what I've got. I think the last time I looked, it was a June 1st delivery to DigiKey. And so it's not like I'm going to go put in an order at ti.com or something. I'm not buying enough to do that. So I'm just going to design it out. I mean, so TI, if you're listening, this is on you. You're losing tens, tens of chip placements per year. Tens.

**Dave Jones:** They're quaking in their boots. Oh boy. That's right. Yeah. Yeah. Anyway. Yeah. Chipageddon is, so the article just summarizes that, well, look, I'm not going to bother like pulling up the screen recording and everything for the video version of this. Sure. Not many people are going to be watching. You don't want to show the, yeah. You don't, you don't want to show the articles. Anyway.

**Chris Gammell:** Cause then we don't say things that are like on screen and people are like, what are we hearing? Yeah, no, that's fine. So anyway, yeah,

**Dave Jones:** there's apparently like chip shortages in all sorts of industries. And they mentioned the Nvidia graphics card segment, the Nvidia graphics card rollout, the iPhones, Xbox, Playstations, and all sorts of, and automobiles as well. Autos.

**Chris Gammell:** Autos are the ones that I think impact me most directly at least. Yep. And maybe,

**Chris Gammell:** and maybe, maybe you as well. I just like think anything.

**Dave Jones:** Why would it impact you most directly?

**Chris Gammell:** Because industrial and auto kind of like crossover, right? You start to see a lot of things that are like, like qualified for auto processes these days. You know, they'll just be like, oh yeah, we qualify that up to 125 instead of 85. Oh, right. Okay. Yeah. And so it, they do it for convenience, but then it's the same, if it is the same part number, then it's literally like, oh, well, it's either Chris Gammell buying 10s or the Ford F-150.

**Chris Gammell:** God knows how many. A hundred million or something. Yeah. Yeah, exactly. And it's just like, there's just no way I'm going to, I'm going to get that.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Because they're saying here, like cars have over a hundred micros in them.

**Chris Gammell:** Oh, totally.

**Dave Jones:** And that's, you know, it's just, yeah.

**Chris Gammell:** And that's not getting any, that's not getting, that's not going down, you know, maybe, well, maybe they'll integrate more, but I think just like the way that.

**Dave Jones:** No, they're packing so many more gizmos in them, so many more sensors and whatnot, you know, like the door handle needs its own micro, you know, because it needs to detect that. It's like, it's just nuts.

**Chris Gammell:** So I don't know if you listened, but when yours was on the show, you know, he designed the Tesla door handle. So yeah. Oh yes,

**Dave Jones:** that's right. Exactly. Yeah. But I mean, that,

**Chris Gammell:** that alone is like a very complicated, like the model S door handle is like, it's a, it's a little robot, you know, it's like crazy.

**Dave Jones:** Exactly. It's nuts. Cause it, what it pops out or I haven't listened to the episode. It doesn't pop out automatically. It's got like a little,

**Chris Gammell:** on the, on the S it does on the model three, it's a push. So, but it's like that, you know, flush.

**Dave Jones:** Speaking of that, I tweeted last night, there's a video, I think it's on CBS or some, one of those, you know, big mainstream media things. It's the interview with the original founders of Tesla with the two original founders. I saw that. Elon Musk is not one of them. And it's like, yeah. And it's just like two nerdy engineers just being interviewed. It's like, you know, these guys like they're, yeah, they're entrepreneurs. They did like an e-reader startup and stuff like that. But yeah, it's just, you know, they're just more interested in the tech than they are the business side of things. Really? That's right. You know, it's clear.

**Chris Gammell:** So onto the next thing, onto the next problem. Yeah. Yeah. Exactly.

**Dave Jones:** The next fun thing to work on. Yeah, exactly.

**Chris Gammell:** Yeah. I mean, it's a different, different skill set to like go and take it and make it a big thing. It's just, you know, you think about like all these people that are like tech founders or whatever else. It's like, yeah, if you want to get super rich, you're not going to be day to day, like very few people. I know they talk about, you're not going to be the day to day engineer. Yeah.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Like, Oh, Elon like has all these meetings, whatever he's in meetings all day long. He, you know, like he, aside from, you know, I'm sure he's very curious. He's a very curious person, whatever, but like any of the tech people, it's just like from a organizational standpoint, you cannot, you cannot dig in and do the tech stuff. And, uh, I just think it's, it sucks. You know, if you want to do the tech stuff, you got to stay in the, the tech side of things, you know, like individual contributor. I thought about this for consulting too. And like the, you know, people ask me if I can do a job after I've already got a bunch of jobs. And I start to think of it. I'm like, Oh, well I could, I could hire all these people on. I can pull on subcontractors. I can do this, all this stuff. Yeah. And I extrapolate this out and I'm a project manager. Exactly. I can make more money, but that's boring as hell. And I got into this to do more tech stuff. I want to do that. So yeah, it's just, it's not. That's it.

**Dave Jones:** And, and somebody on, um, Twitter or somewhere mentioned to me that one of the founders on there in this, one of the founders of Tesla, he actually does all these old retro, uh, computer, um, compilers and stuff as well. Like the guys like, you know, he goes, Oh yeah, I actually use this, the Tesla's co-founders compiler for this old obsolete processor. You know, it's like,

**Chris Gammell:** we should try and find that guy. Awesome.

**Dave Jones:** Yeah. Yeah. Maybe we can get him on. That'd be great. And yeah, it's the typical story, you know, of people ask me, Oh, why don't I form a big, you know, company? And no, it's like, Jesus, hard enough with one employee, you know, right.

**Chris Gammell:** That's right. He doesn't, he doesn't listen to me anyways. He's on a forum all day long. Uh, Hey Dave, you're a little, uh, you're a little fuzzy on the, uh, the video side of things. I know the video is a huge deal.

**Dave Jones:** Oh no, it's streaming. The local recording will be good.

**Chris Gammell:** Oh, okay. Yep. Interesting. Yes. Yes.

**Dave Jones:** It streams in two 40 P, but it records in seven 20 P. So streaming deliberately gets throttled so that we can be more real time.

**Chris Gammell:** I'm just saying doc Brown looks more focused behind you. So that's why I,

**Dave Jones:** Oh, okay. No, no, I am. Well,

**Chris Gammell:** okay.

**Dave Jones:** Really? No, it's all looking good here. Okay. So assuming, ah, Oh, okay. Right. Cause I'm trying to push the video to one side so that when I edit this,

**Chris Gammell:** that's good now.

**Dave Jones:** That's it. Ah, okay. Right. All right. I'll, I'll push my camera back. All right. I'll figure it out. Oh God. Now I'm going to goof it. Nah, nah, this is not going to, this is not going to make my editing easier at all. All right. I'll just have to butcher it. All right. Not a problem. All right. Chip again. So back to chip again. Chip again.

**Chris Gammell:** I think I mentioned my buddy, my buddy who's a buyer. And you know, I was like, I was asking him about this stuff. You know, he's, he's got in depth, you know, he's actually doing big volumes and all this stuff. He also mentioned in general, like 5g rollout. So they mentioned iPhones, but then on the other side of it too, like towers, you know, like all the tower number is going up like crazy. Right. So it's the, they're still, Oh yeah.

**Dave Jones:** They've got thousands of them in a city, you know?

**Chris Gammell:** Yeah, exactly. And so like, that's another thing. And then just infrastructure around that server side infrastructure. Oh yeah.

**Dave Jones:** No, it's huge. It isn't just the tower with the transmitter. There's a whole bunch of networking infrastructure in a box down below somewhere. That's right.

**Chris Gammell:** Yeah. And so he said, that's definitely one thing. And then, but the real thing is he said it was, okay, uh, let's see, March, April, everything started to fall apart with coronavirus in the States at least. Right. Yeah. So all these companies, they go,

**Speaker ?:** and they're like,

**Chris Gammell:** pull all the orders, shut everything down. This is 2008 again. Red, red alert, red alert, red alert. And they do that. And then two months later, they're like, Oh look, the economy is roaring. And so like, and so they all put their orders back in, you know, and what are you going to do? Go tell Ford or Tesla or Apple, no, you know? And it's just like, so then it just becomes, well, we're just going to take every single thing that's in the supply chain that you can possibly give us. And, and here we are. So, many of us have been complaining on Twitter about this. And I think the best advice I've seen so far is, you know, it's, it's not, I think it was Joseph on Twitter. It's not good enough to just like, see that something's in stock and design it in and then go buy it. If you see something in stock, you buy it, use that, you buy it right then. Like as many as you think you, not, not like overbuying, but like, it's like, you build 10, go buy those 10, you know, it's going to be worth the investment. Or 20, or 50,

**Dave Jones:** or, you know, it depends on their price, you know, like if they're little, you know,

**Chris Gammell:** well,

**Dave Jones:** and that's the thing,

**Chris Gammell:** but then the people overbuy as well. This is, that's also, I think, contributing to it. Like people, you know, these purchasing agents as well, they're, they're scared. They're like, their jobs depend on it. Right. And so it's just like, yeah, it's, so then there's overbuying and it's just, so I think what's going to happen is in, you know, whenever the supply chain actually catches up, I think we're going to see a lot of extra chips because they're just all overbuying, over ordering as well. And so that'll be nice for cheap chips and about, you know, cheapest chips, uh, about the end of the year, probably maybe later, but like until then it's going to be, it's going to be a fight.

**Dave Jones:** So yeah. And it's not just the pandemic. They said it's, you know, it's all sorts of factors that are going into the chip again.

**Chris Gammell:** So chip again.

**Dave Jones:** Yes.

**Chris Gammell:** Wow. But you can get capacitors sometimes. So that's past that one, you know, it's just like, it's just all, yeah, it's just lean manufacturing.

**Dave Jones:** Right. And, uh, Samsung are building a big us fab.

**Chris Gammell:** That's right. This is actually, I think they're, they're looking to expand. This is like the last time they did this was when I got a job. Right. So this is down in, I think they're, they, it says they got a permit for like Arizona and New York, I think, and maybe Texas. I think they're just trying to like, they're just going to like spread it around and try and get like tax breaks from all the different places that already have chip fabs. Yeah.

**Dave Jones:** You'll choose the one that gives you the biggest tax break. Of course. Yeah, exactly. Um,

**Chris Gammell:** Oregon, Oregon's not on there. Right. So Oregon, so like the, the main places in the States are Oregon where Intel's based.

**Chris Gammell:** uh, uh, who's the other, not Hynex. Uh, there was another, there's a memory maker up in Boise and Idaho. And so like Pacific Northwest, there's some chips, factory stuff, Arizona's where like microchip and, uh, more Intel. Uh, there used to be a lot more in California, but now it's all small fabs. And Richardson, and Richardson, Texas is where TI is, but they have been pushing off to TSMC and otherwise, which is another problem in the chip again, side of things. Austin's where Samsung is. Yep. Uh, and then East fish kill and like Albany area. That's where like global foundries and IBM, the exports came from. IBM was really Vermont, but they all, a lot of their employees ended up moving over to, to like upstate New York. So this is the decision making I had to do when I was deciding whether or not to stay in the chip industry. Those are the five places I could live. Right. That's it. Only some of them sounded okay.

**Dave Jones:** And you can't really telecommute in the chip industry unless you have maybe design in the chip or something. Yeah. Then you don't have to live. No, but if you're on the floor, it's like, you know, yeah, the chips have to be made.

**Chris Gammell:** A lot of people I know, they ended up in like upstate New York in like, like pretty much a couple hours from where I grew up. And it's just, it's just like farmland, you know, it's, there's a ton of really, really smart people near the Fingerland. And, uh,

**Dave Jones:** well, is that a problem?

**Chris Gammell:** No, it's just really boring. I mean, it's like,

**Dave Jones:** sounds nice. And it sounds cheap. Yeah. Boring. It's usually cheap. So that's true. Yeah. Yeah. Got it.

**Chris Gammell:** Yeah. So we'll see what they do with that. I mean, like, so like I said, they, this is not the last time they did it. Samsung has definitely expanded since I, uh, I was there in 2006 to 2008. So that's when they built their first, uh, chip fab after they built one in like 99 and then 2009. And then, and then they expanded it over time and they moved into logic side of thing. They started making Apple chips for a while. Yep. And so this new one, it would be a, like a large expansion of that, like high end processor chip side of things. So definitely way more advanced than anything when I was there. So, uh, it's good news, uh, for, for wherever it lands, but it's, uh, I think it's someone, someone said in the comments, even, it's just like, you think it's hard to get chips, try and get the machines to make chips, you know, just like tell and a mat and all the, all of the people that make the actual machines are just, they're very, very complex.

**Dave Jones:** They're hugely complex, hugely complex process. And for those who want to know, um, Samsung have, uh, yeah, South Korea, they've got a USA, Austin, Texas line already.

**Chris Gammell:** That's the one I used to work at.

**Dave Jones:** Yeah. Right. Okay. Yep. And, uh, mostly South Korea, they've got like four in China, but yeah, more, you know, six in South Korea, four in China, one in the US.

**Chris Gammell:** Oh, only six logic fabs. I think. I think they have. Oh, okay.

**Dave Jones:** Well, I'm just looking at the Wikipedia list. Of semiconductor fabs.

**Chris Gammell:** When I was there back in. Oh, six to oh eight, they were building, I think fab 15 or 16, like, and they do double floor. So they, they do. They're like these monster buildings. And then they're, they're stacking them.

**Dave Jones:** Oh, they're stacking them. Wow.

**Chris Gammell:** Oh yeah. That's okay.

**Dave Jones:** Cause that, that makes a much more expensive building. Uh, you know, like it's easy, like easy and cheap to build like a single level, you know, metal roof, but then it's all got to be clean. Right. Yeah. It's not, I mean, it's not going to be cheap. It's, it isn't making, a Tesla car, right? It's not.

**Chris Gammell:** Yeah. Well, yeah, I don't know. Uh, they, uh, they definitely, they, yeah, I think they might save a little bit just in terms of like the, the, uh, the plants, like the power plant and the, you know, the water plant and all that stuff. You know, if you, all of the logistics of having the crazy chemical inputs to a, to a process like that. So.

**Dave Jones:** Oh yeah. No, there's, there's not just machines. Like it isn't just powering. You need all sorts of water and chemicals and, and all of that has to come out as well. And it's all very messy business and they're dangerous stuff too. Aren't they? They're, they're like really ridiculously like, you know, aren't they like, you know, fluoro carbons as well. Aren't they kind of all sorts of nasty chemicals that, yeah.

**Chris Gammell:** Yeah. Like HF is the one that they always talked about.

**Dave Jones:** So like cancerous causing. Yeah. Yeah. Hydrofluoric acid. That's right. Yeah. Nasty. It is.

**Chris Gammell:** It is. You definitely learn your MSDS, your material safety data sheets. So I don't, I don't miss that part of it.

**Dave Jones:** Right. No, messy business, but yeah, it's very interesting though, but whether or not you want to work in there every day, you know, I've, I've worked in factories and it's not, it's, it's not that fun. Like really messy factories. It's not that fun.

**Chris Gammell:** Yeah. I think, I think the, the, the surprising thing is that like, it's really cool when you get into any factory, right? It's like, yeah, the, how it's, how it's made of the world. They're so great. Right. To, to see how things are. And then once you're sitting there for like a couple hours, maybe a day, two days, three days, you're like, Oh, this same thing happened over and over and over and over again.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** And that's how it's supposed to work. It's supposed to be the exact same thing every time. And you're like, Oh man, it is yuck, yuck, yuck, yuck.

**Dave Jones:** And then you need to be Johnny on the spot because if you delayed five minutes getting out there, Oh yeah. That, that, that costs the company X millions of dollars, you know, every, every hour, the machine is down. Yep. So yeah, nasty business. Yeah. No, thanks. I don't really miss that. So anyway,

**Chris Gammell:** yeah, designs, designs where it's at folks. I've,

**Chris Gammell:** I've been on both sides.

**Dave Jones:** Can we talk about key cat? Cause apparently you did a video that I probably should have watched. You just did an Eagle import video. Oh, key cat, Eagle to key cat. Somebody pointed it to me and I just released a video last night, which was trying to import an Eagle file into key cat.

**Chris Gammell:** Oh yeah. What happened with it?

**Dave Jones:** I, it, it didn't go that well.

**Chris Gammell:** Oh no. Okay.

**Dave Jones:** I'm using the latest, you know, 5.1. 19 version. Yeah. 5.1. 5.9. Yep. Which is the latest release. Yeah. Yeah. Dot 19. Yeah. Which is the latest release. And you know, it, it didn't import it, but it gave me some errors and then there's all sorts of, yeah, it's just, it's messy. It's messy. You know, the power planes aren't connected. Oh, this is for the, uh, Trezor, uh, crypto key. I downloaded all their open source hardware stuff and,

**Dave Jones:** yeah, to see if I could import it into, and their Eagle files. So the only thing I had was the Eagle board, board and schematic files in an older version, 7.77, the Eagle, and tried to import it. Yeah. It wasn't that great. And then everyone, you know, a lot of people said, Oh yeah, everyone has issues with it. It's not great. And people have written their own Eagle import scripts because it doesn't work that well. So they had to write their own to solve, you know, some issue they've got and things like that. So that was, was yours easy. I haven't watched your video.

**Chris Gammell:** Is there some trick? The old one was messy, right? It was just whatever, but the, it, a lot of that stuff has been improved in the 5.99, which is the pre-release for the version six. So,

**Dave Jones:** Oh, okay. Right. So I'm simply not using the latest. Well, I'm not, I am using the latest release. Well,

**Speaker ?:** you're using the latest stable.

**Dave Jones:** Yeah, exactly. That's right. Okay.

**Chris Gammell:** And we should be, so it is February. I think FOSDEM is happening or did happen. That was kind of like the target for V6. I don't think they're going to, I don't think they made it. I think we've probably got another month or two. Hence, hence 5.99. Well, they've been like that. So they want to have it so that they can, so that it's very easy to tell. It's not going to be, you wouldn't be able to catch up to that revision, even if you had to rev the, the stable. Many, many, many times. Right. Right. So it's like, you don't want to call it V6 or V6 RC. You basically call it 5.99. And then when you're ready, you tip that over into the, into the V6 thing. So got it. Yeah. So the V6 is nice, but it's, there's still some. Right. Issues.

**Dave Jones:** Okay.

**Chris Gammell:** Yes.

**Dave Jones:** Here's something somebody took me to task over because I complained about that. They didn't put the Gerber files in the Git, in the Git repository. And everyone says, no, no, no, you should never. And I said, oh, there's no PDF schematic in there as either. And there's no, you know, it was just the board. It was just the originals board and schematic file. That was it. No project files, no nothing. And people took me to task saying, no, that is what Git is for. Git, you do not put the compiled stuff into Git. But I thought that's what you've been crapping on about for years. Yeah.

**Chris Gammell:** They're talking about software though.

**Dave Jones:** Yeah. I know they're talking about software. I don't abide by that.

**Chris Gammell:** I don't abide by that. Actually. I think that's a, I think is the wrong. So yeah, I, I keep my source files in Git. I, on GitHub. But then what I do is I, I've started standardizing on an input folder and an output folder. Oh, okay.

**Dave Jones:** Right.

**Chris Gammell:** Because on input, I want to like capture all of my, any step file that I'm bringing in, any kind of graphics I'm bringing in, anything like that. But then at output, it's all manufacturing files. Right. Yep. And the, the tough thing, the reason they say that is they don't want things to get out of sync.

**Dave Jones:** That's what I was going to say. Yeah. It's about sync. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** And there's sync obsessed people. Cause that's what Git solves. Right. It's supposed to solve. And then this hardware business comes along. It just screws everything up. Right. Because we have to make stuff.

**Chris Gammell:** It's kind of like, it's like jury rigging it for the, for the system that's being put in. Right. And, and like, so the, so like if you're releasing a rev a to production, okay, great. You're supposed to like, so basically one way that you could do it is you say you tag at whatever revision is you tag it and you say, and then you could, and the tag is maybe labeled rev a, you know, very simple, all lowercase, whatever. At any point you could then go and say, get checkout rev a, and it'll zoom you back to that point. And you could view the files, whatever. Personally, I do not like that. I, because I mean, I, I still do that. And I like that, but when rev a happens, I put an official schematic in the output folder. And then in rev, so then by the time I get to rev D, which happens quite often, uh, is, uh, I actually have rev a, B C in, in the output folder tag at, at each tag point, because most often I need that reference to go back to, I can't, got it. I can't switch, you know, like I can't have multiple repositories and, you know, side by side compare. I, I want the actual hard file there.

**Dave Jones:** And so what if it's a, what if it, if you just made some changes, but you didn't actually release that schematic, would you still put that in the output folder?

**Chris Gammell:** No, no. I, I want the official one that's because anything that is at the, at the mark, anything that went public manufacturing, well, manufacturing really. Well,

**Dave Jones:** manufacture, but even if, but what if you manufactured a prototype and you didn't, it didn't go anywhere and you only care about the ones that went public, for example, because you're doing 10 internal prototypes.

**Chris Gammell:** You know,

**Dave Jones:** you just doing prototype after prototype, you know, sure,

**Chris Gammell:** sure, sure. I mean, yeah, then I would put all, you know, put, you would, you would put them all in.

**Dave Jones:** Okay. Right. Yeah, I think so.

**Chris Gammell:** All right. Would you, I mean, how would you do this?

**Dave Jones:** Oh, yeah. Well, no, I've, I've done both. I'm guilty of doing both. I don't think there's a right answer here. It depends. No, no, there is no right answer, but you know, yeah, I got taken to task by the Git purists because they said it's, you know. Yeah. I mean, that's the thing there.

**Chris Gammell:** They're talking about it from a software perspective, right? Yeah, yeah, exactly. I get it. Like they don't like binaries. No, I don't like binaries either. You know, they say, oh, you should build from source. You should have this, whatever. Yep. I don't always build. And they're like talking about like, like automation and what they called like continuous integration type stuff. And it's like, you always should always build the latest or build it from source at a certain time. Yep. No, I just, I don't agree with that. I know.

**Dave Jones:** I know.

**Chris Gammell:** I would love to hear arguments against it, but just saying, don't do it. It's not a good enough argument for me.

**Dave Jones:** Well, this, uh, Trezor thing, right. Is probably a classic example, right? They've got, for the older version, they've got more stuff. I was working on the newer model Trezor, but for the older one, they included the bomb and they included PDF schematics. They included all sorts of stuff. And I looked in the firmware folder for it. And it's like, I, at a glance, it may be there, but at a glance, I couldn't just find the, uh, binary to program the chip. Right. So like, like, am I expected to recompile it from source? Like, you know, I just want the, you know, I, I, because I'm, I'm making this, I'm duplicating it. So all I care, I don't care about the source. That's, that's their job to handle, right? Or it's the community's job to handle all I want. I'm just making the widget. So I don't, you know, all I care about is the binary to program the chip. That's it. That literally is all I care about.

**Chris Gammell:** So sometimes it exists in the releases folder, right? So there's, when you do an actual release, when you tag something, it will do a release, but there should be a binary at that point. Like there should be somewhere.

**Dave Jones:** It's gotta be somewhere. Yeah. But it may not be in the source. Yes. It could be in some, some release subdirectory somewhere. That I haven't found.

**Chris Gammell:** Well, and so, so KaiCad still doesn't have a way to, to script to like the, the API is catching up in terms of like scripting. So there's a talk by Jesse Vincent, who has been on a show during one of the travel shows I did, but Jesse runs keyboardio. And he did a talk at KaiCon about, about basically this whole idea of like scripting, scripting it out so that when you tag, so that you say, Hey, this is Reve, you hit go and it goes and it zooms off and it generates your Gerbers and your bomb and your, and I think Altium does this sort of thing, right? And it generates basically a manufacturing package. Yep. Yeah. And so like basically that kind of idea and I like it a lot. It's just, you know, if it's not built in right now, I'm not, I'm not really capable of doing it. Yeah.

**Dave Jones:** Got it. All right. So yeah, get, please leave it in the comments down below if you, uh, what you do. Yeah. Yeah. Yeah. That'd be great to know. I mean,

**Chris Gammell:** like that's the thing that does. Yeah.

**Dave Jones:** I have no problem with it not being in the actual source subdirectory. That's fine. I'm, I'm fully on board with that, but yeah, there should be like an output folder somewhere.

**Chris Gammell:** Yeah.

**Dave Jones:** But there's not. So, you know, anyway, as a, yeah, I can't push my stuff back into somebody else's git. Can I, I've got to do a pull request.

**Chris Gammell:** Yeah. So the way you do it is you would fork the repository, right? So, so if Trezor has this open source thing, you fork it and then it basically creates a copy in, your GitHub account. Yep. It's the exact same. Basically it tags it at, not tags it, but it basically grabs it at the exact time that you did that fork. Yeah. You go and make your changes to it. And then you say, you push the change back to Trezor and you say, Hey, here's the changes I made. Do you want to include these in your repository? And they say, yeah, sure. Why not?

**Dave Jones:** Right.

**Chris Gammell:** That's like,

**Dave Jones:** so that, that may not be changing the source at all. That may just be adding an output subdirectory because they, they haven't done it. So someone like me could come along, fork it, do an output subdirectory and then put all the files in there and then do a pull request for them to pull it back in. Right. See, I'm, I'm totally with it now. I'm totally with this git thing. I'm, I'm learning.

**Chris Gammell:** Yeah, it is, it is a bit of a shift, especially if you're coming, like, cause the Altium stuff's also version. And so.

**Dave Jones:** Yep. Yeah. That's what I'm used to when I worked at Altium, we were using subversion. Yeah. Yeah. I assume they're still using it for their own source code and stuff. I think they are. Yeah. A lot of, a lot of people do still.

**Chris Gammell:** So, right. It's kind of more, it is more like kind of zip up the whole idea. Right. So, which is problematic when there are binaries. And, and really, I think this is where ASCII based type stuff like, like Ike does and Eagle does. It's nice. Cause you can actually see changes.

**Dave Jones:** Yeah.

**Chris Gammell:** And, you know, and being able to view stuff as well. Right. So like, I think that's an argument against, so if you are using like a propriety, so say you have to use Altium for this thing, then I think it actually does make sense to have Gerbers and all the other stuff there, just because even though there's viewers out there, it's just hard to get to that data. I think, you know, it's just, if you have a PCB doc or a CH doc or whatever the thing is, it's tough to get to.

**Dave Jones:** Well, I think regardless of what package you use, you should be, you know, if you're going to do an open source thing, I guess, you know, there should be like an output folder just to make it easy for people. But, you know, you don't have to. And if you don't want to, because you just don't want to, that's fine. You know? Yeah. There's nothing wrong with that. So.

**Chris Gammell:** Yeah. I try and, I think the thing that I've been figuring out for myself is just like, uh, being kind to myself, my future self. Right. That's like, right. Yeah, exactly. It's just like, Oh yeah, I, I, I've opened up some projects recently. I'm just like, what the hell was I thinking here? You know?

**Dave Jones:** Yeah. They're a mess. Yeah. Yeah. Yeah. I know. Uh,

**Chris Gammell:** all right. What else got on the list today? Well, speaking of great advice that I give myself, I am signing up to give other people advice. So I am, uh, starting a new course called, uh, hang your technical shingle and introduction to consulting. So this is a new, uh, hang your tech, what? Hang your technical shingle. What does that mean? Like hang your shingle. You know, you've ever heard that before? No. A shingle is a roof tile, isn't it? That's right. Or it's, it's like, it's kind of like the thing that's like, uh, like an old, uh, blacksmith shop, you know, it'd be like hanging outside, like the, the sign. Oh, okay. Yeah. Yeah.

**Dave Jones:** Got it. Okay. They call it a shingle sometimes too. So you hang your shingle.

**Chris Gammell:** Basically it's a, it's a colloquialism for going out on your own for business. So hang your technical shingle would be, you want to go become a consultant. I've been making videos now for a couple of weeks. Uh, basically I have a course, all the things I wish I would have known before I got started consulting. And so, uh, let me tell you, Dave, it's about five pages of just outline. Uh, so, uh, yeah. So we're gonna go through and we're going to, you know, so if people are interested in becoming a consultant, a technical consultant specifically, not like a management consultant for like McKinsey or, you know, accounting consultant or anything like that. Uh,

**Dave Jones:** this is like a design consultancy.

**Chris Gammell:** A design consultancy. Exactly. Yeah.

**Dave Jones:** Or whatever skill you happen to have.

**Chris Gammell:** Exactly. And so it's good for software people. It's good for hardware people. It's good for mechanical people. I wouldn't say it's good for someone who's like a creative, you know, like a graphics designer, but maybe, I don't know, but definitely not like a management.

**Dave Jones:** The advice can be greatly different between software and hardware though.

**Chris Gammell:** Is that something that you touch on? Yeah. But not when you're talking about like how to do marketing and how to do, how to do accounting.

**Dave Jones:** Oh, okay. No, no, they're, they're fairly universal, but how to do legal stuff,

**Chris Gammell:** you know, like all that stuff. Right. So,

**Dave Jones:** and it'll be country specific too. Cause there's like, um, you know, tax and thing. Do you get into that sort of stuff? Well, I mean, we talk about it broadly. Tax and finance side of things.

**Chris Gammell:** And the big piece of advice is, is hiring someone. That's pretty much what it starts with. This is like, Oh, you should hire someone, but accounting methods like gap, like GAP, like that stuff is the same everywhere. So like bookkeeping and similar things. So this is basically,

**Dave Jones:** it's not the same here. I bet you our laws and tax rules and everything. It'd be different to the U S let's,

**Chris Gammell:** let's find out right now. Let's see if Australia uses gap. Nope.

**Dave Jones:** I've never heard of gap.

**Chris Gammell:** Well, you're not an accountant though.

**Dave Jones:** Well, no, I'm not. Okay. Fair enough.

**Chris Gammell:** Generally accepted accounting principles, the Australian equivalent to IFRS. So,

**Dave Jones:** Oh, okay. Right. Yes.

**Chris Gammell:** Do you know what that is or no?

**Dave Jones:** I've heard of it. I don't.

**Chris Gammell:** Okay. All right.

**Dave Jones:** So that's why I pay like five, six grand a year to my accountant. Like I pay a shitload of money to my accountant. Who handles all my business stuff, handles all my personal tax returns and everything, you know, it's like, yeah.

**Chris Gammell:** So I think there definitely are going to be country differences, especially on the money side of things and taxes and stuff in corporations for sure. But you know, marketing's the same mindset's the same stuff like that. So, yeah. So we're, I've got a beta program going like I did for contextual electronics back in 2014 now. Oh my God. It's been a long time. Jeez. Yeah. So it is going to be a paid beta. So that's important to state upfront. Oh yes. Yes.

**Dave Jones:** It's not free. No. Yeah.

**Chris Gammell:** Just because as I say in the intro video, like I had 50 people sign up for the, actually I had like 150 people sign up for the first contextual electronics beta. And I, I said yes to 50 and about five showed up the first day.

**Dave Jones:** Right. Yep. Was, was that one paid at the time or was that one free?

**Chris Gammell:** That was all free. Yeah.

**Dave Jones:** Oh, so. Okay. I was going to say paid you to get a higher percentage showing up because they've,

**Chris Gammell:** I think so. Yeah. I mean, it's not going to be a lot, it's going to be much reduced from what it is normally. And there's like a coaching component. So we're all going to talk and like, have like group calls and stuff like that too. And just kind of talk through the consulting side of things. Obviously I've been talking about consulting a lot on here. Yep. I mean, I love it. I really do. I think it's, it's terrifying sometimes, especially at the beginning, it was very terrifying, but I love the problems I get to work on and like the amount of control I get. And just, you know, like I'm the only electronics person in the room. Most of the time, like that's cool. That's like, it's great.

**Dave Jones:** What people need to remember with the consulting gig is that you're still working for someone. That's right. Yeah. Like you, you, you aren't your own boss. You,

**Chris Gammell:** you, like you have, you have actually like four or five bosses. You have,

**Dave Jones:** you have four or five bosses. Yeah, exactly. They're called clients and yeah, that's right. And they'll make you do ridiculous, stupid stuff that you can't argue against, you know, because they're paying you to do this ridiculous stuff. Well, no, you can though. I think that's the thing. Well, you can, you can try in a nice sort of way, but at the end of the day, they're the ones who decide which way to go. And if you think that that's a dumb idea, this is not going to work.

**Chris Gammell:** Right. Right. They're like saying, we're going to put this, make this a battery product. And we want it to also, you know, be a kilowatt of energy. It's just like, okay, cool. I guess, you know, yeah, you're right. At the end of the day, you make your case and, and that's the best you can do. But I think that's actually important thing as well as like building your marketing enough so that you can, pick the right clients. Like finding the right clients is like a key to happiness. If you just take any job that comes around, oh, it's, yeah. And you know, everybody starts like that, right?

**Dave Jones:** That's not really marketing though. No,

**Chris Gammell:** no, no, no. Marketing is having enough coming in the door so that you can be choosing.

**Dave Jones:** Oh, okay. Right. Okay. Yeah. Yeah. Because I was going to say for, for a consultancy marketing, like what people think of for, as when you say the word marketing, that's just an absolute waste of money. Paying to like advertise your consultancy on, on Google AdWords or something. It's just, you might as well flush your money down the toilet.

**Chris Gammell:** I can't even imagine how expensive that would be. Yeah. Exactly. No, just,

**Dave Jones:** just flush your money straight down the toilet. Yeah. I agree.

**Chris Gammell:** And that's not going to be like, I think that's another thing too, is just like finding people, you know, having people find you is a lot different than you finding people. Right. So I would put the, the Google search terms in like you finding people, but you're going to find everyone, you know, you're just going to find like the people who are like, I need an inventor, you know? Yeah. Oh my God. I couldn't run fast enough in the other direction. If someone said, I need an inventor. Oh yeah.

**Dave Jones:** No, that's just, no, that's an instant refuse.

**Chris Gammell:** Right. They're like up late night. They're like, they see that commercial. You guys don't have the commercial there, but there's like this one commercial here where it's about like, are you an inventor? And then it's like this caveman, like hitting a rock into like a, like a wheel. Oh yeah. Classic, classic commercial here. And like, you know, they're scamming those people. Oh yeah. Yeah.

**Dave Jones:** Don't even do the classic over quoting thing either. Like, yeah, if you don't want the job, don't quote five times more. Just simply say, no, sorry, not interested.

**Chris Gammell:** No bid. Yeah. That's good advice. Yeah.

**Dave Jones:** Just don't do it. It's like, you know, like I was offered, uh, I sure I've told the story. I was offered like 20 or 25 grand or something and a trip to Canada. If I would come out and verify this guy's energy device. And you know what I'm talking about when I say energy, right? It's like, Oh, it's not free energy. No, no, no, no. Trust me. It's like, it's like, it's like,

**Dave Jones:** it's like,

**Dave Jones:** it's like, it's like 25, like us. That's not what I would have put in the,

**Chris Gammell:** in the, uh, the category of consulting.

**Dave Jones:** Yeah. But,

**Chris Gammell:** but I guess it is a consulting job.

**Dave Jones:** He, yeah. Wanted me to come out and verify. And it's,

**Dave Jones:** it's simply no, no amount of money is worth working on that. Yeah. You know, it's just, no, no, go away.

**Chris Gammell:** Yeah. So if people are interested in the beta, there's an application. There's a, I made a bunch of videos, like the introductory videos for each section, kind of just talking through what we'll be talking about there. All the usual stuff there. I try not to promote contextual electronics too much on here.

**Dave Jones:** Aha. I've got your course content list. Yeah. Sorry. Yeah.

**Chris Gammell:** Yeah. Yeah. So it's just, uh, you know, people can go and check that out. It's got some really content. And we're going to figure it all out. And yeah, the reason I have beta people, I, you know, the videos I'm kind of working through, that's fine. I was going to make my stuff anyways, but it's also like, what do people need to know? Right. So like the people that are worried about getting started, I have my own fears and yeah, that stuff's still fresh in my mind. Yeah.

**Dave Jones:** And here is the course content introduction to the consulting course, money handling money's right up front because you don't have money. You're out of business.

**Chris Gammell:** Yeah. I mean like there's a whole, there's a whole section on accounting, but also like cashflow, man, like cashflow too, right? We talk about that. Oh yeah,

**Dave Jones:** we, we did. I, I simply ran my business ran out of cash at one point, you know, I was sitting pretty literally one week. I'll sit in pretty. Then the next week I went, I'm, I'm out of cash. I'm like, you know, I'm simply out of cash. Like I, I, I didn't have to do that. Like, but it was just, yeah. Oh, like, cause I didn't manage my,

**Chris Gammell:** right.

**Dave Jones:** And it's yeah. And it's just like all these purchase orders came that I'd promised months and months ago. Cause there's a big lead time, you know, so I promised to buy all this equipment from multiple, uh, menu, all this, um, stock from multiple manufacturers. And it all sort of just hit at once and bam, you know, all my cash vanished. Like, and I had to stop paying myself wages. Like, yeah, you know, it was, yeah. Just so I could buy the stock. And, uh, so anyway, money handling next marketing for legal and administration grown, uh, five client relationship management. Once again, grown, you know, it says all this stuff has grown already. It's like time management, grown professionalism. Oh, okay. You know, it's like, she'll be right. No worries. Um, and right. There's resourcefulness and nine is mindset. Where's the engineering, Chris, where's the engineering.

**Chris Gammell:** That's the rest of contextual electronics, Dave.

**Dave Jones:** Right. That's a different course.

**Chris Gammell:** That is. Seriously. Yeah. I know it's yeah, this is, this is like the end of contextual electronics, right? This is basically, you've already learned all the other stuff, like it's actually electronics. You know how to build stuff. You build stuff on your own. You want to go out on your own. Yeah. That's, this is all the stuff that you've grown at. And you're like, Oh, I never thought I'd need to know this stuff.

**Dave Jones:** And, and that is the point. Like, you know, everyone, as someone who's doing this, we'll already have the technical skills. Right. So there's no, you know, right.

**Chris Gammell:** I wouldn't expect someone to, to start tomorrow and be like, Oh, well, you know, I'm figuring out what resistors are and I'm going to go off for my services. No, man, like 10 years though. And you've got like, you know, like you've got a Greg Davil level of portfolio stuff and you're ready to go offer your, you know, to hang your shingle. Yeah. Like that you are the person then, you know, but, but the big thing is like, so we've talked about on here, like how would you go? So say you've got a huge portfolio and then you go and turn around and, uh, you go and try and get a job at like a, you know, big company. It's like, you're going to get, you're going to get stopped by HR every single time, you know, just because you don't have the degree or the right degree or the experience.

**Dave Jones:** Or you don't have the experience at a big company. So, you know, yeah. Yep.

**Chris Gammell:** So,

**Dave Jones:** yeah. So yes, they're, they're, they're supposed to be grown worthy. Professionalism, money handling. Right. I'm going to,

**Chris Gammell:** I'm going to put, put Dave as my testimonial. Grown worthy, Dave Jones. Grown worthy.

**Dave Jones:** Oh, boy. Yeah. Well, I hope that works well. Well done. Yeah. Yes. That is. Yes. Yeah. Yeah. I think the other thing too,

**Chris Gammell:** is just like, you know, building community around it too. Like, it's just, yeah. Right. Well,

**Dave Jones:** you've already got that with the, cause you've got the, um, the forum, don't you? You've got the consultants consulting forum. Yeah.

**Chris Gammell:** This is going to be separate from, this is going to be like a subsection of that, even just because it's going to be like, as people are getting started, but yeah, there's also the consulting forum and things like that. So is that consulting forum?

**Dave Jones:** Is that like an invite only thing? Yeah. There's an application. I'll put, Oh, okay. There's an application. You can't just write, join it. Yeah. You've got to. Okay. Yep. Got it. What's it? What is the threshold? You've got to show us your stuff. Is that the threshold?

**Chris Gammell:** Sure. Your consulting site pretty much. I mean like, yeah. Oh, okay.

**Dave Jones:** Right. But what if they don't have one? What if they've just getting into there and they want to, they don't have a consulting site. They just have their projects.

**Chris Gammell:** That's okay too. Like just a link to that. Just basically to show you're legit enough, you know,

**Dave Jones:** got it.

**Chris Gammell:** It's a real soft, it's a real soft, you know, gateway.

**Dave Jones:** So actually after this, after this, I'm probably going to shoot a, I'll probably go outside and shoot it. Cause I'm, you know, sick of being in my windowless office here. Somebody emailed me. It was a, just finishing his degree. I think he's part, what three, you know, year three or something of his degree or something like that. And he's, he's worried. How does he stand out? Right. You know, the usual thing, right. How do, how can I, you know, what, what can I do to stand out? And then I chuckled because in his email, he said, Oh, here's my YouTube channel with my videos I've done on. I'm really passionate about audio, you know, electronics. And he's done this whole suite of done, done. You already stand out to 99 more than 99.9, 99% of other graduates. It's yeah. It's, it's done. I just had to chuckle and it was,

**Chris Gammell:** I was reviewing a resume recently and, and it was the same thing where like, he's like, you know, it's got the usual like experience, some good experience up front and, you know, some of his classwork and stuff like that. I got to the bottom. I'm just like, where are all your projects? Like, he's like, Oh, I don't think I should put those on. I'm like, no, you should definitely, definitely put those on there. And, and links, links to your website, where they are focused, you know,

**Dave Jones:** like don't just say, and don't, don't just use the words. Like, you know, you can often include photos in your resume. It's fine to include like, you know, we, we, we always recommend, I'm sure both of us will recommend keeping your resume to like one or two sheets tops, right? Maybe, maybe, especially if you're young.

**Chris Gammell:** I'd say one, if you're, one, if you're young.

**Dave Jones:** Oh yeah. Well, no, even if you're young, well, when you get older, you find you don't actually need a resume really, you know, because you're finding jobs in other ways. Yeah. But yeah, like, like two sheets tops, but it's okay if you include a whole bunch of photos, because trust me, when you've got a hundred resumes and you're flicking through them like this and you're going, Oh yeah. Like you'll read the summary at the top and then you'll probably, you know, like your eyes are glazing over because there's your hundred resume. And then you're just, Oh, I look like, Oh, this is thick. And you see all the photos and you're, Holy shit. It's something different. So you're going to be looking at the photos, you know, cause it's visually stimulating and you're just going to remember that person. You're probably almost certainly going to get an interview. Like,

**Chris Gammell:** yeah, I think, I think it's tough when I think a lot of the traditional advice to like, if you go to like a career services office and things like that, they're going to be like, here's how you fit into this box that IBM asked for, or this, you know, Apple or even Apple, you know, in a best case scenario, Tesla and Apple recruit here and here's what they want. It's like, they're going to tell you how to do that thing. And it's like, yeah, you are probably going to stand out through an HR individual at these big companies. But if you're going outside of that, or even if you want to give it a shot, you know, like put a couple of photos in there, you know, I think that's great. Like, you know, still work within the rules, but bend them a bit, you know?

**Dave Jones:** Right. Right. Because even companies like famously, like Tesla, that, you know, don't like from the top of down, they like, it's fine. If you're not qualified, we don't care. What can you do? You know, are you innovative? That kind of thing. But even those companies, you still have to get through HR. Right. So you've got to have whatever they're looking for. So, you know, you have to give them that. Otherwise they, you know,

**Chris Gammell:** I think, I think Dave's frame is really right though, too, is just think, think about it. Try and empathize with what the, the person, the engineer reading your resume. Like, yeah, you still have to get, you know, you have to check enough boxes to get past HR. Okay, fine. But once you do, then what? Like who, who are you? Yeah. Yep. You're in a stack of paper. How do you make it compelling enough? Right. And as much as I think, you know, a, a career services person telling you that your job at Dairy Queen is going to, you know, show that you were a good worker and all these other, it's just, eh, you know, like if you have to choose between putting another project line on your resume and your Dairy Queen experience, put the project line, you know, like exactly. Yeah. And if you haven't done stuff yet, go start today, you know, like, yes. And document, document as you go, you know?

**Dave Jones:** Yep. Yep. Just do what I do in my video last night, go pull a project out of GitHub and modify it. Do something like that. You know, you don't even have to start from scratch. Just, you know, take an existing project, modify it, do something nice with it. You know? Yeah.

**Chris Gammell:** I think as long as you're like upfront about it, right? I remember the first time.

**Dave Jones:** it's like, yeah, it's like, you know, it's not like, oh yeah, I, I designed this Raspberry Pi, right? It's like, you know?

**Chris Gammell:** Right, right. It's not designed Trezor wallet. It's a modified community version of Trezor wallet. Yes.

**Dave Jones:** Yes, exactly. You, yeah, you've got to do something substantial to it. You know, you can't just take it out and build it. You've got to, you know, substantially give back. And then, you know, but that's just one thing. And then you get experience doing that. And then maybe your own projects and things like that. And start putting it on there. But even that's valuable. Even that you'll stand out above, you know, 90% of other applicants. Yeah.

**Chris Gammell:** So now if you can put some PCB renders and animations on your resume, some, I guess you wouldn't put animations, but if you could put the renders,

**Dave Jones:** Oh, they're schmick. Oh yeah. Oh, these are sexy. What is this? Yeah. We've got a link. Yeah. Where's the, where's the link? Oh, I also want to put it in here. Spectacular PCB renders and animations. Who's it done by? It's done by Shotkey on the EV blog forum, published these on the EV blog forum. And yeah, they're just, wow. Wow. Wow. Wow. Wow. Wow. Oh, I could go screen.

**Chris Gammell:** It, it looks like a bunch of, I mean, it's a bunch of like power, power handling type stuff. It's got huge inductors and looks like, yeah. Power convert boards.

**Dave Jones:** Big screw terminals. And yeah. And it's just, Oh my goodness. It's like, you can tell it's like a render, a Photoshop render, but it just looks so gorgeous. You don't care. Like, and he's got like oscilloscope probes and.

**Chris Gammell:** Yeah. It almost looks like kind of like steampunky kind of, it's got like the dark, you know, yeah. Yeah. Yeah. The dark shadows and stuff.

**Dave Jones:** Exactly. Big in like the industrially type, you know, set in shadows. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** It's like, it's done in some dingy warehouse somewhere, you know?

**Chris Gammell:** Yeah. It's amazing. The, the rendering stuff that happens these days, right? I mean,

**Dave Jones:** it's just insane. I'm my mind's blown. It's just nuts. And he's got video as well, but warning, it is vertical video.

**Dave Jones:** the pictures are better than the video, although I haven't watched them all, but yeah, just absolutely. So that's off to shot key on the EV blog forum. Just, Oh no, here's one. This one's not vertical video. Oh yeah. Okay. Oh, Oh,

**Chris Gammell:** I can't see what you're seeing. If you're trying to show it.

**Dave Jones:** I get, look. All right. Hang on. I will. There you go. I will go like this and I'll go like this and I'll go like, Oh, he's not doing it. Rossman just popped up. Lewis Rossman just popped up. Hang on. Here we go. Here we go. Here it is. You can see it now.

**Chris Gammell:** Oh yeah.

**Dave Jones:** Yeah. There you go. It's like, wait, hang on. They'll do the exploded thing. Here it comes. You've got to watch the video version of this. Oh, look at that.

**Chris Gammell:** That's cool.

**Dave Jones:** That's just that. Yeah. That's just nuts. That reminds me of our branch electronics. I forget his name. Branch electronics, YouTube channel. Check that out. If you want super high quality, like just mind blowing, you know, tear, tear down photos. It's just, you know, like animation. It's just insane. Absolutely insane. And he,

**Speaker ?:** he,

**Dave Jones:** he contacted me and he said, yeah, like he spends like, like 50 or a hundred hours actually producing each video. It's just like, you know, he, he actually tears down. He's got a process for, he actually tears down the products and he photographs them. And he, and then, you know, and then adds renders on top and does all sorts of, you know, stuff to it. And it's just absolutely incredible renders. He's got. So yeah. Branch electronics, just insane. I don't like his voiceover. He's, he's paying someone to do the voiceover, I think. And I don't like the voiceover, but apart from that, yeah, it's,

**Chris Gammell:** you should offer to do it for free, Dave. You should.

**Dave Jones:** No, I'm even worse on the voiceover services. Nope.

**Chris Gammell:** Yeah. I mean, this is, I mean, this, this is really cool. Like the rendering stuff. I feel like at a certain point, it loses efficacy in terms of like, I think it's really great for product shots for someone again, to sell to your clients, you know, that kind of thing.

**Dave Jones:** Like staffing kickstarters and stuff. Yeah. Yeah.

**Chris Gammell:** Yeah. But some people go really far. Like I've seen a lot of stuff with blender and, and KaiCad recently too. And like,

**Dave Jones:** yeah,

**Chris Gammell:** it's really cool. I just, I haven't found a need for it past, like, you know, like there's like built-in rendering. Yeah. No, I just,

**Dave Jones:** I'm happy with a 20 year old, you know, now probably how long's 3d renders on PCB been around? Altium were the first to do it. I think.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** Jeez. That would have to be 20 years ago now.

**Chris Gammell:** Yeah.

**Dave Jones:** I think. Yeah. And like, I'm, I'm just happy with the basic. I'm just happy to get something. I'm just happy to get something that shows my solder mask expansion and my, you know, silk screen and stuff.

**Chris Gammell:** If it's functional and yeah. And it just shows if you're like, if you're stepping on your own components or something like that. I think that that's really where it's value, value comes in for me, but there are, I mean, first off, I think it definitely grabs the eye, right? So if you're scrolling on your Twitter feed or similar, it's like, Oh man, that's going to pop out every time. So you're trying to get attention for something. I think it does make a lot of sense.

**Dave Jones:** It does the job really well. So yeah, I don't know what software he uses. Does he say what software he uses there? It were created in blender. Yep. Of course they were.

**Chris Gammell:** Yep. Blender. Yeah. Yeah.

**Dave Jones:** So, yeah, it's, it's just, it's incredible. It's mind blowing. I don't understand how they can do this.

**Chris Gammell:** And blender's free as well. I think. So that's pretty easy. Yeah.

**Dave Jones:** I think it is. Yep. Yeah. Yeah. But apparently, yeah, there's an art to it. Like it's not something that, you know, idiots like us can just go into and expect to produce really high quality stuff like this. There's massive learning curves and, yep. And, and even then, like some, you know, really good blenderers can't do some stuff that other exceptional blenderers can do. You know, there's like, yeah, it's its own skillset, right? It's that powerful. It's yeah. You, you develop your own methods and stuff to do it. And it's just, yeah, that's just crazy. That's great.

**Chris Gammell:** You should offer that as a service. That would be great. I would, I would definitely feel like there's a niche.

**Dave Jones:** There is a niche. Yes. Right. There is a, it's like glamour shots for electronics, you know, right there. Right. So someone should take Chris's course.

**Chris Gammell:** Sorry. Did you have, did you have glamour shots? Like, was that everything there?

**Dave Jones:** Glamour shots? What's glamour shots? No,

**Chris Gammell:** it was like the eighties and nineties. Look up, look up. Glamour shots. Oh,

**Dave Jones:** right. The, it was like, right. The rock posing with the posing with the. Yeah. Well, no, so like,

**Chris Gammell:** it was like a service that you used to hire in like the eighties and nineties. It was like, you know, like feathered hair and like, everything was like soft, like super soft lighting. And it was just like, and they'd like add sparkles and stuff like, so like you'd have these shots that like, and like, it looked like they had like a fog machine or something too. It was, there is some fantastic old glamour shots, but like, for me, it's just like this, I use it now as a terminology just for like, uh, you know, like way overdone kind of thing. So.

**Dave Jones:** Yeah. Yeah. Okay. I'm saying have, have you seen the rocks famous one?

**Chris Gammell:** I've seen, I've seen that one. Yeah. Yeah.

**Dave Jones:** Yeah. Okay. Yeah. It's just great. It's just classic nineties. It's just, I think it's nineties. Yeah. I think it, yeah, it must be nineties. I thought it was like, wait, I never did that. No, I, there's very few photos of me like pre, pre mid two thousands. Like there's just, yeah. Ever since digital cameras came along, it'd have to be mid two thousands. No, there's very little, very few photos of me. There's probably one or two photos of me as a teenager. Like there's very few, it just wasn't a thing. It just wasn't, you know, it wasn't, it wasn't a thing in our family. We just didn't take, you know.

**Chris Gammell:** Yeah. I mean, these days there's photos everywhere. Oh, no.

**Dave Jones:** Yeah, yeah, exactly. Everyone's photo obsessed with their phones, but geez. And I know it was like in searching for this,

**Chris Gammell:** I see that there is in 2019, there was still five glamor shot locations available. So amazing. So you could still get them done.

**Dave Jones:** Anyway, getting back to, yeah, somebody should seriously, there is a niche for that. Take Chris's course. And I would recommend this to a shot key here on the V blog forum. Actually. Yeah. Take your course and do a set up a consulting business for doing shots like this. Seriously. Like, you know, I mean, but if it takes like 30 hours, every electronics forum and sorry,

**Chris Gammell:** even if, if it's 30 hours to do this sort of thing, and even if you're charging 50 bucks an hour, that's a $1,500 photo. So that's, that's pretty, yeah, that's pretty pricey. I'm not sure I would pay that personally. Like I would pay for a service. Oh no,

**Dave Jones:** but if you're doing a Kickstarter, you would like, if you're doing a Kickstarter and you don't have the skills yourself,

**Chris Gammell:** you know,

**Dave Jones:** I would, because one shot sells it. That's yeah. One shot will sell it. Like, you know, yep.

**Chris Gammell:** Yeah. You were doing some photography stuff recently, right? You were doing some light box. Yes.

**Dave Jones:** I did a do it yourself. A light box. Yes. For, for PCB photography. I've wanted to do it for, you know, years. Cause I always, every time I want to do like a, like a decent shot, I've got to cobble something together. Like I can just use my regular overhead, you know, ceiling lights and then just point, you know, camera on a tripod and get it at the right angle and, you know, and take it. But it's not, you know, it's not the best that it could be. Right.

**Chris Gammell:** Yeah. I feel like just reflections off of things. And yeah.

**Dave Jones:** Oh yeah. It's just, it's just not good. So, you know, so often if I want to go to a bit more trouble, I've got to set up my studio lights, you know, like I'll lean them over and I'll set up the right angle tripod camera attachments. I was pointing down and there's light evenly lit around the size, but I've never had a dedicated solution for that. Yeah. We were in doing the live show the other week with a big Clive and others, Martin Lawton among others. Was that posted somewhere or no? Yeah. Yeah. It's on my second channel. It's on my second channel. It's a two hour live show. Okay. Of like, you know, half a dozen of us. And yeah. And he showed off his do it yourself light box solution, which I censored out cause he, you know, it was kind of secret. So I didn't know he was going to do a video on it. So that spurred me into going, yeah, I should probably finally get off my ass and, and make my own do it yourself light box. And so I experimented. So the first video was just, you know, first experiments and the second one was even better. So I did a second part video of that.

**Dave Jones:** uh, cool. Yep. Everyone's got their own method to do it, but yeah, no, it's not hard. You've just got to diffuse the light.

**Chris Gammell:** I punted on that. I, I have a, I bought $80 on Amazon. It's got a built in light. Yep. It folds down to nothing. And it's fantastic. Like, cause I tried, I tried a DIY version and it just, yeah, I just didn't have the room for it.

**Dave Jones:** So what is it? A light tent? Do you have a link or something? Uh,

**Chris Gammell:** I have a link somewhere.

**Dave Jones:** Is it one of those light, light tents or what is it? Is it a,

**Chris Gammell:** yeah, it's like fabric based. It's probably, you know, like half a meter on each side of a cube.

**Dave Jones:** That's a light tent. Yeah. I've, I've also got, got one of those and I use those for actual product photography and stuff. Okay.

**Chris Gammell:** So this is different than that.

**Dave Jones:** Oh yeah, this is different. This is smaller. So like a board. So if I'm going to do a, you know, a really high res, you know, high quality photo of a board, then apparently, um, yeah, like, yeah, it's just, you know, I've got, yeah, a big light tent, but it's like this big, you know, it's giant. And, you know, it's just pain in the ass to get it out and set it up and, you know,

**Chris Gammell:** got it. So you, you, you keep, you keep the light box out. You're saying it's,

**Dave Jones:** it's just not there. I want something that's just there. I can whack a, I'm doing a tear down. I can whack a board under there. I can do a high res photo. Boom, done. You know, so some people are saying use a scanner, use a flatbed scanner for circuit boards. Apparently you put a circuit board in a flatbed scanner and apparently it's, it's gorgeous. So I'm going to have to try that.

**Chris Gammell:** Yeah.

**Dave Jones:** So, yeah.

**Chris Gammell:** Where will you source such old technology, Dave?

**Dave Jones:** The dumpster. I've got a dumpster. I know. I know exactly where it was coming from. Yep. So yeah, I might try that.

**Chris Gammell:** Yeah.

**Dave Jones:** I might do that today. Just whack it in the scanner and see what output, because you'll get much higher res with that as well. You know, you can do 1200 dots per inch on a large board or whatever,

**Chris Gammell:** you know,

**Dave Jones:** and it's going to be evenly lit because it's lit from underneath as it scans under and,

**Chris Gammell:** and it catches color and everything too.

**Dave Jones:** Well, it should. I don't, I'm not sure how accurate the color is.

**Chris Gammell:** Yeah.

**Dave Jones:** Like mine, my light box, I use accurate, uh, see a high, uh, CRI studio led lights. So it gives, should give an accurate color. Got it. Presentation, but I haven't done like a proper color chart calibration and things like that yet. I can't find it. It's here somewhere. I moved labs and I've lost my color chart. I got one recently and I haven't used it. Oh, here it is.

**Chris Gammell:** Anyone need to see?

**Dave Jones:** Yes.

**Chris Gammell:** Yes. Those. Those. This one was only 20, 20 bucks on AliExpress. So I don't use it much, but yeah,

**Dave Jones:** I got the color chart and a white chart and a grayscale chart and everything. Like one of those things. Yeah. No, they're just separate cards. So, yep.

**Chris Gammell:** Yeah. That is nice.

**Dave Jones:** I haven't actually done any calibration, but yeah. But anyway, yeah, that, that worked. It's amazingly easy to do yourself. It's just, you know, it's nice having a dedicated solution for something, not having to cobble it together every time, which is just paying the ass.

**Chris Gammell:** Yeah. I just, I just found it. So I just linked it in there. I'll, I'll link, I'll link it in the show notes as well. But is that what you're talking about?

**Dave Jones:** Oh yeah. There you go. Yeah. Yeah. Light 10. I've got one that's even larger than that. Yeah. Yep.

**Chris Gammell:** So you're saying you don't like to actually go and set it up. That's what you're saying.

**Dave Jones:** Yeah. No, I hate, I hate setting it up and that's not adequate for like a PCB. Cause the PCB is a flat thing. You know, it's a, it's a flat board. It's, it's, it's different.

**Chris Gammell:** Well, there's like a top, there's a top access, right? So you could, you could zip the whole thing up. there is.

**Dave Jones:** Okay. There's top access in this one. Yeah. Yeah. Okay. Oh yes. I see it. Yeah. There's a little window in the top. Yeah. Okay. Yeah. Fair enough. And, and, and has that just got the leads inside just pointing down? It looks like it's just got the leads.

**Chris Gammell:** It's built in and then it's all reflective around. So that does the light bounce and stuff too.

**Dave Jones:** Okay. Yeah. But that you're going to get reflections on that. If you do PCBs, given the height of that. So if you put your camera outside that cube, that'll be too tall. Unless you've got a ridiculously long focal length. Got it. Got it. Okay. So yeah.

**Chris Gammell:** Yeah. Yeah. It is tough. I mean, when you see a nice photo, you see a Develian photo these days. It's usually a lot of extra work. Yes.

**Dave Jones:** They're great. So anyway, highly, highly recommended do it yourself. Simple solution. Works well. Okay. Yep. So I've got, I've got to put more effort into polish, spit and polish that though. Yeah. I've got to finish it off. Yeah.

**Chris Gammell:** Did you have a chance to listen to the RP 2040 show last week? Did you, did you get all your questions answered?

**Dave Jones:** I did not. Unfortunately.

**Chris Gammell:** It's okay. It is a microcontroller with external flash. That's what they, that was the answer to the, to your query.

**Dave Jones:** To my query.

**Chris Gammell:** Yeah.

**Dave Jones:** There were, there were, I think, I think I, I think I probably had majority support. I did it on Twitter. I did a poll on Twitter. I think I, I think I had majority support that it was not technically a microcontroller. Microcontroller with external flash.

**Chris Gammell:** I was surprised to see that there was, some people were saying there's other micros out there that are doing this sort of thing. There was an NX, NXP one too, where they're moving it outside of, outside of the chip. So.

**Dave Jones:** Oh, it's been done since the 8032 days. Sure. You know, the Intel 8032 in the late, mid to late seventies. I mean, you know, isn't anything new there, but yeah, it's not, it's not a microcontroller. Damn it. Still going to die on that hill.

**Chris Gammell:** That's, that's your, your hill to die on my friend.

**Dave Jones:** It's a, it's an asterisk microcontroller.

**Chris Gammell:** It's a, it is some cheap, cheap silicon. And if it's available, it might be, it might be the only product that's available these days. So who knows? Liam, who was on the show has since written about the journey as well. And he's got a bunch of code snippets and stuff like that. So we'll link that in as well. The journey to Raspberry Pi silicon. So I'm glad they're still writing that stuff up.

**Dave Jones:** I'm working on a little project. I've got right under my microphone here. I can't get down or disturb my microphone, but I'm not going to tell you what it is, but yeah, it once again requires choosing a micro or maybe choosing a, an existing dev board. And I tried having to look, I was going to put this on, I was going to ask on Twitter, but I did find one, a microcontroller, like a board, like a little Raspberry Pi Pico thing, you know, or a feather or whatever it is. One that actually had a built in LCD or an OLED display. One that had like built onto the board, not a, not a hat, not a daughter board that goes on top, but a, but an actual one that's built on.

**Chris Gammell:** Have you seen those, uh, hell tech ones that, uh, Andrea Spees, uh, reviews, like 15 bucks. They got a little OLED. They've got a, um, ESP 32 on them. They've got a Laura chip on them and they're 15 bucks. Like it's, it's insane.

**Dave Jones:** Right.

**Chris Gammell:** Uh, I got a couple of those around. They're right. Kind of crap, but, um, the antenna's crap for sure. Is it whole tech or hell tech? H E L T E C. I believe.

**Dave Jones:** H E L T E C.

**Chris Gammell:** And if you look up Andreas's video on them, he's got a couple of videos on them. Right. But basically there's, I mean, they're going to be like all these express and stuff like that. Yeah. Got it. They're cool little boys. I mean like,

**Dave Jones:** Oh yeah, no, I, yeah, no, that's the one I found. Oh, okay. That's actually the one I found.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. I ended up finding that in my,

**Chris Gammell:** what do you look at? What are you looking to do with it?

**Dave Jones:** It's, I basically just want a, I'm just looking to do some, uh, ADC measurements, some high, some high precision ADC measurements. Oh,

**Chris Gammell:** then I would definitely not use the hell tech thing.

**Dave Jones:** Why?

**Chris Gammell:** Uh, because,

**Dave Jones:** Oh no, no, it'll be, no, I'll have an external daughter board attached to this. Like I'll have an external board attached to the bottom and it'll actually be a combo flat flex board. Okay. Right. So it'll be a, it'll be a, uh, flex rigid, you know, combo. Okay. Board. So I want to attach this, whether or not I actually, you know, use an off the shelf thing like this or whether or not I just simply design everything I want, including the micro I want to use onto the flat flex I'm going to design anyway.

**Chris Gammell:** So I've done that before with, with the feather form factor and the little OLED screens. It's super simple, you know, like the Adafruit libraries are great for that sort of thing.

**Dave Jones:** Oh yeah. You can get it to plug on top. Yeah.

**Chris Gammell:** The thing that stinks about it is that like, so like you're, you're plugging these things together and then you got to rotate sideways. Right. So like basically because it's going to be, so like you could take, you know, the stack of three boards and then turn it on its side. And then it's kind of like a front panel display style. So you could do that sort of thing. Right. Yep. Mounting will be okay, but honestly I've done a couple of prototypes like that. It's been great.

**Dave Jones:** Yeah. I'm, I'm, I'm thinking, cause I got to do the board anyway, like I might as well integrate, like I might as well just do an Arduino nano or something and just put the Atmel processor straight on there and it becomes an Arduino. I like, it's just,

**Chris Gammell:** are you definitely using an external ADC or no?

**Dave Jones:** Yes. I'll be using an external ADC. Yep. External precision ADC. There'll be a bunch of analog measurement stuff. Got it. And, and like, and, and I don't need USB. I don't need like anything else. I don't need like,

**Chris Gammell:** cause I mean, there's a lot of dev. So I was just going to show you my, my little EFM eight dev board, right? That's got like a screen.

**Dave Jones:** I've got quite a few of those. Yeah.

**Chris Gammell:** So that's got stuff in there too. I mean, you could do that if you wanted the laser bead that I have is.

**Dave Jones:** No, it has to be that sort of like small form factor, a lot like we've been talking about. It's got to be that small, narrow form factor just for reasons.

**Chris Gammell:** Okay. I mean, another thing you could do is you could get like a, you know, maybe, maybe get something that just drives like a, like an FFC, like a flat flex and then have the, the screen wherever you want it to be. Right. But then you gotta.

**Dave Jones:** Yeah. Yeah. Just flop over. Yeah. I'm thinking about, yeah, just doing it myself. And, but then it's got to be like an off the, it's got to be an existing ecosystem. So it's got to be a, it's got to be a, an Arduino or an ESP32, or it's got to be, you know, one of the things, cause I don't want to have to write drivers for the, you know, for the screen and everything like that. I don't want to dick around. Got it. Right. Somebody's already written all that stuff.

**Chris Gammell:** Then I would definitely recommend that the Adafruit OLED ones. Those are fantastic. Like they're super, super sharp.

**Speaker ?:** It's just,

**Dave Jones:** it's just a multiple stack that that'll mean I'll, I'll have like a three stack. Like board solution. So I'll need the screen and then I'll need the board. Yeah.

**Chris Gammell:** I'd say prototype that though, too.

**Dave Jones:** You know, yeah, I could.

**Chris Gammell:** Prototype that just because it's not as big as you think it would be. Right.

**Dave Jones:** Right. Oh yeah. You know,

**Chris Gammell:** it's the height of two sets of headers, two sets of like stacking headers effectively. So it's only, it's only going to be, you know, 10 centimeters. I don't know. Like maybe less than that.

**Dave Jones:** Probably doesn't matter in the end. I don't know. It's just 10 centimeters.

**Chris Gammell:** No.

**Dave Jones:** Yeah. Yes. I did look and consider that one.

**Chris Gammell:** My ability to, to metric in my head is, is gone down over time. Right.

**Dave Jones:** You yanks. I know. You seppos. I know. Yeah. Yeah. Weird. And you know, and like some of them have got wifi. I don't necessarily want wifi. Although maybe some people might get use out of Bluetooth for it. Maybe. Okay. Perhaps.

**Chris Gammell:** This is going to be like a product maybe or no?

**Dave Jones:** Yeah. It could be a product. Like, you know, just a simple open source product, whether or not I sell it myself or I just open it.

**Chris Gammell:** Got it. So this is an interesting use case actually, because, so I've been wondering about this. So I don't know if you saw the spark, the new spark fund micro mod, I think they call it. No,

**Dave Jones:** I don't keep, I, I, I've just given up keeping track of all these micro boards.

**Chris Gammell:** So it uses a, it uses an M2 header. We talked about it, I think briefly on here. Maybe, maybe it was when it was a guest episode, but it's a, it's an M2 header and then the microcontroller. So they've put another type of standard out there.

**Dave Jones:** Hang on. What is an M2 header?

**Chris Gammell:** That's like what you plug a flash, hard drive in to your motherboard with. So it's like off the motherboard.

**Dave Jones:** Oh,

**Chris Gammell:** right. It's like a high density edge connector.

**Dave Jones:** Yeah. Yeah. And, Oh yes. I see it now. Yeah. Yep.

**Chris Gammell:** And so they basically, they have this new standard for it. I don't really get it. I mean, like the idea is that like you could go and switch out the processor and then the baseboard is always the same. It feels like a weird place to put modularity.

**Dave Jones:** Oh, no. Well, it has a long history of this before all this maker movement stuff. And before all this, you know, before all these micros came along,

**Chris Gammell:** you're going to say PC one of four, aren't you? Don't say PC one of four.

**Dave Jones:** No, I'm not saying PC one of four. No, there were other formats. There were other in the age of PC one. Oh, right. So like, you know, in the, in the nineties, in the, you know, 2000, early two thousands. Right. There were these form factors and they would use like a memory form factor. There was one. In fact, there was a, a community. There was a, like a consortium of manufacturers. I think don't quote me who got together and standardized on a memory stick. You know, they like, like the SIM module form factor and they'd put their computers onto these SIM modules.

**Chris Gammell:** Like this, like the so dim you mean like that kind of thing.

**Dave Jones:** Yeah. Okay. Yeah. The, so dim. Yeah. The sodium connectors. I can't remember the consortium name or whatever, but the, yeah, that was all the rage, you know, and there's many other companies who've used existing PC based solutions to develop single board computers. That's their interface.

**Chris Gammell:** So there's huge history there. So there's got to be a, sure, sure. I guess, I guess it's the, it doesn't seem like there's much on the actual, the swappable piece. That's, that's the piece. That's what I don't understand.

**Dave Jones:** No, no, no, it's not. There's a micro and there's an oscillator and there's a, and there's a Bluetooth antenna or a wifi antenna, but that's it.

**Chris Gammell:** Right. And so what you were just saying about like the, oh, well we could, you know, switch out for Bluetooth or whatever else. Like that would be, that's what made me think of this sort of thing because you could go and swap it out pretty easily.

**Dave Jones:** Right. Put in a Bluetooth version of it. Yeah. Yeah. It's, you know.

**Chris Gammell:** Every time I look at an M2 header, I'm like, oh, that looks so big. And then like, you actually see it in real life. You're like, oh my God, that's tiny. So like, it is really quite tiny. Yeah.

**Dave Jones:** It's small. Yeah. Yeah. It's pretty small. Yeah. No, I can, you know, there's, there's a niche there for, yeah, but you know, but, but then again, like you've got to buy the M2 header for your, I don't know how much I've never priced an M2 header, but you know, I've, I, right, right. Okay.

**Chris Gammell:** But then the other hardware to actually screw it down as well. I mean like, yeah, it does add up.

**Dave Jones:** I was going to say there's other stuff. Yeah. You've got to add the press fit stud, you know, for the like, oh yeah. Yeah. That, that's why I think the other solutions are more popular. The ones with the, the, the, the pin headers, the stackable pin header, you know, like your Arduino style or the, or the castellation side of the board style, you know? So yeah, they're just more usable in more applications. I think this is,

**Chris Gammell:** yeah, honestly, these days, I just think whatever, use whatever is best supported for what the software you want to do, you know?

**Dave Jones:** Yeah, exactly. That's, that's all I care about for this solution, this project that I've got. It's like everything else, like that, that's all I care about. Cause I don't want to spend a month writing the bloody software. I just want to, okay. Yeah. I might have to write my own analog to digital converter interface and read the sentence, but that's it, right? That's the only thing I should have to write. Everything else should just be handy.

**Chris Gammell:** It'd be interesting. I mean, how much, how much speed do you need on your ADC readings? Oh, nothing. No,

**Dave Jones:** nothing. No, no, it could be five times a second.

**Chris Gammell:** You should try out like circuit Python, micro Python. You know, that would be another good one. The thing I really like about that is like the prototyping.

**Dave Jones:** No, it's just a new language. No, no, I just want.

**Chris Gammell:** It's super simple, man. Arduino EC. I'm just saying.

**Dave Jones:** No, no, it doesn't matter. It might be super simple, but no, it's like a, why? I already know how to program EC. Why would I learn circuit Python or whatever?

**Chris Gammell:** Because you're a content creator.

**Dave Jones:** Yeah, I'm a content creator, but no, you know, sometimes I just want to bring more people into the industry,

**Chris Gammell:** you know?

**Dave Jones:** Yeah, maybe. Yeah. Okay. Right. But then it, you know, but no, you can't just say it's super simple, right? It's a, it's a learning curve. You can't just throw it out there. It's super simple.

**Chris Gammell:** I mean, here's the thing. I've been through both learning curves of C and MicroPython. And let me tell you, this, MicroPython is a lot easier. It's, uh, yeah.

**Dave Jones:** Sure. But I already have the C skills. True. Okay. And almost everyone programs in Arduino. I mean, you know, how many people out there are Arduino literate? Sure. Right. Sure. Practically everyone. So, you know, it's,

**Chris Gammell:** I wouldn't agree with the practically everyone, but I would agree with many. Yeah.

**Dave Jones:** And it'd be jumping on a bandwagon. That is like, which is fine if you want to do that, but switching to circuit Python to do that would like, you know, the reason that you do it, there's no advantage. It's simply you're jumping on a bandwagon. Cause I want to do videos on that topic. Right.

**Chris Gammell:** No, I think there actually is. I think there actually is very specific advantage, which is the prototyping is faster. I can tell you that specifically it is much faster.

**Dave Jones:** Right.

**Chris Gammell:** It is a change in paradigm, right? So it's, it's not, it's no longer like, it's not click upload, verify test, whatever. It's literally like write code, hit save, write code, hit save. And like, you're just seeing this live action happen. It's, it's something different.

**Dave Jones:** Okay. Well, that's pretty cool. It's trying,

**Chris Gammell:** I think maybe on its own, maybe not for a project. You actually want to like, I think, I think what you're saying here is making progress, right? You want to make progress fast. Yes. And Jake,

**Dave Jones:** I want to make progress fast. Yes. Exactly.

**Chris Gammell:** Yeah. Jake Carlson posted a project he was doing and he was, he was saying on Twitter, he's like, I'm really proud of myself just because I got it past the finish line. And like, I really resonated with that because it's so easy to just like over optimize and just getting something out there, even if it's suboptimal, just pushing past the finish line is really important. You know?

**Dave Jones:** Yeah.

**Chris Gammell:** Yep. So tell me about it, but you should make another video about micro or circuit Python. You should try it.

**Dave Jones:** Oh yeah. No. Yeah. That'd be a, yes. That'd be a thing. Yeah. Yeah. Cool. Yeah. Totally. That's great. But yep. Not necessarily for this project. Sorry.

**Chris Gammell:** That's okay. It's all right, Dave. You're not paying me for consulting anyways. Yep.

**Dave Jones:** And if you were, because I would have to do, yeah. Right. Because I wouldn't want that learn, me learning micro Python to be part of that video series, designing that thing. Right. I want designing that widget to be just designing that widget. I don't want to have to, you know, then do two or three videos, you know, learning the intricacies of micro Python. Right. I'd rather that. So I'd have to do that first, then jump in those projects. So I've already, so if I choose that, if I choose micro Python, well, I've got to go learn micro Python first. And then because I'm a content creator, I'm going to shoot video about it. Right. So then I've got to create a whole video series on micro Python or whatever before I can even start work on my little thing that I just got excited about yesterday. That's true. Right. Yeah. It's like, you know, that's a good point. Yeah. Yep. Yep. Yep. Enthusiasm for a project is everything. Right. If you don't have the enthusiasm to finish it, then you're momentum.

**Chris Gammell:** Yeah. Very important.

**Dave Jones:** Yep. Yep. So that's why I poo-pooed you, your micro Python thing. Well, so you're like, you also like, you know,

**Chris Gammell:** for this project. Let's be honest.

**Dave Jones:** Yeah. No, come on. No, I have legitimate reasons always for poo-pooing things. And that's my legitimate reason is because I was excited about this project and I just want to go boom. I just want to do something while I'm excited. And that does not include learning circuit Python. So sorry, dude.

**Chris Gammell:** It's okay. No skin off my back.

**Dave Jones:** Yep. Oh boy. We're way over for an hour and 16 minutes. Yeah. That flew by.

**Chris Gammell:** The video editor is going to be pissed about this.

**Dave Jones:** Yeah. I got it. Yeah. I was going to do shit today. Now I've got to edit this video. Don't I? Glutton for punishment. Yeah. No, I'll just slap it together. I'll just side by side render. That's it. Yeah. No taking out ums and ahs. All right. That's it. Done.

**Chris Gammell:** If you don't like how we sound on this video, go listen to the Amp Hour audio podcast.

**Dave Jones:** Yeah. Because yeah, I'll be, my video version will be using the MOV file, which we think, we argued about this before. Well, you just wondered before the show, does it use lossless compression or not? I think it uses lossy compression. So it won't sound as good as a WAV, WAV, WAV, Sure. File. So anyway. All right. Yep. Talk to you soon. That's it. Catch you next time.

**Chris Gammell:** Whether talking about consulting or stressing about chip availability, we can press the crap out of the week's news each and every show down to that crunchy, high def sound made for your 100K speakers. All thanks to the generosity and goodwill of our patrons. Join the crowd in the Discord channel at patreon.com slash the Amp Hour.

**Speaker ?:** We'll see you next time.
