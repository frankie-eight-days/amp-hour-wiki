---
episode: 567
title: The Rodeo Drive of Electronics
url: https://theamphour.com/567-the-rodeo-drive-of-electronics/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released November 21st, 2021. Episode 567. The Rodeo Drive of Electronics.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. One hour late. Well, one hour early. Early. You got totally confused by time zones that didn't change. Time is a circle. Now, come on. You can't blame it on the time zones this time because it hasn't changed, has it? I don't even know.

**Chris Gammell:** It doesn't even matter anymore. Do you ever see that, though? I think it was True Detective where it's like Matthew McConaughey. He goes crazy. He's just like, he loses his mind. He just keeps going, man, time is a circle. Time's a circle. Sorry.

**Dave Jones:** Sounds too American for me.

**Chris Gammell:** No, it's really good. It's really good. All right. Very good thriller. Classic.

**Dave Jones:** Okay.

**Chris Gammell:** Let's talk jelly beans. I saw you've been making some jelly bean videos.

**Dave Jones:** More jelly bean components. I kind of enjoy this jelly bean series. I've only done two so far. But I could probably do a dozen of these videos with top five jelly bean parts in every category.

**Chris Gammell:** Skip resistors. Skip resistors. Yeah, right.

**Dave Jones:** Top five resistors are.

**Chris Gammell:** Yeah. And the award goes to.

**Dave Jones:** I mean, you could just do it on every. I mean, how many categories of chips are there? I guess you could just go through the DigiKey category list of parts and you could go, well, top five. There's probably about a hundred different categories or something.

**Chris Gammell:** I think the real problem is that everything's changing right now. It's like, oh yeah, that was the top five this week. You can't get those anymore.

**Dave Jones:** But that's the definition, right? If you can't get it anymore, it no longer becomes jelly bean.

**Chris Gammell:** Yeah, I guess so. So what's your criteria? Having multiple of the same SKU or the same partner?

**Dave Jones:** Well, the criteria is it's generally old, right? So that means it's been around for a long. And if it's old, that's when it gets copied by multiple manufacturers. If it's only a couple of year old chip, it likely hasn't been copied yet, right?

**Chris Gammell:** Yeah, that's a good question. Have you seen anything that's been released in the past 20 years that has been copied in terms of part numbers? Like true copy number, right? So there's 14 people that make an LM317, right? You're right.

**Dave Jones:** Off the top of my head, no. But I'm sure there is. Leave it in the comments. Do they start litigating around? Yeah, I know.

**Chris Gammell:** Do they start litigating maybe? I don't know.

**Dave Jones:** I know. Leave it in the comments, please. Now, somebody actually brought this up in the previous video. They said, how can these companies just copy like the LM317 or the LM324 or something, right? How can somebody just copy it? And I actually don't know the reason behind it. But somebody had a good reply saying, oh, this actually stems back to the early days of semiconductors, you know, like 1970s where most of these jelly bean parts come from in the early 80s, where there were these government requirements for the military that they had to have multiple sourced parts. So it's like, oh, okay, you know, TI have a patent on this, you know, new op-ep, but sorry, guys. The government wags their finger and says, uh-uh, you've got to let everyone else make it because the military need it. So therefore, you know, so I wonder if, please, if anyone knows, is that still a thing or is that the actual reason?

**Chris Gammell:** On the sourcing side, there almost definitely is. I think there's like, so my buddy's in sourcing for government level stuff and not like the super high end, not the super like crazy stuff like, you know, NSA level, but like, you know, government contract, that sort of thing. And like, they have some very interesting stringent requirements, which I'm sure I'm going to get wrong. I'll caveat my answer here. But I know one, because I hear him complain about it, is that the board houses and the assembly have to be in the US, right? And that sort of makes sense. But the problem is, right, something like we talked about a couple of weeks ago is that they just keep buying each other, right? And so for a long time, it wasn't that big a deal where it was this, you know.

**Dave Jones:** Exactly. You had your TI, your national, and your analog devices.

**Speaker ?:** Oh, no, no, no.

**Chris Gammell:** I actually mean on the board house even. Oh, the board house. Oh, right. Right? So for a long time, they were pop shops, and it didn't matter that much that it was like really large geometry stuff. So it wasn't super stringent. You know, they had a quality control that they had to go through, whatever. But then as things have gotten more and more complex, including what the designers at these contractors do, it's like, oh, well, now that starts to get narrowed down, and there's more consolidation. And then there's fewer and fewer board houses that can do this sort of thing. And then there's more and more, you know, they're going to layer on top of that all of the shortages and all the requirements. And it's like, oh, my God. Like, they're down to, like, three houses. They mandatorily have to get, like, two or three bids for every job. Yeah, yeah. And so now they keep bidding the same stuff to the same people. And so basically competition's out the window then as well, right? So you have, like, all of these layering compounding effects, and it's just, my friend is a very angry person.

**Dave Jones:** I've got experience in this field. I used to work for military companies, right? That was my burden bar.

**Chris Gammell:** So when you did it, was that also, that was in-country requirements?

**Dave Jones:** Sometimes. It depends on what you work with. And this is why, from the PCB side of things, for example, this is why, yes, this is why the, up until fairly recently, there was only one PCB manufacturer left in this entire country. Yeah. Like, bareboard manufacturer. They're called Lintek, L-I-N-T-E-K. And they were the only manufacturer in all of Australia, right, for bareboard PCBs. The only reason they still existed is because of the government contracts.

**Chris Gammell:** Yep.

**Dave Jones:** Right? And they make high-end boards. Don't bother going to them with your little, you know, four-layer tin pot, you know, Arduino hat or whatever. You know, it's just not going to happen. Well, you can if you have $10,000. Well, you can if you want to pay the money. Yeah, yeah, yeah. Exactly. Oh, no, they'll turn it overnight for you, you know. Well, yeah, yeah, yeah. Right? But, yeah, so they do all the, like, exotic manufacturing processes and everything like that. And, yes, we would often use those for the military staff. It depends on what it was. If it was just, like, if it was designed to go into the actual military product, then, yes, it had to come from them, right? But if it was just, like, a production test jig or something like that, it, like, meh. Like, I can just use anyone I want, right? It didn't really matter. But if it went into the actual military product, yes, we had certified suppliers. And you'd go out to their site and certify them as well. Ah, yes. Any, any, any, certain, like, often I've gone out to a, you know, some, some new supplier and we, and we had to certify them. You know, they had to make molds or they had to, you know, make something or other, right? And wire cables and things like that. You'd have to go out and certify them. And, God, the paperwork involved in that was just insane. But, yeah, that's the only reason the, that own, the board manufacturer, that was the only board manufacturer left in the country because of the government.

**Chris Gammell:** Right, right. Contracts. I've heard that that actually folds back on itself too, right? So, now, like, you think about, like, this over time. So, you have someone like Lintec and they're, they are the only, the only option and they, you know, have kind of a cornered market there and they can raise their prices. And maybe they have higher prices or maybe they have domestic labor requirements.

**Dave Jones:** Oh, sure, I haven't ordered from them for, yeah, a long time.

**Chris Gammell:** Yeah, right. But, but, like, you know, there maybe are just higher costs for operating a smaller operation with specialized labor in a higher cost country. Like, all of those things kind of compound up. But, like, normally what would happen in an industry, right, like, you know, a true market system would be like, okay, you'd have other people entering the market and the cost, cost pressures drive things down or whatever. But because it's like a non-liquid market that it doesn't actually move, right? And so then, so what I've heard about as well is on the machinist side of things in the U.S. Again, this is, anecdote could all be wrong, but I've heard from someone I know who was in the machining industry. They said, you know, you could go and get a mold made for a plastic, an injection molded plastic thing for anything you want, right, at very high quality in the U.S., right? This is U.S. specific for my, for my story. You can go and get a mold made, but it's very, very expensive. And it's like, why hasn't price pressure ever driven that down? And the answer is because it's also still propped up by medical companies that are willing and or have to pay for local stuff or military companies that have to source stuff locally. And so really there is a non-liquid market, so it's not actually pushing the pricing down. Same thing for board houses and whatever, right? There, you know, there are some very realistic costs, right? But if you look at a, you know, long-term type of thing, you'd think automation would drive these sort of things down. It's actually, some of it is military-industrial type stuff that's propping it up because there are these requirements that drive higher cost, sure, but also it's limiting the number of people that enter their market. And yeah, so just econ 101, there is the supply and demand curve is a little skewed. So it's interesting how it works, but it's sucky because if you want to see, you know, if you want to see lower cost stuff in your country, like to just drive more industry, it's like, oh, well, that's going to kind of limit things.

**Dave Jones:** Yep. We do now have one extra PCB manufacturing house here. It was Circuit Labs who were in New Zealand. They now moved to Australia. That was like just before COVID. So I'm not sure if they ever opened or not yet or what's actually happening with that. So COVID would have really screwed around with that. But yeah, that was kind of exciting. You know, it's like we've doubled. We've doubled our number of PCB houses in this country. Look at this growth rate. Yeah, exactly. 100% growth rate a year, you know. Yeah. Yeah. It's just, yep, crazy. Speaking of PCBs, the EuroCircuit factory, which people in Europe,

