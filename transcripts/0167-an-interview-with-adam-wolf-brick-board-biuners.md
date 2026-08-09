---
episode: 167
title: An Interview with Adam Wolf - Brick & Board Biuners
url: https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded October 14th, 2013. Episode 167. With guest Adam Wolfe. Brick and board by Uners. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Adam Wolfe:** And I'm Adam Wolfe of Wayne and Lane.

**Chris Gammell:** Hey Adam, just me and you today. Dave bailed on us and sounds like Matthew, your other half of Wayne and Lane couldn't make it. Yep. Well, that's okay.

**Adam Wolfe:** He's got some sort of wedding emergency or something.

**Chris Gammell:** Yeah, that's fine. Well, we will find many things to talk about, I'm sure. People probably know you from online from your Wayne and Lane stuff and all your KiCad helpfulness on Twitter. And that's obviously what I'm very interested in these days as well and work and everything else. But yeah, what's your background? Tell us your life story. Sure.

**Adam Wolfe:** So I'm Adam Wolfe. I met Matthew when we were in sixth grade. We did nerdy stuff together. Like we made logic gates out of Legos and stuff like that. Oh, yeah. Which is pretty, pretty nerdy for a bunch of 12-year-olds. But I mean, not really necessarily that nerdy. We went to college in Minnesota. And we got degrees in computer engineering. And then after we graduated from undergrad, he went on to work on his PhD in, I believe, computer engineering at Carnegie Mellon. And he recently moved back. And I went into industry and I worked at a large defense contractor for a few years. They closed their site here in Minneapolis two or three years ago. And I changed jobs over to work for Digi, who makes like the XP. Oh, wow. I work here. Yeah. So I work in my day job. I work in their design services group, which was called Spectrum, but is now Ethereos. And basically there at my day job, I work on a variety of projects from consumer to medical to every once in a while, like a support contract for defense. But usually the products I work on end up in shelves that you actually see, which is kind of nice. Yeah.

**Chris Gammell:** That's great. Yeah.

**Adam Wolfe:** It's really nice because of the variety of projects I work on and the fact that we don't make products in Ethereos. We help other people make products. So they don't really mind my Wayne and Lane thing on the side where I make open electronic products like kits, which is nice. But like, I mean, like the market we have at Wayne and Lane is we kind of target usually like intro, intro, kind of trying to spark like the engineering love for people who might not think engineering is for them. Like in school, like in school, as well as, you know, people who don't have an undergrad in electrical engineering and things like that, who want to play around with electronics.

**Chris Gammell:** Yeah.

**Adam Wolfe:** So it's kind of nice that in my day job, I can work with like, you know, the latest free scale processor or things like that. While then on my nights and weekends, I'm trying to like, you know, how can I drop one penny off this bomb cost in order to make this thing $11.99 as compared to $12.99.

**Chris Gammell:** So I didn't realize even that you, I didn't know you worked on the XP stuff. That's pretty cool. We were talking a little bit before the show though, about some of the other things like I asked about Android and stuff like that as well. So maybe that's one of the projects you get to work on there. I've seen you talk about that online.

**Adam Wolfe:** Yeah. One of my longest projects recently was I was working with a medical device company that makes like heart implantables. And I was working with them to port some legacy code from like OS2 that got then ported over for Windows and then basically make that work on an Android device, which was quite intense. Yeah. Not all the projects I work on are like that.

**Chris Gammell:** Yeah. Okay. That's really cool.

**Adam Wolfe:** But I mean, other things like, like, I mean, an average project for me at Digi is like a Linux driver combined with some Python combined with some hardware. And as a group, what we, what we really work on well is basically throwing a lot of radios on a project. So a lot of places will be like, we need to put a 3G radio and wifi and Bluetooth and Ant Plus and Bluetooth LE on this device. And they're like, it'll be really easy. Yeah, exactly. They're like, it'll be really easy because there's modules for all these things. And then they look at like battery life and like all the tricks they have to do. And, you know, it's like, well, this all in one solution that just fixes for wifi, then, well, when we've got wifi going, we can't have Bluetooth going at the exact same time. And so that's one of the things I don't really work on that part so much because that's more hardware and RF group stuff. And I'm more in the, in the firmware slash Linux slash Python slash Android. Nice. One thing that I'm really glad about is that in both Wayne and Lane and at my day job at Ethereos, I'm not really tied down into any expertise. You know, in terms of what I'm interested in and in terms of what the project needs, that's kind of what I become the expert in for that project, which is, which is super nice because I've had it other ways. Right. Where they're just like, well, we know, you know, this one thing and if anything, if we need that, we'll get you. Otherwise, you know, have fun not doing anything. So. Yeah.

**Chris Gammell:** Right. We need to keep you. We need to keep you available. Yeah, exactly.

**Adam Wolfe:** In case there's a really hot project that involves this. Yeah.

**Chris Gammell:** Right. Yeah. I know that I have a friend who works in defense and he says that like, you know, they have to keep capacity around for that kind of thing where it's just, you know, when they need to scale up quickly, the government stuff just demands it. That kind of thing.

**Adam Wolfe:** Yeah. Well, they do their things their own way, I guess. Of course.

**Chris Gammell:** As we have seen over and over again. Yes. Yeah. So what about, so you said you've done a little bit of Android stuff. I'm just curious about that from, you know, just from the embedded standpoint of like working with that. You know, I've, I play with it very little. I think Liquid, is it Liquid Labs who does, I played with one of their Android boards. I think it's Liquid Labs.

**Adam Wolfe:** Yeah. It's Liquid something. Yeah.

**Chris Gammell:** It's the Antipasto hardware or something like that. I remember the blog from a while ago, but. A Liquidware. Liquidware. Liquidware. That's it. Yep. Yep. Yep.

**Adam Wolfe:** Yeah. So, well, one thing that's really nice from like a non-engineering point about Android is a lot of people, when they're like, here's what we need for our end product. The answer is like, well, for how much you want to spend and for what you're looking for, we, like, we can't write this completely from scratch. It can't just be like a raw, you know, on, on the proc type thing. Right. We need it to run, like, on Linux. And then a lot of times, it's not, it's not always the easiest, like, to throw up some menus on a Linux box and have it look like it was made in 2013 and not made in, like, 1995. DOS days, yeah. Yeah. Like, I mean, it's really hard to make it not look like it's on Solaris or something like that. Yeah. And one thing that's super nice is that for a lot of things, if a person's like, you know, I got some GPIOs, I've got some audio and some video, and I just have this hardware that I need to look normal, like, that a normal person can work with and interact with, it can be relatively easy to say, okay, let's integrate that into Android and you'll just have an Android app. Yeah. And then, and then the people who write apps for that device on their end don't always have to be like, you know, I need this master in C that's got this big gray beard. Like, a lot of times, it's like, just find someone who knows Java and can crank out an Android app.

**Chris Gammell:** And he knows fonts and stuff like that or typesetting, rather.

**Adam Wolfe:** Well, I mean, it's like, it isn't the same need. And it's like, I mean, for Android with Eclipse or with Android Studio and Eclipse, they have like graphical things for changing the UI and stuff like that. And it really does, it adds a lot of value on a Linux project for us, like, a few types of projects. So that's one of the things like, that I found is where, like, you know, if you have this microcontroller and you want it to have a flashy screen, a lot of times it's easiest, you know, let's throw gingerbread on it. And you can make the screen flashy, like, on your end, and then you're not, you know, having this engineering firm, you know, charge you per hour for doing it.

**Chris Gammell:** Right, right, exactly. Yeah, and from a, you know, user perspective, too, like, that's, you know, like all the hardware people are like, no, it's got to have great specs and everything like that. And I'm fine with the, you know, command line interface or something. But then it's like, you know, get out in the world and you have real users are like, my cell phone was doing this 20 years ago, right?

**Adam Wolfe:** Well, one thing that's actually a serious issue in the industry is that when a person can buy an iPhone for 500 bucks and they have this, you know, ridiculously powerful piece of hardware that they have in their pocket all day long and they can just go and spend $500 for it. If they want to make a device like an iPhone, but they only want to make 10,000 of them, like there's an expectation issue there where we have to be like, here's what it would cost to make an iPhone. You only sell 10,000 of them. Like you think 10,000 is a huge amount, but it's not always.

**Chris Gammell:** Yeah, right. No, it's hardly ever. I mean, not for something that complex, right? I mean, like that's commoditized or amortized over lots and lots of units. Yeah, for sure. That's, yeah, that's, that's, I've seen that too, you know, with that kind of expectation. It's like, well, you know, you hire a UI designer and stuff too, but yeah, it sounds like you guys are, you have the right idea there. So.

**Adam Wolfe:** Yeah. Well, I mean, it's even the same thing in Wayne and Lane. We see this all the time, right? Like, like if we wanted to make a pocket handheld toy that costs a hundred dollars, we have this expectation that a person can buy an iPod touch for like what, 150 bucks or, you know, a few hundred bucks. Yeah. So we have this price ceiling where if like we're going to charge $200 for a kit that goes in your pocket, it better be as fancy and awesome as an iPhone. And it's like, eh, that's, it's one of the reasons why at Wayne and Lane we really hit that price floor where we've got, you know. Yeah, right. Like $18 kits and stuff like that because. Yeah.

**Chris Gammell:** Well, and you see that in the market too, right? I mean, you know, from selling to people over time, right? You see that, okay, this one sells, this one doesn't, that kind of thing.

**Adam Wolfe:** Yeah.

**Chris Gammell:** So let's, well, okay, come on, let's get to the real question here. Where the hell did this name come from? Wayne and Lane. I think I've seen it once. I think I've looked it up before because I was really confused once before. But what is the story here?

**Adam Wolfe:** So Wayne and Lane is named Wayne and Lane because one night in college, me and Matthew were, you know, trying to talk about a project we wanted to work on and we needed a name. And we realized that my name is Adam Wayne Wolf and his name is Matt Lane Buechler. And. Oh, man. Late at night, we realized that that's pretty funny slash awesome. So we made a link blog, actually, like a WordPress blog where we just anything crazy and interesting we found on the internet, we'd, we'd throw up there. And then when we wanted to make like a LLC, we're like, let's make a kit biz. Adafruit's pretty sweet. Evil mad scientist is pretty sweet. We can do this thing. We already had the domain. So that was, you know, 10 bucks we saved right there. Yes.

**Chris Gammell:** It is economical and awesome.

**Adam Wolfe:** Well, and one thing that's actually kind of nice is that there's times when it helps us look larger than we really are. Like, so if I should call.

