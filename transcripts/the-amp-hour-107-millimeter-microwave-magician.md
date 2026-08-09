---
episode: 107
title: An interview with Tony Long - Millimeter Microwave Magician
url: https://theamphour.com/the-amp-hour-107-millimeter-microwave-magician/
---

**Chris Gammell:** This is the F-Hour Podcast, recorded August 5th, 2012. Episode 107 with guest Tony Long, Millimeter Microwave Magician. Welcome to the Amp Hour. I'm Chris Gammell of Chip Report TV and Chris Gammell's Analog Life.

**Dave Jones:** And I'm Tony Long of reactandslabs.com.

**Chris Gammell:** Welcome, Tony. How are you doing? Pretty good. How are you? I'm feeling a little lonely. I mean, like, obviously you're here, but we had a jettison of personnel here this week.

**Dave Jones:** Yeah, I think we're just a northern hemisphere only this week.

**Chris Gammell:** Yeah, northern and eastern, or whatever hemisphere we're in in the States. No Aussies this week. Yeah, Dave decided to... As people probably saw, we'll post the video in the show notes this week, but Dave really was geeking out about the Mars landing. So he was at an event for that and couldn't make this week's show. So Tony was nice enough to come on. Tony was our guest. And so usually we're at, you know, our guests talk all the time anyway, so it works out well. I mean, we're here to learn about what Tony does and all the cool things he's working on.

**Dave Jones:** So who needs Dave? Maybe I can get a rain check for appearing another time with Dave. Yeah, yeah. Give him a hard time about it.

**Chris Gammell:** Yeah, or we can just have him call you and, you know...

**Dave Jones:** Yeah, that's true. You can record a recording on my answering machine. Yeah, yeah. You've reached Tony Long.

**Chris Gammell:** You like Carl Castle and NPR. Yeah, exactly. Nice. So let's talk about you, though. So Reactance Labs is your new shtick. But more generally, you are working on some awesome things. I actually met you at Maker Faire for the first time. But guests have actually heard about you and your setup before from our buddy Jeff.

**Dave Jones:** Yeah, yeah. So I guess I'll start off with Jeff since he's a longtime contributor here. I was friends with Jeff in college. We did the whole college thing together and then known him for years and years. And heard about the amp hour through him and met you at the Maker Faire because of Jeff. And yeah, so Reactance Labs is a little thing I'm starting up. It's just a sort of a home business kind of thing, a kit making outfit basically. Just trying to come up with a way of sort of having an excuse to buy expensive microwave test gear. I like that. And a means to fund it. Yeah. So that's sort of the main purpose of Reactance Labs. So it's not really going anywhere huge. I guess if it was something that could support me full time and I could build cool projects full time, then yeah, that would be pretty cool. But yeah, so that's Reactance Labs. I'm going to be making microwave-related kits and circuits, some pre-built, some in kit form. But yeah.

**Chris Gammell:** Well, how about you start us off with the Maker Faire stuff because that's actually what I've seen. And that alone is pretty damn impressive, what you were showing off there. So why don't you explain what your project was there? And I'm sure people will be pretty impressed.

**Dave Jones:** Yeah, yeah. So the Maker Faire thing, a little background on that. A friend of mine, Wayne Yoshida, contacted me. He's local to the area, Los Angeles, where I am. And he said, hey, we're putting together this Maker Faire event and we'd like you to come up and bring your radios. I said, sure, why not? And so I did. I brought up a couple tripods worth of radios covering bands from 10 gigahertz through 79 gigahertz. And I set up a little cross-the-booth link on 79 gigahertz so that people could come up and make a radio contact in the millimeter waves. And so that's what I brought. It was probably about 10 years worth of work in radio equipment that I built. So it was pretty neat to show that stuff off and get a lot of people to see that stuff.

**Chris Gammell:** Well, what is the reaction when you – I mean, like, do people often just say to you 79 gigahertz? You meant megahertz, right? I mean, you must be – I mean, that was my reaction. I mean, do you get that a lot or what?

**Dave Jones:** There were a lot of wide eyes. A lot of people, wow, that's high. Just a lot of astonishment, I guess. But, you know, one of the other reactions I got was, are you sending high-speed data through this? And are you using it for its bandwidth? And that was a popular question I got. And I think that should be expected in the Bay Area where there's a lot of internet, online activity type of stuff.

**Chris Gammell:** People are saying, so what I'm really asking is, can I use this for my peer-to-peer streaming?

**Dave Jones:** Yeah, yeah. Or can I get a, you know, OC192 to my house, that sort of thing. Right.

**Chris Gammell:** So what's the answer?

**Dave Jones:** No. Well, yes, but no. Oh.

**Chris Gammell:** So people still have to wait for Google Fiber, huh? They don't get –

**Dave Jones:** Yeah, that's probably a better way to go. So these radios that I build and that other microwave enthusiasts tend to build are for very narrowband communications. And we use them to do weak signal operations. We try and separate ourselves as much as possible, set the distance records and minimum power, that sort of thing. So that sort of really requires the minimum bandwidth. And sometimes it comes down to using Morse code for really weak signals. And there's people even experimenting now with modes that require even less bandwidth than Morse code. These are long-term integration type of things that will take, you know, a minute to send a call sign. Really? And you get really, really improved signal noise performance.

**Chris Gammell:** So it's because you just average it over time, basically?

**Dave Jones:** Yeah, yeah, you're just integrating over time. And so, you know, these kind of things demand really high-performance equipment. So part of the intrigue that I have, at least, in microwave as a hobby is that it's somewhat like tuning up a hot rod or a car. You can continually add things and improve the performance because this is an analog type of an application. And, you know, you can improve your timing. You can improve your accuracy. You can improve your power. All these things you can tweak and add on to over time.

**Chris Gammell:** Okay, so you're tuning this stuff up. But you're actually not – why aren't you doing, like, wider bandwidth stuff? I mean, is that actually just not a challenge? Or is it not an interest? Or, I mean, is it like the machismo is in the distance and then the weakness of the signal? Is that kind of the idea?

**Dave Jones:** No, I think it's more just a traditional ham radio kind of thing. I guess there isn't really a need in sort of traditional ham radio stuff to send high data rates. I mean, people do send video. It's typically been analog. And it is partially a technical challenge. It requires quite a bit of sophisticated hardware to do the modulation and demodulation required for wide data bandwidths. So that's something that's still a big challenge. But in terms of what ham radio is usually about, it's about one guy talking to another and just having a conversation or making a contact, exchanging very basic information. So there really hasn't been a drive to increase bandwidth. There have been a few people who have done some high bandwidth microwave links, you know, sort of for their own use. But it starts to get into a legal issue because ham radio is governed in such a way that you're not allowed to transmit music. You can't encrypt things. And so then it gets a little more challenging to use wideband data if you have those restrictions.

**Chris Gammell:** Yeah. It's like, what are you going to send? Just like huge text files of, you know, some kind of thing. Yeah. Yeah. Yeah. Send 10 gigabytes of that kind of thing. Yeah.

**Dave Jones:** I mean, I could see if you wanted to send streams of high definition video, that might be the only application I can think of. But, you know, certainly other people would be able to think of something. And that's kind of what part of what I'm hearing is I want to get people interested in the hobby who aren't otherwise interested. It's a small hobby. Yeah. And I think it's a hobby that could appeal to a lot of people. Cool.

**Chris Gammell:** So do you have an estimate of how many people kind of participate either regularly or just even in name? I mean, I know there's always distributions of active users versus just total users.

**Dave Jones:** We have a contest here in the U.S. annually. And I believe there's a couple hundred people that operate and submit logs for the contest. So I would say that's probably about 70% of the people who actually operate. There's some people who forget to turn their logs or don't care, who aren't interested in competition. And probably about double that or triple that of people who have the capability but just don't get out to the contest. So I would say it's probably in the range of a thousand or so in the U.S. And probably Europe is substantially larger, I would imagine. There's a great deal of activity in Germany and England and France and Italy, some of the other countries over there. So those are the two sort of main areas of activity. There are actually quite a few hams in Australia that are interested in microwaves. They're doing a lot of interesting stuff too. So it's not here.

**Chris Gammell:** Well, Dave is not a ham as far as I know. I mean, because he was disparaging it when I got my ticket. I only have my technician license, but I'm in that percentage that is not active. Yeah, yeah. I call my podcasting radio and that's about it. But yeah, so do you also participate in lower bands as well? Or is this kind of like this is the main thing? You only care about getting above a gigahertz or something like that? Are you also doing the other stuff or is it not really interesting?

**Dave Jones:** I do a little bit. But the truth is that I really get a kick out of building stuff. And so in the lower frequencies, it's too easy to just buy a radio that works really well. There's some extremely good equipment out there that you can just buy. And a lot of people do build stuff, but personally, I like the challenge of the higher frequencies. It's something unique about it that I like. And I do operate a little bit on the lower frequencies. It's kind of cool to talk to people around the world with nothing but the ionosphere as your transmission medium. So that's kind of a cool thing. But in terms of building things, it's mostly above, say, 10 gigahertz or so.

**Chris Gammell:** Okay. So you mentioned the ionosphere and the hams among the listener base will know that people bounce signals off of that because it plays well with the frequencies of the lower bands. But what about for the higher band stuff? I mean, I'm guessing you probably at 79 gigahertz, I'm guessing you probably shoot right through it, right? Or do you actually get ionosphere bounce?

