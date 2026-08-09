---
episode: 557
title: Generic Nodes with Orkhan Amiraslanov
url: https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/
---

**Orkhan Amiraslanov:** This is The Amp Hour Podcast. Movie September 12th, 2021. Episode 557. Generic Nodes with Orkin Amir-Slanov.

**LoRaWAN:** Welcome to the Amp Hour.

**Chris Gammell:** I'm Chris Gammell of Contextual Electronics. Hello, my name is Orkin Amir-Slanov, and I'm a hardware developer from the Things Industries. Hey, Orkin, how are you? I'm good, Chris. Thanks for having me. And hello to all the listeners and viewers, if there are me.

**LoRaWAN:** Yeah, yeah. Yeah, we are doing video here. We're hopefully going to be able to show off some of the stuff that Orkin's been working on. And people may have heard the Things Industries before, me talking about it, other people talking about it. It is LoRaWAN-based. Can you give people a rundown, a reminder on what LoRa and LoRaWAN is generally?

**Chris Gammell:** Sure. So there are lots of radio protocols currently in the market. And LoRaWAN, or LoRa, is actually one of them very popular in the LPWAN, or Low Power Wide Area Network Protocol. It's actually invented by Semtech. And in the recent years, it gained quite a bit of popularity between the IoT community. And in 2015, Things Network, or Things Industries, took this idea, and they run with creating publicly an open-source LoRaWAN network server, which people would buy the gateways from different vendors, even the gateway of the Things Industries, and then install it in their home, in the apartment, or in their backyard. And this would serve as a sensor network. And the gateway is like a dummy device which forwards the data to the LoRa server. And then you have your own account, and all the data is encrypted. You can do whatever you want with that data. Basically, LoRa as a protocol is very good. The name, the meaning of the LoRa, it means long-range. But because it uses a protocol, or like a chirp, which was, I believe, invented in World War II, for the very long-range communication, so it uses chips of packets, and it's really resistant against noise and other radio interferences. So being resistant, being long-range, it's also very low power. So typical LoRa transceivers, it can go down to less than one microamp sleep currents. So that's very good for battery-powered devices.

**LoRaWAN:** Mm-hmm, yep. Yeah, and it's definitely still higher during transmit, during a little bit higher, or a little bit lower for receive. But yeah, it's very impressive what's out there. Low bandwidth, though, too. People should always remember that. Exactly, exactly. Low and slow, but yeah, slow. It's very slow.

**Chris Gammell:** It's not very useful for real-time applications whenever you need to hide data-rate transmission. For that, 2.4 gigahertz, NRF, or Bluetooth or Wi-Fi would be more suitable.

**LoRaWAN:** Mm-hmm, yeah, yeah. Cool. Cool, okay. Yeah, and I think the thing that I always think about with LoRaWAN is it seems like it was like the networking engineers got in there and they're like, well, we can make it more like a true network, right? So it's like you basically are routing packets. Everything's kind of treated more like a traditional IT setup.

**Chris Gammell:** Yeah, like OC model. There are, I think, two layers of the OC model. They're implemented MAC layer and physical layer. So it's very similar to the 802.1504 stack. It actually inherits lots of stuff from there. Oh, cool. Yeah. But instead of using IP, it uses the device, EUIs, and a couple of security layers involved, like a network session key, application session keys. I think you know that already. Sure.

**LoRaWAN:** Yeah. Well, a little bit. I mean, I haven't used, I've used LoRaWAN by itself. I've used like an RF, no, what's the hope RF modules? The 96, 95.

**Chris Gammell:** RFM 65, RFM 95.

**LoRaWAN:** 95. Okay. Yeah. So I've used those. Basically, I think I was using like an Adafruit, feather, LoRa feather, you know, just talking to one another, right? So like point to point, just real simple, low power. Great. Worked out. Awesome. As long as nobody else was talking to the channel, as long as I, you know, didn't mess up the encoding that I had input in there, you know, because I was basically like compressing down to bits, but this is like much, many more layers above that. Right? So this is like, now you're doing that same thing for a node, but then you also have a processor that's also handling communication. And then there's the, the stacks all the way up.

**Chris Gammell:** And it is basically a star network where all the sensors are sending data in a Aloha style. So there one sensors can wake up and send the data uplink anytime they want usually, and then the gateway receives it. And then the sensors, the nodes open receive window in a LoRa class A for the downlink communication. That's for class A. Then there are a couple of LoRaWAN classes. There's a class A, class B, and C. The most simple one is the class A. Then the, after the uplink gateway transfers the data or forwards the data to the network server. And the network server transfers to the application server. Then you can do a visualization. You can do long-term data logging, whatever you want, or even machine learning on top of that, on top of the data. Yeah.

**LoRaWAN:** Yeah. Yeah. And it does, it, uh, I remember there was also, there's like eight, eight channels. How many channels are there? There's like that you can.

**Chris Gammell:** For Europe, it is eight channels. And I believe for us, there should be two more. Oh, okay. All right. For nine 15 bands are two more bands.

**LoRaWAN:** Yeah. Cause that was the other thing I remembered. I remember that rock wireless, I think makes a receiver as well. Like a, like a raspberry PI based receiver, but then there's also like the commercial ones that the things industries makes. And then I think at one point was, we had a guest on Richard Yenis of TWTG. And I, I'm not sure if he's still there. And they were building one of the things for the things industries. And then there's other people as well.

**Chris Gammell:** It was like Arduino based, um, things who know. Yes. And, uh, the things note. So they were the earlier version of the, like a sensor notes or prototyping devices for the

**LoRaWAN:** things industries. Uh huh. Yep. Yeah. And I remember, I think Dave Jones had bought one of the receivers as well.

**Chris Gammell:** He ranted quite a bit about the things node and the gateway because.

**LoRaWAN:** I think he had some troubles with the software setup.

**Chris Gammell:** I believe it was configured that the, the units that he received by default was configured for EU, 868. Yeah. And in Australia you have 920 and, and he had to reconfigure it. So that was a bit of a, you have to read the manual first. Yeah. Yeah. Everything is upside down there. Yeah.

**LoRaWAN:** No, I think that is a good point about the, the, uh, the different frequencies as well. So 868 and you 915, I believe around here. Yep. There's a shared 433 that not as many people use, I believe.

**Chris Gammell:** No, it's 470 for China and slightly different for Japan and India. Okay.

**LoRaWAN:** We also had JP Norrera on the show. Uh, and he talked about Laura a little bit, but he was not as big a fan. He was working on that Haystack or some kind of other stack thing. Yes.

**Chris Gammell:** They are using Laura as a physical transceiver, but they are building on top of it to make it more resistant. I, I, I listened to that episode. It was really nice.

**LoRaWAN:** Yeah. Yeah. That was a, it was interesting to hear that, you know, cause like I had, obviously I hear a lot of like the popular media stuff. I, you know, I did some research on my own and just reading around other things, network stuff. And I hadn't heard otherwise and then JP's like, oh, well dash seven is better. And you know, here's why. And yeah, just getting different. Inputs on these things is, you know, you don't know all of it until you've talked to people in the industry and oh, this, this is good. This sucks. This sucks that, you know, this is good, that sort of thing. So yeah, it's a, it's good to just hear all these different perspectives. And I think the things industries and you know, the, the open source backend stuff has been improving over time too.

