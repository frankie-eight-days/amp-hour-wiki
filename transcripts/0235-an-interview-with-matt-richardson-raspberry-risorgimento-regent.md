---
episode: 235
title: An Interview with Matt Richardson - Raspberry Risorgimento Regent
url: https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded February 3rd, 2015. Episode 235. With guest Matt Richardson. Raspberry Resorgimento Regent.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Matt Richardson from Raspberry Pi.

**Dave Jones:** Hey, Matt.

**Chris Gammell:** Welcome, Matt.

**Dave Jones:** Thanks for joining us.

**Arduino:** Thanks for having me. It's great to be on.

**Chris Gammell:** And we, I think a lot of our listeners will also know Matt from his wide experience in the past of writing books and writing for make and just kind of being everywhere on the internet. I mean, you're kind of like internet project dude as well. So it's good to finally have you on and see all your stuff kind of rolling into a single project now. It's awesome.

**Arduino:** Yeah, yeah, absolutely. It's exciting. I've been kind of a Raspberry Pi fanboy for a long time. And I was kind of like all over the place. I was doing projects for all kinds of people, doing them for make for other people and kept turning back to the Raspberry Pi. And then, you know, eventually I was like, well, why don't I become an official fanboy for Raspberry Pi?

**Chris Gammell:** So how does that work? So you're working for the foundation. So like it's a foundation, correct? I mean, kind of run us all through this in case there's someone out there who hasn't heard of it somehow.

**Arduino:** Yeah. So yeah, Raspberry Pi is a nonprofit foundation with the mission of advancing computer science education. And we do that by selling a $35 computer, credit card size computer. And it's for, you know, learning how to code. It's for hacking. And yeah, it's, you know, it's only been a month now. It started at the beginning of January. So I've only had a month on duty. And I know a lot about Raspberry Pi from using it. But yeah, I'm still kind of getting the hang of what goes on on the inside.

**Dave Jones:** How many people are working there? Would you know? I'm just curious.

**Arduino:** I want to guess around 15 people full time. Okay. That's fewer than I would have guessed. Yeah. Yeah. It's not, it's a, it's a quite a lean operation. Yeah.

**Chris Gammell:** Right. And then, I mean, there's also, we've, and we've talked in the past before about the, some of the manufacturing that's done. I think the CMs are used for the manufacturing, stuff like that. So that kind of helps expand the empire, of course.

**Dave Jones:** But that's probably all the people you would need. I wouldn't have expected more than that. That's probably double what I would expect. Because you need, okay, somebody, a couple of people to work on the hardware, maybe some, a couple of people to work on the manufacturing side of things, you know, keep that on track. And then you need a couple of people as media or media person. And then you need some program, a handful of programmers. So, you know, that kind of adds up.

**Arduino:** Yeah. You, you have it kind of nailed down there. We also have a very large education department that they're helping to build educational resources and have classes for teachers to learn how to use Raspberry Pi and just any, any kind of educational outreach. There's a lot of that going on.

**Chris Gammell:** Yeah. And that's kind of the interesting thing to me is that, see, the reason I thought more would be because just scale, right? I mean, so obviously it's, it's happened quickly, but, you know, there's, we keep seeing news about what, two, two or 3 million or 4 million sold now. I mean, basically.

**Arduino:** Yeah, I think we're around 5, 4.5 million right now. 4.5 million. I mean, so, yeah.

**Chris Gammell:** I mean, we had Eben, I recorded with Eben at Maker Faire. Two or three years ago. And I think that was like 1 million at that point. And so, I mean, just growth rate, that kind of, I always figure that that takes a lot of people for that kind of thing. But, but that's, that's great that it's, it is staying lean like that. You know, that's, that's important for doing cool things.

**Dave Jones:** What's your take on the concept of orphaned Raspberry Pis for want of a better term? Because there's, I think we've talked about it before on here, Chris, Chris, and it's talked about on the forum a lot and stuff like that, about people who rushed out and bought one because they're all the fat and they're cool. And it's like 35 bucks. It's like, oh, how can I not buy one? You know, I'm just going to click, you know, I'm just going to buy it now. Because it's such a compelling price. And then it sort of sits around unused and they go, oh, okay. Yeah. What do I actually do with it? There seem to be, in my experience anyway, there seems to be a lot of abandon.

**Chris Gammell:** I figured that happened with my Beagle Bone Black as well. I mean, that happens all my, I have a pile of boards.

**Dave Jones:** And you can say it's similar to any flavor of Arduino or anything like that as well. You know, people just get them to see, you know, flavor of the month.

**Arduino:** There's no expiration date on the product. So, you know, anytime someone decides they do want to pick it up and use it. Like, you know, I have some older Raspberry Pis that are, you know, from the first generation. And, you know, every now and then there'll be some reason that I'll be like, oh, you know what? I can use one of those older ones to do this or put it towards that.

**Dave Jones:** I think that's why a lot of people bought one. You know, it's because, oh, yeah, it'd just be nice to have it hanging around, you know, just in case I need to, you know, a really, you know, high-end CPU to run something.

**Arduino:** Yeah. I think there was a point where I was buying them in batches of five because I was like, well, I know I'll need them. And, you know, I used to do the same with Arduino a lot, too. I know I'll need them. So, just like I'd rather have a stock. I don't ever want to have to wait. Yeah, that's annoying. That kills. And Raspberry Pis.

**Dave Jones:** That just kills your product idea enthusiasm, doesn't it? If you have to wait to get something.

**Arduino:** Yeah. You don't want to have to wait for anything. And, yeah, the tools I was turning to, I tried to stock up as much as possible.

**Dave Jones:** Yeah.

**Chris Gammell:** That's smart. That's experience, folks.

**Dave Jones:** Any, well, what tools are we talking about here? What things do you stock up on?

**Arduino:** It was a lot of Raspberry Pis. A lot of my early projects were based on Arduino. It was all the, like, the proto shields and proto boards that go on, attach on top. Yep. Yeah. You know, all those kind of, like, make it easy for people to do electronics projects that I need. Those sorts of things.

**Dave Jones:** What are the must-have shields? They're not shields, are they, on Raspberry Pis? Get it right, Dave.

**Arduino:** They're called hats.

**Dave Jones:** Hats?

**Arduino:** Yeah, hats. It means hardware attached on top.

**Dave Jones:** Okay. See, I've never heard that.

**Arduino:** I thought it was called something else. Yeah. So when the first Raspberry Pi came out, Adafruit, I think, were the ones who coined the Pi plate, like, nomenclature. Gotcha. Which went on the first generation. When we released the Model B+, which is the much more refined physical form factor of the Raspberry Pi, soon after that we released the specification for hats, which set out the mechanical diagram of how it should be, but also the EEPROM that holds information about how the pins are used, how that can be addressed.

**Dave Jones:** Oh, see, I didn't know that. Is there a... Right, so there's a defined standard. You put an E-squared PROM on your hat board, and then the firmware on the Raspberry Pi is able to configure itself based on that E-squared PROM information.

**Arduino:** Yeah, absolutely. The idea here is that it ought to be... For someone who just wants to learn about how to connect sensors and stuff, we didn't want them to have to do too much to, like, you know, figure that out. They want to be able to pop it on and have it configured on boot up. Yeah.

**Dave Jones:** Although the Arduino thing is pretty simple, right? It's just you know what board you've plugged on there, so you just choose the library for it and bam. So what's the advantage of the E-squared PROM over that sort of manual system?

**Arduino:** The pins do have to be configured, and, you know, I don't... To be honest, like, I don't... I haven't dug into the whole spec yet myself. I am hoping to be able to do that during my time at Raspberry Pi to kind of figure out how that works. But there's... You may be familiar with, like, on the BeagleBone, there's a sort of device tree and device tree overlay where you can kind of, like, configure pins and set up how the... Because they're all multiplexed and how they'll work together.

**Chris Gammell:** So does that mean that if someone outside develops hardware, like a hat, does it have to get, like, registered with the Raspberry Pi Foundation folks? No.

**Arduino:** No, it doesn't need to be registered. You just can't call it a hat. You can't go out and say, I made a Raspberry Pi hat if it doesn't follow the spec. Like, you can, by all means, go and create anything you want that sits on top of the Raspberry Pi. Just if you call it a Raspberry Pi hat, we ask that you follow the spec so that people know what they're buying.

**Chris Gammell:** Fair enough. Yeah. Yeah. And that's good, especially for big marketplaces where there's, you know, a lot of beginners coming. That's really good because that can cause a lot of confusion, you know.

**Dave Jones:** Well, because that screws you up, totally, because if, you know, this is like an educational thing. So if you've got a school that's got, like, you know, a hundred of these things and they go out and buy a hundred of these hats, you know, the sort of the non-authorized hats. And then they, you know, phone up and say, well, it doesn't work. It doesn't work.

**Arduino:** Yeah. That's a big problem. Yeah.

**Dave Jones:** That can suck away all your resources because, you know, they've used some third-party hat, which isn't a real hat. You know, they haven't followed the standard. And, yeah, that just screws everything up.