**Dave Jones:** Well, probably would never reach the ionosphere because the atmospheric attenuation is so high at 79 gigahertz that relatively little would get through it, especially at the power levels that I'm using, which are in the microwatts at best. But, yeah, anything above a few tens of megahertz pretty much goes through the ionosphere. And certainly microwaves go straight through it. And that's a good reason why it's used for satellite communications is that it just goes right through the ionosphere regardless of what's there.

**Chris Gammell:** Could you explain the atmospheric attenuation? Is that just because of water molecules or what kind of – what's the deal with that?

**Dave Jones:** Actually, there's a number of mechanisms in play. And there's a cool graph. Maybe I'll put a link to this in the show notes. It's – that shows different absorption lines across the radio spectrum. And these are attributable different things, molecular water, molecular oxygen, dust, things like that. But even just oxygen alone will absorb microwaves. And unfortunately, some of the amateur radio bands are pretty close to these absorption lines. The 24 gigahertz band is actually pretty close to, I believe, a 22 gigahertz absorption line. And so the loss is pretty bad for that band and especially in humid environments.

**Chris Gammell:** So is that why the FCC or local places are just like, yeah, you can have that?

**Dave Jones:** Well, yes and no. I mean there's some applications where you want high attenuation. For instance, if you have a point-to-point microwave link between two buildings at an office, you know, you may be a kilometer apart at most. In which case, the attenuation is actually to your advantage because nobody else would be able to pick up your signal miles away. It's like a laser beam at that point, right? I mean it's like – Well, it just dies off over distance. It's the sort of thing where if you don't want interference or if you don't want anybody eavesdropping, you know, simply having atmospheric attenuation is to your advantage as long as you can meet your link. Yeah.

**Chris Gammell:** So are there actually applications right now where that – like building-to-building kind of stuff? I've never heard of that kind of thing.

**Dave Jones:** Oh, yeah. Yeah. In fact, there's a whole – I think they call it E-band and it's in the, I believe, 50 to 70 gigahertz range. And there's quite a bit of activity now going on commercially in terms of point-to-point microwave links because, you know, you can get high data rates. You can get a gigabit per second easily at these bands. Just the fractional bandwidth is so small.

**Chris Gammell:** And it's just open so the equipment vendors make the equipment and then the users don't have to worry about it at all. They just set up the link and go?

**Dave Jones:** Yeah. Is that the end of it? Yeah. You just plug in an Ethernet cable and away you go. Some are more sophisticated than that. But, yeah, they're sort of just a gateway. Yeah. Wow. That's pretty cool. Yeah. Yeah. And actually, in a lot of developing countries, these microwave and millimeter wave links are very popular because you don't have to lay any cable or fiber. It's a cheap alternative.

**Chris Gammell:** Yeah, definitely. So what other kind of applications are there commercially or – I mean, I'm guessing a lot of – you said satellite as well. But military, I'm guessing that some as well? I mean –

**Dave Jones:** Oh, yeah. Yeah. Military, satellite communications, and point-to-point microwave. Those are the principal applications. Okay. As well as radio astronomy. There's an observatory, I think, in Hawaii that does millimeter wave and submillimeter wave type of astronomy.

**Chris Gammell:** Okay. So you mentioned one of the 24 gigahertz band. What other bands are available to hams that – Okay. That you operate on or maybe that you stay away from?

**Dave Jones:** Yeah, yeah. So microwave, depending on who you ask, is anything above 1,000 megahertz or so. Okay. We have a band at 1.3 gigahertz, 2.4, which is nice because it's right around the Wi-Fi band. And it's actually pretty cool because there's a lot of parts available that we can easily use for that band.

**Chris Gammell:** Yeah.

**Dave Jones:** Then another at 5.7 and then at 10. And 10 gigahertz actually tends to be the most popular of the microwave bands for ham radio use. Beyond that, there's 24, 47. Then 76 to 80, and there's a small gap in between there that I believe is reserved for automotive radar. Yeah. Yeah. So beyond that, there are bands up to 250 gigahertz that are available for amateur radio use. Holy moly.

**Chris Gammell:** Yeah, yeah. They're like, well, whatever you want to do with those. I mean, we're not using them, right?

**Dave Jones:** Yeah. Well, actually, they do draw the line at 300 gigahertz. The FCC doesn't regulate anything above 300 gigahertz. They just – there's nobody using it. We don't care. That sort of thing.

**Chris Gammell:** You think eventually they will or what?

**Dave Jones:** Well, sure. I assume at some point in the past they stopped regulating up to 30 gigahertz. But at 300 gigahertz, the range is extremely small. There's almost no equipment available. Yeah. But that is changing. There are hams that have made contacts at, I believe, 411 gigahertz. That's the highest that I've heard of in terms of coherent radio communications.

**Chris Gammell:** And so, again, that's like a CW or a Morse code contact, right? So – Probably. Wide bandwidth. And that's like 150 hertz band, right? It's never –

**Dave Jones:** Yeah. And probably what they're doing there is just multiplying up. So all you're getting is a tone coming out, just a tone and receiving a tone. So it's very, very simple sort of a stuff. But to actually heterodyne and create a voice signal, most people don't do that above about 100 gigahertz. Okay. Although it has been done at 241. There's a guy back east that has built a pair of 241 gigahertz radios and holds a record. I believe it's some tens of kilometers. It's a remarkable feat. Really?

**Chris Gammell:** Wow. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** So could you explain a little bit about the – you've mentioned distance a couple times so far. But I've also saw on your website – on your Reactance Labs website, you talk a lot about the transmitting from mountaintops during contests and stuff like that. Yeah. Yeah. Okay. Could you explain that a little bit? I mean, is it only because of point-to-point or getting over the horizon or what's the deal with that?

**Dave Jones:** Yeah. Well, you know, part of the advantage of microwaves is you can use very high-gin antennas and they're very small. So the disadvantage though is that now you've got extremely narrow beam widths. So you have to get above local terrain in order to use them. Microwaves don't penetrate well through building materials or trees, foliage of any kind. It's pretty amazing how attenuating a single tree can be at 47 gigahertz. It's night and day. It is mostly to get above obstructions. And it gives you a great view at the top. You can – Well, yeah. Yeah. Well. Mountains, right? And visual view. Yeah. Right, right. Yeah. So, yeah. It's – to make contact with other people. In regular city or rural settings, it's pretty difficult to make contact. Although we can bounce signals off of objects and people have used that where they aren't on the top of a mountain but there's a large water tower near them, for instance. You can use that to sort of scatter signals off of and contacts have been made that way. Also with airplanes.

**Chris Gammell:** Really? That's good. Yeah, yeah.

**Dave Jones:** Any – People call it Boeing bounce. And you can bounce a signal off a plane for just long enough sometimes to actually make a contact over an otherwise impossible path. Really?

**Chris Gammell:** Yeah. Really? And so how many people are local to your area? I mean are you able to just on a weekend just fire it up and kind of point it at a 737 and see what happens or what's the deal with that?

**Dave Jones:** No, no, no. I'd say in the Southern California area, there's probably about 100 people on microwave bands. But very, very few are operating on any regular basis. Okay. We traditionally operate during these contest weekends and then spend the rest of our time tweaking with the radios and trying to make them better. And it's mostly a builder's hobby. If you want to get out and talk, it's probably not the hobby for you. But if you want to build and learn new things about RF and microwave hardware, it's definitely the way to go. The communication is almost just a test to see does your stuff work. Right. And sort of the culmination of your project. Yeah. Yeah, that's great.

**Chris Gammell:** Yeah. And we've talked about that difference before. I mean we don't talk about ham too much on the Amp Hour. But we've talked about the difference between people building or people kind of just getting on and interested in making contacts. And some of them, you know, yapping. Yeah. You know, there's certain hand bands or on repeaters that are pretty loud. But yeah, I think the building stuff is the cool side of it anyways. That's what I plan to get into it for. And then, of course, did a bunch of other stuff. Right. Right. So why don't we get – well, let's see. We had some other things we were going to talk about. Could you just with the contest real quick, just for people who haven't heard about even ham contests before because that would be how people got involved in it, right? I mean what is a contest? What does it even mean?

**Dave Jones:** Yeah. So in ham radio, there's a bunch of different contests that are intended to promote activity. And most of these are contests where you try and talk to as many people as possible. So you get points for every person you talk to. And then there are some other things where you can get extra points. For instance, in the microwave contest, distance is a key factor. So you get extra points for distance. So the farther you talk to the most number of people, the higher the score you get. And, yeah, so ham radio contests in general are a timed event, usually a 24-hour period. And you try and contact as many people during that time. And then you submit your logs. And the ARRL or whatever organizing committee collects them all and gives you a prize of essentially nothing. But you can send away for a plaque if you win. And they'll give it to you. But it's really just a self-satisfaction kind of thing.

**Chris Gammell:** It kind of sounds like a scavenger hunt almost where the hunt is for people. Yeah, yeah. Yeah, it is kind of. Yeah, yeah. License blades and that kind of thing, right? Right, right. I mean, I guess call signs would be the license blade. Yeah, yeah, yeah. Okay. So and how often are you even doing these kind of – I mean, like, are they pretty regular?

**Dave Jones:** I do it twice a year. There's a – it's called the 10 gigahertz and up contest. Okay. Okay. This is a two-weekend-a-year thing. It happens in the third weekend of August and third weekend of September. And they split it over two weekends because microwave gear is so flaky that the first weekend is to kind of get out there, test it out, make sure it works. And then you have a month to fix it before the next weekend of the contest. So that's pretty much the extent of my operation. I'll get out once in a while if there's some special event going on. But it really takes a lot to get people out, haul their gear up to a mountaintop, and have a big activity session.

