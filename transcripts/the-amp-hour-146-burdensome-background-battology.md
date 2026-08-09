---
episode: 146
title: Hamvention, Arduino and Intel - Burdensome Background Battology
url: https://theamphour.com/the-amp-hour-146-burdensome-background-battology/
---

**Chris Gammell:** This episode of the Amp Hour is sponsored by Club Jameco, part of Jameco Electronics. Have you ever wanted to sell a kit you dreamed up? Do you have an idea for a new project you're working on and you think others would like working on it as well? Club Jameco allows you to upload your kit ideas and start selling to your peers. You can earn up to 10% on every approved kit that you sell. Additionally, if you submit an approved product brief, you will get a coupon code for 10% off your next order at jameco.com. To learn more and to see the chosen kit of the week, go to clubjameco.com slash theamphour. This is the Amp Hour Podcast. Recorded May 21st, 2013. Episode 146. Burdensome. Background. Pathology.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Dave Jones:** Are you wearing your funky new Amp Hour t-shirt?

**Chris Gammell:** No, it's in the wash. I've already worn it out.

**Dave Jones:** Mine's been washed and I am wearing it right now. I tried to tweet a photo of it, but my stupid phone doesn't work. Oh, yeah. God, I hate technology. Pisses me off.

**Chris Gammell:** You know, you should build your own phone. Just start from scratch. Oh, yeah. First principles.

**Dave Jones:** You're using all that free time I've got, yeah.

**Chris Gammell:** A whole video series on how to build a phone.

**Dave Jones:** Right, yeah.

**Chris Gammell:** Not a problem. There actually was one at some point where, I forget who, was it Bunny? I think Bunny was doing that. Oh, right. He had like a real, or maybe he found a low-tech phone. I remember seeing a really low-tech phone, but it was basically, you know how you can buy GSM cards and interface to those and that kind of abstracts out some of that stuff. It's pretty cool. So, yeah, build your own, man. Done. Yeah, right. Do it. Do it.

**Dave Jones:** After I destroy this one with a freaking sledgehammer. Yeah.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Maybe I was just to attack it with a screwdriver until it dies. Stab it. Stab it, the heart of that bastard.

**Chris Gammell:** I don't know, man. I think about, I saw someone talking about that on Reddit today about, they said, you could only, a challenge of only using technology that you understand how it works, right? Right. Or, I guess taking that to the next level would be, only allowed to use technology that you've built yourself. Right. I think I would have a very disconnected experience.

**Dave Jones:** Right. So, it'd be fabbing all your own silicon using that chip printer machine in your basement. Oh, yeah. Well, there's that.

**Speaker ?:** Yeah.

**Dave Jones:** Right. Otherwise, you're just a cop-out. Well, no.

**Chris Gammell:** I think, you know, if you can make your own, you know, you'd have to make the silicon. You know, it would have to stop at some point, right? Because even if you're making your own chips, you're not necessarily refining the silicon.

**Dave Jones:** Well, why not put the stop point at whatever you can buy at, you know, at your local department store?

**Chris Gammell:** At the hardware store? Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** No. Well...

**Dave Jones:** As in the final phone. Yeah. It's not going to work. No, I don't think so. Jawed a line somewhere. My ass. Anyway, the AirPower T-shirts are really cool. The Teespring one is infinitely better than the Printfection one. I'm very disappointed with the Printfection shirt.

**Chris Gammell:** Yeah, I'm working with them. So, if any of the people that won, the ones from the contest last time, we're not going to give out any more T-shirts until then, but we will start contests right after we get that all sorted. We have new prototypes coming through, so people know how that is with prototypes, you know. We just got lucky on the first one, you know. Sometimes you get lucky with prototypes, right?

**Dave Jones:** Yeah, yeah. Sometimes.

**Chris Gammell:** That actually happened to me last week. Woo-hoo! Yeah, I saw your tweet. Yeah, I got a new one in, and I'm just like, I fired it up, you know, I got all my protections in place, making sure I currently limit my supply, and, you know, I'm watching everything like a hawk. I'm watching the noise on my power rails and everything.

**Dave Jones:** Spelling for any issues.

**Chris Gammell:** Yeah, exactly. You know, feeling for heat, you know, like just watching everything, you know, just everything you need to do when you bring it up on board. And it just worked. Awesome. A part of me was just like, oh, I know I should be happy, and I was happy, you know, it was good. But sometimes you want a puzzle to solve, right? It's like...

**Dave Jones:** I had a puzzle the other day.

**Chris Gammell:** Yeah? Was it...

**Dave Jones:** I tweeted it, yeah. A new board or what? It's a new board, yeah, thing I'm working on. And it was, you know, there was this really minor offset issue, right? Oh, tell me about it. You know, right? We're down in the microvolts, right? So we're down in the Chris Gammell world at your former life. Yes. Yes. Keithley, right? And, you know, and it was annoying, and I couldn't figure it out. And, of course, naturally...

**Chris Gammell:** So this is on, like, the input to an op-amp or something?

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Okay.

**Dave Jones:** And with a large gain, right? And, like, I figured, well, I've done this, like, but I was using a new chip, and I thought, well, is the new chip at fault? And I'm checking the data sheet, and I'm going, no, it shouldn't be. It should be, you know, your data sheet even gives nice little histogram plots of sample devices and what offset they should have, right? You know, and, like, 80% of them are within this margin, blah, blah, blah. And I'm going, like, mine would have to be right off the outlier bell curve, right, to be this bad. And so I ruled out that, and I thought, oh, it's got to be, you know, it's a new layout board, right? Something's wrong with my layout, so I'm hacking.

**Chris Gammell:** Yeah, like dirty or bad layout or something. Yeah.

**Dave Jones:** Diode drops or something. Yeah, or the wrong, you know, ground points in the wrong location, and there's, you know, some extra circuitry on there. It's getting a drop through the power plane. And, you know, so my engineering mind starts going and thinking of a dozen things that could be, right? Yeah.

**Chris Gammell:** Oh, let me guess the resolution here. Did you change out the chip? Did you just swap it out and it worked, and that was just one bad chip?

**Dave Jones:** No, no, no. I swapped them dozens of times, and I'm putting them and trying them in different boards and all sorts of things. And I even put it in an old layout board, the same chip, and it worked perfectly. And I thought, aha! You know, it's got to be the layout, and that led me down. No. Turns out, you wouldn't know what it was.

**Chris Gammell:** I'm trying to think of it. You know, this is like the escalation, right? This is like, you know, you get the obvious stuff first, and you're just like, uh-huh, this might be a real one. We might be chasing a real one here. Was it a bias current? I mean, could it have been a bias current across, like, resistance or anything?

**Dave Jones:** No, it's not that complex.

**Chris Gammell:** Was it dirty?

**Dave Jones:** Nope.

**Chris Gammell:** Were you measuring it wrong?

**Dave Jones:** I can see your engineering mind, that lower measurement engineering mind going, right? No, you're going in.

**Chris Gammell:** Were you measuring it wrong?

**Dave Jones:** No.

**Chris Gammell:** I guess you'll have to give me a hint here or something.

**Dave Jones:** I'll have to put you out of your misery? All right. Yeah, yeah. It was the bloody power supply. Oh, no. Well, it wasn't just the power supply, right? It was, um... Wait a second. It looks like, well, it looks like a thing with the... It's an issue with the chip, right? The chip is actually, its offset voltage is power supply dependent. And they don't tell you that in the data sheet.

**Chris Gammell:** So what are the rails? What rails were you on this?

**Dave Jones:** Plus, minus two and a half. Well, yeah, around about plus, minus two volts. Okay. Thereabouts, just over. You know, so really low rails. And it only worked when I took it down to 2.8 volts. Like, took it under 3 volts. Over that, the offset sort of just goes through... Well, through the roof in terms of, you know... Yeah, it's still within, like, 0.05% or something. But that's not good enough, right? Right. You know, and it was bugging me. And, yeah, they don't tell you that in the data sheet. They do have that histogram plot of... Of taken at different power supply voltages, like 2.7 volts and 5 volts. But it doesn't hint at that, you know, when you have a large-ish gain on there that the offset voltage is...

**Chris Gammell:** Hmm. So you weren't, like, starting to push the rail or anything, right? Like, so the input wasn't... Was it near the rail or anything or no?

**Dave Jones:** No, no, no. Well, and these are rail-to-rail inputs. No, it was smack in the middle, right? Smack in the middle. Yep.

**Chris Gammell:** Hmm.

**Dave Jones:** So, yeah.

**Chris Gammell:** Yeah. That is... Bastard. Tricky. And so what was resolution then? What did you do?

**Dave Jones:** Oh, the solution is to get a precise circuit is just whack a voltage regulator in, whereas I was just going to power it just from some batteries. And, of course, as the batteries, like, drop, the offset voltage will change.

**Chris Gammell:** Oh, yeah. That's a real big problem, then. Yeah. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, because that wouldn't be a problem if...

**Speaker ?:** Bastard.

**Chris Gammell:** It might get out the door like that, right? Where you're testing it as you get this device out the door, and you're like, yeah, it looks great. I'm always using fresh batteries. Yeah, it looks great. But then once a user gets it in their hand, they're like, this starts to suck.

**Dave Jones:** Well, it's actually the other way around, because the offset voltage is worse at a higher supply voltage. So when you put fresh batteries in, and that was the problem. I put fresh batteries in, and the offset voltage was high. And it's only when the batteries get to right down near the end of their life that the offset voltage is nice where I expect it to be. So...

**Chris Gammell:** Really? Is that on the datasheet? Yeah. Did you find that on the datasheet?

**Dave Jones:** No. No. This is through practical experimentation with this chip. And it's a great chip. I love this chip. Right? It's an analog devices part. Which one? And it's a really schmico chip.

**Chris Gammell:** Will you say which one or no?

**Dave Jones:** 80, 86, bloody, blah, blah. I don't know. I can't remember off the top of my head. 8,000 series. Yeah, one of the four-digit 8,000 series or something. Those are nice.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah, they're very nice. Very nice. Yeah, not too bad. Pop-amp. And not too shabby at all. But yeah, this little pain-in-the-ass problem. And it happens every time. My mind goes into complex engineering troubleshooting mode and thinks that, you know... So I use all my experience of every problem I've ever had over the decades, and I go, right, it could be this, this, this, this, this, this, this. And it's like, oh, jeez, you know. You just make an idiot out of yourself. Yeah, the burden of experience. That's...

