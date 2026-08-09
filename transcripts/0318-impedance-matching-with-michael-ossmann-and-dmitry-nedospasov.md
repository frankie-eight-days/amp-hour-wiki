---
episode: 318
title: Impedance Matching with Michael Ossmann and Dmitry Nedospasov
url: https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded October 5th, 2016. Episode 318. Impedance matching with Michael Osman and Dmitry Netospazov. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Dmitry Netospazov:** And I'm Dmitry Netospazov of Toothless Consulting. And I'm Michael Osman of Great Scott Gadgets.

**Chris Gammell:** And this is another impedance matching episode where we bring former guests back on. Obviously, Mike's been on a couple times now. Dmitry's been on once. But we're going to talk about shared interests and shared topics. And, well, I'm guessing today it's going to be a little bit of hardware security RF stuff. What do you guys think? It's an Amp Hour takeover. Suddenly, the Amp Hour is a hardware security podcast. You know, we keep edging towards it. We still have no idea what's going on with that side of things. But I guess that's good why you guys are here. So, welcome back.

**Dave Jones:** Thanks.

**Chris Gammell:** Thank you very much for having us. Dmitry, you're in Moscow right now. Mike, I believe you're in the middle of a dog kennel right now in Colorado. I'm near a dog kennel. No, I believe you're in a dog kennel. We'll hear.

**Dave Jones:** Well, you know, the rent is cheap. Dogs can't solder for shit, though. We've learned that.

**Dmitry Netospazov:** What do you do about hair getting in under the solder balls?

**Dave Jones:** Oh, man. I've been living with electronics and pets for years. It's nothing new.

**Chris Gammell:** Yeah. Yeah, nothing like a little bit of dog hair on a soldering iron in the morning. You get that nice burn hair smell. That's really better than coffee. So, Dmitry, what's going on out in Moscow, man? So, people may remember you're normally in Berlin, but you also work a lot in Moscow. You're from Moscow sometimes. And so, what's going on out there?

**Dmitry Netospazov:** No, I mean, yeah. I just try to split time. I have family here and stuff like that. So, when I have an opportunity or client work that allows me to work remotely, then I do it from here sometimes.

**Chris Gammell:** Nice. Does that mean you have double labs? How does that work?

**Dmitry Netospazov:** Kind of. I mean, so, I don't remember if I told this story last time, but I had a problem like two years ago bringing an oscilloscope across because Russian Customs got me with my Rigel 2000 series. And then I had to pay 150% of what the oscilloscope costs on top of that as a, yeah, whatever you call it. I had to pay a fine.

**Chris Gammell:** It was like VAT sort of, but it was a fine too.

**Dmitry Netospazov:** No, no. Yeah, I mean, it wasn't just, yeah, it was VAT plus a fine. And then, anyway, long story, pain in the butt. So, I kind of learned my lesson in that I will never try to transport an oscilloscope again. But I did just bring a new microscope that I got, which we can add to the show notes. So, I was looking, I've been doing a lot of micro soldering and really small stuff, which I'm new to. So, I got a new micro soldering iron from Ursa. And I got a microscope to do micro soldering as well. And the microscope I brought with me, because there are certain things that are a pain in the butt to buy in Moscow, actually. And one of which is microscopes. So, the microscope I got is a Brazzer. I don't remember the exact one. I think it's like ICD something. But I brought that with me this time. And then, after I got my bag and I'm going through customs, they're like, put your bag on the x-ray machine. Or put your bag on the x-ray machine. And then, I was already sweating. And then, she's like, what the hell is in your bag? And I'm like, a microscope. And she's like, all right. And I'm like, all right. I got through this time. But I'm not going to risk it again. Totally, totally reminiscent of that situation last time. It was the worst. I mean, when I got caught with the oscilloscope last time, it was at 5. I flew in at like 3 or 4 in the morning.

**Chris Gammell:** Yeah, that's when I'm looking for that stuff. You've got to come in at like 9 a.m. No one's sneaking stuff into a country at 9 a.m.

**Dmitry Netospazov:** I mean, so, Moscow has three international airports. And there are flights going. There are a lot of flights going in and out of two of them. And so, but one of them got busted with a corruption scandal where they were, like, letting stuff through and taking bribes and stuff. And so, that's the one that I got caught on. So, they were totally, they're totally, that's the idea. They're much more hardcore about checking your bags there. So, but, yeah. Anyway, it happens that they check your bags. And then, having something like a oscilloscope. I mean, the funny thing about the oscilloscope is they didn't bug me because it's an oscilloscope. They bugged me because in the x-ray machine, thanks to all the shielding, it just looks like a black box. So, they're like, what the hell is in your bag? So, and then you tell them it's an oscilloscope. And they say, a sila what? And then, yeah.

**Chris Gammell:** Yeah. Well, at least you didn't get arrested. I guess maybe you should have known better, man. Why didn't you ship it, you know?

**Dmitry Netospazov:** Like, shipping it's still a pain. I mean, that is the official way to go. At least if you're shipping stuff to Russia is you ship it and then you, but you have to have a company clear it for you. And the rates are pretty high. So, you have to pay that on top of whatever it is. And plus, the clearing company will take, I mean, you'll end up paying close to 200% of whatever it costs elsewhere.

**Chris Gammell:** Dang.

**Dmitry Netospazov:** So, yeah. So, it's much, I mean, if you can find it, it's much easier to go wholesale. So, for example, the Rigols you can get for 100,000 rubles. That's like 12 or $1,300 or euros, I would say. So, that's maybe like 25 to 40% on top of what they would cost, at least in Germany or in the EU.

**Chris Gammell:** Is this for a 1054 or something or what?

**Dmitry Netospazov:** No, like a 2072. I get the 2072 because if you read Dave's forums, you can figure out how to unlock the features on them.

**Chris Gammell:** Gotcha. Gotcha. Well, that sounds like a lot of hassle just to bring a scope in, but I guess you have it there now. So, hopefully, it's getting good use.

**Dmitry Netospazov:** Yeah.

**Chris Gammell:** Mike, you're in a new space too. Obviously, we mentioned the puppy brigade, but you just moved spaces too, right?

**Dave Jones:** Yeah, we have a brand new lab for Grayscott Gadgets. Nice. I have my own little office, which is great except for the windows right next to the dogs. That's okay. But we have a ton more space and we've got a big laser cutter going and we have a proper warehouse and all kinds of stuff. It's great. Are you manufacturing out of there or what? No. I mean, we'll probably do some light laser cutting, like enclosures, for example. But other than that, we're not going to get into production.

**Chris Gammell:** Well, that's a good... I mean, I'm guessing the mountains of Colorado, not great for logistics, right? But, you know, not a lot of heavy duty UPS deliveries, I'm sure.

**Dmitry Netospazov:** I don't know. Mike's pretty close to the airport, though.

**Dave Jones:** I'm like an hour from the airport. All right. That's not that close. But at least it's a decent sized airport.

**Chris Gammell:** Yeah.

**Dave Jones:** And one of the things we're most excited about in our new space is that we actually have a ground level entry. So that does make shipping and receiving a lot easier.

**Chris Gammell:** Oh, versus having to like...

**Dave Jones:** Having to haul stuff upstairs every time. Yeah. Yeah. That was a lot of fun in the old space.

**Chris Gammell:** Yeah. Right. Lofts are so glamorous. Right. That's great. So Great Scott's growing or what's up in the Great Scott world these days?

**Dave Jones:** Yeah. We've got three of us here full time. Soon to be four of us because Dominic Spill is joining us in Colorado. Oh, no way. Which is exciting. He was actually kind of the first person to work for me as part of Great Scott Gadgets, but he's been a foreign contractor for some years now. And we got him a visa. So he's coming to the U.S. and is going to live in Colorado and work at our lab.

**Chris Gammell:** Awesome. What kind of visa is it? I mean, I've been talking to someone recently about visa woes. And he was talking about even trying like one of the celebrity visas. You know what? Have you heard? I don't know what those are called. Yeah. Yeah. But I mean, that's a no problem.

**Dave Jones:** That's what we got to Dominic.

**Chris Gammell:** Is it really? Yeah. Okay. So tell us about this because this is actually interesting. I've heard about this. So this is now the third time that I've heard about this as a possible thing. What is the type of visa and then how does it actually work?

**Dave Jones:** So the visa is an O-1.

**Chris Gammell:** Okay.

**Dave Jones:** And in particular, an O-1A. And it's a visa that the U.S. offers for folks who have some sort of exceptional ability. And invisibility or walking through walls or whatever.

**Chris Gammell:** Yeah, exactly.

**Dmitry Netospazov:** O stands for outstanding, by the way. Is it really? Yeah.

**Dave Jones:** Yeah. So the idea is like if you've won a Nobel Prize, it should be easy to get a visa to the U.S. And if you haven't won a Nobel Prize or something similar, then there are various criteria where you have to meet like a minimum of three out of these eight criteria to qualify as having that exceptional ability. And then you have to, of course, provide documentation, justification that you actually meet those requirements. But if you can, then it's a relatively easy visa to qualify for, largely because there's no quota on O-1 visas.

**Chris Gammell:** Right. In comparison to like H-1Bs, which are 50,000 now or something like that? Something like that. Yeah. There's a whole lottery to see if you get one. Right. And then like Oracle is putting in like 20,000 applications out of those 50 slots and other big companies are doing the same thing, right? Yeah. Right.

**Dmitry Netospazov:** I mean, it's way more complicated. I mean, so if you actually read the, I mean, you can read about some of the rules. So there's some system, people are going to kill me for not being exactly right on the details. But there's a system where if you pay either the State Department or Homeland Security or whoever the organization is, then you get a certain number of tickets per year, etc., etc., etc. So it's like the quota is very strict. And it's like pre-allocated in a way.

**Chris Gammell:** So it's easier to be famous. Is that what you're saying? Well, I think so.

**Dmitry Netospazov:** I mean, if you guys want to know the easiest way, because I mean, I would say degrees are meaningless. You qualify for an O-1 if you have a PhD. Really? Yes.

**Chris Gammell:** Oh, wow. That's a good start.

**Dmitry Netospazov:** Yeah. I mean, for the most part. There's, of course, exceptions, right? I mean, you still need like a letter from the potential employer saying this is really like an outstanding individual and references work and whatnot. But basically, at the end of the day, you can say, I have a PhD. I'm an outstanding individual.

**Chris Gammell:** I'm an expert in this very, very, very narrow area. Right. I'm the world's biggest of what a PhD is, right?

**Dave Jones:** Well, and like two out of three of those eight requirements are having publications in your field and having significant scientific contributions in your field, which often come from your publications. So you can kind of nail two out of three of those if you're a published research scientist of some sort. Yep.

**Chris Gammell:** Okay. That's great. Well, it's good to hear about Dominic, too. So I met with you and Dominic, and I had talked to Dominic online before, but he did some of the – is it HackRF firmware? Is that right? Or other stuff?

**Speaker ?:** Yeah.

**Dave Jones:** He works a lot on HackRF firmware and software and on GreatFed and UberTooth. Actually, the reason I hired him in the first place years ago was to become the project lead for UberTooth as I was getting pulled in other directions.

**Chris Gammell:** Gotcha.

**Dave Jones:** Yeah, that's great. That's really good news. Yeah. Really.

**Dmitry Netospazov:** Are they still doing the training with Mike Ryan on the Bluetooth stuff?

**Dave Jones:** Yeah. I think Dominic and Mike are planning to probably do more of those, but they don't have any on schedule right now. Okay.

**Chris Gammell:** Well, trainings is – that's a good segue there. So you guys are – so Dimitri got in contact with me because he's like, hey, we're going to be at TorCon, which is coming up to San Diego. And me and Mike will be there. We should do a show. And I'm like, that's a great idea because Dave couldn't make it this week. And so you guys are gearing up for trainings, but tell us about TorCon and tell us about your trainings because I think you guys keep changing what you do for trainings, right? I mean, I think we've talked about them before, and this is just an interesting thing to me in general that this is a big piece of these security conferences.

