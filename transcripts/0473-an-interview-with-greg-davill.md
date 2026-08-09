---
episode: 473
title: An Interview with Greg Davill
url: https://theamphour.com/473-an-interview-with-greg-davill/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released January 5th, 2020. Episode 473. An interview with Greg Dabble. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. And I'm Greg Dabble from Twitter.

**Icebreaker FPGA:** Hey, Greg. How are you doing? That's where everybody knows me from, so it's probably the easiest way to describe what I do.

**Chris Gammell:** They know you from Twitter. Yeah, that's true. Happy New Year, I suppose. We're the first 2020 episode here.

**Icebreaker FPGA:** Yeah, Happy New Year.

**Chris Gammell:** Happy Holidays. Yeah, same, same. Give us a little background. So if people aren't on Twitter, some people are on Twitter, but if some people aren't on Twitter, what is your background?

**Icebreaker FPGA:** I'm just an electronics hobbyist. So just have fun electronics projects that I do in my spare time. Electronics engineer by trade. And so at my day job, sometimes I don't get to do all the fun stuff that I want to do. So when I come home, I just design boards, you know, do surface mount assembly and take photos. That's good.

**Chris Gammell:** That's good. And so we've had you on the show once before, very briefly at Kaicon. So you traveled from Adelaide where you live up to Kaicon in Chicago. So that was great. And people can go and listen to that. I think, I don't remember the episode, maybe like 430.2. It was the second episode of the Kaicon series. I know that. But people can go and listen to that if they are interested. And yeah, I mean, obviously you have a lot of great photography and boards that you work on. What is your most recent project?

**Icebreaker FPGA:** Well, the most recent actual board that I've built is probably one that I've called the Arctic Koala, which is a board that breaks out the new Lattice Crosslink NX FPGA. So Lattice announced this FPGA on December 10th. And they had engineering samples available to purchase from DigiKey. So I managed to design up a board and have it ready December 18th, if I recall. Yeah. Yeah. And I took that board to 36C3 Congress last year.

**Chris Gammell:** At the end of last year. Right, right, right. Well, and we'll definitely get to that. I definitely want to hear about that as well. So this is a new part from Lattice. Is it different than the ICE 40 family or it's the same family?

**Icebreaker FPGA:** No, so the ICE 40 is their ultra low power FPGA. Then they have their Crosslink series is more for media processing, like video streams and camera streams. It's very marketed towards the mobile phone kind of camera industry, it feels. And then they have the ECP5 line as well.

**Chris Gammell:** What delineates the two? What delineates between like a ECP5, which is like a higher end type of thing, and a video processing one? Does it have like different like front ends or something like that?

**Icebreaker FPGA:** The video processing specifically has some more hard-coded IO blocks for dealing with MIPI camera streams. So the MIPI standard has CSI and DSI, camera stream interface, and I think it's camera serial interface and display serial interface. And they're used a lot in mobile phones, but cameras and displays. It's like a low pin count, high speed serial interface. In terms of the actual FPGA fabric itself, the Crosslink NX series is pretty similar in performance to the ECP5 side of things, compared to the ICE 40, which is low power, lowish performance.

**Chris Gammell:** And so is this possible to use this with the open tools like LightX and MyGen and all of the IOSIS and the synthesis tools?

**Icebreaker FPGA:** Not at this stage, but the part was only released less than a month ago. Okay, okay. It's a work in progress. I think Dave Shah's taking a look at the NX parts that he has. And I think from a surface level, it's very similar architecturally to the ECP5. So hopefully we'll see some movement on that this year.

**Chris Gammell:** I'm surprised actually that they would have like a mobile phone kind of like targeted one. Do you know that like the market segment there, I mean, are they actually going for mobile phones with FPGAs in them?

**Icebreaker FPGA:** I'm not sure the exact market segment, but I mean, if you look at every new phone that comes out, they just seem to be incrementing the model number and adding a new camera to the back. So it seems like it's a reasonable market to go for because every phone now, you know, what differentiates last year's from this year's, you know, maybe there's another lens on there and it gives you some more fancy camera features.

**Chris Gammell:** Yeah, I guess you could do that until you have custom silicon and you want to like take a, you know, lower cost thing to market, that kind of thing.

**Icebreaker FPGA:** Yeah. And I think mobile phones, they're high volume products, but they're also a fairly short development cycle. Yeah. Right. I mean, they need a new phone every year to ring out. Yeah. Yeah.

**Chris Gammell:** So what does that look like then on boot? Like, so, okay, so you have Archie Koala, you've got it done in eight days, which is, yeah, that's something.

**Icebreaker FPGA:** There was a few board errata issues, but nothing I couldn't deal with. Okay. Just some rework for some.

**Chris Gammell:** Well, I mean, guess what else is on there too? Is this like a breakout or what else is on the actual board?

**Icebreaker FPGA:** Yeah. So I kept it simple. Are you familiar with the Icebreaker FPGA board from Peter Espin? Yep. Yep. Yep. So that was targeting the Ice40, but it's got the programmer in all in one. So programmer memory, FPGA, just breaks out to some, they're called PMOD connectors. It's a standard from Digilent. So it's just eight IO pins and power and ground.

**Chris Gammell:** Yeah. I feel like the standard is kind of a loose, it's a loose term on PMOD. It's like, you know, it's a bundling of outputs. Yeah.

**Icebreaker FPGA:** It's a standard connector format, not necessarily which pins do what, but that's ideal for FPGAs.

**Chris Gammell:** You need to have power and ground, right? I mean, I guess on the Supercon badge, it was not, I think it was backwards, right? On the Supercon badge. That's pretty much the only thing that needs to be right. So yeah, if you get that, you're good.

**Icebreaker FPGA:** You're good. Yeah. Yeah. You can't, unfortunately, you can't reconfigure power and ground quite as easily as you can with our opens. No, 2020, man. That's the new thing, you know? So basically I've taken the form factor of the Icebreaker board and just, that's an open source hardware board. So I've just taken the designs of that, cut the Ice40 FPGA out and dropped in the new Crosslink NX part.

**Chris Gammell:** Yeah. That's good because it's a familiar form factor and people will be able to get up and running quickly with it. That kind of thing. Are you using the, are you trying out the actual Lattice tool chain as well?

**Icebreaker FPGA:** Yeah. Yeah. That's right now the only way to program them with a tool chain they called Radiant. What's it like? I mean, it's like any vendor tool chain. It's a little bit more modern. I think this is a rework of what they had before, which was Diamond. So they're using both tool, like they kind of have two tool chains right now. Radiant targets the, all the Ice40 parts and these new Crosslink parts. And Diamond is for the ECP5 range and some of their older legacy products.

**Chris Gammell:** Honestly, I wouldn't have ever used Lattice if it wasn't for the EOSIS stuff or, you know, the whole, all the tool chains that are out there, Project Ice Storm and all that stuff. So yeah, it's good. It's good that, I guess they get exposure from the open tool chain thing and, you know, with the new Crosslink chip gets it too. That'll be good. Hmm. What is the, so, so have you, you've been able to play with the, the Nippy CSI, DSI stuff? A little bit.

**Icebreaker FPGA:** Unfortunately, I haven't had much spare time to play around with some of that stuff in recent weeks. Yeah. But the, the board, like the board's built now and I've got a breakout board for a little iPod display that I'll be playing around with as time permits.

**Chris Gammell:** Well, so you had also shared recently on, on Twitter about the Supercon badge hack that you did when you got back from the conference. Ah, yes. You had taken a camera you had. Well, why don't you just tell us what it is?

**Icebreaker FPGA:** So I had an idea to, so this all stems from your SAO that you made for, was it DEFCON 2016?

**Chris Gammell:** Yeah.

**Icebreaker FPGA:** 2017. 2017. Yeah. Um, so if anybody's unfamiliar, you made the, the not a camera, the NAC board, um, and it was a 555 project. Is that right?

