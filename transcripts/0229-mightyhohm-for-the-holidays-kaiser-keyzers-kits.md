---
episode: 229
title: MightyHohm For The Holidays - Kaiser Keyzer's Kits
url: https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/
---

**Jeff Kaiser:** This is the F-Hour Podcast. Recorded December 23rd, 2014. Episode 229. Kaiser, Kaiser's Kits.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And this is Jeff Kaiser of MightyOhm.com. Hey, guys. Yes, sir. Yes, sir.

**Jeff Kaiser:** You know you were going to get it. Ho, ho, ho. Yes, sir.

**Chris Gammell:** Ho, ho, ho. Yeah, it's like, you know, Santa. I appear around the holidays. Or Mr. Hankey.

**Dave Jones:** As I'm recording this, it is 12.45 on Christmas Eve. I know it's not Christmas Eve there, but it is here.

**Chris Gammell:** Well, you push it. It's Christmas Eve Eve here. Christmas Eve squared. Right. It's the drinking night here. It's traditional.

**Dave Jones:** And we haven't had you on the show forever, it seems. I know.

**Chris Gammell:** Thank you for inviting me back. It feels like time has passed so fast since I was last on the show. I actually had to go look it up, and it was, like, late last year. So a bit over a year ago. So time really flies. Oh, man. Wow. Yeah. That's bonkers.

**Dave Jones:** And you're still at Valve.

**Chris Gammell:** I am.

**Dave Jones:** How's that going?

**Chris Gammell:** Yes. Yes. That's all you can say, folks. I can confirm my employment status. No, actually, things are going really well. It's been a really exciting year. And I think that the last time I was on the show was just before we had sort of entered a big new phase for our project. And we're actually on kind of a couple big milestones past that now. But at the time, I think it was before we had shipped one of our early betas to users for playtesting. And so I think that at that time, compared to sort of everything I've learned since then, I kind of feel like I was a noob. And I'm still learning a lot, still super busy. But this year has been a really amazing year. And we're working on a bunch of really exciting projects. And I've been really fortunate to be a part of it and to be very central to one of the products, which I've been kind of most attached to since I started. And it's been amazing, just absolutely amazing. In fact, I just got back from a trip to the East Coast where I was visiting one of our factory facilities and got to see a bunch of equipment that's going to be used in volume production of a product that I've been working on for quite some time. And it's been totally awesome to see that stuff. So yeah, way, way cool.

**Dave Jones:** So you're making stuff in the US?

**Chris Gammell:** That's a complicated answer to that question. It always is.

**Jeff Kaiser:** Designed in the US, at least. We know that. That's what it always says in the back. Designed in the US, made wherever.

**Chris Gammell:** Certainly a lot of the prototyping that I do is US-based manufacturing, just for the pure reason of speed. But when you get to the bigger quantities, it gets a lot more complicated. And I'm hoping that we'll be able to talk about a lot of that stuff next year. So look forward to hearing more about all of this stuff, hopefully soon. And it's going to be really exciting to finally talk about a lot of it with people.

**Dave Jones:** And you're learning the joys of mass-produced consumer items?

**Chris Gammell:** I am. Items? This past year has been really me learning the ins and outs of volume manufacturing of consumer electronics. Right. Which is a whole other class, too, right?

**Jeff Kaiser:** I mean, that's the big thing.

**Chris Gammell:** It really is. Yeah, it really is. And all that stuff that they talk about, there's a lot of buzzwords, but like DFX is one of them. Everybody's talking about DFX, which is designed for excellence or just DF and then blah. And that could mean design for manufacturing, design for test, design for assembly, all of that stuff. I've spent a tremendous amount of time over the past year learning about how design for manufacturability, particularly on PCBs and electromechanical assemblies, how hard it is to get that stuff right. And I won't say that I've gotten to the end of that. There's still quite a bit of work that I've got ahead of me in 2015. But it's been kind of a crash course in design for manufacturability and design for test. And it's all stuff that I wish that they taught in schools, because a lot of it were lessons that were just really hard to learn. And I think it's a combination of reasons why this stuff isn't really taught and also why as an engineer starting out, it's really hard to just like, you can't just pick up a book and read about this stuff, which I wish you could. But it's been fascinating to kind of learn it in many ways, the hard way.

**Dave Jones:** And a lot of it's very specific to the product and the industry that you're manufacturing for. I mean, you know, that's why you can't just read a book and, oh, I'm magically a DFM expert, you know?

**Chris Gammell:** It's really true. And that's true for a lot of things. Like, I've spent a lot of time over the past year doing EMC and design for EMC. And that's one of those things where if you're building a medical device, there's one set of things you need to know. And if you're building a consumer electronics device, it's totally different. The laws are different or the regulations are different. The import-export stuff is different. The limits are different. And it's just like, I know one little corner of it. And it's sort of, it's what they call ITE equipment, which is basically computer and computer accessories. Like that whole sub-branch of EMC, like you could spend years learning the ins and outs of that stuff and how the laws apply in different countries. So I can tell you all about like South Korea's regulatory requirements for wireless devices for 2.4 gigahertz. It's like, I know like these very specific niches. Sorry, ladies, he's taken. But it's the kind of stuff that you have to learn in order to ship a product. And it's really fascinating.

**Dave Jones:** Can you give us any generic things that you've learned? Not giving the game away of the products you're working on, obviously. Any traps for young players?

**Chris Gammell:** You know, one of the things that I've found is kind of universal across many different parts of manufacturing. And I'm actually curious if this is something that's been largely my experience or if this is a typical experience in this part of the industry. And that is that when you're working with large contract manufacturers or you're working with prototype houses or you're working with component vendors, it's really hard at the outset to say, tell me all the things I need to know in order to make a successful product. And I don't mean like a successful product in terms of like it does the right stuff and users like it, which really should be what we spend the most time on. But it's more like all the nitty gritty of like, you know, how far can this component be to the edge of the board? Like, really, you know, not just like tell me the minimum, like the safe limits, but also tell me kind of what you can really do. And one of the things I've found is very true for many of those types of problems is that the only way to really get the answer is to actually build it and that you can't just ask somebody before you build it. Like, hey, you know, what do you think? Never ask.

**Jeff Kaiser:** A person trying to sell me something, what is the primary way this is going to fail so I can buy it from you?

**Chris Gammell:** Exactly, exactly. But even getting that kind of wisdom of like, okay, so for someone who's built a whole bunch of products like this, like in general, you know, what would you say is a good like clearance rule for this particular situation? I found that that almost never really works in a time efficient manner. It's way better to just make a whole bunch of crazy assumptions and then go try to build a bunch of them. Yep. And that's when people will actually take you seriously and will actually say, oh, yeah, actually, you totally can't do that. And that totally doesn't work. And then you end up like kind of facepalm, like, why, you know, why did you let it get to this stage where I've spent all this money and all this time? And like, you could have told me that. But I found that it seems like that's how the industry works. And that it's sort of this iterative design process by which you make a bunch of assumptions. And you just have to try stuff. And in a lot of cases, you'll get to the wrong answer way quicker if you just kind of shotgun it and be like, let's just do X. So that's one of those truths that was really hard for me to learn because I wanted to solve it the other way. I wanted to say, OK, tell me everything I need to know. Yeah. And then I'm going to do it right the first time and it's going to work and it's going to be perfect. It's incredibly hard to do that.

**Dave Jones:** That's not uncommon in the industry. But the only trap with doing it that way, which is the most common way to do it, is that if you give, you know, make, as you said, a whole bunch of crazy assumptions about what you can actually assemble or do and give it to them and then they give you back the finished product and they don't mention anything. They just said, you know, here's your board, you know, and everything's fine. But it turns out that no, they sort of like hand soldered that part or they did this or they did that just to get the job done. And then it's not relevant to volume manufacturer until you hit like a, you know, a hundred thousand. You know, then when you give them an order for a hundred thousand, they go, oh, sorry, we can't really do that.