**Chris Gammell:** Yes. Now, uh, late recently we've released, uh, the, the thing stack version three. Uh, so we have the commercial, uh, sorry for the background noise. So we have the commercial offering the, the thing stack, and we also have the, the things network, which is open for public. And we have also moved the things network from version two to version three. And many people who had gateways and, and devices connected had to migrate those to V3. Hmm. How did that go? Well, it's going fine. We have lots of instruction, easy to follow instructions and it's basically just copying the gateway UI and pasting in the new interface and. Usually good to go. Yeah.

**LoRaWAN:** Yeah. So the things, so just to disambiguate here too, the things network is what someone could go and buy or build a node. And put it onto this open source kind of general data collector thing. Right. And then it's like a community source thing. Is that right?

**Chris Gammell:** So the, the things network, let's say you're living in an area where there's a gateway reception nearby, somebody already installed it, or there could be that some. Telco can, uh, company have installed it already. Yeah. And you can use that gateway to relay your information to your backend. Yep. If there are no gateway reception, uh, you can install your own gateway and enable it to be, uh, on the things network, uh, basically to serve the community, but also you can use it for your own purposes. Got it. Got it. And then the, this is the public, but you can also use the LoRaWAN as a privately, everything would be private. You can, you can host it in your local computer or somewhere in the cloud and then not nothing will be open to the public.

**LoRaWAN:** Right. And so then if, so if I'm running my own cloud, my own gateways, that would be the thing stack, right? That would be like, I would be using this either I'm licensing it or there's the open source version as well. And then that's handling all of the packets that are coming in and they're just for my, so say I have a client as a consultant, I'm like, Hey, you should be using LoRaWAN. I think we should use the thing stack. It's all going to be private, you know, so it's encoded. It's got keys all the way through the data is coming back through that sort of thing. Exactly.

**Chris Gammell:** It's more the thing stack from the things industries is suitable more for the commercial applications. Yeah. And the things network is for public, but you can use the things network as a, at the initial phase of your device design and prototyping. Yeah. Just to get a proof of concept. Yep. Yeah.

**LoRaWAN:** Nothing's more frustrating than thinking a device. You're looking at the, you are, you're like, it's sending packets. Where, where are they? Exactly. Yeah. Yeah.

**LoRaWAN:** Okay. Well let's, we're going to get to the hardware for sure. You've built some very interesting hardware I'd like to talk about, but I'd like to get a little bit background on you first. So how did you kind of come to be working for the things industries and on this, on this stuff?

**Chris Gammell:** Well, yeah, it's, it's a nice, long story, but I'll try to keep it short. So I'm actually originally from Azerbaijan and it's a small country, post Soviet country between Russia and Iran in caucuses. And so I did my bachelor's there and starting from 2007, I did a industrial automation and process control. And because our country is all the rich country and most of the people are basically following the jobs and leads in the petroleum industry. And I also did the same, but for me, electronics was always more interesting. And I'm more of a mostly self-taught electronics hardware developer.

**Speaker ?:** Yeah.

**Chris Gammell:** Great. And after the, like I was about to finish my bachelor's and decided to do the master's instead of, I also received a job offer in back home, but I basically had to respectfully decline it and follow the like lifelong passion of electronics. And I was expect accepted to embedded master's program in, in Norway. It was a joint degree first year in Norway, second year in Germany. And I basically went there, did my master's two years. And during my master's on the second year in, while in Germany, I started working at the nearby company. It's called a German research center for artificial intelligence. And I was working there as a student assistant in that respect is really cool. There are lots of student jobs available where you can earn some pocket money. Yeah.

**LoRaWAN:** Right. To support your studies. Yeah. I mean, well, I mean, there's a lot of good beer there. So, I mean, exactly. Yeah. Also that.

**Speaker ?:** Yeah.

**Chris Gammell:** Basically I was earning my beer money more than enough. And also learning lots of cool stuff, doing lots of cool stuff at that company. And I also got to do my master thesis there. And it was about, you know, this electro luminescent displays. I think Ben Krasnow did really nice electro luminescent display of Saturn module. It was like a timing module, I believe. So I was basically doing a similar thing and designing a driver module for it using tons of triacs. I was going to say it's high voltage usually, right? It is high voltage. And I also had to design the inverter myself and got electrocuted a couple of times. Oh no. Yeah. Because it uses high frequency, high voltage AC. So like 200 volts between 200 and 500 Hertz AC. And I had some protection on board. It's when like overcurrent protection, things like that, but still you would get some occasional touches and tickles. That'll tickle. Exactly. Yeah. And basically my master's project was building this 64 by 64 half or so, two feet by two, two foot or feet. Yeah. 60 centimeters by six centimeters. Big display. Yeah. Using electro luminescence. And it turned out to be working functional, but using the AC, there were lots of leakage current. There was a ghosting effect. Had to do lots of FPGA programming on top of that because FPGA was used to drive the display buffer, frame buffer. Yeah. And there was lots of opto isolators driving the triax with a zero crossing detection, things like that. Wow. Yeah. There was lots of programming involved, but I managed to reduce the ghosting effect, but it wasn't enough. So. Is there a video of this anywhere though? We can maybe share? Oh, maybe, but maybe I can share with you the master thesis itself later. Okay. Yeah. Yeah. That'd be great. Yeah. Yeah. But it wasn't as polished as let's say Ben, what Ben Krasnov did. Wow. Because he was using, he was using very small area and he didn't need much of a driving current to run each pixel. Yeah. And he ended up using one of those small chips with, which has basically built in AC drivers. Yeah. 64 by 64, I believe. I think he still blew them up a bunch though too, right? It didn't. Yes. Yes. I mean, those are, I tried to use them, but for my pixel size was around five by five millimeters. It was for bigger displays and the current was much higher than the chip.

**LoRaWAN:** You know, they make LEDs now. I'm just saying, you know, LEDs are a lot easier.

**Chris Gammell:** The thing is this, this was quite easy to produce in the lab. So we would make our own, just use like a phosphor paste and the dielectric paste laid on the, with a, with a screen printing. Yeah. And we could easily print the display. You cannot do that with the OLED.

**LoRaWAN:** Yeah, that's right. Exactly. I mean like, and making like custom, you're so you're seeing like you can make custom patterns and things like that and light them up. Yeah.

**Chris Gammell:** So you can, you can add like a, you can switch the display in between and use it as a capacitive sensing. So you can use the same area to do the sensing as a touch input, also display the results there.

**LoRaWAN:** Wow. And I mean, is the touch input 500 volts as well? No. So you had to use, you switch the device basically. You're not running it at that time. Yeah. That's cool. No, that's really cool.

**Chris Gammell:** That's really cool. Yeah. And it was around that time I started looking into this thing's network and I started because, okay. After my master thesis, I started working at that company as a fellow research assistant and, and started doing lots of wireless sensor network, hardware development. I was basically designing mostly Bluetooth, sometimes wifi, and sometimes custom 2.4 gigahertz based sensor nodes, which would read the data, collect the data. And then we would run a couple of, let's say experiments and then use that data, collect the data to do a machine learning on top of it. Oh, cool. For example, just using an accelerometer to find or to detect the person who is wearing the sensor based on the, or walking patterns or movement patterns, things like that. Yeah. So we also had the capacitive sensors installed under the carpet and based on the gait analysis, what try to find who is walking on this carpet. Wow. So basically non-invasive, not using camera, but all the other sensors to detect the person, to detect who is walking on.