**Chris Gammell:** Yeah. Yeah. Yeah. To be honest, initially it was supposed to be, um, it was going to say not a camera. And I was like, oh, I was like very ambitious. And I was like, I'll put like a Laura board or a, you know, module on the back or something similarly. And then it turned into like, well, I ran out of time and yeah.

**Icebreaker FPGA:** Yeah. So, so as, as things go, you've got the 555 and then you sold them on Tindy as a bit of a getting started with soldering kit. Right.

**Chris Gammell:** Yep. And I have videos too, about, uh, how to, how to go and do the layout as well. And, you know, my usual, my usual shtick.

**Icebreaker FPGA:** Yeah. Yeah. No, it's really, it's really cool. So you plug it in and the 555 links to a little red led on the front and the board is cut out and shaped like a security camera, but it says not a camera on the side and there's a little red led that's blinking.

**Chris Gammell:** Yeah. It was meant to be, um, Marcel Duchamp. No, not Marcel. Uh, what was his name? Well, the guy who, uh, who did, uh, um, this is not a pipe. It's a, it's a piece of art that anyways, it's silly.

**Icebreaker FPGA:** Yeah. I was, I wasn't aware of that, but so basically I took your board designs, which are up on GitHub. Uh, and as soon as I found out the new Hackaday Supercon badge was going to be FPGA driven, I knew that I'd have the hardware behind it to actually turn it into a real camera. Um, so I, I took a little camera module I'd been using, uh, you can set it up for one bit mode. So essentially the camera outputs a data stream over a single bit. So you send it a clock and it will send back a data value, a frame sync and a line sync pulse. And then the FPGA can interpret all these signals and reconstruct the image. And so this camera plugs into your normal SAO port on the, uh, Supercon badge, which on the, on the Supercon badge actually has an extra two IO pins, which were really helpful. Right. Yep. Um, and then all of this feeds back into the FPGA and just displays the image, the camera stream on the LCD of the badge in glorious, uh, 320 by 320 pixels.

**Chris Gammell:** That's right. Yeah. The, uh, the, uh, the 19, 1980s display, 1990s display. Um, I think it's a good, I think it's a good, uh, a really good example though of the flexibility, right? So you have these two pins, you know, you're trying to do more with less in terms of, you know, pin out and, uh, you're able to, to push that data through those, you know, that, that constrained interface. I mean, that's a very common use case for an FPGA, whereas people are, you know, usually have trouble kind of visualizing what an FPGA is used for.

**Icebreaker FPGA:** Yeah. I mean, FPGA is Excel in, um, video processing and, you know, camera stream, like any kind of parallel stream kind of interface they Excel at.

**Chris Gammell:** Yeah. I always think data, data flow and yeah. Streaming type stuff like that. Yeah. Hmm. So internal, internal on the FPGA then. So what does that, what does that look like? Um, so, so you had to basically translate this one bit output. Um, you said the FPGA was sending a clock out or a bit out and then the camera was sending the, the, the serialized bit stream back.

**Icebreaker FPGA:** Yeah. So in order to keep everything, uh, synchronous logic, um, I provide the clock to the camera and it then like, basically it acts like a shift register back out to the FPGA. Um, and I'm using some Verilog code by that David Williams wrote. So he made a cartridge for his Supercom badge that had a camera on it. And so he's already written some of the low level LCD frame buffer kind of logic. And then I've replaced it with the, the front end for the camera interface I'm using.

**Chris Gammell:** So like when you send a clock to a little, a little camera like that, so you're sending a clock out to it, it's shifting back just a bit stream. How do you tell it? How big is it? Like the camera is limited in terms of how much it has anyways. It's like a, what a two megapixel camera or something like that.

**Icebreaker FPGA:** Um, yeah. So it's, uh, 320 by 320 pixels. Um, so it's, uh, less than two megapixels. It's, uh, I don't know what that is point. Is it 0.3, 0.6 megapixels or something? Okay. Um, quite a small, small image, but essentially you just provided a clock, a free running clock. So there's always a clock signal, uh, at the camera and then it has its own internal frame timing mechanisms. Um, and so basically it'll start spitting out data and then between frames, there'll be like a blanking period, but it activates like the frame valid signal. And, uh, so it's like V sync and H sync basically there's like a line valid and a frame valid signal. And then there's also another interface to the camera, which is over I2C, which is how you set its configuration inside the camera. So it has, it has a few modes. You can crop the image to 320 by 240 and you can adjust, um, bit output timings and you can switch it from one bit to eight bit mode, uh, which was what I was having trouble with at Supercon. I couldn't quite get that step to work. Turns out you have to also have the clock divider set to eight in order for it to enable that kind of eight bit shift register internally as well. A lot of these cameras, data sheet isn't particularly, how should I say? Loquacious. Doesn't document the part very well. Basically they expect you that if you have problems, you're a high enough volume customer to just be talking to a applications engineer directly. The data sheet is, is, is transmitted verbally. Yeah. Um, unfortunately I don't have a sales rep or an applications engineer at this company to, to talk to. Yeah.

**Chris Gammell:** Uh, you know, I, I, um, I was talking to a large distributor recently and, uh, I brought up that exact same point that like, I know that this is not a problem for all of them and probably not even a problem for people that they really care about. Like, you know, large distributors care about large companies and I get it, but you know, I think that over time, large companies, you know, I think that there's more, it could be perception bias, right? Because I obviously am a solo person. You, you are the one person that's doing department at your company. You work at as well. So like, you know, I know a lot of people that do similar things, but I have to imagine that like, you know, big monolithic companies, there are fewer of them. There's a longer tail than there used to be. And, um, you know, having, having other resources for blokes like us, you know, and it's just like, it seems like there would be more of a, a push for it. And so that's what I was pushing for. Hmm.

**Icebreaker FPGA:** Yeah. I don't know why, I mean, I do know why that they don't provide some of these, you know, resources. I guess it feels like more of a support burden on their end.

**Chris Gammell:** Yeah. Right. Everybody's trying to push down the bottom line. So that makes sense from that perspective, but still it sucks for us. Yeah.

**Icebreaker FPGA:** Yeah.

**Chris Gammell:** But at the same time, you know, you're not exactly using like, I'm guessing this camera module was not particularly high to high end either being 320 by 320.

**Icebreaker FPGA:** No, I think, um, it's targeted as a low power, uh, low power sensor for, uh, an edge device in machine learning applications. I think that's what it's actually targeted.

**Chris Gammell:** Oh, okay. So like the one that's on that, uh, ESP 32 processing board or whatever those ones that are out there, they're like all the ones coming out. Yeah.

**Icebreaker FPGA:** I think it might actually be the same camera sensor inside, but it's a different, um, flex cable between them.

**Chris Gammell:** Well, still, it's very, I mean, very clever hack. I definitely liked it. Um, so what did, what did it look like internally? Were you, were you using like the MyGen tools and, and similar stuff internally? Uh, no.

**Icebreaker FPGA:** So just, just pure Verilog. Like I mentioned, it was, uh, some code from David Williams that actually did the LCD driving. So he'd written basically an LCD driver directly. So you take out the, the SOC, the system on chip core that basically was, had the, the dual core risk five processor and, uh, the pick inside that Sprite had written and put in some pure Verilog that basically just takes the camera stream and then outputs it directly to the camera. So there's no CPU in the loop at all.

**Chris Gammell:** So it's just, yeah, it's just, uh, just chucking, chucking frames on screen.

