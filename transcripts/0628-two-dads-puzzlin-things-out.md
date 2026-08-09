---
episode: 628
title: Two Dads Puzzlin Things Out
url: https://theamphour.com/628-two-dads-puzzlin-things-out/
---

**Chris Gammell:** Have you found yourself thinking, you know, I really wish that Chris would go to more conferences outside so he could record like those things where he edited from a tent? Well, I thought everybody might have been missing this. And so I recorded outside with my good friend. Just so you know, this is an outside recording. I'd say give it a shot. See if you like it. If not, see you in the next episode. This is The Amp Hour Podcast. Released April 16th, 2023. Episode 628. Two dads puzzling things out. Welcome to the Empire. I'm Chris Gammell of Contextual Electronics.

**Dave Young:** And I'm Dave Young of Young Circuit Designs.

**Chris Gammell:** And we're on my back porch recording.

**Dave Young:** In person. In person. On a delightful day. It's so beautiful.

**Chris Gammell:** I probably put a preamble in the recording. But if you didn't hear that for some reason, this is an outdoor recording. So there's going to be noise. It won't be as much of a festival or conference where we've recorded in the past where it's like tons of other noise. But there might be some loud cars that go by at some point. But it's so nice that we just had to be outside.

**Dave Young:** Can't be inside.

**Chris Gammell:** Need more today. Yeah. So the first thing. Welcome back, Dave, by the way.

**Dave Young:** Hey, thanks.

**Chris Gammell:** Yeah. Always good. Dave's been on a couple times. Dave, I've known since my Keithley days. Actually, no. Before then. Yeah, college days. Dave and I did our first co-op together. Yeah. And. Oh. What just blipped? Something just blipped.

**Dave Young:** I didn't touch anything.

**Chris Gammell:** I didn't touch anything either. Maybe it didn't blip. Yeah. We'll see. Dave and I have known each other since co-op days. And we. He's the one who got me into consulting. And this is a bubbly water. That is not beer. Not yet. Not yet. I don't drink beer. And. Yeah. And Dave came to visit, which is great. We're actually going to do. We've been doing training. We did training on Friday as well. Yeah. And we're going to do training again on Monday for Goliath stuff.

**Dave Young:** Yeah.

**Chris Gammell:** And Dave is kind of like trying to do the more firmware stuff like I am as well.

**Dave Young:** Yeah. Yeah. I can't wait to have something that's easy to stand up and get things moving quickly. Yeah. Because that's what everybody wants. Right? Yeah. That's all I want. Like I want something cheap and fast and good. Yeah. So we'll keep moving towards that.

**Chris Gammell:** Yeah. Yeah. And I think that's the fast part is the hard thing. For sure. Like. It's like you still need to have some kind of customization. But not. But you need some kind of customization, but you kind of want like a good starting place. Yeah. That's kind of what it comes down to.

**Dave Young:** Yeah. And you don't want to take six months to figure out something's not appropriate.

**Chris Gammell:** Yeah. Right. That is the biggest. Yeah. That's the biggest problem. Yeah. You're halfway down a path.

**Dave Young:** So if it can be super fast and cheap and good, or good enough rather, then you're in a good spot.

**Chris Gammell:** Right. You're trying to prove it out because you're doing consulting. You're trying to prove it out for your clients. Right. This is nice. We get ambiance of car horns and.

**Dave Young:** Just focus on the birds.

**Chris Gammell:** Outdoors might have been. Just focus on the birds. The wrong call. Yeah. So prototyping and getting people to solutions faster because then ultimately you make your money when you're actually doing custom hardware, right?

**Dave Young:** Yeah. Yeah. There might be other opportunities there, but that's where the real value add. That's so I've got 15 years of experience and I can bring that to get somebody to a manufacturable product quickly. Right. Right. But if you don't know what that manufacturable product is yet. Right. That's a real problem. Right.

**Chris Gammell:** I found like we were talking a little bit about like people who show up with like a little bit of technical expertise and then they show up with an Arduino. Yeah. Which is fine. Actually, it's a great way to. It's awesome. What a great way to get a first round of funding. Right. But then you turn around, you have to like make that a real thing. That's I mean, that's a lot of what my business was when I was consulting too.

**Dave Young:** Absolutely. And the thing is, is it's so different. Like it's an entire by the time you're in manufacturing, what you build is very different from that original Arduino prototype by almost every measure.

**Chris Gammell:** Yep. Yep. I will bring up I was on Embedded FM. If you want to hear me talking nonstop about Goliath, you can hear me there. I try not to do that too much here. Of course, Dave being here, we're talking about it because we're doing training on it. But yeah, so go listen to that if you haven't. But the first thing I wanted to bring up. All right. Here we go. We're going to start. Oh, yeah, this is good. Car talk style puzzler this week, including a prize.

**Dave Young:** Ah, prize. Yeah.

**Chris Gammell:** So if so, we're going to make this into a puzzle. I'm not very good at this yet. I haven't written it down, which is probably the worst part of it. But if you think you know the answer, write with the subject line puzzler to the amp hour at gmail.com and you will be entered for in the drawing for this for this prize. The prize will be a hard to get amp hour t-shirt or sweatshirt. You let me know which you'd prefer. If you're in the southern hemisphere, you might be going into sweatshirt season. If you're in the northern hemisphere, hopefully you're like here in Durham where it's already pretty much summertime.

**Dave Young:** So nice.

**Chris Gammell:** If you're in Rochester, New York, where David's, maybe you're still... Yeah, hit and miss.

**Dave Young:** Today, I hear, is real nice t-shirt weather, but tomorrow, probably not.

**Chris Gammell:** Yeah, I heard my folks at Buffalo that it's going to snow next week. Don't turn those heaters off yet. That's right. Yeah, yeah. Okay, here's the puzzler. So I was sitting in my office, in my house last week, and my TV went off, which is my main screen, and my Wi-Fi went off. And stop me if I'm giving too much away, Dave.

**Dave Young:** Yeah, okay.

**Chris Gammell:** Okay. And I'm like, okay, well, I must have blown a breaker, or something must have happened, right? So I go down to the garage where my breaker box is. I go and look at all the breakers. Nothing. It's, they're all, they're all clean. So I start flipping them, powering stuff down, powering back on. Nothing's happening. So I go back upstairs, and I notice the hallway light is on. Hallway's light's on, but my office is off. And I'm like, what the heck is going on? And so I go and like kind of just do a quick audit of the rooms throughout the house. My wife's office is off. My daughter's room is off. My bedroom is on. Bathrooms are on. And so I'm just like, what? What the hell is going on here? And so I'm getting a little freaked out, to be honest. And so I go around, and I start, I go down to the garage, which has been having some problems with the garage door opener. And it's just kind of been like some weird behavior. Sometimes it won't actually, you know, you have to press the button a couple times. Sometimes you have to wait. Sometimes it goes up just an inch, whatever. So it's just been kind of weird. And I go there, and I'm like, and this is next to where the breaker box is as well. And I go to try the GFCI that's in there. And I press the GFCI test button. And it clicks. And it won't reset. And I'm like, what is going on here?

**Dave Young:** And you haven't changed anything about that. Nothing has changed. About that, sir. Yeah, yeah, yeah. Yeah.

**Chris Gammell:** Yeah. And so the only way I'm able to get it to actually reset is I had to flip the breaker on off. Right. And then it would reset. Right. And I go back up to my office. Lights still don't work. The router's still off. TV's still off. Doesn't, nothing's, everything's dead up there. And I'm like, what? What the hell's going on here? So then I go and I'm like, well, I guess I'll go try other GFCI switches. And I go try the kitchen. You know, kitchen has them, bathroom has them, whatever. Finally, I try the bathroom next to my office. And I flip that one. And I test it. And I reset it. And things come back on. Ooh. And I am so incredibly confused at this point. That's on a Monday. I'm like, okay, well, I guess I'll call an electrician if it gets worse. Tuesday night, it gets worse. And it all comes back. And now those switch, the breakers that were off, or sorry, the rooms that are off, they are just off. I can't get them to come back. I try all the switches again. GFCI does nothing.

**Dave Young:** Nothing. So the thing that fixed it before does not fix it now. Yeah, there's no consistency. Oh, see, this is real troubleshooting. Yeah. It worked before, just yesterday.

**Chris Gammell:** Yeah, exactly.

**Dave Young:** I swear.

**Chris Gammell:** So I'm not sure that's enough to recap once again. Some of the rooms in my house have power. Some do not. I have no way to suss it out. And so that's all I'm going to leave you with. It's a puzzler for a reason. So what is the possible problem in my house? And for added bonus, how did I figure it out, aside from eventually calling the electrician? I actually figured it out, but I didn't figure it out. Chris, you're taking too much credit. I know. The guy showed up. It counts as his win. No, he totally got it. But I actually did something that freaked me out even more the next day that made even less sense. And then the electrician showed up, and he figured it out.