**LoRaWAN:** Detect a specific person you're saying. Exactly. Yeah. And someone who doesn't even have like a super like definitive walk, like they don't have like a limp or something like that. They're just, they just walk in a certain way. They have heavy footsteps or they. Exactly. Yeah. Yeah.

**Chris Gammell:** Just the frequency of the steps or how, how the steps are printed, imprinted on the carpet. Pretty shuffle. Yeah. Yeah. Yeah. Yeah. And I was doing that as my day job, but also got interested in the lower band technology and persuaded my boss to buy those gateways. And we installed a couple of them around the company in the top level or on the balcony, let's say, and opened it as a public publicly open things network gateway. I also, after afterwards, I started designing the actual boards just to, just for fun. Yeah. Yeah. And it was, I believe it was around 2017 or end of 2017, microchip came, came up with the SAMR 34. It was the first Laura when or Laura enabled zip. So it's a Cortex M0 plus, plus a SX12 76 Laura zip all in one package. And I met, I met them in the electronica, I believe in the fair. And they had this big, uh, $99 development board. What is the market?

**LoRaWAN:** I think it was a B it was the, uh, one of their explained boards, I believe. Exactly. Yeah. I never understood that, uh, platform. I was like, It has some cool features.

**Chris Gammell:** It has some,

**LoRaWAN:** I just thought it was like, we'll break out every pin in the ugliest way possible. I feel like that was there. Yes. Yes.

**Chris Gammell:** That's true. I totally agree with that. But some of them has really nice, like onboard power measurement. Ah, that's nice. And you can, you can do like a down to microamp, even nanoamp range. So you can also use the same board to, to the current measurement in other boards or also program the other boards. Yeah. Uh, so I basically got into their booth and I asked them, okay, they, they didn't have any modules available for this summer 34. Um, I decided to design my own and at a time I started using key cats since 2014, I started using key cat. Thanks to you, by the way.

**LoRaWAN:** Oh, awesome. Yeah.

**Chris Gammell:** And for all my work at, at my day job, I started shifting everything to keep all the projects to key cat. Yeah. And, uh, also designed, decided to design a radio module around 14 by 16 millimeters size, like very small, uh, radio module around the summer 34 basically took the explain board design, stripped down all the unnecessary part, kept the core part. Are you saying iridium like the satellite?

**LoRaWAN:** No, no, no. Or sorry. Were you saying iridium module or something? You said some kind of module. No, the radio module.

**Chris Gammell:** Oh, radio module. Oh, sorry.

**LoRaWAN:** Okay. I misread you.

**Chris Gammell:** Basically there was no commercially available radio module for the summer. Yes. I decided to design my own using. Yeah.

**LoRaWAN:** I remember you were posting about it on, on Twitter a bunch as well. And I was so excited about it. Cause it was just like, and it was all, it's like a really very fine pitch BGA as well. Right? Yes. Yes, it is.

**Chris Gammell:** I believe it's 0.5. Yeah. Uh, the, the PCB design itself was also basically like using, doing, doing the key cat. It was very manual process. We're doing four layer, very small board, trying to fit everything, all the Vs and also trying to keep the cost low because as you know, the drill size and the. Annual ring, if it gets too small, the price just jumps. That's right.

**LoRaWAN:** Right. Even PCB way will, will charge you many thousands if you, if you want them to. Yep.

**Chris Gammell:** But I managed to fit everything into one board and managed to get it fabricated by OSHPAR. Because of the PCB width, the track width was too small. Some of the tracks got short circuited, but I had to manually just take the X-Acto knife and just cleared all the tracks and made a couple of prototypes for this board. And it started working and I was constantly posting the updates on Twitter and people got interested in lots of people contact me and you want to sell this because they were also interested in the module for this MR34. Yeah. And there was nothing available. Actually micro chip, micro chip came up with an official module from, from them about two years later. Only there was a couple of modules like the RAC 4260. Yeah. Which was released about a year after, but at the time there was nothing about it. And I also posted all the design files on, on GitHub and basically went with the low volume manufacturing of this module and it started selling them on Tinder. It made a feather board for it, like a breakout board. I actually have it here.

**LoRaWAN:** One second. I can do this. I know how to do this. There we go. All right. Yes. So the, so showing, so just to paint a little word picture here. So it looks like you, so you built your own module here, like a castellated edge. Uncertified just to be. That's right. Right. But it's a basically like breakout for the same MR34. Exactly. So that you could easily put that onto their font, their designs. And so it's tiny. It's yeah. So did you end up staying with HodgePark for the, for that module then too? Oh, no, no, no.

**Chris Gammell:** I went to China and I believe I used PCB go, go at a time and they, they offered a really nice price. Mm-hmm. And they, yeah, it was the yield total yield was like about 90%. And yeah, it was good. Yeah.

**LoRaWAN:** That's good. Yeah. And I mean, and then you, you have like a lot of these little breakouts and then you can put the rest, put it onto a larger board. So then you also sell the penguino. What's the penguino? Is that right?

**Chris Gammell:** Yeah. Yeah. This is like a family of devices, LoRaWAN, uh, transceivers and all of them are open source.

**LoRaWAN:** Yeah. And you have the, uh, the, the first Azerbaijan open source hardware number here. Exactly. For the, uh, 4260. Yeah.

**Chris Gammell:** That's pretty cool. Yeah.

**LoRaWAN:** So that's, so that's based on the Rockler wireless module basically, which is, is certified or is not certified?

**Chris Gammell:** That is certified. That is also some more 34 based. Got it. Okay, cool.

**LoRaWAN:** Yeah. And so, and then, yeah, this is nice for doing breakouts. It's all feather form factor. It looks like. Mm-hmm .

**Chris Gammell:** Yeah. I basically have a, now I have, I basically have a, like a template circuit for like power supply for battery monitoring, battery protection, short circuit protection, things like that. And then I just throw in every new module there just for testing and then create a nice breakout, better base breakout. Yeah.

**LoRaWAN:** Yeah. Yeah. I've been using feather for stuff. It's a, it's a, it's a nice, uh, form factor.

**Chris Gammell:** Yeah. It's really nice. And you can find lots of like a 3d cases for it. I printed a bunch of them and it was just giving away on the Tindy. Mm-hmm . Yeah. That's great.

**LoRaWAN:** That's great. And so then using, using the Sam R 34, so a Cortex M zero, how is the driver's support and everything like that? Like what is there a library to talk to Laura, uh, the SX 1276?

**Chris Gammell:** Uh, yes. So there's an official part. So, uh, at Mel, uh, software framework, so official support. But for that, unfortunately I have to use that no studio, which is windows based only. Mm-hmm . But there are lots of community support lately. People have ported it to a platform IO. There's also support for Arduino from Mexican guys, the electronic cats. They, they did a nice port. Oh yeah. Those guys are great. Yeah. They did a nice port and they ported it to Arduino and it also works with all the Laura

