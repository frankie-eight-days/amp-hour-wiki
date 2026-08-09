---
episode: 510
title: Knob and Tube Wiring
url: https://theamphour.com/510-knob-and-tube-wiring/
---

**Chris Gammell:** This is The Amp Hour Podcast. Release September 28th, 2020. Episode 510. Knob and Tube Wiring.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Camel of Contextual Electronics.

**Dave Jones:** We have gone back to the future. I am in the old lab.

**Chris Gammell:** Yeah, yeah. How long is that time loop? Last time I was here. Yeah, when did you leave now that you're back?

**Dave Jones:** Well, last time I recorded an Amp Hour in here is probably four years ago. At least.

**Chris Gammell:** So we'll just say you're on a four-year cycle, you know?

**Dave Jones:** Yeah, right. And bonus, I'm using my old mic. My old Samson C01U that we started our very first Amp Hour with.

**Chris Gammell:** Yeah, man, this is like a throwback show.

**Dave Jones:** Yeah, but I'm out of the cubicle. I'm not recording in the cubicle anymore. Oh, you're in the middle.

**Chris Gammell:** Are you going to set up the webcam again and have people make comments of you about your working?

**Dave Jones:** Yep. Or lack of...

**Chris Gammell:** See, the nice thing, Dave, is that the surveillance technology has gotten so much better. Yeah, right. I don't know if you saw, but there was a crazy tweet today that apparently Amazon Nest... No, Amazon... Who owns... It's the Amazon thing.

**Dave Jones:** Yeah, yeah, Nest. Well, no. Ring. No, it's Ring. Sorry, Ring.

**Chris Gammell:** No, Ring. Google owns Nest. Amazon bought Ring. Ring is like the doorbell folks, and they're trying to do security and stuff like that, too. Right. They just announced today, it's like the craziest looking thing. It's this little IoT looking thing that's plugged in on your desk. It's all industrial design-y. The center part of it takes off, and it goes around your room as a drone. That's just stupid. It's so dumb. It's like a sentry, basically. Right. Oh, my God. So it's an indoor drone. Yeah, it basically goes around, it will check the perimeter, and then it'll come back, charge itself, do it again. A little flying sentry.

**Dave Jones:** That's just dumb. It's so dumb. Just permanently install a camera in each room if you want to check each room. I mean, geez.

**Chris Gammell:** Right, right, right. Right.

**Dave Jones:** Oh, it's just...

**Chris Gammell:** I mean, maybe if you've got really, really high ceilings, but probably what it is, is the engineers there were like, let's see if we can build a quadcopter.

**Dave Jones:** I know. That is a solution looking for a problem. That is a very hard solution, actually, because I've done some work on autonomous quadcopters where you don't have GPS and stuff like that, and you have, like, it's indoors. We said we were doing it outdoors in the canyon.

**Chris Gammell:** Right, so you've got to do, like, pinging or some kind of other way. Yeah, yeah.

**Dave Jones:** You've got to do active radar and stuff like that. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Or ultrasound or whatnot. You know, you've got to do something.

**Chris Gammell:** Or you've just got to make it really, really robust so that it can just run into things.

**Dave Jones:** Right.

**Chris Gammell:** Get chewed out by the dog and, you know, put back, and it's just fine, you know.

**Dave Jones:** That was an essential part of the backup plan was to armor the, yep, thing so it could actually run into, you know, trees and whatnot. Although you just, these days, just throw processing power out. You just have a camera and just do it all visually and throw.

**Chris Gammell:** I guess. I mean, he's got to write the code for that then, though. I mean, like...

**Dave Jones:** Well, yeah, I know. Some bastard's got to write it. It's like, yeah, it's... Yeah. Anyway.

**Chris Gammell:** I guess people need jobs, you know. Engineer work program. Put people to work. Put these ridiculous things into the consumer market. Oh, my God.

**Dave Jones:** Solution looking for a problem. I mean, it's just...

**Chris Gammell:** Definitely, yeah.

**Dave Jones:** Oh, wait. I've got a segue for that, but I wasn't going to jump into it already because it was going to be a segue on top of a segue.

**Chris Gammell:** Oh, well.

**Dave Jones:** So I don't know if I should jump straight into it.

**Chris Gammell:** I don't know if you've been paying attention to the 2020, but life does not really go according to plan.

**Speaker ?:** Right.

**Dave Jones:** And neither... Yeah, neither did our bloody microphone. All I did was move from the big lab to the old lab here, move the computer, physically move the computer. Everything's the same.

**Chris Gammell:** It's bit rotten. Bit rotten, you think. Maybe cable... Cable rot. Cable rot. You know, USB cable's gone bad. You got to switch those out every year, unless you get the really, really expensive ones, you know, like the gold-plated ones.

**Dave Jones:** Right. Okay. That's kind of... That makes the difference. Yeah. Yeah. It's my Rode mic that worked fine locally. Like, it works... Like, when I record locally, it works fine. And yet, then, when we try to use any streaming program at all, either Zencaster, which is what we record this, or we even went back to Mumble. We were that desperate. Went back to old-school Mumble. And it just would not work. So I had to whip out my old... When in doubt, whip it out. Whip out my old Samson USB mic.

**Chris Gammell:** That is not the phrase that we use on the Amp Hour very often. Or ever.

**Dave Jones:** It can mean any tool you like.

**Chris Gammell:** Sure.

**Dave Jones:** Yeah. Nothing wrong with that. Anyway. Anyway, so, yeah, that was weird. So we spent half an hour dicking around before the show trying to get a bloody mic working. Unbelievable. Anyway.

**Chris Gammell:** So was that the segue? That was the segue? No. No, no, no. So what's the segue?

**Dave Jones:** Well, I don't have... I don't want to segue directly into that. Oh, no. Okay. We'll segue directly into that. Fine. Is it on the list? Yes, it is. It's even on the list. I'm segueing into something on the list. True professional. It's the... Where is it? I've got to find it.

**Speaker ?:** Ah!

**Chris Gammell:** Oh, come on. Come on. The old TV causing village broadband? No, no.

**Dave Jones:** It's not the TV. It's the electrified roads. Here it is. Tel Aviv. Set to become the first city with electric roads that charge vehicles. And heaps of people sent me to this. I might have to do a... Just a... I'm not going to do a debunking video on it because this wireless stuff. But once again, my take on this is it's wireless charging in roads. Right? Actually embedded under the surface of the road. And it charges your car. It charges your bus. It charges your taxi as you drive along.

**Chris Gammell:** I've seen this before. They do this in China. We've seen this. We've talked about this on the show before. Oh, it isn't new. Yeah, no. About China as well, right? And it's... It was not in the road, though. It was actually in like... It was like a raised platform bus stop. Right. Yep. And then that basically had these huge coils. And so then when it pulls up the bus stop, it just gets... You know, it's like... It's a huge power transfer, but it just gets the charge and moves on. You know?

**Dave Jones:** Yep. And the reason they didn't put in the roads is because embedding stuff in roads is hard. Yeah. Right? Roads are expensive. Roads have been refined over hundreds of years to be minimal cost, even though they're still massively expensive, but minimal cost per kilometer, right? And longevity of the surface and all sorts of...

**Chris Gammell:** Yeah. It's got its own science that does not necessarily play well with electronics in it.

**Dave Jones:** No. No. Embedding stuff in... You know, it's bad enough embedding... Oh, well, it's... No. It's okay to embed like those little sensor coils for the lights at the traffic lights, right? Because that's only one spot.

**Chris Gammell:** Yeah, but even those break all the time. I don't know. I feel like those... You know, like they're...

**Dave Jones:** It's just...

**Chris Gammell:** It's a really harsh environment. That's really what it comes down to. Yes.

**Dave Jones:** Yes, it is. It's, you know, it's got like the bases that shift and that's why roads crack, the thermal expansion coming out your wazoo and there's, you know, all sorts of stuff.

**Chris Gammell:** You guys don't even have ice there. You don't even know. No. I know. It's like... Three thaw cycles, people. That is the worst. Right. That is why our roads are... Well, that is one of many reasons that the roads are terrible here. Absolutely terrible. Just like bridges falling over. It's real bad.

**Dave Jones:** Ice. Yeah. Snow and ice. We just don't get that here anyway. Except in really extreme Alpine regions. Right. Anyway. This is... Once again, it's a solution looking for a problem. Sure. It works in quote marks, right? And now they're talking about what sort of power levels they're talking about. They're talking about like... I don't know if it's in this article. They're talking about like, you know, 10, 20 kilowatt, you know, wireless transfers, which is, you know, great. Okay. You know, they're always coming out with, you know, some university research group is coming out with the latest whiz bang, you know, technology to wirelessly transfer 10 kilowatts of power. Okay. Okay. Great. That's fast charging for a vehicle. Right. Because once again, we'll segue into, I now own an electric vehicle. So we can talk all about that. Got it. Yeah. So that's, you know, that's a relatively fast charge, right? That'll charge a typical EV in like a 10 kilowatt charge, you know, in two hours, you can recharge your EV or two, four hours. Maybe, you know, you can...

