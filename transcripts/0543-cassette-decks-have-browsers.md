---
episode: 543
title: Cassette decks have browsers?
url: https://theamphour.com/543-cassette-decks-have-browsers/
---

**Chris Gammell:** This is The Amp Hour Podcast. Release May 23rd, 2020. Episode 543. Cassette decks have browsers?

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Looking at some interesting stuff in the marketplace. You know, I'm trying to distract myself from parts sourcing. I'm sure we won't talk about that at all. No, no, no. Yeah, right. Yeah, yeah, yeah. But I've been watching the AirTag teardowns. Have you been watching those at all?

**Dave Jones:** I haven't. I've seen them pop up, but I have not watched them. That one uses the Nordic chipset, doesn't it?

**Chris Gammell:** Yeah. NRF 52832, which is another reason I can't get that part.

**Dave Jones:** If those who don't know, this is an Apple fruity gadget.

**Chris Gammell:** That's right. Yeah. So it's like a little, it's basically like a kind of, it's like a Tile, basically. Tile is another company that does this sort of thing. I've never heard of them. Where basically it's a. No. Oh, no? Oh, interesting. Okay. Yeah, Tile is like an asset tracker where it's Bluetooth based. And the idea was because you're, the broadcasting is like a beacon. As far as I understand it, don't, you know, don't at me. As far as I understand it, because it's broadcasting like a beacon, you know, like you can open up the Bluetooth menu on your, on your phone and it'll show whatever device is around. Basically the app on your phone watches for all these beacons that are happening as you're walking down the street. And if someone reports to the network, Hey, you know, my, I lost my suitcase and it had beacon ID. Oh, right. All right. Okay. Your phone scan, it goes by, you know, the train station, scans it, sees it, and then it tags it because your phone has a GPS on it. Let's see. The idea being that you, you keep the per device cost down because, you know, Bluetooth chips are cheap and cheapest chips, as I believe some say. And, uh, uh, and low power. And, you know, basically it can last for a long time as like a, as a sealed package. And then as people, it's basically kind of wisdom of the crowds kind of idea where, because you have so many people with phones using this app. Supposedly using this app. Yeah. Well, yeah. But if you want to be part of the ecosystem, yeah, there's definitely a network effect, but if you want to be part of the ecosystem, you also have to be willing to have your phone scanning for other tags. I believe this is a similar thing with that Apple's doing maybe longer distance now because Bluetooth long ranges.

**Dave Jones:** I thought though, cause this comes into the Australian COVID tracing app, which was an epic failure. And I thought this didn't work on Apple's cause this is, if you don't know, Australian had this COVID tracing app, you know, back like a year ago during the, you know, May or something last year, peak of the pandemic. Everyone's going to, we're going to force you to use this COVID tracing app. Everyone downloaded. Otherwise we'll, you know, yeah. Papers, please. Yeah. Anyway. So, yeah. And like everyone went near growing something, you know, quite a few people install it, but then people realized that it doesn't actually work on Apple devices because it, well, the only, cause it used a Bluetooth, right? So the whole idea is that everyone has this app. It talks in the background and it's sharing your location with every, you know, it's sharing your location constantly and other people. And if you come within, you know, 10 feet of a COVID positive person or something, then it'll warn you or, you know, it's good. Like, and then you can track, you know, you can do, you know, COVID tracing and stuff like that as well. Right.

**Chris Gammell:** Right. And it's supposed to be, it's supposed to be like rotating codes too. So at least the US version I'd heard about is supposed to be.

**Dave Jones:** Yeah. Something like that. And it's supposed to store, you know, and they went to M team effort to try and prove that. No, we're not tracking you. You know, it's like, that's the whole idea of the app. But no, we're not storing the data. Trust us. You know, anyway, the problem was, is that on Apple, on Apple iOS, it's so secure that it would only work if the app was not only running, but had focus. So if you like, you know, if your phone went into, you know, like actually goes into your pocket and it goes into lock, it doesn't work anymore. The Bluetooth, constant Bluetooth thing didn't work anymore. It was a security feature of Apple and it was a complete and epic failure. And it simply did not work. Right. Yeah. And like, and they wasted, you know, tens of millions of dollars on this boondoggle. And yeah. And somebody could have told them right off the bat that, sorry, this doesn't work on Apple devices. And of course, you know, half the population have this stupid fruity gadget. So yeah. So I'm, I'm, I'm surprised they're doing the same. They're trying to do essentially the same thing here. Unless Apple have updated iOS that allows this.

**Chris Gammell:** Well, I don't know if it's the same thing, but well, it's got to be the same thing.

**Dave Jones:** I mean, right. You're, you're running the app. It's in the background. You don't want to leave this app running in the foreground all the time and leave your phone unlocked. Right. This is, that's just dumb.

**Chris Gammell:** I think if you had lower level control though, of the actual iPhone, you could probably, you know, have.

**Dave Jones:** You can, but I thought it doesn't let you. That's the whole idea. It's actually secure.

**Chris Gammell:** Well, it's Apple. This is an Apple device though. So like, you know, like Apple's looking for their own. So like, that's what I mean. Like, yeah, I could see that with like a third party developer.

**Dave Jones:** No, I thought you were talking about this other one, the slate thing or whatever tile thing or whatever it is. Oh, it's tile. Tile.

**Chris Gammell:** Yeah. I'm not sure about that one. Right. Maybe, maybe they were better programming. I don't know. Like I figured, I mean, I would figure that you would be able to, you know, wake up the phone even and have focus. But maybe also that was a previous versions of, of iPhone. So it could also be that.

**Dave Jones:** Oh, I think they did do updates to it or something event. Apple did eventually kind of, you know, change things to make it possible somehow. I don't know. Anyway. Yeah. Tile. Anyway, it's a thing. Yeah. It's a scan Bluetooth scanning thing. Right. Yawn.

**Chris Gammell:** It's not just Bluetooth though. So it's also wide band. Right. So basically that's a little different. So the stuff that's in here, I'm just on the iFixit. I'll put this in.

**Dave Jones:** What do you mean by iBand? In the notes as well. Well, what do you mean by wide, wide, wide band? What do you mean?

**Chris Gammell:** They have a special chip set for that. I have no idea. Honestly. Let's see. What's it?

**Dave Jones:** It's searching for police radios or something. I mean, what do you like, you know, why do like wide band to me means, you know, it's searching the entire spectrum. Like why?

**Chris Gammell:** This says for spatial awareness. That's what the U1 chip is for. So I'm not sure how that would be used in an AirTag. What? I don't know.

**Dave Jones:** I don't get it.

**Chris Gammell:** Like wide band is usually. So like, that's like a high, like the high frequency, the gigahertz transceivers and stuff like that. You would use that if you were, I'm not sure about the Apple one, but other ones like, like in your car, it's wide band often for proximity detection. Right. So, you know how, like when you are merging into a new lane and the little light goes off the light on your side mirror, that's because there's like a 26 gigahertz wide band, ultra wide band transceiver on there basically is just spitting. And then seeing what bounces. Right.

**Dave Jones:** Right. Okay. Yeah. Got it.

**Chris Gammell:** I'm not sure how it would be used here, but yeah. Yeah.

**Dave Jones:** All right.

**Chris Gammell:** Interesting what they've got going on. And so I'm guessing there's other sensor style things that are on here, but the main thing I believe is that NRF 52832, which is, you know, Bluetooth transceiver, although, and it's got NFC as well, right? I've used that. If you've got the developer kit, the 832 DK is like the board that everybody kind of has as the basis of it. All right. Yeah. Yeah. So there's a couple of DC to DC converters. What else is on here? Oh, a rail to rail IO op amp. I sent this link to you as well in the chat. So if you wanted to see this thing and then an audio amplifier as well, that's interesting. So basically this is a little bit more of a involved sensor device, but basically people are, you know, reverse engineering it. This is, that's how I started to see it. Colin O'Flynn and it was sharing a bunch of stuff about this. People basically getting at the JTAG, dumping the firmware and you know, it's a little Bluetooth chip. So at that point you could start to either put your own firmware on there or see what they're doing. Maybe not the most secure firmware that's ever been out there, but you know, that's fine.

**Dave Jones:** Got it. And how long does the battery, is this, is this thing sealed? Cause it has a coin cell in it. Right. And is it, is it like one of these like five year battery life things?

**Chris Gammell:** Yeah. So like at least the tile, it was a one and done. Basically you buy it and you refresh it every year and you just get a new tile and you re-register it at that point. That was kind of the idea. And then each year, so I had bought one, I had one like early on, which I think was Bluetooth five instead of six and maybe, maybe not even LE, but basically, you know, it was pretty, pretty basic. And then just recently I bought one for a family member and it was like super thin, super tiny, had a lot more features. So, and like super cheap too, you know, like 10 bucks, 20 bucks for these things.

**Dave Jones:** So actually I'm surprised this thing's not potted actually. No, this has an easily replaceable battery. So it looks like you just, yeah, it's got a CR2032 and Bob's your uncle and a little battery compartment thing. So yeah, but I'm, I'm surprised it's not, uh, it's not like a little plotted and potted blob because if I was designing one of those tags, which has to be robust, right? Cause the whole idea is like you attach it to your luggage and stuff. Right. And it gets the crap, absolute crap beaten out of it. Right. Yeah.

**Chris Gammell:** From like just a vibe, shock and vibe. Yeah. I would, yeah, that makes sense.

**Dave Jones:** Pot it.

**Chris Gammell:** So that's true. That might end up impacting antenna performance.

**Dave Jones:** So yeah, but you know, you can deal with that. You can sort of put the antenna towards the outside and then pot around it kind of thing.

**Chris Gammell:** So it's, yeah, but then we wouldn't be able to see a teardown either.