**Dmitry Netospazov:** I haven't changed my training in a while. No, I'm just kidding. I redid it, but more or less the topic's the same. So the main training that I still do nowadays is one where I basically teach people how to use FPGAs to build custom protocol analyzers and custom peripherals. And, I mean, basically what I feel a lot of security people get stuck with once they're – I mean, so let's say you're doing some sort of embedded analysis or you're looking at something where you have proprietary or some not super common protocols, something related to SCADA or industrial control systems or automotive maybe, and now you want to do security analysis. And so one of the problems that you run into is if you want to do security analysis, then you actually want to potentially send packets that are in some way malformed or wrong or where the number of bytes doesn't actually match what's in the packet, et cetera, et cetera, et cetera. And so you'll find that if you use commercial tools, you can very rarely do that. So I teach people how to build – I mean, I teach them HDL on day one, and they have three days. At Torcon, I do HDL – so I do a three-day training at Torcon. Normally, it's a four-day training. So I usually do one day of theory and then three days of assignments. And so at Torcon, I'll do one day of theory and two days of assignments.

**Chris Gammell:** And so when you say the commercial tools don't usually work for these applications, that's because like a spy bus analyzer is going to just put good stuff on the spy bus? Is that the idea or what?

**Dmitry Netospazov:** Yeah, I mean, that's the gist of it. And a lot of times you'll find – I mean, for example, in this kind of space, you'll find things like a vendor will roll their own encryption, but the bus is going at a speed, which is if you were to do it all, I don't know, using something like – I mean, if you want to decode the data in real time, you're pretty much screwed unless you're going to use something like an FPGA. So that's kind of the –

**Chris Gammell:** Ah, I see. Okay. So just because of the hardware versus software kind of processing times and stuff like that.

**Dmitry Netospazov:** Yeah, I mean, so doing real-time analysis. But what I say to people is – I mean, usually the people that I have come to my training are people with a software background, so people who sit there reverse engineering code all day is, I would say, my biggest group. And so they don't even know so much about hardware. And so I kind of – by throwing them in the deep end and if they manage to swim, which they mostly all do, it turns out that they leave the training and they understand what voltage levels are and what serial protocols are and all these things and all of a sudden they are quite knowledgeable in the area of – I mean, they can skip – they can blow straight through beginning in electronics and go directly into let me implement my first protocol analyzer or something like that.

**Chris Gammell:** I see. Because they're basically – you're just giving them another tool in the toolbox, right?

**Dave Jones:** Right. Exactly. Cool.

**Chris Gammell:** Mike, what are you doing these days?

**Dave Jones:** So I'm still doing my two-day SDR class. It's an intro to software-defined radio primarily for folks in the security community or for anyone else who's new to SDR. And it's the class that my online video series is based on. Okay. So it's content that I've been doing for a while, some minor updates, but largely the same goals. Okay. Is it HackRF based or are you using one of the other boards? Yeah. I use HackRF for my class, which was one of the reasons I wanted to design HackRF in the first place, was to have something kind of ideal for my class. Flexible. My class. Right. Yeah. Makes sense. I'm doing it at TourCon in October. And then in November, I'm doing it at POC in Seoul. Oh, wow.

**Dmitry Netospazov:** At TourCon, you mean next week, Mike? Yeah, that is next week. Yeah.

**Dave Jones:** Yeah. Don't forget. Don't forget to book your flight, buddy. Right. And also in London in November. Wow. At Black Hat Europe.

**Chris Gammell:** That's a lot of training.

**Dave Jones:** Yeah. That's... I don't know that I've ever done three classes in a one month period before.

**Chris Gammell:** It's a lot. Well, I guess you'll find out if it's doable. Yeah. And that was the last we've heard of Mike. He had a good run, though. It was a good run.

**Dmitry Netospazov:** But it's... I mean, I don't remember if we discussed this last time I was on, but especially in the security market, there's... Uh-huh. For a lot of people, there's just a requirement that they take training. So there's just a requirement for their certification as being credible security professionals. They have to take this amount of training per year. And so, especially in North America, where that's a big thing, there's a lot of people wanting to take training. And in addition to that, I hope Mike will agree with me if I say, it turns out that if you build some hardware, then a lot of people just want to professionally pay for the author of whatever this hardware is to teach you how to use it.

**Chris Gammell:** Yeah, I think that's true. Why versus someone? Just because of the underlying knowledge you mean? Or because of like... Is it like towards prestige? Or I don't quite understand what you mean there.

**Dmitry Netospazov:** No, just... So basically, you have somebody who's, you know, who had the idea to build this tool and somebody who's clearly very knowledgeable and who can show you a bunch of use cases about how you can use it. That's what a lot of people want to see. So they want to get it at the source kind of versus... And I mean, as somebody who teaches trainings and has taken trainings, you can get a lot more done and learn a lot more, you know, asking, you know, questions about the things that you don't know at a training versus sitting there and reading some wiki or, you know, website with a how-to on your step one and you configure the zero port like this and whatnot.

**Chris Gammell:** So... Yeah. See, now, I was talking to someone about this the other day. Especially, I think a lot of this is actually more about, you know, where I came into the industry and history more than anything. Because I think that this stuff all exists, you know, it still does exist for a lot of people in the industry. But I was thinking back on my 10 years of being in hardware companies. And yes, some of that was during the recession and stuff like that. But I was never sent to training. I was never... You know, I did a lot of on-site stuff, but I was never really sent to anything like this, like the stuff you guys are talking about. And I'd be interested to know if people in the audience from the hardware world, like specifically just designing hardware, had that kind of thing. Like, you know, I think about maybe for CAD and stuff like that, people get sent to that. But it's just, it's really interesting to me from a, you know, almost like a company culture perspective that I was just, this was never a priority at the places I worked. So...

**Dave Jones:** Yeah, it wasn't always a priority in places I worked either. But I would... But it was at some places I worked, you know, prior to my current line of work. And I think that the IT industry in general, it tends to emphasize training, ongoing, continuing education.

**Chris Gammell:** That's great. Yeah. I mean, I think that that's actually a really positive thing in general.

**Dmitry Netospazov:** But Mike, how much of that do you think is related to what I said before with the certification requirements? Quite a bit of it is. Yeah.

**Dave Jones:** Yeah. Like in the security industry, probably the most popular certification is the CISSP. And that one is one of many that does have some specific requirement for continuing education. So in order to maintain your certification, you must do some kind of continuing education and provide evidence that you've done it, similar to what you have for doctors and lawyers and all kinds of other industries.

**Chris Gammell:** Yeah. Yeah. Yeah. And I mean, I guess the PE has that kind of requirement, but not a lot of EEs I know are taking that, are getting their PE, are going all the way through it. Right.

**Dave Jones:** Usually only in certain places where it's required.

**Chris Gammell:** For engineers, you have to. And then like for electrical engineers, usually it's people doing like, you know, anytime you're signing a drawing, right? That's usually the big piece. And I think that that's just happening less as well because there's more, you know, like so if you're working on like the wiring for a building, that's different than if you're designing a circuit board kind of thing. So I'm sure a lot of this is just my perspective on it, but it's more intriguing to me than anything else. Um, I also wonder about, I've also talked to people about, I think on the show before in the past, but just at like big hardware companies. So I, you know, I've, I work at a software company now and I work, I've worked at hardware companies and it's interesting to me as well, because when you think about all the costs of a company, right, you have people and you have offices and you have, you know, uh, computers and stuff like that for just getting work done, printers, all this stuff in normal offices and stuff like that. And then, but with, with a lot of hardware stuff, then you also have all of the baseline, um, overhead costs of the hardware itself that you're building. Right. And so in order to, I just feel like there's less margin in hardware in general. And, and I wonder if that ends up affecting training stuff as well.

**Dave Jones:** So I think that's probably true.

**Chris Gammell:** Yeah.

**Dmitry Netospazov:** So, I mean, I mean, they cut to, to, to, the, the certification stuff kills me to a certain extent though, because there are conferences and I think, uh, Mike, as somebody who's taught at a lot more different conferences that, than I have can, uh, maybe comment on that more. But there are literally cases where you just have maybe a certain percentage of your class say they're just there to get the certificate at the end and then they'll sit there and check their email the whole time.

**Dave Jones:** Oh, that's definitely true. Uh, but on the other hand, um, they, those people, uh, they, those people chose your class versus a whole bunch of other options. And so, um, in my experience, uh, at my classes, at least I thought Mike was going to say, they're

**Chris Gammell:** just really bored with your class, Dimitri. Sorry, man. That was not what I was going to do. Do better. Do better, man. I was going to say that even this turns into a rumble. I like it.

**Dave Jones:** Let's get there.

**Chris Gammell:** Take it up a notch.

**Dave Jones:** Even the, uh, even the people who are there just to get a piece of paper, uh, they tend to like see this class as some fun time for them. Um, and so, uh, I find that, uh, that folks, even if they're not super dedicated, they're still interested and are, are, I'd want to have fun with whatever they're doing, whatever we're doing in the classroom. As long as, as long as we can make it fun for them, uh, then I think it's a good fit.

**Dmitry Netospazov:** Yeah, that's definitely a big part of it too. So I've had a lot more success with my training ever since. I mean, so it used to be, I would say two and a half days of theory. And then it would turn out that the theory was so complex that we were behind schedule and then it would end up being like three days of theory and one day of playing around with stuff. And now I, I basically make sure that we don't do more than half of the first day of theory. And then after that we do like a FPGA bring up because for a lot of people, that's the first time they've done something with an FPGA. So, I mean, what I have them write on the first day is since I want them to learn serial protocols, everyone in my training ends up writing a UART transmitter and receiver on day one. And then I get them, uh, I get them have, uh, so basically you get an LED on the board to, to toggle when you send, uh, like a capital A or some arbitrary character just so that they can see that it's working. And so that ever since I switched to that, so basically I do that. And then since the software guys and I really want to show them what working with hardware is like the, the rest, every other, every day after that, when they actually get actual assignments, I just hand them a board and the reaction is always, what's the assignment? And then I say, figure it out. So I give them a board, a logic analyzer, the FPGA and a bunch of jumper wires. And I say, have at it. And they're like, what's the assignment? And I'm like, figure it out. And they're like, what's the assignment? And then, uh, and then I have to walk around and slowly, slowly allude to it. But my favorite is just when people, it's like, give them an embedded, uh, system and it just has some code, uh, on there. And for the most part, it's spitting out cereal of some sort on, on one of the, one of the pins. And I mean, there's so many aspects, there's so many ways to start solving, you know, going for a correct solution. So some people are smart enough, since I just use an Olimex board as my target board, are smart enough to download the data sheet, which is totally a valid approach. But a lot of people don't. And the funny thing is, is also the board that I use, it has some errors in the Olimex, uh, data sheet, which makes it super entertaining to have people figure out why certain things work, uh, which shouldn't work according to the data sheet. Uh, but yeah. And so either they download the data sheet or they start, but my, my absolute favorite is I tell them, I give them this, uh, I give them Salie's. So shout out to Salie who, uh, are nice enough to help you out. If you're a trainer, they'll, if you write them, they'll, they'll be nice enough to give you a discount code as well. Hint, hint.

**Chris Gammell:** Uh, but, uh, yeah, I'm sure Mark and Joe would love to give everyone a discount code, but yeah, anyway, sorry.

**Dmitry Netospazov:** But so with, uh, with, I, I give them the logic analyzer and it's more than enough to connect to all the pins on the board, but no, and, uh, some people eventually end up connecting to all the pins on the board and start the logic analyzer. And then they tell me nothing's happening and it's an embedded system. So it's done booting. So it's spit something out at the very beginning. And then by the time they connect the logic analyzer, everything's idling. So there's nothing going on, but it's totally, it's totally, it's such a mind blowing experience to people who come from the software world that they connected to this thing and nothing's happening. And then all of a sudden I press the reset button and there's stuff on their screen.

**Chris Gammell:** Nice. Yeah. It's a, it's like a base level assumption that we have. It's like, oh, you know, no stuff happens at the beginning, but of course. Right. Why? I mean, I think a lot of people coming in would be like more interested in steady state in certain situations. Right.

**Dmitry Netospazov:** Right. But I mean, it's totally like a lot of those, a lot of those, uh, uh, kind of traps that I set for people are, uh, specifically for people who are coming from the software side because they're not used to thinking that way that something might boot, you know, you need to hit reset and all this kind of stuff. So that's a, that's a really good way to stick it in their face.

