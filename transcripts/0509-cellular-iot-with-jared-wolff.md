---
episode: 509
title: Cellular IoT with Jared Wolff
url: https://theamphour.com/509-cellular-iot-with-jared-wolff/
---

**Jared Wolff:** This is the AFR Podcast. Release September 20th, 2020. Episode 509. Cellular IoT with Jared Wolfe.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Jared Wolff:** And I'm Jared Wolfe, Circuit Dojo.

**Chris Gammell:** Hey Jared, how you doing?

**Jared Wolff:** I'm doing alright, Chris. How you doing?

**Chris Gammell:** Well, I sound a little stuffy. I had a nose surgery yesterday, so I apologize to everyone out there. I will sound a little stuffy through this, but I did not want to give up a chance to talk with Jared because he's doing some cool things with cellular and sensors and, yeah, how did you get into all this?

**Jared Wolff:** Man, I've been doing this for a while now. Much like you, I went to a school that does a lot of kind of hands-on. I did a co-op program, so there's a lot more hands-on stuff going on.

**Chris Gammell:** Oh, RIT, of course. Yeah, that's up the street from me. I used to, I lived in Buffalo, so yeah, that was on my list.

**Jared Wolff:** Oh, okay. There you go. Just very much so, like what you guys talked about on the show previously, I never really learned a lot of the hands-on stuff. I actually just had to do it on my own, and that's how I learned most of the things I do. It's like all the theory and things I learned in college sort of useful, and like some of the things were interesting at the end was like most of the stuff I learned on my own, SparkFun, Native Fruit, like very early days. Great. Yeah,

**Chris Gammell:** yeah. And then, so you said you actually did like a couple co-ops as well?

**Jared Wolff:** Yeah, so I was really fortunate. I had just really good timing. I ended up working for, it was actually right like 2007, 2008, so right when everything went sour. I worked for Cisco, and I worked for Apple. I had some other stuff

**Chris Gammell:** going on too. That's great. That's really great. So, tell me about some of this companies. I mean, these are not small companies, not small names. What were the work environments like?

**Jared Wolff:** So, the co-op system at Cisco is interesting. We're basically kind of glorified labor to some extent. And like we weren't, we, I learned a lot, and I was close with the engineers, and we were able to teach us stuff and things like that, but we, I worked in the cable group, so our focus was all on DOCSIS 3 modems at the time, except it was not the modems, but actually the hardware that sits in the rack at Comcast that communicates with your modem at home. I mean, a bit, there being some repeaters and stuff in the middle. And that technology at the time was just coming out where it's like the faster cable modems, and we had to take these giant line cards and basically shuttle them between either other engineers, we had to bring them to the rework technicians. We're all kind of in the same room except for the software engineers and the other engineers. So, we were responsible for basically shuffling and moving these $50,000 line cards around. And it was actually the first time, it was really cool to see, and I was like, how does this guy do this? But and I don't know if it's a weird trend in Silicon Valley, but all the rework technicians are Vietnamese in Silicon Valley for whatever reason, at least the ones I I worked with. I know there were some like, some other ones, but the ones that were just brilliant and really good were all Vietnamese. I don't know why. But it was just awesome to just like watch them, because they could just do crazy stuff. I was describing this to somebody else the other day. They would take these chips and then they would run magnet wire to one of the leads, one of the balls underneath these parts, lay down the magnet wire, and then put the part back, and it would work.

**Chris Gammell:** Like what gauge are we talking about here? Like 40 gauge?

**Jared Wolff:** We're talking about teeny tiny. I don't know exactly what the gauge was, but it was super tiny. That actually was at, that particular instance was actually at Apple, the woman who was there, and she was just brilliant. I don't know how she would just do stuff. She's just like, what? You just replaced all of this? You just ran this wire underneath this crazy flash part? Like, alright, cool.

**Chris Gammell:** Yeah, that's great. And then Apple as well, yeah. So that's another different culture, I guess. But the, so both, both Silicon Valley though. So like, did you like make that conscious choice to jump out of Silicon Valley from Rochester or what?

**Jared Wolff:** It was just a good opportunity to learn. I'm kind of an East Coast guy at heart. I'm back in the East Coast. So I lived out there for whatever, seven, eight years in kind of total. It was an interesting experience, mostly because you're just, you know, it's a giant company. It was very exciting as an intern, but I see how soul-sucking it could be if you actually worked there full-time. Because you're like, oh, as an intern, you're like, I want to work. I want to travel. I want to go. I want to do. And then you do that as a full-time job and you have a life outside of work. It's just like, how do you do this?

**Chris Gammell:** Right. Yeah. Yeah. It's definitely like because of the long hours and the flights to China, I'm sure, right? It's just it's a lifestyle.

**Jared Wolff:** It was brutal. And one of my kind of mentors from Apple, he ended up working at Nest, one of the first engineers at Nest. He's got a lot of, you know, issues now, like health issues now that he's taking all these flights back and forth to China, kind of burning the candle both ends.

**Chris Gammell:** Oh, yeah. Yep.

**Jared Wolff:** Kind of paying for it. And a lot of this, like another one of the engineers I know who worked with, I worked with, he was another mentor. He just like flipped out. He just, he just, he after the last startup or startup he worked for, he just like screw it. He needs to kind of went off the rails and just like kind of did his own thing. It's like, like no more

**Chris Gammell:** tech kind of thing.

**Jared Wolff:** No more tech.

**Chris Gammell:** Yeah. No more tech. That's unfortunate too, because I've met some people like that as well that have burned out on tech and it's just like, and they're, you know, brilliant minds. And it's just, yeah, it's just the lifestyle. It's nothing against them. It's just, you know, they really, it, it's such a sour experience that you wouldn't want to be there anymore. If you think that, you know, you might be able to find a smaller company that maybe has better culture, but you might not, you might have the lifestyle that built up around the higher salaries of Silicon Valley or, you know, just the bleeding edge tech. And it's like, well, I don't want to go work for some like Midwest industrial company that's putting down through whole parts of their boards, you know, it's just kind of a, it's a tight spot, I'm sure. And I'm sure just about anything looks better than that.

**Jared Wolff:** Yeah. I mean, a lot of people will kill work for these companies, but there's also the other edge of the sword and the culture has changed a lot. I mean, I worked there when Steve Jobs is still alive. So people would, he would be sitting outside of Johnny and people would walk by and some people we didn't, I was just like, what are you doing? People just stand there and gawk at him and they're just across the way at Cafe Max. And like, it was just like a normal thing. Like people would just stop and watch. And I'm like, it's super weird guys. Yeah. That's just like one level lower.

**Chris Gammell:** That's not even hero worship. That's just like idolatry of us.

**Jared Wolff:** I guess. And I mean, it's just one level lower of going up to them. And I, man, I don't know any stories. I've heard of people trying to go up to them and I don't think it ended very well.

**Chris Gammell:** Well, yeah. But yeah, that's a weird, that's a weird culture, but it's, you know, so then you moved outside of it. So that's good. Let's move on to the next thing. What were we doing after Apple?

**Jared Wolff:** So after that, I went back to school, finished my co-op slash co-op requirements. And I finished the rest of my schooling. It was like another year. And then I came back out to California and worked at some startups in San Francisco. And that's where I got my first kind of introduction to Nordic and their Bluetooth chips. And at the time we were kind of integrating their NRF 8001, which was their kind of intro to, or their, it didn't have a processor in it yet. So we were just, we were, yeah, just the transceiver over spy, I think. And we were integrating that and then they were coming out with the N0 and the NRF 51. We were all kind of excited about it. We were like, ah, we don't know if it's going to work for us in this case. Only at the time it was different. We could have used their, one of the more late recent models like the NRF 52.

**Chris Gammell:** Yeah.

