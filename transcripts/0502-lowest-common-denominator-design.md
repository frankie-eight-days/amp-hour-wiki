---
episode: 502
title: Lowest Common Denominator Design
url: https://theamphour.com/502-lowest-common-denominator-design/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released July 26th, 2020. Episode 502. Lowest Common Denominator Design.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. What's up, nerd? Hey, man. You're going to change the blog name to EEV Drive or EV something? I don't know.

**Dave Jones:** EV something. Oh, I can, yeah, I might do a teaser Twitter photo. Anyway, yeah, I'll tell you about that. No, I'll just tweet it. It doesn't matter.

**Chris Gammell:** Anyway.

**Dave Jones:** So, what?

**Chris Gammell:** You want to talk about that straight off the bat, do you? Sure. Well, we can talk about other stuff. You know, we'll leave that as a teaser for later, too. Yeah. What's going on in your design world? What are you building these days?

**Dave Jones:** What am I building? I am working on, well, you saw a video. I'm working on selecting chips at the moment and working on a, well, a potentially different variant of the microcurrent.

**Chris Gammell:** So, it's almost like maintaining. You're like the maintaining engineer as well.

**Dave Jones:** Ah, right. The, yes, component obsolescence engineer. And, right.

**Chris Gammell:** The CEO, the maintaining engineer, the janitor, the marketing person.

**Dave Jones:** Yeah. Yeah, that's it.

**Chris Gammell:** Oh, man.

**Dave Jones:** Oh, boy. And, like, I did a video, like, looking at, because I designed the microcurrent 12, 13 years ago or something. Like, it's a long time ago. It's actually before the blog, right? And back when I was a regular engineer, when I actually had to do real day job.

**Chris Gammell:** Instead of playing one on TV, you're saying? Right.

**Dave Jones:** Yeah. Instead of playing one on TV. Yeah. And the things haven't changed. Like, I pretty much came to the conclusion that the Maxim chip I chose back then is still pretty much the duck's guts. Well, Maxim has changed. Oh, yes. Didn't Maxim? Yeah. They got.

**Chris Gammell:** They got swallowed up by the analog devices. Yeah.

**Dave Jones:** Oh, well, has it actually happened? Or they said they were going to?

**Chris Gammell:** It has officially been announced, I think, during the quiet period now. Oh, officially announced.

**Chris Gammell:** But, yeah. So, Analog Devices is buying Maxim for $20 billion. $20 billion. And, of course, I went on Twitter and complained about it. And everyone's like, well, but, you know, it's small compared to other things. I don't care about other. You know, like, okay, you're going to compare it to Samsung. You're going to compare it to Intel. I don't care about those companies. I care about the ones that I'm buying from. Right. Yeah, of course. And I care about less part choice. And I care about the fact that there's going to be fewer support people and fewer people in the industry. And it's like, that is, this is a bad thing. I mean, I just, I always keep maintaining that. Even the LT stuff. Like, we've already seen. Oh, yeah. Exactly. You know, there's been layoffs from linear technology.

**Dave Jones:** Yeah, but linear technology, in turn, gobbled up a couple of others. And then, you know, didn't they over the years? And Burr Brown, who bought Burr Brown? Burr Brown is TI. That's TI. Oh, TI. Okay. Yes, of course. Yeah.

**Chris Gammell:** And I mean, when it comes down to it, I figure it's going to be, there's going to be two left standing, you know, Pepsi and Coke is going to be TI and more devices. You know, I think that's, I think that's how it's, how it's all shaken out right now. And yeah, there's going to be other type of chip suppliers and that's fine. You know, there will be other ones out there, but I don't know the ones that I pick from.

**Dave Jones:** For my entire career, like Maxim and analog devices have been like arch rivals, you know, it's been like, Oh, you're either, you know, you're a Maxim man or like sort of like Maxim always for those who don't know back in the old days, it's changed these days, but Maxim always came out with, they were just churning out new designs. Like there was no tomorrow. They would actually, actually release these six monthly data books, like, you know, two inches thick data books with new chips. They'd just released in the last six months. It was just, so, so you got these like six and a half yearly. Yeah.

**Chris Gammell:** You get like the, you get the update book.

**Dave Jones:** You get the update books because they couldn't print one data book big enough back when we had data books that actually contained all of the chips that they produce. So, so you had to get the yearly books.

**Chris Gammell:** Gather on children. The olds are talking about data.

**Dave Jones:** That's it. And, but, but that was the thing. And they came out with so many and their lead times was so horrendous at which we got a segue for lead times. So let's remember that for microchip. And like, and you couldn't get these things, but Maxim had the best sample service in the business, right? You could get samples so you can get onesies, twosies. And that was great for when I was working at the various military companies, right? We would only make like a handful of things, right? Yeah. So using the Maxim parts was great because you only needed a couple of chips because we'd only build like five, five boards. So we'd get out like five sample chips and then bingo, that's our entire production run done.

**Chris Gammell:** Yeah. I actually, I have a data point against that right now because I just got some parts in the mail yesterday and you know, they're obviously very different chips. They're more complex, but I got some cellular modems that are like, you know, sub $10 in production, but they charge more. They actually charge for the samples. There's, there is no sampling. Of course, but you're right. Okay. Yeah. Yeah. Yeah. And then it's like, so it was like 75 bucks for five modems and then another 75 bucks to ship them here. Cause they only do international courier. And so it's like, Oh my God. Yeah. You know, I don't expect them to do, you know, sampling, but, but still these are $30 modems now. Like this is not, this is right. You know, compared to comparing to a sample program, you know, this is, this is the opposite. This is the new reality. It's like, no, you're paying for everything. Okay. Fine. You know?

**Dave Jones:** Yeah. It's different.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Do many companies, does it, many companies offer sample services anymore? Is it a thing? I haven't, I haven't got.

**Chris Gammell:** So TI has like a official sample one. Uh, I think they have like online registration things. Yeah. They'll send you like, you know, two or three parts, uh, and then pass that. Then you got to start talking to salespeople and, you know, getting in the ERP system and proving that you're legit, you know, the old, uh, question, you know, what's your yearly,

**Dave Jones:** what's your estimated yearly buy? Yeah. You know, yeah. You's all they care about. That's right.

**Speaker ?:** Right.

**Dave Jones:** Yep. And of course everyone fudged that, but back in the day, like Maxim, they, nobody beat Maxim for samples. It was absolutely brilliant. It was free. They didn't care who you were and they, they would just, you know, send them to you, you know, and you'd get them by a very courier or whatever. And it was just, it was just crazy good, but, but you couldn't get them because the chips were like 40 weeks lead time. You know? So.

**Chris Gammell:** Well, yeah, they were sampling to anyone, but then they were selling to the big boys. And yeah, we've talked about that many times. Really. This is the only thing I'm sad about is that we won't have like, you know, fun things to, you know, kick around with Maxim having, Oh, we're different this time. You know, no, no, no, we're going to, we're getting better with our, you know, supply. And it's like, okay, well, I guess that's gone now. And I'm sure, you know, ADI is pretty great about their supply and I'm sure it'll be fine, but.

**Dave Jones:** Oh, no, it's no, it's good. And analog devices, like the two companies at Maxim were kind of like the company that made the cool novel new chips. They were always churning out, but T. Yeah. Like a one-off weird chip kind of thing. One-off weird kind of things, you know? So if you had like a niche, you know, a product that did this thing, Maxim probably made some analog-y type chip that, you know, did that. Whereas analog devices made you, if you really needed like really high precision, you know, the best characterized, you know, the best parts, you know, possible in terms of performance, you went to analog devices, you know, Maxim wouldn't have been your first choice. So yeah, but now they're, now they're one. Yeah.

**Chris Gammell:** Yeah. I mean, yeah, it kind of feels like that, doesn't it? It's like, it's like a, it's how do you vanquish your foe? Well, you buy them. Okay.

**Dave Jones:** And the crossover on their parts must be enormous. That will be interesting too. So imagine the team they've got now just, you know, they're probably, if they don't have a team already, they're forming it, figuring out which parts to actually discontinue.

**Chris Gammell:** Who's the winner and who's the loser. Yeah, exactly. I would imagine that like, I think they're all, I think, well, I remember ADI was, you know, they outsourced their, you know, fabrication as well. And, you know, everybody's using like TSMC or similar. Right. Foundry type works. Yeah. And, you know, in terms of like carrying costs for like the actual parts on hand, I, I have to imagine that it would make more, you know, like there probably isn't drop-in replacements just because they don't really do that. I mean, or if there are, then, you know, maybe they'll have, maybe there's a subset of the, you know, the functional crossovers that they'll be like, no, well, actually out of the 30% crossover that we see here, 5% are pin compatible, function compatible. You have to switch over now. Yeah. But I imagine that most of them, they, the amount they would be pissing off customers would not take.

**Dave Jones:** Oh yeah. No, it'd be enormous. No, no. You wouldn't expect them to suddenly discontinue them. And these companies never suddenly discontinue chips. They always give you a warning. Like this is like now an obsolete component, last buys are coming, you know, 2000, you know, last buys are coming in two years time, you know, look, just plan your, you know, these, these companies are good at that sort of thing. So, but yeah, there's gotta be some, gotta be a huge amount of crossover there where, you know, as you said, pin compatible parts, but yeah, maybe, you know, five, 10%, something like that would, I'd expect.

**Chris Gammell:** In all of this, every time this happens, right, this just happened with LT and it really just, it bugs me because, okay, some people might say, well, it's more efficient, you know, fine. There's, you know, fewer people in the marketplace, fewer places you have to shop. It's like, okay, but there, that means there's fewer options. There's few people are like fewer people innovating and trying to do, trying to offer parts to different segments of the market. And I just think there's less competitions worse in this scenario. So, uh, yeah, I, I don't think prices are going to go down. I don't think, you know, I don't think there's really any benefit for us. I think it's really just a shareholder-y kind of thing. And then they're like, okay, great. They're a bigger company. Now they can, you know, squeeze their margins harder and they make more money for their shareholders. Okay, fine. But that doesn't help me as a user.

