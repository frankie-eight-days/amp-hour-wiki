---
episode: 464
title: KonnectorPanik
url: https://theamphour.com/464-konnectorpanik/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released October 27th, 2019. Episode 464. Connector Ponik.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell, Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Hey, man. You know, we're making antennas around here. I'm making antennas lately. I saw that. Yeah. A million.

**Dave Jones:** First one didn't work. They are subpar, let me tell you. A bit loosey-goosey, huh?

**Chris Gammell:** Yeah.

**Dave Jones:** Right. Subpar in what way?

**Chris Gammell:** Every way. I don't know anything. Dave, I don't know what I'm doing yet. So literally, I should mention. And like, so I was-

**Dave Jones:** It's a piece of metal. It's a shaped piece of metal, dude. I know. It's so dumb.

**Chris Gammell:** I think the thing was, I was kind of like putting too much importance behind what it was. You know, it's basically a monopole. And so Pete Bevlacqua, who we've had on the show before, and Mr. Jeff Mightyum Kaiser. Yes, sir. They were helping me on Twitter as well. But basically, I'm just trying to get a feel for like a mental model for how this stuff works. You know, like, it's not like you could just change a shape. I mean, like, yes, as the shape changes, you will have better, you know, properties of antennas. But I can't just pull them out of my keister. You know, I got to like actually go and figure out what those things look like. So what I was doing is I was using that AppNote we mentioned two weeks ago, that AppNote 058, which is from TI. And that is a fantastic document. I was reading more of it. And like, there's stuff in there about how to do testing and just really, really good stuff. But I found another one. I was looking specifically for 433 megahertz that's in the ISM band. Like, I was looking for an antenna at that level. And there weren't really that many PCB antennas. So it's kind of just like doing my Google image search thing and dancing around trying to find something. I found one dev board. And then I did what every person naturally does, which is, of course, pull in the grainy Google image and then trace over it in Inkscape and make an SVG. It's just a place to start, you know. And at the end of the day, it was a monopole, which is stupid because I could have just, you know, put a hole on there and cut a length of wire. I think it's 100. Exactly. I think it's like 127 millimeters or something like that. And 173 millimeters, so 17 centimeters.

**Dave Jones:** Now, is the performance, is the dodgy performance because of the dodgy tolerance on the milling? Or is it because of the dielectric? Or is it a combination? What's going on?

**Chris Gammell:** No. And this was actually, this is like some of the good learning that I got out of it. So it's, as Pete, so Pete runs antennatheory.com or .net or whatever it is. And if I would have read that, I would have read that a monopole is usually just a dipole where the ground plane is the second half of the dipole. Did you know that? I didn't know that. I didn't know that. Basically. Slow learner here, Dave. Generically. Slow learner. And so the problem was that like on, the shape was good, obviously. It did us fine, right? The shape is really just a way to get a length of wire onto a board in a smaller area, just like you do with a resistor or an inductor. Well, I guess an inductor you want to coil. But if you're doing like a serpentine resistor.

**Dave Jones:** That was the breakthrough in fractal antennas, which made mobile phones and stuff. Oh, interesting. Smaller and more possible. Yeah. Fractal, because the fractal shape has, you know, so you get the physical length out of it, but in a much smaller area. Got it. Yeah. Fractal antennas. Yeah. It's folding back on itself. It's, yeah.

**Chris Gammell:** Yeah. That's cool. But you need the ground plane there. And Jeff pointed out to, you needed to have it like an equivalent size effectively. Yeah. So, and this did not have that at all. So, threw it on the VNA, looked at it. It was the wrong size in the first place, you know, wrong resident frequency. And then didn't have a big enough ground plane. So, basically what they said is that because now I'm plugging in a SMA cable, right, into that, right, the ground of the SMA is.

**Dave Jones:** The shield of the SMA, yeah. Yeah.

**Chris Gammell:** So, that is hooked into the ground of this thing. And now, yeah, the shield of that entire cable acts as a thing. So, I moved the cable around and it was just, it danced all around. Not a good antenna. But very good learning opportunity. And I've been cutting some other stuff in the meantime. And, yeah, the RF is a little difficult. A little difficult. Who knew? Who knew, Dave? We've definitely never said that on this show.

**Dave Jones:** They don't call it, yeah, black magic for nothing.

**Chris Gammell:** Yeah. Yeah. And then what's really crazy is then Hardy, someone on Twitter, another person on Twitter, Hardy, offered to simulate it for me. Because, you know, there's like fancy, fancy. Yes, there are. Yeah, packages. Packages for that stuff. And then he sent me an image of the actual, like, maybe I'll use that as the image for the show or something. But it was an image of the, you know, like what the radiation pad would look like. But then also like an estimate of what the resonant frequency would be like. What the S11 would look like and stuff like that too. So, and it was like spot on. Yeah, I was just like, oh, yeah, okay, math. Bring it on.

**Dave Jones:** Got it. It gets really nasty when you want to properly characterize and model that sort of stuff.

**Chris Gammell:** Yeah. It's, you know, it's really tricky business. Right, right. Yeah, and I think about like, so we've talked about, I don't know if we talked about it, but I think it's been peripheral to what we've talked about in the past about like that iPhone where you had to, your hand was like in a way. You had to like hold it a certain way. And that affected the antenna. And it's because, you know, body impacts and yada, yada, yada. Yeah.

**Dave Jones:** That would be really difficult. If anyone out there is a mobile phone antenna design, because you can't just design the antenna in isolation, right? You know, you can't just go, oh, look, I've designed my antenna from the new iPhone and it works fantastic when I sit it in a cradle in the middle of the test stand in the middle of the test chamber. Yeah. But when somebody's holding onto that damn thing, using it like a phone.

**Chris Gammell:** Right.

**Dave Jones:** It's like, you know.

**Chris Gammell:** It's a Pete who was on the show. So he talked, you weren't here, it's fine. But Pete actually designed some of the iPhone antennas. Right. So he talked about it a little bit, but he couldn't talk about it a lot. Right. Of course. And he's done some other commercial stuff. But yeah, I think, you know, I'm sure we'll have some other antenna people here at some point. But it's been good. You know, the thing that I've been trying to figure out too is like, okay, like just baseline, like what is a Smith chart for?

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Still, still, you know, working my way up to that. But it's, you know, like.

**Dave Jones:** They don't teach that anymore, do they? Maybe if you do a specialist.

**Chris Gammell:** If you're doing, yeah, I think you do.

**Dave Jones:** If you did an RF class or did an antenna. Yeah, yeah, yeah. Yeah.

**Chris Gammell:** And like, so what that's really good for though is like, so say you've got an antenna, you know its characteristics now, you know what frequency it's at. But you need to then match it, right? You hear about 50M systems and stuff like that. And you want to measure the, where it is relative, like what is its input impedance, complex input impedance. You want it to be like at the zero point on a Smith chart, which I, you know, have been learning, of course. And.

**Dave Jones:** Your newfangled siglant VNA will do that, won't it?

**Chris Gammell:** Yeah, exactly. Yeah.

**Dave Jones:** Does it actually have Smith charts built in?

**Chris Gammell:** Yeah, it has a Smith chart built in, which is nice. The thing that I didn't realize about it is that like, so you have a Smith chart and like, there was actually the one time when it was like drawing really slow, which is actually really helpful. Because what it did is it was drawing. And then I saw like, everything was radiating out from, from the zero point. It was drawing it like a, like a, like a, like a angle and magnitude kind of thing. You know, so it looked like a, like a polar plot. It is a polar plot, right? And it was actually doing that. I was like, oh, you know, because the curves of a Smith chart always kind of confused me, you know. So those are actually there to guide, to guide you when you want to put in a capacitor or something like that. Yep. There's actually Alan Wolke, past guest of the show.

**Dave Jones:** Yes, he's, he's, he's done a tutorial.

**Chris Gammell:** He's done a really good one and shows you how to do it. And I had someone local here, Danny, was helping me with some Smith chart stuff too. So I'll link in Alan's videos. He's got a couple of them. But I just felt like when I watched his stuff, when I watched Alan's stuff, I didn't quite, I didn't have the background to really understand why it was important. Got it. Yeah. And, and now I'm getting a little bit more. And this is why, like, so if you ever, you know, so like we've talked about like block diagram, not block diagrams, but like a pattern matching. Right. So. Right. A lot of times what you'll see on the output, like, so like I'll throw in a Bluetooth chip or something like that. You'll see usually a capacitor going to ground, an inductor going in series, and then a capacitor going to ground. And, and, you know, you'll see that in like the caps will be no popped. The inductor will be there, but sometimes it's just a zero ohm resistor. And it's like, well, what the hell is that thing doing there?

**Dave Jones:** Why did you bother?