**Chris Gammell:** Yeah. I don't know. I don't actually have a good... No.

**Dave Jones:** Yeah. Don't have a feel for it. Let's say for four to five hours.

**Chris Gammell:** Okay. So, well, how big is... So let's just talk about... Let's just talk about your car. How about... Because then that's a good thing to focus on. Yep. So your car, how big is the battery pack?

**Dave Jones:** 38 and a half kilowatt hours.

**Chris Gammell:** Okay. And I remember seeing at Twitter, you said you only have the normal wall charger. You don't have like a fast charger.

**Dave Jones:** I don't have a fast charger, but I'm thinking about getting one in store because there's a pilot program here that'll pay for it for me. So... Oh, nice. Okay. Yeah. I've got to sign up for two years though.

**Chris Gammell:** So like we can do the math in our heads, but if you... Yep. What's the full charge time for your car? Is it like eight hours?

**Dave Jones:** The full charge time would be about 12 to 13 hours using the socket. Okay. Right? Just using the socket, which is 2.4 kilowatts. Right?

**Chris Gammell:** So then that plays pretty well with the four hours for a 10 kilowatt kind of thing.

**Dave Jones:** About four hours for a 10 kilowatt. Okay. Kind of. Once again, from zero to 80%. So usually you'd only charge your EV to 80%. You don't charge it all the way to 100 because that impacts your battery life.

**Chris Gammell:** Okay. And then what would it be if it was like a fast charge?

**Dave Jones:** If it was a fast charge, you might be talking like my car's capable of 50 kilowatts maximum. So once again, five times faster than that. So you're talking like 40 minutes, something like that. Wait.

**Chris Gammell:** So. What do you mean 50 kilowatt? 50 kilowatt capacity?

**Dave Jones:** 50 kilowatt charging power. Kilowatt. For fast. Oh, no. There's three levels of charger on my Hyundai Ionic. There's the 2.4 kilowatt, 10 amp, 240 volt range. Oh, yeah. Jeez. Right?

**Chris Gammell:** Sorry. No, I'm getting myself confused here because this always happens to me. So your battery pack is kilowatt hours, right? Yes. Because that's total energy capacity. That's capacity. And we're talking about power transfer right now.

**Dave Jones:** Power transfer. That's right. Okay.

**Chris Gammell:** Yeah. Okay. Yeah. All right. So go back to what you're saying. Sorry.

**Dave Jones:** So 2.4 kilowatts charging power, standard main socket.

**Chris Gammell:** Yeah. That's like a 10 amp on a 240 volt mains, right?

**Dave Jones:** That's right. Then I can jump up to a single phase mains charger. So once again, a 240 volt single phase, and that's 30 amps. So you're talking about seven kilowatts, something like that, around about seven kilowatts. They're both AC chargers, and they use a separate, they use the AC charging socket, which is the type two socket, it's called, generically type two socket.

**Chris Gammell:** Plugs into like a dryer instead of just a standard wall outlet, that kind of idea.

**Dave Jones:** Yes, that's right. My car, sadly though, does not support three phase charging. So that type two socket actually has three phases on it, but my car physically does not have the charger inside to support three phase, only single phase. So if you had three phase, you'd get up to 24 kilowatts, something like that.

**Chris Gammell:** But mine's only seven. So in the States, because we have lower voltage, we actually do it where- You have higher current. Well, yeah, two phases come in though. So my dryer, if I go down to my breaker box, I have basically, there's the two phases that are on either side. And then for like the dryer, it actually, it uses two phases to get to the higher voltage so that you can get higher power output. But yeah, standard breaker is 15 amps.

**Dave Jones:** Yes. Your system's very different to us. Your- Yeah. Everyone says US is 110 volts. Technically it's not. US is 240 volts, just like here, except you guys split the phase. You guys split it. There's, you can go into the technical details of it. But yeah, if you go phase to phase, you guys get 240 volts.

**Chris Gammell:** Yeah. I think most people say that because like, if you're coming out of the wall, it's 110, 120, you know? Yeah. Yeah. Yeah. If you're coming out of the wall, yes. Every device is not, most devices are not ready to plug in for 240. If you do that, it's, you let the smoke out.

**Dave Jones:** Yeah. But you guys don't actually have 110 volts coming into your house. You guys actually have the- Right. Yeah. Yeah. Three phases and yeah. Whereas we have single phase 240 volts.

**Chris Gammell:** Not three phase. We have two phase come in.

**Dave Jones:** Oh, sorry. Two phase come in. Yeah. Anyway. Yeah. So, yes.

**Chris Gammell:** This is what we talked about two shows ago too, because remember we were talking about industrial spaces and how that x-ray machine we were talking about- That's right. That actually required like really, really high power, but it's like a special thing. You know, generic office probably wouldn't have that. Even if it has- No, that's right. You know, a high current service, maybe it could do a couple hundred amps into the building. It's probably not at three phase. It's probably just doing that lower 240, two phase kind of thing.

**Dave Jones:** That's right. Yeah. Here in Australia, nobody at home, I don't, I've never seen a single house that would ever have like a 32 amp socket, you know? It, it, like, you know, three phase or, uh, yeah, just a higher current socket. It just doesn't exist here. You know, it's only for like machine shops and stuff like that. It's machine shops and stuff like that. Yep. Totally.

**Chris Gammell:** Does it, does that mean it's like, is it really hard to, to build a machine shop in Australia then? Because like really specialized wiring or is it just, you just hire an electrician and they just know what to do?

**Dave Jones:** Oh, well, no, technically I could, I've got 60 amps coming into my house, right? Cape capability. That's the main few. So technically I could get someone to come in and wire up one of these 32 amp sockets, you know, but, you know, that's very unusual. So, yeah.

**Chris Gammell:** And you're saying that would be the, the 7200, the 7.2 kilowatt hour. 7.2 kilowatts. Kilowatt. Yeah. Okay. And so that would just be, that's, that's just be like a larger, so like to, in the States at least, when you're like open up a breaker box, it's like most breakers are 15, you can get a 20 and that's actually a slightly different plug. That's the one, if people are in the States, it has the little plus, you know, like the, the one that goes out to the side, that's like a 20 amp and then like, or maybe that's the 30 amp as well. But, but basically you can get just different size breakers that just kind of consume more of the more space and they're just larger breakers. Yes. Right. Yeah. They pull off that bus bar more, you know, more current off the bus bar.

**Dave Jones:** Exactly.

**Chris Gammell:** I don't know if I've ever seen an Aussie breaker box.

**Dave Jones:** Oh, they vary greatly. Yeah. I've, I've posted photos of mine and I've got a friend who's working on a, well, I'm not allowed, I'm not sure if I'm allowed to talk about it because I haven't released details, but let's say it's a home battery solution.

**Chris Gammell:** Okay. Okay.

**Dave Jones:** Let's say working on a startup for doing home, home battery solutions. And I, I send him a photo of my box cause he, I'm looking at maybe getting one of his things for trial, you know, he wants to use, you know, wants to give me one. And, um, and, and he looked at my breaker box and wow, we've never seen anything like that before. It's like, yeah, yeah. There's lots of, lots of variability here.

**Chris Gammell:** Yeah. Yeah. There's, there are a little more, I don't know if they're standard here, but all I know is that when I, I, when I moved out of my old house, I, uh, I had to, or sorry, when I moved into the house, they had to switch out the box before I moved in because they, they had the kind installed that blow up. There, there was a certain brand that used to just blow up. The breaker boxes would melt down and, and, uh, it was like part of the inspection process. They're like, yeah, no, you have to, you have to replace that.

**Dave Jones:** You have to get, get all those changed. Wow.

**Chris Gammell:** Yeah.

**Speaker ?:** Whew.

**Chris Gammell:** Yeah. Nasty. I'm trying to remember. It was like Pacific or I forget, I forget the name of the company. It was a certain company, but like anytime a house inspector sees it, they're like, nope,

**Dave Jones:** not pass it with that thing. I assume that they're banned from import now. They're, I assume they're just banned totally.

**Chris Gammell:** Or are they so old that they're simply out of business? The thing would be something. So like some, what's crazy too, is that like with a lot of like housing stuff in the States, you can get like grandfathered in. So like you could even have like knob and tube wiring.

**Dave Jones:** What's knob and tube wiring?

