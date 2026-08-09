---
episode: 106
title: Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature
url: https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/
---

**SPEAKER_01:** This is the Amp Hour Podcast, recorded July 29, 2012. Episode 106, Temperative, Tegman, Temperature.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of ChipReport.tv. Hey, you've got something new. Whoa, yeah. More irons in the fire, huh? Oh, yeah, yeah. I've decided I... Didn't have enough to do, right? I dislike sleeping, yeah.

**Dave Jones:** Right. This marriage thing. Ah, yeah.

**Chris Gammell:** She's been very nice about it. I keep kind of using the same excuse. It's losing some juice behind it, but someday it might be worth something. I might actually... She's still buying it, whatever reason, she's still buying it.

**Dave Jones:** Well done. Well, keep on milking that cash cow.

**Chris Gammell:** Well, you know.

**Dave Jones:** Oh, love it. Yes. So, yeah, ChipReport.tv.

**Chris Gammell:** Yeah, .tv. I broke your rule of the .com thing, but... Yeah. Yeah, whatever.

**Dave Jones:** I like it, you know, .tv. Sorry, dude, it's not a new idea. I sort of had this idea when I first started the blog. Oh, wow. Yeah. That's okay. I don't care. But, hey, it's all in the... It's all out there, and, you know, who actually does the hard work and does it. That's what it's all about. Execution, yes. Ideas are like assholes. That's what they say, right?

**Chris Gammell:** That's right, that's right.

**Dave Jones:** Yeah, so what it is, though, is... Everyone's got one.

**Chris Gammell:** That's the saying. ChipReport's a weekly... Think of it like Chip of the Week, except... It's video. Not on the Amp Hour. It's video. There's, like, actually supplementary pictures and stuff like that. And there's your ugly mug standing there. My ugly mug on video, yeah. Yeah. It's very different. I've had to do a lot of modifications to my lab area. Yeah. It looks like a really...

**Dave Jones:** In terms of what, lighting and backdrop and stuff like that.

**Chris Gammell:** Yeah, really cheap-ass kind of studio setup.

**Dave Jones:** Right. Yeah. Which video camera are you using, by the way? That's my technical video blogger in me.

**Chris Gammell:** Oh, piece of junk. I don't know. It's not a piece of junk. It's DSC something-something. It's a Sony.

**Dave Jones:** Yeah, right. Okay.

**Chris Gammell:** Yeah, doesn't even matter.

**Dave Jones:** No, it doesn't. Yeah. As long as it works. You can overcome anything with lighting. That's right. It doesn't matter how shit your camera is, right? You can... If you've got enough light, it's going to perform brilliantly.

**Chris Gammell:** Yeah, exactly. Yeah. That's... For anyone else that's doing a video out there, they probably know that. Yeah, exactly. It's pretty crazy.

**Dave Jones:** But I've gone back to using my old... Oh, shit. I'm getting into video blogging stuff now. Yeah. Anyway, I've gone back to using my old cameras. I don't think our audience cares about this. And then I realize how shit they are just in regular lab office lighting. You know, like 200, 300 lux kind of range. You know, they're just so crap.

**Chris Gammell:** Well, that happens, I'm sure, with a lot of gear. I mean, not just cameras, but, you know, you go... What was it like going back from the gigahertz or the, you know, super expensive scope back to little scope? I'm sure you missed a couple things there, right?

**Dave Jones:** Yeah, yeah. It's painful, you know?

**Chris Gammell:** Yeah. So, I mean, it's the same kind of thing. It's the same thing with soldering irons, especially, right? Oh, yeah. So, like, you go from a, you know, nice temperature-controlled... Station. ...to a tip. And then you use, like, a little $25 special from Radio Shack. You're like, ah, this is terrible. And, yeah. So, it's... I know what you mean, though. It's any kind of gear. You know, once you get acclimated, you gotta really work with the junkier stuff. But it's good to start with the junkier stuff. I always say that, you know, it's always good to understand where you're going with it. Absolutely. I think.

**Dave Jones:** Well, there's so many people... Like, I know bloggers out there that are using, like, professional $5,000, you know, $10,000 studio cameras to shoot their video blog. And it's like, well, geez, you know, overkill. And they've got the full pro lighting as well. It's like, well, you've got all that pro lighting. And, well, you only need a $100 camera then, you know? Yeah. It's like, wow. You know, it's just a video blog. Yeah.

**Chris Gammell:** And it's like when you're starting out, too, with anything. I mean, like, you know, soldering irons, scopes, anything like that. Cameras. So I've been listening to the Adam Savage podcast now. So that's part of, you know, they're on tested.com or whatever.

**Dave Jones:** Oh, I didn't know he had a regular podcast.

**Chris Gammell:** Yeah, he's got a regular... I'll put it in the show notes.

**Dave Jones:** I'm going to sign up for that one.

**Chris Gammell:** It's pretty good.

**Dave Jones:** Okay. Is it like an hour-long show? Like how else?

**Chris Gammell:** Half hour. Half hour a week. Oh, he's always a busy guy.

**Speaker ?:** Yeah.

**Chris Gammell:** He talks about, you know, buy the junker tools at like Harbor Freight or something like that first. Figure out if you need it and then turn around. And if you do need it, buy the best your money can buy. And then, you know, never have to buy it again. Yeah. Which is great advice. I mean, because I've actually never been to Harbor Freight for tools or anything like that. But I've heard, you know, you can buy like, you know, like a $5 multimeter special kind of thing. Yep. And yeah, try it out. If you need it, go buy the best you can.

**Dave Jones:** Yeah.

**Chris Gammell:** I always have that idea.

**Dave Jones:** It's a similar thing to tradesmen I've had in, right? To, you know, do stuff around the house, right? They come in and I see them using these, you know, Ozito brand tools, which are like, you know, the El Cheapo, One Hung Low brand of power tools, right? And I always ask them why. And they go, well, you know, it basically does the job and it costs, you know, one fifth of the price of like a, you know, a proper Panasonic or something like that. And, you know, and it lasts like 80% as long, you know? And if I ruin it, I just toss it out and buy another one, you know? And it's like, well.

**Chris Gammell:** See, that's an opposite argument though, I think. I think that's an opposite. Yeah, I know. That's like a get along. You'll get along good enough, I think. And that works sometimes.

**Dave Jones:** It does work sometimes.

**Chris Gammell:** Like we've talked about on here, you know, if you get a three and a half digit DMM, you're going to get a lot of the case. You're going to get 80% of your cases, right? I mean. Yeah, yeah, exactly. The times when you need a six and a half or more is not very high.

**Dave Jones:** One thing where it doesn't work is rechargeable tools. Like you buy the cheap rechargeable tools and those batteries are just crap. And that's just going to ruin your day. Right. That's just awful. But yeah, all these, you know, when you're plugging your drill into the mains power cord or a jackhammer or something, you know, you can just, you can get away with the cheapies even for these tradesmen. So yeah, go figure.

**Chris Gammell:** Yeah.

**Dave Jones:** So how do we follow Chip Report TV? Do you want people to mainly subscribe on YouTube or do you want to drive them to the website where you can monetize it?

**Chris Gammell:** I don't care about that.

**Dave Jones:** I'm just trying it out, you know.

**Chris Gammell:** So the website has the show notes. That's a lot of people like that. So you can just go listen or just read the show notes if you want to. It's almost like the script if you're not into video.

**Dave Jones:** And it links directly to the data sheet and stuff like that. Yeah.

**Chris Gammell:** Yeah, exactly. And I'm going to post the audio too. So it'll be kind of like a podcast. And eventually I'll post the videos to be like a podcast as well. But for the subscription side right now, the easiest way is YouTube. Right. So I really don't have any like single source ways because the thing I've learned from this show and from other shows I do is you're never going to cover how everybody wants to do it. You just offer as many as it's feasible at the beginning and then, you know, wait for the complaints. So, but yeah, YouTube's nice. I like YouTube subscribing. Yeah, so do I. It's good. Hopefully a lot of our listeners are already subscribed to you. So it would just be another one on there.

**Dave Jones:** Sweet. I just hit 25,000 subscribers, I think.

**Chris Gammell:** Wow.

**Dave Jones:** Holy cow.

**Chris Gammell:** Yeah, that's great, man.

**Dave Jones:** I know. It's awesome.

**Chris Gammell:** Someday maybe. Someday.