**LoRaWAN:** Van drivers and some of the device drivers. Oh, that's great. And then, I mean, so these things are out there, right? People are buying these on Tindy and using them in their projects and whatever. Yeah.

**Chris Gammell:** The electronic cats version, they also sell it directly from Rack wireless website. And you can buy it from there, but also there are lots of small makers, hardware makers like me, and they're selling it in Tindy and other sources. Mm-hmm .

**LoRaWAN:** Okay. So now you have something like the Pinguino Feather SAMR 34. It's a Laura based device. Mm-hmm . And you want to put that onto a Laura WAN device, like the Things Network, right? Just kind of trying to piece all this together, right? Mm-hmm . So you're getting from the chip to a module that you built. The module goes onto a board. The board works in a system. It's talking to a sensor maybe. You've getting a temperature, the temperature's boring. You're getting a air quality monitoring, a PMI from a Sensurion expensive ass little green brick. Yeah. And you're getting the readings back and you're getting PM 2.5 part particulate monitoring. Mm-hmm . And you want to pipe that back over Laura WAN now. How do you actually tie all that stuff together?

**Chris Gammell:** Yeah. So, on the device side, it's very easy. On your Things Network account, you basically create a new application and create a new device. You copy the device credentials to your sensors and basically flash it with those new credentials. And then you have a Laura WAN stack running on your device. You can read the sensors, sensor data and encapsulate it in the, let's say, a buffer of a transmission buffer and then send it over Laura WAN to your application. And on your TTN account, you will receive the data stream coming. You can implement a payload decoder on top of it because you have to compress the data and use only the important bits. Yeah. And let's say not send a double or integer. You can even make it a byte, a couple of bytes. And then...

**LoRaWAN:** So, no JSON with lots of overhead on these things? No.

**Chris Gammell:** No, no, no, no, no. With Laura WAN, the packet size is quite limited. So, there are a couple of spreading factors involved and based on the spreading factor, that decides how far your radio transmission would go and how much data you can transmit. At SF7, you can transmit up to 230 kilobytes or yes, 230 kilobytes, but very close range, let's say one or two kilometers, depending on your gateway. But at SF12, you can only transmit maybe 50 bytes only. And the data rate will be very slow, but the range can go to many, many kilometers. Like Andreas Spies, the guy with the Swiss accent, he did like a Laura WAN world record from very long distance. I think it was about 149 kilometers. Oh, my God. That's crazy. And last year in our conference, they did a, they installed that sensor node on a balloon, the helium balloon, and it was sending the data from above, I believe, 750 kilometers. Oh, my God. At SF12. So, it was on a line of sight. And if the weather condition is good, it can go really long distances.

**LoRaWAN:** That's great. Yeah, I guess 750 is straight up, huh? Yeah. Makes a little easier, you don't have to worry about the-

**Chris Gammell:** It was up and like, it was drifting. Oh, it was, okay. It was Eastern Europe. And it was received by somewhere in Germany, a gateway somewhere in Germany. Got it.

**LoRaWAN:** Yeah, right. So, that is the other benefit, yeah, is that you are, you might ping a different node. And also, that was another thing I remember from the network side of things is that a packet might hit multiple nodes, right? It's basically a broadcast from a tiny thing, and then all these receivers are like, hey, I got it, I got it, I got it. And then you could even, there's, is there triangulation with that yet or no?

**Chris Gammell:** They are working on it. I believe the new standard allows you to do the, like, the non-GPS, just a pure LoRaWAN-based triangulation. Basically, if your packet gets received by the many gateways, and the network server will decide which gateways data I'm going to use. Usually, it picks the one with the highest RSSI, which is the closest to the device. Mm-hmm. So that the device can also do automatic data rate adjustment. If the device is close to the gateway, there is no need to transmit at highest power available or at the, like, SF-12, you can go down to SF-7. And also, you can save down power, let's say, instead of 14 dBm, you send at 10 dBm or 8 dBm. Mm-hmm.

**LoRaWAN:** Got it, yeah. So you start to save battery, start to save. Yeah, exactly.

**Chris Gammell:** Yeah, right. With LoRa applications within the class A applications, it's all about saving the battery and extend the battery life. Yeah, right.

**LoRaWAN:** And then I've seen 10-year battery life kind of specs, you know, that's, right, that's, people always talk about 10 years, right?

**Chris Gammell:** Well, yeah, the battery will be dead long before the device itself. That's right, yeah. Yeah, you can, technically, you can achieve it if you do a careful design. Mm-hmm. And if you transfer maybe once a day or so, and then you can achieve that kind of long battery life. Yeah, that's cool.

**LoRaWAN:** That's really cool. So, okay, to go back to, so you said SF12, it might get a kilobyte or so of data. Yep. And then tens of kilometers, so that's kind of like the numbers that I wrote down? SF12, couple of bytes, let's say 50 bytes. A couple of bytes, okay, okay. Yes, it's very slow. Okay, got it. And then, so that's what I'm really wondering there. So you said 230 kilobytes for an SF7, a spreading factor 7. Yeah. So what, is it like a window? Like what determines that? Because you could just send another packet after that, but is it like a window within that packet range or what?

**Chris Gammell:** In Europe, there's this thing called a fair use policy. Ah. Okay, we are using the ISM band, but we cannot keep constantly sending the data. Okay. You have to somehow be polite and allow all the other users who are sharing the same bandwidth with you to have some bandwidth allocation. So there's this 1% rule, duty cycle rule, that once you send the packet, depending on your packet size, you have to wait. There's a certain dead time, let's say. Mm-hmm. That's a 1%. Let's say if you're sending a couple of packets every day and it amounts to, let's say, 36 seconds, and the rest of the time, 3,500 whatever seconds, you have to be sleeping. Mm-hmm. Okay. You can allow however you want. You can have a SF7, very small packet, sent once every hour, or you can send everything at once, use up all your bandwidth, and then sleep and wake up the next day.

**LoRaWAN:** Got it. So you take all the seconds in a day, you get 1% of those. Okay. And then the rest of the formula is just how much battery you want to spend on it. Mm-hmm. Okay. That's good. So from your experience now seeing, seeing devices in the field, both as a independent hardware maker and now someone making hardware for a network. Mm-hmm. What are most people doing?

**Chris Gammell:** It's mostly used in the industry and in agriculture and smart city. Uh-huh. Okay. It's very, the LoRaWAN or LoRa itself as a radio protocol, it's not like one protocol to use in every situation. It has its own niche application where the data is not changing very frequently, let's say temperature and humidity. Uh, like for the slow changing data over time, let's say once every hour. So you can use it or you can do the local logging and maybe even using like a tiny ML, do the machine learning and classification on the device. And then send the, the results as a event detected events once every hour.

**Chris Gammell:** You can do that for, let's say preventative maintenance and like a vibration monitoring on the board and, uh, even do a, like a, uh, energy harvesting from that vibration. So the device would extend its own battery battery life. Mm-hmm. Otherwise it's also being used in agriculture for like a crop soil temperature, humidity measurement. There's a popular project, Arduino based, uh, called Winduino. It's being used. Yeah.

**LoRaWAN:** I figured it was. Yeah. Yeah. Yeah. He was, uh, he did one of the early, uh, Hackaday prize. That's how I met him.

