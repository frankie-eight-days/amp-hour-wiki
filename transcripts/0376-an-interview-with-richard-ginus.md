---
episode: 376
title: An Interview with Richard Ginus
url: https://theamphour.com/376-an-interview-with-richard-ginus/
---

**Chris Gammell:** This is the Amp Hour Podcast. Released January 21st, 2018. Episode 376. An interview with Richard Hines. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I am Richard Hines of TWTG. Welcome, Richard. How are you doing? I'm doing great. Where are you calling in from today?

**IoT:** I am calling from the city of Rotterdam in the Netherlands.

**Chris Gammell:** Very cool. So tell me about, I mean, what's it like working electronics out in the Netherlands? I have not been, although as we were talking about just before the show, that may be changing. I need to verify my travel plans.

**IoT:** Okay. Well, the scene is really great, especially for IoT. Innovation is really high on the agenda on most companies in the Netherlands. So all the major companies have something on their agenda that has to do with IoT. So there's a lot of work in this field.

**Chris Gammell:** And is there like a cultural reason for that or just a technology reason? Or is it university-based? What actually drives that?

**IoT:** We have a couple of technology universities that are pretty active. We are well known for solar applications. Yeah. And the solar race in Australia. We also have Philips. Philips is... Oh, I've heard of them. Yeah. Yeah. Kind of big. Yep. Well, they mostly went into NXP. NXP also has a lot of jobs. And ASML, it's... Oh, yeah. Lithography.

**Chris Gammell:** That's a huge one. Okay. Yeah. I didn't know that was there, actually. I knew... I know the name, but I guess I didn't know where it was. So, okay. And so what are the universities like there, too? I mean, like, is that a lot of... That's a lot of the source of that stuff? Or is it more corporate-sponsored research?

**IoT:** I think it's a lot of corporate-sponsored research. Also, a little bit of... In schools, you already get the IoT stuff in schools. It's really... The connection between business and school is really good, I think. That's great. I don't know how it's in other countries, but it's great here.

**Chris Gammell:** Okay. Yeah. That's wonderful. Like a lot of internships and stuff as well? Yeah. Yeah. Okay. Yeah. It depends. I think in the States, at least, it's a little bit more regional. I definitely chose a school based on the ability to go do internships, or we called them co-ops for, like, longer periods. But I love that stuff. I mean, that's what I... I'm all about the experiential learning stuff. So, yeah. I forgot about this. So, there was this amazing National Geographic article about Holland and the agricultural stuff. Like, it's a really big... Tons of sensors around that, but there's this beautifully shot, like, National Geographic piece about it. Is there... Have you seen a lot of agricultural stuff as well?

**IoT:** Yes. Actually, we do. We do. We have some projects that have to do with soil measurements. So, you can imagine, like, measuring minerals and measuring soil moisture. Yeah. That kind of stuff. Okay. Yeah.

**Chris Gammell:** Yeah. It's just... It's interesting to me that, like... Like you said, solar is a big piece there. I wouldn't have expected that. I mean, like, you don't... It doesn't seem like a particularly sunny country. Is that... Am I wrong in that, or...?

**IoT:** No. It's far from sunny country. But maybe that's the driver. You need to be extra efficient to have some kind of...

**Chris Gammell:** Yeah. That's a good point. That's a good point. Yeah. And then I... Well, I knew about... I mean, some of the agricultural stuff. Like, that was the big tulip thing, right? Isn't that one of the famous pieces of the Netherlands?

**IoT:** Yeah. I believe so. I don't really get a lot of sense for that myself. Because I don't really live in those regions. But... Okay. Yeah. We're really famous for our tulips. And you could also use technology to get even more beautiful tulips, of course. Right.

**Chris Gammell:** That's great. So, what about you? So, what is your school background? And then how did you kind of get it started into the industry? Because you're relatively young, right?

**IoT:** Yeah. Yeah. I'm 35. So, I just got out of school in relative terms. Well, I... I really liked electronics from a young age. When I was just three years old, I was sitting under the desk and besides a computer and looking at circuit boards. Nice. And always have, like, a feeling that I have to do something with that and have to explore that further. So, I went through a stage of IT and ICT and software development early... ... ... ... ...

**IoT:** ...

**IoT:** ...

**Chris Gammell:** So, say we all. Yep. Yeah. I think most people listening here would be like, yeah, okay, yeah, of course you went back, yeah.

**IoT:** Because, yeah, well, software is fun, but if it doesn't work and it's someone else's fault because he wrote something wrong, then there's... You can get pretty angry. But if you have hardware, then it's almost always either your fault or Mother Nature's fault. I like that, yeah. Yeah, and it's pretty hard to blame Mother Nature, so...

**Chris Gammell:** I curse it every day, though. Come on. I mean, I live in a snowy region, so that helps, too. Yeah, yeah. Okay. That's great. That's great. And as you were explaining some of your background there, I feel like we should... You know, we're about five minutes in. We should talk about what we're going to be talking about here today and then we'll get back to all this stuff. So, I had been talking about some LoRa projects and you had written to me and you said, hey, I could talk to you about this and I'm like, that's great. I'd love to talk about it. So, that's why, you know, that was the background between IoT and all this other stuff. So, maybe work us up towards... So, you get out of school or maybe even working on projects like this in school, you said there's a lot of IoT-focused stuff. How did you get to where you are today?

**IoT:** Well, my study also focused a lot on media. So, that's like the classic TV, radio, that kind of stuff. So, the first electronics things I did were mostly LEDs.

**Chris Gammell:** Okay.

**IoT:** But they were also always connected to some kind of studio managing system. So, that meant some kind of network. And in the beginning, that was Ethernet. And then when wireless chips became more available to hobbyists, that was also wireless via Wi-Fi. Some kind of... You have those transceiver chips that I would do some FSK, like serial in, serial out kind of stuff.

**Chris Gammell:** Right. Like wire replacement, basically, kind of stuff.

**IoT:** Yeah, yeah, exactly.

**Chris Gammell:** Okay.

**IoT:** But only when I started to work for my previous company, which is a big ICT consulting company, there someone mentioned Laura. And he mentioned some amazing specs, like 10 kilometers of range on a couple of batteries. And then I just said, that's not possible. I...

**Chris Gammell:** Yes. It does... Every time I see the specs, I'm like, okay, well, let's get into this. You know, like, it doesn't seem realistic. So, I'm right there with you.

**IoT:** Yeah. So, exploring that further and doing some projects and getting in on the early development on the networks here in the Netherlands, I started using actually my hobby, which is flying RC planes, to explore Laura. Okay. And I put a Laura radio on the plane.

**Chris Gammell:** Like you were distributing, like, the Laura signal for other... Like you were a hub on the plane or...

**IoT:** No, no, no. Just a client. Okay. And I used a network from a provider in the Netherlands to connect. Uh-huh. But when I got up and I circled around a bit and go down and looked at the laptop for the data, I saw that I hit multiple gateways, you call them. Uh-huh. One, it was in Antwerp in Belgium. Whoa. And one, yeah, one is in Utrecht in the middle of the Netherlands. So, that's quite some range. And from that moment on, then it was sold on...

**Chris Gammell:** Oh, wow. Is that because of the added height so you got over the horizon line? Is that... Yes, exactly. ...that you would have otherwise? Yes. So, what were those relative distances then with Utrecht and... What was it in Brussels, you said? I don't...

**IoT:** No, Antwerp.

**Chris Gammell:** Antwerp, okay.

**IoT:** Uh, from where I was standing to Antwerp was 75 kilometers. And to Utrecht was, I believe, 35 or something.

**Chris Gammell:** Okay. Okay. So, that's kind of crazy. And what were you... So, like, you were just kind of piping back data at that point? Like, just...

**IoT:** Yeah, yeah. Just altitude data and temperature data, I believe. Okay.

**Chris Gammell:** Yeah, that makes sense. Wow. All right. Well, that's a data point there. And you mentioned... Well, let's get a little bit further. So, you started with this in your hobby, but then you also kind of took it back into the professional side of things. So, how does that translate it then?

**IoT:** Yeah, I took the equipment from the company I worked with home to play with it over the weekend. Then I discovered this. Mm-hmm. And when I brought the results back, everybody, of course, was really impressed. And some didn't believe it and spent days looking for the error I made.

**Chris Gammell:** That's nice. I mean, I guess it's engineering, right? That's... Yeah, yeah. Right.

**IoT:** So, also, we told some people at Company, which is just a classic software company. Mm-hmm. And we started to work on some LoRa project over there because there are some clients that would see potential in these kinds of things.

**Chris Gammell:** Mm-hmm. Yeah.

**IoT:** So, I worked on a LoRa project used to pipe data back from a cyclist, the race cyclist.

**Chris Gammell:** Oh, yeah.

**IoT:** Okay. In Belgium and France to the team leader, CAR.

**Chris Gammell:** Okay. That's a good one. I mean, that's like on the move. It needs to be battery, obviously, not tethered. No wires going to that. That'd be a lot of wire. Yeah.

**IoT:** And also a very noisy environment. Sure. That's why we initially thought LoRa was a good choice. Okay. But it's really not. But I can explain that.

**Chris Gammell:** Okay. Okay. And then, so, what other kind of... So, that's obviously like a fast-paced kind of environment. What about... Are you also doing stationary type stuff? I'm guessing a lot of sensors here, right? Sensors, battery, micro, and then a LoRa module. Is that kind of the thought?