**Chris Gammell:** Knob and tube wiring is basically you have the hot, hot neutral and, and, uh, and ground. Knob and tube would be like, you'd have like an exposed copper bare wire going through your, you know, the lath house and just going. And it just gets wrapped around a tube, a tube being like, just like a insulated, uh, it's like a piece of ceramic. You can probably look it up. It might be easier to do that, but it's like a piece of ceramic that got nailed into the, into the studs inside the wall. And then you would run a uninsulated wire from point to point to point. And like, that would basically be an uninsulated hot, you know, 120 volts flowing on that, on that thing. And like that, why would you do that? Because that was the construction method before they came up with, you know, safety switches and all these other, you know, all the other things. It was just like these old methods of doing things. And then over time it got, you know, the national electric code kind of developed, but they would get grandfathered in to certain places. And like there, I don't think there's any rule against it. Usually what it is, it's like, you know, you go buy, you go to buy a house and an inspector is going to look at it and be like, this is a dumb idea. You should not do this, but it's not like you, you cannot do this. Like a lot of other places are much more stringent about it. I'm probably saying all this stuff wrong. So please don't write it. You can write in, of course, but I have not looked at housing stuff in a long time. So I now rent. And, uh, but like, yeah, I, there, there was nothing that it was like a lot of stuff would get grandfathered in. So like, you know, electricians see some crazy stuff.

**Dave Jones:** See, that's when I rented the lab I'm about to move out of now, uh, two years ago, I moved in, I had no safety switches at all. And it's actually, that is, that's not allowed. Now, if you rent a place, if you rent a place to a new tenant, it must have safety switches installed. Right. So it's like, so I contacted him and said, Hey, doesn't have safety switches, please put them in and pay for it. So thank you very much. Yeah. Yeah. It's just against code.

**Chris Gammell:** I think, and honestly, that's like how you, that's like where the rubber hits the road. It's like, in terms of like commercial and housing, all these other things. Like if you like, you can set these regulations, you can't like tell someone you have to go and like rip all the wiring out, but you could say, well, this is a worthless property until you do that. Like that's where you actually make these changes happen. So, uh, but yeah, that the whole time I was in Cleveland, I, it was knob and tube, but then they ended up, you know, pulling Romex at some point, which is like, you know, just two wire instead of three wire. So every outlet in that house was a two wire outlet instead of three. So no ground, no earth ground.

**Dave Jones:** Wow. Wow. It was old. I'm just looking at photos for knob and tube wiring right now.

**Chris Gammell:** Knob and tube is, is, is gnarly. It's.

**Dave Jones:** Oh, wow.

**Chris Gammell:** And like, it would be, and the reason they found it, the easy way to found it was like, there was a door to the, uh, the crawl space above the garage. And like, you open that door and it was like in the master bedroom, you open that door and like you turn your head and there's a light bulb right there. And then right next to it, it's like exposed wiring. That's knob and tube. He's like, well, that was easy.

**Dave Jones:** Yep. That is. Wow. I had no idea. That's incredible.

**Chris Gammell:** I mean, the thing is, it probably was like that in Australia too, but it's just like,

**Dave Jones:** Oh, maybe there was so much.

**Chris Gammell:** It's like when the stuff, like when was, when was all the stuff built in Australia? Like when was, like, when was your subdivision built? You know?

**Dave Jones:** Right. Yeah. We're talking like, you know, forties, fifties. Like there's very few really old houses here, here in Australia. Like, you know, most of them.

**Chris Gammell:** And it's like, it's such high, like real estate costs too, that of course they would just go and replace it or, you know, like they're going to knock that house down anyway. So why would that survive?

**Dave Jones:** No, no, that's right. Yeah. Very few old, old houses survived that it'd have anything like this. So.

**Chris Gammell:** But yeah, it's like you did. And a lot of it is the vintage of the house too, because it's expensive to pull new wire. It's just. Yeah, of course. Yeah. But that's why you should always, if you have a new house and you build a new house, wire, you know, obviously use three wire Romex, but then also like, man, put in some Cat 6. You're not going to get a chance again. And like. Yeah, exactly. You know, Wi-Fi is great, but it sucks sometimes.

**Dave Jones:** I think it's specific to North America. I think it's this knob and tube stuff.

**Chris Gammell:** Is it? Yeah, maybe. I mean, it could be just like. Reading the wiki. The wild, wild west, you know. Got it. Yeah, it's wonky. Wow.

**Dave Jones:** That's incredible.

**Chris Gammell:** It's better now, hopefully.

**Dave Jones:** All right. EV charging.

**Chris Gammell:** Yeah.

**Dave Jones:** We have those two levels. So they are. So technically you have three levels of AC charging. The main socket, the single phase and the three phase. But my car doesn't support the three phase. So that could go up to 22 kilowatts. And then the third one physically uses a different two pin connector, but it actually combines the two connectors into what's called a CCS connector. And that is. So it combines the AC and the DC, but it doesn't actually use the AC power. It only uses the AC power for its data control pins that actually, you know, tell it what type of charger it is and all that, you know, how much power it can draw and all that sort of jazz. So, but that, those two pins, that's DC charging. So that's, when you say fast charging, that's what you mean. Fast charging is DC charging. And that effectively just goes straight into the battery pack. I mean, that's like, you know. Okay.

**Chris Gammell:** So that's where the current control is. That's where it's talking back saying, hey, we got an overheating condition or something like that.

**Dave Jones:** It's very serious. My car's capable of 50 kilowatts, but you know, like a Tesla supercharger, I can't remember the exact number. It might be a hundred kilowatts or something like that. So yeah. Yeah. DC. I'm yet to try a DC fast charger because there's not many of those in Sydney. And that's something you wouldn't, you wouldn't get installed at home because it requires a gigantic box. Hopefully I can get the designer of one of these boxes on The Amp Hour. That is on my list. That is because they manufacture them here in Australia.

**Chris Gammell:** Like the country specific ones. Is it because the handles on the right instead of the left? Is that what it is? Right.

**Dave Jones:** I don't know if they can. I think they export them. I assume they export them. Okay. Yes. There's a company here that manufacture these. You know, they, they look like a large gas pump for you Yanks. Like, you know, like a big free stand petrol pump, right? Petrol pump on the side of, you know, so they have them like on the side of the road.

**Chris Gammell:** I think they did that on purpose to make it look kind of like, you know, throwback key. Yeah, exactly.

**Dave Jones:** But it has to be because there's lots of, also there's lots of, you know, power stuff in them. Yeah.

**Chris Gammell:** Creepage and clearance. You want to make sure it's all like, you know, your spacing is good there. So, and it like, so, but the thing that I never understood is do they all work with one another? Like, so you, so you drive up to a generic charger in like a, you know, a Benny's parking lot or something like that.

**Dave Jones:** Uh-huh.

**Chris Gammell:** It, it just, it's pretty guaranteed to work. Like, is it likely that you will not be able to plug in your car to a charger?

**Dave Jones:** It, uh, here, once again, varies on country. The U.S. use a, uh, type one connector.

**Chris Gammell:** Okay.

**Dave Jones:** Whereas we do have them here. There are some like a charge Fox is that like there's networks, like there's companies that have installed like networks of chargers. And some of them use a type one here, but all cars, all EVs sold in this country are, as I said, a type two connector. And that's standard. Almost every car except the Tesla or except EVs sold in the U.S. will be type two. Yeah.

**Chris Gammell:** Like a cross, cross listed kind of, or like an imported car.

**Dave Jones:** Yes. So every car, basically here, here in Australia.

**Chris Gammell:** Oh, you're saying everything, everything. Oh, in the world. You're saying outside of the U.S.

**Dave Jones:** Everything in the world outside of the U.S. The U.S. is a special snowflake. Well, yeah. And Tesla is its own special snowflake. Right. So I can't just go up and plug into a Tesla charging station. Right.

**Chris Gammell:** Okay.

**Dave Jones:** But I should be able to plug into any other charging station I can find because they'll, they'll either be a type. Most will be a type two, but even if it's a type one, I'm going to buy a little adapter. It's just a physical adapter that changes the pin out basically from a type two to a type one.

**Chris Gammell:** Got it.

**Dave Jones:** So it isn't really a big deal. So in your boot, in your trunk, sorry. Or frunk. Don't forget. Frunk. Frunk. My car doesn't have a frunk, unfortunately. Yeah. But it's got a, maybe it's got some room in there. Like people like with EVs, they.

**Chris Gammell:** Just, just, just, just get a drill and just see, see what's in there, Dave. Come on.

**Dave Jones:** They actually custom make, they custom make these little holders that just sit in little voids inside the, you know, inside the, uh, uh, yeah. Engine compartment. Engine in quote marks.

**Chris Gammell:** So, but is there a, yeah. Yeah. The engine compartment. But is there a standardized, like protocol that talks? I mean, I assume it's like a two wire, like an I2C or something like that.

**Dave Jones:** Well, no, it's actually much simpler than that. It's, I, I'm probably going to do a video on this. It's like actually testing this and showing it, uh, as I, as I said, there's two pins on this type two connector. So if you Google, uh, type two EV connector pin out, you'll actually see this. And there's two pins on there. One actually sends out a one, a one kilohertz square wave. And then it basically. Yeah. And that's it. And there's basically a, a resistor in your car. And the value of that resistor load actually tells it, you know, what type, what level it's at.

