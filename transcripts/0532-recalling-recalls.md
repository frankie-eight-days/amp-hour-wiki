---
episode: 532
title: Recalling Recalls
url: https://theamphour.com/532-recalling-recalls/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released February 28th, 2021. Episode 532. Sponsored by Keysight Technologies. Recalling recalls.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. What's up, nerd? Hey, man. I saw your new fancy toy, your new video fancy toy.

**Dave Jones:** My new video fancy toy, 18 mini.

**Chris Gammell:** Got a little jealousy going on inside the pond. Yes.

**Dave Jones:** Well, I had known about these, but you sort of like prompted me, hey, are you going to get one of these?

**Chris Gammell:** Yeah, the newer version was cool because it's got the individual channel recording, which is very...

**Dave Jones:** Yes, that's right. I didn't know about the individual channel recordings. People don't know what we're talking about. The Blackmagic, designed in Australia. I'm not sure if it's made here.

**Chris Gammell:** It doesn't actually have where it's made on it.

**Dave Jones:** So I'm not... Yeah, I find that really annoying. Anyway, I do know they do make stuff here, but I don't know if like Rode, they make almost everything here.

**Chris Gammell:** Oh, really? Okay.

**Dave Jones:** Anyway, yeah. Blackmagic, yes, they've got their cinema cameras, of course. They do famously, you know, it's not like your Sonys and your Canons are the only ones who make cameras. Yeah, a little Blackmagic in Australia make them too and they're bloody good.

**Chris Gammell:** Yeah.

**Dave Jones:** Absolutely incredible. Well, they make all these video switching equipment and stuff and this is a little, you know, four HDMI inputs to HDMI output, plus it simulates a webcam and it does live streaming. And as you said, the new ISO model records all the raw footage to a solid state USB drive, which is, you know, really cool. So it's like a one-stop, you know, editing shop for streamers and, you know, people like us who make content.

**Chris Gammell:** I think, well, I think even these days, you know, so many people have to do, like, I think about internal trainings at companies, you know, it's just like so tough to, you know, there's a ton of new web tools for this sort of thing. But just thinking about like, if you were training, if you were trying to train up like your coworkers these days, you need to do it all remotely. Most people aren't geared up for that and it's just, I think this is one of the silver linings of the, you know, everybody being remote is just like there's more tools coming out. There's more servicing of remote video needs. So that's a nice little bonus in all the shit that's happening.

**Dave Jones:** The thing I really like about it is that it's a hardware solution because, you know, I use XSplit for my recording. I also use OBS as well. You know, most people use OBS, but I've been using XSplit for years. They're basically identical bits of software. They're OBS copied the XSplit interface and stuff. But anyway, yeah. And they're always having, I'm always having problems with it. It doesn't matter if it's OBS or it's XSplit. There's always, you know, it's a PC. You know, PCs are just a pain in the ass. They, you know. Yeah, they're general purpose computers. Yeah, they're general purpose computers. They crash and they're not, yeah.

**Chris Gammell:** The right tool for the job, right?

**Dave Jones:** No, there's so many layers of software complexity just to do a screen capture or just to record your microphone. It's just nuts. Whereas this hardware, this is like a dedicated box. It just sits on your bench. It powers on instantly and you press record and like, and it goes. And it just records the audio and video and you can do the live camera switching. And if you need to edit later, it can, you know, it has the raw copies of all the files. But geez, so I'm yet to set it up because there's actually quite an effort to set up. I was just talking. It'll probably take me days till I set it up properly and get it.

**Chris Gammell:** Well, you have torn it down though. And I like that.

**Dave Jones:** I have torn it down. And here's the interesting thing is people think, like, because this thing's tiny, you get it. And it's just this little tiny box with a bunch of buttons and a few HDMI inputs. And you think, oh yeah, it should sell for a hundred bucks. No, it's actually 1200 bucks, right? Aussie bucks. And it's like, wow, where's the cost? And you open it up and you go, wow. Okay, here's the cost. It's got an $1,800 one-off price from DigiKey, of course. But it's got the zinc, the Xilinx zinc. It's got one of the top of the line zinc chips in it. And it's like, it is $1,800 one-off cost. Just from DigiKey.

**Chris Gammell:** So that's what I wanted to bring up about it too, is I love that you took it all apart. You saw that there's a zinc in there. I feel like this is one of those things too, where you hear about these parts, you hear about FPGAs, high-end FPGAs. And you're like, what are people using with these things? And I feel like this is maybe a perfect example for it.

**Dave Jones:** It is. I think so, yeah.

**Chris Gammell:** Yeah, it's got four channels, right? So it's doing four channels of high throughput video. And so whenever I think FPGA, I think high-end FPGA, I think of like data pipelines. And that's almost- Data throughput is one of the big things.

**Dave Jones:** You aren't doing it for just like the old CPLD stuff of like logic switching, just replacing a few chips. No, it's data processing, data throughput, parallelism.

**Chris Gammell:** Right. And so there might be inline encoding. There might be inline mixing. So thinking about you have two video streams of high data rate video that's getting mixed together, overlaying. You think about fading from one image to another.

**Dave Jones:** Fading one to the other. Chroma key in doing the green screen. I speculated this in the software. Would they be doing that in the FPGA, the chroma key in? Or would they be doing that in- Because this thing has six ARM processors in it. Right. Six. It's got four applications processors, as they call it, applications in quote marks. And it's got two, or it might be the other way around, two real-time processors. And one's an ARM A53 and the other's an M3 or something, Cortex or whatever. It's got six bloody hard processors in it. This is insane.

**Chris Gammell:** Yeah, it's crazy.

**Dave Jones:** Yeah. No wonder this thing is $1,800 one-off price for the chip. Well, yeah.

**Chris Gammell:** I mean, they're not simple parts at the very least. No.

**Dave Jones:** Absolutely incredible.

**Chris Gammell:** And so then on the four, the quad-core type processor, very realistically could be running Linux on there as well. So then you have some kind of handling for all the USB stack and the Ethernet stack and stuff like that.

**Dave Jones:** Well, is that a coincidence? There's four application cores and there's four HDMI inputs. Is that a, you know, is that a clinkidink, right? And there's two other real-time cores that can just run all the background stuff. So maybe they do actually dedicate an ARM core to doing like green screen and stuff like that. Maybe. Yeah. Yeah. Who knows?

**Chris Gammell:** But I would think that that kind of stuff is, you know, probably running Linux and probably doing general purpose. Oh, I'm sure it's running Linux. Just because then you can start to run, you know, you could write to write software that's, you could simulate elsewhere instead of having to run it on device and that sort of thing.

**Dave Jones:** Yeah. It just makes the development much, much easier.

**Chris Gammell:** Yeah. I think. And then, and then from a, you know, again, like I think the other thing that's exciting about this sort of thing, you know, there, obviously there's FPGAs out in the world. I always think about the military applications, any kind of vision type thing. There's tons of FPGAs. And those, again, because of these like pipelines.

**Dave Jones:** We've, we've used them for beamforming when I was in the military, you know, all the underwater sonar, you know, that's one of the classic cases is, you know, yeah, you've got like, you know, 2000 sensors coming in. Convolution matrices. And yeah. And it's just when you've got to do beamforming of a couple of thousand or a couple hundred sensors, you know, it's like, yeah, you do that in an FPGA. You don't want to be doing that in a sequential processor in environment. It's just not.

**Chris Gammell:** Right. It's not going to work. Yeah. So that's cool.

**Dave Jones:** Well, you can get it to work at like, you know, what, you know, two frames per second or something like that. Right. But you can't get it working in a real time sort of thing. So, yeah.

**Chris Gammell:** Yeah. Well, and so the other thing I wonder about though, is so, you know, you've got this application side processor, maybe, maybe a full OS on there, that sort of thing. Like, so then a device like that, I, the one you didn't ask this in your video, but I wonder how different the ISO is, right. The one that can actually record it for individual streams versus just the one that streams for and mixes for streams.

**Dave Jones:** Cause I, I did actually mention that in the video. Cause there's a $400 price difference. Yeah. Yeah. It's tucked in there somewhere. There's $400 price difference. I think it's right at the end maybe. And yeah. So it's like, this is where you would not be building in, like you would not have the same hardware. Like you would, like you would put in a different chip, like, because the chip could cost you a couple of hundred dollars difference in the bomb cost between one that's got, you know, X amount of fabric and X amount of cores and X amount of memory and stuff like that. And a lower end one in that same family, you know, there can be a couple of hundred dollars difference. So you're not going to just whack in the higher end one in your bomb. I don't think.

**Chris Gammell:** I don't know. Well, I, I, maybe, maybe, maybe not, but I'm just thinking like if you, maybe you cost down later, but I was just thinking, so I had a different, I had a convergent design Apollo, which was like a similar, like video mixer. Basically it was like what you have there is a video mixer, but it also had like TFT on it with a touchscreen where you could basically touch to switch channels. Right. So some very similar in a lot of ways about two or three X the cost. And it was, came out earlier, but the whole thing was I literally updated. I bought the upgrade to this Apollo version from a different version. And it was literally just a firmware upgrade. And so much like the scope makers do, you know, the video makers do this as well. And they, you know, they release, they release upgrades later. And then they also had these, you know, $400 is not a small, you know, that's, I think you said what, like, like a quarter of the cost at that point. Yeah. Yeah, exactly. Or a third. Yeah. So it's crazy.

**Dave Jones:** Yeah. A third of the cost. Yeah. Just because it literally the only difference between, I think between those two models is that one can live record all of the channels. It can like full, full record all of the channels. Whereas the $400 cheaper one can only record the output stream. It can't record the output stream plus the original inputs. So I think that that is the major difference between it. So I don't know. I, I suspect this might, it would not surprise me at all if they physically use a different zinc.

