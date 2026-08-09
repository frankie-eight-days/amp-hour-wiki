---
episode: 520
title: Inductance and Stuff
url: https://theamphour.com/520-inductance-and-stuff/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released December 6th, 2020. Episode 520. Inductance and stuff.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. Want to jump into something that we know absolutely nothing about?

**Chris Gammell:** Unlike usual.

**Dave Jones:** RF.

**Chris Gammell:** RF. What about RF?

**Dave Jones:** I just did a teardown yesterday. I'm going to release it today. And it's an aircraft transponder.

**Chris Gammell:** Oh, interesting.

**Dave Jones:** Yeah, rather interesting. Made in Australia. Thank you very much. Recently?

**Chris Gammell:** Or no?

**Dave Jones:** Oh, no.

**Chris Gammell:** Like, is it modern? Or is it?

**Dave Jones:** Well, it's still a current design. But it was designed in 2000. So it was first sold.

**Chris Gammell:** But still active and still being manufactured. Oh, yeah, still active.

**Dave Jones:** Which is common for these bits of kit. You know, it's like you design them once. And it's got a pick micro in it. Spoiler alert. And it's like, yeah. That's why companies like Microchip and other companies, they still make the same micro. Because somebody designed it into a product 20 or even 30 years ago. Lifecycle. Yeah, exactly. And that's why they still sell the PIC 16C84. You know, you can still buy it. Right? Right. I think you can still get it. Better check that. Hang on. Hang on. PIC 16C84 DigiKey. I'm not talking about that new flash rubbish. Yeah.

**Chris Gammell:** Right. Right. Right.

**Dave Jones:** The old CMOS version. Let's see if they have it. No. You might have to go deaf.

**Chris Gammell:** I have a product that I'm like kind of updating for the modern era. And like, you know, the underlying bones of the thing is, you know, it's got a couple of PIC micros in there. Like, it works great. Like, honestly, it's like industrial equipment. Yeah. Of course it works. You know, like, it's like, aside from the fact that it needs to, you know, go on the internet now, because that's, you know, a new thing. Like, it's great. The underlying stuff that, you know, there's some bugs maybe, but it's just fine otherwise. So, and I think it was built, yeah, 20 plus years ago.

**Dave Jones:** Yeah. Yeah. No, I don't think you can still get the 16C84. I think you have to transition to the F. But microchip, I believe, has a transition document for going from the C to the F, which is not much. You just have to, you know. I think you might have to recompile the code. Not sure. But anyway. Or just program it differently because it's a, you know, choose that target instead of, I don't know. I can't remember. Jeez, I used to be all over the 16F84 like a rash.

**Chris Gammell:** It's like a, you know, it's like these tool sets that people have. I mean, I still don't quite have this in my own, you know, I'm still like, I don't have like a go-to, but like, yeah, I mean, a lot of hardware engineers specifically, they learn microchip. They're like, yeah, it's just every time. Like Mike Harrison's a good example.

**Dave Jones:** Oh, yeah, yeah. It just uses it for everything.

**Chris Gammell:** It's just this tool that he uses over and over again. And it's just.

**Dave Jones:** Why not? Because you know it intimately. Why dick around with new tools? Yeah. So I do micro stuff so infrequently. It's like, what do I use this time? I don't know. It's probably the same learning curve either way now, you know, because I forget. Yeah.

**Chris Gammell:** It's either learning or relearning, right? Right.

**Dave Jones:** Yeah, exactly. So it doesn't seem to make a difference. And as long as you stick with the vendor tools, you just install them, you write your C code and you compile, you know, there might be a few register, you know, tricks and other things between micros. But generally, you know, it doesn't take weeks to solve. You know, it takes like hours, you know, so it's not a big deal.

**Chris Gammell:** Yeah. So I have a lot of firmware. I was going to bring that up later. I have a lot of firmware coming up this winter and I have some, some things that I'm, I'm going through for that. So, right. But let's get back to RF. So what about RF? So this is a thing, aircraft, aircraft or air? Aircraft transponder.

**Dave Jones:** Yes.

**Chris Gammell:** So on the actual airframe, like.

**Dave Jones:** Yes. Well, it's a, no, it's an instrument in the cockpit. It's an instrument in the cockpit. Okay.

**Chris Gammell:** Right. Okay.

**Dave Jones:** So it's the, it's the transponder. It's a, you know, your typical round instrument. So, you know, virtually every light aircraft should have one of these transponder things. And there's a specific frequency, 1,030 megahertz for the reception. So the air traffic control systems or other planes, they will like send out this 1,030 megahertz pulse. Right. And they expect if you're in their airspace, they expect your, you to your transponder to return on 1,090 megahertz. Right. With the squawk code. And then the, when, when you fly into the air traffic control space, they will, you know, tell you, oh, you know, please set your transponder code so that we can track you, blah, blah, blah. You know, so it's got a little dial on it and stuff. Anyway, transponder. So I did a teardown spoiler alert. And there's what looks like a, there's, there's a transmitter. Like there's a big beefy ceramic output power transistor, which are specifically designed by the way, chip of the week or part of the week. I can possibly, hang on. I'll send you the data sheet for, if I've got it. Oh, do I still have one? Is it like tuned?

**Chris Gammell:** Is it tuned to the actual frequency that you're expecting?

**Dave Jones:** Well, it's, well, it's not tuned because it's just a transistor, but it's optimized. It's optimized for this thing. So I will send you, here we go. Here you go. Part of the week. And there's several release. And it's a company, Gigahertz Technology, which I think have merged with somebody else now, but RF microwave silicon power transistors. That's all they do, you know, and they've got one specifically for the 1030 and 1090 megahertz, you know, transmission band, right? So I don't know how you optimize a transition, a transistor for that particular thing. I don't know, but it's, you know, it's got an ultra high MTBF and, you know.

**Chris Gammell:** Yeah. I would assume that it's something about like the dopants in the actual transistor so that it's resonating at the right, you know, the right range of frequency.

**Dave Jones:** I wouldn't, I wouldn't say resonating. I think your common guts are on that turn there. But anyway, if there are any silicon, yeah, Sharia would tell us, right?

**Chris Gammell:** Yeah. Maybe, maybe, maybe we can ask Mr. Mr. Jeff Kaiser on Kaisermis, the upcoming Kaisermis. If he says yes, we actually haven't asked him. We just assume that he's going to show up. Does he design, you know, silicon? Oh, he used to design RF power amplifiers.

**Dave Jones:** Oh, okay. Right. Yeah. Okay. But at the transistor, like actually designing the transistors themselves.

**Chris Gammell:** Yeah. That's what he used to do. Oh, okay. Oh, yeah. Oh, cool. He used to work at a chip firm.

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** Well, ask him all about it. All right. On this year's Kaisermis if he shows up. Yes.

**Dave Jones:** All right. I'll message him later. Anyway, yeah. Specific transistors designed for these Pulsed applications at just over a gig. I mean, you know, we're sure you could use them for other things, but yeah.

**Chris Gammell:** So what's surrounding this thing? What's actually driving this then? So is there actually, is the, is the pick actually driving this,

**Dave Jones:** this, uh, well, yeah, but the picks just like controlling the interface. It's got a two line dot matrix LCD. Oh, got it. It's got a, yeah. Buttons and other things. Right. And there's not much in it. It's just a, basically a VRF side of things. There's just a discrete three transistor power amp, something like at least, you know, there's three of these beasties in there of different types. And yeah, it's, you know, and it just, yeah, it just drives the output. Right. So what's the, what's the power, power rating?

**Chris Gammell:** Cause like a hundred and 140 Watts. Okay. Yeah. That's so like, I'm just going to say like, I've been doing like some RF stuff lately, but it's like low power, you know, Oh yeah. It's low power stuff. This is like 140 Watts. Yeah. I mean, that's like cranking.

**Dave Jones:** Yeah. If you read the installation manual, it says, you know, do not install the antenna, you know, closer than 1.4 meters from anything else or something like that. And it's like, you know, or, or humans.

**Chris Gammell:** You will cook your toe off. If you, if you put this in the wrong spot, you will cook your toe into a Vienna sausage.

**Dave Jones:** Yeah. Anyway, so there's a little antenna on the bottom, you know, probably the backside bottom of the plane. That's the transponder antenna. Cool. Just over again. Anyway. So, and of course, so it's got a receive as well, you know, using the same antenna. So of course they, they tap off a line from that, from the antenna. So you're pumping out the 140 Watts. It's mostly receiving all the time. It'll just only do a little, you know, pulse transmit when it needs to, uh, when it's, when it's requested to, it doesn't just randomly do it, you know, just on its own. It's got to wait for a reception signal and go, Oh yeah. Okay. I'll transpond now. I'll send my code. And anyway, so yeah. So it taps off the antenna output, you know, goes through some controlling impedance lines on the Rogers PCB material or whatever it is, you know, goes through a little, uh, distributed element filter on the PCB as well. Um, I've done videos on those, which, you know, use your traces as your inductors. And then they use like large little pads, which branch off, you know, the, the funky RF looking things you see on PCBs, you know? So they have a little, like what looks like an LC filter there. And then it goes into what looks like to me, and I'm no RF expert, what looks like a comb line, uh, filter. Right. And the comb line, they still like, which is an aluminium set of it's, it's, it's just a block of a piece of block aluminium, right. Or aluminum for you yanks, right. With, with little fingers on it and which then act as capacitor air gaps and stuff like that. And it's, you know, but the thing is, and then it's got little cavities in them where you can actually tune the things. So I'm not sure quite how they work anyway.

