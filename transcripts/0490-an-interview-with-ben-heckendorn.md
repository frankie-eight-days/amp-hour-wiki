---
episode: 490
title: An Interview with Ben Heck(endorn)
url: https://theamphour.com/490-an-interview-with-ben-heckendorn/
---

**Ben Heckendorn:** This is The Amp Hour Podcast. Released April 27th, 2020. Episode 490. Sponsored by Salier. An interview with Ben Heck.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEVblog.

**Ben Heckendorn:** And I'm Ben Heck Heckendorn, his special guest.

**Dave Jones:** What the heck? How many times have you heard that?

**Ben Heckendorn:** Well, I think they used a lot of what the heck kind of puns when I had my sponsored show. Like the hack like heck challenge and stuff.

**Dave Jones:** Yeah. Well, thank you very much for coming on, Ben. It's been like a long time. I feel like we know each other, even though we kind of sort of don't.

**Ben Heckendorn:** Yeah. I don't know if we've ever actually spoken in person before or on a podcast.

**Dave Jones:** The only time we actually collaborated was for that...

**Ben Heckendorn:** That farm thing?

**Dave Jones:** Dumpster. Dumpster hack. The dumpster hack channel.

**Ben Heckendorn:** Yeah. What was it? Like the what does a resistor look like? Right. That like toy. Right. With the pole cord. Remember? Yep. That's right. Yep. Yep. I still get people thinking I'm going to move to Australia because of that. Dumpster hack thing. You got like what? 10,000 views or subscribers for that?

**Dave Jones:** We've got 11,200 subscribers apparently on a channel with no videos.

**Speaker ?:** Awesome.

**Ben Heckendorn:** It's great. It's like some sort of social experiment.

**Dave Jones:** I still get people asking about that and I never tell. I never divulge what those videos on a certain date are about. So I never tell anyone that's my shtick, you know, is that I never reveal the true meaning behind all my videos that come out on a certain day every year.

**Ben Heckendorn:** Right. Right.

**Dave Jones:** And yeah, that was brilliant. I still get emails and messages about that. How many years ago? Like five years ago or something that was. I still get messages.

**Ben Heckendorn:** I think it was two years ago because that's when I was leaving. Is that all?

**Dave Jones:** Oh, geez. Okay.

**Ben Heckendorn:** Yeah, I know. Time flies.

**Dave Jones:** Yeah. Anyway, as what people, you mentioned this before the show to me, like people keep asking you, what the heck does Ben Heck do these days? We'll go back to what you used to do or what you maybe still do. Tell us about what you're doing these days. Give us an update.

**Ben Heckendorn:** I was getting asked that a lot at conventions, you know, before all the conventions stopped. It's like, what do you, what do you do now? Right. I kind of miss having the show because that was a very short answer. Right. Right. Of course. So now I have to sit there and I kind of like, you know, you know, like when you tell someone something for the millionth time, you kind of like your shoulders slunch and you like lock into a pose and like you're, you're acting like a person at Walmart or the train station. You know, tickets are nine to five. So I'm like, so I've gone back to doing contract prototyping work. And one of the big things that I still do, and I'm trying to do more of it, I do a lot of those accessibility controllers for people who are disabled. Oh, nice. Yep. That's something I've been doing since 2006, actually. And I was still doing that while I was doing my show. Oh, interesting. Mm hmm. Because that was my thing. Even when I did the show, I'm like, I have to still be out there somewhat because once I'm tired of the show, I still need to work, you know, because I've been self-employed for like 16 years now. I do a lot of that. And actually I'm making a video right now for my, my own personal YouTube channel, which is actually growing about making a PlayStation 4 version, which I've been trying to do for a while. And there's like twice as many PlayStations as a Xbox, but well, I don't need to describe this to you. Basically the Xbox controller is much easier to hack. There's obvious test points. Everything's clearly labeled. It's a green PCB versus the PlayStation controller. So if you try to modify it, it's got dark purple silkscreen. Oh, actually, no. It's green now. There's no test points. The only contacts for the buttons are carbon, are carbon pads connected to a silkscreen circuit. Oh, dear. Yes. It's much more difficult to hack. So it's not like I hate PlayStation. I mean, I have a PlayStation. Yeah. So what I did was I found like this third party controller from a company called Hori and you open it up and it's beautiful. There's big, giant test pads and they're all labeled. And oh, it's a hacker. Fantastic. Yep. And alongside of that, this is something, you know, that I don't like, probably not very well known, but I also build testing equipment for the video game industry, which also involves controllers.

**Dave Jones:** Ah, right. Yeah. Because you're into the whole pinball. Well, you're into that, been into that whole scene for a long time.

**Ben Heckendorn:** Well, pinball is a different thing. I'm talking about like, you know, video game industry, like Call of Duty and stuff. Oh, okay. So what sort of test gear do you need for that? Well, it's all about latency. Many years ago, it was actually, it was from the old Infinity Ward. Rami Vinson was the guy and he emailed me and he'd actually seen my accessibility controllers online. And so, hey, maybe this guy could help us with something we're trying to do. And this was for Call of Duty Modern Warfare 2. The first time it was Modern Warfare. You know how they rename everything with the same name over again, like Rocky Rambo Terminator. Then it's like, you know, it's Robocop 2019, you know, whatever. Anyway, so this was 2008. And he's like, we've been filming our playtester's thumbs on the buttons and trying to determine time of flight lag with that.

**Dave Jones:** Oh, wow. Right, right. So your high speed video, somebody actually using the controller and then sync that up with the actual responses. Oh, with the screen. Ah.

**Ben Heckendorn:** Well, because as you probably know, I'm sure you do. HDMI has a lot of lag. Upscaling images on the LCD has a lot of lag. There's a ton of lag introduced just by connecting your video game console to a screen to say nothing for the game engine or the controller, right? Of course.

**Dave Jones:** So what sort of order are we talking about here? How many microseconds? Milliseconds. I assume it's like maybe hundreds of milliseconds. It's tens of milliseconds.

**Ben Heckendorn:** It's about 50 to 60, typically. Okay. It's not insignificant. Anyway, so what he was saying is like, is there... I mean, it was a pretty simple hack. He's like, can you... It's more... You know, I'm obviously not as good an engineer as you, but, you know, it's more about can you do all this micro fine soldering to intercept the signals before they even go to any processor? Because I think they had like some arm on the controller back then. Intercept those signals and basically display it for us so we can actually have a light up display with LEDs and then we can compare that against the action on the screen. And then as you mentioned, yes, with a high speed camera, they can determine... Right.

**Dave Jones:** Wow. So have you done like videos on these or info on this sort of stuff? Like public info?

**Ben Heckendorn:** Yeah. I think there's at least one video on my website. I mean, I don't go into all the details of how I build them now because I do it for profit. So I... Right. Okay. Of course. I actually had a company in China...

**Dave Jones:** You capitalist, you. Yeah.

**Ben Heckendorn:** Well, no, I actually had a company in China steal my pinball controller design. Oh, no. Which was a badge of honor. But then when they denied it, I'm like... Of course. Yeah, yeah. But it was initially a badge of honor. Right. So I might do a video explaining everything about like an old computer or a market controller, but I try to keep this somewhat proprietary. But then what we evolved it into over the years... So one of the things I did after I stopped doing the show in June of 2018 was I took the time to make a new version of it where the controller could actually... You wouldn't need a play tester. Basically, it could create its own inputs at the button level and simulate a person, and then you could have a closed loop system for testing and logging.

**Dave Jones:** Ah. This is fascinating. So why wouldn't you just like delay the video or... Oh, no. Because that's the problem, right? Is that the video is lagging too much, so you can't add extra delay to the monitor, right?

**Ben Heckendorn:** Yeah. So the delay with the monitor and the cable, that's something that obviously cannot be changed. What the developers do is try to remove as much delay as they can within the game's operating system. Right. That's what they're testing for.

**Dave Jones:** But there's always going to be some because it's... Well, no, you could manually offset it in the software, couldn't you? You could just assume like there's 50 milliseconds. There's going to... Okay, there's going to be 50 milliseconds latency between the buttons actuating and when we read it, and then you could artificially program that in, I guess.

**Ben Heckendorn:** I'm not sure. But if there's a way to do it, I'm sure they do. And actually, when everyone got... When all the companies got into streaming, you know how streaming is like 3D, it just comes back every 20 years. Yeah, I actually sold quite a few too. Even something you wouldn't think about, like Intel bought a bunch. It's like, what are they doing with that? I mean, I don't care. But the new one that I made, even though it's late in the console generation, it sold very well. And I basically... Yeah, when I was done with the show, I'm like, okay, I'm just going to take the time and develop this and make a much better version. And then that's one of the things I did after I left the show. I was able to concentrate more of my efforts onto a single product. And yeah, it's done well. Awesome. The last game that used it was Call of Duty Warzone. The new Call of Duty has it, or used it.

**Dave Jones:** Oh, right. So the developers used it in order to refine their game? Is that...

**Ben Heckendorn:** Yes, to work on latency. And then, as I mentioned, you can basically load things. It'll basically create a CSV file of inputs. And then you can actually play that back from RAM. And then you can look at the CSV file. There's also a light sensor. So you can compare the time of flight between when something changes on the screen and when the person inputs controls.

**Dave Jones:** Got it.

**Ben Heckendorn:** Wow. I can't remember the exact... I think it runs at like 50,000 hertz. So it's well beyond what the game engine would be. Although game engines also are pipelines. So a single frame that appears on your screen, kind of almost like a five-stage pipeline processor. One image has actually gone through five stages of post-refinement and whatnot. So even the engine might introduce five frames of lag just putting the image together. So whatever they can save is very important. And yeah, I've...

**Dave Jones:** I had no idea such a market existed, but it makes sense, right? I didn't either. I assume you're the only one doing it. I assume that you own the market for this sort of thing. I guess.

**Ben Heckendorn:** I mean, I don't see why anyone else couldn't build it. But yeah, I've got like Intel, Google, Microsoft, Ubisoft buys a ton of them. Who else? Electronic Arts. Yeah, basically sold them to pretty much every multi-platform developer out there. Except for... I don't think Bungie's ever bought one. Yeah. So it's a niche of niches, I guess. But hey, but you know, it's one of those things. Like, what do they say? Like, you make a million dollars by making something people need every day. And you make a living by making something people need once a year.

