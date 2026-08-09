---
episode: 569
title: Electric Fields, Son.
url: https://theamphour.com/569-electric-fields-son/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released December 5th, 2021. Episode 569. Electric field, son.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. Which side of the fence do you sit on? Are you an energy flows outside the wire man or an energy flows inside the wire man? No fence sitting.

**Chris Gammell:** No fence sitting. I was going to say, I usually dig under the fence and you don't pay attention.

**Dave Jones:** I'm putting him on the spot.

**Chris Gammell:** I know you have, and you've been making videos about this. Yeah. I mean, does it really matter if I can turn my blender on at the end of the day?

**Dave Jones:** Well, it matters because you're a design engineer and you're an influencer.

**Chris Gammell:** Yeah, but not with that kind of power, man. Which way does the energy flow? Usually out of the AC to DC adapter in 5 volts. Okay, right. Energy doesn't flow in 5 volts, but you know what I mean. Most of this stuff, it doesn't concern me. But it was an interesting debate for sure. So people should, maybe you should explain what we're talking about here.

**Dave Jones:** Well, no. Well, it looks like you're on the side of Feynman. So you're safe. You're on the side of Richard Feynman, I suspect. Who says, meh, you don't really have to concern yourself with the details. Yeah. I mean, usually. It's, yeah. Anyway.

**Chris Gammell:** It's an abstraction in that it comes out of my wall.

**Dave Jones:** It's an abstraction. Right. Because, oh, come on. Everyone's heard about it. Veritasium, Derek Muller did a video on your misconception. The misconception about how energy is transmitted. What's the actual name? The misconception about, the big misconception about electricity. It's basically a big trolling video to us engineers. I know it's informative to Joe Public.

**Chris Gammell:** It's like physicists versus engineers.

**Dave Jones:** It's physicists versus engineers. It's the electro boom versus Walter Lewin thing all over again. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And Kirchhoff's voltage law thing. But the bottom line is he actually proposed this experiment. Well, no. No. Actually, I'll tell you the thing for those who haven't heard it. He basically is talking about how energy flows outside the wires in the electromagnetic field. In the wires. The actual energy. The actual energy. I.e. power. Because energy is power over time. The actual energy does not flow in the copper itself. It flows outside in the electromagnetic fields. And that's backed up by the physics of Maxwell and pointing as well about the pointing vectors. You know, anyone who studied engineering is, you know, no doubt being slapped over the head with this kind of stuff. And the bottom line is he's not wrong. Right. From a physics standpoint, this seems to be the correct interpretation of how energy actually flows. We're not talking about electron drift and all that sort of stuff. Right. We're talking about the actual flow of energy. Where does it flow? Inside the wire or outside? And Maxwell and pointing theorems say it's outside.

**Chris Gammell:** Right. And I guess to make a very simple case of all this stuff, not a simple case of this stuff, rather, but like in a similar scenario, like, you know, people always say like, oh, current is opposite to electron flow. And I'm like, well, I don't care. Does it help me get my job done faster? You know, like, can I calculate the current leaking into the input of a high impedance op amp input? It's like, if I can do that, that's all I really care about. You know, like, let me measure the physical phenomenon. Now, yeah, there's math behind it for sure. And it's, you know, so in the case of current, it's different. It's opposite of electron flow the same way. But, okay. So the example he's giving, though, one of the examples he was showing the, yeah.

**Dave Jones:** The big question, the example, you've got wires half a light year, half a light second in each direction. So 300,000 kilometers in each direction. You've got a simple circuit, like a battery and a light bulb and a switch. Right. But it goes, but the loops go half a light second in each, each direction. Right. So in theory, it should take like, you know, like a second for this light bulb to light up.

**Chris Gammell:** If you were a photon traveling along the outside of that wire, it would take you one second to go out and back.

**Dave Jones:** Right. But of course it doesn't. The answer is it lights up and they're only a meter apart. They're only a meter apart. So the answer is, and it was tricky with the answer too. And I think it was deliberate. And the answer is it happens in one meter on C seconds because it jumps across the one meter gap. It jumped and it can drop, jump across the one meter gap in three ways. Because when you flick that switch, you're going into a transient mode. So you have to do transient mode analysis as us engineers call it, as these physicists don't know about this sort of stuff. You know, this is the domain of engineering. You have to do transient mode analysis. When you do transient mode analysis, these wires act as transmission lines and they've got inductance, they've got capacitance, and they've got resistance. Right. But he assumes that there's zero resistance. So you take that out. But even then, yeah, the fact that you've got capacitance between these wires, no matter how small, it will jump across. Right. The electric field will jump across and it jumps across in the time it takes to traverse that one meter gap. And then, but you can look at this three way. You can actually analyze these three ways. I analyzed it using like the cable capacitance method because I've done a couple of videos on this. One's on my second channel. I'm talking about the simulation side of it. So I did. So I did. Because I think that's the easiest explanation. There's capacitance, but between these two wires and everyone knows that as soon as you flick on a switch, a capacitor is a short circuit. Right. That's how us engineers analyze this for practical purposes. Yeah. We've done it for ourselves. Yeah. Yeah. So it jumps across to the light bulb in quote marks, the ideal light bulb that lights up instantly with one electron, you know. Right. So it jumps across that one meter. So it doesn't. So when you flick on switch, the energy does not have to flow all the way out 300,000 kilometers and along the wires and back. It can jump over the gap. And there's three ways it can do it. One is the capacitance. The other, you can model this as a transformer. Right. Because you've got a wire, you know, you've got two wires. Right. With a current flowing. And right.

**Chris Gammell:** It's a heck of an air gap. Yeah.

**Dave Jones:** It's a heck of a, it's a pretty piss poor transformer. Let's put it that way. And the other one is you can model it. It's a dipole antenna. Right. So you, so you've got the photons jumping off the antenna and blah, blah, blah, blah, blah, blah. Right. So there's, there's several different ways from an engineering perspective. You can analyze this, but physicists, it's all the pointing vectors and you know, blah, blah, blah. So anyway, it's a trick trolling question and he knows it, but he's not wrong in the answer. Technically. I don't think. Yeah. Anyway. So what was it? Have you actually watched the video? What was your.

**Chris Gammell:** I watched the video. I knew it was going to make people upset and I moved on.

**Dave Jones:** And you moved on and didn't get involved.

**Chris Gammell:** Yeah. Well, you know, I had work to do. So. Right. Okay. Yeah. You know what I would do is if I had, if I had someone who wired up that circuit, I'd have two things. One, I'd say, you just wasted a whole shitload of wire. Yeah. Yeah. That's. I would flip the switch and then I'd, you know, measure it, I guess. You know, get a high speed camera or I don't know.

**Dave Jones:** He actually said that if anyone questions him, maybe he could set up like a big experiment in a desert or something like that. It's like, good luck with that. And meet a gap. You know, you would have to go down, you know, like, yeah, it's yeah. It's going to be pretty hard at a meter. I think to see any real effect on this.

**Chris Gammell:** It definitely makes people think it, you know, showcases. Oh, there's so many spin off videos. Oh yeah. Yeah, exactly. Right. So many people are talking about it. Right. As a science communicator, if nothing else, he has succeeded.

**Dave Jones:** He won. He won spectacularly. I think it's got 7 million views and it's born like 50 different response videos from every engineering YouTuber and science YouTuber on the planet, you know? So yep. Guilty as charged because so many people asked for it. Like I couldn't not do it. I mean, it was, you know, I was being swamped with emails and messages of Dave, have you seen this? Can you comment? Can you comment? Right, right, right.

**Chris Gammell:** You're saying the same thing. You know, you're, I've said I have, I had work to do. And then you said you also had work to do. And that's just, that's the work you do now, Dave.

