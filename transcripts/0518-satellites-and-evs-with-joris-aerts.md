---
episode: 518
title: Satellites and EVs with Joris Aerts
url: https://theamphour.com/518-satellites-and-evs-with-joris-aerts/
---

**Starlink:** This is The Amp Hour Podcast. Released November 22nd, 2020. Episode 518. Satellites and EVs with yours. Welcome to The Amp Hour.

**Chris Gammell:** I'm Chris Gammell of Contextual Electronics. Hi, my name is Yoris, and I currently work at Hyber. Hey, Yoris, how you doing? I'm good, thanks. How are you?

**Starlink:** I'm great, I'm great. People may recognize the name Hyber because we had Martin on about a year ago, well, probably more than a year ago now, probably like a year and a half ago, and who but introduced us to Hyber but Yoris. And yeah, so thanks for doing that.

**Chris Gammell:** No problem.

**Starlink:** So if people don't remember, Hyber is a IoT-centric kind of satellite company. So basically they're doing a modem that then talks up to a bunch of small sats that kind of circumnavigate the Earth, and you get certain windows where you can talk to the satellites. Is that a good characterization?

**Chris Gammell:** Yeah, that's about right. So we're planning to build a satellite constellation of small satellites that can basically allow small devices on low power to relay some messages a couple times a day.

**Starlink:** Yeah. And I've been asking Yoris about like, so Yoris and I know each other. He was very, very nice. And when I was going to Amsterdam like three plus years ago now, he's like, hey, why don't we hang out? And we'll talk about all the stuff that we got to hang out and see there. But, you know, like we got to know each other from that. At 7 a.m. At 7 a.m., that's right. And he came and picked me up, which was really nice. And like, so we got to hang out there and we've just kind of kept in contact since then. And pretty much like, I would say maybe not every episode, but like most episodes, Yoris will send me a message and be like, you know, something about what we talked about on the amp hour. So it's really, it's good to have like, Yoris is like the voice of the audience here. It's great.

**Chris Gammell:** And it's usually live. So I don't wait until the end of the episode. But I always like, as I hear it, I need to instantly send you a message of what my opinion.

**Starlink:** Right. And so because of the seven hour time difference, usually I wake up to some messages like, what are you talking about, Chris? This is so dumb. Or, you know, or very positive things too. But, you know, it's more shocking when it's the...

**Chris Gammell:** Or like, thanks for this cool part I didn't know about. Yeah, right.

**Starlink:** Yeah. So Yoris is the direct line from the audience back to me, which is great. It's good.

**Chris Gammell:** Someone has to do it.

**Starlink:** Yeah. Well, what are you going to do this week? That's the real question. Oh, yeah.

**Chris Gammell:** Oh, yeah. I'm not sure. I don't really like listening to myself. So we'll see. Yeah, you got to do it.

**Starlink:** Sorry. You got to listen. All right. I'll do it. Yeah. Get some feedback. What was he talking about? Yeah. So you introduced us to Martin and you're doing this stuff. And one of the things actually I... You and I talked about when I was mentioning on the show was Starlink, right? So Starlink is this new SpaceX thing. It's got satellites going up and things like that. And I thought that maybe there would be an IoT solution there. But it doesn't actually seem like that's going to be... I mean, it's not what they're targeting, but I thought maybe they'd have access to it. But it doesn't necessarily seem like that's going to be the same thing. I mean, because space has got a couple different segments.

**Chris Gammell:** Yeah, well, I mean, who knows? They're sort of in similar orbits as we are. But I think they're currently really focusing on providing actual internet. So high bandwidth. And so you're mostly looking at more gateway type applications since their ground setup is a bit more complicated than ours. So you're not going to see... I think it's... They call it the pizza box or something. It's a phased array antenna. Yeah. So I don't think you'll see that sort of on a poke in the ground to monitor humidity or something.

**Starlink:** Yeah. And I guess that's what it comes down to, too. It's like... So like we talked about when Martin was on the show, it's like... The idea is... So you have like this weird kind of dome antenna, right? On the IoT thing for Hyber. And it's more like you know that at certain times of day, there's going to be a flyover. Versus like with Starlink, it's going to be like there's just a crap ton. I mean, there's still... There are flyovers, but it's... You have to kind of track more instead of timing it, right?

**Chris Gammell:** Yeah, you need to. It's more like you do with a cellular network, except that here the antennas are moving instead of you.

**Starlink:** Yeah, got it.

**Chris Gammell:** With our solution, it's literally like waiting for the right time and then sending one packet of a couple hundred bytes. And then the satellite picks that up and then relays it down to a ground station later during the pass.

**Starlink:** Yeah. And yeah, and that's why it's like so super low... I guess it is low bandwidth, but it's also just low frequency. Low power. Yeah, low power, right, of course. Yeah, versus someone who's like trying to actually get like a YouTube video through... You know, as the satellite's going overhead, they have to just kind of like track it and be like, Oh, I hope I maintain this connection sort of thing.

**Chris Gammell:** Yeah. Yeah, I don't think we'll be streaming Katy Perry anytime soon.

**Starlink:** Well, I mean, the satellite will be playing it, but who's going to hear it in space, you know?

**Chris Gammell:** We had a sort of a theme song during the naming ceremony of the satellite. Oh, yeah. And we actually stored that in memory. So it will be in orbit. I just, we don't have a way to play it yet.

**Starlink:** Good, good. Yeah, it's like the golden record on Voyager, but, you know, a little bit simpler.

**Chris Gammell:** Yeah, except that this is a really weird polka.

**Starlink:** Really? Yeah. How was that chosen?

**Chris Gammell:** I think just in the days, in the final days preparing the satellite, we needed some, you know, some music to get in the zone. And a friend of ours just randomly sent it to us. And we were like, yeah, this is a good sound to prep the satellite.

**Starlink:** Got it. Yeah. Just really, really motivate.

**Chris Gammell:** I'll send you a link so you can put it in the show notes.

**Starlink:** Okay. All right. That'd be great. Yeah. Me and a group of friends, we used to do a maze party, like a party where you like tape together a bunch of like cardboard boxes and then it's all dark and people climb through it. And like the days leading up to that, there would be a song that would play nonstop as we were building it. It was called James Brown is Dead, which is just like this absolutely horrendous techno song from the 90s. And yeah, so I know how that goes. It's, you know, about the equivalent of a polka. Maybe polka is better, I think.

**Chris Gammell:** So do you have space for a maze in your house or?

**Starlink:** Yeah, we did. Yeah. Yeah. We had a space in the house. So, yeah. That sounds fun. It was fun until there was a fire. It was always a fire risk. And then there was a fire. So not during the party. But yeah, it was no longer loud, but probably for the right reasons. Okay. So let's talk about the satellite. So one thing that we didn't get to talk about with Martin when he was on is like, you know, he talked about a lot of the business and a lot of what was like kind of going on there and the mission. Yeah. The bands and stuff like that. But we didn't necessarily talk about the satellite. And so like what is actually on, you know, like one of these, these small scale satellites? What's the size of it? What does it look like? What's it what's on board?

**Chris Gammell:** Well, first, I want to kind of give a heads up that I'm not an RF person. And also, the more I've had to deal with it the last couple of years, the more I kind of hate it.

**Starlink:** Yeah. You just you just wipe your hands of it. You're like, I'm done. Yeah.

**Chris Gammell:** Like, I'm happy we have people for this. But unfortunately, it kind of is just a bunch of antennas strapped together in a box. So I got a little unlucky there.

**Starlink:** Well, there's got to be others. I mean, like, so what part are you working on then?

**Speaker ?:** Yeah.

**Chris Gammell:** So so I basically did all of the electrical integration and some of the mechanical integration. And since it's a satellite is pretty small, it's it's called three U and when you is a cube of 10 by 10 by 10 centimeters. So our satellite is like 10 by 10 by 30. And then it has a bunch of deployable antennas and deployable solar panels. So when everything is deployed, it's a little bigger than that. But yeah, so that's the space that everything needs to fit in. And then, of course, you have your your maximum point power trackers for your solar panels. You have a battery charger, the battery, you have some some power distribution that also does monitoring and protection against latch ups or other weird things that can happen that could damage your spacecraft. And then it's essentially a bunch of radios and a processing module that takes the takes the RF samples and does something to it and stores it and then beams them down later.

**Starlink:** Yeah. I mean, you're saying it's like this simple thing. You make it sound kind of simple, but I just imagine the amount of storage and just checking. And I mean, like how much how much redundancy is on there, for instance?

**Chris Gammell:** Well, isn't the essence of engineering to to make things simple?

**Starlink:** Sure. Yeah.

**Chris Gammell:** I mean, of course, there's always a bit more to it, but it's it's all existing technology. There's there's nothing really crazy in there. It's just usually a lot of time and effort has gone and making it reliable as you can't really poke at it anymore after after you launch it. And you usually only have one or a handful. So it's not like if 10 percent of my my units dies, I'm still happy. Then. Right. If if if that first satellite is that first 10 percent, then you have a problem. So.

