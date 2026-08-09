---
episode: 36
title: Big Business Buffoonery
url: https://theamphour.com/the-amp-hour-36-big-business-buffoonery/
---

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life. Life, life, life, life, life, life, life, life.

**Dave Jones:** Oh, God, he's got special effects, people. Be afraid. Be very afraid.

**Chris Gammell:** So much fun. I love it. I'll try not to abuse the privilege. Well, I routed the... So I was playing with my drums this weekend, and I love putting drums through effects pedals. So I routed the soundboard I have and all the microphones, including my podcasting mic, through this so I can do a lot of fun stuff on here. Very annoying stuff, you know?

**Dave Jones:** Yeah. Great. We've got an hour of that, folks.

**Chris Gammell:** Yeah, that's right. No, I'm sure people will very quickly tire of it. So I'll take it easy. I'll throw it in when people are just about to nod off.

**Dave Jones:** Right, okay. Cool. I still cannot get the hang of this microphone stand I've got. I've got it hanging in front of me. I'm dual monitored today. I've stepped into the 90s, and I'm using dual monitors. Yeah. And, yeah, unless I have them off to the side there, like the mic just gets in the way with this huge round pop filter on it. Yeah. I can't see the damn... Well, I can see the screens through the pop filter, but it's pretty darn hard to read when you're reading through, you know, two layers of mesh material.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway. Yep.

**Chris Gammell:** So...

**Dave Jones:** Won't complain.

**Chris Gammell:** We're all set to go, though. And we don't have a guest this week. I mean, it's pretty obvious. No, no. They're not hiding in the wings or anything.

**Dave Jones:** No.

**Chris Gammell:** But...

**Dave Jones:** No, we won't. But it was a big success last week. So thank you, Jerry. I know she listens. She listens every week. And, yeah, that was great. And all the feedback was very positive. Yeah. So we will no doubt have more guests.

**Chris Gammell:** Yeah. I like that. I like the fact that we can, you know, kind of go on and off, too. That's, you know, because then, you know, you and I can have the regular conversation and not have to entertain people. You know what I mean?

**Dave Jones:** Yada, yada, yada. Yada, yada.

**Chris Gammell:** Now it's just back to us and the listeners. And we're good, right? It's like when someone comes over to your house, you know, like you have to clean and you have to do all this other stuff. Oh, yeah.

**Dave Jones:** No, that's... Yeah. All right.

**Chris Gammell:** Yeah.

**Dave Jones:** We have a list and we're not afraid to use it.

**Chris Gammell:** That's right. We are not.

**Dave Jones:** There's no way we are getting through 36 items in today's list.

**Chris Gammell:** Only 36. And some of those are old, so...

**Dave Jones:** Well, yeah, probably half of them are old, right? Yeah. I don't know.

**Chris Gammell:** Yeah.

**Dave Jones:** Go figure.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** We normally start with shout-outs. Do we have any?

**Chris Gammell:** Yes, we do.

**Dave Jones:** Oh. Okay. Yeah. They're in the list somewhere. Yeah. I moved them off to the top. There we go. Yeah. Yeah. Yeah. Oh, wow. He's sorted.

**Chris Gammell:** I did. All right. Yeah. So, first up is Mike Cowgill. And he's actually... Hey, Mike. I didn't see his first build, but he's actually building an LCR meter now. And he's just starting that back up now. And it looked like a really cool build. So, he's kind of doing... I think he's open sourcing it, too. He had done RF vector network analyzer previously. But it looked like a really cool project. So, I'll look forward to keeping an eye on that.

**Dave Jones:** Yeah. I've had a look at it, and it's awesome. He's up to part one. And he started out using the new... Well, I don't know if it's new. It's probably been around a while. But the analog device is AD5933, which is an impedance converter, a 12-bit impedance converter. And it's pretty much designed for exactly this purpose. And it's a really neat special function chip. Yeah. So, yeah. But he found a few limitations with it. So, he decided to bugger that. I'll just roll my own. So, I think he's going to roll his own.

**Chris Gammell:** Well, not his own chip, but his own solution. No.

**Dave Jones:** His own solution. Yeah.

**Chris Gammell:** Yeah. It looks really cool, though. So, people should check it out. He's got some good block diagrams about what he's planning. And we'll link to that, too.

**Dave Jones:** Yep. And I like it how he's using a trans-impedance amp instead of the regular... Sorry. A trans-conductance amp instead of the regular sense resistor. So, there's no burden voltage when you... Because normally, you've got to measure to... Do an LCR meter. You've got to measure the voltage and the current and the phases on those as well. And with those, you can calculate everything. Yeah. And, yeah. So, he's using a... Yeah. There's not much to it. You just whack a sine wave through your device under... Well, there's a lot to it, but... No, but in theory, it's pretty... Oh, I know. In theory, yeah. The block diagram's pretty... You know, put a sine wave into your device under test, you measure the voltage and the current. Ta-da! Yep.

**Chris Gammell:** Well, you've got to measure some other things, like how much the shift is and stuff, but how much the phase shift.

**Dave Jones:** Oh, yeah, but that's all done in software. So, you capture the phase of the voltage and the... You know. Yeah, it's easy, man.

**Chris Gammell:** Just throw it over the wall, right, Dave? That's right. Yeah.

**Dave Jones:** Nice. Anyway.

**Chris Gammell:** So, it looks like a cool... Look, definitely a cool project, and we'll keep an eye on that. Yeah.

**Dave Jones:** Absolutely. And then he decided to go high-end, and he's talking about, like, 400 meg sample DDS chips and all sorts of stuff. I don't know. I think he's gilding the lily a tad. I think he might be going to town.

**Chris Gammell:** Oh, gilding the lily. That's right. I like that phrase. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah, I guess you can always... I mean, it's nice when you have pin-compatible, too. I don't know if those chips are pin-compatible, but when you have that, and then you can always downgrade later if you're sick of paying too much for it.

**Dave Jones:** Right. Yeah. And if people out there don't know the term gilding the lily, it is quite an old one. It's a very old term, and it basically means applying... It comes from applying gold leafing to something. You know? So, you're gold-plating it. You're going above and beyond what it... You know? What that product deserves or what you should do. Right. You're just...

**Chris Gammell:** Usually with the implication that it's covering your butt in case you don't have the specs in somewhere else, right? So, in case...

**Dave Jones:** Or... Yeah, that. Or you're just making it look fancy or... Oh, okay. Or... You know? You're just... Yeah. You're just doing it because you can. Ah, gotcha. Yeah.

**Chris Gammell:** A little extra change in the pocket. So, that's gilding the lily. Right. Another shout-out we got. Adam Ward. He took up our idea, I think, from episode 10, I think it was. Man, that's a while ago now. Ah, dude. I have no idea. Yeah. Come on. Yeah. But he started up a new blog and put a picture on there, and we always like that. So, thank you, Adam. And... Yes. And nice looking site to start with. So, he's going to capture some of his projects there. That's good. Awesome.

**Dave Jones:** No, it's a great way to document your projects. You know, why just do them? Why not just, you know, go that little extra step and put the info out there? Yeah.

**Chris Gammell:** I agree.

**Dave Jones:** It's great. It's got so many benefits.

**Chris Gammell:** Yes.

**Dave Jones:** It's huge. All right. We wanted to rant about... Let's get into the rants.

**Chris Gammell:** We got, what, six there?

**Dave Jones:** Is there rant with a reverb effect?

**Chris Gammell:** Oh, let's see.

**Dave Jones:** This is a rant. And that was live. From a church. Right. Thankfully, it's on the your end. Rant, rant, rant, rant, rant.

**Chris Gammell:** Oh, yeah. Yeah.

**Dave Jones:** Anyway. Yeah. We both saw this, actually. But you added it to the list first. So, you've got dibs, I guess.

**Chris Gammell:** Which one?

**Dave Jones:** The Engineering Mind.

**Chris Gammell:** Oh, yeah. Good Friends National Instruments. That's a shame. You know, like, that's... So, that was Todd Sear. Yeah. Yeah. And he was the engineering... An engineering mind for NI. And they just... I mean, he moved jobs and asked if he could take the brand with him. And they said, no. We own that. Blah, blah, blah. You know, probably people duping it out there. Yep. And now it's just sitting there. They're not doing anything. I mean, like, even if they just made videos. I don't care who does it now. Like, you know, Todd did some cool videos. But I can't believe they're just letting it sit there.

**Dave Jones:** Well, it's dead. I actually went to the site. And it's like a shutdown domain. They've killed it. It's like, there it is. Bluehost. Affordable web hosting. There's that nice looking chick on the front with the... You know? With the stock image of the... Yeah. I have no idea why. Anyway. Yeah. Yeah. Welcome to anengineeringmind.com. It's for sale, I guess.