**IoT:** Yeah, yeah, yeah. LoRa is actually a really bad choice for the cycling thing because it was a lot of data. And it needed to arrive relatively real time. Got it. Yeah. Which is absolutely not the power of LoRa.

**Chris Gammell:** Right. Okay. Okay. The power of LoRa. Yeah. As you said, what is the sweet spot then? Because, you know, this is kind of... As people look at all these different options, you know, like I'm in the cellular space and there's LoRa. That's why I got interested in it as well. There's Wi-Fi. There's Bluetooth. There's all these different things. What about LoRa and similar type of things are worthwhile checking it out for?

**IoT:** Yeah. There are a couple of LP1 technologies, which is a group of technologies where LoRa is in. Mm-hmm. Most of them are ultra-neuroband based, but LoRa isn't. Okay. And it's actually a wideband signal.

**Chris Gammell:** Yep. Yep.

**IoT:** The data rate, the amount of data you can send is really low. The range is really high. And also, the battery life is really good because it doesn't really take a lot of energy.

**Chris Gammell:** Yep. Yep. Yeah. It's a short burst and then it turns off and... Well, like you said, if it's not transmitting a lot as well, that helps, right?

**IoT:** Yeah. Yeah.

**Chris Gammell:** Okay. Okay. Okay. So, someone who's, like I said, got a sensor, got a battery, got a micro, and then has a sleep mode, they might want to take a look at LoRa as well. So, what about... So, LoRa, like I said, I was doing a little bit of research beforehand, but LoRa is actually a proprietary thing, right?

**IoT:** Yes. Yes. LoRa is nothing more than an IP block that describes modulation. Okay. And then you're talking about LoRa Phi. You can also differentiate between LoRa Phi and LoRa 1. Okay.

**Chris Gammell:** LoRa 1 is... I say WAN because I'm from Amherst, New York, you know, but... Yeah. Yeah. WAN, yeah.

**IoT:** LoRa WAN or LoRa 1 describes a network architecture.

**Chris Gammell:** Okay. Okay. And so, that would be like more... So, kind of like a higher level and actually talking to multiple devices, is that kind of the idea?

**IoT:** Yeah, yeah. It's almost a carrier-grade network. So, you can set your own network up with a few gateways and have thousands of devices connected to the same network. Hmm. Okay. And uploading data.

**Chris Gammell:** Okay. So, what about at your company and your own work as well? Have you explored some of the other, like... So, it seems like there's a kind of a wide swath of different technologies in here, but I'm not really sure which are just brand names and which were otherwise, right? Because there's like... It's like Sigfox is one that I've heard a lot as well. Yeah. And that seems like a similar technology, but it's definitely proprietary and branded, right? That's like a... They provide that wide area network.

**IoT:** Sigfox is... Actually, Sigfox, the protocol is open source. Okay. But you can only use it with their own worldwide network. Okay. Okay. So, you're logged into the provider, but you have a lot more choice of implementation on the node side.

**Chris Gammell:** Okay. Okay. So, there's multiple manufacturers of the nodes, you mean? Is that the idea? Yeah. Yeah.

**IoT:** You can just use general TI CC1100 series, for example.

**Chris Gammell:** Okay. And then you have to actually buy a license or something to use it for that?

**IoT:** No. You can implement your own stack on it, or you can get the stack from Sigfox. And then I believe you have to go through certification from them before you can use their network. Uh-huh. Okay. And then you have a cost per device per year.

**Chris Gammell:** Okay. Oh, okay. So, then it's just... Yeah. That's the idea is if you're going back through their gateways, that's kind of provided. Yeah. Yeah. That makes sense. Okay. So, comparatively there, if you're going to set up your own LoRaWAN, then you would be able to not pay the gateway price, right? Because you'd be setting up your own gateway, but you'd also have to manage that whole stack as well, right? So, it's some kind of network area, right?

**IoT:** Exactly. Yes. Okay.

**Chris Gammell:** Interesting. What about then, have you looked at like the 802.15.4? Is that another one that's on your map?

**IoT:** No, we don't really do a lot with that. Okay. We do, however, a lot with a narrow band IoT, which is a standard by the 3GPP.

**Chris Gammell:** That's right. Yep. Okay. And that's one I've heard a lot more about because that actually was just announced at CES, which I just got back from. T-Mobile is the only provider doing it in the States, and they just announced that they just rolled it out statewide, whereas it's very, I think, very popular in Europe. Yeah. Yeah. Yeah. So, there's a lot of carriers over there doing that.

**IoT:** So, we already have multiple carriers covering the whole country, so. Okay.

**Chris Gammell:** Okay. Yeah. And that one's like lower bandwidth. It's only one direction, right? You can only transmit?

**IoT:** No, you can't. It's two directions.

**Chris Gammell:** Oh. Okay. Maybe I've got that back. Maybe I'm thinking of a different one then. I thought it was only one way. Okay.

**IoT:** Cephox has a very limited downlink from the network to the device.

**Chris Gammell:** Got it. Okay. Yeah. Okay.

**Chris Gammell:** And, okay. So, and then, but like you said, lots of carriers over in Europe doing that kind of thing. So, that's interesting as well. And I think that, yeah, that's got coverage, but maybe not as much distance coverage, right? You don't get as much. You only need to go to the tower instead of going to, you know, across, over the horizon kind of thing.

**IoT:** Yeah. Narrowband IoT has a lot of penetration, which is really interesting. We actually tested it 50 centimeters underground. Oh, really? Oh, wow. Okay. Almost two foot. Uh-huh. And it still works with the cellular tower about a kilometer away in our case, which I think is really impressive. Yeah. And it opens up a lot of new cases that weren't possible before. Sure.

**Chris Gammell:** That is interesting. I hadn't really thought about that whole getting through stuff thing. But, again, when I was at CES, I saw a booth that was interesting. What was the one? There was another one I saw where it was, they were specifically made to go through walls and stuff like that. It was a 900 megahertz type thing, but it was like the algorithm was there to ensure that you actually got through the walls.

**IoT:** Yeah.

**Chris Gammell:** Oh, SureFi, it's called. S-U-R-E dash Fi.

**IoT:** I never heard of it, but I guess it's an ultra-narrowband technology. So, you put a lot of energy in a really tiny bit of spectrum.

**Chris Gammell:** Yep.

**IoT:** Yep. And then you can get further through things.

**Chris Gammell:** Yep. Okay. Yeah. So, I asked about the 802.1504 because that's actually, if people remember Akiba being on the show in the past, that's actually what Akiba uses for the rice farming stuff as well. So, it's similar like distance-wise and battery-wise, but it's an open standard, I think.

**IoT:** Yeah. I think so too, but it also just defines point-to-point things or maybe mesh.

**Chris Gammell:** Yes. I believe so. Right.

**IoT:** Which is not as interesting for a lot of customers, we notice.

**Chris Gammell:** Okay. Yeah. And that is a good point too. So, maybe we can walk through the different layers as well because some of this is talking about the hardware, right? So, like, you know, what frequency is the radio transmitting at? Some of it then is like a firmware layer and then there's different levels of abstraction up the stack, right? That's kind of the idea. As far as I understand it, maybe you can help me out there. Yeah. So, like, yeah, it's like Laura's using different frequencies, right?

**IoT:** You can apply Laura on a lot of frequencies, yes. Okay. Okay. It's usually used on the ISM bands. Okay. Down from 160 megahertz in the US, I guess, to 315, 433 megahertz, 868 megahertz, and 915 megahertz.

**Chris Gammell:** Yep.

**IoT:** And it depends on where you are, which bands you are allowed to use, and with what rules you are allowed to use them.

**Chris Gammell:** Okay. Like, you mean operating as a user, you mean, or like how much power or what?

**IoT:** Both. Okay. For the 868 bands, for example, in the EU, we have a rule that you can only send 1% of the time.

**Chris Gammell:** Oh, interesting. Okay.

**IoT:** Which is 36 seconds an hour. Yeah. If you send more than that, you're actually illegal.

**Chris Gammell:** Really? Okay. And is that... Sorry, I don't actually know. Is there a governing board? Is it also called the FCC there, or is it called something else?

**IoT:** It's called something else. I believe the Dutch thing is called Agentschap Telekom. Okay. I already met them. They're really great guys. Okay.

**Chris Gammell:** I was going to say, was it a good meeting or a bad meeting?

**IoT:** It was a bad meeting at home, so... Just some out-of-hands Wi-Fi networks.

**Chris Gammell:** Got it. You didn't get arrested, though. Sorry. No, no, no.

**IoT:** Just a warning. Mm-hmm.

**Chris Gammell:** All right. That's great. That's a good thing. Okay. So only 1% of the time, though. So that's of all devices that operate in the 868 band? Yes. Yes. Interesting.

**IoT:** There are some certain subbands, but it's a really tiny sliver of spectrum. You can have 10%, but yeah, that's just one band, so that's also not very much.

**Chris Gammell:** Okay. Yeah. That's crazy. But I mean, well, again, at these... I mean, the data rates we're talking about, like, you're not piping video that we should make that clear for people listening. Yeah. It's not like you're, you know, doing audio video or anything like that. It's like the temperature is 4, right? Yes. Yes. So, yeah, I mean, MQTT type data and getting that out there, right?

**IoT:** Yeah. When you're sending, the data rate will be, like, between 0.3 kilobytes per second to about 11 kilobytes per second.