**Jared Wolff:** But that's where I kind of started cutting my teeth with Bluetooth and Nordic chips. I really enjoyed using them. So it was kind of love at first sight, I guess.

**Chris Gammell:** That's great. Yeah. Continuous to this day. Now you're, you're making stuff that we'll talk about here in a second. Yep. Great. Any other lessons for the startup side of things? We've had people from different startups, but it seems like the ones that you were at were maybe a little more consumer driven as well, like consumer facing rather.

**Jared Wolff:** Most of the ones I worked for are all consumer facing, except for more recently I was doing some IoT work where this kind of rich guy thought it was kind of cool to start up a company and make stuff. We even know there's no market for it, but I digress. Working for startups was interesting because you get to learn a lot. And if you thrive on doing a lot of different things and not being good at particular one thing, then those startups are good. You'll, you'll learn a lot. I like kind of more of the breadth than the depth. Like if you start asking me crazy RF questions, I have no idea. If you start asking me like even kind of like more in-depth like calculations or anything like that, it's like, hold on, let me use the internet. Sounds familiar.

**Chris Gammell:** I think we're kindred spirits in this way. Yeah.

**Jared Wolff:** Like the, I hate technical interviews. Most of the people that are expecting you to just be like, what are all the things you learned from college that you haven't used and tell me now.

**Chris Gammell:** Tell me about your third integrals or triple integrals rather. Not that bad. What if I tell you about things I actually use, you know?

**Jared Wolff:** So yeah, the, it was fast paced, but it's just as stressful as working out of the bigger job. It's just, there's different requirements on you. And you're always, I found myself, especially if we're going for a big build, I found myself going to the leadership and being like, guys, we have a long lead time parks, 14 weeks, got to order it now. And I was just like, come on, come on. I'm like doing the job of like a supply chain person, the test person, like creating all these test fixtures, everything from scratch. And I'm like the only person doing this is like, what is this?

**Chris Gammell:** Yeah. It's like, you're the, you're the reality bringer, you know, like you have to be like, no, no, it's really going to bite us if we don't order the parts at the beginning. You know, like that I've, I've had that role as well, where it's like, it just doesn't click because there's not that immediacy of it because startups are so reactionary normally of like, oh, customer A is angry. Customer B is what it wants to pay less, whatever it's like. It's hard to plan that far out in the future when you don't even have, you know, the cashflow to do that sort of thing. It's just like, that's the downside to hardware startups in general is that they're not built for, you know, the software model is so like cash light and hardware is so cash heavy. Yeah.

**Jared Wolff:** So that was, um, that was an interesting learning experience for me. And I was like, I was always the one bringing the bad news. So, uh, everybody thought I was difficult. I'm like, just like, this is the reality. Like we, we have to ship, but we need to get all the parts and the batteries and the pieces and the, to make it work. Like you can't ship half finished product.

**Chris Gammell:** Right. This isn't an app folks. We can't do an update over the air.

**Jared Wolff:** You know, no OTAs with your plastics yet.

**Chris Gammell:** That's right. Yeah. Well, yeah. The, the hidden promise of 3d printers that will probably never come to with fruition. Uh, so did that make you kind of burn out? I mean, we've talked about burnout a little bit, but like, did that make you burn out of the startups? What made you go out on your own then?

**Jared Wolff:** Yeah. So I totally burned out. So end of June, 2016, after basically carrying the project project I was working on for a while, I just said, I, I saw the writing on the wall in terms of the company was kind of sad because they took a lot of money from people. It was like, what? Oh, but I just had to say, all right, well, see you guys later. So I ended up moving out of my apartment in San Francisco and I got on my motorcycle and I wrote it for, let's see, three, four months around. Oh, wow. Okay.

**Chris Gammell:** So I went to like the highway one kind of thing. PCH.

**Jared Wolff:** Yeah. I've done parts of it before and there were parts of it I didn't do. So I didn't do the rest of those parts that I didn't do, but I also ended up going up through into Oregon, like Crater Lake, Washington, all the way up in Vancouver. I had ridden through BC and UConn Saratorty before I went with a buddy a couple of years before and that was really beautiful. But, and then I went all the way down to San Diego, LA area and just like back and forth, back and forth and I ended up getting sick in the middle of it from some crazy fungus that grows in the, in the dirt, like halfway between San Francisco and LA. Yeah. That was a surprise.

**Chris Gammell:** Yeah.

**Jared Wolff:** And nobody knew what it was. So I ended up having to fly. I was in Colorado and I fly back to San Jose because I had California insurance at the time and they thought I had tuberculosis. So.

**Chris Gammell:** And that's like six cases a year of these, right? I mean, it's like very rare this year, these days, but like. Yeah. It still does happen.

**Jared Wolff:** They forced me to stay in the hospital. And then I, I was just like on the internet, like the second day, I'm like, this is stupid. Like I don't have tuberculosis. And I looked it up. I'm like, oh, it's Valley fever. Like I have all the symptoms. I was in a place where about 30 other workers had just gotten it because they were installing solar panels. Like I, I have literally ridden next to the solar panels on my way out of there. So I was like, oh, oh, Valley fever.

**Chris Gammell:** So what do you call it? Valley fever?

**Jared Wolff:** Like Valley fever.

**Chris Gammell:** Okay.

**Jared Wolff:** I think it starts with this, the short version. I think there's something that there's something before the valley. I don't think it's Death Valley.

**Chris Gammell:** So when you said you were going to like pack up all your stuff and move out of your apartment, I thought you were going to say you move back east. But like, you know, I say riding a motorcycle for four months is like that's, that's a true burnout. I mean, like, that's like you were really burnt out. Like, yeah.

**Jared Wolff:** Super burnt out. Yeah. And then after that, I left my motorcycle in California and I went to Taiwan. So.

**Chris Gammell:** Oh, wow. Okay.

**Jared Wolff:** Yeah. For Taiwan. Man. It was three. It was at first three months and then I ended up staying there another three. The first time it was two months and then I stayed another three. So I was just like, oh, I like it here.

**Chris Gammell:** Yeah. Yeah. I've not been, but I have a friend from there. He loves it. It's very, very densely packed area, right? Just because of the. Yeah. Depends on where you are.

**Jared Wolff:** If you're in, if you're in Taipei, it's pretty dense or outside, you know, New Taipei City is all very dense.

**Chris Gammell:** And is this where you started Circuit Dojo? Is remote, like doing remote work that or what?

**Jared Wolff:** So I ended up not doing any work. I had fortunately I had saved up saved up some money so I could kind of do this. I mean, one of the things I did very early on, which really, really, really sucked was I had paid off all my school loans. I had like, I don't know, probably $50,000 in school debt, 40,000 around there after I graduated. RT is not a cheap school, as you know.

**Chris Gammell:** Yeah.

**Jared Wolff:** Yeah. So I just said, oh, all right. I'm just going to pay this off. And it has paid dividends since then. Because I'd probably still be paying it right now if I was just doing the minimum payments every month.

**Chris Gammell:** Yep. But yeah, I mean, I feel like we've talked about health care now and spending in U.S. universities and yeah, people outside the U.S. it's like, yeah, this is some of the restrictions. Honestly, some of the restrictions on starting your own business or, you know, going on your own is like, yeah, you need health insurance in the states. You need to pay off student loans if you're, you know, depending on what your financial situation was in college. Like it's it's tough. I mean, actually, I think the reason I didn't end up going to RIT is because it was going to be more expensive than Case Western was. So like Case always just gave away a lot of money. And I was like, yeah, I have to go there. And I'm glad I did. But it was I think it was between those two schools.

**Jared Wolff:** Yeah. I almost went to I think I applied and almost I got in the case and I was just like, oh, OK, I, I, you kind of touched on this when I listened to the previous episode and you're like, I kind of got lucky. It's like same here.