**Chris Gammell:** Yeah. Yeah, exactly. And that's there because then you can use that, those, those patterns, it's called a pie filter. And you can use that to adjust the matching basically, because it's kind of just like a, it's like a placeholder for later.

**Dave Jones:** Yeah. Welcome to the world of antenna design.

**Chris Gammell:** Yeah. It's, there's a lot to, there's a lot out there, Dave.

**Dave Jones:** You've only, you barely scraped the surface. Oh yeah. Yeah. But I think. It's a big rabbit hole.

**Chris Gammell:** Yeah. I mean, like the other thing was like, I had to like buy connectors. I think I mentioned two weeks ago, I like buy connectors and just kind of figure out like end connectors, end type connectors always kind of scared me for some reason, but they're just. I don't know. It's weird, right? I think just because they were different and foreign and they're basically just like.

**Dave Jones:** Irrational fear. There should be a word for. Well, you know, yeah, German word, right? Irrational fear of connectors.

**Chris Gammell:** Yeah. It'd be like connect, connector panic or something like that, you know? Right.

**Dave Jones:** Speaking of iPhones.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. This is, well, it's pretty huge news. We've talked about it before, I'm sure. And it's nothing new, but Apple is pulling, is investigating pulling up to 30% of its manufacturing out of China.

**Chris Gammell:** Yeah. Yeah. And this is among other manufacturers. It's not like it's just Apple. Oh no.

**Dave Jones:** It's, you know, it's been an ongoing trend for years now of, if you don't know, a ton of companies are moving out of China, either completely or partially, you know, they're setting up, you know, transition facilities and manufacturing facilities out of China.

**Chris Gammell:** Right. Right.

**Dave Jones:** Because, well, it's like people have suddenly realized, oh yeah, China's a communist country. Who knew? And China, well, you know, look, okay, there'll be a ton of comments now, you know, about what is the real form of communism? You know, like, oh God. Yeah. Seriously. How about this? It's a complicated.

**Chris Gammell:** I think that it would be very safe to say it's a complicated regulatory environment in China.

**Dave Jones:** It's a complicated issue. Anyway, yes. And the new trade war is not going to help. The article I linked in on The Verge, it says, it's a trade you'd probably know more than miss being local. Is it starting next month? Like, what is it? A 30% tariff on Chinese products?

**Chris Gammell:** It's continuing next month, right? So like, basically, they, yeah, they're supposed to roll in the more of the end device type of tariffs, I believe.

**Dave Jones:** Which is phones and other consumer products. Right, exactly.

**Chris Gammell:** So previously it was like end user devices weren't being tariffed, weren't being, had a tariff on them. But parts were. But a lot of the components would be, yeah, exactly. Stuff you mentioned on there.

**Dave Jones:** Which we talked about, which is the DigiKey mouse, a tariff thing. Right, exactly. The parts. Yep. Yep.

**Chris Gammell:** And so, as they were very clear of at the top of the article, they say, no, no, no, this is not coming to the States. It's just going somewhere else that's low cost.

**Dave Jones:** India, most likely. Yeah. But there's many other countries. Yeah. It's, you know. Yeah. I mean, it's interesting. Yeah. So they've instructed Foxconn. And a lot of people think, oh, well, isn't Foxconn Chinese? No, they're actually a Taiwanese company.

**Chris Gammell:** Yeah.

**Dave Jones:** So, you know, it's, yeah. Right.

**Chris Gammell:** And they're so big. I mean, all these companies are just so big that they're just going to pick wherever's cheap and they're going to bring in their processes. And if they need people to like, you know, plug in connectors and, you know, wipe off screens and stuff, they're going to do it until the robots are cheaper. Like, that's how it goes. Yeah. I mean, I actually.

**Dave Jones:** Well, India is a fantastic place to go, though, because not only do they have the population of China, right? But like half of them have freaking engineering degrees. That's true. Yeah. Every second person in India has an engineering degree.

**Chris Gammell:** I think that might be a generalization. It's almost a running joke. Yeah. No, seriously. It's almost a, you know. But I think there's a lot of talent there for sure. For sure. So, like, it's interesting, like, looking at manufacturing kind of floating around, too. Like, they just had a meetup here at my workspace with, like, Korean companies, right? And, like, Korea was like this and Japan was like this and China's like this. Yeah, yeah, of course. You know, manufacturing is like, everyone's going to eventually move up the value chain and it's like, but in the meantime, then, you know, wages go up and education goes up and, you know, it's generally, you know, it's not a clean process by any means, right? People are, I think there's always cases of abuse and that needs to be, like, watched for and everything else. But I think on a whole, it's like, economically, it's a boon for many countries, especially specifically in the manufacturing space, the electronics manufacturing space. Because I think that, like, garment manufacturing has not had that same, you know, like, you look at, like, Bangalore, they don't get the, not Bangalore, sorry, Bangladesh, my bad. You know, they just, it's, you know, that's just taking advantage, I think. So I think, but being around the technology aspect of it all, there's something about that, in my opinion. I have no data to back it up other than my feels.

**Dave Jones:** China's, China, the shift away from China is significantly different, though, from the previous, like the shift away from Japan. Japan was the dominant, you know, high volume, cheap manufacturing center. And then it was Taiwan, right? And then it was China. But the move away from Japan and Taiwan wasn't a political thing. It was because, well, basically competition, right? You know, the competition came up. So it's not like the India's suddenly come up because of competition. It's like companies are moving out of China for political and other, you know, social reasons, right? So it's, yeah, it's kind of a different move to the previous ones, which is really interesting. But we won't go too much more.

**Chris Gammell:** At the end of the day, yes, there's politics. But I think at the end of the day, it's money. Like, at the end of the day, you know, like, politics is driving the money thing. And people are going to, you know, chase low-cost regions just because that's what companies do.

**Dave Jones:** China isn't that low-cost. And, yeah, we've talked about the on-shoring phenomenon over the last couple of years where companies, you know, U.S. companies are bringing, and other companies are bringing stuff back on, manufacturing back onshore because that's actually, you know, they run the numbers. And it's actually, well, it's not necessarily cheaper to bring it back onshore, but it's like it's on par or it's not that much more expensive, but they get more control.

**Chris Gammell:** Yeah, I think, yeah. So it's like, you know. There's less time delay, less, you know.

**Dave Jones:** Yeah, and all that sort of, you know. All those benefits. And then maybe that's worth an extra, you know, 5% or something.

**Chris Gammell:** I remember seeing a stat at one point where, like, so United, the U.S. airline, like one of their top clients was Apple, just flying people back and forth to China. Oh, really? Yeah, I forget where I saw it. Wow. But it was, like, some significant amount of their, not of their revenue, but it was just a large chunk of money, you know. It's just because they have an account set up where people are flying back and forth all the time. Yeah. And, you know, probably a lot of business class, too. And, yeah. Yeah. Yeah. So, interesting.

**Dave Jones:** So, this whole Apple thing, the reason it's important is because of the profile of Apple, not necessarily because, oh, Apple is moving out, you know. Sure. Yeah, they might be the most wealthiest, one of the wealthiest companies on the planet. But, you know, in terms of, like, hiring people, you know, it's still only, you know, like, a percent or something. You know, it's like, like, it's nothing. Right.

**Chris Gammell:** You're saying of, like, GDP level type of things.

**Dave Jones:** Yeah, yeah. It's not a huge deal for China. But, on a, but from a, you know, just a, a publicity standpoint. Yeah, I guess so. You know, it's a huge flow.

**Chris Gammell:** Yeah, I mean, I think a better, a better, more, you know, less clickbaity kind of title for this would be, like, Apple is diversifying their manufacturing out of China. Diversifying, yeah. I'm guessing any localized, you know, like, they're still going to make Chinese handsets, handsets for China, rather, in China, probably, because that's just going to be the best case scenario. But if you're exporting to the U.S., then, yeah, why not go to Vietnam or India or something like that? Yeah, absolutely. If there's high, like, high talent, like you said, and, you know, lower cost manufacturing.

**Dave Jones:** I think at the moment they're only talking about their higher end products are going to be made outside or something.

**Chris Gammell:** Yeah, so, like, Apple said they're making some stuff in Texas, but not phones.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Yeah, and I think it's always interesting thinking about the, you know, the auxiliary stuff that's there, like, all of the shops that support a massive, you know, manufacturing operation like an Apple. It's, you know, I think China's better situated for that, honestly. And it would be, the most interesting thing to me would be to see are the suppliers to the Foxconn and the factory. The factory's got a huge supply chain internally that's not just parts for the phones, but parts for the factory. Is that stuff still coming from China? And I would be willing to guess that it still is, because I don't think India has the infrastructure yet. I think it'll build up, but I don't think it's there.