**Chris Gammell:** Like the LLC part, you mean?

**Adam Wolfe:** Well, we'll know the fact that like if I call up a supplier and I'm like, I'm Adam with Wayne and Lane. I'm Adam Wolf with Wayne and Lane. Like if it was Adam Wolf with Adam Wolf Co. Like they would know it's just one dude or two dudes. Right. But it's like, no, no, it's, you know, I'll talk with the shipping manager. Yeah.

**Chris Gammell:** You put on your fake voice and yes, I'm the shipping manager. Yeah, exactly. Yeah, that's classic. So some of your kits are, you know, I've seen some of these on blogs around town, you know, that kind of thing. Can you tell us about some of your favorite ones?

**Adam Wolfe:** Sure. So our latest projects have been with Lego Mindstorms. So there with first Lego league and other robotics groups, there have been a massive amount of children who work on robots in, you know, in their free time. And I think that's really awesome. We think that's really awesome at Wayne and Lane. Here in Minnesota, in this year, there's 550 first Lego league teams, which is basically 550 groups of elementary school and I think slightly older kids working on robots in like a team championship type engineering competition, which is pretty impressive to me. On the other hand, Lego has its own restrictions, like as awesome as Lego is and as awesome as the brand new Mindstorms is, EV3.

**Chris Gammell:** Yeah.

**Adam Wolfe:** They're not a hardware company. I mean, they're Lego. Well, they're a plastics company, right? Yeah, exactly. And a licensing company. They're an injection molding company. Yeah. And so one of the things we did is we made a shield for the Arduino that lets you hook up everything that's in a Lego Mindstorms NXT box into an Arduino. So it lets you plug in, you know, the light sensor, lets you plug in the touch sensors and the motors and it lets you read the motor encoders and it worked with all that stuff in Arduino, which is we thought that was pretty cool because it helps provide like the rapid physical prototyping that you can achieve with Lego. I mean, you can hand a person a box of Lego and make, you know, an arm or whatever out of your robot parts with the rapid electronics and programming, you know, prototyping of Arduino. And then like there's a few other issues with Lego. Like if you want to buy a touch sensor, which is just a button, it's a push button with their end plug on it. That's something like 18 or $20. Whoa. Okay. So we're kind of working on that kind of front. Like even though they have an injection, you know, a fancy plastic case and even though they have all that stuff, we got a mold made for the proprietary plug for Lego NXT and the latest version of Mindstorms has the same plug. Thank God. So we...

**Chris Gammell:** That was a cool $18,000 you just spent, huh?

**Adam Wolfe:** Yeah. Yeah. Put it on a wall. Yeah. No joke. No joke. So we're kind of in that space right now to kind of help kids and their mentors work with Lego in a more affordable fashion for some ways. But even more so, like Lego Mindstorms is a walled garden and arguably Arduino is also a walled garden. But it's a larger one and one that a person, I mean, like you really can't overstate how widespread Arduino and hackerspaces are. So like when you're a parent and you've got this nerdy kid who really likes Legos, right? Yeah. And they really likes Arduino, right? They're like really... Like there's a pretty high chance you'll be able to find a person who just wants to talk about Arduino just in their free time and kind of help out. And that's like to tie those two groups I think will really help. Like as large as the Lego homebrew robotics group is, there are a lot of Arduinos out there.

**Chris Gammell:** So I had a couple questions about this. First off, have you had any problems with Lego yet? I mean, like that's usually the problem with walled gardens. Yeah. Is that they like them walled because they can charge admission at the door. So have you had any problems with Lego at all or no?

**Adam Wolfe:** Well, we haven't. I mean, right now at this point, if you buy our shield and you plug it into your Arduino, like all the pieces that you plug into your shield, you still have to pay Lego for. So I don't think they're probably that frustrated. I mean, it's not like they lose out.

**Chris Gammell:** Right. And they're making like 80% margin on that kind of small stuff, right?

**Adam Wolfe:** Well, I mean, like, well, the thing is, is that it also in Lego Mindstorms, they also have that brain brick that has their arm or whatever. And in the newest EV3, so that came out in September, it's actually a full Linux box.

**Chris Gammell:** Okay. I was going to ask about that, what it's actually looking up to.

**Adam Wolfe:** It's like, like the NXT is like an ARM SAM 9 or something like that. Like it's, it's a lot more powerful than the Arduino in terms of like megahertz and stuff like that. But it's also in a box and you only have like these five like output ports that you can plug into as compared to with an Arduino. I can just plug in a bunch of LEDs and drive those LEDs directly. Yeah. Right. Right. But in the new EV3, I mean, the thing runs Linux. It's got a micro SD slot in it. Like I was working on like a Doom port for it. Like, I mean, like the thing is way more powerful. And so that's also a thing that we're kind of trying to figure out where do we want to go in this Lego space over the next few years? Because as more and more people buy this EV3, they don't need like replacing the brain brick, if you will, of an EV3 with an Arduino. Like you lose functionality. It's not as awesome.

**Chris Gammell:** Right.

**Adam Wolfe:** But in the previous generation, it was totally sweeter to have this Arduino behind it because it could plug into all these other things. Right. So that's one of the times where we started to look at kind of the peripherals and what gets plugged into these Lego things and what are the costs and, you know, is there a way to bring down the costs on some of these things? Like, I mean, I think I saw a classroom pack of touch sensors for Lego that was like $500 or something like that. Oh, man. And like, I mean, like it's not that there's not value there, but I think there should be some alternatives for cash strapped teachers out there who need to provide their classrooms.

**Chris Gammell:** You don't want to be limiting kids like who really want to get into electronics or just the field, like robotics in general, just because they're trying to make money there. It's like, you know, at least have other options. It's not a bad thing. Yeah, exactly. You know, and it's, I understand why they are charging that much. I mean, I have coworkers. I don't have any kids myself, but I have coworkers who have kids. And I'm sure when, you know, Dave's son grows up too, it'll be the same way. Like, you know, it's just like, it's these nerdy dads who have this instant connection with their kids, right? And they're like, yeah, I'll pay anything for this. You know, like, first off, it's awesome. And second off, it's like, yeah, of course. You know, like, this is like, it's educational. There's, I mean, I grew up on Legos too. So, yeah, it's, I would totally open my wallet for that kind of thing.

**Adam Wolfe:** Yeah, well, I mean, and also when you look at like the schematics or when you work out the schematics for a few of these pieces, they're like, they're pretty heavy duty. Like, they have a lot of protection for, you know, if you plug in your motor port into the wrong thing and you're putting in five amps and nine volts into the button, it won't melt. Like, I mean, they really do make it so these things don't break very often. I'm certain they do break, but they go out of their way a lot more than like the average open hardware product has in terms of making this thing last. And I don't know what their volumes are. And I don't know, you know, in terms of like from their, like, I mean, there's some, well, like with iPhones, right? Like there's not, it isn't even a drop in the market compared to, you know, a large product like an iPhone. So, I mean, like, like they may not be, you know, swimming in, in like their pools of, of coins or anything like that at Lego. But on the other hand, there's, there's not a huge number of, of low cost options for adding on to Lego. And that's, that's probably a place that we'll enter. Yeah. As Wayne and Lane.

**Chris Gammell:** Well, that's great. That's great. I mean, any, any aspirations to, to go full time on Wayne and Lane eventually? Is that, is that kind of the eventual plan?

**Adam Wolfe:** Um, well, so Matthew is wrapping up his PhD. He started a job here in Minneapolis while he wraps it up. He's probably only has a few months left. That's the goal, at least for him. And then for me, at least, you know, right now at the day job, I'm like, I have enough new things that I'm working on there that right now with where Wayne and Lane is, I wouldn't be able to work on those things like the same way.

**Chris Gammell:** Yeah.

**Adam Wolfe:** So, I mean, it's a balancing act, right? Like, I mean, if I just was working on the markets that Wayne and Lane works on now, I don't think I'd be growing as fast as an engineer, perhaps in terms of like entrepreneurial efforts and things like that, I would be growing faster. But, but really it's, you know, it'll be there someday, I think. But I've got no problem with the slow burn. You know, we slowly grow year after year. I mean, we started in 2009, the fall of 2009. And we put in like 300 bucks each to make like 100 of one kit. And we said, well, if this fails, we'll just have a lifetime supply of, of this certain pick and this PCB and it'll be like no big deal. Yeah. And then, I mean, last year with our Blinkies, we sold tens of thousands of our Blinkies to retailers. And so, I mean, it's not, it's not that we're, once again, like Lego, you know, it's not like we're swimming in it, but it, it certainly pays for itself at this point. Yeah, right.

**Chris Gammell:** You get, you get the trip to Maker Faire each year, definitely. You're both, both of them paid for it. Well, sure, sure. At the very least.

**Adam Wolfe:** Well, that, and it's like, you know, if I want, you know, some test equipment or if I need, you know, to play with KiCad and have, you know, explain why I'm taking all this time and, you know, not, it might not be the most fun or something like that. Like, it's like, well, you know, I'm paid basically out of my profits from this to work on these other things.

**Chris Gammell:** Yeah. Yeah. You know, that's a really good way to look at, you know, I always, I always advise people who talk to me about it, you know, like trying to find jobs where it's like, you can just learn, like mentors are a big one too. But I think, you know, having a wide range of topics where you can kind of keep learning and stuff like that, because, you know, I've been at jobs before where it's like, when you stop learning, basically, I know it sounds bad, but I feel like when you stop learning, you're like, eventually like, well, I can go make more money in management. And that's what all my friends did at my old job.

**Adam Wolfe:** Well, I mean, like, I've worked at places where like, you look around and you realize that, that, that people lose skills over time at some jobs as compared to gain them. And then you realize the longer you work there, the less employable you are anywhere else. And you're usually not having fun at that type of job either. So it's just like a time bomb.

**Chris Gammell:** Right. Well, and another, another layer of that is a lot of people I see that like, you know, their family, families are growing and stuff like that. And then they have more kids or the kids are going to college and stuff like that. And they literally can't leave because they have all these, you know, expenses on the line too. So it's like this horrible trap. It's like, oh God.

**Adam Wolfe:** Like, I mean, like it also helps like when you can think of your job as a thing that you choose to do. Like, I mean, it isn't like Wayne and Lane would pay my same, you know, salary right now that I get at my day job. But I mean, if push come to, I could probably make it work. And that kind of really helps on the days when it's not as fun when you're just like, you know, I'm making the choice to work here. Like, like I'm really lucky that way. And I think that having the Wayne and Lane stuff helps me, you know, weather out the day job a lot better.

