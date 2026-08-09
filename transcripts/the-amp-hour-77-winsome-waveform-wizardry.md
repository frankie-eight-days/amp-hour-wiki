---
episode: 77
title: An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry
url: https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/
---

**Chris Gammell:** This is the Amp Hour Podcast, recorded January 9th, 2012. Episode 77, with guest Dr. Howard Johnson, Winsome Waveform Wizardry.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life. Today on the show, we have a guest known not only for his writing, which is often featured in EDN, but also his writing in some of the biggest, best-known handbooks in high-speed digital design, often referred to as the handbooks of black magic. He also is a guest lecturer at Oxford University and is a full-time consultant. So we're really happy we could have him on the show today. Dr. Howard Johnson, welcome to the Amp Hour.

**Howard Johnson:** Thank you, Chris.

**Dave Jones:** Thank you very much for coming. It's awesome to have you on our show.

**Howard Johnson:** Yeah. It's a pleasure to be here.

**Dave Jones:** We're huge fans of the book.

**Howard Johnson:** Oh, good. Well, talking about high-speed digital design is my favorite occupation.

**Dave Jones:** It's probably one of the two books, The Art of Electronics being the other, where you just have to say, the book. And if you're talking about signal integrity stuff, it's like, it's the book. Yeah. High-speed digital design, a handbook of black magic.

**Chris Gammell:** Yeah, great title, too.

**Dave Jones:** Who came up with that title?

**Howard Johnson:** Well, that was my idea. I've gotten a lot of flack about it from university professors, mostly. Some of them have told me, basically, how dare you sully our subject by calling it black magic. Oh, man. You know, you're demented using that. And I think, great. They don't like it. Excellent. It's not their kind of book. Oh, that's awesome. It's a reference book for people who are on the job and need to know something. And there's a lot of other fine books that have come out in the, gosh, what's it been since 1993? So I guess it's been 18 years since that was first published. It's been quite a while. And there have been a lot of books in the area that have added to it.

**Dave Jones:** Well, you've got a follow-up book. Advanced Black Magic. I see you use the term again. You have to go for a double dip there just to rub it in.

**Howard Johnson:** I did. Yeah, that was a rubbing in thing. It really was.

**Dave Jones:** But is that kind of a piece? Because it's more math and theory oriented, I think, the second one, isn't it? The first one's very practical, just like the art of electronics. Math is kept to an absolute minimum and lots of tips and practical stuff.

**Howard Johnson:** The first book was a survey book, just to do a broad survey of the whole field of signal integrity. And the second book was just to focus in just on the propagation of one signal going down one track. What are all the things that can go wrong? If you're going fast enough or far enough that you have to worry about signal propagation. And so it has a lot more theory in it, which for some people who want to optimize their designs is fabulous stuff. Yeah.

**Dave Jones:** So was that book, was the second one actually received well by the academia?

**Howard Johnson:** Well, it doesn't have problems in it. So in terms of a college text, the people who try to use it to teach from, you know, they have to come up with their own problem sets. Right. So that's a big issue. It wasn't really intended as a semester course. They're both intended as reference works. You know, 800 pages. You can't do 800 pages in one semester. So it's intended to, when you want to know about one thing, then you go look that up and read a chapter about it. That's the best way to use it.

**Chris Gammell:** I'm sure most students would say that their teachers try and do 800 pages in a semester. But it feels in a way sometimes. Yeah, it definitely does. It definitely does.

**Dave Jones:** So speaking of the book, of course, what is the history behind it? How did you, when did you decide to do it? Why? How long did it take? And what's the history there?

**Howard Johnson:** A lot of questions. I'll answer the last one first because it's the easiest. It took 2,000 hours.

**Chris Gammell:** Wow. 2,000 hours.

**Howard Johnson:** It takes for me to write a book like that. Wow. Okay. That was about 400 pages. And it was a third of it is the writing, a third of it is the lab work, and a third of it is the post-production, doing all the editing and finishing work on the text to make that happen. So for those of you out there who are thinking of writing your own book, if it's a technical book, that's about what it takes. And unfortunately, at this point in time, our publishing industry is collapsing.

**Dave Jones:** Yeah. Right.

**Howard Johnson:** You won't get paid squat for writing a book anymore. So only do it if you love the subject. I don't know.

**Dave Jones:** And how long was that 2,000 spread over? How long was that spread over?

**Howard Johnson:** Oh, it was spread out over about two years. About two years. So we're talking about half time for two years.

**Chris Gammell:** I'd say 2,000 hours, you probably want to only write books when you're really, really into it in the first place anyways.

**Howard Johnson:** Yeah. Well, and I was. I had a good motivation for that one. I had, you know, I'd grown up with electronics all my life. I was a TV repairman at a young age. It got me started. Ham radio. Did all the things kids do. And then went to college and got a professional training in electrical engineering. Went all the way through a PhD. And at the time when I got out of school and was working professionally at the first big company I worked for, they were in California called ROLM. R-O-L-M. They made telephone equipment. Oh, yeah. Okay. And, yeah. Yeah. I was the original inventor of phone mail. It was the first voice messaging system. Wow. Excellent.

**Chris Gammell:** So you're who's responsible.

**Howard Johnson:** Right. Yeah. Well, in part, yeah. Yeah. It took a long time for people to accept that. But now it's ubiquitous.

**Chris Gammell:** And almost on the downside now. I mean, with email, it's almost, I mean, Google now translates or they transcribe.

**Speaker ?:** And texting.

**Chris Gammell:** Right. Yeah.

**Howard Johnson:** Yeah. All the Twittering and texting is really maybe surpassed it at this point. I'm not sure. But in any case, I met a fellow at ROLM named Martin Graham. He's my technical mentor. And he's a professor at Berkeley or was at the time.

**Dave Jones:** And the co-author at the book.

**Howard Johnson:** That's right. Which you're going to get onto.

**Dave Jones:** I was going to ask, who is Martin Graham? There you go.

**Howard Johnson:** Well, he was my mentor. I grew up at a time when engineers had, you would have a mentor who would teach you your craft. And I was lucky enough to get Martin. And he had been, gosh, he had been president of the Computer Society and an architect of some of the first tube computers that were ever built. And just had all this history about computer science and how things went together and the cycles that he would talk about in terms of, you know, fads and trends for computers. And so he did his best to teach me everything he knew about computer engineering, including all the high-speed aspects. And this took about 10 years. And that was his way. He would take one student at a time and work with them for a decade and teach them everything. But he never wrote anything down. Wow. He didn't write any papers. He didn't write any books. He didn't do presentation. He didn't do anything but work with students. And when he got ready to retire, I realized, that was about 1990, I realized that I had been his last student. And all the other ones were presidents of companies and marketing guys. And they weren't doing technical work anymore. Wow. That's crazy. And so I felt like I was the last one of his students that had learned this material. And I should, you know, somebody should write it down. So I decided to do it. And so I wrote the book, which was a huge effort. But I did it because of Marty, really. And then I put it on the shelf. I thought, well, that's it. I've written a book. Now I'll go back to my consulting career. And not six months later, I got a call from Oxford University. And they had read the book. And they called and they asked me if I could please come over and teach my class. They assumed that I was a professor. Right. And that I had a class. Yeah, yeah. And so I said, jolly good. I wrote up some PowerPoint slides and I went over and I taught a two-day seminar, which was the genesis of the seminars that I teach today. Right. Based on that kind of an outline. Updated, of course, you know, with time. But based on that and over the years, it's been 19 years now. This coming June will be my 19th year of teaching at Oxford in the summer program doing a short course. It'll be the or the course has been for about a decade the most popular summer engineering course they've ever had at the university. Wow. Fantastic. And we've tried to add to it. I've now got several other guys that teach over there as part of a series. We have Bruce Archambault that teaches electromagnetic compatibility theory and simulation. We have Lee Hill teaches practical EMC mitigation. We have Doug Smith teaches instrumentation. And those courses kind of, you know, go with mine and people take them in any order and go around the loop learning, you know, more and more about high speed stuff. It's a fascinating program and the only place in the world where you can go and get that much concentration in that one subject area.

**Dave Jones:** I've got to admit, I don't know anyone who's actually graduated engineering from Oxford.

**Chris Gammell:** Yeah. Do they have a regular program there?

**Dave Jones:** Do they just magically disappear and become CEOs of companies and you never?

**Howard Johnson:** No, there aren't any. There's very few. And I wondered, you know, because of that, they have a great, you know, science department. Biology, I think, is really strong. And they have huge political science. And some departments are just great over there. But in terms of electrical engineering, it's a very small department. Right. So I wondered why in the world would they want to have my course? And I finally came to understand that you don't get to continue as an educational institution for 800 years unless you're constantly looking for new things and trying them and bringing them into your organization. And having these two-day seminars was their way of starting to see, well, is this popular? Is this something we should do? And so now they have mine and Bruce's and Chris's and Doug's. And we're building a subject area. They've also got a strong program in the summer in telecommunications, you know, all sorts of cell phone protocols and RF design techniques that they have cobbled together that they don't teach to undergraduates. It's just in these seminars. And I think eventually, you know, that may translate into a whole department forum. I think this is how they acquire new subjects.

**Dave Jones:** Okay. So this is like an industry thing where you pay to attend this class. It's mostly outsiders, is it? Or do you set it up really for graduates? Yes, that's correct. So you've got to pay to do it.

**Howard Johnson:** It's a, you know, continuing education program. Right. Okay. Kellogg College. And they bring, in fact, it's primarily people from all over Europe in the EU that come to England in the summer to take these classes.

**Chris Gammell:** So everybody sign up now. There might still be spots if you're lucky.