**Chris Gammell:** That's good. Yeah. I like that. Yeah. Booty is what happened when I have to wait, uh, when my system restarts, right? That's all that happens then. So cool. Well, uh, it sounds like you guys are, are doing good stuff on the training side of things. Uh, what about, uh, new hardware? I mean, so, so Mike, it seems like you're always building new hardware. Dimitri, I, I hear about some of this. So you've been talking about the, uh, the soldering stuff you've been doing, the micro soldering. So what's, what's new in the hardware side of the world for you guys?

**Dave Jones:** Well, I'm designing a whole bunch of boards lately. Uh, great fit is a big project that we've gotten in production right now and, uh, designing a bunch of add on boards for it. And that's like a general purpose hardware hacking platform. Uh, and then, uh, hack RF project has really been, uh, active lately. I've, I've made a couple of add on boards for hacker F one and I'm in the process of designing, uh, marzipan, which is the code name for the next generation hacker F. And it's a, um, it's basically the same radio as hacker F one with a Linux capable arm, uh, CPU. So it's a single, single board Linux SDR embedded platform.

**Chris Gammell:** Nice. Wait, so isn't a lot of the stuff that you do for hacker F though, is that just pass through? I thought you did some like low level processing on the hacker F.

**Dave Jones:** Um, on hacker F one, we primarily designed for, uh, just passing samples back and forth. Uh, so it's a, it's a USB peripheral. You plug it into your laptop and then you do all the DSP on your laptop. Now it can, you can do some DSP on hacker F one, but it's fairly limited, uh, in a CPU power.

**Chris Gammell:** Yeah.

**Dave Jones:** So you had the, uh, CPLD down there. Is that right? There's a CPLD, but it really isn't very, it isn't large enough for any DSP really. Um, but you know, we have had some success doing DSP on hacker F one, uh, standalone in particular with Jared Boone's port-a-pack. Uh, he's done some amazing things, uh, but we kind of want to. Do better. We want to have a platform that's a single board SDR that, uh, that you can, uh, really do a whole lot with the onboard CPU and use it as a standalone platform or an embedded platform, uh, or a remote node that you connect to over ethernet, um, instead of using it as a peripheral.

**Chris Gammell:** Cool. So it would spit back, uh, shaped, shaped packets instead of just raw packets. Kind of, is that the idea?

**Dave Jones:** Yeah, kind of. Right. So you, you, you, you would get, um, you might have it, uh, like the modem function of actually converting between the physical layer waveform and the, the higher layer, uh, packet data. Uh, that modem function is something that currently in most cases you would implement, uh, on a host computer that's connect that has the hacker F one USB connected. But with Marzipan, uh, I would envision in most use cases that modem function would, would be operating on the hacker F itself. Hmm.

**Chris Gammell:** That's really cool. Uh, any hints on, on which processor?

**Dave Jones:** Yeah. Uh, it is going to be the IMX seven dual.

**Chris Gammell:** Oh, I have, I've heard about the IMX six. I don't know anything about the IMX seven other than, other than NXP might be getting bought. That's my only.

**Dmitry Netospazov:** Well, yeah, there is that.

**Chris Gammell:** Uh, does that throw a wrench in your works or no?

**Dave Jones:** I don't think so. I don't, yeah. Um, but, uh, but the IMX series comes from Freescale, of course, which was bought by NXP not too long ago. And now NXP may be, uh, uh, getting purchased by Qualcomm. We'll see. But, uh, um, the IMX seven is an arm cortex a seven, which is, uh, kind of a newer, um, a lot of people know the, the A8 and A9, um, and A7 sounds like a step in the wrong direction, but, uh, it really is kind of a slightly more advanced than the A9 and in some ways and less and simplified in other ways. Uh, so it ends up being, uh, kind of, I think the best, the best thing about the A7 is that it is highly power efficient. So you get really good bang for buck, uh, in terms of like CPU, uh, power versus, uh, electrical power consumed.

**Chris Gammell:** So you have to, you can like run it off USB versus having a separate plug pack on a thing. Is that the idea?

**Dave Jones:** Yeah. Yeah. And, um, we probably, um, I haven't figured out what kind of power supply we would include with marzipan when it someday goes into production, but, um, it could potentially be, um, operated off of maybe USB 3.0 power, that kind of, uh, amount of power draw. Uh, it could be operated off of a barrel jack or it could be in a wall wart or it could be, and this is one case that I really want to make sure that we enable, uh, is that it could be powered off of power over ethernet.

**Chris Gammell:** Oh, interesting. You don't hear much about that anymore. You know, like I, I ran into a power over ethernet, like a power insertion thing the other day and I was like, Oh, I forgot, kind of forgot about this. I know it's used a lot of places, but it's a pretty cool solution. Yeah.

**Dave Jones:** Uh, and especially for this particular device, I think it'll be super handy to be able to, you know, throw the, throw the, the, uh, the board, uh, in your attic or in some funny place where you want to connect it to an antenna and, uh, Someone else's attic. Someone else's attic. Yeah. Yeah. That sounds like, that's what I'm really thinking.

**Chris Gammell:** As long as you can run ethernet to it. Yeah. So what about battery too? Are you going to try and do battery power?

**Dave Jones:** No, I don't think so. No. Okay.

**Dmitry Netospazov:** What's the point if you have POE?

**Chris Gammell:** Well, I did for when you don't, that's what I meant. You know?

**Dmitry Netospazov:** I mean, you can get batteries with a POE output.

**Dave Jones:** Oh, right. Oh, okay. Interesting. So we can have a, that's one way that it could integrate with a third party battery.

**Chris Gammell:** Mm-hmm. Okay. That's cool. It's what, and what, so power over ethernet, what is, what are the specs on that? Like what can it, what can it do power wise?

**Dave Jones:** Uh, I forget what the maximum power over, power over ethernet is, but it's, it's something like in the order of 10 watts. Uh-huh. Um, and, um, you know, we should, we should be drawing less than half that. Yeah. Hopefully. So I think, I remember looking at one point when I had.

**Chris Gammell:** For the, for the math averse out there, that's a two amps, two amps supply on a five volt, uh, or it's two amps out on a five volt supply. So. Yeah. Yeah. That's, that's a lot of, that's a lot of juice actually. Yeah.

**Dave Jones:** Yeah. It really is. So, um, uh, my, my kind of target, uh, maximum power consumption that I'm going for is basically, uh, USB 3.0 power. Yeah. Um, uh, we're not going to have USB 3.0 data on the thing, but that, that kind of is a, a reasonable power target, I think. Well, uh, that's, that's great.

**Chris Gammell:** Uh, Dimitri, are you building new stuff?

**Dmitry Netospazov:** Um, I mean, I just applied for something pretty cool in Germany called the prototype fund, which is, uh, from the German ministry of education there. Mm-hmm. And, uh, basically it's something where they'll give you up to 30,000, uh, euros to do a project where you have to set your own milestone. So in a way, kind of like, uh, some of the DARPA projects and it was a really easy to apply for as opposed to proper either German government or EU, uh, funding, which are a total pain in the butt with tons and tons of documentation. Yeah. Yeah. Yeah. And, I mean, like upwards of 40 pages, uh, just for the application. Uh, so it was totally easy to apply for. So if I get it, I'll definitely be doing some new hardware because, uh, I'll basically have more than enough reason to allot some time to do some, uh, open source work. And plus that's a, that's, that's a requirement. So I submitted something with, I'll be building either, uh, I mean, so one thing that I, that I have on the table that I've been wanting to do for a while is, uh, a better than what currently exists, uh, car adapter. So to analyze, uh, car protocols and for people who want to do automotive hacking. And then another thing that I wanted to do was, uh, just basically do something that's a little bit better than, uh, the bus pirate and can do maybe quad SPI or something like that.

**Chris Gammell:** Oh, cool. And that's, uh, so when you say car stuff, do you mean like OBD2 or do you mean like, uh, um, like direct on, cause OBD2 isn't, isn't like a canvas direct. It's not direct on the canvas, right? That's it. Oh, it is. Why do you think it was locked out of the canvas?

**Dmitry Netospazov:** It is. It also is. So basically what they, what a lot of times you have to do is you have to authenticate yourself and then the car will start. And then afterwards, uh, so basically you have to send like, uh, some sort of passphrase, uh, or some sort of command to say, open her up. And then you can just, then you're on the, uh, can fire hose quote unquote from the car.

**Chris Gammell:** Oh, cool. Okay.

**Dmitry Netospazov:** So, but basically that's proprietary, but what I wanted to build and I will be happy to give this, I mean, I'm planning to do an open source project. So if somebody beats me to it, I'll applaud them. Uh, what I wanted to build was something where you have, uh, an ODB male connector on one side and an ODB female connector on the other side, because the most interesting thing is to connect, uh, whatever the dealership has for debugging and setting parameters on your car. So I don't understand why that doesn't exist.

**Chris Gammell:** I mean, not man in the middle for security people, huh?

**Dmitry Netospazov:** Right. Exactly. So that's, that's, uh, I've yet to see, uh, an adapter that does that really well. And so I also, since there's a, a lot of, there are a lot of adapters that can, but I wanted to do some of the other, uh, crazy ones. So this would yet again be me doing something, uh, on with an FPGA to do some real time processing and basically to encode, you know, USB or whatever I'm speaking on one side to whatever the, the protocol is on the other side. That's great. And same thing with, I mean, so both of my submissions, I would say the architecture will look, uh, similar where I'm probably just going to take either, uh, USB to FTDI or a Cypress or something and just do, uh, uh, basically USB two or USB three, then have an FPGA and then have it spit out something else on the other side. Because I, and I also want to, especially for like, as a bus pirate replacement, I don't even think that like considering if there, if I had some time, I mean, I, I would, if I was to improve on now, don't get me wrong. I use the bus pirate myself just because it's such a reliable tool on occasion, you know? Uh, but if I wanted to, uh, basically set certain parameters or, uh, decode or interface to some device, uh, I could do a lot of it, a lot of the heavy lifting in Python and then literally just, you know, decode the bits from one protocol to another using FIFOs on a, on an FPGA. And me personally, I think there's merit to doing things that way, especially since you could basically implement whatever protocols you want in that fashion. And then there will be a nice reference for people because I don't know how many people, uh, who listened to the show have looked at open cores, but everything I've ever looked at on open cores.

**Chris Gammell:** Or no, no, sorry. That's a, that's something different, right? That's the, that's the open source arm. Yeah. I mean, I don't want to knock on it. This is the one where it's like, you can download someone's HDL and try and implement it, but you're going to say that it's unreliable pretty much on there, right?

**Dmitry Netospazov:** Right. I mean, I've, there's some things that I think it's good for, which is if you don't know how to implement a cryptographic protocol. So for example, back in the day, I wanted to build an AES, uh, and I wanted to just very quickly look at someone's implementation of how to do it purely in logic. And so I went there and, uh, I saw a, uh, I mean, so basically I just wanted to see how they implemented the S box, which was one of the components of, uh, of, um, of the, the actual algorithm. And so they had exactly what I wanted. And so I took the piece from the project that I needed and I implemented the rest. Uh, but I wouldn't recommend just downloading someone's, a lot of times, uh, it's some, you know, college student at some point, 10 years ago, uploaded this HDL onto that website, zipped it up, uploaded it, and no one has ever tested it.

**Chris Gammell:** Yep. And I've definitely gotten burned by that. Yeah. Yeah.

**Dmitry Netospazov:** And it's, I mean, the, the thing that, the thing that bugs me is, or I mean, especially compared to tools that you can download off of GitHub, I mean, I'm kind of thinking it maybe from the point of view of people who take my training as well is they're used to there being these great open source projects, especially for doing stuff like, I mean, any sort of security analysis or scanning the internet or what have you. And so they just have, uh, an expectation that they go onto this website. There's nice open source code with a proper open source license and that they're going to download it and it's going to work out of the box. And the reality is 10 people have downloaded this and none of them have gotten it to work. And the author forgot to add a couple of files or something like that.

