---
episode: 150
title: Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness
url: https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded June 17th, 2013. Episode 150. Solar. Shopper. Sickness.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life. And you're sick. Gross.

**Dave Jones:** I am not a happy little puppy today, but we decide to soldier on instead of hold off for a day. Because we figure, you know, I could just get turned into a nasty cough or something. Right. We don't know if Dave's going to make it. He's getting old, so, you know. Yeah. So if I sound more nasally than I usually am, then we'll know why.

**Chris Gammell:** And that's saying something.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** We've determined that Dave's not allowed to laugh either because that might set him off in a coughing fit. But we'll try and edit it out whatever we could. It could. Yep. So this is going to be a very solemn episode of The Amp Hour.

**Dave Jones:** Don't throw in any ridiculous marketing things. That makes me laugh every time.

**Chris Gammell:** Yes, yes. What do you do? Did you used to skip work? I'm always interested in that kind of stuff, you know, like from people coming into work and being sick. You know, because, like, I don't have kids, right? But I know a lot of people have kids, and kids are just like germ factories, and they all transfer it from school to school. And, you know, then they go home, and all the parents get sick, too. And then, of course, I get it from the parents when they come into work because they all feel obliged to work.

**Dave Jones:** Yeah, yeah, exactly. Yeah. Yes, I'm, you know, yeah, I've done that many a time. I've gone in and soldiered on because, you know.

**Chris Gammell:** I'm a wimp, man. I'll just sit home.

**Dave Jones:** Oh, really?

**Chris Gammell:** Yeah.

**Dave Jones:** Okay. I know that's a smart thing to do because that's why you get sick days because it's actually a smart company will understand that it's beneficial for you to take the day off and not come and infect everyone and not. Oh, yeah.

**Chris Gammell:** Yeah. Places I've worked have had unlimited sick days just because it's like, you know. Wow. Yeah, yeah. If you abuse it, they know if you're going to abuse it, right? Right. But if you're actually sick, what do they get? Yeah. You know, like that policy of like, oh, well, you know, you have to come in today. It's like, that's stupid. Right. You know, if you're sneezing on your hand and touching your oscilloscope and someone else comes over and uses it, it's like, that person is also sick now. And it's just, I don't know. That's gross.

**Dave Jones:** The worst one I've ever had is, I was working for Altium and I was going to go to Shanghai, right?

**Chris Gammell:** Oh, God. Sick traveling is terrible. Yeah.

**Dave Jones:** Oh, yeah. And like a day before, we were supposed to fly out, right? Bags packed. Everything's packed. All my boxes of all the gears packed and everything. And yeah, I get one of the worst viruses ever. And this was smack on the bird flu. Oh, yeah. You know, crap. All that bird flu.

**Chris Gammell:** So I'm hearing you started bird flu. Is that what I'm hearing?

**Dave Jones:** Oh, that's it. Dave took SARS to Asia. So they were scanning like every single person who got off the plane. Oh, yeah. They were monitoring every scene. Right. This was during the big scare, right? And they scanned every single person. There's no way I would have gotten in the country.

**Chris Gammell:** So this was like, yeah, they did like face scanning, right? For like temperature differentials and everything. Yeah. Yeah. I remember that. That was weird. My worst one was I was real sick down in Texas when I used to work in the fab. And being really sick and being in a clean room, I might have mentioned that on the show before, but it's like the worst thing ever. Yeah. It's like I would just like shove Kleenex up my nose to try and like make sure nothing. Right. But even still, you know, like sneezing inside a clean room is not a good thing because, you know, if you've ever seen like a slow motion of like someone sneezing. Oh, yes. That sneeze. Yeah, yeah. It's like an explosion. It's awesome. Yeah, it is awesome. But yeah, that is a terrible existence and really fabs in general.

**Dave Jones:** Heel just plummeted. Yeah. At, who was it? Samsung?

**Chris Gammell:** Yeah, it was a Samsung. Yep.

**Dave Jones:** Heel just plummeted on all their, every Samsung device. Every Apple device that relied on Samsung memory or something.

**Chris Gammell:** Just, yep. That's funny. That's like a, that's like a butterfly flaps its wings kind of thing, you know?

**Dave Jones:** I was about to say that. Yeah, it's one of those chaos effects.

**Chris Gammell:** Yeah, process engineer gets a cold and your iPhone fails. Oh, that's, yeah, that's gross.

**Dave Jones:** I just used my mute button there.

**Chris Gammell:** Oh, good, good. Yeah, me and Dave have been talking about creating a USB mute button, but the logistics of it seemed tough because you'd have to break the stream for like a USB device, but also still stay connected.

**Dave Jones:** No, I'm telling you, do it in software.

**Chris Gammell:** Do it on client side?

**Dave Jones:** You tried to do it that way and it was dumb. Yeah, yeah. Have it as a separate device, plugs in the USB and then it's a software that just turns on the Windows mute function somehow. Now, that's it. End of story.

**Chris Gammell:** Oh, okay. It's just like a key toggler kind of thing, like a, like a foot pedal insert. Yeah. Yeah. Yeah. I've seen those before. Yep. Yeah.

**Dave Jones:** And it's got to be that dead man type because we, we've got this mute button, right? We've got the Windows one, but you always forget to turn it back off. So you start talking again. Oops. Yeah. You know, you just, so you need to have your hand on and then, whoop. Hello? McFly? Yeah.

**Chris Gammell:** Yeah. No, I'm not mucking around. If you're at the show, I'm going to be like, Dave, are you there? Dave? Bye. Dave, are you there?

**Dave Jones:** Hello, check. Check. Check. Two. Nice. Check. There we go. Yeah. Yeah.

**Chris Gammell:** That's annoying. Very, very good example there. Yeah.

**Dave Jones:** Have we had enough snot on today's show? Oh, God, yes.

**Chris Gammell:** I don't handle that stuff well. I don't, I don't do well with, I was, I've never thought I was going to be anything by a neurologically related, you know, never going to be a doctor, never going to be a... Right. Yeah. I learned that one from a young age. Uh-huh.

**Dave Jones:** Is it time for a rant? Can I have a rant? Just get it out of the way. Sure.

**Chris Gammell:** Yeah.

**Dave Jones:** You know what I hate? What do you hate, Dave? I hate it when companies automatically cancel your account because you haven't used it in a while. Why? Why? Who did this? Bloody J-Car out in Electus, their wholesale arm. It looks like they've cancelled my wholesale account. Oh, jeez. That I've had for... Ugh.

**Chris Gammell:** Yeah, you know, I just take that as they don't want my business. That's fine. Whatever. I'll move on. You know? Unless you're paying for the membership and, you know, then it's like, you know, like if it's like a membership club or something.

**Dave Jones:** Right. But it doesn't cost them anything to leave you enabled in their system. Uh... It's ridiculous. The cost of... Everyone buys stuff every month, every month. Bang, bang, bang.

**Chris Gammell:** You know? Maybe it's the cost of, you know, filing your papers or something because they're still really...

**Dave Jones:** Oh, bullshit.

**Chris Gammell:** ...really behind the times. No.

**Dave Jones:** Bullshit. There's no cost whatsoever. They've changed their system. They've just decided to purge everyone or something.

**Chris Gammell:** See, that's weird because... Stupid shit like that. You should appreciate that because most places will not just keep you, they'll sell you to other places. You know? You'll be getting emails from not just Jcar. You'll be getting them from, you know, every distributor on the planet.

**Dave Jones:** Yeah, but come on. We'll bundle you up like a CEO. Two different issues. Let's not tie those issues together. Come on. I guess. One doesn't automatically mean the other. I don't know.

**Chris Gammell:** It's just...

**Dave Jones:** It's annoying. Yeah, it's annoying. Anyway, I hate it. It's rant-worthy. It's bloody annoying.

**Chris Gammell:** Yeah.

**Dave Jones:** Does anyone else have any companies, name and shame them, that have automatically booted you out because you haven't bought something from them for six months or something?

**Chris Gammell:** Yeah. I don't think that happens to me very often. When has that happened? I guess that happens with credit cards sometimes, but yeah, not like electronics companies. I mean...

**Dave Jones:** Well, it's different with companies because if you've got like five people in the company and, you know, somebody's going to buy something from them, you know, sooner or later, but when you're on your own, when you're your own one-man band, you know, you may not do anything for six months and then all of a sudden, bam, you've got a new project and you want to buy a buttload of stuff and, you know?