**Howard Johnson:** Well, you know, sometimes people ask me about where they can see one of my courses. And I always tell them, well, I teach around the U.S. We do public classes all the time. But that if you really want a treat, tell your boss that those are all full. Yeah. The only one I have a seat in is you have to go to the Oxford. Sorry. I got it.

**Chris Gammell:** And, you know, there's only one place to stay is the local pub. They have rooms upstairs.

**Howard Johnson:** They've got some great places to stay over there. It's a beautiful city. I always enjoy going.

**Chris Gammell:** That's amazing.

**Dave Jones:** I've never been there, unfortunately.

**Chris Gammell:** Yeah. I'm mostly a U.S.

**Dave Jones:** I live on the opposite side of the planet. Yeah. It's not often that I can convince my employers, previous employers, to send me overseas for a course. The furthest I've gone for a course is Melbourne, you know. And that took about three years to try and extract that out of them.

**Chris Gammell:** Well, Dave, you should ask your new employer.

**Dave Jones:** Yeah.

**Chris Gammell:** My wife, right? That's... So now you're teaching... Howard, now you teach locally. You said all over the U.S. And you're based out of Washington. Is that right?

**Howard Johnson:** Yeah. I'm in Washington State. You know, people think of Seattle when they think of Washington. Well, there's Seattle. And then there's a range of mountains. And on the eastern side of the state is the dry, sunny side. It's where I live, really high up in the Cascade Mountains near the Canadian border. I'm in a small town called Twisp, T-W-I-S-P.

**Dave Jones:** I had a look at that on the map. It looks like it's some sort of open area test site in the middle of nowhere. Is that actually your house, the address you put on the website?

**Howard Johnson:** It is in the middle. And we live in a large horse pasture. Right. And surrounding us is state and federal park on three sides. So it's a pretty isolated spot out here.

**Dave Jones:** It'd be an isolated RF. I think it'd make a great open area site for EMC testing and stuff like that, would it not?

**Howard Johnson:** You know, it's really good for snowshoeing and cross-country skiing, too.

**Speaker ?:** Right.

**Chris Gammell:** And why not carry a Yagi antenna while you're going out that way? Why not, you know?

**Howard Johnson:** Yeah. You could. Yeah. I tell people who visit that you can't get cell phone service out here. Right. And so they won't bring their cell phones, so they won't turn around. Actually, it works fine. But I just don't want them to be interrupted constantly when we're talking about something. That's smart. That's smart.

**Dave Jones:** Oh, I'll have to do that. I have to tell all the Yanks who come here, oh, cell phones don't work in Australia. You just don't bother bringing them. We don't even know what they are yet.

**Speaker ?:** Right.

**Dave Jones:** So have you always lived there?

**Howard Johnson:** I've been here for 13 years.

**Dave Jones:** Right. Is there any temptation to move to Silicon Valley? Because I can imagine being... If I was to move to the U.S., just the sheer... You know, that's just where it all is. Is there been temptation there to do that?

**Howard Johnson:** Well, I did. That's the place to go seek your fortune, really, as a young person. I think it's the best place in the world in our industry. In fact, my daughter, when she graduates from Carnegie Mellon, will end up in Silicon Valley. I'm sure she's going to be there this summer as an intern. It's a great place to go. And I was there for, gee, from 79 through about 93, you know, living in that area. And eventually, when we had kids, I started thinking seriously about where we wanted to raise them. And my wife and I wanted to be in a smaller community. So we ended up here.

**Chris Gammell:** Fantastic. And now you're able to consult remotely. Is that right? So that's how you're able to kind of bridge that gap between middle of nowhere. And I'm guessing you still talk to a lot of those big Silicon Valley companies, right?

**Howard Johnson:** Yeah. Yeah. All the time. You know, I travel out. We try to hold it to about eight trips a year. Oh, that's good. Because it's a long way to the airport. It's about a five-hour drive to get to the SeaTac airport. Ouch. Wow. Wow. Yeah. But I only do it eight times a year. Yeah. Okay. So actually, on average, my commuting time is only about, you know, 10 or 12 minutes a day. It's all that works out. It's not that much. That's smart. It just comes in big chunks. Yeah. But then when I get out on the road, I try to do a lot of stuff. So I'll teach a couple classes or I'll go here and there and consult and do. Well, now you can do as much as I can while I'm out.

**Chris Gammell:** And now you can listen to the Amp Hour on your way to the airport. So added bonus for you there. Yeah.

**Howard Johnson:** You've listened to five episodes on the way to. I can. This sounds good.

**Chris Gammell:** All right.

**Dave Jones:** So we never got around to how many copies of the book have been sold? Do you know?

**Howard Johnson:** Do you have any idea? Oh, yeah. Yeah. Over 100,000.

**Dave Jones:** 100,000. Wow. Wow.

**Howard Johnson:** And, you know, what strikes me is there's only, at any one time, there's only about 70,000 high-speed digital engineers, you know, or digital engineers at all, really, in the world practicing. And so it means that it's really what that really tells me is that turnover is very high in our industry. You know, guys get out. They work for seven or 10 years. They burn out. They become salespeople or something else. And they're not doing digital design anymore. And I wish that weren't true. When I speak to EMC audiences, I don't know if you've had this experience, but for a while, when I was working in Ethernet standards, I went to a lot of standards meetings. And when you're working on a big standard, I was the chief technical editor for Fast Ethernet and Gigabit Ethernet. And when you do that, you have to go to other standards groups and do these presentations to make sure you're not stepping on their toes in the standards world. Yes. So you had to go to every other standards group in the IAAA and do a presentation about yourself. So I stood in the back of the room in every group, you know, the protocol group and the wireless group, you know, all these different groups. Anyway, when I got to the wireless networking group, it was a bunch of RF guys. And from the back of the room, you can tell instantly because most of them are bald.

**Speaker ?:** They're right.

**Chris Gammell:** They're wearing handcaps and everything else, right? Yeah.

**Howard Johnson:** And there's a reason for it. It's because EMC professionals on the whole, in my experience, do a better job of educating themselves on the job than any other IEEE group. They have the strongest societies. They go to the most lectures. They read the most books. They keep up to date the most. And as a result, they are able to keep doing the job they love to do their whole careers.

**Dave Jones:** Interesting. I'm not terribly surprised by that, though. That doesn't... All the EMC guys I've ever dealt with are all, you know, dare I say it, old. You know, they're the old graybeards. They're, you know, they've been doing it forever and they know this stuff. You know, I've never met some young up-and-coming EMC guy. It's just, you know, in my limited experience anyway.

**Howard Johnson:** It's a whole different world for them. I think the education is really the key. I admire that very much on their part. So what do you think?

**Dave Jones:** Because it's not something you can learn very quickly and become an expert at. I think you've got to really have those years of on-the-job experience. I think so, too.

**Howard Johnson:** I think the ability to do experiments and try things and see what really works in your application is key to learning anything that has to do with fields and waves. And the older guys have had that time. And so they're the most experienced. So what are we going to do in the high-speed world? We have people designing, you know, serial lengths at 5 or 10 or 20 gigabits per second. And a lot of them don't have any clue what a magnetic field is or what influence it has on their circuit or how to think about it or what sort of problems they're likely to encounter. And there's nobody to teach them. We don't have mentors anymore. And when was the last time you heard somebody talk about, oh, my mentor, you know, told me this.

**Dave Jones:** Yeah.

**Howard Johnson:** We don't do mentoring at technical companies. We don't have Bell Labs anymore where the central place where that used to happen is gone.

**Chris Gammell:** You know, I just wrote about that actually yesterday about just the trickle-down effect of that. You did, yeah. Of, you know, Bell – and I wonder what's going to happen in about 30 years. You know, right now we're seeing a lot of the carryovers still, right, of that great work that is done in Bell Labs and other big research labs. And we're still kind of riding that high. But what happens at 30 years from now, really? I mean, like, you know, when we run out of juice, you know, I'm not sure what's going to happen. So I think the mentoring is important, but I think there's bigger components to it too. What kind of – are you able to participate in mentoring from a distance, Howard, or how – I mean, are you –

**Howard Johnson:** In some cases it works out. Occasionally, you know, when I'm working with a company, what I always tell them is the best way to use – well, really, any consultant – is to identify somebody on the inside that they're going to teach and have the consultant come in and do the work and teach this person how to do it at the same time. And I've talked to a lot of consultants who feel like that would be undercutting their business. Like they don't want the product to know how to do their – And my feeling is if you're good at what you do, you know so much. You could teach for a decade and the person on the inside still won't know everything that you know. Right. And that – so I don't think you give anything up by trying to help them. So that's what I always try.

**Chris Gammell:** And I think even in any kind of relationship like that too, you have – you know, like you still want to check in with that master, right? You still want to know what's going on with them. So I don't know. I think it's not that big a problem if you're really teaching because that's going to be a much bigger deal in the coming years as well.

**Dave Jones:** Well, and I've got a feeling that – like I've had a couple of maybe you could call mentors on certain things. And you always knew that even though they taught you all that stuff on the topic, you always knew that they knew more than you ever will. You know, that's always – you know, you always got that feeling that, you know, oh, no, you know, I'm the master now. And, you know, I'm smarter than my mentor. And it just – you just know that that's not the case. Although it could be. But, you know, that's the feeling you get anyway. We should get into some questions.

**Chris Gammell:** Yeah, we have tons of great questions from our listeners and great questions from me and from Dave.

**Dave Jones:** Well, I'm game for anything. Let's start with the – let's start with our listeners. Okay. That's a good idea. Yep.

**Chris Gammell:** So let's start with the cosmic ray question. We mentioned this briefly before we started the show. One of the questions came from Adam Ward. The question was, does the high-speed electronics industry have to deal with problems caused by cosmic rays interfering with the operation of sensitive circuits? And if so, can it be proved that it causes a razor to blame?