**Chris Gammell:** And then, so instead of like giving feedback, it's like, ah, screw this. I'll do it myself or whatever. Moving on.

**Dmitry Netospazov:** It's not, it's not screw that. I mean, for most people, it's just, uh, they, I think a lot of times they give up and then I don't, I don't know.

**Chris Gammell:** That's encapsulated in the screw this. Yeah. Maybe it's just a language difference. I don't know.

**Dmitry Netospazov:** Yeah, no, but it's, it's, uh, it's tough times. So I kind of want, like my dream would be that for, if there was a project like this and there would also be nice open source reference implementations for a bunch of protocols that we see and use on a daily basis. And that's also something that's missing. And so you wouldn't go to open course to download your simple usable I2C core. You would go to a project that's actually using it and that a lot of people are using.

**Chris Gammell:** You wouldn't download a car diagnostic tool, right?

**Dmitry Netospazov:** I mean, yeah, I haven't checked the cans on there, but yeah.

**Chris Gammell:** I mean, I think, I think you missed it there. Yeah, it's, it's fine. Mike, you got it? Did anyone get this? Yeah. Is anyone laughing out there? All right, good. That's all I wanted. It was like one, like, I just wanted like one, like, like nose breath, you know, like, you know, okay. Anyways.

**Dmitry Netospazov:** But it's also, it's also crazy what, uh, what Xilinx will charge you for their, uh, Xilinx or Altera will charge you for their CAN implementation.

**Chris Gammell:** Right. Uh, well, they're not charging you for the code. They're charging you for the fact that they checked it.

**Dmitry Netospazov:** Uh, yeah, that's, I mean, that's true as well, but that's where, that's where I believe in the open source community coming together in an effort to, uh, do something for the greater good or whatever you want to call it.

**Chris Gammell:** Ah, well, there's a philosophical discussion. Um, uh, well, Mike, how do you feel about that? I'm obviously you're, you're, you guys are both in the open source community. Do you, do you, do you feel that, uh, in terms of the, the community? Uh, in terms of that they'll come together and then it's, uh, you know, like I, I, I, I, I guess my thing is that I, I'm not sure I believe that Dimitri's point, but maybe I haven't seen the right things of it.

**Dave Jones:** Well, I, I think that, uh, the open source community has had tremendous success in the past. And, uh, and the open hardware community is, is still, uh, still growing. It's nowhere, nowhere, nowhere near as large as open software. Open HDL is kind of a, kind of a strange little niche where, um, there, there's, it's kind of a hybrid between hardware and software. And yet somehow it never seems to be, uh, kind of, uh, I don't know the, the, the open HDL community is nowhere near as much of a community as either the hardware or the software community is in, in my experience.

**Chris Gammell:** When you say open HDL, is this like a site as well?

**Dave Jones:** No, no, I mean, just like open cores and HDL that's on GitHub and everything else. Um, it's just, um, there aren't that many people doing open source HDL in general and there aren't, uh, there isn't as much collaboration, uh, that I see, you know, usually, um, usually a project that is hardware description, uh, kind of goes the way hardware projects go. Uh, like, like Dimitri mentioned, you, you, you see somebody who like did a project for a university or something and, and they, they post it, but it's, it's not so much an open source project as it is just a dump of a retired project. And, um, it's, they tend to be not well maintained or not at all maintained. They tend to, uh, not have a lot of collaboration. And so it's a rarity in the, in the open source community to see, um, to see something that uses HDL, uh, that really has, uh, kind of a, an active project with more than one contributor. Hmm. Yeah.

**Dmitry Netospazov:** Is it, uh, and then, uh, other, the other side of things is you download Xilinx's core and they'll have the latest in, uh, proprietary encryption technology to not let you look at how it's actually implemented.

**Dave Jones:** Yeah. And that's one of the biggest reasons I think that, uh, or it's one of the hurdles that people who want to do open source, uh, have to deal with if they're dealing with FPGAs. Uh, and that's changing a little bit, at least with, uh, like project ice storm, but, uh, which is pretty exciting, but that is a project that targets only one family of FPGAs that is kind of on the small end of the spectrum. So, uh, for certain projects, it's great. Uh, and I'm probably going to use it on Marzipan actually. But if you have a project where you need a, a larger FPGA and a lot of people do, uh, then that's not going to help you, uh, unless you further, uh, project ice storm or something similar to, uh, to target larger FPGAs. Um, but that's, you know, that's a rather significant hurdle. Uh, it's great that we have project ice storm, uh, but the, the task of reverse engineering a new, uh, FPGA, especially a larger one to be able to integrate with an open source tool chain, uh, is no small task. Right. Right. Yeah.

**Dmitry Netospazov:** And I mean, you can see, you can see people do talks about that, uh, especially at, uh, recon, uh, which that's right. You have people every year talking about reverse engineering, uh, some, some aspects, some bit stream, some compiler or something like that. And then, yeah, it's, I mean, the, the thing that's always the most depressing to me is that when a new family comes out that they don't have support for it anymore. So they have to go back, go back to start. Yep. But I also want to say that for me, I mean, especially, uh, as somebody who wants to get people more and more just playing around with FPGAs, I think one of the worst things that you can do, especially since there are boards like what I use in my training is a digital and arty, uh, and there are boards that cost maybe, uh, between, I mean, under $150. So I would say 120, something like that. So, uh, these, if there are boards available with this gigantic FPGA that costs so little, then I don't see the point in, uh, going with a lower end FPGA only to find out that at some point because of your coding style, because you're new to this, uh, you run out of space on your FPGA.

**Chris Gammell:** So you're saying that it's, it, it's like that crossroads of not even worth it to try this open source protocol because, because of the limitations of learning. Is that the idea?

**Dmitry Netospazov:** I mean, I just think that as people, so for example, like a good example is let's say you're building some sort of protocol analyzer and then you want to multiplexer design a protocol analyzer on, uh, every, uh, single pin you have there. And so the trivial way to build it would be you write, uh, a UART, you write an SPI, you write an I squared C, and then you connect one to your connect one of those modules with each, each with its own internal counter, uh, to kind of down sample and output stuff at the correct baud rate. You would implement one of those for each of the pins that you're using, but that means you're wasting a lot of space from the point of view of the FPGA. But from the point of view of somebody who's learning how to build stuff with, uh, HTL, I really don't think that space should ever be a limitation kind of.

**Chris Gammell:** Right, right, right. Yeah. Yeah. So you're saying that like, it's a, so to put it like in a microcontroller terms, it's like the difference between someone walking up to someone and saying here, start with an Arduino or here, optimize your assembly to get into this, you know, AK of memory or whatever. Yeah, exactly.

**Dmitry Netospazov:** I mean, that's, that's actually a really good example. Yeah. Yeah.

**Chris Gammell:** Okay. Yeah. Well, I agree. I mean, like, I think that, I think that especially like because you guys are trainers and I kind of am a trainer, I think that like the important piece in, in any kind of learning is actually just, um, that first dopamine hit, you know, like you just need, like if you're frustrated, I remember I've been a lot of trainings, uh, like for software and, uh, in, in the fab world actually. And there's nothing worse than like you're saying like, oh, well now you have to do the serial, like in windows, you have to do the serial driver setup, right? Like there is nothing more soul crushing than serial driver setup when it doesn't work, uh, over and over and over again. So yeah, it's, it's just so important to get that first. Hit a dopamine, no matter what the resources it takes to get that right. If you have to, you know, use a huge part or whatever.

**Dmitry Netospazov:** No, and I mean, having, having said that, especially with FPGAs, I mean, even as long as I've been doing FPGAs, so I'm a, I'm a, I'm a youngster also, as Dave would say it. Uh, so I've only been doing it for, I don't know, the past, uh, so at university maybe for the past 10 years or whatever. But to imagine that 10 years ago, it would be as easy to write something, you know, in Python, in a language like Python that reaches down and is interfacing to the hardware and toggling the bits and outputting something on the wire. That would have been, you know, uh, uh, a dream many years ago. And now through things like, uh, lib FTDI and, uh, lib USB, which is, I mean, lift it FTDI and lib USB are, I don't remember exactly. There's also a fork, I think where they try to re-implement it. Uh, but, uh, so it should be, I think lib FTDI is still based on lib USB, but in any case it abstracts it all away from you and just, you know, you get, give me, give me the raw bits, just give me the bits. Huh. And so you don't have to worry about the coding or the, I mean, the most important thing is you don't have to worry about the drivers that abstracts away the drivers completely. So that's, that's one of my favorite things. And I mean, in, in, in a way, uh, projects like, uh, the bus pirate, they were built at an age where the only thing that you had was best case you'd have a serial interface. So the reason that they're interfacing over serial to, and outputting all these other protocols to me, to a certain extent is the driver situation. But I, from my experience, that's improved significantly where now it's easy enough to write something in Python. Admittedly, you have to install a couple of eggs and I don't test Python three, uh, and stuff like that. But for the most part, you just install a couple of eggs and, uh, you get it up and running on Mac and you paste the exact same commands and you get it up and running on, uh, Linux. And, uh, if you install Sigwind and it's straightforward on windows as well.

**Dave Jones:** Yeah. And that's very much what we're doing with the great vet project, which is, uh, on a successor to the good vet, uh, which in some ways is like a bus pirate. Uh, but, uh, one of the reasons that we wanted to, uh, kind of, uh, revive the good vet project and make something better out of it, it was, was the Python interface. It's so, it's so powerful just to be able to twiddle bits of hardware, uh, arbitrary hardware, whatever you want to connect it to, um, from a Python interface on your laptop. And, uh, yeah, so just echoing exactly what Dimitri is saying that that's such a powerful tool and enabler for people to get started, um, with all sorts of different hardware projects. Uh, that that's, that's been the focus of the great vet project from day one. That's awesome.

**Chris Gammell:** Yeah. I can't imagine anyone being like, I wish it was harder to get to low level access on my, on my hardware. You know, I, uh, I mean, personally, like I, uh, you know, for twiddling bits, at least I, when I was testing a bunch of ADC stuff, like I would just switch to Arduino just because it was super easy for me to, um, you know, just write simple, simple command interfaces, kind of like what people do also with bus pirate too. But it was just, you know, I was just going over a spy, a spy port and, uh, I could have gone all the way back and done it on a micro that I, you know, put down on a board or something. But at a certain point, you're just trying to get a thing done. And I think that that shift from like, uh, I want to do this, the quote unquote, right, right way versus I just need to get this thing done. And it seems like, uh, that, that difference is, is important and it actually benefits everyone at the end of the day.

**Dave Jones:** So definitely. And I don't think that making tools for rapid prototyping, uh, necessarily encourages people to, to not do things the right way. Um, but, uh, it, it, it enables all people to do things in all ways.

**Chris Gammell:** Right. Right. Exactly. And it's almost like an evolutionary model of like, well, whatever, whatever works best is probably going to make it right. And, uh, wherever people would decide to put their time, either, you know, making new, new tools like you guys are talking about, or, you know, contributing to projects, stuff like that.

**Dmitry Netospazov:** Yeah. But I mean, with any of those tools, something like an Arduino is a perfect example where at that point you're limited to, on the one side, you're limited to serial. And on the other side, you're limited to whatever, uh, protocols, uh, it speaks. And then it'll do, I mean, you can't get it to get a bus to hang, uh, or something like that or to, for example, uh, one of, one of the things that I was doing recently is if you have a I squared C interface, what you can do is you can basically, uh, reply, uh, so you can, since it's pull down, uh, or rather since there's a pullup resistor there and everything is, you know, just basically outputting a zero when it's communicating, then you can corrupt the address and then pretend you're whatever peripheral, uh, you actually want to, uh, be and the peripheral will not reply anymore on the bus. So stuff like that is where you run into issues and you can't use, uh, you know, standard tools. And that's where, that's where people come to me to take my training and that's the kind of stuff that I build on that PGA.

**Chris Gammell:** Nice. That's great. That's great. Uh, so you guys keep mentioning open source, uh, Mike, you are going to be at open hardware summit. Is that right? Yeah, you bet. All right. I'm looking forward to seeing you there.

**Dave Jones:** Uh, are you bringing any toys with you that I will, uh, get to see? That is a good question. I probably should think about that. Um, I'll, I'll bring some great fat stuff.