**Dave Jones:** Ah, yeah. Someday I'll be successful.

**Chris Gammell:** Okay.

**Dave Jones:** I'm doing it full time. But, you know, I'm just, I'm still, you know, chicken feed in the scheme of, you know, number of views and stuff like that, you know. Number of subscribers, number of views.

**Chris Gammell:** As Chris said last week, it's quality, not quantity. Right. So I think we got some good listeners and you have good viewers and stuff. I agree. That's all I care about. Another YouTube group that we like, and I think we've talked about on here before, is the Signal Path guys. Yes. And so, Shariar, I think is how you say his name?

**Dave Jones:** I can't, I don't know how to pronounce his name correctly, so I won't try. Shahia?

**Chris Gammell:** Shariar, maybe? Yeah, maybe Shariar.

**Dave Jones:** I did try, there you go.

**Chris Gammell:** Yeah, yeah. Yeah, I'm sure. Anyways, they've got a cool, he's got a cool video up. I was watching it this week and I highly suggest people check it out. It's, he's actually doing liquid nitrogen cooling of passive components.

**SPEAKER_01:** Hmm.

**Chris Gammell:** So he's got an LED and then he basically dunks it and then the result is really cool. He actually shifts the band gap. So the color of the LED changes.

**Dave Jones:** Yeah.

**Chris Gammell:** It's awesome.

**Dave Jones:** Which is probably not surprising. That's exactly what it's supposed to do. Is it?

**Chris Gammell:** That's the thing, like it's been a while for me since, you know, band gap days and all that stuff.

**Dave Jones:** I don't remember any of that shit either, but it just doesn't, you know, strike, like I didn't see it and go, wow, it does. I just went, oh yeah, that doesn't surprise me, you know. Really? Yeah. Man. You know. Is your boyhood wonder gone? Things change drastically with temperature. What's the matter, man? Everything in electronics changes with temperature.

**Chris Gammell:** I mean, it doesn't. I totally agree with that. I've run into that problem before. Oy, yeah. What kind of ranges do you, so when you're designing like USB power supplies and stuff, do you give a toss, as you say, I mean, about temp range or do you just kind of say, eh, zero to 70 parts and done with it?

**Dave Jones:** Well, you don't give a toss about under zero, for example. I mean, you know, who's going to use the freaking thing outside in Antarctica, right? I mean, you know. You are right in now. Right. Yeah. Come to pitch now. Right. I'm happy to give those people their money back, you know.

**Chris Gammell:** Right.

**Dave Jones:** If you don't like it, because you're in Antarctica, well.

**Chris Gammell:** And your condolences for being so cold there, right?

**Dave Jones:** Oh, boy. You know, I don't care too much about it, really. You know, unless there's some formal reason that I need to do it, which I have often done for work, you know. Yeah. Yeah, definitely. But, you know, yeah, my own personal projects, because I know they're going to be mostly used in the lab, mostly over, say, from, you know, they won't even get down to zero, you know. They'll go from, you know, five, ten degrees minimum. Basically, if you're sitting there in your lab, freezing your ass off at five to ten degrees, then, you know, I mean, it's pretty, it's not a very pleasant place to work. So, very pleasant.

**Chris Gammell:** You're not designing, like, stuff you could go put at a substation somewhere or something like that, right? And you're making development equipment in a best-case scenario, right?

**Dave Jones:** That's right. And then at the high end, of course, it's different, because you're not going to work in over 40 degrees, personally, right? Once, you know, ambient, we're talking about. But in terms of the high end stuff, components heat up, especially power components. So, the high end is much more important than the low end.

**Chris Gammell:** Right, yeah. And so, you've got to have to calculate whatever the temperature rise is going to be, and that's always based on your packaging in that case, right? Yeah.

**Dave Jones:** So, that's much more important than the low end. I basically don't care about the low end. It's not that important.

**Chris Gammell:** Right, right. And, you know, and you think about the low end, too, right? In reality, if you had a nominal 30 degree rise in your case, then you could technically go down to minus 30. And then it would rise up to, I mean, you couldn't guarantee it, right? But I always think about that. And that's why the low end is even less of a problem. Because, you know, if you just spec some kind of on time, you know, say, oh, you have to warm it up for an hour or something like that, then, well, that problem's gone. So...

**Dave Jones:** And then if your item's powered from batteries, then you've got another whole world of hurt, right? Oh, yeah. Because batteries are very poor performers down at low temperatures, you know? Right. Well, you know, if somebody's using their alkaline battery at zero degrees and wondering why the, you know, the bloody thing isn't working, then, well, there's your problem. Yeah. Right? You know? Right. So, yeah, there's a limit. There's a line you've got to draw there, you know, where you just don't care that much. You know, it's not worth the extra design effort because, you know, especially if you know it's mainly a bit of lab gear or it's, you know, something like that. So... Right. Well, and... I know it's not super professional to think like that, but, you know, at some point... Yeah, it's practical, right? I mean... Yeah, it's practical.

**Chris Gammell:** Especially for, I mean, stuff that you're designing, if it's, you know, if you're selling it to other hobbyists and stuff like that, then it's... Exactly. It's... At that point, it's definitely not there. Yeah, because, I mean, I've done the design stuff, too, and it's like, you do have to... You do have to worry about that at some point, but really what it ends up coming down to is you spec it so that it's, you know, it's... So it's usable, right? I mean, like... Yeah, exactly. So you do, like, derating in the spec sheet or, you know, like... So you do, like, accuracy or derating in the spec sheet, so then you kind of do your error budgets and stuff like that and all that mess.

**Dave Jones:** And as far as electronic components goes, you don't have to worry about the low end. It's more the high end you've got to worry about. So...

**Chris Gammell:** Yeah. Yeah, the times I think about, like, the people who really have to care about this stuff is, like, Tom Lamentz, who we've had on the show, right? I mean, he was the automotive...

**Dave Jones:** Yeah, yeah, yeah, exactly.

**Chris Gammell:** You know, like, automotive electronics. You are... Your stuff is sitting outside, and it's... Mm-hmm. That's crappy, right? I mean, it's just... I think I talked to someone about automotive and, like, battery cold starts and stuff like that. And, you know, like, 12-volt batteries, they said those things will get down to, like, four volts, and they'll have to try and jump a car. Yeah. You know, like, try and crank a... Oh, I'm getting in trouble already. Try and turn over the engine, basically, with, you know, this battery. But it's usually 12, and now it's at four, and it's like, that's not gonna...

**Dave Jones:** That can ruin your day.

**Chris Gammell:** Yeah, that'll ruin your day, exactly. That's a call to AAA or your insurance company or something, right? If you can't handle it. So, that's... Yeah. Oh, boy. Temperature is a stinker.

**Dave Jones:** The Olympics is on at the moment, dude.

**Chris Gammell:** It is, yes.

**Dave Jones:** Have you been watching it? Did you watch the opening ceremony?

**Chris Gammell:** I did not watch the opening ceremony. I was watching water polo today, though. Oh. And I think the Olympics is, like, the ultimate time for nerds to be like, ah, I should go outside and run or...

**Dave Jones:** Right. You know, you have these perfect physical specimens and... What you do is you sit inside on the forum. Somebody started a thread. How do the timing systems at the Olympics work? You know? Like, that's what nerds do, right? They get together and figure out...

**Chris Gammell:** They get a lot of interesting questions.

**Dave Jones:** Yeah, exactly. Oh, boy. And it's great.

**Chris Gammell:** I love it. And there's a lot of technology like that. I was actually talking to someone about quadcopters the other day about... We started talking about, like, football, like American football, and, like, how they have the wire cameras. Oh, yeah. And how we wondered if the quads will ever actually become, like, film equipment for Olympics or even just any kind of sporting event. And I don't think right now, but I'm sure in the future it could be, right? I mean, you get some cool shots. Yeah, but they're very dangerous.

**Dave Jones:** Can't fly them over people. There's real major concerns there. Like, it's just... They're professionals. Eh. Yeah, right. So just make them light, whatever. Or is it not to do it? Yeah. Yeah.

**Chris Gammell:** But, yeah, there is interesting tech. And I think a lot of the Olympic stuff and, yeah, the timing and making that accurate and repeatable is interesting. But I think a lot of the camera stuff is really cool, too, because... Oh, yeah. Oh, for sure. You see a lot of, you know, a lot of innovation that's needed in order to... Did you see it?