**Starlink:** Right. So you're not doing like so like other space type stuff in the past I've heard about was I guess less so with like the other space companies we've had on here. But like, you know, traditional space is like, you know, the triple. Oh, actually, that was Brock Lemares is talking about that with like triple redundancy processing, things like that. So you're not doing like lockstep processors or anything like that.

**Chris Gammell:** Yeah. Yeah. There's a couple of different approaches. Like back in the days, everything had to be, you know, actual radiation, harden it and all super custom, all super expensive, like tested to infinity, basically. So you have 100 percent confidence. But because technology has been so changing so quickly recently, that basically means you're always stuck with 30 year old microcontrollers, if you can even call it microcontrollers.

**Starlink:** 8050 ones are the best. Yeah. Yeah.

**Chris Gammell:** I think there's also a lot of power PC in there somehow.

**Starlink:** Oh, got it. Yeah.

**Chris Gammell:** But so then what, for example, SpaceX is doing if I this is also just from what I see on the Internet, but they take new stuff, but then just have everything. Like super redundant and their mission missions are also relatively short. Right. If you go to the ISS and come back, you're in space for, you know, maybe a couple of months top, but you're not staying on Mars for tens of years. So like total radiation dose is not so much of a problem. You're mostly concerned about like faults as a result from radiation. That's something that you can fix with having triple redundancy. So that if one device goes down, you basically have a majority vote and things can keep running without having to reboot the whole thing.

**Starlink:** Mm-hmm.

**Chris Gammell:** And so what we are doing is like, we don't have any really sort of life critical or, or other critical systems. So we just designed the whole system that it can just gracefully reboot quickly and then resume where it has left off.

**Starlink:** Got it. Yeah. So like a worst case scenario would be if someone like, so like I'm monitoring humidity out in the field somewhere. I wait for my daily window. I send up a packet as this, this satellite is going overhead. The humidity is 34. Oh, so exciting. And then if like memory gets corrupted on that, as it's like waiting to downlink it to the base station, that'd be bad. But you're saying it's not like end of the world and you have other checkings.

**Chris Gammell:** Also, in that case, you usually still have some, some checksums and whatnot. So like if, if a bit flips, then you can, you can usually recover from that. It's more like a microcontroller resets. Got it. So what that means would that you sort of miss maybe like a couple seconds of RF data. And that's something that you can, can work around by, you know, either sending the message, the messages a couple of times, or, you know, basically picking a service plan where if you miss the humidity for, for one sample, then, you know, there's no real harm done.

**Starlink:** Yeah. Yeah. I was surprised I've used global star. No, what's the other one out there. So there's iridium and then there's. I think it's global, not global, global star, something like that. But there was like an older, like space, older satellite based technology and there's modems you can get and stuff like that. But one of the things that it says is it's like, yeah, send your message six times. And it was just like, that was part of the protocol is to just send it six times, which sucks for power, but it also sucks worse if you miss the data. So. Yeah.

**Chris Gammell:** And I think that's also a result of, you know, there's, there's all these nodes on the ground that are not necessarily synchronized and they're all just basically send a will. So you can always have bad timing where two messages arrive at the same time.

**Starlink:** Yeah. That's interesting. So like, is there, is there a spec on density of things in an area or is it more, you just kind of hope that there's not. It's almost like an automatic retry. Yeah.

**Chris Gammell:** Yeah. Well, well, it's mostly one way traffic, so there won't be a direct acknowledgement after the message has been received. But so we basically have a bunch of models that define what the statistical failure rate would be as a result of a number of nodes in a certain area. As soon as that gets problematic, you just need more satellites. So, and that's, that's kind of what our, what our business is built on that we can, we can scale along with basically customer demand.

**Starlink:** Yeah. And so the device itself wouldn't know whether or not it made the transmit. So again, the humidity, so we'll, we'll keep this, this, this ruse of a example going here, but like a humidity sensor in a field, it wouldn't know that it did or did not update its stuff. It did or did not, did or did not have a certain packet get there, or it does have any knowledge downlink.

**Chris Gammell:** Well, in theory, we, we, we can do downlink and we'll, I think we're also still planning to support that in the future, but we have, we have much more limited downlink capacity. So like basically anytime we're sending any packets downstream, we cannot receive any packets.

**Starlink:** Oh, right. Right.

**Chris Gammell:** So, so you want to, you want to limit it.

**Starlink:** Right. And the device in the field, the humidity sensor probably doesn't have like a full duplex second antenna array that can handle other frequencies or something like that.

**Chris Gammell:** No, that's fine. It can definitely receive packets, but it's just that it's much cheaper to just send the packet, you know, three times or not worry about one packet that, that hasn't come through then to acknowledge every packet for every device.

**Starlink:** Got it. Okay. So it's just simplifying it to the point where it becomes economical almost. Yeah.

**Chris Gammell:** Yeah. So I think we're really going after, you know, a niche market where we, we can make the product really cheap, but of course you have to make some trade-offs there. So as soon as you start adding all those requirements on, you're probably better off with a different solution, like the ones you already mentioned.

**Starlink:** Yeah. Yeah. I guess there, I mean, there are more that are out there. It's just, it's crazy that there's, you know, this is obviously a burgeoning field. I think from my perspective as someone who, you know, makes IOT thingies and has clients who are asking to go to more and more remote locations that might not even have cellular anymore. It's like, it's, it feels like it's coming up, but it's just like, I'm sure that there's this like push pull of like, well, you can't go and invest like a ton. You know, you could, could go and throw a ton of satellites up in this, into the sky, but it's just like the cost of doing so if there's no business behind it. I mean, that's basically the, uh, that's the premise of eccentric orbits, right? That whole book is about like, they just went forward anyways.

**Chris Gammell:** Yeah. That book is crazy. Yeah. Yeah. Thanks for the recommendation, by the way. I must say I haven't finished it. Like it was super exciting, but at some point it's just sort of investing investment deals that don't go through and then go through and then don't go through. So it's right. Right.

**Starlink:** Yeah. And if people don't remember what we're talking about here, this is the book about Motorola and the Iridium constellation and then how it didn't, it didn't work commercially, but then it got saved by this individual. And there's the story of that. And that's why the deals at the end were really, yeah, it's boring.

**Chris Gammell:** So I like the parts where there was like a guy in the room behind the self-destruct button. Yeah. Right.

**Starlink:** Yeah. They just really wanted to blow that stuff up. You know, they just did not want it around anymore.

**Chris Gammell:** Yeah. Yeah. But it's weird. Like you mentioned, like a lot of these other vendors that have satellites in the air for like a long time already, but it appears that everybody is starting to only now become aware of it or something.

**Starlink:** I think as there's more hunger in the marketplace for it. And, you know, there's, I don't know, like there's certain industries I feel like that are just growing in their technology adoption. Right. Even like the, I mean, oil and gas has always led a lot of the space, but like there's just more vendors that are serving that industry now, you know, for better or worse. And the same thing with like agriculture.

**Chris Gammell:** Yeah. And I guess people are starting to realize we can measure something here. Maybe, maybe that's what's driving a lot of it.

**Starlink:** Yeah. Yeah, exactly. And it's just, yeah. So it's like, yeah, there, there's some kind of economic incentive that's driving a lot of innovation. But the reason there's been barriers in the past, especially like not being able to get the signal back. And so that was, that's starting to come down finally. And it's like this, all of these different things kind of come together. Like agriculture is probably even, even better example of like, you know, it's just like farmhouses 20 years ago had even less connectivity than they do today. But you could have, you know, you could have a farmhouse that actually has fiber in some parts of the world now, and you could use that to back all your data even. Or you could, you know, if you're really, really remote, you could go and, you know, use something like satellite. So it's, there's just more options, I think. And that drives more innovation. Yeah. What about, so on the actual satellite itself. So you mentioned there's, you know, a lot of RF stuff, but I imagine that that would be pretty power hungry compared to the overall like power budget of a satellite. Like, are you, does that mean that then you as the person that's kind of helping to enable these RF engineers that you work with, like, do you have, are you really like power constrained than otherwise?

**Chris Gammell:** It is kind of tied. I think it's mostly limiting the lifetime of the satellite because your solar panels degrade over time. Oh, really? Okay. So if you can reduce power consumption, it essentially means your satellite will be economically viable for a longer period of time. Mm-hmm. Basically, power is always a limitation and it's not just power consumption, but also the amount of heat you can get rid of.

**Starlink:** Ah, yeah. Yep. Yeah. Because you can't like put like huge heat sinks on there either, I'm sure.

**Chris Gammell:** Well, you're, you're basically limited by, by the surface area that you have to, to radiate your heat away. So you can have like fancy quadruple deployable solar panels, but if you can't radiate that heat away, then yeah, you can't really use all that power.

**Starlink:** Yeah.

**Chris Gammell:** Like when, when we design our systems, power consumption is always one of the, it's always in the back of our minds. And then, yeah, usually it's, uh, it just kind of comes together.

**Starlink:** Yeah. Well, I'd hope so.

