---
episode: 24
title: Solar Cells, SparkFun, TSMC - The Detroit Debunking
url: https://theamphour.com/the-amp-hour-24-the-detroit-debunking/
---

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life. Hey Chris, how are you doing? Good Dave, Happy New Year.

**Dave Jones:** Yes, you too and all of our audience, Happy New Year.

**Chris Gammell:** Yeah, so it feels like last year.

**Dave Jones:** Yeah, how long have we been doing the show now? In terms of, it'll be 20, what's this show, 24? So it's 24 weeks, almost half a year.

**Chris Gammell:** Yeah, wow, that's crazy.

**Dave Jones:** That is insane. You're only five minutes late today, I see. So if we round down, then you're actually on time.

**Chris Gammell:** Well, go me. I must have turned a corner in the new year.

**Dave Jones:** Awesome, New Year's resolution, huh?

**Chris Gammell:** There we go, yeah.

**Dave Jones:** Yep, turn up on time for the Amp Hour. But granted, you do have to drive home for work, whereas I'm just sitting here lazily eating my breakfast. So it's pretty easy for me.

**Chris Gammell:** Yeah.

**Dave Jones:** But that's an interesting question. Should we round up or round down? Because you should snack on the five. If you're on the four, I was going to say, well, we could round down. But yeah, I don't know.

**Chris Gammell:** I might have to count it against me this time. Sorry. I'll try harder next time.

**Dave Jones:** Well, someone on the forum, my recent LCR meter review, somebody talked about that. They noticed. I didn't. I don't think I noticed it at the time, but I'm going to have to go back and check the video. But they noticed that the LCR meter display wasn't rounding correctly because when you hook it up to the PC, it extracts extra digits out of the thing. But it can only display five digits. It can only display a count up to 40,000. And he noticed. I'm not sure if he's correct or not. I've got to check. But he said it was rounding it wrong or something. So, he wasn't quite sure what was going on there. So, that's an interesting question. If your instrument can measure more than it's actually displaying, then, yeah, how do you round it? I guess you use the typical five, right? And go up and go down on the lower side of the phone.

**Chris Gammell:** Yeah, unless you're doing like a ceiling and floor kind of thing because isn't ceiling where it's like anything above zero, it goes to the next digit up?

**Dave Jones:** It goes to the next digit, exactly. So, maybe that's the algorithm they're putting in place. That'd be weird, though.

**Chris Gammell:** I wouldn't do that for an LCR meter.

**Dave Jones:** No, I wouldn't either. I would just do your traditional, you know, five you round up and four you round down. And that's... Yeah. I'm sure there's a name for that. Is there an official name for that kind of rounding? Half rounding or something? I don't know. I would just call it rounding. I just made it up. Yeah.

**Chris Gammell:** Yeah, I don't know. I'm sure there is a name for it. I mean, maybe they just don't care about those last digits. Maybe it's just all noise anyways.

**Dave Jones:** Right. Well, that's the thing. This was brought up on the forum by this person. He said, because this meter, when you hook it up to the PC, it can extract a whole bunch of digits. It can extract an extra two or three digits out of the thing. What use are those digits... You know, let's say you've got a six-digit meter. What use are those six digits, having them on the display, if your meter's only accurate, to three digits, for example? Why have the extra three digits? And it's a good question.

**Chris Gammell:** If I had to guess, I'd probably guess it was like a single precision kind of thing. Like if it has a single floating point precision internally, and then when it does a conversion, it just says, hey, I have these digits. But it doesn't mean the hardware necessarily supports it.

**Dave Jones:** Not necessarily, that's true. But multimeters are a classic example of this. When you get a very high precision bench meter, it might be, say, plus minus 100 counts or something like that. So why have those extra two digits? Well, the answer is the difference between accuracy and resolution. Resolution is useful even if your accuracy is totally crap. You can have a 10% accurate meter, but you can have a six-digit resolution, and that can be useful for getting comparative relative measurements between one component and another component, for example. So those digits are actually useful, even if the accuracy is totally pointless, because its accuracy is three or four digits above that or something. So yeah, that's the answer to the forum question anyway. Resolution, those extra digits can come in useful.

**Chris Gammell:** If only we had some kind of time measuring mechanism so we could round up or down.

**Speaker ?:** Right.

**Dave Jones:** Anyway, I've done a video on that, talking about counts and all that sort of stuff and plus minus counts on meters and things like that. So yeah. What have we got on today's show? That was the first item. That was way down the line. I just added that like five minutes before we started.

**Chris Gammell:** Jump of the gun. Yes. You just wanted to talk about your review, didn't you? Well, I did. I did. It was a good review. I liked it. I liked it.

**Dave Jones:** Thank you. Oh, they're getting too long. I mean, what do people think about 30-minute product reviews? People are obviously watching them. I've already had like 3,000 people watch it, and that doesn't include the podcast people. So people are actually watching these half-hour reviews.

**Chris Gammell:** Well, I don't know. Can you tell if people are actually shutting it off early? That would be the real measure, right?

**Dave Jones:** You can tell their attention span. I haven't really gone in and analyzed that as much.

**Chris Gammell:** That might be worth doing then.

**Dave Jones:** Yeah, it might be worth going in, but people are certainly starting it, and they know it's 35 minutes long. It tells you up front, you know, that it's how long it is. So people are watching, but I don't know. I just can't seem to do a bloody review under half an hour these days. It's crazy.

**Chris Gammell:** It's that off-the-cuffness. Yes. That's the problem. That's the problem, yeah. Yeah.

**Dave Jones:** And I just like to be wordy. My style is a conversational style. Right, right. So I guess, what can you do? Oh, well.

**Chris Gammell:** Yeah. So let's see. To start out, we got a shout-out to SparkFun.

**Dave Jones:** SparkFun, yes.

**Chris Gammell:** Innovative new idea known as pick the junk up off the trash bin and sell it to people.

**Dave Jones:** It's a pick-and-place grab bag is what it is, basically. And it's awesome. I love it. I know.

**Chris Gammell:** It's so great. I mean, I don't really know all the range of the parts that they're using. I don't think they use any, like, high-precision parts or anything like that, but, I mean, they use enough parts that are, you know, you're probably getting some op amps and you're some transistors in there and everything, so why not? And if people don't know what we're talking about, basically, a pick-and-place machine might have, you know, like, the suction when it picks up a part and tries to put it, place it on a board, it might fall off, or, you know, maybe it just rejects the part before it even tries to do that. All that stuff goes into just a bin where the rejects go. And that's what they sell you. They sell you a bag of that stuff for 10 bucks, so pretty cool. I bet they'll sell out of those, to be honest.

**Dave Jones:** Oh, yeah, absolutely. People will grab those, no pun intended. And, yeah, and these, if you don't know about these pick-and-place machines, you've typically got to, especially for the real cheap throwaway items like your resistors and your capacitors, you can't give your manufacturer a reel of 100 resistors and expect them to populate 100 boards because they're going to want some excess components, so when they wind the thing on, a few excess components will fall off. You know, it might be 10 or 20 or something like that. So you've actually got to provide excess components to them. And if you've got really expensive components that are, you know, if a chip is $100 a pop or something and you happen to have a reel of 1,000, well, you know, you don't want them to be wasting those particular chips, so you've got to tell them that they're actually, you know, expensive items. Please be very careful about how you reel them and put them on the machine and don't waste them kind of thing. So, yeah, but that's something you've got to watch out. And all these things end up in the grab bag.

**Chris Gammell:** It's cool. I like it.

**Dave Jones:** It's a bin of components. It just looks awesome.