**Chris Gammell:** So that's more like USB than it is anything else. It sounds like that's like, uh, like USB-C is getting more, like it's really current driven these days with like USB-C. It's complicated. But like, but, uh, yeah.

**Dave Jones:** The older USB. Yeah. Yeah. You have, you have the resistor divider thing.

**Chris Gammell:** Pull down, pull up, whatever, you know? Yeah.

**Dave Jones:** Yep. And it's a similar sort of thing. And I think there's a diode involved as well, but that's basically it. There's a, a resistor and a diode and a one kilohertz signal. And it's like, yep, that's, that's basically it.

**Chris Gammell:** I mean, I guess it's good to keep it simple like that, but you know, eventually they're going to layer more and more stuff on top of it. I'm sure.

**Dave Jones:** Maybe. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** I don't know what the Tesla one does. I don't know the protocol for the Tesla one. Tesla has its own special snowflake, but everything else. Yeah. Pretty much standard. As long as you have the cable for it, as long as you have the physical, because some charging stations you pull up will have the cable attached. And then if it's a type two, you just plug that into your car, just like a regular pump, right? Regular petrol pump. But, um, otherwise you've got to carry the cable in your boot. So, you know, it's just a wall outlet socket. Oh yeah, of course.

**Chris Gammell:** You're ready to go.

**Dave Jones:** Yep. So every EV owner will carry around a whole, you know, a few little cables and a type one, type two adapter. Exactly. Yeah. Yeah. Just in case the place you go to doesn't. Just like electronics nerd.

**Chris Gammell:** You know, you just, you never know when you're going to need a, you know, type B, you know, all the different USB C, different types of USB cables you might need. You know, you just got to have them all. Just carry them all with you.

**Dave Jones:** The interesting is, is that, um, some of these, uh, companies like one in Australia, I think is a charge Fox or charge point. I think it might be charge point. Um, they're, they're actually gone under here in Australia, gone under, down under there. Yeah. So I don't know. I have yet to go up to one of their charge points. I think they're now free. I think like until somebody takes over the company, I mean, the things are still there. They're still physically connected, but, uh.

**Chris Gammell:** Yeah. Well, what's the total coverage too? Like, I mean, two spots at every parking lot you go to or.

**Dave Jones:** Oh, no, there, there, there might be one typically. I, I, I haven't done a big survey of the local area, but, uh, sometimes there's two, like in a shopping center or something like that. You'll get, you know, two, two spots. You'll mainly, you might have a two Tesla spots and you might have two regular spots. So, yeah.

**Chris Gammell:** Tesla owners refer to Dave as a normie.

**Dave Jones:** Normie. Yeah. One of those normie EV owners. Right. Oh, bloody Tesla and a special. Yeah. They're literally the only holdout. Like in the entire world. Like Tesla. They're the only manufacturer who. Yeah.

**Chris Gammell:** Well, they're actually on our list too. Uh, I don't know if you saw their battery day stuff, which is, you know.

**Dave Jones:** Yes, I did.

**Chris Gammell:** I did. It's very. Apple esque. It's like, okay guys, we get it. You want to do the presentation. We are. Yeah. No, just one more thing. Okay. However, this was actually an interesting like technical presentation on how they've been changing battery chemistry and all this other stuff. And I'm like, and then the process changes that they're doing. So I was just watching today. I really, you know, I'm not watching EV stuff like Dave is. I'll just say that straight out. I'm sure Dave is much more interested in this. I have no chance of getting EV in the next five years. But this was very interesting. Just talking about, you know, they're talking about new anode types and new cathode types. They're changing the battery format, which is kind of big.

**Dave Jones:** The construction, that's probably the most interesting takeaway. Well, there's two, I think probably two major interesting takeaways. One is, yeah, they're changing the physical cell construction because if you don't know, you know, they're going from an 1865 or 1865. 8540. What is it now?

**Chris Gammell:** 803040 or something like that. Yeah, it's bigger.

**Dave Jones:** 8540. Yep. Which is 8.5 millimeters diameter, but longer or whatever. Yeah. Oh, sorry. 85 millimeters diameter by 65.

**Chris Gammell:** But it seems like they're going to be able to pack it. Okay. Yeah. Yeah. I actually did not know that. The 16850, I didn't realize that was a dimensional thing.

**Dave Jones:** The 18650. Yeah. Yeah. The 18650 is 18 millimeters across by 65.0. That's what the extra zero. Elon Musk said he didn't know what the extra zero meant. The extra zero is a decimal point. It's actually 65.0. So that's why it's 18650. So Tesla are now calling it 1865. Yeah, whatever. Because Elon doesn't like the extra zero. He finds it offensive. So, yep. Whatever. And anyway, so the 18650, right, is a prismatic cell. Like it's a cylinder cell. And if you unwind it, right, it's like a meter long, right? There's a lot of rolled up, you know, there's a lot of rolled up material in there. Which means that the interesting part about that is that in the inner parts, the actual, the current has to flow through that entire one meter roll if it wants to get out to those tabs. Right? So there's extra internal resistance. So there's extra ESR. Then that's going to limit the power you can get out of that battery, right? We're not talking capacity.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? Like the kilowatt hours. We're talking about power, instantaneous power delivery.

**Chris Gammell:** As a quick aside on that. Sorry. I've been doing some battery ordering lately. And it's like, it's interesting just kind of like asking about charge rates and what they can do. And obviously, you know, people are used to like the pouch pack batteries that you're used to just getting. You know, most of the time they're like current limited to like 1C. They just, they say, okay, 1C, your discharge rate is what your charge rate is. And it's basically what you're, you know, you get a 500 million amp hour battery. You get 500 million amps out of this thing. That's what you get. And it's like, you want to start moving up. You know, you either need to have different chemistry in there. You need to have, you need to take off that governor effectively. But it's like, yeah, this is the power delivery stage. This is what Dave's talking about here is basically how much, how much can you get out of it? You've charged it up. It's ready to go. But now you've got to dump a crap load of current into a motor. It's like, now this really matters. Right. And it's like, you know, that's about internal resistance. So there's heat, right. There's heat, temperature rise. There's also, there's the, the wear on the battery. Yeah. Yes.

**Dave Jones:** Yeah. It's a thermal problem. Yeah. Yep. It actually becomes ultimately a thermal issue in terms of the whole system pack. But anyway, so they've designed, I don't know the name of it. Did they give a name to this new cell design? Like it looks like a flower. Like it's got these petals and it's got like multiple.

**Chris Gammell:** So it's, it's a tabless battery and it's got like shingles. Basically they're like overlaying. So basically they're, they're, I think they're like paralleling more stuff effectively. Right. I think. I don't know. We will be linking this in so people can go and watch this stuff because we're getting this very secondhand of course, you know, but yeah.

**Dave Jones:** Yeah. Yeah. So instead of the current going through that one, like if it's, you know, in the center of the cell, it's got to travel that whole meter through that windy, right. The whole windy path to get out this one. It just has to travel the maximum 85 millimeters to get out. That's it. So it's like, yeah. So they can deliver like five times an hour or something. I can't remember the exact number, but yep. Yep. Although, yeah, there was some weird thing on there. Somebody, a few people emailed me about this saying, Hey, they're claiming five times the energy when their other numbers don't back that up. So it's weird. So I don't understand because it's, yeah, they're claiming five times the energy, but only 14% more range or something. So that doesn't add up.

**Chris Gammell:** Oh yeah. I see. I see this. Yeah. Yeah. Five. There's like a big slide.

**Dave Jones:** Anyway, very cool design. Yep. So they're going to manufacture. Yeah. So they're going to manufacture their cells in house. Now these new cells, they're not going to get them from Panasonic, although they'll still buy them from Panasonic and other makers because they just can't. Yeah. Right. They'll get enough cells. They'll just buy them from anywhere. But ultimately Tesla want to manufacture their own cells. And the other interesting part about this is that the anode material is not a wet anode. It's a dryer. They changed the manufacturing process of actually putting this dry powder. Yeah, me too. I'm probably botching this, of course. But the interesting thing is it takes up one, I think, one-tenth or one-twentieth of the factory floor space that the old machines required to actually manufacture this material to actually put the powder onto the alloy. I think the... I think the... It's...

**Chris Gammell:** I think... Well, watching this presentation too, like, you know, the... I don't know the title of the other guy that was up there with you on. But the... It was a very, like, factory capital expenditure. It felt like this was as much like a, hey, investors, keep giving us money because we're going to be building big factories. And by the way, they're cheaper than they would be otherwise. But really, really, we need that money. We're going to issue some crazy bonds and all this financial skullduggery. But we really need your money.

