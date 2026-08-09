---
episode: 123
title: An Interview with Jon Oxer - Innoxious Implant Innovator
url: https://theamphour.com/the-amp-hour-123-innoxious-implant-innovator/
---

**Chris Gammell:** This episode of the Amp Hour is sponsored by Club Jameco, part of Jameco Electronics, a leading component distributor for over 35 years. Club Jameco allows you to upload your kit ideas and start selling to your peers and the public at large. You never need to purchase large lots of components up front or bag and ship your kits. Sign up and submit your design, and if it's chosen by the community, you can start making up to 10% on the cost of your kit. To learn more and see some of Chris and Dave's favorite kits, go to clubjameco.com slash theamphour. This is the Amp Hour podcast, recorded November 26th, 2012. Episode 123, with guest Jonathan Oxer, inoxious implant innovator.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of ChipReport TV and Chris Gammell's Analog Life.

**Jonathan Oxer:** And I'm Jonathan Oxer from Freetronics and IVT.

**Dave Jones:** Woohoo! Thanks for joining us, John. Another Aussie.

**Jonathan Oxer:** No worries. Yes, we've got him outnumbered this week.

**Dave Jones:** Excellent. Although you're originally a Pom, aren't you?

**Jonathan Oxer:** Well, technically, yes. I was born in London, but I came over to Australia when I was just a little wee baby. So I think I qualify for a UK passport or something, but I've been in Australia pretty much my whole life.

**Chris Gammell:** Yep. You got the accent, so that's all I manage. Yeah, that's right.

**Dave Jones:** Exactly. Unfortunately, he's from Melbourne, folks.

**Chris Gammell:** Oh.

**Dave Jones:** A bit of Sydney-Melbourne rivalry.

**Chris Gammell:** So, okay, John, my first question is, you know, we've had Alan on before. I think he might be the... I guess Philip was originally from Australia, but I guess we didn't really ask Alan about the electronics scene in Australia. How full of crap is Dave in general? About what? About everything. About everything. Everything Australia, everything electronics around there.

**Jonathan Oxer:** No, mostly he's pretty much spot on. Ah, come on. Thank you very much. Help me out here, man. No. Thank you. The thing is that... We got a plan. He's been paid. Yeah, yeah. I'll give you my bank account details later. Yeah, right. The thing is that my experience of the industry, if you talk about it from an industry perspective, it's pretty limited. I'm really coming from a hobbyist perspective. So, I haven't done any of the sorts of projects that Dave has when he talks about some of his military projects and that sort of stuff. That's way out of my league.

**Chris Gammell:** So, what's your background then?

**Jonathan Oxer:** My background is as a random tinkerer, basically. I don't really claim any particular skill or experience with any one field. And we like that. We do. Yeah. I make stuff up as I go along. Just like us. I've spent many years working in software and just playing around with hardware. My early days, my background was in hardware. And I ended up diverting and spending so much time just sitting at a computer keyboard and not enough time holding a soldering iron. And it's really just in the last four or five years that I've started to get back into actually building things again, which has been a fantastic experience. And, of course, it's totally different now to what it was like 15, 20 years ago, last time I was doing things with hardware.

**Dave Jones:** Yeah. How many potential hardware tinkerers and engineers are lost to software, I wonder? Oh, yeah. Because I strayed down the software path at one point. You know, I was working. I was doing software projects. I was spending most of my time programming as opposed to doing electronics at one point.

**Jonathan Oxer:** So, I'd like to know. Yeah. I think a lot are. Yeah. I've actually had a really interesting experience with that because for the last few years, I've been running the Arduino MiniConf, which is a one-day event that's tacked on to the start of the LinuxConf that takes place once a year in a different city around Australia or New Zealand. And LinuxConf is basically a whole bunch of software geeks because it's all about Linux kernel and open source software development. And for a couple of years, I ended up doing talks there about hardware hacking and introducing software people to the concepts of hardware and demystifying it a little bit, just showing, hey, it's not actually that hard. If you have a parallel port on your computer and it's really easy to address in software and it gives you a gateway. Yeah. Well, seriously. It's a talk from the 80s, you know. Yeah. Well, that was how it started. It started. But that's a really good way conceptually of getting software people over it because you can explain the parallel port as simply being a representation of bits in memory. Yes. So you just say, you know, you write to these eight bits and these eight pins go high or low. Yeah, that's right.

**Dave Jones:** Oh.

**Jonathan Oxer:** Things back in the moment. I did a couple of talks about that at the software conference. And people, like software people are really interested in it. And they have this concept that it's magical and it's beyond their capabilities. And so I did a number of talks where I just showed that it's really easy to get started with hacking around with hardware. And that led to the Arduino MiniConf, which is this one-day event. It's been run – we've run it three years now and the next one's coming up in January. And what happens is that we end up with between 50 and 100 software people in a room for a day. And we take them through learning how to solder and some basic Arduino projects and do talks about how to do things with Arduino. And they're typically extremely strong from the software point of view. I mean, people who come along are Linux kernel hackers and people like that. But they haven't had the opportunity to hold a soldering iron. And a lot of them just love that opportunity. It's like being a kid in a candy store. So I think we do tend to lose a lot of hardware hackers to software. But I think for a lot of people and people that are interested in software, anyone who has that sort of inquisitive nature and they want to understand how things work and they want to make things, the idea of being able to make something physical rather than just make software on a computer is really attractive. And they really want to give it a go.

**Dave Jones:** And there's so many options to do that these days with Arduinos and quadcopters and all sorts of fantastically fun things to play with.

**Jonathan Oxer:** Yeah, we're in a golden age at the moment. It's fantastic what you can do.

**Dave Jones:** It's almost as if they've got it easier these days. Because back in the 80s or something, stuff like doing microcontrollers, for example, was actually really hard and really expensive. Yeah, absolutely. Totally different. Now, most people know you from Freetronics, right? I would hazard a guess most people listening to this show anyway.

**Jonathan Oxer:** Yeah, for this show, certainly.

**Dave Jones:** And you're doing – tell us about Freetronics, how it came about.

**Jonathan Oxer:** Well, Freetronics came about – there are a couple of reasons that it came into existence. One was the Arduino MiniConf. Part of the Arduino MiniConf was that I wanted to put together a bunch of kits for people to assemble, you know, to go through this hardware assembly project. And it basically turned out to be a total pain managing the money side of it. So what happened was that we had a couple of people that would help out. There were some friends from the Melbourne Hackerspace who helped design the actual project. So we'd have PCBs manufactured. We'd get in parts, sit there around the kitchen table and count all the parts out into bags and that sort of thing. And then we'd have to collect money from people. And there was all this big overhead in terms of the actual process of administration of how to do this. And then figuring out expenses afterwards and dispersing cash to people. So part of it was that the – it was a mechanism to allow that sort of thing to happen. And the other part of it was after Practical Arduino came out, which is a book I – Yeah, a couple of years ago. I got a call from a buyer at Electus, which is the wholesale arm behind J-Car that Australians at least would be familiar with. For everyone else, it's basically an electronics parts chain in Australia. And they –

**Dave Jones:** That sells the finest imported stuff China has to offer. Exactly.

**Jonathan Oxer:** It's a bit like what Radio Shack used to be like. Yeah. Yeah. You can still walk in and buy resistors and that sort of thing, which you can't do in many places now. And they wanted to carry this book because they'd heard of Arduino and they were selling a few PIC-based modules and things. But they didn't really – they weren't really going anywhere and they wanted to start carrying much more in the way of Arduino. So they called me up and said, we want to start selling your book. So can you please put us in contact with the publisher so we can buy it directly? And we also want to sell some hardware to go with it, like maybe some Arduino boards, some shields, just to give people the tools they need to get started. And where can we buy those from? And after thinking about it for a little while – Hello. Hang on. It just so happens. Well, the point was that we weren't – Just give me a couple of weeks, folks. Yeah, that's right. So I ended up talking to a good friend of mine, Mark Alexander, who's my partner at Freetronics now. And we set up the company. And also Hugh Blemings was involved in the early days. He was the co-author of Practical Arduino. And so we did some quick running around and thought, hmm, they want to buy Arduinos. We can supply those. So we did some designs and got some fabrication happening and did some production runs. And it's all grown from there.

**Dave Jones:** In China, I assume, to get cost down because J-Car would want them pretty darn cheap.