**Chris Gammell:** There's this one. When I was looking through, I think we did an episode on here about where to find parts. I remember someone linked us through to this really, it was a ham page, and it's just this guy, I think he might be in Jersey or some, I'm not sure where he is, but it's just like his own little grab bag of, you know, he just mixes up components and sells them. And it's the same kind of thing, but his are even more, you know, his might have like through hole kind of components like big wound inductors and all that other kind of stuff. So, it can get crazy though.

**Dave Jones:** I always love grab bags. When I was a kid, you know, you go into Dick Smith or Jay Carr and you'd, you know, first you'd go straight for the grab bag bin. They used to have a big bin where they'd have, you know, smaller bags of these junk, you know, just excess components. And they were great. That was a great way to stock your lab. But I've still got, you know, tons of those components from, you know, 25, 30 years ago. I'm not sure how good they are now, but I've still got a lot of them. And yeah, it's just a great way to generically stock your components. I don't know how long you're going to have to spend sorting through them because to make them useful, you really got to sort them out. Right. And if you've got things like resistors, that's a trade-off, right? Yeah. And if you've got things like resistors and capacitors, especially the capacitors, which won't be marked, you know, you'd have to go through and individually measure each one. And well, that's more trouble than it's worth. You may as well just go out and, you know, buy them in strips from J-Car or from DigiKey or something like that.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** Especially with, yeah, yeah. They're tempting,

**Dave Jones:** but only if you've got a lot of free time and you just enjoy sorting through bags of components.

**Chris Gammell:** Especially, yeah. I mean, yeah. If you've got some good op amps in there and everything, I think that'd really be worth it.

**Dave Jones:** Oh, it'd be useful, yeah. And other components that you're marked, you know, if they're marked components, great. Not a problem. You know, you can sort them out pretty easy.

**Chris Gammell:** Yeah. Well, we like it's SparkFun. Keep it up. That's cool. Yeah. Let's see. What else we got? We got, so we had a suggestion for a rant. That's a new one. Oh, okay. Suggestion for a rant. Basically, it's from one of our listeners. Oh, I've lost who it is. I'm sorry. They're anonymous because they have to be in this case. J-Blogs. Yeah. Basically, he's been working on and off, wherever this was, and he wants to use, like, the IEEE kind of services that are out there and everything, and he can't because he doesn't have money for a membership now. So what the hell is he supposed to do? And because, you know, IEEE has some good resources for, you know, people looking for jobs. They post jobs all the time. And they didn't waive the fee, though, because he has to be making less than $13,000, I think, which is, which is...

**Dave Jones:** Yeah, his argument is that it costs more than $13,000 to actually live. Right. Yeah,

**Chris Gammell:** doubly so for where the majority of electronics people in the U.S. live, you know. Right. If you're in California. Oh, yeah,

**Dave Jones:** because you're going to be living in Silicon Valley or something, right? Right,

**Chris Gammell:** yeah. Yeah. $13,000 might... They might want to revise that number upward. That might be an old number. Right. But it's kind of ridiculous. They should have, like, some kind of...

**Dave Jones:** Discount for unemployed people. How do you prove you're unemployed, though?

**Chris Gammell:** Is there a... Well, you can... I mean, if you're in the U.S., you have to file for unemployment, so there's tons of paperwork for that stuff.

**Dave Jones:** That's... But that's only... Well, that's if you're getting unemployment benefits, but I've been unemployed before and I didn't claim unemployment benefits out of principle and all that sort of stuff. So, yeah. What are you doing that case? I guess you're screwed, right?

**Chris Gammell:** I don't know. Maybe a letter from a former employer or something?

**Dave Jones:** Right. Anyway, yeah, I reckon the IEEE, get on the case IEEE. I reckon you should have a very heavy discount for unemployed people. Yeah.

**Chris Gammell:** Yeah. Especially these times, you know, like, IEEE.

**Dave Jones:** But then again, if you're unemployed for like a month, do you jump in? Oh, quick, I'll jump in and renew my IEEE membership and then, bang, you get work again and then...

**Chris Gammell:** Well, you can do a month-to-month basis or something. I don't know. There's a lot of things you could do. I'm sure. Or even just open up certain things that people that are unemployed would need, right? You don't need... Oh, you don't need to necessarily be reading journals, but you might need access to the boards or, you know, other kinds of things like that, so...

**Dave Jones:** Yeah. In fact, they should probably give free access to engineers who are unemployed, especially if you're a previous member and you're now... You know, you've proven that you're in the industry, you're a previous member and now you happen to be unemployed and you're desperate for work, well, and your subscription expires, they should give you free continued access to the...

**Chris Gammell:** Yeah.

**Dave Jones:** To the jobs board, absolutely.

**Chris Gammell:** Yeah. Anyway, no. Hopefully they'll figure it out. I don't think they're listening. No, not listening. No, of course not. They would have, you know, blown their top already for the other things we've said about them. Right.

**Dave Jones:** Speaking of California, you've put here that California is getting rid of the old 100-watt light bulb.

**Chris Gammell:** Yeah, I saw that on Cree's Twitter page today. I had known about this because Germany had did it. Did it. They had outlawed 100-watt incandescents a while back.

**Dave Jones:** Well, that's the same here. We've had that for a long time now. I think at least a couple of years they banned sale of incandescent light bulbs here, which is just crazy.

**Chris Gammell:** I mean, there's no negative effects from that, right?

**Dave Jones:** Oh, well, the problem with it is that they went stupid and they did this complete blanket ban on all incandescent bulbs. You know, even when they're used in special niche applications. Like, you know, you need a light bulb that goes in your oven or something like that. It needs to be special high temperature bulb, right? You can't just put a compact fluoro in there. Yeah. It's crazy. Why does everything taste like mercury?

**Chris Gammell:** This is weird.

**Dave Jones:** Yeah, it was just, oh, yeah, there's just better ways to encourage people to move over to compact fluoro and other low energy light systems than to simply just flat out blanket ban the old ones. It's just, ah, it's, yeah, it's pointless, you know? People are just going to stock up on the old ones anyway, and they're just going to continue to use them out of protest rather than encourage people by, you know, just banning something doesn't, doesn't help in it. Yeah, I'm not sure if we talked

**Chris Gammell:** about it on here. The guy in Germany, though, that was, did we talk about that on here? The guy in Germany that was selling 100 watt heaters, he got them reclassified, he got 100 watt light bulbs reclassified as heaters.

**Dave Jones:** Oh, fantastic.

**Chris Gammell:** Yeah. They just happen to output light, and I mean, if you've ever put your hand over a 100 watt light bulb before, it's pretty, you know, bloody hot. That's the basis for an easy bake oven, right? Absolutely. Very clever. So, I wonder if that's going to, maybe that'll happen in California now, but.

**Dave Jones:** Yeah, people, you'll find the same, have they actually banned them? What is the?

**Chris Gammell:** They banned the 100 watt, not lower wattage bulbs, though. Right, okay. And then the rest of the US is going next year, so.

**Dave Jones:** Right. No, they'll just find, same thing here, people will just stock up on them, and yeah.

**Chris Gammell:** Yeah. Anyway. You got like a closet full of them at home, Dave? Is that, are you admitting this on air?

**Dave Jones:** No, I'm not a closet, incandescent fan. No, I switched over to compact flueros totally, years ago. Yeah,

**Chris Gammell:** last year for Christmas, that's what I asked for. Oh, really? Yeah,

**Dave Jones:** oh, at least half a decade ago, I switched, no, more than that, God, seven, eight years ago, I switched over to compact flueros.

**Chris Gammell:** Nice, nice.