**Dave Jones:** No, no, it doesn't. Yeah, it has some, I'm sure. Yeah. And, but, yeah, no, it'll come. Yeah. Yep, yep. So, but, you know, there's other countries, there's Malaysia, for example, like Keysight get most of their gear. Yeah. That's where their main manufacturing hub is, you know. They get some stuff made in China, but it's mostly Malaysia. So, you know, they've got large, you know, infrastructure manufacturing stuff in place there. So, yeah.

**Chris Gammell:** Yeah. There's lots of options. Very global. Anyway. Yeah.

**Dave Jones:** Yep. So that's a big deal, I think, just from a, you know, yeah, a media point of view.

**Chris Gammell:** Yeah, you're saying like a visibility kind of thing.

**Dave Jones:** A visibility thing. It's just like, holy shit, Apple's moving out. So a lot of companies will see that, you know, a lot of CEOs of companies, oh, Apple are doing it.

**Chris Gammell:** Follow the nerd. You know, it's like. And the Apple book. Yeah, exactly. Yeah. Yeah. Yeah, I mean.

**Dave Jones:** They're all talking about it at their big CEO luncheons right now. That's right. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Speaking of Apple. So there's another article, not article, but a site that I had linked on here. A friend pointed this out to me because he was doing some recruiting and he pointed me at this Carnegie Mellon Development Center, right? So it's basically like the career center for Carnegie Mellon, which is a, you know, top tier engineering university. Where is that at? So that's in Pittsburgh. In Pittsburgh. Okay. Really, really big into robotics. I think they're like top five engineering schools in the States. And, but what they share is, so they, they do data stuff on all of their graduates. And so if you click into electrical and computer engineering here, people following along at home. I'm clicking. And then I just followed, I clicked on the masters in computer, electrical and computer engineering. So basically.

**Dave Jones:** Why don't you do masters? Just do a Joe Bloggs bachelor.

**Chris Gammell:** Okay. Sure. Sure. We'll look at bachelors, but basically they track where all of their graduates are going including average salaries, locations, job titles, employers. And it's really interesting because I was thinking, as I saw this, I was like, I would have loved to seen something like this two years before I was graduating, you know, because then you see like who's generally hiring. Of course, it's never going to be the same thing, but at least like, you know, go research them, seek them out at a job fair and then, you know, find the small ones too. I think the small ones are more interesting personally.

**Dave Jones:** Well, I'll tell you what, the bachelor one is interesting. I'm looking at the pie chart now. Where people have gone after they've finished their bachelors in electrical and computer engineering, which I think are two different fields, but you know, like anyway, they seem to lump them together. Okay. And only, well, there's only, well, there's a total number of graduates. So there's only 165. Out of 165, only 62 are employed.

**Chris Gammell:** That's right.

**Dave Jones:** Whereas 98 decided to continue on. I don't think that's that unusual. I think that a lot of people are going-

**Chris Gammell:** Education. Are going-

**Dave Jones:** You think more people are going on to masters these days.

**Chris Gammell:** Well, especially like a top tier school. So you got to imagine they have 165 grads in their senior class of a ECE program. Like these are all, these are smarty pants, you know, like they're smart kids. Right. And so a lot of them either were planning to go on or they're going for PhDs, stuff like that. Got it. That's why I looked at the-

**Dave Jones:** So you think that's a result of the caliber of the school rather than a general trend in the industry. Yep. Yep. Yep. And so I actually ended up, I ended up going back. Makes sense.

**Chris Gammell:** So the same friend, Chris, who shared this with me, he said that the phrase to look for, and you can look for this at other schools too, I'm pulling it up, sorry, is, come on, Reddit. Reddit. What did, I didn't, I didn't write it down. Darn it. I'll find it in a little bit, but there's a, there's a search term for it of like, so that you, maybe like destinations or something like that. Mm-hmm. And like, that's how you could find it. So I actually found it for my school as well. So I went to Case Western. Oh, okay. Right. And, and you could find it there too. So.

**Dave Jones:** Nice. And average salary for those playing long at home and with a bachelor's is 106,000. That'd be Yankee bucks.

**Chris Gammell:** Yeah. Which is definitely, I mean, I think the average when I was-

**Dave Jones:** Well, the salary range is from 52 to 146. Right. Of 40 salaries reported.

**Chris Gammell:** Yeah. I think-

**Dave Jones:** So only 40 out of those, 62 employed would report their salaries.

**Chris Gammell:** Right. Yeah. That is lower than I would have guessed out of the, I guess 60, yeah, 40, yeah, two-thirds. That's not bad.

**Dave Jones:** And what does it go to? Oh, okay. It jumps from, it only goes up by an extra 10 grand. No, five grand. Only goes up by an extra five grand if you got that master's. Yeah. As an average. So, yeah.

**Chris Gammell:** And I think the big thing, so the thing-

**Dave Jones:** Well, even the salary range, it's from 60 to 155. Yeah. So, it's basically straight off the bat, as a graduate, it doesn't really matter if you've got a bachelor's or a master's in terms of salary. There's really hardly any difference in terms of your first job.

**Chris Gammell:** Hmm. That's an interesting, yeah, that's maybe, I think, specific to CMU. That's what the data shows. Right. I think that's specific to CMU. Because it's like top-tier graduates who are leaving anyways. Now, the other thing that I wanted to point out about this is that this is an ECE program, right? So, this is electrical and computer engineering. They have a separate computer science department.

**Dave Jones:** Oh, okay.

**Chris Gammell:** Got it. Look at all, read some of those job titles off. Which ones? The computer science? No, no, no. So, in this ECE report, right? So, I was surprised by this is an electrical and computer engineering group, right? This is the school at CMU.

**Dave Jones:** Oh, software, software, software, software. Is that what you're getting at? Exactly right, yeah. Yeah, yeah, yeah. And it's like-

**Dave Jones:** So, there's five went down. There's software. Yeah, there's one product development engineer. Yay, in South Carolina. Good on you. One applied machine learning research scientist. But software, software. One design engineer. Keep in the faith. One firmware engineer.

**Chris Gammell:** Right.

**Dave Jones:** Yes. Come on. Is there a PCB design, like, you know, basic design engineer? I think these are good.

**Chris Gammell:** Well, like, so you think about, like, so I think about young, young, young, influence, not influential, the other way around. Easily influenced Chris, right? I didn't give a shit when I was leaving school. I cared about money. Like, I'm going to be honest here. I cared about money. And that's why I ended up going to work for Samsung. You know, like, and it was interesting too, of course. But, like, I was chasing money. Like, and, like, I think about that too. Like, people come-

**Dave Jones:** How much money did you get at Samsung? How much was that? That was your first job, right?

**Chris Gammell:** That was my first job. I think I started at, like-

**Dave Jones:** How much money did you get at your first?

**Chris Gammell:** I think it was, like, 55, 53. Yeah, right.

**Dave Jones:** Yeah.

**Chris Gammell:** This was 2006. So- Right. 13 years ago. 53, I think, and then there was a bonus.

**Dave Jones:** And that was good money at the time?

**Chris Gammell:** It was not as much as I hoped for. I'll tell you that much. And I know that one of my classmates who had a master's, one of my fraternity brothers, actually, he had a master's degree. And he, I think he got, like, 15 grand, 20 grand more than me or something like that. So they had, like, performance bonuses and stuff like that too. But, like, yeah, that was definitely at different levels. Chris was not a top recruit, Dave. I was among 200 grads too. Like, that was, like, the other thing. Oh, yeah. Yeah, yeah, yeah. I didn't have much, yeah.

**Dave Jones:** I love this. Somebody's job title is GPU driver architecture engineer. No, you're a software engineer. It's like, I'm sorry. That is. Driver architecture engineer. You're a software engineer. Come on. So, yeah, that's, wow. Okay. What about the bachelor's? That's, yeah, software, software, software. So marketing. Oh, you bastard. Tennessee. Yeah, bugger off to Tennessee. Easy, Dave. Easy.

**Chris Gammell:** Here's the term that it is. So student destinations is the search term.

**Dave Jones:** Yeah, student destinations.

**Chris Gammell:** So that's how you find, if you do, like, student destinations and your school or a school you're interested in, that's the way to, that's, and so, excuse me, I was looking through others just trying to find, you know, other stuff out there and I found a couple. I didn't find much data. I think this is, like, a newer trend, but I really like it. I mean, this is great. This is great data. Like, really great for, like, because you're just seeing, like.

**Dave Jones:** Yeah, but it's not great that everyone's getting into software.

**Chris Gammell:** No, no, no. I'm saying it's great as an educational tool.

**Dave Jones:** Oh, I know. It's fantastic.

**Chris Gammell:** Yeah.