**Jonathan Oxer:** Yeah. And a fast and large volume as well. So, yeah, we are doing – we do all of the design and prototyping and that sort of thing just here in Melbourne. But for volume production, we do it in China. Yeah. In fact, a lot of the early ones, the really early boards, were based on projects from Practical Arduino. And the way I actually got started with that was I designed the PCBs for them in Eagle, sent the designs off to PCB cart, got the bare PCBs back. I bought in surface mount parts and I baked them in my toaster oven. Nice. So probably the first few hundred boards that we shipped were actually baked in my toaster oven at home, literally in the kitchen. It's like HP, right, with the mecalate in the oven. It's back-breaking work, though. I hunched over the microscope for hours. Oh, yeah. No. It doesn't scale.

**Dave Jones:** It's a bit of a mugs game, really, when you start trying to, you know, assemble your own boards. And people are talking about pick and do-it-yourself pick and place machines and stuff like that. And, you know, you're better off handing that off to people who, you know, more enjoy doing that sort of thing and are better and more efficient. Yes. Right.

**Jonathan Oxer:** And have the tools. It's all about tools. Yeah. It's amazing how fast a good production facility can work.

**Dave Jones:** So you produced, what, many, many thousands of these things starting off with Jcar, and then you set up the web store and decided to sell them yourself?

**Jonathan Oxer:** Yeah. Well, we – what actually happened in terms of the sequence was Jcar got in touch and said, we'd like to sell them. And so we ramped up to produce them. And then it took – I think it was about six or eight months before they actually wanted to proceed. So in the meantime, we set up the web store and then we brought on other resellers. I think we had about five other resellers or six other resellers. So we've now got resellers all over the world, like in Germany, England, the US, New Zealand.

**Dave Jones:** Because like me, do you find that really shipping stuff from Australia is a pain in the ass? That's why you have the resellers?

**Jonathan Oxer:** Yeah. Yeah. That's it. It's so slow. It's just ridiculous. And it's really weird the way it's so different. You can order something from the US on a Tuesday and it will arrive on like a Thursday or a Friday in Australia. Yep. You send a package back the other way and it will take three weeks to arrive on their doorstep. It's just crazy.

**Dave Jones:** And then all the customs forms and stuff like that. There are more automated ways to do it. But yeah, dealing with Australia Post is not as efficient as in some other countries. Yeah, that's right. Yeah.

**Jonathan Oxer:** So we use a shipping agent now. I used to walk down to the post office every day with a big bunch of packages and write all of the customs declaration forms by hand. Yeah. Oh, yeah.

**Dave Jones:** Been there, done that. I had a stamp made up properly to sort of semi-automate the customs forms and things like that. But now I simply just refuse to sell directly to overseas people. Oh, really? Yeah. I only sell to Australia and I have various resellers in other countries now. So if you're overseas and you want to buy one, go to the reseller, please, because it's not worth my time to hassle with Australia Post. But whereas within Australia, it's easy. You just throw it in one of the prepaid bags and boom, it's done. Yeah, and where it goes. Yeah. Very simple. So any advice for people getting into the hardware kit business like that? Don't?

**Jonathan Oxer:** Yes. Well, I suppose the major thing to think about is scaling and you have to optimize everything. Don't spend your time doing things manually. Make sure you set things up so that it all scales.

**Dave Jones:** Yep. And try and get resellers, even though you don't make as much money. No, that's right. Because you go through resellers and they have to make their large margin on it as well. So if you don't put sufficient margin, we talked about this a lot on the show. Yeah. The minimum is like 2.4 times your bomb cost everyone talks about. But that's absolute minimum kind of thing to make it worthwhile.

**Jonathan Oxer:** Yeah, I think Chris Anderson did a great blog post a while ago about margins and how to calculate how you should do your markups. There's some really interesting stuff there. A lot of people approach this with the point of view of you look at your bomb cost and then I'll add 20% or something for your margin and that just doesn't work that way.

**Dave Jones:** Yep. No, it's not easy at all. So there's plenty of info out there, folks, if you do want to go do your own hardware startup, which every man and his dog seems to be doing these days, which is great. It's great to see. Everyone's doing kits and shipping them.

**Jonathan Oxer:** Yeah, that's very cool.

**Dave Jones:** So how much time do you spend on Freetronics these days? Because you have a lot of things. What, you're the head of Linux Australia or something. You're doing Superhouse TV. Yep. TV show about home automation. Tell us everything you're working on at the moment. Okay. Or have we got time left in the show?

**Jonathan Oxer:** Well, Linux Australia, I was president of Linux Australia for three years, but that finished up a few years ago. So I'm only peripherally involved in that now, only in the annual conference. So that's not really too much of a time sink. Probably my major business over the last few years has been Internet Vision Technologies. That's my software company. And so I've got, I think, 24 staff in that business. Oh, wow. Okay.

**Dave Jones:** That's a serious size company.

**Jonathan Oxer:** Yeah, yeah. It's doing really well.

**Dave Jones:** I had no idea. There you go.

**Jonathan Oxer:** Yeah. So that's...

**Dave Jones:** So how much time do you spend managing that day to day?

**Jonathan Oxer:** Well, very little as of a few weeks ago. I was doing more than full time in that. Right. And I found that I just couldn't split my time efficiently enough or effectively enough. So we've now appointed a general manager for that company. And I've actually moved myself physically out of that office. So up until a few weeks ago...

**Dave Jones:** So you aren't tempted to do...

**Jonathan Oxer:** Yeah.

**Dave Jones:** So you aren't tempted to get involved? Yeah.

**Jonathan Oxer:** It's a matter of stepping away from the minute to minute or the day to day operations of the business as well. I'm just thinking about the higher level strategy of the company. So I know I have a desk at that office. So I've moved another staffer into my desk. So my office now is at home. And we've been doing big renovations at home and set up a really nice office slash workshop area, which is fantastic. And so now I'm spending far more of my time on Freetronics. And so Freetronics, in terms of development as a business, is much more at the stage where you have to be very hands-on and dealing with day-to-day issues and answering support emails and designing boards and things like that.

**Dave Jones:** Do you find it more enjoyable because you find the hardware aspect more enjoyable? Or have you just had a sort of like, oh, the other company, been there, done that. It's got 24 employees. It's big now. I want to do that challenge all over again kind of thing.

**Jonathan Oxer:** I think it's probably partly both. One of the things, the further I go on, the more I realize I don't know about how to run businesses and I keep thinking about everything about life. Yeah, yeah. Join the club. So in retrospect, the way IVT as a company developed, it could have been done so much better. And it's one of those iterative things where I think about, oh, I wish I'd done this or I wish I'd done that. And it's a bit of an opportunity to do it again and try to do things in a better way. So one of the traps that I fell into with IVT was doing way too much in-house. So when we needed to, and this is a trap I think you fall into as a software company in particular, you see a need for something like, okay, we need a project management system. Now, your job is not building project management systems, but you build a project management system. Give me a year. Exactly. Exactly. So you end up-

**Dave Jones:** How many companies have made that mistake?

**Jonathan Oxer:** It's the obvious one, but we fell into it big time. And so for the last two years or so in particular, what I've been really trying to do is streamline the company and just say, this is the core business and anything else, don't spend your time on it. So we end up using external tools for things like project management. And we used to do things like run our own mail service, so we now use Gmail for mail servers. And just that sort of process, the idea is to trim off everything you don't need to actually do as your core value for the business. Right. Yeah. I think that-

**Dave Jones:** And it's obvious with hindsight, isn't it? Yeah, it is.

**Chris Gammell:** It is. Especially when you look at the UI for whatever you design, you're like, oh, we didn't spend any time there. Yeah, that's right. Something like that. It's like, ooh.

**Jonathan Oxer:** Yeah. Oh, man. And I think that's the major lesson that I learned that I've really carried over into Freetronics. And the idea with Freetronics was to set it up so that there was zero or as close to zero infrastructure as possible. So when we set it up, for accounting, for example, instead of installing MyOB or whatever, we use Xero, which is an online accounting package. And we use Google Apps for documents. And as much as possible, we try to not rely on any of our infrastructure. So it's part of that whole lean startup sort of philosophy. And the idea is just focus on what it is that your business is all about and the value that you can add. And don't worry about the rest.

**Speaker ?:** Right.

**Chris Gammell:** So what would you say that is over other kit businesses and stuff? I mean, is it mostly the localization of being in Australia? Or are there kits you could think that really blow others out of the water? Can you tell us about those?

**Jonathan Oxer:** You mean in terms of what is good about Freetronics?

**Chris Gammell:** You know, like lean startup and focusing on what you're good at, right? So if you were telling someone, you know, like, this is what we're really good at, what is that thing?

