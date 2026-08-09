---
episode: 442
title: An Interview with Travis Goodspeed
url: https://theamphour.com/442-an-interview-with-travis-goodspeed/
---

**Travis Goodspeed:** This is The Amp Hour Podcast. Released May 12th, 2019. Episode 442. An interview with Travis Goodspeed. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Travis Goodspeed:** I'm Travis Goodspeed, and I have an electronics problem.

**Travis Goodspeed:** Oh, what is your electronics problem? Just that you love electronics?

**Travis Goodspeed:** Well, I like making things with electronics, and then I find myself getting stuck supporting them, you know?

**Travis Goodspeed:** Ah, yes, that is quite the problem. And people might know you from the GoodFet, the GoodWatch. I see things marked with neighbors often. I think that's part of your be a good neighbor. That's kind of your thing, right?

**Travis Goodspeed:** Yeah, coming from Southern Appalachia, I just like, it's like half true, but I half invented from whole cloth fictional society with traditions of neighborliness and that sort of stuff that was mostly ripped off from Mr. Rogers.

**Travis Goodspeed:** Okay. Hey, if you got to pick someone to, you know, borrow heavily from, Mr. Rogers is not a bad person to do that from.

**Travis Goodspeed:** I think he's an inspiration to us all. He shows kids how things work. Like, where he'd do, like, factory tours and show you how crayons were made. Or, you know, I like to think that if he did shows for the sort of an audience, he'd, like, show you how to take apart radios and stuff. Or maybe even teach children how to do that.

**Travis Goodspeed:** This is the 400-volt bus bar. Don't touch this, children. Yeah, that's great.

**Travis Goodspeed:** Okay, kids. Today we're dealing with high voltage, so you keep one hand behind your back to safety first.

**Travis Goodspeed:** It's like, guess a number, except the number is, yeah, how many minutes you're going to live. Keep one hand behind your back during that.

**Travis Goodspeed:** There'd be, like, a whole song and dance about it, you know, with puppets reminding the kids to keep the hand behind the back.

**Travis Goodspeed:** Right. That could save lives. Show the creepy king. The king always creeped me out in Mr. Rogers, but then, like, he gets electrocuted or something like that. He was a bit weird. So, I actually, you and I have met in real life. I don't know if you remember this. Probably not. It was a long time ago. It was actually the first time I ever went to a hackerspace. The first time I ever met Drew Fustini from Osh Park. And the first time I'd ever been in Chicago.

**Travis Goodspeed:** Chicago. Yeah. Yeah. I was visiting Chicago. And Drew, like, he's like, hey, you want to go to a trade show? He's like, you don't want to go to a hackerspace? I'm like, what's a hackerspace? And I went there. I met you and walked around the space. And it was awesome. A long time ago.

**Travis Goodspeed:** Which trade show is that? Was that the Embedded Systems Conference?

**Travis Goodspeed:** Yeah, I think so. Yeah, it was. Or I don't remember which one. It might have been 2010, 2009. It was many years ago, though. Maybe nine years ago. Yeah.

**Travis Goodspeed:** Yeah, the one that I really missed was the TI Developers Conference.

**Travis Goodspeed:** Oh, I never went to that one.

**Travis Goodspeed:** It was amazing. There were, like, seven or eight tracks all running in parallel. And the lecturers were TI employees. And the only part of it that was a sales pitch was that they would teach you how to make things with TI products.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** And they would teach you how to do everything from, like, wireless power to radio to... They had one that was just this old fellow who knew everything. And he was talking about how he used electronics design techniques in rewiring his house.

**Travis Goodspeed:** Oh, nice.

**Travis Goodspeed:** Like, when the wiring went wrong, he measured the capacitance of it in order to know where the break in the wire was.

**Travis Goodspeed:** Like, TDR almost kind of stuff? Like, time domain reflectometry?

**Travis Goodspeed:** Oh, no. He just measured the capacitance. Because when you have two wires that are separated by an insulator, that's a capacitor. Sure. And then the capacitance ought to grow roughly linearly.

**Travis Goodspeed:** Oh, okay. So the bigger the capacitor, the longer the run was kind of thing?

**Travis Goodspeed:** Yeah. I mean, he was off, but he was off by, like, three feet and 100. So that was close enough to identify, like, a known good spot in the wiring. I think they didn't do proper conduit, so they weren't able to run a new wire out.

**Travis Goodspeed:** Well, that's awesome. So is that conference gone now, or what happened to that?

**Travis Goodspeed:** Yeah. I think they replaced it with, like, a roadshow in each market. So then they would do, like, a smaller one in Munich and then one in New York, and it shrunk from there.

**Travis Goodspeed:** That's too bad.

**Travis Goodspeed:** But back when they did just one big one, it was the greatest week of education you could get.

**Travis Goodspeed:** Yeah. I mean, TI's brought, you know, bought a bunch of other brands, too. So they basically just collected talent over the years. And that's too bad that that's not there anymore, because that sounds like a blast.

**Travis Goodspeed:** It's a shame that some of these parts are so hard to get documentation about or to get an introduction to. And just having, like, a feeding from the fire hose event where every part for sale had an expert who had designed a product with that part on hand for you to ask questions, to give you free development kits. It was incredible.

**Travis Goodspeed:** Right. Yeah. And then they, I mean, I think it's not just them. I don't want to call out just TI. But, like, a lot of them are like, well, we want to serve larger parts of the market, and they want to get that. And so then they switch everything to online. But then that kind of is like a downsampling of information. Like, what you're talking about sounds like being in a room with someone and, like, being able to just be, like, peppering with questions is amazing.

**Travis Goodspeed:** Yeah, and you could do that. Yeah. Either at the lectures themselves or in the hotel bar. I mean, we're talking about the size of DEF CON or Black Hat here, but only for TI parts.

**Travis Goodspeed:** That's killer. And you have done a bunch. So I've seen some of your stuff uses some of, like, the, some of their parts, but also, like, a lot of, like, integrated RF components. Is that what's on the Goodwatch? So maybe we should kind of walk through some of your products that you've worked on in the past and what they are.

**Travis Goodspeed:** Thanks to that conference back in 2008, I kind of got hooked on TI's microcontroller family, the MSP430, which is, like, their alternative to an AVR or a PIC. It's a little bit smaller than the ARM microcontrollers that sort of form, like, the next rung up as far as power consumption and processing power go. So the Goodwatch contains a chip called the ChipCon 430. ChipCon is a radio company that TI purchased. And the ChipCon 430 gives you a sub-gigahertz radio that is very configurable. You can make it compatible with lots of different things. And it also gives you a 16-bit microcontroller that costs almost no power. I believe I'm measuring three microamps. So I get years of battery life on a coin cell.

**Travis Goodspeed:** Nice. Yeah, that's great.

**Travis Goodspeed:** Now, you've got to be very careful about it. You can't leave, like, any pins disconnected when you're getting this sort of battery life. So maybe eight or nine years ago, there was a TI development kit that came out called the Kronos watch. And the Kronos watch was a lovely idea, which was that you could use this ChipCon 430 chip to make a wristwatch. And then you would have, like, a radio on your wrist.

**Travis Goodspeed:** I remember that kit. I think I got one of those. And it was just like, okay. That just kind of sat. You know, the demos didn't do much. And so unless you're, like, ready to dig in, like, you're talking about, it was kind of just a sits in the drawer kind of thing.

**Travis Goodspeed:** Yeah. There were all these, like, little things that were so very close to being perfect about it, but weren't quite. Like, you know, the design is open source. And that's great. But the hardware layout was not available. And the schematic diagram was a blurry JPEG screenshot. So you couldn't quite read all of the component values.

**Travis Goodspeed:** Oh, boy. Yeah, okay. So it was get out of DMM and desolder components to find the values kind of thing?

**Travis Goodspeed:** Not that bad. Like, you could kind of squint or recalculate what the value should be yourself or look it up in another data sheet. But it made it hard to play with it as a hobbyist because you had to then redo a lot of the work of designing it. And the same with the software. It was only compilable with TI's proprietary compiler. Later, this was moved to run from the GCC on the command line. That's cool. And there were other little issues. Like, in the initial release, the real-time clock didn't work. So you had a watch that couldn't keep accurate time.

**Travis Goodspeed:** Okay. So a wrist-mounted electronic thingy. Sands time.

**Travis Goodspeed:** Right. And the worst part about it was that it was horrifically uncomfortable to wear. And the second worst thing about it was that it was very ugly. Okay. Going back to the same TI developers conference, I met some fellows there from Fossil. And they were explaining to me that a wearable isn't a wearable if you don't wear it.

