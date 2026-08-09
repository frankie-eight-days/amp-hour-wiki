---
episode: 161
title: Interview with Michael Ossmann - Gifted Grimgribber Grokker
url: https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/
---

**Chris Gammell:** Hey guys, real quick before we start the show, I know this is kind of non-standard to have announcements before the show even starts. Sometimes there's advertisements here, but I thought I'd throw it in here just because. First off, if you're going to the Open Source Hardware Summit, we are having a meetup. It's still in the works as of Tuesday night, which is kind of pushing it, but it will be Thursday night, 7.30 p.m. at a Boston location. Keep your eyes on the AmpHour.com and Twitter feed in order to find out where that is. We'll also be doing a tour at Bolt, the hardware accelerator, at 5 p.m. The other thing is Michael, who we're about to hear from here, has a Kickstarter. If you're listening to this and you're thinking, oh, I'm going to listen to little bits at a time, his Kickstarter ends in a few hours from the publishing date of this, the morning of September 4th in Eastern Time Zone. So if you're interested, skip ahead, read some of the links, and check out his Kickstarter so you don't miss it. If not, you can probably purchase it once the Kickstarter is over, but it'll be a little while. That's all. Enjoy the show. This is the AmpHour Podcast. Recorded September 2nd, 2013. Episode 161. With guest Michael Osman. Gifted. Grimgribber. Grocker.

**Dave Jones:** Welcome to the AmpHour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Michael Osman:** And I'm Michael Osman of Great Scott Gadgets.

**Dave Jones:** Great Scott! What a brilliant name.

**Michael Osman:** It is a great name.

**Dave Jones:** Trademarked, I see.

**Chris Gammell:** Yeah? How'd you do that one? Was that...

**Michael Osman:** Well, I don't know. I just claimed it as a trademark. I did a search to make sure nobody was using Great Scott for anything, or at least Great Scott Gadgets.

**Dave Jones:** Well, yeah, I don't think you'd be able to get Great Scott, maybe.

**Michael Osman:** No, it's too common a phrase. Yep. Right.

**Chris Gammell:** All right. That's a good one, though. I'm jealous. Dave's going to have to pun it up later. He'll be thinking of other ones.

**Dave Jones:** Because I'm a huge fan of Back to the Future, as a lot of people are. Oh, yeah.

**Michael Osman:** Of course. That's what I always have to remind people of if they ask me about it. Like, people who are native English speak the name. Like, Great Scott Gadgets. That's a cool name. And then when I talk to somebody who's a speaker, they always say, who's Scott? Because they don't know the expression like we do. Even if they speak excellent English, they'll say, who's Scott? And then I always have to remind them, well, do you remember Doc and Back to the Future, how he says, great, Scott. And they say, oh, right, okay. But they still don't get it.

**Dave Jones:** Somebody actually went through and added up the number of times he said great, Scott, in the entire series. I think it was like 38 times or something. Oh. There was this webpage. You know, some nerd went through and counted them all, as you do.

**Chris Gammell:** Well, 50th time through. I mean, what else do you have to do, really?

**Dave Jones:** Well, yeah, exactly. Speaking of which, I'm probably going to build up my Lego Back to the Future after this. I'm going to shoot a time-lapse video of me building my Lego.

**Chris Gammell:** Very nice, Dave. Perhaps we should ask Michael about his background and stuff, though, too, right? Yeah, let's get it. I don't know. I want to hear more about the Lego Back to the Future. Well, I kind of do, too. All right, we're changing the show format. All Lego, all the time. So, Michael, tell us your background, though. I mean, where do you come from? What have you worked on in the past?

**Michael Osman:** So, I'm one of these people who came to electronics by way of software. That's one of them, Dave. Yeah.

**Chris Gammell:** I know. No, that's good.

**Dave Jones:** They're everywhere. They're everywhere. They're my new favorite.

**Chris Gammell:** That's my new favorite type of person, too, for contextual electronics.

**Dave Jones:** It isn't like when zombies attack, it's when software people attack. It is. Well, what kind of software, though?

**Chris Gammell:** Are we talking like JavaScript? Are we talking like C++?

**Michael Osman:** Oh, all kinds of stuff. All kinds of stuff. I mean, if you asked me when I was eight or nine years old what I wanted to be when I grew up, I probably would have said an electrical engineer or an inventor. And then I just totally lost sight of that for many years. I used to put together electronics kits when I was a kid, but I never got very far. I could tell you how a resistor worked, but I couldn't tell you how a transistor worked. So then I didn't pick up a soldering iron for like 20 years or more. Ouch. Because I just got interested in music and computers and eventually got into IT stuff and kind of worked for a long time as a system administrator and network administrator and did a lot of little software development projects along the way. And gradually did more and more security work, eventually became an information security consultant. And through my work in information security, I got into wireless communication security. And through that, I ended up doing just some kind of pure research in wireless communication security that led me to software-defined radio because software-defined radio is kind of the ultimate tool for hacking on all things wireless. And then from there, I got into electronics to kind of try to build my own devices for wireless security research and development. So really, I mean, that was just in the last few years. Four years ago, I had never done any surface mount soldering. I'd never programmed a microcontroller. I'd never designed any kind of a circuit board. It's all new to me.

**Chris Gammell:** You're making us look bad here, you know? Yeah, exactly. Crap. That's awesome. I mean, that's really cool. So when you say like wireless security type stuff, is that actual like people tapping into lines and trying to see when other people are tapping in? Is that the idea? Because as much as... Partly, yeah.

**Michael Osman:** Interception, eavesdropping on communications or interfering with communications, inserting your own messages, and like spoofing legitimate communication, all of those kinds of things. And a lot of people are familiar to some extent with Wi-Fi security and how bad Wi-Fi security used to be and how much better, how much it has improved over the years. But there are a lot of wireless communication systems in the world, and none of them have gone through as much positive change for security as 802.11 has. So there's a huge... It's an amazingly diverse field of different wireless communication systems and the security elements that they have or that they lack. And it's a fun field to be in because sometimes you find things that are very sophisticated, and sometimes you find things that are just completely broken and wide open. And easy to break. So you get a little of both. You get some stuff that's fun and easy to break, and then you get some stuff that's a real challenge.

**Dave Jones:** I'm using, I think, WEP2, is it?

**Michael Osman:** Probably WPA2.

**Dave Jones:** WPA2, yeah. WPA2, is that should I be concerned?

**Michael Osman:** Well, it's a huge upgrade over WEP, which was the mechanism for securing Wi-Fi in the early days and was completely broken.

**Chris Gammell:** Yeah, like the why even bother kind of security.

**Dave Jones:** Right, so I'm generally okay, but the NSA can still tap in.

**Michael Osman:** Well, once it gets onto the wires, they probably can. But today, I think probably the worst vulnerability for 802.11 systems, if you're using WPA2, probably the worst vulnerability is that there are some weaknesses in the way that a lot of Wi-Fi equipment sets up an initial key for you. So if you use the built-in feature for it to generate a seemingly strong passphrase, it may not be as strong as it appears. Right. But as long as you set up WPA2 and you choose your own passphrase and you make it a good one, then it's pretty solid.

**Dave Jones:** Right. Is there anything better than that or do you have to buy some sort of commercial, high-end commercial product to get better security than WPA2?

**Michael Osman:** So most of the high-end commercial products actually have far worse security than WPA2. Oh, right. And I think it's mostly a function of the lack of peer review on a lot of the commercial products, the more proprietary products, that is. The open standards and the more popular open standards, and especially Wi-Fi, get a lot more scrutiny.

**Chris Gammell:** So it has the one thing that makes me sound sort of what I know like I'm talking about in software, security by obscurity. I really don't know what I'm talking about, but that's the only thing.

**Michael Osman:** Yeah, security by obscurity is the norm in the wireless business. Oh, okay.

**Dave Jones:** Does it matter, though? Like if somebody hacks your Wi-Fi, they're just going to steal your bandwidth. It's not like they're going to steal your credit card info and all that sort of stuff, right? What's the...

**Michael Osman:** Well, they could steal your credit card info.

**Dave Jones:** Okay.

**Michael Osman:** You know, and they could, as somebody who's on your Wi-Fi, is very likely able to gain access to every computer on your network and maintain that access even after they're not in range of your Wi-Fi.

**Chris Gammell:** Oh, fancy.

**Dave Jones:** Right. Of course, they can install some backdoor thing, right, that allows them to access your machine from anywhere. Yep. But really, you need someone with intent to do that. Most probably, most intrusions are probably going to come from people who just want to suck your Wi-Fi bandwidth for an hour or something, right?

**Michael Osman:** Most, yeah, but it only takes one. Yeah, exactly. And you're owned forever.

**Dave Jones:** But once your computer's hooked onto the internet, you're screwed anyway, right? Right. Wi-Fi is probably the least of your problems, right?