**Chris Gammell:** So when you were talking about, you know, having these kind of on hand and, you know, and also Arduino on hand, stuff like that, can we go back a little bit and talk about some of your project history? Just kind of run us through some of your favorite projects. I mean, we're looking at this on mattricherson.com and people can go there as well, but maybe some of your favorite ones to work on.

**Arduino:** Yeah, sure. So I think for me, I started, I think my first really big project was called the Awesome Button. And this was all inspired by the Teensy USB, which before the Arduino Leonardo had like its USB human input device set up on it. The Teensy was the first one I think that was really easy to use, had kind of the Arduino development environment, but let you emulate a keyboard or mouse. And so I was using the Teensy, I put it into a Staples easy button, you know, the kind you can buy, you hit it and it plays the audio. And I connected that to my computer. And the idea here was that like I was writing for Make all the time. I was seeing all these awesome things and awesome this, awesome that. And I realized in my writing, I kept overusing the word awesome. So the button every time I put it would jam in a new synonym for awesome so that like, and then I was talking about fantastic and incredible projects. And so I made that and I kind of like showed it around and it, I mean, people really took to it. It really got a lot of attention.

**Dave Jones:** And I saw it at the time. Yeah. It's yeah, it was amazing.

**Arduino:** And like, you know, and then I, I mean, that was like one of my first really big projects that really took off. And I'm, you know, you're watching all these YouTube comments going by and you guys know what YouTube comments. But there's something sort of like exhilarating about it and fun.

**Dave Jones:** And at first, at first, five years into it.

**Arduino:** It absolutely gets exhausting after a while, which is probably why my YouTube channel is like gathering desks right now.

**Chris Gammell:** With fatigue from it, huh? Yeah. Yeah. Yeah.

**Arduino:** Yeah. And then I think the other, the other one people know me from is a project that was inspired by me watching TV. And they were talking about like Kim Kardashian or something or Sarah Palin or something. And I was like, enough. I can't listen to this anymore. And I realized that because at the time I was working on reading the closed captioning data that was coming off the broadcast. And I realized, well, if the programming is closed captioned, I can look for keywords that I hate like Sarah Palin, Donald Trump, Kim Kardashian, and then send the, my television's IR code for mute. So it's an Arduino project that listens to the closed captioning and mutes the TV anytime any of those people are mentioned. Of course, you program in anyone you hate into it. And so I called that the enough already. And that was another one that like, and people really took to that. Like, I think that was the first time an Arduino project was like covered by Us Weekly, you know? Oh, really? Wow. There were entertainment blogs that were really into it. I don't know if it was Us Weekly or whatever, but like there was good entertainment crossover there. I remember like the New York Post called me and was like, so, you know, what about Lady Gaga? Could this be used to silence Lady Gaga? And I'm like, yeah. And like, can you talk more about- The devil just says he can silence anyone. Exactly. He kept pushing me. He was like, so, can you talk more about how much you want to silence Lady Gaga? And I was like, I was not giving him any, I was just like, I'm sorry. Like, I know what you want out of your article here. I read the New York Post before you're not going to get it to me. They're evil.

**Chris Gammell:** They're just evil. The tabloids call you up. Matt Richardson finds Alien also hates Lady Gaga. Right, right. Oh, man, that's hilarious.

**Arduino:** Yeah. That was a fun project because I didn't realize how much that would like, it would, I was explaining to so many people what Arduino was when I was like talking to press about the project because they just love this idea that you could put something together that does something so many people want to do. And so, you know, that was when like, that was probably one of the biggest like mainstream press projects I've done. Yeah.

**Chris Gammell:** Yeah. And I mean, it's good like that crossover stuff as well where it's, you know, it is, you know, there's some popular cultural elements, but also like artistic elements and also just stuff that draws people into technology. It seems like that's a strong theme throughout a lot of your projects. I mean, I-

**Arduino:** Yeah. I mean, I love technology. I love playing with technology. I kind of, I like to, you know, stick the blocks together in different ways and see what kind of comes out of it. I've never, I've never been into the super nitty gritty. In fact, I start to get bored when I have to think too hard about how to implement something. It's my biggest weakness probably. And so I, I'm the kind of person who just looks at the blocks that are already made, let's say a library or a piece of hardware and seeing how I can kind of attach it in interesting ways.

**Chris Gammell:** Yeah. Yeah. That's good though. I mean, like, because a lot of the time that is that integration stuff, I think you were the one who told me about that sketch, was it sketching and hardware? Is that the one? Yeah. There's like, could you, could you talk about that? Cause I don't think we've ever talked about it on the show before.

**Arduino:** Yeah. So sketching and hardware is, I don't know the history of it, but it's a, it's a conference, maybe 50 people get, or some amount of people are invited to it. I think maybe 50 to 70 people show up. It's a different place in the world every year. And it's people coming together to talk about their hardware tools that they use, the things that they make with it. So, you know, you see people from Arduino there all the time, you know, I, I think, uh, when I was there, uh, you know, the BeagleBone was represented, uh, the guys who did Space Brew, the, the platform for kind of connecting internet of things projects a couple of years ago was there. Um, yeah, it's, it's a great conference. Um, I had a lot of fun there. You meet a lot of interesting people and the idea is everybody has to give a talk about like a 20 minute talk and present what they're working on.

**Chris Gammell:** That's an, yeah, I think, I think that's just interesting for a lot of people listening to this because it's like, sometimes it's easy to kind of dig into the electronic side of things and then forget that like, there's also sometimes people that are taking what's, you know, the output of, you know, the people, the stuff people are selling on Tindy or, or other places like that, the smaller pieces like that, and then integrating them into larger stuff. And that can, you know, it can have a big impacts on, on other future projects.

**Arduino:** Yeah. And I, I should say that this whole idea of sketching and hardware, I think it's, it's kind of, it comes off of the idea of sketching user interface design, which I cannot remember the guy who wrote the book, but the idea is that you, you want to, if you can work quickly, if you have the tools that can let you develop hardware quickly, then, you know, you can, you can really refine your product really well. And so it's, it's, you know, that's why Arduino is kind of like the perfect thing to show at sketching and hardware and talk about at sketching and hardware. Cause it's one of those things where it's like, oh, I have an idea for something I want to do. I need to make it happen now. Let's, let's see if I can make it happen right now. And Arduino is one of those things you can grab to make that happen.

**Chris Gammell:** Yeah. No, I remember, uh, uh, Jeremy Blum, who's been on the show before he was talking about, he would show up at like a hackathon and actually do hardware when everybody else is doing software. And the same kind of idea where it's like, you're showing up with pieces that are already there, but you're kind of taking them and then molding them around an idea. And then, you know, trying to basically show the power of the technology there in order to actually output something interesting that, you know, a broader, broader range of people that would understand. So I think that's really cool.

**Arduino:** Right. And it just like with software, yeah, it's just like with software, you, it just, it matters of knowing the tools, knowing what's out there, what's available, and then just kind of like having the, the, the development environment set up for you, however you need it.

**Chris Gammell:** Yeah. So does that mean for your, uh, that you favor certain types? So again, for, for people listening that are, that are developing hardware and projects for others as well, or like smaller, smaller pieces for a larger integration. I mean, is there stuff that, that helps you out? Is it, is it mostly the libraries or it also, you know, interface documentation, stuff like that?

**Arduino:** Oh yeah, absolutely. It's like, you know, when, when you go to a site that has like a, let's say an internet service that has this excellently documented API, you know, that, that's such a draw for me because I really rely on that. Same with hardware. Oh, totally. When it's really clear, it's really clear what I need to do, uh, that it's such a draw for me to use that as a tool. Um, it's critical for me.

**Dave Jones:** I think it's critical for everyone. I don't think anyone wants to reinvent the wheel to struggle just to flash their lead or do something, you know, just to get up to speed.

**Arduino:** Yeah. Oh yeah. Yeah. You're right.

**Chris Gammell:** So, so your background also, uh, so you did that, uh, when I met you, you actually gave me a tour around, uh, ITP. Could you tell us about that a little bit as well?

**Arduino:** Yeah. Oh man, that place is great. So yeah, NYU has a grad school called ITP. It stands for the Interactive Telecommunications Program. But I think ITP is a better word to describe it just because it's a sort of a morphing program. It's not necessarily about telecommunications and, uh, not necessarily interactive. Um, it's a, it was started in the late eighties, I think maybe even early eighties that the idea here is that blending technology and art to create something new and something interesting. So you're, you, the program, the people who are in the program are, some of them are engineers, some of them are artists, some of them are doctors, some of them are dancers. And the idea here is they all want to use technology in some way. And so it's, it's a super collaborative environment. Um, and the classes you take are really kind of, they're, they're, it's interesting the way that the classes are kind of a, of a flipped variety where most of the stuff you do in the classroom is really about discussing how, how technology is used. And the, the outside of the classroom is where you're really learning the stuff you need to learn. Because, you know, if you have a dancer and an engineer, you know, in one class, how are you going to teach the material that's about like doing, uh, let's say drawing on screen or doing projection mapping or, uh, physical computing with Arduino or something like that. So, um, yeah, it's an incredible, it's an incredible environment. Uh, the, the, it's a two year program. Um, I, you know, I absolutely loved it. I stayed on for another year as a research fellow, um, and got to hang out with all these great people and I didn't want to leave, you know, it's a fantastic place.