**Chris Gammell:** Yeah. Bastards. Sorry, man. Should we call the wambulance? Speaking of buying, though, you've bought something new and fancy and fun. Tell us about it. Have I?

**Dave Jones:** Oh, right. Yes. Is that in your house? Hang on. I was just going to say that I've got Gary Johnson's phone number. Gary Johnson. He's the CEO of Jcar slash Altronic slash whatever they call themselves. Oh, yeah. Bend his ears out. This month. Yeah. I should. I should give him an earful.

**Chris Gammell:** I never heard of Jcar until I started the show with you. It's weird how that stuff's just regional.

**Dave Jones:** Well, yeah, yeah, yeah. It's regional. You know? I mean, it's like people in Australia. We don't care about, you know, Jameco or something. We just don't. We never hear of them. They don't advertise here. They're not a... Well, they do in the air power. I mean... Of course. Yes, they do. Of course. Yeah. But, you know, I mean, back in the day, right, they just... Yeah, you would just never, you know, heard of them. Yeah, it's weird to think about. And I'm sure there's other US suppliers no one's ever heard of. Yeah. Outside the US and other countries, so... Hmm.

**Chris Gammell:** Yeah, it's tough with that stuff, too. I saw today that there's a... There's this really awesome-looking contest from Littlefuse where they, like, are giving... Right. They're giving away a tour of NASA. Oh, what? Yeah. Awesome. Yeah. And you can't do it. Sorry. To US residents only. Exactly. Asterix. Yep. Yeah. That's always a tough part, right?

**Dave Jones:** Or to East Coast residents only. Yeah.

**Chris Gammell:** Or West Coast. Yeah, probably West Coast. West. Yeah. Anyway. It's just tough, though. You know, it's just a globalization thing. You know, it's like the world seems a lot smaller now, but it's still pretty big. And a lot of companies still aren't... You know, there's so many legal restrictions between countries, too. It's like... Hmm. As much as you want to see NASA, it's like, well, sorry, buddy.

**Dave Jones:** Yeah. Tough tits. Yeah. You're on the terrorist list because you're not a US citizen. Exactly. And even if you are a US citizen, you're still on the terrorist list. Yeah. Because, well, we don't trust anyone because we're the US government. Sorry. Let's not go there. Get it out of the way, man. Just get it all out.

**Chris Gammell:** Let's get it all out. Right. Yeah. These days. But, yeah, let's not go there. Right. But, yeah, it did look cool.

**Dave Jones:** Should we try and get... Should we try and get Gary on the radio show? Yeah. Because he does like to talk a bit and talk about the history of founding a, you know... Yeah, definitely. A component supply company like that. I might have to get in touch.

**Chris Gammell:** You should. Yeah. Give him a call. Ben is here. And then invite him on. You know, a little...

**Dave Jones:** Right. Your company's shit. And then it would just like to come on the show.

**Chris Gammell:** And while you're here... Yeah. Would you like to have an American berate you as well for... Right. Even though he's never used your services. Right.

**Dave Jones:** Yeah. It's a win-win. Yes. Oh, boy. Love it. Anyway, yes, I have something new and fun.

**Chris Gammell:** Yes. And big.

**Dave Jones:** Although I find... I feel as though I am like five years behind the times. I really do.

**Chris Gammell:** Why is that?

**Dave Jones:** I've got a new... Well, I've got a new solar power system. I've got a new three kilowatt. Wow. Massive. Three kilowatt. Apparently, that's like baby stuff. So I'm told. But yeah. Anyway, I thought it was pretty big. I've got a three kilowatt home solar power system. Apparently, everyone has been, you know, complaining that I called it a solar system.

**Chris Gammell:** What is... What is it really called?

**Dave Jones:** Because they think, oh, it's the... Well, I don't know. I guess they want me to call it a solar power system. They don't like the term solar system because that refers to the entire solar system. Like space. Like referencing space, right? Yeah, space. As in...

**Chris Gammell:** Who cares? I mean, that's stupid.

**Dave Jones:** I didn't think of that. Yeah. Yeah. Anyway. Solar power system. Yeah. But I feel like I'm so far behind the times. Every man needs dog everywhere I drive. Everyone's got a bloody solar system. Well, yeah. Sorry.

**Chris Gammell:** Because of that thing you mentioned in the video. It's the feed-in. We've talked about that before. The feed-in tariffs were huge in Australia. You know? Like that's...

**Dave Jones:** For a time, yeah. Yeah, for a little while. And that just fueled the explosion. And I probably should have bought at the time, you know? Yeah. Well, I didn't. I was dumb. And now I get a lousy six cents instead of 60 cents.

**Chris Gammell:** Yeah. And if people don't know, the feed-in tariff is basically... It's like a subsidized rate for selling power back to the grid. So, you know, your inverter turns on and you start raking in bucks.

**Speaker ?:** Yeah.

**Dave Jones:** And then there's two systems, net and gross. I'm on net. Yeah. What that means is that I only get paid for the excess energy I put back. So, my house uses it first if it's during the day. And I've got, you know, something turned on during the day in the house. And I use it instead of exporting it back to the grid. But gross is... Tariff is where you get paid for everything going back regardless of, you know, whether or not you use it.

**Chris Gammell:** Why? Because then you just get charged from them as well? Is that the idea?

**Dave Jones:** Oh, well, yeah. You get charged your normal rate for using the energy, but you get paid for every cent you export back to the grid, which is all... Yeah. Every kilowatt hour you generate. So, you get paid for it. Whereas I only get paid for the energy that I don't use.

**Chris Gammell:** Right.

**Dave Jones:** And put back. So, that's the difference. Anyway, yeah, so I'm getting shafted two ways. I've got a net system and I've got a lousy six cents per kilowatt hour.

**Chris Gammell:** Yeah, but that's not why you did it. Come on. No, no, no. I did it because you're a tree hugger and, you know... In a good way.

**Dave Jones:** Yeah, exactly. But no, it'll pay. It should... Well, I'm not measuring my consumption at the moment. I need to buy another doodad that measures my consumption. Right. But yeah, I... Like, my rough calculations were... It would pay back in five years tops. So, you know... Yeah, that's totally worth it. And the inverter has a 10-year warranty. The solar panels have a 20-year life... Well, you know, output warranty. Yeah. If they're still in business, you know. Right, of course.

**Chris Gammell:** Yeah. Well, LG, they should be around.

**Dave Jones:** LG, yes. I went with the LG. I specifically paid more to get the LG panels figuring that they might be around in, you know, 10, 15 years' time.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, it's interesting.

**Chris Gammell:** We don't talk about the grid much on here because it's, you know, it's... We talk more about electronics than the actual electrical systems, you know, behind everything. But, you know, like, I've seen a couple articles about the effect of solar in the coming years. And just from a grid normalization standpoint, I mean, like, if people don't know, like, actual power plants, like, most of their money is made actually at peak times. So, like, when a hot summer day, they flip a switch, they turn on an extra turbine, and that's actually when they start cranking out all the money, right? All the normalized stuff is not as big a deal. And so, if you, you know, if you get to the point where a lot of people have solar and it helps, like, basically, it effectively is, like, you know, if you're looking at it as, like, an electronic system, that would be, like, the, you know, the bulk capacitance for the system, right? Where it normalizes these ripples of, you know, people turning stuff on and off. And it adds capacity to the system, right? But if you don't have that anymore, then the whole economics of the grid change, and it just gets weird really quick. I mean, like...

**Dave Jones:** But that's why they're being smart, no pun intended, and switching everywhere, trying to get the government to mandate smart meters, you see?

**Chris Gammell:** Ah, yeah, yeah.

**Dave Jones:** So that you get charged per usage hour, you know, the time of the day you use the energy. So there'll be peak, off-peak, shoulder times, all that sort of stuff. And you can get charged double or triple during peak hour. Right, right. Yeah, peak hour. And, uh, sounds like traffic, you know. Yeah. But, yeah, that's the idea, you know. And they go, oh, but it'll be cheaper, you know, because you only pay for energy when you use it. And it's like, yeah, bullshit. Yeah. I checked here in Australia, at least one company, the company I'm with, in Victoria, they don't have it in New South Wales, but the peak time is from 1pm to 8pm. So it's like, bam, you know, you've come home, you're cooking, you're watching TV with your five kids and you, you know, you've got all your air con running because it was cold or hot. You're using a hairdryer or anything else.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, exactly. And you're taking your hot showers, you know, and it's like, yeah, of course, you're, you know, there's no way you're going to pay less for something like that. You need more of an unusual type, you know.