**Chris Gammell:** Yeah, maybe. Yeah. Yeah. I mean, you're right. It's, it's not a, yeah, that's, that is an expensive part. No doubt about that.

**Dave Jones:** Yeah. Oh, it is, it is 90% of the bomb cost. Right. It's like, yeah. So I don't know. I would love to know that the price that they're getting those for. Yeah. It's 1800 bucks. One off at digi key. I'd love to know, you know, but it's, it's, it's not like it comes down to 20 bucks or something, you know, it's, it's, there's, I guarantee they're still paying a couple hundred bucks minimum. Yeah, exactly. So. That's cool. It's good to know. Yeah. Good. Enjoyed it. Yeah. It's yeah. So they're not, I don't think they are price gouging on that because it's like, you know, I think they're charging quite a reasonable cost considering that other, the, the other equivalent professional gear, you know, like high end stuff, you get to do exactly the same thing. It's like four or five times the cost.

**Chris Gammell:** Yeah. Right. Exactly. Yeah. Like I said, I had one that was $3,500 from a past work and yeah. Yeah. Right. Similar, nothing, nothing, fewer, fewer features and stuff like that too. I think it just came out earlier. So. Yeah. Exactly. I think we're just, this is like, yeah, it just is coming down in price because. You know, parts getting cheaper. Yep. Parts are more accessible, that sort of thing. So. Yep. It's great.

**Dave Jones:** And, and I think probably one of the reasons why you're not going to see like cheap, like clones of these sorts of products is because just the sheer amount of development, software development required that goes into this. I can't imagine the effort that goes into like, it's, yeah, they can copy the hardware, right. You know, some company come along and just copy the hardware, but to really, you know, there's a lot of software and firmware that goes into something like this. There's a lot, crap ton of development that goes into it. So. Yeah.

**Chris Gammell:** I think, I think if you are making products, this is the way, this is the way to differentiate, you know, like to have FPGA bit stream somewhere. You might have a cloner, but you're probably not going to have direct competitors, like trying to rip you off like that.

**Dave Jones:** No. I think. With actually writing their own software. Yeah. Right. Exactly. That's right. Yeah. From scratch because it's just, yeah, it requires a development team of.

**Chris Gammell:** Yeah. And then you do, you know, you also turn on the security features, but you know, even if you do that, you can start to separate yourself from, from the pack with the algorithm differences, feature differences. I mean, at this point, like you could literally get a new firmware build that has new FPGA fabric in it that does something else interesting. Yeah. Yeah. Of course. Maybe it could do 4k mixing instead of 10k, 10, 1080p, that sort of thing. So it's just a matter of efficiency over time. And, you know, when I think about it, I also think about like, you know, software burndown charts, it's like, okay, we've got this thing working. It's out the door. Let's go and update it so that we can add another feature, like a software feature, a true software feature. And yet something that could up the cost or up the selling price rather, because it can do more.

**Chris Gammell:** Yep.

**Dave Jones:** Cool. Anyway. Yeah. I like it. I'm yet to actually use it in anger. Cause as I said, it actually requires a lot of effort to, to set up a proper rig properly. Actually, you know, you've got to have the right cables and they've got to have the right lengths to go places. So I, I probably like, don't have the, like, I have the ability to like cobble it together, but not the ability to set it up nice. I'll have to buy like, you know, dedicated length cables and, you know, things. Cause cameras have to go from one side to the one side of the lab to the other. And, you know, just doing stuff like that. So.

**Chris Gammell:** Yeah. Yeah, man. Got to go and hit that supply chain.

**Dave Jones:** Anyway, that's going to be nice. Yeah. I'm just looking.

**Chris Gammell:** How is your supply chain doing these days, Dave? I feel like we should check in and in the era of Chipageddon.

**Dave Jones:** For a lot of my products, not huge differences at the moment for one, one product there is, but yeah, it's, yeah, it's, it's doing okay. It's just the normal production delays. You know, I put in an order and my product comes in a couple of months later. You know, it's like, I actually need to optimize my warehousing better, you know, warehousing in quote marks, you know, predictive, uh, ordering.

**Chris Gammell:** And yeah. Right. We've talked about that.

**Dave Jones:** Yeah. Yeah. Yeah. Exactly. Because yeah. Like I, I so often I've been doing this for years. It's like, Oh, all of a sudden, Oh geez, I'm running out of stock. Oh boy. It's a two week lead. It's a two month lead time for ordering new meters or, you know, whatever. It's just like, even, even something simple like a test leads, for example. Right. You think, you know, I was buying, buying the Breiman test leads at one point. It was like, Oh, sorry, we, we can't, there are two, three month lead time. It's like for a test lead. Holy crap. You know?

**Chris Gammell:** And that's not even a retract automatically retracting test lead.

**Dave Jones:** Like you, like you said, no, it's not something, something fancy, fancy. No, it's just a regular.

**Chris Gammell:** Something that doesn't exist yet. Yeah.

**Dave Jones:** But it's, I, yeah, it's crazy. Yeah. Lead times anyway. Yep. Yeah. It's tricky.

**Chris Gammell:** I got hit by, uh, uh, my, so there's been ice storms here in, in the States. And, uh, obviously I don't know the power outage. I don't know if you've read about that down in Texas as well, but, uh.

**Dave Jones:** Here's the thing, right? I first learned about this, uh, Texas snowstorm thing from the bit guys. Uh, you know, he does vintage computer stuff. Right. And he did, you know, his house has been ruined. His house got flooded or something. So, so, so that popped up and he went, yeah, in Texas, we're having these snow storms. And I just went, it snows in Texas.

**Chris Gammell:** Right.

**Dave Jones:** Like, I had no idea. Like to me, foreigner, it's like, no, Texas is like, you know, the equivalent to the outback here. It's just, you know, hot desert and bloody. Yeah. I had no idea.

**Chris Gammell:** About every like five or six years. Right. You'll get a freak. They get hit.

**Dave Jones:** Right. Wow.

**Chris Gammell:** I, I, you know, I used to live in Texas.

**Dave Jones:** Is this like Northern, is this like Northern Texas or lower Texas?

**Chris Gammell:** This was all of Texas. All of Texas.

**Dave Jones:** Wow. I thought there would have been like, I thought it would have only been. Oh no, the whole South got hit. This is a really big deal. South of Texas. That's practically on like, that's the Mexico border.

**Chris Gammell:** Yeah. Like, yeah.

**Speaker ?:** What the?

**Chris Gammell:** I have no idea. Weather systems, you know, climate change. It's like a thing. It goes both ways. Really hot and really cold. Yeah. So like, there was like a system that dropped down there and just dumped a bunch of.

**Dave Jones:** Wow. Wow.

**Chris Gammell:** So I used to live in Texas and I have never been as frightened as driving in the roads when there's been like ice. I was like driving a little Honda Civic. Yeah. On the roads with all these Texans with their trucks and. Oh yeah. Yeehan passed me and just like, just seeing cars slide off the road.

**Dave Jones:** Oh, that's scary. Yep. Yeah. Wow.

**Chris Gammell:** So yeah, no, it was very, it was very unfortunate. There was, there was a lot of loss of life, unfortunately as well. Yeah. Yeah.

**Dave Jones:** I saw that huge pileup. Yeah. That was incredible. I saw the video of it. Wow.

**Chris Gammell:** That was just, Oh, not just that. I mean, like just because the power got shut off a bunch of places too. Oh yeah. How extensive you heard about, but it was like the whole Texas grid pretty much got taken down.

**Dave Jones:** And yeah, once again, I only find out, you know, cause I'm not following like us local news or whatever. I only find out because somebody on Twitter, I think it was, uh, Lawrence Krauss or somebody, you know, I follow some physicist and he lives there and he said, Oh, I've been without power for a week now. I didn't know he lives there.

**Chris Gammell:** It's like, he used to be a professor at my, at my university. I don't know if you knew that. Oh, okay.

**Dave Jones:** Yeah. Oh yes. I think you mentioned that. He was the physics professor. Yeah. That's right. Yeah. I know. I think I, well, it's someone I follow on Twitter. I don't think maybe, maybe wrong about Lawrence Krauss, but yeah, somebody said, yep. It's been a week, no power. Holy crap. Yeah. You know, the, the longest here in Sydney, cause I've lived in Sydney all my life. The longest we've ever been without power is probably in like my entire lifetime is probably half a day.

**Chris Gammell:** Do you guys bury lines there or no?

**Dave Jones:** It depends on the suburb, older suburbs. No newer suburbs, which when I say newer, my, my, my suburbs, like 30 years old. Yes. We, we have buried cables. So yeah. Yeah.

**Chris Gammell:** So in Texas, you can't, you can't do that a lot of places cause like it's bedrock. So. Right. Okay. Yeah. So that's one thing. And then, but the real thing was that at the actual, like, uh, so like a lot of the diesel generators froze up and a lot of everything got overloaded and then they have their own grid. And it's just like all this crazy stuff that I don't really understand, but I do know that it was, it was not ready. It was not ready. Unfortunately. So it almost is like an economics thing. It feels like more than a, than it was a, uh, you know, like, like an electrical thing. It wasn't like they, they didn't have the.

**Dave Jones:** You guys have a lot of politics in your grids, in your grid management over there. Yeah. Yeah. It's, um, yes, all of, uh, California shut down. Sorry. Not, not because of a, not because of a, you know, like line problems. It's because of, you know, bartering energy, bartering, trading things. Sorry. You know, it's like, yeah, that was a big thing. A long time ago.

**Chris Gammell:** PG and E has got their own issues out there. Yeah. So yeah, no, it's, uh, it's unfortunate, but it's, uh, I glad it's all back on and people are recovering hopefully.

**Dave Jones:** Yeah. Yeah. It's crazy. It shows how, how dependent we are if, you know, if the power goes out.

**Chris Gammell:** Yeah.

**Dave Jones:** So I, I am up, I am upgrading my solar system. So yeah.