**Dave Young:** Oh, right, right, right, right.

**Chris Gammell:** Yeah, you know that part.

**Dave Young:** So the other thing that I'm just going to add here, because it-

**Chris Gammell:** Because that's what they did in Car Talk, too. They always gave, like, the- Yeah, yeah, yeah.

**Dave Young:** So I'm going to add that your house is a delightful house that was recent build. So you're not dealing with, like, squirrely 1920s wiring. No tube, knob and tube, like my old 1950s house. This place was built less than 10 years ago, right? That's right, that's right. Yeah, so it's all to code and legit and not some, like, Jim Bob homeowner that decided one day he's going to fix the problem by just jumping this to this. That's not in play.

**Chris Gammell:** Right, right, no pennies in the few bucks.

**Dave Young:** Yeah, yeah.

**Chris Gammell:** Okay, so that's what it is. If you'd like to compete, please email theamphour at gmail.com with the subject line puzzler with your answer in the body of the email, and we will pick from among the winners. So good luck. And I will reveal the story, the remainder of the story next week. Yeah.

**Dave Young:** Yeah, that's good.

**Chris Gammell:** All right. What else do you want to talk about?

**Dave Young:** So I want to talk about an exciting thing for me in my world is the chip shortage, which has been, like,

**Chris Gammell:** exciting.

**Dave Young:** The last time I was on the amp, are we talking about it? And I was in the depths of despair because all my clients can't make anything. That's right. They can make most of their stuff, but as we all know, one part missing is no part out of the end of the service mount line. So I think it's way better. I just had a client this last week had to pivot and switch. Now, they had a bunch of their stuff on the shelf because of all the problems and the issues we've been having, but it was easier to order a prototype-sized batch of parts from DigiKey than to pull them off reels and stuff like that. Yeah. So we did that, and it was, like, 90-plus percent of the bomb. So what was the other 10%? We were able to get. The other 10% was actually is really just one part, which is still not available, and it's an instrumentation amp.

**Chris Gammell:** Ah, okay. So, like, specialty, let me guess, TI? Analog.

**Dave Young:** Well, so that's my point, is there are now only two companies that make instrumentation amps. Yeah, that's right. Well, that make them in earnest.

**Chris Gammell:** That's right. Like the spec wars that we're used to.

**Dave Young:** So where is the motivation for them to turn back on this instrumentation amp line that I need them to turn back on? If they're competing, their one competing company doesn't make something similar.

**Chris Gammell:** That's right. Yeah, it's like a, not prisoners' dilemma, but it's like they're edging forward. They're like, you're going to do it? I'm going to do it? Yeah. I'm going to do it? And they all can make money, like bigger money, and probably have more clients yelling at them, like the apples of the world, being like, no, you will make our parts. You will make our parts. Yeah.

**Dave Young:** So where is the incentive? You know, it's the problem with a duopoly is you get weird incentive structures going, and it's a problem. So that's the issue. And I am lamenting the mergers over the last minutes.

**Chris Gammell:** I don't know any, what is the, any positives come out of that?

**Dave Young:** I mean, in theory, it's economies of scale, but then we got burned by economies of scale during COVID with the chip shortage. Like one fab goes down, and half your parts are unavailable.

**Chris Gammell:** I mean, but they're not using, if they were making their own, if they had their own fabs. True. It's different fabs. TI has their own fab. But if they're all, if they're all fabless, then it's, there's no scale there.

**Dave Young:** But as you get larger and larger companies, you find economies of scale because one order looks like a piece of a giant order. Oh, I see. I see. But the problem is everything looks, all of the product lines of these two companies look the same. Yeah. And so one problem comes along, and it impacts everything. Right. The same. As opposed to if you have all the distributed companies doing different things, they take different, like, linear, for the longest time, had their own fabs. Yeah. And even in the shortage that happened in 2008, you were able to get linear parts way sooner. Like, TI was talking 99 weeks, and linear's talking 30.

**Chris Gammell:** So... I don't remember the 2008. Yeah.

**Dave Young:** I was talking with Jeff Ivanko about this. He was like, we are in a totally different scenario than TI because we have our own stuff, and we have a bunch more, and we're set up to be more nimble. Yeah, yeah, yeah. So linear was just, like, a different company to start with, and that was one of the benefits. So now that linear's part of analog, it's like, well, it's all the same, and it's just there's two ways to do it, and it's the TI way and the analog way, and they're not that different.

**Chris Gammell:** Yeah. That sucks.

**Dave Young:** The approach isn't that different.

**Chris Gammell:** Right, and there's no, like, Fabless that are popping out of the woodwork either for that stuff.

**Dave Young:** No. What was that company that tried to be Fabless? Did they succeed? No. Was it Tordex or... I can't remember. Triad.

**Chris Gammell:** No, not Triad. Triad is a semiconductor company. I know who you're talking about. Yeah. We had them on the show. We had them on. They failed. No, they're gone.

**Dave Young:** They didn't make it? They didn't get bought out? It was not as successful? They got, like, acqui-hired, I think. Okay. So that's not bad, but still, it's just the same thing as linear being bought by analog. So...

**Chris Gammell:** Sorry, I'm a little distracted here. I'm also, you know, because we're recording at home in person, I'm also watching the monitor, and my daughter is stirring. The monitor, not the audio monitor. Not the audio monitor, the baby monitor. Yeah.

**Dave Young:** Right. So the other problem that I have, the shortest problem that I still have, and this is for my education company, Blue Stamp Engineering, where we are teaching kids how to build cool stuff. Yeah. We can't get a Raspberry Pi. No. So the point of Raspberry Pi is to teach kids stuff, and we can't get pies. No. And so I don't know what I'm going to do.

**Chris Gammell:** It's getting a little better. I did get some CM4s.

**Dave Young:** Did you?

**Chris Gammell:** Yeah.

**Dave Young:** Okay. I can't use the CM4s. I know.

**Chris Gammell:** You need a baseboard, then. I mean, that's actually meant to try and offload some of the people that are using Raspberry Pies.

**Dave Young:** Okay. Hey, so that's a step in the right direction, like recognizing how people are using your product, and we'll leave this for the kids, and we'll make something special for you. And they'll scale that other stuff. And that you want the CM4 anyways. Right. Because you don't want the full size pie. That's right. You want the slot.

**Chris Gammell:** I want the IOs and a tiny pitch.

**Dave Young:** Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Young:** Yeah. So I can't get the Raspberry Pis. That sucks. If anybody out there knows how I can get Raspberry Pis, please let me know. I would be very interested. Because right now, our best approach is to pay the scalpers.

**Chris Gammell:** Yeah. That sucks.

**Dave Young:** And I also don't like doing that because I'm contributing to the bad behavior of scalping.

**Chris Gammell:** Yeah.

**Dave Young:** So, yeah, I don't know what I'm going to do. So please, somebody.

**Chris Gammell:** There is a tracker that doesn't. And people give me that as the, you know, there's like a Raspberry Pi tracker that allows you to see who has it in stock, whatever. Yeah. But they're all zeros. Well, they're all zeros, but also it doesn't really help. I don't need a tracker. I need a alert service, really. Right. Like we have some. I need a purchasing agent is what I really need. You know, I need someone who's like, oh yeah, I'll just buy them when they come up, you know? Yeah.

**Dave Young:** Well, so I've got our program manager checking every day.

**Chris Gammell:** Yeah.

**Dave Young:** For stuff.

**Chris Gammell:** Do you have orders in anywhere?

**Dave Young:** No.

**Chris Gammell:** Yeah. That's the other thing too is like you need like a, who's the most statistically likely? And I'll go wait in line as long as I know that line might get filled.

**Dave Young:** Yeah. But like we talked about last time with the chip shortage, you could have an order in with Mauser and then they have some on the shelf. You see it just because you're checking and you're desperate because of the chip shortage. You buy them. And they ship the ones that you put an order in two seconds ago in and your back order is still sitting there waiting.

**Chris Gammell:** Oh.

**Dave Young:** So, and I can appreciate the position they're in. Like they were in the mess just like we were. So they were probably just trying to do their best. But just putting a back order in is not the same thing as having an order. Yeah.

**Chris Gammell:** I think about it more as a backstop. I mean, my big order.

**Chris Gammell:** It doesn't cost you anything. Unless they do shit. My big order came in on Christmas Eve. Yeah. It filled on Christmas Eve. Yeah. Or the day after Christmas. It was definitely around Christmas. I was very surprised by that. So, yeah.