**Chris Gammell:** The comb line filter is actually like a separate element you're saying, or it's actually on the PCB as well.

**Dave Jones:** No, no, no. It's a separate aluminium block. But the interesting thing about it is, sorry, I can't see your photo now, but the, maybe we can include it as the screen.

**Chris Gammell:** I mean, I'm looking them up as you're talking about this. I don't, I don't, I didn't know this term though beforehand. So.

**Dave Jones:** Well, okay. Comb line filter. And there's many different varieties, how you implement them. But this one is basically just a picture and aluminium thing with little fingers on it. Right. And the signal goes into the aluminium. Right. It just, it's just bonded into the side. It's just got bond wires. And then it pops out the other side. But the interesting thing is, is that this comb line, this aluminium filter is then just grounded, screwed straight into the chassis, which is grounded. Right. So you're effectively grounding the output of your power amplifier. Right. It just goes into that. It still blows my mind.

**Chris Gammell:** So it looks like you're like dumping it into a ground. Yeah.

**Dave Jones:** It looks, it looks like you're dumping it into a ground, but at one gig, you're not. Right. That's right. Because at one gig, everything changes. Skin effects. Right. Or no. Well, yeah, it's just inductance and stuff, you know? Like, yeah. Inductance and stuff.

**Chris Gammell:** Inductance and stuff.

**Dave Jones:** Stuff. It's a t-shirt there. Yeah. And it's just, I, every time I see something like that, I go, well, you know, like, yeah.

**Chris Gammell:** That sounds like the right, the right response. Yeah.

**Dave Jones:** It's not the right engineering response, is it?

**Chris Gammell:** It's kind of, oh, I should learn that. I think all engineering starts with wonder and then eventually you go, yeah, I should learn more about this.

**Dave Jones:** Yeah, exactly. If I could be bothered to, yeah, learn all about it.

**Chris Gammell:** I mean, these power levels too, like, I just don't deal on these power levels. No, exactly. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Because some of this, like the comb line stuff, like some of that is on PCBs sometimes, right? Like microstructure.

**Dave Jones:** Oh, yes. Yeah. You can get comb line filters on PCBs. Yes. Right.

**Chris Gammell:** And you've shown that, like when you do like VNA teardowns and stuff, you'll see some of that stuff, right? Or like spectrum analyzers.

**Dave Jones:** Oh, yeah. Yeah. You'll see those on the PCBs. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. But this one is like, it's screwed into the block. Like originally when I looked at it, I was all through my video. I've got to actually re-edit it. All through, I thought it was a cavity filter, which is a different thing, right? I thought the wire went in the side and it was insulated when it goes through the side and then it's inside, it goes through the cavity, right? I thought it was a cavity, but it's not. The wire is just bonded, soldered to the aluminium, piece of aluminium, which is then screwed into the bloody case with no insulating thing. It's just screwed into the grounded case. It's like, oh, what the? Anyway, I'm sure we're going to cop a lot of crap in the comments. Well, you know.

**Chris Gammell:** I think we started pretty well with like, you know, we don't know what we're talking about here.

**Dave Jones:** No, exactly. Yeah.

**Chris Gammell:** And people probably start with a safe assumption of that. I, you know.

**Dave Jones:** Yeah. Oh, well, yeah.

**Chris Gammell:** Do you have interest in this otherwise? I think that's the real question is like, are you going to take this further? Because it would be interesting to like throw something like that. So like the filter, the Comline filter, is it like an SMA input or something like that? And then like, it's like a through pass? No, no, no.

**Dave Jones:** It's, it's literally a block of aluminium with a wire soldered into the side of the aluminium.

**Chris Gammell:** But is it a two port device or one port device? It's like, there's nothing coming back out?

**Dave Jones:** No, no. Well, no, there's a wire on the other side of it. Also wired directly through and soldered into the aluminium. But so it's a piece of aluminium.

**Chris Gammell:** Right. But the signal is going through it though. That's what I mean. It's like the signal is going through this thing.

**Dave Jones:** Through in quote marks. Right. It's like, yeah, that's the weird thing. It's like, it's shaped like a comb. So picture a comb, you know, the bar at the top, the aluminium bar, and there's a wire, and it's got all these little fingers coming down. And there's a wire that goes into the first finger and a wire that comes out the last finger. But if you put your multimeter on it, of course, it measures zero ohms because it's just a chunk of aluminium.

**Chris Gammell:** That's right.

**Dave Jones:** But, you know, and it magically just, yeah. Like the ones you get on PCBs, like they might be isolated, of course, right? They're not actually grounded. Although that might be the definition of a comb filter. So anyway, I won't go into details. Because I can't.

**Chris Gammell:** Yeah, I was just wondering, like, if you put it on a VNA, what it looks like, that kind of thing, you know? So like looking at the actual impedance of that thing would be interesting.

**Dave Jones:** Yeah, it's just fascinating. It's a block of aluminium. Like I could understand if it was like insulated from the chassis, you know, and it's just sitting there and it's just a block and it's, you know, okay. Right. I can, I know the fact that it's just screwed into the chassis and it's grounded and it's hooked practically directly to the antenna via a PCB trace. It's just like, well, oh man, it just, it just weirds me out. That's all. So I think I'll stick to digital, you know, low power stuff. Thank you. Okay. End of story. Yep.

**Chris Gammell:** Okay. Well, we have another thing on the list about RF stuff. There's apparently, there was a test on the Pi 4, which is like, if you're on the ethernet, you can actually, it was actually in, was it 375 megahertz, I think? Yeah. But this thing was actually like, the Pi 4 was like just cranking RF energy out of the ethernet port.

**Dave Jones:** Right. That's interesting. Well, technically, is that classed as conducted mode radiation? Because it's conducted out, even though ethernet is technically isolated because of the transformer. Or there's another tricky question for our RF aficionados. Is it conducted? Because there's two types of radiation. There's conducted mode radiation, which radiates out of the wires that come into and out of your device. Right. And technically, that's what's happening here. Right. But usually, by the term conducted, it means electrically conducted via the shield, via the, you know, the power wiring and stuff like that. Whereas ethernet is technically isolated. So I think I'd still call it conducted mode.

**Chris Gammell:** But here's the thing. So like the, if you, if you watch the video, if you watch the video, it's basically just a Raspberry Pi attached to a battery hanging out in space. And then he's got a radio across the room that's receiving.

**Dave Jones:** Oh, right. Is that all? Okay.

**Chris Gammell:** Yeah. It's receiving signal from it. So.

**Dave Jones:** Oh, okay. Oh, so he hasn't even got an ethernet connected to it.

**Chris Gammell:** No, no, there's, yeah. It's not actually the case. It's through the actual, yeah. The ethernet Phi basically is cranking.

**Dave Jones:** Oh, okay. So it's not even, sorry. My little rant about conducted mode interference is totally worthless there. Yeah. Okay. I thought, I just assumed it would only do it, you know, when it has.

**Chris Gammell:** Yeah, you meant like actually over the. The cable hanging off. Yeah, yeah, yeah.

**Dave Jones:** And then the wire acts as the antenna. That's what conducted mode interference is. Right.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** This is crazy.

**Dave Jones:** Wow. All right.

**Chris Gammell:** And one last thing since, since we're in, in the RF mode and this is maybe another good question for Jeff. We have not, we talked about it here, but I have no idea what's been happening. So I had to stop recording on my H6N, which is like a recorder, right? So it basically is how I.

**Dave Jones:** Portable thing. Yep.

**Chris Gammell:** Yeah. It's a little portable recorder. It does XLR inputs and stuff like that. And so I have in my setup downstairs, I have like a microphone. That's a shotgun microphone. And then I have a cable going off that. And sometimes I, you know, I would use lapel mics off of it too, whatever. But, uh, and I live in downtown Chicago, live pretty close to like a huge transmitter known as the Sears or Willis tower. And like, but if the, uh, the wires are configured just right, it picks up a, not even just right. It's like all the time because we're pretty close. And like it basically it conducts, uh, it will start playing a radio station and it sounds like an FM radio station. Just, just from the content. I haven't been able to match up with which station. Like it would make more sense if it was an AM station just because it's like, cause it

**Dave Jones:** would be bridge rectified. Cause then you can have it just purely AM rectified, but FM requires demodulation of

