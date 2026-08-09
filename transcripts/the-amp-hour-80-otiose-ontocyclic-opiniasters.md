---
episode: 80
title: Otiose Ontocyclic Opiniasters
url: https://theamphour.com/the-amp-hour-80-otiose-ontocyclic-opiniasters/
---

**Chris Gammell:** This is the Amp Hour Podcast, recorded January 29th, 2012. Episode 80, Otios Ontocyclic Opinionasters.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Dave Jones:** I have to say it, Arduino sucks.

**Chris Gammell:** You're just having a bad Monday, aren't you?

**Dave Jones:** Yeah, I think so. It's Monday there. It is a Monday. Usually we record on Tuesdays, my time, of course. Yeah, yours, right. Which is the leading time because we're ahead of the US in everything.

**Chris Gammell:** Of course, you guys are always ahead of us. Yeah, that's right. Returns of kangaroo races and shrimp barbieing.

**Dave Jones:** Shrimp barbieing, yeah. And there's koalas climbing the harbour bridge. Yep.

**Chris Gammell:** So, Monday, yeah. How's Monday going? Other than...

**Dave Jones:** Freaking Monday. Well, all my hurdles are past me, so Monday's looking good.

**Chris Gammell:** All right, good. So, Arduino problems, huh?

**Dave Jones:** Yeah, it sucks. This is the first time I've ever, like, actually designed a real Arduino. Like, I've, you know, I've hooked up an Arduino and typed a bit of code in and something popped up on the LCD and it worked. You know, that kind of thing. But actually design a product, Arduino compatibility, into a product. And it's been nothing but a nightmare.

**Chris Gammell:** Huh. Well, so what made you decide in the first place to use one? I mean, because maybe it's your fault for using it.

**Dave Jones:** Well, it is, yeah, of course. And everyone says, oh, duh. Of course Arduino sucks. Why, you know, why the hell are you doing that? And, well, the idea was that this is a power supply kit and, you know, it's for beginners. And I thought, well, you know, I can, you know, the community can build on. Arduino is massively popular. It might be popular, you know, it might be even more popular if people say, oh, it's Arduino compatible. I know how to program in Arduino. Great. I can modify the code and, you know.

**Chris Gammell:** So it's kind of like broad base making it acceptable. Not acceptable, but more accessible, rather.

**Dave Jones:** Making it more accessible for more people, yes. It's not a bad idea. Yeah, exactly. And that was the intention. And I thought I'd give it a go.

**Chris Gammell:** Minus the inability to code in it, right?

**Dave Jones:** Well, yeah. Well, no, it's problems with the tools and all that sort of stuff. But, yeah, I thought, well, why not? You know, because it's just an AVR. If I don't like it, I can always, you know, I didn't like it. Or somebody doesn't like it, they can always go back and program directly in C or freaking Klingon or whatever it is they want on the AVR. Yeah, because it's an abstraction layer, basically, right? Yeah, it's Arduino. It's just another extraction layer on top of, you know, regular C++, really. And it's handy because there's lots of libraries out there. There's libraries for Ethernet. If I want to add Ethernet to this thing real easily, there's an Arduino library. I plug in a module and bang, away it goes, you know. There's that massive support base out there of all these libraries. So what's the great thing? Which brings me to my first gripe. Oh, boy. Which is none of the bloody – all these hundreds of thousands of libraries people have written all out there, right? Yeah. But a good lot of them now are useless. They have to be rewritten. Oh, no, because of the hardware? Because Arduino have gone from alpha. I didn't – actually, I had forgotten that. Arduino's always been up until, I don't know, when they released 1.0 recently, right, in the last month or two. It has been alpha software. So it's grown to this massive popularity based on the software's alpha. Like it's not even beta, right? Anyway, Arduino released – the Arduino team released the version 1.0 software. Oh, yeah. I heard about that. I remember when that happened.

**Chris Gammell:** That was a month ago or so.

**Dave Jones:** So I went to the website. Okay, I need the latest version of Arduino. I'm going to download the latest version, right, 1.0. Of course I'm going to do that. And it turns out, wah, nah, that's the wrong thing to do. Arduino 1.0 sucks ass or sucks ass. Sucks American ass. So everyone tells me. And it's not compatible with a whole bunch of existing code out there. They've changed the API, the application programming interface. Presumably for good reasons. In the future, everyone will thank them for it, right? But at the moment, no, a lot of the existing code out there is broken. Yeah, exactly. And, well, maybe they should have done that with the pin spacing, huh, on the header. What do you mean? All those. The incompatible and the shield. On the Arduino header, shield uses an incompatible. It's not on a 0.1-inch footprint. And they've been copying flack over that for years now.

**Chris Gammell:** It's not 0.1? I thought it was. No.

**Dave Jones:** No, it's not. There's one pin which is on one of the headers, which is offset by my 50 mil. And that screws everything up.

**Chris Gammell:** Yeah, now that I think. I do remember people talking. I always thought they were talking about. They always said 0.1, but I didn't realize they were saying that it didn't have 0.1.

**Dave Jones:** Yes, it didn't have 0.1. It's got 0.1 for all of them except one of the headers, which is offset. And they admitted that, yeah, whoever laid out the first board goofed it. And they've had to live with that footprint ever since. Rather than take their medicine up front and just, you know, okay, we screwed up. We'll fix it. All the existing shields, which aren't many at the moment, are incompatible. And, yeah, we'll just go forward. But it looks like they've done a similar thing. They've taken their medicine now with the environment, the API. And it's broken all this existing code.

**Chris Gammell:** Which is a good design lesson, right? I mean, there's no way for them to know that they were going to be extending for this long, right?

**Dave Jones:** No, no, exactly.

**Chris Gammell:** But you're right. Now you've got to support it all.

**Dave Jones:** That backwards compatibility issue is a big deal. And it's the main attraction. I mean, if there's one big attraction to Arduino, it is the fact that there's so many people using it and so much existing example code out there. It's everything. And now it's a good lot of it. Some people say, oh, 95% of it, but I don't think it's that high, is incompatible with the new API. It's not hard, apparently, to change the code to fix it. But the fact is, you know, if you're a beginner, you download it, compile, fail, doesn't work. Gives you all these cryptic C++ error messages. Well, you know what the real solution would be?

**Chris Gammell:** If this was like NASA or, you know, like the NOAA, you know, like the National Weather Service, anything like that. Oh, right, yeah. You know what they would do here, right? They would hire an old geezer to maintain the old code, and then they'd just build another abstraction layer on top of that. And then you just start again. Yeah, yeah. That's the way it's done. You know, that's why people are still writing Fortran.

**Dave Jones:** And that's the way it's done in the banking industry, right? Yeah, exactly. They're still using, you know, all the baseline codes all in Fortran and COBOL.

**Chris Gammell:** Exactly, exactly. And then they also have to buy like 133 megahertz motherboards, you know, with the turbo button. Yeah, yeah. Yeah, I've seen that before. It's amazing. You know, I've actually talked to a coworker about this before, how I'm not sure how the logistics of it would work. But like, I think there's a real business case for like starting a business where all you do is support old designs. And that reminds me, there's a company that does that. There is. Oh, tell me about them.

**Dave Jones:** And before I forget, I tweeted it the other day. They start with W, WDC or something is the name of the company. And they've just released the 6502 processor in the original DIP40 package.

**Chris Gammell:** That's right. Yeah, I saw that.

**Dave Jones:** And you can buy it from Mouser, right? So if they're, you know, some people complain, oh, it's seven bucks or something, you know. Right.

**Chris Gammell:** But that's the thing. That's the brilliant thing about this business idea because people will pay it. I mean, they'll pay more than that. Yeah, of course they will. If you are in a jam and you can't get a 6502 and it's in the only product you sell, you're going to pay infinity dollars, right? I mean, like there's a niche business for that. There will be a practical limit where they can't, you know, the company buying that processor can't sell to their customers anymore. But believe me, it is very high. And there's other companies based on that same kind of thing. I mean, Rochester Electronics.

**Dave Jones:** They sell old surplus ICs.

**Chris Gammell:** Yeah, they buy dye and they cut the dye.

**Dave Jones:** That's a huge market, yeah. Yeah. Especially for stuff I've worked on in the past, which is old, you know, old design based on military stuff. A lot of military stuff is, you know, I mean, it's already 10 years behind when it actually gets released. And then 10 years later, when you've got to maintain it again, you're using 20-year-old chips. So you've got to go out and find that 20-year-old processor, you know? Yeah. So, yeah. And there's a niche market out there for that.