**Chris Gammell:** I've never used. I hadn't even heard about this until the fire. Right.

**Dave Jones:** No, I hadn't heard about it. But yeah, there was a fire at their Hungarian factory. And yeah, I guess it shut down for a while. So that's nasty. I wonder what type of fire it was. Because they don't have hot, like they have, you know, chemicals and stuff like that. So I don't know. But I don't think they're that flammable. I guess they are technically flammable. But, you know, I don't know. Who knows? It's just some machine that just caught on fire. I don't know. Anyone knows details?

**Chris Gammell:** Yeah. Well, I hope everyone's okay.

**Dave Jones:** Yeah, there's only one person injured, but they're okay, apparently.

**Chris Gammell:** EuroCircuits, I've mentioned on the show before, they have a really, really cool. Actually, it was past guest Yoris who told me about it. They have a really cool DFM system on their site. So you like upload your design. I've heard about it, yeah. Yeah. Probably for me. Right, probably. Via Yoris. Yeah, exactly.

**Dave Jones:** So, yeah. Very cool. All right. We are going to talk about infrastructure, aren't we, Chris? Because you just love your politics, Chris.

**Chris Gammell:** This is a non-political. So this came up on a, this is part of the infrastructure bill, which is a US thing.

**Dave Jones:** It did get the most thumbs up on the Reddit, on the subreddit. Yeah, it did. So we have to talk about.

**Chris Gammell:** It actually was on Planet Money, which is another podcast. You haven't maybe heard about it. You know, it's probably like the top 10 podcasts that download each week. Nope. It's an NPR podcast. Right. But they do like shows about like some Ontario issues.

**Dave Jones:** It's in the name. National Public Radio. National means US. Not IPR.

**Chris Gammell:** It's NPR. Yeah. Yeah. Right. Not APR. Yeah.

**Dave Jones:** There's this, you know, the world's like a globe and America's just like one little tiny part of it. Yeah, it's the center of it, right? Yeah. Right. Center of the universe. It's weird.

**Chris Gammell:** It's like a Taurus, you know, right in the middle. And then it all curves away. It all curves away. Yeah. Obviously, this is US-based infrastructure stuff. But it came up if people were listening to NPR. But by the way, a lot of Australians listen to NPR. Just getting that out there. Okay. NPR is very big in the podcast. Sure, Chris.

**Dave Jones:** Yeah.

**Chris Gammell:** Anyways, they came up and I was just listening. So someone was listening to this and they told me about it. And like in the middle of this random podcast, they're talking about how a tiny airport in Thief River Falls. Yeah. A town of... So I didn't realize the numbers. They said 8,500 people in Thief River Falls, which DigiKey is.

**Dave Jones:** Yeah.

**Chris Gammell:** 4,000 to 4,500 work in DigiKey.

**Dave Jones:** Yes. I know. That's insane. I know. It's crazy. They actually bus people in from other towns. DigiKey have their own bus services that, you know, bus people in.

**Chris Gammell:** That is crazy.

**Dave Jones:** This is one of the reasons why I love DigiKey is because they're still dedicated to this tiny, small town where I think one of the co-founders... We should actually try and get one of the co-founders on the show. That'd be...

**Chris Gammell:** I think it's more than one. I have a request out. I have a request out right now. Oh, okay.

**Dave Jones:** Right. Cool. Yep. I think that'd be great. And yeah. And they're still dedicated to this small town. And of course, it's a cool name. Thief River Falls, right? It's just a great name. Yeah. And it's... Yeah. I just love it. And there's this big airport there that almost like almost all the planes coming in and out are DigiKey like, you know, flights.

**Chris Gammell:** No, not big. No, five people work there. It's small.

**Dave Jones:** Well, yeah. No, but it's like... But it's over capacity. That's the thing. That's why they had to expand it. So they've... Yes. You know. Well, I'm having a look on the map right now and it's kind of... It's like I've...

**Chris Gammell:** It's no bush plane. It's no bush plane airport.

**Dave Jones:** No, I've flown into much smaller airports. Okay, Chris. To me, this is a big airport, right? Well, you know.

**Chris Gammell:** On the far side of the Taurus. Right.

**Dave Jones:** Oh, boy.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, it looks big, you know.

**Chris Gammell:** It's big-ish. I think the real thing is that like, you know, you just think about like the scale of operations and stuff like that to get that much stuff out. You'd want to pretty much put the biggest plane you could, right? In terms of like economies of scale.

**Dave Jones:** Yeah, yeah. Of course. I'm not sure what planes they fly in and out of there. And it's just...

**Chris Gammell:** They're not like... It's not going to be like a 747. You know, like a lot of those are like modified 747s.

**Dave Jones:** Right.

**Chris Gammell:** For like UPS and FedEx and like the other couriers. They all buy old planes and then they just pack them to as much as they can.

**Dave Jones:** Right.

**Chris Gammell:** But I don't think they have those flying.

**Dave Jones:** Well, I can tell you for those playing along at home, the runway is two kilometers long. So the main runway... Actually, see, it's got two runways and taxiways. This is a big airport, okay? It's monstrous. In quote marks, right? Yeah, yeah. It's got a whole two runways.

**Chris Gammell:** Right, right, right.

**Dave Jones:** So don't, you know...

**Chris Gammell:** I feel like if we looked at like the flight tracking out of that, that's how you really tell. You look at the biggest plane coming out of there. Yeah, yeah, right.

**Dave Jones:** Yep. Yeah, flight radar thing, which is fun to watch. Those are fun to watch. Yeah, yeah, yeah.

**Chris Gammell:** You don't watch like the single flight. You got to watch the whole map where all the planes...

**Dave Jones:** The time lapses and stuff. And people do time lapses and things like that. That's right. Yeah, yeah, yeah.

**Chris Gammell:** The big planes going in like the A380s. Yeah. That's a lot of fun.

**Dave Jones:** Yeah, I thought about getting a receiver thing and actually receiving those and feeding data in there. But, you know, like there's already heaps in Sydney. So, you know. Ah, ah. Yep.

**Chris Gammell:** Yeah, they have the same thing for boats as well. Right. There's like a... You can watch like boat traffic and stuff like that. There was actually just a video about global logistics on Wendover as well. About like how shipping...

**Speaker ?:** Oh, yeah.

**Chris Gammell:** I think I saw that. Because it's all like stacked up at the ports here. And a lot of places probably. That was a good one as well. Just like seeing how a shipping container works and all the logistics of that sort of thing. Which, you know, some stuff comes over. I'm sure some of the parts coming over from China are probably on those. But not all, obviously.

**Dave Jones:** Anyway, I love it. Yeah. They just dominate this small town. I mean, it's just like, you know, it's twice the size it would be just because of one company that's there. You know?

**Chris Gammell:** Yep. It's just...

**Dave Jones:** And they're like, I'm actually looking at the warehouse now. And the car park is bigger than the warehouse.

**Chris Gammell:** All right. Wait. Are you looking at the new one? Because they just built a new one too.

**Dave Jones:** Oh, did they? Oh, okay.

**Chris Gammell:** Well, no, I don't. If it's an old map.

**Dave Jones:** Well, imagery 2021. So... I don't know.

**Chris Gammell:** Maybe it's still being built. I'm not sure.

**Dave Jones:** Right. Anyway. I'm not sure what the deal is. Yeah.

**Chris Gammell:** Brooks Avenue.

**Dave Jones:** Anyway, if you have a look at the map there, it's the biggest building in town. So, you know. And there's another one next to it, which is linked as Arctic Cat, which make like jet ski type things. But surely they don't have that entire building as big as DigiCube. But you never know. I don't know. Do they make Arctic Cat things there?

**Chris Gammell:** Oh, that's like a snowmobile.

**Dave Jones:** Snowmobile. Sorry. Snowmobile.

**Chris Gammell:** Snowmobiles. You know what those are, Dave? No, I don't.

**Dave Jones:** I've heard of them. I've seen them in movies.

**Chris Gammell:** Yeah, right. In Inception and stuff like that. Right. Bond movies. They love them in Bond movies. They're exceptionally bad fuel economy.

**Dave Jones:** Yeah. But anyway, yeah, it's very cool. Okay. So, is it nearby? Is it on like the same campus, the building? Or is it... Somewhere else in... What's the same... Oh, yeah, I think so.

**Chris Gammell:** I thought it was... Yeah, let's see layers here.

**Dave Jones:** Is it actually a second building? Or are they moving into just one bigger building?

**Chris Gammell:** It's a second building, yeah.

**Dave Jones:** Okay. All right.

**Chris Gammell:** Yeah.

**Dave Jones:** Cool. Well, there seems to be heaps of land around there.

**Chris Gammell:** I think that's got to be theirs. I think the Arctic Cat's got to be their property too.