**Travis Goodspeed:** That's right. It's a door-able. Yeah.

**Travis Goodspeed:** Yeah. Like, if the battery dies or if it's uncomfortable or if it dissolves in sweat, you lose the habit of wearing it. It winds up in a drawer and it's gone. So for years, I wanted to redo it around, like, a proper commercial watch casing. Because I can make electronics, but I can't make, like, a watch case. I'm not a jeweler.

**Travis Goodspeed:** Sure. Right. Right. Right. We all watch ClickSpring on YouTube, but being ClickSpring is a lot harder. Yeah. Actually, like, making commercial love. Like, even just, like, stretchy bands or even leather bands. Like, you know, sourcing that stuff is intense.

**Travis Goodspeed:** Yeah. And then, like, if you get the wrong one, how do you know? Do you wait until, like, the guy wearing it has an allergic reaction? Oh, yeah. Or do you become a plastics expert yourself? Or, like, what do you do about it, you know? So then, years later, I found myself in this horrific... I don't want to call it, like, a demonic ritual, but that might be the best description of it. It was a daily, hour-long scrum meeting. Oh, my God. Every morning, one hour, like, updating the spreadsheet on the projector. It was, like, the biggest gumption killer that you can imagine. Like, you go in, you're ready to get some work done, you waste an eighth of your day in that meeting, and then you're useless for the rest of it.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** So, while I was sitting in this meeting, I had a screwdriver, and I had a Casio wristwatch. And so I took the watch apart.

**Travis Goodspeed:** Is this, like, the classic, like, calculator watch, or are we talking about, like, a proper screen watch kind of thing?

**Travis Goodspeed:** No, no. This is, like, the classic Casio one. I think the design is from the late 90s.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** It's a Casio 3208 module, which you find in the CA53 and CA506 watches. Like, basically, any calculator watch that they still manufacture will use this casing and not the older ones.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** And when I took it apart, I realized that, like, I could make a board that would fit where the old board went. And I could have, like, a press-on connector for the display where theirs went. And I could have the same thing for the keypad. And I could have little tabs for the side buttons. And I could have the, like, connector for the coin cell that the original watch had. And then I could have my own wristwatch with whatever electronics I could fit in there.

**Travis Goodspeed:** Right.

**Travis Goodspeed:** Both in space and in battery power.

**Travis Goodspeed:** Right. And then it's a pre-constrained engineering problem, which usually makes my brain start to go off. It's like, oh, I could do this and this, but I can't do this. And it really kind of helps to formulate the actual product then, or the project, I guess.

**Travis Goodspeed:** Yeah. Yeah. So you, like, tinker around a little bit, and your first prototype doesn't quite work. And then you fix the mistakes on it. But pretty soon you settle on something cool that does fit within these constraints. So I then decided to, like, take a sabbatical, which is the polite way to say be unemployed. And my buddy, my buddy, Torsten Haas paid me $1 per day that I was unemployed to work on the watch. Nice. Okay. Yeah. So every day I'd get a check for $30. You know, a bum's got to have a dollar. Okay. And that's how the watch was made. So I had some prototypes printed up in China, soldered them up myself, wrote the firmware. And now I've got a wristwatch with every feature that I could want in the wristwatch, because I wrote the code myself. So, like, the calculator is now reverse Polish notation. There's a hex editor and a disassembler.

**Travis Goodspeed:** Of course, because that's what you need in a watch. How does that actually work with the, like, do you, like, scroll through lines on the screen? Because it's a pretty constrained, maybe we should explain the screen, too. I mean, it's just, like, what, 10 characters, 20 characters, maybe?

**Travis Goodspeed:** It's eight characters.

**Travis Goodspeed:** Oh, 10. Too many.

**Travis Goodspeed:** Well, it's a 16-bit CPU. So the left four are the address, and the right four are the 16-bit word at that address.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Okay. And then if you hold down the four button, then it will disassemble the instruction and show it to you in assembly.

**Travis Goodspeed:** Wow.

**Travis Goodspeed:** And then the top row of buttons moves each of the four nibbles up and down for the address.

**Travis Goodspeed:** So, like, does it then, like, scroll left, right to actually see more of the assembly code, or what?

**Travis Goodspeed:** No, I wrote in assembler understanding the constraints of the instruction set and the display. Okay. So they all fit. That's awesome. Yeah. And it also has a radio. So I have a frequency counter in it. So if I have a UHF transmitter and I need to know what frequency that transmitter is running on, I just transmit next to the watch, and the watch will read off the frequency to me off by maybe a couple of kilohertz.

**Travis Goodspeed:** So this is like some James Bond stuff here, almost. You know, if James Bond was into programming and needed some help disassembling a program.

**Travis Goodspeed:** If instead of, like, sports cars and exotic locales, James Bond were into, like, ham radio and electronics design, then this is what he would have.

**Travis Goodspeed:** That's great. So how much range does the radio have? Is it like SDR or what is it?

**Travis Goodspeed:** No, no. You cannot do SDR for power budget reasons. You know how, like, your laptop fans go up when you're running an SDR on your computer?

**Travis Goodspeed:** Yeah. Yeah.

**Travis Goodspeed:** Well, I'm dealing with a 16-bit chip running at about 1 MHz.

**Travis Goodspeed:** Got it. So I can't possibly keep that there. I meant more, like, how tunable is it? Like, what range of tuning is there? More than, yeah, I guess SDR is a stupid way to say it. I meant, like, how flexible is the radio? Because it showed, like, 433 or something?

**Travis Goodspeed:** Yeah. My initial model was, like, 430 to 436. My current model you choose is either 250 to 500 or 250 to 1 gig. Maybe 950 is more accurate at the high end. And that's controlled by the filtering. So you can only transmit in the upper half of that.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Because you don't want the transmission harmonics to interfere with anyone else.

**Travis Goodspeed:** Yeah, this thing doesn't have an FCC ID, I'm guessing.

**Travis Goodspeed:** No, no. I make them for ham radio. So, like, they're for experimenting. There's no Rojas. There's no FCC ID. I don't mass produce them. They're only for myself and for anyone else.

**Travis Goodspeed:** They're boutique items for the discerning radio enthusiast. Radio and programming enthusiast, I guess.

**Travis Goodspeed:** Yeah. Like, sometimes you just want a really cool watch. Yeah. And you don't necessarily want to mass produce it or to sell it or to support it. You just want to have a cool watch. And that's the situation I was in. And now I have a cool watch. But if you want your own, all the code, all the hardware, all the design docs, everything is on GitHub. It's rather well commented. You can run through and see how any individual application works just by reading two or three pages of C.

**Travis Goodspeed:** The RF that's on board, though. So, what was the target for that chip in the first place? Was it meant to be, like, consumer-level, like, beacon stuff? Or what was that actual... Like, was it meant to operate in the ISM band? Or which bands was it meant to operate in?

**Travis Goodspeed:** It was made for, like, the sub-gigahertz ISM bands or the commercial ones. So, it's very versatile. It has a couple of gaps. But the chip can do about 250 megahertz to 1 gigahertz.

**Travis Goodspeed:** Wow.

**Travis Goodspeed:** They intended this for things like electric power meters, right? Like, the smart grid was a big thing back then.

**Travis Goodspeed:** Right.

**Travis Goodspeed:** And they were trying to figure out how it would work to electronically build people for their electric usage without sending someone by to physically read the number on the meter and write it down. It's also worth remembering that this chip came out before Bluetooth Low Energy.

**Travis Goodspeed:** Okay. Yeah, it's a while, huh?

**Travis Goodspeed:** Yeah. Do you remember how Zigbee used to be a really big thing?

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Yeah. And, like, there were all these cool development kits for it. But commercially, it didn't really get much traction because no two products would ever talk to each other.

**Travis Goodspeed:** Everyone's setting up their own standards, their own, like, their own packet types and everything like that. And they don't, never the twain shall meet.

**Travis Goodspeed:** Right, right. So, Bluetooth Low Energy, like, you know, they were concerned with, like, old-fashioned Bluetooth was very power hungry. It was focused on things like audio and just sort of had, like, a serial port mode as, like, a side thing. And then the Bluetooth consortium came out with Bluetooth Low Energy and then all the cell phones supported it. And then all the chipsets supported it.

**Travis Goodspeed:** Mm-hmm. Yeah. Yeah. Yeah. Yeah.

**Travis Goodspeed:** But the advantage of using a chip that predates Bluetooth Low Energy is that they had to be compatible with everything. Oh, interesting. So, like, I've implemented POXAG for it so that I can receive pages on the watch.

**Travis Goodspeed:** And what, so what was that, was that an acronym? I don't actually know that one.