**Dave Jones:** Exactly. Hmm.

**Chris Gammell:** But we don't really have any choice either. So even though like Tim, so Tim Ansel was on the show last week, he was talking about the open source PDK. Yeah. And, you know, we talked about some of the analog stuff. It's like, it's not like that's coming up anytime soon. You know, like that's not going to be offering op amps, you know, like precision op amps for anyone anytime soon. It might be highly integrated and have some, you know, have some analog capabilities in it, but it's not going to be anything like that. And so, yeah, if you're precision, you're basically, you're shopping in, you know, column A or column B and take what you got, you know.

**Dave Jones:** For those who don't know, when you're fabbing chips like that, unlike your digital chips, which you can just test and that's it. Like, you know, like simple, yeah. Like, you know, you can easily exercise the chips out, you know, maybe if they're really ultra high speed, high performance, that kind of thing, there's sort of variations, but analog chips are different. Analog chips, you have to characterize and guarantee various performance limits. If you deep dive down into the data sheets, you've got to look at the bin ins. And, you know, they sell all the different grades of op amps for a reason. It's because they've got to individually bin them, you know, and voltage references and, you know, stuff like that. They'll be binned into five different grades of actual parts, depending on how they come off the production line, how they're tested. And it's really complex and expensive to not only design test jigs to characterize all this analog performance, but actually do that as well. So if you think that you can...

**Chris Gammell:** But on every wafer, every segment of every wafer, it's not like you can do some sampling thing. You've got to be like, you know, unless it's like some super low cost thing, which they're probably not doing anyways.

**Dave Jones:** Right. So even if... So that's what we're saying. Even if they do have this, you know, do it yourself analog fab ASIC thing, then yeah. It's... Yeah, right. It may not be as good as it sounds. So yeah, you may be better off. Yeah.

**Chris Gammell:** I think it'd be good only in the integration piece. You know, that's really the only thing I can imagine. And, you know, and everything else that you need on, you know, so like Tim was talking about too, it's not just pure analog, high precision analog type stuff. It's more like, you know, there's other analog things on board. He said like the IO section is analog, you know, and everything that's not running actual just logic elements has some element, has some analog component to it. And you have to get the plan for that.

**Dave Jones:** Maybe you'd be better off like going for some custom hybrid bare die solution, for example, like take the existing, you know, if you want a complex analog system, take existing off the shelf wafers that are all characterized and tested and actually assemble those on like a hybrid module or something like that yourself, rather than actually design and build your own, you know, high performance analog ASIC.

**Chris Gammell:** Yeah.

**Dave Jones:** Jeez, you know. Yep.

**Chris Gammell:** Yeah. Yeah. And that's kind of like what Ming was talking about a couple of weeks ago too, from Zglue. I don't know if they, I don't remember if we said they did any analog stuff. I think, I guess some of the chips that they pulled in were, you know, they had sensors, but I think they, I think all the interconnect between them. So that was like the chiplets and the chiplets go down onto like a substrate and then you can talk between the different chips. Yeah. Right. But I'm not sure if that, yeah. I do like the chiplet idea though. I think that's, I think that is a very interesting idea, but again, it's, you know, it's going to be TI or ADI.

**Dave Jones:** It's niche. It's not. Yeah.

**Chris Gammell:** Well, you're going to, you're only going to have so many choices there. So, and then however many of the parts that are out in the system that are actually capable or available as chiplets as well.

**Dave Jones:** Yep.

**Chris Gammell:** It doesn't really matter for me. I don't think I've ever going to be a volume to, to be able to do that unless it gets so low that it's, you know, literally as simple as making a PCB, but I don't, I don't think we're there for a couple of years at least.

**Dave Jones:** Right. Well, who makes the analog FPGA type things? Those, um, EPAC ones, the, um, electrically programmable.

**Chris Gammell:** Analogic is sticking out of my mind, but I don't know if that's the ones. Analogic?

**Dave Jones:** No, no. It's one of the other mainstream. Oh God. I can't believe it.

**Chris Gammell:** I can't believe I can't remember. That's a healthcare company.

**Dave Jones:** Now we're frantically trying to find it in the.

**Chris Gammell:** Well, I mean, it's not really, it's not really, it's, uh, Cyprus has the PSOC. The Cyprus, yes.

**Dave Jones:** The PSOC. That's what I'm thinking. Oh yeah. Cyprus with their PSOC.

**Chris Gammell:** PSOC is kind of reconfigurable. Man, those are really expensive. Like.

**Dave Jones:** Yeah. They're not cheap, but they're kind of cool. Like, you know, but they're not. Oh no, they're very cool.

**Chris Gammell:** Yeah.

**Dave Jones:** But as is common with a lot of these, you know, modular analog things, they're not that high performance.

**Chris Gammell:** Exactly. Yeah. If you need like 16 bit, 24 bit, you're not going to probably get that in there. I think. Yeah. I think I've seen 12, 12 bit.

**Dave Jones:** And even then the specs are a bit loosey goosey. I think. Please correct. I'm sure.

**Chris Gammell:** I think that's the thing at the end of the day, I prefer to mix and match. I don't want like, like, I think that the answer for having analog, you know, in the open PDK thing, it's like, yeah, some people are going to want integrated analog. Okay, great. But yeah, I don't think that's the answer for me because I'm not making custom chips either. You know, like I'm, I'm going to be mixing and matching for as long as they're available. It's just that I, I don't like that there's fewer available now. Oh, well. I believe at this point enough, I think. Let's talk about sourcing stuff. So this was a, someone actually wrote in. Oh shoot. I forgot who wrote in. We'll get his email up here, but there's actually an email. So we were talking about like lead times from Maxim, right? Like 40 at 44 weeks. But apparently microchip sent out an email and a letter to all their customers. They're like, Hey guys, what you're doing is not cool. That's kind of how it read to me. I don't know.

**Dave Jones:** How dare you order parts from us? Right. That's not cool.

**Chris Gammell:** Right.

**Dave Jones:** Sorry. We have to explain this because that sounds absolutely ridiculous.

**Chris Gammell:** Yeah. So, oh, this is from David. So David wrote in. Thank you, David. And basically the letter says, we're getting all these orders. We don't know where they come from, but people are asking for expedited orders. And expedited always is kind of weird to me in general too. Like, so one of my buddies who's like a buyer, he's like, yeah, you know, we could do expedite. I'm like, why doesn't, it's kind of like. Why is it standard? Yeah. Well, exactly. Like, well, it's like you, you know, the, it's like, it's like sending an email with urgent on it. You know, eventually there's inflation and everything gets marked as urgent or double urgent or triple urgent or must read now, you know, like, and it's just, yeah, it becomes meaningless. And so like, that's the thing that you can do when you, you know, contact these fabs and you can try and get a hot lot or you can try and get expedited, jump the line, whatever. And so this letter saying like, Hey, we're getting this a lot right now. They don't know what it's from. And we can make conjecture on that.

**Dave Jones:** I'm sure. Well, they actually speculate what it is. Yeah. They speculate that every, all companies were shut down. Yeah. Companies were shut down all of a sudden they've come back into business because the, you know, the companies shut down due to lockdowns and now they're back in business and all of a sudden everyone wants their stuff and they have to ramp back up and bingo, they want their chips now, please. And, and basically they're saying, sorry, our normal product lead time is 16 to 20 weeks. And they're saying, can you please at least give us 12 weeks of backlog visibility? Like, please. It's like, we, we can't just bump every, you know, we can't expedite everyone's order. It's just not possible. Like if you get a PCB manufacturer, which is like a short, you know, like chips have a very long lead time, right? There's lots of process steps involved, but you know, a PCB can be turned around in like a day or, you know, hours. Right. And you, you can pay to have your design expedited it, but it literally means they put you to the front of the queue, they bump everyone else's job and then they immediately start working on your board. We, we used to do this when we were at Aldi and we would have like eight to 10 layer boards turned around in 24 hours. Right. 24. Yeah. And it'd be thousands of dollars for one, like for a prototype board, but we, you know, we, we wanted it for various reasons and yeah. And they would expedite it and they would bump everyone else's job and they would manufacture our board. And, you know, we, they would literally start like, you know, 10 minutes after you sent in the email saying, yep, we're happy to pay that expedited price. Then somebody boom, immediately starts working on it, bumps every other job, you know, and yeah. And, and you get in there, but chips, it's a bit more complicated. The thing is when you're starting from sand. Yeah. Yeah.

**Chris Gammell:** I mean, I think, I think the stuff that I used to work on in the fab, it was like, I think it was like a 30 day start to finish, you know, wafer in, wafer out kind of thing. And that's like getting, I think that was even just a test. And then you, you're a test then at 30 days. So let's call that four weeks. You're then you've got, you know, all the lead times and shipping and everything else. And then you have to ship it to another country to usually get, to get packaged up. And then there's further testing past that. And then shipping out to a distributor or shipping out to directly to your manufacturer. And it's like, yeah, I mean, six weeks is a, there's a huge process flow there. It's not to mention, like if there's, if they're ordering material, like say there was a huge surge. I mean, I always think about it kind of like traffic too. You know, like when like a traffic jam is like starting back up, there's always like the, the start, stop, start, stop just to try and like even flow. And it's like, if basically, you know, if you get to the point where you now want to start speeding, that being like a very fast lead time, well, you're stuck behind everything else. And then it all ripples through the system as well. Like if you want, even if you wanted to say you got your absolute minimum down to six weeks. Okay, great. Well, what about the wafers? You know, like if the wafers aren't in the system too and shipping to the fab, then they're, you know, it's just, you can't like conjure it out of thin air because it's, it's, you have to start somewhere. So yeah, it's, it's, uh, there's some very, very tough realities, especially when you're talking about the volumes that, you know, some people are like, well, you know, I could see on DigiKey there's, or Mauser there's, there's a, you know, 10,000 parts. It's just like, okay, what if you need a million? Yeah, exactly. You're not buying a million parts off distribution unless it's capacitors. And even then, not, not really.

