---
episode: 546
title: Thousands Of Dependencies
url: https://theamphour.com/546-thousands-of-dependencies/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released June 21st, 2021. Episode 546. Thousands of Dependencies.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. I hate computers. You start a lot like that, yeah. Yeah.

**Chris Gammell:** I've seen what's been going on with you, but yeah, it's a...

**Dave Jones:** I don't know if you watch my video.

**Chris Gammell:** Part 74, yeah.

**Dave Jones:** Yeah, yeah, yeah. I'm not sure if you watch my... I'm sure you didn't watch my video. It's like half an hour of me just failing at assembling a new computer. Yeah, it sucks, man. Because, yeah, like I did no research on this thing, but I had this case. It sort of like just all happened very rapidly. I scored this motherboard, like a micro ATX motherboard, and I had an AMD socket. So I thought, ooh, I'll buy the biggest, baddest AMD Ryzen processor that can fit in this motherboard because I just happened to have this new case and this, you know. So it all just, right. I checked the website. What processes do support? Oh, the Ryzen 5000 series. Fantastic. So I go and buy like the almost top of the range Ryzen 5,000... 5990... 5990, is it? X? Yeah. The 5900X processor. And yeah, it didn't work. Because why, you ask? I hear you ask.

**Chris Gammell:** Yes. Why?

**Dave Jones:** That is the million dollar question. Well, because the motherboard had old firmware on it, right? Because this new processor is so recent that the firmware has only just been updated to support it and it was an old stock motherboard, right? It was basically an old one for a year or something old or something. And even if it was three, four months old, three, four months old, it wouldn't have the latest firmware. And the problem is to upgrade the firmware, you need a processor in it. So it's like you need a supported processor. So you have to actually... This is such a problem. And of course, I didn't know any of this because I didn't research any of it. And I'm not like... Somebody tweeted that or commented that, oh yeah, everyone knows on the AMD subreddit that this is a thing. People have known for years. And it's like, oh yeah, I hang out on the AMD subreddit. Right, right. Like, anyway, so I learned the hard way after building this damn thing up.

**Chris Gammell:** The plans for the intergalactic highway have been in the planning office for millennia now, you know? Yeah.

**Dave Jones:** And it didn't help that... I also tweeted this out. I thought it was a memory problem because the motherboard's got, you know, error status leds and one of them is Mark DRAM, right? There's one Mark CPU, there's one Mark DRAM. And it was the DRAM one that was on. So I thought, oh, there's something wrong with the memory and the memory timing. It was Intel memory. So I'm trying to figure out, you know, like, is it the bloody, you know, it must be the DRAM, right? Because this motherboard supports the CPU. No, no. It turns out it's the CPU apparently. And everyone knows this. And it's so known in the industry, such an issue that AMD actually have this program where they loan out old CPUs. If you contact them, they will actually, yeah, they will ship you an old CPU so that you can put it in their socket so you can upgrade the firmware and then you ship it back to them. That's interesting. I had no idea, right? But apparently this is like, yeah, everyone in the AMD computer world knows this, right? It's, you know.

**Chris Gammell:** Yeah. I mean, I tried to switch out my computer as little as possible. It sounds like these people are trying the opposite. They're like, you know, like gamers and people trying to like optimize. Yeah. Everyone knows this stuff.

**Dave Jones:** Yeah. Right. So are you still running Intel or AMD?

**Chris Gammell:** Good question. I think it's an Intel. Doesn't know, doesn't care, folks.

**Dave Jones:** Yeah. I mean, yeah. Which is the, you know. Yeah.

**Chris Gammell:** It's abstracted by an OS. I'm cool. Yeah. Yeah. Yeah. It's right. And then it's abstracted again by a VM above that. So like, yeah, I'm cool. I just get mad when the fan cranks aren't too high. I'm like the, I sound like an old person, you know, at this point, like, oh, I just, just, I just want my AOL to work.

**Dave Jones:** Right. AOL. My BBS. I just want to dial into my BBS. That's right. Yeah.

**Chris Gammell:** I just, I just want to, I just want to get to my Psy.whatever. Fidonet.

**Dave Jones:** Yeah. Use Kermit.

**Chris Gammell:** That's right.

**Dave Jones:** Yeah. Oh, that's great. And, and that's not the end of the problems though. That's not the end of it. Then somebody remarked that, oh, be careful of the USB stuttering problem. If you, if you get a new motherboard or whatever. And I go, well, so I Google this and then down the rabbit hole, I go with the USB stuttering problem. Apparently there was some sort of bug in the, either the AMD processor or it was the 450 or the 550 chipset, the motherboard, the AMD motherboard chipset, right. That all these motherboards are built on. And it would apparently all of the built-in USBs on the motherboard, these motherboard, AMD motherboards would like spontaneously like reset every couple of minutes. So they would like actually disconnect and reconnect. So your keyboard wouldn't work for 10 seconds while it's like, and apparently like, would

**Chris Gammell:** it re give it a new ID number and stuff too?

**Dave Jones:** Well, it would reconnect and continue to work. And, and, and it wouldn't do the windows thing, you know, it, it wouldn't do that. It'd just freeze. Right. It'd just like stop working.

**Chris Gammell:** So would you start power on the peripheral?

**Dave Jones:** Like would you still have power on the peripheral, but it's a, no. So you won't see the lead go off. It's just a, like a comms thing. Yeah. Yeah. And, and everyone tried to, was trying to figure out why their keyboard and mouse would freeze up for five seconds every couple of minutes, you know? And apparently this was another huge known problem in the AMD industry and caused a lot of people to move away from AMD. Oh, I don't trust them anymore. These bloody Silicon bugs. No, apparently they could, yeah. You turn off this option and this option in your bias and it fixes it. New firmware is fixed it. Apparently. So. Yeah.

**Chris Gammell:** It's interesting to me, like the, the level of like how much I think about my computer as electronics. I know that sounds like a stupid, stupid statement, but like, to me, a laptop is really more like a screen and a keyboard. And like, of course there's electronics running it.

**Dave Jones:** You shouldn't have to think about it. It's a tool.

**Chris Gammell:** It's a tool. Below the hood that it's just like, yeah, I don't think about that stuff. But of course it's, it's very, very, very advanced electronics in there. Incredibly advanced. Way more bleeding edge than anything that I've ever worked on. Yeah, exactly. And so it's like, yeah, you just gotta, you know, and I expect to be like, oh yeah, I just scuffed my feet on the carpet. I'm going to go switch out my processor. Yep. Or the DRAM.

**Dave Jones:** So yeah, everyone in AMD land knows, oh yeah, disable this option in the bias, this one, this one, and this one, and use an external hub and do this. And you can bypass the USB stuttering problems. Like, oh, okay. Jesus. So I'm going to be a glutton for punishment. After this, I'm going out to buy a new motherboard. And yeah.

**Chris Gammell:** I was going to say, is this just because you're fishing crap out of the garbage again? Is this, is this your, your, your weird hobby coming to bite you?

**Dave Jones:** Well, yeah, kind of.

**Chris Gammell:** Yes.

**Dave Jones:** Yes. So it was like, I know, just buy the proper motherboard.

**Chris Gammell:** I'm not going to be one of those people that says you should just go buy a MacBook, but like, you know, go buy a goddamn computer, Dave.

**Dave Jones:** I did sort of do a poll on this and ask, well, there's three options. One, I can go through the AMD processor loan program grown, right? Sounds like a chore, right? Or I can, or I can de-solder, de-solder the flash chip from the board and then put it in my programmer and then try and program it. But apparently there's a whole slew of issues with that. Like it's an incremental upgrade, a flash binary. So it's not like, apparently you have to upgrade to two previous versions before you can upgrade to the latest one. So it's not like, oh, I just download the ROM image from the website and then flash it in my programmer. Apparently it's not that easy. So say half the people out there and then the other half of people say, oh yeah, you can just do that.

**Chris Gammell:** Well, even the half that say it's not easy, they like doing this stuff.

**Dave Jones:** I know, they just love it. What is the matter with you?

**Chris Gammell:** Don't do this. This is a terrible idea.

**Dave Jones:** So would I normally, right? But I don't want to do computer videos.

**Chris Gammell:** Go buy a normal computer and then do this on the side.

**Dave Jones:** And then do it on the side. Yeah, exactly.

**Chris Gammell:** Buy a tool and then make a project. Yeah, right.

**Dave Jones:** No, but I don't want to make computer videos. It's like, no, I don't know. No, it's just, I have no interest in it at all. Okay. The only reason I make these computer videos is because I'm building this computer anyway. I might as well turn the camera on. Because you're so upset.

**Chris Gammell:** You're so upset about it. Yeah.

**Dave Jones:** I might as well switch the camera on, right? So, you know, so a video pops out of it. But I don't go out of my way to make computer build videos, you know, and stuff.