**Dave Jones:** Yeah. Maybe. Like, why would that be different? Yeah, I know. It doesn't make sense. The Arctic Cat building's bigger than the DigiKey building. Sorry for those who can't see this, but you can play along at home with your Google Maps.

**Chris Gammell:** I'll link it in down below. Oh, no, it does say Arctic Cat. Oh, that looks like manufacturing, actually.

**Dave Jones:** Okay.

**Chris Gammell:** So if you look on Street View, that does look like manufacturing.

**Dave Jones:** Oh, okay.

**Chris Gammell:** I don't know.

**Dave Jones:** Yeah. There you go.

**Chris Gammell:** It's just a general American town, I guess. Lots of manufacturing and warehousing.

**Dave Jones:** Well, maybe that's 100% of Fee Free of the Forces DigiKey and snowmobiles. You know, that's the line. Yeah.

**Chris Gammell:** Oh, man. I am not missing snow, Dave. Let me tell you. This year has been awesome. Right. It was like 24C here today. Oh, that's right. It's winter over there now, isn't it? Or almost winter. Yeah, that's right. That's right. Yeah. Yeah. Sorry to all my friends up north. I'm not missing that lifestyle. I went for a walk today. It was fantastic. Right.

**Dave Jones:** In the burbs, huh? Walking the burbs. Yep.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Yeah. Yeah. There was a train line going through there, too. I love trains. I'm a big train fanboy. Oh, yeah. I didn't mention that right after we stopped recording last week. Oh, yes. You went on your train trip.

**Chris Gammell:** I mentioned it to you, but I didn't mention it on the show.

**Dave Jones:** How did that go? And what did it take? Like 18 hours or something?

**Chris Gammell:** No. God, no. Oh. That would have been to New York. So from Durham, it's seven hours up to DC. It would have been four and a half driving. Oh, that's right.

**Dave Jones:** So you decided to sit on the train for seven hours. It would be much more relaxing, and you got work done. That's right. Exactly.

**Chris Gammell:** Yeah, I didn't have to pay attention. I could kind of zone out when I needed to. I was doing work. There's Wi-Fi. Yep. There's a place to get coffee in the train. That's all. Right. Pretty much lists all of my requirements for a working space. Right. I mean, I had to wear masks. Or you needed to support a lab. Yeah. Yeah, right. I mean, I had my analog discovery with me. Oh, there you go. That was good. Actually, oh, that was something I meant to mention.

**Dave Jones:** It's surprised somebody, sorry, surprised somebody didn't, like, see that, see you playing with that, and you got your ass hauled off by federal agents at the next thing. Because there was just news. Oh, really? Somebody got, yeah, they were at an airport or something, or they were on a plane, and they had an old school Hasselblad camera. Right? I think it was a Hasselblad. I don't know what that is. Come on. It's the one they used on the moon, dude. Hasselblad is, like, the highest end camera you can get.

**Chris Gammell:** Yeah. Old school film.

**Dave Jones:** You know?

**Chris Gammell:** Okay. Yeah. Right. Anyway. Oh, is that, like, the one where it, like, kind of wrote? I just pulled it up. It's, like, the one where you, like, rotate it on the side, like, to advance the film.

**Dave Jones:** Oh, there's many older ones. But, yeah, yeah, it's one of those older style, you know.

**Chris Gammell:** It's just, like, huge sensor.

**Dave Jones:** Large, big, you know. Yeah. And no, no, no. None of that's sensor rubbish. Film. Right? I'm looking at a new one. It does.

**Chris Gammell:** There is one with a new sensor. Yeah.

**Dave Jones:** They do have sensors. Yes. They use these mega sensors. They actually join sensors.

**Chris Gammell:** $32,000?

**Dave Jones:** Yeah. Starts at that. Oh, yeah. Oh, my God. Yeah. These are the high end. Yes. Hasselblad is.

**Chris Gammell:** So this is out of my pay range.

**Speaker ?:** Right.

**Chris Gammell:** Yes.

**Dave Jones:** Anyway, Hasselblad, the one they used on the Apollo missions, right? It's, you know, one of the world's most respected makers, the best digital cameras on the market, et cetera, et cetera. Okay. Right.

**Chris Gammell:** So someone got arrested for.

**Dave Jones:** Old school film. Somebody. Yeah. They're on the tarmac. They're hopping off the plane. And then all these federal agents came in or something, threw them to the ground. And, you know, you're under guns pointing and blazing everywhere because they thought it was a bomb. Somebody actually reported it. And somebody didn't know what an old school film camera looked like. And they thought he was playing with a bomb. You know, it's like, it's just nuts.

**Chris Gammell:** Oh, boy. Yeah. Oh, boy.

**Dave Jones:** Young whippersnappers anyway.

**Chris Gammell:** Turns out the guy didn't have a bomb. He had a camera.

**Dave Jones:** So he's playing with wires. Oh, this guy on the train, he's like wiring something up with these. It's got a circuit board. You know, it's like, oh, it's going to be a bomb.

**Chris Gammell:** Yeah. I kind of feel like it's, well, first off, on a train, it's like much lower stakes, you know.

**Dave Jones:** Right. Yeah. But still, you know, if somebody reported it, they have to take it seriously. Yeah, I'm sure they would. Yeah. Yeah. Yeah. So, yeah.

**Chris Gammell:** If you see something, say something. Say something.

**Speaker ?:** Right.

**Chris Gammell:** I've always thought it'd be nefarious to have like a little like ESP32 or equivalent and like set the Wi-Fi to something bad, you know.

**Dave Jones:** Ah, yes. Well, my Wi-Fi here, if you want to find the EAV blog lab, it might or might not have NSA surveillance on it. So, you know. Classic. Yeah. So everyone nearby, everyone in the building sort of go, you know, scanning their Wi-Fi going, what? The NSA's tapped into the building, you know. It's like.

**Chris Gammell:** They'd be like, what's the NSA? We don't live in the US. Right, Dave? No. Everyone. What is this? The US is in the center. The US is in the center of everything. Everyone's seen the movies. Come on. Yeah. That's true. That's true. Yeah. So train, it was nice. Yeah. Cool. Didn't get kicked off. That was good. They still have smoke breaks. Smoke what? That was interesting. I mean, I live in the South now. So like, you know, maybe more people smoke here, but like, yeah, they.

**Dave Jones:** What? So they just stop in the middle of nowhere and then you can just hang out and smoke your fag and what?

**Chris Gammell:** Yeah. They stop at a, they stop at a, you know, a station and they say like smoke break for like 10 minutes, 15 minutes. They also use it to like compress schedule. That's right. Yeah.

**Dave Jones:** So did you see anyone actually do it or? Of course. Yeah. Okay. Right. Yeah.

**Chris Gammell:** I mean, cigarettes aren't 25 bucks a pack here. Like they are in the Aussie. Right. Yeah. No, I think they're so expensive.

**Dave Jones:** I think they're about 50 here now.

**Speaker ?:** Oh my gosh.

**Dave Jones:** Yeah. That's awesome. Yeah. I think it's nuts. Yeah. Yeah.

**Chris Gammell:** Oh boy.

**Dave Jones:** Smoke go breaks. Oh my God. I can. Yeah. Classic, huh?

**Chris Gammell:** Actually, the old days they would have just been like, you could smoke on the plane, on the train rather. Oh yeah.

**Dave Jones:** There were smoking carriages, but you had to find the smoke. It was usually at the end. So you had to run down the end of the platform to get to the smoke because my dad smoked. So I can remember, yeah, we, you know, having all to run down to the smoking carriage, you know, because that's, you know, but yeah, that went the way of the dodo by the late seventies, I think. I think they. No.

**Chris Gammell:** God, no. Oh yeah. In Aussie land maybe, but in the US not until the nineties. Yeah. I mean like on planes for sure. Oh God, no. No, no.

**Dave Jones:** I think it was gone by at least the mid eighties smoking on, on trains and buses was gone. Yeah. And planes as well. I think. Yep.

**Chris Gammell:** Good riddance.

**Speaker ?:** Yeah.

**Dave Jones:** Oh boy. Anyway. How did we get onto that?

**Chris Gammell:** Trains. Yeah. So trains are great.

**Dave Jones:** Trains. Yeah. Trains are great. Trains are great. Love it. Love it. Both train fanboys. Yep. Excellent.

**Chris Gammell:** Yeah. I was going to, oh, I was going to pull up Adrian Studer. I was looking up to see if we'd had him on the show and like one of the, uh, I thought we may be at one of the conferences that I've talked to him before.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** But he has a, I think it's an APRS receiver. Yeah. He was at, oh, there we go. Episode 450. I talked to him at teardown and he has like a receiver, AIS receiver. So that's something where you could also collect. I think, I think that's boat beacons and stuff like that. Okay. Right. I'll link that show into.