**Dave Young:** Yeah. So anyways, I'm not sure what I'm going to do. And the other thing is I do pay a penalty if I put a back order in and then I forget about it and it ships in July after the program's like almost done. That's a problem for me. Yeah. Here's your $4,000 bill and all your Raspberry Pis.

**Chris Gammell:** Yeah. That sucks.

**Dave Young:** Yeah. Hopefully, we won't need that many Raspberry Pis. Hopefully, you do. You have so many students. I have so many students that are so interested in electronics. Yeah. Yeah. Yeah. Yeah. Yeah. So, yeah.

**Chris Gammell:** It does feel like this. I mean, like I haven't been building a ton of stuff, but it does feel like it's a lot, generally a lot easier to get stuff. And I feel like it does. Because one of the things that was problematic was this ping pong effect where like, so you and I are trying to buy the same kind of chip. Yes. Right? You would say instrumentation amps again. I see that I have the TI part in my thing. I decide to go and design the analog part. Right. I take away from you. Take away from me. You take away from me. And it's just like ping pongs around the ecosystem like that. I mean, boards aren't that hard to re-spin. There's obviously cost. Yeah.

**Dave Young:** There's the time and money cost. And really, it's the risk. Yeah. Right. Right. Yeah. It's the risk. Yeah.

**Chris Gammell:** Because you miss something or the pinout's different or whatever it is.

**Dave Young:** And you got it. It doesn't work until I see it work. I tell that to everybody. Like, so we can go to production. It doesn't work until I see it work. Yeah. Yeah. So, it's just a lot of risk. But hopefully, it's on the end. And this is the last time we have to talk about not being able to get parts and having to pivot. But I do want to talk about the CM4. Have you designed in the CM4 or are you still working on it?

**Chris Gammell:** It's still going. But yeah.

**Dave Young:** Is the CM4, I haven't looked at the pinout yet. Is the CM4 have high speed layout requirements for that slot?

**Chris Gammell:** Define high speed.

**Dave Young:** Like, do you need. Control impedance. Can you design. If you're not using any impedance controlled buses. In order to make that work. So, if I had like a simple Raspberry Pi design where I just need to communicate. I just need a GPIO. I just need GPIO or I just need like an I2C bus or a spy bus or something like that. Mm-hmm. Do I. Can I use like a low grade two or four layer PCB. You can do that. In order to plug in and it'll work.

**Chris Gammell:** You can do that for controlled impedance too. As long as you follow the rules.

**Dave Young:** Yeah, I know. But then if you're going to do controlled impedance and you need to know stack up and you can't go to like some random place.

**Chris Gammell:** You do the cheapo big name Chinese. Right.

**Dave Young:** I'm not saying there's not solutions. Yeah, yeah. My question is do I have to use any of those techniques. If I were a beginner.

**Chris Gammell:** Got it. So, like if one of your. I would like frame it like this. If one of your students. Yes.

**Dave Young:** This is exactly what I'm asking.

**Chris Gammell:** Or an intern maybe. Maybe because maybe student is. Maybe a high school student is there. But an intern might be. Sure. Is an intern able to do this? I think so. I think the big thing.

**Dave Young:** There's nothing crazy about your layout.

**Chris Gammell:** No, nothing crazy about the layout. The big thing is the. It's a .05. There's a 50 mil pitch connector. And those are hard to get. Those are unobtainium still too. Oh, is that right? They're Hirosi connectors. They're 100 pin. You need two of them. They're expensive. You need two. They're like two rails.

**Dave Young:** Oh, right. Because they did the. It's like the daughter board module. It's like a daughter board. It's not the RAM slot anymore. It's the daughter board. I forgot about that. Yeah.

**Chris Gammell:** And so like if alignment's off. Oh, how are you doing alignment? Are you hand building these or something else? I am hand building prototypes. And then production. You know, someone else will be building them. Yeah. So that'll be fine.

**Dave Young:** You're going to be able to do the hand populated alignment?

**Chris Gammell:** I have stopped even using paste for them. My paste. I got myself into trouble with my paste. I was using five-year-old paste. Don't do that. That's a bad idea. Yeah.

**Dave Young:** They have an expiration date on them. They have a very firm one.

**Chris Gammell:** I should have thrown it out three years ago. Yeah. And it's just like I wasted a lot of my own time.

**Dave Young:** Yeah. Because it's just not as nice to work with. I don't even wait until it's halfway expired.

**Chris Gammell:** You should buy it. Yeah. You should buy it every. If you're not refreshing every year, you should just throw it out.

**Dave Young:** I don't even make it that long. I feel like every time I make a board, I'm going to be considering buying flux. Yeah. Or buying paste. Buying paste. That's not a bad idea. Yeah. Now, that said, I have an expiration date on some of my leaded solder with rosin core that's got to be 15 years ago. Oh, totally. And I still use that, and it flows great.

**Chris Gammell:** Yeah. Yes. Anyways, so I got myself in a little trouble with paste. So what I started doing is I just hand soldered it all. I like literally these 50 mil pitch connectors. Now, what technique did you use? Just a drag solder. Yeah. Okay. So pin the corners. So you stake the two down. Pin the corners, and then float. And honestly, if you have good magnification, it's fine. I mean, not fine. You get used to it. You get better at it. And what it really came down to is I was reworking a bunch of them, and then I was like, this is just so much easier to do by hand.

**Dave Young:** Yeah.

**Chris Gammell:** So.

**Dave Young:** Yeah, that was my question. How many did you screw up?

**Chris Gammell:** Oh, so many.

**Dave Young:** So many. You know what I like to do with those things is I put the connectors in the CM4, and then I solder. I tack on the four pins.

**Chris Gammell:** You can't get it. It covers. Oh, you can't get it at all. Yeah.

**Dave Young:** Oh, man. Yeah. And that's 50 mil pitch. It's tough. 50 mil's not surface mount, though.

**Chris Gammell:** It's teeny tiny.

**Dave Young:** Yeah. 50 mil? Is it 50 mil? 50 mil's not teeny tiny, because 100 mil pitch pins is like a dip. Oh, no. Sorry.

**Chris Gammell:** Not 50 mil, then.

**Dave Young:** A dip.

**Chris Gammell:** Sorry. It might be 0.5 millimeter. What is the Hirose part?

**Dave Young:** 0.5 millimeters would be tough. That sounds about right.

**Chris Gammell:** 100.

**Dave Young:** Because a 0.5 millimeter would be like a typical QFN.

**Chris Gammell:** R5CM4. I'm doing a live search, of course. Yeah.

**Dave Young:** At least the internet's good. It won't be slow. Well, maybe I was wrong.

**Chris Gammell:** Which one is it? It's the DF40HC100DS.

**Dave Young:** You guys are watching him check right now to make sure they're stock. Yeah, yeah. Or not. Yeah. If he finds some stock, he may have to step away for a minute and get some. Yeah, right, right.

**Chris Gammell:** Now, I'm all stocked up. I'm all stocked up on that stuff. Oh, this is just, man, this ResRoy part article is not. Anyways, it's not 50 mil. You're right. That'd be big. That is wrong. This is, what is the pitch? 0.4 millimeters. 0.4. Oops. Yeah, got that. Yeah. This one might be wrong. It might be 0.5 millimeters. Yeah, but still. It's tiny. It's tiny. Yeah. I think this is, it might be the DF50C.

**Dave Young:** But you figured it out. You got there.

**Chris Gammell:** I got there. And I would say it's possible.

**Dave Young:** You can make one right now. Could you do it?

**Chris Gammell:** Yes, I could do it. Okay. But I have good magnification. I ended up getting a long throw magnifier off of AliExpress. Okay. So it's got like this long, it's like a telescopic lens, basically. And then like a 30 megapixel sensor. The whole setup was like about 200 bucks. But I mounted up above, like, probably like a, you know, half a meter off my bench top. So you can get it off there. So you get a ton of. It doesn't have to be right on top of it. People have seen it before. They're like, well, you don't have stereoscopic then, which is true. Actually, Florin from Voltlog, he has a video about this setup. I stole all this stuff from me. Yeah, yeah, yeah. So he bought it as a thing that he put onto his microscopic or his stereoscopic microscope. And then he added this as like the third inlet to that thing. And then he uses that.

**Dave Young:** Yes.

**Chris Gammell:** I didn't want to do that. But it comes with this long throw telescopic lens. And I just use that. Okay. And as long as you have, like, I mount it to a shelf. So my bench, if I'm messing with my bench, it doesn't vibrate. Right. And then I have an HDMI, like a cheapo HDMI monitor right there. So it's basically like, it's like a heads up. I'm like looking up at the screen.

**Dave Young:** So is that like seven inch HDMI monitor or something like that? Yeah.

