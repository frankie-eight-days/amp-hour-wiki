---
episode: 221
title: Warming Up To IoT - Tendentious Thermal Tools
url: https://theamphour.com/221-warming-up-to-iot-tendentious-thermal-tools/
---

**Dave Jones:** This is The Amp Hour Podcast. Reported October 20th, 2014. Episode 221. Tenditious Thermal Tools.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Why do I always start?

**Chris Gammell:** Why do you always start?

**Dave Jones:** I don't know. That's just... I don't know. Did we... At the start of the... When we first... I was such a delicate flower when we started, Dave. Right, okay.

**Chris Gammell:** And now I've blossomed into a... Now you're a big... A ragweed of annoying...

**Dave Jones:** Badass nerd.

**Chris Gammell:** Annoying loudness.

**Dave Jones:** You're actually learning to shout back. Yeah, well... Yeah.

**Chris Gammell:** I've had a good tutor.

**Dave Jones:** The finest.

**Chris Gammell:** Yes. So what's new, man? How you been?

**Dave Jones:** Busy.

**Chris Gammell:** Busy.

**Dave Jones:** I released a video for a week and somehow I'm flat out busy.

**Chris Gammell:** Yep. Well, these things happen. You missed a good one last week.

**Dave Jones:** Yeah, so I heard. Yeah, but it went for two hours. Yeah, sorry, people. Yeah, we goofed up the time because it was like daylight savings or something. We had a guest and we always goof up guests and throw in the daylight saving and, yep, all hell broke loose.

**Chris Gammell:** You know, I'm starting to like it, though. I realize after the show, I'm like, you know, I got asked all my questions. You know, usually when we have both of us, it's like we're like kind of vying to ask questions and, man, when you can't make it, I'm going to have to schedule some more interviews without you. We'll see. We'll see. Ah, goodness. It's nice when the guest talks more. Yep. So how goes the world of electronics? You said you've been tearing down. Well, I saw your terror tear down on the new Rigol scope. That was nice.

**Dave Jones:** Yeah, what I did yesterday and I've got to finish off this morning because, hell, it takes a long time to do this. I was reverse engineering the Rigol, the analog front end on the Rigol.

**Chris Gammell:** Right. Which went over in that teared on video. You said it was real different.

**Dave Jones:** Yes, yeah, it's totally different. They've gone for a discrete transistor front end, which makes it harder to trace as well. And then it's a four-layer board. So, you know, there's the difficulties of, you know, trying to trace a four-layer board where things go. If that via suddenly disappears into the middle of the board and you can't see it on your photograph overlays, it's like, well, get the multimeter out and start buzzing every pin systematically.

**Chris Gammell:** Time to buy an X-ray machine, man.

**Dave Jones:** Yeah, exactly. That's right.

**Chris Gammell:** Was the old Rigol a two-layer? Is that... Is that...

**Dave Jones:** No, I'm sure it would have been four as well. I can't remember offhand, but I'm sure it is. I'm sure it is.

**Chris Gammell:** You know, I was remarking earlier this week that I've gotten... I've been so spoiled. Like, I was back doing a two-layer board with, you know, like, not a complicated layout, but like, you know, it was a compressed layout. It was a SSOP pinout and stuff. And it was just like, oh, I'm so... When you're used to four layers, you get so spoiled by it, you know, you just can't...

**Dave Jones:** By those power planes. You don't have to worry about power routing because you just know that's going to go on the inner layers. Right, exactly. No problems whatsoever. Even if you've got four different power planes, you have four different, you know, cores on something, it's still, hey, you've got two internal layers. No worries.

**Chris Gammell:** Exactly. Well, yeah. And, you know, a lot of people will be like, oh, well, you can just pour... You can do a pour on the bottom of the board, right? Just for a ground plane. You know, a ground plane helps there. But like... But then all the time, you're always worried about, you know, breaking up the ground plane by, you know, putting a trace through it and cutting it in half. Yeah, yeah, exactly. And that could be even worse if you do that. If you... Your signal integrity could start going to crap real fast. You could almost make things worse doing that. So, yeah, it's a hard road backwards. Yeah, it's hard to beat the full layers.

**Dave Jones:** Yeah, I know. Especially if it's just single, you know, supply or something like that, yeah. Yeah, right. Power plane, you've got your ground plane and everything's sweet.

**Chris Gammell:** Yeah.

**Dave Jones:** And you know, you know, you just don't have to worry about anything.

**Chris Gammell:** Infinite sheet of charge, just like them physicists like, right? Yeah, right, yeah.

**Dave Jones:** That's right. And you can just pop it through anywhere you like. That's right. Magic.

**Chris Gammell:** Yep. Glorious. I saw you sent a tweet out that you're going to be speaking in a physics conference. Is that right?

**Dave Jones:** Yeah, I got an invite to give a keynote at a physics conference. It isn't for another year. Oh, that's good. So, they gave me lots of advance notice, which is excellent. Anyway, I'm going to visit them shortly to talk about it. And also, they're going to show me some porn as well.

**Chris Gammell:** That's okay. Nerd porn. Yeah. We have an electronic show. Yeah, of course.

**Dave Jones:** It's a given that it's nerd, you know. Right, of course. That's nerd porn. Hardware porn.

**Chris Gammell:** I don't know what you do, man. Like, I only taught you like an hour a week. So, I just, the rest of the week, whatever you want to do, you know, it's fine. No, that'd be good though. Yeah, I feel like that would be really scary to talk to. Like, I don't know. I feel outgunned by physicists.

**Dave Jones:** Yeah, it's, yep. I know. Yeah. It's scary. These are all, you know, PhD physicists, you know. Right.

**Chris Gammell:** So, I guess at a certain point, you could be like, you could just be like, yeah, but I know how to solder. Yeah, right. Bring it, physicists. Bring it, nerds. You'll be the Wallowitz, right? Right. Yeah, yeah, exactly. Crack some jokes about that. Yep.

**Dave Jones:** Oh, yes. Yeah, I might. Yeah. Yeah. Start writing that now, yeah. Got to start writing that stuff down. Excellent. And, yeah, so that's, yeah, I, you know, eh, why the hell not, you know. Oh, yeah.

**Chris Gammell:** No, it's a good way to meet new people and see fun new equipment and hear about new stuff

**Dave Jones:** and apparently my blog is very popular in their field. Yeah, there you go. These aren't like, these aren't like hardcore, well, they're, you know, they're hardcore physicists, right? But they're not the theoretical physicists. They're the ones who, you know, actually build stuff. The ones who implement practical solutions to, you know, solve the physics problems, you know. So, the ones who design the, you know, the electronics and all the physics hardware that goes into the Large Hadron Collider and all that sort of jazz.

**Chris Gammell:** Yeah, right. So, yeah. There are terms for that. I mean, I know there's like the theorists and the, what is it, like the practicalists? Or, I don't know what it is.

**Dave Jones:** Yeah, there is a term. Yep. Yep.

**Chris Gammell:** Because I know that in like academic publishing too, because there's like papers that are about the actual theory and then there's papers about the method as well.

**Dave Jones:** They're called experimental physicists. Yeah. There's the theoretical physicists and there's the experimental physicists. Yeah. I think these are the highly experimental. Ah, that's good.

**Chris Gammell:** The ones who build stuff. The ones who build stuff. Always, always welcome here on the Amp Hour to talk about that stuff.

**Dave Jones:** Not that the others aren't important. No, we just wouldn't.

**Chris Gammell:** I wouldn't know what to say to them and be like, oh, hey.

**Dave Jones:** No, yeah, yeah, exactly.

**Chris Gammell:** I used to do math.

**Dave Jones:** Yeah, I mean, the first time the email came through, I went, oh, I don't know. That sounds a bit, why the hell are they asking me? And then I went and read about the group and everything and the, yeah, these are the, yeah, I can understand why they've seen my channel before. Yeah. So.

**Chris Gammell:** Yeah, there are these different levels too, right? I mean, like, because I think about even, even like as you keep moving down the line, right? Like, so a lot of the theoretical physicists and, or just theoretical scientists in general, you know, they're coming up with these big, big grand theories and stuff like that. And then the experimental ones are testing it and then eventually it moves in the engineering realm and it becomes a little more commercialized. Yep.

**Dave Jones:** That's pretty much the level it goes down. Yeah.

**Chris Gammell:** Well, no, it goes down further from that then even, right? I think that then. Because then you like, you might have someone who then gets pushed into like a chip and then there's the application side, right? And then you get like FAUs. Right, right. And like factory FAUs designing into dev kits. And then eventually there's shlubs like us who start using dev kits and pretend we designed the whole thing from scratch.

**Dave Jones:** Right.

**Chris Gammell:** Yes, I do know how this works.

**Dave Jones:** I feel like the more exotic stuff we take for granted on chips these days and solid state solutions to like magnetic compasses, you know, digital compasses, accelerometers, right? Right. 10, 15 years ago, right? These chips didn't exist, right? If you wanted to build an accelerometer, well, you put a gyroscope and, you know, electromechanical solution, right? And a digital compass had coils in it and a big, you know. Right.

**Chris Gammell:** And you get to do all the math and there are no libraries written. Yeah, yeah.

**Dave Jones:** You know. And now you just, you know, like these, the tricorder, you know, the, you know, everyone's doing one of these Star Trek tricorder things, having a go at it because you can get so many censor chips now. You can get ones that sniff, you know, anything and sense anything. And, you know, and we just take for granted. And these stuff have only come around like probably the last 10 years has been an explosion in censor chips.

**Chris Gammell:** There's a whole lot of standing on shoulders of giants and such, right? Yep. But that's good. I mean, like, yeah, we totally benefit from it. So what about that?