**Dave Jones:** Haven't, haven't looked back.

**Chris Gammell:** Yeah, that's good, that's really good. Well, that's good because you're not throwing stuff out too. I mean, less, I mean, I guess the CFLs have problems with throwing stuff out. Yeah, well,

**Dave Jones:** yeah, I was going to do a blog on that. CFLs are notoriously unreliable. The components in them, just the way they run them and they overstress them and they don't survive in heat, these things, yeah, they advertise them as 10,000 hours life on the box or whatever, but what they don't tell you is that is in free air standing at room temperature with airflow. If you put these compact flueros in an enclosed enclosure with no airflow, they will die extremely quickly, you know, a thousand hours, hundreds of hours, something like that. So, they're very susceptible to high temperature. So, just be careful.

**Chris Gammell:** Yeah, you know, I've looked at the block diagram too before because, I mean, you actually have to, for the flueros, you have to like step up the voltage, don't you? I mean, they actually have like a step up transformer inside, correct?

**Dave Jones:** To actually arc them over, yes.

**Chris Gammell:** Right. Yeah, so, I mean, like if people out there have never looked at the block diagram, I'll try and post a link to it, but, you know, it's a pretty standard step up transformer inside of it when then they have to, and I think there's some kind of, there's an LC tank in there, I'm trying to find it right now, but the, you know, it's, these kind of components are, these are normal electronic components, not just a wire, like a tungsten wire, like an incandescent is, so, there's a lot more going on in there and that's, a lot of the failure mechanisms come from those actual components failing, as opposed to the, you know, the, there's no filament to burn out, it's not like the, the gas is escaping the tube, it's just, the, the thing that strikes the, the plasma isn't, isn't there, so.

**Dave Jones:** And then of course the, once they became, because they're quite an expensive item, back when they first came out, you know, you pay 15 bucks for one of these compact fluoro bulbs, and that's when the one hung low factory swung into action, and thought, aha, we'll, we'll get some of this, we'll get some of this market action, and. Right. All these poor quality CFLs came out, and they would literally disintegrate in your hand, they were. Really? Physically just crap, oh yeah, you go to screw them in, and they wouldn't even survive being screwed in, they would just shatter, and oh, just really horrible physical quality as well. Yeah. And.

**Chris Gammell:** I've noticed that when I've cracked one open before, you know, you look at the, the actual components, and it's like the cheap bakelite kind of looking boards. Oh yeah. You know, really junky looking caps, and. Yeah. But that's how we get them for $3, and that's what we demand, so.

**Dave Jones:** Exactly. Yeah. Market's got itself to blame, I guess. Yeah. And then the other, there's the other interesting concept, where these bulbs flicker. Have you ever had that? Your switch is turned off, but you're, like every five minutes or something, your bulb might just go flick, and it flicks on for half a second. A little, a little tiny flash. You can notice it at, at, at night.

**Chris Gammell:** No, I've never seen that.

**Dave Jones:** No. Okay. Well, it doesn't happen to everyone. It's only due to specific home installations, and what it is, is the capacitance in the wiring, okay, is enough to leak some charge, and actually charge up the CFL bulb, even though the switch is off, okay, the capacitance, the wiring, capacitance wiring in your roof, is, couples through to the CFL bulb, charges it up, until it gets enough energy to go flash, and then it arcs on for, you know, half a second or something like that, and then switches off, and then charges up again. So, you might find these bulbs actually flicker, at a rate of once every minute, or once every 10 minutes, or something like that. So, yeah, it's a very, very obscure kind of problem.

**Chris Gammell:** That is kind of, yeah. And that's not just for higher voltage, like 240, like, like Australia?

**Dave Jones:** Oh, no, I don't think so. I think it happens in the US as well. So, it's all due, it's due to the capacitance of the wiring. So, yeah, I'm not sure, if there's any difference in 110, but, yeah, it certainly does happen. And, but it is a bulb specific as well, only some, certain bulbs are susceptible to it, and certain house wirings, but you put the combination together, and, yeah, you have all these reports of these lights, mysteriously flickering in the middle of the night, even though they switched off. And, and people think their house is possessed, and they call in, you know, they call in the Ghostbusters. Yeah. Uh, yes.

**Chris Gammell:** I wonder how many times capacitance has been, has been, uh, blamed on ghosts, or ghosts, you know, other way around.

**Dave Jones:** Capacitance is highly underrated, I think, as a, as a phenomenon.

**Chris Gammell:** It's the specters, and the spooks.

**Dave Jones:** Everything has capacitance, so. Yes.

**Chris Gammell:** Yeah. Ah, indeed. So, I wanted to mention the, the throwing out of the CFLs, because there's been a, there's been like a, I don't know, you kind of, kind of see trends about stuff, and, and I've been seeing more trends just about, like, electronic waste. I, you know, I saw there's an E Times article, I heard an NPR story, all this kind of other stuff, and just kind of how it's, and, and you heard it like a couple years ago, too, about, you know, these huge junkyards in other countries, in China, and Africa. Oh, yeah. where all this stuff ends up, but it's kind of resurging again, you know, it's a, it's a topic that keeps going on, and someone was even talking about it on the EV blog forum, so, I thought it was interesting just to see, what's going on in the regulation market, because that, that affects people doing electronics directly with Rojas, and then, if people actually care about the, the implications of, having all this electronic junk laying around, because it's not good, it doesn't just, it doesn't just disintegrate, unlike those light bulbs.

**Dave Jones:** Those light bulbs are pretty simple, that, yeah, electronic components, they've got all sorts of nasty chemicals in them, that's what ROHS, everyone thinks ROHS is, or ROS compliance is just about lead, but it's not, it's about all these other, you know, I think there's five or six different chemicals, that actually, it actually controls, so, yeah, and,

**Chris Gammell:** and they pop it up every year, too, I mean, they keep adding more things to the, to the list basically, because,

**Dave Jones:** to the list of stuff, yeah, exactly, that reminds me, the story of, have you heard about the story of stuff?

**Chris Gammell:** The story of stuff, is this a bedtime story, or what kind of story are we talking about here?

**Dave Jones:** it's a video, it's an online video, done by this chick, formerly from Greenpeace, I think, don't quote me on that, and, she does these really interesting videos, not always 100% correct, very, quite sensationalized, but they're excellent, cartoon type videos, exposing, stuff like this, and, and the latest one, that's just come out, I've been waiting six months to see it, they've been hyping it for like six months, and it talks about, exactly this, what do you do with your electronics waste, you know, where does it go, how does it, and, oh, well, I'll have to post the video, and, it's incredibly popular, and these things, her videos get millions of views, you know, they just go viral, every time she brings out a new one, and, and they're fascinating, so we'll definitely link to that, the story of stuff,

**Chris Gammell:** storyofstuff.com, I just found it,

**Dave Jones:** storyofstuff, is it .com, yep, yes,

**Chris Gammell:** .com, yep, storyofstuff.com, storyofelectronics.org, and that's a new one too, and maybe that's the reason, this is coming up again,

**Dave Jones:** that is the new one, I didn't know they had a dedicated, address for it, but, yep, that's the one, that's a video, it's well worth watching, I haven't, sort of gone through, and, once again, they don't just do the video, they provide references, to everything they, they say in the video, so,

**Chris Gammell:** unlike us,

**Dave Jones:** unlike us, we just, yeah, we just bullshit away, yeah, oops,

**Chris Gammell:** I know the, the interesting thing I was listening to, on NPR about that, was just how, the way they get like the gold out, and all the, the precious metals out of it, is not by like, I always kind of envision like, breaking apart boards, trying to like actually pull off traces, no, they just, they just light that crap on fire, I mean like,