**Chris Gammell:** How much of your past experience was actually like, were you like securing other systems or were you mostly just doing a lot of analysis? And trying to break stuff for people?

**Michael Osman:** Some of both. Actually, the area where I did the most work initially in my career in information security was in healthcare. And I did a lot of security assessments for different healthcare organizations around the U.S. This was in the early days of HIPAA. And HIPAA? HIPAA is a regulation of a rather significant piece of legislation in the United States that governs a whole bunch of aspects of how healthcare providers and insurers do a lot of different things. Right. And the part of it that's relevant to security is that HIPAA kind of increased the potential for sharing of patient information between different healthcare entities. And so as a part of that, to kind of cover people's fears about patient privacy, they said, well, we're making it easier for them to share information about people. So we're also going to establish these rules about when it's appropriate to share information and how they need to protect information. So HIPAA included a privacy rule and a security rule that introduced a whole bunch of red tape for healthcare organizations. And it kind of forced them to start developing information security programs to protect the patient information that they had. So I was doing a lot of consulting for hospitals and other healthcare providers in the early days of the HIPAA security rule enforcement and kind of helping them figure out where their weak spots were and figure out how to shore up their networks and their procedures. And eventually I found my way into a position as an information security officer for a hospital system. And from there just kind of fell into a role as a wireless communication security researcher for the Department of Commerce. That seems like a big jump.

**Michael Osman:** It was a big jump. I think I was very interested in Wi-Fi security and I had published an article or two, not any real fundamental research of my own, but just kind of raising awareness of Wi-Fi security matters. And somebody just kind of called me up out of the blue and said, hey, we have this research lab in Boulder and we have a whole bunch of people who are like RF engineers studying communication systems. And we want to look at security of communication systems. And none of our engineers know anything about security. So we just wanted kind of an information security generalist who knew something about wireless. And so I started there. And it was an amazing environment. I mean, because I was suddenly doing just pure research, which I love. And I was surrounded by all these amazing smart people. They were all electronics engineers and RF experts. And I was like the one security guy, the one Linux guy. Oh, yeah. The one, maybe not the only software guy, but my software skills were a lot more advanced than most of the engineers.

**Chris Gammell:** So you were the one-eyed man in the land of the blind, huh? Yeah, exactly.

**Michael Osman:** And so it was a real symbiotic relationship for a long time where people would come to me with interesting problems that I knew how to solve. And I was surrounded by all these other people who could help me solve problems that I'd never kind of tried to tackle before. So it became very easy for me to – that's one of the reasons that I was able to kind of learn electronics very rapidly because I had, you know, half a dozen PhDs just up and down my hallway that I could chat with at any time. That's awesome. That's like boot camp almost. A lot of – oh, yeah. There were a lot of conversations, a lot of circuit diagrams on whiteboards and napkins over lunch. It was great. Wow. Cool.

**Dave Jones:** So they had seen your articles. They'd seen your publications and just called you out of the blue. Right.

**Michael Osman:** Yeah.

**Dave Jones:** That's another example of – we keep saying this all the time that, you know, publish stuff.

**Michael Osman:** Oh, absolutely.

**Dave Jones:** Either on your own – you know, it used to be back in the old days, you know, you publish it in the journals. But these days, it can just be on your own website or blog. Right. Or whatever, YouTube. Right.

**Michael Osman:** I mean, I didn't have anything.

**Dave Jones:** And then people will eventually come to you. If you've got the skills, people will find you.

**Michael Osman:** Absolutely. I didn't have anything other than just some stuff on the web.

**Dave Jones:** There you go.

**Michael Osman:** Well, that's awesome.

**Dave Jones:** Works every time. I'm telling you, folks.

**Chris Gammell:** So how did you actually start diving down into the hardware side then? Once, you know, you had these great mentors and guys to bounce ideas off of, what would you start diving down with?

**Michael Osman:** Well, it was kind of two things. I mean, one was that I was surrounded by these people at work. But the other was that I was getting more active in the information security community and going to more conferences and meeting people who were involved in hardware hacking and just kind of getting inspired that way. And ultimately, I started doing some work. I was investigating a number of different communication systems, especially public safety radio systems at work. But I was having so much fun with software-defined radio doing that kind of stuff that I started picking up projects on the side. And one significant one was that I just sort of became obsessed with Bluetooth and Bluetooth monitoring in particular because there just weren't any tools available for Bluetooth monitoring. So I started looking into using software-defined radio for Bluetooth monitoring. And I found this recent paper that had been written on the subject. And I said, hey, this kind of is a good start for what I wanted to do. But I had some ideas that went a little further. So, you know, I ended up contacting Dominic Spill, who was one of the authors of that paper and who had published some code from that project. And I started taking his code and updating it and adding some new features to try to implement more complete Bluetooth monitoring capability using software-defined radio. And we started collaborating. And within a matter of a few months, we had a presentation at a conference together, which was the first time I met him in person. And we... Well, me and Dave still haven't met yet, so... Yeah. Yeah, exactly. Really. Like, that's pretty funny. So, yeah.

**Dave Jones:** Small, small problem of, you know... 14,000 miles. 20,000 kilos.

**Chris Gammell:** Right. Yeah.

**Michael Osman:** I think when I first started trying to contact Dominic, he didn't answer my emails for all because he was driving from London to Mongolia. For what? Finally, he was back in London and we started collaborating. Yeah. Yeah. And so, that project ended up... We ended up implementing some really cool stuff and kind of showing people, hey, it's possible to discover Bluetooth devices that are non-discoverable, for example. You know, everybody thinks if you turn your Bluetooth device into non-discoverable mode that other people can't monitor its transmissions or find it. But we showed that that's absolutely not true. And we showed how to, you know, how to use the tool of software-defined radio to just monitor arbitrary Bluetooth packets over the air and actually, like, derive enough information just by monitoring one channel to figure out what the frequency hopping scheme is or the actual hopping sequence and be able to follow along with it and all that kind of stuff. But ultimately, nobody really took our work and very few people actually reproduced what we did. One of the reasons, I think, is that the platform we were using was fairly expensive and we were like, hey, you know, buy this $2,000 piece of equipment and then take a soldering iron to it so that our hack works. And then you can do this stuff. And not many people want to do that. So I started the UberTooth project in response to that as a way to, I mean, we had this relatively conceptually simple way to monitor Bluetooth on communications on one channel. And I thought, well, it can't be that hard to take a more traditional lower cost approach as opposed to the software-defined radio approach. It can't be that hard to make a device that just monitors one channel and, like, spits out the bits over a USB interface to a computer. And that one project, the UberTooth project, just, that is what really motivated me to dive into electronics headfirst and try to build this thing. And it was a, you know, ridiculously complicated project for somebody who, you know, like, I barely knew what OMS law was, you know. I wasn't going to say anything. And, but I, you know, I had the benefit of being surrounded by all these engineers. I had the benefit of getting to know hardware hackers at these security conferences. I was inspired by, like, electronic badges made by people like Joe Grand and Travis Goodspeed and Amanda Wozniak and a whole bunch of people in the information security community who kind of encouraged me. And I also had the benefit, you know, we're really in this golden age for people who want to get into electronics. Like, I started out looking at SparkFun and going through the SparkFun, I think it's called the beginning embedded electronics tutorials. So, like, I knew I was going to have some kind of a microcontroller. So, I just looked for how do I get started with microcontroller. And I found this tutorial and I bought an at Tiny and put it on a breadboard and got it to blink an LED, you know. And, yeah, I mean, that's such a huge step. It's all downhill from there, guys. But it was amazing that I had this resource available to me online to, you know, walk me through that stuff. And I was able to just kind of ramp up and take on. I knew that I wanted to build a Bluetooth sniffer, but I knew that I wouldn't be able to do it right out of the gate. So, I just sort of set out to find projects that would help me learn along the way. And somehow it all worked.

**Chris Gammell:** It sounds like that your research background kind of helps there, too. Because, I mean, researchers are always starting from scratch with that kind of stuff. You know, like, it's always, well, we don't know what we're doing yet, but we'll figure it out eventually. Because that's the whole point, right? I mean, you're going into discoverable territory. So, it's nice to have markers along the way from SparkFun and everybody else.

**Michael Osman:** Yeah, yeah. And being able to do both software-defined radio and doing hardware were just very empowering to me. Because, like, I came from a software background. And I would look at it. But I had a pretty good knowledge of communication protocols, like internet communication protocols. And kind of how to look at a protocol and kind of guess at where the weaknesses might be and figure out what to probe. And so, I would look at a specification for a wireless communication system. And I would flip through, you know, the hundreds of pages. And it's very boring work to analyze these things. But I would go through them. And I would point at something on, you know, page 157 and say, hey, this message that's transmitted, this should be authenticated. And it's not. And that's a vulnerability. And people would look at me and they would say, okay, that's great, kid. No one's ever going to do that. And surely it's, you know, it's too difficult for anyone. Like the radios, the off-the-shelf radios don't actually support doing the kind of attack that you're proposing. And it's just not practical. And being able to build my own radios, either with software or hardware, gave me the ability to actually take theoretical vulnerabilities and turn them into practical vulnerabilities and demonstrate them to people. And say, like, here's what happens when I send this unauthenticated control message and your radio dies, you know.

