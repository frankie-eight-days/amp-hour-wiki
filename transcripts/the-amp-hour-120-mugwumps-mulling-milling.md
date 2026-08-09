---
episode: 120
title: Prototyping, Machining & Accelerators- Mugwumps Mulling Milling
url: https://theamphour.com/the-amp-hour-120-mugwumps-mulling-milling/
---

**Chris Gammell:** This episode of the Amp Hour is sponsored by Club Jameco, part of Jameco Electronics, a leading component distributor for over 35 years. Club Jameco allows you to upload your kit ideas and start selling to your peers and the public at large. You never need to purchase large lots of components up front or bag and ship your kits. Sign up and submit your design, and if it's chosen by the community, you can start making up to 10% on the cost of your kit. To learn more and see some of Chris and Dave's favorite kits, go to clubjameco.com slash theamphour. This is the Amp Hour Podcast, recorded November 4th, 2012. Episode 120. Mugwumps. Mulling. Milling.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of ChipReportTV and Chris Gammell's Analog Life.

**Dave Jones:** What about that new intro?

**Chris Gammell:** Hey, hey.

**Dave Jones:** Hey, hey.

**Chris Gammell:** That's something different for us, huh?

**Dave Jones:** It is. We actually have a sponsor.

**Chris Gammell:** Yeah.

**Dave Jones:** After, what, a year and a half? How many episodes? Almost 120-something?

**Chris Gammell:** Oh, well, it's been two and a quarter years now. I mean, we started in August. Over two years? Oh. Yeah, we're in two years.

**Dave Jones:** I don't think we even mentioned our two-year anniversary, did we?

**Chris Gammell:** No, because it was really close to the 100th episode, so it was like, eh, whatever. Ah, right. Okay. Yeah.

**Dave Jones:** Of course, because this is weekly. Yeah. Right. We've been 104 or something.

**Chris Gammell:** Yeah. So, we finally got there, though. Two and a half years in, two and a quarter.

**Dave Jones:** And we're in the big bucks. Woo-hoo!

**Chris Gammell:** Not really. Jameco.

**Dave Jones:** Yeah. No, not really, but Jameco are sponsoring this episode, so thank you very much, Jameco.

**Chris Gammell:** Yeah, and we'll talk a little bit more about them later in the show.

**Dave Jones:** Yep.

**Chris Gammell:** So.

**Dave Jones:** So, they will be there. It's a trial. We're going to do it for a few weeks, are we not?

**Chris Gammell:** Yeah, a few weeks. Yep. See how it works out. A few weeks.

**Dave Jones:** And if people click through the link, please do. Check out Jameco's stuff, if you haven't already. Check out Club Jameco, and if they get a good response, then they will continue to sponsor us here at The Amp Hour, which is excellent.

**Chris Gammell:** Yeah. I'm excited. Hopefully, you know, some extra money can help us do some extra stuff, and it should be fun. I'm excited.

**Dave Jones:** I'm going internally berserk. That's how excited I am. I can hear it. Yeah. You can hear it? All right. Excellent.

**Chris Gammell:** You're so low-key, usually, and right now, I mean. Okay. Yeah. Just calm down, Dave. Just calm down. All right. Breathe in. Yep.

**Dave Jones:** Breathe out. Just breathe. Okay.

**Chris Gammell:** Yep.

**Dave Jones:** So, did you survive the storm? Did it hit you in Cleveland there?

**Chris Gammell:** It did. You know, there was some footage of, like, you know, like, crazy flooding and everything else. It was on Daily Show, actually, and they zoomed out, and they're like, this is in Cleveland.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** Or underground car parks flooded. And have you got, like, an underground subway system in Cleveland?

**Chris Gammell:** We do in certain parts, yeah. Right. Okay. It depends where you were. Certain parts of Cleveland were worse than others. I'm in, like, the southeast corner. It was... Yep. It was nasty out, but it wasn't, I mean, it wasn't, like, New York, and it, I mean, even the west... Cleveland's actually split in half by a big valley. Right. And, um... And on the west side, I'm on the east side, um, it was everything. Power's... I think power's still out in some areas. Right. So, it's, uh... Yeah, man.

**Dave Jones:** Seeing all that footage, it's rough. Did, like, the entire New York subway system get submerged or something, or...

**Chris Gammell:** Yeah. Yeah, man. It just flooded like crazy.

**Dave Jones:** The thing I don't understand is, how does stuff work after that? Like, surely the whole system... You know, the whole system would be buggered. Right? All of the electronics, everything would be ruined. Yeah. Wouldn't it?

**Chris Gammell:** I don't know.

**Dave Jones:** I mean, is it up and working again? Like, sure, you know, yeah, they pump the water out, or the water drains out naturally, or something like that, you know, so eventually the water goes, but then everything would just be cactus, wouldn't it?

**Chris Gammell:** I know certain lines are back up in New York City, but I know a lot more are down for weeks, like, big time, and I think the stuff, like, on the south end of Manhattan are pretty bad still. I mean, like, and they're still without power and everything else.

**Dave Jones:** I can't believe it'd only be weeks, you know? Right.

**Chris Gammell:** Yeah, you'd think they might have to rip stuff out and, like, redo it, but, I mean, track's not gonna... I mean, like, the track and the cabling...

**Dave Jones:** Oh, no, tracks and things would be fine, and, you know...

**Chris Gammell:** Yeah, maybe, like, switch gear. I don't know. It depends. And, uh... Yeah. It depends on how much they design that in from a, you know, like, do they have to design against waterproofness? I don't know.

**Dave Jones:** Are all the boards conformally coded and, you know, stuff like that? Right. Well... I don't know. If anyone knows...

**Chris Gammell:** Yeah. If you look at the era that that stuff was... I mean, they do updates here and there, but, I mean, there's some old stuff running those trains. I mean, that's not...

**Dave Jones:** I've been on the New York subway system, and it was the most dilapidated rundown system. Right. You compare... Oh, shit. I'm scared. This thing's going to collapse, you know? Like... Oh, no.

**Chris Gammell:** I wouldn't worry about that, but, I mean... You compare, like, Shanghai, like, a brand new... Oh, yeah. No, it's... Yeah. You know, a huge subway and New York, and it's like... I mean, New York's still got a good subway, but...

**Dave Jones:** It just looked like it hadn't been maintained in 30 years. Like, yeah, they built it 30 years ago, and they haven't touched it since. You know? That's the impression I got. Yeah.

**Chris Gammell:** Well, it's tough, because, you know, when you have such a highly utilized system... I mean, electronics designers run into this, too, right? Like, how do you design a maintenance schedule for something that high... That high utilization, right? I mean, in industrial situations, you have to have, like, redundant cards and have things, like, switchable and stuff like that, and it's a really tough problem.

**Dave Jones:** I've been involved in that. You know? You would have to bring the production line, which operates, you know, all day, all night. You know? It operates 24 hours a day, seven days a week production line. You've got to bring stuff down for maintenance. It's like, well, you know, look, we're going to lose, you know, $100,000 an hour if you don't... You know? It takes you two hours to fix this instead of one hour. You know? I mean...

**Chris Gammell:** It was like the chip fab, too, where they had to bring down... Because eventually, basically, eventually, wafers dirty up the chambers, right? And eventually, you have to switch out these quartz kits that are inside of them. This is for, you know, dry etch. And so, they'd have to bring them down, and then, you know, just pumping them down takes long enough. But, you know, like, if... You know, then you have to test them, and then you have to verify them, and, you know, and there's just tons of crap to just get stuff back online. And like you said, I mean, the cost with that, you know, when one machine goes down, you just... Not only do you have the lack of capacity, but you have this big pile building up behind it, because it's designed for 100% utilization, right? And it's just a mess. You want to talk about a bad time when the power goes out, it's a really bad time when the power goes out in a fab, because all of... Like, especially, you know, like, a dry etch chamber, if you look at it, like, you know, like, there's all these chemicals and everything, and they're, like, eating away at wafers or whatever. And it's effectively, like, you know, it's a vapor cloud in there. It's a plasma. And there's a plasma near the surface, and there's, like, a vapor cloud. You turn the power off, though, and all that crap that's hanging out above a wafers and the fridge goes, voom, and it just ruins every wafer, and let alone the ones that are in chambers where a robot just then goes and smashes it into a wall because the power gets shut off.

**Dave Jones:** And you would have hundreds of wafers in there, right?

**Chris Gammell:** Right, yeah, full fab. Yeah. Thousands of wafers, right? Yeah. At a time.

**Dave Jones:** They're in these huge chambers, right? They're getting all the stuff deposited on them and stuff like that. They won't do it one by one. They'll put them in a big, huge, big chamber, and there'll be thousands of wafers, yeah?

**Chris Gammell:** Right. Oh, yeah. So, like, for, like, when you're, oh, crap, what's it called? Like, annealing something, so you're actually, like, growing, you know, an epitaxial or something like that. Yeah. You know, like, that actually, you put in, like, four lots at a time, so that's, like, a hundred wafers in just one machine. So, if that shuts down, you know, you're screwed, and that's a big heater. It's a big oven. So, yeah, that's just, I was never there when it happened, but I've heard stories of just, like, beepers going off at, like, two in the morning, and, like, everyone in the company coming back in at once. Yeah. Yep.