**Chris Gammell:** It's like the acid trip of troubleshooting, right? You're having flashbacks of, oh, it could be this.

**Dave Jones:** Oh, that's right. I remember that bastard from 10 years ago. It's the same trap, you know, and it's not. Can that be the title of today's show, the burden of experience?

**Chris Gammell:** Yeah, something like that. We can put that in there. Something, yeah. I don't know, man. That still doesn't strike my ear as it... That might come back and hit you still. I mean, so you're saying you put a voltage regulator on there, and now everything's fine?

**Dave Jones:** Well, I haven't put a voltage regulator on yet, but I've tested with my bench supply and individual batteries.

**Chris Gammell:** I think we might hear about this in future shows. This might not be over yet. To be continued. Nope.

**Dave Jones:** No, I'm pretty sure I've nailed it. I've tracked it down, and yeah, that's it.

**Chris Gammell:** Well, once you do, you can make it into one of your little fundamental Fridays, and I can learn something from it, because I still don't understand that mechanism. Right.

**Dave Jones:** Well, neither do I. It's internal to the op-amp, right? It's inherent to the op-amp, so I don't know what's actually going on there at the individual transistor level to cause this, but sure enough.

**Chris Gammell:** Yeah, I had a weird experience a couple days. I guess it was last week or so. When I was making that... Sorry, I was working on a new T-shirt idea, right? Right. The one that I tweeted out, and I sent it to you, and a lot of people didn't get it, but I was pointing to all the bases on the LM324 schematic with all these NPN and PNP transistors, and it was all your base are belong to us. And if there is interest in that, I am still willing to make a T-shirt, but I just don't think there's as much interest as there might be.

**Dave Jones:** There's not. Even when I asked you to explain it to me, I still didn't get it. I know.

**Chris Gammell:** I know.

**Dave Jones:** I thought, what's the joke? There is no joke. It's stupid. You'd have to know what the... It was like this thing back in the 90s. What? Come on.

**Chris Gammell:** It's pretty cryptic. But anyways, it'd be cryptic and then electronics on top of it. But anyways, so I was redrawing this LM324 schematic, right? I was just looking at it, and I think it was in the Art of Electronics is in there, in a simplified form. But it's just kind of like, as you look at things over the years, it just started to fall into place a little bit more. I'm like, oh, I kind of get this now. You know, like, it's like I always ignored a lot of the schematics and stuff from the lower-level op-amp stuff. And the LM324 is a simpler one in terms of modern terms. But, you know, it just feels good as you kind of start to see the matrix, you know, a little bit more. Got it. You know, it's just, it's a good feeling. And so people that don't yet, you know, the ones... That's what I really want to say is that if you don't get it yet, right, if you're looking at schematics and you're just starting out, it'll come eventually. You know, really it's about pattern recognition. You know, that's a big part of electronics, I think, is, you know, at first it just looks like gobbledygook. You know, I remember looking at early schematics and being like, not early schematics, but just early ones for me, and just being like, which directions are the signals even going in? You know, if someone is, you know, they maybe ran out of room on the page and they start to loop signals back around, you don't know if it's going in or coming out, and you're like... Ah, it's Bob P's style, huh? Yeah.

**Dave Jones:** Oh, yeah, it's... You remember, Bob P's used to draw the most obscure hand-drawn circuits, right? Oh, yeah. They'd be like all over the shop, like spaghetti. Yeah, exactly. So you couldn't recognize any common building blocks.

**Chris Gammell:** Yeah. The secret of his success, then he needs to teach you how... What the hell he's talking about, right? Obfuscate. Yeah.

**Dave Jones:** Obfuscation.

**Chris Gammell:** Oh, yeah. That actually could be a good contest, a t-shirt contest for us. I used to do that with a friend at work. We would draw obfuscated circuits, right? You take a circuit and then you put in... A standard building block and then just... Yeah, you put in like diode drops where there shouldn't be, and, you know, loop signals back around. You allow current paths, and we were bored sometimes. But, yeah, you know, it does get better. That's what I'm trying to say is that if you're not... If you're starting out or, you know, even if you're, you know, on your way towards, you know, learning more electronics, you know, it's just about pattern recognition and really then implementing those things as well, right? I mean, I think these days it's getting easier because, you know, there's all these great app notes and great circuits that are given to you from vendors and, you know, as part of, you know, these higher-level integration chips. But even with the lower-level stuff, a lot of times it's just kind of, you know, cookbook style sometimes. Not always, but sometimes. And then the real art is kind of integrating everything and throwing in the glue components in order to, you know, get that diode drop you need or get the, you know, get the voltage range to where you need it to be, that kind of thing. That's the fun stuff, I think.

**Dave Jones:** I think you've given me an idea for a T-shirt.

**Chris Gammell:** Oh, another one?

**Dave Jones:** Yep. I'll tell you after the show.

**Chris Gammell:** Okay. All right. Write it down. You write it down? Yeah, I've written it down. We forget way too often. Yeah, otherwise forget. Yeah.

**Dave Jones:** And then I forget where I've written it down. Yeah. Well, that's just getting old, man. Because there's just post-it notes everywhere and it's like, yeah, there's not, you know, there's not already 10,000 post-it notes around my lab, you know. Right. Yep. Ah, man.

**Chris Gammell:** So I just got back from Hamvention.

**Dave Jones:** How was it?

**Chris Gammell:** Nerdy, nerdy, nerdy. Based on the photo, yeah. And old. Really old. Old. Like the, so we had our meetup on Saturday night, which was great. Bunch of guys showed up. It was really, really great to meet everybody. Um, but these guys are like the youngest ones of the bunch. Like.

**Dave Jones:** I was going to say, the photo, everyone in the photo looks relatively young. Yeah.

**Chris Gammell:** Yeah. Uh, so apparently last, I think last year there was a survey of Ham, Ham radio, um, you know, I think participants, not necessarily people that just have licenses.

**Dave Jones:** And they were getting younger, weren't they?

**Chris Gammell:** Last year was the first year it didn't go up, I think. But last year was still 61 was the average age of Ham, uh, amateur radio enthusiasts. So 61 is pretty, that's pretty up there, you know. And, and I saw it as, you know, I got on the bus, you know, there was some oxygen tanks and there was a lot of great hair. And they were all, you know, they were great people, you know, like, but it was just the, it was just the vintage, you know, it's like, that's just what happened back then. You know, it's just people, when people were getting into technology, they would go into Ham radio immediately. And then a lot of them stuck and that's awesome. And that's, that's why it's been able to persist, I think, but it is an aging population in general. So.

**Dave Jones:** Yes. Yes, it is.

**Chris Gammell:** We talked to about a couple of times too of, um, when they took it. So the technician class license, which is what I have, they, it was a couple, maybe less than 10 years ago, I think they took out the CW requirement or Morse code requirement. Yep. And that actually did a lot for the hobby because. Yes, it did. That was very restrictive. And, and we got into a discussion about that too, because, you know, there's, that's like a lot of things, right? You know, even, even just general, you know, just general electronics, right? We, you hear people talk about Arduino. I've, I've been on down on Arduino at one point, but the ultimate conclusion has been, no, it's a good thing. You know, opening up any kind of hobby in any way possible is always a good thing, in my opinion. You know, you always have people that are cranky and, oh, well, you know, back in my day, some, some people say that. I was a boy. Yeah. I was a Dwayne, I rubbish. Right, exactly. And it's like, okay, yeah, you know, that's still going to happen in any hobby in any, you know, there's always going to be codgers like that. But it, in general, you know, you can still have elite members in, within a hobby and then open it up to the general population. And it's always, it is always a net positive in my opinion. So it's a. I totally agree. Happening with Arduino as well. Yeah. I mean, you've seen it, you've seen the, you know, the hobbyist electronics market come back. So you've seen that firsthand, right?

**Dave Jones:** Yeah, exactly. It almost died, you know? Yeah. I mean, geez, who wants that? Right?

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. I'd rather have everyone using freaking Arduinos than, you know, than have the whole thing die out.

**Chris Gammell:** Right. Exactly.

**Dave Jones:** You're going to be kidding me.

**Chris Gammell:** Right. And, and I think, you know, well, I think Arduino on its own has a lot of benefits as well. So. Yep. That, that's a whole other, whole other thing. So, and we've talked about that before, but yeah, uh, hand invention was great. Uh, so it was actually a former guest. Dr. Greg Charvat, who, uh, actually had encouraged me to go. And so I got to hang out with him all weekend and one of his college buddies, Scott. Um, and then I met all the people on the, in the photo here and it was great. It was cool. Awesome.

**Dave Jones:** A grand total of three amp hour shirts here. Yeah.

**Chris Gammell:** Yeah. I probably saw about five, two of the other guys left, uh, had to leave. Right. But, um, I think I saw about five or six shirts the weekend and yeah, it was really cool. Um, the flea market is, was a sight to behold. Probably the biggest one I've ever been in.

**Dave Jones:** Um, are these out of the, are these out of the boots of the car? Sorry, trunk. Yeah. Yeah.

**Chris Gammell:** Like, like at that, uh, Wyong field day that you went to.

**Dave Jones:** Wyong field day that I went to. Yep.

**Chris Gammell:** Yeah. Uh, right.

**Dave Jones:** So they're actually boots of cars and.