**Travis Goodspeed:** Oh, it's POCSAG.

**Speaker ?:** POC.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** It's the British post office standard for pages. It's, like, one of the two pager protocols that are popular.

**Travis Goodspeed:** And it's still active?

**Travis Goodspeed:** For amateur radio.

**Travis Goodspeed:** Ah, nice. Okay.

**Travis Goodspeed:** So, there's a network called DAPnet run by a, like, a group of amateur hobbyists. And they convert UHF ham radio transmitters to be pager transmitters. And then you can buy a pager programmed for your ID number on their network. And then you can receive pages that have been sent to your ham radio call sign. Yeah.

**Travis Goodspeed:** That's awesome. That's really awesome. I feel like that would work well with the, you know, badge life community, too. Like, just have, like, a centralized pager network kind of thing. And it's just badge life on your wrist, really.

**Travis Goodspeed:** It would. I think that the Telefreak party one year had, like, pagers that they would hand out. And then there would be an announcement by pager to tell you where the party was.

**Travis Goodspeed:** That's great.

**Travis Goodspeed:** And the pager protocol is perfect for my wristwatch application because it pushes a lot of the power budget to the transmitter. Before you have a radio packet, you have this thing called a preamble. And in modern radio, like Bluetooth, for example, the preamble is very short and it only exists to show the receiver how wide a bit should be in time. In POXAG, the pager standard, the preamble is half a second long. So your radio can wake up, like, every 400 milliseconds and look to see if a message is coming in.

**Travis Goodspeed:** But what does the preamble look like? Sorry, like, so it wakes up every 400 milliseconds and then it's just like seeing a certain frequency transmitting is just like a repeating code over that time or what?

**Travis Goodspeed:** Yeah. And the code is as simple as possible. It's a one and then a zero and then you repeat it. Oh, okay.

**Travis Goodspeed:** All right. So like a clock almost.

**Travis Goodspeed:** Yeah. So as the receiver idles, it's not actually waiting for a packet. It's just sort of periodically waking up to see if a packet will be coming in the next half second. And if it's not, then it can immediately go back to sleep, turn everything off.

**Travis Goodspeed:** Okay. So when you said that pushes the power budget to the right, you mean that pushes the power budget to the transmitter, like the centralized transmitter that'll be heavily powered. Yeah.

**Travis Goodspeed:** So this half second is like a half second running at 50 watts that is done for every single transmission.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** But it also means that the receivers can run for months on a AA battery.

**Travis Goodspeed:** Yeah. That's great. So does that mean that limits the system then though, right? Because there's only, or does it like blast out multiple messages after that preamble of the half second?

**Travis Goodspeed:** The latter. So you queue up a bunch of transmissions and then you flush them out all at once.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** And while you're fleshing them out, everyone is awake, but you can minimize how often this happens.

**Travis Goodspeed:** I used to have a pager for work. So I used to work in a fab and like they gave us pagers and like they just loved them because, you know, you can just get through walls. No problem. You know, walls ain't no thing. Yeah. And obviously, yeah, like you're saying that, I mean, usually you have a really high power transmitter as well. And so anywhere you were in the fab, you'd just be able to get a page. No problem.

**Travis Goodspeed:** They have other cool design things. Like the last three bits, the lowest three bits of your number are encoded by where in the packet your message arrives.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** So like if your last three bits are zero, you actually come closest to the beginning of the packet.

**Travis Goodspeed:** So like every, so, okay, so every, every device wakes up and says, I see that there's an incoming message in some amount of time. I'm going to stay awake. And then there's a blast of messages that might come through for, say, there's a hundred pagers in the field. Like 20 of them have messages. Does every pager receive every message?

**Travis Goodspeed:** So yes. Okay. For numeric pages, they might all be in the same batch.

**Travis Goodspeed:** Uh-huh.

**Travis Goodspeed:** Alphanumeric paging breaks a lot of this because it takes up multiple slots. Okay. If you wanted to, you could even rearrange the batches to be more efficient. Like to, um, have the fewest total number of batches by overlaps.

**Travis Goodspeed:** Does this mean though that the messages are all just kind of like hanging out there and unencrypted and usable by all?

**Travis Goodspeed:** Oh yeah.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Yeah. Um, and there are people who, um, have published like software defined radio code to sniff the public pager networks. Um, here in America, they mostly use flex for the wide networks and they'll, um, they only use PoxAg for things like, um, restaurant pagers. Uh, PoxAg is the protocol that I implemented for my watch and flex is the commercial protocol that's used by like modern pager vendors, uh, the nationwide networks.

**Travis Goodspeed:** Yeah. I remember, uh, someone I was in, when I was living in Cleveland where there was a high school student who came, he came by the meetup we had. He's like, uh, so I just like decoded all these pagers from a hospital and they're unencrypted medical things. And I don't know what to tell about it. It's like, Oh my God, it's just like all this HIPAA data that was just like floating on the airwaves. And this kid found it. And, you know, like he's trying to do the right thing, but like the, who do you, you know, who does he tell at that point? You know, he was in high school.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** It's tough.

**Travis Goodspeed:** And I mean, largely it's a known issue. Yeah. You can purchase an encrypted pager. Um, they're available. I don't know how good they are, but there is a niche for that.

**Travis Goodspeed:** Yeah. Yeah. But pagers are still a thing. It sounds like you're saying.

**Travis Goodspeed:** Mostly for like, um, like you being in the fab where you won't have a cell phone signal everywhere, but you absolutely have to get that message when it comes through.

**Travis Goodspeed:** Uh huh.

**Travis Goodspeed:** So you can have like a local transmitter in the building to cover everyone inside of that.

**Travis Goodspeed:** Oh, okay.

**Travis Goodspeed:** Uh, and then also for, um, like, uh, work in a secured environment where you're not allowed to have a phone, but you still need to receive messages.

**Travis Goodspeed:** Yeah. I just remembered when we'd be sitting in a meeting with like 20 people and if everybody's pager went off, it was going to be a bad day. It's like a real bad day at that point. Uh, so that's cool. So, so then how, how do you interact with the watch then? So like, are you, is this when you're going to like, like ham conventions and there's one of these transmitters set up? Like, how are you, um, how are you testing this? I guess too.

**Travis Goodspeed:** So I've been testing it at my desk. Um, and if I'm to be totally honest, I don't actually want to receive pages from people. What I really want to do is win the local pub quiz.

**Travis Goodspeed:** Well, how does that relevant? Is that because there's those use the same protocol or something or what?

**Travis Goodspeed:** No, no. A pub quiz. Like when, uh, you go to the bar and they ask questions over the PA system and no one's allowed to have a cell phone.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Well, you can have an accomplice who does have a cell phone and pages you all the answers.

**Travis Goodspeed:** Uh, Travis, that does not sound very neighborly. Although it does sound like you'll be getting two for one wings with no problem if you do that. Or a $50 gift certificate.

**Travis Goodspeed:** Um, we actually, uh, made an arrangement with the guy who hosts the local pub quiz. Uh, we're allowed to phone a friend once if I can do it only with a Casio watch.

**Travis Goodspeed:** Okay. That's, that's a fair trade, I think.

**Travis Goodspeed:** Yeah. And like we're announcing it, we're not being sneaky about it, but it totally would have worked if we wanted to be sneaky about it.

**Travis Goodspeed:** That's right. Right. It's that, uh, white hat, black hat kind of hacker stuff there, huh? You're, you're doing it because you can and because you want to make sure that you're protecting others from the system.

**Travis Goodspeed:** You know, for winning a pub quiz, I don't think it's about protecting anyone. I think it's because it's funny and it's like a good story to tell afterward.

**Travis Goodspeed:** Yeah, that's great.

**Travis Goodspeed:** And sometimes that's its own reward.

**Travis Goodspeed:** Yeah. Uh, do I remember you were doing some of the I am me stuff as well?

**Travis Goodspeed:** Yeah. Yeah. Um, the, uh, back in grad school, I wrote a reflexive jammer for P25 with it.

**Travis Goodspeed:** Okay. What's, what is P25?

**Travis Goodspeed:** P25 is the, the handheld push to talk, uh, radio standard that is used by larger police networks.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Uh, by firefighters, um, like, uh, emergency response and that sort of stuff.

**Travis Goodspeed:** Got it.

**Travis Goodspeed:** Um, so we had, uh, uh, the, the paper is called, uh, why special agent Johnny still can't encrypt. Okay. Uh, Sandy Clark, who you might know is the first author on it. Um, so we, um, we took a look at these radios and how they worked from a security perspective and, um, found that like very often it would be clear text when it shouldn't be. We found that you can send a message to the handheld to ask where it is. Oh, that sounds dangerous.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Well, yeah, you can build a device that says like, uh, Hey, are any cops nearby? Right. And the cops might lie to you, but the radios won't.

