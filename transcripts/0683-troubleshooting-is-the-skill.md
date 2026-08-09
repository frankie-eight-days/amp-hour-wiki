---
episode: 683
title: Troubleshooting is the skill
url: https://theamphour.com/683-troubleshooting-is-the-skill/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released November 20th, 2024. Episode 683. Troubleshooting is the skill.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** You know, despite my exhortations during our last episode about how no AI tool should be used for layout, I have been using them to help me write code. So I'm a little bit of a hypocrite, but nothing new there.

**Dave Jones:** They're a very good tool. You know, you've got to, like, even when I did it, like, what, probably a year and a half ago now, it practically wrote all my code. Like, you know, it's a very useful tool.

**Chris Gammell:** What level of code was it doing for you? What was it helpful?

**Dave Jones:** It was doing hardware abstraction as well as coding. So it was, like, I gave it a physical description. Sorry?

**Chris Gammell:** Was this a microsupply or something else?

**Dave Jones:** No, this was my BOM.

**Chris Gammell:** Was this the BOM? BOM. This was it, yes, the BOM.

**Dave Jones:** Yeah, I got you. Yes. Yeah, timer. So I gave it a hardware description. Got it. Like, a description of shift. Like, because I needed to drive shift registers and seven-segment display. So I gave it the description of the hardware, just the hardware, and it wrote the code, and it was almost, there was only one error in it. That's pretty cool. It was, like, I was absolutely blown away, and that was, like, I don't know, a year and a half ago or something. Yeah.

**Chris Gammell:** Yeah, and this keeps getting better. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** No, it's great. I mean, that is one area that I, I mean, obviously, it's not like I'm like, oh, it's going to take my job. It's like, no competition there. For me, it was, I've been doing some Zephyr stuff, and the thing I'm not sure about is, like, Zephyr moves pretty fast, right? There's, like, a lot of, like, development on the project, and you don't really know if it's going to suggest something that's, like, not correct anymore. That's the only thing I've kind of, but the compiler tells you, you know, like, so that it's just, like, you might run into that sort of thing, but it helped me troubleshoot device tree stuff, which is, like, an ongoing issue of, like, how you connect stuff together, and that was a great use case of just, like, hey, you know, kind of, like, structure, like, checking structure, that sort of thing has been very, very useful.

**Dave Jones:** Right. No, I thought it was fantastic. Like, for guys like me who don't code, like, I can code, but I do it so infrequently these days that I almost have to, oh, God, how do I code again? Like, it takes me, like, a day to get back into it or something for, you know, some dummy like me who, you know, just doesn't do it a lot, and I would use it as a first step just to get some base code of something running just so that I'm, you know, actually I have something to work with rather than just write it from scratch. You know, the old school days of just, like, starting from scratch

**Chris Gammell:** are, you know, it, I think. Yeah, I think, like, normally my MO would be, like, go find samples, examples, whatever, right? Yeah, yeah, exactly.

**Dave Jones:** But this is basically starting from there. And then you cobble that together, you cobble the sample together. But this is like, this can get you, you know, runs on the board, like 90% there, something like that.

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** So, yeah, why not?

**Chris Gammell:** Yeah, I do wonder about, sort out the bugs later. I've been reading about, or actually I was asking, yeah, so I paid for Claude, the Anthropic product, because it's been really good for code stuff, and I've just been, I've been using it for language learning too, like for, like, practicing Spanish, also good for that. Not as good as OpenAI, because that'll actually talk to you, but it's fine. And I was asking, I was just kind of curious. I was, like, watching my kids, and I was, like, asking about, like, what you should do with teaching and stuff like that, and teaching children in an age of AI. And it said, don't worry about it. It's no problem. I'll take care of everything. Not creepy at all. No, yeah. No, I didn't say that. But one thing that has, I've done some, I've done a little bit of reading about was just, like, you know, troubleshooting. Troubleshooting generally is, like, when you rely on a tool like this, I was relying on it as a troubleshooting tool in my case. Then, like, when you actually get to something where, you know, whatever LLM or equivalent you're using doesn't have the answer, then, like, if you're so dependent on that crutch that you don't have the skill set, like, so it's like, like, troubleshooting as a skill set was going to be kind of a, it's a level up from there, like, maybe the baseline, like, everybody's going to use it to troubleshoot device tree like I'm talking about. But then it's also about synthesizing that information and being able to utilize stuff outside of that as well. And I don't know, just it's an interesting skill set that I think a lot of us have that are listening and hopefully speaking. But it probably will be even more critical, especially in kind of those corner case kind of areas where an LLM might just not touch on and really need to have some more useful skills there.

**Dave Jones:** Or worse, it hallucinates code. Oh, sure. Yeah. Right, right, right.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. But one thing I'm not worried about, like, one thing I don't really lose my skill at is debugging code. Like, it doesn't matter how long a break I've taken from coding, the problem's always, like, starting again, like, writing from scratch. Oh, God, how do I, you know, and do this and all that. Yeah. But if there's code in front of me, it doesn't matter how long I've been out of the game, I can read that and start troubleshooting almost immediately. Check your inbox, actually.

**Chris Gammell:** We're going to prove this live on the air. I'm just kidding. Oh, what? Okay. No, that would be something, right? If I was ready for that. Right, right. But it's not, you know, you have to do it on video. Check under your seat. Oh, boy. Yeah, no, that's it. So, I actually, I got to fire that engine back up when I'm, like, not in troubleshooting mode. So, you're saying you can just, you think you can just turn right back on no matter what?

**Dave Jones:** I think for debugging code, yes. I think for debugging code, I think it's not really a problem. So, that's why I'm quite confident in using, you know, an AI-type tool to generate some code to sort of get me off the ground. And then if it doesn't produce any output, I think I'm, you know, quite skilled at being able to, at least possibly skilled, in actually being able to get it to actually, you know, to sort of massage it into doing something, right? Yeah, yeah, exactly. Do something. So, yeah. Poke the meme with the stick. Exactly.

**Chris Gammell:** Yep, yep, yep. Yeah. Well, there's another skill set right there, too, is being able to deploy memes as necessary. Yeah, of course.

**Dave Jones:** I'm a meme master.

**Chris Gammell:** Yeah, right, right. Take heat, kiddos.

**Dave Jones:** Dude, you don't follow me on Twitter anymore. I don't. I'm just banging out memes like there's no tomorrow.

**Chris Gammell:** Oh, man. It's like things that you'll tell your grandkids about.

**Speaker ?:** Exactly.

**Dave Jones:** I was a meme lord. I was a meme lord during the great meme wars of the 2020s. Yeah, right, of course, of course.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep, right up there with the corn syrup riots or whatever. What was it?

**Chris Gammell:** I don't actually know.

**Dave Jones:** Ready Player One. I just watched Ready Player One last night and the bandwidth riots and the corn syrup droughts.

**Chris Gammell:** Oh, interesting. I have blocked that movie from- It's been a while since I've read the book, but yeah, I know you're talking about like in the dystopian beginning.

**Dave Jones:** I know you hated the movie and I thought about that last night. You hated it so much. I was just thinking, I was sitting there watching it late last night and I thought, how can Chris not like this?

**Chris Gammell:** Because I read the book so many times. How many times have you read the book? At all or no?

**Dave Jones:** Yeah, once.

**Chris Gammell:** Once, okay. Yeah. It just was, here's the thing, like no one's listening to me. It's like freaking Steven Spielberg directed that movie. Like everyone's like, yeah, it's cool. Don't worry about it. I just personally, I didn't like it. I don't know. Yeah.

**Dave Jones:** I don't get it. Don't get it at all.

**Chris Gammell:** I don't like how they started it. I don't like how much they skipped. Oh, the starting is great. There was like so little on the backstory. The IOI stuff was so poorly done and like low budget looking. I don't know. It's just, yeah. You know what? My movie head, the head movie rather was much better and that's fine. Okay, fine. Lower cost, lower budget and only I get to see it.

**Dave Jones:** And only you get to review it.

**Chris Gammell:** That's right. Right. Yeah. Yeah. Yeah.

**Dave Jones:** Oh boy. I mean like,