**Chris Gammell:** And it's amazingly hard to get that kind of feedback. And I think that's what really separates a good contract manufacturer from a bad one. And I've been really lucky to work with some really great resources on the contract manufacturing side who have taught me a lot and have helped. But at the same time, the kind of thing that you're talking about where something that works perfectly well in prototyping doesn't scale to volume. I really do feel like the only way to know if this is going to work when you build a hundred thousand is to build a hundred thousand and that you're going to, you're going to learn it one way or another. And you're going to have a lot of reason to fix it when you've got 50,000 bad units that are sitting on a shelf somewhere. So there's a lot of pressure to figure this stuff out, but it's sort of like you can't plan really for that kind of crisis enough. Like there's, it's just, the system is not really set up for you to do that.

**Jeff Kaiser:** We should remind people about your background too. It's like you just used to design those preamps, right? Like the, I think the stuff we were talking about last show with, uh.

**Chris Gammell:** I, so I, I listened to the show last week, which was an awesome show, by the way. And all of those things about three, five semiconductors and gas and. I thought that might have been your stuff. I see. That's the, that's the world that I came from, uh, and that I worked in for quite a long time. And I actually designed gallium arsenide, uh, power amplifier chips. And I think that might be where, you know, you take the chip designer in me and then you thrust someone like me into consumer electronics. No, no testing it out. You can't just try it and see what happens.

**Jeff Kaiser:** It's like, oh, that's right. That lot cost a hundred thousand to do one test run.

**Chris Gammell:** And I think that is an interesting cultural thing. And you guys were talking about CMOS prices for a mask set. You know, when you're doing CMOS chip design, there's a huge incentive to get everything perfectly right. And you'll spend millions of dollars in simulation tools and you'll hire design verification engineers and all these people that kind of all work together to make sure that the thing works as designed at the, at the outset. Um, that, that really isn't true in many other, uh, from, at least in my experience in many other branches of electronics design, it's more, uh, just build it, you know, find out what works, keep tweaking until you get it right, until you get the yields where you want them to be. And it's this very, um, it's, it's a hard process and it can be very stressful and very difficult. But at the end of the day, um, I think that you, you end up being able to follow the bleeding edge of technology, right? If you were overly conservative, then you'd end up paying more for your product and you'd end up, uh, not taking advantage of the full capabilities of all of the parts of the supply chain, right? Because you'd be designing for the least common denominator. Exactly.

**Dave Jones:** Oh, so you're, so you're doing some stuff in the U S but ultimately probably a lot of it's going to be done in China, right?

**Chris Gammell:** It's, it's definitely, it's a complicated picture. And I, I, I think a lot of those details will hopefully be things that we'll be talking publicly about next year. Right. Um, so I'll be excited and interested to kind of share that story then, but it's still a story that's kind of unfolding as we go along. There's still a lot of work to do. Um, and it's been interesting to see that, but, uh, I, I, I will say that, you know, the majority of PCBA manufacturers, of course, done in China. There is some that's being done in the U S you know, particularly you hear about companies like Apple that are building, uh, Mac pros. There's a lot of medical devices that are built in the U S a lot of kind of higher margin stuff. Uh, but for consumer, it's pretty hard to, to beat China and there's a lot of expertise there. Pricing is generally, uh, going to be better. Uh, so you end up making decisions that are based on a lot of factors and, uh, we've, we've had to make a bunch of decisions along those lines. And I'm very interested to see how that stuff plays out, uh, as we, as we, you know, start building lots of widgets, um, which is something that is very new to me still. And it's been fascinating to, to learn about a late nights coming up in your future.

**Jeff Kaiser:** How about a lot more, a lot more, right? Dave knows the, uh, the rigors. Christmas, New Year's Eve. What's that? Yeah. It doesn't matter.

**Chris Gammell:** It's really, it, it's, you know, I think it's, it's worth it. It's like, it's kind of, you, you have to go through it. I wouldn't have believed when I started that I would get to do this and that I would get to learn so much about this process. But I really do think that it's not something that you can easily be taught. I think you have to, you have to do it.

**Dave Jones:** Yep. Totally. So is, is this the kind of stuff that would Valve would want to show off at the Consumer Electronic Show, for example, or is that not the right, uh, place? Because that's, that's, that's coming up like a first week in January. So yeah, you better get that, uh, you better get that halfway finished.

**Chris Gammell:** It was, I was actually thinking about CES recently. Um, why is CES in January? I think it's because of- I was talking to a coworker of mine, like why, who was it that decided that the biggest consumer electronics event of the year was going to be in January such that all engineers and consumer electronics were going to have to work frantically through the holidays. And, and not only that, but you've got all these poor sales reps that are trying to schedule meetings during the first week in January. And, and to be honest, like this time of the year, most people are kind of checked out, right? They're at home with their families. If they're not frantically working towards some prototype, like people are just not around. And so you've got these sales reps that are trying to coordinate meetings and, and they're getting nowhere because everybody, it's like, it's like molasses, right? People are just kind of, they turn into a pumpkin and they go away for two weeks around Christmas time. And I think every company is different, but like, what about March? There's a lot of other times of the year that probably would be perfectly cool. And Vegas would be just as cool other times of the year. Why on earth is this the first week in January? I don't know. I really don't understand.

**Dave Jones:** If anyone knows the history, um, please. Well, it went like, it was started like way back in the eighties or something, wasn't it?

**Chris Gammell:** And, you know, I think they still had Christmas at that time though.

**Dave Jones:** I think they would have, but you know, like it wasn't nearly as big, like it was sort of, you know, I don't.

**Chris Gammell:** CES or Christmas? I think Christmas was the same, but I, uh, yeah, you might, you might be right. I, I don't really get it. Um, I mean, there's a lot of other shows that are throughout the year and, uh, Valve goes to a couple shows, uh, pretty regularly. Um, we've been at CES the past couple of years. Uh, and yeah, I think it's, for us, it's really more about like making sure that we've got the product at the point where we want to talk about it publicly, that we feel like we have something to talk about than just going to the shows and using the shows as like milestones. Cause I've actually been a part of that before at previous companies where like CES was like the event of the year and you had to have all your stuff ready and it was going to be a big opportunity to get funding and actually share with the world what you've been working on. And so it ends up being this big milestone to actually get a working prototype at CES. And you, you read about this, like all the big computer companies, like they always used to have their, like the Commodore 64 or whatever was like wired together with bubble gum and holding things together. And I think that's kind of the mentality that a lot of companies go into shows like CES with. Uh, and I, I think that, you know, where I work, it's a little bit different. I'm really fortunate that it's not this mad rush to get ready for CES every year.

**Dave Jones:** Right. So Valve is not showing anything at CES folks. This year coming up, maybe you got something.

**Chris Gammell:** If, if we do, it'd be a big surprise to me, but. Oh, there you go.

**Dave Jones:** All right. All right. So we'll either have to wait for next CES as in 2016 or, uh, or some other show to reveal your hardware, because what's the, I mean, you said 2015, but it's a long year, you know, it goes from January to December.

**Chris Gammell:** Yeah, it sure does.

**Dave Jones:** Come on, throw us a bone, throw us a bone. No, you're not getting, you're not getting anything. Damn it. He'll have HR down on him before you can know it.

**Chris Gammell:** No, honestly, I mean, it's, I've been working hard this year and, uh, expecting to, to just keep plugging along and there's a lot of work to do. So it's, it's making a product, uh, takes an incredible amount of effort and it's not something that happens overnight. Uh, it's something that takes time and, and a lot of really talented people to, to pull it off. Well, I'm very fortunate to work with some.

**Dave Jones:** Speaking of which I just, uh, I'm currently rendering as we speak. So I hope my machine doesn't crash, uh, rendering a video, a teardown video of the Apple, uh, Lisa, the original 1983 Apple Lisa. Um, and it, uh, the reason I brought that up is because it took apparently five years to actually develop that machine from when they first started work on it to when they actually released it in, uh, January, 1983. So it started back in, uh, 77 or thereabouts. Absolutely amazing. Just takes forever. And that's, you know, like, uh, people who used to, you know, product that, you know, they say like the typical product design, uh, time, eh, less than two years and that, um, 18 month kind of, you know, ballpark, um, is, is always been the magic figure. And then, uh, people are saying, oh, it's getting worse these days. It's always, you know, it's nine month, uh, cycle, you know, nine month development cycle. And yeah. Um, but no, some, some things can take many years and I was surprised that the Apple, uh, Lisa took five years or thereabouts.

**Jeff Kaiser:** Can you tell me what the Lisa is? What is that device again?