**Dave Jones:** Hey, somebody's an autonomous driving software engineer at NVIDIA.

**Chris Gammell:** Yeah, I believe that. They're selling a lot of those Jets and Nanos and they're doing all the visual, you know, camera outside.

**Dave Jones:** Oh, who's working at a company called Okie Dokie?

**Chris Gammell:** I saw that one too. Blockchain engineer.

**Dave Jones:** Blockchain engineer at Okie Dokie in Singapore. This is great.

**Chris Gammell:** Yeah, so there's a couple years worth of stuff. There's other schools.

**Dave Jones:** No, hang on. Hang on. Winner, winner. Chicken dinner. Literally. Literally chicken dinner. Continuing education destinations, right? Some of you know, people have gone on to computer science, robotics, technology ventures, mechanical engineering, all that sort of stuff. Oh, I know where you're going. Somebody's gone. Bugger it. Diploma in food and wine. I'm going to Lee's School of Food and Wine. Good on you. I went, ah, none of this engineering rubbish. That's right. I got my ticket. They'll probably end up earning more.

**Chris Gammell:** The smartest one of the bunch, Dave. The smartest one of the bunch. Yeah, right.

**Dave Jones:** Got into food because everyone still has to eat, right? But when the world's gone to crap and everyone's stopped using their eye farting gadget, then, you know. It's great. This is goldmine.

**Chris Gammell:** Yeah, yeah. It's really great. What did we learn from that? You had mentioned Okie Dokie, which is a blockchain startup.

**Dave Jones:** Oh, yes. Segway, segway.

**Chris Gammell:** So this comes from, I had asked on Twitter about, you know, what's going on in the electronics world. And Paul Gerhardt has been working on this thing called, I'm not sure how many people, but it's called Kong.cash. Now, I'm about to say some words that I don't like, but this is a cryptocurrency idea. Boo. Yep. But it is gorgeous. The way that it was, the hardware that he made is just gorgeous. So, Dave, why don't you paint a little picture of what this thing is?

**Dave Jones:** It is a physical polymer type note, but it's actually a flex PCB. So just imagine a very colorful, like the Australian colorful currency, our polymer note currency. So it looks like that. It's all beautifully colored. And it's a, like, and it's a Kong is the cryptocurrency. And it's like, has like 500 Kong note. You have a 50 Kong note. You have a 10 Kong note. And it's a flexible note. And it has an embedded RFID chip on it.

**Chris Gammell:** Yeah.

**Dave Jones:** Which generates its own, which generates, holds the private key and generates the public key all within the note itself. So you can physically hand it over to another person as, like, cash, as a fiat currency, kind of. Right.

**Chris Gammell:** Yeah, it's tied to Ethereum, which is like the, I think that's the one that has, like, a lot of developers and API stuff, right?

**Dave Jones:** Most of the cryptos out there, except for ones that have their own system, are on the Ethereum blockchain because it has the smart contracts and other technology inside the Ethereum blockchain. So, yeah, it relies on the Ethereum blockchain to work. Yeah.

**Chris Gammell:** I am the biggest skeptic. I get it that, you know, academically it all works, crypto works, whatever, whatever. I'm a skeptic of a practical implementation, but I love this just because…

**Dave Jones:** It works. People buy stuff on my store with…

**Chris Gammell:** No doubt, no doubt.

**Dave Jones:** I'm just saying… You can get a discount, by the way, if you go to the eBlog store, you get a discount for crypto.

**Chris Gammell:** Okay. Sorry. It's the grandmother test that it doesn't pass the…

**Dave Jones:** Right. No, no. Of course it doesn't pass the grandmother test.

**Chris Gammell:** Go on. But something like this, I mean, like, if… So, again, if crypto ever took over and you had to do something where you had physical stuff, you know, something like this is interesting. At least, again, as an academic…

**Dave Jones:** It's fascinating. As I said, off the bat, I said I don't see… Sure, sure. It looks fantastic. It's novel, but I don't see a future for this. Right. And so, another thing is… But it's fantastic. I want one. It's just… Yeah. It looks gorgeous.

**Chris Gammell:** There's a tweet we'll link in, too. Like, these things are like… So, like, you know, it's got a fancy animation on the site. But then, like, there's a tweet of an actual piece of Kong cash or whatever. Yeah. And it's just… Like, it's UV printed over flex PCB. It's like, oh, my God. Like, multicolor. Like, it is… Yeah. It looks fantastic. Nice design, too. Like, it's really… It looks…

**Dave Jones:** And it's got somebody's, like, head on… Like, a Greek head on it or something. Whose head is that, you know? And one of my first thoughts was that, like, can it be used as a wallet? Can you, like, charge it up with currency and do that? Because if you could do that, technically, that would be possible. But then that would be pointless of printing a note which says 500 Kong. Yeah. Yeah. It's just you may as well have it on a… You know, yeah. Yeah. It just defeats the entire purpose. And then my next thought was that you could physically… Because everything's stored within the chip, right? So, you could physically hot air the chip off, move it from a 500 Kong note to a 5 Kong note and all vice versa. And, you know, bingo. You've got to counterfeit.

**Chris Gammell:** And people thought that learning how to use a hot air pencil wasn't going to pay off in the end. You know what? Right. Yeah, yeah. We're going to show them.

**Dave Jones:** Yeah. I'm going to counterfeit my 500 Kong notes now with… Replace them with five Kong notes. I'll make a killing.

**Chris Gammell:** So, this is an interesting chip, too. So, the ATEC 608… It's A-T-E-C-C. So, it's in a secure storage thing. I'd actually looked at… I'd written an article about this. I didn't know much about it, but I wrote an article about it for the Things Network a while back. The idea is it's like a secure storage element. Like, and… Yeah. Who makes it? Microchip? Uh, but it's like… I don't think there's any security vulnerabilities with it found yet. I think I talked to Colin O'Flynn, past show guest about it. Because, you know, I was wondering, like, side channel type of things on it. Of course. I don't think anyone's gotten that stuff out of it yet.

**Dave Jones:** Right. Interesting.

**Chris Gammell:** So, yeah.

**Dave Jones:** And is it a physically secure chip as well? Does it have, like, the little micro mesh in it and all that sort of stuff to stop and attack with acid and all that sort of jazz?

**Chris Gammell:** I don't know. I should probably look at that. You don't know? Anyway, it's cool. So, I see these things popping up all over the place. So, like, anything that's, like… So, I saw a reference design that was talking to, like, AWS and it has one of these on there. And it's used in, like, Google Homes and similar things like that. Basically, it's like a key manager for, you know, getting stuff online. Yes.

**Dave Jones:** One of those, yeah. One of those USB key manager sticks. So, you carry around your USB stick. You stick it in and it gives you your password access to everything. Yeah. Is that what you're talking about?

**Chris Gammell:** It holds, like, the secret key and then I think you do a challenge of… Boy, I'm out of my element here. You thought crypto was going to be bad or RF. Wait a second. Chris is going to talk about cryptographic generation of keys. Yeah. Yeah. Yeah. So, anyways, we'll link the data sheet in. How about that?

**Dave Jones:** Anyway, Kong.cash. Kong.cash. It is. I didn't know there was a .cash extension.

**Chris Gammell:** Oh, yeah. You had imagined there's someone…

**Dave Jones:** I'm going to have to buy eevblog.cash just because… It's cash. And I'm cash fanboy. I'm a cash aficionado. I did a wallet review.

**Chris Gammell:** Yeah?

**Dave Jones:** I've branched out into wallet reviews. Oh, I saw that. I didn't watch it. Sorry.

**Chris Gammell:** It didn't grab my attention, Dave.

**Dave Jones:** No, I'm sure it wouldn't have. That's all right. I just did it because I could. You know, it's one of those things. And, yep. Anyway.

**Chris Gammell:** Well, we'll link that into the wallet review. It was, like, a really thin one or something?

**Dave Jones:** Yeah. It was one of those micro… Yeah. The world's thinnest wallet.

**Chris Gammell:** I love that teardown you did. The millivolt meter thing.

**Dave Jones:** The millivolt… Oh, I got taken to task. I got taken to task by the fanboys.

**Chris Gammell:** Okay. Well, first off, let me just… How dare I… Let me promote the video first. Okay. If you want to watch Dave freaking out about hinging units for, like, half an hour… Half an hour, yeah. It's very fun. Yeah. It was really cool construction. But you're saying you got taken to task for what?

**Dave Jones:** I got taken to task because all the fanboys out there said, how dare you just call that a millivolt meter? Oh, I see. No, it's a selectable band pass. Yeah, I called it a fancy-pantsy millivolt meter, and that's what it is. Nah, nah, nah, nah, nah. So I'm going to continue to call it that.

