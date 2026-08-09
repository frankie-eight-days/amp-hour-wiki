---
episode: 552
title: Shouting at chips with Colin O'Flynn
url: https://theamphour.com/552-shouting-at-chips-with-colin-oflynn/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released August 1st, 2021. Episode 552. Shouting at Chips with Colin O'Flynn. Welcome to the Empire. I'm Chris Gammell of Contextual Electronics.

**Colin Oflynn:** I'm Colin O'Flynn of New A.E. Technology and for one more month of Dalhousie University.

**Chris Gammell:** All right. How you doing, Colin? It's been a while. Yeah, pretty good. Pretty good. So no more Professor O'Flynn? Is that the thought here? Yeah, got to remove that. Okay. All right. Well, you know, is this going to be like a clip of you throwing out all of your corduroy coats with the elbow patches on it or something?

**Colin Oflynn:** Yeah, well, you can't. It's like everything, right? So I'm still going to end up as adjunct, right? So I'm still going to be involved in academia. It's like you never you can never fully escape, I think, is the answer.

**Chris Gammell:** Yeah, yeah, yeah, yeah. Well, what what prompted the move out of academia?

**Colin Oflynn:** It was a bit a long time, you know, coming maybe. But and it wasn't. It's funny because some people have left that really were I want to say negative about it, right? They they didn't like it. And I didn't have that experience. I think it was just a bit of juggling too much. I was trying to do sort of a bit of startup life at the same time of academia. And it was it was a bit like, you know what, it's trying to do too much at once.

**Chris Gammell:** So, yeah. Yeah, it's tough, right? Yeah. I mean, you're growing your business, you know, you you do training. So people don't remember Colin's been on the show before. And I get to hang out with Colin back in the olden days when we went to conferences and there were security conferences. And so Colin is a security researcher and he makes things like the chip whisperer and the chip shouter. I think that's actually come out since we had you. I don't even remember the last time you were on the show. It was a long time ago.

**Colin Oflynn:** So, yeah, probably was after that. Now that I'm thinking of it. That's true. It was wild.

**Chris Gammell:** Yeah. So it's a while. And these are well, maybe you could tell people what those those things are as well.

**Colin Oflynn:** Yeah. So, I mean, the the backstory, right, is I'm doing security tooling work. So I made a product chip whisperer initially, which was a Kickstarter. And it was for doing side channel power analysis and fault injection. So this was like 2014, 2015 ish, I think the the original. That was a while ago. Yeah. Yeah. Which is it's still using. I mean, some of the like Spartan 6 stuff has gotten pretty long in the tooth. So we're actually going to do an update to that that should be live pretty soon.

**Chris Gammell:** No big deal. You can't find parts of the old stuff, can't find parts of the new stuff. What's the difference?

**Colin Oflynn:** Yeah. Well, yeah, I mean, it'll be interesting, right, with R&D. We had some new stuff we're planning on doing. But like, are you going to design something when you so it's like just a panic? OK, if we know this kind of works, let's just do that. Right. Build that.

**Chris Gammell:** Rolling the dice. Rolling the dice. So it's a whole whole new game. OK, maybe as a quick refresher for people, what is side channel analysis as well?

**Colin Oflynn:** Yeah. So side channel analysis is when you're the sort of classic examples are in a human factor way. Right. It's like additional information that's leaked. So there is a bunch of fun examples of this. There's like the pizza index, I think, in D.C. And it's like if there's a bunch of late night orders for pizza, like coincided with military operations starting. Yeah. On embedded devices, it's more commonly like timing. The time it takes for a device to execute a comparison tells you how many characters were right in the comparison. What I look at particularly is power. So it's like the power used by the device is related to data being processed and stuff like that. So you can actually recover encryption keys really effectively from digital devices with just power measurement.

**Chris Gammell:** So, yeah, that was the demo when you I got to go to one of your trainings and when you were like recovering the keys, I mean, it's just like magic. It was kind of like in the what's it called? Like in the like movies when, you know, the codes are on the screen and then just kind of all lines up. You're like and then you just have this encryption key and this is like, oh, OK. And that's because of the statistic analysis, right, of like how much of zero versus a one is that sort of made sense to me. But then the back calculating it, that's that's the part that always kind of blew my mind.

**Colin Oflynn:** Yeah. I mean, it's pretty amazing. And when you first explain it, no one believes it works. I mean, I didn't believe it worked. That's how I kind of got into it. Right. It's crazy. That doesn't work. And like really fundamentally, you can think of like the on the digital data bus. It's like setting that data bus higher or lower. It's charging this tiny capacitance right of the data bus line. It's like, well, that takes power. And if you average that enough, you will see that power difference. Right. Yeah. Yeah. It's you think it's not going to work, but like people do it on, you know, gigahertz processors.

**Chris Gammell:** Right. Right. And so, I mean, the tooling like this chip whisper and stuff like that, too, it is it's making it more accessible. I remember it was like more scriptable. It did Python, Python stuff for writing scripts on it.

**Colin Oflynn:** Yeah. Yeah, exactly. I mean, and that was kind of the like the back story to it. Right. The I started doing research in the area and it's like fundamentally, it's not different what it's doing, but it's like you had to script together a bunch of oscilloscopes and like you're using Visa and all this stuff. Right. That anyone who's done that knows it's like not super portable. So if you want to give that to someone else, they've got to figure out, OK, how am I going to take your work and get to work in my setup, which is different, blah, blah, blah. So it's like, well, let's make something really simple that people can replicate everywhere.

**Chris Gammell:** Right. Right. Exactly. And so how how has it changed then? Since the last time you've been on the show, how is it how is the the nature of, you know, this this field changed in terms of is it gotten harder? Has it gotten easier? Is it gotten more widespread? You know, what are people doing kind of in the security industry? I don't think we've actually had a security guest on in a while.

**Colin Oflynn:** Yeah. I mean, it's it's interesting because this this field is relatively old. I mean, the field was introduced in like 1999. You could say the people that cared for the longest time were like, you know, Visa, MasterCard and especially KTV type people. Right. So countermeasures existed. But in consumer devices, you never heard of it at all. Yeah. I feel like that that is changing. Not as fast as I thought it would be. But I mean, you can see the Silicon Labs EFR 32 MG 21 A and B. They talk about, you know, power analysis countermeasures. There's your start to see basically you're seeing like what I call consumer devices. Right. So devices you might use yourself, you know, without an NDA. Basically, you don't need to sign an NDA in order. Millions of them are starting to have protection against this stuff. So it seems like people care or there's customer demand somewhere.

**Chris Gammell:** Yeah. OK. And then do you then see on the other side, chip vendors are providing more defenses against it, I guess. I mean, like what are what is the implication, you know, in any kind of system like this? I would imagine that there's evolutionary kind of aspect to it all of like if there's more people able to do these attacks, then there would be more defenses against those kind of attacks.

**Colin Oflynn:** Yeah, exactly. That's what I mean with like these people bringing it up like Silicon Labs. So that device claims countermeasures against some of this. Right. So it's coming. It's still a little slow. I mean, there's all this lag right in the design time of the chips is so long. But when I've talked to vendors before, it's really like the end customers aren't asking for it. So then they're not designing it in. So it's like, you know, if whoever's making IoT, whatever, doesn't think they need this, then. They don't have demand for it. So, you know, they're not right. I see all this stuff.

**Chris Gammell:** Right. It kind of does. It does beg the question of like, is it the chip vendors adding more features that drives the adoption? Or is it the push from the people in the field that ultimately drives the chip vendors? Right. It's like that push pull side of things.

**Colin Oflynn:** Yeah. Yeah, exactly. And that's the part, you know, when I was starting this that I thought was kind of like what you needed. Right. Is you almost need to like leapfrog because people didn't care because they didn't know about it. Right. So it was like self-fulfilling almost. It's like, wow, no one knows what side channel. So we don't care about side channel. So there's no chips you can do with it.

**Chris Gammell:** So, yeah. And I'd imagine like the other thing, too, is that there's almost like the perception of like, well, I'm not big enough for anyone to care about reverse engineering my device. Right. Like if I'm a small device, maybe consumer products. Right. You could reverse engineer, get get some keys out of that and then spoof a wide range of, you know, like Google Home speakers. Or something like that. But if it's just, you know, some small industrial device, you're like, oh, who's going to bother with this? But that's kind of security models in the first place of just, you know, obscurity and similar.