**Chris Gammell:** Yeah. Well, some people set up like tents and there were some like more formalized vendors and stuff, but the, really the formal vendors were inside, but then there were some bigger vendors outside as well. Um, but yeah, man, a lot of people, I think the only way I could really tell how many people were there was they do drawing, they did drawings. And so they had ticket numbers and I saw a ticket numbers as high as about 25,000. So. Wow. No way. I think they, I think they had that many tickets sold at least. Not saying that means everybody's there, but yeah, that's a lot of people, a lot of old people. Yeah. And, uh, you know, it was weird too, because the, it was, it was skewed towards the earlier in the day. Right. So, so it goes Friday, Saturday, Sunday, Sunday is kind of a, yeah, it's a, it's a three day thing. Sunday is kind of a non, a non issue day. I mean, it would just, I actually didn't even go on Sunday. So apparently Friday morning, and maybe this was like that at Wyoming, but Friday morning, like that is the time to get there for the, that's when all the deals are to be had. Right. So when I actually, I actually got there about one o'clock on Friday, by the time I was getting there, there were already people leaving with, with their, their halls. Right. Yeah. Yeah. And, um, yeah. Yeah. And there were, there were some deals to be had. So Greg got like some 1944 radio for like, I think he paid like a hundred bucks for it or something like that. And they ended up fixing it that night in this hotel room. Oh, nice. Getting on the air and everything. And so I think I got videos. I got a bunch of videos that I still have to post, but, uh, then he got another one of like this gear driven, like all, all, it was all like gear. It was like looking at a clock inside and that was awesome. Um, yeah, man. I love radios. I was in the market for an LCR meter. Didn't see any of those. Um, I was also in the market for a function generator, but, uh, those were not the right price and the right availability. Unfortunately, eBay has kind of decimated some of the, some of the availability of stuff.

**Dave Jones:** Somebody, I think tweeted, I think it was Hamvention. Could have been Maker Faire, but I think it was Hamvention. Somebody tweeted a photo of, um, these cheap multimeters, you know, these cheap $2 multimeters and they were selling them for 20 bucks.

**Chris Gammell:** Yes. That does, that did happen a lot. You'd go, you'd go up to a table and you'd be like, they'd be asking like, like, like $400 for a tech four, six, five or something like that.

**Dave Jones:** Oh, right. Geez. I could even get one here for half that.

**Chris Gammell:** I know. Right. Well, that's the thing. And it, it, so some of it was the people were, you know, they're, they're into ham radio, but they, they didn't build anything. Right. And then basically anything with the screen, they would just mark it up and hope that, you know, they'd be able to get a lot for it. Other times there'd be people selling for others. Right. You know, and so some, some of it's just weird pricing, you know, and, and you, you didn't have to haggle a lot and you had to, you know, talk people down, but, which is some of the fun, you know. Right. Uh, but you know, it's, I think eBay kind of ruined some of that stuff, but at the other, on the other side of it, it's like, well, it also makes us available the rest of the year and better deals. So. I mean, you know all about that, right? You, you buy, you buy and sell all the time.

**Dave Jones:** I buy and sell on eBay a lot. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Do you ever buy outside the country or no? Yes. Yeah. That's, um, what I used to do all the time. That's one of my things I did. Um, uh, is I would always buy, look for the deals outside of Australia and then resell them back inside Australia for a profit.

**Chris Gammell:** Huh. How do you deal with it?

**Dave Jones:** And for fun. You know, it was, it was mostly for fun, you know, cause I like Teske. But, um, yeah, but no, I would, you know, I could easily double or triple my money on almost everything I bought.

**Chris Gammell:** Really? That's pretty good.

**Dave Jones:** Yeah. Because, uh, because a lot of Australians just won't, will refuse to buy from overseas cause they think they're going to get scammed or something. Right. So I take that risk and I never got scammed. Of course. Right. It's a bit of a myth. Yeah. Cause you know what you're looking at. Well, I know what I'm looking at. And really, you know, you buy from somebody with 10,000 feedback, they aren't scammers. Right. And I mean, it's just, you know, but yeah, anyway, there's a lot of people who just refuse to, you know, buy outside of Australia. And so you can resell them here in Australia for quite a significant margin.

**Chris Gammell:** I guess if that market's smaller than two, if there's less on the market there, then you can just charge more. Exactly. There's less on the market. And yep, that's right. Yeah. And then you get to keep whatever you want. So that's, that's good. Yeah. Yeah. Man, I never got into the eBay thing that much. I mean, I bought it. I just, I never, I never really liked it. You know, like that there was a, there was a time when it was like really, really big. I remember. And it's kind of died off a little more now, but. All right. I don't know.

**Dave Jones:** I would just love getting that bargain, you know? So you would, you would sit there for months just waiting for that, you know, sub hundred dollar Fluke 87.5 to come on sale, you know, because somebody goofed the title in the, you know, so, so everyone is searching for Fluke Molding, you know, it'd be called Fruke or something, you know, with an R instead of an L, you know, they type it wrong and it doesn't show up in the search and, you know, or they get the model, they type in the model number wrong or something like that, you know? So there's various searches. And when you see that bargain or somebody who just has no idea what they're worth and they put a buy it now price on and you manage to just grab it. Holy crap. 50 bucks. I can sell that for 500. Buy it now.

**Chris Gammell:** You know, and yeah, yeah. Yeah. Shipping doesn't even matter at that point. Right. Yeah.

**Dave Jones:** Shipping almost doesn't matter. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** But of course, that's the other thing, you know, sitting and waiting for a bargain on shipping as well. So you may actually pay above market for the unit itself in the US, for example, but then, but they, but they would offer cheap shipping. So you go, okay, I'm paying above market rate for this thing, but the shipping is really cheap. And I know that if I get it here cheaply, I can resell it for double. You know?

**Chris Gammell:** Yeah. So, yeah. You know, I was thinking about this kind of stuff too, because I've, I've, I've worked with people before and it's like, you know, like they just don't optimize like that. And I was, I was trying to imagine how you, because that is, seems like a trait that is like very engineer, not centric, but it's, it's a, it's very characteristic of engineers, right? That opt, that wanting to optimize in that situation. Yep. Yep. You know, and it does happen. It carries over into finance, but I think about the same thing with like, you know, like being on a distributor's website and want, you know, trying to figure out where that price point is. It's like, ah, you know, I could buy just 10 resistors, but it's, it just makes sense to have. Yeah. Yeah, exactly. Or a hundred or buy a whole reel because, you know, I'll just resell them or just, I, I know I'll need them. And you always have that balance point and you just kind of have to keep it all in your head. And, and I've met people that don't have that before and, and almost always in other fields. And I just wonder how, is that a taught thing? I mean, what, what, how do you get that? Is it, is it just from, you know, like, is it just the performance versus price kind of thing? Is that, is that the cheapskate in all of us kind of coming out? Is that the manifestation of cheapskateness?

**Dave Jones:** I think it's got, yeah, it's got to be. It's got to be.

**Chris Gammell:** Because Lord knows that I'm a cheapskate and I think, I think you've said that you are too. Yeah.

**Dave Jones:** And so sometimes, sometimes like I don't mind paying a premium if I really want that, if I desperately want it, I'll, you know, I'll, you know, almost pay anything to get it kind of thing.

**Chris Gammell:** But yeah, but you know, you also know the variable of your time, right? I mean, like, you know, like, well, sometimes that, that doesn't matter, right?

**Dave Jones:** Sometimes it's my hobby. I just do it for fun. Yeah. Well, yeah. Yeah. So, yeah.

**Chris Gammell:** Yeah. So you always kind of hold those variables in your head. You're kind of balancing and, but I don't know, I was thinking about how, how you could teach that to someone who's like a librarian or something. I don't know. Maybe it's just not as relevant in other fields.

**Dave Jones:** Well, yeah, it's not. They go, why do I need to learn this? It's, you know. Right.

**Chris Gammell:** But then they have skills that I don't have, like empathy, you know. Right. Got it. Whatever the hell that feels like. And in my case, tactfulness, you know, or something. Yeah, exactly. Public speaking.

**Dave Jones:** Some useful life skill that, you know, I just don't need.

**Chris Gammell:** Right. How to iron my shirt. Right. I know. I know. Thank you.

**Dave Jones:** We're a weird bunch. I'll see you in the news. Yes, we are.

**Chris Gammell:** We are odd ducks. So, yeah, we, but yeah, Hamvention was fun. A lot of good deals and good times and beers were drank and stories were swapped. And I hope, I hope, I hope, I hope we can do many more meetups in the future because that was honestly the best part. I mean, like getting to meet people. Yeah, it's cool. You know, that's really just great. I mean, I got to meet a lot of cool people.

**Dave Jones:** I really enjoyed when the trade show last year where I, you know, had my stand and got to meet everyone. That was pretty cool.

**Chris Gammell:** Right, exactly. It's like, because, you know, like I'm always amazed at like how many cool jobs are out there. You know, so I'd be talking to people, swapping stories, whatever. And I'm like, really? You work on that? Even if it's just a hobby. Like, like Brad, one of the guys I met, he's just like, oh yeah, you know, I got the six foot satellite dish in my backyard and I, you know, do these crazy ass radio, the race. He's doing like radio telescopes and stuff like that. I'm just like, really? This is, you know, like some of the things that I'm like, wow, that I just can't fathom some of that stuff, you know?

**Dave Jones:** Yep.

**Chris Gammell:** Same thing with work. You know, some of the people that just were working on cool, cool things. And I, I really, so I, I feel really bad because I can't remember his name. Um, but he, he gave me something that is really cool and I, I will definitely try and find out his name. I emailed a couple of people to try and remember, trying to figure it out. But so this is a trend. He works at Wright Patterson Air Force Base, which is in Dayton, right? And, um, and so every group, and he works on like military research and stuff like that. And he had a coin with him and I'm like, well, what the hell is that thing? He showed it to me and, and I'm like, what the hell is that thing? And he's like, well, here. So he gave me a second one that he had and it's amazing. It's, it's called a challenge coin. Have you ever heard of this? No. It's apparently, so apparently it's a thing in the States, but it's different, different divisions of, I guess, military and research and everything else. They all have their own branded coin. And this thing is pretty, pretty hefty. Yeah. So it's a challenge coin, right?

**Speaker ?:** Yes.

**Dave Jones:** The coin thing in America is really big. It's really big in the, all, all these geo coins and stuff. If you're into, uh, caching, if you're into geocaching, sorry, geocaching for you, you know, every team has their own minted coin.

**Chris Gammell:** Oh, that's cool.

**Dave Jones:** You know, to, to get a team's, you know, coin, a rare coin to find one in a cage is a big deal and all that sort of jazz, you know? And yeah. Anyway, go on.

**Chris Gammell:** So that's not quite the same thing here. It's a little simpler, but so the coin itself is amazing, but the challenge coin is if you're out and you meet someone from a different division and you challenge them and they do not produce their coin, they have to buy you a drink. Oh, right. Which is a great tradition. I just love traditions like that. Right.