**Chris Gammell:** Okay.

**IoT:** But that's only a part of the time, so it's really not a lot of data. Yeah.

**Chris Gammell:** And do you, I mean, so have you found that you run into that and you say, oh, that's, I mean, I can't work with this? I mean, what, or maybe that cycling example is a good one. So, like, what were you trying to, what were you trying to send versus, you know, where did you start running into limits? Yeah.

**IoT:** We were just trying to constantly update the car with actual data of pedaling power. But we just didn't, we didn't really know about the 1% rule yet because. Right.

**Chris Gammell:** Right. That's what you learn. Yeah. In situ, right?

**IoT:** Yeah. Yeah. Of course. And so that's, we actually ignored the rule. In the early days, there were some modules that were not restricted. The modules you buy now are, have a built-in library that restricts you from sending after you go over the limit.

**Chris Gammell:** Mm-hmm. Okay. And, and so you were just trying, so you were, okay, so maybe that helps with the stack discussion too. So in that case, were you implementing your own LoRa stack? Is that the right phrase?

**IoT:** Yes. Yeah. Well, I, I, I of course got it from the, the GitHub from IBM. Okay. And then you can implement it on an ARM chip. Oh, really?

**Chris Gammell:** Like that level of, like what, what kind of, what kind of processing was necessary? Was like an M3, M4, something bigger?

**IoT:** I believe it was an M0 actually.

**Chris Gammell:** Oh, okay. All right. So low power, low, low processing.

**IoT:** Yeah. That's good. The thing is you, you do need a chip from Semtech, which is the owner of the LoRa IP. Okay. And that's an, an SBI controlled chip that does the radio part and yeah, the, the low level communication. And then you need to do, to run some library to get the date out.

**Chris Gammell:** So that's from Semtech. What, is there like a family name there of what, what it's called?

**IoT:** Um, the, the, you have a different families of chips you can use for LoRa. Uh-huh. There are specific gateway chips and there are no chips. Uh-huh. Uh, the no chips start with SX1270X.

**Chris Gammell:** Okay. And that's no chips. Okay.

**IoT:** Yeah. And, um, the, the gateway has some specific chips where they divide the, the front end of the, the radio and the baseband processor into different chips.

**Chris Gammell:** Uh-huh. Okay.

**IoT:** Uh, but gateways have a lot more sensitivity and they can do eight bands at the same time or eight channels.

**Chris Gammell:** Okay.

**IoT:** So they can send a lot more and, uh, always listen on, uh, and on one channel for join requests, for example.

**Chris Gammell:** Okay. Yeah. Now that's, okay. Yeah. Definitely going to get into that. Um, so, okay. So the idea is that Semtech owns this. So they created this. I see a little R in this. So all rights reserved on LoRa. So that's interesting. So, so when people say LoRa though, that means it's going through a Semtech chip.

**IoT:** Yes. Okay. There's, there's one other way I currently know, and that is GR LoRa. Okay. And that's someone, uh, reverse engineered LoRa protocol and made a GNU, GNU, uh, radio. Oh, interesting. Okay. To, uh, encode and decode LoRa packages. Uh-huh.

**Chris Gammell:** Oh, interesting. Yeah. I was, that's, so this, the, the concurrence of me getting some LoRa modules is also concurrent with me getting a HackRF because I was hoping to kind of see what I was doing and maybe decode stuff live. It really just troubleshoot my crap that I'm, that doesn't work. You know, that's, that's, uh, so what do you, what are you usually doing when you're troubleshooting? Are you using just spectrum analyzers and similar or how are you dealing with it?

**IoT:** I am actually also using a HackRF. Oh, really? Okay. Yeah. Um. It's, uh, it's ideal, but I usually not, don't go further than the, the, the waterfall, uh, diagram. Okay. Okay. Uh, and just see if there are, is a message sent on a particular channel. Got it. Okay. Um.

**Chris Gammell:** So it's pretty much using it like a spectrum analyzer, but with waterfall, like you're saying.

**IoT:** Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. That is super useful. And so, and you had actually sent me a picture of this. So what the, what the actually looks like as you're moving through it and we'll post it, but maybe you could try and give us a word picture here as well.

**IoT:** Yeah. Well, uh, the, the modulation of LoRa, uh, uses a chirp modulation, uh, chirp spreads, spread spectrum. And, uh, that's a way to, uh, reduce, uh, influence from a multi-path and that kind of stuff, uh, which makes it on the waterfall look like zigzags across the screen screen.

**Chris Gammell:** Right. Uh, yeah. And that's because, so the chirp, and maybe you could explain the chirp spreads, spreads spectrum as well. I can never say that. Right.

**IoT:** Yeah. So information is encoded in chirps, uh, which is just, um, moving, moving up and down in frequency and the spectrum in time. And, um, the, every, every, the direction of the chirp, uh, simply says, uh, it's a one or zero. It's, it's a little bit more complicated, but.

**Chris Gammell:** Okay. No, that's interesting that I actually didn't realize it was the directionality thing. So, so that's the idea is that basically if it's going up or going down, for example, up is a one down to zero, that that's the idea.

**IoT:** Yeah. Yeah. Yeah. For example, it's, it's, it's a, it's a little bit hard to, to explain through speech, but.

**Chris Gammell:** Right. Well, we'll, we'll definitely, like I said, we'll, we'll share pictures for sure. Um, but, uh, yeah, people, you know, people have seen chirps on, uh, you know, like that's effectively actually what a spectrum analyzer is usually doing, right? It is sweeping through different frequencies and then, uh, that allows you to see different things as, as you go through the frequencies, right? So, or network analyzers do that as well. People think about, uh, you know, inject a 10 Hertz to one megahertz signal. You'll see how a circuit responds over time. That's kind of the idea. Um, so you mentioned it reduces multipath though. So could you maybe explain that a little bit?

**Speaker ?:** Yeah. Yeah.

**IoT:** In, in a lot of, um, situation where you use a low power wide area networks are urban areas, uh, for example, uh, detecting if a parking space is empty or not. Uh, so there are a lot of. Echoes essentially. In, uh, in the signal it's been transmitted. It's echoing of buildings and it all arrives at the receiver, uh, at different times and at different amplitudes. And the, the spread spectrum, uh, chirp modulation helps to, uh, get the, the right signal out. So it's, it's, it's, uh, makes the signal to noise, noise ratio better.

**Chris Gammell:** Okay. And so would the idea here be that, uh, so you have, you have the main signal being sent, you have one reflecting off a building, you have one that reflects off a building two blocks down the road is the idea that basically because of this, you can just see, you'll see the strongest signal, uh, as it shifts through time or, or what is it about the shifting that helps?

**IoT:** I don't know really in, in fine detail, but I believe it's easier to track the signal because you know, uh, it, it should be, uh, it's, it's, it's at some place in some time and then you can predict a bit over where it will be, uh, a little time later.

**Chris Gammell:** Okay. Okay. Okay. Yeah. That's good. Okay. Um, so, and then it is spread spectrum as well. And so is that just because it hops between different bands with, or sorry, with, within different channels within the band? Is that that idea?

**IoT:** No, the, the spread spectrum part is just, uh, the chirp. So, uh, it starts at a certain frequency and ends at another frequency.

**Chris Gammell:** Okay. So, so didn't you mention channels though, or something like that within the 868?

**IoT:** Yeah, that's true. Uh, the 868, uh, part of the spectrum that you can use license-free, uh, has room for a few channels. Okay. Uh, because LoRa uses channels that are, have a certain bandwidth. Uh, you can actually set the bandwidth, but the most common one is, uh, 125 kilowatts. Okay. So you divide the, the 868 band in 125 kilowatts channels. Uh-huh. And on each channel, you can use the 1%, uh, rule.

**Chris Gammell:** Oh, okay. And how many total channels fit in the 868 then? Is it?

**IoT:** Um, I believe it's eight. Okay.

**Chris Gammell:** Don't quote me on that. No, no, no, that's fine. Yeah. We'll, we'll put that on people to actually do that. I guess that makes sense. That'd be like one megahertz total, right? Yeah. So, okay. That's great. So, okay. So that does open up though, you know, reducing interference and all that other stuff. Cause I imagine if you have two sensors right next to each other and they were on the same channel, you'd be kind of just guessing, you'd hoping that they don't transmit at the same 1% interval, right? That's, that would be problematic. And then you would start to lose data because of interference and stuff, right?

**IoT:** Yes, that's true.

**Chris Gammell:** Okay. So what about that then? So like, say you have, say, you know, you have a thousand modules out in the field, right? Or within, within, uh, um, an area for, uh, the gateway or whatever, what did you call it? You called it the, there's the node and the gateway, or is there something else?

**IoT:** Um, well, a thousand nodes, uh, in, in the, in reach of one gateway is, uh, it's honestly is a bit much. Okay. Okay. That's good to know. Yeah. Yeah. Yeah. Uh, but, uh, yeah, you want to use, uh, you want to design your application in a way that they, uh, don't inherently send at the same time. Okay. Because, uh, that will, uh, well, you will get in trouble basically. Okay. Uh, because there are eight channels, there are eight devices that can send. At the same time, uh, nodes can check, uh, if there is free airspace available and then only send if, uh, there is some free space.

**Chris Gammell:** Okay. And what's the usual like transmit time then all, all told, like, so you said like 36 seconds, but would a device actually, it wouldn't actually use all 36 seconds, right?