**Colin Oflynn:** Yeah. I mean, and it's interesting to loop back. So we're moving buildings down. The building came with this like access control system. So I started I never looked at those before, to be honest, you know, despite being in security. Yeah. And there's a lot of good stuff. Have you had Sammy Kamkar on this show before? I didn't think of that.

**Chris Gammell:** I think so. It's been a while. I know Sammy, but yeah, I think Sammy's been on. Jeez.

**Colin Oflynn:** I meant to look that up before because I couldn't remember either. He's done a lot of this work. He looked at it forever.

**Chris Gammell:** Yeah. Sammy's got a new company doing this stuff. Since we talked to him, he was talking about all the hacks and stuff. Oh, yeah. I recorded it at his place, I think. Yeah. Okay. So, yeah, we talked about all those hacks and stuff. That was episode 308. So people will hopefully, you know, forgive me if I don't remember from five years ago.

**Colin Oflynn:** I mean, did I talk to him on a podcast or did I just talk to him? That's right.

**Chris Gammell:** Yeah.

**Colin Oflynn:** Which way? What is real life, Colin? What is real life? I said, what is real life? Yeah. Right. Yeah. Like, you know, so we've been looking at it forever, but it's fun when you, like, finally get a chance to kind of have an excuse to look at it. And it's like, oh, yeah. I mean, a lot of them are pretty terrible. Is it? Yeah. And so the one in here is pretty old. So I've been upgrading it to what's basically the particular company's latest one that they had to offer. So this one's like Kantec, which I think is a smaller system, it seems, than some of the others. But yeah, like, you know, it's funny. They list AES everywhere. It's like an all their marketing material. It's like AES 128. Uh-huh. Boom. Right. It's there. But it's like, so the main unit on the wall communicates back to some server. But when you're setting it up, it's like, what is your UDP port? Tell me what port you're going to use to talk to this device. Right. So it's not like SSL. It's just like encrypted. And there's a key in the software. It's like, put your 16 byte key in here.

**Chris Gammell:** So it's consumer choice, Colin. Okay. That's what people want. Give the people what they want. Ah, so. Yeah.

**Colin Oflynn:** I see why he made a company to do this better.

**Chris Gammell:** Oh, yeah. Yeah. I think, so John Barry, who I work with now, he did a little bit of that at WeWork, and he talked about that when he was on the show. It sounds like a disparate, what it, when John's told me about it, when Sammy's told me about it, it seems like it's, that industry specifically is, because it's sold so vertically, it's sold to like building owners, to people that own multiple buildings, especially. It's like, when you have like a sales force like that too, like, you know, it can be buzzwordy, but really it's like, it's going to be about connections and like that sort of thing, you know? And there's comparisons between vendors, of course, and there are going to be some that are better than others. But I can't imagine it's like the most vetted solution that's out there because it's like, well, you know, you're not getting in the door, not getting in the door. Sorry, those were quote fingers for people just listening. Terrible puns all around here. It's a, it's very, it's a limited field, I would imagine. And so there's not as much competition there.

**Colin Oflynn:** No, I think you're right. Like that's, that's for sure. I mean, this system seems pretty old. The one that was in here is quite old and even their upgrade one. Yeah. Yeah. I mean, like everything I'm buying a bit through eBay, I got a whole bunch of the readers actually to look at.

**Chris Gammell:** Oh, so you're not just doing, I think, okay. I thought you were just poking around in your system. You're saying this is now a new, a new area of interest.

**Colin Oflynn:** Well, yeah. So I, I will, so I'm upgrading my system. So this is the new ones. These ones have like smart card capability. Cause the one that are on here are like the clonable. It's just like an RFID, right? EEPROM. Yep. It's like, okay. It's, I feel like if I have a security building company or security company, I shouldn't be using that. Right.

**Chris Gammell:** So I did, I did get a cloner. Those things are pretty fun. I forget what they're called. They're like the, it was like a third generation, you know, just like the Proxmart. Proxmart. Yeah. Yeah. Those. Yeah. Well, yeah. Those are super fun. So this was like also, you know. Yeah. Yeah. Yeah. Never had one for years.

**Colin Oflynn:** Yeah. So I finally had an excuse and it actually worked out because I used it to clone. Like we didn't have enough badges. So it's like, oh great. I'll just clone them. Cause it doesn't matter. Right.

**Chris Gammell:** Right. Right. But at that point it's basically like owning a, you know, like one of those key cutting machines, you know, that's the point. Right. You know, you don't need any specialized skill. You just need the original and then you make a copy and then you're like, oh yeah, good to go. You know? Yeah. Exactly. So yeah. Yeah. Well, it's even, it's easier, right? It's way easier. I just like put it on and yeah. Less a grinding metal sounds. So yeah. Right. That's great. That's great. I mean, that's, there's probably not like super crazy tech in there either though. Cause another thing is like, it's just like this very widespread kind of thing. Right. So it's, it's, it probably has very strong cost constraints versus, versus something that might be, you know, a mobile phone or equivalent. Right.

**Colin Oflynn:** Yeah. And that's, and that's part of that. See, so I ripped one apart and it's like an STM 32 episodes, or it's like multi-processors actually, cause they have BLE and all this stuff in it because you can use your phone. You can use, you know, the may high frequency cards, low frequency cards, but yeah. So the core processor that I think I haven't rifted apart far enough to confirm that it has like an encrypted, right. AES 48 or AES 128 bus over RS 485 back to the main unit, but there's an STM 32 F zero in there and it's like, okay, so clearly it's doing software crypto in that. So, and that particular device I don't think has some of the higher level protection. So you can just dump the keys out of it. I'm, I'm guessing kind of by design. So we'll see. It's like two do.

**Chris Gammell:** So obviously this shows that you are not lacking in terms of things to do. This also is, so we kind of refer to the beginning. I mean, you were doing the academic thing. You're doing this new office, but also side projects. And then you're built your business, your training, whatever back to the academic stuff real quick. I mean, were you doing, I mean, that was like a research position. Is that right? You were doing like actual research on security.

**Colin Oflynn:** Yeah. Sort of a standard sort of like assistant professor, right. You do research, you do some classes, some like undergrad, some grad classes. Okay.

**Chris Gammell:** I guess in the academics, I don't really, you know, I've never, I guess we've had a couple of professors on here before, but is there, I mean, it was just a time thing for getting out of the professor game.

**Colin Oflynn:** Yeah. I mean, this is a good rate. This is like an interesting conversation too, about what is the point of universities and, and across the world, it's, it's not at all limited to, you know, our local one. I think you really see the sort of like push for everyone to go to university. And like the university becomes more like a business. It feels like, right. So they have like strong encouragement to get a certain number of students in, you know, not because it's like, Oh, we have hundreds of students that are going to excel at this program, but like we need to have a hundred students in this program financially. That's right. That's right. We have overhead. Right. So, so that was kind of where it went to. And then we had, I mean, and so they had a strong incentive with COVID, right. To get people back on campus and things like that. So it felt like a bit like, ah, I don't know. I don't know if I fully agreed with it, but I don't want to get paid. You can't really like get paid by the way that they're doing it. Cause it's not like they they're, they're forced to do this per se.

**Chris Gammell:** Right. Like butts in seats equals dollars kind of thing. That idea.

**Colin Oflynn:** Exactly. So it's like, if I'm going to criticize anyone about having more students in, then I shouldn't at the same point, get paid right from those students.

**Chris Gammell:** You heard it here first, folks. Colin O'Flynn wants to work for free. How's, how's your wife feel about that?

**Colin Oflynn:** Stability. Uh, well, it's funny, especially my parents too. Right. They were like, uh, like professor. It's like, it is pretty stable. I mean, it was a bit of like, uh, this could be a huge mistake. It's still the bag feeling. You stick around that. And once you get on tenure track, like you. Right. Just hang out more or less.

**Chris Gammell:** Chill. Chill. Yeah. Yeah, no, it's interesting. It's interesting about the, one of the things that I think about, one of the things that was interesting when you told me about Dalhousie and in general, just like being a professor around security issues and stuff like that is the fact that there was teaching around it. Right. I had not actually heard of that before. And I think that's, you know, that's a feather in their cap that they're teaching what is by design, you know, a leading edge thing, right? And you need to be up on the latest techniques. You need to be trying all the latest things or else you're not really that relevant as a security researcher, I imagine, or a pen tester or whatever. So that alone was kind of interesting to me. But if there is a tenure kind of thing in there, like there's not as much incentive to stay at the leading edge, I would imagine.