**Dave Jones:** Oh, it was that the Apple Lisa was the first, uh, graphical user interface. Um, uh, Apple pre the Mac. It was actually before the Macintosh. So.

**Jeff Kaiser:** Was that the one that was like a tablet or actually it was just a display? No, no, no.

**Dave Jones:** It's a, no, it's a video display. It's a, you know, it looks like the Macintosh except it's a wider. It's much wider. It's like three times the width. So. Come on. I thought you guys would know the Mac. The Lisa.

**Chris Gammell:** Oh, no, absolutely.

**Dave Jones:** Absolutely. Chris. Youngster. Sorry, man. I don't know. You weren't even born when that was out, were you?

**Jeff Kaiser:** Uh, I don't know. I don't know.

**Dave Jones:** Unbelievable. So yeah, it is 31 years old. So yeah, I think it is, uh, younger than.

**Jeff Kaiser:** I am also 31 years old. So. Oh, there you go. Yeah. So there you go. Yeah. That's crazy.

**Dave Jones:** So yeah. Anyway, that took five years of development. You know, imagine the ins and outs over five years and how, you know, imagine if you're working on that from the get go and your product didn't see the light of day for five years. You know, that's, that's a long time for an engineer to handle.

**Chris Gammell:** And I, well, I mean, it could be much worse though. There's many products that, uh, have never seen the light of day that have been worked on.

**Chris Gammell:** Yes. That was my entire career.

**Dave Jones:** Yeah.

**Chris Gammell:** I think I'd much rather.

**Dave Jones:** I built my career on unfinished projects.

**Chris Gammell:** I'd much rather have a product that came out eventually than one that just got canned. And I, I know engineers I've worked with that have had that happen at previous companies. And, uh, that's dramatic. I mean, you think about the number of startups that work on a product for years and then they just kind of fold. Fold before it gets out the door. That's too bad.

**Dave Jones:** But it has its pros and cons. I mean, the, you know, the bad thing is that, well, you never get to see, you know, the satisfaction of people using it and never get to see it on the shelves or whatever it happens to be. Right. But the flip side of that is that you don't have to do the, you know, that last 5% of the crap work actually getting it to market. Right. So you just do the cool design stuff and then, ah, yeah, that, that, that was canned. Okay. I've done 90% of it. Yeah. That was fun. And then you go on to the next project. So you don't have to worry about, you know, dicking around bloody production. So it has its, unless you're an aficionado of test systems and all that production jazz, you know?

**Jeff Kaiser:** Don't you love GPib?

**Dave Jones:** Love what?

**Jeff Kaiser:** GPib, the programming interface for a lot of test gear.

**Dave Jones:** Oh, GPib. GPIB.

**Jeff Kaiser:** Yeah. You don't call GPib?

**Dave Jones:** I've never heard it called GPib before.

**Speaker ?:** Hmm.

**Dave Jones:** Is that a Yankee thing?

**Jeff Kaiser:** I don't know. I just work at a test equipment company and they, that's, you know.

**Chris Gammell:** Yeah. I've definitely heard that.

**Speaker ?:** Yeah.

**Chris Gammell:** Right. Well, it used to be HPIB and it was GPIB, right? Yeah. HP interface bus.

**Dave Jones:** No, it's always been spelled out like that. IEEE 488. Or it's always been the HPIB. Yep. Oh, the IEEE 488. Yeah, exactly.

**Chris Gammell:** Oh, goodness. So you've got triple five, but not, uh, not GPib.

**Dave Jones:** Right. Yes.

**Jeff Kaiser:** Oh, we, man, that's an old conversation from the amp hour.

**Dave Jones:** It is a very old conversation.

**Chris Gammell:** Let's not go back there. Think of me like that backup that you find, you know, years later. It's still got the files that you were working on. Yeah. Yeah. You're right. This is the Kaiser disc. So you could draw it like diagrammatically.

**Jeff Kaiser:** Or, uh, it was a PsyQuest. PsyQuest, actually. Yeah. Was it Big Endian or Little Endian? I don't, I don't remember.

**Chris Gammell:** I had kind of like a bookmark, a bookmark for the show. Yeah. And kind of go back and we could figure out what we were talking about.

**Jeff Kaiser:** Speaking of 555, are you still selling your, um, uh, your, your, uh, detection kit for the, um...

**Chris Gammell:** I totally am.

**Jeff Kaiser:** Yeah?

**Chris Gammell:** Yeah. The, the Geiger counter kit. Geiger counter. Thank you. Sorry. Yeah. And, um, it's been, uh, kind of a back burner thing for me because obviously I've been really busy, but, uh, I, I do still do a little bit of the hobby stuff on the side and I still do the, the kits. Um, but it's, it hasn't been as big as it was, um, years ago. Like I, at the time that that happened, I think everybody was thinking about radiation and interested in learning about radiation and Geiger counters and Fukushima was still fresh in everybody's mind. And so I think that meant that the first couple of years there was a huge amount of interest and it's definitely slowed down a bit. Uh, but I've also been sort of spending less and less time on the kit businesses. I've had just kind of less time for projects. Um, but it's still plugging away. And, and actually I just had kind of a surge of, uh, holiday orders that I just finished shipping out that it was sort of a surprise to me. I was actually thinking, okay, this is going to be the first year that I don't have like a big holiday rush. And that'll mean, gosh, I really need to work on a new kit because this one's getting kind of, you know, long, uh, it's, it's been around for quite a while, but then out of nowhere,

**Dave Jones:** uh, for whatever reason, uh, it came a flood of orders.

**Chris Gammell:** Yeah. And so it, this year was kind of a funny year for me because I, I spent most of the year, uh, where I wasn't really selling very many. And then all of a sudden, November, December, things got really busy again. Um, but, uh, I, I'm really lucky. I spend a few hours every weekend and I kind of am able to keep up with it. And it's been really fun because I actually still enjoy doing that a lot. It's, it's really cool for me to have kind of complete ownership of a product and actually be working on optimizing the kind of really small scale manufacturing and looking at suppliers. So it's like all the same kind of stuff I do for my day job, but on a way, way, way smaller scale. Uh, and it's kind of funny to go back and like, look at the design and think, oh God, you know, there's so many things that I would have done differently if I was doing that now. And I think actually designer skill. Yeah.

**Dave Jones:** And I mean, I knew how many I was going to sell, you know, and that, that is actually a

**Chris Gammell:** thing. Like I'd say the number one thing that I wish I had done a better job of when I did the initial design is just using a fewer line items in the bomb. Because when I'm sitting here like stuffing bags of components, I'm thinking, oh gosh, why are there like 42 parts in this thing? Uh, I really could have gotten away with a couple fewer resistors and things like that. And, and I think at some point I'd like to go back and take a look at that, but there has to be sort of like this level of like, you have to be frustrated enough by it that you're actually willing to open up the design again and go and redesign things. And, and I haven't quite gotten to that point yet. And I, I feel like probably the defining moment will be when a component is no longer available. That's when you say, oh, right now I've got to go work on this thing again. But, uh, it's pretty amazing. The design has held up really well and I still get lots of emails from people that are building them and are excited that they got their kit working. And, uh, it's, it's just amazing. I never would have guessed that when I designed that kit that I'd still be selling them now. It's just totally a shock to me, but I'm really happy that I was fortunate enough to find something that people wanted and enjoyed using and building. And, uh, and also that I'm lucky to have distributors like Adafruit and the Makershed that are selling my stuff. It's just really cool. I can concentrate on manufacturing and ship off products and they sell them. And it's just, it's really cool. It's, it's fun.

**Dave Jones:** And, and that's always the trap, isn't it? You go, well, how many more of these bloody things am I going to sell? You know, like it could dry up, you know, and like, it's not worth the design re-spinner. It's not worth ordering another 500. I'm going to order 50 instead.