**Chris Gammell:** Yep. Oh, here we go. So this is actually a programming thing, but I think we get extended to hardware here. It's an idiom, right? Programming is like sex. One mistake and you have to support it for the rest of your life. Yeah. Beautiful. I mean, you really do. It's the same thing, though, you know? Of course, yeah. Like, if you really do have these weird paradigms that you have to support, then you've got to just keep dealing with them. And then, you know what the real problem is? As a young whippersnapper myself, the young whippersnapper comes in and says, oh, I can fix this. And basically, you struggle against it for about six months. And then finally, you're just like, ugh, all right, fine. Yeah, just give it.

**SPEAKER_01:** Yeah, exactly. Okay, I get it now. I give up. All right.

**Chris Gammell:** Yeah.

**SPEAKER_01:** Oh, that's brilliant.

**Chris Gammell:** Yeah, so that sucks. You've got to deal with that. But sorry, are you going to switch over to a new board or something? Because you're already on Rev 2, aren't you?

**Dave Jones:** I'm already on Rev 2 or Rev B board, yes. And I'm going to go to a Rev C because there's a few things on there I want to change. There was one error because I was dragging around my schematics, right? You know, if you watch the videos, I went from like everything jammed onto one A4 sheet into when I did Rev B, it was in a bigger A3 sheet. You probably don't know what A4 and A3 is being a yank.

**Chris Gammell:** A4 is close to 8.5 by 11, which is standard letter.

**Dave Jones:** Yes, it's close to the letter size. I don't know what A3 would be, but A3 is double A4 size.

**Chris Gammell:** Yeah, it's like tabloid, basically like a schematic size, right? I mean, that's what you really want to print on.

**Dave Jones:** Yeah. So I reformatted to that. So that entailed dragging my schematics around, copy and paste in and putting nice pretty boxes around them and doing all that. And in the process of doing that, I obviously deleted a couple of lines and thought I could put them back. And I swapped two pins on the op amp, didn't I? Oh, no. Yeah, yeah, yeah. Somebody thanks to whoever pointed that out to me, but I would have found out eventually. Yeah. When I build up a circuit and it's, huh? It's not regulating.

**Chris Gammell:** Or it starts letting out blue smoke. Yeah.

**Dave Jones:** Oh, man. Oops.

**Chris Gammell:** I hate that. So that was just from the actual transporting of schematic symbols?

**Dave Jones:** Just the dragging around of the cut and pasting of the schematics, yeah, to making them. Because it was all crammed together, so I had to cut and paste and select and move little bits out of bigger bits and it got all ugly.

**Chris Gammell:** Dave, you were complaining about it. You were looking at a schematic the other day and I remember you complaining about how smooshed together it was. You're breaking your own rules now.

**Dave Jones:** No, I don't mind smooshed together. I wasn't complaining about it.

**Chris Gammell:** I hate smooshed together.

**Dave Jones:** No, I love that if you can cram a schematic on one sheet. That's brilliant. No, that is the holy grail of electronics. Your schematic on one sheet. I swear.

**Speaker ?:** You are old.

**Dave Jones:** That's what that is. No. That's what you are.

**Chris Gammell:** You've got these huge symbols with 20 pins on a super fancy micro. Yeah. No, I don't like that. I don't like necessarily.

**Dave Jones:** No, I wasn't complaining about that.

**Chris Gammell:** You were. Whatever.

**Dave Jones:** I was complaining about people don't put enough annotation and information on the schematic. I was looking at even the Arduino ones do this. They're horrible for it. If you look at some of them don't even have the names of the chips on them. That's what I was complaining about your Schmoo project. The S-E-E. C-E-E. Whatever it is. Yeah. C-E-E. Sorry. Yeah. Project. I looked at the schematic for that. I swear, unless I'm a Stevie Wonder and can't see it, they haven't put the chip number next to it. They've got the chip there with the pins and everything. They don't tell you what the chip is.

**Chris Gammell:** I haven't looked at the latest one.

**Dave Jones:** Do I have to go look up U1 and then go look up cross-reference of Bill of Materials or something to find out what the chip is?

**Chris Gammell:** Put the damn number on the schematic. I don't agree with that. You're right. I don't like just having the reference designator. You've got to have the actual chip name.

**Dave Jones:** You've got to have the chip name. What is with that? I mean, that's just-

**Chris Gammell:** You know what the worst thing is, though? When you start having multiple chip names, like if you have an internal name for a chip, like some of the companies that work- All the companies-

**Dave Jones:** It's the Dragon processor or something, but it's actually a rebadged something else.

**Chris Gammell:** Well, no, not any of that. I mean, like if there's an internal part naming system because you bring in resistor one and resistor two, right? So then you need three markings on the page, right?

**Dave Jones:** And it's 369-497. That's the part number for that. Yeah, that's the kind of part number. Right, exactly. No, that doesn't go on the schematic. That's buried in the Bill of Materials for purchasing and stuff like that.

**Chris Gammell:** I've seen it on schematics, too. I mean, it depends. Oh, no, that's just- Because then you can-

**Dave Jones:** Well, yeah, okay.

**Chris Gammell:** It's kind of like a built-in security measure then, right? So if you lose that- Yeah, I've probably seen that. Yeah. It's not necessarily just, oh, well, this is an LT- Well, that's okay. 10-07.

**Dave Jones:** As long as it doesn't substitute the actual real part number. You can put it in addition.

**Chris Gammell:** If they're both there, yeah. If they're both there, that's good. That's great. What I'm saying is I've seen it without both there. Oh, okay. So you'd have reference designator and only internal part number, and then it's like-

**Dave Jones:** Right, yeah, yeah. And yeah, okay, yeah, I've seen that, too. I've probably had to do that, actually, on a design or two back in my military days. So, yeah.

**Chris Gammell:** Yeah, you got to hide those secrets, how to hook up an op-amp.

**Dave Jones:** Follow some convoluted naming system that some idiot in the company made up 50 years ago. It was just propagated.

**Chris Gammell:** Exactly. There's another one where it's like, I've seen schematics where the LEDs are named pilot lights, right? It's like, what are you going to do? Yeah, yeah, right. You know? It's just, they all get shoved in the same category.

**Dave Jones:** And they've got little filament symbols, you know? Yeah, exactly. It's actually a little filament with a glass bulb around it.

**Chris Gammell:** Yeah, I don't think that's what's really going on in there anymore, right?

**Speaker ?:** Right.

**Chris Gammell:** Yeah, but it's just the stuff you got to live with. Yeah, yeah. I don't know.

**Dave Jones:** No, if you work at a company, you play by their rules. That's right. Yeah.

**Chris Gammell:** I guess the real question is-

**Dave Jones:** That brings me to my next bitch.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Oh, man, I got no end of him today. I'll tell you what.

**Chris Gammell:** He is raring to go. Monday, guys. Monday. That's what I'm saying. And Dave comes off a weekend of-

**Dave Jones:** Moaning Monday. Yeah, moaning Monday. There you go. Where I just moan about everything. Yeah.

**Chris Gammell:** Oh, that's good. All right. All right, go ahead.

**Dave Jones:** And that segues directly into something I expected from my latest video. I posted some code in there, right? I showed some code. And I was debugging code in real time trying to fix this DAC problem, right? And, of course, nobody talks about anything else about the product apart from how shit my code is. You know, that's all they talk about. Oh, no. What are you doing that for? No, don't do this. Do this. Do this. And I was like, shut up. It's a dictatorship. Okay? It's my code. I'll do what I damn well like. Stick it up your ass. You don't get a say in it.

**Chris Gammell:** Yeah, that's one of those things where a lot of the people – I mean, like, software always seems accessible, right? And so – Yeah, yeah. Everyone's accessible. And I haven't seen your code. It really could be shit, right? Well, it could be, yeah. But it's like everyone has an opinion. So that's what the real problem is. That's the problem.

**Dave Jones:** Whereas hardware, it's order and magnitude more opinionated than hardware. I mean, I've had a lot of – with the Power Supply Series, I've had a lot of opinions. A lot of opinions on the hardware of what I should and shouldn't have done. And it's like – and in the end, it comes down to that's what I want to do. So kiss my ass. I guess what it comes – yeah, with hardware. I mean, your way is not better.