**Dave Jones:** they just burn the whole damn lot,

**Chris Gammell:** that is not a good idea, that stuff is nasty, nasty stuff,

**Dave Jones:** well it's fine in China, isn't it, no one cares about China, or, or India, or wherever else they're doing it, I'm being sarcastic by the way, I'm holding up the, oh okay, okay, right, yeah, but that's, that's what these, that's what the story of stuff video, talks about, in several of the videos, is that, you know, because we don't have the problem here, we ship everything, all of our waste, overseas, and, yeah, all of your recycled stuff, all your recycled electronics, you think you're doing good, it goes overseas, to be, you know, burnt in somebody's village, over there, you know, and they're the ones, who get polluted, and get cancer, and everything else, it's just, yeah, I know, well another question,

**Chris Gammell:** that comes up too, is like, you know, we talk about, some of us, not to bring up, a sore topic, talk about printable electronics, but there's even, but just to, bypass that subject completely, but, you know, like, like biodegradable type electronics, you know, if you do have, a printable, like even a printed circuit board, right, we do that with etching, etching right now, but if you start getting, other conductive materials, that you can put down, on a PCB, that maybe is, you know, not as speed sensitive, as the fastest things, but, you know, you just need to run, on the mill board, maybe you can start making, those biodegradable, kind of materials,

**Dave Jones:** yeah, possibly, I don't know about, biodegradable, but certainly, not as harmful, you can definitely do that, because, like all the major, you know, Dell, and your Hewlett Packards, and all those, sort of companies there, and Apple, with their iPhone, now everything, they're very, they're even advertising, that all their products, are designed with, you know, 30% recycled plastics, and they're designed, not to be hazardous, and for when you dispose of them, and all that sort of stuff, and yeah, I mean, yeah, things are definitely happening there, I don't know, that'll get to a point, where electronics is going to be, biodegradable, I don't think that's possible, but, well,

**Chris Gammell:** there's a, I mean, there's a, there's a new, in this article, I'll link through from EE Times, there's one from ST Micro, and then, this group out of Switzerland, called DeBiotech, and they're working on it, basically, that's the kind of thing, that they're working on, so, I think we're still in the very early, research stage, but, it is a possibility, at least, I don't know, about economic viability, which is much, Well,

**Dave Jones:** your board might biodegrade, but I don't know about your chips, and everything else, so,

**Chris Gammell:** Oh, right, yeah,

**Dave Jones:** yeah, you know, there's lots of components in there, that just, you know, your physical connectors, and your, and your mounting, well, no, your mounting hardware, and all that, you could, I guess, you could, you know, mounting hardware can be made out of, uh, biodegradable material, I guess, stuff like that, maybe, shells for connectors, I don't know, but, yeah, there's a limit to how much you can do there, but, everything helps, so, that's, uh, good research,

**Chris Gammell:** yeah,

**Dave Jones:** well worthwhile,

**Chris Gammell:** I don't know, I saw another article about the,

**Chris Gammell:** I've seen a couple articles, if you couldn't tell, right,

**Dave Jones:** yeah, you love reading articles, we know,

**Chris Gammell:** yeah, so, I saw another one about, how, it was from, it was a weird source, it was from the Omaha Times, I don't remember where I saw it from, right, uh, Omaha Times, or something like that, but just talking about all the different things that, that microchips are in these days, and it kind of seemed like, uh, you know, a lot of people who listen to this are very well versed in electronics, right, but, this seemed like more of a, a lay person's explanation of where microchips are going, and why they're in different things, and it kind of struck me as, you know, they're talking about, oh, well, there's microchips in everything, and that's because they all need these things, and it struck me as, no, there's kind of microchips in everything, because they don't know what else to do with them, and they're really cheap, like, I don't know, you look,

**Dave Jones:** they add functionality though, they add smart functionality, which is, you know,

**Chris Gammell:** which is important, the application software adds functionality, right, having a chip in there by itself, I don't know, I, I mean, yes, you're right, that it does add the potential for functionality, yeah, but like, if you just put a microchip in something, and then you write some two-bit program, there's no, I mean, who cares, right, put a switch on there, some of these things,

**Dave Jones:** you can make it smart, so instead of, you know, if you've got a little kid's toy, that flashes an LED, right, instead of having a, a simple, you know, transistor circuit, that just flashes it, on and off, if you put a, a 10 cent micro in there, then you can do all sorts of funny patterns with it, you know, it's one of those, yeah, I know, but I'm saying, once you start putting an intelligent device in, you do change the game a bit, so,

**Chris Gammell:** you do, but what's, what's the point of that, I guess, maybe that's not my, question to ask, I mean, we're talking about putting like, microchips in tombstones, you know, it's like, really? Oh, well, yeah,

**Dave Jones:** it's, I don't know, why not, I kind of think that'd be fun, imagine my tombstone, have a video screen up there, and it just keeps replaying, replaying the blog, I mean,

**Chris Gammell:** do we have to go visit grandpa, he's really loud, and he talks funny,

**Dave Jones:** and,

**Chris Gammell:** oh yeah, yeah, well, I mean, I'm guessing, you wouldn't, do you sound funny for an Australian, I don't know, I mean,

**Dave Jones:** oh, not, yeah, I kind of do, I guess, yeah, I, well, not as funny as some, it's like, I'm probably, I guess, deemed fairly normal, I guess, compared to, some more ochre, accents, ochre's the word, right, yes, hmm, yeah, ochre, yeah, like, stereotypically, more stereotypically Australian, accent, like, yeah, yeah, good day, mate, yeah, how you doing, mate, wow, something, yeah, like, something really, exaggerated like that, let's not do that again, I'm not that bad,

**Chris Gammell:** let's not do that again,

**Speaker ?:** right,

**Dave Jones:** that was a bit, that, did I actually peak there, let's just, no, I didn't, I didn't peak,

**Chris Gammell:** it peaked my interest in, cancelling the amp hour,

**Speaker ?:** right,

**Dave Jones:** but I guess it needs some, high pass, some low pass filter in there, so,

**Chris Gammell:** oh my goodness,

**Dave Jones:** I guess you got the same in the US, you know, yeah,

**Chris Gammell:** you're right, you're right,

**Dave Jones:** you know, some of those southern accents are a bit,

**Chris Gammell:** yeah, oh, speaking of the south, oh, segue, I was just waiting, let Dave go until we find a segue, so, TSMC, they announced today, they're building a plant in Mississippi, they're building a solar cell plant, my bad, they're building a solar cell plant in Mississippi,

**Dave Jones:** well, they've, kind of missed the boat, haven't they, China's got the market sewn up,

**Chris Gammell:** right, here's the thing that's killer about that though, this is basically the equivalent, in my opinion, of like, Honda, or Toyota, right, Honda and Toyota are brilliant Japanese companies, some would say otherwise, because of Toyota's recent problems, but they, you know, I'm still giving them the benefit of that, I mean, like their production system and everything, everybody knows that, right, but then they, they basically come over to the US, and they build large scale manufacturing type things like cars, cars, trucks, whatever, because it's much better to build it here, you know, lose some of the local, you know, if they're building it in Japan, obviously they'd pay for labor and everything like that, and support the economy there, but instead support the economy here, build up a brand name based on that, and not have to ship cars all over the place, because you have a local manufacturing force, and so now this is equivalent in solar cells.

**Dave Jones:** Right, because they're getting so high, and they're actually quite big, you know, you get these huge, you know, panels you're putting on your roof to power your house, they are physically huge.

**Chris Gammell:** And heavy, I mean, like shipping on that would be, Oh,