**Chris Gammell:** Yeah. Well, and I'm sure it's rewarding too. You know, when you do have a bad day, you can go home, work on Wayne and Lane stuff, have people be appreciative of you, you know, helping out or giving lower cost options for that kind of thing for the Lego stuff.

**Adam Wolfe:** Yeah. Well, I mean, like it also works the other way around is when like I open up my Wayne and Lane inbox and I look at the emails. I'm like, oh gosh.

**Chris Gammell:** Yeah. So I was going to ask you about that. So we talked a little bit on, I think it was Twitter about this. But so you said you had some culture clash stuff when you were trying to kind of mash up Lego and Arduino. Can you tell us about that?

**Adam Wolfe:** Yeah. So Matthew and I worked with a local author and hacker, make blogger, John. John writes on the make blog and he's written a bunch of books. He wrote the cult of Lego or he was one of the authors. And we worked with him and O'Reilly and we made a book called Arduino and Lego Projects. And we made like eight projects with a bunch of motors and inputs and we used our Lego shield and we had a whole chapter on how to like breadboard the shield up from the motor driver parts because we didn't want it to be just like an advertisement or manual for a Wayne and Lane project. Right. We had the step-by-step instructions on how to build kind of like you'd have from a Lego manual. And at the end of it, like we published it, you know, we had a bunch of sales and we realized that the people who buy books, especially like Lego books and our previous audience of people who found out about our products from make and hack a day and other places on the web. We're not necessarily the same groups. So that meant that like our website, the way that our website was laid out and the word, you know, the wording of things on our website. And even just the way that we thought our end users would interpret what we were doing weren't necessarily valid instructions. And we got some pretty – like I mean I understand, you know, like you can't read the comments and stuff like that. But we had some people who were pretty angry because they, you know, weren't expecting the same thing because we didn't – we weren't aware of the change in our audience when we changed mediums.

**Chris Gammell:** Huh. That's – yeah, that's an interesting lesson from like, you know, not just, you know, moving to Lego obviously but just kind of any kind of new market like that. Like knowing – I don't even know how you'd find that out, right? Like I think it would be the same kind of situation.

**Adam Wolfe:** Well, I mean I don't even think we – like I didn't think about that even at all. But like for you with the contextual electronics things, if you put these things on like PAC TV, you know, like on Channel 10 or whatever it is where you guys are, right? That audience wouldn't be the same audience as if you put these up on a streaming video site. Yeah. And it's not the same audience as if you had just a big torrent of them and you threw them up on Pirate Bay or something like that. Like it's – like for us, it was a thing that we learned was to think of who your actual audience is. And it sounds so dumb that we didn't think about it now. But that's – but there's so many things that are obvious after you already know them. And this is a case where, you know, a pair of engineers, you know, working on some projects, we did not think about this until after we, you know, had already released it into the world.

**Chris Gammell:** Yeah. So has it calmed down these days? I mean –

**Adam Wolfe:** Yeah. I mean like a lot of it is that when – like I think – well, I hypothesize a lot of the issue was pre-orders. So when people saw the cover and they saw just the blurb and that was all that was available on Amazon, they weren't able to flip through the book or see a sample chapter or anything like that. They didn't – like I mean it's hard to say what is everything that will be in a book. And it's hard for – like for Lego books, if you go and buy the average Lego, you know, idea, inspiration thing at a store, it will just be some projects and some Lego parts. And it isn't like, well, you have to buy these like a microcontroller board and you have to plug it into your computer and program it. Right. Right. And it's like even though it says Arduino in the cover, like we had multiple people like be very angry at us that they had to purchase an Arduino in order to, you know, work with these projects.

**Chris Gammell:** Yeah. Okay.

**Adam Wolfe:** And now there's a sample chapter on the website and if you're in a store, you're able to flip through it and see what's in it. And I think the people who buy it now know more of what they're going to get than when they – when it was just blind pre-orders.

**Chris Gammell:** Right. Yeah. So that's got to help then too. Yeah. Totally. Totally. Yeah. And that's right. I think you said that at a previous time too. You said that people are such big Lego fans that they'll kind of just go with whatever for that kind of thing, which is an interesting thing as well, right? So if someone started up like a – if you pair up with like a – I don't know, like Giorgio Armani or something like that. Arduino and Giorgio Armani, right? Yeah. Someone's just going to buy it because it's just Armani, right? I mean like that's – but then you'll also have the Arduino component of it.

**Adam Wolfe:** Yeah, exactly. Well, I mean like I think I – like I see that a little bit with glass a little bit actually. Yeah. Like with glass it's like, well, here's a thing in glass and you'll look at the comments and it's all about how like technology will like completely end our world. And it's just like – it's just because of the audience of that article now, you know, that's who is attracted to that type of thing.

**Chris Gammell:** Right. Yes. When the gadget heads come out, that's when I'm usually like, all right, well, I'm going to go back to the other corner of the internet and look at how something's made.

**Adam Wolfe:** Well, like I mean like the root problem here is that we read the comments really.

**Chris Gammell:** Yes, that is always, always the problem. I'm continually amazed that Dave continues to read his comments because he's on YouTube so much. I'm like, no, I don't want to. No.

**Adam Wolfe:** Well, I think if you have the right type of personality, even like an angry comment is still fuel, positive fuel.

**Chris Gammell:** Yeah. Oh, well, yeah. Yeah, that's Dave. So glass, yeah. So you actually got glass before I did. Have you been building anything on that?

**Adam Wolfe:** It was a little bit. So, well, one of the things is at the day job, we tied glass in with device cloud and we're, which is their internet of things type platform at ethereos. And we were kind of trying to see like what are the, what are the possibilities here to put our alert framework and things like that to just pop up on glass and stuff like that.

**Chris Gammell:** Oh, okay. So that's like how you got into the whole thing as well.

**Adam Wolfe:** Well, yeah. Yeah. I mean, that, that was one of the big, they helped finance it that, which helped a lot.

**Chris Gammell:** Yes. That does help a lot. Yeah. Yeah. So, so, so I'm curious because, you know, we have been talking about your day job a bit, but so, I mean, do you use KiCad at work as well? I don't do PCB layout at work. You don't? Okay.

**Adam Wolfe:** Nope. So we've got people who are really, really great at that. And while I play with that at Wayne and Lane and I help lay out the PCBs at Wayne and Lane, that's not something that we do really. Okay. Nope.

**Chris Gammell:** Yeah. Cause it was interesting with, you know, and then obviously aetherius must have a lot of RF stuff as well. I was really, I was, I was wigged out that when Michael Osmond was talking about doing RF on, on KiCad, it's like, I'm going to have to try that eventually. I think I, I don't, I don't know. Yeah. Yeah. I'm not a big RF person to start with. So, but. So, uh, I wanted to ask you about KiCad though, cause obviously this is something that you are very involved in. Um, so you do, you have a bunch of great tutorials. First off on Wayne and Lane has a bunch of great tutorials. And then I think, uh, I think you guys, or you also have stuff on the build, the nightly build stuff, right?

**Adam Wolfe:** Yes. Like, like I want to be very clear. I'm not a member of the dev team and I don't, I don't necessarily aspire to be either. Uh, I follow the dev, uh, list, which sometimes takes a lot of, a lot more reading time than I think I might ought to spend on it. And I maintain the nightly builds for Linux for Ubuntu. So I'm working on expanding that to the nightly, uh, Windows builds and nightly Mac OS builds. Um, hopefully by the end of this month, but I've said that I believe five months in a row now.

**Chris Gammell:** Yeah, I know how that goes.

**Adam Wolfe:** So in, in Matthew has written some really great tutorials and taught a bunch of classes on KiCad as part of Wayne and Night.

**Chris Gammell:** Uh, so could you tell us about the, the nightly build stuff then? Cause I, I, I'm always a little confused about that with, with the, uh, the KiCad side of things. So, like, sure. Does it ever break your stuff? I mean, like, does it just like, do you just like wake up one day and you're like, well, I guess, uh, CAD's not working today. Maybe better tomorrow.

**Adam Wolfe:** So, yeah, well, I mean, it's, it's pretty rare. It's, it's pretty rare that you would like open up your nightly build and then it would be completely broken. Um, it, it happens. I would say it's probably happened five times this year, but personally, excuse me, the way that I work with my own nightly build is I'll update maybe every two weeks. But one thing is, so like on, on the list, they've been talking about library table support. So basically like there was this big dream of how they want to handle. Okay. I'll back up first. Okay. So in KiCad, the standard workflow for people is you start out by making a schematic. Then once you make your schematic, you export that into the next, uh, piece, which ties like the library pieces from your schematic and ties that into your like footprints. And then you open up PCB. Exactly. And then you open up PCB new and then import the footprint and, and like the routing data. And then you place your modules and then you route and then you export out, out your files to get fabbed. Like, so that's your generic workflow. So they have had a dream about how to change the library lookup for quite some time now. And there was some recent traction, some awesome recent traction to make this happen. So one thing is, is in the very most recent builds, if you enable like a debug, like, like this may break your code switch at compile time, it will let you open up an Eagle, an Eagle library and use those parts without any sort of import process. Really? Oh, that's interesting. It'll do the same with, uh, with like, with, uh, what's, how's it pronounced G E D A.

**Chris Gammell:** Yeah. I've heard G E D E D A or G E D A. I, I, I, I call it G E D A.

**Adam Wolfe:** Yeah. It, it, it'll work the same there. And they also have a plugin framework to kind of help it make easier for other interpreter type things in order to say, here's how it, here's what their format is. Here's some code to translate it. And then they'll just natively work with it, which is kind of super awesome in my mind, because then I don't have to open and export out a thing from the Adafruit library or from the SparkFun library.

**Chris Gammell:** Yeah. Right, right. Yeah. All that, all the work that's been done in Eagle, right. It's so you can just use it immediately, which is nice.

**Adam Wolfe:** And now, now that's experimental. It's still, it's still, it's not in the production builds unless you turn it on specifically. Uh, but it worked for the board I mailed out on Tuesday, last week, Tuesday. And, and then another thing is they enabled storing your parts libraries on GitHub and on the internet. Oh. So then that way, when I pull a part in, it, it pulls it from the internet directly as compared to off of, off a mirror or a cache on my local machine. Right.