**Dave Jones:** So you've got a challenge as in just, do you have the coin on you?

**Chris Gammell:** Do you have your coin on you? Yeah. Oh, you work there. Do you have your coin on you? And I feel terrible that I don't remember his name. I was talking to him for a little while. But he was so nice to give me a coin and it's so cool. But thank you, mystery coin giver. So cool. And I just love traditions like that. I think that's really fun. It's just really cool.

**Dave Jones:** Hey, you've just given me an idea for a perk. There you go. A useless perk for my upcoming crowdsource funded project.

**Chris Gammell:** Oh.

**Dave Jones:** I could have my EEV blog minted coin with my head on it.

**Chris Gammell:** That'd be cool.

**Dave Jones:** Why the hell you'd want one? I have no idea.

**Chris Gammell:** Dave bucks. Right. And then when you're doing some video, right, you could hold up the coin and be like, buck this.

**Dave Jones:** No. Sorry. No? Is that too? No. No. That's too American. Yeah.

**Chris Gammell:** Well, I like that idea though. Everyone does minted coins.

**Dave Jones:** Right. Yeah, you do. Very cool. You think it's all right for a perk?

**Chris Gammell:** Yeah. I think that's a great idea. And that's coming up, huh? That's going to finally happen?

**Dave Jones:** That's going to finally happen, yes. My first crowdsource funded project. Why? I don't know. Just because, you know, everyone else is doing it. Dave doesn't have enough to do. Yeah. Yeah. And yeah, I can see how much work is involved in this. Like I'm, you know, I've set up my account. I'm not using Kickstarter. I'm going to use the Australian version Possible. And yeah, I'm setting up my account on there. And I'm going through the motions of putting the whole thing on there. And I have to do a video for it. And I've got to, you know, do photos. Yeah, I've got to do a video. Go figure. But yeah, pain in the ass, all right? I've got to shoot another video. I'm sick of doing videos.

**Chris Gammell:** Yep.

**Dave Jones:** Anyway, yeah, I can see how much work is involved in setting up a good crowdsource funded campaign.

**Chris Gammell:** Yeah. You don't usually see single person teams, even when it's like a single focus kind of like for like when it's an artist and, you know, they're doing like an album by themselves or something. Usually there's a team helping out in some capacity, you know, family members or, you know, producers or something like that. So, yeah, it's no small task for sure. And especially, you know, I remember Stompy, the one that I backed, that walking hexapod robot. I remember they said that they, you know, if you do well, you know, you have a lot of stuff to send out, you know. And it's not necessarily, you know, the ordering of stickers or T-shirts and everything else. It's the logistics of getting it to people, you know, and getting the right address.

**Dave Jones:** Well, that's the thing. I mean, you know, if my, I don't know how popular this would be, you know, it may not be that popular. But anyway, if it does turn out to be popular and I have to ship a thousand of them or two thousand of them or something, you know, I may have to look into hiring some center, you know, someone who does the fulfillment for me. So I just give them a list of names and addresses and, you know, this fulfillment company will, you know, pack and ship them. Um, because me packing and shipping, you know, a couple of thousand units, I'd, you know, have to stop the blog for a month and.

**Chris Gammell:** Yeah, exactly. You know, it's, it's no small task. And actually we're, so we're seeing some of this stuff too for like crowdsource type of stuff, not just for the, the logistical, you know, pack and ship kind of stuff. They're actually starting to see, I'm starting to see some of these things pop up services for helping develop hardware after people put hardware like ideas on there, like actually, you know, setting up factories. It's kind of like what Scott Miller does for dragon, but like on a smaller scale, just for a campaign. And it's like, it doesn't seem like it would be a very, I mean, it seems very, very niche, you know, like just very constrained of how, how useful might be to the, you know, if you actually scale to a full company, but yeah, it's out there, you know, there's, there's different cloud fab type services or what is that called? Cloud fab was something else. It was a, there's something with cloud in it.

**Dave Jones:** I know what you mean. Yeah.

**Chris Gammell:** Yeah. And so it's, it's interesting to see that stuff.

**Dave Jones:** And you get everyone to handle it all for you and all that sort of jazz, you know? Yeah. But I've, I've, I've got a local guy who says he wants to do everything for me, you know? Oh, there you go. He wants to, you know, pack, test, ship, do the whole, you know, the whole, the whole

**Dave Jones:** We should start a pool.

**Chris Gammell:** We should start a pool for when kickstart, when a crowdfunding falls out of favor, you know? Right. Okay. You know what's going to happen, right? Ebbs and flows.

**Dave Jones:** Well, yeah, maybe, but well, I don't know. Is it, is it too big to fail now? Maybe. Until the government regulators come in. I mean, that's the next step, right? Is the government regulators will come in.

**Chris Gammell:** Well, and that will happen in the States when, when that jobs. Oh, the jobs act. It kicks in. Right. Yeah. If, if it kicks in ever, I mean, I think it's still, it's still in limbo, but yeah, if there's any kind of, if it's just money type of thing, when it's not products and it's people are investing money into companies instead of just buying, you know, pre-purchasing and supporting companies like that, then there will definitely be some stuff in there, but I think it'll really have to take, it'll take some pretty terrible Bernie Madoff style swindling, I think, for it to fall out of favor. Yeah, yeah, yeah. It's going to happen in a big way at some point. And it's just a matter of time. Not to be a pessimist, but come on.

**Dave Jones:** Yeah, no, no. Yeah. You can just see something. Hucksters everywhere. You know. You're right. Speaking of someone who's, I think, probably going to make a mozza on a crowdsource funded campaign, Jerry. She's announced who, who hopefully we'll have on the show soon.

**Chris Gammell:** Yeah. We're hoping for next week. We're still working on scheduling with her, but maybe by next week. Yeah.

**Dave Jones:** She has announced that she will start a campaign for her new augmented reality glasses. Yeah. Thingamabob.

**Chris Gammell:** Thingamajiggy. Sorry, Jerry.

**Dave Jones:** It's a thingamabob.

**Chris Gammell:** Yeah. Well, until it's, you know, for sale, then it's a thingamabob, you know? Right.

**Dave Jones:** And then, yeah, I mean, that's the classic, you know, example of, yeah, she'll probably, there's a lot of gamers out there who'll probably lap all this stuff up. And I think it seems to be a very successful, yeah, I think it could be a very successful Kickstarter campaign. Yeah. But then the problem is, you've got to produce it.

**Chris Gammell:** Yeah.

**Dave Jones:** And therein lies the problem, you know?

**Chris Gammell:** Yeah. Well, I'm very much looking for it. It's not easy. I talked to her a little bit a while back before it was all public about stuff. And, you know, we were talking about the, you know, like, I just wonder if she's going to be able to put it in an ASIC, right? Because they have a very aggressive price target, too. I think I saw publish 200 bucks or something.

**Dave Jones:** She wants to sell 200 bucks. And it's not just the glasses. Right. It has to include the screen and, you know, everything. There's a lot of kid in there. So I think her margins are going to be slim, you know? Yeah, maybe.

**Chris Gammell:** But if, you know, if she licenses it to people, you know, or companies for developing games on, then that's where the money is. But, yeah, we can talk to her about it when she gets on here. But I really look forward to, you know, hearing about the tech, too, because we know she's big FPGAs and stuff. And I remember talking to her a little bit. She was talking about just the arrays of FPGAs she needed to implement stuff with. Right.

**Dave Jones:** Well, she is working on an ASIC. I read it in an article that she's working on a video processing ASIC or something like that.

**Chris Gammell:** Right. Yep. Very cool. And she's working with her partner, Rick, as well. So that's important to mention there. Rick's doing software and she's doing hardware. So very cool stuff.

**Dave Jones:** But the whole fascinating thing, if people haven't heard, this is what stunned me and a lot of people, right? Is that Valve, her former company, actually gave her the technology? They said, here, we don't want it anymore. Take it. It's legally yours. Do whatever you want with it. We won't sue you. And, you know, I thought, wow, that hardly ever happens in this industry.

**Chris Gammell:** Yes. That was very different.

**Dave Jones:** That was a big deal.

**Chris Gammell:** Yes. I agree. And, I mean, I think that speaks highly of, you know, them. Oh, hugely.

**Dave Jones:** Because Valve. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Because they knew they weren't going to do anything with it, right? And if they just kept all the technology to themselves, it would just die out in the back room somewhere, right? It'd never see the light of day. Why not just give it to someone who's enthusiastic and it promotes the industry?

**Chris Gammell:** But they're also smart. Well, I think it's even more than that, though. I think. What is it? Because, I mean, releasing a technology like that, right? I mean, it's basically releasing a potential competitor into the wild, right? I mean, that's the really interesting thing to me. It is. But the smart thing is. Because they were betting on one. Okay. Go ahead.

**Dave Jones:** They aren't just competitors, right? They could be an ally.

**Chris Gammell:** That's true. Yeah. That's very true. Right? Because they're a gaming company, right? Yeah. That's true.

**Dave Jones:** Yeah. They could, maybe, they're going to get, you know, favorable, you know, licensing deal from them in the future or something like that.

**Chris Gammell:** Yeah.

**Dave Jones:** You know?

**Chris Gammell:** Well, I agree. It is very, very interesting stuff. It's very cool. And I hope Jerry can make it on next week. Last I talked to her, she was very busy setting up meetings with people. So, I'm sure there's a lot of interest out there.

**Dave Jones:** Meetings.

**Chris Gammell:** Yeah. Oh, yeah.

**Dave Jones:** All the fun has just instantly died out of it. I know, right? Yeah.

**Chris Gammell:** Oh, man.

**Dave Jones:** Oh, boy. Yep. Screw that. Meetings. Yeah. I'm glad I don't have to do that anymore. Oh, yeah. You don't have to do that anymore, huh? No. It's funny to say, well, you know, I just have little meetings with myself in the corner and talk to myself. Talk to yourself.

**Chris Gammell:** Yeah. You should record a video yourself and then play it back and talk to them. Yeah, right. Yeah.

**Dave Jones:** The great thing is, though, is that I always win.

**Chris Gammell:** That's true. It's like playing tennis. Well, no, I guess that's like the Mitch Hedberg joke. Where he talks about how he hates playing tennis against a brick wall because brick wall always wins.