**Chris Gammell:** FM. Exactly. And that's where it doesn't make any sense to me. I probably should just investigate it more, but like, yeah, it's, it leaks into everything and, uh, here and it's, uh. Yeah.

**Dave Jones:** We've had this on the show before. Were we almost borderline going to like drive out to like near a transmitter and try it somehow? Now, didn't you, uh, you know, well, I live near a transmitter. I mean, you said, Oh, take your zoom, you know, take your zoom out there near the transmitter

**Chris Gammell:** and yeah.

**Dave Jones:** Try it. Have you actually verified that it is an FM station?

**Chris Gammell:** And that's the thing I haven't done. I really should do that because otherwise I think you need to do that, but it's all like music and like, you know, like just, there aren't many AM stations that play music these days just because like, why would you? So I don't know. I should, I should actually try and match it up with, with the station, but.

**Dave Jones:** Because if people don't know, like a crystal radio set is the classic way to pick up an AM radio signal, right? They, they did this in the, in the trenches in, you know, the world wars, right? They, you know, they crafted together, uh, radios out of a razor blade and a pencil. That's literally all you need, right? To make a point contact diode and you can pick it, whack it onto an antenna and put in a crystal earpiece and bingo, you can actually pick up signals, right? It's cool. It's called a crystal radio. And there's lots of things that can actually form parasitic PN junctions, i.e. a diode. And then once you've got a diode in there and a long antenna, you're picking stuff up, right? And it's being rectified and it's, yeah.

**Chris Gammell:** Yeah. And that's why it would make a lot more sense if it was AM, but, uh. Right. I didn't think it was. Is that, I, yeah. Anyways, I, I should really, I should verify that first. Cause that makes a lot more sense. Fascinating. Wow.

**Dave Jones:** And annoying.

**Chris Gammell:** Fixed it by changing the cable length. If you didn't know that.

**Dave Jones:** Cable length. Okay. You can fix it. You get in our foil and, you know.

**Chris Gammell:** No, not that. I mean, yeah, yeah, that's not going to help much, but, uh, I mean, cause this is basically, I was like, had a huge antenna because it was just like a, you know, a six meter cable or something like that. It was just extra cable I had. And, you know, it was like at the right, right frequency.

**Dave Jones:** So you need to move out into the burbs, my friend.

**Chris Gammell:** I know. Well, yeah, I gotta, gotta, I have wondered about that too. Cause I have like a bunch of like spurious noise on scope sometimes too. And like, like being near, you know, some of it's beneficial, right? I mean, like I can hit a cell tower, like three blocks from my house when I'm doing cellular stuff. But when I'm just like trying to like pick up, you know, when I'm like looking at like a high bandwidth signal on my scope and I start to pick up all this other noise, I'm just like always questioning, like, is it, you know, some kind of localized RF that's getting rectified into, into this stuff. So.

**Dave Jones:** Oh, you, you, you could be chasing your tail. I think you've got no, you know, problem in your product. Exactly. Right. Yeah. It's yeah. You gotta be careful. So, well, you may actually have a problem in your product. As I said, some parasitic diode junction somewhere in some long cable, that could be a problem with your product, but it only manifests itself under certain. Right. King in certain configurations.

**Chris Gammell:** Right. And yeah. And on the one hand, you could imagine it'd be good because it's like, I'm going to find that problem early instead of like, if I was like in the boonies and I was, you know, developing a product and I'm like, oh, this thing works great. You know, there's no interference around here. Then, you know, I drive downtown, I drop it off at a customer and they're like, uh, yeah, this thing, this doesn't work at all. So I guess from that perspective, it's good, but, uh, you know, it's a little, uh, still annoying. I'm just trying to get my scope to work, man.

**Dave Jones:** Oh boy. Can we talk about dodgy wiring? I've, I've got a segue with dodgy wiring that I tweeted this morning.

**Chris Gammell:** Yeah.

**Dave Jones:** I saw that. Yeah. I, um, got a new air con in Stortle, you know, she who must be obeyed did got another air con for the, because she's working from home now. Right.

**Chris Gammell:** And then we're, we've got a new back room where, you know, and it's hot as hell in Australia right now. So.

**Dave Jones:** And it's coming into summertime. So she said, well, I want a damn air con, you know, cause we've got air cons in other parts of the house, but you know, there, it doesn't sort of bleed. Yeah. Cause we don't have like central air con or whatever. That's right. So anyway, um, they install, you know, the tiniest one we could get, cause it only really only suitable for one room. So it's a 3.5 kilowatt air con, which of course doesn't mean it draws 3.5 kilowatts. Right. Because the coefficient of performance air cons are heat pumps. Right. So technically like a, you know, a 3.5 kilowatt air con in this case supposedly only takes 800 watts. Right. So the coefficient of performance, you divide 3.2 by, you know, 8.8 or whatever. And that's your coefficient of performance. Right. And, but there's other peak surge figures involved and stuff like that. I can't actually make heads or tails of the label.

**Chris Gammell:** It's like the max rating. Is that kind of the idea? So that's just like, you can size it. Like that would be the absolute maximum output there.

**Dave Jones:** Yeah. The label's got two things. Have a look at my, you know, if you're interested, have a look at my Twitter photo, which will link in to the show notes. And you can see there's two, there's one table for the unit itself, but then there's another one, which if you look up the model number four, it goes, Oh, it's only 0.8 watts, 0.8 kilowatts power consumption, right. For the 3.5 kilowatt model. So which one, you know? So yeah, I think it's the point. Anyway, what they did is they wired it. Like I just expected them to install a new fuse in the box, right. And run another dedicated cable. Cause I thought, Oh, air cons, they draw a lot. I didn't think about, you know, how much it actually drew, even though I knew it was a small one. And I just assumed, so I went out to the box to check that they've installed the new fuse and everything. And there's nothing there. So when, how the hell have they wired this thing in? And I thought, and I tried checking out the other switches. I thought, Oh, maybe they shared it with one. Cause we've got two other air con, you know, circuit breakers. So I thought, Oh, maybe they've shared it. Cause it's a low power one or whatever. And no, I tried to control that. No, it's still working when I disconnect the other fuses. So I went, these bastards have wired it.

**Chris Gammell:** What's it hooked into?

**Dave Jones:** Yeah. These bastards have wired it into the mains, into the PowerPoints. They must've, it was the only option. And so I went up in the roof that like one of the local.

**Chris Gammell:** So you mean like one of the actual plugs on the wall near it or something?

**Dave Jones:** Well, yeah. The, the wiring that goes to the PowerPoints in the wall. Right. So yeah. And sure enough, I went up in the roof this morning and sure enough, I took a photo. There it is. It's wired into the spliced into the existing PowerPoint wiring. And I didn't, I just assumed that wasn't legal to hardwire a device, like an air conditioner into a, into a PowerPoint wiring.

**Chris Gammell:** Yeah. I mean, this would be like the equivalent of like point, like plugging a, so like I have, I actually am staring at an air conditioner as well. And we have a dedicated circuit for it because it's like a heavy duty, but it is plugged into the wall in a, you know, like, so the U S has that dual phase. Right. You can have it. Yeah. So that's, but it's, but it is, it plugs in.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. It's its own circuit, but it does plug in. Yeah. And I mean, you could do that for a window unit too. If you had a window unit to, to put into.

**Dave Jones:** You could probably plug it in, but this one's a fixed device. So I believe the laws are different for anything. That's a fixed wide device. Please correct me if I'm wrong. Cause I don't know my code, you know, it's all about the specific. So.

**Chris Gammell:** Yeah. What do you call it? It's it's any, the NEC here, the national electric code, I think.

**Dave Jones:** National. Yeah. It's something else here. I don't know what it is. It's, you know, some standard here. Anyway, it's very, you know, it's like a 300 page book or something, isn't it? And you know, if you want to become a Sparky, that's what you have to know inside and out. Right. And I just know absolutely nothing about it. So I don't even know if that's legal or not. And, but I guess if it is, I'm going to have to measure it. If it is actually drawing only 800 Watts. And technically that's just like plugging in 800 watt microwave into the PowerPoint. Right. It's not a, you know, it's not a big deal, but whether or not it's technically legal to do that, I don't know. So please leave it in the comments. If you're a Sparky certified in New South Wales.

**Chris Gammell:** Right. Exactly. Yeah. And it is, it is a local thing too. Right. I mean, you really should just talk to them.

**Dave Jones:** Oh, totally local. Yeah. I'm sure it varies from state to state too. You could probably have different. Yeah. I could be wrong on that, but that wouldn't surprise me at all. Consider that we have different legislation requirements, registration requirements for different states.

**Chris Gammell:** Yeah. To be like called an electrician. Yes. Yeah.

**Dave Jones:** Well, what you have to go through to become an electrician in different states is, yeah, it's different. It's all state-based. So, yeah. So that, that wouldn't surprise me at all, but there's probably some national code for it, but yeah, I don't know. I just thought that was like dodgy. I just, you know, but it may not be, they may went, well, it's only, you know, if it does draw 800 Watts, only 800 Watts was whacking into the existing 20 amp wiring, you know, for the PowerPoints. But I don't know.