**Chris Gammell:** this is not like a new thing for me though too. Like, I really, you know, I love the Expanse books. I think I told you about like James S.A. Corey, right? Like the nine part series and like just brilliant and like Amazon made the show. It was like, you know, very well regarded show. I hated it. Absolutely hated it. I'm like, the casting is all wrong and I just didn't like how they cast this person and that person and whatever and then you look at the credits and like the two writers were the, they were in charge of the show. It's just like, oh, well, you know.

**Dave Jones:** I think we know where the problem is there then.

**Chris Gammell:** I think we do. Yeah. Right. If we really narrow it down. Here's the thing though, Dave, I don't have a lot of opinions. I mean, I do have some opinions on this show, but like, you know, usually I'm, yeah, yeah, I'm not like you, you know what I mean? Right.

**Dave Jones:** Okay.

**Chris Gammell:** I don't have as many opinions as you, but these sort of things I do have opinions about, so I feel good about that.

**Dave Jones:** And my opinions are always right, of course.

**Chris Gammell:** Sure. Yeah. Yeah. Yep. Absolutely. There you go. Yes, grandpa, your meme is so great. You've still got it, grandpa.

**Dave Jones:** My boys do great memes. Really? Yeah, they're really into meme, meme, like the entire meme culture thing. Interesting. They're really into it, so yeah.

**Chris Gammell:** Okay. All right. Well, I, yeah. Well,

**Dave Jones:** the oldest one is anyway, the youngest one, not as much, but you know,

**Chris Gammell:** he sort of follows along and yep. I can't even begin to imagine what it's like to be a teenager these days and like, yeah, your son's obviously part of it and just like, yeah, so you're experiencing it from a whole thing. Like I've got, many years yet to discover that of like having a teenager. you're a,

**Dave Jones:** 10 years off, I'm afraid, you're a decade off. In for a wild ride,

**Chris Gammell:** I'm sure, yes. Yep, absolutely. Yeah.

**Dave Jones:** Anyway.

**Chris Gammell:** Anywho.

**Dave Jones:** I had my, I finally got the rat's nest updated. My house wiring has been completely, my switchboard completely rewired.

**Chris Gammell:** Nice.

**Dave Jones:** I just released a video this morning. You can see it.

**Chris Gammell:** Yeah, we'll link to that. Yep. Sure.

**Dave Jones:** Yep. What,

**Chris Gammell:** what did it take to get it done?

**Dave Jones:** What did it take? Um, a spare slot in the electrician's time. It took six months.

**Chris Gammell:** Really? Is he that good or are they in that short of supply?

**Dave Jones:** He's just so busy. He's so flat out. And this guy I like, and he agreed to do it on camera, which is the thing I really wanted, of course, right? I didn't just want to never nobody who just showed up and, oh, maybe they might mumble a few sentences, right? I actually knew this guy was good and I knew he'd perform on camera and I, and I knew he wanted to be on camera.

**Chris Gammell:** So this was really a video shoot, is what you're saying.

**Dave Jones:** Oh yeah, yeah. Tax deductible, I'm sure. Yes, absolutely tax deductible. Yeah, yeah, yeah. Everything's tax deductible in the YouTube world, let me tell you.

**Chris Gammell:** As known as content, it's content, Mr. Tax.

**Dave Jones:** Haircuts. I claim my haircuts. Oh,

**Chris Gammell:** well, there you go. Yeah.

**Dave Jones:** Yeah. Got to maintain my professional appearance.

**Chris Gammell:** Good luck. Good luck with that. Yes.

**Dave Jones:** Oh boy. Anyway. So yes, finally, finally got it done. Finally got it done. Great. And it looks way better. Interestingly, like a lot of people, especially overseas, of course, everyone in Australia totally understands, what this is all about and where it comes from and everything. But everyone overseas going, well, what's improved? And I'm going, well, it's just basically a wiring tidy up. My old existing rat's nest, have you seen it? We could actually include the photo of the rat's nest.

**Chris Gammell:** We talked about the show when I think you were, you were doing another, your battery install, I think. Oh yes, yes,

**Dave Jones:** the battery install. And we had to add yet another circuit to the, that's right. Yep. You know, and it's been bodged like eight or nine times over the last 18 years or something.

**Chris Gammell:** I have to say, it does seem a little less, formalized. I know it's like higher voltage and, but like, just even the fact that you're talking about wiring inside the circuit breaker box is very, like, you know, it's very, it's all sheet metal here, right? It's just form metal with the contacts here. And it felt like it's more custom kind of ad hoc, you know, at least the stuff you described.

**Dave Jones:** You're talking about the case, the outer.

**Chris Gammell:** No, no, no. I remember you opened up, you looked at the back of the thing and it was like wired. It's like point to point wiring, right?

**Dave Jones:** Yes. Yes. It is totally point to point wiring.

**Chris Gammell:** That doesn't happen here. I mean, as far as I understand it, I mean, like, yeah.

**Dave Jones:** Absolutely. That's just, but that's just a thing here, you know, where, right, that's what I'm saying.

**Chris Gammell:** It's not bad. It's just ad hoc. It's different than what I'm expecting.

**Dave Jones:** It's actually perfectly legal. And you can actually still wire a box legally that way right now.

**Chris Gammell:** Okay. There's no problems whatsoever. Is that just yours or is that all of them in Australia? I guess that's what I'm trying to disagree with.

**Dave Jones:** It would be every, everyone from the 80s, maybe even the mid 90s backwards. Yep. Yep. Totally. After that, yeah, they tend to use a din, a proper railing with din mounts and, you know. Got it. Yep.

**Chris Gammell:** Oh, din mount. Okay. Interesting. Yeah. Yeah. So it is more like a, like an industrial look than.

**Dave Jones:** It's more of an industrial look, especially from the front. It's like, you know.

**Chris Gammell:** Yep. Got it. Okay. Yeah. Again, like that is just, that's very different from what I'm used to because here it's, you know, you have your, your, all of your landings come in from the signs.

**Dave Jones:** you guys have like big bars. You guys have big bus bars. That's right. Yeah.

**Chris Gammell:** Because the dual phase thing, right? I mean, that's the weird, that's the weird thing here, but that, but that does end up being like, because you're snapping your breakers directly onto those bars.

**Dave Jones:** Yeah.

**Chris Gammell:** That's all you get. Yeah. There's no like custom, there's no wire. No. Except the stuff that's landing. Yeah. Right. There's no like interstitial wiring. It's just the stuff that gets to it.

**Dave Jones:** it's totally different here. It's a, I'm not aware of that bus bar thing being a thing here in Australia at all.

**Chris Gammell:** Yeah. It might not be rated for what you guys do, honestly. Maybe.

**Dave Jones:** Yeah. Yeah. It may not be, it may be in an industrial situation would be totally different, but homes and things. No, no, I'm not aware of that here. So yeah, all new modern houses uses, use a din rail system with a plastic enclosure box and then surrounded by a metal enclosure. And, and this is outside the house. This is a lot of things that the Yanks don't get. They go, and why is the box on the outside of the house?

**Chris Gammell:** Well,

**Dave Jones:** that's just what we do here. Cause like, it doesn't like snow here and stuff like that.

**Chris Gammell:** Cause then you get more spiders. That's the good stuff.

**Dave Jones:** You really want to have those social,

**Chris Gammell:** the social media photos of your spiders just taken over your, your, your box.

**Dave Jones:** That's it. Snakes and things getting in there. Yep. Yep. That's a ticket. Yep.

**Chris Gammell:** Right. Australia.

**Dave Jones:** Australia for the win.

**Chris Gammell:** Yeah.

**Dave Jones:** And yeah, so we, we have a box on the outside of the house. Um, a few modern houses might have them on the inside. If they're, they, uh, Simon, the electrician who did this, he said, uh, yeah, he works on these big mansions and stuff. And some of them have like a tiny room actually devoted to just switch gear. If it's like a modern, like one of these like fully automated houses, you know, that has like, you know,

**Chris Gammell:** like the third wire kind of thing for smart, smart switches and stuff like that. Yeah.

**Dave Jones:** And all that sort of wakery. Yes. They will have like a small room, which has all the automation control equipment and also the, uh, fuse box and stuff like that. So if you're building a mansion from scratch, maybe you might have it inside, but just, just your general average, you know, four bedroom suburban house or something is still going to have a box sitting on the outside of the wall. And, uh, yeah, with just a din rail thing on the inside.