**Dave Jones:** And once it gets down to the lat level.

**Chris Gammell:** I was going to ask about that tricorder because you've been, you've been, you've been doing some judging. You've been more than usual.

**Dave Jones:** I've been a judging. A judging. A judging.

**Chris Gammell:** Yeah.

**Dave Jones:** The Hackaday Prize. Yes, that's right. That went down. Yes.

**Chris Gammell:** So how'd that go?

**Dave Jones:** I looked through. It's not easy. Duh. It's not easy because you've got, yeah, duh. I know. For those who haven't judged before, it's, it's, I've done a few now and it's, yep, it never gets any easier. Yeah. But, and often there's one that really stands out to me, you know, like just personally, you know, like aside from the judging criteria, I go, that one should win. Yeah. You know, I didn't really feel that this time. Oh, no? Okay. I was more torn. Yeah. I was, I was more torn. So it's hard to pick a favorite. And. So is that a better thing you think? As I posted on the.

**Chris Gammell:** There's just like more. Sorry? More stuff to see then you're. Is it like you don't have a number one or is it like you didn't, it just didn't strike that chord?

**Dave Jones:** Yeah. It just didn't strike that chord. You know, I eventually, you know, cause we had to choose a top 10 out of the 42. Yeah. And, you know, I finally, you know, I went through the criteria, the way it works is you go through the criteria and you're supposed to give them a scaled score in each different category. There's like six different categories and, you know, openness and usability and, you know, all that sort of jazz. All right. Yeah. And so I went, so I go through, you know, the first pass, I just put down what I, you know, guess the numbers might be. And then I go through and sort of, because like when you do the first one, you go, well, what score do I give it? I don't know. Cause I haven't looked at any others. So there's no scale, you know, so you sort of have to balance the scale as you go along. And then when you finish that, you've got to go through again and sort of scale them all out. And then you've got to, then you've got to sort the list and you go, oh, that popped out on top. Did it? Oh, you know, and like, yeah. And, oh, that's not my favorite really, you know, and, oh, I don't think that one belongs in the top 10. You know, I think this one, oh, I can't believe that one missed out the top 10, you know, it's because it's really hard to give a subjective scale across so many projects and stuff like that. So you've got to really go through and sort of tweak it until eventually, I guess you get your top 10. Um, you know, it's, so it still works on that scale thing. Um, it's just that, yeah, you can often forget, you know, you're up to project, you know, 32 and you forgot that project five was really awesome. That was actually better in that category, but you scored it low because it was a lower because it was way back at the start and you didn't know where to rank it and, you know,

**Chris Gammell:** and anyway, well, you have no, uh, no, I don't, I don't feel bad for you. I was part of the judging of 850, the original 850. And that was, oh my God, that was terrible. It was so, so much, so much time. Yeah, I can imagine. Yeah.

**Dave Jones:** I only had so much sympathy. I know, but Mike, it was Mike who judged them all, was it? The originals?

**Chris Gammell:** No, a bunch of us did. A bunch of us did.

**Dave Jones:** Oh, right. A bunch of you. Okay. Right. Yep. And yeah, not easy. And like a few of my favorites that I wanted to see just didn't, that were in my top 10, way up the top. They didn't make it through to the final five. I was a bit disappointed. You know, I kind of like, I liked those and they didn't make it, you know? And well, yeah, that's the way it is. And I foolishly made the mistake of actually posting on the Hackaday forum. And you know the forum nerds, you know? Yeah. Yep. Yeah, right. So, no, it's, you know, and in the end, you've got to say, well, tough tits, you know?

**Chris Gammell:** What, you just go with it? Okay. Yeah.

**Dave Jones:** No, no, look, you know, like ultimately there's no nice way of saying that, sorry, you're lost, you know? Like, you know, it's like, yeah, better luck next time. Why did you lose? I don't know. There's eight judges. You know? Don't ask me.

**Chris Gammell:** Right.

**Dave Jones:** So, right.

**Chris Gammell:** I think the tough type too is like trying to look across all of these different fields too. Like the, so like the ramen pie, this ramen spectrometer thing.

**Dave Jones:** Oh, that had the worst video I've ever seen in my life.

**Chris Gammell:** I knew you were going to say that.

**Dave Jones:** Oh my goodness.

**Chris Gammell:** I know. Right.

**Dave Jones:** So, it did lose a few points there for that. Yeah. For just annoying the hell out of me.

**Chris Gammell:** Yeah.

**Dave Jones:** But yeah, no, it was very impressive though.

**Chris Gammell:** Right. But I mean, like, I don't know anything about spectroscopy in the first place. So like that, you know, that kind of stuff is like.

**Dave Jones:** So you have to do a bit of research and, you know. Yeah. Yeah.

**Chris Gammell:** But yeah, I do, I do recommend people check them out. There, there's a, aside from the, the video for the, the ramen pie, which like Dave said, was terrible. Because he used like a computer voiceover board and then he sped it up. Yeah. And then sped it up. And oh, voice.

**Speaker ?:** Terrible.

**Dave Jones:** Yeah. Computer voice. Oh yeah. That's awful. Yeah. It was almost like one of those infomercials. You must buy this now, you know, after 12 PM, you're a LOL special. Well, buy it now.

**Chris Gammell:** Sunday, Sunday, Sunday. In terms of conditions, may apply. That's it. Yeah.

**Dave Jones:** Yeah. Well. Yeah. Oh well. And then the 3D printer guy, sorry, I forget his, Neil, I think is his name.

**Chris Gammell:** I don't know.

**Dave Jones:** You know, real, you know, tried to argue that his 3D printer was open, was more open than any other project. No, I, sorry, more connected. And I'm sorry, it's not, it's not a connected, you know, if you do a 3D printer, I don't care what, you know, core you're using in there to communicate with everything. It's not a connected device, really. It hooks up to a PC in it. And I, sorry, it's not a 3D printer. It's a pick and place machine. Yeah. So it's a pick and place thing.

**Chris Gammell:** You know, so I was reading some of those comments too about that. And that was, so it was an interesting conversation there. And really just his project in general. Actually, he wrote a post that sounded similar to the, we wrote about jumping the shark. And we had talked about that a couple of weeks ago.

**Dave Jones:** I didn't, I didn't read that fully. I started and got distracted.

**Chris Gammell:** And so he brought us some really interesting points in there, actually. Do tell. One of them being that, you know, like this is a, you know, a much more important thing to have a pick and place these days. And I think that he's right. You know, kind of just moving towards, well, okay. I already hear the, I hear the, I hear the grumbles.

**Dave Jones:** He's right in theory. He's right in theory. Right. And like, it's like a chip printer machine. Well, okay. No, no, no, no, it's not. No, no, no, it's not. It's not good. Because pick and place machines are real. Right.

**Chris Gammell:** Right. Yes. No, but I mean, I, I, I think about just kind of like moving forwards, you know, so I, I think it could be more realistic that people need these a little bit more. Right. Just in terms of complexity going up. Sure.

**Dave Jones:** Oh yeah. No, totally. Totally. Oh, there's totally a market for it. Yeah.

**Chris Gammell:** So whether or not he could do it, I don't, I don't have any comment on. Right. Exactly. I mean, that, that, that remains to be seen. And I hope he, he continues to make that thing. Cause it could, if it does deliver, it could be great.

**Dave Jones:** I fully support him. No, it's yeah. It's great.

**Chris Gammell:** Yeah.

**Dave Jones:** It's just that like, um, it's, I, I like to compare it to sort of making your own boards, right? Yeah. It's possible. You can do it. Yes. You can do plated through. Yes. You can do everything else, but ultimately there's a niche need for it because, you know, you're, you're caught in that balance and same thing with pick and place machines. And I, I suspect they might always be like that. It's just the inherent complexity of the task.

**Chris Gammell:** Well, and really it comes down to, it's like, who knows and who really cares, right? I mean like that, it'll, it'll fall out when it needs to, if, if it does become a need, then people will go buy them and more, more things will hit the market, right? That's kind of what it comes down to.

**Dave Jones:** Yeah. Yeah. But it's one of those things that ultimately can't get pushed too far down in price, you know, because it's a complex thing you've got to do, you know, when, when you have to have 20 or 30 feeders and you've got to have vision systems and you've got to have pick and place heads with suction and vacuum and blue, all this mechanical, you know, precision. It's, there's just inherent limits to the physics of how easy it is to make. Well, and yeah.

**Chris Gammell:** And maybe the fact that he put $300 on is one thing, but I'm just saying like, if the market exists, then people will pay more for it. Right. I mean, like, so, so we talked about a couple of weeks ago.

**Dave Jones:** Well, that, that, that, that Chinese one, right? Yeah, exactly. The, the Wayne and Lane, they're doing that one. The $3,500 Chinese one, right? Yeah. And that, that's like a legit one.

**Chris Gammell:** Everyone's raving over that. Yeah.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** And because it's, it's way cheaper than, you know, like, like when Ryan O'Hara was on the show, he was talking about that quad that he has, right? And that was like $16,000 and, you know, it's just steps down and, you know, maybe that next generational jump will be there. Maybe it may not be $300, but maybe it'll be worth $500 or $1,000, you know?

**Dave Jones:** See, that's the thing people don't realize about this project. You know, it says the $300 pick and place machine and you go actually read the project on the, on the page itself, on the, uh, Hackaday, uh, you know, entry page. It says, yeah, it can be anywhere from $300 to $3,000 depending on the options. And I'm going to go, well, I can already go buy a $3,000 one from China.

**Chris Gammell:** Right. Yeah. And that's, and this one might be better. Like I said, all that stuff can shake out in the market. You know, if there is really a market for it, that stuff will all shake out over time, I think.