**Chris Gammell:** I was just like. I mean, maybe they can calculate the load on the total circuit or whatever, but yeah.

**Dave Jones:** Well, well, that's the thing. Like technically each outlet is 10 amps, right? Each. And yet we've installed how many PowerPoints in the, in the new back room that has the new wire in there, right? There's like, I don't know, eight PowerPoints or something, right? So you can't put 10 amps into, you can't draw 10 amps from each one.

**Chris Gammell:** Have like three vacuum cleaners running in there.

**Dave Jones:** Yeah. Yeah. And a fridge and a, and a microwave and a hairdryer and a, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Right. You just, it's just going to get a busy place.

**Chris Gammell:** It's a busy place.

**Dave Jones:** Yeah, exactly. Like on my bench here, just the bench I'm working at now, I've got 20 PowerPoints. I, I, I believe that's the maximum you can install on one circuit. So yeah. Yeah. Yeah. Yeah. Anyway. Yeah. So please, I need to know, is that dodgy is, you know, it just seems a bit, how are you doing? Yeah. Anyway, what else we got?

**Chris Gammell:** Well, we could stick on the, uh, the RF side of things if you wanted to stick on the RF side if you wanted to, because there was, there was a teardown of the Starlink. We, we talked about the Starlink when yours was on the show, uh, last week, last week. No. Yes. Uh, the, uh, basically we talked about, no, that was, sorry. There's Michael last week. So two weeks ago when yours was on the show, we talked about Starlink a little bit. And then he actually sent me a link that was about someone did a teardown. They took their early dishy, which is called the, uh, that's the thing in that. So it's kind of cool.

**Speaker ?:** Hmm.

**Dave Jones:** Our former, former guest and friend, uh, Robert, uh, Faradik, who, you know, runs the, uh, excellent YouTube channel. Um, he's, and runs the PCB courses and everything. Yeah. He's just done a video, which, which PCB design software is the best. The top four.

**Chris Gammell:** This is a clickbait.

**Dave Jones:** What I, is clickbait. Did he give any conclusion? Cause he's an Altium man, right?

**Chris Gammell:** Well, but he basically said the right, the right, sorry, spoilers, but he said the right one is the one that you, is the right for you.

**Dave Jones:** You know, it's the one that's right for you. Yes. Well done, Robert. There's a, there's a golf clap for the, uh, for the clickbait. Yeah. Yeah. Yep. And it's probably going to work. And yeah. Oh boy. I think, yeah. That's like, he doesn't mention Eagle. Does he? He doesn't mention Eagle. He doesn't. Altium, Cadence, KeyCad, Mentor.

**Chris Gammell:** Yeah. But that might be right for some people, you know?

**Dave Jones:** So see, 10 years ago it was Eagle, Eagle, Eagle was going to, and nobody talks about Eagle anymore. It's just Gonski.

**Chris Gammell:** Some people do. I mean, well, first off, Eagle is going away. I mean, it's going to be called, it's Fusion 360 Electronics or whatever they call it.

**Dave Jones:** Okay. Yeah.

**Chris Gammell:** That's what they're migrating it to. And there's going to be, you know, people that are upset about that. I'm sure. But. Oh, sure. Yeah. Yeah. It's. I don't know.

**Dave Jones:** Yeah. Yeah. No, I think KeyCad is just absolutely buried that now. So.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** You do any boards these days? Have you done a board recently? No, I haven't done a board recently.

**Dave Jones:** No, unfortunately. No. You should check out.

**Chris Gammell:** So the, I, well, I just started using, I did. So I have, I've been doing a bunch of VM stuff lately. And I was looking at a design that was done in version six of KeyCad. And it was interesting. Just like, you know, that, that first time you open, it was almost, it was almost so, not so different, but it was different enough that it like, I opened it up and I'm like, Oh, what am I, what am I doing here? Like I just like got lost immediately. And you know, you might want to check out the new one. It's, it's getting closer to an Altium kind of thing. So. Oh, okay. So they've totally revamped the UI again. Have they? Not, not the UI, but like some of the more of the features and like, it's all scriptable for, so like one of the lacking in the V5 was kind of the, the individual nature of DRC. So that you could, you couldn't like really specify DRC to like the, the same level that like an Altium or a, you know, an Allegro or whatever it could do. And now it's all like scriptable even, which is kind of pretty cool.

**Dave Jones:** Right.

**Chris Gammell:** So yeah. That part's, I mean, it's a lot of like, you know, so like we did a, a developer chat a while back, which was like the replacement for KaiCon. And they, they talked about, you know, like John Evans and Seth Philbrand and Wayne and the whole team. Like they all kind of went through all the different things that are out there that are going to be different on there. So I can, I'll link that in again, but.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. I was just wondering if you would open that up recently and seen, seen some of the new designs. So.

**Dave Jones:** Unfortunately not. I'll have to check it out.

**Chris Gammell:** Yeah. It's, it's good. You know, I do like this new method of, so I've been doing, I, I've been doing like VMware boxes for like each client. So like a VM basically. So each time, you know, all the tool chains in there, I have a Kaiket instance in there. Right. It's just kind of like a standalone thing. Then if I need to, I can just like box it up and ship it over and it's like sending them a laptop. So that's the. Right. That's the, that's the new method of doing things. So, cause I've also.

**Dave Jones:** That's rather professional of you, Chris.

**Chris Gammell:** Yeah. I mean, you know, I, I think the real thing is that I, I had to refilm at a computer and I lost a tool chain and I was like, Oh, this sucks.

**Dave Jones:** All right. This sucks.

**Chris Gammell:** So I should just do this better, you know? So, yeah.

**Dave Jones:** Oh boy.

**Chris Gammell:** Yep. Yeah. All right.

**Dave Jones:** Nice. Oh, speaking of PCB designs, Greg Darvill on his Twitter has been doing a an advent PCB every day. So if you want to follow him on Twitter, I don't know where he gets the time to do a PCB every day. Like, and some of them are, you know, like just is like mad man.

**Chris Gammell:** Yeah. Yeah. He's a mad lad.

**Dave Jones:** Mad lad is the Pobbies call him. Yeah.

**Chris Gammell:** Yes. That's right.

**Dave Jones:** Mad lad. Is that a term in, in the U S too? Mad lad.

**Chris Gammell:** No. I mean, just on the internet. Right. Quoting British people. Yeah. Yes. Yeah, exactly. Mad lad.

**Dave Jones:** Absolute mad lad.

**Chris Gammell:** Yeah. There's another advent thing too. I think this is kind of like a popular thing. I've seen one for like 3d stuff. There's also one that's advent of code. So like if you wanted to like, so like a, so there's like an advent calendars, like a Christmas tradition type of thing, you know, it's non-religious, all this stuff, but it's like a, it's like a thing a day. Yeah. It's like a month. Yeah. Yeah. And so there's one for code as well. That's going on. So it's, you know, it's the third now it's, you could still get into it though. It's called advent of code.com. So that's another one you could do, you know, just a good way to like kind of follow along, follow the people kind of push yourself to do a thing. When I talked to Sophie Wong on the protects electronics podcast, she did one, which was like a 30 days of fusion. So she was learning 3d modeling. I thought that was a great idea too. You know, it's like just a good way to push yourself each day. And even if it ends up being coming something where it's like that day is not like the most, you know, it doesn't have to be the best thing on a day, but it's just getting that, it's getting them. It's doing something down and doing something. Right. Exactly. There was a, I think it's in the, one of the books I like atomic habits, I think maybe one of the other books, there was like this anecdote about like a photography professor professor and they talk about like the, he split his class into two and he said to one group, you get, you get judged on how many photos you do. You have to do at least a hundred photos in the semester. And then the other group was you get judged on the quality of your best photo. And the idea was like comparing, comparing those two. And I really liked that because the, the quality, the quantity group, you know, they didn't have the best photo. Every photo is not the best photo, but because they iterated so much, they just like, they outshone the other group like crazy because people weren't like really concentrating on that one thing and like perfecting it. It was more just like, yeah, just try a bunch of different things.

**Dave Jones:** So churning it out. And eventually you're going to hit on a winner, right? There's going to be one in there that's absolutely spectacular, you know, or just as good as you could have done when you carefully planned it and, you know, set it out. It's like, you know, everyone's used to that. When you take photos, you know, you go on a, you know, a holiday or something and there'll be one or two spectacular photos that just happened to turn out, you know, and the rest are just meh, you know.

**Chris Gammell:** But you still make people sit through the entire slideshow. It's like a slideshow.

**Dave Jones:** Yep. Yep. I can remember when I actually produced a DVD of our world trip, you know, and then, yeah, you'll make the family members sit through.

**Chris Gammell:** You didn't, you didn't, you, did you ever do slides? You ever do actual slides? No, no. I always wanted to, but I never had like a carousel, you know, like you had to actually have like a projector carousel thing.