**Dave Jones:** The stadium, the ceremony, the big... Every seat had a LED panel, had a multicolored LED panel. So the whole stadium was one big dot matrix screen.

**Chris Gammell:** No, I didn't see that. Oh, there you go. I'll have to find that video.

**Dave Jones:** And it was a bit wanky. I'm sitting, like, and they're showing close-ups of people. And there's this big LED panel sitting next to them, you know. So on their seat, like an armrest, like a pop-up, like a screen on the plane, you know, it pops up on the seat and, you know. Yeah. Yeah.

**Chris Gammell:** Well, is it just it didn't look very elegant or what?

**Dave Jones:** It didn't look very elegant when you were actually showing shots of people, you know. They're sitting next to this big LED panel.

**Chris Gammell:** Right.

**SPEAKER_01:** Well, it's not meant for them.

**Dave Jones:** It looked good from a distance, you know, the big helicopter shot showing the whole stadium and there is the big dot matrix screen. Yeah. Okay, cool. You know. And no, I enjoyed the opening ceremony. I thought it was good. Cool. Well, yeah.

**Chris Gammell:** And, you know, I just kind of missed it.

**Dave Jones:** So cool technology problems, though. Well, they had Mr. Bean on there. They had Mr. Bean. He's my favorite. Love him.

**Chris Gammell:** Really?

**Dave Jones:** Did you know? Bit of trivia. I did. Mr. Bean is an electrical engineer.

**Chris Gammell:** I did know this. Was an electrical engineer. Was. I think it's pretty safe to say he's out of electrical engineer territory. Yeah, I think so. But, yeah, Rowan Atkinson, he started as an electrical engineer and then he started getting into comedy and then.

**Dave Jones:** Well, I'm not sure he ever actually worked as an electrical engineer. But he did. Oh, you think he just went to school for it? Actually, he did do the course. So he did. Okay. That was his thing. Apparently, he did a degree in EE and then went to, I think, move straight into theater or something. But, yeah, technically, EE. Well, hey, man. We can claim him.

**Chris Gammell:** There's your mass audience, you know, once you get past that 26,000 mark on YouTube. Right. You could just switch over to comedy.

**Dave Jones:** Yeah, I'm going to get into physical comedy. Yeah.

**Chris Gammell:** Right. He's pretty funny, too.

**Dave Jones:** Oh, he's freaking awesome.

**Chris Gammell:** Yeah. So speaking of education, you mentioned Rowan at the university level. Did you see this Analog Devices and Digilant announcement?

**Dave Jones:** Uh, no.

**Chris Gammell:** No? Oh, okay. So Analog Devices and Digilant, who's an educational kit maker, basically, they're offering a $200 kit and it can act as a makeshift DMM and oscilloscope, right? Right. And you're like, oh, okay. Well, it acts as a, you know, oscilloscope.

**Dave Jones:** It's a USB connect. Oh, yes, I have seen this. It's a USB. You did see this. Okay. It's called the Analog Discovery.

**Chris Gammell:** That's right. Yeah. And you don't think it's much, but then, because it runs off your screen. It's PC-based. It's actually Windows-based. Yeah. But it's got, I mean, it's got a 125 mega sample converter, right? It's got a 100 mega... 14-bit. Yeah, 14-bit. Yeah. Yeah. But how much is your scope? I mean, most scopes are 8-bit these days.

**Dave Jones:** Yeah. Yeah. So, I mean, like, that's... They can go up to 10 or 12 with the high res mode with oversampling and then they average the samples in between. Right. So they can, you know, you can get an effective 12-bit res from an 8-bit converter. Yeah.

**Chris Gammell:** I mean, this isn't, like, it's not bad. It's a mega-ohm input. I mean, 20-volt max. It goes down to 250 microvolts per division. Yeah. So, I mean, it's not bad. I mean, they're gaining it up, obviously, so you're going to lose some of those bits. But, you know, but who cares, right? I mean, like, so it's, I think it's pretty great. I mean, this whole thing is...

**Dave Jones:** It's all right. I'm not that excited. I'm sorry. You know.

**Chris Gammell:** Well, I think you should get... This sounds like this is ripe for review, man. I think, I don't know. I was very impressed by this.

**Dave Jones:** Yeah, somebody asked that. Somebody asked, can I review it? You know, it's like, well, yeah, okay, if they send me one, I'm certainly not going to buy it.

**Chris Gammell:** Of course. Of course. But, you know, like, 16 logic analyzer and pattern generator and everything else, I think it's pretty cool. I mean, it's good. They're obviously targeting it for education, right? They actually have a discount for education. Yeah, right. Yep. But, you know, it's 200 bucks, man. It's not bad. It's not going to be like a scope, right? This isn't going to be a scope of placement.

**Dave Jones:** But there's so many of them on the market. I mean, there's just, that's what, you know, it makes me yawn. You know, there's so many things like this. There's nothing new here at all. There's nothing new whatsoever. Okay. Yeah. Sorry. I mean, you know, it's fairly highly spec'd, I guess, in terms of things. But once again, nothing new. I mean, it's... You got excited.

**Chris Gammell:** I remember you got excited when you had... You got all excited when you got that dual channel, you know, like 500 microvolts per division scope. And scope, I don't know why you wouldn't be excited about this. That's what I'm saying.

**Dave Jones:** Oh, I'm quite excited by the 250 microvolts per division. Yeah. But that's the only thing I see majorly exciting here. Sorry. Maybe it's all about the software. Maybe the software is really good. Well, in this case, yeah, it is. Yeah, it is. And is it open source? I don't think it will be. Or is it all proprietary?

**Chris Gammell:** It is not open source. And that was another thing. I was hoping they would open it up for, you know, open up the API for Linux. Oh, yeah. No, that's a crock of shit.

**Dave Jones:** No, thumbs down then. No.

**Chris Gammell:** Yeah. Windows only. That is a big downside. And actually, we... John Shook from your forum and a couple other places online, he actually asked on their Facebook page if they planned to open it, and they said, anew. So that was on digital.

**Dave Jones:** Well, then why are we promoting this shit then?

**Chris Gammell:** I still think it's interesting. If you can get it for $99 as a student.

**Dave Jones:** No, go away. Anyway, if somebody can write a driver for this. So... But then they haven't open sourced the hardware, so they'll bloody sue you if you go off and make your own, you know?

**Chris Gammell:** Oh, I think this is... This is basically a dev kit. I mean, they're trying to... They want you to build your own. They want you to at least design in the part, so...

**Dave Jones:** Yeah.

**Chris Gammell:** Right. You know. They're selling parts as much as anything else here, I think. Oh, of course.

**Speaker ?:** But...

**Chris Gammell:** Eh, I thought it was newsworthy. I liked it.

**Dave Jones:** And you probably can't make your own for the same price, because those analog devices parts aren't cheap, I'm sure. They're kind of like... But the Rolls-Royce parts in the industry, you know?

**Chris Gammell:** They are the number one converter company in the industry, I think.

**Dave Jones:** Analog devices do not make cheap parts. They make really good ones.

**Chris Gammell:** Yeah.

**Dave Jones:** At a really good price.

**Chris Gammell:** Really good, quote-unquote, yeah. Yeah, exactly. Yeah.

**Dave Jones:** Oh, boy. Anyway, I'm not talking about that anymore. Nah.

**Chris Gammell:** All right. Next. Okay, here we go. So, this would be... So, one other thing I was excited about that thing for was the argument of, well, you know, headless test equipment, which we've talked about on here, right? And the... Oh, as in display-less, headless. Display-less, right. Display-less and or using a... And using your tablet for... Yeah. Yeah, using an off-the-shelf tablet. And...

**Dave Jones:** This was another one of your big calls, you know, just like the chip maker machine that, you know, we'd all be using our tablet to, you know, use every widget under the sun, you know.

**Chris Gammell:** And... Someday, I will be vindicated as a technologist. You will see. Ray Kurzweil ain't got shit on me. That guy's crazy. Anyway, the Antipasto hardware blog, those are the guys that they did the liquidware kit that was built on top of the beagle board and everything else like that. They actually have a post about that and doing quite the opposite of what I suggest. Because I was saying, oh, yeah, well, you should just use an off-the-shelf tablet, right? And they actually have a post about using... customizing your own Android tablet and not doing that. And I'm sure that there's a little bit of something in there because they sell these things, but on the other side of things, you know, there are some valid reasons in here.