**Icebreaker FPGA:** Yeah. Basically just manipulating a pixel stream. Yeah. Which, which unfortunately wouldn't have made a very good demo because it now means the HDMI doesn't do anything because the HDMI was directly driven with the frame buffer interface from the SOC. So, uh, even if I'd got it working at Supercon in this configuration, it wouldn't have looked very good as, as a demo on screen because, well, firstly, the camera's not very good in low light. And so in that dark hole during the closing ceremony, it wouldn't have really picked up much. Um, and then I can't use the HDMI. So they, you'd have to be looking at the screen, uh, which is also problematic. Yeah.

**Chris Gammell:** I mean, it's crazy. Like how much the, how much, you know, video is so normal these days, you know, we see it in everything and yet the amount of processing it takes and everything that's kind of behind it, you know, at least I take for granted. Um, but it's still, it's still, uh, pretty impressive stuff.

**Icebreaker FPGA:** Yeah. There's a lot your, uh, your phone camera does to process that image, to make it look, uh, look nice that you don't really think about.

**Chris Gammell:** Well, uh, so you mentioned Supercon. Obviously we were hanging out at Supercon. You've, uh, you were at KiCon this year and you also mentioned you were at, uh, Chaos Congress. Uh, that's a, that's a lot of travel coming from Adelaide, Australia. Um, but how was, how was Congress this year?

**Icebreaker FPGA:** It was my first time actually. And it's, I still don't really know how to describe it. It's a big, uh, big gathering of German and European hackers, I guess. You went to, you went to Chaos Camp.

**Chris Gammell:** That's right. Yeah. So I was at Chaos Camp in Berlin in April, um, or sorry, in August. And, uh, and it's a lot of the same crowd, but it's a lot smaller actually. So camp is, I think five to six, maybe five to 7,000 people. I'm not sure what the exact numbers are. And then Congress is like about 30,000 people or something like that. I think it's, uh, about 20. Okay. Yeah.

**Icebreaker FPGA:** But still, I mean, that's, uh, it's a lot of people. Yeah, definitely. Definitely.

**Chris Gammell:** So how was the mix then? I mean, so you've, you've been to many of the same conferences I have. Did you meet like a new, a new crowd there or was it, uh, actual hackers, software type

**Icebreaker FPGA:** people or what? Um, yeah, I mean, lots of the same crowd. I, I, I mostly fit around circles of hardware hacking. So there was plenty of crossover between all three events actually, you know, uh, met a, met a few new people that didn't want to make it to the U S for super con. Right. Yeah. Which is fair enough.

**Chris Gammell:** Okay. So what is the, I mean, did you do talks and stuff too, or was it mostly, uh, mostly just kind of the social trading of tips and tricks?

**Icebreaker FPGA:** Yeah. For me, it was just, uh, the social meeting people talking about their projects and, uh, seeing kind of, uh, what people are working on, I guess.

**Chris Gammell:** What is, so, I mean, you're, you're in our ad hoc correspondent here. So, so what'd you see, what'd you see that's different?

**Icebreaker FPGA:** Uh, so we're definitely, they, everybody loves their addressable LEDs. Yes. Um, so I, I brought my icosahedron, um, my led clad icosahedron, or you can call it a D20, 20 sided polyhedra. Uh, everybody seemed to love that. And there was three other people that had made LED cubes and other, and another guy that had made an LED geodesic polyhedra. So it's a much more spherical. Uh-huh. Uh, that was really interesting.

**Chris Gammell:** Oh, uh, yeah. So that looks like a, yeah, I saw that when it was like a lot of tiny panel, like tiny triangular panels, like a geodesic dome, like you're saying, right? What were the specs? Like how many, how many sides were that?

**Icebreaker FPGA:** Uh, yeah, I'm trying to run off memory here. I don't know if I can remember how many sides it was, but it was each side only has one pixel behind it. Uh, so it lights up the whole area with one, um, WS2812 kind of style LED on the inside. And it's an entirely 3D printed frame and it's about the size of a soccer ball. So yeah, definitely a good size, huh? And then of course there was, um, plenty of, uh, plenty of badge, you know, badge enthusiasts there and seems like badges and add-ons are, uh, not going away anytime soon.

**Chris Gammell:** We haven't, we haven't jumped the proverbial badge shark. No, not yet. Okay. Well, we'll get there. I'm sure we will. Let's talk about your, uh, iso, how do you say it? Isoquahedron? Uh, icosahedron. Icosahedron. Okay. Icosahedron. So, so what, what is it and, and how, how is it constructed?

**Icebreaker FPGA:** Uh, so that was a project I created initially just to, after I'd created a, uh, my LED cube, which is about Rubik's cube sized, basically LED panels on every side. I thought, how can we make this more interesting? Cubes are, cubes are nice, but there are other polyhedra. So the nice thing about the icosahedron is every side is triangular. So it's basically 20 triangles, um, create this, this polyhedra. So it means you get by with less circuit board design, basically. It means I only have to design one triangular LED matrix panel, and then I could just make 20 of them and I'll have myself an icosahedron. Nice. So this is a project born out of laziness I'm hearing. Well, not quite. I'm just, yeah. I mean, uh, optimizing the problem. There's other shapes you could make, but they, some of them would require pentagons and octagons and, you know, different sizes. So basically decided on the icosahedron, had to work out how to model an icosahedron in Fusion 360, uh, which is a bit of a non-trivial task. I ended up watching a YouTube video that, that walked through and basically followed exactly the steps that this guy took. Um, and once I had a model, I worked out what size panels I'd need for an object about the size of a tennis ball was what I was going for. Uh-huh. Um, and so what that ended up being is 20 circuit boards with 120 LEDs on each of them. Uh, and then some LED drivers on the back. Uh, and then the drivers are constructed in a shift register format. And so the 20 panels, uh, essentially a daisy chain together. Uh, and then there's a controller on the inside that has a little FPGA on it. Um, cause I'm reusing work from Peter Esden and other people that are made LED cubes. The code is already written for that FPGA. So I could just take that and reuse it on my project. I don't have to, don't have to make my own code to drive the LEDs. Yeah. Uh, and using that, I created a little custom circuit board that fit on the inside and the whole thing fit into a 3D printed enclosure. So how big is this shift register? So is it just single shift register? It must be multiples. So every panel essentially architecturally looks like an array of 16 by 16 LEDs. Okay. Except that only half of them are populated. You can imagine a square of 16 by 16. If you cut that diagonally, I basically threw out the top half of that triangle. And the bottom half is what was, is populated on the circuit board. Oh, okay. But the LEDs are multiplexed with shift registers that we've got 16 bits multiplied by three because there are RGB LEDs. Um, and then we have a 16 bit kind of row driver. So with the shift registers, they are all cascaded in a single, basically in a single chain. Um, so we have, uh, uh, sync drivers, 16 bit sync drivers that drive red, green, and blue channels. And then there's another set of two 74 series, uh, 595 shift registers that drive the, uh, anodes of the LEDs. And basically that just looks like a single 64 bit shift register with, um, uh, you know, clock data latch and blank signals.

**Chris Gammell:** And so how fast can, how fast can you clock something like that then?

**Icebreaker FPGA:** Uh, the shift registers probably let you run up to, uh, I want to say 30 or 40 megahertz before they'll give up basically. And with the number of LEDs I've got, I broke the chain into four sets of, um, shift registers and they're kind of five panels long. And with that kind of breakup, I can drive all the LEDs in a 10 bit color mode at about 120 frames a second. Whoa. Okay.

**Chris Gammell:** Nice. So then what does it look like? So you, so you have 10 bits of color, you have 120 frames per second. What does it look like when you then map this? So you're, you're, then you're like, okay, I've, I've hooked all this stuff up. I got it in the FPGA. It's all mapped out, which is non-trivial of course. But, um, what does that look like for like writing, writing software to drive the actual programming of, of these LEDs?

