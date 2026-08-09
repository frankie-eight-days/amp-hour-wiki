---
episode: 197
title: Spacing Out On Space - Dave's Dongle Designing
url: https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/
---

**Chris Gammell:** This is the Amp Hour Podcast. Recorded May 5th, 2014. Episode 197. Dave's Dongle Designing.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Hey dude, sorry I missed last week.

**Chris Gammell:** Oh, that was, well, more mic for me to talk to. Did you get a chance to listen to that yet?

**Dave Jones:** I did actually listen to at least the first half of it. Yeah, it was good.

**Chris Gammell:** Man, that guy.

**Dave Jones:** He knows his stuff.

**Chris Gammell:** I feel like my brain would melt if I would have sat in a room with him for like a couple hours past that, you know?

**Dave Jones:** That's it.

**Chris Gammell:** Some people said I did okay talking about software. I don't know if, I don't think I really did. I think I faked it a little bit.

**Dave Jones:** I think you did okay on the parts I listened to anyway.

**Chris Gammell:** There was a lot of faking it.

**Dave Jones:** Right, yeah, yeah.

**Chris Gammell:** Man, that sounds crazy though. So hopefully we can have him back on at some point. He did say, we talked after the show, he said he's going to be in Sydney, or not in Sydney, but in Australia. But I think he said Brisbane and...

**Dave Jones:** Oh, I checked his schedule. Yeah, he's doing everything but Sydney. Yeah. Actually doing everything but Sydney and Melbourne. Yeah, he's doing like Perth, Adelaide, Brisbane. Yeah. I don't know why. I presume he's done in Sydney and Melbourne before. Yeah, that's what he was saying.

**Chris Gammell:** He said he's been out there a couple of times. Right. Sydney's old news, you know? Right. There's nothing to do there anymore. He's already looked at all the stuff. He's tried to buy offices. That hasn't worked out. No, no, that was you. You were trying to buy an office. That hasn't worked out. So what's going on with that?

**Dave Jones:** Well, did we talk about that? Yeah, we talked about it a couple of weeks back.

**Chris Gammell:** Yeah, well, you were talking about possibly doing it, you know?

**Dave Jones:** Yeah, possibly a workshop space and things like that because, you know, I wanted to do it as sort of an investment kind of thing and, B, I get shit internet here and maybe, you know, if I moved somewhere else I might be able to get better internet. You know, that was the plan, but by sheer accident, I was able to get in contact with a guy who runs his own little internet, you know, business internet, doing exactly that, getting internet into, high-speed internet into businesses like mine, right, in big corporate office buildings. And he runs this little company. He's actually a real estate agent and he got so fed up with not being able to get decent internet in the buildings he was in that he started his own little company to, you know, buy fiber space and stuff like that and, you know, repackage it and resell it and install their own D-SLAMs and stuff like that. So anyway, got in contact with him and as it turns out, my current building that I'm in now, who knew, already has one of their D-SLAMs in the basement. So, yeah, like this was one of like half a dozen buildings in all of Sydney that was wired up, that was already wired up for his particular cheap plan. And it's like double the speed and half the cost of anything, of the next nearest one I could possibly get here. And for those who don't know, get in office, fast office internet here. And by fast, I mean like 10 meg, 10 meg, okay? So yeah, stop sniggering everyone in Romania and all the other countries that can get fiber to their doorstep, right? But yeah, and that cost, if you go through Telstra here, it's $8,000 a month, right? Jesus. Or if you go through a more sensible provider, it's $1,300 a month, right? For 10-10. And I could get wireless. We also have a wireless dish on our roof and I can get 10-10 through that. And it's only $800 a month plus GST, you know? Right, right, right. But that's what you've got to pay in Sydney. That's how ridiculous this country is.

**Chris Gammell:** Yeah, well, I think that's a big thing, you know? Did you see that video? It's a huge deal. It was made by, I think it was a Dutch company, but it was made by an internet provider. And basically, it was like showing what lag looks like in real life. Did you see that thing?

**Dave Jones:** No, I haven't. Have you got a link to that?

**Chris Gammell:** They took a, it was a video, so it'll take a little while. But they took Oculus Rift and then they put a forward-facing web camera and then they piped that through Raspberry Pi and they basically just programmed in lag, like 300 milliseconds, three seconds. Yep. And that affects us too, right, on the show. I mean, we have that kind of problem all the time. Ours is more geography-based, but it's sometimes also traffic-based. And it's just hilarious to see people do that kind of thing, you know? When that impact is there, I mean, three seconds is a bit extreme, but, you know.

**Dave Jones:** Oh, they're very extreme. Yeah, you wouldn't, with three seconds, hey, that's the round trip to the, isn't that the flight time for audio to the moon? Is it? Like, it's ridiculous. I think so, like, there's a, isn't there, or it's a 10-second delay.

**Chris Gammell:** I know, it's eight minutes to the sun, I know that. I know that that's the speed of light to the sun.

**Dave Jones:** Right, yeah, yeah, it's eight minutes to the sun, yep. Yep. I think it's like, it's like, yeah, like seconds to the moon. Oh, I don't know. Anyway, here we go. No, come on, Google, Google will always answer everything. Yeah, okay. Yep.

**Chris Gammell:** As you said, three seconds, I was thinking three minutes. So, actually, that does seem to make sense scale-wise, then. Three seconds sounds better than... Yeah, but eventually you're going to run into the speed of light, right? That's always going to be... Yeah, well, it's...

**Dave Jones:** Exactly. So, anyway.

**Chris Gammell:** So, you're still looking, huh? Okay, no. Yeah, so that sounds cool. So, you're going to stay there, though. You're going to trick out your lab a little bit more and put in...

**Dave Jones:** I'm going to stay here, and because the place we really liked was very expensive. I mean, it was pretty opulent for one person. But, you know, 2.56 seconds. Yeah, you were right. There you go. All right, cool. Yeah, there you go. I know my space stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** And I think that's each way, though, but anyway.

**Chris Gammell:** Okay, okay.

**Dave Jones:** Yep. Yeah, so I'm going to stay here now in my 50 square meters and make more efficient use of it. Because I used to do all my editing at home, right? Because that's where my faster internet was, so it made sense. But now I'm going to move that here, because this is where I'll have the fast internet. And...

**Chris Gammell:** Yeah, and it does impact. It does impact. Yeah. I didn't quite realize that either, you know, until I'm sitting here doing the same kind of thing. Obviously, this is not necessarily electronics related, so usually video people are more interested in this kind of stuff than electronics people. But, you know, it impacts how fast you can get stuff up on the web and show what you're working on. Yeah, of course. And any time spent delaying, you know, it's just less time that you can be shooting video and putting stuff up on the web. So...

**Dave Jones:** Well, even for this show, like, after we do this, I zip up the WAV file, which I record locally, and I send it to you. And, like, that takes, like, freaking an hour or something. Yeah. To send the damn thing.

**Chris Gammell:** 900 megs, it's zipped up. Yeah. It's, like, 300 or something, so... Yeah. Yeah, it's still pretty slow. Yeah. It's still...

**Dave Jones:** So, anyway, you should be able to get it in about five minutes now, I think.

**Chris Gammell:** Sweet. Anyway. Yeah. Yep.

**Speaker ?:** Yep.

**Dave Jones:** So, anyway, that's going to be installed this week, and I get 8.8 for starters, and then they're going to install a new fiber to the building. That'll take a month or two, and then I'll be able to sign up to 2020, hopefully.

**Chris Gammell:** Awesome. Awesome. Awesome.

**Dave Jones:** And it's only, in quote marks, $375 a month for...

**Chris Gammell:** Bargain basement.

**Dave Jones:** ...for the 2020. But, yeah, no, seriously, for Australia, office internet, that is a bargain. Yeah. So, yeah. So, anyway, I'm very happy.

**Chris Gammell:** Yeah, man.

**Dave Jones:** Happy as a piggy mark. Well, assuming it all works, so, anyway. Right. I'm planning on it working. Right.

**Chris Gammell:** Well, you've got to plan for success, right? You've got to...

**Dave Jones:** Exactly. Exactly.

**Chris Gammell:** Yeah, you've got to be ready for it.

**Dave Jones:** And we were talking about... I was going to also set up a little mechanical workshop here. And you were saying before the show that there's this craze in Japan where they've got all these miniature little lathes and all sorts of workshop-y type gear.

**Chris Gammell:** Yeah, actually. So, I was talking to Todd Bailey. So, Todd Bailey, guest of the show a couple weeks back, he came to town. We had some beers. It was a good old time, you know, talking electronics and all good nerdy things. And he mentioned that he had visited Japan because we were talking about the markets and everything else. And he was talking about Akihabara. And he said that there was, like, a trend for small tools. Like, so, like, tiny drill presses. Like, and we're not talking, like... Like, I have a desktop milling machine, right? Yeah. But, like, smaller than that, even, he was saying. And, like, tiny band saws and tiny circular saws... Or chop saws, rather. And, yeah. So, you might be able to... Sounds like you need to take a trip to Japan, Dave.

**Dave Jones:** Hey, there's this thing called the internet, dude. Internet shopping. That's true. Online shopping. That's true. You just feed in your credit card and magically... I've heard about this. Turns out.

**Chris Gammell:** Well, you know, you could... You and anyone else could win a wonderful trip to Akihabara or space. You could. If only you enter the Hackaday Prize.

**Dave Jones:** Which you are intimately involved in because you work for Supply Frame. And I am intimately involved in because I am a judge. So, I'm one of the ones you've got to suck up to.

**Chris Gammell:** Yep. Yep. Or not. You know, whatever works. Well, yeah, so that's our...

**Dave Jones:** Just produce something good.

**Chris Gammell:** That was the big news last week was... So, Hackaday is running this contest and basically the winner gets to go to space and we're announcing at Electronica and it's very, very exciting. So, I really hope that a lot of Ampower people will think about doing it because the other thing is that it's... The other thing that I was really interested in with it is that one of the biggest parts of the contest is the openness factor, right? So, the more you publish about your project... Yep. The more that you produce meaningful code, right? You could just slap a label on anything and say, oh, it's open, right? And it's like, well... Right. And it's like, well... And, oh, my schematics are up there. But it's...