**Dave Jones:** Yep.

**Chris Gammell:** Point I was trying to get to though, is that another step in there, I think is a better intermediate step. It's actually a step I'm taking right now. Uh, I am building a, uh, toaster oven reflow. Not, nothing new or groundbreaking here. Mostly just, I wanted to.

**Dave Jones:** You do realize you can buy off the shelf solutions here.

**Chris Gammell:** Uh, yeah, of course. Right.

**Dave Jones:** Uh, well, both in terms of the, like a complete unit and also the oven controller. Like I've got one of those, you know, prebuilt oven controllers. Oh, you do? I highly recommend it. Which one do you have? Yeah. Uh, it's the German, uh, Elektor one. Okay. I think it's Elektor. Anyway, it's something, uh, I can, I can run and get it.

**Chris Gammell:** Uh, if you, if you want to, sure. I can talk about it. I'll be back in two seconds. There actually is a new. Talk, talk, talk. Yeah, I'm talking. Don't worry. There actually is a new one. Uh, there was a Kickstarter that just, uh, came out as well. Like Dave said, I mean, these already exist. This is a new one that's, uh, running right now. It's already like trebled its goal for, uh, Kickstarter. It's like 18, it's, uh, it's. I'm back. It's like 80 bucks. I was just talking about the, the Zalus. There's another one that's on Kickstarter right now. It's got a touchscreen.

**Dave Jones:** Oh, is it? Okay. Yeah. I mean, and I'm sure it's very similar, right? That'd be nice. I might. Yeah. Have a look at that. Mine works. It's just got leads. You know, it doesn't have a fancy.

**Chris Gammell:** Right. And this, I mean, so it's got a thermocouple. And the real, so the real reason I was going to do it though, is I started thinking about it and I'm like, well, I need, well, let's see. I, I, I, I didn't know I wanted to, you know, cause I'm using smaller and smaller package types and, um, doing boards and stuff like that. And then I started thinking about it. I'm like, okay, so if I buy like a $25 Toastrovenoff Amazon, which I did. Yep. Uh, I'll need a thermocouple. I'll need, you know, some, uh, some kind of relay control and then I'll need, and then if I want to make it a little bit more convection, like I'll need like a fan controller and I'm like, oh, Hey, this is, uh, this is the bench buddy. This is what we designed in contextual electronics. And I'm like, and it's like, it's not cheap, right? Obviously the, you know, to build the bench buddy was more than whatever this, uh, the Zalus is, but.

**Dave Jones:** Yep.

**Chris Gammell:** You know, sometimes.

**Dave Jones:** How much is this Zalus?

**Chris Gammell:** Uh, it looks like the early ones are 80 bucks.

**Dave Jones:** Okay. Mine's a hundred and 29 euros. So it's not cheap. Okay. It's a fairly, you know, it's a fairly expensive.

**Chris Gammell:** But yours exists already too. And I think the Zalus isn't. Oh yeah. No. Yeah.

**Dave Jones:** Totally. You can buy it, but there's plenty out there, you know, you can even get them as Arduino shields, you know, you can get a shield. There's really nothing.

**Chris Gammell:** And that's the fact that the bench buddy is too. It's an Arduino shield. It's just big. Right. And there's nothing, you know, there's, there's really not much to it. Right. It's like I said, it's a thermocouple.

**Dave Jones:** There's a thermocouple and a, and some. Thermo. Relay.

**Chris Gammell:** Yeah. A relay controller. Right. And a relay. And a relay. And yeah, you basically put a profile in. But, uh. Yep. My whole point in this was like, this is kind of the, the step between, because if you're going to get your own boards, it's just as easy to, you know, a lot of the pick and place woes can be solved just by putting down solder paste and then having it, uh, you know, form up in an oven because of the surface tension, you know, that's going to solve 80, 80% of your issues anyways. Right. You don't have to solder anymore directly. So, yeah, I mean, I think that's just another step along the way. And so it's, yeah, that's the, that's my new project.

**Dave Jones:** I recommend if you are going to get one, get one that has a really easy to use learn mode. Cause that's not just for setting it up. Cause you're always changing, you know, your oven, the position of the board, all sorts of, you know, you do a small, tiny board, you do a big board, all sorts of things like that. And you're always changing that. So it must have an easy to use learn mode. So you can whack the thermocouple in there with the big base board and then you can, uh, hit the learn button and it learns. It's exactly, you know, it learns the profile for that particular placement of the thermocouple, et cetera, et cetera. Oh, I see. Okay. Yeah.

**Chris Gammell:** So you move it around depending on the board as well. Okay.

**Dave Jones:** Move it around depending on the board and stuff. So yeah.

**Chris Gammell:** Yep. That's interesting. Why wouldn't you just fix the thermocouple inside the oven?

**Dave Jones:** Ah, but see it, um, it changes depending on how, what, how big a board you're using and what base plate you're going to, uh, sit your board on and all that sort of stuff. Oh, just because of like thermal resistivities and stuff like that. Yep. It's, it's got thermal, um, thermal mass. If you have a big board, you know, if you've got a big panel, right. Doing a big panel with lots of ground playing on it, right. Huge thermal mass.

**Chris Gammell:** Yeah.

**Dave Jones:** In these sort of things. That's a totally different, uh, reflow profile to having just a little tiny board sitting on the grill at the top, you know, just with five, uh, you know, things on it. Right.

**Chris Gammell:** But I mean, I figure, I mean, first off mine can't fit, I mean, like mine's literally a toaster oven. It's just a piece of crap. So.

**Dave Jones:** Right.

**Chris Gammell:** That's. Okay. Yeah. Yeah.

**Dave Jones:** But they can usually fit a smallish panel. They can usually fit a, you know, a 300 millimeter wide panel. Surely.

**Chris Gammell:** Oh, uh, yeah, maybe.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. I guess it depends how much you panelize and stuff. I always think of panels being bigger. Well, I remember when Mike was on the show, Mike, uh, Mike's electric stuff, Mike, uh, he talked about, he had like a pizza oven, didn't he? Didn't he mention that?

**Dave Jones:** Uh, I don't recall, but yeah, let's go with that.

**Chris Gammell:** Yeah. He does now. Right. And that, I mean, that, that's the kind of size I think of when you, when you are, when you have a full panel. So, so tell me, do you actually use this thing though or no?

**Dave Jones:** I have used it. Yeah.

**Chris Gammell:** That's not what I asked.

**Dave Jones:** I don't use it. Well, no, look, I don't use it often cause I'm not doing boards. You know, there could be months go by where I wouldn't use it. You know?

**Chris Gammell:** Okay.

**Dave Jones:** Because I'm, I'm not doing any projects at the moment. I don't need to assemble them or I'm hand soldering.

**Chris Gammell:** Gotcha.

**Dave Jones:** You know? Yeah.

**Chris Gammell:** What I'm trying to say, Dave, is why aren't you making any boards, man? Hop two. Hop two.

**Dave Jones:** I'm too busy. Cause I'm doing this bloody radio show. I don't have time. I know, right? Yeah.

**Chris Gammell:** The amp hour, it's, it's all to blame. It's all to blame. So much of your week. Yep. I bet, I bet you record the amp hour about as much time as you spend on the forums, right? Right. Yeah. Right. Right. Yeah.

**Dave Jones:** And then you've got to maintain the blog. No, that takes, as I said, I rarely have time to work on projects at the moment.

**Chris Gammell:** Yeah. You'll get there. So yeah, I've been, I've been kind of on a, on a buying streak lately. I've, so I, I bought this toaster oven and I think that's what kind of set it off. I also bought a, a SparkFun RedBot kit. You ever seen that?

**Dave Jones:** No. What's a RedBot?

**Chris Gammell:** So it's like, it looks like a little Arduino compatible, but basically it's got like a, um, motor drivers on board and a bunch of inputs for sensors and stuff like that. I'm actually not sure why they didn't make it into a, uh, Arduino compatible shield. It's like its own standalone board.

**Dave Jones:** Ah, right. Yeah. It's, it's, it's a little, it's actually a full robot kit. It's like, it's got little wheels and goes around and blah, blah, blah. I don't know.

**Chris Gammell:** I want to learn about robots. So, um, yeah. Trying that out. And then, uh, I got the, uh, the light blue bean. Have you heard of that?

**Dave Jones:** You told me about it before the show.

**Chris Gammell:** You're supposed to play dumb, Dave. Come on. So that's a little, uh, yeah, well.

**Dave Jones:** It's yet another Bluetooth-y, Internet of Things-y. Yeah. It's like a little $30 board.

**Chris Gammell:** It hooks up to, it's like Bluetooth, uh, low energy. And then it's got some, some breakouts on it and it can run off a coin cell. And, uh, yeah. Meant for that kind of Internet of Things-y stuff. The only thing I don't, I, I, I just got it running, like, I got it up and running like 20 minutes before the show. And, uh, I like, I like that it's like a, it's like a custom Bluetooth module on it. Like they make the actual module as well. And, um, the only thing I don't like is that it has to run on a Mac. Uh, I'm sure that it's just a temporary thing, but. Wah. Yeah. It's, uh, I was, I was actually pretty surprised by that. Like, because I think, you know, it's always got built-in Bluetooth hardware, low energy hardware on Macs. I think that was by design. Right. Um, so, uh, but that's okay. I mean, it, it runs, a little Arduino. It runs right in the, the Arduino environment. So that's pretty cool. I'll try that out with some things. All right. And what else? Sounds like fun. Yeah. I, uh, oh, I am. Oh, go ahead. Yeah.

**Dave Jones:** Oh, I was just going to say, I am working on a project, but it's not actually laying out a board. It's hacking an existing product. Oh, that's fun.