**IoT:** No, not, not in one message. Um, messages can take quite long. I have seen messages that are almost a second when you fill the, the, the packets, uh, full of data and use, uh, the lowest spreading factor, which is also something we can talk about. Okay. Uh, but there are also messages that are like a millisecond or so in our time.

**Chris Gammell:** Okay. All right. That's good. Yeah. So what about then? Uh, okay. So now, like, like I said, like the thousand or you said the thousands probably unrealistic, but I imagine over time as this gets more popular, you're, there will be more, um, that are not necessarily like, so if I set up, you know, 10 sensors in a part of a city, that's fine. But then there could very well be other sensors in the city that are also crowding it out. So, so what happens in that case? Is it, is there brokering or how does that all work?

**IoT:** Well, uh, that's actually, uh, some people say that it's a big problem. Um, it will be a problem sometime in the future. Okay. Uh, there will be, uh, coexistence problems. If everybody would use Laura, we would, uh, you, we would get there pretty quickly because Laura has a wide band. Okay. Uh, so there is a little bit less, uh, space for other people to send stuff.

**Chris Gammell:** Interesting. Yeah.

**IoT:** Um, so I, I hope there will be a lot more spectrum opened up to this, these kinds of, uh, technologies.

**Chris Gammell:** So Richard says, don't, don't step on his Laura. Even though he's on here. Yeah. Don't, you know, if you're, if you're in Rotterdam, stay away.

**IoT:** Well, we actually never had any problems with that yet. Okay. With overcrowded, uh, Laura stuff. I have been at, uh, some kind, uh, some, some meetings and trainings where the air was really busy, uh, uh, but it's still all kind of works. Um, I don't, I don't know this for sure, but I, I believe, uh, even if, if, uh, signals partly overlap that receivers can, uh, pick that out.

**Chris Gammell:** Yeah. Yeah. Right. And so, yeah. And maybe, maybe this is a good thing to ask about too. So you said, I mean, like this can handle lots of stuff, but also far away. So then what about, so, okay. So maybe going back to your RC plane example, right? So you now have a device that's transmitting temperature from, you know, uh, what a kilometer up. I don't know how RC planes fly, uh, you know, you know, I shouldn't say it's more than 120

**IoT:** meters. Okay. So a hundred meters up.

**Chris Gammell:** Yeah. I guess, yeah, I guess above that, the RC plane probably would start to drift. Uh, okay. So a hundred meters up, but it's a hundred meters up. Still pretty good distance. Um, okay. Secretly in my head, I was trying to do the conversion, you know, stupid American, uh, you know, imperial units. Uh, um, so a hundred meters up and it's transmitting, but now there's someone getting a packet. There's someone in, uh, where'd you say it was, uh, Antwerp, right? So someone in Antwerp, you, you saw a tower in Antwerp. Yes. But someone was also transmitting in Antwerp at that time, right? Yes. So what happens then? So if, if, if in the instance that it was absolutely like dead on the exact same frequencies, the exact same channels, the exact same time, um, would a receiver be able to pick it up in Antwerp or you would just never have seen it?

**IoT:** I think what would happen is that, uh, the receiver in Antwerp would pick up the guy that is in Antwerp.

**Chris Gammell:** Okay.

**IoT:** Uh, and leave, uh, leave my message. Uh, yeah. As, as nothing. Okay. All right.

**Chris Gammell:** So it just would have gotten flooded out by the, by the, the, the higher power signal close by. Yes. Okay. Okay. So it's safe to assume that the one that hit the tower in Antwerp was, uh, it was, it was open at that time, right? It was, it obviously talked to that tower. Yeah.

**IoT:** Yeah. It's where it's really early days. So the, the spectrum was really not used a lot. Okay. Okay.

**Chris Gammell:** Uh, it's interesting though. So, uh, so again, going back to that example of there's a guy in Antwerp that, you know, flooded, flooded your signal out in that case. Would it, would it just, your signal would look like background noise to that signal? Is that kind of the idea? And then, and then the, the gateway is just drawing that, that higher power signal out of the noise that you're contributing.

**IoT:** Yes. Um, it, it could also very well be if, if the signal was still good enough that it would pick up both signals.

**Chris Gammell:** Okay.

**IoT:** Um, if, if it, if there's enough interference, then it, it won't, uh, it won't do anything. Uh, but, uh, if the, the most, the strongest signal of course, uh, is very much easier to, uh, to decode than, than, uh, the, the weaker signal.

**Chris Gammell:** Right. But in that, in that case, then you said, if it could pick up both, is there capabilities within the same channel, within the same frequency to actually draw out both? I guess that's the piece that I don't understand.

**IoT:** Um, I believe not. I believe that's, that's, uh, if, if you're in the same channel at the same time, then yeah, well, it's like two people speaking through each other. Yeah. You cannot extract, uh, a lot from that.

**Chris Gammell:** Okay. Okay. And so I guess that, uh, so then is this technically, this is all half duplex, full duplex. I don't really, so full duplex would be two different channels, right? Like one SIM receive?

**IoT:** Uh, full duplex would be like sending and receiving at the same time.

**Chris Gammell:** Oh, okay.

**IoT:** Uh, this is half duplex. Okay. In the case of only using Laura5, you can, uh, you can, you can design your own application and, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, pick the time you want to send or, or, or, or listen. Mm-hmm. In Laura1, there's actually, uh, three different schemes for that.

**Chris Gammell:** Okay.

**IoT:** Um, you have the class A, Laura1, uh, which is, uh, you send an uplink with your device and then you should listen for two downlink slots.

**Chris Gammell:** Okay.

**IoT:** One is immediately after your uplink and one is a little bit later.

**Chris Gammell:** Okay. And that helps to take care of distances or how does that work?

**IoT:** That is for the situation where you mainly want to put data up to the cloud and when we already are awake, we also can do some downlink while we're at it.

**Chris Gammell:** Okay. Okay.

**IoT:** Class B is more for devices that can also be controlled from the network, say like a street lighting. Okay. And they have scheduled receive windows.

**Chris Gammell:** Okay.

**IoT:** And Class C is even better for street lighting because you are always listening except for when you're transmitting.

**Chris Gammell:** Oh. Is that higher power then?

**IoT:** Yes, yes. But it's a street lamp so it has like a line power.

**Chris Gammell:** Oh, okay, okay. Yeah. Interesting. And when you say, so always listening except for transmitting, so that is the same frequency and channel though?

**IoT:** Not necessarily.

**Chris Gammell:** Okay.

**IoT:** I don't actually know. I could imagine that when you send to the tower on one channel, you will get an answer on the same channel because the nodes can only listen to one channel at the same time. Okay.

**Chris Gammell:** All right. Yep, yep, yep. But so I guess the thing that helps with that is that the traffic that's going out is addressed to a certain MAC address. Is that kind of, is that what helps to allow people to understand which message is intended for which device?

**IoT:** LauraFi doesn't actually specify anything about that. With Laura1, you need to actually attach to a network.

**Chris Gammell:** Oh, okay. So it'd be like, you do like a handshake, like, hi, my name's Chris. I'm talking to your network. And then when the packet's getting sent back, it's being sent for Chris. Is that the idea?

**IoT:** Yeah, yeah, exactly. It's, Laura is AES encrypted. So only the network that the message is meant for can decode it.

**Chris Gammell:** Okay. That was on my list too. That's good to know. Yeah.

**IoT:** There are two different ways to attach to a network. One way is to do over-the-air activation. When you have a device, you put a secret application key in it. And the application key determines that the device connects, belongs to a certain group of devices and connects to a certain application in the backend.

**Chris Gammell:** Okay. So that's like a unique ID of some type. Yeah. Yes. Okay.

**IoT:** And it's, the key is shared between the device and the backend. Okay. And then the device does a join request. And it sends a message to the gateway. Gateway sends it to the network server. And then your own application has to allow the device to, to the network by generating keys.

**Chris Gammell:** Okay.

**IoT:** And then you'll get some session keys and you're set up to go. Okay. Uh, the other way is to, uh, directly put in the network session keys, uh, but that's not a recommended way, but it's really easy to test with because, uh, you don't have any handshaking. And, uh, so it'd be like,

**Chris Gammell:** so I have a, I have a little plastic widget. I upload the session key into that. Yeah. And then, like, like into memory or something. And then, and then it just knows how it's like the, it's the key to the lock. Is that the idea? Yeah.

**IoT:** Yes, it is true. Uh, there, there are two different keys. One is to do, to encode the network messages. And one key is to encode your payload data.

**Chris Gammell:** And they're, why are they different?

**IoT:** Uh, I believe to, uh, to, for example, when you have a provider that provides your network, you may not want to have them read your message. Oh,

**Chris Gammell:** yeah, that makes sense.

**IoT:** They only have the network key and you only have the application key.

**Chris Gammell:** Okay, cool. Yeah, that's good. That's good to know. And so you said over the air is kind of the, it's the normal way to do it.

**IoT:** Yeah, that's the normal way to do it. That's only scalable way, uh, because, uh, that way you can keep your firmware package, uh, the, uh, the same for multiple devices, uh, because you need a different session key for every device.

**Chris Gammell:** Yeah. Oh yeah, I guess so. Yeah. Oh, I guess, yeah, if you're, if the network is also defining it, I was going to say you could, well, you could like, you could append like a unique ID on the device, like the Mac of the chip or like unique ID built into the microcontroller, but you can't do that because the session key is generated from the network.