**Dave Jones:** Lead times, pain in the ass.

**Chris Gammell:** Interestingly, on the, uh, on the, the subreddit page for this, Maddie, Maddie guy said, uh, same old song and dense, a variation of this letter has been on Microchip's homepage since I entered the industry. Nothing to see here.

**Dave Jones:** Oh, really? Okay. Interesting.

**Chris Gammell:** But yeah, I've never seen it before, but, uh, I'm not on the homepage of Microchip very often. No, no. Yeah. I've been used, yeah. And then DR Twist said, as Microchip customers, we don't have any kind of visibility into our own customers' short-term demand. And that's, again, that's like the traffic thing. Ah, right. Yes, of course. You know, like, as, you know, everybody gets stopped up at certain points. Yeah. Yeah, that, that whole, uh, the whole COVID thing, basically, I mean, everyone, I think the market crash really did it at the beginning. And everyone, like, clammed up. They're like, we're not spending any cash. And no, no, no, wait, we've got tons of cash. We'll spend as much as we can. And then there's nothing there because everybody shut, shut down, you know? So.

**Dave Jones:** Oh, it's nuts. The world is nuts. Economics. It's silly. Anyway. But there's, there's, like, as I said, there's nothing new here at all. I mean, this, you know, chip backlogs of people take, uh, for granted, like, you know, most people who have probably listened to this show are sort of like your more low volume type stuff. You used to be able to getting stuff X stock from DigiKey and Mouser and Element 14 and all those sort of places. Right. But when you're talking about volume production, it's an entirely different game. It really is.

**Chris Gammell:** You know, that's the first thing. So, like, whenever I have a new client and they're like, okay, we think we're going to make, I don't know, 50,000. And I, I, you know, I show them the math. I go, okay, you want 50,000 units next year. I have to put, let's say 50 LEDs on this one project. You know, it was like an LED project. Yeah. 50 LEDs times 50,000 boards. It's like, you can't get that many LEDs in many places, especially if they're special at all. So like, just so you know, there is going to be a very specific lead time. It's at least 20 weeks. So like, yep. Build that into everything you do.

**Dave Jones:** And you have to make those design decisions upfront and you have to buy those, you know, and then you're stuck with that part. It's like, no, we can't change that part now because no, we've, we've already ordered, you know, half a million parts. Yeah. Better make sure you did your math right. Yeah, exactly. So yes, because you can get caught out. Like, you know, like if you didn't do your engineering properly, if you didn't do it thorough enough, you go, oh God, no, this ship is just like, it looked great on the surface. It worked great on the prototype, but we didn't do the thorough, you know, thermal testing or whatever. And we thought, oh no, it's not the right part. No, we're going to have to get this other one. It's like, you know, you've, you've just blown, you know, half a million parts. Right. It's just, yeah, it's nuts. Engineering. It's hard. It's fun. Hardware. I don't know.

**Chris Gammell:** I had this thought the other day, like I've been like in, I've been doing a lot of CAD lately and like, like I kind of like look up and I'm like, you know, I'm kind of like in the flow and like, but like some of this stuff, man, it's, it's great. It's really great. Like learning new things too. I think I said that last time. Uh, yeah. No, I like learning. I know. Right. Yeah. Total good. Unbelievable. Some of us read books, Dave. I actually have been reading. There was a, there was an RF, you know, I do it before I fall asleep usually. And this was a bad choice for a night. Cause I was like already thinking about work stuff and then I couldn't sleep. And I was like, Oh, I'll read a book about layout. This is a great idea. No bad idea. But there's a, I think I mentioned it before. There's like an RF layout book. It was just like an Amazon book. It was from a consulting company and they were like, Oh yeah, we'll just publish a book here. Right. So it's kind of good. I've been dealing a lot with, uh, with like RF spacing and stackups and, and all that kind of stuff lately. And it's been, it's been interesting. It's, you know, a little challenging. I don't know how much, have you done that a lot or no?

**Dave Jones:** Oh, well, this is a video I'm going to edit after this actually. Um, and this comes up on the forum cause somebody on, on the forum there, they're developing, um, this little board. It's got like an image sensor. It's got an FPGA on it, like a small FP. So a low end image sensor, like, you know, 640 by 480 or whatever. And a low end FPGA is just like a quad flap. It's a, you know, a 32 pin FPGA. It's nothing. Oh yeah. That's, that's tiny. And yeah. And so they asked for a feedback on the list. So they wanted to know about layers. They first started asking about layer stackup and stuff like that. Oh, which stackup? Cause I'm using a four layer board. Cause I've got to route out this little pain in the ass BGA, uh, image sensor package. So I need the trace. And that's an interesting trade-off. Normally you could have, uh, laid out this board on a two layer board, but because the pin pitch and the image sensor BGA was designed for like use in mobile phones and by the looks of it, this sensor, the pin pitch is so small that you can't route out. The traces have to be 5,000 or less to route these things out. Right. So the two layer process manufacturing tolerances didn't allow for traces that small that he wanted to use, uh, the particular service. So he was sort of like forced into the four layer, uh, service so that he could get better tolerance on the, uh, track and, and space. So he's got the luxury of a four layer board now, and he wanted to know how to stack it up and stuff anyway.

**Chris Gammell:** Yeah, but he's, so I'm guessing he's using JLC, right? I can tell that. Yeah. Yeah. He's using JLC. Yeah. Cause it's five on two layer and 3.5 on four layer. Okay. Right. Okay. Yep.

**Dave Jones:** So he, yeah. So he's forced in the, so, you know, you've got luxury of the four labels.

**Chris Gammell:** You can't do the stack up then. You're not talking, you're talking about the layer stack or the actual. I'm talking about the layer stack.

**Dave Jones:** Yep. Yeah. No, he just wanted to know like which one should be ground, which one should be signal, which one should be power and stuff like that. So I started off asking about that and then got into, you know, talking about bypass capacitors and then somebody on the forum who's like a really high end RF designer, you know, jumped in and like sort of went to town about this is how you have to, you know, you've got to have a bypass capacitor for every via that you have on your board because, you know, so he was thinking in RF terms, you know, which is, which is all valid, you know, really valid, great advice for RF, RF design, but he's got that RF thinking. So, you know, so that's how it came. So that's how he was answering the question from the RF perspective of I'm going, hang on a sec. This is a low end FPGA, like bypass is not going to matter a rat's. You could have one bypass cap for this whole thing. It's not going to matter a rat's ass. You know, it's like, because it's so low end.

**Chris Gammell:** And you said like RF, you know, like RF thinking or like high, you know, digital speed thinking or analog. All of these are like approximations, right? These are all like ever abstractions rather of like these design rules that are like kind of internalized. And yeah, I mean, when you try and apply one to the other, it doesn't always make sense from a cost perspective or a density perspective. But then again, like you look at like, I just bought an RF amplifier the other day and I was talking to someone on Twitter who had cracked theirs open. And like, it's, it's really simple inside because it kind of has to be, you know, like it's like, and like a lot of RF circuits are, you know, not, not simple overall. Like they're very complex, I think. But you know, in terms of like the density you can have and just the design that, you know, how you think about the design around it, that also drives some of these design rules that you might, you know, not design rules. That's a bad, probably a bad disambiguation of the term, but like these kind of design methodologies around it because you might go and optimize for something that's not usually really dense. And now you take it to a really dense process, like, like a four layer BGA type thing. And it's like, oh, okay, well this isn't going to work now.

**Dave Jones:** Right.

**Speaker ?:** Yeah.

**Dave Jones:** And it's interesting that, yeah, just the, you can actually over-engineer things like, or you can go into all the detailed engineering for bypass capacities and everything else when you don't need to, it's like, so, and when it comes to PCB layout, I guess there's no such thing as over-engineering a PCB layout. Cause it's, it's just a little bit of time. Like there's nothing, like it's not adding really any extra costs.

**Chris Gammell:** You don't pay per ounce of copper.

**Dave Jones:** Yeah. Right. Unless you make everything thicker.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. So if, you know, if you like do all your ground planes and you do massive via stitching and all sorts of other, uh, you know, techniques in your, you know, you might do star grounding when you don't need to, you know, and all that sort of, uh, jazz it's, you know, so there's nothing wrong with using, you know, good engineering rules of thumb on PCB layouts when you don't need to, cause there's no real, you know, so you can over-engineer a PCB and it doesn't cost you much, but when you over-engineer like bypass capacitors, they're expensive. You know, if you get like your, you know, your one mic and your 10 mic bypass capacitors, cause you can't put like, you know, a hundred of those on a board. Jeez. Oh, sure. You, you, you watch your bomb cost. Soar. Right. Those little, um, especially the smaller they get, the more expensive.

**Chris Gammell:** I need a 10 microfarad C zero G. Yeah. $10,000, sir.

**Dave Jones:** Can you even get a 10 microfarad COG? I don't think you can. No. Back when I was doing COG work, like I think 10 nanofarads was enormous.

**Chris Gammell:** Yeah.

**Dave Jones:** 10, like it was like, we were paying like $10 per capacitor or something. And it's like, and there's only one manufacturer in the world that does it. Like it was, you know.

**Chris Gammell:** Why would you, you need it for the tolerance or something or what?

**Dave Jones:** No, it was for the, uh, analog performance. It was for the, cause these were AC coupling capacitors and sampling capacitors in a 24, in a ultra high end 24 bit analog to digital converter. Right.

**Chris Gammell:** But for super slow signals. So you need a high capacity.

**Dave Jones:** You need high linearity. You need, you know, everything else. You can't have it, you know, so yeah, you, you, you know, it was nothing to pay $10 for