**Chris Gammell:** Okay.

**Dave Jones:** Together. Yep. It's going to be, um, people, my supporters, um, will have already seen, um, uh, 3D, uh, case renders of it. Oh, fancy. Yeah. Okay. Fancy, fancy.

**Chris Gammell:** No content from Dave there. Yep. Sign up today, folks.

**Dave Jones:** Well, well, well, well, patreon.com, EV blog. No, it's not on the forum. It's on my new Patreon website. Have you seen that? Cool, cool. My new Patreon. I'm, I accept patrons now. Yeah. Okay. Anyway, I haven't done a video. I haven't really announced it. I announced it on Twitter and.

**Chris Gammell:** You just did.

**Dave Jones:** So. All right. Well, there you go. I'm on Patreon now.

**Chris Gammell:** But you know, you don't, you didn't play dumb with me.

**Dave Jones:** Look, I tell you what, it's a lot better. It's a lot better than just accepting PayPal donations, right? Because it's all open, right? Everyone can see how much I'm getting, how many people are contributing and all that sort of stuff. You know, it's just, you know, and it gives me, you know, I can, then there's the automated platform in place for me to, you know, if I want to, I can give content or, you know, updates to people who are, you know, who pay up to a certain level, you know, if you're paying, you know, five bucks a month or whatever. Yeah. Yeah. You know, you get a certain thing. And if you pay X amount, I haven't done that. But. No, that's cool. I think that's a good way to support people. I'm not doing the levels. Yeah. Yeah. No, it's great. So. We're big fans of that here. And it's just all open and it's not hidden, you know, and it's, yeah, it's almost got that crowdfunding vibe to it, you know, support Dave. He's up to, you know, my top level is.

**Chris Gammell:** Buy second another book at home. Yay.

**Dave Jones:** I need to pay for my 500 bucks a month internet costs, you know, so sign up for 50 bucks a month and you can pay one 10th of my internet costs. Thank you.

**Chris Gammell:** Yikes. That's a lot of internet costs.

**Dave Jones:** That's fine. Yeah. 500 bucks a month. I'm paying for that.

**Chris Gammell:** Oy. Yeah. Yeah.

**Dave Jones:** Yeah. Yep.

**Chris Gammell:** So, yeah, so this blue bean thingy, pretty, pretty neat. I do recommend people check it out. Like I said, I haven't played with it too much. It's, it's, it's low power. The only, the other thing I don't like about it is the LED, like there's no way to tell that it's powered on other than just, you know, probing it with the DMM saying, oh, okay. Oh. That.

**Dave Jones:** You think they'd whack a lid on there, but then it's low power, right? Well, they, yeah, they do. And then you can. It's a way current with.

**Chris Gammell:** Well, you can, you can hook it up so that it basically, so that it, you basically hook it in to your computer and it recognizes it. Okay. There's a Bluetooth device. And then you can, once it recognizes it, you can click blink an LED just to see which one, cause you can have multiples on the screen. That's kind of interesting. All right. But I didn't know that. And I didn't, there's no, until you actually hook it in, you know, you don't have any way to know if it's alive or not other than measuring it with the DMM. So I was a little confused about that. But yeah.

**Dave Jones:** Hi, I'm just looking at this, uh, Zealous reflow controller page and that actually looks quite good. I like it. Yeah.

**Chris Gammell:** Yeah. I mean, it looks nice.

**Dave Jones:** Yeah. I like, well, there's, there's no box for it, but I guess you could like 3D print a box. And, uh, I think that, yes, they actually mentioned that print your own 3D enclosure. There you go. Um, no, I, I just liked the fact that it has a screen on it, you know, it's a reflow oven is something you don't want to watch with leads, you know, like a lead turns on, it's now in ramp up mode, you know, soak mode. Right.

**Chris Gammell:** And then you're like looking at your watch. Yeah. Yeah.

**Dave Jones:** No, I want to see like a live graph, you know? And yes, I might get one.

**Chris Gammell:** Well, there you go.

**Dave Jones:** I think I might get one. Hmm. Even though I've already got one, but still. Well, that's the thing. I mean, like.

**Chris Gammell:** This one has a graphical screen. All this stuff, right? Like, we don't need any of this stuff. I didn't need a robot kit. No, no, no. Totally not.

**Dave Jones:** Mine is perfectly adequate for the task. It is perfectly purpose designed for the task. And I'm just being an idiot wanting a graphical. Yeah. I'm just a nerd. I want to see a graph.

**Chris Gammell:** A gadget nerd. Right. Yeah.

**Dave Jones:** Uh, yep. Anyway. Oh, I should. It's a sickness. I'm already trying to sell shit on eBay of all the stuff I've got here. Right, right. I'm trying to clear it out. Seriously. Yep. It's all slowly going. I'm working up to getting rid of everything. And then if I need something again, I'll just buy it again. Right.

**Chris Gammell:** Exactly. Yeah.

**Dave Jones:** Rather than have everything sitting around for, you know, just in case, I might use it. And then 10 years later.

**Chris Gammell:** Holding up the lab, right? No, use it.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** It's a sickness. Anyway. Hmm.

**Chris Gammell:** Uh, so.

**Dave Jones:** Speaking of Kickstarters.

**Chris Gammell:** Yeah. Go ahead.

**Dave Jones:** Oh.

**Chris Gammell:** The, uh. Speaking of buying stuff when you need it and just then selling it very quickly later.

**Speaker ?:** Yeah.

**Dave Jones:** Um, there's a, a routery thing. Um, the Anonabox.

**Chris Gammell:** Anonabox. Yeah.

**Dave Jones:** The Anonabox. It's a, you know, it's not really electronics related. It's one of these IT, you know, secure web, you know, stop the NSA spying on you projects, you know. Right. Yep. Kind of thing. Yeah. It's just, and they ran this Kickstarter campaign if you haven't seen it. And, uh, it was, um, apparently too good to be true. Uh, a lot of people, there was a bit of backlash against it. And then, uh, uh, somebody discovered that they were lying their ass off. Um, they hadn't actually developed this, uh, product. It's, they're just buying it from Alibaba, right? They're just buying an off the shelf router from Alibaba and just whacking already off the shelf firmware in it. Yep. Like, you know, which is fine. Like, if you want to do that and produce a ready solution for people, hey, there's a market for that. Yeah. But you've got to be honest about it. Right. You've got to be, you know, upfront. And they, they, they showed photos of the boards they supposedly developed over the last four years or something. I don't know, a couple of years. And, and it's all bullshit.

**Chris Gammell:** Yeah.

**Dave Jones:** Um, and, and anyway, um, yeah, their campaign was suspended. They like hits like, what was this? Was it 600,000 or something? It got up to, it got up to a lot. And, uh, yeah. And they, uh, they suspended it because they, um, everyone reported them and were taking their money back out. And there was a huge backlash. And, uh, yeah. Yeah.

**Chris Gammell:** I actually first saw this when the, uh, going through those, the, um, the 50 final or semi-finals or whatever for the Hackaday prize. One of them was a project very similar to this. It's that someone talked about how it had already been ripped off. And apparently like some of the, some of the, the verbiage from there, uh, got into this Kickstarter as well. I was just like, oh man. Oh, okay. Got it. Shiesty. Yeah.

**Dave Jones:** Right. Ah, goodness. Anyway, let that be a lesson to you. Don't, yeah. Just be honest.

**Chris Gammell:** Don't steal stuff and then start a Kickstarter.

**Dave Jones:** Yeah, you're allowed to, right? No, you're allowed to.

**Chris Gammell:** I almost would have gotten away from it if it wasn't for you damn kids.

**Dave Jones:** Right? Pesky nerds. Yeah. Checking all these details. How dare you go and analyze our photo and compare it with something on Alibaba? Yeah. Yeah. Oh, goodness. No, that's fine. You know, there's, there's a market for value adding like that. Yeah. Oh, definitely. For buying an existing off the shelf solution and, and just tidying it up and packaging it and, you know, and definitely. Yeah. Yeah. Yeah. But you gotta be honest about it. Jeez. That's just, that's just lame. They deserved everything they got.

**Chris Gammell:** I think it's interesting too when you see like these projects, like you said, it's kind of like IT related. And I feel like this is kind of the same class that like a Raspberry Pi was in. You know, like there's like this huge contingent of like people that are, and I'm sure even some of our listeners are in the IT field, interested in electronics. And, you know, if you just say, okay, well you have to go program firmware and, you know, solder this, solder that. But it's a lot less appealing than like, here's this thing with Linux on it. Right. That automatically brings in an entirely new group, which is awesome. Right. I mean, ultimately that is a really good thing for the, for the hobby, for the field, everything like that. You know, like Raspberry Pi was great for that. It brought people in, but then, you know, there are always, and that means these huge campaigns as well, but it can, it can go sour real quick because of that. Obviously Raspberry Pi worked out really well, but it's.

**Dave Jones:** And there was nothing. The only unique thing about the Raspberry Pi was the $35 price point or whatever.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** It was released at like, you know, a, you know, these boards were not new that they didn't invent the Linux embedded computer, you know, far from it. They'd been around for a long time. Oh yeah. Right. Right. But they, they just bought it down to a price point that everyone could afford.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, and made it sort of, yeah.

**Chris Gammell:** Definitely. It's crazy.

**Dave Jones:** Awesome.

**Chris Gammell:** I'm hoping to actually catch up with, is it Eben? It's Eben, right? I think I saw that he's going to be at Electronica.

**Dave Jones:** Oh, okay. When's, when's that again?

**Chris Gammell:** That is. Electronica. Second week. Soon, isn't it? Yeah. Second week of November and I will actually be there. Oh, okay. Excellent.