**Dave Jones:** Crisis mode. So. Yep. I worked in a factory for, oh, man, like, a good decade off and on, right? And I actually can't recall the power failing at all, really. I mean, it was extremely rare if it did, or there would just be a momentary glitch and everything at reset. Yeah. So, I think we have it pretty good here in terms of power and stuff like that. Yeah.

**Chris Gammell:** Right. Well, I mean. Some areas are a lot worse. I know that the, there was also a, I heard a rumor, I'm not sure if this is true, but I think it is. I heard a rumor that they, that the fab I was at had a deal with the power company that they were buying so much power anyways because fabs take gobs and gobs of power. Or that if, if there was a preventable outage from the power company, that the power company was responsible for all the ruined wafers. Oh, really?

**Dave Jones:** Wow.

**Chris Gammell:** That's a hell of a contract to sign, right? That is, right?

**Dave Jones:** Your hand shaking as you saw in that sucker, right? Exactly. Exactly. Holy crap. Oh, man. Yeah.

**Chris Gammell:** And, you know, from a, you know, my heart really does go out to all the people down in New York. It's a, that's a dense city to start with. Why not? But it just, it just points out like how fragile the grid is, you know, like I've been seeing all these articles all week about, you know, just what could have been done and sometimes it's just nothing, right? I mean, like, unless you put, even if you put all this power equipment up on, you know, 20 foot platforms, right? The platforms could blow over, right? I mean, there are certain things that are just not going to stop nature. Mother nature is in charge. Always wins. Yeah. And it's, it's a tough problem, you know, and, and it's going to get, it's, it's going to get worse, unfortunately, because at least in the States, I mean, I don't know how it is in Australia, but there's just not a lot of investment going on. Like, you know, like people talk about the smart grid, but it just, it takes so much to invest in that stuff and it's just, it's not there yet. So I think, unfortunately, it's going to happen a couple more times before people finally kick into gear and they're like, oh, we should probably fix stuff, right? Like, like that power outage in India. I'm sure they're going to finally start considering that one that if people don't remember is a couple of weeks or months ago, where it's like 600 million people lost power. Only 600 million. Yeah. Yeah. Right. Makes, makes New York look a little less power. Chump change. Right. Yeah.

**Dave Jones:** But the, and it's always power, right? Power is key to everything. You know, yeah, you can lose your water and you can lose your sanitation for a couple of days and well, you're probably going to survive, you know, the other thing is the sewerage system. Sanitation's a big thing, of course, because that can lead to nasty stuff pretty quickly. What runs the pump, right? Yeah, exactly. What runs the pumps for all that? Power runs the pumps. You know, it's usually those sort of things fail because the power fails.

**Chris Gammell:** So my, my basement flooded just from the storms here. And it was, yeah, the pump failed. I mean, like the pump actually broke, but you know, if the power's out and the water's real high, it's like, well, okay, you're just going to have a flooded basement. So nothing to do about that. Yep. I mean, yeah, you're right. And it's like.

**Dave Jones:** You, you, you Yanks seem to love building stuff below ground, don't you?

**Chris Gammell:** Yeah.

**Dave Jones:** Sort of every, you know, I don't think we've got a single city here in Australia that would flood like that. I don't think it's.

**Chris Gammell:** City is on the coast. I mean, there's coastal waters at least, but is it all hills?

**Dave Jones:** Yeah, we're on the coast, but oh, no, we're not, you know, I mean, we've had some massive storms here and we get some local, you always hear about localized flooding, you know? Yeah. So one street, yeah. Water will be up to the wheels on the cars, you know? Oh, that's nothing. Yeah. Yeah. Yeah, exactly. But that makes front page news here, right? That's like a big deal. Well, yeah, that happens once every couple of years and, you know, a big super storm comes through and yeah, well, okay. So there'll be a, you know, a few cars in one, one street that'll be, you know, flooded. That's it. It's usually very localized to like one that, you know, that one street that happens to be in this particular gully with not enough drainage and all that sort of, you know, jazz. So it's, yeah, it's very localized. You never hear about a whole city going down.

**Chris Gammell:** Would you guys get hurricanes or no?

**Dave Jones:** Uh, not really, no.

**Chris Gammell:** Okay. Well, that helps too. Not getting those. Yep. Those are pretty, pretty beefy storms.

**Dave Jones:** I mean, they're pretty nasty. Yeah. No, we're pretty good here in Australia. We don't, you know, we're sort of pretty earth cake free, you know, cyclone, you know, tsunami free and all that sort of jazz. We, we do pretty well here. That's good.

**Chris Gammell:** I got to worry about his crazy Aussies, right? That right. Yes.

**Dave Jones:** Oh boy. But yeah, it shows how critical that power is.

**Chris Gammell:** Yeah. And you know, I've been seeing, um, like I said, there's articles out and I saw an article about microgrids and that's kind of an interesting idea of, you know, like with the rise of solar and even the rise of like small gas turbines and stuff like that, it, it starts to make sense. I mean, maybe not New York, right? You're not going to have like gas turbines in every building, but, um, but, but, you know,

**Dave Jones:** like the suburbs where everyone's going to like, it seems like everyone here has got bloody solar cells. I'm thinking about getting some myself this summer and, uh, and you know, and effectively you are already sort of micro gridding because your, your power is most likely coming from the solar cells of the house next door.

**Chris Gammell:** Right. And the key there though, is you need to have a battery system. Um, if you really want to be like self-sufficient in that case, right? Most people, the cheap, the cheap and smart and honestly smart way to do it, I think is to just sell it back to the grid, right? You just put your cells up, you have an inverter and then it just, it just regulates between when it's selling to the grid or buying from the grid, you know, that's the most straightforward way of doing it. But I think the battery side of things, you know, actually, you know, having a, uh, rectification down to DC, storing it in batteries, having some kind of charge monitoring like, uh, like Bob Simpson did. It is.

**Dave Jones:** And it's expensive and it's a high maintenance cost. You know, you've got to replace those batteries periodically. And they're risky too. For what? I mean, for the odds of, you know, the power going out once a year or something, you know, if you're in a bad power area, fair enough, but we get maybe on average one power failure barely one a year. And if anything, it'll go down for, you know, half an hour. That'd be a huge power outage, you know, it's like, what's the big deal?

**Chris Gammell:** Well, you know, it's, it's never, it's never too big a deal until it happens, right? When it happens. Well, yeah. Well, you know, I know people like, uh, Alan, uh, Wolke, he's, uh, out in Jersey, right? And he said he's been, you know, battling for gasoline every day for generator, right? And so in that kind of case, right, he's, I'm sure he's saying, you know, well, right now a battery pack would be nice for if, if he had solar cells and everything else and actually storing it for the day. And really the main thing is, I mean, you think about the critical electronic device or electrical devices in your house, you know, it's food, food refrigeration is a big one. Yes. Water pumping. If, if you have a well, or if you have a sump pump in the case of a basement and, uh, a cell phone charging for maybe, uh, for emergencies and stuff like that. But it doesn't take too much, but it's, it's not trivial either, right? It's not like ride a bike and, you know, turn a dynamo or something like that.

**Dave Jones:** So it's, uh, it's, but yeah, it's expensive, expensive and high maintenance to go fully self-sufficient. So really, you know, I, I think only those in like, you know, rural areas or those in very poor power areas can really warrant that sort of thing. Unless you're like a, uh, one of those, uh, survivalist preppers, you know, and you're just be ready for the, be, be ready for that zombie apocalypse, you know? Right.

**Chris Gammell:** Shout out to zombietech.tv. They're back. Yep. Good timing, guys. Good timing. They went somewhere? They were taking a break. So. Oh, right. Okay. One of our, our friend podcasts, zombie, zombietech.tv, they are, they are back on the air. And, uh, yeah. And they're prepped and ready to go. I think they're ready to go. Yeah. They were, they were saying if, if, if you listen to that show, you might be ready, you know?

**Dave Jones:** Right. Yeah. Oh boy. Yes. We have been on that. We have both been on that. It can be kind of an obsession.

**Chris Gammell:** Yeah. We have.

**Dave Jones:** It can be an obsession. Yeah. Well, it's a big thing in the US, isn't it? You know, prepping for the apocalypse and all that sort of, you know, it's a big industry. 2012 or something. All that survivalist industry. Yeah. Holy shit. It is 2012. Yeah. We've only got like a month left. Isn't the 21st of, uh, we'll have to do a big show like on the 21st of December.

**Chris Gammell:** Oh, is it going to be a Sunday? This year. That'd be great. We should do a big Google Hangout show.

**Dave Jones:** Yeah. Yeah. Yeah. Oh, it's a Friday. Well, that's not bad. It's a Friday, is it? Yeah.