**Dave Jones:** Well, on my, on my second channel, I've actually, I, I snipped this out of my live show from a couple of weeks ago. I had not seen his video. I'd not heard about it. And somebody mentioned it in my live show chat. So I show my reaction to just like hearing about it. And the instant I heard about it, my mind, like I, I didn't even know the title of it. I didn't even know what it was about, but the way people were explaining it, like, you know, explain it to me, my mind instantly jumped to. Uh-huh. I think he's talking about energy in the fields. And yeah, this is a real thing because it is a real thing when you start talking transmission lines, right? When you start talking high speed PCB transmission lines, like the energy flows in the dielectric. It's a big, you know, it's, it's like a real thing that you have to take into account. This isn't just obscure physics crap. Right. Sure. It's, um, you know, it's, you really do have to care about this sort of stuff once you get into the high end engineering side of things. But yeah.

**Chris Gammell:** Yeah. I mean, I think one of the things is one of the things that happens is like, it kind of, it gets abstracted away, especially for people like, you know, we have these mental models we have to go and amend over time. Right. And one of my concerns is always like, is if you, if you lay that on someone and you say to them like, well, energy travels in the fields and that means it's actually going through the dielectric. And it's like so hard to comprehend at the beginning that they just throw their hands up and leave. Exactly.

**Dave Jones:** Yep.

**Chris Gammell:** Maybe we visualize this as a wire on the top of a surface and it's going real slow. And it's like, you know, it's like a wavy thing. Like, and it's just like, I don't know, there, there is that aspect as well. And I think a lot of people who are into the pure physics and the math of it, they're like, well, you just got to work through it. And it's like, okay, that's great. But we're trying to keep more people. We're trying to keep people here, you know? I don't know.

**Dave Jones:** This is where the rubber meets, hits the road with engineering, with practical engineering, right? At the end of the day, engineering is a practical science, right? You've got it. This is why we've developed the tools and the methods. Like we, we, we don't use Mac. What engineer uses fricking Maxwell's equations and pointing vectors? Nobody. Right. This is why Ohm's laws, Ohm's law was developed. The power transfer theorem and, and Kirchhoff's voltage and current laws and all the other like tools we use in our tool set.

**Chris Gammell:** It's all just, it's all just dressing up Maxwell over and over again. Yeah. Yeah. Right. Okay. Yeah.

**Dave Jones:** You can go back to the fundamental physics, but there's, for most practical purposes in engineering, there's just no point, you know, even, so even the famous Richard Feynman says this, right? Richard Feynman in his famous lecture notes, which I put in my video, he says, yeah, well, this seems to be true about when he's, you know, he's talking about the pointing vectors and energy flowing outside the wire and stuff. He goes, you know, you can be forgiven for not caring, but basically to, um, to be good.

**Chris Gammell:** Dick said it's cool. It's cool with me.

**Dave Jones:** Yep. Paraphrase Feynman. Yep. So yeah, yeah. I think that's, yeah. If it's good enough for Feynman, it's good enough for me. Yeah. Yeah. Yep. Totally agree. I don't like to, you know, name, name drop and, you know, by authority, you know, I don't want to do by authority, but you know, Richard Feynman's held him pretty high as Steve. Right. So yeah. Oh boy. Anyway, what a troll. Speaking of which you put in here a, a video, which I have not watched yet, but I will watch this at lunchtime today while I'm eating my sandwich. I will watch, uh, how electricity gets to you.

**Chris Gammell:** Yeah. Yeah. This is great.

**Dave Jones:** So you, you've obviously watched it. I have not. So it's, yep.

**Chris Gammell:** You know, my lunchtime time is before your lunchtime and your lunchtime is before my next lunchtime. Yeah. No, this is a great one. This is from, uh, I'm loading it up and forgetting my name. Wendover Productions. Wendover. Yeah. Wendover Productions. Amazing.

**Dave Jones:** I do like these videos.

**Chris Gammell:** But they show all of the different, you know, energy sources. So like the steady nuclear coal, that sort of thing. And then like peak power and stuff like that.

**Dave Jones:** There is no physics in this, right? I, I sort of briefly just skipped through and I don't think this is a.

**Chris Gammell:** No, I don't think so. No, this is more about practical, like how it's delivered.

**Speaker ?:** This is practical.

**Chris Gammell:** How does it. Right. Showing all the different, uh, step down voltages at various levels and, uh, transfer. And then like energy storage. One thing that he didn't bring up in there, which I'm, I'm kind of, that I was thinking about as I was watching this thing is like, so he talks about like, uh, so he's focusing on Colorado and basically they have, when they have excess generation, they do that thing where they pump water up a hill, upper reservoir, and then they pull it back down as they, they need it throughout the day, which is fantastic as assuming you can, you know, if you have

**Dave Jones:** the geology to do it. Yeah.

**Chris Gammell:** That's right. Yeah. Exactly.

**Dave Jones:** Geography to do it. Yeah.

**Chris Gammell:** And, uh, Colorado most definitely has elevation. Yeah. Yeah.

**Dave Jones:** Exactly.

**Chris Gammell:** But I was thinking about another version of that, which would be, which I'm not a huge fan of overall, but it could work where you could basically, you could do like compute cycles, right? You could do like low, you could like bunch batch all of your compute. Bitcoin mining. Just put all your Bitcoin mining. That's right. Yeah. Your excess power. Well, and you could do it just at night. I mean, when it's cheap, that sort of thing. Yeah. Yeah. Of course. And then that would help level out loads and stuff like that. And, yep. And then, you know, as need really gets there, we can completely discontinue Bitcoin and all crypto and go back to the old ways. Uh, but I think I'm going to lose that battle. Not going to happen, dude. Yep. You're going to lose that. I know. I know. That, that, that, that cat's never going back in that bag. Uh, but yeah, just that kind of idea of like compute, like as a consumer, instead of like storage of energy, basically you just have variable consumer levels. But, uh, yeah, maybe that's a bad idea too.

**Dave Jones:** Well, they're doing that with.

**Chris Gammell:** Waste a lot of energy.

**Dave Jones:** Electric cars. They're, they're actually doing that there. Like, um, I, I actually signed up for a trial to get a, um, one of these smart fast charger things where, you know, they'll, they'll doing the government's doing this experiment where yeah, to actually time and stagger. So the idea is you come home at night and you plug in your EV, right. And then you, and then it, it's centrally controlled so that it'll charge you. Uh, so that'll charge you like so that everyone doesn't charge their car at once and the grid falls over. Right. It's good. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. And that is one of the points that, uh, Wendover's making as well is that like, you know, all power, when you flip a switch, it's being requested from an actual, like it's, you know, it's drawing it off the grid, but it's like, it's being generated somewhere at the exact same time to backfill that energy in the fields.

**Dave Jones:** Did he go into power factor at all? Did he mention, did he mention that? He does not mention that. I thought that was, would be a bit too much for the, yeah, this is a higher level type thing.

**Chris Gammell:** So this is more about like sources and, you know, and then like various types of energy and pollution levels and stuff like that too.

**Dave Jones:** So, yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. It's, it's absolutely fascinating. For those who don't know, the world's largest structure is our grid. Like massive orders of magnitude. It's just, it's such a massive infrastructure. People just, I think just take for granted. It just works. You know, you turn on your switch and your power's there, but.

**Chris Gammell:** As, as both a homeowner and a recent parent, I can tell people definitively, turn off the lights when you leave the goddamn room. Yep. Were you born in a barn? Do they have that phrase? Do they say it in Australia?

**Dave Jones:** Uh, tent.

**Chris Gammell:** Oh, really? Oh, interesting. Ah, were you born in a tent?

**Dave Jones:** You're born in a tent. I say it to Mrs. EEV blog all the time, you know, born in a tent. That's funny. You know, you're born in a tent, you know, yeah. Leaving the doors open. You know?

**Chris Gammell:** Yeah. Yeah. No, here it's, here it's barn. Okay. Born in a barn. Born in a barn. Yep. Culture. Learning. Yeah. Yeah. No, it's a, that was a great, it's a interesting thing about that stuff. I'm not sure there's much else to learn from that. No. You know, Wendover is a fantastic channel.