**Chris Gammell:** Like a lifestyle, like a second shift or something. Yeah.

**Dave Jones:** Yeah. Yeah, exactly. You, you have to be a shift worker or something like that to really see massive benefits. Yeah. And, uh, anyway. Hmm. Well, it's interesting that we're going to have to change our habits a bit to get the maximum benefit because now effectively, because we're not getting paid much feeding tariff for our solar power.

**Chris Gammell:** Yeah.

**Dave Jones:** Then it's sort of either use it or lose it kind of thing, you know, use it or not get paid much. So we're going to, you know, put our washing machine on during the day, our dishwasher on during the day. Right. And stuff like that. Try and use energy during the day when, uh, and warm the house up during the day or something like that.

**Chris Gammell:** Right. Because it's winter there, as I always forget. Yeah. It's winter here at the moment. Right. Right. Or you could get a battery system. That's the other option, right? That's the, uh, although that's more cost.

**Dave Jones:** They're horribly inefficient, expensive and maintenance. Yep. No. If you're hooked up to a reliable grid, there's no point having a battery system unless you really want to stick it to the man and, you know, not use a drop of electricity. Or you want to build it yourself.

**Chris Gammell:** I think, I think battery systems are, they're, they're still dangerous, right? But I think they're, in terms of the realm of what you'd want to do, you know, you could probably, you know, engineer your own battery system for your house versus I think doing that versus like trying to do an inverter would be much more, much more advisable in my opinion. Exactly.

**Dave Jones:** Don't do your own inverter, folks.

**Chris Gammell:** No. And those things are really efficient too. That's what, I'm always amazed at that, like the efficiency of those things. They're like, what, mid to high 90s? Is that right? Uh, yeah, at least. Yeah. Yeah, like 98 or something like that. Yeah. Very high. Right. Yeah. I guess that adds up pretty fast if you don't have that. So. Well, now the real question is, are you going to try and, uh, go all Dean Kamen and, because it's his, uh, I think I read about his house on, uh, North Dumpling Island. He's got like LED lights all over the place. He like, he designed a completely custom DC infrastructure, you know, so basically he just taps off his solar panels and then he, I think he, he has a storage system out there because it's just, uh, it's off the grid, but.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** You can do that then?

**Dave Jones:** Well, that's, well, there's no point because, you know, like if you want to run your LED lights directly from your DC panels, for example, then, uh, what's the point? Because you don't need lights during the day when the sun's out.

**Chris Gammell:** Oh, that's true. I guess you would need to have actual storage system at that point.

**Dave Jones:** You would need to have a storage system.

**Chris Gammell:** And of course the point is not to actually have lights, it's to, you know, show everyone how to build it. That's the fun part. Oh, right. Yeah. Of course. Yeah. Oh boy. There's a.

**Dave Jones:** Yeah. So I, I find myself getting sucked in now. It's like, oh, I've got my data exporting to the grid and I'm going to automate, uh, the grid export into the web. So you can actually see all my solar power. I'm going to have it live up there and now I'm going to track my consumption. I'm going to get one of, I'm going to tie that in and I'm probably going to track the temperature and I want to track the mains voltage and blah, blah, blah, blah, blah. And you just get sucked into the stats behind the whole thing, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And I, I love stats, you know, graphs and things like that.

**Speaker ?:** Right.

**Chris Gammell:** Of course. Of course. Graphs are great. And you know, it's like a game at that point, right? It's like, it's just the, it's the engineering mindset of wanting to optimize things. So you, you see how you can, how you can optimize the system and, you know, oh, oh, oh, just don't turn that off for, don't turn that dishwasher on for two hours. Yeah. Right. Or, you know, like.

**Dave Jones:** Yeah. Yeah. Yeah. It's right. It's fun. Yeah.

**Chris Gammell:** The, there, there was an article actually on O'Reilly's rate, the, the radar site, which is like their, their ongoing blog. And it's about, you know, like, so internet of things, right? Let's just get the term out there. Right. So stigma term, but at the same time, right? The author of the article, he's, he's basically saying like at a certain point, every, every technology becomes commodity. Right. And he's saying that this is kind of the next thing, like the connected devices is, you know, we, we get pissed off on the show and we say internet of things, but what happens when it's just connected? It's not like a big deal anymore. It's just, okay. You just plug a cat five cable on the back of your dishwasher or your, your thermostat is wireless now. Right. I mean like the nest thermostat. Yeah. And it's, it's interesting, interesting from that perspective of like, well, yeah, I mean, it's always started. Technology always starts super crazy, right? Oh, electronic control of, uh, you know, even like a battery powered thermostat, right? It's, oh, it's not running with a mercury switch. Oh, okay. Well, or whatever that other, that little metal coil that was in there on the old thermostats, you know, like that was, that was a weird technology at one point too. So.

**Dave Jones:** Well, doesn't it take like 20 years for a technology to become integrated in mainstream society?

**Chris Gammell:** It sounds about right.

**Dave Jones:** I think that's sort of, I, you know, yeah. Almost everything you can name, like, you know, toasters, TVs, computers, everything you can possibly imagine took probably 15, 20 years to sort of become, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, there is a curve. Integrated with our society, second nature.

**Chris Gammell:** I forget what it's called. There's like a, you know, a product adoption curve and, and they, and they actually map it out over time too of like where certain things are. I remember I've seen it recently for the, for like where 3D printing is on the curve, right? Because 3D printing is not new and, you know, it started in the eighties, right? No, no, no. But, yep. But in terms of that, where it actually is on the curve, it's different. Oh, it's. You know, it's, it's more publicly acceptable. It's commoditized, everything. So.

**Dave Jones:** Well, yeah, but I think it's 10, 15 years away from mainstream.

**Chris Gammell:** Eh, maybe. I mean, uh, it's, I, I don't know. Like, like mainstream, like as a, I guess, I guess like an appliance, right? That, that is the ultimate measure of. Yes. Yes. Exactly. Because then it's commodity. It's, you know, it's lower cost. It's accessible to the masses. It's pretty dumbed down. But then, you know, there's certain technologies where it's just like, well, is that ever going to happen? I mean, like.

**Dave Jones:** Well, see, it may not.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. Because the 3D printer, what do you use it for? To print objects. Where do you get the files from to print those objects? Yeah.

**Chris Gammell:** It's the hype curve. That's what it was. That's what I was thinking of. Because it, it not only is, you know, the actual adoption of it, it's also how much people talk about it. Right. And, and where, where it is on, you know, oh, this is going to be the next thing. Right. Well, if, if it's super hyped right now, there's like a top peak of, of inflated expectations and then it dives back down, people forget about it and then it finally comes back. Google Glass? Oh, we're, I don't even know. I think that's a trigger. Like the very early side of things.

**Dave Jones:** Right.

**Chris Gammell:** Yeah.

**Dave Jones:** Have you seen the Google Glass teardown? I have. Oh yeah, that was good. It's not that surprising. There's not much in it. Duh. Like, you know, it's had exactly in it what I expected to be in it. Yeah. Duh. You know, it's not like mega revealing.

**Chris Gammell:** Duh.

**Chris Gammell:** And you know, it's, it's tough to tell too, because the, the price point isn't realistic yet as we know. Right. Uh, it'll be interesting when they, when they finally release a final price to see what, you know, then you can really start comparing these parts and everything to prices and, and see how that actually fits together versus what it is now. It's just like, okay, well, yeah, parts. But yeah, it was done by, uh, SparkFun sponsored it, I think. And, uh, Star, Star Simpson.

**Speaker ?:** Yeah, I think so.

**Chris Gammell:** Something like that. And, uh, I forget who the other person was.

**Dave Jones:** Yeah, someone like that.

**Chris Gammell:** And I think, I think this finally makes up for Star. Uh, she, uh, I'm still mad at her because the, she, she's the one who started the Taco Copter rumor. Do you remember that? Uh, no. It was a, uh, uh, Quadcopter service, a taco delivery service by Quadcopter. It was this, it was this, you know, I, I, I forget. It was an April Fool's joke or something. I think it might've been, but it wasn't, I, I, I found out later it wasn't real and I was very angry because I was so excited about the idea of tacos delivered by flying UAVs. But yeah, uh, so the, the, the, the, I can't believe you fell for that. What? It's going to happen. There's, there's another technology. Like, uh, they're talking about like Quadcopter delivery off of UPS trucks. That's, that's another technology that, that could happen. Right? I mean. It's ridiculous. It's not going to happen. It could happen.