**Travis Goodspeed:** Right. So what does that look like on the, on the protocol side of things? And like, how does it actually do that, that, um, handshake of like figuring out where they are? They didn't have GPS in them, do they?

**Travis Goodspeed:** Some of them do actually. Uh, but even if they don't, the idea is that you want to know, uh, which radios are within range, right? Because there's no use in calling someone who's out of range.

**Travis Goodspeed:** Oh, I see. So it's like a call and response kind of thing. Like, so you do a broadcast and then you wait for people to ping back or something like that.

**Travis Goodspeed:** Yeah. Yeah. Uh, just like a little heartbeat type thing. Uh, so the, the tower sends a packet out saying like, Hey, could radio 395 call back and then radio 395 will send one little ping back.

**Travis Goodspeed:** Yeah. And so anyone, anyone could do that you're saying, or, or, or you could impersonate the tower or how did that work?

**Travis Goodspeed:** Yeah. Uh, very often the encryption would be optional so that even if the network were encrypted, you could still forge these types of packets.

**Travis Goodspeed:** And so the, how did the jammer then work into that? Like the IME, IME was like a tiny little handheld thing, right?

**Travis Goodspeed:** Yeah. Yeah. But it uses the, the same radio core as my watch does.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** And like I said, it's a very versatile core. So you can, um, you can have it listen for an incoming packet, which is from a transmitter that's very far away, right? It's a very weak signal. And as that packet is coming in, it can then, uh, recognize that a packet is arriving and transmit during just the most important part of it. Um, and then turn off.

**Travis Goodspeed:** Oh, so it's not detectable then either as a jammer.

**Travis Goodspeed:** Well, yeah, it only runs like, uh, 3% of the time. Uh, you can detect it with specialized equipment, but if you've got just general direction finding stuff, then the tower will be the dominant signal.

**Travis Goodspeed:** Uh, is that, is that the same? Like, so you mentioned the P25 protocol, is that like doing the same kind of thing where it's, it's doing a long preamble to set people up to know there's an incoming packet as well? Is that, is that kind of the, the, the tough spot there? Or like, how do you, how do you know the signals coming in and then what is the part that you're actually blocking out?

**Travis Goodspeed:** So you have to get a copy of the standard and then you read it and then you implement it from what you've read.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Um, so P25 has, um, so it's called four FSK, which means that you have like, um, two bits determining which one of four frequencies you'll be transmitting on at that instant in time, like per symbol. Uh, it runs a little bit faster. Um, but these are all just parameters that you can feel. They can feed into the watch or the IME to re-implement the protocol. Um, P25 doesn't do the same power management tricks because your radio is supposed to be charged every night or between shifts.

**Travis Goodspeed:** Yeah. And usually they're the big, like, these are like police radios. You're saying like the big Motorola type ones are similar.

**Travis Goodspeed:** Yeah. They weigh a ton. Yeah. Um, they do make, uh, smaller ones for like hotel security that look like an old feature phone.

**Travis Goodspeed:** Oh, like, uh, Nokia like phones you're saying? Like, like a brick. Is that what a feature phone is? Sorry.

**Travis Goodspeed:** Yeah. A feature phone is just a phone without a touch screen.

**Travis Goodspeed:** Got it. Yeah.

**Travis Goodspeed:** Like, uh, you remember when they had buttons?

**Travis Goodspeed:** Yeah. Yeah. I do. It's been so long, man. It's been so long.

**Travis Goodspeed:** I know the world changes.

**Travis Goodspeed:** It does.

**Travis Goodspeed:** Ain't nothing like it once was.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Um, there's a related project that you might find interesting. Um, so one of the competitors to P25 is called DMR and DMR is used for things like, um, really small police departments, like, uh, university ones that only have like a limited territory. Uh, uh, um, and for business radios, but it's also very popular for amateur radio. And there is an internationally trunked network. So you can make calls between countries using it.

**Travis Goodspeed:** Whoa.

**Travis Goodspeed:** Nice. Yeah. So one of these radios is called the MD380. It's, um, about $90 and you can, uh, buy these everywhere. Like, uh, all over, um, all the websites have them, all the ham radio shops have them. Um, so some friends and I broke the encryption on the firmware updates, reverse engineered the firmware and now maintain our own patched firmware that runs in the official radio.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Um, so by doing this, you can get promiscuous mode and you can hear everything that's on the channel, even if you're not a part of the conversation.

**Travis Goodspeed:** Oh, wow. Okay. That's so, is that because it's sharing among channels to like to up the bandwidth or what?

**Travis Goodspeed:** Yeah. Yeah. You can basically have two conversations at once, but in ham radio, you're not supposed to talk over someone else. So you need to know that they're having a conversation to be polite and in a commercial radio, you never want like the, the workers to know what the bosses are talking about, even if it's on the same radio network. Uh, so the commercial radios didn't have this feature and we just added it. Um, there's also a phone book of all of the users. So you can like, as someone is talking, you will see a name and a call sign, a city and a country.

**Travis Goodspeed:** That's, that's a feature you guys put in or that's an, uh, a natural feature.

**Travis Goodspeed:** It's a feature that we added. Um, again, open source on a GitHub. Um, the core of the code is proprietary, like the, the vendor's proprietary software, but by reverse engineering it and changing it, we were able to add our own features.

**Travis Goodspeed:** And then how do you do the lookup of who would actually like whose call sign and who was actually calling?

**Travis Goodspeed:** There's a spy flash chip and we download the database from the volunteer organization that does the registration. And then we just flash that into the spy flash chip and search through it by software.

**Travis Goodspeed:** Oh, wow. Okay. So this is, so there's, uh, there's already a pre-registration you're saying of the people that are on the network, but then you're able to actually show it as, as it's live happening. Okay.

**Travis Goodspeed:** And then, um, our code fits where the Chinese font used to.

**Travis Goodspeed:** Oh, nice. Okay. Not using that space anyways. Yeah.

**Travis Goodspeed:** I wish that I could read Chinese, but me too. Since I can't. And it was a fifth of all of memory. Might as well.

**Travis Goodspeed:** Yep. Yeah. Is this, so, um, is this like a hand, this is a handheld unit you're saying it's kind of like MD380 is kind of like a, like a Baofeng style, like handy talky kind of stuff.

**Travis Goodspeed:** Yeah. It's a little bit larger than a Baofeng.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Um, and it's, uh, digital, like it has an analog mode, but by default you're using digital.

**Travis Goodspeed:** What is the, what is the project called that actually has the replacement firmware?

**Travis Goodspeed:** Uh, it's called MD380 tools. It's on a GitHub or you can go to MD380.org.

**Travis Goodspeed:** That's great. So then how are people, I mean, is this like a thing where it's, you're going to keep adding features to that, to that radio or how does that all work? I think I'm done with the project. Okay.

**Travis Goodspeed:** Um, when you start these things, sometimes they're really cool and exciting. And then after a while you're no longer using the project and it becomes more of a chore. So, um, like for a year or two, it was a whole bunch of fun, but now it's not. So I'm not very involved anymore.

**Travis Goodspeed:** So how do you, I mean, how do you find these new products? I mean, cause it sounds like you're doing these interesting projects like you're talking about. How do you find them initially? Like what, what, what will pique your interest enough where you're like, oh, okay, I should go refresh the engineer, that code, or I should go and create a PCB for a watch. Like, do you, is there something specific that you find happening over and over again? Or, or is it just kind of things that eat at your brain and you want to like, eventually you just need to make this thing in the world.

**Travis Goodspeed:** I think it's mostly like a nervous habit of taking things apart. Right. So I buy the radio, the MD380, for example, and I take it apart and I see the chip inside of it. And then I recognize that it's an STM 32. Like I've worked with that chip. I know that chip.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** So knowing the chip, I know that I can rip the code out of it. I know that I can change it, that I can reverse engineer it and patch it. And from that point, like knowing what's available or what can be done with the tools and the things that are available, like the, the idea crops up and then either I get around to it or I don't.

**Travis Goodspeed:** That's great. That's great.

**Travis Goodspeed:** I mean, where do your projects come from?

**Travis Goodspeed:** Some frustration. I mean, I've got a list of projects that are kind of just sitting in idle state. Some of it's, yeah, that are more timely. Like I think like, like I did a, a board last year where it was just other people were working on similar things. I was like, yeah, that, that sounds like something I want to do. And I was like looking for a new technical challenge. So I spun up a board and started working on it through that. Um, and then the rest is work. So work stuff is more of a, uh, yeah, there's, I should probably do this if I want to keep my job or, or make some money. You know, there's, there's that piece of it.