**Speaker ?:** Right.

**Chris Gammell:** You know, if it's garbage schematics, if there's no documentation, if there's no comments in your code or anything like that, then it's open, but who cares, right?

**Dave Jones:** Right.

**Chris Gammell:** So...

**Dave Jones:** Well, it's open, but it's poor quality.

**Chris Gammell:** Right. Right. And so... Documentation.

**Dave Jones:** With these contests, as was said before, it's all about the documentation.

**Chris Gammell:** Yeah. Oh, yeah. It definitely is. And that's why we got experts like Dave and Lamore and Alicia and Jack and basically and Bunny and everybody else. And basically, you know, they're going to be able to help us kind of figure out which is legitimate documentation, that kind of stuff as well, and the level of openness. So that's going to be good. But I really do hope that Amp Hour folks throw their hat in the ring. I mean, it's going to be pretty sweet.

**Dave Jones:** Well, somebody commented... Well, quite a few people actually commented that, oh, you know, oh, don't bother entering because I stand no chance of winning because the winning idea will have to be so freaking awesome that you can't possibly compete. Right. You know, somebody's probably been working on something for five years and they go, ah, I'm almost finished it and it's ground world beating and, you know, I'm going to win this thing. Right, yeah. And, you know, how do you compete with your little project? Well, it's all about the novel idea. I probably suspect the person with the coolest idea might win. And obviously, if they've got shit documentation, they may not. But, you know, I mean, it doesn't necessarily have to be big and complicated and, you know, it's just got to be clever. Right.

**Chris Gammell:** Well, I think... You know, so when we were setting this whole thing up, I kept referring back to the 555 contest, right? And thinking about similar kind of things, right? And it's exactly what you're saying there, right? People had circuits that they submitted that, you know, they were just circuits and some of them were cool, but at the end of the day, it was just a 555 doing something, right? It was always the ones that were doing something interesting. Like, remember Le Domino? Do you remember that one? Yeah, yeah. It was like 555 with like blinkies that actually like set up a little domino and you could like configure them and they were like modular, plugged together kind of things. Like, that was... That is novel and it was well documented and it was, you know, it was artsy, I guess. I mean, like everything about it was cool. You know, it was just... That's the kind of stuff where it's... It's not... It wasn't technically, you know, super crazy. It was just a, you know, just a 555 blinking light out and then receiving it, right? Yeah. That was basically it, but it was the application of that technology that was really interesting.

**Dave Jones:** Or there were really cool builds or something like that, you know, because you used a hundred 555s and you built something in a normal way. Where is that guy after all? He disappeared...

**Chris Gammell:** Alan disappeared into Valve and he never came back out. We got to dig him out of there. That's it. Maybe. Yeah. We'll get him. We'll get him, folks. Don't you worry. Oh, goodness. He's doing good. Him and Jeff and everybody else, they're all doing good stuff there still, so...

**Dave Jones:** So while something like that could win the 555, I don't think just a clever build will win this one, I suspect. That's just my original... That's just my gut feel. I suspect it's just more of a clever idea and implementation than, you know, oh, look, I built a, you know, big walking robot or something like that. But if it doesn't connect, it doesn't... Right. Yeah, yeah, yeah, yeah. Sort of...

**Chris Gammell:** Well, and that's the thing. Like, so the real goal there, too, was, you know, one thing we talked about. Is the hope that it's not just, like, this is, like, a project that's, you know, gets paraded around and thrown away, but also that the technology is reusable, right? So either the person... That's it. ...could take it and kickstart it, or, you know, there's a bunch of good libraries in there that can be built upon. Like, you know, there's just a lot of interesting things like that that are not usually rewarded in contests that we wanted to reward as well. And things that actually benefit the world, right? I mean, like, if it's a cool-looking project and someone goes to space, that's cool, right? That's good for that person. But if it's a cool project that also goes on to sprout new technologies and gets fed into other projects, and that person goes to space, then that's even better.

**Dave Jones:** Like, you don't even... Like, it probably doesn't even need to be a real finished, polished product. If you came up with some new whiz-bang, you know, image algorithm or something that does, I don't know, connects to the cloud and does all sorts of weird and wonderful stuff and it's going to change the world, then you don't... You know, that on its own could be enough to win it.

**Chris Gammell:** Right. That's why... I mean, and that's why we have technical judges too, right? The ones who can understand the in-depth side of things like that.

**Dave Jones:** The merits of the originality of the idea and the implementation and what potential effects it could have on the industry.

**Chris Gammell:** Right. Yeah. Right, exactly. Yeah, it's not just... I mean, it should work, right? That's important. But does it work and has it not been done before? That's pretty cool. Is it open? Exactly. Is it shareable? Like, all of that stuff. Yeah. Like, it's easy to imagine, like, this nebulous idea of, like, what you said right there, like an image algorithm that's never been done before, right? That recognizes when a mouse runs across a screen or something. I don't know, something weird like that, right?

**Dave Jones:** Yeah. And it does it in 10 milliwatts, you know, of processing power or something, you know? Yeah.

**Chris Gammell:** And then you get Jack Gansel looking at it and he, you know, goes crazy about it, like something like that, right? Yeah, yeah. Yeah, exactly. Right.

**Speaker ?:** Right.

**Dave Jones:** So, although it is a hardware design contest, you could win it with not much hardware. Well, yeah, yeah. That's probably what I'm saying, you know?

**Chris Gammell:** Well, we talked about that too. And I think the real question is, are there any hardware design contests these days or any hardware designs, really, that don't have some software component, right?

**Dave Jones:** Exactly.

**Chris Gammell:** And...

**Dave Jones:** Or a massive amount of software component. Yeah.

**Chris Gammell:** You know? Right. Right.

**Dave Jones:** Because hardware is almost commodity these days. Yeah, you know, because you can whack a Raspberry Pi in something and you've got all that processing power.

**Chris Gammell:** Right.

**Dave Jones:** You know, it's like hardware is pretty commodity these days.

**Chris Gammell:** Well, it's going to be what you stand up around it, right? That's not necessarily... Yeah, yeah, of course. Yeah, there's a lot of cores.

**Dave Jones:** It's the idea you put around it. Right. It's the idea and the implementation that you build around it. Right, exactly.

**Chris Gammell:** And you want to do that too because you think about how much time it takes to get all that stuff done. Yeah. If you had to start from scratch, right, and you're like, oh, you can't use Linux. Oh, okay. Well, how much stuff is this really going to do now? But now it's like, okay, you could use a BeagleBone Black, you can use Linux, you could build custom hardware on top of that. Like, what can you do then? It's like, man, you could do anything. I mean, like, honestly, that's kind of the point in history that we're getting to is like, you know, you have so many libraries to build off of. And it's not like the implementation is easy that you're doing that. It's just like, there's so many giants whose shoulders you're standing on. You know what I mean? Like, there's just so much, like, existing technology. And if you build something that continues, you can continue to build on, you know, and continue to abstract out different elements, then that really benefits everyone. And then you go to space.

**Dave Jones:** And then you go to space. It'll be interesting to see if the winner actually takes the prize.

**Chris Gammell:** I hope so.

**Dave Jones:** Have you guys actually talked about the odds of somebody actually winning this and taking the prize instead of the cash equivalent?

**Chris Gammell:** No, I haven't really talked about that. I mean, personally, I, you know, you just really, really, really hope they do. I mean, like, like, I understand. Like, you know what I mean? Like, a lot of people look at that and be like, how could I pass up the money? If you know, if you feel like if you're working on something, you're in debt. You know, it's like, okay, yeah, you know, you might do that. But if there's any chance, you know, you gotta go, right? I mean...

**Dave Jones:** But the thing is, by the time this contest finishes, they still won't be able to go, right? Right.

**Chris Gammell:** Yeah, there's not like they hop on a plane the next day. It's like the...

**Dave Jones:** No, they have to wait at least a few years. So, you know, the contest will be long gone and forgotten by the time this person gets into space.

**Chris Gammell:** No, you know, I was reading up on that too, because there's a couple different providers and stuff like that at various levels. They, Branson was on a flight...

**Dave Jones:** Yeah, but you name one who's... Yeah, but are they close to even getting into space?

**Chris Gammell:** Yeah, he was on a rocket flight in February, I believe. It's on the wiki page.

**Dave Jones:** Oh, it was?

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, really?

**Chris Gammell:** I thought so. Maybe I'm wrong. But yeah, I mean, that's what I'm pretty sure.

**Dave Jones:** Yeah, but it didn't go into space, did it?

**Chris Gammell:** I don't know. I'll link it in. I looked at it quickly, but yeah, you're right. There is a little bit of... There will be a little bit of lag, but I mean, like, basically, it's like a Kickstarter, right? Yeah, yeah, yeah. It's a Kickstarter for going to space. But yeah, you know, you'll get a ticket to go to space, so pretty cool. And there's a bunch of other stuff too, so it's going to be great. It's going to be great.

**Dave Jones:** So, yes, people, don't be scared off by thinking that your little project can't win. Right. You know? Right, exactly. It's all about the idea. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** And there's lots of other cool prizes. Like, as you said, go to Japan.

**Chris Gammell:** Yeah, yeah. Yeah. A bunch of different things like that, experiential type stuff. And then also, you know, gear and things like that. So, yeah, man.

**Dave Jones:** I had ideas for lots of cool space-related prizes. Yes. Which I'm surprised you didn't have more space-related prizes. But I'm a bit of a space buff, so...

**Chris Gammell:** Yeah, you kind of, yeah.

**Dave Jones:** I kind of nerded out on some of the possibilities. Right, you kind of did a little bit. It's okay. It was excitement. That's good.

**Chris Gammell:** That's good. Oh, boy. So, speaking... So, you and I have been going back and forth a little bit. We kind of fell off on this, but we talked about it two weeks ago with the portable lab idea. We were talking about the guns a lot, of course, and stuff. Yep. Excuse me. We've been kind of...