**Chris Gammell:** So actually mine, mine is outside too. Yeah, that's true.

**Dave Jones:** It is really. Okay. Yeah. The main panel is, I have a sub panel. Yeah.

**Chris Gammell:** Um, in my old, my previous house, um, it was in the garage. I think that's actually a great blend, right? It's like, right.

**Dave Jones:** Right.

**Chris Gammell:** Kind of, kind of firewall, not really firewalled, right? If there's a fire. Yeah, but it's kind of, yeah, but it's like the dirty, the dirty panels out there. Um, my Cleveland house is in the basement.

**Dave Jones:** You don't have to, if there's a blow on fuse, you don't have to go outside to in the freezing winter. Right. So to, you know, I live in the South now, but yes, it's still cold here. It doesn't matter. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Makes no difference.

**Chris Gammell:** Yeah. I mean, it might be really, really hot that, you know, there's that. So yeah. Anyway. Yeah. Um, yeah. And so my current house, I have like my main panels outside and then I have a sub panel up in my laundry room that controls like all the lights. Cause it's like second floor. So then like that, then controls all the lights that are like in the ceiling and stuff like that on the first floor. So,

**Dave Jones:** okay.

**Chris Gammell:** Yeah. I, I've been having some weird stuff too. Like where my, the inductive load of my dryer ends up like impacting the other sub circuit. I gotta get it looked at. I don't know. Oh wow.

**Dave Jones:** Really? Okay.

**Chris Gammell:** That could be frustrating.

**Dave Jones:** Some sort of, I don't know. Nutri. Yeah. But you guys are weird. You got the split phase thing and it's all, it's all weird.

**Chris Gammell:** Yeah. I mean, it's all the lights that flicker when it happens. So like I said, I haven't been here that long, so I need to get someone looking at it, but yeah, no,

**Dave Jones:** there's something wrong there.

**Chris Gammell:** Yeah. There is the, when you mentioned with like the, the fancy room too, I mean, there's like all of the, all the smart home thing, they have like the, you need like the Rome X four, three or four, whatever it is. You know, pulling the extra wire to, to power, power the switch even when it's off sort of thing. I don't know if you, you guys do that. Probably don't have any smart stuff. I don't either. I don't have it here, but like when you look at,

**Dave Jones:** I don't think it's particularly common here. Only in some fancy, fancy house and they want to automate all their blinds and crap like that. Yeah.

**Chris Gammell:** Right, right, right, right. Yeah. So like, I'm sure I'm getting this wrong, but basically it's like you have, you have a neutral that goes to your light switch, I think, because you need to basically have a way to power it even when it's, even when the switch is off. Right. So, right. Yes.

**Dave Jones:** We do not have a neutral go into the, to the light switch.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** Yeah. So,

**Chris Gammell:** yeah. So that's like one of the, and, and that just requires special wiring. And I, cause I've been looking at smart switches for one of the things in my house and, um, yeah, it's not going to work. So instead then they still turns into like a, you know, wireless type of setup and, and, and I haven't set up my, um, home assistant. You mean switch anything. Yeah. Yeah. I agree. I agree.

**Dave Jones:** You still haven't set up home assistant.

**Chris Gammell:** I had it in my old house. I just haven't like unpacked the box still.

**Dave Jones:** I just tried to set that up yesterday. And at the moment, I, I'm staring at a boot screen right now and it's got like a login thing. So it boots up on the Raspberry Pi four. Um, and it just sits at a login flashing a cursor at me and it says, well, go to your internet address. I plugged in the ethernet and go to, um, the, this address and it's not there. So I don't know. Oh,

**Chris Gammell:** okay.

**Dave Jones:** I haven't figured it out yet. And then, and then I, like I mentioned that I, I was doing this and then everyone, like everyone told me use home assistant, use home assistant. They're badgering me left, right and center. I start using home assistant. Then they go, Oh, you don't run it on a Raspberry Pi. You idiot. You've got to run it on a NUC. Uh, one of these until NUC. And it's like, Oh God.

**Chris Gammell:** Raspberry Pi. It's fine. Honestly, a Pi three or four. What, what size of Pi? What, what generation?

**Dave Jones:** It's a Raspberry Pi, but a Raspberry Pi four compute module. And then I've got like a little daughter board thing.

**Chris Gammell:** That's no problem at all.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Yeah. I think the thing is a lot of those people are saying that because if you run ESP home, on there, right? So we had Keith Brzezinski on the show. I'll write that in. He, he works for whatever the people that are the main company behind ESP home. I think he was the one that told me this, but basically it like crunches all the, the code on that device then. Right. So then if you want to say, you want to reconfigure one of your devices, you're basically compiling now on a Pi four. Oh God. Okay. So that's, I think that's really the thing that ends up bogging down. I mean, if you're just sending like a couple of sensor readings through, it's like no big deal. It's like, that's all I'm doing.

**Dave Jones:** I'm just like want to combine solar readings and that's basically it. Yeah.

**Chris Gammell:** You're gonna be fine. Okay.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** That's, you're gonna be fine. I just don't, don't overthink it. You know, that's the big thing for me.

**Dave Jones:** And then everyone badgers, starts badgering me again.

**Chris Gammell:** I think you, yeah, you gotta not talk to people about it. Yeah. Yeah, exactly. That's the problem here is people, Dave.

**Dave Jones:** I know. A lot of humans.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Everyone's got a stupid opinion, which is wrong. When I had it.

**Chris Gammell:** It's only my opinion that's right, obviously. Well, you should get an AI to tell you as much. Right.

**Dave Jones:** I'll train my own personal AI on, on myself. So it's always right. There you go. Right, right.

**Chris Gammell:** You still sound just like Dave's supposed to sound.

**Dave Jones:** Oh boy.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. Anyway.

**Chris Gammell:** Um, yeah, the thing that I really liked is the Zigbee bridge, Zigbee, Zigbee bridge. Right. Yes. Yeah. That, that was like a big unlock for me. Cause it's basically like, once you have that in there, it just kind of starts sucking in different, um, Zigbee readings. And it was super easy to set up after that. So you're going to be fine. Yeah.

**Dave Jones:** It's okay. I don't, I don't really want to control anything. Like I've just got a home heat recovery and ventilation system. I've done a second channel video on that. Um, that, that finally got installed. Um, and yeah, technically that, that's got like a mod bus thing. So I could hook it up, you know, and there is somebody who's integrated with home assistant, but it's like, it's what, why? Yeah. You know, like, nah. Yeah.

**Chris Gammell:** Yeah. I mean, well, I mean, we, we, we joked about on the show, like the, the thing that was easiest to do and the most worthless thing out there was my stupid Bluetooth toothbrush. Right. I mean, like,

**Dave Jones:** Jesus, you're doing it wrong, dude.

**Chris Gammell:** Yeah, I know. Yeah.

**Dave Jones:** The only thing that I've got at the moment, which I, I guess it would be nice to automate is the, um, pool heat pump because at that moment I've got it set to a timer, right? Cause we're almost in summer here. So I've basically set it via a timer to come on to use excess solar power. But in the last couple of days, including today, it's like, it's really overcast. So there's no excess solar at all. So I don't want to pull that energy from my battery. My battery actually died the other day because like,

**Chris Gammell:** I didn't have enough heaters are just like, yeah.

**Dave Jones:** And heat pump. Well, it uses 2.5 kilowatts. So, you know, it's, it's a reasonable amount. You can certainly put it on for a couple of hours, but you don't want to leave it on for eight hours or something like that. It'll drain my home storage battery now. So yeah, I'd kind of like that to correlate with like the weather. And you know, if, if it's sunny out, then yes, turn it on to use excess energy and stuff like that. And I want to do the same with thing with the air cons as well. I, I'm, I failed the other night. I, I tried to actually program my air con with like a timer. So it comes on every single day at three o'clock or something. So it uses excess solar power. And then it,

**Dave Jones:** sure. Yeah. You know, and it's, I woke up this morning and it, and it didn't work. So the time it didn't work. So I screwed something up. Yeah. Bloody hell. User interfaces are just terrible on those little.

**Chris Gammell:** Dave's HVAC is still blinking 12. Blinking midnight. No,