**Dave Jones:** Right. Well, there's... There's an interesting... It's what they didn't say, what they didn't mention that was also interesting. They didn't... I don't know if they either didn't mention it at all or they said they weren't going to do it. But basically, they've implied that they will not be offering charge to... Car to grid charging. So using your car, which has a gigantic battery pack, bigger than any home battery pack, right? Not using your car as a home battery storage, right? So when you drive... Like, so when you park, like, you charge it up, then you can drive out during the day. When you come back, the solar cells charge it and, you know... So you use it as home battery. So that's car to grid technology. Tesla have basically implied or said that they're not going to do that. Whereas a lot of other manufacturers...

**Chris Gammell:** Yeah. Or build your own. They want you to buy a Powerwall. We've talked about that on the show before.

**Dave Jones:** But they also don't want it... Yeah, yeah. But they also don't want to degrade the range either. Like, they don't want, you know, extra cycles out of the... They haven't said as much, but that's sort of implied. There's a reason. You know, there's...

**Chris Gammell:** Sure.

**Dave Jones:** Technical and or business reasons why they... You don't... You will not be able to use your Tesla as a, you know, home power source. Yeah. Which is interesting. Which, as I said, that DC fast charger, that almost connects directly through to the pack. So in theory, cars can, you know, you can extract via those two pins. You can extract the power from that battery.

**Chris Gammell:** It would make sense. I mean, if you were draining down more, though, like, so say your power goes out and now you're, like, draining off your battery. Yeah. Yeah, you're going to have more cycles then, you know, that's... That is problematic. Yeah. Right?

**Dave Jones:** Yes, it is. But, you know, anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** So they said they're not going to go for that, but very cool tech. Yeah. They want to... The interesting... Other interesting takeaway is that they want to be the number one manufacturing company in the world.

**Speaker ?:** Yeah.

**Dave Jones:** Well... Not just cars. Right? Tesla want to be the number one in automated... I mean, that is...

**Chris Gammell:** Yeah, big focus. World-class manufacturing. That's a tall order. Right. That's a real tall order. Yeah.

**Dave Jones:** Yeah. So they'd be almost becoming, like, more of an engineering company rather than just a car company. You know, or a battery company. Or whatever, right? Sure. They're sort of, you know, manufacturing's their thing. That's their big focus.

**Chris Gammell:** Yeah, but I don't know. Like, a lot of other cars... A lot of other car companies are all, you know, vertically integrated in that way, too. It just feels like it's almost a necessity. Like...

**Dave Jones:** Yes, they are. But, you know, Tesla want to level up, though.

**Chris Gammell:** Yeah. Like, more vertical integration. They want to... Yeah, right. They want to mine the ore at some point. Or they want to make the chairs in their factory or something like that.

**Dave Jones:** That's... Well, they actually just bought a lithium mine or something. Or they bought land that has lithium on it. This has happened in the past as well.

**Chris Gammell:** I was just talking to a friend about this. Like, you know, like, the idea of, like... Oh, yes, it has. It's not new. Tektronix, where they said... So, like, when Keith was being bought by Tektronix, or... Maybe you were telling me this. Someone was telling me that, basically, you know, in Tektronix, it was so vertically integrated, you would call down to get your desk built custom. Right? And that's, like... That is too much vertical integration. You know? Like, that's, like, basically... And, like, same thing with Motorola. Like, you know, like, you basically... It makes sense from a... You know, like, you're looking at the books and you're like... You're like, hey, well, we could save even more if we don't have to give this money to the capacitor manufacturer. We're the capacitor manufacturer. But there's a lot of hidden downsides to doing that, right? Just like, you know... Right. Tesla mining and the Tesla mine is going to... Yes. Oh, yeah. It's going to have problems, not insurmountable ones, but usually the reason you're paying that premium to a company that's mining your lithium or making your capacitors or whatever, the, you know, the margin that you pay them is them solving problems for you and, like, being able to shop around. Yeah, exactly. And, like, I feel... The only downside to this sort of thing is that it becomes, like, this endemic... Like, everything's custom. Everything's got to be custom. Not to say they're not already like this because, you know, they're at such scale that it makes sense. Right. But when there's everything so custom, then it starts to be, like... It's this kind of poisonous thought process. Yep. Not poisonous. Poisonous is probably wrong. But it's, you know, like, moving so far away from standardization, it becomes problematic. I just... I believe that in my heart. It's, you know... Yeah.

**Dave Jones:** They're designing their own alloys.

**Chris Gammell:** Sure, sure. Right. And, yeah... Tesla have invented their own alloys. Yeah, from a material science standpoint, like, you're designing batteries. Like, what is the business of batteries? It's, like, okay, it's chemistry and it's material science and it's structural engineering around that explosion that, you know, basically waiting to... The explosion waiting to happen. You're basically trying to contain all that power in one place. Great. Like, that's your business. But, like, mining the materials? Right. Yeah, maybe that's, you know, that's a level of integration that I would probably question. But, like, yeah, that makes sense for them. I just always look at, you know, presentations like this and I always just think about it, like, they're also having... They're also a public company, so they also have to deal with all the other silliness of the markets. And it's, like, that's an undertone here that I was reading into it, of, like, just explaining this stuff so that they keep juicing the stock to keep getting the cheap capital to build these huge-ass plants. You know, like, the Terra Factory, whatever they're calling it. It's like, that is not cheap. That is a huge, huge investment. And, you know, if they don't want to give away more of the company, then they try and do it by pumping up the value and saying, oh, by the way, we can just, you know, trade against this highly inflated stock. And then, you know, hopefully that all works out. I want to... Like, you know, this is great. I want more efficient batteries. This is awesome. This is awesome for us as electronics designers, right? This is super cool, but, like... Yeah, I know. Yeah, it's great. Grains of salt have been taken. Right.

**Dave Jones:** Anyway, it's... We highly recommend that you watch the battery presentation. It is quite fascinating.

**Chris Gammell:** Yeah. Yeah, now, I found a 16-minute cut-down version as well. That is nice. Yeah. Fewer people in their cars honking. Mm-mm.

**Dave Jones:** Yes. Yes, there is a cut-down version. Yep. Because otherwise, it's quite long.

**Chris Gammell:** Yeah. A little culty there, guys. A little bit cultish, you know?

**Dave Jones:** Yep. Yeah, because they had... They didn't... They had audience was people in their Teslas just honking their horns out in a big... See what I'm saying?

**Chris Gammell:** See what I'm saying?

**Dave Jones:** Yeah. ...car parking lot or something. Yeah. Yeah, it's...

**Chris Gammell:** Yeah.

**Dave Jones:** But that's what keeps the money printing machine going. Brr! Yep. No, no. Yeah. It works. Don't knock it. Oh, boy. Anyway, EVs. Yes. I have an electric car. And on Monday, I'm going to look at an electric bus.

**Chris Gammell:** You're going to buy a bus?

**Dave Jones:** No, I'm looking as I'm going to...

**Chris Gammell:** It's getting a bus route.

**Dave Jones:** Yep.

**Chris Gammell:** Cool. That's great.

**Dave Jones:** Going to... Yeah, yeah. We're trialing them here in Sydney. Cool. And I'm going to go check one out.

**Chris Gammell:** Yeah. Yep. I saw one go buy in Chicago that it's, you know, like, it's just, like, marked on the side that's an electric bus. And it's like, oh, okay. You know, but...

**Dave Jones:** Right.

**Chris Gammell:** I'm sure it makes sense. Especially, you know, non-COVID times when people are actually riding buses. But, like, you know, yeah. Yeah.

**Dave Jones:** You know what the interesting thing about owning an EV is? That you instantly notice?

**Chris Gammell:** That you can't stop talking about it?

**Dave Jones:** Yeah, probably.

**Chris Gammell:** By the way, are you going to get a custom plate that says EEV car? Because you need to get something like that, right? I mean, it's, like, in your title of your blog.

**Dave Jones:** I know. Maybe. We'll see. Because that would technically make me a wanker, you see. I mean... Here in Australia, they're called wanker plates. Oh, yeah, yeah, yeah. You're right. Yeah.

**Chris Gammell:** Vanity plates are true to name, for sure. Or wanker plates. Yeah. Yeah.

**Dave Jones:** Yep. That may happen.

**Chris Gammell:** Anyways, what were you saying, though? You were saying, what do you notice as an EV owner?

**Dave Jones:** Not just me, but... All the people that you talk to. Also notice the same thing. Yes. Notice the same thing. Is the lack of smell. Oh, interesting. As in, like, it's... Yeah. So, like, this is EEV blog now. I'll call our other car the stinky car. The stinky car. And she doesn't like driving the stinky car. Because it stinks, right? Because you don't notice that. You just learn to ignore the smell of, you know... Like, even when you just sit in there idle, even outside, the fumes actually come back and get inside the car. You know, you're taking forever to get the kids inside the car and the engine's running and the car's just filling up with fumes because it's, you know... Yeah.

**Chris Gammell:** I mean, I park in a parking garage and, like, that traps it all in. So, yeah, for sure. Yeah.