**Dave Jones:** It's not going to happen.

**Chris Gammell:** I'd say it wouldn't happen because of insurance companies.

**Dave Jones:** It's just not going to happen. It's not practical.

**Chris Gammell:** Hey, Joe, how's the delivery job going? Well, you know, I chopped up someone's dog yesterday. Yeah. The Quadcopter got out of control. I chopped up someone's dog.

**Dave Jones:** Sorry. Packages weigh a fair bit. Okay. There's just, you know, it's just stupid to think that that's viable. And, you know, the UAV to deliver your pizza. You know how much of a good pizza weighs? You know? It's true. It's just ridiculous. It's not going to happen.

**Chris Gammell:** Especially if you like the right amount of cheese. I mean, if you're, cheese ain't, cheese ain't light. Right.

**Dave Jones:** Want a heavy slice. But you've got a big, thick crust. None of that thin crap. Exactly. Exactly. Yeah. Right. It's not going to happen. Tell him he's dreaming. All right. Sorry, that's an Australian joke there.

**Chris Gammell:** Yeah? What's it mean?

**Dave Jones:** Yeah. Oh, it's from the movie The Castle. If you haven't seen it.

**Chris Gammell:** No, I haven't.

**Dave Jones:** No. You have to see The Castle. They've Americanized it. Oh. Apparently. I haven't seen the American version in quote marks, but apparently they've changed a few Australianisms to words that Americans can understand. So, anyway, it wouldn't be nearly as funny in America as it is here in Australia. Anyway.

**Chris Gammell:** I'm sure lots of things aren't, Dave. I'm sure you guys got lots of inside jokes that we wouldn't get.

**Dave Jones:** Yeah, yeah. Exactly. And vice versa. Right. Of course.

**Chris Gammell:** Of course.

**Dave Jones:** Yeah. But anyway, if you hear me say, tell him he's dreaming, then you know where that comes

**Chris Gammell:** from. Yep. Speaking of dreaming, so this is the dream of FPGA programmers everywhere. Maybe. Maybe not. I don't know. So, I found out about this new library for FPGAs. It's called MyHDL. Have you ever heard of that?

**Dave Jones:** No, I haven't. But isn't there an open HDL thing?

**Chris Gammell:** I don't know.

**Dave Jones:** Yeah, you're talking about modules and things.

**Chris Gammell:** Oh, you're talking about the open... Yeah, I know. You're talking about FreeRTOS.

**Speaker ?:** Yeah.

**Chris Gammell:** Not FreeRTOS. God damn it. OpenCores. You're thinking... OpenCores.org. Thank you.

**Dave Jones:** Yes, I'm thinking OpenCores.

**Chris Gammell:** Right. No, that's... So, OpenCores is actually... That's actually VHDL and Verilog. Primarily. I haven't seen any, like, System C or anything, like, crazy on there. System Verilog. But no, that's actually...

**Dave Jones:** And what else is there?

**Chris Gammell:** So, that's actually coded in... What else? In HDL. So, this is a Python library, though. So, that's what's different. What's Python got to do with FPGAs? Exactly. So, basically, it's... So, this is a high level... Higher level, right? Because HDL... Like, VHDL and Verilog, they can go down really low, and you actually, you know, create registers, and you can actually, you know, create structures in logic, right? This is more... Which is the whole idea of the advantage of FPGAs. But go on. Well, no, no, no. Okay, so, yes, I do agree with that. But when you're trying to do higher level functions, right? Like, really math-heavy stuff, like DSP type of stuff inside of FPGAs, which is increasingly a very big component of FPGAs, right? You don't want to necessarily code everything by hand each time.

**Dave Jones:** Right. Oh, okay. So, it's a Python to hardware compiler, just like you can get C to hardware compilers. Yes, exactly.

**Chris Gammell:** Exactly. Right. Yeah. Okay. Right. And so, yeah, I mean, it's just, like you said, I mean, C to hardware exists, but the ones I've seen you've had to pay for as well.

**Dave Jones:** Altium has it free. It's all built in. Oh, they did? C to hardware compiler.

**Chris Gammell:** Okay.

**Dave Jones:** It does kind of work, you know? You can write your C code and you can just go convert to hardware. Yeah. And then automatically converts it to a hardware module and then plugs the processor code into the hardware module and boom. Yeah. Right. It does actually kind of sort of work. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** But, eh. Well, okay.

**Chris Gammell:** So, there's goods and bads, right? I mean, because I've tried learning Python. I haven't gotten there yet. I've been using those, not Coursera. What's the one? Code Academy. I've been using Code Academy. Right. That just doesn't, I don't know, coding. But, I mean, there is benefit to this, right?

**Dave Jones:** And here you are wanting to do an electronics learning.

**Chris Gammell:** That's electronics. I'm just saying coding just doesn't hold my interest. That's what I'm trying to say. Right. Okay. Yeah. I mean, a lot of people use that stuff. I mean, it's not like, you know. Anyways, that's besides the point. Contextualelectronics.com. So, I have done, though, in the past, I've actually done DSP work on FPGAs and I've always done it from, I did it from Simulink, doing Simulink down to, and then that converted to VHDL and then you push that down into a FPGA. Right. And then that actually, you know, did the signal processing. This is basically, I think this is somewhere between C and Simulink because Simulink's like super, super high level, where C is, you know, high level but not that high level. And then, you know, I think this Python thing would be somewhere in between. And, I don't know, I just think it's pretty cool. So.

**Dave Jones:** Yeah. It's like, meh. Meh? If you happen to like Python and you happen to need a Python to hardware compile, fine. It exists.

**Chris Gammell:** I think it's one of those things where, you know, it opens up, it opens up digital hardware, you know, building your own digital hardware to more people, right? I mean, there are going to be issues with it, right? Because troubleshooting sucks.

**Dave Jones:** People who want to, but the people who know they need to don't want to use that. It's like, no, it's just not going to, it's not going to become mainstream. Oh, no, probably not.

**Chris Gammell:** No, I don't, I don't think it would be either. But it's just another option, right? I mean, it's just like.

**Dave Jones:** It's just that, that's why I'm going meh. It's just another option. Great. Okay. There's a Python to hardware compiler now. Great. For those who specifically need that. Knock yourself out.

**Chris Gammell:** You're putting the kibosh on it, man.

**Dave Jones:** I like it. I like it. It's, well, fine. It's, you know, it's, so do I. It's okay. But, you know, it's not going to suddenly make FPGAs more attractive and everyone's going to use FPGAs. Sorry, maybe I'm a bit burned because I spent four years at the company. Yeah. That.

**Chris Gammell:** I think that might be coming out.

**Dave Jones:** Their entire vision was that the future of electronics would be FPGAs. And it was like. That's true. And I just giggled every time I walked into work, you know, it was.

**Chris Gammell:** Right.

**Dave Jones:** It's crazy. And I was right.

**Chris Gammell:** Well, people have been saying that for a long time, right? Obviously. And I'm not going to say it here that, you know, FPGAs are the future. Because instead we can have, we can have someone else say it. There's another article by, I think, Proper Fixation. But basically, you know, kind of like as an overview about FPGAs and why people do and don't use them. And basically this, Joseph K. is making an argument for FPGAs being much more widely spread. So I don't need to say it because this person is. But also the other point that he's making is that it's not just FPGAs anymore, right? It's not just, you know, FPGAs of old, right? Or CPLDs before that. Or what was before that one? The, not ECL. Let's see.

**Dave Jones:** Gals. Gals.

**Chris Gammell:** That's actually Gatorade. Pals and Gals. Is that right? Yeah. Yeah.

**Chris Gammell:** Pals and Gals. Yeah. That was just, you know, programmable gates, right? And then it moved up in abstraction layers to, you know, registers and then whatever slices or whatever Xilinx and Altera and everybody else are calling it these days.

**Dave Jones:** There's a lot of people who still look at it effectively as a Gatorade, you know? I mean, whoop-dee-doo. It's got flip-flops. It's just got gates arranged as flip-flops. Yeah.