**Dave Jones:** Yeah, right.

**Ben Heckendorn:** And it's cool, you know? Because like when... You know, I was really thrilled like in Modern Warfare 2. It's like, oh, wow, I got a special thanks above the Navy SEALs. I'm super cool.

**Dave Jones:** That's great. So like, because I'm not a gamer. So it's like, you know, my eyes kind of roll in. I used to do some gaming back, you know, in my teenage, late teens and early 20s and stuff like that. But geez, that was a long time ago. That was, you know, where we're talking, you know, Duke Nukem and, you know, games like that. The original. Anyway, isn't the new Xbox and PlayStation coming out soon? Or have they come out? What am I behind the times?

**Ben Heckendorn:** They're supposed to come out this year. I guess we'll see if they do. I personally believe that they're going to be fairly forward and backward compatible. I mean, are you familiar with like how they have the PlayStation Pro and the Xbox X? Terrible name, but...

**Dave Jones:** No, not really. I've got an Xbox 360 at home and that's about my... Oh, okay. So that's about my limit. Yeah.

**Ben Heckendorn:** Well, so they did these mid-generation refreshes. Basically, they made a souped up PlayStation 4 called the PlayStation Pro and a souped up Xbox One called the Xbox One X, which I was actually doing a talk once. It was in, I think, the Portland Retro Gaming Expo. And I was like, who came up with the name Xbox One X? That's a terrible name. And then some of the audience is like... It is. I did. And I'm like, it sounds like an S. Yeah. It sounds like an S because there is actually, you know, like the white Xbox One, the cheap one they sell? Yes. Yeah. That's technically called the Xbox One S as in snake.

**Dave Jones:** Oh, God. Really? Yes.

**Ben Heckendorn:** And now there's another model called Xbox One X.

**Dave Jones:** Oh, God. Oh, there's like half a syllable in there, right? Yeah.

**Ben Heckendorn:** Yeah. Actually, I was... I forgot my saver card, like my food saver card. I went to the grocery store last week and the girl's like, oh, if you give me the phone number, I can type it in. And I was like, okay, it's blank, blank, blank, niner, zero, niner. And then she looked at me and I'm like, oh, nine, zero, nine. And she's like, why did you say niner? No, I know. And I wasn't going to hold up the line and, you know, infect people with diseases while explaining that's what air traffic controllers use because nine sounds like a five. Exactly. But...

**Dave Jones:** Oh, that's great. Yeah, yeah, yeah. Anyway, my point... Young kids.

**Ben Heckendorn:** Yeah. My point being, so they've already made like, you know, upgraded consoles. And what I think is probably going to happen is the new consoles will probably be forward compatible with existing consoles. So like that Cyberpunk 2077 game everyone is excited about. And they're like, oh, if you buy the current gen version, you get a free upgrade to next gen. But I think what's really, really happening is that next gen games will probably still work on the older consoles. So I'm guessing there's going to be like...

**Dave Jones:** Oh, that's interesting.

**Ben Heckendorn:** That's just my theory that there's going to be like a unprecedented level of cross compatibility. And that's one of the reasons why... Yeah. Well, actually, obviously, as soon as I get next gen controllers, I'm going to make a next gen model. Like last gen, Microsoft actually sent me a console early to get started. Oh, okay.

**Dave Jones:** Ben Hex, that important, folks. Yeah.

**Ben Heckendorn:** Microsoft has always been nice with me. Yeah. Yeah. Yeah. And then, of course, from, you know, the capitalist in me is like, oh, boy, I get to sell everything over again. Yeah. Yeah.

**Dave Jones:** Is this the first time they've ever done forward compatibility?

**Ben Heckendorn:** If my theory is correct, yes.

**Dave Jones:** Right. Okay. Because, yeah, I don't... Because they change the hardware architecture each time. And if you're lucky, you get backward compatibility, right?

**Ben Heckendorn:** Correct. And then when you went from like PlayStation 3 to PlayStation 4, you went from the cell architecture, which is basically a PowerPC architecture, to x86. But then Microsoft, the code wizards there, they actually have real-time bytecode, not emulation, but like virtual machines. So you can actually put a PowerPC game in an Xbox One, and it will actually translate the code as it executes. It's pretty impressive.

**Dave Jones:** Wow. Wow. Well, don't Microsoft specialize in backward compatibility. I mean, you can still run, you know, a DOS 1.0 command, can't you?

**Ben Heckendorn:** Well, yeah. And we were just talking about that before we started about how there's Windows 10 still has dialog boxes from 1995.

**Dave Jones:** It's from... Yeah, yeah. That's it.

**Ben Heckendorn:** I think ad printers the same way. But anyway, but now all that's changing. So the current consoles are both eight-core Jaguar AMD APUs, and they're basically, they're still going to be x86. It's basically a beefed-up version of what we have now. So it's going to be x86 again. It's just going to have, I think, more CPU cores than twice the RAM. Like, they're only going from like eight gigs of RAM to 16 gigs of RAM, which is actually the smallest increment in RAM size ever in console generation.

**Dave Jones:** Oh, okay. Normally, it's more than double.

**Ben Heckendorn:** Yeah, usually it's about 32 times. Oh, okay, right. Yeah, well, yeah. You had like Xbox, the original Xbox was like 64 megs, and then it jumped to 512 megs, and then it jumped to eight gigs. So yeah, it's usually pretty exponential, just like memory in general. So yeah, I think, and also, you know, if the economy's been slowed down, I think they probably aren't going to push the new consoles as much. Exactly, because RAM's expensive. Well, no, I just mean to sell to people. You know, it's going to be a slower sell. And then you look at like PlayStation 4, they already have an install base of like 100 million units. They're not going to like just abandon that overnight. Like most companies are probably going to plan for at least three years post-launch of the old cycle. Well, we talked a lot about video games today.

**Dave Jones:** Yeah, we have. Considering I know nothing about video games, but that's your thing. Well, that's all right. I don't care. No. And that's why we got you on here. You know, we're going to be talking about your stuff, not my stuff.

**Ben Heckendorn:** Oh, we should talk about your stuff, too. I mean, I watched your latest video where you fixed up that arcade. That was pretty cool.

**Dave Jones:** Oh, no, that was just a power supply. Dodgy old power supply. I almost gave up on that. It's just not worth the effort.

**Ben Heckendorn:** Yes. Spooky uses those in pinball machines. And I want to say they're $15 for that standard arcade supply. As you would say, they're cheap as chips.

**Dave Jones:** The confusing thing was that it had a date code on there of 1984. So in the video, I assumed it was like a, you know, like a 1984 stock board. But then somebody, people in the comments go, oh, no, it's still the same board from 1984, but it's a modern build. And it's like, really? They're still using the same layout board from 1984? They've still got original stock of, you know, like how far are they pushing this thing? It's like, wow. Wow.

**Ben Heckendorn:** Oh, you know, I think I actually have, I have one of those in my basement. I don't know if I'm going to bother taking it apart, but I'm not quite that bored yet. But yeah. Yeah. So those are the, oh, and I've also been doing like just contract work for people and stuff. And although I'm going to be starting up a new, a new pinball machine design here pretty soon. So that's something else I'm working on in the background.

**Dave Jones:** Is there a big marker for that? For like your own custom pinball? Well, I mean, I guess with your notoriety, there's a.

**Ben Heckendorn:** No, it wouldn't be a custom pinball machine. It would be like a mass market produced game.

**Dave Jones:** Oh, right.

**Ben Heckendorn:** Okay. Yeah. No, but pinball. Well, again, things are a bit slow right now, but pinball has been super hot for like the last 10 years. It's like insane. Really? Oh yeah. It's, it's like, like people were like home basement bars. It's like, yeah. Yeah. They fly off the shelves. Like a spooky pinball, the company that I worked with before and I'm working with again, the ones that use my original board set that China copied. Yeah. They announced a Rick and Morty themed pinball machine, 750 units. They sold out in four hours.

**Dave Jones:** Wow. Yeah. Is it, where, where is the demand? Is it for new ones or is it for retro, like old, you know, original star Wars, Indiana Jones pinball machine or something?

**Ben Heckendorn:** No, it's definitely for new ones. So you've got like Stern down in Chicago. Then you've got Chicago gaming company, Jersey Jack, spooky, a lot of manufacturers. And yeah, I mean, I don't know the exact numbers. I think Stern produces like 12,000 machines a year and these are like $7,000 games. So it's a, it's big, it's big money. Yeah. Yeah.

**Dave Jones:** Wow. Is there, is there a lot of margin in that business? If you know, is it?

**Ben Heckendorn:** Well, there's not as much as other things that we actually ran in. I mean, there's obviously margin because the companies are still in profit. Of course.

**Dave Jones:** Still in business. Yeah.

**Ben Heckendorn:** I mean, it's, well, you know how it is. It's usually like 3X or you take the retail price and the actual cost of it's divided by three. It's not that high, but the thing is, there's a lot more direct distribution. You know, you don't have like Target or Walmart or Amazon. No, of course.

**Dave Jones:** No, they're, they're not holding stock at your local.

**Ben Heckendorn:** We did run into that. I think it was when we did, I think it was the Rob Zombie pinball machine. And cause you deal with their, you know, you deal with their licensing department and their licensing department does assume that you're making a 10 cent lunchbox in China. Right. And so they're like, so they'll propose a royalty percentage, but the first one they proposed was too onerous. And we had to explain that the, again, the profit margins were much different versus like a lunchbox or a two-bit-based. Yeah. Yeah.

**Dave Jones:** Right. Interesting. So is it, is there a lot of call for like, like really branded stuff? Like a new movie comes out and you'll get the latest, you know, Arnold Schwarzenegger pinball machine, you know, Terminator pinball machine or something like that. Or is it just like people just invent their own stuff, which is more popular?

**Ben Heckendorn:** The market by and large wants licensed themes. It's actually a big point of contention. And when they do try to make like an unlicensed theme, it'll sell, but not nearly as well. And then weird things sell too. Like one of the biggest hit pinball machines of the last decade was based off Metallica of all things.

**Dave Jones:** Oh, wow.

**Ben Heckendorn:** They're, well, they're not new. And ACDC, you know, from your neck of the woods. Oh, yeah. I think that's actually Stern's top selling pinball machine ever. And that came out in 2012. Really?