**Chris Gammell:** Exactly. Yeah. Yeah. That's one popular one. And, uh, there are lots of device makers. Now, if you go to our website, thingsindustries.com and there's a device marketplace, a lots of listed gateways and sensor nodes where you can basically, there are. Like dev board style devices also ready to use with the proper IP rating.

**LoRaWAN:** Yeah. That's great. That's great. I mean, and the agriculture thing makes sense too, because it's like, so having worked in the cellular industry and like people are like, oh, I'm going to have like a thing, you know, in every field, I'm going to have like a, you know, a cellular device there. It's like, well, okay. Make sure you have a tower nearby and also make sure you have a car battery nearby. Exactly. Yeah.

**Chris Gammell:** But people really don't want to, some people don't want to pay the subscription fee of the, for each, each sensor node. And the, the power consumption is really huge with the 3G or 2G modems. Yeah. And there's now a bit like MBIoT LTM, which is a bit more low power, but still. I was actually talking about those even. Yeah. Even those, they, they really can't compare with the lower van because you still have to wake up periodically and send the, let's say I'm alive signal to the tower. Right.

**LoRaWAN:** Unless you want to do a full refresh and then you have to like basically reprovision another, not IP address, but another connection to the tower. And yeah, it's a, it's a, yeah, it's, it's for very special use cases. Yes.

**Chris Gammell:** I mean, you, if you have some sort of, let's say solar based or vibration based energy harvesting where you can extract some energy and extend the battery life, then those could be useful as well because. Mm-hmm. Laura is not per, or perfect for all those applications. If you, if you just need IP based device where you can send UDP packets or TCP IP packets directly to your server, and you don't want to involve in like an intermediary gateway, things like that, then you can use MBIoT or LTM based device. Yeah. Yeah.

**LoRaWAN:** I think it is, it's a general good practice to like, to be, so if someone's like trying to be a solution provider across many, you know, remote data sensing type of things, have a bunch of tools in your tool belt, right? I was just talking to a friend about this the other day, you know, have a cellular device that you're comfortable with, have a Laura device you're comfortable with, have a wifi device you're comfortable with, right? If you're doing high bandwidth, you don't want to be on either of those things. Cause you don't want to pay for cellular. You don't want, Laura is not good for your high bandwidth. And it's just like, you need to have all of these things because there is no perfect thing there, you know?

**Chris Gammell:** Yeah. You don't want to lock yourself into one technology and just keep using it for every application. I believe it was Richard from TWTG that he was mentioning that he tried to use it for bicycle racing and to monitor the real time, real time like pedal pushing off the rider. But he was getting lots of delays because Laura was just wasn't the technology for this application. Yeah. He needs something with low latency and Laura cannot really provide that. Yeah.

**LoRaWAN:** I mean, do you find that people are doing like aggregation on device? So you said with, you know, spreading factor seven, you could do 230 kilobytes per packet. You could do one to two kilometers per thing. But do you find that people are like logging data, compressing it into like a table format and then just spitting that whole thing back?

**Chris Gammell:** Maybe it's not very, there are, there are several, there are several, let's say, byte encoding techniques that people use to condense the data into, let's say a single, or let's say four, four byte value into a single byte, even half the byte, a word like four byte, four bits word. And then you decode it on the, on your TTN account or whatever network server you're using. Because the bandwidth is very crucial and you're trying to condense the packet size as much as you want to reduce the airtime. That's the most power consuming part of the lower van doing the transmission in, let's say 14 dBm, depending on the module you're using or a radio chip you're using can go up to 60 milliamp. And in 22 dBm in us can go up to 150, 180 milliamps. Basically some batteries are not even able to provide that much instant current rush. You have to have lots of deep decoupling as well for the 22 dBm. Yep.

**LoRaWAN:** Yep. That makes sense. Okay, cool. Well, let's talk about your, the thing you've actually been building on behalf of the Things Industries and the Things Network. What, what are we looking at here? Once I pull it up.

**Chris Gammell:** So as, as I mentioned earlier, I was designing this open source, Penguino family of devices and Vincade, the CEO of the Things Industries, has seen some of my designs on LinkedIn and he contacted me and said, hey, we want to design something similar with more, let's say, ready to use everything enclosed in one nice enclosure and with a couple of sensors around. And do you want to come work for us? He said, yeah, why not? Sure. I'm not doing anything, you know, this week. Well, I was, I was, I was having a bit of a, let's say burnout at my car, a previous company. Ah, yeah. And it was already four years that I've been working there and I needed something new. And it was really the perfect fit for me to move to Amsterdam and start doing this cool project.

**LoRaWAN:** And so cool project, cool city, I mean, cool company, like, yeah, that's pretty ideal.

**Chris Gammell:** So yeah, everything fit together nicely. So, um, there was a generic node idea in the company and they started developing initial version with the summer 34, but, um, that project didn't took off. Like they had the early prototypes, but didn't took off. There was some hardware issues with it. And they, uh, at a time ST has released this new chip STM 32 W L. And, uh, we as a company have a really good relationship with ST. They are in, even though they didn't have custom chip for Laura, when they're being, they're being used in many of the Laura modules as a main microcontroller. Right. So it was a natural fit and, uh, they decided to help us a lot with the design phase and also supplying, uh, like early samples.

**LoRaWAN:** I feel like in a couple of years, there'll probably be no problems getting ST parts. Well, well, we'll see. We'll see about the chip shortages.

**Chris Gammell:** Such a, such a big company. Well, they do have a, you know, the ST has this longevity program. Yeah. And, some of the parts they promised that for the next 10 years, it will be available. Yeah. I believe this part is also one of them.

**LoRaWAN:** So we decided to use. So is that you could, I'm sorry. I keep making jokes about ST parts. Does that mean you could get them in 10 years or there'll still be available in 10 years?

**Chris Gammell:** Well, some of them you will get in five years if you order now. Oh man.

**LoRaWAN:** It's like, it's almost like gallows humor. It's like, if we don't laugh about it, we're going to cry. So there are two ways. Yeah. Right.

**Chris Gammell:** It's hard to, it's hard. Like you can laugh if you have nothing to do with it, but if you are in the business and you need those chips, that's terrible. It's terrible. You just have to cry. Yeah. So we decided to use this STM 30WL. It's a, it's a really nice chip. It's a, it's a first LoRa SoC, which integrates the LoRa transceiver inside the SoC. So, so this, so this is different than the, the, the, at some R34 or certain animal. Yeah.

**LoRaWAN:** Yeah. Microchip now microchip. Oh, now microchip part of previous that. That was actually a sip you said, right? So it had. That was a sip. So it was a different dye. Yeah.

**Chris Gammell:** Microcontroller and the transceiver was different dye, but this one combines everything into one dye. Right. More integration and smaller size.

**LoRaWAN:** So this is like ST basically licensed the design from Semtech, put it onto their chip, test it all together. It's one contiguous thing. Yeah. Great.