**Chris Gammell:** Right. Yeah. Yeah. I was, uh, I was looking at, I saw that there was some more GitHub support. So I just started using GitHub, uh, I think maybe because of you, uh, perhaps. Yeah. And, um, and I saw that they were, they were rolling some of that, that support in there, but it's, uh, it's interesting that I didn't realize it's for the footprint stuff. Yeah. So that's kind of the hard thing for me is like, it seems like it's all kind of, you know, I, I see you mentioning it. I see someone else. I see, uh, Robert Schutzenfeld mentioning it on Twitter and stuff like that. And it's kind of like through Twitter is how I hear about new stuff. Uh, is there, are there any like go-to places other than the dev list?

**Adam Wolfe:** No. Um, so one thing is, is the developers for KiCad. Now I have to be extremely general here and I'm talking in like vague groups on purpose because it isn't really like there's one specific person who owns the entire thing. Like that there's a small group of maybe say 10 people who, and then there's a larger group of people who have ever written code for KiCad. And, and then there's this larger group of people who use KiCad and the developers in general. Um, like there's one guy, Miguel, who's really into the Mac Mac builds and he supports the Mac builds. There's Brian and a few other people who support the Windows builds really hard. And I really hope they're not paying attention to this podcast and get really angry that I missed someone. And then there's other people who just work mainly on the Linux builds. But in general, um, the feeling is that if you want to be on the bleeding edge of KiCad, that you're going to compile it yourself. Now, I don't necessarily agree with that philosophy. And that's one of the reasons why I maintain these nightly builds.

**Chris Gammell:** Ah, okay.

**Adam Wolfe:** Is so that basically if you want to test out this latest thing for like, like this footprint support, you should be able to, I guess, as long as you know that this isn't like, like they don't have their approval seal on it is it's not going to break anything. But, but I, but it's, it's one of those things where I feel like that's not necessarily a restriction or that isn't something that I feel is, is, is helping or a good thing. So that's one of the ways that I try to help. Now, that being said, right now, my builds on my public builds are like two months out of date. Now, granted, there haven't really been any huge new features that are in production for the last two months. And it, and it's one of those, it's, it's a problem, right? Cause it's one of those things where it's like, I always have work for Wayne and Lane that I can bill basically that, that'll, you know, make the income. Yeah.

**Adam Wolfe:** As compared to working on KiCad, which it's so easy as a person who runs a kit biz or any business, really. It's really, it's so easy to get, you know, like inspecting your own processes so much that you never actually use them to produce anything. Right. So like, it's so easy to get stuck in the trap of like, well, let me upgrade my website. And you're like, let me do AP testing and let me learn CSS. And then like, you realize that this is a whole career that you're going to try to just like, oh, I'll quickly learn a whole career and then I'll move on to the next thing.

**Chris Gammell:** Right. Huh. So that's, well, that's interesting. So, you know, I've never really been, I, obviously I say all the time, I'm not a software person, but, uh, you know, even just like using, I hesitate to say experimental, but like just even open source projects, I guess. Cause there's a lot of open source projects like this where there, you know, there's a developer list and stuff like that. There are experimental builds. So it does kind of ripple through and it's easy to get excited about a lot of the features, but it's, it's interesting to hear about like how, how that does end up affecting end users like me, like just, I mean, John Q public like me that happened to build circuit boards. Yeah.

**Adam Wolfe:** Well, I mean, like, it's like, it's also, it's kind of scary in some ways too, right? That, that there's just people who, I mean, granted, they all really know KiCad well, and they really love KiCad, but they, they do this change and it could screw up your, like it could screw up your fab files. Yeah. You know? So one of the things that, that a few other people and I are working on is kind of like, let's, let's automate this for every build of KiCad. How about we like automatically like drag the mouse around and make a new PCB and then check to make sure that nothing changed in the Kerber's.

**Chris Gammell:** Yeah. So that's going to be like an automated GUI test basically where I always hear about like unit testing from software people and I'm like, yeah, yeah, it sounds like a decent idea. Yeah.

**Adam Wolfe:** Wouldn't that be awesome if we could do that for hardware?

**Chris Gammell:** Yeah. Well, yeah. I mean, I mean, you, you're talking about like, like actual like board production kind of stuff, right?

**Adam Wolfe:** Well, yeah. And I mean like you can a lot, but a lot of times like a test engineer has to follow this manual that's super boring. Right. Like, wouldn't it be totally awesome if we had a cheap and easy way to be like, turn the machine on and press this button 500 times and then turn it off and.

**Chris Gammell:** Yeah. Well, and yeah, and that's useful from, you know, even running like experiments and stuff like that. I think about like crossing, crossing parts, right? Or, or getting, getting a replacement part, you know, and you want to run it through your line a couple of times through manufacturing, you know, say I'm designing a new op amp. Even if I look at the specs, I want to, and I say, okay, that looks good enough. Right. I still want to run it through and having an automated test like that's nice. You know, oftentimes you'll use some kind of cursor data, but it's, it's not necessarily like an automated thing.

**Adam Wolfe:** So yeah, like, I mean, and not only that, the automated tools that are out there now I'm talking way outside of my expertise, but a lot of times the automated tools are not necessarily cheap, like a lab view chassis and things like that.

**Chris Gammell:** Like, Oh, Oh yeah. It's not a flying probe machine. You ever use one of those?

**Adam Wolfe:** No, no, but, but it's like, but it's like, you know, it's not as easy as in software where it's like, let's just learn about it and then download some things off the internet for free.

**Chris Gammell:** Yeah. Yeah. Right. Yeah. We should get on that. We should, we should start working on that. Yeah. So, so, so what have you, have you seen anything in the upcoming KiCad that, you know, excites you that you think is going to be a big feature?

**Adam Wolfe:** Well, one thing that's really nice is that, is that there's some people who are being paid to work on KiCad now, which is totally awesome. Yeah. So one of the features that CERN has been working on is in PCB new, I guess I've never run into this problem, but if you make a really large PCB with a lot of layers, things can get kind of slow when you move things around. Um, and they have thrown, I may get the technical wording wrong here, but they've basically thrown all of PCB news canvas. Like the part that draws the PCB into the GPU into the graphics layer so that it's hardware accelerated. Oh, wow. So that's pretty, that's pretty cool. It's, it's still experimental, but they've got people paid to work on features for KiCad at CERN, which is to me, I think that's amazing in terms of open hardware. Like, I mean, like you don't have to have open tools to make open hardware, but it certainly helps, at least in my point of view, that anyone can download this thing and, and, and have it run on their PC. Um, and to have people paid to work on it, I think is a huge milestone.

**Chris Gammell:** Yeah. Well, yeah, definitely. I mean, and, and I guess, I guess, you know, anyone just throwing their weight behind it like that is a, is a big deal, right? I mean, because that, that kind of guarantees it. I mean, and if it's a, you know, if it's a big particle accelerator group too, that probably doesn't hurt either. Yeah.

**Adam Wolfe:** No kidding.

**Chris Gammell:** Well, but they might be smart.

**Adam Wolfe:** I'm just saying to go back with like open tools and open hardware, like. In my opinion, between Eagle and KiCad and a few other free PCB tools like that, I don't think any of them are like 10 times awesomer as any of the other ones. So it, it really, like, if you are a super expert at Eagle, you're not going to be any more productive in KiCad. I don't think personally, like, like I might be making everyone feel, you know, horrible about it, but I almost feel this like the same way, the other way around. If you really know KiCad, you're not going to, you know, have your eight hours of layout. Now take one hour if you switch over to Eagle. Right. So being that they're like, like being that they work okay for hobbyists and for even, you know, small time. Pros at this stuff. It's like we, I was at a event two weeks ago, which was held by a nonprofit here in the, or it's out of Texas that helps promote education in STEM for women in Africa. So like, like, like, like I'm not exactly certain on the ages. I think they were, uh, between like 12 and 15 or around that, but they, in, in August, one of the product or one of their projects for one of their days was they worked on our blinky kits. And so they all, you know, they got our PCBs, they got all the parts, they soldered them together. They talked about like the theory and I don't remember if I've talked about the blinky kits yet on this podcast, but basically they're LED. There's a lot of LEDs on a PCB and they have a microcontroller on there. And the way that you program the new pattern is you hold up the PCB up to your monitor. And we've got this JavaScript program where you type or draw in the new message and it'll kind of blink these two squares, black and white on your monitor. And then there's a pair of light inputs on your, on the project, then read it into the, the microcontroller and it rewrites the EEPROM.

**Chris Gammell:** So that then when it boots, yeah.

**Adam Wolfe:** So then when it boots, it can, you know, scroll your name or it's good. Like we have a POV one and we have a grid that's like nine or eight by seven and that has a character table in it. And through there, basically, you know, it's, what's really nice about that is that people can help make it their own without having to know programming or without having like to have drivers or plug it into their computer. So like, like, like, like they were in Nigeria and the school that they were working in or the, the place they were working in, like the net wasn't really available. And so they had a thumb drive that had our website on it and they were able to load that up and open up in their browser and update it to scroll their name or, you know, the name of where they were or the camp and stuff like that. And it's like, you know, if you're in an area where you can't access the internet on a reliable basis, you know, having open tools, I think is kind of really awesome that if they wanted to for no extra dollars, like they can open up the board files. And, you know, and, you know, and, and find out how this thing was actually made and, and how I made the files and mailed them off and had the boards made and stuff like that. And it's like, like, to me, that's really kind of, it's, it's, it's changed what, what kits we do, because we go out of our way to make sure that if you have basically no resources that you could still redo our work. You know, like, like, like one of the things is for this blinky kit, we use a pick on it and we have like the free pick a compiler and we use up to, I think all but the last four words of memory and this pick. And we could shave off, we could add more features into it. We could expand the font table. If we went with the pro compiler that would only cost us like a few hundred dollars. But then the problem is that other people wouldn't be able to re recompile the firmware without paying that few hundred dollars. And so it's, it's, it's one of those things where it's like, as long as we can rebuild it with free and open tools, I mean, and it's still cool. It's, it's like, we might as well. At least that's our, that's our feeling here at Wayne and Lane.

**Chris Gammell:** Yeah. Well, it's like you guys are making gateway drugs to the, to the tech world, except then you don't, you know, charge in the backend. No, that's, that's really great. I didn't realize that the, the, the blinky kit was programmable like that. That's really cool.

**Adam Wolfe:** Yeah. And I mean, we have sold so many of those that when I just think about like how many people have been introduced, you know, or have, have picked up a soldering iron to make them because we don't have any that are prebuilt. So the fact is that there were, you know, 15,000, 20,000 or more, some people who soldered one of these together. It's like that, that I think it's a pretty awesome statement about our world, I think. Yeah.