**Dave Jones:** And everyone said you're just a crazy hero. Yeah, yeah, yeah. Yeah, but go on.

**Chris Gammell:** But... So, I found an interesting sub-genre of carrying cases that actually might work and fit the bill. It is...

**Dave Jones:** They're makeup cases, aren't they?

**Chris Gammell:** Makeup cases, yeah.

**Dave Jones:** Have you got a link to these? Because I haven't seen them yet. I just saw it before the show.

**Chris Gammell:** Yeah. I just... I just... Here we go. Is it in Reddit? Here we go. I'll send it to you right now. Here we go. All right. And, like, it seems to make sense, too, right? It's like... You know, there's, like, these makeup artists have lots and lots of little fiddly bits, right? They have lots of individual items. Oh, wow. Look at that. Like hand tools. Yeah, yeah, yeah. And they have, like, you know... Basically, it kind of sets itself up for having parts and bulk stuff.

**Dave Jones:** It's a portable tool chest.

**Chris Gammell:** Yeah, exactly. Right.

**Dave Jones:** It's already a portable tool chest.

**Chris Gammell:** And it's built, like, a piece of luggage, which is crazy. So...

**Dave Jones:** Yeah, yeah. Yeah.

**Chris Gammell:** So that's why I'm really interested in it. And there's a couple other ones, too, where, like, there's, like, fold-out legs and it actually stands up on a table, too. I don't know which one would work and which one would hold up, but I don't know. It's...

**Dave Jones:** Oh, and it's got, like, a drawer that pulls out with those Constantina fold-out... Yeah, exactly.

**Chris Gammell:** ...tool things.

**Dave Jones:** And, wow. Yeah. Look at that.

**Chris Gammell:** So this is the kind of thing that I'm targeting for that. And, you know, you think about the build-ins you can do. The only thing I'm not sure about is, you know, if I put, like, a Rhygol in there, right, which is what I was thinking I would probably do, like, put a Rhygol on the bottom of that thing. You know, you don't want it to be get trounced around, right? You know, like, I just wonder how much of this stuff actually gets held in there.

**Dave Jones:** Well, it doesn't. That... You'd have to put, you know, foam inserts for everything and...

**Chris Gammell:** Yeah. Okay. Well... Yeah. I could do that, I suppose.

**Dave Jones:** So you would have to customize it.

**Chris Gammell:** Yeah. But this is a good starting point, so...

**Dave Jones:** No, this is a... This is a really good...

**Chris Gammell:** So go makeup artists. And that's what surprised me. It's not like... It's not like there's one. It's like... Like, I was looking at, like, you know, roadie cases for, like, bands and stuff like that.

**Dave Jones:** So was I. That's what I was looking at. And they're all just empty boxes. Yeah. Well, they are because... All their racks. Like, I was looking at those rack mount ones. You know, you get those 19-inch racks in the portable things. And, well, yeah, they're okay, but...

**Chris Gammell:** But they're not as... You know, there's no... They're not, like, human portable. It's like, you need, like, a... You need a van to transport that stuff, right? It's not like you put it on a plane, whereas this is... Right. Yeah, yeah. Plane... Well...

**Dave Jones:** This one has the wheels built in and the pulley handle and the, you know... Yeah.

**Chris Gammell:** Yeah. So... Yeah. Yeah. I don't know. That is ongoing. Me and Dave have a Evernote notebook going back and forth, keeping track of links and stuff. So if people have other ideas, we'd love to hear them. An ongoing amp hour collaboration.

**Dave Jones:** But this one's got Wynn written all over it. Yeah.

**Chris Gammell:** Well, I might just have to buy it and see what it feels like. You know, it's going to be a lot of, like, feel and how much it holds up and sturdiness. Oh, of course. Yeah, yeah. Totally. Those hinges look a little wimpy.

**Dave Jones:** So do they come in different size... Like, you can get different size ones and...

**Chris Gammell:** Yeah. Oh, yeah. Yeah. If you... And, you know, it's like anything else. Right. Just like electronic components, right? You know, it always comes down to finding that key search term, right? If you don't know what you're looking for at first... Of course.

**Dave Jones:** Exactly. You'll never get it.

**Chris Gammell:** You'll never get it. You know, like... And that's actually what usually... Usually my tool for that... Of choice for that is typing in something generic, right? So, like, rolling luggage in this case into, like, Google image search. And then you try and just scan it. Google image search, totally. Yeah. And then when you see something that looks good, then you figure out what it is. Yeah. What sub-genre it's in. And then you're like, okay, now it's a makeup rolling case. And then you find this whole... You know, and then there's all the copycats in China and stuff like that.

**Dave Jones:** It's the old visual catalog method. Yeah, exactly. Right. When you didn't know what sort of multi-way connector you wanted, well, you'd just flick through the Farnell or the DigiKey visual catalog, right? You know, back when we had paper. And you would flick through and you'd go, oh, that looks like the kind of connector I want. Oh, I had no idea it was called that. Yeah. And then, bang, you've got the...

**Chris Gammell:** Right. Yeah, especially when it's coded for, like, some, like, military number, right? And you're like, oh, jeez, how would I ever found that? Right. Yeah, and it's either that or you talk to an FAE and you're like, well, I need something with, like, molded and it needs a grommet and five pins.

**Dave Jones:** Well, who there... Like, if you wanted a multi-way PCB connector, you wouldn't know that it's a DIN 41612, right? DIN straight, I wouldn't. Which is the standard industry term, right? That's the industry standard connector for multi-backplane plug-ins. It's been the standard for, like, 30 bloody years or something, right?

**Chris Gammell:** Right, yeah.

**Dave Jones:** And there is no other name for it. It's a DIN 41612. Yep.

**Speaker ?:** Right?

**Dave Jones:** And, well, yeah. If you didn't know that, you'd probably never find it unless you search visually.

**Chris Gammell:** Did you know DIN stands for Deutsche Industrial... I have to go to N is, but it's because it's a German standard. I think I might have mentioned that on the show before. Yeah. That always cracks me up. Right. Yeah, so that's... I mean, yeah, you have to search like that sometimes, too. And, you know, I think that's actually when a lot of the, you know, innovative solutions come through, too, because it's never like... It's never like, oh, well, you know, Chris is designing something. He did it the same way they've been doing it for 30 years. How innovative. It's like, no, Chris went to go design something, and he borrowed something from a different industry, and it just happened to fit well, and now it's a much better solution, right? And then new solutions spring up around that. That's where a lot of interesting solutions come from, I think, when you do cross over into different areas like that.

**Dave Jones:** Yep. And it comes in pink.

**Chris Gammell:** Sometimes it also comes in alligator and pink. Yeah.

**Dave Jones:** Alligator skin.

**Chris Gammell:** So, another thing we talked about with this was possibly rolling in, like, an Android tablet and then having, like, a USB-based scope. So, I was looking around for that kind of thing, too, and I did find one that I hadn't heard about, and I don't think it's anything, like, super crazy special, but it's the first one I found that kind of fit the bill. It's called the Aussie Prime. Have you heard about this? The Aussie Prime, I've heard of it. Yeah, there's a thread on the EEV blog forum, actually, I found as well.

**Dave Jones:** Yep.

**Chris Gammell:** And, you know, it's not like crazy specs or anything, but it's open source hardware, it talks to Android, and really that's what I'm interested in, is having something that can pass through and talk to a tablet and see if that's even possible right now, and if there's an app already written, because I don't want to do that kind of thing. So, uh...

**Dave Jones:** But, you know, I still... I'm still of the opinion that you should just find the smallest bench scope you can get and shove it in there. You know, I'm still of that opinion.

**Chris Gammell:** Yeah, no, and that's why, you know, that's why I was talking about the Rigel before as well. I mean, I think that's a good idea too. But, you know, what it actually came down to was thinking about all of these scopes that are out there, and they all have fans, and they all vent, right? And thinking about how it just... You'd have to do, like, ducting to get the venting out if you're going to pack it into foam. Whereas with a dev board type solution, you know, this is effectively... Yeah. ...this OSCE Prime is basically a dev board plugging into a tablet. It's a ventless solution, right? Yeah, yeah.

**Dave Jones:** But, yeah, so you've got to build a box around it. You've got to, you know, have a power supply for it, and you've got to do all that sort of jazz, so... Right. Well, and that's what it comes down to. And this portable lab's got to be mains powered anyway, because you've got to have that soldering iron in there. That's true. You know, like, you want to... Because our goal here, right, is to have it as a semi-proper lab. Yeah, right, yeah. You know, it's like, you know, that isn't, you know, like, a spare no expense kind of, you know, at least you've got decent tools in there that you'd have in a real lab. Right. So, none of this, you know, portable butane-powered soldering iron rubbish and all that crap, right? No, no, somewhere where you can pull out and you can do SMD work, and you've got a proper temperature-controlled soldering station, which means mains, and, you know, you've got a proper scope with proper probes, and, you know, it's got the full range, and you've got a SIG-Gen, and you've got, you know, yeah.

**Chris Gammell:** Yeah, well, there'll be a trade-off there somewhere. It's not like you're going to have a, you know, Tech 465 in there or anything, but it's... No, no, no, exactly. Yeah, there will... Yeah, I guess you're right. I mean, I just, I think that having, you know, if there was a good trade-off for, you know, depending on what kind of work you're going to be doing, too, right? I mean, like, if you're going to...

**Dave Jones:** I think you should just whack one of those handheld scopes in there. I mean, those, you know, there's quite a few, you know, the Handtech brand handheld scopes, they're pretty good. They're pretty decent. They've got, you know, like a gig sample. They've got, like, a mega memory there. They're pretty decent. And they've got, you know, proper full-range attenuators on the input. That's the problem with these little USB scopes. Right, right, right. It's always the front end. A couple of ranges. It's always the front end, right? And, but these, you know, these Handtech portable scopes and other brands that are out there now, there's a bit of a booming industry for those. And they're doing them right now. You know, the user interfaces still might leave, and the control layout might leave a bit to be desired, but they're, you know, streets ahead of what handheld scopes used to be.