**Chris Gammell:** Yeah. The 21st is a Friday. Although it'll be. That'd be a sad day here. Well, if we have, yeah. So if we have a show on the 23rd and 24th, then, you know, we're all fine. Right. I think it's the 21st, isn't it? Yeah. It's the 21st. Yeah. It's the 21st. 12, 21, 2012. Or however you say, you know, time or dates. Yeah. Yeah. So, you know, another key part, you know, the one thing I did forget actually with that too is lighting. Lighting is a big part if you have a generator. And the nice thing is if you have, if you are going to go to a battery system, it's nice because then you could just go straight to LEDs if you had a homebrew system, right? A lot of LEDs have, you know, they have Edison sockets and stuff like that. So, is that the right term? I don't think lighting. Is it Edison socket?

**Dave Jones:** Edison socket, yes. Yeah.

**Chris Gammell:** Yeah, that's right. Okay. Yep. It is. So, you don't think lighting is what?

**Dave Jones:** I don't think it's that big a deal because when you really need it late at night, well, just get a few more hours sleep, you know? Just go to sleep. What's the big deal? You know? It could be.

**Chris Gammell:** Yeah, I agree. I mean, I agree with that sentiment, but I mean, at the same time, you know, sometimes you need it, right? And flashlights and batteries.

**Dave Jones:** Yeah, but a torch, you know? Flashlight and a battery. Who hasn't got a flashlight and a battery? Flashlight. Well, that's the thing.

**Chris Gammell:** They sold out of batteries out of, like, all of New York and New Jersey. They're just out. Wow. Yeah. That's scary. Right. And you can use your phone if you had charged for that. And actually, that's a link I had this week. So, they're using, out in the streets of Brooklyn, they're using some kind of, what are they calling it? BioLite. And so, I think it's like a pyroelectric charger, basically.

**Dave Jones:** Right.

**Chris Gammell:** And so, you, like, put a little fire in there and you can cook your dinner and then it also charges your cell phone.

**Dave Jones:** It charges your iPod as well. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, boy.

**Chris Gammell:** I mean, it's a good idea for this kind of situation, right? Yeah, it's not bad. Yep. If you're a terrible camper and you bring your cell phone with you while you go camping. Right. Yeah. But, yeah, it's pretty smart, I think. I mean, it's a cool little device. I didn't really see much on, like, the how it's doing it, but.

**Dave Jones:** Right. It's, you know, it's cool. But, of course, any of us engineers can hack up a charging system if we need to, you know, the power fails. Could you? And we desperately need to charge up our phone. I don't know. Yeah. I don't know, man. I don't know if I could. You've got power somewhere. What? I mean, like. I could. You couldn't hack up 5-volt power. Surely you've got, like, a 7805 sitting in your parts drawer and whack it up to a bunch of batteries. Come on.

**Chris Gammell:** Oh, yeah. But that's crap. I mean, yes, that's pretty. That is not crap. It's going to work. Yeah. Come on. What, a 12-volt battery down to a 5-volt charger? Yeah. Your 5-volt rail? Man, you're burning all that power.

**Dave Jones:** Yeah. I don't know. You're just pissing it away, but it's an emergency, right? You know, here's an emergency, and Chris is caring about efficiency, you know?

**Chris Gammell:** Well, if I'm building a project, I might as well.

**Dave Jones:** Right. Got to do it right. Do it right, right? Oh, boy.

**Chris Gammell:** Yeah.

**Dave Jones:** I don't know. There's another.

**Chris Gammell:** Oh, go ahead.

**Dave Jones:** Chris Anderson, who we've had on the show. He is now full-time do-it-yourself drones.

**Chris Gammell:** Yeah. Yeah, he's doing it full-time. He's going to be CEO.

**Dave Jones:** He's leading wide, if you don't know. He was burning many candles. He was a many-ended candle guy. Yeah. He put me to shame. Yeah, I know. It's embarrassing, isn't it? Yeah. Yes, makes us look like slackers.

**Chris Gammell:** The thing I didn't understand about it, like the five kids thing, man, like that is just really impressive because it seems like he's rolled his hobbies in with his kids, and that's just really smart, you know? Yep. One is a handful, let me tell you. Yeah, I know, right? And five, oh, five, and trying to keep them all happy. Ooh. That is impressive.

**Dave Jones:** Well, see, I don't know if five times, you know, I don't know if, like, it's five times worse than having one. Well, get going, man. Because when you're having one, yes, they've monopolized your time, so what's the difference with having five monopolized your time? I guess there's, you know, a point where it doesn't.

**Chris Gammell:** I guess you might get some efficiencies, too, because you get them to, like, play with each other, you know?

**Dave Jones:** Yeah, exactly, yes.

**Chris Gammell:** So, you guys go figure out the 3D printer, I'll be over here. Yeah.

**Dave Jones:** Oh, boy. Yeah, anyway, he's leaving Wired after, like, ten years or something, I don't know, it's been a long time. Oh, yeah.

**Chris Gammell:** It's been a while, since the 99, I think. So, I just finished his book, too. It was good. I enjoyed it.

**Dave Jones:** Oh, okay. Yep, he's a new one. What is it? The coming revolution of the maker revolution?

**Chris Gammell:** Yeah, maker is the new industrial revolution.

**Dave Jones:** Right, yep. It was pretty good. Excellent.

**Chris Gammell:** I love my library.

**Dave Jones:** It'll be on my list.

**Chris Gammell:** Yeah, yeah, man. That's a good one.

**Dave Jones:** Which I'll be able to read on my Kindle, because it has, like, a one-month battery life when the power fails, and it's got a building light.

**Chris Gammell:** Ah, yeah. The new one. You see?

**Dave Jones:** I'm totally covered, dude. Yeah, for a month. See? You know, if you've got one of these stupid iPad things, yeah, the power's going to run out. You know, odds are you're probably only going to have half charge anyway, and then you can't piss it away reading a book, so, you know. Yeah, I was going to say, you've got to have the right tool for the job. I always say.

**Chris Gammell:** I have a medium that holds up for longer than a month. It's called a book. Right, yeah. Paper. Infinite battery life.

**Dave Jones:** But you need light for that, if it's dark. Yeah, not in the daylight.

**Chris Gammell:** No, not in the daylight. Yeah, that sun thing.

**Dave Jones:** Yeah, get it for free. Yeah. Anyway, yes, I wish him the best of luck.

**Chris Gammell:** And times two, I do as well. That's cool. You know, that's... It is.

**Dave Jones:** I suppose it got too much, you know. His wife said, look, one of these has to go. Probably. Maybe.

**Chris Gammell:** Right. I don't have to have him back on to ask about that, yeah.

**Dave Jones:** Oh, boy. And what else have we got? There's a 7400 competition.

**Chris Gammell:** He's running again. I think that's closed now, but there's been some cool entries.

**Dave Jones:** Oh, but you pulled out an entry from this as a notable entry.

**Chris Gammell:** Well, it's pretty impressive, I think.

**Dave Jones:** Well, okay. What it is, is the dude has done a BGA dead bug style. So he's flipped it on his back. I don't know. It looks like it doesn't say how many pins. Oh, sorry. Not that one. Sorry. No, no, no. I think you got the wrong one on the list there. Yeah, I got the wrong one.

**Chris Gammell:** There's a different article from Dangerous Prototypes, and that's actually pretty impressive, too.

**Dave Jones:** Well, let's mention that one first, then. Yeah, that's...

**Chris Gammell:** Okay.

**Dave Jones:** That's, yeah, he's got a... There is a... Somebody has done a BGA dead bug style. Right? So... Which...

**Chris Gammell:** Yeah. It's like... I don't get it.

**Dave Jones:** Yeah. It's interesting. Like, there's a big bulk capacitance. Yeah, I don't get it either. It's, like, so desperate. And it's, like... Like, people think that's impressive. Well...

**Chris Gammell:** Well, no, it is impressive.

**Dave Jones:** It is impressive, but, you know, it is doable. It's easily doable. If you put in the effort to do it, it's doable. I don't know about easily. Well, it's a pain in the ass to do, right? But it's doable, because this is a 1mm pitch BGA, right? It's not like you sold her into a little 0.5mm pitch BGA. Dude, this is a crazy... Or something, right?

**Chris Gammell:** This is a crazy, crazy... I mean, you're right. It's not 0.4. I saw 0.3 as well. They're going to 0.3 now in certain parts?

**Dave Jones:** Yeah, I know. It's a pain in the ass.

**Chris Gammell:** Evil bastards. It's tiny.

**Dave Jones:** But, yeah, it's not hard to solder to an individual pad on a 1mm pitch BGA. Let's, you know, I mean... I don't know, man. That's a fact, right? It's not hard. It's not hard. It's not easy.

**Chris Gammell:** It's not easy.

**Dave Jones:** Oh, it's a 1mm? Jeez.

**Chris Gammell:** Don't make it your first project.