**Colin Oflynn:** Yeah, it depends, right? And it depends a bit like where, what the universities are and what they are. Because like, you know, lots of people that, so the guy, when I was a first year student doing physics, our professor, Jeff Don, he's like a battery researcher. So totally unrelated to my field. Right. But he was like an amazing professor for just like first year physics, right? Not like incredibly basic relative to what he does. But on the flip side, he's staying at the leading edge. Like he works with Tesla quite a bit now. He has sort of some local connections there to some, some setups he's done. And so it's funny what it like, you know, and I'm sure everyone's had professors like this. Some are like amazing, right? Some are like clearly kind of checked out a little bit.

**Chris Gammell:** Oh yeah. Yeah. I had some of the latter. The ones that I actually liked were the ones though, the ones that I was most close to, I'm sure people will be super surprised by are the ones who were in industry who were doing hands-on stuff. And the ones that I did not like were the ones who were old school, very theoretical. This doesn't fit my persona at all, of course, but I imagine that you were the former because you are, you're still doing all this stuff and you're pushing stuff out there. So that's good.

**Colin Oflynn:** Yeah. I mean, it's interesting. It's kind of curious too. Like, so I'm not as looped. I mean, I went through Canadian university systems, but like, it seems in Europe, it's much more common. People switch to industry back to academia in terms of professors. Like I've noticed that a lot with, with people I work with there, you know, there's sort of very common shifts back and forth, which is, which is pretty interesting. Like I think here, it seems very much like one or the other. And even, you know, going into industry, it's like, Oh, well, okay. You'll never be able to get back to academia because you won't have the publications kept up. Right.

**Chris Gammell:** Exactly. Yep. Yeah. Same, same in the U S I think. And, you know, just pedigree becomes more of a thing, at least in the U S adjunct seems like they get kind of not treated perfectly. Yeah. So I mean, that's the thing.

**Colin Oflynn:** It's, it's a bit of a carrot. So normally I think the idea is, or I think what it gets used for is like, Oh, you know, do an adjunct for a while. And it's like intern basically. It's like, maybe we'll look at you when there's a position available.

**Chris Gammell:** I see. Right. Right. You can work towards the cushy thing as long as you work really hard for the first. Yeah. Exactly.

**Colin Oflynn:** So, I mean, I'm kind of doing it a bit because, you know, there's some students that are helping supervise and stuff like that. So it's like, officially it's easier if I stay as an adjunct because then you're tied in. Right.

**Chris Gammell:** It's not like a hard cut then.

**Colin Oflynn:** Yeah. Yeah. You know, otherwise it's like some of these students we'd need to find new for, for their supervisory committee and things like that. It's like, I technically couldn't do it if I wasn't associated with the university anymore.

**Chris Gammell:** And yeah, well, I'm sure there's push pull as well. Right. I remember you, you and you ended up hiring some people from the university, too, for the, for new AE. Right.

**Colin Oflynn:** Yeah. Yeah. Right. Which is a great way. I mean, and that's the other kind of value people put out there for the adjunct. It's like, you meet interesting people that, you know, kind of want that, maybe want to leave academia, but still work with you.

**Chris Gammell:** Yeah. Yeah. No, it's great recruiting pipeline. I mean, like I, I'm a very big fan of co-ops and internships. Co-ops are, you know, a little bit better, I think for the time and just the amount you can really sink your teeth into things. But overall, I think any kind of experience to just the real world problems are awesome. And, you know, and to be fair, some college programs too, they, they import real world problems and, you know, they, they either have sponsored research projects or equivalent, but mine did not do that. So I went external. Yeah. Speaking of research projects though. So I had actually brought up your playing around with air tags as well. So this is something you had been doing. And then I talked about it on the show and I very clearly showed that I had no idea what I was talking about as we were talking about it. I basically had looked at the post just prior. What's what was your interest in? Yeah. You know, yeah. Fake it till you make it unless you don't make it. Yeah. So let's, let's roll it back a little bit to that. So air tag stuff, what got you into starting to rip those apart in the first place?

**Colin Oflynn:** Probably the original. I think they just showed up as I said, when there's new stuff, sometimes I'll order them and be like, yeah, this could be fun to look at. So yeah, I think I had tried, I had ordered them. I pre-ordered them just because it was like, ah, this is an interesting thing, right? A little tracking device. Like how are they doing that? So when they showed up, it's sort of like, ah, okay. There was already a few teardowns of it by then. So it was kind of like, let's just see what's in them. To be honest, I, I poked around with them a bit, did some test point stuff. So they have a little NRF device in them, which is pretty interesting because it's a, you know, consumer microcontroller. You could in theory reprogram it. I'm often interested for a lot of these IOT things. They make really nice dev boards. Cause like the little air tag, right? It's just like a little thing like that. If you could reprogram it, you can kind of use it as your own product for something. Or not product, but you know, your own, your own little mesh thing. So yeah, it was, it was a pretty interesting device, but then another, a few other colleagues. So Thomas Roth or stack smashing on Twitter, he had taken an exploit. Another guy live overflow or not, sorry, limited results had done this glitcher on the NRF. So he had looked at these like microcontroller that's in them. And he figured out how to glitch it so that you could recover the firmware. So I know Thomas at the same time I was talking to him. I think he like, God, this was like a good nerd snipe. Right. I had like some photos I sent him and I forget, I think it was night there. It was, yeah, it was night in my time. So he was asleep. So I was like, okay, you're not doing anything this week. And I guarantee it. Cause like here's, you know, these are super hackable because there's all these test points. It's like, you can open the case, you know, it's going to be fun. So I'm pretty sure he like took a train to go buy them. Like right there.

**Chris Gammell:** Nice.

**Colin Oflynn:** That's great. Yeah. And it was like a day later he had already attacked them. Yeah. Like dumped it out.

**Chris Gammell:** Yeah. And so, I mean, so that is, so the NRF 52832 is in there. I remember that because I was trying to source them at the time. I was really pissed that they were, you know, available to everyone except me. Not really everyone. But then the one thing that I had said wrong on that was the UW one or whatever it is, the ultra wide band chip that's on there. I was completely wrong about what that actually does. It's like range finding, I think. And I thought it was like, I'm radar. It was just really bad. Yeah. Yeah. You know, it's like a wiggle, but it goes faster, you know, like a signal that wiggles. Yeah. Pretty close. They say horseshoes and hand grenades and RF. That's what, that's how the, that's how the phrase goes.

**Colin Oflynn:** So I don't know much about that chip either, actually, but I'm just, let me just pull up on black cat. Here's this briefings. There's going to be a talk. So if you're interested, let's see this.

**Chris Gammell:** Are you going to black hat? Black hats in person, right?

**Colin Oflynn:** Yeah. And no, I'm not going in person. That's zero. Got it.

**Chris Gammell:** So it's like a hybrid, a hybrid model this year.

**Colin Oflynn:** Yeah. And they're doing, so they're doing some trainings that are, all the trainings are virtual. Ah, okay. Cause I think it, maybe it was too risky, right? Or anything like that.

**Chris Gammell:** I think, you know, if someone's maybe, maybe you can space people out. Well, you know, for normal talks and stuff like that, but you know, if someone's breathing down your neck as you're trying to troubleshoot, it's like, okay, you're probably in pretty close proximity then. So. Yeah. That's, that's the thing. So. Yeah. Yeah. Here you go. So if you're interested in that one, the U1. That's a, that is a great talk name. Wibbly wobbly timey wimey. What's really inside Apple's U1 chip. Wow. So you are, you're doing training this year as well. Uh, remote. Yep. I'm trying. We'll see how it goes. Have you done any remote trainings before? I always wondered about the, like the, I do remote trainings as well, but there's no hardware aspect to it. I mean, people are on their own for contextual electronics pretty much, but I've talked to Joe Fitz about his trainings. He's went remote. I know Dimitri and, uh, Josh. Josh. Thank you. Josh. Yeah. They also do remote, right? So it's just like, there is, there is the security industry seems like it has, at least the part I know, uh, has made some, some switchovers. So.