**Chris Gammell:** Yeah. Like seven inch. Yeah. A hundred bucks.

**Dave Young:** So you do it for like a Raspberry Pi project.

**Chris Gammell:** Yeah, exactly. Yeah. So super, super simple.

**Dave Young:** Okay. Okay.

**Chris Gammell:** Neighbors.

**Dave Young:** Chris is enjoying the ambiance of the outdoors. No, I wasn't.

**Chris Gammell:** The birds are great. The birds are great. Yeah. The trucks and the motorcycles. Okay. Just birds. Just focus on the birds. Chirp, chirp, chirp. Chirp, chirp. Yeah. Yeah. You think you'd have, do you think that's something your students would do or what?

**Dave Young:** What, lay out a board? Yeah. Yeah. So at Blue Stamp, we lay out boards. It's only, it's a subset of the population because it has, we have to plan it. We have, so at Blue Stamp, we have what's called a student defined project. Yeah. And that's literally, they get to do what they want as long as it's safe and reasonable. Do it well. No. And many students come in and be like, I want to lay out a board. And I'm like, yeah, you do. Here we go. This is why we do this stuff.

**Chris Gammell:** Yeah.

**Dave Young:** And so we figure out a way so they can lay out a board and we, and we, you know, we get the super swift service from Osh Park or we, we figure out a way to make it so that they can get it on time and still assemble it and build it. But they wouldn't, you know, impedance controlled board, if that's what it took to get a CM4 in there, it's not going to go. But it sounds like if you, if I needed to just do power ground and a bunch of IOs or whatever I need.

**Chris Gammell:** I wouldn't say that though. You really do want the impedance control part because otherwise you don't have a display output. Right. So unless you're just. So that, yeah.

**Dave Young:** But if I wanted to do like an IOT device based on the, on the, on the, on the Pi.

**Chris Gammell:** Don't do that.

**Dave Young:** Yeah. Well, so that's the other thing is like, why are you using a Pi? Probably for like a video camera interface. Exactly. And then you're into what, what is that? Like the MIPI standard? Like that's a pain in the ass.

**Chris Gammell:** DSI, DSI outputs. DSI. Yeah. That's a pain in the, I've laid those out.

**Dave Young:** It's a pain in the, it'd take me the entire blue stamp just to teach them how to lay out that. Yeah.

**Chris Gammell:** And I think HDMI then too. But like, it's doable, but it's not. Yeah. It's doable. Right. It's just probably not worth it for the timeline you have.

**Dave Young:** Probably not worth it. Yeah. Still, it's good to know that if, if there is something that comes up.

**Chris Gammell:** And it's not like, they're not like more accessible. The CM4 is not more accessible. It's just that I, I had an order in it for a long time. Right. So that's the main thing.

**Dave Young:** Right. Right. Yeah. So it probably wouldn't work out, but it's good to know. I mean, the other thing is a backup plan. If we can't get the real boards, get the CM4s and the, and a breakout board. Yeah. You can do that. I would say like, you know, like there's new rock pie type things like. So the problem is, is we try and use known, we try and use projects that have already been documented. Yeah. I get it. And so.

**Chris Gammell:** Some of that stuff that was made. To port it over. It's not, it's not porting though. It's like the OS level is the same. It's the same. Sure.

**Dave Young:** But like the pinouts may change or the, you know, a lot of stuff can change and you could easily spend, you know, the point of Blue Stamp is to be accessible enough so that anybody can do it, but we can quickly assess where a student is and dial in a custom program so that they can be challenged at their level. Yeah. And so it's very challenging at a experienced student level to engage in that kind of transition, but it's true. It's not fun. Nobody's going to stay in engineering because of changing from a raspberry pie to a pine or whatever. Yeah. So it's, it's an interesting problem, but so far we just pay the scalpers.

**Chris Gammell:** Yeah. It sucks. Yeah. It sucks. But that's probably the right call.

**Dave Young:** If I can pay the scalpers and I can give the student the level of experience I'm trying to give them, then that's going to be the best or the least worst option.

**Chris Gammell:** Right. Yeah. That's true. That's true. Yeah. And it is interesting when you have like reference hardware like that, like, you know, even in a someone else's hackster IO project or something like that, right. It's still the, you know, that's the thing that you're following.

**Dave Young:** And so the other thing is they already have, yeah, you can post comments on their site and sometimes they respond and like, there's all kinds of stuff that comes along with it that makes it work so much better. And it teaches the student, you know, you're not alone. Yeah. It's okay if you don't understand how something is going to come together. Right. Right. You got to have a little faith and just find the next step. Yeah. Yeah. Right. It's not about the last step. It's about the next step. Yeah. So that's, that's all the stuff we're trying to teach. And so it fits. So we'll just, we'll just pay the scalper, pay the man. It sucks. Ugh. Bugs me every time. Yeah. All right.

**Chris Gammell:** Hmm. Well, um, I don't think we're going to call the shortage over yet.

**Dave Young:** No, no, certainly not. It's just not, it's just, it's just not like the, the fire on hair on fire feeling any longer. It's a, it's a problem. Yeah. That's all it is. It's not an emergency. It's not a crisis. It's just a problem. Yeah. You can manage it. You can manage it now. Yeah. The other thing I wanted to talk about was.

**Chris Gammell:** Good. Cause I don't have anything.

**Dave Young:** Yeah. It's okay. I got my notebook here.

**Chris Gammell:** Yeah.

**Dave Young:** Uh, so Amazon sidewalk being opened up.

**Chris Gammell:** Oh yeah. I want to talk to you about this cause I don't think Dave Jones wants to talk about this.

**Dave Young:** Oh, okay. Here we go.

**Chris Gammell:** Yeah.

**Dave Young:** I'm sidewalk.

**Chris Gammell:** So you're excited about this.

**Dave Young:** Yeah. So, and this comes up when we were talking about Goliath is, um, what are, what are my opportunities to get data at a low cost? So there are many opportunities to get data out at high cost, right? Like I can just throw a particle device in somewhere. Sure. And if you can pay the monthly fee, you've got an amazing solution. Yeah. Right there. But if I don't have a monthly fee, uh, if I don't have a product or I don't have a project or something that it can rationalize it, it's not so great. Right. Um, so what if I want something that's a little bit different and this would be another viable option and the fact that they have already paid all they being the consumer has already paid all the money to create the network and maintain the network.

**Chris Gammell:** It's not just a consumer too.

**Dave Young:** Uh, yeah. Right.

**Chris Gammell:** Maybe you should explain what it is.

**Dave Young:** So Amazon sidewalk is where they have a way they connect their devices. And then if you, so then it connects to the internet by way of a router.

**Chris Gammell:** Right. Right. So like certain Amazon ring products. Yes. Uh, I think some of the Amazon router or some of the like wifi euro, right. Things like that.

**Dave Young:** And you would, it would, it's a mesh network, right? No, it's just point to point. It's Laura. Oh, it's Laura. Okay. Yeah.

**Chris Gammell:** So basically they snuck Laura radios into just about everything they've been making. And then they're like, you know what? We're going to turn this on and share your, so like you have to opt in now. It was right. They had that big thing. Yeah. Where they got in trouble. Yep. Yep. But when you, people do opt in and, um, even you just think about the ubiquity of these products, it's not all Amazon products either. It's some products. And, but do you think about the range of Laura? So like Andreas, who's been on the show before, he did testing on line of sight, Laura chirp type stuff. Oh yeah. Yeah. It's like 36 kilometers or something. I mean, it was a mountain, but like just the amount of range you get versus other stuff is, is significant. And so now, now you have all these consumer products throughout neighborhoods where you're trying to maybe track stuff. You're just basically trying to pass stuff back through the network to get it back to some server. Yeah. And, you know, I think actually it's, it's kind of like a, it's an analog to, uh, the Laura WAN based, uh, things, things network. What was that? Was that Sigfox or is that something else? That was Laura as well. Okay. So that's based on Laura WAN. So Laura WAN is basically, you have Laura radios, which are that in the U S is nine 15 and Europe it's eight six eight megahertz. And Australia is nine Oh four. I think.

**Dave Young:** I'm, I'm really impressed. You know, these numbers.

**Dave Young:** Thanks. Or you were able to make them up.

**Chris Gammell:** I, you know, yeah, exactly. You don't really know. Um, and, uh, so there are, uh, concentrators basically. And so a concentrator is basically a, a thing, a multi-channel because there's different channels within, you know, nine 15 is like the base band, but then there's different channels where there's these little slices of, of frequency. And so there's different channels you can receive on. And so like a multi-channel concentrator would be listening for Laura signals on all these different channels. And then it would, uh, it would pass, it would basically hand that message along to over an internet connection to the server. Um, and yeah, um, I think the baby's going off. So you have, so you got a big network that you can tap into. That's right. And so, yeah, the basic idea is if you're, so the things, the things network is a community kind of organized one. And if you have a server in your region and you have a device that is validated to be on the things network, uh, then the packets allowed to go through, it'll be handled along the server and eventually it'll show up at its destination and be good to go. Now, if we think about it, instead of a, uh, community, uh, contributed concentrator, it's just an Amazon device. Yeah. They do, they're doing the same thing.