**Howard Johnson:** I'd say yes, we do in space, absolutely. And for the last couple of decades in satellites and ballistic missiles and things of that type, there's been a lot of research by the military about what does it take to have something that's reliable in space? And what we observe is that if you send up a computer system with a bunch of memory in it, that over time, the bits get flipped. The Voyager spacecraft, in fact, I was just reading in the last – I don't know, within the last year, had a bit flip in it somewhere. And they were able to get things back. And then they assumed that it was a cosmic ray. Now, that's an assumption. I mean, nobody had a cosmic ray detector that could prove it. But what we know is if you shoot cosmic rays at memory, you get a certain percentage of flips. And if you measure the density of cosmic rays in space and you predict what you think is going to happen, that's what happens. So our reaction to it for space applications mostly has been you make great, big, honking memory cells. Yeah. So that instead of, you know, 50 electrons stored on a gate somewhere, you've got, you know, 50,000 electrons stored on a gate. And so it takes a lot harder hit in order to knock that thing off balance. Right. Another strategy is you make redundant memories. You just triple them. Just have three of them.

**Dave Jones:** Yeah.

**Howard Johnson:** And then if a bit gets flipped, you've got a good chance you can get something back.

**Dave Jones:** Or do a combination of both. Yeah. ECC.

**Howard Johnson:** Yeah, that's right. Error correcting codes are extremely effective at combating that sort of thing. And you can detect it. You can see it. You can even put it back and, you know, get the bit back to where it should have been over time. Refresh is really important. If you're doing some sort of, wow, what's that weird sound? I'm not sure. I don't know. It's not me. It's not me. It's gone. Okay. Refresh is really important. If you're doing a FPGA-based design, for example, using a Xilinx part, you know, you're supposed to load in the program and then it runs, right? Yep. Well, in space, you need to load the program in periodically. Just keep resetting it, reloading the program to make sure it's always fresh. Right. So if anything went wrong, it automatically flushes through and it keeps working and doing what it's supposed to do. Okay. Those are some of the things that we do. You know, as part of this, using larger cells for memory means that you're several revs downgraded from the latest and greatest memory technology. Yeah.

**Dave Jones:** Yep.

**Howard Johnson:** So in space, they're never going to catch up and go as fast or as small as what we're able to do for, you know, the atmosphere shields us against a lot of the cosmic rays that come in. And so our flux here on the Earth is a lot less than what it is in space. That's the whole...

**Dave Jones:** But it's not completely, though. So we get cosmic ray effects here on Earth. They've been measurable and apparently. And it's based on stats. It's all pretty much a statistical thing. You can never really, you know, know for sure. You can just say, you know, with X percent of certainty, we'll get a bit flip every 10 years or something.

**Howard Johnson:** Mm-hmm. Yeah, it's totally unpredictable where or when it could happen anywhere. Shielding doesn't make any difference hardly. It doesn't matter what you're... You know, it's cosmic rays. It'd be a big shield. You'll through almost anything and explore wherever they want to.

**Chris Gammell:** They go through the entire planet, don't they? Yeah. So of those things you mentioned, Howard, the FPGA, memories, you know, space electronics, are those among your customer base? I mean, are those the kind of people you're consulting to? I mean, obviously, memories are moving to very high speeds as are FPGAs and processors.

**Howard Johnson:** Well, really, anybody that's working with high-speed electronics is the sort of person that I run into. There's people working on high-end servers. There's networking is a huge section. But military electronics is certainly really important. And they, in the last, you know, 20 years, have... I don't know how I want to say this, but if you go back in time, go back to year 2000, at that point, the military was maybe 20 years behind in terms of electronics technology deployed in the field.

**Howard Johnson:** Compared to commercial applications. And you look at now, and maybe they're only five or 10 years behind. Interesting. That means in the last 10 years, they accelerated more than twice as fast as the rest of the industry. I'm surprised they're behind at all.

**Chris Gammell:** I kind of had the notion that, based on, you know, large funding, that they would be ahead. But I guess that's not necessarily true.

**Howard Johnson:** No. Okay. It doesn't really happen.

**Dave Jones:** Well, they don't have very long cycle times, long development cycle times and things like that, where you have to lock stuff in early and, you know...

**Howard Johnson:** And really low volumes. Oh, yeah. If you work at Nokia and you do a design, and then, you know, 200 guys will spend the next three years optimizing the design and squeezing it and making it better and better and better and better and better. And in the military, you make one design, you're done, you go on to the next thing. You don't get to optimize or go back. You don't have time for that. You have some other crisis you have to respond to. And so, yeah, I have a lot of sympathy for them. But my experience is that in the last 10 years, they've gone through a huge educational upgrade to try to catch up as close as they can, and they're still not quite there. Okay.

**Chris Gammell:** So speaking of catching up and kind of hitting barriers and such, we're kind of seeing faster and faster levels, obviously. I mean, whereas CPUs kind of started to kind of flatline and even scale back because of power limits and such like that. I mean, digital communication seems to keep on increasing. So we had a couple questions. One was about the limits of Ethernet, which you seem very well informed to answer based on your involvement with the standard. But also just, you know, where are we going with general trends and what kind of limits are we going to reach in the near future?

**Howard Johnson:** God, faster and faster over the expected career lifetime of everyone listening to this show. So we can assume, now, okay, career lifetime is only about seven more years for an average guy. That's what you've got left.

**Dave Jones:** That's true, yeah. Right, yeah. Before you go into management, yeah. That's all that really matters. Right.

**Howard Johnson:** And over that span, you can assume that things are going to go faster and faster every single year. If you look at the international technology roadmap, which I think has been really one of the most effective marketing prediction tools ever on the planet.

**Chris Gammell:** Wow.

**Howard Johnson:** They're still predicting speeds going up and cell sizes shrinking and memories exploding into huger and huger sizes for the next decade easily. They don't see anything stop. Now, eventually, sure, we'll reach a limit. And I will point out I've been hearing that since I started in the business in 1975, that we were going to hit a limit or something would happen or, you know, photons are only so big you can't do lithography smaller than that. Well, now we use x-rays. Right. You know, we do things to change and it's not a limit.

**Chris Gammell:** It's the only constant, right? The only constant is that people keep saying that.

**Howard Johnson:** Yeah.

**Dave Jones:** In terms of serial communication, what can gain you the big advantages or what has gained the big advantages over time? Is it manufacturing technology of connectors? Is it manufacturing technology of cables and, you know, that sort of stuff? Or is it transceiver technology? Is it protocol technology? What is the – I assume it's a combination of all of them.

**Howard Johnson:** Primarily, I think it's been the silicon. It's been getting faster. Right, the silicon. So it's the transceivers. The individual transistors inside can switch way faster than they ever could before because they're smaller. Going small is good for that application. The connectors, we've always known how to make a connector go as fast as we want. You just shrink it. Yep. You take any connector that performs at some level and you shrink it by a factor of 10. It's going 10 times faster. There's no question about that. Right. In physics. And so as long as we have the ability to shrink the connectors, then we can keep going fast. Now, some things change in the way we make them. Like we used to make connectors that had individual pins sticking out the back that right angled and went down into the PC board. And so the pin hanging out in space is not a real favorable geometry. If you take the pin and you put a reference plane next to it every place where it goes, that works better. So connectors have that. Yeah. Or that works if you put the connector down right tight against the board so the pins are naturally next to the reference plane. That helps to make a more consistent transmission environment. And that makes them work better. And that was a really good idea. I'm glad we do that. But fundamentally, shrinking and making the transmission path smoother and more consistent everywhere it goes is the key to making connectors work. And that's not difficult. Now, the materials is a different story. The size of the wires determines your skin effect loss. And the material from which you make the dielectric determines the dielectric losses. And so if you use big, fat wires with really good dielectrics, you can go like blazes, but it's very expensive. If you want to make little, bitty, tiny things with small wires and you want to use crummy, ordinary, plain old FR4 materials, then that's limiting how fast and how far we can go. It's kind of like a speed distance product. You know, if you want to go a gigabit at 10 inches, it's not a problem on any reasonable PC board material. You can do that. So if you want to go 10 gigabits in 10 inches, well, then we have to start thinking about our materials and what we do. And if you want to go 100 gigabits, it becomes a serious problem. Eventually, what we'll have to do to get around that, I think, is we'll just have to go to optical, you know, to photonics, fiber optics, in order to overcome the limitations of our printed circuit board materials. And, you know, I've been waiting for that to happen for a long time. Come on, guys.

**Chris Gammell:** Come on, Intel, right? Come on, board makers.

**Howard Johnson:** It hasn't happened. Yeah. You know, I hear more rumors about it this year than ever before.

**Chris Gammell:** Oh, CES is going on now. I'm sure they're, well, they're probably actually talking about tablets. Never mind. So disregard all that.

**Howard Johnson:** You'll see it in backplanes for high-end servers is the first place that you'll see it. And, you know, whatever trends we have in transmission, first you see them in long transmission lines, and then you see them in shorter interconnections, and then you see them in backplanes, and then finally you see them between chips, and you see them on chip. It's sort of a natural progression of how things work. And so do we have fiber optics in long lines? Yeah, sure. We've had that for a long time now. And so the next step is fiber optics on the backplane. And getting connectors that work on the backplane, and getting the power down on the transceivers are the two things that we've been working on to try to make that happen.

**Chris Gammell:** I hope it does happen. Can I get a clarification real quick just from what you said there? Because you were talking about the speed of – were you comparing connectors versus the PC board? Because you said smaller connectors means you can go faster, correct? Or smaller conductors of a connector. But then you also said you needed larger channels on a board?