**Dave Jones:** You know, true, but still, you know, yeah. Yeah.

**Chris Gammell:** Yeah. So it's interesting seeing this stuff. I mean, there's, there's a ton of, there's a ton, ton, ton of stuff out in the IOT world around asset tracking. Yep. But this is a very specific brand of it. I think, you know, this is Bluetooth based. It requires, you know, that a phone walks by it, that it can act as a beacon. It requires some level, you know, if you're, if you're a farmer in Nebraska and you know, you have like two neighbors, this is effectively worth it. Right. Right. But if you're, if you're living in Chicago, like I am, you know, there's all these people walking by your stuff all the time and it's able to kind of broadcast. Yeah. That might have some more. I mean, I guess maybe the Nebraska farmer, you could start to do like time. I think there's some time of flight stuff in here too. So you could start to say like, you know, where's my wallet in the house? If you had one in your wallet or on, on the remote. So I guess you could do that sort of thing, but you're not going to get the, like, you know, someone stole my dog. Where's my dog sort of thing, you know, unless you're driving, you know, in a cross hatch pattern across town, trying to, trying to see a Fido pops up on your, on your ID thing.

**Dave Jones:** So it's the modern day equivalent of war driving then.

**Chris Gammell:** Uh, yeah, I guess that could be. Yeah. Sort of. Yeah. Yeah. The, yeah. I mean, asset tracking is moving into like the, the cellular space as well, right? There's all these chips. Like, so this has a Nordic chip on it. There's also the NRF 91. Uh, we've had Jared Wolf on the show and we've talked about that sort of thing too. Basically tiny. I do think that's kind of the future and that's probably what you will start to see, but it's still just so expensive.

**Dave Jones:** Hang on. I'm, I'm looking at the board now. It's a little circular ring kind of thing. And it's got a Maxim class AB digital audio amplifier in it. What the, why? Yeah. I said that. What does that do?

**Chris Gammell:** I have no idea.

**Dave Jones:** What?

**Chris Gammell:** Yeah.

**Dave Jones:** I don't get it.

**Chris Gammell:** There's two, there's two amplifiers. There's a TLV 9001 as well. I guess it's an op-amp, not an audio.

**Dave Jones:** So it's got a custom Apple-y fruity chip in it. The U1 ultra wide band transceiver.

**Chris Gammell:** Yeah. Right. That's right. Okay. Yeah. And I think that, I think that, that is in the iPhone as well for like, Oh, okay. Right. Like proximity detection and like spatial awareness, that sort of thing.

**Dave Jones:** Got it. So, okay.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** The RF engineers at Apple are, they've got a lot of, a lot of stuff to do. That's for sure. It's a, I mean, like just this little tiny thing. It's like, you got so much RF spitting out of it. Yeah.

**Dave Jones:** And it's a, but it's all in the software application layer as well. You know, that's where the magic, that's where most of the magic happens. Right. Yeah. So, Hmm. All right. Yeah.

**Chris Gammell:** So we'll, you'll see how that stuff goes. I'm kind of interested in this. So I also wanted to talk about one other thing. So we missed, we missed that on here, I guess in, again, in the realm of IOT, which is, you know, I'm interested in, you're probably a little less interested in.

**Dave Jones:** You think? Exaggeration?

**Chris Gammell:** Yeah. Right. I mean, I think it's, anyways, it doesn't matter. Uh, the, so there was an article we had on here called sidewalk labs launches pebble, a sensor that uses real-time data to manage city parking. Okay. Whatever. So first thing I wanted to say about this, this is confusing as hell because Google has a group called sidewalk labs. However, there's a group at Amazon called sidewalk. Oh God.

**Dave Jones:** And basically, I mean, I think of the pebble. And then pebble. Exactly. Right.

**Chris Gammell:** Exactly. Right. Yeah. It's like, come on guys. Let's, let's get some, let's get some cross name cross-referencing before we start naming things. Anyways, the sidewalk labs is interesting. Sorry, not sidewalk labs sidewalk. The Amazon sidewalk thing is interesting because for a while now, right? So like, not, not like your phone is sitting and broadcasting and doing, you know, or checking in on things. Now the Amazon echo has, they've been putting Laura chips on there and I'm sure they've known about it, but they've started to activate them. Right. So basically using Amazon echoes as receivers for, as Laura sensor collectors.

**Dave Jones:** So they've activated Skynet is what you're saying.

**Chris Gammell:** I wouldn't say Skynet, but basically imagine now, like the thing we're talking about here, where instead of phones kind of moving around and reporting GPS data or whatever, now it's basically say someone steals Fido, right? In downtown Chicago. And they walk past an apartment on third street. Yep. Right. And there's an Amazon echo in there and it's got enough range. Ah, right. And then there's a device that's tracking and saying, you know, so now Amazon wants to have basically tracking devices now too. Fido's got a thing on his collar. It's broadcasting, it's broadcasting, it's broadcasting. It goes past an echo. And then the echo knows where it is in space. And it can say, Hey, I just saw Fido's tag. You might want to track. And then maybe even over time, they could start to say like, Oh, Fido's moving up third street, you know, like, and you know, maybe it wasn't taken, maybe it was just wandering, but whatever it is. I mean, this is, it's a wild world out there, man. Yeah.

**Dave Jones:** No, I can see like that. Everything's about tracking these days, be it software, hardware, whatever, everything's about it. I can, I can see, I can see a time coming when there will be, you know, part of the population that just goes like, it'll be trendy to not want to be tracked.

**Chris Gammell:** Oh, I think that already exists. Yeah.

**Dave Jones:** Right. It's probably, you could say there's already here, right? People just go, no, they disable every tracking thing. It's like, it's getting too much.

**Chris Gammell:** People start to look like you and the cover image of our last episode. Right. Yeah. With the tinfoil hat. Literal tinfoil hats.

**Dave Jones:** Yeah. It's just, no, I'm personally getting sick of it. It's like, you know, yeah, I can see the novel applications, but I'm not going to turn all this shit on just so I can help somebody find their Fido. You know?

**Chris Gammell:** Yeah. Well, yeah, no. And that's an interesting counterpoint too, because specifically Apple, right. Is, is making other headlines for in the iPhone privacy tracking. They're like turning off. You have to like opt into Facebook tracking. Now there's like, oh, there's a lot to do about that. Whatever. I couldn't care less about it. I think it's, you know, it's fine. Good move. Whatever. Who cares? I don't have an iPhone, but they're like, oh, we're against digital tracking. But now it's like moving out into the world. Yeah, exactly.

**Dave Jones:** No, we want to track you.

**Chris Gammell:** I think you're right that there, there are like things like this where people are going to be like, oh, I, I don't want this stuff to happen and to track in the real world or, or equivalent. And it's just going to be the usual trade-off of convenience versus privacy sort of things. Yeah. Yeah. It's, I'm just really interested because Amazon sidewalks out there, right? Basically you can use this. You can basically pay for it, right? It's an AWS type of offering. So now you can develop onto this platform and you just don't know. I think the thing that bugs me about it is just that it's almost impossible to know what your devices are doing anymore. Not, not like I really have this deep knowledge anyways, right? I don't know what my TV is spewing out on wifi or similar, but it's just like that is increasing. And yeah, that's, that's a little, I wouldn't say scary, but it's just, I think it's just frustrating, right? It's just, it's just the complexity of the modern world. I think that's part of it. Yep. So, yeah. All right. Yeah.

**Dave Jones:** Yeah. Nothing. You know, things tracking crap. Can we like put that on the list of banned items on The Amp Hour?

**Chris Gammell:** I'm no, I'm going to keep talking about IoT. I hate to tell you. Yeah. I mean, it's kind of my livelihood. Yeah. Right. Yeah. Okay. Yeah.

**Dave Jones:** All right. So I'll just have to put up.

**Chris Gammell:** I do like cellular.

**Dave Jones:** Yeah.

**Chris Gammell:** Because, you know, like it's at least a little bit more upfront, you know, but it's basically, but basically the, the, you know, the cell companies also know exactly where you are and what you're doing. Right. It's like, we're all carrying around sensor nodes in our pockets every day to, you know, again, for convenience.

**Dave Jones:** So I'm like, like a seriously, I, I, I look around and usually at when I go to the gym, for example, right. I leave my phone in the locker downstairs. Right. I just like, I do not take it in. I'm the only one who does that. I look around the, I look, look around the class and everyone has their phone in the class with them. Why?

**Chris Gammell:** Why? Do they listen to music during the class or are they listening? No, no, no.

**Dave Jones:** They, they will just be, you know, texting and checking things. Because that's like part of the class, right?

**Chris Gammell:** It's like the pump up music.

**Dave Jones:** Oh yeah. No, but you'll have music over the speakers. You don't have music through your own iPod thing, you know?

**Chris Gammell:** I get it.

**Dave Jones:** No. And it's, you know, they, they just want to desperately check two seconds before the class starts. They want to check their Facebook status, you know? What the hell? Facebook.

**Chris Gammell:** I mean, Facebook. I don't know.

**Dave Jones:** Whatever the kiddies are using these days. I don't know. Jesus.

**Chris Gammell:** I'd say TikTok, but I think probably that's probably already, you know, moved on to. Yeah. It is tough to keep track of.

**Dave Jones:** It's just, anyway. Nothing.

**Chris Gammell:** Anyway. Can we. Well, why isn't the, why isn't the amp hour on more social networks? We don't, we have no, we have literally no idea where to go. Find us on Twitter where old people hang. Right. And complain about hardware.

**Dave Jones:** We need to be on TikTok, do we? We need a Twitter TikTok. No, no. No, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** No, thanks. I have my dead body. Yeah. Okay. All right.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. Speaking of China.

**Chris Gammell:** Sure. Sure. I guess, I guess. Yeah.