**Jonathan Oxer:** What is that? Oh, okay. Sure. In terms of Freetronics, what we've done, what we found has been most effective is to create reasonably special purpose boards. So in the case of Arduino, probably our biggest selling board is called the EtherMega, which is like an Arduino Mega with Ethernet built into it. And it just solves one of those obvious problems that you've got to stick an Ethernet shield on if you want networking. So one of the early boards we did was called the Ether10, which was like an Arduino Uno with Ethernet on board. And that's been really super popular. And so has the EtherMega. And so we have the staple boards that are things like the 11, which is a basic Arduino model that I personally think it's one of the nicest ones, of course. But it has the same sort of features as other boards. But there are plenty of other. That's right. Yeah. Whereas something like the EtherMega, there is no other manufacturer in the world making something like an EtherMega. Really?

**Dave Jones:** I can't believe there's nobody else making an Arduino with an Ethernet on it.

**Jonathan Oxer:** Do you think? Not with... Surely. There is a board called the Arduino Ethernet, which is based on the Uno with Ethernet on board, but it doesn't have a USB interface, which means that you need an FTDI cable or something similar to program it. And there is no equivalent anywhere for something like an Arduino Mega with on-board Ethernet. Right. And the Mega is really useful because by the time you add the software stack necessary to do your network connectivity and you want to store a bit of data and do some IO, you quickly run out of pins and memory and things on a standard AT-Mega 328 type platform. So the bigger MCU and the EtherMega is a good combination. But a lot of this came out of just wanting it for myself. And my... I mean, people would kind of laugh about this probably, but my approach to market research is to ignore the market and think, what do I want? I'm going to make that. Want, exactly. That's the way to do it.

**Dave Jones:** And it almost works every time. You know, because there's always, you know, it turns out, yeah, there's always somebody else out there who wants the same thing. You know, whether or not it's a huge market or a smallish niche market, it doesn't matter. There's always, almost always someone out there with the same needs. Yeah, that's right.

**Chris Gammell:** I think you hit that on the head, Dave, because it's, you know, if you, I think a lot of the Arduino boards and the, you know, I saw that you have a power over Ethernet as well. Like that kind of stuff is like, you know, like someone wants that for hobbyist type things. You know, if you're going mass market, then you can't, you can't necessarily guess what everybody would like, but that's when you actually need to get into real market research. And who wants to do that anyway?

**Jonathan Oxer:** That's no fun.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** And that board was very specifically... Sorry? I was just going to say, the more you try and second guess what you think the market wants, the more compromised your product's going to be or the sillier it's going to get or you never finish it because of continuous feature creep or something like that, or you just misjudge the entire market. Yeah, so...

**Jonathan Oxer:** Sorry, it's better to iterate.

**Dave Jones:** You might as well do what you want and be done with it. And if it, you know, if other people like it, so be it. If they don't, well, move on to the next project.

**Jonathan Oxer:** And in fact, the Ether 10 was very specifically designed to go inside the light switches in my house. Like, that's how specific it was. Because I was thinking, I want to put an Arduino board behind the light switches. I need it to be networked and I don't want to have to run power to it. So I made a board that did that and it has all sorts of applications.

**Dave Jones:** Now, it's a fair thing to say that you're a bit obsessed with home automation.

**Jonathan Oxer:** Well, kind of. I would agree with that statement. Well, it probably looks like it. Let's start with the obvious thing here.

**Chris Gammell:** John, what is in your arm? Let's start with the craziest thing.

**Jonathan Oxer:** Yeah, okay. So...

**Dave Jones:** This may have started the rot, right?

**Jonathan Oxer:** Yeah, well, it didn't start it, but it was one of the major things. So I have an RFID microchip implanted in my left arm, just in my forearm.

**Dave Jones:** I told you the government's doing this shit.

**Jonathan Oxer:** Excuse me, I'll get my tinfoil hat. Yeah, right. And, well, funnily enough, that is actually... Yeah, well, that whole paranoia about government surveillance was actually part of what drove it. Because when I did it, it was around the time that Australian passports were being issued with RFID tags in them. And there was a whole lot of controversy. And you could go online and buy things like on eBay. You could buy a wallet that you put your passport into that shields it so that it couldn't be scanned remotely. And, you know, the tinfoil hat for your passport sort of thing.

**Dave Jones:** Yeah, yeah.

**Jonathan Oxer:** And there was all of this hype going on. For example, there were people saying, all this means is that terrorists will be able to walk into an airport and pick out the correct nationalities based on their passports. And then they can target the right people. You know, all sorts of stuff was being said. And being curious, I don't take stuff at face value. So I wanted to understand how this worked, both from a technical point of view and also from a social and privacy sort of point of view. And the best way to learn how stuff works is just to try it yourself. So I ended up... I contacted a company in Sydney, which is a distributor for implantable RFID equipment. They sell it to vets. And basically, I phoned up and said, I want to buy some implantable tags. And, you know, they're used to selling to vets. But I told them a bit of a story about what I needed it for. And the smallest number that would sell me is 10. Because they're used to selling in lots of, you know, 100 at a time or whatever. So they sent me down some pre-sterilized implanters with RFID chips in them. And I then... I did a whole lot of research, so...

**Dave Jones:** Stop at home on your couch going now. Get this thing in.

**Jonathan Oxer:** Not quite. It's on the outside now. I want it... Somewhere else. Part of the objective here was I wanted to know how hard it would be to do this going through the proper channels. So the first thing I did was I went to my doctor, my GP. And I just booked an appointment and walked in and said, I'm not sick, but you might think I am. But I am crazy. I am crazy. Yeah. And, well, I figured that... So I gave him the little spiel and said, you know, this is the RFID thing and this is what it does. And I want to go about... I want to have it implanted. At the time, I said, I want to have it implanted in my hand. How would I go about arranging to have that done? Oh. And I thought... I thought he was going to say I was insane and throw me out. He sat there sort of looking curious for a few seconds and said, that's a really interesting experiment. I'd like to see how this turns out. And it turned out he was really positive about it. So he then put me on to a couple of surgeons. One was a hand surgeon and the other was some... I'm not sure what their specialty was. And said, go and see these people and they might be able to help you out. My original concept... Excuse me. I've got a bit of a crunchy throat. My original concept was to put it in the webbing between my thumb and forefinger. The idea being that I could put something like an RFID reader in a door lock, in a door handle. So I walk up to the door, just grab the handle and the door unlocks. And this is part of the whole approach of trying to make technology invisible. And the idea that the physical world around you should simply accommodate what you want to do. You shouldn't have to think, I am going to unlock this door, for example, as a manual operation. It should just be unlocked for me but locked for everybody else. And so I went through this process with the surgeon and looked at possible implant sites and things. And we ended up deciding it would be better on the forearm. Because you have to consider things like strike injuries. If you get a hand crush or something, then you've got bits of shattered glass inside your hand. It's not good. So... Is that what the transmitter looks like? Yeah. Is it like actual... It's glass. It's actually a little glass tube. Yeah. If you imagine a large grain of rice, that's basically it. It's 12 millimeters long and 2.2 millimeters diameter. And it's glass with a coating on it called Paralene, which is slightly porous. So protein strands form in it and they lock it in place and stop it moving around inside your body. So... Oh, cool. Yeah. So one of the surgeons said, this is a great project. I want to do it. Let's set a time. So we scheduled it. And on the morning that the procedure was meant to be done, I got a phone call and he said, I'm really sorry. I can't proceed because I called my medical insurer, told them what I was going to do and they laughed at me. So... Bloody bureaucrat. Yeah. Yeah, right. So it turns out that medical insurance is based on the types of procedures that you do. So the risk of the procedures and they have a standard list. So when you apply for medical insurance as a doctor, you tick which procedures you do. And he tried to explain to them what it was and they said, there's no category that falls into. Forget it. Yeah.

**Dave Jones:** It's like insurance for certain types of sports. You know, if you do some obscure sport, you know, where you may kill yourself and you want to get life insurance, a lot of them just, if it's not on their list, they just throw up their hands and go, no.

**Chris Gammell:** They need to do it, right? They need to know just how much risk there is. Yeah.

**Jonathan Oxer:** Yeah. That's right. If the actuaries can't analyze it and come up with some stats on what's the likelihood of dying or injury or whatever, then... Yeah. Yeah.

**Chris Gammell:** Yeah. What's your sample size?