**Chris Gammell:** Yeah, no, it's like, yeah, it's, I guess maybe it's not like how real engineering is supposed to happen. But so we kind of had a philosophy where, you know, we try to get the power consumption on every system as low as we can. Sure. And then, uh, we'll, we'll, we'll see where that gets us. And then, uh, we like worst case, we'll have to reduce our, um, our duty cycle a bit where we maybe for this first generation, not sample over certain regions or, or do some other tricks to, to save some power.

**Starlink:** Yeah. Yeah. Yeah. I mean, I would imagine that there's, there's some inherent like constraints just on how much, how much solar can you fit on there in the first place. Right. That's like your very, very outer constraint. But then like you're saying, like the heat is another one. And, you know, what I heard you saying with the, you know, it just kind of comes together is like, there's just some realities that you have to deal with. And then there's margins of error and things like that. Yeah.

**Chris Gammell:** It's basically, we have this much energy available. We try to make everything as low power as possible. And then that's kind of what it is.

**Starlink:** Yeah. Yeah.

**Chris Gammell:** Of course you want to ideally sort of know that before you launch. So of course we did some simulations and measurements and calculations, but you never really know until you're really into operation.

**Starlink:** Yeah. Right.

**Chris Gammell:** But yeah, it's, it's not like if like we're, we're not going to launch because we didn't meet our power budget or something. Yeah. Yeah.

**Starlink:** Yeah. And I mean, I guess if you can turn things, you know, if you have all the different ways to turn things on and off, you can always, you know, send software updates to, to start to turn, you know, basically optimize for, for what you have available.

**Chris Gammell:** Yeah, definitely. So for updates is a big part of this project.

**Starlink:** Yeah. Yeah. When you're doing that, that initial calculation, I guess I never really thought about it like this. Like, you know, I live in a very cloudy city, right? Amsterdam is pretty cloudy too, I think. And so like, I always think about like solar is, you know, it's like, Oh, it's not that big a deal. You know, like it's not a huge benefit to have solar on projects here. It's better than nothing, obviously. But like, is there anything in space where you have to like, do you have to like calculate the like solar ebbs and flows? Like you get full sunlight when you're facing, when you're in the, not on the dark side of the earth. Right. But like, is, is.

**Chris Gammell:** Yeah. It's actually much more straightforward. Yeah. There's no weather up there. So you just know your orbit and the orientation of your spacecraft and you know, the data sheet of your cells. So it's, it's pretty easy to, well, I wouldn't say easy. I didn't do the calculations myself. So credit to my colleague who did, but, but you can actually get, get very close to the actual value. Got it. Because there's much less variables.

**Starlink:** Yeah. Yeah. I guess I just don't ever really think about that, but like, and there's not like, it's not like you don't collect dust on there either. Like things that like on even sunny places, you have to like clean off your panels. Like Dave always talks about having to clean off the, you know, the solar panels in Australia. And it's like, yeah, I mean, that's something, but it's really sunny there, but you don't have to do that in space, obviously. So it's just like this kind of optimal, probably the best case scenario for solar.

**Chris Gammell:** Well, well, the downside is you do collect some charged high energy particles.

**Starlink:** Oh, really? Okay.

**Chris Gammell:** Yeah. So that's what I mentioned in, in terms of degrading over time. I think that's, yeah, that's just, uh, inherent. Also, most of electronics is shielded behind a bunch of aluminum, but the solar cells are really out there. So they're collecting a bunch of particles flying through space.

**Starlink:** Got it. So that'll be like, uh, like just like a high energy particle, like go and knock out like a, like a doping element inside the solar panel itself. And it won't, won't be effective.

**Chris Gammell:** I think that's what it is.

**Starlink:** Oh, okay.

**Chris Gammell:** Hmm. It's, it's essentially all, all silicon, right? So there's just all these junctions and they kind of become less ideal over time.

**Starlink:** Hmm. Yeah. Yeah. I guess. Yeah. And you wouldn't, I mean, you wouldn't like send up water or other like ways you normally, you wouldn't be able to shield it anyway, because you want to have it. You literally want it to be exposed to as much photons as you can get. So yeah, that's, that's crazy. What is, what is the lifetime overall expected for a satellite? Right.

**Chris Gammell:** Well, it depends a lot on sort of your, your mission and what your, I guess your, your business model looks like. And also how fast the technology is evolving.

**Starlink:** Sure.

**Chris Gammell:** Yeah. Yeah. We're, we're aiming currently at around four years. If I, if I remember correctly, I think it's also changing a little bit now and then, but so that's, that's the ballpark. And the idea is that, you know, after four years, you know, technology has moved on. So you can probably replace it with something better and you can probably make something that lasts longer, but it would be more expensive than just launching one every four years.

**Starlink:** Oh, do you mean to like actually get the benefit of, of the new technology would be less expensive?

**Chris Gammell:** No, I just, I mean like the amount of like money and time you would have to invest to make the spacecraft last longer. Oh, I get it. Works out, you know, negative compared to just launching one every four years.

**Starlink:** Yeah. Right. And that's like, yeah, the same kind of thing with how they're not using rad hard parts. There's not just the technology element, but they're also really expensive parts and you could plan for obsolescence basically or plan for replacement at a certain point.

**Chris Gammell:** Yeah. Yeah, exactly.

**Starlink:** Cool.

**Chris Gammell:** How do y'all get these things up there? We usually catch a ride.

**Starlink:** Yeah.

**Chris Gammell:** Our next launch is with SpaceX. And I think it's part of a big ride share mission. I guess there's a couple of different models. There's one where, you know, there's a big, big old satellite that's getting launched with some free, free cavities here and there where they then chuck some cube sets in. Oh, really? So it's really sort of, you go along for the ride and you get dropped off along the way. But this is an actual dedicator.

**Starlink:** It's the Uber, Uber ride share of space. That's crazy. Yeah.

**Chris Gammell:** Uber pool or whatever it's called.

**Starlink:** Yeah. That's it. Yep. Yep.

**Chris Gammell:** But so this, this launch is dedicated with, I think it's like 60 or like even more. There's a lot of micro and small sets that just all get deployed one by one. And then there's usually like a company that buys up a whole rocket and then resells the pieces to smaller customers. Like we are.

**Starlink:** The landlords of the, of the rocket industry. Yeah. Huh. That's really cool. I mean, do you have an idea of like when the next ones are going up?

**Chris Gammell:** Well, we, we just handed off our, our first in-house design satellite and it was supposed to go up in December, but like things always move around a bit the last. Yeah. Weeks. It's the, the launching game I was told, but it, so we, we handed it off. So it's going to be, it's going to be soon.

**Starlink:** Yeah. Well, I mean, I, I'd say like the waiting is better than like, you know, them rushing it. And so Sean, who was on the show, Sean Meehan, who was on the show, he, he talks about the fact that they were on the one, one of the SpaceX ones that blew up. And it was just like, oh my God, I just, I can't imagine. It's just like, it's a possibility with space stuff, but it's just, holy crap. You know, like, yeah.

**Chris Gammell:** Yeah. I think, I think recently the Vegas rocket had some issues. Like, I think that's the, the European one. I think they had two, two failures out of the last three launches. So, and we were also considering them for, for launches. So you're like, whoops, we, we got lucky, I guess.

**Starlink:** Yeah. Yeah. Yeah. That's great. I mean, that's, it's like, it's just such a, I interviewed Joe Barnard too, from a BPS space over on the contextual electronics podcast. And like, one thing that's always exciting about this stuff is like watching, you know, it's exciting when there are failures, but like, man, it sucks. You know, like it's, it sucks for the people that are doing it, but it's like, it's kind of awesome to watch as long as, as long as no one gets hurt. So of course, of course.

**Chris Gammell:** Yeah. Yeah. He's the guy that's making the model rockets, right?

**Starlink:** That's right. That's right.

**Chris Gammell:** Yeah. Yeah. I listened to it. It was really cool.

**Starlink:** Yeah. I mean, when his stuff goes wrong, it goes real wrong.

**Chris Gammell:** Well, and sort of like his, it's kind of an educational project for him. So if something goes wrong for him, it sucks, but it's kind of. The mission too, in a way, I think. Right.

**Starlink:** Yeah. Yeah. Low stakes other than time, you know, like, yeah.

**Chris Gammell:** Well, and also when, when a rocket blows up, it's like someone else learns, but we learn nothing because. That's right.

**Starlink:** Right. We're supposed to learn when we fall out of orbit. Not when we. Yeah. Yeah. Not when the rocket goes. Damn it. Yeah. That's, that's tough.

**Chris Gammell:** Yeah. That's, it's going to be an exciting time when sort of, when it gets deployed and then waiting for the first beeps. Yeah. Because as soon as you get those in, then at least you have learned something, right? Then you can do some, some telemetry readout and get some, even if it doesn't work, at least you'll probably know what doesn't work. But if you don't hear back, then yeah, it's pretty difficult to figure out what went wrong.

**Starlink:** Right. It's the hello, the hello blinky from, from many thousands of miles away.