**Dave Jones:** A hearty congratulations to the, I guess it's the Chinese space agency who we're sorry. I don't know. No. The, yes. CNSA, I think. Anyway. They, they, they landed a Mars rover first go. Really? I didn't hear about this. Yes. Yes. Look, look, I'll send you a link right now. Here we go. I'll send you the photo. They just released one photo. Cause you know, this is like days after it landed. Cause they don't release anything. It's like. Right. But now that it's happened, they've at least released one photo. Oh, bloody links in this Zencaster aren't working properly. This sucks.

**Chris Gammell:** Anyway.

**Dave Jones:** Yes. It's the TNWEN1. If I'm pronouncing now, I'm butchering that. I'm sure the TNWEN1, it's got a little rover and you can see a photo of the ramp and it's going to come down and it landed. And this is their first attempt. Whereas, you know, like most countries have failed on their first attempt. Like Mars is hard. All right. Landing something on Mars is hard. So yeah. Hardy, congratulations. They did it. And they've got this little rover. I don't, I don't know how much it can do. You know, it's, it's not a curiosity sized rover. Do something. Come on.

**Chris Gammell:** Where's, where's your quad cop?

**Dave Jones:** Exactly. It's so 2000s, you know, it's like, yeah, but no, that, that is hard to do.

**Chris Gammell:** That's really impressive. Yeah. That is hard to do.

**Dave Jones:** And they, yep. And there's a, I don't, I haven't looked for, I haven't looked for, I haven't seen updates show up on my Twitter feed. I'm not actively looking. I'm waiting until the YouTubers that I, you know, the space people on Twitter that I follow retweet them. So yeah. Because they're looking constantly and they're on top of this sort of stuff. So anyway. Anyway. Yeah. There's a little, little ramp that it's going to, it's going to drive down and drive around, I guess. So cool. Cool bananas. Yeah. There doesn't seem to be much features there where they landed. It's kind of like a real safe flat spot. You know. Good for landing. Yeah. Yeah. It's our first go. Let's land somewhere.

**Chris Gammell:** Did they have a similar landing profiles like the, like the hover and drop? Or is it more like that?

**Dave Jones:** I don't know. I think it was a, a completely powered descent. Like the balloon and roll thing? Yeah. It was just a completely powered descent. It didn't drop down tether. There's none of that tether stuff. I believe it was just completely powered like the Vikings landers back in the seventies. So. Okay.

**Chris Gammell:** What do you, what do you mean by powered descent?

**Dave Jones:** Powered descent. It uses rockets and it just powers all the way down and then just lands. Got it. So it doesn't like go, you know, it doesn't drop anything on a tether and then cut the tether and drop it and then fly away. It's, it's a fully powered descent. I believe. Don't quote me on that. So. Okay. Because that's just the easiest and safest, safest way to do it. And they would be doing that. The West would be doing that if they were landing small stuff. Right. Or they'd be using airbags or something.

**Chris Gammell:** Weight limits on.

**Dave Jones:** Like that.

**Chris Gammell:** Right. I remember, I remember the one that was like a, it was like a pyramid of airbags. Yeah. Pyramid of airbags.

**Dave Jones:** Yes. That was two missions. That was the Sojourner rover and the other one. Yeah. The airbags, but, but for the curiosity rover and the, and the perseverance rover, they couldn't do that. It was too big. It's the size of a car. So you can't, you know, it's different. SUV really. Yeah. It's the size of an SUV. It's, it's absolutely enormous. And it weighs, you know, a ton or more or something. And if, if you propulsively land that you need so much thrust that it just, it, the dust that goes everywhere. The rocket equation gets you too. Sorry?

**Chris Gammell:** Like the rocket equation would get you as well. Well, everything gets you.

**Dave Jones:** Every part of physics gets you. And you just need so much rocket propulsion to land the damn thing. Yeah. That it just kicks up so much dust. That's why they had to come up with the sky crane tether thing so that the, you know, the rockets were, you know, 10, I don't know how many feet up, right? How many meters up? 10, 10 meters up or something like that. So you don't kick up as much dirt because once you, you know, you don't want your scientific lab that you're landing on Mars to be covered in dirt, right? That's kind of, yeah. Sorry. I shouldn't be using the word dirt because it's technically not.

**Chris Gammell:** Martian soil. Martian soil.

**Dave Jones:** Regolith, I believe is technically the name, but a lot of people think that's only in relation to the moon, but I don't believe so. I believe dirt is here, like is on planet earth, but everything else is technically regolith regardless of whether or not it's on the moon or on Mars or anything.

**Chris Gammell:** A layer of unconsolidated rocky material covering bedrock. That's the definition of regolith apparently.

**Dave Jones:** Right. Yep. So I do believe that is technically it, but anyway, Martian soil, Martian dirt, right? That red dirt stuff.

**Chris Gammell:** Dirt goes here.

**Dave Jones:** And yeah, you don't want that blowing all over your nice freshly landed science lab. So that's why that uses sky crane, but this one's a bit smaller, the Chinese one. So I believe they propulsively landed it. But anyway.

**Chris Gammell:** What they really need to do is just send a robot and then have a second robot that there's just with a can of like compressed air. And it just, you know, that's what the second robot's there for is, you know, just clear it right out.

**Dave Jones:** It'd be fine. I love it. How Mars is technically a planet entirely habited by robots.

**Chris Gammell:** Yeah, that's right. Well, that we know of. There could be tiny little wee beasties out there.

**Dave Jones:** There could be microbes and stuff like that. So yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway.

**Chris Gammell:** Well, speaking of dropping electric vehicles on other planets, there's a new electric vehicle that dropped on this planet. And it's very interesting. Interesting culturally, I think, because of the US trucks. Well, in the US, nobody else gives a shit. Yeah, right. Right. Exactly. No, no, no. I completely agree. The fact that the F-150 is the number one selling vehicle boggles my mind every time. And of course, once you've got set cities, yeah, it certainly makes sense.

**Dave Jones:** And it's so crap, isn't it? Apparently, like, it's like- Oh, no. No, it's not. I thought it was like crap. Oh, no.

**Chris Gammell:** They're super slick insights these days. Oh, right.

**Dave Jones:** Oh, okay. Right. I'm thinking.

**Chris Gammell:** But they're huge. I mean, it's like- I know. It's enormous.

**Dave Jones:** I've seen some around here.

**Chris Gammell:** Yeah. Yeah. It's just silly. Oh, really? They have them there? Oh, yeah.

**Dave Jones:** And yeah, they actually advertise them. There was just an ad last night that I saw on TV. They were advertising the Ford. You know, their tagline is, it eats utes for breakfast. Right? So that's, you know, because it's a ute here, right? A truck is a ute. That's right. That's right. So, yeah. So they're advertising, it eats utes for breakfast. So, you know, bastards to piss off. Yep. Yeah, right. Yeah, the thing's stupidly big. Just dumb. Yeah. Yeah.

**Chris Gammell:** Yeah, I think the interesting thing about this is, so I was listening, there's a report on, I think it might be this NPR report that the link is, but also, but basically it's like, they're not trying to say like, oh, it's environmental or anything like this stuff. It's like, basically, this thing is a beast, you know, like it just hops off the line. It's like huge and it hops off the line because it's, you know, an electric vehicle. And yeah. So seeing that, it's kind of interesting. The thing I'm not sure about is that they have, so you and I have talked about this and you've also talked to some of the folks, I think when you were doing all that electric bus stuff. Yep. But basically back powering a home.

**Dave Jones:** That's called VTL, vehicle to load.

**Chris Gammell:** Yeah. So I think this has it. That's at least what the article implies, but I didn't see anything about the details of it. And, you know, from a, okay, like, you know, it talks about like having outlets on board for powering stuff, campsites or work sites. That all makes sense, whatever. But the thing that interests me is back powering a home. That could be very interesting. Oh yeah.

**Dave Jones:** That's no, technically the new model Leafs can do it as well.

**Chris Gammell:** Ah, okay.

**Dave Jones:** But the box to do it is like $10,000. So it's like ridiculously expensive. Yeah.

**Chris Gammell:** Oh, so it's not just built in. You need like a secondary. No, yes.

**Dave Jones:** You need a secondary thing. You can't just plug it into your PowerPoint at home. No, you, you need an inverter box. You need to meet all the regulations like you do for a, for an off-grid solar system and the whole works. Right. So there's all sorts of safety implications there. Oh yeah. So it's very expensive. Got it. Yeah.

**Chris Gammell:** Yeah. Yeah. I mean, some of those things, like if the power went out, like you could like go and just plug your fridge into this, you know, it's got a huge inverter in it. Oh yeah. It's got a standard PowerPoint.

**Dave Jones:** Yep. The, I just saw they've just released, well, they haven't released it yet, but people are test driving it. The one prototype that's going to be released, the new Hyundai Ionic 5. And it looks stunning. Oh my God. And it does. I, well, I have the Ionic curiously, they've named it the Ionic, but it's not really a follow-up to my one. So it's not, it uses the name. So they're just borrowing the brand? They're just, yeah, they're just borrowing the brand.

**Chris Gammell:** Oh, it's a hatchback?

**Dave Jones:** Yeah. It's kind of like a SUV crossover sedan kind. It looks like a sedan, but it's more of like an SUV size kind of, or a crossover SUV or something.

**Chris Gammell:** That's cool.

**Dave Jones:** Yeah. It's it. Wow. And it's got the same thing. It's got vehicle to load and it comes with this little, little inverter. That like pops into the side charging port, right? It, it pops into the CCS port on the side of your car.

**Chris Gammell:** Oh, so like the, the charge port where you'd normally plug in. Where you'd normally plug in.

**Dave Jones:** And then it has a mains plug on it and then you can just power anything. Right. And then it can also do vehicle to like, it could do the house thing as well. I'm sure.