**Chris Gammell:** Yeah. Like choose choosing choosing electronics is like a long term kind of thing.

**Jared Wolff:** Yeah. Well, originally I was going to try to get into mechanical engineering and they're just like, sorry, no full. And here's your other option. And I was like, computer engineering. OK, I like computers.

**Chris Gammell:** Yeah. Well, if people don't know, too, I mean, RIT has this amazing like like they have a fab in house there that was that was actually one of the big things they pushed for when I was getting like looking around there is they talked about how you could work in the fab. And it was one of the bigger ones on the East Coast, at least.

**Jared Wolff:** Yeah. It's cool to walk by because we're all shared in the same shared building. So you could walk by on the way to class and people would be in their bunny suits and be holding up a wafer.

**Chris Gammell:** Yeah. Yeah.

**Jared Wolff:** And it's like, oh, this is kind of cool. Or they have they have a statue of it's not really a statue. It's actually a big piece of silicon in like a case. So like this is the silicon that's, you know, like an

**Chris Gammell:** ingot or something.

**Jared Wolff:** Yeah. It was an ingot. Yeah.

**Chris Gammell:** Yeah.

**Jared Wolff:** It's like what? And it's like it's changed so much since I've been there. And it's like there's more buildings and more stuff. It's like what? They have a whole right down the hall. They have a whole manufacturing lab, which I'm actually more interested in. So they have CNC machines, lades, like everything you can think of. And it's just like right there and it's a big glass box. So you can just like look in and see what's going on.

**Chris Gammell:** Yep. Yeah. Northwestern has that here up in Chicago, too. They have like a big innovation space. And it's like there's like the top floor. You kind of look down into it and watch watch the fellow nerds at work. It's great.

**Jared Wolff:** Ah, yes.

**Chris Gammell:** So then so then you started developing. So is this so when you say so circuit dojo is consulting for others or just building your own stuff? I mean, when did that actually start to kick in? When did the when and how did the burnout go away? Because, yeah, I've definitely felt burnout, but maybe not as long of a time. It sounds like there was a bit of a recovery for you.

**Jared Wolff:** Yeah. So when I worked when I came back to so I left Taiwan and then someone had hit me up. I'm a previous mentor from Apple. He was saying, oh, hey, we have this project. This is the IOT one. And we're doing this thing. I'm like, OK, all right. We'll do it. And I end up working for them for a little bit. And then it was like a year later. And then the the owner was just like me. I don't feel like paying any more money. You guys are done. And we're like, OK, cool. So at that point.

**Chris Gammell:** Yeah, that's not that's not fun.

**Jared Wolff:** I mean, what what like this advice for anybody is like have at least three to five months of expenses and savings. We're when working at a startup because people will paint it in the most beautiful picture. And then you start working there. And it's just like surprise you're laid off or surprise we're paying you minimum wage because we haven't got a round of funding yet.

**Chris Gammell:** Oh, wow. So, yeah, I feel like I was when I went to go join a startup, I was advised many times to ask about their cash flow situation, ask about like what's their runway and all this other stuff. And the funny thing is, is like even if you have a company that has like a two year runway, they don't want to use it. You know, it's not like they're like, well, go down to zero. It's like, no, no, no. We get to one year. There's a big chop coming. You know, if we get to six months, there's another big chop coming because we got to stretch it out. And it's like that's what I didn't quite get. I didn't quite grasp. It was just like cash by itself is not a good indicator of how fast it will be spending it.

**Jared Wolff:** No, you kind of, you have to look at their, their runway and how they're spending it and what their plan is. Yeah. Because I've worked for companies where they're like, we're going to ramp up. And then they ramped up and they ran out of money.

**Chris Gammell:** Right. Right. Because then you get ramp up and you need cash to go build all the things that you don't have it. And it's like, oh, okay. Yeah. It's almost like, what are the, what are the key turning points? It's like, if we don't ship by, you know, June 1st, then what happens? You know, that's like almost a better question to ask than how much runway do you have? It's like, you know, how much revenue do we need to have in order to, for you to keep everybody around? Because I get it from like a, you know, from a business perspective, they, they want to survive, but it's from a, you know, from as an employee, it's like, you know, I don't want to be, I don't care how many ping pong tables you have or, you know, how, how great the kombucha is, you know, it's, it's, you know, how much job stability do I have and, and, uh, and what can I do with that or what should I be planning for otherwise?

**Jared Wolff:** Yeah. That's the problem. It's like it, if you're looking for job security, go work for Apple. If you're looking for experience and things you'll never, you'll never see anywhere else, work for a startup.

**Chris Gammell:** Yeah. Yep. Right. Right. Yeah. If you never thought you'd be packing and shipping at two in the morning and, you know, running, driving somewhere. Yeah. Yeah.

**Jared Wolff:** We had to do filming for a full order of thousands of units. We were at the factory along, alongside the people at the factory doing all the work. Yep. Because we didn't have any money.

**Chris Gammell:** Yeah. Your, your time is bought and paid for by salary, salary dollars, huh?

**Jared Wolff:** Uh-huh.

**Chris Gammell:** Yeah. Wow. And so when you were doing all this manufacturing too, was that all, uh, overseas or were you doing it domestic?

**Jared Wolff:** So I've done a mix of domestic. The company, the one I really burned out at, this is the one I just mentioned where we're doing assembly. We did do the kind of the first manufacturing run actually in California. And then we ended up bringing it overseas to China. Uh, not surprised, surprise, surprise. And then we kind of started bringing up our factory there. And that's when I said, see you guys later. Like everything's up and running.

**Speaker ?:** Bye.

**Chris Gammell:** Yep. Yep.

**Jared Wolff:** Um, and then that's kind of been the theme of, of China in kind of my relationship with engineering in the past kind of 10 years when I first started there. Like, yeah, we're going to go to China. Like, this is just like a thing. Like someone, someone somewhere said, China is a really good idea.

**Chris Gammell:** Yep. It's in the NBA playbook. That's what I always say. It is like, no one

**Jared Wolff:** questioned it. I was like, when someone, someone told me or told me that I had to protect our source code and like do all these things to make sure they don't steal it. I'm like, why are we going there even in the first place? Like question mark. Hey guys. Um, I mean, now I've, I'm what, 10 years, 13, 14 years later. It's like, Oh, Hey, I actually have a choice about this. So most of the stuff I do these days are it's a local. So my manufacturer, my CM that does all the board assembly for circuit dojos down the street besides myself, which is really cool. Like I didn't realize there are so many board houses in this area. There's within my, within the driving distance of like 10, 15, 20 minutes. There's like three or four.

**Chris Gammell:** Yeah. Yeah. Usually I find that it's if you have a large, if you have a behemoth former company nearby that usually helps to sprout up a lot of like supporting companies. So like I still benefit from a lot of companies that were here to serve Motorola back in the day in the nineties and two thousands. And, uh, and so a lot of the individual companies, you know, they may have pivoted to medical or military or, you know, whatever they could do to survive, but a lot of them are still around. And I don't know if there was like a big company there that was it, there's a GE facility near you, right? Or something like that.

**Jared Wolff:** We have a lot of military here. So there's a lot of guys, um, Pratt & Whitney, which is up north. Yeah. There's, there's just like, there's like three or four different like government contractor type companies in Connecticut that you'd never think they were here.

**Chris Gammell:** Uh huh. Yep. Oh, that's cool. That's cool. And yeah. I mean, is there much of a scene? Otherwise, can you like go in and meet people that are designing electronics or is it more than just on the manufacturing side?

**Jared Wolff:** There are some cool, uh, maker spaces. They're, they're growing. So there's more coming out and some are closing, some are growing right now. It's really tough because of COVID. I actually had to, like, I was really tough for me at one point. So I was like, sorry guys. Like I kind of, I wanted to help because it's like these places need to stay open. Like these are, these are really important. Like all these hackerspaces are just super important because that's the only way people will know how to make stuff these days. Like nobody knows how to make stuff anymore. Like how do you cut a piece of wood in half? How do I change my car tire? Like what? Yep.