**Jonathan Oxer:** One? I'll be it. Yeah. Yeah. They don't like that so much. So the end result was that I did it myself. Oh, jeez. Get a large bottle of Jack Daniels? No. Actually, we were no painkillers or anything. So I talked to a number of people about the best way to do it. And obviously, infection is one of the things you've really got to care about. So I used proper sterilization techniques and things like that and implanted it. And basically, the implanter is like a big syringe. And when I say big, imagine like a house, like a roofing nail with the end cut off at an angle. Yeah. That's pretty much it. I'm pretty squeamish about this stuff.

**Chris Gammell:** So if I sign off and... No, no. No, don't do it for me. But we should warn listeners that if this is your kind of thing like me, if you hear a hurling sound in the background... Me, I am totally fascinated.

**Dave Jones:** Please continue. I am too.

**Jonathan Oxer:** And have you got video of it? I have photos. Yeah. The thing is that I did it without really telling anybody. My wife knew I was going to do it, but she didn't know that it was that particular time. So she sort of went out of the room and I thought, oh, here's my opportunity. So I grabbed the camera and went for it. But part of this was pride. Because the thing is that I had been scheduled to speak at a conference. And I'd been telling people that I was going to talk about RFID and implantable RFID. And I thought it would be really lame if I have to turn up and I haven't got it done yet. And it was all scheduled when the surgeon had agreed to do it. And when he pulled out, I thought, oh, I'm just going to look like an idiot if I turn up and I haven't done it. So I just gritted my teeth and went for it. Nothing like a little peer pressure, huh?

**Dave Jones:** Oh, brilliant. Wow.

**Chris Gammell:** And so they've been doing this since as well. I saw that, I think it was at 28C3 or some other conference, they were doing like voluntary injections as well. I remember seeing a talk with that girl that put magnets in her fingertips. I mean, there's like a whole movement here, right? It's just like, I don't want to see any of it, but it's very interesting.

**Jonathan Oxer:** Yeah, the magnets in the fingertips thing is really interesting. The whole idea of adding sensors to your body, being able to detect things. So in her particular case, she could detect magnetic fields. So I met her in New Zealand a few years ago at Foo Camp actually. And she said that what happens is because the magnet is implanted in her fingertip and it moves in relation to fields around it, that then stimulates the nerves in your fingertips. So you gain a tactile sense of magnetic fields. So you move your hand around and you can actually feel fields. That would be awesome. That is so cool. One of the light bulb moments for her was she said she was working on her computer and she noticed that she got a buzzing sensation in her fingertip when her computer suddenly started going a bit slower. And she had her hand just near the computer itself. And she eventually put two and two together and figured out that what she was detecting was when her computer went into swap and it was pounding the hard disk. And the field from the drive was enough to actually be detected in her finger. So she could detect swap being activated through her finger.

**Dave Jones:** This is real like a superhero kind of stuff.

**Chris Gammell:** This is great. I don't know if you've seen the video, but she talks just how painful it is. It's just, oh, yeah. I know. Because you've got so many nerve endings there in the first place. That's a crazy procedure.

**Jonathan Oxer:** Because if you think about where there are lots of nerves in the tips of your fingers, it's a very sensitive spot. And I think from memory, she didn't have any anesthetic when it was done. It was just done using ice. No, she said vodka. Oh, vodka and ice. She said vodka. I think, yeah.

**Chris Gammell:** Yeah. To hear her talk about it, that one really, I mean, like your stuff was, yeah. You're right. Hers was just really.

**Jonathan Oxer:** Yeah. But to get back to Dave's question about the whole home automation thing, it might seem like I'm a bit of a home automation nut. But it's more that the house is like a big toy. It's like it's something that you can modify and come up with new ideas for. So it's really just a playground or a test bed for all sorts of things. And I'm not really that obsessive about home automation as an end result. It's more a matter of I like playing with things and I want to see if I can control the lights from my phone or, you know, use a connect with gestures to open and close the curtains, you know, that sort of thing. And then it's a matter of figuring out the technological challenge of how to make that happen.

**Dave Jones:** So you don't really care about using it on a daily basis. You just more care about, oh, it works. You know, look, I'm able to do this.

**Jonathan Oxer:** Yeah. I do use it on a daily basis. I mean, our entire house now, every light in the house is controlled through the automation system. So we've got something like a kilometer of cable in the house. Wow. But it's interesting that it doesn't in some ways really change your day-to-day life. It's not like all of a sudden life is magically better. It's just more conveniences. So I can totally understand people being skeptical about home automation and just not seeing the benefit of it. It's a bit of an incremental thing. But if you like playing with technology, it's a fun thing to do.

**Dave Jones:** What about stuff like these, you know, the wireless light bulbs and, you know, stuff that you can control from your iPad? Well, you know, is that gone? Is that taking it too far? Like you end up spending more time playing with the thing than you do for, you know, like just switch it on and leave it on kind of thing. If every bulb in your house, you have to operate with your iPhone. I mean, how inconvenient would that be?

**Jonathan Oxer:** Yeah, that would be inconvenient if that was the only mechanism for controlling it. But one of the really interesting things about it is that what I've found is that it has the network effect where the more, you know, it's that old saying about the more items you have connected to your network, the more value that network has, which applies both for computer networks, but also for, you know, all sorts of other conceptual networks. So what I've found is that if you take, for example, a light in a room and you connect it to your home automation system so you can control it, and then you put a switch on the wall so that you can send a signal to your home automation system to control the light, what you have done is replicated the exact functionality you had before. There's, you walk up to the light switch and you flick the switch and the light comes on and off. But what you gain by doing more and more of those things is being able to recombine them. Because what you've done is abstracted the control, which is the light switch from the result, which is the light through the automation system. And you can do things like if the smoke alarm is triggered, then turn all the lights on automatically throughout the house and unlock the doors. If you've got your door locks connected. So it's not just a matter of, yeah, so the more things that you have wired into it.

**Dave Jones:** But what happened if the fire that caused that smoke detector has just knocked out your home automation system? Yeah. Or what happened if the fire started in your home automation system? In your home automation system. That's right.

**Jonathan Oxer:** Yeah, well, that's a possibility. Smash the window the old-fashioned way. Get out that way. Climb out, yeah. Yeah. Oh, boy. The interesting thing is that I've got things like the exhaust fans temperature of the water I had linked up and door locks and lights and heating and all sorts of things around the house connected. And the more things you connect in, the more value you get, just because you can do combinations of things that you haven't necessarily thought of before. So, yeah, it's just a big playground.

**Dave Jones:** I love it. And you're doing a series, right? You're doing a TV, a podcast series, a video series?

**Jonathan Oxer:** I'm actually surprised by how much interest that's got. Quite a few years ago, I registered the domain name superhouse.tv because I had the idea of doing a series about home automation. The idea was to do something like a high-tech twist on a typical home reno sort of show. So, not just – I really don't like the idea of these shows that are more like infomercials where it's like, oh, we bought this high-end commercial home automation system where we plugged it in and we paid an installer and this is what we've got. What I really wanted was this is how you get cable to go under a concrete footpath. And this is how you solve this problem or this is how things really work. So, a little while ago, I just started recording some videos explaining stuff as I'm going. And part of it is exploring as well because I've got a number of other episodes that I've mostly filmed but haven't yet put online. And some of it is starting off with I'm going to try to do this and I haven't actually done it before. And in fact, I don't even know how I'm going to do it. But let's give it a shot and we'll see if we can work it out. And by the end of the episode, there's something that's operational.

**Chris Gammell:** I like it. Okay, we need to take a quick break for a word from our sponsors, but we'll be right back. We'll get back to our interview of John Oxner in a second to hear more about his books and his kits and everything else that he's been working on. But in the meantime, we wanted to tell you about another kit maker, ClubJameCo.com. ClubJameCo actually will take your kit ideas, submit them to the community, and then the most voted on ideas will actually be produced by JameCo and sold and you get a cut of the profits. We've actually been doing this for a couple weeks now and we've featured a bunch of different types of kits. This week, we're featuring a kit that actually includes a power supply. So it's a transformer, a bunch of linear regulators, and some passives that allow you to control and filter that power supply. And then the PCB that comes along with it. It's nice because if you're starting out, you might not have a wide-ranging power supply at your house. You might just have batteries. So this is a nice way to not only learn, but also jump in and actually build your first power supply. The kit's less than $30. There's some great documentation. There's a video by Colin Cunningham of Make Magazine. And so you can go check it out now over at Club JameCo. If you go to clubjameco.com slash theamphour, you'll see all the kits we've featured. And you'll also be able to find out how to submit your own kit idea. Thanks for supporting the show. All right. And we're back with John Oxer of Freetronics and Superhouse TV and lots and lots of books. So tell us about these books.