**Icebreaker FPGA:** So I'm still a little bit lazy on this, this aspect of the project. Um, basically the FPGA has a frame buffer inside that is just a two dimensional frame buffer. Um, so remember before I said that every panel essentially looks like a 16 by 16 array of pixels, but we're cutting that array in half diagonally. Uh, it turns out, well, the way it's working internally, it's still driving the other six, the other half of that, uh, the other half of those LEDs. They're just not populated anywhere. And so the frame buffer is just a two dimensional frame buffer. And then in order to actually display on a single panel, you need to remap how that essentially how that frame buffer is turned into a checkerboard and then diagonally sliced, which I haven't done. All of the animations I've, I've built for this so far have just written to the, the 2d frame buffer directly.

**Chris Gammell:** Well, it still looks good. So who cares? Right. I mean, you're getting to the pieces here.

**Icebreaker FPGA:** So like, yeah, that's what you really care about. Yeah. The animations I've written, uh, I kind of picked so they don't highlight this fact, but say I wanted to make a, so there's an accelerometer inside. And so it could actually always have a dot that appears on the top surface as you move the, uh, the echoes that he'd run around in order to facilitate an animation like that. I would need to do basically what you're describing to do a, like a remap between, uh, this two dimensional frame buffer. And basically I think you'd want to do almost spherical coordinates around the, the echoes of hedron.

**Chris Gammell:** Like an R and theta or something like that.

**Icebreaker FPGA:** Yeah. And that would just be a one-time calculation that would be encoded into a lookup table.

**Chris Gammell:** Okay. Well, more to, more to do, but it's not, it's beside the point really. I mean, I was, I was just curious about the mapping in general because I think about LED projects and that's usually where I get held up as I'm like, oh, well, how do you, how do you actually write software for it? That looks interesting and, you know, um, you know, just does something, you know, like I, I feel like I can, you know, I could design the boards, I can design the, you know, and maybe, maybe figure out the FPGA piece, but then it's like, oh, okay, well I had to call a software person or something like that, you know? And so that's where I was kind of curious about that piece.

**Icebreaker FPGA:** Yeah. In fact, I've seen, since I built this, there's been two other projects that have appeared on, on my Twitter feed, actually. Um, one from, um, horrible names, uh, uh, jury, I think is his name. He makes some brass sculptures and he's made, uh, an entire sphere out of WS 2812s.

**Chris Gammell:** Oh yeah. I saw that one. Yeah. That, uh, it was like rolling in the dark, right?

**Icebreaker FPGA:** Yeah. Yeah. Yeah. And actually just, just this week, somebody's made one using, uh, circuit boards that are fitted in kind of like, uh, like an arc shape. Yeah.

**Chris Gammell:** Like a slice of an orange that are kind of like crossover for one another.

**Icebreaker FPGA:** Yeah. Yeah. And, and the most recent animation they've made is from the side, making it look like a Pac-Man.

**Chris Gammell:** Oh yeah. Which I thought was pretty creative. Yeah. That's great. It's, it's nice that like this kind of stuff, you know, it's, you're not making a product here, right? It's not like you're selling a D20, uh, you know, die to gaming nerds. Although that would, that would definitely kill a game convention.

**Icebreaker FPGA:** I'm just saying, uh, uh, but you know, yeah, it would definitely, uh, probably kill my wrists as well. Placing that many LEDs.

**Chris Gammell:** I think, you know, maybe you can outsource it. I feel like if I made another one. Yeah. Yeah. How long, how long did it take to, uh, to assemble this?

**Icebreaker FPGA:** Well, I did it all piecewise. So I did like, um, the LED panels were panelized as a, a four, four circuit boards in one. So I, I just had to assemble four at a time and each four probably took maybe an hour. Oh, okay. Placing LEDs. So it's not, not too long.

**Chris Gammell:** So 15 minutes per butt times 20. And then, you know, the actual mechanical assembly and the coding and yeah. Yeah. And we'll ignore the fact I had to rework all the boards. Right. Right. Right. Yeah. All the, all the normal things. And then, so you, you 3d printed the, uh, the actual, the chassis that was holding this

**Icebreaker FPGA:** or how did that work? Uh, no. So I designed it to be 3d printed and then had shapeways make it out of nylon. Oh, okay. Yeah. Yeah. Um, there's quite a lot of fine detail. And I, I tried doing test prints on my FDM printer. I've got a Prusa i3. Uh-huh. Um, and they just didn't turn out. I mean, there's, uh, we're talking, talking about, you need a little pocket on every side.

**Chris Gammell:** Yeah.

**Icebreaker FPGA:** That's just, just over one millimeter deep. Yep. Yep. Um, to fit the circuit boards in. Yeah. That's the, that's the other secret of this thing. Well, it's supposed to be press fit. Um, when I rebuilt it, when I rebuilt it, yeah, I used some, um, silicon. Yeah. Some, um. I used some RTV or something. Yeah. Some RTV silicon just in every corner. So it's still replaceable if I need to, but, um, that just holds every panel and actually gives it a bit of shock absorbance.

**Chris Gammell:** Oh, yeah. That's good. So not, not quite ready for production yet. That's what we're really getting at here. Yeah. Yeah. Yeah.

**Icebreaker FPGA:** Uh, in fact, I've still got to tidy up some of the files and release them onto GitHub so people can make their own if they're, uh, well inclined.

**Chris Gammell:** Yeah. I saw you tweet about that to someone. Did, did you say like bomb cost was about like less than a hundred? Ooh, no.

**Icebreaker FPGA:** Oh no. Okay. The LEDs were less than a hundred dollars. I think it's about $60 worth of LEDs, like just the LEDs. Okay. Um, and then the driver electronics are probably also about another 60. Um, and then circuit boards, uh, basically free at this point. Yeah. Right. What a time to be alive. Yeah. Uh, but then the 3d print was, I paid to have it rush made cause I kind of ran out of time with this project. Right. But shapeways charged me about $150 for that. Ooh. Yeah. Um, just for the 3d print, you know, it's about tennis ball sized, but I mean, they're made on a half million dollar multimillion dollar machine. So yeah, I guess it makes sense. They can charge that much.

**Chris Gammell:** I have a, uh, at, uh, where Kycon was, I don't know if you took the tour when you're at M hub, but there's, there's a printer there where they just charged from material. It's probably the best deal. It's probably worth the cost of the membership just for that, because it's like, it would have been like 20 bucks compared to one 50 from, I've like done shapeways comparisons before. And it's like material cost alone is, it's pretty killer. I should have, uh, should have called in a favor and had you make it. Yeah. Next time, man, let me know. It's only the only run it once a week. So that is the downside. The rush, the rush thing does make it more expensive. And then, you know, shipping to Australia.

**Icebreaker FPGA:** Yeah. Yeah. I think I did, uh, take a look at that when I did the tour. Yeah. Uh, they also had the little colored donut there. Oh man. Right. Yeah. Yeah. It's a lot more dense than I would have thought. Yeah. Cause that's like a powdered night. Was that powdered nylon?

**Chris Gammell:** No, that one is the, uh, that's the object. So they get bought by the, whoever they got bought the other big one. Uh, but it's like a, again, maybe it is nylon. I don't know what the powder is made out of, but it's like a, it's like an inkjet process and it's a little bit different cause it's like a color, color based ink instead of just the, the binder by itself. Okay. Yeah. It's a, yeah, it's fun for a demo. I, I, I wonder about the 3d printing. Like when, when would it be useful to have like a colored, color demo like that? Like if I was an industrial designer, maybe, you know, if any of my 3d models had any element of design to them.

**Icebreaker FPGA:** I leave a lot of the design stuff to, to the designers. Yeah. Yeah. Focus on the electronics. Exactly.

**Chris Gammell:** They're, they're great at it. They'll, they'll get that stuff done. Uh, so you mentioned the, uh, you know, the rush shipping and getting it to Adelaide and stuff like that. What is, what is Adelaide like? I mean, what is, what is your part of the world like?