**Chris Gammell:** Yeah, they're not doing anything with it at all. So, it's a darn shame.

**Dave Jones:** Oh, that's just... That's pathetic. Really. And, yeah. And I do know that we'll have to get him on and let him explain, you know. Because I think it would be an interesting story. Yeah. I don't know whose idea it originally was. But if you haven't seen it, An Engineering Mind was like a video blog style thing. Where Todd sits in his cubicle at work and he just, you know, rants on about stuff. And he does like a funny little skit. And they were very well written. Very clever. Yeah. Yeah. Yeah. And I thoroughly enjoyed it.

**Chris Gammell:** I mean, you said that was your only competition for a while too, right?

**Dave Jones:** That was pretty much my only competition. Because Jerry was still doing... I think she was still doing the... Yeah. The Circuit Man and Fat Girl at that stage.

**Dave Jones:** And it wasn't really a video blog. Now she's gotten into YouTube. She's my competition. Oh, yeah. Yeah. Anyway. Yeah. And Todd was my only opposition, I thought, at that time. And, yeah. But I thoroughly enjoyed his show. I thought it was awesome. It was a different style. You know, it wasn't... You know, there weren't tutorials or reviews. It was just like a funny little skit. Yeah, it was entertainment, basically. Kind of. It was entertainment. Yeah. Engineering entertainment. And I loved it.

**Chris Gammell:** Yeah.

**Dave Jones:** And I just pissed it away. What are you doing? Oh. It's too bad. Can't get over these big companies. They just have no clue at all.

**Chris Gammell:** Yeah.

**Dave Jones:** It's too bad. And he had like a couple of thousand, a couple of thousand, you know, not listeners, viewers. The subscribers or something? Subscribers, yeah. Yeah. And it was going well. Oh, boy. And they pissed it away. Anyway, as far as I'm aware, Todd wanted to take it with him. He even offered to, you know, look, I'll keep you guys as a sponsor. You can approve the scripts and everything. And, you know, they said, no, piss off, basically.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Anyway, the joys of doing something for your company. Yes. Or that involves your company. Yeah.

**Chris Gammell:** Yeah. You know, the question I always wonder about, too, is like, well, when does it become... If it was just Todd doing it, right? Or say it's just you doing it for a company. Yep. Like, do they own your name? Like, do they own your face? Like, do they, you know what I mean?

**Dave Jones:** Well, no, of course they don't.

**Chris Gammell:** I mean, but... Unless there's something in writing.

**Dave Jones:** Yeah, well, maybe. If you didn't sign anything and you registered the domain name, I mean... No, I know, but I'm saying, like, so say... He who holds the domain name rules, you know? Right. No, no, I know.

**Chris Gammell:** But, like, say John Smith starts working at... I don't know. Yeah, right. National Semiconductor, something like that, right? And they want him to start doing videos. And he starts doing videos under John Smith, right? Yep. And then he leaves. And he says, well, I want to start blogging or doing videos or, you know, doing other stuff. Tough shit. Yeah, right? Is it like...

**Dave Jones:** Yeah, no. It's... Seriously, it's tough shit. It's like I can trade under the name David Jones, right? There's a huge department store in Australia. They own the trademark, I think, you know, David Jones. But I'm legally allowed to form a company that's named... Well, to trade under my own name. Oh, okay. Because my own name is David Jones. So, I can trade under that. And they can't stop me.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, they do not own that brand if it's your name. So, yeah. And even if you thought up the name and you registered the domain name and you were, you know, doing that, but your company was effectively paying for it, well, that's tough tits to them. You can continue to do it.

**Chris Gammell:** Yeah.

**Dave Jones:** So, yeah. They'd probably try and shut you down, but then you just tell them to stick it up their ass and that's it. End of that. Yep. All right. Absolutely. That's my advice for today. Tell everyone to stick it up their ass. That's the Australian way.

**Chris Gammell:** All right. So, we've talked about people going into marketing and stuff like that, but what about finance? We have nothing on here about finance.

**Dave Jones:** Yeah, you added that this morning. Yeah, I did. Rant away. Go on.

**Chris Gammell:** Well, there's a TechCrunch article about people... Not people. Not people. Come on. We're not people. So, engineers going into finance. You know, this was a big thing probably started, you know, 10 years ago.

**Dave Jones:** Oh, it was the 80s, wasn't it? 80s even? I don't know. Big finance. End of the 80s was the big, you know, everyone wanted to get onto the stock market and work as a trader and that was like the big, you know, when was that? When was the movie Wall Street out? Was that?

**Chris Gammell:** That was 80s, yeah.

**Dave Jones:** Late 80s? Yeah. Yeah, that was the start of the rot.

**Chris Gammell:** Ugh. Yeah. Yeah. Yeah. So, anyways, a lot of, you know, engineering students, they become quants as they're called where they go to, you know, hedge funds or whatever and they work on algorithms that trade for you basically. And, you know, they made a buttload of money. That's basically the idea of it. But now it's starting to trend back the other way except not so much really. So, that's kind of my rant is I can't believe people are still doing this stuff. I mean, I know there's money in it but like seriously, if you're an engineer and you're going to do this stuff, I really hope you lose your job. That's all it comes down to. I know that sounds kind of rough but I was laughing my ass off when those guys started getting laid off. Like people with like legit engineering talent who squandered it because that is squandering it. You're not doing anything useful for the world. You're pushing paper. You're not creating value. I'm sorry. So, that's my rant about that. I don't know.

**Dave Jones:** I don't necessarily disagree.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah? All right.

**Chris Gammell:** But they're talking about how it's becoming sexy again to get back into engineering and Oh, great. Oh, okay. Engineering. Yeah. Yeah. And engineering. And that's good, right? You know, when the dip came around. Absolutely. You know, but not the dip even, the recession. When the recession started, you know, these guys couldn't find jobs, guys and girls couldn't find jobs being traders and being, you know, working in these big funds and now they're getting back to it. You know, now the market's coming back, they're going back to it again. It's just like, man, you guys are, you're not helping anybody. That's the basic law. And that's the bottom line. You're not helping anybody other than yourself. Yeah.

**Dave Jones:** Not that there's anything inherently wrong with that, I guess. You know, if you want to be like that, well, you know, fine. But yeah.

**Chris Gammell:** Just don't come crawling back. That's the real thing.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Ooh. Yeah. That's right. I said it. Right.

**Dave Jones:** That's pretty mean. What? I always give someone a second chance. No, I'm sorry. No. No. Okay.

**Chris Gammell:** If you're causing a global meltdown, if you're causing a global financial meltdown, you're like, oh yeah, come on, come on and work in my business, you know, come work with me in business. Right. I want you to sit in the cubicle next to me. How is that going to happen? All right.

**Dave Jones:** Fine.

**Chris Gammell:** No second chances for me. I'm sorry.

**Dave Jones:** All right.

**Chris Gammell:** Yeah. He's mean. Yeah. I'm an a-hole. Bastard.

**Dave Jones:** Absolutely. I've got another rant. All right. It's a US rant. Uh-oh. Yep. Sorry. It's okay. I did a video. I've got a bird problem. Yeah. Out the front. Oh, yeah. All these birds are nesting in the tree. Yeah. Out the front. Right. At about 6, 7 p.m. or something for an hour or more, they just yap away. Yap, yap, yap, yap, yap. Tweet, tweet, tweet, tweet, tweet, tweet, tweet. Something like that. Well, that sort of sounds like in my garage because once it enters the garage, it just echoes around the garage and it's pretty darn close. Yeah. I was impressed there. And it's bloody annoying. And I've had to stop shooting my blogs. I just can't do it. It's just too darn loud. And of course, you know, I did a little video, a quick little video on it just to show what it's like. And I tweeted it as well. And without fail, almost every, including yourself. Including me, yeah. Christopher Gamble.

**Chris Gammell:** Yep. That's like my mom would call me, like yelling at me.

**Dave Jones:** Yes, exactly. And add your middle name as well.

**Chris Gammell:** Yeah, John. Christopher John Gamble.

**Dave Jones:** Christopher John Gamble. Christopher John Gamble. Ah! Yeah, you, even, even you came on, all the yanks came on and said, I get a gun and shoot them. Shotgun. That's, don't use a shotgun. Mike, use a freaking shotgun and shoot the bastards and, I don't know, blow them up. Do something. What is it with you yanks and guns?

**Chris Gammell:** For goodness sake. I mean, that will solve your problem, at least for now.

**Dave Jones:** That is the US solution to everything. Weapons. Yeah, I know you said that. Yeah.

**Chris Gammell:** Yeah, I know.

**Dave Jones:** Great. Anyway, and Duran.