**Dave Jones:** That's, that's only a couple of weeks away. That's only three, four weeks away. Yeah. Three.

**Chris Gammell:** So we'll have two weeks of just Dave on the Amp Hour. We'll see how that goes. Woohoo! This is Dave talking. We'll try and find him. Maybe I might take a break. Some co-hosts. No taking breaks. No taking breaks. But yeah, it's, I'm already looking at like all of the, like the money that's like, I was looking at like giveaways. Like someone's giving away a Tesla and like, there's a bunch of stuff like that. Like just like. Who's giving away a Tesla? I thought it might've been DigiKey.

**Dave Jones:** Oh, okay. Wow.

**Chris Gammell:** Yeah. I'm going to put my name in. I mean, I think this is going to be like the ultimate, like, you know, put your name in a hat and then get spam for seven months kind of thing. Yeah. Yeah.

**Dave Jones:** And, and you probably have to be present at the booth when the names are called, right? Is that the, that's, that's, that's the usual deal.

**Chris Gammell:** Imagine having. I don't know.

**Dave Jones:** 10,000 people crowding around the DigiKey booth because they're about to. Well, for a Tesla. We're about to draw the Tesla.

**Chris Gammell:** Attention. Yeah. I mean, and it's. I don't know. It'd kind of be worth it. But I mean, then you like, look at like this other stuff though. Like, like taking a look at this page that they're doing, like they're giving away a Tesla. Awesome. Right. But then like, they're having like, like Marilyn Monroe and like. Oh, they've got lookalikes. Michael Jackson lookalikes. It's just like, what? Johnny Depp. This is just like a big, big conference thing. You know, there's going to, this is going to be like tons of booth babes and all like the, the crazy practices, a big, you know, it's just like a big trade show filled with not just engineers either. Like there'll be a lot of engineers and I'm looking forward to that. But mostly I'm looking forward to, you know. Right. The seeing new stuff. Not necessarily.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Pulling up.

**Dave Jones:** No, it's going to be huge. I'm sad I'm not going to be there.

**Chris Gammell:** Yeah. Next two years maybe.

**Dave Jones:** It's bloody Germany. Yeah. That's a long way for you.

**Speaker ?:** It's Germany.

**Dave Jones:** So. Yeah. That's like, if you think the US is a long way, try going to Germany. Yeah.

**Chris Gammell:** Well, yeah. You got to go the other way, right? Man.

**Dave Jones:** Yeah. Yeah. It's pretty horrendous. Yeah. It's 24 hours on a plane each way.

**Chris Gammell:** Yeesh. Yeah.

**Dave Jones:** That's not including like stopovers and things. Yeah.

**Chris Gammell:** Gross. Yeah. So I'm excited to, so I've never been to Germany before. I want to meet a lot of, if people are listening, I know that a lot of our audience is Germany, in Germany.

**Dave Jones:** There, yeah. A lot of it. It's probably our second most popular. If it's anything like my blog, it's the second most popular. Mine goes US, Germany, UK, Australia.

**Chris Gammell:** Yeah. Yeah. I think it's very similar to that.

**Dave Jones:** In terms of popularity. I'm sure it would be.

**Chris Gammell:** So if people are going to be there, definitely let me know either in the comments section or find my email address and send me an email.

**Dave Jones:** Do we have new Amp Hour t-shirts? Are we going to do a new run of Amp Hour t-shirts so they can wear them?

**Chris Gammell:** Oh, we can't.

**Dave Jones:** Can we get them in time?

**Chris Gammell:** Oh, no. We won't get them in time. So.

**Dave Jones:** No, but if we run it for like a campaign only for like the next three days or something. Yeah, but the shipping's always late.

**Chris Gammell:** It takes longer too. So. I'll take a look at it. We'll see.

**Dave Jones:** No, no. Try it. Try it. Let's see if we can run another campaign. Actually, I wouldn't mind another one. You know, the sandstone color one. Oh, yeah. Sand colored. Sand colored. Is that the only one we've done? No, no. No, we've done black, right? Yeah. No, we've done the black too. Yeah. But you can auto rerun the campaign. Sorry, you can auto put down your name for these shirts again. Do we have a link on the website to the shirts or?

**Chris Gammell:** No, we have a store that people can buy them at. But again, that's not very fast. So we'll try and figure something out. That's a good idea though. We'll try and figure something out. And yeah, I don't know. I need to get stickers or something too. I've been meaning to do stickers for a long time. So.

**Dave Jones:** I've got stickers. I don't think anyone's bought them.

**Chris Gammell:** Right. Sometimes you've got to give them away.

**Dave Jones:** Right. No one's going to buy stickers. Yeah. Exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, goodness.

**Chris Gammell:** So yeah, I'm looking forward to that though. It should be interesting. I'll be at a bunch of the Hackaday events as well. So. Should be a good time. Sweet. Yeah. So what else is going on next? Yeah. I started using my motor kit again. Remember how I was doing that for a while? The motor stuff. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** You're spinning things. Yeah. Spinning things. So actually someone had written, I forget who it was. Someone had written very snarkily in our comment section about how I should just get a voltage, a step up voltage transformer. Right. And I was like, oh, yeah, that works. So I bought one on Amazon. Yeah. And actually they suggested one. And I got that one off Amazon. So as a recap, what the problem was is basically 120 coming in, 120 RMS coming off the walls in the US. That's like 170, 180 peak. And so you put that through a rectifier. So you get about a little bit less than that because it drops. Right. So you get like a 170 volt DC bus off a rectifier without any craziness. And then I ended up, all this kit stuff, I ended up needing to buy a different kit anyways in order to get a different microcontroller in there. But I thought that I needed to get a power factor correction because power factor correction also acts as a boost converter in order to boost it up and blah, blah, blah, power factor stuff. But basically I was able to, with this step up transformer now, I was able to step it up to 220 or 240, whatever. And then the rectified.

**Dave Jones:** Yeah, you're a destroyer. It comes straight out of the wall, dude.

**Chris Gammell:** I know. And you guys have tea kettles that heat up faster and everything too, right? But you don't get to, well, it's true. There's like people that complain about that. It was, oh, it was Martin, it was Martin Lorton complaining about that in the States. He's like, he's like, oh, the tea kettles heat up slower here.

**Dave Jones:** It's the same amount of total power available.

**Chris Gammell:** I don't know. You just said that. I don't know. I don't know. And, but you guys can't work on, so like you have to have a licensed electrician work on your stuff in your house too, right? Oh, yeah. Yeah. Yeah. And around here you can. I'm not sure if you're supposed to, but at least you can. I felt the tingle of 120 many times. So anyways, I got, so I got this kid up and running again and then should be, should be moving forward. I don't know. Like I said, like the, that's what I was kind of getting towards before when I mentioned the, the scientist kind of, everything kind of moves down the line towards slubs like me who are just using dev kits. Right. And, and, uh. Right. So I got this thing spinning and I'm like, yay, I did so much. And then I realized that now I really, I really only hook things together. Yeah. Yeah. That's a trained seal who also did the same thing. That's right. Give me a cracker or a fish. Yeah. So I don't know. It, uh, but it's, it's nice. Cause as you like kind of go through, I'm starting to kind of get a better feel for it. You know, you know, like that, well, and maybe you never have this, but like, I was like really afraid of this thing when I started out and I still have a healthy fear of the voltages and stuff like that. But just as you start to use it more and more, you kind of get normalized to it and you get, you know, you kind of understand more of the, you know, the dip switches that are on board and stuff like that. And that can really, that can really end up helping you, uh, when you're, when you're trying to troubleshoot problems after the fact. So, so that has been useful so far, but now it's the, now it's the tough, the tough work of, uh, making it work properly and turning it into something else. Yeah.

**Dave Jones:** Good luck. Have fun.

**Chris Gammell:** Thanks. Spinning stuff. If, if people are listening at our motors people, I, I still, I still appreciate help. So.

**Dave Jones:** Noob.

**Chris Gammell:** Yeah. Hmm. Guess what?

**Dave Jones:** Guess what segment we won't have on the show anymore.

**Chris Gammell:** What's that?

**Dave Jones:** Workbench of the week.

**Chris Gammell:** Oh yeah. We haven't done that in a long time. We don't need to.

**Dave Jones:** It's on Reddit.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** It's on Reddit. There's a new subreddit called Workbenches.

**Chris Gammell:** Not that new, but, uh, it's, it's pretty awesome.

**Dave Jones:** Well, it's there. Yeah. It's like a workbench point. Post your workbench.

**Chris Gammell:** Yep. Yeah. So it's, there's some good ones on there. Yeah. One post a photo of their workbench. Uh, and, and, you know, there's actually a, uh, one for not chip of the week, but it's called new chips. I think. I think that's another one that's on there. And that, that kind of acts as a, uh, as a proxy for chip of the week. And right. So it's not new chips. It's something like that. Nice chips. That's what it is. Nice chips. Yeah. Right. So Dave, we're slowly being replaced by Reddit, I suppose.

**Dave Jones:** Right. Okay. We'll just be, yep. Uh, we'll end up as just random text on a, out, from out, out of some bot. Right. Somewhere, which then translates it into audio.

**Chris Gammell:** Just like on that, uh. In that video.

**Dave Jones:** Hackaday project. Yeah.

**Chris Gammell:** Speed it up and.

**Dave Jones:** Welcome to the app. I'm Dave Jones from the EV blog. Oh, goodness. Yep. That'd be so bad. You would know what I've got a inkling for. What's that? I'm going to have to dig out my old, uh, voice, SBO256 voice synthesizer chips from back in the eighties. I still got one or two hanging around and I want to hook them back up.

**Chris Gammell:** What, what, what was that number again?

**Dave Jones:** SBO256.