**Dave Jones:** I managed to set the time correctly. Damn it. And yeah, but just think though, Dave,

**Chris Gammell:** in terms of memes, kids won't get that one, you know?

**Dave Jones:** Right. Yeah. The blinking 12. Yeah.

**Chris Gammell:** Yeah. Right. Or is it, is it 24? My kids would understand.

**Dave Jones:** No. Yeah. Okay. 12.

**Chris Gammell:** Do devices still do that even? I don't even know. Like for me, it was always a VHS player. That was the thing. The VCR.

**Dave Jones:** Microwave ovens do it.

**Chris Gammell:** They blink 12 though. Yeah. Like the thing where people don't even like bother to program. I feel like it was, I was always the VCR. No? No. Okay.

**Dave Jones:** Ovens. Yep. Ovens. See around here, mine just doesn't show anything. If it's like,

**Chris Gammell:** you get a power reset, it just shows nothing.

**Speaker ?:** Oh,

**Chris Gammell:** really? Okay.

**Dave Jones:** No, ours blinks and.

**Chris Gammell:** Okay.

**Dave Jones:** Flesh is 12. Yep.

**Chris Gammell:** Yeah. On the topic of home assistant, I was just watching Andrea, the past guest of the show, Andrea Spies. He was just doing a video about Bluetooth devices and like interfaces and then setting up relays too. Cause there's a new, new ish capability to do like a relay. So say you had like a Bluetooth device in one part of your home, but then you had like a ESP 32 set up as a relay. It could then bounce that to your home assistant server basically. Which is kind of cool. Right. So check that out. I don't know if people are interested. I'm not, this is not going to turn into a smart, a smart home show because we just, we don't know enough.

**Dave Jones:** Yeah. For my guest of the show, Ian Scott Johnson, I think it's Ian Scott Johnson. He wrote his own, instead of using home assistant, he wrote his own. He wrote his own automation system from scratch. And he says, I've been working on this for two years or something. I was like, I really don't want to throw it out. Cause I spent so long working on it. Although I could just do it all in home assistant, you know? And he's like,

**Chris Gammell:** yeah,

**Dave Jones:** it's a really crazy, like gooey interface. It's got check boxes everywhere. Like, you know, 50 different like things that he can tie together. And it's really impressive, but thoroughly impressive stuff. It's like, yeah, but.

**Chris Gammell:** Yeah. I think this might be falling into sunk cost fallacy on that one, you know?

**Dave Jones:** Yeah. Right. Yes.

**Chris Gammell:** Cause then like every time you have anything new, say there's like a new sensor you want to use, it's like, well, you have to implement it. And then like, you don't get any of the benefits of a ecosystem.

**Dave Jones:** So that's right. Yeah. There's some reasons to do it though, too. Yeah. Personal edification. Cool.

**Chris Gammell:** Yep. That sort of thing.

**Dave Jones:** Absolutely. And it's very impressive. And you can tweak it until the cows come home, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** So I think he's got it tied into the weather service. So he's like, he's got his own special algorithm that, you know, predicts the weather and then, you know, does all this stuff and, you know, yeah, really, really quite impressive.

**Chris Gammell:** Yeah. You know, I do API stuff for day job stuff. I don't think I want to do it at night. You know, that's the thing. Like I want like a tool that just like, Oh, I, I know what everything's going on in your house and here it is. But some people love that stuff, you know?

**Dave Jones:** Yeah. Well then there's somebody who was like on Twitter the other day was telling me about my home battery and how I can automate it with the new, some of the new, cause I've got a new smart meter. I can, I think we talked about this. I can integrate it with the new smart plans. And then he said, Oh yeah, no, he's telling me all this great, great stuff I can do with it. Right. With my new smart meter and my new battery and how I can integrate them all. And he, and then he said, Oh, by the way, it took me two years of tweaking and it's still only, and it still only does 95% of what I want. It's like, Oh God. Yeah. Okay. Yeah. Thanks. But yeah, nah.

**Chris Gammell:** Yeah. I'm not going down that route. So I mean, that's the thing. A lot of these, a lot of these kind of like setups too. It's like, uh, you know, I, I always like lament, like, Oh, my in-laws use all Apple products. And it's like, so, you know, I'm like, ah, you're like stuck in that system. It's like, yeah, but it works for them because they don't want to do any of it. So like that is worth it for them to buy the, if they're going to have anything, they just buy it. And it's like, okay. Yeah. Yeah. Fine. I get it. I get it.

**Dave Jones:** In fact, I would never get a cost. I would never get a time cost payback on any of this automation stuff. Right. Because like take my pool heat pump, for example, right. If it's an overcast day, I can simply press a button and turn it off.

**Chris Gammell:** That's right. Yeah.

**Dave Jones:** Like, you know, like, and, and even if I have to do that 50 days a year, that is still only what that, like an hour's work. Not even, right. It's like 10, like 10 minutes work. Not even Dave,

**Chris Gammell:** what if you aren't home in time to press the switch?

**Dave Jones:** Right. Well, at the moment I can't do it remotely. So just the other day I caught up the Mrs. EV blog and I said, uh, it's overcast today. Can you switch the, please. Our battery's getting low because I can see remotely my battery and I can see, you know, the power consumption. I can see whether or not the pool pumps on and stuff. I just can't control it remotely.

**Chris Gammell:** So you just need that digital finger. You know, that is one thing that I had in a home assistant is like, there's actually like a button. There's just a thing that'll press buttons for you. So that's all you got to do.

**Dave Jones:** I need to investigate that. If I can do it on my shoe phone or I can do it from my rails or something like that, then great. You know, that's just easy. Then there's no point to automate it really. It's because then you'd have to continually tweak it. Cause what if one day the batteries, you know, you'd have to tweak the algorithms. Okay. What if the battery is actually already full, you know, because the day before was good or whatever. Corner case, corner case, corner case. It's a corner case. You'd always be hitting these corner cases, you know?

**Chris Gammell:** Totally.

**Dave Jones:** And it's like, just continually tweaking it.

**Chris Gammell:** I think like in a, in a home assistant setup, my most likely thing was I was like logging in and toggling a button myself. That was like the way I used it. Oh,

**Dave Jones:** right. That, that was your automation. That was human automation.

**Chris Gammell:** I mean, it was like what I really, I wanted to like see the status of things and be able to control things. Like you said, like command and control.

**Dave Jones:** That's exactly what I'm doing at the moment. And I've got all the tools to monitor everything. And I simply go in and I can hit some buttons. Yeah. So I think you'll,

**Chris Gammell:** I think you'll be in a good space there. The only thing I would say in that case is it sounds like you want to be able to do this stuff remotely. So you're either going to have to VPN into your own system, like using like a,

**Dave Jones:** yes.

**Chris Gammell:** What's it called?

**Dave Jones:** Well, as, as I said, the only thing I can't do remotely at the moment is the hot water heat pump.

**Chris Gammell:** Got it. Yeah.

**Dave Jones:** So, yeah.

**Chris Gammell:** But if you also pay the,

**Dave Jones:** that's really the only load I want to control, but maybe, maybe the air cons as well.

**Chris Gammell:** Got it.

**Dave Jones:** Maybe those, but you know, trying to control the air cons, I'd need an infrared transmitter that transmitted the bloody code.

**Chris Gammell:** Oh, right, right, right. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Well,

**Dave Jones:** I can actually tell if my air cons are on based on the power consumption. So I can sit here at my desktop at work and I can remote view my actual power consumption to see, well, like I can see that currently I've got it open now and I can see that, well, the pool, sorry, the hot water heat pump has just switched off. So, yeah, I can. Ladies and gentlemen,

**Chris Gammell:** November 12th, 2024, Dave local time. Today is the day that Dave accepted IOT as his Lord and Savior.

**Dave Jones:** No, it's not an internet of things.

**Chris Gammell:** Sure, sure sounds like it. Hey, you know what? Nope. I'm a little bit more of an expert in this field than you are, my friend. I don't care. I'm looking at data. I want to control the data. I'm like, Dave, I'm sorry, man. You've got, you've got the sickness. You've been, it's been confirmed.

**Dave Jones:** You do realize I've had this capability for a decade, right?

**Chris Gammell:** Well, there you go. You know what? Even worse.

**Dave Jones:** Oh boy. Yeah. Yeah.

**Chris Gammell:** Yep. Well, it'll be interesting to see your experiments. I would say, yeah, people have very, very strong opinions about how you should be doing things like, especially like home, it's almost like a bike shed type thing where it's like, you know, it's kind of available to everyone. So there's a lot of opinions about how you should do it. It's like, I wouldn't listen to it. Just try it out. Nah,

**Dave Jones:** for me, I'm, I'm not into over automation. It's just, you know, the amount of effort you put into it. Even if, you know, like, cause I, I actually like controlling. Like I actually like having a switch I can turn off and on under my own human algorithmic control. You know, meat controller. It's great. Yeah. Yep. Meat, meat controller. That's it. Yep. So. Well,

**Chris Gammell:** best of luck, my friend. Best of luck.

**Dave Jones:** Thank you.

**Chris Gammell:** Yep.

**Dave Jones:** Ah, boy. Anyway, can we get back to electronics? Maybe. Well,

**Chris Gammell:** there is electronics in the IOT. I'm just saying, you know.

**Dave Jones:** Ah, right. Yeah. Well, you know, talked about that to death. I do like this video that you posted. Um, who's, who's the YouTube channel? Which one? Oh, Oh, hang on. Oh, the, uh, linear power one? Yes. Yeah. Yeah.

**Chris Gammell:** Yeah. This was actually a new channel that I would just discover through Timon, um, Scrooge. Um, and it's like this really great, like explainer series. He does other ones around, what was the other one I watched? It was around, Oh, how MOSFETs work. It was great. It's just like the user circuit boards and he puts this stuff together. So yeah, maybe we'll have to, you know, see if we can.

**Dave Jones:** So the channel is. Electra. It is E L E C T R. And then arc two 40. So.

**Chris Gammell:** Electrark.

**Dave Jones:** Electrark. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. I don't know why he didn't use the full name, but like, well,

**Chris Gammell:** yep. It's fine. It's cool. Uh, but yeah, no, it's great.

**Dave Jones:** So basically what's, yeah, the video is like half an hour long. And he's basically, um, explaining step-by-step how a, how a, uh, power supply works in particular, a linear power supply. He's done one on a switch mode. I haven't, or have I seen that? I might've. Anyway. Um, and, and then he's got a separate PCB literally for each component. So he's got like a transformer on one PCB. He's got the, uh, he's, he's got the, uh, decoupling cap on one PCB. He's got the output filter on one piece of it. Like it's yeah. It's like from a visual point of view, it's actually like he's, he, he has the fuse on one PCB. Like it's just really cool. Like from a visual point of view. So he's gone to a lot of effort to visually set this out. Um, so yeah, I'm very impressed. He has a switch on, on its own PCB and then he joins them all together and they're all color code. He's got different solder mask color PCBs. So that, yeah. And just to help them with the visual, um, separation. Wow. It's just, yeah. So much work has gone into it. Hats off.

**Speaker ?:** Yeah.

**Dave Jones:** Seriously good. So, yep. Very impressed.

**Chris Gammell:** Yeah. I mean, it's, I, I, I just like it cause it's a, you know, like when you're talking about like MOSFETs by themselves, like the MOSFET video is great too. Cause it's like, uh, he actually visualizes with like relays, which is great.

**Dave Jones:** Oh,

**Chris Gammell:** actually live showing relays and things like that. So yeah, that's really, it's a,

**Dave Jones:** you need to know about MOSFETs. Oh, right. Yes. He's done a similar sort of thing. Yeah. Yeah. Yeah. Okay. Right. It's good. Right.

**Chris Gammell:** Kind of feels like it's a, he's like a former, like TA or something.

**Dave Jones:** Oh, he's got to be a former teacher or something like, or a teacher or something like that.

**Chris Gammell:** It's just the ability to like explain stuff in that way, like really breaking it down is good.

**Dave Jones:** Yeah. And really breaking it. Because this is very much what I'd expect to see in a lab, like a, uh, uh, electronics lab, like actual teaching lab. Right. Right. Right. Yeah. They like, like they have separate modules and they have them all identified and labeled and everything. And you join them all together. Like you join the separate building block components together. Um, that that's a very common, um, thing in any sort of like, uh, electronics lab teaching thing. So, yeah. So I, I, I'd be surprised if he doesn't have that sort of background, that's where it comes from, or he just found, or that's how he learned, you know, or, or something like that. And then he's just trying to duplicate it. So yeah, it's great. Anyway, very impressive. Good stuff. So yes, channel of the week. Electrarch. Electrarch. Does that mean he's from a 240 volt country? Which is basically every country except the U S right?

**Chris Gammell:** And Canada. And Mexico.

**Dave Jones:** Oh, they're, they're 112. They're two, are they?

**Chris Gammell:** 120 is what you meant to say, but yeah.

**Dave Jones:** Sorry. 120. Yeah. Yeah.

**Chris Gammell:** There's a map somewhere. And then, no, Japan's 240, but they have 50 and 60 Hertz. And then like a bunch of South American countries also have like, so the weird ones are like, so there's a wiki map somewhere that we've definitely linked on the show before, but it's like, it's the ones where you have multiples in a country. It's just like, how the hell does that work? Right.

**Dave Jones:** Yeah. How does that work? Yeah. Yeah. Yeah. That's nuts. We're like, I mean,

**Chris Gammell:** it's not, it's not the grid, but have you ever seen, have you ever seen the wiring in like some cities in India? Just like,

**Dave Jones:** Oh yeah. It's like wild.

**Chris Gammell:** It's really wild.

**Dave Jones:** That's the wild west. Yep.

**Chris Gammell:** Yeah. I mean, it's like, so just as like a visual thing for people, it's just like, Oh, first off, just the number of them. Cause obviously there's a lot of high population density. So like a lot of power needs, of course, but then, but then it's like city center. Like you look at like, like the power going to polls. I don't know. Let's find some videos or something. I'm sure there's like explainers.

**Dave Jones:** It's like ethernets, like cable tied straight onto main. It's basically like you look at it and you're like, what am I looking at?

**Chris Gammell:** And then it looks like if you asked a generative AI, like to like show you power lines, it like draws that sort of thing. Right. Yeah.

**Dave Jones:** It's really incredible.

**Chris Gammell:** That's off to the people that can actually maintain it. If you can, I mean like that's, that's very impressive, but it doesn't look, it doesn't look clean. You know, like you compare it like that then to like someone who's got like buried, like you guys have a buried lines, right? Where you don't see any wires.

**Dave Jones:** Yeah.

**Chris Gammell:** It's like, Oh man, I mean, granted you're in a suburb, but like, that difference is stark, you know?

**Dave Jones:** How common is underground cabling in the US?

**Chris Gammell:** It is, it depends on the age of the, of the development usually.

**Dave Jones:** Same, same here. Same here. It started in the eighties, I think.

**Chris Gammell:** Yeah.

**Dave Jones:** Something like that. Don't quote me,

**Chris Gammell:** but yeah. So like my neighborhood's very old where I live now. And my old neighborhood, I don't know. Well, I think some of it's also like, like features as well. Like if you can't dig a whole bunch, like if you can get deep enough. Right.

**Dave Jones:** If you've got like a water table or, you know, something. Yeah.

**Chris Gammell:** I think like freeze lines up north and stuff like that too. So like,

**Dave Jones:** Oh, okay. When someone used to live in Cleveland, that's right.

**Chris Gammell:** I was like, like to my street, like I was probably set back like probably like 50 to 75 meters off the street. Like it was pretty far to the street.

**Dave Jones:** Yeah.

**Chris Gammell:** And, and so I had, I had a cable, I had like my own pole in my front yard and then the wire came all the way to my house. And it was long, it was long wire. Yeah. Yeah. That sounds about right. Actually. Yeah. Yeah.

**Dave Jones:** Was that underground from the pole? No, that was above ground. Yeah. That was above ground. Right.

**Chris Gammell:** But then sometimes, um, it was mixed media. So then I, I would walk to the subdivision next to me and they were all underground. So you would see like basically where the incoming, you know, you'd have like an incoming transformer and they would just like go underground and that would then feed that whole subdivision sort of thing.

**Dave Jones:** Got it.

**Chris Gammell:** Yeah.

**Dave Jones:** Hmm.

