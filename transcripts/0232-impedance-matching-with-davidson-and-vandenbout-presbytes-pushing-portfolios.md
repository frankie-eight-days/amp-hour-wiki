---
episode: 232
title: "\"Impedance Matching\" with Davidson and Vandenbout - Presbytes Pushing Portfolios"
url: https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/
---

**Chris Gammell:** This is The Amp Hour Podcast, reported January 13th, 2015. Episode 232, with Bob Davidson and Dave Vandenbaum, Prez Bytes, Pushing Portfolios. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Dave Vandenbaum:** I'm Dave Vandenbaum of XS Corporation. I'm Bob Davidson with Ambient Sensors.

**Chris Gammell:** And this is another, well, I just renamed it probably a couple hours before the show, but we're calling this Impedance Matching. Because we've had one show in the past where Greg Charvat and Mike Osman came back on, and that was critical success. We thought, why not throw some more guests back together? And Dave and Bob seem like a perfect match. We're going to have a good and possibly catankerous old time here. And some laughs and talking about the industry and electronics. So welcome back, guys.

**Dave Vandenbaum:** Thanks. Thank you. We may not be a critical success, but we'll certainly be critical. Yeah, that's right.

**Chris Gammell:** So what's been new? I mean, Bob, you were mentioning before the show you've got some consulting work. Dave, you've still got the FPGA boards and everything like that. How's everything been going?

**Dave Vandenbaum:** Why don't you go ahead, Bob?

**Bluetooth Low Energy:** Okay. Well, yeah, I've been doing consulting work to keep my product development for other companies to keep my lights on and pay the rent. But I'm also starting to develop some products because I realized that the only way you can really scale if you're just doing consulting type work is either work longer hours or charge more. And there's limits to both of those. That's right. But there's some interesting little side projects that I've been developing, a lot of them for my own work, but then figuring that other people might be interested in it. And so, you know, I'm doing some work with Bluetooth Low Energy, and I just finished, I just built today a new board that's going to let me create a long-range iBeacon. This is for outdoor applications that has a solar input, but also a battery and a battery management system to allow it to run 24-7, but be powered over time from the sun.

**Dave Vandenbaum:** Is that the one that you posted a picture of on Twitter that you said something about, you know, always doing a paper layout or something beforehand or something?

**Dave Jones:** Yeah.

**Chris Gammell:** Oh, I didn't see this, so I need some prompting here.

**Bluetooth Low Energy:** Well, it's supposed to fit in a box, and the box is an odd shape, and I laid it all out from the top, but I really wanted to have the solar cells on the bottom, so the board's supposed to flip over. But the symmetry of the box doesn't allow that. And I could have checked that, because I know better, but I got in a hurry. But the board's still going to be, I'm just building a couple of prototype boards now, and it'll still be useful for checking out the circuit, and then I'll deal with the shape of it. But I also got burned by this solar cell manufacturer, because they had this, I won't say who it is, but they had a spec sheet out that said that the solar cells could be run through a surface mount reflow process. So I put it through my, I have a little reflow oven, and it melted the solar cells. So then I read a little deeper into their spec sheet, and they said, oh, you're supposed to use this silver paste. Right.

**Chris Gammell:** Use some kryptonium and, you know, protect it. Yeah, and you bake it at 160 degrees.

**Bluetooth Low Energy:** Apparently 220 was more than, or 230 was more than it could handle.

**Dave Vandenbaum:** Yeah, I bought some little power connectors once from China, because they were cheap, and I hand soldered them onto the board. And I put the boards in the toaster oven to dry them off after I washed them down, and the toaster oven set at like 200 degrees Fahrenheit. And when I took them out, all those little connectors were all just warped and slumped down, like they were made out of chocolate. Yeah.

**Bluetooth Low Energy:** Yeah, it happens to everybody, no matter how experienced you get, I think. Just, that's how you learn. Yeah, the hard way. But do you? Well, I learned this. That's not to say that the next time something else works. That's right.

**Chris Gammell:** Small permutations still cause different results, huh? Yeah.

**Dave Vandenbaum:** Yeah, there's an infinite number of things to go wrong, so you can never get rid of all of them.

**Bluetooth Low Energy:** Yeah, that's why I get excited when something works, because...

**Dave Vandenbaum:** Yeah, I've always said that anything more complicated than a wire is probably going to take two tries to make it work.

**Bluetooth Low Energy:** Well, one of my clients is a software guy, and actually he should know better, but he was wondering why you couldn't just get this stuff perfect from the start. And he was making an analogy to, well, they build skyscrapers, and they don't build multiple versions of it before they get it right. Of course, that's not exactly true.

**Dave Vandenbaum:** Yeah, I read a novel once about the building in a skyscraper in New York, and it was just one thing after another, and all the little jimmies and shims that they had to put into it, and highly machined little connectors and stuff to get all the beams to meet together in the right way for these. And people, you know, they had these really nice machined spheres with places where these rods screwed into them, and they were using to put together this very beautiful canopy that went over the top of the skyscraper. And the spheres were so beautiful that people in the contracting office kept stealing them and using them for, you know, desk ornaments and things like that. That's awesome.

**Chris Gammell:** Yeah, I've always wanted to sit in on that meeting. Because, you know, like, I guess we kind of have that in the electronics industry, but, like, architects are basically, like, weird artists, right? They're, like, artists, but, like, I want to sit in the meeting where they get just, like, tongue-lashed by the structural engineers and be like, what are you doing here, man? This can't work. Like, have you ever done a load beam before? I mean, like, how is this possibly going to be held up, you know? It's just, like, taking art projects and then trying to make them stand up over time has got to be the most hilarious and terrifying meeting ever.

**Dave Vandenbaum:** It would have been great to sit in on that meeting with Gary when he designed those buildings up at MIT that looked like they had been put through the oven and just, you know, they just warped and melted.

**Chris Gammell:** I have a story about that, actually, because they paid for, at Case Western, where I went to school, they built it while I was there. It was a Gary building. It was by Peter B. Lewis, by the progressive insurance guy. Well, they designed it, and it was great. But then what ended up happening is the design constraint they didn't put in there, which we're seeing a lot of right now, is, well, when you have a huge, metal, shiny, slidey roof, sometimes the snow slides off of it and knocks students on their ass. So they ended up having to put guardrails around certain parts of the building, because if you walk there, you would literally get flattened by snow sliding off and knocking you over. Avalanche hazard.

**Dave Jones:** What?

**Dave Vandenbaum:** We had, at my undergraduate school at North Carolina State, they have a round building called Harrelson Hall, which they're tearing down this year, but it was designed back in the 60s, and it was just a round building. and had a big spiral ramp that went up the core of it that you would go to classes, you know, to get to classes. But all the classrooms had to be shaped like pie wedges. And there was not a right angle in the entire building, which, you know, just drives you crazy with desks, putting desks in the professor's offices and putting in bookcases and anything else. And all the blackboards had to be curved because they were being put on the walls, which were curved. It was just a complete mess. It was, you know, supposedly beautiful, but it was, you know, impractical to do it that way.

**Bluetooth Low Energy:** They needed flexible electronics.

**Chris Gammell:** Yeah. Well, yeah, and that's kind of the way around it, right? I mean, like you could probably shove – I'm looking at your picture now on Twitter now, Bob. You could probably shove a bunch of flexible electronics into this enclosure, but, you know, you got to basically pay for the privilege of doing as much. Oh, yeah. Yeah.

**Bluetooth Low Energy:** No, you know, that's why hardware, you know, is hard to do. And the thing is, is that once it gets this fully developed, I didn't expect the first board to work. And you just learn from each one and then improve it. Like, I have a bunch of ideas already after building this board, even though I'm fairly happy with it, that I want to add to it. One of the things I want to do is – that I didn't do, but it would be fairly easy to do is pull out the I squared C to some pins so that I can add external sensors and so forth to it. Oh, that's a good idea.

**Dave Vandenbaum:** Yeah, and that's the interesting part about doing the design is how much of those ideas come to you when you're doing the design, whereas so often you hear about people that say, well, you know, I just want to be the architecture guy. I want to design the architecture and, you know, have somebody go off and do the nitty-gritty details. But so much of the improvements and the new ideas you get are made while you're actually just forcing the board into the shape that it has to be. That's one of – This is close to that. You know, why can't I do this? And, you know.

**Bluetooth Low Energy:** That's one of the things, and that's kind of maybe how Chris first got alerted to Dave and I was – recently was – re-alerted to us. Yeah, you're right.

**Chris Gammell:** I've been totally ignoring you guys. We talked about pennies, man. Talking about that. Walking past you on the street, just like covering my eyes. Oh, God, I hope they don't see me. I hope they don't see me on Twitter.

**Dave Vandenbaum:** Alps for the blind. Alps for the blind.

**Bluetooth Low Energy:** But I was reading that book, Shopcraft as Soulcraft, by Crawford, which is a really good book, talking about the value of working with your hands and also the intellectual side of that. And one of the things I noticed when I came to work for HP a long time ago, we used to build everything, even the front panels and silkscreen, the letters and things on it. And now they don't build anything. And I've noticed that – No, Keysight's building it. Duh. Yeah, I know. Well, but even they aren't – actually, Keysight's in a really interesting situation. As I noticed, I noticed that companies like Rigel come out with really good equipment for not much money. And I've got one of their scopes and I've got their spectrum analyzer. And I was used to, like, with the spectrum analyzer, that that was something that was, you know, well north of $10,000 not very long ago. And now you can buy it for $1,000 or $1,500. But what happens is, well, they kept talking about moving up the value chain at HP and giving up things like manufacturing to low-cost places like Shinsen. But the thing is, just like the circuit board, a lot of your inspiration for the next designs come from being around the manufacturing. And if you give up the manufacturing, you just move further and further up that pyramid until there's nothing left.

**Chris Gammell:** And I see – You're a consultant for consultants about how to consult, right? Well, they sell services. Yeah. IBM? Are we talking about IBM too?

**Bluetooth Low Energy:** Well, IBM and HP, both the bean counters see a lot of – you know, they're just really attracted to that model, I suppose, because it doesn't – I don't know. Anyway.

**Chris Gammell:** Well, we could pay people and make stuff and have overhead costs or we could just pay people and then they can make stuff up. And let's go for that one.

**Dave Vandenbaum:** Well, let me give the opposite point of view because I used to work for AT&T and Bell Labs and, you know, we were the poster boys for vertically integrated at the plant that I worked at where they made telephones and customer premises equipment. They used to grind their own coal to make the microphones that went into the phones. And I mean, we did everything stem to stern. I mean, if it wasn't done by Western Electric and, you know, in-house, then it wasn't done. We had our own ICs. We had everything. And that caused a problem later on is when I started back in 79, we were doing a project and it needed a microprocessor in it. And the one that we selected was the Motorola 6801 with 2K of RAM and 128 bytes of RAM. I mean, we were swimming in it. Oh, yeah. You know, we needed that.

**Chris Gammell:** Where will I find the opcodes? What will I do with all this opportunity?

**Dave Vandenbaum:** We needed that processor in the way that it did its interrupts and the way that some of the peripherals it had for generating waveforms because we were generating and decoding the modem waveforms in the processor under interrupt loops. And so we needed it to be able to do that. And we had an internal group in Bell Labs that was making a 4-bit microcontroller called the MAC-4. And the problem with the internal groups in AT&T was we couldn't sell outside. Oh, yeah. It was not allowed legally for us to sell anything outside and compete with outside companies. So any project that needed a microprocessor, microcontroller, this MAC-4 group was going to latch onto it because that was the only way they had to make sales. And they came in and they pitched the MAC-4 to us. And we, you know, said, well, it doesn't do this and this. You know, it's a 4-bit machine. We need an 8-bit machine. We need these peripherals on here. You don't have the peripherals. It won't run fast enough. It's going to cost too much also because we not only had to pay our overhead on it, we had to pay your overhead on it as well as you know.