**Howard Johnson:** Oh, yeah. Well, let's see if I can straighten that out. When you have a significantly long channel, then the size of the conductor really matters. If you have something like a connector, which is typically just a couple of tenths of an inch long, then there's not enough loss even in the wires to worry about because they're so short. And so then it's mostly just a matter of whether you've maintained a consistent characteristic impedance as you move through. There's a consistent relationship between the signal conductor and the return conductor. If that relationship is consistent in the same spacing every place you go, then your signal is going to propagate just fine, and that's the connector problem.

**Dave Jones:** And you don't have to worry about the DC loss. You don't have to worry about the resistive loss in the copper, the impedance loss in the copper.

**Howard Johnson:** Not really. You know, I can make a connector. Inside the connector, yeah. I could take most connectors and I could make them out of nickel, and they'd work fine because they're so short.

**Dave Jones:** Because it's so short comparative to the rest of the transmission line. So the impedance matching is the key.

**Howard Johnson:** That's right. You don't want to have reflections off your connector. That's the thing we want to do. And we don't want to have crosstalk on our connector. Now, crosstalk is something that I think I would like to encourage connector manufacturers to do a better job on. Crosstalk is adequate for doing binary transmission through connectors today. But that's not what I want to do. I don't want to just send one bit in every BOD cell. I want to send, you know, four bits, which requires going, you know, having 16 levels. And if I have a 16-level signaling, you know, you can send four bits of information, and you're not going any faster, so the bandwidth requirements aren't any higher. But the crosstalk requirements become 16 times more stringent in order to make that work. Because a loud channel can interfere with the little tiny levels on the channel next door. And so if we can improve our connector crosstalk performance by a couple of orders of magnitude, then suddenly we'd be able to use multi-level signal constellations. And that would really boost up our speed and allow us to continue using nice, cheap, old, copper, simple PC boards for a lot longer.

**Dave Jones:** Only a couple of orders of magnitude. You're not asking much there. Yeah, that's all we need.

**Chris Gammell:** Do you see in the future then, that's almost like a transition back to analog then. If you take that to the extreme, then if you go from not four channels, or 16 channels, or 16 levels rather, but you go to infinite, right? Then you approach an analog signal again, correct?

**Howard Johnson:** Well, yeah, kind of. You know, Shannon's theory tells us a lot about the range of possibilities between analog and digital, and what signal-to-noise ratio means, and how that affects how much data information you can possibly transmit through a channel. What we've done with our connectors now, with the high-level crosstalk they have, is you've limited the signal-to-noise ratio. So that eliminates a lot of possible signaling strategies you could otherwise use that would be better. And I want to get that signal-to-noise ratio improved a lot so we have the ability to use Shannon's theorem to really boost our data rate.

**Chris Gammell:** That's interesting because that's almost the knob that you're talking about when we hit that wall. That might be where people turn and just start saying, well, go multi-level because that's all that's left, or that's what makes more sense.

**Howard Johnson:** That's what we have done in every communications system that's ever been made by mankind. If you go back, I have, let's see, I'm trying to think of a name.

**Dave Jones:** Does that include fiber?

**Howard Johnson:** A history, well, I'm going to go back into prehistoric times. Oh, excellent. If you look at woodcuts that show men signaling on the battlefield in 300 BC, this was in History of Data Communications. This is great stuff. It shows guys with torches. You know, you're holding torches up. And to make it work, you erect a wall. You stand behind the wall. Your torch is either visible above the wall or not. So you can blink it on and off really effectively. Nice high contrast ratio. And the guy on the other end of the field can see you. And you can signal with sort of a, well, a Morse code.

**Chris Gammell:** Yeah, a Baudot code or something similar, right?

**Howard Johnson:** Yeah, right. They had some, you know, code patterns they would do to signal things to the other end. And then there was another wood cut from a couple hundred years later that showed a wall, eight guys behind the wall, eight torches doing different patterns. You know, it's the same signaling rate. They're just seeing more information. More information. Yeah. It's brilliant. And then when we went into the era of telegraphs with Morse code, that was, what, 1838? We got our first telegraph demonstration, and it was binary. And over time, as people install lines, if they would put in a line, let's say, from Philadelphia to Boston, they'd have a lot of traffic. The traffic built up. And it got to the point where one telegraph operator could not send all the messages in 24 hours, you know, to satisfy the demand. And so the operators had to have a way to send more stuff. Well, you could put in another line, but, of course, the lines were expensive.

**Chris Gammell:** Yeah, it's a lot of copper.

**Howard Johnson:** And so they decided, it is, they decided maybe we can send two signals on one wire. And so they came up with a duplex arrangement that one guy's key would control the polarity of the signal on the wire, and the other guy's key would control the amplitude, either strong or weak. And so with those two, you had four different things you could do, and they could separate it out at the other end, and they could get, you know, transmission to work. And then, and so that was a, you know, now we got a four-level signal going on the telegraph wire. And, of course, they sped it up even more. They used paper tape to record the individual telegraph operators. So if I was an operator, I would be beeping, you know, as fast as I could. It records it on paper tape. And then they would take the paper tapes, and they would put them into a high-speed player, and they would all the bits down to the other end where it was recorded on paper tape and then spanned out to a bunch of operators and played at slower speed. And so they multiplexed in time that way. They multiplexed, you know, with multiple levels. And then they were able to arrange circuits. They could go in both directions at the same time on the same wire. So they could get double use going two directions on the same wire. And so that was, you know, this is a long time ago. And people hit on the idea that if you make the circuitry at the ends of the wire more sophisticated, you can pump more data down the same wire. And then in the telephone world, we got 300 baud modems with some of the first ones. I mean, I can't imagine trying to surf the Internet on a 300 baud modem today.

**Dave Jones:** I know. It was painful back then.

**Howard Johnson:** Oh, it was. It would be horrible. I wasn't around. But we did that. And then we made them. Yeah, you were in poor, sonny boy. We made them faster and faster and faster. And we did it by adding more and more levels to the signal until finally we have, what is it, like a QAM 256-point constellation is the standard thing that we transmit on a, you know, 24-kilobit modem over a phone line. If anybody does that anymore, that's what we use. It's happened on every media. In fact, in the Ethernet world, gigabit Ethernet on ordinary category 5 plus UTP is a five-level signal.

**Dave Jones:** Right.

**Howard Johnson:** So they get two bits transmitted in each baud on each wire pair. This is the way things evolve. And it's got to happen. Now, I've been thinking this was going to happen for a long time, and it hasn't. I first, you know, thought, oh, this will happen on backplanes back in, oh, what was it, 1997. I started working with accelerant networks, and we made a 10-gigabit transceiver that worked on, you know, an ordinary backplane.

**Chris Gammell:** Who did it talk to?

**Howard Johnson:** Well, there wasn't anybody else at 1997 that could go that fast. Yeah, it was totally useless. That's a heck of a cornering of the market. Folded. Yeah. Yeah, cornering of a market that didn't exist.

**Dave Jones:** With the gigabit Ethernet development, how did that come around? Because you were, what, the chairman of that group?

**Howard Johnson:** Not the chairman. In the IEEE, there's a huge structure of organizations. 802 does all computer networks. 802.3 does Ethernet-type standards. And within 802.3, it was 802.3U and X and Z. Right. Do various things. Well, one of those was fast Ethernet. One was gigabit Ethernet. And within those, there's a chairman of the committee that handles the political work, and there's a chief technical editor that's responsible for identifying technical flaws and getting them fixed. And so that was my role as the chief technical editor.

**Dave Jones:** Okay.

**Howard Johnson:** And then the thing that made the Ethernet standards work so quickly and effectively is there was a shadow organization formed of…

**Speaker ?:** Ooh.

**Dave Jones:** Ooh. This sounds good.

**Howard Johnson:** Yeah. Formed of…

**Dave Jones:** They may kill you if you talk about it, but let's go.

**Howard Johnson:** Well, it's part of the way it works.

**Chris Gammell:** Five-hour drive to the airport, though.

**Howard Johnson:** It's all the marketing guys. It's the guys who used to be engineers 10 years ago, and now they're in the marketing department.

**Chris Gammell:** All right.

**Howard Johnson:** And their function, besides publicizing the existence of the standard and making sure that their companies are designing things compliant with it, part of their function was… You ever been in a meeting and there's one guy that, like, takes all the time in the meeting and doesn't contribute anything?

**Chris Gammell:** Every week. Every week, Howard. It's an internet meeting for me.

**Howard Johnson:** And you wish that somebody could just, like, grab them by the neck and throw them out of the room.

**Chris Gammell:** Yeah. Yep.

**Howard Johnson:** And so, if we had this shadow group and one of their functions was we could call their marketing people and we could say, this guy is getting in the way. And they would strip his funding and he couldn't go to the meetings anymore. Wow. Brilliant. It was brilliant. And it worked on everybody except for one guy. There was one guy whose name I will not reveal. That's fine. We'll call him Ernie, just to give him a name. Ernie. Ernie was a problem. He was just using up way too much time in the committee meetings. And so we made the call and we asked him to take him out. Make the call.

**Chris Gammell:** Take him out. Just take him out. He sounds like a Tom Plancy novel.

**Howard Johnson:** This is great. It felt that way. And so at the other end, there was this long pause. And then after a minute, they said. This is Ernie? This is Ernie. This is Ernie's company. Because we called this marketing guy at his company and said, take Ernie out. And the marketing guy finally paused and he said, why do you think we send him to your meetings? Because they couldn't stand having him on the plant. This is how they got rid of me. This is great. Oh, no. This is great. So what we had to do in the group, there were nine sub-editors in this group. Because it was a massive standard, 450 pages. And so I had nine sub-editors working on different groups, the areas of the standard. And so every night during the big meetings, we would draw straws. And one of us would have to take Ernie out and get him so drunk that he wouldn't be able to report in in the morning. And so his committee would be able to get some work done from about nine until 11 when he showed up.