**IoT:** Yeah. And also the session, you want to replace the session keys every session, of course.

**Chris Gammell:** Oh, really? Okay. So,

**IoT:** because otherwise you can slowly decode the key, uh, via all kinds of security things. I don't really know much about, right.

**Chris Gammell:** Okay. That makes sense. Yep. Huh. All right. Well, that's good. So, so like, so session key direct, direct session key stuff is kind of no use to troubleshooting and early programming, but then otherwise it does it all on its own.

**IoT:** Yes. Well, the one other reason to use the direct session keys, which is called ABP, uh, authentication by personalization, I believe.

**Chris Gammell:** Okay.

**IoT:** Uh, is when you are not sure the gateway can send a message back to you.

**Chris Gammell:** Oh, uh, because of distance or what?

**IoT:** Yeah. Well, the, the systems are, are not symmetric. Uh, so you have a transmitting device that is, is largely different from the receiving device and gateways are a lot more sensitive in receiving than devices.

**Chris Gammell:** Hmm.

**IoT:** So when you're in the edge of the network, you don't have really good coverage. Uh, you can descend a defy, uh, a message to, uh, the gateway because it has a high sensitivity, but if the gateway sends something back to you, then you cannot hear it because you're not sensitive enough.

**Chris Gammell:** Huh? Okay. So what does, what does that all look like? So as, as you're moving towards, you know, getting a device on a network, what does that, what does that look like? And is it just like you talk to the, to the gateway and then it says nothing, nothing back to you?

**IoT:** The gateway is actually a very passive device. There are two more components that are behind the gateway.

**Chris Gammell:** Okay.

**IoT:** Uh, you have a network server and an application server.

**Chris Gammell:** Okay.

**IoT:** And the network server, uh, shuffles, uh, stuff around. And application server is the other end of your connection, essentially, uh, where you manage your devices and where the data comes out.

**Chris Gammell:** Okay. And that, that's how it actually hits the cloud or whatever, wherever your end point is.

**IoT:** Yes. Yes.

**Chris Gammell:** Okay.

**IoT:** And you, you can write your own application server and you can even write your own network server. Uh, it's all explained on the internet how to do that. All right. Go internet.

**Chris Gammell:** Uh, okay. So maybe, maybe let's take it back to, to you in terms of hardware person. How much of this stuff do you actually have to do? Like how much is taken care of on a, you know, when you're getting new devices online and everything?

**IoT:** Yeah. Well, you can order the, the, the, the,

**IoT:** the,

**IoT:** or you can choose a module from other companies like for example, microchip. Um, if you want to have a short time to market, you of course choose the module. Also, if you want to have some more, a little bit more easy development, you will choose a module. But if you really are scaling a lot and, and, and are implementing a lot of devices, then it's of course cheaper to do the chips directly.

**Chris Gammell:** Sure. Yep.

**IoT:** Uh, if you use a module, then everything is really simple. Uh, most modules use an 80 commands interface. Oh really? Uh, which is, uh, yeah, it's, it's really, it's really simple for all the steps you need to do, uh, connected to the network. It's like three or four commands you have to send in sequence and then you're connected to the network.

**Chris Gammell:** Okay. So I'm like halfway through, uh, an Adafruit tutorial using the RFM 95. Yes. Uh, and that actually has, uh, a library from the radio head library it's called. And that someone, I think someone else wrote, but basically it's, so I'm talking through layer and layer and layer, but I guess the thing I haven't, I haven't actually looked under the hood of that library, but I'm guessing that that's probably taking the stuff and doing all the AT commands and the handling of things, right?

**IoT:** Exactly. That's just an AT command handler.

**Chris Gammell:** Okay. Interesting. AT command, you know, that's, well, obviously that's a big thing in cellular. I'm kind of learning about that too. And, uh, those things are never going away, are they?

**IoT:** No, it's pretty old. I believe it's like eighties or something.

**Chris Gammell:** Yeah. I mean, that's what Nokia phone, and stuff used to, I think. So it's, I know it's like network standard interface, interface type stuff, but boy, it's, yeah, it's, it's sticking around.

**IoT:** Yeah. But it's, it's really working very well. As long as we're still using serial connections, then why wouldn't we use the protocols that are working on top of it?

**Chris Gammell:** Sure. Sure. And so are you,

**Speaker ?:** are you,

**Chris Gammell:** are you kind of use, like, do you have software people in house that are helping you write kind of, uh, user libraries that you can not have to touch the AT commands? Are you regularly just writing AT commands for these things?

**IoT:** We, we as a company actually made the hardware that, uh, is being sold by the things network. Oh, great. And they also have an, uh, uh, TTN uno, which is just an Arduino with a LoRa modem on it and an excellent, uh, library for Arduino. So I always use that because we have lots of them around the office. Sure. Right. Yeah. The best support I can get, I guess.

**Chris Gammell:** That's right. No, that's, that's the way to do it. That's smart. Okay, cool. And, so, and, uh, things network is one of the gateway. It's like community based gateways. Is that right? Or.

**IoT:** Yeah, the, the, it's really the, the, the network of the people. Okay. So, um, there are people that I'm read. Yeah. There are people that own a gateway and that's, uh, connected to the backend from the things network. Uh, uh, and that way they share their gateway in, in a, in a common network. Uh, so there are other people that have devices and they can register themselves on the network, on the things network. Uh, and then whenever they come close to someone that has a TTN gateway or a gateway that sends, uh, signal to the, the TTN backend, uh, uh, then, uh, you're connected.

**Chris Gammell:** That's great. So, uh, that, uh, I have to look back through my notes now. So the over the air activation then is taken care of, or wait, wait, so the network server and the application server is what you were talking about on those gateways, right? So does that mean that when you sign up for the things network that the network server is taken over by the things network? Is that right?

**IoT:** Yes, that's true. Okay, cool. So part of the application server, uh, if you want to. Okay.

**Chris Gammell:** So basically it's, uh, it's like borrowing someone else's firmware, but then you get more networking because of that.

**IoT:** Well, it's, it's, it's really hard to build your own network because you really need to own a lot of land or a lot of interesting places to put the gateways. Uh huh. So it's really great if you can share it. If, if you use, if you deploy a few gateways and share it with other people, then yeah, well you, that's the only way to get a truly really global network that you can use for free, I guess.

**Chris Gammell:** Yeah, no, that's great. Um, and so what, so it'd be like, if I, so I'm setting up a small gateway in my house or sorry, I have a bunch of sensors in my house. I have a gateway. I sign up on this thing and then it also offers it to my neighbors. Is that kind of the idea?

**IoT:** Yes. If you're a sensor, if your neighbors have sensors, then they can connect to the network via your gateway. But also if you take your sensors with you in your car and you're go to another city, uh, then you can use their network.

**Chris Gammell:** Okay. So then how do the sensors then set up with the network? How does that work?

**IoT:** Well, all the, the gateways are just pass through devices. So you are always connecting to the same thing essentially.

**Chris Gammell:** Okay. So, okay. I, I guess, uh, does that mean that any, so I don't actually have to be a member of the things network as a, as a node, right? So if I have a temperature sensor and I'm driving in my car from Chicago to Cleveland, and there's a couple networks along the way, basically it's like an open enough thing where I, it will just find the next tower and send it through that to my end point on like, uh, AWS, IOT cloud or something.

**IoT:** Yeah, exactly. That's, that's, uh, that's the case. You don't have to have a gateway to use the things network.

**Chris Gammell:** Interesting.

**IoT:** Uh, there's also a really fun activity, uh, with which you can help the network, uh, without having a gateway, which is, uh, war driving.

**Chris Gammell:** War driving. Okay. What is that?

**IoT:** Well, you just, uh, take, uh, a note that's, uh, sending out, uh, constantly sending out or as much as you're allowed to sending out, uh, a message. And when it gets received, um, you can, uh, track down which gateway it was, uh, because not all gateways are visible to the network and on, not all their locations are disclosed. So if you are driving past it, you know, it was there. It's just like the wifi war driving.

**Chris Gammell:** Okay. Uh, I didn't know that's the thing actually. So, so war driving is basically just discovering new networks. Yes. Yes. Interesting.

**IoT:** I did learn this on the street view cars.

**Chris Gammell:** I was going to say, I did learn that Google has a reverse API lookup so that if you see a new network and it has a unique ID, they can tell you pretty much. That's also how they figure out where you, like when you click on your phone, use my wifi to help locate me faster for like GPS location. And what it actually is doing is looking up which wifi networks it sees and says, Oh, you're probably here.

**IoT:** Yes. Yes.

**Chris Gammell:** That's creepy, but that's, but that's the effect of, that's the result of war driving you're saying and, and having lots of devices on a network.

**IoT:** Yeah. Yeah. And also the, the network is pretty fluid for the, for the things network because people just unplug their gateway. And, uh, so the, to keep the data up to date, uh, it's, war driving is the only really true reliable way to know.

**Chris Gammell:** Interesting. And so what would, so if, if someone wanted to participate in that, that's listening right now, what would they do? They'd buy a node, set up a node and just start connecting randomly with packets. The,

**IoT:** the most, the most, uh, uh, famous or the most used tracker is, uh, TTN mapper.org. Okay. Uh, it has some basic pages of how to set up your lower nodes to work with the, the mapper.

**Chris Gammell:** Okay.

**IoT:** Uh, you only need the device, uh, a TTN account and, uh, the code that is provided by TTN mapper.