**Dave Jones:** Yeah. It's a great channel. And it's an absolutely fascinating topic. If you, if you just, just go searching for like, I think we've mentioned on here before tours, like there's videos that like tours of, of power substations. They're just absolutely fascinating.

**Chris Gammell:** That's right. You know? Yeah. That's switching. One of the things they mentioned in the video is high voltage DC and how that's, apparently there's a link from Portland down to LA. And so like hydro in Portland will power LA air conditioners in the summer. And they said the other direction for heaters.

**Dave Jones:** Okay.

**Chris Gammell:** So I was actually thinking about this in context of like the, so if you're doing high voltage DC, does that mean you actually are pushing the electrons then? Or is it like electrons pushing out their electrons? You know what I mean?

**Dave Jones:** That's the argument when you reach DC steady state. See? And you remember how I was talking about transient analysis before sooner or later, like a couple of seconds later, you reach DC steady state and then all bets are off. But according to Feynman, it's according to, yeah, both Feynman and Pointing and Maxwell, it still flows outside the wire, but, oh, there's less, there's even less, if you didn't think there was a reason to worry about it before, there's even less reason to worry about it during DC steady state. In my opinion, in my humble opinion. So yeah. So yeah, the arguments sort of start going away in DC steady state, but technically.

**Chris Gammell:** I mean, at these high voltage DC levels, right? So I think I've seen like up to a million volts DC.

**Dave Jones:** Yes. On these overseas transmission lines. Yeah.

**Chris Gammell:** Because I used to catch this stuff from like, when I was working at ABB, they'd be talking about this stuff all the time. And I honestly, I just don't understand it. This is a video for you to make. I don't understand how the hell that works. Dude, I've made a video for everything.

**Dave Jones:** Hang on. EV blog to DC transmission. The world's largest solar.

**Chris Gammell:** Here it is. This guy just doesn't stop talking folks. I just, he just talks about everything.

**Dave Jones:** I don't stop talking. There it is. Second channel video. A couple of years ago, I did a run in the numbers on a high voltage DC transmission line, which is going from Australia to I think Singapore. Was it something like that? Anyway. Yeah. In the, so yeah. Cause we were going to put this huge solar farm here in Australia. Cause you know, it's the outback and we have lots of sun and lots of room. So we're going to install this huge solar array. And then we're going to export the energy overseas and it's 3,800 kilometers away. So we're going to export at 3,800 kilometers. Yes. To Singapore. Yes. We're going to transport it to Singapore. So, so all that, so this, a solar array in Australia was going to power Singapore. I don't know how much, but it was a good percentage of Singapore's power, like half their power or something. Yeah. And I just ran the numbers on that and it's absolutely fascinating. So go on, go on.

**Chris Gammell:** Was it at a million? I mean, like.

**Dave Jones:** Uh, it's, I can't remember. Was it at a million volts? I can't remember. It was, I think it's pretty close. It's, uh, I do know it's 2,420 amps by my notes here. No, 500 KV. I was assuming 500 KV.

**Chris Gammell:** Cause I, I know that some of them have been moving up to a million volts.

**Dave Jones:** Up to a million. So yeah, I realized. Yeah. Yep.

**Chris Gammell:** So that's still 1200 amps then. That's pretty beefy. I mean, that's like. Yeah.

**Dave Jones:** Oh yeah, exactly.

**Chris Gammell:** It's not small. It's not small cabling.

**Dave Jones:** No, it's a big deal. But yeah, apparently I think I ended up calculating like a 10% loss or something, which, you know, is significant, but it's not a showstopper. Right. So, you know. Yeah. Yeah.

**Chris Gammell:** Yep. Well, I mean, having stepped down transformers in the middle of the ocean would probably also be problematic. Like, ah, yeah, nah, not going to happen. Yeah.

**Dave Jones:** Oh boy. Anyway. Yeah. Cool. And for those, um, I get, you know, these questions all the time as you might as well being an engineering educator. No, no, no. I'm sure you have, you know, engineering students are going, oh, what field should I get into? What speciality should I get into?

**Chris Gammell:** Electric fields, son.

**Dave Jones:** Electric fields. Oh, I'll pay that. I'll pay that. And, um, oh boy. And electric fields outside of your industry. That's right.

**Chris Gammell:** Right, right, right, right.

**Dave Jones:** Anyway. Yeah. No, power. Power is if you want the, uh, filthy lucra, you know, if you want the, uh, if you want the filthy bucks, you know, if you want the high pain.

**Chris Gammell:** The big dollary dues.

**Dave Jones:** The big, big kahunas. Get into power. Get into power transmission and stuff like that. I think you'll find. Yeah. I don't know.

**Chris Gammell:** I mean, it's exciting when you see your coworker fried. Right. Thanks for that. Not the good kind of exciting, you know. Yeah. Right. Oh yeah. Yeah.

**Dave Jones:** Yeah. But no, there's like, and that can be fascinating to a lot of people. So it, I'm not saying go into it because of the money. I mean, I, you should definitely go into whatever you find the most.

**Chris Gammell:** Go into what you're interested in and there'll also be money.

**Dave Jones:** And there'll also be money. If that's the case, if you find power transmission interesting, go watch a bunch of YouTube videos on it and you'll find that. Oh yeah. That's fascinating. I'd love to work in that. And there's big bucks in it and there's lots of jobs. So yeah. Yeah. Yep. Yep.

**Chris Gammell:** What's Andy's channel? I forget. Zappy Zappy.

**Dave Jones:** Andy.

**Chris Gammell:** Andy the Brit. Yeah.

**Dave Jones:** Oh, come on. Until I get it.

**Chris Gammell:** Photonic induction. Photonic induction. There it is.

**Dave Jones:** Oh my God.

**Chris Gammell:** Yeah. Yeah. Watch that. Watch that.

**Dave Jones:** Thank you. Oh boy. Yeah. Watch photonic induction. Good fun. He enjoys his craft.

**Chris Gammell:** Yeah. That's true.

**Dave Jones:** There's a man who enjoys his hobby. And that's his line of work too. It's not just his hobby. He's in that sort of stuff. Maybe we can get him on the show sometime. He can talk about it. Yeah. Yeah. Yeah. That'd be cool. Anyway. Yeah. Power transmission. And YouTube arguments. I just got into another YouTube argument. It's YouTube drama all the way this week.

**Chris Gammell:** Not for me. But go ahead. No. It's the EV. No, I know what you're talking about. I think actually I am on your side on this one.

**Dave Jones:** Oh, excellent. Excellent. It's the electric buses. Electric buses. Adam something. Another YouTube channel. I think he's got like five, 600,000 subscribers or something. And he said electric buses are basically a scam. They're not practical and they won't happen. And well, no, he's completely wrong. And I did a 30 minute response video saying why he's wrong. And yeah, no, sorry. Yeah, it's happening. Yep. There's some people in the comments who have said, like, cause I use that in the, I use that in the video, not as an argument, but a lot of people took it as an argument. And I said, well, it's happening whether you like it or not. Right. And that wasn't meant to be an argument. Cause I go into a whole ton of arguments. Right. That was just meant to be something that he didn't admit to that. Like he admit to, no, it's not practical. They're only making a couple of these and it's just, no, it's a scam. It's just a, you know, a PR gimmick, you know, and the, the, the usual stuff like that. And no, it's not. It's like countries, entire cities, my, even Sydney here, we're going a hundred percent fully electric bus fleet. And this is not pie in the sky that they just ordered another. They just put another 40 on the roads last month, I think. And they go into a hundred percent fleet and they're not doing it for no, no reason. There's very good reasons that they're doing it. Very good economic reasons, which he said, no, it doesn't. It's more cost effective to stick with diesel or go to a trolley buses, which is the overhead wire thing.

**Chris Gammell:** Yeah. I thought the diesel thing is way off. I think the, the wires. Yeah. I mean, it's basically the same thing. It's basically AC versus DC at that point. Right. I mean, it's, you got AC wires up above and you're doing that, but then infrastructure cost wise. I mean, I wouldn't know what the difference.