**Chris Gammell:** We actually had that problem at my old work. We would walk in in the morning and just be, oh, super loud. And they tried, they tried shotguns without any, like, actual, like, ammunition in it. Not ammunition, but it was just the. Blanks or whatever. Yeah, it was just blanks for sound. And they'd fly away and they'd come right back. So.

**Dave Jones:** Yeah, of course.

**Chris Gammell:** Yeah.

**Dave Jones:** And of course, everyone has a shotgun over there, right? There's one, there's one, the secretary at the front desk has one.

**Chris Gammell:** A chicken in every pot, a car in every garage, a gun in every cabinet. Yeah. That's what it is, Dave. Right, yeah. Yeah. Unbelievable. Living up to our stereotype. Maybe it's just the people on Twitter. That's what it is. And YouTube. Right, okay. You know the people on YouTube are nasty, so. Oh, yeah, they're, yeah. They're just protecting themselves from other people on YouTube.

**Dave Jones:** You guys have, it's so ingrained into your culture. It's scary.

**Chris Gammell:** It really is. I know. Unbelievable. I have never fired a gun myself.

**Dave Jones:** Oh, there you go. Yeah. Wow. Yeah. You unpatriot you.

**Chris Gammell:** Yeah. Well, I'm afraid of them, so. I'm afraid. You know, I think about my problems with, like, soldering irons, how much I burn myself, and high voltage. And then I think about, like, guns. I know high voltage can kill you, but guns are a little more dangerous, like, because. Right. There's no internal resistance to bullets. Exactly. Yeah.

**Dave Jones:** Oh, dearie.

**Chris Gammell:** Yeah. Yeah. So, I'm very afraid of them, but.

**Dave Jones:** Right.

**Chris Gammell:** All right. We should switch off for hands. What do you think? Yes, please. All right. Let's go to this suggestion from Patrick. So, Patrick York wrote in about old Radio Shack magazines. There's a site called RadioShackcatalogues.com. Have you ever seen this site?

**Dave Jones:** Yeah, I've seen that. It's been around for a while. It's awesome.

**Chris Gammell:** Yeah. Yeah, it's really cool.

**Dave Jones:** Yeah, yeah, yeah. It has. And.

**Chris Gammell:** I mean, you have a lot more experience with older Radio Shack stuff than I do.

**Dave Jones:** I used to collect Radio Shack catalogues, and I cannot, well, add Tandy catalogues, as they're called here, it always. Okay. And, and I can't believe I threw them out. I collected every monthly flyer. Really? They ever had every catalog. Yeah. Yeah. Oh, and I just tossed them. And.

**Chris Gammell:** Were they different for like, did they have, were they like, were the Radio Shack catalogues like the DigiKey is today? Is that kind of, like just parts, or did they do app notes and stuff too?

**Dave Jones:** No. Well, no, they didn't do app notes. It wasn't electronics. Okay. Because they were mainly a consumer company. Yeah. Um, you know, they've always mainly been sort of, you know, they've had those, those consumer catalogues. So they've had all your audio gear and your computer gear and your hi-fi and everything else, but they did have components as well. But yeah. Yeah. Ah. Yeah.

**Chris Gammell:** It's a really cool site though. You can just click through and check them out. Yeah. There's some old ones, man. Oh man.

**Dave Jones:** I don't, I don't know if they've got the monthly flyer. Are they like just the yearly catalog? I think they might be. I haven't looked at this site for quite a long time. Are they just yearly catalogs or something? Yeah. Right. Yep. Yeah. I had the monthly flyers. Oh.

**Chris Gammell:** Although the downside is they, they use this, this stupid thing where it like looks like it's flipping the page actually. When you. Oh yeah. I know. One of those wanky. Yeah.

**Dave Jones:** Flash animation things. Yeah. I know. Yeah. This thing's great. Just give me the PDF. You know.

**Chris Gammell:** Articles about the TRS 80 system. Ooh.

**Dave Jones:** Trash 80. Yep.

**Chris Gammell:** Trash 80. Nice.

**Dave Jones:** That's what it's called. That's what, that's what it's affectionately. Oh yeah. That's what it's affectionately known as the trash 80.

**Chris Gammell:** I love it. This is. Oh, they have sound too. Why do you need sound for this? It's like, I don't know when I'm flipping the page.

**Dave Jones:** No, that's pretty pathetic. Yeah. Yeah. Just give me the.

**Chris Gammell:** Yeah. That's bad. Modern convenience when you're using a computer to flip a fake page and it is sure to rustle for you. Right.

**Speaker ?:** I don't.

**Dave Jones:** Have they like paid someone to do that site or they've done it themselves or you know. Yeah. I don't know. I guess you can get that as a plug in that wanky animation. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Just list the PDF. A text page with every. Yeah. A link to every PDF from 1920.

**Chris Gammell:** Yeah. You don't have to stare at their ads underneath then though. That's the real thing.

**Dave Jones:** Right. Well, you can put text ads on the side. That's fine. But.

**Chris Gammell:** Not if you're downloading the PDF though. That's what it really is.

**Dave Jones:** Oh yeah. Yeah. But you've got to go to the site to do that. Yeah. Yeah. You know. Text in the Google AdSense ads will be there.

**Chris Gammell:** Yeah. Man. This is great. I love looking at old advertisements. I think that's my favorite thing. Like. Like the catalog's cool. They're showing tubes. And I'm looking at the 1940s version. You know. Yeah. You can see tubes and you know. A bunch of stuff. Heat sinks. Whatever. But it's always the ads. Ads always. Because like. Advertising has changed a lot over the years. You know. Absolutely. And.

**Dave Jones:** And look. And there's a woman in every ad. You know.

**Chris Gammell:** Oh really.

**Dave Jones:** Well. Not. Not quite. But yeah. There are lots of women in these ads. Yeah. Bet your bottom dollar. Yeah. So. Which we ranted about last week. Yes we did.

**Chris Gammell:** Which we won't go back into. Right. No. We will not.

**Dave Jones:** But yeah. Oh. Looking through all. You see the progress of. Well. You know. The old ads are fun. But then you see the progress of electronics. And test gear. Yeah. And components. And all sorts of stuff. And it's just. Ah. Could spend all day on there. Just browsing. Oh yeah. It's fantastic.

**Chris Gammell:** So people should definitely check it out. It's a great site. Yep. Great site. For sure.

**Dave Jones:** What else you got on here? I can hear a dog in the background there. Oh yeah. Your dog is.

**Chris Gammell:** My pup is barking. It's gone off. Yep. Right. She goes crazy sometimes. So what's next? We should get into the discussion stuff. How about.

**Dave Jones:** Well. You. You had a thing. There was a. Thing about the Hewlett Packard open source calculator. Oh yeah. Yeah. So. This is not new. It's pretty old. No. No. It's not.

**Chris Gammell:** But Eduardo wrote in about this. Basically they open source. One of their older designs. With schematics and everything else. Well.

**Dave Jones:** It's a current. It's a current calculator.

**Chris Gammell:** Yeah.

**Dave Jones:** But they. Yeah. They decided to open source it. And. Yeah. And give you a. A developing kit for it. And the schematics. And you know. Yeah. Everything. It's. It's great. They open source their calculator. And there's a JTAG. They build a JTAG header into it. So you can just. You know. Yeah. Hook it up and. You know. And they. They'll sell you a little programming cable. That you can. Hook up and hack the thing. And. Yeah. It's just great. Yeah. Display. And I. I actually talked about this design. Back in. My. Fifth. Blog. Or fourth. Or fifth. Blog. Oh. It's that old. That's. It's. It's that old. Yeah. Exactly. And. Yeah. They. They use an Atmel arm. Processor. But unfortunately. Let's get into some electronics here. Yeah. They use it at. Yeah. Go figure. Right. They use an Atmel processor. But they. Clock it at 30 megahertz. And this is what I done. This is what I did my blog on. And you can look it up. And I do. Yeah. Yeah. And do all sorts of things. Yeah. But. They. Which. At the time surprised me. I thought. What the hell do you need. To run. Your processor at 30 megahertz. On a simple. Financial calculator for. I thought that was just nuts. And then I looked into the details. Of it. And. It's powered from. Two 2032. CR 2032. Coin cell batteries. Right. And they have a quite high. Internal resistance. Of about 10 ohms. Each. Or something. So that's about five. And they put them in parallel. So that's about five ohms. Internal resistance. When they're fresh. And of course. That ramps up. Yeah. You know. It's a curve that ramps up. With. As the battery. Ages. And every time. You take. You know. What they did. As soon as you. Actually hit a key. On the keyboard. The actual processor. Would power up. Run at 30 megahertz. Process it. And then shut back down. And. Which. Which. People all said. That. Oh. That's. That's fine. Because it draws. The same amount of power. Whether you do the processing. Instruction. In. You know. One. Microsecond. Or you do it in. You know. Whether you do it in 100 microseconds. At a slower speed.