**Chris Gammell:** Wow.

**Howard Johnson:** And so they had all their good, productive work done in that little two-hour window that we were able to give them each morning. It was –

**Chris Gammell:** That's like putting the tape on for the kid, you know? Like, oh, put on the tape. We need to get some stuff done around the house, you know?

**Howard Johnson:** Yeah. Yeah, it kind of is. And Ernie just thought he was so popular. Everybody wanted to go out with him. It was a great –

**Howard Johnson:** It was a brilliant approach. So was there one – Sorry. No, continue. We got those standards done in two and a half years each.

**Dave Jones:** Right.

**Howard Johnson:** Which compares to, you know, ATM was like 15 years or FDDI was, you know, 12 years and never got finished. And two and a half years each. And I think it was because of that organization in a lot of ways.

**Dave Jones:** Wow. Was the technology done before you – or sort of in place before you started going, right, we're going to use this technology to get to gigabit Ethernet? Who made that technical decision that that's the method you're going to use to do that?

**Howard Johnson:** Well, it was a pretty –

**Dave Jones:** Is it a group thing or is there one genius who goes, I'm sure, you know, strokes his gray beard and go, this is going to work, trust me? And that's the one you went with.

**Howard Johnson:** That's the way it works. Yeah. Well, actually, there's two or three people who agreed at the beginning that in each case that, yes, we're sure this is feasible and mapped out a matrix of approaches that could be combined together to work. And then –

**Dave Jones:** But it hadn't been tried at that point.

**Howard Johnson:** Pieces of it had been tried. Pieces of it, right. It was all existing and there wasn't anything that we thought was, you know, too hard to develop.

**Dave Jones:** No showstoppers, yeah.

**Howard Johnson:** The problem after you've got that matrix of ideas is to slowly reveal it to your technical group in a way that gets them to all feel like they've all contributed and they've all made decisions about what to do.

**Chris Gammell:** Human nature coming and rearing its ugly head again, huh?

**Howard Johnson:** Well, it's a wonderful thing because this is part of building consensus. You know, if you go to a meeting and let's say – in part of that meeting, somebody says, oh, my gosh, there's this terrible problem. You know, this will never work. What are we going to do about this? And the reaction is, well, we'll study that at the next meeting. Okay, so the next meeting comes around and let's say you have five different companies that all have presentations showing the same possible solution and all saying that it's going to work. And the people that were worried about the problem haven't studied enough to have anything coherent to say. Well, what are people going to vote for? They vote for the thing all these guys say is going to work.

**Chris Gammell:** Yeah, yeah, yeah.

**Howard Johnson:** And you've made progress. And so as long as you have in your back pocket enough ideas for how to make it work, then when you hit a crisis, you disseminate your next idea. You say, okay, next meeting we're all going to work on this. And if they all come back and they've done their work and they all agree it works, then you're golden and you can get your standard done.

**Chris Gammell:** For all the students out there listening, this is also a guide how to succeed in the workplace. If it's a covert guide how to succeed in the workplace, I think Howard has it right.

**Dave Jones:** Deal with it is real. I keep telling you. Deal with it is real. Well, you must deal with it.

**Howard Johnson:** It takes a lot of thought. You know, if you've ever tried to get three engineers to agree on anything, you know what a task that could be. And you imagine 450 guys that all have to agree. It's essentially a consensus process. If somebody really objects, then you have to go back and start over. You have to get them to all agree that this is good. Yeah. And that's kind of what it takes. Yeah, you've got to start with the winner.

**Dave Jones:** You've got those brainstorming sessions where, you know, somebody's running this brainstorming session. It's full of engineers and somebody has to present their idea. And one of the rules of the brainstorming session is that you're not allowed to say anything negative about the person's thing. You've only got to say positive. And you've got to zip your mouth. You know it's not going to work, right? Dave's biggest challenge ever. I was about to say it. Yeah.

**Chris Gammell:** Oh, I love it. Yeah, that's great.

**Dave Jones:** We've got another question. Yeah, good. Which I think is a really good one from Eric Smith.

**Chris Gammell:** Yes.

**Dave Jones:** Hey, Eric. And he says, well, I'll read out the whole thing. Now that so many of the newer ICs have adaptive pre-emphasis and equalization on their lanes and receivers that can function with practically no eye, as in the eye diagram, it is still important for the typical PCB engineer to understand high-speed digital design. First question. You know, links. There's three or four questions.

**Howard Johnson:** A lot of things at once. Let's see what I can do with that. First thing is the adaptive equalization is a fabulous technology. I love it. And you can do a lot with it. Second thing, it has limitations. Every equalizer is designed to equalize a certain number of types of deficiencies in your transmission link.

**Chris Gammell:** So if we can clarify real quick, the equalizer is actually something built into a chip. That actually helps with a physical phenomenon.

**Howard Johnson:** Yes, it is. If you send, just think of it this way. If I'm going to have my whole link work, then I have got to be able to send one bit and have one bit work.

**Chris Gammell:** Yeah.

**Howard Johnson:** So why don't we just send one pulse and just look at it at the end and see what it looks like. Okay. And so let's say I send you a pulse and it comes out. Oh, that's a pulse. And it's not shaped like a rectangle. Let's say it comes out and it's shaped like, I don't know, a pyramid or so. It's got some weird camel. Let's make it a camel shape. It's got two humps. Okay.

**Chris Gammell:** Camel to the camel.

**Howard Johnson:** Let's say you get this weird shaped thing that comes out and it's way too long. And so it'll overlap with the other bits. Okay. Well, if you just look at the first part of it, the first hump, you can tell whether it's a one or a zero.

**Chris Gammell:** Yep.

**Howard Johnson:** And then after you've done that, you know what's going to follow because it's always going to be the same camel shape. So you can take whatever you think is coming next, subtract that out of the signal, and whatever new arrives has got to be the effects of the next bit, not the lingering effects of the one you just looked at.

**Dave Jones:** Wow. And that's the same all the time. So you only need to do it once and you've got the characterization of that line to correct. Is that right?

**Howard Johnson:** That's right. The learning process in terms of learning, well, what is the camel shape? Some systems you transmit a single pulse first and you just look at it and you memorize it. Other systems, it's possible to make something where you just send it everything all at the same time. If you send a bunch of random data, it'll eventually figure it out.

**Chris Gammell:** Is that like an alignment unassertives kind of thing?

**Howard Johnson:** I love that. Yeah, that's part of the alignment process. I love that sort of stuff where it just figures it out at the end and you don't have to think about it. And that's great.

**Dave Jones:** How does the circuitry actually measure that? How does it actually measure that pulse, that shape? How does it do that?

**Howard Johnson:** Well, now it depends on what kind of equalizer we're talking about. If we were doing simple pre-emphasis, then basically the simple pre-emphasis has the ability to correct for pretty much one deficiency. And that is that the rising edge is slurred out too long.

**Dave Jones:** Right.

**Howard Johnson:** And it can correct for that smearing effect.

**Dave Jones:** So it's a rise time issue.

**Howard Johnson:** But it couldn't correct for a double hump camel, could it? You're the expert. If it's only designed to handle one thing, it won't handle other shapes. Right. So what we have to do is we have to know enough about signal integrity to get our link good enough to where we get it within the zone that our equalizer is capable of fixing. Okay. And then the equalizer fixes it. But if you don't know enough to get it in the right zone, you're screwed. Nothing will ever work.

**Chris Gammell:** So in that case –

**Howard Johnson:** I would say, yes, you have to know enough about signal integrity to get things to work properly. Now, things that are fairly simple to unequalize or effects that are easy to undo would include skin effect loss and dielectric loss. Those create nice, smooth, simple, slurred rise time effects. And it's easy to predict how they work. And it's just a question of how much undoing you want. You've got like a one-dimensional parameter you can use to run it up and down and get more or less preemphasis and get something to work. If that's the only problem you have, that'll get you a long way. If you had, for example, not only that but also some echoes, let's say that I send my pulse and you hear bing, bing, bing, bing, bing, bing. So, you know, you just heard – Due to poor termination. Yeah, seven or eight different things rattling around there.

**Chris Gammell:** Right, and that's one bit, right?

**Howard Johnson:** How are you going to equalize all that with one parameter? You can't. You need seven or eight parameters. And they need to be timed and spaced at different places. Yeah. So you need a much more sophisticated arrangement to do that. So for the gentleman who was thinking maybe if he has preemphasis, he doesn't have to worry about anything. What I would say is he has to worry about reflections a lot. Get rid of the reflections to the greatest extent possible. And if all that's left is skin effect and dielectric loss, you've got a good chance that an adaptive equalizer may be able to correct for that and that can work.

**Chris Gammell:** So it almost reminds me of like a camera, right? Like if you have a digital camera, if you take a good picture, you start off at a good spot and you can do it after processing. But in the case where you take – if you're moving 50 miles an hour and you're not focusing on anything, then you're probably – you're not going to have a great picture at the end, right?

**Howard Johnson:** Well, in the camera analogy, there's certain types of distortion that you might have. You might have a linear translation, which causes a linear smearing in one direction. You might have a vertical translation that causes smearing of a different type. You might have rotated your zoom lens, which makes things zoom in and out from a radio point in the center. Those are three different types of distortion, and it would take three different kinds of equalizers to undo those effects. Okay.

**Chris Gammell:** Yeah. Yeah. So if you had all three, then you might be able to do it. But the best case is to try and fix the actual problem.