**Chris Gammell:** With hardware, there's only two ends of a resistor. You're going to hook it up one way or the other. Both are right. With programming, you can do whatever the hell you want to, as convoluted as you want it to be. And then it hopefully will work at the end.

**Dave Jones:** Well, I think my code is not convoluted at all. And I think it's very straightforward. And people took me to task because I didn't put something in a for loop. My SPI driver code, oh, I should have put that in a for loop. And you should have done this. And well, you know. I don't know why you keep – It was easier to cut and paste. And it was easy to modify when I was debugging the thing. So bite me. I don't know why you even keep YouTube comments on.

**Chris Gammell:** I was talking to Steve Grafio about that. You know, like what are the value of YouTube comments these days?

**Dave Jones:** It's just – Well, it makes in your search engine – in your rankings. It's big for rankings. So yeah, turn them off at your peril.

**Chris Gammell:** Yeah. Search for the word ass and they come up in comments all the time, right? Or something like that. Like every bit of profanity comes up in a YouTube comment search.

**Dave Jones:** Oh, yes. YouTube commenters are the most colorful of any – Scum. Yeah. Scum. They are. I'm just – Whatever. There are some bad – yeah. You get a much higher percentage of bad ones on YouTube than you do anywhere else. Yep. And everyone has an opinion. But no, they don't talk about the hardware or anything else. All they're talking about is bitching about the code. And then, you know. Yeah. Anyway, I really – I expected that. So it's not – you know.

**Chris Gammell:** Yeah. Not surprised. In the least. Well, what else is in there? I mean, you got the Arduino wonkiness. You got the people on YouTube. Yeah.

**Dave Jones:** Well, there were a couple of things with the Arduino wonkiness. It wasn't just the fact that they broke stuff with the API interface, you know. There was other stuff. Like I found out the hard way that the Arduino IDE, right, can actually delete your source code file and the entire subdirectory it's in with one click of the mouse from within the IDE. I find that staggering. I don't know of any other development environment I've ever used where I can actually delete the code I'm working on from a menu option. It actually erases – it deletes the file from your file system and deletes the subdirectory. And there's a drop-down menu there. Delete. Boom. Gone. I thought it was just, okay, I'm deleting the tab on the IDE. You know, the IDE has open different files and it has different tabs you can open up and you swap between files. And I thought I was just shutting down one of those. But no.

**Speaker ?:** Poof.

**Chris Gammell:** Gone. No backups. Nothing.

**Dave Jones:** What possessed? In what universe is this a good idea to add a delete option to a program, any program, let alone one designed for beginners? Are you shitting me?

**Chris Gammell:** Yeah. Well, why did you click it?

**Dave Jones:** Because I wanted to figure out how to delete the tab, close down a file. There's no close option. I couldn't find it. So, oh, it must be delete. Boom. Yeah. You know. Silly me. I didn't see that it would delete the whole file on the subdirectory it was in.

**Chris Gammell:** Yeah.

**Dave Jones:** Unbelievable.

**Chris Gammell:** Anyway.

**Dave Jones:** And there were other stuff. There were – basically, Murphy got me at every step. Yeah. You know. It was – a lot of things conspired to make my first Arduino experience, you know, completely horrible.

**Chris Gammell:** That's too bad, man.

**Dave Jones:** I know. It sucks. But anyway, I'm over the hurdle now, I think.

**Chris Gammell:** So now you're locked in, right? There's no going back now?

**Dave Jones:** Now I'm locked in. Yeah. Yeah. Exactly.

**Chris Gammell:** See now – so I'm going through the same thing. I'm starting up a project with just a simple MP3 player. And I'm putting it into this old vintage radio, and I've been talking about it for a little while. But I don't know – What? Why? I'm still keeping the tubes. I'm pumping it into the tubes.

**SPEAKER_01:** Right. Oh, the tubes still light up.

**Chris Gammell:** Yeah. No, they're not lighting up. Do they actually do anything? Yeah. I'm pumping the audio right through the tubes.

**Dave Jones:** Oh, awesome. For that warm – Get some extra distortion on top of the MP3.

**Chris Gammell:** Yeah, right? Yeah.

**Dave Jones:** You better run a very low bit rate on that MP3, too, rather than like 16K samples per second or something.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Telephone quality doing it. Yeah, right. 8K samples.

**Chris Gammell:** Oh, my God. But, yeah, it was – Why not? The tubes are going to give you a couple of percent distortion anyway. Oh, they will definitely, yeah. Awesome.

**Dave Jones:** Anyway, continue.

**Chris Gammell:** Oh, no, it's – I'm just wondering about the – I was asking on Twitter earlier this week about that. You know, I'm trying to decide whether or not to just go with an existing board, like an Arduino or something with expandable headers, like a BeagleBone, Arduino.

**Dave Jones:** BeagleBone's overkill, I think.

**Chris Gammell:** It's total overkill. But the tradeoff there is speed. Granted, I still have to get the BeagleBone up and running and get the file systems, and that's full-blown Linux, too.

**Dave Jones:** There's plenty of boards out there that just – like they have like a PIC or an Atmel on there, and they have an SD card slot, and they play MP3s. There's plenty of projects like that. Surely somebody sells a kit for that, and you can just buy the board. Yeah, well, that's the real question. It's literally a DAC chip. It's literally an AVR or PIC chip with an SD card.

**Chris Gammell:** Yeah, but the question is – well, not the question. The thing that I'm trying to balance, too, is like I want to use this as like a learning more, too. I want to go along and have stuff to learn and more embedded experience.

**Dave Jones:** Right, so it's not just hacking something together to work.

**Chris Gammell:** Right, yeah, exactly.

**Dave Jones:** Otherwise, you just would have gone to the $2 shop and bought a little compact MP3 player and stuck that in there and wired it up.

**Chris Gammell:** Right, exactly. It's like why – yeah, because you can get MP3 players for about $3 these days, something like that. Yeah, exactly. Exactly. It's kind of ridiculous, but –

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, so I don't know. I don't know if I should –

**Dave Jones:** And it has to play MP3s or can it play WAV files? Because WAV is easier. You know, there's less processing and grunt involved in doing WAV files.

**Chris Gammell:** The balance there is just the size of the SD card, I guess.

**Dave Jones:** Well, they're cheap, but you can get a two-gig one for free. They give them away for – I've got a drawer full of them here. Send me some then, man. But it costs more in postings than it would, too. Yeah.

**Chris Gammell:** You'll be fine. Just send me some. Yeah, you got these accounts. You're good. Right. Yeah. So, I don't know. I'm moving along. I'm enjoying ripping this radio apart and it's – Okay. That's fun.

**Dave Jones:** I see you wanted to use some old chip or something that's obsolete. Is that right?

**Chris Gammell:** Yeah. Yeah. I was looking at the – you know, I was actually looking at Lemore's project, Minty MP3. And I didn't know that one. I think that chip is still around. But then the – There's another one that's like just a really hard chip to get. And it is funny, too, because like it's like this all-in-one chip. It's by VLSI Solutions, which is I think a Finnish company. And – but they're just so hard to get because they don't distribute through anyone. You know, you go on like Find Chips or Octopart and it just says, nope, no one sells those. And you can go –

**Dave Jones:** Because they're only sold to the toy companies you want to make a million little MP3 plays. Exactly.

**Chris Gammell:** And then when I try and buy – actually, I think SparkFun has it for like $20, which is still a lot.

**SPEAKER_01:** Yeah, that's a lot. Yeah, that's huge.

**Chris Gammell:** Exactly, right? And then, you know, you see them in bulk. You can get them for like $3. But I'm not buying more than – I'm two maybe, so.

**Dave Jones:** Right. You need to go to a market in Shenzhen.

**Chris Gammell:** Yeah, exactly. That would be, you know, a perfect – if I had that kind of access to materials.

**Dave Jones:** Maybe somebody has a reel somewhere, but, you know – but none of it's itemized, you know. So you have to go store to store. Oh, yeah, this guy's got reels. I'll ask.

**Chris Gammell:** Yeah, yeah. Yeah, and then they just were like, no, no, just believe me. It plays MP3s. Yeah. Oh, boy. It's interesting. We have some stuff on the list about that ability to get on the street. If you're a manufacturer, right? Say you're manufacturing your heart up for stuff. Basically, that is a competitive advantage over anyone else. So if you're – that's why companies making electronics in Shenzhen or Beijing or anywhere else they're doing in China. Or even like – what's the one in Japan? What's that shop?