**Chris Gammell:** a capacitor. You weren't using, we're using the capacitor, those C0G as decoupling or are you using those in, you said. Oh no, no, no, no, no.

**Dave Jones:** These are in the signal path. No, these are sampling capacitors for you, you know, for your converters and they're, you know, coupling capacitors. And, you know, coupling, not, not decoupling. Right. As in there. Right. So, yeah. And yeah. And so the quality, like, yeah, sampling capacitors are, for example, really critical that you have a very low drift, you know, ultra stable cap as your sampling capacitor. So.

**Chris Gammell:** Yeah. Yeah. If it changes halfway through a cycle, you, you start to lose frequency information, right?

**Dave Jones:** Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** So, well, yes, exactly. And, and then non, non-linear with temperature and voltage and all sorts of horrible, you know, things which you don't care about for a bypass capacitor, but when you're, but when you're actually processing a signal, especially at 24 bits, it's a real big deal. And that's why if, if you open up like a simple multimeter, right. For example, if there's like a sampling capacitor, cause it's got dual slope integration. So there'll, you know, often be a sampling capacitor in there. They will have even like a special through hole cap. They will have like everything else is service mount on there. And they'll have the one through hole part, which is a poly put the kettle on, you know, type material. Right. Because that's, that's your sampling capacitor. It's, it's actually critical. It has to be a proper type. You can't just whack in a bloody, you know, a Y5U ceramic, you know, God, God.

**Chris Gammell:** I found this on the carpet in the engineering lab.

**Dave Jones:** Exactly. Whack that in. And oh God. Yeah. Anyway. Yes. Special capacitors. Oh goodness. There's a whole art and science there.

**Chris Gammell:** So I thought you were going to be talking about the actual stack up of the board. We talked about that. Oh yeah. Sorry. Yeah.

**Dave Jones:** I got sidetracked on the board. Yes. Yes. We were talking about the stack up of the board and things like that and how, you know, look, the signal layers are going to go on top and bottom. You're going to put your power grounds in the middle. Most SMD layouts, the Holy grail of SMD layout is to get all your signal traces on the top layer. Right. And big, big, big components are on the top. You lay it out as if it's a single-sided board. Right. It's almost going like back 40 years old school where, you know, everything was single-sided. None of this double-sided rubbish. Right. So SMD designs, you think when you're laying it out, you need to be in the mindset, right, this is a single-sided layout. So I want all of my, you do as many traces as you can on the top layer. And then when, and then you route your power traces and things later, because you can't go running power traces along the top layer, because that's where you want to run your signal wires, you know? So that's what this design did. It was like running one power trace from one side of the board to the other on the top layer. And it's like, oh, then you've got no room to route your signal traces. So it was dropping like 10 wires down for all the signal traces just to sacrifice. So you sacrifice 10 signal traces for one power trace. It's like backwards. So anyway, it's hard to talk about. You have to visualize. Well, you're going to make a video about it. I'm going to make a video about it. So yeah, it's just fascinating stuff. It was interesting.

**Chris Gammell:** So I have two things about, so I'm using JLC for the board I'm doing, Contextual Electronics. Yep. One thing that's been really interesting about it is looking at the controlled impedance calculator that I don't, I can't get any other calculator to match what their calculator and their actual like board stack up is. Oh, really? Yeah. And so what I'm guessing is that they have some empirical values that they just plugged in there?

**Dave Jones:** Yeah, probably. Yes, that's likely, very likely.

**Chris Gammell:** And given that, it's probably a good idea to just follow what they say and then ask them why it didn't work. Yeah. Yeah. But it's still kind of like, it's, you know, I don't really like that. I like to rather have it spec'd out. And yeah, so still going back and forth on that.

**Dave Jones:** Yep.

**Chris Gammell:** I also made the choice about the 3.5 millimeter thing. And what I've been trying to do is I'm using a NRF 52. 3.5 millimeter? 3.5 millimeter. Sorry. 3.5 mil. Thank you. Mil. Thou. Or thou. Yeah. 0.889 millimeter trace in space. Oh, come on.

**Dave Jones:** What? Give it to me in Imperial. Track and space is always Imperial.

**Chris Gammell:** 3.5 mil or thou. Yeah.

**Dave Jones:** Oh, so it's 2.5.

**Chris Gammell:** 3.5. 3.5. Sorry. Space trace.

**Dave Jones:** Space trace. Okay.

**Chris Gammell:** Yeah. And so this part that I'm using, it's got this really ugly, like it's called an AQFN, but what it is is like a dual row, like tiny BGA with a huge thermal pad in the middle. And the part is great, but like to escape that, like basically they show, okay, you either got to do like blind and buried vias. And that's like the suggested layout is. And that's what I've done in the past. But that basically takes the board costs up a ton. And well, someone pointed me to Luke Valenti's post for tiny FPGA. Have you seen those boards before?

**Dave Jones:** I've, I've heard about them.

**Chris Gammell:** Heard about them. Okay. Yeah. So he does like super fine pitch stuff and I'll, I'll share a link to it, but it's a, he basically, he bastardizes the outside pins and then he makes them pill shaped and he did a bunch of testing on it. But basically because of the, because of the surface tension of the BGA, he's able to basically neck down the outer pins to this pill shape and then escape using a larger space trace than he would have otherwise. And he tested it on multiple boards.

**Dave Jones:** And it worked.

**Chris Gammell:** Yeah. I mean like I, it's fine, but like.

**Dave Jones:** So, so, so he's got the circular pads on the inner ring and then the outer ring, he necks, he necks them down.

**Chris Gammell:** So he's doing, he's actually doing a BGA. So it's more, it's multiple rows. I think it's a six by six. Oh, okay.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Yep. But, and the, but that is the outer row is the important one. Yeah.

**Dave Jones:** But you don't gain any actual space by making them elongated. Cause like a certain, a BGA pad is circular. So how do you neck it?

**Chris Gammell:** Well, no, no, no. So he took it, he basically said, Hey, here's our, you know, here's the surface area of the original circle. And then he made the pill shape to be an equivalent amount, assuming that the, you know, the surface tension of, or sorry, the, the ball size will stretch itself out. Okay. So it's not, it's not more overall space, not overall, or surface tension or surface, surface area rather. Yeah. Right. Gotcha. But it's just, it's just a different shape then. And then you can escape through those, those pins.

**Dave Jones:** So the elongated pad, the neck down pad is actually a smaller width than the original circular pad.

**Chris Gammell:** Smaller. Yeah, that's right. Yep. Yep. That's right.

**Dave Jones:** It has to be. Yeah. Yeah. It has to be. So you, Oh yeah. Okay. Well, you, well, yeah. Everyone's like starting to twitch. Now, anyone who knows anything about this sort of stuff is really starting to.

**Chris Gammell:** Well, like I said, he tested it. And so it's, it's interesting. I don't know if he went for that. I think it was just for a prototype. And so anyways, I was trying this just for, for my prototypes as well. And, you know, just because like thinking about. Has he x-rayed it? He, he didn't x-ray it, but he did because it's the outer row. He can tell, you know, he shows, he shows photos. And it's like a half. Oh, okay.

**Dave Jones:** Cause you can see the outer ones. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Right.

**Chris Gammell:** Yeah. And so mine is much, much like his is, is, is pretty extreme. Like it really is. It like goes from like, like circle to pill. Mine is like, goes from circle to oval. And so I can just basically a three mil space trace could get out, but a 3.5 couldn't. And I was like, well, it makes sense. And in order to be able to like iterate on boards, it makes sense cost wise to be able to do that. And so it was literally a $400 difference in terms of boards to be able to go from blind and buried to this slightly modified outer. And that's like the smallest thing. And so I was like, all right, well, it makes sense. Yeah.

**Dave Jones:** Yeah. Oh no. If you can save a huge amount of costs. Oh, once you go to blind buried for years, although it's, you know, it's still reasonable costs.

**Chris Gammell:** I love doing them. Like, I think they are like, there's just, it makes everything easier. Yeah. But yeah, it's, it's, it was interesting hack and yeah, we'll see how it turns out for mine.

**Dave Jones:** Well, that's, this is the art of engineering, right? Especially art of PCB engineering is like lowering your cost. That's one of the arts. And one of the ways you can do that is by changing your design somewhat, your layout somewhat to actually, and, or your design to use a different PCB process to end assembly process technology. So you can save cost on the bare PCB and you can save cost on your assembly as well, depending on which parts you choose. Like, like, like, like, like for example, simply choosing 0402s for everything. Bingo. Technically you're gone up in assembly cost because you've got to use a higher tolerance, a better tolerance, uh, assembly machine to do 0402s, especially in high volume and high quantity and, and, you know, things like that, because you'll have potentially a higher failure rate.

**Chris Gammell:** Yeah. I'd say it's part for the course though, these days when you, I'd say like maybe moving down into the 0201, 0105. Yeah.

**Dave Jones:** Yeah. But technically you can, you know, if you stick to 0805 or 0603s or something, you will have a, you can place them yourself. Yeah. You can place them yourself. You've got older, cheaper pick and place machines.

**Chris Gammell:** Whereas, you know, it's like a filtering mechanism of like, okay, like you're on like a parametric search and you say, okay, I'm going to have all 805, everything, the world's your oyster. You can use any machine, but I'm going to use 0402. It's now down to 65% of all the machines and 0201, 30% of the machines and on and down from there.

**Dave Jones:** And that's assembly. And once again, on bare board, bare PCB cost, you can save costs by, if you don't, if you don't need that six layer board, if you can get away, if you can escape your BGA on four layers, you do it because it's going to be cheaper. And if you can escape it using, as you said, a higher process, sorry, a lower quality process technology, like a 4,000, 4,000 instead of 3,000, 3,000 track space, bingo, you've instantly have available cheaper manufacturing process technology. So your bare board should in theory be, well, you could potentially source it cheaper than you did if you said, oh, I'm going to use 2,000 traces because I'm a real designer.