**Dave Jones:** It's the Akadaka machine. Yeah.

**Ben Heckendorn:** But it's like when you play it and it makes you feel like a rock star, you know, it's like you make a shot and it's like, you hear the crowd go. You feel like a rock star playing it. And that's what makes it good. It gives you that fantasy. Yeah.

**Dave Jones:** Yeah. Yeah. That's great. Oh man. Yeah. I'd love a pinball machine, but I just don't have room. You know, it's like, and they're so expensive, especially to get them here. Like I would love like a back to the future Indiana Jones or something like that. You know, but, but geez, to get those here is like, oh, you gotta, yeah. Gotta sell your firstborn.

**Ben Heckendorn:** I have a friend in Auckland. Well, it's in New Zealand, but you know, same kind of thing. Well, I know. Yeah. You guys don't. Difference. Yeah. Yeah. And yeah, I think not only do they have the shipping, but then they have, you know, it's more expensive to import.

**Dave Jones:** Yeah. And they're so rare here. They're just the sheer rarity of them. If they come up on eBay, I've looked sometimes at pinball machine prices. Holy crap. No thanks.

**Ben Heckendorn:** Well, and remember most of them, well, there are manufacturers in Europe, but most of them originate from Chicago. Chicago. So yeah, it is. Right. Well, it's just like you think about with anything like economics, the bigger something is, the more sense it makes, makes to make it in your own country, which is why there's still a lot of cars way to North America, but all like the tiny cell phones, you know, get shipped on the bars.

**Dave Jones:** Unfortunately, there's no cars made here anymore. Really? We just stopped all, we just stopped all automotive production here in Australia. Yep. Holden, Toyota, Ford, they're all, yep. Nissan, they're all stopped. Yep. Shut down. That sucks. Yep. No kidding. Oh, yep. Anyway. Yeah. That's Australia for you.

**Ben Heckendorn:** I've never, I've never been there. I've been to New Zealand, but never Australia. Maybe someday.

**Dave Jones:** Excellent. Well, you'll have to come to the dumpster room.

**Ben Heckendorn:** Yes. What I, well, yeah, I had to, I had to admit your dumpster room is a little hard to believe, but I guess I believe it.

**Dave Jones:** You guys don't have that sort of thing over there, like corporate office tower complexes.

**Ben Heckendorn:** Like, well, I guess we, well, of course we. I do, but I mean, I don't live in one.

**Dave Jones:** Right. You've, you've, you've never worked in one.

**Ben Heckendorn:** I know. And Silicon, in Silicon Valley, they actually guard their dumpsters. Like they don't want. Oh, okay. To like steal things from the dumpster. Of course. Yeah. Now the best we might get here is, oh, look, that couch by the side of the road looks okay.

**Speaker ?:** You're right.

**Ben Heckendorn:** Yeah. Yeah.

**Dave Jones:** Yeah. We, we, we used to have that here. Like it will, it varies depending on which council area you're in, like the council pick, council cleanups they're called. And it used to be like twice a year on the same date. Everyone had dumped their stuff out on the, you know, on the front, you know, in the front driveway or whatever, front verge or whatever you want to call it. And, and then, so everyone had then come along and pick up, you know, you go through and half your stuff would be gone by, you know, hours after you put it out. Right. So all this stuff was being recycled. Only twice a year. It was only twice a year. Yeah. Or you could actually request an individual pickup. You could, you know, but now they've changed to this system where no, you have to, you can request two pickups a year. So you can, so you've got to request it so that now there's not all these people going around hunting for stuff. Cause they knew when the day was now it's like just completely random. And it's like, uh, that's, you know, dumb. I like seeing people recycle stuff from the verge, you know, it's great.

**Ben Heckendorn:** There's a thing. Well, this is a, I live in Madison, a big college town, and there's a thing called hippie Christmas. And it's, it's at, it's at the end of the school year when all of the, uh, college students, you know, clean out their dorms or their houses they're living in. And so you go downtown and like the entire streets are filled with stuff. And then everyone picks it up. Actually. Yeah. Just actually, wait, what is today? Thursday. Uh, yeah. On Monday I went and had a back porch, uh, social distancing, uh, lunch with a friend of mine from the show. And then as I was leaving a picker truck stopped by and picked up the chair. He, it was, I was almost like, I was like, Oh, I can't get out of the driveway. There's this old truck there. And I'm like, Oh, it's a, it's a junk picker. Yeah. I was like, I was remodeling my garage and I'm like, Oh, I don't like this. I was just ripping everything out of it. Yeah. Cause I was redoing it, but then I put it on the curb and I want to say, I put like five things on the curb and all, but two of them are gone. So we're quote unquote lucky here. They actually do that every two weeks. Oh, right. Wow. Then we have pretty, pretty high taxes in this, in this town, but, uh, I guess so hashtag lucky, unlucky. But anyway, um, but what I do, so our, our garbage day or large pickup day is like every other Monday. Right. So what I do is if it's not going to rain, I put something out on the curb or the verge because that gives people all weekend to see it and possibly pick it up. And yeah, hopefully use it. Right. So that's, that's my method. So basically it gives, Oh yeah. This little old lady was walking down the road and there's this terrible rickety ladder covered with paint that I was like, I'm not going to stand on that. And then, and she comes up, she's like, Oh, are you giving away that ladder? And I'm like, well, yes, it's on the curb. I wasn't rude. I'm like, yeah, yeah. And she's like, Oh, so I can take it. And I'm like, yeah, if you want. And then the back of my mind, I'm like, if you fall off it, don't remember what house it came from.

**Dave Jones:** Well, I don't think she'll, I know that. I don't think she'll remember when she falls off and she'll be dead.

**Ben Heckendorn:** Who will she sue? But the thing is she probably weighed, she probably weighed half of what I do. So technically she'll be safer on it. It was either that or chop it up into firewood.

**Dave Jones:** Oh, yeah. That's great. Yeah. People love free stuff. They just, you know, yeah.

**Ben Heckendorn:** I got my, my kitchen table. I got, it was sitting next to a dumpster one time when I moved from an apartment. Cause the thing is people don't throw things away because they're bad. They throw them away. Cause they don't want to move them.

**Dave Jones:** Right. Exactly.

**Ben Heckendorn:** So yeah, I've got a dumpster kitchen table. I don't, I don't care. I'm not proud.

**Dave Jones:** Yeah. That's why I find all this stuff in the dumpster because like people in their offices here, right? Businesses, they couldn't be bothered like advertising this thing to get 50 bucks for it. It's just not worth their time. You know, waiting around for people to turn out. It's already been written off. Yep. Exactly. So it's like, no, they just order their new shiny computer and they throw their old one out complete with hard drive and all their info on it. Cause they don't know any better. You know? And it's like, haven't found any Bitcoin yet. Damn it. Because anyone who's into Bitcoin would be smart enough not to throw out their Bitcoins, you know?

**Ben Heckendorn:** Didn't you, didn't you found like a four toner laser printer once, right? That wasn't an April Fool's, right? A color laser printer, right?

**Dave Jones:** Oh no, I found, oh no, I've got one here. I was actually going to do a tear down of that today. Oh yeah. Yeah. I found multiple. I found like half a dozen full on. I've got a large Dell one. Those things are expensive. I know they're hugely expensive. I was going to tear it down cause it kind of like it works, but it's got like streaks all over it. Couldn't be bothered to repair it. It's huge. You know, I'm downsizing the lab. So, so what I was going to do is actually put a big mat down on the floor and I was going to tear it apart. That was going to be today's video, tear it apart and see what parts you can salvage from one of these big, like sort of corporate laser color laser printers.

**Ben Heckendorn:** Oh, that would have been a great earth day episode. You just missed it though.

**Dave Jones:** Oh, okay. I just missed earth day. Did I? Okay. Yeah.

**Ben Heckendorn:** It was yesterday. It was a yet another canceled holiday, like April fool's. Right. Yeah. Yeah. So yes, I'm definitely, well, I have, I have this thing. I grew up in rural Wisconsin around all these junky farmers. I don't know if it's like that down there, but they just buy everything and they just put it in their front lawn and brainwashed me to not be a hoarder. Right. Yep. So like, like my uncle, my uncle gave me his lathe and then he's got like a 1967 tectronics oscilloscope in his garage. And he's like, you want that too, Ben? And I'm like, no, I actually gave away my 1969 tectronics oscilloscope to somebody when I moved to shop. Don't need any more with a cadmium solder inside.

**Dave Jones:** Oh, my, my dad was always buying and selling things. So I, I actually grew up with that on our front lawn was like, you know, stuff for sale. He'd buy and sell box trailers, caravans. He'd buy, you know, there'd always be hubcaps out, out the front with, you know, sale prices on them, you know, everything. He'd just buy and sell everything, you know, anything for a buck. You know, it was, it was just, just a hobby, you know, it was a hobby of his. And right, right. Yeah. It spilled over to me. Like for way, since way before I was doing the podcast, I still do it these days is buy and sell stuff on eBay. Like I'll buy a test gear from the US and then I'll like get it imported here and then I'll either fix it or clean it up and, and test it out. And then I'd re sell it here for like three, three times what I paid for it. Oh, nice. Yeah. Yeah. Yeah. Because our, because our market, there's a niche there. Whereas a lot of, a lot of people in Australia will not buy, will not trust. Buying from overseas, especially on eBay. Right. Because I think they'll get ripped off. It'll never get here or whatever. So I re buy it. I, I take the risk buying it and then resell it and make a handy profit.

**Ben Heckendorn:** eBay and PayPal have pretty ridiculous buyer protections. It's very lopsided. Oh yeah. The buyer. Yeah. It is heavily. Yep. Yeah. I know. I've had not too many issues, but it has happened. So yeah.

**Dave Jones:** Which is good for the buyer, but you can, but for the seller, you can get scammed. So, you know. Yeah, definitely. Yeah.

**Ben Heckendorn:** I used to, I used to like, I used to like going to pawn shops, but I haven't done that. And actually, I went to that a couple of years ago.

**Dave Jones:** Yeah. Yeah. I used to get old vintage calculators and multimeters and stuff like that.

**Ben Heckendorn:** I got, I think the last thing I bought was this crappy four, three ratio, uh, LCD TV. It's like 20, not even 20 inches, but it's really, it's super handy. I take it to conventions and you can put VGA into it. It takes PAL and NTSC. Yep. So I can hook up my ZX Spectrum.