**Chris Gammell:** Yeah.

**Dave Jones:** So yeah.

**Chris Gammell:** But they have bigger cables, lower drop, that sort of thing. Yeah. Yeah.

**Dave Jones:** Because it, it, it supports the new 800 volt system, which is 250 kilowatt charging. It's like insane. Like, you know, the. Holy moly. Yeah. Like, and, and, and if you don't know for those, right. Anything over 50. Well, no, even the 50 kilowatt ones they have, like, there's so much power going through these, these connectors. If you've like got a high power appliance at home, you know, that's drawing like the maximum current for your mains. If you actually pull the plug off after you've used it, it's warm. Right. Oh yeah. Because of the contact resistance. Right. That, that connector heats up. Well, imagine doing that for 50 kilowatts instead of two kilowatts. Right. Right. Yeah. Just. Or 250. Yeah. Well, I'm talking just at 50 kilowatts. Right. Which is what mine is capable of. Actual maximum. Those ones actually run liquid cooling through the cables, through the connector to actually you can, you can physically hear the pump and you can feel it vibrate. You can feel the thing. Cause they're pumping fluid. They're pumping cooling fluid through the cable, through the charge connector, right up the cable. Because it's, you know, that's why they're so big and bulky and you know, it's not because they've got a lot of copper in there. It's because they're cooling the dam. Yeah. Cooling hoses.

**Chris Gammell:** So is it just, it's just, it's just a, a simple pump for that sort of thing. It's just like a closed, closed system. Yeah.

**Dave Jones:** Yeah. It's just a closed pump system. And there's, then there's a heat sink in the big, that's why those cabinets have to be so big. Cause they've got giant heat sinks and fans and things in them. So. Got it. Yeah. Yeah. Yeah. And then, and they've got a little fluid pump and it's like a closed, you know, just, just like one of those newfangled gamer kiddie PCs, you know, with the liquid cool

**Chris Gammell:** closed cycle. With ground lighting. Yeah. Yeah.

**Dave Jones:** With the RGB wank lighting.

**Chris Gammell:** Sound sensitive LEDs. Yeah.

**Dave Jones:** And yeah, but, but imagine 250 kilowatts, right? That's just, you know, it's like, that's just nuts. That's like five times 50 kilowatts, which already has to liquid cool it. So, you know, but your latest Tesla's, I think they'll charge at 200 kilowatts. Won't they? I think some of your latest ones and yeah.

**Chris Gammell:** So the thing is, this is still so far out of my, well, I thought it was out of my price range, but some of these new ones are getting cheaper and cheaper.

**Dave Jones:** So that's, you guys have lots of subsidies over there. So you're pretty lucky. It depends on what state you're in. That's why everyone has a bloody Tesla over there. Cause they're all subsidized.

**Chris Gammell:** There's not that many here. Come on. Well, it's not Illinois.

**Dave Jones:** Come on. Everyone in bloody California drives a Tesla. If you don't, you're a nobody.

**Chris Gammell:** There's more. Yeah. You're a nobody.

**Dave Jones:** You're a Neville.

**Chris Gammell:** You, you said it. You heard it here first, folks. I'm a nobody.

**Dave Jones:** Nobody from Chicago.

**Chris Gammell:** But to be fair, I don't have a car. So there's, there's also that. So like, yeah, I wouldn't have one anyways. Yeah. Yeah.

**Dave Jones:** Because you don't own a car, do you? Big sure.

**Chris Gammell:** I do not. Yeah. I currently. You're a suburbanite. I'm a city dweller.

**Dave Jones:** You're a cityite.

**Chris Gammell:** Yeah. Yep. Yes. Yuppie is, I believe the term. Oh, yuppie. Oh God, that's so 80s. Yeah. Yeah.

**Dave Jones:** Is that term still around?

**Chris Gammell:** Yeah. It's usually used derogatorily. Yeah, of course. It's correct. Yep. It's a, it's, it's a lifestyle and it's an annoying way to live. And I embrace it.

**Dave Jones:** Excellent. More power to you. Yeah. Anyway. Yeah. All these, this year, this year and next year, the market is going to be flooded with electric cars. Oh my God.

**Chris Gammell:** That's right. The number that we've got coming out. Unless they can't build them. Unless they can't build them. Yeah.

**Dave Jones:** Of course. Yeah. You won't be able to buy one for quids. You know, the second hand car markets boomed apparently.

**Chris Gammell:** Yes.

**Dave Jones:** Absolutely booming because people can't buy new ones. So everyone's going to buy like a one to two year old lease car, you know, they're buying all this second hand.

**Chris Gammell:** Those are really hard to get to. Right. Yeah. They're basically the same price. They're actually selling out. Yes.

**Dave Jones:** Because everyone's, they can't buy a new one. So they go look for one that's a couple of years old and while they're selling out too. And yeah. You know. Yeah.

**Chris Gammell:** Yeah. Yeah. It's just weird. It's a, it's a weird time. It's weird time to be buying it, buying anything, you know, lumber, houses, cars, whatever, whatever you want to build by. You basically can't right now.

**Dave Jones:** Yeah. Yeah. No, it's a, it'll be interesting.

**Chris Gammell:** I really, really, really, really, we're going to launch into the sourcing stuff now. I really, really, really, really, really, really, really hope this swings back in the other direction. I have an inkling that it won't. That it won't. Oh, pessimist folks. Yeah. Yeah. The eternal pessimist. It just feels so bleak right now.

**Dave Jones:** It feels so bleak. There's no way out of this hole. Just, you know.

**Chris Gammell:** Oh, it just, I mean, yeah, I'm seeing lead times, you know, like lead times are just, yeah, we don't need to.

**Dave Jones:** There's only one solution, Chris, and that's to go bush.

**Chris Gammell:** Just stop making electronics and go native.

**Dave Jones:** Well, go, go woods, I guess, as you Yags would call it. Yeah. Right. Right. Just move into the woods and.

**Chris Gammell:** Yeah. Mountain man. Yeah. Right. Yeah. And have to get to the mountains first, but then be a mountain man. Yeah. Yeah. That's, that's true.

**Dave Jones:** Yep.

**Chris Gammell:** You know, my, my current thing is right software for hardware already have on hand. That's basically the best I can do right now. Just keep, keep improving the same piece of hardware, uh, with firmware. So yeah, that's, that's one thing I can do.

**Dave Jones:** Well, if you can't buy new, you can always like repair broken stuff.

**Chris Gammell:** Yeah. Nice. That, that's, that was a good one. That was a good one. What are you repairing?

**Dave Jones:** Well, no, well, actually, no, this, I didn't think about that segue. There's two segues here. Should we talk about the thing I'm repairing at the moment, or should we talk about the right to repair?

**Chris Gammell:** All of those things. Actually, I have a third repair thing that actually is related to cars. I've been wondering this as I think about all these electric vehicle things, what's going to happen to all the car repair shops? Do you think they're going to switch over to?

**Dave Jones:** They're all converting to EVs. Yeah. Yeah. Yeah. They're all recycling. I just watched a YouTube video last night about a company in the UK who, you know, they're now specializing in EV battery refitting. So, you know, getting older Leafs that are nine to 10 years old and, and getting new batteries installed for them. And they're, they've niched into that now. They've, they've totally moved into that. So, yep. Yeah.

**Chris Gammell:** I mean, there's certain parts of the car that are still going to be required, right? Oh, no, of course. And, you know, like axles and stuff like that.

**Dave Jones:** Well, people think that, that these EVs have nothing in them, but that's not true. You've still got your power steering. You've got your air con systems. These are all traditional systems. You've got cooling systems.

**Chris Gammell:** Well, not all of them are power steering, are they? Yeah. I mean, cause some of them are.

**Dave Jones:** These are all regular steering systems. You've got to have. Hub motors.

**Chris Gammell:** You would still need to. Yeah. You still need to like, yeah, I guess you'd need to like have a hydraulics to move that sort of thing.

**Dave Jones:** These are all got all regular systems in them, but instead of being driven by belts from the engine, they're driven by motors, electric motors, but they're all traditional air con systems are all traditional braking. So the hydraulic fluid braking systems, right? These are all traditional things, right? You can't just rely on the regen braking of an EV, right? It's got to have a traditional hydraulic fluid pressurized disc braking system, right?

**Chris Gammell:** Right, right. Clamp down. Clamp down on a disc or a drum or whatever.

**Dave Jones:** So it's all there, right? It's all. So all these systems still exist. They've just been driven by motors instead of belts.

**Chris Gammell:** They're not going to be able to sell me. They're not going to be able to sell me oil changes as much. I guess they still have some lubrication needs. No, but they seem to be- They won't be able to sell me like fluid flushes or- Well, they're crazy reliable. Yeah, exactly.

**Dave Jones:** Because timing belts are a thing and you don't have those anymore. They're more reliable because they- How often does your air con system in your car actually break down? Never, right? 100,000 miles. Right. Yeah, yeah. It's almost never.

**Chris Gammell:** 200,000, whatever. Right? Case. Yeah.

**Dave Jones:** Yeah, exactly. So EVs are crazy reliable, but they still have all these traditional systems in there. They're just driven by motors.

**Chris Gammell:** Yeah. Yeah. Interesting.

**Dave Jones:** So, you know.

**Chris Gammell:** I remember why I actually thought about this. I was listening to this this morning and I was thinking about this and I was like, oh, I wonder what's going to happen to all these repair shops. And I was like thinking, oh, all these grease monkeys are going to start being interested in electronics. That got me very excited. And then the thought that really got me excited is you and I have said in the past, the best compliment we could get is that we're heirs to the thrones of car talk. And I was like, holy shit, it's happening.

**Speaker ?:** Right.

**Chris Gammell:** So, you know, when electronics and vehicles collide, you know, the amp hour becomes car talk.