**Chris Gammell:** So it's just...

**Dave Jones:** Pulling stuff out of the garbage. Anyway, there's always something. It's like, and then, oh, then, oh, we're not finished yet. Then people go, oh, don't know. Don't use that motherboard at all. Don't waste your time changing the firmware, everything else. Because that's got poor VRM, right? Which is a voltage regulator module. That's computer speak. We'd call them voltage regulators, but they're VRMs in the computer motherboard world. Right? VRMs. And, oh, yeah, no, it doesn't have adequate VRM to power that new Ryzen 5000 processor. You know, and it's like, oh, it'll be marginal. It'll drop out all the time. It'll do this. And I was like, oh, God. Yeah, right. Okay. I'll just go out and buy a new motherboard. That just works. So it's like flogging a dead horse kind of thing. Yeah. I don't. Yeah. No.

**Chris Gammell:** Good luck. Good luck, man.

**Dave Jones:** It's so painful. I like the whole computer. And as you said, it's so advanced.

**Chris Gammell:** I'm at the point where I'm... Actually, so I'm working with a firmware engineer. And the other day, he's asking me, like, why didn't you upgrade from version 4 of this software to version 5? And it's a great question, right? Yeah, yeah. Of course. Why wouldn't I? Like, the latest thing supports the latest OS. I'm like, look, it's just not broken. And I put it in a VM. And it's just sitting there. And I never have to touch it again. Yeah, I know. Yeah. It's just I'm allergic to these kind of changes. And I don't know. Like, it sucks. I don't want it to work like this.

**Dave Jones:** Well, this firmware engineer has not had it come a gutter on them. Once they do. Once it happens to them once, really? And they still want to keep on the bleeding edge of their latest compiler. I just would know. If it works, it works.

**Chris Gammell:** I mean, this isn't really on the bleeding edge. Yeah. But yeah, it's... I don't know. So I also have another perspective on this, which is, like, I've been doing more, like, documentation stuff lately. And this cool program called DocuSaurus, which is all, like, Node.js. It's all, like, JavaScript-based, right? And it all dynamically builds. And, like, it really is super cool. But every time I see anything with, like, Node.js, I am flabbergasted at, like, how many things have to, like, go right in order for this. Like, seriously, it's just, like, pulling down, like, 500, 1,000 dependencies. Really? And it's just, like, everything. I mean, like, and don't get me wrong. The people writing the software are amazing. They have tests written. And, like, they have interactions. But, like, just seeing all this stuff happen, like, my heart starts to race. I'm just, like, oh, my God. Nothing's going to work. Nothing's going to work. Nothing's going to work. And then it works. It works. And you're amazed. Yeah. I am amazed. And, like, it's a testament to, like, good methodology of, like, writing tests and, like, making sure things can, like, regression testing and stuff like that. But, like, looking at it, that is not how I operate. I'm, like, no. It worked once. I'm going to make it work once. And it's going to keep working like that for the rest of its life. And it's going to work for 30 years. You know?

**Dave Jones:** And I'm still using ProTel 99 SE. You know?

**Chris Gammell:** Yeah. But, I mean, I don't know. Like, there are definite arguments against doing it the way that I'm talking about. It's not as robust. It's, you know, it's not safe to do that. You know, if something does change, you lose the VM or whatever. And it's, like, you can't build it again.

**Dave Jones:** Right.

**Chris Gammell:** And, like, someone's going to be, like, oh, you should get Docker. And you can build Docker no matter what.

**Dave Jones:** And I get, okay, cool. And then Docker's out of fashion in five years' time, you know? I mean, I don't know. Yeah. Come on.

**Chris Gammell:** I'm always going to get myself in trouble when I start talking about software stuff like this. But, like, the methodology change is very stark for me where I'm, like, I don't want to work on tooling. I want tooling to work once. And I want to lock it up. And I want it to never change ever again. And I know that's stupid because there are security issues. And there's upgrades. And there's all these other things. But, like.

**Dave Jones:** No. Only change if it goes wrong. No. I don't. Like, if, you know, if your compiler's not working and it's got a bug or something, yeah, you might have to upgrade your compiler. Otherwise, no. But just, like, why? Yeah. Why? Why would you upgrade? It's just dumb.

**Chris Gammell:** Did we talk about this last time?

**Dave Jones:** Oh, we've talked about this a million times. Come on.

**Chris Gammell:** No, no, no. So we were talking about. Who was I talking to about that? I think it was you. But, no. It was not. Oh, boy. I've been recording other podcasts lately. But we were talking about, like, the idea of, like, the idea that, like, every time you open a CAD program, it's slightly different. Who the hell was I talking to? I just did an interview the other day, dude.

**Dave Jones:** Well, there's your problem with key CAD, you know?

**Chris Gammell:** No, it's not. That's the thing, though. It's, like, there's a stable thing. Whereas, like, a lot of the SaaS tools, which is something we're going to talk about here, a lot of the SaaS tools, including Altium, like, they're, I think, maybe this was you and I, but, like, I don't know.

**Dave Jones:** Yeah, but Altium doesn't upgrade unless you do it, that I'm aware of.

**Chris Gammell:** Yeah, but they're moving into the SaaS world, right? That is the eventual thing, which is every time it opens, it's been tested. It's, you know, like... It's been tested in quote marks. No, no, no. There's, I mean, there are, like, you can say this sort of thing, but, like, to use an easy example, every time I open Fusion 360, it's a slightly different version. And, like, that is a very SaaS model. Yeah, it's like, you know, it's... Okay, right. You're downloading the latest. You have the latest thing. It's always being upgraded. It's continually improving. And that's fine if it keeps being improved, but at a certain time, it shuts off. This is just the new SaaS methodology.

**Dave Jones:** For those who don't know, SaaS is software as a service.

**Chris Gammell:** Thank you.

**Dave Jones:** That's good.

**Chris Gammell:** Versus, like, the thing you said. Some people lock down on ProTel 99, and they're still just, like, doing that one thing. Yeah, yeah. That's its own thing, you know? And it's just, like, they're... I think the modern methodology is this more, like, everything updates. Everything updates, but it's tested, you know? And it just kind of, like, pulls down the latest. And there's reasons to do that. I have no doubt about it. But as...

**Dave Jones:** Yep. It's not for everything.

**Chris Gammell:** As an aspiring, old, grumpy engineer, it scares me a little bit. That's all I'm saying here. Yep. Totally. Now I have to go and look up who the hell I interviewed the other day, because my brain has fallen apart. I haven't been sleeping much lately, man.

**Dave Jones:** Speaking of things that scare the crap out of you, and a beautiful segue, even if I do say myself, Altium has rejected a takeover bid from Autodesk, who have the Fusion... No soup for you. They do Fusion 360, right? That's right. That's who it is. Software as a service. And everyone went, holy shit, they dodged a bullet there. I think every Altium person, like, just collectively sighed in total relief that they...

**Chris Gammell:** Release the old cornhole. Yeah. Yeah.

**Dave Jones:** So...

**Chris Gammell:** It's interesting, because it was Altium that did a press release, basically saying, look, we've got this bid and...

**Dave Jones:** It wasn't good enough. They did know, for those up front, and I'll say up front, Altium did not reject this based on principle. They rejected it based on price, right? Autodesk...

**Chris Gammell:** Which is pretty rich, given how much they were worth about 10 years ago.

**Dave Jones:** 10 cents, and now they're, yeah, 40, 35 bucks. Yeah, right. But basically, Autodesk offered 33% above the current market share price value, right? So a big jump above, and Altium went, nope, not good enough. So the Altium share price jumped 33% in response to that, thinking that...

**Chris Gammell:** Yeah, nothing like a reference point to give a bunch of stock brokers like, ooh, okay, yeah, we'll move it up.

**Dave Jones:** But then again, to be fair, Altium has been at a higher price than this. It was like $35. Altium has hit $40. So, you know, very briefly, then it went back there, $23 or something.

**Chris Gammell:** Yeah. $25. So Altium... I'm sorry, Autodesk is no stranger to buying companies and, you know, enveloping them. That's fine. I'm very curious. Yeah, Eagle's one. But I mean, not just on the ECAD side, right? Eagle is the most... Oh, yeah, of course. Yeah. Oh, I'm sure. But actually on the MCAD side, right? I mean, like they... Autodesk is just a... It's a juggernaut at this point. I mean, they're just big. Like, and I just... Man, what would this have looked like? It would have been very interesting.