**Dave Jones:** Which I should point out to you last time.

**Chris Gammell:** Yeah, but they actually do it in, you know, an eloquent and...

**Dave Jones:** Right, yeah.

**Chris Gammell:** ... concise manner, right? Not just, oh, no, you're wrong. I don't do eloquent. Yeah, but I mean, they do make some good points. And I think you might have made some similar points. I might concede that. Maybe. Maybe. Please.

**Dave Jones:** Anyway, we've got a follow... All right.

**Chris Gammell:** Yeah, go ahead.

**Dave Jones:** We've got a... It follows on from the DigiLint thing, right? Not opening stuff up. Bloody hell. This pisses me off a bit, I tell you. Heathkit. Schematics.

**Chris Gammell:** Oh, yeah. I saw you post this.

**Dave Jones:** Yeah. Yeah. Somebody pointed out on the forum. Sorry, I don't remember who it was, but, you know, Heathkit haven't been around for like, you know, 30 years or something, right? Since before you were born, Chris. You haven't gone that long? Hell yeah. Hmm. Anyway, right? They make all these old gear, right? And there's a lot of... Yeah, they used to make kits and everything like that. Yeah, kits and all sorts of stuff, right? So there's lots of enthusiasts out there who want to maintain this gear and, you know, and build upon them. Right. And you could build scopes.

**Chris Gammell:** You could build TVs. Exactly. You could build stereos. A lot of stuff, actually.

**Dave Jones:** Yeah. And you used to be able to get all this info online, right? For all these old kits. Great. And then some dickhead... Hang on. I've got his name here. I'm going to name him. Hang on.

**Speaker ?:** Hang on.

**SPEAKER_01:** I'm ashamed. Yeah.

**Dave Jones:** And Don Peterson. Don Peterson. There you go. From Data Professionals. He's got his own little company, right? He's from California. And he apparently is a former Heathkit employee, right? Which is great. But what he's gone and done is basically bought... His company has bought all the copyrights to all the Heathkit documentation. And now he's actively going around getting all the content pulled off the internet, apparently, and so that he can sell it himself, you know, so that he can control the whole market and for Heathkit documentation and sell it. And it's like, I'm sorry, there's a line in this industry that you shouldn't cross. And he's crossed it, quite frankly. And it pisses me off. It's just, you know... No. You just do not do it.

**Chris Gammell:** We should give the background to that, too, because basically, they tried to bring Heathkit back. There was a recent resurgence in it. That's right. And they tried to sell some kits again.

**Dave Jones:** I'm not sure if it was affiliated with the same...

**Chris Gammell:** I don't think it was the same owners, but it was definitely... I mean, it was the same. I mean, it was the brand name and everything else like that. They were trying to bring it back. And they had a good name to go on. But then about a month and a half ago, I think, they said, oh, no, it's done. They're toast, right? Yeah. And then even just like last week or the week before, there was actually a... You know, there was an auction site. You can go online. You could buy like all the old office gear from the Heathkit offices up in Michigan. And it was very apparent that they are not coming back. There is no chance. And at this point, I think it was like, you know, a couple of guys in a warehouse were, you know, trying to keep the dream alive. But yeah, it's over. Which is sad. I mean, it is because it is a great name. And now this guy bought all of it.

**Dave Jones:** He bought the documentation. Yeah.

**Chris Gammell:** It almost sounds like patent trolling, you know? It almost... I mean, it's not patent trolling, but that's the feeling it is. Yep. Yeah. So, like, if I own it and I posted it to my site, then does he actually have a case against it? I don't understand. If you own what? If I own like a PDF copy of the... If I own a Heathkit device and I put the schematic online... No. He owns a copyright to it.

**Speaker ?:** I'm in trouble.

**Dave Jones:** End of story. You have not been reassigned. You have not been assigned the copyright or a use of that copyright. So you can't put it online. You can keep it for your own personal use, but you can't share it. No? And he's clamping down on it, apparently. I don't know all the details, but... Yeah.

**Chris Gammell:** Hmm.

**Dave Jones:** What a loser.

**Chris Gammell:** That is lame.

**Dave Jones:** Yep. That is very lame, indeed.

**Chris Gammell:** Lame. Lame.

**Dave Jones:** See, if he bought all the copyrights and then released them all to the world, he'd be a hero, right? Get standing ovation everywhere he goes. But no. For a little while. Now he's, you know, the personification of evil in this industry.

**Chris Gammell:** I don't know if I'll go that far. For somebody who does that. It's pretty lame. It's pretty lame. Yeah.

**Dave Jones:** Not happy at all. Yeah. Spoiling everyone's fun. Not good. Yeah. Just for a little, you know. Because he, you know, his eyes lit up. Oh, I can see the profit now. Everyone needs all these Heathkit schematics, you know. This huge hobbyist industry out there. Oh, I'll sell it to them. I'll buy the rights. Yeah.

**Chris Gammell:** You gotta source all your own parts now, too. And I mean, half of those parts. Yeah. I mean, if you're looking at original schematic, it's going to call out like, you know, Dallas semiconductor. Not even that. Semiconductors, right? What the hell are those? It's going to, you know, it'll call out like, you know, nylon caps and stuff like stuff that's really hard to find. Right. Right. Exactly. Yeah. Like, really hard stuff to find. And because it's old. And, but on the other hand, if you abstract it out and you say, all right, resistor, resistor, here's the value, you know, like that. Yeah. Okay. Then that has value, right? And using it as a study guide and as a basis for your new models. But to be honest, you could do that now. You could, if you did get a hold of them in some manner, right? Maybe not a public way. You could make derivative type works and no one has to know, but. Because he doesn't know the patents. He owns the, he owns the copyright.

**Dave Jones:** Right. Yeah. And I'm sure he's going to claim, oh, I did it to protect the material, you know, to make sure it survived. Well, you could have just done nothing and then the company would have failed and then everyone would have just released the info and it would have been free and wild and survived for all time, you know? And. Yeah.

**Chris Gammell:** Yeah. That's too bad. Dickhead. Yeah. Speaking of schematics, DigiKey. It's kind of weird.

**Dave Jones:** Yeah. They've jumped on the bandwagon. Yeah. I haven't tried it. I don't want to try it.

**Chris Gammell:** Well, we should say what it is though. Yeah. Go on. DigiKey's trying to pull in schematics. So this kind of looks like a circuit B and even though it's a, even though it's a, what's that other one? There's, there's that online spice program, right? There's a lot of ways you can share schematics now, right? Yeah. Aside from just even sending someone else a PDF. But this new DigiKey one is supposed to be like, you can, you know, put a schematic in and you can share it with all your buddies and, and, and then, oh, surprisingly you can also buy stuff. Yeah, exactly. Which is the real reason they're doing it.

**Dave Jones:** But then what do you do? Once you put the schematic in there, how do you make your board? Electronics is a physical art. I mean, you know, it's not, the art is not necessarily just designing the schematic. You got to, you know, you've got to go that extra 10% and actually design your board.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** What do you do? You just have to redraw the thing in another package to get. Right.

**Chris Gammell:** And that's what it comes down to is ultimately this seems like a good idea, but what they should have done is worked with a company that actually makes layout software or. Yeah, exactly. I know. You know, like database software, right? And this is trying to do it all yourself and, and that's good. And I understand why they would do that because then they get to maintain control. But, uh, I still say, you know, like once, even if you did like an open source run, I mean, if you worked with like KiCat or Jita, right? Yeah, exactly. These would all be great ways to do it. You, you write your software in order to work with very readily available information like KiCat or Jita or even Eagle, right? Eagle's good too. I mean, or, uh, with someone you like, Diptrace, um, you know, all of these could work. That's a whole bunch. Yeah. And, uh, I would think that would be a little more productive, but I guess there, there is a little more work in maintaining that, but.

**Dave Jones:** I, I want to know where they got it from. It didn't just magically, you know, they didn't, you know, they must've bought it from someone, right? Or I don't think they've had some boffin in there sitting there writing it. Have they? Or have they, you know, teamed up with somebody and they're rebadging it?

**Chris Gammell:** It could, yeah, it could be. This is, I mean, this is pretty slick looking if you, you know, click on it. Um.