**Dave Jones:** absolutely.

**Chris Gammell:** Yeah, so, I mean, this is a big, I think it's a big deal, I mean, I don't, I mean, it's not as good as say, a research and development team, being in the US, and, and, you know, then, building a fab here, and doing that kind of thing, but at the same time, it's better than nothing. Oh, of course,

**Dave Jones:** I agree, it's a big thing. I guess you could claim it's a problem, because it's not an American owned company. It's the same here in Australia, you know, somebody comes and opens a plant here, great, but it's not Australian owned, you know,

**Chris Gammell:** right,

**Dave Jones:** so the profits go back overseas, but anyway, yeah, everything helps.

**Chris Gammell:** Right, and I think the thing that really struck me about it is, I don't think, I mean, I think the US is far off from this point I'm talking about, but, you know, or rather the, the large scale manufacturing in a different country, because of shipping costs, and all those other, those other things they describe, that's one thing, but I think because Mississippi is so low income, and, and needs this kind of investment, I think it's even close enough to the point where if China's, you know, if they ever flow to their currency, which is a different issue, but even as wages continue to rise, and Mississippis are so depressed because of the economy there, like, it's starting to reach an inflection point where companies are looking at this and saying, well, maybe, maybe it'll be equivalent eventually, and that's just another thing that adds into it, you know, like, that the US now, might now have low cost manufacturing.

**Dave Jones:** Right.

**Chris Gammell:** Which would be crazy.

**Dave Jones:** It, it would. Well, you can do certain things locally, yeah, it, there becomes a point where it's more economical to manufacture locally, because of all the shipping costs and everything you've mentioned, you know, that overcomes the cost of the shipping and everything else, and all the other issues, issues, so, yeah, who can bend over the furthest? Oops. And take one for the team, you know?

**Chris Gammell:** Yeah. Oh, boy. Yeah. But it's all good. Yeah, so, that's, that's good news, that's, I mean, that's obviously the US news. But,

**Dave Jones:** that wouldn't strike me, as the, well, there are other states which are struggling more, aren't they?

**Chris Gammell:** Oh, I don't know, man, deep south?

**Dave Jones:** Well, there's Detroit, which is destitute, right?

**Chris Gammell:** Right,

**Dave Jones:** yeah, they're, yeah, but I think they have, practically on the verge of, you know, riding in the streets, aren't they, or something? I don't think that's, if there's any people left.

**Chris Gammell:** Why, why not just go further, Dave? I think they're all zombies by now, right? Right, I don't know where you're getting your info. I mean, Detroit's not great, but, no,

**Dave Jones:** it's great. I saw a great, a doco, the Requiem for Detroit. If you haven't watched it, watch it. It's awesome. They reckon that they're, that they're so, like, everything is so, it hits, so rock bottom, you know, nobody's got a job, the whole, all the industries have moved out, that there's nothing left, except they're going to move back to farming. They're actually, all the residents are setting up these little individual farms, they're turning the streets back into farms, or something, and they reckon within 10 years, it'll be a farming city, rather than manufacturing cars, which I think is brilliant. That's pretty cool. Absolutely brilliant. Good on them.

**Chris Gammell:** I know, I've read some stuff about them recently, too, and actually, it's worth noting, too, that Maker Faire is up in Detroit again this year. Excellent. So I'm going to try and get up to that, though. Yeah. Because, you know, they still do have a very strong car automotive base there. Really?

**Dave Jones:** I thought it was dead.

**Chris Gammell:** No, I mean, it's hurting, but it's not dead. Right. I mean, and the design portion, too. I mean, so there's Kettering University up there, and there's, you know, U of M's nearby, and there's a lot of, there's a lot of resources up there. So, I wouldn't write them out completely, but like you said, with the land use up there, that's a big deal. So, that's, yeah, it's an interesting program they're trying up there. I don't know if it's going to work, and I think Flint is actually a bigger one, where they have.

**Dave Jones:** Oh, Flint, yeah, yes.

**Chris Gammell:** Yeah, yeah. So it's, it's interesting, but we'll, we'll link through the Requiem for Detroit, too, and the Maker Faire Detroit, because they could, they got a lot of, they got like a lot of hackerspaces up there. I mean, like, like in terms of like interest in the area, I think there's a lot of interest, and I, when comparing to like Mississippi, I don't think those two compare, really, because there's still a lot of high tech, like, base, it's not as strong as it was, but there's, you know, it just in terms of like, the institutions that are there, I think that's a lot stronger, so. Okay. And, and another thing that can't be written off, is union labor, too. I don't think they'd want to go to Michigan. Right, okay. If you're making solar cells, I think you want to be making them in non-union states. Right. That's, that's just a guess. I, I don't know if they talk about that in the article, but that's just a guess.

**Dave Jones:** I'm sure it's factored in, yes. Yeah, yeah.

**Chris Gammell:** But, way to go, Mississippi. Mississippi.

**Dave Jones:** Absolutely, Mississippi. Oh,

**Chris Gammell:** dear.

**Dave Jones:** How do you spell it?

**Chris Gammell:** M-I-S-S-I-S-S-I-P-P-I.

**Dave Jones:** I think every U.S. kid's taught that in school, aren't they? They are. Yeah, they are. How to spell Mississippi? Yep. Oh, God, I can't even say it. Yeah. But, that's an interesting question. Do cities like that, cities and states like that, which are really struggling, and I know there's lots of them in the U.S. and other countries for that matter, do they actually hit a point where, you know, it becomes so attractive for foreign investment or other companies to actually move their stuff there, you know, because it, yeah, because they've still got the labor force, people out of work, they're desperate to work, they want to work, and, and the states will no doubt offer them massive incentives to come in and build their big plants, and, you know, next thing we know, we'll be seeing an Intel, you know, a $10 billion Intel fab plant in, in Detroit or Mississippi or, something like that perhaps, I don't know.

**Chris Gammell:** Well, Intel did, I mean, they, they had that $8 billion announcement a couple months back.

**Speaker ?:** Oh,

**Chris Gammell:** right, what was that? They pledged, they pledged over the next couple of years to, invest $8 billion in the U.S. Right. I think that was Andy Grove, and, you know, he's, Andy Grove is very, very big into innovation and U.S. investment and education, all this other stuff. Oh, well,

**Dave Jones:** you wouldn't think so from their previous history. They've been setting up everywhere but the U.S. I guess he's had a change of heart now.

**Chris Gammell:** Yeah, I'm sure they're going to grow there too. I mean, like, the thing is there's talent everywhere. You know, there's a lot of talent. Yeah. And, and if you ignore that, you're even dumber than if, I mean, like, yeah, like if, if you think that like, you know, like nationalism in that regard is stupid, you know, like it'd be better to build, I mean, granted it's okay still to build somewhere and try and lure workers in. And, obviously that's been the model in the U.S. for the past, what, 60 years. Right. But, you know, it's, if you're ignoring that stuff, you're, and, and you're running a company, you probably shouldn't be running the company because there's a lot of talent out there. So, yeah.