**Dave Jones:** Akibaba. I'm pronouncing that wrong. I'm sure. Akiraba or something.

**Chris Gammell:** Yeah. Yeah, but the same thing. You know, you're able to just go down the street and you have this whole supply chain set up. And there was an article earlier this week about – it was on Bloomberg actually.

**Dave Jones:** Oh, dubious quality of course. But still, hey, it's there, right?

**Chris Gammell:** Oh, yeah, yeah, yeah. You don't know if you're getting necessarily – yeah, if you're buying it off a stand, you know, you don't know if you're getting like top quality parts. In fact, you should probably plan that you're not.

**Dave Jones:** Akai is also selling hot dogs, right?

**Chris Gammell:** Soda is 99 cents more.

**Dave Jones:** You get a free reel with every dog.

**Chris Gammell:** Yeah, yeah. But yeah, there's a lot of hubbub this week about that Apple article. It was Apple talking about Foxconn and just availability and how Steve Jobs was able to – they wanted to quickly bring up the screen capability and how the supply chain is in place in China. And that's true and it's just something that basically everyone else has to deal with outside of China and that's kind of the big competitive advantage these days. This Bloomberg article actually talks about that the wage difference isn't necessarily the only thing holding people back anymore. Oh, no. It was crazy. I always – because it's only 10% of the cost difference and the rest is just availability workers and regulations and taxes and everything else. And I didn't realize it worked like that. I mean I'm always shocked when I see that kind of stuff.

**Dave Jones:** Yep. That's the real world.

**Chris Gammell:** Well, damn it.

**Dave Jones:** I know. I want to continue to live in fairy land. Yeah, right? Oh, boy. Yeah, it's a big deal. You know, availability. Try living here in Australia. You know, we've got Farnells here which isn't bad. But, yeah, but, you know, they're holding less and less local stock and it's got to come from Singapore. It's got to come from somewhere else or, you know. Yeah. And then it's still not as big as Digikey and then Digikey, once again, isn't often – isn't as big as, you know, the local markets in Shenzhen. So, you know, well, especially in terms of price and stuff like that and sometimes availability and – yeah. So, they can't carry everything. There's just too many parts, damn it. That's the problem with the world.

**Chris Gammell:** One of many, yes. Yeah. So, speaking of manufacturing though, I mean, there was an announcement this week, at least in the U.S. about –

**Dave Jones:** Your illustrious leader.

**Chris Gammell:** Yeah. Oh, yeah.

**Dave Jones:** Your illustrious leader gave his State of the Union speech, which nobody else in the world gives a shit about. But apparently it's a big deal in the U.S., right?

**Chris Gammell:** Yeah. Yeah, I guess so.

**Dave Jones:** But what I heard was very great. Which he has no power over anyway. Well, that's true. But aside from that – Congress, send me a bill now and I'll sign it today. It's like, well, Congress are half and half. They each hate each other and they're not going to put through jack shit.

**Chris Gammell:** It's not the country who works at all. Right. But I did like what you were saying. I did like the idea, but some of the execution is kind of interesting. Like, so that same thing with availability of parts, right? Say we try and bring tons of tech manufacturing back to the U.S. today. Like, just even PCBs. Hang on.

**Dave Jones:** Can we start out by saying at the State of the – if you haven't heard Obama's State of the Union address, basically pretty much at the start, I think it was, he started talking about bringing manufacturing jobs back to America. That was – you know, that's going to be the saving, you know, thing for America and all that sort of stuff. Maybe. Well, you know, as well as taxing the rich and prosecuting the people of the global financial crisis. And building up their military while at the same time downsizing it, which is an oxymoron. Yeah. Anyway, let's not go there. But anyway, yeah, he's – you know, he gave lots of rah-rah about bringing local jobs and manufacturing back to America.

**Chris Gammell:** Right.

**Dave Jones:** So that was the basis of this whole thing.

**Chris Gammell:** Right. Exactly. And I like that. I don't know what other people like. Of course. It's well-intentioned. Right. Very well-intentioned. But the question for this forum is, is that realistic? I mean, could electronics come back to the U.S. or even weirder, could electronics come back to Australia? And I don't know. I think, you know, that other article I was talking about –

**Dave Jones:** Well, it can for the U.S. For Australia, you know, no. It's just not going to happen. Now, Mark, it's not big enough.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, yeah. I can't even get a production PCB manufactured here. I can get a prototype PCB manufactured here but not a production board.

**Chris Gammell:** Right.

**Dave Jones:** They're all shopped out.

**Chris Gammell:** What would it take then to actually get that stuff back next to you? And I think –

**Dave Jones:** Well, it takes somebody to actually have the guts to do it and take a loss for a while until people realize the service is there and then hopefully pay extra for it as well.

**Chris Gammell:** And enough people that want to pay extra, I suppose, as well.

**Dave Jones:** It has to be an affluent market that people see an advantage like I am at the moment. I see an advantage in advertising my stuff as locally produced or as locally produced as possible even though it costs more. But, you know, hopefully people will think, oh, yeah, that's a cool thing. I'll pay extra for that. I could be wrong and go out of business but that's fine. You know, at least I'm having a go.

**Chris Gammell:** Yeah. And I think that, you know, in terms of like parts and availability of parts, I think that kind of stuff actually does build back up. But it doesn't build back – you know, there's all that stupid lean, you know, lean manufacturing and all that other crap.

**Dave Jones:** Yeah, just in time. Just in time.

**Chris Gammell:** Just in time meaning you can't get parts. Sorry, guys. Yeah, that's right. Yeah. You could if you were just in time with payment as in lots of payment. But I think that stuff builds up naturally alongside it. So I don't know. There's – I think there's a compelling case for it but I don't know. I don't know if it's going to happen in the next 10 years but I hope it does because similarly, I would love to be able to buy a board from a local house if for nothing more than to be able to go knock down their door and be like,

**Dave Jones:** What the hell did you do here? Yeah, yeah, exactly.

**Chris Gammell:** Well, you've got that option.

**Dave Jones:** How many PCB fabs are there in the U.S.? There's a lot.

**Chris Gammell:** There are.

**Dave Jones:** Yeah, there's some.

**Speaker ?:** There are.

**Dave Jones:** End of story. There are.

**Chris Gammell:** But production run style, I don't think many go to them anymore.

**Dave Jones:** Oh, no, because everyone wants the last cent, you know, they're shaving off the last cent. Right. So, you know, it's a race to the bottom. Right. So they're going to offshore. Right.

**Chris Gammell:** And I think the real thing is if that race to the bottom would ever come back, I don't know if it will because I don't want to run that company.

**Dave Jones:** No, I think that time has passed. I think people are starting to realize, you know, this China thing is oversold itself, I think. Oh, oh, like that. And, you know, there are jobs coming and there's manufacturing coming back to the U.S., coming back to Australia. We've talked about it before and it's happening and it's visible.

**Chris Gammell:** Yeah.

**Dave Jones:** That it's happening. So will it continue to happen? I think it's a certainty.

**Chris Gammell:** Yeah. Okay. Well.

**Dave Jones:** As people in China want first world wages and first world conditions and I don't blame them. They should. So I think that, you know.

**Chris Gammell:** Right. And then we can treat domestic workers like crap.

**Dave Jones:** And then India, then we can treat India as our next race to the bottom.

**Chris Gammell:** And there's a thing that keeps bouncing around. Yeah. I don't know. Eventually, costs will just go back up. There will be some semblance of equality across currencies. And then eventually, you'll have a shop down the street that'll make stuff because it's just as expensive as shipping it from across the planet. Or. Yes. Or at some point, there might be printable electronics that are cheap enough to just print your home.

**Dave Jones:** Grown. Yeah. Before it was making your own chips and now it's printable electronics. Yeah. Because you failed in that and you'll fail in printable electronics too.

**Chris Gammell:** All right.

**Dave Jones:** All right. And it comes down to the consumers too. Us. We, you know. When we expect to buy something for a dollar and, you know. And for it to flashlights. It's the real issue. And for it to flashlights and do everything else. Yeah. And we're just encouraging that market. If people actually would actively seek out all locally produced, you know, people who advertise locally produced products and all that sort of stuff and be willing to pay more for it, then the consumers can fix this. It's a supply and demand thing. Always has been. Always will be.

**Chris Gammell:** Economists. We do need them after all. Yeah.