**Chris Gammell:** Yeah. I didn't know they're doing that in maker spaces, but I, maybe they're cutting wood in half, but they're

**Jared Wolff:** cutting wood. I'm just saying like being handy in general. Yeah.

**Chris Gammell:** Right.

**Jared Wolff:** Right. Like you ask that to somebody in San Francisco or San Francisco Bay area in general. And they just go, huh? I don't know how to do that. I just call triple A. Are you kidding me?

**Chris Gammell:** Yeah. Yeah. So how has it been? So you said you're working with a domestic manufacturer. Have you done like cost benefit comparisons? It gets going overseas or just kind of heading it off?

**Jared Wolff:** So I did, I did soon do some kind of initial quotes with a manufacturer I had visited in Taiwan and it wasn't too far off. It was only like a few dollars. like honestly, it wasn't that big of a deal. And I was, and I'm like, I'm not some big faceless corporation that needs to get every cent. So I was like, why? Why do it?

**Chris Gammell:** Yeah.

**Jared Wolff:** That's great. So I was like support local. Why not?

**Chris Gammell:** And then, yeah, I think even Jimmy that'll just drive there. If there's a problem, it's just like, oh, I'll be there in an hour. Oh, that's huge.

**Jared Wolff:** We had a, I sent out an email to my backers the other day. We had an assembly issue at the beginning and I always try to do this where we'll, we'll, we'll populate one panel and then I'm just going to kind of make sure it's all good. And we found that some of the LEDs were upside down and some, you know, and the, um, the buck boost, it was totally rotated 180 degrees. So it's just like that happens every single time.

**Chris Gammell:** Yeah.

**Jared Wolff:** It's like without fail. So we were able to catch it early and that's the best when you can do that. And then you can run the rest of the boards and there's not much of a problem except for maybe some potential assembly issues here and there.

**Chris Gammell:** Tombstoning or yeah. Just like weird flow of solder paste or something weird.

**Jared Wolff:** Yeah.

**Chris Gammell:** All right. So we should take a break real quick here and say, what, what are you building? I guess we haven't said that yet. Sorry about that.

**Jared Wolff:** No, that's okay. So right now, uh, I am focusing on building the NRF 91 60 feather. It's a cellular module. So Nordic cellular module NRF 91. And it's, we had a processor in it and also it's a low power radio for a cellular. So cat and one and NB IOT

**Chris Gammell:** and GPS and GPS.

**Jared Wolff:** Good.

**Chris Gammell:** Yeah. Yeah. Yeah. I, uh, I had first heard about that when I was working at a pest company and I was super excited about it, but that was like, two or three years. It was, I was three, three years ago now. And it, it was a very slow ramp from Nordic. And I was surprised when I started following your posts, I was surprised that it seems like it's definitely, they've definitely worked a lot of the kingstop, but what is the status of that part right now? That 91 60.

**Jared Wolff:** Man. Yeah. So I had mentioned this a while back and you might've seen this is Dave been talking about this part for probably four or five years now. And it was like very secretive. And I remember seeing pictures of it in like a Pelican case and it's like, here it is secret. Oh man. And I just, actually, I just talked to Jonathan Berry yesterday. Oh yeah. Okay. He was, he was interested in using the RF 91 and he was just like, the biggest thing that I've seen is just like, it's the networks. It's the networks. It's the issue. Yeah. It's getting all the certifications and I'm painfully learning that right now. It's like how terribly streamlined it is to even get a pre-certified module work where you can use their network. It's just like mind-blowingly difficult. And like you have to be in Linux system administrator actually get those tests to work. It's like, what?

**Chris Gammell:** Yeah. Yeah. So let's talk about that a little bit. So this is part of my past life. I was at Hologram and I introduced to those guys as well. And so, yeah, you have to have a sim, but tell us about like, what is it like to get a piece of silicon, you know, and all of the, there's support circuitry, obviously on your board. There's also support circuitry even within the NN 9160 module. What does it take to get that onto a network and like talking to towers?

**Jared Wolff:** So the NRF 91 has a whole, it's ginormous, a specific modem firmware. So I believe they're using one cord or just run the modem firmware. And the other core is running your application firmware. I could be wrong here.

**Chris Gammell:** So that's not from there. Yeah. From, from, from the promo stuff I saw. Yeah. Yeah.

**Jared Wolff:** So whenever I try to update the modem firmware, it actually takes like a good 40 seconds to a minute. Oh, wow. So it's, it's huge. Yeah.

**Speaker ?:** Yeah.

**Jared Wolff:** And so what's happening is very much so like how you're describing kind of how the, the collectile modules work, you're issuing commands to that modem firmware and modem firmware is doing some magic in there to kind of manipulate the hardware lower levels to communicate with the cell towers. And that's, that's how, that's how it's working. So they abstract all of the kind of complex AT commands and network stuff in Zephyr in the software itself. So you're not actually having to issue those commands yourself unless you want to.

**Chris Gammell:** Right. Yeah. So if you wanted to do the certification though, you'd have to be doing AT commands. Is that right?

**Jared Wolff:** The certification process, it would benefit you to know the AT commands, but for the most part, you're actually just using pre configured software, actually part of Nordics SDK. They have a few examples that you're mainly using for the certification process.

**Chris Gammell:** Got it. Okay. So what certifications are you going for?

**Jared Wolff:** So in terms of compliance, I just want to make sure the board is compliant. I'm not really particularly worried, but FCC and I said, which is Canada, they, I don't know, recently renamed it from industry Canada to I said, and also CE. So making sure that there's no EMI issues with the board and any of those regions. Those, that's what, those are my kind of big, biggest concerns. So compliance. And then also I'm working with Verizon to get the board. Okayed as a socket modem. So anybody, it's kind of like a socket modem. This is where things get hairy. It's like now that you have a processor along with the radio chip, it all of a sudden becomes a standalone thing, but you need to have some certain support for lightweight M2M for, for more over the air updates, things like that. And it starts getting hairy and also starts getting hairy when you want to use this device on their network because you have to run a certain version of Nordics SDK to make sure you're compliant with Verizon, for example.

**Chris Gammell:** Got it. Yeah. Right.

**Jared Wolff:** So there's a lot of boxes.

**Chris Gammell:** So the certification with Verizon, the certification with AT&T, there's PTCRB, are you doing that one as well?

**Jared Wolff:** So recently AT&T just came, they just, they just finished AT&T cert. I don't know if they've published that day, but it is done. And then I don't know if there's anything, there's no other domestic US carriers at the moment that you can get certified with.

**Chris Gammell:** But are you doing PTCRB as well?

**Jared Wolff:** I'm not doing any PTCRB.

**Chris Gammell:** Okay. Yeah. I mean, it's just such a, it's really crazy too, because I talked to, you know, I've talked to clients who wanted to do so in the past and I worked on the hologram if you wanted to, you know, certify their hardware. And it's just like, you just keep like, oh, I have, I have to do this now. Like I didn't even know about it. Like there's nowhere that's just like, here's all the things you have to do to get a modem certified on all these different networks, talking to all the towers, getting the right updates. And it's just like, it really is much more of a hodgepodge than I would have guessed. And, you know, our phones are so seamlessly handing off, but well, if depending on your carrier and stuff like that, but like even even roaming and stuff like that, it feels like it's so seamless and yet it's such like fiefdoms, you know, like there's a rise in fiefdom, the AT&T, the Sprint, Sprint, what's the other one? We just bought Sprint.

**Jared Wolff:** T-Mobile?