**Chris Gammell:** Support the fab and buy the chemicals.

**Dave Vandenbaum:** And we fought for months on that and had to have meetings and go back and forth on that all the time while we were trying to do the project. And then they finally admitted defeat. And then two weeks later, they came back and said, okay, how about two MAC-4s in there? So we go through the whole thing again for, you know, back and forth. No, it doesn't work. It's too much. It's too expensive. We don't know how to divide the program, blah, blah, blah, blah, blah. You know, a month or two later, they finally said, yeah, yeah, okay. A week goes by and they called, okay, how about three MAC-4s? And they said, oh, let's just shut up. Get off the phone. And they didn't really push that one because I think they were finally embarrassed. But about a year after my project got canceled, one of our guys met the guy that had been pushing the MAC-4s. And he said, you know, you guys made the right choice on that, you know, choosing the Motor 6801. And, you know, he was embarrassed because he was in a position where he could not come out and tell the truth. He was shilling for the MAC-4 group. And he couldn't say what he honestly felt. And he just had to keep going through the motions and just wasting time. And, you know, so that's the opposite thing. When you have these captive groups in your company that have to make sales to you, then they can get in the way of you doing anything as well.

**Chris Gammell:** Yeah. Well, that's like a lot of the incentive structures, right? I mean, like that guy, it's like if you don't sell it, you're fired, right? Yeah. That's obvious. And then, well, let's look at your market. You've got maybe 20, 25 groups totaled to sell to.

**Dave Vandenbaum:** Probably less than that at that time. But there weren't many microcontroller projects going on in AT&T at that time. And, you know, it was pretty thin. So, like I said, when they heard you were doing a microcontroller project, they were on you. I mean, it was like that little Gonzo bird in the Muppets, you know. And he's holding onto your leg and he wouldn't let go.

**Bluetooth Low Energy:** That's awesome. Dave Packer did say that, you know, profit was one of the best measures. Maybe not, certainly not the only measure. And certainly he didn't believe that it was the only measure. But he said that was one of the best measures of your contribution, though. People were buying your stuff. Yeah.

**Dave Vandenbaum:** I mean, I've always said that, you know, your mama will tell you you're beautiful. But when somebody hands you $100 for something that you've done, that's a true compliment. I mean, that's honesty right there.

**Chris Gammell:** Yep. Yep, exactly. Speaking of how goes the FPGA sales these days, Dave. Well. That's a weird one because I assume people are handing you hand over fist money, right?

**Dave Vandenbaum:** Oh, right, yeah. Well, they're handing me hand over fist money, which I hand hand over fist to my ex-wife. But, you know. Well, you know. Well, yeah. You know. Like Bob says, keeping the lights on. That's right. I've, you know, over the past half year or so, I've gotten into working with a fellow over in Portugal, Alvaro Lopez, who did the Zipuino soft core processor. So, I've been kind of integrating some of his work into my boards and using that soft core processor as a kind of an open core alternative to using some of the tools from Xilinx, which are kind of closed up and not that readily available to hack on unless you buy a full license. Interesting. Yeah, I mean, it's really pretty neat. It's all VHDL. It's all open. And you can slide your own peripherals into it pretty easily. And I've got a recent blog post where I just show how to put a very simple RGB LED controller in there that will, you know, just dim and light up an RGB LED with various colors and illuminations and things like that. Just to show how you can make your own peripherals to do things like that and offload the processor. So, all it does is every now and then goes out and pokes it and makes it do its thing, but it's not continually generating PWM waveforms on its own. Yeah. And so, that's kind of neat to work with that stuff and to work with somebody else that has, you know, offloaded a lot of the effort of doing some of the design. And it's just a matter of taking his code and putting it into a little different form and being able to use it. That's always nice to be able to take advantage of other people.

**Chris Gammell:** We're going to quote that one. That one's going to go in a T-shirt. So, Dave says, it's always nice to take advantage of other people. It's always nice to take advantage of other people.

**Dave Vandenbaum:** And I've also gotten a little bit involved with some of the Internet of Things in a peripheral manner. I've been playing around with some of the ESP8266 Wi-Fi boards that have been coming out.

**Chris Gammell:** Oh, yeah. That's the real low-cost chip. Oh, yeah. I see that stuff on Hackaday sometimes. I don't know. I mean, like, that's – oh, no, that's what it was. So, it was someone – one of my friends actually was telling me about the – they passed CE but only on certain models or something weird like that.

**Dave Vandenbaum:** Yeah, and in fact, they probably really haven't passed CE at all from what I've heard on other forums there. But, you know, it's – you're looking at a device that costs now about $2.70 for a board. It has Wi-Fi on it and a programmable 32-bit microprocessor, the LX160, I think, from – oh, who is it? I can't remember. But it's one of those – oh, Tensilica. Yeah, they made it. And you can get in there and Espressif, which is a company that's making the chip, the SOC that goes on there, they've given you a full development environment. You can download a virtual machine that has all the compilers and everything in there. They give you the full source code and people are going in there and hacking this thing out to run the MQTT protocol and run web servers and everything else. So even though it was originally intended as something you'd hook up to the, you know, the serial UART lines to a microcontroller, they're just, you know, getting rid of the microcontroller externally and they're using the one that's right on the chip itself. So –

**Chris Gammell:** Just for compactness of – Oh, yeah. – and lower power, stuff like that.

**Dave Vandenbaum:** Yeah, I mean, it's not a low-power device in terms – you know, it's Wi-Fi. So you're looking at 100 milliamps or more when it's working. It's not like Bluetooth. But it is a pretty cheap way to get going. And you've got to imagine some of these companies that are coming out with Wi-Fi boards now that, you know, that looked really, really low cost, you know, three or four months ago. And now they, you know, they're not looking so low cost anymore.

**Chris Gammell:** So, okay, so if you don't mind my saying as much, taking a step back, the – I don't know how to say this right – the old guy view of IoT. Is it okay to say old guy? Can I say that for the rest of the show? Are we cool with it? Oh, sure. Sure. Okay. Okay. I feel old guy myself a lot of the time. I'll spend the picture.

**Dave Vandenbaum:** No, Chris, you're not old guy. No, I know, I know. Quit trying to steal our thunder. Old guy at heart. We earned our old guy. That's right. No, I get that.

**Chris Gammell:** I get that. So what is the old guy view of IoT? Because, I mean, like you said, I mean, so Dave, you're saying the – you know, this seems like a pretty legit entry into that. We see a lot of that crap that came out of CES. They kept talking about it. Bob, you work on Bluetooth stuff, and that's all, you know, lower energy stuff. What – how do you see it? I mean, like you guys are veterans of the industry. How are you seeing this? How are you seeing it practically implemented?

**Dave Vandenbaum:** I'll let Bob talk for a while. Okay, well – Then I'll steal his ideas.

**Bluetooth Low Energy:** Yeah, I don't have any ideas. The – I don't know. You know, it's – a lot of that's just marketing. Agree. The marketing folks are really excited about it. The –

**Chris Gammell:** I think because – I mean, yeah, you're right because they take it, they bundle it into a thing, and then they call it IoT, right? Yeah, and they want to combine it with – For us, it's like we still need to deal with protocols. We still need to deal with hardware. Yeah. And you can't really separate the two. It's not like everything talks to everything. It's, yeah, well, device A talks to device B because they're both Bluetooth. Well, yeah.

**Bluetooth Low Energy:** VLE, whatever. I think the idea of putting every sensor on the internet is kind of crazy. Mostly, I mean, the way I envision it and the way that I actually implemented for this grape vineyard is for wine grapes. But it is, you know, you have your local sensor network and then a gateway device of some sort that you don't put every sensor out in the –

**Chris Gammell:** Yeah, like hub and spoke basically. Yeah. The hub is doing the communication.

**Bluetooth Low Energy:** Yeah, and people think they can – I mean, a lot of people are really focused on the big data side of it. I mean, the abstraction and so forth is always a good thing and making things talk together and standards. I don't know that there needs to be a standard for IoT. I think most of the – you know, most of what you need is there. The things that have been – that I saw that was pretty exciting was Bluetooth low energy and mainly because smartphones have become ubiquitous. So I think smartphones are a logical gateway device for a lot of it. And the fact that both Android and iOS support Bluetooth low energy natively. So you can just – if you want to hook up a sensor to an iPhone, you just do it through Bluetooth low energy and you can write an app for it right away. And use the power of the smartphone to display your data and to take it up into the cloud if you need to. Makes a lot of sense.

**Dave Vandenbaum:** Yeah, I agree with everything Bob said. In fact, if he hadn't said it first, I would have said that. I believe that. I believe that now that I hear that. Yeah. And, you know, he's right that IoT has become, you know, quite a bit of a marketing term and I think people are throwing it around a lot. But I really do like to see everything that's going on. I like to see the low-cost, low-power chips coming out. I like to see a lot of shit flying around because, you know, a lot of it turns out to be – Chaos creates, right? Yeah, a lot of it seems to be really bad, but there's going to be a few good things in there that are really going to be great. You know, I love the idea of being able to just plaster sensors all over bridges and have them soak up the energy that comes in and be able to rebroadcast information if there's going to be a crack developing. You know, stuff like that is, to me, just the exciting part. I don't really care that much about monitoring my heart rate.

**Bluetooth Low Energy:** Yeah. Yeah, my scale in my bathroom sends my weight out into the cloud every day, which is kind of embarrassing.

**Chris Gammell:** It's all this data we can just ignore on a daily basis. Bridges are falling down, waves are rising.

**Bluetooth Low Energy:** I mean, I got that too.

**Dave Vandenbaum:** That scale wouldn't last two days with me. Yeah.

**Bluetooth Low Energy:** But one of the areas that I found pretty interesting personally is that's related to what Dave was saying is there's a lot of really interesting work going on in energy harvesting. And there's some practical things happening. I've been working a lot with some of the linear technology parts, but everybody has their own versions of it.

**Chris Gammell:** So delicious, so expensive. Yeah, I know. Literally, I love, I mean, listeners know, I am a fanboy of LT parts. But man, every time I see the one piece price on like an online distributor, it's just like, holy shit. Where did they come with that number?

**Bluetooth Low Energy:** Yeah. They provide really good support and the stuff just works is what I've discovered. But the other stuff out there works too. So I don't know. Yeah. But the energy, like I'm working with this new, it's fairly new, LTC 3330. And it's sort of a general purpose energy harvester. So you could hook up a solar cell or a PZO. It doesn't have quite good enough performance to work with thermoelectric generators. Maybe some of the newer ones.

**Dave Vandenbaum:** You know, in terms of scavenging energy, Bob, what is the best source for getting that from the environment? If you had, I mean, solar is obviously a very good one. But, you know, is that the best or is there something else better than that?

**Bluetooth Low Energy:** Well, solar is, well, okay. So it gets into the practical side of it. Like some of these sensors are so low power that you can run for quite a few years on a couple of AA batteries. So there may be no point in doing energy harvesting. But in situations like if you're putting thermal sensors into power transformers up on a pole, it's so application specific that there's not like a, you know, general solution. But like if you have a power transformer, it's generated a lot of heat. So it's logical to think about, you know, doing thermoelectric generation. Right. But this system with just a few square inches of solar cell, and I found these really neat industrial batteries that also are very expensive. But everything I'm doing is very expensive.

**Chris Gammell:** You know people are going to ask for part numbers. I know.