**Chris Gammell:** Exactly. And they have two versions of two main versions. One is a single core. The other one's dual core. We opted for the dual core version, which has Cortex M4 and M0 plus. Oh, cool. Yeah. And the single core version has just M4. Okay. Yeah. And then we decided what sensors to put on the sensor, on the node. What kind of interfaces should we have to make it a bit more developer friendly, have a standard pitch, 100 mil pin headers for programming and also expansion. Also have a quick connector if you want to add the I2C based devices to it. Yep. And have a, like a quite a wide range, a wide input voltage from two volts up to 5.5 volts with the JST connectors. So you can use lipo or lithium ion phosphate or two or three double A's or triple A's in series. So we, we decided to have this, all this flexibility to the user. And at the end, I was really rooting for it that to make it fully open source, all the hardware design files, schematics, PCB, BOM files, and including the SDK, we made it open source. And every, anybody who wants to look at the design, they can just, yeah, you use it as a reference design for their own or whoever. Yeah. Cause that's what you want, right?

**LoRaWAN:** You want more people building more thing. This is a generic node. Then you want people to go and build the specific nodes, right? Yeah. I mean, it's like a in between device.

**Chris Gammell:** It's both at the development board, but it is also a ready to use industrial and certified device.

**LoRaWAN:** Yeah.

**Chris Gammell:** It's going to be certified for now. It's going to be C certified for you only, but later on, we are going to do the FCC as well.

**LoRaWAN:** Got it. Yeah. As a general thing. I mean, do you see, I mean, I would imagine with the things in the industries being a Amsterdam based company, there's probably a lot of EU based interest, but do you see the split US and EU, I mean, or even other markets, China, Europa, not Europa, Australia, Asia, or whatever they call Oceana. That's it. I like Australia, New Zealand. Yeah.

**Chris Gammell:** Yeah. Actually, there are not much of a split because most of the people who are interested in using LoRaWAN.

**Chris Gammell:** Yeah. A lot of people who are interested in being a digital or industrial or industrial monitoring companies wants to retrofit their devices. Instead of like a wired connection, they want to use LoRaWAN as a, like, offer a wireless version of the sensors. Even like a big railroad companies in Europe are trying to use it now for like a platform monitoring, even like sync their clocks. They're using LoRaWAN for it. Like all across the whole country. They're like syncing the clocks within like a less than a second timing precision using LoRaWAN. I figured that would have been like a solved problem by now, but I guess not. Mostly it is mostly. Oh, well, depends.

**LoRaWAN:** I figured that you stick a GPS module on something like it's like network time from like satellites,

**Chris Gammell:** right?

**LoRaWAN:** Yeah. But they have to keep the cost low. If you add GPS to every clock then adds up quite significantly. Yeah.

**Chris Gammell:** True. Yeah. And then power hungry too, right? I mean, they thought it was. Also power hungry. Yes. But because the other idea is to, if there's a power outage, they can still operate the device remotely using a self-powered gateway or gateway with the UPS and the cellular connection, then it will be much easier to maintain the network. Yeah. So with our generic node, we basically use like a jelly bean parts of sensors, temperature humidity sensor, accelerometer. We have a really nice buck boost converter from Ricoh. It basically has a 300 nanoAms of quiescent current. Wow. So it can go really low. When I said that this is a both developer friendly and also industrial ready device. So it is designed to be low power. You can switch off power gating, all the sensors, even the expansion part. And in sleep mode, we've measured something around 1.7, like 1.8 microamps. Very nice. Putting the microcontroller in a stop mode 3. Yeah. And basically, I can show you the enclosure itself, how it looks. I have one as well, somewhere around here.

**LoRaWAN:** Unfortunately, everything's around here is still in boxes. Yes. But can you show it again? Sorry, I didn't have your videos large on the screen. Yeah, sorry. So that's the enclosure. Yeah, that's nice.

**Chris Gammell:** Basically, there's a user button here, RGB LED. A small opening here for the temperature humidity sensor right underneath the enclosure. Yep. So there's a hole, we've detected it covered with a waterproof mesh, which are typically used on the smartphones. It allows air, allows humidity to some degree, but prevents the water. So we can keep the IP65 rating. That's awesome. And the board itself is very small. Yeah, it's hard to see when it's huge on the screen.

**LoRaWAN:** So yeah, that's great that it's in your hand there. Yeah. Yeah, no, that's great.

**Chris Gammell:** It's 65 by 33 millimeters.

**LoRaWAN:** And then what is the battery size that fits in that case too?

**Chris Gammell:** In this case, we managed to fit in two AA's.

**LoRaWAN:** Two AA's. Oh, great. Okay. So at 1.8 microamps, theoretical max, if it was just sleeping the whole time, what would that get it?

**Chris Gammell:** If it's just sleeping, you would get more than 10 years. Oh, yeah. If it's just sending one packet of, let's say, 20, 25 bytes every hour, and you can get, expect three or four, maybe even five years of battery life. That's nice. We haven't done any long-term extended battery life testing. It's only been around for a year, not even. Yes. But we have a real nice partner, you know, Koitek? Oh, yeah. Yeah. Yeah. They have this OT mini power analyzer. Battery tester. Battery tester. And they are doing this extended battery life measurements, and hopefully next month we will be able to tell exactly how much it's going to be. Oh, that's good. But just rough estimation with the online IoT calculators, with the tools that I have behind me, measured. So it's definitely going to be like four years, five years with one uplink every hour.

**LoRaWAN:** Yeah. Once an hour. That's very impressive. Yeah. And then, so what's the spreading factor there then, too? Because that's, again, I don't really have a good, I'm sure that you've got this internalized at this point, right?

**Chris Gammell:** Yeah. Well, it's no problem. We've made everything open source. And we even discuss most of, many of the stuff in the GitHub issues as openly as possible. That's great. All the radio testing certification results. Oh, great. Initial pre-testing results. Like a power measurement results. If there are some bugs on the board, we also highlight it there, which will be addressed with the next revision. There are not any major issues with the board, only maybe like a labeling error in the first revision and then which one gets in the next revision. Yeah, that happens, you know. Yeah, that's why we have the revisions, you know. Yeah. It's an iterative process. Yeah.

**LoRaWAN:** That's great. That's great. And so tell me about the testing. So going through CE testing, what are the limits like for the ISN band stuff as well?

**Chris Gammell:** For Europe, the main limit is the output power of 14 dBm or 100 milliwatts. And another limitation is following the 1% fair policy usage, duty cycling. And also not to have any spurious emissions. So have them low under the certain limit. So they are doing this sweep while the device is running, doing continuous RF transmission. And then they're doing sweep of measurements from zero up to six gigahertz to find are there any, let's say, harmonics or spurious emissions from the device itself. We tried to shield the device and also use a four layer design, sand which all the high frequency lines in between and cover it with the ground plane.

**LoRaWAN:** And basically, you did internal, you did an internal layer, like, oh, interesting.

**Chris Gammell:** Internal tracks. So basically to keep everything. And it's my first board as like a commercial product and going through certification. But I'm really happy that it's still passing all the pretests and following all the, let's say, regulative limitations. That's great.

**LoRaWAN:** And then in terms of like the front end, is there like a, is there a preamp on there or like a power amplifier rather as well? Everything is built into the chip.

**Chris Gammell:** It has a PA and a PA boost. You can use it for 22 dBm, but it has a low power output and high power output. You are using for EU. We are, we have internal switch and you're using software switch. You're using a low power output with a maximum of 14 dBm. So there is no way you can transmit higher than that. That's nice. So if you're using a low power path, we are utilizing the high power path and that can go up to 22 dBm.