**Dave Jones:** Right. Okay.

**Chris Gammell:** We'll just, we got another 20 years in this then.

**Dave Jones:** Sorry. I have no affinity for car talk whatsoever. It's just not a.

**Chris Gammell:** You should. You should go listen. It's still on. You can still hear all the episodes. It's so good, man. It's so good. Except the only difference is if people call it in here and they ask about their cars, I won't have any idea. So I guess we won't. Yeah. I won't be doing that.

**Dave Jones:** Okay.

**Chris Gammell:** All right. That's all I need to say about repair. What are you repairing?

**Dave Jones:** I'm repairing an amp at the moment. One of those, you know, newfangled surround sound receiver things. Does anyone have surround sound anymore? Like it was all the rage back in the nineties and two thousands, right? Everyone was installing surround sound speaker systems. Now everyone's got like a sound bar.

**Chris Gammell:** Yeah. My in-laws have a, have a surround sound and I've been at houses that have it otherwise. Yeah. I mean, it's still around. I think it's just that, yeah, sound bars are cheap. Sound bars are cheap and easy.

**Dave Jones:** You don't have to install wiring. They don't sound that good.

**Chris Gammell:** I got one. It's just not, not that good. Oh, they're right. I mean, they're better than like flat panel TV speakers. Yeah. Yeah. Yeah. Yeah. You just don't need depth to those things. You need some like, you need depth in a speaker. Yep. You know what I mean? You need a big throw. Those cones. Those giant throw cones. Yeah, exactly. I'm pushing that and pumping that area. It's an inductor with a piece moving through it. You need to move it through it. You know, you gotta, you gotta really push those air molecules around, man.

**Dave Jones:** Well, this comes into when we had big Clive on the amp hour, he, he mentioned that a lot of people, like if they were listening to him on their phone speaker, they could not hear him. They simply couldn't hear him because he's got really low base. I can't even do a low base voice, you know? And, and me, everyone can hear me. So I'm so high pitched and you know, everything's.

**Chris Gammell:** His wonderful accent too.

**Dave Jones:** Yeah. Yeah. So, and those bloody little, you know, neodymium magnet, tiny little piss ant speakers in your phone.

**Chris Gammell:** Yeah. A little class D with like a, you know, a half inch speaker or something in there, maybe less. I don't know how big the speakers are.

**Dave Jones:** I, I, I don't want to go whole, I don't want to go audiophile, but you know, I guess there's a whole new generation of people who don't appreciate good audio, you know? Yeah.

**Chris Gammell:** Uh, that would be me as well. Yeah. I mean, like I appreciate audio in that, like we try and have decent audio on here and you know, like we, we want it to be at least a baseline, but I think we want it to be like, you know, a level of quality as best we can, but like, yeah, I, we're not like, Ooh, but do you hear the, the, the fine, the finer touches of the timbre of Chris's voice is just,

**Dave Jones:** Oh, phenomenal today. The one crunchy sound of the tubes.

**Chris Gammell:** Yeah. No, I don't think anyone's listening to us. Right. Tube amp. But if they are, if you are, if you are listening to us through a tube, we would love to see your setup. And also we have other questions. Right. But, um, yeah, it's not, I always used to say like, I, I didn't care. Like I grew up, I grew up, I, you know, in college I was downloading 96 kilohertz, you know, it, it was terrible. Yeah. Yeah. Yeah. 96. But you know, you know, any port in a storm, whatever, whatever the equivalent audio, you know, anecdote is, uh, I just, I wanted, I wanted the music. I wanted just to hear something.

**Dave Jones:** That's still way better than tape though. That's way better than making a mixtape. Yeah. Maybe. You have no idea what a mixtape is.

**Chris Gammell:** Do you? You just, I know exactly what a mixtape is. Come on. I'm not. Yeah. But yeah, but you're not from that generation. I made mixtapes, Dave. I mean, I, you made mixtapes. My 12th birthday. I got a boom box with a double tape deck and a CD player. Uh, I mean, it was like at the end. So like I, uh, to have Chrome support. I don't know what that is. I don't know what that is. Oh, metal tapes.

**Dave Jones:** Chrome tapes. Come on.

**Chris Gammell:** I thought you were saying Chrome support. I was like, did it run a browser? Exactly. I know. I knew you'd be confused by that. Yeah. That's why I put it out there. Yep. So what is Chrome?

**Dave Jones:** Chrome, metal Chrome. That was all the rage. You got Chrome tapes. They were higher quality.

**Chris Gammell:** Oh, interesting. No, mine were always vinyl, like the cheapo.

**Dave Jones:** But, but your, uh, heads had to support it. Your, your physical tape heads had to support. So there'd be a metal Chrome tape switch. There'd be normal Chrome.

**Chris Gammell:** So you would get like.

**Dave Jones:** Normal Chrome switch. Really? Yeah.

**Chris Gammell:** How did they, like magnetically encoded onto Chrome?

**Dave Jones:** Well, it was, it was Chrome was part of the formulation of the tape and it was just, you know, metal tapes. Okay.

**Chris Gammell:** So it was like a, like a harder tape or something like, like for more write cycles.

**Dave Jones:** It was, uh, physically better, you know, dynamically better recording or something. You know, I, I can't remember the exact advantages, but yeah, it was all the rage. Yes. And, and, and if you had a high end Walkman, it would have a metal, a normal Chrome switch on it. That'd, you know, playback Chrome tapes. Yeah.

**Chris Gammell:** Yeah. I think the limitations on Walkmans were more about, uh, everything else around the Chrome, the Chrome tape. Yeah.

**Dave Jones:** But no, all of your boom boxes, a good boom box will have a metal Chrome switch, a normal Chrome switch on it. I was just looking at boom boxes the other day. I'm, I'm way, I'm, I'm sort of, I, I can, I neither confirm nor deny that I have an eBay watch list for the boom box from the eighties. The boom box. The boom box. I won't mention the model number. You'll have to just, you know. Okay. Yeah.

**Chris Gammell:** Yeah. You don't want to, you don't want to. No, I don't want to. Don't want to. Yeah. Flood them up. I bid yourself by people watching it. Yeah. Right.

**Dave Jones:** People outbid me. Can neither confirm nor deny that an eBay watch list exists.

**Chris Gammell:** What are you going to do? Are you just going to tear it down or you actually have, do you have tapes anymore? No, I don't. I don't.

**Dave Jones:** Maybe. Oh, I've got some. Yeah. I've probably got some old tapes, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. But, yeah. Yeah. Tapes didn't really. I mean, I think the mixtapes will live on in the, you know, the cultural zeitgeist. Yep. But they're not coming back anytime soon. No, I know. Like vinyl is.

**Dave Jones:** No, I know. I, you know, it'd just look good in the background, you know, it'd be like a background piece on the shelf, you know, kind of thing.

**Chris Gammell:** Right. Right. Right. Yeah. Old electronics behind you. That's what you need more of. More of. That's it.

**Dave Jones:** Not this newfangled tracking rubbish. Yep.

**Chris Gammell:** Yes. Right. So, okay. So you have an amp, you are fixing an amp. Yes. What is, is this a garbage amp? Is this a, from the trash?

**Dave Jones:** No, no, no, no. It's a, belongs to a relative actually. So, you know, yeah. Yeah. Occasionally they, you know, I go, oh yeah, I'll have a look at it because I get, technically I get paid to do this. Right. Cause I get advertising revenue from the videos and everyone likes to see a repair video and stuff. So it's a vacuum fluorescent display is the failure. Right. Right. So the vacuum fluorescent display is, is failed. So, and, and the thing worked, like I was able to get the thing working without the vacuum fluorescent display and it plays and everything's fine. So all the amp and all the power supplies and everything's just fine. And, and yeah, I went down there. It was one of those repair rabbit hole things. And it was one, if you've ever opened up these surround sound receivers, there's like a dozen boards in here. Right. And they're all interconnected. And it's like, that's right.

**Chris Gammell:** And wire harness, unwire harness, unwire harness.

**Dave Jones:** And, and, and then it turns out that the power supply for the vacuum fluorescent display is not on the vacuum fluorescent display board. Of course not. It's like three boards removed from that.

**Chris Gammell:** Right. But so, because usually the VFDs need like 60 volts.

**Dave Jones:** They need minus 40. Yeah. Or something like that. Minus 40. On this particular one, it's minus 35. Yeah. So yeah. Got it. VFD. It turns out, yes, there's no minus 35 volt thing. So I, once I went down the rabbit hole, I forgot to check that. That was one of the supplies that I, you know, that I was last to check. It was, and sure enough, that seems to be the reason for the failure.

**Chris Gammell:** Thou shalt check power rails. Thou shalt check voltages.

**Dave Jones:** Yeah, I know. I know. Yeah. I eventually got into it in the video. And, but in the end it was like, oh yeah, look, I've tracked it down to this circuit, but it's on this board, which is three boards removed from the display board. Right, right. And you can't just like turn it on. You can't, because it's a soft power button. Yeah.

**Chris Gammell:** That system level troubleshooting is really tough.

**Dave Jones:** Right. So you can't even like power the damn thing up because the soft power button is on the display board on the front. And then the display board wires into the video muxing board, which then the video muxing board wires into the main power supply and video processing board, which then connects through to the amplifier board, which then connects back through.

**Chris Gammell:** It's connected to the leg bone, the leg bone's connected to the hip bone.

**Dave Jones:** To the, I'm getting this right. And then goes back to the mains power supply board, which has the soft start relay that enables the damn thing. So you need to plug like five boards in together just to power the thing on. And of course they're all physically buttered at right angles and you can't, you know, so yeah, you're just. Yeah.

**Chris Gammell:** So you have it like in parts strewn across the bench. Yeah.