**Chris Gammell:** Right, right.

**Dave Jones:** Back in the day.

**Chris Gammell:** Wait, so you're saying handheld, though, or you're saying USB-based?

**Dave Jones:** They're handheld. Handheld. No, they're handheld. Oh. Type in, Handtech is a popular one at the moment, I think. Handtech handheld scope.

**Chris Gammell:** Handtech is a USB scope I have sitting right next to me. That's why I was wondering. Ah. So, they do have a USB version as well, but I'm-

**Dave Jones:** I might be thinking of a-

**Chris Gammell:** But you're saying, you're saying, like, one, like, a field portable kind, right?

**Dave Jones:** A field portable, yeah. They're, like, quite large, you know? Yeah. Like, they don't quite fit in your hand. They've got, like, a carry strap, like, or two carry straps. And you sort of hold them as, like, one of those military tablet kind of things.

**Speaker ?:** Yeah, right, right, right, right.

**Dave Jones:** You know? They've got, yeah. So, they're- But they're smaller than a bench scope, yet they're still fully featured. Yeah. Like a-

**Chris Gammell:** Yeah, they've got tactile buttons, too. That's nice. Yeah.

**Dave Jones:** Yeah, yeah. They've got proper buttons and things like that. And, you know, I think, yeah, when, you know, if I build my little portable workshop, that's probably the first choice I'd put in there. Huh. Okay, I'll have to look at that. So-

**Chris Gammell:** Yeah, DSO. I'm looking at DSO 1200, 200 megahertz. DSO 1200, yeah.

**Dave Jones:** Yeah, exactly. Interesting. Yep. Huh. Yep.

**Chris Gammell:** You ever used one or no?

**Dave Jones:** And look, you know, no, no, I haven't used this model. Yeah, it's only, like, $359. So, it's, like, Rigol price. And that's dual channel 60 megahertz, right? So, that's sort of Rigol-y type price.

**Chris Gammell:** Cool. You know?

**Dave Jones:** So, yeah.

**Chris Gammell:** All right. I'll check that one out next. Yeah.

**Dave Jones:** I reckon they've got Wynn written all over them. So, yeah, I'm quite excited about that portable workshop idea. Yeah. Right. But I think, you know, do we sort of, you know, if we standardize on it and we release, like, the plans for it, is that the plan for this thing? So that everyone can sort of go, oh, look, someone's already put in the hard work. I'll build one of those. You know?

**Chris Gammell:** That would be a really good idea, too. Because if it did become a standard form factor, then what you could do is, as people spin up new hardware projects, they say, oh, well, there's a slot in the, you know, in the Porto case thingy, right, or whatever it's called.

**Dave Jones:** Right. Yeah, yeah. Yeah.

**Chris Gammell:** And it needs this. I'm going to design for the Porto Lab, right? And...

**Dave Jones:** It could be the standard Porto Lab. You know? Yeah. I think we should go out and actually get to PortoLab.com.

**Chris Gammell:** Well, we better do it right now.

**Dave Jones:** Right now, before we upload this episode. PortoLab.com. There you go. And, you know, it'd be nice if there's, like, a standard that every, you know, it was so well documented and the parts were readily available in all the countries and knew exactly how much it was going to cost to build and kit one out.

**Chris Gammell:** Well, it makes you wonder how much need there really is for this kind of thing, though, too, right? I mean, we think that that's necessary, but maybe this is just a boyhood dream, you know?

**Dave Jones:** Well, I can see it being necessary, but I just see it being fun as well. But I know for a fact that I've talked to a lot of people who have, you know, severe restrictions, especially, you know, we talked about students in dorm rooms and stuff like that, severe restrictions on, you know, what sort of lab they can set up. So if it's just, like, a little portable wheelie case that just sits in the corner.

**Chris Gammell:** Yeah, that's true.

**Dave Jones:** You know, that's got wind written all over it.

**Chris Gammell:** Yeah, man. Plus, they can put Ampire. We'll have to get Ampire stickers now.

**Dave Jones:** There's probably even a business out there for... Right. Yeah, you put them on the side. So there's probably even a market out there for selling, like, fully built and finished units. You know, it's probably a small niche market out there for that.

**Chris Gammell:** Yeah. Maybe vanishingly small.

**Dave Jones:** Vanishingly small, but hey, I don't know.

**Chris Gammell:** Well, you definitely need a portable lab if you still worked at Altium, right?

**Dave Jones:** Oh, yes, you would. My hat's off to that self-aware. So what is the deal here?

**Chris Gammell:** Have you been looking at this or no?

**Dave Jones:** I've had a look into this. And, yes, out of the blue, as always, in true Altium tradition, not even the employees knew, apparently. Yeah, just out of the blue. Oh, man. They've upped and they've announced that. We're moving out of China. We're going to the United States of America. So they're moving their headquarters. I've got a – we'll have to link it in, but I've got a post on the forum where I translated their press release into English. I translated their – I should actually call it up and I'll go through it. Yeah, because it had so many wank words in there, you know, and you could – it was so easy to read between the lines of what they were. Yeah. You know, what they were actually doing. So here it is. I'll call it up. Altium moves again. Here we go. We'll link in. You want me to send you the link? Sure. Yeah, that'd be fine. There we go. Done. This is glamorous stuff, which you can't see, audience. You can't see us furiously typing.

**Chris Gammell:** I was going to say, until Dave's uplink changes and he gets 20 megabits and we're – maybe we can switch to video at that point, right, Dave?

**Dave Jones:** Well, we've trialed that before and it was a lot of dicking around, but we ultimately didn't have the bandwidth to do it live. Definitely not, yeah. Because, you know, because this audio sucks up all of our bandwidth. Which is so sad. Because we've – not only do we have to –

**Chris Gammell:** I mean, we're also recording off the server, so there is that. I mean, like, it's not like there's nothing there.

**Dave Jones:** Yeah, we're recording off the server.

**Chris Gammell:** You know.

**Dave Jones:** No.

**Chris Gammell:** That's still what? Just audio. We'll have to do the math on the data at some point, you know.

**Dave Jones:** Anyway, there are a couple of people who have requested that, you know, a live video feed so they can watch us record in the ampere. I don't know why. I don't know either. Yeah, anyway. Our super emotive faces. Anyway, we can certainly do that.

**Chris Gammell:** Yeah, you can see my face hiding behind my new silver portable soundstage.

**Dave Jones:** Right, yes, soundstage or me hitting the mute button and then coughing my guts up.

**Chris Gammell:** Yeah, there you go. Dave's sick pretty much 12 months out of the year now, so.

**Dave Jones:** No. Well, yeah, exactly with the kid. Yeah, yeah. And it's coming into wintertime here. Oh, yeah, it's going to be bad. Yeah, yeah. Anyway, here we go. The translation. Well, I probably shouldn't go through the whole thing. No, it's okay. Yeah, yeah. But, yeah, basically, they're saying, yeah, we're taking the next step in our growth strategy by relocating our R&D and headquarters to San Diego they're going to, by the way.

**Chris Gammell:** That's, can't really pick a better place in the States, I do have to say that. I mean. Really? Okay. Oh, dude, San Diego is beautiful. I'm going to be out there in June, actually, for vacation.

**Dave Jones:** I've been to San Diego. I thought it was a, I wasn't that impressed.

**Chris Gammell:** Oh. Dude, like, in terms of weather, like, it is, like, the most stable weather in the United States.

**Dave Jones:** Okay, right. Yeah, yeah. And, well, it's close to their existing headquarters, not headquarters, but close to their existing facility there anyway, which is in. I thought they were Palo Alto. Colesbad.

**Chris Gammell:** Oh, I thought they were Palo Alto. I thought the article said they had a research center there.

**Dave Jones:** No, they're north. Okay. No. Anyway. Well, they were. I haven't checked lately, but. Anyway, so, yeah, so the next step in their growth strategy. Translated, that means our move to China was a complete and utter failure. Of course it was, you know.

**Chris Gammell:** There might be a little bit of personal feelings on this one.

**Dave Jones:** No, no, no. Look, like, you know, it's plain to anyone who's followed this story, right? Altium just packed up and moved to China on a whim, right? This was not, it wasn't thought through. It was just on a whim, right? Because that's what Altium's always done. And they thought that they could get, you know, cheap programming talent in China. And that failed. That turned out to be a complete myth. They couldn't. Well, from what I hear.

**Chris Gammell:** So the only thing they got in China. You can get cheap programming talent, like an actual talent, but it's just hard to keep it, right? Yeah, yeah. Anywhere in China, it's just hard to keep good talent around because everybody moves around so much.

**Dave Jones:** And it's not cheap. And if it is good talent, if it is, like, really top-notch talent, which is what Altium wants, right? Yeah, of course. Altium have always hired the top-notch employee. It's very difficult to get a job at Altium, especially in the programming side of things. Yeah, hardware to add anyone, right? You really have to be top-notch. Right, yeah. And, yeah. And basically, if you can find someone, they don't stay.

**Chris Gammell:** Yeah, right, right.