**Speaker ?:** Okay.

**Chris Gammell:** And then, and then it just basically, Oh, so it's sending to some endpoint as well. I'm guessing their endpoint.

**IoT:** You can, you can send, uh, location data via Laura, or you can actually use an app, uh, that's, uh, you, you, you sense the, the, the phone's location to the backend.

**Chris Gammell:** Okay. Yeah.

**IoT:** And, uh, that way you don't have to have a GPS, uh, Laura, uh, enabled thing. Right.

**Chris Gammell:** Okay. So it's probably just sending GPS coordinates, strength of the signal, name of the signal and whatever else it sees. Right. Yes. Yes. Oh, interesting. Okay. So, uh, let's get back to the, the physical side of this stuff too. So you had talked about spreading factor, but how, how does it, I mean, so, okay, now, now I see there's a tower 10 kilometers away with, within the, you know, within the, um, line of sight effectively. Uh, but then I start moving away from it and the signal gets worse and worse. Does the module actually change itself or, or what actually needs to happen when, when you do start getting weaker and weaker signals?

**IoT:** Uh, it could actually change some parameters. Uh, that's called adaptive data rate.

**Chris Gammell:** Okay.

**IoT:** Um, but there, there are a few notes you can turn, uh, to get a more range.

**Chris Gammell:** Okay.

**IoT:** Uh, one of them is the spreading factor and a spreading factor essentially is the duration of the chirp.

**Speaker ?:** Okay.

**IoT:** So instead of going from low to high in a really short time, it goes low to high in a longer time. Um, that's where you can increase the energy per symbol, the sort of energy per bit.

**Chris Gammell:** Uh, uh,

**IoT:** and you can imagine if people talk slower, you can understand them better.

**Chris Gammell:** Yes. This is how I get around foreign countries. Yes. Yes. Just speak English really slow. Yeah. Increase your spreading factor. Right. And louder too. I also, I try and get louder. You, you understand me.

**IoT:** Sorry. Louder is sadly not allowed. Um, you, you are mostly sending at the maximum, uh, uh, transmission, uh, power. Okay. You can, you can lower it, but then you're really close probably.

**Chris Gammell:** Okay. And so, yeah, so that makes sense. It's a trade-off of battery power. So if you're already sending it max power per, per signal or per chirp, then spreading out the chirp just means you're adding more battery current going through us, you know, going through your chip, going through the, uh, the antenna, which creates invisible wavy things, which then, you know, wave for longer. Exactly. Okay. All right.

**IoT:** there's another thing. And that's a coding rates, uh, because your actual data is encoded with a pseudo random stream. Okay. Uh, which is some, some, uh, deal to, uh, increase, uh, the amount of signal you can get out of it from the end.

**Chris Gammell:** Yeah. Okay.

**IoT:** Uh, so you can, uh, add more, uh, pseudo random, uh, data to it, which makes the messages, uh, longer, but then it's easier to, uh, to get the data out. It's similar to the technique that QR codes use, uh, to get data out.

**Chris Gammell:** Yeah. I saw, I saw Mike Osmond giving a talk about this at DEF CON and it, it blew my mind a little bit that it's like, yeah, you just add a longer string. And I guess it's just, I guess the thing I don't understand about it is you don't need to know the string on the other side, right? Or you do need to,

**IoT:** um, I believe it's, it's a pseudo random string. So I, I guess, I don't know, actually. Yeah.

**Chris Gammell:** I'm trying to remember the presentation too. I remember, so Mike was talking about going from like, five, 12 bits to like 2048 or something like that. You know, it was like, it was a significant change in terms of the number of encoding bits, but I didn't understand. I, I, I honestly, at this point, I've just forgotten that was back in August. So, um, yeah, but it's, that's interesting. Okay. So it's basically Joe, it's just more encoding bits that allows you to draw more crap out of the, out of the draw more signal out of the crap of the, uh, you know, noisy environment that you're in.

**IoT:** Yeah. Yes.

**Chris Gammell:** Okay. And so the trade off here in both cases is pretty much just battery. Is that kind of the, the main thing?

**IoT:** Uh, the trade off is always, uh, between battery and range.

**Chris Gammell:** Okay.

**IoT:** And, uh, yes,

**Chris Gammell:** if you want it, you want a really low battery power situation, you probably want to just set up another, another, uh, gateway.

**IoT:** You can set up another gateway or move to another technology. If you're really close, then you're best off losing, using a BLE, which is sure. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**IoT:** Yeah.

**IoT:** Yeah. Yeah.

**Chris Gammell:** So, uh, maybe that's a good, a good segue into like, what is the applications that you've seen so far? What are the usual battery lives, like capacities and battery lives that you expect to see? Like, excuse me, I always, you know, the, the measure is always like, you know, I can do a year on a coin cell. It's like, okay, well, uh, but like, what does it take?

**IoT:** Yeah. A coin cell would be a little bit too little in, in, uh, in, in amperage wise in immediate power.

**Chris Gammell:** Sure. Oh, you mean just cause the internal resistance and stuff? Yes. Exactly. Got it. Yep.

**IoT:** Uh, but if you have like a few pen light cells, uh, then you have enough. Uh, we usually use, uh, lithium, uh, chloride cells, and then you can get, uh, really, really long lifetimes of 10 years.

**Chris Gammell:** really? Okay. Of what kind of capacities?

**IoT:** Um, there is some, it really depends on the application and the sensor, of course. I guess. Yeah. Uh, but we have some amazing batteries that are, I, if I'm not mistaken, 11 amp hours.

**Chris Gammell:** Okay.

**IoT:** Uh, which is pretty huge.

**Chris Gammell:** Yeah. Yeah. That is, that is pretty big, but, but again, that would sit there and yeah, transmit for a good chunk of time. That'd be one. So that'd be like a, a streetlight backup or something like, again, where you're sizable, you can add extra stuff in there. Right.

**IoT:** Exactly. Yes. Yeah. But you can, you can easily get, uh, I believe a year or two years. It's really depends on the application. Uh, but the year or two years is not unheard of on, uh, a two AA, AA cells.

**Chris Gammell:** That's yeah. Well, that is amazing. Um, and, and, and that's, you know, and that's also like, you also play with the amount of data you're sending, right? If it's just a little bit of data, you know, if you're updating once a day or once an hour, it's probably not that much data, right?

**IoT:** Exactly. Well, once a day and once an hour just makes also a world of difference. That's true.

**Chris Gammell:** Yep.

**IoT:** Uh, but usually what you do is, uh, send periodically, uh, I, uh, keep a live message and then, uh, send some other data when it's relevant. So if you were are measuring temperature, only send it if it's actually changed.

**Chris Gammell:** Oh, interesting. Okay. And so then the, the, that's kind of more on this, the cloud side of actually storing that it's, Oh, it's still there. It's still transmitting, but nothing else has changed. So just keep the same flat line on your graph. Exactly. Yeah. That makes sense. And then, so is that because a keep alive packet is really tiny? Um,

**IoT:** yes, it's, you can make it really tiny. So it's really low power. Uh, and you can also put a tiny bit of data in it. Uh, maybe just, just the, send the temperature once a day and, uh, to increase resolutions and when it's relevant.

**Chris Gammell:** Okay.

**IoT:** Uh, but you, you, you generally want to know every day if your device is still functioning.

**Chris Gammell:** Sure. Yeah, definitely. Right. I mean, that's, that is kind of the thing where it's like, Oh, if you, if you didn't do that, keep alive, you're like, Oh, it's fine. And then a year later, like, Oh, it actually has just not been active. Right. Yeah. Yeah.

**IoT:** Which is really bad if you're, if you're something is, uh, getting underwater or something.

**Chris Gammell:** Right. Yeah. That would be bad. So what about on the, uh, I know you're on the hardware side, but like in the stuff you've seen at least, is it usually using like MQTT or what kind of like protocols is it actually talking over? Is it just, I guess I don't even understand. And is it just a packet of,

**IoT:** yeah, it's just a packet. So Laura has its own, uh, message format and, uh, headers, um, usually on the side of the cloud where it, where it comes out the other end, it is often, uh, it goes to, into a database or it goes for your MQTT.

**Chris Gammell:** Okay. Okay. That sounds good. Um, yeah. And I guess the MQTT server, then you could just use that. If it, if it goes into the MQTT server, then that, the idea of that is that it's also broadcasting it back out to whoever subscribed for it. Right. Yeah. So if, yeah, now I'm on a wifi network, the MQTT servers on the wifi network, it received a packet, it's stored in the database. And now it's like, I'm subscribed to what is that field, field device number four. it'll just kind of relay that to me. Yes. Interesting. Um, so I'm still a little confused on the gateway piece though. Right. So if I, so you said you, you saw these other gateways, right? So you said you saw Antwerp, you saw, uh, you director, uh, and then you had your, your local one, but on the RC plane, but like, does it send it through all of them and then it's taken care of on the backend? How does it actually know who, who actually stores that data then on your, or sends the, the forwards, the data along to your endpoint?

**IoT:** Okay. So the, the message is received by all the gateways in range and all the gateways sends their data back to, uh, the same network server. Okay. And the network server actually takes care of, uh, double receivings and selects the best gateway to, uh, sends a message back if you want to.

**Chris Gammell:** Oh, interesting. Okay. So that is one of the big roles of the network server, like you're saying.

**IoT:** Yes.