**Dave Jones:** Cool. Yeah. Yep. Yeah. So if you live somewhere obscure, you know, like, like in the middle of whoop whoop or something, then yeah, it'd be cool to like install these receivers and then feed the data back because, you know, like if you live in the city, like, you know, like there's heaps of them around, but you know, if you live out in the middle of nowhere, yeah. Or a top of a mountain or something, you know, then yeah, it'd be really nice to install some of these things and get all this coverage for everyone to help track, you know.

**Speaker ?:** Yep.

**Chris Gammell:** So, uh, I was talking about the analog discovery too. There was a David Cherry. He sent me one. It's a, basically it's like he built a differential front end for analog discovery too. Yep. It's super cool. It's basically just like op amps and like balancing and stuff like that, but it kind of like supercharges this thing.

**Dave Jones:** Didn't it already have a selectable differential or single ended option? Or am I thinking of something else?

**Chris Gammell:** It has a differential option or differential input for the, for the scope input, but it's not a difference amp, right? So like actually having like rejection and stuff like that. Right, right, right. So I think he posted about it on the CE forum, but yeah, I think, I'm not sure if he's making them yet. He at least sent me a prototype of it.

**Dave Jones:** I really wish that was open source. That'd be cool. Cause you know, you could, cause the software is so good, right? It's the software that makes that thing, right? The hardware is just, okay. You know, the hardware is the hardware, right? You know, it's just a few chips on a board, right? Right. But yeah, no, the software really, really makes it. And it'd just be great. You know, like the interface is open, like you can, so you can design all these boards to plug into it and, you know, front ends and stuff to plug into it.

**Chris Gammell:** But yeah. Yeah.

**Dave Jones:** Yeah. Unfortunately, the hardware itself is not, it's not open. Right. So, right.

**Chris Gammell:** Even so, like one of the testers that I have for one of my, one of my boards, I use, I use an analog discovery too. And then I've, I've started working on a interface basically to just instead of like, so right now I like, you know, manually plug each cable in when I need to test something. It's like, oh, I should just make a conversion board from one to the other. And then the discovery two becomes a, almost like a, almost like a tester in production. And that's what they're trying to do with like the pro, right? So like analog discovery pros, this new thing that came out. Yep. But it's not, I mean, it's cool. It's, it's higher end and it's got like a computer that sits in it. So it's got like a Linux box inside of it, but it's really the portability and the simplicity that I'm looking for. And I guess the scripting too. So that's cool too. It's got like, it's got Python scripting, but the built-in on the back end is like JavaScript and it's simple enough where like I can do it. And so that's like saying his own thing there, you know? Yep.

**Dave Jones:** Yeah. Nice.

**Chris Gammell:** Yeah. But I, I really like it just for travel. Right. So, so my travel, you know, we, we, we, we've talked about the portal lab and it's shrunk over the years and now it's a TS80 at your recommendation. It's a, what's the other one? The Anang. What's the Anang?

**Dave Jones:** Which is the soldering iron for those playing along at home. That's right. Yeah.

**Chris Gammell:** That's the USB-C soldering iron.

**Dave Jones:** Yes. Yes. USB-C.

**Chris Gammell:** The Anang, which is I think another one you do.

**Dave Jones:** Do you plug that into a power pack or do you plug that into your PC to power that?

**Chris Gammell:** I plug that into, so I have my PC supply. So when I need to, I can power off.

**Dave Jones:** Oh, okay. You can just actually, yeah, right. Yeah. Of course.

**Chris Gammell:** So if I need that and then I also have, I also bring the plug pack with it so that I could plug into a wall directly with like the, I like the flexible cable. And then actually there was a, what is it called? It's a crowd supply thing that I backed that is a PD, a power delivery board. Right. So I could also use that if I needed to as well. Cool.

**Dave Jones:** Yep.

**Chris Gammell:** So I think that's already passed, but it was, it was pretty, you know, it's a pretty cool little board. And then Anang 8008, I think that's another one of your recommendations.

**Dave Jones:** Oh yes. The little meter. Yep.

**Chris Gammell:** That's right. So all this stuff actually fits. I actually, I harvested the analog discovery to like case that it comes in and I use that as my new carrying case. Right. So it's got then the probes, the analog discovery to set aside side cutters. Yep. And that's kind of all I need most of it. Oh, uh, like a serial interface. So like USB to serial, like to have a separate one for that sort of thing, bunch of solder, some, uh, enamel wire just for like hacking stuff together. And then that's kind of it.

**Dave Jones:** No portable power supply. You don't really, because you're, because you're not really working on breadboards or any, you know, you're not really, you know, building stuff.

**Chris Gammell:** I can use that USB PD thing for that as well. Yeah. Oh, okay. So that, that has selectable output. I mean, it's not going to be like, like dialed in. Yep. I would have, I would have put a, you know, a micro supply in there, Dave.

**Dave Jones:** Yeah. A micro supply. I know the sexy micro supply. Yep.

**Chris Gammell:** Wow. Yeah. I know. Is that dead forever? Is that, is that gone? Probably. Yeah. I think so. Oh, okay. Well, it's a market opportunity folks. Yeah. If you want to make it into the portal lab on Chris's and Chris's backpack, call me. Right. So, yeah. Cool.

**Dave Jones:** Yeah.

**Chris Gammell:** I'd, I'd probably have like the same stuff.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** It's, I mean, it's great for just like random, I'd say if work holding would maybe be another one. I, you know, those, they had those like the little clampy things for like bench level clamps. I like those two, but they, mine broke and what do they call that? Like the floor vice or something like that? Right. Travel vice. I don't know.

**Dave Jones:** The thing is like everyone's requirements are different. There's no such thing as like a universal portable lab, you know, it's, it's just like, it's not going to suit everyone. Everyone has a different requirement. So. Yeah.

**Chris Gammell:** I mean, I mean, some people are like, well, I work on RF. It's like, oh, okay.

**Dave Jones:** Well, yeah, well, home, uh, for example, like, you know, not, you know, there is no generic home lab. Like it depends on the stuff you're working on.

**Chris Gammell:** That's right. Yep.

**Dave Jones:** Oh, that, that brings up, I haven't got it on here, but maybe I can search for it or something. What is it? Um, it's somebody on the EV blog forum, right? A kind of like a noob, not total noob, but you know, setting up a lab from scratch and needless to say, this caused a bit of controversy. Their, their post was, um, controversy. They, their post was basically, oh, what is the best scope I can get for $30,000? Oh, it was like, for $30,000.

**Chris Gammell:** They come into some money recently or what is it? Yeah.

**Dave Jones:** Yeah. Yeah. They basically said, yeah, I've come into money and I, and I want a really good scope for my home hobby lab. And it's like, I'm willing to spend $30,000.

**Chris Gammell:** That's actually, that's a very interesting, uh, I know exercise. It is.

**Dave Jones:** It is. And so you can imagine, cause the EV blog forum is the world's biggest test equipment forum. That's right. Everyone just went. Yeah. Like, wow. Yes. Well, no, everyone tried to talk him out of it basically. So. I mean, he had no experience. Uh, little, I think little, but he just, yeah.

**Chris Gammell:** I wanted to know what this comes down to the, uh, you should never buy the Gibson Les Paul as your first guitar.

**Dave Jones:** Oh, right. Yes, exactly. It's the same thing. Yeah. Yeah.

**Chris Gammell:** Not, not, not only because you will ruin that guitar, but it will ruin you.

**Dave Jones:** And I, oh, I'm having trouble finding here. Why? That's okay. I mean, yeah, but anyway, I'll put in the link. And one, one of my responses among several was that, look, you know, basically suck of

**Chris Gammell:** the salve as they, as they say, I have more thoughts about this. I've been thinking about it overnight and I have more things to say.

**Dave Jones:** It was basically that. Okay. Right. Anything over probably two or 300 megahertz, especially, especially over 500 megahertz. You really just taken the piss for a general purpose scope. Right. Because the, a, the passive probes that come with it won't go that high. Okay. There's probably, I think there's only one manufacturer in world, which is Tektronix who do a one gigahertz passive probe. Like a, you know, a, uh, regular 10 to one passive power.

**Chris Gammell:** Or yeah, it plugs right in and even that.

**Dave Jones:** Without being an active probe. Right. Right. And it's like, no, but if you actually do the calculations on that, it's like 30 ohms at one gig. Like, cause it's got four and a high, it's got four picofarads input capacitance. And that's like 30 ohms. It's like, yeah, have, have fun with your 30 ohm probe. Okay. No, it's like, it's, it's just, you know, I'm not going to say it's silly, but.

**Chris Gammell:** Well, what, what, what level of electronics was this person going for? I, I, I actually love this as a mental exercise. Cause.

**Dave Jones:** Oh yeah. It was just a basic lab scope. I'm going to have to, I'm going to find it here. If you can talk for a second, I can find it.