**Dave Jones:** There you go. I just tweeted yesterday and nothing, total, total non-sequity here. Oh, okay. That, um, Goldman Sachs who own practically half of the U.S. and the U.S. government, but let's not get into that. Um, they just bought into Facebook now. Yeah. So, they, oh God, they got a finger in every pie. God, now they're into, they've bought part of Facebook because actually this is interesting. This is, this segues into, um, startup, tech startup companies actually, because the traditional startup thing, you always, the goal of any startup company was to go public, right? That was the sole goal of a startup company. Everyone becomes rich. Bang, you move on to the next, you know, startup. That was the sole goal. Now they reckon that the new thing is not to go public anymore. Like Facebook and other companies are now showing. They're trying to, um, they're trying to hold off on going public as long as humanly possible. And they're doing that by getting this, um, private funding by the likes of Goldman and Sachs. So that companies like Goldman and Sachs can sell private shares to their big business buddies. And then when they do, when they become so big, they have to go public. Then the big business people make the fortune instead of the, you know, somebody else. But anyway, that's the whole idea now is not to go public anymore. You can actually make your billion dollars or, you know, a hundred million dollars by having private funding. So it's a new model.

**Chris Gammell:** Whenever I look at that stuff and I, I see like, first off when I see software stuff like that, I, I know it's like the times that we live in and everything like that. But man, like 50 billion, that's just, it's unreal to me because like, yeah, it's software, you know, like, you know, we talk about hardware on this program and I try and like extrapolate in my mind, how would you do that in hardware? And to these days, I don't know. I don't want to sound pessimistic because it does sound pessimistic, but I don't know how you do it these days. I don't know how you start. Fab, I guess would be, you know, like unless, unless a certain person's predictions come true. Right. Right.

**Dave Jones:** Okay. Yes. But honestly, right.

**Chris Gammell:** I mean, like that might be a way of doing that,

**Dave Jones:** but yeah, I know software is everything because software adds the software adds the layer of, of functionality. functionality people, you know, that can give you a novel product or a novel idea or, you know, a novel website in, in this case of Facebook and right. Yeah. I mean, yeah, it's all about the software. It's all about the intelligence built into the product. Um, not so much the hardware itself. So, you know, you can still make a fairly big business out of some hardware, you know, some neat little hardware thing or something like that, but it's not going to be a Facebook, you know, I, right. Yeah. I don't think it's going to be that big. So I, I share your, uh, yes, your feelings there. Yeah. I can't,

**Chris Gammell:** I can't imagine. And, and I mean, as, as for the private investment thing, I mean, bootstrapping has always been the best method to, you know, to, on the path to riches, right? Of course. Yep. If you're going to start a company and you can use your own money or you can hold off and get some smaller investments, definitely do that because the more you hold onto the, the more control you have first off too. I mean, that's, that's definitely one thing that means that, the majority shareholder, if Mark Zuckerberg is the majority shareholder in Facebook, that means he gets to call the shots. And as soon as, as soon as they go public to get money and he's now down to like two or 5% shares of the shares rather than, yeah, sorry, sorry, buddy. Uh, if, if the public doesn't like it, doesn't like public, the, your privacy policy, then it's going to change or not the public, but your shareholders. Yep. So, so that's definitely a reason to bootstrap. I mean, I, I, I completely agree with that. I don't know about the private investment, that's, that's up to them. Yeah.

**Dave Jones:** And if people don't know about the term bootstrap, um, in this aspect, it, it basically means to, you know, start off with a small amount of, of money, which you can afford your own money. Don't typically don't borrow it and then make it, you know, sell a few items and then use that, use the profit on that to build more and then so forth and so forth. And you slowly build up with no investment capital at all. Yeah. So, yeah, that's how all smart businesses at the ground roots startup, you know, to, to come up with some, you know, whiz bang idea and go get venture capital somewhere. That's, you know, it's extremely high risk. All your eggs are in one, but you know, you know, the, the failure rate there is huge, but the failure rate for bootstrapping is very, very low.

**Chris Gammell:** right. And, and the other reason is because you're not going to put your money in unless you really believe in it too, right? If you know you have a good product and you're willing to work 20 hour days, you know, to get your idea working because, Hey, you just gave all your money to your business. Uh, yeah. I mean, of course you better make it work or else you're going to go back to doing something else. Yeah. You know, you know, you know exactly what's, you have all of the skin in the game in that case. So,

**Dave Jones:** yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** And it comes down to like, also we've mentioned before on here that you don't have to put in huge amounts of capital upfront, you know, you don't have to, you can just sell a simple product first. That's, that's not perfect, but it gets you bootstrapped. It gets you, you know, it gets you some income, which gets you profit. And then, you know, it's, you don't have to go out and spend a hundred thousand dollars to get a nice molded case for your product. Right. That's right. That, that can be money down the hole really when you can just put it in a square box and sell it and bootstrap it.

**Chris Gammell:** Do that revision six. Who cares about revision one? Yeah. Yeah. So since it's 2011 and since you've already gifted me one non sequitur, I wanted to gift one right back. How about, please? How about some, uh, some top 100 ridiculous claims for 2011?

**Speaker ?:** Oh, right.

**Dave Jones:** I, do we have to go through that list? Oh my God. Not the whole list.

**Speaker ?:** Top 100?

**Dave Jones:** Oh.

**Chris Gammell:** No, there's not. Well, there's, no, there's not that list. The other list. There's a list of, of trends in 2011. And there's a couple I wanted to highlight.

**Dave Jones:** A hundred things to watch in 2011.

**Chris Gammell:** A hundred things to watch. That's right. That's right. So number one on the list actually too, is 3d printing, which I think we've seen a little bit of that in the maker movement and everything else like that. Yep. Absolutely. So that's cool. Uh, micro businesses was another one. I don't know if you saw, saw that one. And this is all from a, a, a company called JWT and they do this list every year and, and they claim, Oh, so much success and yada, yada, yada. But micro businesses, I thought that one was kind of cool. Yep. That was a number 51. And that was, uh, basically having all the, all the means necessary to bootstrap yourself, you know, kind of, kind of relevant there. So they think that's going to increase as well. We'll see, we'll see about that one. Bamboo.

**Dave Jones:** Number seven is bamboo.

**Chris Gammell:** Seven. Oh, you're only at seven.

**Dave Jones:** I'm only, yeah, I'm sorry. I'm not scrolling through fast enough. Beer, beer is number 10. Oh,

**Chris Gammell:** I had some picked out so we'd have to scroll through. Right.

**Dave Jones:** Okay. Go for it. Sorry.

**Chris Gammell:** They mentioned near field. Cause Google's pushing that still a lot. That's, that's going to be, that's coming up. And then it's already big in Japan.

**Dave Jones:** Apparently I've heard everyone's mobile phones got near field and they buy their vents, you know, their stuff from vending machines by swiping their mobile phone or something. I don't know how true that is, but it's what I've heard.

**Chris Gammell:** I have confirmation of that too. So, right. Yeah. Yeah. Pretty, pretty cool. I mean, it's just, it's just a matter of the platform. Now if Google, if Google does it, yeah, you're probably going to do it. Right. I mean, like I know I will. Uh, and, uh, so that was another one they mentioned though, tap to pay. So they mentioned near field is like, you know, opening doors and all this other crap, but also tap to pay would be the thing you talked about. And then the last, and of the, of the hundred, we only, I only saw like four or five that I liked. So the number, the last one I had was self-powered devices. So energy harvesting and all that other kind of stuff,

**Dave Jones:** all that sort of stuff, which is, which can apply to, you know, very low powered stuff, watches, things like that. So,

**Chris Gammell:** right. Yeah. Yeah. And maybe even other things as, as sensors, you know, keep dropping. Yeah. Yeah.

**Dave Jones:** I like number 17. Somebody was thinking there, it's quite novel. Capture advertising.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** If you go into, like if you signed up for a website and ask you to, ask you to verify if you're human, it's called a capture and it puts up like a, an obfuscated bunch of letters. Well, instead of just putting up the letters, how about putting up an ad? So, yet more ways to make ad, ad, ad revenue. It's just, is there no end to,