**Chris Gammell:** Uh huh.

**Dave Jones:** And I went. No. It's not. You're not looking at the details. Right. And the detail is that. ESR. That battery. Every time. You take a gulp of current. From. That. You're going to have a loss. In the ESR. Of your battery. So it's not beneficial. To. To. Do. Faster processing. In a shorter time. Uh huh. It's actually. More. Power efficient. To do slower processing. Over a longer period of time. And then you don't waste that power. In your. The ESR. Of your battery. And I think I did the calc. And it started out like. 5%. Or something. Was the. Would be the loss. So each calculation. They were pissing away. My favorite term. Pissing away. 5% of their. You know. 5% of the power. Just due to the ESR. And once. Once the batteries start age. That just gets worse and worse. And you know. It goes up to. You know. 30. 40% or something. Or 30% or something. At the end. Of the battery life. It's just bad. It's just poor design. Yeah. What about the.

**Chris Gammell:** What about the transient power equation too? Like. When you're. Looking at like. Switching of transistors. Did you work that in too?

**Dave Jones:** Well. No. See. That's the thing. Everyone was arguing. Is that. Technically. If you just power the chip.

**Chris Gammell:** Yeah.

**Dave Jones:** It. It really. Because it's a CMOS chip. It uses the same amount of power. Effectively. Very minor differences. Okay. But you know. Don't. Don't include them. Essentially. It makes no difference. Whether you. Process something. In one. Microsecond. At 10 megahertz. Or 10 microseconds. At one meg. It uses the same amount of power. Ta-da. But. When you power it from batteries.

**Chris Gammell:** Yeah.

**Dave Jones:** No. It doesn't. You. Lose power in the ESR of your batteries. Or the ESR of anything else. That you're powering it with. So. And then you've got. Complicated stuff. Like bypass capacitors. And things like that. But. Yeah. That current's got to come from somewhere. Right. So. Right. Right. So it's. You know. You are pissing away that power. Okay. So it's poor design. And Cyril. You mentioned in the notes here. Cyril's the guy who actually designed their calculator. In fact. Cyril is pretty much the entire Hewlett-Packard calculator division. Oh. Actually. Okay. There's Cyril and one other guy. As far as I know. Oh.

**Chris Gammell:** Cyril's a name? I thought that was a person. Or a place rather. No. No. No. Or a division.

**Dave Jones:** He's French. He's. Yeah. Yes. No.

**Chris Gammell:** That's quite a.

**Dave Jones:** Oh. I see the notes. It's a developer. In a division called Cyril. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. No. Cyril D. I won't get his last name right. Cyril DeBrucen. Okay. I think is his last name. But yeah. He's one of two guys in the entire Hewlett-Packard calculator division. They've pruned back just a tad. Yeah. On staff. Yeah. Right. You know. Since their heyday of their Hewlett-Packard calculator. Yeah. Division when the was worked there.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. They're now down to two I believe. Anyway. But maybe there's a manager in there as well.

**Chris Gammell:** There's got to be a diminishing return. I mean like calculators. I mean like you know it's kind of getting pushed off. Yeah. Exactly.

**Dave Jones:** Well and they're all made by a company called a Kinpo. Okay. Anyway. Kinpo in China. Oh. Okay. Yeah. Big shock. Yeah. Big surprise. They're actually made in China. But yeah. Yeah. But they still do develop them in the US there. And yeah. They just subcontract out the manufacturer of them. And even some of the source code I believe. So. Which is a bit of a shame. But anyway. Yeah. He saw my video and admitted that yeah. Probably wasn't the best design decision. And he would look at fixing that in the next design. Which I don't think he did. So.

**Chris Gammell:** So the basis behind your calculation was that like. P equals I squared R. That's what you're talking about. So the higher.

**Dave Jones:** The I squared R loss. Yep. There's the I squared R loss you've got to consider in the battery.

**Chris Gammell:** So does that actually manifest as heat then? Through the battery. That manifests as heat.

**Dave Jones:** Yep. That manifests as power wasted. That stinks. Yep.

**Chris Gammell:** What you're going to do is.

**Dave Jones:** And it starts out at 5%. Which is quite low. You know. But when you're designing a calculator. Which is the. Yeah. That seems to last forever. Almost the ultimate low power. One of the ultimate low power devices. Right. And considering some of HP's old. You know. The Voyager series calculators had 20 year battery lives. Right. Crazy. You know. This is a tad disappointing. So. Yeah. Well. Yeah. That's okay. Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** And. Yeah. And he tried to argue that the ESR was much lower than the data sheet. And I went bullshit. Well. It was possible.

**Chris Gammell:** But. Yeah. But. Goes up over time.

**Dave Jones:** No. You've got to work from the data sheet. Yeah. Specs. And he couldn't produce data to prove it. Yeah. And he finally admitted that. Anyway.

**Chris Gammell:** Yeah. That's an interesting point you mentioned about working from the data sheet. Data sheet. I call them data sheets. It's like. You know. You can go off data sheet. Right. I mean. Like a lot of times you will be able to find parts that are way better than what the data sheet says. But. Yeah. And this is something I've seen before. Like. When you go back to the manufacturer. You say. Hey. It used to be. You know. Like. It used to be 10 ohms internal resistance. And now it's. Right. Now it's 20 when it comes to me. And they're like. Well. We spec'd 100.

**Dave Jones:** Because they've changed the diet. Yeah. Right. Okay. Right. Yeah. I mean. But if it's still in there.

**Chris Gammell:** They're going to just say. Well. Guess you should have listened to us the first time.

**Dave Jones:** Exactly. You should have. You don't rely on.

**Chris Gammell:** I know.

**Dave Jones:** Measured. Typical. Figures. Because it. You know. They're not guaranteed.

**Chris Gammell:** Yep.

**Dave Jones:** So. Well. And my current video. Is. I've got a blog for everything it seems. I guess so. My current video shows exactly that. The LM3. The classic LM317. Yeah. Right. I thought I'd get a bit better. A bit better dropout voltage than what I got. Yeah. I was hoping for a bit better than data sheet. But then I went through and measured it. And you can see it on the video. That no. It exactly. Almost exactly meets the data sheet. Yep. Load graph. And. Oh. Bummer. Yeah. You know. Yeah. And that comes down to. Can't you give me.

**Chris Gammell:** That's like a process engineering thing too. Because it's like. If you're. If you're a process engineering. Is good. Engineering is good enough. Right. And it's getting out the door. You're still making money on it. And so. There's no. There's no. There's no added bonus to. To make it any better. You know. And. And the other side of it too. Is sometimes people. Are relying on. On what you expected not to find. Right. So. What was. What did the dropout voltage end up being.

**Dave Jones:** It was 1.5 volts at 20 milliamps. Right. And so some. Which increases to 1.7 at 200.

**Chris Gammell:** Right. And so some designers. Are actually designed with that in mind. Right. So it's always. You're never going to make anyone happy. Absolutely.

**Dave Jones:** No. Well. No. Exactly. But. Yeah. I. Let that be a lesson to you kiddies.

**Chris Gammell:** Yeah.

**Dave Jones:** Never use typical figures from a data sheet. Yeah. Well. Do. Do so at your own peril. Be sure to test as well.

**Chris Gammell:** Testing is important.

**Dave Jones:** Yeah. Don't assume. Yeah. Number one rule of electronics. Don't assume. Measure.

**Chris Gammell:** Mm-hmm. Mm-hmm.

**Dave Jones:** Mm-hmm. Catch you every time. Yes. Murphy's a bitch. Anyway. That's enough Hewlett-Packard calculator ranting. If you didn't know I'm sort of into calculators. Yeah.

**Chris Gammell:** Yeah. We've heard.

**Dave Jones:** I'm a bit of a calculator nerd. Yeah.

**Chris Gammell:** Well. And related to that. We actually. So we had talked before about the. The Agilent phone calculator. How they have an app for that. Right.

**Dave Jones:** Oh yeah. That's right.

**Chris Gammell:** Right. And back. Actually on. Electronic Stack Exchange. I was. I was browsing that. And I saw someone. Talking about. Wolfram Alpha. There's actually a really cool. Yes. Conversion engine. Built right into. Wolfram Alpha.

**Dave Jones:** Well. It does everything. Doesn't it? Oh yeah. Yeah. Like a.

**Chris Gammell:** It's an answers engine. That's what they call it.

**Dave Jones:** It's a be all end all tool. Oh right. An answers engine. That's the wank.

**Chris Gammell:** I haven't used it in a while. You know. There's always the gimmicky stuff.

**Dave Jones:** Oh when it first came out. Yeah. I typed a few things into it. Oh yeah. That's kind of cool. And other things didn't work. And it's like. Eh. Whatever.