**Travis Goodspeed:** Yeah. Yeah. Sometimes you do have to pay the bills.

**Travis Goodspeed:** Yeah, exactly. What is the, uh, what kind of STM 32 stuff have you done in the past? Aside from the radio? Work stuff. Work stuff. Got it. Not, not talkable work stuff or? No, not really. Yeah. Okay. All right. That's all right. You've done a lot of other stuff that's non-work stuff too. So that's, uh, that's good. Yeah. So what do you, what do you think about that chip? I mean, if you're, you're using on a regular basis, I guess there's, there's a bunch of different families in there too.

**Travis Goodspeed:** Yeah. Um, for the old ones, I wouldn't recommend them like, uh, for design that you need to keep secure or prevent from being copied. Um, I really do like how, um, how easy it is to target ARM devices with just a vanilla C compiler.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Like, uh, do you remember the days of having to pay for a compiler?

**Speaker ?:** Yeah.

**Travis Goodspeed:** Yes. They're not over for everyone. I don't know if you know this.

**Travis Goodspeed:** I'm sorry. Like, I know that children might be watching and I don't want to, I don't want to use harsh language. So I suppose I should stop talking about paying for compilers.

**Travis Goodspeed:** Yeah. Um, I think that's the thing. Like this, we were talking about this, um, at, uh, Kaicon and a couple of the times too. And it's like, GCC was around a lot longer. It's just people still prefer the paid stuff. I think it's, it's come to equilibrium now, or it's maybe surpassed it where it's like, it's a viable option for a lot more people. I think, especially in a professional context to not pay for compilers. Whereas in the past it was not as much of an option.

**Travis Goodspeed:** Uh, some commercial tools have a feature that's handy. Like, um, uh, visual C++ has incredible debuggers with it. Right. If you're writing, uh, like I know people who write Unix code first on windows just for visual C++.

**Travis Goodspeed:** Oh, yeah.

**Travis Goodspeed:** Um, and I really don't mind paying extra for a tool that makes my life easier, especially for commercial products where like, you know, my, my livelihood comes from it.

**Travis Goodspeed:** Mm-hmm. Yep.

**Travis Goodspeed:** Um, what I mind is getting locked out of my own designs.

**Travis Goodspeed:** Yes.

**Travis Goodspeed:** Like, uh, like I designed some things in Eagle years ago and now I can't open them.

**Travis Goodspeed:** Yep. You're preaching, preaching to the choir on that one.

**Travis Goodspeed:** So as soon as the open tools catch up, then like I will jump ship to them in a heartbeat because I know that I will never be locked out of them. I know that there won't be a license that expires. I know that I, I can always have an old virtual machine running key cat five and 30 years from now, I will still be able to edit my designs.

**Travis Goodspeed:** Yeah. It is kind of frightening to think about some of my mechanics. So again, professional stuff too, where it's like maybe like, like 3d CAD, I'm still in a proprietary tool for that. And it's like, you know, I can get the STLs out, but then I got to either redo it or pay someone to redo it at some point. And, and you lose a lot of that. It's just a downsampling. That's what it really is. Right. Every, every like output file. If you just have Gerbers is a downsampling. If you just have an STL, it's downsampling. If you just have, you know, binaries, it's downsampling and you don't get all that other stuff that you don't get to say, look at the C code and see what it's made up. Like you said before.

**Travis Goodspeed:** Or what if you get it out and it's ever, ever so slightly wrong.

**Travis Goodspeed:** Or the chip vendor comes up with an errata. I don't know. That could, that could happen too. And you know, something's broken. It's fun. So that's, I think.

**Travis Goodspeed:** Again, children might be, children might be listening. So we shouldn't mention a chip errata too much.

**Travis Goodspeed:** Okay. Yeah. Yeah. I guess with the SCM 32, you might've, uh, it might've run into that once or twice too. I've heard some, I've heard some stories.

**Travis Goodspeed:** Uh, also in the chip con 430, like the, the real time clock and the older version of the chip, um, if your chip is running at full speed, you can almost always set the time. Wow. But if your chip is running at low speed about one time in 10, the address at which you the individual instruction that performs the right into the clock, if that address is like divisible by 16 evenly, then you're not able to update the clock.

**Travis Goodspeed:** Oh my.

**Travis Goodspeed:** That's a, this is particularly, uh, annoying because anything that you change in your code will redo the alignment and the bug will go away. Okay. So whatever you try, we'll fix it for now. And then it'll come back later.

**Travis Goodspeed:** And so you start waving your arms and something changes and you're like, oh, it's gone. And then it goes back. No, it's gone. It comes back.

**Travis Goodspeed:** Yeah. Uh, the solution from the vendor is to, um, to use assembly code to write to it. So the only assembly code that is in the good watch is to set the time to work around a hardware bug.

**Travis Goodspeed:** That's crazy. Yeah.

**Travis Goodspeed:** It's a crazy world.

**Travis Goodspeed:** Yeah. So, um, what about, uh, what about some of the other past projects? So, um, we talked about it. We talked to Mike when at, uh, at KaiCon, uh, Mike Osman was here and he was talking about the great fed a little bit, but you are the creator of the good fed. So can you tell us a little bit about where that came from?

**Travis Goodspeed:** So, um, TI has a JTAG debugger that they call the MSP430 FET or a flash emulation tool. And the good FET was an attempt to write, um, an open source replacement for that, that could be flashed without already having a chip programmer. So you should be able to solder the parts to a board connected by USB and then flash it immediately without already having a chip programmer.

**Travis Goodspeed:** The chip, the chips programming chips problem you're saying that's kind of the idea.

**Travis Goodspeed:** Yeah. Yeah. So there's, um, a mask ROM bootloader in the MSP430 that you can use to flash it over a zero port for the first time.

**Travis Goodspeed:** Huh? Okay.

**Travis Goodspeed:** Later on, it became a general bus adapter, um, so that you could write Python code on your host computer and that that Python code could interact with a spy bus or an I2C bus or JTAG, um, in order to interact with, um, a radio or a memory chip or things like that.

**Travis Goodspeed:** Yeah. The way it was explained to me, it was kind of like a prototyping tool, uh, because you can quickly just turn around and try these different protocols and throw, throw commands at external things. It was kind of a, like I said, it was like an API to the digital physical world.

**Travis Goodspeed:** Yeah. Um, so then, uh, about the time that I, I lost interest in the project because I, you know, I had a good run. I had a lot of fun with this project. We made a USB emulator called the face dancer. We made, uh, all sorts of radio adapter boards. Um, but about the time that, uh, I wanted to pass it off to find a new home or a new maintainer for it. Um, my classmate and I were hanging out in Las Vegas and, um, he mentioned that he had wanted to redesign it around new principles. Um, specifically my design was made to use as few components as possible, but I didn't consider the price of the parts if they could be sampled. Um, so he came out with the great fat, which is a re-imagining based on making it, um, mass producible.

**Travis Goodspeed:** Right. Okay.

**Travis Goodspeed:** Uh, he keeps the idea of doing like everything host side that you possibly can. And only offloading what you can't. Um, and so the, the great fat is a lot more modern, a lot faster. Um, it has support for things like, um, emulating USB devices, just sort of built in. You don't need, um, a neighbor board for it, which is what he calls the expansion boards. It's taken a few years for the, the project to be ready for a commercial release, but I think he's just about there or did you, um, uh, has he announced it as being ready yet?

**Travis Goodspeed:** Yeah. They started shipping last Monday, I believe. So beginning of May. Yeah. So yeah, it's out there. It's, I have one on my desk, actually. I have not booted it up yet, but I have, I have one of the early ones. So I'm excited to try it out.

**Travis Goodspeed:** And it's a lovely idea to, to separate the prototyping stage from the deployment stage when you're working with firmware. Yeah. Or the embedded version needs to be awkward to interact with.

**Travis Goodspeed:** And that's, and that's kind of the thing that like that, that cycling of like, write firmware, compile it down, load it over, write firmware, compile it down, load it over, you know? And like, and like, yeah, of course you can do debugging and all that other stuff. But like the idea I get from good fed slash great fed is like, it's more like throw commands, throw commands, throw commands. Cause you already have this interface that's kind of out there. I mean, and, and then I think the idea would be that Mike and the great sky gadgets, gadgets team are making a bunch of neighbors, but then eventually people can make their own as well to interface to new parts as well. Cause I assume that you were also making, you were making add on boards, like you said as well.

**Travis Goodspeed:** Yeah. And, um, and the advantage of reusing this platform for your own add on board. Is that all you have to do hardware wise is to wire it up to the right pins.