**Dave Young:** They're opening it up. And so that's what open, that's what makes so much available. And I was thinking initially I was thinking like stuff around my neighborhood I could do or stuff in my community I can do and pass things around. Um, but like I said, if you, so I don't think you have to pay for it. You are, you have to be on AWS.

**Chris Gammell:** You have to be on AWS.

**Dave Young:** So if you're paying AWS, IOT, whatever thing, then, so it sounds like it's a sales technique for Amazon. It's a loss leader. Yeah. I think so. Yeah. And so it makes it so that the product is now all of a sudden viable where before it was not because the per user cost is zero.

**Chris Gammell:** Uh, who's the user in that sentence?

**Dave Young:** The user being the person that has it at their house. Whoever's going to put this device.

**Speaker ?:** Oh yeah.

**Dave Young:** Yeah. Yeah.

**Chris Gammell:** The, this is basically like if, if the, uh, if the things network concentrator was thrown in for free, all you had to do was click a button. Yeah. That's basically this. Right. Yeah.

**Dave Young:** Uh, and that, but that's a huge cost. That's a huge cost. For every other competitor in the space.

**Chris Gammell:** Oh yeah. Right. Exactly.

**Dave Young:** So this is, this opens up a different business model that otherwise wouldn't be available.

**Chris Gammell:** Another analog here is the helium network, right? So helium basically did the same thing where they tried to get people to install hardware and then they incentivize them with a now absolutely worthless coin. Is it absolutely worthless? Cause I switched, they switched to from HNT, which is a helium network token, whatever it was. And that was their currency, their cryptocurrency. And then they switched to Solana recently.

**Dave Young:** Okay.

**Chris Gammell:** Yeah.

**Dave Young:** So does that mean that all your helium tokens are not worthless?

**Chris Gammell:** I think they probably got changed over to Solana.

**Dave Young:** So there was an exchange rate and it was kind of like a buyout situation. I think so.

**Chris Gammell:** I think they didn't want to administer the token anymore. Yeah.

**Dave Young:** Who would? Huh? So, but, so that's how they incentivize people to buy this hardware and then distribute around. You put the right incentives in place and you can do cool things like this. That's right.

**Chris Gammell:** Right. And then you drop the cost of, but that was always my question with the helium stuff is like, it's actually a great model to get consumers to pay for hardware to install.

**Dave Young:** Yeah.

**Chris Gammell:** How do you get, uh, how do you actually, I never heard of them incentivizing the developers to put stuff onto that helium network to utilize all these different concentrators, basically?

**Dave Young:** Yeah. Well, I would assume that the incentive is the same one that Amazon now has. And so they're getting undercut. But if I can put some, I could put a device on helium and I could transfer, oh, but you can't transfer data over it for free. Somebody's got to pay for that in helium coin. That's right. Exactly. Yeah. So that's, it's amortizing that cost.

**Chris Gammell:** Now Amazon is basically saying, well, it's just data. We'll just give it to you for free. Yeah, exactly. We're going to make it up on the backend. Right. When someone, they're going to get locked in with whoever's using this. Yep. Someone's going to deploy a fleet. Yep. And then they'll make it up at some point in the future. And they're locked on AWS. Which is what people can do when they have huge networks. And it's, it's honestly, it's pretty brilliant, right?

**Dave Young:** Yeah, because it's not, it's way cheaper for them to do this than to do other methods of acquiring customers. So to pass that data, they already have the hardware deployed.

**Chris Gammell:** Oh, yeah. Yeah. I mean, it'll be interesting to see what's built on top of this. Because there's, there's a lot of lock-in, but also Amazon's huge. And it's not like people like, it's, it's not a terrible choice, right? No, certainly not. It's not like, you know, Bobby's fly-by-night IoT shop. Sure, sure. It's AWS.

**Dave Young:** And it'll be around for a long time. You can be pretty confident they're not going to run out of money.

**Chris Gammell:** Well, I don't know if I would say it around for a long time. I mean, Google IoT Core is no more.

**Dave Young:** It's not going to be because Amazon's not running out of money, is what I'm saying.

**Chris Gammell:** You never know. You never know. You never know. You never know. You never say never. But it's a safe bet. I think it's a safer bet, yeah. And it's, and it's a, it's a low cost, not low cost, that's the wrong way to say it. It is a, what do I want to say here? It's, it's. The marginal cost for them to do it is cheap. The marginal cost, yeah, that's right. They, basically, the main cost is the, the development of the network. Right. And then. Which they had to do anyways. And then the chip cost that they threw into the, you know, like, it's not cheap to throw a radio in a already low margin product. Right. But they were already subsidizing hardware anyways. Yeah. So, like, this is them probably making that back.

**Dave Young:** Right.

**Chris Gammell:** You know. Right. On a longer timescale.

**Dave Young:** The other thing is they can use that for their products too.

**Chris Gammell:** That's right.

**Dave Young:** So, every product that I could think of, I'm sure is on a drawing board at Amazon right now.

**Chris Gammell:** Oh, yeah. You're right. Right. Right.

**Dave Young:** So, they're putting it in there being like, all right, it's a marginal cost. Once again, it's that marginal cost that they're worried about.

**Chris Gammell:** Yeah. Yeah.

**Dave Young:** It's like, what does that chip cost me?

**Chris Gammell:** Yeah.

**Dave Young:** What does a large chip cost today?

**Chris Gammell:** If I wanted to put one.

**Dave Young:** I have no idea. In a high volume product.

**Chris Gammell:** Semtech. Semtech. SX1276, something like that. You can look it up.

**Dave Young:** Yeah. I'm just curious what it would cost to put one in in high volume, like, one to 100,000 piece quantity. What are you going to pay to add that wireless network to your product? Yeah.

**Chris Gammell:** I don't know.

**Dave Young:** Yeah. Anyways, I'm excited. There's a bunch of stuff I want to do personally with this. And then there's just a tinker around with stuff in my area, because I know everybody has rings around me. And then there's a bunch of stuff that I could see as a potential product.

**Chris Gammell:** It would be interesting to, like, war drive with this sort of thing. Just to be like, I'm just going to take something that's going to blip every second, drive through the neighborhood, and I'm going to see where do I get coverage, where do I not. I'm sure they have maps, too. They have a map. They do have maps.

**Dave Young:** You go on, and you can see what the map is, and my neighborhood's covered in it. And a lot of places are covered in it. Yeah. And the other thing you realize is every place that I would, if I'm trying to design, if I'm trying to make a legitimate business model product, 95% of my customers, customers that would be wanting something that's connected, it's probably already got an Amazon Ring product. If not in their house, in their neighborhood.

**Chris Gammell:** Oh, yeah. You're saying, like, the lookalike audience.

**Dave Young:** Yeah.

**Chris Gammell:** Right. If you're looking at your typical customer, they're going to be covered by Amazon Sidewalk. Right. I think that's probably right. And I think, I don't think Amazon's the last to do this. I'm sure Apple's working on something similar. They already have, like, the Find My Network, right? And that's on phones. Yeah, right. That's Bluetooth-based, kind of a similar stuff. I'm not sure if other developers can get onto that, but... I'm sure the answer is no. Well, they have, like, the MFI service, whatever it is, where you can, like...

**Dave Young:** Are you familiar with what it takes to do MFI?

**Chris Gammell:** No.

**Dave Young:** It's a pain in the neck. Yeah. It was. I looked at it years ago, like, six or seven years ago.

**Chris Gammell:** Okay.

**Dave Young:** And, like, you have to be brought in. You have to go through all this legal stuff. You need a chip on your stuff, right? You need the chip, but even to get the data sheet, you have to be in the system. Oh, wow. Okay. And so, and there's, like, all this stuff you have to do legally and business-wise and competitive-wise. Like, they don't make it easy to just be, like, give me that MFI chip so I can put it on my board. The answer is no. Yeah. Right. So you have to be another big co. And to their point, they want to make sure you're holding their standards. Right, right. Because you could blow up their customer experience, and that's what they sell on. Yeah. So I understand the point, but I am not super optimistic that they would let you on there real easy.