**Chris Gammell:** Yeah. So. It was. Endolith. On. On. On. Electronic Stack Exchange. And. And he just typed in. 0.02 milliamps. Eight years to. Milliamp hours. And it just. It craps out this whole long page. Of all the conversions you could possibly want. Oh. Awesome. It's awesome. It's really cool. Right. So it's. It's nice to have. Yeah. I don't know if it's. Yeah. So let's see. 0.2. 0.02 milliamps. For eight years. And that's actually. I think they were doing like a calculator type. Conversion as well. Right.

**Speaker ?:** So.

**Chris Gammell:** So. For like. Long term power. And it just says. 1400 milliamp hours. That's the answer. And then it also goes into. Kilocoulombs. And megacoulombs. And coulombs. And everything else. Fantastic. And then even. They do it as a comparison. To Kindle battery capacity. That's crazy. Oh really. Yeah. Wow. Yeah. Okay. They actually give you a real life example. Yeah. Comparisons as battery capacity. They say. One half of a typical double A battery. 0.92 of a Kindle battery. And it's about equal to an iPhone. That's awesome.

**Dave Jones:** That's pretty good. Yeah. That's. Yeah.

**Chris Gammell:** Yeah. So. Oh boy. Nice job Stephen Wolfe. From. We approve.

**Dave Jones:** And if you go to volume. Will they give you. You know. It's twice the volume of Sydney Harbour. And it's. Oh yeah. I'm sure. Five football stadiums worth it.

**Chris Gammell:** I haven't tried that one.

**Speaker ?:** Right.

**Chris Gammell:** Yeah.

**Dave Jones:** What is a standard sized football stadium anyway.

**Chris Gammell:** Well. What kind of football are we talking about. We're talking about.

**Dave Jones:** Well. That's right.

**Speaker ?:** That's right.

**Dave Jones:** That's right. We're talking about your crap gridiron thing. Yeah. Right. That big sissy game with the pads. Oh yeah. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Us and our teeth. Right. And our non cauliflower ears. Oh dear. Yeah. Yeah. Bunch of pussies. Oh well. And I'll play it anyways.

**Dave Jones:** What else have we got. Well we should probably get a few things that have been on here for a while. I guess so. Agilent. Agilent released. You know. I did the review of the Agilent scopes. They came out to a big fanfare.

**Chris Gammell:** Yeah.

**Dave Jones:** You know. Some time back. And Haymeg at almost the same time released their new series of scopes. And you know. It got me thinking. Is this a coincidence. Do these companies know that. Yeah. What the other company's doing. I mean. Yeah. You work at. As someone who shall remain nameless. But. Do you guys hear about your competitors. Well I also work at a company who. Well everyone works at a company who has competitors. Right. I guess. Is it. You know. Common knowledge inside companies to know what the others are doing. In terms of product releases and. Stuff like that. You know.

**Chris Gammell:** I don't know. I heard about the Agilent thing just with. I heard about it with. Just regular marketing material. So. I don't know. I wonder about that. Right. Because there's. There's always stories throughout history about like. You know. Patenting too. Like how patents seem to always come around at the same time.

**Dave Jones:** Exactly. You know. They. They actually arrive at the office on patent office on the same day. Like within hours.

**Chris Gammell:** And. Yeah. Exactly. It's weird. It's weird. I mean like. I don't know if that. It's just got to be the right time for a lot of things like that. You know. Like. I mean. You think about it too with. Like. Especially with like electronics. There's only. Unless you're out there making your own chips. Which we can talk about later if you want Dave. Please do. Oh yeah. Because you're wrong. Oh yeah. Unless you're out there like making your own stuff. If you're using stuff that's off the shelf. Right. So tomorrow. Yeah. Analog devices makes a new part. Right. And analog devices. 12 million. Whatever they're calling their. Their AD 12 million. And. You have. There. There's only. There. There are some practical limits to how soon you can get these really nice new parts worked into designs. And you know. Yeah. Even. You know. A lot of those chip vendors will give you early previews. But even if you're the one of the first person. One of the first companies to use it. That means everybody else is using it at the same time too. So. You got to imagine people are watching the same specs on new parts.

**Chris Gammell:** And that's kind of. What leads to. A lot of the same. Products having similar specs on the. On the flip side.

**Dave Jones:** Yeah. But. But. Because these. These products have such a long development time frame. I mean. You know. How long does it take to actually develop a scope. You know. One of those high end scopes. Right. Yeah. That's true. Or. Or. Even a chip. You know. It. It takes. It takes time to. Actually design and lay these things out. And test them. And actually get the first samples out there.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And. Yet. Companies seem to. Come out with stuff at the same time.

**Chris Gammell:** Yeah. I don't know. Yeah. And maybe it's a market driven thing too. Maybe it's because everybody's asking for. You know. If they have. 20 gigahertz scope now. They're going to say. I need a 25 gigahertz scope next year. Right. And. And they. They get asked the same question by every vendor. And maybe that's why.

**Dave Jones:** And. They seem to come out with the same. Specs. Like all these new scopes have serial decoding built in. And they have upgradable bandwidth. And they have. Yeah. Yeah. You know. There's lots of similarities. Yeah. Between these. Yeah. Scopes. And it's just. Yeah. You just got to wonder what's going on there. Yeah. I really.

**Chris Gammell:** I really like that serial decode thing. I always. Yeah. Yeah. You ever. You ever sit there on a scope. And try and count the up down. And do the. And do the. Oh yeah. The division. You're like.

**Dave Jones:** Everyone's done that. You know. I'm going to go with that's a C. Yeah. Exactly.

**Chris Gammell:** That one's E. I guess. Oh. Yeah.

**Dave Jones:** Serial decodes worth its weight in gold.

**Chris Gammell:** Oh yeah. It's nice. It's really nice.

**Dave Jones:** And that's the traditional domain of a logic analyzer. Right. Right. And. You know. Or. Or some sort of protocol analyzer or something. Before logic analyzers there were protocol analyzers. You know. Yep. Because a logic analyzer wouldn't decode it for you. It would just show you the way you form. Yeah.

**Chris Gammell:** It's.

**Dave Jones:** Do your own decoding. Exactly. You can. You can figure out Esky can't you. Yeah. Right. Why should I do it for you. What am I a machine. Yeah. Right. Yeah. Yeah. Yeah. And now it's all coming down into the one product. Which is a natural. Natural progression I guess. But still. Because it's trivial. To include that sort of stuff. But they still up the price. You know. They still keep those price points high. Yeah. The bastards. Yeah. So. Yeah. Because they can. And the market will tolerate it. Yeah. So. Yeah.

**Chris Gammell:** And you wonder too with like. With finished products like. Like test equipment or software. Stuff like that. I mean like. It seems like that kind of narrows. But it would be interesting to watch. As like more and more chip people. Come out with new products. Because it seems like. It almost seems to me like. Like a lot of the chip makers. Are absorbing. What was previously. You know. Finished good products. Right. So now there's a lot more. Right. Like on chip integration. And there's in package integration. Yeah. All that other junk. And. And so that. They'd be the ones. Just to really watch. And see if. If they're all coming out with the same part. At the same time. That means one of two things. Either. A. They're all using the same foundry. Right. Because then. Right. As soon as. You know. The foundry. Updates their. Their process. No. Then everybody gets that bump. Or. Yeah. That means that everybody. That the same effect. Is actually occurring. So. I don't know.

**Dave Jones:** Right. Yeah. I don't know. Or there's just good old fashioned. Corporate espionage. Well. There is that too. I mean. I mean. I. I'm all for that. Great. Spy versus spy. Spy versus spy.

**Chris Gammell:** Yeah. Yeah. It gets crazy. You know. Like some people. I have no exposure to it. You know. Like. I'm not a spy. Yeah.

**Dave Jones:** I don't really know. And. Well. I. One of my previous companies. They deliberately set up a Chinese wall. As they call it. With our. With our design group. Because we were deliberately. Designing. A product. Which would. Be exactly. The same. Well. In functionality. Exactly the same. As. One of the. As. We were actually. As another company. Who we were buying. The rights. To use that product from. So we wanted to do our own. In house design solution. So. You know. And they deliberately set up. A Chinese wall and company. Right. We are not. We. The design team. Are not allowed to know. Not even allowed to look at. The competitor's product. At all. Any aspect of it. Wow. You know. Was. Was just banned. Because they didn't want anything. To. Any design decisions. To subconsciously. Be copied. From the other person's product. So. Did you guys do an analysis.

**Chris Gammell:** At the end. To see how much was actually similar. That would be interesting.