**Dave Jones:** Nice.

**Ben Heckendorn:** Uh, yeah. So that was a great find. I was, uh, the LGR guy. He, he inspired me. I'm like, oh man. Oh yeah. Cause I used to love going to Goodwill too. I just never do it anymore. But then one day I was going to Goodwill. I think it was when I was looking for a screen. I bought that at the pawn shop, but then Goodwill. They had a Sony Mavica digital camera with a floppy disk. Like I used. Oh yes. Yeah.

**Dave Jones:** I've done a tear down on one of those.

**Ben Heckendorn:** Yeah. They're great. I was, I used to be a graphic artist before I did this. When that camera came out in 97, that was a revelation. People do not understand. It was so big.

**Dave Jones:** At, at our company, it was kept under lock and key. Somebody, literally somebody was like, you know, the secretary or whoever was in control of this camera. And if you wanted it to take a photo, to put documentation into your, you know, your 1990s Word document, right, you would, you know, yeah, you'd have to go sign out the camera and then you'd get it and you'd charge it out and you'd take your photos. You had to return it and sign it back in. And it was that valuable, you know? It was like, yeah, it was like 800 bucks. I want to say. Yeah, it was, yeah, it wasn't cheap, but it was, you know, it was the only way that you could get images into a PC to include them in, in like, you know, uh, testing documents and, you know, test procedures and things like that. You had to take photos of, you know, things to hook up and, and it was the only way to get photos into a Word document back then.

**Ben Heckendorn:** And well, there, there did exist, uh, flash memory cameras at that time, but they were obviously flash was extremely expensive. So you might have two megabytes tops and we had one, but the only way to dump the data was through a 9,600 baud serial cable. So even though the Mavica was lower quality images, you could get them off super fast. And the key thing is if you're on location, you just stick it another floppy disk.

**Dave Jones:** Exactly. So yeah. And it was, it was good enough for like, you know, putting a photo in a report or something like that. You know, it wasn't, it wasn't good for blowing up images and things like that, but I think it was six, was it 640 by 480 or something? It was like one megapixel or something.

**Ben Heckendorn:** Yeah. It used a video camera sensor. So it was also interlaced. Yeah, it did.

**Dave Jones:** That's right.

**Ben Heckendorn:** Yeah. That just reminded me, cause I saw someone on Twitter was asking about Maker Faire or an opinion. Uh, the last one I went to in 2017 in San Mateo, I actually took my Mavica and, uh, I was taking all the photos that whole weekend with the Mavica and I actually ran into like this 10 year old kid. He also was taking photos with a Mavica camera. I was like, probably twice as old as he was. And so anyway, then we took a meta picture of each other. So. Oh, right. Yeah. Nice. I thought I was like, oh my God, I never thought I'd. Yeah. Cause a lot of people were like, it was a great conversation piece. Like people are like, what the heck is that? And I explained it, but then to see this little, so I was having like 30 year olds ask me that, but then to see this 10 year old with one was very funny. With one. Oh, wow. That's great.

**Ben Heckendorn:** Here in the Amp Hour, we're pairing with advertisers who help educate our listeners. Celia makes logic analyzers, test equipment with an innovative software interface used for measuring analog and digital signals. Long time listeners of the show will recall we had Mark and Joe Garrison, the founders of the company on the show back in 2015. I had a chance to talk with Mark recently and asked him for a refresher on how logic analyzers work.

**Chris Gammell:** Yeah. So when you're recording like a digital signal, right? Well, there's a couple of the big factors. And one of them is sort of what's called the IO threshold, right? And if you remember from school, there's a lot of electrical standards like CMOS and TTL and those kinds of things, 3.3 volt logic, 5 volt logic. There's actually thousands of these things. And so what we did for the pro devices in particular is that inside of the logic analyzer, we actually have three different voltage references and you'd be able to switch between them and then high speed digital comparators. I can't do all the digital inputs.

**Ben Heckendorn:** And that's the low level capture of signals. But as we move up to higher levels of abstraction, how are engineers using this device on their bench?

**Chris Gammell:** Probably have like a microcontroller. You probably have some sort of like, you know, boot EEPROM or you have memory. Maybe you have, you know, sensors, cameras, et cetera. And all that stuff needs to work together. And there's usually quite a bit of activity involved in there. If things don't work, you know, the proper sequence or some communication is intermittent or fails, then it can cause a creative problem that's very difficult to find. It doesn't occur all the time. Maybe it's buried in the activity. And so what you want to be able to do is you want to record a long stretch of information, ideally from the moment you turn your device on to, well, lastly, the errors occurred one or more times so that you can actually have complete context. Then once you have that information, you want to sift through it. So you probably have, you know, some digital channels in there with like I2C or SPI communication going on or serial or whatever that might be. Maybe you're looking at some analog power supplies and you want to see their power sequence.

**Ben Heckendorn:** Having used a salier before myself, I can see how much it helps to be able to sort through lots of data. Their software is especially well-tuned to large captures and then getting the signals you care about all without fiddling with the knobs like on a traditional logic analyzer. So I was wondering about other companies that are also using this large capture capability and what they're doing with it.

**Chris Gammell:** We see electric car companies are using our products. They're using it to record quite a lot, a wide variety of analog signals. It's one of the really interesting things to see what people are using the analog side for. We have people working on, you know, self-driving car vision systems and stuff. And they're using our products to record can data traffic. And our product I know has been used on equipment that simulates rockets for testing rocket flight controllers. A lot of academic projects. Our product has been to some kind of remote places. It's been to Antarctica with a underwater robotic vehicle team. It actually has been with those two different unrelated underwater robotic vehicle projects.

**Ben Heckendorn:** So whether you're looking to capture data on your bench at home or traveling to the Antarctic, check out the Salier products like the Logic 8, Logic Pro 8, or Logic Pro 16, all of which give you a portable, user-friendly way of measuring digital and analog signals. Salier is looking to get your feedback too. You can win a Logic 8 or a second one and hear about their new releases as their software keeps improving. Go to salier.com slash amp hour to take the survey and enter to win. That's salier.com slash amp hour. And now we're back to the show.

**Dave Jones:** Well, speaking of which, let's get to this Twitter question from David Ray. What do you think about what happened with Maker Faire last year as in shutting down? And will it affect the future of the maker industry? Will it have an impact or influence vacuum to be taken up by others like Artifruit, Spark Fund, et cetera?

**Ben Heckendorn:** Well, I wouldn't be surprised if other fairs pop up. Did they all get canceled or just like the big ones? Yeah. A lot of them are independent.

**Dave Jones:** Make Affair went bust.

**Ben Heckendorn:** Or make, you mean.

**Dave Jones:** Well, make. Make went bust, which means Maker Faires went bust, which means technically, I guess, if you were running a licensed Maker Faire, you can't call it a Maker Faire anymore because I guess somebody somewhere still owns the trademark, you know? So, you know, you could still hold it, but yeah.

**Ben Heckendorn:** I've been to many Maker Faires. San Mateo many times, New York at least three times, Detroit three times, many Maker Faires here. So I really enjoy Maker Faire. I would say going to them over the course of like seven years or whatever it was, I did see changes that I think probably affected it financially. A lot of the big, super big sponsors kind of started to drop out.

**Dave Jones:** Right.

**Ben Heckendorn:** If you went back in like 2010, 2012, you'd have a huge Intel booth, Microsoft, Google. And then as the years went by, those kind of got smaller and, you know, kind of started to drift away. It's very much like what's happening with E3, the video game expo. Okay. Or like a mall. Once you lose the anchor store, you're kind of done.

**Dave Jones:** Yeah, the anchor store, sure. Yeah.

**Ben Heckendorn:** That's it. Maybe it's like the corporatist in me, but I always thought, you know, the big sponsored booths were the coolest because they had huge budgets behind them. They had cool things you could buy. And then it kind of, I know that, you know, it might, you know, it might be a little touchy to say, but it just kind of, even like the one in San Mateo, it got like more arts and craftsy than technical. And at least for someone like me, I'm like, I don't care about sewing. I know a lot of people do. Of course.

**Dave Jones:** But yeah, it's like, yeah, we're just tech nerds. Right. So. Right. Yeah.

**Ben Heckendorn:** But, you know, I've, I've been doing this kind of stuff for a long time. Like even professionally, I was doing it before the maker movement and the make, you know, we didn't even really have a maker movement 20 years ago. It's like, oh, I need to buy an icy battery charger. Where do I get it? Right. Right. And yeah. So even if maker fair is gone forever, I think it did, did actually play a very crucial role in developing the maker concept and, you know, helping introduce people to it. And like, oh, I can actually, it was, it was like a county fair, basically a county fair with electronics, or as I sometimes described it, it was a burning man, but people had clothes on.

**Dave Jones:** Right.

**Ben Heckendorn:** But, you know, it was, it was because you'd have a lot of families coming and they'd be showing their kids and the kids would be getting into it. Yeah. And, you know, they'd have funnel cakes and whatnot. So yeah, I mean that, that stuff was really cool. And yeah. So even if it's gone, I think it did play a good part. And as to whether like Adafruit or SparkFun or whoever will do it in the future. I mean, I could see smaller ones cropping up. Like, have you ever heard of the Midwest RepRap Fest? No. Like a 3D printer festival. Right. So it started as like one room in a county fair building in March. Like, I don't know, five years ago. And well, it was canceled this year, but it's been exploding in size. And like, it has Google as a sponsor now. And it's in the middle, it's in the middle of nowhere, Indiana. Right. Like trucker and strip club world land. And, but no, but every, every year, like I can't, I think they, they went from like a hundred to 500 to a thousand to 3000, I think was going to be this year. It was just exponential growth. And that's a fairly new thing. So I think that's kind of going to be the future. Like, you know, small, smaller localized things, but then they always inevitably grow.

**Dave Jones:** That's interesting. Cause like 3D printers aren't the rage anymore. I mean, what, five, six, seven years ago, 3D printers. Well, yeah. Oh, 10 maybe. Yeah. They're like 3D printers where the future, everyone would have one in their home. And that kind of all fizzled out, didn't it? It was like, it's like 3D printers. Now it's like yawn.