**Dave Jones:** And you can't even plug them together. So I've got a now after this, straight after this, I'm going to get back into it. Cause I got jack of it yesterday. I just wanted to do other stuff. So I released a part one video, but damn it. I'm going to fix it today. And I'm going to release a part two. Hopefully after this, I'm dedicated to go back in and I'm going to find the fault. Cause, cause I know where it is, but I can't power it up and test it. So I have to go in and check every, my next step is to check every component. I'll desolder them individually. If I have to, I've already desolded one of the transistors and measured it in a transistor tester. And it seems to be okay. So, you know, yeah, because other, like, like I can't power it up. And measure voltages. Right. So I can't, you know, so all I've got to do is go in. Sorry.

**Chris Gammell:** Why is that? Why can't you power it up?

**Dave Jones:** Oh, it's just the way it's physically assembled. I can't do it. I can't do it. I can't access the board and power it up and access the bottom of the board at the same time. Got it.

**Chris Gammell:** Cause it's all like folded on.

**Dave Jones:** It's folded back on itself and it's not cables. They're like right angle, but connectors and stuff like you can't. Yeah.

**Chris Gammell:** No, it's. Yeah. Right. So they're there. They do that because they want to, you know, have space saving.

**Dave Jones:** They want to pack as much into that as yeah. There's a lot of stuff packed into this one case, you know, it's a.

**Chris Gammell:** Yeah. Well, it's always interesting too, when you see that kind of thing. So if you went to the, what I assume is the late eighties, early nineties shop floor where there was probably a tech doing that. What I would expect to see is that they have connectors and or a test jig that basically unfolds everything.

**Dave Jones:** They have jigs. They have extender boards and stuff. Yeah. Back, back when I was a repair tech, when I was a boy.

**Chris Gammell:** Yeah. Yeah. We, yeah.

**Dave Jones:** We had the special purpose custom extender boards and that's how you did stuff.

**Chris Gammell:** So that you could, you could see it. Yeah. You could get it.

**Dave Jones:** Like if, you know, if you're working on 19 inch rack gear, how do you like power it up? Like, you know, rack cards, right. And you know, you should have a 19 inch rack product and then have all these plugging cards with the handles, you know, and the slide out frames. And you can't work on those unless you have a giant extender board, which brings it right out. So you put in your plug in your extender board and you bring it out. And then, then you prop the board up and then you can probe all the individual stuff on that one board, you know? So yeah. Yep. Yep. So damn it. Yeah. So I'm going to do that. I'm going to check it. It has to be, I've narrowed it down. I'm almost a hundred percent confident there's something wrong with this particular circuit, which is on this board. So anyway, yeah, I'm fairly confident.

**Chris Gammell:** So do you have like a system diagrams as well? Yes.

**Dave Jones:** I've got a full service manual for it. Oh, it's gorgeous.

**Chris Gammell:** Oh, you do.

**Dave Jones:** Oh, it's gorgeous. Yeah. Yeah. Without that, it'd be up. Because like, as I said, like you would not think that where this vacuum fluorescent driver is, you wouldn't think it's there. Right. It's like three boards removed from the vacuum fluorescent display board. It's like from a design point of view, it's like, why put it there? Why on earth would you put it on there? It's like, it's because of the way it's routed and powered and, you know, it's just, oh, it's a nightmare. So from a design point of view, it's just horrendous. And things are just scattered on different boards that you wouldn't think were even remotely related. And it's just, yeah.

**Chris Gammell:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So if you go in blind with no schematic, you're in a world of hurt, you know?

**Chris Gammell:** That's right.

**Dave Jones:** Yeah. Especially when you can't check anything when it's powered on. I could. The front panel display board, because it swung out, right? It was on a cable and it swung out from the front and I was able to measure and access that. But the power supplies for it are not on there.

**Chris Gammell:** So, you know. Yeah. They're passing it over the cable. It's nuts. Yeah.

**Dave Jones:** So anyway. And speaking of repair, there's a right to repair summit that I'm almost certainly going to.

**Chris Gammell:** In fact, I have actually registered. In person.

**Dave Jones:** It's the first right to repair summit in Australia. It's in Canberra on, which is our Australian capital. You've been to Canberra. We've stayed at Canberra. I have. Yeah.

**Chris Gammell:** We went and looked at a huge satellite dish there. Yep.

**Dave Jones:** Yep. We did. And we went to the museum there.

**Chris Gammell:** And people can listen to us talking in the car. Yep.

**Dave Jones:** Yep. Went to Canberra. Anyway, it's down in Canberra and sponsored by iFixit. Cool. And yes, it's 9th of July. It's a Friday, I believe. 29th of July, 2021. So, yep. I'm pretty sure I will be there. That's great. Yeah. So, yeah. In person events. It'll be tiny, like, cause it's, you know, I don't know how big it's going to be, but yeah, I'll be there. So, if you want to come hang out for the day.

**Chris Gammell:** You're going to give a talk? Is it like talks or is it just going to be like-

**Dave Jones:** It's talks and stuff, I think. I think there are talks and there's, you know, people will just hang out.

**Chris Gammell:** Just give a talk? Come on, man.

**Dave Jones:** Yeah. But I'm not in the repair business, although I just got through saying how I'm repairing something, but, you know. Yeah, exactly. I don't know what I'd talk about. But, yeah. Anyway.

**Chris Gammell:** I tear things down for a living. Look at all this stuff I've looked at. This is why this is important. Here's how we organize.

**Dave Jones:** From a design point of view, there's absolutely no reason to have serialized chips and all that bullshit. You know, it's just these companies, these fruity companies are deliberately doing this. You know? Yep. Yes, they are. There's no technical reason to do it. Absolutely none. Oh, yeah. To have serial number, serialized chips that, you know, you can't even take a part from another iPhone, a genuine part from a genuine iPhone and put it in another genuine iPhone to repair it. It's just ridiculous. You can't even cannibalize a unit for parts. It's bullshit. So, yep. Anyway. There ends my talk. Okay.

**Chris Gammell:** Thank you for coming to my TED Talk.

**Dave Jones:** There's no reason for this. It's bullshit. The end. Thank you. I'm taking questions. Yep. So, there you go. There's a preview. Ah, boy.

**Chris Gammell:** I am hoping there are... So, we... I've talked to two groups that might have conferences in the US by the end of the year, which would be awesome. I don't know. I can't... I don't think I can mention which ones there are, but I am going to... I am angling to be at one in-person event before the end of the year. Oh, okay.

**Dave Jones:** So, this has nothing to do with repair. You're just excited that you have events again.

**Chris Gammell:** Just don't want to see humans. Yeah, I just want to be...

**Speaker ?:** Oh, right.

**Chris Gammell:** See, yeah.

**Dave Jones:** That's a foreign concept here because we've had this stuff for a year. So, you know. Yeah.

**Chris Gammell:** Yeah, I know. That's great. But I'm on a different continent and...

**Dave Jones:** On a different planet. Yep. Yep. That's right.

**Chris Gammell:** Yeah. It feels like it sometimes. Hello, Dave. Can you hear me from afar?

**Dave Jones:** See, I just... Like, this morning, I just saw Jerry Ellsworth, a friend of the Amp Hour, tweet that, oh, I'm going to be able to hug people again in a year. She just had a shot. So, and I'm going... You know, and this is just so foreign to me. After a year, you mean?

**Chris Gammell:** Yeah.

**Dave Jones:** Like, you know, it's just... I don't know. You know. Sorry. I can't. Yeah. That's great, man. I just can't. Yep.

**Chris Gammell:** New t-shirt for Dave. I can't empathize. I can't empathize. Yes. Yes. Yes, we know.

**Dave Jones:** Sorry.

**Chris Gammell:** In the meantime, there are still a lot of developer summits going on. There's one coming up for Zephyr. I'm going to be attending that one. People have heard me talk about Zephyr on here. It's a real-time operating system and cross-platform. You know, you can put it on things like that chip we talked about earlier, NRF2832. Yeah. Pretty cool. Some good talks there. So, I'll be at that. I actually really like this format, too. It's basically a three-day conference, but it's only like four hours a day. And so, it's like that's the way to do a conference.

**Dave Jones:** And this is online, right? This is a…

**Chris Gammell:** That's right. This is all online. So, it's also because it's Europe and the US. How is it being done?

**Dave Jones:** Is it just a giant Zoom meeting or is it… What is it?

**Chris Gammell:** Yeah. I think it'll be like if it's a panel, it'll be multiple people on a Zoom and then everybody can watch it. Or if it's just a person, then sometimes they pre-record them even and they'll do talk. They'll do questions at the end, that sort of thing. So, yeah. Right. Yeah. There's been a bunch of things. It's tough. I've done like one or two virtual conferences since the beginning of the pandemic and obviously nothing in person. It's really tough to stay engaged. So, the ones that do keep people engaged, I'm very impressed with. Usually, it's because they have other things going on during a conference. It's just… Yeah. You got to have something to keep you there and keep you engaged because email is always calling and chat and forums and whatever else that's on the web. Yeah.

**Dave Jones:** It's too easy to get distracted and check Twitter and… Yeah. Yeah.

**Chris Gammell:** Yeah. Exactly.

**Dave Jones:** Yeah. Right.

**Chris Gammell:** Yeah. Unless you're like posting about it on Twitter and talking, having a discussion there. But I think you just need to have some kind of way to keep involved. Right. In what's actually happening.

**Dave Jones:** Cool. Cool bananas.

**Chris Gammell:** My old company, Supply Frame, got bought. Oh, yeah.

**Dave Jones:** They got bought out. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Like 700 million bucks, dude.

**Chris Gammell:** Yeah. Many bucks.

**Dave Jones:** I mean, they're just essentially an advertising agency, aren't they?