**Dave Jones:** So. Yeah. Yeah. We just got used to in the last 10, 15 years of buying all this cheap shit from China. We got so used to it.

**Chris Gammell:** Yeah.

**Dave Jones:** And it's our own fault.

**Chris Gammell:** Yeah. I think, you know, I think with cheap stuff, I think there will be some kind of trend towards, you know, either making your own cheap stuff in terms of like printing it or buying it. You don't think so? I think so. Well, not printed electronics necessarily, but, you know. Thank you. Well, no, like printed stuff, you know, whatever printed.

**Dave Jones:** Well, yeah, for, you know, the case, a 3D printed case or something like that. Right. For prototypes. Yeah. It's not going to do it for quantity, of course. No, no. But, yeah, just for prototypes and short runs and things like that. For sure.

**Chris Gammell:** All right. Well, I'm done. I'm done on my manufacturing rant. Right. Okay.

**Dave Jones:** Thank you. Can we go on to other rants? I'm sure we have other rants. I got something about it.

**Chris Gammell:** Ooh. Go.

**Dave Jones:** Well, Dax. Dax. In my latest video. Lost in all the... Meanwhile... Lost in all the noise over my bad coding techniques and how I'm doing it all wrong was the fact that the DAC I'm using, the microchip MCP4922 12-bit DAC is a bit of a heap of shit. It's got pretty poor specs. And I actually measured them. And they're pretty darn ordinary. I was expecting better. It advertises an INL of plus minus two bits or something. And it's... But you read the spec sheet and it's plus minus 12 bits over temp, of course.

**Chris Gammell:** Oh, so that was like marketing versus reality.

**Dave Jones:** Yeah. And sort of, you know, I just sort of expected. But it is the cheapest DAC you can get on the market. So, you know... How cheap is it? Granted, I got what I paid for it. Oh, it's $1.90 or something. Which is... Sounds like a lot. But it is the cheapest through-hole DAC I could get on all of DigiQ. Oh, through-hole.

**Chris Gammell:** You're still dealing with through-hole, huh?

**Dave Jones:** Yep. Yeah. But others aren't much better. You know, they're a similar price. You actually pay a premium for these. It's not like you can get a 20-cent DAC, you know?

**Chris Gammell:** Yeah. Well, you can get... I think the thing is they're getting pushed into a lot of micros these days, too. Like, I know some of the...

**Dave Jones:** Yeah, and their performance is pretty shit, too. So, I wouldn't count on them. No, I would know. You know, you've got to use an external DAC. That's why external DACs still exist.

**Chris Gammell:** Yeah.

**Dave Jones:** Because their performance is generally better. Except in case this microchip... Well, it's not that great. You know, I was expecting a bit better. I measured three different chips, and, you know, and I could see the spread across the three chips, and... Yep. Anyway, I think I'll try the 10-bit version. It should be tighter for my application. So, here's an application where it could be beneficial to go back from 12 bits to 10 bits.

**Chris Gammell:** So, it's one of those things where it's die sorted, and you're just using the 12 bits shaky, but it's... They just say it's 12 bits.

**Dave Jones:** It's shaky, but it's... Yeah, exactly. As you said, as we said the other week, we talked about this chip, and it was the fact... You said it's exactly the same die, and they just, you know, give you the reject ones for the 8 bits, and the 10-bit ones. But at least they're tighter. Right. Because then you're... Yeah, if you look at them all...

**Chris Gammell:** Down to at least a significant bit. Yeah, exactly. If you look at them all as 12-bit DACs, and you just slice off certain amounts of bits, then they look pretty good, right? I mean, you could just... I mean, effectively, you could just use the same one and throw off the last two bits and say... Oh, yes. It's a 10-bit DAC, but then you are paying for 12 bits when you only get 10.

**Dave Jones:** Yep. But the way I'm using it, I've got to use the low-order bits and not the high-order bits, just based on the gain of my amps and stuff and how the system works. So, I've got to use the low-order bits, and I explained that in the video. So, and yeah, otherwise, yes, I could use the high-order bits of the 12-bit DAC, and, you know... But, yeah, sadly, that's not how it worked in this case.

**Chris Gammell:** So, you wouldn't switch over now to a whole new part?

**Dave Jones:** Ah, no. No, no. No, I'm sure the 10-bit one will do exactly what I want. So, the 12-bit one's adequate. You can calibrate it out if you want, but I was just expecting a bit better, that's all. I was a little bit surprised, maybe wishful thinking.

**Chris Gammell:** Are you doing this for, like, current programming, or what are you using it for?

**Dave Jones:** I'm using it to generate a voltage, which determines the output current and the output voltage of my power supply.

**Chris Gammell:** Ah, okay.

**Dave Jones:** So, the actual DC accuracy matters, you know. Yeah, DC accuracy.

**Chris Gammell:** I remember that stuff.

**Dave Jones:** Yeah.

**Chris Gammell:** That's not my world anymore.

**Dave Jones:** You know, and I'm using 0.1% resistors, and I'm using a 0.25% voltage reference, and et cetera, et cetera, and the DAC's just, eh, it's pretty darn ordinary. But, anyway, it is cheap.

**Chris Gammell:** Yeah.

**Dave Jones:** But, yeah, I know, not as cheap as just PWM in it. Yeah, yeah, yeah. Okay. No need to leave comments. Thank you. I know. Right. I'm perfectly well aware of that.

**Chris Gammell:** He gets enough software comments, folks. Yeah, that's right.

**Dave Jones:** Yeah. I decide to use an external DAC. It's lower noise, and because it's a better educational thing, it shows people how to use external devices, and then it's more expandable, more flexible for variations on the system design. People want to design their own, then, you know, they might want to put in a really schmicko external 12-bit DAC.

**Chris Gammell:** Yeah.

**Dave Jones:** The system will be capable of that. Just plug it in.

**Chris Gammell:** So, now, if you were teaching someone about, I guess you are kind of in your videos, you're teaching someone about board design.

**Chris Gammell:** But, like, say you were teaching someone about board design for 10 years from now. What would you tell them to, like, concentrate on? So, there's this article that someone shared basically about 10 years from now. Like, what do you teach people for 10 years from now? Like, how do you prepare them? I was thinking about it for electronics. It's like, I don't know.

**Dave Jones:** I've got a simple answer. You teach them passion.

**Chris Gammell:** That's, yeah.

**Dave Jones:** That's what you teach them. You don't, you know, technical shit doesn't matter. Right. You teach them to be enthusiastic and passionate about what they're doing, love what they're doing, and then they'll be good in 10 years' time, regardless of where the technology goes.

**Chris Gammell:** That's a really good answer, actually. That was my… Thank you very much. That was my favorite answer from the whole bunch of the people. Because they, like, interviewed…

**Dave Jones:** Oh, there was other people who said the same thing? Good. Oh, yeah, yeah, yeah. Good to see.

**Chris Gammell:** Yeah, there was some… And they interviewed a lot of people, and they're all like, oh, well, I'm in the medical field, so I think people should study medicine. Yeah. I'm in the electronics field, so people should study electronics. But the reality is that, you know, who knows in 10 years, you know? But that's a good answer, Dave. I like that. Thank you. I think your kid might turn out okay, you know, aside from all the being raised by you and stuff.

**Dave Jones:** Can I have a little Altium rant again? Again? This kind of just jumped in there, you know? They're always trying to… Come on, let me do it. They're always trying to be 10 years ahead of the market. They're always trying to guess where the market's going to be in 10 years, or it's going to be FPGAs, or it's going to be cloud, it's going to be the Internet of Things, it's going to be this and that. And they try and base their business around that instead of focusing on just the core basic stuff, which will still be around regardless of what happens in the wider field.

**Chris Gammell:** So you're saying to concentrate on the really good… Yeah, and I think that's not just Altium.

**Dave Jones:** Concentrate on the core stuff, which is important, you know? If you're learning electronics, learn your electronic building blocks, you know? They're always going to be the same.

**Chris Gammell:** Yeah, make sure you understand all the law. That's a good starting point.

**Dave Jones:** Exactly. Really? You know, understand basic op-amp configurations, basic transistor configurations, basic components and how they work and how they interact, and everything builds on top of that.

**Chris Gammell:** Right.

**Dave Jones:** So, there are, you know… Yeah, especially when you look at it