**Chris Gammell:** T-Mobile. That's it. Yep. And I mean, it's just like, it's crazy that they, and then you think about overseas as well, and it's just, there's so many different towers and operators you need to talk to. It's, it's really quite a mess.

**Jared Wolff:** Yeah. There's no such thing as a universal service or, I mean, they do have quote unquote universal SIM cards where you can bring it. And that's where like hologram comes in. They're awesome. You can go pretty much take your hologram based LTE device anywhere. As long as they have kind of 4G, CADM1 or even NB-IoT. That's kind of the advantage there. But yeah, without a company like hologram, you're kind of out of luck and you have to go to every single vendor and be like, Hey, I want to use your network. And you have to set up and get a particular SIM card for their network. And it's just a mess.

**Chris Gammell:** So yeah, it's just like such a tough thing where even right or even hologram rather, you're roaming with data there. You're not even using, you know, full speed, full capabilities that you might be with a, with a Verizon just because they don't, they wouldn't let you on the network to, to crank data like that really. I mean, you'd have to have specified cards and, and things like that. So yeah, it's kind of crazy that it's, I guess the other thing that's crazy to me is that like, yeah, they call it pre-certified modules, but like they are pre-certified, but it's still, you still have to do all these other steps.

**Jared Wolff:** Yeah. And that's the sucky part is you need to get your product and certified. And then there's also whisperings of an end software certification, which kind of totally defeats the purpose of having a module or anything. It's like, why even why?

**Chris Gammell:** Right.

**Jared Wolff:** So those are extra hoops.

**Chris Gammell:** Yeah. I feel like, I mean, like I get, I get the reason that they do it. Like they don't want spurious traffic or something that's just like spewing bad packets on the network, but like, yeah, if it's pre-certified, that means that the hardware should be taken care of that, not the software. Like I shouldn't be able to access any modes in the modem that allowed me to, you know, spew stuff on the wrong frequency or, you know, send bad data or continuously send bad data. You know, like that's, that should be at the module level in my opinion.

**Jared Wolff:** Definitely. I agree with that. And the only other thing I could say is that from what the Verizon engineers kind of alluded to is, for instance, like firmware over the air is like part of the process. Like you have to have that capability. And if you're, if your device doesn't have it, that's where it's just like, you're kind of screwed. If you, if like the network operators update their firmware and their towers, and all of a sudden your, your device can't talk to them, they have to have that kind of emergency switch where they can go in there and they can update your device. So at least it can talk to the talk to the towers. So that's just like one extra thing.

**Chris Gammell:** Would you say that firmware, you mean the modem firmware versus like your application firmware?

**Jared Wolff:** Well, that's where it gets sticky in the NREF connect SDK is that the firmware over the air stuff is actually on the application side.

**Chris Gammell:** Oh, okay.

**Jared Wolff:** Yeah. So you have to add that into your application code for that particular part of the code to work. And for you to be kind of Verizon compliant and then all the modem firmware stuff that doesn't really change. And eventually they are, I know Nordic is in the process of making it so you can do kind of firmware over the, over the air for the modem firmware, but that's kind of still in the process. Cause as I mentioned, it's huge. Now we're talking about, I don't know how big it is, but it's, it's gotta be in the upper hundreds of kilobytes, if not.

**Chris Gammell:** Yeah. Yeah. And, and like, what is that percentage wise? Like what, how much memory is on board that chip, that module rather?

**Jared Wolff:** So it has, it has one mega application space. So I don't know if that, I don't think it's split. I think that's just what's available to you. There's a lot of functionality in the NF91 is still not documented or shared. I'm curious if it has another five for like a Bluetooth. I'm just like, cause there's a lot of pins on it. There's a lot of pins on it that aren't used.

**Chris Gammell:** Right. I think they are. Well, so the 91 thingy I found out does have a Bluetooth chip on it. Cause I was talking to someone and showing them my new board. I was like, Oh, look at this. It has Bluetooth and cellular. And he pulls out his 91 thinking, which is like the little square dev board that they sell for people who haven't seen it before. And it's like, Oh no, that, that has one on there too. It's definitely already a thing. So it's not like anything was original from my side of things, but it's, and it's, it's definitely on the, that's definitely what Nordic wants to be doing is saying, Hey, cellular and Bluetooth together is a good combo. So hopefully it will show up on that singular modem.

**Jared Wolff:** I hope so. And that's what I was originally hoping that they would do. When I, when I first heard about the cellular, I'm like, wow, this is awesome. They're going to get a Bluetooth chip plus a cellular chip in the same module. And then like two years later, I was like, Oh, they don't have Bluetooth. So I think that's probably the next step. That's a logical next step, right?

**Chris Gammell:** Yeah, I think so. I mean, well, the crazy thing too, is that like internal of these chips, like they're all SDRs internally, you know, but I think it's more of the muxing and, you know, the antenna capabilities you need to have on the outset, you know, you'd the, I don't think the cell modem, sorry, the cell antennas that are recommended are either wideband, but I don't know if they're, they're tuned enough for 2.4 to be useful. Cause usually the cell modems are what, like 18, 1900 megahertz for the high end of GSM, at least. So.

**Jared Wolff:** You'd be surprised. Some of these, so some of these antennas that I was looking at, I was evaluating for the NRF 91 feather. Some of them actually are tuned pretty well for all of the bands for cellular, including 2.4 gigahertz. So technically, even including GPS, if you get the right one and it's like, well, like all I have to do is plug in one antenna. This is awesome.

**Chris Gammell:** That's pretty nutty. Yeah. Yeah. You see like the peaks on the S11 chart, or sorry, the dips in the S11 chart. Exactly. That's a lot of dips, you know, like if someone did a lot of simulation on these, and it must be a small, a small antenna for yours, right? Cause the feather form factors is not large.

**Jared Wolff:** So I am using external ones. There's no space for, for a chip, for a chip down in time. That would have been crazy. Yeah. I'm just using an external that gives people the, the flexibility. If they want to use a different antenna completely, maybe they have like a rubber ducky style, or maybe they want to do a UFL to SMA and then hook up that way. As long as it's within the limits of FCC, obviously.

**Chris Gammell:** Yep. Do you have like a recommended one that you're, did you sell one with a kit or did you just kind of say, here's where you might want to get one? Or how did you do that for your, your crowdfunding backers?

**Jared Wolff:** Yeah. So the ones I have for my crowdfunding backers, it's included. So every package comes with a antenna, which is like a flex antenna that has some three M tape, double-sided tape on the back. So you can kind of stick at things if you want. It comes with the NRF 91 feather, it comes with some, some headers you can solder on if you want. And it also comes with a hologram SIM card.

**Chris Gammell:** Yeah, that's great. That's great. So just to go back for a second, I don't know if we've ever talked around the show before. Could you explain the differences between cat M1 and Biot and cat one or the other cats that are out there?

**Jared Wolff:** Man, there's so many cats.

**Chris Gammell:** The bag of cats. Yes.

**Jared Wolff:** So many, just a bag of cats. So cat four, as you go down, so you start like cat four, you, you, your phones, I don't even know what the phones have. Cat five.

**Chris Gammell:** I think they're cat six though. Yeah.

**Jared Wolff:** Cat six. So the higher category, the faster speed you have. So the, the lower you go. So you're going down. So this modem is capable of cat M1 and NBiot. Cat M1 is like the slowest. You can go on a traditional LTE signal. So they're, what they're doing is as you go from the top to the bottom in terms of fast, slow, they're, they're changing the, how much bandwidth are using. So they're squeezing the band, band slower and smaller, smaller, smaller for NBiot. It's kind of a different beast because it's, I believe they use some different modulation techniques, but it's also much more narrow and it's actually even less data you can get through.