**Speaker ?:** Right.

**Dave Jones:** Exactly. Oh, boy.

**Chris Gammell:** You could build a robot to argue with you.

**Dave Jones:** Once again, with my infinite amount of time and resources, I will build myself, eh?

**Chris Gammell:** Well, if you don't have time to build your own robot, you could also purchase a robot kit from our sponsor, Jameco Electronics. I like that for... That was impressive. Yeah.

**Dave Jones:** That was impressive. He's a true professional, folks.

**Chris Gammell:** Yes, that's right. True radio professional. Club Jameco.

**Dave Jones:** Although you are 15 minutes late. Sorry. Oh, well. It was supposed to be in the center of the show. So you're supposed to, you know...

**Chris Gammell:** Yeah, we'll just have to make... We'll just have to go an hour.

**Dave Jones:** Guide the show towards the center sponsor segment.

**Chris Gammell:** Well, I'll just carry that show to the hour and a half mark. We'll be fine then. No complaints from the audience. All right. Yeah. Our sponsor, Club Jameco, continues to be a sponsor, so we thank them for that. If people don't know, you can actually submit your own kit idea and you can make up to 10% on it if you get it approved by the community. And then also, if you actually just submit a project brief and that gets approved as this isn't a blank sheet of paper, then you also get a 10% off coupon on your next order at Jameco. At which point, you could purchase our kit of the week, which is this little robot kit.

**Dave Jones:** It's a robot. What's it called?

**Chris Gammell:** The J-bot robot kit. Yeah. V2. So it's...

**Dave Jones:** It kind of looks like... Wally!

**Chris Gammell:** Wally! Yeah. I like that movie.

**Dave Jones:** With the stereo ultrasonic eyes, you know? Yeah. Yeah, exactly.

**Chris Gammell:** The ping sensor and everything. So it looks like a cool little kit. I mean, it's Arduino-based and then the base is included. So it's not as much soldering, but then you can also integrate your own electronics on top and everything because it does have a breadboard and you could add other sensors and whatever you can dream up to put into the Arduino. So very cool kit. Very nice. Check it out. Yeah. Check out clubjameco.com slash theamphour and you'll be able to find that kit and then more info about submitting your own kit. Fantastic. All right. Did you see another... There was actually another robot kit and other kits from the Arduino team, actually. They had a bunch of announcements this weekend. Did you see that?

**Dave Jones:** Oh, I already heard about the Wi-Fi one. It's like, yeah, Arduino's got Wi-Fi and Linux. Oh, yeah, blah, blah.

**Chris Gammell:** Well, I thought the... Linux was interesting. I mean, I wouldn't have thought to put... Linux and Arduino don't really go together in my brain because...

**Dave Jones:** No, because that usually doesn't have the horsepower to run it.

**Chris Gammell:** Right. Well, yeah. And the MM... I mean, to do full-blown Linux, you need a memory management unit and I don't know which...

**Dave Jones:** Well, this isn't full-blown Linux. I think this is a special... Oh, it's like embedded Linux. Like Micro-C type Linux. Yeah, cut down. Yeah, I don't know what the... Hang on. It's here somewhere.

**Chris Gammell:** Yeah, it's... I don't know. I've worked with Micro-C a little bit before. Micro-C Linux and other... I think there's other ones out there. I think some of the early... Other early dev boards had, you know, reduced Linux without the memory management unit. And not like I know what I'm talking about.

**Dave Jones:** It's running Linino. Linino. You're starting to stretch it with these names. Linino. Linino. Yeah, I know.

**Chris Gammell:** Still like the product. The names are getting a little out there.

**Dave Jones:** So, it's a MIPS GNU Linux based on OpenWRT.

**Chris Gammell:** OpenWRT. There you go.

**Dave Jones:** For all you aficionados out there. Okay. Who will know what we're talking about because we have no idea, do we?

**Chris Gammell:** Yeah, no, that one is just... I think that might be the Wi-Fi stack or something like that. It could be.

**Dave Jones:** Yeah, stack or something. Yeah.

**Chris Gammell:** Yeah, okay. Well, that's interesting. Yeah, and you know, it makes sense that they would need a little bit more horsepower for, you know, actually doing Wi-Fi. You know, you look at a lot of the cards that, you know, like a lot of the modules that plug in to do Wi-Fi or, you know, Bluetooth and other stuff like that. There's usually a secondary process on it and they're just doing... Oh, yeah, of course. ...a stack, you know, and handling all the communications. And then you just talk to it through Spy or I2C or something. So, it's...

**Dave Jones:** Well, if this is all done in the AT Mega, I mean, how many resources are left over to actually run your sketch after doing all the stack internal? I mean, there's a reason why those Wi-Fi modules have their own dedicated processing is because... Yeah.

**Chris Gammell:** You know, so you offload all that, so... And I think more so you just get into just complexity issues, right? I mean, like, Arduino as a starter platform is great because it's, you know, it's like... It's a sequential... Easy way... Easy to write a sequential program that just runs in a loop. But when you start doing Wi-Fi type stuff or networking type stuff, sometimes you need to get into, like, real-time operating systems and...

**Chris Gammell:** ...or, you know, other types of... If it's full-blown Linux, then it's a real operating system, right? It's not deterministic at that point. Yep. So it gets... It could get messy, but, you know, neither of us have enough details on that stuff. No. The interesting thing is that it's, you know, it's just that they're outputting... That they are moving in that direction. So I wish them well. Fairly obvious. Yeah. Yeah. That's funny about the name, though, because I remember at... I think it was the first Open Hardware Summit. Massimo Banzi was up on stage. It's like... This is going to be my terrible Italian accent, but he's like... You need to stop calling Arduino something Arduino. It does not mean what you think it means. Because, like, someone named something, like, something Arduino, but it ended up being, like, a swear word or something like that.

**Speaker ?:** Oh, right.

**Chris Gammell:** It was really funny at the time. I'm sorry about my terrible accent, but...

**Speaker ?:** Right.

**Chris Gammell:** It was, like, just the way you said it, too, you know, it was just really good.

**Dave Jones:** Got it. So how many, for our Italian listeners out there, how many Italian words end in Duino?

**Chris Gammell:** Yeah, right. How many bad words, right?

**Dave Jones:** How many bad words end in Duino?

**Chris Gammell:** Yeah.

**Dave Jones:** Because I'm sure there's, like, hundreds of them. Like, not words, but there's hundreds of products. I'm guilty of it. I've got a, you know, a micro Duino RGB thing. Oh, yeah. Had Duino in there, and, you know, it's... Yeah, yeah. People look for the... Hundreds, hundreds.

**Chris Gammell:** Just kind of to carry on the success, right? And having the name recognition of sorts, right? Yep. Yeah. And people should remember that you can't actually call an Arduino unless it's licensed by them. So that is very specific. Yes, it's a trademark. Right. That's a trademark thing. So I guess that kind of skirts the issue, but, yeah. Sometimes you just look like you don't know Italian. Right. Yeah. Oh, dear. Yeah. So...

**Dave Jones:** They've got, well...

**Chris Gammell:** They also had a robot. I didn't see much about the robot, but they also have a robot kit, so...

**Dave Jones:** Arduino have a robot kit?

**Chris Gammell:** Yeah. I think they're working with partners and stuff, so...

**Dave Jones:** Right. Oh, there you go. Yeah, they do. They're working with lots of partners to do... A lot of this is not in-house. It comes from various partners and things like that. Mm-hmm. So it's just not 100% in-house stuff. They're always teaming up with other people. Yeah, which is great. That is a very... Yeah, of course.

**Chris Gammell:** ...very powerful thing to do, I think, you know? Yep. Helps expand your reach and your integration with other things, so that's good.

**Dave Jones:** Absolutely. I mean, there's only so many projects you can do in-house, really.

**Chris Gammell:** Oh, yeah, yeah. So, yeah.

**Dave Jones:** It does make sense.

**Chris Gammell:** Yeah, it's all about what you want to focus on. Yeah.

**Dave Jones:** What's this crap about Rat Shack are going to be selling... Rat Shack? Yeah, well, speaking of...

**Speaker ?:** Rat Shack.

**Dave Jones:** Rat Shack. Radio Shack.

**Chris Gammell:** ...co-branding and everything, right? Or Tandy, as it was called here. Back in the day. Radio Shack for the... Back in the day. For the Yanks. Those not in the know, right? Yeah, them and Make are going to start co-branding stuff. And really, I think it just means that Make is going to get more... I mean, they already have a bunch of stuff. If you go into Radio Shack today, at least near me, I mean, you can... They have a section, usually, with, like, Make Electronics type stuff. Wow. Yeah. So... But it's good. I mean, because it's like, you know, you look at Radio Shack and... That was dwindling to be their only electronic stuff for a while. So, you know, even just having a small display is a good step forward. And if they're focusing on that stuff...

**Dave Jones:** Can you still buy the two resistors in the blister pack for... Yeah, yeah. You got to do that. Right. Yeah.

**Chris Gammell:** That's painful, man. I've paid 99 cents for a diode before. Yeah.

**Dave Jones:** Yeah. So have I. Yeah. Back in the day. Yep. I'd save up my money and I'd go to Tandy and I'd buy my, you know, a couple of chips and my few resistors and I'd build up my circuit on the breadboard and...

**Speaker ?:** Yep.

**Chris Gammell:** Yeah. Yep. That gets better too. People starting out. When you buy... When you start to buy more than one thing, it gets better too. Just like looking at schematics.

**Dave Jones:** Yep.

**Chris Gammell:** You have a...

**Dave Jones:** How do you store the shit though? I still have not... You know, I was talking about earlier in the show about, you know, oh, you'd buy 50 components because you might just need them. But then where do you put them so that you can retrieve them easily later? I'm just...

**Chris Gammell:** Yeah. You know, I was actually talking to someone about that. I sold it. At Hamvention. They were saying that... Because we were talking about resistors and, you know, we saw that there was someone selling, you know, resistors off the reel at some ridiculous price. Right. And they were saying, you know, like if you go on eBay, you can get, you know, pretty standard resistor values. Nothing fancy, you know, like it won't be like the highest E-series resistors, but, you know, you can get a pretty good chunk. And they said it was like an entire series, like zero ohm up through like a mega ohm or 10 mega ohms.