**Chris Gammell:** And it's usually on mountaintops, huh? So like our Kansas friends are out of luck. Is that kind of a –

**Dave Jones:** Yeah. Yeah. That's too much. There isn't a whole lot of activity in Kansas that I know of. There is a group called the Central States VHF Society, and I don't know exactly how they operate. I think they will find the sole mountaintop or single high point, and then somebody or a group of people will get up on there, and they'll make lots of contacts. But the majority of activity tends to be in places where there's at least something high. Recently, there were some activity over the Great Lakes where they were using the – I believe the evaporative ducting mode of propagation where they don't have to be very high, but as long as they get their signals into this layer of evaporated water over the lake, they can communicate great distances.

**Chris Gammell:** Wow. Finally, it's good for something other than lake effect snow. As someone who grew up in Buffalo and now lives in Cleveland, I could not be happier. There's actually a reason for it because otherwise – That's right. That's right. It's just my misery that it's been there for. Yeah. So you went to – you had something this past weekend though too because you wrote to me an email about that.

**Dave Jones:** Just yesterday. Yeah. We do a test day here in the LA area once a year before the contest. And this is where a guy from San Diego named Kerry, N6IZW, he brings up a bunch of equipment including a spectrum analyzer, a frequency source, and mounts all this stuff on top of a tower at the end of a park. And the rest of us set up our radios at the other end. And we do two tests. One is to determine the minimum detectable signal. And the other is to determine equivalent radiated power. So these are the two sort of key parameters that you care about when making long-distance contacts is what's the weakest signal I can hear and how much power am I putting out. And it takes a field test to really prove this out because you can take elements of the radio. You can take an amplifier or an antenna feed or a local oscillator and you can measure those in the lab. You can get really good accurate results. But when you put everything together with the antenna on the tripod and everything, it's pretty difficult to measure in a lab. You've really got to get the antenna into the far field. Yeah. So that's what this is. It was a test to see how everybody's radios were working. And so we go down the line and everybody does their two tests. Yeah, yeah, yeah.

**Chris Gammell:** Number one, go. And you mentioned Ham Nation was there, the TWIT podcast?

**Dave Jones:** Yeah, yeah. Gordon West, WB6NOA, is a longtime microwaver, actually. And he's been at these tune-up sessions many times and operates the contests every year, sometimes from a boat, actually, which is interesting. Oh, that's kind of cool. He'll go out off the coast and motor along. And actually, it's to his advantage because every time you go, I believe, 10 miles, you can make contacts over again and you get all those points.

**Chris Gammell:** So he's very mobile, huh? Oh, yeah. Yeah. And people might know Gordon West's name from – he has a bunch of courses if people are ever interested in learning ham stuff. He has a bunch of courses and check him out.

**Dave Jones:** Yeah, and so he was doing the This Week in Technology Ham Nation podcast. They were recording a video. And I guess it will be up later this week on YouTube.

**Chris Gammell:** I think those go up on Tuesday or Thursday or something, Wednesday or Thursday.

**Dave Jones:** I think they said Wednesday, yeah. Yeah. So I'll get a link for that. Okay. I'll put it in the notes for later. But yeah, so he was there. It was a pretty nicely done video. So you can get a really good idea of what's going on. And this year, one of the things we did differently is we actually had one person do the listening for the minimum detectable signal test. Because you can always imagine that you're hearing a signal and get a little bit better. So this one guy with calibrated ears went by and listened to everybody's radio to make sure that there was sort of a standard MDS reading.

**Chris Gammell:** So is that kind of like how when people listen to static radio, they think they hear voices? Yeah, yeah. Because it's just like the human ears tuned to hear voices. Is that kind of the idea?

**Dave Jones:** Oh, no. This is like, okay, the signal is so weak that it's actually gone, but you're imagining that it's still there.

**Chris Gammell:** Right, right, right. You want it to be.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Oh, you want it to be. I get it.

**Dave Jones:** Yeah, yeah, right. Because you want a better minimum detectable signal.

**Chris Gammell:** Yeah. Right. Okay. So the output from this then is just for the upcoming thing in the third week of August? Is that the?

**Dave Jones:** Yeah, yeah. So basically everybody takes a look at the data and says, okay, my radio is performing similarly to somebody else's radio of a similar construction. And you can kind of compare. You can say, okay, I'm receiving 6 dB worse than Joe's radio who's got the same antenna. Something's wrong in my receiver or my transmitter and receiver down by the same amount. So something's probably wrong with the antenna. Wow. So it's a full system checkout and it's pretty valuable.

**Chris Gammell:** Oh, yeah. I bet. It's like when you're troubleshooting in a lab too, except in your case, you can't do that in the lab. Right, right. That must be frustrating when you don't actually, when it doesn't work, right? I mean, like it's good to know that it doesn't work, but just as easily if you didn't have another checkout in time, then you could just be kind of up a creek, right?

**Dave Jones:** Right. And I've had that happen. I took a 24 gigahertz radio several years ago into this tune-up day and I thought, okay, it's all done. I've done a great job on this. Got it there and it was just not working at all. Yeah. So I discovered the problem, fixed it, and by the time the contest happened, I was ready to go. So it really did help.

**Chris Gammell:** Could you give us a little picture? I was looking at pictures on your blog before, on the React and Slab blog, of what the radios actually look like. Okay. Could you try and give us an audio picture of what, if we saw you standing in a field with one of these things, what is this thing going to look like?

**Dave Jones:** It's going to look like a heavy-duty tripod with a box on it and a parabolic dish antenna sticking out the front. Okay. And sitting on top of the box is probably going to be a commercial radio of some sort, like a ham radio single sideband transceiver. So that's a typical setup, but there are a wide variety of setups that people use. Everything from bolting parts to a piece of wood.

**Speaker ?:** Yeah.

**Dave Jones:** That's a good look. I like that. Oh, yeah. Yeah. And durable, too. Wow. You know, use a nice hardwood. Yeah, yeah, yeah. Yeah. People have put them on bar stools for rotating. Really? There's all kinds of crazy things that people have done. Yeah, that's great. You can use a lot of creativity, and that's another cool aspect about this hobby is that as much electrical engineering goes into it, there's also a ton of mechanical engineering to actually get these things to work right. Oh, yeah. And to be able to point things accurately, to hold things stable in the wind. Yeah. If you've got a large dish, some people go out there with six-foot diameter dishes, and to hold that up against a wind on the top of a mountain is a very tough challenge. Yeah.

**Chris Gammell:** Wear a parachute, that kind of thing. Yeah, yeah. That's what it becomes, yeah.

**Dave Jones:** Or it'll end up looking like a Mars science lander.

**Chris Gammell:** Yeah. Yeah. So you mentioned the accuracy of aiming this thing, and you talked earlier about that, too. How do you aim it? Is it with a laser pointer? So if you're on top of a mountain, you have this big rig, and say you're pointing and trying to make a contact down the mountain or wherever you're trying to go. I mean, you said the beam size isn't that wide. Yeah. I don't know how big would actually – it's probably the size of the actual wavelength, right? But some scatter. How the hell do you – how do you find someone? It's probably like shooting an arrow, right? It is a bit.

**Dave Jones:** And so that's actually one of the biggest challenges during the microwave contest is acquiring a weak signal from far away. It's frequently the case that signals are strong enough that you don't have to point very accurately. But when you're really going for those long-distance contacts, you've got to have a good way to aim. And so one of the ways we do this is we have beacon transmitters that are installed in mountaintops at determined locations. So we can point our antenna to one of those and have a compass rose on our tripod, establish a heading because we know where we are and we know where the other side is. And then we say, all right, let's – we know where the other guy is transmitting from. I'll just point my antenna directly to him. That'll get you pretty darn close.

**Chris Gammell:** Yeah.

**Dave Jones:** Within a degree or so. And from there, we exchange transmissions of carriers. So we'll use a UHF repeater link typically to coordinate these things. And I'll tell the other guy, hey, okay, transmit a carrier. So he will transmit a carrier to me for a minute or two minutes. And I'll aim my dish to maximize the signal level. I'll lock it down. And then we'll do the opposite. He'll pick up his. And sometimes we'll have to go back and forth a couple times to get it really good. But that's sort of the typical routine. Sometimes we –

**Chris Gammell:** How do you communicate – this is the part that always gets me. Is it like you're like talking on the phone? You're like calling with a cell phone to tell them like, oh, turn on your carrier now?

**Dave Jones:** No, no. We try to keep away from the cell phones just because this is an amateur radio contest. And keep in the spirit of it.

**Chris Gammell:** Yeah. I see people on Twitter sometimes like, oh, I'm going to be on this wavelength now. It's like, why are you doing this?

**Dave Jones:** Well, yeah. You know, there's different reasons. There's what they call packet clusters for HF operations. If you're trying to do contesting or trying to work as many countries as possible, then it's more a question of is the propagation there, is your antenna there, than it is of coordination. But in this case, we really try and keep to using amateur radio equipment. And in California, we're lucky enough to have a very good UHF repeater system that is linked across the entire state. And that's essentially a repeater. We get on there and say, so-and-so is looking for contacts. I'm on top of Fraser Mountain, for instance. And then somebody who's available will say, oh, okay, yeah, I'm interested. Let's talk. I'm on another mountain and then set things up.

**Chris Gammell:** So on the repeater, you'll just use a handheld or something like that in order to actually talk. Exactly.