**Chris Gammell:** I felt that way the first couple of years that I was doing this. And I, I think that the first build I did was 30 kits and I was like, oh, I don't know if I want to build like a hundred. I don't know if I want to build a hundred. It's like, yeah, that's a lot of components. It's a lot of money and Geiger tubes and all this stuff. And, you know, I've, I've sold a lot, sold a lot more than a hundred kits by this point. And, and I think that the real, the, the message to that is, I think it is good to kind of play it safe the first year that you're doing this. But if you're still selling pretty good quantities, like a year or two out, like that's when you do like I do and start buying things in like the five hundreds and thousands, like you just buy a lot, you buy a year's supply of stuff to get the cost down at the distributors. And you, you end up buying stuff overseas and you can afford to wait. Cause you're not, you're not like waiting on a day by day basis for components. And so it lets you do things like that really help. Um, it helped for, for me, like my most precious commodity is time. You know, as somebody that does this kind of on the side now, it's not the majority of the work that I do. Um, for me, I really have to optimize so that when I've got time on a weekend and I can sit down for a couple hours that I've got all the components ready to go and I've got everything there. And so I do tend to like over buy and just make sure that on any given weekend, I've got something I can work on, be it, you know, clipping wires or stuffing bags or putting labels on. And so you have to kind of queue up work, uh, weeks in advance such that at any given time, I've got something that I can do to try to make forward progress. And that's, that's worked really well for me.

**Jeff Kaiser:** That's why I'm still doing it actually. I mean, like that's like, that's not how I think you have to be free time, to be honest.

**Chris Gammell:** So you have to be a little bit nuts. Uh, and I, I think that I, I have become a little bit of, I've, I've become maybe a bit of a workaholic and it's definitely been something that I've, I enjoy doing it. And so I want to do it more. And I, it is hard sometimes to keep up all the side projects and also, you know, keep because, because my, my day job can be pretty intense as well. Uh, and so trying to balance all this stuff has been challenging, but I've pulled it off and it's been a lot of fun doing that. Uh, and, and that's not even including kind of the other projects. I've been working on a lot of non-electronics related stuff recently.

**Jeff Kaiser:** Like? Well, come on, man. We didn't ask you here just to, you know.

**Chris Gammell:** But I thought this is an electronics, uh, themed podcast.

**Jeff Kaiser:** Well, just give us a list and then we'll hear if there's anything that we want. You'd be surprised how many people accuse us of not being electronics podcast.

**Chris Gammell:** Oh, well, so what I've been spending a lot of my time, uh, recently is actually building engines. And, uh, I've got a couple old cars and I think people that know me know that I'm into kind of old seventies, sixties cars. And I, as of this year, I had never actually built an engine before. And so this year I decided that for the first time I'd been wanting to do this for years, I was actually going to rebuild an engine entirely myself. You know, I was going to have all the machine work done obviously by a professional because I don't have all the equipment, but I was actually going to do all the assembly and all the checking and everything myself. And it's something I've always wanted to do, but I'd always thought, oh gosh, that's going to be like a year long project. And it's a huge amount of work. And it turns out it is a year long project and it is a huge amount of work, but it's also, um, incredibly rewarding. And it's one of those like multidisciplinary things where to build engines, you need to learn how to measure things accurately. So I bought a set of micrometers and it's amazing the kind of stuff you can buy on Amazon now that would have been really expensive years ago, but now you can get a decent set of micrometers on Amazon for under a hundred bucks and all the tools are available to you pretty readily online. And it's been totally awesome. So I'm one of those people that if I do electronics all day, I like to go home and then work on something else. Like I, I need to have kind of a change and, and the kit business is, I mean, to be honest, that's largely like manufacturing. It's not so much electronics. Oh yeah. It totally is logistics. No, that's actually very true. It really is.

**Jeff Kaiser:** I browse DigiKey when I'm feeling stressed after a long day of work.

**Chris Gammell:** I mean, finding a new supplier for a component that is like supply chain. It's, it's different than a lot of the stuff I do during the day. And so I get to spend time doing that stuff at night and emailing suppliers for plastics and things like that. But then I also like to do kind of the totally unrelated stuff. And for me, it's always been kind of the mechanical is a really nice way to change things up. So I do electronics design during the day. I get to wrench on cars and stuff at nights and on the weekends. And it's been, it's been a huge amount of fun, but man, is it a, is it a time commitment? It's pretty intense.

**Dave Jones:** Now getting back to the kit thing, cause I know there's a lot of people who want, will want to know details on this. I'm not sure if we've discussed it when you've been on before. Uh, what techniques are you using to actually, uh, to, you know, sort out the components and manufacture these kits? Do you have a, like a separate little, uh, you know, those red little bins for each part? And then you, do you do 10 at once, 20 or 50, or do you do the whole batch at once? How do you handle all that?

**Chris Gammell:** That's a good question. I've, I've, I've seen some of the other pros do it. Like I've been to Ada Fruit and I've seen how they do it. And I think, um, Lady Ada has done videos on how they do kidding. Oh, okay. Um, I've, I've done it pretty much the same way since I started, uh, doing the Geiger counter kits at least. Um, and it's, it's pretty simple. Um, but the thing I do is I've got a big kitchen table and it's, it's kind of a larger than a normal kitchen table. And it's really important to have a huge work surface. And I've, I've got a series of bowls. I actually like bowls, like they're, they're plastic bowls and they have a kind of a, a chamfer on one corner, which means that it's easy to pour stuff out of them, which is really nice for small components. So I've got it. And they're, they're like Dixie bowls. They're like really cheap kind of red plastic bowls. And it just happened to be what I had at the time I started this. I didn't buy them for this project or this purpose. Um, but I do one component per bowl, which means that if a component is like two per on the bomb, there's actually two bowls. Oh, that way you just pull, you pull one component from each bowl. You don't have to like think about it too much. Uh, and I, I basically put exactly, uh, 100 parts typically into each bowl. So I build in batches of a hundred.

**Dave Jones:** And you've got to manually count those or you weigh them.

**Chris Gammell:** And then I use a weighing, a counting scale. Uh, and, and I got to say, um, Adafruit uses the counting scale and that's how I learned about it. It's, it's, I've had it for quite a while. It's pretty, pretty cheap. Um, there are many components though, that do not count well. And one of the ones I found, which is, is annoying is resistors through hole resistors for whatever reason, at least the ones I buy are not super consistent in terms of weight. And that means that you're always going to be either have too many or too few, but the, you know, so for those I manually count and I actually just kind of line them all up and I do groups of like five or 10 and just count them off. And it's tedious, but that's the kind of stuff you can do while you're watching TV. You don't really need to think too hard about it. Um, but the, the basic idea is that by putting exactly a hundred parts into each bowl, if at the end of the building, all of these kits, you've got extra parts, uh, that's when you've got to actually sort through, look at all the bags and we'll know, I mean, I've actually gotten pretty good at like auditing, like the bag and no, you can't do that. No, you can't do that. No, because there's a few parts, like any kind of components on cut tape, the weight varies by more than a resistor is worth of weight.

**Dave Jones:** Yep. Exactly.

**Chris Gammell:** Yeah. ESD foam is also like, I don't always cut it exactly the same. Right. So there's a few sources of, uh, variability, but I think even if you looked at the weight variability of each of the components and added all that up and did a statistical distribution, you'd find that the uncertainty is greater than a resistor. Yeah, exactly. Because resistors weigh almost nothing. Like it's really hard to discern, uh, one resistor, but, um, that's what I've been doing for, uh, I guess about three years now. Uh, and it's worked amazingly well. And I've, I think of all the kits I've sold, I've had maybe one or two examples of screw ups where I missed a part and I didn't find it in my kind of double checking process.

**Dave Jones:** Well, that's not too bad. Out of how many units do you think you've shipped now?

**Chris Gammell:** Thousands, thousands and thousands. Yeah. Uh, I, I don't know what the exact number is. I should go look it up, but I, I crossed, uh, a couple thousand, I think well over, uh, gosh, probably two years ago. I had already crossed like 2000.

**Jeff Kaiser:** You probably just look at your, uh, your tube orders, right? One per kit. Yeah.

**Chris Gammell:** I used to, I used to keep closer track of it, but now I don't have as much time to do kind of the analytics, but I, I used to actually plot prices over time and make sure that, uh, like, cause for a while the, the Geiger tubes were getting more and more expensive as the demand just got crazier and crazier after Fukushima. Like before Fukushima, you could get Geiger tubes for like almost nothing. Like they were very inexpensive. And then all of a sudden everybody wanted Geiger tubes. And for a while I was really nervous that I wasn't going to be able to afford making kits anymore because the prices for tubes just kept going up and up. And I was buying in like bigger and bigger quantities to try to get around that. Fortunately, things are not as crazy anymore. And I find that the market crash situation market crashed.