**Chris Gammell:** Is that like the one that's in the speak and spell from TI or what's, what's the, uh.

**Dave Jones:** I don't know if it's in the speak and spell, but it's the same era. Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** It's a similar era.

**Chris Gammell:** Yeah. Those kind of did go away. Didn't I mean like you don't really hear those anymore. I mean, well.

**Dave Jones:** Well, there, there, there is a new chip available. There is a new, I can't remember the name offhand, but it's a very similar kind of sounding one and it hasn't improved. Um, you can get like really advanced ones, you know, from the big manufacturers, but there's like super expensive and complicated. Right.

**Chris Gammell:** And at a certain point you just put a single board computer in there and have that.

**Dave Jones:** And you don't want a human voice. You want a computer voice.

**Chris Gammell:** Yeah. It depends on the, it depends on the era of project, right? I mean. Oh yeah. Yeah. Of course.

**Dave Jones:** Totally. But anyway, so there's the, um, I think it's the SBO256 and then there's the SBO256AL2, which is the speech allophone chip. Right. Anyway, there's one, there's one that takes, yeah. Cause if you've only got the bare chip itself, then you have to know how to put the speech allophones together to make up a certain word.

**Chris Gammell:** Yeah. What are those called? Like, so there's like the sounds are, are they aliens or something like that? I remember there's like a very discreet. Allophone.

**Dave Jones:** Allophone. Allophone is the name of a thing. I thought it was like a phoneme or something like that. Yeah. It's a phoneme or whatever. Yeah. Yeah. We're talking out our ass again, but yeah. Anyway. So there's also a matching chip, which I've also got somewhere, which then, um, it takes ASCII input and then it's got a built in table and it knows how to pronounce those words. So it translates the ASCII into, uh, you know, speech, all of the, yeah. Then it sends the commands directly to the actual speech chip, you know, cause there's like, you know, 30 of these, you know, phonemes or whatever built into the chip and you can make up any word with those 30 odd. Right.

**Chris Gammell:** It's basically replicating sounds that the humans can make, right?

**Dave Jones:** And you can make up any, you know, word with those little, that wasn't accurate by the way, folks. I don't go sampling that. Okay. Okay. Now we know. And, uh, yeah. And, uh, yeah. So, but you know, and it's a bit of an art to know how to put those together to form a certain word, whereas this chip's already done it for you and it knows how to convert ASCII. It reasonable, you know, it does a, it does an okay job or it does a 1980s. Okay. Yeah. Right. Right. Do you want to play a game? Yeah. Shall we play a game?

**Chris Gammell:** Yeah. So did you actually use these in projects or was it just like you buy one and you try it and then you're like, yeah, okay.

**Dave Jones:** Oh, I just, yeah. I built a, you know, I built a board, hooked it up to a PC and, you know, and I could, um, send, send commands from the PC and I could make it, uh, talk from the PC port.

**Chris Gammell:** Is there any practical use for it though? I mean, like.

**Dave Jones:** Oh, no, no. You know, you build it into, you know, like a doorbell, you hit a doorbell and it, you know, speaks and, you know, just boring, you know.

**Chris Gammell:** Well, cause I mean, there are practical implementations of this, like, you know, from the single board computer side of things. Like, so like, uh, I, I finally found a use for Google glass. Uh, I'll be.

**Dave Jones:** Only, it's only taken you two years.

**Chris Gammell:** It only took me two years. Yeah. Uh, but I'll be, I'll be, uh, you know, freaking people out in Germany and, uh, wearing them for, uh, for like translations. Granted, everybody. And what's the use? But basically. Oh, you're using it for translation. Yeah. It'll do on the fly translations. I have a, a MyFi where I'll be able to buy, um, uh, uh, SIM card over there. And then basically if I get in a situation where I, I need to speak German, which is unlikely. I mean, everybody speaks English over there, but.

**Dave Jones:** Can't you just buy an app for that? You don't have to use Google glass. Can't you get an app on your phone that. Oh yeah. You definitely don't have to. Ask somebody to speak in it.

**Chris Gammell:** Yeah. Yeah. You can definitely do that.

**Dave Jones:** I haven't tried it.

**Chris Gammell:** Don't take this away from me, Dave. I'm just saying. Right.

**Dave Jones:** But that is, I mean, like there are, I mean. Like speak into my glasses. Right.

**Chris Gammell:** Like lean up towards my eyes. Yeah. That's right.

**Dave Jones:** Get close to my face and speak.

**Chris Gammell:** Right. Uh, yeah. No, uh, but, uh. Fail. But I, I think that, you know, there are practical, like, like even just the app side of things, you know, on the, on the, the software side, there are practical implementations of that these days, you know, for translation app type things. There are, that's a practical use of it these days. It's, it's moved out of the hardware realm just because of, it needs to do more than that. But that's pretty interesting. Cool. So, uh, you think you're gonna, you're gonna pull this chip back out, start exercising it and make it say.

**Dave Jones:** Yep. I wanna see if it still works after 30 years. Yeah. Yeah. That's it. And, um, yeah, I'll build it up on breadboard and see if I can shoot some data at it and make it talk again after 30 years. That'd be, that'd be awesome. Yeah. I'm pretty sure I've still got the chips somewhere. Like, you know, I've got like an old chips bin somewhere, you know, that has, you know, yeah. And, uh, so you used to be able to buy these things at Tandy Radio Shack for you, US folk, you know, you went in there and they would hang on the rack, would hang in a plastic, you know, one of those blister plastic containers would be the chip that had the speech sheet and it had the full data sheet in the back, you know, and everything. Yeah. It was, you know, that's how you bought your chips.

**Chris Gammell:** I was cleaning up my, uh, I was cleaning up my lab yesterday or two days ago and I found a blister pack of what looks like maybe 10, one and nine, one, four diodes. Uh, that I probably paid, I probably paid $2 for. Back in. Oh, it is 10. Yeah. It's a package of 10. Uh, and, uh. Nice. I'm probably going to save it just because I know I'm never going to buy that again. And, uh, I don't know if Radio Shack's going to be on long enough to even have the option to, so. Right. Have it in a place of honor. Somewhere on the, somewhere on the bench.

**Dave Jones:** In your lab, which is currently at 49.44% humidity and 73.0764 degrees Fahrenheit.

**Chris Gammell:** Yeah. Fahrenheit. Yeah.

**Dave Jones:** I'm looking at your, you've got one of these, uh, imp, um, modules.

**Chris Gammell:** Yeah. So this is actually Luke. Uh, Luke had posted this on our subreddit a while back. Basically he built, uh, just a little tiny, uh, little tiny board there, uh, just as a, so for some, um, Silicon Labs chip, basically just an I squared C. And then he wrote some code for the electric imp and, um, basically real simple setup. And then he's got, uh, I think we might've talked about it a couple weeks ago, the imp.guru. So basically using the SparkFun data collection, like you could point your SparkFun basically to collect data directly and then it'll broadcast that data out. And then the imp.guru is like a, a graphing platform you can build on top of it. Uh, which seems like a lot of platform. Cause you still have to go through the electric imp service as well. Right. Cause, cause electric imp basically it's like a, a single URL that you could just keep pinging. Right. So I think that the SparkFun, the way I think it happens is I think the SparkFun thing pings that URL and then tracks the data and then spits it out in a friendly format. And then the imp.guru basically, uh, graphs it. You takes that data and then graphs it, uh, with like standard graphing APIs. So a lot of steps, but, uh, it, it works and it was really fast to set up.

**Dave Jones:** And now it's awesome. I think they're sending me one.

**Chris Gammell:** Uh, yeah. Luke said he's sending you one. Um, right. It's really creepy.

**Dave Jones:** So yeah, I've, I've, I've got one I've had, but I haven't had it hooked up. I've got like a, hang on here. It's right here.

**Chris Gammell:** Okay. Good radio again, Dave. Hang on.

**Dave Jones:** Oh, yeah, I know. Fantastic radio. Here we go. I've got it in my hands. It's a Pokeys. A Pokeys? Pokeys. P-O-K-E-Y-S. It's a Pokeys 56E.

**Chris Gammell:** Okay.

**Dave Jones:** And it's a POScope.com. P-O-Scope.com. And it's, yeah, it's a little, uh, uh, Ethernet, uh, processor and it's got all sorts of, you know, IO and it's got a temperature sensor board. And if I hook it up to, um, the Ethernet, um, I believe I used to log the, uh, data and, uh, humidity, uh, temperature and humidity in my lab here. Um, and it's got a separate five volt supply. You hook it up. But I think it's like, I think the service it used is now gone.

**Chris Gammell:** Ah, right. Which is always a problem, right?

**Dave Jones:** Yeah. It was the same thing as this, right? It was a graphing service that used some third party graphing service. And then I think they were bought out and merged with somebody else. And now it's like broken and doesn't work. Yeah. I think. So it's like, yeah, thanks. You know?

**Chris Gammell:** Right. Right. Which is always an argument. I mean, obviously that's, this has the same thing, right? Electric Imp, it goes through their service and now the SparkFun things there, the ImpGuru things there. So yeah, you are definitely dependent on that stuff and, you know, so.

**Dave Jones:** And, and it's not a matter of Imp folding. Like if, like in this case, and like that, that they could get bought out and then people who buy them out have other intentions and they change the service. And so it could be simpler than that.

**Chris Gammell:** I mean, Electric Imp tomorrow could change their API, you know, and how that stuff happens. And it's like, if it doesn't ripple through the chain. Yeah. I mean, that's just a, that's just a software issue always. Right. I mean, like, go try and start up a, you know, a, I don't know, an old windows machine and try and get on a network or something. I don't know. Like there's, there's always stuff like that. Right. Okay. Drivers and everything else. So yeah. Yeah. But like you said, I mean, if you're expecting this data, it's, it's, it can be difficult. So yeah, like I said, it's creepy. It's super creepy. Why is it, why is it creepy? Well, okay. So you could see on this graph and people could see this too. I, I was thinking about taking it down on my.