**Chris Gammell:** Yeah. I'm wondering if we need to amp up this amp hour experience by this auditory quest that we were on by bringing a baby into it. Yeah, sure. Let's get the cacophony going. I think. So just, okay, so let's just call this 40 minutes of a normal show, and we're about to go. We'll see what happens. We're about to go to bonkers mode. We'll see what happens. I got a couple kids myself. This is called dad life. Dad life. Hashtag dad life. Yeah, that's right. I'll be right back.

**Dave Young:** I'm going to, while you're gone, I'm going to talk about the. Oh, you are? Yeah. I'm going to talk about. Don't say anything weird. I'll say lots of weird stuff. Okay. About the home appliance stuff. Oh, yeah. Yeah. So I've got, so I've got a problem. My mom has a stove in her condo that is, you know, it's eight, nine years old, maybe 10 years old. She's got a stove in her condo that she put in, and the front panel failed. Uh, so that, you know, all the lights, all the buttons are gone. You can't see anything. And so my brother takes it apart. He looks at it, and he's, I don't know. This is definitely electronics problem. So he gave it to me to check out. Um, and I looked, I was like, okay, let's look. Let's see if we can get something online. Uh, my brother Hunter, he looked for me, and actually he looked, he took the initiative and looked himself, and he said they have refurbished units, because they obviously don't make them anymore. The parts are gone, uh, from the factory. They have refurbished units, but they're $450. So now we got to decide, like, okay, we have a stove that would probably take between one and $2,000 to replace, and a real pain in the neck to get up to a condo, or a refurbished board on a 10-year-old stove, which may have another thing fail in who knows when. So neither of those options are particularly good. Uh, so he sent the board out to me to look at myself, and I checked it out, and I found the problem was they have an LDO, and they've got a low dropout regulator that's generating the 5 volts for the whole board, and next to the LDO, there are these two 1206 resistors in parallel on the input line. So you've got a couple resistors coming in from the power source, which I'm not sure what it is yet, and it goes through these resistors into the LDO, which then generates the 5 volts. So we have the 5 volts that are supposed to come out, and this is a technique that I've seen in a bunch of different designs, where instead of doing a switcher, you're cost-sensitive, or you're space-sensitive, well, not really space-sensitive, but if you're cost-sensitive, you can put a cheap LDO in, and then if it's too much power for the LDO to consume, you can add a couple of resistors in line with that LDO, where you know that a lot of the power, the bulk of the power, is going to get chewed up by the resistors, and then you still leave the LDO there to regulate the voltage outside of that. So I look, and the two resistors on the way in have obviously charred, and they're smoked. Not totally smoked. It looks like they have slowly been baked. So it's got, instead of like a flame-looking char, it's got almost like a tan or a dark hue to the PCB around the resistors, and then the solder looks all kind of funny, and the resistors don't look great. And so sure enough, I see the baked components, and I check the resistance, and it's very clear that the resistance is open. The resistors are open, totally fried, not working at all. So my immediate response is, I'm just going to replace these 1206s, and we'll be back in business. But I thought if it failed once, it's going to fail again, and I don't want this to be the thing that fails the second time. So instead of using two 1206s, I used four 1206s, different resistor values, so it's still the same resistance, just a lot more surface area for the heat to be dissipated. If you're hearing that crinkle, that would be Chris getting some goldfish for his daughter, and they look so tasty. I'm back. Anyway, so I have the board fixed. My brother's going to put it in this weekend, and hopefully we'll find out, you know, what are we working with? Is this something that is going to fix it or not? I'm pretty sure it's going to fix it. At least I checked the 5-volt regulator, and the 5-volt regulator now runs, where before it didn't.

**Chris Gammell:** I actually didn't get the whole... I didn't get all the details here.

**Dave Young:** Yeah. Well, long story short... I'll go listen later. ...is the designers blew it, and they put too much heat through resistors, and over 10 years it failed. Yep. So, I mean, there could have been another short down the line, and the resistors acted like a fuse, but it didn't look like that. It looked more like baked parts. Mm-hmm.

**Dave Young:** So, I was really frustrated that I have this stove, which hundreds of pounds, like a lot of weight, a big hassle, a big amount of money that failed because of a rookie mistake. Right? It feels like most people would just throw out the stove, too. Most people would throw out the stove. That's crazy. And so now you've got all this stuff in a landfill or best-case scenario recycling place, and then a whole new several hundred pounds of stuff that I have to buy of virgin material.

**Chris Gammell:** Right, right, right.

**Dave Young:** So, the whole thing feels so icky. Why do you hate stimulating the economy? What's wrong with just consuming, over-consuming, and consuming more? So, I'm really frustrated. This whole scenario, and it all comes down to a rookie mistake that a five-minute design review would have been like, you can't do that.

**Chris Gammell:** Yeah.

**Dave Young:** Like, you can, but you're going to mess up a bunch of stuff, and it's not going to last. And there's, of course, the cynical side of things. Are they doing this on purpose so they make you buy a stove in 10 years? Yeah, right. Like, the planned obsolescence, like, ha, ha, ha, ha, ha. Not only am I saving a nickel, I'm also making $2,000.

**Chris Gammell:** That's right. That's right. I'm building a job for myself.

**Dave Young:** Yeah, right. And that whole thing just feels so smarmy to me. I mean, you really got worked up when we were upstairs, huh? And, yeah, I do. Why don't you leave me alone? What's going to happen?

**Chris Gammell:** Don't leave this man alone with a microphone.

**Dave Young:** Just hi to Dave.

**Speaker ?:** Hi.

**Dave Young:** Hi.

**Chris Gammell:** That's my daughter. She's now noshing on goldfish crackers.

**Dave Young:** Who doesn't like a goldfish cracker? I mean... They're delicious. Yeah. Anyway, so I'm not sure how to solve this problem, but it feels like there is value to be had, where the consumer wants to buy one stove in their life, maybe two.

**Chris Gammell:** I don't know. Well, what is their... I don't know. I see, like, new smart devices and, like, all of the stuff that's in there. Like, oh, we have an air fryer now.

**Dave Young:** Okay. Yeah. Buy one separately, I guess? I don't know. I don't know. I don't know. The smart devices... Do you know anybody that wants their phone or their stove to be connected to Wi-Fi?

**Chris Gammell:** Yeah, and I see the things that, like, people, like, go gaga over that June oven. You seen those things? I have not. It's like a toaster oven, basically, and it's got, like, a down camera, and then it's got, like, a QR code scanner. And so the business model is, like, you order these...

**Dave Young:** Don't tell me you buy your food from them. You do.

**Chris Gammell:** Stop it. It still works. It's not like it, like, locks you out from using it as a toaster oven, but if you wanted to have, like, these pre-made profiles, and so it just cooks it, and you don't have to think about it.

**Dave Young:** So you just know.

**Chris Gammell:** You just know.

**Dave Young:** I could see that, because so many pizza joints that you would, like, go and pay money for aren't any different. Right? Yeah, exactly. They dial in one thing.

**Chris Gammell:** You're just paying a 16-year-old kid to do the same thing.

**Dave Young:** Yeah. Right.

**Chris Gammell:** Yeah, that's your monitor.

**Dave Young:** Yeah.

**Chris Gammell:** So anyways, I'm sitting here thinking there's... I mean, let's go on the childhood track. How are you teaching your kids electronics?

**Dave Young:** So right now, it is... They get to come out to my lab, and they get to ask me questions, and... That's nice. We get to... Your kids are... We get to do stuff.

**Chris Gammell:** Below 10.

**Dave Young:** Yeah. Right. So they're elementary school age.

**Chris Gammell:** Yeah.

**Dave Young:** I'm dreaming of the day when I can have them build boards for me, and I think it's coming. And I think at least my older son is interested. That's good. I don't know if my younger one will be or not. It's too early to tell.

**Chris Gammell:** I'm sorry.

**Dave Young:** But they are both very much interested in the lab, which is a great sign.

**Chris Gammell:** That's good.

**Dave Young:** They might be interested because I'm interested, and it's fun to do with daddy, and they always know they can get positive attention, but what a great way to...

**Chris Gammell:** Well, other Dave, he's trying to get his kids into electronics, it seems, and I think that is the dream, but you also don't want to force them.

**Dave Young:** Yeah, well, I'm going to pay them.

**Chris Gammell:** Well, that's one way to do it.

**Dave Young:** Right? Like, giving them a whole bunch of money to come and build boards? Oh, yeah.

**Chris Gammell:** Yeah, of course. Right?

**Dave Young:** And they can make more money building boards for me than they can working at McDonald's. Sure. And it's going to be way better. They can sit there and watch Netflix while they're doing it and assembling boards. Oh, absolutely. You've never watched Netflix while building boards?

**Chris Gammell:** I have done it for my personal boards. I'm just saying I'm not going to let a kid do it, because when I was a kid, I was so locked in the screen, I'm going to burn my finger off. I guess you learn pretty fast there, too.