**Chris Gammell:** We actually have a blinky on the satellite. So.

**Starlink:** Oh, you do?

**Chris Gammell:** If all fails, we can maybe get a big telescope and.

**Starlink:** Really big.

**Chris Gammell:** See if it blinks.

**Starlink:** You might be better off trying to phone up the ISS folks and asking them to look. Yeah. Where does it, where does this live in the, in the, in the orbit? Like where does it, how, how high up is it?

**Chris Gammell:** I believe we're at like 400 kilometers. Mm-hmm. I think, I think slightly above ISS. So they would have to look up. Okay. Yeah. But if I've actually heard some crazy stories of like cube sets that were deployed and that didn't send back telemetry, but you can still get like a giant scope dish and then listen for the crystals on your, on your, uh, on your microcontrollers to see if they're running or not.

**Starlink:** Wow. That's, that's something that's, that's quite a hobby.

**Chris Gammell:** Size does really matter in terms of antennas.

**Starlink:** Yeah. Wow. That's crazy. So what else, I mean, on the, on the satellite side of things, this is other stuff we want to talk about here too. I mean, on the satellite side of things, like what were some things that are unexpected when working on space electronics?

**Chris Gammell:** I think in a way that it's surprisingly like any other type of engineering, because I joined Hyrule about two years ago with no experience in, in space, but you know, all your, all your engineering rules still apply. So that was, that was a nice surprise, I guess.

**Starlink:** Yeah. Yeah. Yeah. It's not like the lab is at a vacuum or anything like that. So that helps.

**Chris Gammell:** Well, and just like, you're still, you know, you have a bunch of requirements that you try to meet and then you have some trade-offs that you need to make. So it's, there's, there's maybe a bit more at stake in some ways.

**Starlink:** Is testing different?

**Chris Gammell:** Well, I think one big difference is that, so, so before this, I worked at a automotive company where volume is super high. So you basically want to test everything for the shortest time possible. And here we have basically only like a handful of units, but you repeat the same test a whole bunch of times.

**Starlink:** Yeah.

**Chris Gammell:** So I think in the end you do the same amount of testing, but just on like one hundred thousandth the amount of parts.

**Starlink:** Yeah. Yeah. And that's interesting too, about like the having low volume, I mean like super, super high complexity and then low volume as well. I would imagine like having time on the unit or handling it would be maybe higher stress than it might be if you were making a million of something and you're like, well, if this one breaks, I'm just going to go use another one. You know, like it's just harder to, you have to spend more time kind of focused on one unit, I would think.

**Chris Gammell:** Yeah. There's definitely like a more limited supply in units. Like if you, like back in the days, if I drop a unit off my desk, I just like chuck it

**Starlink:** out and just brush it under the desk with your foot.

**Chris Gammell:** Like, yeah. And just get a new one. Like no one, no one, no one saw that. Move on. That's right. But here, there's always a bit more, uh, you know, you always, you're always a bit more on edge. You don't want to damage. I think it actually took me quite some time to sort of feel okay with picking up parts that would actually go to space. Just feels weird.

**Starlink:** So like, like just spending, like spec, speccing stuff is, feels more high pressure.

**Chris Gammell:** No, just literally like physically picking up the parts that you know that will go into space.

**Starlink:** Oh, interesting.

**Chris Gammell:** Like I really had to sort of get over that and sort of like be okay with just handling them. Hmm.

**Starlink:** Yeah. I mean, so like if you're sending, if you're sending five satellites to space, how many, how many total units would you end up producing for that sort of thing?

**Chris Gammell:** Uh, depends a little bit. Usually you build them in batches and then you at least want to have one sort of clone that you keep on the ground after, after they launched.

**Starlink:** Yeah. I saw Apollo 13 as well. Yeah.

**Chris Gammell:** Oh yeah. Cool. Yeah. So ideally, ideally it should be identical, but in the end there's always some, some tweaks here and there that, that don't make it to, to one of them. And then you usually also have an engineering model that is a bit more of, I guess, a bit lower threshold to, to mess around with.

**Starlink:** Got it. Okay.

**Chris Gammell:** Yeah. So if you have your, your sort of your, your golden backup, then yeah, you don't want to mess that up. So you always want to have some extra parts that you can just play with without having to be worried of damaging something because it really slows down testing and development.

**Starlink:** So you mentioned like there's, there's a golden unit and that, you know, this is a multi unit assembly. It feels like, I mean, do you have a standardized form factor internally then as well for creating like a, so if you go and want to create a new, I guess maybe that's a bad example. I was thinking like a new MPPT kind of setup that you want to test, but even more than that, say, say you were like trying to add like a whole slew of new sensors. Is there like a standard board form factor that kind of then all pieces together as well?

**Chris Gammell:** Yeah. And unfortunately there is. And I think it's based on some random student project that decided that, that PC 104 was the way to go. So it has like screw holes at completely insane locations. Like.

**Starlink:** Got it. So it's like 87.24 millimeters apart and they're not on a grid. Yeah. Yeah. Okay.

**Chris Gammell:** Yeah. And then it has this, this giant 54 pin header, which makes it impossible to take units apart after, if you've put them together. Uh, so that, that's been sort of the standard in, in CubeSat world for, I don't know, since it started.

**Starlink:** Is it, is it published somewhere like the, that, that, that's standard?

**Chris Gammell:** I think if you search for a, like a pumpkin space, PC 104 or something.

**Starlink:** Oh, so it literally is PC 104. Okay.

**Chris Gammell:** Yeah. Yeah. It's, it's, it's.

**Starlink:** Oh, wow.

**Chris Gammell:** I think someone, uh, that, that escalated quickly, I think. Oh yeah. Wow. But so, so nowadays like vendors are starting to slowly move away from that because they realize it's, it's not very practical. And so we ended up with kind of our own form factor that we basically arrived on together with a vendor of the majority of our sort of off the shelf systems. And it still has the crazy mounting holes, but, uh, we, we no longer have the connector.

**Starlink:** Yeah. So these look, so the, the mounting, I'm looking at the pumpkin space one, the motherboard module, and I'll link this one in, but it does look like, I mean, it literally, they're like 0.1 inch headers. Is that right?

**Chris Gammell:** Yep. Yep. Wow.

**Starlink:** And that's in space. That's really weird. That's so like, why not just rip all that up and start from scratch? Is it just like a timing thing? You're just like, oh, well, we'll get to it at some point.

**Chris Gammell:** Well, there's, there's always sort of keeping the door open for some off the shelf module. So basically everyone is using these mounting holes and you can usually do some hacking with the wiring, but in the end you still need to stack the whole thing up. Yeah. So that's why these are so, uh, persistent.

**Starlink:** Yeah. Yeah. And I mean, I guess the interoperability is nice. It just seems like, yeah, really inefficient from a, yeah.

**Chris Gammell:** It's unfortunate.

**Starlink:** You're giving up a lot of room there, honestly. And it like the, you know, the, it looks like the standoffs that are in there, you know, they're fine, whatever it seems like. And it's like the, the height, at least on the one that I'm looking at, well, the hell the one I'm looking at has a USB a connector on there as well. So it's got like a pretty significant, you know, amount of height up there. Probably what? Like 10 millimeters. I don't even know.

**Chris Gammell:** Yeah. I think that's the stacking height is usually something around that. Yeah. But so, so we moved, moved away from that and we basically made a generic aluminum box outline and, uh, we use a flex PCB to, to connect all the modules together.

**Starlink:** Oh, that's interesting.

**Chris Gammell:** That gives you much more flexibility in terms of, uh, you know, what do you want to connect to what? Not everything has to be, uh, like a, uh, a bus that pokes through every board.

**Starlink:** Yeah. Right. And so this all kind of leads into like the cube idea, right? I mean the cube, the 10 by 30, 10 by 10 by 30 is like, so you get stacked this whole thing into like a big log of just like stacks of boards. Right. But you're giving up a lot of airspace in between. It seems like.

**Chris Gammell:** Well, so, so our modules are, I think 11 millimeters is the standard thickness and you definitely need some space for, for connectors and, and, you know, some, some parts that are slightly higher profile. So I don't think we end up wasting too much space. Uh, so we basically, like you said, I have our, ever log of our, of our own platform components. And then on top of that, we, we stick everything that is still old school. Yeah. So we still have a couple of boards that are, uh, they're still using that, that PC 104 form factor. And then we basically have a, a legacy interface board that connects those to our bus.

**Starlink:** Yeah. It's really interesting how that works. I mean, I could, yeah, I mean, I could see the benefit and like, so just so people don't think I'm being too conventionally about this, I could see the benefit in one way, especially like the, like you mentioned the, you know, the being able to use off the shelf is like great for testing or validation or lots of things, you know, being able to push that or if you, I mean, or to be honest, if you were ever, you know, if the, if hybrid was ever interested in selling to other companies too, it's like, you'd have to be able to play in the same playground, but it's, it's still, it's like, it's kind of crazy. Yeah.