**Chris Gammell:** Yeah. I thought they were just using like sidebands for NBiot or something. Something that's very non-traditional is like 200, 200 kilohertz. And it's like just the sideband or something weird in there, but I don't remember what it was specifically.

**Jared Wolff:** Yeah. It's something crazy like that. And usually they need separate equipment. So that's a big difference between cat M1 is that they were able to roll out cat M1 in the U S faster because they, all they had to do is update their existing infrastructure with some firmware updates. Whereas with NBiot actually requires some more capital investment to actually get people to install those things for it to work. So that's where, that's why you don't see a lot of kind of NBiot in the U S is just because it's such a, such a process.

**Chris Gammell:** Yeah. I think the first test site was out in Vegas, just on T-Mobile and it's been spreading, but not as much. And I think it's still just T-Mobile that's doing it. Correct. Over in Europe. It's, I think there's more, like you said, right? There's more in Europe and Asia. They're trying it there because like longer term, it's like so low speed. And I think the costs were really low too. I remember seeing like a, I think Teemo was doing like five or 10 bucks for a whole year of data. And it was like a pretty decent amount. Yeah. So like that's, this is always the restriction with cellular is that, you know, people have to pay for their data when they're used to like, Hey, I have an ESP 32. I can just hook it into wifi. It's like, well, yeah, you don't, you don't get that anymore. Sorry.

**Jared Wolff:** Nope. Not at all. Yeah.

**Chris Gammell:** How about coverage? Have you, have you gotten word? Well, I guess, did your customers check if they have coverage everywhere? Cause I have heard about spottiness and even so the cat M1 stuff and stuff.

**Jared Wolff:** Yeah. I mean, it's been growing. So when I first kind of came out and like, I was working on it in 2016 or 2017, 2018 ish. And it was still kind of new. And when I called them Verizon, people still had no idea what a cat M1 device was. And you had to like get to the special technician to get it.

**Chris Gammell:** You're like sending out the same PowerPoint to every, when you talk to every customer service person you talk to,

**Jared Wolff:** you had to get to the specific person that knew what to do. So you, your, your SIM could get activated. It was that bad.

**Chris Gammell:** Oh wow.

**Jared Wolff:** And I was talking to the, the Verizon guy, the kind of FAE. And he was like, Oh, it's been great. It's been like this for a while. I'm like, I don't think so, dude. Like that's not my experience.

**Chris Gammell:** Right. Right. Well, probably because he was probably hearing it internally. Like, yeah, it's coming. And it's like, well, you know, if it's, it's a lot different than like when you're talking to like a level one customer service person, it's like, well, they don't get every, you know, it's got to work all the way down the chain to every operating procedure that exists. And it's like, if it doesn't make it that far, then it effectively doesn't exist to, you know, the public. Well, let's yeah. It's I had, I had one customer, I was doing like a remote monitoring project. It was really interesting. It was like, it was a cat on one modem on board and the person deploying the system out in the field. They held up their phone. It was on AT&T. They held up their phone for four bars on AT&T, right? They could see the tower. And then they, nothing would happen on the board that we were working on. And they were trying to deploy. And it was like, so finally they called up AT&T. They're like, Oh, you know what? Actually, we don't run that tower. And it's like, because there's these third party operators that, you know, go under the banner of AT&T, but they don't have, you know, software control of the tower operator. So it was like this tower operator just didn't have the right software on it to do cat on one. And like you said, it is as easy as a switch, but they hadn't flipped the switch yet. They hadn't upgraded their software. So that site was completely down. Like you just couldn't deploy in that area. That. Oh, yeah.

**Jared Wolff:** Yeah. That's the, that's the story of cat on one these days. And I mean, it's a lot better. I've been able to, the, the cool thing with holograms I've been able to use, I've been able to sit in my office and it will seamlessly switch between sprint and AT&T. Without me even thinking about it. So, I mean, if one goes down, then you have the other option or it's just, it gives you options.

**Chris Gammell:** Yeah. Yeah. Yeah. That's great. So you had mentioned on this device, you are doing Zephyr. Can you explain what Zephyr is?

**Jared Wolff:** Zephyr is a real time operating system and our, our toss. And it is a kind of a culmination of a lot of work from the folks at the Linux foundation to create this. It's basically, it's kind of like Linux for embedded. It's very similar. It takes a lot of kind of a lot of configuration similarities from Linux and it brings it to the embedded world. And there's a lot of advantages around using it as an RTOS. Because a lot of, I mean, as I mentioned, there's a lot of work that's been done already. You can load up things that's been pre-coded by people. It's just a giant repository of anything you can think of.

**Chris Gammell:** Yeah. Yeah. When you download the package, it's like, now downloading every SDK from ST. Now downloading all the Nordic SDKs. It's like, holy shit, this is like 20 gigabytes of stuff that is downloading just to, you know, because it just wants to have everything there. And it's, yeah, it's not small. It definitely killed my last hard drive. It was like full after that.

**Jared Wolff:** Yeah. So that one of the things about Nordic SDKs is basically the Zephyr SDK, but they tune it and they remove items that there's not applicable. So they'll remove all the, the microchip and the ST and everything. Oh, they will prune it out. So it's much smaller. It's not that big of a deal compared to if you were to just do, use, they have a program called West that you use, do all the management with.

**Chris Gammell:** Uh-huh.

**Jared Wolff:** And, uh, it's, it's a little bit better.

**Chris Gammell:** Yeah. So, I mean, did you have a lot of Linux experience previous to this? Not at all. Or was it kind of a learning curve?

**Jared Wolff:** It was, I mean, I've, I've been using Linux since I was a kid somehow or one or another. I had like, I had a game server in my house running at 130, 133 megahertz.

**Chris Gammell:** Yeah. Turbo button.

**Jared Wolff:** I don't know how I did it. I had like eight slots in there. It was like a counter-strike server. Then that's where I kind of cut my teeth on Linux. I was like, Oh, this is kind of cool.

**Chris Gammell:** Yeah.

**Jared Wolff:** And then somebody was able to like kind of hack into it. I don't even know how they did it. Okay. Some, uh, some thing with the counter-strike server. They were able to get backdoor access.

**Chris Gammell:** Well, but so do you think people that are coming into the, using Zephyr, would that be tough for them if they're not Linux savvy?

**Jared Wolff:** If they're used to Linux development, they might be able to take to it like fish like water. For, for other people, I kind of alluded to this. And when I originally started posting about it, it's like, if you're coming from maybe Nordic traditional SDK and you're going to Zephyr, it's going to be a bit of a change. There's a different process flow. There's different tools. For instance, we, as you mentioned, like you need to download like a bunch of repositories. Well, they have West, but the tool called West for that. And that, and West basically, it's kind of like if you use get sub modules, but not really. So you have this kind of definition file that basically says, here are all the repos that I want. And here are all the checksum or the hashes for those repos from that commit. I want. And then it'll go and fetch them all and kind of a, it'll do a shallow clone versus doing like a full clone of a repo. Or I think it goes down a few steps deeper, but it's not like a full clone of every single repo. That'd be crazy.

**Chris Gammell:** Yeah. Yeah. That's good. So it's just the stuff that it, you know, the header files, whatever it needs in, and everything else is kind of left to the, to the user. If they want to go get everything else or what?

**Jared Wolff:** The, it'll do, it'll get everything for you. And it'll get all those, like all the source files that are within those repositories, repositories that you've, you've called out. If you want to tune it and you only want to include certain pieces of code in your, in your project, that's where you would go in there. They have a, a project file. So for people who have used Nordics SDK previously, they had a SDK config.h. Well, this project file is very similar to that concept where you're enabling or disabling certain parts of the, of libraries or that's where everything gets turned on and off. And that's where you're either compiling it or not. Now in terms of not downloading more code, I don't think there's any way to do it other than removing the line for the Git repository from your project configuration.