**Dave Jones:** The tube market actually did not great tube market crash 2013.

**Chris Gammell:** I told my broker to sell them all off, man. The market didn't actually, it didn't crash. Um, it's, it's actually one of those things that that's still a desirable part. Everybody wants Geiger counter tubes for lots of projects. Uh, but it's definitely gotten less crazy than it was, which means that I can be more confident in pricing because it's more stable. Um, but it's still not at the levels that it was when I, before I started all this stuff. It's just crazy to see how supply and demand works.

**Dave Jones:** And how many units would you pack at one time? Uh, how do you mean? Like a hundred per bowl? You'd sit down and do a hundred?

**Chris Gammell:** I'll do a hundred. A hundred is about as many as I would want to do in one sitting. Like at the end of a hundred, your eyes are getting kind of bleary and you're starting to get kind of sore. And that's when I start daydreaming about making robots do all this automatically so that I don't have to do it. Um, but a hundred is, uh, about as much time as you can do like in one sitting. And I've done like 200 and maybe even 300 in a weekend before. And at the end of that weekend, you're just totally wiped out. It's, that's a lot of work.

**Jeff Kaiser:** Resist your stab wounds and all your fingers and you're just, your lead contents up.

**Chris Gammell:** There's kind of silly things that end up being a problem. Like, uh, the ESD bags that I use, uh, if you handle one of them, it's not obvious, but if you handle a hundred of them, they're a little bit sticky. And at the end of a hundred, it's, your hands are sticky and it ends up being like harder and harder to separate the bags. So there's kind of like comedic things that at, at scale, you would never know would be a problem. Um, but I think in general, like I have to say, if it wasn't fun, I wouldn't do it, obviously. So it's, it's something that it's, it's quite a lot of work, but it's really enjoyable. Like I was trying to think recently of like, why do I not, why do I not just give all this work to someone else and pay somebody to actually do all the hard work of like stuffing the bags. But I think at the end of the day, like it's, it's extremely relaxing work. Like it's, you really enjoy kind of carrying the product all the way. And actually like everyone that builds a kit, they know, like I painstakingly built this with my own hands and I did everything. And, and actually I should give my wife credit because she does a lot of the work also. She helps quite a bit. I've drafted her into this and she's been great about it and she kind of knows exactly what to do as well as I do. Um, but if I didn't enjoy kind of that, that feeling of like making this kind of bespoke item, I don't think I would do it. It would be.

**Dave Jones:** Oh, totally. Yeah. Just more work. You have to be crazy to do it.

**Jeff Kaiser:** Well, Hey man, if this whole kit thing doesn't work out for you and this whole valve thing doesn't work out for it, I hear that Dave is hiring. So, I mean, you could probably go and make kit for him if you just moved to Australia and then, you know, you just work over there.

**Chris Gammell:** So I've, I've had a few people ask me if I would do design for, for kits. Uh, and I, I would love to do that. Honestly, I, I need to find a way of calling my projects, but I would love to do more kit design and, and I've got a few ideas for kits of my own that I'd like to build. Um, but one of the things I'll say, you know, to people that do this and have a day job, when I started doing this, I was doing freelancing. I was writing the book. I had a lot of free time, uh, and I was able to, to do, spend a huge amount of time at the outset to kind of get this whole business going. I cannot imagine doing all of that while also having a pretty demanding full-time job. So for people that do that, that started it while they were working, like I know Garrett Mace did that while he was working full-time. There's a number of people that have started this and all also had a full-time job. I have a huge amount of respect for people that do that. It's just, I, the only reason I'm able to keep this going is because I started it kind of before I got, uh, so busy in general. Um, and so as a result, it's really hard to do new kits because that, it takes a lot of time. Like if one of the interesting things about being a manufacturer is that the more things you design, there's sort of this like limit of like, you can't keep manufacturing and do new design, which was one of the things about Adafruit that amazes me is that Adafruit, they've got a manufacturing business, but they're also designing new stuff as, as somebody that has like a couple kits, like two kits that sell. Exactly. It's, it's really hard. Like it's hard to, to scale. And I think that's actually true.

**Dave Jones:** When you've got like a couple of hundred employees, it makes it easier.

**Chris Gammell:** Gosh. But, but at the same time though, if you're like the owner operator, uh, like, like you think about somebody like, uh, like, uh, Lamore, like she's got, she's a manager also. She owns a company. She's got to manage this company. So, so, I mean, it's not like it scales arbitrarily and where there's no additional impact to hiring like the 101th person and there is going to be some impact. Now, granted, it's going to be definitely less than hiring like the first person where you've got to tell them what to do and you build structure. Right. But it's still, I think any manufacturer has this challenge in that it is, you're, you're sort of beholden to the products that you've already designed and that are shipping. And that sort of makes it harder for you to continue innovating and continue making new stuff. And I've definitely experienced that for Mighty Ohm because it's, it's very hard to kind of find that time to do new stuff while also working all the time to fulfill existing orders. That's, that's a challenge for, I think, any small business. Totally.

**Jeff Kaiser:** Well, yeah, man. Dave's about to go a number one. He's about to, uh, you know, hire number one soon.

**Dave Jones:** Yeah. Yep. Get number one. And, uh, yeah, cause I've been doing it solo for 20 years. You know, I've, I've had a kit business for 20 years before all this open source hardware rubbish came along. Oh yes. When I was a boy, I was packing and shipping kits and, you know, typing with a typewriter, you know, typing the addresses on the labels, you know. Old. No, I was fully computerized back then, 20 years ago. You know, I would have my dot matrix printer printing out labels, you know, with the, you could buy labels on the, uh, on the, with the, uh, reels, you know, and then you stick them in your, stick them in your little nine pin dot matrix printer and you could print out, uh, print out address labels. Automation. Woohoo. And, um, yeah. So yeah, I'm going to hire another one. I was surprised actually at that. Like, this is something that I didn't consider. Right. I thought like, didn't it barely even cross my mind that anyone from overseas would bother applying, but like more than half the applicants are from overseas. And I'm going, well.

**Chris Gammell:** How does the, how does the visa process work? Exactly. How does that work?

**Dave Jones:** Do you, like these people, you know, like, like I can't blame them, right? They're like, they're fans or whatever. And they, you know, they, they really want to, you know, come work here and that's great. But unfortunately it's the logistics of the whole thing, you know? And, um, yeah, cause I've heard that getting a working visa here in Australia is pretty horrific. And then, you know, there's a lot of paperwork at my end as well, you know, hiring someone with a work visa or something and they, you know, send people around to audit you to make sure they're not illegal workers and all that sort of jazz. And it's just, yeah, it's just not going to work. Let alone, how am I going to interview you? You know, video interviews suck. And, uh, yep. So unfortunately it's just, it's just not going to work out. So, and also I feel kind of selfish, right? Um, because I, uh, I put on my job description that I'm an equal opportunity employer, right? And I didn't think that that would, you know, I thought, yeah, I definitely am, right? I'm not going to discriminate against anyone for whatever, but ultimately I am because I'm, I really want to hire a local, you know, somebody local.

**Jeff Kaiser:** Oh, well, that's not what that, that term means, Dave.

**Dave Jones:** Yeah, I know it's not what that term means, but it kind of, you know, it's a bit, it's a bit ironic. I put that in there and I'm going to, you know, kind of sorry to those who applied from overseas, but pretty much, um, automatically rule you out because I much prefer to hire a local and support local talent. I just feel much better about that.

**Chris Gammell:** Um, that's a totally reasonable requirement. You just say like, must, must be eligible to work in, uh, Australia, you know, whatever. Must speak Australian.

**Dave Jones:** Must speak Australian, yeah. And I think one person had a working visa and you know, that, that might be okay. But like, I still, even in that case, I still prefer to give it to a local, I think just because, well, you know, I was born here, I spent my whole life here and I sort of want to help support the local industry. Right. Yeah. Yeah, exactly. I want to give a local a start, not somebody from overseas. And when they're finished, well, they're just going to go back overseas.

**Jeff Kaiser:** I mean, you know, that could happen to the local. You can work for Dave.