**Chris Gammell:** Oh, okay. Well, I mean, I, the one thing I think about is like, okay, so I already talked about like the Gibson Les Paul thing, how that would ruin someone. But I mean, I don't really know what most people need on most of these scopes. Even like the, you know, like I think about the amount of functions that I use on the scopes in or around my bench. And it's like, uh, okay, maybe 25%. And you know, the, so people can get away with a lot of stuff. And so then it all kind of comes back to like, if you're a true beginner, what do you really need? I think you need repeatability, right? You need like, so stability, you know, don't buy the bottom of the barrel because you're going to, you're going to get hosed, right? You're going to, you know, maybe you're going to have extra noise in there. You're not going to understand what's going on. I think actually one thing that's important for beginners is buying something that other people have. If you buy some brand new, no name, whatever, and then you have a problem with it. Of course. You're screwed. You're screwed. Yeah. Right. Right. Yeah. So yeah. Even, I mean, maybe if you can buy support from the, from the company you're buying it from, maybe if you trust them, but if you know, no, then you have no community support.

**Dave Jones:** Exactly. And, and like the scope hasn't been hacked yet, you know, or something like that. Right. Yes.

**Chris Gammell:** And it's like, anyway, I think about it kind of like, kind of like how I think about 3d printers, right? So I have a decent amount of experience with scopes, very little experience with 3d printers. My number one requirement was what are the most people say is the right answer. Exactly. And price was a little bit less squishy there. Yep. It's, it's actually more about like, what am I going to do when everything goes to shit? Yeah, exactly. I'm going to go online. I'm going to start Googling and I'm going to hope for a lot, very helpful community. Exactly.

**Dave Jones:** Exactly. Yep. So I would be in the same position if I was buying a new 3d printer. Totally. Yeah. I mean, like, and, and reliability. So again, that, that also kind of, or if I was buying a pick and place machine, if I was buying it, you know, definitely. Right. What is the one that most people have Dave? None. That's the answer.

**Speaker ?:** None.

**Dave Jones:** Right. But you know, there's little small communities, you know, out there. So yeah, I would find a dedicated one that has a dedicated community. Absolutely. And it was like, anyway, I've sent you the link to the, what is the best oscilloscope I can get for $30,000 and Symax on the forum. My budget is $30,000. I want a very feature rip scope. And I figure with that kind of budget, I can, four channels. The goal is I buy one scope to have it be the last scope that I'll ever need. Some of the plans include decoding software, like on micros, Arduinos and picks. Right. But he does, he does mess with RF from time to time, but it's like, yeah, come on.

**Chris Gammell:** I would buy a $1,000 scope and a $28,000 field Fox.

**Dave Jones:** Right. Yes, exactly. Yeah. I, that was one of my responses as well. Like, yeah, I would like buy a couple of grand scope, you know, buy a nice couple of grand scope. And then I'd buy a nice, you know, a couple of grand spectrum analyzer. And then I'd buy an, you know, all sorts of, you can, you can equip your whole lab. You can get a really nice schmick lab for under 10 grand. Right. Yeah. So you only have to spend one third.

**Chris Gammell:** If you want to spend a lot of money, get into RF. Do you remember how I mentioned that? Yeah, exactly. Mr. Jeff Kaiser has, has my, my $3,000 very old, very used HP A753D thing. It costs $3,000. Jeff spent another $3,000 on frigging cables, Dave. Cables. Yeah. Cables. I know. RF is dumb. I know. I love it, but it's dumb. It's dumb.

**Dave Jones:** Totally agree. I know. Yes.

**Chris Gammell:** Don't at me. Yeah, that's, that's nothing. Don't at me. RF is dumb.

**Dave Jones:** Dude, I used to pay 1500 bucks for test leads for a resistance meter.

**Chris Gammell:** Oh, I believe it. Yeah. Yeah.

**Dave Jones:** Yeah. Mm-hmm. A, a high voltage HP resistant HP back in the day, you know, key site, you know, whatever. Sorry. Sorry, agilent, you know. And yeah, but because they're this special bloody, uh, tri-axial, you know, bloody connectors on them. And, and the test leads, they're like a thousand US, which is like 1500 Aussie bucks or something for these bloody test leads for a freaking resistance meter.

**Chris Gammell:** Oh yeah. Keith Lee, Keith Lee made tri-ax too. I wasn't allowed to have those, man. When I worked there, they were like, no, we don't have that many of those.

**Dave Jones:** Yeah. Yeah. Lovely tri-axial connectors. Pain in the ass, you know.

**Chris Gammell:** That's right. That's right.

**Dave Jones:** Yeah. But, you know, cause it's a high impedance resistance meter, right? It's not just a regular, you know, up to 10 meg kind of thing, you know, it goes up to, you know.

**Chris Gammell:** Yeah. You're driving it with a couple thousand volts.

**Dave Jones:** Yes. Yes. It can go up to a thousand volts and, uh, down to, you know, pico amps. Yep. Yep. Yeah. So yeah, it's a very sensitive piece. So you need these low noise, special low noise tri-axial bloody cables for it just to, just to do production testing. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So, you know, I had to buy these in the dozens and it's like, oh God.

**Chris Gammell:** So where did this person land? I'm having trouble seeing the link you sent, uh, it looks broken. Uh, it looks like I got chopped off actually. But, uh, where, where did this person land? I'm very curious about this sort of thing.

**Dave Jones:** I am. I, I will find it for you in a second, but where is the. Oh, really? You can get four. Oh yeah. No, it's chopped off. I'll send it to you on the, um, on the, uh, here it is. There you go. There's the link on the, uh, googly's. The googly monsters.

**Chris Gammell:** Ah, got it. Yep.

**Speaker ?:** Cool.

**Dave Jones:** Right. Got it. All right. I don't think it's, it's up to seven pages of responses now. So I, last I heard, he hasn't decided. I was the last one to post. So I, no, he had decided on, I think the one gig siglant. I don't know if he's actually purchased it yet, but he looked at the siglant, the one gig version of the siglant. And I'm going, eh, well, once this is why I replied, like, why the one gig? Like, you know, you really don't need anything more than three, 500.

**Chris Gammell:** You know what I would do, Dave? I would send this post. If this was me, I would send this post, maybe along with a bank statement or equivalent to every FAE. Right. And I'd be like, can I get your nicest scope on loan, please? Yes, exactly. I would like to try it out. And they'd say, yes, sir. Right over here, sir.

**Dave Jones:** I know. That, that was also one of my replies was that they will, the local dealer will happily come to your place. That's right. And, and show you, they will, you know.

**Chris Gammell:** It's like that scene in Pretty Woman where she goes shopping for like all the dresses and stuff like that, you know.

**Dave Jones:** And yeah, they'll come by with the scope and they'll, and they'll give you a free foot.

**Chris Gammell:** They will outfit your lab.

**Dave Jones:** They will give you a free foot massage and everything for, you know, there's a 30 grand sale on offer, you know. Yep. Yep. But yeah.

**Chris Gammell:** That's what we need, Dave. We need, we need the Rodeo drive for electronics. Right, right.

**Dave Jones:** Oh boy. Yep. Well, that, that's DigiKey, isn't it? The, the record. Oh, maybe. Because, you know, because I, I, I did this tweet. I don't think we've talked about it. I did this tweet where I looked at while I was doing searching for jelly bean parts, I came across all of.

**Chris Gammell:** You, you, you, you, you sorted by price in the other direction.

**Dave Jones:** I sorted by price in the other direction. And I'd like, I've done this many times over years because it's fun. Right. Yeah. It's totally fun. And, and the cheapest, the most expensive chip I found was $22,000.

**Chris Gammell:** You want to see some military parts. You will find some military parts. Yes.

**Dave Jones:** And that's exactly what I found. Right. And the most expensive chip was $22,000. No, no. It was a hundred and a hundred, no, $128,000. But it turned out.

**Chris Gammell:** And it was like a CPLD from the early nineties.

**Dave Jones:** No, it turned out it was actually a wafer. It was actually like, apparently a full wafer. Like you could actually buy the full wafer from the factory. No. Oh my, I don't know. Cause Rochester, so Rochester electronics.

**Chris Gammell:** I've complained about, I still complain about Rochester electronics. I would love to talk to people from there. If anyone knows people there, but I complain about them because they pop up in searches and I did. They're just not what I want.

**Dave Jones:** They infest DigiKey now. They infest it. Do you know if that, like if they ship components to DigiKey and then DigiKey ship them to you or I, cause I've never ordered a Rochester part through DigiKey. I have by accident. Does anyone know? Oh, you have. Okay.

**Chris Gammell:** They must have stock on hand. I think they must. Right.

**Dave Jones:** Okay. Yeah.

**Chris Gammell:** It's a, so people don't know. Rochester basically buys up old wafers. They then have like service contracts for people who say, I need, I need this to source for 10 years. The vendor can do it.

**Dave Jones:** For the military, for the government, that sort of thing.

**Chris Gammell:** Not just, not just military. I mean like. Not just, but that's a huge part. Yeah. Automakers need 10 year agreements. Right. Yes. I think, I think, I think for low volume where you're not going to be able to show up with, you know, a million dollars at the door, you're not, you're not getting the foot massages. Right. Right. You're, you're a small time player, but you can guarantee this like longer term income.