**Chris Gammell:** That's cool. And what are, what are some other projects, like other projects that came out of there that people would know about?

**Arduino:** Yeah. So the, probably the, the most, uh, well-known project that I did while I was at ITP was the descriptive camera. Um, the idea here is that it works just like a regular camera. You point it at something you want to capture, you hit the shutter button. But instead of a photo coming out, you get a text description. And in fact, the text description comes out on a little slip of paper on the front of the camera. Thermal, thermal paper. Yep. Yep. A little thermal printer. And this is, I think this is, this is an example of a project where I am putting blocks together, like, you know, like I'm literally taking. So one block was the, uh, the thermal printer. And then I used a beagle bone at the time, uh, with a shutter button. The other block was Amazon's mechanical Turk, which for those of who don't know it, it's just how you can basically pay humans online to do tasks online for you. So, um, you know.

**Dave Jones:** Boo. So there was actually a human, there was a, there was a somebody under the mechanical Turk actually.

**Chris Gammell:** Yeah. Yeah. That's what mechanical Turk is.

**Dave Jones:** Oh.

**Chris Gammell:** That's how you prototype. That's good. Yeah.

**Dave Jones:** My dreams of artificial intelligence are shattered.

**Arduino:** You gotta, you know, if you knew me, you knew, you knew that there's no way I could ever do any kind of computer vision algorithm that would tell someone that their hat looks nice and, you know, where did they get that tie? And, you know, that sort of thing.

**Dave Jones:** So what would the response time be between sending the picture and actually getting the text backs, having somebody in India look at the picture and go, Ooh, that's a hat. Sorry about the accent there. I have to add the Indian accent.

**Arduino:** So it, so with mechanical Turk, the API lets you put any price you want on the job. So if I put 10 cents on a job, it would be about 10 to 15 minutes. I put 25 cents on a job. It would be maybe 10 minutes. When I was demoing it for my instructor, I put about $2 on the job and got it done in a matter of seconds, I think.

**Chris Gammell:** Oh, wow. So it's like a bidding, it's like a bidding backend as well. So that.

**Arduino:** Yeah.

**Chris Gammell:** Wow.

**Arduino:** Yeah, absolutely. I think, and I think it's that, that, that, that service is still going. No, it is. Yeah.

**Chris Gammell:** I talked about using it for stuff before for a program or for online.

**Arduino:** Yeah. It brought up a discussion. I think it was with Steve Hofer. He, at the time it came out and he was like, well, it's an interesting thing to think about. Like if you have a robot, let's say that it's autonomous in some senses, and it gets to a point where it's not sure what it should do. Is it about to go over a set of steps or is it about to, you know, approach where it's supposed to be? It is a possibility it could take a photograph and send it off to ask someone, anyone out there to like, tell me what I'm looking at here and how I should proceed.

**Chris Gammell:** Right. No. And I think it's even, even broader. Like it's just, there's so much that technology can't do right now that I think that it actually I mean, the time is definitely a limiting thing for that. But, but like, even when you're prototyping things, there's so much where, like, like Dave, you've talked about this before where, you know, you're like at a trade show and you're the guy behind the booth, like flipping, flipping the LED, right? You know, like that's the same thing. That's the mechanical Turk in this situation. And it's really just a matter of, for prototyping, it's just there while you can't, you know, you don't have the technology in place yet. You can just fake it until, until it's ready, that kind of thing. So I think that actually is, is really powerful. I think the interesting thing with it though, is, is that you can get variation in the results, right? If you took the same picture and send it, if you took the same picture five times, you would get five different things, right? Because you probably have different people describing the picture.

**Dave Jones:** It depends on how complex it is, you know?

**Arduino:** Right, right. And the, one of the ideas I had down, and when I wanted to, I thought about taking this project further was just like, you know, Instagram has different filters or even just any actual camera has different filters you could put on it, that there would be maybe a switch on it that would say, I want poetry or I want prose. Oh, nice. Or I want, I want comedy or I want something deep or dark, you know, kind of set the mood of the text. And then that could then go to the appropriate person. And by the way, when I, when I made this, I was using Mechanical Turk at first and I, and I got accepted into a show where I was going to be showing it and demoing it. And it was going to be like three or four hours where I was going to be taking pictures, taking pictures. And it's like, well, there's no way I can use Mechanical Turk. It'll either be very slow or very expensive. So I, I, I, I like leading up to the show, I cobbled together a, like a PHP backend so that I could have my partner who was at work, uh, just getting every single photo himself. Um, I don't have to pay him. Right. And so I, I just, uh, I just, uh, everything went to him over IM. He replied and it came right out of the camera really fast. The benefit of that was that, uh, my partner is the funniest guy in the world I know. And it became really fun and people got a huge kick out of it because the descriptions they were getting were like totally off the wall. That definitely makes it better. Yeah. Yeah.

**Chris Gammell:** I was, when you were talking about the different types, I thought you were going to say like you'd have different settings where it'd be like Frank or Susan, you know, like the setting is the person it goes to basically.

**Arduino:** Yeah. Yeah. You could do that. And like, you could configure that any way you wanted. Yeah.

**Dave Jones:** Still goes to show you cannot beat the, uh, wet computer, the human brain. I mean, I was just, I was just, um, uh, looking at this the other day, like the, everyone knows that the brain takes like, you know, tens of Watts of power, right? You know, it's like the whole human body's like a hundred Watts or something. Right. Anyway, it's like in the order of tens of Watts for all this computing capability we've got up here. And we can actually, if we really, really wanted to actually match the computational capability of the brain today, but it would, people have done the calculations for this using our current hardware, the best available hardware. It would take, I think, 10 terawatts of power to match the computational. So how many orders of magnitude is that? I mean, so it's, it's possible, but it's, it's just the power consumption. It's physically the power consumption. That's how efficient the brain is. Sorry. I just wanted to throw that little. No, that's, that's interesting. I mean, that little factoid out there.

**Chris Gammell:** I mean, Matt, so, so I've become a little bit more interested in the UI stuff recently. And I mean, I think that, I think that a lot of this stuff coming online too, just, you know, the dropping price of screens and, and, and, and computing and, you know, talking to screens, stuff like that. What's your take on, you know, UI these days and especially like in projects like this or other stuff, do you see it changing?

**Arduino:** Yeah, I think what I'm seeing is that at least with, you know, coming from my perspective and that's the world of places like ITP people and where they're exploring with all kinds of different user interface elements from physical to, to virtual that like the, the interface, we're, we're using screens again, a little more, I think that kind of compliment the physical as well. You know, the, you know, if you can get a cheap touchscreen and a Raspberry Pi that can be your, your user interface, which can be upgraded and changed anytime you want. And then that connects to your, your motors and your whatever, you know, that's, I've seen a lot of that. That's just because I think that the price is coming down and there's better tools for doing graphical user interfaces. That's meant for that, you know? Yeah, right, right. Exactly.

**Chris Gammell:** Huh.

**Arduino:** So it seems like, I like the switches and the dials personally. That's fun. But, you know, I could see a, you know, a nice screen being a great user interface for a physical project.

**Dave Jones:** I can remember back in the eighties, uh, we would pay an absolute fortune for GUI libraries, right? There was none of this, you know, for free stuff available on the internet. There was no internet, right? And you would pay a fortune for these graphical user, I am, for these graphical user interfaces running on these single board computers, right? They were Intel, you know, 8086 PC 104 boards, you know, and, and you would have, you know, racks of these things and, and all the IO cards and everything. So it's a, you know, similar, basically similar to what we've got today. Same concept, but yeah, I mean, just the amount of free tools and libraries available today is just ridiculous. Back then, yeah, you know, we would pay $10,000 for a GUI library for the rights to this GUI library so that we didn't have to write it from scratch, right? But that was cheap because if you had to write this graphical user interface with, you know, icons and pretty things, then yeah, it'll take you forever. It'd take you, you know, thousands of man hours or hundreds of man hours or something. And it's, so yeah, you're happily paid your 10 grand for your GUI library.

**Arduino:** Yeah, and graphical programming is, is one of those things a lot of people I've seen get their start with programming, especially on the hobbyist side, you know, they, you, they may use processing on their computer, you know, to, to draw a line or something like that. And so it just, like, they carry that into the physical world as well. Yeah.

**Chris Gammell:** Yeah. So, yeah, I mean, and I think that it helps too, to have a lot of these resources now for, like you mentioned, you know, you cobbling, cobbling blocks together as well is, you know, that's, I think that's a skill on its own, right? You know, knowing where to find stuff and, you know, put it, piecing it all together and then kind of getting towards that final idea. Oh yeah.

**Arduino:** You've written, knowing what, knowing which block to reach for. Like, that's what I use Twitter for. What should I use? I want to do this. What should I use? And then, you know, before you know it, you get all these responses.

**Chris Gammell:** Yeah. Mechanical Turk for the, for the, in the public, right?