**Dave Jones:** No, but it's, you know... Come on. If you get there with a soldering iron, it's not hard to solder on a wire onto a 1mm pitch BGA. Try it. Give it a go. It's not that hard. But he's put it... But the fact is, there's a sheer number of pins, right? And he's wired them all together. And he's done little bus bars. And it's, you know, it's very nice. Very nicely done. And it's got multiple levels. He's put multiple layers of bus bars in there by the looks of it.

**Chris Gammell:** So... Oh, that's insane.

**Dave Jones:** It's pretty... Yeah, it's pretty impressive. But from a pitch point of view, you know, it's actually harder to solder onto a 0.5mm pitch quad flat pack or something as a dead bug, you know, than it is a 1mm pitch BGA like this. But anyway, got it working. I don't know what the project does. Anyway.

**Chris Gammell:** It's a Mandelbrot. You ever do that stuff? Oh, Mandelbrot.

**Dave Jones:** Yeah, yeah. I know all about Mandelbrot. It's in chaos theory. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** I never understood. James Gleick, Chaos. Great book if you haven't read it. It's quite old now. Yeah. But it's, yeah, it's an excellent book on chaos theory and Mandelbrot and the people behind it who found it all and all that sort of stuff. That's cool. So, yeah, yeah, it's an excellent book. James Gleick. What's it called again? I believe. James Gleick. It's just called Chaos, I think. I don't know. If you search for James Gleick, doing this live on air here, which is always great for a radio show.

**Chris Gammell:** No, I was just typing it for later. I don't want to have to find it later. Anyways, the other thing that was on the Dangerous Proto, though, is they've been doing the 7400 series contest. And I'm pretty sure it's over now. I don't think I'm wrong about that. But the impressive thing about this is he designed an FPGA out of discrete logic. I think it's really cool.

**Dave Jones:** Well, he did one LUT, right?

**Chris Gammell:** It was like one LUT, right, exactly. And it looks like it's probably a couple, you know, like two or three inches square on the PCB. But then he puts some 0.1 inch headers on the edges and basically you can plug them together.

**Dave Jones:** So you can join them together. So I said, yeah, is there a photo of them all joined, like multiple ones? Oh, yeah. Yeah, I think further down. There's a video, too. I haven't watched the video. He's got like eight of them all interconnected there. So, yeah, that's pretty cool.

**Chris Gammell:** It is cool.

**Dave Jones:** That's pretty cool.

**Chris Gammell:** You know what the crappy thing about this is? What? The Xilinx software still won't compile for it, I bet. Right, of course. The eight LUTs? No, we can't fit it in there. Sorry, Xilinx people. I had to get the dig in.

**Dave Jones:** Actually, yeah, you have to read the detail. How does he actually program it? How is it? Is it compatible with any? I don't know. Anyway, go and check it out.

**Chris Gammell:** I feel like this is the equivalent. This is like when, you know, Doc Brown designs the microchip with vacuum tubes back in 55 and back to the future. Yeah, yeah, yeah. You know, there was a 2 or whatever it was.

**Dave Jones:** It looks like he's written his own. He's implemented his own simple hardware description language. It's called DHDL.

**Chris Gammell:** There you go. That's cool. That's really cool. Nice.

**Dave Jones:** Oh, boy. That brings back memories of my life. I wrote my own finite state machine compiler once. Really? Yeah, I made up my own finite state machine language and I wrote my own finite state machine compiler. Because I did this little finite state machine project. And yeah, that was fun. I know.

**Chris Gammell:** A lot of people get into like writing compilers and writing their own languages. I just never did that kind of stuff. I don't know. Okay. Yeah. At least at my school, it was a lot of CS type folks that were doing that kind of thing. And I know it's good because it helps you understand. But at the same time, I feel like it encourages this broadening. It's like, yeah, okay. Sometimes it'd be better to just maybe don't write another one. You know, it's like sometimes it's easier to invent your own. You know, it's like same with circuits. Sometimes you don't want to use the method that everybody else uses because you want to try something new. But at the same time, maybe it's a good idea to just use what other people are using. Yeah. There's academic exercises and then there's practical exercises. And yeah.

**Dave Jones:** Well, I think mine would have been around the late 80s, early 90s or something. Yeah, early 90s probably. So this is pre-internet, pre-web, you know, kind of thing where, you know, you could find, you know, anything you wanted basically. So yeah, I decided, well, I'm just going to write my own. And that's when I enjoyed doing software, big software projects, you know, and I loved. Yeah. Yeah, I don't do that anymore.

**Chris Gammell:** Makes you wonder, because people don't have that requirement anymore of, you know, if you want it, you've got to invent it, right? Is that actually hurting people or helping, you know, or not even people, is it hurting projects or helping projects because, you know, maybe people have less experience starting from scratch? Well, it's both.

**Dave Jones:** But there's both. Because there's so much you can do now because there's so much information out there that you wouldn't even dream of being able to do some stuff before. But now all of the resources are out there and all the examples are out there. All the communities are out there.

**Chris Gammell:** That's true.

**Dave Jones:** You know, I mean, no, I would not go back. We've talked about this before and I've done a video on it. No, I would not go back to the pre-communications internet thing. Oh, well, you wouldn't have a job right now if that was the case, right? Right, yeah, of course.

**Chris Gammell:** Who's that guy with the Sony over-the-shoulder handycam just making videos for himself? That's weird. Oh, right, yeah. You're like at, like, flea markets trying to, like...

**Dave Jones:** He's selling copies on VHS tape, you know. Yeah, Betamax. Yeah. That would be great. Yeah, I... Yes, my... Yeah, I could do a video blog by mail order, you know. Oh, God. I have to mail out all the tapes and CDs. Right, and people do, like, trading. Yeah, exactly.

**Chris Gammell:** The trade-up, you know.

**Dave Jones:** Oh, boy. Yes, that'd be something.

**Chris Gammell:** I like that Dangerous Protos is doing this 74 Series contest, though. I think it's a good idea. And they've done it once before, at least. And it's tough because it's so broad, you know, like, something like this is huge, right? This is a big one. But at the same time, it also helps people kind of, you know, I didn't grow up with 74 Series Logic, so I, you know, I always have to look up numbers. I don't know about you, but I still have to look up numbers. I recognize a couple, you know, like, like, uh, um, like latches.

**Dave Jones:** I still remember a bunch of them. Come on. Right, shift registers. You would know, like, a 401-1-4000 Series CMOS, and you'd know a 7474 flip-flop, and you'd know a 7-4-245, you know, octal, uh, buffer and stuff like that, so.

**Chris Gammell:** Sure. Right, yeah, and there's certain things you do, but it's nice because it kind of just gives exposure to more of the variety of functions that are out there. And it's, uh, I don't know, it's not, like, super necessary these days, but at the same time, you know, it's, sometimes it's better to put one of these in than throwing an entire ATtiny in there, right? I mean, like, cost-wise and everything else.

**Dave Jones:** I remember, I may have mentioned this before, but I remember a job interview I went to once with a batshit crazy startup company, um, and the technical interview consisted of asking me, like, uh, asking me to, um, like, he would throw me, like, uh, you know, a 7-4-245 and ask me what that did, and I knew these off the, bang, bang, off the top of my head, you know, because this was back in, yeah, early 90s, once again, pre-internet thing, right? So, yeah, back when you had to remember all this shit.

**Chris Gammell:** Right, you were reading, uh, data books for fun.

**Dave Jones:** Yeah, yeah, it's like I was reading data books when I was eight, you know? I mean, yeah, exactly, right? I had my own database and data book library, like, you know, by the time I was, like, nine or ten, right? Yeah, a whole shelf, you know, full of them. And, um...

**Chris Gammell:** Which people can still get if they want. They're, they're, they're going cheap these days. They're kindling.

**Dave Jones:** And I remembered these things, and he was so impressed that he offered me the job, you know? And I actually went to him. That's your whole technical interview. Don't you want to ask me something else? Oh, no, I, I think you'd, you know, I'm fairly impressed. I know, this job's going to suck. Just because I remembered, you know, some 7-4 series numbers. Yeah. I mean, that was, yeah, I was just taken aback by that. Anyway, I turned it down.

**Chris Gammell:** The job sucked. That's probably smart. All right, so we are at our halfway mark-ish, and we should, uh, break for commercial. This is weird.

**Dave Jones:** Should I? I just, yeah, it is. I just had somebody knock on my glass. I just had somebody walk up to me and knock on my glass.

**Chris Gammell:** Maybe he's trying to tell you to keep it down. Stop talking about 7-4 series logic.

**Dave Jones:** Right. Could be. I don't know. Maybe I'm talking too loud. All right, well, if we get another knock.

**Chris Gammell:** Yeah.

**Dave Jones:** That could be my first, uh, yeah. I don't know. My first warning. I have no idea.

**Chris Gammell:** Right. Time for Dave to build a rail gun. Anyways, we should talk about our sponsor, which is Jameco, and actually Club Jameco. Yes. And Club Jameco is, uh, well, it's a new project they're kind of putting together, and basically you can submit a kit idea, and then there's a big voting system, and then whatever gets voted up the most, that, uh... Gets might. Yeah, they'll turn that into a kit, and then you can get upwards of 10... I think it's, there's like a gradation schedule of, you know, how much you can make, but if you get over 500 bucks for any quarter, you get 10% of, uh, 10% cut of the profits, and, uh, so that's pretty cool, but...