**Dave Jones:** Yeah. It makes sense. No, I've, I've been involved in this once again for the, uh, this was not, this was not the military. This was a, for commercial contract. Right. They sort of like custom design this analog to digital converter for us. Right. For the seismic market. It wasn't just for us, but it was for the seismic industry. Like nobody else uses this chip. Right. This chip is just designed for the underwater seismic industry. Right. And there's maybe five customers worldwide tops. And we were one of them.

**Chris Gammell:** Right. Right. And it's probably not listed on DigiKey or equipment. No, no, no.

**Dave Jones:** I, no, it did. You've, it was probably not even on their website. Right. So yeah, we would get like the, we would get and test like the beta silicon and everything. Right. So yeah, but we would have to, this was part of the negotiations for the contract for designing this product, this part into our thing was that, yeah, we need like a 15 year guaranteed in writing signed by your CEO. Right. A contract to supply this part. Right. And they did it. Right. They, they, yeah. The actual CEO signs it and goes, yep, we will guarantee this for 15 years. We will still make this for you regardless of how much it costs us. You know?

**Chris Gammell:** Yeah, totally. Yeah. I mean, that's, I think that's kind of like the table stakes of certain things. Right. I mean, like that was it for even industrial stuff that I used to work on. Same, same kind of thing.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** So yeah. So there you go.

**Chris Gammell:** So I think, I think the problem though, is that sometimes those companies, even though they have those agreements, they go out of business. Right. And they just, they flop or, or something happens.

**Chris Gammell:** No, of course. Or they get bored. Or they sell the service contract to someone like a Rochester. And I think that's what we're ultimately seeing. And I think, I think then sometimes also Rochester's buying up wafers, they have agreements with a vendor and they say, we want to buy these and package them ourselves.

**Dave Jones:** And, and, and they do actually re, they do actually remanufacture chips. So they actually, I don't know if they do it in house or whether or not they subcontract somebody, but they actually take this, the wafers that they've got and they actually package them up. They will actually package them and test them and, you know, sell you a finished chip for this obscure chip from the 1980s.

**Chris Gammell:** Yeah.

**Dave Jones:** You know?

**Chris Gammell:** Yeah. Yeah. It's, it's fine. I mean, like, I'm sure it's actually a great business. I'm sure it's stressful business, but I just don't want to see it. That's the main thing.

**Dave Jones:** I don't, you don't want to see it on your DigiKey. Yes, I know. There, there, there is a button on the DigiC which says remove marketplace items. Oh, I know that one.

**Chris Gammell:** Oh, that's.

**Dave Jones:** But they still come up.

**Chris Gammell:** No, they're a real vendor. I mean, that's the real thing. That's, they're not a, they're not a.

**Dave Jones:** Oh yes. Right. Okay. Yeah. But it did get rid of a lot of them. So I'm not sure what, I'm not sure how it actually works.

**Chris Gammell:** I bet that's the split then. I would bet that the marketplace is someone who's shipping from their own factory and then, and then in-house they have, they have stock.

**Dave Jones:** Whereas the other one, if it still shows up from them, then DigiKey will have it on their shelves.

**Chris Gammell:** Surprisingly, this segment not brought to you by DigiKey. DigiKey, right. We have no affiliation other than knowing some people there. And you know, I guess being fanboys, sorry. Yeah.

**Dave Jones:** Yeah. Right.

**Chris Gammell:** We're just, you know, we're just fans of small towns in Minnesota. Oh yeah.

**Dave Jones:** Exactly. Okie dokie. Anyway, the most expensive, somebody, somebody found the most expensive item on DigiKey so far, so far, what was it? $1.8 million. Ooh. Okay. And it was a Molex tool.

**Chris Gammell:** Oh yeah.

**Dave Jones:** There is no photo. There's no photo. There's no jar of sheet. You can't find a link to it anywhere on the internet, but there's this weird Molex tool part number that's listed for $1.8 million on DigiKey. Wow. Or is it 1.2 or something? Anyway, it's, yeah, it's there.

**Chris Gammell:** You can order it. Maybe our $30,000 scope friend has enough money for that sort of thing. You really, you just got to ask what the return policy is like. You're right.

**Dave Jones:** And it's, you know, 40 week lead time.

**Chris Gammell:** What's the, what's the shipping like to, to Australia? Oh man. Oh boy. Yeah.

**Dave Jones:** Yep. It's just, yeah, it's, it's, it's nuts.

**Chris Gammell:** Speaking of obscure parts, you are hoping to find, you've talked for many years about the obscurity of low gate count FPGAs. Oh yes.

**Dave Jones:** Right. There are some. Yes. I've been saying this for 15 years. This is Dave basically being like, I understand CPLDs. It's not really. No, it's, it's, it's not. Unfortunately, it's not. It's not a. No. My, my dream was to have like a million logic, like a big high end beefy FPGA with a million logic elements in an SOIC. Yeah. Or just, just any small, any small usable pin count.

**Chris Gammell:** As people listened to last week when Carmen was here, the, the power requirements alone, if you had a single, so if you have eight pins, that means one of them is power. And that means you have a lot of inductance. Yeah.

**Dave Jones:** The surge power just to turn on. Yeah. Right. Right. Right. Yeah.

**Chris Gammell:** That thing would, that thing would start, that thing would start singing. It would start singing to you. You're all of your expensive RF equipment you bought for your lab. It would, it would light up.

**Dave Jones:** Yep. Oh boy. But yeah, nah, they just, anyway, no, this is cool. Former guest of the show, Steve Leibson, he tweeted, cause he works in that business, that Genesis through, cause they acquired, Genesis acquired, who was it?

**Chris Gammell:** Everyone. They acquired Innerso, who Carmen was talking about last week.

**Dave Jones:** No, no, no. Green Pack. Oh, they did. Oh, I didn't realize that. Who makes the Green Pack chips. Oh, I thought they were a standalone company. They actually, yeah, so they actually acquired them. And it's, I think through their arm that they're doing these new FPGAs, but they're ultra low power, low cost. They're, they're called the forge FPGA family. But the thing is, is that like they got, you know, just like jelly bean kind of thing, like 5,000 gates of logic, right? They got one to 2k of lookup tables and stuff. They worked down a standby power of 20 microamps, right? And they've even got a one-time programmable jobbing. So it's like, you know, you program this thing for production. And they're available in what packages? Like little low pin count packages. And they're going, yeah, we, we're, we're going to service this market that has not been served before. And they're 50 cents.

**Chris Gammell:** Not for me, but interesting. Yeah. I feel like this is like them looking at Green Pack and being like, people want more of that, but in one place, you know?

**Dave Jones:** Oh yeah. Well, for those who don't know, the Green Pack is like an, an analog FPGA kind of thing. Like they've got little up amps and switches and kind of thing.

**Chris Gammell:** I think of them more like a one-time, one-time programmable, like logic gate, programmable logic gates in like the tens of gates.

**Dave Jones:** And they've got logic gate version as well, but they do have a mixed, yeah, they have like

**Chris Gammell:** timers and stuff like that too. Yeah.

**Dave Jones:** No, no, no. They have mixed signals. So they've got other stuff in there. Yeah. So they've got analog-y type stuff in there too.

**Chris Gammell:** What I really think about with Green Pack is hard to get expensive. That was always my thing. I was always like, this, this is for like, you know, this is like for someone maybe in my ABB days when it was like, I was big enough that they would get the, and like the price was low enough. But this is for someone like making a specialized, someone doing like a load dump test capable board at a car manufacturer. And they're going to make a million of them. You know, Toyota is going to make a million of these things and they just need this one thing to work around this one problem they have. And it's going in there. Like, that's what I think about it.

**Dave Jones:** Exactly.

**Chris Gammell:** You know? And then, and then, yeah, it's 10 cents now. Uh, cause you're Toyota.

**Dave Jones:** Anyway, the thing I, the other thing I like about it is not only are the tools free, but they've also got a schematic capture tool. Basically they've got like a, like a join the, you know, join the gates up. Right. So for those who don't know, don't groan. Right. If you, if you, if you're not comfortable with HDR, if you just want something that's, you know, if you just got a simple design and you want to consolidate some glue, some, you know, logic, glue logic, right. Into one little FPGA that solves your little problem. You don't want to write hate, learn and write HDL for it. You just want to throw in the schematic, you know? Yeah. I look, look, I need a bunch of shift registers here and I need some, you know, flip flops here and I need some, and you just join them all together and Bob's your uncle.

**Chris Gammell:** Right.

**Dave Jones:** You don't have to dick around with the HDL and knowing, you know, all that synthesis crap. Right.

**Chris Gammell:** Yeah. This is the, both of those things are not for me. So, uh, not yet, maybe in the future. We'll see.

**Dave Jones:** Oh, right. So you're just, yeah, right. I'm just a knocked out.