**Dave Jones:** Well, Eagle would have... Yeah. Like, surely, like Eagle would have to die. Like, or something's got to die, right? You know? Yeah. I don't know. It wouldn't die at first, right? This is what all the discussion on the E-VBill forums about, right? Oh, okay. Well, we get in. It wouldn't die at first, of course. Yeah. You know, they keep both going because they don't want to shock. When you buy a company like this, you don't want to rock the boat, right? You don't want to scare everyone off. So, you know, you just reassure them. Oh, don't worry. It was still just going to run it as a separate company. And then 12 months down the line, it's like, yeah.

**Chris Gammell:** Right. That's when it gets... We've decided we have to make some small changes and then on and on and on and on. Oh, sorry.

**Dave Jones:** We do have to go. It's better for you, the customer, if we go to the software, to the rented software model. We have to move production to China.

**Chris Gammell:** Oh, that was a shit show. Big old NBA playbook right there.

**Dave Jones:** Oh, boy. Yep. Yep. Yeah. So, I don't think there was anyone who was any Altium user who went, oh, yeah, buy and buy Autodesk. That'll be great. Yeah. Although, no, there was some discussion that they would take bugs more seriously than Altium do. Like, because Altium's famously had the same bugs for 20 years. Like, they just, you know, like... So, apparently Autodesk, apparently everyone says they take bugs really seriously and they nail them on the head and it's done. You know? So, people said that would be the only benefit of being bought.

**Chris Gammell:** Yeah. So, I just... You saying the bug thing actually finally shook my stupid brain loose. I just interviewed John Evans, one of the lead developers on Kaikad, and we were talking about this for like a half hour. So, that's... Right. Okay. My brain is a big old pile of mush right now. It is oatmeal. So, yeah. But that'll come out later next week to talk about...

**Speaker ?:** Yeah.

**Dave Jones:** So, now everyone on the forum is talking about, oh, who should buy Altium? Because Altium have basically come out and said, oh, yeah, we're for sale. Give us your checkbook. You know, you can buy us.

**Chris Gammell:** Every company's for sale, right? Yeah, yeah. But this is saying, yeah, we'd actually... Yeah. We consider this enough to release it. So, yeah. We're taking all...

**Dave Jones:** Well, there's a lot of people who say the AutoCAD company, is it Salt Systems?

**Chris Gammell:** That's not AutoCAD. That's... That is not Inventor. That's also Autodesk. It's SolidWorks.

**Dave Jones:** SolidWorks. Okay. Yes. Everyone. Yeah, yeah. Because Altium integrates with SolidWorks.

**Chris Gammell:** Yes.

**Dave Jones:** So, everyone said, oh, yeah, wouldn't that be great if they bought them?

**Chris Gammell:** SolidWorks, they white label Altium, I believe. What? I think so. Isn't that them? There's an MCAD company. Really? That does... They white label Altium.

**Dave Jones:** Oh, okay.

**Chris Gammell:** Yeah. SolidWorks PCB. It's just Altium.

**Dave Jones:** Oh, really? Okay. I had no clue. I was not up to date, obviously, in the industry anymore.

**Chris Gammell:** It's weird. I mean, it's really just like a branding thing. Yeah, yeah. I think they sell it. So, I think, yeah, I think that would make sense. I don't think Dassault Systems is that big. I think they're...

**Dave Jones:** Well, they're a military company, aren't they? Dassault? Or is that a different subsidiary or something?

**Chris Gammell:** I don't know. Dassault. I mean... I don't know how...

**Dave Jones:** They made fighter jets, right? This is a big company.

**Chris Gammell:** They made fighter jets? Really? Oh, I didn't know that. Dassault.

**Dave Jones:** Yes. I believe they make fighter jets. Yes.

**Chris Gammell:** I believe it's Dassault. Dassault.

**Dave Jones:** Oh, well, yeah. Yeah, French. I don't know.

**Chris Gammell:** I'm probably wrong. Yeah. No, I don't... Yeah, I think it comes down to how big companies are. It doesn't really matter at a certain point. I mean, like...

**Dave Jones:** Yeah, they're a French aircraft manufacturer of military and business jets, Dassault Group.

**Chris Gammell:** I didn't know that. Okay. Yes.

**Dave Jones:** Yes. Cool.

**Chris Gammell:** Makes sense that they would have a 3D CAD group then. Yeah, right. To design their planes and their... Yeah. That's right. Yeah.

**Dave Jones:** Yeah, no, they're huge. Cool. Yep. All right. Yep.

**Chris Gammell:** Yeah. Maybe them then, you know? Yeah. It doesn't really matter. Yeah. I mean, like, I think it would be much more interesting if it was Autodesk because it would be such a significant change. Right. You know, there's such a significant shift in ownership and integrations and... Yeah.

**Dave Jones:** Let us know what you think down below. Yeah. It's a matter of who should buy Autium, not if Autium should sell. They're obviously... Right, right. ...looking for that payday now. Ever since they ousted the CEO, the founder, Nick Martin, it's like, oh, yeah, now we're a, you know, four or five hundred billion dollar company, which is, I think they're heavily overvalued. But anyway, that's just me. Okay. Well... Yep.

**Chris Gammell:** People can go and listen. Matt Bergen was on the Amp Hour two years ago, one year ago. Oh, yeah.

**Dave Jones:** That was a long time ago.

**Chris Gammell:** Yeah. Yeah. He is one of the lead guys on the electronic side of things at Autodesk. And also interesting, he used to be at Autium. Yes. Yeah. Yes. Yes. That would be interesting. Like, it'd be like him coming back home. So you can listen to him on the Amp Hour. We have that episode out there. So...

**Dave Jones:** So, yeah, that'd be interesting. Hmm. Anyway, I have no opinion. I don't really care anymore. I'm not really... Yeah, I mean... I don't care that much about the Autium system anymore.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. I just don't do enough work in it.

**Chris Gammell:** Yeah. Well, when you do, you might be using the LM3914. What is this part?

**Dave Jones:** You might use the LM3914. Please tell me you don't know what... You know what the LM...

**Chris Gammell:** I don't know what it is. You do not know of the time. It drives LEDs, LCDs, and vacuum fluorescents, but I'm using the marketing section at the top.

**Dave Jones:** The LM3914. The LM3914. The LM3914 is the chip of the 1970s. Come on. Along with the LM741 and the, you know, triple five timer. Come on. It's one of the classic...

**Chris Gammell:** Classic.

**Dave Jones:** ...chips that was used in every hobby project and every, you know... Because, like, audio was big in the 70s. So, all those VU displays that, you know, there's LED VU displays that you saw in anything. Yeah. Yeah. Yeah. And, like, guaranteed uses the LM3914.

**Chris Gammell:** Nice. Because... So, is it just like a shift register and a LED driver? Is it a bunch of LED drivers?

**Dave Jones:** Well, it's officially known as the dot bar LED display driver. And that's what it does. It drives 10 LEDs in either a bar graph format or a dot format. So, you can, like, just have a dot instead of a bar graph, right? And it has a pin to, you know, actually select. You can select the mode on it and stuff. And it's basically, yeah, analog signal in and digital bar graph out. And it's just... It's very cool.

**Chris Gammell:** That is cool. Okay.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** So, this is like... Yeah. So, you... So, all right. So, it does all the work for you, basically. It does all the work. It's got... A bunch of comparators.

**Dave Jones:** 10 comparators inside. There's a voltage reference source. 1.25 volt voltage reference source. When I was a kid, I had an LM3914 and I used it as a voltage reference, you know, to actually check my multimeters were good, you know, because the voltage reference in that was better than my analog multimeter at the time, you know. So, right.

**Chris Gammell:** So, the reference... Oh, because that was the comparator reference you're saying?

**Dave Jones:** Yes. Yes.

**Chris Gammell:** Got it.

**Dave Jones:** So, it's a built-in Xenor voltage buffer.

**Chris Gammell:** What's the reference voltage?

**Dave Jones:** It's 1.25 volts.

**Chris Gammell:** Yeah.

**Dave Jones:** I don't think it was that good, but I can just remember as a kid thinking, oh, this is better than anything else I've got, you know. So, I used my LM3914s, which you could salvage from, you know, any bigger gear at the time. And there's all... Just like the Triple Five. There's like hundreds of different novel things you can do with the LM3914. There's, you know, there were, you know, like contests back in the day. Oh, who can design the... Who can submit to the magazine the most innovative novel way to use an LM3914?

**Chris Gammell:** You know, so... A lot of blinkies, I'm guessing, right? A lot of blinking things.

**Dave Jones:** Yeah. It's very... Yeah. It's very cool. But it's a voltage source with a bunch of voltage comparators and like an op amp in there. And it's got... You can choose the mode and... Yeah. And Bob's your uncle. Gives you a bar graph out. It's great. Anyway, the reason I'm mentioning this, chip of the week. Chip of the week. Chip of the week. And you can set...

**Chris Gammell:** Chip of the week, 1974.