**Chris Gammell:** But it's got look-up tables and everything else too, right? I mean, like, it's not just gates. Yeah, yeah. They are different architectures.

**Chris Gammell:** Yeah. But now, I mean, now it's moving up even more, right? Where, you know, now FPGAs have, they've pushed hard processors back in, right? I mean, you can't almost, I think every top, all the top four vendors have that now where they all have a hard processor in there again. You know.

**Dave Jones:** Because they admit a defeat that FPGAs weren't the future. Oops. People want processors. Okay. Well, yeah, it's not very efficient and blah, blah, blah. All right. We'll put a hard processor in there. They go into hard silicon for bloody everything.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, not everything. FPGAs are turning into processors with a bit of FPGA fabric. That's where it's headed.

**Chris Gammell:** I agree with that. I think that is the future. I always thought that Intel was going to push some stuff into there, like that a different chip vendor was going to buy IP from like a Xilinx or an Altera, but, or maybe they did at one point. I don't remember. But. I don't know. I always, yeah, I think that that was going to be a bigger thing too, because I got really excited when Actel did that. They had, they had said that, oh, you know, we're, we're making microprocessors that just happen to have programmable logic, right? Because that's. Right. Yep. Yeah. I mean, because the real benefit of the logic, the programmable logic is doing, it's doing the custom fast functions. So.

**Dave Jones:** And often a system, you know, is mostly you do it CPU based and that you might need a small function that you have to do in hardware.

**Chris Gammell:** Right.

**Dave Jones:** Yeah. You know, you might, you might need a serializer or something, you know, and bam. Okay, great. I've got a little bit of FPGA fabric I can do that in and, you know, yeah.

**Chris Gammell:** I think it's cool. But yeah. So FPGAs. I don't know. I still, so anyways, I, I think the, the, my HDL, I think that's cool. I, I'd like to try it eventually. It's all open source. It's a, there's a good, good bit of documentation. So if people are Python programmers. Sure. They can jump in.

**Dave Jones:** Knock yourself out.

**Chris Gammell:** Yeah. It's great. Post some links to that.

**Dave Jones:** Because those sort of things are fun. When they work for your application, like just like the C to hardware compilers. Yeah. When they worked for your application, they are magic. Right. Yeah. Because you just write your traditional C code and bam, you push a button and you know, if all your parameters are right and everything else and, and bam, it's, you know, it's magic. It really is good.

**Chris Gammell:** Yeah.

**Dave Jones:** For those who, but it's not a universal solution, but for those that it suits. Yeah.

**Chris Gammell:** Yeah. I was like that. Shall we have a. Oh, go ahead.

**Dave Jones:** No, I was. No, no. Please finish off. I was going to completely change direction.

**Chris Gammell:** So I've used the, there was one where it wasn't just C to hardware for like custom blocks of logic, but there's also one where like you could create, I think it was Altera. You could create a, a, God, I can't even think of it now. It was an instructor. You do a custom instruction. So you actually set up an instruction in the processor for like super high, super used commands and stuff. You actually set up as an, as, as a specific instruction directly inside the processor. So it's like really fast. I always thought that was really cool too. Got it.

**Dave Jones:** But that's, that's, that's pretty cool. Yeah.

**Chris Gammell:** Yeah. It, like you said though, it's, it's, it's hard to integrate. And especially if you don't, if you don't have that when you're going in, right. If you're a software program and you're not like, you're not thinking about, well, should I push this to hardware? Where you're thinking, how can I optimize this code? Right. So you're right that, that hardware programmers often, or hardware, hardware, I guess that's, that's correct. You know, digital hardware people have that.

**Dave Jones:** A hardware programmer is called a soldierer.

**Chris Gammell:** Well, yeah, I don't know. I've referred to digital hardware people as hardware programmers, I guess. Right.

**Dave Jones:** Yeah. All right. Let's move on. My, my, my favorite programming language is still soldier.

**Chris Gammell:** Yeah. Mine too. Because I can't do anything else. You're right. Yeah. Because we suck at it, right? Hello world. That's a blink, blink, blink. So what's up? You were going to, you were going to change the subject. What were you going to change to?

**Dave Jones:** Come on. Let's have another ranty bitch time. Circuit Lab. The online. Ah, yeah. Hello. Nobody predicted this coming, folks.

**Chris Gammell:** Right.

**Dave Jones:** Circuit Lab. We've, I have, we've talked about them before shortly. Yes.

**Chris Gammell:** Yes, we have. And they, they have, I have them. They're always in my site because they're like a Chrome plugin. So it's like a Spice Chrome plugin.

**Dave Jones:** Yes. Yes. Yes. Yes. And they're one of the current 20 million, um, online PCB slash, um. Yeah. Is it, do they do PCB? Yes. This is, this one does PCB, doesn't it? I didn't. No, I didn't think they did. No, no. Oh, this is only, only does circuits. Right.

**Chris Gammell:** Yeah. I thought it was just space. I could be wrong. But.

**Dave Jones:** Spy, simulator, or whatever. I, I lose track of all these companies. There's like a dozen of them now. Yeah. I was exaggerating before. I tend to do that. There's like a dozen of them now or something, or close to that number, of these online PCB schematic simulation, blah, blah tool, you know, CAD EDA tool. Yeah. Right. And they're charging. Now they've decided to go, well, who is it? Somebody complained. Somebody on Reddit. Oh, yeah. Complained, did they? Jezcombe. Yeah.

**Chris Gammell:** I don't know.

**Dave Jones:** I don't, I don't know that name. Sorry. Jezcombe. Yeah. Yes. Jezcombe. Anyway, that's their Reddit name. And they're complaining that, um, that they were happily using CircuitLab. Then all of a sudden they found that all their files were watermarked. All of their output files were watermarked. Yeah. And, uh, nag screens with, you know, enforced timeouts and all sorts of stuff. We haven't tried it ourselves, so.

**Chris Gammell:** Yeah, I tried it back in the day. Like I said, I had, I had it installed and I haven't. Yep. I mean, that's the thing. Like, you know, I said that on, on the Reddit thread too. It's like, okay, it's, I like it. It's, you know, it's a decent simulator, but I still use LTSpice the most, you know, it's on my computer. It's, it's never, never. All it does is nag me to update. I don't care about that. You know, I'll ignore that every time. But yeah, it's, it's tough. You know, like I, I get it that companies need to, uh, you know, they, they gotta make money, but.

**Dave Jones:** Well, they, this was a startup, right? They need to monetize it in some way. So it's been free for, I don't know, six months or something. Yeah. And, uh, they've all of a sudden decided, uh, yeah, looks like you gotta pay. If you want the professional version, it's, uh, 30 bucks a month, which, um, I don't think is, you know, the poster complained about that it was, you know, mega expensive at 30 bucks a month. Well, I don't necessarily think it is. Yeah. But, um, I mean, what professional is going to use a web based EDA tool that can't do PCBs? Like just simulation, like not many professionals out there, as you say, they're going to use LT Spice or something else. They're not going to use one of these web ones.

**Chris Gammell:** Yeah.

**Dave Jones:** I, yeah. Sorry, guys. Sorry. Yeah. I, I, I can't help but think, you know, I mean.

**Chris Gammell:** Well, yeah, of course we, we expanded out to every, every tool, which may or may not be the case, right? I mean, like there, there is a place probably for everything and it's. Of course. Of course. It's just, it's tough. You know, it's.

**Dave Jones:** I, yeah, I can't see any of these online CAD EDA tools being picked up by the professional market. Um, I could see. I think that's a really hard sell. That's a really hard sell.

**Chris Gammell:** Well, as I, I've said before, I mean, if you let me export to, you know, KiCad and, and you can pull, pull files back in from KiCad, then yeah, fine. That's great. Cause then I can share. I, you know, that's the thing. I love the sharing aspect of all this stuff, right? I mean, that, that is by far their strongest point. And I think, I think they, you know, they grab a lot of people with that and rightly so, but, uh, it's everything else is tough.

**Dave Jones:** The thing they're doing wrong though. Okay. Charge you 30 bucks a month for professional commercial use. Yeah. Fine. No problem. But their student educator and their hobbyist versions are four, are five bucks a month. Right? Yeah. Why? No, it's a stupid concept. You have a free version and you have a paid commercial version. End of story. Anything else is just stupid. This is what I hate about Altium at the moment. And I'm going to have to do a rant because they don't have, they're not tackling that free market. That's why Eagles beat their ass to death in the low end.