**Chris Gammell:** It sounds like this, if someone would have cut into this story like two minutes ago, they would have been debating between someone getting into technology and someone becoming a supervillain. And they dared me not to do it, but I did it anyways, you know, that kind of thing. I'll show you all. So, jury's still out on you, Michael, I got to say. We'll see. We'll see within the episode if you're a supervillain or not.

**Michael Osman:** I'm a big believer in using superpowers for good. Yeah. Okay.

**Chris Gammell:** Well, you can say that.

**Dave Jones:** So, how long in the end did it take you to develop the Ubertooth 1?

**Michael Osman:** Yeah, Ubertooth 1. Well, I started out with Ubertooth 0. Right. And I think, you know, that stage took me maybe a year and a half. But it really, like, I didn't know what it was going to look like at first. At first, I thought it was going to be – actually, I was thinking it would be a software-defined radio kind of architecture because that's what my background was. I knew basically how SDR equipment should work. And I thought, well, maybe if I could kind of rip the guts out of some kind of 2.4 gigahertz device, like the RF front end out of that, and then rip the back end out of something else, like a TV tuner, for example, and kind of make a Frankenstein device. It could be low cost and easy to assemble, and it would allow people to do this basic Bluetooth monitoring. And over time, it sort of became apparent that I was going to be better off kind of designing the circuit from the ground up, which was terrifying. But, you know, I found these other projects to get me started along the way, and I just kept going with them. And I had great mentors like the folks at the Boulder Labs and Jared Boone of ShareBrain Technologies. He's an open source hardware developer that I met at a hacker camp. And, you know, he's really – we're continuing to do a lot of projects together. And I had just a lot of people to help me along the way, and eventually I made UberTooth Zero, which was just a USB microcontroller and an RF chip, you know, a wireless transceiver IC, and an antenna, basically. And I designed it in Eagle and had a few made, and it worked. So then I started trying to make UberTooth One at that point because everybody was saying – like all my friends in the hacker community were saying, hey, that's great. When can I buy one? And I was like, really? I don't know about that. But I just decided to try my hand at making something a little more marketable. So I designed UberTooth One, which was a little bit smaller, a little bit cleaner design, had a front-end amplifier chip on it. So it had better RF performance than UberTooth Zero. But otherwise, it was basically functionally equivalent to UberTooth Zero. And threw it up on Kickstarter to see what would happen. And sure enough, enough people wanted it that it actually – you know, not only was it worth manufacturing, but it – within a couple months of delivering my units to Kickstarter backers, I had enough additional sales, post-Kickstarter sales, that I was able to quit my day job.

**Dave Jones:** Fantastic. And it doesn't take a huge amount. I mean, we're into – yeah, you raised $50,000, $53,000 of your $16,000 goal, but it's only 441 backers. And, you know, in today's global economy and global marketplace, like that's not many.

**Michael Osman:** Right, it isn't.

**Dave Jones:** You know, 400 – and it doesn't take many to get – you know, to turn it into a full-time business.

**Michael Osman:** I mean, I announced the availability. I launched the Kickstarter at a conference where I was talking about the project. And I already had somewhat of a reputation within the security community, which is the primary people who would be interested in this thing. So even though I was new to building electronics, I have this niche market that was kind of ready for this and knew me. Yeah, that helps. It helps a lot, I think. Yeah. And that's Great Scott Gadgets was born.

**Dave Jones:** And you've been doing that full-time. Yeah, ever since.

**Michael Osman:** And actually, Great Scott Gadgets was born like a year or two before then because it was a – I just created a fake company website to – As you do, yep. Yeah, as you do. I was just, you know, trying to get some data sheets out of manufacturers and stuff. And so that's – I don't know. I just – I needed a fake company name. And Great Scott Gadgets was the first thing I thought of. So then later on, people were wanting to buy stuff from me. And I'm like, well, yeah, I have this company. And I'll just pretend it was legit all along. Thank you, Tim. I love it. Works every time. Yeah, absolutely. Absolutely.

**Dave Jones:** So how many Ubertooth ones did you end up selling?

**Michael Osman:** I still sell them today. I think I've sold a total of around 5,000.

**Chris Gammell:** Oh, wow.

**Michael Osman:** Over the last two and a half years. That's awesome.

**Chris Gammell:** Jeez, that's a lot. Where are you manufacturing it? How did you get launched into that?

**Michael Osman:** Yeah, so I had – you know, I just asked a friend of mine, like, hey, you've had some conference badges, electronic conference badges made. Who do you have manufactured those? You know, I got a referral. And I just tried these guys out. Eat a net. They're owned by somebody who lives in the Bay Area, but their operations are in Shanghai. And I had great experiences with them. Like, my first ever manufacturing went very smoothly or as smoothly as you could possibly imagine. Of course, there were minor hiccups. But I think I just kind of got – I kind of lucked out with a good referral early on. Yeah. And I've had such good luck with that. I keep using that manufacturer.

**Chris Gammell:** That's great. If you find one that's good, you just – yeah, that is the right thing to do. And that's – I mean, referrals are the right way to go in the first place anyways, I think. Because you basically have other people do the hard work for you of, you know, getting through the crap and just finding the good ones, which is smart. Right. Yeah. Yeah.

**Michael Osman:** I mean, one time I had a rapid project. Like, I was making a badge for a conference. And it was like a ridiculous thing that I put together in like eight weeks, including design and manufacturing. And so it was – you know, I tested two or three units before it hit the factory. And they were coming off the line in the factory and like a good 30 or 40% of them weren't working. Oh, no. And so they just – they stopped the line. And like I think I was in Europe at the time or – and they're in China. And my main contact is in California. So, like, it's just time zone nightmare. And it turned out like by the time I actually got on the phone with people, they had figured out that I – that my load caps on the crystal were suboptimal. And they had fixed the problem and resumed production.

**Dave Jones:** On their own.

**Michael Osman:** And fixed – on their own. They made the money better.

**Dave Jones:** Which is good and bad. And sometimes it's good that they found the problem and fixed it for you. Right. But other times it's bad in that – Yeah. No, you know, you don't want them to make changes. Give me a call next time too.

**Michael Osman:** Right. Exactly. Exactly. Yeah. Exactly. Well, they were trying to get a hold of me. But under the circumstances, it was great because it was a very quick turn project. And there really wasn't time to do anything but that. So, it was definitely – I was kind of sold at that point.

**Chris Gammell:** So, it looks like you – I mean, you've done a couple badges here. I see the two Torcon badges on the Great Scott site. Are you like a conference junkie? Are you always at conferences? It seems like a lot of the – I don't really do many conferences. But I'm always curious about that kind of, you know, like going around to a lot of them.

**Michael Osman:** Yeah, I am. Especially lately. I think I stayed home for four or five months last winter. And then at this time of year, it's just ridiculous. I've been to four different places in the last month. Oh, wow. And yeah. And I'm home like for a week between two trips to Europe right now. It's kind of ridiculous. But the information security community has a huge number of conferences. And they're just great people and really interesting content. And they're my primary market for most of the stuff that I'm doing. And I really – I continue to do projects just, you know, not related directly to my products that are, you know, worth talking about at these kinds of events. Or sometimes they are directly related to my products. And I teach a lot of classes. I do a software-defined radio class that I teach – oh, this year I think I'm teaching it four times. It's a two-day class that I usually do at a conference. And so it's a big part of my life, both professionally and for fun. It's where all my friends are.

**Dave Jones:** We don't have conferences here in Australia, you know, be in the backwater and all.

**Michael Osman:** There is actually at least one information security conference in Melbourne.

**Dave Jones:** Oh, there you go. Have you been to it? I haven't been yet.

**Michael Osman:** I have not been yet. But I hope to eventually.

**Dave Jones:** I think we've lost Chris.

**Chris Gammell:** Oh, no, I'm back. I'm sorry. I'm back.

**Dave Jones:** No, he's back. He's back.

**Chris Gammell:** I'm back. Yeah, sorry. Mute problems.

**Dave Jones:** Someone's hacked in as we're – Yeah.

**Chris Gammell:** My Wi-Fi's been hacked. So, I mean, you mentioned your two-day course there. I mean, so that kind of brings us to the main event here, which is the HackRF, which is the new Kickstarter project, which funds today or funds tomorrow. What is the trigger date? Right.

**Dave Jones:** 38 hours left.