**Arduino:** Yep. Yep. And then sometimes, and then here's, here's what happens sometimes is you're looking at, let's say you say, this is an interesting tool. This is an interesting block here. And you kind of put it aside. Here's another interesting one. How can I like combine these together in some twisted way to like make something that someone has never, ever seen before?

**Chris Gammell:** Yeah. Yeah. That's, I mean, that is tough, right? I mean, like the whole, the making things that are unique is, is it tough? You know, thinking about like project ideation, that kind of thing is, is really difficult when you're, when you're starting out, especially. And, you know, I think.

**Dave Jones:** It's all about the idea. Yeah. Because the, the, the execution is so easy these days. You know.

**Chris Gammell:** Yeah. Well, especially GitHub and finding, sharing, stuff like that.

**Dave Jones:** Yeah. Yeah. You know, it's all about the idea, you know, knowing what you want to do.

**Speaker ?:** Yeah. Yeah.

**Dave Jones:** And then, you know, it's, it's pretty easy to find tools to do it.

**Arduino:** Right. Right. Yeah. And so if, yeah, you, you find the tools first, then a lot of times it inspires the, the idea.

**Dave Jones:** Yes, it does. Yeah. It is. Exactly. Just like the mechanical Turk, right? You didn't actually do anything incredibly fancy technically there, right? You just bolted these things together and, and bingo, out, out popped the solution.

**Arduino:** Right.

**Dave Jones:** So, you know.

**Arduino:** Absolutely.

**Dave Jones:** Yeah. It's great.

**Chris Gammell:** So how do, how do you, how do you think of those new things, man? Oh. Teach me how to think.

**Arduino:** You know, I don't know. I think it comes from kind of having a sort of twisted, like, I don't know. Like, I, again, like, I think most of the time when I, when I've had an idea for a project I wanted to do, it really did come from knowing the technology first or knowing what was out there and saying, Hey, what can I do with it? So the TNT USB, I said, Hey, this could act like a keyboard. You know, what does that allow me? And, you know, it was kind of like letting that tool bounce around in my head and thinking about that while I was writing a blog post one day when it hits you, it's like, Oh, I just used the word awesome three times. I should be using the TNT to fix that. Right. Right. Right. Yeah. Yeah.

**Chris Gammell:** I actually really liked the, uh, that bike helmet one you did as well. I thought that one was, that was probably my favorite of your projects. The, uh, yeah, the bike headlight.

**Arduino:** Yeah. Yeah. Yeah. So that was, that was, um, I don't remember how that even came to me, but I, the idea there was that, uh, it's a dynamic bike headlight. It's a headlight that shines onto the ground ahead of you while you're riding and it can display information in the beam of the headlight. So in the example I show, it's the speed of the bike. Um, but it could show, you know, you know, maybe which way is North or which, you know, maybe it's a navigation information. Um, but, uh, that was, there's a Raspberry Pi project that points, uh, the Raspberry Pi connected to a, uh, what do you call it? A Pico projector. And that had its own battery and the Raspberry Pi gave a battery. I did some coding and open frameworks to read the speed of the bike and then project out the speed ahead of me as though it looked like a, as though it looked like a, like a headlight. Um, that, that was another case where I think, I think at the time, the way I came up with that was, I was like, well, if I look at a Raspberry Pi and what it's capable of, and I look at a projector, which has its own battery and is mobile, what, what could you do if, you know, with a projection and a mobile projection? And I think it kind of went from there.

**Dave Jones:** See, I would have done that a different way. If I had the idea for that, I wouldn't have used a Pico projector. I would have used a normal light and then I would have stuck a, uh, a transparent LCD in front of that. So then you could just, uh, you know, so then the light shines through the LCD and then the shutter, you know, the LCD shutter would generate the shadow. I don't know how well it would work, but you know, that'd be my first. Yeah, exactly. Yeah.

**Arduino:** Yeah. It's great. And it's fun to like, just try all that stuff out, you know, it's like, like if you, I don't know that on my site, I have a picture of it, but like, I, I took like, like the way I, this was like a perfect example of me sketching in hardware where I just screwed with one screw of Raspberry Pi to a piece of wood, clamped down the projector. I ran the wires and I, it's like all zip ties or, or cable wraps and like, you know, it's like zip ties. Yep.

**Dave Jones:** Yeah, exactly. And the problem with that is what?

**Arduino:** That's great. Well, yeah, I was able to get it out on the street and try it out and see that it worked. And so that was probably, that's probably my best example of sketching in hardware. And then, so I'd never, I like, uh, like at the time I showed it to my dad and he was like, Matt, you got to start be like patenting this stuff. And I'm, I'm like, no, I don't have the patience. I don't want to like, I don't want to make a product out of this. I don't want this to be the rest of my life. I want to like move on and do something else. So if there's anyone out there that has the patience to make a dynamic bike headlight, by all means, go for it. Yeah.

**Chris Gammell:** No, I mean, that's what I was thinking when I saw it too. It was like, oh, I, I, you know, it's the kind of stuff where you expect to see, you expect the, the, the, the video to start with the person turning the camera. Hey, Kickstarter, we're here today to tell you about.

**Arduino:** I think I, I, I probably would never do a Kickstarter. I don't want to rule it out ever, but like, I, I just like, I don't have the, the patience and the wherewithal to, to go through with something that long. I want to jump from one project to the next.

**Dave Jones:** And trust me, it is as bad as you think it could be.

**Speaker ?:** Yeah.

**Chris Gammell:** I don't know, man. You've done books. Books are no, uh, that's no easy, uh, uh, yeah. Books aren't easy.

**Arduino:** I can vouch for that too. That pushes, that pushes the limits of my patience, uh, is doing books. It is, it's, it's a grueling process.

**Dave Jones:** And like everyone else, are you going to say that if you're in it for the money, you're a mug? Yes.

**Arduino:** I would say that. Although I, although if I would give this piece of advice, um, that it's not necessarily, it won't necessarily be the quality of writing and the, the, the, all the work you do on the perp, making the diagrams perfect.

**Dave Jones:** Oh yeah.

**Arduino:** A lot of it's going to come down to what you write it about. So in the case of. And how you market it. Right. Yeah. But for me, like, uh, the, the, the best selling book still was the first book I ever wrote, which I co-wrote with Sean Wallace, which is getting started with Raspberry Pi. It was one of the first Raspberry Pi books that came out. Um, and, and that technology.

**Dave Jones:** Everyone's going to buy it.

**Arduino:** Yeah. That, and that technology is just like, it's just much more popular than other technologies I've written about. And that's just the fact. And I lucked out by being able to get the contract to write the book about it. It wasn't that I'm a great writer. In fact, there's a lot, I wish I could like, you know, I, a lot of work I want to do on the book now that the new Raspberry Pi is out. Oh yeah. Right. Um, but, um, yeah, I mean, I, I do tell people like if I, if I were to do another book, it would, it would come down to just choosing the right subject matter that hits that it almost like predicts where, what people are going to want to know about. And that's, that's, that's the tough part.

**Chris Gammell:** Matt, if you could predict the future and do as, don't go write a book, just go play lottery or do, you know, if you can predict the future, that's, that's, that's a better option.

**Arduino:** The Raspberry Pi one was just lucky. Yeah. That was total luck on my part being, getting on that, getting on that gig.

**Dave Jones:** Speaking of which, there is apparently a new Raspberry Pi. So I've heard, tell us about it. Why should we get excited?

**Arduino:** So the, the new Raspberry Pi, it's the biggest leap we've ever made in terms of performance. Um, and you know, if you're familiar with the first Raspberry Pi, it was a single core 700 megahertz processor. Um, and it, depending on the model you had, it was either 512 megabytes of RAM or 156 megabytes of RAM. Um, and, uh, we just released and we just announced and we just started shipping the Raspberry Pi to model B, which has a quad core 900 megahertz arm V7 processor and one gigabyte of RAM. Um, the performance improvement, they, they peg it at around like, uh, six, a factor of six, six times more fast. But like, of course it depends on the application you're using, uh, whether it's single threaded or multi-threaded and it goes, you know, the clock speed alone and the architecture of the processor means even a single threaded application is going to really do a lot better. Um, but then, you know, there's some things that really scream on it now.

**Chris Gammell:** Yeah.

**Dave Jones:** And the biggest leap forward is that it now uses the arm V7 instruction set. Yeah. Right. Because that was apparently a huge limitation of the previous one.

**Arduino:** Yeah. The previous one was arm V6 and that meant we had our special, uh, Raspian, uh, you know, uh, operating system for it and a few other operating systems that people could load on it. And now that we're on arm V7, that means Ubuntu, um, can be run on it and already at release.

**Dave Jones:** Uh, but I thought you could already run Ubuntu on it.

**Arduino:** No, no, there was no support for arm V6. Uh, oh, okay.

**Dave Jones:** Well, how are people running?

**Arduino:** Well, now, now that the Raspberry, now the Raspberry Pi 2 is arm V7.

**Dave Jones:** Um, yeah, but everyone was running a version of Linux on the old one. So how did that work? Yeah, they were.

**Arduino:** It was, it was, it was, that was Raspian. That was a Debian version of Linux. Oh, right, right.