**Travis Goodspeed:** Right.

**Travis Goodspeed:** And then all of the software becomes a Python problem.

**Travis Goodspeed:** Which is exceedingly accessible these days. Uh, which is great. I think the, and you, so you could, I mean, you could also do, you could physically wire it up if you wanted to, right? You could do jumper wires to plug into the little header thingies, but from a perspective, you start to get dangerous.

**Travis Goodspeed:** Uh, and that's why he uses a 0.1 inch header to, um, I mean, you can rig one up out of prototyping board if you like. Yeah. Nothing to stop you.

**Travis Goodspeed:** So are you still, I mean, do you still prototype like that with your own stuff? I mean, like with a great, a good fed, um, in your work?

**Travis Goodspeed:** Occasionally. Um, with the, the good watch, um, it also has a host side Python environment. So like when I wrote the, the pager receiver, I did all of that in Python first without ever touching any C code until I knew what I was doing. And then I migrated things over piece by piece until it runs standalone on battery power without wiring to the host.

**Travis Goodspeed:** That's really awesome. Yeah. For that, that iteration cycle, it seems like that's like super key for, for trying lots of things. And I mean, it's always a frustration too, is like, especially as you're like reading through data sheets. And I assume that if you're, if you're playing with a moderate moderate modifying the radio stuff, you're probably just deep into the register set and trying different things. And that's always a big frustration. It's like, oh, well I got this, I messed this bit wrong or I messed that bit wrong. And it sounds like you'd be able to do that from Python now.

**Travis Goodspeed:** Yeah. And then only after it's working, do you bother moving it over?

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** The other nifty thing that you can do is, you know, I'm writing my firmware and C I can compile C to run on my desktop. So, um, my disassembler will run just as well on a desktop as it will in the watch. And that's how I test it, uh, as a regular Unix application.

**Travis Goodspeed:** Okay. I was going to say, you're just running it from the command line and just loading it up and seeing what happens. That kind of thing.

**Travis Goodspeed:** Yeah. Yeah. The, the, the make file will like automatically test all of my libraries before building the firmware image. Uh, it also gives me the compiler warnings of like the most modern desktop compiler, even though I might be using like an older version of GCC to compile and link my firmware.

**Travis Goodspeed:** And what, what are the benefits of that then?

**Travis Goodspeed:** Well, like, um, when you're writing C code, you can mess up in different ways. Oh, don't I know that one? Okay. Um, but, uh, as compilers become more advanced, they can catch more of these ways. So like the, the Clang compiler has very good error messages.

**Travis Goodspeed:** Got it.

**Travis Goodspeed:** Um, so having the Clang compiler on my desktop, I can compile my code with it and see if it gives me any warnings that GCC did not. So I've got like, uh, two different compilers, double checking that my work is accurate and clean.

**Travis Goodspeed:** Got it. Okay. So this wouldn't necessarily be like resource type errors. It's more like how your code is interacting with itself, that kind of thing.

**Travis Goodspeed:** Yeah. Like, um, sometimes you, um, you don't have the right grouping symbols for the order of operations that you intend. Oh yeah. So it looks visually like your if statement is checking one thing, but it's actually checking a different thing. Yeah. Or maybe it will always test true.

**Travis Goodspeed:** That's a, that's a, that's a really great example because that, that contributes like, and that's like the kind of bug too, where you're chasing it and you're chasing it and chasing, you're trying to find this, this thing that doesn't happen. And, or even, even worse, if it does happen once in a while, but not every time, like that you're thinking it's going to happen, just that corner case that doesn't happen. Oh man, that's, that's real tricky. So that's, that's a, that's a good, good example. Yeah.

**Travis Goodspeed:** Um, you can also throw in a bunch of assert statements that only run like when you compile it on your PC so that my firmware isn't bogged down by all of these checks, but that if I made a mistake, it will come out when the test runs on my desktop.

**Travis Goodspeed:** So what does that, what does the process look like then? So if you're writing Python, I mean, so you're writing high level Python to test these different things, you know, getting it down into the watch. What does the conversion process look like then? Is it just kind of refactoring? I mean, obviously the languages are different, but, but is it, uh, each, each test that you might be running in Python just becomes a module, uh, or like a subroutine in C? How do you have any like formula of how you kind of transition from one to the other?

**Travis Goodspeed:** Um, okay. So you've written like a sloppy code before at some point in your life, right?

**Travis Goodspeed:** Almost exclusively. Yes. Okay.

**Travis Goodspeed:** Um, and at least once you've written like, um, proper code where you were careful to cross every T and dot every I?

**Travis Goodspeed:** Yes. Yes.

**Travis Goodspeed:** So what I do is I write it first in Python as a throwaway, like as a rough draft when you're writing fiction.

**Travis Goodspeed:** Yeah. Okay. That's a good analogy.

**Travis Goodspeed:** And I know that I'm not going to keep that code so it can be as ugly as I like. And I'm only doing that to make sure that I have the right radio settings.

**Travis Goodspeed:** Got it.

**Travis Goodspeed:** Or to make sure that I understand the problem that I'm trying to solve.

**Travis Goodspeed:** Mm-hmm. Yeah.

**Travis Goodspeed:** And then that gets me like a minimal viable receiver that gets me, uh, like one raw packet off of the pager.

**Travis Goodspeed:** Uh-huh.

**Travis Goodspeed:** Then I rewrite that cleanly and slowly in C because all of my experimentation is now over and I understand the thing that I'm trying to write.

**Travis Goodspeed:** Okay. That makes sense. So it's, it is, I mean, it is refactoring. So it's basically, you're taking like the essence of the thing that you had tested and then you are just carefully making sure you get the same output and that kind of thing as well.

**Travis Goodspeed:** Yeah. And it's a, it's a total rewrite. It's not a refactoring.

**Travis Goodspeed:** Okay. That's yeah. That's kind of what I was getting at.

**Travis Goodspeed:** Um, the, the Python code only exists for experimentation and in the watch, uh, cause you're not going to wear a watch with wires running out to a computer somewhere.

**Travis Goodspeed:** Mm-hmm. Well, yeah. I mean, you, you might, but I mean, some people do. Yeah. That's cool.

**Travis Goodspeed:** So not exactly fashionable.

**Travis Goodspeed:** Right. What else do you do in the ham radio community? I mean, it sounds like you're, you're pretty deep in the community as well. How long have you been a ham?

**Travis Goodspeed:** I think I got licensed for the first time at Sky Dog Con maybe five or six years ago.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Um, I made a, uh, shortwave station in a converted TV news van. Um, nice. So it's got a 50 foot microwave tower and then it's got like an air conditioned office in the back with all the equipment on it.

**Travis Goodspeed:** Wait, you, you bought this or wait?

**Travis Goodspeed:** Yeah. Yeah. Like I bought an old, uh, TV news van from ABC seven in Chicago.

**Travis Goodspeed:** Oh my God. That's awesome. That's like the ultimate, uh, like a hacker camp vehicle, huh?

**Travis Goodspeed:** Yeah. Unfortunately, thanks to the road salt of your fine town, the, uh, the legs no longer work, but the tower works fine. Got it. And, um, yeah. A fun little thing to drive around. My brother hooked me up with, um, Ghostbusters decals for the doors.

**Travis Goodspeed:** That's great.

**Travis Goodspeed:** And, um, uh, some local guys were converting a food truck, uh, out of an ambulance. So I have an ambulance light bar on the roof.

**Travis Goodspeed:** Nice. This is, must be a something quite, quite something to see coming, huh?

**Travis Goodspeed:** Yeah. Yeah. When I drive around, people yell, uh, who are you going to call?

**Travis Goodspeed:** What, uh, so what have you used the microwave for? I mean, have you actually transmitted with it?

**Travis Goodspeed:** The mass rotator is damaged at the moment. Um, so my, my initial plan for this was to raise a directional antenna up, like above the, the tree line and then spin it around in order to triangulate where different microwave transmitters were located. So you can sort of like park the car at like three or four different locations, raise the tower, spin it around.

**Travis Goodspeed:** Yeah. And then, uh, modified war driving.

**Travis Goodspeed:** Yeah. Yeah. Uh, it's got war driving stuff in it. It's got, um, solar charging.

**Travis Goodspeed:** It's great.

**Travis Goodspeed:** For a separate electrical system. And I can jumpstart the main battery from the radio battery.

**Travis Goodspeed:** That's, that speaks to the, uh, to the, the juice you got there, huh?

**Travis Goodspeed:** Well, you know, if there's a zombie apocalypse, you might not be able to start your car every couple of weeks in order to keep the battery fresh.