**Michael Osman:** Yeah. I think – right. So, by the time you post this episode, there will be very little time left. Like 10 hours left or so. So, if you're listening – yeah. If you're listening and you happen to be listening really soon after this episode was posted, then I'd love it if you go check out HackRF on Kickstarter and tell all your friends about it. But if not, then sorry for the bad timing. But it will be available in some form after Kickstarter. Okay. That's great.

**Dave Jones:** And by the time our next episode comes out, you'll be – you'll have half a million dollars in the bank.

**Michael Osman:** Yeah. Well, hopefully. We'll see.

**Dave Jones:** That's what it's currently up to. It's up to $529,000. Oh, great.

**Michael Osman:** We'll see how long it takes to like – for my bank to allow – to release the funds. Yeah.

**Chris Gammell:** Well, don't worry. You don't have to build anything until then, right?

**Dave Jones:** Yeah, there might be an issue or two there.

**Michael Osman:** You got how much? Yeah.

**Dave Jones:** And see, once again, it sounds like a lot of money, right? But it's only 1,700 backers.

**Michael Osman:** Right. Right?

**Dave Jones:** Like, I got like 2,300 backers for my little PCB ruler. Right? You know, 1,700 is not a huge number. Well, it is. But, of course, the product itself is what? $275. So you multiply that by –

**Chris Gammell:** But it's really a percentage of the market that I think that matters there. It's the – you know, how many people that want this kind of thing that are actually buying it. I think that is a big chunk because, you know, the SDR is – it's not necessarily new, but it's in terms of like accessibility to the public. There is definitely a lot of interest in it. And I think this is a great entry product into that kind of thing.

**Michael Osman:** Yeah. And that was one of the major motivations of the HackerRF project in the first place was to provide a very general purpose platform at a lower cost that people could use to get started with software-defined radio. I really – you know, I don't see HackerRF being the best tool for any one job, but it's a great tool that can be used for a huge variety of jobs. And I hope that it introduces more people to software-defined radio and kind of broadens the exposure of technology.

**Dave Jones:** I had a whole bunch of people ask me about this HackerRF thing on Twitter and other places, and they said, are you going to get one? Are you – you know? And I think Chris and I talked about it last week, didn't we, Chris? Yeah, we did, yeah. Well, yeah, we – you know, yeah, it looks cool. But then we – then both of us went, oh, you know, it's – well, here in Australia, it's going to be like 300 bucks for me. And it's like 300 bucks, oh, I'm probably – you know, it's – I'm probably never going to really use it, you know. Right. Like it would be a fun toy, you know. I'd love to be able to experiment with this sort of stuff, but it's just another – you know, for someone like me, it's just another, you know, gadget to play around with, really, you know. Right. With the other two dozen gadget boards I've got sitting in a box, you know, so.

**Michael Osman:** Yeah, and it depends a lot on what your potential applications are.

**Chris Gammell:** Yeah, and it was really software that scared me off. I mean, like software – I always talk about software scares me off. But unless there's like – I'm not really into the software side of things, and that seems like what this is really good for. It's basically allowing someone to – you say to someone, you know, you know programming, and now you can turn programming into RF signals, which is amazing, right? I mean, like before you have to go through tons of other stuff to get there, and now this is basically an abstraction layer for RF, which is – that's the beauty of SDR.

**Michael Osman:** Yeah. It's unreal. It is. And that's what got me excited about SDR in the first place. I was a software guy, and I was in an environment where I really needed – in order to demonstrate the kinds of things that I was theorizing, I needed to build radios. And I said, hey, software-defined radios lets me build radios with software.

**Chris Gammell:** It's got my expertise in the title. Yeah. Exactly.

**Michael Osman:** And so I was so excited about that, but then a few years later, I found myself turning into a hardware guy anyway. But I think part of that was just the immaturity of the field at that time. There were software-defined radio platforms several years ago, but they were more expensive, and the software was less mature. And so now we have less expensive, more accessible platforms, and we have better software frameworks. And I think the dream can be more of a reality now that if you're a software person, you can build radios with software-defined radio without having to learn all that much about hardware and RF.

**Dave Jones:** At what point is the software at the moment for something like this? Is it good enough so that you don't really need to program anything? Can you do useful stuff without having to cut code?

**Michael Osman:** You can do some things without code, like spectrum analysis and demodulation of common things like FM radio stations. FM radio, yeah. Like land mobile radios, like public safety radios, both digital and audio. Scanner, right. Scanner type of applications. Modes that are common in the amateur radio community are well supported by some of the software that you can use with an SDR peripheral without having to write code. But I always encourage people to get into the software side of things. Like GNU radio is the framework that I recommend people use. Everything that I do is open source. So I do only open source hardware and open source software. And I've been using GNU radio for years. It's a fabulously powerful software framework for building stuff with software-defined radio. And it's pretty easy to get started with because you can write code for GNU radio in either C++ or Python. So it doesn't matter.

**Dave Jones:** I don't know either.

**Michael Osman:** Either one. But even better than that for getting started is it includes a tool called GNU radio companion, which is a GUI tool for building software. Just kind of drag and drop. Put your blocks, signal processing blocks together and drag a line directing the output of one into the input of another. That's my style. Yeah. It works. It's an incredibly useful tool for just getting started, learning software-defined radio, learning GNU radio. And even if you are a Python or C++ programmer, this is the way I recommend that you start with GNU radio because GNU radio companion actually, after you have built a flow graph in the GUI, you click a button and it generates Python for you. So you can look at the code that it generates and learn how to emulate that and use those signal processing blocks in the same way. Yeah. Twiddle and hack.

**Dave Jones:** I think you've just scared off both of us by the term software framework. No, but then you just want us over with that, you know, just click here and it generates the code. Yeah, thank you very much.

**Chris Gammell:** That's a great way to dive down into it too. I mean.

**Dave Jones:** Maybe I should buy one now.

**Chris Gammell:** There you go, Dave. He's selling now too. Yeah.

**Michael Osman:** Yeah, you should buy a HackRF. Or, you know, if you don't feel like you're ready to jump in headfirst and spend the money on HackRF or any of the more expensive SDR platforms, you could get one of these Realtek TV tuner dongles. Yeah.

**Dave Jones:** Everyone's talking about those. Are they any good? They're amazing.

**Michael Osman:** For 20 bucks they are. That's for sure. You know, they're more, for 20 bucks they're amazing. Right. They're more limited in capabilities than HackRF obviously. But as a way to get started and just experimenting with software-defined radio, it's so cool that people can do that for 20 bucks. Yeah.

**Dave Jones:** And you can use the same software tools. You can. Yeah.

**Chris Gammell:** I've got that in my computer and it's, I think it's SDR Sharp or something like that. It's a C Sharp kind of interface program and it's super simple. And the only problem with me is that I'm in a basement. That's the main thing.

**Michael Osman:** You know, there's a solution for that.

**Chris Gammell:** I know.

**Dave Jones:** Want to be the coax out the window? Yeah. Exactly. Exactly. Well, yeah.

**Michael Osman:** You wouldn't want to actually get out of the basement. I know. Exactly. Yeah.

**Chris Gammell:** Can't let the air in.

**Michael Osman:** SDR Sharp is one of the programs that supports HackRF today. And I think everything today that supports HackRF also supports the Realtek dongles. Yeah. And they're receive only, whereas HackRF can also transmit. And they have a more limited operating frequency range. But it's still a pretty impressive operating frequency range. And you can explore a lot of spectrum and just get familiar with how software-defined radio works for a very low cost.

**Dave Jones:** This would be an ideal platform for those people who want to quite possibly experiment with their car role in remote controls and things like that. If you've heard about, you know, some illegal hacking of, you know, cars, you can sit there and you can record people's remote controls and then open their car.

**Michael Osman:** Definitely. And people have already experimented with those micro-less entry systems with HackRF, for example. Right. And, you know, all of those systems, I think, are vulnerable to some kind of attack. Like if you take somebody's remote out of range of the receiver and push the button and record the signal that it plays, if you beat the owner of that device back to their receiver, back to their car or back to their garage door or whatever, you know, you can replay that code and use it once, even if it is a rolling code, a non-repeating code.

**Dave Jones:** Oh, right. You can still use it once. Right.

**Michael Osman:** Yeah.

**Dave Jones:** And that's really all you need. Usually just once.

**Michael Osman:** Yeah. Like on a garage door, for example. Yeah. Most of those garage door openers are extremely easy to program with an additional remote. So if you get into a garage door once and you bring your own remote along, you can just push a button on the thing and program it to honor the codes from your remote and then you can get in forever. And, you know, attacks like that are maybe not as well known as they should be. And, of course, then there are some systems that don't even use rolling codes. Like any time, the very old garage door openers, for example. Like mine, yeah. Yeah. Some of the, a lot of the ones today that are multi-user. So if you have like an apartment complex or a gated community that has a gate that opens for 100 different remotes, that's probably a fixed code that all the different remotes are programmed to because implementing rolling codes with a large number of remotes is not very practical. So those are things where you can just record a signal and play it back as many times as you want. It's fun stuff.