**Dave Jones:** You know, they will move in three months. So, you know, by the time they've gotten up to speed, they're gone. And so that's why they've done a lot of their programming in the Ukraine now, which is probably a bad move at the moment. Oh, geez, yeah. With all the... A little bit of unrest, yeah. Yeah, with the Ukraine crisis happening. Anyway, I don't know if that affects the Altium employees. But, yeah, a lot of their R&D has been done there since they moved to China. And the China thing only... Well, according to Max's column, he's done a column on this. Clive Max... Maxfield. Maxfield, who we haven't had on the show, have we? Nope, not yet. No. He should be on the list, I guess. He is on the list. Oh, okay. There you go. Maybe he listens to this episode. Hey, Max. Anyway, he... Yeah, it says they've got two teams there in China. One is the library management team, you know, because they do all their libraries there now, or most of them. They used to do some... Their library headquarters used to be in Tasmania, here in Australia. But, yeah, a lot of that's in China now, or most of it. And their Internet of Things, in quote marks, you know, that was their big strategy. Which is another complete and utter failure, and they know it. But they won't admit it, of course, in the press release, you know. It's... Oh, it's been a... You know, they worded it, you know. Anyway, the... Oh, here we go. Their quote, the company has also redefined its Internet of Things strategy to be in alignment with its core business of the development of world-class PCB design tools. Translated, they admit that the Internet of Things is a complete fire. It was the stupidest strategy they've ever done in the history of the company. Maybe not, but it's close, you know. It's one of the doozies. And they've, you know, and they've booted out their former... It was so bad, they booted out their former CEO and founder, and they're focusing back on the core PCB tools, which they should be, which is a great strategy. And this is a strategy that they should be following, of course. Yeah. And they are now. So they're basically admitting, yeah, it was a complete nut of fire. And the other thing, the other rumor going around is that they, Altium, are now starting to lose a lot of business, a lot of their military contracts, U.S. military companies, who did not like the fact that they were in China. Oh, interesting. You know, doing their R&D in China, because apparently there are rules and regulations in the U.S. about how you can deal and what products you can get from a company that is effectively based in China.

**Chris Gammell:** Yeah, it's like export type regulation stuff and supplier, yeah.

**Dave Jones:** Stuff like that. And yeah, things like that. So, yeah. That's interesting, yeah.

**Chris Gammell:** I wouldn't have thought that level would affect it, but...

**Dave Jones:** Well, like it took that 12 months or something for that to really kick home, because when the, you know, by the time somebody in the company, the big military company finds out, oh, they're in China now, are they?

**Chris Gammell:** Well, and plus you have to renew licenses and stuff like that.

**Dave Jones:** You have to renew your license yearly. You know, you're paying your support subscription. So they may have got a, you know, they may have, you know, secretly renewed it for a year without anyone finding out. But sooner or later, somebody in the company finds out and, yeah. Interesting. So rumour has it, yep. So that is rumour. We don't know if that's true, but yeah. Well, we don't know if that's true. We don't know the internal numbers and all that sort of stuff. I've got no idea, but that would not, so I would guarantee you that there is some truth to that. Yeah. I mean, I've worked at companies, you know, said military companies, okay, they're not U.S. ones, but the Australian ones were, you know, fairly strict in that regard. Yeah. As well. Maybe not as strict as the U.S. ones, but certainly, yeah.

**Chris Gammell:** You know, it's interesting with all the military stuff, too, because it goes way beyond. It's not just software. I mean, like, that actually supports.

**Dave Jones:** Oh, it's chips and everything. Yeah, yeah, yeah.

**Chris Gammell:** It supports, like, small fabs and, you know, component manufacturers and, you know, basically.

**Dave Jones:** Yeah.

**Chris Gammell:** There's some crazy stuff that happens with that. There's some stuff that goes around it, I know. Like, sometimes there's, like, importers and they, like, recertify stuff like that. But, yeah, that's just crazy. I mean, like, it was, at least in the U.S., I'm sure the, you know, the rules were written in the 50s and 60s when the industrial complex was, you know, like, and all of the other industry was here as well, right? Now it's just, like, you're looking around, like, there must be a component manufacturer somewhere, right? Right. Why are we paying $45 for a 1K resistor? Right. But it's just the reality of that. I mean, like, it's, yeah, there's a lot of craziness with that. So.

**Dave Jones:** Yep.

**Chris Gammell:** Well, that's too bad. It's, you know, it's.

**Dave Jones:** Yeah.

**Chris Gammell:** It's.

**Dave Jones:** The other thing is that they would have got completely jack of living in Shanghai. Who the hell, when you come from Australia, who the hell wants to live in Shanghai?

**Chris Gammell:** Yeah, there's certain parts that I would like. Nah, man. I mean, hair quality would be a downside. You don't want to live in the city. But, you know.

**Dave Jones:** You've got to move. A lot of these people move their families there. Well, yeah, that's true. Right? And, nah, there was, trust me, there was a huge backlash to that. And ultimately, they lost most of their programming talent because nobody wanted to move there. That's just a big move, yeah. And, you know, they've been there a couple of years. And, yeah, they were, I've heard they've lost another few big people since the time. And they're, you know, getting very few and far between. So they're probably wanting to move back because, yeah, they don't want to lose talent. So it's a whole combination of, you know, reasons that make it obvious that it was obvious to me and everyone else that they were never going to survive in China. They were never going to survive and thrive in China. They always would have made the move back. And my prediction was two years. I think it was at the time. And that's pretty close to, I think. Yes, it's been two years this last month. Yeah.

**Chris Gammell:** Oh, yeah. All right.

**Dave Jones:** Yeah. So I think I'm bang on. Yeah.

**Chris Gammell:** Thanks a lot, Altium.

**Dave Jones:** I'll have to go back and see if I can find.

**Chris Gammell:** I'll have to go back and find my old quotes.

**Dave Jones:** It's, you know. Yeah. Anyway. Anyway. So there, yeah, they're moving to San Diego, which is not the first time they've done it. A lot of people forget that in the 90s, Altium packed up and moved to San Jose in the US. They moved to Silicon Valley because that's where the action is. And then they realized that that didn't work. So they came back to Sydney with their tail between their legs.

**Chris Gammell:** Yeah.

**Dave Jones:** So, yeah. So it's hilarious. It's like a soap opera. It's great. A bit. Yeah.

**Chris Gammell:** I mean, and ultimately what it comes down to is like you just hope that the software survives, you know. It's a good program. Yeah, yeah. It's still a good program, right? Of course. I mean, like that's.

**Dave Jones:** No, no. Yeah. Oh, yeah. No, it's great. Yeah. Even though they have done absolutely nothing on the low-cost version, which they promised all the shareholders.

**Chris Gammell:** Oh, yeah. Right.

**Dave Jones:** So, yep.

**Chris Gammell:** Well, they'll see. Speaking of low-cost CAD tools, there is a change coming for Eagle as well. That's another thing in the news this week. Oh, is it changing? Version 7 is coming out. The only thing. So on Twitter, it was. Sorry. Who was it? Oh, Randy Glenn, who was. He was looking through the terms that have changed. I think because Adafruit is a reseller now and they updated some of their stuff. And basically, it said something about Node-Lock licenses. And so basically, Eagle's switching over to Node-Locked, whereas previously it was just code-based. So enter a code. A serial number kind of.

**Dave Jones:** So if you had five computers in your laptop or you had a computer at home and a computer at the office, you could install them both. You could still do two.

**Chris Gammell:** They said that you could still do two now. I think that's what they said for the new stuff. Oh, right. Okay.

**Dave Jones:** Home. Yeah. You have to allow at least two.

**Chris Gammell:** Yeah. I think that's practical.

**Dave Jones:** Because there's so many people who work at home and office. Right. You can't have them buying two licenses as that. It's just bullshit. So that's a good thing. So obviously, they're concerned about.

**Chris Gammell:** Piracy?

**Dave Jones:** People actually pirating the software. Yeah. Yeah. Apparently. I mean, yeah. They're obviously concerned enough to move to that model. Right.

**Chris Gammell:** And I mean, ultimately, what the discussion came down to this week was like, node lock licenses do not really stop. I mean, it's a lock on the door, right? I mean, like thieves and robbers, if they want to get around the lock, they still get around the lock, right? But I guess this slows it down. But ultimately, it makes it a bit more of a hassle for the users. So that's a downside. I mean, I think a lot of people were overreacting a little bit, possibly myself included. But, you know, it just changes for that kind of stuff. And yeah, we'll see. We'll see what happens.

**Dave Jones:** I can't wait until they go back to hardware dongles.

**Chris Gammell:** Yeah.

**Dave Jones:** Hardware dongles are the parallel port.

**Chris Gammell:** Oh, yeah. I had those for, I was using pads in the past. And pads still uses dongles. Yeah. I mean, that's.

**Dave Jones:** Yeah. I, I, someone wanted me to design him a hardware dongle way back in the day. That was, oh, very early 90s or something. So we're talking, you know, 20 to 23 years ago now. Yeah. And, you know. Do you put that on your business card then?

**Chris Gammell:** Like, Dave, David L. Jones, dongle designer.

**Dave Jones:** Dongle designer. Yeah.

**Chris Gammell:** Dongle designer. That might be going on the show name.

**Dave Jones:** That's it. Okay. Hey, this show will be labeled D. Dongle designer, Dave.

**Chris Gammell:** But yeah. So, I mean. All right. You can make some. It still does exist, right? So, you know. And it's.

**Dave Jones:** Oh, yeah. Yeah.

**Chris Gammell:** I don't know. We'll see. We'll see what happens. I mean, obviously, I'm a big fan of KiCad. There's no hiding that. So, if it gets people to switch. Look, if I change.

**Dave Jones:** If I switch, I'm probably going to KiCad. You know. It's just. Yeah. Yeah. I was trying to think of. That's probably what's going to happen.

**Chris Gammell:** Of a t-shirt to make for Maker Faire. I still might do it. But, you know. Something about KiCad. Right. Because I'm giving talks on KiCad as well. And stuff like that. Okay. So, I need to think of some kind of slogan at some point. Right. It's really weird. For all of the. The. You know. Like, the fact that the code is open source. Everything like that. Like, there's nothing about the logos or anything. Like, the logos are copyrighted. But they're like to individuals. And it's like. I don't know. Oh, right. I don't know how that stuff works. You know. We've talked about that in the past with open source hardware.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Oftentimes, the name is trademarked. And stuff like that.

**Dave Jones:** Hmm.

**Chris Gammell:** I don't. Yeah. I don't know how the logos work, though. Like, I. Like, that whole. Like, if I want to make a shirt with the Kaikad logo on it. You know. First off. Right. I have to figure out which one's the official logo. And then the second off. I have to figure out. Dude. If I can.

**Dave Jones:** Golden rule. It's easier to seek forgiveness than it is to seek permission. Right.