**Chris Gammell:** and Alan Turing is rolling over in his grave. Yeah. To go from a test that tests it to, that, that checks if you're a robot or not to turning people into robots for brands. Yep. Pepsi. It's the one.

**Dave Jones:** Number 24, Detroit. There you go.

**Chris Gammell:** That might've been where I saw it before. Yeah. Right. Okay. There you go.

**Dave Jones:** What are they actually saying?

**Chris Gammell:** I don't remember. I didn't put it on the list, Dave.

**Dave Jones:** Well, they're, they're going to raise the city or something and consolidate the population, create new residential business areas.

**Chris Gammell:** They're talking about Flint in that one, I think really, because I mean, they talked about Detroit, but yeah. Yeah.

**Dave Jones:** Interesting.

**Chris Gammell:** Yeah. It's a cool list, but I mean, the tech centric things are just, we've seen some of them. We'll see if, I don't know, if near field really takes off. I don't know how much I, I mean, it's going to take a long time to roll out, you know?

**Dave Jones:** Yeah, it does, but it's eventually going to happen.

**Dave Jones:** it will,

**Chris Gammell:** it will, but you know, like, you know that Visa is going to be pissed, right? Or MasterCard. All those guys are going to be pissed if Google tries to do this. So. You betcha. And then they'll impede it. So, we'll see.

**Dave Jones:** Yeah. Yes, there'll be wars going on there.

**Dave Jones:** yeah. Anyway, that's,

**Chris Gammell:** go for it. Did you see the, the, the predictions that went Ari on, on IEEE with Kurzweil and IEEE?

**Dave Jones:** Yes, Ray, Ray, Ray Kurzweil. If you haven't seen it, we'll put up the link. He, I, I, IEEE wrote a savage in article, of him last month. It's not a cover. Basically saying, oh, he's a crock of shit. And none of his, none of his predictions come true. And he's just, you know, all this sort of stuff. So, he, he actually responded to them. He wrote a letter to the IEEE. No, is it? Yes, it's the IEEE.

**Chris Gammell:** Yeah, it's IEEE.

**Dave Jones:** Wrote a letter to the IEEE. And, yeah, pointing out errors in there. Yes. It was, it was quite funny.

**Chris Gammell:** I think you and I, Dave, I mean, some of the stuff Ray Kurzweil says is right. A lot of the other stuff is wrong. But, we should say enough things. God. We should say enough things that something's bound to be right. And then we'll just work on, you know, defending what we meant by all the things we said that were wrong.

**Dave Jones:** Of course. You can always come up with a clever defense. Yeah.

**Chris Gammell:** That's my plan for the printed, the printed chips, right?

**Dave Jones:** The chip making machine. Yep. Yeah. Yeah.

**Chris Gammell:** Well, what I really meant was it's possible, but it's not economically viable. No, no, if you go back, you'll find that, no, no,

**Dave Jones:** your original argument, you've modified your argument once you realize. No, that's what I'm saying.

**Chris Gammell:** You have to modify your original argument in order to,

**Dave Jones:** in order to massage it into the,

**Chris Gammell:** that's the game. That's the game here, Dave. What actually happened.

**Dave Jones:** Yeah. So, we need,

**Chris Gammell:** so, but if you make enough, it's just the law of large numbers, large numbers at that point. Something has to be right. And then you can just point to that one over and over again. Right. But I was right about near field communications or whatever else you say.

**Dave Jones:** Yep. Yeah. Oh, that's funny. Yeah. More, more predictions. Um, this is a bit, well, no, not, not,

**Speaker ?:** not,

**Dave Jones:** sorry, not, not predictions, but it's an old I triple E article. Um, some people have been tweeting it. Um, it's a couple of months old, um, but it's the top 25 chips of all time. And I love it. Um, I, I love, I love lists like this. And, um, I, I think you just love it because you're old.

**Chris Gammell:** That's why I know.

**Dave Jones:** Cause I'm old and I remember them. So,

**Speaker ?:** you know,

**Dave Jones:** it's great. Where is, Oh, where is it? Where is it? Top 25 chips of all time. I've got it open here somewhere.

**Chris Gammell:** There it is.

**Dave Jones:** Here we go. That shook the world. That shook the world. 25 microchips that shook the world. Um, yeah. Oh dear. And well, let's, let's go through them. And I guess, why not? Hi. Okay. It's electronics related. We're talking chips. And of course, they don't actually number them. I don't, they're not putting them in order. You'll have to excuse me if I don't know some of them. That's all right.

**Chris Gammell:** If I don't know some of them that, I mean, some of these are, you know, 12 years before I was born. So just, just, just, I'm just going to sit quietly by for some of them.

**Dave Jones:** Okay. Well, the first one, no surprise, the triple five timer or the NE, the, the Signetics NE triple five.

**Chris Gammell:** Wait, wait, wait. I thought it was 555, Dave.

**Dave Jones:** No, it's triple five. Sorry. Triple five. Triple five here in Australia. Or. Yep.

**Chris Gammell:** Triple five. What was, what was the last one? There was one more.

**Dave Jones:** the 555 is fine, but it wasn't five, or no, or the 555. Um, you know, the 555 timer. Yeah. Um, but no, the 555, it's definitely not the 555. 555. No, no, sorry. Ah, and they, and they've got a whole story behind each one, which is great. You've got to read this list. It's awesome. We'll put it up. And, um, so yeah, no surprise, triple five, bow. We are not worthy. Uh, and, uh, yep. And the next one I love, which you probably won't remember is the Texas Instruments TMC 0281 speech synthesizer chip. Now, nobody actually remembers the number. I don't remember the, uh, number for that chip, but you know, it's just the, the T I speech synthesizer chip. It's what everyone remembers. And that's circa 1978. And if you've ever watched, uh, E.T., the extraterrestrial, he uses the, the, uh, the speak and spell, uh, machine.

**Chris Gammell:** That is my first, that is my first, uh, exposure to this chip. Right. Okay. It was through E.T. Yeah.

**Dave Jones:** It was through E.T. I'm sure it was, yeah. But it was the hottest Christmas item in 1978 or 79 or something like that. So yeah, yeah. The speak and spell chip. And that really was game changing because at the time people went, holy shit, look what chips can do. You know, before that you needed, you know, like everyone knew you could build a computer with a whole, you know, hundreds and hundreds of chips, but this is when shit, a chip can speak. Oh my God. You know, the, you know, the future's here. It's, it was just that game changing. I think. Yeah. I've looked,

**Chris Gammell:** I've looked at that chip before too, because I, I forget why I was looking at it. Uh, but I, I, it's actually really interesting if you look at how, how they built it and, and like how they built up the phonetics and combined them. So they actually only, they had a very small subset of sounds that they could combine together. Yep. And it, I mean, it is somewhat intelligible. It's a little different today. I mean,

**Dave Jones:** it's, yeah, it's a lot different, but it's still based on a similar, similar concept. The speech allophones, the little, little nuances of speech. They've actually done a lot of, a lot of research, massive research goes into this about how speech can be broken up into these little allophones. Um, right. And there's other names for them too, but, uh, that's how they use it in these chips.

**Chris Gammell:** And that's coming back too, because there's a, I mean, there's a big push from Google even, you know, to increase their translation and their, their text to speech and speech to text kind of stuff.

**Dave Jones:** Text to speech is, yeah. Um, and if that was, yeah, it really didn't improve much there in 20 years. I mean, from 1978 to, right. You know, it didn't improve a massive amount. Now it's, it's pretty schmick these days. Um, well, it's all,