**Chris Gammell:** Okay.

**Dave Jones:** Um, I don't have any of my latest hack RF projects in a state that I could actually bring them. Uh, although at least one of the boards is like on its way here from Osh park right now. You should just tell them to keep it there. I mean, you've got to board. I should. Yeah. But, uh, yeah, it may be too late for that. I think it shipped like yesterday. So, uh, I'm, I'm probably just going to miss it. But, uh, um, anyway, it definitely won't be something that's assembled. And functional, even if I do get it in time to show people. Gotcha. Uh, yeah.

**Chris Gammell:** Real quick, can you explain what I, so I, I keep hearing about good fat. I don't quite understand it. I'm sorry to say. Yeah. What is, what is the point of good fat? What is, what are people going to use it for? Sure.

**Dave Jones:** All right. So good fat is a project that was started several years ago by Travis Goodspeed. Um, and it was his take on the MSP four 30 fat as basically a variant of that debugger. Uh, so he, um, he made this thing called good fat, which was an open source hardware, uh, debugger. And, um, it very quickly kind of gained a lot of additional functionality and in part, because it was inspired by the bus pirate. Uh, but it was a pretty simple, uh, board that just gave you a USB to, uh, USB to serial interface or USB to arbitrary debug protocol, uh, interface. And it would, um, and it had a Python, uh, library so that you could, you could interact with it very easily on your host computer and Python, um, either in an interactive Python shell or through some small Python programs. Uh, and, um, and it was, it's super, uh, it's super popular in the information security community, uh, for debugging for, uh, flashing. Like, let's say you just, you just want to dump the flash off an EEPROM or something like that. Um, or, um, like I, the first time I used a good fat was to program the I am me, which is a pink toy that, uh,

**Chris Gammell:** Oh, that's a 900 megahertz, like a communication device that was meant for.

**Dave Jones:** Exactly.

**Chris Gammell:** Right.

**Dave Jones:** So like my first, that was really my first embedded, uh, development project was writing the spectrum analyzer for, for that. And, uh, and I was introduced to the I am me by Travis and he handed me a good fat. PCB and I took it home and soldered it. And that was my first, um, that was my first surface mount soldering that I ever did. And my first real embedded project, uh, it was all kind of started or, uh, uh, inspired by, by Travis. And, um, years go by and the, the good fat project has, uh, forked in a whole lot of different ways, um, especially in hardware. Uh, so there are a bunch of different variants of the good fat where they kind of, uh, in most cases, they add something to it. So they'll add a can adapter to it, or they'll add a wireless interface to it, or they'll add, um, on a secondary USB port. And that's actually the kind of the most popular variant of the good fat is called the face dancer. And it adds a USB device. Um, so basically it's a, it has a, a USB device on either end of this board. So you plug one end into your host computer and that's where you control it from. And the other end, you plug in, uh, to another USB host and it allows you to do things like, um, explore, uh, the security of the, or to probe the security of the USB stack on the host that you're connecting it to. Um, and that particular functionality is, has, has, um, yielded, uh, a lot of bugs in USB stacks. So really? Yeah. So the, the, the face dancer is one of several different hardware variants of good fat. And there are at least three different, uh, incompatible code bases for the face dancer. And there are, there's even, there's even more fragmentation in the software side than there has been on the hardware side. So it, it, it ended up that this project got really fragmented and, um, and also it has some, some problems in terms of commercialization, uh, because, like, it's very popular project for people who build their own hardware, but it is somewhat, uh, less successful as a commercial project. I think because, uh, it's sort of needlessly expensive. You don't, you know, the hardware is very simple, but it isn't really optimized for cost at all. It's, uh, it's optimized for what's easy to build, uh, with sample parts that you can get from TI. And, um, so it's, it's, uh, it has, it has shown its age, this good fat project, but it's still very, very popular in the security community. And so the great vet project is the great scout gadgets take on good fat. It's kind of the next generation. And, um, well, I was looking initially for, for some years, actually, I was looking at how can, how can we optimize good fat for costs so that it could be more useful for people who want to just buy one. In addition to being useful, uh, for people who want to build their own. And for, after some years of looking at it and thinking about optimizing costs, I, I finally decided that it made more sense to change direction and optimize for greatness.

**Chris Gammell:** And, uh, so you're saying, are you saying that you made the good fat great again? Is that what I'm hearing?

**Dave Jones:** That is exactly it. Yes. We are making good fat great again. Just like the hat says. Yeah. Yeah. Yeah. So we, I, I gave a talk at black hat in August and, uh, you know, made a whole bunch of hats and handed them out to people.

**Dmitry Netospazov:** Mike is so good with names.

**Dave Jones:** Thank you, Dimitri. So, uh, yeah, anyway, it's a, it's a, it's a board that is kind of similar to a good fit, but bigger has a much more capable microcontroller. It's actually the one that we use in hacker F1, um, and a whole lot of expansion pins. It has a hundred pin interface. So it's a LPC. Yeah. It's a LPC 4,300. Uh, and it has a secondary USB port built into the microcontroller. So we put that on there. So it's basically like a face dancer plus, um, and we call it great fight one. And we're, we're in production right now, but we haven't started shipping yet. And, um, we're in the process of making a bunch of add-on boards for it.

**Chris Gammell:** So is it mostly like the software layer is the main, I mean, I know you said there's a lot of fragmentation there, but is that, is that kind of the main thing that goes on? Is that people are expecting just that library level? And then you're kind of making all these add-ons to that?

**Dave Jones:** Um, the, the software is, is definitely, uh, super important to this project. Um, and, and it's kind of complicated because we have, we have firmware for the LPC 4,300, but we also have, um, software for the host computer. Um, because what you can program this as an embedded platform, that's not really our, our primary use case. Our primary use case is that you use it as a peripheral and, you know, it's a, it's a general purpose, general purpose, high speed USB peripheral that you can do whatever you want with. And easily control it from a Python interface on the host computer. So, so getting that Python interface working well and getting a protocol over the USB that we like and getting firmware, uh, all working together to make this as general purpose as possible, uh, has been a challenge. Uh, but it's something that we're, we're, we're, um, we have some basic functionality kind of working the way, the way we want. And we're able to do things like dumps by flash and stuff like that, uh, already. Awesome. Well, that's really great.

**Dmitry Netospazov:** I mean, uh, can I, can I throw in, uh, two pro tips?

**Dave Jones:** Yeah, you bet.

**Dmitry Netospazov:** So number, number one is, uh, ordering samples from Texas instruments. Number two is, which is, you got to qualify to quantify that a little bit.

**Chris Gammell:** What's that's, that's just a pro tip in general.

**Dmitry Netospazov:** Like, I mean, that's the greatest, uh, that's what gets a lot of PhD students through, through their studies is ordering free parts from Texas instruments.

**Dave Jones:** Oh, definitely. I mean, there are some other vendors who are good at that too. Yeah.

**Dmitry Netospazov:** I know, I know people at my university who didn't have as big a budget as, uh, we did for ordering parts. Cause I very quickly learned, uh, what writing grants is like. And my favorite category was stuff. I mean, I'm trying to think of what it's like raw components or something like that. And that one, that's the category where you don't have to explain what you ordered because if they try to come and find it and kind of do an inventory of, uh, what's left, it won't be there. So that's the best. You try to fit as much of the budget as you can in that category because it means those, those things disappear. And so I would just order stuff from Farnell and DigiKey, but a couple of colleagues of mine who didn't have a budget, they would sit there on TI and optimize everything. Use TI DC to DC, use TI LDOs, use TI ADCs.

**Chris Gammell:** You guys are playing right into their hands, man. No, I mean, that's what they're hoping for. That's how you build brand loyalty is a couple of free parts to, this is just like, uh, buying a bunch of kids, a bunch of grad students pizza, you know? And connectors from Samtech. Samtech, that's right. Exactly. There are other options, people.

**Dmitry Netospazov:** There are other options. Is that a second pro tip is connectors from Samtech?

**Dave Jones:** Oh, yeah. Well, they, they are similarly good about, uh, giving free samples out. Yeah.

**Dmitry Netospazov:** Yeah, but I was, I just, I always find it crazy that you order, uh, from Texas. I mean, they, they ship faster than, uh, Farnell and DigiKey half the time. I mean, it was overnight. They would ship from some distributor, I assume somewhere in Germany.

**Chris Gammell:** No, no, no, no, no. Uh, no, TI actually, if you don't notice the, when you order TI samples, they come from Thief River Falls. Guess where that is? So they just come from DigiKey. That's right. Yeah, that's just marketing cost, I think. I mean, that's, but it's brilliant. I mean, like, don't get me wrong. That's, look how much we just talked about them on the amp hour. Yeah.

**Dmitry Netospazov:** I mean, I don't know. You corporate chills. I don't know how effective that is because every time I build something myself, I sit there on DigiKey and then buy whatever's cheapest or is available in ample quantities and whatever. And I totally use different parameters for my decision making, so I'm not totally loyal to TI. But TI definitely is, I do like the free sample stuff that is very useful. But another pro tip, which I actually have from Travis from developing the FaceDancer was you can actually use VMware to generate PCAPs for USB, which is very, which is probably, I mean, in total, that's the cheapest way to do any sort of decent USB debugging with any solution out there. Right.

**Dave Jones:** I think the kind of solution you're talking about is, like, having a Linux host and then you, if you need to, like, sniff USB on Windows, you can run that Windows inside VMware on a Linux host and then you can use the Linux kernel's USB monitoring solution. Is that the kind of solution you're talking about, Dimitri?

**Dmitry Netospazov:** Yeah, but I mean, you can even just have at least, I mean, it works on Mac as well. You can just have it spit out a PCAP for you over everything that's going over USB.

**Chris Gammell:** Right. Sorry. What's a PCAP? Sorry. I don't know.

**Dmitry Netospazov:** So it's a packet capture.

**Chris Gammell:** Packet capture file format.

**Dave Jones:** Thank you. Yeah. So it's super handy for reverse engineering USB protocols and also for troubleshooting or debugging your own USB protocols.

**Dmitry Netospazov:** Exactly. That's what I was getting at. So, I mean, if people are complaining that, you know, a Beagle is out of their price range, then where they should start is buying this proprietary, you know, a proprietary license to VMware, and it'll totally be worth it because it's...

**Dave Jones:** I have a better option. Go for it, Seth. Potentially. I mean, the VMware... Pro tip three. The VMware solution is really good in a lot of use cases. But another option is to use USB proxy, which is some software that Dominic Spill wrote for the BeagleBone Black. So you buy a BeagleBone Black, which has two USB ports on it, and you do man-in-the-middle USB with the BeagleBone and the software USB proxy. And then you can do your capture, your USB capture, right there on the BeagleBone. So it's just like a dumpster raw file kind of thing or what? Yeah, exactly. Okay. And, well, it has some flexibility in what you do with that data and how you could actually manipulate it in real time in addition to just logging. Like filtering of packets or what? Yeah, you could do some kind of filtering. Dominic actually did a kind of a USB firewall thing as a sort of proof of concept. But... That's cool. It's super low cost and it's all open source because, you know, USB proxy is open source and the BeagleBone Black is open source hardware. And it's a lot lower cost than, you know, a commercial USB analyzer, for example. Yeah. And it's also something that we hope to get working sort of similar solution working actually on GreatFit because we do have two USB ports on that as well. But it's a little bit of a different architecture because we're not running Linux on the GreatFit. So the software would be completely different for it. But theoretically, we could do some...

**Dmitry Netospazov:** So you get to do everything in real time.

**Dave Jones:** Yeah.

**Chris Gammell:** We get to. Yeah. That's a good outlook on life. I like that. Yeah. Right.

**Dmitry Netospazov:** Real time OSs are so fun.

**Chris Gammell:** Yeah. I'm kind of amazed. Like, I mean, like, how much do you guys have to deal with the USB stack on all this stuff? I mean, like, so this is talking about kind of once it gets to the physical kind of grabbing packets off and stuff like that. Do you guys have to deal with the actual USB stack and dive into that at all?