**Chris Gammell:** Okay. And then, huh. And so the network server though is actually like on a cloud device. Is that the idea?

**IoT:** Yeah. Yeah. It's, it's also, yeah, it's, you can put it on your gateway, but that's for testing. It's, it's great, but in a, any serious application you want it in the cloud.

**Chris Gammell:** Right. Cause then you'd also have to talk back through all the, the cloud, infrastructure to, if you had multiple gateways, right? If you had it on your gateway.

**IoT:** Yes.

**Chris Gammell:** Um,

**IoT:** uh, yeah, if you have multiple gateways, then it's no question. You, you should put it somewhere central. Okay. Uh, you also need quite a bit of horsepower. If you want to send, uh, if you, for example, use class a and want to send something back to the nodes after it has sent something to you, uh, you have a couple of, um, I believe tens of milliseconds to, uh, uh, process, uh, what did I send, uh, think of something to send back and then get it to the device before it goes to sleep again.

**Chris Gammell:** Okay. And then you, yeah. And you said in class a, it's, it's, so you said there's listening for two slots, one that's right after the uplink. And then the one that's later, how does it know when to wake back up? Is it like a defined time?

**IoT:** Yeah, that's a defined time.

**Chris Gammell:** Okay. And is that settable as well? Or is that something that's just like, uh, it's always 40 seconds later?

**IoT:** Um, I believe it's fixed. I don't, I don't actually know the number.

**Chris Gammell:** Okay. All right. Well, so maybe a better question is how often are you using each of these a, B or C? Like, is it, I mean, it sounds like it's application dependent, but, um, what, what have you seen most?

**IoT:** Uh, by far the most is class a.

**Chris Gammell:** Okay.

**IoT:** And also by far the most, uh, it's only uplink.

**Chris Gammell:** Oh, okay. So it's just transmitting temperature and then you don't send anything back.

**IoT:** Yeah. There's, there's very little, uh, use cases where the device would do something, uh, that is controlled from the network.

**Chris Gammell:** Okay. Yeah. I was going to, because that was my next question too, is like, when you do need to send something back, which, which one do you usually choose? Do you choose right after you choose the second slot?

**IoT:** Uh, usually, uh, if it has to go through your application, you are already too late for, for the, uh, the first slot. Okay. The first slot is for data that you already, uh, put in a queue.

**Chris Gammell:** Oh, okay. Okay. So it's like, uh, you schedule like, uh, like a shutdown for the night or some kind of command set that happens right after. That's kind of the idea.

**IoT:** Yeah. For example, or, or like a settings change. That's, that's one use case to use downlink is, uh, for example, you don't want the device to send every day, but every hour because the situation changed. And then you say, Hey, uh, send it every hour to me instead of every day. Yeah. And that's an ideal thing to, uh, to put in the first downlink message.

**Chris Gammell:** So what about like, can, so in these, in these situations where it's class a or even, even the other like class B or C, um, is it possible to update firmware over this? Or is that just way too much stuff?

**IoT:** No, that that's, that's not an option. I don't know if it's on the roadmap, but, uh, I currently that's not an option. Okay. Uh, all Laura devices also in, uh, speak FSK.

**Chris Gammell:** Okay.

**IoT:** Which enables a far better bandwidth. Uh, but it comes with,

**Chris Gammell:** I don't know what that is actually. Sorry.

**IoT:** Frequency shift keying.

**Chris Gammell:** Okay.

**IoT:** And, uh, that, yeah, that's, it's a more basic kind of modulation, if you will. Uh, but you, you could do it over, over FSK, but I have never seen any case where that has been done.

**Chris Gammell:** So, but that would be, you'd have to be local to the device, just not plugged into it.

**IoT:** Uh, yes. Okay.

**Chris Gammell:** Yeah. So I, yeah, I assume that one of the benefits of this is that you can make an enclosed, like a waterproof kind of, your battery's never going away. Well, no, it's got, you got a battery for a while. You're, you know, you're low power. You're don't need much in that way. I assume that you could enclose this whole thing and just be like, when it's dead, we're throwing it out. Yes. Not, not that I approve of that, but yeah. Um, but you're saying that FSK would allow to actually reprogram then without, without a USB cable.

**IoT:** Yeah. But I would, I would recommend using a Bluetooth low energy to, uh, firmware update.

**Chris Gammell:** Okay. All right. So just some kind of wireless near nearby type thing, but you're not going to do it from a, from a gateway back down to the, the, the, the node at this point.

**IoT:** No, not Laura is not the right technology for such application.

**Chris Gammell:** Okay. Yeah. Uh, so what is the, what has been the best, I mean, you've seen a couple applications at this point. What is, what is, what has been like the, what type of application, not necessarily who, or, or, you know, who's using it, but like what type of application has been like, Oh, this is just tailor made for it.

**IoT:** Um, I, I think remote sensing is, uh, is, is, is tailor made for it. Uh, there are two different scenarios where Laura really shines. And that is when there is no other network available. So you have to set one up anyway. Uh,

**Chris Gammell:** uh,

**IoT:** and when you have a relatively large amount of sensors in a relatively tiny amount of space. Um, so let's say you have like a container terminal and rather than we have a pretty big one. Oh, like a shipping port.

**Chris Gammell:** You mean like, yeah, yeah. Okay.

**IoT:** And there are containers there that are on a, on a train that is a few kilometers, a square kilometers. Uh, so you can use only just one gateway or maybe three if you want to get around some dead corners, uh, to cover the whole place.

**Chris Gammell:** Yeah. Okay.

**IoT:** And then, then it would be really cheap. Yeah. But if you have an application that is over the whole country, you're traveling around, then you're maybe better off using another technology.

**Chris Gammell:** Yeah. Yeah. No, that's, that's a great point. And so like, I was really surprised, you know, like I've come into a, you know, internet connected type role now too. And my, my new thing is like, yeah, there's not, you're not going to get away with just one. Someone who says there's only one way to do a thing or that there's only one thing that will solve all problems is, is lying through their teeth. Right. Because sometimes it's Laura, sometimes it's, you know, or, or similar type of thing. Sometimes wifi is the right call, sometimes Bluetooth, sometimes cellular, whatever. So yeah, it's, uh, you gotta, unfortunately you have to know all of them, but that's also kind of exciting, I suppose. And it seems like with the hardware that's out there, it's getting easier. Does that sound right or no?

**IoT:** Yeah, yeah, sure. Uh, you can use a multitude of technologies right from your home, uh, ordering it from, uh, AliExpress or something. And, uh, yeah, I, I think it's really easy to implement these technologies today, uh, compared to what you have to do 10 years ago.

**Chris Gammell:** Yeah. Okay. That's good. So like, so in your, in your day to day, are you mostly focusing then more on the sensor side of things and the, the micro processing type stuff or, or what is, what is, is it, how much of this is a hassle to you or how much is it just kind of built in at this point?

**IoT:** Um, not for my, the main, the main things I, I, I am working on is sensor technology and, uh, sometimes converting, uh, an old, an older sensor technology to one that is more low power. Uh, because of the degree, the low power battery requirements. Uh, so yeah, for example, the MQ gas sensors are a very good example. Okay. Uh, it's very fun to, to hook them up to the Arduino and, uh, uh, smell some, some CO2 or methane or something else, but there's a heater elements inside those sensors. So it's not great for low power. No, that's out of the question. And also as a heating, a heating time of 30 minutes or something ridiculous.

**Chris Gammell:** Whoa. Okay. Uh, so what do you, are you like doing pulses or how you have to actually change it around then? Or, or what are you doing there?

**IoT:** Um, what I am usually working on is finding other sensor solutions, uh, from manufacturers or sometimes even they're rolling our own.

**Chris Gammell:** Oh, cool. That's neat. Um, yeah. How much, how much of it is, are you seeing a lot of projects that are kind of building this stuff with small solar panels as well? Or does that make sense for a lot of this cases here?

**IoT:** Yeah, we actually have, uh, a finger called the tryst and that's a light energy module.

**Chris Gammell:** Okay.

**IoT:** And, uh, essentially what it is is a little brick and it has a solar panel on it that is really efficient, uh, indoors.

**Chris Gammell:** Oh, wow. okay.

**IoT:** So it has an, an efficiency optimum that is around, uh, around the lights level that you have in a business building and you can use them indoor to power your sensor.

**Chris Gammell:** Hmm. That sounds like, uh, yeah. And if, so you've got a low power sensor, you've got, yeah, with indoor lighting, that's pretty impressive actually. Uh, what kind of output does it get?

**IoT:** Um, power outputs, um, I, I, I think it has a peak, I don't, I don't actually know.

**Chris Gammell:** I guess it's probably like, it's probably charging a battery though, right?

**IoT:** So it's charging, it's charging a buffer and, uh, it's working from 200 lux. Wow.

**Chris Gammell:** Okay. Yeah. That's pretty low. Yeah. That's great. Uh, yeah. I've seen those, uh, a lot of the, like the, what do they call them? Like microchargers or something like that, like where they kind of sip off of, uh, uh, solar cells and stuff like that. They have really, really low drop diodes that kind of help with boost circuits. So, uh, really interesting stuff.

**IoT:** So a lower message takes, uh, in the order of tens of milliamps. Uh huh. And, uh, if you have, uh, some kind of buffer, uh, you can, you can use this module to send lower messages. Okay.

**Chris Gammell:** That's good. Yeah. That's good. That's a good to know. So then, so then in the only real restriction would be how long it takes to refill that buffer, right?