**Dave Jones:** Oh, it's huge. The, the, well, I've, I've got numbers in the video. I found some, well, just maintenance numbers. This didn't include, this is just to maintain the overhead wire grid. It was like almost, it was like 15 times. It was no, no, two orders, almost two orders of magnitude more than just electric buses. Cause there's zero maintenance costs. Cause it's the existing roads, right? There's, there's just nothing right. Which have to be the existing roads have to be maintained anyway.

**Chris Gammell:** Right. You centralize all your, all your infrastructure at the charging stations then.

**Dave Jones:** Right. Yes, exactly. So no, no, he's wrong. So he'll, I'm sure he'll do a response video picking apart my video. And it's like, maybe I'll do another response video. And we'll do some ping pong maybe, but I know he's not, not that's that ain't a thing.

**Chris Gammell:** Yep. Yep. Yep.

**Dave Jones:** Can we follow the YouTube theme this episode? Because it's, I put, I don't know if you've seen it where, and I put it in here somewhere. Insane changes at Linus Tech. Nobody thumbs it up. Nobody wants me to talk about it. I want to talk about it. Cause I think it's interesting. Insane changes at Linus Tech Tips.

**Chris Gammell:** What do you think is interesting about it? So this is a, Linus Tech Tips is a long time. YouTube channel. He does a lot of tech reviews and stuff like that.

**Dave Jones:** It's all, it's all PC tech review stuff, right? That's right. It's basically almost all PCs, isn't it? I think it's almost all PC related.

**Chris Gammell:** I think phones as well.

**Dave Jones:** Oh, phones as well. Okay. Right. Yeah. I don't watch it. You know, I'm not really a regular viewer. Just if, you know, something interesting pops up and people point me to it, I'll watch it. And yeah, I thought that they had already expanded to insane levels, but I was wrong. And they're only just getting started. Right. Cause he's got like 20, 30 employees or something. And he's got like four editors and they shoot with like high end 8K, you know, $100,000 red cameras that, you know, like it's just like, and they've built all this service. They've got their float plane system to host their own content. And, you know, it's like, it's just crazy level for just what they, you know, for the kind of stuff they're doing. But if that's what they want to do and they're making a, they're making money from it, they're employing people and they're making a profit. Great. You know, fantastic. But what he's doing now is he's, I think bought a gigantic new place. I assume he's bought it. Anyway, it doesn't matter. This gigantic new place. And what he's saying is basically what it's going to be is a state of the art lab, a state of the art test lab. And he's going to hire not just tech people, he's hiring real engineers, like, you know, top grade engineers to actually, they're going to install all sorts of test gear from RF and echoic chambers to acoustic chambers. To, you know, a power supply, you know, full on testing. And, you know, almost anything you can think of. Right. He wants to install not only the testing infrastructure to do it at any cost. Basically, he's basically, he showed a blank check on their thing. Right. I've got this blank check. And if you think I can't afford you, try me is his own words. He's talking to engineers here. Right. He's talking. If you're like the best engineer out there at testing power supplies, I want you. Right. And I'll pay anything to get you. And it's just, I don't know what to think. It's just on one hand, I'm blown away. On the other hand, I go, well, what is kind of the point of all, like, it's just PC review stuff. Yet they go into such intricate detail on everything. But I guess that's the audience, right? The audience who buy their $2,000 video card care about, oh, this thing does it two cycles quicker than this one. So I'm going to pay an extra two grand for that. You know, it's like, that's the kind of audience. They're so caught up in the absolute minute details. If you think engineers care about power supplies, right? No. Go over to the PC world. Go online. And they're arguing over the brands of the capacitors and the type of layout and the power transistors used in their PC power supplies. Right? They're like that insane level. These gamer PC people, they're just, wow.

**Chris Gammell:** They're a new level of extreme. Yeah, but I always kind of felt that was more like the audio file community more than. I didn't feel like there was actually any real analysis behind it so much as like specksmanship behind it, you know?

**Dave Jones:** Well, that's what he wants to do. He wants to quantify it all. He just doesn't want to do hand wavy testing. He wants to actually quantify that, yes, this SATA cable is better than this one because of the signal integrity. Look, I can push it to four, you know, 10 gig or something as opposed to eight on this one and check out the eye diagram on this sucker, right? He wants to quantify all this stuff. And that's the interesting part of how he's expanding here. It's a big quantification lab. Is that a word? Quantification lab? I don't know. It's a big lab where they measure shit, basically, right? And like do it and automate all the testing so that they can test like, you know, 20 different power supplies and like and automate the entire testing and everything. It's phenomenal what he wants to do. It's just, it's crazy level, but in a good way. Yeah, I just, I don't know how he's going to pay for it, you know? Well, sponsorship and merch.

**Chris Gammell:** Yeah.

**Dave Jones:** He says merch is a big part of it and he's expanding the merch part and department. He's like hiring like 50 to 100 people or something. I'd know the list is huge of people that he wants to hire for just this testing lab. It's just crazy. So, yeah, well, hats off to him because that's just nuts. And this spurred me to think about and I posted this on my YouTube community channel. You laugh away. Anyway.

**Chris Gammell:** I'm just imagining you being like, I'm going to hire someone again. I'm going to hire someone again.

**Dave Jones:** Thought did cross my mind. Anyway, we'll talk about that in a second. I've got my new 30 square meter dungeon downstairs, right? Whopping 30 square meters. So, I thought what sort of cool test, like big test gear can I put in there that would make for cool videos? Not something that sucks my life away like a pick and place machine, please, please. But no, no, I'm talking like a real proper big thermal chamber, like a big vibration test rig, which is actually today's video. We can talk about that. I'm about to edit it after this. Did some vibration testing, which was cool. And, you know, a vibration test cable, maybe an acoustic test chamber to measure fan noise, right? Like, you know, maybe a little mini far field RFI testing thing, you know?

**Chris Gammell:** Sure. That'd be good. Stuff like this.

**Dave Jones:** If anyone's got any ideas of, you know, what stuff I can...

**Chris Gammell:** I think one thing that happens with a lot of the testing stuff is like, you know, there's a lot of expertise at the testing houses, obviously. And there's a lot of expertise in longtime engineers who have had to go through it a bunch. Yep. But then like there's maybe some consulting people that are willing to offer you training, that sort of stuff. But it's just like, it's such niche knowledge. Oh, yeah. Yep. Yeah. It's not like, there's not a ton of stuff out there. Like, here's how you always pass your EMI tests and stuff like that. It's more like, sign up for my training and I'll teach you how to customize your design. Yeah. You know, that sort of thing. It's like, okay. I mean, that's valuable. It's worth it to do that sort of thing. But it's not normally on YouTube, as far as I could tell.

**Dave Jones:** There's not much out there. There is some. But I've done some videos on it. I've done some videos on conducted mode, emissions and stuff like that.

**Chris Gammell:** Right. Yeah. But it wasn't in a lab, was it?

**Dave Jones:** No, no, no, no. It's not. It's not. This is a real calibrated measurement that's going to match one that's going to be in an EMC lab. Yeah.

**Chris Gammell:** I mean, I want to see like, you know, like a reading, you didn't have Reading Rainbow there, I'm sure. But, you know, like a Reading Rainbow episode where they go to a testing lab and they do a test. Right. That's what I want. Yep. I want LeVar Burton to be there.

**Dave Jones:** I have visited a lab. I have done a video visiting test lab. But it was basically a tour. It wasn't, right, we're going to test something. Here's all the steps in testing this product in this lab, you know. So, yeah.

**Chris Gammell:** Yeah. I want to like basically follow along as an engineering team goes through it. You know. Yep. I want the mockumentary of the test lab.

**Dave Jones:** So, it also did get me thinking, as you mentioned, like hire someone. It did get me thinking again. Not that, you know, it always gets, this sort of stuff always gets me thinking. You do not want to do that again. No, I'm just wondering if there is a market out there for this Linus Tech Tips sort of idea. But in the test equipment space, like would people actually want to see like a proper lab setup and somebody whose job is to thoroughly evaluate and test all the new test gear that comes on the market?