**Dave Jones:** It's, it's okay for like quick and dirty stuff maybe, but for a serious design, nobody's going to use it.

**Chris Gammell:** Yeah. Well.

**Dave Jones:** Because any serious design, you have to take it to a PCB.

**Chris Gammell:** Yeah. It's just ridiculous. Well, there is an export, there's an export link. Um.

**Dave Jones:** Export in what format?

**Chris Gammell:** Uh, I don't know. I haven't gotten that from you.

**Dave Jones:** You know, but it's no, it's no, you'd need that integration. You need the, no, fail.

**Chris Gammell:** Oh no, they export as PNG and PDF. So, DigiKey. No way. If you are, if you are listening, if you export into, uh, I don't know, what are all the Kaikad, uh, they've got some weird formats, right? Uh, you know, export to Kaikad.

**Dave Jones:** Well, Eagle now uses the open source XML format. There's, you know, XML, that's a great idea. So now there's a bit of an industry trend towards trying to use this XML format for schematic, you know, export and stuff. Right.

**Chris Gammell:** And also import then. That's another important thing. So I want to be able to export it, use it, you know, actually like do some useful work, do a layout and then push it back. Or even better, if you want to use these brilliant software developers to write stuff for open source programs, we would appreciate it. That would be all. And that is a competitive advantage.

**Dave Jones:** Do they have every part linked in?

**Chris Gammell:** Oh, I doubt that. I mean, I don't know. I'm guessing they, they talk to their database, so. You're right. Uh, you know.

**Dave Jones:** No, I, I think they failed here. They chose the wrong path. They had a golden opportunity to tee up with one of the major players in either the open source or the, you know, the low end. Because no, no professional is going to use this. Right. Let's, let's put it that way. Let's, you know, let's be frank. Right.

**Chris Gammell:** No.

**Dave Jones:** It's just not going to happen.

**Chris Gammell:** Yeah. If you're going to share a schematic, like if you want to share an easy way to share a schematic and you also need to buy it, or even if you, you know, want to just store all your stuff from DigiKey there. Right. Yeah. Um, was that, was that Chris we were talking to last week about that? Just storing it and being able to hit go and just buy everything at once? That was me.

**Dave Jones:** That was you that said that. That was you that said that. Oh, okay. Yeah. I have my bomb in DigiKey. So. Right. That's a good way to do it. So I just hit go and, yeah.

**Chris Gammell:** Right. And if you have these assemblies, then you know you're going to do it. Maybe, maybe then just to, you know, if you needed to visualize, oh, well, you know, U15 is obsolete or I need a different version of that now. So now you, if you wanted to visualize it, but you probably have that internalized already, right? I mean.

**Dave Jones:** Yeah, that's right.

**Chris Gammell:** If you're working on a schematic, you, you know that schematic because you have to, right? You, you understand all the parts and you can't just get away with having this really light, light knowledge of, if you're on board, it's your board, it's your baby, right? I mean, it's, you just have to know it well. And so.

**Dave Jones:** Right. So the end of the story is no pro is going to use it. So they're only looking, they're only shooting for the low end here and they haven't teamed up with the, with another low end player. It's just, they got it wrong.

**Chris Gammell:** Well, it's nice. It's a good start.

**Dave Jones:** What were they doing in their committee when they were sitting around thinking this thing up, brainstorming this thing?

**Chris Gammell:** Hey. Hey. Didn't they have anyone in there who had a clue? Hey, well, you think about the skill sets, right? I mean, that's, that's the problem a lot of times, right? If you have a team that's writing even just a CAD program, if you have a team that's writing a CAD program, they're likely mostly software engineers, right? Or if you have a team of electronics designers who are designing something for the oil industry, right? You're not on a rig. You don't know what's going to work and doesn't work. That's why there's application groups. But I always think if you can, you know, if you are an electronics designer, you need to go out to the rig, right? Or if you are a software person, you need to go use that, that CAD software. But especially at big companies, that, that's hard to do because you're like crossing these silos of, oh, well, you're an electronics designer. Why do you need to go to a rig? Well, because I need to know what it's used for. I need some context. Dumbass, you know? It's, it's, you know, that's, that's a lot of like, you know, you read about like project management stuff. Like, like Jack Gansel does this brilliant project management course. And that's a lot of what he talks about too, you know? Like he, and that's even just any kind of, you know, like lean, lean product development and all that crap and agile and everything else. It's all about getting quick feedback and, and also experiencing it yourself. That stuff, like context matters. That's the basics. You need to have a clue. And, uh, did you see that? Well, it's maybe not here, but we are welcome. We are, uh, you know, we're saying we're speaking our mind now. So there's some feedback. Hopefully they're, you know, maybe they're listening. Maybe. And if not, we can, uh, we can, we can, we can make it. We'll tie them down and we'll make them listen.

**Dave Jones:** Yeah. Oh boy. I hate it when I, you know, I pass up a golden opportunity to, you know, any company passes up a obvious golden opportunity to do something right. You know?

**Chris Gammell:** Well, sometimes it's about getting it out there, right? I mean, we've talked about it, like, like even with, uh, my, um, chip report stuff, right? It's not everything I wanted to do. It's, it's crap right now, but it's going to get better. I got people telling me what to do already. It's like, cool. All right. There's some feedback. I, I know what people want more, right? That's the, and you've talked about that before too, right? You know, you say, just get it out there.

**Dave Jones:** Yeah, of course, but this isn't trivial to do, right? It's not like you can churn out a thing like this in a day and get it out there. Yeah.

**Chris Gammell:** This isn't a text, the text editor or something.

**Dave Jones:** And, you know, I.

**Chris Gammell:** GUI based and.

**Dave Jones:** No, I'm sorry. From day one, they should have gone to somebody and teed up with some PCB CAD software.

**Chris Gammell:** They should have teed up with two brilliant podcast hosts that, you know, claim to know what they're talking about.

**Dave Jones:** Quite a substantial fee. Yeah, right.

**Chris Gammell:** See, now that's the thing though. If you do that, then you're never going to get to put some input in. But if you, you know, if you're legitimate, uh, want to, you know, I, I'd like, I'd like a tool like this. You know, I, I do. I've, we've talked about it on here before. We would love a tool like this.

**Dave Jones:** I've already got half of my parts on the digi key bomb system. Right. So if it tied in, Hey, this could have worked. This is a tool I could have used and promoted, but.

**Chris Gammell:** Right. No. Oh, and not even that. I mean, you think about the, the convenience of it. Right. And so, and we should say. Yeah. That's right. Digi key. If you're, it's not just digi key listening, Mauser, uh, anybody else. Right. If you have this stuff and you don't say it's really a leap of faith too, because it's not like, Oh, well, we have that on our site. You know, it's like, well, you got to actually branch out and be willing to work with other people. Right. I know that some of the other people have that. Oh, well, we have a bomb tool. It's a, you know, it's a Excel, upload your Excel bomb sheet. And we'll, uh, you know, we'll, we'll assign parts to that. And it's like, okay, cool. Um, you know, I can do that too. Uh, yeah. But it's, it's that, it's that third party stuff when it really starts to get valuable. So whoever does it first though, you have a competitive advantage. And, uh, and, and, and I would say that you could even chart, I don't want to say this, but I think that you could even, you know, for that one click ability for that Amazon effect that, that, uh, you know, buy it now thing, there's, you could probably sneak a margin percent or two a margin in there. Right.

**Dave Jones:** I wouldn't complain about paying a, you know, a few bucks to use their bomb feature. Yeah.

**Chris Gammell:** Like a fixed five buck cost or something. Yeah.

**Dave Jones:** Yeah. Yeah. Something. Every time I use it, it adds five bucks to every order. I, you wouldn't get, I don't think you'd get any complaints, although it'd have to be better than what it currently is. The bomb system's a bit quirky at the moment. It's user interface is not that great, but still the convenience of it is, is really good.

**Chris Gammell:** Yeah. It's there. So, you know, I know back to the drawing board guys. Oh boy. Yeah. Yeah.

**Dave Jones:** And, uh, you know, since I don't work on, you know, huge professional designs anymore, um, you know, my, my needs in the PCB CAD area are fairly simple these days. And yet it can't even do the simple stuff I want. Yeah. So, you know, I mean, so who's it for? If it can't even do bare basic minimum stuff, it's a fail around.