**Chris Gammell:** It's more like usually you want to, you know, focus on, on your, on your own payload. So in our case, that's the radio. Yeah. Yeah. That communicates to our customer modems, but you don't necessarily want to make your own MPPT. Yeah. So it's, it's nice to have the flexibility to go between either making something yourself or maybe you realize that it didn't work out that well. And then the next satellite, you can swap it out for something off the shelf again. So it gives you sort of this agility to, to go back and forth and, you know, pick what makes the most sense without having to redesign your whole architecture.

**Starlink:** Yeah, exactly. Exactly. Hmm. That's cool. And then, I mean, you mentioned on the control side of things, I mean, are you, are you guys doing mostly just processors, FPGAs as well for the kind of higher data stream type stuff? Like what's, what's on the processing side of things?

**Chris Gammell:** So we, we basically have your, your typical SDR setup with one of those analog devices chips. Then a Zinc to take all the data in. And then, then we process that on a Linux computer.

**Starlink:** Oh, cool. Okay. Yeah, that's great. I mean, and, and are any of those, those are all the custom things that you guys make. Do those then have to still talk to like, is there some like master controller that's like, again, I'm just looking at this one page on the pumpkin industries and then it's like eight or 16 bit MCUs. It's like, oh boy. So like, does it still have to interface with like that?

**Chris Gammell:** A lot of that is still in sort of Arduino land. Okay. But, but no, so our, our Linux machine is the, I guess the, the master controller of the whole satellite.

**Starlink:** Got it. Okay. Yeah. And that makes sense. Yeah. It's really cool.

**Chris Gammell:** It's actually, it's, it's a very distributed system. So if, if any module is down, then you can, everything else can still continue to operate. There's no one bottleneck. Yeah. Between communication. And that also means like we are command and control radio is just a router. So even if our onboard computer dies, we could still talk to the battery module or talk to something else because it's just a dumb router that, that forwards packets back and forth to the shared canvas.

**Starlink:** Oh, okay. It's canvas too. That's good to know. Yeah. That's, that's interesting. I mean, yeah. And I, I guess that would probably also help on the testing side of things too, right? Of being able to, to kind of plug a board in like this. And it's just talk, if it's just talking on canvas, you can just put a simulator on the other side or, or something like that to, to actually test the board itself.

**Chris Gammell:** Yeah, exactly. And in, and just in general, it's really nice to keep the amount of IOs to, to as little as possible because all of those need protection and they need to be tested and just more board space, more connector pins. So we really try to, you know, really limit everything to, to the canvas and then use that for everything. And it also means that in terms of test equipment, you really just need a can dongle and usually a programmable power supply and that's it.

**Starlink:** Oh, that's nice.

**Chris Gammell:** Yeah.

**Starlink:** All right. Well, a canvas is a great lead into, you mentioned a car manufacturer earlier. Uh, yours, what's a, what car manufacturer did you work for?

**Chris Gammell:** It was, uh, an electric car manufacturer in California.

**Starlink:** Uh huh. Uh huh. Yeah.

**Chris Gammell:** Yeah. Yeah. It's, it's, uh, it was Tesla.

**Starlink:** So this is actually when yours had mentioned to me, it's like, Hey, do you want to come visit the Tesla offices in Amsterdam? I'm like, uh, okay. I didn't know there were Tesla offices in Amsterdam, but yeah.

**Chris Gammell:** Yeah. I guess that was my, my trick to, uh, to make you come over.

**Starlink:** Yeah. Yeah. Yeah. But yeah. So what did you, what did you do at Tesla? I mean, so this is the, you know, very high mit volume manufacturing you mentioned as well. Obviously you'd mentioned as well that like there, there isn't a lot of difference. It's interesting how you said that there isn't a lot of difference from the engineering side of things, but I would imagine the constraints are kind of wildly different in that way. Yeah.

**Chris Gammell:** Yeah. Especially I guess sort of the cost factor at a automotive companies, it's pretty insane. Like everything really comes down to, to the last dimes and cents. And in the, in the beginning, it wasn't that much of a focus because I joined back in, I think it was 2000. What was it? 11, 12. And they were still just trying to get the product to market. So it was mainly just about, you know, getting it done, getting it on the road and then we'll, we'll take it from there.

**Starlink:** Right. And then you cost down at some point.

**Chris Gammell:** And then, then you cost down afterwards and can be, can be boring, but it can also be very interesting because it forces you to, you know, think out of box and maybe come up with a completely different solution that only uses half of the parts.

**Starlink:** Yeah. Right.

**Chris Gammell:** And I think a good example is, is the sort of the, the red thread that went through my, my Tesla career. It was the door handle of the Model S. I started working on that.

**Starlink:** Oh, you mean the most famous part of the Model S? Is that right?

**Chris Gammell:** Yeah. Yeah. And Elon still likes to talk about it. So that.

**Starlink:** Everyone likes to talk. I mean, like that is the most, that's like the first thing you notice. Cause like any door. So if you don't know when you walk up to a Tesla Model S and I think, think some of the other ones too, like the door handles pop out. And so like it pops out of the door. So, so it's cool.

**Chris Gammell:** Yeah. It's, it's kind of silly, but, but like you said, it's the first thing you see. And especially now looking back, I think it really is sort of the first interaction people have with the car and it really defines the experience of the, of the user. And now it actually works quite well.

**Starlink:** Yeah. Yeah. I mean, it feels like futurey, you know, like that's kind of like what you'd expect to like a futurey card to do maybe to also like, you know, have little stairs pop out if it, you know, it's obviously it's, you know, but like some kind of like automation, kind of weird robot-y kind of stuff that happens. Yeah.

**Chris Gammell:** But, and now a lot of other brands have, have followed suit. So I guess it's not that crazy of an idea after all.

**Starlink:** Well, I mean, it just makes the market for it. Right. I mean, that's just how it goes.

**Chris Gammell:** Yeah. But so this is the project that I started working on as an intern back in the days and it was a little janky. It kind of worked, got the job done. Yeah. And I was just kind of blown away that, that my pet project went into actual production. Yeah. Which was, which was a bit of a surprise, but of course then as it, you know, start going to volumes and into customers hand, there were obviously some problems with it. And then we had to go back and do two major iterations on it.

**Starlink:** One of the things that always amazes me about like, when I like look, start to actually, you know, like I feel like you get in a car and everything's just kind of there and just kind of seamless to the, to the user. Right. It's just like, oh, it's just this thing. It's just really, it's more like a feature level. Yeah. It just works. But, but really it's just like, it's like, oh, it's just this function that I have in the car. Right. So like door handles or, you know, like the mirrors that move, you know, the little controller in the car I have that like moves the mirrors to adjust them, that kind of thing. And it's like, but no, there's like engineers, like multiple engineers and production people. And like, like you said, it's like someone's project at some point to just make that thing work every single time. And it, and it's all throughout the car. It's crazy.

**Chris Gammell:** Yeah. It's, it's really crazy. Like, I mean, and this, this door handle has a freaking bootloader and it's a microcontroller. It's, it's pretty, pretty insane.

**Starlink:** Right. Right. And so like, and does each one operate independently of one another?

**Chris Gammell:** Yeah. They're, they're basically self-contained systems that also have a, like a digital interface. In this case, it's a Lin, which is kind of a cheap version of CAN for like smaller sub networks.

**Starlink:** I forget someone was on the show talking about that. Maybe, maybe Earl, um, from Makana, but it was, but at some point I learned about CAN versus Lin and like, it seems like kind of like the less critical systems are on Lin. Is that a good approximation?

**Chris Gammell:** Uh, yeah, it's, so it's mostly cheaper because you can, can run it on a UR peripheral of any microcontroller and only uses one wire, which is half the cost of two wires. That's right.

**Starlink:** Right. Cause yeah, the harnesses in cars are insane.

**Chris Gammell:** Yeah.

**Starlink:** It's really insane.

**Chris Gammell:** But so actually I've, I've really have come to like Lin bus. Most people hate it because they come from a CAN background and it's a little different. So they usually just don't really get it. But for, for its specific niche, it's, it's a pretty nice solution.

**Starlink:** What, what about it? Like just because it's simpler or because it's.

**Chris Gammell:** Yeah. It's just, it's just a lot simpler. It's, it's a single master bus. So usually you have like one big body controller that just talks to a bunch of dumb sensors or actuators and yeah, it's, it just gets the job done.

**Starlink:** Do you still, do you still have like transceivers on the bus to actually like have isolation and things like that? Like CAN usually does?

**Chris Gammell:** Uh, yes. There still is a transceiver, but it runs at 12 volt, uh, voltage level or logic level. Uh, so it's essentially just a open drain on both sides with, uh, some pull-up resistors.

**Starlink:** Oh, okay. Yeah. So like, like using optos or using actual, like.

**Chris Gammell:** No, it's, it's literally just a open, open drain fat. That's.

**Starlink:** Oh, okay.

**Chris Gammell:** Driving it down to zero.

**Starlink:** It's just 12 volt tolerant at that point. Right. Yeah.

**Chris Gammell:** Yeah.