**Ben Heckendorn:** Well, I love 3D printers. I use them all the time. I was finishing up a print right before I logged on, but yeah, they're not for everybody. It's not a mass market item, like a microwave.

**Dave Jones:** No, it just, it just didn't turn out. Why do you think it didn't turn out? They're just finicky. They're just always going to be finicky.

**Ben Heckendorn:** Well, they're, they're really cheap now. I mean, you can, you know, once the Chinese printers showed up, it's, it's very cheap. I think it's one of those things where like, if you know what you need it for, you want it, but if you don't know what you would do with one, you don't need it.

**Dave Jones:** You don't need it. Yeah.

**Ben Heckendorn:** So if it's just something like, oh, I heard about this in the news. I think it's cool. And then you have it. You're like, what do I do with it? Now for me, it's like, what did I do without this? Kind of like my Dremel oscillating tool.

**Dave Jones:** Oh, of course. It's, it's like, you know, purpose-made for someone like you who does custom mods and you're always doing custom housings and things like that.

**Ben Heckendorn:** Yeah. I used actually the, the, well, not silver bullet, but killer out for me was, uh, I got my first, well, I built a 3d printer first and then I bought a replicator one in 2012 and it somehow it still works.

**Dave Jones:** Right.

**Ben Heckendorn:** That was the same time I was developing my first commercial pinball machine. And for that, it was amazing because I actually, I saw them at maker fairs. I'm like, oh, big whoop. You made a bottle opener, right? Who cares? Right. But then when I actually started using it for like my development of like custom mechanisms in a pinball machine, I'm like, this is amazing. Cause you know, I've been doing CNC. I had a laser, but 3d printer definitely, at least for me, has an amazing niche. I have, I have two and I have another one. That's like, it's actually one of the better, more expensive replicator clones from China. It's actually pretty finicky. So I'm going to swap it out for E3D and put in like the new 32 bit ARM controller. Cause I want more. Because as I mentioned, I'm trying to develop more accessibility controllers, which means I need more 3d printer bandwidth.

**Dave Jones:** Got it. Cause you're doing multiple prints at once.

**Ben Heckendorn:** And yeah, the way I look at it is if I'm building something by hand for a customer, the, the time it takes to 3d print, the parts cannot exceed the time it takes me to assemble it or wire it. That's my rule of thumb. Got it. So.

**Dave Jones:** Yep.

**Ben Heckendorn:** Do you have one?

**Dave Jones:** No. Oh yeah. Yeah. So I've got a 3d printer. I've got a make a lot thingamajig make a lot replicator. I don't. Yeah. Yeah. It's a one as well.

**Ben Heckendorn:** The wooden one.

**Dave Jones:** Yeah. Yeah.

**Ben Heckendorn:** Made it made in Brooklyn.

**Dave Jones:** Still works. Still works. Yep. After I did a few upgrades to like the support mechanisms for it and everything, you know, it was always a bit dodgy. So, you know, I things stiffen things up and works a lot better now.

**Ben Heckendorn:** Did you replace the five volt regulator on the motherboard? Actually, didn't Chris design that? No. Wait. No idea. Didn't Chris Gammell design that? Not that I'm aware of. Maybe I'm thinking of somebody else.

**Dave Jones:** No, you must be thinking of someone else.

**Ben Heckendorn:** The original five volt regulator on that is only rated to 21 volts DC input. And the power supply is 24. Ah, oops. Yeah. It's barely in spec. Well, you know, there's always overages. Yeah, yeah. So a lot of them fried. And basically, it's one of those things. So if, well, it doesn't sound like you use it very much. But yeah, putting in a properly rated five volt regulator is one of the things you do to keep it running. So, yeah. I think of the movie WALL-E where the little robot's collecting his extra parts of himself. So I have my ancient replicator one. I have an extra motherboard. No, I have two extra motherboards, two sets of drivers, and an extra power supply. So I could probably keep it running a while. It still prints well. It's slow, but it prints well.

**Dave Jones:** Last time, I use it so infrequently. Like, one time I went to use it, and then the software didn't work. And I went, what the hell's going on? And I found that, like, oh, no, they abandoned support in the latest software for that printer like two years before or something. So I had to download. So it only works with an old version of the software or something ridiculous like that. Oh, really? I don't know if that's still the case. But yeah, it was dumb.

**Ben Heckendorn:** I used to use the software because it did make it easy to run multiple printers at once because they had a background process going that actually hooked up to the COM port. So the software instance itself didn't have to reconnect to COM ports and disconnect. But then I started using Simplify 3D, which is, I think you pay like $150 for it. It's basically a slicer. But anyway, it supports everything, even including ancient replicator one. That's the trick. Yeah. Okay.

**Dave Jones:** Yeah, now I'm just using the MakerBot software, whatever that was. But I use it so infrequently. What software do you use for 3D modeling? 3D CAD?

**Ben Heckendorn:** I use Autodesk Fusion 360.

**Dave Jones:** Okay. Yep. Is that... That's something I've never learned. I've never learned 3D CAD. And that's probably why I don't use my MakerBot a lot because, well, I've just got no skills to, you know, very rudimentary skills to...

**Ben Heckendorn:** Back in the 90s when I was into making independent films, that was my hobby for like 10 years. I paused doing electronics to do that, which I... Looking back now, I shouldn't have, but whatever. Anyway, I did a lot of like 3D stuff. What was it called? Like Lightwave or True Space or something like that? So... Lightwave I've heard of, yeah. Yeah. So, I mean, I was somewhat familiar. I'm not that good of a modeler either, but I could do enough to get by. So, yeah. But it's fun to learn. You know, it's basically two-dimensional sketches. Yep. And then you extrapolate them into 3D.

**Dave Jones:** And then you extrude it out. Yep.

**Ben Heckendorn:** Yep.

**Dave Jones:** Yep. Got it. So, let's talk about the... We didn't actually introduce you at the start of the show, but everyone knows who you are anyway, so it doesn't matter. So, everyone's familiar with your work. Tell us about the movies and stuff that you... The movies? Are you still doing the movies? I see the last one was like 2008 or something.

**Ben Heckendorn:** Oh, yeah. I've actually got a poster of it on my wall right here. Possumus Woman. Right. Yeah. My giant killer. Possumus Woman. Yeah. Well, the first one was Possumus Man, you know, so...

**Dave Jones:** Right. Of course. So, you had to do a sequel. Yeah.

**Ben Heckendorn:** That was actually the last one I did. So, I basically... Actually, that was the first movie we shot with solid-state cameras. Oh, okay. Yep. Panasonic P2. Oh, my God. That was... Just like the Mavica camera. A solid-state...

**Ben Heckendorn:** A solid-state camera that can shoot 720p in 24 frames a second. Progressive. Oh, my God. It was amazing. You know? Yeah. My laptop at the time, they still had PCMCIA slots on it, right?

**Dave Jones:** Yeah, right. Yeah, of course.

**Ben Heckendorn:** So, that camera had two PCMCIA slots for the media. And the media was... It was like $4,000 for like four gigs of storage. Oh, wow. But what you could do... You could hot-swap them. So, you could actually pull one out from the camera, stick it into your laptop's PCMCIA slot, review the footage, and dump it to a hard drive, empty out the cartridge, and put it back into the camera. Oh, nice. Fantastic. And then when we started doing the Ben Heck show, they said, okay, get two cameras. And so, I went to Full Compass, and I got... I actually got a P2, since I was very familiar with it. Because at the start, I was filming and editing myself. And then I also got this little dinky Canon 1080p, which I still actually have. It's... Right. They're like, oh, you should buy this as your B camera. And I'm like, this little dinky camera is like only $900. And I thought... And they're like, no, trust us. It's really good. And they were right. I don't use it anymore, because it's not 4K. But I still have it. It still works.

**Dave Jones:** Yep. I'm watching Possumus Woman now. Oh, yeah. You've done an aerial shot of like a small little beach kind of thing. How did you get that aerial shot? Because this is before drones. I think I just climbed up on a hill. Oh, okay. Oh, and zoomed in. Right. That's why I thought... Yeah, yeah. Right. Okay. That's... That's...

**Ben Heckendorn:** What's it called? It's here in Wisconsin. It's where the glacier split apart as it was smashing everything. Right. Devil's Rock. Yeah. Basically, I went there and stole a bunch of footage of people. And then edited it in to make it look like we had production value. Yeah, yeah. That's great. We didn't have drones back then. Actually, I'm... We made this joke, because we did the first one when we were teenagers in 1995. Possumus Man. Yeah. It's much worse. I mean, Possumus Woman is like at least... Well, it's a stupid movie, but it's fairly well put together. But anyway, we're saying, oh, 13 years. We have to obviously make the third one, since next year will be the 13 years between the sequels.

**Dave Jones:** Yeah, yeah.

**Ben Heckendorn:** It's just like that movie with Ethan Hawke where he meets that one woman over and over. So, yeah. We'll see if I'm feeling financially secure enough next year to bother making a stupid pasta movie. But you know the thing that's...

**Dave Jones:** I've got a name for it. What? You've done Possumus Man. You've done Possumus Woman. Oh, boy. The thing that now has to be Possumus he, him, or something like that. You know, it's got to be like pronouns.

**Ben Heckendorn:** I was thinking Possumus Men. You know, there's like a bunch of them, like aliens. Right. But we'll figure it out. But you know what? The thing that's... Possumus Pronoun is like... Yeah.

**Dave Jones:** That would be...

**Ben Heckendorn:** That would be... Yeah. That might be... That might be a little too clickbaity, but...

**Dave Jones:** Right. Yeah. Okay.

**Ben Heckendorn:** But yeah. But the thing that's weird is even though it's been a long time since I've done that, I bet all my friends would still do it for some dumb reason.

**Speaker ?:** Right.

**Ben Heckendorn:** That's great. Well, this... My character is allegedly Australian in it, and I have a terrible accent. Like, purposefully terrible accent. Right? And then this other guy I know who... Another friend of mine who is actually from Australia, but he lives here now. I was like, hey, you should play my long lost brother from Australia in the next one. And then I was also telling him that... He's like, oh, can we... And your kids are blonde. They should play a young version of me. I was like, I could be an American parent. Parents take me to Australia. They get killed, and I'm raised by dingoes or something, which explains my accent. So I came up with this completely stupid backstory. Oh, that's great.