**Chris Gammell:** Yeah.

**Dave Jones:** Next.

**Chris Gammell:** Next. Ah, what about, so say you're buying a chip, right? Say you're on DigiKey or any other site, right? Right. And, and you're, you're, even, even you're in your, your, your CAD tool and you're designing it in. Do you ever stop and say, I wonder if this company's going to go bankrupt soon? Uh, do you ever say that?

**Dave Jones:** As in the company, who? The, uh, part manufacturer?

**Chris Gammell:** Yeah, the chip vendor. Yeah. Yeah. The, yeah. The manufacturer.

**Dave Jones:** Not really. Cause they're major ones I've been using for 20 years. I mean. Right.

**Chris Gammell:** Say like a major one you've been using for 20 years is about to run out of cash by next year.

**Dave Jones:** Oh, well they, they usually don't. They always get bored out, but we've talked about this before. These companies just do not fail, right? Somebody buys them out. The parts continue. Yeah. You know, at least. But it's a hassle, right?

**Chris Gammell:** I mean, so basically ST, ST Micro is running out of cash at the end of the year. And they're, and you're right. They're talking about it, you know, like the French government's ready to step in and yada, yada, yada. Okay. Cause you think of all the jobs at the fabs and everything else, but at the same time, uh, that really kind of sucks. Yeah. It could, it could, you know, I'm sure this gives.

**Dave Jones:** They could rationalize in quote marks their inventory, you know, their, uh.

**Chris Gammell:** Oh, like, uh. Their line of products or something.

**Dave Jones:** They could rationalize their line. Yeah. That, that kind of sucks. Um, that's happened on the odd occasion. They've rationalized, you know, some. What do you mean? Can you explain rationalize more?

**Chris Gammell:** What do you mean?

**Dave Jones:** Uh, they rationalize their product line. It means they dump products that aren't selling. Oh. And that happens to be, of course, Murphy's law says that's the one that you're using in your product. And, but nobody else is using it. Oops. So they dump it and you're left holding the bag, you know? Yeah. So. Yeah. That sucks. Yep. But even like a branding change, right? It's called rationalization of your product line. That's the marketing. That's the business wank word.

**Chris Gammell:** Okay. Okay. Well, the other side of it too is like, you know, you could have like, like they're talking about this article about, um, selling off that part of the business, you know, just like the micro arm. Of course. Because these are, these are huge conglomerates, right? You think about the biggest players out there. Oh, massive. T-I-S-T, you know, all these guys. Intel. Like, you know, if they spin off, even if they spin off and change the name, right? Like, uh, like, uh, Freescale. Freescale is a spin off of Motorola.

**Dave Jones:** Yeah, that's right.

**Chris Gammell:** Uh, you talk about bomb changes. I mean, like, you got to change everything then, right? You got to go through all your bombs and all your old stuff. You need to make sure all the part numbers change and stuff like that. So it's not a trivial, you know, a trivial venture when someone changes their name and, or even, even like part markings, right? I mean, that I'm sure you've had that before where you're looking at a chip and you're like, what the hell is that symbol? Yeah, exactly. It's, it can be, uh, it could be a hassle, especially if, I mean, for people reviewing electronic circuit boards on, on a YouTube, you might have some problems. Yeah, that's right. Yeah. At least you get to look it up. I saw at one point there was actually like a library of, of pictures of, of like logos and stuff like that. Yeah, I have no idea. I'm going to have to find that and put it in the show notes.

**Dave Jones:** I just couldn't be bothered. If I'm going overboard in a review, I go, oh, I don't know what that part is. Yeah. I just, you know, I'm not going to stop the camera and go bloody look up the internet and try and find a, you know.

**Chris Gammell:** Right. Yeah. And sometimes they, they obfuscate too, right? I mean, uh, I saw on, uh, Mike's electric stuff. He, uh, he posted about, he had some old military board where every chip got rebadged. So he didn't know what any of the guts were, but you know, they were all badged by the defense company. And, uh, but yeah, you know, like that, that can be a hassle if, if you're going from a Motorola to a free scale name, right. Or even if you're already at a free scale name, then you have to go and find old parts in your, in your, in your system at work. Right. That, that can be a hassle too. Absolutely. Because databases are not, uh, they're not intelligent beings, which is why they're not going to, you know, rise up and kill us yet, which is a good thing. But, uh. Oh boy. But then you have to remember, you have to internalize that. Oh, well, it's, it's not free scale back then. It was Motorola. So I should search under Motorola.

**Dave Jones:** Right.

**Chris Gammell:** So, um, so no, no considerations though for the, the, uh, the financial fortitude of a company when you're designing in parts.

**Dave Jones:** Not really. Oh, you know, I, like, like I'm not going to go out and, uh, use a chip from a startup and unless I absolutely have to like the, you know, there's some massively compelling reason to do it. Um, just because yeah, the odds of them failing are quite large and that part not being there in five years time is, you know, is very, you know, the odds of that is very large.

**Chris Gammell:** That's a tough part for the, for the, uh, chip company. I mean, we talked to, we've learned about that, right? That's their dilemma, you know? Yeah.

**Dave Jones:** But some, some, some, some developers don't care, right? You're doing a run and you know, you're, you know, you're doing a, you're, you're designing something that has a, you know, a 12 month product life frame or something. Well, you don't care if they're going to be there in five years time. Sometimes. Right. That's true. It depends on what you're designing, what market you're in. Yeah. So, I don't know.

**Chris Gammell:** Well, how about this, uh, chip company? Have you ever heard of the Arm chip company?

**Dave Jones:** I don't know. Who are they? Well, no, but seriously. What if they make a stupid name?

**Chris Gammell:** I know. Yeah. But we, so Arm, you know, it's like the IP vendor, right? They're actually developing the FinFET with TSMC, which means that they're, I don't know. I don't know if that means they're just not going to be, I mean, they're going to still be an IP developer, but.

**Dave Jones:** A FinFET? Is it a FET?

**Chris Gammell:** FinFET based chip, basically. So, they're working on, you know, they're working with TSMC who says, oh, well.

**Dave Jones:** I haven't heard of FinFET before.

**Chris Gammell:** Oh, it's the shape of the MOSFET, basically. So, it's when you're going from, you know. It's got fins on it, doesn't it? 32 nanometers, yeah.

**Chris Gammell:** Down to 20 nanometers. Right. Basically, the gate widths keep shrinking. And in order to get more surface area on a gate, what you do is you start using weird-ass geometries to get more surface area in a smaller, you know, XY distance. You actually start using Z.

**Dave Jones:** It's kind of like the winged keel, is it? Or are you too young to remember that? The winged keel? Where we whipped your ass in the America's Cup back in the 80s.

**Chris Gammell:** Oh, yeah, because everybody in the U.S. is like, oh, America's Cup. Is that sailing? I don't even know. Yes, yes. I'm a little young for that, Dave. Also, my sailing knowledge is not quite up to date.

**Dave Jones:** Right.

**Chris Gammell:** I know.

**Dave Jones:** Right.

**Chris Gammell:** No, but it's not that. It's kind of like, and there's lots of features like this, too. DRAM did the same thing to get the gate lengths longer. Basically, you're just trying to make the gate length longer in order to get the same transistor properties without actually making the physical overall distance longer or larger. Exactly. That's the basic idea.

**Dave Jones:** It's kind of like a fractal antenna. You know, you get the performance of the antenna in this tiny space. Yes, exactly.

**Chris Gammell:** You're trying to optimize for space. That's the basic idea. And so ARM is actually working with TSMC. And I don't think that means, I'm not sure. It feels like that they would be, you know, making their own chips. But I guess it'll just be, it just means that they have to try and, you know, go back and forth with the biggest fab in the world to try and, you know, design these, this IP. But I always figured that happened at, like, the vendor level. So then, like, TI would buy, you know, ARM's IP and then say, oh, we're going to work with TSMC or, you know, Maxim or whoever else is, you know, buying ARM.

**Dave Jones:** As engineers, do we care about this? Actually, all we care about is the end parts, right? Well, that's what I'm wondering, though. Can we get them? How much do they cost? What do they perform like?

**Chris Gammell:** What I'm wondering is if ARM is going to actually make a chip, though. That's my question, right? So Steve posted this on the EDA 360 Insider. But that's my extension of this is if ARM's working with TSMC and they announced a multi-year deal to develop a 64-bit ARM V8 processor, basically, does that mean, though, that they're