**Chris Gammell:** And it can, I mean, it can only stop at about what, 7 billion or whatever it is. So that's, that's awesome. That's really awesome. What else? Let's see. So we did have a question to go back to KiCad real quick. Okay. Kind of jumping around here, but someone who wrote this in, MK Johnson wrote in about the, the Mac side of things. So you said there's someone who is, is working on Mac stuff now, but I've heard this from other people too, where Mac, Mac stuff might be a little bit less stable. Do you know anything about that on KiCad?

**Adam Wolfe:** Well, I think like, yes, I know there are stable builds from Miguel. I'm not sure if they're, they're easy to get to or easy to find. I will take that as an action item to make sure that his builds are available on the KiCad website. I don't have control of it, but I can email, hey, let's make sure this is up there. Um, I know that the KiCad folks don't really care about making stable releases for end users. Like, like they would much rather say every single release we make is stable and that by them having a stable release, they're implying that the ones that aren't stable releases aren't stable.

**Chris Gammell:** That's, that's, are you sure there's no one managing that? Cause that sounds like they're trying to impress a manager. That sounds like something I'd say would work.

**Adam Wolfe:** Well, well, I mean, like it's like, it's because they have these feature branches, basically they have these, these, these switches that at build time, they just don't add this code in that. That's been how they've been throwing this experimental code in. They've been saying that this is experimental, but you have to turn it on specifically at build time so that if you don't turn it on, it has the tested code that we have. And it's one of those things where, you know, once you have a stable release, then there's a lot of questions about like, okay. So once we have a stable release and we fix a bug, do we make a patch or do we re-release it? Do we, you know, what features get included? What ones don't? And so instead it's more like we've got these, we've got this mainline branch. And right now, every once in a while, it'll be broken, but it's, it's very rare and it's usually fixed within minutes. And, you know, they go out of their way to make sure that works. And then if they have experimental code, they kind of hide it away, but keep it in that kind of mainline. It's an, it's an alternate way of making code is the stable. And I'm certain I, well, I take that back. It's very likely that what people, what happens is people download the latest stable release. What's late, what's labeled the latest stable release. I don't, I do not think that's from even 2013. I'm not certain, but, but I think it is probably quite old. So that may be one of the issues that they're having if they're on, on OS 10 and it's not stable. Like I know that the KiCad build box that we purchased at Wayne and Lane is a Mac mini because we wanted to make sure that we could put a windows VM on it and a windows and, and a, and a, and a Linux VM on it. And then also have it test the, like the OS or the Mac stuff as well. So I tested a build for like a PCB and it worked fine. So I, like, I mean, I guess I'll make sure to poke the appropriate people to make sure that, that Miguel's builds are available.

**Speaker ?:** Huh.

**Chris Gammell:** I guess, yeah, I guess the thing that's amazing about it, it's like, cause it, you know, I've been using a lot more obviously, but you know, I, I, I'm continuously impressed that it, you know, for, for being open source and a lot of open source projects are like this where it's like, man, this is like, it's still got a lot of stuff in it. Right. I mean, like, and, uh, you know, just, I guess distributed workforce is still, still amaze me. That's this, that's kind of the short and long of it.

**Adam Wolfe:** Well, I mean, basically like the key is, is you find people where it's a super important part of their life that they work on this thing. And as long as they can work together, it's pretty surprising, right? I mean, look at Wikipedia. Right.

**Chris Gammell:** Exactly. Right. Right. And there are power users there too. Right. I mean, like it's the same kind of thing, right. Where there are big contributors and there's smaller contributors, but it's still, still gets the job done. Yeah.

**Adam Wolfe:** As a student at, uh, in college, I worked in their math department, uh, in their like IT, in their Linux box group. And we had a professor at that department who we had a game where we would try to find any math related article that he was not in the edit history of. And so, well, I mean, to be completely honest, after we, after we were playing this game, we're like, let's find out how many edits he has personally made. And he was 12 or 10 in the world for number of edits that he had made. Wow. And it's like, that just means that it was super important to him to make sure to make, I mean, not only is he like a professor in it, which means like he's probably qualified, you know, like to do these things. Like it was important for him to spend his, like he, he chose to spend his time on this planet adding to Wikipedia is compared to whatever else hobbies he might have. And I think that's totally awesome.

**Chris Gammell:** Yeah. I see. I think the thing that's rising up in me is like, like, uh, I, I want to meet other people. Like, obviously, you know, you, that's good. Uh, and, and I know other people online and I know a couple of people in real life who like high cat, but like the thing that's rising up in me is like, like, there should be like a conference or something. Right. I mean, like I should buy people who are working on this a beer and I should be able to, you know, I want to like go and chat and, you know, like, you know, that's how conferences start. Right. Yeah. That's all I can think about. And so, uh, I know it's all over the world, but we could have it like New York or something or have it with like a maker fair meetup or something like that. I don't know, but. Yeah. I'm sure that at some point that'll eat up, eat up time as well. I'm sure I'll jump on that eventually.

**Adam Wolfe:** In like, in like 10 years, we'll be complaining about like, Oh, we got to go to the ChiCAD conference. Got to make, got to make a booth for the ChiCAD conference.

**Chris Gammell:** There's, there's worse things to, uh, to, uh, complain about, I suppose. Oh yeah. Yeah. Yeah. I mean, well, maker fair. I don't complain about that. I got to get back. I didn't go to New York this year. I went to the open source hardware instead, but, uh, seems, seems like the New York one was a success. You were, you were there, right?

**Adam Wolfe:** Yeah. Yeah. I was, we actually spent the most time walking around at this maker fair than I think any maker. So than any fair we've ever been to. So we've been going to maker fair since Wayne and Lane started. So like since 2009 or 2010 and you know, it's, it's kind of like changes terms of like, which ones, like how much time we spend at our booth as compared to how much time we spend walking around. But we spent a lot of time walking around at this one and we had a great time. Like, I mean, it's, it's just, it's like, it kind of, it's, it's almost sad that when you're at your booth, you're like, I bet there was all this cool stuff I could have seen. And then when you're walking around, you're like, oh, I bet there'd be all these cool people I could meet at my booth. And it's like, like, like, I mean, I kind of wish I had a time turn or something like that. So I could spend the whole time at my booth and then also spend the whole time walking around.

**Chris Gammell:** Like, I mean, I get totally freaked out when you run into yourself.

**Adam Wolfe:** Oh, I mean, I spent 45 minutes at maker fair at my booth with these three girls from Long Island who were working on a first Lego league team. And they were like, well, we were originally with the school one, but there were all these people at the school ones who were, you know, like, they weren't very good. So we kind of made our invite only private team. And like, it just blew my mind that there's these three, you know, preteen girls who are debating, like, like drive styles that we can put on a robot. You know, like, oh, I think we should have a tank or I think we should drive from the rear. I think we should have three wheels in the back. And it's like, it just blows my mind that, like, I mean, I'm not that old, but when I was a kid, we didn't really have that type of infrastructure in society, like, to support that type of thing.

**Chris Gammell:** Right. Yeah, it's like, it's like you want to bottle that up and kind of take it with you. And it's like, you watch the news one day and you're like, oh, God, everything's terrible. And you kind of like pop the top on it. Like, okay, we're cool now. Yeah, it's like kids in the world doing this stuff. It's like, we're going to be okay.

**Adam Wolfe:** Yeah, exactly, exactly. Like, there are like, like, I mean, if you've ever had a chance to stop at one of the first Lego League championships, I would go out of your way to find one in your region and go to it. Like, the ones I'm at, they have like a DJ. They have music pumping. Like, they have like the lights down and there's like lights flashing and people are screaming. And like, there's scoreboards that are live updated. And like, like, in first Lego League, a lot of the times there's like this like live coding piece where like you have to update your robot manually and you don't know what the changes are going to be. I mean, it's just, it's mind blowing to see people in, you know, elementary school and middle school completely jacked up about programming and robotics. Robotics.

**Chris Gammell:** Yeah. So, so yeah, and it's first Lego League. So, it's actually part of the first robotics, like the, the, the high school competition, right? It's like the, the precursor to that. Yeah.

**Adam Wolfe:** Yeah. It's one of the like, like, you know, entry pipes that after they do this, they'll graduate on into first leg or first, first robotics and stuff like that. Yeah.

**Chris Gammell:** That's intense, man. Oh, yeah. I've seen, I've seen documentaries about the, or maybe not documentaries, but just videos of the, the regular, the first stuff. I mean, it's just like, yeah.

**Adam Wolfe:** Yeah. Like, I mean, it's like, and that's kind of nice. And like, I mean, I don't like, I mean, I like first as well, but I just love the age thing. It's like when I was in fifth grade, pretty much, I think all I cared about was SNES games. I think, I think that was the big thing then. It's like, I want to be linked to the past, which is by far the best of all the Zelda games. Yeah. That's one of my favorite. And it's like, and I could like, had I been in fifth grade now, I guarantee I'd be like, oh yeah, I made my private first leg of league team. Cause the school, I just let anyone in. It's like, oh man, just mind blowing.

**Chris Gammell:** It's going to be, it's going to be intense too.

**Adam Wolfe:** It's like, what does that pipeline look like? Like, I mean, right now, like it's like not, not to take this the wrong way. Right. But a lot of engineers have histories that are pretty close. Like that, that's one of the problems I think with engineering or one of the issues that engineering has right now is that if you look at, you know, an engineer who's in their thirties in the United States, they, a lot of them are a lot like the other engineers who are 30. And, you know, in the United States working as engineers. Yeah. And when you get people entering the whole engineering pipeline who are just, you know, just jacked up about robotics from age eight on, it's like, what does that mean for what, what engineering will look like? Like both inside the workforce and outside, like, I don't want to like hit it too big picturey, but like a culture of making, like people used to make their own TVs. Like that was just the way that you got your TV to go and people would, you know, fix tubes and stuff like that. And I mean, what would that mean when you have people who are like, oh yeah, I just did robotics for like five years as a kid growing up. And I understand breaking down a problem into a control structures. Like what does that change outside of just programming? What does that change in society?

**Chris Gammell:** Yeah, I, I, I, I don't know. I think I, you know, the TV points interesting because I feel like that, you know, the, the Heathkit stuff, like, I feel like that was more necessity. I'm not sure that the, the kit building of like TVs and stuff is as much, but like, even just from a, you know, general population, say, say maybe 10% of these kids end up doing robotics later or engineering later on. The other 90%, I don't care that they're not doing that stuff because they have, like you said, they have that, that problem solving ability that that's, what's really valuable there. And if they take that into medicine or, you know, law or, or, you know, creative writing or anything like that, it's like, I don't, I don't care. That's awesome. Yeah.