**Chris Gammell:** Right. Well, and I think the thing that popped out to me, so like I said, I've done a design with this chip on it before, and it was like a 100mm by 100mm board, 100mm by 100mm square board. Right? Yep. And I had to pay for all of that space, but the only chip that needed this was that tiny little one chip. And it's like, so everything else is basically carrying the cost of this one chip. And you could say, well, you could go to a, you know, and really this is why modules are a good idea sometimes too, is that the module, yeah, it might have, you know, super tight tolerance, you know, and then it's also pre-certified for FTC. There's other reasons to do it, but then you're paying that cost and you're carrying that across other things. And so, yeah, I don't know. I think it is a balance point. That is the engineering piece, I suppose.

**Dave Jones:** Oh, yes. If you choose one tiny little pissant BGA, right? Like as in tiny, like as in, you know, tiny ball pitch and stuff like that, and everything else on your design is huge, and you've got a big, you know, 300mm by 300mm board, like a giant board like this, right? That's going to cost a lot of money, right? Right, yeah. But that's not uncommon. If you're making industrial stuff, right? Like a three, a big, a giant board's a, you know, a common, common as mud. Yeah.

**Chris Gammell:** Yeah. I'm staring at one right now on my bench.

**Dave Jones:** And then if you choose one component that requires, you know, three thousand, three thousand tracers, bingo, you're screwed, you know?

**Chris Gammell:** It's the lowest common denominator pretty much. Yeah. Right.

**Dave Jones:** You have to use that process technology for your entire giant board. And that board is going to be $100 a board instead of five bucks a board.

**Chris Gammell:** Yeah.

**Dave Jones:** Right?

**Chris Gammell:** Yeah. It's almost like it would make more sense. If you really need that BGA, it would almost make sense to make a plug-in module yourself.

**Dave Jones:** Make a module yourself. Make a little door-to-board. Yeah. It's cheaper to get like a tiny little one inch by one inch board made, put the BGA on there and have pastellated edges or have a, you know, board-to-board interconnect. It'd be cheaper to buy the board-to-board interconnectors and put them on your board than it is to pay for a giant board.

**Chris Gammell:** High density if you want.

**Dave Jones:** Get, you know, top quality Samtech ones or something, you know? And even if you pay a couple of bucks per connector, it's still cheaper than paying for that one giant $100 bare PCB.

**Chris Gammell:** Yeah. Yeah. Totally. You know? Totally.

**Dave Jones:** Yeah. And you actually see that. When I do teardowns of various test instruments, scopes and, you know, keysight scopes and other scopes, you see that. The high-end FPGAs and, you know, system-on-chip processors that they use, right, they always come in like these, you know, high pin count PGA packages, right? So they'll actually put those on the door-to-board and they put them on a door-to-board so then they can transfer the cost of the piece. So, yeah, they only have to pay for the cost of that small board, that high-density small board. They only need that eight-layer board for that part of the design. The rest of the scope is just, you know, four or six layers or something.

**Chris Gammell:** Right. Well, and just like the RF section too, you wouldn't, I mean, you could make a small microcontroller go on to Rogers PCB material, but you would be an idiot, you know, like, you could do it, but don't, don't do that. That's a bad idea. Don't do it. Don't do it. Your boss will get very mad. Yes. And so, yeah, you do different boards, you do interconnects and everything else. And yeah. Yep. Can you imagine? Can you imagine being like, yes, this is just the finest Rogers material. And there's the ATMEGA 328P. Yeah. Yeah. Right.

**Dave Jones:** Yep. Yeah. So, yeah, that's the, that's the art of PCB engineering. That's the art of, you know, and it's really fascinating stuff. Yeah. And I've done many videos on that. I'm sure. Over the years. And it's very important. He doesn't even remember anymore, folks. Oh, I don't remember.

**Chris Gammell:** Come on. Come on. Yeah.

**Dave Jones:** Do you remember every video you've done? I bet you, you don't.

**Chris Gammell:** I do not. No.

**Dave Jones:** No, exactly.

**Chris Gammell:** Yep. I did share the link. If you wanted to see the, what it looks like. I shared the link in our, our chat program here.

**Dave Jones:** Oh yes. There it is. Yeah. Let's have a look. Let's have a look. Is this public or is this? Oh no. It's public. Yeah. It's a Hackaday IO post. Yeah. Yeah. Right. Oh yes. There's a tiny little BGA. Oh, isn't that, isn't that hideous?

**Chris Gammell:** Yeah. Yeah. Oh, so that's actually what I wanted to bring up too. So this is actually, so I was, I was shopping for.

**Dave Jones:** Oh wow.

**Chris Gammell:** I was shopping for power converters the other day. You know, I was at Tosche station going to get some power converters.

**Dave Jones:** Power converters. Yeah. Oh geez. The, the soda mask alignment on that BGA is terrible. It's real bad.

**Chris Gammell:** Yeah. It's really bad. Right. And so like that, well, that's another good point too. It's like, if you're going with a low cost house, you might have other effects that like, okay, yeah, sure. You're, you know, they're going to test your copper and that that's fine. But if the alignment's bad, then you might also be in bad, bad shape of the soda mask rather. So anyways, I was shopping for a DC to DC converters and it, it's getting to the point where like, I, I was looking at like the newest fanciest chips and I was like, nope, that's BGA is too small. BGA is too small. And you know, and like, of course you can filter for all this stuff, but you are, you're basically, you know, you're any, any of the newest chips. It's like, why wouldn't they do that? And then like Tim and Ming had both been talking about in the past two episodes, the past two guest episodes, like everyone, everything's driving towards CSP anyways. And so.

**Dave Jones:** CSP is chip, chip scale package for those. That's right.

**Chris Gammell:** Yeah. Thank you. Yeah. And so, um, yeah, so upcoming contextual electronics course is actually going to be about doing your first CSP in order to, you know, because like, otherwise you start to lock yourself out of certain technologies and certain chips that are, everything that's being developed for a, you know, a cell phone that's going to trickle into the market. Yeah. It's all chip scale. If you know, and it's, it's tiny, you know, it's like.

**Dave Jones:** And, and for those who don't know why it's called chip scale package, just as a side thing, it's because the, the chip, they're talking about the bare die. So the package is essentially no bigger than the bare die. And that's why they have the BGA because the bumps on the bottom match up to the, you know, the.

**Chris Gammell:** Yeah. Usually that's the top level of the, uh, the metalization and then the, yeah, they just literally flip it over.

**Dave Jones:** They actually flip the chip over and then they attach the balls to that and that's the ball, you know? So there's no lead out. Like there's, there's no lead frame. It's called in, in your traditional, uh, you know, SO type packages and dip packages and stuff like that. Uh, whereas, uh, you know, they have the, then they ultrasonically put in the little bond wires and things like that. There's none of that bond wire rubbish. This is like balls directly on pads on, on the actual wafer itself. So that's why they're tiny. That's why the pin pictures are tiny because the silicon's tiny.

**Chris Gammell:** That's right. Yeah. It's evil. That's great, man. No, it's evil. Invest, invest in your micro, your, your microscopes, you know, like, I think it's just, honestly, it's just, it's just the reality of the world we're living in now, you know, like, and even like I look at QFNs and I'm like, that's not the size of the silicon in there. You know, that there's probably just, it's just a little landing pad with the CSP in there or something like that. Anyways, they're making, they're making QFNs, even QFNs, which, you know, a lot of people hate. It's like, they're making that for schlubs like me, you know, they're not making, they're not making, uh, you know, dip package parts for the, out of the goodness of their heart. They're making them because they've been selling them, you know, that's a consistent revenue stream and, you know, some fresh faced engineers, you know, out there making, you know, every time they cost down the silicon, it gets, you know, half as big and they got to just figure out a new way to hook it up to the dip packages that everybody wants to buy. So, sorry. Isn't this a great industry? Come on.

**Dave Jones:** Can we talk about the automobile manufacturing industry?

**Chris Gammell:** Oh yeah. We, yeah, this is good, uh, callback from the beginning. So this is the EV, Dave putting the EV and EEV blog. Here we go.

**Dave Jones:** And, uh, this is, yeah, this is great. Munro and associates. They're like a analysis. I don't even know what they're an automotive analysis company. They do teardowns of cars, right? That's one of the things.

**Chris Gammell:** It's basically like, uh, yeah, it's like the, what's, what's the repair company that does, uh, like I tear down. It's like, I tear down, but for really big things.

**Dave Jones:** Right. Anyway, their, their website is lean, leandesign.com. So they're into like, you know, optimizing manufacturing and how things are manufactured and stuff like that. So anyway, they do teardowns of cars. So they get new cars on the market and they tear them down to every last component, every last bolt. And they not only photograph and document all these parts, but they figure out all of the manufacturing costs that, and, and the manufacturing yields as well. So they figure out this for every, and itemize it for every single part in this car. So they go, okay, this screw here, this module assembly has 20 screws and they, and they cost X amount each. And these moldings, they analyze the injection moldings.

**Chris Gammell:** I have a very good example here. Page, uh, 319, Dave.

**Dave Jones:** Page 319, obviously. Page 319.

**Chris Gammell:** What do you, what do you see on there? So this is.

**Dave Jones:** Assemble high voltage module cover. What?

**Chris Gammell:** Yeah. See what, see what the actual part is though?

**Dave Jones:** It's a cable harness. Oh, it's a zip tie. It's a zip tie. Yes. They've analyzed this zip tie. This is a great example. Yeah. Yeah. You're right. So, so they've analyzed this zip tie and they go, look with an, they've calculated with a 99.74%, they will get this zip tie right in the assembly process first time.

**Chris Gammell:** That's amazing. Right. And it takes 51 seconds to put it on there.

**Dave Jones:** 51 seconds to process that and put it on there. And it's, it costs three cents per, uh, for, for the material, for the cable tie, but the process, the supplier process costs, they've broken, broken this all down 77 cents for the supplier process costs. That probably includes delivery and everything, you know, the whole thing and the quality burden is they can define all these things.