**Bluetooth Low Energy:** Okay. I'll go grab it. But the neat thing about them is they have an operating range from minus 25C to 85C, which means they'll work outdoors around here. Yeah. Pretty well.

**Chris Gammell:** Not around here.

**Bluetooth Low Energy:** Yeah. But so solar, I guess you just have to, a lot of people have been trying to generate or, you know, use mechanical energy to generate power. And I haven't seen a lot of successes there. I mean, more likely, the number one energy scavenging thing has been solar with some battery backup. And then after that, it would be probably thermoelectric generation.

**Dave Vandenbaum:** Yeah. The reason I asked was maybe a week or two ago, I saw somebody talking about energy scavenging. And they were talking about how, you know, scavenging the RF in the air was just much, much, much, much less efficient or, you know, much less power out there than it was from getting something from movement or thermals.

**Bluetooth Low Energy:** I know. You hear people get really excited about they're going to energy scavenge from all the TV signals around. Exactly.

**Chris Gammell:** How close to the tower? Yeah.

**Bluetooth Low Energy:** Well, I've been working with a local university, and they have a pretty good material science department. And they've been building some thermoelectric generators. And one of their projects was scavenging waste heat off of, like, a Humvee. But they're generating, like, a kilowatt of electric power from the waste heat on one of those things. That's legit. Yeah.

**Chris Gammell:** Yeah.

**Bluetooth Low Energy:** So there are applications. You just have to look at each application. Right.

**Chris Gammell:** But it's not Wi-Fi, right? It's not like, oh, you know, like any time you see a Kickstarter or Indiegogo, probably. Yeah.

**Dave Vandenbaum:** Wasn't there the Indiegogo thing that was – or what? It was being funded by somebody, actually, by Hurwitz and Anderson or something with the acoustic energy they were going to beam into, you know, like your cell phone. You'd put it on there, and then the acoustic energy would go into it, and it would charge it up.

**Chris Gammell:** Yes. Listeners of the show will know our ongoing distaste for the U-beam. And U-beam is a – I think they've switched over to an antenna array or whatever that's called, the directed antenna stuff. But it's terrible. One of them –

**Dave Vandenbaum:** Maybe we could just, you know, rub it on our hair and charge it with static or whatever. If I had any hair, I'd rub it on there. Right.

**Chris Gammell:** Well, you have – you both have dogs, right? I mean – I do have dogs. Dogs and horse. Dog hair harvesting.

**Dave Vandenbaum:** He is not sitting still for that shit. Yeah.

**Chris Gammell:** That's what the cats are for. That's right. There you go. Yeah. Just put whatever device you need, like, on the keyboard right when you're about to start writing code, and the cat will be there ready to charge up whatever you need to charge.

**Bluetooth Low Energy:** By the way, these are Tadrin, T-A-D-I-R-A-N, lithium inorganic batteries. T-R-A-N. T-A-D-I-R-A-N. Tadarian.

**Dave Jones:** Hmm.

**Dave Vandenbaum:** Sounds like something from Star Trek. Yeah. I know. It does.

**Bluetooth Low Energy:** And part number TL4935. But they have a bunch of different ones. But they're made in Israel.

**Dave Vandenbaum:** That's good to know. How much did they cost?

**Bluetooth Low Energy:** The battery costs about eight bucks. So, it's pretty expensive. Ooh. Yeah. But, you know, if you're sticking this up someplace that's hard to get, then it doesn't matter.

**Chris Gammell:** Right. What's the cost of a technician going out to switch out the battery, right? Yeah. That's always the measure, is you have to compare those things.

**Bluetooth Low Energy:** Yeah. So, I try to find work that justifies the expensive parts that I like to use. That's good. No, that's really good.

**Chris Gammell:** I think that's because that's where the interesting problems are, right? Yeah. You want to be able to play with the fun stuff. Yeah. It's like, if you're like, oh, well, I need to find a MOSFET that isn't 13 cents. I need to find one that's 12 and a half cents. Yeah. Because. Well, that's its own set of challenges. Yeah. It is. But those aren't as fun, right? It's not like, you know, we were talking the other week about, me and Dave were talking the other week about the R and D type of things, right? Where is the R? Where is the D? The most people in engineering are doing development, right? Yeah. I mean, development is optimizing. It's finding better parts. It's, you know, like all of the things that like, that I think the bulk of engineers do.

**Bluetooth Low Energy:** Smaller or big D. Yeah, exactly.

**Chris Gammell:** Smaller or big D. It's like, it's not as exciting. I mean, I think research on its own is not necessarily exciting either, but ultimately the output is you save some money versus you find, you discover something new. Well. And it's always tough.

**Bluetooth Low Energy:** The way I think about it, because I worked on a lot of technology projects, is that the technology projects take a long time and, but they should pay off over multiple generations of products. Yeah. Like we worked on, I worked on a magnetor resistive thin film heads and that took us 16 years before it was actually in a product. In part because the other technologies that were defending the land that they had were able to keep improving. Yeah. Keep improving. So you didn't, you know, a lot longer than anybody would have thought. But, but it takes, there's different, it's kind of what I noticed at HP, which is kind of fun because it's big enough to, to see different aspects of it was it kind of sorts people too, because if you're willing to go work on something that's undefined, like a technology development project is, and are happy with that, you might feel really too constrained doing manufacturing. On the other hand, I knew people in manufacturing that were just driven crazy by the lack of definition in the technology. Yeah.

**Dave Vandenbaum:** I mean, I, I used to work in, you know, as a faculty member at university and, you know, so that's a lot of research, but I eventually left that because it was mainly looking for money and then, you know, managing people that were doing the research for you and you never got to really do the research. In fact, somebody told me once, he said, well, faculty members really want is they don't want to be faculty members. They want to be graduate students with faculty member salaries. Yeah. They don't want to be the actual faculty member doing, you know. All the grant writing and everything else. And so that's eventually why I got out of it. But, you know, so I'm, I'm more D now than I am R.

**Bluetooth Low Energy:** Yeah. I was a research professor and, and you spent all your time writing grant proposals and doing very little actual work. And the other thing, well, not actual work, that grant writing has certainly worked, but the work that I wanted to do. You want to be doing. And the other thing I didn't like about it was you felt some of these writing proposals felt like you're really doing research for the granting agency. Mm-hmm. And if somebody would clever at the granting agency would ask questions and get all these hundred page reports on how different people would do it and then pick the one that they liked and go after that.

**Dave Vandenbaum:** Yeah. Well, the, the thing I always felt was that when you're writing grants, the only way to get a grant approved was you had to have it all nailed down and done before you even wrote the proposal. Yeah. Because you had to have, you know, all the issues had to be had, you know, you had to have good answers for all the issues. And if you didn't, you were coming up against some other group that had been working in that area for years and they had all the results already and they were just writing the proposal to get money. Yeah. To move, to, to move on to their next project, whatever that might've been.

**Bluetooth Low Energy:** Yeah. It's, you know, it has its pluses and minuses. The thing that I really liked about the university is working with the students and I, but the, I've got a best of both worlds now because my office is just on the edge of campus and I have students that come over and want to work with me and, but I don't have to deal with the university. Yeah.

**Chris Gammell:** That's awesome. Yeah.

**Dave Vandenbaum:** Yeah. I mean, I like the students, but I found, you know, as a faculty member, you, you get a lot more students that were in there for the degree and a lot fewer students that were in there for the learning of what was going on with the degree. Yeah. I had a student come into my office one time and I had a book on my desk. It was about biomechanics. You know, it was an examination of, you know, how different sizes of animals use energy and, uh, and what the effect of different sizes was on the frequencies of various things that went on in their body. And he looks at the book and says, what the hell are you looking at that for? Well, way to show some curiosity there, pal.

**Chris Gammell:** Yeah, right. Been to Wikipedia much? Yeah.

**Dave Vandenbaum:** Ever been on a wiki hole? Yeah. Yeah. It was a long time before Wikipedia, but, you know, we used to have, you know, we used to go to the library every, every week and they would have a section of the library set out for all the new books that were coming in that, that week. And, you know, you could go through there and you could find all kinds of outrageous crap that was just interesting to read about. But, you know, and to be honest, when I was a student, I was kind of like that as well. I, you know, I, I was very concerned with getting the right grades and making sure that, you know, uh, the, the numbers were there, but, uh, it didn't take me, you know, it took me a while to get out of school before I realized that there was more value in the knowledge than the actual grade that I was getting. Yeah.

**Bluetooth Low Energy:** I always thought of myself as a C student and that worked out really well because then I could take whatever courses I was interested in and, and not worry about the grade.

**Dave Vandenbaum:** Well, I, I'll tell you, um, um, when I look at students now, I mean, I, I see a lot of students grubbing for, you know, those, those, you know, all A's and things like that. But a lot of times I've said that if I were looking for a student coming out of school to work for me, I'd look for the guy that had like all F's and one A and whatever he got that A and that's what I try to get him to do for me.

**Bluetooth Low Energy:** It's like you don't want a brain surgeon that's well-rounded.

**Dave Vandenbaum:** Yeah. You want the guy that's showing some real interest in something and is, you know, is willing to work on that to the, almost to the exclusion of everything else. And, uh, you know, the guys that are real well-rounded and get all A's, a lot of times they can say, well, you know, if I don't do good at this, I can always move over to, you know, doing this over here instead. And, uh, so, you know, they don't have all their eggs in one basket. So they're not really worried that much if, uh, you know, if one basket gets broken, they've got another one to go to, you know, it's like all those guys that say, you know, I'm a math prodigy and also I'm a violin concerto, you know, master. So, you know, I can do one or the other. So they end up doing neither and both.

**Dave Jones:** Yeah.

**Dave Vandenbaum:** Anyway.

**Chris Gammell:** I think about the guys that I used to go to school with and, and like, obviously I was not the top student. I, I, I very much recognize that. But then I think about like the guys that I know, I, I, I, I follow them and I, you know, obviously social media makes this easier than it used to be, but like, like these guys, they went to Intel, they went to, you know, like all these high-end companies. And then I look at, you know, what they're doing now. It's just like verification engineer at Intel. And it's like, dude, you're looking like, I know you're great at analog circuit design, but like you were looking at one circuit over and over and over again. And, and, and some people like, I think it's personality type too. I think some of, some of it is that it's like they, you know, they, that might suit them really well, but I don't know. I think, I, I think about what I want to do and it's just like, I want to build stuff. I want to make new things, you know, like, I don't know.

**Dave Vandenbaum:** Yeah. I mean, there, there are multiple ways to success. And the university really only, only rewards one of those ways. And so these guys were successful in the university and now they've, you know, they've gotten themselves into maybe a position that they think is very good, but, you know, you were kind of, you know, you got out and maybe the, you didn't have as many opportunities as everybody else, but you made opportunities as you went along. I mean, The Amp Hour is a perfect example of that. And that's the kind of thing that doesn't get measured very well in a academic environment. Huh?

**Chris Gammell:** No, I hope not.

**Dave Vandenbaum:** No, I mean, that's, that's what I would want in a student is somebody that, you know, makes his own opportunities. That's, that's like, that's the thing. That's what you want, but you can't measure that in the university and you can't assess your program based on that. And when ABEX comes around to accredit your program, they can't see that. So it, you know, it's kind of what you measure is what you get. And if you can't measure it, then you never get it.

**Chris Gammell:** You know, that's, that's a really good point too, because like I, I had forgotten that both of you guys had taught a university as well, um, and various capacities. So let's, let's, let's shift the focus there. I think that's, that's even worth more, more, uh, discussion. What is your take on education these days? I mean, like what, I mean, obviously you've already talked about what, what do you like to see in a student, but what, what do you, where, where do you think we're going in the future? As long as I stay off my lawn, I don't care. That is the correct answer. That's it.