**Chris Gammell:** No. They have like SaaS tools too. That's the other thing. So, they were selling like intelligence tools to big companies. Right. I think there's a lot of interest right now too because you may have heard there are part shortages. I don't know about you, but I'm on FindChips a lot, which is one of the sites I helped use when I was working on when I was there. Yeah. Just because basically when there's no parts anywhere, you're trying to look everywhere and that's kind of one of the things they do.

**Dave Jones:** So, yeah.

**Chris Gammell:** So, yeah. They got bought by Siemens and Siemens owns Mentor as well. So, it's interesting to see that Siemens is moving into this space, big German.

**Dave Jones:** Oh, right. So, there could be some integration with FindChips with that perhaps, maybe. Sure. That's one of the, yeah. Just like Altium bought Octopart and then, yeah, they integrated it kind of thing. Yeah. Yeah.

**Chris Gammell:** I think there's a lot of interest in like the data intelligence side of things, but real happy for my former coworkers. All my friends are still there.

**Dave Jones:** Excellent.

**Chris Gammell:** Congrats.

**Dave Jones:** Yep. Yeah. Was that a, like, did employees own that? Did they have stock options or what?

**Chris Gammell:** It was a private company. So, there was, right.

**Dave Jones:** So, probably not, right.

**Chris Gammell:** It was like venture capital funded. So, it was technically still a startup.

**Dave Jones:** Oh, okay. Right. So, in- 16 years on, I think it was still a startup. Some-

**Chris Gammell:** Yeah, exactly. Vested interest.

**Dave Jones:** Okay. So, I hope, you know. I hope they did get a payday.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Because we talked about that the other week, you know, the advantage of like, and the disadvantage of going to a startup is like, we can pay you in script, but, oh, geez, I can't, I'm having trouble at the local supermarket trying to pay for my groceries in script, you know.

**Chris Gammell:** I always think about the Simpsons sketch where, like, Homer goes to Itchy and Scratchy World and he changes all his money over to Itchy and Scratchy Bucks. Oh, right. And then he walks into the park and everywhere has a sign up that says, we don't accept Itchy and Scratchy Bucks. Yeah, that's right. And they're non-refundable. So, it's just like, yeah. Yeah. Yeah. Yeah. That's how I think about most startup, you know, stock options. Sometimes, though, you know, it works out.

**Dave Jones:** Yeah. Sometimes it works out.

**Chris Gammell:** You know, take your shot. Make sure you're getting a salary, though, too. That's an important thing, folks.

**Dave Jones:** Who was it who we've had? Oh, I forget his name. Sorry. Who we've had on the Amp Hour, who was the co-founder of AkerBot along with Bree Pettis. That's right. Zach. Zach. Yes. Yes. And yeah, I can remember him. Like, he totally abandoned the company, but he still had all the stock in there. And then when it finally got sold, you know, he just tweeted, thanks for the 20 million or whatever. I'll see you on the beach. You know? That's right. Yeah.

**Chris Gammell:** Yeah. And if you follow, it's Zach Smith. If you, I followed him for a long time on Instagram and stuff like that. And true to his word, I don't think he came back to electronics. Right. Yeah. Yeah. If he is listening, we'd love to see you back, Zach. Yes.

**Dave Jones:** We'll have to link that one in. That was a good episode.

**Chris Gammell:** Living it up on the beaches of Thailand and similar. So last I watched and, you know. Good on him. Good on you. Yeah. It pays off sometimes. Yeah. That's right. Sometimes it doesn't. Yep. Yes. Yep. Yeah. Ah, well. It's a shot in the dark sometimes, but yeah. Let's see what else is on my thing. Let's close it up. I had an interesting conversation about library structures for CAD. And I was wondering if you have any thoughts on how to set up libraries or if you always just kind of walked into systems that were.

**Dave Jones:** No, no, please don't mention the war. Don't mention the war. The war, like internally even at Altium.

**Chris Gammell:** Sorry. Got it. Yeah. So keep going. I think this is what I was talking about.

**Dave Jones:** Yeah. Yeah. When we worked at Altium, there were like, there were multiple ways to do libraries. Let's just put it that way. And there still are in Altium. There's multiple ways to do it. And in the time that I was there, the four years I was there, it was like, it was still not clear the direction the company was taking. You know, the company really hadn't solidified, right. Everyone should use, this is the way to do libraries. It was like, meh, you know, here's all the different ways to do it. Pick whatever one you want kind of thing. You know? So it was like. Yeah, that doesn't work. Yeah. So our own hardware group, we went, well, we're going to use this method. And, you know, it was like, yeah. So I know what it's like these days. It's all.

**Chris Gammell:** So I've been thinking about this for KiCad and I was talking to someone about, you know, they were basically, they're, you know, getting started with KiCad and they were, they were asking me about it. And I was thinking about, it was like, maybe we just need to draw a line in the sand and be like, here is a way. It doesn't have to be your way. Yeah. It's not necessarily the way, but it is a way. You know what I mean? And like.

**Dave Jones:** I think there should only be one way to do it. I think a CAD tool should really should have one way to do it. And everyone uses that. Interesting. I like, because it was just so frustrating. It was like, you know, like how.

**Chris Gammell:** What was the justification to switch between the different ways though? Is it because there's some inflexibility somewhere?

**Dave Jones:** Oh, it depends where you came from. It depends if you had legacy stuff. You know, a lot of people had legacy libraries and they were just used to doing it that way. So Altium couldn't just suddenly abandon support for that, but they also want to push the tool in new directions and follow new, you know, cloud-based, you know, there's many reasons to go to like, you know, proper cloud-based libraries and things like that. Right.

**Dave Jones:** Okay.

**Chris Gammell:** So some of this is sort of like a file-based versus database-based. Right. That's like one, one way of thinking about it.

**Dave Jones:** Well, there's at least three major ones with any, well, you know, there's like, you keep your own local ones and you do it per project. Well, even that's split into two, right? You can either keep a global library local for yourself. Yeah.

**Chris Gammell:** So it's like on your machine. Yes. And you've got like the Chris library. And it's on your. And everything that I use, I have a common library.

**Dave Jones:** You have a common library across all products. The other way to do it, of course, a lot of design engineers, and there's nothing in, some say there's nothing inherently, you could argue there's nothing inherently wrong with this, is to do a project-based library. You have a library for each project and you build it up as specifically needed for that particular product. And, you know, and there's pros and cons, both ways of doing that. You can't say one's better than the other. It depends on the circumstances. Right. And then, then you've got a central. So I can't. God. Used it so in. Spins out of the Altium loop for so long. Then there's the central server. So you don't keep it local anymore. Right.

**Chris Gammell:** So now like the company, the company has one and you basically. Right.

**Dave Jones:** And then, and then you actually set up a dedicated server. Right. A data, like it's, it's actually a server product. It's a software.

**Chris Gammell:** Yeah. Like phone's home. And now it's almost like a, like a GitHub style. It is something like that. Yeah. Local remote. Yeah, exactly.

**Dave Jones:** I can't, God, I can't believe I can't, can't remember the name for it. But anyway, yes, it's, or it's the vault or whatever the vault servers or whatever.

**Chris Gammell:** Yeah. The vault's one thing. Yeah. Right. But the downside to that is now if you have a company librarian and they update a part and you're working on design that doesn't, hasn't been updated yet. Does it pull it in?

**Dave Jones:** Or has some unique requirement and where that thing doesn't, you know, no, sorry. I need something very, I need an ultra tiny footprint because I'm working on a watch product, right? A tiny, ultra tiny. So I have to use ultra tiny pads. Whereas somebody is working on a nine inch rack mount unit. They don't want that footprint.

**Chris Gammell:** Right. They want, they want the extra copper to help pull the heat away.

**Dave Jones:** But, but it's an identical part, right? You both use the same part. It has the same bomb number. It has, it comes on the same reel. It, it, it's in the same place on the pick and place machine and everything's programmed the same, but you have different footprints. Right. And then you have, well, do you have alternative footprints that you can use, but then they go and update that. And it's like, oh, it's, it's just, it's a mess. And then you've got the cloud based, the whole idea where it's a global thing. Not a, it's not just company wide. It's global. It's like, oh, well, there's only, of course, there's only one footprint for an 0402 component. Why would you use anything else? You idiot. Right. Of course. No, everyone in the world should be using this one footprint for this 0402. And there's people who argue that this is a good way forward. Right. That there's one universal footprint that everyone should use. Right. And, and in some cases that's true. In other cases, no, that's bullshit. Right. And there's just, there's so many ways to, it's just, it's a mess. It's just an absolute mess. And then within that.

**Chris Gammell:** I think there is a lot of depth within that too, but you said there should be one way at a company. Does that mean you have a preference personally?

**Dave Jones:** Well, it depends on the product I'm working on, quite frankly. Right. Cause I've worked on products that have different requirements. Yes. It's physically the same part, but I want to use different footprints or I want to.

**Chris Gammell:** No, no, no. I mean, I meant, sorry, the library setup. Oh, the library setup.

**Dave Jones:** Oh, I, I, I, I.

**Chris Gammell:** Cause this also kind of got me thinking. So last week we had Jan on the show too.

**Dave Jones:** I would say that a company should have a library. A company should have a company library. I think that's the best way to start from. And then if you have individual requirements, you deal with that. I think that's probably your best bet.

**Chris Gammell:** Yeah. Right. Yeah. So we had Jan on the show last week from parts box and he was also, we were kind of talking about this as well with meta parts and all that other stuff too. And so that also got me thinking about the centralized database idea. And like, if, if you're buying parts and I was thinking about my time at Keithley and like, we had like customer part numbers, they were specific to us. They, you know, there were some alternates that you could have in there, but basically if you have a part that's an in-house part, you should definitely have a centralized database for that. Right. And I actually liked that, but there was a librarian that did all that stuff. So it was like, you know, the overhead to do that sort of thing is significant. I think it's just like, so it's also like, where, where are you in the scaling of the whole thing of like, how big is your company? You know, how many parts do you use in a year? Yeah. How many products you got? How long does it take to get a part made? You know, like what's your approval to get a part into your system in order to get purchased by your purchasing group? Yeah. Yeah. For that sort of thing. It's just crazy.