**Colin Oflynn:** Yeah. Yeah. I think, I mean, like I only did one early on, like there was one I was going to do in person and I switched to remote and it went okay. It was like one team. So that was pretty smooth. Uh, cause they could, you know, help each other a bit. Um, I think like what you missed right is the, when you're in class, you can walk around and like see if someone's having trouble. And like, that's, I think a big part of it that's missing. So like, I know some changes. So like the, the advanced security training dot training stuff. So that's like Dimitri and Josh and Thomas Roth was involved in it and some other people too. They changed around a bit. So they would have like short videos and a lot of like interactive chat time and stuff like that. So, you know, I, I think the issue is when you tried to like, just take like, ah, we're going to do this training that was in person and just put cameras in front of everyone. It doesn't work very well.

**Chris Gammell:** Yeah. Yeah. I mean, there is something just about that high bandwidth nature. I mean, even now, right? Like the conversation we're having now versus the conversation we'd be having in person. It's just, it's different. It's not necessarily worse, but it's just different. And I think from, uh, I don't know, like I've done some, even just remote conferences, I think it's really a focus kind of thing. You know, there's just like that. I think something in our hind brain is like, oh, there's another human in the room. So I have to like, it's like a different way of paying attention. I think. Yeah.

**Colin Oflynn:** Yeah. I mean, did you do many remote conferences? I,

**Chris Gammell:** I did a couple,

**Colin Oflynn:** I did like a few and kind of stopped. I was like,

**Chris Gammell:** yeah, it got, I, my whole screen time went down. I stopped doing like meetup, you know, I throw meetups and I, I just, I just scheduled one for in person, the first one in person in 16 months. And I was like, yeah, I just gave up last year. I just, I couldn't do it anymore. I couldn't, I couldn't work all day in front of a screen and then do a meetup in front of a screen too. And it was just like, I, as much as I wanted to see people, it just wasn't that, it wasn't good. So. Yeah.

**Colin Oflynn:** Yeah. I feel that. That was kind of my, my results too. It's like, yeah.

**Chris Gammell:** Yeah. I mean, if, if this goes out on time, it probably will not, it'll go out. This will go out Sunday night. If people hear this and you're in Chicago, you have about 10 hours to get to a meetup in Chicago. It's on the Monday after. So. I,

**Colin Oflynn:** we'll get a few more people.

**Chris Gammell:** Yeah, maybe, maybe not. It's okay. I'm going to do more in Durham, you know, assuming the world doesn't blow up again. So, okay. So you've, you've been playing around with the, you won, sorry, the air tags. And you, so since you've been on the show last, we talked about the chip whisperer, you made the chip shouter. So what is that thing? Cause I remember the first time you told me about it, you're like, don't touch this. Yeah.

**Colin Oflynn:** I forget what variant that was, right? It was like, it's gone through many revisions. Yeah. Yeah. So chip shouter. So this is like all the fault injection. So fault injection is pretty cool in general. So like what Thomas was doing with the air tags, he was using fault injection to, to bypass the like, you know, fuse configuration or security configuration. Okay. Right. So in general fault, Jackson's pretty interesting from security, the normal issue, or one of the issues is like, if you have to modify the board, it's potentially less, you know, it could be trickier to do in real life. So chip share uses that demo.

**Chris Gammell:** Doesn't get as many like oohs and ahs.

**Colin Oflynn:** You're saying it doesn't feel like magic. The other thing too, is sometimes it's the, the threat is amplified. If it's like, you know, you don't have to modify it. So a while back, I had looked at like a treasure, uh, early version, early version of our firmware fix now wallet. Right. And it's like, one of the things is that if you could clone it without leaving a trace, right, that's a lot more powerful than attack. Then it's like, if you have to destroy it.

**Chris Gammell:** Right. Right. Right. Yeah. I, I, I, I hacked you and then it's just like in pieces. It's like, no, no, literally it's hacked apart. Sorry. Yeah. It's like,

**Colin Oflynn:** maybe you can, if you were just stealing, you know, Bitcoin or something, it's the threat obviously. But then it's like, what if you just want to clone it? And then later they put a bunch of Bitcoin on it. You steal it. Sure. Future point.

**Chris Gammell:** Yeah. Yeah. That's a good point. Hmm. Right. I mean, is there a lot of, so like, again, you know, I haven't had people on from the security industry in a while. I don't really know what the state of the security industry is. I mean, is there like a lot of focus on crypto because of the potential value there? Or where, where do you see focus, focus, focus?

**Colin Oflynn:** I mean, I don't, it probably hasn't changed that one that much since you had someone on before. Okay. To be honest. It doesn't feel like it's changed that much.

**Chris Gammell:** Then get out of here, man. No, I'm just kidding.

**Colin Oflynn:** You talk about, I don't know what else. Yeah. Yeah. I mean, there's definitely more interest. Like, I guess the question is, is it translating to real?

**Chris Gammell:** Right. Right. Yeah. Like, is there an actual threat or is it just like FUD that's being sold to companies? It's, it's interesting from my perspective. So one of my friends actually contacted me about like, he's like, Hey, you know, you'd ask me if I know anyone in security industry about like how to do audits and stuff like that. And it feels like this kind of nebulous thing of like, I know it's important. My people, I know, know it's important. And yet then what? Right. And so it's like, then I guess I could call someone, but it's not like there's, I mean, maybe there's standards out there too. Like, what should people be thinking of when they're, when, you know, people listening to this are designing embedded products or just stuff that might have some value to a malicious actor. What should they be thinking about?

**Colin Oflynn:** What is, what is the checklist? Yeah. So there's, you know, there, there's people that have been trying to build that. And that's something to be honest, that I was surprised, you know, when I first started, I was like, Oh, within a year, you know, some big company is going to come out and make this checklist like UL, you know, yeah, exactly. It's like, it doesn't have to be that good to be honest. It just has to exist. And like, they're going to sell tons. Like, you know,

**Chris Gammell:** yeah. Put the stamp on it and you just walk away. Then you're like, I'm good. Cause I've got the, you know, the, the, the CO stamp. Yeah. Why UL? Let's go Colin O'Flynn CEO. Yeah.

**Colin Oflynn:** Well, so I, I should, I probably should have, right? Because originally I was like, Oh, it's, it's so going to happen. I'm not even going to bother. Think about it. Right. I'm going to like put effort into doing this. Yeah. Cause it's immediately going to get, it's already happening. I'm sure. Yeah. I mean, people have been starting. So there's like arm has platform security architecture, their PSA thing, which is actually pretty good. The first levels, like it's a self checklist, right? So it's not like a big fee to doing this. And I have to pull it up here. And like at the lower levels, it's like pretty simple stuff. It's like, did you turn on debugging? Like interface, right? Stuff like that.

**Colin Oflynn:** sure. Sure. So, and it's more about having that checklist to be like, okay, you should check it and you should check it on the final one because there's like, you know, I've looked at devices. I think one of the nest, either the smoke alarm or one of their smart locks, I looked at it and it didn't have debug lock enabled, you know, not, it was just weird. It's weird that a huge company, right? Wouldn't have done that. And when I talked to them, it was like, Oh, it's supposed to be, but that was pushed to our contract manufacturer. Like that was the final production step.

**Chris Gammell:** That is an interesting disconnect. Yeah.

**Colin Oflynn:** Yeah. There was no, let's see, wait, so you can download it somewhere. I'm just kind of scroll.

**Chris Gammell:** There's like a spec. You can actually, you can actually like a P a PDF or something.

**Colin Oflynn:** There's like a PDF at some level. It's like, I think at the higher level, like level three, which involves side channel and fault injection, you do, you have to talk to a test lab. So then it's, you know, money.

**Chris Gammell:** Sure. But I think that's, I think that's the thing. Like when I, when I think about approaching one of my clients and being like, you seem worried about security. You seem worried about, you know, the, the potential that something's going to get out on here. Let's go through this process. Usually there is a, you know, there's an implicit cost to it anyways. Right. There's a, and there's definitely a cost. There's some unknown costs to having a vulnerability, right. Having a recall, having a, whatever's going to happen as a result of this. So. Exactly. Right. So, so if you go through this, it's like, Oh, it is. And it's like, it's a, it's like a fill in the blank kind of thing almost.

**Colin Oflynn:** Yeah. Right. So they're going to say, here you go assessment. And like a lot of this is just good. Right. So it's like scope evaluation name. Right.