**Dmitry Netospazov:** I mean, I think Mike should comment about... I remember listening to Mike's talk at TorCon, I believe, and Mike was talking about the DAI show. And I remember how much USB debugging you guys had to do there since you implemented your own USB 3 core. That was pretty nuts.

**Dave Jones:** Yeah. Yeah. And that's sort of the next step beyond USB proxy on a BeagleBone is our DAI show project, for which we actually implemented USB 3.0 man in the middle running through an FPGA. And we developed an open source USB 3.0 super speed device core. Really? Yeah. So that's out there, by the way, in the DAI show project.

**Dmitry Netospazov:** And it's good Verilog code. I can vouch for it.

**Chris Gammell:** Yeah. So wait, you basically read the spec on USB 3.0 and then you implemented your own core? Yeah. But then explain the stuff, too.

**Dmitry Netospazov:** Mike has a very talented FPGA guy. Yeah, I know.

**Dave Jones:** Sadly, he doesn't work for me, but he's contracted for me in the past.

**Dmitry Netospazov:** Yeah.

**Chris Gammell:** What is the... Is there a secondary... So there's an FPGA device, but then is there a software stack on top of it that's talking to that device? Is that the idea for the core?

**Dave Jones:** So there's a... You need some kind of a physical layer transceiver. Yeah. And we were using this low-cost PHY chip from Texas Instruments, actually. Free samples. Yeah, you can get free samples, probably. Oh, who knew? Who knew? It's... So, like, if you shop for super speed USB chips, there isn't a whole lot out there that's, like, readily available in low quantities. One of the parts you'll find is the Cypress chip that has an ARM core on it and costs, like, $20 plus. And that is a reasonable option for a lot of projects, but we were trying to find something lower-cost and more flexible. And so we found this transceiver chip, which is just a very simple... Basically, it's a Certes solution that's specifically designed for USB 3.0.

**Chris Gammell:** And Certes is serial deserializer, if people don't know. That used to confuse the hell out of me. Yeah. Those are common transceivers on FPGA that are super high. Like, what is it, like, 5 gigabit or 60 gigabit, something like that? Yeah. Or more.

**Dmitry Netospazov:** I mean, it's the speed of USB 3 in that case, which is, I guess, 1.8 gigabit?

**Dave Jones:** Well, in the case of USB 3.0, it's a 5 gigabit physical layer speed. Oh, right, right, right. And so we have this 5 gigabit FI chip that basically gives you, you know, breaks that high-speed serial link out into a parallel interface with a whole lot of pins. I think it takes something like 180 pins or something to completely implement that interface. And so we took three of those and put them on an FPGA so that we could do, like, a USB man in the middle with an additional USB 3.0 interface going to a host computer for control and monitoring and stuff. Wait, three of those transceivers? Three of those transceivers hanging off an FPGA, yeah. Holy crap. Yeah. So it ends up being a whole lot of pins. So that's 180 times three? Right. Yeah. Wow. But we made it work. And as a part of that project, we had to implement all the logic for the USB core, the USB interface in our own core on the FPGA.

**Dmitry Netospazov:** My favorite story was daisy-chaining all the USB analyzers that were available. Oh, yeah.

**Dave Jones:** Yeah, because the – I mean, this was in early days of USB super speed. And the test tools that were out there, hopefully they've gotten better. But the ones that were out there at the time, they all kind of had their own bugs. And so we had cases where we would, like, daisy-chain multiple USB 3.0 test tools just because we were trying to test our own core. And we had to – we kept on running into bugs of the test tools. And so we would need to do tests where we would have, like, one test tool A to work around test tool B's bugs and test tool B to work around test tool A's bugs. It was nuts. Yeah.

**Chris Gammell:** That is a lot of – and so this is all Daisho, is that right? Yeah. Okay. So we've talked about Daisho on the program before. Is that released yet or no? No.

**Dave Jones:** I mean, it's still – it's out there. It's released as open source, but we haven't commercialized it.

**Chris Gammell:** Okay. So you're not selling it. Like, people can't go and buy it right now, right? Right.

**Dave Jones:** Okay. It's something we might sell in the future. In particular, using it as a platform for this USB 3.0 core is something that I would like to make available to people. Yeah. I'm not sure how popular our original intended uses would be in the marketplace, but just having something that you could buy off the shelf and, like, start building your own custom super speed USB device that's fully open source hardware and software might be useful to people.

**Chris Gammell:** Yeah. That's great. That's really great. I think my brain's exploding from that. I don't even know what to say next. All right. Changing topics. Yeah. You guys are talking about Med – what was it called again? MedSec? MedSec. MedSec sounds – yeah, that sounds weird to me. So what is it? What is it first?

**Dmitry Netospazov:** I should prepend this by saying – so there was a conference in the Netherlands. I guess it was maybe two weeks ago now. So it was hardware.io, hardware spelled like wear, like you're wearing something, which is – I guess that's how it is in 2016 with domain names. But –

**Chris Gammell:** So there was no, like, tie-in to, like, wearables or anything like that? No, no, no. That's not how they did that? Not at all.

**Dmitry Netospazov:** No. So it's –

**Chris Gammell:** That seems silly then, yeah.

**Dmitry Netospazov:** They had a lot of – I mean, so it was hardware-focused, hardware-security-focused. So I very much recommend the listeners take a look at that conference. And as far as I know, all the videos – almost all the videos will be on YouTube minus the couple of people who ran into cease and desist from the vendor. Oops. Yeah, so – These things happen. That's a perfect segue into MedSec, actually. Which is – so one of the topics of the discussion, they actually had a very good panel. And one of the people on the panel who was most outspoken and had the most, you know, I would say things that were on point to say relating to the whole MedSec fiasco was Katie Masuris, who's famously somebody who is very closely associated with responsible disclosure or the correct process of letting a vendor know that you know about vulnerabilities and whatever they're selling. And so there was a very heated discussion just with a lot of people who were there because it's something that a lot of people who – I mean, Mike and myself certainly have come across similar situations where you're reverse engineering some piece of hardware or looking at the security of some piece of hardware and you tell the vendor and they send you a cease and desist and say, please don't look – or not please. They don't write please. They say, please.

**Chris Gammell:** They say, please, yeah.

**Dmitry Netospazov:** Don't look at our devices anymore or we'll serve you. And that's a huge problem.

**Chris Gammell:** Yeah, and is there like an actual precedent for – like this is where I always get interested too because it's like – so I've watched – like I see a lot of the announcements and stuff like that. And usually before anyone announces about it, they're like, well, we inform the vendors so that they can go and try and patch this stuff.

**Dmitry Netospazov:** That's the proper way of doing it. So this story where this story gets shady is – I mean, I wouldn't call it – I mean, I would – as somebody who comes from this field, I would totally say that this is a gray area. And so they're at court – I mean, this whole case is going to court. And so there's not a legal precedent for this yet. But so that's why –

**Chris Gammell:** And it's international too, right? I mean, that's the other problem, I'm sure, is that –

**Dmitry Netospazov:** Yeah.

**Chris Gammell:** You can have a legal precedent in one country and then you just go somewhere else and it doesn't apply anymore.

**Dmitry Netospazov:** Right. But I mean – so basically what happened with this case is this – so there's so many sides to the story. And I've heard so many sides to how this actually happened and how – I mean, so I bet the court filings or whatever comes out of court will be the most, you know, true view. As to who did what when. But the gist of it is there's this company who was studying the security of a medical manufacturer, a medical device manufacturer, specifically – I'm trying to think of what – St. Jude. Yeah, it's St. Jude, but I'm trying to think of what's the device called for your heart? Cardio.

**Dave Jones:** Pacemaker. Pacemaker, yeah.

**Dmitry Netospazov:** And ICD.

**Chris Gammell:** I'm thinking of the German word. It's an implantable something-something, right? Right.

**Dmitry Netospazov:** And so what these guys did at MedSec was they released – I mean, so they had a bunch of bugs that they found. A bunch of them were critical. And I mean, as somebody who's looked at medical devices before, medical devices, cars, anything related to IoT, the security is complete crap. I mean, that's why there are people like me and Mike who do consulting in this area. And I have yet to fail on devices that I get from most manufacturers because the level of security is – it usually starts with when they sent me the device is when they start implementing security. And that's unfortunately true for medical devices as well because there's actually – people underestimate how many medical vendors there are. And they're at such – they're having so much – I mean, so basically they have certification there. So one of the big factors is actually that they have certification. So the fact that they have to have this device certified, the certification also implies that if this device – if vulnerabilities became known related to this device, they would lose certification. Which, I mean, in theory on paper would mean people have to go back into the hospital and have this device taken out of them because it's not – it's no longer considered safe.

**Chris Gammell:** There's some real-world implications in this stuff. Right. Much like cars though too, right? I mean, like there are – right? There's always –

**Dmitry Netospazov:** Yeah. I mean, cars are another whipping boy for everyone in the security community right now. And you'll see – so specifically at hardware.io, I think there were three or four car security talks with, you know, somebody shows this for manufacturer A, somebody shows pretty much the exact same face palm for manufacturer B, then there's manufacturer C, et cetera, et cetera, et cetera. But anyway, so here's where your mind is going to explode even more than talking about three surdeezes and FPGA in between is what these guys did, and I don't know how the communications went, is they gave this information to a hedge fund. Whoa.

**Dave Jones:** And specifically a research firm called Muddy Waters Research. Muddy Waters. Which is a fantastic name. That is just – yeah. It is. That works out well. It's like a movie, yeah. Right, right. And like what Muddy Waters does is they publish research about publicly traded companies while short-selling the stock of those companies.

**Chris Gammell:** Yeah. It's like – who's the Moneyball author or what's his name? Big Short. Michael Lewis is going to have a field day with this stuff, right? Yeah. Exactly. No, and I mean – It writes itself.

**Dmitry Netospazov:** Get on it, Mike. So you can imagine what ended up happening. So they disclosed these vulnerabilities. Apparently, St. Jude is very close to an acquisition, so it was the worst time ever –

**Chris Gammell:** Oh, my God. Yeah.

**Dmitry Netospazov:** For this to happen to them and their stock went down. It bounced back up when should I – but it was –

**Chris Gammell:** Right, but you could have bought it at – you know, you could have bought it at the low point and then made a bunch of money when it bounced back up.

**Dmitry Netospazov:** Right. Or sell on the way down as well. Wow. That's insane. That's insane. So, like – So you make money –

**Chris Gammell:** Are we just seeing hardware people and security people being hired in order to find vulnerabilities in order to –

**Dmitry Netospazov:** I mean, so this was exactly the discussion bit and that's why –

**Chris Gammell:** That's like some Bond-level shit right there. That's like when – No, that's it. In that one movie where they're trying to blow it up the plane in – what's it called? They're trying to blow up the plane in order to short the stock, right?

**Dmitry Netospazov:** Yeah.

**Chris Gammell:** Sorry. Spoilers. Spoilers. It was the first Bond with Daniel Craig. If you haven't seen it yet, you're stupid, by the way. So, yeah.

**Dmitry Netospazov:** Should we have done a spoiler alert before talking about getting free parts from TI as well?

**Chris Gammell:** Stop bringing it up, man. It's fine.

**Dmitry Netospazov:** I swear to God. Someone's making money here, I think, you know. No, but it was – it's a very mind-blowing precedent for the reasons that you said because – Yeah. I mean, the funny – One of the comments that came up in the discussion – So I totally enjoyed the conference for this discussion because I didn't expect myself to be in a room with, you know, I don't know how many people were at the conference, but I would say, you know, 20 or 30 people that I respect very highly that also do security stuff talking about this case. And it was very interesting to hear – it was very, very interesting to hear what everyone had to say. One of the best comments was that, you know, short selling and making money on the way down, the whole ethics aspect, you can apply ethics and say – I mean, you can say short selling is bad in general. But most people react to the ethics of this being bad is – I mean, the ethics is related – But they didn't do the security in the first place? No, but the ethics is related to you saying, I can turn off someone's heart. That's much more – a much bigger aspect of, you know, what people feel is unethical about what happened, more so than what happened to the stock. And so one of the comments was, what if this was any other device? What if this was some IoT startup or something, some IoT piece of crap that you hang on the wall? And the results were as profound as what they did. And the answer, everyone kind of stood there scratching their head. And I think a lot of people had – I mean, couldn't decide if they would categorize that as being the same thing. Right.