**Dave Jones:** We, we weren't a, we weren't a camera family. Technically we had a camera, but there's, there's so few photos of me as a kid, like of our family actually growing up. There's like, I could count them on, you know, both hands.

**Chris Gammell:** Even like a handy cam, like a, like a point and shoot kind of thing. Like those, those were like getting popular as you were growing up, right? No, no, no. What? Wait, you're talking about a video camera? No, no, no. Sorry. Like the, uh, you know, 35 millimeter, like a handy cam, like a, probably the wrong term, but you know, just like the 35 millimeter, you throw like two batteries in there and

**Dave Jones:** it's self-winding and you're talking about a compact. Yeah. No, you're talking about a compact camera. No, I, we didn't know we had some ancient thing and, um, yeah, no, I probably wasn't until mid nineties that I got a film camera of my own, but that's, you know, beyond being a kid anymore, you know, that's like, yeah, like maybe early nineties or something that I actually got. Dave decides to try photography, right? Yeah. Yeah. It's like, yeah, you know, I got one of those compact things and it, you know, it's, you know, it had the little LCD on it and had all the various, you know, man, you know, it can measure distance and it had the infrared to measure the focus distance automatically and all that sort of jazz, you know? Yeah. And, uh, I think it was a Pentax. There you go. Pentax fan boys. And, and no, but when we were a kid, no, it was like, no, we just didn't take photos. It's like, you know, technically, yeah, we did have this film camera somewhere gathering dust, but no, just right.

**Chris Gammell:** Right.

**Dave Jones:** Yeah. So yeah. Don't ask me for photos of when I was a kid. There's like, I can maybe pull out a couple, but that's it.

**Chris Gammell:** You heard it here first folks. Was Dave even ever a child child? Yeah. No, we don't know.

**Dave Jones:** No. Yes. Ah, boy.

**Chris Gammell:** Anyway. Yeah. So firmware, I realized that all of my, uh, all of my projects are like coming, like I'm doing all these assemblies and stuff like that. And like between, okay. So first off, uh, news flashed, everyone out there, Chinese new year will be happening again this year. It is, uh, the first week of February, I believe. And, uh, it's, it's coming towards us. So get your designs out now. You think about it now. Uh, and so I've been thinking about that and I've been like, kind of like doing the math and like, okay, well I should, you know, I got about a month, you know, a month and a half to build and, you know, build my own or, you know, I could still get parts from DigiKey or I could, you know, get some locally sourced boards, whatever. But it's just like, that's a pretty big schism in the electronics world. And so it's like, I'm going to have everything built by then. But then it's like, oh man, like that means a good portion of the winter is going to be me doing firmware. And it's like, yeah, just kind of like that mental shift is like, I don't know, maybe I need, I, so I've been thinking about like how to get better at firmware and I've been asking online and things like that. And obviously there's just a wide, wide, wide variety of people giving, giving advice and it's very much appreciated, but it's a, it's a, it's a lot. So I'm, I'm reading new books, Dave. That's I'm sure you'll be surprised to hear. I'm reading new books. I know. Yeah.

**Dave Jones:** Yeah. Can we shout out again, former guest Bunny, who's done another just incredible blog post about the precursor is his new, is it a phone? It's not really a phone, is it? But it's a, it's a mobile device with an FPGA in it. And it's a, anyway, it was a Kickstarter or still is a Kickstarter or something. The precursor. Yeah. Something like that. Is it as he, as he met his targets last I looked, it wasn't.

**Chris Gammell:** He is not. He's at like 180, 220 K. So I bet he'll hit it though. I bet.

**Dave Jones:** Oh, that's, that's agonizingly close, isn't it?

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Anyway. Yeah. The precursor. And he basically, this is a blog post about the custom PCBs in there and everything to do with manufacturing detail of these custom PCBs. You know, he's put together all these, you know, micro photos of the via, you know, of the section, the cross section of the PCB and matches that up with the PCB layout and stuff. It's just, it's, yeah, he's gone to a lot of effort for this blog post. So it's well worth reading.

**Chris Gammell:** Yeah. There's a lot of stuff in there. That's, it's kind of like, if you're on the edge of like, uh, using, you know, maybe the prototyping services and like that, and you're thinking like, oh, I want to push the envelope of my own designs and get to, you know, get to hire. Like he talks about, you just literally can't use some of the parts that are out there these days that are like 0.25, 0.4 millimeter pitch BGAs. You just can't get the stuff out of those parts.

**Dave Jones:** Can't do it on a standard $5 proto board. Yeah, exactly.

**Chris Gammell:** And so he's using like laser, laser micro vias and, and stuff like that. And he shows a stack up and how that impacts things. And then he talks about the, uh, the inverted F antenna that he's using for 2.4, which is also the logo on the bezel. And it's just super cool. Yeah. You know? And so, yeah. Bonnie's been on the show twice before we might try and get him back. We'll see. But, uh, he's working with Zobbs as well. Who's also been on the show. And, uh, yeah, it's always interesting seeing. So like the precursor is, I think tied to his work. He worked with Snowden for a bit.

**Dave Jones:** Yes. He worked with Snowden on the, uh, secure phone thing.

**Chris Gammell:** That's right. That's the focus of this as well.

**Dave Jones:** I don't know if that ever became a product though.

**Chris Gammell:** I don't think so. But I think this is, this is, uh, not an offshoot of that, but I think this is the same. This is, so it's security first is kind of the, the precursors kind of thing. And basically knowing everything that's in your phone and they're going to eventually do custom silicon. They have FPGAs on board. And so Sean had worked on the, he did the FOMU. And so he, he's been on the show before talking about the FOMU, which is the tiny FPGA board that also has the open tool chain that Tim Ansel has been on the show before about talking about. So, yeah. So they're doing really cool things about like knowing your knowing. This is kind of like a know your device top to bottom, kind of like the, this is like the handheld communicator version of the Novena, right? So the Novena was the laptop that they also worked on and talked about on the show before. You know, it's got all these different elements on there that are meant to be like super high trust, super secure. And then as a basis for building that next thing, I think that's why they didn't, I think they explained at some point about why they didn't put a cellular modem on there, but I think it was also because like, you can't, you just can't get access to the silicon and trust it enough that it's not, you know, diving into your data kind of thing. So sweet. Yeah. And it's, you know, it's got a nice keyboard. That's fun. In other news, can we, can we do a news? Did it, did it, did it, did it news? Can we have a, I'm still a little bummed you didn't have more questions for me about firmware, to be honest. I thought you were going to like, I don't know, like you just don't want to, don't want to talk about firmware at all. No, no, no. Okay.

**Dave Jones:** No.

**Chris Gammell:** All right. I'm going to, I'm going to embed it. I'm going to talk to those folks about it. Fine.

**Dave Jones:** You can have them. You're, you're surprised that I didn't want to talk about firmware.

**Chris Gammell:** All right. Fine. Fine. We'll talk about, I'll talk about it on the other podcast too.

**Dave Jones:** If it was 20 years ago. Yeah.

**Chris Gammell:** You know, I'd be talking to like engage you to like talk about, you know, like be like, Oh yeah, I should really do some firmware. Like, you know, like, yeah.

**Dave Jones:** No, no. It doesn't excite me.

**Chris Gammell:** It's not fun. Honestly, I'm a little scared about it. I'm a little, you know, like it's a lot of, uh, you know, getting better, but it's, uh, yeah. Yep. No, I'm not that excited. Sorry. All right. Well, that's fine. That's the thing. So like, I also think about this. So like, and you know, we can find realms of electronics that are, that are firmware free, right. Or firmware simple or all these other things. But I just, you know, from a work perspective, from a things I want to build perspective, I just can't get away from it. I don't know. And some of it is of course, because I'm dealing in like IOT ish type things.

**Dave Jones:** Of course. It's, it's impossible. It's the field you're in. No, there's, there's other fields that you can go your entire career without touching firmware.

**Chris Gammell:** Right. Right. Exactly. I mean, like the, if you, and especially if you specialize too, like the, some of the analog folks that I knew at Keithley or when I was doing some of the analog stuff at Keithley, it's like, yeah, they were just 30 year analog veterans or RF people that were just 30 year RF veterans, you know? And it's just like, yeah, I want more Dave. I want to do more of it. So, all right.

**Dave Jones:** Anyways, knock yourself out.

**Chris Gammell:** All right.

**Dave Jones:** All right.

**Chris Gammell:** So what's the next thing you want to talk about?

**Dave Jones:** Can we have a moment's silence, please? It's not electronics related really, but.

**Chris Gammell:** Oh, no firmware, but let's talk about something else.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** Totally.

**Dave Jones:** Why not? You get to indulge your firmware fantasies. I can indulge my space.

**Chris Gammell:** It's not really fantasy so much as life, but yeah.

**Dave Jones:** Anyways, this is my space and astronomy and moment of silence. What a silence for the Arecibo radio. Tell us, did you see the video? They actually had a drone. It just, I just saw it this morning. They had drone footage. They happened to have a drone in the air when the thing collapsed.