**Ben Heckendorn:** And he's like, yeah, sure, Mike. Yeah, we can put my kids in it. Well, whatever. So we'll see. But then I was telling him he could be my improper dialect coach. I'm like, David, you must make sure that my accent is consistently awful. If I start to sound like an authentic Australian, you have to stop me.

**Dave Jones:** Yeah, yeah. You've got to stop me.

**Ben Heckendorn:** Oh, yeah.

**Dave Jones:** Brilliant. Yeah. So you've pretty much given up on the movies for the most part. It was a part of your life. It was a hobby.

**Ben Heckendorn:** It was a lot of fun. But, you know, you don't make any money off of it. We had actually been... Actually, David and I had been developing an actual, a quote-unquote actual movie. And we'd actually been exploring filming it in Australia because you guys have ridiculous tax rebates for film production down there. I don't know if you're aware of that. Actually, maybe you shouldn't look it up because you'd probably get mad at how good they are because you're a taxpayer.

**Dave Jones:** Yeah, probably. Right. So I'm going to be sponsoring your next trip down under whether I like it or not. Is that the...

**Ben Heckendorn:** Well, you know what? If I'm ever down there, I definitely have to pop out of your dumpster and we can film it. It's like, oh, look, there's a Yankee here. Yeah. Yeah. Yeah. Like I said, like, you know, if I don't make Possum 3 next year, my friends won't let me hear the end of it. So, yeah. Right. Hopefully, yeah. Cool. If I'm actually done with my new pinball machine by then, although it's going to be basically once we start, it's going to be like a year. So, yeah. Okay. I might have enough time next summer. I mean 2021. And my legs still work. So, yeah. I probably have to lose a little bit more weight, though, because I've gained like 30 pounds since I made that last movie.

**Speaker ?:** Right.

**Ben Heckendorn:** Does it matter? Oh, definitely. If you're like running around and carrying cameras and crap, it definitely matters. Yeah, yeah. I mean, what was that guy like, you know, speaking of New Zealand, Peter Jackson, like he used to look like Jabba the Hutt. And then he made three movies in a row. Now he's like super skinny.

**Speaker ?:** Yeah.

**Ben Heckendorn:** Oh, yeah.

**Dave Jones:** Oh, love it. All right. We should probably talk about, of course, the Ben Heck Show. Start us off. Like, how did that start out?

**Ben Heckendorn:** Right. So it was in 2010. So it was actually not that long after I made that possum movie. And I got a random email from an ad agency. It was Newark Element 14, or as you know them, Premier Farnell. They had an ad agency for their Element 14 initiative, which is basically like a social community for engineers, right?

**Dave Jones:** That's when they had started up. They wanted to do the whole Element 14 community in quote marks thing. Yes. Yes.

**Ben Heckendorn:** That was the major goal. And so what the ad agency had pitched to them was they said, well, what if we do like videos? And so this ad agency, it was really vague. It was really vague at first. They were like, hey, we have a client and they would like you. If they're wondering, would you like to make videos for electronic videos, basically? I didn't even know who the client was until like two months later or whatever. Oh, right. Right. And how did they find you? They just randomly emailed me like everyone else. Everyone randomly emails me. I don't.

**Dave Jones:** I think they may have emailed me at the time and I just went, no, I'm making my own stuff. 2010? Probably something. Yeah. Because I started my channel in 2009.

**Ben Heckendorn:** Yeah. It's quite possible. Yeah. And I had a YouTube channel, but there was hardly anything on it. I just put like random videos of like wires and stuff. So it was probably more my website. Although I found websites. I still have my website, but they're much less useful than they used to be. It's a small part of it. Yeah. Well, anyway, so then I had a couple of meetings with the ad agency out in San Francisco. I remember that because I was already there for a maker fair, actually. I think I was also the first one I went to. Then we had the corporate meeting in the summer and then they greenlit like a six episode pilot just to make sure it was going to work.

**Dave Jones:** So did they have the name? Did they have the theme of it and all that sort of stuff?

**Ben Heckendorn:** Actually, not really. It was very loose. So they were just like, we want you to make this show. So then I was shooting some stuff and I was doing electronics, but also like talking about video games. And they're like, oh no, we don't really want to talk about video games. So it was kind of loose at the beginning. Like I didn't quite know what they wanted. But then as I was doing the pilot episodes, I found out what they didn't want. And so. Right. And what was that? What didn't they want? It was like having my friend on and talking about Bioshock, the video game.

**Dave Jones:** Oh, okay. Yeah. Right.

**Ben Heckendorn:** Because they wanted to be about electronics. Now I will say like Element 14 was always very, very supportive of whatever we wanted to do. I mean, you know, sometimes they would have like a product or a certain company that they'd want to promote. Well, not promote, but, but, or like, you know, build this using the MSP430.

**Dave Jones:** Here's the new Intel board, you know, or something like MSP430. Yep. Right. The Intel's, what was that? Not the Edison.

**Ben Heckendorn:** The Arduino. I think it was the Intel Galileo. Oh, Galileo. Right. Yeah. And it was, it was had an x86 core, but then it used like I squared C to emulate the IO of an Arduino. It was so slow. Right. So we did this, we did the six episodes and then they, they approved us for like a full first season. And then we hired Alison to be the videographer and also do the rough assemblies. And we were still like mailing deep burnt DVDs of edits back then at that time. Yeah. Because back then, you know, the internet was like maybe, maybe 20 megabits tops.

**Dave Jones:** Yep. Yep. Because I, I heard through the grapevine that somebody that another, like some professional agency was editing and like doing all the editing on that. Is that right?

**Ben Heckendorn:** Oh, revision three. Yeah. That's a whole story. They're gone now. Right. So yeah. Okay. So, okay. Well, yeah, you make videos. So what, what we did was we never really had a plan as the episode is basically just film Ben and then edit the story or whatever. So Alison would do, I hired Alison because she, well, selfishly I use Adobe Premiere and I was actually a little bit ahead of the curve because back then, again, Adobe Premiere wasn't as popular as it is now.

**Dave Jones:** Right.

**Ben Heckendorn:** But she also had experience with that. I'm like, okay, we can work together on this. So then she would do a rough assembly edit, but it was basically everything in order. And then I don't know, I think we were still mailing, mailing discs or maybe we were FTPing it. We would send it to revision three over in San Francisco. And then they would do the polish edit, put on the lower thirds, put in the commercials and all that stuff.

**Dave Jones:** Right. And how long did that go on for?

**Ben Heckendorn:** What do you, what do you think happened, David? I'd be curious to get your prediction. It seems like you have an idea of what would have happened.

**Dave Jones:** Well, I suspect is that, well, they were, A, charging a shit ton of money to do this work. And it was, yeah. In fact, I do kind of sort of heard how much they were making at the time. And, and it's more than you probably.

**Ben Heckendorn:** Yes. Way more than me. Yes. Yes. I was actually a little shocked when I saw the number and, but they're, they're gone now. So we can say whatever we want. Right.

**Dave Jones:** Yeah.

**Ben Heckendorn:** Of course. Well, of course the people still exist, but yeah, there were, there were really good advantages. They had very good distribution channels. Cause like, I know when we stopped using them, people were like, oh, I can no longer watch your show on my Roku or through the Xbox app.

**Dave Jones:** But right. Okay. Yeah.

**Ben Heckendorn:** It was astronomically cheaper to have Alison work full time and do basically a near final edit and then send it to Newark because they have their own video department just to put on the lower thirds and the, uh, the pre-rolls and all that. Yeah. I mean, I want to say, well, I shouldn't say the number because I think I'm still, I'm not quite out of my NDA yet, at least for non-compete. Uh, but yes, it was a lot. It was a lot of money.

**Dave Jones:** It was a lot of money folks. I can, yeah. Per episode. You'd be shocked. Like I can remember hearing the figure and it was like, holy crap, that's more per, they charged more per episode than I've spent on all of my YouTube career, including all of my gear combined. Like, and that was just for one episode.

**Ben Heckendorn:** Yeah. And well, I guess that's why when we went there, they wined and dined us pretty well. And, but I distinctly remember, cause we, we went there a couple of times. Uh, we were in San Francisco and Allison was with me and, uh, they're like, oh yeah, we were down in mountain view. Cause I think we just were, we were hanging out at Google and then they're like, oh, we'll send a car to bring you up to San Francisco. We're having a happy hour. Right. And I remember, I remember we had, we had a very good chat with the car driver. He was really funny, but then we get there, uh, they're doing a tour and actually the woman who was working at, uh, revision three actually was from Madison, just like us. And anyway, so she points to this room and she's like, and this is where the Ben Heck show is edited. And I looked over at Allison, I looked over at Allison and I could just picture like cartoon smoke coming out of her ears, you know, in frustration. I mean, I knew Allison well enough by then to know exactly what she was thinking. And, uh, yeah, that was, yeah. But anyway, so yeah. So, um, so there definitely were some drawbacks to doing it internally, but financially it was advantageous. And then, then, yeah, we, uh, I think we only had them like the first two or three years, although they, they did have really good advice. Like early on, they're like, you guys should do it every week, not bi-weekly because of the increased viewership, even though. Yep. I mean, one thing I, I, I've said this before, but the schedule of that show is one of the main reasons I got tired of doing it.

**Dave Jones:** Yeah. I was going to ask about that. That's insane.

**Ben Heckendorn:** 52 episodes a year. And then you had to double up to take off time for Christmas and whatever.

**Dave Jones:** Oh no, no. So yeah. So some weeks you were doing two.

**Ben Heckendorn:** Oh yeah. Some weeks we do three.

**Dave Jones:** Oh, and the thing is, how do you do it? That's insane.

**Ben Heckendorn:** Your, your blood pressure goes up to like 180. That's how you do it.

**Dave Jones:** Oh no.

**Ben Heckendorn:** Yep. I mean, they, they, they always, they always treated me well. I mean, it was very advantageous financially, but yeah, after like eight years, I was like, I, I, I need a break, you know? And yeah, I, I'm, I'm more, I'm more chill than I was then. So, but yeah, I mean, it was, it was a really fun ride and, uh, there, and they're still doing it. They have element 14 presents. Oh, by the way, calling it the Ben Hex show was not my idea. I wanted to call it. Oh, okay. I wanted to call it circuit breakers.

**Dave Jones:** Circuit breakers.

**Ben Heckendorn:** Which would have made it easier.