**Dave Jones:** Yeah, you can buy entire kits. I've bought kits. Yeah. Yeah.

**Chris Gammell:** And they said it was like 20 bucks. 20 bucks for that and 40 bucks if you get it in a binder. Yeah.

**Dave Jones:** And they give you every value from, you know, in the E24 series.

**Chris Gammell:** I like the binder method a lot. I don't like the drawer method for SMT and having cut tape. Yep. For through hole resistors, man, I don't even know. That is an innovation that still needs to be a carousel or something.

**Dave Jones:** Well, no, resistors and caps are pretty easy, right? Yeah, you just have your drawers and you label them and that's, you know, Bob's your uncle, but, you know, things like chips.

**Chris Gammell:** Yeah. Well, you could do the same thing with chips. You know, you can do the label and then a little black foam and stick them in the foam

**Dave Jones:** and bottom of the drawer. Yeah, but then you've got to categorize them and categorize them, sorry. And, you know, do you categorize them into just op amps or do you categorize them into categorize them? I made the same mistake again. You know, how do you categorize all these obscure parts that you get? Because most designs, like you're not going to, well, most of my designs end up having parts that, you know, I never have in my junk box because they're not really being parts. They're always, you know, very specific. You know, half the projects in my latest, half the components in my latest project will be very specific.

**Chris Gammell:** Yeah. You know, well, you can continue doing the method you do. I mean, I think it's a good method in general. Just do it by project and then have the box for the project.

**Dave Jones:** By projects and have a box with all the components in the, yep. And then you've got to remember, yeah, I used that. Oh yeah. I used that component in that project. So I go look in that project box. And at the moment, it's probably the only way that I do things.

**Chris Gammell:** I think that's an effective method. I mean, it's probably the most likely for how you work. It does kind of work, yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** You know, it's, I don't know. It depends what kind of work you're doing that too. I mean, if you're just kind of tinkering, then yeah, you want the, maybe you want just the pile of components and you want to dig through it or, you know. But it's usually a diminishing returns of how much time you want to spend on the organization system.

**Dave Jones:** Organizing and, yeah, exactly. Yeah.

**Chris Gammell:** I saw in Jack Gansel's newsletter today, which is a great newsletter and one of my favorites. It's the Embedded Muse. But someone wrote into that about talking about PartKeeper. Did we ever talk about that on here? PartKeeper. I don't think so. There's like no E. It's like PartKeep and then just an R. Right. Right. But it's a Linux-based tracking system. It's basically like a fancy spreadsheet for like doing, but it's actually like a program for doing like tracking and then you can host it on a server. Yeah. Inventory tracking.

**Dave Jones:** Tracking your hobbyist inventory of all your hobbyist parts. But once again, how much effort goes into maintaining something like that? You know what I mean? Well, no.

**Chris Gammell:** The maintenance would be the easier part with that, right? Because, you know, once you basically, it would be like having like a part stores. Like what is that called? Like, you know, companies sometimes have like a cage, you know? Like you go back to the cage and you sign out parts and everything.

**Dave Jones:** Yeah, but I hated that. I don't want to have to do that in my own bloody lab. Like every time I get a resistor out, I've got to go over and update the database. No, no, no, no. Screw that.

**Chris Gammell:** So the thing that would be good though would be to, okay, here is the next Kickstarter idea I want to see. Oh God, here we go. Get your notepads ready, kids. I want to see a low cost.

**Dave Jones:** You too can steal Chris's ID. Yeah, right. Get ready. Please do. Here we go.

**Chris Gammell:** Tie part keeper to like a dispenser, right? You have like a little, you know, like a candy dispenser or something like that. And just, so you have to type it in, right? And then it just craps out the parts to you, right? You just hold out your hand and it just throws out the parts to you like a vending machine. You know, that's one way to do it. It would be a truly electronic method of doing so, right? And if you've got a low cost mechanism, you know, you could potentially do it. I'm just saying.

**Dave Jones:** Why not just hire 10 trained monkeys to sort and gather all your parts for you?

**Chris Gammell:** Yeah, right, right, right. Well, eventually one of the monkeys will end up eating one of the components and then your count is off and then you're screwed. Exactly.

**Dave Jones:** Because you thought you had one in stock because you trusted your stupid dumb ass database.

**Chris Gammell:** Yeah. Yeah. That's like, you know, I keep a little coin jar with like a counter, you know, as you put a coin in and it counts stuff. And I was like, oh, you know, I told my wife the other day, oh, we hit like 45 bucks as I put a quarter in. And she's like, oh, that's all wrong. I take change out of there all the time, right? It's the same thing people do with parts, you know? Yeah. You know, like everybody does that when there's like a, when there's a parts room and it's like 8 p.m. and you're the only one there. You're not going to fill out a parts form for requisitioning parts. No, no, no.

**Dave Jones:** It's just going to nick the part. You're just sneaking in the back. But you need to do your job, you know? Yeah.

**Chris Gammell:** Oh, I'll tell them tomorrow. You never tell them tomorrow. Yeah, yeah, that's right. You know? And then they do the count and then everybody gets in trouble. And, you know, of course I never did that, but, you know, I've known people who do that. But honestly, I've only ever had that at places where there's manufacturing on site. There's never a parts room unless for, you know, when there wasn't manufacturing on site, then there wasn't a parts room because there's no steel room.

**Dave Jones:** No, I've worked at a company. Every company I've had at has had a parts room and we didn't do in-house manufacture of, you know, boards.

**Chris Gammell:** Oh, okay. What?

**Dave Jones:** No, it'd be for like servicing and prototyping.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Yeah, no, just servicing, prototyping. And usually, you know, and often back in the old day, we used to have a full-time lab person who would take care of that, you know? Right, manager. We'd have a lab manager of, you know, yeah, and they just sort of keep it all sorted and stocked up and, you know? Yep. And I've got to admit, it's very handy when it's in place, you know? You can just walk over the drawer and, you know, yep. And it's there.

**Chris Gammell:** Yeah, yeah. If there's someone there cursing you after you didn't, you know, didn't fill out the little card, the Kanban card once it's empty or something, right? Everybody's done that one. Please fill out this card once the drawer's empty. Yeah, if I don't care enough to fill out the card, you're probably not going to know about it until the next time I start screaming about why the drawer's empty, you know? But with this idea, if you had like a little weight sensor in there, you could do inventory management. You could, come on, man. Someone's got to do it. I will pay at least $25 for this magical device.

**Dave Jones:** For this automated, magical automated system. And if you pay $50, your perk is a free 3D chip printer. Yeah, of course. Right.

**Chris Gammell:** Why dispense parts when you can build your own? Right, yeah.

**Dave Jones:** Oh, man. Oh, no, come on. We're really scraping the barrel alarm.

**Chris Gammell:** No, we've, no. This is important stuff, man.

**Dave Jones:** This is important industry talk, huh?

**Chris Gammell:** Yes. You never know when you need to self-distribute parts, you know? Even though I don't get a lab manager anymore, nor I just keep my own parts these days, so.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** I just have the box, you know? Just the one box that I have to dig through each time I need something.

**Dave Jones:** Oh, boy. Speaking of 3D printers. Yeah. Kind of. Yeah. Buddy has done a teardown of the new Formlabs 3D printer. Which, if you remember, I don't know. How much did they raise on Kickstarter?

**Chris Gammell:** Oh, I think a million plus.

**Dave Jones:** A million plus, was it? Yeah. There it is. Yeah. I'm going to call it up. I'll be able to tell you precisely. 2.945 million. Wow. Almost 3 million smackers. Of their $100,000 goal.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. That is a lot. And, you know, that's only 2,000 backers, right? You know? Yeah. Right.

**Chris Gammell:** Because they cost, like, $2,200 a piece or something?

**Dave Jones:** Yeah. $2,500. Yeah. $2,500. Okay. Yep.

**Chris Gammell:** Yeah. And this was, I mean, this is a very precise printer, too. I mean, it was a stereolithography. And they got them out, too. That's the other impressive thing. I think we mentioned it at some point.

**Dave Jones:** That's what I'm impressed at, is that they're actually, well, they're not shipping production units yet, but Bunny got a, you know, a beater unit. Early. Yeah. So, yeah.

**Chris Gammell:** Although for a beater unit, it looks pretty nice. I mean, it's, this is.

**Dave Jones:** Yeah. It comes in a nice professional box, and the unit itself looks great, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** Very cool. Very sort of 70s vintage retro orange Perspex cover on it.

**Chris Gammell:** Oh, yeah. It reminds me of, I used to have a Lego kit that had that same kind of glass. Right. Yep. Orange Pyrex. And they do that for blocking out light, because it's a light-sensitive goop. But, you know, it's, it's cool. Yeah, it's cool. Yeah. And, of course.

**Dave Jones:** It looks very professionally put together. I'm very impressed, because I know how much work goes into producing such a kit. Yeah. Well, it isn't a kit. It's a finished product. I mean, you don't buy a kit of parts. It's, you know.

**Chris Gammell:** Yeah, I think this one would be a bit difficult if it was a kit. But, yeah. It's cool that you got, you got an early version. I mean, it looks like it's a two or three board assembly, you know? And they've got a lot of precise stuff in there, too, you know? Like, they actually have to form a laser.

**Dave Jones:** Oh, lasers and mirrors and, yeah, yeah, yeah. All sorts of stuff.

**Chris Gammell:** Small tasks, so.

**Dave Jones:** There's lots of trim pots in there, too.

**Chris Gammell:** I didn't see the trim. On the power supply board or on the main board?

**Dave Jones:** Motor drive is by the looks of it.

**Chris Gammell:** Oh, okay, yeah.

**Dave Jones:** They're tweaking some stuff.

**Chris Gammell:** Yeah. That's fun. I've never had to do calibration like that, but I've heard stories about the magic technician who knew just how many turns to go, you know? Yeah, that's it. That's right.

**Dave Jones:** But, yeah, I'm very impressed that they got this product out, you know?

**Chris Gammell:** Yeah, scaling will be the next challenge.