**Chris Gammell:** Right. Right.

**Dave Jones:** It's because they offer that free version.

**Chris Gammell:** And I, yeah, I think they have a, well, that's the thing. So we should say though, I mean, so, uh, Circuit Lab has a free version. It's just, it'll, it'll continue to have the screens and, you know, the pop-ups and everything. And basically it's, yeah, we're not sure of the exact.

**Dave Jones:** Yeah. And watermarked maybe. I don't know. So the claim is, but. Right. But a hobbyist version for five bucks a month, just make it free.

**Chris Gammell:** Yeah.

**Dave Jones:** People are actually quite honest, you know, like if they're actually going to use it for commercial purposes and it's a reasonable price, they'll actually pay it. Yeah. You're not going to have too many people ripping you off at the low end.

**Chris Gammell:** No, at the low end, if, if they want to use it, they're just going to find it anyways. Right. I mean, like, you know, if someone, if they need software, they're just going to go.

**Dave Jones:** No, no. At the high end. Oh, at the high end. They're going to rip you off. At the high end, the high end, like the Altiums of the world, they're going to pirate your software. Right. Because there's no affordable version. Who's going to do that? You know, if.

**Chris Gammell:** You think that. Everyone does it. Oh, I don't think companies do it. I mean, it's the thing. Like.

**Dave Jones:** Oh, no. Well, companies, right? Okay. No, but no, I'm talking about the lower end. Right. If you've got a high end tool. Yeah. And you're, and you don't offer a lower end version, people are going to, you know, just pirate your software. But if you've got, if you've got a free low end version and then you've got a more expensive, like a reasonably priced commercial version, people don't mind paying the money. Most people don't mind it. Yeah. If it's a reasonably priced, which this slight 30 bucks a month is certainly, you know. Oh, yeah. From a business perspective, I think it's good. Yeah. No, it's cheap.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. I guess, you know, everybody's got to make choices about what they want to try and charge, right? I mean.

**Dave Jones:** Yeah, of course.

**Chris Gammell:** I'm sure when my thing starts up, people give me crap too, but whatever.

**Dave Jones:** Yeah. But likewise, you've got to have free content as well. Exactly. You've got to have free to entice people in.

**Chris Gammell:** Yep.

**Dave Jones:** Does anyone at all out there think Eagle would be as popular and de facto as it is now in the open source hardware industry if it didn't have the free version? No.

**Chris Gammell:** No, I don't think so.

**Dave Jones:** You'd have to be a fool to think that. Yeah. I mean, that's. It's because of that free version. Right. With no limitation. You know, yeah. Okay. You work with your limitations. There are limitations, yeah. Well, yeah. Size limit. But it doesn't watermark your files, right? It doesn't ruin them. It allows you to do, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** And then they've got a reasonably priced commercial version of that. So if you want to produce, what is it? 50 bucks or something? I don't know. Don't quote me, but it's not. On what?

**Chris Gammell:** On Eagle?

**Dave Jones:** On Eagle. If you want to do, keep it to the small size, but then release commercial products.

**Chris Gammell:** I don't know. I haven't looked at their pricing in a long time. Oh, something.

**Dave Jones:** Anyway, it's, you know, it's not that expensive. It's, you know, it's quite reasonably priced. So I would, I would hazard a guess that most people using, well, a lot of people using Eagle, for example, that do actually sell their products, right? You know, an open source hardware person selling their products. They do probably pony up the small fee for the commercial version. Yeah. Because they want to feel good about it, you know? I think at a certain point, too, though. If it's a reasonable price.

**Chris Gammell:** Any kind of software, if you're, you know, if you're using it already, right? And someone says, all right, well, you can't make anything and you've already done 90% of the work. You're just going to be like, all right, yeah, fine. Just give me it. You know, like, that's fine. Just use my credit card. Go. Go away. Yep. Yeah.

**Dave Jones:** If it's reasonably priced. Yeah. Of course.

**Chris Gammell:** Right.

**Dave Jones:** If it's not, then, well, people will find a way around it.

**Chris Gammell:** Right. Yes. And that does happen. Right. Yeah. And the Eagle Lite is 70 bucks. And then the...

**Dave Jones:** 70 bucks. There you go. Yeah. Does that allow you to do commercial?

**Chris Gammell:** This is poorly formatted, Paige. I don't know. I could be. Hobbyist is 169. I could be wrong. For non-commercial. That's for the full version. And then Eagle Lite is the commercial for 70. Right. Yeah. But that's the restricted. Right. Right. That's weird.

**Dave Jones:** Yeah. Size. But, hey, if you work within those limits, then, you know, you pay you 70 bucks. It's cheap as.

**Chris Gammell:** Yeah. Right? Sure. Especially if you're making money from it. I mean, yeah. Yeah. That's true. Yeah. And that's the thing. I mean, like, you know, anytime... You know, I've been going through this with, like, WordPress stupid stuff, right? Like, blog stuff. Right. At a certain point, it's like, you know, I used to stress about $60 themes and everything. And after, you know, after spending 10 hours troubleshooting, you know, like, PHP and teaching myself all that crap, like, I can learn it. I know I can learn anything. Right? But 10 hours worth? Like, that and me ripping my hair out the whole time? Like, no, that's not worth it. I mean, that is just... There's no reason.

**Dave Jones:** There's $1,000 at commercial rates if you're charging your time.

**Chris Gammell:** Exactly. And at that point... And even... Not even that. Just for that... Not having that... Oh, that terrible feeling in your stomach where you're just like... I... You know, like, there's something to be said. Like, if you're struggling, right? If you're working on electronics or some other hobby you enjoy and you're struggling and learning from it, that's great. If you're just banging your head into the wall because you want to... You know, you just want to get done. You don't care. You just want to get done.

**Dave Jones:** You do something simple and just get it done and... Yeah. Yeah.

**Chris Gammell:** Yeah. That's right. Yeah. Yeah. I mean... Just pay. Yeah. That's it. And we were talking about this before the show, right? I mean, like, double E's... Not even just double E's. Just, you know, makers in general. Just people. If you have enough time, you can learn a lot of different things, right? I mean, like, a lot of trial and error, you know, just practice and YouTube. I always say that, like, you know, with YouTube and enough time, I could learn a lot of stuff, you know? Learn machining that way. Not well. Well...

**Dave Jones:** Do engineers in... Do engineers and hackers and hobbyists instinctively have a better ability to learn new stuff? I've... I think they possibly do. That's probably what got them into it in the first place. Maybe. Well, is your average dumbass who just can't learn anything for whatever reason or doesn't want to? Or is it just an attitude thing?

**Chris Gammell:** I think it's an attitude thing. That is the thing that I keep seeing over and over and over again. You know, I see all these success stories and, you know, you look at, like, the epic struggles of here and there. And the only thing that... Not the only thing, right? But the primary thing that always jumps out to me is perseverance, right? That just that... Yeah, okay. You didn't learn it that time. But you kept trying it, right? Eventually, you're going to get something. And that perseverance is... Like, that is such a key aspect of success that it's... It's getting repetitive, to be honest.

**Dave Jones:** Although I know people that persevere for years and, in some cases, even decades on a project and never get it done.

**Chris Gammell:** Right. You know?

**Dave Jones:** Well, yeah.

**Chris Gammell:** It's not the only thing. But if you look at people that are successful, it's always there, right? It's never like...

**Dave Jones:** Yes, of course.

**Chris Gammell:** You know, you might also need good mentors or, you know, good resources or a little bit of luck. But it's an inclusive thing where you... If you're successful, you definitely have perseverance. If you have perseverance, you're not necessarily successful. So...

**Dave Jones:** Yes. Yeah, I... Hey, that's me. You know? I, you know, work for years producing videos, day in, day out.

**Chris Gammell:** Yeah.

**Dave Jones:** And ultimately, yes, it led to some success. Yeah. You know? Now I'm doing it full time. Now you get to talk to me every week. It didn't necessarily have to work that way. You were just like... And... Yeah. Every week, man. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And that's the same thing with our show, right? We, what, did a hundred plus episodes before we got our first sponsor. Right? Yeah, that's true. Even, you know, this is not a full time gig for us. No. No. Obviously. But, yeah, but now we're starting after, what, two years of work and, you know, a hundred plus episodes where...