**Chris Gammell:** I wonder if that's going to drive future things like that. So like, you know, thinking about Texas now, I have a friend who works in, you know, the power service industry and stuff like that. And just seeing if they, I asked him if they've seen an uptick and just general interest in it. And he said, yeah, they have seen some more interest in just kind of like it was, this was not a battery system, but you know, just general, like people having this near term focus on power. Yeah. And I do wonder about that longer term of just, you know, people building out their own battery systems that they had a capability and just kind of self-alliance in that way, because it's like, if you can't get reliable power, especially the most emergency times, it's like, Oh, then what? You know, like it's tough.

**Dave Jones:** Well, see, the thing is, it's not just, you know, your life goes back to normal. If you've got a battery system. Yeah. Your, your house stays up. Your fridges are still working and you can still use your computers, but you may not be able to use the internet because that's got to go to the local, you know, it's got to go to the local cell tower. And if the whole state or the whole city's out, like, well, no, you're, you're not going to get phone or internet either.

**Chris Gammell:** Right. It's only if, only if you got, uh, what's the, what's the, uh, satellite Starlink. Yeah. Yeah. Yeah. Yeah. Yeah. Starlink.

**Dave Jones:** I mean, that's another like, you know, sure. No, if you want to be totally autonomous. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. If you're, you're living in the middle of nowhere. Well, even if you're not living in the middle of nowhere, cause as I said, I'm upgrading my solar system, I'm going to be getting a, I'm going to have a total eight and a half kilowatts, I think system now. And it's like, now I'll be able to get a battery because then it makes sense. Whereas before we were using all the energy, having a battery system was pointless. Cause we'll suck in all the energy. You'd never actually use it. Yeah.

**Chris Gammell:** Yeah. Or you never over capacity.

**Dave Jones:** No, no, exactly.

**Chris Gammell:** So then what's your, what's your thinking on the battery side?

**Dave Jones:** Well, yeah, I will. Well, I'll get the solar system installed first. I'll run it for a couple of months. I'll look at how much excess energy we're feeding back into the grid. And then I'll be able to calculate how much where, you know, can actually store and then reuse during the night and stuff like that. But you know, like battery systems aren't cheap and they're probably, they're probably not going to pay for themselves.

**Chris Gammell:** Like, you know, interestingly, one of my, one of my buddies is talking about like solar and battery as like a hedge against inflation. Like, you know, obviously the U S has a lot of economic things right now where we're spending a lot of government dollars and you know, whatever you feel about that. I think more dollars in means potentially higher inflation, but he's like, look, if money's worth less than the future and I buy something that has real value now that actually generates power, then that actually is a pretty interesting idea. I know long-term you've got to think long-term. Yeah, exactly. Yeah. And like, I love that idea personally of just like, first off you get like the nerdy thing of like solar and batteries and like some, like, you know, like resources for yourself. Cool. And then also it gets quote unquote cheaper over time, which is, you know, not, you know, this kind of a mind game, but whatever. And then it also generates power and it's like potentially money. So that's cool.

**Dave Jones:** Well, I ran the numbers on this new system and it's like, well, it saves us $40,000 over the next, over the lifespan of the panels, which is 20 years over the warranty period of the panels.

**Chris Gammell:** Yep.

**Dave Jones:** It's like, you know, it's like $40,000 in, in that that's in, that's in today's money, not in inflation guaranteed inflation money in the future. Cause the way the money printer's going, yeah, it's like, uh, yeah, it's not kids.

**Chris Gammell:** Dave knows memes.

**Dave Jones:** You're not going to avoid that. Exactly. I'm the meme Lord. I'm not quite Elon Musk level, but you know, I, I, I do know my, do know and appreciate my memes.

**Chris Gammell:** Here on the Amp Hour, we look for sponsors who are interested in teaching our audience. This week, our sponsor is Keysight Technologies, who are ramping up a new contest called Stump the Experts, which is focused on Keysight's 5G testing technologies. I had the opportunity to talk with Martha Zameed, who's a longtime Keysight FIE who now focuses on 5G. I started by asking what her typical day looks like.

**Chris Gammell:** I work with customers. I get to see what they're developing and what they're actually, you know, testing. And then I take that into our design team to make sure that our solutions will be able to support what customers are working on.

**Chris Gammell:** Before we stump any experts, let's get unstumped ourselves about how 5G works. Where's Martha focusing in the technology stack?

**Chris Gammell:** My focus is on the physical layer. That's the air interface side of things. The biggest challenge with 5G and R compared to any of the previous generation, one is the frequency that it operates in. With all previous generation cellular technologies, everything operates in the RF, mostly below 3 gigahertz frequency. But because the RF side is pretty populated, there isn't enough spectrum to support 5G and R. 5G also uses millimeter wave technologies. And that's never been used for cellular technologies. So that is a new area for our customers. Operating in millimeter wave does provide you with a very wide bandwidth. There is a lot of spectrum available because, again, it has never been used for cellular technologies. So it provides the operators enough bandwidth to be able to support extremely high throughput. That's the good thing about it. But the challenging part is all the propagation that happens in millimeter wave limits, you know, how far the signal can go. So you won't be able to have as much coverage as you do in the RF frequencies below the 3 gigahertz.

**Chris Gammell:** So what's the hard part about 5G?

**Chris Gammell:** From what I do and from the physical layer aspect, one challenges are the frequency, being able to make measurements in millimeter wave. The other is the bandwidth, right? Now you're dealing with an extremely high bandwidth. Just to give you an example, for LTE, when we look at a single carrier, the maximum bandwidth was 20 megahertz. But now with 5G and R, when we look at it in FAR 2, it's 400 megahertz wide signal. So the challenge is in achieving almost as good performance as an LTE, but at a very wide bandwidth. And you always have to deal with the weather, the bandwidth, the noise that you have to deal with. Having test equipment that has extremely good performance at a very high frequency and at a very wide bandwidth is our own challenge, right? From a testing measurement. And then similarly for our customers, as for their devices and for their base stations to achieve.

**Chris Gammell:** KeySite's new contest wants you to ask questions to stump the experts by recording a short video about a range of 5G and test questions. Early signups can win a t-shirt and contest winners will win consulting time with some of the KeySite experts. Some participants will also win books about 5G. To learn more and enter the contest, head to theamphour.com slash 5G and that'll take you to the contest page. And now back to the show. Did you see Martin Lurton's thing about inspecting solar panels? No. Inspecting them how? I think he shines like a UV light at them.

**Dave Jones:** I saw he developed a... Oh no, I saw he developed a measurement box or something for them.

**Chris Gammell:** Yeah, that was a while ago. But this was... So Martin's been on the show before here and Dave and I... Dave actually introduced me to Martin when he was living in Cleveland. And yeah, he's basically... I think he's doing like... He took the filter off a camera so it captures more UV, I think. Right. And then he's shining light at it and then seeing like these cracks and like... And it actually... He has like damaged panels and it's super interesting. I've never seen anything.

**Dave Jones:** That's fascinating.

**Chris Gammell:** I think he actually mentioned your micrometeor strike. Oh yeah, video. In some of his videos too. Yeah, right. Yeah, so...

**Dave Jones:** Yeah. I wouldn't know that you'd get like invisible micro cracks. So they usually... Oh yeah. They're just... They're either like 100% tough or they completely shatter. Like, you know...

**Chris Gammell:** Yeah, yeah. Yeah, like a spider crack kind of thing. Yeah. Yeah, yeah. It's just... Yeah, it's really interesting. I mean like... Wow. I feel like there's like this whole area there of like... I don't... I don't understand solar still.

**Dave Jones:** Well, and that's going to vary between panels because they've all got different manufacturing technology and you know, they're all made different. And you know, they don't use the same glass. They don't use the same materials and stuff. So it's very different, but yeah, so I'll actually be having a mixed hybrid system. I'll be having sort of like my system will be like two thirds new, which is going to use the micro inverters, right? So it'll use... I'm getting new panels. It'll use the new micro inverters, but I'm going to have my existing system still running. I'm just going to move that to the other side of the roof. So I pick up the morning sun because why? Like it's still a great system, even though it's seven years old. It's still... It'll run for another 15 years at least, you know? Yeah. So I'm going to use my existing string inverter and my old panels. I'm just going to reuse them. Why not? So I'm just going to pay the installer to move it to the other side of the roof so that my... Oh, that's a great idea. So that my new panels can get the best sun on the main side, but yeah. The south side? Yeah. Or whatever the direction is. Well, no. See, my panels, people don't know this about my system. It's not even optimally north oriented. None of this are south rubbish. That's for you weirdos on the other side of the planet. Oh, Jesus. Right? North, right? So you've got to orient your panels north here. That's right. North. North. So technically, we do have an ideal north facing roof, right? Uh-huh. But Mrs. The EV blog doesn't want solar panels plastered right over the nice front of the house. Yes. Yes. So ours are actually on the west side where the sun sets.

**Chris Gammell:** Mrs. Contextual Electronics has expressed this when I've said...

**Dave Jones:** She said the same thing?

**Chris Gammell:** She said... She's like, look, when we buy a house, you can have solar if there's a garage that faces the right direction.

**Dave Jones:** I'm like, come on. Okay. Yeah, yeah. It's free power. Yeah. Yeah. See, because we've got nice tiled roof. You know, we've got like a nice looking tiled roof and she doesn't want it like plastered with... So even though she's like an eco nut and she doesn't, you know, she loves the solar. She just doesn't want it ruined. Right? So yeah. So we've got it on the west side.

**Chris Gammell:** Ah, got it. Yeah.

**Dave Jones:** Yeah. So yeah.

**Chris Gammell:** It's just showing to the neighbors if they're in their backyard or something like that.

**Speaker ?:** Yeah.