**Bluetooth Low Energy:** You've chosen wisely. Um, sorry.

**Dave Jones:** Go ahead, Bob.

**Bluetooth Low Energy:** Go ahead. Oh, no, I, the students that I have, uh, worked with here that are really interested in the work, um, are as good as students, um, anywhere. And I, I think they're as good as this is, you know, people in my cohort were. So I don't know. Um, what, what I, um, really think is lacking in, um, not so much in college education, although maybe to a certain degree, but in secondary education is the idea that, you know, we're working with your hands is valuable and, uh, intellectually challenging just as much as, as doing some other things that are normally associated with that, like, you know, being good at math. So, um, I, and that's part of the reason why my business is set up the way it is. So I, any prototypes that I need, um, we build them here, um, on site and, uh, keeping my hand in that has been really, I mean, literally has been, is really valuable in terms of design. How do the students know to come to you in the first place, Bob? Oh, the other professors over there, um, know me, of course. And, uh, so the, and they have senior projects. So they're always looking for, you know, sponsors for students for the senior project. Um, and, um, so the, uh, well, I was just thinking about whether I should tell this story or not, but. Oh, yes. That definitely means you should. You can't stop and think about it. Come on. I just had a student over here, uh, the other day that just said, oh, well, I sure appreciate that you took the time to help me. He said, I asked all these other people if they could help and they were all too busy. And I wanted to say, well, that's because they probably didn't know, but, um, you know, there's a, I don't know. Um, everything's, there's good, good side to what they do, of course, too. So.

**Dave Vandenbaum:** Well, I can tell you, I can tell you, you know, a dozen stories like that, but, uh, you know, when I was a faculty member, which was like from the late eighties to the early nineties, uh, you know, we get, every organization has a story that it tells you that is not true. And the story that they, the story that they tell faculty members is, you know, your academic career here is based on three legs on a stool. Those three legs are research, education, and community outreach. Community outreach is helping local companies solve problems if they have them. Uh, education is, you know, teaching classes, just what, you know, teaching students and research is getting research money. Now, the thing they never tell you is that out of those two legs, one is a pine, you know, a pine stump that's about two feet thick. And the other two are like little paper straws that, you know, will not support any weight. And the research is the one, you know, if you've got the research like that, your stool is going to stand. If you're counting on the education and the outreach, you're going to end up with your ass on the floor. And, uh, one time, one time there was, uh, my, when I was married, my wife had a friend that worked at the university. And, uh, one time I come home and my wife says, guess what? So-and-so won a best teaching outstanding teacher award. And I said, she's gone and, uh, sure enough, within one year, she was gone. They drummed her out of the department. And, uh, you know, you know, it's, I mean, I was-

**Chris Gammell:** Obviously she didn't have tenure or anything, right?

**Dave Vandenbaum:** Oh, no, no, no, no. And, uh, but you know, it's, it's, uh, I mean, I was obviously being very cynical, but, uh, as I told my girlfriend once, I said, I'll renounce cynicism when it ceases having its predictive power. And, uh, she was gone. And, you know, and that's what, that's why, you know, Bob gets students funneled to him is because, you know, the, you know, for, for at least part of the reason is that the faculty members, you know, they can't put that down on their resume. They can't put that down on their CV is, you know, I helped student X, you know, solve this problem, you know.

**Bluetooth Low Energy:** Yeah.

**Dave Vandenbaum:** And it, it, it can't be measured. Therefore, it doesn't count for anything. And, you know, uh, but I think, you know, getting back to Chris's original question about how students are, I think, I think there is good or better than they were when I was in school. And a lot of it is that they have so much more access to information than they used to before. Yeah. That's amazing. So much more than, I mean, we used to be stuck with whatever data books were lying around the student lounge. And now, you know, you've got everything. And if you want to take advantage of it, you can take advantage of it. And, you know.

**Chris Gammell:** Let's cover that then. So, so, okay. So the, the, the Bob and Dave, the Bob and Dave method, uh, not, not the Bill and Dave method, the Bob and Dave method. What is, what is the recommended path? Because I mean, like, I, like, I know, I know the statistics of our show. I know, I know who listens, right? I mean, one third is students. Hello, all students out there. Good luck in your finals in a couple months. Uh, but, uh, what, what, what is the recipe for success in your, in your minds? What, what is the best percentage of success? I mean, like, okay. So, so personally, what I think about is obviously I teach contextual electronics. I think about project-based education. I think about making stuff, right? What else, what is, what else is part of that equation? What else is stuff that students should be doing, you know, in or before their senior year of college so that they can, you know, build interesting stuff, get interesting jobs, be, be involved in interesting projects. What, what have you guys seen in your own careers that has allowed you, what has allowed you for success in your own careers?

**Dave Vandenbaum:** You want to go first, Bob, so I can steal all your answers again?

**Bluetooth Low Energy:** Um, well, I was just thinking about, um, you know, I was interested in this stuff from when I was pretty young and got involved in ham radio and, um, like, got my license when I was 11 or 12 and, um, and then that led to working as a technician. I, for me, I think having the hands-on experience, which I got outside of school, I got it working in a TV repair shop and which they don't do anymore.

**Chris Gammell:** Yeah, what is, what is the modern TV? So like, again, doing, doing interviews across, across lots of people, like the repair shop, personally, I started in repair as well. Yeah. Like, I think Dave probably started in repair, uh, Dave Jones, of course. Uh, what, what is the modern repair shop? Does it exist?

**Dave Vandenbaum:** Uh, maybe the hacker space, but there's so few of them around that, that it's hard to get to those.

**Bluetooth Low Energy:** I would say, yeah, building things, um, which is not so much ham radio anymore, although that's still a viable, I mean, if you're assuming you're going into something like electrical engineering, which I guess would be reasonable considering it's the amp hour. Um, yeah, probably, you know, writing software is, is fine. Um, but, you know, I don't know. There's what I think is exciting right now, uh, for students is the idea that, uh, you can go out and for essentially zero money, get involved in developing embedded hardware, um, which is a fairly recent development because even 15 years ago, a lot of the tools would have been out of the reach of students if, if not, you know, a small business like mine. Um, and, uh, taking it and the internet, the internet, there's so many great resources, YouTube, um, uh, you know, I, I learned a lot from watching people's like what you do, Chris, or what Dave does. And, uh, I don't know, get out there and build things and network with people and learn, learn about.

**Dave Vandenbaum:** I've got to, I've got to echo that about what Bob has said there. I mean, when I was a student, you know, you know, 74 to 78, which is, you know, quite a while ago, it was all grades. I mean, you had to grub for me. And, uh, the only way I was going to get interviewed to, to join Bell Labs is if I had, you know, just fantastic grades. Uh, if I had B's and C's in there, I was going to make that. And that, you know, that was back then. But nowadays, to me, that just seems like a death sentence to, to be concerned about the grades. The first thing you should be doing, I mean, the only thing you should be really concerned about in, in your undergraduate is build stuff, build stuff, build stuff. I mean, you should be looking for. Portfolio style. Like. Yeah. Well, I mean, you should be looking for every opportunity to build stuff. If your classes don't have you building stuff, you should be building stuff on your own. You should be finding other people in your class that build stuff. You should be building stuff together. You should be building stuff on your own. And if your grades suffer, then I say, so be it. And that's better. That's better than, than coming out. I mean, if, if a company won't interview you because of your grades, but you've been building stuff and building stuff, building stuff, that's not the company you want to work for. I don't think that, I mean, that nowadays I think that's true. And I mean, if you, and if you don't build physical things, build software, you know, build something. That's because that's where everything comes together is when you had to build something and make it work.

**Bluetooth Low Energy:** Yeah.

**Dave Vandenbaum:** And it's so cheap now. I mean, you've got so much access to so much stuff that, I mean, $10 microcontroller boards that, you know, have 32 bit microprocessors with a megabyte of RAM on them, you know, raspberry pies and everything else. You've got no excuse anymore not to build stuff. But professors do not like you building stuff just, just, you know, at least when I was there because, I mean, it's, well, they can, but that, you know, that, that, I mean, it's, again, it's what you, you know, it's what you get measured by. You don't get measured by building stuff. You get measured by writing papers and finding students to write papers and, you know, funding research projects and, you know, all great stuff. We need research, obviously. But, you know, if you're the undergraduate student and you want to come out with an education, what they need to do for their career is not what you need to do for your career. You've got to show initiative and build stuff, build stuff, build stuff.

**Bluetooth Low Energy:** The thing is, you need both the sort of academic learning, but there's a lot of subtleties. And when you go to build things, you'll find out.

**Chris Gammell:** About project boxes and everything else. Yeah. No offense. No offense taken. I've made a mistake so many times. I just, I'm laughing at myself. Yeah. Oh, no, you have to be able to laugh at yourself. I'm trying to see what I'm thinking in my head right now.

**Bluetooth Low Energy:** Yeah. I was going to say that, you know, having that desire to do it versus just deciding, you know, what's going to make you the best, the most money as a outside, you know, in your career is a big indicator of who's going to be successful. If people are doing it because they just want to do it, in fact, not want to do it, they sort of almost have to do it. And there's nothing that could keep them from doing it. Those people would do a lot better than the people that just, you know, look at, you know, all the different possibilities and decide on electrical engineering because that has the highest income. Doing things that are hard to do is always good because those act like barriers to entry. And usually getting paid well follows that. Hey, you're shitty at this. You get an F.

**Chris Gammell:** Yeah, I know. Well, this is now a barrier.

**Dave Vandenbaum:** Yeah. You know, it's like what they said on Adventure Time, you know, sucking at something is the first step to being kind of sort of good at something.

**Bluetooth Low Energy:** Yeah, you really have to be willing to take risks. And part of it is being willing to fail. And like, I was only half joking when I said that I thought of myself as a C student, because if you are the sort of person that has to have an A, then you'll usually, you know, be cautious about what courses you take. Exactly. Exactly. Exactly. And, of course, I was, my dad sent me all my report cards from elementary school and I was looking through them and they had interesting comments like, Robert has to be separated from the other children. He would rather fiddle with clay than pay attention and looks out the window. So, sounds right. Yep, yep, yep. So, anyway.

**Chris Gammell:** I think throughout the ages, the only thing that changes is clay gets replaced with Legos, gets replaced with, you know, Arduino and everything else, right? Yeah. I think these are just the non-permanent thing is the item being fiddled with, right? Yeah. So, the other question I wanted to talk to you guys about is, so you were talking about the need between fiddling on your own and that kind of idea. And one thing we had talked about over email, the balance between, you know, being in a small company versus a big company and, or even being on your own. And I'd be kind of interested about how you guys feel about that. I mean, you've both been, you know, in the big organization, been in the small organization, been on your own. How have you balanced that and how do you see that balancing going forwards? You know, like, how do you see people acting as individual agents or as part of an organization going forwards?

**Dave Vandenbaum:** Well, certainly, individual agency has become much more possible, you know, over the years than it was, you know, quite a while ago. But I started off in AT&T at Bell Labs and, you know, that was just awful. I mean, you know, we had...

**Chris Gammell:** Because that's pretty, that's pretty much like, you know, we talked to Shariar as well, right? He was, he was, he's part of Bell Labs still. Like, it sounds awesome in parts of it, right? Yeah. Like the parts are like the research and the being around smart people. That part's great. Yeah. But...