**Chris Gammell:** And for people listening, Colin actually has this on screen. We are actually. Oh yeah, right. This is a podcast. Post the video. Well, why not both? Yeah, no. Yeah. So, yeah. So this actually does, we'll link this in, but you want to see what we're doing. And if you want to see future videos, what we're doing, this is the second video we've done because it's gotten a little easier for us to do video here on the amp hour. So why not?

**Colin Oflynn:** There you go. Yeah. Anyway, so it's pretty good. I mean, that's a good reference, right? Oh, I should plug, you know what? I'm terrible at marketing, right? Yeah. So Jasper from riskier and I, we have a book coming out with no search press. Yes. Okay. What's it? What's the title? A hardware hacking handbook. Oh, that's a great title. Yeah. There you go. So there's an updated cover. That's going to be pretty cool. And it's going to be 500 pages ish instead of 300. Okay. So I think they might have to update the price,

**Chris Gammell:** but what's in there. So it's like a, how to become a hardware hacker kind of thing.

**Colin Oflynn:** Yeah. So it's more, I mean, you know, this, this talks a little bit more that the backstory to this is it started as like a bunch of other people were involved and it was just getting slow because everyone was busy. Right. Right.

**Chris Gammell:** Yeah. The more people involved, the more, you know, the more meetings you have to have.

**Colin Oflynn:** And yeah, exactly. And it's like, and, and like a lot of us are like, you know, Joe Fitz was involved and like, he was really busy. So he actually contributed one of the chapters. He just gave it to us in the end. It was okay. Here you go. Make this happen. Got it. Right. So it was supposed to be like a big, more encompassing book. I mean, Jasper and I really started with side channel and fault injection portion of it. And we kind of filled in the rest, but yeah, it's probably of interest. If you're curious about hardware hacking, it really does slant more towards those, you know, higher end attacks, let's say. Sure. Rather than talking about like, Oh, how you should, I mean, we don't discuss how you should do secure boot at all. Like that's not right. How to do it properly. It's more like, here's how it can be broken.

**Chris Gammell:** I think that's great though. That's, that's like getting, even just getting kind of situated and like understanding what the expectations are. Right. It's like, or even, you know, how, how deep someone needs to go. It's like, Oh, well I can learn this when I, when I encounter it or when I get to that part of the project versus I should be training for two and a half years to even get to the starting line. You know, like that's, that's a pretty important distinction, I think.

**Colin Oflynn:** And that's actually a good point too. Right. When you say like, what should people do with security and it's this like balancing problem. Right. So I think like sometimes security, people, myself included can be a little terrible because it's like, Oh, here's this. I wasn't going to say anything. Okay. You know, you're so nice. Right. It's like, yeah. Well, there's some like comic about that. Right. And it's like, Oh, here's this product. And it's like, you spent like 10 years carefully building it and like security guy comes along. He's like, Oh, that's that spot right there. That's never going to work. Oh boy.

**Chris Gammell:** Yeah. Yeah. Right. Yeah. You better, you better start from scratch. And it's like, where have you been hiding? Yeah. Right. So, so,

**Colin Oflynn:** I mean, I think, I think it's also realizing, you know, this is where that like arm PSA thing I kind of like, because it's, you know, realize you don't have to be perfect. You don't have to, like, you probably don't care. You may not care about some of these advanced attacks. That's fine. That's a totally valid answer. Right. That's probably a smart answer in many ways.

**Chris Gammell:** Yeah. Yeah. I mean, before meeting you and other people in the security industry too, it's like, you know, the idea of like attack surfaces and like all these other things. And I was like, Oh yeah, people will probably care. There's probably some value. There's monetary value. At the end of the day, it comes down to monetary value. Right. And then you kind of back calculate like, Oh, okay. Well, there's some kind of secret sauce in there that isn't necessarily just the IP. It might also be the keys to the web kingdom that then, can be used for X, Y, or Z to in order to extract money because there's value there, you know, like all the way back. And like, I didn't have any of that mindset at all. And yet people that were in the security industry are like, well, yeah, you could, you know, if you have encryption keys, you can do all X, Y, and Z and you can, you know, cause this havoc. And it has happened before because we've been in the industry and I'm like, all right, well, I don't know. Like, what does that matter? You know, I, people should need to buy my products first in order for them to actually extract any kind of value. I need to get value before they get value. Yeah.

**Colin Oflynn:** No, for real. Well, it's funny too. Another like, you know, risk factor here was I had done a project with some smart locks a few years ago and I just was a black guy to talk about it. So when I talked to the company that we're building the locks, which I don't know how to pronounce the name. And so I almost like try to skip over it. It's Schlage, S C H L E G E.

**Chris Gammell:** Oh yeah. Yeah. Yeah. That's like a standard. They've been making locks much longer than smart locks, right? Oh yeah.

**Chris Gammell:** That's the thing. I say Schlage, I think.

**Colin Oflynn:** Schlage. Okay. I never know if they correct pronunciation and I meant to look it up, but anyway,

**Chris Gammell:** it's whatever you say it is, man.

**Colin Oflynn:** Yeah. So, so, you know, they have like huge list history of locks and this was a consumer lock. So it's not, you know, there's a price point if it's put on a door, that's probably okay at best. Right. With like,

**Chris Gammell:** it's not super secure. Like it doesn't matter how good the lock is when someone can just punch through the door. Yeah.

**Colin Oflynn:** Right. So it's like, it shouldn't be terrible. And that's kind of like, and it was definitely that. Like, so they had a flaw that you could remove the front keypad and brute force it through. So it was a cool, like it was an interesting engineering sort of attack, right? Engineering perspective. Practically it's irrelevant. You know, zero people are going to do this instead of smashing it or breaking a window,

**Chris Gammell:** going around the door. Yeah. Maybe using, I don't know. If my, if my old house has any, has any indication, getting the ladder out of the garage, climbing up on the roof and just opening the window that was already open because I got locked out. Okay. Was that a you thing or a, that was me. Uh, yeah. I took the air conditioner out of the window too. So if anyone wants to break in my house five years ago, now you know how,

**Colin Oflynn:** now you know, it's solved now, but yeah. Right. So, I mean, that was the thing. So it's like for them, the threat bit. So what they said though, is they, they were actually pretty happy. I talked to them because they said, you know, the threat for us wasn't necessarily monetary or anything like that, but it's what if someone does this and then goes on black hat and doesn't tell us and they make a presentation that's like, you're going to get murdered if you use this law. Cause you do see people that, you know,

**Chris Gammell:** and then the headline is that only, right? Yeah. Yeah. Exactly. So that was murdered.

**Colin Oflynn:** You know, the, the, the, the threat to them was, they knew it wasn't terrible. It was a threat to the consumer, but you know, to the marketing side. So sure.

**Chris Gammell:** Sure. Yeah. And I think that that could be true of a lot of things, right? Yeah. I mean, there are different levels of monetary, I mean, I guess even reputation based could have a monetary aspect to it, but yeah.

**Colin Oflynn:** I mean, if you're looking at like a bunch of smart locks in home Depot, right. And you're like, Oh, I saw a bad, you know, CNN headline about this one. Yeah. And they're all kind of the same. Like they're, they're pretty similar, all these things, right. Right. Like I don't think it takes that much to, to nudge people one way or the other. So, and it's, it's funny for them at where he, for, or for him, the, the guy I talked to worked out really well. Cause he's like, yeah, they were just setting up, you know, the IOT security stuff and figuring out budget. So he's like, this is perfect. Cause this is like a great, like, Oh, I need more budget. Right.

**Chris Gammell:** Yeah. Yeah.

**Colin Oflynn:** Yeah. Yeah.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah.

**Colin Oflynn:** So he was like pretty happy in the end, I think was the summary of the whole thing.

**Chris Gammell:** You got me nervous now that I just bought a house and you know, it's got smart locks on it and I'm like, I'm going to take those off,

**Colin Oflynn:** but it looks so cool.

**Chris Gammell:** You know, having a code is really nice. You know, I lose my keys all the time. So.

**Colin Oflynn:** Oh yeah. Oh, well that's the thing, right? I mean, let's, if it saves, it still could be more secure because you don't have to have a key with you somewhere that you don't. Oh true. Yeah. That you might lose.

**Chris Gammell:** Right. Sure. Sure. Sure.

**Colin Oflynn:** I don't know if you're going out, if you remember that being the thing that you could do,

**Chris Gammell:** then going, Oh, like going to a place. Yeah. Somewhere. Not in the house. Yeah. Right. I would say the, the big one is like not having to carry a key to go for like a walk or a run. That's a nice one. Yeah. Yeah. Or I could just move to Canada where, you know, you guys don't lock your doors anyways.