**Chris Gammell:** Yes, I did see it because I think you retweeted my retweet.

**Dave Jones:** Oh, did I retweet? Oh, you're right. I was just in a hurry this morning. I saw it on my Twitter feed. I don't know who I was retweeting.

**Chris Gammell:** Yeah, it's pretty cool though. I mean, like there's another view of it too, where there's, there's a view from the ground where you actually see the entire thing. Really? Okay. I haven't had a look. And if people don't know what we're talking about here, this is in Puerto Rico. This is better known as the site of Goldeneye when the last scene where, you know, James Bond's running along the pathway out to this thing and it's supposed to be controlling the Goldeneye satellites. Yeah. That's the popular culture reference, but, but the actual thing is like.

**Dave Jones:** It's also in Carl Sagan's Contact as well.

**Chris Gammell:** Oh yeah. Right. So why don't you explain what the telescope is though, if people don't know.

**Dave Jones:** Oh, it's, it's a, it's the world's biggest radio telescope. It's built into a natural divot in the ground. Right. I can't remember the exact width of it. It's like, was it 300 meters or something? It's absolutely enormous. Right. There's no way you can build that bigger dish without, you know, building it into the ground. There's no way you can have it up on a pivot point and then pivot the thing around. Right. So what they do is they built the big dish into a natural, you know, crater in the ground. And then the, then they've got these three gigantic cables that come over for the, uh, for the receiver on top and or transmitter. Right. And then that's the thing that moves like normally, normally you steer the dish. Right. But because this is a fixed dish in the side of the mountain, you can't steer it. Right. So the way they steer it is to move the, uh, you know, it, it, it has a name and it escapes where we're, we've both been there. We've both been to the, you know, the Canberra deep space network. So we should know the name of the thing at the top, the head, you know, bit. And so it's, that's what they steer, right? So there's giant cables that can move the head around so that the focal point is different on the dish. Right. So that's how they steer it.

**Chris Gammell:** Right. This is your, uh, this is your algebra class, right. Of like, yeah, it's a, you know, like geometry, I don't even know. Like it's a, yeah, I guess it's geometry, but like the problem.

**Dave Jones:** I think it's a Casa grain. I think it's Casa grain. Oh yeah. Interesting. Okay. Anyway, uh, I could, I could be totally balls on that one up, but anyway, um, it is, it is, uh, actually the world's, uh, largest radar transmitter as well. So they actually do radar imaging of asteroids and planets and stuff like that. They can actually get ridiculously high resolution radar maps of these one, one kilometer wide asteroids, you know, and stuff like that. It's the only dish in the world that can do it. Yeah. Uh, and yeah, anyway, it's, it was built in like the 1960s and basically they cut the funding by like 90% of this thing. And so they couldn't maintain it. Uh, the time to maintain it was like a decade ago. They're screaming out, look, this thing needs maintenance. It's a big, you know, huge mechanical beast. Right. Right. These giant cables. And no, um, one of the, you know, and it famously, like, I think a couple of years back there was some damage to it or something. It's been having problems over the years. And then like six months ago or whatever, uh, made all the news because, you know, um, one of the, like the part of the superstructure of the dish actually collapsed or whatever. And now they just released a report last week saying, sorry, it's too dangerous to even try and repair it now.

**Chris Gammell:** Right. Like how would you get near it without it? Like knowing it's not going to snap or whatever.

**Dave Jones:** Knowing then these cables, they're all fatigued and they're measuring the loads on these cables and they're going, shit, this is like, the load is like twice what they're designed to take. And then as one cable snapped, um, it put extra load on the other cables and stuff. So yeah, it's just, but what a great call that the team who evaluated this said, no, it's too safe to even work on it. Right. Sorry. It's, it's too unsafe to even work on it. And sure enough, like a week later after that report came out, it collapsed the whole thing. The cable snapped and well, it actually pendulumed or something. I have to watch the video again. I haven't.

**Chris Gammell:** If you look at, I just dropped the link in the, uh, the, the closer one or the better view. So yeah.

**Dave Jones:** Yeah. Yep. Okay. All right. Here we go. Let's, let's, let's have a look. Hang on. I'm watching. I'm watching. Oh, look at it. Whoa. And a pendulums. Yep. A pendulums on the two cables. Yep. Yep. And then one of them snaps. Oh, wow. Wow. Oh, and the tower went to, did it? One of the towers. Oh, wow. Wow. That's, I'm retweeting that one now.

**Chris Gammell:** Retweeting. Yeah. I mean, there's just a lot of failures. That's insane. It's a lot of.

**Dave Jones:** Yeah. But the interesting thing is apparently what triggered it is an earthquake. There was, it, you know, it can't be a coincidence that they, they actually time correlated an earthquake. It was only a small little tremor thing. Right. But apparently these cables were so old and so overloaded that that's all it took was one little vibration and it just boom. And it just, yeah, it snapped it. Yeah. So, wow. Wow. And everyone wanted to save it, of course. Why don't you save it? And they went, nah, sorry. It's too dangerous to even work on.

**Chris Gammell:** Well, what about like the, cause there's the square kilometer array right down in South Africa.

**Dave Jones:** And Australia has a square and Australia has a partial one. That's right. Which is the merchants and merchants and wide field array or something. It's called. Yeah.

**Chris Gammell:** Yeah. I mean, so you're talking about like some of the functionality is specific to this implementation. So it's like, you're not going to replace that, but, but some of the coverage they are going to be able to go otherwise. Right.

**Dave Jones:** Oh yeah. For some things, but other things like radar mapping, this is the only dish in the world that could map high power objects with map, map objects with high power radar. I believe anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** So yeah. At, at this sort of scale. So, and I also tweeted out last week when the news said that they weren't going to fix it. I did the comparison. I did the calculations. You can build six, I think five or something for a four or five brand new Arecibo telescopes around the world for the price of what a Virgin Hyperloop are wasting on their stupid new Hyperloop center.

**Chris Gammell:** Your favorite topics. Yeah.

**Dave Jones:** Yeah. Yeah. That's. Yeah.

**Chris Gammell:** But Dave, how do you sell that? You know, is a. I know you can't sell it. Exactly. It's a hole in the ground. Is that as sexy as a vacuum tube with.

**Dave Jones:** That's not as sexy as a vacuum tube with rich people shooting through it. Yeah. Which is not going to happen. Yeah. Yeah. Yeah. That's going to be 500 million bucks wasted. So. Yeah. Totally. Yeah. Anyway. Um, oh, so you actually agree with me. You, you agree that Hyperloop's bunk.

**Chris Gammell:** Yeah. I don't, I mean, I don't really have, I don't have a hard take on it to be honest. Right. Okay. Right. Yeah.

**Dave Jones:** It just, the vibe, huh? The vibe is like, you know, I mean. Yeah. You're not going to get me in a, you know, a 200 kilometer long vacuum tube, you know?

**Chris Gammell:** Oh, well. Okay. So they, so actually when Rahm Emanuel was like the mayor here, it was like here in Chicago. Yeah. Like that was like one of the first spots they were talking about, like going from downtown Chicago. Yeah. Out to O'Hare, which is like a, I don't know, 40 kilometer distance or something like that. It's, you know, it's a long drive for rich people that are in the city that want to go to the airport kind of thing. You know, like it's like, oh.

**Dave Jones:** They did this in Singapore. The, um, sorry, Shanghai, the Shanghai Maglev does that. Yeah. 30 kilometers to the airport.

**Speaker ?:** Yeah.

**Chris Gammell:** Right. But they, everything's built out here and they're not, there's no way they're going to eminent domain, like all, you know, an actual train. There is a train line that goes there. It just takes, it takes an hour from downtown. Yeah. Yeah. Yeah. I mean, like they should just put a, you know, there's just no way to do a express line. And so. No. So Elon came to town and he was talking about, oh, well, we could dig under the crown and you know, it was just big news silliness here. It's stupid though. Like Chicago can't afford anything, let alone a tunnel, you know, like, and it was just, it's just such a quagmire that like, I, I, I'd take a lot of these things with grains of salt and like, I'm sure they're going to build one at some point, but like, is it worth it?

**Dave Jones:** No, it's not. I will go on record as saying there will not be a functional one. Uh, transporting humans. I, I, you might get some stupid thing. Yeah. Yeah. Yes. Yeah. Yep. I, I just think the, the number of engineering. Yeah. It's possible. You can do it. Right. But if you just look at the engineering involved in it, it's just ridiculous for the benefit you get. Just put in standard maglev. Right. It's just, you know, there's just not enough advantage for all of the problems that go along with it. There's just, you know, it's, it's, it's not five times faster. Right. It's in fact, it's, it's only, it's not even twice as fast. Right. It's a, well, well, let's just know it's borderline twice as fast. Right. So it's twice as fast as regular maglev. Right. Even, but not as a high speed trains, high speed rail is even closer than a maglev at the moment. But anyway, let's say it's twice as fast. Right. Uh, okay. But all as, but.