**Icebreaker FPGA:** Um, it's right now it's quite hot, although we just had a cool change come through. So yeah. Last week we had 40 degrees or two days ago was 40 degrees. Yeah. And today we had rain showers. So I really don't know what's happening with the weather.

**Chris Gammell:** Yeah. Well, yeah. I mean, obviously lots of Australia is having, uh, lots of climate issues right now. Uh, I don't know if the fires are there. Yeah. Yeah. It is. But.

**Icebreaker FPGA:** No. Well, so a lot of the fires are on the East coast right now. Yeah. Um, unfortunately we had a fire breakout on place called Kangaroo Island, which is just, uh, a little island. You can get a ferry off to it's like nice little tourist destination. Uh, but the fires there, uh, I think it may have got through like one third of the island, which is pretty devastating. Ooh.

**Chris Gammell:** Yikes. Yeah. It's tough. I mean, like, I mean, you're, and you're further South. I mean, you're Adelaide's the bottom, the bottom of Australia, right?

**Icebreaker FPGA:** Yeah. Kind of central at the bottom. Yeah.

**Chris Gammell:** Is there an electronic scene? I mean, what does it, what does that look like? I mean, obviously you have a gig there. Um, but what is, what is the professional scene like there?

**Icebreaker FPGA:** Tough. Yeah. Okay. Um, a lot of my friends that graduated the same year as me, they've moved interstate. Uh, we have a little bit of a resurgence now with, we've got a few like space initiatives starting up with our new, uh, government backed space agency, um, that that's now headquartered in Adelaide. Oh, that's cool. The government's trying to push, push grants out to local manufacturing electronics industries, so hopefully we'll see a bit of a rise there.

**Chris Gammell:** But no, uh, I guess what I'm really getting at is like, is there, are there enough people to have like a five person meetup? Like, is that, or is that kind of tough, a tough ask?

**Icebreaker FPGA:** It's a little bit tough. We have a, we do have a hackerspace here. Okay. That's a good start. Um, the facilities are a little bit, little bit, um, varied compared to international hack spaces though. Well, uh, we basically share space with the university one day a week. And then there's another meetup, uh, on the weekends that's at a community center space.

**Chris Gammell:** Yeah.

**Icebreaker FPGA:** Uh, so there's no real, like, you know, 24 hour access to, you know, like a facility that you can, you know, go to and hack around on things yet. Well, we do have a makerspace that's opened up in the city. Uh, that's only a recent addition though. So hopefully we'll see that extend this year.

**Chris Gammell:** Well, what I'm hearing here is if there are any listeners in or nearby Adelaide, give Greg a call that, uh, that sounds like, uh, you know, you never know, like I, it's always weird too. Like I, I keep meeting people that are like in Chicago, obviously Chicago, Chicago is pretty big, but like, you know, just, you never know where, where the, you know, maybe the introverts are hanging out in their garages or their, their lofts or wherever they are. And, uh, it's good to, to get the word out where you are.

**Icebreaker FPGA:** So, yeah. Yeah. I mean, that's, that's obviously true. I mean, I tend to just stick to my home lab here just because it's a bit more equipped than, uh, than the hackerspaces meeting areas are.

**Chris Gammell:** Oh, totally. Yeah. I mean, I go to hackerspaces for social events. I don't go for gear. I, I have, I have my own stuff and I, and sometimes I'm not willing to share it, you know, not to sound bad about it, but you know, you never know what's going to happen to it. Um, well, let's talk more about projects that you've been, you've been, uh, working on. I mean, so you did that one. I think I first, you and I first interacted, I think on Twitter about that tracker that, um, that Sam R34, it was like a Laura tracker. Is that right? Oh yeah. Yeah. What ended up happening with that?

**Icebreaker FPGA:** Uh, it's sitting on my desk right now. Uh, in fact, I can see it.

**Chris Gammell:** It knows exactly where it is. So do you. So it sounds like it's a hell of a tracker.

**Icebreaker FPGA:** Yeah. I mean, I know where it is and it knows where it is. No, like a lot of projects that, uh, the hardware is what I really excel at. So I designed up the circuit boards, had them manufactured, uh, got the bare circuit boards back from China and assembled them, took some nice fancy photos and threw them off on my Twitter feed. Uh, and now it's sat basically idle because I'm too lazy to write the firmware for it.

**Chris Gammell:** Well, I mean, that's work, right?

**Icebreaker FPGA:** I mean, that's what you do for work. So it's a fate that a lot of my projects fall into. Yeah. I mean, at work, I do the same, same thing. Basically it's, uh, I do the full stack. So I have to do the hardware, software and firmware side, and then also documentation. So basically I stretch that muscle enough at work that sometimes I don't want to write firmware for my hobby projects.

**Chris Gammell:** Yeah, no, I feel it. I feel it, man. That's, uh, that's my goal for 2020 is to, to do more of the firmware projects at home because I need to, I need to improve my skills. But yeah, it sounds like, like even just saying it like that, that sounded like, like me going, you know, it's me going to the gym. I'll give up on it in March or something. Well, that's, that's cool though. So, so what was, what was that project for people who don't know?

**Icebreaker FPGA:** Um, so basically I created a, uh, little GPS tracker unit, uh, maybe four years ago now for a local Beagle club. Oh, what is it? What is that? To be able to, sorry. I would say Beagle is the dog. Yeah, I, I got that. Beagle dogs. Yeah. Yeah. Yeah. So there's a club for people that are like Beagle enthusiasts. No, Beagle owners. So basically Beagles are really good at tracking scents. And so there's all these clubs around that let you take your Beagles and it's, um, they, they run a trail bike with, um, some raw meat dangling from the back around like farmland. And then they let the Beagles chase the scent. Okay. So it's like. They basically work up to this, but they chase the scent. And it's, uh, at the pack count level, which is the higher level, I think it's about a five or a six K kilometer, uh, track that they run. Wow. Following this scent and they follow it pretty closely. Basically they wanted a GPS to just put in the pouch behind the dogs so they could look at how closely they were following and they could put one on every dog and see, oh, Hey, this dog, you know, walked around the tree five times before getting back onto the scent. Um, that's why he came back late, you know? Right. And so I made this little handheld device battery powered. Um, I think this one was MSP four 30 driven. Cause that's what I was using at the time. Uh, just takes a GPS feed, records it to an SD card inside. Um, and then you can download the logs later over USB. Um, and this project worked pretty well. And so I had all these enclosures leftover after I'd done a small batch for this club. And so I decided to redesign the board with a wireless interface. So you could potentially have a Laura receiver and have it transmit, um, just packets over Laura. I wasn't really focusing on the Laura WAN aspect of, of kind of that ecosystem, just, just the Laura transceiver itself, you know, long range, a low power, long range kind of, and also low bandwidth. I mean, I was just wanting to send basically just, uh, ID number, where they are at the time or whatever. Yeah. Uh, and so basically AdMail had just come out with this new part, uh, which I think, uh, you were using, or you mentioned it on the amp hour. So I thought I'd pick up, uh, pick some up and design up a board for it. And so I built the boards, but I haven't programmed them yet. These things happen, but that's kind of where the project grew out from. So, I mean, this was really just a hobby thing to me, you know, maybe play around with this chip.

**Chris Gammell:** I think, I think that the first thing I saw, I think it was the first time I saw like the renders you were doing too. And like, and maybe we could talk about the renders real quick. Cause you give, you give a talk at Kaikan about it, but, uh, that's part of like the, you know, people looking at your Twitter feed, uh, regularly see these renders that you're doing. So, and that was one of the first ones that I saw, I think as well. So what is your, what is your process there? Like, what are you, what are you doing with the rendering?

**Icebreaker FPGA:** Um, yeah, basically from Kaikad, you know, you can be stuck in the, the design page of Kaikad, looking at your circuit board for so long that you kind of can't see the trees from the forest. And I always find that if I switch into the 3d mode and I'm looking at the 3d board, suddenly I get so much more insight as to like, oh no, that, that, that button is way too close to the connector there. I'm, you know, I'm not going to be able to push that. Um, and then also there's an aspect of mechanical integration to get a circuit board to fit into a mechanical assembly, like an enclosure or a case. So there's a need to have a 3d representation of your board. And so Kaikad actually has an option now for exporting, uh, step models. So, um, S T E P step, and those can be imported into mechanical environments. Um, fusion 360, uh, there's actually another, another file format, keypad exports that you can import into blender. Uh, and so I was doing this just for the mechanical aspect. And then I realized that these CAD programs have a way to render boards. Uh, and so I started playing around with that and just, you know, take a look at what board renders look like. Um, and then from that, how, how different is a physical board to what the program renders and straight away, you'll see that keypad doesn't export the actual copper layers or the silkscreen or any of like the actual features on a circuit board. It just, it just gives you like a blank, uh, a blank, um, solid mass. Yeah. It's basically a 3d rectangle cube, I guess. Yeah. Yeah. More or less just a little flat solid. And so the first step was poking around it, um, plotting settings in keypad. You can plot PDF files of your boards, uh, PDF, and then I moved to SVG. And so you can plot the copper layers as an SVG file and then convert that to a PNG and then apply that as like a, a texture almost to the, to that solid, uh, circuit circuit board in the mechanical CAD tools. And when you render that, it looks like, looks well, it's better.

**Chris Gammell:** Yeah. It's almost like a, like a wallpaper that you're wrapping around. A piece of like solid material kind of thing. Like it kind of warps around it. That kind of idea.

**Icebreaker FPGA:** Yeah. Yeah. More or less. And then instead of doing all this manually, I've started poking around at the scripting features in key CAD. And so I've written a few Python scripts that integrate into the scripting environment in key CAD. And so just by running the script, you generate a stack of SVG layers. It's colorized and then exports to a PNG file. And then this basically, yeah, it's like a, what you're saying, a wallpaper or I think Fusion 360 calls it a decal, like a sticker that you basically are putting onto your model. And then that, that basically gets you like 80 to 90% of the way to like, almost like a photorealistic board. You're missing a lot of the material properties of a real circuit board. Right.

**Chris Gammell:** Yeah. Like the reflectiveness or whatever, reflectivity and like what absorbs or bounces light, that kind of thing.

**Icebreaker FPGA:** Yeah. And the fact that a lot of these things you kind of almost take for granted. I mean, you look at a circuit board and it just looks like a circuit board to you. But if you get light to bounce off of the right way, you can have, say the Enig might show up like the, the gold plated pads. But the surface of the actual soda mask is reflecting all the light. If you get the angle just right. And it might just appear white because it's reflecting, reflecting light. And so it's hard to get all of these materials to map perfectly. So I basically stopped trying to achieve any closer to photorealism and just kind of stopped to that 80% mark. Yeah. But even with that, you can enable features in these CAD tools like depth of field.

**Chris Gammell:** Right. Yeah.

**Icebreaker FPGA:** Right. And that, that really makes it feel like real, right? Yeah. Suddenly it makes it look like you've, you know, you're using a real camera. It's not like, you know, you get the depth of field that you would get if you were using a macro lens, you know, you're right zoomed into your board. And so I've started, started just turning those features, basically turn those on because they're in the programs and gives you a bit of an extra, extra depth. You can say for free.

**Chris Gammell:** Yeah. I mean, it just, it's kind of just tricking the human eyeball into thinking it's looking at something real, you know, like that's kind of what it comes down to. Obviously there's like eye candy that's on Twitter. Do you find, I mean, you've mentioned kind of the, the 3d kind of piecing stuff together. Is it, is it because the, the geometries are so small or, or because you're using weird case sizes or how do you find this most useful?

**Icebreaker FPGA:** Moving back to the icosahedron project. I exported the boards from that and had them in my mechanical 3d environment just to look at things like, like how the PCBs will be mounted. So the LEDs have a certain height. I think the LEDs I'm using are maybe 0.8 millimeters thick. And then the circuit board is going to be one millimeter thick or 1.2. And I couldn't quite decide if I wanted to go one or 1.2. And so exported it into the 3d model and you can basically embed the circuit board into the shape I'd already sent off to be 3d printed. And I could basically tell, you know, Hey, I do want this a little bit thicker. So the LEDs are sitting flush or they're going to sit poking out a little bit. And it's just kind of the entire mechanical integration aspect. I mean, some projects will just stay as a bare circuit board forever, but most products don't exist in that form. They're going to be in some kind of enclosure or some kind of case. And as soon as you have, you know, buttons on your circuit board that have to be exposed through a opening and enclosure or, you know, like a button in an enclosure that has to activate, actuate on a button on the PCB, kind of all of these problems are helped with the 3d representation.

**Chris Gammell:** Yeah, that's, that's good. That's good. Um, one thing I wanted to talk about that we haven't brought up yet is, uh, soldering stuff mostly because that's a large, uh, another large part of your, your Twitter feed is showing these, uh, you know, these solder hacks or, or I guess reworks and, and similar kinds of things. And I was wondering if you had, I mean, so another one of my goals for 2020 is, is to just better, get better at soldering in general. Like I've, I have pretty sloppy technique. Um, I don't know if you have any like tips and tricks to just kind of how you, how you find yourself improving or, or what, what do you find on a daily basis to, uh, to make you better at soldering?

**Icebreaker FPGA:** Yeah, I'm not sure. I mean, I've just, I guess I've just gotten better with time and practice and, uh, I guess trying, I I'd say try to practice soldering with low risk projects. So you really shouldn't be, you know, looking at a board that you have to go work on. You're working tomorrow and it's 2am and you know, you're bumping your head. It's like, I just need to solder this one, this one bodge wire will fix, you know, everything. Uh, but the bodge wires, you know, under a BGA part, you've got to run out. See, that's a very, I guess, like high risk environment and you're pretty likely to mess it up. Um, if you haven't done that kind of stuff before. And I mean, a lot of the times with practicing this stuff, I'll mess it up, but it doesn't matter. Like you just, you could just try again. I'm not really reliant on a lot of my soldering hacks to, to go into kind of production things.

**Chris Gammell:** Yeah.

**Icebreaker FPGA:** Yeah. I'm just trying to get boards that I've made working without having to kind of re-spin them.

**Chris Gammell:** Yeah.

**Icebreaker FPGA:** On kind of like a hobby level.

**Chris Gammell:** Saving time for, for spins and similar kind of things. Hmm. Um, so I don't, I don't know if I have any tips. Uh, I guess what's your, what's your setup at home?

**Icebreaker FPGA:** Like maybe that's, that's a better question probably. Okay. I mean, a lot of people might laugh at this. My soldering station is, um, a Quico brand. Is that like the cheapo, cheapo, uh, low cost hot air pencil? Uh, yeah. So this is a, just a soldering, um, pencil. It takes T12 tips, which is a hacker style tip, but Quico is a brand I found on Ali express for about 30 bucks. Nice. Uh, so that's, that's the soldering iron I use at home. A $30 soldering iron works great for, so all the soldering iron I do is lead free. So works great for the lead free stuff. What is, uh, what's your, what's your solder and flux of choice? I quite like the spark fun lead free solder. Okay. Um, which is what I've been using. I bought a 500 gram spool of it. Jeez. I don't know. Uh, five years ago now, you know, I've still got 200 grams left. Nice. Yeah.

**Chris Gammell:** It doesn't go fast. I mean, even, even with lots of projects, you can really get away with, you know, having around for a while.