**Dave Jones:** And you can set your LED bright and you didn't need dropper resistors for the LEDs. And you can set your LED brightness with one resistor. Beautiful.

**Chris Gammell:** Right?

**Dave Jones:** Bobby Dazzler. Right?

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Anyway, the reason I bring this up is because somebody emailed me. They said, hey, you know, I'm building like 500 of this board and it's got an LM3914. And I went to the assembler to get it quoted. And like the LM3914 is so expensive. Should I continue with this or should I like redesign it? Rip out and redesign. Yeah. Rip out and redesign the LM3914. But it works. You know, I've already done the engineering. It works. I'm ready to go. And it's like, but... You know, and it turns out that they were charging like $3.50 for each one of these chips. And sure enough, if you go check your fine chips or your octoparts or whatever, yeah. You know, oh, you can get it for as little as like $1.50 or something like that.

**Chris Gammell:** Uh-huh.

**Dave Jones:** But even if you go to LCSC, right, they don't have any stock. But yeah, it's like $1.50 or something. But if you go to AliExpress, Alibaba, it can potentially be as little as $0.10, so they claim. But, you know, they're obviously not genuine ones. But you better test it before you put them in. They're not genuine ones, right? Yeah. So they're, you know.

**Chris Gammell:** Yeah, that's good. I mean, but that might work, actually. I mean, it might be like a localized fab. Yeah. It's just doing a replicated part.

**Dave Jones:** Well, it's not exactly an advanced process. So I wouldn't be too concerned about using a fake in this particular circuit. Yeah. As long as the fake actually works. I was just saying, make sure there's silicon inside the package. Yeah. But, you know, it's not like a fake, you know, fake precision op amp or anything like that, right? It's not like a fake transistor that doesn't have the parameters, right?

**Chris Gammell:** $1.50, you could, I mean, depending how much current you're driving through the LEDs, like you could probably just get an 80, you know, get like a tiny micro with like 20 pins. Exactly. Put the voltage into an 80C, you know, and just drive it like that, right? I mean, like, depending, you know, you'd have to put some bets or something. Yeah.

**Dave Jones:** But then you don't, you know, you don't have the ability to, but then you'd have to have an external resistor for each LED and stuff like that. It doesn't drive the LEDs the same way. You know, you can't just use a digital output to just drive it. Yeah.

**Chris Gammell:** I mean, that would just be the redesign exercise if it was there, but you're right. And it is, that's the thing about these specific chips. It's like they're, they're, they kind of suck to design out sometimes because it's just like, oh yeah, that one chip does everything.

**Dave Jones:** Yeah.

**Chris Gammell:** You know.

**Dave Jones:** So I thought it would actually be an interesting video to, to do like what would be involved in actually, if you had to just using the LN3914 as an example, which is a big, which is basically an analog chip, really, you know, could you redesign it? How would you redesign it? Like it's a dip package chip and then have everything fit in.

**Chris Gammell:** You know why I like this video series? Why? Because this is basically Dave Jones saying, you know, what's good content? The job that Chris used to have that he always makes fun of him for.

**Speaker ?:** Yes.

**Chris Gammell:** Obsolescence engineering. Sustaining engineering. Yes. Sustaining engineering.

**Dave Jones:** Component obsolescence engineering.

**Chris Gammell:** I mean, I do think it's actually very interesting in that way. Right. It's like you're, you have a, you have an extremely constrained problem in that. Like I have, I have a working device. I want it to work exactly the same. I cannot use the exact same part. What the hell can we do here? And how can, how cheap and fast can we make it? So like from that perspective is actually pretty, that's a, that's a cool problem.

**Dave Jones:** You know, engineers love constrained problems. Engineers hate. Oh, just do anything you want. They hate it. They hate it with a passion.

**Chris Gammell:** Yep. I agree.

**Dave Jones:** Yeah. It was funny with David when he was working here. I was like, oh, I just go, oh, don't worry about it. Do it any way you want. And it's like, oh, no, no. Give me constraints. Give me constraints. Give me a, give me a.

**Chris Gammell:** That's, you know. That's the hard part about products. I think in the first place. Right. I mean, you've talked about that when you were doing the micro supply stuff of just like. Oh yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Like we could do anything. Right. But then what's the cost going to be? What's going to, what are the, what are the size constraints? The weight constraints?

**Dave Jones:** And I did end up doing anything I wanted. And that's why I went in like three different directions and everyone hated it. And I got so much hate mail over. It's like, oh, why don't you just do some specifications, stick to it and finish the damn project. Ah, piss off. You know, like I'm having fun, you know, like. But yeah, that's what happens. Right. When you're just left with free constraint to do anything. It's like.

**Chris Gammell:** Yeah. Totally. Totally.

**Dave Jones:** Yeah. So I don't, it'd be interesting. So I'm, I'm not sure how easy. And, and you would have to fit this. And yeah. And you would have to fit it on a PCB that, that could fit into a dip 14 or dip 20. Is it, is a 20 pin?

**Chris Gammell:** I've seen MLCCs on the, on some of the packages for the TI part, at least it was MLCC. Oh yeah.

**Dave Jones:** You can get alternative packages, but most people use the dip.

**Chris Gammell:** Got it. Got it. Yeah. Okay.

**Dave Jones:** I, I think it's quite high. I think it'd be quite hard to get a surface mount version of the LM3914 these days. Don't quote me on that, but.

**Chris Gammell:** Oh, sorry. PLCC, not MLCC.

**Dave Jones:** Yes. Right. Yep. Yeah. No, I hardly anyone uses that package. That's like, it's probably rare as hen's teeth. Yeah.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. Switching out the dips, Philip Frieden, but he did like, like pins on the side of a PCB that actually made it like a dip package. Did you ever see that? It was like a Bluetooth, like wired.

**Dave Jones:** Hmm. No, not, not recalling it.

**Chris Gammell:** It was a, a dip package basically with like, he had machine, like stamped out these metal pieces that looked like the legs of a dip package. Right. And then he would solder those to the side of a PCB. Right. And it would effectively make like a dip size package. I've seen something similar. Yeah. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** And it sort of had like a, like a BGA, like a Cortex M0 on it with Bluetooth. And, uh, and then it was like, as a way to, to communicate, it was like a serial wire thing. So I don't know what ever happened to that project. I'll have to check that out. But it was a cool, it was cool.

**Dave Jones:** Yeah.

**Chris Gammell:** Philip was on the show a long time ago.

**Dave Jones:** So great fun. Yeah. I, I reckon that'd be a terrific thing to do. So yeah. Yeah. Probably very difficult. Let me, you know, I'm, I'm looking at it and looking at the data sheet now and I'm going, Hmm. Yeah. To, you know, duplicate every functionality and it was like, you know, I was going to do this with a triple five timer once. I was going to replace it with a dip because I thought I found a, an eight pin dip micro that had the same power pin out as a triple five.

**Chris Gammell:** Huh?

**Dave Jones:** But I think I'm wrong on that. I think I was, I think I was mistaken and that's why it never went ahead. But yeah. Okay. Because in theory, in theory, you probably could simulate a triple five timer in a micro. It's just a matter of getting the pin out. So, you know, it's a, yeah, yeah.

**Chris Gammell:** Yeah. That's, that's a weird one.

**Dave Jones:** Oh, it'd be, it'd be limited to voltage, of course. Like, you know, it's. Yeah.

**Chris Gammell:** I was going to say, cause I mean, it is BJTs internally, right? So there's some, there's some current draw to the pins and stuff like that. Also, that's a fantastic waste of resources, but. Yeah. Yeah. I guess if you have the same, the same pin on. Yeah. Well on the, uh, not being able to find chip stuff, I, you know, anecdotal evidence only, of course. But I've been getting emails saying, Hey, this is back in stock. You know, you put in your email for various parts. And yeah. So like back in stock emails, it's a nice thing to get. I'm not sure. I wouldn't exactly use that as a, we're out of the woods kind of thing.

**Dave Jones:** Oh, there's people who were saying it's going to get worse.

**Chris Gammell:** I totally could see that. I'm just saying this is pure anecdote. Right. I've gotten more than one. That is great. You know, like it would have been greater if I would have gotten it right when I needed those parts, but instead, uh, I did not. Uh, and, uh, yeah. So I think it's, I think it's just comes down to like, it'll be interesting. I wish there was some way to map like as different parts open up, you know, like you're going to have lots coming out of, so in this case it's a TI part. It's an industrial part. It's available from TI, right? They do direct distribution. And so like, will they be able to buy it at a distributor? I don't know. Maybe, but like it, uh, is it, you know, but the fact that there's enough even internally that they say, yeah, there's some available. That's something for me. They may have been bought up already. You know, that's the other thing. Like there's all this latent demand. Well, that's the thing.