**Adam Wolfe:** Well, exactly. Like it's like, as a person who also writes programs, it, like, it makes me really sad when I see people open up like a document and alphabetize a thing by hand. Like, like this happens all the time.

**Chris Gammell:** Here's how to make Adam sad.

**Adam Wolfe:** Right. Like, like, I mean, it happens all the time that people alphabetize things on their computer by hand. And it's like, what does it mean when not only, like, I mean, like there's one type of, you know, I can open up Facebook. Like, I mean, I love the fact that my grandma is able to email me. No problem. I love that. Right. But, but, but what does it mean when like people understand breaking down problems into things that a robot can solve? Like, I hope that that has like these deep seated ramifications that like, you know, the Arab spring of everybody understanding programming. Like, I think that would be totally sweet.

**Chris Gammell:** Yes. The robot spring. Yeah. The robe springer. Yeah. Yeah. You know, the, the other thing that I think about this stuff is like part of me, so I've said this on the, on a past show as well. Where like, when, when I recognize it's something like is making me kind of clam up and feel like protective about, about engineering, like, oh no, like these people are going to come in and ruin it. That kind of thing. Like, that's usually a sign of like positive change. Like if something frightens me, if it's, if it's that drastic of a change that it frightens me, usually I have to take a longer look at it and actually realize that, no, this is a good thing. And it means that it's going to make, it's going to make you and me run faster when we're, you know, 50 and these kids are the, the, you know, the new, the new hotness. Oh, I don't even think of engineering world. Right. Yeah.

**Adam Wolfe:** Well, well, well, yeah, exactly. It's, well, it's, it's the same way that like, there's a lot of kids today that don't know where their food comes from. Like they don't realize that the hamburger is made out of a cow or that like their food comes from this farm and it's processed or, or just is mostly processed or whatever. Like the fact that they don't, that there are a lot of kids that don't know where their food comes from and they have to go out of their way to make this like a thing in a curriculum that we go over. Like what are, what are common ingredients and things that you eat and where, you know, where do they come from?

**Chris Gammell:** Multidextrin does not grow from the ground. Well, exactly. So it's like, so. Not directly.

**Adam Wolfe:** So it's like, you know, the same type of way that when more people, even if, you know, a person buys a blinky kit for me or hits a camp that has a blinky kit in it. And if they don't become an engineer, that, that isn't necessarily a failure just because they now know, you know, how they now know what, what goes into making the things that they have. Like, and I mean, not only that, like, I love this story because it's a hundred percent true, but my brother-in-law, he was like 16 or so, you know, at home with, with, with his parents and their TV broke, their flat screen TV broke. And I'm like, you know, honestly, of all things, I'm like, it's probably a blown capacitor as a joke, right? It was, it was, he, like, he bought a soldering iron. He, he got like a, like a $20 exact replacement for this capacitor, which, you know, is $19 probably too much.

**Chris Gammell:** But on the other hand, no specking necessary.

**Adam Wolfe:** On the other hand, he fixed his TV. Like in, you know, 2010, they had a multi-hundred dollar TV that was completely broken. And he went to go ask to find out how much it would be to fix it. It's like, it's like 500 bucks. You might as well buy a new TV for 500 bucks. And he spent, you know, $20. He got, you know, like a Radio Shack old school fire starter iron and fixed his TV. So it's like, like that skill on its own has some value. Yeah.

**Chris Gammell:** Well, and not, not to mention the, uh, the positive reinforcement and the dopamine dump that happens in your brain. You were like, oh, I have changed my environment.

**Adam Wolfe:** Yeah. Oh yeah, exactly. Like, like, I mean, when you make stuff, like you're basically like, like you're taking your will and expressing it in the physical world. Like it's kind of, it's kind of sounds pretty psycho when you say it that way, but like, it's basically raw manifestation of your will in the environment. Right. It's like.

**Chris Gammell:** In the form of blinking LED, right? That's what we always talk about. In the form of a, of a hello world. The power of the Arduino is, is almost completely captured inside the blinky, right? That's, that's the, that is the gateway drug. That is the first dopamine dump.

**Adam Wolfe:** Well, I mean, even more than that, like, like my wife and I, I don't even think we were married at this point. And I'm like, I need you to promise this to me. I'm like, for the rest of my life, I'm going to say, Hey, come look at this. I just spent three days doing this. And every time it's going to look exactly the same to you. It's going to be a blinking light and you won't be able to tell them apart without asking me why they're different. But I need you to be like, that is awesome. And to this day.

**Chris Gammell:** That is so much better than last time.

**Adam Wolfe:** She's like, like to this day, it's still a thing where it's just like, that's awesome. And I'm like, that is going over the internet. Or that is, that, that microcontroller was programmed by audio waves. I have an audio bootloader on that thing or, you know, or whatever. Right. This is running on a spark, you know, it's on wifi or something like that. Right. Every time it's a new architecture or a new, you know, what with the Galileo, it'll be like, that is an Intel processor that I am making a blinking LED.

**Chris Gammell:** Like, yep. You know, well, that's also a sign that you, you've got a keeper there. I mean. Oh, I do. I do. Any, any significant other that will, you know.

**Adam Wolfe:** Well, let's be honest. Humorous. Like, Wayne and Lane has really helped. Like, it really does. Like, I kind of like the fact that there's a pretty low barrier of entry with Tindy and stuff like that. Like, I'm not saying everyone should make kits. But if you're really into DIY electronics, it's possible to make it pay for itself relatively easy compared to a lot of hobbies. Like, I've got a friend into, like, glassblowing. Yeah, it's pretty hard. It's pretty hard to just, like, oh, I'll, you know, put $200 in and I'll make one thing and sell that and make two things and eventually have a whole workshop. But it's pretty tricky to do that. But on the other hand, between, like, Tindy and a few other options online, you know, it's pretty, it's relatively easy. Osh Park, right? Like, I can make a PCB for three copies of it for $5 a square inch and get it back in 10, 12 days or something. Whatever he quotes now, it's, like, mind-blowing.

**Chris Gammell:** Yep, I've got one right here. I'm looking at it right now.

**Adam Wolfe:** Yeah, I mean, like, my dad was an electrical engineer or is an electrical engineer. And, like, when he graduated from college in the 80s, you know, he had these ideas for new amplifiers and new, you know, like, designs and things like that. And, like, he even looked into, like, what would it cost for me to do, like, a quick startup to make this one prototype for this amplifier? He's, like, well, I need PCB layout software, so that'll be, like, five grand and I need, you know, I need to make some PCBs. Yeah, yeah. He's, like, I need to make some PCBs. So that's going to be, like, well, probably only, like, $1,000 setup cost. And, you know, and it's, like, these days, it's, like, oh, let me go download Eagle or KiCad and I'll make a PCB and crank it off for $20. It's, like, it's mind-blowing how low the barrier to entry is at this point to get into this stuff.

**Chris Gammell:** And now we turn to the audience. We say, and so why haven't you done it yet, guys? If you haven't, today is the day. Head over to Wayne and Lane and look at KiCad tutorials because those are great. Or even just jump in with a Blinky Kit. And you guys got the game, what's the game kit as well? The Video Game Shield.

**Adam Wolfe:** Oh, Video Game Shield. So that is a pretty awesome shield for the Arduino Uno. Well, it's for any AppMega 328 pretty much. And it lets you do black and white TV RCA style. So, like, plug into the back of your old school TV type thing. It lets you do black and white video, black and white text, and audio, bit-banged audio, of course. So tone and stuff like that works. It lets you plug in two Wii Nunchucks into it and control those, read the accelerometers, and stuff like that. And it's, like, $20 or something like that. But what's really cool with that is that, like, the Wii Nunchucks snap into the board. So that's kind of a cool thing, like with the edge of the connector.

**Chris Gammell:** Oh, really? So is it like a – oh, it's like a PCB edge, you mean? Yeah. Oh, okay. Cool. I was going to say you had to, like, reverse engineer the Nunchucks. I'm guessing those are not very friendly.

**Adam Wolfe:** Well, you know, it's actually – it's just I2C. So it's not too bad. Oh, okay. The only problem is that they're all hard-coded to have the same address because, like, the Wiimote is the master usually. And so if you think about it, anything that plugs in the bottom will be a slave, and you can't really plug in a lot more than one. Right. So all of them – we have, like, a switch chip on there where we basically just – I2C is great that way, right? Like, we can talk to one of them. Then we just switch over our chips and talk to the other one, and then we can go back and forth.

**Chris Gammell:** Right. Like, I mean, it's all packetized anyway. Well, it's all packetized. Yeah, and if you're playing Pong, it's not a big deal, right? Yeah. It's not – yeah, that's really cool. Yeah. Yeah.

**Adam Wolfe:** Yes, we've got, like, Pong, and we've got snakes on a plane type thing, which is just snakes. But then we also have snakes on a torus where, like, you wrap around on top and bottom. And snakes on a sphere where you only wrap around on the side. We thought we were pretty clever.

**Chris Gammell:** Oh, plane like a flat plane? Yes, exactly. Exactly.

**Adam Wolfe:** Yeah, so snakes on a plane, if you hit the edge – it's that snake game, right? Like every old phone had or calculator.

**Chris Gammell:** Right, right. YouTube has it.

**Adam Wolfe:** Yeah, exactly. So now, like, if you hit the edges on snakes on a plane, well, like, you die. But then we made snakes on a torus, like a donut, which wraps around at the top and the sides, right? Yeah. And then you also have snakes on a sphere where the top doesn't wrap around, but the sides do.

**Chris Gammell:** Nice.

**Adam Wolfe:** Yeah. Nice.

**Chris Gammell:** That's a nice play on words.

**Adam Wolfe:** Oh, man. Oh, man. Like, the clever play on words for us is, I think, probably, like, 10% of why we do it.

**Chris Gammell:** So you guys have any other boards in development or any other plans for your future?

**Adam Wolfe:** Oh, we've got a bunch. We just showed off a thing at Maker Faire. It was kind of like a private secret thing because we're not – it's not for sale yet, so we didn't want to make everyone excited about it. But one thing we're working on is we work with the chip kit people kind of a lot. So that is PIC32 Arduino.

**Chris Gammell:** Mm-hmm.