**Dave Jones:** Ah. Well. It's. Well. The functionality. Well. Yeah. Was always similar. And. And there's only certain chipsets. On the market. Yeah. That you can use. And stuff like that. So. Yeah. In the end. Yeah. There were a few similarities. But. Yeah. It was just like a superficial. Oh. Okay. Kind of thing. Deep. Deep. You know. The underlying. All the software underlying. It was totally different. And. Well. Software. Yeah. Software I can understand.

**Chris Gammell:** But I mean. I think about like. So. Say you had a problem. You're trying to solve. And you have like. Ten design teams do it. How many of those design teams. Are going to design. A very similar architecture. And then.

**Dave Jones:** Well. It depends on the product. But our one. There's only a few ways. You can do a charge amp. Front end. Yeah. With a world leading. 24 bit. AD converter. Right. There's only like. Two chips on the market. You can use. One or the other. Right. And one is. Got 90% on the market. The other's got about. Yeah. 10%. Which one are you going to use? Well. You know. You're going to use the same. That same chip. Which then you're going to follow the app notes. So you're going to have a similar. Input functionality circuit. They've got. You know. So the front end. So it would depend on the problem too. It starts being the same. Yeah. And. Yeah. It does. Yeah. Totally. Okay. That is interesting. But then. But then the system level solution was totally different. Yeah. So. Yeah. You know. It was. Yeah.

**Chris Gammell:** Interesting. Anyway. Yes. Well. Speaking of the. The. Using the same foundry. I. I found this interesting company. Actually. On Twitter. This was very shocking to me. It was. Really weird. So the company is called Touchstone. Semi. Yep. And they just like showed up on Twitter. It was just like. Hey. What's up? We're a new company. We're an analog. You know. I love analog. Right. We're an analog chip company. Hey. What's going on? We have a new product. They just like came out of nowhere. I don't know. Actually. Not out of nowhere. It turns out. I would say. I poked around their site. I'm sure they. They're all former Maxim people. It looks like. Right.

**Speaker ?:** But.

**Chris Gammell:** Yeah. It's. They have a cool product. And they only have one product right now too. But they're. They're like fab based. So they're using TSMC. And. And their product is. Oh. It's like a 0.8 volt. Rail op amp.

**Dave Jones:** Oh. Is that all? Okay.

**Chris Gammell:** Yeah. It's. It's cool. I mean it's cool. It's a time. It's a really. Oh. Well. Yeah. To like 200. I don't want to like plug the product. I haven't tried it. But. But like. You know. It's. It's cool. You know. They're using. They're using TSMC processes. Yeah. But. It. It was just weird. They just came out of nowhere. And the fact that they showed up on Twitter first. Where. These. Monstrous. Billion dollar companies can't show up. Oh. Wait. Wait. Wait. Wait. Ahem. Ahem. Ahem. Ahem. Ahem. Ahem. Ahem. That was. Actually not me saying that three times. I should have actually talked over myself. Come on companies. You can do better. Come on companies. You can do better. Come on companies. You can do better. There we go. There we go. Oh man.

**Dave Jones:** I can. I can. I can do that. Do that. Do that. Oh man. Damn it. And. And. And. And. Yeah. All right. I'll stop doing that. All right. Sorry. All right. Anyway. There it is. You go to the product page. And they've got one. One part.

**Chris Gammell:** One part. Yeah.

**Dave Jones:** Yep. Great. Got to start somewhere. Yeah.

**Chris Gammell:** Yeah. And it's. It's interesting. It's possible these days. Because like the fabulous model. But. I haven't seen it on the consumer side. You know.

**Dave Jones:** Yeah. But then that's the classic chip startup. Problem. Right. Oh. No one wants to use your parts. Yeah. Until you can buy them a DigiKey or Mouser. Well. Yeah.

**Chris Gammell:** I'm a little worried about that. But. I mean. At least they. It would be different if they were. If they had a whole fab on their own. Right. Because then you're like. Well. Right. Who knows if they're going to be able to get. Chemicals tomorrow. Well.

**Dave Jones:** Nobody has a whole fab on their own. Well. Yeah. Starting from scratch. That doesn't happen as much. Yeah. Yeah. You need like a 500 million dollar startup. Yeah. That's true. That's going to happen. Yeah. Right. Sure. You know. It's a bit different to. You know. Three engineers in a. In a rented office somewhere. Right. Right. Yeah. It's a tad different. Yeah. Yeah. So I know. Yeah. There it is. It's got a 75 cent cost. Yeah. So this little rail to rail. Chip.

**Chris Gammell:** Yeah. And.

**Dave Jones:** VDD minimum 0.65 volts.

**Chris Gammell:** Oh. Is that what it was? Sorry.

**Dave Jones:** 0.65. Which is under. The. The. You know. The dropout voltage of a single cell is 0.8. After that it just drops off like a brick wall.

**Chris Gammell:** Right.

**Dave Jones:** Right. Yeah. So this thing is absolutely. You know. Yeah. It's cool.

**Chris Gammell:** I mean it's cool.

**Dave Jones:** Fantastic.

**Chris Gammell:** But you know. You can tell from the voltages too. You can tell they're using the new core voltages that they'll use on like. You know. TSMC. So they're using some. Yeah. Some CMOS process. And. Yeah. Like the rest of the specs on the chip aren't really aren't that bad. I mean it's an op amp. I love op amps. Like. They're not bad specs. But. Oh no. But. But these guys will get. They'll only get a bump. You know. Like that's. That's the difference. Right. So. These guys will get a bump when TSMC improves their process. Whereas like people like Linear Tech or National or TI. A lot of them have their own fabs. And then they can go in and tweak stuff. They can tweak. Yeah. Like processing parameters. As opposed to just. You know. Changing widths of gates and all that other junk that people do as chip designers.

**Dave Jones:** Now. The interesting thing is. Right. They're. It's a startup company. And they're designing an op amp. Right. Yeah. It might be really cool. But is there another comparable one out there? Is it that unique? I don't know. I'd have to. You know. Off the top of my head. I can't say. Yeah. But that's what it would require for them to be a success. Like really niche. Because nobody in their right mind.

**Chris Gammell:** Yeah.

**Dave Jones:** Would. Would design in a part from a startup company. A critical part from a startup company. Right. Into your product. Unless there was no. Absolutely. No other choice. Right. You'd be mad. Yeah. You'd be sacked if you designed in this part into your product. Unless you had no other choice. Right.

**Chris Gammell:** And that's the thing I've heard about with like. Not even just startups. But just companies. Like just competitors in general. You have to try and be like low cost enough. And you have to chase things that are. That basically the other company won't notice. You know. Like the big boys won't notice. So. Yep. If this is maybe. Ten million dollars of chips a year. Perfect. Yep. Low cost to the people actually designing the chips hopefully. Yep. That's how you start building.

**Dave Jones:** I've always been of the opinion that there's. You know. There's no end of FPGA startup companies out there. Right. Yeah. But none of them are producing. This is one of my big. Rants with FPGAs. None of them are producing small easy to use pin count FPGAs. With high density. Large die sizes and high density. They're all going for the massive pin count.

**Chris Gammell:** Yeah.

**Dave Jones:** If you know. If one of these FPGA startups would come out with like a. Heck. You know. An eight pin SO package. Woohoo.

**Chris Gammell:** That would be pretty sweet.

**Dave Jones:** Yeah. Or just. You know. Just a low pin count high density thing.

**Chris Gammell:** Hear that Zylix? How about you all Tara? Yeah. Anybody?

**Dave Jones:** Oh. I've been bitching out for 10 years to do that.

**Chris Gammell:** Sorry.

**Dave Jones:** Idiots. And I've. You know. And I've had official responses from. And they go. Well. That's. No. You know. The market forces don't dictate that.

**Speaker ?:** Yeah.

**Dave Jones:** Well. If you put it out there. People might actually go. Oh. That's neat. Because I only need 10 IO pins. Yeah. But I need. To put a huge soft core in there. With all this decoding. And other fancy stuff. So I need lots of. Yeah. You know. I need lots of logic elements. Lots of flip flops. Lots of memory. All that sort of stuff. But. Jeez. You know. I don't want to get it. I don't want to have to use a thousand pin BGA to get it.

**Chris Gammell:** Yeah. That'd be like hiding a. You know. Like a. 600 horsepower engine inside like a Hugo. Or something like that. You know.

**Dave Jones:** A. A. Hugo. What's a Hugo.

**Chris Gammell:** It's a. Crappy type of car. It's an old. Right. Old car. No. Sorry. I don't know. That's what I assume. But I've never heard of it.

**Dave Jones:** Well.

**Chris Gammell:** How about a Nova.

**Dave Jones:** A Beetle. A Beetle. How about a VW Beetle. There you go. Yeah. Everyone knows a VW. Yeah. There you go. Right. Awesome. But yeah. Anyway. End rant. FPGA. Slash. So anyway. Good luck to touchstone. Yeah. Touchstone semiconductors.