**Dave Jones:** All of these big distributors, they put in long lead time orders for these parts and guess who's going to get fulfilled first, you know? Oh, totally. Yeah. Yeah. They should. So the web store will be a, you know, distant second.

**Chris Gammell:** So as a correction to last time, uh, I said that, uh, Digi, DigiKey does place rankings and I was, I was roundly corrected about that. So my mistake, uh, they said that.

**Dave Jones:** So I was right.

**Chris Gammell:** Was I, you were right about that. Yeah. There are some sites that do it, but, uh, DigiKey is not one of them.

**Dave Jones:** I didn't think DigiKey was one of them. Yep. All right. Indicated.

**Chris Gammell:** Yeah. Nothing. Thanks a lot, DigiKey. Makes me say that Dave was right. I don't care about, you know.

**Dave Jones:** Oh, it was them who actually corrected you, was it?

**Chris Gammell:** Oh yeah. Yeah. It was my friend at DigiKey. So yeah. I mean, yes, it was my friend who's told me and, you know, I trust him. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** I thought that wasn't my experience at DigiKey. Like, you know, so, yep.

**Chris Gammell:** Yeah. So hopefully, you know, I don't know. The supply chain is going to keep being a problem. We didn't talk about it last time. I don't think we did, but there was a, there was a video that was by Wendover, uh, systems. Wendover.

**Dave Jones:** Wendover Productions. Yes.

**Chris Gammell:** Yeah. And they talked about it. And the one thing in that video that stuck out that I think someone actually mentioned on the, uh, in the, the subreddit comment section as well is the, the fact that Toyota specifically, right. So a lot of this, like just in time stuff is like, you know, tied back to Toyota production system. And the thing that's really interesting about that is that Toyota is specifically called out as saying, has having recognized. Correct.

**Dave Jones:** Yes.

**Chris Gammell:** That this was happening and they, they bucked their own trend, right? They said, no, actually we need to turn off just in time. This is a huge risk. And they, they had a bunch of parts and that's what allowed them to keep going. And, you know, when I talk about the NBA playbook, I've, I've been challenged on it before. Like, you know, I said the stupid phrase about it. The NBA playbook in my, in my experience would be someone being like, well, no, no, no, no. We do just in time. It doesn't matter. We're just going to keep, just keep going by that same rule. But the, I guess the only way to really explain it would be the opposite. And the opposite would be taking a critical look at the, at the industry, what's going to happen and saying, actually, our rule is wrong. We need to do something different. So that is very impressive to me.

**Dave Jones:** If, if, if you're a smart company, you have some, you have an expert that just does that, that continually checks your processes and goes, is this still the right way to do it?

**Chris Gammell:** Right. Exactly.

**Dave Jones:** Like do it every, do it continuously, not like every 12 months or something, do it continuously. And they would have looked and went, well, like 90% of our chips come from one factory in Taiwan, TSMC. Right. And it's like, that's bad. That's really bad. Right. If like, none of this, you know, they didn't, didn't predict COVID and all the rest of it. They just went like, that is a huge company. That's a systemic risk to our company. If something happens to that factory or war breaks out or something else, I don't know, there's an earthquake there and the whole factory is ruined or whatever. We are screwed. So they, they, they took the proactive.

**Chris Gammell:** If there's an earthquake and TSMC goes, we're all screwed, dude.

**Dave Jones:** I know. Exactly. But they were smart enough before this pandemic to go, well, we've identified this. We're going, I don't think they, I think they just stocked up really well. They did. They had like six months worth of stock or something. They went, right. Right.

**Chris Gammell:** But that's breaking your own rule. It's not. Yeah. Exactly. No, exactly.

**Dave Jones:** Yeah. Because they practically invented just in time. Right. Yeah. Yeah. Right. Yeah. They literally did. I believe. Right. It was, it was their invention. Yeah.

**Chris Gammell:** Well, I don't know. I don't know if that's. TPS reports. Yeah. TPS. They're out of production system. Yeah. I think that is, but yeah, that, that is applied to like, you know, having parts on the line and delivery at the cells and all that stuff.

**Dave Jones:** And they bucked that trend and said, yeah, we're going to have six months worth of stock minimum of every single item on our cars. So they're still manufacturing cars while everyone else is shutting down their factories. So yeah. Hats off to them. Yeah. Yeah. Yes. Well done. Definitely. Yep. Somebody earned their money there. That's right. Yeah.

**Chris Gammell:** Probably a group, you know, the size. Maybe. That's a significant. Yeah.

**Dave Jones:** Oh yeah. It's not one, one person goes, right. We're suddenly going to order six months worth of parts. Right. That would have been a huge capital outlay. There probably would have been a lot of people within the company going, no, we're not going to spend this money. No. Why? It's been working for us for 50 years. Right. We invented this system. It's fine. Look at the track record of the system. Right. Just look at the track record. So imagine being there trying to convince someone, and this has been working for 40 years or whatever, however long the production, Toyota production system has been around and going, this has been working fine for all this time. In fact, it's made us the company who we are and you want to change that and suddenly go and buy six months worth of stock. Are you mad? Like, you know, that, that, that would have been a tough sell, but you know, they're heroes now, you know, like, yeah, fantastic. Fantastic. So have, has anyone out there in the audience got an example of that where you went, you know, you had tried to, you, you know, bent over backwards, put your ass on the line to convince everyone that, you know, so, you know, something was a, you know, something was a problem and, or could potentially be a problem and no, we should work on this. It actually is something just popped in my head. It was the nine, nine 11, you know, the twin towers fell, right. There was some company on the, you know, the hundredth floor, like the very top floor. Right. And there was this one guy like huge, huge company. And they were the only ones to actually survive on the top floors or whatever, because there was this one guy in the company who insisted on doing fire drills every week or something. Like he, he was known as the fire Nazi or something, you know, and, and everyone, you know, but he was adamant that this is going to save our lives one day. And sure enough on the day it did every single person in that company way above where the planes hit got out because, you know, he drilled everyone so well for years and everyone thought, Oh God, this is just, you know, this is just dumb. Right. Right. You know, yeah, she'll be right. But it, you know, now is a hero for, for saving every single person in the company. Right. And same thing with Toyota. Well, you know, not saving lives, but you know, saving jobs. Right. So, yeah.

**Chris Gammell:** Well, it's interesting with the, uh, the Toyota thing too, because there is like that culture of like pulling the, the, the cord on the line. Right. So like, that's part of the TPS system is like pulling the cord that stops the entire line.

**Dave Jones:** Oh yes.

**Chris Gammell:** You have to be encouraged to do that sort of thing. And that's part of the, the, uh, boy, I have, it's been a long time since I've looked at TPS stuff, but like, but there is something about that where you basically pull that, you basically pull that line or you pull the cord and everybody stops.

**Dave Jones:** I've, I've done that many times being the head technical person in a production environment that works 24 seven.

**Chris Gammell:** Yeah.

**Dave Jones:** And I had the power to go, right, everyone stop. I need to fix this. Otherwise it's going to cause a huge grief, you know, in a month's time. So yeah. Many times I've had to stop production.

**Chris Gammell:** I just can't even imagine Dave's smugness when that happens.

**Dave Jones:** And we're, and we're talking like, you know, it costs like $50,000 an hour to shut down that line. Sure. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** It's, you know, it's huge dollars. So I, I, I had to make the call that, you know, sometimes, Oh, we only, okay. We can just shut down part of this line and, you know, it'll only cost us 10 grand or something, you know, but yeah. So it was a big thing, but you sort of have to trust your employees in that position to make the call. It's kind of, you can't just have a committee and go, Oh yeah. Okay. We'll shut down the line next Tuesday for an hour. And you know, it's like, you know, some things just have to be fixed. Right. Yeah. So, yep.

**Chris Gammell:** You know, it's interesting. Now people are going to, now all the software, if there's anyone left listening, software after all this, I just found an article. I was just looking up the stop the line thing and someone actually relates it back to continuous integration, which is basically what I was complaining about before. So I'm, uh, I don't know. Do you know what continuous integration is?

**Dave Jones:** Oh God, I've heard the term. I, I, it, it has been deliberately expelled from my memory. I'm sure of it.

**Chris Gammell:** Yeah. Yeah. I mean, like basically the idea is that like, if you do a, and I've been like running into this more with some of the software stuff I've been doing, but like the, if you have all the systems set up, every time you do a commit to the, to the main part of your repo or your repository, basically it'll go through all the builds, go through all the tests. And if it doesn't work, it throws a flag and basically says, Hey, look, something's broken here. Chris just tech gen some crap code and everything's broken now. Right. Right. And so then the, what we were talking about earlier was continuous deployment where basically once it has been put into the world and it's been tested and it's been verified, you just push it out to everyone. Right. So that's kind of the idea there. And that's what, that's the part that scares me. The integration pieces leak at least testing, like you have tests in place and, and, uh, you know, there's some startups that are trying to do this for hardware too. And I, I love the idea of it. I just, I haven't wrapped my head about how.