**Starlink:** Huh. That's interesting. Yeah. I guess that would definitely. I, maybe I'm wrong about the, the CAN stuff then. I thought CAN was sometime, is it sometimes isolated or is it, or there are specific drivers?

**Chris Gammell:** Yeah. You have different, different, uh, FIs. So you can get a opto isolated, uh, yeah. Driver chip that isolates your microcontroller from the bus. Mm-hmm.

**Starlink:** Yeah. You know, I guess I've been doing some RS-485 stuff lately too. And like, that's got transceivers as well. Kind of in the same vein, you can get isolated, not isolate, whatever. But I guess you're right. Some of it is just, the drivers are just to boost the current and be able to drive to, you know, all the capacitance on the line or, or whatever like that.

**Chris Gammell:** Yeah. And they have some logic in, in them as well. Usually like to, for example, make sure that if your microcontroller gets stuck, that it doesn't allow you to drive the line dominant for long periods of time. So there's, there's a little bit of logic in there.

**Starlink:** Yeah. So like a timer. Yeah. Something like that.

**Chris Gammell:** And it, uh, it usually has all your, your protection in there as well. So usually they're pretty tolerant to, uh, common mode offsets and other kinds of pesky things so that your microcontroller pins don't have to deal with that.

**Starlink:** Yeah. What about, so, okay. So now you're making a thing that lives on a Lin bus, maybe talking to like a, some Lin master somewhere, but like when you're at a big company dealing with multiple revisions of a car or whatever like that, like, how do you actually, how do they, how do they communicate to you that like, is it like handed down to you? Like you're, you're going to be on this wire in this harness talking to this master. Like how, how does that stuff actually work at a, at a organizational level inside a car company?

**Chris Gammell:** Yeah. I think, I think that also changed a bit through the lifetime of Tesla in the beginning was very ad hoc and in the end patch everything together.

**Starlink:** Kid run your own wire. Yeah.

**Chris Gammell:** But I guess, I guess one, one advantage of, of all these buses is that it's all software controlled. So as long as you're on, on can or on Lin, you can kind of deal with the interfacing at a later stage. For example, like when I, when I was working on the door handle, I just added hooked up to a USB Lin dongle and send commands from my, from my laptop and read back status. And when that is working, then you hand that off to the person that is doing the software of the body controller. That's communicating to it.

**Starlink:** That's cool.

**Chris Gammell:** And of course you usually want to talk to those people throughout the project and not, not drop it on the desk two weeks before launch.

**Starlink:** By the way, I changed the address over cool. You know, it's, there's all these different modes now.

**Chris Gammell:** Yeah. No. So there's, there's always a bit of a back and forth and there's always, of course, when you get to it, there's always lots of funny details that make things more complicated than it now sounds, but that's the advantage of, of having it so much firmware defined because it's much easier to, right. To change throughout the process.

**Starlink:** Yeah. I guess you have to have, I mean, you said there's a bootloader, but I guess you'd also have to be able to like get into bootloader mode, be updated over the bus, that kind of thing. Yeah.

**Chris Gammell:** Yeah. Yeah. Bootloaders is something bootloaders need to be rock solid, but of course the advantage there is that you can share a lot of that. So at some point you just build up a bunch of bootloader libraries and sometimes you have to adapt it to a certain platform, but the majority of it, and especially sort of the high level bootloader protocol is, is shared throughout all the components.

**Starlink:** Hmm. It's kind of crazy too, thinking like, so I know that like Tesla can, they have like modems and so they can get like updates overnight and stuff like that. But at some point that would mean that like, so if yours was changing the, the nature, you know, the drive speed of how fast the door handle pops out that like your firmware would be getting distributed over cellular to a car, which then gets pushed down through the various levels of hierarchy. It's just like, it just seems like so much work to get something updated, but also it's really cool that it does.

**Chris Gammell:** Yeah. It's, it's, it's really mind boggling the amount of over there they can do that. Every little mic controller in that car can get, get updated over the air and they very routinely are.

**Starlink:** Oh really? Okay. So like, and so then you also have to track that there, you know, it's version 2.37 instead of 2.35 or whatever it is, right?

**Chris Gammell:** Yeah. Versioning is a, can be, can be challenging, but usually, yeah, I don't know how much it should speak to it, but they treat the whole car. Like every, every mic controller software version as sort of a package. Yeah. So they bundle everything up into a package and everything is always at sort of one platform version.

**Starlink:** Oh, I see. Okay. I got it. Got it. So like you might get into a release for the next, so the car doesn't do it piecewise, like handles are different than the, the, you know, the brakes or something like that, but it would just be like everything gets updated at once.

**Chris Gammell:** Yeah. You would never update a single module. You release a new vehicle package and then maybe just one, one image changed between the previous version, but you still deploy it as a, as a whole. Yeah. Vehicle package.

**Starlink:** That makes sense too. Cause then, yeah, you could do the air, like you mentioned on the satellite too, like you could do the CRC, you could do the checking to make sure the image is really well packaged and, and instead of like doing it. You know, one at a time. Yeah. That makes a lot more sense actually. Yeah.

**Chris Gammell:** Yeah. So it's this super complicated giant beast of a system, but the nice thing about it is that once you have it, it becomes really easy. If you add a new module to your system, you can just sort of plug into all this infrastructure.

**Starlink:** Yeah. Yeah. So like actually like troubleshooting and testing and that kind of stuff.

**Chris Gammell:** Yeah. And just the whole deployment scheme of, you know, just implement this bootloader protocol and then the whole built CI infrastructure and getting it packaged into a vehicle firmware package and sent to the car and then to your device that, that, and then the version checks, all that is sort of comes for free after you've done it. Yeah. Yeah. Yeah. Every software engineer is like, no, it doesn't. How dare you, sir? No, but just in terms of like adding, adding one module to this existing infrastructure. Right. That's, that's, I kind of feel bad for, for all the other car manufacturers that have to do it the other way around.

**Starlink:** Yeah. What is, what is the opposite? Like, is it, you'd have to pull the thing out and put a programmer into it and.

**Chris Gammell:** Well, no, just in terms of sort of getting, getting to this OTA end game where, where you want to be able to do this, they, they kind of have to, well, I don't know, but my feeling is that they do more a bottom-up approach to, to get to the same result, but where Tesla started doing this from, from day one and their whole architecture is built on it.

**Starlink:** Got it. Okay. So you're saying because of the legacy nature of, you know, you might have an ABS controller that's from 30 years ago. Well, that's not true. 10 years ago that, you know, and then you're trying to integrate it with some fancy new feature. They, you have to try and make them work at a higher level because they're all independent on like a GM car or something like that.

**Chris Gammell:** Well, even if, even if you have a new ABS module, then you have to go through all these layers up and all of them need to support this, this firmware update mechanism in order to, to get to that last module on the chain.

**Starlink:** Yeah. Yeah. I guess, I mean, yeah, that is, that is the benefit of like a vertical integration in the first place, I suppose, you know?

**Chris Gammell:** Yeah. Yeah. It's kind of weird how that's all coming back. Right.

**Starlink:** Yeah. Yeah. I think, I think some of it, I mean, some of it is complexity and like, I feel when I think about vertical integration, like an Apple product or a Tesla product or anything out there that's like, you know, these kind of walled garden vertical integration, it's because they're very focused on like user experience. It feels like, and for like in the user experience space, it feels so necessary to have that. Maybe it won't always be like that, but it feels at this point in history that it is really necessary to have that level of fine control. You know, there's a lot of downside to doing it, of course, but to, to get that fine control, you really need to own everything, you know?

**Chris Gammell:** Well, but if you look at SpaceX, they don't really care about their user experience. So there must be something else that's also driving this vertical integration, right? Sure.

**Starlink:** Yeah.

**Chris Gammell:** Is it, do you think it's just maybe technology moving so fast that you kind of have no choice if you want to keep up?

**Starlink:** I would say user experience might actually be genericized out to SpaceX though too, right? The user experience is, their user is the US government and the US government wants cheaper rockets. And so the user experience, a good user experience is being able to reload, you know, to be reused rockets. And so like from that perspective, I think that it is still user experience and, you know, however you want to define it, you know, user experience kind of gets interwoven with like UI and, and, you know, kind of flashiness like Apple and Tesla, like I mentioned, but like.

**Chris Gammell:** It could also be B2B user experience.

**Starlink:** Sure. Yeah, exactly. Yeah. I mean, I don't know. It's, I don't know otherwise why there's more focus on vertical integration. And I feel like there's always, I don't know, you've been, you've, you've worked in it. Like, what's it like working in a super vertically integrated company like that?

**Chris Gammell:** Well, I don't, I don't know for sure, but based on what I've seen, I think it has to do with technology moving so fast that by the time, you know, you finish your spec for your third party to, to build your, your sub module that by the time it's done and tested, technology has already moved on.