**Chris Gammell:** Well, yeah. Yeah. But they ask on the t-shirt sites, Dave. They say, do you own this image?

**Dave Jones:** I don't know. Oh, well. We're not. I don't know. Yes. I need a court ruling. Yeah. Exactly. Yeah. Oh, man. Yeah. Yeah. So, yeah.

**Chris Gammell:** I do have one t-shirt on the way. It's pretty. I like it. Right. I'll tell you about it after the show. I'll post a picture after Maker Faire's over.

**Chris Gammell:** Cool. I should mention, I'm going to be at Maker Faire. I'll be at Maker Faire. And that's coming up in two weekends. And then Solid Con, which is the Wednesday and Thursday after it. So, I'm actually going to be out in the Bay Area from the 16th through the 24th. So, pretty good chunk of time out there.

**Dave Jones:** So, are you doing this on your own, bad? Or is this a supply frame? A little bit of both.

**Chris Gammell:** A little bit of business. A little bit of pleasure. Yep. So, I'm giving a talk at both. You're just a traveling machine now, aren't you? Yeah. Tell me about it. This is what prompted that whole portable lab thing.

**Dave Jones:** The portable lab thing. Yeah.

**Chris Gammell:** So, I might be jumping ahead here. We'll see.

**Dave Jones:** I guess you couldn't get that together for the Maker Faire, right? That's probably too soon.

**Chris Gammell:** Amazon Prime begs to differ.

**Dave Jones:** Right. Okay. All right.

**Chris Gammell:** I mean, honestly, what I need is not that much in terms of getting stuff done. Because, really, all of the tools we're using for contextual electronics, too, are pretty low cost and pretty small and stuff like that. Right. Pretty fun, actually. So, the Gabotronics, the X-Mini Lab that we've been using, I mentioned on the show a couple weeks ago. It doesn't have an AC mode. And so, I just made my own probe.

**Dave Jones:** Oh, right.

**Chris Gammell:** I just solder. With a cap in line. Yeah, just cap in line. It was great. I was like, oh, yeah, that's like what it does. That's really.

**Dave Jones:** Mr. Analog guy.

**Chris Gammell:** Well, it was just like, you don't think about it. When you're using a scope, you're like, oh, okay, there's a button for it. Yeah. It's just relay with it. Of course. You know, it's dumb. Anyways. Yeah. Oh, goodness.

**Dave Jones:** Yep.

**Chris Gammell:** So, yeah.

**Dave Jones:** So, I will be out there. Right. So, we might see a portable lab out there.

**Chris Gammell:** Maybe. I don't know if I'd be lugging it around with me, though. That's the other thing.

**Dave Jones:** This is really like a Ben Heck style thing, isn't it?

**Chris Gammell:** Yeah. What Ben's done. He's done two different. He's done two different ones already. Yeah. Portable labs.

**Dave Jones:** Yeah. Right. But I don't think that the custom's the way to go. I think really the way to go is the way we're now.

**Chris Gammell:** The way we're moving towards. Have a look at.

**Dave Jones:** You know. An off-the-shelf case that everyone can buy.

**Dave Jones:** It's available in every country. And you can fit it out. And here's the custom foam pieces. And maybe, you know. If you need some 3D printed holders or something. You know. You can make the 3D models available online. And stuff like that.

**Chris Gammell:** Yeah. Right. Right. Right. Yep. Yeah. That'd be kind of cool. I actually started doing SketchUp, too. See if I. You know. Because I can make like metal brackets and stuff now, too. Right. Yeah. Of course. And stuff like that. Yeah. Fun stuff. I don't know. We'll probably fixate on that for a while. And then forget about it. Yeah. Of course. Yeah. As we do. Yep. Yep. So what I was going to talk about. We got. Oh. That's lots of chip stuff. The chip stuff.

**Dave Jones:** Nobody gives a shit about Google Glass anymore.

**Chris Gammell:** No. Well. What about this. You know. There's an interesting trend now happening. Maybe not a trend. But. All of these server companies. So like Facebook. Google. Amazon. They're all cranking out their own chips. And like cutting their own agreements. Basically. Have you heard about this stuff?

**Dave Jones:** Oh. It's been coming for quite a long time. Right. I think.

**Chris Gammell:** But I think they're finally getting to the purchasing side of things. So there's a. There's an article on Wired. Right. About Google's. Google's plans. Right. And I mean. This is like Google has hardware engineers working on this kind of thing. Right. They're actually designing server boards. Yeah. And power supplies. And all the actual hardware stuff. Facebook as well. Yeah. Facebook had that open source. They open source their power supply design. I believe.

**Dave Jones:** Oh. Did they? Yeah. That was like a year or two ago. Right. And aren't Apple buying some, you know, fab which makes. Fab is the wrong word. But some factory which makes, you know, 100 million iPhone screens a year or something. You know. Actually glass foundry type. You know. Which makes the glass. And I read that somewhere this week.

**Chris Gammell:** I think I saw that. But this is chips. Focus Dave. Focus.

**Dave Jones:** All right. I'll stay focused. I'll stay focused. Well.

**Chris Gammell:** The interesting thing though is that Google chose IBM power architecture. So they chose the Power 8 processor. Right. Yeah. Yeah. And this is like after all of this stuff, you know, going away from Power PC type stuff. I mean Power 8 is different than Power PC I believe. But, you know, moving away from that and then Google goes and chooses non-Intel based. I mean like.

**Dave Jones:** Or non-ARM.

**Chris Gammell:** Or non-ARM.

**Dave Jones:** Arm and Intel. The whole world is ARM and Intel. Right. You know. That seems to be what the whole world is.

**Chris Gammell:** Right. So Google is giving hope to other things. I'm guessing what really happened is IBM came in with a good looking architecture and gave them a sweet ass price. You know. And a 30 year contract or whatever the hell it takes to get it done. You know. They just got it done. Yeah. That's right. But I mean when you think about it. When you think about how much hardware these guys are buying. It's. I mean this is some legit amount of hardware. Right. I mean.

**Dave Jones:** Oh. Every cent matters. Every cent in licensing fees matters. You know. Like it's a big deal.

**Chris Gammell:** Yeah. Well. And not only that. Power matters too. Especially for server stuff. Right. Oh. Of course. Power is usually the biggest thing there. Oh. Power is everything. Yeah. Yeah. It's really interesting to see what's happening there. I mean like obviously. You know. It's what maybe. Maybe 10 companies are designing their own hardware for this kind of stuff. And. You know. So maybe a total of 100. 200 engineers in the world actually care about this. But. You know. It actually has a lot of ripples throughout the system. Because. You know. You think about iPhones and everything else. Everything that gets commoditized from the big boys. Right. That ends up affecting us little guys. Right. I mean. When we want to go and buy a chip. Right. And it happens to be on a bomb. Yeah. For an iPhone. You know. That's like. Bunny's talked about that. Right. He actually took the iPhone schematic. And he went and looked through that kind of thing. Um. So when you have that then. You know. That actually does affect us eventually. And it's. It's just kind of interesting. You know. Seeing this. You'd see. It's like looking into the future almost. So. Okay. So. We might be able to get cheap Power 8 chips at some point in the future. Right. You know. You know. So. Same kind of thing. Same thing with the. It happened with ARM. Right. I mean. We can get really cheap. Yeah. ARM chips now. Because. They started pushing them into smartphones. And all the smartphone stuff took off. Uh. That's why. There's so many variations of that now. So. It's just a big game of follow the lead. And.

**Dave Jones:** They even. Um. Amazon. They posted a job for a. Um. A CPU architect.

**Chris Gammell:** Right. Yeah. Apparently. Right. Right. They just design their own. You know. And that's the thing. I mean. Like. There's. There's probably talent in the marketplace too. Right. As. You know. As. These bigger companies. AMD. Intel. Shed jobs. Right. Where are these guys going to go? It's like. Well. They're going. They. Where they can find work. So. That's. Fine with us.

**Dave Jones:** Well. They're. And. Amazon's. Claiming. That they can knock 30% off the price. When they design their own stuff. Straight away. Just off the bat.

**Chris Gammell:** Is that just margin you think? Just. Not.

**Dave Jones:** That's just margin on. Yeah. Because they're doing it themselves. You know. So. There's huge savings to be had here. So. That's why they're. Really pouring money into this. And taking it seriously. Yeah.

**Chris Gammell:** I think the interesting thing. So this article. The. The Wired article. Is talking about. Obviously Google. And. And how it affects Intel. I think what's going to. Honestly be interesting is. Is.

**Speaker ?:** Is.

**Chris Gammell:** If we're going to see. Intel finally. Finally. Finally. I mean. They've started to a little bit. But actually like. Open up the shop. And be like. All right. We're actually a foundry now.

**Dave Jones:** Yeah. Right. Yeah. Yeah. Yeah.

**Chris Gammell:** It almost feels like. It's like an inevitability. Right. I mean. Like as. As they lose share. Overall. Of the computing market. You know. I mean. They're either going to go. And. You know. Start making ARM stuff themselves. But that's probably unlikely. But I would think. You know. Their process leadership. They'd be like. Okay. Well. And they're doing that for Altera. Right. I mean. We talked about that. A couple months back. But. What else are they going to do? Intel's huge. Right. You know. It's just so much money. And. And then. And then. That's the thing though. As soon as it starts to turn a little bit. Right. And then. Amazon has a chip designer. They just go to Intel. And they say. Okay. Well. Now we can make stuff here. And.

**Dave Jones:** One. One. One chip designer. That's all it takes. Well.

**Chris Gammell:** I don't know about that. One man. One chip printing machine. And the rest of the world.

**Dave Jones:** Dream on dude.

**Chris Gammell:** Someone mentioned that to me. They're like. Oh. Someone should enter that in the Hackaday surprise. Right. Yeah.

**Dave Jones:** Oh. Goodness. It. It would win. Yeah. The fact that it's not plausible. Dave would even vote for it guys.

**Chris Gammell:** You hear that? I would. Yeah.