**Icebreaker FPGA:** Yeah. And soldering paste, uh, I've bought quite a large quantity now of, um, it's a Loctite GC 10. Uh, unfortunately you have to buy a large quantity. You can only buy tubes of 500 grams or 600 grams, um, which ends up to be quite cheap per gram, but it's still, you have to buy 500 grams worth. So it's, it's not really a cheap investment, unfortunately, but it's turned out to be really good solder paste. And that's what I use for everything now. And what about flux? Uh, flux. I don't quite know the model number off the top of my head, but it's, uh, a tacky flux from Amtech, uh, that I found out about from watching some of Lewis Rossman's MacBook repair videos on YouTube. Yeah.

**Chris Gammell:** Past guest of the show. Lewis Rossman is probably, yeah. That, I mean, watching that guy solder is, it's impressive. You know, it's, he's doing some small spots, small stuff.

**Icebreaker FPGA:** Yeah. And I think he's probably started in a similar seat. I mean, none of us, you know, are born knowing how to, how to solder BGA components. Yeah. Uh, we just kind of learn it. Yep. And I think he, he just like self-taught himself all of that. Right.

**Chris Gammell:** Um, what about, uh, I mean, I guess another thing is magnification. I mean, Lewis, obviously, and you as well. I mean, like, I think that's a big thing that I've come, come around to is like, it's not cheating to have magnification. It's, that's necessary. It's, it's smart. It's like, I don't know why I avoided it for so long, but like I had like, I always used to try and hand solder stuff with just like my eyeballs. And then I'd look at, finally looked at my solder joints under a microscope and I was like, oh my God, what am I doing here? Yeah.

**Icebreaker FPGA:** Yeah. Yeah. So, I mean, I, I bought, uh, uh, last year I bought an Amtec, uh, uh, hang on there. Amscope. Amscope. I don't know why every, every company has to start with Am. Amscope is, uh, like a, it's the American brand of like a Chinese series of microscopes or something. Um, but they're quite low cost affordable microscopes. So I bought one of those from, I think just from China.

**Chris Gammell:** Yeah.

**Icebreaker FPGA:** Yeah. Um, and so, uh, stereo microscope. So two eyepieces that gives you the, the depth kind of depth perception under the microscope. Yeah.

**Chris Gammell:** So it's like, you're actually using your eyeballs instead of, instead of looking through eyepieces and that kind of thing.

**Icebreaker FPGA:** Yeah. And I think with the setup I've got now, it's about a 3.5 to about 20 times magnification.

**Chris Gammell:** Yep.

**Icebreaker FPGA:** Um, so 3.5 is good. You, like that's the, the widest you can go. Mm-hmm. And that gives you a, a, a view about like of a credit card sized working area underneath. Um, and then you can definitely zoom all the way in if you need to inspect joints or if you're soldering, um, soldering bodge wise on. After getting that at work, uh, I picked up, found one secondhand, uh, basically the identical microscope, but it's a Japanese branded one. And so it's a little bit more expensive, but the optics are just, just a little bit, it's hard to really put your finger on it. They're just like sharper. Oh, okay. Basically, you know, almost functions the same. I could switch between the two, the Japanese one, uh, the camera. So that it's a Japanese one's a trinocular port. So it has a port for your camera to attach to as well. And you can use the camera while using the eyepieces. Yeah.

**Chris Gammell:** That's nice. That's really nice.

**Icebreaker FPGA:** Which is a feature. A lot of them. Yeah. See what you're doing. Yeah. A lot of them call that simul focus, I think. Oh. To be able to use both the camera port and the eyepieces. Some of the cheaper models, they give you a little switch that you basically push and that moves a mirror in and out. And basically the camera basically just redirects one of the eyepieces. Uh, and that's, if you can avoid that type, um, when you're buying them, I definitely would be looking for the one where all three ports are active at the same time. That's good. Well, nice.

**Chris Gammell:** That's nice. So do you have a stereo microscope now? I have one at, uh, M-Hub has a couple. Um, they're not stereo though. Yeah. They're just mono. It's like dual eyepiece, but stereo, but mono. I think, I think it's the same view. Cause I don't get much depth out of it. And, um, but yeah, stereo is nice for that, for, for getting additional depth and stuff like that. Yeah. Yeah.

**Icebreaker FPGA:** The, I mean, the other type is, uh, I guess what Dave has, which is like the Mantis scope, right? Which I think is like a heads up LCD almost that you're looking into, but there are almost a different price range.

**Chris Gammell:** Yeah, definitely. Yeah. You need to have enough like focal range that you can, you need to have enough zoom, I guess, to, to be able to get in. So you have your hands are free under there. That's kind of like the, one of the big things I feel like, uh, the lower cost, older, older microscopes. It's like, yeah, you can get in as close as you need to with, you know, like how it looks, but you're also going to be right on top of your, your, your scopes right on top of your side of your hand, which is not what you want to have.

**Icebreaker FPGA:** Yeah. Yeah. So with the stereo ones, um, you get something called a, a Barlow lens, which basically attaches to the, the bottom of the microscope. Uh huh. And it will have the zoom distance, but double the working distance. Uh, so that's what I have on mine, which gives me about 15 centimeters, 15 to 20 centimeters of, of working distance, which is, you know, plenty to get, get light into your seat, like in and around what you're working on and, you know, soldering iron and your third hand, you know?

**Chris Gammell:** Yeah. Yeah. And to get it up off the table, if you needed to, I mean, like, it's nice if you have like one of those low slung, um, holders, what do they call those? Like the, uh, I think you, you have one of those, right? The, the clamps that are like directly on the desk.

**Icebreaker FPGA:** Yeah. Mine clamps on the side of my desk and it has like a swinging, uh, that can, the scope can swing out, uh, swing out over the desk.

**Chris Gammell:** That's great. So, okay. One last question, question about solder or soldering, uh, is, is your solder paste application? Because that's another thing that I noticed in your photos all the time is you have these super clean solder paste poles. And I know that it's, you know, social media, so it's a selection of the best ones, I'm sure. But what is your, uh, your solder paste technique look like? I mean, are you using stencils? Are you using, uh, sorry, frame stencils? Are you using loose stencils? Are you, uh, do you have a jig? How are you doing all of this stuff?

**Icebreaker FPGA:** Yeah, actually a lot of the time you can tell if I've had to, uh, wipe off the solder paste can try again because you get little solder balls stuck under the solder mask. Oh yeah. But often I can now get pretty good, uh, application on the first try if, if I spend time setting it up. Um, so for a lot of my hobby boards, I will use just, uh, unframed stencils. So just basically the stainless steel sheets that you get. Yeah. From, uh, fab houses, just a standard laser cut stencil.

**Chris Gammell:** Yeah. I will say those are, uh, I, I have recently determined those are the most dangerous pieces of equipment that are in my entire lab. Not, not hot solder irons, not, you know, cutters, not exacto knives, nothing like that. I sliced the crap out of my hand by not realizing there was a solder paste or stainless steel sheet underneath something else. And I just like jam my hand into it. Oh my God, I was bleeding everywhere. So be careful about stainless steel folks. That, that'll cut you deep. Yeah.

**Icebreaker FPGA:** Yeah. I mean, uh, they're, uh, they're pretty sharp on those corners.

**Chris Gammell:** No, not even the corner. It was just an edge. It was just an edge that like. Just the side. Yeah. I just push, you know, flesh in the edge of stainless. It's like a, it's a knife, you know, it's a dull knife.

**Icebreaker FPGA:** Yeah. Yeah. Especially you can get like thinner ones. I think some of the thin ones I've got, uh, probably what, 8,000. Oh really? Okay. Um, which is, so, you know, you're basically on the verge of like razor blade thickness at that point. Yep. Yeah. So I, I just use unframed stencils and yeah, you do be careful of where you store them. Um, uh, well, if you buy them from Osh stencils, they have lots of warning tape that says, you know, stencil is sharp, you know, do not cut yourself. But the chat, the ones from China just come in a Ziploc bag. So I use circuit boards around the board that I'm actually trying to stencil just to raise up the stencil off the table and have a basically a flat plane that the steel sheet will sit on. Cause if you don't do that, the, basically if you were to bend the edge of the stencil down to the level of the table, it would bow the entire stencil. It wouldn't be sitting flat anymore. If you can kind of imagine. Yeah. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** It's like, uh, it's like, uh, if you're stretching saran wrap over a book or something like that, you know, you get like that, that bend down kind of thing or tinfoil or something.