**Chris Gammell:** You said AC and DC, I believe, right? So it implies you need some kind of filtering system in there, right?

**Dave Jones:** It's a fancy-pantsy. You can use it as an actual receiver. Apparently, you can hook up an antenna to it, and you can selectively dial in the bandwidth you want, and it'll decode it, and you can actually tune in stations and stuff. Okay. It's actually, you know… But yeah, it's a fancy-pantsy millivolt meter. Sue me. So I'm going to continue to call that just to troll everyone. Got it. Yeah. Yeah.

**Chris Gammell:** Yeah, so people haven't seen it. Basically, it was like a modular approach. Could you tell from taking it apart that… Were those standardized block sizes? Because there's all these cans.

**Dave Jones:** No, no. Everything was custom. Everything was custom.

**Chris Gammell:** So that doesn't make sense to me, though. So from a reusability perspective, why would a designer do that?

**Dave Jones:** They don't care about reusability.

**Chris Gammell:** Okay. So it's not modular in the case of wanting to reuse it. It's more modular.

**Dave Jones:** Not between products. No, they wouldn't be reusing those cans between products.

**Chris Gammell:** Like looking at a VNA or something where you see each block. Not a VNA. Any like RF design where you have like a certain element and then surrounded by nicely grounded gold areas.

**Dave Jones:** Yes.

**Chris Gammell:** It's just that.

**Dave Jones:** The schematic modules you could reuse, of course, you know, the actual circuit modules. And that's why they did it is because modular design is easy. You can break everything down. You can individually test each module. You can have different design teams or people working on each individual modules. And you guarantee when it all comes together, it's going to work because each module has been individually designed and validated and tested. Yeah. Well, you can't just whack them together, you know. Right, right. You can completely come a gutter because all the different penetrators between the modules and just the ground interactions between all the modules are going to ruin your day. Yep. Right? So it's, oh, but it's, and apparently, someone pointed out that I missed a whole level of cans in there. I didn't take part. So I'm going to have to, after this, I'm going to have to go back in and go, oh, no. There were like four levels. Apparently, I only did three. So I'm going to have to double check. But yeah, oh, it's gorgeous. Yeah. 1980s German technology. It's just, wow. Everything is a modular block.

**Chris Gammell:** Yeah.

**Dave Jones:** But I like that idea too. It doesn't.

**Chris Gammell:** The idea of like black boxing. I mean, like, again, going back to like school days too. Like, you know, they talk about like transfer functions, basically. Like you're treating each block as a transfer function effectively. And it doesn't work like that in practice, like you said. Right. But it's an interesting mental model that then, you know, that then they took to extreme with like shielding and canes and everything else.

**Dave Jones:** Well, it makes development of advanced products like this. Because this is like a, back in the day, it's like 40 grand, I think somebody said $45,000 bit of kit in today's money. Wow. Right? Just for basically a fancy, fancy. How much in Kong? For a fancy. That's a lot for a fancy, fancy millivolt meter. Yeah. Right? Yeah. And it's a level meter, technically, is it's name. Level meter. Anyway. It's a selective bandwidth.

**Speaker ?:** Yeah.

**Chris Gammell:** It's a millilevel meter. It's a mill. Yeah. The level is a millivolt.

**Dave Jones:** And where was my train of thought going on that? Oh, God. You lost me.

**Chris Gammell:** I think you're talking about like piecing things together, people working independently.

**Dave Jones:** Oh, yeah. Yeah. Yeah. PC, it's a, you know, when you're designing such an advanced product, it makes sense to make everything modular, just like they do inside spectrum analyzers, even today. They just break down the modules. And that's why you physically see them separated inside there. You don't necessarily have to do that from an electrical layout point of view. Sometimes, you know, you stop cross coupling between modules and things like that. But, yeah, it's, you know, it just makes the design easier. Right. That one's done and dusted. We've tested that. It's, and then you, because a lot of these spectrum analyzers and stuff, they are modular block designs effectively. Like one, you know, it goes into a bandwidth filter, right, a bandpass filter, and then it goes into a mixer, and then it goes into a down converter, and then it goes into a detector or whatever. You know, they're all separate functions. And so it makes sense to separate the designs out. Yeah. Both physically and in terms of your schematic as well.

**Chris Gammell:** Yeah. I think about it like most of the time, the designs I've been doing lately, at least, you know, it's like some kind of processing element at the middle, and, you know, there's not just a lot of like signal path type stuff happening. You know, it's just basically like, usually it's signal path is like input protection.

**Dave Jones:** Signal path is the word, that way. Yeah, yeah.

**Chris Gammell:** So like input protection, maybe amplification into an ADC, and you're done. You know, and then it's bits. Right, right. But like, yeah, like what you're talking about.

**Dave Jones:** And you sort of treat that as, it's so simple, you treat it as one, an entire design.

**Chris Gammell:** Yeah, it's one input, and then there maybe are other ones, but they're all going to a centralized place, which is the micro or the FPGA or whatever, right? But this is like, it's a serpentine, like, you know, block, block, block, block, maybe a relay to split it to two different places, you know, block, block, block, block.

**Dave Jones:** Do I put the block diagram in there? I'm not sure if I did. I don't remember.

**Chris Gammell:** Yeah.

**Dave Jones:** But oh my God, yeah, it's wow. There's like dozens and dozens and dozens of blocks all interconnected. It's a serious bit of kit. Yeah.

**Chris Gammell:** You should put, if you're making another video about it, you should do that in the block, the block diagram.

**Dave Jones:** Yeah, I'll definitely, yeah, I was going to actually go through the, because I got the service manual, I was going to go through it, but the video was already long enough.

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** So, yeah, which has all the block diagrams and stuff. So, yeah, I'll do a second video and include that.

**Chris Gammell:** Yeah, and so, speaking of signal path, if you watch like Shariar's videos, he does that all the time too, where he breaks it down into like blocks. And then he says, you know, this is the section that's doing a filter or a amplification or whatever. And it matches that pretty well, I think. Yeah. So.

**Dave Jones:** Because that's how all these RFE things work, which is what he's into. Right. You know, it's like, yeah. Yeah, it makes them interesting too.

**Chris Gammell:** Like, it's not just, you know, if it's, you look at like an SDR, you're like, oh, look, it goes into the ADC. And then there's a DAC that goes out the other side. Yeah. Okay.

**Dave Jones:** But if you look at how to lay out a schematic, the video I've done, you know, like how to do a proper schematic and stuff like that. One of my things is to like draw modular, like draw a box, a group, your schematic together in functional blocks and draw a box around that block and give it a label. This block does this.

**Chris Gammell:** And the guy, get fans out there will know about hierarchical schematics, which allow you to do that exact thing. Yeah, of course. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** So.

**Dave Jones:** Yeah. That's the way to go. That's the ticket laddie.

**Chris Gammell:** Yep. That's good. Well, that's cool. Are you actually, does it, does it, did you get it working? I saw you said the button doesn't work.

**Dave Jones:** No, no, it doesn't. No. So it's just a turn. No, it's, it's completely dead. It's a lot of effort to get it apart. A lot of people are asking to repair it and stuff.

**Chris Gammell:** So if I had 45,000 Kong in 1980 dollars, what would I be buying it for?

**Dave Jones:** You'd be buying it for telecommunications. Got it. Testing the lines and the systems in telecommunications stuff. So you can dial in a particular bandwidth within like a particular part of the biggest old school analog telecommunication channels. They're broken up into different bands. Right. So you can like tune that one band and then listen to that one band and check the signal level in that one band or, you know, I'm sure there's more to it than that.

**Chris Gammell:** No, and it's probably at a millivolt or so. Yeah. So that's good. It makes sense that you would have a millivolt meter.

**Speaker ?:** Yep.

**Chris Gammell:** That's great.

**Dave Jones:** And so, yeah, somebody brought this up on the EUV blog forum. They said, oh, I need a new multimeter. You know, like it was in the beginner section. I, you know, can anyone recommend a, a multimeter that does that, you know, I'm looking at measuring like hundreds of microvolts AC signals. And then I went in, aha, multimeters don't do that. That's what AC millivolt meters are for.

**Chris Gammell:** Oh, okay. Yeah. Yeah.

**Dave Jones:** And so I, I put links to AC millivolt meters and like uni, I found even, I didn't know this, uni T, you know, maker of the finest cheap ass multimeters. They did a dual display AC millivolt meter. I don't think you can buy it anymore. But, you know, AC millivolt meters, people, if you actually remember them at all, or if you've ever used one, most people have never ever used an AC millivolt meter in their life. But they're usually old school analog ones. And you can still buy analog AC millivolt meters. Brand new.

**Chris Gammell:** So I know it would just be like a power level on that or it actually, what would it be?