**IoT:** Yes. Okay. Yeah, that's true. Uh, and it will be quicker when there's a lot more light and it will be slower. Sure. Sure. Sure. Right.

**Chris Gammell:** But that's a, that's a great capacity thing. Uh, is that one of the things that you can go in? So say you were in class a and you had a, you had a downlink slot. Could you tell it to, to stop sending so much data because it, it, because of a change in the, um, the power capabilities or, uh,

**IoT:** it would be smarter to do that locally. Okay. Uh, so what the, sometimes try to do is, uh, uh, make the, the sending scheme dependent on the energy that is available.

**Chris Gammell:** Okay. So you do like a, like a current sensor in line and you say, well, I only have, or is it like you, you can talk to that power brick type thing?

**IoT:** Uh, you, you cannot, you, well, as yeah, you can, you can talk to it. Uh, you can measure how full it is in, in, in, in voltage, and then you can say, okay, I've got about this much energy left. So I'm going to send this often.

**Chris Gammell:** Okay. All right. And then, yeah, would you, would you sometimes then encode like how long, how often you're going to be sending with that one message then as well?

**IoT:** Uh, you could, but that's a trade off. It also costs extra time to send actually that, uh, that data. I want to keep it actually as short as possible.

**Chris Gammell:** Interesting. So you, so you do that as well. So you optimize the packet length, to, to only send exactly what you need.

**IoT:** Yes. And, and the smart things to do is, uh, for, uh, example, GPS location is just sends, uh, the full location once. And then, uh, from that send a relative location.

**Chris Gammell:** Oh, interesting. Okay.

**IoT:** So if your device is not moving all over the world, uh, really fast, then it's really feasible and it's, it saves a lot of data.

**Chris Gammell:** Uh, and then is, does that also pair it with the, you know, don't send it unless it actually is changing, or you just send, um, when you say relative, then is it because there's fewer digits of precision needed?

**IoT:** Uh, yeah, but, uh, there is the, the same kind of precision, but, um, why would you send, uh, why would you define where you are on the world scale when you never move a more than a few kilometers a day or something?

**Chris Gammell:** Right. Right. I'm just thinking about like the, so it's usually like 49.42466 or something like that, right? But then you'd only be sending a 0.0006 or something. Wouldn't that be it? So I'm just thinking like, depending on how you format that number, it could be the same length. If it uses this, like it was like a float or something, you'd still send the same number of bits though, wouldn't you? Or is it? Yeah,

**IoT:** but if you multiply it by like a thousand, then it becomes a lot of smaller number.

**Chris Gammell:** Oh, okay. Okay. Interesting.

**IoT:** Yeah. So you have to keep the track on by that, uh, with that, uh, in the backend to divide it by a thousand again.

**Chris Gammell:** Got it. Okay. Yeah. So is there, are there any other compression techniques that you, you know, then implement in this case, or is it more of the, it's a customized enough message that doesn't need some compression?

**IoT:** We don't have a standard way to compress data. Uh, but there's a lot of these tricks you can do, uh, to make the data as small as possible.

**Chris Gammell:** Yeah. Yeah. Yeah. That's great. That, that is, that's a good one. I mean, um, okay. That's, that's really interesting. Um, and maybe give us an idea. We are, we're over an hour here and I could probably keep going for a little while, but, um, how much of this is, how much standardization is there at all? Even, even for like within your company project to project, is it like, is it always custom because of these power needs?

**IoT:** Um, um, yeah, it's,

**IoT:** it's mostly custom with our projects. There are actually some standards, uh, that are defined by some LoRa backends. Okay. So there are some companies that deploy a network, uh, serve, uh, server and application server. Uh-huh. And they also define a way to, um, to structure your messages. And, uh, some people, some people standardize on it and some people don't. And, but we usually have the really hard cases where, uh, we're right on the edge of the, the possibility. So we have to, uh, right. Use, uh, techniques to reduce it. Yep.

**Chris Gammell:** Yeah, no, I know, I know that goes like, I, I have a friend that does Bluetooth standard stuff and sometimes the Bluetooth ain't so standard. You know, like if you, if you're right on the edge, yeah, sometimes you gotta just like, well, you're not gonna work with everything of course, but your, your devices that are talking to each other probably will because they, they understand those variations and all that other stuff. So it's just about defining both ends. Um, I'm trying to figure out if I, I have a clear picture on, I, this has been first off very, very useful. Um, and I will, I will be posting all of these, uh, pictures you sent me, which were very useful and links and stuff. I, I, I'm still, I've, I may have asked this already, but if there's a device, so there's node in the field, I make a node, you're running a gateway. Are you, are you saying that I can just connect to any gateway? That's Laura based?

**IoT:** Um, it's not really a connection. It's a really a connectionless, uh, thing, Laura. Okay. So, uh, certainly if you send a message, which is broadcasted to everyone, uh, then I can receive it with my gateway. Uh, uh, and my gateway would send it to my network and my network would have, uh, a couple of keys from, for its applications. And it would see, uh, with which key it can decode the message.

**Chris Gammell:** Okay.

**IoT:** If it's cannot decodes the message with my keys, because you are not on my network, then I don't have anything, uh, right. To do with the data.

**Chris Gammell:** Lost in the ether. Right. Yeah. I get, okay. I get that. It's thrown away. Um, but I guess I'm kind of thinking about it like wifi at this point, but maybe that's not a good example, but like I can see other people's gateways now. So I, so I have a node, my node sees your gateway. Um, it has to be actually authenticated at some point.

**IoT:** No, it's, it's really, it's connectionless. So it's a broadcast every time. Uh huh. And then everybody forgets everybody.

**Chris Gammell:** Oh.

**IoT:** So there's, there is a session in the sense of the, the, the session keys and the security. Uh, but the gateway is, is fully passive in that sense that it doesn't know which nodes are talking to it and to which nodes it is talking to.

**Chris Gammell:** Huh?

**IoT:** Yeah. And only the network, the, the, the backend knows its nodes and knows who it's talking to.

**Chris Gammell:** So, Oh, all right. That might be getting a little too software-y for me. Then maybe that's where, maybe this is where this is falling apart in my mind, but yeah. Okay. So, so the gateways are front ends with a backhaul to a network server. And then that's where all the magic happens. But, but the gateways are there to enable this on the RF side, right? So it's internet to Laura packet thingy.

**IoT:** Exactly. It's, it's not quite SDR yet, but, uh, it's, it's, they don't do really much more than an SDR would do.

**Chris Gammell:** Hmm. Yeah. Okay. Okay. That makes sense. Um, what about like, so from a security perspective, it sounds like you've, I know you said you were not a security person, but like it, you've at least thought through some of this stuff though. So wouldn't it be possible that some, like some rogue person could come and like flood a gateway with a bunch of bad traffic?

**IoT:** Um,

**Chris Gammell:** if it, uh, like jamming, I guess so. I guess you could do that on a wife. I mean, you can do that on authenticated networks too. So that's not a big deal. Right.

**IoT:** It's,

**IoT:** um, with, with, with wifi, you have some, some certain attacks that, that's worked this way where you have a deauthentication attack.

**Chris Gammell:** Sure. Yep.

**IoT:** Uh, so you send to the, the, the access point, like, uh, I am the authenticated and you impersonate some else, some other device. Yeah. And you send to the device, like, uh, the network has, um, has disconnected from you. And then they both think they are disconnected. That's some kind of attack you could not do with Laura because there is no connected or disconnected state. Huh?

**Chris Gammell:** So the only thing you could really do is jam, like you said, because you're not, you're not interrupting someone's like point A to point B connection with a key. You're just flooding the, the, the receiver with too much stuff. Right?

**IoT:** Yes. Okay. You could do that. Uh, you could do that with Laura specific packets or with just random noise. Yeah.

**Chris Gammell:** The spark gap. Yes. Yeah. Okay. Well, um, I think I get it. Uh, I'm sure that if people don't get it, they will leave, uh, comments in our comment section or maybe on our Reddit. But, uh, Richard, this has been a great, uh, yeah. Thanks for explaining all this stuff to me. It sounds like you've got quite a handle on it and, uh, it's, you're working on some interesting things. So where can people find out more about you or your company or anything else going on in your life?

**IoT:** Um, you, you could go to our company's website. Sure. Which is TWTG.io. Right. Um, if you, if you live around the Netherlands or in the Netherlands and you want to work here, that's also possible. Oh, nice. Um, if you want to contact me directly, I can leave an email address in, uh, in the, in the comments or something.

**Chris Gammell:** Right. And, and we were talking about before the show, you have a Twitter account, but it's, uh, somewhat silent. Uh, yeah. Are you, well, uh, you said you're a big Hackaday fan though. Maybe, are you on the Hackaday IO? Maybe people could reach you there.

**IoT:** Uh, I am on the Hackaday IO. I have a, I have a few projects there. Uh, also I haven't been there for a while. So.

**Chris Gammell:** All right. Well, we'll link your, we'll link your profile there as well. Cause there's a chat thing in the backend, but we'll also have the email address. Yes. Okay. Well, thanks so much. Uh, I appreciate, uh, hearing all about this stuff and I'm going to be looking into it more. I do have some, I do have some modders on my desk and I promise they'll be working soon. I'll have more questions for you too. Okay. All right. Thanks again.

**IoT:** Bye. Bye.

**Speaker ?:** Bye. Outro Music