**Dave Vandenbaum:** Yeah. That, you know, that'll last you two weeks right there. But, you know, it gets, it'll get to you after that. The problem that, that we had where, where I was is, you know, we had a lab that was almost, you know, when I left it, it was almost 500 people. And I think I could count, I could count on the fingers of, you know, of one amputated hand, the number of projects that actually went out and became real products that people could buy, you know, and use because it was start a project, you know, start a product, get people on it, work it for two years, cancel. I mean, it was over and over and over. I mean, we even had a song that we would go by and sing to people when their project was canceled because it was just so common that we just had to have, you know, we, we came up with something and it was just...

**Chris Gammell:** Well, we need to, we, wait, hold on, hold on.

**Dave Vandenbaum:** Oh, you don't want me to sing it.

**Chris Gammell:** I think Bob will agree with me that we need to hear this song, right? Bob, I mean...

**Dave Vandenbaum:** This is... Come on. Do you really want to hear this thing? Yeah, no, I really, really, really want to hear it. It's only, it's only like, it's only like four verses. I don't care. Just go ahead. This is a song that Ron Meyer and I...

**Chris Gammell:** We'll pretend we're going to edit it out, but we're not going to.

**Dave Vandenbaum:** Yeah, yeah, please. This is... I mean, when I sing, my girlfriend's daughter says, oh, please stop. But this is a song that Ron Meyer and I came up with, you know, and it was sung to the tune of Johnny Carson's theme song, which probably nobody listening to this remembers except for me and Bob. Yeah. But it was...

**Chris Gammell:** Wait, what's the theme song?

**Dave Vandenbaum:** I don't know the theme song, but... The theme tune, or, you know, it didn't have any words to it, but it was... And, you know, Johnny would come out and he'd do his golf swing and that kind of thing. So, Ron and I sat down one day and we heard about a project get canceled. And I said, you know, we ought to have a song for that. So, we started, you know, sitting in our office. He said, your project's canceled. You know, I'm getting things out. What comes out of that? So, he said, your project's canceled. You're out of a job. You thought you were hot shit, but you were dead wrong. That's about as far as we got until somebody in management came by and broke it up. But, yeah, I mean, it was just... It was just... It was just like two years, you know, and you were done. And it's like management, you know, I'd like to think they had a concrete reason for canceling it, but a lot of times it looked like they just got bored. They said, ah, we've been working on this for a while. Let's just can this. Something new. Hey, there's something neat to do. Let's do this over here. Yeah. You know, it's just so debilitating after a while. You know, it's just tough.

**Bluetooth Low Energy:** One thing that we used to do at HP that worked pretty well in the old HP was something called the Next Bench Syndrome of product development. But the idea was that you'd develop a tool for some problem that you wanted to solve and somebody... But you'd... Or rather, you'd develop a tool that would solve a problem for the guy over on the next bench. You'd find customers and you could check whether you were doing something that was to be worthwhile or not pretty quickly by finding local customers and getting that feedback. But that gets... The whole thing gets into... I mean, because I was on, you know, several projects that were canceled as well. In fact, the one technology project that I worked on, we worked on for 16 years before it actually got into a product. But it just brings up the idea that you've got...

**Dave Vandenbaum:** They would never have gone 16 years wrong. Yeah. Well, we had... It probably got 16 months.

**Bluetooth Low Energy:** It got canceled several times, but I just kept figuring out ways to stay involved with it.

**Chris Gammell:** You rename it each time you're rebranding, right?

**Bluetooth Low Energy:** Yeah. But no, there was good reasons for why it happened the way it did. But the thing is that what makes a thing a success is not just the idea, but also the execution. And part of the execution is, you know, making sure that you're addressing a real problem for people. And that could be where it gets a little bit lost in big companies. One of the things about big companies is that, well, there are certainly a lot of things that require a big organization to do that an individual or a small group of people probably couldn't do on their own. And mostly, it revolves around setting standards for things. But anyway... Exactly, yeah. Which standards are definitely important. I mean, PCs didn't take off until Microsoft kind of got set as the de facto standard. Right. But...

**Chris Gammell:** It takes a lot of money, too. I think that's kind of an underlying thing, right? A lot of people. Yeah. I mean, maybe not these days, but I think...

**Bluetooth Low Energy:** Yeah, I think there's still projects. Like, if you're building a rocket to go to the moon, you know, 10 guys are not going to do that. But... Right.

**Chris Gammell:** Yeah, SpaceX is not a small organization by any stretch.

**Dave Vandenbaum:** But it's smaller than what NASA originally started off as. Yeah, that's true.

**Chris Gammell:** But it also doesn't have all the spurious... I mean, like, it seems like the Bell Labs project you talked about, Dave, where, like, the... Like, I hear about... NASA has a research center in Cleveland, like, NASA Glenn. Mm-hmm. And I hear about that stuff, and it's like, you know, we're talking about lasers and all these other things. It's just like, what the hell does that have to do with going to space? Like, I get it. It's cool. It's awesome. It's probably related to the future.

**Dave Jones:** Mm-hmm.

**Chris Gammell:** But it's not about launching a thing into space, you know? It's not like getting off... It's... Getting out of Earth's gravity's pull, right?

**Dave Vandenbaum:** Yeah, it's probably, you know, something that they're working on in concert with another, you know, government lab, and they're able to share some funding on this or something like that, that, you know... And that's where it is. It's the money aspect, right? Yeah. They got to get money in the door, and that's the way to do it.

**Bluetooth Low Energy:** Yep.

**Dave Vandenbaum:** But, I mean, you know, talking about, you know, big companies, the thing about big companies is, you know, when you're a small company, you know, think of it in terms of cell size. When you're a little tiny company, a little, you know, like a little cell, most of you is surface area. So that means that everybody in the company is kind of like on the surface, and they're all seeing, you know, the application for whatever they're doing. They're interacting with customers. They have pretty much a direct line to the lifeblood. The lifeblood of the company, which is...

**Chris Gammell:** Everybody has a Twitter account. Everybody is listed as the main contact. Yeah.

**Dave Vandenbaum:** And you see the customers, and you see what's going on, and you see, you know, this is how I impact this. And if I don't do this, then it's going to have a bad impact. If I do this, then it's going to have a good impact. But, you know, when you get into being a big company, and then you're a great big cell, and then you have the surface area to volume ratio is going down a lot. Now there's only a smaller portion of people on the surface that see where the rubber meets the road.

**Chris Gammell:** Now the goddamn mitochondria, right? Yeah.

**Dave Vandenbaum:** And now you're stuck over there in the goddamn endoplasmic reticulum, and you're saying, well, what the hell am I doing over here? So you say, well, I don't look very important over here. You're just, you know, combining these little molecules. I'd better grab some more bigger molecules, and, you know, maybe I can gum up the works over here for a while. I should frigging mutate. Yeah. I should replicate quickly. Yeah. I'm going to divide this nucleus. You see if I don't. That's right. And it's just, you know, then they have to do things to justify their own position. And again, it gets back to what you measure is what you get. And you have a hard time measuring those internals in there, so they have to do something. And so they start doing things that can be measured, and that's where everything kind of goes to hell. I mean, you know, with a small company, you know, if you miss the ball and it goes between your legs, it's going to roll all the way to the outfield wall, and that's what you worry about. But with a big company, it's like what you're worried about is one of your teammates is going to grab the ball, and he's going to throw it into the outfield fence, and then he's going to blame it on you. That's right. So there's a lot of, there's some good things about big companies in terms of being able to get hold of those big means of production and having some significance out there. But there's a lot of, it comes with a lot of negative things as well that you have to, you know, that can be very debilitating.

**Bluetooth Low Energy:** If you get in the right situation in a big company, it can be pretty nice. Yeah, like CEO. Well, I was thinking about when I was working at HP Labs, but CEO would be nice too. It'd be more lucrative.

**Chris Gammell:** Someday, someday, you know. We aspire to that.

**Bluetooth Low Energy:** And a small company has its downsides too, because you've got to do everything. So I've got a lot of bookkeeping to do that I don't necessarily like, but you have to do that.

**Dave Vandenbaum:** Yeah, or when the U.S. post office decides to change its web interface for figuring out, you know, postal fees for shipping packages, and then, you know, they send you an email and they say, oh God, here I go.

**Chris Gammell:** Yeah.

**Dave Vandenbaum:** You know.

**Chris Gammell:** Did you guys ever think when you were in school for electronics and stuff like that, and you'd be like, and someday, I will be worrying about the best logistical option for my, the widget that I took, you know. The thing that took me 20 hours to develop and debug now takes me 100 hours to ship and optimize logistically.

**Bluetooth Low Energy:** Well, I mean, that's part of the fun part of it, is doing everything, if you like that, on the other hand.

**Dave Vandenbaum:** Yeah. I mean, there's a lot of, I mean, you know, I've learned a lot about managing a website. I can't, I mean, a lot of that I like, but a lot of that I don't like, especially when it goes down because, you know, some service provider is not doing their, you know, has changed its interface to me, and that's a problem, and then things are offline again. But, yeah, I mean, you know, probably it's a better, a good thing that we can't really see into the future, and it's probably also a good thing that we can't revise our past, but, you know.

**Speaker ?:** Yeah.

**Chris Gammell:** Well, so, Bob, you, so the reason this whole conversation, literally this whole conversation, listeners, this whole conversation started because Bob and Dave on Twitter were talking about this stuff, and it was about possibly, you know, moving from, you know, smaller private enterprise back into a larger corporate enterprise, and kind of that discussion, and so... There are days that that seems appealing. Well, yeah, it's kind of a grass is greener thing, right? I mean, so let's talk about that. From an engineering perspective, is there one you prefer over the other, or, you know, like, so say you were, say you had an intern come into work for you, and then after they were done, they're like, all right, I'm going to look for a job now. What do you recommend to them? What is the thing that you say, this is your best shot going forward in 2015?

**Dave Jones:** Oh, gosh. Your best shot. Come on, guys.

**Chris Gammell:** I need a job. Give me a job. Come on, guys.

**Bluetooth Low Energy:** Well, I think you can go work for a big company and learn a lot of things, and then go out on your own if you want to later. I don't think it's changed from when I was starting out a lot. I mean, there's a lot of opportunity in big companies right now, and in fact, it's probably easier as a young person to get hired into a big company right now.

**Dave Vandenbaum:** Yeah, once you get a few years on you, they would probably rather pass on you, because you kind of know what they're all about, and they can't run the same game. I think you're old and in the way. Yeah. Well, you're old, expensive, and in the way, and you don't take shit anymore.

**Chris Gammell:** Yeah. Yeah. Personally, for me, the sweet spot was that you always see the job listings of two to five years. That was the big one. It's like, if you have that two to five years in the relevant field that you want to eventually be into, you're going to get a pretty decent offer, and then from there, you can kind of turn that around however much. But I think then, once you're past the 10-year mark, it's like, oh, well, this is a grizzled veteran. Yeah.

**Bluetooth Low Energy:** Well, that's because they have, like...

**Chris Gammell:** Say that to a doctor, right? It's like...

**Bluetooth Low Energy:** Yeah, that's because they have 20-year-old political science majors in the HR department or something. Right. Right. Exactly. There's a lot of stereotypes of engineers, too. Yeah.

**Chris Gammell:** It's true. Yeah.

**Dave Vandenbaum:** I mean, your best bet is to have somebody on the inside that is technical that you know that will grease the way for you. Networking's essential. Yeah. And, you know, that gets back to being visible online nowadays.

**Chris Gammell:** What is the way that you guys define... How would you go about networking these days? I'm not a good person to ask that question.

**Dave Vandenbaum:** I'd do the best work that I could, that I could talk about, and I would put it out online and try to find other people that have problems and try to help them solve those problems. And also, when people, you know, when people get in contact with you and ask for help on things, you know, make sure you give them a hand to try to help them out. But, you know, also look out for the student or, you know, the person that just wants you to do the whole prosy form. Yeah. You know, don't get roped into that.