**Chris Gammell:** This has got to be the most nightmare of a spreadsheet ever. It's probably like you open up the spreadsheet and then 25 minutes later you come back and maybe your computer has stopped choking on it, you know?

**Dave Jones:** Yep. So they've come to the final conclusion. They've added it up that it costs a dollar and two cents to install two cable ties.

**Chris Gammell:** Which is crazy. Right.

**Dave Jones:** It's right. But Hey, so, so if you can, if you can work that part, so if you can, you know, work your, if your mechanical CAD designer can work their magic so that they can integrate the cable tie with that particular plastic mold in somehow, you know, like it doesn't need cable ties or something like that. Yeah. It's got some sort of windy thing that you put it in or something. You can save a dollar in your car for your component costs right there. And this car has like 22,000 parts or something on it. Right. And they analyze every single one of them. And the, the report we're looking at, right. Is 2,627 pages long.

**Chris Gammell:** And it's only.

**Dave Jones:** And it's only for the battery pack in, in, in this BMW i3. Right. This BMW i3 car. Right. And there's 10 different, there's 10 different PDFs analyzing different subsections of the car. Right. And.

**Chris Gammell:** How much, how much does it cost to take this home today, Dave?

**Dave Jones:** $80,000 to buy this report. But I happen to have paid $10 for it because it's an old report they did in 2015 when the BMW i3 was new. Right. So they, they taught, so they bought one of these cars and they tore it down and it took them probably a year to analyze six months to analyze this thing and produce the reports. Like how do you produce a report that's 2000 pages long and do that 10 times? Like, oh my God. Anyway.

**Chris Gammell:** I mean, it's gotta be like a, like a forensic style thing, right. Where they're like labeling everything and like putting, you know, logging in the system.

**Dave Jones:** And they must have custom software packages that they put all this information in. And the report spits out.

**Chris Gammell:** So to do it, you know, like to, to actually get this done, they, they can't manually do

**Dave Jones:** it. They must have automated processes to do the documentation anyway. So yeah. So you used to be able to buy this report for $80,000 and obviously they only sold like two, two dozen reports or something. Right. Because, you know, I sell it to other car manufacturers and sell it to, you know. Yeah. Yes.

**Chris Gammell:** Well, he's probably sold to the main, to the, uh, to the suppliers, right. All of the, all the OEMs that are going to here. Cause then if you have, if you basically get this, you know, two months after, and then you want to start selling like a, you know, a replacement part, you know? Okay, great. Yeah. It's a dollar for the zip tie. You better beat that one cent price tag or else you don't even bother, you know?

**Dave Jones:** So yeah. So anyway, people buy these reports, you know, $80,000 and apparently they spent over a million dollars doing this teardown. Yeah. You know, to actually produce the, this actual report million bucks. So they, hopefully they got the money back. Anyway.

**Chris Gammell:** Are we going to have a, are we going to have a link for people to buy this or no?

**Dave Jones:** Yes, we will have a link for people to buy this. I'll send it to you.

**Chris Gammell:** So people are, yeah. Okay.

**Dave Jones:** Yeah. It's great. It's worth the 10 bucks just so that you can see what's involved in manufacturing. If you're interested in, at, in anything to do with manufacturing process technology and costing, this is just a, this will be an eye opener. Really will. Anyway, they decided to release it. They said, oh, we've got 10 different reports for this car. We'll charge a buck. Um, you know, we'll charge a dollar each. So you can buy all 10 reports for this, can tear down for this car for 10 bucks. And I, I, I ponied up the 10 bucks and I've got. Yeah.

**Chris Gammell:** I think that's totally worth it. I mean, it's cool.

**Dave Jones:** It is so worth it. I don't even like, I, I couldn't even produce a video on this. It's so like, as I said, like it's 2,600 pages just for the battery.

**Chris Gammell:** 400 hours of video. And Dave is just exhausted at the end. I haven't slept in weeks.

**Dave Jones:** And every part, even down to the cable ties is photographed, itemized and cost analyzed. I mean, holy shit. It's great.

**Chris Gammell:** This is incredible. The other thing that's interesting, like just looking at the, so I've only seen the battery stack one that Dave just shared with me, but like even seeing that, like, okay. So someone walks up to you on the street and they're like, I need you to design a battery pack tomorrow. I don't know. Where do you start? You know, like, like what's in there. And this is, you know, this is five years old, right? So they're already however many years down the line and they're working on the newest thing and, you know, increasing capacity, whatever. But okay, this is a great resource for build, you know, say you're, say you're building a robot for, you know, a university course or something, and you want to make sure it's really secure. Take some design ideas from here. And it's like, this is, this is a great kind of, these, these kinds of things are great resources just for filling up your mental library of like, oh, well maybe, you know, maybe we could stack vertically instead of horizontally or whatever, whatever comes out of it, you know? Right. So yeah. It's a required reading. This should be part of college courses.

**Dave Jones:** This is just insane. And then they analyze like the, the die cast plates and things like that. So you can figure out, you know, look, this, this die cast, the entire, if you're interested, the entire bottom plate for the whole battery pack of the big aluminum die cast plate, it's massive, right? It costs $62 for the, this giant machine, you know, no, it's not die.

**Chris Gammell:** And they have a material cost and they have.

**Dave Jones:** Yeah.

**Chris Gammell:** Material cost and something, something forged or stamped or whatever, you know, mechanical stuff.

**Dave Jones:** It's just, it's just ridiculous. Yeah. I, I, I just blow it away. You'll be blown away too. See, if you're not blown away by this, get out of the industry because bloody interesting stuff.

**Chris Gammell:** And this is what, you know, we are the arbiters of what's interesting. Yeah. You will listen to us.

**Dave Jones:** Damn right. You will find this interesting or you will leave. You will look at zip ties and you will think, Oh, zip ties, a dollar. Oh man. It's just, yeah. It's mind blowing stuff. Anyway, definitely worth the 10 bucks or maybe I'll do a video on it and you'll get a snippet of what's in there. But yeah, definitely.

**Chris Gammell:** Cool. I think you should. I think, like I said, to just to showcase to people that there's, so are there others out there? Like, how did you find out about this? Did you?

**Dave Jones:** Somebody tweeted it or sent me a message. Somebody sent me an email or something.

**Chris Gammell:** I would just be interesting if there's like, so like if there was other teardowns like this, you know, like these kind of like crazy teardowns, I think it has to be high dollar materials. Oh, it's gotta be. Yeah. High dollar and high volume, you know, in order to someone spending time on this. But if there was like, you know, say there was like a ventilator teardown like that, you know, there obviously a lot of ventilator stuff or, but like, you know, a full, a full workup

**Speaker ?:** of like a.

**Dave Jones:** The market's just not big enough for that. I think you'll only find this in automotive. You wouldn't even find it in aircraft.

**Chris Gammell:** Maybe like cell phones, I guess you could kind of do that. Maybe. Yeah. Yeah. Yeah. There's so much stuff there. This is very mechanical. It seems as well. You know, there's a lot of. Oh yeah. And people do like, so I was watching a teardown video of like an iPhone, like a recent iPhone and it's like, yeah, it's interesting. But they're like, there's the, uh, the whole, like, uh, the what's it called when it has like the vibration motor in it. They, they have like a special name for that subsystem. And it's like, they were tearing it down. They're showing it's like, but there's just like blobs of silicon in there and that. Okay. You know, it does some kind of control. There's probably a microcontroller in there. Okay, great. You know, like, that's not going to tell me as much as like the stack up of like batteries and all the mechanical stuff that's in this one.

**Dave Jones:** All right. So anyway, um, yes, I know for a fact that there are companies who specialize in forensic teardowns of, uh, phones. There are companies that actually do that. And, uh, yeah. And, and they, you can, you can buy their reports. They will tear down the latest iPhone and they'll itemize the cost.

**Chris Gammell:** I've met. I'm looking for the bargain barrel. I want the bargain barrel report prices. I'll pay for it like you did, you know, but.

**Dave Jones:** No, well, you'll get those on like iFixits when they do a teardown. And I think they kind of might do a cost estimate of, you know, like the basic chips used in there at least, you know, but no, if you want the real cost, you have to factor in all the assembly and transportation and other warehousing, you know, all the costs associated with actually manufacturing, vertically integrated manufacturing and entire phone. You know?

**Chris Gammell:** I think the other thing that's interesting about this is like, like seeing in the mechanical realm too, so much of it is custom. Right. And, you know, there's obviously, you know, chip, phone manufacturers are moving into their own chip space, right? Apple's doing their own chips and the other Samsung does their own chips. And like, that's not out of the realm of possibility, but it's not like they're just, you know, turning around and spinning up a, you know, a stamping plant that, or, you know, they cut a new die to do a new chip. They have to actually go all the way through the process. And in the mechanical realm, it's like, there is a lot of custom stuff, especially in the plastics and, you know, like, because there's just more tools for doing that sort of thing.

**Dave Jones:** Prepare to have your mind blown. I'm going to give you the executive summary of what it takes to manufacture an electric car battery pack. Here you go. Page 34, Chris, for those playing live for you.

**Chris Gammell:** Let's fire 15% of the workforce. All right. I'm in the right mindset now. I feel like an executive.

**Dave Jones:** Okay.

**Chris Gammell:** All right.

**Dave Jones:** Here we go. Just the battery pack in the BMW i3, right? It's the big, you know, a big die cast, you know, alloy assembly that contains all the cells and, you know, everything else.

**Chris Gammell:** Goes on the bottom of the car, low center of gravity.

**Dave Jones:** Number of parts. Guess, Chris, how many parts are inside? I'm not looking. I'd say 1200. Off by an order of magnitude.

**Chris Gammell:** 12,000?

**Dave Jones:** 12,295 parts.