**Chris Gammell:** 150.

**Dave Jones:** You know, starting to get some traction.

**Chris Gammell:** Oh, this is 150, isn't it?

**Dave Jones:** Yeah. Something like that. Yeah, yeah. I think this is 150. Yay! Yay! 150. There you go. Yay! We did it! Yay! Yay!

**Dave Jones:** Yay!

**Dave Jones:** Yay!

**Dave Jones:** What was that? I don't know. Blown your nose?

**Chris Gammell:** No. Yeah.

**Dave Jones:** It's my brass rosy.

**Chris Gammell:** We, uh, we should... What? I have no idea what you're doing right now, man. That's it. 150. I'm done. I'm out. Anyway, I'm... Woohoo! Woohoo!

**Dave Jones:** I'm taking, uh, um, I'm taking, um, resumes now, folks, for a new co-host. Oh, yeah. Chris is out.

**Chris Gammell:** Yeah, Dave gets, Dave gets to keep the show. That's right.

**Dave Jones:** Someone bails, the other person gets the show. That's true, yeah. Yeah. Goddy. Yep. Yeah, so it's, you know, it's, yeah, it's perseverance. But as you said, yeah, perseverance does not always equal success. So, but, you know, usually, um, yes, the people who are successful have persevered. You know? Very few people get there by luck. You know, just sheer dumb luck, bang, instantly they're successful. Yeah. You know? They're, uh, usually doesn't happen.

**Chris Gammell:** I saw, I've been, you know, I read all this, uh, floofy crap that, you know, the business books and everything you don't like, right? But they, uh... Yeah, yeah, you're a big fan. Yeah. Yep. They always talk about the 10,000 hour rule. You've got, and you've got MBA written all over you, dude. I'm way, I'm way better than MBAs. Anyways, uh... Um... They, they always talk about the 10,000 hour rule, right? I mean, that was part of, uh, Malcolm Gladwell's Blink and... Right. Or outliers, rather, and he talks about that, but that's actually based on another study. And, you know, it pops up everywhere. But I saw someone talking about that recently, and they said, yeah, 10,000 hours of practice, which is roughly five years at full time, you know, like, that, that's like the, that's another thing where it's inclusive, right? Everybody who's successful has that 10,000 hours, but it's not 10,000 hours of just practice. It's 10,000 hours of the right practice. It's, you know, reviewing your design. You know, if you're doing electronics, you're reviewing your designs, going over, with people, and, you know, revising your methods. If you just keep doing the same autorouter crap layout for, you know, 10,000 hours, you can even count that as hours, right? Then, yeah, you don't, you don't improve then, right? You have to actually have some kind of feedback, and...

**Dave Jones:** Well, that's, that's the thing. Some people just, you know, no matter how long they do something, they're just not going to be good at it.

**Chris Gammell:** Right.

**Dave Jones:** Well, yeah. Some people don't have the innate ability. Right, but if you get outside... Or their brain isn't wired the right way, or whatever it is.

**Chris Gammell:** Right, or they don't seek, you know, seek training, right? Or, you know, like that kind of thing. Like, having a mentor is so important for that kind of stuff. I think. So.

**Dave Jones:** And having some natural talent, and... Because everyone's, you know, a lot of things will come down to, is it physiology of the mind, and all that sort of, you know, how your brain's wired and stuff like that?

**Chris Gammell:** Yeah.

**Dave Jones:** As I've said before, right, I could spend 50,000 hours learning to play chess, but I'm never going to beat Garry Kasparov.

**Chris Gammell:** No.

**Dave Jones:** Right? It's just not going to happen. That dude's brain is wired in a certain way that, you know, that makes him the world champ. Right, right. You know, I mean, it's just... Eh. That's what I always hate about these, you know, these success seminars. You know, oh, if you put your mind to it, you can do it, you know, all you have to... You can do anything. You can become anyone you want. Well, no, sorry, dude, you can't. You know. Like, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, if you're five foot one, you're probably not going to win high jump at the Olympics, you know what I mean? But, you know...

**Chris Gammell:** Yeah, I will not be in any heavyweight boxing matches anytime soon. Yeah.

**Dave Jones:** Exactly. Right. No, I'm not going to win Mr. Universe. Right. You know, it's just... Eh. Come on. Right. Right? There are limits to... Yeah. Yeah. But all these successful people will tell you, oh, there are no limits, you know. It's just, no, I'm sorry, the real world. That's the practical engineer in me, you know. Yeah. Yeah.

**Chris Gammell:** Well, if you find a field, though, that you like, like electronics, and it seems to work, right? You could do cool things. So, that's what we're here for. Yeah. So, like one...

**Dave Jones:** Engineers can be a downer in that respect.

**Chris Gammell:** Yeah, we'll tell you what you can't do. Can't we? Like... Immediately.

**Dave Jones:** Yeah, I'll just instantly say, well, you can't do that because blah, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** And it's, you know, and I'm usually going to be right most of the time. Yeah. At least he'll be allowed. Well, I'll usually only say that if something's obvious. Yeah. Right? Well, yeah, exactly. I'll be outspoken.

**Chris Gammell:** Yeah.

**Dave Jones:** But if something's obvious that it's not going to work because of X, then, you know, eh, that's it. You can't beat the laws of physics, Captain. Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Have we ranted on nothing?

**Chris Gammell:** Yeah, I think we've ranted. We should get back to electronics. Thanks. I saw this. There was this cool post in Hackaday last week of beer can stencils. Obviously, you wouldn't be able to... You don't drink beer, so you wouldn't be able to do this. And you don't machine stuff, so you wouldn't be able to do that either. But this guy did solder stencils out of aluminum, basically from machining out, you know, all the solder pads, and then you could use it for solder paste squeegeeing and everything.

**Dave Jones:** Out of a beer can? Yeah. But a beer can's round. Don't you have to flatten it out first?

**Chris Gammell:** Yeah, you cut the edges off and then you flatten it.

**Dave Jones:** Wouldn't you get distorted? That's one of those... Yeah, okay. Yeah, neat hack, but there's infinitely better ways to do it. Why would you do that? Cheap? Like, wouldn't you start... Fast? When you... Yeah, but wouldn't you want... Wouldn't you start with a flat sheet? Yeah, I mean... Cheat? Rather than a round can and you've got to flatten it out? It's like... Yeah. I like it.

**Chris Gammell:** I don't know. I like the machining aspect, too. I mean, if you had a laser cutter, that's... Yeah, okay, neat. If you can do a laser cutter, I think that's the way to do solder stencils. Solder paste stencils. Oh, of course.

**Dave Jones:** Yeah, yeah, yeah. But then you just get cheap sheets of mylar and bang.

**Chris Gammell:** Yeah. Do you do that for your projects? I mean... I guess you don't do assembly for your own projects, right? You usually send out for them. No, no.

**Dave Jones:** No, I hand assemble. Yeah. Yeah.

**Chris Gammell:** Yeah, I haven't done... I don't do squeegees ever. I do... Sometimes I'll do, like... You know, like a foot apply. Side paste where you'll have, like, the little air pump and the solder. Yeah, yeah. Syringe. Yep. And that's not too bad. That's... Yeah.

**Dave Jones:** Oh, yeah. Yeah, it's okay. I don't know. I think it's cool. Yeah, I just get down and solder by hand. You know, I go, hey, I've only got 50 parts. Hey, I'll just solder them by hand. You know what I mean? Yeah.

**Chris Gammell:** The Zen. The Zen sit there and listen to music and... Yeah, yeah. Crank it out. Yeah.

**Dave Jones:** That's it. So, yeah, sorry, but I think that one falls onto the neat but impractical, like, you know, why anyone would duplicate what that person did as, you know. It's just easier ways.

**Chris Gammell:** Of course, yeah. Well, necessity probably. That would be my guess. Right.

**Dave Jones:** Yeah, it's fun. Okay. Made a solder stencil out of a beer can. Great. Done. Don't do it again. You know, because it's just...

**Chris Gammell:** Let's do a chip of the week because we haven't done that in a long time. There's a new part from Maxim Integrated because they don't just call themselves Maxim anymore. Oh, God. Yeah. Yeah. But they... Is it in stock? Oh. Probably. It's not cheap. It's eight bucks per thousand. So, it's not cheap and people usually get pissed about that kind of thing. But I think it's a cool part. It's a... So, it's a power line modem. So, basically, you can... You know, you can put your data line signal on top of your mains. And... Right. Yep. But I think this is... I think they released a new one just because it's industrial grade. But, you know, it's interesting just seeing that this is getting more attention because... Right. It's been talked about. I've seen it talked about for a long time. But, you know, I still don't see many products actually putting this out on the marketplace.