**Howard Johnson:** You try to get the cleanest picture you can to start with. That always helps. Now, you asked how does it know what – if you're working with a double hump camel equalizer, how does it know what the shape of the signal is? And I'll give you some hints, not because I'm trying to be coy, but because this is, I think, the best way to begin to understand it. Let's say that I received data from you, and let's just postulate that it's good enough that I can recover most of the bits. And so I have a pretty good idea what the bits are, but I'm still making occasional mistakes. If I'm in that situation, then I might postulate – I might say, well, I think that each of his bits that comes in is interfering 20% with the next bit. So let's just try that. Let's try a delay Y1 and a coefficient of 20% and just construct that signal and look at it. And what I want to do with that signal is I want to look at the difference between the received signal that you're giving me and the ideal bit stream that I think I have recovered. And if this new signal I've created correlates with the difference between those two, then it's a good candidate for helping me to unequalize. I'm looking for things that are somehow correlated with the distortion that I'm receiving. And everything that I find that seems correlated with the distortion, I can subtract that out of the received signal, and it makes it a little better. I don't know if it's –

**Dave Jones:** But could you actually just guess? Could you guess at those things and then find the one that is the closest match?

**Howard Johnson:** Exactly. And the way a distributed feedback equalizer works is it says, my guess is going to compose – is going to be a signal like this. I'm going to take the received data stream, I'm going to take 15 delayed copies of it, each one delayed by one more bit, and I'm going to have a coefficient on every one of them. So I've got 15 coefficients, and I adjust those coefficients in order to get what I think is the best match to whatever the distortion is in the received signal. That's a thumbnail sketch. Yeah. You know, John Bingham, B-I-N-G-H-A-M, John Bingham wrote a great book called Theory of Modems that goes through a discussion of distributed feedback equalizers and how they converge and some things about using it that I think is the best introductory description I've ever seen of distributed feedback equalizers, which are very powerful, wonderful tools.

**Dave Jones:** Excellent. That's another book to have on your shelf.

**Chris Gammell:** Yeah, we'll put that in the show notes to make sure people can find that easily.

**Dave Jones:** So is the most important thing in high-speed digital design getting, like, knowing termination? If you had to know and understand one thing, would it be proper termination?

**Howard Johnson:** I would say the most important thing that you need to have if you're going to be a successful high-speed engineer is you need to know other high-speed engineers.

**Dave Jones:** Right.

**Howard Johnson:** You know, you need to be able to cheat. If you're working on something and you're having trouble, you've got to be able to call somebody up and go, hey, you know, this is happening. You've got any ideas? Yeah. If you don't have that, you're trying to work everything from books on your own and it's hopeless. And a lot of engineers don't really have the skills to go out and meet and make 100 friends. Of course not. And get to know them. Yep. I would just encourage them to try to do that. You know, at least if you can call people just to talk to them technically about your technical area. Maybe you can make some acquaintances and that will really help you with solving problems and with your career. Yeah, definitely. The more people you know, the better off you do. Oh, for sure. My God.

**Chris Gammell:** Do you have any online references that, like, forums so you can meet people, maybe not in person, but even to initiate, like, Skype conversations to try and find that kind of group? Do you have anything like that that you know of?

**Howard Johnson:** Well, there's two things I can think of. One is there's an electronic forum called the SI List. It stands for Signal Integrity List, SI-List. That's part of freelists.com.

**Chris Gammell:** Okay.

**Howard Johnson:** And it's an open mic discussion forum about SI topics. And somebody will write in and say, you know, what about right angle bends? Are they okay? And then, you know, 10 people will go, you're stupid. Don't ask that question. And one guy will go, you know, I don't know anything about that. And you wonder, why is he saying anything? And then one person maybe will speak out and say, you know, here's when they're okay and here's when they aren't. And here's an article you can read about it and you get something good. And reading that, you can eventually pretty quickly figure out, well, who are the guys who seem to answer every single bloody question and don't have anything to say? And just tune them out and take some of the other names and try to correspond to it. You know, my experience is if I write to someone who's knowledgeable on a subject and really knows it and I ask them a technical question, a lot of times they'll try to help. I know I do. I answer hundreds of questions every year that come in. That's awesome. So that's one forum, the SI list. Second thing, well, on my website, people are welcome to ask questions if they want. There's a contact us feature and they can write to me.

**Dave Jones:** Uh-oh, you've opened up a can of worms there. Well, yeah, because I've had to – I'm now getting so many technical questions and so many emails through my video. Look, I can't possibly answer them all now. It's just I wouldn't be able to – I'm not physically capable of answering all technical questions. So there's – unfortunately, there comes a time when you have to actually say, well, sorry, I can't help you anymore. Please go ask on the forum and the forum is a better way, be it the SI list or something else, is a better way to get the information.

**Howard Johnson:** Well, you're right. It can be overloading. But I found it to be very satisfying and a great source of research ideas for me. You know, when I hear about problems I haven't heard about before, it gives me something to go investigate and find out. And then last, of all the different IEEE chapters, the EMC Society has the strongest chapters. They actually have periodic meetings in most major cities, especially if you're in Palo Alto or San Diego or Boston or someplace or Dallas. You can go to their monthly meeting and the way it runs is they'll usually have some pizza. Everybody sits around and talks. Then they'll have a speaker. Somebody does a presentation or maybe they watch a film or they – I have several –

**Dave Jones:** What sort of films would you watch at a meeting like that? I'm taking it's not Avenger the Nerds or something like that.

**Howard Johnson:** No, no. It would be something on a technical side. I have nine different movies that get circulated at EMC societies. I was going to ask about that.

**Dave Jones:** Yeah, you've got one called Mixed Signal Isolation or something.

**Howard Johnson:** Yeah, that's a really popular one. They love that.

**Dave Jones:** Can you buy it on DVD or something?

**Howard Johnson:** Yeah. If you look on my website, there's a way you can order one. We'll send it out. It's not very expensive. And, you know, a great use for that is to have a meeting, show the film, get everybody talking.

**Chris Gammell:** Yeah.

**Howard Johnson:** And that's the way the EMC Society works. People meet each other. They get some technical input. Then they talk. And then usually there's a part at the end of the meeting where they go, okay, who needs a job?

**Chris Gammell:** Who's got a job? We're handing out jobs here, folks.

**Howard Johnson:** Come on down. The employers don't like to hear that they talk about that at the meetings. Yeah. I'm sure it does. Of course. If you need an EMC consultant, by the way, that's the best place to go. To meet them, talk with them, find out what their experience is. And you learn a lot. But I find that the people with RF backgrounds, at least they have an innate understanding that the size and shape of the circuit has a huge influence over its performance.

**Dave Jones:** Yep.

**Howard Johnson:** And that's something that is more difficult to grasp for digital engineers if they grew up looking at nothing but logic schematics. You know, in a logic schematic, it doesn't matter how close you put the wires in the drawing. It doesn't make any difference. But in a real circuit, it actually has a huge impact on them. It matters huge time.

**Chris Gammell:** Yeah. Remember, those digital guys, they get forced to do the layout because I'm sure they come knocking at your door and sending you emails. Right, Howard? Yeah. I don't see a lot of them. Yep.

**Dave Jones:** So how difficult, how robust are the modern serial and transmission systems like Ethernet and other USB 3.0 and those sort of things? Are they so critical that the cables really matter? Can you really beat them around and put them through a piece of wet string and they're still going to work or what?

**Howard Johnson:** If you actually max out all the parameters for an Ethernet length all at the same time, it's got like a 5% margin left.

**Dave Jones:** Right. Okay. If you max out every, how many different parameters would there be roughly?

**Howard Johnson:** There would be the cable length is the primary thing. Yep. The cable length, length of jumpers, quality of the connectors that are used between those different elements. Yep. The cable performance itself, how close they came to that. And the cable manufacturers, you know, they struggle to make cables that are good enough to meet the spec. They're within a couple of dB of the spec usually. Those are the main things that are going to matter. And then, of course, you're packaging your layout on your board. It's easy to screw the system up. Sure. Right on your board. But if you've done a good job of that, and let's say you're in the field and you're installing Ethernet things, the service people find out that a lot of times they can go, you know, 5% or 10% extra length and it works and they don't say anything to anybody, especially if their jumper is a little shorter than usual. Stretch it a little bit. Yeah, yeah. Great. And that's a wonderful property for a lake to have. I like that. You know, one thing that gets you there is the budgeting process that we used in those standards where you come up with a list of impairments and you have a budget for each one. And you say, well, this is going to be worth this many dB and this many dB. And you add them all up and you've got to have something with a little bit of margin left over. Okay. And that's the way, I think, to design a really good link. There's a trend in link design now, instead of having budgets with individual compartments, is you design everything all at once. And you use your simulator to simulate everything all at once. And if the simulator says it's okay, you assume it's going to be all right. And you don't worry about the individual compartments. And I just think that's a mistake. I think, you know, in every high-speed serial link project I've been involved in, the way it works is you start out on day one and you have an envelope. And on the back of the envelope, you write out your budget for what you think is going to happen. I think we can go 100 meters. We can go this fast. We use this kind of cable. And here's the thumbnail sketch. And this says what's going to happen. And then as you go through the process, things always get worse. Because I've never, ever had something turn out to be better than what we thought it was going to be in the first budget. Yeah, magically. We just found all this margin.

**Chris Gammell:** Who knew? Unsurprising.

**Howard Johnson:** So that means you've got to start out with a lot of margin in the first place so that as you lose margin, you're still looking in. Great. So what would happen? Just think practically for a minute. Let's say you're the chief engineer for some new project and you go to your boss and you say, well, here's the budget and I've got 7 dB margin, you know, on this thing, just in case. Your marketing people are going to scream. They're going to take that away. So we'll make the cable longer. Make it go faster. Make it get us more and more and more to max it out on day one. So you've got to hide it. In consequence, exactly. You must never show your actual budget. You have to have two sets of books.