**Chris Gammell:** Maybe. I think one of the things that always comes back to for me is like you need to first define all of the product categories.

**Dave Jones:** Oh, yeah.

**Chris Gammell:** Having worked at a test equipment company, let me tell you. Yeah, yeah. Right. There's nothing that a product marketer loves more at a test equipment company than making their own category for a thing so that nothing compares to it. And it's like, okay. So, then the job of an external group is to be like, all right, well, how do we compare these things? And, oh, well, this one's specced it like this. Yep. And this one's specced it like that. And, you know, the chip companies do it too. And it's just like, okay, well, can we just agree on a single standard? And the answer is no. They never, ever will. No, of course not.

**Dave Jones:** No, no, no.

**Chris Gammell:** At least on the chip side, it'll all be taken care of when it's just down to a single chip company.

**Dave Jones:** Right. As it inevitably will be. Oh, yeah. We're down that path. We're on that path. But, yeah, is there, I don't know. Please leave it in the comments down below if you think there's a market out there. Obviously, like this is not something, if you wanted to take it seriously, like you have to have a full-time person. You've got to have a full-time lab. You know, you can't just dick around. And you would have to get sponsors to pay for it.

**Chris Gammell:** Yeah. I mean, that's the thing. Like, and I'm like, how do you make it interesting too? Right? I mean, like that's. Yeah, yeah, yeah. Exactly. I don't know how Linus and crew make that stuff interesting in the first place. But, like, you know, when there's always some subjective nature to, like, when I think about, like, a lot of the tech reviews that's out there. Usually there's personalities and there's, like, you know, they're like, oh, well, this one feels like this. And this one's.

**Dave Jones:** Yeah. It's also in the editing as well. This is why they have half a dozen video edits. Sure, of course. Right? Is because it is to make the polished content, you know, is to get it down to exactly what they need.

**Chris Gammell:** So if you really wanted to do it right with doing, like, comparing, say, like, five different mid-tier scopes. Scopes, right. You do similar kind of testing that you would. Like, anyone who's doing an evaluation when they get a bunch of budget at the beginning of the year, right? So people are probably coming up on this in corporations right now. And it's like, okay, you want to see, like, comparisons of five different scopes with the exact same test. That's great. You want to see that data. But, boy, that'd be boring to run and to work, to watch, you know. No, no, no.

**Dave Jones:** That's why you have to edit it down to a 15-minute video, right? It's got to be like a 15-minute summary, right? It's got to be edited down.

**Chris Gammell:** Not even that. I mean, I just mean if all you're doing is comparing five things, it's like, ooh, look, this one is 4% better.

**Dave Jones:** Well, if that turns out to be the case. But then you can, of course, the interesting stuff comes in the problems that you have, right? Some of my most popular videos have been, oh, this scope is shit. Because, well, it's not shit, but check out this bug I found. Like, this is shocking. You know, this is like, you know, it's nuts.

**Chris Gammell:** Right. But what happens when you stop finding that, right?

**Dave Jones:** And you stop finding that and they're all very similar. It's like, man.

**Chris Gammell:** These five scopes are pretty good.

**Dave Jones:** I know.

**Chris Gammell:** 8.8. All of them out of 10.

**Dave Jones:** 8.8. Well, judging by the popularity of test equipment on the EEV blog forum, I'd say there's a big market out there of people arguing over this shit, right? Yeah, yeah, yeah. That's what people are arguing. Whether or not it translates into views and can translate into, I don't know, somehow you've got to pay for it all, right? It's like, it's not something that I can do on my own, right?

**Chris Gammell:** No, I think it's like- It's just not.

**Dave Jones:** You've got to have-

**Chris Gammell:** It's not a YouTube channel. It's a consumer report service, right? Where you have-

**Dave Jones:** Yeah, it's a consumer report service. Or it's like-

**Chris Gammell:** You know what you should do? You should start an award ceremony. Here's what you should do. You should start an award ceremony and have a big to-do every year. Yep, yep. Best new scope. Best new scope, yep. Most improved scope firmware. Industry award, you know. That's right. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** Oh, boy. I don't know.

**Chris Gammell:** Terrible industry to be in.

**Dave Jones:** Yeah. Yep. Well, I do have, you know, a couple of products, a couple of name brands over the years have won the EEV blog retarded product of the year award, right? So, you know.

**Chris Gammell:** I don't use that word, Dave. Okay.

**Dave Jones:** Come on. You know.

**Chris Gammell:** Yeah. So, I could see going the other direction, the Darwin awards of products, that sort of thing.

**Dave Jones:** Yeah, but that's, you know, but then it's got to blow up.

**Chris Gammell:** That's true. That's true. It would have to blow up.

**Dave Jones:** You know, it's got to, you know, which has happened, but, you know. Sure. It's not, you can't make a channel over it.

**Chris Gammell:** Most of those don't get to market. Yeah. Or they shouldn't be getting to market.

**Dave Jones:** Yeah. Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Hmm.

**Chris Gammell:** I don't know. I mean, these are the things that happen is, you know, like, we all go through our careers. Things change. Things get normalized over time. I'm trying to work my way towards hardware engineering at 40 plus. This is what I'm trying to work towards in a segue.

**Dave Jones:** Right. Okay. It didn't really work. But Dave, you're over 40. Well, so the rumor goes, yeah.

**Chris Gammell:** Yeah. And I'm getting pretty close myself here. This was actually a post that was on Hacker News, which is a lot of software people, right? A lot of startup-y software people. And reading some of that stuff is insane to me.

**Dave Jones:** Is this on the list?

**Chris Gammell:** It is on the list.

**Dave Jones:** Oh, hardware engineering 40 plus. Yes, I missed it. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. So there's an associated Hacker News article. Just basically about, like, as you move up in the software world, right? You don't necessarily lose your edge, but there's definitely some ageism in there. And there's also, like, you might not be attuned to the newest, hottest software. You might be in a niche or something like that. And so they're talking about, like, well, yeah, you want to be a software engineer 40 plus, you better have tempered expectations. And so what I was wondering is, like, that doesn't really exist in hardware. I mean, like, not that there's not ageism in the electronics industry. There totally is, I'm sure, as well. But, like, just how that maps to hardware engineering as well. Like, is it possible to be the grizzled old gray beard? And do they get kind of stuck in the corner? Or can they still have, like, a...

**Dave Jones:** Are they talking about, like, changing? Like, changing, not changing careers, but changing focus in their career? What are they... Or are they talking about just actually getting a job?

**Chris Gammell:** They're talking about, I think, moving up in a job, really. So, like, they're already... Moving up, okay. Well... Yeah, they're already 40 plus. Maybe they want to move latterly. So, like, in this case, again, they're talking big, you know, Fang-type companies, manga-type companies, whatever you're calling it. Fang-type? Apples. What? Oh, so Fang traditionally was Facebook, Apple, Amazon, Netflix, and Google. Oh, right. And now the joke is that it became either ma, if Google becomes alphabet and Facebook becomes meta or manga. Oh, please. No. If you just change Facebook, yeah, it's stupid. No. No. But anyways, it's these very, very high-paid software engineering roles. That's what it really comes down to at these monolith software companies. So, yeah, I mean, it's just interesting kind of comparing because it doesn't... From my perspective, like, I've worked with many older hardware engineers who they're actually lauded for having that much experience. You know, it's like you basically... Yeah, of course. Yeah, yeah. You've seen a lot of it. Maybe, you know, maybe you're grumpy and you're not going to be designing the next, you know, Wi-Fi 6 widget or something like that. Or you might not be doing like the 24-layer board design or something if there's... Or maybe you are. I don't know. Like, you know, like just kind of where experience in the electronics industry helps or hurts. It seems like in the software industry, it hurts sometimes, which is interesting to me.

**Dave Jones:** Like, if you want to do something like, you know, all the interesting things that happen in startups, right? For example, well, that's how that's the promise, right?