**Chris Gammell:** Yeah. I wonder if they're getting any crap from the movie studio. Right.

**Dave Jones:** Yeah. Yeah. There you go. Yeah. Hey. Watch out. Yeah. You could get your ass suit off. I hope you've got a lot of venture capital there. To. Yeah. Touchstone pictures. Well. Touchstone semiconductor. Yeah. Yeah. Go figure. Yeah. I don't know.

**Chris Gammell:** Speaking of California. Have you seen this thing with Hackaday?

**Dave Jones:** Oh yes. Please. Let's. Let's. Let's talk about this.

**Chris Gammell:** So Hackaday is hiring a project maker. Which is a really cool idea. Right. I mean. They're basically going to pay someone. Yep. To sit there and hack on stuff. You know.

**Dave Jones:** Fantastic.

**Chris Gammell:** Basically be a content creator for them. Yep. But. 30,000 guys. I know. It's probably. Students you're looking for. Or whatever. But $30,000 in California.

**Dave Jones:** Right. I take it. That's kind of low.

**Chris Gammell:** That's kind of low. Let's see.

**Dave Jones:** Right.

**Chris Gammell:** I don't know. What do you think about this?

**Dave Jones:** Oh. I think it's. Well. It sounds pretty low to me. It sounds like they're really low balling. And. Well. If that's all they got available. Well. You know. I mean. Hackaday is not exactly a. You know. A huge company. Right. Right. In fact. I thought it was just a one man band. Still. Almost. Effectively. I thought they're.

**Chris Gammell:** I'm going to talk on my book there. Yeah.

**Dave Jones:** I don't know. Yeah. Let's not talk about that. But yeah. I. You know. Like I can understand maybe like as a part time.

**Chris Gammell:** Yeah.

**Dave Jones:** Job. Yeah. Or something like that. You know. They shouldn't be hiring somebody full time. Yeah. At that low ball salary. Because that starts setting precedence in the market. And well. You know. Yeah. This content. Producing content like this is worth a lot of money.

**Chris Gammell:** And it's hard. I mean. If you're doing a hack a week. Or whatever it is.

**Dave Jones:** Oh yeah. Like that's. Let me tell you.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** You're doing a hack every week with video. And you know. Explanations. I know. Everything else. I heard it was. That's a lot of work.

**Chris Gammell:** Santa Monica. I'm not sure if that's right. But that's what I heard it was. Right. I think it was Santa Monica.

**Dave Jones:** Well that's even more expensive. Isn't it? Isn't Santa Monica a real expensive.

**Chris Gammell:** I think that's what someone said.

**Dave Jones:** Area to.

**Chris Gammell:** Ah. Crap. Sorry. But. If it is Santa Monica. And you wanted to move to Cleveland. You would get paid a whopping. $9,520.

**Dave Jones:** Oh really? Yeah. Is that the conversion? Is that the conversion?

**Chris Gammell:** Cost of living calculator conversions.

**Dave Jones:** Cost of living calculator. Yeah. Wow.

**Chris Gammell:** Yeah.

**Dave Jones:** That is. Unbelievable. Uh. I don't know what the minimum wage here in Australia is these days. But it's not. It's around that. It's got to be around that figure. Yeah. So. You know. That's like. You know. Flipping burgers at Macca's. Mickey D's. Sorry. I was like. What Macca's?

**Chris Gammell:** Yeah. So. That's what it says. Santa Monica. Santa Monica office. $30,000 to $40,000 a year. And if it was. Oh.

**Dave Jones:** Up to $40,000. Oh. Okay. If you're really good. And you've got a big name. Because you're a big name blogger. Maybe. They'll give you $40,000. I mean.

**Chris Gammell:** I'm guessing they're probably going to try and target people that aren't. You know. Yeah. Doing much. If it's $40,000 to Santa Monica. You can move to Cleveland. And you can get $12,694 instead. And it would be equivalent.

**Dave Jones:** Oh. Live it up. Yeah. Yeah.

**Chris Gammell:** That'd be interesting.

**Dave Jones:** Spend until the cows come home. Yeah. All right. And $30,000 US is worth. I don't know. About a million Australian dollars now. So. You know.

**Chris Gammell:** See if you're rich. There you go. Was it really that bad? Sorry.

**Dave Jones:** No. It's worth about one Australian dollar. Oh. Okay. That's what it is. Sorry. You've got to go in the opposite direction. Yeah.

**Speaker ?:** I was going to say.

**Dave Jones:** That's what I thought. Because the Australian dollar has surpassed the US dollar. We are superior. Thank you very much. All right. That's good. Round of applause. Yeah.

**Chris Gammell:** Oh, yeah. Currency.

**Dave Jones:** Yeah. That's.

**Chris Gammell:** It's those damn engineers trading currency with computers. That's the real problem.

**Dave Jones:** Right. Moving into finance and crashing the system.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, anyways. Anyway. Just thought I'd mention that. And. What's his name? Dino. Dino. Yes. Make a Dino. Yeah. Has started. HackaWeek.com. I love this. He just went out and went. Well. I don't like this. I'll go out and register. HackaWeek.com. Do it for free. Exactly.

**Chris Gammell:** Yeah. So we'll. Brilliant. Post the link. And he started already. So we'll. We'll see how that turns out. I mean. But. I don't know. Yeah.

**Dave Jones:** I saw his first video. And. Yeah. Well. He didn't do anything. He was just announcing. Yeah. Yeah. It's like. Thing. And. Yeah.

**Chris Gammell:** It's almost like civil disobedience. So now he has to produce content. I'll do this for free.

**Dave Jones:** Yeah. I love it.

**Chris Gammell:** Yeah.

**Dave Jones:** Ah. It's great. Yeah. Stir in the pot. Mm-hmm. See. Because. Well. Hacka. You know. Hackaday used to be. You know. Used to have a good. Well. They still. Well. Up until this point. They had a good rep. As. Well.

**Chris Gammell:** They still have a good rep. I mean. They still. They show great projects. They do. Yeah. They do. It's still a great site. And they have a community. I mean. They have forums now and stuff. And it's. Yep. It's not a bad site. It's just. That's just. I think.

**Chris Gammell:** Unrealistic. That's what. That's what I'm pointing out. Yeah.

**Dave Jones:** I think that was a bad move on their part. Yeah. To try and hire full time. They should have just. Hired part time. You know. Look. We'll. We'll give you. A thousand dollars per hack or something.

**Chris Gammell:** Yeah. You know.

**Dave Jones:** I mean.

**Chris Gammell:** Or. You know. Let them do it remotely. Right. And forty thousand dollars. In Cleveland or somewhere else. You know. Des Moines, Iowa. Exactly. Then it's not that. Yeah. It's not that bad. Right. Yeah.

**Dave Jones:** That's right.

**Chris Gammell:** That would be the real thing. I would think. But.

**Dave Jones:** Yeah. Well. And. Why do you even have to be in the US? Why can't. Why isn't open to anyone? Yeah. Why do you have to. I don't understand this. If I was running a company. I wouldn't be hiring. For. A. I wouldn't be. You know. Going out and renting a bloody space to do it. You know. Like a. An actual office. And crap like that. You know. Do the offerless. The offerless. The office-less. Model. And. You know. Just have people working remotely from their home. They're happy. You're happy. Cost is minimum. And. You know. And it works. There's quite a few companies like that now. Who don't have an office anywhere. They don't hire full-time employees. They pay. Or if they do. They let them work remotely. And they. Yeah. They can be anywhere in the world. Why do you have to be. Yeah. I think there's. In the office. In.

**Chris Gammell:** You know. I don't know. Yeah. There's still a lot of resistance to that. With like. I mean. Like a lot of people are getting better with telecommuting. And it's. It's tough with electronics sometimes. You know. Because you do have. If you have shared equipment. That's. That's one thing. But. Oh yeah. You know. If it's like you and you have your own lab. Right. That's not as big a deal.

**Dave Jones:** Well. Then it's fine. Yeah.

**Chris Gammell:** But I mean. Yeah.

**Dave Jones:** Or they can. Or they can send you some gear. Or they can pay. You know. Some gear for startup. You need. You need a decent oscilloscope. Fine. You know. Yeah. Yeah. Then you write it off. Here's a couple of grand. Go out and buy one. Exactly. Yeah. Yeah. Yeah. I don't understand. Why. A company like Hackaday.

**Dave Jones:** I assume. They. They have an office. Right. You've got to come in. And work in their office. Yeah. Why. I mean. No.

**Chris Gammell:** To be fair. There are some. There are some benefits. You know. Having. I think there's. Benefits to having a workplace. Yeah. Maybe. There are. I think there are.

**Dave Jones:** Yeah. Well. Of course. Okay. Given.

**Chris Gammell:** Yeah.