**Jonathan Oxer:** Well, once again, I suppose it was a pride thing.

**Dave Jones:** Yeah, it sounded good so far. It sounded good.

**Jonathan Oxer:** Oh, do I have to? Oh, really?

**Dave Jones:** What an experience that was.

**Jonathan Oxer:** It's not that much fun, actually. Yeah, you'd prefer being on the internet these days.

**Dave Jones:** Tell us why the book publishing process is not fun.

**Jonathan Oxer:** It's not as glamorous or financially successful as you might think. And you might think that it's not very financially successful at all. And even then, you'd be overstating it. Right. So it's really not the sort of thing you do. If you figure out the number of hours, like if you actually sit down and thought, how many hours has it taken me to write this book? And then how much have I got back in royalties? You'd say, that was a waste of time. Yep. But it does open lots of doors. So I think that's been the biggest benefit. I would have to say that all of Freetronics came about as a direct result of writing Practical Arduino. And Practical Arduino was a huge effort over the space of many months and very little sleep for a relatively small financial return. I would have been better off spending that time doing consulting work or working on the business or whatever. So it only took you a couple of months to write that? Well, it took... That's incredibly short.

**Dave Jones:** The average books are at least a year. Yeah.

**Jonathan Oxer:** I think the...

**Dave Jones:** Especially these sorts of books rather than just like a novel or something like that.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. These ones that are technical books, they take a lot more effort.

**Jonathan Oxer:** Because you can't just sit down and start writing. The actual writing process for me comes reasonably quickly because I've spent a lot of time doing writing in the past. So for Practical Arduino, the vast majority of the time was spent in creating the projects. And... Yeah. Yeah. It's probably, I would guess, about 20% of the time we're sitting there writing out the words that explain how it all works.

**Dave Jones:** Yep. So not something you'd recommend to people unless they're really passionate about it?

**Jonathan Oxer:** I think it can be a great career move. And another book I did previously, which was Ubuntu Hacks, had a similar effect. Basically, it got me speaking spots at conferences and exposure and various things like that. It's a key to open a whole bunch of doors. But it doesn't make you a huge amount of money.

**Chris Gammell:** Yeah. Another podcast I listen to talks about books as like the biggest business card you'll ever hold. Yeah. That's exactly right. You hand it to someone, here's what I did.

**Dave Jones:** So do you think a book is even better than doing your online blog or becoming famous doing blogging or something like that? You still think it holds more currency in the...

**Jonathan Oxer:** I think it holds more credibility in the real world.

**Dave Jones:** Credibility. All right.

**Jonathan Oxer:** I think part of it is the idea that to some extent there is still this gatekeeper function and the idea that if you've convinced a publisher to publish your book, then it must have some value. Whereas anyone can get online and publish stuff on the internet. Publish crap on the internet. That's right. No one knows you're a dog. Some weirdos on there. Yeah.

**Dave Jones:** We're all raising our hand here. Yeah, right. We're all just publishing crap on the internet.

**Jonathan Oxer:** But there's also obviously self-publishing, which I've done for a couple of books. And vanity publishing, which is where you just pay a publishing company to print however many copies you want and no questions asked. So I think there is still this perception that if you've had a book published, that has some value. Yeah.

**Dave Jones:** Right. I should get onto it then. I think you've got a big enough audience already.

**Jonathan Oxer:** You're doing pretty well, Dave.

**Dave Jones:** Right. Well, I've already written a book, but I self-published. So yeah. Yeah. Well, I've been offered a deal to write a couple of books for a major publisher. But it's like, well, where do I find the time?

**Jonathan Oxer:** Yeah. It is a big time sink.

**Dave Jones:** And as you said, I know there won't be the financial reward for the hours put in. I just know it. I've gone through the math and I know how many it will sell roughly. And even if I double that number, it's still not going to make, you know, I'm still not going to make a return on those hours put in. Yeah.

**Jonathan Oxer:** That's right.

**Dave Jones:** So you've got to do it for the love of it.

**Jonathan Oxer:** Yeah.

**Dave Jones:** Or for the selfish gain. Selfish gain that it might give you. Which is fine if you want to do that.

**Jonathan Oxer:** Yeah.

**Chris Gammell:** Well, it's interesting because the practical Arduino, that was through a rail?

**Jonathan Oxer:** That was done through A-Press, which is distributed by O'Reilly, I believe.

**Chris Gammell:** Oh, okay. Yeah, Ubuntu Hacks was done through O'Reilly. Yeah. That's cool. Yeah, I mean, because that's a name a lot of people recognize and stuff too. So that always helps as well.

**Jonathan Oxer:** And that actually did really well. Ubuntu Hacks was one of the earlier books that was distribution specific. And from what I was told, the thing is that you don't really have access to a lot of numbers. So you can see what reports you're getting in your own royalty statements and things, but you don't really know relatively how well you're doing, other than looking at Amazon rankings and things like that. But what I was told through people within O'Reilly was that Ubuntu Hacks was one of the biggest selling Linux books of all time. So it did really well. And it still didn't make you rich and famous. That's the thing is that you have to be within that top fraction. What made you famous? Well, you have to be in that top fraction of a percent to really make serious money out of books.

**Dave Jones:** Yeah, you poor 5% of you. Top 5% is not going to do it for you. You've got to be 0.5%. Right. Right. Yeah, it's a bit of a mugs game, as they say, here in Australia. Yep.

**Chris Gammell:** Ah, boy. So you've also hacked a car before? Is that right? So I was looking through your Superhouse TV YouTube account, right? I'm like, holy crap. John's got tons of views. And then I'm like, wow, this one video has 700,000 views. Yeah, that's right. So what did you do here? What did it take to get this done?

**Jonathan Oxer:** I have had an interest in cars for a long time. In fact, back around when I was at uni and then just shortly afterwards, I had a small business for a while doing automotive electronics and ended up mounting computers in cars and did things like that. So what I did a few years ago was take my car and mount a very small, low-power computer, which is based on a router board, basically, in the boot with a 3G internet connection and then wired it up to a number of things. I had GPS and connected it into the ignition system. So I actually got an Arduino and wired it into the ignition system of the car and connected that back to the computer. And the idea being that the car itself would be alive and online 24-7. So I could pull it up from anything with a browser. And because the car is on 3G, it doesn't matter where it is. And it would report its position on Google Maps and log data. So it was also connected through OBD2 into the engine management system. And through the ignition system, I could start and stop it by remote control and lock it, unlock it, all of that sort of thing. And so what I could do basically from anywhere in the world, although I think the furthest I ever did it from was a few hundred kilometers away, just to prove the point, was use a smartphone or a browser. I could log into the car, see where it is, start the engine by remote control, and then watch the data coming back from the engine management system and then turn the car off again. Wow. So it was basically an experiment in how to take a car and put it online.

**Chris Gammell:** And now that is like a standard feature in a lot of cars too. I mean, I've seen that in commercials and stuff of, oh, iPhone control. But that's more specific. Yours was very, you know, you could have generalized this to any car versus a lot of the ones that are manufacturer specific.

**Jonathan Oxer:** Yeah, that are built into the main. Yeah, that's right. And I had a whole lot of people say, why the hell would you want to do that? What's the use? Once again, part of it was just because I could. Yeah, exactly. But there are some interesting things that came out of it. One of the hypothetical uses for this is imagine you have some kind of a fault with your car or your car might be due for servicing. What your mechanic could do is log into your car by remote control while sitting in your driveway, start it up, interrogate the engine management system, pull out any fault codes or whatever, and then turn it off again. So, you haven't had to book to take your car in and drop it off and then take a bus to work or whatever you have to do. Your mechanic could actually be doing things on your car sitting in their office. So, that's one possible thing. Yeah, hopefully it's not in the garage at the time. Yeah, carbon and oxide poisoning. Yeah, Graham was hanging out in the garage and I'm feeling a bit woozy. I just killed someone with my smartphone. Yeah, right. Well, that's actually one of the interesting things that you have to be really careful about this stuff. I mean, I've got a bit of a reputation over the years and all of the conference presentations and things I do because I often talk to software people and I'm showing hardware. I start off with disclaimers about, you know, don't burn yourself and don't electrocute yourself and, you know, these sorts of things can kill you. And so, the thing with mucking around with car electronics is that you don't necessarily just kill yourself. Or if you're going to kill other people around you if you get it wrong. So, yeah. And when I started looking into the wiring on my car, I got the wiring diagram for it. And this is just the limited wiring diagram. It's not even, you know, the schematics and things. It's just the interconnection of the black boxes. I think it was something like 60 pages of wiring. And so, one of the first things I wanted to mess around with was the hi-fi system, like the head unit, because I wanted to inject audio into it from the computer so that the computer could announce things through the sound system. So, I started looking at the wiring diagram. Would you like me to use Turbo Boost? Yes, please. In my best kit voice. Just sweet. And so, I was looking at this wiring diagram, and I had this big block for the head unit for the sound system, and these connections going off to various places. And one of the connections coming off from it had a connection to the anti-lock braking system. And that's a bit of an eye-opening moment. You think, should I be messing around with a stereo if it can affect the anti-lock brakes?