**Dave Jones:** Like if... Available on satellite. Yeah. If you come down our driveway, you can't see... You wouldn't think that we've got a solar panel system. You just cannot see it. So... And that's how she likes it. So yeah.

**Chris Gammell:** You know, she might be right though, you know, so if there's like a zombie attack, right? Oh, right. People are going to go right for the... Right. The house that... You know, the solar panel houses first.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Yeah. And Google Maps won't be working because the tower will be out. Come on. Right.

**Dave Jones:** Oh, boy. So yeah. Yeah. So I'm going to be running a hybrid system. Oh, that's cool. So that'll allow me to do like videos actually comparing, you know, comparing like the string inverters versus the micro inverters and all sorts of stuff.

**Chris Gammell:** And what is... The string inverter is basically like you invert it after you... Like you stack all the panels up and then you invert the higher voltage?

**Dave Jones:** All the panels are in series. So a regular solar panel is about 40 odd volts, something like that. So you put them in series and it goes like my system's about 460 odd volts because I've strung 12 of them in series, right? At about 40 volts each. So it's like 460 odd volts, you know, maximum open circuit voltage.

**Chris Gammell:** Yep. Yeah.

**Dave Jones:** Yeah. And that's actually... So I'm pretty much at the limit. You know, that's the limit of most string inverters. Mine's actually got two channels, so I could put a second string on there. But the problem with the string inverters is that if one panel gets blocked, that brings down the whole string, right? That's right. That's the advantage with the micro inverters is if one panel... Like Christmas lights. You know? Yeah. Right. Yes. So that's the... Yeah. That's the disadvantage. So I'm going with micro inverters this time. Yeah.

**Chris Gammell:** And that's supposed to be better for mixing, right? Because then you're mixing at the AC. You're mixing AC power that you can match.

**Dave Jones:** They are AC out. Yeah. Because they're dedicated little inverters. So everything's low voltage. So they're actually much safer. Because 460 volts DC, I've done a video on this where my DC isolator switch actually went bust, right? And it's lucky it didn't catch fire because these are a thing, right? Because when you've got high voltage, high power DC, if that sucker arcs over, there it is. It just keeps going. It's a DC. That arc sustains until something catches on fire, which is that something is your house, right?

**Chris Gammell:** Yeah. I was going to say probably until the carbon builds up so much that it's like, oh, I'm a resistor now.

**Speaker ?:** Yeah.

**Dave Jones:** And it's... Yeah. It is bad. Like go Google. This is a good one. Go Google DC isolator, solar isolator failures or fires or whatever. Wow. Yeah. So they're not that safe. So yeah, mine certainly failed. And there's been recalls of various brands have had to be recalled because they're not safe and et cetera, et cetera. Speaking of which, there's rumor. I haven't looked into the story completely, but Hyundai, you know how I've got the new Ionic EV. They might recall all of those worldwide. Hmm. So due to safety concerns. That's not good. No, it's not good. I love my EV. I don't want to have to bloody send it back and get the battery changed or whatever, or I don't know what they have to do to it.

**Chris Gammell:** Or just trade the whole damn thing out, right? Right.

**Dave Jones:** Yeah. I don't know. But yeah, that's really annoying. I know they've already done that in certain countries, but at the moment it hasn't hit Australia yet.

**Chris Gammell:** God, what a nightmare that would... Yeah. Have you ever been part of a recall, like a product recall?

**Dave Jones:** I have. Whoa. Yes, I did. Wow. This was a long time ago in a galaxy far, far away. An old... Was it an AWA brand? No, or was it an RCA brand TV? I'm talking none of this LCD rubbish, right? Old school CRT. This was back in the early 1980s when a color TV was a big thing. We were just sort of coming out of the black and white age, right? And yeah, they had to recall. They recalled RCA or somebody. I can't remember who it was. It was recalled. And they actually sent somebody around to your house and they actually did the repair in your house. You didn't have to take it back. They actually sent someone around.

**Chris Gammell:** Wow. That is interesting. I actually meant on the developing a product side.

**Dave Jones:** Oh, right. Have I had a product recalled? Yeah.

**Chris Gammell:** Because I mean, that's like... I feel like that's like the fear of God's in me about that. I'm just like, man, there's not... I mean, there's just like nothing more expensive. I feel like some of the time it's just like, well, you just close up shop, go home, see ya. You know, like...

**Dave Jones:** Oh, well, we had the... Yeah. Well, we had the switch problem with the 121 GW meter after the Kickstarter came out. You know, we got all these meters. I was about to ship them or we did ship some and then people are going, oh, my range switch doesn't work. And, you know, then we started getting more reports of this and about like, you know, 2% of people actually reported that their range switch is dicky. And then sure enough, we actually determined or, you know, Kane actually, they're the developers of it. They actually determined that, yeah, it was the thickness of the PCB was slightly out. The thickness of the PCB from the manufacturer. And it's like, well, we've manufactured like 4,000 of these boards, 5,000 of these boards or something. It's like, and they've all been populated with parts. So they've gone up the value chain.

**Chris Gammell:** The cost is much higher. Yeah. Yeah.

**Dave Jones:** The cost is so, you know, it's not like we can scrap like 4,000, you know, if they were just blank boards, maybe, but these have been assembled, right? They've got all the parts on them, you know? Yeah. Like, yeah. So it's gone from like, you know, okay, we scrap them at the cost of a dollar per board if they're a blank board or whatever, the blank board, you know, it's only a dollar or two, right?

**Speaker ?:** Yeah.

**Dave Jones:** Well, I don't know. It was five bucks. I think, right. Sure. Whatever it was. It's manageable cost, right? But once you populate them with all the expensive multimeter chips and all the analog parts and all the references and everything, boom. You know, I don't know what the bare board cost is, but it's enormous, right? Sorry. The actual populated board cost. Yeah, the populated board.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. It's enormous. So we couldn't just scrap them. So we had to develop a shim system. And then, then I had to mail out, you know, 2000 of these shims and people had to retrofit their shims to it, you know?

**Chris Gammell:** Yeah. But that's, that's just, you know, that's, if that's the worst that Kickstarter does, at least it's delivered and stuff like that.

**Dave Jones:** Oh, at least it's delivered. Yeah. But it's a big hit to the reputation, right?

**Chris Gammell:** It's a huge hit.

**Dave Jones:** You know, it's like.

**Chris Gammell:** Yeah, that sucks though. Yeah. It's totally embarrassing. But I wouldn't call that a recall. I'd call that a.

**Dave Jones:** Oh, no, it is not a recall. That's a mod.

**Chris Gammell:** You know, like that's, that's a mod. Yeah. Yeah. I just, I just think about like a huge, like a large scale global recall. Like, man, like how do you even deal with that? I would love to hear in the comment section, if anyone has been part of a large recall like that, but just like, almost like, what is the, what's it like at the office? You know what I mean? Like, like what is, how do you continue on from that? Does it just like everybody shifts into recall mode? Do you even keep making the next thing that you're like, you know, you're always working on the next device as the one is being produced. So it's like, do you even bother? You're just like, oh, well, I guess we won't be making anything new until we fix this old one. You know, I just.

**Dave Jones:** Well, I'm, I'm sure it's killed companies. I would like to know if product recalls have got, you know, cause when you're like Hyundai or you, you know, you're actually Tesla, there's talk about Tesla having to recall all their cars as well. Isn't there?

**Chris Gammell:** Holy shit.

**Dave Jones:** I think.

**Chris Gammell:** I don't know. Yeah.

**Dave Jones:** I think I read something about that. They're like, yeah, they've had to admit. Apparently they've been trying to, trying to avoid it for years. And I, yeah, anyway. Well, don't worry.

**Chris Gammell:** The stock price will still go up. Oh yeah.

**Dave Jones:** No, of course.

**Chris Gammell:** Completely decoupled from reality. Exactly. Don't worry about that. But yeah, that's still, that's crazy. I mean, like, you know, that's billions and billions and billions of dollars.

**Dave Jones:** Here we go. 5th of February. Tesla has responded to a United States recall of failing touchscreens in 135,000 of its cars, arguing the units were only ever expected to last five years in the first place. Wow. That was their excuse. Tesla's excuse where the touchscreen, which is the main operational thing in a Tesla, like, because it has no other controls.

**Chris Gammell:** It's dead in the water if it doesn't have that. Yeah, yeah, yeah. It's like, I guess maybe you could operate it from the app at that point. Wow.

**Dave Jones:** They've actually, yeah, this is breaking news. Tesla claims recalled touchscreens only expected the last five to six years. Wow. That is.

**Chris Gammell:** I wouldn't say February 5th news is breaking. Oh, well, come on. I think it is in the app hour. Yeah, exactly. 20 days later, the app hour reports, you know, like. Wow. Yeah. So, like, in that case, too, like, that's, I've heard about, like, I've had recalls like that on a car that I had. And, like, I guess some of that is the same thing where, like, they call it a recall. And then it's like, you have to go to a service station. And I think it was, like, a car I, like, maybe it was a Hyundai I had at one point or something like that. No, it was a Mitsubishi I had where it was, like, the airbag switch in the car had to be switched out. So, it was just so you had to go in and get that switched out. And it was free.

**Dave Jones:** What about the Takaka, if I'm pronouncing that correctly? Airbags incident. Have you heard about that? I don't know if it came into the US. But anyway, there's this. The Takaka? Takaka Airbags is the company.

**Chris Gammell:** How do you say? Oh, that's like the OEM?

**Dave Jones:** Yeah. Yeah. That is the OEM of these airbags. Yeah. The airbag recall. They went into all of.

**Chris Gammell:** Takata.

**Dave Jones:** Mitsubishi's cars. Ford. I think Toyota. Jen. Like, they're like the OEM. They're like the big airbag OEM. Takaka. And Takata.

**Chris Gammell:** Takata. Takata.