**Colin Oflynn:** So there you go.

**Chris Gammell:** Yeah. Just go where all the people are very nice and safe. Hopefully. Yeah. Yeah.

**Colin Oflynn:** Well, that's like the, uh, ever so often there's like a post on like neighborhood Facebook. It's like, a car got broken into last night. Right. Which actually means owner lost their key. They, someone just went through the car. Like it wasn't locked. It was never locked. Right.

**Chris Gammell:** Broken into is crossing the threshold of the, of the door. Yeah.

**Colin Oflynn:** Basically for real. It's like someone was there. It wasn't invited.

**Chris Gammell:** So. Okay.

**Colin Oflynn:** All right.

**Chris Gammell:** Oh man. All right. So back to the security industry too. So we talked a little bit about crypto. We've talked about smart locks, you know, more things are getting smart or sorry, more, uh, quote fingers there for the listeners. Uh, so, uh, yeah. And, uh, you know, I talked to Dave and he's very anti IOT. I'm very pro IOT, but where else are you seeing potential risks? I mean, like as more things kind of come online, as more things get connected, is it at, is it always at the hardware layer? Is it at, you know, like communication layers? Where are the potential vulnerabilities that you kind of, I guess most of the time you'd be kind of, we're looking at the hardware layer, right? But yeah,

**Colin Oflynn:** I mean, that's the thing, right? I really focus on that. It's like, of course I'm going to say there.

**Chris Gammell:** Yeah.

**Colin Oflynn:** Yeah. It's sort of interesting. So another thing I looked at a little bit recently is I got my hands on a Starlink dish. Oh, cool. To tear that apart. So, and that, that one's sort of interesting. I mean, originally it was like, yeah, what's the risk there? But it's like, if there's some backlink, right, that could actually be pretty serious. Like if you could get into the satellite network, right? If there's some like security model there where it's like, if you have access to an end terminal, which I'm going to assume they, you know, don't have that level of access, but that's the type of thing where, you know, if you think back to sort of the origins of network hacking, computer hacking, right? It was a lot of stuff like that. Tap in that kind of idea. Yeah. Right. So it's like, it's like, who knows, who knows what you could do, right? It's all pretty new, all this stuff. So, yeah, I mean, there's definitely a lot, like, I'm kind of curious if you're going to start seeing BitLocker for embedded device, right? So it's like, are people going to lock out or not BitLocker, right? Are people going to like ransomware? Ah,

**Chris Gammell:** interesting. Okay. Yeah. And for like large deployments too, I could imagine that would be, I mean, I guess it depends how valuable that thing is, right? If it's like a hundred dollar smart speaker. All right. Well, it's getting along in the tooth anyways.

**Colin Oflynn:** Yeah. And I meant to say crypto locker. That's what I was thinking of. Got it. Got it. Like look up. I was like, what was I thinking? But yeah, it's, uh, I mean, this goes back to, could they start a company is kind of the question I've always had. Okay. It's like, if you say, Hey, I'm going to lock out all of your users of your Sonos speakers, or you pay us a million dollars. Like,

**Chris Gammell:** they're like, well, we do that anyways, man. This is, this is, we don't want to support it anymore. So if you could just be a hacker and, uh, you know, if you could come in with a hoodie and tell, we can tell our users that they've been locked out. So, yeah.

**Colin Oflynn:** Right. That's, so it's like a weird thing. Right. But then, I mean, it's pretty cool on the flip side. It's like getting stuff. Recovered that have been made end of life because with all the IOT stuff, right. If the server, you see these, like whatever that juicer was that the server went offline. It's like, yeah, no, I can't use your juicer or whatever.

**Chris Gammell:** Yeah. Right. Hmm. So one thing I realized we didn't talk. So we started talking about the ship shouter, but we didn't actually say what it is. So what is it?

**Colin Oflynn:** I like a sidetrack here.

**Chris Gammell:** Yeah.

**Colin Oflynn:** So electromagnetic fault injection. So basically what it does, it has an inductor at the end of it. You dump a really powerful, um, pulse. So really what you need is a big current change to generate a strong magnetic field.

**Chris Gammell:** That magnetic field or V equals LDI DT, right?

**Colin Oflynn:** Yeah. Right. So there's, there's your university. It has a use.

**Chris Gammell:** I got that from Keithley, man. I, that was just the, on the job.

**Colin Oflynn:** Yeah. Yeah. So it induces a voltage basically in your, your chip or your device that you put it over. So when you induce that voltage, that's going to, you know, it could flip it to memory. It could mean like the, the bits at a note or the voltage at a node, which may be as like a bus line has changed such that it reads the wrong value or anything like that. So,

**Chris Gammell:** ah, okay. So it's kind of like nudging, nudging the program counter into a, into the next thing over or something like that kind of idea.

**Colin Oflynn:** Yeah. Yeah. I mean, it can be a whole bunch of stuff, right? So like a pretty common one, a sort of pattern, you see a lot of bootloaders and, and other devices do is like, you know, something's going wrong. Like it's going to fail a password check. It just goes to an infinite loop. And so it's like, you know, and it's just a while one loop, right? Or they just call exit, which actually just ends up being a while one loop. Right. But it's like, if you skip over that loop, if you can get out of the loop, then it's actually the rest of the code is, is sitting right there. Right. So it's like, cause the programmers, the, the compiler seems like, okay, it's all compressing it down. And right. Yeah. Right. So then it's like, if you jump out of the loop, it actually just keeps running everything that it wasn't supposed to run. So.

**Chris Gammell:** I never really understood that about like doing firmware dumps. So like the idea of like, you know, not sure if it was like the chip shouters, things like that before, where you just do something to a device and then it just automatically dumps its firmware. I don't, how does, how does that work?

**Colin Oflynn:** Yeah. I mean, well, it depends on the devices, but a lot of those it's like, so there is a really good example. Mika Scott did one with like a USB device and it needed a bit of triggering, but it's like, if you do a device that's sending back data, right? Say it sends back a data buffer and inside the firmware somewhere, it's going to have like a USB read, you know, or USB send or whatever the command is. And it'll be like, send this data buffer and this much of the data buffer back. So it's like, if you corrupt how much to send, it can actually cause it to just continue to read memory. And if the address map is such that the firmware is there, it's also going to read the firmware out of it and stuff like that. Got it. Hmm.

**Chris Gammell:** That's cool. Yeah. Okay. All right.

**Colin Oflynn:** And actually that's a pretty good example of one where like to loop back to what should people do and really basic stuff. It's like, if you have sensitive data or even your firmware, right? If you put a invalid memory segments, right? Throughout your memory map, you'll kind of block that because the issue comes out when it's like, there's a data buffer in Ram, you can read that data buffer because it's supposed to be read. And then you can just continue to read, you know, forever. But if you can, you can just put invalid memory segments, like a lot of the memory managers, like even cortex M zero, I think a bunch of them support, maybe not M zero, but like M four for sure. Yeah. Yeah. Sure. Right. So like, which nowadays a lot of people use, you can put like invalid memory segments that are kind of like landmine. So if it hits that, it's going to go to an exception. Yeah. Right.

**Chris Gammell:** Right. Oh, that's cool. Okay. That's it. Yeah. I'll have to check out that list. I've never seen anything like that, but it's, it's important to, okay. So when you're using the chip shutter then, so it's basically dumping EMF into a device and just kind of hoping it does the right thing or the wrong thing, I guess.

**Colin Oflynn:** Yeah. Well, so the timing, right. So normally there's like all this timing stuff. That's the thing with glitching. Like sometimes it's pretty easy. So it can be started, leanly easy. How this stuff works. It's like, you know, on boot. So a common one is right. When the device is booting up, you hit it with something. So it's like reading from memory, a configuration or fuse. And then based on that fuse, maybe it turns on or off a J tag lock. So if like at the right time you skip over, turning on the J tag lock, it just comes up on lock. So, so several of the like, you know, more interesting or, or I'd say more use glitches or stuff like that, where it's like, they're just trying to dump memory. So they get the device to come up and disable, not, not show it's J tags lock status or some lock status thing.

**Chris Gammell:** Okay. Yeah. That makes sense then too. Cause you, so from a, from having J tag access, you can just go and peek and poke at memory and just pull it all out then.