**Chris Gammell:** Oh, wow. Okay. This is how many. Or we should say we got the order of magnitude thing last. Everybody loved to correct us on that one. We got it wrong. Okay. We got it. Yeah. Thank you. Yeah. Like the log scale. It's a log scale.

**Dave Jones:** Although, no, I am. No. Yeah. No, no, no, no. I'm still going to stand firm on that.

**Chris Gammell:** Okay. Fine. Whatever. But a lot of people. No, I'm standing firm on the log thing.

**Dave Jones:** Five is half an order of magnitude. Damn it. I don't give a shit about the log thing. Okay. No, don't care. Don't care.

**Chris Gammell:** Great.

**Dave Jones:** No, no. In the true spirit of order of magnitude, it's an estimation.

**Chris Gammell:** I feel, you know, I feel like this is what it is.

**Dave Jones:** It's about the feels. Feels over reels, you know?

**Chris Gammell:** Feels over reels. Yeah.

**Dave Jones:** That's it. That's the spirit of order of magnitude. Anyway. I shouldn't have brought it up. I'm going to make you guess on each one of those. How many fasteners?

**Chris Gammell:** Of the 12,000?

**Dave Jones:** No. How many fasteners, you know, to like cable ties and screws and things?

**Chris Gammell:** 4,500.

**Dave Jones:** No, no. Now you're way overestimating. 830 fasteners.

**Chris Gammell:** Okay.

**Dave Jones:** Okay. I don't know.

**Chris Gammell:** What else is in a battery pack? I guess like cells and like plastic things.

**Dave Jones:** Okay. There are 12,200 parts. How many unique parts?

**Chris Gammell:** Oh, that's interesting.

**Dave Jones:** Yeah.

**Chris Gammell:** I'd say, how much duplication is there? I'd say probably 8,000 uniques. No, 6,000 uniques.

**Dave Jones:** 500.

**Chris Gammell:** 500 uniques.

**Dave Jones:** 500 uniques. So what the hell are they? They're reusing a lot of the same screw, I guess. Okay. Yeah. Yeah.

**Chris Gammell:** Okay. So then that's a little bit more doable then. So of 500 unique parts, then. 500.

**Dave Jones:** It's more doable. Yeah.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** Heck, I've made PCBs with, you know, a couple of hundred unique parts.

**Chris Gammell:** Yeah. Yeah. Right.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. You get into resistor values and all that other stuff.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. It's, you know, so.

**Chris Gammell:** Boy, imagine like all the drawings they have to maintain for all that. Like, oh, talk about PLM. PLM nightmare. Yuck.

**Dave Jones:** Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Explain that these acronyms.

**Chris Gammell:** Product life cycle management. So that's like, you've got screw one, two, three, four, five, and that is now obsolete or the manufacturer's not making it anymore. We didn't need to insert screw one, two, three, four, six. And then you basically rev the drawing and then it just rolls all the way up the assembly. Yeah. Yeah. Oh my God.

**Dave Jones:** You definitely want to be one of those engineers. Yeah. Who would do that?

**Chris Gammell:** Yeah.

**Dave Jones:** I've, I've spent a week of my life sourcing a screw. I believe it. Yeah. Yeah. Yeah.

**Chris Gammell:** I mean, I mean, if you get it wrong, it's really, everything goes bad. Oh yeah. Everything goes, it's up. Yeah. That's the real bad.

**Dave Jones:** Okay. Okay. Chris, how many, how many process steps? Like how many actual process steps to assemble this entire battery pack?

**Chris Gammell:** 500.

**Dave Jones:** Order of magnitude again. No, two orders of magnitude.

**Chris Gammell:** Wrong direction. Yeah. Which way? Up or down? Up. Really? 50,000 steps?

**Dave Jones:** 59,000 steps. How is that possible?

**Chris Gammell:** Is it like process step would be like, like one screw of like a torque wrench is like. Yeah. It's like one step.

**Dave Jones:** Yeah.

**Chris Gammell:** Oh, so it's like every standard operating procedure is multiplied times, however many.

**Dave Jones:** Is multi. Yeah. So each, you know, just, just putting on that cable tie might take five steps, you know?

**Chris Gammell:** Yeah. Right.

**Dave Jones:** Like, you know, you've got to get the cable tie, then you've got to put it on. Then you've got to cut it off. And then you've. Step two.

**Chris Gammell:** Yeah. Yeah. Yeah. Right. No, that's a good point actually. Like of the, yeah, you zip it down.

**Dave Jones:** Because everything costs money. When you analyze this, every step costs money. It's time. Time is money. Right? Totally. Anyway. So what was the total cost again?

**Chris Gammell:** What was the total cost of the battery pack?

**Dave Jones:** The total cost is $10,456.

**Speaker ?:** Huh.

**Dave Jones:** It weighs 278 kilos. It takes 33 hours. I won't let you guess anymore. It takes 33 hours. Yeah. Supplier process time. So that's the suppliers to manufacture the processes. It takes the original equipment manufacturer process. The time is almost four hours. Right. The first time they get it right. The first time.

**Chris Gammell:** The percentage of time they get it right. Yeah. So like error rates and stuff like that. Or the opposite error rate.

**Dave Jones:** 0.08%. That must be backwards. That sounds backwards.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, yes. Yes. Because this pops out of the magic formula. Right? Because there's 12,000 parts. There's 59,000 steps. You're guaranteed to screw something up.

**Chris Gammell:** Oh, so it's like multiplying through basically. Like every, every. So if you're like 99% sure that part A is going to work. Then that 1% error multiplies through everything else.

**Dave Jones:** Multiplies through everything else. And yeah. Jesus. They will. Somebody will screw up a step somewhere. With 99.9% guarantee. Yeah, Carl. Where your, your, your pay is being docked 0.1 cents because you wasted X amount of time. You know. Oh my God.

**Chris Gammell:** This is like a, yeah, that's like a good, you know, like manufacturing sucks is like, that's, that's a good. I mean, that's why like you talk about like Six Sigma though. It's like you have to drive everything towards that Six Sigma point. Yes. In order to get everything to have a yield of 80% or 90%. Right.

**Dave Jones:** Exactly. After your thousand steps. Yeah. Right.

**Chris Gammell:** It was crazy about this is I keep thinking like, oh yeah, this is like BMW saying this. This is a third party company saying this. So this is all conjecture stuff. Like they could be totally wrong, but, but it sure sounds right.

**Dave Jones:** It's based on their experience, right? This is what this company, these are experts. This is what they do.

**Chris Gammell:** They're probably hiring old manufacturing engineers and people that work to BMW and anyways. Yeah.

**Dave Jones:** Right. Right. And anyway, so $10,456 manufacturing costs. Only $4,900 of that is the actual material costs. The rest of it is OEM process costs, supplier process costs. $107 for quality burden.

**Chris Gammell:** Yeah. You got to check those parts. Yeah. Someone's looking at it. You got to pay their salary. Yeah.

**Dave Jones:** Yeah, exactly. So there's a hundred bucks just in the cost and SG&A, I don't know what SG&A is, but that's $1,500.

**Chris Gammell:** That's like, that's another overhead amount. I forget what it is.

**Dave Jones:** Yeah. I can tell you.

**Chris Gammell:** An accountant would know what that is.

**Dave Jones:** Yep.

**Chris Gammell:** But it's like, it's like the carrying cost of the organization. I'm pretty sure.

**Dave Jones:** Right. Yep.

**Chris Gammell:** Selling general and administrative expenses. Right. So basically like. There we go. Yep. Yeah. All the overhead of sales.

**Dave Jones:** All the paperwork overhead. Yeah. Right. And all the other overhead. Yep. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, you have to pay managers and you have to pay, you know. Sure.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Inspection workers.

**Chris Gammell:** That meeting does actually cost money as much as your manager doesn't really pay attention to that. Yeah.

**Dave Jones:** Right. Anyway, so that is absolutely fascinating. So well worth your 10 bucks if you're, you know. What are the other reports?

**Chris Gammell:** So this is just the battery pack, but does it do like the motor, like the motor assembly and stuff like that too?

**Dave Jones:** The other one. Yes. The drive line is a report. The Rex system, whatever the hell the Rex system, the IP and interior trim, the seats have their own reports. Infotainment system.

**Chris Gammell:** That's probably the IP. Yeah.

**Dave Jones:** Yep. Oh yes. Yeah. I, I, IP info, info something. Yeah. The structure of the body, the exterior reports are like bumpers and things like, you know, headlights and things like that. The roll in chassis report. Uh, the system electronics report. So they've got a report just for the system electronics.

**Chris Gammell:** So, you know, just for the harness, probably like the cabling harnesses. Yeah.

**Dave Jones:** And your, and your car computer and your, and your anti-lock breaking computer and your, you know, radar. Yeah.

**Chris Gammell:** That would be a good one to look at too. Yeah.

**Dave Jones:** Oh yeah. Yeah. Yeah. It would be. Um, and, and then the cooling system has its own report. So yeah, you know, the battery has to be cooled and everything, you know, and, and the air con, the, it'd be include the air con system. And yeah. So there's 10 separate reports and you can get it for 10 bucks.

**Chris Gammell:** They're going to sell a couple of reports. I think after this, Dave. Yeah. You should get a, you should get some kind of a, I should get a kickback.

**Dave Jones:** I should get a referral. Yeah, for sure. Anyway, it's just, yep. And they've got right at the end. If you look at the second last page or something, they have some YouTube videos for the ice I BMW, I three plant assembly line videos. So I, I have not watched those yet, but that could be fascinating as well. So yeah, but the cost. Wow.

**Chris Gammell:** There was a disappointing video. It was, I thought it was going to be better. It was an Intel factory tour. It was just showing like the internal. I saw that.

**Dave Jones:** It's nice. It's nice to see the pods go. And they just showed these pods, these overhead pods.

**Chris Gammell:** They're called Dave.

**Dave Jones:** Foops. Oh, sorry. I didn't use the industry terminology.