**Dave Jones:** It's basically a signal level. It doesn't do all the fancy, fancy stuff that this Wandel and Galteman $45,000 one does. Sure. Basically, yeah. It just measures low level AC signals over the range from, you know, microvolts. Right.

**Chris Gammell:** You want to see if your signal is getting through and if it's at this, maybe at a certain band, a certain frequency or whatever. Yeah. That's interesting.

**Dave Jones:** Yeah. Because the problem with multi, with your general multimeters is that the true RMS converters in there, they aren't good at low level signals. If you actually go read the fine print, the little asterix inside, a lot of people don't know this, little asterix inside your user manual specs for your multimeter, it'll say, oh, the accuracy, you know, your AC range, your AC millivolt range might be accurate to half a percent or something. You know, that's because, you know, like you can't get 0.005 percent.

**Chris Gammell:** Right, right, right. Yeah. Because your cap's not huge. You don't have like a really high quality caps in there and stuff like that.

**Dave Jones:** No. And anyway, so it's half, say it's half a percent, but little asterix says only above, you know, 0.1 percent of full scale or something. Oh, interesting. Right. So if you're measuring real, so if you get under a threshold limit, the converter goes all wobbly and doesn't know what it's doing. You know, it can't do it because it's got hectifiers in there. It's got to rectify it and everything else. So it gets a bit nonlinear down in that low level region. Right. So, you know, some meters are different. And of course, so the only other way to do that is to use an AC millivolt meter, which doesn't measure AC the same way as a multimeter, a digital multimeter does with its true RMS converter, or you need a scope with a pre-amplifier front end. Right.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** You know, that's the only way to do it. So AC millivolt meter, the long forgotten.

**Chris Gammell:** Yeah. You mentioned who was the, you said Wave Tech? Not Wave Tech. It was Wave someone. Wave.

**Dave Jones:** Wave Tech. Yeah. Is that who they bought? They, Wondell and Galteman bought Wave Tech. Technically, it was a merger, but you know, yeah, right.

**Chris Gammell:** Is it?

**Dave Jones:** We have a segue for that. Yes. Onshape. Onshape, which is the online 3D CAD tool. Oh, I didn't realize.

**Chris Gammell:** I was wondering why you posted this before the show, but I know why, because you guys use it.

**Dave Jones:** We use Onshape. We use it for the micro supply case. And they have a free version, if you don't know, you know, it's free and it's an online tool. It works in the browser. David used to, like he loved it at first and then he started using it like in depth to design the micro supply case and then he started swearing and, you know, and yeah.

**Chris Gammell:** Yeah, that's how a lot of tools are. I mean, they start great and then you get deep into them and the veneer comes off. Yeah.

**Dave Jones:** But anyway, no, he finally figured it out and made it work and it's, you know. But anyway, yeah, they've just been bought out by a company I've never heard of, PTC.

**Chris Gammell:** So PTC is Creo. They made Creo, which used to be Pro-E. So Pro-Engineer. Oh, Pro-E. Yeah, they changed the names a bunch.

**Dave Jones:** Oh, Pro-Engineer. Oh, okay.

**Chris Gammell:** So PTC, I think, is a bigger company, but they made Pro-E. And that's how, yeah, that's.

**Dave Jones:** Right. So Pro-Engineer is now Creo.

**Chris Gammell:** That's right. Yeah.

**Dave Jones:** Oh, God. Okay. Right. Okay. Fair enough.

**Chris Gammell:** I just always know because I always say PTC Creo. That's like when I hear designers talking about it or mechanical posts talking about it.

**Chris Gammell:** Yeah. It makes sense, you know. I had no idea. Yeah.

**Dave Jones:** That's right. Yeah, because that's a standalone product. They wanted a cloudy solution. That's right. Yeah.

**Chris Gammell:** Well, they might have something there, but yeah, I'm not sure. Yeah.

**Dave Jones:** It's not cheap. Anyway. That's for sure. Right. Got it. Yeah. Creo's nice.

**Chris Gammell:** I mean, they're all, you know, fancy.

**Dave Jones:** Oh, yeah. No, when you pay top dollar for that, they're all nice. Yeah.

**Chris Gammell:** Of course. But yeah, we'll see if the free stuff sticks around. Yeah. I keep hoping. Yeah. I keep meaning that I don't have anything that I need to like make right now. Last time I did a 3D design, I was just doing it in Fusion, which is, you know, good. Right. But on my list is to.

**Dave Jones:** So do they, they have a free version, right? Fusion.

**Chris Gammell:** Fusion has a student and hobbyist and startup version. Right. And so it's like, if you're not making more than $100,000 in a year, then you're a startup. Right. Or something. I don't know what the numbers are, but it's startup and it's, yeah. So they have a free version. Right. But, you know, free is always, you know, it's until they decide not to be free, which is going to be, you know, potentially the same thing for Onshape, right? So my, I won't call it a New Year's resolution or anything, but the next major design I do, I want to try out FreeCAD some more too, which is a, you know, open source just hasn't, it's tough. It is visual stuff. It's just not, FreeCAD is better than it has been. It's definitely improving, but it's, you know, 3D stuff is just tough.

**Dave Jones:** But it's not quite there yet is what everyone tells me.

**Chris Gammell:** Yeah. Yeah. And I tried out the scripting one too. What is that called?

**Dave Jones:** Oh, yes. Open SCAD.

**Chris Gammell:** Yes. Yeah. I tried that by, founded by, or started by former guest Clifford Wolfe. Oh, really? Yeah. Isn't that great? There you go. Yeah. Yeah. He doesn't maintain anymore, but he started it, so. Right.

**Dave Jones:** Okay. Cool.

**Chris Gammell:** And it's, I'm not a software person, as we may have, we may have talked about in the past. And software people love it though. Like, I don't know why. Right. Right.

**Dave Jones:** Yeah, I know. Yeah, they get all, yeah, they get all moist about it. Yeah.

**Chris Gammell:** It's a lot of like nested functions and stuff like that.

**Dave Jones:** Yeah. All that sort of jazz.

**Chris Gammell:** It's an interesting idea for sure. I mean, like the idea of like parametized models and stuff like that. Kind of cool, but yeah, not quite there yet. Right. Yeah. So do you think this will impact you though, the buyout or no?

**Dave Jones:** I don't think so. We'll, you know, we'll see. Like there's no point at the moment to panic and extract our design out. Right. Yeah. You know, move to something else.

**Chris Gammell:** Yeah. I mean, if you have the.

**Dave Jones:** I'm sure there'll be forwarding, like this is a huge company. They aren't going to suddenly, you know, go bust and the tool's just going to stop.

**Chris Gammell:** Right.

**Dave Jones:** Working. Yeah. I think that. Or they'll suddenly change direction.

**Chris Gammell:** I think if they change direction too, you're like, all right, I guess I'm going to pay. You know, this is like the business thing. Yeah. Right. Oh no, of course. Yeah. I would pay to get my business. Open source projects and stuff like that. If they're dependent on the, the, the kindness of a, you know, a, you know.

**Dave Jones:** But, but if I have 10 years time, do you expect your online browser on shape design to still be working? You know? Right. Yeah. Yeah. That's a good question. I think. Maybe five years, but 10 years down the track, you know, it's like, yeah. Right. Yeah. It's one of those things, but that's the, you know, that you, you know, that going in, if something is web based and you don't have the executable file that you can back up and store on your own hard drive forevermore and keep it running forever, then that's the, you know, choice that you make. Yep.

**Chris Gammell:** Definitely.

**Dave Jones:** So there's nothing you can do about it. So, can we talk about dumbass, dumbass design?

**Chris Gammell:** Sure. Please. Who are we talking about here?

**Dave Jones:** Tesla. Oh, Tesla.

**Chris Gammell:** Tesla. What about them?

**Dave Jones:** Yeah. They're a flash memory. Oh yeah. That thing. Is all dying. And the black screen of death in four year old Teslas, apparently. Apparently a lot of Teslas are, cause they use flash memory of course, and flash memory has a limited number of rights. And of course, Tesla love to log stuff. So they're logging everything, continuous furiously right into this flash memory. And four years later, all these cars are dying because all the flash, they've exceeded the number of flash rights. It's like, this is, this is like basic design, I know one, you know, school boy level mistake.

**Chris Gammell:** Like I, I would make this mistake, but, uh, yeah, I would assume that a big company wouldn't. Yeah.

**Dave Jones:** It's exactly, I, I can't believe that somebody at, at Tesla didn't go, um, hi, there's a limited number of rights in this flash and we're writing to it a thousand times a day.

**Chris Gammell:** Like, you know, you know, if there's any Tesla engineers or former Tesla engineers out there listening, what would be a good email address here? Secret stuff about Tesla at the amp hour.com.