**Chris Gammell:** as like a distribution of when you're going to deal with super, you know, like learning about memristors, right? Yeah, exactly. You might learn about memristors, and they might be important 1% of the time, but if 90% of the time you work with op-amps and signals and, you know, DC accuracy like you were talking about, yeah, you should really… You need to know that stuff, right? That's kind of like the…

**Dave Jones:** That's right.

**Chris Gammell:** That's like a musician knowing their scales, right? That's the same kind of thing.

**Dave Jones:** It's bread and butter. Yeah. It's your bread and butter stuff.

**Chris Gammell:** So, you're saying the companies do that too, where they try and… Some companies try and go off too much.

**Dave Jones:** Yeah, companies like Altium try and… Or Altium in the US try and… Yeah, they try and guess where the market is going and try and, you know, and put all their development efforts into what's going to be in 10 years' time at the expense of the present and the expense of those 99%. You know, once again, it should be Occupy Altium. Yeah. And at the expense of the 99%. I think you still got to look a little ahead, though.

**Chris Gammell:** I mean, you got to look two to five years. Oh, yes, you do,

**Dave Jones:** but you don't bet the farm on it.

**Chris Gammell:** No. Yeah, I wouldn't bet the farm. Yeah.

**Dave Jones:** It's ridiculous.

**Chris Gammell:** Yeah.

**Dave Jones:** And likewise, you don't… You know, some university teaching electronics now, if they go and concentrate on the memristor or whatever it is down the track, quantum frigging electronics or something, and you spend half your course learning that shit, and then in 10 years' time, you find, oh, that's, you know, only used 0.001% of the time.

**Chris Gammell:** Yeah.

**Dave Jones:** Every job I've ever been to needs just the basic stuff, then you're screwed.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? Because you spend too much time focusing on that niche stuff that might be the future. Yeah, it's okay to spend, you know, a bit of money, time, and effort on it. Keep it all going. Fully support that, of course.

**Chris Gammell:** But, yeah.

**Dave Jones:** When you… So, it's… The question is obvious. The answer to that question that you asked is what should you teach people now for 10 years' time? It's obvious.

**Chris Gammell:** Passion.

**Dave Jones:** Anyone who says something specific, that's the wrong answer.

**Chris Gammell:** Yeah. Interesting counterpoint to that. There was an article about older engineers in Silicon Valley, in the New York Times, and basically how they can't get… Have they got graybeards? They do have graybeards. Excellent. Some people call them graybeards. But, yeah, they were saying that they can't get jobs either because, you know, they're hardware engineers or, you know, there's too much software around there and it's only, like, younger people getting hired. And there was this really interesting comment, though. They said… They talked to Google and they said their… Google said, we're looking for people… candidates who are passionate and, quote, truly have a desire to change the world. And so, what I'm wondering is, are they trying to say that older engineers are not passionate?

**Dave Jones:** They're crusty and they don't have any passion anymore. It's been beat out of them by Dilbert Land.

**Chris Gammell:** I mean, maybe. That's… I mean, I've seen that before where there's, you know, like, you kind of slow down. Old and bitter, yeah. Yeah. And the question is, I mean, like, are there engineering jobs in this crazy world we live in where, you know, they're stable, quote, unquote? Does that even exist anymore?

**Dave Jones:** Military jobs, yeah. Big military companies, yeah. Yeah. Those stable, quote marks… Stable. Stable jobs in big companies there, yeah, they beat the passion out of you. But some people like that, you know.

**Chris Gammell:** They beat you with specs.

**Dave Jones:** Specs and procedures, yeah. And Gantt charts.

**Chris Gammell:** And using 20-year-old obsolete parts. Yeah, that's interesting. I wonder if certain industries kind of shade more towards that, like, other than military. Because… Congratulations, you've been promoted

**Dave Jones:** to component obsolescence engineer.

**Chris Gammell:** Yeah.

**Dave Jones:** Please go to a new corner. Yeah.

**Chris Gammell:** That's what I used to do.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** Yeah, I don't miss that at all.

**Dave Jones:** No, it's, you know, it's true. And there's jobs… But there's jobs out there for everyone, for all kinds.

**Chris Gammell:** Yeah.

**Dave Jones:** People… And there's nothing wrong with being old and crusty and hating the world. That's fine. If that's who you are… Add some flavor, yeah. …who you want to be, you know, that's… And cynical about everything, that's fine. Yeah. There's a job for you, you know. Yeah. It's… Maybe if you're not getting the job, it's because you're a dick instead.

**Chris Gammell:** Oh. Or you're unemployable like I am now, I think. We decided to go with other candidates because you're a dick.

**Dave Jones:** I think… I think I'm probably unemployable now. Oh, yeah, you totally are. I think I totally am.

**Chris Gammell:** I would have to… All of your shortcomings are now well documented on the web, don't you?

**Dave Jones:** Yeah, yeah. I know. I would so have to ditch everything from my resume, you know.

**Chris Gammell:** I was thinking about that. I put some of my online stuff on my resume finally and I was thinking about it. I'm like, this could go really well or really poorly. Yeah. You know, it's like, yeah.

**Dave Jones:** I've had it go both ways. I've had it go excellent. They go, holy shit, you do all this stuff on the side? We're hiring you. You're the best candidate ever and then I've had others just shake their head and point towards the door. Really?

**Chris Gammell:** Wow.

**Dave Jones:** So, yeah.

**Chris Gammell:** Why do you think that was?

**Dave Jones:** Because they don't like anyone who, you know, with their own opinion or with their own desire to do things their own way. Opinions? No, surely not. And, yeah, all companies are different. Every company has different requirements. Some love that.

**SPEAKER_01:** Yeah.

**Dave Jones:** You know, like Google may love that or something. They may love that passion and excitement but other companies, that's no. You'll get, you know, pointed straight back out the door and don't let the door hit your ass on the way out, sir.

**Chris Gammell:** Yeah. It's interesting because... It's the way it is.

**Dave Jones:** The world's a diverse place.

**Chris Gammell:** Yeah. I mean, like, so on the other end of that, right? So, crusty old guys might not... The ass end of the world, yeah. Right. The old hardware guys might not be able to get hired but there's actually software startups that are so hard up for people, they're training people without any knowledge which is really interesting because, you know, like, I don't... You got an example for this? Yeah, yeah. Living Social that... What's it called? I've heard of that. Yeah, it's like a, you know, it's like a Groupon or Coupon site but, yeah, they took 24 people. They hired them based only on their... I guess it would be like a...

**Dave Jones:** Niceness? Their personality?

**Chris Gammell:** Yeah, you know, it'd be like one of those... What do they call those behavioral interviews? You know, tell me about a time where you had a problem with a co-worker and how you solved it.

**SPEAKER_01:** Oh, God, I hate those. Punch. Oh, you're not wrong.

**Chris Gammell:** Yeah. Yeah. Anyway. So, the worst kind of interviews ever but these people were obviously very bright but just didn't have any programming background so now Living Social, they took them and they were hungry for a job, basically, and they said...

**Dave Jones:** Is this some sort of experiment like public experiment of...

**Chris Gammell:** Yeah.

**Dave Jones:** It is because surely there's no shortage of programmers out there they could have hired.

**Chris Gammell:** Well, but...

**Dave Jones:** Experience. Come on, you can't tell me that there was absolutely no programmers left that they were forced to do this. They're doing this as some sort of experiment, right?

**Chris Gammell:** Social experiment. I don't think so because I think the problem is that they're in Washington, D.C., right? So, if you try and get...

**Dave Jones:** Come on!

**Chris Gammell:** Hey, you try and get people to a part of the country that there are no other jobs, that's a pretty big risk for someone, right?

**Dave Jones:** I get no other jobs. Would you move to...

**Dave Jones:** programming jobs in Washington, D.C. And you would rather have somebody with absolutely no programming background at all

**Chris Gammell:** rather than somebody with just some. I'm sure they're getting a discount for this, but it's a very...

**Dave Jones:** Oh, you think there's government incentives involved here?

**Chris Gammell:** No, I think they're getting a discount because you're not hiring an experienced programmer.

**Dave Jones:** Right, so they're paying them. Right, if you can't

**Chris Gammell:** teach them, train them, right? Or if you can't hire

**Dave Jones:** them, train them. Right, okay.

**Chris Gammell:** Interesting. I think it's a really cool idea. I don't know if it's... I mean, it's a big risk, obviously.

**Dave Jones:** It's not very practical. You've put a lot of resources into training these people.