**Chris Gammell:** The whole FPGA thing is not for you. Yeah. Right now. I mean, I'm not, I think I might operate, you know, these days, given the stuff I've been doing, I might operate at the, you know, ECP5, put a microcontroller in it and then add some logic around it. Uh, that might be something that fits what I'm doing, but yeah, not.

**Dave Jones:** You, you sound like more of a hard sell, hardcore, I'm here all week. Hardcore, hard processor core fanboy. Yeah. Like an IP block. That sounds like something you would use.

**Chris Gammell:** Like having like a Cortex M4 internal, like, uh, yes, exactly. Brian Faith was on the show. The, uh, what is that called? The, uh, quick logic. Yep. Brian came on, was talking about quick logic. It's got like a Cortex M4 in there and it's got some blue logic and some other fanciness around it.

**Dave Jones:** So, and it's got some fabric around it. Exactly. Yeah. Yep. Yep.

**Chris Gammell:** Uh, yeah.

**Dave Jones:** So yeah, the, the thing I like about these is that they've basically turned the industry on its head by saying, yeah, we're, we're going to cater for low cost, small pin count, small, you know, FPGAs. And we're going to also give you these like cool schematic capture tools. I haven't tried it yet, but it sounds good. Like, whereas the whole industry was going away from that. Right. That was a thing. Schematic capture was a thing back in, you know, the eighties and nineties. Right. But then they went in, into the HDLs, the high, high definition languages, sorry, the hardware description languages. Right. They, they went all into that. So Verilog VHDL, right. That was, you know, that was the only way you did FPGAs in modern times. And they're going, no, we're going to go old school. Thank you very much. Yeah. We'll give you your HDL tools, but we're going to give you a schematic capture as well. And I think that's fricking great.

**Chris Gammell:** I think, yeah, they're targeting. I think what they're really telegraphic with that is that they're targeting us that previous market. Right. So like people in the CPDL space.

**Dave Jones:** And while they're targeting non FPGA people, cause it's a big learning curve to learn a HDL. Sure. Right. It's a totally different mindset to go to. Yes, it is. What?

**Chris Gammell:** You don't agree? I, I, no, I think you're, I think you're talking about two different things though. I think one thing you're talking about is like synchronous, like thinking about how data is flowing through a device and stuff like that. That is different than people who are used to like iterative processing, like on a microcontroller where it's going through loops and things like that. I feel like that's one thing, but then you're talking about the, the flow of, okay, now I've, I've learned that stuff. I've gotten it right. I, I, even if I borrowed someone else's code and okay, so you start from someone else's code. Now you have to then run it through a synthesizer, run it through place around, run it through all those tools. And that is a second thing that's hard to understand. I feel like.

**Dave Jones:** Yeah. It's an entirely different mindset, right? Every, every engineer is taught logic, right? They're, they're taught. Not very well for me. They're taught gates and their carton, right? And their Kano maps simplifications. And they're taught, right? They're taught all logic. I still love Kano maps. Come on. Kano maps. Yeah.

**Chris Gammell:** You're just doing Kano maps for, for funsies. Yeah. Yeah. Yep. Funsies. Yep. Anyway. Everybody's got their hobbies.

**Dave Jones:** Jeez. Anyway. So that's how you're taught, right? That's how you're taught. And then you're taught sequential programming on microcontrollers and processors, right? They're the two things you're taught. You're not taught hardware. Like you're not taught.

**Chris Gammell:** I think some of this is changing.

**Dave Jones:** Hardware description language. I think some of this. Oh yeah. It might be. Sure. It might be.

**Chris Gammell:** The newer, the newer, the newer class of, uh, of engineers. Maybe. I'm sure. I hope. Right. I hope.

**Speaker ?:** I hope.

**Chris Gammell:** Newer classes.

**Dave Jones:** Maybe. So, but, but it's basically a third discipline. That's what I'm saying. Sure. Sure. Right. There is, there is logic. There is HDLs and there's sequential programming. They are three different disciplines. Sure.

**Chris Gammell:** I'll give you that.

**Dave Jones:** And they have their own rules. They have, they have their own traps for young players.

**Chris Gammell:** Oh, I think, I think one of the big traps is if you are coming from that like top down, like starting from HDL and being like, okay, now I'm going to like, I understand all this stuff as like from a programming model, but like you don't understand what's happening underneath, then you're like, I have this program. I don't know why it's placing and routing for such a big thing.

**Dave Jones:** Oh, well then you get into the intricacies of the FPGA and the architecture of the FPGA

**Speaker ?:** you're using.

**Dave Jones:** Being closer to the hardware and stuff like that. That's another thing. Yeah. That's totally another thing. No, I, I'm, I like the fact that they went backwards to old school schematic captions. I think you should try this out. I want to play with them. Yeah. I think you should. I am. I'm, I want to get a kit. Okay. Yep. Bring it. Absolutely. Yeah. So yeah, I think you can download the software now, but I can't, I didn't find a data sheet at readily like straight away. But anyway, yeah, it's very cool. Do you disagree? I want one. So yeah, I'm going to try and get, I think there's a preliminary dev kit available. So I'll try and get a preliminary dev kit.

**Chris Gammell:** I mean, Dave Jones can't get an early dev kit. I mean, what are we even doing here? We'll see. Yep.

**Dave Jones:** Cool. All right. How much time we got left? Have we pissed it all the way on DigiKey?

**Chris Gammell:** We have about five, five minutes left. We can always go longer, of course. But yeah.

**Dave Jones:** Right. Boy. All right. We should make the photo for this one. Me in the DigiKey sack. You in the DigiKey sack. There's an old photo of me. Was it? Oh God, what is it? There was a photo of me in an EV log DigiKey. It came in a sack or something. There was a potato sack?

**Chris Gammell:** Like a...

**Dave Jones:** DigiKey postage fail. 146. Here we go. I'm just looking at my... Yeah, we are in the old days here.

**Chris Gammell:** I was just looking at Steve Leibson's episode two when he was on the show. That was episode 99. Like, damn. I forgot Steve was even on the show. I mean, like, I followed Steve for a long time, but yeah. And didn't he retire and then he just joined another company? Didn't he just like...

**Dave Jones:** Oh, yeah. He's joined... He's with yet another company. So, yep. Some consultant... Yep. Good for him. I don't know. Anyway, there's a quote from him in the article.

**Chris Gammell:** Cool. Okay.

**Dave Jones:** So there you go. So, yes. There's the... Here's the incoming thingamabob.

**Chris Gammell:** Dave in a sack.

**Dave Jones:** For the... Dave in a sack. Yes, I believe. Yeah. I think it's... From memory, it's like at the end or something. I come in... I stick the DigiKey sack on my head. Not recommended for the kiddies. Yeah. Yeah. Yeah. There it is. Right at the end.

**Chris Gammell:** Tell my daughter not to do that. Yeah. Okay.

**Dave Jones:** It's actually a Swiss Post bag. So I don't think it's actually branded DigiKey. So, yep. So I guess that's not a good thumbnail. Okay.

**Chris Gammell:** So maybe it's...

**Dave Jones:** Forget it. Okay. We just pissed away another five minutes on DigiKey. Stop it. Come on.

**Chris Gammell:** Come on.

**Dave Jones:** Focus. Focus.

**Chris Gammell:** Focus, Dave.

**Dave Jones:** Okay. Oh, we have to shout out the wooden seven segment display. Holy crap. Oh, my God.

**Chris Gammell:** That thing was gorgeous.

**Dave Jones:** Oh. Oh, that is magical. Yeah. Who is it? I can't pronounce it. It's K. K. Dollar Sign Yuzuki. I think, yeah. Beltree Nursing.

**Chris Gammell:** I think it's Suzuki.

**Dave Jones:** Suzuki. Beltree Nursing on Twitter from Japan. Yeah. This is... Like, holy crap. Yeah.

**Chris Gammell:** So why don't you explain what a wooden seven segment display is?

**Dave Jones:** It... Well, it is a two digit display. It's about like an inch high or something like that.

**Chris Gammell:** Wow. Imperial units. Look at that. Dave's really flexing on that one.

**Chris Gammell:** Absolutely.

**Dave Jones:** And... And it's... Yeah. So a two digit wooden display and there's like a knob on the bottom of it that is turning. And these... It's... It looks like a real seven segment display. But it's actually like little slithers of wood that come through that are obviously like painted on top or have some little top thing on the top. And there's all these cogs in there that flip the segments over as he goes. And there's this like coding wheel inside which then determines which ones are flipped in and which segments are flipped in and out. Yeah. And it's all manufactured with wooden cogs. It's magical.

**Chris Gammell:** Yeah. Following this person's channel is just like a... It's like a playground of like wooden clock masterpieces. Oh, yeah.

**Dave Jones:** Oh, really? Okay. So it's... Oh, they make wood. I didn't look at their profile. Okay. So they make wooden art and... Yeah. Oh, yeah. I think clock specifically.