**Dave Jones:** Yeah. But you just learn to ignore that. But when you don't have that, it's like, oh, wow. And then when you suddenly go back to it...

**Chris Gammell:** Oh, yeah.

**Dave Jones:** You go, wow. You know, it's... Yeah. It's like being around non-smokers and then... That's true. Suddenly somebody, you know, a smoker enters. It's like... Yeah. You know?

**Chris Gammell:** Yeah. Like, I remember going out to bars when I was younger and it was still, like, you know, still people smoked at bars. And it was like, yeah, whatever. You know, you come home and your clothes reek. And now, like, you go out to bar and it was like that, you know, like... It's like, holy crap. Yeah. Really, you notice it. Yeah.

**Dave Jones:** I can remember when you used to be able to smoke on planes and trains and buses. Oh, my God. Yeah. Yeah. Yeah. And cinemas, you know? Yeah. Like, you go into cinema, watch a movie and you...

**Chris Gammell:** Yeah.

**Dave Jones:** Wow. People are... Yeah. Puffing away.

**Chris Gammell:** Times, they are changing.

**Dave Jones:** And, yeah, so it's a similar shock like that. When you go, you know, you've been using your EV for a while and, yeah, you suddenly get, yep, I can smell all these other cars. Gross. So, anyway, very cool.

**Chris Gammell:** That is cool. You know what else stinks, Dave? What? Is firmware updates.

**Dave Jones:** Yeah. Well, they can.

**Chris Gammell:** Yeah. I've been...

**Dave Jones:** Firmware updates can be done nicely or they can be... You know, I've been...

**Chris Gammell:** You know, ruin your day. ...plan... So, you know, I got my new board. I think we talked about that a little bit on here. Yes. Yeah, we have. But I've been playing with OTA DFUs. You ever done one of those? No. Me neither.

**Dave Jones:** I've... Okay. But I can guess what it means. It's over the air. Yep. DFU, which is your regular USB. Device firmware update. Yep. Device firmware update. Yep.

**Chris Gammell:** Yeah. So, there's like a bootloader. I've been asking friends for help on this stuff. But there's like a bootloader that you can put in there, basically. And if it's already got a... So, this is an NRF52 840. And if it's got a soft device in there that, you know, is the battery... Or, sorry, is the Bluetooth control chip thingy. Basically, you can use the NRF Connect app and load a new piece of firmware in there. Which is what I'm hoping to do so that I can, like, put it in a case. And, you know, you don't have to crack it open or anything like that. So, yeah. Right. It's a... This is a strange new world for me. There's that one. And then there was... That was one stinky thing with firmware. And the other one was Zephyr. You heard about Zephyr? Do you know what Zephyr is?

**Dave Jones:** I've heard of it.

**Chris Gammell:** Yeah.

**Dave Jones:** Remind me.

**Chris Gammell:** I don't know if we've talked about it specifically on the show. Maybe I mentioned it last time on the show. But Zephyr is... So, I think it was Wind River? I think, yeah. Wind River was the one who started it. It used to be called something else. But they got bought by Intel. They were, like, a firmware shop. This is, like, a real-time operating system that they developed. And then the Linux Foundation took it over. And now it's, like, this kind of cross-platform Linux-esque real-time operating system. So, basically, you can pull in lots of different software development packages or SDKs. And then you can build, like, this kind of higher-level RTOS that's more like Linux. And it's supposedly easy. But I have not found... I have not gotten to that point yet. So... But the promise is that, like, you know, implementing Bluetooth is like a hash include instead of a writing low-level interactions with APIs that are kind of opaque. So, that's the thought. Right now, I've basically spent, like, you know, a day and a half trying to get the toolchain working and finally got that. Of course. But, you know... Yep.

**Dave Jones:** Yep. Yeah.

**Chris Gammell:** So, yeah. It's been a fun bit of time.

**Dave Jones:** I don't have time for things that, you know, technologies like that that muck me around now. I mean, like, we live in a world where you expect those sort of things to just work. You know? Like, there's so many choices out there that...

**Chris Gammell:** But I think this is... So, the reason I... Yeah. And I would agree with you on that normally. But I think the reason that I'm doing this is because it's kind of, like, front-loaded with pain. Mostly... Right. Because it's a different way than, like, even using the other Nordic stuff, like the, you know, Sega Embedded Studio or even GCC and stuff. It's a little bit different than that whole, like, flow of doing things. But once you do it, apparently it's, like, include a file system. Include Bluetooth. Include this other stuff. And it's, like... And then that stuff just kind of works because all the SDK stuff that's already underneath the hood is supposedly working. And there's, like, APIs down to that stuff. So, like, that is the reason to do it, I think. But I am... I am not there yet.

**Dave Jones:** Right.

**Chris Gammell:** And some of it also is... You don't like Linux in the first place. And I didn't like Linux those day and a half that I was doing that stuff. But it was really... It was my system that was the problem because it was, like, my whole Linux, you know, part of my computer crashed. And it doesn't really work anymore. I basically, like, you know, fussed around with it so much that it just doesn't work anymore. So, I'm now running a VMware virtual box... Or, sorry, VMware virtual machine, rather. And that hosts Ubuntu. And then I just pass through whatever USB cable I'm plugging into that. And then the virtual machine has all of the Linux-based toolchain on it. And then that just easily talks to the board. And that works well enough for now.

**Dave Jones:** I have to correct you there. It's not like I don't like Linux. It's just that I don't use it.

**Chris Gammell:** Yeah. Right. Well, yeah. That's a better reason.

**Dave Jones:** Like, I simply have no need for... I have no need to use it. So, I don't use it. Right.

**Chris Gammell:** And I would normally say that. And, like, I looked... You know, and so, like, a lot of these tools are cross-platform, which is great. And the toolchain works for Zephyr. But the SDK is not available in Windows. So, I was like, okay. I don't know how that really works. So, if it's not available in Windows, how would we use the tools? You know, like, all the stuff that you're going to build is going to use the SDK anyway. So, yeah. So, I'm slowly learning. But I honestly, like, after years of running websites, like, and, you know, that kind of stuff, like, I feel completely comfortable in, you know, on the command line in Linux. I feel fine with that stuff. I kind of prefer it most days. Like, I was even using Windows subsystem for Linux as well, which is, like, it's, like, basically in Ubuntu or, you know, a little Linux instance that's directly installed in Windows. It's, like, a, you know, virtualized instance that's directly installed in Windows and you can, like, access Windows programs from it and stuff, too, which is kind of cool. But it doesn't talk to the USB. So, that's problematic. So.

**Dave Jones:** Ugh. It's all problematic as far as I'm concerned. It's all, you know, everything you were saying there is, like, oh, why? You know, it's just.

**Chris Gammell:** Well, I mean, it's just to access higher level functions than I'm used to, right? It's not, like. Right. I'm not just, like, flipping bits anymore, like, talking to Bluetooth or talking to cellular stuff or creating file systems. Like, you could do that all from scratch, but that would take even longer. So, this is kind of the price you pay. You're kind of moving up a level into the system. I will say I'm reading a really cool book on real-time operating systems that I will heartily recommend if you're interested in learning about them. And there's. I haven't been following along with the book with the dev board, but there actually is a whole bunch of, like, examples you can go and run. On this STM32F7 board. And so, it's using free RTOS. You basically, there's examples. But even just the book by itself is, like, a really, you know, comparing it to, like, you know, other RTOS stuff that I've read before. Like, I had read, like, the Micrium Micro 2 OS book a long time ago. You know, just, like, what is a mutex? What is a semaphore? Like, oh, what are all these things for? How do they actually interact? And, like, you know, like, round robin scheduling. All the things that, like, you know, you'd hear about if you were looking at an RTOS. Like, it actually starts to make sense. He, like, he shows timing diagrams. And it's really quite a good book. So, I've been reading that and enjoying it. Let me pull up the name of it here.

**Dave Jones:** Once again, RTOS is one of those things that I would consider that should just work these days. Like, I can remember using an RTOS for the Rabbit 2000 processor way back in the day. And their big claim to fame was that it just worked. You didn't have to know about RTOSs. Don't worry about it. Just plug it in.

**Chris Gammell:** Just follow this structure. And you want to start a task. And you just do this one command. And that starts a task. And I think that's true, though. I think that's true with a lot of this stuff, right? So, this is for RTOS, right? Now owned by Amazon. I don't know if you knew that.

**Dave Jones:** Right. No, I will.

**Chris Gammell:** Oh, yeah. They were bought by Amazon. I was like, I knew it was like integrated with Amazon and AWS. But I didn't realize that Amazon actually bought the company that develops free RTOS. So, it's like free asterisk RTOS. But it's still like, you know, still open source. And so, you could still strip out all the other stuff if you want to.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. And it, like, for a dum-dum like me, right? I'm just like, also, I could go and start a task and do all this stuff. I think what it really comes down to is like, what are you going to do when you're troubleshooting? Right? That's the, that's when the rubber hits the road. Because even with the rabbit, like, it works great until it doesn't. Right? You know, like. Oh, yeah. No, of course. So, you schedule too many tasks or, you know, you have a conflict or task inversion. Yeah. Is that the priority inversion? That's another one I learned about.