**Chris Gammell:** You have one. I was really teaching all those students out there how to succeed in business, right? Oh, yeah.

**Howard Johnson:** You have to have one that shows what you really think is going to happen.

**Chris Gammell:** Right.

**Howard Johnson:** And then you have the other one that's your published budget where you take every one of your, you know, 15 categories and you make them each one worse by a quarter of a dB. Yep. And so you've got, you know, three or four extra dB hidden in there where nobody knows what it is. And then the day somebody comes up and says, oh, well, the connector isn't quite as good as we thought. Oh, great. Well, then you can say, well, look, I found out this thing is a little better than we thought. But then you can, you know, take some of that margin out of your back pocket. Exactly. And when you get done.

**Dave Jones:** And you do it right at the last minute, you know, you come up with a solution. No, you don't tell it straight away. You go, oh, yeah, we'll work on it. Working hard. Oh, we can't find the solution. And then all of a sudden, bang. Perfect.

**Howard Johnson:** Yeah. Just like Scotty. And that's it.

**Dave Jones:** Yeah, that's it.

**Howard Johnson:** You remember on Star Trek when Kevin Kirk would always say, Scotty, how long is it going to take to fix the dilithium crystal? And he's like, can I do it? And those are two days. And actually, he knows he can do it in about 45 minutes. Yeah, yeah, yeah. That's right. He can do it the rest of the time. Yeah. And he always gets it done, you know, before the Klingons attack. It's great. That's it. And relationships work that way. Yeah. Oh, that's brilliant.

**Chris Gammell:** And that's why they call it black magic.

**Dave Jones:** Black magic. How bad are those cheap Chinese cables? You know, the ones that aren't made to any standard. They're just copied and, you know, come straight out of the one hung loaf factory in China.

**Howard Johnson:** Well, if I took coaxial cables as an example. In my mixed signal isolation film, I show two coaxial cables. I put a signal on one. I just hold the other cable up next to it. And you can see the cross dock in the other cable. And then you take really good cables and you hold them up and you can't see anything. It's an astonishing difference in quality. And some of which you can see looking at the spec sheet for the cable. They show you a lot about attenuation, don't they? But they don't tell you much about cross dock. And that has to do with the quality of the shield.

**Dave Jones:** I was going to say that would be the shield weave, right? It would.

**Howard Johnson:** And the shield weave is an expensive part. You know, I've never seen a coaxial cable weaving machine. It must be fascinating because it extrudes the plastic with the center conductor in it all centered perfectly. It weaves all at the same time. It does everything. Wraps the foil and does all this jazz. It must be a hell of a machine.

**Dave Jones:** That is manufacturing black magic.

**Howard Johnson:** Yeah, it is. And it's got to be expensive to get it to work. And so, yeah, there really is something to, in terms of cross dock performance, there's a lot to say about cable. For the attenuation performance, it's mostly a matter of the size of the center conductor and is it copper or not. The quality of the dialectic material, which they can control fairly well. And the uniformity of the process. If the center conductor is wobbling around, especially in some predictable way as it weaves, you know, every 10 feet there's a wobble on it, then that can create some unusual artifacts at high speeds that cause trouble. And that, you know, was something you'd expect in a cheap cable.

**Dave Jones:** So you could almost see imperfections in their manufacturing machine if you tested that cable closely enough. You might actually be able to see, oh, yeah, look, every meter there's a little kink.

**Howard Johnson:** Yeah, exactly. And the thing to do is, quite simply, just put in a step edge and look to see what comes out the other end. That's the primary test that we as digital people need to do on cables. It's very simple. And see if it complies with what you expected to happen over a cable with the specified, you know, skin effect and dielectric loss that you expect to have. And then put two of them next to each other and see what kind of cross dock you get.

**Dave Jones:** Hmm. Interesting. Now, I know we're way over time here, but we don't care because you're such a cool guest. But I've got to ask, I've got to ask, what is your take on the audio fool industry? If you know the audio fool industry, you know, with their $10,000 cables and their, you know, their $10,000 power cables. Oh, yeah. $20,000 cryogenically frozen speaker cables. It's, and have you ever had them?

**Howard Johnson:** It's embarrassing to me. It's embarrassing to me. Yeah, it is. To see engineers, you know, trying to convince people that effects like that really would matter. And I'm very sorry to see that audio folks are very gullible about this and believe a lot of that baloney. I don't see any to it. Have you? And I know what we're going to hear. People are going to say, oh, well, you've never heard a really fine audio. Heard the difference. Yes, that's right. Yeah. You don't know what good audio actually is. Yeah, that's right. And I'll tell them, yeah, I do. Yeah. Yeah, actually. I know one of the first engineers at Ampeg who designed some of the first recording systems ever and worked to make to perfect them. I know, you know, people, when I was, you may not know this, but on our property here, we have a very large barn and we've outfitted it as a classical music venue. And we have a chamber music festival that happens every year. Awesome. And it's a beautiful affair. People from all over the world come here and they play at the top level, you know, chamber music in this small, you know, venue way out in the country. And so in designing the venue, I had to know how to light it and how to arrange the sound and the acoustics. And so I asked my friend Gary Harper. And Gary, the first thing he said was, he said, oh, well, when I do recordings at Benaroya Hall in Seattle at their main symphony hall, here's the way I do it there. And he showed me how everything was done. And so, yeah, I think I know what good audio actually is. Yeah.

**Dave Jones:** You know, they talk about skin effect and transmission effects and they go into the math, which are actually technically correct, but they just, you know, they're just fooling you because they don't actually apply to what they're actually making.

**Howard Johnson:** Yeah, and I think they misinterpret a lot of it. There was some skin effect article at one point that I wrote that was about speaker cables and whether or not the skin effect would conceivably have any measurable impact on speaker performance. Oh, I have to link this one in. And my conclusion was it's really not going to make much difference. And furthermore, the transition frequency at which the skin effect begins to take hold is quite high. It's in the, you know, 50 to 100 kilohertz range where it even starts to do anything until then that the current completely penetrates the conductor anyway and everything's fine. But if you make a great big fat speaker wire, like an inch in diameter, huge, you know, what is that, like five, five-aught wire like Monster Cable used to do when they first started.

**Chris Gammell:** Pure gold, right.

**Howard Johnson:** Then the skin effect transition would be down in the, you know, a few hundred hertz area and maybe you'd hear something. And so what happened, because I was making fun of them, and they used to make cables like that. And anyway, the editor took that out and reinterpreted it, you know, to say that there's something about how his cable was wonderful and better than everyone else's because of what I said in the article. And I was really pissed. But then he wouldn't communicate with me anymore, and he has it posted on his site. And, you know, things like that happen. Crap happens. I lost a lot of respect for him. And as a result, I haven't really, you know, and also because it's just not a field I'm that interested in. And I haven't done much with it. But I will point out that if you look inside your speaker and you unwind the coil, there's a whole bunch of wire in there.

**Dave Jones:** There's a whole bunch. And it's not that thick either.

**Howard Johnson:** No, it's a whole bunch of little skinny wire with a lot of resistance. And there's your problem.

**Dave Jones:** There's your problem.

**Howard Johnson:** It's not the wires leading from the amp to the speaker. Now, grounding your audio components to each other very well will make a difference in terms of the hum that you get out of a system. Definitely do that. Put everything in a rack. Bolt everything to the rack. Make sure the screws are electrically conductive from the face of the equipment into the rack. And you'll have a nice quiet system, and that'll work. But after you've done that, the quality of the ground on your power wire hardly makes any difference. It's getting all your piece of the system grounded to each other is the main thing you have to concern yourself with.

**Dave Jones:** And I've got to have one last question. Sure, anything. I've got to throw one in. Oh, we're asking over time. But we don't care. I don't care. I'm not sure if you care.

**Howard Johnson:** I'm okay up to a point. Actually, tonight I have a rehearsal. I've got to get ready. I'm going to play.

**Chris Gammell:** No, that's okay. I've got one more question. I want to hear what he plays, though. Howard, are you a musician?

**Howard Johnson:** Yeah, I play upright bass in a jazz trio. Oh, that's great. We're going to do the Claude Bowling Suite for Piano and Jazz Guitar. That's awesome. Which is really challenging. Claude Bowling music is killer. We've got to play it Saturday, so I've got to go get ready for that. So I've got about 10 minutes left.

**Dave Jones:** No worries. Here we go. You're probably the best person on the planet to answer this. The age-old question, right angles on PCB traces. Tell us your take, and when does it start to matter? Yeah, I think that's a good question. Because it does matter, but it's a matter of when.

**Howard Johnson:** Okay, so let me start with this. If it mattered, you couldn't use vias. Yeah. Because the via, you're going horizontally, boink, straight down the rabbit hole. That is as right an angle as you can have.

**Dave Jones:** It is.

**Howard Johnson:** And so apparently.

**Dave Jones:** But it's nice and circular, though. Come on.

**Howard Johnson:** It must not be as big a deal as people think. And actually, it turns out that there was a lot of research on right angle bins conducted by the microwave community back in the 60s. They studied it. They modeled it. They have a really good understanding, I think, of how it works. And here's what they found out. If you go around a right angle, you know, I'm talking about a single-ended trace. It's not different. There's one single-ended trace. Let's make it a microstrip. And it's a 50-ohm trace. And it takes a right angle bin. Then in that edge, as you imagine a single going around the corner, you can imagine it gets a little wide at the corner, doesn't it? Yeah. More value. It does. The extra width, that little pointy triangle on the end, it's like an extra piece of copper hanging on the side of your trace that you could do without.