**Dave Jones:** So it's actually a special build for.

**Arduino:** Yeah, it's a special, yes, it's absolutely a special build based on Debian. Oh, okay.

**Dave Jones:** Right.

**Arduino:** And now we're, so we're starting to wade into a deeper area with me when my knowledge of Linux builds.

**Dave Jones:** So, um. Anyway, like. Suffice it to say that, um, the people on the forum have been talking about this and they say it can, it can now run practically the same software any other arm board can run. Right, yeah. So that's basically what it comes down to. Yeah. So if it works on some other platform, you'll be able to run it on this.

**Arduino:** Yeah, there's very strong support out there for arm V7. And so it's, it's great to have that. Um, I'm excited to see what, like, robot operating system is. Right. It only supports arm V7. Ah, okay. You know, yeah. Yeah, I want to see that. I want to see that on Raspberry Pi. I don't know how difficult that is to get over there, but I do want to see that because I think I want to, I love seeing people make robots with Raspberry Pi.

**Dave Jones:** What, what, what platform were people, uh, using the Ros on before? Because it's, you know, as you said, it's extremely popular. And, um, what platform were, were they using?

**Arduino:** You know, I don't know. To actually run that. Yeah, I don't know. I just wonder. Yeah. Yeah.

**Dave Jones:** I just assumed it was Raspberry Pi. I thought, oh yeah, the robot operating system runs on Raspberry Pi. Of course it would. You know?

**Chris Gammell:** Is that the one that the Willow Garage guys were doing? Is that, I, I forget about, I don't, I remember hearing about it, but I don't know who it was.

**Dave Jones:** Every man and his dog's running the robot operating system to control their robot these days. It's the in thing. So they're obviously, I don't have a robot yet, man. They haven't been using Raspberry Pi. Well, you need to get out more.

**Chris Gammell:** Okay. Well. Yeah, yeah. So it's the PR2. Anyway. That's the Willow Garage, the PR2. I just looked it up, so. Okay. Yeah. Okay. That's, I don't know what the hardware internally to it is, but that's, at least, I know the PR2. Huh. Sweet.

**Dave Jones:** Well, that's great, though. Yeah, the Pi.

**Arduino:** Yeah, I mean, I think, I don't know how difficult it is to kind of port those things over, but, you know, it's exciting that it's closer to being possible.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm sure someone will do it. Oh, yeah. Basically, if you build it, they will come, you know.

**Chris Gammell:** Well, especially at scale, right? I mean, that's kind of the main thing is, like, just, that's what's kind of different about this, is scale around a single platform is bigger. Now, David was going to want to talk about PC 104, but I think around a single vendor as well, I think that that's very interesting, you know, from a community perspective, right? That's kind of the big thing here, right, is community.

**Arduino:** Yeah. I mean, with 4.5 million boards out there, with all the support we get from various open source projects that want to be part of that, it means that your experience when you get a Raspberry Pi, there's no, the way I look at it is this, there's almost no question, no technical question that exists without, like, someone asking, can you do that on Raspberry Pi? And someone answering that question. So, like, even the craziest stuff, like, so, you know, you can go out there and look and find that everyone is asking, can I do X with Raspberry Pi? Can I do that with Raspberry Pi? And many of these questions have answers. Sometimes it's no, you can't. But many times it's, well, yeah, you can, and here are these blocks that you need to

**Chris Gammell:** make it happen. Gotcha. What about the, so, so one of the things that I remember from the first version was some of the limited IO output stuff, but then I didn't pay attention when the B, or when the B plus came out, or I remember the header got bigger. Could you kind of run us through some of the header stuff and what, what is output from there?

**Arduino:** Yeah, the, when we came, when we released the B plus, we, that was, that was actually a big change physically for Raspberry Pi and the way it looked, you know, you got the rounded corners, but the, and the screw holes were finally in the corners, which were like, that was the thing. I don't know. It really bothered me that it had the squared off corners and the 90 degree corners and the screw holes were like all over the place. But, um, the, yeah, the, the headers were now on a 40 pin header, uh, which now all our models have, uh, the model a plus, which is the lower end, which is the $20 version of the Raspberry Pi has the same 40 pin headers, GPIO. It's got input and output, UART, um, I squared C, that kind of stuff. Um, and, uh, so that's, uh, that's kind of like our, our, any kind of hat, any attached hardware expansion board will, will go onto that 40 pin header now up from, I think it was like 26 pin header before.

**Chris Gammell:** So is there no native, uh, SPI though? Is that the one that was not there?

**Arduino:** I don't know. That's, that's the, that I, I don't know about that. Okay.

**Chris Gammell:** Cause I remember, so I was doing a comparison of, you know, a couple, I guess it was years ago now, but it was comparing just kind of BeagleBun Black and Raspberry Pi. And obviously you've written books about both, but it seemed like that was one of the things that was limiting because I usually go for chips that are spy because I'm, I don't like I squared C for some reason. I don't know why it's like, Oh, run, run more lines, Chris. That's smart. Uh, so yeah, I don't, I don't know what the, uh, I didn't know if there was that in there, but I mean, you could always bit bang it, but then maybe the, uh, then that, that kind of ties up processors and stuff like that.

**Arduino:** My, my intelligence shows that, uh, the, the information I'm looking at, I should say shows that there's one SPI bus.

**Chris Gammell:** Oh, there is. Okay. Okay. Yeah. Cool. No, that's good. That's good. I mean, like, and honestly, like with high enough speeds, usually, you know, you're going to be pushing certain amount of data over, over that, but you're not going to, you could always multiplex it on the other end if you do have, you know, the right, the right, uh, hat on their plate or whatever you end up calling it. So, yeah.

**Arduino:** Mm-hmm. So you're, you're informing me now because I'm learning from you. This is, this is, again, I'm, I'm, I play with blocks. Yeah. No, that makes sense.

**Dave Jones:** Let's go through the issues on the forum. Um, the, one of the big, Matt, the support, tech support, tech support for Matt. Tech support, tech support for the, for the EV blog forum. Here we go. I have no comment on this.

**Chris Gammell:** I have no comment on this.

**Dave Jones:** One of the big limitations of the Raspberry Pi has always been that it's not open hardware, right? It uses the Broadcom, uh, chipset. Right. And that's still the case, right? It uses the, uh, BCM 2836 now.

**Arduino:** Right. We went from the 2835 to the 2836.

**Dave Jones:** Which you cannot even get a data sheet for. You have to like sign your first born child away to get a data sheet. Right. For this thing. And is that, has that been the issue? He's going to sign Sagan away, but his wife said no. He said no.

**Chris Gammell:** She said no. So.

**Arduino:** You know, I, I, it's a good question. Um, you know, I think what I, I remind people is that what we're, our mission here is to make an inexpensive learning computer. Right. Open source is great. Um, we do a lot of contributions to open source software projects. We are open in a lot of ways. Um, there's been a lot of work on the video core video driver to make that more open. Oh yeah. On the Broadcom side. Um, but, um, you know, we have to weigh a lot of options when it comes to creating an inexpensive learning computer. And, um, you know, again, that, that, that, that has to be our priority and how we keep it inexpensive and, and how we give it all the power we need. And, um, yeah. So.

**Dave Jones:** And all these pesky people who are thinking that, who want it to be more than you intended it to be. Right.

**Arduino:** And again, like, you know, the, that we, we, you know, we love all the ways that people use Raspberry Pi. It's fantastic that it's not just a learning computer. It is, it has become much more than that. It's absolutely fantastic. It's like a late speed, you know? And, uh, but you know, we, I, like every time I'm reading up on something or I'm, we're thinking about a decision, the mission of our foundation has to come to mind first. And, you know, that, that's really the priority. And so, you know, for example, a lot of people ask, well, why is there no gigabit ethernet or why is there no SATA on it? And, and again, it's gotta be an inexpensive learning computer. I don't know. It's $35.

**Speaker ?:** Yeah.

**Arduino:** It's $35. Honestly, I don't know how much people are going to learn better if they had SATA on the board. I know.

**Dave Jones:** And on the forum, they're talking about why don't you support LVDS and, and TMDS LCD interfaces and all sorts of stuff. It's like, you know?

**Arduino:** Yeah. You know what? I think it would be, it would be a lot easier to create a board that had everything you want on it, I think, you know? But we, you know, our mission.

**Dave Jones:** It's twice the price. It's three times the price. Exactly. Exactly.

**Arduino:** If you, if you pull off the restriction on your, your price restriction on it, which ours is especially low, you know, yeah, it's, we could throw all that stuff on there. Sure. I'm sure it's tempting. And again, I can't speak for the engineers who make the decisions on, in Cambridge, but you know, I'm sure it's tempting to say, yeah, I do kind of want that, but how are we going to make that work with, you know, with our bottom?

**Dave Jones:** That must be frustrating. As a design engineer, that must be, yeah, that must just eat away at you, you know, but there's other solutions out there. If you want higher power, you go for a BeagleBone or an Intel Edison or something, right? Or roll your own. Yeah, or roll your own, damn it. You slack asses out there. Yeah, exactly.