**Dave Jones:** Yeah.

**Chris Gammell:** I know that I had a lot of trouble learning the nomenclature when I started learning about this stuff. So, you know, you hear repeater and like, well, what the hell is that? And that's just a tower where-

**Dave Jones:** It's a party line. It's a party line. Yeah. Yeah. And during the contest, it gets incredibly busy. Oh, yeah. It's one channel for everybody. Yeah. And so, you know, you've got 30 to 50 people that are competing for space on this thing. And that's another challenge is to shout your way through the party line, to almost develop a voice that has got a certain characteristic people know or that people pay attention to.

**Chris Gammell:** Without your call sign, that kind of thing?

**Dave Jones:** Well, you use your call sign. But, you know, some people have distinctive voices and you say, oh, that's Robin, for instance. He's got a very distinctive voice. So, you know, certain things stand out.

**Chris Gammell:** I'm Robin. I'm on the repeater. Oh, ho, ho, ho, ho.

**Dave Jones:** See, if you got on, everybody would know, hey, that's Chris Gammell from the Anthem.

**Chris Gammell:** I'm leaving. Yeah. Okay. Well, that's cool. That's a good start to that stuff. You mentioned in a note you sent me about analog video. What's up with that? I mean, I think you mentioned earlier, too. So people send video with this or are they down or what's the deal?

**Dave Jones:** Yeah, they do. In Southern California, I believe there's a network of video repeaters that are used to basically have a conversation with somebody just with video.

**Chris Gammell:** Like Pictionary or what?

**Dave Jones:** Well, yeah. I mean, it's like a video conference, essentially. So, you know, it's not too popular. But, you know, the people that do it are pretty into it. And I believe they do it on 10 gigahertz and 2 and 5 gigahertz also. Yeah. But one of the cool things we do at our local club, the San Bernardino Microwave Society, they broadcast their meetings online through a microwave analog video link. So there's a crew that comes out and they set up a bunch of cameras in the meeting hall. And outside the door, they have this microwave dish that's pointed up to a hilltop where there's a repeater. And then this goes into their video repeater network and eventually makes its way into a website. And we get people all over the world watching the meetings. There's quite a few people that are interested. Yeah, yeah. It's all done on amateur radio wavelengths.

**Chris Gammell:** Yeah, we'll have to put a link in the show notes about that, too, because I bet some people might be interested in watching that kind of thing.

**Dave Jones:** Yeah, definitely.

**Chris Gammell:** Is that one of the bigger clubs in the States, at least?

**Dave Jones:** It's definitely the biggest club in Southern California, maybe even California. Yeah.

**Chris Gammell:** I mean, because there's a bunch of RF guys in Southern California, right? I mean. Yeah, yeah. It's based on industry.

**Dave Jones:** Yeah, yeah, exactly. And Texas as well. There's a North Texas Microwave Society. It's a pretty popular active group. But I'm obviously not there, so I don't really know all that much about what they're up to. But they do put out some excellent technical papers. And a lot of the meetings tend to have a very technical focus. We get people that come to speak that provide really interesting technical talks. We've had people that came out and discussed the very long baseline antenna array. We've had people from JPL come out. Really? So it's a pretty neat group. And part of it is that a lot of the people that do microwave amateur radio are themselves involved in the business of microwaves. It's one of those things where people that are really into microwaves just have the hobby and then they decide, oh, you know, I'll do this for a living too. Yeah. So that tends to be pretty popular among the microwave enthusiasts.

**Chris Gammell:** Well, it seems like there's only – I mean, not that there's only so many people who can do this, but there's only so many that are doing it, that kind of thing. It's like a very captive market, that kind of thing.

**Dave Jones:** Yeah, that's part of it too, yeah.

**Chris Gammell:** I mean, only so many people are looking up at the skies. But I have heard notice – I've heard people talking about, you know, doing hobby-level radio antennas for space reception kind of stuff, you know, actually doing radio telescope and that kind of thing.

**Dave Jones:** Yeah. Actually, there's a number of people who have very large antennas set up at their homes, very large pair-block dishes. And they've picked up things from the moon. I can't remember exactly – maybe the lunar reconnaissance observer satellite? I don't remember exactly which one. But they've picked up signals from the moon from satellites up there. So, yeah. And people are doing radio astronomy as well. Yeah. And also – That's what I was trying to think of what it's called, yeah. And there's actually been a fair amount of interest in the SETI people. Well, there doesn't seem to be a lot of cross-pollination, I guess, among microwave radio enthusiasts and SETI people. But they do tend to use some of the same hardware, which is precision pointing of large parabolic dishes and really low noise figure amplifiers. So there is definitely some commonality there among the two.

**Chris Gammell:** Well, you mentioned low noise stuff. I mean, let's get into the good chunk of this stuff. I mean, so this is not an easy thing to do. I think people who are listening have already figured that out. But what are some of the technical challenges? I mean, and especially with the mix. This is the really cool thing about it is the mix between electrical and hardware. Just go. I mean, it's just so much cool stuff. How do you build one of these things?

**Dave Jones:** Okay. Okay. So like everything, it depends, right? You can build a 10 gigahertz radio on an FR4 printed circuit board and it will work. But if you really want to get excellent noise figure, like below half a dB noise figure, you're probably going to have to use a higher performance substrate. So that'll mean sort of like a Rogers material, Teflon-based materials, things like that. So you start getting into exotic materials very fast.

**Chris Gammell:** What's a Rogers material? I've never heard of that before.

**Dave Jones:** Rogers is a company that makes low loss, high frequency dielectrics. Oh, okay. So these would be circuit board materials made from Teflon or ceramics, things like that, that have very low loss tangent and different dielectric constants than FR4 and also much more repeatable. So you start getting into those difficulties where if you're trying to build a circuit, you've got to start using these materials. And most of the cheap board vendors will not deal with this stuff because it's a totally different chemistry, right? For plating through holes and etching. The materials are softer, so they're harder to deal with. Things tend to squish around a lot. Multilayer boards are very difficult.

**Chris Gammell:** It sounds like you just start over, basically. You just say, all right, everything, you know, you guys call everything below a gigahertz DC probably, and then you say, all right, we're starting over. Let's just build something from scratch, that kind of idea.

**Dave Jones:** Yeah, yeah. Yeah. Essentially, you have to start over. You have to reexamine all the things you use, the types of metals you use, the types of semiconductors, right? I mean, silicon semiconductors, with the exception of silicon and germanium, don't work very well above a few gigahertz. And so we start using materials like gallium arid. And a few people are starting to look at gallium nitride. So these more exotic semiconductors are sort of the main tool of microwave amplification. And so to build a low noise amplifier, you have to use exotic semiconductors, exotic board materials. And then you start getting into the housings. So the housing of these things ends up becoming a significant part of the circuit. If your housing is too large or if it's too reflective, you can get moding that occurs inside the air cavity, and you can get resonances that, without the lid, are simply not there. So the housing becomes important. Yeah.

**Chris Gammell:** Well, basically, everything becomes a capacitor. That's kind of the basic idea, right? Is that different—I mean, FR4 itself, the dielectric of it makes it, you know, a crappy capacitor, and you start losing all your signal, right?

**Dave Jones:** Essentially. I mean, if you think about a transmission line, let's consider a 50-ohm microstrip transmission line. So this is just a line of metal across the top of a circuit board. Okay. You've got the inductance of the wire itself or the trace itself, and you've got the capacitance to ground. And both of those experience loss because they are propagating through the medium of the dielectric, the FR4, significantly. Some of it goes through the air above the board, but most of it goes between the conductor and the ground plane. Right. So that dielectric becomes very, very sensitive, and it's really a dielectric loss tangent effect. And it affects both the inductance and the capacitance, if you will. But it's mostly a propagation loss. Okay. Yeah.

**Chris Gammell:** Okay. So it's not like a DC loss or, you know, like you're not losing it to heat. It's just going away.

**Dave Jones:** Well, not for low-power stuff, which tends to be most of what microwave hams do. But at the lower frequencies, you know, one, two gigahertz or so, people are building 500-watt, 1,000-watt amplifiers. And there, yes, you do end up running into conductive losses that will cause your circuit board to explode if you have a mismatch. It's not pretty.

**Chris Gammell:** No, I believe it. Yeah.

**Dave Jones:** It's going to be a bad test day, right? Seeing a crater in a Teflon circuit board makes you think, wow, there's a lot of energy there.

**Chris Gammell:** Well, what about cost? I mean, so, you know, you're talking about gallium arsenide. You're talking about silicon germanium. Germanium diodes and stuff like that have been around a long time. But is it hard to find this stuff? Is it expensive to make all this stuff? What are we looking at here?

**Dave Jones:** It has been expensive. It has been difficult. But it's getting easier every day. Really? As more microwave technology is commercialized, we're getting a lot more access to good parts. And it really changed, I guess, in the sort of early 2000s, late 90s when the telecom industry sort of took off. With all the 2.4 gigahertz type of activity, all the wireless stuff, that really gave a huge boost to the industry in general. And a lot of that trickled down to microwave point-to-point links. So a lot more activity there gave us access to more gas parts. And, yeah, so it's not too hard nowadays. In fact, you can order parts from DigiKey. They sell low-noise gallium arsenide transistors, and they're just a few dollars apiece. More complicated circuits are available as well. So these are like, they're called monolithic microwave integrated circuits or MIMICs. And these are also available. Some of them are packaged and some of them are unpackaged. And you have to work with a bare die. And that's a whole separate challenge. But those parts are becoming more available, certainly. And with more parts being packaged, it's even easier. Hittite and TriQuint and, let's see, mini circuits. There's a number of companies that actually sell packaged gallium arsenide MIMICs. And they're pretty affordable. You can get stuff today that 20 years ago simply just didn't exist or required wire bonding. And so, yeah, it's not too bad.