**Chris Gammell:** This is like next level stuff, basically.

**Dmitry Netospazov:** Right. But, I mean, having said that, the irony is then a lot of people came out with their stories of exactly what I was alluding to at the beginning, which was that you look at – So, especially if the – so, usually now when I do contracting work, I wait for the manufacturer to come to me. Because my experience of doing – just spending the time and doing any sort of low-level hardware stuff that I'm actually interested in doing for a vendor, it's exactly what ended up happening, which is this company sent a cease and desist to MedSec and said – took them all to court. And, I mean, the lawsuits are still forthcoming. But –

**Chris Gammell:** Lawsuits are flowing like wine, huh? Right.

**Dmitry Netospazov:** And, I mean, that's totally – it's totally an issue. And the reality is kind of – I don't want to get into market mechanisms. But one of the arguments was that short selling is a mechanism that one can use for the discrepancy between a manufacturer will either pay you zero or something like – maybe they'll pay you for three months of consulting. Right. Whereas the damages to them are million – you know, can be multi-million dollar damages if you were to publish this research. Right. You know, openly –

**Chris Gammell:** And that's always where I get into it, too, is like I think about – so I think the security field in general – and I do like the disclosure stuff. But there's just – it's basically not – I won't say – it's not quite blackmail, but it feels kind of like blackmail. Like you totally could blackmail someone. Like I will publish this unless you pay me to fix it kind of thing. And –

**Dmitry Netospazov:** I mean, there is that aspect to it. Although I wouldn't say you go out and blackmail companies. But the issue – Right, right.

**Chris Gammell:** You'll get more people with honey than vinegar type of thing. It's like here's your issue. By the way, I know how to fix it is a lot better than –

**Dmitry Netospazov:** I wouldn't even go – I wouldn't even go as far as to say it's honey and vinegar. It's just that the software security industry and, I mean, specifically companies like Microsoft, they had so many issues related to security that they're just light years ahead of the hardware industry. And the hardware industry is basically where the software industry was in the early 90s, quote unquote, with the same kind of disclosure policies. I mean, the irony of it is that there is no legal way to go to one of these manufacturers. They don't have on their website a disclosure policy. Like if you come to us, we will – I mean, so for example, if you – I have friends who professionally do something called fuzzing. So they run fuzz farms. They have all these servers that they set up. And they basically start Firefox, Chrome, Safari, et cetera. And in an automated fashion, test different, you know, malformed images and see what crashes. And in this fashion, they find tons and tons of bugs in the browsers. And what happens is Google pays them $1,000 per bug that they find. And that's something completely different where – I mean, so that being an example of where there's a very – you know, you can go on the manufacturer's website, on the vendor's website, and read, what am I going to get paid for this class of bug? And so also notably, Apple recently – so now they're discussing and now they have all the security.

**Dmitry Netospazov:** You mentioned this to me.

**Chris Gammell:** Yeah, yeah, yeah. This is great.

**Dmitry Netospazov:** And so they're also rolling out a security kind of – so a responsible disclosure and what's called a bug bounty. A bug bounty is where you define what you're going to pay per bug. And so –

**Chris Gammell:** It's very upfront. It's understood that like, yeah, you find one, it's not – it's no longer a ransom. It's more of a prize. Right.

**Dmitry Netospazov:** Exactly. And I mean, the manufacturer – I mean, the manufacturer should be interested. They should also have their own – you don't have to – I mean, selling them your work isn't a matter of first convincing them that they need it. They should be aware that this is something that is part of – I mean, especially if there are things like certification at play, they should have a budget and an interest in going out to security professionals and catching the things before they end up on the internet. And they have to pay – I mean, they can either pay security researchers to help them make their devices more secure or they can spend the same amount of money on lawyers and sue the security researchers.

**Chris Gammell:** Right. Or recalls in hardware's case. Right.

**Dmitry Netospazov:** Yeah. I mean, that's the only issue where it's a problem in hardware is the recall and how to do the updating. And especially with medical devices, it's even worse because a lot of times the software and the full stack gets certified. So they even can't roll firmware updates without getting recertified. But having said that, that's all to – I mean, for me, that just means that that's not kind of an upgrade cycle or a firmware update cycle that's viable for the future, they should come to security experts and consult with security experts who would tell them that you need to – so step one is you need to have a certified USB bootloader that you can lock down and use some sort of decent cryptography and whatnot to kind of keep people from pushing malicious updates. And then next step is you have updates on a regular basis and you test these, et cetera, et cetera, et cetera. So, I mean, I really – I have my fingers crossed that this will mean that especially in the area of IoT where everyone's building hardware devices for, you know, everything you see around you is connected to the internet in some way, I have my hopes that there is a future and that the vendors will recognize that this is something that they have to spend money on and there's a very easy way if you make, you know, reporting bugs to you both worthwhile for the researcher and easy, then it's something that they'll do versus selling it on the black market. And I mean, that's the – That's pretty close to what it seems like, right? Yeah, but I mean, that's the other – I mean, so I would definitely say that I don't want to get into a lengthy discussion about, you know, ethics of short selling and whatnot, but this is clearly a gray area. It's not black – it's not, you know, something completely black hat that they're doing. And same – it's a gray area. And if the official way is I go to the vendor and they'll pay for my flight to come and meet with them and then not do any consulting services and make me sign an NDA before they talk to me, then – and the other option is I sell this to, you know, on some market somewhere, then a lot of people are going to choose I'm going to take, you know, in cash this amount of money and sell it to the black market versus –

**Chris Gammell:** There's a higher – yeah, there's a higher risk, but there's probably also a higher payout as well. Yeah. That's pretty crazy. Yeah, I don't know. I think it takes – it takes events like this, like it's very tangible with a pacemaker, right? It's like Nana's going to die if some hacker messes with it, right? That's very tangible.

**Dmitry Netospazov:** No, but let's say – now let's say you find a bug in the power management IC of a Samsung Galaxy S7 and you can get the battery to explode or something along those lines because they're –

**Speaker ?:** Sure, right.

**Dmitry Netospazov:** Right. That's totally something that I see in the future as well. Or your Samsung washing machine, you somehow over the Wi-Fi interface or whatever, you somehow trigger it to go out of control and destroy itself.

**Chris Gammell:** Yeah.

**Dmitry Netospazov:** Not to pick on Samsung. I mean, that's totally true for all IoT and consumer devices.

**Speaker ?:** Right.

**Chris Gammell:** Anything connected, if you can figure it out, you can probably make it at least break if not hurt other things as well, right? Right. Yeah. Yeah, that is – I actually didn't know about any of that stuff. So that's very interesting that that's coming up. Let's say. So where do we go from here? Like, not like on the show, but I mean, like, where do we go on the security side then? Like, so is this all just so you guys sell more training? Is that what it comes down to, guys? Well, it is an exciting time to be in hardware security. Yeah, I believe that. Man, that's great. And so do you guys get approached about this stuff now too where it's like when people are taking your training, like, well, we're trying to do this because yada, yada, yada, yada, yada. There's new policies in order to make sure our devices are rock solid.

**Dmitry Netospazov:** I mean, I can comment from my side. The only industry that I've touched where there's, as I described last time, where there's a recognition that they have to spend a ton of money on security before they run into problems on the black market or kind of from a discrepancy between what they're willing to pay and what the security is worth to them and how much people are willing to pay for on the black market is to this day, to me, there's one area in hardware security. They got it right, and that's pay TV, and that's securing your satellite TV so that you can ensure that people are actually paying you for porn and sports.

**Chris Gammell:** Yes.

**Dave Jones:** Well, I'll add one more relatively small industry to that list, and that is gambling machines.

**Chris Gammell:** Right. Ah, yeah. But ironically... It's stuff that's really close to the money, like super high margin, super easy to steal, right? You can't... It's not like you're stealing a piece of hardware or hurting a piece of hardware. It's basically bits turned into cash, and they want to protect that bit stream, right? Yep.

**Dmitry Netospazov:** No, but with gambling machines, ironically, a lot of the vendors there are, in one way or another, also using smart cards and kind of come from the same industry. And then if I was to continue down that path, a lot of point-of-sale systems have pretty good security as well with all kinds of meshes so that you can't stick your screwdriver drill in and then they'll short and erase the EEPROM, and it's all running off a battery backup and all that kind of stuff. So they're pretty good, too. But like I said, most devices, and unfortunately, my... I mean, I was also having this discussion, what would examples be from that category? And I think kind of one of the parameters is public safety, and I would say medical devices is definitely one, and automotive is definitely another big one. Yeah.

**Chris Gammell:** Yeah. Well, that's... We keep seeing more and more articles about people probing those systems, so I'm sure that wherever there is opportunity for research, people are going to go towards that first, right?

**Dmitry Netospazov:** Yeah, absolutely.

**Chris Gammell:** Yeah. Are you guys personally getting in the medical side, or what are your thoughts on the medical... Obviously, we're talking about the ethics stuff here, but are you interested in that side of things?

**Dave Jones:** Not me. I mean, I'm interested, but it's not an area that I'm actively working toward.

**Dmitry Netospazov:** There's a lot of RF and medical, Mike.

**Dave Jones:** Well, that's true. And I have helped other people out with their research projects on medical devices when they run into RF stuff, but it hasn't been a primary research area for me.

**Chris Gammell:** Okay.

**Dmitry Netospazov:** And for me, I mean, I've looked at medical devices before, but with me, one of the reasons I haven't looked at it, or at least I don't look at it in my spare time is because it's all RF stuff. I mean, especially if you have a pacemaker, the only way to interface it is over the air.

**Chris Gammell:** Oh, right. You don't have wires coming out of your shoulder or something? Exactly, yeah. Not yet. Not yet. That's right, guys. Every time I see things about implant... I know this is off topic, but every time I see these things about, oh, implantable this, implantable that, and I'm so squeamish about medical stuff. And I've talked about it when Dave was talking about his knee. I just... I get so grossed out by anything implantable. And people that are doing biohacking stuff. Short aside there.

**Dmitry Netospazov:** I had an ice hockey coach, and one time I banged up my knee and I couldn't walk for a while. And he had a model of the knee, and he was explaining all the sport injuries you can get to your knee and pulling the tendons out of the knee. And I could feel everyone in my knee as he demonstrated them on the model.

**Chris Gammell:** Yeah, that's... I guess I won't be going for the brain implant as soon as they come up with that. But, yeah.

**Dmitry Netospazov:** I want to see the standardization process for an interface that they make for people to devices.

**Chris Gammell:** Yeah, that'd be a lot of arguments, huh? I think that's the last thing about medical, too, is just that, like, at least in the States, the, you know, like the approval... You guys alluded to this, too, but the approval process is just nuts. Like you said, with the full stack certification and stuff. And I'm sure that's a huge piece of... Even if there is... There's probably a calculated, you know, like that scene in Fight Club where it's like, if A plus B plus C equals less than the cost of a recall, we don't do it kind of thing, right? Or less than the cost of lawsuits.

**Dmitry Netospazov:** I mean, that's the unfortunate truth of medical devices, of automotive is... That's... I mean, that's... That scene from Fight Club is the truth.

**Chris Gammell:** Well, it'll shake itself out one way or another, I'm sure. Mike, you said you had one or two other things on your list. I know we're bumping up against hour 40 right now, but I've got time for one or two more if you guys do. I don't know.

**Dave Jones:** Yeah, I have all sorts of things. So, speaking of automotive, I don't know if you guys ever discussed on the show the VW, the Volkswagen... Oh, the cheating on the firmware, right? Yeah. The emission stuff. Did you guys talk about that? I can't remember. I'm pretty sure either.

**Chris Gammell:** We mentioned it, but we... I mean, like, what are we going to say?

**Dave Jones:** Like, oh, bad. That's bad. Yeah. Well, anyway, I just had it on my long list of things that might be interesting to discuss at some point. Uh-huh. Because it was a really interesting case, I thought, of where kind of firmware developers could have a major impact in the world.

**Chris Gammell:** Not necessarily positive. Right, right.

**Dave Jones:** But, yeah. And also, it's a really interesting case when it comes to the security kind of vulnerability disclosure debate and also the right to tinker with your car or anything that you own.