**Dave Jones:** It probably needed all of that money, you know? It probably needed all that money. I don't know how much profit they'd end up getting in the end. Well, because it's a very professional-looking product. It just takes a lot of money to perfect that. They wouldn't have got that bang first go. You know? They would have, you know, gone through a few iterations and, yeah, it's just very impressive. I like it.

**Chris Gammell:** And we should also, since we borrowed the Bunnies review, he also hawks the position at the bottom that they're looking for a double E, so if people are interested in 5,000 double E's clamoring for the same position at a cool new company. Although I don't think these, you know, they're MIT grads, so I think they're going to be looking for top-notch, and I think the amp hour can supply it, so go for it.

**Dave Jones:** And yes, folks, they are late.

**Chris Gammell:** Oh, of course. As all these projects are. Oh, yeah. Well, yeah. Packing and shipping takes a long time. Did you see this Intel Science Fair stuff, speaking of new technology? I've got it open here, and what, is it students? It's students, yeah. So every year, Intel does a competition for Science Fair type of stuff, and then they give the winning students scholarships towards whatever college they're going to or towards their research. Yeah, it's great. I mean, the first story I saw on it, actually, the reason I got really interested in it, someone sent me a story, and it said it quoted the winner's name as Gordon E. Moore, and I'm like, whoa, that is a hell of a coincidence that the winner of the Intel Scholarship is named also Gordon E. Moore, and no, it turns out, I forget what his name is, but it's definitely he's from Ukraine, I think, or something, and his name is definitely not Gordon E. Moore. He won the Gordon E. Moore Prize. E. Moore. Right, I got it. I got it. Ah, yes. Internet reporting, folks. But the interesting thing was, and it was Guan on Twitter who sent me this, but it was because the runner-up, the first runner-up was a supercapacitor who claimed, it was a chemistry student who made supercapacitors and, you know, claiming that it's going to revolutionize cell phones and charge cars and everything. And I'm like, oh, okay, I'll check this out. And then you kind of dig in a little bit, like, after charging the supercapacitor for 20 seconds, while the news reports said it could charge a cell phone, it's actually, it could light up an LED.

**Dave Jones:** Right, yeah.

**Chris Gammell:** No. While the feat itself is actually, you know, making a supercapacitor is actually very, very impressive for a student.

**Dave Jones:** Yeah, yes, it is.

**Chris Gammell:** But once again, the media kind of...

**Dave Jones:** The practical implementation of the finished product, yeah.

**Chris Gammell:** Well, I think it's just, you know, the telephone aspect of, oh, someone, you know, made something groundbreaking. Well, they made something very amazing, but it, you know, it's not changing any technology anytime soon. So, very, very cool tech. I'm really glad Intel does this stuff, though. And they get tons of applications, like 1600, I think. Wow. Jeez. Yep. Very cool.

**Dave Jones:** But that's always the way, isn't it? I mean, companies, well, you know, media, I guess we're...

**Chris Gammell:** Yes, we're in that as well. We've been known to speak here and there.

**Dave Jones:** We're loved in that, I'm afraid. But, yeah, they always, you know, they'll do an article on some, you know, somebody's done some research on a new battery technology or something, and they go, oh, it'll be able to, you know, within, you know, a year or two, we'll have a new battery technology. You know, of, you know, smartphones that run for a month or whatever, you know, on a single charger. It's like, it's bullshit. They've just done a little bit of research and you're just extrapolating, you know, or all the people that are doing the research. They're also guilty sometimes, you know, often. People who are doing the research, they just extrapolate thinking that their little test sample or whatever can, you know, is going to be linearly extrapolated out to, you know, kingdom karma. It's just ridiculous. Right.

**Chris Gammell:** Right. And at this, we have one user on our website now, and next week we had, the next week we had 10 users. And at this growth rate, we will have more people than the planet in about three months. That's right. That's right.

**Dave Jones:** Yep. That's how it goes. The only step in there that's missing. Every entrepreneur, every researcher in every field on the planet is guilty of this, I think. Oh, yeah.

**Chris Gammell:** Well, the only step in there is also swindling some VCs at some point as well, getting, you know, the $100 million valuation as well. Right.

**Dave Jones:** So they're the smart ones, right? The smart ones are the ones who take advantage of the bullshit, right?

**Chris Gammell:** Take the money and run. Yeah. Yeah.

**Dave Jones:** See, nobody takes the money and runs anymore. You know, that's old-fashioned scamming. You know, now it's take the money and waste it, you know, to actually spend and try and have some fun and work on your widget for a year and hire all your friends. Yeah. And then just load it all. Oops, sorry, we ran out of money. Oh, well. Yeah.

**Chris Gammell:** It's a risky investment, I guess. Good luck.

**Dave Jones:** Next startup.

**Chris Gammell:** Yep.

**Dave Jones:** Oh, dearie.

**Chris Gammell:** Speaking of students and early technology, there was another story that I took some general interest in this. So apparently, it's for computer science, but Georgia Tech, Udacity, which is an online, like, massive online open courseware site, and then AT&T, who's helping sponsor it. So they are offering, and Georgia Tech is, I think, the fourth, the top fourth, the number four engineering school in the nation, I think, or top five at least somewhere. For $7,000, you can get an accredited master's degree through this kind of program, which maybe in other countries isn't an unreasonably low sum, but in the United States, that is a- That's low. Crazy low number.

**Dave Jones:** Do they let anyone in with the money? Like, do you have to have a suitable undergraduate degree to be let in to the master's?

**Chris Gammell:** No, no, you're going to have to apply for this. This isn't going to be an anyone gets in. Because that would dilute it, right? I mean, it still has to be-

**Chris Gammell:** Yeah, yeah. You know, choosing people that can do it, and also will finish it, right? But- Right. Yeah, man. That's crazy. A master's degree for $7,000? I mean, granted, a lot of people who do master's degrees, not a lot, but some people who do master's degrees, especially in the STEM fields, you know, they sometimes can get fellowships or apprenticeships. Well, no, that's not the right word. But, you know, like, basically funding through research grants and everything else to work with, you know, work on a research project, and then also helps pay for their tuition. But tuition, at least, last time I looked at some of the, you know, like my alma mater and other ones, it's like, you know, a year of graduate school can be an easy $30,000. So, you know, this being $7,000 is pretty impressive. Cheapest chips. Yeah. Although you do lose out on stuff. I mean, that's always important to remember as well. I mean, this wouldn't be necessarily possible in hardware because you wouldn't have access to facilities and stuff. But even in this thing, you lose out on, you know, in-person contact, networking, all the, a lot of the things that are really a big value of graduate school, you know, research methods, everything else, right? Maybe with people that are more lone wolf in the first place, it might be, still be a good fit, but man, that's cheap.

**Dave Jones:** Are they offering your dream course? Masters in social media business marketing?

**Chris Gammell:** Masters in punching you in the face.

**Dave Jones:** Come on, it's your dream, ain't it?

**Chris Gammell:** No, it's not.

**Dave Jones:** Combined with an MBA, I know it is.

**Chris Gammell:** They do have online MBAs, but I don't know if Georgia Tech does. But there are some out there. I mean, yeah, there's lots of programs like that. I mean, but usually it's not this cheap. I mean, they'll still charge a lot for it. You see a lot of, I hear like radio ads for the schools in the area doing like executive MBAs, you know? And that's when I start to, you know, they're like, oh, just one class per month, one Saturday every month. It's like, really? I mean, like, at a certain point, you're just paying someone to give you a piece of paper, right? Yes, yes, exactly.

**Dave Jones:** Yeah.

**Chris Gammell:** School should still have some value here, you know? I don't know.

**Dave Jones:** What, actually teach you something? Right, I know. Come on, get with the program. I know. This is 2013.

**Chris Gammell:** Yeah. I started doing, I got an email from Code Academy the other day and I started back in on their program. Apparently attrition rates are really high on these like coding programs and everything. And I'm guilty of it as well. But, you know, I've always wanted to learn Python and Code Academy has a Python module. And so I started doing it again, you know, got distracted and haven't gone back. But, you know, there are a lot of great resources out there for that kind of thing, you know, follow along. And apparently this is going to also allow you to get a master's degree. So it'll be interesting to see how it all works out. Well, if it does nothing more than lower the cost overall of education, that's all I care about because, you know, at a certain point I'm going to start agreeing with Peter Thiel and, you know, telling people not to go to school at all, right?

**Dave Jones:** Right, yeah.

**Chris Gammell:** Like the Thiel Fellowships. And I think that's a little extreme, but I think, you know, paying 200 grand for a degree is also pretty extreme, at least in the States.

**Dave Jones:** It's pretty stupid, yeah, exactly.

**Chris Gammell:** You know, what's the going rate in Aussie land these days?

**Dave Jones:** Oh, I have no idea. I don't follow it, but I can guesstimate it's $20,000, $30,000. Really? Okay, so that's going up there too. Yeah.

**Chris Gammell:** Because some places, I know, I think I talked to some of the UK and they said, yeah, it's going up, even where it's subsidized by, you know, like, and there's state tuition in some places in the States as well, you know, like a state school like Ohio State University or the Ohio State University. Right. Excuse me. It's, uh...

**Dave Jones:** That's actually funded, that's subsidized by the taxpayer, is it?

**Chris Gammell:** Yeah, basically if you're in state, you get a lower tuition. Right. Right. Okay. Like if I went there, it would be, you know, 10 grand cheaper or something, but it's still a lot, you know, and it's going up all the time.

**Dave Jones:** Yeah, it's, yeah.

**Chris Gammell:** So... Got it. That is a bubble ready to burst in my opinion.

**Dave Jones:** And you want to know what, the reason why it gets out of hand, well, especially here, I assume it's very similar, I think it's very similar in the US, is that you basically don't have to pay for it. Well, you don't have to pay for it up front because the government gives you a loan, right?

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** And then you don't, so you, so, you know, if you're a young whippersnapper, you want to go to university, yeah, the government will pay for it.

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** They, you know, you just have to remember that, well, ultimately you've got to pay it back sometime, you know? Yeah, man. And yeah, here, once you earn a certain amount and you file your tax return, it automatically comes back out of your tax return each year. Oh, really? And you slowly pay it off. Oh, yeah, yeah, yeah. So you can't escape it. Oh, you can't here either. No, they're tracking you, you know?