**Chris Gammell:** Well, you touched on that. So let's go there because that's actually how people probably first heard about you on the show from our buddy Jeff Kaiser. He mentioned you as someone with a – he said his friend had a die bonding machine. And we were like, what? So when the hell did that happen? I mean, was it just a necessity to work in the hobby before? Is that kind of the idea?

**Dave Jones:** Well, I bought this several years ago. And it was a surplus thing. It came out of a hard drive factory in, I don't know, somewhere in the east, in Asia somewhere. And it is an unusual piece of equipment to have. And there's actually a number of people in the microwave hobby that do have functioning wire bonders. There's a guy in Portugal, actually, who's done a lot of really good work and published a number of articles and so forth on operation and design of wire bonders for microwave use. We tend to use gold wire and ribbon for most of our work. And it's the sort of thing that becomes necessary once you start going above a certain frequency. And that's probably around 25 or 30 gigahertz. Beyond those frequencies, there are very, very few packaged parts simply because the parasitics of the package are – just completely wipe out any gain that you might have otherwise.

**Chris Gammell:** Yeah, people thought their lead inductance was bad on their microcontrollers or something. It's like, you ain't seen nothing yet. Right, right. Oh, man, that's crazy.

**Dave Jones:** And, you know, even at frequencies like 47 gigahertz and 79, you have to start using multiple wire bonds to reduce your inductance to an acceptable level. So it becomes a little bit of an art, certainly, to do that.

**Chris Gammell:** So the actual bonding itself, I mean, what kind of – what size pads are you bonding to and actually like how do you go about – I'm sure there's like videos people could look at. But what size pads and how do you do it?

**Dave Jones:** Okay. So a typical mimic has usually a 50 micron square pad or 100 micron square pad. So, you know, these are very, very tiny pads. You certainly cannot do this without a microscope. And the bonding tool itself is – it looks just like a needle. It's like a fat needle. The tip of the needle is ground precision to just a little bit wider than the width of the wire, which is one mil, a thousandth of an inch. And – Oy. Yeah. So you have this – the wire bonder itself, to a large extent, is a mechanical reduction device. So you have a hand input device basically.

**Speaker ?:** Yeah.

**Dave Jones:** Okay. And there's a mechanical reduction that reduces all your movements by some order of magnitude so that you can accurately position the wire and then squish it. And the wire bonding itself is a thermocompression weld. It's actually a welding of the wire to the pad on the dot.

**Chris Gammell:** So soldering is for wimps, that kind of thing. It's just – if you need to get solder out, you're screwed. That kind of thing?

**Dave Jones:** Yeah. Yeah. Solder is a problem and largely because of the gold. Most gallium arsenide devices use gold metalization and the gold and lead don't mix at all. Or they do, but too well and then it becomes a problem. Yeah.

**Chris Gammell:** It becomes mostly lead at that point then. Yeah. Yeah.

**Dave Jones:** And it becomes brittle and it cracks and fails and, you know, that's no fun.

**Chris Gammell:** And then you have a bad test day. Yeah. Yeah. Exactly. Exactly. So the weld itself, is it from the amount of pressure you put on it that it just welds or how does that work?

**Dave Jones:** It's a combination of direct pressure and heat and vibration. So this needle tip or a wedge as it's called will vibrate back and forth with an ultrasonic transducer. And so this acts to scrub the weld and induce a lot more energy into the contact. And as well, there's also some heat involved. You heat up the whole thing to about 150 degrees Celsius. And the combination of all those things makes a pretty solid contact. And it becomes a single piece of metal. It's an intermetallic bond that occurs. And it's quite an excellent performing contact.

**Chris Gammell:** Yeah. I had actually just heard – there was a video a couple weeks back about a very different scale. It was about a high-speed rotation welding where you spin something up at a very high speed. And then you kind of just smush it together and the friction from that does it. And then my coworker told me about the same thing of ultrasonic welding. And I had never heard of that before. Apparently, it's used in a lot of different applications. Yeah. A macro scale as well as this tiny, tiny macro scale.

**Dave Jones:** Right, right, right. Yeah. There's all kinds of strange welding techniques. There's laser welding. I saw another video recently about friction stir welding where you take a probe that is spinning around and you just run it through the two pieces of metal. And just – it's crazy the amount of force involved. But yeah.

**Speaker ?:** Yeah.

**Dave Jones:** These equipment makers are badass, right?

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** And not to mention explosive welding. That's even more interesting. They take sheets of metal. Like say you want to attach copper to aluminum. Yeah. You take the two plates, stick them inside of a cave, surround them by dynamite, and explode the two things together and you get a pretty solid weld. Yeah.

**Chris Gammell:** Well, that's how they do it. Wow. That's insane. So, okay. So, now you – where are the wires coming from? Are they coming from the Teflon – other components on the Teflon board?

**Dave Jones:** Well, yes and no. Usually with Mimics, you connect them with transmission lines. So, this will either be a Teflon board or actually a hard substrate, which is a ceramic dielectric like alumina. Alumina oxide is the most common one. And those come in little strips and you can cut them to length. And that's a whole other ordeal. And then you attach – you basically stitch these pieces together. You have one mimic. You have a substrator transmission line. And you stitch it together. And then the next one and so on. So, these tend to be sort of series circuits of amplifiers or mixers or whatever. To get DC in, you typically have bypass capacitors that are really close to the chip, to the Mimic. Those will either be a single-layer dielectric capacitor, which looks a lot like a Mimic itself. And then there's porcelain capacitors that are also used. And once you get past that point, you can just go to a regular circuit board because all the RF is gone. But getting into the microstrip world and back out is another challenge.

**Chris Gammell:** So, this would be if you had your transceiver. You mentioned before a single sideband transceiver that you plug in to actually get a generated signal, right?

**Dave Jones:** Yeah, yeah. Well, okay, yeah. So, in terms of low frequency, that's actually pretty easy. You can just tie a wire directly from a piece of coax to your Mimic or through a substrate, something like that. But actually getting the microwaves or millimeter waves from the Mimic into free space can be pretty tough, especially if you're not using a connector. And a lot of times at the higher frequency, you're using waveguide. So, we go from a microstrip into a waveguide. And that's where precision machining comes into effect. And one of the things that I showed you at the Maker Faire at Jerry's dinner party was this 47 gigahertz down converter module. And what you saw there was a housing that incorporates a waveguide transition to microstrip. And that...

**Chris Gammell:** Right. So, basically, Tony walked up to me. He's like, hey, check this out. And this is probably two-inch by three-inch piece of aluminum that he frigging milled with something. I don't even know how he did that. And then there was a bunch of circuits inside. And I'm like, I have no idea what I'm looking at. I honestly had no idea. Yeah. I could kind of ascertain that it was circuits, but it was very foreign to me.

**Dave Jones:** Yeah. So, let me get this out of the way first. This is sort of at the ridiculous end of the microwave hobby. You don't have to go to this extreme to have a lot of fun with microwaves.

**Chris Gammell:** And there's a lot you can do. Everyone just shut off the pod. You know, like, never. I'm never going to do this. Yeah. Yeah.

**Dave Jones:** But if you like the challenge, it's there. Yeah. And there's a purpose for it, right? I mean, you can use this to contact one other person in the world.

**Speaker ?:** Yeah.

**Chris Gammell:** Well, and it's just cool, too. I mean, like, I think a lot of electronics hobbyists or even professionals, you know, they – there's – sometimes it's just you're sitting at your lab bench and there's not as much connection to the physical world other than blinking an LED or, you know, turning a servo or something like that. Right, right. Sometimes getting your hand on metal is awesome. I was mentioning to my wife, like, how I want to take machining classes because it's just – it's such a tangible, awesome thing. Yeah. You know?

**Dave Jones:** It's just – And then when you connect the two, that's where, for me, there's a lot of magic that happens because it's like, wow, I'm going from this piece of rectangular pipe into a bare die and it's receiving a signal from 100 miles away. It's kind of cool. Why is this working? Why is this working? Well, more amazingly is this is working. Wow. Yeah.

**Chris Gammell:** Yeah. Yeah. That's true. Okay. So you're actually – when you do the machining of this little metal – first off, do you have pictures of this thing we can post? I'm guessing you probably do.

**Dave Jones:** I have some stuff on Flickr that I can link to. Okay. Yeah. Yeah. So we'll have pictures up there.

**Chris Gammell:** So you're going from like an SMA connector? I don't remember what the connector was.

**Dave Jones:** Yeah. So for the IF port, which is at 144 megahertz, it's an SMA connector, which is overkill, but it's small and easier to work with.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** The local oscillator port is at 23 gigahertz and that's also an SMA connector and I incur a lot of loss there. It's several dB of loss that occurs simply because that connector is not really rated to that frequency. Yeah. And then once I get inside the little aluminum box, it jumps down with a piece of – I think I just use silver epoxy to get down to the circuit board.

**Chris Gammell:** Is that like high-frequency RF glue basically? Yeah. Is that kind of – Yeah. Yeah. Yeah. It's the duct tape of microwave. It's the duct tape of microwaves. Yeah. Certainly. Yeah. Yeah. Yeah. Okay. And then so it's – then it's actually in a waveguide channel, right? I mean that's – Well, okay.