**LoRaWAN:** Huh. I wonder why it's different here. Any idea? Like why, why it's 22 here versus there? It's just population density in this, in the Midwest?

**Chris Gammell:** I guess it's density and the, the US is like huge and the distance because of the distances, you need more power. Yeah. I guess our farmers are further apart, huh? Exactly. Yeah.

**LoRaWAN:** That's interesting. Yeah. How that's part of it. Yeah.

**Chris Gammell:** Yeah. And unfortunately, so there are a couple of commercial available modules for the STM 32WL, but they are using the high power path by default. You have to have lots of, let's say, RF matching network balloon function on your PCB. So, so that you can utilize both RF paths, but they are using just default high power path in their modules. And the difference between low power and high power is the power consumption. So in high power, if you trans decide to transmit at 14 dBm, that's going to end up consuming about twice more current than you do the transmission at 14 dBm with the low power output. Interesting. Yeah.

**LoRaWAN:** Just because of a logarithmic nature of it? There are different circuits built in. Oh, different circuit.

**Chris Gammell:** Okay. Yeah. Yeah. It's like a sub modules inside the radio transceiver. One is dedicated for low power path output. The other one is for the high power path output. Got it. And high power is by design, it consumes more power. Yeah.

**LoRaWAN:** Hmm. So you only get two years instead of four. Yes.

**Chris Gammell:** Well, yeah, unfortunately, that is the case. But when in our generic node, we decide to use both paths, so that with the, with the sacrifice of extra bomb parts on it, about 15 more passive components, let's say inductors and capacitors, plus an RF switch to switch in between low power path and high power path. But I think, yeah, that's going to be a more, let's say, it was a user centric design decision. Sure. That gives them more flexibility. If they want to save power, yeah, use a low power path, even for US. Got it. Yeah.

**LoRaWAN:** Well, on the, when people make their own specific node, they can rip off the high power path if they don't need it, right? Yep.

**Chris Gammell:** Exactly.

**LoRaWAN:** What are, what kind of costs are we talking about here? What does it cost to buy one, to buy one of these? So if I was going to go buy one, what does it cost?

**Chris Gammell:** Well, right now we've did, we did the low production volume of first phase, we did 100. And we, we sold it. We basically gave away most of them for free. In the next run, we are doing 500 and that's going to be about 70 bucks. But because of that low volume, the initial cost is really high. But in the next phase, we are doing this higher volume, let's say 5,000 or even 10,000 nodes. Then, then the MSRP we are planning is going to be around 40 bucks. So that's great. We are trying to go as low as possible and not make too much money out of it. I mean, sometimes not at all. Yeah.

**LoRaWAN:** I mean, I would think if it's the, you know, the things industries is making their money on the software piece. This is almost like a loss, not a loss leader, but like a, this is the thing to get people through the door. Right. I'm in a very similar scenario. Exactly. Where the hardware is a enticement into like being part of a larger ecosystem. Exactly.

**Chris Gammell:** Like to onboard the customer to the ecosystem and give them a easy to use tool and which, which is also like an industrial ready to use device. Yeah. And which delivers what it promises so that they can use our services and software services on top of it.

**LoRaWAN:** Yeah. I think the hard part is when, when a software company comes in and they don't quite understand hardware and they're like, I would like to buy 50,000 of these so I could put them in the field, please. You're like, nah, we had those. Yeah. That's not how this works. You guys, this is a development platform. Like this is not, but I mean, that's the thing. It looks like it could, I mean, it could operate in that way. And people are like, well, here's a solution. Why can't I just buy this solution? I can go to Amazon and buy a blank. Right.

**Chris Gammell:** Yeah. We are also planning to like license it and make a, like a custom version of the generic node, use a bare bone, use the SDK and use all our drivers and ecosystem because we are in our SDK, we are trying to make it as friendly as possible for the developers. So we have Azure RTOS, even like a thread X version. We will have a, Arduino support embed support and a bare metal of course, and a free RTOS version. Basically like all the popular choices there will be supported in, in this platform in our SDK.

**LoRaWAN:** Cool. And you said Azure RTOS that was thread X. They bought. That was thread X. Yeah. That was the thing. All these, you know, all these cloud providers are buying, are buying Amazon bought free RTOS. Yeah. Yeah. Azure bought, Microsoft bought thread X and, you know,

**Chris Gammell:** Well, it's, it's the same in hardware world. Like all the companies get bought by a bigger one. Let's say I recently was, Maxim was acquired by VDA, analog devices. Analog devices.

**LoRaWAN:** Yeah. Another one bites the dust guys. Yes, exactly. Yeah. It's, it's, it's, it's. At the end we will have like one big corporation, which is called like, like, a V semiconductor. Right. Chip, chip company. The chip company. Yeah. You buy your, you buy your parts from chip company. You send your data to data company. And then eventually data company buys chip company. And we just throw up our hands. We're like, all right, well, I guess I'm going to go flip burgers now. I don't know. Exactly. What the hell do I do anymore? But yeah. For now we can sit around and wait for STM 32s to come available. Sorry. Last time I'll make that joke. I'm sorry.

**Chris Gammell:** Okay. Okay. Yeah.

**LoRaWAN:** Just five, five more years. It's, it's really painful. I assume if you guys have a partnership, at least you're at least, you know, on the list of like people getting parts before schlubs like myself. So.

**Chris Gammell:** We do, we do, but it's still, it's not easy peasy.

**LoRaWAN:** Yeah. You're not, well, you're not Apple. You're not, you know, you're not Microsoft or anyone who's making big things. So.

**Chris Gammell:** Yes, exactly. Yeah. For those it's right now, it's a bit hard. Yeah. Recently.

**LoRaWAN:** I mean, yeah. Toyota, right? They can't get parts.

**Chris Gammell:** It's like, okay. They're cutting down the like a auto sale for about 40%, I believe. Yeah. It's really hard. Yeah. Like even like a company like Toyota, they were like a super conservative about buying the parts. That's right. Like for the chips and now they're out of stock. Yeah.

**LoRaWAN:** It's a tough time. It's a, it's, it's, it is tough. It's a good time to be in software.

**Chris Gammell:** Yeah. In our production. So we are right now having a delay a bit about the, all the chips are no problem. We found them. We sourced them, but the enclosure. Man. The raw material for plastic that is also running out and we are being delayed for that as well.

**LoRaWAN:** Right. Well, what if you just like shellac the whole thing and then stick the PCB out in the field, you know, just dangling wires with two double A's and the.

**Chris Gammell:** And, uh, you know, well, that could work as a dev board that could work.

**LoRaWAN:** You know, like, uh, make, make, make the farm look like the server farm, right? You know, like server farms, they got rid of all the cases. It's just bare boards and racks basically. And they're just cooling. And, you know, cause it's so, so much scale. So now we just do that in the fields for agriculture and boom, we're done. You know, just, you need to really just. Yeah.

**Chris Gammell:** Conformally coat the device so that it would.

**LoRaWAN:** Conformally coat the crap out of it. And then you're done. Yeah.

**Chris Gammell:** The problem is, uh, is, is the antenna. Yeah. So we tune the device, including the enclosure, including the battery holder PCB, which is a secondary PCB. And if you remove the enclosure from the equation, the whole, uh, like a resonant frequency of the antenna shifts quite drastically and it starts to perform very poorly. So it has to have that enclosure.