**Dave Jones:** Yeah.

**Jonathan Oxer:** Now, in that particular case, it was simply because the stereo unit was being used as a status display for whether the brakes were engaged or not. Ah, right. Okay. But still, it just shows some of the issues you have to deal with. You can't just start messing around with these things.

**Chris Gammell:** Yeah, but if you've got like a Bond car, you flip the wrong bit and you start firing rockets, right? Yeah, you launch a missile. Yeah. Yeah. There goes your kindly old missile. It helps you with your lawn, you know?

**Jonathan Oxer:** It turned out that there were quite a few people interested in that. So I set up another site a few years ago called geekmyride.org, and a number of people submitted their project cars and things they'd hacked on them. So that project hasn't really gone anywhere very much, but it was a fun thing to do. But Chris, you mentioned the Bond car and, you know, firing rockets or whatever. One of the other things I've just been involved in recently is ArduSat. Have you heard of that project?

**Dave Jones:** Yeah, the satellite, yep.

**Jonathan Oxer:** Yeah. Yeah. So I've just been working on some payload design for ArduSat. Oh, nice. For listeners who don't know what it is, ArduSat is a CubeSat project. CubeSats are very small satellites. They're 10 centimeters on a side. They're under a kilo in mass. And they basically piggyback along as a secondary payload on some other launch. So if some commercial launch is going up with a communications satellite or whatever, because of the way – because lift vehicles are designed to have certain capacities and satellites are designed to be small and light, often there is excess payload space. So what happens is that CubeSats are packed in extra space around whatever the main payload is and taken up into orbit. And they're used by researchers and uni students and that sort of thing to get experiments up into space. Because the thing is that even getting a CubeSat into space is an expensive exercise. The launch itself might be $35,000 to $50,000. And the platform itself, you might be up for between – it varies depending on what you're doing. But it might be $10,000 or it might be $50,000 or $100,000 worth of hardware that you are sending up into low-Earth orbit.

**Dave Jones:** Why does the hardware cost that much?

**Jonathan Oxer:** Is it all rad-harding and stuff? No. Very little of it is. It's actually surprising how little rad-harding is used in satellites, particularly in low-Earth orbit. And there are a lot of parts to it that are really expensive. So the actual launch itself, you're paying basically to get your mass into orbit. It doesn't matter what the mass is. But the parts themselves, I think partly because it's very specialized, it just tends to push prices up. So if you have an idea for some kind of an experiment that you want to get into orbit, even as a CubeSat, which is incredibly cheap and easy to do compared to a typical commercial launch, you're still looking at maybe a $50,000 to $100,000 project. And that's a lot of dollars. Yeah. Like at a hobbyist level, that's just way out there. That's the hell of a Kickstarter. Yeah, that's right. So the idea with iGESAT is to create a platform that allows multiple people to run their own experiments on it. And it's really a matter of breaking down that cost even more and making it easy for people to get access to it. And the objective of the iGESAT project basically is to give people a week of processor or experiment time on an orbital platform for in the region of $250 to $300. So it makes it really accessible. And the way that's being done is that iGESAT itself is designed with a whole bunch of sensors on it. It has about 20 sensors. You know, things like temperature and ambient light sensor, Geiger counter and various other things. A whole lot of optical stuff, like there's a spectrometer. And then a whole lot of processor nodes. And the idea is that all of the processor nodes can access the sensors in parallel. And you can run a whole lot of experiments at the same time. So the idea is that if, for example, you're a high school physics class and you want to do an experiment, you can prototype the experiment on really cheap hardware. Basically, you just need an Arduino and a few bits and pieces. You can prototype it in your classroom, send your software across to the iGESAT team. They upload it to the satellite. It runs on one of the processor nodes in the satellite. And then the results are sent back to you. Nice. So it gives people a real hands-on, I suppose, in a way, access to doing things that in the past is like $100,000 entry point. So that's been a really interesting project.

**Chris Gammell:** How did you get started with that? How did you get started with all this crap? I don't know. You do some cool stuff, man.

**Jonathan Oxer:** Thanks. I basically said, hey, I want to help. So iGESAT was a project that began a little while ago. It was started by a group who funded it through Kickstarter. And their goal was, I think their objective was a $35,000 threshold, which would have covered some hardware costs. And basically, it would have been enough to do a minimal project. And they ended up getting something like $120,000 or $113,000 of funding. So way beyond what needed. And they've now gone for venture capital funding as well. So they've got some reasonable money behind them. And it was one of those standout Kickstarter projects. And I just looked at it and thought, this is awesome. I want to get involved with this. So I got in touch with them and said, hey, can I help you design your payload? And they said, yeah, that'd be great. In fact, this is a tie-in to what we were talking about earlier. I talked to their payload specialist. And they said, yeah, we have your book here. We use it as a bit of a reference Bible. That's awesome. So that's exactly where this sort of thing pays off. Yes.

**Dave Jones:** Well, speaking of Kickstarter projects, although this isn't relevant to you, really, John, I think we probably all should talk about it. It's pretty hot news at the moment. We don't normally get guests to talk about this stuff. But I'm sure you have an opinion on it. So we'll go for it. Did you hear that 3D Systems are suing Kickstarter and Formlabs for their new 3D printer?

**Jonathan Oxer:** I saw that there was a lawsuit, but I don't know any details about it. Right. I just saw all these people on Twitter saying, oh, 3D Labs is suing. But I don't know the details.

**Dave Jones:** Well, there you go. Yeah. They're claiming, you know, patent. It's a patent lawsuit that they've got, you know, the patent on this stereo lithography technique, which Formlabs are using as well. And they're not only suing Formlabs, but they're suing Kickstarter. That's crazy. As well, because Kickstarter are aiding and abetting, you know, effectively. You know, they're their sales channel, effectively.

**Jonathan Oxer:** I've just got to say, I hate patents. Yeah. Yeah. Join the club. Yeah. They're such a stifler of innovation, which is the exact opposite of what they were meant to be.

**Dave Jones:** Yes, exactly. There are some, I've got to admit, there are still some good uses for them. But in general, yeah, they're just, no, the whole system is just a joke now. Yeah. And, you know, it's just crazy. And now a 3D system's name is Mud, pretty much, you know, because you've got every geek on the planet.

**Jonathan Oxer:** Yeah. How to get people offside.

**Dave Jones:** Yeah, exactly. And anyway, it'll be interesting to watch. So you're of the opinion also that patents are just a waste of time, money, and effort. Because you're a big advocate of open source, of course. Yes, that's right. Free and open source.

**Jonathan Oxer:** Open hardware, open software. Yeah, definitely. I think that's really the platform that we need for innovation. If you can't see what other people are doing, you're going to reinvent the wheel. Well, if you can see what they've done and you're not allowed to do the same, then you can't build on it. It's all just a losing game.

**Dave Jones:** Yep. So what is the best license, in your opinion, for 3D, for hardware, for open source hardware? Have you got a favorite? Yeah. Or do you prefer not to do anything at all, just public domain the whole thing and be done with it?

**Jonathan Oxer:** Well, for the vast majority of the designs I've released, I've done under the Tapper open hardware license. Right. That was – and there is now the CERN open hardware license, which is very similar. They take quite similar approaches. The Tapper open hardware license was written by – well, it was – they were advised by Bidel Garby, who is a guy I know quite well through Linux Australia and Linux Conf, who I have a lot of respect for. And when I was first wanting to publish designs, I was looking around at what's appropriate, looking at things like Creative Commons licenses, which are really not appropriate for hardware. The thing is that licensing hardware is a complex problem. You can't just really cover it by copyright and there are patent issues and all sorts of other things.

**Dave Jones:** Is that a reason why – you know, a lot of people just throw up their hands and go, oh, I'm just going to public domain it. I'm not going to bother with the license and be done with it.