**Dave Jones:** For, you don't have to do much, like, you don't have to be involved in the whole engineering of design, you know, actually designing the kit properly, and, you know, all the, all of that horrible engineering work which goes into actually producing a kit. Right, exactly. They'll do that for you.

**Chris Gammell:** They have engineers helping out with that kind of thing. I think you need to document... And they have guidelines, and, and that, you know, you can link through all that stuff and, uh, and see it, but it's a cool little, little project, uh, little, uh, site that helps you, you know, make a project. And I think, really, that getting rid of the hassle is, is the best part of that, you know, the getting out of the, the bagging, bagging components. That's the, that's the tough part, right? You know, purchasing and bagging, so. And Jameco has a lot of other, you know, you can actually buy parts on Jameco, so, um, but if people want to check out, we actually picked out a kit for this week. They, um, we went through all the kits that they're, um,

**Dave Jones:** Well, some of them. Past people. I don't, yeah, some of them. Didn't catch right.

**Chris Gammell:** Well, we went through the ones that, uh, have been submitted as, as kit ideas before. And, uh, we picked one out. It's a light organ. So it's a cool little kit. People should check it out. And they can, uh...

**Dave Jones:** As in audio goes in and woohoo! Oh yeah, and then it lights up. You get a fancy light show.

**Chris Gammell:** Right. It's kind of like a, a graphic equalizer. And, yeah. But it's all op-amp based. And so it's good for, you know, if you're learning op-amps.

**Dave Jones:** Audio microcontroller. Yep.

**Chris Gammell:** Right, right. Cool. And so, uh...

**Dave Jones:** But there's like, I don't know how many projects are on there, but there's a lot. Isn't there? There seems to be...

**Chris Gammell:** Yeah, yeah. The Explore projects. I mean, in terms of what's been submitted, they said they've been overwhelmed by entries. But, you know, the good ones, they're kind of working through them. So, and if you have a good idea and you'd like to, you know, have it made, this is a good place for it. Yeah. And so, and it's nice with open source kits. You know, you can put open source kits through and, uh... That's great, right? I mean, helps to get it made.

**Dave Jones:** Are they open source by default?

**Chris Gammell:** I don't think so. There's a FAQ page that I was just on and then you made me click away. Oh, sorry. Yeah. Yeah. Anyway, we'll find out the details. Yes, and we'll... We will. And you can find out more by going to...

**Speaker ?:** And it'll be LinkedIn.

**Chris Gammell:** Right. If you go to clubjameco.com slash theamphour, we have our own link and there's a link to that kit and there's a link to other information on there. And like Dave said at the top of the show, if you go through that link, that really helps us out, especially if you're typing it in a browser. So, go to clubjameco.com slash theamphour.

**Dave Jones:** Or go to our website if you don't want to actually remember that. Go to theamphour and we'll have a link there. Yep.

**Chris Gammell:** All right. That wasn't too painful. That wasn't... No, that wasn't. So, thank you much, James. Sponsorship. Yeah, it's novel, isn't it? It is. It's different. It's good. And now back to our regularly scheduled program. Scheduled, right.

**Dave Jones:** Now I'm concerned. I'm like... Because I've got headphones on here, right? And somebody knocked on my window. Like, because I'm in my little office here, right? Which is my little... It's creepy. ...ocupical office. You know, two and a half. And I saw them. They walked up and they tapped on my window here. Like, it's like got a... I couldn't see who they were because it had... Because I've got that, you know, frosting kind of thing. But I saw they definitely walked up and tapped on the bloody window. So, I'm not sure if they... Do you lock the door? ...knocked on my main door and I didn't hear them. Huh. Or something. I don't know.

**Chris Gammell:** Do you lock the door or no?

**Dave Jones:** Yeah. Yeah. So, they can't just walk in.

**Chris Gammell:** All right, good.

**Dave Jones:** But, yeah, I certainly wouldn't hear them if they knock. So, I've got my headphones on here and... Huh. Hmm. Oh, well. Bugging you. How dare you interrupt our show.

**Chris Gammell:** Exactly. You should put a little... We should get you a recording sign so you can be like... I do. I do have one of those. You do? You should hook that up, man. That'd be cool. Yeah.

**Dave Jones:** I know. It'd be awesome. Yeah.

**Chris Gammell:** Well, uh... So, did you see some of the links that Greg sent over? So, our former guest, Dr. Greg Charvat. Mm-hmm. Uh... He sent over some fun links this week, actually. Um... In terms of art. He's, um...

**Dave Jones:** Can Radar made it on the IEEE Spectrum site, too.

**Chris Gammell:** Yeah. Yeah, that was cool. And that was actually... That was kind of like a build log of the guy that was doing it. And, uh... And actually, uh... Tony Long, or one of our other former guests, is now building a kit for him. Uh... So, there's actually going to be a kit for him. Oh, he is. Yeah.

**Dave Jones:** We actually suggested that, didn't we?

**Chris Gammell:** Well, I... He was doing it before we suggested it. Oh, wow. But it's good because if people want to try it out, then, it'll be a lot easier to procure all the parts. And, uh... You know, it's... Because it's tough if you're buying, like, single quantities of, you know, like, RF components and, you know, if you're kind of diving in the first time. So, it's a good intro to microwave stuff, which is cool. But the thing that I really like, there was this video that, uh... That Greg actually helped... Um... He helped advise on. And it's these guys from... Uh... Where are they from? I can't remember. Oh. Uh... UC Davis. They're from UC Davis. And then they had, uh... Uh... Over at a Chinese university as well, which I can't pronounce. I apologize. Um... Basically, though, they had... They had, like, a... Uh... A microwave horn, right? And then they actually detected the phase on that thing. And what they did is they did a light painting with... With an LED spectrum reader, basically. And so they moved it back and forth and they could show where it was in phase. And what they did is they actually mapped out a sine wave by moving this horn in space. And then once they captured that on a long exposure shot, it actually shows a sine wave. It's just so cool. That is... Yeah. Well... That's brilliant. I mean... Right. Of course. You know, it's so hard. It's so hard when you're starting out, too, of just how you visualize this stuff, right? I mean, you don't think about it, especially with, like, you know, like, like, uh, magnetics and, and, uh, magnetic fields and electronic fields, right? And, and, uh, how, how they interplay and stuff, too, and, and trying to actually figure that stuff out. It's just really hard to visualize. And this, this definitely helps. I mean, so there's, there was a whole bunch of videos. Apparently, there's, like, some, uh, there's some other con... There's, like, a video contest for, um, for microwave stuff. But this, this is by far my favorite. Yeah, it's cool. Yeah. Yeah. It's really cool.

**Dave Jones:** Nice work.

**Chris Gammell:** Yeah. So, if people like that, go check it out. And then later, if you want, you can, you know, build your own microwave horns and everything. And, and, and like that guy in the spectrum said, he actually was, he said, like, he was good at, like, 50 meters. He could actually, like, track himself and, like, running across. Yeah, that's cool. Track someone running across. So, that's, that's cool stuff, man. I've never really done that stuff.

**Dave Jones:** No. Me neither. You know, I'd love to do all sorts of stuff like this. But, yeah, you know, you've got to weigh up your time and interests and all that sort of stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm happy to just leave it to the people who are really super keen on that sort of stuff. And then they do cool videos showing it often. You know, I'm just happy. Let me just watch YouTube all day. Yeah, exactly.

**Chris Gammell:** Yeah. Well, that's, I mean, like, yeah, I mean, like, time-wise, I mean, I have, I have a brand new Raspberry Pi sitting in front of me right now.

**Dave Jones:** Excellent. Is it, is it, is it the new model? Because didn't they? It's the new one, yeah.

**Chris Gammell:** I got one of the first new ones.

**Dave Jones:** Oh, I've got, right, as I am, I'm behind the times again. I've only got the old one, I think.

**Chris Gammell:** Well, it doesn't matter because I'm not using it. And you know, you know what the tripping point for me was? What? This is honestly what it was. It was like, oh, they didn't include an SD card. Now I have to go find one.

**Dave Jones:** Oh, no.

**Chris Gammell:** I'm busy. So that has been my stumbling point so far, but.

**Dave Jones:** You couldn't get an SD card.

**Chris Gammell:** It's all the way upstairs, you know, they just. Right, yeah. That's, that's a cool little part though. I mean, it's interesting the marking on the, so, you know, they, it's this, it's a Broadcom part, but I think Samsung's packaging it because, I think they are at least, the only, the only main IC on here, like the high density BGA is marked Samsung. And I think that's because it's got the 512 memory inside there too. So I'm guessing, I'm guessing Broadcom's just selling them to die and then Samsung's doing the final integration and packaging with, you know, memory internal. But man, it is. It's all too complicated. It is tiny. I love it. It's great. I mean, it really is. I mean, this is the size of a credit card. That's, that's really cool. I know we said some, you know, so we said, oh, whatever at first and, you know, but I've, I've gradually warmed to it. And, yeah. Okay. And, and there's been good news. I don't know if you saw this. They, Raspberry Pi is going to be one of, I think, the first that is open sourcing an ARM-based core with the GPU. So all their code is going open sourced.