**Dave Jones:** Yes. And this was a huge. Yeah. Yeah. Yeah. Japanese brand. And they had to recall, like, every single airbag. And this hit, like, five.

**Chris Gammell:** 67 million. 67 million. Oh, my gosh.

**Dave Jones:** Yeah, yeah, yeah. And it's like, and I think, oh, don't quote me if I like, but the head had to resign or something else happened to him. And like.

**Chris Gammell:** Oh, my gosh.

**Dave Jones:** Yeah. Like, this was like, because in Japan, like, you know, face is like everything, you know, it's like. Sure. Yeah. And no, it was like.

**Chris Gammell:** Dude's not getting another job after that. Oh, my gosh.

**Dave Jones:** Oh, no, no, no. It's like, yeah. And this was. Yep. Yeah. Yeah. Yeah. Yeah. 17 people have died, apparently, from these. And 200 injuries from these airbags just, like, exploding, just actually going off. So, yeah. In Australia here, 130,000 cars were actually recalled just in Australia due to these airbag things. Oh, my gosh. Just due to this one manufacturer. Yeah. Wow. They've got 50,000 employees at this Takata. Wow. So, they're a huge. That's a huge company. I just.

**Chris Gammell:** Yeah. Man. Wow. That high reliability, like, long-term type stuff. Yeah. Yeah. How do you deal with it? It scares the bejesus out of me. Like, and I, like, you know, I have clients that are, like, industrial. And, like, it's just like, man, that is what keeps me up at night. Like, yeah, the supply stuff we talk about. That is. Sure. That's a definite. That's a short-term hassle and risk. And, yeah. But, man, this stuff really, really gets me.

**Dave Jones:** I've got a big story about this. I've done a video on it, like, 12 years ago. It's one of my original videos. But I'll tell the story again. Yes. Of course. I was working for.

**Chris Gammell:** At 12 years, you start to recycle.

**Dave Jones:** Yeah. Yeah. Yeah. Telling slash.

**Chris Gammell:** Or two.

**Dave Jones:** And it's due to a rubber band. A rubber. I think the title of my video is how a rubber band caused, you know, like a $20 million recall or something. You know? Oh, my gosh. Yeah. I can't remember the exact title. But if you search.

**Chris Gammell:** How a rubber band caused millions of dollars.

**Dave Jones:** Millions of dollars. How a rubber band caused millions of dollars. And the breakdown is we're doing these underwater sonar stuff, right? Underwater seismic survey streamers, right? They're actually 100 meters long. They're giant, right? We've got a giant factory 150 meters long that manufactures these 100 meter long things, right? And anyway, so we manufacture these things and we send them out there. Once they get out on the boats, you know, they're towed underwater behind the seismic survey boat searching for oil, right? And they all started to like their noise performance. Like they just got like noisier and noisier, right? Because these have some of the world's quietest analog to digital converters, right? They have to be, you know, you're trying to hear these echoes. Like, you know, the noise floor is like minus 136 dB or something, right? It's like the world's lowest noise floor stuff, which is some of the designs I worked on. And it's, you know, it's incredible. So the noise floor started to go up, right? You know, not by much, but it's like, but it's enough to ruin your data.

**Chris Gammell:** Percentages, right? Yeah.

**Dave Jones:** Yeah. Like it goes up 5% and that's enough to find oil or not find oil, right? And so it's not like a failed. It just, its performance just degraded a little bit. And then, you know, we did all our investments. So the customer's complaining because these are failing out in the field. And every day that ship isn't working is cost like $100,000 a day to just run it, you know, just to keep it operational.

**Chris Gammell:** Sure.

**Dave Jones:** And hundreds of thousands of dollars. So anyway, so we did our investigations and we found that inside the hydrophone, right? We use these, we manufactured our own ceramic hydrophones. They're little, you know, and they're, then they're inside these oil filled pouches, right? They're, you know, it's about half a foot long or something, you know, 30 centimeters, 15 centimeters long, big oil filled pouch. And that allows the, the acoustic waste and the water to travel through the oil into the hydrophones inside, right? And then we, what we did is we, of course, these wires coming out of these hydrophones and we actually tape, tape them down or we, we held them down with rubber bands, right? Just, just so that when you put the outer shells on, it didn't, you know, the wires didn't get pinched and everything else, right? So we're just using these rubber bands inside to hold down these wires and we didn't think anything of it, but the actual acoustic design of this, of, of how the shell works, you know, the oil has to flow through one side and everything else. And, you know, there's a certain acoustic design to it. And these rubber bands, the oil inside actually made the rubber bands swell up over time. And, and they swelled up enough to actually block some of the flow of the oil inside. So it was like, so the microphone, so the hydrophone became unbalanced, so to speak, and the oil didn't flow properly through the whole thing. And it caused the, you know, it caused an increase in, you know, noise and actual, you know, the performance to actually degrade and everything else. So these bloody, a bloody rubber band cause this, you know, it's, it's just nuts. Yeah.

**Chris Gammell:** That's bonkers.

**Dave Jones:** Like, and yeah. And so we had to not recall these streamers and we, we had to actually cut them out. So we had to develop procedures. Cause these things are like sealed. Like there's a gigantic outer sheath, a hundred meters long. So we had to develop techniques to actually repair these, which involved actually getting a scalpel, cutting open, like it's, it's like surgery, right? Cutting open this outer sheath.

**Chris Gammell:** Yeah. This is, this is totally a recall story right here. I think Dave. Right. And then, yeah.

**Dave Jones:** And then actually pulling the sheath back. So, and then we had to develop the tools to actually grip the sheath to actually pull it back. Cause you couldn't do it by hand. Right. So you had to open the thing up. This was like open heart surgery on, on the product.

**Chris Gammell:** Right.

**Dave Jones:** Right. We, we, we had to develop the tools to actually repair them. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** And then we had to go in there and we had to, you know, strip it all out. And then we had to develop, uh, molding systems that, you know, to, cause you had to put, you couldn't re cover the entire a hundred meter long streamer. So we had to develop, uh, once again, jigs to actually, uh, world the, uh, polyurethane back in place to actually seal up the, seal up the world and everything, you know, to actually weld and weld, weld the polyurethane material. You know, I don't know what it was, but, uh, yeah. And, and, and actually seal these things back up. So we had to, it was just incredible. It was a huge operation. It was absolutely enormous. Cost us like, I don't know how many untold millions.

**Chris Gammell:** Spared, spared no expense.

**Dave Jones:** Yeah. Like, and it was nuts. So we, we had to do like, and I actually had to develop the custom hardware and software to measure the performance.

**Chris Gammell:** I was wondering, cause it, your video mentions DMMs. I'm like, what, where is the DMM in this, in this story?

**Dave Jones:** Right. Well, right. Cause this streamer, right. And picture it, it's a hundred meters long and it's got, uh, there were, I can't remember the exact number, like 50 hydrophones. Like, you know, there's a hydrophone every meter or two. Right. It's actually to do with the wavelength of the frequencies we're trying to measure and stuff like that. Right. It's all, you know, wave acoustics and whatnot. So, you know, there's a lot of these streamers, but we, but because they're all in parallel, right. All these streamers in parallel, we didn't know which ones were failing. Right.

**Speaker ?:** Right. Right.

**Dave Jones:** So we didn't know which one, like, and you couldn't just replace them all. Right. That would have been, you know, you may as well make, make the product again from scratch. So, so I had to develop a jig and, um, software with a, uh, with a differential speaker solution that would actually clamp over. So this big thing that clamped over had a couple of speakers and I drive them, uh, differentially on each side so that we could work out if one of the ports was actually blocked and then, you know, hook it up to a system and measure its performance and everything else. And we could actually determine whether or not that individual hydrophone was actually busted. And then I, and then, because, and then it was a trade-off, right? Because they're all in parallel. You couldn't just waste. And here's the thing. You couldn't just waste money repairing everyone that failed. Right. Cause there was no hard threshold where, well, if it's over this value, we need to need to replace it. It's only when you combine it with all the others in parallel, can you make a determination of whether or not that one's worthy of actually replacing? Cause it was X amount of cost to replace one of these hydrophones, right? And you couldn't just go and replace it. So I had to write and optimize this software that actually predicted what the noise performance would be over the, when they're all in parallel and go, well, if, if we replace this one here and this one there and that one, it'll just bring it below the overall threshold. So my software had to actually predict how many to replace and where to replace them. And yeah, it was, wow.

**Chris Gammell:** That's intense. Yeah.

**Dave Jones:** That's, it's just, yeah, it's absolutely crazy. So that's a very, very unique story. I think in terms of, you know, it's not, you know, something just hasn't failed. It's just performances degraded. And yet you could actually leave degraded ones in there and it would still meet spec.

**Chris Gammell:** Right. Yeah. It's meet some maintenance over time kind of thing. And also like, it's almost like a statistical kind of thing. Yeah.

**Dave Jones:** But that was a huge hit to the company rep, you know, company reputation. And there's only like three companies in the entire world that do this stuff. Right. Exactly.

**Chris Gammell:** So everybody heard about it. Everybody knew what happened.

**Dave Jones:** Everyone knows about it. And, you know.

**Chris Gammell:** And it's brought up at the next time someone's trying to sell something too, I'm sure.

**Dave Jones:** But I guess the, I guess the only saving grace is, is that the customer could just go, well, bugger off. We're going to go with your competitor. It's like, because you're, because they're invested for hundreds of millions of dollars into your system, right. Into your ecosystem, which is not just the product. It's all the gear that goes along with it. You know. Yeah. So they can't just, you know, change on a dime. So, but yeah, we lost a, don't know how much money we lost on that, but geez, that was.

**Chris Gammell:** On the DMM front. So you mentioned DMMs now.

**Dave Jones:** Oh yes. I saw this.

**Chris Gammell:** Yeah. The new, the new Marco reps video. You saw that.