**Dmitry Netospazov:** If I can add one more, it was super interesting for me to find out that in Germany, the engineers that did it and knowingly, even if they knew what they were doing, the conclusion was, at least from what I read in the press, if they were following orders, there's not a whole lot that they can be held accountable for if these were demands coming from above.

**Chris Gammell:** I thought they were the only ones that did get in trouble. That's at least what I remember. But maybe that's...

**Dmitry Netospazov:** I mean, we'll have to go. There was a really good talk at CCC about the specifics, I'm sure.

**Chris Gammell:** Yeah, there was.

**Dave Jones:** Okay.

**Chris Gammell:** Anyway, so what about the disclosure stuff, though, Mike?

**Dave Jones:** Well, like, one of the interesting aspects, I think, of the whole Volkswagen case is that it was discovered by a third party. And if you don't have the ability to actually, like, tinker with your car and find out what it's doing, you're going to lose the ability to, like, check and make sure that the manufacturer is doing what they say they're doing. Right. And that's pretty important for things like emissions, where we really rely on manufacturers to do things right. And one of the more interesting aspects of the case, I think, is the actual settlement between Volkswagen and the EPA in the U.S. The fact that the EPA was able to seek tremendous damages really kind of highlights that vendors are on the hook. And if they don't do things right, you know, they're going to be subject to things like a multibillion-dollar settlement.

**Dmitry Netospazov:** I mean, going back to our previous conversation as well with what you could do on the financial markets with that information. Oh, yeah. Right. Absolutely.

**Dave Jones:** So it's another aspect of kind of the disclosure debate or the disclosure options that people have available to them. In the case of MedSec, we had public disclosure with a short sale. In the case of Volkswagen, you know, we had kind of public disclosure with the EPA and other government agencies around the world getting involved. Right. But that's going to affect stock price as well, right? I mean, I'm sure it took a dive.

**Chris Gammell:** Yeah, totally. Oh, yeah.

**Dmitry Netospazov:** I mean, they were talking about, I remember reading stories about that Volkswagen is going to sell Porsche and all this kind of stuff.

**Chris Gammell:** Oh, yeah. Yeah. Yeah. Yeah. It's kind of crazy to think that this stuff could actually have, like, monetary, like, hardware hacking for fun and profit, right? I mean, like, there's some legit money-making ability there. But like you guys were saying, it is a pretty – oh, man. I'm looking at the price now, too. Sorry. I just pulled up the stock chart, too. It went from 250 and then it dived all the way down to below 100. Wow. So, yeah. That's a significant – That's a big – Yeah. That's a big choice.

**Dmitry Netospazov:** Their market cap is huge as well.

**Chris Gammell:** Yeah. Mm-hmm. So, wow. So, yeah. Yeah, there really is a lot of implications in the – because it's all built on confidence, right? I mean, that's what stock markets are built on confidence and future growth earnings. And if you can disrupt that, it's like you have a lot of power.

**Dave Jones:** Yeah. And meanwhile, Volkswagen and other manufacturers are moving towards and lobbying for the legal right to move towards even more obscured systems that are harder – that are protected from tampering or analysis by third parties. Yeah. And so I think it's a really important part of the kind of right to hack your own stuff debate that if you don't – if we lose the right to tinker with our own devices, our own cars, et cetera, then we're going to be, I think, seeing more things like manufacturers cheating at their emissions tests. Or all the – One example.

**Dmitry Netospazov:** Or all the hardware hackers become whistleblowers.

**Dave Jones:** Yeah.

**Chris Gammell:** You know, it's interesting thinking about that. So, we talked about it on the show a while back with the John Deere thing. Remember, they were talking about John Deere and not being able to access firmware and stuff like that. And they did it from the IP perspective. They're like, oh, well, we can't have people messing with this stuff because there's proprietary information in there. And yet now this has me wondering, like, was that actually more of a financial concern? Because if someone finds a vulnerability or finds something like that – I mean, John Deere is a huge company, too – that there's real-world implications of that, of people being able to get in there.

**Dmitry Netospazov:** I mean, I think for a company like John Deere, they're – I mean, any sort of big manufacturer, especially, that's been around for many, many years, they do have a very sincere concern that if anything became known about their, you know, secret recipe – Make the wheels go forward. Right. Big wheels on the back, small wheels on the front. Turn on the thrasher. Right. But, I mean, they really do think that they have to protect their secret sauce to that extent. But it's also – that's also something – I mean, this just gets back to how – what a discrepancy there is between the software industry and software security and hardware, where it's – can I – you go to one of these manufacturers and to do any sort of project with them, if you want to do it on kind of the, you know, help them in improving their security, it'll start with – They'll send you so many NDAs that you'll never be able to talk about ever having touched one of their products. Right. And they'll send you so much proprietary documentation. I mean, in a way, kind of to prevent you from ever looking at their products again, just so that they know that legally you're kind of one of the team.

**Chris Gammell:** Right, right. They've got you under lock and key, right? Right.

**Dmitry Netospazov:** And exactly what you said with – It's a hardware hacker chastity belt. Yeah, exactly. No, and I mean, it's – so like I said, for me, this whole MedSec thing, and I didn't think about the bulk second case in the same way, but Mike's totally right that it's similar in terms of epic proportions that, you know, it's yet to be determined what consulting for companies like that will look like in the future.

**Chris Gammell:** Well, anything else on the list, guys? I think that's probably a good spot. Okay.

**Dmitry Netospazov:** But people should totally watch – I guess we should link it into the show, but people should totally watch the CCC talk about the car stuff because – so half of it they had – I know because I also help out with the CCC a bit, and especially in the talk selection, I know that they had two people submit to the topic of Volkswagen cheating. And so one person talked about how an engineering – how the engineering looks at the company. And the second person talked about the technical details as to how he was able to discover stuff in this firmware of an architecture that he's never looked at before. And my favorite part was just when he talked about that he figured out that there was some curve, implicit curve in the software with like an upper limit and a lower limit, and that he just drove according to this curve. And then his – you know, the actual additional fluid or whatever the technical term is that gets added to these diesels to make them more emission-friendly. That turned on and the emissions would go down versus it being in a kind of an operating state where it wasn't caring so much about the emissions. And then just the moment in the talk where they overlaid the curve of what's necessary for certification, and it's right flat in the middle of what he reverse-engineered from the software. So it was totally – it was clear to everyone just by the fact that the margins were the same on the positive and negative side that that's exactly what this was for without any shadow of a doubt for anyone who's done software or firmware or anything like that.

**Dave Jones:** Yeah, that was really good. And I also really liked the aspect of that – I think it was the other half of that talk, which was kind of giving people an insight into the engineering and the firmware developers and how in this industry kind of what we see as cheating. And I think in this case at least was pretty overtly cheating. But it was really kind of a small step from this sort of – I would say the equivalent of a white lie, you know, the sort of commonplace cheating that happens all the time.

**Dmitry Netospazov:** Yeah, the examples are awesome. Like the testing they do on the road for aerodynamics and miles per gallon, they remove the left mirror because that's – no country is that – are you actually required to have a left mirror on the car? Yes. Yes.

**Dave Jones:** So there are all these funny cases where auto manufacturers for decades have been developing tests and dealing with compliance for all sorts of different things. And they find – and there have sort of been these sort of industry standard cheats that have sort of developed along with the tests. And so the VW particular cheat is a pretty bad one, but it isn't that much worse than the kind of stuff that they're doing all the time to deal – at all various manufacturers to deal with a bunch of different regulatory requirements. Right.

**Chris Gammell:** They also – It kind of reminds me of like my friends who were wrestlers in high school where it's like they're trying to get into like the one whatever weight class and the days before they would not eat anything. Sure. And it's like I think you guys are missing the point here. I know you're doing it for – it's a competition, right? So, of course, people are going to optimize for that stuff. But it's like that's really dangerous, you know? Like it's the same kind of thing where it's like that's not really why that stuff's there, but people optimize for those reasons. And it's dangerous. You optimize what you measure. That's right. Yeah, exactly, right? And I've never, ever, ever gotten the proposed mile per gallon on the sticker. I'll tell you that. Right. And I've tried. I just never got it.

**Dmitry Netospazov:** No, but the examples were so damning and so hilarious when you think about them. I mean like they – of course, they do the miles per gallon testing on an empty tank because that extra weight from the tank being full would make your miles per gallon worse. And then – but my – I mean the one that I didn't expect at all was filling up all the air intakes so the car becomes even more aerodynamic.

**Chris Gammell:** Ah, nice.

**Dmitry Netospazov:** But the engine overheats, but it doesn't matter because the test is for, you know, a couple minutes so it's fine to do it.

**Chris Gammell:** Right. Well, you might say the same thing about data sheets, right? If you're using parts, they're testing you to the extreme limits, but whatever. Yeah. So anyways, you guys mentioned CCC and you mentioned all the other things. Can you quickly rattle off the places you'll be in case people might be at these conferences in the next couple months, maybe through the end of the year? I know there's a couple, but just in case.

**Dave Jones:** Yeah. Well, we'll both be at TourCon in San Diego and we'll both be at Zero Nights in Moscow. So I'll be at Open Hardware Summit and also Power of Community in Seoul and Black Hat Europe in London.

**Dmitry Netospazov:** And I'll be at – I mean, I don't know if – I'm trying to think if I'll go to any other conferences. I think I'm only going to TourCon, Zero Nights, and CCC this year. Yeah. Hmm.

**Chris Gammell:** Okay.

**Dmitry Netospazov:** So CCC is probably of the aforementioned conferences. I would say for people interested in hardware hacking, probably CCC is the best choice to go to. But it's also the absolute worst time of the year because it was decided by hackers that it would be cool to see everyone before the year is over, which also means it's right after Christmas.

**Chris Gammell:** Right. And I actually was thinking about it. Last time I looked, there wasn't any information. Is there more information out yet or no?

**Dmitry Netospazov:** I mean, I know the CFP is definitely out, but it's always the same dates, man. It's always the 27th to the 30th.

**Chris Gammell:** And it's in Hamburg, is that right, in Germany?

**Dmitry Netospazov:** This year will be the last year as far as I know that it's in Hamburg and then they'll pick a new location because they do that moving around Germany. Cool. But yeah, you should come out there, Chris. There's a lot of cool people to hang out with there like Bunny.

**Chris Gammell:** Yeah. Like I said, I've been thinking about it. And so I, and it goes through New Year's or no? You said it's the 30th, right?

**Dmitry Netospazov:** Yeah. I mean, I can't remember if the 30, it's usually the 30th, yeah. But a lot of people stay until the 31st and just hang out in Hamburg or Berlin. I mean, Hamburg's two hours by train from Berlin. So it's really easy. And the conference is literally at Hamburg's second train station. So you can literally get on the train and go to Berlin. And two hours later, you're getting off the train in Berlin.

**Chris Gammell:** Very nice. Awesome. Well, guys, thanks for coming back on for another impedance matching episode. I think this one definitely took a turn with that whole, that ethics stuff. I think that stuff is, I'm going to be thinking about that for a while. I'm sure our listeners are too. We'd love to hear from them on Twitter or a comment section or email, feedback at theempire.com. Where can people find you guys online?

**Dmitry Netospazov:** So people can find me on Twitter, NEDOS, N-E-D-O-S. And my website for the consulting work that I do, which includes upcoming training dates, is toothless.co. And I just check. And if people still want to take the training, then there's a couple of slots left if people are interested in the kind of stuff that I do.

**Dave Jones:** Cool. I'm at Michael Osman on Twitter. And you can find me at greatscottgadgets.com.

**Chris Gammell:** Awesome. And you can also find my cleaning out dog kennels. I hear them. They're going a little crazy, Mike. It might be time to go feed the pups, I think. Yeah. You know. Could be. All right, guys. Thanks again. We'll talk to you soon. I'll see you sooner, hopefully. See you next week, Mike.

**Dave Jones:** All right. I'll see you next week. And I will see you, like, tomorrow, Chris. That's right. See you.

**Dmitry Netospazov:** All right. Bye. Bye. Bye.

**Speaker ?:** Bye.

**Chris Gammell:** Just under.