**Adam Wolfe:** So that is Microchip and the crew make PIC32 Arduino stuff. And there's a board called the Fuberino Mini and the Fuberino SD, which come out of a hackerspace collective in New Jersey called Fubar Labs. And also co-designed by a guy here in Minneapolis, Brian Schmaltz, who makes – who's Schmaltz House. He makes a few things with SparkFun, like the EggBot board he makes. And he makes a few, like the Big Easy driver and a Bitwacker type thing. He's got a bunch of stuff on SparkFun where they make his products for him and he gets a kickback. Yeah. And he does some stuff for Fuberino. And we made – we tied in an audio codec chip with the Fuberino Mini. So that is basically a pretty good audio DAC and ADC on a chip along with everything you need to drive, like a microphone and 8-ohm headphones or whatever. Uh-huh. And we just have – like we're kind of working on, you know, kind of the hello world of audio that's Arduino-ish type compatible. So you've got your delay and you've got your echo and you've got your distortion type pedalee type stuff.

**Chris Gammell:** Yeah, yeah, yeah.

**Adam Wolfe:** We're not quite sure how we want to market it. It's not a DSP, right? I mean it's not – it's not meant for DSP stuff.

**Chris Gammell:** So sampling or anything like that is just introducing – well, I guess it would be sampling, huh?

**Adam Wolfe:** Well, yeah. So, I mean like you could – like we added some SRAM onto there. So like for delay, it can delay three seconds, I think, and we can stack that up. Oh, that's not bad. I mean we can stack that up actually pretty far, I think. It's pretty much just dollars that you want to put into it for SRAM chips. Yeah, right, right. It's like a buck for like – yeah, I mean we could put –

**Chris Gammell:** SRAM just for fast access kind of stuff? Is that why?

**Adam Wolfe:** Yeah, well, like so actually Microchip makes a really kind of nice I2C SRAM.

**Chris Gammell:** Ah, okay.

**Adam Wolfe:** It's like eight pins. They have actually SOIC and DIP and a few other smaller forms. But basically they have a new one out that's – I think it's like a quarter megabit, maybe half a megabit. So, I mean it's got quite a lot of space. And if your audio is 24-bit or 16-bit, they're just stackable on I2C. And you can – no, they may be spy. They may have both. But either way, but I mean like it's like one pin to throw another one on there. And once you've got a few, you put a multiplexer on it and you call it a day. And you've got an audio ring buffer that you can put a whole bunch of audio. And then once you've got that ring of audio, all your effects are pretty straightforward, right? You've got your delay and echo and –

**Chris Gammell:** Right. You just grab different memory locations and then you kind of skip through the time effectively, right?

**Adam Wolfe:** Yeah, yeah, exactly. So, like we made – like our example had delay and pitch shift with like the idiotic style where you just change the speed of your read and write pointers. So, I mean like you can sound like a chipmunk or sound like James Earl Jones on –

**Chris Gammell:** So, you just said skip like skip between them effectively? Yeah. Like you have your second memory location?

**Adam Wolfe:** Well, so I forget what this technique is. It's like the line drawing algorithms. But basically like you index into the pointer. Like let's say you have a pointer that's – or an array that it can be indexed in eight bits, right? Well, if I make a pointer into this array and let's say I make it be 10 bits, then I can kind of fractionally assign through fixed point. I can interpolate in between here. So, that way I can go like 1.2 samples per iteration and I can basically add. And then when I need to index in, I just truncate off the bottom two bits and index into the pointer. So, that's – like I forget what the name of that technique is.

**Chris Gammell:** Sounds like decimation almost. Yeah. Like for DSPs type stuff.

**Adam Wolfe:** Like I mean like so we have this –

**Chris Gammell:** You oversample and you take stuff out and that kind of thing.

**Adam Wolfe:** Yeah, exactly. We don't read one for one, right? So, for every 10 writes, we might do 12 reads. Well, that will slow you down a little bit.

**Chris Gammell:** Yeah. Right? I can see that. Yeah. And, you know, I don't see a lot of that stuff with Arduinos either because, you know, I mean usually the ADCs, DACs were always – you know, the built-ins at least is what, 8, 10-bit kind of stuff.

**Adam Wolfe:** Well, and even so, you're RAM limited so tightly, right? Right. You've got like –

**Chris Gammell:** Exactly, exactly.

**Adam Wolfe:** So, like the Fuberino Mini has like 128K of memory. Yeah. Or of RAM. Right.

**Chris Gammell:** But this debate – basically my point was like that opens up an entirely new group of people who have already been hacking, right? I mean you look at any, you know, group of musicians, there's going to be – if you've got 100 musicians, there's going to be like three or four guys who are, you know, tinkering with pedals anyways, right? Oh, yeah. Just doing analog, switching out. Like I remember the first guitar pedal I ever got was modded by Analog Man, which was basically switching out for like some very specified JFET op amp, which when I look at it now I'm like, okay, whatever. Yeah. I paid 20 bucks extra for that. But, you know, it's like doing that kind of thing where you're – basically it's the – it's like your brother-in-law fixing a TV. It's, you know, switching out a diode or a transistor or an op amp, that kind of thing, and there's a lot of value to that group. And then you can kind of pull people in from that community and, you know, maybe simultaneously disrupt, you know, the entire guitar pedal industry as well. Yeah.

**Adam Wolfe:** Well, we won't have monster cables. There won't be any like plating of gold on our, you know, as cheap as possible enclosures, which means I'm certain there will be a huge crowd that will say that it's absolute garbage. But – Right. Oh, I didn't just offend, you know, a huge segment of people. But anyway –

**Chris Gammell:** I'm not on here, I don't think. If they did, they're welcome to be offended.

**Adam Wolfe:** But, yeah, well, like so that's the thing where it's like, you know, how can we make it easier to play around with audio type stuff for people who don't want to learn DSP and they don't want to, you know, have this huge program on their computer, but they just want to add, you know, or even the amount of people who want an Arduino just to play back one little sound effect. You know, it's like maybe we can just say you can just store it here in your RAM and call it a day.

**Chris Gammell:** Yep. Nice and easy. No SD card or anything else necessary with all the other type of stuff. Yeah. That's great, man. Yeah. I think that's a good guiding principle too. It's like, yeah, just make it more accessible. If you just keep doing that, everything is going to just be fine.

**Adam Wolfe:** Well, I mean like there's a few directions that a place like Wayne and Lane can go, right? Like we could just make, you know, $20 kits for like forever and just aim at the people who want to get into this stuff, but they don't want to throw – like we have an SMT Blinky where we just said like how can we make a kit as cheap as possible? So these people who are so scared of soldering SMT that we can just make a three-pack. And so if they burn something up, they don't even feel bad. Like let's make it as cheap as possible.

**Chris Gammell:** Yeah. That's good.

**Adam Wolfe:** But then the other direction like we can go is say, you know, like how can we make a $300 board really, really cool? Well, it's cheaper for us to iterate on the $20 products. So that's where we're hanging out right now. Right.

**Chris Gammell:** You never know the future though, right? Yeah. And that limits your market size too, right? So like if you want to get 100 people doing something, you know, it's going to be easier with $20 than at $300. Yeah.

**Adam Wolfe:** Well, one of the things we try with our like intro kits that we aim at kids actually, I make sure that I work – like I keep saying I, but Wayne and Lane is a we thing. We make sure that when we make a new product that we can have a bunch of 12-year-olds build it in a workshop. Oh, really? Because if they can't put it together, 12-year-olds will usually read the instructions more often than adults will. Because adults will usually think they know what's going on. Right. And kids will usually be like, oh, I guess I'll glance at these instructions. Right. So, you know, like we make sure that kids can produce these things. For a few of our kits, we've just made a whole bunch of them and then just mailed them out on the internet to people and said, hey, would you build this? And then find out if they build it right or not.

**Chris Gammell:** Yeah. Yeah. That's the way to do beta testing, I suppose.

**Adam Wolfe:** Or Maker Faire is like the perfect way for us to test our projects because a lot of times we don't have enclosures. So, if our products can last being handled for a whole Maker Faire, then that means they're good because they're going to get dropped. They're going to get – The peanut butter test. Oh, they're going to get chewed on. I mean –

**Chris Gammell:** Yeah.

**Adam Wolfe:** Oh, man.

**Chris Gammell:** That's great. Yeah. Well, that's awesome. Yeah. So, wayneandlane.com is where people can find all the projects, right? And your site is – feels like burning.

**Adam Wolfe:** So, I've got Feels Like Burning. I haven't posted anything up there for probably a few years except for just what I read once in a while. Okay. Every year at New Year's, I say like, oh, man, I should really work on my blog and I post like two posts.

**Chris Gammell:** Yeah, I know how that feels.

**Adam Wolfe:** And then it's like – like last year, it was I should really post on G+. So, like if you look in January, I posted like 60 times to G+.

**Chris Gammell:** It's like – well, I say that about working out too. I just start working – you know, I get the two months of working out in. Oh, yeah.

**Adam Wolfe:** I mean, realistically speaking, you average that over a whole year. It beats not doing it for two months. So, it's like at least I have at least a few posts every year.

**Chris Gammell:** Yeah, right.

**Speaker ?:** Yeah.

**Adam Wolfe:** So, actually, one thing. Do you mind if we hand out like a 10% off like for anybody on this podcast? No, no.

**Chris Gammell:** That's great. Okay. I love that kind of stuff.

**Adam Wolfe:** So, then let's figure out what we should make that because I haven't done that yet. So, actually, so if you go to wayneandlane.com slash T-A-H, that can be our landing page. And it's not up yet because I just thought of this right now. So, let's do slash T-H-H. And then the code will be T-A-H-O-C-T for October. And I'll make that 10% off anything in our store until November 1st.

**Chris Gammell:** Nice. So, if you're listening in November, you should subscribe to the Amp Hour so you get this sooner. Yes. You should have done that, guys. Sorry.

**Adam Wolfe:** Well, actually, we could make it through November. Oh, damn it. Okay. We could make it through November if you want. What do you think?

**Chris Gammell:** No, it's okay. Well, let's see.

**Adam Wolfe:** Well, what do you want to do? Would you want to promote people having this play right away when it comes out? I think so. Let's lock it down to October. Yeah, let's just do October.

**Chris Gammell:** Yeah. Okay, so T-A-H-O-C-T. Yep. Yep. That's awesome. Yeah, and I'm sure that a lot of people – I think I got – now with this blinky thing, I got to try this with the screen programming. That sounds awesome.