**Dave Jones:** And then within Altium, like our hardware group, the four of us, we were, who were designing the hardware products, we were using, we ended up using SVN, the Tortoise SVN. Yeah. Right. Interface for our component libraries. Right. And that's another subset of how to do it. Right. Rather than just like local ones that say with the project, it's a Tortoise SVN based, which is like a GitHub kind of, you know, thing.

**Chris Gammell:** Yeah. I mean, subversion is another, uh, it is. Sorry.

**Dave Jones:** Tortoise goes on top of subversion. So it's SVN is subversion. So it's, but we use the Tortoise interface on top of that. Something like that. Okay. And yeah. And that's how we were doing it. But that's, I think we, we weren't unique on that, but Altium supported it, but that's not what we were pushing at the time, but that's what our hardware group, we weren't pushing that as a company. Right. As, as, as the solution, but that's what we were using internally in our hardware group, just because at the time when we started that, well, it, it seemed a reasonable way forward and we just stuck with it. Right. And it seemed to fit. Yeah. It fit in and we stuck with it. We were used to it. It became your legacy too. And it was like, you know, yeah, I.

**Chris Gammell:** Yeah. Yeah. Yeah. And I think that, so if, if there is a line in the sand, I think it's important to, to basically couch it in terms of like what it's used for. Right. So it's like, here's, so probably what I'm going to do is like, here is a small engineering company, KiCAD setup for a library. Right. That I think is the best practice. That would be like what I'm going to move towards and develop. But it, it's really, it's Chris's small company. Right. KiCAD setup. Right. Because it, it, it could be totally wrong for another group too. But I still think that like, when someone asked you, when someone asked me, I suppose not you, you, you as well, but someone asked me like, what is the best way to do it? It's, it's always tough to be like, well, there's so many ways. Most people just want you to say, here is a way or the way. And yeah, give it a shot. See if you like it. And if not modify from there, you know, it's like, it's like a template almost.

**Dave Jones:** But, but then when you go and then modify from there, that's the, that's a path that leads to the dark side. Right. It's like, because then you're doing it different. It's like, yeah. It leads to suffering. Choice leads to components suffering. Yeah. Right. Right. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh God. It's just, oh. So yeah, it ended up like the hardware group in Altium was doing, was using, you know, a different system than most of our customers. You know, it was kind of like, oh, you know, but yeah. But it was good. Like I, I, I didn't mind it. The way we were doing it was okay. And everyone was happy with it and, you know, but it wasn't the way we were pushing. So, oh, it's just, it's just a mess. Yep.

**Chris Gammell:** You were dog fooding the process. It sounds like, and pushing back pretty hard.

**Dave Jones:** Well, I've mentioned this before. We were supposed to eat our own dog food. If people don't know this term, it's a, it's a, you know, a startup or it's a, you know, industry term, which means you're supposed to use your own product.

**Speaker ?:** Right.

**Dave Jones:** Good or bad. You're supposed to use your own product. Yeah. So we were, we were supposed to eat and, and also within, especially in software companies, in terms of what it meant at Altium, eating your own dog food meant you had to use the daily build. And I'm not kidding. Right. They would let, they would build a new version daily. So it would pull in all of the code changes that the, that the programmers had made overnight. Right. And pull it in. It had run some automated test stuff to make sure it wasn't broken. Right. They had these automated, you know, really advanced things to, you know, check it, do exhaustive testing. And then it spat out this new version. And we were, the hardware group that were trying to do practical work. We were supposed to use the daily build. We were supposed to update daily and, and, and use the latest build.

**Chris Gammell:** So how often did you actually update? That's what I really want to know.

**Dave Jones:** How often did we actually update it? Well, yeah.

**Chris Gammell:** Did you have like the secret version? We had, we all agreed.

**Dave Jones:** We all agreed on one version that we thought was the most stable and the best. And we, oh yeah. Yeah. Yeah. And for real work. Right. You pick it out and you say, here's the most recent stable one. Here's the most recent stable one. Last Thursday was the one. And all of us agreed. Yeah, totally. All of the hardware group. Yeah. We all agreed that that was the best. And we all secretly use that to do any serious work. Yeah. You know?

**Chris Gammell:** Yeah. Yeah. Yeah. As we move towards V6 of KiCad, this is, this is a very common, this is a common occurrence right now in the KiCad world as well. Right. Okay. You gotta, you gotta just pick your battles. Yep.

**Dave Jones:** Yep. And yeah. So yeah, that doesn't surprise me that that's in the KiCad world as well. So yeah. Yeah. Anyway. So that was, yeah. Interesting. But the most interesting part of that is I was like, I was so scared that using another build would break my files, right? Like if I, if I edited in this daily build, I would lose that day's work or whatever that week's work because they changed the file format or something had changed. My files wouldn't import anymore. Never happened once. So I'll, I'll take my hats off to the way the programmers at Altium program, the file structure in that you would never break it. It doesn't matter what crappy build you use that day. It had never, you could save your files, you know, like, like the program. Like if it was a horrible build and something went horrible and it was buggy as hell. Right.

**Chris Gammell:** What I'm really thinking here, Dave is, is, is I, I kind of wish, you know, like how you always say, like, I wish your projects don't work. I kind of wish that in the first week it would have just completely ruined one of your sets of files. And then you'd been like, you know, I should really get into revision control. You would have been like, oh yeah, this is, this is a thing now. Yeah. But you would still use, lose that week's work. Oh, true. Yes. Yeah. Yeah. You would still, yeah. You'd burn it. Yeah.

**Dave Jones:** Right. Because the fire, it actually corrupted those fire, right? Like you couldn't then load it back into a stable version, but that was never the case. I never encountered that once. I was amazed. I was absolutely amazed.

**Chris Gammell:** My revision control is, it prevents that.

**Dave Jones:** Well, your, your revision control is dependent upon it always working. Right.

**Chris Gammell:** Nope. Nope. No. I mean, it's so.

**Dave Jones:** Oh, I, I, you store the entire copy of the file, right. Of the, of the program, right. The working copy of the program.

**Chris Gammell:** No, I mean, so like, so I do a revision control. So today's Thursday here. And if I end, end of the day and I do my final commit and I push it to the server. And then Friday morning, I come in and I pull down a new version of KiCad and it completely corrupts that file. I just go and grab yesterday's files from the server.

**Dave Jones:** But if you've been using that version for a week and you've done a week's worth of work and you suddenly find, oh, it's all corrupted, then you've lost that week's work. Your version control isn't going to save you. It's not going to save you. Sure it is.

**Chris Gammell:** Cause I, I, I do, I do commits every day. Like multiple commits a day.

**Dave Jones:** Yeah, but you're committing in that new corrupted version. So if, if, if, if you, that's what I'm talking about. If you have to go back to that stable version and this new file format that you've got is not compatible with that old version, you've lost that week's work. You're screwed. That's what I, yeah.

**Chris Gammell:** You're saying that all the changes. Yeah. Yeah. Okay. Yes. That would be.

**Dave Jones:** That is the fear I had out him and it never happened. It was amazing. Regardless of how crap that build was, the files would be compatible. I was stunned. Yeah. So anyway. Hats off. Yep.

**Chris Gammell:** Hats off.

**Dave Jones:** That's it. Interestingly, can we talk about the, it's not on the list, but Audacity, which we use. It's, it's split. Oh, they, they got bought out by, I can't remember which company. You know what? Muse. Yeah. They got bought out by a company called Muse. That's right.

**Chris Gammell:** People do Muse. Muse score. Muse score or something. They've got some other music products or something. Yeah. They do like a musical transcription or whatever it's called.

**Dave Jones:** But anyway, the, the open source Audacity, if you don't know, Audacity is probably the number one audio editing sort of like open source kind of audio editor.

**Chris Gammell:** Yeah. Kind of thing. They estimated 20 million users.

**Dave Jones:** Yeah. Yeah. Yeah. So it's a lot for an audio editing tool. And yeah. And it's the one we use and they, they got bought out and within the ink wasn't even dry on the contract. It was less than 24 hours. Wasn't even dry on the contract before the company started adding tracking stuff into the source code. Wow. Wow. So all of the users suddenly went your trackiness bullshit. And they were using the F word. They were starting to mention the F word, the fork word. Right.

**Chris Gammell:** Uh-huh. Yeah. Yeah. Record scratch. Record scratch.

**Dave Jones:** 20 for less than 24 hours to, to talk about forking. I mean, come on. You gotta, you gotta have a little more time. At least wait six months or a year, you know.

**Chris Gammell:** Exactly. Yeah. Sneak it in later. Come on, man.

**Dave Jones:** Dickheads. Oh, unbelievable. Yeah. Yeah. That's just, that's dumb ass. Really. Anyway, we're way over our amp hour.

**Chris Gammell:** We are. I have, I have a baby crying at me from downstairs. So I gotta go. I gotta go help out there.

**Dave Jones:** How's the new found parenthood?

**Chris Gammell:** Oh, that's great. Yeah. She's adorable. Yep. Yep.

**Dave Jones:** It's easy at the moment. I'm telling you. The fun comes in a couple of years when they start. Yeah.

**Chris Gammell:** I know. Yep.

**Dave Jones:** Anyway.

**Chris Gammell:** I've heard all about it. Cool.

**Dave Jones:** Catch you next time.

**Speaker ?:** Bye. We'll see you next time.