**Dave Jones:** And learn bugger all and earn bugger all. And, but you know, that could happen to a local too, right? You know, they could work here and then bugger off overseas. Right. But hey, you know, the odds are they probably won't. They'll, you know, continue to get a job locally and it helps, you know, support the industry and all that sort of stuff. So, so would you guys say that I'm right by doing that?

**Jeff Kaiser:** Oh, I'm, I'm way behind you, man, on that. I think that's totally legit. I think logistically, I think, you know, supporting your local community, all those things are good things. I think you're going to catch a lot of crap for it, but you know, whatever.

**Dave Jones:** Oh yeah. Well, I'll cop some crap. I'm sure. You're Dave.

**Chris Gammell:** I would say, I would say that if, if you can, if there is a candidate that's not local, that's willing to take all of the burden of making it easy for you, then that's kind of where you'd say, all right, well, this guy, he went like the extra mile because he got the visa on his own. He figured out how to get sponsored. He came over. You know, like that's, that's where, that's how you're going to separate the folks that like really, really want to do this versus the, like, it would be cool to work with Dave Jones.

**Dave Jones:** Yeah. Yeah. Exactly. And they don't give a thought to the practical elements.

**Dave Jones:** Yeah. Terrible working with Dave. Are you kidding yourself? Come on, man. I would also I would probably consider the person who has a working visa right especially like you know if they're much better than everyone else if they're the ideal candidate then yeah I'm probably going to take them on right I'm not going to take on somebody who's crap just because they're local. Here's my take

**Jeff Kaiser:** on all this right no offense to you Dave but that's right you never want to be the first hire no one wants to be the first hire you want to be like the third or fourth hire let them work out all the kinks on something else right I mean like because that's what it is it's messy you know once you've had like I was the oh yeah totally I was the third co-op at my first co-op position I was the third one they had mostly figured out kind of the well what do we do with a kid who isn't actually an engineer yet kind of thing but like that's a tough thing to do right I mean

**Dave Jones:** oh yeah I have no idea what I'm going to do I'm going to get them in here and we're just going to go well what do we do now I don't know we'll probably stare at each other and go I don't know

**Jeff Kaiser:** right so people from overseas give it one or two you know let Dave figure it out let him screw up the first two or three and

**Dave Jones:** as the empire expands right and I'm moving the bigger dibs you know

**Jeff Kaiser:** yeah there's no stock options in EEV blog don't worry about that you're not getting any early oh no there's no ground floor in the ground floor is the new bunker that Dave bought it's not it's not anything glamorous

**Dave Jones:** exactly yeah yeah yeah I love it yeah

**Jeff Kaiser:** yep well how so Jeff how is I mean how is the scene up in Seattle right we hear I mean we heard a little bit about Seattle when you moved up there and stuff like that are you finding like are there swap meets up there are there like are there hardware events at all because I mean obviously Seattle is a huge software town but are you seeing kind of hardware in the area

**Chris Gammell:** um a little bit I think it's a huge that happens in terms of electronics it's a really really good swap meet and I think it's one of the biggest ones in this area um so that that was a great discovery I learned about that I think I got a flyer or something in the mail and uh decided if I was gonna go I might as well sell and uh it was it was totally cool

**Jeff Kaiser:** yeah you're not getting emails about swap meets man you're getting you're getting like someone going to your door or like an old guy coughing and you hear about you know swap meet it's it's actually

**Chris Gammell:** I find it I find it really endearing like I I actually enjoy amateur radio at least in the Seattle area is a somewhat um I don't know antiquated uh group like yeah man these are mostly the Boeing guys right that have been doing this a long time and I actually find that really charming um I I it's kind of fun to actually mail in an application to a swap meet with a check and you get your notification on a little card that you have to bring with you paper um but I but I will say actually um the the maker fair would learn a lot from this group oh yeah um this group uh the Mike and Key Amateur Radio Club it was the best organized uh event in terms of like loading and unloading of stuff than I've ever seen in my life and maybe that is like there's a Boeing connection or something but basically you pull up you pull up with your car and your car is full of test equipment and heavy stuff and everything uh you are responsible for unloading your car onto a pallet and then that pallet gets a number and it's your table number and then it disappears the pallet just goes away and and you you pull out so like you go into a turnout you unload your stuff in like 10 minutes uh you drive away you go park and then it's going to take you like a half hour to get back to the site you can go get coffee go get breakfast oh yeah and you go to your table and your stuff is there that's nice they actually they actually transport all your stuff to the table and then you unload it off the pallet and then they come by later and they put the pallet away so it's not you know in the way I I was amazed like and and I I should have said something to the maker guys because I saw Dale this year at the maker fair and I saw a bunch of the maker guys like what a cool idea like these guys in terms of manpower it was a lot of people like it was a huge amount of work for them to pull it off but it was it was so cool to not have to worry about like what am I going to do with my car like how am I where am I going to park that I'm going to be able to carry or use a dolly do I have to go buy a dolly to move all this stuff into this building because I was on like the second floor of a pretty big building oh and they took care of all that stuff

**Speaker ?:** oh it rains a lot

**Jeff Kaiser:** yeah I was like why aren't you guys just outside in a parking lot we don't do

**Chris Gammell:** we don't do the outdoor anything here really and I say this as it's pouring rain as it often does here no an outdoor swap meet I think that would be like a joke that would be like the swap meet that they send the newbies to to like oh you go to the you can go to the parking lot sale everything's like half off about the outdoor swap meet and it'll be all the noobs will be in the parking lot and they'll be soaked yeah that's not a that's not a thing here so it's actually at the I think like county fairgrounds or something like that in Kent and so yeah that was really cool I enjoyed that a lot and I think Monty and Alan had a good time too

**Dave Jones:** well that's totally different to the one I went to I sold some stuff as well but like it was a car boot sale you drove your car in to the area you found a parking spot you laid a sheet out or you could leave the stuff in the boot if you really wanted to oh sorry trunk for you right you know a trunk sale or whatever you want to call it and yeah so you just put a sheet down on the ground and you just you know take all the stuff out of your boot and lay it down and there it is

**Jeff Kaiser:** some of the classier folks have tables too yeah

**Dave Jones:** oh well fancy fancy tables

**Chris Gammell:** yeah

**Dave Jones:** oh goodness that's kind of how

**Chris Gammell:** the Silicon Valley one is the one at De Anza is sort of like that like there's a lot of guys selling stuff out of their pickup trucks and you know they get a I think they're like the preferred thing is you have like a blanket that you put on the ground and you cover the blanket with your stuff and if you're like primo you've got a table

**Dave Jones:** oh yeah

**Chris Gammell:** something about tables that's exactly what this is

**Dave Jones:** although yeah like the year before I did this apparently like it was it was actually rained out you know so like like everyone just yep there basically was hardly any car boot sales that day because yeah it was just raining so that sucked

**Chris Gammell:** if we did that we would never get to do anything

**Dave Jones:** right yeah it rains a lot in Seattle I know

**Chris Gammell:** it does although not as not as much as people make it out to and actually this year was probably one of the driest years in the past like 20 or so so we had we had an awesome summer this year Seattle is a really nice place in the summer

**Dave Jones:** yeah I've I've been to Seattle and it actually didn't rain that much so yeah I was surprised like everyone said you gotta have your umbrella take it everywhere you know and I went well no I didn't really need one you know it might have it depends

**Chris Gammell:** yeah it depends

**Dave Jones:** so then again I was only there for like two days or something so you know

**Chris Gammell:** yeah you know apart from the the Mike and Key show I haven't found too much I know there's a couple meetups but I haven't I haven't had the time to really check out all of the meetups that are in town there's there's there's a another amateur radio conference I guess amateur radio is probably the biggest in terms of the hardware scene here and I actually saw Michael Osmond's talk at the Tapper TAPR oh that's right he was up there for that right

**Dave Jones:** yeah

**Chris Gammell:** and I wish I could have talked to him because he had just been on the show and I wanted to meet him and I was really sick that day like I dragged myself over to the show I was feeling like horrible and so I was like oh I'm just not going to be contagious so I went I sat away from everybody else I checked it out and then I like disappeared immediately after that

**Jeff Kaiser:** I'm mighty home sorry

**Chris Gammell:** but it was a cool talk and that's another event that I know folks in this area really look forward to is Microsoft has a similar conference called I think it's like Micro Hams and I think it's also very digital radio-y yeah so I think this year there were actually like two conferences that were that were pretty pretty good and I only got to go to the the TAPR one but it was great