**Chris Gammell:** We talked about, you know, Bunny had that post about the Gankai phone and the MediaTek chip as well, and it seemed like, you know, it seemed like a similar trade-off as well. It's like, you know, you can use, and him and Zobster were hacking this chip to try and get it at the register set and stuff like that. But basically, it was a trade-off. It's like, you want this super cheap chip, you kind of have to, you're not going to get any support because there's all these commercial applications that are making it so cheap in the first place. You know, that's kind of the same. It seems like a very similar kind of thing. Yeah. And it's just kind of pick your poison. Do you want to be low cost and chase those parts that are in the super low cost region or, you know, maybe more access at a higher price kind of thing? Right, right. So, yeah. That makes sense. I mean, that's good. I mean, that's good to acknowledge that trade-off is, you know, it would be better if it's open hardware, but there are realities in the electronics industry that we have to deal with.

**Dave Jones:** Look, if you want a higher powered platform, you go for an Odroid C1. It's $35, right, for this Odroid C1 platform. And it's, you know, and it's got better, like, you know, Ethernet capabilities and all that sort of jazz, you know, if you're into that sort of thing. Right.

**Chris Gammell:** Right. And then in that case, you give up maybe some of the community as well, right? That's some of the other stuff.

**Dave Jones:** Totally. Totally. You totally give up the community. But if you wanted some, like, real hardware to, like, you know, run some, like, you know, real grunty industrial stuff with, you know, like, the learning board-oriented Raspberry Pi is probably not the platform for you. You know, you want something else that's more tailored to that.

**Chris Gammell:** Yeah.

**Arduino:** I sometimes don't understand what, you know, when, you know, people want all this performance. I'm not even sure what that extra, you know, half a gigahertz is going to, oh, really. How do people use that?

**Dave Jones:** Well, in industrial applications, it's easy. Vision, for example. Okay. You know, to do vision processing, that's a huge, big thing these days, and you need a lot of processing power. And even with the, you know, the fastest boards out there, the fastest processors out there, you still can only do, like, you know, 640 by 480 at 15 frames per second or something, you know? So, yeah. Right. You know, people are really pushing for that sort of thing.

**Arduino:** Right. And it reminds me of people who say, like, oh, you know, the Raspberry Pi is not a good NAS because USB and Ethernet are shared. Yeah. And I think, well, we're not trying to be a NAS here. NAS, I know.

**Dave Jones:** If you want a NAS, go out and buy one. You know? Like, there's plenty of platforms out there. Yeah. Yeah. I know. Yeah. It's pretty dumb. Yeah.

**Arduino:** Yeah. But, you know, I'm happy that we have all these people also challenging us and there's competition out there. It's great, you know, to have other people. You know, you look at some of these other boards. They look a lot like the Raspberry Pi. So, it means we've got to be doing something.

**Chris Gammell:** No, it's true. Yeah, exactly. The right size and the right, you know, a lot of the similar peripherals, stuff like that. I mean, but, and that's another thing that people give up, though, too, is kind of like, you think about it. You know, you can go buy a ripoff of just about any type of hardware if you go to, you know, Shenzhen Markets. But what you're going to be giving up there, too, is, you know, we've talked about this with, you know, Arduino as well, right? If it's not an Arduino thing, you show up at a forum, you're like, well, I've got this piece of hardware. It's not working. Now what? And then, well, is it actually, you know, the right piece of hardware? Then you lose that, right? So, you lose that kind of things. So, that's, I mean, and ultimately, I think that's going to be one of the things for, especially around education, stuff like that. So, that's where Raspberry Pi is doing well. Yeah. Yeah. Absolutely. What are some of the things? I mean, like, so, I know you've only been there a month, but obviously, you've seen it in the past with your past work with it as well. You know, are you seeing, or is the foundation seeing people doing a lot of, you said schools, but are there like classes forming around it, that kind of thing?

**Arduino:** Yeah, right. So, in the UK, I think Raspberry Pi has a kind of a good handle on the UK education system. Unfortunately, in the US, it's a little bit, you know, it's not as cohesive. There's probably lots of different education systems. And I don't, you know, at least 50, I would say. Yeah, probably. Probably even more. But, so, what we really, we need to do is kind of figure out how best are we going to, you know, approach the US education market. And, you know, so it's like, how to do that most effectively is what I'm sort of been figuring out now. I've been just basically on the phone calling people all the time. Anyone who will give me time who knows anything about the US education market, especially when it comes to computer science education, you know, talk me through it. What's your decision, you know, when you're choosing what you want to do with your students? So, you know, we have in the UK, they run this thing called Pi Academy, where UK teachers can go and learn about Raspberry Pi and connect with each other and be a part of the Raspberry Pi community so that they can kind of take it back to the classroom. We're figuring out, does that same format, will that work in the US? How can we pull that off? And what changes do we need to make? So, you know, figuring that out now. That's cool, though.

**Dave Jones:** What age groups are you looking at there? Is this like high school?

**Arduino:** Yeah, oh yeah, high school, middle school, even less than that, you know, even in lower ages than that, you know, because it's preloaded with Scratch, for instance, you know, the drag and drop programming language. So it really lowers the bar for people to get on it and young people to try it out. That's awesome. There's a version of Minecraft on there. So like, wow, that's, you know, that's a great way for people to at least want to set up a Raspberry Pi. And then hopefully maybe they can explore beyond that a little more. That's really cool.

**Dave Jones:** Or just wasting their life playing Minecraft.

**Chris Gammell:** There's some benefits of that. I think Minecraft's one of those weird things where it has like these ulterior effects, you know, like, that's not the right word. But like, but basically, you know, they're learning logic by building stuff up as well. I think there's some, there's been a bunch of interesting posts about, that's fine.

**Arduino:** I think there are some mods to Minecraft. There's people out there who, there's the mod community who use Python to mod Minecraft. There is a project that they want to do a Kickstarter soon called Piper, where you're learning electronics with Minecraft with Raspberry Pi. So yeah, I think like, Minecraft is a bloody breadboard.

**Dave Jones:** And some components plays. And then the source goes. Well, you do.

**Arduino:** And so the idea is that you see the breadboard in Minecraft world, but you have to replicate it in the real world. And so for, for kids who their motivation to do something is Minecraft. And apparently there are a lot of kids out there like this. This is, this is a, a way for them to kind of get in there. The project's called Piper. And I think they're going to be doing a Kickstarter in the, in, you know, in a couple of weeks. Right. No, that's good.

**Chris Gammell:** I mean, that's, I mean, Dave, you, you, you and I have grown about it before, but like, it's anything that brings people into the field is good. Right. I mean, like ultimately whatever it is, right. If it's, I mean, like hell, if that Us Weekly article that, that, that you talked about Matt, like if that brought people in, who cares? Right. It's like, oh, Us Weekly readers, you know, that's trashy, but you know, but who cares? You know, it's just about bringing people in. That's, that's, that's what's interesting. And, and.

**Arduino:** Yeah. I'm glad there's lots of points of entry. Yeah. You know, I, you know, it may not be the tool for you or me, like a Minecraft isn't something that I'm particularly interested in, but I'm glad that people who, who, people who that motivates, I'm glad it's there for them.

**Chris Gammell:** Dave's just upset because there's Minecraft players who make buttloads of money on YouTube just playing Minecraft. Oh, no kidding.

**Arduino:** A hundred times more than me. Are they pushing your, your, are they pushing your ranking down or is that? There we go. Right.

**Dave Jones:** No, they're just earning a shitload more than me. Yeah.

**Arduino:** For much easier videos. Well, you know where to switch to then. Yeah, I know.

**Chris Gammell:** Well, in terms of bringing people in too, I mean, like that's one of the things I mentioned this before the show is like, you know, this is, I think Raspberry Pi is really interesting for me as well because I see like, you know, I talk to people that are like, like just computer networking people that just never would have even considered it. And even if you, so out of the 4.5 million, say 1 million of them are computer networking people that never would have touched electronics. And of that 1%, you know, maybe consider it. And then of that 1% actually do it. You still got a chunk of people that are still entering and trying things out. And like, sometimes it just comes down to numbers and it can spread like that, you know, getting more people interested in electronics.

**Arduino:** Absolutely. I know that like so many of the people who I know who work in the world of web development have been asking me about all these different hardware platforms. The fact that they can, you know, spin up Node on a Raspberry Pi or whatever is like, that's like, they're in some kind of comfort zone there. Yep. And then they can kind of push that out a little bit where if there's a library that lets them access the GPIO, okay, yeah, they made a, something that tells them if the bathroom is open or not. And it's using some crazy JSON API and everything. But that's like, it's so crazy to do that, but that's kind of like their comfort zone. And that's how they kind of like, you know, find their way out in that realm.