**Chris Gammell:** Is this the software world or the hardware world? Or both?

**Dave Jones:** Both. You can say both, right? So would... Is it common? I don't know enough about the startup world. Is it common to get the old greybeards into a startup company? It doesn't seem to be the case. Like, you might get them on the board or something like that. You know, they might get them on the advisory board or something. But I don't see... I can't say I've noticed startups like hiring. Oh, yeah, we've hired this greybeard engineer. You know, it's like they're usually like, you know, oh, we've hired a young PhD. You know, we've hired these young...

**Chris Gammell:** Yeah, right, right, right. PhDs or whatever.

**Dave Jones:** And, you know, like, yeah, they don't seem to be... I don't know. I actually... Have you seen that at all?

**Chris Gammell:** I don't think I agree with you on the hardware startups are doing the most interesting things. I actually think it's like the most interesting problems I've seen are like at the Northrop Grumman's of the world, right? Yeah, yeah, no, of course. They're like these defense contractors and they have like super, super specialized roles for hardware. And they're just doing things that nobody else is asking for where there's... The market is like the US government and then the British government. And that's like it, you know? Right. It's like, oh, okay. Well, that's probably not going to work if you're trying to sell into like consumer level markets or even industrial level markets. So I think that might be part of why you don't see as many older engineers in startups. I think there's also a risk tolerance type thing. Like you might not want to take the risk of, you know, delaying some of your compensation towards stock that's worth something in 10 or 20 years, right? So and if it's another bet, right? So if you do that when you're 25 or 30, it's like, okay, that the first startup didn't work out. The second one did. And then you've, you know, you've made a small payday. It's like, okay, no big deal. Or maybe you do three in a row and it's still not that big a deal because then you're still you're 40 and then you go work at a corporate job or something like that. You have this interesting experience in your resume.

**Dave Jones:** Well, this, the, the poster on Hacker News, man next door, he basically seems to be talking about sort of like, you sort of end up in a limbo land where you don't have enough experience to be a staff engineer or a principal engineer or whatever the buzzword is these days. Right. Cause he's saying that, you know, like only the top three, he uses the example, only the top three to 4% of engineers in the industry have that sort of level yet. You're sort of, you're, you're more experienced, way more experienced than just all the regular, you know, Joe average engineer.

**Chris Gammell:** You might get someone who's a senior engineer, who's like got five or seven years of experience. And then the next step up for them at 10 years of experience is that same level as you at 30 years of experience.

**Dave Jones:** It makes sense. Yeah. I've, I think I've said this in my videos. Once you get like five plus years experience on your resume, it's like, yeah, you're in, right. You're, you're an experienced engineer and you're pretty much the same. It probably makes no difference between five years and 15 or 20 years experience. Really?

**Chris Gammell:** Right. Right. I think some of it is, is like you're, you know, you're how well you're known, what you're known for, what you can deliver. And yeah. Yeah. You've crossed that threshold.

**Dave Jones:** Once again, I think it comes back to your previous work experience. Like, do you have a work experience in that field? If you do, you're in. And if you don't, it's like, well, you can come on as a Joe average engineer, but you know, like, yeah.

**Chris Gammell:** Yeah. I mean, well, I think the other thing that happens too, is that some of it is structural in the industry. Right. So like a lot of people around that age, they start moving up. They're like, okay, I want to move up the company. And, you know, a lot of companies do have dual track. They have independent contributor or technical track, and then they have a management track. Right. And, you know, I've seen that promoted by other people as well, where, you know, I think the top, the top tier that I saw was like chief architect scientist or something like that. Yeah. You know, basically that is the top of the technical track. But from my perspective, that's still like, you're not really running things. There's always like command and control aspect of it all. And it's like, yeah, the management track is still making decisions.

**Dave Jones:** Yeah. Well, I've worked at companies where people have gotten into management engineering roles that have, that suck at management. Like they can't do management. They have no experience in it, yet they got there simply because they've been there the longest, you know? Totally. And like, yeah.

**Chris Gammell:** Yep. Right. Right. And, you know, I've talked to people. So like, obviously in the consulting world, I think consulting is a work around all this, right, both in hardware and software that you can take your expertise. You can kind of sell that expertise at a premium and say, I'm short run, you're not hiring me for forever, but you can use my expertise. You can rent my expertise instead of buying it, that sort of idea. Yep. And I've met people that have actually come back into technical consulting from managerial space. And it's just like, yeah, they're like, I didn't want to do that anymore. And that's kind of the, that's the way to pull the lever. I mean, I was kind of on that path as well, right? I was in product marketing. Right. And I was moving towards like more of that. And I was like, no, I want to do technical stuff. So.

**Dave Jones:** Right. I've, I've been in a group, like a hardware group. I was just, you know, engineering the hardware group and the position was open for the head of the hardware group. Right. And it actually went to another engineer over yet another engineer who had a master's degree and had a lot of experience managing groups. Right. These were new, new employees who came in. We were all fairly new. And, but the person who got the role was not the master's degree experienced in managing hardware teams. Where's a tie every day guy. He didn't get it. It was the barefoot, you know, t-shirt hardware engineer. The hippie engineer. It was the hippie engineer who, I'm being a bit melodramatic, but you know, yeah, it was like the one who had no engineering, who had no management experience at all. But because that person was the most liked engineer. Ah, interesting.

**Chris Gammell:** Like a team leader style kind of thing.

**Dave Jones:** Well, no, it wasn't even a, well, yeah, no. The person much higher up in the company liked this guy more than he liked the guy who should have got the job, who, who actually had real team, you know, technical engineering team management experience at multiple companies. And he didn't get the role. He was, he was effectively demoted to just regular engineer. And so, yeah, it's, it's not who, you know, it's not what, you know, it's who, you know, I guess, or who likes you.

**Dave Jones:** Yeah.

**Chris Gammell:** It's who knows you, Dave. That's the, that's the way that phrase goes.

**Dave Jones:** Yeah. I thought that was, you know, and he left soon after because he realized like, this is just dumb, you know, like, come on. I'm, you know, this guy has no management experience whatsoever.

**Chris Gammell:** Was there an age aspect of that or no? Oh no. Or was it just experience?

**Dave Jones:** No, similar age. No, no, it certainly wasn't an age thing. It was just a simply, no, this person was liked more. So they got the role even when they probably shouldn't have, you know? So yeah. Yeah.

**Chris Gammell:** Yeah. Interesting. Yeah. Well, I suppose this is as good a time as any, I should probably announce that I, I actually, speaking of startups and speaking of non-management roles, I recently joined a startup.

**Dave Jones:** I didn't know you were going to announce this.

**Chris Gammell:** I am going to announce this. Yeah.

**Dave Jones:** You are now a full-time employee.

**Chris Gammell:** Yes.

**Dave Jones:** Yes.

**Chris Gammell:** This is actually a former guest of the show, Jonathan Berry. We talked about why IoT sucks. And actually, he didn't want me to name it that at the time. That's what I said, why IoT sucks. And I think we named it why IoT is hard. And this is back in January, I think, of 2021. We talked. And then back around April, I started talking to him. When I went on paternity leave, I started talking to him about consulting. And then, you know, just enjoy the team, enjoy the space. And I enjoyed torturing Dave talking about IoT.

**Dave Jones:** Yep.

**Chris Gammell:** And so that's fun. And yeah, so I'll be doing hardware. I'm the only, much like Dave said, I'm the only hardware person at this startup.

**Dave Jones:** Which is small, right? It's like sub 10 people or something. 10 people. 10. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** But yeah, it's an IoT platform. I posted about it in the channel. And yeah, I'm really excited about it. It basically enables hardware. I always say hardware weenies. I probably shouldn't say that that often. But I always say hardware weenies like me to actually connect things to the internet, which is like completely impossible, right? Yeah.

**Dave Jones:** To me, from a software point, like, you know, I can program, but I can't. Once it involves web and the internet and everything, or no, I'm out of it. You know, I'm just like, no. Exactly. No, throw my hands up. No.