**Colin Oflynn:** Yeah, exactly. Right. Then it's pretty straightforward. Most of the time. So,

**Chris Gammell:** okay. Do you get feedback from your users? Like chip, shouter chip, whisperer. Do you get to hear about this sort of stuff or does it go kind of dark after you sell it?

**Colin Oflynn:** Yeah, a little bit. So like, I mean, also when, have you ever emailed, you know, HP to be like, thanks for the scope. This is what I did with it.

**Chris Gammell:** Well,

**Colin Oflynn:** but they're not as friendly as Colin O'Flynn is, you know? Okay. So, so I mean, I think a lot of people don't do it just cause they end up. But really, Hillary is more,

**Chris Gammell:** more friendly too. I mean, like if you can get, get ahold of Hillary during, you know, during the customer support process, it's going to be a lot, a lot nicer.

**Colin Oflynn:** Life will be easier. Yeah. That's right. I mean, that was the kind of cool thing, right? That I, I was happy I did with chip whisper is like, because it was kind of targeting academics, you also see the results in papers. So like, we do see quite a bit of output in that. So I always like to see, you know, like what people are doing with it. And even if I go like since 2021 on Google scholar, you know, you can see, Hey, here's like 58 papers that people have used. And, and some of them, you know, sometimes it's just a reference to it, but you'll see people doing like a lot of deep learning stuff. It's pretty cool. Cause people will implement entirely new stuff on FPGAs. And, and use chip whisper to test some of that.

**Chris Gammell:** That's something I wouldn't have thought of, but that actually makes a lot of sense. Cause if you're trying to basically, I mean, even the, the simple demo that I had tried out and got working, it was basically pattern matching. But now if you start to put higher levels of compute against it, I guessing you could probably draw out even, even crazier amounts of even more stuff in the noise, basically.

**Colin Oflynn:** Yeah, exactly. Right. So, yeah. So it's, I mean, that's the cool thing that I, I kind of like that feedback, right. It's like pretty interesting to see people and we'll like, we'll see blog posts. That's pretty cool. And like,

**Chris Gammell:** yeah,

**Colin Oflynn:** no people will use it and other courses, which is pretty neat to see. So it's like the, you know, the plus side of the sort of open, more open source, open side of things as you do see that feedback, right. That I think if you're just selling to finished product only to whatever people, like commercial companies, things that you're never going to hear through a distribution channel. Right.

**Chris Gammell:** You're just like, all right, well, someone probably bought 50 units because I just have to restock 50 units. Yeah. Right.

**Colin Oflynn:** So it's like where, who knows?

**Chris Gammell:** Yeah. Well, on, on the topic of restocking 50 units, how, one, one way that you and I interact pretty regularly is on a, on the consulting forum and hearing about sourcing woes. But I think you started that thread about, about sourcing woes, but how, how has it been sourcing for things that have FPGAs and. Great. You know, life is the best. Love it. Awesome. All right. Great. Done.

**Colin Oflynn:** Yeah. I mean, it's been weird. It's we've avoided some issues. We've definitely got hit with some stuff. I don't think we've had to stop any production yet for it. I don't know if that'll happen. Um, I think the bigger hit is on like, you know, like there's stuff that we're going to do with R and D that I didn't bother. Cause it's like, I don't have time to do the R and D and then do a prototype. And like, I just need to buy stuff now. Yeah. That's the killer. So I think like, I don't know. I worry about a lot of small companies too, if we're going to see more issues. Cause like, you know, there's a lot of people like me that have a small company with a few products that are pretty margin sensitive, I think. Right. And it's like, you sell some products, you use that money to fund a new run and buy some more product, blah, blah, blah. But it's like, now it's like, Oh crap, we might need to buy a year's worth of chips for something we might be doing. So actually I'm doing that now because we have a new capture board, chip whisperer Husky coming out that I'm setting up a crowd supply for. But like, you know, it's like, I'm going to buy a hundred or 200, at least quantity parts for some of the stuff that I'm pretty sure we're going to end up using in the final production, but that production won't happen. Right. For maybe a while. Right. Like,

**Chris Gammell:** right. You're just, you're just pre buying for safety basically.

**Colin Oflynn:** Yeah, exactly. So, so it's like really the, it screws up all the cashflow stuff. Cause it's like, okay, now.

**Chris Gammell:** Right. Small business cashflow. Yeah.

**Colin Oflynn:** Yeah. So, so I don't know. So it's a weird, yeah, it's a weird time for a lot of us. Like, I don't know. We'll see, see what happens, I guess.

**Chris Gammell:** Okay. Well, I mean, yeah, you mentioned like supporting older stuff too. So, I mean, that's been okay as well, like in terms of sourcing old stuff, I guess the other thing that I wanted to bring up is that you, you are a pretty big proponent of your desktop pick and place. Cause I'm curious about how that's been going. I mean, is that still a tool in your arsenal or use the less these days? Cause of time.

**Colin Oflynn:** Yeah. We, I mean, so we've used it less as we've, our volumes gone up a bit. So in some ways, and that was always the thing that was like, it was really good. It helps, especially when we were smaller with cashflow, because you could do stuff like buy, you know, parts that were going to be an issue to store them. And then parts that weren't going to be an issue, right. Or were more expensive. We could run later. Some of that's gone down though. Cause I mean, like jail PCB or JLC PCB, right. Doing their like super cheap. I don't know if you've used that at all, that they're like, no, not yet. Yeah. Okay. Yeah. So they do it. It's, it's absurdly cheap would be how I described it. I don't know if it's changed, changed recently.

**Chris Gammell:** Yeah. I thought some of it might've been promo at the beginning, but, uh,

**Colin Oflynn:** I think like they just optimized pretty heavily. So like you order this SMT assembly. It's like, I don't know. It's, it's, it seems like free. I think there's some.

**Chris Gammell:** Colin is not sponsored by JLC. Nor is this podcast. I guess I should say that. I mean, we're just cheapskates, right? I mean, that's what hardware people are. I think it's just part of, it's part of the ESA ethos for some reason. Yeah. Which is true. I mean, optimizing it's about optimizing cost. I think.

**Colin Oflynn:** Yeah. The, the whole question of, so I forget, but I had scoped it. Like I was doing this chip shover and like, I think getting them to assemble it, getting the board, them to assemble, they don't assemble at all. It's just whatever parts they stock, which is not everything. But it's like, if you're going to end up hand assembling it anyway, wouldn't you rather not hand assemble all the capacity?

**Chris Gammell:** And then it's like a rework for the, for the stuff that you don't can't buy from them basically. Right?

**Colin Oflynn:** Yeah, exactly. So. Yeah, I think it was like cheaper for them to do it than buying the parts from Digi-key. Cause I mean, I think it was like, I think it was like, yeah.

**Chris Gammell:** Yeah. I mean, you look at the most bombs are what? 50% jelly bean, you know, 10 Ks 0.1, like whatever, whatever you have. I think about, I feel like most of my boards are like 20% zero ohm resistors. Cause I'm so neurotic about connections these days, you know? So, yeah.

**Colin Oflynn:** Yeah.

**Chris Gammell:** But yeah, that's great. That works out. And like you said, your volumes are going up. So it seems like even just from a time perspective, it would be tough to go in. And manage the, you know, just the workflow of, of doing that sort of thing. And even if you're hiring interns, like we talked about earlier, do you think you gotta retrain them and just getting people to run that stuff is sometimes it's nicer to just push that out outside the, uh, the organization.

**Colin Oflynn:** Yeah. Yeah. We definitely, I mean, we've tried to outsource more, so we were lucky at least one of like the first people that sort of has been working with us and worked with us a bit part-time initially, that's been full-time for a few years, our like production manager, production, everything in person. Right. So she came from like pretty varied background and like bit of design, bit of production. And varied is great for small companies. Right. But then like, she's also taking some of this to, to being able to run like the pick and place. If it's like, uh, you know, so we did a chip share to run six months ago, I want to say where I was going to outsource it, but then it was like supply chain issues. And it was like, uh, I can get some of the parts now. So I'm going to order them. And then like, we're going to do the run. I think we ended up just doing part of the run and then we're going to get more parts to rework. And we could outsource that, but at some point it was like less, it was, it was easier to do it yourself. I mean, I'm terrible for being like, ah, this is a hassle to tell someone, right. Had to do it. Right. I'm just going to do it myself. That's like also a very engineering. Right. Right. Right.