**Dave Jones:** There are. But is it worth it for such a small. Well.

**Chris Gammell:** That's. That's a different question. Yeah. Yeah.

**Dave Jones:** A company like that.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** That really effectively doesn't. Like. Well. They do make kits and stuff. Don't they? So. I guess they're. They've got to have space for that. Yeah. You know. Yeah. I guess. Yeah.

**Chris Gammell:** There's a lot of cost to having a brick and mortar. For sure. Definitely. Yeah.

**Dave Jones:** There's a huge cost in that.

**Chris Gammell:** Yeah.

**Dave Jones:** And. That's why most businesses. Go under. You know. It's the old. You know. Like 70% of small businesses. Go out of business in the first. Year. Mm-hmm. Or something. I'm sure it's similar in the US. Yeah. But that's what the figures are like here. And. It's because these people. You know. Think that the only way to do it. Is to go out. And pay. You know. $2,000 a week rent. To hire an office space. If you're just running an online website. You know. It's just.

**Chris Gammell:** Yeah.

**Dave Jones:** It's stupid. You know. It's just crazy. It's. There you go. Pissing away. You know. Yeah. Pissing your money down the drain.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Ah.

**Chris Gammell:** Hmm.

**Dave Jones:** Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Well it's. Anyway. Dino. Good on you. I hope it works. And. Hackaday. I hope. Yeah. You choke on that $30,000. Because that's. Yeah. That's. Come on. That's just. No. Let them work anywhere. And let them. You know. Just hire them. To pay them per hack.

**Chris Gammell:** Let's do. Yeah. You can do that.

**Dave Jones:** What's wrong with that? You know. Mm-hmm. I don't know. Instead of. You know. Slave driving their ass. In your lab there. For $30,000 a year in California. Yeah. Which I assume. Is a very. High cost of living.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway. Not happy.

**Chris Gammell:** What about. This design. So. Before you get into. Your design contest. I want to just mention. We're actually finishing up. 555 stuff right now. It's been a while. Admittedly. But we are actually. I want my spreadsheet list. I know. I know. Dave wants to judge. Australian. Australian entries. Yes. But. Yeah. We're almost done. And. So we should be announcing here. In the next couple days. I'm really worried. Because it.

**Dave Jones:** Fantastic.

**Chris Gammell:** It looks like it's going to line up. To be like April 1st. And me and Jerry said. From the beginning.

**Dave Jones:** Oh no. We can't even.

**Chris Gammell:** There's no. There's no way we're going to do that. You know. Like. Right. I don't trust a damn thing. On April 1st. On the internet. It always. It always takes me at least one. You know. I read one thing. And then I'm like. Right. I'm like. Yeah. Oh yeah. Okay. Right. Brilliant. Yeah. But how about. How about the design. So. You are. Officially judging.

**Dave Jones:** I am officially judging. The. Renesys RX. Design contest. Yes. I am. On one of the judges. And. It just closed yesterday. They had a big countdown timer. On their site. You know. Ta da da. Six hours left. And. In the true style. Everyone submitted in the last. 24 hours. Yes. Or something. Awesome. And you know. Down to the last minutes. There's. Entries. You know. If engineers are one thing.

**Chris Gammell:** It's consistent. Consistently. Procrastinators.

**Dave Jones:** Including Jerry. Who was very early. She was quick off the gun. She submitted with about. Five hours left. Or something.

**Chris Gammell:** All right. Go Jerry. I.

**Dave Jones:** You know. Jeez. She just pissed away. Those extra five hours. I know.

**Chris Gammell:** She could have just been sitting there. Cackling. And waiting to hit submit button. You know.

**Dave Jones:** Right. Yeah. Exactly. Do it at the last minute. There you go. Disarming that bomb. MacGyver style. You know. There's got to be two seconds left on the clock. Got the blue wire. Anyway. They only had. In the end. 30 entries. Wah. Wah. Wah. Wah. Wah. Oh. The Dave sound effect. Yeah. Sorry. Yeah. That's a bit. I know they were expecting. A lot more. Yeah. Entries. But granted. It's kind of a more advanced design contest. Than the triple five. It is. Right. There's a lot of effort. I know a lot of people have put a lot of effort into the triple five one. But it's easier to get motivated. Right. It's a start up time. Right. It's a start up time. Because you think it's easy. And then you go. Oh no. I'll just do this. And then you just add it on. Whereas up front. If you know you've got to get a 32 bit micro up and running. Yeah. And do something. You know. Oh. Fancy graphics on the display. And you've got to use the ethernet. And you've got to use. You know. Yeah. Yeah. Exactly. And it's a. People just go. Oh. I don't know. It's a bit hard. I'll do it later. Yeah. I'll do it later. Exactly. I've used a micro before.

**Chris Gammell:** I'll be fine. Seriously. I'll be fine.

**Dave Jones:** And somebody tweeted. I can't remember who it was. When I tweeted that there's six hours left. Get you. And someone went. Oh shit. Is there?

**Chris Gammell:** Because that's over.

**Dave Jones:** I shouldn't have procrastinated. Whereas. If there was six hours left for a triple five contest. You likely could have. Maybe. Yeah. You could have put something in. Lash something up. You know. Yeah. At the last minute. For sure. Yeah. Yeah. So. Yeah. Anyway. So I guess that's. You know. It's hard to compare. Yeah. The two contests. It is.

**Chris Gammell:** It is. It's. Yeah. It's tough in general. You know. A lot of companies struggle with design contests in general. I think. And it's just because. There's a lot of them. You know. A lot of people. Want to get your. Want to get their ideas out. Or want to get their products. Like in people's hands. And like show off their products. But. It's. You know like. It's tough because. Because of that startup time. And because there's so much other stuff going on. So. Keep trying people. I think personally. And I'll. I'll give this advice free to all. All companies out there. Looking to do design contests. Honestly. Sometimes. You'd be better off. Just giving the stuff away. And just not doing anything with it. Like. And that's effectively what TI did with their. Their launch pad boards. Right. I mean. They were effectively free. You have to have some kind of cost to. Make sure people don't just like order 10 of them. But. You know. But give it away. And see what people come up with. Because people are going to do something. If they have just a microcontroller sitting around. Or parts sitting around. Yep. So. I agree. Yeah. And then later. You know. Once people have it in their hands for a while. Then you run a design contest. You remind people. Hey. Remember that board we gave you? Hey. Yeah. Yep. Why not use it now? You can use that. Hey. Fabulous prizes. That's the way to do it. Yep. Yep. So.

**Dave Jones:** And no board. You know. Just make it simple. You know. Simple's good too. No legal rigmarole. And all the other crap. Yep. You know. Just keep it dumbass.

**Chris Gammell:** Mm-hmm. Yeah.

**Dave Jones:** It's not hard. But. Big companies can't do simple. It's just not in their nature. Right. Well. Yeah.

**Chris Gammell:** And there's. You know. Like simple will eventually equate to elegance too. Right. I mean. If you open it up. Yes. And you don't have a lot of rules. And. But you say. Do whatever you want to. You're going to have people that really get into it. You know. Like we saw that with 555 Contest. Yep. Yeah. People love it. Take it and they run. Yep. So. That's the way to do it people.

**Dave Jones:** Absolutely.

**Chris Gammell:** And I think. Our amp hour is up. What do you think?

**Dave Jones:** Oh. God. It is too. Yeah. One hour and one minute. Yep. Unbelievable.

**Chris Gammell:** And so we had a suggestion last. And we didn't even get into half our stuff. I know. Well. Well. Please. 36 items. We had a suggestion last time though. That we should. Not just ramble on. Start. Start. Talking about bad names. At the end of it. But. Bad names? Threesomes basically.

**Dave Jones:** Oh. Right.

**Chris Gammell:** Okay. Right. And that. Now we've just done it again. Anyways. I want to remind people that. If you go to the amp hour. You can comment directly on the page. We love having comments there. Also you can find me and Dave on Twitter. And if you have suggestions. We always love suggestions. We've been getting more suggestions lately. We have? Yeah. It's really cool when people do that. So we appreciate that. So if you got something in mind. Give us a shout. If you have a guest in mind. You know. If you really want to hear someone on the amp hour. Give us a shout for that too. That's.

**Dave Jones:** Please. And we'll try and get them on. Because we are a large. Highly. Highly respected radio show now.

**Chris Gammell:** Yeah.

**Dave Jones:** Which is now cheapened with. Yeah. With bad sound effects. Cheap sound effects. Thanks Chris. Yep.

**Chris Gammell:** Yep. Yep. All right Dave. All right. Well we'll talk to you next week. All right. And cool. Thanks for listening everybody.

**Dave Jones:** See you guys.

**Dave Jones:** Yeah, power rules! Help, I'm stuck in a cage!