**Jonathan Oxer:** Yeah, I think it might be. Yeah, I think it's often just too hard. And so what we've ended up with for open source software is a couple of different philosophies and approaches, things like the GPL versus the BSD. And most people couldn't care less. They just want the software. But for people that really care about it, there are very big differences between, say, the BSD license approach versus the GPL approach. They come from very different perspectives. And there are similar things in hardware. So my preference is just the TAPA open hardware license. Right. I don't have – the CERN license would do just as well, I think.

**Dave Jones:** And do you think they're still complete licenses? Do you think they embody the ethos of the open source hardware movement enough? Like I've done a video on sort of like, you know, in quote marks, the unwritten rules of open source hardware. What's your opinion on that? I mean, take, for example, the MakerBot clone, the Tangibot. Did you agree with, you know, the Tangibot thing, project, which I assume you've heard of? Oh, yeah. Which was like just an absolute direct clone of the MakerBot with not improving anything, not value adding, just making it cheaper in China. What's your view? Okay.

**Jonathan Oxer:** My view on that is probably not quite the same as yours. But I remember you talking about this on a previous episode and saying that they were adding – he was adding no value. I think you're right in saying that he's not adding any value to the design. But I think in terms of making it accessible at a lower price point, that is adding value. Or price or achieving the economy of scale.

**Dave Jones:** I don't disagree. I just think it's not adding sufficient value. I think he should have done at least a few token things. Yeah. I certainly understand why he caught the flack.

**Jonathan Oxer:** Yeah. Right. But simply doing a carbon copy of someone else's design and saying, I'm going to take all of your hard work and undercut you and take over your market. I mean, there are obvious ethical issues with that quite apart from – Well, that's what he did effectively. Yeah. That's right.

**Dave Jones:** Well, that's what he tried to do. Yeah.

**Jonathan Oxer:** If someone has access to manufacturing capability and they're able to produce something at a lower price, I think the ethical thing to do in that case would be to talk to the original designer and say, you know, we'd like to give you a percentage or come to some arrangement over it. Not just say, well, we're going to take this and ride off into the sunset and make lots of money. Yeah. But that said, that is actually what the principles of open source allow. It's designed to allow, yes. Exactly.

**Chris Gammell:** Well, I think the other thing there too was the fact that he was getting all that money up front though and he was just kind of brash about it. I think there was a lot more facets to it.

**Dave Jones:** He rubbed people the wrong way. Yeah. I agree with you, John, on a lot of these points really.

**Chris Gammell:** Yeah. It was an attitude thing. Right. And we talked about it when we first discussed it was that innovation does come in process, right? There is a legitimate value to that because that's how societies move forward. That's how we get more efficiencies and get cheaper electronics, right? I mean, look at the price of electronics over time. It's just ridiculous. If we didn't have the process innovation, we'd still have Z80s, right? Maybe not even that. Yeah. Yeah.

**Dave Jones:** So our views are still very similar there because that's essentially what I said in my unwritten rules was that, yeah, it would have been nicer if you approach, you know, don't just ignore the original design or if you've got, you know, actually talk to them, you know, and either offer them a small cut because without them you wouldn't exist, right? Your business wouldn't exist or whatever or, you know, or offer to manufacture it for them or, you know? Yes.

**Jonathan Oxer:** Yes. That's right.

**Dave Jones:** Do something like that. So, yeah, rather than just ignore, you know, totally ignore the original designer and just go, right, I'm going to wipe you off the mat, you know?

**Jonathan Oxer:** And I think that largely comes down to the whole community aspect as well because the idea is that people that are involved in open source, either hardware or software, are not all working in isolation. The whole point is that we all build on each other's designs and ideas. Exactly. And collaborate. So you really have to respect what other people have done.

**Dave Jones:** Exactly. So there are unwritten rules there which you really can't cover in a hardware license because all those hardware licenses say you're legally allowed to do all this. End of story.

**Jonathan Oxer:** Yes. That's true.

**Dave Jones:** If you publish your thing under this license, you have no right at all to complain if somebody ruthlessly undercuts you and ignores you and puts you out of business. Yep.

**Jonathan Oxer:** But on the other hand...

**Dave Jones:** Even though it's against the, you know, it's against the community, sort of, you know, that's not how the community works. So there's two sort of, you know, levels that there that the community's working on sort of a different philosophy to what the open source hardware license is, so to speak.

**Jonathan Oxer:** Yes. And you see that with things like the non-commercial option on the Creative Commons license. Ah, yes. So I see any license that has a non-commercial flag on it as being non-open because it's restricted what people can do with the end result. Yes, of course. But once that ties into this unwritten rule that you shouldn't just take someone else's work and build on it and not give them any credit, not interoperate with them in any way.

**Dave Jones:** There are some instances where you can do that. Like, if they've obviously, like, you know, they designed this thing, they just put it out there and they've totally abandoned it and they're not interested in it anymore and that kind of stuff, then, you know, there can be, you know, that can be fine. Yeah.

**Jonathan Oxer:** Or even in a more extreme case, part of the point of open source as well is to avoid vendor lock-in. And vendor lock-in can be just as much from an individual as from a big corporation. So if you have, imagine you have an open project which has a non-commercial license on it and it was developed solely by one person and that person's hit by a bus, all of a sudden everybody that relies on this doesn't have any development resources available and they can't develop it commercially. So you can't then hire someone else to work on it and sell it. So there are, I think we need to err on the side of the minimum restrictions possible, which I think most of the current open hardware licenses do, which is good. Once you start adding those restrictions, it might look like you're putting in place restrictions in order to protect your freedoms or protect the philosophy of open source. But in fact, in many ways, it works against it.

**Speaker ?:** Yep.

**Dave Jones:** So it's probably impossible to write some of these more community philosophical things into a legal license, right? It just, it's probably never going to happen.

**Jonathan Oxer:** Yeah, yeah, I think you're right.

**Speaker ?:** Is it really?

**Dave Jones:** Because, you know, the legal world and the real world of, you know, people being friendly to each other and all that and the community aspect are just two totally worlds which will not ever 100% agree, I suspect. Yeah.

**Jonathan Oxer:** Well, the world's a messy place and we can't have perfect definitions, unfortunately. So we've just got to live with it the way it is.

**Chris Gammell:** Oh, boy. John, you've been doing open source projects for a long time. I mean, I think you said you've been doing Linux since, what was it, 2000, early 2000s kind of stuff?

**Jonathan Oxer:** Yeah. Yeah. In fact, even a little bit before that. Yeah. Okay.

**Chris Gammell:** What would be some advice you'd have for, like, for younger engineers or hobbyists or anything like that to actually get jumping into those kind of things? I mean, what, how did you, how did you first get into the Linux side of things like actually developing and then, you know, like, how do you actually jump in and contribute?

**Jonathan Oxer:** I think the most important thing is to consider the community. And a lot of people overlook this. They think of open source as a technology and it's really not. It's a, it's much more complex than that. It's an ecosystem. So my advice is to do things like go to open source conferences and go and meet up with people. I think one of the most eye-opening things for me was the very first time I attended Linux Conf, which was in Brisbane in 2002. I think it was the first time I went to that particular conference. And at the time, I was doing some work on a file server which had a web-based management interface. So I was doing stuff using Samba, which is, you know, the Linux-based file server for Windows compatibility and PHP. And I went along to this conference and was talking to various people. And there were a couple of guys standing in the, outside one of these rooms. And it sounded like they were having an interesting conversation. One of them was talking about PHP. And so I just walked over and stood nearby and started listening and sort of edged myself into the conversation. And I had no idea who these guys were. And they were talking about, one of them was talking about a file server and using PHP for the management interface on it. And the other one was, you know, explaining some stuff about PHP. And after I'd been talking to them for a little bit, I looked at their name tags and I realized that one of them was Andrew Tridgell, who's the author of Samba. And the other was Rasmus Lerdorf, who's the inventor of PHP. And let me tell you something else, buddy. And so you just slinked out of there, weren't you? No, no, no. Oh, I don't know as much as I thought. Well, the thing is that these people are really accessible. And, you know, I've met both these guys many times at conferences and things. Like I see Tridge quite frequently. And he's a great guy who's really into, he's getting into open hardware now as well. And the point is that they're accessible. It's not as if the, you know, these products come from some faceless corporation that you can never find the names of the people who actually wrote it. You can actually go up there and shake hands with the person who wrote whatever it is, piece of software that you're using. Or, you know, in the case of larger projects, there are many contributors. But you can definitely engage with people directly. And I think that's probably the most important thing is not just to sit in a dark room on a computer and get out there, go to conferences, go to user groups and hackerspaces and things like that. And you'll find that there is such a vibrant community and people are so welcoming and willing to help out. I think that's probably the most important thing.

**Chris Gammell:** Yeah, I know. I felt that, I mean, when I went to that open source hardware conference that first year, that was, it was just tons of fun, you know. Not only just the getting to know people like that, but just the putting personas to faces as well. It's weird, but it's really cool. I enjoy that side of it.

**Jonathan Oxer:** Yeah. Yeah. And I think that goes counter to a lot of geeks' natural tendencies. I mean, I'm naturally a shy person. So, I have to overcome that to some extent. Like, if you put me in a party, I'll be the person sitting in the corner being quiet and, you know, not interacting with anyone. Right.

**Chris Gammell:** But at conferences, there's only so many corners, right? So, that's the best part. Yeah, that's right. Put everybody around very well populated.

**Dave Jones:** Well, actually, at these conferences, no one's in the center, right? There's just all the pockets of great geeks in the corner, right? Yeah, but they're chatting with each other, right?

**Jonathan Oxer:** That's the thing is that they're talking about really interesting stuff. It's like you go to a party and people are talking about things that I couldn't care less about. But, you know, you go to a tech conference and people are talking about really amazing stuff with 3D printing or electronics or software or whatever. And it's really easy to get into in-depth conversations.

**Dave Jones:** Yep. Do you find it's getting a bit of a hindrance for all this stuff that you're in being based here in the backwater that is Australia in terms of the technology industry?

**Jonathan Oxer:** It does often feel that way. To some extent, it's not because we do have this whole I can work from anywhere sort of… This whole internet thing, right? Yeah, that's right. This thing called the internet. It's kind of handy. It's wonderful new technology. Yeah. Never heard of it. It does mean that I can't turn up easily to the open source hardware summit and, you know, those sorts of things. And I've been over and I've done talks at places like AusCon, which is usually in Portland each year. But for me, I mean, Dave, you know the pain. It's, you know, 20 hours on planes and things to get anywhere.

**Dave Jones:** And if you have a family, it's doubly bad.

**Chris Gammell:** You should charter a cruise boat and have like a hacker cruise come across. You guys could like work on projects on the way over.

**Dave Jones:** That'll take about two weeks. Yeah, it probably would. That'd be awesome.

**Chris Gammell:** It would be awesome, right?

**Dave Jones:** I know. That'd be the best part of the experience.

**Chris Gammell:** You just, you know, you hit the shores of the U.S. and then you turn right back around. Yeah, you turn right back around. You just leave again. I haven't got any time to see it. Yeah, the journey is the destination, right? That's right. Right. You could be on to something.

**Dave Jones:** What can we do in Australia to get more stuff happening here in terms of that community thing? Is there just not a big enough community here? No, I think there is a big enough community.

**Jonathan Oxer:** I think that...

**Dave Jones:** But are they too sparsely... Are they too dispersed between cities? Because we've got a couple of major cities here where sort of most of the... That problem happens everywhere, though, Dave. I mean, like, I live in the middle... Yeah, true.

**Chris Gammell:** I live in the burbs of Cleveland, right? There's no one around me. I mean, like, it's... Yeah. That same problem happens everywhere, I think. It's the living online helps and, you know...

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. And then taking the time to...

**Jonathan Oxer:** Well, they're just in Melbourne, for example.

**Dave Jones:** Do we need more big conferences here? Do we need more big sort of, you know, make affairs or something?

**Jonathan Oxer:** Yeah, I think we need more of that sort of thing. And Paul Shimkoviak, a friend of mine that organised the last mini make affair in Melbourne that had something like a thousand people turn up to it, is really keen to do more of those. I think he has more... At least he wants to do a major one next year, I think. Awesome. Probably in Melbourne again. And I think hackerspaces are a major part of it. I just love the hackerspace movement, the fact that people can get together and build cool things. And the fact that you can turn up to a hackerspace not knowing what you're going to find. Every time I go along to connect to Community Hackerspace in Melbourne, there's someone with some other project that I've never heard of before. But it's just really fascinating to see what they're doing.

**Dave Jones:** Yep. Yeah, we just... I know. It's... Every time I hear about all these conferences overseas and everything, it's just... Oh, sorry. I'd love to go to that. Oh. Ah. But we only have a limited population here. Yes. I mean, we've got a country of 20 million, as you know, whereas... Yeah. You know, they've got like 20 million in a city over there.

**Jonathan Oxer:** Yeah, that's right. No.

**Dave Jones:** There's a big difference. That's China. Sorry, just a whinge about Australia again. But we do live in the best country in the world, don't we, John? We do. Absolutely.

**Jonathan Oxer:** I wouldn't trade it.

**Dave Jones:** Exactly. No, no, no, no, no. Sorry, Chris.

**Jonathan Oxer:** It's okay.

**Dave Jones:** And is that all we've got time for this week? I think we're way over. Oh, yeah. As we normally do with guests.

**Jonathan Oxer:** That seems like it was about five minutes.

**Chris Gammell:** Yeah.

**Jonathan Oxer:** That's how it usually goes. Always does.

**Chris Gammell:** Yeah. Yeah. Time flies. I would personally highly recommend people check out John's YouTube channel. He does a great walk around. What is it called? A walkabout? Oh, yeah. Walk time blog. It's a walk time rant. Same as mine. Yeah. Walk time blog. It's a lot of fun. Except I commented on your last one.

**Dave Jones:** You weren't walking. I haven't been walking that much recently.

**Jonathan Oxer:** In fact, the first... You get a treadmill or something.

**Dave Jones:** You just stood there. It's called a walk time rant. You just stood there with the trees behind you.

**Jonathan Oxer:** The funny thing is that that blog series started as a response to the Amp Hour. It's because you guys were talking about something and I thought, I want to talk back. There was no mechanism to do it. You were so frustrated. Yeah. Damn. I just like my media.

**Dave Jones:** Yeah. That's good. That's awesome. Push technology. Yes.

**Chris Gammell:** And we encourage other people to do that as well. They can do great stuff like John's done. So, people should also visit John's site. It was at john.oxer.com.au. Yeah. A-U. Yeah. That's awesome. And you can find all those other sites there. J-O-N. Yeah. Well, yeah.

**Dave Jones:** Why did you get john.oxer and not johnoxer one word? Because you thought oxer was just a cooler full-letter domain name? Yeah.

**Jonathan Oxer:** And also just for email. So, I've got email set up for everybody in my family. So, my email address is just john.oxer.com.au. Yeah.

**Dave Jones:** Oxer.com.au.

**Dave Jones:** It makes sense. Fair call.

**Jonathan Oxer:** And there are some total of about seven Oxers in Australia. Right. There you go.

**Dave Jones:** And admit it. You're a domain junkie like me. Yeah. Every idea you come up with, you just instantly buy the domain name. Exactly.

**Jonathan Oxer:** Exactly. In fact…

**Dave Jones:** And if you can't get the domain name, that name's not good enough, right?

**Jonathan Oxer:** That's right. The funny thing is a long time ago, I actually bought the domain name fiberoptics.com. And I've been sitting on it ever since. I still have not… It must be like 12 years since I registered it. And I still have not thought of a use for it. So…

**Dave Jones:** Hasn't somebody given you an offer on that?

**Jonathan Oxer:** No, no. So, I think… Really? I think if you go to fiberoptics.com now, it just goes to my blog or something. But, yeah, I've got a bunch of domain names. It's a sickness, folks. Yeah, it is.

**Chris Gammell:** Collecting.

**Dave Jones:** Oh, boy. Well, thank you very much, John. Thanks, Dave. Thanks, Chris. It's been awesome.

**Chris Gammell:** Yeah, it was good talking to you, man. Oh, you can also find John on Twitter at Freetronics. Freetronics. He's a… Yeah, she tweets. What else?

**Jonathan Oxer:** Superhouse TV. Yeah, my personal Twitter account is just John Oxer. J-O-N-O-X-E-R. Right.

**Chris Gammell:** All right, cool. All right, well, we'll see you on Twitter and we'll see you around the web with all your awesome stuff. Great.

**Dave Jones:** Thanks, guys. Thanks, mate. See ya.

**Chris Gammell:** See ya. This episode of The Amp Hour was sponsored by Club Jameco, who allows you to upload your kit idea and make up to 10% of the sale price without ever needing to buy or bag components. Go to clubjameco.com slash The Amp Hour to see the kit discussed on this week's show and to support the show.

**Speaker ?:** Bye.