**Chris Gammell:** Right. Right. Right.

**Colin Oflynn:** It's like you end up doing a hundred things because you don't want to outsource it. Yeah.

**Chris Gammell:** Yep.

**Colin Oflynn:** Cause in your mind, it's going to be easier.

**Chris Gammell:** Right. I get to choose whatever 16 hours I work. I think that's what I always think of.

**Colin Oflynn:** Exactly. Somehow it's better. It feels like you chose to do it.

**Chris Gammell:** Yeah. Well, what else is, uh, I mean, exciting coming up for you. It's, it, it seems like the, uh, the conference schedule is always a fun time, but it's not, uh, not really a thing still. So what else is kind of exciting in the world of security and the world of new AE in the near term?

**Colin Oflynn:** Yeah, I think we're just going to be doing feature. Refresh. So this chip whisperer husk, I mean, we basically moved to like a seven series FPGA, some, some newer stuff. The one, I guess the one big update is so with the original chip whisperer, it's like I did the FPGA stuff, right? So it's fine. Right. Technically it is FPGA stuff. The guy that's doing the new ones that we, we had, uh, hired, joined us a while back. JP, he worked with synopsis before. So, I mean, like he's like actually doing it.

**Chris Gammell:** Yeah. It's, it's a real FPGA. Now you're saying, yeah.

**Colin Oflynn:** Yeah. So, I mean, he has like, like the whole thing is simulated,

**Chris Gammell:** right?

**Colin Oflynn:** Which I never, I'm supposed to think people do.

**Chris Gammell:** Yeah. Yeah. Of course they don't just try it and see if it works and try to see if it works. Yeah. That's what I did. They do it. They do it at digital, right? I mean like this.

**Colin Oflynn:** So it like optimize. My, so, so the, the, the code itself is a lot more sane, but that he's also with a larger device, it's adding. There's a lot of stuff where it's like, Oh, that's super cool. And it was always just too flaky to do. So having like a logic analyzer built in so you can see what's going on. Like if you're doing clock glitching, right? Being able to see like, Oh, this is what my clock looks like. Right. Pretty simple. But before the solution, which worked was like just attach your oscilloscope. Cause to be honest, that's easier than Colin figuring out.

**Chris Gammell:** Right. And you have one and other people maybe don't. So it's like, all right now it's more self-contained and yeah.

**Colin Oflynn:** So that would be pretty cool. So I think we're going to spin that into like another higher end. Cause like we kind of, you know, on the question of small company and all that stuff, we've kind of tried to keep like a cheap and expensive product going at the same time. So it's like, yep.

**Chris Gammell:** Yeah. Yeah. Cause you guys made the nano at one point, right? You made like a chip whisper nano or something. Yeah.

**Colin Oflynn:** So that one still exists. We can still get parts for that. So it's like a $50 one.

**Chris Gammell:** Yeah. I just think if people that are listening that maybe want to get started with it, that might be a good, a good place to get started and try it out for pretty low investment.

**Colin Oflynn:** Yeah, exactly. Right. And that was kind of the idea. And like, eventually I'd kind of hope to do like a conference badge with it or something at some point, but sort of like, you know, supporting all of that. So, so I think we're going to do a high rend version of this, but again, using the like new architecture, right? So it's like new, new FPGA uses Vovato. So the old one used ISE, which like, I think you can run on windows 10. I don't even know if he can.

**Chris Gammell:** Yeah. Yeah. Any thoughts on the, the open tool chain stuff or is it just not, not what you need?

**Colin Oflynn:** Uh, no, it's, we haven't, I'm, I mean, I'll use Altium, right? So this is like the anti open source.

**Chris Gammell:** No corporate, I believe is the subreddit for that.

**Colin Oflynn:** Yeah. Yeah. Right. Exactly. So no, actually I'm doing, um, the, the zero to ASIC course right now for fun. Oh, you are.

**Chris Gammell:** That's cool. Yeah. It's Matt Van, Matt Venn's course. If people don't. Yeah. And it's really cool.

**Colin Oflynn:** Basically, I was curious. I mean, the ASIC side opens up a lot of stuff. I mean, the speed is insane, right? That's the real crazy thing is how quickly you can reconfigure stuff. Right. So like you can go from high level language to reconfigured and, you know, under a second, I'm pretty sure with, with some of the stuff that I've seen. Claire, Claire Wolf was posting on Twitter about that, or who is, I just saw something recently about that.

**Chris Gammell:** Yeah, we have to, I mean, we, we pretty regularly have people on. We just had Michael back on from micro and they're doing a bunch of stuff in there. But, uh, yeah, I think it's, we keep, we keep, uh, pushing that around here and I still, I should really take that course too. But it's always interesting. Like the application side of things, like I, I don't do many FPGA things. I mean, like, I feel like the stuff you're doing with like signal analysis, things like that, it's really fits very well, but, uh, certain products that I'm working on, like if I'm just adding IOT to stuff, it's not really necessary. FPGAs are probably not the right answer, but, uh,

**Colin Oflynn:** I mean, with part shortages, maybe it'll be like, yeah, right, right.

**Chris Gammell:** Ultimate flexibility until you can't buy the FPGA.

**Colin Oflynn:** Well, yeah. Well, that was, I mean, going back to part shortage. So we had a kind of fun, I think this is why I started the thread was I was doing a project. So some of the, this new board stuff where we're trying to support some people that are actually going to be using some of these. And so it was like, they re they needed it. It was like, you have to deliver this and we'll pre, we buy some of this stuff for you to help you out. But it's like, we need these FPGAs when we do the run or otherwise this whole thing is pointless. Right. And like the only, so anyone who's buys FPGAs, you, you wouldn't buy them off design. Like when you look at Xilinx pricing on DigiKey, it's like the one FPGA costs more than the digital board. Right. How does that make sense? It's like, well, the FPGA pricing is crazy on, on DigiKey. Like you always go through their sales guys, but we couldn't do that because they don't have stock. So it's like, you just have to buy them from DigiKey. And it's like, yeah,

**Chris Gammell:** it's like a luxury car worth of FPGAs. Literally. Yeah. Right. In this box. I do remember you posting about that. Yeah. And it's like, yeah, that's, that's stressful. I mean, like just like cash swings like that. It's just, that's a lot of dough, you know?

**Colin Oflynn:** Yeah. One of the biggest FedEx, right. It's not like some special thing. It's just like, there's, you get a tracking number and like, you know, for a day it's stuck. I think there was a snowstorm at the time. It was like in the winter. Right. So it's like disappears for two days. Oh my gosh. And you're like, Oh, hopefully, hopefully that's fine. Cool. I'll, I'll breathe. I'll breathe again in two days. Yeah. Right. It was like once it was here, I think until I shipped the boards out, then it was like, okay, now I feel better. Cause also it's like, what if it gets lost? And right. I'm, they've got insurance. So yeah, but then I can't get like the money's useless. Basically. That's right. Yeah.

**Chris Gammell:** The parts are actually what's matters.

**Colin Oflynn:** Yeah. So it's like, that's what I need. Yeah. Oh man. Oh man.

**Chris Gammell:** All right. Well, Colin, this has been a wild ride back into the security field. So I appreciate you coming on, especially last minute. People don't know. Colin was my shining, night and shining armor here. They would come and, come and talk to me about, about security stuff. So thanks. Thanks for joining me here today. And it's good catching up, man. It's, it's been too long. So yeah,

**Colin Oflynn:** it'll be good in person. I do have any in-person plans for conference or anything.

**Chris Gammell:** And I am supposed to go to the embedded Linux conference out in Seattle in September, October, September, end of September. Yeah. We'll see if that goes off. I don't know right now. It's not, not looking good in the States. So I don't, yeah.

**Colin Oflynn:** Yeah. Yeah. That's fine. It'll be good to see people again. I mean, I might do, there's some academic ones, in Europe in October, November, but I was thinking originally, yeah, maybe.

**Chris Gammell:** I'm not, I'm not super bullish on the state of the general populations.

**Colin Oflynn:** Yeah. The world basically too.

**Chris Gammell:** Yeah. Yeah. All right. Well, hopefully happier times are ahead and we'll get to hang out soon. Yeah. Thanks again for joining us.

**Colin Oflynn:** Good to see you again. Good to catch up. All right.

**Chris Gammell:** Thanks, Colin. Talk to you soon. We'll be right back.