**Chris Gammell:** You got it. And at that point you're, you're messing around with stuff that's already pre-configured. Usually it's like you're starting from a pre-configured thing. Anyways, I'm guessing if you're using the Nordic platform, or if you're using like an ST thing, that's already ready for it, you just use that dev board to start with and then modify for, for your needs.

**Jared Wolff:** Exactly. And you're when we usually like Nordic, they give you, they give you everything. So all you have to do is download it and start using it. And other vendors probably do the same thing, but yeah, if you want to go off the rails a little bit, then you're kind of on your own. And I don't recommend that for, for people who are starting, starting out, but it's definitely doable.

**Chris Gammell:** Okay. Yeah. You have written a post about it that I actually really, so I should say I am, I am based on this, this post and also, and not, and not X or guys were talking about it recently. And then Ian, who's one of the guys on my forum, they were all kind of talking about Zephyr. And I started taking a bigger look at it. I was just going to do, I was going to do free RTOS instead, which I don't know is an option on the 9160, but it definitely is for the NRA 52. And I was looking at it and looking at it and looking at it. I've got a book on free RTOS, which is interesting just for learning RTOS in general, but like it's, it's, it feels like this is kind of a new push in that new direction of like, Zephyr's kind of got a lot of backing. If you pick the right, if you're, if you're within what the vendors are choosing it, like ST and Nordic, then you are in a good spot. If you wanted to bring in like a, you know, like a Renesas part, you might be kind of up a Creek, but you know, you could, you can find some parts that are targeted. Zephyr's targeted for.

**Jared Wolff:** Yeah. There's a huge library of boards that are available and Zephyr. If you, if you go to like Zephyr boards in the, in terms of the file structure, they have like arm and risk and everything. You just click down in the arm and there's just like a list of different boards and like what, but you're exactly right. It really depends on the vendor. If they've supported Zephyr. And I know Nordic has had support for Zephyr for one, like unofficial support for Zephyr for a long time.

**Chris Gammell:** Yep. Yep. Huh? Okay. So then you've, you've, so you've written this post, the how to build drivers for Zephyr. And that does seem like it's kind of the hard thing. Cause now you have an RTOS, which are real time operating system. It's kind of like doing all the timing and all the task switching and all that other stuff. But now much like Linux, you need to like write a driver. So what does that look like for people that are interested in doing that sort of thing? Specifically me, I'm really worried about me, me here, Jared, you know, you can do it.

**Jared Wolff:** Number one, it's not that big of a deal. And it's too, you can go to whatever level you want to. For instance, you can kind of implement your driver code within your app. If you really want to, that's kind of like the more traditional way. At least I've done it in the past, but Zephyr has a bunch of pre-determined kind of structures for different type of drivers. So the article that I wrote was based around a real time clock chip that I have on Anerf91 Feather. And they don't exactly have an API that matches it a hundred percent, but they did have a, I believe it was a timer API. So I went through and I kind of searched around. This is all like, once I got comfortable with the SDK, I was like, all right, well, I got to figure it out. I'm going to do this. So I started searching through the SDK and I was like, all right, if I have to use this structure, like how do I initialize it? And what they do is they, you create this structure as a driver and that driver, all the functions get pushed into a struct, like a struct constructors, like what's your init function? What's your write time function? What's your clear time function? And then what you do is you then access all those calls by using their, which I'm still trying to figure out a hundred percent, but they have a whole, I think it's a Linux idea of this device tree. So you look up a device by its name or by whatever you configure it as, and you pull it in and then it becomes a kind of this generic device. And then you can call certain calls from that device. And that's what happens. It's like your driver, that struct kind of gets turned into something you can access through a device in your, in your main code. And then you can swap out. Like for instance, if I wanted to use a different RTC, I don't have to go through and recode everything. I can go to the data sheet and I can create another driver using that same kind of structure. And then I can just start using with my code and just, and then it's just a, a defined in my project file.

**Chris Gammell:** Yeah. Yeah. That's, I mean, that's the magic of Linux, right? That's how Linux and I mean, Windows as well, right? Like these higher level operating systems, they, they know that they need a certain function and that is there, but then they don't really care what the hardware is underneath, which is pretty great. If, if,

**Chris Gammell:** when it all works out. So,

**Jared Wolff:** yeah. And that's the, that's the hard part.

**Chris Gammell:** That's the, that's the rub. Yeah. That's the rub.

**Jared Wolff:** It's like, Hey, I mean, there's an API here, but we don't know what's going on underneath. So,

**Chris Gammell:** so sometimes are you writing like the translation layer between what the API is from the vendor or are you like to translate between that vendor supplied API and the Zephyr stuff or what is the hard part?

**Jared Wolff:** The, well, the hard part was trying to figure out what, what API I can use. Like I was looking through, I'm like, what looks the most, I had to have the search by text. So I'm like timer, like a real time clock, like going through. And then I found the, that timer one, the one I'm using right now. I'm like, all right, this looks like it has, I would look at their API. So I'd look at the struct and see what calls they had. And if it was something that was match up, at least I can get functionality out of the chip. That's where I would, that's where I would go. So that layer, that layer that I'd write, it would include every time, everything from like ice for C initialization, actually kind of sending commands back and forth. And then that is all abstracted from your app. So you can just kind of use the, the API and just, you know, set a timer. You can read the timer. You can clear it. So on and so forth.

**Chris Gammell:** Yeah. Okay. So were you, did you have to write the, the all the way down to the bottom, like driver as well? Like, so you were writing like register manipulation code kind of stuff, or like how low did you have to go for this?

**Jared Wolff:** Yeah, I was, I was at the low level. So I was reading the data sheet. I was going, okay, what register do I need to change to get this thing to start a timer?

**Chris Gammell:** Got it. Okay. So you were handed, you were handed like the thing of like init, right? So it's a very simple example of like, all right, I want to edit a real time device of some type. And then, you know, during an init, then you'll go look at the data sheet. You're like, all right, I have to set, you know, the daytime, whatever, whatever the different registers are. And then that encapsulates the behavior that the init function is asking for. Is that right?

**Jared Wolff:** Yeah. And it really depends on the chip. So I don't think I have to do too crazy of a procedure, but yeah, for some other chips, maybe you have a more complicated accelerometer gyro where you have to do a bunch of setup. Then that, yeah, that's, that's where you would do it. And then as you use the device, then you can make these API calls, which go down to the low layer. And then that's where all the magic happens in terms of, you know, stuff going over I square C or spy or you, you are.

**Chris Gammell:** So how, how are you testing this? So you're writing this code for the low level RTC. How are you testing it? Is it like a standalone test for just the code that you write? Or how do you actually go and step through all that to make sure it's, it's correct?

**Jared Wolff:** I think there are better ways of testing it, but right now I'm just doing functionality testing. So it's not that crazy of a driver. It's just like, it's a, it's timer, like an external timer. So I'm just making sure that it's working and I can change it and set it to different, different, uh, timer intervals and it'll actually interrupt when I need it to.

**Chris Gammell:** Okay. So you're writing the full app and then using that with like breakpoints or whatever, like you're just debugging the full app and that works. Okay.

**Jared Wolff:** Yeah. And that, yeah, that's basically what I've been doing. I've, I've played a little bit with doing the debugging as effort is a little bit different from what I'm used to in the Nordic SDK. And that's also very possible. I think it gets more complicated when you have a, a bootloader, they decided to use MCU boot, which is good and bad because I didn't realize that I had issues debugging and I, I removed the bootloader. I'm like, Oh, it's working all of a sudden. And so for anybody who's trying to debug guns off or if they have MCU boot initialized, they might have to do some extra funny business to get it to work.

**Chris Gammell:** Okay. That's good to know. Well, that's great. I mean, this is a, I really do appreciate that you wrote this, uh, this document on men fault. I think it's going to be helpful for me. So I appreciate that. Thanks a lot.