**Chris Gammell:** I think clock specifically. Right. And there's more... Okay. There's more mechanics on there. But yeah, it's... Wow. It's intense. It's intense. It's very cool.

**Dave Jones:** Oh, there's another one as well.

**Speaker ?:** Mm-hmm.

**Dave Jones:** If you scroll further down, if you go to the channel and scroll further, there's like a large one and you can see the cogs inside.

**Speaker ?:** Yeah.

**Dave Jones:** And it's a single digit like, you know, four inches high or something like that.

**Chris Gammell:** At first I was wondering because it goes from zero all the way through 23. I was like, what the hell is it doing? And I was like, oh, yeah. Okay. I get it. Some people keep track of time like that. Okay.

**Dave Jones:** Yes. Yeah, they do. And it's just... Oh, Ed. Wow. Yep. Hats off. Absolutely fantastic. So... And oh, yeah. There's extra photos of the pieces that go inside there and stuff. Oh, there's another photo of the... Without the segments on the front. That's really nice. Yeah. Oh, it's just... Anyway. Yep. Fantastic. What else we got? I do like the... Robert Teldr has how to make a CPU picture guide. I think this is great. I think this is terrific. Yep. So shout out. We'll link that in.

**Chris Gammell:** It's just like the process steps. And it is pretty high level, actually. So it's basically talking about like semiconductor processing.

**Dave Jones:** Yeah.

**Chris Gammell:** All the way down from like, you know...

**Dave Jones:** Yeah.

**Chris Gammell:** Well, smashing a... Get a rock. Smash a rock. Yeah. Okay. Come on now.

**Dave Jones:** So he's making it look like he's actually making this in his poem. You know, he's like...

**Chris Gammell:** Right. All the way from the ingot as well. Yeah. Yeah.

**Dave Jones:** All the way from the ingot and everything else.

**Chris Gammell:** Come on, Sam's aloof. You haven't made your own ingot yet? Yeah. Exactly. Just making these things in your dorm room? Anyway, yeah.

**Dave Jones:** I just think that's worth a shout out. Yeah.

**Chris Gammell:** That's great. What else? No, that's it. There is an old article about Sting Operation where they basically spoofed...

**Dave Jones:** Oh, you wanted to.

**Dave Jones:** It was in Australia.

**Chris Gammell:** It was like across the globe, but it was like they basically created a smartphone brand for criminals. Yep. And somehow it worked. I mean, it's too long to explain, but that's enough to like start with. And it's pretty fun. Pretty fun to follow. So, you know, it's always nice when you don't feel bad for one side. You're like, oh, criminals. Oh, no. They got scammed.

**Dave Jones:** Basically, what they did is the Australian Federal Police... I assume it's Federal Police or whatever. Their cyber crimes department or whatever. In combination with the FBI or somebody. I don't know. Maybe... Dave's really selling it here.

**Chris Gammell:** Really selling it. Yeah.

**Dave Jones:** They created, yeah, a smartphone and they sold it. Was it called the ANOM? Right? Yeah, that's right. And they advertised this thing via a dummy company or whatever as being like a secure smartphone so that nobody could track you. Right? So all the... And then they ceded it to the criminals. Right? And they got one key criminal to use it. And then he recommended it to all his criminal buddies. Right? And it spread.

**Chris Gammell:** Yeah. They actually say criminal influencer. They use that term. Criminal influencer. Yes. Fantastic. Just fantastic. That's great. That's great. Yeah.

**Dave Jones:** Criminal influencer. Yes, it was the Australian Federal Police. Yeah. Right. Yeah.

**Chris Gammell:** I do think it'll be a movie someday. This is not a new story either. I found this later. I think it was... Yeah, yeah. Two months ago or something like that.

**Dave Jones:** This happened in June. It actually happened in June.

**Chris Gammell:** If you read, it's really worth the read. It's a lot of fun.

**Dave Jones:** And they actually made 800... They actually arrested 800 people who actually were using these phones. Yeah. And they seized like 148 million bucks in cash from all these criminals.

**Chris Gammell:** I think what it really comes down to is like when you think you're on a secure platform, right? Once you've like validated, you go through all these steps.

**Dave Jones:** Once you trust it. Yeah. Yeah.

**Chris Gammell:** And then you're like, all right, I'll just say whatever. You know? And it's like, oh yeah. Exactly. I would do the exact same thing. And that's what they did. Yeah.

**Dave Jones:** But what would you... It'd be so tempting not to tell... Just to keep it going, right? To see how far...

**Chris Gammell:** And then maybe pick them... Yeah, they say in the article that they know about someone who's going to be killed. And they have to go and surreptitiously prevent that person from being killed, but not give away the whole farm saying that like... Not give away the whole farm. We know exactly what you've been saying here, guys. Yeah, exactly. Yeah. Like I said, this is totally going to be a movie someday. You know, this is like... Oh yeah, I know. It's great. Like the old mob movies and stuff like that. Like, I love that era of like, you know, there's always a sting. Someone's always wearing a wire.

**Dave Jones:** Yeah. Yeah, exactly. And they made this secure fund and a criminal influencer. Just spread it to his criminal buddies. Yeah. Yeah.

**Chris Gammell:** You too could be a criminal influencer someday. Yeah.

**Dave Jones:** Just go on. It'd be tempting just to pick them off one by one. And then, you know, and then so that they slow, you know, like it takes them years to figure out, oh shit, they're listening to the phone. You know?

**Chris Gammell:** I mean, it's almost the same story in like, if you look at like the code breaking happening in World War II. Like they had to like... Right. Yeah. They seeded like bad messages then too, right? They had to like... Yep. Yes.

**Dave Jones:** Yes. Exactly. They couldn't just stop everything. They actually had to let some things happen, which ended up, you know, their own people were killed. You know, their own soldiers were killed. And they could have stopped it, but they didn't want to give it away. Yeah. Because it was such a big thing.

**Chris Gammell:** I've gotten most of my knowledge from it, from Cryptonomicon, which is like fiction. It's like, you know, historical fiction, but very good.

**Speaker ?:** Oh, okay.

**Chris Gammell:** All right. Neil Stevenson book. Right. And yeah.

**Dave Jones:** Oh yeah. They decrypted like half of their traffic or something. And they knew a ton of stuff like years before, you know, and yeah. So they had just had to let things happen, unfortunately, which meant, you know, they didn't inform certain generals or whatever that they had this information that, oh yeah, they're going to get ambushed or whatever, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** It's like, yeah, they just, because there was more, there was more at stake. Like there was like the whole war at stake.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** So they, yeah, they couldn't actually tip their hat.

**Chris Gammell:** I, uh, I just finished reading or listening to, uh, Thunder Below, uh, which is about World War II subs in the Pacific. And they also cover it in there. They talk about like, uh, having, uh, that one is great. I heard about that from, so Destin from Smarter Every Day did that like seven series on nuclear subs and he recommended it at the end of one of those. Yeah. That was great. Then I talked to former guest Josh from CryptoProtronics and he mentioned that like that book is like revered, he's a former subariner himself. He said the book is like revered in like in the U S Navy still. And it was like written in the fifties or sixties. It's, it's really fun to listen to. Not least of all, because the audio book reader guy, every time there's a depth charge, he goes, boom, a lot of, a lot of fun to listen to. That's great. I like it. I like it. Very cool.

**Dave Jones:** Uh, yep.

**Chris Gammell:** Anyway, my dad doesn't listen to the show, but he, if he was listening, he would find out he's getting that book for Christmas. Oh, okay. Right. Yep. And see now I've seated him. And now if, if he was like, I don't want to put that book for Christmas, if I talk to him at like Thanksgiving, I'd be like, aha, see now my, I know my, my channel of communication is not secure.

**Dave Jones:** Right. That's it. Damn. This. Yeah. Publicly available. That's right. That's right. Yeah. That's right. Yeah.

**Chris Gammell:** Encrypt your messages, folks. It's important. Yep.

**Dave Jones:** Like it's probably once a week that I'd like come home, you know, to the, um, it's a ZV blog and they go, Oh, you know, do you hear her, you know, talking about the day or whatever. And, Oh, do you hear about this or whatever? And she goes, no. And I usually always go, well, you would, if you followed my Twitter feed, you know, and she just rolls her eyes. And like, so like every week she cops that, you know, you would, if you followed my Twitter feed, you know, all about it. Yeah.

**Chris Gammell:** She doesn't talk about at home then. You know, I guess you did.

**Dave Jones:** Exactly. She doesn't watch my video. She doesn't follow me on Twitter. She doesn't listen to the amp hour. Sorry, dude.

**Chris Gammell:** She might not even listen to you at home. Who knows, man?

**Dave Jones:** No, no, exactly. Well, apparently I'm the one who doesn't listen to her.

**Chris Gammell:** Well, you know, that's how it goes. That's how it goes.

**Dave Jones:** That's it. Catch you next time.

**Chris Gammell:** Yeah.

**Dave Jones:** See ya.

**Chris Gammell:** It's been fun.