**Chris Gammell:** But the cost is.

**Dave Jones:** Well, no, it's not just the cost, but all the, not only the cost, the safety, the maintenance and everything else that goes into keeping a low pressure vacuum system like that for, you know, a hundred or a thousand kilometers. Right. That's insane enough. But the fact that then you have to go through all these airlocks and stuff like that, you have to go through an airlock. Then you've got to pump out the, you know, the back, all this takes time. Right. So all this supposed high speed, and then you've got to get up to speed. Right. So I actually calculated that you, you need, like I've been on the Shanghai maglev. Right. At 430 kilometers an hour. Right. That's how fast it goes. Right. But you only get to do that, that 430 Ks for like a minute. Right. Because you, you, you have to accelerate up to that and you have to decelerate. And the limit of that is human endurance. Right. People don't want to be uncomfortably shot off at five Gs. Right.

**Chris Gammell:** I know all about that from, uh, from science fiction. You know, you listen to some hard sci-fi and you're going to turn, you're going to learn that, you know, halfway through the journey, you turn around and start decelerating, you know, at the same rate.

**Dave Jones:** Yeah, yeah, exactly. And, and so that's the thing. So all the time. Right. Um, so all that supposed extra speed doesn't gain you much advantage, especially when you've got to go through airlocks and safety procedures and all sorts of stuff. Whereas the Shanghai maglev, it just turns up, you hop on a minute later.

**Chris Gammell:** And it's bigger. And it's also, yeah.

**Dave Jones:** And it's just bigger. It carries more people. Like, and it's a proven existing technology.

**Chris Gammell:** Yeah.

**Dave Jones:** I mean, I like it for what? Twice as for twice the peak speed. No, it's just, no, it's dumb. It'll never happen. It's money. Well, it's money down the hole guaranteed. And they, and they new center, they new development center. They new are in design center.

**Chris Gammell:** You got to shut down firmware. I get to shut down this thing. This is a, we get it.

**Dave Jones:** Like nowhere. It's just, no, no. All right. All right. Enough. All right.

**Chris Gammell:** All right. All right.

**Dave Jones:** I just wanted to go on the recorders if I haven't on the show before.

**Chris Gammell:** You have on Twitter. I've seen it on Twitter.

**Dave Jones:** I have on Twitter. I don't think I've done a video. Oh, maybe. Yeah. I've done a partial video. I've done one hyperloop video on the second channel. Yeah. Okay. Consider me shut down.

**Chris Gammell:** Okay. I'm pairing. I don't disagree with it. So. Oh, wow.

**Dave Jones:** Which is a shock. I'm absolutely stunned.

**Chris Gammell:** I think it's a, yeah, it's a good logical argument. I think it's just, you know. Yeah. Okay.

**Dave Jones:** Yeah. Right. But you haven't, you don't care about the details. You just go. Yeah. That's the thing. Probably not. You know.

**Chris Gammell:** I mean, here's the thing. I live in a city that's so like backwards in terms of just like getting construction done, just like regular road construction. That's like, you know, I look at like, I look at China. Like there was an animated GIF of a train, like a, like a maglev train, you know. And there's like a, you know, so Kane Shea, he does old machine pics. The Twitter account. And so basically it's like these amazing, you know, industrial processes and all these things that are like animated GIFs of that sort of thing. And so, but there's one where there's this train element that comes and like basically lays down a, it can extend itself and like cantilever it so that it actually gets to the end of a bridge that it's building effectively. You know, all of the concrete barriers.

**Dave Jones:** Yes, I retweeted that the other day. Yeah.

**Chris Gammell:** Oh, maybe I saw it from you then. Yeah. Yeah.

**Dave Jones:** I think you probably saw it on my timeline. Yeah. It builds its own bridge.

**Chris Gammell:** Yeah. But that is so far out of like the capabilities of like, you know, Illinois building and like funding and like just, there's so many layers in between that I'm just like, I, it doesn't, it doesn't register for me. It's like, it's like, you know, someone being like, oh, well you can get 5G on your, your new circuit board. And I'm like, I am just trying to get an LED to blink, you know. I'm just trying to buy some PCBs here, you know.

**Dave Jones:** Well, well, well, if you want to make stuff happen, just go for communism, you know, knock yourself out. Yeah. And it's easy then. Right. You just, yeah. Good luck. Yeah. Yep. Right. The great reset.

**Chris Gammell:** Yes. Wow. Sorry.

**Dave Jones:** Yeah.

**Chris Gammell:** Speaking of parts though, have you been noticing that like.

**Dave Jones:** Speaking of parts.

**Chris Gammell:** Well, I was talking about LEDs and trying to pivot away from you talking about communism and

**Dave Jones:** the great reset. And come on, I'm going to drag you into it.

**Chris Gammell:** No, you're not.

**Dave Jones:** All right.

**Chris Gammell:** But. All right. Uh, supply chains are just like out. Oh. Like crazy.

**Dave Jones:** I, I, I do have a, a proper segue for that.

**Chris Gammell:** Okay. I'll take any, I'll take whatever you got, Dave.

**Dave Jones:** Yeah. Okay. My, my latest rant video, right. I bought this new DJI. Ah, that thing. I saw that thing. Pocket 2 thing. Yeah.

**Chris Gammell:** No, that's, that's not related. That's a firmware thing. You don't want to talk about when we talk about firmware.

**Dave Jones:** No, it's not a firmware thing. It's a, it's like, it's a paradigm change. Like I bought a camera and the camera stopped working after five uses. Yeah. Until I actually install this spyware app and register it and provide all my details. Then my product that I paid for. Yeah. I get it.

**Chris Gammell:** I get it.

**Dave Jones:** Right.

**Chris Gammell:** So this was not tied to supply chain. This is tied to China.

**Dave Jones:** Oh no, no, no. This is. Yeah. No, this was tied into the whole great reset thing. Got it. Got it. Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah.

**Chris Gammell:** So you were trying to just drag me into that still. You just don't.

**Dave Jones:** No, no, no. I'm not trying to drag you. I'm trying to drag you more into the side of. No, this is the way products are going. Right. This is the way that they're going. And this impacts all of us. Right. Is that, you know, like you don't buy things. Any, like you don't buy and own something anymore.

**Chris Gammell:** I don't buy stuff from, I don't buy stuff from DJI either though.

**Dave Jones:** No. Well, that was the first time I ever did. And I didn't give it a second thought. I thought, oh, I'm buying a camera. It says video to the SD card and that's it. You know, it's like, oh yeah, I might have to plug in the USB if I ever update the firmware. You know, that's like a thing. Right. But no, it literally stopped working and bricked itself after five uses until I, you know, I've got no option. Yeah.

**Chris Gammell:** You gotta, you gotta hook it in.

**Dave Jones:** Yeah. No, it's bullshit. It's like.

**Chris Gammell:** Well, send it back. I don't know. Like don't, don't support that.

**Dave Jones:** You know, that that's what I'm doing. Yeah. A lot of people said, um, a lot of people said, oh, I do a video sledgehammer in it. You know, why do they arise in it? And I thought, well, that doesn't send them a message. You know, if, if everyone sends this stuff back, then that sends a message. Yeah.

**Chris Gammell:** I mean, I think that cheap part, you know, so I let it see a lot of cheap hardware out there, right? There's a lot of cheap hardware in the ecosystem. Some of it is just because it's, you know, it's built to design to be low cost. But if it's like, if it's cheap and you don't know why, and it does crazy things for you, it's like, oh, okay. Well, where's the money really coming from for this thing? Like, not to be like, that's not like conspiracy ish. It's just that like, there's probably some other revenue stream in there. So like, if it's like, so if you go and get like a Google home speaker and 20 bucks, it's like, and you look in it and you're like, there's probably $20 of parts in here. Yeah. It's like, they're making money some other way. Right. And it's just like, yeah. I mean, if, you know, if, if you, if you're not paying for it, you're the product kind of thing and I think that's, yeah, that, that is definitely the, I worry more about the consumer sentiment around it and like the expectations, of course, you know, like people being like, oh, well it has to be 20 bucks. Why isn't it 20 bucks? And it's like, the way that I deal with it is I just kind of opt out. I'm like, well, I'm going to pay for the prosumer version of it, or I'm going to, you know, if I'm designing stuff, I don't design stuff for the consumer market because there's no way I can get the volume or the, uh, you know, the, the timeline for that sort of stuff. I'm not playing that game, you know, that's, and, uh, yeah, hardware is more expensive and hard to get. That's, that's what I was trying to say is hard to get to parts are hard to get these days, Dave. I don't know if you know that.

**Dave Jones:** So, but yeah, like lead times and stuff have been killer. Apparently.

**Chris Gammell:** Yeah. Jeez.

**Dave Jones:** It reminds me of the nineties, you know, and, and, and the days of Maxim, you know, like, you know, 40 weeks lead time. It's like, that's right. I think that's what's coming back.