**Dave Jones:** Yeah. Yeah. Right.

**Chris Gammell:** Um, yeah, I'm sure there's a reason for it. Like I doubt it was an oversight. I'm sure it was more of a design risk and then it was just a, like, if you didn't, maybe if it wasn't tested for it.

**Dave Jones:** No, no, no. It wouldn't be a design. Like if, if you showed the numbers to some, like if an engineer spoke up at a meeting and said, Hey, look, I've, I've ran the numbers. We're only going to get four years use out of this and then it's going to die. Like no one's going to go, Oh, don't worry about that. You know, like it's, it's either they were too scared to speak up. I can't believe there's nobody there who, who didn't calculate the number of rights. I mean, it's just, it, it's so fundamental. Everyone knows about this, especially at that sort of design level.

**Chris Gammell:** You know, I think it's easy to look at, I think it's easy to look at a design decision after the fact and say like, Oh, how could they have done that? But then, you know, like I made mistakes. I'm sure you made mistakes. You know, like I just, I think the bigger thing is that it's a team. Yeah. With a team, it's, it's harder to believe, but you know, it slips through the cracks. Um, I would be, I would be very interesting to interested to know if, um, if this was not, not that it was a surprise because it would surely it was a surprise or else they would have fixed it, but like, yeah, well, just what the thinking was there. Because if there was like, Oh, well we expected maybe like the logs went up, you know what I mean? Like if a software engineer decided to log more stuff. Right.

**Dave Jones:** Log more frequency and nobody. Right. So it passed the initial design thing and they went, Oh yeah, we've calculated it's going to last, uh, 20 years. Yeah. And that's longer than the life of the car. And then the software people nine, 12 months down the track actually implemented these software updates. And then without going back to, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** They write more frequently. The other surprising thing about this was.

**Chris Gammell:** Without consulting the hardware engineers. I don't see it in this one. I think it's on a different article, but they said the replacement cost was like 1500 bucks for the board or something like that. I was like, Oh my God.

**Dave Jones:** Yeah. Well, cause you can't get, officially you cannot get Tesla parts.

**Chris Gammell:** Well, I don't need Tesla parts personally. I can't afford a Tesla.

**Dave Jones:** Yeah, but no, you can't know. But even, even repair places can't get them. Apparently they, they have to scrap old, you know, Teslas that have been in accidents or whatever. They, they just vulture out all the parts because that's the only way to keep your Teslas going. There's a whole black market for all these, you know, aftermarket Tesla parts and these companies that are sprung up that specifically, um, you know, hack Teslas and, and because often you have to hack them to, uh, put in these car parts from a different car or whatever, you know, you've got to hack the serial number. If you've got to hack something else, I don't know the thing behind it, but yeah, it's, um, it's, it's not good. Um, wasn't the car covered under warranty? Like, you know, in usual cars are like five years plus warranty these days. Wouldn't you just.

**Chris Gammell:** Dave, I'm going to sound like a yuppie here, but I do not have a car anymore. And my only car I've ever bought was from 2004. Right. Okay. So, uh, yeah, that's all gone. Uh, are they covered by warranty that long? I guess. I don't know. All right. I'm always surprised.

**Dave Jones:** Well, apparently not because they're going to these unauthorized repair places because that's the only way to get their Tesla back on their own. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** And if you had that big investment, you'd be like, no, no, no, I'm, I'm keeping this. This will work. Yeah, exactly. I will get this working right now. Um, I, I think we, yeah, I, I remember we talked about this. This is a long time ago, but it was like, I was always surprised that they didn't have removable screens. Do you remember when you talk, remember we talked about like tablets? I always thought that would be a good idea of like tablets or like removable consoles and stuff like that.

**Dave Jones:** Oh, so you're, you're talking about the, the Tesla screen to rip it out and it becomes a tablet. Yeah.

**Chris Gammell:** I mean, well, not to become a tab. I don't, I don't need like a piece of commercial stuff. I just mean like a, like that stuff, it feels like everything is so because of sourcing issues. Right. Right. And I'm not sure I stated this nuance back in 2011 when we were starting the show or whenever this was, but like, because of sourcing issues, thinking about like a screen is so far, you know, like display technologies are so leading edge and sourcing for automotive with all the testing requirements, everything else is so trailing, not so trailing edge, but definitely not leading edge that like, that they wouldn't have been replaceable in the first place. Like that always blows my mind and I'm, I'm sure there's reasons for it, but like this kind of points to like a replaceable unit, you know, at some point, like the fact that it's not.

**Dave Jones:** This is where the car companies, you can't just go, Oh, my LCD is filed. Oh, let's just get another off the shelf one from a manufacturer or something. It's like they, they have to manufacture these at the time of the car and they keep them in storage. They keep, you know, this is how all your Toyotas and your Fords work. They, they manufacture, you know, a million cars and then they manufacture a million spare parts and they keep them in massive warehouses of all these, you know, spare parts. And that's, and that's how it's going to work here. I'm sure. Yeah. So there's, I'm sure there's a warehouse full of LCD, Tesla, LCD screens somewhere.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? Yeah. That's if they are a proper company and they, automotive company and they thought that far ahead, you know?

**Chris Gammell:** So I guess the better question is then I, I don't, I don't know how to do this stuff. Like what would have been the better way to do this? So like, so say you had these massive amount of logs, why, how would you, would you put a different hard drive in there or something? Like, I guess, is it overwriting itself?

**Dave Jones:** You would use a different technology. You would use an FRAM or you'd use some other technology and then, and they, or you buffer it. The other way, the traditional way to do it is you buffer it during the day. Okay. If you need to write logs a thousand times during the day, you don't write a log each time. You write it to even some battery backed SRAM somewhere, you know, you physically write it to, and then you do once a day, you run a little, you know, thing, which then dumps it once. So you're writing just once per day instead of a thousand times a day. That's that, that's the traditional workaround for this. So.

**Chris Gammell:** Yeah. This seems weird to me, right? So like, yeah, I imagine that like, so just thinking about like Linux systems that I play on, which is not great, right? They said this is just like.

**Dave Jones:** Sorry, if people don't know, this is an E, E, E, E, M, M, C.

**Chris Gammell:** Yeah.

**Dave Jones:** E, M, M, C memory. So they're using it like a hard drive, you know? So, so the software engineers didn't care. They just go, oh, I'm going to save it to the drive, save it to the drive, save it to the drive. Right. Right. And the, and the thing's wearing out.

**Chris Gammell:** Yeah.

**Dave Jones:** So yeah, it's, so it's more high level. It's not like a low level embedded, you know, pick chip with its, you know, 32 K of flash memory inside it. It's, you know, a high level operating system.

**Chris Gammell:** It's got 512 gigs of flash or something on there, right? Yeah.

**Dave Jones:** Something, yeah. And, and it's appearing as a, as a C drive or whatever for some Linux operating system that's running. I don't know what's running. Yeah.

**Chris Gammell:** It's, it's, well, some of the tweet, tweet comments are about Linux. And like, and so like my, no, limited knowledge of Linux is just that like, you know, there's slash VAR slash log, right? That's like where you put a bunch of stuff. And if it, you know, so like the server that the amp hour runs on when it gets hit by a, you know, like basically someone asked for a request on there, it logs all of that stuff. Right. And it's only like, there's like, it'll log everything in there. You know, it's just garbage. If not garbage, but it's, you know, it's just lots and lots of stuff for tracking over time. I, I imagine that like, this must be overwriting itself though. Right. So like in that same total amount of memory space, like even if you're, you must be clearing it out. It must be generating so much info.

**Dave Jones:** Oh, it depends. Yeah. It's clearing it out and then writing it again. So keep the last week or something. Right.

**Chris Gammell:** So I'm just thinking about like, so what would be a better way to do this? It's like, do you have a removable, like a, what is it called? Like the.

**Dave Jones:** Well, you store it offline in the cloud. The, the, the Tesla order already has, already does talk back to base, right? Yeah. You wouldn't put logs there.

**Chris Gammell:** You would spend tons of money on data then. You know what I mean? Like this is generous.

**Dave Jones:** Yeah, but no data in the clouds cheap.

**Chris Gammell:** No, no, no, no, no. Not, not in the cloud. I'm saying getting it to the cloud. It'd be going over cellular connection. I can tell you that that's, that's frigging expensive.

**Dave Jones:** No, no. That's built into the Tesla. The Tesla does that already. No, I know, I know. But they're not sending logging. The Tesla is always reporting back.

**Chris Gammell:** They're not sending Linux logging data. I guarantee that, that they are not doing that. They're sending. Yeah, I'm sure.

**Dave Jones:** No, but they could. I'm saying it's already, you know, reporting everything back.

**Chris Gammell:** No, no. Okay. Let's do a little thought here. So let's say you had a 512 gig just thing on there, right? And it's getting overwritten so many times. It's generating so much data that it's passing.

**Dave Jones:** No, it's not that much. Okay. It's not, it's not hundreds of gigs per day.

**Chris Gammell:** No, no, no. I'm not saying per day. It's not that much. So like, so okay, how many days? So it's 1200 days in a four year span, right? So let's assume that it's like, I think memories are guaranteed to like five or 10,000 writes. Right. So that means that you're probably generating like two or three gigs per day of logging data, which is insane, but it must be something like that. Right. If you were. That's nothing for a modular cellular connection. No, it's, it's nothing to do it. I'm saying the cost of doing that is insane, Dave. That would be two or three gigs a day.

**Dave Jones:** Yeah, but that's part of owning a Tesla. Two to three gigs per day.

**Chris Gammell:** Oh my God. That would be terrible.

**Dave Jones:** No. Yeah. No, it's not. I'm, I'm on a $50 plan and I get like 60 gigs. Oh, sorry. A month or something. Yeah. No, I get 90 gigs a month or something. Yeah, but it's not. I don't think it's as bad as you think it is.

**Chris Gammell:** I think that'd be pretty bad. I think that'd be a lot of data for. No, no, no.

**Dave Jones:** I don't, I don't think so. Anyway, you're, you're talking about solutions, right? That is one solution. That is one solution.

**Chris Gammell:** I agree with that.

**Dave Jones:** Is to dump it back and dump it to the cloud.

**Chris Gammell:** I think that would be a big waste of bandwidth, but yes, that is a solution. Sure. Okay.

**Dave Jones:** But it's better than your car dying, right?

**Chris Gammell:** Yeah, that's true.

**Dave Jones:** Come on.

**Chris Gammell:** Yeah, yeah, yeah.

**Dave Jones:** You're, you're, you're asking for possible solutions. That's one of them.

**Chris Gammell:** I was thinking about like removable, removable storage too. Like maybe not, maybe not an SD card or, but maybe like a SATA, SATA drive on online. You know, you could have it so that that thing pops off, right? You could have like an E-Safe.

**Dave Jones:** Well, no, look, if I was designed, if I was on the Tesla design team for this and I knew there was a limited number of rights, right? And, and it's got this computer, what's it called? The, the, the, the, the, ECU one or something, right? The ECU one module. If I was designing, charge of designing the ECU one module, I would like have a little, as you said, like a removable, even if you have to like open the bonnet or get under there or, or whatever, at least, you know, get in there and have a physically removable drive that own that, the job of that drive was only to store logged data. Right. So, so if that drive died, like, it doesn't matter. Okay. Your logged data is gone.

**Chris Gammell:** Right.

**Dave Jones:** Right. Who cares? Right. The car still works or the, or the, you know, I was going to say avionics or the, you know,

**Chris Gammell:** it's, it's drive-ionics, Dave, drive-ionics.

**Dave Jones:** Or the drive-ionics still works, right?

**Chris Gammell:** Yeah.

**Dave Jones:** All that sort of stuff still works. And, but no, this is like so integral with it that it's, uh, they're just storing it in the same drive that they're using for all the display stuff. So the displays are dying and going black and you can't drive your car or you can, or you can't charge it anymore. It's like, it's bad modular design.

**Chris Gammell:** I thought of the same, the same thing about like, well, we were just talking about removable, but then they must have like shock and vibration type concerns as well. Right. So. Of course.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. I don't know.

**Dave Jones:** No, no. But still I would know. Come on. That, no, that, that's easily solvable as someone who comes from that background. I can tell you that's, that's the least of your worries. Right. Right. No, they, they just stored everything on the one drive. It's a, it, it was a dumb ass decision. Somebody should have stepped in and said, Hey.

**Chris Gammell:** No, no, no, no, no, no, no, no, Dave, you're wrong at theampire.com. That'll get directly routed to Dave.

**Dave Jones:** And automatically trashed me. That's right. And no, it's, it's just not.

**Chris Gammell:** I think it's really tough to look at this from the outside and say that we would have.

**Dave Jones:** No, it's easy to look from the outside. Well, it's easy for you.

**Chris Gammell:** I would not have said this, but you know, Dave, you are a bold, a bold individual to say you would have gotten it right.

**Dave Jones:** Well, no, come on. When you're working on a big design team on a big product like this, your, one of your jobs is to think of ways it can. Sure. Sure. Sure. It can fail and, and how one, one thing doesn't, this would be a huge thing in automotive design. How one thing doesn't take out something else, especially in a car, which is so computer oriented like this one. Come on. It'd be like a design requirement, almost number one, that if one part, okay. If your login system dies, it doesn't stop the car from driving. I mean, good for goodness sake. Surely that would have been top of the design tree for, for, for this sort of thing.

**Chris Gammell:** I mean, I, I, it's, I just, you know, I live in a glass house of design and I shant cast stones.

**Dave Jones:** So I, I, yeah, I'm just, I'm just flabbergasted that, you know, I, I can, no, I can, I can understand how it happened, but it like, it shouldn't have happened.

**Chris Gammell:** Sure.

**Dave Jones:** Right.

**Chris Gammell:** Yes.

**Dave Jones:** Sure. Like having all your eggs in the one basket like that is just, yeah. So if one part of that dies, it's like, geez, you know, if your login system dies, your car stops driving. I mean, give me a break.

**Chris Gammell:** Yeah. It is all interconnected. So that, that, uh, that's rough.

**Dave Jones:** Anyway, anyway, uh, our, our, our is well and truly up and we haven't even talked about the chip printer.

**Chris Gammell:** We haven't talked to, you know what? We should leave the chip printer. Let's just let that one lie.

**Dave Jones:** I will. All I'm going to say is I was right 10 years ago and I'm right again.

**Chris Gammell:** Now I will say this thing looks ridiculous. Even though it's on Kickstarter. This thing looks ridiculous. Oh man. It's raised $130,000. Y'all just lost your money. Yes. Oh yeah. This is, it like said like, oh, we have eight different heads to do this stuff and do electronic stuff.

**Dave Jones:** Oh, so you're not pro this. Oh no.

**Chris Gammell:** God, no. This is, this, this is not it. This is, if there was going to be a chip printer, it's not going to look like this. And first off, they, they said things like there's N type semiconductor and P type semiconductor filament. What the hell does that mean? I think that boron doped, like, like flexi material, like that's ridiculous. This, this is.

**Dave Jones:** Well, technically you can make a piss poor transistor out of it.

**Chris Gammell:** People voted for this to troll you, Dave, but it doesn't, it's not going to work. Yeah, I know. It's not, yeah.

**Dave Jones:** I know. It's just, yeah. I'm sorry. I was right a decade ago. I'm still right and I'll still be right in a decade.

**Chris Gammell:** Well, yeah. Well, we'll see you in another decade, you know, 10 years is a long time.

**Dave Jones:** Oh, come on, dude. You're not clinging on. Yeah.

**Chris Gammell:** Interestingly though, the cost of, so we always said, you know, FPGAs, flexible stuff. This is actually something that was submitted on Twitter by Frank just before we started here. I had not seen this previously, but you know, all these cheap boards I keep bringing up on the show, like the CYPED and all this. So they have an FPGA on here that I have not seen before. So this is a new FPGA, maybe not new, but new to me for sure. It is the, I don't even know the site that this is on, Alcom Electronics FPGA. It's got. Okay. It's got 1,152 LUTs, 864 flip-flops, 72K a block SRAM. And so the crazy thing though is that the board with an FPGA on it at C Studio, you know, again, these are all pre-order, like C just keeps cranking out these pre-ordered boards. So, you know, that's the GD32 that we talked about in the past weeks and stuff like that too. Yep. Five bucks, five bucks for an FPGA board. So like, that's kind of interesting. I don't know much about it yet, but five bucks for an FPGA that, and the fact that, you know, we've always talked about there being four FPGA vendors there, you know, maybe a fifth. Yeah, well, we're not quite there yet, but just someone else new in the market is kind of interesting.

**Dave Jones:** Oh man, there's Chinese ones, isn't there? All these ones we haven't heard of in China?

**Chris Gammell:** I have not heard of any. I don't know any of any, but I think this is what this is, so.

**Dave Jones:** Okay.

**Chris Gammell:** Oh, this is, sorry, it's Gowin? I don't know what the hell this is. Gowin or Alcom Electronics? Well, I'll link them in, but. Cool. Gowin. G-O-W-I-N. So. All right. This and more conjecture in future episodes of The Amp Hour. Thank you for listening.

**Dave Jones:** That's it. Catch you next time. We'll see you next time.