**Bluetooth Low Energy:** What I was thinking about also was this whole idea of open source and the idea of publishing all the details and helping people. And what I've found is I get back a lot more than I put out there. And I try to be a good citizen. But it's just, that's just the way it works because there's, I try to explain that to people who think about more of the traditional approach, which is, you know, to patent everything and keep all your intellectual property secret. They just don't get the idea of open source.

**Dave Vandenbaum:** But patents are like, you know, what they say is $10,000 to get a patent. But $100,000 to defend it for the first time and then it's worth something.

**Bluetooth Low Energy:** Yeah. You know. The, yeah, that's another thing in a startup I wouldn't really, I mean, you have to protect your intellectual property, but I wouldn't put my emphasis there or think that I was going to, you know, keep everybody out because of my great IP. The, yeah, if I always tell, I always tell people, because I get a lot of people who are interested in doing startups coming around too. And, and I've had some major failures as startups and that's where I learned the most. It was really painful. But one of the things that's really important to keep in mind is that the value of something is really the idea times the execution. And if you have a great idea, but poor execution, that's not worth very much. And so learning to execute is critical.

**Dave Vandenbaum:** So, um. Right. And the, and the thing is, especially when you're executing on products that are going out to people is that 90% of your execution better be in the last 10% of that project because that's when it fails.

**Chris Gammell:** Like the, uh, the, the box that it goes in and the response emails or what?

**Dave Vandenbaum:** No, not the box, but at least the. I mean, that stuff matters still, right? It doesn't matter, but the, the, uh, experience the customer is going to have when he unpacks that product and tries to get that thing to work, is that going to be an easy thing or a hard thing? And how many, you know, they say that, that every slight bump in terms of getting from start to finish there costs you 30% of the people that would use it. So if you had three bumps on the way, then you've lost 90% of who's going to use it. And, you know, and those bumps don't have to be very big, you know, and like, oh, I need a 3.3 volt AC power supply to run my board. You know, who has one of those sitting around? That's a bump, you know, and then you, then you lose, you know, people throw, you know, throw it in the side and the desk door and say, I'll get back to that when I get my 3.3 volt AC power supply. And, you know, then another bump comes after that where, oh, you don't have a certain library installed. There's another bump, you know, and then it just keeps on going to you, you know, and, and that's where a lot of your customer support calls come from. It's just, you know, those little bumps that come along and you better fix them or else, you know, they may seem mundane and they may not seem like they take a lot of brain power to fix, but if you don't pay attention to them, they just eat you up.

**Chris Gammell:** I was talking to my buddy who has a 3d printing company, but he prints out, you know, parts of a 3d printer and ships them to people. And we were talking about a lot of that. It was just like the, you know, a lot of the times it's the, it's the supporting and the handholding that'll get you the most sales. And that's going to be what gets you the, the bulk of things. And it's not about how, how great your printer is. It's not about how great your electronics are. It's about how well you support the customer. And that's, and that's, I I've never heard of anything like that in a school or anywhere online. I mean, like you just don't learn that until you're in it and you're in the thick of it. Right.

**Bluetooth Low Energy:** Part of it's because school is very much an individual, you know, getting information into your brain and there's not a lot of teamwork. That's one thing that school should have more of. And actually the school does have a certain amount of some places, some places more than others, but. Yeah.

**Dave Vandenbaum:** And about 20 years ago when I, when we went through an ABET review at my school, they were just starting to emphasize design projects and design teams in, in, you know, in the senior year capstone courses. And, and, you know, that's, that's important. And that's a lot, there's a lot more of that now than there used to be. But at least when I was there, they just, you know, that work was scut work. You know, if you're a professor, you did not want to get involved with that stuff. So they, they tried to push all the senior design projects onto like one or two guys. And, you know, they were adjunct faculty because, you know, they didn't have to publish research or anything like that. And they could handle that. And they just burned those guys out. I mean, they were doing, you know, great work helping the students and everybody loved them, but they just get burned out by it all. So, yeah, but yeah, those, those, those team designs are really important for students, you know, and it's, again, it's building stuff, which is always important.

**Chris Gammell:** Yeah. That's, that's the real, that's the real world stuff, right?

**Dave Vandenbaum:** I mean, that's kind of, you know, it makes the academic stuff, you know, it, it, it gives you a place to use it and see why it's useful. And, and I mean, we talk about that, you know, I mean, that's being talked about a lot more in terms of getting students into engineering, right? You know, you gotta, you gotta make it seem applicable somehow. You know, it can't just be sit down and do your math and then there you go. I mean, you know, everybody has a problem with that, but so, so you have to have, you have to have some application and if you have to provide it on your own, then, you know, so be it. And having, having hackerspaces inside a university would also be a great thing to have, you know, because that would offload, that would offload the, that would offload some of the professors having to do all the work. I don't remember, are you guys, are you guys hackerspace members in your local areas? I don't have one close enough to me. The closest one is over in Durham, which is about 40 miles away. Just can't, can't make it there often enough to make it worthwhile.

**Chris Gammell:** In the boonies, huh? Yeah. Yeah. I'm out in Idaho. But we do have a hacker. Idaho is just boonies.

**Dave Vandenbaum:** You're close to a university, right? You said you're across the street from a university.

**Bluetooth Low Energy:** Well, up the hill, but there's, we do have a hacker space here in Boise. I haven't been, I've been involved with it. My biggest problem is time these days because I also have, you know, three kids and horses and dogs and all that kind of stuff.

**Dave Vandenbaum:** So, got to get rid of those, got to get rid of those, Bob. Oh, the kids, the horses and the dogs are awesome, right? Can you get the dogs to eat the kids? Yeah, the problem is the kids keep coming back.

**Bluetooth Low Energy:** I keep thinking they're going to go out into the wide, wide world and then they come back.

**Chris Gammell:** Feed yourselves, good Lord.

**Dave Jones:** I know. I was thinking that there's... Move, Bob, move. I know. They keep finding me. That's the problem.

**Chris Gammell:** Stop attaching your location to Twitter, man. Yeah, I know. It'll help, you know.

**Bluetooth Low Energy:** There is a big difference between different companies, too, because, and one of the things about a, just switching subject real quickly, but one of the things about, a smaller company or a company that's not publicly traded is, it's oftentimes a lot more clear at the end of the day what you did, how it advanced the company, especially in a small company or a startup that's real clear. And a big company like HP could do great work and the stock could still go in the tank because it's driven mostly by what's going on in Wall Street. Yeah.

**Dave Vandenbaum:** Especially nowadays.

**Bluetooth Low Energy:** Yeah, so that's pretty frustrating. It also drives a lot of bad behavior in the bigger companies, but that's a whole other subject.

**Dave Vandenbaum:** Well, you know, you're talking about working at HP. I'll give you one compliment is that at my Bell Labs location, you know, the department heads would take a page out of HP's book and they would do the management by walking around thing. Oh, yeah. Oh, yeah. Yeah. I mean, that was, that was helpful. I mean... Management by wandering around. Yeah. Actually, there's a... That...

**Bluetooth Low Energy:** Sorry. Go ahead. Oh, there's a wonderful video that was put out and I wish... I should just put up on YouTube and then ask permission later. It was done by HP, but it was a retrospective of Bill and Dave and a lot of historical footage and a lot of them discussing why they did what they did. And it's very different than the HP of today once they weren't involved in it anymore. Actually, the thing is, between Bill Hewlett and Dave Packard and I, we used to have over 50% of the company ownership and... Oh, yeah.

**Chris Gammell:** You tipped them over that edge. Yeah, that's right. Good for you, man. You know what? That three-person team is unstoppable. Right.

**Bluetooth Low Energy:** But, you know, as soon as it became mostly driven by Wall Street, it really changed things. Computers and everything else. And then you get the... It's this class of people that are kind of like pirates that are on the board of directors and scratching each other's back and it's not good. Oh, yeah. That's why I was thinking there are... On the other hand, I found companies and an example is Seagate. Which is a pretty big company, but it really runs a lot like the old HP. It's also a private company. So they can do... They can have a longer-term view. That's the thing about the publicly traded companies. They tend to be driven by the next quarter's results. And they do screwy things to make the numbers look good.

**Dave Vandenbaum:** I remember one...

**Bluetooth Low Energy:** Oh, sorry.

**Dave Vandenbaum:** I mean, that's really a result of a... That's the result of good intentions on, you know, or unintended consequences and good intentions. It's that, you know, long ago when companies were, you know, sold stocks and bonds in themselves, then they would take the money from the investor and then they'd just go off and do whatever the hell they wanted. And finally, Congress got involved in that. And then they, you know, they maybe have a legal responsibility that you had to maximize shareholder value. And so when you turn around, this is what you get. And so, you know, you got to be careful about good intentions. Well... But anyway...

**Bluetooth Low Energy:** Yeah, right. Yeah, you got to be careful what you measure because people tend to behave according to how you measure people because they'll behave according to how they're measured.

**Chris Gammell:** Well, and how you incentivize them too, right? Because ultimately that's what it comes down to is what is that person's paycheck? It's like if the CEO gets a, you know, 20% bonus on a, you know, $10 million salary, it's like, oh, shit, you know. Yeah, but if, you know... Two and a half million extra to fire a thousand workers, like, well, I don't really talk to them. But, you know, the older way of doing it was, here's your pink slip.

**Dave Vandenbaum:** But if your shareholders can sue you because they think you're, you know, they're making 18% when they really could be making 20, you know. Yeah. Then as a CEO, you know, if your job is on the line all the time based, you know, looking at that shotgun point of that, you know, you're going to give them exactly what they want, what they can measure. And everything else be damned with it. So that's why you get into these situations. But anyway...

**Chris Gammell:** And ultimately we talked about the research dollars there, right? Because ultimately that's what drives a lot of the engineering stuff is, you know, that's kind of the first thing to go is like, well, we can't, we cannot, you know, take this risk. It's always about risk. And we can't take this risk this quarter and blah, blah, blah, blah, blah. And that's when all the interesting problems go away because we're just going to rest on our laurels and keep just maximizing shareholder value by reducing costs, blah, blah, blah. And it's like, you know, as an engineer, you know, okay, maybe I hold stock in the company I work for, but ultimately what I care about is, are interesting problems coming down the pipeline? You know, do I get to work on interesting stuff? Right. And that really hurts when that doesn't happen.

**Dave Vandenbaum:** Well, there's a book written by a guy named Quigley, which is something about the collapse of civilizations or the ascent of civilizations or something. And he, he points out that any civilization that is rising has three things going forward. It has people that are incentivized to innovate. It has surplus resources that don't have to be used today. And it has a, an agency somewhere that is willing to invest that surplus into those innovative ideas. And, you know, what you see in a lot of companies is, is they, is they have the surplus and they have people with the innovative ideas, but they're not willing to put the investment into those innovative ideas. And that's when the companies start dying off.

**Chris Gammell:** And that's what you hate to see, right? I mean, like, obviously, Dave, you work for Bell Labs. I mean, Bob working for HP. Like, we've seen that in both of them, right? Like, there, there are still, you know, pockets of, of innovation, interesting things, but it's like, it's, it's just about ultimately what is the, what are the long-term goals? Or, or maybe even what are the, you know, the absence of long-term goals in the, in the blind, the blind chase after interesting things. Right. You know, like that, it's, it's hard. I mean, like, it's hard, it's hard with that focus on, on the, on the profit side of things, because ultimately the things that create the longest term value are going to be the things that are never, ever, ever, ever going to be, you know, a good decision to short term. Right. The semiconductor would never have been invented otherwise.