**Chris Gammell:** Well, you've got to make them sign a contract to stick around, right? And they're very

**Dave Jones:** unproductive for quite a long time.

**Chris Gammell:** Yeah, well, that's a question. I mean, there's been other studies about kids in high school programming. Programming is kind of weird like that, I think. I mean, like hardware, maybe it's the same, but you have to not only work with your hands, but also have the conceptual stuff in your head, so...

**Dave Jones:** There's a theory there that you have to be... You know, the best programmers are the ones who can remember eight-digit numbers or something, and there's a direct correlation there. Some people just aren't cut out to be programmers. Their minds aren't wired that way, regardless of how much you, apparently,

**Chris Gammell:** according to YouTube.

**Dave Jones:** Me, apparently, yeah. Regardless of how much effort you put into it, it's like, you know, I could study chess for the next 50 years of my life, 24 hours a day. I'm still not going to beat Garry Kasparov at chess, right? Because his mind is wired in such a way that I'm just not going to be that good, not even close. I'm sure my mind's not wired that way. So regardless of the amount of training you put into it, some people just can't, aren't going to be good at this stuff.

**Chris Gammell:** Yeah, and maybe that's what you screen for in these applications. I guess... Or you think you're screening for. You think you're screening for, right. I mean, that remains to be seen. But an interesting thing would be the same with hardware. I mean, if you had a group of 100 people from scratch, what do you look for for hardware people? Oh, shit. Willing to burn themselves? How many times have you electrocuted yourself around the house? And how did you feel about doing that?

**Dave Jones:** That's a very interesting question.

**Chris Gammell:** I think so. I think I would go for risk-taking. I mean, not afraid to try stuff. Not afraid of breaking stuff. I think about my own exploits. It's like, you know, the times I was most successful... No fear of looking stupid. Yeah, and retribution from management, right? Sometimes that matters too. Yeah, there's a lot of that. I mean, that's for a lot of industries, but maybe for electronics, I guess, yeah, trying stuff out, reading stuff.

**Dave Jones:** Maybe if somebody walked in and the first thing they said was, I don't give a shit, you're hired!

**Chris Gammell:** The Dave Jones test.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah, I don't give a shit if you sack me or think I'm doing something stupid or my ideas are dumb. So, yeah, maybe that's the attitude you need.

**Chris Gammell:** Yeah, I think that would help for sure. I don't know what else there would be though. I mean, I think about, like, you know, watching people start up from, like, hobbyists and a lot of times it's just willingness to, I think even willingness to copy stuff at the beginning, you know, like, get that effective muscle memory, right? So, knowing that resistor A connects to resistor B, that kind of thing, and not being afraid to even do that, that's a good starting point too. So, I don't know.

**Dave Jones:** I don't think there's one right answer here. You know, there's never one right answer for this stuff. It's so wide open.

**Chris Gammell:** Yeah. I guess you could just put them all in a room with, like, some Legos and see who makes the coolest thing. That's always a good test.

**Dave Jones:** Hey, that's as good as any, right? Yeah, right?

**Chris Gammell:** And plus, at the end, you got a couple cool things, right?

**Dave Jones:** You know, there's somebody, look, I made an elephant. You go, nah, that's pathetic.

**SPEAKER_01:** Oh, boy.

**Chris Gammell:** Yeah. Actually, so there's another thing about, there's actually, not necessarily just for hardware, but there's, I hadn't heard about this, there's a similar program for startups. And, like, a boot camp slash incubator. Have you heard about this? The, I'm going to say this wrong because it's stupid leet speak, but Haxalator? H-A-X-L-A-R-8-R?

**Dave Jones:** No, and it is really bad. Yes, I agree.

**Chris Gammell:** Yeah, that's really bad. But the idea is really cool. Basically, I think it's with Seed Studio, but basically, you go to Shenzhen, and basically, you start a hardware startup. And I was like, whoa, that's awesome. So there's, like, actual applications. I think it's still open. I'm not sure if it's, like, rolling applications, but basically, they are trying to pull in startups, hardware startups, and actually give mentoring and materials and, I think, money even, like, kind of like a Y-Combinator type of thing. And so if you look at the list of mentors, I mean, Brad Feld, who's real big in the investment scene, Mitch Alton's on there. Eric Pan from Seed Studio. So a lot of, like, really familiar names. And these are all available for mentorship and everything else. I don't know. It's a really cool idea, I think. So I don't know if it'll work out, but hey, money and hardware, that doesn't hurt. Who's it open to? Anyone? People with startups. Here we go. Frequently asked questions. So you get up to, oh, that's what you get.

**Dave Jones:** What kind of startups, though?

**Chris Gammell:** Oh, oh, no. Is it like an open source thing? Oh, good thing I mentioned it today. The deadline to apply is January 31st, 2012. So you guys have two days. Assuming it's not Shenzhen time, in which case it's one day. Wow. Should have mentioned this earlier. This has been on the list for a while. And it was just luckily right above. Man, that's...

**Dave Jones:** Some of the shit on our list does expire. Yeah, it does.

**Chris Gammell:** But yeah, here's the things they're looking for. They're looking for consumer devices in either health, fitness, or travel, other things too. Gadgets, consumer electronics in software. Oh, not more gadgets. Eh. Appliances, packaged goods, or just a means to end, basically. And I don't know. I think it's a really cool idea, but obviously people have two days. And so, they're also teamed up with China Accelerator, which is the same kind of thing. And I think that's actually sponsored by the People's Republic of China, I think. Right. Yeah, people should check it out. I mean, in terms of, you know, a cool program that's available, in terms of like, how do you learn to do a startup? I'm guessing you have to have some kind of experience in order to really make it into this program. Right. But I think a really good idea would get you into this program as well. Right. So. Yeah, it's cool. And you got 24 hours or so to apply. Hope you don't listen. Tick, tick, tick. Yeah, if you're listening to Amp Hour on, good thing we didn't record tomorrow, right Dave?

**Dave Jones:** And we've got it at the end of the show, so we've just wasted an hour of your time.

**Chris Gammell:** Yeah, right? 23 hours.

**Dave Jones:** Exactly. Damn, they should have mentioned this at the start. Yeah.

**Chris Gammell:** Oh, man.

**Dave Jones:** Oh, boy. Come on, we've got five minutes left.

**Chris Gammell:** Oh, what else? Maybe we should find other things on the list that might expire soon. Oh, boy.

**Dave Jones:** What to bitch about.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Why not?

**Chris Gammell:** I'm looking, man.

**Dave Jones:** We've done a lot of bitching on today's show.

**Chris Gammell:** Oh, we have, yeah. What else is on here? This makes for great radio. Oh, it's so good. Dave, start singing. Did we get our ham thing?

**Dave Jones:** It's not going to happen.

**Chris Gammell:** I forgot to check in with people.

**Dave Jones:** Not going to happen. Not enough hams.

**Chris Gammell:** Not enough hams. You just said you wouldn't do it anyways.

**Dave Jones:** And not enough care factor from me, so that's...

**Chris Gammell:** To all the people that did get their ham license.

**Speaker ?:** Once again, it's a

**Chris Gammell:** dictatorship, dude. It's not a dictatorship here. It's a two-person dictatorship. I don't know. It's a council.

**Dave Jones:** What I do is my own dictatorship. Oh, yeah. I can assure you.

**Chris Gammell:** Yeah.

**Dave Jones:** Nobody else gets a saying it.

**Chris Gammell:** something over your head. There we go.

**Dave Jones:** Oh, boy.

**Chris Gammell:** Yeah.

**Dave Jones:** Hey, we were talking before the show about my MakerBot, right, which I still haven't built yet, but every day I go into the lab, I can smell that burnt wood.

**Chris Gammell:** Yes. Right? Yeah, because it's laser-cut wood.

**Dave Jones:** Because it's the laser-cut wood, and I can smell it, and it is really quite strong, and are there any dangers of this? Are there people dropping dead in the MakerBot factory? Or are they going to drop dead in 20 years' time, you know, because it's all carcinogenic because of all this burnt wood?

**Chris Gammell:** Mesothelioma, something like that. Yeah, gesundheit. That's like the asbestos disease. Oh, right. Mesothelioma. There's commercials for it all the time around here because all the lawyers want to help sue whoever.

**Dave Jones:** Oh, okay, want to sue? Sue! Sue! Yeah, exactly. Can we link in the Weird Al Yankovic clip? I'm going to sue you! I'm going to sue you!

**Chris Gammell:** What was that a play on? What song?

**Dave Jones:** Oh, I know. I don't care what song it plays on. I just love his songs for the fact that they're just cool in their own right, not that they're playing on someone else's song. Oh, I know.

**Chris Gammell:** It's easier because you were just singing.

**Dave Jones:** Most of them are obscure songs I've never heard of anyway. Oh, okay.

**Chris Gammell:** Gotcha. Yeah, because you listen to mostly nerdcore. Yeah, I'm a lot of it, yeah. Right.

**Dave Jones:** And, yeah, is it a problem? Does anyone know?

**Chris Gammell:** I hadn't heard of it. Let us know. I had never heard of it, but I mean, there are a lot of kids out there that are doing that kind of laser cut wood thing, so.

**Dave Jones:** Yeah.

**Chris Gammell:** I know that all the laser cutters definitely have really good ventilation on them.

**Dave Jones:** Yeah, good ventilation, so when it's happening. But are there any after effects from the, you know, I'm sure when it's the act of burning, yes, I'm sure it's very bad stuff and you wouldn't want to be breathing that shit in. But afterwards, I don't know, if I can smell it, then, well, you know, I mean, there's something in it, right?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** So it's given off something. And if you know how to get rid of it, can I seal the edges? Can I lacquer the edges? And that will sort of seal in the goodness. You know?

**Chris Gammell:** Yeah.

**Dave Jones:** Seal in that oil, sealing all that carcinogenic goodness.

**Chris Gammell:** You can just spray paint the whole thing, right? Yeah. I guess you'd have to take it back. You take it apart yet? You didn't even build it yet, I thought. No, I haven't even built it yet. Yeah, but it looks cool, right? Yeah. No, it looks cool. Yeah, you have the first pink maker bod.

**Speaker ?:** Oh, yeah.

**Dave Jones:** Great. That's all I need. Yep. Oh, boy.

**Chris Gammell:** So I have one last thing. It's actually a fun thing I found on Reddit. And a lot of people were excited about it on there, too. That's an endless source of amusement for you, Reddit. Oh, I love it. Hey, man, that's how we met. We got to give it some shout outs, you know? But yeah, there was a great post, basically. Agilent is giving away free posters. So if people have a lot of room on their walls.

**Dave Jones:** Spare no expense.

**Chris Gammell:** What do you mean? Free posters? Posters. Oh, yeah.

**Dave Jones:** Free posters. Hey, they're cool looking. I thought you were about to say giving away free oscilloscopes or something. Oh, yeah, right. And then the ears prick up and, you know, giving away posters. Yeah, but they're giving away good, I don't know,

**Chris Gammell:** these are good stuff. So like they got like a RF transmitter and receiver, kind of like the whole chain. And obviously they're trying to get you on their list of people.

**Dave Jones:** So the informational posters.

**Chris Gammell:** Yeah. Oh, yeah, yeah, yeah. So like how, you know, a DMM works or how an RF transmitter works, that kind of stuff. And it's for education. But it's cool, you know, if you've got room in your lab and you want to hang stuff up, you can give them a shout and they'll send you a poster for free, I think. So I think I think the cost of admission here is your email.

**Dave Jones:** Yes, to be sucked into the funnel. And obviously you have to be U.S. based as well because nobody exists outside the U.S., I'm sure.

**Chris Gammell:** Yeah, there was something about that. There's a certain country. I know Brazil didn't. They wouldn't ship to Brazil for some reason, but.

**Dave Jones:** Oh, yeah. Those pesky Brazilians.

**Chris Gammell:** Yeah, I guess so. So. But yeah, nice looking poster. So if you if you want some of that, you know.

**Dave Jones:** Want some of that poster action?

**Chris Gammell:** Poster action.

**Dave Jones:** Get on there. Milk them for all they're worth.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** That postage has probably cost the most.

**Dave Jones:** And if you've got your own domain name, you've got infinite email addresses, can you get an infinite number of posters and send

**Chris Gammell:** an agilent broke? It's weird. Dave Jones 1 through 37. They all seem to be going to the same address.

**SPEAKER_01:** Oh, boy.

**Chris Gammell:** Yeah. So I should mention for next week, I'm not going to be here.

**Dave Jones:** Oh, yes. That's right. Yes. Yeah. Yes. Enjoy your honeymoon.

**Chris Gammell:** Yes. I'm going to my honeymoon. Actually, next two weeks, I probably won't be here. So I think I'll be real jet lagged on the second week back. But we do, as people always like when Jeff is on the show and Jeff has agreed to help us out.

**Dave Jones:** Oh, he has agreed, has he? Yes, he has. Yeah. You actually asked him instead of just assuming he'll turn up. Yeah. Call on the day of. Hey, Jeff, what you doing, buddy?

**Chris Gammell:** Yeah. Yeah. So next week, Jeff will be on. I will. Can you say where you're going to? I'm going to Hawaii. So I will be halfway between here and Dave, basically.

**Dave Jones:** You always do things by halves. You never finish.

**Chris Gammell:** That's your problem. Yeah, that's true. But why would I want to go see you on my honeymoon? True. Yeah. I did look at Australia. Australia's cool. It is. Yeah. But I looked at it, but it was a little too pricey. So, yeah.

**Dave Jones:** And I did. Then I sort of tried to argue with you. No, you should make the effort to come to Australia. Then I realized, no, you're almost on the other side of the US. So you can't. It's not like you're on the West Coast where you can just fly out and, you know, it's only a 12, 13, 14 hour flight or something. Only. Yeah. I think it's like. Yeah, you've got to do like another eight hours, don't you, on top of that.

**Chris Gammell:** You really don't know geography, do you? I don't either. But yeah, it's like it'd probably be about 15 hours from Chicago to Australia.

**Dave Jones:** Right. Yeah. Okay.

**Chris Gammell:** But yeah, someday, man.

**Dave Jones:** No, but you'd have to do it. Well, no, it's 14 hours. You said 14 to Dallas. From Sydney to LA.

**Chris Gammell:** Oh, I thought you said 14 to Dallas, but okay.

**Dave Jones:** Well, yes, it's 14 or 14 and a half to Dallas. That's as long as the planes can fly. Okay. So then you're actually sucking on fumes as you're landing. Yeah.

**Chris Gammell:** Yeah. There'd be another two hours on top of that. But I'm sure I'll get out to Australia someday. We're going to try and get, you know, we'll see if we get some sponsors someday to, you know, send me out there or Dave over here. Maybe one day me and Dave will actually shake hands. You never know.

**Dave Jones:** And the world implodes. Yeah. Oh, boy. That'd be good. So which islands are you going to? I know we're over time, but I'm just interested in your holiday. I'm taking personal interest in life here. Look at this. We're like almost friends, Dave.

**Chris Gammell:** We're not just co-hosts. We're almost friends, buddy. I'm going to Maui and Kauai. And then I, Oahu is the big island, the main island where Honolulu Airport is. So I'll spend a day there too.

**Dave Jones:** But that's not the big island.

**Chris Gammell:** No, not the big island.

**Dave Jones:** So you're not actually going to the big island?

**Chris Gammell:** No, no.

**Dave Jones:** Oh, man. That's the best. Yeah. Volcanoes. Meh. Oh, I think it's active at the moment.

**Chris Gammell:** I think it is. Yeah.

**Dave Jones:** Another reason not to go there.

**Chris Gammell:** Another reason not to go there.

**Dave Jones:** No. It's awesome. Live a little.

**Chris Gammell:** I will. On a beach. With a drink in my hand.

**Dave Jones:** Why? There's no beaches in Cleveland?

**Chris Gammell:** There are, actually, but they're frozen over right now.

**Dave Jones:** Oh, okay. Well, I'll just go sit there anyway. Lay a towel down and save your money.

**Chris Gammell:** Yeah, that's right. I could. I could. Nice half-hour drive up to the beach.

**Dave Jones:** Awesome work.

**Chris Gammell:** All right, guys. Well, I will talk to you in three weeks, and I'm sure Dave will be back next week, unless he forgets.

**Dave Jones:** Yeah, I've got nothing better to do.

**Chris Gammell:** All right.

**Dave Jones:** I'll be here. Catch you later.

**Chris Gammell:** See you.

**Speaker ?:** Bye. Bye. ! Bye. administered administered administered