**Dave Jones:** Let's step back. We're saying you come in with the IF port, which is low frequency, and the local oscillator, which is higher frequency. You go through a mixer and then you go throughout – through the RF port eventually. That's where it's waveguide.

**Chris Gammell:** I hate to take an even bigger step back of what IF and local oscillator is, but maybe you could generalize that.

**Dave Jones:** So these microwave radios that we built are usually not full-on radios, but they are frequency converters. And so we'll go from an intermediate frequency, or IF, of about 144 megahertz usually. And that's the frequency that we can use a normal ham radio with.

**Chris Gammell:** Yeah.

**Dave Jones:** The radio does all the radio stuff and we do all the microwave stuff. So the IF frequency is the intermediate frequency. And that gets mixed with the local oscillator, the LO. And that is a much higher frequency. And in the case of my 47 gigahertz radio, it's 23 gigahertz. And the reason for that is the mixer is something called a subharmonic mixer. It multiplies the LO, which has a number of advantages. But anyway, the point is that there's three connections.

**Chris Gammell:** Basically how the math works out is kind of the idea.

**Dave Jones:** Well, the advantage is that it's easier to build a 23 gigahertz oscillator than it is to build a 47 gigahertz oscillator.

**Chris Gammell:** You know, I was saying that the other day. It's like, oh, geez, these 23s are just kids' play. Yeah. Put one in an Altoids 10, you know, whatever. Yeah.

**Dave Jones:** You know, an Altoids 10 might work okay. I'll have to try that.

**Chris Gammell:** Yeah. Well, you'd fit in with the hobby crowd.

**Dave Jones:** That's true. Especially if I put a 555 timer as the local oscillator source as a reference.

**Chris Gammell:** Yeah. There you go. Yeah. Good luck with that. Yeah. Okay, so now we've got this high frequency. I'm guessing we could probably link people to videos on how, like, you actually do mixing and stuff because that's a whole class at college, right? I mean, like, that's some pretty advanced stuff. That's, you know, conceptually, you can eventually wrap your head around it, but the math and practice is not worth it.

**Dave Jones:** The simplest way to think of it is adding and subtracting frequencies. So if I mix 144 megahertz with 1,000 megahertz, I'll get 1,144 megahertz out of it. A bunch of other stuff, too, but for the moment, we'll just add. On the other end, when you receive a signal at 1,144 megahertz, you pump in that 1,000 megahertz and then you get back out that same 144 megahertz.

**Chris Gammell:** That's a good explanation. I like that.

**Dave Jones:** That's so, yeah.

**Chris Gammell:** If only you would have been sitting in my signals class almost so many years ago. Yeah. Yeah. Okay, so now we're on the waveguide, right? So this is actually in the aluminum box. We have a very high frequency signal and it's actually traveling on the waveguide. Is that the idea?

**Dave Jones:** It starts off traveling on this aluminum substrate on a 50-ohm transmission line, very much like what you'd see on a regular printed circuit board, just a lot smaller. And then that transmission line sticks out into the waveguide and by magic, that signal... Whoa. Yeah. Okay. Yeah. By magic, and that's a lot of electromagnetic theory. That's what it feels like. Yeah, yeah. That signal couples into the waveguide and the microstrip mode becomes a waveguide mode and then the signal now propagates through the waveguide.

**Chris Gammell:** And could you explain what a waveguide kind of looks like? I mean, people can look... We'll look at, you know, Wikipedia pages and stuff like that. We'll link in, but...

**Dave Jones:** It's a rectangular pipe.

**Chris Gammell:** All right. That's good. And it's... But it's mostly... Is it solid? Is it air or what is it? Yeah.

**Dave Jones:** Oh, okay. So it's a pipe filled with air. Okay. And there are dielectric waveguides. They're, you know, filled with styrofoam or plastics, things like that. And you can adjust various things to do different types of operation of waveguide. You can come out with antennas straight out of the waveguide using dielectrics. A number of applications there. But most hams use just air dielectric waveguide. And it just... It varies in size. Waveguides come in all different sizes from, you know, the size of a room to fractions of a millimeter across. So... Yeah. Yeah.

**Chris Gammell:** Is there any brief explanation of why that works? Or we're just going to stick with magic as well?

**Dave Jones:** Let's stick with magic for now.

**Speaker ?:** Okay. Lord.

**Chris Gammell:** But you actually... So when you constructed this aluminum box you handed me, this was... Did you, like, measure out how big you wanted it to be and everything? Is that kind of... Yeah. Yeah.

**Dave Jones:** I did a lot of simulations with some electromagnetic... Did you use, like, HFSS? HFSS. That kind of... Yeah. Yeah. And there's a number of people that have access to that. And, yeah. So HFSS is one of the tools that was used. And it took a little bit of work going back and forth between actually making this thing and then the simulation. The dimensions get so small. At 47 gigahertz, the waveguide is less than a quarter inch across. And, you know, if you think that a tenth of that is going to make a difference, and it does, then you're talking very, very small dimensions. And actually building this accurately, machining it accurately, becomes pretty tricky. Yeah. And it takes a lot of time. So...

**Chris Gammell:** Well, what did you use to machine it then? I mean, what is... I have a... What kind of gear do you have?

**Dave Jones:** I have a $300 Harbor Freight benchtop milling machine.

**Chris Gammell:** The pinnacle of precision, folks. Absolutely. Absolutely.

**Dave Jones:** But, you know, the truth is, if you use slowly enough and using careful measurements, you can do good enough, at least for 47 gigahertz.

**Speaker ?:** Yeah.

**Dave Jones:** Now, I've also used some other tools that people have. I had a friend that worked at a machine shop that did very precision electrical discharge machining. And this is a type of machining where you take either a wire or a piece of metal and you apply a current across the tool and the piece being worked on. When they come in contact, there's a discharge that occurs and it eats away the metal. And after time, you can basically bore your way through a metal block very precisely. And in waveguides, the main reason to do this is that you get sharp corners. And you can get very nice internal flat surfaces with sharp corners. And I had access to this shop for a little while, got some very nice CNC EDM work done. And that was another part of it. So the other part of the microwave hobby is that you've got to be resourceful. And yeah. In figuring out who's got tools, who do I need to know? You know, where can I get cheap surplus parts, that sort of thing. So it's definitely a networking sort of thing, too.

**Chris Gammell:** Oh, that's good. It keeps it social. I mean, it seems like it's... I mean, any part of ham is usually social, at least. You know, they're trying to get together and you need someone to talk to. So that's... Right, right. That's always a good part about the hobby, I think. Yeah.

**Dave Jones:** And that's... You'll find that most microwave amateurs are really interested in getting other people into the hobby because, you know, we're tired of talking to the same people. We want to talk to new people.

**Chris Gammell:** Have you talked to Jim? He's so frigging annoying.

**Dave Jones:** No comment. Yeah.

**Chris Gammell:** Yeah. Nice. So you mentioned sharp corners. Why does that matter?

**Dave Jones:** Well, actually, truth be told, it doesn't matter too much. But an ideal waveguide does have sharp corners. And, you know, at a wavelength that's a quarter inch across, most machine tools on a milling machine are going to have a pretty good size radius. And you will get that ideal waveguide. You'll get something like an oval. Gotcha. And they don't quite perform as well.

**Chris Gammell:** Okay. So you just mean the corners of the rectangular channel you're making, not the...

**Dave Jones:** Yeah, the internal corners of the waveguide. Okay. Yeah. Yeah.

**Chris Gammell:** Okay. So then you get to the end of this waveguide. What's at the end? Are there other components that you're connecting to? Or what's the deal?

**Dave Jones:** In my radio, no. No. I have a switch at the end. And that switch is another mechanical piece. And it's actually a lot like a piece of plumbing. It's a... You just keep regressing here, you know? We call this plumbing, actually, in the microwave world. Really? Yeah. We try and keep away from plumbing as much as possible because it's a pain to machine all this stuff. But at some point, you do have to get to it. And in this case, this switch is actually a rotating cylinder, a solid rotating cylinder with a channel, a curved channel machined out of it. And that curved channel rotates between two of three ports on a cube. One port being the antenna port and the other two being the receive and transmit ports. So it just... It becomes a single waveguide as it rotates.

**Chris Gammell:** So it's basically a mechanical selector switch between these different pipes.

**Dave Jones:** Yeah, exactly. It's exactly what it is. Yeah.

**Chris Gammell:** That is so weird that it... Like this super high frequency that you eventually just... It's like regressing to...

**Chris Gammell:** Yeah. You know, like herding sheep or something. Yeah, it is.

**Dave Jones:** And actually, it could be a problem because you can get dust in there. And, you know, junk can get inside and start causing problems. And there's not really a great way to keep it out because, you know, anything is lossy at these frequencies. So you can put windows over it, but they're a little tricky.

**Chris Gammell:** Yeah. Wow. Could you take a step back real quick to the actual electronic side? So are you actually... When you mentioned mixers and amplifiers and stuff like that, are these actually like multi... I'm used to op amps, right? Mm-hmm. And the low frequency analog stuff. But do these kind of... Is it just like single FETs and single transistor kind of solutions? Or what do they actually look like in the electronics?

**Dave Jones:** Yeah. A lot of it is a single transistor, sort of a common source amplifier arrangement. That's what most of it is. And it's gallium arsenide FETs for the most part. A typical mimic, which is probably the most complicated thing we're going to use in microwave bands, will have at most a dozen transistors. And that's partially a yield thing. They just can't make mimics with thousands of transistors. They just don't yield. The gates are written by electron beam lithography, usually. And that's just not a high yield process. So yeah, we deal with...