**Travis Goodspeed:** Right. Right. And if it's a movie about the zombie apocalypse, it's almost guaranteed that you're not going to be able to start the car the first time until they get just to the car. And then, and then you will.

**Travis Goodspeed:** Right. Right. And then in the TV shows, like, um, you know, six years after the zombie apocalypse, the thing still starts on the very first try, as long as they jumpstart it just right or hotwire it, hotwire it.

**Travis Goodspeed:** Right, right, right, right. Yeah. Gas doesn't go bad or anything in the, in the movies. Well, um, what, let's talk about your, I mean, so you've given a bunch of talks as well. Like what, what do you, it sounds like some of the stuff you've spoken on is, is the, uh, you know, the, the radio stuff and the, and the, the watch, um, other, other talks that people should watch. I mean, we're, I'm obviously going to link all of these in, but, uh.

**Travis Goodspeed:** Yeah. Um, so, uh, Sergey Bratis and I started a project called the face dancer, which was a USB device emulator from Python. The idea was that you could write like a fake USB device as a Python module on one machine and the other machine would believe that it were real.

**Travis Goodspeed:** Wow.

**Travis Goodspeed:** Um, Kate Temkin has now taken over this project. Um, she, she works a lot with Mike Osmond and the great Scott gadgets folks. Mm-hmm. And it now runs on the great fat hardware so that you don't need any custom hardware for it at all.

**Travis Goodspeed:** So like what would be the, uh, what would be the usage of the face dancer project?

**Travis Goodspeed:** Like to, well, um, the initial idea was security vulnerabilities. Um, at the time there were a couple of USB vulnerabilities coming out. Like, um, uh, Colin Muliner came out with, uh, what's called a time of check to time of use attack against a smart television. He basically made like a fake thumb drive and speaking the USB mass storage protocol, which the face dancer can also emulate. And he put a plugin for the TV and the plugin was very large so that it couldn't fit in Ram. And the first time it was read, he would present a perfectly innocuous and legal plugin. But the second time that it was read, he would present the one that he actually wanted to install.

**Travis Goodspeed:** Because it was just going to do an automatic retry. Is that kind of the thinking?

**Travis Goodspeed:** No, no. First it checks to make sure that it's good and then it installs it only if it's good.

**Travis Goodspeed:** Oh, okay. Okay.

**Travis Goodspeed:** But there's no reason why these have to be the same thing if you control the USB disc.

**Travis Goodspeed:** Right. So it's like a bait and switch, but a digital bait and switch. Yeah. Yeah. That's cool.

**Travis Goodspeed:** So Colin did this against a TV. There was an attack against the PlayStation 3 that involves creating a USB hub and then making devices appear and disappear in order to corrupt memory. But there were no good development tools for this that would allow you to write the exploit for the first time or to experiment with it.

**Travis Goodspeed:** Yeah. To try all the different things you need to try in order to iterate and see what was going to work.

**Travis Goodspeed:** Yeah. And you want to do that from like a nice big computer instead of from a small embedded system.

**Travis Goodspeed:** So what does it actually look like? So is there like a processor serving up what looks like a USB stack to the device? Let's see. So you'd be emulating a device and then the thing that you're attacking is the host, right?

**Travis Goodspeed:** Right. Right. So the initial prototype was a good fat connected to the developer's workstation. And then there was just a USB device chip. Okay. Max 3420.

**Travis Goodspeed:** Uh-huh.

**Travis Goodspeed:** That would appear to be the USB device to the other computer.

**Travis Goodspeed:** Oh, because you could dynamically change registers in that device chip that's serving up. It looks like a USB device chip anyways, right? And you're just then forcing in the payload that you want to have through that chip, right?

**Travis Goodspeed:** Yep. And USB 1.1 is very generous about a device being too slow. So that generosity we abused to provide a remote control from Python.

**Travis Goodspeed:** Like what are the relative speeds here we're talking about?

**Travis Goodspeed:** My initial prototype, if I'm going to be perfectly honest, slow as dirt. That's a technical term. It is. With the modern GreatFet, though, I believe he can get tens of megabytes per second.

**Travis Goodspeed:** Okay. Are there devices, so to use a smart TV as an example, have they changed anything in the meantime? Or is this kind of thing still available? You plug in a USB cable, you plug into a GreatFet, you have this Python script running, or this Python environment running and delivering a payload of bad stuff to it. Most TVs still are vulnerable to this or not?

**Travis Goodspeed:** Well, the TV that Colin attacked, they patched the bug.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** There are other devices, though. Like Kate Temkin, who now runs the Face Dancer Project. I believe that her initial interest in it came from attacking the Nintendo Switch.

**Travis Goodspeed:** Oh, interesting.

**Travis Goodspeed:** So she was able to find a bug in a USB driver that the Switch had. And then she could abuse that by emulating the device that connected to it.

**Travis Goodspeed:** And I bet the engineers that make these end devices, too, they're just never thinking. I'm sure that they're told about security, but I doubt they see people like Kate or you or Colin coming. You know? Why would someone do this? How would someone do this? You know? And then it's just like, yeah, custom hardware is kind of the ability to take and attack these environments like that.

**Travis Goodspeed:** Yeah, that's part of it. But there's also like, you know, they have to ship a product. And all I have to do is like build a prototype that can make fun of that product. It's a lot harder to build something that you can ship than to show that there's a mistake in that thing that was shipped. Yeah, sure.

**Travis Goodspeed:** Of course. And that's, yeah, that's a fair assessment. I mean, I think that gives the engineer some credit. But still, I'm just amazed that like the ingenuity of these kind of projects that you guys have done to allow testing in this way. So it's, I mean, what it effectively does is like these are open source tools that are out there and accessible to people and now accessible with Python even. And I think about the test companies that would have been, you know, in the same space 20 years ago or when USB came out, you know, 15, 20 years ago, right? And like they probably weren't given Python interfaces to things. And, you know, it's like it was more about like these modules that you had to buy for scopes and other physical hardware. So it's just, it's a good time for tools like yours that are helping people making testing more of a thing.

**Travis Goodspeed:** Oh, it's an amazing time to buy tools. Yeah. Like I drive a Studebaker, like the greatest American car brand that went out of business.

**Travis Goodspeed:** Right. And there's a picture of it at the top of your Twitter profile, which we will link in down below, of course, too. So it's a good image.

**Travis Goodspeed:** So we'd have this problem called vapor lock. Vapor lock is where the fuel pressure drops to be too low.

**Travis Goodspeed:** Mm-hmm.

**Travis Goodspeed:** And your gasoline can be rather hot as long as it's under pressure.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** At regular room pressure, gasoline will boil at like 100 degrees.

**Travis Goodspeed:** Fahrenheit or Celsius just for the...

**Travis Goodspeed:** Oh, Fahrenheit. Like 100 degrees Fahrenheit. Got it. Like on a hot day, gasoline will boil if you leave it out.

**Travis Goodspeed:** Oh. Yeah.

**Travis Goodspeed:** So when that car was made, if you had this problem, you just had to think really hard about it. And thinking really hard about it, you'd realize that maybe the fuel pump was bad or maybe there was a clog in the line.

**Travis Goodspeed:** Mm-hmm.

**Travis Goodspeed:** But that something was preventing the fuel from getting through. Now in the modern world, I can go online and buy a little gizmo with a thermocouple and have an accurate log of my fuel temperature dating back a week retroactively. Yeah. Whenever I care to yank it out of my car. I mean, the sort of like oscilloscopes that you can buy, the random radio test equipment, it's just available for nothing.

**Travis Goodspeed:** Right. Yeah, it's crazy.

**Travis Goodspeed:** Like we've really got a good test equipment wise.

**Travis Goodspeed:** Yep.

**Travis Goodspeed:** Tom and Ray, are you a Car Talk fan? I'm not. I haven't listened to them. I have nothing against them. I just haven't gotten into it yet.

**Travis Goodspeed:** That's the only reason I know what Vaporlock is. It's because of Car Talk. And yeah, in the same way, it's like you didn't have that tribal knowledge like you're talking about. It would have just been like, yeah, take it to a mechanic, you know, like to talk to an expert. But how do you like get access to that knowledge? It's not like you're saying. It's low cost test equipment that you can kind of just monitor with.

**Travis Goodspeed:** Yeah. And I have to learn it myself because within my lifetime, every auto mechanic who has ever worked with a carbureted car will retire.

**Travis Goodspeed:** Yeah, that's true. That's a good point. I mean, I'm guessing you're going to be keeping these Studebakers around for as long as possible.