**Icebreaker FPGA:** Hmm. So I think it's a common technique to use spare PCBs cause then they're all the same thickness, you know, it gives you a nice level field. Um, and then I use blue painters tape. I mean, you could use just masking tape, um, to hold down the stencil. So you kind of align it by eye. I use blue painters tape along one edge. Uh, and I always use fresh solder paste. So that's, that's another key thing. Yep. Uh, I like to store my paste in a, in a, in a syringe, like a Luolock syringe. So like a blunt tip. Um, and I'll apply solder paste to the stencil, just like a long bead along the top. Uh, and I've recently bought a proper stenciling squeegee. Oh yeah. So it's got a stainless steel blade in that, uh, that gives you a lot more force to apply, uh, like as you're squeegeeing. And then, yeah, I mean, often I used to think that you had to squeegee in one single stroke in order to get a good application. A lot of the time now I try to do, like, I just try to mix up my technique and be like, well, will this actually work? Will it make it worse or better? And so recently I've been doing, uh, like one squeegee down from the top and then, uh, up from the bottom. So like kind of in both directions. And that seems to be working quite well. And then I do one final pass, which is quite a sharp, sharp, sharp angle.

**Chris Gammell:** Um, to try and like scrape off the top and that kind of thing.

**Icebreaker FPGA:** Yeah. I usually squeegee at a shallow angle to kind of push the solder paste through the stencil and then I'll do a clean up pass at a really sharp angle, almost like 90 degrees to the stencil, just kind of push down and across. And that just cleans up the top, uh, and really gives you a nice.

**Chris Gammell:** Photographical. Nice application. Really nice looking, uh, solder paste porn photos. Yeah.

**Icebreaker FPGA:** And then, you know, I, then I pull out the macro lens and set up the, the camera flashes and, uh, soft box and takes the photos. Yeah. But one thing I found with this solder paste, it's really, it's got a great, uh, working life. I think on the data sheet, they specify 24 hours. Oh, wow. From when you, when you stencil it onto your board to when it needs to be reflowed.

**Chris Gammell:** That is.

**Icebreaker FPGA:** Yeah. And so often, often my boards, as you've seen a quiet, I mean, I, I don't know if I'd say complicated, but often they do have a lot of parts on them. Like per board. Oh, I'll think I'll be able to get something done in time. And then it'll be like two in the morning and I'm like, I just can't place these components anymore. I gotta go to sleep. And so I'll just put a cover over the board, like throw the board in, uh, just something so the dust doesn't settle on it. Uh, and just finish placing components in the morning.

**Chris Gammell:** Okay. Yeah. Yeah. It's good too. I mean, you save, I mean, at a certain point you literally have like diminishing returns, you know, your hands get shaky, your eyes get tired, everything like that. And you're just going to start doing, you're starting to make, making, making mistakes at that point. So.

**Icebreaker FPGA:** Yeah. That's definitely, uh, definitely learned that from experience.

**Chris Gammell:** I know this is going to sound weird asking this on an electronics podcast, but do you ever get sick of electronics?

**Icebreaker FPGA:** Uh, I mean, there's definitely times when I'm less motivated to work on projects. I think everybody gets this. Um, but there's just so many other facets.

**Chris Gammell:** It seems like you do a lot. I'm just, I'm, I, I, I feel like I should say I am very much in awe of the work you do. Like, I think you do great work, Greg. Um, and I learned a lot from watching your Twitter feed and stuff like this, but it seems like you just do a lot. Um, and then you do it at work too. So like, like that's awesome, but damn, like, dude, that's why I was wondering if you get tired of it, you know?

**Icebreaker FPGA:** Yeah. No, I, I think, um, there's definitely different facets that scratch a different itch in my brain. So like designing boards and then actually manufacturing them. I feel like they're definitely two different tasks. Uh, and I know other engineers that really love designing boards and they design fantastic boards, but like they would never, never even think about assembling themselves. Like they would just pay for somebody to assemble them. Um, you know, either that's, they're just not interested in doing that or they don't feel like they have the skills or it's not worth their time. I mean, so I feel like they are two different tasks and I just enjoy both of them. Um, yeah. Yeah. The, the designing definitely, sometimes I, I definitely have days where, you know, I've just, it, it definitely like, it doesn't flow as easily. It's almost like writer's block. Yeah. Yeah. Yeah. You know, it's like, I know I have to place these, you know, schematic blocks, you know, I need a power management, you know, section for this board.

**Chris Gammell:** Another buck converter.

**Icebreaker FPGA:** You know? Yeah. So like, you know, I know what I need to do, but then like, I just, I get distracted and, you know, spend the afternoon watching YouTube videos or something.

**Chris Gammell:** I've never done that. Um, I definitely never done that every day.

**Icebreaker FPGA:** And so, yeah, I mean, there's, like I said, there's kind of two different things. So sometimes I might get sick of, uh, not sick of, but like not designing thing. Like.

**Chris Gammell:** Yeah.

**Icebreaker FPGA:** You view them as all different tasks and different, different energy to like work on a new design. So I just pull off a box from my shelf and, uh, you know, start writing some firmware for a project that I haven't, you know, looked at and kind of, uh, try to just try, try to doing something productive with my time, even if it's not, uh, the highest priority on the list.

**Chris Gammell:** I mean, as a casual observer, I want you to just do the cool things personally. So whatever, whatever you're doing. Great. Great with me, man. I would, honestly, I was just curious cause it seems like, you know, you're very driven. So that's, it's great. That's really great. Uh, what else do people know about you? I mean, we're kind of coming to our end here. So.

**Icebreaker FPGA:** Yeah. Well, I'm now realizing that I'm at the start when I introduced myself saying that I'm from Twitter, I don't actually work for Twitter. I just post on Twitter.

**Chris Gammell:** Right. Right. People are like sitting here this whole time. Like, man, this guy does a lot of electronics. I've never seen any Twitter products out there.

**Icebreaker FPGA:** Yeah. Um, no, I don't know. I have a blog as well, but I don't, uh, I don't really post on there as often as I should, which I think is a common thread. Ah, should.

**Chris Gammell:** Who knows should, you know, it's just, you just haven't done it in a while. I haven't done it in a while, you know, blogs are so last decade, really even the decade before that. Cool. Well, that's, that's good. Uh, where can people find you? I mean, I guess Twitter is one thing.

**Icebreaker FPGA:** Yeah. That's probably where I'm most active. Just onto my Twitter feed. I'm sure you'll have all this linked in the description of the podcast. Yep. Yep. Yeah. Otherwise on my website, I think there's probably an email link at the bottom of my website. Um, if anybody wants to reach out. Cool.

**Chris Gammell:** Well, Greg, thank you for, uh, for being my Aussie stand in this week. I mean, Dave's on holiday and, uh, good, uh, good to talk to someone from down under. It feels like, it feels like a normal week and I enjoyed, uh, enjoyed talking to you.

**Icebreaker FPGA:** Yeah. Thanks. It's been, uh, fun talking to you too, Chris. It's a good start to 2020.

**Chris Gammell:** Yeah, definitely. Definitely. All right. Well, I'm sure I'll see you at a future conference cause you seem to be traveling a lot and, uh, I look forward to hanging out again. Yeah. Thanks. See ya.

**Icebreaker FPGA:** See you soon.

**Chris Gammell:** We'll be right back.