**Chris Gammell:** Although that is getting better. Did you see that deal that Intel inked with ASML, rather?

**Dave Jones:** No, I haven't seen that.

**Chris Gammell:** Yeah. So Intel, a little bit of electronics news, ASML, the big litho vendor that works with Intel and Samsung and everybody else, basically they said EUV is the next step after the current 190 nanometer lithography stage. And basically they said, well, we'd love to build the next generation machines, but we can't because it's so expensive. It's 13 nanometer light. It's like you said, it's EUV, so you have to have this basically like rastered litho, which makes it very difficult and very expensive. And so they said, well, Intel, you got to foot half the bill. Samsung, you got to foot... I mean, basically they sold parts to their company in order to get buy-in.

**Dave Jones:** Yeah, I guess if you start throwing huge sums of money at it, you can solve it. And that's the thing that microwave has not had that sort of money that Intel has had. It's a more niche market, so it hasn't had that sort of development money.

**Chris Gammell:** Well, maybe you'll see some benefits, though, from the technology kind of shrinking. Everything's shrinking, right? So that could eventually help you.

**Dave Jones:** It could be. There are a lot of differences between the processing of the two different materials. So it's hard to say what would transfer over. But yeah, definitely the machinery would help.

**Chris Gammell:** Yeah, and they keep moving to different... Like you mentioned, gallium nitride isn't very common yet, but that's... That's a big part of LEDs right now. We've had John Creon, or John Edmund of Creon here, and he talked... That's their main thing.

**Dave Jones:** Yeah, well, gallium nitride is certainly the future for microwave. And it's just that so far there aren't a lot of sort of established vendors of high-frequency microwave parts available to the amateur radio community. The focus has primarily been on the lower frequencies, you know, a couple gigahertz sort of range for cellular base stations where power amplifiers make sense and where you can afford the power and where there's a market for it, basically. But there's definitely a future in microwaves and millimeter waves for gallium nitride. Definitely. That's cool.

**Chris Gammell:** So you mentioned the difficulty of processing this stuff. I mean, where are most of these parts made? I mean, you mentioned Hittite, TriQuint, and mini circuits, right? You lost me. I've never heard of them.

**Dave Jones:** Yeah, there's a few foundries. Let's see. TriQuint is definitely one of the bigger ones. Wind Semiconductor has a 3-5 compound fab.

**Chris Gammell:** A 3-5 referring to like gallium arsenide.

**Dave Jones:** Gallium arsenide, gallium nitride, indium phosphide, and there's some others that are not quite as important.

**Chris Gammell:** Yeah. All the fancy stuff. Yeah.

**Dave Jones:** Well, that's why TriQuint is called TriQuint. Ah. 3-5. Uh-huh. Nice.

**Chris Gammell:** That's pretty good. Yeah. Yeah. Okay. Cool. So, man. Oh, test equipment. This has got to be the last thing we talk about because we're starting to... Okay. We're already about 10 minutes over, I think. Wow. But what the hell? How do you look at this stuff? I mean, other than that guy standing in the field, you mentioned earlier that you need to be able to buy equipment, and that's why you're kind of ramping up. Starting a company to do it. Yeah. Start up Reactance, which is brilliant. I think that's very smart. What do you buy? What do you need?

**Dave Jones:** Yeah. Well, okay. So, the principal pieces of test equipment that you need are a power meter and a spectrum analyzer. Maybe a frequency counter. But the truth is, there's a lot of really old equipment that you can use. Yeah. For instance, I have a spectrum analyzer that I bought for $100, and it goes to 12.4 gigahertz. Really? But this thing was built in 1968. So, you know. It's awesome. It's very old. Yeah. It has served its purpose, but it's time to go. Yeah. So, I'm upgrading to a much newer, probably 1985 vintage spectrum analyzer pretty soon.

**Chris Gammell:** Yes.

**Dave Jones:** So, yeah.

**Chris Gammell:** You're going to have a CRT in that baby. That's right. Yeah. No more of those dials and needles.

**Dave Jones:** No, hand cranks.

**Chris Gammell:** Really?

**Dave Jones:** This thing had a hand crank, yeah, to tune the frequency. No. That's awesome. It has this chain inside. It's crazy. Oh, you do pictures of that thing, too? No, I don't. But if you're interested, it's an HP 851 spectrum analyzer.

**Chris Gammell:** HP 851. Okay. Yeah. That'll be a good start. And it's got a round CRT. Yeah. Back before they had a rectangular one. So, you mentioned power meters, too. Are you a big Bird Electronics fan?

**Dave Jones:** No. No? No? That's good for lower frequency stuff and higher power stuff.

**Chris Gammell:** Oh, gotcha.

**Dave Jones:** But for microwaves, I have, again, an old HP 432 power meter. And this is actually a resistor base. It's a ballometer. Ballometer. That's a new name. Yeah. It's like a ballonimeter, basically. That's what it sounds like. Yeah, pretty much. Yeah. You're full of balloni. Yeah. And it'll tell you that, right? Yeah. You think you've designed a great amplifier, but no. No, you're full of balloni. Yeah. Yeah. But it's a very old way of measuring power. It also has served us time, and it's ready to go. And it's making way for a diode-based power meter. Interesting. Yeah.

**Chris Gammell:** So if you were to buy this stuff new these days, I mean, who are the big vendors of this kind of... I see stuff for like 60 gigahertz scopes, and I'm like, who the hell buys these? Is that actually your market? I mean, or is it... You can't even bother.

**Dave Jones:** Oh, no. I don't even bother. But the cell scopes, at least, probably don't get a whole lot of use in the microwave community just because we don't care so much about what our waveform looks like. It's always going to be sinusoids, and we're not trying to get sharp rise times, things like that. But the big vendors are going to be Agilent, Rodion Schwartz, and Ritsu. Those are probably the three big ones. There are a number of others, but a lot of this stuff is extremely, extremely expensive. Oh, yeah. Hundreds of thousands. A 50 gigahertz spectrum analyzer will be as much as a Ferrari. So people should buy kits from Tony so he can afford one.

**Chris Gammell:** That's right. Oh, man. So what is the upper range right now? I mean, I guess that's another question. How fast can you go?

**Dave Jones:** In terms of frequency of radios that we can build?

**Chris Gammell:** Well, yeah, so you mentioned a 400-some gigahertz. Yeah, yeah. How do you measure that?

**Dave Jones:** That's a good question. Test equipment does exist to test those, but again, it's in the Ferrari range or higher. I think a lot of people test them by seeing if they can receive a signal by something else that was built the same way.

**Chris Gammell:** Oh, okay. So it basically builds your own test equipment like how scientists do it all the time.

**Dave Jones:** And that's what I did with 79 gigahertz. I built two radios in part because there's nobody else to talk to, but also because it's nice to be able to test out the equipment and see if it's working. Yeah. And that was an easy way to do it. Easier way to do it, I should say.

**Chris Gammell:** So did you eventually find someone to talk to with it?

**Dave Jones:** Yes. I found one other person in the Southern California area. Sweet. There are a few in the U.S., so got to try and talk to them too.

**Chris Gammell:** I guess you have to work on your social skills to make sure that you make friends with them too, so you're not like, hey, I need to test something.

**Dave Jones:** Yeah, yeah, yeah. Well, that's also part of it. You know, one of the things I was doing yesterday at this tune-up day was getting a feeler for where people are going to operate during the contest so I can say, okay, I want to set up here because I want to talk to these guys on these frequencies, that sort of thing. So there's definitely a bit of social engineering that's required to get what you want out of the contest.

**Chris Gammell:** Yeah. Yeah. So you also mentioned the oscillator, rather. So what are you sourcing these frequencies with? I mean, it's not actually a piece of like, it's not a signal generator, right? It's actually like a crystal that you're playing with?

**Dave Jones:** Yeah, yeah. On all my radios now, I start from a 10 megahertz ovenized crystal oscillator. And it needs to be ovenized because when you multiply it by 5,000 times, the stability becomes a real issue, especially when you're doing this narrow bandwidth stuff. If you're off by, you know, a kilohertz at 50 gigahertz, it's going to be really hard to find a signal when you have a 100 hertz wide filter. Right. So yeah, sometimes people use rubidium oscillators. And this is one of those things where you can get really exotic technologies and it makes sense in microwave because you actually need that performance. Yeah. But yeah, so I start with a crystal oscillator and then I use a phase lock loop synthesizer, which is one of my React and Slabs products. To...

**Chris Gammell:** Yes, we got to the plug, people.

**Dave Jones:** Exactly. To get up to usually around two and a half gigahertz or so, at least for 10 gigahertz. And then I have multipliers, which is a future product. And then you start getting into the microwaves, really. And so most people nowadays use synthesizers, frequency synthesizers.

**Chris Gammell:** Okay. So it goes oscillator, synthesizer, multiplier?

**Dave Jones:** Yeah. Yeah. That's the typical thing. And there's also dielectric resonator oscillators that people use that are phase locked to a crystal. There's giga oscillators, which is a very strange type of oscillator. If you want to look it up, it's YIG.

**Chris Gammell:** Yeah, actually, I mentioned a very high frequency thing the other day about that. And it was actually because my old boss used to work on those. He used to work at HP on YIG synthesizers and stuff like that.

**Dave Jones:** That's quite an art, from what I understand, to actually make a YIG oscillator work.