**Chris Gammell:** I seen, there was a, so I was looking at the CM4, the, uh, the, actually the one that we talked about here earlier, the, uh, the ethernet RF thingy, that's the compute module, right? I was looking at that for a project I want to do.

**Dave Jones:** Right.

**Chris Gammell:** And yeah, some of the, some of the modules you can't get till May, you know, it's just like that's six month lead time type of thing. And some, some you can write it as swappable, whatever, but it's like, yeah, they're just kind of way out there. It's just crazy because I think.

**Dave Jones:** It was only last year that we were joking about on the show. I'm sure about how that was such a thing of the past, how these long lead times were a thing of the past. Yeah. You know? Oh yeah. I remember that when I was a boy, you know, and, and like, no, it's, it's, it's back.

**Chris Gammell:** Yeah. Wow. Yeah.

**Dave Jones:** So, yep. Hmm. Whether or not, is that going to be a temporary, you know, cause like half the world's shut down with COVID, you know, Australia's doing fine. We should start up manufacturing again, you know? You should.

**Chris Gammell:** Yeah. Try it, man. See how it goes. Yep. Yep. Yeah. That, uh, have you looked at the, the compute module, the Raspberry Pi compute module?

**Dave Jones:** I've had a quick squeeze at it. I'm thinking about designing a custom board for it. So we'll see what happens.

**Chris Gammell:** I've started to do that for a project I'm, I'm working on and, uh, yeah.

**Dave Jones:** It's still, it's still not the best bang per buck. Like it's like, if you want, you know, there's, there's others out there that have better processing bang per buck than the Raspberry Pi. Oh, sure.

**Chris Gammell:** Sure. But can you buy them? Well, like what's a, what's an example of that?

**Dave Jones:** Oh, like the, um, you know, like the, instead of the Raspberry Pi, you get the orange Pi and stuff like that. Right. So they said they're not quite compute modules, but you can, you know, there's no reason like there's, you get more bang per buck in like an orange Pi than a Raspberry Pi, for example.

**Chris Gammell:** I see. Yeah. Yeah. Yeah. But this is, I mean, this is the actual like compute, like the module. Yes. This is a, yeah. This is a compute module. It's actually integrated to a product and you know, you have to run.

**Dave Jones:** It doesn't just use a pin header anymore. Or it uses a high speed, a, um, uh, a Samtech, a high speed connector. Yeah.

**Chris Gammell:** Like a mezzanine connector. That's right. Yeah.

**Dave Jones:** Mezzanine connector. So that now, which, which means you can't stack them vertically now, which is kind of annoying.

**Chris Gammell:** You know, you can't like. Well, you could though. I mean, you could basically, you could put them side by side. You could. Yeah.

**Dave Jones:** But you'd have to design another daughter. You'd have to have a yet another plug mezzanine board to plug into the, to plug your compute module in that then plugs into the motherboard. You know.

**Chris Gammell:** Why would you want to stack them vertically?

**Dave Jones:** I don't get that density for a cluster.

**Chris Gammell:** Oh, I don't do that. No. Yeah.

**Dave Jones:** Exactly.

**Chris Gammell:** Yeah. I think that that's probably the, a good point though. Like it has. So the form factor has switched away from a vertical to a horizontal. Well, yeah. So in like a so dim, so you could, you could have plugged them into like row, row, row, row, row, but yeah, this would have to be side by side or some other way. But yeah, I think this is, this is interesting. Interesting. Your way to do it. Yep. I've been, I've been looking at it. And so there's a friend sent me the high speed layout guidelines for signal conditioners and USB hubs. They're like a TI app note. Yep. Highly recommended. It's nice, friendly, big, friendly diagrams. Good, good background info all about, you know, high speed reference plane, stuff like that. So if you're, if you're getting into it, I do recommend that, you know, looking through that, it's a, it's a really good resource for, for, you know, control impedance, differential pairs, things like that. Cool bananas. Caps in the right place. All the stuff that Dave already knows about that. Yep. Yeah. Yeah. You should make, you should make a board though. It would be interesting to hear your take on it. You could use, actually you could use a version six of KiCad.

**Dave Jones:** It's a, I was going to say, because they actually provide, that's the other thing. They do actually provide a KiCad files, don't they?

**Chris Gammell:** That's right. Yeah. The IO board is in version six.

**Dave Jones:** So they provide a template. They, yeah. That they provide it.

**Chris Gammell:** No, it's the actual board that they make. They make the, they make the IO board. So it's basically like, yeah. So the board itself, the, the module itself is, is in.

**Dave Jones:** Oh, so the entire board is KiCad.

**Chris Gammell:** Well, the entire IO board. So like the breakout of all the signals.

**Dave Jones:** Oh, the breakout of the signal. Oh, okay. Right. The reference. Okay. Not the actual Raspberry Pi itself.

**Chris Gammell:** Right. Exactly. Right.

**Dave Jones:** Cause that's all closed source. The Raspberry Pi is not an open source design.

**Chris Gammell:** That's right.

**Dave Jones:** They don't release schematics. They don't famously release, you know.

**Chris Gammell:** Yeah. So you can access to the headers and things like that. But yeah, if you're, you're not going to be able to buy, you couldn't buy the chip, you couldn't buy the BCM chip anyways, the Broadcom chip. Right. Okay.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** But this is kind of like the next best thing. And the IO board is open source and you can get the files and stuff. So yeah, it's, it's a nice, it's a nice change. It's a, the only downside is if you are in version six, you can't go back to five. So just keep that in mind.

**Dave Jones:** Oh, really? Okay.

**Chris Gammell:** It's a, it's a one-way trip. So that's why I have it on a VM because I don't want to, I don't, I'm not going to, I'm not moving my other designs there yet. So I don't do that until, until V6 is solid, which is probably early 2021. So.

**Dave Jones:** Yep. We're getting there.

**Chris Gammell:** We're getting there. Cool. But yeah, you should do it. It's a, it's cool. I mean, it's a, it's a good opportunity. This is a great app note. You can go over this app note in your videos and stuff too. It's like.

**Dave Jones:** Awesome.

**Chris Gammell:** Good stuff. And like when Jay.

**Dave Jones:** Link it in to the show notes.

**Chris Gammell:** I do. I will. I will. When, when Jay was on the show too, you know, he talks about a lot of this stuff. He was talking about his, so Jay Carlson was on the show. The student he was working with, you know, was doing layouts of DDR memory and stuff like that. And it was just like, you know, it's, it is this commonplace thing, but it, there's a lot of question marks around it. I've always had a lot of question marks around it too. And it's like, it's just becoming more commonplace. And so like even doing controlled impedance traces out to like an HDMI, you know, connector or something like that. You still have to know some of this stuff, but it's just becoming more accessible. And that's probably easier than DDR3. And like Jay was saying, the DDR3 even is easier than it used to be. So I think that that, that's all a positive direction. And so like showing that kind of stuff is, is easier and figuring it out. So yeah.

**Dave Jones:** Cool.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. Our amp hours up.

**Chris Gammell:** Oh, it is. What do you know?

**Dave Jones:** Yes. No, there you go. Flew by. So, yep. Just remember this. I'll leave you with a final thought in, in the future, you will own nothing and you will be happy.

**Chris Gammell:** Do I agree with that? I don't agree with that. I definitely won't be happy.

**Dave Jones:** So you, so you're against the great reset. All right. I had to get in there. It's fun. Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** Yep. All right. I will go and buy my own pick and place machine before I can, can't own anything anymore. Okay.

**Chris Gammell:** Yeah. That'll make for some great video. So you should do it, man. Get yourself a charm high.

**Dave Jones:** In my new charm high. In my dodgy charm high in my new 50 square meter lab. Yeah.

**Chris Gammell:** Hey man, you know what you could do? You could loft it. You could like put it like on a winch cable.

**Dave Jones:** A hoist. Yeah. The hoist. A hoist. Right. Exactly.

**Chris Gammell:** So past guest, past guest Todd Bailey. he did this with his bed in his Brooklyn loft. He actually had a winch that like lowered the bed up and down. You could basically just build this thing when it's not in use, goes up to the ceiling. Yep. Yep. And then when it's, when you need it, it comes down. Yep. I mean, you can do this with a train set too. You can make it, you can make a whole second level in your lab, Dave. You know, you could really,

**Dave Jones:** you could really optimize. I could do it in the bunker. I got tall ceilings in the bunker. I could, I could have a whole mezzanine. I could build a mezzanine level in there.

**Chris Gammell:** Build a second level. There you go. Yeah. Yeah. Yeah. Collect all the crap that you already collect. Yep. All right. Well, see ya. Catch you next time. If you dig into the programming manual of today's episode, you'd see a register set that is maxed out by default. And that'd be the generosity of our patrons. Join the club at patreon.com slash the amp hour and join our discord. So Chris has someone to talk to about firmware. A special thanks today to our corporate sponsor. Bino.

**Speaker ?:** A special thanks to our administered administered in administered administered in administered administered in administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered
