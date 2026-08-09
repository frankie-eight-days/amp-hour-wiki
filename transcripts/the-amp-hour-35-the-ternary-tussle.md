---
episode: 35
title: An Interview with Jeri Ellsworth - The Ternary Tussle
url: https://theamphour.com/the-amp-hour-35-the-ternary-tussle/
---

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life.

**Jerry Ellsworth:** And I'm Jerry Ellsworth taking over the stream today.

**Chris Gammell:** What? Jerry? A pirate.

**Dave Jones:** Jerry Ellsworth, who opened the door and let you in?

**Chris Gammell:** Yeah, really.

**Jerry Ellsworth:** Yeah, stray. You're everywhere.

**Chris Gammell:** Yeah, she is everywhere. And nowhere.

**Dave Jones:** Goodness gracious. Is nothing sacred? Nothing.

**Chris Gammell:** Welcome, Jerry. Welcome, Jerry. Good to talk to you finally. Extend some niceties, I suppose.

**Jerry Ellsworth:** Thanks.

**Dave Jones:** Got to be courteous with you being a girl and all.

**Jerry Ellsworth:** Yeah, you better watch out after what happened this week. Oh, yeah. Oh, yeah.

**Dave Jones:** We're going to get into that. Yeah, we will. I want to talk about that.

**Chris Gammell:** There's a couple things on that, yeah.

**Dave Jones:** So, yeah, we'll get into that.

**Chris Gammell:** We should mention first that we're recording on Skype today, so if it cuts out at all or we sound crazy, like with pauses between each other, we're trying something new to try and incorporate guests. We want to accommodate, so that's why we're on Skype.

**Dave Jones:** Because we tried Google Talk and it just failed, didn't it? We couldn't all join up together. So, yeah, oops. Yeah, we'll see how it works. Well, maybe we're just not smart enough to figure out how it works. I don't know. We're just Luddites when it comes to this sort of stuff.

**Chris Gammell:** Yeah. Well, Skype. Skype works for now.

**Dave Jones:** Well, we are electronics nerds, not computer penguin nerds, right? Right. Well, at least I'm not. Oh, no.

**Jerry Ellsworth:** No? I need my idiot's guide to see programming any time I try to do coding.

**Dave Jones:** Nice. Well, you heard it here first. That's right.

**Chris Gammell:** I didn't know that either.

**Jerry Ellsworth:** Assembly language, that's about it for me.

**Chris Gammell:** Really?

**Jerry Ellsworth:** Oh, really? Well, there you go.

**Chris Gammell:** My stuff is weak to non-existent. Yeah, that's about right. I came in afterwards, I do see, and that's it.

**Dave Jones:** I started with assembly on micros and PCs, and then I saw the light, and really high-level languages were the...

**Chris Gammell:** Really highly.

**Dave Jones:** As I've done a rant on. And then I got abused by all the assembly language diehards who just, you know, oh, God, they really didn't like me slagging off against assembly language.

**Chris Gammell:** You slacker. They talk about just, like, space constraints, power constraints, all that other stuff, and especially for embedded. Yeah, all that stuff.

**Jerry Ellsworth:** All your programming needs to be done in the interrupter service routine. That's where it all belongs.

**Chris Gammell:** Right.

**Dave Jones:** When the difference between a micro with 1K of memory and a micro with 8K of memory is like 20 cents these days, it's like, oh, God, you know, why do you bother, really? Well, if you only know assembly, that might be why. If you're really desperate, yeah, but, oh, I don't know.

**Chris Gammell:** Well, and Jerry, you do toy stuff, too, so that 20 cents does matter, right? Oh, of course.

**Jerry Ellsworth:** Big time. Big time. Yeah. You're lucky to get anything. I've had machines that I had to program on that didn't even have RAM. You only had a stack that was 8 deep.

**Chris Gammell:** Wow.

**Dave Jones:** Oh, wow. Yeah, that's tight.

**Chris Gammell:** Yeah. I've never done anything. I've never done any kind of projects that was that cost-constrained, so that would be a definitely new challenge for me.

**Dave Jones:** Yeah. Well, it opens a whole different world, really. I mean, if you're used to designing products, and then you come along, and they say, well, you know, you're limited to this, and you can't put in an extra resistor because it's going to cost 0.01 cents, and, you know, it really adds a lot of complexity to the design process, so that's something a lot of people... But it's a lot of fun, too. Well, it can be. Yeah, I've done that, and it's... Yeah, it's good.

**Jerry Ellsworth:** The toy industry is like that, and it's the only place that I've ever been, like, patted on the back and, like, good job, Jerry, for cost-reducing something. You know, everywhere else, it's kind of time to market, but there, they actually care about saving a few pennies here and there, and if you can do something elegant and kind of hacky, you know, they love you for it.

**Chris Gammell:** Now, tell me, when you try and get out of that mode, so say you're doing a toy design, and then you go off and you do something, like, real fancy and high-level then, is it hard to get out of that mindset? Do people, like, come up to you and say, come on, get moving, we need to get this stuff out the door? Like, is it like that?

**Jerry Ellsworth:** It's a big problem, yeah. Yeah, I moved on to doing some big chip designs, and, you know, I'm still in that mindset trying to optimize everything, and they're all about just grinding out as much RTL and code as possible. And, you know, in the end, in reality, it always comes back and bites you in the butt if you don't think about your design first and try to do it elegantly. You know, it's...

**Chris Gammell:** Oh, yeah.

**Jerry Ellsworth:** You know, up front, you can make it look like you're getting a lot of progress done, but when it comes down to verifying all this sloppy code that you throw out there, RTL, I should say, and it becomes, like, this steak, a bad steak. You chew on it, but you can just never... You can never get it down because there's just too much spaghetti code in it. Yeah.

**Dave Jones:** Well, it wouldn't be the first time that I've gone through and actually had to throw it all out and start again because, you know, enough thought wasn't put in up front because we were too busy trying to just get something up and running for a, you know, for a first demo or something like that. And then we figured, well, that's just totally the wrong direction. We can't, you know, if we try and run with that, we're just going to fail. We just have to start again.

**Jerry Ellsworth:** In the States, there's this consumer electronics show, and for whatever reason, all these chip companies always want to go out there and show off their chip at this show. So it's always, through your Christmas time, you're doing this dog and pony show just to get ready for CES, and it's all throwaway code. Yeah. But the managers always think that you can take this dog and pony show code and use it in the actual product. And I don't know how many times we've had to throw that stuff out. I mean, I just came off of a company a couple years ago where all of the engineers were being held up to the standard of this guy that just seemed to be producing, like, tremendous amounts of RTL. And it's just like, how can we keep up with this guy? He must be like some kind of god. And then six months into the project, they did a code review and found out that he wasn't, he was doing it as behavioral code, not as synthesizable code.

**Chris Gammell:** Oh, God.

**Jerry Ellsworth:** Oops. Oops. And so anyway, he got scared off and left the company. And then we ended up having to divide up his module and try to make it synthesizable as well as do our current modules that we were working on. It was terrible.

**Chris Gammell:** That's a long time to a code review. I mean, you just like let someone crank on their own for a while and you're just like, oh, well, I guess we'll just get the end. That's unusual. Yeah.

**Dave Jones:** Because companies aren't, you know, if there's not good management, this is one point where management can actually be, you know, a good thing is to enforce stuff like that and drive things like that. And if you don't have good management, if there's no adult supervision, you know, then this is what happens, you know, the inmates take over the asylum and, yep.

**Jerry Ellsworth:** Oh, don't give me a start on code reviews, though. I mean, it can be like a double-edged sword. Yeah.

**Chris Gammell:** Oh, boring as shit.

**Jerry Ellsworth:** Yeah. Or a pissing contest where... Oh, really? Yeah. One engineer is trying to show up the other and, you know, you take this big steaming pile of code in there and it's like, okay, it's not complete, but we're going to look at it anyway. And then all of a sudden they start tearing up all these parts of the code that, you know, you tried to tell them ahead of time that it's not complete. So you spend an hour just screwing around in areas of the code that it doesn't matter.

**Speaker ?:** Yeah.

**Chris Gammell:** Class, grumble, grumble, grumble. Yeah. Put an input in even if it's just to say something, right? Mm-hmm. Much like my comment right there.

**Dave Jones:** And then in the reviews, there's some people who just never say a thing in any meeting. You know, I'm... It might come as a shock, but I'm the one who always sort of says something in a meeting, even if I'm... I know. Dave Jones? Even if I know nothing about it, like I'm dragged into a meeting. And I haven't even worked on the project, so I'm going, well, why have they dragged me in? But, like, I'll be the one doing most of the talking, and I'm thinking to myself, this isn't even my project.

**Chris Gammell:** Yeah. It is now.

**Dave Jones:** It's like, well, yeah, that's what usually comes out of it.

**Chris Gammell:** Yeah.

**Dave Jones:** And, well, who's been doing the most talking? Dave? You seem interested in this. Well... Oh. I was just trying to tell you, you're doing it all wrong, or... Yeah. I'll be in my cube. You haven't considered this, or... Oops.

**Jerry Ellsworth:** I wish there was a good way you could document your gripes, so that six months down the road, when something comes back and, like, screws up the design, you can say, look, I told you so six months ago. Oh. You know, it's so frustrating for me. I've done it. I...

**Dave Jones:** Yeah. I always put in an email, if I think, oh, this is going to fail massively, you know, three or six months down the track, I put in an email, send everyone my concerns, and it's saved in the, you know, the outbox, and I drag it back out and say, look, you know, I told you so, and, eh. You know, people just shrug their shoulders and, yeah, whatever. Yeah, exactly. And they go and make the same mistakes again. Classic.

**Chris Gammell:** Oh, what can you do? Sounds like Dave needs to go into management. That's what I hear. Right.

**Jerry Ellsworth:** Ooh.

**Chris Gammell:** Bad. Bad times. Yeah. There's a mistake waiting to happen. There's a micromanager waiting to happen. Right.

**Jerry Ellsworth:** I would not want Dave to be looking over my shoulder in my cube.

**Chris Gammell:** I wouldn't want Dave in my cube.

**Jerry Ellsworth:** I wouldn't want me in my cube. Yeah, right? Exactly.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** The company that I worked at, we found these extra cubicle parts, and we closed off one of the guy's cubes. Awesome. Put the extra wall piece in. Yeah. That's what I would do to keep Dave out. I would just get a ladder and climb over.

**Chris Gammell:** Nice. Well, it sounds like that's what Dave's doing to his own cube there in the garage at his house.

**Dave Jones:** Yeah, I thought about putting up a wall around it so I have a two and a half square meter cubby. Yeah, padded cell. Basically, it would be padded because I want to acoustically dampen it too. So, I could go in there and bang against the walls. But I don't know. I thought about going for the full curtain now, so I might have wimped out on the entire wall idea. It's a bit of a commitment. It is.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And if I goof it up and go, well, that was a stupid idea, then, well, I've got this wall there. So...

**Chris Gammell:** What you should do is knock out a wall and extend your entire garage. That's what you should do.

**Dave Jones:** Well, that's called the side brick wall of the house, you know, so that could be a problem.

**Chris Gammell:** Brick comes down just as easy as anything else, Dave.

**Dave Jones:** Well, yeah. Well, it has been mentioned, but it was vetoed by she who must be obeyed. Oh, yeah. And I'm not talking about Jerry. Oh, goodness. All right, let's get into some real stuff here.

**Chris Gammell:** Whoa. That was a Skype up right there.

**Dave Jones:** A Skype fail. Because if we all talk at once, then Skype just cuts out. Which is a brilliant thing for, like, the world's most popular chat voiceover IP thing. You know, it's unbelievable.

**Chris Gammell:** So, what were you guys saying? Sorry.

**Dave Jones:** Yeah. Well, I was saying that, yes, we should actually get onto some real stuff on today's show that's actually on the list.

**Chris Gammell:** And what did Jerry say?

**Jerry Ellsworth:** I said, I don't object to any kind of lab expansion ever. Oh, that's right. Everyone should have bigger labs.

**Chris Gammell:** There we go. Yeah.

**Jerry Ellsworth:** Well, okay.

**Dave Jones:** You heard it your first. Can you please call my wife and tell her? Yeah, right.

**Jerry Ellsworth:** But I do second. We should cover some stuff.

**Chris Gammell:** All right. Let's get into some shout-outs. First up, we got Jeremy. And he finished his Arduino videos. Jeremy Blum. Yep. Yeah. Yeah. He was doing videos for Element 14. And he ran through a really good set of tutorials. I think he might pick it back up with other types of microcontrollers. But if people hadn't seen those, those are really pretty good videos. So, I like that.

**Dave Jones:** I only saw the first one or two, I think. Yeah. But anyway, great job, Jeremy.

**Chris Gammell:** Yeah. And second up is Electronic Stack Exchange. So, we've talked about that on here before. They got a facelift. They're actually... At first, they were Chip... What were they before? ChipHacker.com? And they got pulled into the Stack Exchange, the Joel Spolsky, that whole...

**Dave Jones:** That's the thing that you keep crapping on about. Yeah. The Stack Exchange concept. Yeah.

**Chris Gammell:** You'd love that, don't you? I love it. It's such... All right. So, I like forums. I think they're great. But I don't think anyone's gotten it right. I think that they got it right. That's why I like it. And because you can respond to a question and then you can have people add notes on to that question. I just... I think the format is spot on. That's why. And basically, today, they got a... They released a new just look to it, basically. So, same great flavor, new look or whatever. Whatever that saying is.

**Dave Jones:** Same shit, different smell? Is that the... That's the common saying here. Okay. I'm not sure if it's relevant, but sorry. I just threw that one in. I remember that one. Couldn't help myself. That's for sure. Right. Yeah.

**Dave Jones:** Yeah. That ties into the whole project thing, you know, when you're doing a project and you're making the same mistakes as before and, you know, it's the same shit, different smell. Yep. Sorry. Nice.

**Chris Gammell:** No, that's a good one. I like it. That's another good... All right. Aussie-ism.

**Dave Jones:** Aussie-ism. Well, Jerry used... And when we were chatting before the show... No worries. What was it you said, Jerry? No worries. No worries. Wait, she...

**Jerry Ellsworth:** Oh, that's not Aussie. Come on.

**Dave Jones:** She threw in a no worries.

**Jerry Ellsworth:** I think Dave's just claiming all these phrases.

**Dave Jones:** Yeah, right? Aussie-unique. Australians always claim everything, especially everything New Zealand.

**Chris Gammell:** Check out this new word. It's the.

**Dave Jones:** The. That's ours. Yeah. Dibs. Oh, come on. America... Yanks are just as bad. Oh, yeah. Well, everything else belongs to us. Yanks think the world revolves around America. Come on.

**Chris Gammell:** There we go. I'm a citizen of the world, Dave.

**Dave Jones:** Right.

**Chris Gammell:** Right.

**Dave Jones:** No worries. That's ours.

**Chris Gammell:** Okay.

**Dave Jones:** That is ours.

**Jerry Ellsworth:** It's got to be. At least we have fixing to. I'm fixing to. Oh, I've never heard of that one. It's a southern...

**Chris Gammell:** Right. Like, I'm fixing to go work on some electronics, that kind of thing.

**Jerry Ellsworth:** Exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Okay. That's a new one for me. Sorry. Yeah. All right. Learn something new every day here on the Amp Hour.

**Chris Gammell:** Yep. Cultural education.

**Dave Jones:** Right. All right. Although I am being... I am getting ganged up on here, you know, on this show. Two games.

**Chris Gammell:** Oh, we haven't even started yet. Wait until we get into printable electronics, Dave.

**Dave Jones:** Right. Yes. And I'm being attacked from both sides, east and west coast. That's... Well, that's all...

**Jerry Ellsworth:** Well, you're kind of. East to you. Sort of.

**Chris Gammell:** Yeah, I'm in the middle.

**Jerry Ellsworth:** And as soon as my Twitter trolls get in here and start going after you guys.

**Chris Gammell:** Yeah. Right. Well, let's talk about that. So... Let's talk about your Twitter trolls and the bus fiasco.

**Jerry Ellsworth:** Oh, boy. Oh, yes. The bus fiasco.

**Chris Gammell:** What's the status of that now? I mean, we've got a... We've seen a lot of coverage of the whole thing.

**Jerry Ellsworth:** Well, to give some background, right? Portland, Oregon, the buses have been running over pedestrians. So, a year later, they... It's bad. I mean, they're running over pedestrians that are in the crosswalk in the right of way. So, instead of... Well, okay, I shouldn't say instead of, but they decided, in addition to training their bus drivers not to do that, they're adding these devices to the buses that say, the bus is turning, the bus is turning, when it goes through the intersection at 100 decibels. It's pure noise pollution. And that really bugs me, because I used to live on a bus line. Oh, yeah. And it would start early in the morning and go way late into the night, and you would hear the announcement for the next bus stop, which is probably 100 decibels also.

**Chris Gammell:** Did you live on a corner? Is that why? Yes. Right at a bus stop. That'd be extra bad, right? Yeah.

**Dave Jones:** They would actually announce the next bus stop, would they? Yeah. Real? What? Outside the bus? There would be an announcement.

**Jerry Ellsworth:** Or when the doors would open, you would hear it, I think. Oh, right.

**Dave Jones:** Okay. You would hear that. Got it.

**Jerry Ellsworth:** That sucks. Yeah. It'd wake me up all the time. Well, anyway, so this device that they're installing costs $4,600, almost $5,000 to... All it is is this voice chip that says the bus is turning. So, I got a hair sideways and got all upset about this, so I made a video kind of mocking it, and I prototyped up a very simple circuit that does the exact same thing with some of my toy chips that I had left over here. Just a chip that plays back in audio playback. And I hooked it to this toy steering wheel, which I helped design, and I just showed how I could do it for $10. And I put this up onto the web, and it got a little bit of press, and people thought it was kind of funny, because I did my little paper animation stuff. And a local newspaper reporter picked up on it and did just a little blog about it. And then it gets crazy. All of a sudden, I saw this post on the comments, the sexist comment that said, you've just set women back 100 years. Years.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** 100 years for having an opinion and making this video. And so, I tweeted about it. I'm like, haha, I've set women's progress back 100 years. And someone on Twitter did a little bit of research and looked at this guy's YouTube channel, and it ends up it's the president or some bigwig in this company that makes this device.

**Dave Jones:** Oops.

**Jerry Ellsworth:** Oops. Unbelievable. So, then everyone's starting to get really riled up about this, and I'm tweeting about it more, and just stirring the pot.

**Chris Gammell:** You were stirring the pot, because I talked to you about that throughout, and it was funny to watch.

**Jerry Ellsworth:** So, people are getting, I mean, I get sexist comments all the time. People are really rude out there. Yeah. Like, some executive in this company coming and leaving that on my YouTube account was not right. So, of course, I sent my emails off to the company and said this wasn't right, and a lot of other people did. Well, this reporter that had blogged about this was kind of following the drama of this guy, this Peter guy.

**Dave Jones:** Peter Bartek. Let's name him. Come on.

**Chris Gammell:** Oh, yeah. Name and shame.

**Dave Jones:** Even if Jerry won't, I will. Peter Bartek, and the company is Protran One.

**Jerry Ellsworth:** There you go. So, this reporter called him directly and got him on the phone, and he's like, what? I don't know what you're talking about. My YouTube account must have been hacked. Totally.

**Dave Jones:** My ass.

**Jerry Ellsworth:** Totally bogus, because I was having this dialogue with him on the YouTube comments, because, and he was coming back saying that, well, this system was designed by a woman. Like, he knew an awful...

**Chris Gammell:** One of my best friends is a woman. It's like that, right? I mean, like, that's what he's saying.

**Jerry Ellsworth:** Like, I'm supposed to have some kind of vaginal loyalty or something, because it was designed by... That's a first on the Amp Hour, huh? Word of the week.

**Chris Gammell:** Word of the week. Yeah, there we go.

**Jerry Ellsworth:** Vaginal loyalty. You heard it here first on the Amp Hour. Vagina. Don't cut that out. Leave that in there. That's... Okay. We can start another scan.

**Chris Gammell:** I don't even know how to edit stuff, so don't worry. No, we don't. It's too much work. We're too late. I would have edited Dave entirely out of the show by now at this point.

**Speaker ?:** That's right.

**Jerry Ellsworth:** So, okay, this reporter gets him on the phone. He says it's hacked. And the reporter's like, that's odd. It doesn't seem like it's hacked. And then a couple minutes later, his YouTube account was removed. So, this reporter wrote another blog about it. And then, of course, I'm stirring the pot more. I'm like retweeting this blog. And then who picked it up? Make Magazine picked it up. And Ada for... All kinds of... Who was it? It was one of the bigger ones picked it up. And that really...

**Chris Gammell:** I think it was Boing Boing, wasn't it? Yeah, yeah. It was Boing Boing. I think Phil submitted it to Boing Boing or wrote about it or something. Yeah, apparently it was on the front. Or on Make, maybe. And then it went on to Boing Boing, whatever.

**Jerry Ellsworth:** Apparently it was on the front page of the Oregonian Sunday, too.

**Dave Jones:** Nice.

**Jerry Ellsworth:** It's still escalating. I just got contacted by the guys at Woot. So, it may be on Woot.

**Chris Gammell:** Woot? That's a sales site, isn't it? Yeah.

**Dave Jones:** I thought that was a conference.

**Chris Gammell:** I thought... No. Woot.com is a... It's like a one deal a day. You can buy whatever. They get large lots. Oh, okay.

**Jerry Ellsworth:** I might be mistaken.

**Chris Gammell:** Okay. I love Woot. I think it's awesome.

**Jerry Ellsworth:** I don't know if they have a blog or something that might be going up there. I don't know. They might.

**Chris Gammell:** Maybe they're selling, like, audio devices that day and they want to, like, tie it to a blog post or something.

**Jerry Ellsworth:** Oh, right.

**Chris Gammell:** Maybe they're selling buses. Who knows?

**Jerry Ellsworth:** Go check out my YouTube channel. It's on there. It's... Yeah. It's... The name of it is Oregon Trail 2011.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** Which is a very popular video game in the United States that depicts the traveling from East Coast to West Coast. And all kids had to play this in school. Oh, yeah.

**Chris Gammell:** I played that for sure.

**Jerry Ellsworth:** Oh, okay. Right. Now, I was wondering...

**Chris Gammell:** You have lost four wagon wheels and an oxen.

**Jerry Ellsworth:** Right. Right. The game was so bogus, too. I mean, we all had to play it and we got... At least I got graded on it. You got graded on it? Whoa. Yes, we got... We have a really bad school system here in Oregon. Right. The game is completely random.

**Dave Jones:** One thing's for sure, Jerry, you're going to get huge mileage out of this one because people love to... Especially the papers. They love when this sort of modern day sexism type stuff happens. They just eat it up.

**Chris Gammell:** It seems to be popping up a lot of places, too, to be honest. It is. Like, you posted this other one, Dave, about...

**Dave Jones:** I have. I have. Edmund Optics. Let's call them out. Yeah. They're an optical company. They're a huge... Like the DigiKey of Optics or something. You know, they're a huge catalog. And their front cover has... I will put up a photo of it. Has this... There's no way to say it. She's got big boobs, okay? This animated superhero girl. Right. Like, with these... I don't know how big these things are, but they'll take your eyes out. Let me tell you. It's just the comic style. It's like how comics are drawn. Yeah. Sort of... Yeah. Comic style. And she's, you know, going to save the day by delivering your optical products or something. You know? She's, I don't know, hero girl or something. Yeah. I don't know. Optical girl. And it turns out that it's not the first time they've done it. I'll post a link to one of their previous catalogs as well, where somebody on their blog actually took them to task about their previous catalog. So, they have a history of doing this. What is it? The 1970s all over again? Because if you were reading electronics magazines in the 70s, there were like, you know, girls in every second ad. Yeah. It was... It was even into probably the 80s, I think. Probably the mid-80s. They might have stopped doing that. I don't know about the US, but it was like that here in the Australian mags anyway, so...

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** Well, they certainly haven't stopped doing it at trade shows. I mean, there's booth babes at every electronic trade show that are there just to try to lure the guys in. You know, and I don't... I mean, I don't...

**Speaker ?:** I don't know.

**Dave Jones:** And it works.

**Chris Gammell:** I was going to say, Dave and I have talked about this before, though, and Dave is on the side of booth babes. He likes the booth babes, so I don't know if he's the best one to be calling out. I mean, it's interesting that they're doing this, but Dave did say he liked the booth babes, so I just want to be full disclosure here. I don't mind that as much.

**Dave Jones:** Well, I'm against having them, but if they're there, you know, I'm going to have a look. I'm going to go visit the stand, okay? I think it's a waste of time and money. It is a waste of money, for sure. Anyway, I... Yeah, it is. I agree, but...

**Jerry Ellsworth:** But on a more serious note, though, I mean, I should state that I get a lot of sexist comments and it offends me, and especially when it's diminishing my engineering ability just because I'm female. Yeah. Yeah. I experienced that a lot in my life. Yeah, that sucks. And around the racetrack, it was really bad. Granted, a lot of those guys weren't the brightest out of the bunch. The most evolved, as it were. Yeah. Maybe that's sexist in itself right there, but... Exactly. It's less than electronics, but still, every time I go to a trade show, I actually make it a game now. I'll go up to a booth and I'll let the salesperson start talking down to me and they'll be like, so this is an oscilloscope? Oh. And you use it to measure waveform... You know, and I'll be like, oh, really? Oh, that's interesting. Oh. So what DSP functions does it have? Bitch. And then just watch their face drop when...

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, brilliant.

**Chris Gammell:** Wow.

**Dave Jones:** I would have so much fun with that. Oh, that'd be awesome.

**Chris Gammell:** I don't think you would, Dave.

**Dave Jones:** Well, no. I mean, but the flip side of that, being a girl in this industry can actually be a massive advantage too.

**Jerry Ellsworth:** True. True.

**Dave Jones:** I mean, I would be surprised if you're not aware that a lot of your success, you do a lot of cool stuff, but it's also, a lot of it is because you are a girl, I guess, and people find that really cool and different.

**Jerry Ellsworth:** Yeah, I go to a lot of events and I speak to a lot of schools and stuff, and I think there's one thing engineers should pay attention to is standing out in a positive way. And for me, it's a little bit easier. I can put on roller skates and it's like, all right, I'm in a group of 400 guys, so I'll be usually the only girl there on skates. So that's memorable. And people will remember me when it comes time to do a job interview or... Yep. Yep. Absolutely. If you're just another suit in the crowd, you're not going to be remembered. So I think engineers should stand out in some way.

**Chris Gammell:** Yeah. I totally agree. Yeah, Dave, you've talked about that before too, like even when you're in a job interview, when you bring in your boards and stuff, that's a great way to stand out, you know. Hey, I made this. I think that's brilliant, you know.

**Dave Jones:** And doing your own stuff on the outside or having your own blog or having your own radio show, having your own whatever, YouTube videos, anything that helps you stand out when you're going for that job interview. Because yeah, everyone else has got the qualifications, everyone else has got the experience. You know, what makes you stand out? And I know if I'm hiring people, the people I will get in for the interviews are the ones who have, you know, done stuff outside of work, who are interesting, you know. And dare I say it, if a girl applies, I'll get her in because I think that's cool. More women in engineering, you know. So, I would, you know, I'd love to meet her and find out, you know, how, well, not only is she suitable for the job, but, you know, is, you know, where am I going here? I don't know. I'm painting myself in a corner. And Jerry's going to give me a slap down. Yeah. You know, we actually talked about that. Just keep digging.

**Chris Gammell:** We talked about that on engineer blogs because there, and there was like a big controversy about that because, you know, a lot of, a lot of guys feel, feel that, that, you know, they, they feel like they get passed over because women have, you know, stand out naturally just because, you know, they're, they're in the, they're in the pack. Right. And just the, just that, that one differentiation is there and they felt like, uh, discriminated against. And it's like, well, maybe, but I mean, there's so many other things that guys don't realize that women have to put up with in trying to be in a, for now, male dominated feel and field. And like that, that's just kind of the way it is. So.

**Jerry Ellsworth:** Well, that's the way. Guys can work around this though. I mean, it's, whether it's just wearing a funny colored shirt or, uh, bringing your boards in. Yeah. Yeah. I mean, that's partly how I busted into the electronics field. Having green hair or something.

**Chris Gammell:** Great hair.

**Dave Jones:** Dave just said great hair. Green hair. Green hair. Green. Wow. Exactly. Yeah. Yeah. There's many ways to stand out, but I remember on Twitter, there was this, I don't remember her name, but she was a young female engineer or graduate maybe. And she, uh, I don't know how we got talking about it, but I said, um, that, uh, being a, oh, she commented that to me that, oh, it's so hard being a woman in engineering, you know, it's, and I, and I went rubbish. It's easy. You've got a massive advantage. Use it. You're female. It's, it's novel. You know, um, use it to your advantage.

**Jerry Ellsworth:** I don't know about that.

**Dave Jones:** I will.

**Chris Gammell:** I don't know. I think. Ah. I'm with Jerry on this one, Dave. Sorry.

**Jerry Ellsworth:** I, uh, I mean, I think there's a natural sort of, I mean. It gets you in the door, but it doesn't, it doesn't help you when you're in. No, no, no. Yeah. It's hard to deal with the pissing contests that happen in engineering. Yeah. Um, if, if I come in and I start to take a hard stance on something, I feel that the guys really take offense to that where I can watch two guys do the exact same thing to each other. And it's just like, ha ha ha. We're just having our little fight. Right. So there's, there's a different interaction between. Yeah. Um, male, female and, and male, male.

**Dave Jones:** And, um, that's just how our species are. I mean, it's just, you know, it's nothing to do with, oh, I guess engineering is a little bit different. So I feel I always have to be like backing down a lot. It's quite natural. I don't know. So I just think, yeah, there are some inherent advantages there. And, and, well, the last thing, well, the last thing I really wanted to see is for some, you know, is for a young female graduate engineer to be so down that, oh, I've got to compete against all these men and I've got no hope. And, oh, I've got to be like a man. And, you know, all that sort of rubbish. I just, no, I mean, just being female is, I'm sorry to say it, but it will likely get you interviews. Um, you know, and then you've got to stand out. Of course, it won't get you the job just because you're female.

**Chris Gammell:** Right. But Jerry's saying it's past that point. I think that's the part that would be really tough. I think.

**Jerry Ellsworth:** It is. It is tough. I mean, I, I come in as a contractor a lot. So that also adds a little bit more complexity to, um, the interactions. So as a contractor, a lot of times you're hired to be the, um, superhero to come in and fix some kind of project that's behind schedule. So everyone's got a chip on their shoulder anyway. Yeah. So I, I find that the first three or four weeks that I'm on a project that I have to do a lot of like. Clean up. Well, no, no, just a lot of, uh, taking a lot of shit from people.

**Chris Gammell:** Oh. And so. Oh. Integration into the group. Is that what it was more? Like kind of like fitting in and.

**Jerry Ellsworth:** Yeah. Yeah.

**Chris Gammell:** Getting into the groove of like code compiling or whatever it is.

**Jerry Ellsworth:** And I feel, and I mean, I don't have any other kind of point of reference to, to justify this, but I feel that, you know, maybe if I was a guy and came in there, I could just come in and just be like super aggressive and say, this is what we're going to do. And you're going to listen to me. And, and, you know, trust me, I've tried to do that and it really backfires badly. And I don't know if it's a gender thing or not.

**Dave Jones:** That's interesting because I've never experienced that with the female engineers I've worked at. As soon as you open your mouth and say, you know, good things, right. People will listen. That's you instantly gain respect. I'm surprised it takes, you know, months or something to gain people's respect. At least weeks. At least weeks. Wow. That's, that's surprising. I haven't really encountered that. You know, it's, I, I find, yeah, if you come in and you say the right things and do the right things straight away, then people go, well, okay, she knows what she's doing. And you don't care if they're male or female.

**Chris Gammell:** No, it's the, it's the defensive mechanism though. Right. Is that what I'm hearing Jerry? Is that like, right. Okay. So like you come in and you slam the table and they're like, well, why is she slamming the table? Whereas if it was a dude, it'd be like, oh, I should listen.

**Jerry Ellsworth:** Yeah.

**Dave Jones:** I mean, on the flip side, I've found that. That's the same thing with guys. If a guy comes in like me and is like really kind of aggressive and will say what they think, um, then, you know, it doesn't matter whether you're male or female, that's going to get a lot of people offside. Um, so maybe it's just your outspoken nature. Maybe it's not because you're female to, uh, you know, or not entirely because you're female. Maybe. Perhaps. I don't know.

**Jerry Ellsworth:** Perhaps.

**Dave Jones:** Because I've, I've, I've had exactly the same thing. Um, you know, I've come in and slammed my fist on the table and said, you know, you're doing it wrong. This is how you got to do it. And, or et cetera, et cetera. And, um, that gets a lot of people offside and instantly I'm, I'm shunned. Uh, so yeah, because I, I said too much.

**Chris Gammell:** Chris still isn't sold, Dave.

**Jerry Ellsworth:** Well, I, I don't think, you know, we're both looking at this front through our own prism and I don't think we can actually judge this accurately.

**Chris Gammell:** You know what we need? We, we need like a freaky Friday moment. What's a freaky Friday moment?

**Jerry Ellsworth:** Yeah. What?

**Chris Gammell:** What? You guys, the, like the old, like Disney movie where like they switch bodies for like a day, you know, like the mind switch out.

**Jerry Ellsworth:** Oh man, I would wreck Dave's body. I would just go out there. I'd be like caving. I'd be jumping off of like big cliffs. All right.

**Chris Gammell:** Woo! I can just imagine you with a hammer in your hand, hitting yourself in the head. Not going to use this anymore. Pop, pop. Wow. Oh goodness.

**Jerry Ellsworth:** Well, this is probably going to be the, chalk this one up as the most interesting amp hour ever.

**Chris Gammell:** Oh, we'll try and tap it. Don't worry.

**Jerry Ellsworth:** Okay.

**Dave Jones:** Absolutely. Wait until we get the name for it. Because every, every episode has to have a title.

**Chris Gammell:** Oh yeah. We'll work on that.

**Dave Jones:** Freaky Friday.

**Chris Gammell:** Freaky Friday. Oh God. Oh dear.

**Jerry Ellsworth:** So anyway, this guy with the bus. Boy, if you're listening, Peter, you know, you should have just apologized in the beginning and said, man, I was drunk or I was upset. It would have been over at that point. Yep. Instead of. Absolutely.

**Dave Jones:** Instead of you're a douche and you didn't admit it. Exactly. And you just, yeah. And you tried to weasel out of it.

**Chris Gammell:** Yeah.

**Dave Jones:** Man. Makes you even look like even a bigger douche. So. So done. Nobody, by the way, nobody buys the my YouTube thing was hacked and your account shut down. That's just bullshit. Come on. I mean, please. What do you, what do you take us for?

**Chris Gammell:** Yeah.

**Dave Jones:** Seriously.

**Chris Gammell:** Oh no, my wallet was stolen, dear. And someone went to the strip club on my tab.

**Dave Jones:** Yeah. I have no idea what that.

**Chris Gammell:** Those purchases? No, those were not mine. Someone hacked my YouTube account.

**Dave Jones:** That's a bit sexist, isn't it, Chris? Sorry, I don't go to strip clubs, Dave. Men just go to strip clubs?

**Chris Gammell:** I don't go to strip clubs. Anyways.

**Dave Jones:** Anyways. Yeah. More douches. The Edmund Optics people. Buy a clue. Okay?

**Chris Gammell:** I agree.

**Dave Jones:** Do your idea. Yes.

**Chris Gammell:** All right. I want to switch gears. I want to talk about Jerry's van.

**Dave Jones:** Go for it. Van? Jerry has a van?

**Jerry Ellsworth:** Yeah. It's gray and it says solar heating on the side.

**Chris Gammell:** So I was talking to Jerry yesterday and I say, Jerry, I want to talk about Japan. And she heard your van and I was actually saying Japan.

**Jerry Ellsworth:** You can talk about my van if you want. It's fine.

**Chris Gammell:** I have no interest in your van, Jerry. I'm sure it's windowless and creepy.

**Dave Jones:** It is. Is it like an A-Team van? Because the A-Team van's cool.

**Jerry Ellsworth:** It's a Ford, but it's close. It's close. And it has this expanded metal grill between the back area and the front area so I can abduct people and put them in the back. Nice. And I can yell through the back like, shut up in there. Shut up.

**Dave Jones:** Wow. Oh, brilliant. We learn something new about Jerry every day.

**Chris Gammell:** Oh, I don't know if we want to anymore.

**Dave Jones:** Right. Anyway, what about Japan? What about Japan? Yeah. Yeah. So there's tons of stuff going on over there. I figure it hasn't been in the news much.

**Chris Gammell:** I know, right? I wanted to rant a little bit about the fact that the first article, honestly, the first article I saw was in a tech magazine talking about, oh, well, what about our chip supplies? And it's like, yeah, okay, we understand. You're actually going to have some chip supply. Everyone's going to have some chip supply problems. But there was just a 9.0 magnitude earthquake. You think you could hold off on maybe like a day, two days? Like, I don't get why that's the first thing out of their frigging mouths.

**Dave Jones:** Oh, because they're a niche content.

**Chris Gammell:** Nope.

**Dave Jones:** They're niche content magazines.

**Chris Gammell:** Not excusable.

**Dave Jones:** You know, I don't really care about that sort of thing. People want to know.

**Jerry Ellsworth:** I mean, business goes on.

**Dave Jones:** People want to know straight away. In the meantime, yes, but not the first thing. If you're in the industry and you're reliant upon, gee, you want to hear. From the industry experts, the magazines and the sites you're reading.

**Chris Gammell:** I don't think they're doing that for the electronics people. They're doing that for the investors. And then the first thing they do is, you know, dump all the stocks. I frigging hate that stuff. I can't stand it. I don't know. The first thing out and the first thing that happened was all the stock prices dropped. And it's like, all right, if there weren't enough problems, let's make sure Japan's economy goes in the toilet too.

**Dave Jones:** I don't know. I think you're being a bit harsh. I think they should talk about it. You know, everyone knows, yes, it's a tragedy and everything, but. In the meantime, yeah. I mean, you don't have to give it a couple of days, Grace. I'd want to know up front. You know, news is news. I mean.

**Chris Gammell:** Yeah.

**Dave Jones:** That's not news.

**Chris Gammell:** That was speculation. It was the first thing out of their mouths. Oh, well, the chip fab.

**Dave Jones:** Yeah, but we're talking about billions of dollars. You know, like hundreds of billion dollars worth of industry stuff here. It's important. You know, people have to get the facts. They have to talk about it. They have to discuss it. And yeah, I think it's important whether or not it happens a week. You know, if it happens a week after, I think that's too late. So why not have it straight away? I disagree.

**Chris Gammell:** I think that's insensitive. I agree to disagree. All right. Jerry?

**Jerry Ellsworth:** What do you think? I don't find a problem with it, really.

**Dave Jones:** Two to one, Chris. Oh.

**Jerry Ellsworth:** That's it. We're getting six guests on here from now on. It isn't sensitive, but these trade magazines and trade sites aren't there to be sensitive.

**Chris Gammell:** I will agree with that. But I just hate it was the first thing I – maybe I shouldn't read this stuff when that kind of news pops up. But it was the first thing I saw, so I hated it. In the meantime, it's like, yeah, of course this is an issue. I mean, like, you know, Japan is a huge part of the world economy.

**Dave Jones:** Then why shouldn't they talk about it straight away? If that was the first thing you saw about the Japanese earthquake and tsunami, well, you're reading the wrong newspapers. You're reading the wrong things for your news. Well, maybe just a general, too. Right.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** If it showed up on CNN or something, that would be very insensitive because that's not their demographic they're targeting.

**Dave Jones:** Exactly.

**Jerry Ellsworth:** Now, and something else, I think this was in the notes about manipulating prices. We saw that in the 80s with memory prices and in the 90s with the epoxy shortage and a lot of speculation going on as far as, like, immediately jacking the price up on parts.

**Chris Gammell:** Yeah, but that was supplier side and that was talking to one another, wasn't it? Where they said, okay, well, today, this week, it's going to be $4 for a DRAM chip, right? And then the next week they said, okay, $4.25. And everybody ticked up incrementally so there was no economic pressure. That was a different thing, I thought. No? Anyone? Bueller? Bueller? Bueller. Bueller?

**Dave Jones:** Oh, he's sick. My best friend's girlfriend, cousin. Sorry. Anyway. I love Ferris Bueller. You're right. Bueller movie.

**Chris Gammell:** Oh, yeah. I think you're right about the prices, Jerry, but I thought that was a little different because they were actually doing that on purpose. Whereas this, it's just people are stockpiling and jacking up the price just because they can now as opposed to it's, like, opportunistic versus pre-thought-out.

**Dave Jones:** Welcome to the real world, you know? Yes. Yeah. That's what companies do. Yeah. Speaking of the real world, there's a follow-up to Tyco last week.

**Chris Gammell:** And speaking of, you know, a-hole executives. Oh, yeah. Yeah. This is brilliant. Tell us about it. So Ryan Barnes wrote in. And he actually was listening to last week's episode, and we talked about how Tyco, who is a huge supplier of electronics components, a lot of other stuff, they are now TE Connectivity. And they changed their name. We were complaining about it. Why? You got to change your name. Well, Ryan wrote in. Maybe it's because of this. Tyco, their top brass, basically all just got indicted from anywhere from 15 to 20 years in prison and, like, millions of dollars in fines. And they – because they stole $600 million. Just embezzled it or – Yeah. Or they, like, gave themselves loans and they forgave them. You know, all the kind of usual dirty tricks. I loved it.

**Dave Jones:** And they got busted for it. Can we have a round of applause, please?

**Chris Gammell:** Oh, yeah.

**Jerry Ellsworth:** Yay. Thank you. I love seeing – Tyco is such an odd company. They just go out and acquire and sell companies so quickly.

**Chris Gammell:** Yeah.

**Dave Jones:** I love this. In the article, they spent $2 million on a Toga birthday party. Toga. For the executive's wife. Toga. Toga. Toga. Toga. Toga.

**Speaker ?:** Toga.

**Dave Jones:** Brilliant. Toga. On a Mediterranean island. On a Mediterranean island. And then I'm hanging out with the wrong people.

**Chris Gammell:** I know, right?

**Dave Jones:** I know. We should get them as a sponsor. Geez. Imagine the cash we could embezzle.

**Chris Gammell:** And this week we're doing a giveaway of gold-plated 555 timers.

**Dave Jones:** And we can record from their $18 million Manhattan apartment with the $6,000 shower curtain, it says here in the article. I could use that as an audio dampener. Screw that.

**Chris Gammell:** We should rent like a blimp or like a Zeppelin and record from above the earth. That's what we should do. Why stop at $18 million? Awesome.

**Dave Jones:** $600 million. How many guys? Is it two? Is it two guys?

**Chris Gammell:** Two main ones and then there's a third one that's not as severe. And I don't know about you guys, but I love white-collar criminals getting locked up. I think it's the best thing in the world. I think they have a quote in there. They said, through the lawyer, he said, we didn't take anything we didn't deserve. It's like, I can't believe it's, oh man. It's stuff like that that I think, and I'm like, you know, if that's like success, I will be in my basement working on electronics till the day I die. Because screw that. You know, like, that is just so jaded and ridiculous.

**Dave Jones:** That's how most of them get away with it. That's the sheer arrogance of them. And it takes arrogance to get away with stuff like this. And most of them do. Most of them get away with it. This is pretty rare that somebody's actually being jailed for this. It's incredible. So, yeah. There's got to be, you know, there's got to be 100 to 1 at least to the number of people that get away with it. Probably 1,000 to 1. Oh, yeah. Definitely. It's just, yeah. Anyway, sucked in. Yeah. That's just awesome. I love it. Yes. That's a win. Win in with a hash.

**Chris Gammell:** Sorry, Charlie Sheen. No, I'm not getting into that stuff. I hate that. It's just as bad. All right. How about into some other awesome stuff? How about the one right above it? The USB open source USB analyzer. Have you guys heard about this?

**Jerry Ellsworth:** Oh, I have. That's awesome. The way they jump-started that project. Did you see their video?

**Chris Gammell:** I didn't see the video. No, I just... Oh, I haven't seen the video yet. I just found out about this. Yeah, we'll link it.

**Jerry Ellsworth:** This is a way to promote a startup project. It was funny and straight to the point. And they raised like eight times the amount of money they were asking for.

**Chris Gammell:** Yeah. And it's called Open Vizsla? Is that how you say it? Open Vizsla.

**Dave Jones:** Well, no. V-I-Z-S-L-A. There's no U in there.

**Chris Gammell:** Huh? Okay. Open, yeah. Vizsla, yeah.

**Dave Jones:** Z-I-Z-S-L-A. Z.

**Chris Gammell:** What, Z? Yeah, Z. Z. Sorry, wow. But it's great because they also sold spots on here for corporate sponsors too, which, you know, some people might be against that. In terms of like, it's just a name on a board. So Altium bought a spot, Boing Boing, Farsight, a couple other that I don't recognize the logos. But it's brilliant. I mean, and they had great levels. We've talked about Kickstarter on here before. They had great levels where you're just getting dev boards. You know, like, as they come out, you get the alpha, you're the beta tester. And if you donate enough, you get all of them. You know, like, you get to actually have feedback in the process. So this is how it's done, folks. Check out the project. Check out the page. I can't wait to see it too because this stuff is really expensive. I mean, like, to get a USB analyzer.

**Jerry Ellsworth:** How much did they raise for this project? They were only asking for like $81,000.

**Dave Jones:** Yeah. And they were asking for $17,500 was their goal. Yeah. And they got 584 people to back it. Yeah. At $81,000. That's just awesome.

**Chris Gammell:** I love Kickstarter in the first place. I think it's great that you can just, you know, kind of put your money where you really like something. Like, I'd love, instead of just buying something, you're supporting the actual people directly. You know, it's like the difference between going out and handing an artist $10 and for, you know, a MP3 track versus buying it through iTunes and, you know, paying some portion of that to the artist. This is like directly sponsoring that person to do this project. Yep. So...

**Dave Jones:** Ah, and the person is Bushin. He's the one who originally did the Rigol hack. Oh, really? Yeah. And also, he was one of the ones sued by Sony, insert evil sound, for hacking the PlayStation or something. So, I believe, anyway. So, yeah. Good on him.

**Chris Gammell:** Yes, at least. At the very least. That's awesome.

**Dave Jones:** That's why he goes under the pseudonym Bushin. I don't think he ever uses his real name, but... Right. Yep.

**Chris Gammell:** That's awesome. Yeah, so we'll link to the Kickstarter page, too. There's a whole category for technology. There's one for open hardware, one for open software, and then there's just kind of floaters in there, too. And there's a couple other good projects that need some funding. So, be sure to click on over and, you know, fund your favorite ones.

**Jerry Ellsworth:** Have they fixed that so it can take PayPal now? Last time I tried, I think it was on there. They had some other service.

**Dave Jones:** No, it still uses Amazon. It still uses Amazon, I believe. And, curiously, a friend of mine here in Australia tried to do a Kickstarter project, and apparently, if you're Australian, you can't do it. Ah. For some reason, there's some payment issue or something. I couldn't find anything in the terms and conditions that said, you know, you have to be from the U.S. or something. But, yeah, apparently, that's what she told me, is that she went through and it wouldn't let them do it if you're from Australia. Something to do with the Amazon payment system or something.

**Chris Gammell:** Yeah.

**Dave Jones:** I don't know.

**Chris Gammell:** Yeah.

**Dave Jones:** Crazy. Well, it's kind of...

**Chris Gammell:** So... I mean, Kickstarter just in general, I mean, it's kind of like to Jerry's point before, too. It's like it pays to stand out, like with that video and just the... I mean, the concept itself is great, but that's what's going to get you funding, and that's what's going to allow you to do some cool work. So, if people are considering it, definitely spend the time on the upfront. That's what's really going to pay off, I think.

**Dave Jones:** Yeah. There is actually an Australian version of this site, but it's not called Kickstarter. It's... There is another name for it. It'll come to me. Okay. But there are ones in other countries. There are other versions of, you know... So, it's not the be-all, end-all.

**Chris Gammell:** Okay. Well, we'll hopefully put that in the show notes if you think about it, if you think of what it is. Hmm. So, speaking of open hardware, there's actually... I saw on the Bug Lab's Twitter account, they are talking about setting up another one. So, I went to that one last year, and I don't know if I'm going to be able to go this year, but it seems like there's another one in the works. What is it? The Open Hardware Summit.

**Jerry Ellsworth:** Oh, okay. Yep.

**Chris Gammell:** I'm sure...

**Dave Jones:** Even though the license is still called Open Source Hardware, which everyone took me to task on. Right. Jerry, what's your take on that? Is it called Open Source Hardware or Open Hardware? How do you pronounce it?

**Jerry Ellsworth:** I have no take on it at all. I don't care. Make cool shit.

**Dave Jones:** Oh, there you go. Okay. Make cool shit. There's the Jerry license. All right. Yeah. Make a YouTube video. That's your license.

**Chris Gammell:** Yeah.

**Dave Jones:** Fantastic. What else have we got on here? We've got about 10 minutes left. 10 minutes. We've been just yapping on with Jerry all day.

**Chris Gammell:** Works out pretty well. Sorry.

**Dave Jones:** Maybe we should do a two-hour show.

**Chris Gammell:** No. I don't have a comfortable enough chair. I'm sitting on like a piece of wood, basically. Right. All right. So, I have a new segment I wanted to kind of sort of debut. I don't know if it's going to go anywhere, but I called it Go Gear Go. So, for new gear. Because there was two people that kind of showcased some fun electronic stuff. I know that Adafruit does their part finder Friday, and it's kind of like that, but not really, because these aren't necessarily parts. The first one being Alan. So, his, what's his ham handle? I don't know what it is. V2, VK2, S-V-A-Y, whatever. Throw you hams out there. Oh, yeah. He actually was, he's been talking about these, like, storage boxes for SMD components. And they all link together. And so, hope he doesn't mind me swiping the link, but they're really cool. I mean, they're just like, they're probably the size of, like, an American quarter. And you can, like, snap them all together. And they're really good for storing small parts, basically. So, it's another storage system for the lab.

**Jerry Ellsworth:** Cool. Yeah, it looks like the lid on those will stay closed and seal in little parts, too. It's for medical use, right?

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** Yeah. Yeah.

**Chris Gammell:** And there's a great picture of him on his TwitPic page of he made a periodic table out of it. He, like, snapped them all together in that form. Oh, right. It was awesome.

**Dave Jones:** That's pretty cool. And then we've got these Proto Flexboards.

**Chris Gammell:** Yes. They are flexible, sticker, conductive, they're conductive stickers, basically, that break out SMD components to larger pads. But they're stickers. And that was written in about, from Dino. And they're really cool looking. I mean, like, they're standard.

**Jerry Ellsworth:** Are they polyamide, uh, Kapton type? The orangey ones? Yeah, I think they're a Kapton. Yep. Yeah. Yeah.

**Chris Gammell:** That's what it looks like. And they have them for, you know, sticking just onto Proto Boards or actually even putting them as connector interfaces.

**Dave Jones:** Yeah.

**Chris Gammell:** They're brilliant. I love them.

**Dave Jones:** Yeah, they're neat. How much do they cost?

**Chris Gammell:** Uh, you have to get them.

**Dave Jones:** Anyone know?

**Chris Gammell:** Uh, I see. Oh, crap. Where is it? Where to buy? There's a link through Jameco. But I didn't see the price. I'm guessing not cheap. Oh, am I?

**Dave Jones:** No, yeah, probably not. But they're very cool to have around. Oh, yeah. You know, you buy a bunch of them and you just have them on hand when you need them, so. Yeah.

**Chris Gammell:** 60 bucks for a sheet of the, of the, uh, SOT 23 breakout, or SC70 breakouts. Ouch.

**Jerry Ellsworth:** All those breakout boards are just so expensive, always. It's frustrating. Yeah, they are.

**Dave Jones:** Yeah.

**Chris Gammell:** Goes down to 50.

**Dave Jones:** And, of course, it's patented. Patented. I'm using the quote marks. It's patented. Yeah. Patented. Patented.

**Chris Gammell:** It's okay, Dave. It's all right.

**Dave Jones:** And there's this ridiculous terms and conditions of sale on the website. If you, like, there's a menu down the side, and if you go click on terms, there's all these. Number one, there's six terms and conditions. Warning, these products are not designed for testing with a level of reliability suitable for use in or connection with surgical implants. Well, Jesus.

**Chris Gammell:** It sticks to a person. Why not? Right?

**Dave Jones:** Just critical components in life support systems. Aircraft or vessels.

**Chris Gammell:** Oh, yeah. That's all the law stuff.

**Dave Jones:** Oh, dear. I hate that crap.

**Chris Gammell:** I do, too. I don't know. I think it's a cool idea, though. I wish they were so expensive, but I'm sure they'll come down eventually. And they're kind of printed looking. What do you think?

**Jerry Ellsworth:** Do them at home?

**Chris Gammell:** Maybe.

**Dave Jones:** Dreaming, people. Dreaming.

**Jerry Ellsworth:** Dave, Dave, Dave.

**Chris Gammell:** Did we... When will you learn? I don't know. There's actually... I don't know if I mentioned it, but, yeah. There's a whole conference of printable electronics.

**Dave Jones:** Of course there is. Printable electronics is a big industry. It's not going to happen in the damn home.

**Chris Gammell:** People. Jerry, come on. We've got to gang up on them. This is why you're on the show.

**Dave Jones:** Oh, oh, oh. Yes, it will.

**Chris Gammell:** Yeah.

**Dave Jones:** Take that, Dave.

**Jerry Ellsworth:** That's the best I can do.

**Dave Jones:** Then you'll have to come back to, I think, my five points I've put in the previous blog rant on this, which nobody has ever come back and questioned, because they can't, because I am right. What? Where's this five points? Who even reads this? I don't even know about this. It was in the comments section. Where? Of the previous blog. Really? Yeah, where? It's been conveniently... Squelched. It's been conveniently lost in the ether, has it?

**Chris Gammell:** I don't see it, but which one did you mean the last time we talked about it? Is that what you mean?

**Dave Jones:** I think it was the first time that really, you know, the big half-hour discussion happened on it, and then, yeah, I put all the points up there.

**Jerry Ellsworth:** I'm just going to have to do it to prove you wrong, aren't I? Awesome.

**Dave Jones:** Please.

**Jerry Ellsworth:** I encourage people to prove me wrong. Sounds like a Kickstarter project, Jerry. Yeah, there you go. I can make you an inverter today if you want. Awesome. And it works. It probably costs like $100 in electricity. Right. But if you need an inverter, it's worth it.

**Dave Jones:** Yeah. Right. Okay. Right. If J-Cars closed and you just can't get one of those.

**Jerry Ellsworth:** I just did a homebrew circuit board this weekend. It worked out perfectly. And, you know, I couldn't have got a quick turn board over the weekend. So...

**Chris Gammell:** Yeah. And that's one of the situations we talked about with where that's actually a very big necessity, right? Unless you have like a router or you have the... You do chemical etching, right, Jerry?

**Jerry Ellsworth:** Mm-hmm. Photo and... Yeah.

**Dave Jones:** Yeah. I've been doing that for decades. Yeah. Yeah. It works fine. And you can go from a... You know, I can have a board ready in an hour or something like that. It's, you know, it's quick.

**Chris Gammell:** Yeah.

**Dave Jones:** And easy. But, yeah. That's...

**Chris Gammell:** There's a link on Hackaday about that today because there was a guy that printed directly to the circuit board. I thought that was kind of cool. Because, you know, a lot of people do the toner transfer.

**Dave Jones:** Yeah. There's inkjet printing versions of them where they put these special inks in inkjet. They modify an Epson inkjet printer because it uses a special type of printhead which allows it to work. And, yeah, apparently they've had some success with that. But, yeah, nobody's really cracked the...

**Jerry Ellsworth:** I've seen some that use commercial ink and there's some baking process.

**Chris Gammell:** Oh, yeah?

**Dave Jones:** Yeah. That's right. Yeah. You put it in the oven and it sits hard and then it... Yeah.

**Chris Gammell:** See, that's like printing onto a copper clad, right? And then you etch away. I would think that if you could... The way that I would suggest doing it if there ever was a Kickstarter project would be to modify a printhead so that it actually printed conduction layers, like a conduction layer, which would be really hard.

**Jerry Ellsworth:** It's difficult because I've tried this. I've tried using both the HP and the Epson Piezo printheads. And they plug up very, very easy. Oh, yeah? I tried to run this very thin dopant through, which I've been using the semiconductor stuff. And it just plugs up almost instantly. Yeah. Yeah.

**Chris Gammell:** It's like almost you need a whole new printing topology, right? Yeah. Yeah, it's tough.

**Jerry Ellsworth:** I don't know. There is some research with dip and... I don't know the exact name, but it's pretty much like a quill and ink. So it dips in and then it'll drag it onto your work surface.

**Chris Gammell:** Really? Yeah. I've seen one. Oh, right. Okay. Yeah, I've seen one like that before. Like where it prints resistors. I've seen that kind of thing before. Yeah. That was very large feature size still. So I don't know if that would be available for really tiny kind of things. But I would think that would be the way to start too. I mean, either try and raster it across where it's actually using a pen or you try and print actual layers like a regular inkjet or laser jet would do it.

**Dave Jones:** But then regardless of the process, you come down to the same points as that. Well, that's great for single-sided and maybe double-sided if you can flip it over and you can get the registration right, which is a problem in itself when you flip the board over. Well, then how do you do your plated through holes and how do you do your drilling? You still have to drill the damn things by hand. And it's just... Yeah. It's great for those little one-off things that work well on a single-sided or a coarse double-sided board or something. But yeah, I know. If you're trying to do a real bore, a real double-sided bore with lots of vias on it and stuff like that, it's just...

**Jerry Ellsworth:** I've always wanted to try to do 3D printing but with conductive layers. So you would... There are some 3D printers that use a powder that's centered after the fact. And if you could deposit a conductive layer, I could see some interesting things you could do where you could build up the vias from the bottom to the top side.

**Dave Jones:** From the bottom to the top, yeah.

**Jerry Ellsworth:** You could even have pockets for surface mount components. You could stop the process halfway through and drop them in and then keep building up.

**Dave Jones:** Unfortunately, yeah. There's a problem where then you've got to solder it and... Well, solder it. Sorry for you yanks out there. Solder. Solder. And then you've got to solder it. So, well, usually I don't think the 3D printing... I don't know. What temperature do they melt at? The 3D... The typical 3D printing plastic material, polymer.

**Jerry Ellsworth:** I don't know. I don't know either. Anyone know? No. No? No.

**Dave Jones:** Okay. But yeah. It'd have to be like 500 degrees or something like that. Otherwise, yeah, you solder them and your board falls apart. Oops. Yeah. Yeah, that'd be...

**Chris Gammell:** Didn't they... There was someone who was working on transistors with a MakerBot or a RepRap or something, wasn't there?

**Dave Jones:** Mm-hmm. Yeah, I remember something like that. Yeah, here it is. I don't know what became of it, but...

**Chris Gammell:** I think it's still in the works.

**Dave Jones:** It's a university project.

**Chris Gammell:** Yeah. So Matt Metz posted it on Make. Who was it? John Sarek. Mr. Kim and John Sarek. That's right. I got a shout-out in that. Yeah, you did. And so that's actually... That's a good start. I mean, they were large, large feature-sized transistors. They kind of layered them together, but...

**Jerry Ellsworth:** You know what? The microwave guys really have it... Have some really cool processes down. These ceramic substrates that are... Yeah. ...are sintered, and they have different conductive layers that are... I forget the name of it, but it's kind of laid down in sheets.

**Chris Gammell:** Mm. That's pretty cool. Yeah, that might be a good way to look at it.

**Jerry Ellsworth:** Right.

**Chris Gammell:** Hmm. I can't believe Dave hasn't objected in the meantime. I mean... Come on, Dave.

**Dave Jones:** No, no, not at all. I totally encourage... I totally encourage all this. I just know it's not going to happen in the home, and it's not going to be a revolution, which is your original claim, which you tried to weasel out of, Chris.

**Chris Gammell:** Ah, nope.

**Jerry Ellsworth:** Ah.

**Dave Jones:** Oh, dear, oh, dear. I don't know.

**Jerry Ellsworth:** Well, you'll have to let me back on when I make... That's where I am, hours up, guys. ...when I make the revolution happen.

**Dave Jones:** All right. I'll humbly eat my words.

**Chris Gammell:** And then you'll fly to the U.S.

**Dave Jones:** And then I'll fly to the U.S., absolutely. Hanging out in Ohio.

**Speaker ?:** Woo!

**Dave Jones:** It's all happening in Ohio.

**Jerry Ellsworth:** That's right.

**Dave Jones:** Cleveland, Ohio. Yeah.

**Jerry Ellsworth:** That's where the action is. This Wednesday, I'm heading out your direction, Chris. There's the Midwest Gaming Classic. I don't know how close it is to you.

**Chris Gammell:** No, that's pretty far still. Oh. Midwest is pretty big. Right. That's a long drive to the middle.

**Jerry Ellsworth:** Fixin' two. Go to the Midwest Classic.

**Chris Gammell:** Fixin' two, yeah. That's out in Madison, right? Or something like that?

**Jerry Ellsworth:** Something like that. I don't even know I have the plane tickets, but I don't remember. Just hop on a plane.

**Chris Gammell:** It might show up to the right spot. Yeah, hop on a plane and you're there. Spot, yeah.

**Dave Jones:** You can't really do that here. You hop on a plane. There's only a couple of points you can go to. Yeah. Because most of the center of Australia is just nothing. Right. Really. Yep. That's why it's called the Outback, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, our amp hours up, I'm afraid.

**Chris Gammell:** It is. Our first guest.

**Dave Jones:** And we covered absolutely nothing. Oh, please.

**Chris Gammell:** We got through 15 points on the sheet. That's way better than usual.

**Dave Jones:** Did we? Oh, no way.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** That is. How did we do that? It's all because of me. With Jerry on board as well.

**Chris Gammell:** Yep, I guess so. I'm taking all the claim. It's because she's a race car driver.

**Jerry Ellsworth:** You got to keep moving. You got to keep steering and giving input.

**Chris Gammell:** There you go.

**Jerry Ellsworth:** Well, it's been fun. Thanks for having me.

**Chris Gammell:** Yeah. Well, thanks for coming on the show. It's nice to be had.

**Jerry Ellsworth:** Thank you very much, Jerry.

**Chris Gammell:** Yep. All right. Well, we'll maybe talk about having another guest in the future too, right, Dave?

**Dave Jones:** Awesome. Yeah. I think this has worked. We were a bit worried about how three people talking over each other would work. But I haven't heard back the finished result. Yeah, we talked over each other really well, I think. Yeah. I think it worked just fine. So you could see more threesomes in the future.

**Chris Gammell:** Put your swords.

**Dave Jones:** Nobody's going there, are they? All right. Okay. That has to be the name for today's Ampower, surely. No, no. The threesome theoretical.

**Chris Gammell:** I'm just cutting out those last two minutes right here. It's not even going to show up on the recording.

**Jerry Ellsworth:** What is the phrase? Terrible threesome or something?

**Chris Gammell:** Terrible threesome for kids that are growing up.

**Jerry Ellsworth:** There's got to be a threesome one. Fearsome threesome.

**Chris Gammell:** I just think we'll come up with something else.

**Dave Jones:** Oh, come on, Chris. Should I stop recording? Are we done?

**Chris Gammell:** No, we're not done. Well, I guess so.

**Dave Jones:** No, we're not done.

**Chris Gammell:** We've got to say goodbye, I guess, this last minute. All right.

**Dave Jones:** All right.

**Chris Gammell:** Thanks, Jerry. All right. Bye, guys. See ya. Bye.

**Chris Gammell:** Bye.

**Speaker ?:** Bye. ! Thank you.