**Dave Jones:** Yeah, doing... Well, because I've heard they're not hugely reliable.

**Chris Gammell:** Yeah, I'm sure if you're wiring in your house as crap, then it wouldn't be great.

**Dave Jones:** But... Yeah. Yeah. Yeah. Or you're on a different phase or you're, you know, whatever. Yeah.

**Chris Gammell:** Like different phases of the house?

**Dave Jones:** Anyway, how much stuff... Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** Or your lab or wherever you are. Yeah. How much of... How much external circuitry do you need to make a practical thing?

**Chris Gammell:** Not much. It's a...

**Dave Jones:** Because we're dealing with the mains here.

**Chris Gammell:** Right. Yeah. So, it's a transformer. So, you can actually couple to the mains, right? So, you want to be able to couple on top of the mains. So, you're not actually, you know, like, you're not just putting your circuit...

**Dave Jones:** So, you buy your $8 chip and you only need a transformer. Well, you know.

**Chris Gammell:** No, not just that. Then you also, uh... You also need a high-pass filter, right? Because you want to make sure that you're not in the same frequency range as the mains. So, not... Oh, what? They couldn't integrate the filter into the chip? Uh... Come on. Probably because of the size of the components needed, I'm guessing. Right? Because you're doing... If you're doing 60 hertz, 50 hertz stuff, it's probably going to be pretty big. Yeah, but they could have... Pretty reliable, you know. Probably don't want it blown up.

**Dave Jones:** Yeah, but they could have used external components. Yeah. What? So, you've got to actually roll your own separate high-pass filter any way you...

**Chris Gammell:** Yeah.

**Dave Jones:** ...can, I guess. Yeah. Right.

**Chris Gammell:** And then there's the chip, and then there... So, it's two chips. It's a Mac PHY, and then it's a front-end, basically. And then... Then you just plug it into your Ethernet, you know, on your... Right. So, if you have, like, a board that can do Ethernet, talk over the... What's that? The...

**Dave Jones:** Do you need a separate PHY or what?

**Chris Gammell:** Yeah, you need a separate PHY. The 20... They show the 2982, but... Right. 2198182, that's their... You know, they want to sell you both, but... I don't know. I just... I think it's cool. And I've always wanted to do this kind of stuff, you know. Like, it's a cool idea, especially if you think about... I mean, not necessarily just within your house, which would... You know, that's interesting if you wanted to try and, you know, not have to run a second set of cables all throughout your house, but... Right. Yeah, yeah. Right. But also, someone was mentioning on Reddit, too, about, you know, like, thinking about it as a last mile kind of thing, right? Because that's the expensive side of things if you're doing... You know, if you're trying to run fiber or if you're trying to get around all of the crap cable companies, right? Like, my cable company... We are talking over a very expensive, not very reliable connection right now, because my cable company's not great. So it's just another wire into your house, basically. You know, if you can... Please don't think that's practical. No, I don't.

**Dave Jones:** You don't seriously think that's practical for everyone in the street in the last mile to be hooked onto their mains to get their broadband internet?

**Chris Gammell:** It's not going to happen. Probably not. You think? Yeah, I guess not. This is only 14 megabits, so yeah, probably not. Right. Yeah. I don't know. It's just a cool technology. I like it. I think it's...

**Dave Jones:** Yeah, yeah, yeah, sure. Oh, there's lots of advanced stuff to make this work. Yeah. I mean, you know, 10 years ago, you couldn't get, you know, the thought of putting data over your power line was, you know, crazy. Yeah. Madness. Right. Hmm. Maybe 15. I don't know. But, yeah. Okay. Fair call. Yep.

**Chris Gammell:** Chip of the week. We don't do that anymore, you know? We don't do chip of the week anymore. Maybe there's a reason. Yeah. It's tough. You know, I watch a lot of the... Because when I was doing chip report and stuff, which has obviously stopped, the... You know, I watch all the product announcements, and it's tough from, like, week to week because, you know, there's interesting stuff out there, but, you know, like, watching all the different announcements and everything, it's just... You know, it's very seasonal, right? So, like, you know, three companies will come out the same type of chip at the same time. It's like, okay, cool. Another six-amp buck converter. Okay. Next. You know? Or, you know, it's just tough like that. You know, like, there's... And then there's... But then there's also just stuff that's the same... It's... They're improvements, right? So, like, there was another chip that I found that was the... An LT chip. It's a 20-bit SAR 500 ks per second converter, right? It's, like, crazy, right? That's a crazy high-resolution fast converter, right? But it's also 20-plus dollars, right? It's not cheap. Yeah, yeah. And it's not practical for 99% of the population and probably more than 99% of our show, too, right? There might be a couple...

**Chris Gammell:** A handful of people that might be able to use it. So, it's like, oh, okay, well, you know, it's interesting from the precision market, but... But that's just the chip industry in general. You know? There's so much of, you know, segmentation that until a segment gets updated, it's kind of boring.

**Dave Jones:** And in most cases, if somebody needs it, they're going to find it.

**Chris Gammell:** What do you mean? Like...

**Dave Jones:** Because that's part of engineering. Like, you know, oh, I have a requirement for this super high-end ADC. Okay, you've got to go out and search for it and you'll find it.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? It's very rare that a chip comes along that's so, you know, amazing that you go, whoa, wow, look, everyone's going to design something with this, you know?

**Chris Gammell:** Yeah, that's the thing. Like, the ones that usually catch my eye are the ones that are not standard, right? So, like, with the Powerline thing, right? It's like, I don't see many Powerline chips, so that catches my eye. Yeah, of course. Or, like... There's been more ones for, like, super isolated battery monitoring for, like, electric cars, right? Like, again, it's, like, not a market that I'm never going to buy a chip from because they price people out of it, right? You know, like, they don't want you to buy one of them. They want you to buy one million of them. So, they price you out of it, but it's still cool to see what's going on in there. And then you'll also see the technology that's in one chip, it'll start to sneak into other chips, too. So, I think it's, uh... It's worthwhile to watch, but it's tough to... It's tough to keep up with sometimes. Sometimes they just skip the notices. I'm just, alright, I'll catch you next week, guys. Oh, boy.

**Dave Jones:** Speaking of which, we've been going for an hour and ten minutes.

**Chris Gammell:** Yeah, we should probably cut it off.

**Dave Jones:** Of waffle.

**Chris Gammell:** Yeah. Uh, I did want to call out two new subreddits. So, I know, people are hot and cold on subreddits, but, uh... There's two, there's a new one for, uh, app notes, which is, okay, it's just getting started. But then also, printed circuit boards, uh, slash r slash printed circuit boards on Reddit. That actually has a lot of great content. Um, so good stuff on, you know, PCBs and everything. So, I highly recommend people check that out.

**Dave Jones:** Because that's something that everyone needs, right? Everyone needs a PCB.

**Chris Gammell:** Yeah. Until... I won't say it. Yeah. No. I'm not going to buy it. Okay. All right, well... I guess I'll see you next week. Show 150! Yeah, in the bag. Woo! Uh, feel better, man. Hope, hope you feel better next week.

**Dave Jones:** Yeah, thank you very much. I'd now have to go shoot my Teardown Tuesday. Yeah. Yay. My nasally voice.

**Chris Gammell:** Yeah.

**Dave Jones:** And I probably shouldn't appear on camera. Because I'd look like shit, you know? So... Yeah. So, yeah, if I don't sit in the chair in front of the camera and go... You should wear a mask. Don't turn it on, take it apart, you know? Do you have like a gorilla mask or anything? Right. No. Maybe I can get one of those Guy Fawkes masks. There you go. You know, those... Yeah. All right. I am anonymous.

**Chris Gammell:** Maybe you could just, uh... You could like do a voiceover for just Sagan sitting there. You know? Use him as a stand-in. Right. Yeah, yeah.

**Dave Jones:** Oh, boy.

**Chris Gammell:** All right. Well, feel better. I'll talk to you next week. All right. See ya.

**Dave Jones:** show about nothing was a very Seinfeld like show it was very Seinfeldian

**Chris Gammell:** nothing for you