**Dave Jones:** Yeah.

**Chris Gammell:** Awesome. How about that? That was, that was about two weeks ago now they mentioned that, but.

**Dave Jones:** Well done.

**Chris Gammell:** Yeah, man. That's pretty cool.

**Dave Jones:** What's this about ARM moving to 64 bits?

**Chris Gammell:** Oh, that's another thing because, you know, ARM's everywhere, right? I mean. Right. Just no avoiding them.

**Dave Jones:** Yeah. It's almost to the point of boredom.

**Chris Gammell:** Yep. Yeah. You know, I, I feel like I should get, but like at the same time you look at this article, right? It's so 64 bits, AMD is giving up basically on a lot of their, not giving up, but they're moving towards ARM for server cores and everything like that. They're going to be the ones manufacturing a lot of that stuff. So they're doing the licensing, but then you read these cores and it's like, what, where are they coming up with these names? What is it? It's like a, the A, you know, they're like A7, A9 is what a lot of the older stuff is. And they went to like Cortex M0, M3, whatever. And now it's, and then the Apple stuff, all the A5 and stuff like that, like the A8, A9, all those Apple integrated chips, they used a A15 core, right? And try and keep them all straight. And now, now, now AMD is licensing the A53 and the A57. It was like, okay, whatever. You know, it's just.

**Dave Jones:** Why can't they have something fun like the A666 or something?

**Speaker ?:** You know what I mean?

**Chris Gammell:** Right. Come on. It's a beast of a trip. You can be creative. I mean, come on. Well, I mean, it's, I don't know. Is it better, is it better to have like, not integrated, incremental type parts? You know, like, like how, like how HP stuff was always incremental numbers and stuff like is it better to do that? And then you have product families based on that? Or is it better to have like random ass names like car companies are with like, you know, Nissan Muranos and all that other stuff? And it's like, okay, well. Oh, right. Yeah.

**Dave Jones:** I don't know.

**Chris Gammell:** Six of them and half a dozen of the other. It's annoying either way.

**Dave Jones:** As long as it's not some weird ass part number, you know, that you can't, it's so freaking long and convoluted that you can't remember or some product number. Yeah. You know, like, you know, Agilent's famous for it, you know, numbering all their products with some stupid, ridiculous, arbitrary number, you know?

**Chris Gammell:** Right. Well, at the end, it doesn't really matter, right? I mean, like, like, like any brand name as well, right? Like Samsung doesn't mean, Samsung means three stars, right? Or Broadcom doesn't mean anything to me, right? But at the same time, you just start to associate it with the process, right? Or the, the, whatever they're selling. That's the idea behind branding. It's like, well, the same thing happens with chips, but at the same time, you know, it's not exactly easy to remember. Oh, is this an A9 or an A13 or an A15? I don't know. A57. So it's a.

**Dave Jones:** I don't know.

**Chris Gammell:** It's stupid. It's all over the place.

**Dave Jones:** I don't like it.

**Chris Gammell:** Yeah.

**Dave Jones:** Shall we talk about the big upcoming election? How far away is it? Oh. You're regretting this.

**Chris Gammell:** What I'm really hoping is that most people are listening to this to try and avoid all that stuff. So I don't, I don't really want to talk a lot about this. I'm in Ohio, right? This is honestly.

**Dave Jones:** This is the big swing state, right? Yeah. The critical.

**Chris Gammell:** I posted, I posted a thing when, when Sandy, the storm was coming through. It took a right turn at Ohio, right? It started going north. And I'm saying, I said, even, even Sandy doesn't want to come to Ohio because of all the ads that are on TV right now. It is just, it's just terrible. Not bad, huh? Yeah. It's, it's, they should use it as a campaign for, you know, like kids to not watch TV anymore. You know, like, oh, kids, you shouldn't watch TV because then you have to watch campaign ads.

**Dave Jones:** Oh. And that's where the hundreds of millions of dollars goes, right?

**Chris Gammell:** Oh, yeah. And this year it's, it's, it's really bad because like, you know, even YouTube and Hulu and everything else there, you know, they're all targeted now. They know where I am in Ohio. So I was thinking about getting a VPN connection just to try and pretend I'm in Australia.

**Dave Jones:** Oh man, that's bad. Yeah. We, we, we, we don't have anything like that here. You know, there's none of this, you know, spending hundreds of millions of dollars mass, you know, campaigning people. Yeah. There's the odd ad on television or something for the party or whatever, but you know, it's, it's really, it's not to the point of saturation like it is over there. And my condolences.

**Chris Gammell:** Well, yeah, thank you. It's, it's almost over. It's over on Tuesday here. But the one thing that, that I had posted about was there's this really well researched article on, by Cabe Atwell over on Element 14. And basically, you know, you can go read it yourself, but basically it's just about who's better for engineering, you know, Romney or Obama. And it's, it's just an interesting article from, he lays it all out there and it's, it's like, it's a long ass article too. It's probably a good 2000 words. And so, you know, you can take whatever you want from it, but yeah, I haven't read the whole thing. I think, I think a much bigger, interesting, more interesting thing is what's going to happen in the States if the sequestration happens. Right. And this is bound to happen either way. It's just because of gridlock. But this is where, and this is where this article comes into talking about, you know, spending and stuff like that. Right. I mean, a lot of, I was, I was talking to my wife about this just in terms of spending in general, it's like, you know, you give, you give a research scientist a hundred, a hundred million dollars and some of that's going to equipment manufacturing, some of that's going to parts and stuff. So I don't care who's in office. I just care that they start spending money on engineering and science and stuff like that.

**Dave Jones:** No, I, I think you have to be scared. I think there's a lot more. But I don't think he mentioned that all of Romney's cronies are on the science committee and none of them believe in bloody evolution or anything else. Nutcases. And they're on the science committee. I'm, I, I, you know, come on. Chris is speechless.

**Chris Gammell:** Just waiting it out, man. I'm just waiting it out. Just get it all out, man. Just get it out. Just get it out.

**Dave Jones:** I don't know how you put up with those people. Really. Come on. See, then this is why you can't move to the States.

**Chris Gammell:** This is why you can't move to the States, Dave.

**Dave Jones:** Yeah, they wouldn't, they wouldn't even let me in, right?

**Chris Gammell:** One of many reasons, right?

**Dave Jones:** Why? Because I actually believe in science. Hey. Can't have someone like that in our country.

**Chris Gammell:** I meant your wife wouldn't let you, but yeah. Right.

**Dave Jones:** Oh, it's, it's disgusting.

**Chris Gammell:** Anyway. Boy. All right. So back to electronics.

**Dave Jones:** No. Do you think that you'll have an answer next Tuesday or is it going to, or next, whenever it is, or is it going to be too close to call? Like, and it'll drag on and just be one in the courts again.

**Chris Gammell:** I hope not. Yeah. You know, there's this, there's this really interesting, if people are interested in this kind of stuff, there's this interesting, like, flow chart that you can look at on New York times about all the different options. And it's like, it's just like, you're, I'm so deep in this stuff right now that I'm just like, you know, I'm kind of like drinking the Kool-Aid and looking at all the statistical stuff. And it's interesting from a, from a statistics standpoint, right? Of like, you know, there's so much uncertainty about everything, right? That, that there's only, there's, there's signals popping up everywhere. Right. I mean, like if this was a, a filter system, right? You'd have to have a, such a well-tuned filter that it's just like, but there's so much crap in the system that it's like, you can't even, you can't even tell, right? There's no way to predict this stuff right now. So, um, it's, uh, I just want it to be over Dave.

**Dave Jones:** So you do actually vote. You're one of the, uh, one of the people who do actually get off your ass and vote.

**Chris Gammell:** Yeah. Yeah. That's good. Awesome. Yeah. It's important. And people that are listening should vote. I, yes, regardless of your views, I want you to vote. So that's good.

**Dave Jones:** Here it's actually compulsory to vote. If you don't, they are fine you.

**Chris Gammell:** Really?

**Dave Jones:** Yeah. And I, I know the Yanks will be screaming, oh, that's against freedom. You guys don't have any freedom because you have to vote. It's like, no dude, I'm sorry. You don't quite get. How much do you get fined? Oh, it's only 50 bucks. It's like, so there are a lot of people who just simply refuse to vote and they pay, and they pay the 50 buck fine or whatever. You know, it, you know, it isn't a big deal. So if you want to make, if you want to do that protest, but you know, people do the old, you know, they, they, they do the old false vote. They do the donkey vote. You, you, you turn up, you get your name signed off and you vote for none of the above, you know? Yeah. It's called the old donkey vote.