**Chris Gammell:** So.

**Dave Jones:** Very cool. Yeah.

**Chris Gammell:** Except when the power goes out.

**Dave Jones:** Yeah. Exactly.

**Chris Gammell:** Yeah. Yeah. Oh boy.

**Dave Jones:** Yeah. I don't know how they, how they do it. Like how, how do you replace like, cause if water gets in there, it can rot away and you know, like, Oh, I don't know how they maintain that underground stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** It doesn't seem like a very forgiving area. Yeah. Yeah. Anyway, because the only thing I remember is like our current house that we're in is like our, um, our phone line cables were completely rotted away. This is when, you know, my first one, the early days of the blog, when I was like up uploading my videos via a 56 K modem. Right. Wow. It was like, wow. So heavy, heavy file compression and uploading.

**Chris Gammell:** Back in my day, it was easier to just mail your memes to people.

**Dave Jones:** That's it.

**Chris Gammell:** Higher bandwidth. Sneaking it. Yep.

**Dave Jones:** And, uh, yeah. And like, it was just so bad cause all of our copper cables were just eaten away. Cause you would actually like, I was actually down in the pit checking out the wiring and stuff. And it's just, Oh my God, the pitch is fills with water and all the cables just rotted and everything.

**Chris Gammell:** What's the pit? What is the pit?

**Dave Jones:** The pit is the, uh, cable pit. Cause all of our phone lines are underground. So they go in like, they'll, there'll be like a, a man sized cable pit where you can actually either hop down into, or, or you can actually reach down into, which has all the, uh, terminations, you know, all the phone line.

**Chris Gammell:** You would actually do this as a civilian? You would have.

**Dave Jones:** Really? Yeah. You can just lift it up. It's just, is just a concrete, um, thing. And you put a metal bar in there and you lift it up and you know, yeah.

**Chris Gammell:** This is not making any sense to me at all, but I can't visualize it. Yeah. I'm imagining you like going down a manhole kind of thing.

**Dave Jones:** I'll try and find a photo for you. Okay.

**Speaker ?:** Yeah.

**Chris Gammell:** But you had access to your neighbor's telephone terminations.

**Dave Jones:** Yeah. Yes. Totally.

**Chris Gammell:** Sounds like some, some Snoop worthy type things there. Yeah. Not like it was encrypted communications. You could just like go and tap someone else's lines.

**Dave Jones:** You could. Yeah. Yes. I could certainly do that. Yep. Huh.

**Chris Gammell:** That, uh,

**Dave Jones:** every, every, every street. Yeah. Um, yeah, I'm trying to find a, you know, it's like a telecoms pit.

**Chris Gammell:** Come pit. But it wasn't like controlled area. I mean, like it wasn't even locked.

**Dave Jones:** No, no. Look, I'll.

**Chris Gammell:** These aren't that nice. You're not Canadians. Come on, man. I'm not that trustworthy.

**Dave Jones:** There you go. I'm posting you an image of what a typical one, a typical small one would look like. There you go. You have it. It's just, it just sits on the ground. It's just got a concrete thing on top. It weighs 30 kilos. It's actually marked 30 kilos.

**Chris Gammell:** I'm doing stuff like this. Yeah.

**Dave Jones:** Yeah. Yeah. And you know, we might have that as well here.

**Chris Gammell:** I don't even know. Right. To be honest.

**Dave Jones:** Yeah. And I don't usually open those things up. You'll, you'll find all, all the terminations for every house on your street. Yeah. Very common.

**Chris Gammell:** Oh man. Google chat. just tried to give me some suggestions on after you sent me this photo. Yeah. And it's one of the suggestion. One of the suggested responses is I'm in. What? Like you were sending me a photo of that. I should go break into this. Oh, right. Pit.

**Dave Jones:** Oh God.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. There you go. Interesting. Very common. Anyway, that would just, um, rot it. Oh yeah. I've got a photo of one with cables in it. Here you go. This is what. Now we're talking. Good stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** Here we go. Boom. Check that out.

**Chris Gammell:** That looks horrendous.

**Dave Jones:** That is like a, yeah.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** Typical kind of rat's nest.

**Chris Gammell:** Yeah.

**Dave Jones:** Of, of wise.

**Chris Gammell:** Yeah. Except in, in Australia, I'm sure it's spider's nest, right?

**Dave Jones:** Right. No,

**Chris Gammell:** something like that. Yeah.

**Dave Jones:** No, we call them rat's nest here, but usually like, um, they, they won't have like the, uh, number of the house on it. It'll be some obscure other number and you'd have to have a show to look it up or something like that, you know? So if you did want to tap into, you know, your neighbors one, yeah, step them all.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh boy. Yeah. Well, I could do that. Um, no. Okay. No, I won't mention it.

**Chris Gammell:** He was going to say at his office park. I'm betting. Yeah.

**Dave Jones:** Not saying a word.

**Chris Gammell:** Got it. Okay. No worries. I can say it for you. Dave has access to a room. He probably is not supposed to have access to. That was my guess without actually having talked to him before this. That's what my guess is.

**Dave Jones:** Well, what would give you that idea?

**Chris Gammell:** Just how awkward you're sounding about this.

**Dave Jones:** Right. Oh boy. Yeah. Anyway. Yep. Next.

**Chris Gammell:** All right. Uh, what do you think about the, uh, bricking of the car thing? Did you see that, that article?

**Dave Jones:** Bricking of the car thing?

**Chris Gammell:** Yeah. So Spotify had this.

**Dave Jones:** A car has been bricked.

**Chris Gammell:** No, no, no, no. This is, uh, although, well, that's increasingly a problem too. Spotify had this pretty cool idea for like a device, basically like a crappy. Do you remember, um, when Jay Carlson came back on the show and he talked about the Linux devices? Did you, did you ever listen to that episode when he was on? I don't recall. Okay. Okay. So Jay came back on, he's like, you know, one of his students was actually building something very much like this, where it was basically a, uh, custom embedded Linux device. All it did was it like had ethernet in and he wrote some custom code for it and he got it working with Spotify. Right. So it was just basically a Spotify listener. And that's basically what Spotify built, uh, and then sold them and they were called car things, but they were, uh,

**Dave Jones:** car things,

**Chris Gammell:** car. It was literally, it was called the car thing. Yeah. That's what it was called. It's a very confusing name, but, um, the idea is if you're, if you have like an old school car, like if you had a, just a Bluetooth connection. It's a little,

**Dave Jones:** it's a little LCD display with a dial. Has it got a dial on it?

**Chris Gammell:** That's right. Yeah. It's a dial. Right. Exactly.

**Dave Jones:** Okay.

**Chris Gammell:** And, um, and they bricked them all. They're bricking them all because at the end of the day.

**Dave Jones:** I was going to say that that's what I actually want here. That's what I actually want here.

**Chris Gammell:** Oh, you might be able to get one secondhand. There's so if you watch this video, damn it, Jeff, the guy that does the channel, he, he didn't end up hacking his, this is a bit of a misnomer on the thing. He's basically implementing someone else's firmware that reprograms this thing. And then uses a private service. And he was showcasing how to do it as far as I understood it. And, uh, but now there's kind of like some open source tooling around this as well. They were trying to push Spotify to open source the whole thing, but it doesn't seem like that's likely, but you could still buy these on the open market. And people are using them like you're talking about, where it's just a, a desk device. Basically it's just like a little smart, you know,

**Dave Jones:** radio. Well, it won't be very smart after December 9th.

**Chris Gammell:** Right. Exactly.

**Dave Jones:** I'm on the website. Car thing will stop operating after December 9th. That's right.

**Chris Gammell:** Yeah. And they're intentionally breaking them all. It's not like they're like just shutting down the service. They're actually going to send an update. I think that will kill them.

**Dave Jones:** Why?

**Chris Gammell:** I think lawyers, Dave, I think that's the answer.

**Dave Jones:** Yeah. But isn't this, uh, like I can use Spotify on my tablet or whatever. I can use it on my phone. See at the moment here, the reason I want something like I want like a, just an easy use Spotify interface. That's always there at the moment. I've got an old tablet, which is hooked up to my amplifier here, which is hooked up to my speakers in the lab. And every time I want to go use it, I've got to, Oh, bloody turn on the tablet, wait for it to bloody start up. And then I've got to log into the stupid thing. And then I've got to open the Spotify app and then we are bloody hell. No, no, I just want it always there. And I can just tap it. Yeah. And it goes,