**Dave Young:** Yeah, that's true. That's true. I mean, they wouldn't watch some show they've already seen 100 times.

**Chris Gammell:** Do they only get paid for working boards? No.

**Dave Young:** Yeah, I see what you're saying there. That could be tricky. But yeah, so I involved them. When I went to Supercon, you know, they had the badge.

**Chris Gammell:** Yeah.

**Dave Young:** They loved the badge.

**Chris Gammell:** Ah.

**Dave Young:** And it was...

**Chris Gammell:** I do think, like, Blinky. Like, I thought about, like, building something for her.

**Dave Young:** But they loved it way more, because it was all exposed. Yeah, of course. So instead of being in that plastic case, like the little video game things are, whatever is...

**Chris Gammell:** Which badge did you get? You got the...

**Dave Young:** I got the... The Game Boy? So both of them. So the little Game Boy one that was on the Adafruit board, and then the big one that had the big screen with the Flappy Bird and the...

**Chris Gammell:** Right.

**Dave Young:** Yeah. So the Flappy Bird game they loved.

**Chris Gammell:** That was 2019. That was made by Sprite.

**Dave Young:** Yes. Yeah. Right. It had, like, an FPGA on it. Yeah, it was, like, a legit piece of machinery.

**Chris Gammell:** I sold mine for $350.

**Dave Young:** Stop it.

**Chris Gammell:** Yeah, I gave it to Girls Who Code.

**Dave Young:** Oh, that's awesome.

**Chris Gammell:** That's the way to do it. Go to Supercon, sell your badge, donate the money.

**Dave Young:** Donate the money. That is the way to do it. Yeah. $350?

**Chris Gammell:** People love those badges. I mean, that one was particularly good. I mean, the last one was, too. Like, the... Yeah, that one was particularly good.

**Dave Young:** Like, you could do so much with that. Well, anyways...

**Chris Gammell:** Yeah, it's basically a dev platform.

**Dave Young:** That's what I'm doing, is I'm trying... The same way I do it... Mama! Oh, Mama's home. Oh, look at that. The same way I do... Blue Stamp is the same way I'm dealing with my kids. Ah, yeah. First, you make it exciting for them. Figure out where they are.

**Chris Gammell:** That's tough, yeah.

**Dave Young:** How can you make it exciting for them?

**Chris Gammell:** Yeah.

**Dave Young:** And then build from there. And it doesn't matter if they're building boards for me, or they're sorting parts for me, or they're playing with the Flappy Bird game. Like, it doesn't matter. As long as they're involved and they are growing that involvement, you're winning. Yep.

**Chris Gammell:** Yeah, I think that's right. And I just think about, like, accessibility. Like, I don't know. Like, I feel like I would probably lean in a little too hard on some of the stuff. Be like, isn't this so cool? And then that makes it not cool, you know?

**Dave Young:** Oh, 100%.

**Chris Gammell:** Yeah.

**Dave Young:** And Chris, I gotta tell you, you personally are very vulnerable to that happening with your children. Yeah. You are overly dad excited about many things.

**Speaker ?:** Oh, yeah.

**Dave Young:** Yeah. And you might run that risk, for sure. Yep. I feel like I might be a little more loose. Be like, yeah, that's cool, but you know what I mean. Yeah, yes.

**Chris Gammell:** I guess I know how to control electricity, but no big deal.

**Dave Young:** I mean, I can show you all kinds of cool waveforms on the scope.

**Speaker ?:** Yeah, I mean, yeah.

**Dave Young:** If I can make an LED blink. Yeah, right? Yeah. You want me to change the color? Yeah, right. Exactly, yeah.

**Chris Gammell:** I think that actually is the right... I mean, for really any beginner, the right way to entice people is LEDs.

**Dave Young:** Uh-huh. Yeah. Sure. And usually it's blue. Why is it that the blue LEDs are so much more enticing than all the other ones?

**Chris Gammell:** Oh, I think the NeoPixel style, like...

**Dave Young:** Right, right, right. But if there's one color... Your daughter today was looking at the... The washing machine. The washing machine. Or dishwasher. The dishwasher, and it's blue. And I'm convinced if it were red, it wouldn't be nearly as interesting.

**Chris Gammell:** Really?

**Dave Young:** I don't know. The blue is very noticeable. It definitely hits our... That's true. Our eyes differently. It hits your eye different. Yeah. That's true. That can be... By that measure, green is also very interesting, and green hits your eye differently, too. So... Yeah. Maybe that's it. Humans are just built to pick up green and red, or green and blue. Yeah. Who knows?

**Chris Gammell:** Yeah.

**Dave Young:** But blue LEDs is how you sell electronics.

**Chris Gammell:** No. I think that's how you blind people.

**Dave Young:** Both?

**Chris Gammell:** Both. Yeah.

**Dave Young:** Yeah.

**Chris Gammell:** You ruin their night by blowing out their cones or their... Yeah. Whatever it is. Yeah. Yeah. Yeah. I don't know, because I feel like just... I think about how she's going to grow up with just screens everywhere, and I am addicted to screens. Oh, absolutely. She's going to be addicted to screens, but how do I make it so that she's interested in what's happening behind the screen, you know?

**Dave Young:** Well, so that's the... And for me...

**Chris Gammell:** And not as a content creator as well, by the way. Right.

**Dave Young:** Well, that's what we talk about all the time. You and I have talked about is the difference between using a device to consume and using a device to create. Yeah. That's right. And so using a tablet's no problem if you're creating, and you're doing something. The tablet is your tool, and it's not your distraction. Right.

**Chris Gammell:** And I don't care if her or future kids care about... I don't care if they do electronics, but I do care if they're creators versus producers, and not creators like content creators, but just people doing...

**Dave Young:** Bringing something new into the world.

**Chris Gammell:** Bringing something new into the world. Right. Don't just sit there.

**Dave Young:** And I think as long as we're chasing after that, ministering to that, then you're raising your kid in a way that is conducive to the human experience. Right. Yeah, I think that's right. Yeah. You know, people innately would like to create, and so showing them the path to get that dopamine hit when it hits. I don't know if I agree with that.

**Chris Gammell:** Really? You think innately they like to. I think innately we are bags of salt who will sit there watching the tube all day, if given the choice.

**Dave Young:** Yeah. I don't know. I don't know. If that were true, though, would we have ever broken out of our early civilization days?

**Chris Gammell:** Well, there's other motivating factors. That's true. That really drove a lot of that stuff. Yeah, right. Money, power, sex, the usuals.

**Dave Young:** Yeah. Yeah, those are also innate. But I think creation's in there. I'm not going to say it's more powerful than money, power, and sex, but I think it's on the list. To create something new that wasn't existing before, I think is in there. Oh, I might be part of it.

**Speaker ?:** Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Chris Gammell:** Yeah.

**Speaker ?:** Sure.

**Chris Gammell:** Sure. Sure. Sure. We're having a little bit of swap out here. Yeah. Our... Yeah. Our... Our... Oh, yeah. Yeah. We're having fish while we record. Yeah. Yeah. Here we go. Thank you. Doesn't care more real than that.

**Dave Young:** Youngest amp hour guest yet.

**Chris Gammell:** That's true.

**Dave Young:** She did. Yeah.

**Chris Gammell:** You mean my wife? Both. Yeah. Two of the youngest and most beautiful guests ever to be on the show. Ever to be on the show. Yeah. Ever. And brilliant. Brilliant.

**Dave Young:** Send this to her. Yeah. Just a clip though. Yeah.

**Chris Gammell:** Right. That's... I mean, it's interesting what... You know, just thinking about that stuff. I haven't thought about it too much, honestly, because my daughter's not... Yeah. She's not ready yet. At school age yet. Yeah. So... And I think even in school age, she probably won't get exposed to stuff. Yeah. Like, there's like a lot of early programs, but they're kind of more targeted to your kids' age. Yeah.

**Dave Young:** And even in my kid's age, I haven't found... They have them and they're great.

**Chris Gammell:** And what we were talking about, like the Mark Rober box and... Yeah.

**Dave Young:** So they have a ton of cool stuff.

**Chris Gammell:** Yeah.

**Dave Young:** And, you know, when I was growing up, it was fun to have activities and toys and things that were building related. Yeah. The thing about the...

**Chris Gammell:** I had all that stuff, but that didn't do it for me. Like, it was Legos, I'd say. Legos, absolutely. Yeah. Legos are a common thread, I feel like, throughout the...

**Dave Young:** Yeah. The other thing that did it for me, and this was... It was a big deal in the early 90s to have a computer.

**Chris Gammell:** True. Yep.

**Dave Young:** And so I had a computer in my house. Yeah. And at my school.