**Chris Gammell:** Front opening unified pod.

**Dave Jones:** It's worth a watch.

**Chris Gammell:** It's my experience talking. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** I wish there was more stuff like that because it really is interesting. It gets kind of dull after, you know, working.

**Dave Jones:** But you've got to have somebody knowledgeable on the whole thing to take you on a proper technical guided tour. You know, this is just a, this is just a fluff piece, you know, it's just look at all our fancy overhead robots, you know? Yep. Kind of. Yeah.

**Chris Gammell:** And the robot systems are, are really interesting and like, you know, how they have like, well, I guess what we talked about earlier, right. Thinking about like supply chain, like you can visualize supply chain in a fab, right? So like if you, and they don't show that they show a little bit of this, but basically like you think about if you've got a photolithography process where they're, you know, basically they're exposing a wafer and then they rinse it and then it's supposed to go to dry ash, which is my thing that I used to do. And then, but say I messed something up and I broke all the machines. I never did that. Let's just pretend I never did that.

**Dave Jones:** Right.

**Chris Gammell:** But then basically what happens is you have all of this, you know, all this supply coming in there and just like building up. And like, so literally they have like these storage bins, like these storage areas inside a fab where they will just store the foops for however long. And eventually they'll have to slow down the incoming stuff. But say now you slow down the incoming stuff and you just, you just turn off all the photolithography. Then you just say, nope, nothing else is coming through. And then finally Chris gets his shit together and that process step starts to go again. And then you work through the backlog and then, but then if you don't, if you don't start up the photolithography stuff again, then there's not enough supply in, in that cycle, in that chain rather. And now you're running behind again. And so it's like this push pull. And so it's like a really good visualization of like, of the overall electronic supply chain of, you know, if you don't have the parts in your start at the right time, it just ripples all the way through and it really can, you know, and it's like, and now Steve's saying, he's begging us to, you know, put us 12 week, 12 week, uh, whatever. And that's because like, they're just trying to make sure that they don't look like, you know, buttheads because they don't have any parts. Right. And so that's ultimately what it's coming down to.

**Dave Jones:** Yeah. Because I have to plan them. They've got to buy the raw materials. They've got to set up the process line. Yeah.

**Chris Gammell:** It's a crap job. I, I, I don't, I don't, uh, I don't envy them. It's, it's, we just get to sit here and complain. It's, this is, this is the thing to be doing.

**Dave Jones:** And we just watch videos going, Ooh, robots. But I was actually surprised at the complexity of this overhead robot system, which basically just transports wafers like through like 12 different buildings.

**Chris Gammell:** It's like, you know, how would you, how would you do differently?

**Dave Jones:** Cause I, Oh, I don't know. I just thought they'd be on carts and they'd just wheel them around. Like I, I didn't think there was that high volume in terms of like, like, like, like as one, just one wafer, you can get like thousands of chips out of. Right. So I didn't think there was that kind of throughput in terms of wafers kind of thing. I was just actually surprised that they needed to go to this sort of effort to just to physically transport the wafers around.

**Chris Gammell:** Yeah. There's, there's like a, there's basically like a monorail for these, like the little, the robots. And then basically the monorail comes up. It lowers it literally like Dave's saying with like, with cables and then it lowers it onto a, uh, like a platform. And then the whole food slides in to actually get processed by the particular process step it's at. And yeah, it's, it's, um, I think if it was on the floor, you wouldn't get as much. So first off, you couldn't have humans there and then you just wouldn't get as much throughput either. Right. Yeah. So, yeah.

**Dave Jones:** And, and they've got storage bays, like when, when they're not being, you know, when they're waiting for the next process step, the, they can, the robots can just pick these up and go put them in the storage facility and they're all tracked and marked and then they can bring it back out once, once the next step is up and running, you know, or he's actually, yeah. They go, right. We have to manufacture more, you know, Intel i7s over here, you know, and push the button and, and the floop comes in with your wafers, you know, there it'd go or whatever. Yeah.

**Chris Gammell:** The floop. Yep.

**Dave Jones:** Whatever it is. I don't know. What's it called?

**Chris Gammell:** Foop. F-O-U-P.

**Dave Jones:** Foop. Foop. Foop.

**Chris Gammell:** Yeah. Foop's a good word though. I mean, I like it. I just think it's, you know.

**Dave Jones:** Anyway. Yep. That's enough about manufacturing. Jeez. This whole episode was about manufacturing, wasn't it? Well, we have no idea what we're going to talk about when we start this show. We just press record and it goes somewhere, you know. Yeah, exactly. It's just, anyway, so we're way over time. So let's end with, unfortunately we have to end on sad news, but we really have to, yeah.

**Chris Gammell:** Yeah, we've got to mention it.

**Dave Jones:** Grant Imahara, Grant Imahara from, you know, he, he, he was one of the Mythbusters. Yeah. Sadly passed away at 49. He wasn't old. Yeah. In fact, he didn't, you know, he looked nowhere near 49.

**Chris Gammell:** Yeah. Yeah. He was always boyish looking. Yeah. Yeah.

**Dave Jones:** And he had brain aneurysm. And he's, yeah, like apparently quite sudden, although not that sudden. Apparently, um, I read a thing that, um, did say like, it didn't, didn't just suddenly happen. It happened over like two or three days or something. So it happened over a couple of days. Like he was just having dinner.

**Chris Gammell:** Yeah, there's lots of complications from, from that kind of thing.

**Dave Jones:** And they tried to save him, but they, yeah. Over a couple of days, he had two operations. They were actually, uh, he was preparing to go into a third operation, but yeah, the brain and aneurysm just got him. Unfortunately, Grant Imahara, a true nerd, a true engineering nerd like us. And, uh, yeah, yeah. Like, yeah. I only heard good things. Like everyone I know who actually knew him, um, said he was a top bloke. So.

**Chris Gammell:** Yep. Definitely. Yeah. I got to meet him a couple times, but it was always like promotion, you know, type things. Like, uh, yeah.

**Dave Jones:** Yep.

**Chris Gammell:** So yeah, we're going to miss him. It's, uh, it's, you know, people should go check out, obviously there's all the old Mythbusters things to watch, but also the, you know, the.

**Dave Jones:** I haven't watched the White Rabbit Project and there's the BattleBots and, and yeah. And he starred on a Star Trek, Star Trek series. Yeah. I didn't know that actually. It was Sulu. No, I didn't know that either. He was, uh, he played Sulu.

**Chris Gammell:** I think that was like a, it wasn't fan fiction, but it was like a fan produced.

**Dave Jones:** Yeah. It's more, yeah. It's something like that. Yeah. Yeah.

**Chris Gammell:** It was like a web series type of thing.

**Dave Jones:** Yep.

**Chris Gammell:** So it's cool.

**Dave Jones:** So yeah, very sad for a, yeah. Fellow nerd, fellow engineer.

**Chris Gammell:** Yeah. Yep. Yeah. And, uh, if people want to hear other nice anecdotes about him, uh, Adam Savage, who worked with him on Mythbusters, obviously. Yes. I watched that. Him and Norm Chan, uh, over on Tested, they did like a. Yep. There's some great stories. Like a one hour kind of. Yeah. Yep. We were calling it. So yeah. That was really, that was a nice, that was a nice, uh, tribute.

**Dave Jones:** So yeah. It's a, geez, I hate 2020.

**Chris Gammell:** Yeah. Frigging sucks.

**Dave Jones:** Sucks, man. Just. Yep. Yeah. Really does. But yeah, that's unfortunately, that's a, you know, a bit of a wake up call. It's like, geez, you know, he was only young and yep. That, you know, no other preexisting medical conditions that I was aware of. And just, yep. Brain aneurysm. Jeez. Fingers crossed.

**Chris Gammell:** Touch wood. Fingers crossed that you. Yeah.

**Dave Jones:** Okay. That I don't. Yeah. That, you know, something doesn't explode inside me. You know.

**Chris Gammell:** Got it. Yep.

**Dave Jones:** Yep. Yep. So yeah. Sad, sad loss, unfortunately for the industry. He was one of like the whole high profile engineers. You know, there's only, you know, there's not too many high profile engineers in the industry. I agree. Yeah. He was, he was one of them. Like, could you name what other high profile engineers, like public engineer, you know, there'd be Bill Nye, the science guy, who's technically a mechanical engineer. He's not a scientist.

**Speaker ?:** Yeah.

**Chris Gammell:** Maybe like Dean Kamen, maybe.

**Dave Jones:** Yeah. But no, people don't know him as an engineer, I guess. Like people know that. Yeah. Grant Imhara. Yeah. He's, he's the engineer from Mythbusters. You know? Yeah. He was like, you know, I mean, there's not too many. Please leave it in the comments down below. If you're aware of any other, like, you know, public. Yeah. Obviously we could rattle off names in our little niche, of course, but that. Yeah.

**Chris Gammell:** You stop someone on the street though. That's the, that's the real question.

**Dave Jones:** You stop someone on the street and they're not going to know who Bob is. Right.

**Chris Gammell:** They'd be like, what's an engineer. That's, that's probably what most of them would say. Yeah. Yeah. No, I think Grant was a great example of outreach and, you know. Yep. Yeah. I mean, like I read tons of people in comment sections just saying that Grant got in engineering and that's, that is a hell of a legacy.

**Dave Jones:** Yep. It is. And, and he did all those mouse videos, which were more mainstream kind of thing. They were like, you know, he went, uh, went around the, you know, and visit different places and things like that. And, um, sort of did, you know, more general interest engineering stuff.

**Chris Gammell:** Well, we should all aspire to do that. I think everyone should go build a robot in Grant's honor.

**Dave Jones:** Or simply design a piece of B because he was in. Sure. Yeah. Why not that too? He was a fellow nerd like us. That's what he did. You know? So any, any engineer in will do. We'll take in the engineer. It doesn't have to be robots. Okay. Yep. All right. Catch you next time. We'll see you next time.