**Dave Jones:** It sounds very eighties. It sounds very eighties movie. Kind of.

**Ben Heckendorn:** Thing is when, when I was like, I'm going to like, we, we had an exit strategy for me, like almost two years before I left. Right. Right. And it was like, it was like, oh, we're going to bring on somebody else. And they brought on this, we were talking to this one guy, but then he got another big contract. So he's like, okay, I'm no longer interested. And then they changed it to like a hack, like hack challenge. And then like, oh, now we have to rebrand it. I think they rebranded it to something other than Ben Hex show for like 10 seconds. And everyone freaked out. So they had to switch it back. So even though, you know, selfishly calling it the Ben Hex show would make it really hard to fire me. However, when it came to transition the show, it, it posed a lot of challenges. So now it's called element 14 presents max who Alison was there for four years. And then max was the new editor and he actually is still the editor. Of all the content sent in by the video content producers. Yeah, but it was a lot of fun. But another thing, I also got tired of all the travel. I mean, I know some people traveling, but it gets old.

**Dave Jones:** Yep. Why, why were you like, first of all, where was it? Like, did they like, did you like have a, a, like a head, like a lab somewhere? Like it obviously wasn't shot in your home or anything like that.

**Ben Heckendorn:** And we had, well, we had two different shops. We had one shop for four years. And then the last four years we moved into a larger shop. Because originally it was just me. Then it was me and Alison. Then it was myself, Alison and Felix. And then it was four of us eventually. Yeah. So we were, like I said earlier, like if we were still filming it now, we probably would have been shut down actually during this, but yeah. So we, we were doing it in a industrial park in a building and then we put up all the lights and we got, we got one of the things I got tired of. It took so long to put up individual like C-stand lights that like one weekend Felix and I lined all the, like, if you look at the top of a room, all like the, the edges of the room, the ceiling of the walls, we lined it all with fluorescence and then hooked it up to an Alexa switch. So we can instantly make everything super bright, but if you didn't want it to be on all the time because it was too bright. So we would, we would only activate it when filming because otherwise, and then also, uh, I can't, yeah. It also makes it hotter, you know, in the summertime, it makes it too warm to have the lights on. That's another thing you have to think about. So that was, that was kind of interesting, but yeah, all in all, you know, it was a good run, but eventually, yeah, the schedule just got to me and I was like, I've had enough.

**Dave Jones:** Uh-huh.

**Ben Heckendorn:** Yeah. It's like, I've made, I've made X amount of dollars. I think I've had enough.

**Dave Jones:** Right. So you actually, were you still like contracting for them or were you an employee? How did that work?

**Ben Heckendorn:** We were all 1099 contractors. So I have been self-employed for 16 years now. Got it. Well, yeah. A lot of times it had like all the negatives and positives, no, all the negatives of both a regular employment and self-employment because you have a nine to five schedule, 52 episodes a year, but you still have to pay your own health insurance or, you know, and do your taxes. And then the big thing we have in America that a lot of employees don't realize is that your employer pays like social security, Medicare, unemployment tax, all this other stuff that you never see, but self-employed people see it. It's actually a lot. Yeah. Yeah. But yeah, you know, as far as travel is concerned. So yeah, I would go to two maker fairs every year, probably at least two conventions plus my other travel. So nowadays I'm like, oh, I'm only going to go to the conventions. I want to.

**Dave Jones:** So was that for the show or was that to just, they wanted you to appear?

**Ben Heckendorn:** Oh, they would like, they would have a booth or then I think they got bought out by Avnet. So the last time I went to maker fair was we had a big Avnet booth. So we did meet and greets. I talked to people and then we have like scheduled talk times. And I did like a Google, I did like a Google IO talk, uh, 2013. I did a TEDx talk, uh, in 2016. Uh, I, oh gosh, there's all sorts of stuff that I had. It's like, oh, go here, do this. And then, you know, yeah. Yeah. And it's cool, but I think I've had enough conventions for one life. I went to SAS a couple of times. That was pretty cool.

**Dave Jones:** Uh, yeah. We just don't have the option here. Like there are, there's virtually no conventions here. You know, we have one show every year, but that's it. You know, that's, that's the industry show and it alternates between Sydney and Melbourne. And it's the same show every year. What's the show? It's just a bunch of, it's the electronics show with an X electronics with an X fancy spelling. And it's just a bunch of, you know, commercial, you know, suppliers just showing off their latest oscilloscopes and stuff like that. You know, there's, there's no maker thing to it. We, we did have a, so I've never been to a maker fair. I've been, we used to have a mini maker fair here in Sydney. It was run by our powerhouse museum here, which is a big tech, uh, you know, museum here. And they used to rent it. And the first year it was a, like a maker fair branded. So it was a mini maker fair. And then the next year, suddenly it was, it was exact same thing, but it wasn't the mini, it wasn't the maker fair anymore. Cause they just said, Oh, it was too much red tape, you know, to, to do all the maker fair branding and all that. So then they wanted to control it in, you know, down to the nth degree and things like that. So they went bugger that we'll just run their own.

**Ben Heckendorn:** Was it still successful?

**Dave Jones:** Uh, yeah. Well, I thought the second year was better actually. Awesome. So, um, no, I, I don't know about in, you know, number of people turning up and stuff like that, but, uh, yeah, no, it was good. So, but then they've, but it was basically run by one person from the museum. And once he left, they just never did it again. It was one guy's passion pretty much. So yeah, we, we don't have any sort of anything here anymore.

**Ben Heckendorn:** That's too bad. And then to get to anything, you have to fly over vast oceans or India.

**Dave Jones:** Oh God. Yeah. I'm not going to fly to, you know, Asia or U S or somewhere.

**Ben Heckendorn:** And that's expensive to fly that far.

**Dave Jones:** Well, well, yeah, it is, you know, it's thousands of dollars and, you know, people ask me that all the time. Oh, why don't you come to, you know, Europe and why don't you come to America for this show or whatever? And it's like, actually, you know, I get invited, uh, to like, uh, you know, these sorts of things, you know, chaos computer camp or something, you know, wanted to fly me over one time or whatever it was. And it was like, you do realize it's like, it's on like the 27th of December or something. And it's like, I would have to leave, leave on Christmas day.

**Ben Heckendorn:** And, and the travel is going to be more expensive at that time.

**Dave Jones:** And the travel is 20 and it's 24 hours. Like, well, no, it's like 30 plus hours each way to Europe and just getting to the U S is like 30 hours of travel. So that's almost an entire working week. You know, it's like, Oh God, no, I'm so, I'm so over overseas travel.

**Ben Heckendorn:** I don't, I don't blame you. We, I think we only, we only had to do overseas twice. I want to say. Right. But that wasn't, and that was just to Europe. So that's only like eight hours. Although I had jet lag on one of those, on one of those, I have worse jet lag on one of those trips though, versus, uh, when I went to New Zealand, cause we were going West, West is easier than East. I've found jet lag.

**Dave Jones:** I've never had jet lag in my whole life. Oh really? Never had it. Oh yeah. I don't understand it. Yeah. It's just never happened to me. So yeah, I'm very lucky.

**Ben Heckendorn:** Well, I either don't get it, but I don't know. Well, and there was a, I think it was a crying baby on the flight, which, oh yeah. Oh, I do. I do have one more convention story for you though. Cause I know you want to stick to an hour, but the best one was freescale semiconductor in Austin, Texas in 2015, I want to say. Um, and so it was, you know, all these products that use freescale, this is before they got bought out by 10 other companies, but they, you know, they had the convention area, but every day they had two different lunches, like different ethnicities. So like for lunch and dinner, there was always a variety and it was always amazing. And they just brought food everywhere. It just appeared everywhere. And then at 6 PM, at 6 PM on the dot, the convention went until 10 at 6 PM in the dot, all these bars appeared everywhere, like mini bars everywhere. Like, like every five booths, it was insane. And then they had like a mega bar at each end. Like they put five of the bars together to make mega bars. It was nuts. And then they had, and then Steve Wozniak spoke at one of the things. And then at the very end, they had, they had the group cake show up. And so we had a cake party. Oh my God, it was so good. And they had, they had this microwave and I think it was controlled by a free scale, you know, MCU. And it was really amazing. It would actually analyze the way the radio waves with microwaves are bouncing off the food and use that to fine tune how it cooked the food. So it could basically make things that tasted like they were fried. And so Max and I kept going back to that booth because these, these delicious jalapeno bread ball poppers. They'd be like, Oh yeah. Nom, nom. Tell us a little bit about this microwave. Nom, nom, nom. Oh man. And then also at the time, Max was dating a week. He was dating a vegan. So once we got to Austin, Texas, we're like, we're going to eat barbecue every day. That was a really fun trip.

**Dave Jones:** Oh, I, I did go to one. I got, I did go to one, uh, invited, um, conference thing. They wanted me to blog their conference. This was back in my early days, 2010 or something. It could have been. Genesis was the company. Renesis. They had their big DevCon or whatever it was called. Oh, right. Yep. It was a DevCon event. Yeah. And, uh, so they invited me over there. And one of the big things was that during their dinner, you know, it was like a three day event and everything. It was huge. It was, ah, the catering and everything else was absolutely phenomenal. And, uh, they, they got in, um, all these arcade machines, by the way, which you'd love. They got a whole room full of arcade machines. And where was this? And this was at a hotel in Anaheim. Uh, this was in a plush hotel at Anaheim. And they took over all the, all the conference halls there in the hotel. It was a hotel conference center kind of thing. And they took over all three halls or whatever. And when they filled one with like pinball machines and mini part part and all sorts of, you know, uh, it was absolutely phenomenal. But one of the things I was supposed to do was at one of the main, uh, dinners there, one of the main, uh, dinners, cause you'd have, you know, breakfast, lunch, dinner, you'd stay there for the whole three days. And, uh, I was supposed to, we were supposed to have this Q and a discussion thing during dinner. And I was like, nobody thought about this. You've got a thousand people in a, like a big, you know, dining thing, you know, massively catered. And I was, you know, on a table with these other panelists and I was supposed to host this panel. And of course, like during dinner, nobody's listening. So I had to stand up on the table with the microphone saying, you know, everyone, can you shut up? You know, like we're going to do this panel thing and everyone just ignored us. And so we just had to shut it down and they flew me halfway across the planet to do this. And it was like, it just didn't work.