**Starlink:** Yeah. It is kind of shortcutting that, right? It's like basically saying, well, we're not going to get consensus from everyone, even our vendors. We're just going to do it. And there's still, there's still got to be some kind of consensus, right? At some point, at some point, someone said, well, we're going to have this style for our bootloader. Like you mentioned, there's consensus there, but it's not as widely distributed. It feels like.

**Chris Gammell:** Yeah. And it's just, you always like, when you're sort of going in between companies, you're always dealing with this business overhead, like, oh, we need to make a quote for that and we need to review it. And then like, it's just, I remember some crazy stories about like changing the idea of a can message with some like insane lead times and costs associated to it. And if it's in-house, you can literally park up to someone's desk and say, hey, can you change this byte for me? Okay, sure. Right. Make a pull request and it's done the next day.

**Starlink:** Yeah. Yeah. That's a great example. That's a great example. And it's just like the amount of hassle that's there goes down. You know, I guess maybe it's more of the kind of move fast ethos, but there are a lot of downsides too, of course, right? You know, like, like you mentioned, you know, getting a roadworthy car out on the road, it took longer than they thought it would, right? That's just getting bootstrapped up to a first vehicle is really tough. It feels like.

**Chris Gammell:** Yeah. And I think another big downside is that you're much more at risk for if your specific industry goes down, then you have all this manufacturing capacity sitting idle and whether the opposite, if you just make a module, it goes to maybe parts in a bunch of different industries, then you're less susceptible to ups and downs in individual markets.

**Starlink:** Yeah. Yeah. And I think, I think by, again, with necessities, I think it's like, there's like a scale level that's just necessary as well. Like, you know, so at hyper, you know, you might want to go build the rocket, right? You might want to build every element. You might want to go build the caps that are the best caps for a, you know, to put into a satellite, but it's like, well, it's just not realistic to do that. Right. Given the marketplace with like high level technology type things that, you know, the target that SpaceX and Tesla and Apple all targets, like, you know, there's enough volume or there's enough desire. There's enough money at the back end, which is what you really need to get scale. If you can't get that money, then yeah, you're not going to, that vertical integration doesn't happen with small companies. Yeah. Or if it does, they. Yeah.

**Chris Gammell:** I'm actually waiting for the day that Apple starts making their own capacitors.

**Starlink:** I mean, yeah. I mean, I think as soon as it becomes realistic that probably the first time they can't get the caps they need, they probably will. They'll probably just go buy some company and take them over. You know, like that's.

**Chris Gammell:** Yeah. I remember, when was it like, like a year or three or four ago that there was this crazy market shortage of. Oh yeah. Yeah. Of ceramic caps. And I think part of that is because like all the production lines changed to like 0201 and smaller because that's what, what Apple and co wanted.

**Starlink:** Yeah. And just got to deal with it.

**Chris Gammell:** Yep. Yeah. I mean, Apple must be at a scale where, well, I don't know. I'm not an expert in capacitor manufacturing. Maybe it's not as fun as it sounds.

**Starlink:** It does not sound fun. Although the testing is really cool. I mean, like when you think about like, oh yeah, every cap gets tested. Like that's, that's insane. You know, that is really insane. Yeah. Uh, speaking of testing, uh, you are interested in standardizing and testing and stuff like that. And you're thinking about a new test format. What, what's going on with that thing?

**Chris Gammell:** Yeah. I'm, I guess maybe as, as many other engineers are, I have a little bit of OCD going around. What?

**Starlink:** No.

**Chris Gammell:** No. Okay. All right. That's probably just me.

**Starlink:** No. Yeah. Yeah.

**Chris Gammell:** I think, you know, in order to, if you want to do testing, right, you need to have a reliable test setup. And if you have like a big bowl of spaghetti on your desk, that if you bump it, you know, the results change, then it's very hard to, uh, get anything done. So I've been thinking about actually throughout my career, if I look back, I've always been trying to find out ways to make things neater and compact and letting me take my test setup on the bus so I can work on it on the way home, like that kind of stuff. And, and it's, it's always a fine balance between like putting so much effort in it that, you know, it just makes the whole operation worthless or like not putting enough effort in it and then dealing with the results of not being able to test properly. So I've been, I've been looking at a lot of different form factors. And right now I'm thinking about making some kind of like generic Eurocard subrack where you can slide either off the shelf or custom modules in and then don't have to deal with so many wires. So we'll see where that goes.

**Starlink:** And so this would be like for the actual board itself or for like a piece of test equipment that would then test a board?

**Chris Gammell:** Well, so we usually have a lot of setups where we have like a bunch of off the shelf EVA kits and our own boards that are, that have some USB adapters and have just a bunch of bits and pieces that are spread out over one or more desks. And I'm trying to get to a form factor where you can standardize that a little bit and just slide cards in where you can either, you know, make custom cards or have some, have some generic cards where you can mount your, your board on to just make this test setup a bit neater and reproducible. And also with this whole COVID times more remotely accessible.

**Starlink:** Right. Yeah. Yeah. That, that's a big one. I think is, you know, I ship, I ship boards to clients and, you know, I'm like, oh, well just like probe here and here and here. And it's like, if I could ship them a, a card cage that had, you know, the standard setup in there and then I could ship them a board and then it's like, they're like, oh, it's not working. I could say, well, just plug it into the test setup. And it's, it's kind of a known at that point.

**Chris Gammell:** Yeah. Or you could say like, Hey, connect this to port B instead of, can you look on the desk where the USB hub is and see which parts are available. And so that way, I think, I think it's, it's very useful. Like we also noticed that, you know, with our satellite, everything's on can. So we just made a little recipe, Raspberry Pi hat. It had some, uh, controllable power supplies and a can interface. And my firmware colleague was also working remote a lot. And you would just ask me, Hey, is it, is it plugged in? And then from there you could do everything remotely. And that, that really has, has saved us the last year.

**Starlink:** Yeah. Yeah. That's yeah. I think that's a, that's a great point. So what is the custom piece? So like if you're making a custom card, would it be like your custom card would maybe be like a carrier for your actual product production board? Is that kind of the thought?

**Chris Gammell:** Yeah, it could be. It could, it could just be like a physical carrier and it just provides power and maybe USB or ethernet. Uh, maybe you could put a little FTDI on it. If you want to wiggle some pins or send some, some UR commands, or it could even be like a full-fledged Pogo pin breakout. And then the slot next to it could have a, you know, logic analyzer or, or a JTAG dongle.

**Starlink:** Ah, I see. Okay. And so then some of the signals that it might be sending to a backplane would be like signals that you might want to probe with a logic analyzer. You could send those to a generic sized backplane. Is that kind of the idea?

**Chris Gammell:** Yeah. I don't know. So right now it's, it's just basically a USB hub and an ethernet switch. So it's, it's very generic and that the idea is that, that you can then work from there and, and, and make mix and match off the shelf modules with, with custom cards.

**Starlink:** Hmm.

**Chris Gammell:** That's great.

**Starlink:** Yeah.

**Chris Gammell:** And there's actually a bunch of similar projects out there. I can send you a couple of links. I think one there's, it's called easy five. I think it's coming from, uh, from Saren, the particle accelerator where they really focus on making more affordable measuring equipment. And so not, not so much testing actual hardware. And there's a couple of other ones. Some, some people have made like raspberry pie farms with FM receivers to then stream those over ether, over internet. But there's, I think, and, and also there's of course like the, the NI Pixie chassis that use a similar phone. Yeah.

**Starlink:** That's what I was thinking about. Cause actually a bunch of my former coworkers went to go work at NI and the Pixie is interesting. It's like, it's, it's really, it's for some of the stuff they try and do it with it. They really push the limits of like the power envelope of like what they can fit into like a chassis like that.

**Chris Gammell:** Yeah. It's pretty crazy. Yeah. It's really nice. So actually I think the best way to describe this is I guess a poor man's Pixie chassis.

**Starlink:** Okay. Yeah. That's a, that's a great, I think visualization. Yeah. Yeah. So it might have, it might have a, a port on the end that could, you could put an SMA out and actually, you know, get data in that sort of thing or whatever.

**Chris Gammell:** Yeah. Yeah. So I think they, they do everything on, on PCI express. Is that correct?

**Starlink:** I'm not sure actually.

**Chris Gammell:** I think, I don't know. It's, it's all very high end. So it's, it's very, also if you want to make something custom for it, it's, it's a, it's a big project. And the idea with this is that you can basically take your, your nuclear dev board or whatever screw it on there and then just connect the USB port. And then you, it's part of the system.

**Starlink:** Got it. Yeah. Yeah. I guess that, that is the piece that I was kind of confused about too. Cause when I think about Pixie, right. I think about like, so, you know, you had these cards that slide into a, I'm trying to picture paint a word picture here. You have like a PCB that slides vertically into a slot. It plugs into a backplane, but then usually there's a face plate on the front of it. And like, so there might be like a, if it's like a DMM Pixie, it's actually got the black and red banana plugs in there. And then that would usually plug into something external off of the actual chassis. But you're saying now that you might have it just kind of loop around and go to the next board over and plug into the, the board that actually has the thing you're testing, the dot, the thing you're testing on it.