**Chris Gammell:** What about actually some of the hardware on this thing? I'm looking at the schematic for the, so it's called the Jawbreaker, right? I keep calling it HackRF, but that's kind of the more platform side of it, right?

**Michael Osman:** Well, HackRF is the brand name. And Jawbreaker is just the code name of the beta board.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Right. So what are the primary differences between the beta board and the finished HackRF, which you'll actually deliver?

**Michael Osman:** Right. So I don't have a name, actually, for the finished HackRF. Contest? It probably needs something. It needs something. Maybe.

**Dave Jones:** It needs a Back to the Future name. It needs something.

**Michael Osman:** That would be good.

**Dave Jones:** Related to Back to the Future. Maybe.

**Michael Osman:** Yeah. So I'm open to suggestions. But for now, I'm just calling it HackRF. But by the time I ship it, I probably need to have some better name for it. But it will differ from Jawbreaker a little bit, but not a whole lot. Jawbreaker has a built-in PCB antenna, which was kind of stupid. And I just wanted something that people could use out of the box where all they need is a USB cable. They can plug it in and start experimenting with something. Because I was distributing beta boards to primarily people in the information security community who didn't necessarily have a background in RF and probably don't have antennas around. So that was just a way to facilitate testing. So I'm going to remove that PCB antenna. I'm going to kind of shrink down the whole board by just removing a little bit of dead space and some things that were, you know, like pads that I had for development that didn't end up getting used. And so it'll probably be about two-thirds the size of Jawbreaker. And then I'll put it in a full enclosure and call it done. So it's not – the important bits of the circuit design aren't really going to change.

**Dave Jones:** Got it. What sort of enclosure are you going to use?

**Michael Osman:** I don't know yet.

**Chris Gammell:** I want it to be a full enclosure. All steel. All steel? Yeah, something that will not be great for RF, right? Right.

**Michael Osman:** Yeah. I'm not sure yet what the enclosure is going to be. I was kind of putting off that decision until I knew what my manufacturing volume would be. I know I want it to be fully enclosed so I can throw it in my backpack and it won't get stuff, you know, paper clips in the circuit.

**Dave Jones:** Well, at your current volume of like, what is it, 1,700 or something, that's not a huge volume. You know, you wouldn't go injection molding a custom enclosure for it. Yeah, maybe a soft mold. For example. You might. I don't know. Yeah, maybe.

**Michael Osman:** I already have one product with an injection molded case that I'm only manufacturing in quantities of 1,000 at a time. Yeah, it's only 1,700 at the beginning too. It's not 1,700 forever.

**Dave Jones:** Well, it's China, right? We're talking about China. Yeah.

**Michael Osman:** Right, right.

**Dave Jones:** Although me, I would, you know, if I was involved in, I would like lay out the board to fit maybe an existing off-the-shelf case that then you can machine holes in. Right. Or something like that. So then you can order it directly from the manufacturer. Beige cases. You know all the mounting holes are in place and you sort of, yeah. Yeah, that's definitely an option. But I like to play it safe like that. But I just like, you know, having, being able to buy the case off the shelf and then just go, okay, I can drill the holes manually. Right. But in volume production, they'll drill them for me and, you know. I'm a big fan. All that sort of jazz.

**Michael Osman:** I'm a big fan of the sick of beige cases too. Right. So like I, regardless of what kind of enclosure I have for the final product, it will support, it will support a sick of beige style enclosure. So if people are building their own HackRF board, for example, they'll be able to, you know, even if I have like a custom machined or injection molded case, they'll be able to have some kind of enclosure that they can get made affordably.

**Dave Jones:** I kind of liked this sick of beige fad when it first came out. But now it's like I want to start something else. Sick of clear acrylic plastic with no sides, you know. Right. Yeah. Campaign. Yeah. I think it's been heavily overused. Beige for president.

**Speaker ?:** Yeah.

**Michael Osman:** I can see the point of view. I think that it's a great option to be able to support though for people who, specifically for people who are building their own boards, just because it's so easy to get those things manufactured, laser cut. You know, I, a friend of mine had, I don't know, three dozen of them or something like that just made on his, his friend's laser cutter. Yeah. And we handed them out to, you know, everybody who wanted one at DEF CON. And it's really great to be able to have that very accessible.

**Dave Jones:** Yeah, of course.

**Michael Osman:** It's a small unit manufacturing.

**Dave Jones:** Brilliant. Should we get on to our questions? Yeah.

**Chris Gammell:** I was just going to say the questions are probably a good idea. Yeah. Um, I, I had a question actually, uh, add on to one of the questions that was in here. Um, and of course I have to find it now. Oh yeah. So that's what I was asking. Well, ask yours first. Cause you, you get priority. That's why I was asking about the hardware. So the, the person here asked about the, uh, the zinc chip, which we've talked about, uh, it's been popping up more. And, uh, it, it just, if you had any opinions on that. And I was just wondering, you know, just your design decisions behind the LPC. So it's an LPC is your main processor, right? And then you have, uh, it was a Xilinx part I saw on there. Um, I didn't know.

**Michael Osman:** It's just a CPLD. Oh, CPLD. Okay.

**Dave Jones:** Right. And what is the CPLD doing?

**Michael Osman:** It is simply interface glue between the analog to digital converters and, and digital analog converters and the microcontroller.

**Dave Jones:** Oh, so it's just, right. So it's not any heavy duty.

**Michael Osman:** No, no.

**Dave Jones:** Heavy duty parallel processing.

**Michael Osman:** It is not doing any digital signal processing.

**Dave Jones:** Glue logic. Yep.

**Michael Osman:** And in fact, it may be possible to remove the CPLD from the next design. Yeah, if you get like high certes or something like that. Well, there's a pretty cool feature on this, uh, LPC 4300 microcontroller that we're using where it is called, uh, SGPIO, serial GPIO peripheral. And it's basically a highly configurable external interface that can, that can support various parallel or serial modes. And we're using it in a parallel mode with external clocking. Um, right. The only, and so that's a pretty rare kind of interface to have on a microcontroller, something that can be, uh, you know, a parallel interface that can handle eight bits at 20 million times per second, actually 40 million times second. Uh, and, um, with external clocking. And the only reason we, we put the CPLD in originally was because the ADC DAC chip uses a, uh, DDR interface. And interfacing the DDR with the SGPIO peripheral looked tricky. So, so we put the CPLD in because we knew we could do it that way.

**Chris Gammell:** Yeah. And it's configurable so you can always fix it later.

**Michael Osman:** Yeah. Yeah. It looks like we could do it without, but we might keep it anyway, just because it, it's kind of fun to have that configurability there. Yeah.

**Dave Jones:** And you don't want to go rocking the boat for, you know, your current platform works, right? So you wouldn't want to go changing it for this hack RF.

**Michael Osman:** Yeah. I mean, it's not as, it's not as critical or, or as, as difficult to test as, as maybe changes in the RF path, but it's still, it's still, uh, I want to.

**Dave Jones:** It's a risk. You don't want to go.

**Michael Osman:** I don't want to delay manufacturing because I made some stupid design change that I didn't need to, and it didn't work.

**Dave Jones:** Yep. Just because you thought it would be cool to get, get rid of one part, you know?

**Michael Osman:** Right. I think relating to your question, you know, really, really, really question was about like zinc. Yep. Processor. So we're not using anything like that on hack RF, um, which is a little unusual that we don't have any kind of FPGA on board. We just have this tiny CPLD that doesn't really have any digital signal processing capability. And then we have the LPC 4300 microcontroller. And it, it was our intent. And the, the, the, this decision was made primarily by, by me and Jared Boone, who I mentioned earlier, uh, who's, you know, really had a huge role in this project. Um, we, we decided that, that we wanted to have kind of the, the lowest cost solution that would let us get samples in and out of high speed USB at the maximum rate. Ah, okay. And we didn't really care if we had digital signal processing capability on board because the DSP capability in everybody's laptop is, is so impressive these days. And it, it, now there are some benefits to have ESP on board. So we're, we're having fun with the fact that we did end up with a solution that have some capability, but that wasn't the main goal there. Uh, the, the, the core M4 is, uh, is, or the, the PC 4300 is a Cortex M4, which is, you know, kind of, uh, the top of the line Cortex M series, uh, with, with DSP instructions. And it has a floating point unit and it's running at 200 megahertz and it has a Cortex M0 coprocessor. So it's, you know, it's, yeah, it's not a very big deal. It's a micro, microcontroller. Uh, and it has this built in high speed USB interface that we've been able to run at very, very much at the maximum theoretical speed. So it, it's, it's been great. And we haven't really missed having an FPGA on board. Uh, Jared put together this really cool thing that the HackerF PortaPack, which is, uh, it's just a prototype at this point, but, but it's a, uh, it's like an add on board that plugs into the Jawbreaker. And it has a color LCD screen and a couple of directional buttons and an audio codec with, uh, with, uh, like headphone and microphone jacks. And he, like, he just wrote some code that does wideband spectrum analysis and plugged in a USB, um, battery pack. And it's just running the HackerF with this PortaPack in standalone mode, just as a handheld spectrum analyzer across six gigahertz of bandwidth. Uh, well, not six gigahertz at once, uh, like, like 20 megahertz at once. Right. Right. And he, he was able to, uh, get that running at, I think a thousand FFTs per second. So yeah, which was, I mean, I'm not usually running that. I'm not usually running FFTs that fast on my host computer. So I was pretty excited that, that he was able to do that. And it really kind of, kind of showcases the fact that we do have some DSP capability on this board, even though it wasn't our original intent.