**Chris Gammell:** Yeah. Yeah. And so this actually, it's built with Zephyr, which is the open source RTOS that I've mentioned in the past. Yep. And that 100% has learning curve. I'm trying to make videos about it and like make that easier to learn. But once you learn that and you tie this stuff in, it actually like, it's for example, like the ABC board, which I've talked about on here. And I made that for my course. I just kind of figured I was going to figure that stuff out later. Right. I hired Bilal, who I've talked about on the show before. He's the one who was a Zephyr developer. And even like Bilal didn't know how to like, he knew how to like throw packets at an MQTT endpoint. But like, okay, then what? And like, how was I going to figure out how to do like firmware updates and like hook into databases and do all that other stuff? And so this is all that other stuff basically kind of taken care of. And even some of the stuff that Bilal was doing, well, assuming someone like Bilal has already written a driver for it. Right. So if you like choose a board that already has all the drivers, basically I stood up a, I stood up a demo for a, you know, flip a solenoid, turn on LEDs, measure whether or not a door was open and do all that over cellular and have firmware updating. And then be able to like change all this stuff over cellular to the network, to a, to a web endpoint.

**Dave Jones:** Right.

**Chris Gammell:** And basically like from the, from a webpage, I could like do all that stuff I was talking about, measure and, and interact with stuff.

**Dave Jones:** Yep.

**Chris Gammell:** And doing all that took me three hours.

**Dave Jones:** Wow. Very cool.

**Chris Gammell:** Yeah. So I'm excited about it. Excellent. Hardrow weenies like me may enjoy it.

**Dave Jones:** Does, does that mean that you're out of the consulting business? No one should contact you?

**Chris Gammell:** We're doing a little consulting actually.

**Dave Jones:** So doing some, but not, you're not accepting new work. Are you? That's right. Yeah.

**Chris Gammell:** So don't call me about new stuff, but I have lots of friends on the consulting forum I can refer you to. So cool.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. Yeah. But building lots of hardware and yeah, it's really exciting.

**Dave Jones:** Well, I hope that works. I hope you get gobbled up by Google and you make a fortune because that's the end goal, right? Of every startup get gobbled up.

**Chris Gammell:** Apparently it is. Yeah. Yeah. Yeah. Yeah. So anyway, but yeah, build lots of hardware, hopefully that's a, and that's, you know, that's a, that's, you know, so like to be completely frank about it, like I, I enjoyed the stuff I'd done in the past and product marketing stuff at, at, um, you know, I did a little bit at hologram and a little bit at supply frame, but like one of the things that I struggled with was the fact that like, you know, you and I would talk every week and I'd be like, I haven't built electronics in like six months, you know? And it's just, you know, I get away from it and it's one, we don't have anything to talk about then. And two, it's like, I don't like it. I don't, I'm not as engaged when it's like just writing emails all day or writing, you know, marketing campaigns. So, so yeah, I am in, I'm back on that tech. I mean, obviously I've been on that technical track for the past three years doing consulting, but I was not going to hop away from consulting unless I was doing hardware design.

**Dave Jones:** And so I still am. Right. Right. So you wouldn't have gone to just a marketing role at some start. That's right. Yeah. I don't think. Even if they offered you a, you know, 30% in the company. Gobs of money. Oh yeah.

**Chris Gammell:** I don't, I, I just, I don't know. Like if you don't like your job in the day. Oh no, of course.

**Dave Jones:** Yeah. Yeah. If you don't like it. Yep. Why do it? Yep. Totally agree.

**Chris Gammell:** Right. Right. Well, I think we're very lucky in that way, right? That we have that option.

**Dave Jones:** Yeah. Yeah, exactly. Because we've been in the industry a while and we can, you know, people, people know.

**Chris Gammell:** Because we are 40 plus and or near, near to it.

**Dave Jones:** But more, but more to the point, people know who we are. So, you know, that's, that's more important than the, knowing people having, people knowing who you are is more important than, uh, it can be more important than what you've done and what you know. If people know you.

**Chris Gammell:** That's right.

**Dave Jones:** Then, you know, yeah. Opportunities come.

**Chris Gammell:** So one of the former engineer blogs, writers, there's a long, there's a long throwback for people, uh, for new listeners, a blog is what, uh, people used to write technical articles on. Uh, and so Sam Feller is one of the guys who used to write on. He actually just put out a post about a, uh, a CRM. So a customer relationship management software that he was using where he would just do that to keep in touch with people. And he said he got a bunch of like consulting work like that. And just like, he said he would reach out every on people's half birthdays instead of on their birthdays. And that like allowed him to keep in touch with people and that allowed him to get jobs. And yeah, I don't know. Just like people knew him because he kept in touch with them. So that kind of thing is important.

**Dave Jones:** Right.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm not, I'm not really a people person. Whereas you are, you're a contact collector. You're a, you know.

**Chris Gammell:** That's a little, little cynical. It's a little, little cynical.

**Speaker ?:** Maybe true.

**Chris Gammell:** Maybe true in the end, but, uh, I'd like to think I enjoy talking to people. How about that?

**Dave Jones:** Yeah. Yeah. Yeah. But you're much, you're order of magnitude.

**Chris Gammell:** You're more social than you think. You just don't need to talk to people because I mean, honestly you do though. Right. I mean, that's, that is another option. And that's what we talked to Florin about last week from Voltlog. You know, Florin got consulting work because he was doing technical videos. Yeah. And like people found him through the internet. It's basically, it's a. Yeah, of course. Pull instead of a push. Right. So Sam is writing about pushing out emails to people and keeping in touch like that. Yeah. And Florin is talking and Florin and you as an example as well. Basically, you know, you guys push out these, these videos and instead that pulls people to you. So I think that's another way to do it.

**Dave Jones:** Well, that's the, that's the difference between which is still current. It's all about your contact list. You know, it's all about your contact list. Like I get emails from companies all the time. Oh, can we, can we buy your contact list? It's like, no, I'm not, I'm, I'm not harvesting every, you know, like everyone who buys on my store, I'm not harvesting their email. You know, and I do actually have a newsletter where people can sign up and technically I, you know, I, I've got a list of like 5,000 people or something like that, but I'd never like sell it. You get an email when, when things are on sale. Yeah. It's like, whereas that is the approach that a lot of people in, in the industry take is that it's all about the quantity of names and addresses that you have and that sort of stuff, as opposed to like putting out content and then having new people actually find out you that way, actually making something useful.

**Chris Gammell:** Right.

**Dave Jones:** As opposed to, you know, making content or, you know, a product or something like that where, where people can, you know, hear about you and find you. No, you just actually collect. You just harvest, you know, contacts. Yeah.

**Chris Gammell:** Yeah. Yeah. I mean, I think a lot of that is kind of the, the view of the internet of like, there's always more people out there and, and, uh, I usually don't ascribe that to like the electronics world of, of the internet. You know, the electronics people on the internet, there's probably millions of people that are interested in electronics at various levels, but like, you're trying to find like the most engaged people in test equipment. It's probably a, there's probably a fixed number at any given time in history. And so if you try and gather all of the people on the EV blog forum and spam them with an email, uh, that crowd might get to, might get a little upset.

**Dave Jones:** They'd get a bit miffed. Yep. Yeah. Yeah. Yeah. For sure. Yeah. Well, I've, I've not like every time I, even though people deliberately signed up for my email list. Right. And I, and I tell them when they sign up, it's like, you're signing up because I will send you very occasionally, like when I release a new product or I have a sale or something like that. Right. That's right. You, this is what you're signing up for. Right. Like it's not, and they have to go to the webpage, put in there and hit the button, everything. And then I get, you know, every time I send out a mass email to like 5,000 people, I can actually see, you know, in the data, you can see how many people unsubscribe and, you know, they hit the unsubscribe button. It's like, no, I don't want this shit anymore. This is, you know, and, and you get, you know, reasons I didn't sign up for this. It's like, yeah, yeah, you did. Oh, I forgot about that. Yeah. Right. You know? And it's like, yep. Yeah. Yep. And, uh, and it's the same for signing up for a, when you subscribe to a channel, right? You subscribe to a YouTube channel, you subscribe to a podcast like this. It's like you change over the years, right? You, you signed up for that content back then and the content hasn't changed, but, but you've changed, which isn't a bad thing. You know, like it's just, you know, people's change, people's needs and, and things change over the years and their interests change and whatnot. And the, what they signed up for a long time ago is no longer relevant.