**Jeff Kaiser:** is that the one that's way up in the the sound like on the far coast because Mike's told me about that one I always forget which one it is or maybe that's Smoocon so TAPR oh

**Chris Gammell:** it's the one that's like

**Jeff Kaiser:** on the very far there's one

**Chris Gammell:** that's that's Tourcon Tourcon so Tourcon I went the first year that I lived here I think it's one of those like every other year events and it's a camping themed event so you you bring all your tent and a bunch of stuff out to it literally is one of the most western most parts of the country in northern it's like it's like

**Jeff Kaiser:** the upper left corner of the states it's like you look over and it's like hey there's Canada

**Chris Gammell:** so the funny thing is that you know you're already pretty up and left being in Seattle and then you have to drive like five hours to get out there like it's way out there and I went the first year that I lived here and it was super fun it was it's absolutely beautiful out there like the drive itself was really neat we got to take a ferry which was cool and that was a good scene and I met a few folks that are local that I've sort of kept in touch with since then and it was a nice way to meet people having just recently moved to the area but I didn't go this year unfortunately I was super busy that time of year when it happened I think it's in like the late summer early fall and I missed it like the only time

**Jeff Kaiser:** you want to be up there

**Chris Gammell:** yeah no actually that's probably kind of true yeah I mean it's just

**Jeff Kaiser:** well I guess there's weird there's weird stuff in Washington State too with all like the windward and wayward side right isn't it yeah right you get on one side of the mountain it's like desert and the other side it's like super rainy kind of shit

**Chris Gammell:** no it really is one of the things I've been wanting to do since I moved and I haven't gotten around to yet is go to Hanford there's a nuclear site where they made plutonium for quite a long time I think it's the most polluted area in the country in terms of like a super fun site so you're either taking your wife there for like a romantic get away just go for a short amount of time it's really about cumulative exposure but I think they've they've done a lot of work to try to improve the quality of the environment there but this is the Hanford the reactor where they they did a lot of the plutonium for during the atomic program and Los Alamos and all that stuff and so they give tours and that is in eastern Washington which is in that weird desert-y area and it's like several hours away from here it's quite a long drive but it's a really interesting drive and you get to see really beautiful dramatic country that's not representative of what you would think like Washington looks like like it's not all pine or evergreen trees it's like rolling deserty hills and I drove through there on the way out here from Texas and I've always wanted to go back so hoping that I get to do that maybe next year

**Jeff Kaiser:** I'm imagining you going out there and then being like sir did you bring something with you is your pocket beeping right now so I'm testing I'm testing my Geiger counter

**Chris Gammell:** I would totally bring one of the kits if I went out there I might even bring a few of them musical and give them to people there it's the thing about that area is that I think this was sort of in that era of the military in the United States where if you were done using something you poured it into the ground and that's sort of that this is part of that whole thing and I think there are holding vats for enriched uranium and plutonium in the ground and the vats have like become porous because they were made of steel and they rusted and so all that stuff went into the ground and of course there's a major river that goes through there and so that's not good but apparently I'm told that they're working on that but don't worry that goes further south yeah they're gonna yeah but it's supposed to be really neat you can actually see the B reactor which I think has been restored and so folks have told me that have went out there that it's really impressive so Seattle's actually got a few I guess that's Washington but this area there's there's a few sites like that you know you've got the Boeing tour you've got that there's a computer museum in downtown Seattle that opened up that Paul Allen started that has a pretty big collection of old computer hardware both large and small and the cool thing about it compared to the computer history museum in Mountain View is that you can touch all of it they actually let you enter programs on a teletype machine that's connected to a PDP and you can you can actually sit in there like a whole day you could actually buy a ticket go in in the morning stay the whole day and goof around on a wide variety of old computer equipment so it's really neat yeah Seattle's got a bunch of stuff like that sometimes it's been a little hard to find those things but I've been really pleasantly surprised

**Jeff Kaiser:** helps when you have lots of nerds with money Paul

**Chris Gammell:** I swear like the Microsoft guys in one way or another there's quite a few there's like a World War II aircraft museum up by in Everett I think or near the Boeing factory that I think is also Paul Allen or one of the other Microsoft guys might be

**Dave Jones:** Charles Simonyi or someone like that who's been into space he paid like 40 million to go into space

**Speaker ?:** oh is he one of

**Dave Jones:** the guys that wanted

**Jeff Kaiser:** the 20 million to get on that rocket yeah oh yeah I forgot about that

**Dave Jones:** yep that was Charles yeah he was one of the early ones he's the one who developed Microsoft Office for those yeah

**Chris Gammell:** history yep did he have anything to do with the game that's or the easter egg in Excel isn't there like a flight simulator in Excel

**Dave Jones:** oh possibly that's stretching my I don't know but no that might be after his time he worked on you know the very early very early implementations Bill Gates if you want to know your history Bill Gates hired him because he did his masters or PhD thesis on ways to implement you know software management and all that sort of you know compiler you know design and all that sort of jazz so yeah he came up with he invented his own method for doing software development and Bill ready's thesis and went yeah that's how we want to do things at Microsoft and apparently they tried to implement it and found it didn't work that great in practice but hey he's a smart guy anyway yeah you know there you go

**Jeff Kaiser:** did you guys see this Intel a picture internal like of the die just crazy old RAM chip kind of thing I don't know if you guys I was saying a shift

**Chris Gammell:** register memory right yeah yeah yeah that's far out

**Dave Jones:** 1970s vintage yeah what sort of what sort of process geometry was that

**Jeff Kaiser:** I have no idea big like

**Dave Jones:** five micron or something you know

**Jeff Kaiser:** yeah that's crazy

**Dave Jones:** yeah very cool I love those tear downs yeah once again done the overlays on there to show you how it works and stuff like that so that's really quite neat very nice we'll definitely link that one in I'd love to do stuff like that but you know the chemicals to you know etch away at these and you really need a proper microscope you know you can't dick around you've got

**Jeff Kaiser:** like an x-ray machine put it in your new space Dave you could

**Dave Jones:** oh yeah I'll just yeah I'll just bid on one of those hundred x-ray machines that are always coming up on ebay here in australia yeah I guess

**Jeff Kaiser:** you have fewer of those huh

**Dave Jones:** I know they're dime a dozen in the states but here you know stuff like that is rare as hen's teeth

**Jeff Kaiser:** yeah you know

**Dave Jones:** I would love to yeah because I've got room to put stuff like that now it'd be fantastic but but they never come up you know I've had a few things you know over the last couple of years I've got oh I wish I could bid on that but I can't because I've got nowhere to bloody put the thing you know so but yeah I've never seen an x-ray machine come up that's for sure

**Jeff Kaiser:** maybe you could buy one here and we'll just like charter a boat and you can have like the nerd cruise shipping it over to Australia yeah

**Dave Jones:** oh goodness Jeff you got

**Jeff Kaiser:** any uh you pick up any sweet gear when you're at these swap that swap meet thing did you see any

**Chris Gammell:** I picked up a a Hameg digital slash analog oscilloscope on the last swap meet I was at and it was one of those ones it's actually got like a analog front end and you can use it in full analog mode or you push a button and it becomes kind of a basic like mega sample digital storage scope and it's kind of a neat scope I got it mostly out of a curiosity and because I kind of wanted an analog scope for home because I only had a digital and it it was super cheap because all of the front panel knobs had stopped working and it had become really intermittent and it uses rotary encoders and so I got it home and I pulled it apart and sure enough it used a rotary encoder that I could buy on digikey of all places like it was a very common part and so I stripped the whole thing apart and Hameg was actually nice enough they sent me a full service manual for it also and so I pulled it apart replaced all the rotary encoders and it's like a brand new scope like it looked like it had never been used it had just been stored and I guess moisture had gotten into the switches or whatever and so I picked that guy up and I'm pretty happy with that I've been playing around with that guy picked up some old vintage Heathkit stuff a lot of which I've since sold because I realized I didn't need that much old Heathkit stuff it's always so tempting when you go to the swap

**Jeff Kaiser:** meets and the ham fest and stuff like that and it's like oh that's so cool looking and old and you're like oh and I have like a $300 scope that's better than that you know what I mean it's just like yeah