**Dave Jones:** It's just temperature and humidity. It's not like I, it's not like a live webcam. When are you going to set up a live webcam, by the way? I've done.

**Chris Gammell:** Yeah. I don't know why you do that. That's, that's extra creepy.

**Dave Jones:** Yeah. But. Yeah, I know it is, but that's, that's the business I'm in, isn't it?

**Chris Gammell:** Yeah, I suppose so. Yeah, I mean, it's a, I've said that before. It's like technology voyeurism, right? It's like basically people want to see what you're working on. And I, yeah, I mean, that is, you're right. That's totally part of the thing. Okay. So if you zoom out, if you hit load more data and you zoom out to like a day's worth or two days worth, you can see when I'm in the lab, like that's creepy to me. Like you can see, I start my day normally about 10 AM. And that's like when I go turn, as soon as I turn the lights on, the temperature changes, the humidity changes, everything. And, and the thing is that all of this stuff acts as a proxy, right? And this, this is actually interesting because it's like, it basically is the, like we, we, we've talked and complained and talked about Nesk before, but like, basically this is, this is the, this is the reason, right? It's a proxy for everything that's happening in your environment. Temperature is a great proxy for that kind of stuff. And, you know, it knows when you're home, it knows when your heat's on, it knows when your, your lights are on, like all of these things, you know, everything can be, all these behaviors can be back calculated and, uh, you know, not necessarily for nefarious purposes, but for some purpose. And so if you're.

**Dave Jones:** Totally. Yeah. Yeah.

**Chris Gammell:** So.

**Dave Jones:** No, if, if, if people want to know when to rob my lab, it's not hard. Right. Right.

**Chris Gammell:** Right.

**Dave Jones:** Yeah. There's a webcam there and it's all recorded too, even creepier. So you can actually log in and go through my entire archives and it'll even tell you on a timeline when there's movement in my lab. So you can go, oh, this is when Dave actually was in the lab doing something. So this, this is drop cam. This is drop cam. This is, this is, this is a drop cam.

**Chris Gammell:** Which was also bought by Google shortly after. Which is. Yeah. Exactly. Right. And, and so like, that's what it shows, right? Like all of this data, right? So it's like just data, data, data. And, uh, I never quite grasped, you know, how this stuff is valuable, right? I mean, like it's valuable to energy companies, it's valuable to security companies, it's valuable to consumer companies, right? All of this stuff.

**Dave Jones:** To the governments, NSA, and everyone.

**Chris Gammell:** Oh, I mean, it could be, it could be way dumber, right? Like think about, uh, okay. So now you have a group of people that buy a Nest thermostat or buy a drop cam. Well, not a drop cam. That's the Nest thermostat, right? But, uh, they're trying to now do data for like, like, I forget what that service is called where they call your house and ask if you're watching certain television programs, right? That doesn't work for certain age groups, right? They just don't either have landlines or they can't be called or, you know, they don't watch television, you know, when it's, they record stuff or they watch the streaming, that kind of stuff. Like, like that's relevant to Nelson's, Nelson's ratings. And like, it's, it's relevant to them then, right? They're trying to see when people are home, right? You could slice and dice this data. God knows how many ways. Oh yeah. It's just, it's crazy. I mean, like, and this is, I mean, this is what it is talking about. Like, and I guess up until this point, I didn't quite get it and, uh, had to see the fact that you could tell when I'm in my lab and, uh, yeah, I mean.

**Dave Jones:** It reminds me of the movie, uh, Sneakers, uh, the line from, uh, Sneakers, it's all about the, it's all about the data.

**Chris Gammell:** The data. Yeah.

**Dave Jones:** It's all about the data. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** You gotta, yeah. Little bits of ones and zeros.

**Chris Gammell:** Yep. No, I mean, it is.

**Dave Jones:** And, uh, totally.

**Chris Gammell:** So it's, uh, it's gonna, I don't know. I guess, I guess it's not that big of a deal to me. It's creeping you out. I still have it published. So I really can't complain. You need to go off the grid. No, I can't complain because I have this stuff, right? I mean, I live on Twitter. I, I have this stuff published.

**Dave Jones:** Yeah.

**Chris Gammell:** I have no room to complain at all. I get it. But, uh.

**Dave Jones:** You are a public figure, you know?

**Chris Gammell:** Yeah. Right.

**Dave Jones:** You choose to be a public figure, right? Right. Right. Right. I mean, yeah.

**Chris Gammell:** But I think, you know, when people talk about privacy stuff, you know, like it's more and more, it's going to be an interesting, um, and what it's really going to come down to is just trade-offs between, um, you know, the benefits people get from something like a nest that, you know, is figuring out when you're home and when to set your heat accordingly and your energy savings, blah, blah, blah, blah, and the backend data sales type of stuff. Right. So that's, that's what people will trade. I do want to mention, since we talked about the imp, uh, I did get to also try the spark. Have you ever tried that one?

**Dave Jones:** Oh, yes. Right. Yes.

**Chris Gammell:** Uh, I like that. It was, it was a great little, you know, it was nice.

**Dave Jones:** Yeah. Yeah. Yeah. It's neat.

**Chris Gammell:** Same kind of thing. It's like, yeah, I'm actually not sure. So with the imp, we, we talked to Brandon, Brandon was on the show. Um, and so we, we know how that hooks in that has a little led blinking programming, um, or the photo receptor rather on the board. And then you blink your phone in front of it. Uh, I'm not sure how the spark does it. Do you know how that actually gets onto the wifi networks?

**Dave Jones:** On the top, top my head. No, sorry.

**Chris Gammell:** The only thing I could think is maybe like the, the spark is act like, so it's got like a CC 25, not 25, whatever the, the, I think it's got the TI chip on there, the wifi chip.

**Dave Jones:** The TI one. Right. Yeah. Okay.

**Chris Gammell:** Uh, yep. And the only thing I could think is that it's acting as like the host to start with, like the, the device on board and then my phone hooks into that. Oh yeah.

**Dave Jones:** It can, it can hook directly. You, you, you don't need a PC. It can go straight onto the wifi network and straight out.

**Chris Gammell:** Wait, which ones, which can go straight on the network? The spark. Spark can go straight on the network. What if it's got the password though? That's what I don't understand. I didn't understand how the, the credentials, cause I had to pass it credentials. Right. And that's, well, that's always what the hard part is with, well, not the only hard part, but one of the hard parts is getting, getting credentials across. So I didn't, I didn't know how that happened. Cause that's, yeah, that's a lot of these connected devices are like that. Um, but it was a great interface. I mean, so it's got a little Android app basically, you know, could just tap and turn stuff on. I didn't know about the, you know, the wider usage of being able to script stuff. And, you know, I'm guessing it's, you know, I know it's Arduino compatible, so you could, you know, get some kind of interface.

**Chris Gammell:** But, uh, yeah, I mean, great, great user experience. That first blink experience is kind of pretty important, right? I mean, so I've talked about the bean, which is Bluetooth. And then the, the, the, the imp is, uh, wifi and then, um, Spark. So all those things, I mean, it's, it is important as a first experience too, because you have people that are coming in from the IT sectors and elsewhere, software, stuff like that, you know, they're targeting those people and trying to get them kind of soft shoot into the field. And, and so that's really important to get that stuff going first and, you know, get them up and running.

**Dave Jones:** I'm wondering how many of those, it's, it's like the early PC era, right? How many of these companies are still going to be around in 20 years time?

**Chris Gammell:** Oh.

**Dave Jones:** I'm curious, you know, like, it's almost impossible to say. Like standalone? You know, that's. Yeah. Like, you know, are, you know, imp going to be still making their modules in 15 years time?

**Chris Gammell:** I'm sure they are. I, I can almost guarantee it's going to get bought. I mean, like.

**Dave Jones:** Oh yeah. You're right. Every, see, everyone's going to get bought out. Yeah. I mean, like. And all changes. Consolidation.

**Chris Gammell:** I, I, I hope that all of them go to, you know, I think that's the, the companies that go the distance and, and stay, you know, stay the course and do their own thing. Like those are the really good ones, right? I mean, like you don't see that as much because it's tough, right? You, you know, it's, it's tough when you're offering big payouts like to, to not. Oh yeah. Autonomy. Don't worry. Don't worry. MakerBot. Sorry. Couldn't help myself. And you know, it's, and it's, of course, why wouldn't you do that? Especially if you have investors that want to be paid.

**Dave Jones:** But aren't a lot of these companies deliberately set up from the get go to make, to turn it into a huge business corporation. So that's their natural progression, right? Like, I, I don't think there's many of these that actually, oh, I'm just making one of these in my garage and, oh, I might put it on Kickstarter. Yeah. I got 10,000 bucks. And then I grew and grew and grew. And you know, I, a lot of these are starting from scratches. Yeah. You know? Yeah. I'm going to do a startup. It's the startup culture.

**Chris Gammell:** Well, yeah. But I think the difference is if the, if they're looking to get acquired, not even looking to get acquired, but just like the difference is, do they want to jump out and do something else? Right. Because I think.

**Dave Jones:** But everyone who does a startup is looking to get acquired, aren't they? Otherwise, what are you? Like, I think it's got to be like 90, it's got to be 90, 95% of them. Surely.