**Dave Jones:** Any plans to have that as an official add on kind of thing for it?

**Michael Osman:** It's definitely something that, um, we're going to keep working on. Uh, it's, it, Jared is, is, uh, he may be working on manufacturing a small number of them just for the people who have the jawbreakers. And then he's, and then he's definitely going to, uh, update the design for the final HackerF board and, and we'll, and we'll make it available for, uh, you know, for anybody who has a HackerF down the road.

**Dave Jones:** Awesome. Awesome. We've got a question from OJazz1. Uh, will there be a different way to power the board? Um, he can't imagine it being able to transmit any significant distance sourcing power from just the USB port.

**Michael Osman:** That is a good observation. Um, we don't really want people transmitting any considerable distance from just... Is that your problem though? The FCC's a thing, huh? Yeah, yeah. The FCC is a thing. And, and, uh, so, you know, we're, we're really pushing the limits of, of USB 2.0 bus power. Yeah. And, and this was another one of our kind of major design goals for HackerF. I mean, our, our big goals were number one, open source hardware. Number two, uh, very wide operating frequency range. Number three, um, uh, transmit and receive. Uh, and number four, portability and, and being able to, um, uh, being able to just plug this thing in on USB and, you know, all you need is a laptop and a USB cable and an antenna. And you can, you can, you can take it with you anywhere you go. Uh, this was a, a really, uh, a key goal for, for me. And, um, and, and part of that is that it doesn't give us that much leftover power for say a front end amplifier, uh, for, for transmit. Uh, we do have, we do have, uh, oh, 10 dB or so of, of amplification that you can switch on at the front end, but that, that doesn't, um, that doesn't get you, uh, into any kind of power that's going to go further than, you know, tens of meters most likely for most applications. Right. So it's something that you can use HackRF to experiment, um, on your bench or across the room. Uh, but if you want to actually transmit signals any great distance, you're going to have to add external amplification. And if you do that, you should also add external filtering and you should know something about what you're doing. Yeah, get an ambulance and everything else. Um, yeah, exactly. So, so that's my answer for anybody who wants more transmit power is you're on your own, but there are a lot of options out there. You know, we have a 50 ohm antenna port and, uh, you can plug whatever you want into the front of it. Uh, I just caution you to, to take care and be a good neighbor on the spectrum and follow your country's laws and, uh, and all that.

**Dave Jones:** Boo.

**Chris Gammell:** He's, that's kind of like what Greg did. So Greg Sharvat, one of the former guests, uh, I went with him down to Hamvention. He ended up buying this old, like super heavy, badass receiver. And then he ended up pairing it up with a transmitter separately because it was only receiver, you know, like actually like pairing up equipment like that. You could do the same thing here where you just have a transmitter, you hook it in, and then you're ready to go and using that as your front end. Right? Right. Yeah. That was a pretty cool hack. Yeah. I like, I like that stuff. Um, I had a question kind of on a personal selfish basis. Did I, did I hear you're using KiCad for all your stuff now? I am.

**Michael Osman:** Yeah. I adopted it. Uh, great. I, I adopted it for Ubertooth one originally when I did Ubertooth zero in Eagle, just because I was kind of going through the spark fund tutorials and that's what we're using. And, and that's what everyone else seemed to be using. And then, uh, and then I started working on Ubertooth one and it quickly became apparent that I needed to make it a four layer circuit board. And, you know, my first thought was, well, let's see how much it costs to upgrade Eagle. And I said, well, it's not, it's not that expensive, but this is an open source project. I want anybody to be able to take this design and use it and modify it and do whatever they want with it. Um, you know, the open source is most important goal for, for me and for my business. Uh, and so I decided I should look around and see if there were any alternatives because I didn't want people to have to pay for a license for some software to modify my open source design. And so I found KiCad and I started working with it and, uh, I thought it was great. Um, it, it, it has its quirks as do most tools. Um, but, uh, but I've gotten used to those quirks and I think, uh, it, it's a pretty exciting project that's progressed a lot since I was using it. And I'm using it now. Oh yeah, even in the last year or so. Oh yeah, I'm using it now for, uh, for absolutely everything, uh, including some pretty complicated projects like HackRF and like my, my Daisho project, which is, uh, uh, uh, multi, multi person, multi board thing, a project that, that, uh, involves FPGAs and USB 3.0. Oh, and all kinds of crazy stuff that's, that's, um, really kind of, we're pushing the limits. We're pushing KiCad to its limits in some ways. What's it called? Daisho? Daisho. Yeah. It's a D-A-I-S-H-O. Um, and this is a project that I started primarily for, um, monitoring and security research into high speed wired communication systems. So, uh, the idea is it's a main board that has an FPGA and some RAM and a USB 3.0 backend to a, to a host computer. And then there are pluggable front end boards that each implement some target, uh, communication medium. So we're targeting high speed media, like USB 3.0, a gigabit ethernet, HDMI, uh, and, and we put on the front end board connectors and transceivers like the five chips for the target technology. And we put, we put a pair of each on. So a signal will come in, a connector into a transceiver, go over to the FPGA on the main board in digital form, and then go back out the other transceiver and connector. And it's a, it's a man in the middle type of architecture. Oh yeah. That lets us do monitoring and injection or modification of traffic on the fly on these very high speed wired communication systems. Yeah. So the project is pretty exciting, I think, because, uh, for, for multiple reasons, one is that we haven't had tools for, uh, some of these high speed communication technologies. Um, like the, the only thing I can think of that is a similar architecture is bunny's any TV.

**Chris Gammell:** Oh yeah. We injected the messages on top of the HDMI signals, right?

**Michael Osman:** Yeah. So we're doing a very similar architecture to that, except supporting, uh, higher rate signals, uh, like the any TV only supports up to, I think, if I remember correctly, 10 80, I, HDMI. Um, and so we're going to support 10 ADP and beyond. Uh, and we're also going to support a whole bunch of other different protocols and we're throwing RAM on the board, which makes it more capable of doing, uh, fun stuff. And it, and we're also putting on this backend USB 3.0 interface, which is one of the most exciting parts of the project because we, there are basically only two USB 3.0, uh, chips that you can buy, uh, in, in small quantity today. And one of them is a pretty high cost microcontroller with USB 3.0, uh, from Cypress. And the other is just a bare USB 3.0 transceiver, uh, from TI. And so we're just using the very simple transceiver and plugging it in to the FPGA and developing an open source USB 3.0 core running on the FPGA.

**Chris Gammell:** That's, that's going to make a lot of companies angry, I bet. Some, some, some, some, some, some, some, some ones happy, big ones, mad. I think.

**Michael Osman:** Well, anybody who wants to develop a low cost, uh, or open source or especially open source, um, USB 3.0 device would probably find this quite cool. Um, and we already have, I mean, this, this work is being done primarily by Marshall Hecht, who's a contractor working for me. And, um, he's already completed all the USB 2.0 functions and is currently working on USB 3.0. Uh, and it's, it's a little bit slow going, but, but he's made great progress and, and it's pretty exciting.

**Dave Jones:** What's the plan for this? Another, uh, another crowdfunded project?

**Michael Osman:** I don't know. I, I, I suspect that Dyshow may be, uh, less marketable than HackRF. Um, but I'm not sure yet. This project still has a ways to go and, and, and exactly what the, the applications are. Um, other than our, our, our main goal is just to get the platform working and support inline monitoring of a handful of, of different communication media. And that has, um, that has some pretty good uses, especially in the information security community, which is, uh, my community primarily. And, um, but I'm not quite sure how marketable it's going to be because it will be a more expensive platform than most of the stuff I'm working on.

**Dave Jones:** Um, well, the good thing about the crowdfunded platform is you put it out there and if you don't meet the target, if there's not enough interest, well, nothing happens.

**Michael Osman:** That's true. That's true. And that's actually, that's one of my favorite things about doing crowdfunding is, is just the fact that it is built in market research. Market research. Exactly. It's, it's great.

**Chris Gammell:** Um, did I, did I see on your Kickstarter profile that you had one that was not successful? Was that right?