**Dave Jones:** Speaking about high end. Yes. High end, like world's best performance or whatever. Yeah. Yeah. The eight and a half digit volt meter, but this is not his design. Is it? It was a someone on the EV blog forum, right? He, he just built one up.

**Chris Gammell:** So this is CERN. So CERN actually developed this open source. Oh, okay. Right. Eight and a half digit. They're calling it a volt meter. I'd say it's actually more like, I mean, there is a volt meter, but it's really like a, so it's like minus 10 to 10 volts. And so it's basically like an ADC input effectively. Right. And so there's no ranging or anything like that. So it's not like a DMM, which is really, I think how you differentiate that sort of thing and all the protection elements, everything else. However, the eight and a half digit volt meter. Holy moly. Yeah. Yeah. It's, I mean, so, so Marco does actually like the assembly of this thing. He did a bunch of circuit boards. He actually shows, he's just like throw tosses off like, oh, by the way, I just like did a DIY vapor phase, vapor phase reflow during it. And he does machining. And it's just, it's, it's amazing. The whole thing is really amazing. So I don't know how much I had to say about this other than like.

**Dave Jones:** It's just, yeah. I don't know how much effort went into this one video, but it's months and months of effort. Yeah. Into this one.

**Chris Gammell:** I think that the thing that, that really sticks out to me in this is like, you know, people wonder like, so you have high end, like what differentiates, you know, three and a half digit from an eight and a half digit piece of equipment. And like from my days at Keithley, not, not any special input for me. It's just like, it's a lot of it is sourcing really, really, really, really amazing components.

**Dave Jones:** Yes.

**Chris Gammell:** And so I forget what he calls them, but they're basically these gold encapsulated through mount, through hole dip mounted parts that are actually matched resistors. Yes.

**Dave Jones:** They're actually a network of resistors. Yeah.

**Chris Gammell:** Yeah. And like, that is, that is often the magic you need. That is key. Characterize them yourself as well. And then, and then the LTC 1000, which is like a, the best reference in the world, like he mentioned, and it is talked about ad nauseum on your forum, you know, like, but then again,

**Dave Jones:** you can't just whack in the LTE and can't just whack in right. That, that part and expect that performance, right. There's a lot of like finesse that goes into making sure that's thermally stable, structurally stable, right. Because if your PCB expands, that actually bends the legs a little bit and bending the legs a little bit can actually degrade the performance of the part.

**Chris Gammell:** Sure. Right.

**Dave Jones:** It's just, it's insane.

**Chris Gammell:** You know, it's like, yeah, it's like, it's like you need all of your components in like a nice warm, fuzzy spot. And, and really you just needed to know that it's always going to be the same too. So there's a Peltier cooler integrated as well. So like that it's their heater and cooler. So like, yeah, it's just, it's definitely worth the half hour video. It is. It's really, really, really good. So.

**Dave Jones:** Well, you can probably do like a six and a half digit meter with all off the shelf parts and get away with them. Right. You know, a decent performance, six and a half. When you go from six and a half to seven and a half, now you start requiring really precision parts and knowledge. When you go from seven and a half to eight and a half, you're on the bleeding edge. It's like, you know.

**Chris Gammell:** I would say six and a half is still pretty tall. I'd say three and a half is doable, but I'd say six and a half is still. Oh no.

**Dave Jones:** If you, if you do a tear down of a six and a half digit meter, it's pretty much all off the shelf parts, you know. Yeah.

**Chris Gammell:** But they're still matched and they're still.

**Dave Jones:** Yeah. But you don't have to do, take thermals all that seriously. Oh, sure. Like it's, it's not the same level. Right. Yes. I agree with that. Right. Yeah.

**Chris Gammell:** You're, you're depending more on like the box that it's in is probably at an ambient temperature of 30 C or whatever it is after, you know, you still have your warmup times. You still have everything. You assume stability because of the air in the box instead of the machine metal pocket, like Marco did that holds the, you know, that has this locally controlled temperature down to, you know, a certain, certain precision and stuff like that. But yeah, it's bonkers. I was, I was telling someone in response to this. I really need to get some of my former coworkers on the show before, uh, before they retire. So we'll try to do that. Yeah. Some of the Keithley folks. I just, uh, I have a interview in the bag with Joel Dunsmore. So that's coming soon. Uh, we'll see when. Sorry. Who's that? Joel is the guy who did the 87 53, pretty much the entire VNA, not, not the entire thing, but he did a lot of the RF front end and everything. And he wrote a book about it as well. Oh, really? Sweet. Yeah. So he's still a Keysight and, uh, he's like, he wrote a book about developing that. He wrote a book about how to use a VNA very effectively.

**Speaker ?:** Oh, okay.

**Dave Jones:** Right.

**Chris Gammell:** And, uh, and it's this amazing reference. There's a new second edition out. So that episode, I will continue to tease for a while, I think, but, uh, but let me tell you, talking to Joel, I was so nervous. Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. And, uh, yeah, he's great. But like, but that kind of thing, you know, like people in the industry, they're just depth of knowledge is so insane like that.

**Dave Jones:** So yeah, it's great.

**Speaker ?:** Yeah.

**Dave Jones:** Ah, boy.

**Chris Gammell:** And if people know other people like that, we want to talk to them, right? Yeah. So please drop us a note, send us an email, feedback at the empire.com. We'd love to hear about them. There's also a form you can fill out. We do look at them all. Uh, we try and schedule with people that are suggested as well, but like those deep, deep, deep knowledge experts like Joel, uh, man. Yeah. I'd love to talk to someone like that, especially if you know them, that's even better.

**Dave Jones:** They're terrific. Yes. I'm trying to line up someone for the micro inverters that I was talking about. The micro inverter stuff. Yeah. Yeah. That'd be great. That's in progress.

**Chris Gammell:** So, you know, I, I remember, so, oh shoot, I forgot his name. We had someone on a long time ago from Cree and Cree was doing a lot of silicon carbide stuff. Yep. What was his name? Oh God. John Edmund. John Edmund. That was a long time ago. Yeah. That was episode 71. How did we get him on? He was the CT. He's the C, he was, is the CTO of Cree.

**Dave Jones:** He was the CTO of Cree. Yeah. We just asked, I guess. And we, yeah.

**Chris Gammell:** Anyways. So I, I remember when we talked to him too, like a lot of like the, so there are IGPTs often in like, you know, micro inverter stages. But I remember him talking about like how this was going to be a, you know, a more accessible thing as silicon carbide comes online, as you know, more silicon carbide comes online for, for switching FETs, you know, 1200 volt switching FETs are just kind of ain't no thing. And I, I remember, I remember that thinking about that and just how that was going to change things. And now micro inverters are the normal way of doing things with solar, right? I mean, like that is most of the time what you're seeing on the back of panels versus the string, unless you're doing like a farm.

**Dave Jones:** I don't know if they've hit that level yet. I think string inverters probably still dominate. I don't know. I don't actually have the data on that, but that's my gut feeling is that strings to do dominate. Oh, sure. Because it's a cheaper. It's, it's, it's simply cheaper and economics is going to win, right? It is not cheaper to get these micro inverters, right? It's more expensive. So yeah, yeah, yeah.

**Chris Gammell:** You know, one of my buddies from high school ended up, he's a solar salesman now, which is like, especially in Illinois, it's like so weird that he's here and like selling in Illinois, but he's like killing it in Illinois. Yep. And like, it's weird that it's a thing, like I said, but also like he has, I'll have to ask him about that and see what the, see what kind of systems he's selling just because like that's right. You know, yep. Might be different here versus there versus, you know, what are the broad trends?

**Dave Jones:** So, and most people, you know, Joe average is going to go for cost, right? Joe, Joe average doesn't give a crap whether they're micro inverters or it's a string inverter or what brands they are or what, you know, they just don't care. They go, how much warranty do I get? And how much does it cost?

**Chris Gammell:** Right. Right.

**Dave Jones:** That's it. Right. So there's a lot of, uh, yep. I've, I've, I've mentioned this before, right? Solar resellers in Australia, over 500 of them have gone out of business. Right. Wow. It is. That's crazy. Yeah. Like so many, you can't almost count them. Right. It is. Yeah. Because they spring up when some government program comes in and then every man and his dog is selling, you know, solar systems is actually, you know, installing and selling solar systems. And then the rebate finishes and boom, all these companies just vanish along with their warranties, you know? So it's like, yeah. Yep. You have to be careful. It's a, yeah, it's a bit of a, yep.

**Speaker ?:** Hmm.

**Dave Jones:** All right. We've got like, we've, our shows and we've almost done our dash dude. And we've got so much more to talk about. There's like so much more news. Come on.

**Chris Gammell:** What do you want to talk about next?

**Dave Jones:** Oh, well, bloody perseverance landed for goodness sake.

**Chris Gammell:** Oh, geez. Yeah. Oh yeah. Blah, blah, blah. Another planet. No big deal. That was frigging amazing.

**Dave Jones:** I live streamed it. And it was just, yeah.

**Chris Gammell:** I, I think at the, I don't think anyone listening, this is going to be like surprised. They're like, Oh my God, we landed on Mars again. No, no, no. It's like, yeah.

**Dave Jones:** At the start of the stream, I think I put the odds at like 85% plus. Cause they had already done it. It was, it's, you know, almost essentially the same airframe, but things were different, you know, like it is the same landing system, but yeah, they did. Yeah. I love it. They just nailed it. They just nailed it again. It's like, you know, and you've got to understand the sheer size of this thing. It's a car, right? It's the size of a car. Like not a small car either. No, it's the size of a large SUV. That weighs like a ton and a half or something. Right.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** And they just landed that sucker on the surface of Mars. Just unbelievable.

**Chris Gammell:** I don't know how much we have to say about the electronics in general. I don't know. I mean, like, that's the thing. I was just like mouth agape, of course, but.