**Dave Jones:** becoming a hardware company?

**Chris Gammell:** I mean, ARM's doing it all now. I mean, they're not doing it all, right? I mean, other companies wrap peripherals around ARM. Well, that's the thing.

**Dave Jones:** A lot of people don't understand. You cannot go out and buy an ARM processor from the ARM company. Yet. They don't make chips. That's what I'm asking. Yeah, they don't make them.

**Chris Gammell:** Right.

**Dave Jones:** They just sell their core.

**Chris Gammell:** Right.

**Dave Jones:** That's it. And other chip vendors provide. That's why you can buy 20 different brands of ARM processor.

**Chris Gammell:** Right.

**Dave Jones:** Because it's just the ARM core.

**Chris Gammell:** But what I'm saying is right now, I mean, they just license it, but I'm saying that there's really nothing stopping them. I mean, they could hire a couple of peripheral people and develop IP.

**Dave Jones:** And they don't have to pay themselves a royalty. They've got a competitive advantage. But then that might piss off all their suppliers, all their customers, right? Because they're the ones paying the royalty for the IP. And if ARM try and undercut their market and bring out their own core, their own physical chip, then they've obviously got a competitive price advantage there.

**SPEAKER_01:** It's true. Yeah.

**Dave Jones:** And that would piss them off. And that's why they've been successful, because they don't compete in that area, I think. That's why they're successful.

**Chris Gammell:** Well, it's just an interesting case of frenemies and the chip industry, right? I mean, chip industry is way bigger than us or anyone, right? I mean, this is some big stuff, because this is billions of dollars and lots of smart people. But I was just curious, because it would shake stuff up if that ever did happen. Maybe I'm just reading it wrong.

**Dave Jones:** I think if they're going to bring out their own chip, I think it's the wrong move. I think it's just going to piss everyone off. Not good. Going in the wrong direction. Hey, guess what Tektronix are doing these days?

**Chris Gammell:** What's that?

**Dave Jones:** Tektronix now have a place where you can upload your own reviews of Tektronix products.

**Chris Gammell:** I don't know anyone who's ever reviewed a Tektronix product.

**Dave Jones:** There you go. They've got a website. You can go to the website, and it's tech.com slash ratings dash and reviews. Great URL there, folks. Yeah. How about you just do tech.com slash reviews or something? That would have been much better. Anyway, apparently you can upload. And tips on writing your review. This is what I like. Keep your review focused on your personal experience with the product. Describe the problem and the product is helping you solve and how well it solves it. I.e. We want marketing material.

**Chris Gammell:** Oh. See, they're calling right now, Dave. They're calling right now. Why are you talking about us? Yeah. They've already heard. This is. That's freaky. Maybe they bugged the scope you do have.

**Dave Jones:** Should I answer it?

**Chris Gammell:** No. No. No. So, they know.

**Dave Jones:** And, yeah. They're, you know. Well, yeah. And, of course, they had to put in, oh, you know, yes, we want you. We appreciate your honesty and all that sort of shit. But, no, they don't. Trust me. Right? If you really slag off the product, they're not going to approve it. Right? No. If you just rant on, rant and rave about how shit it is and how crap that they haven't bought out and laid a scope, right, they're not going to approve that.

**Chris Gammell:** Well, no. I'm sure. I'd be surprised if they did. I think it's more of a text. It's more of a text review thing, though, too. So, that's good.

**Dave Jones:** They encourage you to do video. They encourage you to do photos and video.

**Chris Gammell:** Yeah. Photos and video. But photos would be a text thing, really. It would be. It would be a text blog.

**Dave Jones:** But, no. They're after freaking marketing material. Which is okay. You can't blame them for trying, right? Right.

**Chris Gammell:** And, yeah, they get it from you for free. There you go.

**Dave Jones:** Get on there, folks. Upload a video. Just rant in. And see if it gets approved. Ranting about how they haven't kept up with the market and all that sort of stuff. So, how their scopes are old and slow. See if it gets approved, please. It would be hilarious. Boy. Boy. I'm certainly not going to do it because I don't give content to other people. Screw that. Right. I didn't expect you to. That doesn't help me. That just helps them. Right. Yeah.

**Chris Gammell:** Not going to happen. What else we got on here? Oh, this is actually kind of speaking of content. Dwayne Benson, who does work for Screaming Circuits. You've probably seen him. He is on Twitter and he's a couple other places. But he actually has been doing this really cool feature on Programmable Planet. He's like a marketing guy for a board company, which is out in the open. But he's learning about FPGAs and he's kind of just learning from scratch. And he's got these pretty cool articles about just kind of like the first pass of learning FPGAs. Which is a lot of people don't. I mean, if I hadn't have been gone to school specifically for, you know, and taking classes on programmable stuff, it's harder. I think it's a harder thing to get into than microcontrollers.

**Dave Jones:** Oh, it's a very big hurdle. FPGAs is a big hurdle. Yeah. It's, you know, it's a different paradigm to what you're used to. You know, it's a, yeah. You know, everyone's, you know, every electronics engineer knows how to program in C, right? Just, you know, and use microcontrollers. It's natural to them. Right. You know, but yeah. And then when you've got to do this HDL stuff, it's, you know, it's a different ballgame.

**Chris Gammell:** It definitely is. And, you know, and then branching out from, you know, we talked to Chris about this last week too. It's learning the parallel side of things. And he, I think he was not as impressed with the FPGA side of things because of the level of technology that's in the newer chips. But, you know, like one of the things that is nice about it is the parallel nature of it, right? It's not necessarily for processing side of things, but, you know, if you need some parallel logic, you can't really, man, you can't beat that stuff. You need to do like filters and stuff like that. A lot of digital signal processing is moving on FPGAs these days. And, man, you can do some cool, cool stuff on there.

**Dave Jones:** You can indeed.

**Chris Gammell:** Yeah. So, yeah, he's got some cool articles though, you know, especially like more of the practical side of it too, like the, you know, bringing up an IDE, actually creating bit files and, you know, just the format side of things. Awesome. And that stuff is, you know, it's good. And like we said before.

**Dave Jones:** I love people producing content. You know, five, 10 years ago, nobody was producing content. You know, it was like, it was so hard to get this sort of info. Now it's, you know, everyone's out there producing content. It's hard to get time to do it. Yeah. You haven't got time to, you know, you haven't got time to view it all.

**Chris Gammell:** Right.

**Dave Jones:** There's so much info out there. But that's a good problem to have.

**Chris Gammell:** Yeah.

**Dave Jones:** Awesome.

**Chris Gammell:** Definitely.

**Dave Jones:** I love people who produce content. They're my favorite people.

**Chris Gammell:** Thanks, man. I appreciate that. I like you too.

**Dave Jones:** Chippaport.tv. Oh boy. You're doing a lot of stuff now. How do you, how do you find time to do it all?

**Chris Gammell:** You know, I don't sleep. Don't sleep. Yeah. Don't eat. Don't, I don't know. There's, there's not really a secret to it. Keep a consistently low quality on everything I do.

**Dave Jones:** Right. Minimum effort, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** All that sort of stuff.

**Chris Gammell:** That's the thing, you know, and it's like, you know, getting into, you know, like a board design, right? Like I've been mid board design for a bunch of stuff, but I haven't been able, we were talking about this before the show, you know, like that last, that last 10% of something.

**Dave Jones:** That last 10%.

**Chris Gammell:** It's not easy. It's not like finishing stuff is a, I was remarking to Dave too, there was a Olympics commercial about, oh, well, the finishing isn't the important part. It's all about how you got there. And it's like, okay. Yeah. I agree with that. You know, like I would not be here without, you know, all of my years of training, but if I don't finish any projects, then who cares? Right. I mean, if I don't want to gold medal, then who cares?

**Dave Jones:** If I, you know, I'd still be tweaking my first video, you know, instead of having punched out 330 of them or something. Yeah.

**Chris Gammell:** Exactly. Exactly.

**Dave Jones:** It's just, yeah. You've got to finish stuff off and.

**Chris Gammell:** Yeah. Execute. Execute.

**Dave Jones:** I'm as guilty as anyone. We've talked about this before, you know. Yeah. I've been fart assing around on half a dozen different projects. I haven't finished any of them.