**Michael Osman:** Yeah, I had one that was not funded, um, like a, a little over a year ago. Um, and, uh, I actually think of that project as being a great Kickstarter success because, uh, because I learned that, uh, it wasn't, that that device was not marketable the way I thought it was. And I learned that with, with, you know, with, with, you know, very little, at very little cost. I didn't, I didn't, I didn't make a thousand of them.

**Dave Jones:** Can you tell us what the product was?

**Michael Osman:** So, it's called the Firefly cap. Um, and, uh, it's just a hobby electronics product, which is a little different for me to have something that's kind of pure hobby electronics. Um, but it, it's, um, a lid. Do you have mason jars in Australia? Uh, they're like a home, home canning jars or jelly jars that have a two part lid. Yeah. It's like a seal. Oh, right. I think I, yeah. The seal. Yeah. It has a, it has like a disc and then there's a threaded ring that goes, that holds the disc onto the top of the glass jar. So these are super common in the U S like everybody has some of these jars in their cupboard. And, uh, and so what I did was I made a circular circuit board that's made to replace that disc. And, and, and it has contacts on it to which you can solder an array of LEDs and it's a jar of fireflies. Um, which of course, you know, lots of people in the hobby microcontroller world have built their own jars of fireflies, uh, which is how this project started. But what was, what was unique about this project was that, um, I had it powered by a, uh, photovoltaic panel and a super capacitor with an energy harvesting circuit that would work in indoor lighting conditions.

**Chris Gammell:** Ah.

**Michael Osman:** And I mean, so you guys know that that is a major challenge getting, getting something like that. Yeah. Yeah. Yeah.

**Michael Osman:** As a, as a designer and as a, my own personal project, that was the challenge. And that was, what was fun about that project was making it work indoors and it, you know, under kind of moderate indoor lighting conditions, it would wake up as soon as it got dark after charging all day and put on a light show for a little while. You know, it might only be 10 minutes, but it just sort of would, when it gets dark, it would simulate fireflies for a little while. And if it happened to get a lot of sunlight, like it was put in a window, uh, then it would, it would put on a show for much longer, like an hour or something like that. And, um, uh, so that was a big challenge. And that made the thing, um, more expensive than it otherwise would have been. And, and so what I learned from putting it on Kickstarter primarily was, uh, when people see this thing, they immediately think of, uh, a $5 garden light. And they think, they think, why, why does this thing cost $30? That's stupid. Um, he's, you know, I'm, I don't, I don't want to pay that much for this and he's never going to reach his funding goal. Um, and so that was, so it was extremely educational for me and Kickstarter did for me exactly what I needed it to, which was show me that while this project was great fun for me personally, it, it, it wasn't marketable in the way that I thought it was.

**Chris Gammell:** Customers are still a thing, huh? Yeah. Go figure. Just like the FCC, FCC. Yeah.

**Michael Osman:** Still a thing. So, but that, but that was a really cool project and it may be something that I revive someday, but it's never going to be, it's never going to have the mass appeal, uh, that I thought it might. And I, and I also, I set my funding goal probably higher than I needed to, um, in part because, uh, I wasn't a hundred percent convinced that that's where I wanted to take my company. That, uh, you know, I wanted to make something higher volume for a larger market as opposed to focusing on more niche products and more focusing more on, on my own community, uh, the information security community. And, uh, so it was kind of like, well, if there's enough interest to make it worth kind of taking on supporting all these first time microcontroller hobbyists, uh, then maybe I'll manufacture the thing. So I set the goal kind of artificially high. Um, and that to some extent bit me too, because people would see that high number and say, ah, he's never going to meet that goal. Uh, I won't bother.

**Chris Gammell:** Yeah. Psychological stuff, right? There's always barriers. Yeah. Yeah.

**Dave Jones:** So that's a lot of, that's a mistake. A lot of people make, they think that, you know, to be successful, they have to go into high volume consumer stuff yet. Some of the most successful people out there are the niche players.

**Michael Osman:** Absolutely.

**Dave Jones:** For example, like, you know, yeah, it may not make you filthy rich, you know, it may not make you Apple rich, but it's, you know, but you can make a damn good living. Absolutely. I don't think the pebble guys are filthy rich, man.

**Chris Gammell:** I don't think the pebble guys are filthy rich, man. I think the pebble guys are.

**Dave Jones:** Yeah, well, maybe. But, you know, well, no, I wouldn't say they're filthy rich. Yeah, they got their 10 million bucks or whatever, but, you know, I'm sure you spent a lot of that actually. Yeah, exactly. That's what I'm saying too. Right. Manufacturing a proper polished consumer product.

**Michael Osman:** Right. Yeah. Right? That is such a huge responsibility.

**Chris Gammell:** Yeah. Plus, it's nice that you, I mean, you target people that are really interested in, you know, like people that are using SDR type stuff at least have a very deep interest in it. Right? You have a certain type of person you're targeting with that. So you probably get a lot of benefit from people that contribute to the repositories and, you know, feedback bugs and everything like that instead of just asking for a lot of support. Right? They'll go figure it out themselves.

**Michael Osman:** Huge benefit. And that's been a part of the way I run Grayscott Gadgets from day one is that I do everything in the open source way. Like all the things that people commonly do to execute and support open source software projects, I do with my open source hardware projects. I use open repositories and I use wikis and I have support channels like email lists and IRC channels. And I've really had the benefit of getting a lot of my own users kind of involved back involved in the project and contributing to the projects. And, you know, now I have half a dozen contractors working for me and they're pretty much all people who volunteered to help with my projects. And then down the road, I was able to say, hey, you know, I have some funding for this thing. How would you like to, you know, keep doing this kind of stuff and actually get paid for it? And, you know, that's my only recruiting method really is just taking volunteers who I know do good work and I know are interested in this stuff and finding ways to, you know, give back to them the way that they're giving to my projects. You know, I can't do that for everybody, but I try to do it where I can and specifically in the form of contract work for them to do specific development tasks on various projects.

**Chris Gammell:** So I have another selfish question because I was just learning GitHub this weekend or Git really in general. Yeah. So, I mean, what's the deal with that in hardware? Because I'm kind of learning about that as I go. And, I mean, does it fit well? Is there stuff that it's good at or not good at? We've been talking about it on the show a little bit in the past and just revision control in general with hardware.

**Michael Osman:** Yeah. I've pretty much migrated all my projects to GitHub. I like GitHub. And the main reason I like GitHub is because I really like Git. Git is an outstanding tool. And GitHub is a convenient place to use that tool. The, you know, almost all my projects have multiple facets. Like there's a hardware design and there's some firmware. And then there's some software that runs on a host computer that talks to that firmware. And so I have, you know, multiple parts, some of which are software and some of which are hardware. And that all kind of need to be kind of consistent with each other and track version numbers together and so forth. So using, and I have a lot of volunteers who are helping out with my projects or contractors who are helping out with my projects. So it's essential to have some way to collaborate. I find Git to be an excellent tool for hardware and for software. As long as your design software for the hardware side uses a text-based file format. Which KCAD does, of course. And we do, like, we generally collab. I get more collaboration on software than I do on hardware typically. But it's very common to have kind of in my loose-knit team two or three people working on a hardware design together. Where only one person is making substantial changes. And the others are acting as a sounding board, are doing design review, are helping with architecture decisions. They're like, how about you use this chip here? And so we very much take the approach of one person is a designer and other people are there to help that designer. The Git and other revision control systems aren't really, aren't too well suited for software like KCAD. Or really, it's the other way around. KCAD isn't too well suited for software like Git.

**Chris Gammell:** Concurrent design, right? Right.

**Michael Osman:** In terms of concurrent design, right? Branching and merging. We've done a little bit of branching and merging with our KCAD designs. But it's dangerous waters. Yeah. Because, you know.

**Chris Gammell:** I didn't put that part there.

**Michael Osman:** Who put this part here? It mostly, like, certain changes work really well. Like, if you go through and update all of the, and put manufacturer and part number information in for all the 10K resistors in a design. Mm-hmm. Without actually, like, changing the layout. That kind of a change. That kind of a change, it works extremely well in a revision control system. But actual changes to the layout or to the circuitry are things that we haven't done much of other than just, we haven't done much of in a multi-user mode. Yeah. Or multi-designer mode.

**Chris Gammell:** There's a script, a script I saw of the weekend where this guy Robert on Twitter, he actually does, he creates Gerbers from, he dynamically generates them and then overlays them. So you can actually see the, see, like, where the parts have changed and everything. It's like a visual diff. Oh, oh. Which is like in real time.

**Michael Osman:** In real time or close to it? Yeah. That's cool. Yeah. That's like a continuous integration sort of concept.

**Chris Gammell:** Yeah. It still seems really difficult. But it's just, he wrote it for himself. So, again, getting it to, like, a wider audience would be tough. But, yeah, it's really, that's really cool. Yeah, absolutely.