**Chris Gammell:** Yeah. Yeah, totally.

**Dave Jones:** Hmm. Have we YouTubed enough for today? Have we content platformed enough for today?

**Chris Gammell:** Sure. Yeah, I guess so.

**Dave Jones:** Probably.

**Chris Gammell:** Are we over the limit? We are over the limit. We are over the limit. We're a minute over, dude. There, I mean, I want to talk more about IOT, not about my IOT actually, but Amazon, Amazon just launched, it launched something interesting. A private 5G network. So this is an Amazon. So basically if you, so Amazon has their big conference right now, reInvent. I think it's, it's over tomorrow. So it'll be over by the time people are listening to this. You can go watch the old stuff, but.

**Dave Jones:** Well, they physically install in polls. What's, what's going on? How's, how are they doing it?

**Chris Gammell:** They will have, yeah, they'll have like transceivers on site. Like, so say you had a factory. Yep. They'll have like, what do they call them? Like Pico stations? Yeah, yeah. The little, yep, yep. Yeah.

**Dave Jones:** So they'll pay to put them on your building or something? Is that the.

**Chris Gammell:** Well, it'll be private to your, your staff though. Right. So basically it's like, and you can already do this. Like, so the, the fab that I used to work at, at Samsung, they had a telephone system at least. Not, not that they're talking about telephone system here, but they, they had a telephone system that was bespoke to a fab and use low frequency audio signaling to, to reach all the different phones in the fab, that sort of thing. And so now this is kind of the same thing. It's like high speed, high bandwidth capabilities to maybe inside your warehouse or, you know.

**Dave Jones:** Right.

**Chris Gammell:** So maybe like the DigiKeys or the Mausers of the world, they want to know where their carts are and they want to have like precise tracking. Okay.

**Dave Jones:** So they're targeting businesses, right? They're not, they're targeting factories and businesses that they aren't targeting Joe Average on the street to.

**Chris Gammell:** That's right. Yeah. I mean, they're not even a carrier. They don't even guarantee that they would hook you into, basically they're just hooking you into a local network at that point. They're not hooking you into a carrier and into the broader like VoIP ecosystem or data ecosystem. As far as I understand it, I think this would be like, you'd have a, you'd be using like 5G frequencies. So you could buy an off the shelf 5G modem, you know, so like a lot of like QuickTel and SimCom and a lot of them offer 5G modems now, which is cool.

**Dave Jones:** Well, this was going to be my question. Have they developed their own hardware or is the, are they just using off the shelf hardware and it's just a software infrastructure? Oh, it's off the shelf. Is it? Okay. Right.

**Chris Gammell:** Yeah. And it says it uses shared spectrum, like CBRS, right? So CBRS is citizens broadband radio service. So basically they're within a certain band.

**Dave Jones:** I didn't know there was citizen band stuff on fire in, in the 5G space.

**Chris Gammell:** Yeah. 5G kind of spans a lot of stuff. So like, if you look at a lot of what 5G is like, there's like a additional spectrum in some of the 4G frequency ranges. And then, you know, so 5G also has millimeter waves. And then that's up in the multi, multi gigahertz type of ranges. And that's when it's in the 13th or something. Yeah. Right. Yeah. You start to see like, uh, like transceivers on multiple poles in a city, right? So that's what they start talking about. So 5G is very, uh, it's not nebulous. It's, uh, it's very dispersed over different technology types. And it's kind of all falls under this 5G umbrella. Right. That's why for a long time we said on this show, 5G doesn't exist. Uh, but when a lot of the marketing started, it was basically just like higher, higher bandwidth 4G frequencies. And what's eventually going to happen in theory is that it will have, you know, you'll have millimeter wave transceivers kind of spread throughout a, uh, a city, for example, and you'll have really short distance, but really high bandwidth. And that's kind of the idea there. So. Okay. Well, this is, this is interesting. Yeah. It's interesting that, I mean, really this is a new space for Amazon at least. And they had a, they had a bunch of different announcements come out of our reinvent. Uh, this is one of the most interesting ones that I saw. Uh, so yeah, it's interesting to see this kind of thing. Like, like I said, I mean, it's possible for people. So like they had a, you could set up a LTE frequency network other places. Right. So like when I went to, uh, uh, what's it called? Not tour camp. I went to chaos communication camp. Like they actually had a private network. So private cellular network on site where they had, you know, they would hand you a SIM. It wouldn't talk to any other networks out there.

**Dave Jones:** Right.

**Chris Gammell:** But it operated in the same way. And they had like SDRs that were doing the same kind of thing. So it's not like, that's not possible now. It's then like, okay, are you, what frequency range are you in?

**Dave Jones:** Yep.

**Chris Gammell:** Uh, you know, make sure you're not stomping on some real carriers frequencies. And, uh, and then what are you then doing with that data when you collect it locally?

**Dave Jones:** So is this a new way to maybe automate factories? You would embed 5G. See the, the thing that immediately pops to my mind is the Amazon Kindle, right? Cause it, it has a 5G, like, well, it's got a SIM card in it. Well, you can buy a SIM card version, right?

**Chris Gammell:** Yeah. A lot of those, a lot of those are going to stop working soon. There's a lot of them are 3G actually. Oh, right. The older ones. 3G and a lot of 3G shutting down. Yeah. Right. Yep. Make sure your wifi password's updated. Make sure your wifi works.

**Dave Jones:** Yeah. So they could, uh, presumably like as they come off the, they're, they are already doing this as they come off the production line, they can actually program these things and they set them up as they come up. You know, when, when you order one, you can set up and they can program that and they can target that particular serial number device wirelessly and program it and pre-set it up for your actual account for your Amazon account. Which is fairly cool. And they can do that using these little 5G transmitters things. If it's got a 5G receiver in it.

**Chris Gammell:** Yeah. I mean, I don't think that would be the target of this specific thing for Amazon right now. No, it's not.

**Dave Jones:** No, but that's what pops into my mind, which is why I mentioned factory automation and stuff like that. You could, you know, you could potentially build into your factory equipment, these little 5G.

**Chris Gammell:** Yes, that's right.

**Dave Jones:** Yeah. You know, transceiver things. But then again, like there's so many existing solutions for that. You know, anyway. Yeah.

**Chris Gammell:** I mean, I think most, most people that are like low, you know, low number of devices and stuff like that. As long as you have a tower nearby, it's going to make more sense. Even though you're, you're paying a carrier then it's like, it's going to make more sense from an infrastructure perspective to use a carrier and rely on the towers and that sort of thing. So.

**Dave Jones:** All right. But if you, if you can control it yourself, then, you know, that's going to be better, I guess. Cause then if the tower goes down, you know, or something happens, I don't know.

**Chris Gammell:** I guess I don't.

**Dave Jones:** Then your factory keeps running, I guess.

**Chris Gammell:** But I guess so.

**Dave Jones:** I don't know.

**Chris Gammell:** Yeah. I mean, factory stuff is, is very, very difficult.

**Dave Jones:** Yeah.

**Chris Gammell:** Anyway. Fascinating. If you've, if you've got in place machines, I'd say good old copper. Yeah. Copper. Yeah.

**Dave Jones:** With the signals flowing inside the wires. That's right. That's right. Yeah. Nice. Nice throwback. Thank you.

**Chris Gammell:** Yeah. Yep. All right. That's enough from us. I'm sure we'll have lots of IOT things to torture Dave with in the future.

**Dave Jones:** Oh, great. Great. Yep. Thank you. Talk to you then. Catch you next time.

**Speaker ?:** Bye. Thank you.