**Chris Gammell:** Yeah.

**Dave Jones:** I think I'm going to take today off and now I'm going to finish this bloody board.

**Chris Gammell:** There you go. Yeah.

**Dave Jones:** I'm going to lay the bastard out and order the parts and just, you know, instead of fart ass around, I'll just order the prototype from the PCB supplier and be done with it. If it's wrong, who cares? At least I've progressed, right?

**Chris Gammell:** Bodge wires are a brilliant thing. Yeah.

**Dave Jones:** Oh, you know.

**Chris Gammell:** Speaking of PCBs, actually, so Erin, a robot girl, she does a bunch of like little bird robots, the robo bird and everything. Right. She's got this really great time-lapse video of doing a board layout. Yeah. It's really great. It's got like chiptune music. It's got commentary.

**Dave Jones:** It's got annoying music in the background.

**Chris Gammell:** Yeah. It's like chiptune music. But it's, you know, like when you look at it, this is probably, you know, I don't know if she had the time of how long it took. But yeah, I don't think she mentions what speed it's at.

**Dave Jones:** Yeah. So you can't calculate how. And if it's edited or not. But it doesn't seem to be. Like she's just opening all these windows. One thing I noticed is she never went full screen. Yeah. It's like when I'm designing a board, I want the maximum freaking viewing area possible for my board and my schematic. In fact, I've got two screens, you know, I've got the schematic on one, I've got the PCB on the other.

**Chris Gammell:** Yeah. I'm spoiled like that too. Yeah.

**Dave Jones:** Dual screen. And like, and she's working in these little windows.

**Chris Gammell:** Well, you don't know how big this is though too. She could be on like a 30 inch monitor, you know.

**Dave Jones:** True. But still, hey, give me the whole 30 inches like I used to have at Altium. Everyone had three 30 inch monitors. Yeah. I mean.

**Chris Gammell:** Yeah. That is nice to have. But yeah, this is, you know, it's mesmerizing to watch. It's just, you know, just fast layout and everything. And it's.

**Dave Jones:** But it's not just the layout. It's her jumping to, you know, a, you know, a digi key or she's jumping over to a trace width calculator and she's jumping to a website and calling up, you know, other.

**Chris Gammell:** Yeah. And she does part creation. She does footprint creation and everything too. So it's, it really is a lot of it. Right. And it's, it's, it's, it's very hard to see any detail because it's very quick.

**Dave Jones:** Like it's, you know, it goes for six minutes or something and it's like at least six hours or 12 hours or something condensed down into. Yeah.

**Chris Gammell:** I'd say that's probably about 12 hours. Yeah. Yeah. But yeah, it's great. I really enjoy it. So people want to see. And she does some cool stuff for the traces too. She, she does, she ends up rounding everything out, which is not, not standard. I don't think. I mean, I usually do 45s. I don't know if that's standard or not.

**Dave Jones:** I do 45s. Yeah. I, the, it's very old school to round you. Yeah. It kind of reminds you like old, like trace out. The old tape. Yeah. The old tape layouts, you know. Yeah.

**Chris Gammell:** But I, I like that look. I think it's cool. I think it's a cool look.

**Dave Jones:** I don't know. I'm, I'm over it really.

**Chris Gammell:** Ah, come on. It's fun. But I think it's like a, you look at the old, you look at the old tape ones though. Then, and you know, it's not like a program where you actually have different widths, right? It's like, it's like you actually have like, it'll just kind of transition into a pour and you're just like, whoa, what happened there? You know, true, true artwork. Someone went a little crazy with their Sharpie or whatever.

**Dave Jones:** Oh, those were the days.

**Chris Gammell:** Yeah. Did you ever do tape, tape out like that? Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** I used to do tape layouts. Yeah. See, now that would be a good video. I think of just seeing what that looks like.

**Dave Jones:** Donuts and stuff, you know, stick down to, and you would have all the footprints. You would have all the dip packages and you would actually peel them off, you know, and you'd put them down and, and you know, that, that's how you created your IC footprints. And then you'd snake around with the tape. You'd have this big roll and then you'd run your finger along and you'd roll it out and you do the curve nicely. And while you're holding your tongue at the right angle and if you're a light box, you know, and, uh, yeah.

**Chris Gammell:** Yeah, man. I think you should get your hands on one of those and, uh, and do it.

**Dave Jones:** Well, I, yeah, maybe. I think you can still buy the stuff, but.

**Chris Gammell:** Really? Oh, that would be.

**Dave Jones:** Yeah. I mean. That's like a. Make a good old school video. Steampunk. It's pointless, right? Right. Right. It's just silly to do that anymore. Right. So, um, yeah, CAD came in, in the eighties, right? So, yeah.

**Chris Gammell:** Right. Right.

**Dave Jones:** This is a very seventies thing. Yes. So, uh. Definitely.

**Chris Gammell:** Yep. But you get all those cool pictures too, you know, like Bob Weidler standing over the table and, you know, like cleaning up these huge tables, right? It's like, it's a very physical thing then. Yes. Talk about having to be close to your design, right? Yeah.

**Dave Jones:** Well, some people, yeah, you would do it at, uh, twice. The size, you know, often a lot of people would do, you know, if it's a really dense professional layout, you might do it at twice the size and then you photo reduce it. Right. I never, I don't think I ever did twice. So I always, I always hid the one to one scale stuff. Okay. So, and, uh, you know, I had good eyes. Yeah. Could do that. Yep. And then I would actually do. Randy's calling again.

**Chris Gammell:** Is he? Yeah. Yeah.

**Dave Jones:** I, I, I would actually do my reverse side actually backwards. So I would actually flip it in my head and I'd do it backwards. I talked about this before. I think you have. Yeah. So, so then I wouldn't get any parallax error when I, um, when I actually, uh, photo, uh, expose the stuff because the tape would be physically pushed against the board instead of the tape being on the other side, et cetera, et cetera. Right. And then, and then you, maybe you do a two-step process where you, you, where you turned it into a negative first and then you use the negative on the negative photo resist board. No. Anyway.

**Chris Gammell:** Those were the days, huh, man? Yeah.

**Dave Jones:** Those were the days. Yeah. Yeah. Yeah. Yeah. Ah, boy. I find, I was pretty good at that. I used to enjoy it. Very, very therapeutic thing. Yeah.

**Chris Gammell:** You know, any kind of hands-on kind of thing can have that, that Zen, that Zen motion to it. I mean, soldering is like that, right? It's, you know, we can be very meticulous about it.

**Dave Jones:** Just sit there and do, you know, a thousand joints can be very therapeutic. Yeah. Absolutely. Don't have to worry about anything else. Not a care in the world. Just. Yep. Soldering your joints. Brilliant.

**Chris Gammell:** Yeah. One last, uh, one last video that I saw this week was actually a, uh, a cutter that someone made to, uh, to go from copper clad to, uh, create little islands basically on copper clad.

**Dave Jones:** I saw that. Yeah. Yeah. Yeah. Yeah. They've actually machined out little, uh, circles on bare board.

**Chris Gammell:** Right. And so then you can solder to that and that's used a lot in Manhattan construction technique where, you know, you can create these little islands basically and you solder all your components to that. And then, then you can also still use the, you know, the main, the non cutout part as your ground plane for, you know, like dead bug, if you want to try that or any other, you know, just actually having a ground plane for signal integrity. So awesome. I enjoyed that a lot. And we're out of time. I think we are. Yeah. Chip of the week this week is, uh, go check out chip.chipreport.tv. All right. But we will still do it on here and it'll be, yeah, it'll still be on here. So. Cool. All right. Well, uh, people, oh, if people want to give us reviews on iTunes, we always love that iTunes or whatever other podcasting things there are. We would very much appreciate that. Or tell your friends about the amp hour. That's cool too. Twitter.

**Dave Jones:** We don't have a guest for next week yet, do we?

**Chris Gammell:** No, we'll, we'll get on that.

**Dave Jones:** Yeah. Cause we are still trying to, if you haven't noticed, we're trying to do the alternating week, you know, where we have a guest on, then us. And, uh, yeah, I don't know. It was us this week.

**Chris Gammell:** If people didn't figure it out, we've, it's not like we're bringing on the guests now. It was just us. All right, man. Well, we'll see you next week. Hopefully we'll have a guest.

**Dave Jones:** All right. Catch you later. Bye.