**Chris Gammell:** Yeah, it's very, it's very top down. Like, so, so we, like many things, Dave and I have disparaged JavaScript based processors before, like, and now I know the Tesla folks and stuff like that. And I talked to them about it, like, oh, what's the difference and stuff like that. And, and, you know, like between using C or using JavaScript on, I think it's actually no running on like a micro. And it's like the, the time differences is huge, but when you put that in front of someone, it doesn't matter. You know, you're getting someone in, you're showing what you can do, then they go. And then I think the people that are going to be optimizing anyways, eventually then it's like, you know, C is your end point or assembly is your end point anyways, right? It is as you chase more and more perfection and not perfection, that's a bad word, but, you know, just optimizing for that kind of stuff. You're going to learn, you're going to teach yourself a bunch of other stuff in the way anyways, because, because you want your robot to get out of the way in time or you want your, you know, your vision application to do what it needs to do. So I think that that ultimately is what it's all about is, you know, access and bringing people in.

**Arduino:** Yeah, absolutely. It's, you use the tool you're comfortable with to, you know, get something done quickly, even if it's some phony prototype, you know?

**Chris Gammell:** Yeah. Oh, definitely. Definitely. So are you seeing, so in terms of like the community stuff, are you seeing, are you, do you get to like an inside view of like interesting new projects now? I mean, I don't know if you can tell us about interesting new projects, but like within the community?

**Arduino:** Yeah, no, I haven't seen, and no one's come to me with, I mean, that Piper project, someone came to me with that. And I thought that was pretty interesting what people were doing, the Minecraft electronics one. But, you know, yeah, I, I, I hear, I hear ideas of people want to do, I haven't seen anything interesting yet. But, you know, like the, one of my favorite makers, Michael Newman, sent me a project that he had worked on, which was like an installation at UCLA extension. A, it was kind of like, the effect was a panel that had 35 separate circular screens on it, but it was really just one large screen with like, kind of a masking over it. And, um, it's a really neat project. I wrote it up for the Raspberry Pi blog, um, because I liked it so much. And, um, you know, I, I just love that, like, this is a case where people are using screens in interesting ways. And, you know, as people are upgrading to their 4k television sets and they don't know what to do with it or whatever, you know, their, their junkie, whatever said, uh, that sucks. Um, they can, you know, put that towards a project or an interface or something, you know? Yeah.

**Chris Gammell:** Oh yeah. Yeah. I, I definitely saw, I was like, when I got mine, I'm like, oh, I'm using all my HDMI connections. Like, no, you know, it's like those small things that just kind of like, oh, well now I have to go figure something else out. I don't know, but it's, it's about, it's, yeah, that's what we have to deal with. I suppose.

**Arduino:** Yeah. Yeah. But yeah, there's, I think there's, there's going to be a lot of great stuff coming down. Um, a lot of people working on things where I like, I'm, I'm working on some cool partnerships in the U S here. I'm, you know, talking to a lot of people trying to get raspberry pie out there. And, um, you know, I'm one guy over here in the States. And so if actually you're the only one on the first, I'm the first ever raspberry pie employee in the U S and so, um, I can use all the help I get. I can get like, uh, you know, partnerships or ideas, um, ways that raspberry pie can kind of get out there in the U S and why, how we can basically, you know, advanced computer science education in the U S using raspberry pie. Let me know.

**Chris Gammell:** Oh yeah. Yeah. We'll get your contact info at the end so that everybody, everybody knows how to get ahold of you.

**Dave Jones:** You're just working from home.

**Chris Gammell:** Yeah. Yeah. I love it. Sweet. So I want to hear a little bit more about the educational side of things. Like, so what, so have you gone through the, the, the UK stuff, like for the UK pie Academy stuff?

**Arduino:** So my, my, I haven't gone to pie Academy yet. I, I, I, the, I, the plan here is that I'll be making at least quarterly trips to the UK to be with the team in Cambridge. Um, and I'm hoping that next time I can time it so I can sit in on a pie Academy to see how it runs and see what's needed for it. And the, you know, see how we'll adapt it for the U S. Um, our, the education team is also, I've been talking to them about bringing them out here to do a pie Academy. There are a lot of different possible ways that like, there are a lot of possible ways that we can kind of get that, that those resources out there, whether we bring it from the UK or we seed it here or something, you know, we're, we're, we're figuring that out. I think we're going to try a few different things to see what works best.

**Chris Gammell:** I was just wondering like, uh, what, what programming languages and stuff like that that might be used. Oh, usually like Python.

**Arduino:** Okay. Okay. Yeah. Yeah.

**Dave Jones:** Python is kind of model. Yeah.

**Arduino:** So the model a takes away the ethernet port and three of the four USBs, uh, USB host ports. So it's much smaller as smaller footprint, much lighter. It still works with a hat specification and has the, uh, the Broadcom 2835 on it. Um, and, uh, yeah, that's supposed to be the even lower costs, Raspberry Pi. If, if you want to use that as well, it would be great for smaller projects.

**Chris Gammell:** Yeah. Yeah. And it wasn't there like that, uh, memory card form factor at one point.

**Arduino:** Yeah. Yeah. And so that's still around. That's the compute module. So let's say you've made a project with a Raspberry Pi and you want it to be a product. Um, one way you could do that is by using the compute module, which uses a so dim, um, interconnect on it's basically has the Raspberry Pi. The, the, it's, it's basically the Broadcom chip, the Ram and some flash memory as well. So if you want Linux in your product, you can put this into your design and it takes care a lot of the, the, the hard stuff for you. Um, so there are like, for instance, there's a, a hackable camera called auto OTTO that uses the compute module. They had a Kickstarter that was a smashing success. And so I think they're starting to ship now. Um, and yeah. So every single one has a Raspberry Pi inside.

**Dave Jones:** Right. So is that actually made, is that actually made by you guys?

**Arduino:** Yes. Yeah.

**Dave Jones:** Oh, okay. So that, that seems to be against your focus on making an educational board. You've actually developed this compute module for like sort of like commercial industrial applications.

**Arduino:** Right. Yeah. And we found that, you know, there's all those people who, uh, do use Raspberry Pi beyond what, what Raspberry Pi is used for, um, what Raspberry Pi is intended to be used for. And so, you know, they, they wanted to provide some kind of stepping stone so that projects that are based on Raspberry Pi that, that, you know, that advanced Raspberry Pi, that they had somewhere they can kind of graduate to without needing, figuring out how to get into the world of like, uh, you know, putting an SOC chip onto a board themselves. Um, so yeah, that you're right that, that absolutely it does. It's kind of more of a play in the industrial, uh, area, but, um, that was, uh, what's great about it is that every single compute module sold will benefit the educational mission. Yeah. Yeah.

**Chris Gammell:** No, that's interesting. That's a, I, I was imagining like, well, I started with the Raspberry Pi and then in the next day I was doing a high speed layout for a, yeah, yeah, yeah, right. A DR3, I don't know. Yeah, yeah, yeah, that's right. Crap! No, that's really cool though.

**Arduino:** Yeah, it's, it's nice that at least that like, you know, we, we didn't want to ignore the people who were doing these incredible things with Raspberry Pis that could become products. Um, it's not, it's certainly not meant for people who are going into super high volume because we don't allow, the price breaks just don't work that way with us. You know, it's, it's, it's cheap for everybody, not just some people. So, um, it's, it, with the way I look at it, it's kind of a stepping stone on to like, so that you could do maybe, uh, 5,000 of a product that is based on Linux using Raspberry Pi.

**Dave Jones:** Yeah. So I would assume that you actually make a profit on that, which then supports your essentially non-profit educational focus.

**Arduino:** That, that, that's exactly right. Right.

**Dave Jones:** Yeah. Because you have to get your money from somewhere. Otherwise, you know. Right.

**Arduino:** Unlike charities that go out and seek donations, we just try to get people to buy Raspberry Pi because all the profit from that goes right into the foundation and supports it. Yeah. Of course, some of it goes, uh, obviously some of it goes towards, uh, you know, improving the product. Um, and then a large portion of it also goes to the education side.

**Chris Gammell:** Yeah. It's interesting too. I wonder, I mean, has there been any talk with like the OLPC, the one laptop per child foundation at all?

**Arduino:** No. You know what? What's the deal with them? I, I, are they still around?

**Dave Jones:** Uh, I've been in contact with a guy that's doing something similar to that. I am not a fan of the one laptop per child.

**Chris Gammell:** You're not a fan of the foundation or the actual hardware?

**Dave Jones:** I'm not a fan of the concept.

**Chris Gammell:** Oh, okay. Well, I, I, I always thought it was a cool idea in terms of like, well, I mean, it's a, it's a, it's a similar, it's a similar idea of, of like broad access to computing and programming and stuff like that. But Dave wants to say.

**Dave Jones:** Well, I want to say that these children in third world countries need clean water, education, medicine, right? Right. They don't need a freaking laptop, right? They need essential stuff to make them healthy and learn. Not, you know, like.

**Chris Gammell:** Well, I think it could go towards a learning thing. A lot of these people don't. It's just a lack of. I agree with the other stuff.

**Dave Jones:** It's a lack of priorities. You know, if you're going into these third world countries and you're given his, he's a laptop. Congratulations. Look, you know, and they go on, but, but my family's starving. You know, I don't have fresh water. I don't, you know, have, you know, pens and pencils for my classroom. Like it's.