**Dave Jones:** If it was plausible. Yeah. Good luck to you. You know. Spend the next six months designing. Go for your life. Yeah. Oh boy. Yep. File.

**Chris Gammell:** Yeah. So. I guess other. Other stuff in the same kind of vein of this is. You know. So we were talking about Apple. And like all of the. The chip designers there. And. Or all of the. Commoditized hardware that comes from that. The interesting thing there this week was that. I know that a lot of people don't care about the mergers and stuff like that. But this is interesting because. Yeah. Serious Logic buying Wolfson. Right. So that's. That was news this week.

**Speaker ?:** Mm.

**Chris Gammell:** Mm.

**Speaker ?:** Mm.

**Chris Gammell:** Mm.

**Chris Gammell:** Mm.

**Chris Gammell:** Mm.

**Chris Gammell:** Audio only. Manufacturers.

**Dave Jones:** Yeah. They're. They're audio only. Aren't they?

**Chris Gammell:** Right. So they. They. They're like. They make codecs. They make class D amplifiers. That kind of stuff. Mm. And like. You. You asked me to name two. And those would have been the two. And.

**Dave Jones:** Yeah. Wilson. I. I found their chips in like the Kindle. Yeah. You know. The Amazon Kindle. And phones. And stuff like that. Yeah. They. They're. You know. Pretty much own the market almost. That's what I thought. I mean. Maybe there's like.

**Chris Gammell:** Maybe like TI's into that. I don't actually know if TI might be.

**Chris Gammell:** Probably. Yeah.

**Dave Jones:** Yeah. I'm sure they would be.

**Chris Gammell:** Yeah. What is a TI into right?

**Dave Jones:** Yeah. Exactly.

**Chris Gammell:** But. Yeah. It's interesting seeing this stuff kind of fall apart too. Because. Even Sirius. Right. So Sirius we've talked about in the past. Because that's the company where. Like 80% of the revenue came from Apple. Right. And like. From the iPhone specifically.

**Dave Jones:** Well. Well. Sirius Logic do audio stuff as well. Right. Right. Right. I mean. That's. So. So they're buying their rival. Right.

**Chris Gammell:** They're buying their rival. But. But. Yeah. Like so much of the revenue comes just from the iPhone. Right. Right. So dependent on it. And now if Wolfson is in there too. It's like. Okay. They're going to be like the one stop shop. But. I don't know. Yeah. What happens if they fold. Right.

**Dave Jones:** Well. Yeah. Maybe you shouldn't be buying shares. Is that what you're saying?

**Chris Gammell:** Well. Yeah. I guess so. But not even that. It's just like. What happens when there's one supplier left? I guess other people pop up and say they'll start doing it.

**Chris Gammell:** But.

**Dave Jones:** It still represents 65. Apple represents 65% of their revenue.

**Chris Gammell:** That's crazy. That's. Yeah. That's a. That's bad. That's. Yeah. It is pretty bad. The silent, silent partner who's not so silent.

**Dave Jones:** It means that they can screw you over. Right. So. So much so that you have to sort of almost make a loss on the sales to them. Yeah. You know. Right. Well. That's not even what I'm saying though.

**Chris Gammell:** So that's still business side of things though. Right. So. Okay. So then. Tomorrow. Cirrus slash Wolfson. Whatever they end up calling themselves. That company fails. What then?

**Dave Jones:** Or Apple buy them. I guess so.

**Chris Gammell:** Man. That's just like. That's just crazy. Right. I mean like. Is it like. The new Nexus. Nexus 6 smartphone. Now without sound.

**Speaker ?:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** I mean. I don't know. Like. I'm sure there's other stuff in the marketplace. But it just seems like such a crazy amount of consolidation. And it's just like. Well. What other choice do you have at that point? I don't know. I guess other companies will pop in and do that kind of thing. But. It's not. It's not like there's new chip companies popping up these days. So. When you start running out of choices. Yeah. Yeah. That's. I just. I wonder what the ultimate result will be.

**Dave Jones:** Hmm. All I know is that I wouldn't want to be in the chip business. I.

**Chris Gammell:** Yeah. I got out of that one. Yeah.

**Dave Jones:** Oh. It's a rough one.

**Chris Gammell:** Yeah.

**Dave Jones:** Boy. I don't like it.

**Chris Gammell:** Hmm. What else are you building these days, man? Anything?

**Dave Jones:** What else am I building? Building shelves in my office. I'm expanding my lab, dude. Man. We talked about that right at the start. I know.

**Chris Gammell:** You've got so much logistical stuff going on. I don't know. It's like. Yeah. Yeah. Well, my bench buddies.

**Dave Jones:** Hey, I almost. Almost. Finished my Kickstarter shipping. Oh, yeah.

**Chris Gammell:** Okay. So then you're going to start on another one?

**Speaker ?:** Yeah.

**Dave Jones:** It's like a month. Ultimately. Ultimately. Yeah, probably. Ultimately. Glutton for punishment. Ultimately, like a month late past the promised. Yeah. Not too bad still. Yeah. You know. And so. You know. But I did start shipping on time. It's just that the sheer numbers of them. And my. My assembler can't manufacture them quick enough. Yeah. And there was a goof up with the parts. We didn't order enough parts. So we had to. You know. Man, how do you get around that?

**Chris Gammell:** You know. Like that's. That's. That's such a common. Actually. I was talking to Jerry about that on Twitter this week. Yeah. She was mentioning. She was having supply issues as well. I mean. Like it's the same thing that always happens. Right. And I just don't know. Like how do we fix that? You know. Like it's just always the same problem. Like how do you double, triple check against that kind of thing? It's still so human dependent.

**Dave Jones:** No. Yeah. Well you need a full time person devoted to it. So that they make sure it's right. You know. I'm sort of rushing. Doing all the. Buying all these parts. You know. And shipping them. And trying to keep my bomb up to date. And my numbers that I've got in stock. And I goofed. You know. I missed. You know. I just miscalculated on my bomb. Oh. I see. And we ended up with not enough parts.

**Chris Gammell:** So it's like because you did like. You were like batching stuff up. You said. Oh. Well I need 300 here. 300 there.

**Dave Jones:** I was batching. Yeah. Yeah. Yeah. 300 there. And I must have missed an update in my. You know. Stock count or something like that. And my assembler comes back and say. Hey. We've run out of parts. You know. Oh. Jeez. Yeah. Yeah.

**Chris Gammell:** Yeah. That's. That's. And that's the worst. Right. When it gets down to it. It's like. We can't get.

**Dave Jones:** Well. The worst is when. Well. The worst is when your assembler comes to you and said. We've run out of parts. And then they're not in stock. Oh. Yeah. Right. Yeah.

**Chris Gammell:** It's only 16 week lead time. Right.

**Dave Jones:** Yeah. Only 16. Yeah. If. Like. Some of my parts in there were a couple of months lead time. You know. And. Well. Not the critical ones that we ran out of. Because I made sure I got those right. I ordered like 2,000 of them. You know.

**Chris Gammell:** Yeah. You know. It's interesting working with. So when I was working with purchasing back in the day. Back. You know. Back when I had a job. Yep. It was interesting. You know. I almost feel bad for. I always feel bad for purchasing agents. They actually do a very. Very difficult job. That I. I don't. I don't. I don't envy at all. But you know. It's getting so. To the point. You know. With the internet and everything. Like. Whereas before. I feel like. 10. 15 years ago. You could call around. And be like. Okay. Well. We found some parts that weren't in the system. But it feels like. It's such a. Not a perfect system. But like. A. There's such an economic incentive. To be up to date. The system is. That like.

**Dave Jones:** Mm-hmm.

**Chris Gammell:** You know. They call around. They're like. Yeah. We can already see. There's no stock in the entire world. You know. And it's just like. Yeah. But they still have to call around. Right. They still have to call around. Yeah. Yeah. Of course. They still have to call the manufacturer. And be like. Can you expedite my shipment? And it's always the same. You know. It's like the same script they have to go through. Yeah. And I sat with them before. And I'm just like. Oh. This is so. You know. Because there's no. There's no control there. Right. Even the people at the fab. They're like. Well. Like. It takes 30 days to make the silicon. And then you got to cut it up. And then you got to. I know. Test it. And it's just like.

**Dave Jones:** And then we got to slot it into the schedule. Yeah. You know. Like. It's not like we can dedicate a whole line to your chip. Yeah. You know.

**Chris Gammell:** Right.

**Dave Jones:** We make a thousand different chips. And everyone's screaming the same thing.

**Chris Gammell:** Yeah. You know. And then it be. You know. It becomes like a broker game. And like. And we've talked about brokers on here. Of course. Yeah. The people who basically. Yeah. You know. Buy and hold components. And then they jack up the price. And you know. They tell themselves. Yeah. That they're providing a valuable service. But we all know otherwise. We all know what they really do. Yep. Yeah. So.

**Dave Jones:** And with all these. You know. With the crowdfunding revolution. And all that. And every man needs dogs. Getting stuff manufactured. Yeah.

**Speaker ?:** Right.

**Dave Jones:** In their garage. And selling hardware. And everything. It's almost come down to a point where. You know. And. And sort of niche-ish. Volumes. Yeah. Oh. Definitely. Is that a word? It is now. You know. Like in. In. In. In the thousands. Right. Right. So you can. So you plan your entire project. Around what you can get in stock. That's it. You don't think about anything else. You don't trust anything else. You just go. I can get stock of this. And I got multiple suppliers. DigiKey and Mauser have it. And Farnell have it. Just in case. Twice the price. Right. Right. You know. And. But at least it gets you out of the shit. That's a bargain at that point. When you're. When you're. Yeah. Exactly. Oh yeah. I'll pay $5 a chip. Instead of $1.

**Dave Jones:** But you know. As long as I can get it. It saves my entire reputation. Right. Yeah. I got my reputation riding on this. And yeah. So you'll gladly pay it.

**Chris Gammell:** It's almost like you need like a. You remember like a department. I guess they still do this. But like department stores do layaway. It's like you almost need that like. Layaway? No. You don't. You never heard of that? So like before like credit was more easily available. So like.