**Dave Jones:** One of the interesting things is that they used off the shelf FLIR cameras, that, that footage that you see of the sky crane coming down. They actually, yeah, but they didn't use special stuff. They used FLIR, not, not, not infrared. Apparently FLIR make regular industrial cameras, I guess. Sure. You know?

**Chris Gammell:** Probably very, very strenuously tested.

**Dave Jones:** Oh, I'm sure they would have been, you know, qualified, but, you know, but technically you can buy exactly the same camera that was, you know, the commercial vision camera that was on. Yeah. I think they had like six or eight cameras just watching the landing. You know, they had multiple ones on the back shell, multiple ones on the rover looking up. So you can see the parachutes and, you know, all sorts of stuff. And yeah, these were just off the shelf cameras because like, it wasn't a priority of the mission. So I guess they didn't want to spend a huge amount of money and development, you know, developing like, it is not like the actual custom.

**Chris Gammell:** Yeah. It's not for the science. It's just for the marketing.

**Dave Jones:** It's just for the marketing and the marketing camera. Right. Yeah, exactly. So yeah, they wanted to spend as little as possible. So if they, and that's why they have multiple ones. Cause if, you know, four of them failed, who cares? Well, you've got another four, you know, it's like, yeah, that was just, that was, that was amazing. So yep. It worked.

**Chris Gammell:** Yeah.

**Dave Jones:** I was surprised how quickly it all happened. Like, cause I, I, I wasn't there for the previous one. I wasn't there live for the previous one. Unfortunately, I'm still scarred from that incident, but yes, it was, I was just like surprised how, like, it was all like, I was there live stream and I'm going, oh, okay. They're 300 meters up. And, and, and next, like five seconds later, it's landed touchdown. I'm like, boom.

**Chris Gammell:** I mean, that thing is, it was burning fast, man. Oh yeah. It was going.

**Dave Jones:** I couldn't believe how quickly it all unfolded. So it was almost an anticlimax. Cause it like, there wasn't enough time to build up the tension almost.

**Chris Gammell:** You know, it was like. Should have opened the feed sooner.

**Dave Jones:** I blinked and I missed it. You know?

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway. Yeah. Very cool. So that's, that's, uh, landed. So yep. Fantastic. Another science lab on Mars. Great stuff. Yeah.

**Chris Gammell:** Yeah. Some of the stuff that's on board, I am very interested in like the, so the RTG on there is longer term. I was, it was a really good.

**Dave Jones:** Longer term one. Is it?

**Chris Gammell:** It is. It's a different RTG. Right. I think it uses a different isotope.

**Dave Jones:** Different Peldia device or isotope in it. Yeah.

**Chris Gammell:** I think it's a different isotope in there. Right. There was a really good video from one of the engineering channels I follow. I'll link it in. But it was just going over all the things that were on board. So that was one thing that was really interesting. And the oxygen generation. Did you read about that?

**Dave Jones:** Oh, cause they're doing some tests about, yeah, they're doing some tests to see if they can produce oxygen or something. Aren't they?

**Chris Gammell:** Yeah. They're basically like cracking CO2. Yeah. Yeah. So there's like an electrode and they have to pump a bunch of power through it. And from a power perspective, it was interesting because like, I think the solar panels can do like 150.

**Dave Jones:** Right. That's probably, ah, so that's why they need more power, is it? Is because they're going to chew a lot of power for this experiment.

**Chris Gammell:** Right. So, yeah, I mean, kind of like, like your solar panel thing at home, right? I mean, like you only have so much power right now that can run the air conditioner and the washer and dryer and all that other stuff. Right. And they're working under similar budgetary constraints from a power perspective in that this thing needs a ton of power. So I think, I think they had something like, like 150 Watts of solar available, but this thing needs like 180 to start working. So they're going to like bank the power with cells on board. And then when they have excess power, they can run the experiments. I think.

**Dave Jones:** Hang on. The Rover doesn't have any solar though. It's all, it's all. Oh, sorry.

**Chris Gammell:** Yeah. Sorry. You're right. You're right. Sorry. Not, not solar. It's from the art. It's from the RTG. Yeah, that's right. So when they have excess power stored from the RTG, that's when they can run this experiment.

**Dave Jones:** Right.

**Chris Gammell:** But basically it's like a, there's like an anode and they power it somehow, but it's actually going to generate atmospheric oxygen for future. They're testing it as like a way to potentially make air for future astronauts that might be there. But then also if they can really start to generate more than they could start to make propellant as well, because that's just like zero two for a return trip, which is like, man, that's some science fiction stuff. You know, like that is frigging cool.

**Dave Jones:** You can make anything give it, give enough power, dude. You can make gold. You can manufacture gold if you've got enough power, right? It's just not economically viable to do it. You know, it's just insane. Yeah. You can, you can manufacture diamonds, gold, you know, all sorts of stuff. Yeah. Right.

**Chris Gammell:** It's just, I think it was the real engineering channel. So like I said, I'll link that in. Yep. But yeah, it's, there's a lot of really cool science on board. I, I feel really guilty. I didn't know about what was going, I think, what's his name? Veritasium made some videos about it a while back and, you know, it was just like the slow burn and like, I just didn't really pay attention to it. And then like, man, coming up to it, I was just like, and then the excitement happens.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, exactly. I think that's just kind of how it goes with you're not into the, you know, some of these people are, it's like their full-time job, like many, many people. It's like, damn, so cool.

**Dave Jones:** Yep.

**Chris Gammell:** But yeah. All right. Science. I love science. Other news. That's great.

**Dave Jones:** It finally had to happen. Finally. They finally had to fold fries, fries, electronics is no more. Yeah. This has been coming for years.

**Chris Gammell:** I mean, yeah, this is the death of retail in general. Right. But yeah.

**Dave Jones:** No, no fries has been. Yeah. If you've been like, there's been all these people out there actually visiting the stores doing walkthroughs for the last three, four years. Yeah. And they're, and they're just empty. Like the stores are just empty as, and everyone's just empty. Everyone knew it was coming.

**Chris Gammell:** Yeah. It's too bad. I mean, like.

**Dave Jones:** And in, in, in fact, our fries even pretty much announced that, well, you know, the end is nigh, you know? So. Yep. It's not surprising, but no, they are shut.

**Speaker ?:** Yeah.

**Chris Gammell:** They, you know, like a lot of these, you know, brick and mortars in general, like, especially computer stores at the scale they're at, it's like really tough to do. But I think the sucky thing for, you know, like, like obviously Radio Shack's long gone, you know, just having basically the electronics, you know, if you're really in a bind, you're stuck with stores like this. Oh yeah. Yeah.

**Dave Jones:** You want to go down and pick it up. Yeah.

**Chris Gammell:** You want to be able to get something. And literally this happened to me the other day. I needed a Raspberry Pi for a project and I was able to, Micro Center is still around, which is a US based chain.

**Dave Jones:** You're able to get one. Yeah.

**Chris Gammell:** Yeah. I just like ordered one and picked it up, which was like super nice. Cause they're all sold out on Amazon and everything else.

**Dave Jones:** Really? Okay. Yeah.

**Chris Gammell:** And I was able to get the same day. So like that kind of thing, like it's not often, but when it does, it's like.

**Dave Jones:** Oh yeah. When you need it. It's really important. But that doesn't sustain a huge business. You know. It does not. Right.

**Chris Gammell:** Yeah. Me buying three Raspberry Pis at once is probably not going to.

**Dave Jones:** Keep them afloat. Yeah. Right. Exactly. Buy more, Chris. Buy more.

**Chris Gammell:** Yeah.

**Dave Jones:** So yeah, sadly. Cause yeah, I visited Fry, a couple of Fry's stores. Like while we're talking about 12 years ago now. And I was amazed. Like, oh man, it was incredible. But, but, but even then at its peak.

**Chris Gammell:** They were, they were like temples to, to nerds. You know, like they were.

**Dave Jones:** Temples to nerds. Yeah. It was. And they're all themed and it was, you know, the underwater theme and there was an Egyptian theme one or something. And they were, you know, absolutely incredible. They had everything. But even then walking into it, I'm going, geez, they're over capitalized on space. I mean, you know, I know this is the U S and like, you know, you've got a lot of space in your cities and stuff, but geez, you know, like. Yeah.

**Chris Gammell:** I mean, how many people can you actually get through there to actually make enough money to support it? Yeah. Yeah.

**Dave Jones:** But they like, like the checkouts, they'd have like 40 checkouts or something. And it's like, what, how many people do you expect to come through at once? Like, you know, it's just, yeah, it's just, I don't know. Yeah. They really seem to have been over capitalized. So yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** There's a, there is a lot to be said for like a niche, you know, thing like, you know, because they, they try to do everything, you know, you could buy white goods in there at the same time as you pick up your soldering iron and your components. Right. I mean, come on.

**Dave Jones:** And your, well, and your gaming computer. And your gaming computers, you could build a computer from all the parts in there and you could, at the same time as you pick up a new washing machine and a microwave. I mean, come on. Like.

**Chris Gammell:** I think, I mean, it becomes a supply chain issue in general too. Like, it's just like, you need to make sure you have a couple of, you know, like our pack rat tendencies are going to actually pay off in certain ways. Yeah. They're going to pay off sometimes. Yeah.

**Dave Jones:** Yes, they do. So. Yeah. All right. What else we got?

**Chris Gammell:** Uh, U S is talking about boosting chip manufacturing. So there's been a couple of things about this. We talked about Samsung last time and like, there's been some U S administration, you know, talking about chip shortages. Obviously we talked about last, last time you and I talked was about the chip shortages hitting the automotive industry. Yep. And that's usually enough to get like governments around here paying attention. That happened back in 2008 too. You know, auto industry goes down. A lot of jobs. Yeah. Yeah. Right. A lot of jobs.

**Dave Jones:** And that means a lot of nasty letters. Yep.