**Chris Gammell:** Yeah. It just bugs me. You know. Yeah. No. From a humanitarian side, of course. Yeah. That makes sense. Yeah. Yeah. No. But I think, I mean, I know one of the things that they had struggled with was they were trying to get like sub 100 or something like that. And they. Yeah. They had missed it once or twice. But I mean, it's, I just, I think it's interesting seeing, you know, going forwards, you know, this is, this is the path of hardware, right? It's just these lower and lower cost things. And so this could kind of supplement that if they're, you know, in places where there is hopefully they've, you know, access to water, clean water and food and stuff like that.

**Dave Jones:** Once they have all the basics, then yes. Yeah. Once they have, you know, basic infrastructure, then I'm a supporter of it. Absolutely.

**Chris Gammell:** Yeah. Definitely. Hmm.

**Dave Jones:** Yep.

**Chris Gammell:** Hmm. I had actually, I woke up from a, I woke up from a dream the other night and I started thinking about, so I, you know, I teach contextual electronics. Now we're getting trippy.

**Speaker ?:** Now.

**Chris Gammell:** Where is this going here? No, no. So I had taught, I'd, you know, so I try and offer like, I suggest, you know, common tools so that we're all on kind of the same basis. And, you know, like, like the, the EX330 that Dave talks about in the $50 shootout, stuff like that, you know, just like low cost, but effective tools. And then I started thinking about, well, what happens now if you offer a common computing platform as well, right? Because there's always a lot of strife around computing of, oh, well, you know, it doesn't work on my version of windows or Mac or Linux or anything like that. Obviously, you know, KiCad has that problem as well. But then if you kind of standardize around a platform and it has enough computing power, right? Like this upgrade to the Raspberry Pi 2.

**Dave Jones:** You're talking about tools, right? You're, you're, you're talking about running KiCad and.

**Chris Gammell:** Yeah, right. And, and Matt, you had mentioned to me that it does run on there well, right?

**Arduino:** Yeah. That was one of the first things I tried. It was a pretty easy install. It loaded up. It felt really snappy. Yeah. And so what I, what I'm hoping to do is to be able to design a hat. Oh, nice. Expansion board. Recursive hardware. Using Raspberry Pi. Yes, exactly. Use Raspberry Pi to design expansion hardware for Raspberry Pi. Show people how to do it. And maybe you either mill the board yourself or you send it off to get manufactured.

**Dave Jones:** I was going to say what it does is it needs to talk to a milling machine and then talk to a pick and place machine. Yeah.

**Arduino:** Both of which have Raspberry Pis, right? Yeah. Yeah. Well, I went, I went to visit other mill. They make the, I went to visit other machine where they make the other mill and I, you know, that machine is incredible and really neat. And I was like, oh, how could we get Raspberry Pi running this so that we can go right from the CAD right to the mill and get those boards coming out.

**Chris Gammell:** Yeah. That's great. That would be, that would be really cool. So, um, yeah, I'd love to see that. Yeah. So, I mean, like, I was just kind of thinking about that around like, you know, and I put it out on Twitter and a lot of people are like, oh, I use this and use that. And I don't, it was, the argument was not specifically for Raspberry Pi, but just the idea of having low cost common hardware. I mean, that's obviously the educational side of things like, you know, you guys are working with, that's really important because you remove so much variation. Yes. People have to give up their free, their choice on, you know, platforms, but sometimes you don't want that, you know? Like, and people are like, oh, my hardware, blah, blah, blah. I don't care. You know, like when you're trying to achieve a goal like education, it can be really beneficial. And, and, and that's good because that's what you guys are trying to do. So.

**Arduino:** Yeah. And, and, you know, it reminds me that we, we, like one of the things that is out there is resources for doing bare metal programming with Raspberry Pi. Um, you know, so people can use assembly to, to, you know, bring it up. And obviously it's really rudimentary. It's something I've been meaning to kind of play around with a little bit because I've always been kind of using higher level languages my whole life. I'd love to just kind of jump down and get, get in there a little bit. Um, it, it, it focuses on how to write assembly for, that runs on Raspberry Pi. And that's great because so many people out there have Raspberry Pis and can try it out and it doesn't need to be for a particular chip or whatever. It just, you know, here's how to do it with your Raspberry Pi. I love that. I can't wait to try that myself.

**Chris Gammell:** Yeah. Someone had mentioned that to me that there was like a course about, there was an online course or, I don't know, it was at Stanford maybe?

**Arduino:** I don't know if, um, I think it's, uh, University of Cambridge, uh, School of Computer Science has the, the bare metal core, has a bare metal core. I'm sure there are plenty of them out there.

**Chris Gammell:** Yeah. Excuse my ignorance on this and maybe Dave will laugh at me as well, but like you don't need to know anything about register sets or anything like that in order to do that bare metal programming. I mean.

**Dave Jones:** You do. I was going to ask about that. How do you do the assembly language programming if you don't have the data sheet?

**Arduino:** Um, that's a good question. I, um, that I haven't gone through the tutorial yet myself.

**Dave Jones:** Or maybe, or maybe you can get the programming. No, but I thought the whole concern about the, um, about the Raspberry Pi and the use of the Broadcom chipset is you couldn't get any information on it, let alone the, um, actual, uh, physical, like the assembly, like the instruction set programming language. So I, I, I'm very curious to know how, how that's going to work because, uh, Broadcom won't be a fan of that if they're. Well, it'd be interesting for us if it was a hack. Sorry, dirt. It's arm. It's arm seven. Oh God. What am I thinking? Yes, of course. It's the arm V seven. It should just work, but then you've got to, yeah. Okay. So that's the instruction set you need. Yes, you're right. That's what you're saying. Okay. Yep. Yep. Yep. Okay. That's why I felt stupid. I think the IO side of things is maybe different, but yeah. But as far as actually running code on the processor, yeah, it's just standard arm V seven. Of course it is. Duh.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** Yeah.

**Chris Gammell:** And again, that was my lack of knowledge. I don't, I don't do assembly.

**Arduino:** So not yet, not yet, but I know where to turn if I want to learn it and I'm going to do that.

**Chris Gammell:** No, that's cool. No. And I think, I think someone mentioned that Stanford or somewhere, somewhere out West coast is doing it as well. So. Oh, cool.

**Arduino:** I'll have to look that up. So I do want to know what people are doing in that realm. Cool.

**Chris Gammell:** So any, any big projects planned for yourself? I mean, do you got anything in the hopper?

**Arduino:** Right now I'm focusing on where we're going to be going to South by Southwest. Oh, cool. Interactive. We're going to have a nice presence there, I think. So I'm, I'm figuring all that stuff out now with some of the folks in Cambridge to figure out how, you know, we're going to, what kind of fun activities. We're going to do. We're going to have some hands on stuff. What barbecue to go to. Salt Lake. Salt Lake. Party. Yep. Yep. Oh yeah. So yeah, we'll, yeah, we'll be at South by Southwest. We'll have a nice contingent from Raspberry Pi there where we can kind of really kick off our U.S. Our U.S. presence, even though we do at Maker Faire. They've done Maker Faire many years now.

**Chris Gammell:** Yeah. That's great though. I mean, you're like, you're like the, the U.S. beachhead for, for, for Raspberry Pi.

**Arduino:** Yeah. Yeah. It's great. It's a little overwhelming. I have to say it's, it's a little overwhelming and there's a lot of work to be done. And, but, um, luckily there's plenty of like really eager partners in the U.S. who are just waiting for Raspberry Pi to have enough bandwidth to be able to like really like foster the relationship. So I came in and got a bunch of emails of people I should contact and it's been great.

**Chris Gammell:** Well, I'm sure you will also get some emails from our listening audience. So how, or well, or however you'd like to be contacted, how should people contact you?

**Arduino:** Yeah. So I mean, I'm on Twitter, just Matt Richardson. And, uh, if, if anyone wants to just have a casual conversation with me, but if, if anyone out there does have, uh, something passionate they want to talk about when it comes to Raspberry Pi, Matt at raspberrypi.org is where they can email me about it.

**Chris Gammell:** He got the single name email. That's, that's early. Nice.

**Arduino:** I wish you, well, that's why.

**Dave Jones:** Right in at the ground floor of the company.

**Speaker ?:** Yeah.

**Dave Jones:** So no other Matt's allowed.

**Arduino:** I wasn't sure if I wanted to join Raspberry Pi or not. And I asked, well, are there any other Matt's there? They said no. And I said, so I can have Matt at raspberrypi.org. They said yes. And so I said, yes, I'll take the job. Wow.

**Chris Gammell:** That's great.

**Dave Jones:** That's your sole job. That's your sole requirement for joining a company now. What will my email address be?

**Chris Gammell:** Before, before I say yes here. How many shares of Raspberry Pi? Oh, oh, is it non-profit? Okay. I'll take the address. No, this is fine. Yeah. Well, Matt, thank you so much for coming on the show. We really appreciate hearing about the, the, the new stuff in the U.S. That's awesome.

**Arduino:** And yeah, thanks for having me. This is a lot of fun.

**Chris Gammell:** Cool. Well, we'll, we'll talk to you on Twitter soon, I'm sure. And we'll look for, for more projects. Thanks, Matt. Thanks a lot.

**Dave Jones:** Catch you next time. Thank you.

**Speaker ?:** Bye. Bye. !