**LoRaWAN:** And it, because it'd be shitting because you tuned it to that, you put, you changed out inductors, capacitors, whatever needed.

**Chris Gammell:** So the, the matching network was tuned, including the enclosure, including the batteries, like alkaline batteries altogether. Yeah.

**LoRaWAN:** It's one piece. Huh? How much, how much was that process when you were doing that? Was it like you're on the bench of swapping out components or what were you doing there?

**Chris Gammell:** Practice antennas. Yep. So it was part of our partnership, but that's what's going on. That's what basically they are doing. They are first doing the simulating, simulation, and then getting the suggested part values for the, for the matching network. And then on the real bench, they're just basically soldering, disoldering inductors and capacitors until they hit the sweet spot.

**LoRaWAN:** Yeah.

**Chris Gammell:** Yeah. Which is interesting because in their early simulation, because this is very tight design and the two double A's are really close to the antenna. They were really worried that, okay, the antenna will perform poorly. But in the, in the actual device, it turned out that the antenna performance is actually not that bad. It's actually very good. That's great. Given the, the proximity of the battery. It's actually because in, in their technology, they call it a virtual antenna technology and they're using ground plane to emit. Yep. Because battery is also one of them, at least is part of the ground plane. The, the, it extends the size and actually helps with the emissions.

**LoRaWAN:** That's super cool. Yeah. So if you, so actually that's an interesting point then too. So if you switched it, so you said using the two millimeter JST plug, you could switch out for a, like a lipo or something.

**Chris Gammell:** Yeah. Any, any type of battery, which can deliver, let's say more than 200 milliamps. Uh huh.

**LoRaWAN:** And, uh, which, that would then change the ground plane as well. Right. Yes. Not necessarily worse, but it would definitely change it because it's just a different shape and a different, you know, chemistry internally. Most definitely. I mean, it would have to be retuned again. Yeah. Yeah. That's great. Yeah. Well, that is, that is really cool. I mean, so, uh, what's the timeline on the, you said the, the two different builds, you said the $40 build will be hopefully 5,000 to 10,000 units. What's like rough timeline.

**Chris Gammell:** That is planned for next year. Uh huh. That's planned for next year because we will definitely get bit by this component shortages. Yeah. Yeah. Of course, even with this 500 run, it's not too much of a component, but we still, had to wait a couple of months to get those parts. Totally. And we are planning to start delivering the first nodes next month, hopefully. And if everything goes well, we also planning to hold a small virtual conference dedicated for the generic node sometime in October or November. We had to postpone it. Actually, we were planning for September, but yeah, we have to wait for the enclosures, unfortunately.

**LoRaWAN:** Well, that happens. Yeah. And you guys have other conferences. I keep getting emails about other conferences. So things network does, or things industries, things networks.

**Chris Gammell:** We have one super big conference, which is every year annually in January, end of January in Amsterdam, which is mostly physical event. So it's a little event, but last year due to COVID, we had to make it online. But this year we are planning to make it more like a hybrid conference. Yeah. Partially for those people who are not able to travel, for them, there will be definitely an online part, also a physical part in Amsterdam. But all across the year, we also have a small virtual conferences dedicated for one part of LoRaWAN. Let's say one was about the ThinkStack. The other one was about like using LoRaWAN in logistics applications, in maritime applications. Another one will be hopefully about the generic node itself. Cool. And yeah, we also have having like a local conferences, the pre-COVID times. We had one in India. After the COVID, maybe we'll do more of those as well, like a smaller version of the Thinks conference.

**LoRaWAN:** Great. Well, do one in North Carolina, man. There's still farmers here, apparently. I don't know.

**Chris Gammell:** Well, that could be a nice option for us. Yeah. Yeah.

**LoRaWAN:** That's great. That's great. And I think that, you know, people should definitely check this out. I'm really excited to, like I said, I have mine. It's, I got mine, one of the early ones. It's somewhere in the stuff that's off camera here.

**Chris Gammell:** Yeah. Of course, you started doing lots of firmware development. Maybe you can try to use our SDK. Yeah. Yeah. Just do a recursive pull from our GitHub, and then you'll have everything ready to go. Just, we are using CMake and ARM GNU tools. So just install those and you'll be good to go. And we have options to use like Docker, even VS Code based, and also support for the STM32 cube IDE. So you can import our project to the cube IDE itself.

**LoRaWAN:** That's cool. Yeah. I mean, that's what Philip was on the show talking about last week or two weeks ago, depending when this episode goes out. And yeah, kind of like those build systems that just kind of getting stuff really kind of instrumented and built up from the command line. And yeah, it sounds like it's a good starting place.

**Chris Gammell:** Exactly. Yeah. You can even use our SDK to develop for other sorts of STM32WL devices. Ah, cool. Because it's very similar to the official nuclear board from ST. All the pinouts are the same for the RF part. And you just have to change some of the I2C ports or UART ports, but RF part stays the same and pinouts are the same. It is compatible. That's great.

**LoRaWAN:** Yeah. Yeah. How was it, I mean, pulling that in, I mean, you said there's a nuclear board. I mean, those are really great starting points. I think that's a strong point of the ST ecosystem, rather, in terms of like the one thing with ST parts, it's always like the clock management always kind of felt weird to me. Like the, you have to kind of like, it's like very chained along. You have to make sure that this one's turned on and this one and then this one and this one. If any of them are not, you're just like, well, it's not doing anything.

**Chris Gammell:** Like, oh yeah. Well, it's in general, it's an ARM thing because of the high speed bus, low speed bus, all the peripherals gets a different clock source. And especially if you have, if you are using the internal clock source and then you have to enable PLLs to get higher clock frequency. In this one, we are using for precise timing or using TCXO for the radio. And you can get those? Well, yeah, that was also one of the hard part to get. I've heard, no, I've heard specifically with those. Yeah, yeah, they're hard to find. Last year actually, there was a big fire in China and what's that like that. Yeah, right, right. That was a huge hit. Yep. We had to change a part that we are using to different one because of that. Yeah.

**LoRaWAN:** Cool. Well, Orkin, where can people find you online? I mean, I think following your Twitter is a lot of fun. So where can people find you on Twitter and otherwise? Well, I'm mostly on Twitter.

**Chris Gammell:** You can find me with the tag name Aziri Maker. I'll be there and you can also message me there. And otherwise, I have like a blog where I post about my tanguino boards. It's called makertronica.com. And yeah, over there, I also have contact details. So feel free to contact me with whatever questions about LoRa or about the boards, open source designs I made. Also on GitHub. Yeah. Great.

**LoRaWAN:** That's awesome. Well, thanks so much for joining us here. Tell us about the generic. No, this thing is very exciting and I'm excited to try out more LoRa and LoRa Wayne stuff. I think it's going to be a, it's a, it's a lot of fun things that are out there, especially for low power, broad sensor networks. There's a lot of, a lot of need for that.

**Chris Gammell:** Yeah, definitely. And thanks, Chris. Thanks for having me. It's an honor to be here. I've been a long time listener of this show and yeah, it's really, it was great to be here. Thanks. All right. Thanks Chris. Have a good day.

**Speaker ?:** We'll see you next time.