**Dave Jones:** Lay by.

**Chris Gammell:** Oh is that what it's called there?

**Dave Jones:** It's called lay by.

**Chris Gammell:** Okay. So around here it's called layaway. And yeah. It's the same kind of. So people don't know. It's like. You know. These days people are just like. Oh I have a credit card. I'll just put it on that. And you know. Pay 30% interest. Right. Right. But in the day. Back in the day. It'd be like. You put it in this back stock room. Then you'd go. And you'd pay some towards it each month. And then you know. Eventually when you paid it all off. You'd get it.

**Dave Jones:** They would hand it to you. But they'd physically keep it. And store it for you.

**Chris Gammell:** Here near there. But you know. It's like. We almost need that for chips. Just because. So you could be like. I. Yeah. I need that. I'm going to need those parts. In about three months. Right. And then you know.

**Dave Jones:** Exactly.

**Chris Gammell:** Pay some amount of.

**Dave Jones:** Well you've got no choice. You've got to buy them now.

**Chris Gammell:** Well that's. Yeah.

**Dave Jones:** I. That's what I did. I ordered some critical. I ordered the world stock. Of this critical part. Before I. My. Before I started my campaign. You know. Because. I just needed some. In the bag.

**Chris Gammell:** Right.

**Dave Jones:** You know. I. I.

**Dave Jones:** I couldn't risk. Was it the op amp or something?

**Chris Gammell:** Was it the.

**Chris Gammell:** Was it the. Was it the.

**Dave Jones:** Was it the. Was it the. Was it the. It was the. Was it the resistor.

**Dave Jones:** I. You know. I bought up the world. Yeah. That was a good buy. Yeah. It still wasn't enough. Right.

**Chris Gammell:** Right. But you at least had enough to deliver. The early stuff.

**Dave Jones:** Yeah. And as soon as the stick. As soon as the money came through. Well as soon as the Kickstarter campaign started. And I knew I was committed to that. And I could see the volumes pretty quick. Yeah. I went and placed the order for 2000 and there was like a two month lead time. Yeah.

**Chris Gammell:** Right. Right.

**Dave Jones:** And yeah.

**Chris Gammell:** Yeah. It's weird. You know, it's like you mentioned that with like the whole hardware revolution, you know, everybody's doing a Kickstarter kind of thing. Everybody kind of becomes a purchasing agent at that point. Right. I mean, like you don't think about it really, but you know, on a, on a micro scale, if you, if you're just buying volume parts from even just from a distributor, you have to deal with that kind of stuff. You, you kind of keep track of, of lead times and really all that other stuff. It's, and it's just such a mess. Oh.

**Dave Jones:** And you can't just leave it up to your turnkey assembler. You know, if you're going to get spark fund to sell it for your art of fruit or seed studios, you can't just leave it up to them. You've got to design this in. You've got to think about this while you're designing the product.

**Chris Gammell:** Right.

**Dave Jones:** And maybe even buy some parts for them upfront because you're the one who has to drive this thing. Ultimately, you can't wait until they're involved and then, you know, and there's all the, all your deals signed for the, you know, getting them to do it and everything. And then their purchasing department finally gets around to it. And by the time they do that, oops, sorry, that, that, that parts out of stock. So you've got to preempt that.

**Chris Gammell:** You know, who else we should blame here is, is the, the lean manufacturer, those, those darn Toyota manufacturers,

**Dave Jones:** the lean manufacturing,

**Chris Gammell:** damn it. like, I get it. I get it. It's great. But you know, there's no such thing as just in time when you're, you know, 10,000 miles away from the goddamn fab and 45 days away from, from a wafer start. Right. There is no just in time. There's, there's, just lost my job. And just almost made it.

**Dave Jones:** If, if people don't know what we're talking about, these things came around in the nineties.

**Chris Gammell:** Oh, before that.

**Dave Jones:** they're, they're, they're sort of, yeah, they're, you know,

**Chris Gammell:** 80, 80s was some Toyota production system, TPS. Yeah.

**Dave Jones:** Right. Okay. Yep. Yep. Yep. And these are all, uh, uh, manufacturing techniques and you can do courses on these. You can get, you know, you can do professional course as a management and manager, you're almost made in any big company to go and do these courses. And one of them is called lean techniques. One of them is called just in time, J I T. And, and they're all different.

**Chris Gammell:** Kaizen and Kanban. Methods.

**Dave Jones:** KK's and Kanban and all that sort of thing. Yeah. They're all different techniques of how to project manage the supply chain and get thing. And, you know, something like, uh, the summer self-explanatory just in time is just that your parts. You don't, the whole concept is in a nutshell, if I've got it right, is that, uh, you don't want to hold stock.

**Speaker ?:** Right.

**Dave Jones:** No, exactly. We're probably talking out of our ass, but you know, we know the basics. Yeah. You know, you don't want to hold stock because the, uh, you know, the thing goes that, well, well, you're holding stock. You need inventory. You need bigger warehouses. You need this, you need that. And it costs your company money. Right. So use this just in time technique where you order things just in time. So they turn up on the truck, on the truck, on the truck, like almost the same day that they're being assembled into your product,

**Chris Gammell:** you know? Right. And you know, the only thing that ever gets in the way is, uh, man, reality. Yeah, exactly.

**Dave Jones:** And these things can be made to work and some companies make good use of them. Right.

**Chris Gammell:** I think on a factory floor, I think this stuff is, it's perfect. Right. I mean, like, like I've seen, I've seen a lot of this stuff work on factory floors that I've been on before. Right. And it's in a,

**Dave Jones:** that's same here. We've had can band systems. Yeah, exactly.

**Chris Gammell:** And that's what it was designed for. It was designed for, you know, car, car manufacturing. Right. So you, you need a bracket to install that seat into a car. You don't have a storeroom of 10,000. You have one for each new chair that comes through and each new car. Right. Yep. And, uh, that's a lot different though, because that's in your company. And yeah, of course there's raw materials you need, but like it's for these vertical systems as well. Like these, you know, Toyota was making all of their parts and they had custom parts and all this other stuff. And it's like, you know, when you're buying from DigiKey, can ban is a can of garbage. Sorry. I was trying to make some kind of fun. I did. There's nothing there, but can ban is can't ban. I'm sorry. I'll see myself out folks. Uh, but yeah, you know, you know, it's just, it's just, it's, it's a, it's tough. It's a tough system to deal with. Supply, supply chain stuff is difficult. It is. That's why I'm trying to fix it. Uh, you schmuck.

**Speaker ?:** I know.

**Chris Gammell:** I'm such, I'm screwed. Uh, yeah, whatever. You're the one who's still jumping. You know, I was thinking about this today cause you were, you were late to showing up for the show and you're like, you told me you were, you were shipping these things. I'm like, damn, he's still shipping these things. I'm like, and that's what we get for building hardware folks.

**Dave Jones:** No, I know. Yeah. Yeah.

**Chris Gammell:** But some people do it right. I got 50 left.

**Dave Jones:** Marcus did it right. Yeah. Some people do it. He's doing that. Oh, well, yeah. And he takes a hit in terms of the amount of money he makes on each unit. Right. He's, he's traded off hassle. Yeah. Right. So he's, he's getting the no hassle. Solution, but he's also getting less income per unit.

**Chris Gammell:** Sign me up every single time. Right. Yeah.

**Dave Jones:** Well, you know, depends on what you want to do. You know, sometimes it, sometimes if you get somebody else to do everything, it may not be worth your while to even do the thing at all, even though it is zero hassle.

**Chris Gammell:** Well, yeah,

**Dave Jones:** it may not be worth your time to actually, to actually design the thing and prototype it, do everything else and manage it. And then finally get somebody else to take it off your hands and you earn, you know, five bucks a unit or 10 bucks a unit or something. It's like, well, and if you're only going to sell a couple of thousand of them, yeah, then, well, you know, it may not be even worth your while. So you've got to charge more, charge more, yeah, do higher margin products or, you know, it's, yeah. Yeah. Because you don't, you don't want to work for slave wave, slave labor wages. Right. Folks, ultimately, it's just not worth it.

**Chris Gammell:** Yeah. You heard it here first, folks. Slave wage labor is not, it's not worth it. And that will be, Oh goodness. our final word for the week.

**Dave Jones:** Yeah. Cause we're way over. We're 15 minutes over. No one wants to hear us rant on anyone.

**Chris Gammell:** Yeah. We could start talking more about lean manufacturing and what we don't know about it, but we should probably.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** And then we get some, we could get some expert on it and then we just fall asleep halfway during the show. Well,

**Chris Gammell:** we've had a lean expert on, but it was, uh, Eric, Eric was the, uh, he was lean startup, which was somewhat based on lean manufacturing, but loosely, I think.

**Dave Jones:** Yeah. No. All right, man. Well, so we'll have to get a, somebody who's got their green belt in, uh, you know,

**Chris Gammell:** Oh, I, I got a green belt. Wait, did I get green? Oh, you've got a green belt. Did I actually get the green belt? No, I don't think I actually got the, I was in green belt training, but I never, yeah, you want a black belt. Right. You didn't finish it. Pass. I, I, I just, I'm so over that stuff. I don't know.

**Dave Jones:** Yep. So am I. Now I spent far too many years dealing with that crap and yep.

**Chris Gammell:** Now we're inefficient and we make podcasts that go too long. Uh, next week we will have a mystery guest.

**Dave Jones:** Mystery guest.

**Chris Gammell:** Which means I haven't scheduled it yet.

**Dave Jones:** Right. So, so you can't even give a clue because you have no clue. I have. Truer words have never been spoken,

**Chris Gammell:** Dave. All right, man.

**Dave Jones:** Yes, I have the, the chip printer. Okay. All right. That's true.

**Chris Gammell:** We'll catch you next week.

**Dave Jones:** Catch you next time.

**Dave Jones:** Bye.

**Speaker ?:** Ass.

**Chris Gammell:** You're in your last word. x x