**Chris Gammell:** So what a mess. There's actually a new podcast too, that was actually pretty interesting from, uh, it's called, uh, innovation hub. It's from the Boston. It's, it's out of Boston. And, uh, and they actually covered a bunch of this stuff about, you know, just science funding, engineering funding and stuff like that. And I'll, I'll try and link it in. It's, it's a really good, I've really enjoyed it so far.

**Dave Jones:** Is it just a general interest podcast or is it like a sciencey based?

**Chris Gammell:** It's, it's definitely science based. I mean, it's, uh, everything, you know, it dives in engineering a little bit, but mostly science, um, you know, kind of the innovation. So it's like, that's pretty broad, but, um, I really enjoy it. So people should check that out. The thing I've been keeping myself busy with trying to ignore all of this stuff, which you kept rubbing in and reminding me of is, uh, CNC machines. This is my new, uh, what? You don't like it? No, it's fine. This is my new obsession. This is my new, uh, this is my...

**Dave Jones:** Go and get yourself a new toy. Um, I'm, I'm surprised the wife is, uh, allowing you the privilege of buying such a toy.

**Chris Gammell:** Here's the key. Here's the key. Uh, one, I've, I've somehow sold her on the benefits of how I could, you know, use it, not just for, you know, making cases and front panels and all the other stuff for electronics things. Mm-hmm. Uh, but I've also convinced her that I can make stuff for her, which is smart. And when you say you can make things out of metal and wood and plastic. I just, just, yeah.

**Dave Jones:** I'm not sure if you can hear that, but the building fire alarm is going off.

**Chris Gammell:** No way.

**Dave Jones:** Yes way. Well, I'm afraid you're going to have to anchor the rest of this yourself. Do you have the, uh, mumble app? Uh, I, no, I don't know. I don't think so. Try and get the mumble app. Sorry.

**Chris Gammell:** I gotta go. Try and get the mumble app on your cell phone.

**Dave Jones:** Bye. Bye. Catch you next week.

**Chris Gammell:** All right. Oh, oh, oh, oh. Ah, so this is interesting. Anyways, um, I hope he turns the sound off at least. So this is Chris and, uh, Dave didn't turn the sound off. He, uh, he was waiting outside for a few minutes and I kept going. I was recording by myself, but we all know how bad five minutes with me is by myself. So 15 minutes was a little undoable. So here's me and Dave once he got back into the office. So basically, basically I found, I found this article on, uh, so we, you know, we have a subreddit, right? We have the amp hour subreddit. There's another good one. If, if people are on Reddit, um, called hardware startups and you know, they post about, you know, we've been talking about hardware startups, a whole bunch on here and with Kickstarter and everything else. And there's a lot of focus on software wrapped in plastic these days. And basically though, they, they, you know, he, uh, the people post a lot of cool articles in there and there was a really good one about, about mold making. And I never really looked at that before. Yeah. And it's, have you ever made a mold before? Like for neoprene buttons or anything like that?

**Dave Jones:** No, not really, not as such. No. Like I've made molds for various, um, enclosures and potting things. Like I've put my circuit inside a, a mold and then filled it up with cotton, uh, filled it up with potting compound and stuff like that. But that's probably the limit of it. Fairly boring stuff.

**Chris Gammell:** Okay. Well, that's, that's important. Actually, uh, one of our, one of our listeners tweeted about that. He wanted to know about, uh, how to, how to waterproof electronics down about 10 meters or so. I, I've never really done that.

**Dave Jones:** I mean, I've done that down to several thousand meters.

**Chris Gammell:** How do you do it? You just pot it?

**Dave Jones:** It's not easy. I've got potting, potting is one way. Yeah. But I'm ultimately, usually with these underwater stuff, you've got to get like sensors in and out. You've got to get wires in and out and just doing penetration. I mean, even down at 10, 20 meters, um, yeah. You probably need a good half an inch of potting, uh, length on your wires. Otherwise the water will creep under pressure, creep back up the wires. And then you've got to prep it. So you've got to prep your wires. You've got to clean them with isopropanol alcohol. You've got to, you know, so that the potting compound adheres properly to the PVC and all that sort of jazz. It's non-trivial. And if you get one little bit wrong, you know, bingo, the wires, the water's going to leak in.

**Chris Gammell:** So it's all about where the, uh, where the intros and outros are, or inputs and outputs. Yes.

**Dave Jones:** All the, uh, all of the water penetrators, the penetrating connectors, you can buy proper water penetrating connectors and stuff like that. So, and then you get into the whole thing of O-ring sealing because usually your widget has to have a lid, you know? Yeah. Your gasket, your O-ring and sealing all that up as an art in itself. Uh, getting the pinch angle, you'd be amazed at the amount of engineering, which goes into getting just the right pressure on your O-ring and stuff like that. You know, if you want to do it right.

**Chris Gammell:** I have worked with that stuff a little bit. I used to work at a military place and, or military and fire and they, uh, and they had, you know, they had a lot of O-rings and they'd do like submersion testing, but never like, never like super high pressure like that. So yeah, that's crazy. Yeah.

**Dave Jones:** Yeah. We used to have our own, um, in-house, uh, water, uh, tank so we could actually pressurize it. I think it went up to a thousand bars or something like that. Uh, we worked in bars, you know, that's, you know, I can't remember offhand now what that is. I've worked in many bars myself, Dave. I've, uh, hit the bars every weekend. Your entire education was built around the bar, wasn't it? Yeah.

**Chris Gammell:** College was based on bars, right? Right.

**Dave Jones:** Oh boy.

**Chris Gammell:** Yeah. Uh, so yeah, CNC. So the other thing I, so I was, I, the reason I got into all this, right, is, is, is the wife, right? And I've sold it to her as I'd be able to, you know, not only just make, you know, aluminum cuts and wood cuts and plastic cuts, you know, like blocks of ABS and stuff, which would be like a 3D printer, but in the opposite direction. Um, but also the actual viability of, you know, using a CNC milling machine to make, you know, quick turn, um, copper clad cut boards, you know, like, and you and I have talked about this before. You're not really keen on them because you think it, and I agree. It's just as fast.

**Dave Jones:** Oh, they're okay machines, but you've got to have a high spec one. You know, if you've got to do it, you've got to go for gold, you know? Right. So I'm curious about these CNC machines. At what level do you have to spend before you get something that's not a piece of shit?

**Chris Gammell:** Uh, well, I mean, you know, I've had, I've had some help so far.

**Dave Jones:** It's really useful.

**Chris Gammell:** Yeah. I've had some help so far, and it seems like, it seems like a lot of the, the, uh, the lower end stuff, and even the higher end stuff, right? You know, it's all still, it's old stuff. I mean, it's old, it's using parallel port kind of stuff, right? I mean, and good luck finding computers that have parallel port cards these days. Yeah, no, fail. You have to install them yourself, and even then, you have to have probably a full, uh, PCI bus, whereas most things are PCI Express these days. So, not exactly an easy thing. PCI?

**Dave Jones:** Pfft, ISA. Pfft, ISA, right? Oh, my God. Yeah. Right. Industry standard architecture.

**Chris Gammell:** That's right. And, uh, and so, like, all that stuff, you know, it's a lot of DB9s, DB29s, and that's to be expected with just higher, just for the current carrying capabilities, if you need to drive, you know, a stepper motor or something like that, right? That, you need higher current cables.

**Dave Jones:** Usually, they're, usually, they're just comms.

**Chris Gammell:** Oh, they're self-powered?

**Dave Jones:** Usually, they're just an 8-bit, yeah, they're, yeah, usually, they're, yeah, they're always, yeah, they don't drive any, any amount of current out of the parallel port, for example.

**Chris Gammell:** Yeah. Well, that's just, no, I don't mean the actual, not the, not the parallel port, I mean from, so then from, that parallel port goes to, like, a, you know, a controller box, and then the controller box talks to the steppers.

**Dave Jones:** Oh, okay, and the controller boxes use all D25 connectors. Yeah, you can get up to a couple of amps per pin on a D25.

**Chris Gammell:** Yeah, three amps per pin for a DB9, I know. So, it's, I mean, it's nice for that kind of thing, but, anyways, it's, it seems like a lot of this stuff is older, just because it doesn't need to be super fancy, right? I mean, you're not going to be whipping through a ton of stuff. I mean, there's some videos I can link in which are insane, you know, like, people, they're cutting out V8 engine blocks with CNC, you know, they're all liquid cooled and all that crazy stuff, five axes, that's not even close to what I wouldn't be doing. Right. Yep. But, at the same time, it's fun, it's, you know, it's porn to look at, right? I mean, just like, oh, it's just so cool. Of course. Yeah. So, uh.

**Dave Jones:** But, what can you get for a reasonable amount of money? How much money are you thinking of spending so that people can, if they know about this sort of thing, can suggest something?