**Adam Wolfe:** Yeah, it's pretty – when we came up with that, it was – we spent, I'm not joking, a year. Two college graduates spent a year on the screen transmission because – like, I mean, you would – Was it JavaScript? Well, yeah, it was JavaScript. But, no, like, would you – like, at first we wanted one – like, a protocol that clocked on its own, right? Like, we wanted one so that we'd have one input sensor on the screen, and you'd hold it up to your monitor, and it would just blink, and we'd have some clocking protocol like Manchester or, you know, a thing that we could figure out a clock based on the transitions. Yeah. Well, at the time, if you told a computer to blink a square through JavaScript every – like, at 10 hertz, it would do that over the long run. Right. It would do 10 hertz.

**Chris Gammell:** Average itself out.

**Adam Wolfe:** But you would – on a regular basis, it would be white for one second or two seconds and then blink 50 times in 100 milliseconds.

**Chris Gammell:** JavaScript sucks.

**Adam Wolfe:** Well, I mean, I'm certain it's better now because this was, like – honestly, like, iPhones were kind of new, like, when this, like, is a new thing. Like, I'm certain that the web browsers are way better today, but it was just – like, I mean, it's understandable to me that blinking a square accurately at 10 hertz or more is not a design requirement of web browsers. What do you mean?

**Chris Gammell:** That's how they used to sell stuff, right? With, like, blinking ads, so.

**Adam Wolfe:** Well, see, I guess sometimes, though, you just say the faster we can blink, the better, right? So your eyes attract to it even more. But, like, so, I mean, the amount of time that we spent looking up line encodings on Wikipedia, old textbooks for, like, let's – like, I mean, the amount of time. And then, furthermore, after we have this protocol, right, we're in microcontroller world, which runs at a new – a higher speed than humans. So I'm – like, so we've got raw data dumps where we're just logging what a white square looks like. So LCD backlight usually works by – they pulse width modulate a backlight behind, like, the screen. So if it's running at, let's say, half brightness, that means you've got, like, 120 hertz of noise blasting at the same time that you've got a carrier wave at this certain frequency. And then you've got fluorescent lights above you that are going at 60 – Right, blasting 60. Blasting a different 60 hertz. And at the time –

**Chris Gammell:** Plus all the garbage at the high end, the high frequency stuff from the switchers around it, too.

**Adam Wolfe:** Oh, it's like – like, so, I mean, just the raw reading the actual light values from your screen, if you don't turn your screen brightness up to 100%, you will get – I mean, it's almost impossible to tell off from on. And it's like if we were to average that out, we would drop our – we'd, you know, drop our data rates. So long story short, kids, the reason why, like, there's no other products out there that blink things up on your monitor is that it's a huge pain in the butt. But, I mean, we collected a massive amount of data from CRTs, and I did it from TVs and LCD types. And we've got a pretty good filter that does pretty good. But, I mean, we've had people pretty angrily talk to us and say, like, I can't get this to transmit. There's nothing I can do. And the first thing we say, no matter what, is we're like, I know you probably did this, but make sure you turn your screen brightness to 100%. But it's like the day the LCD monitors, like, start to just have a super bright screen and pulse with modulated again, we are hosed. We are just – Well, then the process will start over. Well, I mean, like, realistically speaking, if we were to re-release today, we would probably drop off the parts where we optimize for, like, CRTs. Like, that's probably not needed anymore. Like, I mean –

**Chris Gammell:** No, probably not.

**Adam Wolfe:** I would like to make sure to check – we do a lot of schools and workshops, and I would just like to make sure that there's not really many CRTs left anywhere in, you know.

**Chris Gammell:** But, I mean – That's, like, a mission of yours, you mean?

**Adam Wolfe:** Well, I mean, no, I mean, like, for that camp in Africa, it would have been a shame in, you know, if that school would have bought 50 or 100 blinkies and they hold them up to their monitors. And here I am, and I'm like, oh, yeah, no one uses CRTs anymore. I'm going to remove this.

**Chris Gammell:** It's like – Just hold it up to your 70-inch plasma. It's no big deal. Whatever. Yeah, exactly. No big deal.

**Adam Wolfe:** Hold it up to your iPhone. Like – Yeah.

**Chris Gammell:** Yeah, that would be insensitive to say at least. Yeah. So –

**Adam Wolfe:** Yeah. Like, so, I mean, so that's one of the things where – it's one of – like, it's kind of nice that I – like, I enjoy trying to hit the widest possible intro market. Because as kind of an engineer slash PM slash entrepreneur slash janitor, you know, like, when you're a one or two person thing, you do everything. It's like – it's interesting just to be like, what happens to the engineering process when from day one you know that you're trying to hit a person who has almost no background knowledge? Yeah. Or a person who has hardly any resources or any, you know, money?

**Chris Gammell:** Yep. That changes a lot of stuff.

**Adam Wolfe:** Right? I mean, like, in, like, the big places I've worked, it's like, we do DFM here. So we make sure that everything – you know, we think about manufacturing from stage one. And it's like, as much as I've heard engineering firms say that, when you're a one or two person company, you're really thinking for design for manufacture, right? Because, like, you're probably doing it.

**Chris Gammell:** Because you're designing for not getting emails at 2 in the morning or calls at 2 in the morning. That's the real power of DFM.

**Adam Wolfe:** Right? Like, I mean, so, like, when a major retailer says, well, we just want to try this product out. So we want 10,000 in two weeks. And you're just like, okay, gulp, click. Right? And it's like, then your whole house is full of, like, 2X, you know, battery holders to hold your blinky kits. You're like, maybe I could do something with coin cells that won't necessarily fill up my whole house. Yeah.

**Chris Gammell:** Yeah. That's a lot of plastic in empty space, huh?

**Adam Wolfe:** Oh, man. Like, you – like, at some point, a lot of product pricing, at least at our volumes, is how much it weighs.

**Speaker ?:** Huh.

**Adam Wolfe:** Like, I mean, for us, like, the LEDs that we got, like, we're looking – like, for LEDs on our blinky kits, right? Like, these things are not ultra-high quality audiophile or iFile LEDs, right? Photophile. Yeah. Yeah. These are not photophile LEDs. These are not gold-plated, right? We just need them to indicate on and off. And, I mean, they're bright. Like, we're proud of them. I don't want to say that, you know, we got crap LEDs or something like that. But, I mean, we're not paying a lot for those LEDs when you buy them at half a million five-millimeter LEDs at a time. Yeah. But those battery holders, they're a piece of plastic, two wires, and a switch.

**Chris Gammell:** A little stamped metal contact, right?

**Adam Wolfe:** Oh, but they take up so much space that it's, like, everywhere in the world, those things cost 30 cents. If you buy them – it's just because that's how much it costs to ship them plus, like, a penny. Yeah. Right.

**Chris Gammell:** Exactly.

**Speaker ?:** Yeah.

**Adam Wolfe:** Yeah. For us, it's always been, like, the only way to get them cheaper is if we, like, slow-bolt them and they're, like, they could get there any time in the next, like, six months. That's really the only way for us.

**Chris Gammell:** And you put them on a shipping container to your house, too, right? Or from your house.

**Adam Wolfe:** Well, and that's also not cheap because, I mean, I'm in Minnesota. There are not too many ports around here. No? That's weird. It's not too easy to just – you know, I'm not in the mission or something like that where I can just be like, oh, yeah. Yeah. I'll go pick it up. Go out of the dock. Yeah, exactly. Exactly. It's like, okay, so then once you've shipped it, then I'm going to pay another, you know, thousand dollars in freight charges for you to ship it to my house. And I'm in an apartment. Oh, yeah. I got to convince my apartment owner that they can drop it off in my house and I don't have a loading dock.

**Chris Gammell:** So. Yeah, so when you do buy a house, it'll be like, well, I bought this house because of battery holders.

**Adam Wolfe:** Yeah, well, I mean, there's not too many houses around here that I see with loading docks. So, I mean, I'm not – Well, you never know. I'm not really sure. Like, maybe like a loft.

**Chris Gammell:** Yeah, why project Specken.

**Adam Wolfe:** Or like a loft or something like that, you know, like a downtown apartment that's all hip and trendy that's an old warehouse that's been all converted.

**Chris Gammell:** Right, coffee house downstairs, right, yeah.

**Adam Wolfe:** I could unconvert the loading dock.

**Chris Gammell:** Yep. Freight elevators.

**Adam Wolfe:** Yeah, exactly. That's how you do it. I'm certain I could find a really hip, trendy place that's in an old loading dock and I would just then just open up my wall and just say, bring her on in.

**Chris Gammell:** Well, good thing that, you know, Minneapolis isn't very cold either because I'm sure that that would be an easy place to heat. Oh, yeah.

**Adam Wolfe:** Yeah, no kidding.

**Chris Gammell:** The things we have to worry about in the great white north of the states.

**Adam Wolfe:** Oh, it's – Yeah, yeah. It's so funny, you know. Like I think I saw a blog post today about pizza places or something like that. Like what's the most popular pizza place? And the article was like, well, in the Midwest, it's Godfather's Pizza because it's really popular in Iowa. And like you look at this chart and it's very obvious that the author of this blog post is like, well, if it's big in Iowa, that's the whole Midwest.

**Chris Gammell:** And this is how we rate pizza like we rate primary elections.

**Adam Wolfe:** Yeah, exactly. Exactly. It's like, well, you know, it all rounds over. It's in the middle. They're far away from water.

**Chris Gammell:** Yeah. Fly over country. Yeah. Well, Adam, thank you so much for being on the show. It was good talking about Kaikad, good talking about Wayne and Lane stuff. Thank you for the code. I'm sure everyone will take advantage of that. Yeah.

**Adam Wolfe:** Yeah, thanks for having me on. It was fun. Yeah.

**Chris Gammell:** We'll have to have you back when Matthew does not have wedding emergencies. And Dave's in town, too. We can have another. We can have a round two.

**Adam Wolfe:** Yeah. Well, and I need to, like, I want to clarify, it's not his wedding. No, of course not. I'm sorry.

**Chris Gammell:** I didn't mean to say it like that.

**Adam Wolfe:** Like it was a wedding he was in or something like that.

**Chris Gammell:** Yeah.

**Adam Wolfe:** Right. Yeah, that could be a weird. Yeah.

**Chris Gammell:** What happened, man? I'm so sorry.

**Adam Wolfe:** Yeah, exactly. I don't want him to go to work on Monday or something like that or have his dad call him up and be like, what's going on? Yeah.

**Chris Gammell:** Maybe we can bleep it out. No. You know what? We'll take it out in post. Yeah, yeah. Exactly. We'll take it out in post. Don't worry about it. Take it out in post, yeah. All right. Well, thanks again. We'll talk to you soon. All right. I'll talk to you later. Bye. Bye.

**Speaker ?:** Take care.