**Ben Heckendorn:** So they didn't plan that very well.

**Dave Jones:** It sounds like they didn't plan that very well, but I was, I also gave a keynote address announcing their new contest. So that worked and I blogged their event. So that worked, but yeah, the dinner that, yeah, that was an epic fail.

**Ben Heckendorn:** Oh, that's too bad.

**Dave Jones:** Yeah. Yeah. Anyway, I thought it was hilarious. So, yeah.

**Ben Heckendorn:** Well, you know, that, that's on them, not you.

**Dave Jones:** Oh, no, no, totally. I just got it. But it was so embarrassing. Here I am standing on a table yelling at everyone in this thousand people.

**Ben Heckendorn:** Did you, did you click your glass like at a wedding?

**Dave Jones:** Like everybody kiss. No one in here. Nobody even heard me with the microphone. It was like, you know, the big PA address system. Everyone just kind of, oh, there's a noise happening over there. What's that?

**Ben Heckendorn:** Thanks get back to. I just thought of something really dark.

**Dave Jones:** You could have yelled fire. Fire. They still wouldn't have heard me. That's too dark. Oh, they wouldn't have heard me. Oh, man. That's funny. And it was like, it was such a dog and pony show. It was like, and so we were having this dinner. And then after dinner was when they had these big black curtains separating the two halls. Right. And they go, oh, we're doing the big reveal now. And then after dinner, they pull back the curtains and there's the big arcade room and everything. And, you know, it was like, oh, whatever.

**Ben Heckendorn:** So what do the arcades have to do with their products? Just they thought they were cool?

**Dave Jones:** Absolutely nothing. It was just something they wanted to entertain people with. Okay. All right. So they hide in this company just to fill the place with all. And they had poker. And, you know, so they had poker. Like, you know, they actually got dealers in and poker tables and all sorts of stuff. Oh. You know, it was this epic thing. It was. Well, that part sounds fun. So, yeah, these companies love to spend money. You know, they just love to. Yeah, these big companies.

**Ben Heckendorn:** Yeah. And going back to the Maker Faire, like once that, you know, extravagant expenditure left Maker Faire, it kind of hurt it. So, because, yeah, I mean, they were, you know, Intel, Google, we're pumping a lot of production value into Maker Faire.

**Dave Jones:** Right. Do you think the Maker movement's kind of like dying the way, like the hype around it's dying the way 3D printers have kind of, you know, it's, or is it hard to tell?

**Ben Heckendorn:** I think it's still alive. Like I said, I think it's, even though, yeah, Maker, make.com or whatever is gone, I think the idea, it was pretty well instilled. You know, you've got a lot of young people excited about Raspberry Pis and Arduinos and whatnot. So, I think the seed was planted, even if the tree is dead. Oh, for sure. Yeah. Write that on a bumper sticker.

**Speaker ?:** Yeah, right.

**Ben Heckendorn:** But, yeah, so, I mean, and then, like we were talking about, I mean, you see a lot of knock-on effects. If it's like, oh, I need this I2SquaredC screen, you know, you can go to Amazon or any number of sites. And then, or, like, well, you know, you've been around a while. Like, if you're trying to do something back in the 90s or even the early 2000s, there's a lot less integration of packages than there. Or even, like, the Arduino interface itself. It's not like microcontrollers didn't exist before that, but that really, um. Oh, no.

**Dave Jones:** It was just, it was, like, I can remember when microcontrollers, it was a couple of thousand dollars to buy a dev kit for a PIC microcontroller. And, like, and you had to, like, you couldn't buy it. You had to go through a dealer where you had to have an account and you had to, like, you know, like, who are you? You had to be a big business to get this development kit for a microcontroller. It was just nuts.

**Ben Heckendorn:** Yeah, and now it's changed to, oh, I have to spend $35 for an Aviar ISP Mark II? I won't pay it. Oh, gosh darn it. But if you think about it, like, I was designing, or it's already been done, but we made a new pinball platform for making games or whatever, right? And we used Atmel SAM D21, the little ARM chip. It's basically the same thing as the Arduino Zero. Now, for that, I programmed it using Atmel Studio from the Metal Up, right? Right. But I think about that. Like, you might do it, you might, like, do it like that. Like, I do it like that because I want to know, you know, what every interrupt's doing, all the IRQs, you know, all the timers. But then you think about, like, this is, you know, yeah, not that long ago. This is how everything had to be done from scratch. And it's a very large learning curve or a cliff that you have to climb. And, yeah, the average person wouldn't have done it. But now pretty much anyone can pick up an Arduino. And, yes, there's a bunch of software, a code bloat and all that shit that's on there. But it still works. It still works.

**Dave Jones:** Yes, exactly. It gets the job done easily, you know, with minimal. Yeah, exactly. You don't have to dick around with the registers and getting it booted and, you know, all that sort of jazz.

**Ben Heckendorn:** There is, yeah. And then there is kind of the thing where, well, maybe not with Arduino, but just in general. There's a lot of IT people who don't, like, even know what registers necessarily do. So I do wish people thought about metal more or, like, oh, man, I'm going to use a byte instead of two shorts, you know, or something like that. So, but still, it's – and I personally enjoy programming things at low level because it's, like, I know exactly what's going on. Because even, like – Exactly. Even if he's, like, Atmel software framework, it's like, oh, I need a UART. And they're like, okay, here's 10K of code for a UART. It's like, oh, my God. Yeah, no, screw that. Thank you very much. But that's all been made much simpler. Even – I wouldn't say the last 10 years, but definitely the last 20.

**Dave Jones:** Yeah. I don't miss assembly code, though. I've got to admit, you know, back when 1K – back when 1K was a lot of memory on a microcontroller, you know, and you had to do assembly because, well, you were – you know, you didn't have a choice.

**Ben Heckendorn:** What were you doing assembly on? PIX, mostly. Back in the 90s, early 2000s?

**Dave Jones:** Back in early 90s, yep, it would have been, I think, something like that. So 1K or 2K of memory was, like, that was, like, the biggest pick around, you know. The PIX 16 – this was before Flash, right? Oh, God. You would have CMOS. So you'd have one time – you'd have – it used CMOS memory. It didn't use Flash memory. Sorry, it used eSquared Prom memory. It didn't use Flash. So it was the PIX 16C84. That was the – it executed from iSquared CE Prom?

**Ben Heckendorn:** Yes. Yes, it did. Oh, my gosh. So you would basically need assembly just to get any speed out of it.

**Dave Jones:** Yeah, well, that's what you did with PIX back then. Like, there were C compilers, but with only a couple of K of memory, you know, you could do it. But –

**Ben Heckendorn:** Well, yeah, because you wouldn't know how much bloat was added by the C compiler. Whereas, you do assembly, you know exactly what you're using.

**Dave Jones:** Yeah.

**Ben Heckendorn:** Yeah.

**Dave Jones:** That's it. Like, you couldn't add a printf. That was impossible because the printf routine would take up more memory than the entire microcontroller had.

**Ben Heckendorn:** Well, even now, like, I was doing a project. I was doing, like, a Z80 bootloader badge, like, for a convention that also was canceled. And even that, I was – not printf, but I was using a different print command because I was running out of – even in modern times, yeah, you use some of these functions. And you don't know what's under the hood, however many layers of abstractions, like function calling function. So, I'm like – yeah. So, I'm like, oh, crap, I'm running out of RAM because such and such is being copied from RAM to flash. And, yeah, I had to go through it. And then I'm like, ooh, I got back 2K or 1K or whatever. Woo-hoo! Yeah. So, I like to think, like, you know, program like RAM is still rare. That's my motto.

**Dave Jones:** Yes. Yes. Flash memory is cheap.

**Ben Heckendorn:** And then, yeah, you don't know how big the stack is, for instance. So, that's another thing. It's like that's always the creeping monster creeping down from the top of RAM.

**Speaker ?:** Yeah.

**Ben Heckendorn:** Yeah.

**Dave Jones:** Oh, fantastic. Well, Ben, I think we're – I think our amp hour is up, unfortunately.

**Ben Heckendorn:** Oh, that's – the amp hour went by very quickly. And we caught up with current news.

**Dave Jones:** Yeah.

**Ben Heckendorn:** He's here all week, folks. Try the veal. All right.

**Dave Jones:** All right. Thanks, mate, for joining us.

**Ben Heckendorn:** Oh, no problem.

**Dave Jones:** In fact, I can't believe we haven't had you on before. It feels like we have, but you definitely haven't, right? You haven't been on the amp hour before.

**Ben Heckendorn:** It's been long enough that I can't remember. Same here. It's been like a decade. I can't – I think the last thing that we did was that kid's toy thing that rotated.

**Dave Jones:** Yep, that's right. Oh, boy. Anyway, very cool. Thank you very much, Ben. No problem. Nice to catch up, mate.

**Ben Heckendorn:** It was a pleasure. And, oh, where can people follow you, by the way? Oh, right. So you can find me on Twitter. It's just Ben Heck. And then I also have a website, www.benheck.com. And then I do make YouTube videos, but now only when I want to. And that's on YouTube. It's called Ben Heck Hacks. Ben Heck Hacks. Fantastic. Not Ben Heck is a hack.

**Dave Jones:** Right. Right. Because you didn't actually own the trademark to the Ben Heck show, right? Kind of. Not real. Maybe.

**Ben Heckendorn:** There was a time, like, in the older contracts, there actually was a time where I would have been able to continue making videos with that channel. But I think they realized it was too valuable just to give away.

**Dave Jones:** Okay. Yeah.

**Ben Heckendorn:** So I want to say, like, it's season five or so that disappeared from the contract. Right. But I don't. But you know what? They paid to develop it. It's theirs. You know?

**Dave Jones:** Yeah. No, of course. Yeah.

**Ben Heckendorn:** I'm just a hired thug.

**Dave Jones:** Fantastic. Fantastic. Okay. We'll put our links down below for all your channels. And what if people want you to do contract work? Are you available for contract or does it only come through?

**Ben Heckendorn:** Yeah. No. If I have time. Like, actually, like, right now I'm a bit busy. But if you go to benheck.com, there is an email link and you can hit me up. Sweet. All right. Thanks, mate. No problem.

**Dave Jones:** Catch you next time.

**Speaker ?:** Bye.