**Dave Jones:** exactly that's a hundred times better yeah it's kind of pointless I keep

**Chris Gammell:** buying these like little baby oscilloscopes like Ico had I think it's like the 435 or 400 series there's these Ico I think they were kits that were sold in the 60s and 70s and they've got a little like 3 inch CRT they're tube based and they're really kind of cute and small and I keep buying them because they're always like five bucks and I'm buying them kind of hoping that at some point I will do a tube based scope project and maybe just turn them into like art so I've got a little collection of these guys but that's like that kind of thing that you start buying them and then they start piling up on the shelf and now in my

**Jeff Kaiser:** basement too

**Dave Jones:** that's not junk honey it's art trust me

**Chris Gammell:** I'm an artist it's not art yet but it will hopefully hopefully at one time when it's not like taken apart and covered in like you know 40 years of like sludge and grime hopefully it will be art but yeah I have to say like I'm probably compared to folks that I know I'm a little better about not collecting large amounts of stuff like that so when I go to the swap meet I actually bring a lot of stuff to sell and I'm like stuff that I don't want to be hauling around because I've moved a few times over the past few years for work or whatever and every time I've tried to like get rid of stuff but I've kept certain things now it's like yeah you know if it's not made before like the 2000s maybe I'm not going to hang on to it because just stuff like that starts to get kind of flakier and flakier and when you need it to turn it on and just kind of work it's it's hard there's some test equipment that I've I've got on my wish list that I'm hoping I can come across some good used ones at some point but I'm probably not going to find it a swap meet I've really fallen in love with Agilent's 4000 series well sorry key site key sites 4000 series scopes

**Jeff Kaiser:** that came out like you know five years ago or something well I mean there is a used market for that there is a used market for that

**Dave Jones:** the 4000 is very sexy to look at but it's a pretty disappointing because it's essentially just the 3000 with a bigger screen and some touch that's not true that's not true I've got one at work I've got one at work so I got

**Chris Gammell:** one for my office at work about a year ago what's the

**Dave Jones:** extra functionality that has that the 3000 doesn't

**Chris Gammell:** so first of all Dave I would like to review

**Dave Jones:** it's got

**Chris Gammell:** zone triggering so the zone triggering is awesome and I've used it a bit the touch screen is actually the surprising feature that I thought the touch screen would be kind of a joke when I got it like oh this is really silly like everything's got to be all mobile phony and be touch the touch screen is awesome like it is I use it every single day it is totally killer but the thing that really sold me on that scope is that the scope can actually do high speed USB packet data analysis triggering and signal quality so you can actually you can do USB in rush current testing you can do USB mask testing but more than that you can actually do well oh but I mean think about the number of like USB devices that people are developing particularly in the professional world everything's USB right so there's a lot of reason to want to be able to look at bit by bit and packet by packet USB and I'd say that just based on those features alone that's enough of a reason why you'd want one over a 3000 series and the 3000 series is a great scope but man once you get that big LCD and you get the touch screen but it's the same resolution

**Dave Jones:** that's the thing that pisses me off it's still the same 800 by 600 resolution you know that's

**Chris Gammell:** that's true and that's because of key I still have trouble saying key site HP's the engineering that HP and Agilent and Keysight they made that chip right and that chip does all the heavy lifting but I think that I haven't found that to be a problem really it's a beautiful scope so I'm waiting for those to become available on the used market and I'd love to pick one up I actually feel like between that scope and the Keysight Fieldfox combination network analyzer spectrum analyzer

**Dave Jones:** you could

**Chris Gammell:** totally start those two tools and there's so many free design tools for RF design now you could totally start an RF consulting business with just that equipment because they're so incredibly capable tools I've got to get the question

**Jeff Kaiser:** what are those tools just so we can list them out so people can go so that

**Chris Gammell:** the RF design tool that I've spent a bit of time so there's LTSpice of course which is incredibly useful mostly for analog and I think people have done RF design and LTSpice which I'm pretty impressed by but there's a tool called QUCS which stands for Quite Universal Circuit Simulator have you used that before? No I've seen you tweeting about it it's totally awesome how do you say it though is it QUX QUX I don't know ducks go QUX but between that tool and HP's old APCAD which is kind of a micro strip calculator tool you can use to do some simple stuff that's been around forever but this QUCS program you could totally do like filters synthesis impedance matching networks all that kind of stuff using free tools and it is amazing you can actually capture STP files which are S-parameter data files using the field fox and then copy them over to your PC and then actually open those up in QUX and use that to synthesize matching networks it's amazing I didn't know about that tool more than about a year ago I wish I had found out about it years ago it's been around for a while and actually there was a presentation by one of the guys that developed there's a low-cost European network analyzer it's one of those primarily kind of hobbyist oriented I think it's like one gigahertz ish maximum bandwidth network analyzer I wish I could remember the gentleman's name but there was a presentation he gave at a conference that listed a bunch of kind of free tools for like filter synthesis and RF design and it's getting pretty impressive like it used to be where you needed ADS or microwave office to really do any kind of RF design and I think you still kind of need those tools to do like professional level design if that's what you're doing all day but on the other hand you can do a pretty impressive amount with an Excel spreadsheet and some of these free design tools and I've been really impressed I've also done a bit of antenna simulation using NEC like there's a bunch of variants of NEC around which is a really old school antenna simulation package there's one called I think it's like easy NEC or for something easy NEC there's a bunch of Windows based derivatives of that and I've used that to synthesize some kind of simple PCB mounted antennas and had actually really good results so I've been just amazed by the quality of it you know and they're not the easiest to use but they get the job done awesome

**Jeff Kaiser:** yeah

**Chris Gammell:** yeah

**Dave Jones:** we had a couple of segues back there very quickly because oh sorry sorry guys the speaking of art and Heath kits we had a link on the forum I tweeted this one as well to some awesome electronic art check it out

**Jeff Kaiser:** yeah the clock it's just the building

**Dave Jones:** yeah the clock yeah the clock a little too late for Christmas

**Jeff Kaiser:** to build this for someone but maybe for next year someone could

**Dave Jones:** it's a bit like I'd love to know how many hours work he put into this but geez yeah it's stunning yeah maybe we can have that as our better photo for this episode or something maybe yeah anyway and also there's some Heathkit controversy

**Jeff Kaiser:** yeah we were talking about that and yeah we were talking about that's right

**Dave Jones:** and apparently there's a thing on Artifruit yeah about the history of the Heathkit and how they can't restart and they restart again and how nobody can find out any info about the person who's doing it and sounds all dodgy and yeah I don't know

**Jeff Kaiser:** I think Jeff kind of got to the point of it too it's like you know the magic of it was you were building a kit that was a good thing the downside was you were building it because you had to because there wasn't really many other options but these days there's so many good options

**Dave Jones:** so many cheap test instruments that's why I wouldn't buy I wouldn't do a piece of test gear as a kit these days it's just there's so few people that are going to want to build it really

**Jeff Kaiser:** I mean you'll learn something if you build it there's always that totally totally but it's not like

**Dave Jones:** it was back in the old days when the electronics magazines all they were filled with was test equipment projects because if you built your own it was great I sold thousands of my digital storage scope kit because back then you couldn't buy a digital storage scope so you built your own and you know that was massively popular and yeah I sold that for years and jeez it was yeah totally different these days so you know and why it's almost why even build your own power supply these days unless it's something niche for your own requirement you know because there's you know like a bit you know like just a simple you know 30 volt 3 amp you know your regular 30 volt 3 amp linear bench supply you can get them for like 50 bucks on ebay

**Jeff Kaiser:** yeah

**Dave Jones:** it's just scary

**Jeff Kaiser:** oh that's Dave's wife telling him it's time to go home for Christmas it's time to go home folks yeah folks all right we need to end it but Jeff thank you for coming back it was always great talking to you and yeah thanks for having me on the show it's always

**Chris Gammell:** a pleasure

**Jeff Kaiser:** can't wait to hear what's what the heck is going on with your professional stuff I'm sure we'll see stuff not at CES as Dave was very clear nice that was really that was really suave Dave by the way yeah thank you

**Dave Jones:** that's why I earned the big bucks yeah there they are again serious it's Christmas Eve here yeah

**Chris Gammell:** see you guys all right thanks all right thanks bye We'll see you next time.