**Chris Gammell:** Yeah, the only way you can do it here is if you die. That's the only way your student loan debt goes away. If you file bankruptcy, it doesn't go away.

**Dave Jones:** Oh, right. Well, no, this one, yeah, same here. I don't think it, it won't ever vanish, but if you never earn enough to reach the threshold, then technically you'd never have to pay it back for the rest of your life.

**Chris Gammell:** So you fail in two ways.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** I'm sorry, money is not a measure of success. I'm sorry, that was a crappy thing for me to say.

**Dave Jones:** No, but I'm talking like, it's like minimum, like 30,000 a year or something like me. Yeah, so if you're not even earning that, then you're not paying. Yeah. Well, then, yeah, you're doing pretty poorly.

**Chris Gammell:** Yeah.

**Dave Jones:** It's crappy, man. You're eating cat food, you know?

**Chris Gammell:** Yeah. I wish it was cheaper, you know, because, I mean, hell, I don't necessarily want to go back to school, but I understand the draw of it. I mean, obviously I went through it, right? I mean, you went through it. It's like there is a very big draw to being at a point in your life where you're just focused on learning and, you know, it's exciting and, you know, it's just a great time, right? It's still hard, but it's very rare, right? And I get it. And I'm still paying my loans back. Don't kid yourself, you know? Right. I just wish people didn't have to – I wish there were other options out there that were, you know, that then employers looked at, right? And that's the next step up from this online thing, you know? Like, it would be – if you had a large corporation that was looking at the employment field, right, like, say at Google, right, and they said, all right, well, we think we can find programmers and maybe hardware people that if they go through this program that we develop online, then we're willing to hire them or interview and hire them, right? And if you take the university degree as the gating factor, right, that ultimately is what is the gating factor here. That's what's driving the price of everything up because if you don't have that piece of paper, then you can't get a job no matter how good you are at, you know, doing electronics or coding, whatever else, right, unless you find backdoor methods to doing that kind of thing.

**Dave Jones:** I don't know.

**Chris Gammell:** I want to fix the world sometimes, Dave. It's just hard to fix.

**Dave Jones:** You can't. The world just sucks sometimes.

**Chris Gammell:** It does suck. You know, I think the focus, though, is that – and, you know, I think looking at how people have done it – you know, like talking about Jerry, right? Jerry was self-taught for a lot of stuff and what it ultimately came down to – I mean, she's told her story a couple times, but, you know, like she networked to jobs. She found mentors. She networked, right? And then eventually she was doing work on her own. It's just not following – she was following a nontraditional career path. Same with Jack Gansel, right? Jack didn't finish college, he said, and, you know, he started his own company, right? And that – I think at that point that is – it's kind of mother of necessity being the mother of invention in that case, right? You know, it's – if you can't find a job, you make a job, and in both their cases and in other cases as well, you know, like that's the option. And if that became the norm, then maybe the university education wouldn't matter as much. It would be just the merit of your work and what you've designed. But until then, it's –

**Dave Jones:** Well, that's – I've always said that that's in the electronics industry, at least here in Australia, that's how it works. Oh, really? Nobody gives a shit if you're – what school you went to, what degree you got. Nobody cares. Can you do the job? Yes, no, you're hired.

**Chris Gammell:** Right, but do they still gate it with a degree? Do they care? I mean, like –

**Dave Jones:** No.

**Chris Gammell:** Okay.

**Dave Jones:** Most employers, the majority of employers in the electronics industry do not care. Well – All I care about is can you do the job?

**Chris Gammell:** That's great. I mean, because that's how it should be, I think.

**Dave Jones:** Well, yeah, of course. There are some regulated, you know, like the medical industry or something, you know, it's next to impossible to get an engineering job in a medical company, for example, without being a member of the Institute of Engineers, for example. Oh, interesting. Or some government department, for example. So, yeah. But as far as the free market goes, no. No, it's different. It doesn't matter. Our rats.

**Chris Gammell:** Well, that's good then. Because, I mean, at least around – I mean, at least in the States with like – you know, like you look at like a job fair or big companies, right? Like people that – you think about people that want to – companies that people want to work at when you ask like the general populace, general engineering populace, you know, top employers and stuff, you know, like the Googles and the Apples and everything else. They all – many of them have that gating factor of do you have a degree because it gives a certain – usually it indicates – Oh, yeah, of course. – the proficiency and, you know, dedication to hard work and stuff. But it's not the only way, right? So –

**Dave Jones:** No, that's right.

**Chris Gammell:** But you're saying that even big companies don't care? Big companies don't care. Well, that's – that is impressive because every big company I've ever talked to has got an HR department that really, really cares and they suck.

**Dave Jones:** No, I'm talking, you know, $50 billion companies. I'm talking big companies.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, that's good then. I'm talking the world's largest defense contractor.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Yeah.

**Chris Gammell:** Then I hope that becomes the norm because that –

**Dave Jones:** Yep.

**Chris Gammell:** That should be, but –

**Dave Jones:** But you've got to keep a tight rein over the HR department. If you let the HR department run the shop, then yes, they will exclude all those people, right, automatically. You've got to tell them, look, I don't give a shit. Give me all the damn resumes, right? Yeah. So you've got to tell them not to do their job, basically, which isn't much. Their job isn't much at all. Right. Yes, I am saying HR departments are redundant because they are.

**Chris Gammell:** What I'm saying is I hate you, HR. No. I don't think we have any HR listeners, so if we do. Right. Yeah. Worthless. Yeah. Well, that's interesting. I didn't really always like that out there. But I do agree that if HR gets in charge, it's usually curtains for –

**Dave Jones:** It's usually – and it can also depend on the – like a head of a department who's hiring somebody. They will instruct HR. Look, I only want people with X level degree from X colleges. I don't want anyone from Zagazig University getting in here, right? Yeah. Sorry to all the people who've been to X colleges University because that is actually a real university.

**Chris Gammell:** I was going to ask. Yeah. Yeah.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** Yeah. I remember seeing – there was an EEVblog forum post about this whole topic at one point, I think, as well. Oh, yeah. Yeah.

**Dave Jones:** Of course there is.

**Chris Gammell:** Yeah.

**Dave Jones:** There's a forum talking about everything.

**Chris Gammell:** Oh, yes. It's EEVblog.com slash forum. That's right.

**Dave Jones:** All right. We should do – Dude, we're going 20 minutes over.

**Chris Gammell:** I know. But we should go through the rapid fire news stories at the end because there are some interesting ones. All right. Here we go.

**Dave Jones:** Yeah. TinkerCad found a new home at all our desks. Yeah. Yeah. They're back from the ashes. Phoenix-like. Yep. Fine.

**Chris Gammell:** Circuit Hub. Excellent. Andrew Seddon was on the show previously. Circuit Hub is now supporting KiCad. At least in a beta stage. So, rockin'. Bring it on. That's awesome. Let's see. Beta. Beta. Beta. Beta. Bloody yanks. Beta. I don't know. Cubiboard has been released. I think it might have been on for a little while, but there is a new version of Cubiboard, so check that out.

**Dave Jones:** I didn't know there was an old version of Cubiboard. Yeah.

**Chris Gammell:** It's another, it's an A10, similar, another process, another A10 processor, similar to like a Raspberry Pi. It's a high-power arm, basically. Right. My point on that was community matters, and it's starting to get where community matters much more than specs, because everything has these low-cost chips on them, but if you don't have people that are also working on it, then screw it.

**Dave Jones:** No. Yep.

**Chris Gammell:** I think that's it. Is that it? There's probably other stuff.

**Dave Jones:** Yeah, we do have a workbench photo, though.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Somebody sent this in. Oh, yeah. Don't have the name.

**Chris Gammell:** It is the one true stick man. He actually didn't want his real name. The one true stick man. Does he have a real name? His real name shared. No, he didn't want that shared, so.

**Dave Jones:** Oh, okay. Well, he's the one true stick man.

**Chris Gammell:** He is. Yeah. It's a nice bench.

**Dave Jones:** And that's a schmick-looking lab.

**Chris Gammell:** Yeah, I like it.

**Dave Jones:** I like that. Good setup. It's just built high, you know. Yeah. It's built right to the roof, and it's on a desk of the computers and a tiny little workbench there, and it's just... Yeah, there it is. Yeah. It's all there. I love the blender down in the bottom left corner.

**Chris Gammell:** Oh, yeah. There is an oscillator there, actually. I got an oscillator at the swap meet.

**Dave Jones:** Old school. Which model?

**Chris Gammell:** Oh, I had it here. It's the... Oh, it's heavy. It's on the ground. It is an HP L4, I guess. There's a long... I don't know what it is. It was the end of the show buy. It was honestly like we were walking out on Saturday, right at close, and we were like... I was like, oh, because I had been looking for one, and I was like, yeah, how much for that? Ten bucks? Yeah, no big deal. So, yeah. Sweet. If nothing more, it's a beefy case. I actually haven't tested it yet, but... We cracked it open at the meetup, and it was very nice construction inside. I'll try and...

**Dave Jones:** Does it have a light bulb stabilized ween oscillator in it?

**Chris Gammell:** Yeah, we think so. We didn't... It was really poor lighting in the bar we were at, but... Yeah. It was awesome to roll into a bar with a bunch of fellow nerds, and to bring in an oscillator and crack it open, and to have everyone excited about that, except for, you know, the regulars at the bar.

**Dave Jones:** I'm surprised I didn't call Homeland Security.

**Chris Gammell:** Yeah, right? It's Dayton. Dayton's pretty rough in Tumble City. They're probably used to a lot there. Right. Cool. All right. All right. That's our show, surely. Yes. Hopefully we'll have a guest next week. A certain... Hopefully. Jerry guest.

**Dave Jones:** Big surprise.

**Chris Gammell:** See you then. Bye. Bye. Bye. This episode was sponsored by Club Jameco. Upload your project brief today, and if approved, you'll get a 10% off coupon. If chosen by the community, you'll make 10% off any kit sold without ever needing to buy or bag components. Go to clubjameco.com slash theamphour to find more details and to support the show.

**Chris Gammell:** So, someone left their Ray-Bans at the meetup, even though it was dark by the time we got there. But anyways, I have them, and if you want them back, and you can prove you were there, because this ain't no sunglass giveaway, shoot me an email. Chris at theamphour.com.