**Dave Jones:** Everything works great in theory. Well, I just, yeah.

**Chris Gammell:** I don't know how it would work. Like in terms of like, uh, like, like with schematics specifically in, in layouts.

**Dave Jones:** Well, the, uh, price of failure is much larger for hardware. Okay. We're going to manufacture, you know, 10,000 of these boards. Oops. Went, went wrong. Sorry. You know, like shit, you know, like evil. We've, we've got to scrap those 10,000 populated boards or we've got to rework them. Either way is painful. Right. Yeah.

**Chris Gammell:** I'd say that's actually an argument for this sort of methodology though too. Right. It would be basically be like every time you moved a resistor and you hit save in Altium or KiCad or whatever. Right. It would basically be like, all right, I'm going to go check to make sure everything's hooked up. All ERC passes, all DRC passes, everything, everything, everything. Right. And then once it's checked in, it's like, okay, no, actually you could go. And yeah. So the equivalent would be like, I've checked all these things, ERC and DRC all pass all of your tests pass, whatever. And not only that, we're going to go.

**Dave Jones:** Yeah, but you've got to physically build the prototype. You can't just push it to production.

**Chris Gammell:** That would be the craziest iteration of this would be like, actually we were building version 455. Now we're moving to version 456. And it's like, oh my God, that gives me some pause.

**Dave Jones:** Now I'm going to be absolutely wrong here. Right. And I know I'm wrong, but I'm going to use it as an example. I believe Tesla do something like this. They're like continuous refinement or something they call them. Apparently like it's not uncommon to build a Tesla one week and then build another one one week later. And then a week after that. And there's like three different subtly different builds. Like they've, they've, like they've changed the PCB a little bit. They've changed this. They've, they've modified this component. They've done that. Apparently like the, yeah, the people who tear down the Teslas and stuff, they go, yeah, every time we tear it down, it's different. Every, like every single, like, oh yeah, this was, you know, last month's model in three months time, it'll be like, it'll have all these subtle incremental improvements in it. There is no like one big jump. Like they're used to seeing in all the auto manufacturers.

**Chris Gammell:** Yeah. Like you have a model year and it's like release production.

**Dave Jones:** And it's like, you can guarantee, well, if it's that year, that model, it's exactly the same car, but no, Tesla's apparently make all these lots of incremental improvements.

**Chris Gammell:** Apparently that's what I've been hearing from the tear down people. That, that troubleshooting, if that, if that is true, and I'm sure we will hear if it's not, if that is true, that gives me heart palpitations. Just thinking about like, I know, I know. I mean, every, I mean, you'd have to do like indexing. Like we talked about in our past couple of shows about like, you're being able to back calculate what's in a box, right? What's on a circuit board. Every, you'd have to back calculate all the way and say like, oh, this is, you know, revision

**Dave Jones:** for 5722.

**Chris Gammell:** Right. And it has the following sub assemblies in it and each sub assembly. And it has this and this. And like, so now I have, you know, car serial number one, two, three, four, and I have car serial number one, two, three, five. And what the hell is different between them? Right.

**Dave Jones:** Yeah. Just tracking the serial numbers would be a nightmare. Yeah. Yeah.

**Chris Gammell:** You need like a diff program for like, for like a whole car. And it was just like, oh my God.

**Dave Jones:** That's a big ass spreadsheet, dude.

**Chris Gammell:** That's, I don't know if it'd be, I mean, if it's software based, like it might be easier, but man, I just, yeah, it just shows how many people are working on that kind of stuff. Cause. Oh yeah. Yeah. That's way bigger than me.

**Dave Jones:** So anyone working at Tesla, please confirm. Oh, I know.

**Chris Gammell:** I know a certain someone who's going to, who's going to talk my ear off about this. Oh, okay.

**Dave Jones:** Yep. Yep. I'm sure it's not as gung ho as that, right? I'm sure they've got a system in place to make sure it works and works well. Right. Yeah. But the fact is, is that they're different to other car manufacturers in that respect who will like, oh, you want to make a change? Holy crap. That's, that's six months of meetings to make a change, you know? Right.

**Chris Gammell:** Well, and I mean, with like a Tesla or anything that's really vertically integrated, you can do this more, right? Cause you're not putting, going external to the company and being like, oh, actually, you know, third party manufacturer, we need you to change this spec. And it's more like, actually, if you change anything, we're going to sue you as part of our contract. Yeah.

**Dave Jones:** Right. Yeah. Oh boy.

**Chris Gammell:** Yikes. Yikes. Yikes.

**Dave Jones:** They make all their boards in, in house. Don't they? Do Tesla make all their boards in house? Cause if they do, then yeah, it's much easier. If you do it all in house, then it's much easier to push subtle changes like that. It's like, yeah, no worries. Just, you know, slip this different part real on the, you can place machine and yep. Like, you know, done.

**Chris Gammell:** Oh, you mean like assembled in house? Yes.

**Dave Jones:** The board, the boards assembled in house. Yes.

**Chris Gammell:** I don't know. That'd be a good, good question for Vincent. We should have him back on for another three hour session.

**Dave Jones:** Yeah. I do believe he's still the head PCB designer at Tesla. I think, I think he's still there as far as I know. So yeah.

**Chris Gammell:** Great.

**Dave Jones:** And one thing you don't have to worry about with your supply chain, if you chose a Bosch component, they're, they're opening a $1.2 billion chip plant in Germany.

**Chris Gammell:** Yeah.

**Dave Jones:** Because they're a German company. So that's right. It makes sense to open in Germany. 1.2 billion. They're not just dishwashers. Yeah. That, that, that doesn't build you much of a chip fab. It doesn't build you a, you know, an, a Intel chip fab or something, but it builds you a chip fab that can do lots of sensors and stuff. Cause they're, you know, Bosch make all sorts of sensors and all sorts of, you know, custom niche semiconductors and stuff like that. So yeah. Yeah. Does it tell you 300 millimeter wafer? Does it tell you the 300 mil?

**Chris Gammell:** 65 nanometer. It says on a different link. 65. Okay. Right.

**Dave Jones:** 65. So it's not state of the art, but for doing sensors and analogy stuff and all sorts of other things. I think that's right.

**Chris Gammell:** Yeah. Especially with the analog stuff. That's right. Yeah. I mean, it doesn't, yeah, it doesn't sound that expensive. So it's in Dresden. There's other chip manufacturing there. I think AMD maybe. I don't know, but I think there are other.

**Dave Jones:** Anyway, it is the biggest single investment in the company's history. So it's a big deal. These guys, you know, they're going, well, yeah, look, I mean.

**Chris Gammell:** Yeah. Building sensors is interesting. I mean, like you think about like the cost, first off, you know, the, how much stuff is out there that needs to be sensed in the world anyways. But then like in terms of complexity, there, there is very obviously like analog complexity, but it's not like chasing, it's not chasing the three nanometer mark or whatever. It's not like the bleeding edge. Which is good. Processing. Of course. Yeah.

**Dave Jones:** You wouldn't want to, who would want to be in the three nanometer market for quids? I mean, I mean, 65.

**Chris Gammell:** So 65 nanometer is basically, I think I start when I was doing chip stuff in 2006. So that's when I started, we were doing 51 nanometer with the stuff we had on hand, the equipment we had on hand. And so that was like flash memory.

**Dave Jones:** That was state of the art memory. Yeah, exactly. That was memory.

**Chris Gammell:** Well, it was like, it was like one or two generations back, right? The state of the art, I was doing manufacturing. The state of the art was like the research people. They're already down at like 20 something nanometer. But, but still, I mean like the, so like, it's very realistic that if they had kept up the equipment and they, they may have been selling it off, they could sell it to someone like a Bosch and it could still be in use, right? It might be an AMAT machine that I programmed poorly at some point, you know, like that's, I think we talked about like a couple of weeks ago, we talked about like spinning chip fabs back up and it's like, of course they would sell off this capital equipment. It retains value because it's all serviceable, right? And yeah. So 1.2 billion might be, it might be the newest stuff, but it doesn't need to be. I was actually, I just had, I just chatted with our old friend, Sam's aloof earlier this week. Oh yes, right. Yeah. Making me feel old. He's now almost, almost a senior in college. Uh, you know, he's not just, no longer just making chips in his high school garage. He's not making them in his high school dorm room. Yeah. And, uh, yeah. Big step up. Smarter than ever. Uh, and making me feel stupid. But, uh, Sam was telling me about, uh, ASML machines, which is like some of the patterning stuff. And like, they're like a hundred, a hundred plus million dollars these days, you know, EUV machines, which is like what you need for the, you know, the three nanometer stuff. It's just like, so, so expensive price of secondhand gears going up. That's no, no, that was, that's leading edge. Not that's not what they would be using here. Yeah. So, I mean, yeah, with 1.2 billion, how many, how many, how many patterning machines could you even have at that point? You want one maybe? Right. Okay. Yeah. And I think, I think they must be using, you know, older equipment, cheaper equipment, you know, just, but that's great.