**Chris Gammell:** I think what's happening. This is just me conjecture. I'm not sure. You're not remembering the video either. I'm pretty sure there's a bounce service. Basically like there's a hosted thing for, for the, for the car things. They're basically authorizing as devices onto your account. And then that's basically.

**Dave Jones:** I thought it would have. Yeah. I thought it would have just logged into your account. I thought it'd just be like a little Androidy tablety, custom Androidy tablet thing with a Spotify app and a login.

**Chris Gammell:** No. Cause this is like, I don't think this has enough juice to be a full, it's like pretty underpowered, but yeah, I think it's talking to a, like a relay service effectively. And the relay service is also going to be shut down and that's why they're not supporting it anymore. So. Yeah. That sucks. You know? Yeah. It kind of sucks. Cause it seems like it's, it's finding kind of a new life. We'll see what happens. Might be worth getting one. Try it out yourself. You know?

**Dave Jones:** Yeah. But if it's just going to die, what's the point? Or is it the thing?

**Chris Gammell:** So there's new jailbroken firmware that points at a new service that you can, yeah, that sort of thing. So. Right. Okay.

**Dave Jones:** But then you're reliant upon that new service.

**Chris Gammell:** It's open source. It's fine. I mean, like, yes, you're right.

**Dave Jones:** Yes. But somebody's got to run the server somewhere.

**Chris Gammell:** It's true. It's true. Right.

**Dave Jones:** Yeah. At some point there's,

**Chris Gammell:** there's a human in the loop. Yeah. There's, it's, you know, there's a man in the middle. Yeah. Yeah.

**Dave Jones:** So. It's. I don't know. Anyway, like half of me says like, Oh, class action lawsuit. Right. And the other half and the other freedom goes, no, because you signed up. What, what company, what right do you have? Even if you bought the thing, you own it. You don't have a right to force a company to maintain a service that you bought. They have the right to shut it down if they so choose. And it's your stupid fault for buying into that system. That is reliant upon them.

**Chris Gammell:** You know better. Yeah.

**Dave Jones:** Yeah. Okay. Exactly.

**Chris Gammell:** So. That's a hot take. No, that's the, that's the freedom side of me. It's the free market you're saying. Yeah. I guess so.

**Dave Jones:** It's a free market. No, you can't force companies to do shit.

**Chris Gammell:** You know? No, you don't. Yeah, you can't, but you can, you can. Well, you should. Flash their name with paint, you know, and just say. Yes. Oh yeah, absolutely.

**Dave Jones:** You can slag them off until the cows. Yeah,

**Chris Gammell:** there you go. Yeah. Yeah.

**Dave Jones:** Yep. Sure.

**Chris Gammell:** I'm not saying that Spotify has to do this. It's basically because people saying that you should, they should open source the firmware.

**Dave Jones:** So it's easier to repurpose that sort of thing. That would be nice. That would give them. Yeah. I don't know why they don't do that. Lawyers. Lawyers. This is the answer. Yep. Always the answer.

**Chris Gammell:** Same answer. Yep.

**Dave Jones:** Yeah. Jeez. Yep. Yep. Hmm. I don't know. My son came home, my eldest one came home from school the other day and he said, oh, we're talking about careers and stuff like this. And I don't know who, but somebody was talking about, oh, the best career is a lawyer because they earn the most. I'm going, oh, no, just, just no. And, and then I had to explain with him that you're basically a surf, right? You've got, you, you've got, you're so like under the pump as a lawyer. You've, you've got to account for every six minutes of your time.

**Chris Gammell:** That's right.

**Dave Jones:** Like you are like, it's just like, you have to book every six minutes.

**Chris Gammell:** It's synchronized your coffee break and your potty break.

**Dave Jones:** Yes. It's just no. It's just, yeah. Yeah. Nightmare.

**Chris Gammell:** Yeah. No, it's, I would not recommend it personally. I happen to be married to a lawyer who doesn't operate as an attorney.

**Dave Jones:** And I have a brother-in-law who's an attorney. I was going to say, yeah,

**Chris Gammell:** your, your son should go talk to his uncle. Yeah. It's, it's a tough life, you know, like there's, there's a lot of, a lot of stuff there. That's interesting. Yeah. Yeah. What would you say? I don't know what I would tell a kid if they, not saying that, that Sagan asked this, but like if, if you were teaching that class today, Dave, and you'd say the number one job is, what would you say?

**Dave Jones:** You can't, you can't predict it. So don't even try. Just build your skill set, build your talent stack. Right. Number one, number one job, according to Davis,

**Chris Gammell:** be a contrarian. That's what it is. Okay.

**Dave Jones:** Be good at a lot of stuff that, that allows you to combine skills together to make you more valuable than 99% of other humans. That's what my advice would be to young kids.

**Chris Gammell:** That is incorrect. The correct answer is anesthesiologists. Obviously. I don't know. Yeah, I know. Right. Yeah. Yeah.

**Dave Jones:** All right.

**Chris Gammell:** You're saying that they put people to sleep for a living. That is correct, Dave. Very good. Yes. You must've put that together with all your skills.

**Dave Jones:** Have multiple skills, a big, a big talent stack, make it wide. So you can combine.

**Speaker ?:** I mean,

**Dave Jones:** you could say that.

**Chris Gammell:** You could also say, join a, uh, uh, uh, protected industry, like lawyers or doctors or, you know, like that is. Electrician. Electrician. Right. Exactly.

**Dave Jones:** No one keeps asking me why I didn't, why I didn't wire my own switchboard. Because it doesn't matter what qualifications you got. It's a protected industry.

**Chris Gammell:** Yeah.

**Dave Jones:** If I want to get my electrician's license, I, I have to go through the full, my qualifications do not matter. I have to go through the entire apprenticeship from the start. No exemptions. None. Zero. I've, I've, I've got a friend who's in his forties.

**Chris Gammell:** Why would you get an exemption?

**Dave Jones:** Because I've already studied all of it. Right. I already have a full of the age.

**Chris Gammell:** I guess. I don't know. Yeah.

**Dave Jones:** You know, like, like you don't have to learn basic electrical theory or something like that. Oh, I see. You would, right. Yeah. There's zero. Zero exemptions.

**Chris Gammell:** I guess I don't know what an apprenticeship looks like in your country or just broadly, you know, like, there's not like a classroom component though. There are like a degree component. And it's just, it's just experiential, right? No,

**Dave Jones:** no, no. You have to do, I think it's a certificate for in electrical or something. Don't quote me on that. It's some sort of certificate. I don't even know what those things were mean. So, yeah. So, so it certainly is a, an educational certificate.

**Chris Gammell:** So there's no like testing out of, of the capabilities and stuff like that.

**Dave Jones:** But you can't,

**Chris Gammell:** you can't take a test and be like, I already know blank, blank, blank. You just have to do it all.

**Dave Jones:** That's how it used to be. One of the things I totally regret is not getting my, electrician's license. When you could just sit the exam, you could just sit the exam. And if you pass the exam, you've got your license and Bob's your uncle. And then what? Yep. And then you could just, and then it became a protected industry. It became a fully protected industry. You have to do a full apprenticeship, which means you've got to work full time under a licensed electrician.

**Chris Gammell:** Coffee errand boy. Yes.

**Dave Jones:** Yeah. Yeah. So yeah, there's, there's no way there is literally no other. Well, there is, there's one other sort of restricted class license. And I actually read it. I thought, Oh, maybe I can get a restricted class license. And it's like, no, you're literally not allowed to do anything. You're allowed to touch wires, but you're not allowed to join them or something. You know, it's just something ridiculous like that. And it's, it's totally pointless. It gives you no ability.

**Chris Gammell:** Sounds like lawyers got to that one too.

**Dave Jones:** Yeah. I think what, what that one was intended for was for those who could get a partial license to like pool cables and stuff like that. That would make sense. Sure. Sure. Yeah. Yeah. Yeah. So, you know, it gives you some partial thing. Um, yeah, but no, it's a fully protected industry. So I got a friend who's in his forties and he decided to go back and become an electrician. Yeah. And, and he's got it. Yeah. So he's now he's, he's in his forties, you know, he's got a wife and kids and he's, here he is. Here he is apprenticing to an electrician. How long,