**Chris Gammell:** Yep.

**Dave Young:** And so being able to do... Really, that was the trick. That was the magic, was being in school with the computer and like learning from a teacher who knew what was up and then being able to apply it at home at my own pace and my own interest. I think that's probably the magic is you get the basis from someone who knows what's up and then you let your own direction form. Yeah. Yeah. Yeah, that's a good point. And then you really solidify both the love and the ability.

**Chris Gammell:** I do remember... I remember one of my good friends growing up, his grandfather was an inventor.

**Dave Young:** Yeah.

**Chris Gammell:** Not a particularly good one, but he had a workshop that we were allowed to plan. Yes. And that was the jam. That was like we made some of the stupidest things ever. Sure. But that was like the desire was there, you know?

**Dave Young:** Yeah. And I think a lot of it is about the autonomy and the... Like you are given the opportunity to make what you want. And I'm sure he didn't walk in and be like, hey, here's your kit.

**Chris Gammell:** Yeah. Right. Yeah, there is that too, right? Yeah. A lot of this stuff is kind of prefab, like, oh, I follow the directions, whatever. When do you make that switch over from like... Not saying that I did. I don't think I'm a good example in any of this space. But that is an important thing to be like. You don't always have to follow the directions. You can go use what you've learned and figure it out. It's like... Or come up with your own ideas. Come up with your own ideas. But then you have to almost just be like, that's harder, but might be more rewarding. Yeah.

**Dave Young:** And it's worth going to do the work.

**Chris Gammell:** Right.

**Dave Young:** Exactly. Yeah. And that's the thing with all the kits, which are spectacular. I like the kits. Yeah. Thimble. Are they still going? Thimble at IO? Oscar. Oscar's thing? Yeah. I thought he did a great job. His kits were great. And I bought some for my cousin.

**Chris Gammell:** I think he's going still. And David too. Is that right? David? I never met the other fellow.

**Dave Young:** But I got those for some of my cousins when they were appropriate age. Yeah. And they were great. The problem is with those is you have to involve the student in the picking of the project. Yeah. So I got them. And that was my experience was I got them a kit that I thought they would like. And it was a risk. And the thing is, they don't own it.

**Chris Gammell:** Yeah. Right. Right.

**Dave Young:** They're doing it because I said it would be cool and fun. It's like, I don't know if it'd be cool and fun. I haven't done it. Right. Right. They haven't done it. And so in order to make.

**Chris Gammell:** The shopping experience matters.

**Dave Young:** In order to make that leap. Yeah. So like, I'm going to put the time in to see if it's fun. It's got to be your thing. Yeah. That's true. It's got to be your jam. So if I were to do those kits with my kids, I'd sit them down and I'd be like, hey, which one's cool? Yeah. Yeah. Right. Like, which one do you want to do? A little market research.

**Chris Gammell:** Yeah. I think about this. You know, we were talking a little bit about like, you know, kind of persistence. We were talking about music training. Yeah. But like persistence in that way too. And like, I think that kind of tracks in this space as well. Like things are going to go wrong by, I mean, in blue stamp. Yeah. Right. In music training. And that's good. In learning electronics. It is good, but it's about how you respond to it and like how you, you know, it's not like you have to keep going, but you, it's like trying to get that switch over to, you want to keep going. You want to keep going. Wouldn't it be cool if we kept going and you do this? Right. Yeah.

**Dave Young:** I love that phrase. Wouldn't it be cool if.

**Chris Gammell:** Wouldn't it be cool if. Yeah. And one of the things I mentioned is like, I think the best, the best possible scenario you can get is if you have a friend who you get to push each other with. Right. If you can find a friend who's like pushing you and be like. Right. Like, wouldn't it be cool if we tried this other thing and let's keep playing? Like, how do we keep playing? How do we keep the game going? You know?

**Dave Young:** And a little bit of competition. A little competition. It's tough. I remember that. Right. Yeah. I had, I bought an RC car, like a build RC car. Yeah. It was like a big, it was all my money. Yeah. Like all my money, which was a big deal. Yeah. And I bought it and it took a long time to build a lot of intricate parts and stuff. But at the end.

**Chris Gammell:** Did you have a buddy doing it the same way?

**Dave Young:** And I had a friend that would do it. And I'd call me how far you get with stepping on.

**Chris Gammell:** Oh man. That's, that's killer. See, now you think about origin story. That might've been it right there.

**Dave Young:** That could've been, that could've been it. And that was just an RC car. Like, there's nothing hard about that. The little receiver is this little servo that goes on.

**Chris Gammell:** But you got it working?

**Dave Young:** Got it working. And it was fat. Like it was, it was the ones they, it was the ones they like compete with. It's like a grownup hobby car. Okay. That I, so you run it on the street and you're like, man, that is fast. That is awesome.

**Chris Gammell:** That's going to ruin someone's toe.

**Dave Young:** Yeah. Or worse, ruin the car. Yeah. But the cool thing was I ruined it many times and I would just.

**Chris Gammell:** Figured out how to fix it.

**Dave Young:** I would just figure out how to fix it because I knew where to get the parts.

**Chris Gammell:** Yeah. Fixing is another thing that's important. You know, I, just again, you know. And improving. I'm 630-ish shows in. Someone else would fix their car. 630 shows in. I've asked a lot of people how they got into electronics or engineering or whatever. And it, Legos is always in the story. Not always. It's often in the story. Fixing. Yeah. Like some kind of fixed culture, which you and I both had in our first co-op as well. I think some kind of mentor figure. You know, just think about if we were trying to replicate this. If we were trying to make it formulaic, not saying it's the right call. If we're trying to make it formulaic, what does that look like?

**Dave Young:** Right. Yeah. That is a good question. I think anything. And the other, the fourth piece of that, which is more of a wild card, not as a thing you need, is the opportunity. Is everybody in their whole lives have, everybody in their whole lives have a phase of life that they're in or a mood that they're in or whatever. And you have to capture it at the right moment. They got to have the time.

**Chris Gammell:** They got to have the inclination. Privilege in there too, right? I mean like. For sure. Right. We're all, we were in good educational spaces. Yeah. We had the resources, all that.

**Dave Young:** And then with the privilege comes, I think what the privilege comes down to is the number of opportunities. Yeah. Opportunities you get. Yeah. Where you're in a place where you can grow. Right. And so. Yeah.

**Chris Gammell:** I'd say college is about four years of opportunity. Yeah. Exactly. And many different chances. Yeah. And I messed up a bunch of them. Good. Let's say five years of college for me. Yeah. Right. Well, the co-op. You get the count. Yeah. I know.

**Dave Young:** I know. Co-op counts. Yeah. Yeah. Yeah. But that's the edual question, right? Yeah. Yeah. How do we make ourselves and our society better by teaching? And these are all great places. And it really is all about just trying. Just really make a good effort and it'll work out. Okay.

**Chris Gammell:** Maybe.

**Dave Young:** And if it doesn't, then try again.

**Chris Gammell:** Yeah. Yeah. We hit an hour. I'm surprised it's been an hour. This is a fast hour. We did it. We did it. Yeah. I kind of popped this on Dave when he showed up on Friday. Yeah. Or just before. Yeah. I was like, hey, we're recording Ampar.

**Dave Young:** It's best to not think about it. Yeah. That's right. And to just dive in. Yeah. It's one of those things like cliff diving when you go into the pool. Oh, yeah. Don't look down. Yeah. You don't think about it.

**Chris Gammell:** You just run off the ledge. Yeah. Right. Right. Right. Makes it more entertaining. I actually don't run off the edge, personally. I'm not a cliff diver myself.

**Dave Young:** No. But you did here. Here we are. You put it together. Made it go. Oh.

**Chris Gammell:** No. I have jumped off a cliff many times for the Amp Hour. Don't worry about that. Yeah. I know. I know. All right. Well, thanks for being here, Dave.

**Dave Young:** It really is my pleasure. And I got to, for other guests, when you're here in person with Chris, it's way more fun and it's easier. But you have to really be careful because he keeps trying to tell you to do different things and do this with the mic, do that with the mic, and you actually have to do it. Oh, yeah. I suppose when I'm at home, he doesn't know what I'm doing. Yeah.

**Chris Gammell:** Like when you're a thousand miles away, I can just tell you all day. Yeah, I can do whatever I want.

**Dave Young:** I can keep hitting the desk. I can do whatever I want. There's nothing you can say because we're on air. Yeah. But now, you can just look at me with his finger.

**Chris Gammell:** Yeah. Don't do that.

**Dave Young:** Don't do that. All right, man. Thanks for being here. My pleasure.

**Chris Gammell:** Bye.

**Chris Gammell:** Bye.

**Speaker ?:** We'll see you next time.