**Dave Jones:** Yeah. Okay. Cool. If anyone's in the know of exactly, you know, how they're setting that up for 1.2 billion, which is like, yeah, it's chump change for a fab.

**Chris Gammell:** Yeah. Really.

**Dave Jones:** It's, you know, yep.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** Hmm. Interesting.

**Chris Gammell:** Yeah. Yeah. I mean, it's interesting too, of like the type of sensors that are out there, they, they kind of keep rolling out and they keep doing, you know, there's new gas sensors and pressure sensors, everything that's out there. But you don't, they're not like these banner things. Right. And there's, they're sensing kind of, there's not like a whole bunch of new categories of sensors aside from maybe some of the high frequency RF stuff that's coming out, you know, like I don't really hear about like a new way of sensing CO2 or something like that. You don't hear about that as often.

**Dave Jones:** No, you don't hear about it because it's not, you know, Joe Average doesn't care. Joe Average in the computer geeky Reddit world doesn't give a crap. Right. So.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. I care.

**Dave Jones:** Well, I'm sure if you subscribe to Sensors Monthly magazine, you know, it's like front page news, right?

**Chris Gammell:** Right.

**Dave Jones:** I mean, come on.

**Chris Gammell:** I got to sign up for that Sensors Monthly or we got to start it.

**Dave Jones:** Don't laugh. There are magazines like that.

**Chris Gammell:** Or they were. I know. Yeah. They're like super targeted. Yep. And they're mostly ads, but that's fine. Right.

**Dave Jones:** I still get. I still get manufacturers monthly or something or manufacturers quarterly or something is in print magazine. They still send it to me. I don't know how I got signed up for it, but yeah, I still get this bloody copy of manufacturers something magazine. Yeah. I don't know.

**Chris Gammell:** One thing I'm excited about with Sensors and all this other stuff is like the idea that the idea of like not having to do much with it. So we talked about this a little bit when Brian Faith was on the show. So Brian is a CEO of QuickLogic and he was talking about they, they have Sensimal, Sensimal. Yes. Sensimal. Which is like a company doing this sort of thing, but it's like basically machine learning around sensors. And so instead of like being like, well, when this sensor increases at a certain, you know, slope, then it means this one thing. If it's decreasing at this other slope, it means another thing. And the idea is basically you don't care about anything at all. Now you just do the thing that makes the slope high. Right. So in Brian's case, he was talking about like a pressure sensor. You close the door and you do that a hundred times and you collect this data. And then you'd go and characterize it and say, actually, that's a, that's a door closing. And like, that is super cool to me. Right. That is basically obviating the need to know DSP, which is super cool to me. I hate that stuff. And so there's an article though about machine learning. And this is like tiny ML or machine learning. This is something that I think Google is putting money into it as well. But this just kind of this idea of not having to deal with sensors ever again. I mean, you have to deal with them, but you have basically, you put these things into like a, you know, it'll go into like a Cortex M4. There's another startup doing this sort of thing too. I can't remember the name. They've got ML in the name too, but, but yeah, it's just kind of cool thing. And basically you don't, you don't need to do the characterization yourself anymore. I don't know. I don't know if that's something you've had to do in the past, but I've, I've always hated it. You know, it's like, basically all I can do is like threshold, you know, it's like, oh, it's above a threshold. Yeah. Now it's a different state. And now it's like, it's much more, uh, that's smart, but it's, it's more characterized.

**Dave Jones:** Right. Okay.

**Chris Gammell:** So I think that's, that's probably the next layer of interesting stuff with sensors. So now you have a sensor, you can layer this machine learning data on top of it, having a model that spits out like, oh, actually we can tell when the doors close. Like Brian talked about instead of like, it's not like a threshold.

**Dave Jones:** It's like, uh, it's a, it's a, it's a pattern matching. It's a, um, yeah, exactly. It's an envelope matching.

**Chris Gammell:** Yeah, exactly. Yeah. Without any math that I have to do.

**Dave Jones:** Yeah.

**Chris Gammell:** That's what I'm really looking for.

**Dave Jones:** This is not new technology, Chris. They were detecting Soviet submarines like this in the 1950s, you know? Right. But not like this. They go, oh, from that propeller noise, we can tell that's in the cooler class, you know, Bravo. And that was manufactured in, you know, some sort of port in, in, you know, sure.

**Chris Gammell:** But they were doing it with math, right? They were doing it with a lot of scientists looking at sensor data and being like, all right, we're going to develop a model and detect based on that model. Now it's basically like, oh, the computer does the model for you. That's the, that's the part that I like. They're not doing math.

**Dave Jones:** Yeah, but it's, oh, no, I don't know. I don't see where, I don't see anything new here. Sorry.

**Chris Gammell:** It is most definitely new. And I think it's a, it's a, a semi big deal. Not, maybe not a huge deal, but it's a, it's a workflow thing for, I think people listening to this is a workflow thing that is an unexpected output from the neural net training side of things. Right. So like a lot of neural nets, they always talk about like vision and all this other stuff, you know, like being able to detect a dogs in the camera frame or a person or whatever. Or that's, you know, that's a, that's something that's interesting, but it's the sensor stuff that I think is probably no surprise that I'm not as interested in vision stuff than I am in sensors. But I think it's more interesting to be like, you know, the, the VOC sensor goes up to a certain level and you could tell that the dog has rolled in paint or some other stupid example. I can't come up with right now. I don't know, but like, uh, uh, yeah.

**Dave Jones:** Yeah. To me, no, this is just old school pattern matching and envelope matching, you know, but

**Chris Gammell:** it's not a human doing it. It's a computer doing it.

**Dave Jones:** It's a bloody computer doing it. All right. Yeah.

**Chris Gammell:** All right. Great. Next. Yeah. Uh, how about Andy? Andy's back in the, you know, in terms of the, uh, to go from boring sensors to exciting fuses.

**Dave Jones:** Better known as photonic induction.

**Chris Gammell:** That's right. He's, he's back and he's blowing some shit up.

**Dave Jones:** How long has it been? Like four years or something. And from a YouTuber's point of view, it's just amazing how the, the algorithm trademark, um, didn't give a rat's ass. He's first, he's like his second video. Well, his first real video before a, Hey, I'm back. Uh, video. Here's why it got late. Well, I don't know how many views it is now. Let me have a look. It was over a million last I looked. Oh, geez. It just lasted my years. Two and a half million views. Yeah. Two and a half million views. Unbelievable. For his first video back after like four years. Unbelievable. Unbelievable.

**Chris Gammell:** I mean, he's blowing up a 5,000 amp fuse, Dave. That is so cool.

**Dave Jones:** It is awesome. Yeah. It's just great.

**Chris Gammell:** He didn't really say in the video of what it's for. Did he say that? Maybe I missed it.

**Dave Jones:** Uh, he said it was surplus. Well, no, he said he obtained it surplus. So he wasn't blowing up a good one. And it, no, it's just used in one of those big industrial, like a, uh, voltage transmission.

**Chris Gammell:** Oh, okay. So it's like at that level. Okay.

**Dave Jones:** You know, like voltage transforming, you know, like maybe taking from the main, uh, supply down to a smaller one or, you know, something like that. Or it could be a major fuse in a large, uh, factory or something like that. Like a major inlet. Yeah. That's what I was wondering. If it's like, maybe it's in a smelting plant or something like that. Yeah. Yeah. Yeah. Something like that. Yeah, exactly. It's bonkers. Yeah.

**Chris Gammell:** Absolutely bonkers. Yeah.

**Dave Jones:** 5,000 amps isn't much actually depending, depending on your power. I guess at that level, you really do have to talk about power.

**Chris Gammell:** Yeah.

**Dave Jones:** 5,000 amps at one volt, right. Is like in the scheme of things, not, you know.

**Chris Gammell:** Yeah. Only five kilowatts.

**Dave Jones:** Yeah. Right. It's only five kilowatts. Right. It's not much. Right. So you can almost get that out of your wall.

**Chris Gammell:** It's just so far out of my. Yeah.