**Chris Gammell:** Right. Right. And you know, if, if something comes out of this and that they actually start to bring chip capabilities, but I don't believe it to be completely.

**Dave Jones:** Well, they're putting 37 billion into it. And well, a new plant costs like 15 billion or something. Yeah, exactly. So it's like, it doesn't buy much.

**Chris Gammell:** Right. And, and, and really, you know, 37 billion is like, okay, that's a lot. That's all right. That's a ton of money. Right. Yep. That's, that's like, that's like two thirds of a Bill Gates, uh, on a good day. Yeah.

**Dave Jones:** But still these plants are so expensive, right? Right. Right.

**Chris Gammell:** Exactly. Right. Well, and just the startup time too. So like, this is not going to have any impact for years and years and years. Yes.

**Dave Jones:** But, but you have to do it now. Like, you know, you've got to think beyond the current election cycle. I know that's a shock, right? Like, you know, for a politician to think beyond the next election cycle.

**Chris Gammell:** I do hope that there is, there is long-term thinking about this sort of thing. Yeah. Yeah. Because one, I think, I think there's a lot of, so like, like, like I've complained about on this show a lot too. Like from a business perspective, I totally get it. Like TSMC is monstrous. They are going to have the fast, you know, the, the newest nodes. They're going to have the most capacity. They're going to have the best engineers. They're going to have everything you possibly want. If you are a chip manufacturer, they look like the answer, right? They are, they are the Amazon of the chip world. Right. But when Amazon, when AWS goes down, you are screwed. You are so frigging screwed. And you know what? Same thing happens here when you're like centralizing for economies of scale. Yeah. That looks great until something happens. And like, sometimes you have to have inefficiencies and whatever that looks like. I know it's like, it's, it's, it's, it's an impossible argument to make. And yet when the shit hits the fan, someone's gonna be like, why did we do this? And the answer is the economics, you know, it's just like, it's just such a, yeah.

**Dave Jones:** You also have to remember, right. That you don't necessarily need these bleeding edge plants, right? Yeah, sure. Okay. They can produce like the, like, like the latest Intel processor and whatnot, but like really is the world, is the country going to end if people don't get their latest Xbox or get their latest gaming PC? No. But if you can't produce cars and white goods and other consumer products that use like lower end chips, but you know, it's still important. Right. I mean, it's like, yeah, you can.

**Chris Gammell:** So all the stuff we've had on the show, you know, talking about like the Skywater PDK, all of the Google stuff, like all of those, they're all at 180 nanometers, I think. So like we're talking many, many generations back from what is, what is the bleeding edge? And it's like, that is capable. It's not everything you need. Obviously it's not.

**Dave Jones:** That's all that automotive stuff, right? That's all of a shortage at the moment that all the manufacturers complain about, right? Then they're not using five nanometer, seven nanometer bloody chips in their automobiles, right?

**Chris Gammell:** Well, I think they're using 45 nanometer, right? So TI is on 45 nanometer. But I think that, you know, it really comes down to like, what are the trade-offs then? It's like, okay, so maybe we can't make, you know, maybe we should be designing in something that has a slower switcher or, you know, like less efficient switcher or something like that. Yeah. I don't know. I don't know how you do that at like a system level because, because at the same time you think about all the sales incentives that are there too, right? You think about TI engineer walks into Ford and they're like, they're not going to be hawking the thing at the fab that's going away in five years. They're hawking the newest part that's on the newest process because that's also what they're incentivizing. It's just like such a big, tough system to work within. And, you know, like I get, I get how some of it works and, but it's still like, there needs to be some kind of like backstop kind of thing. I wish there was, man, I wish, I feel like if you took 37 billion and they just like standardized footprints, let's spend 37 billion and have, have someone standardized footprints so that I can just drop in a different part with the same footprint. You know, like why does a boost converter need to have a different goddamn footprint every time? Just have the boost convert. I know this is, people are screaming at me right now. It should be government regulation is what you're saying, Chris. This should be government. No, this is terrible.

**Dave Jones:** Yes. Yes. The government need to step in.

**Chris Gammell:** No, but I want like a fallback. How about, how about this, Dave? How about we have a fallback boost converter footprint? And I could put that on my board in addition to the fancy new footprint from TI or on semi.

**Dave Jones:** Well, you can, you can put in a, you know, a classic, one of the classic inverters from 1970. They still make them.

**Chris Gammell:** Yeah. I guess so. Yeah. I mean, yeah, I guess you could do that.

**Dave Jones:** Switches, one of the classic switches.

**Chris Gammell:** Maybe something a bit smaller, a little bit, you know, mid range. I don't know. I don't know how this all works. It's on you.

**Dave Jones:** If you design in the latest whiz bang, weird ass footprint thing and you're tied to one manufacturer, well, that's on you. Oh, you know, unless you absolutely have to come on. There's not.

**Chris Gammell:** Okay. Yeah. I agree. I agree with the premise. Yes, that is on you, but that's not fair to say that's on you for, because you didn't design in the 1970s thing, because that's just not realistic, right? There. Yeah.

**Dave Jones:** But come on. I mean, you know, is our power supplies that critically most products that you can't put in at least something that's available with a standard footprint from several manufacturers. Come on. I mean, you know, most people aren't developing products like that.

**Chris Gammell:** I mean, well, if we're going to go back to the beginning of the episode, you showed a part that was, you know, the zinc, little zinc. Oh, true. Well, yeah.

**Dave Jones:** Okay. That enables the product. Granted.

**Chris Gammell:** It has a bunch of, you know, it has like five, five or six PMIDs around the thing. Yes.

**Dave Jones:** Okay. They could have used a separate FPGA, but even if they used a separate FPGA, you still tied into that one vendor. Right. It's like, yeah, but we're talking power supplies here, dude. Right. I don't know, man. I don't know. We're talking power supplies. Come on.

**Chris Gammell:** There is literally no answer here, but it's just, I wish there was, I wish there was, you know, Dave, I just wish things were, I just wish there was a chip printer, Dave. You know what I really want?

**Dave Jones:** Oh yeah. Yeah. That's it's coming next year because you predicted it 12 years ago.

**Chris Gammell:** I literally, I literally had that thought at one point of like, oh man, that would, that would be nice though. I know it's never coming, but it would be nice.

**Dave Jones:** Oh, you admit it's never coming. Now you use the word never. You finally admit after a decade that I was right.

**Chris Gammell:** Maybe, maybe Dave, maybe.

**Dave Jones:** Hallelujah. That's it. But it would be nice. That's it. Okay. The amp hour is over. That's it. We're done. We've come full circle. Chris is finally.

**Chris Gammell:** It would be nice. It would be nice.

**Dave Jones:** Wouldn't it be nice if there's chip printer. That, because we had that song in a commercial here. It was a, was it Cadbury's? Wouldn't it be nice if the world was Cadbury's? Beach Boys, yeah. You know, and it's like, yeah. Yeah. It's like, yeah. Everyone, when, when you think of that song here in Australia, you think of the TV commercial, unfortunately. Yeah. Yeah. For chocolate. Yeah. It's been hijacked. Yeah. Yeah. Boy. Anyway. Is, is that it on our news list? There's a couple of other items, but.

**Chris Gammell:** A couple other items. Yeah. Yeah. Go check out the subreddit. That's what it's there for. Yeah, exactly. Drop, drop your links in there too. You know, we'd love to hear from people like, you know, people send me links sometimes on Twitter or elsewhere, which is great. But man, if you want more people to see it, it's open. Just go on Reddit. If you don't have an account, just.

**Dave Jones:** You can do, you can post it there yourself. And then people will thumbs it up and. Yep.

**Chris Gammell:** Yeah, exactly. I mean, and there's comments on it too. You can go discuss things. You can talk about it before we get to it. And yeah, it's sweet. It's great.

**Dave Jones:** So there's 40. How many members here? 4,300 members on the Reddit? Four and a half K. Four and a half thousand members. Ten people online right now viewing it.

**Chris Gammell:** Right. They don't even know. We're watching them. Yeah. We're watching them.

**Dave Jones:** There you go. Yep. I can stalk you. Well, not really.

**Chris Gammell:** Yeah.

**Dave Jones:** No.

**Chris Gammell:** All right, Dave. Well.

**Dave Jones:** That's it.

**Chris Gammell:** Go buy another Blackmagic switcher, the non-ISO version and open that one and then do a comparison. And I will. Oh, right. Okay. Thank you.

**Dave Jones:** Yes. I'll go spend 800 bucks and do a comparison. Yeah. Yeah.

**Chris Gammell:** You got it. You got it sitting there. Come on.

**Dave Jones:** Oh, boy. Can we talk about what I got offered the same day I ordered that?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Literally, like a couple of hours after I spent my 1200 bucks and ordered my Blackmagic switcher, I was contacted by the Blackmagic distributor here in Australia. And they said, hey, we heard you mention it in the last video I did. Was it a, I don't know, I mentioned some video somewhere and that I was possibly going to get one. And they said, hey, would you like us to send you the new model? And say, oh, shit, I just bought it.

**Chris Gammell:** You should see if they can send you the old model and just tell them you're going to tear it apart. You know, like, it's great. I'd be interested. Yeah. Just tell them that. They probably have some sitting around. Yep. You know, like, that's great.

**Dave Jones:** It's an interest. Okay. Yeah. I'll see if I can run some one up.

**Chris Gammell:** Just tell me you're going to reveal all their company secrets except for the bit streams and all the code and all the other stuff that's inside.

**Dave Jones:** Because I held off getting one because news was coming out that they were going to do a, they had a press conference for a new, you know, talking about this. So I thought, oh, there's a new model coming out. Sure enough, there was a new model, but it's like an eight channel job, which I didn't need. Anyway. Very cool. All right. That's it. All right, man. See you. Catch you next time.

**Speaker ?:** We'll be right back.