**Travis Goodspeed:** Yeah. Yeah. Like ages from now, when I break out of a nursing home and like go on a cross country ride in a blaze of glory, it will be in a Studebaker.

**Travis Goodspeed:** Got it. Any plans for electric conversion or anything? I mean, I'm hoping by the time you break out of a nursing home, there isn't any gas to be seen, but I'm not that optimistic about it.

**Travis Goodspeed:** That's a good point. I should probably buy one of those like Len Lee's wartime models that could run on everything from moonshine to cooking oil. Yeah. Yeah. They had them to where you could adjust the distributor timing from inside of the cab. Oh, really?

**Travis Goodspeed:** That's amazing.

**Travis Goodspeed:** Yeah. That's amazing. As you're barreling down the road.

**Travis Goodspeed:** Yeah. What got you into those in the first place?

**Travis Goodspeed:** We had one when I was a kid. And when I moved back to Tennessee, my brother and I thought it'd be cool to get back into them.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** And they're beautiful cars.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** It weirds me out how similar all modern cars are to one another.

**Travis Goodspeed:** They're all merging into the same like SUV-ish shape, you know?

**Travis Goodspeed:** Yeah. That same little bubble. And it doesn't matter whether it's like something domestic or something really exotic like a Lada or a Skoda, like a French or a Slovakian car. Like they all look the same.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Until you look at the badge, you can't tell the difference.

**Travis Goodspeed:** Yeah. Yeah.

**Travis Goodspeed:** I mean, there was a time when people would know the name of the guy who ran the design studio who designed the body of the car.

**Travis Goodspeed:** Just from the look you're saying? Yeah. Yeah. Yeah. I think with aerodynamics and crash safety ratings and everything else, they all kind of merge towards the same, not standards, but practices. And that kind of makes a lot of the same features.

**Travis Goodspeed:** Well, crumple zones are very important to safety. But my hope is that if, God forbid, I am in a collision, the other car will have crumple zones.

**Travis Goodspeed:** That's right. Well, I'm sure a student baker's got some steel in it. You know, it's got some heft, right?

**Travis Goodspeed:** Yeah. Yeah. One of us will be driving away from the collision.

**Travis Goodspeed:** That's right. That's right.

**Travis Goodspeed:** There's other cool stuff from back then. Like, you know, the controls for the high beams and the lights. It's a foot switch.

**Travis Goodspeed:** Really? That's interesting.

**Travis Goodspeed:** Your left foot switches between high beams and low.

**Travis Goodspeed:** And so, wait, is it like there's got clutches to it, right? So, they're four pedals?

**Travis Goodspeed:** No, no. Mine are automatic.

**Travis Goodspeed:** Oh, it's automatic. Okay. Yeah. That would also be dangerous, too, if someone thought it was a e-brake or something. And, you know, like you're going into a crash. You're like, no, no, no, e-brake. And then high beams go on.

**Travis Goodspeed:** I think what happened was that, like, way back when, like in the 20s or the 30s, that would be the button that would run the starter motor. And that they had a bunch of these buttons left over when they switched to more modern key locks. And you got to do something with them. So, you might as well make it control the high beams.

**Travis Goodspeed:** Use them again. Right.

**Travis Goodspeed:** Or the gasoline goes in the back so that you don't have to remember whether the gas port is on the left or the right side of the car.

**Travis Goodspeed:** Yeah. You just got to remember to pull forward a little.

**Travis Goodspeed:** That you do.

**Travis Goodspeed:** Yeah. What is it like in, I mean, so, we should finish up here. I know you got other stuff going on. But Tennessee, is there a tech scene there? Or is it just because family ended up back there?

**Travis Goodspeed:** I mean, Knoxville is a very modern city. We've got someone doing something of everything. But I think when you're, like, in college or just out of college, it makes a lot of sense to choose a city where the city might focus on your hobby. I think this is why people move to, like, New York or to the Bay Area or things like that, to Berlin. But I don't think that this makes as much sense later in your career after you already know your trade. Like, I would much rather be able to have free parking and elbow room at my neighborhood bar. Dogs being allowed indoors and, you know, affordable rent.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Than to have, than to be surrounded by people who shared my hobby.

**Travis Goodspeed:** Well, and it sounds like, I mean, I don't know about you, but I travel to see people, like, within my hobby, I guess. You know, at conferences and stuff like that. It sounds like you do quite a few conferences. And it's like everything else is kind of the, the everything else time is the work time and the family time and stuff like that. And I think that a lot of our listeners that are, you know, have families and they, they are disparate as well. I think that a lot of people listen to the show because there aren't as many centralized hubs as people would like when, you know, life has other, other things going on.

**Travis Goodspeed:** Yeah. And while under no circumstances, but I recommend leaving family and friends to indulge in your hobby, like after you've made a career out of it. Conferences are great just for having an in-person discussion with someone who cares about the same weird thing that you do.

**Travis Goodspeed:** Yep. Yep. Yeah. There is, there are a few great feelings in the world to find another weirdo that's like, oh, wow, you're, you're like me. This is great. And then you have that conversation for a couple hours, you know, it's, it's awesome. Uh, what, uh, what conferences are on your schedule? I guess maybe where people might catch in the, in the coming months or years.

**Travis Goodspeed:** I think, uh, recon in Montreal. It's a reverse engineering conference that teaches you how to, um, take software and hardware apart. That, that one is always fantastic.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** I, my, my conference schedule is lightened up a lot lately. Yeah. I need to, uh, maybe book some more of those.

**Travis Goodspeed:** No, no chaos campus here. Any, any chance of that?

**Travis Goodspeed:** No, no, I might do, um, uh, camp plus plus, which is in, uh, Komarum.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** It's, um, a town in the North of Hungary. Cool. They do it at like an old Soviet ammo dump.

**Travis Goodspeed:** That's awesome.

**Travis Goodspeed:** Yeah. They've, they've got, um, do you remember when the, the CCC camp was back in Finovac?

**Travis Goodspeed:** I, uh, if I go this year, it'll be my first time.

**Travis Goodspeed:** Okay. So they used to do it at like an old, um, GDR air base and they had MIGs and stuff and statues of Lenin. And people would put, um, like headphones and a hipster scarf and thick rimmed glasses and a DJ table on Lenin. Oh my God. Wow. I mean, if you're going to have to be, if you're going to have to see that statue of a mass murderer every time you walk by, you might as well make them look funny.

**Travis Goodspeed:** Yeah. Lighten the mood a little bit. Come on.

**Travis Goodspeed:** Yeah. Um, so at the, um, the fort in Komarum, they don't have like the old statues, uh, but they do have old radar trucks that the USSR left behind when they evacuated.

**Travis Goodspeed:** Wow.

**Travis Goodspeed:** Uh, and it's a much smaller camp, um, um, maybe 150, 200 people.

**Travis Goodspeed:** Oh, wow. Okay. That's great though. Like that size conferences, like those, those conversations where you're having two hour, three hour conversations with someone and you really get to know people that can be a really good size for that kind of thing.

**Travis Goodspeed:** Yeah. And also like, um, when something scales to a certain point, no matter how well you run it, um, you kind of have to make it more professional. Uh, whereas when something is very small, like, um, it can be like, uh, a little less organized and a little more, uh, free for all.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** Without people taking advantage of that or being jerks about it.

**Travis Goodspeed:** That's a good point. Well, Travis, I, uh, I, I really dig your worldview. Um, you, uh, you seem, you seem to like, like just even that, like about the conference stuff, like that's, that's a really good view on life. I like that. So thanks for talking to me here today. Where can people find you online if they're, they're looking to get in touch?

**Travis Goodspeed:** Um, my Twitter username is Travis Goodspeed and that's probably about the best place.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** Um, and if, if I could end with one, uh, plea. Sure. Um, uh, if anyone listening now is from Texas Instruments, you folks used to have the very best electronics education conference in the world disguised as a sales pitch. And I, it's the reason why I use Texas Instruments parts in my design 11 years later.

**Travis Goodspeed:** Yeah.

**Travis Goodspeed:** If you could please bring it back, I would be so forever grateful.

**Travis Goodspeed:** Okay.

**Travis Goodspeed:** I would even go back to Dallas for it.

**Travis Goodspeed:** Please. That's a big one, man. That's a big one. Yeah. I, I, I, that's a great, great call. Um, yeah, I'll see if hopefully there's some people out there listening. We'll see.

**Travis Goodspeed:** Yeah. I love Texas. Dallas is just too flat.

**Travis Goodspeed:** Yeah. I was more of an Austin man myself. All right. Well, thanks Travis. We'll talk to you soon.

**Travis Goodspeed:** All right. Thank you. Bye.

**Travis Goodspeed:** Bye.