**Dave Jones:** It's a little stub almost, you know?

**Howard Johnson:** It is. It adds a little extra parasitic capacitance to the ground, just as if you'd had a straight trace and soldered a little tiny triangle on the side of it of that same size, you'd have about the same effect. And the effect is, if I remember the numbers correctly, on a 10-mil wide trace, 0.01-inch wide, which is pretty fat by our standards today.

**Chris Gammell:** It is.

**Howard Johnson:** You get 0.02 picofarads of additional capacitance to do the corner.

**Speaker ?:** 25 to the point.

**Chris Gammell:** Wow.

**Howard Johnson:** Okay? Yep. Yeah. Compared to a via, even the smallest via, it's going to be 10 times. It's going to be 10 times that size. And so, in that sense, the right angle bins are not nearly as significant as vias for us. But they do have an effect. Now, why would microwave people care? And this is where I think it gets interesting. And this is where the whole rumor started that the right angle bins are a big deal. Because a microwave guy will tell you, oh, no, you can't have right angle bins because they cause a lot of trouble. And the reason they say that, the primary reason, is because they make huge fat traces. Yep. They're not. They'll make a two-layer circuit board with solid ground on the bottom, a top layer, 60 mils away, 120 mil wide trace. 120 mils wide. And so, the right angle is gigantic compared to ours. And so, of course, if they're at 120 mils, how wide are your traces? What, three, four mils maybe?

**Chris Gammell:** Eight or six. Yeah. Six or eight standard points. Six or something like that.

**Howard Johnson:** So, they've got a trace that's 20 times fatter than your trace. And so, it has 20 times more capacitance. So, instead of the 0.02 picofarads, now suddenly it's 0.4 picofarads.

**Chris Gammell:** Right. And they're actually going at very high speeds regardless because of it's an…

**Howard Johnson:** Excellent point. Yeah. They're going 10 times faster on average. Yeah. And they're more sensitive to tiny effects. If you have a little 5% or 10% effect in your circuit, you can still receive the bits. Yeah, it matters. Not a big deal. But for them, if they have a, you know, flatness spec plus or minus, you know, 0.2 dB, you know, 5% effect is a killer.

**Chris Gammell:** Yeah.

**Howard Johnson:** The whole system won't work. And especially because they cascade multiple stages. If I'm making an amplifier. Now, my father used to be in this business. He made microwave amplifiers. And you've got an amplifier with 10 stages. And your overall spec is plus or minus a half a dB. And you have 0.05 dB per stage that you have to comply with. And one 120-mil wide, you know, corner at 50 gigahertz is going to eat your lunch. Yeah. And so you're scared of them. So you tell people, my God, you can't do these things. But they're 10 times as sensitive. They're 10 times as fast. On traces, 10 times as big. They're 1,000 times more sensitive to ridingle bins than we are with our little tiny chases in our very tolerant system. Well, I've got a whole megahertz, you know.

**Dave Jones:** So we'll still propagate the myth. No pun intended.

**Howard Johnson:** Yeah. It's not a big myth. Now, some people worry that when you hit the ridingle bin that the electrons might have difficulty rounding the corner somehow. Yeah.

**Dave Jones:** Or they fly off the ends.

**Howard Johnson:** That's right. And so I just want to remind everyone that the electrons are jiggling and wiggling back and forth at the speed of light, constantly running into things.

**Chris Gammell:** They're doing okay.

**Howard Johnson:** The drift velocity. Drift velocity. The average rate at which they drift down the trace. If you have a logic 1 and you've got, you know, 50 milliamps pouring down the trace forever, the drift velocity is about as fast as an ant walks.

**Dave Jones:** Yep.

**Howard Johnson:** That's it. And yet they're jiggling at the speed of light, bouncing off every atom that they encounter and drifting very slowly. And if they bounce off the side of the trace, it's not a big deal. They don't have any trouble doing that. This is what electrons do. They bounce all the time.

**Chris Gammell:** So there you go. Dr. Howard Johnson, thank you very much. I think I have one last question. Is it ever tough looking at the world in the way that you just did and being like – I mean, it just seems like being a very – you know, you're an expert in high-speed signal stuff. I have to imagine sometimes you're just like – That's your head against the disc.

**Howard Johnson:** Well, you see things that you'd rather people didn't do. That's true. You see it all the time. But we're used to that. Like we see people, you know, texting on their phone while they're driving. Yeah. And you go, you know, this isn't going to work. Yeah. And their attitude is, oh, well, it hasn't not worked. It's fine. I can do this. It's fine. And they just haven't encountered the situation that's going to kill them. And in the digital world, we have the same thing. I see people doing practices that I know, you know, lightning strikes, you know, within a mile and your system's not going to work or whatever that bugs me. And where there's really the confluence of those ideas is when we start thinking about putting more and more computers in cars.

**Chris Gammell:** Yeah.

**Howard Johnson:** You know, they're already in control of our brakes. Oh, yeah. And when they get in control of our steering and our accelerator pedal, you know, one of these rolling computing platforms gets a lightning strike. And I don't know what's going to happen. It's going to make a mess. You know, one of my friends, Michael King, he's an EMC engineer down in Southern California, got started that business at its inception back in the 60s. And he told me that when CB radios first came out, that that was about the time that anti-lock brakes were invented. And anti-lock brakes were first implemented on big rigs. Because, you know, you slam on your brakes and if the wheels lock up, you can jackknife and it causes a very serious accident. And it's worth a lot of money to avoid that. So big rigs are the first vehicles to have anti-lock brakes. And that they noticed that if someone pulled up in a car next to a big rig and keyed on their cell phone, it would sometimes jam on all the brakes on the big rig.

**Dave Jones:** Oh, no. Wow.

**Howard Johnson:** What a time to learn something like that.

**Dave Jones:** Yeah. Ouch.

**Howard Johnson:** You know, interference happens.

**Dave Jones:** So it made it to the field. The design made it to the field with that sort of limitation.

**Howard Johnson:** Wow. We had, you know, heart, what do you call it, you know, when you need a little help with your heart, you get a heart pacemaker. Oh, yeah. That stimulates your heart to give it a regular heartbeat. The first heart pacemakers were susceptible to microwave ovens. You just walk near one and you didn't croak. Ouch. And, yeah, I believe that really, really happened.

**Chris Gammell:** That's like Uncle Eddie in Christmas Vacation. Every time Helen turns on the microwave, I pee my pants and pass out for 30 minutes.

**Howard Johnson:** Yeah. Yeah, right. These things happen and they've been happening for a long time. You know, my mentor Martin told me that in the computer field, the same trends recur over and over and over. He said, what will happen is we'll invent some wonderful new technology. Like, we invented, you know, we started with relays. And we worked with relay technology until we pressed it to the upper limits of its speed capability. Yeah. You know, in which case, you had trouble with ringing. You know, the little levers would actually bounce. Yeah, yeah. They had trouble with that. Still do. The whole system. Yeah. If you did it synchronously and everything was going, the whole system would vibrate so much that it would cause bit errors in other places. They had trouble with heat. They had all these problems with the packaging. And then we invented tubes. Hey, all those problems went on. Yeah, great. And suddenly the tubes seemed to behave in an ideal, perfect manner. You know, you put in a logic one, you get out of logic zero. It was just like perfect. You did whatever you wanted. As long as you went slow, nobody had to know anything about packaging. And so for a while, there was a generation of engineers that grew up making simple tube computers that didn't have to know very much about how they were built. But then as they pressed to the upper limits of speed, suddenly all this knowledge about crosstalk and signal propagation became extremely important. And, you know, Marty, in the last tube computer he made, he was trying to transmit a clock signal from one tube that had to go down to 300 other tubes that were located in three different buildings. Oh, my God. I mean, tube machines were large. These were huge things. And to get that to work requires a certain finesse. And then when we invented transistors, everything shrank. The packages are smaller. And it seemed like all our problems were solved. And they got faster. And then we invented ICs. And that was great. And now we're getting to the limits of what you can do with the IC packages. And we need smaller packages. I mean, we need to go to chip scale packages. And we need to do it quick because that's going to be one of our big limitations. And if we continue trying to go faster without doing the chip scale flip chip packaging thing, we're going to have to just know more and more about signal integrity.

**Dave Jones:** But you can't solder the bars.

**Howard Johnson:** No, there's all sorts of problems with them. Yeah, of course. But signal integrity-wise, it's the answer. I know. You've got to do it. It's the answer. That's the price you've got to pay.

**Chris Gammell:** Yeah. Well, I think in order to keep you employed, Howard, I think we'll stick with the regular chips for now. And we'll keep sending the suckers your way, huh?

**Howard Johnson:** All right. That sounds great.

**Howard Johnson:** Chris, it's been a great pleasure talking with you today. Thanks for calling me out.

**Dave Jones:** Thank you very much, Dr. Howard Johnson. And if you haven't got his book, it is High Speed Digital Design, A Handbook of Black Magic. Yes. We have it and it should be on every- If you don't have it, well, you're not in the business.

**Howard Johnson:** Thanks so much. Seriously.

**Dave Jones:** No worries. Thanks again, Dr. Johnson. Thank you for joining us.

**Chris Gammell:** It was awesome.

**Dave Jones:** All right. Great show. Thank you.

**Chris Gammell:** Yeah, I think I might have to do a little editing. Tell Sagan he sounds like a cat when he cries.

**Dave Jones:** Cat. It sounds like- Meow. He rarely cries and he just all of a sudden just, you know, he heard your voices and something weird was happening and just burst out crying. That was-

**Chris Gammell:** Yeah. Yeah. Anyway. Hates Americans, man. I'm telling you.

**Dave Jones:** Hates Americans. Oh, boy.