**Dave Jones:** Yes.

**Chris Gammell:** Yeah. So, I mean, yeah. And they've been around for a long time. But it's interesting that I would, I would have expected that there would be like consolidation in the market. But I always, you know, if you read like Jack Gansel's newsletter, which we heartily recommend in this, on this show, you know, he does like a survey every year and it's just so like, like a whole bunch of people are like creating their own, which is like, that's kind of crazy, you know? Anyway.

**Dave Jones:** So, how many, like, it's like the standards, like that XKCD standards thing. Yeah, that's right. 15. Yeah. Yeah. Yeah. We've got 14 standards. Let's create a new standard to rule them all.

**Chris Gammell:** Right, right.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. I think there's that. I think also like, you know, so like a new thing, like Zephyr comes out, it's the new, the new hot thing, whatever. Right. But then, you know, more people get fractured off into that. But, you know, the guy that's working on the thing that he custom designed 20 years ago, and he's still maintaining, like, he's not going to, he's not moving that over to Zephyr or, you know, free RTOS or whatever. He's just going to keep doing the thing because he has to, you know? And I also learned about like, I didn't quite understand how, like the whole idea of an RTOS is like, you actually like, each task has its own stack. Did you know that?

**Dave Jones:** Yes.

**Chris Gammell:** I didn't know that. So like, that was kind of like a, that was like a very.

**Dave Jones:** That's bread and butter stuff.

**Chris Gammell:** Yeah, that, yeah, exactly. So that's like the level that I was at when I was, you know, starting. Right, okay. The book is called, by the way, it's called Hands-on RTOS with Microcontrollers. So using free RTOS, STM32s, and SEGGER. So highly recommend. And the board itself, I think, was like 40 bucks. So the book is 30 and the board's 40. So like 70. Nice. Yeah, that's nice. So, yeah, you know, learning. Learning.

**Dave Jones:** Awesome.

**Chris Gammell:** Yeah.

**Dave Jones:** Guess what they learned in, you mentioned it earlier. In some little village. Oh, yeah.

**Chris Gammell:** I saw you post this. This is great.

**Dave Jones:** Where is it? Oh, this is great. They learned about EMI testing.

**Speaker ?:** Amen.

**Dave Jones:** Exactly. If you don't know, it's made all the news. Everyone was free to our news because it's just hilarious. There's this little village. Which country is it?

**Chris Gammell:** Is it Wales?

**Dave Jones:** Wales, is it? Okay. Yeah. There's this little tiny village, right? And for 18 months at 7 a.m. every morning, the whole village's internet would go down.

**Chris Gammell:** And I couldn't figure out why. You know, that's a tough thing too, because you have this like very strong signal of like 7 a.m. Why is it 7 a.m.? What's happening at 7 a.m.?

**Dave Jones:** Why is it 7 a.m.? Yeah. It turns out some old guy who has an old telly, an old, you know, is it a valve telly? I don't know. But, you know, he's got an old television and he switches it on at 7 a.m. And it obviously was not EMI compliant, TMC compliant. And it would somehow take out, yeah, the, you know, the internet connection they had to go into the village or something.

**Chris Gammell:** The TV was found to be emitting a single high-level impulse noise or shine. Apparently that's the proper, probably shine noise event, right? For the E at the end. But I like that. There's like a specific acronym for this. Single, single high, high-level impulse noise event.

**Dave Jones:** I don't think I've ever heard of that.

**Chris Gammell:** I haven't either. That might be like people that are like testing for interference like this, right? But.

**Dave Jones:** Oh, yeah, yeah, I'm sure.

**Chris Gammell:** But it's basically a TV that's sending out an EMP, you know?

**Dave Jones:** Right. So for 18 months, 18 months. Wow. Like I've had these sort of issues before. I'm sure I've mentioned this to donkeys years ago. But I was like troubleshooting a long-term data logger that we designed, right?

**Chris Gammell:** Oh, man. And yeah, did I mention this? I'm sure you have. But I just, you know, long-term, long-term testing in general is like, yeah, I started to get, you know, my eyes start to cross, you know?

**Dave Jones:** So anyway, it would like, it would corrupt. So I would leave it logging overnight. And then it would corrupt, like I think it reset or something, you know, it did something, did something weird. And it was like, we got to the point where like, I couldn't force it to do this, but I knew it happened overnight. Right. So, you know, like I set up, so I was able to like log to synchronize like a, you know, the time and. Yeah. Yeah.

**Chris Gammell:** Like an ADC capture or something like that or what?

**Dave Jones:** Yeah. And I, no, it was part of the, well, I was able to log it on the scope as well. I was able to get some probes hooked up and I was able to get, you know, some things as well as cross correlate to the logger because the logger had time date as well.

**Chris Gammell:** Yeah. I just remembered what the punchline is to this one. I'm going to let you finish. You have told it before, of course, but like, yeah, I mean, this is a, this is a great example, I think.

**Dave Jones:** Yeah. 11. I think it was 11 o'clock at night.

**Chris Gammell:** Yeah.

**Dave Jones:** This thing would happen. Right. So like, so I decided to stay there at 11 o'clock or something. And it was like all the, um, the air con systems would all like start up and do something weird at, at 11 o'clock. And that was causing, so I still could not figure out the actual impulse where it was or how it was getting in. It was like, Oh, holy. Yeah.

**Chris Gammell:** Is it power line or is it, you know, the, the chill of the, you know, the air or something like that. Right.

**Dave Jones:** Yeah. I, I'm not sure whether it was like, you know, power coupled or whatnot. I can't remember the details, but yeah.

**Chris Gammell:** And it would, it was like staying up as like a ghost hunter, like Charlie Brown, like waiting for the great pumpkin, you know, like you're sitting there just like eating chocolate bars, waiting for this event to happen. You know?

**Dave Jones:** Yep. And this is where I discovered one of my very old videos back in the old lab was, uh, the famous chair thing where you'd hop up off the chair and it'd generate a static impulse.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Yeah. And that, that, this is in my famous hand photo.

**Chris Gammell:** Yeah. Right. Right. Right. You're at the camera. That's your like logo. Yeah.

**Dave Jones:** That, that thing that I'm testing there on the bench. That's the actual thing.

**Chris Gammell:** Oh, interesting.

**Dave Jones:** That's the actual thing that was getting upset. And that's where I discovered the chair thing. So the chair would generate an electromagnet, uh, would, you know, generate static. Like a static probably, right? Yeah. Yeah. Well, electrostatic. And that would couple into the scope probe. And then they'd couple into the grounding system, the scope and cause an impulse. So you can make your scope trigger.

**Chris Gammell:** Oh yeah.

**Dave Jones:** By doing that. And, you know, so I was sitting there for ages, you know, go like, you know, trying to log this fault and, and I'd hop out of my chair and come back and it had triggered. And I'm going like, what the hell? It never like, it's the old watch, watch pot never. Yeah. It's the old watch pot never boils. Right. It always triggered when I wasn't there. It turns out it was triggering when I stood up from my chair was generating a static impulse, but that, that was different. That was on top of this 11 PM thing, you know? So, oh, it was just, that's super frustrating.

**Chris Gammell:** Yep.

**Dave Jones:** Long-term logging sucks.

**Chris Gammell:** Oh, it totally does. Yeah. And I think it's like, it's a great example. I think it's a great example of like sampling problems, right. Of like in general, because what you really want to do is like, you want to capture every event. You're like, all right, I know this is probably happening over the span of, you know, one, one thousandth of a second. So I'm going to capture a thousand events a second. Right. But I need to do that for 25 days. That data is just like so crazy. And so like, that's, that's it. That's the reason triggering exists because you have to have some other way to throw away, you know, once your buffer's full, you need to throw away all the crap that you collected that is not relevant because you've already determined that it's, you know, that it's, you got to capture more data. So you got to throw out the old data, you know, it's like, and, or just capture everything and you just captured a whole ton of, you know, worthless data effectively until you capture that one event.

**Dave Jones:** That's what triggering is for. And that's why every scope by default has 50% pre and post triggering and every logic analyzer 50% because you want to see what happened before that trigger event, you know, as well as after. So yeah.

**Chris Gammell:** Electronics, you know? Yeah.

**Dave Jones:** Anyway, poor bastards in that village, 18 months, 18 months.

**Chris Gammell:** You can imagine that's a long time to let that go. I feel like that's like a slow pace of life kind of thing, you know, like I don't have internet every morning for 18 months. Like I'm doing something, man, at least going to the coffee shop to get internet there.