**Chris Gammell:** Yeah, yeah, yeah. So, well, there's, to step back a little bit, there's this great document that I found on that hardware startup subreddit, and basically it's all about mold making, and it's all about, you know, like, basically an intro to machining, right? And it's really CNC machining, right? It's not necessarily hand machining, which is a whole different field. But it's a really great primer, at the very least, and quasi-textbook, you know, in reality. But they also suggest a whole bunch of different ones that are out there, and they started about 500 bucks, and that's the lowest he would recommend. It was like a Hong Kong-based one. And then it goes up to, you know, an easy 20 grand, right? And that's still in the mid-level, not prosumer, but probably mid-level, you know, not like high volume, not high speed. Well, it's high speed, but...

**Dave Jones:** So, it's similar to the 3D printer market. You pay anywhere from 500 bucks to 20 grand for a...

**Chris Gammell:** Yeah, it's shockingly similar, actually, because of the... Well, I think there's certain things that are better, but the one I'm looking at, you know, I've been selling my drum set, I'm selling my drum set, I'm selling a bunch of, you know, all the music gear I have.

**Dave Jones:** He's hocking everything, folks, to get this dream 3D... Yeah, well, you know, I'm excited about it. ...CNC router.

**Chris Gammell:** It was time, anyways, but the point is, you know, like, and you look at, like, the relative stuff, so I'm comparing it, like, you know, a Replicator 2 versus, like, a CNC machine, and it seems like the CNC machine's a little bit better.

**Dave Jones:** Bloody hell, there goes the fire alarm again. Oh, no. Again.

**Chris Gammell:** Oh, crap, I got it.

**Dave Jones:** All right, I think we might have to call it... No, no, better not. Just light on fire? I'm on the Strata committee, if I ignore it, I'm, you know... Yeah, all right, I better go again, folks. Sorry about that, I'll catch you next week on Planet Kolob. Planet what? Sorry, Mormon joke there.

**Chris Gammell:** Oh, right. No, I'm not sorry. Can you turn your recording off this time?

**Dave Jones:** It's a hilarious Mormon joke. Oh, yeah, I will. I'll stop. Okay. Oh, no, hang on. Hang on. It just stopped, folks. Hey! It went away. Yeah. It went away.

**Speaker ?:** Cool.

**Chris Gammell:** All right.

**Dave Jones:** Excellent. We shall continue. Yeah. Not that we have much time left anyway.

**Chris Gammell:** Yeah. So, anyways, this guide's great. And it seems like with, you know, like I said, you know, Replicator 2 is about $2,500. And that's kind of the upper, that's the top of the range I'm looking at. Because as someone said on Twitter last week, you know, there's a difference between buying a tool and buying a project. And I really, I like that a lot. I think that was a really good way to look at it. You know, like if you buy low end, you can get it to work and you can, you know, you can tweak it and you can eventually run into, you know, your limitations. But sometimes you just want to buy stuff that works, right? I mean, like you say all the time about like Windows versus Linux, right? Yep. And so part of me just wants to get it to work just because I want to start making things. You know, that's the main thing. Yeah, of course. Yeah. So there's, I don't know. I'm really excited about it.

**Dave Jones:** I think you're going to have to spend a decent amount. I think you're going to have to spend a couple of grand before you get anything that's going to produce decent results for you.

**Chris Gammell:** Well, I don't know, man.

**Dave Jones:** I'm afraid that's just the way it is.

**Chris Gammell:** Half mil repeatability on the $2,500 machine I'm looking at. So that's pretty crazy.

**Dave Jones:** Yeah, yeah. That's pretty awesome.

**Chris Gammell:** Yeah.

**Dave Jones:** But then you've got to have like the heads, like how much do the tooling heads cost and stuff like that? That's a good point, right. Yeah.

**Chris Gammell:** And there are, yeah, they're probably like 15 bucks a bit, you know, or whatever. Whatever you call them. The end mills and the drill bits and everything else. So, you know, non-trivial. Like, you know, I'm sure that a full set would probably run me another 500 bucks. But, you know, it's like anything else, right? And the materials too. It's, if it's a tool, it's not cheap. You know, or I could go cheap. I could go buy them from, you know, like China.

**Dave Jones:** I think you'd regret that.

**Chris Gammell:** I think so too. I think, I don't think I will. But I mean, I'm sure there's some good stuff from China. Don't get me wrong. There's, you know, there's probably a range of stuff you can get. But if I go cheap in general, if I go cheap from, you know, China or the US or Italy or anywhere else, you know, Germany, it doesn't matter where I find the cheap stuff. They're cutting corners somehow, you know. Exactly. Most processes are pretty efficient to start with. So, it's, you really got to, you got to, you got to pay up sometimes.

**Dave Jones:** So, if anyone has any good advice for Chris, let him know. Yeah. And happily take it.

**Chris Gammell:** Yeah. So, the last thing I wanted to mention is because I mentioned that hardware startups Twitter account is the interesting focus on it from a big name in the startup space. So, Paul Graham of Y Combinator, which is like a software startup group, he wrote like this interesting article just basically about the rise of hardware startups and he's calling it a hardware renaissance. And it's like nothing that we didn't know, but it's always interesting when you see big names like that. Jump on the bandwagon. Right. Exactly. Yeah. Exactly. Yeah. And even more interesting is when a competing incubator at Bolt, which Scott Miller, the guy we've had on the show from Dragon Innovation, he's involved with one of the other guys from Bolt, Ben, he wrote, yeah, that's cool they're interested, but they're not going to help you out much. So, we might be starting to see some antsy in the pantsiness around here with people arguing over hardware startups. But in terms of our listenership, I think the more people are interested in hardware in general, the better, right? It's a good thing. Absolutely. Good problem to have. Mm-hmm. And the last thing I will say is that Hexcelerator, the other hardware incubator, the one over in Shenzhen that we've talked about before, they are on their second round and they're looking for new applications. Sweet. So, people are interested. I mean, Bolt has been looking for people as well, but if you're interested in heading over to Shenzhen for, I think, 12 weeks or so, and then kind of demoing in front of a bunch of big investors, yeah.

**Dave Jones:** And they'll fly you out there, right? That's part of the deal, isn't it?

**Chris Gammell:** Yeah. Yeah. Yeah. So, they give you money for investing in your company and they give you access to tooling and you work with all the Seed Studio guys. Eric Pan's part of that as well. And it seems like a cool little program. Yeah. I didn't see any of the output from it. I don't know if anyone got invested in heavily, but, you know, I think that it was a young program, so I'm sure that, you know, as more people find out about it, they'll get better. Yeah, it'll grow. Yep. Yeah. I remember that sous vide cooker that was on Kickstarter ended up, that was out of Hackcelerator. So, yeah. It's cool, man. I like it. Exciting times. And not just because of fire alarms and elections. Yeah.

**Dave Jones:** What would you take if, you know, there was a fire? Would you actually, you know, would you grab your oscilloscope? Like off my bench? Yeah.

**Chris Gammell:** I would, no, that stuff can be replaced. I'd say hard drives would be the main thing. I mean. Yeah, data.

**Dave Jones:** Right. Data cannot be replaced. Right.

**Chris Gammell:** Exactly. Although a backup, people should back up their stuff. We learned that one the hard way here. Yes, they should. Here too. Yeah. So, yeah, I don't think there's anything I would really take. I mean, like my bench has got some okay stuff, but like I said, nothing can't be replaced.

**Dave Jones:** Yeah, I don't think I'd grab anything if I knew it was a real fire. I'd just, you know. Yeah, laptops. Well, I don't have insurance. That's a concern.

**Chris Gammell:** You don't have insurance for your workplace? No. That's an important thing. I guess I should get some, huh? Yeah, you probably should be.

**Dave Jones:** Well, the building is insured, so I would get a new building, right? But no, but the actual contents, no.

**Chris Gammell:** Yeah, you might want to think about that. That is an important part of any startup and business and such.

**Dave Jones:** Yep. But then again, I figure like if this whole thing burns down, I've got more things to worry about than, you know, buying, you know, five grand worth of gear to get me back up and started, you know.

**Chris Gammell:** Yeah, but it's nice to have that five grand in your pocket. Oh, yeah, of course. Once the insurance plan comes through, so.

**Dave Jones:** Yep.

**Chris Gammell:** Well, regardless, stay safe. Don't light anything on fire, Dave.

**Dave Jones:** I'll try not to. I do have a fire extinguisher in here. I'm ready to go. That's good.

**Chris Gammell:** That's good. Yeah, you only got one exit, right? So be careful.

**Dave Jones:** Yeah. No, there's two, actually.

**Chris Gammell:** Oh, good. Good. Also important.

**Dave Jones:** Well, no, there's one exit through the door here, yes. Out of the actual office, yes. All right. But I figure I can jump through the flames, Hollywood style, you know. All right.

**Chris Gammell:** And when we start singing, it's time to end the show. All right. We'll see you next week. We have lost the plot. Bye. Bye. Bye. This episode of The Amp Hour was sponsored by Club Jameco, who allows you to upload your kit idea and make up to 10% of the sale price without ever needing to buy or bag components. Go to clubjameco.com slash The Amp Hour to see the kit discussed on this week's show and to support the show.

**Speaker ?:** Bye. x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