**Chris Gammell:** it's not based on discrete either though. It's, it's based, I mean, most of it is, you know, based on a CPU that is running at high, you know, high, high band or high frequency. So yeah,

**Dave Jones:** of course. Yeah.

**Chris Gammell:** Software based. Right.

**Dave Jones:** Yeah. And, and it's more, being more research and combined that way with today's computing power and everything else. And right, right. It's, it's starting to come together, but it still sounds like a computer voice, you know, so you can still pick it.

**Chris Gammell:** If there was, if there was a Ray Kurzweil-esque, uh, prediction I'd, I'd like to, I'd like to put forward too, it'd be the universal translator because that's what, that I've actually wrote about that before because I think that, that when that point comes when I can walk into any country and be able to communicate with someone and, you know, I pull out this little device that actually lets people know that I'm a stupid foreigner too.

**Dave Jones:** that little device will be called your phone.

**Chris Gammell:** Yeah, exactly. Yeah.

**Dave Jones:** Because everything's, everything's phone centric. Nobody has separate devices these days.

**Chris Gammell:** Right. Right. Right. So that, that would be mine. I can't wait for that. I can't wait.

**Dave Jones:** And will that be done as an app or will that have a dedicated voice chip in there? Because there's massive. I don't care. Come on. What do you mean you don't care? This is an electronics radio show. Of course you care. Oh, I know. You want it to be hardware, don't you? You don't want it to be some pussy software thing. I want it to be a reconfigurable FP,

**Chris Gammell:** reconfigurable FPGA. That's what I want.

**Dave Jones:** Oh, it can't be a reconfigurable FPGA. They draw too much power. They're too big. It's got to be a custom.

**Dave Jones:** for now. It's got to be a custom.

**Chris Gammell:** No way, man. Why not? You can reconfigure for each language. That'd be bad ass.

**Dave Jones:** Oh, yeah. Yeah. Oh, yeah.

**Chris Gammell:** Oh,

**Dave Jones:** yeah. Dedicated. So, well, dedicated silicon. Yeah, show me a mobile phone that's got an FPGA in it, you know.

**Chris Gammell:** Yeah, it's true. Yeah,

**Dave Jones:** they don't because they don't hit the power form. They don't hit the power. They don't hit the density. They don't, you know, they're great for bigger applications that can afford the, A, the expense, and B, the power consumption, C, the size, and all the rest of it.

**Chris Gammell:** the awesomeness.

**Dave Jones:** Well, yeah, they're pretty awesome that you can reconfigure you. Yeah. That's pretty awesome. But, yeah, I have to say,

**Chris Gammell:** after analog FPGAs are my vice. I like them. I think they're cool.

**Dave Jones:** Yeah, yeah, they are cool. I mean, you, but you get to a point, you know, you're all struck by FPGAs at the moment. A lot of people were, a lot of people are, and then you get to a point where you go, well, shit, I can't use them in everything. Well, of course you can't.

**Chris Gammell:** I know that.

**Dave Jones:** You know, but, ah, okay, well, you're a step ahead of some people then. Well, yeah. Because there's a lot of people out there who, who think they're the universal solution, and there's people out there who are betting that they're going to be the universal solution. And they're just, no, I don't think so. You know, no,

**Chris Gammell:** no. Principal, principal chips once you prototype it on FPGA. Right. That is the solution. Ah, I rolled it back in there, didn't I? Ah, come on,

**Dave Jones:** dude.

**Chris Gammell:** Anyway,

**Dave Jones:** next one on the list. Next one, next one. Let's finish the show with this. I think we've only got five minutes left.

**Chris Gammell:** Well, yeah, yeah.

**Dave Jones:** The 6502 microprocessor. Well, yeah, because it drew, it was one tenth the cost or something. That's what enabled the Apple One. That's what enabled, you know, was to go and build the Apple One. And, yeah, definitely.

**Chris Gammell:** And people still build with them today. You see projects on Make all the time, or Hackaday and everything. Yeah. So, 65 or two are big.

**Dave Jones:** Yep, absolutely. That was a huge thing. Even though it wasn't the first micro out there, but it was very influential, because it started Apple.

**Dave Jones:** yeah, and in the TMS DSP, the first TMS 32,000 series DSP, 1983. That was a big turning point, when you could do, you know, a DSP type processing in a device. It didn't have to be done all in software. So,

**Chris Gammell:** also a big, a big, a big, important event in, in that year that happened. What was that? I was born. I was born.

**Dave Jones:** You were born in 1983. Yeah. Holy crap, dude, in the 80s. I know. Jeez, man. I was sold on shit in my work, in my lab in 1983.

**Chris Gammell:** I can't help how old you are, Dave.

**Dave Jones:** I know. Oh, dear Eddie. I'm not that much older, but yeah, I started young.

**Chris Gammell:** That's good. That's good.

**Dave Jones:** Next on the list.

**Chris Gammell:** I was soldering the next year. How about that?

**Dave Jones:** Right. Okay.

**Chris Gammell:** Awesome.

**Dave Jones:** The microchip pick 16C84 in 1993. And, as some people, one person on the forum claimed that this wasn't, that claim, Atmel should have been on here, because they were the first flash device and all that. But, I think, no, the microchip definitely deserves to be on here, because it was the first microcontroller that wasn't either UV erasable or one time programmable. It used eSquared Prom. And, to do that, you know, to be able to program the thing, InCircuit was, and you didn't need an InCircuit, a very expensive and big InCircuit emulator, like you had to before these, you know, where you would take it for granted, that you can just, you know, recompile your code, download, boom, boom, boom, you know. Done. Ah. Whereas back in the old days, you either had to take the chip out, put it in a UV eraser, or you had to get a, or you had to get a big InCircuit emulator, which emulated the whole darn chip. And, ah, geez, anyway, let's rush through the list. I think we've, we're at 741. I think our amp hour's up, but I'm going to go through InnerCell waveform. Oh, the 8038 waveform generator, Western Digital UART. Everyone takes UARTs for granted, but before the chip came along, the Acorn Arm 1, the, you know, not, not everyone knows that arm processors came from the original Acorn, computer back in the 80s, but that's its heritage. So, there you go. Um, the first image sensor from Kodak. CCD. Um, the deep blue chest chip. Um, I'm skipping a couple. Um, 8088 processor, the first MP3 decoder. Yep. It's all there. Yeah, these are all big ones. Yeah. I don't know. Is that 80?

**Chris Gammell:** Yeah, I like that list. Yep. Yeah, it's good.

**Dave Jones:** I think it's a good list. I can't think of anything that, well, offhand, that is kind of missing, that was so important that it should have been on there. So I, yeah, I think they did well.

**Chris Gammell:** Great list. Kudos to the IEEE. Yes.

**Dave Jones:** Yes. Again, even though we do like to bash them occasionally.

**Chris Gammell:** We do like to bash them, but they do put us, I mean, like you've said before, their spectrum is, I mean, the spectrum magazine has some good stuff. I mean, it does.

**Speaker ?:** So,

**Chris Gammell:** yeah, very nice list. All right. I guess that's it.

**Dave Jones:** We're blowing it. That's the first one for the year, folks.

**Chris Gammell:** Yeah, and the first one without the, we're sorry for all the workbench of the week we skipped. Oh,

**Dave Jones:** holy crap. We forgot workbench of the week.

**Chris Gammell:** Yeah, we'll get them next week.

**Dave Jones:** We did. What did we spend an hour talking about then?

**Chris Gammell:** A lot of crap, man. Oh, jeez. Thanks for joining us, guys. Yeah, we'll talk to you next week. See ya. This is the Amp Hour Podcast. Recorded January 4th, 20, 2011. The Detroit.