**Dave Vandenbaum:** Yeah. You had to have a guy with some vision there. But, I mean, when, when AT&T was broken up by Judge Green back in, you know, with a consent degree back in the early 80s, you know, all the division just went spinning out into different places. And, and we ended up in a company called, I think, American Bell. And they gave us all key chains on the, on the day we joined that, you know, company. We were in the same place, but it was a new company, kind of like, you know, different trees, same monkeys. Yeah. Yeah. And, and so they gave us these key chains and chains. And, you know, about a year after that, I, you know, when I left the company, but, and, and years later, I still had the key chain. And I, and I used to take that out and I'd show it to people. I'd say, you see this key chain? This key chain lasted five years longer than the company did. The company was gone in a year, you know, and it was reabsorbing something else. And, you know, just, just people, you know, they just mismanage things. They think that they, that they know what's going to happen when they get out in the competitive world. And they don't, they, you know, they weren't ready to, they weren't ready to be out there. But anyway, you know, that's big companies.

**Chris Gammell:** Yeah. So the last question I wanted to ask you guys, I know this is very, very nebulous, but where do good ideas for electronics come from? Where do you guys draw inspiration from? Where do you, you know, when you're, when you're thinking about a new project, what are the resources you use? What are the, you know, what do you draw upon in order to find new innovations?

**Dave Vandenbaum:** Hmm. I look for what's close to what. You know, I, I have a lot of things that are kind of scattered around and I say, you know, well, what's close to what, what, you know, here's this thing, here's that thing. Can they, can they be put together somehow? Do they, do they cooperate with each other in some way? Are they completely different? If they're completely different, how do I, you know, how do I make them work with each other? Does it even make sense? And, you know, you get a lot of really, just a lot of really bad ideas. But every now and then one of them, you know, one of them works out and you can, you can develop a little bit. But, you know, it's just a matter of being around a lot of stuff. And, you know, I've got a lot of stuff on the internet that, that comes flying in every day, you know, through Feedly. And you look at it and say, that's interesting. This guy's taken this and this and he's done this with it. You know, so how does that apply? You know, where does, so most of my stuff is, you know, kind of application oriented. You know, it's not research oriented. It's development oriented. How do I put things together? How do I, how do I make something that's going to be useful to somebody else?

**Bluetooth Low Energy:** Yeah. Yeah. I think finding, I mean, I, I try to find problems that are, that people have and then see if there's a solution to it in the things that I'm working on and interested in. And it's really tough. And a lot of, we were talking about internet of things earlier. A lot of this stuff, a lot of technology is just a solution looking for a problem. And that's a terrible place to be. Right.

**Chris Gammell:** It's a cognitive surplus plus money surplus plus whatever else.

**Bluetooth Low Energy:** So I guess you have to be, I was trying to think of the word, but, you know, gregarious enough talking to people and, and testing ideas that you might have. I mean, well, you know, for example, one of the things that I got involved with early on in this company was developing a system to measure how hard football players get hit. And, and, yeah, I got an award for that. But the, but it has not sold. And part of the reason is because that industry reminds me a lot of the tobacco industry. They're just in denial about concussions. They don't want to admit to him. And so we had, you know, a device that.

**Chris Gammell:** Well, people probably just get dumber over time. It's probably not about the, you know, full contact.

**Bluetooth Low Energy:** What they say actually is even more insidious than it. And it's exactly like tobacco industry. They say, well, we know that concussions are a problem, but the science is not yet good enough to really set us. Oh, my God.

**Chris Gammell:** Well, this is a personal choice that they make on their own. And, you know, there's nothing addictive about the money involved in football.

**Bluetooth Low Energy:** So even if you find a problem that you think is a good one to solve, unless everybody else agrees, you know, it's just not. But if you can't, if you can't sell, I mean, you're trying to sell that to schools, right? Well, we, yes, mostly moms, probably.

**Dave Vandenbaum:** Yeah. I mean, is this the kind of thing that, is this the kind of thing that's small enough and easy enough to install that somebody could buy one and install it in their own helmet?

**Bluetooth Low Energy:** Well, the thing is, actually, just go, the one that I was working on, the version of it went in the chin cup. And it does a great job. And I spent a lot of time at Wayne State University in the injury biomechanics lab and also another company called Biokinetics testing this thing. And we used a thing called the head injury criteria, which was developed for studying blunt force trauma in automobile accidents and has a history that goes back to the 50s. But then you try to sell it to a sporting good company. And everybody's worried about getting sued, of course. But then there also, you hear people in the… What are they worried about getting sued about? Oh, well, they might be worried because you say this detects concussions. And it doesn't detect concussions. All it detects is the… Right. You got a hit at a level where 50% of the population would get a concussion if they got hit at that level. Right, right. There's microscopic details about the brain and individual differences that make a big difference as well. And there's just a lot of details and things that you can't control. But with the head injury criteria, you can set it at a level that says, well, we'll alert you if you get hit at a level where 50% of the people would have a concussion. And then the idea is that you go off the field and they check you to make sure. But the protocol now, if you do get a concussion, is to rest for a fairly long period of time.

**Speaker ?:** Oh, yeah.

**Bluetooth Low Energy:** Yeah, it's a long time. So, if you're a senior in high school, there's just a lot of motivations to not… They just don't want to know. Because if you're a senior in high school, you could miss most of the season and not get a scholarship.

**Dave Vandenbaum:** Have you actually thought about or looked at actually selling these things to the parents of the kids?

**Bluetooth Low Energy:** Well, I did the work as a… I developed a product for a sporting good company back… I know that they spend a lot of time trying to figure out how to gain traction. And they just haven't. And I don't think it's because they're not good at selling stuff. Because they sell a lot of other stuff. Yeah, because if I was a parent, I would want to know. Yeah, I know. Even if my school didn't, I'd want to know. Well, in Idaho, there's actually a law that says that if you get a concussion, you have to take care of it. But there's just not the… You know, it's actually the parents and the students and it's everybody. And at the pro level, there's a lot of money. The money is probably at risk at every level. But anyway, it's just… So you can have a great idea that's solving a real problem in the world and still not make…

**Dave Vandenbaum:** Maybe you should go and start marketing it to the soccer people because they're always hitting things with their heads.

**Bluetooth Low Energy:** Yeah, any sport, I think you're going to run into the same trouble. Yeah, yeah. But who knows? Those Europeans, they might buy it. Yeah, they might. But it's… So there's a lot of things outside of your control that determine success. And a lot of times, the business pornography industry always writes in a real linear way. I did this and this and this and then I was hugely successful. And you get the idea, well, if I just did the same thing in the same order, I would also be successful. Right.

**Chris Gammell:** It's like formula, right? Yeah.

**Bluetooth Low Energy:** But it doesn't work that way. And people don't give enough credit to sort of the serendipity that… Yeah, yeah.

**Dave Vandenbaum:** And the other thing is what we've learned from TV is aim for that lowest common denominator. I always tell people that, hey, you developed a neat electronic thing there, but nobody's going to buy that because it doesn't have an LED that's flashing on it or something like that. I mean, I hate to say that about people, but that's the way a lot of people are. If it's not flashing an LED, it just doesn't get over the threshold no matter what else it's doing. And it's just… I mean, it's just kind of a weird mindset, especially in people that are pretty smart in what they're doing that sometimes you need to have, you know, that little bauble that attracts the bird and then he'll bite out it and he'll swallow it.

**Chris Gammell:** Yeah, it's tough too. I mean, like, it's the broad-based marketing side of things, right? It's like you kind of have to take… You have to make a decision up front. It's like, okay, I know this is going to be a niche product. It's not going to appeal to the masses. And you have to be okay with that, right? Yeah. And you have to be like, okay, this is meant for a very specific group and you can't be drawn in by all the BS online about, oh, well, if you're a startup and you get… What if you got 10 million page views and then on that 10 million page views, a million people brought your product at $10? You'd have $10 million. Oh, yeah. Oh, I could be rich. And it doesn't work like that. It's like you have to… If you're going to pick a… You know, especially for hardware, I think, and especially for this kind of niche hardware, it's like, yeah, you have to solve a problem, right? That's ultimately what… That's what we're on this planet for is to solve… Engineers as an archetype is that we're on this planet to solve problems. Pick a problem. Go solve it. Figure out the money later. That's ultimately what it comes down to. Right.

**Dave Vandenbaum:** You've got to be interested in your solution before you can try to interest anybody else in it. You know, if you're not interested in solving the problem, then chances are you won't be able to interest anybody else. A marketer may be able to do that, but you wouldn't. Right.

**Bluetooth Low Energy:** Flipping it around, you could say that if you can work on lots of different things, why not work on the things that people are interested in?

**Dave Vandenbaum:** Yeah, if you know what those things are. And it's hard to get people sometimes to tell you what they're interested in because they don't know that they would be interested in it because they'd never seen it before. You know, like the old Henry Ford quote, if I'd asked people what they wanted, they would have said a faster horse.

**Chris Gammell:** Yeah, better buggy whips. Yeah.

**Dave Vandenbaum:** That's right. Yeah.

**Chris Gammell:** Yeah. No, that's a good point. I mean, especially I think, you know, like we've been kind of talking about that divide between small company, big company, especially when you're on your own as a small company. It's like, you know, it's like you don't have the time, but maybe even more so you don't have like, unless you're already in the marketplace, you know, solving a problem. It's not like you can go out and just like query a bunch of, you know, a thousand people like, well, what do you need? And then collecting the best responses. Oh, this will be the most profitable. It's like, no, you know, like, so you have to kind of just test and go and test and go. Yeah. So I think the best case scenario.

**Dave Vandenbaum:** Yeah, it's like your interview with Eric Ries, you know, you've got to get that first viable product out there to try to get an assessment of what's going on and make sure it has enough of the qualities that you're trying to test that you can tell whether people like it or not.

**Chris Gammell:** Yeah. Are you guys practicing the lean hardware? Are you in the lean hardware movement? Obviously, Bob, you had the hardware that didn't go into the box, so you had to turn it quickly, right?

**Bluetooth Low Energy:** Actually, it's easier to do that now than it's ever been again because, you know, I can send off files and get boards back. A lot of it has to do with how much you're willing to pay because if I'm doing my own stuff, more hobby type stuff or low priority for my business, then I'll go through OSH Park and get boards in a week or so or maybe two weeks. If I, on the other hand, for some of my higher priority stuff, I'll go through a company called Sunstone over in Portland and I'll pay, you know, I'll pay $500 or $700 and get, you know, overnight or two day turnaround. Yep. Yeah, so rapid, being able to turn design, you can't turn designs too quickly in hardware, not like you can in software.

**Dave Vandenbaum:** But the other thing is all the ancillary stuff that goes around the hardware is, you know, you have to have some documentation or it's something that tells you, you know, tells people how to use it. And if the documentation isn't very good, you know, you can get those first adopters to use it. But, you know, if you're if you're going toward the standard user, any like I said, any bump costs you 30 percent right there. And so you have to generate these other things that go along. And especially if you have to generate software that has to be used with your hardware, then the software has to work on various OSes. You know, some guys are going to be Linux, some guys are going to be Windows. And then, you know, you get a few real weirdos that are on OSX or something like that.

**Bluetooth Low Energy:** That would be me.

**Chris Gammell:** Oh, well, yeah. It's just it's just Unix. I just I prefer to think of it. It's just it's just Unix.

**Bluetooth Low Energy:** Well, yeah, I try not to get religious about operating systems. They just pick the one that does the job.