**Chris Gammell:** how long does the apprenticeship take?

**Dave Jones:** Four years, I think.

**Chris Gammell:** Four years. Wow.

**Dave Jones:** Four years full time. And you can't do it part time. You've got to devote to it full time.

**Chris Gammell:** Is it like full pay or is it like degraded pay too?

**Dave Jones:** Oh yeah. I, I don't know. Like fixed pay sort of thing like that. Apprentice electrician would get paid.

**Chris Gammell:** Yeah. Yeah. Don't know. I don't have a good feeling. I don't even know here. Like what, I guess I could look that up, but, um, I think you get paid well here, but I don't know.

**Dave Jones:** I get a minimum, minimum, you might get minimum apprentice wage rates. Oh God, that's not good. That's rough. Yeah. Yeah. Okay. Apprentice and trainee pay rates. Yeah. You might get sort of minimum.

**Chris Gammell:** Like fixed. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** But that also might be protecting you from the downside as well. Like someone who's like, well, I'm actually not going to pay anything for the next four years.

**Dave Jones:** Oh no, you can't do that here in Australia. We have very strict laws.

**Chris Gammell:** Oh good. Good.

**Dave Jones:** A first year apprentice is $631 a week. A fourth year apprentice goes up to 930. So that would be minimum. Like if you work for, you know, if you work for someone who really likes you and wants to pay you well, they can pay you more. I mean, sure. Yeah. But that is the absolute minimum for a standard 38 hour work week. Yeah.

**Chris Gammell:** Wow.

**Dave Jones:** Yeah. And you got to do that. I think, yes, you got to do it for four years, four years of apprenticeship. Any other qualifications don't matter. Squat. It's totally protected. We should,

**Chris Gammell:** we should make up some requirements for, you know, I guess we're not going to be in charge of electronics generally. We need to come up with some kind of like sub, sub group of electronics design and then create a industry group around it and then create some, some, some walls around that garden. You know what I'm saying?

**Dave Jones:** Right. You want to, you want to protect the electronics industry.

**Chris Gammell:** That's right. That's right. Like a, like a honey badger, you know?

**Dave Jones:** No, thanks. You're on your own.

**Chris Gammell:** Oh, you don't want to do that. You don't want to, you don't want to start a union. No, it's bullshit. Okay. Yeah. No.

**Dave Jones:** I've done a video on this here, here in Australia, you don't need any qualifications at all to work as an electronics engineer.

**Chris Gammell:** Yeah. It was like when the, I remember that story we talked about on The Amp Hour. It was like in Victoria, they were trying to do it for electronics, right?

**Dave Jones:** Yes. Yes, they were electric electronics. It was electronics. It was definitely electronics.

**Chris Gammell:** It was about the term engineer. That's what it was. The term engineer.

**Dave Jones:** They were trying to protect it. I don't know what happened to that. I haven't followed up, but there was that famous case in the U S. What was his name? The Hans somebody in Oregon, was it? And he, you know, they tried to, they tried to find him. Well, they did. They find him because he wrote a letter to the, uh, traffic authority or something like that, telling them how the design of their lights is all wrong. And they went, that's engineering. You are not allowed to do that. You are not a licensed engineer in this state, even though he's a degree qualified engineer back in Norway or somewhere, where he comes from, one of those Nordic countries. And they find him, but he took them to federal court and he won. Um, so, yep. Legend. So,

**Chris Gammell:** yep.

**Dave Jones:** But you're still, yeah, the term is still protected in the,

**Chris Gammell:** we could be the people getting sued. We just have to come up with a new term.

**Dave Jones:** All right. Okay. Yes. Yeah. We could do that. How about smart, smart engineer,

**Chris Gammell:** smart engineer. It's gotta be really terrible, you know, like realtor.

**Dave Jones:** we can simply spell it wrong.

**Chris Gammell:** Oh, there you go.

**Dave Jones:** Because engineers can't spell, right? So, but if we, so if we deliberately spell it wrong, it's like, yeah, I am in engineer.

**Chris Gammell:** How about like I N J U R.

**Dave Jones:** Yep.

**Chris Gammell:** Inger near. N E A R. Inger near.

**Dave Jones:** We, we need to stand up for this. We need to have it ratified.

**Chris Gammell:** We injure people that are near us because we're engineers.

**Dave Jones:** And if we can get it ratified by the ICC, I believe.

**Chris Gammell:** Well,

**Dave Jones:** man,

**Chris Gammell:** that's gotta be easy.

**Dave Jones:** Yeah. I think we can do this.

**Chris Gammell:** Wow. Yeah. I think all you need to do is add a rights reserved at the end of the, the word. And then that's basically nine tenths of the law right there. If only we do some lawyers.

**Dave Jones:** I'm certainly, I'm, I will definitely go ahead with that. If they try and ban the word engineer here in, um, the state of New South Wales.

**Chris Gammell:** Yeah. Screw.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Well, you know, think about the merch,

**Dave Jones:** the merch alone. We'll make it rich. We'll be on our wildest dreams. Yeah.

**Chris Gammell:** Oh, man. Yeah.

**Dave Jones:** I love it.

**Chris Gammell:** What do you got coming up in the next few weeks in the electronics design side of things, Dave? Any big, uh, big videos coming down the pipe?

**Dave Jones:** If I can, Oh, I want to get back into some whiteboard tutorials. Well, you know, there's some old, yeah, I didn't finish my AC series. I finished my DC tutorial series. I didn't finish my AC series. So yeah, I want to finish that off getting back into it. I've been flooded with bloody soldering iron equipment at the moment. So I've got, you know, I've got reviews I haven't done and like, yeah, I don't know. I want to get back to some whiteboard tutorial stuff. Yeah. That'd be nice. Yeah. Hmm. I don't do enough of that these days, you know,

**Chris Gammell:** no time like the present, my friend, no time like the present. Yeah,

**Dave Jones:** absolutely.

**Chris Gammell:** I, I got my rev B boards back and they mostly work. So those are the ones that I, that relay board that I mentioned, I rotated the board, the connector 180 degrees. I'm sure I talked about that on here.

**Dave Jones:** Possibly. Yeah.

**Chris Gammell:** Yeah. A hundred, a hundred degrees. I did a live stream where I, I live streamed the whole thing. And it wasn't popular enough that anyone's like, Hey, that's backwards. So it is now fixed.

**Dave Jones:** No one spotted it. Ah, yeah. Yeah.

**Chris Gammell:** They get to see all the fixes in, in the session, fifth session of streaming though. And yeah, now it plugs in and works, works well. So then I think I, I got to figure out what's, what else to build on top of this thing. So I, so this is like a, this is like a, effectively like a shield that plugs into a cellular board that I, you know, have been working on for a long time. And this one is just relays, something stupid.

**Dave Jones:** Cool. Yeah.

**Chris Gammell:** Just like four, four relays that can do 120 volts and 20 amps. Okay. Sorry. 240, 240 at 20 amps. Right. So you're doing,

**Dave Jones:** what is this for mains switching or something?

**Chris Gammell:** Yes, this can do, Oh no, actually it's, there's 120 at, Oh, that's different than I thought it was. Anyways. Yes. 120 at 20 amps. Right. Yeah. So main switching, but it also can do DC. You can do up to 28 volts. So, so now I have like this form factor proven out. Like now that I, so that was the whole idea is to prove out this form factor. It's like a PCB front panel effectively that plugs into a board that's below it. Now I have a, a working, mostly working PCB panel or PCB front panel. And then I put components on top of instead of like a display panel. It's like a, kind of a place to load components onto. And so I got to figure out something else interesting to do there. And you know, this was kind of, this was, this one was inspired by a smart locker. I had built way back in the day, just needing to switch 12 volts into the, into the lights and the real solenoid and stuff like that. And now I'm not sure what's next. Maybe high speed ADC. Maybe a few of ideas. Let me know. If you have needs, Dave, I can build you something.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah. All right. Well, we will have another one soon. Yeah.

**Dave Jones:** Catch you next time.

**Chris Gammell:** Talk to you later.

**Speaker ?:** Bye.