**Dave Jones:** I know. My realm of capability. It's just insane. Yeah. And just see what's inside it when he blew it apart. It's like these little. Yeah. It's like metal tabs. But huge metal tabs. Like big metal rods almost. They're all like little chunky bus bars. It's made up of these little individual bus. It's incredible. And they went flying. These little individual bus bars just went flying everywhere. So I think it worked on the principle that there wasn't. There was like a hundred of these packed inside this large thing. It's like a foot wide or something. You know. It's huge. Right. And yeah. And individual. And these little individual fuse links. Fusing quote marks. Right. They're like a metal rod. Right. A thick metal rod. Like a centimeter across or something. Centimeter diameter. And there was like a hundred of these inside. So the principle was I think that once one sort of started to pop. Then it would. There'd be more current in the others. And then there'd be sequentially pop. Yeah. Yeah. Yeah. Yeah. And fail over real quick. But oh man. That was.

**Chris Gammell:** Yeah.

**Dave Jones:** That was really something. And then he had to get a. Then he had to make up a relay. To. You know. Something that could switch the 5,000 amps. And that was like this big new pneumatic contactor. Like he just hit the button. And the big. This big ram just jammed this big metal plate against another metal plate. And it was like that's the relay contact. You know. Yeah. It was like oh man. That was. That was seriously good. So. Yeah. What a comeback. Holy crap. So. Yes. Don't call it a comeback. Absolutely fantastic. Yeah. Great to see him back. So. Hey we should try and get him on.

**Chris Gammell:** Definitely. Yeah. Yeah. Yeah. I'd love to talk to him.

**Dave Jones:** Because he. Like. Because I don't think anyone knows where. Like. He's a consultant in this field. Like he works for himself. Which was part of the problem. While he was. Why he was away. If you want to watch his video. On why. He was away for all that time. But yeah. I. You know. I do believe. Like he works in this industry. Like it's. You know. He's a consultant for the industry. Or something like that. You know. He's a gun for hire. Or something. So yeah. Because you don't play around with this stuff. Without. You know. Having a background in that field. You're just. Gonna. Yeah. You're. Just gonna kill yourself.

**Chris Gammell:** You mean they're not gonna hire me. Is someone who's afraid of five kilowatts. That I can hire to. To handle. You know. Ten megawatts or whatever.

**Dave Jones:** For. For me. Anything over 12 volts DC. Nah. Nah. Don't bother. It's like. Yep. Yep. Don't know about it. Yep.

**Speaker ?:** Yep.

**Dave Jones:** Oh boy. Yeah. It's amazing. I've never got around to doing the video. Of. Story of my life. Never got. After. After like. 2000 videos. I never got around to doing the video about. Showing how much energy there is. In like a double A. Or a triple A battery.

**Chris Gammell:** That's a good one. I like it.

**Dave Jones:** People don't realize. It's like. It's. You know. You short out a double A. Or triple A battery. And like. Yeah. Okay. The wire gets a bit warm. And it's gonna. Yeah. No. But it's. But it's internal ESR. Is going to limit that. Right. That's right. It's going to limit the current. And everything. Sure. You get a couple of amps.

**Chris Gammell:** It's like a power versus an energy thing. Right. It's like. It's an energy thing.

**Dave Jones:** So that's why I said how much energy is in a battery. Yeah. Right. Right. So much. So what I was going to do. Is to take. Even. Even a tiny little triple A cell. Or a four A cell. Or something like that. I was going to like. Extract all of that energy. Into a super capacitor. And then weld. With it.

**Chris Gammell:** Right. And then weld. Oh yeah. Yeah. Like.

**Dave Jones:** You know. Actually weld something. Like spot weld.

**Chris Gammell:** Weld one spot. Yeah. Yeah.

**Dave Jones:** Yeah. And like. Everyone knows. Welding like that. Requires a huge amount of. Power. Right. Requires a huge. Yes. You can get that. Because you've. You've taken the energy. From a. High ESR device. Into an incredibly low ESR device. That can then deliver that energy. You know. In huge amounts of power. Yeah. Right. Because it's got. Naf all ESR. So. Equivalent series resistance. For those playing along at home.

**Chris Gammell:** Hey man. No time like the present. Time to. Do you know how to weld? I don't actually know how to weld. I should probably learn. No.

**Dave Jones:** I don't. No. No. I'm hopeless at it. I was. I was on the verge of buying a. Tab welder. For like batteries and stuff. Because I've. I've got sitting here. A bunch of model three. Batteries. A bunch of Tesla model three. Batteries. So.

**Chris Gammell:** Oh man. Yeah. Dave. You're. Really worried. That I'm going to get a call someday. And be like. Chris. We need. Dave. Dave. Listed you as the. Executive. Of his estate. You have to clean out. All the data sheets. Yeah. Old monitors. From his lab. You know. I'm like. Oh God. I'm going to fly to Australia. And just. Put all the stuff back in the next room.

**Speaker ?:** Yeah.

**Chris Gammell:** I'm calling you a hoarder. If you couldn't tell. Okay. Yeah. I know. I know. Yeah. Yeah. Yeah. Yeah. Yeah. You have a problem.

**Dave Jones:** Soon I'll have more space to hoard. I'll have more. Oh my God. Yeah. I bought another space. It's the best thing you need. Oh my gosh. No it's not. It's the best thing I need.

**Chris Gammell:** It's the last thing you need. No. Sure. It is a. It is a. It is. Junk for you is like a. It's like a liquid. It fills up the volume of space that you give it. You know.

**Dave Jones:** You never saw my storage bunker when you were over here. Did you?

**Chris Gammell:** No. I did. I did. I went down and saw it.

**Dave Jones:** Oh you did? Did you? Yeah. Oh.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh.

**Chris Gammell:** It was full of crap.

**Dave Jones:** Can't remember that. Okay.

**Chris Gammell:** Also you show it on video all the time. I've seen it. Like I know what it looks like. Marie Kondo that shit. You know. Does it bring you joy? No. It doesn't. Yes. It brings me joy.

**Dave Jones:** Knowing that I have it all. No.

**Chris Gammell:** It brings you anger and like you know problems with computers. You know.

**Dave Jones:** Do you know how much work it takes to get rid of all that shit?

**Chris Gammell:** Yeah. I do because you do the opposite of it. Bringing it into your place.

**Dave Jones:** But that's the enjoyable part is bringing it in.

**Chris Gammell:** Oh my gosh. You just need to have. Oh jeez.

**Dave Jones:** Oh boy.

**Chris Gammell:** You need a dumpster and like some other poor sucker. To walk by. To pull stuff out of that dumpster.

**Dave Jones:** All right. We're overall amp hour. But do you have an update on your. Are you currently homeless? Are you homeless in North Carolina?

**Chris Gammell:** I have a home under contract in North Carolina. So. Fingers crossed. I. Oh by the way. I need to borrow. Borrow some money.

**Dave Jones:** Oh okay. Right. No worries. The bank of Dave will. That's right. Yeah. Yeah. Do you a loan at 5%. All right. Yeah. That's right. Oh God. 5%. That's cheap isn't it? When I was a boy. It was 17%.

**Chris Gammell:** That's right. That's right. No. I can remember getting 15% interest on my cash.

**Speaker ?:** 2.7% baby.

**Chris Gammell:** 2.7% man. That's. That's why. That's why. That's why you're. That's why your savings accounts get 0.3% interest in the US. Friend of mine.

**Dave Jones:** Just their home loan was just. They just locked in four years at 1.9%.

**Chris Gammell:** That's bonkers. Yeah. Four years. Yeah. It's actually gone up. Four years. Yeah. Yeah. It's gone up now.

**Dave Jones:** Yeah. So I think they actually called the bottom like within a week or something. And then it just instantly like it actually went up a week later and then it's gone up a couple of times since.

**Chris Gammell:** Well, I will have more questions about setting up labs from scratch. Yep. How to find the best dumpster in the neighborhood, of course. Yes. To pull crap out of. And, you know, how to, you know, how to, how to, how to socialize amongst a group of new nerds, because that's what I, that's what I think of you for.

**Dave Jones:** Well, I am. Yes. And I think you have to, because I've seen the place you bought. It's very nice, but it does not have a dedicated lab garage space.

**Chris Gammell:** Not a, not a garage space. No, there's a. No, it doesn't have a. That will become my lab.

**Dave Jones:** A bonus room. Okay. That's. That's right. Yeah. Cause it was advertised as like an X bedroom and it had X plus one, didn't it?

**Chris Gammell:** It did. Yep.

**Dave Jones:** Yeah.

**Chris Gammell:** Cool. Yep. Yeah. Yeah. X bedroom plus lab. That's, that's how they're going to, that's how they're going to sell it next time. Right.

**Dave Jones:** Boy. Anyway. So when, when, when do you move? When, when do you finally like, like drive out of Chicago and never look back?

**Chris Gammell:** Probably mid August. Right. You know, the, the, the temperate part of, of the, of the summer. Okay. Yep. I'll be moving South. Yep. I will have more updates on the lab soon. Sweet. Excellent. Catch you next time.