**Chris Gammell:** Now, that's a good point, though, about like all the other stuff. I mean, like especially when you think about turnaround time for for developing hardware. It's like I mean, even just like the ordering of parts, right, the generator bomb. OK, that's fine. Go buy all the parts. It's like just getting through a single purchase of parts and just verifying because you don't want to miss that one resistor, that four point two four five K resistor that you really, really, really need. It's terrible.

**Dave Vandenbaum:** I had Seed Studio do me a turnkey board a couple of years ago. Then the board has, you know, maybe 15 components on it, something like that. It's not real complicated. But, you know, to get the turnkey done and to get them shipped here and get them, that's two months right there. Two months. Wow. I mean, it was. I mean, back and forth and everything else. I mean, I don't want to say they do good stuff. It was near the beginning of the year. So we've got Chinese New Year's things coming in there. Oh, yeah. Some issues there as well. But, you know, still takes them a while.

**Chris Gammell:** That's a good reminder. Remember, people, February.

**Dave Vandenbaum:** February is Chinese New Year's. It's coming. It's coming. Yep. But, you know, mostly for small proto-runs and everything, I'm just doing the self-assembly, you know, myself. Because, you know, if you need 20 or 30 units, you can do that and get them out there and have people look at them. But, you know, if you get higher than that, then you need to have somebody do that for you.

**Bluetooth Low Energy:** Luckily, there's a lot of local. At least here, I've got two really good contract manufacturers that I could rely on to do sort of middle size, you know, thousands type manufacturing. And because it's all automated, it's actually the cost advantage of going to China is sort of going away. Right. Right. Yeah.

**Chris Gammell:** Do you care to share the names of those or do you want to keep your secrets safe?

**Bluetooth Low Energy:** It's not really a secret. So Western Electronics is one. And another one that I really like is Computrol. And Computrol is a really interesting privately held company. And it was actually started by some HP engineers who went out to build a fish finder. And their motto was fish found by sound. And so the Computrol factory, they have a big tank where they used to test the. It's probably 20 feet deep. And they keep goldfish in it so they can still, you know, so you could see them on the. But they're excellent. And they have a prototype line, pick and place prototype line that you can build on. And it's still a lot. So the lead, the shortest lead time, if I need two or three pieces of something is to build it myself. And I've set myself up so I can do that with my own, you know, stencil machine and reflow ovens and things like that. But all tabletop. I really want to get a tabletop pick and place.

**Chris Gammell:** Oh, yeah, going for that TMS 280 or whatever that thing is. Something like that would be awesome.

**Dave Vandenbaum:** I knew one guy that got one of, you know, that got a low cost pick and place. And I guess he bought it. It was a demo unit or whatever. So he got it for a pretty good deal. And I think that after, you know, after a half year or so, he was deciding he was going to sell that back. Yeah. Get rid of it. It was just such a pain to swap reels and settle up for each job that he just said, you know, I'm losing money on this thing.

**Bluetooth Low Energy:** I'm actually pretty good at placing it with a pair of tweezers. Yeah.

**Chris Gammell:** Yeah. Yeah, right. I mean, yeah, it's like the human element is like, where is that threshold of where you cross over?

**Bluetooth Low Energy:** While we were talking, I just placed some 32-pin QFN parts. That's what you've been doing this whole time? Jesus, man. And it turned out.

**Dave Vandenbaum:** And that does not show the proper respect for the show right there.

**Chris Gammell:** Oh, well, you know, that actually shows the perfect amount of respect if you're not drinking and or placing parts during the show. No, I'm drinking and placing parts. And talking to you guys. Good, good, good, good.

**Dave Vandenbaum:** Dave, you're actually lagging behind here, man. Geez, all I've done here is pour all my energy into the microphone here. You guys have been sitting there making money, probably dealing online stock trading.

**Bluetooth Low Energy:** I'm sinking money here. Yeah. Oh, and I tweeted it while I was in the middle of the show, too. Oh, man, really? Damn. Geez.

**Chris Gammell:** These guys right here.

**Dave Vandenbaum:** Yeah. Oh, wait, let me see if I can find it. Let's see. Talk under two assholes. Is that the one? Yeah, exactly.

**Chris Gammell:** Yeah. No, I mean, that's good about the personal prototyping stuff. That's important, right? I mean, that crossover point is really, it's tough to figure that out, too, especially until you figure where that point is. I mean, we saw this week. I don't know if you guys saw the Salier article. I thought that was good to bring up now versus next week. But, you know, like those guys, they bought a pick and place. That was for a larger operation, for the logic stuff. But, like, you know, they wrote about it, which was really nice for all the rest of us. But it's tough, you know, like actually getting a pick and place in house. Like, you're going to be spending months and months and months of that time just focused. You become a process engineer. You don't become an electrical engineer. You're a process engineer. You care about thicknesses of solder paste. You care about, like, accuracy to the mill of placement, you know, and rotation and statistical distributions of the placement over time.

**Bluetooth Low Energy:** They're a really good company as an example of what you need to do to be successful. And it's partly the hardware, but it's like I have one of their new Pro 16s here, which is really a neat piece of equipment. And another example of how you can do so much with a lot fewer resources now. Oh, yeah. And it had one small problem. And it's funny because it's got all these FPGAs and fancy pick and place PC boards and a really beautiful case. But the brown wire on channel one was broken. You know, the very lowest tech part of it. But the thing that makes a difference is their response because they were super responsive to that problem. I think they probably appreciated that I troubleshot the thing for them and figured out that it wasn't like a dead part of the FPGA, but it was just a wire. Yeah. And talking about talking about talking about.

**Dave Vandenbaum:** I'm sorry.

**Bluetooth Low Energy:** But the difference between them and maybe some other companies is that they were super responsive to it and got and took care of me. And that just builds a lot of, you know, I'll buy more stuff from them later, I'm sure.

**Chris Gammell:** Brand equity is the term you're searching for there. It's a douchey marketing term. Just doing the right thing. Yeah.

**Dave Vandenbaum:** You talk about those, you know, those little errors that creep in. Did you ever look in, I mean, notice in your book that you wrote, Bob, Getting Started with Bluetooth Low Energy, Tools and Techniques for Low Power Networking, available now on Amazon for $34.01, at least to me, which is probably the hyped up price because they always screw me. But in my copy, I was reading it. And, you know, at the very beginning in the intro when they give you all the formats and everything that's going on in the book, they have two little icons in there. One looks like an icon of a lemur or something. And the other is an icon of a scorpion that's supposed to point out when you, you know, dangerous things that might happen or, you know, things to watch out for. Then I go through the entire book and every place where there's one of those icons put, it's not either one of those. It's a bird. Oh, yeah. So I said, where's the scorpion? Where's the lemur? It's always a bird. What does the bird mean? Did he eat the scorpion? Yeah.

**Bluetooth Low Energy:** No, I didn't have anything to do with that.

**Dave Vandenbaum:** The iconography is not your forte. I did have a question that I haven't gotten around to asking you. But what were the mechanics like writing that book with four people and with O'Reilly as the publisher? What was that like?

**Bluetooth Low Energy:** How that got started was O'Reilly came to me and asked me if I'd write a book. But they wanted the book out by the time of their solid conference. So they wanted this. It wasn't a long book. But they wanted it done in May. And they were talking to me in November. And I hate writing. So I found three other guys that are really good at writing and like to do that. And got them involved. And one of the guys actually, Carl's, is involved in the Bluetooth low energy stack for Nordic Semiconductor. And, you know, and Kevin Townsend. They're all young guys with a lot of energy. So I did my little part. And then they did the most, all the six. Oh, Kevin is the, is that micro builder?

**Chris Gammell:** Micro builder. I forget his name.

**Bluetooth Low Energy:** And he's also the head engineer or something for Adafruit. And then Freak Labs, Akiva. There's a good group of people. And, but they, it's all done, you do the book completely online. And so it's really easy to. I mean, how online?

**Dave Vandenbaum:** Is there some package or something that you use? Or is it like Google Documents?

**Bluetooth Low Energy:** They have their custom, they have their sort of custom packages, but it's really built around GitHub. Yeah. So you can use. It's like a markup language, right? Yeah. Oh, okay. It's a markup, it's a markup language. So all those little birds and stuff come in later as part of their. Mm-hmm.

**Chris Gammell:** Well, that's. Those are just tags. That's neat. Yeah.

**Dave Vandenbaum:** I mean, because, you know, when I wrote books for like Prentice Hall, you know, it was all type the book out and do your own figures and then turn it over to them. And then they'd redo all the text and then they'd redo all the figures and you had to go back and reread it all again and reproofread it and recorrect it.

**Bluetooth Low Energy:** Yeah. You know. Well, we had an editor that kept us in line on the English language. But it was, the neat thing was, so Kevin's in Paris and Carl's was in Barcelona and Akiba was in Tokyo and I was in Boise. I have to get a, I have to get a t-shirt that says Tokyo, Paris, Barcelona and Boise. Or maybe going around the world with Bob. Yeah. But, you know, because it was all online, it was pretty easy for us to all stay synchronized. Yeah.

**Dave Vandenbaum:** It's nice that they have, that O'Reilly has a system set up to do that.

**Bluetooth Low Energy:** No, it's an excellent system. And if people have ideas for writing a book that O'Reilly was really good to work with, I highly recommend. And you can just go propose a book to them and, you know, possibly they would run with it.

**Dave Vandenbaum:** The word on the street, Bob, is that with the royalties from this book, O'Reilly gave you a jewel-encrusted gold battleship.

**Bluetooth Low Energy:** Yeah. Something like that. Actually, it's not a very lucrative thing. I kind of had to look at it as a marketing. Yeah. It's a promo thing. Yeah.

**Chris Gammell:** Which is when me and Bob got to meet at Solid. So that was good.

**Bluetooth Low Energy:** And I also got to learn about how Bluetooth Low Energy works. There you go. Yeah.

**Chris Gammell:** Learn and write at the same time.

**Dave Vandenbaum:** Yeah. That was the thing. When I was a college instructor and I had to teach a class, I'd say, well, I had to stay at least a chapter ahead of the students. And so I guess when Bob was writing the book, he said, well, I guess I just had to stay a chapter ahead of everybody else.

**Bluetooth Low Energy:** Just find smarter people than me to work with. I also remember from teaching, I taught electromagnetics for three or four years. And boy, by the time you're done with that, answering all the questions that people can ask, you really get it down pretty cold compared to just being a student going through it. It's kind of like the difference between driving a car versus being a passenger in a car. Right. Exactly. You both get to take the same trip. Yeah.

**Dave Vandenbaum:** One of you can actually remember how to get back. Yeah.

**Dave Jones:** One can't.

**Chris Gammell:** Well, guys, thank you for being on the show. This has been another successful impedance matching episode, I think.

**Dave Vandenbaum:** Thank you very much for having us, Chris. And I'd like to point out that I did not once mention my butt crack.

**Chris Gammell:** That's always a good thing. Minus one for that one. Ah! Blew it at the end. Yes. Oh, well. But if people don't know the reference, of course, go back. There are great interviews with both Bob and Dave separately. Previously, Bob was the episode 144 and Dave was 181. We'll link both of those, of course, into the show notes. Definitely worth a listen. Lots of good stuff in there, too.

**Bluetooth Low Energy:** Well, thank you.

**Chris Gammell:** Thank you, guys. Well, we'll have you back on again, I'm sure, sometime soon. Okay. If there's not the cantankerous, grumpy old guy vibe here, we're doing something wrong. I know. Okay. I gotta go. I gotta go past the stone. That's right. Oh, God.

**Dave Vandenbaum:** Well, good luck with all that. Okay. We'll talk to you guys soon.

**Bluetooth Low Energy:** Thanks, guys. Okay. Bye-bye.

**Speaker ?:** Outro Music