**Michael Osman:** I think that's a great use of the technology. And that's the kind of thing that I'd like to do more of. And I'd like to do more automated testing. Now, when you're making hardware design changes, you can't really, you know, you're limited as to how fast your testing cycle can be. But it's definitely worth pushing that limit. And it's also worth doing automated testing for things like firmware changes. But it is hard. You know, you have to have some kind of a setup where you have the attached hardware and you have programming system and some kind of automated tool to take whatever's been committed to the repo and, like, automatically compile it and install it and run some kind of test procedure. It's a lot harder when it comes to software and firmware than it is for a, or for hardware and firmware than it is for a pure software project. But that kind of continuous integration and testing has become the norm in many areas for software development. And it's an incredibly valuable tool, especially when you are trying to promote collaboration with multiple people. You want to find, if somebody breaks something, you want to find that out right away instead of finding it out, like, a month later after everybody else has forced that code. So, finding ways to do that more with hardware and firmware is something that I'm very interested in pursuing down the road.

**Chris Gammell:** You software guys are messing up hardware in all kinds of good ways. Yeah.

**Michael Osman:** Well, we're only going to get so far with it. Well, yeah, solder is still a thing. With continuous, yeah, solder is still a thing, very much so.

**Chris Gammell:** Sold is my favorite programming language. That's right, yeah. Yep. It's not going to, it's going to fix a lot of stuff still.

**Dave Jones:** Do we have any last minute Reddit questions? There is a technical one here from Super Coup. Super Coup. How fast will the HackRF be able to retune and settle the oscillator to jump between frequencies?

**Michael Osman:** Oh, yeah, that's a good technical question. Yeah.

**Dave Jones:** Do you have a technical answer?

**Michael Osman:** Yeah, yeah. I can say a few things about that. But one is that for a lot of frequency hopping systems, you don't actually have to retune in hardware. Because HackRF can operate simultaneously across 20 megahertz of continuous bandwidth. So if you have, like in the 900 megahertz ISM band in the United States, there are a lot of proprietary frequency hopping systems that hop through a set of channels that all the channels together fit within 20 megahertz of bandwidth. So to implement that, you don't have to retune the hardware at all. You just retune in software. And it's instantaneous. But there are some applications, certainly, where you might want to retune in hardware. And Bluetooth comes to mind, for example, because Bluetooth operates over 79 megahertz of bandwidth. And we don't have that much on HackRF. So if you wanted to hop along with a Bluetooth network, you would have to retune in between packets. And in the case of Bluetooth, you have a little over 200 microseconds in between. That's like your minimum time between packets. And that's pretty typical. You don't see, I haven't seen a lot of frequency hopping systems that really push that to a lower number than about 200 microseconds usually. With HackRF, we haven't really optimized the tuning and receive transmit time yet. But when we do, I expect to get that time under about 100 microseconds just based on the parts we have. And we actually have multiple stages at which we could accomplish that tuning. So if it turns out that one stage isn't as fast as I think it's going to be, then we can always just use a different stage to do that tuning. So I'm pretty confident we'll be able to hit that 100 microsecond ballpark. However, and this is the big gotcha, that's the tuning time after the command is issued by the microcontroller. If you want to control frequency hopping from the host computer, you also add in USB latency. Yep. And that's going to push you, yeah, that's going to likely push you way over 100 microseconds. And potentially be a problem for any frequency hopping implementation. So if you want to do a frequency hopping implementation, and it is wider than 20 megahertz of total, all the channels, then you'll probably need to implement your frequency hopping in the microcontroller. Yeah, right in the firmware there. Which fortunately is pretty easy because it's an ARM microcontroller and it has a built-in bootloader. And if you have any experience in software development, it's a pretty accessible platform. If you've done any C code on any architecture, it's not too big a leap to learn how to write C for an ARM and get it compiled and installed. So that's one of the nice things about having kind of a general purpose microcontroller as opposed to an FPGA, is that it just makes that kind of development a little bit more accessible.

**Chris Gammell:** Did you have to learn FPGAs as well? Is that like another one of your skills now too?

**Michael Osman:** Yeah, I'm not great with FPGAs. That's one of the skills that I've in particular sought out from people who work for me. But I know enough to be dangerous. And it's something that I'm working on getting better at. But I haven't had to do too much yet because we went with an FPGA-less design for HackRF. And my first real project with an FPGA is Daisho. And I have other people doing those parts of the project. So I haven't been forced into becoming as much of an expert in FPGA development as I probably should be.

**Chris Gammell:** Well, once it's in the world, the buck stops with you. So you'll be learning it at about 1, 2 in the morning, the day before it goes to the manufacturing. So yeah, you'll be fine. It's easy. Well, Mike, I'm very impressed with that. Four years, really? Like I said at the beginning of the show, you're making us all look bad here.

**Michael Osman:** Well, honestly, a huge part of why I've been able to do what I've done in a relatively short amount of time is online resources like the Amp Hour, like SparkFun's tutorials, like so many of the things that have been made available by guests that you've had on the show and all the people in the open source hardware community. And that is really why I am so dedicated to open source. Everything, even going back into my IT days, absolutely everything I can think of that I've ever done in my entire career that I was proud of, I did with something that was open source. And so I feel very strongly that I want to give back to that community. And that feeling has only increased as I've gotten into hardware because the rapid development of the open source hardware community over the last decade is really what has enabled me to take this stuff on.

**Chris Gammell:** Does that mean you're going to be there in Boston this coming week? Unfortunately, no.

**Michael Osman:** No, darn. I just have a terrible travel schedule right now. For some reason, like everybody wants their conference to be in September and October.

**Chris Gammell:** And so do weddings too. That's why I've missed it. Yeah, right.

**Michael Osman:** Yeah, so I really wanted to go this year and last year and both times had to make the hard choice not to.

**Chris Gammell:** Maybe next year. Maybe when Dave finally comes over. Yeah. Finally. I'll make you a deal. I'll make you a deal, Dave. If you go, I go.

**Dave Jones:** Yeah.

**Chris Gammell:** Right. Oh, man, that's easy out. I'd say instead we just start having conferences like in like January, February timeframe. There's a bunch of conferences in like Australia. So it's like, oh, sorry, dear. I have to fly to this warm location while you're freezing in Cleveland. See you later.

**Dave Jones:** That's the, yep. Yep. Just move everything here.

**Chris Gammell:** Not a problem. No, Dave, just start a conference. That's what I'm trying to say, you know. Oh, right. Three-person conference. Me, you and Michael. I'm there.

**Dave Jones:** Can do. All right. Can consider it up. Thank you very much. Michael Osman. Even your last name, I just realized, is O-double-S. Yes. M-A-double-N. Open source software man.

**Michael Osman:** Yes. I didn't even recognize that until somebody asked me. In all seriousness, somebody asked me just a few months ago, like, if I change my name to Osman for that reason. Right. And I was like, oh, wow. I never thought of that. Pretty funny.

**Dave Jones:** Oh, boy. Next thing you know, we'll be having, you know, people's kids named. Right. Open or something. Right. Yeah.

**Chris Gammell:** After a famous astrophysicist or something.

**Dave Jones:** Sagan's an awesome name. Thank you very much.

**Chris Gammell:** I agree. Yeah. I totally agree.

**Dave Jones:** I get much praise for that.

**Chris Gammell:** Yeah. So, Michael, where can people find you on the net? I mean, GitHub, sites, or where's the best place to start?

**Michael Osman:** Yeah, probably the best place to start is greatscottgadgets.com. Okay. That has links to my blog and GitHub for various projects and Twitter. I'm at Michael Osman on Twitter. But that means you have to know how to spell Osman.

**Chris Gammell:** Double-S-double-N.

**Michael Osman:** Double-S-double-N. Yeah. That's good.

**Chris Gammell:** All right. Well, thanks again, man. And, you know, enjoy your 500 grand that's about to hit your bank account. Thanks.

**Dave Jones:** Which I guess we really have to produce them. Yeah. Right.

**Michael Osman:** Yeah. Yeah, exactly. That's the thing. I see that number go up and I'm like, oh, wow, that's a big obligation.

**Chris Gammell:** That's a lot more units.

**Dave Jones:** There's like 35 hours left, folks, as we're recording this. Probably about 14. Right. By the time you hear this, it's probably like one hour left. Yeah. Right. Yeah. Yeah.

**Michael Osman:** Well, thank you guys so much for having me. I've been listening to the show for, I don't know, 100 episodes or so. We're sorry. It's one of my favorites and it's really a pleasure to be here. Well, thank you very much. Thanks for coming on.

**Chris Gammell:** All right. Well, we'll see you at the next conference, hopefully. But until then, we'll be looking at all your awesome projects. All right. See you, Mike. See you. See you then.

**Michael Osman:** See you then.

**Speaker ?:** See you then. See you then. Bye. I love you.