**Chris Gammell:** Yeah. I have no idea yet if this makes sense or not, but it seemed like a way to make things more portable and neat, I guess. Yeah. I think it would look cool too. I mean, like, honestly, yeah, that's important.

**Speaker ?:** Yeah.

**Chris Gammell:** And so like you can, you can imagine if you, if you're, you know, developing some kind of, uh, you know, like a firmware stack or like you, you have some software product that you want that you need to test on like 80 different targets. And this could also be a way to say, so you want to test it on the whole nuclear family, then you can just make it a generic. Nuclear carrier with the mounting holes in the right spot. And then you can like make a rack of your, your 80 different nucleos and do your CI testing in it.

**Starlink:** Yeah. That's a, that's a good example, I think. So you'd have maybe like a, so like in the nuclear example, right? The board would be like flipped over, plugged into a bunch of receiving headers that match what the, I guess it doesn't even have to be flipped over because of how the nucleo is, right? It has the bottom pins. So it's plugged in, it maybe has a tiny USB stub that plugs into the USB on the nucleo. And then it's all on a rack or on this card that gets plugged into a rack. And then all of the pins and all of the USB is exposed on that backplane that then could be switched to using some kind of switch matrix.

**Chris Gammell:** Well, it's an ethernet switch or USB switch. So then you just hook it up to your Raspberry Pi that runs the whole setup or straight to the corporate network so you can control it externally.

**Starlink:** But would there be the, would the IO be broken out too though? Is that kind of the thought?

**Chris Gammell:** Right now I have, I have no IO. So if you need IO, you just need to put an FTDI chip on it or some other interface thingy.

**Starlink:** Yeah. Okay. So then USB really does become that generic, genericized interface there and you just talk to each thing you need to and it's, yeah, good to go.

**Chris Gammell:** Yeah. So you could also think about like, if you want to simulate bigger BLE or lower networks, then you can just make, make maybe a card with, with four BLE micros on there and then, you know, simulate your whole network.

**Starlink:** Yeah. Yeah. That's cool. That's really cool. And then the form factor is like some, is this, is this your frustration on the, the, this is actually metric.

**Chris Gammell:** Well, actually it's really funny. It's a combination of Imperial and metric dimensions. Why? So for example, yeah, I don't know. Well, there's the, you know, the, the use and the HP units. So there's, so the board outline is metric. The, the mounting holes are kind of on funny locations. I usually round them down to metric, but like it goes into a 19 inch rack. So that is all got it. Yeah.

**Starlink:** Not getting, not getting away from that. Yep. Yep. Yeah. I, I've been, uh, I've been cursing Imperial lately. I was dealing with some, some like, uh, standoff heights and things like that. And it was just, you know, like some funky and I'm like, oh, it's, this is some fractional Imperial thing that then got converted to millimeters. But then the connectors that stacked up to the same height as the standoffs, it just, it didn't line up. It's like, what are we even doing here? Yeah.

**Chris Gammell:** Yeah. Come on, get yourself together. USA.

**Starlink:** I know. Yep. Yep.

**Chris Gammell:** Maybe, maybe that's something for the, for the net to put in the next, uh, don't you guys, with your elections also vote on some random things?

**Starlink:** Yeah. Maybe this could be, yeah. Yeah. I got blocked at some point. I think in the seventies it got blocked. Really? Maybe it's time.

**Chris Gammell:** Maybe it's time, Chris.

**Starlink:** I wish, I wish. I wonder about, yeah, no. We don't need to dive into politics. We don't need to dive into politics.

**Chris Gammell:** No, no. I was just not talking about politics. I was just talking about metrics.

**Starlink:** Metric. Yeah. Do you think we'll ever get away from it?

**Speaker ?:** I think that's the thing.

**Starlink:** It would become politics. It would become politics. True. Yeah.

**Chris Gammell:** Do you think a hundred years from now, will we have Imperial still?

**Starlink:** I don't know. I don't know. We still have a lot of things that are like, there's a lot of units that are out there. I've been doing some pressure stuff too. And like, let me tell you, pressure is a, is a unit. They have some units that are just so dumb. Yeah. Bar and ATM. ATM's good, but like, you know, PSI. Oh, good Lord. Good Lord.

**Chris Gammell:** Okay. So we're probably stuck to it.

**Starlink:** Yeah. I think it's, I think it's just, yeah, it's, it's a carrying cost for now. You know, BTUs, British thermal units.

**Chris Gammell:** Do you think there's like talking groups so we can sort of work on accepting it?

**Starlink:** Yeah. Right. Like a therapy. Yeah. Group therapy. I think this, this amounts to group therapy right here. You know?

**Chris Gammell:** Yeah.

**Starlink:** Maybe. There's people nodding their heads out there. There's some people also raging at their podcast listener right now. Like, Oh, I love my Imperial units. It was like, okay. Oh yeah. Sorry. Well, yeah. I mean, but that's the thing, but then you get PCB designers like, you know, well, I'm never giving up mills. Yeah.

**Chris Gammell:** Like PCBs are also this, this weird, weird hybrid world where. Yeah.

**Starlink:** Yeah.

**Chris Gammell:** Like even if you're like, we make our, at least I tried to make sure all our boards are in sort of rounded metrics and in the outline, but then there's still people talking about mills and trace. Yep.

**Starlink:** Yep. Specs. I think, I think the thing that'll actually drive it more is like, so if, if like the board houses, at least if the China board houses or the European board houses were like, yeah, we're just doing metrics from now on. Sorry. You just got to deal with it. Then I think that would actually drive the industry more than we'd expect. There would still be people that are like, wait, what's going on here? And they would do the conversion.

**Chris Gammell:** Yeah. Because you go on the website and you see like, oh, this is your track spacing and width. And that's what you type in your cat tool. So that's, I think, yeah, you're probably right. So maybe that's where we need to start, Chris.

**Starlink:** Yeah. Well, and I think the connectors are honestly doing it too. It'd be, well, cause like the China, like all the connectors are made in China effectively. Not all of them, obviously, but a lot of them are. And it's like, it's hard. I am actually honestly shocked when I open a data sheet these days and a dimension is in not metric. Like a connector dimension. It just, it feels weird.

**Chris Gammell:** What also keeps blowing my mind is like how all these also package drawings always have the dimensions you really don't care about. Yes. It's just insane. You always have to like add four up and then to take an average to get this center point. It's just. Yep. Yep. Just give me the numbers that I can type in without having to open up Excel to convert everything to, to the center point.

**Starlink:** There was a tool at one point that like allowed you to like actually like click like the outline of the, of the connector and it would like approximate measurement and stuff like that. And so if it was drawn to scale, it would be fine. It would like give you like.

**Chris Gammell:** Like from your PDF, you mean?

**Starlink:** Yeah. Yeah.

**Chris Gammell:** Oh, cool.

**Starlink:** Yeah. It didn't make it, but it was, it was a great demo. It was too complex. Yeah.

**Chris Gammell:** There was not enough AI evolved. Maybe now.

**Starlink:** Yeah, exactly. Exactly. Throw some AI at it. Well, you know, they should have been vertically integrated, but they didn't, you know, they couldn't raise enough money. So. Yeah, I guess. Well, yours, thanks for talking about all this stuff. And yeah, it's really exciting. You're doing some exciting things. So I'm excited to hear about the platform and the measurement stuff and where, what else you're launching into space in the future. I think that'll be really cool.

**Chris Gammell:** Yeah. It's just, I guess, look out your windows at night. From January. There's actually a website where you can sort of see all satellites. So if you type over in there, you'll know when we fly over.

**Starlink:** Oh, what's the website called?

**Chris Gammell:** What was it called? I'll send you a link. I think it's a space book or something. It has a pretty cool visualization. This also shows you junk.

**Starlink:** Oh yeah. That's great. Yeah.

**Chris Gammell:** It's kind of scary in a way.

**Starlink:** Where can people find you online?

**Chris Gammell:** I'm a more of a consumer than a producer. So I'm not on the Twitters or the Facebooks. I guess they can contact you if they want to reach out to me. Yeah. Or do I need to pay extra for that service?

**Starlink:** Yeah. You got to pay extra for that service. Okay. Yeah.

**Chris Gammell:** I'll think of something.

**Starlink:** Maybe you could start a Amp Hour review group or something like that. You can send out a group text instead of just texting me.

**Chris Gammell:** Oh yeah. Or maybe I'll start my own social network. There you go.

**Starlink:** There it is. Yeah.

**Chris Gammell:** Vertical integration.

**Starlink:** Concerned Amp Hour citizens.

**Chris Gammell:** Yeah.

**Starlink:** All right. Great. Well, thanks for being on the show, Yorish. We appreciate it. That was a pleasure. Cheers. I called Yorish the voice of the audience, but the real voice of the audience is our weekly sponsor, our patrons. Join the club today at patreon.com slash the Amp Hour. A special thanks to our corporate sponsor, Bino, who will now offer the PC Byte. The first time I heard about that solution was from Yorish.

**Speaker ?:** We'll see you next time.