**Dave Jones:** You know, like I guess this was way, way back when I first moved into our house, right? We had a DSL internet, right? Yeah. I had that in the lab here too, to start off with. Right. And it would, it'd be flaky as all buggery. Right. And it was just absolutely atrocious connection. And we had them out so many times to look at this. Why is it just crap? You know, it'd come and go and it would do all sorts of stuff. And like, we were like, it was like a two or three year battle for them to try and figure out what's wrong. It turns out all of the cables were rotted in our, our, our, our pair was rotted in the street because the, the, the pit would fill up with water at the top of the street and that would leak its way down the wires. And, and yeah, our, our particular pair was just completely rotted. And so I was making like intermittent connection that have rust in there, which is acting as little, acting as little, uh, point diodes and you know, it just gets really weird. Right. Right. It's like, oh, so that's why it was just so flaky. Wow. And, um, yeah. So they had to like just run, run new wire then. Yeah. Yeah. They had to run new, new cabling.

**Chris Gammell:** That's crazy.

**Dave Jones:** So yeah. It's like, oh God. But yeah, every time they tested it, it'd go, oh, it seems fine.

**Chris Gammell:** Right. Right. Exactly. Yeah. The diagnostics is different than, right.

**Dave Jones:** Yeah. Yeah. Yeah. And it'd just drift in and out, you know, when it, you know, extra moisture or whatever. Thermal.

**Chris Gammell:** It's really, really hard to tell like a technician to be like, can you just stay here for like the next three days and just, you know, like see what I'm dealing with. Monitor it.

**Dave Jones:** Yeah. Exactly. Yeah. So, uh, it's like the demo effect.

**Chris Gammell:** It's like the really, really bad demo effect, you know, like it's not going to happen when you need it to happen.

**Dave Jones:** Uh-huh. So that's what I picture happened here. You know, the poor tech that came out, you know, 10 times to the village. Cause there's probably no tech in the village. You probably had to come from the big smoke.

**Chris Gammell:** Oh, that's true. Right. And why would he get there at seven in the morning? Right. He would get there at nine in the morning because he's got to drive there. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** And it was like, and I can, that's why it took 18 months to find this mongrel. So that's great. So anyway, uh, love it. So yes, if you've got a similar story, leave it in the comments. Yeah.

**Chris Gammell:** Oh, a couple of links that I wanted to call out before we end. Uh, one is past guests of the show, Bunny Huang and the Sejito, uh, Kosagi, his company, they're doing a, uh, like an open source mobile phone without a, without a, uh, it's like basically a platform. So it's called the precursor. It's got a risk five on it. It's got, I think, a FPGA on there too. That's cool looking. It's got a screen. Basically, it's going to be like a base level platform for doing, building other things onto that looks like a phone. So that's kind of cool. Right. Got it. Yeah.

**Dave Jones:** Yep. Does it actually have any phone hardware in it?

**Chris Gammell:** It doesn't have it. It's got a wifi. It doesn't, it doesn't have a modem or a cell. Okay. I got it. Right.

**Dave Jones:** Got it. Yep.

**Chris Gammell:** But you could always, you could tether it to a MiFi or some similar, right. If you really wanted to, it's very privacy focused. I'm not sure. I'm sure you'd have to kind of, you know, if you wanted to put actual cell hardware on there, you'd have to be a little, you're basically on someone's network then. And yeah. A little less trusted, I think.

**Dave Jones:** Right. Got it. Very cool.

**Chris Gammell:** The makers, this is kind of a cool thing. The smart module. So this is the quick tell, the guys that make the modem that I use, the cellular modem that I use, they have a new module coming out. That's basically like a Android on a SOM effectively. So like, it's like a plugin module and the whole thing, it's like a whole Linux Android based device that just plugs in. It's pretty cool looking. Again, this one doesn't have any cellular on it, but it's got like kind of, it could do like 4k monitor, six cameras, like a bunch of, wow. Yeah. It's like a bunch of stuff. It's really cool looking. Yeah. I don't know how much it costs, but I saw the press release. I like quick tell. It's just, it's an interesting idea. Like I'm always looking for these like Linux plugin systems because they're, you know, like for consulting, especially like, I love to be able to just like walk up, plug into something like this and it just, you know, then you hand it off to a software person. And then I do the, the other side of it where it's like, you're, you know, you're making the device that it has to talk to it's talking to the motor controllers or the power, you know, the power stuff that it needs to talk to. And that's not really out there yet, but so I would love this trend to continue. Maybe there's other stuff. I would love to hear if there's other modules out there like this, but industrial Linux type computers that are not a Raspberry Pi. It's actually more like a plugin ready to go ship it with your hardware and you can buy it easily. So if people know about that, I'd love to hear about it, but this is, this is an interesting new one, especially because it's Android based. I think it's, they're targeting like kiosks and stuff like that. So yeah. And then the last one I wanted to mention was the 108 rare and bizarre media types. People have probably seen this. It's got like 1.3 million views, but this is just amazing. It's the eight bit guy. He goes through like every type of wonky disc, magnetic tape, like all, all of the different things. It is a great, great video. So yeah. Yeah. It's great.

**Dave Jones:** Yeah. Yep. Terrific. Yeah. Oh, love it.

**Chris Gammell:** Great.

**Dave Jones:** That's it.

**Chris Gammell:** How did I sound Dave? You know, I have a brand new nose.

**Dave Jones:** What?

**Chris Gammell:** Yeah. I had a nose surgery. I, what? Where I was once deviated. I am no longer deviated.

**Dave Jones:** Oh, okay. Yeah. Yeah. You wouldn't hurt.

**Chris Gammell:** It was last week. Yeah. I was during the day after the surgery. I was actually a little, a little bit on some drugs last week, but it worked out fine.

**Dave Jones:** Got it.

**Chris Gammell:** I talked to, I talked to her, Suzanne, our wonderful editor, and she's like, yeah, you didn't, you didn't sound too bad. I was like, okay, I feel good pushing this out. But it was like, it was like 24 hours after I had come out of like general anesthesia for the first time ever. So dedication, man. That's what I'm, that's what I'm about. You know, the amp hour doesn't sleep.

**Dave Jones:** Yeah. Took one for the team.

**Chris Gammell:** That's right. All right. Yeah.

**Dave Jones:** But so you were supposed to sound different. Is that now? No, no, no.

**Chris Gammell:** I just, my, my, my nose is all clear now. So I was wondering if my radio voice has become more radio-y.

**Dave Jones:** Yeah. I was, I was going to say that, like, how would that change your voice? I mean, that's.

**Chris Gammell:** Well, you know, you know how it's like some people are called nasal, you know, it's because your sound gets caught in your, in your sinuses and your, your nasal passage. Cause you don't have airflow going through there. And I have tons of airflow now. So I don't know, maybe I just sound angelic.

**Dave Jones:** Oh, you know. Oh, okay. So they didn't tell you that your voice might.

**Chris Gammell:** No, no. This is just. It might sound. This is just me bantering really, you know.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. No worries.

**Chris Gammell:** Do I sound better? Dave, come on. Just say yes.

**Dave Jones:** You sound normal.

**Chris Gammell:** Yeah. All right. Fine. I'll take it.

**Dave Jones:** Normal yank. Yeah. Yeah. It's like, yeah. Oh boy. Anyway, that's great. Yeah. Yep. That's good. So does that help you sleep better and stuff? Yeah. That's the idea. Yeah.

**Chris Gammell:** You're right. Sleep like a baby.

**Dave Jones:** Got it. Why? Why didn't? Why now? In your advanced old age.

**Chris Gammell:** Because I grind my teeth and you can't get a, you can't get a mouth guard until you've, until you can breathe through your nose. You can get a mouth guard if you can, you can't breathe through your nose, but it's a lot better if you have a mouth guard so you don't grind your teeth if you can breathe through your nose. And so I had to get my nose fixed so I could fix my teeth.

**Dave Jones:** Yeah. Okay.

**Chris Gammell:** Falling apart over here, Dave. Makes no sense, but sure. Okay.

**Dave Jones:** Well. Yep. It sounds like I'm doing better than you are.

**Chris Gammell:** Yeah. I'm late 30s going on early 80s.

**Dave Jones:** Oh boy.

**Chris Gammell:** Yeah.

**Dave Jones:** Excellent. All right. Well, that's it. We managed to survive this show. Back in the old lab with a cobbled together mic and empty room so I probably sound like shit. Yeah. You sound great.

**Chris Gammell:** You sound great. Yeah. See how easy that was? Fantastic. Thank you very much. Talk to you next week. Bye. Bye. This episode was produced by Analog Life LLC and brought to you today by our patrons. Join today at patreon.com slash the amp hour to get access to a private discord channel and discounts on amp hour swag. We'd like to welcome our first corporate sponsor, Bino. Jonathan Giorgino is the founder of Bino and was on episode 461.

**Chris Gammell:** Bye.

**Chris Gammell:** Bye.

**Speaker ?:** Thank you.