**Jared Wolff:** You're welcome.

**Chris Gammell:** Uh, let's talk a little bit about the other board that you, uh, built as well. So you are in the feather form factor ecosystem. It seems like, uh, I saw you were also using some of the particle stuff, the Xenon and, uh, but then you made a sensor board.

**Jared Wolff:** Correct. Yeah. So the sensor board is called the air quality one, and it's based on a few different sensors that I wanted to kind of put together for testing air quality. I was kind of concerned at the time with the air quality in my, I was at the time at my brother's house. We were renting a room from him and he has baseboard heating. So whenever the baseboard heat would turn on, I'm like, I wonder how bad the air gets when this happens.

**Chris Gammell:** Yeah.

**Jared Wolff:** So between the, so I had a TVOC. It's a kind of a total organic volatile chemical compounds. And then also for every humidity temperature. And also I had a particular sense particular sensor made by Honeywell, all connected to this one board. And then I would hook it up to at the time, the Xenon, and I would use that to broadcast it up to the cloud and then into an influx DB database. And I had a graph on a front end where I could see where all the, all the variables were at the time. I could look back and see what the history was. So what I found out was you, there's a lot of particles when you're cooking. And when you're heating up your house with a baseboard heat, there's a lot of dust that gets thrown into the air, a lot of particulates. Those are the two big things that I've noticed so far using this device. And I've had mine on the wall, just like running and I actually hooked up a little piezo to it. So whenever it goes over a certain level, it starts beeping. So, and then you walk over to the, to the, the air filter, the air purifier. And I just like turn it on max until it goes down again. Yeah.

**Chris Gammell:** I've got to hook that thing in the network next, you know, you get to get that thing to talk, talk to the network and turn itself on. Right.

**Jared Wolff:** Yeah. I mean, that's a, that's my next project. But once I, that's, I have a lot to do before then.

**Chris Gammell:** Yeah. Yeah. It sounds like, I mean, this is, I mean, I'm sure that a lot of people out, our friends out on the West coast are probably feeling this more than most with all the wildfires that are happening. I just keep seeing posts about, you know, particulate counts are really up out there. Not, not that you would probably need a sensor when they're that high, but it's still, right. Yeah. It's a good thing to be thinking about. I think the VOC sensors, I use those on a project as well. And it was like, I heard that they got really popular because of, Hurricane Katrina, apparently that's like what drove a lot of the, the VOC center, you know, boom that's happening right now, because there's like some kind of like legislation that happened when they brought in these trailers that had like a bunch of formaldehyde in the, in the walls or something like that. Some VOC volatile, like organic comic found. And it was like, that's what drove a lot of the sensors. And that's why it's easier to get them than it used to be.

**Jared Wolff:** I found that I've gotten the most insight from the particular particular sensor where it's actually shooting a laser and counting the particles. Yeah. But the, the T-box sensor does kind of align with those results though, which is kind of cool to see. Like it'll, it's a little bit slower, but it follows the results. So as, as things go up in the room, it usually kind of follows a lot of right along, which is pretty neat.

**Chris Gammell:** Yeah. Yeah. It is, it's interesting to kind of like pull trends out of a, you know, like once you do graph it, it's like, it's very visible and visceral at that point. You're like, Oh, okay. It was real bad that day. That's why I felt like crap or whatever it was, you know? Right.

**Jared Wolff:** Exactly. It's like, why are my eyes itching? And then you go and look at the graph. It's like, Oh, all right. I got to turn on the air filter.

**Chris Gammell:** Yeah. So let's talk, let's just swing back to the NRF 9160 there. Any other lessons learned before we, we get finished here? I mean, what else, what else have you been learning as you've been crowdfunding this thing and getting it out of the world?

**Jared Wolff:** Oh man. Any other lessons learned?

**Chris Gammell:** I should say that you've, you've been posting really great updates throughout. I've been following that. Uh, just seeing all the, uh, the different things you've been going through, but like, yeah. Are there any like unexpected things given your, your hardware experience?

**Jared Wolff:** The biggest thing is it takes a long time, like by yourself. I've been working on this thing for months now. And I'm at the end of the tunnel. It's just this compliance stuff and then getting the boards. Built. Oh, that's kind of the biggest things. And then after that, it's like making sure the software is good enough to make sure everybody's happy or when they're using these things, uh, that's a whole other can of worms too.

**Chris Gammell:** yeah. Yeah. The first half takes 90%. The second half, it takes 90% of your time. Whatever that saying is.

**Jared Wolff:** That sounds about right. Yeah.

**Chris Gammell:** Or maybe it was the first 90% takes 90% of your time. The second, the last 10% takes 90% of your time or something like that. But yeah, it's a, yeah, it can definitely be like a, uh, you know, and then you have all the customer support stuff you're gonna have to deal with as well. Cause you've sold like a couple hundred of these things, right?

**Jared Wolff:** Yeah. There's a, there's a lot of boards going on in the world and about half of them are going outside of the U S and half of them are in. So, so the shipping out of the U S thing is going to be interesting. Hopefully nothing gets lost. I've had some stuff get lost before, so it won't be a surprise if something does.

**Chris Gammell:** Oh boy. Yeah. Yeah. I mean, all right. So 9160 can work overseas as well.

**Jared Wolff:** Yeah. So for it's, it's nearly a global module. So Nordic, that's what Nordic has been working on these past years when we were like, okay, they have the module. Cool. You can't use it. Well, what they've been doing over the past year, and if you go to their website, you can go check out their compatibility matrix for the different bands in different countries. You can also, they also post, uh, I believe it's on their compliant. If you search for Nordic semiconductor and NRF, NRF 9160 compliance, we should bring you to that page where they have all the cellular providers that they are certified or they work with. And also the compliance in terms of countries where the modem, the module is certified to work on particular bands in those countries. Um, so if you're in a country and you want to use NRF 91, I would definitely check that out just to make sure that it works with a provider you have. And also that, uh, and if it works with a provider and most likely is obviously certified, uh, in terms of compliance.

**Chris Gammell:** Yeah. One thing that's good too, is if you haven't ever done it, uh, listeners, not you, I'm sure you've done this, Jared, but if you go to opensignal.com slash networks, you could see coverage for all the different, uh, carriers within your country. And that's, you know, some approximation of the coverage map as well. So that could be a helpful, helpful resource to make sure you're not buying something you can't use. Uh, just to cross reference that, you know.

**Jared Wolff:** Yeah. If you, uh, especially for Canon one, that, that usually kind of aligns with cellular, anything. If you have a cell signal, most likely you're going to have them one might not be the same for MB IOT. So that's a, something to remember too.

**Chris Gammell:** Yeah. Yeah. That's a good point. Well, great. Well, Jared, thanks for joining us here. You said, uh, you might have a coupon code for people that are, uh, or a link to, for the remaining boards. Is that right? A place to buy. Yeah.

**Jared Wolff:** So there are some NRF 9160 is going to be available very soon. Uh, if you want to go to jerrywolf.com forward slash amp out, uh, you can sign up and you'll get a 10% off coupon. If you want to, uh, purchase the NRF 9160 further. And that should be within the next couple of weeks or so. I, I have some boards here right now, which is very exciting. So it'll be shipping out to backers and then it'll be available for sale shortly after that.

**Chris Gammell:** Great. Great. Well, good luck on all that. I'm excited to see this stuff and I appreciate, like I said, I appreciate you sharing what you're doing and showing it, you know, showing your progress on your blog and elsewhere. It's been really useful.

**Jared Wolff:** Thanks, Chris.

**Chris Gammell:** All right. Talk to you soon.

**Jared Wolff:** All right. Later.

**Jared Wolff:** Later.

**Speaker ?:** Later. Later. Later. administered in administered administered in