**Chris Gammell:** It's basically like building a very tiny tuning fork out of a very rare material.

**Dave Jones:** It's a sphere of this weird stuff. Yeah. And you put it in magnetic fields to make it...

**Chris Gammell:** Yeah, it sounds very Star Trek kind of shit. I mean... So are you actually ever dealing with that kind of stuff?

**Dave Jones:** No. I mean, I have some YIG oscillators and I've used them. But in terms of actually building a YIG oscillator, no, I haven't even thought of attempting that.

**Chris Gammell:** And could you afford one? Or no? I mean, like... You said you have them. So how do you get those?

**Dave Jones:** Well, you can get them on eBay, right? Like everything. There's actually a lot of YIG oscillators available out of cell phone base stations, wireless point-to-point links, things like that. Okay. So they are available. They're not too expensive. Maybe $50 or $100 for a YIG oscillator with synthesizer. So... Okay. Okay.

**Chris Gammell:** So you'll actually like either buy them or... Do you scavenge them too? Oh, yeah.

**Dave Jones:** Yeah. Definitely. Definitely. I go to electronic swap meet. There's a really great one near me. Yeah. Surplus electronic stores. It's a big hunting thing to try and find cool parts. And when you do, you brag about it to everybody.

**Chris Gammell:** Oh, yeah. Yeah. It's like hoarders basically, right? You got your... Yeah. Your pile of YIG oscillators and you're like, yeah, you can't have them. Nah.

**Dave Jones:** Yeah, pretty much.

**Chris Gammell:** Yeah. Oh, man. That is crazy. This is... It's a very interesting... So we didn't get into this. How the hell did you start in this again?

**Dave Jones:** Oh, geez. That's a really good question. I got into ham radio when I was like 12, I guess, 12 or 13. And I don't know why, but at some point, just the idea of microwaves appealed to me. I started in ham radio being interested in satellites and talking to satellites and talking to the space shuttle, things like that. Yeah. And then, I don't know, at some point I just thought, hey, microwaves are cool. And there was a club in San Diego where I grew up and I started going to their meetings and they helped me out. You know, they're like, hey, I'm a kid.

**Chris Gammell:** How old were you at this point? You were like 13?

**Dave Jones:** 15, 17 years old, something like that. Wow. So, yeah. I got lots of help. I bet, man. That's one of the things about the microwave clubs that exist. You can get people that will help you out. They'll loan radios, too, if you want to use them to get your feet wet, that sort of thing. Yeah.

**Chris Gammell:** Oh, yeah. I mean, Elmering is a big part of ham radio in general. Yeah, definitely. If people don't know, Elmering is what they call basically mentoring. Mentoring, yeah. Yeah. Yeah, that's great, though. I mean, and that's the thing. Usually, it seems very intimidating from the outside. I was very intimidated by the whole thing on the outside. And then I went to go take my technician test, and I walk in, and I'm like, these guys look at my grandpa. I mean, it was all just a bunch of old guys drinking coffee and talking about ham radio. It's just another hobby, really. It is. Yeah, yeah. And then yours is just another smaller sliver of that. Right, right. So, that's really cool, man. And then that's actually what got you into the college thing and everything else, right?

**Dave Jones:** Yep. I said, hey, I can make money doing this. Why not? Yeah.

**Chris Gammell:** And you do. I mean, we didn't talk about your day job, but I mean, you do this for a day job, and then you come home at night, and you do that, too.

**Dave Jones:** Yeah, pretty much. That's a good sign. That's a sign of passion.

**Chris Gammell:** It's something I like. Yep, definitely. That's great, man. That's really great. Okay, so let's go through where people can find you. First off, reactinlabs.com. Reactinlabs.com. That's right. We'll link in. And you actually have stuff on sale now?

**Dave Jones:** Not yet. I'm actually getting ready to order parts for my first set of kits, which will be those frequency synthesizers we talked about. Okay. And those are going to be available probably in the next couple weeks or so. Okay. So the OpenSynth, different numbers afterwards. Yeah, OpenSynth. Yeah, that's right. And it's a synthesizer that uses an Atmel processor, and it's, you know, the source code's available, and it's got an in-circuit programming port. It's got extra I.O. pins and stuff like that, so you can use a synthesizer for other purposes besides just a local oscillator. You can use it for a beacon or, you know, whatever you want.

**Chris Gammell:** So, you know, is this open source hardware, or does it not even matter at this point because who's going to build other ones?

**Dave Jones:** I mean, yeah, it's open source. I'm going to publish all the schematics and BOM and, you know, all that stuff. Yeah. Definitely, I want to keep all my stuff open source. I'm not sure if I'm going to actually, like, bother to put the license up or anything. Yeah. I don't really care.

**Chris Gammell:** I mean, I feel at a certain point, it's just like, well, you know, you can take whatever. I mean, even if it was closed source, it's like, well, you know, what are you going to do about it?

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Go figure it out, buddy. Yeah, yeah. You can figure it out. You get to keep it. So looking at this thing, there's a little heat shield, and then is there actually like a, yeah, what's underneath the heat sink?

**Dave Jones:** Okay, well, that circuit, actually, there's a few things. On the top side, that large thing you're looking at is a heat sink attached to the synthesizer module. Okay. And this is a synthesizer module that Mini Circuits makes. Okay. And inside of there is a phase lock loop synthesizer chip, an analog devices chip. And there's a voltage controlled oscillator as well as a loop filter. And all that is in that little tiny module. Yeah. And Mini Circuits sells these from frequencies of about 400 megahertz all the way up to four gigahertz. They're really good performance. And by using these modules, I can cover that whole range without having to design 100 different circuits for optimum performance. And so you order from me the one that you want, or you can order one without the synthesizer on it. And the rest of the board has the microcontroller. And it has a buffer amplifier for the output. And on the backside, it has a pair of ultra low noise voltage regulators. And this is kind of interesting because I started out using LM317s for the thing. And the phase noise was 10 to 15 dB worse than it should have been. So I had to go to this discrete route, and I use a ultra low noise voltage reference, some low noise op amps, and it's a much better solution.

**Chris Gammell:** So you just do like a compare, and then you drive a FET, that kind of idea?

**Dave Jones:** Yeah. Well, it's just a BJT path transistor. Oh, BJT. Okay. Yeah, with a voltage divider. Yeah.

**Chris Gammell:** Nice. That's great. Yeah, that's cool. I like it. And then in the future, you're going to have, what was the other thing you said you were going to have? Yeah.

**Dave Jones:** I'm going to have some frequency multipliers. This is the next thing. I've got some prototypes that are working really well that will take the output of these synthesizer boards and put a signal out in the 8 to 13 gigahertz range. And with about plus 15 to plus 17 dBm of output power. Wow. Those probably won't be kits because they have QFN packages. And, you know, it's hard enough for people to buy a kit that's all surface mount, but having them do reflow soldering is probably kind of not going to happen.

**Chris Gammell:** Some of our listeners do it. Oh, absolutely.

**Dave Jones:** Definitely. But, you know, it's one of those things where a lot of hams aren't too familiar yet with reflow soldering.

**Chris Gammell:** Right. Right. Yeah, this is cool. This is kind of bridging the gap between hams and, you know, circuit weenies like us, right? Yeah. Yeah.

**Dave Jones:** That's good. That's good. And it's all in FR4, actually, all this stuff that I'm doing. And, you know, it seems about 12 or 13 gigahertz is the upper limit, but I'm going to try and do a 24 gigahertz multiplier after this. So if that works, then I've got a whole bunch of other cool ideas that could work.

**Chris Gammell:** So no plans to have the Harbor Freight Mill running 24-7 and shipping metalized containers?

**Dave Jones:** No, no, no. That 47 gigahertz radio took me three years of work to build. So that wouldn't be a profitable endeavor by any means.

**Chris Gammell:** Well, I mean, if you – no, yeah, you're right. That would never work. Yeah. Okay. So people can find you on Twitter. Is that right?

**Dave Jones:** Yeah. I'm at mmwave, millimeterwave on Twitter. Nice. Nice.

**Chris Gammell:** Okay, cool.

**Dave Jones:** Yeah, that and React and Slav is about it. Okay. Well, that's good enough. And I'm sure people can – Or my radio calls. You can find me on microwaves, right? KC6QHP. Very nice. Very nice.

**Chris Gammell:** Okay, cool. And if people have questions, they can leave them in the comment section as well, and we'll get those over to Tony. And, yeah, it's been great. Yeah, it's been excellent. Excellent. Thank you for being on the show, and thank you for telling us about this. This is cool as hell, I have to say. It's just – Sure, no problem. My awe continues, so.

**Dave Jones:** Well, I hope other people are awed but also inspired to look into it and get interested in the hobby.

**Chris Gammell:** Yeah, and we'll definitely put as many links as we can find in getting people involved in the show notes.

**Dave Jones:** Yeah.

**Chris Gammell:** All right, great. Thank you very much. Well, we'll talk to you soon. All right. Talk to you later.

**Chris Gammell:** Bye.

**Chris Gammell:** So, how much do you like living in Southern California?

**Dave Jones:** Well, I like it a lot. But, you know, now that I've been on the Amp Hour, I think that means I get a job offer from Valve, right?

**Chris Gammell:** Oh, yeah. You better pack up your parka. You might have to head up to the upper northwest. That's right. Hang out with Mr. Kaiser. Yeah. Give him his mic back. It was a nice one to send that to you. That's true. Yeah.

**Dave Jones:** Yeah. It's a definitely nice microphone. Oh, yeah.