**Chris Gammell:** I think, yeah, you're right. A lot of that. But I think, you know, some of them, they want to be in it forever. Right. I mean, like, but like, that's the difference, right? The, if you think about like, I, so, so obviously I worked at Keithley, right? And Keithley in year 50 and Keithley was eventually bought, but Keithley in year 50 was very different than Keithley in year five or year one. Right. You know, like, and, and some of the people that were there, uh, one of the apps guys was there the entire time, you know? And so he saw that whole difference and it's, it's a radically different culture from the beginning to the end. And, and, you know, I think one of the things with startups especially is like, you have people that kind of thrive on that adrenaline of, you know, do or die kind of stuff. And as you get into the more stable years of growth and, you know, maybe not trying to acquire, but trying to get your revenue streams up and stuff like that, it's a, it's just different stuff, right? You start having meetings, right? You start having structure and, you know, it becomes a corporate culture. Yeah. And it does by necessity, you know, it's just, so I don't know. I, I, I think it's awesome when companies do that, but it's, you know, those companies are way different. Like Google is started way different than it is now. Right. Google is big company now. So, okay. You know, you think? Yeah.

**Dave Jones:** Goodness Christ.

**Chris Gammell:** I think the interesting thing too is, so I forget that there was one other thing I was reading about with people being outside, you know, cause like there's all these startup centers now too, you know, there's Silicon Valley and Silicon and San Francisco are kind of, and then New York and Boston and all these other ones. But actually my friend, Ken, who runs tiny circuits, he wrote an article about being based in Akron actually. And I think it's interesting because when you, when you move outside of those big centers then too, like doing the startup thing is not quite the same either. Right. So he wrote, and he writes about that and you, you know, trying to find people that are in that startup mode are, it's, it's a harder thing to find those people. And then, you know, trying to grow in that, that way, you know, heart's hard to get funding. And, and of course the benefits are there. So what is the, yeah, go ahead.

**Dave Jones:** What is the bottom line? Why did he stick to Akron, Ohio?

**Chris Gammell:** Akron, not Akron. Akron. Akron is like, it's about half an hour south of here too. Yep. It's, so he, basically the bottom line was because he's from there and he knew he could do it. So he does tiny circuits. They have that tiny screen Kickstarter going on now too. Yep. And, but basically it's a difference in culture. He was writing about like the, the, you know, basically everybody leaves the Northeast Ohio area, which is true. Some of us come back. Right. But, you know, like it's a, it's a different mindset and kind of see if he could, right? Obviously there's other benefits, like you could buy a house for the cost of a VCR.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** And, and places like Akron and Cleveland, there's a lot of industrial infrastructure that's there that, you know, there's a lot of other cities like this where there's like, you know, from prior eras, there's, there's infrastructure that you can build on top of. It's going to be a little rundown.

**Dave Jones:** But with, but with today's global, you know, the global village or whatever they, you know, call it, you know, the global marketplace, you can do it from Antarctica. Right. It's like, it doesn't matter where you're based. Seriously. And unless you're one of the people who like, you know, networking, you know, like, like being in Silicon Valley, cause you're around other like-minded people, blah, blah, blah. Right. Apart from that factor, you know, you can do almost any startup from anywhere in the world.

**Chris Gammell:** I think the, and I, I think that he talks about this a little bit, but one of the biggest things, one of the biggest limiting factors, I think, is actually talent. Right. So like trying to get other people to work there.

**Dave Jones:** Well, that's if you want to hire someone.

**Chris Gammell:** Well, yeah, of course. Yeah. If you want to work in your basement, you can work in any basement. Right. I mean, like that's.

**Dave Jones:** Yeah. But once again, do people have to be there with you? No, they don't. You can just subcontract everywhere. Everyone works, works remotely.

**Chris Gammell:** And I don't know, man. So I've been doing, I've been working remote now for a while and it's, it's different. You know, it's a different thing. Especially like when you're moving really fast, like, like when you have time differences, when you have, you know, like, like you hear people talking about working with China too, right?

**Dave Jones:** Yeah, but it's possible. Right. But it's possible.

**Chris Gammell:** Yeah, of course it's possible. Right. I think, I think software is a little better suited to distance and hardware, you know, because you, like you could ship, you could ship software with a click. You can not ship, you know, you have to go down to your FedEx, your UPS to overnight something in order, you know. That's right. Between hardware people. So, but, so you're right that people can work remotely, but I think, I think that in terms of hardware, I think that it does depend on, you know, being a talent pool, right? I think that, I think that is probably, probably one of the bigger things. Granted, I mean, you know, there's software, there's few, very few hardware projects are without software these days. So maybe you could be a hardware small team in one area and then, you know, have software. Oh yeah, totally. Totally. But same things apply. I mean, how about, so I don't know if you saw this story, Jerry, Jerry and the technical illusion team.

**Dave Jones:** She's, yeah, they've, they've, they've moved to Silicon Valley because they got funding. They got some extra funding.

**Chris Gammell:** Yeah, well they got funding, but also because they couldn't, I talked to Jerry about it. She said they couldn't, they couldn't, they could find good people in Seattle for hardware and they could bring people to Seattle for hardware, but not enough. Right. Right. And that's what it comes down to. That's why people keep going to the Bay area because it's just like, there's so many hardware people there and just, not even just hardware, but just talent around that space.

**Dave Jones:** Yep.

**Chris Gammell:** That's hard to find. I mean, that's why people go to Shenzhen for manufacturing, right? It's hard to find. Oh yeah, of course. That critical mass stuff and, and it really can matter a lot. So, um, yeah, I think that's, I mean like, so like Ken wrote about, about Akron and he's right. I mean, like he, he gets like, like these sweetheart deals on like, on, on industrial space. He's got huge amounts of space and, you know, three phase power for doing, um, reflow and stuff. And that's great. But, uh, you know, it's hard.

**Dave Jones:** But if there's no one there to fill it. Yeah. Right.

**Chris Gammell:** And it's just, you know, this stuff is more spaced out and everything. Now granted, like, you know, it's cheaper here, but there's always those. It's trade-offs.

**Dave Jones:** So, yep.

**Chris Gammell:** It's, uh, it's, it's tough. Business. Oh goodness. Business is hard. So is hardware. Hardware is hard. Blah.

**Dave Jones:** Everything's hard. Yeah. Even blogging's hard.

**Chris Gammell:** Blogging's hard. Yeah.

**Dave Jones:** Keep telling yourself that, buddy. Speaking of which. Yeah. I have to hire help.

**Chris Gammell:** Oh yeah.

**Dave Jones:** But I can't because I'm in, yeah, I'm in Borkham Hills.

**Chris Gammell:** Oh yeah.

**Dave Jones:** Who the hell is in Borkham Hills? Nobody.

**Chris Gammell:** You can get someone to, uh. Can't get good talent. Yeah. Right. Borkham Hills. Maybe you can get someone to commute out there.

**Dave Jones:** And I don't, and I, and I don't have enough space. I can't afford enough space to, to fit someone. I can't fit another person in the lab here. Yeah. She's not enough room for me.

**Chris Gammell:** Maybe they should just work remote, Dave. What, why, why can't you just have them work remote?

**Dave Jones:** They should work remote. Oh no. Oh no. Because see, video blogging's a different business.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Well no, it's the same thing, right? I mean, you could, you could go and overnight someone, a USB drive with, with video on it. Right. And that would be like, effectively shipping hardware. You know, like, just because of bandwidth costs and, and bandwidth limitations.

**Dave Jones:** Yeah. Yeah. But I've got to produce hundreds, essentially hundreds of products per year.

**Chris Gammell:** Oh, that's where we're going here.

**Dave Jones:** Video is a product. Yeah. Yeah. I went there, dude. I went there.

**Chris Gammell:** Oh my God.

**Dave Jones:** Each, each video is a product. Each video is a product. And it has the full life cycle development of a product. Oh man.

**Chris Gammell:** He's really reaching here, folks. I am shouting back on this one. Totally legitimate. Shouting back. Totally legitimate. No.

**Dave Jones:** Each one has to have back and forth. It has to have the same, not to the same depth, but it's got a similar thing to developing a product.

**Chris Gammell:** Oh my God. Dave's videos are the, are the, are the, are the, are the, are the, are the, are the, are the, are the no silk screen, no solder mask, single sided boards of products. Yeah, they are. Of video.

**Dave Jones:** But still, I had to make it.

**Chris Gammell:** More of a prototype. We'll say they're prototype videos. Yeah, they are.

**Dave Jones:** Oh goodness. Anyway. On, on that note, I'm going to call it quits because we're over our amp hour. We are over our amp hour. And I got to go finish my bloody reverse engineering video before people start screaming. That's been a week since I've released a video. Yeah. Well, good luck.

**Chris Gammell:** Which by the time I get it up probably has. Good luck on your new product, Dave. Your new product.

**Dave Jones:** Thank you very much. New product.

**Chris Gammell:** Next week we will have, we will have Bill Hurd of Commodore fame. He was one of the designers or the designer of C128. It might be the designer. Yep. And, uh.

**Dave Jones:** B, I think.

**Chris Gammell:** Yeah, he's been doing videos for Hackaday. I get to meet him at the Hackaday event. Uh, super, super interesting dude. And he's working on some new stuff that's real fun too. So, I'm looking forward to that.

**Dave Jones:** Sweet. Absolutely. Yeah. PC retro week.

**Chris Gammell:** Retro. Yeah, definitely. Very cool. Awesome. All right, man. Talk to you then. See you then. Bye. Bye. Bye.

**Chris Gammell:** Bye.

**Speaker ?:** Bye. Bye.

**Chris Gammell:** Okay, Glass. Google. How do I say this technology is not necessary in German? Diese technology is nicht e-foli-deck. E-foli-deck. E-foli-deck. E-foli-deck. E-foli-deck. Ha ha ha.
