---
episode: 460
title: Rubber Ducking
url: https://theamphour.com/460-rubber-ducking/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released September 29th, 2019. Episode 460. Rubber Ducking.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Flat out like a lizard drinking.

**Chris Gammell:** That's right, yeah. Lizard drinking, huh? Never heard that one.

**Dave Jones:** Oh, you haven't heard flat out like a lizard drinking? No. No, it's an Aussie term. There you go. You've heard it now.

**Chris Gammell:** Yeah, I have, yeah. Yeah, we're both flat out as usual. Yeah, a little busy. Yeah, a little busy. But no, it's good, man. So, you know, I have a consulting forum where I talk to people about this, and it's better to be busy than not busy, of course. Right, of course. You know, well, with the caveat that like some people are kind of like further along in their careers and they're like, yeah, I actually bill for jobs now instead of hourly. So it's not as like tied to hours. But like when you're billing hourly, like I do, it's, yeah. Busyness is kind of means making money.

**Dave Jones:** Bill every spare minute. If you're at the gym, it's going, oh, geez, no, I'm losing money. Yeah, yeah, yeah.

**Chris Gammell:** I mean, August, it was tough for me to like go places in August or like take vacation. It's a little, it stresses you out a little bit. But I've been trying to think of everything as an investment, right? So like when I'm doing my code learning stuff that I'm working on, that's an investment in the future. When I'm on vacation, it's an investment in mental health. Mental health, yeah. When I go to the gym, it's an investment in regular health. When I walk the, and like, honestly, there's, oh, what was I reading? Oh, I just finished Art in the Motors.

**Dave Jones:** Oh, of course, he's finished another book, folks. It's bingo. It only took like a minute, two minutes. And he's already mentioned another book. Yep.

**Chris Gammell:** Yeah, well, I just finished then in the Art of Motorcycle Maintenance. Of course, yeah. Have you ever read that one?

**Dave Jones:** Oh, I did. Yeah, I've read it all the time. Yeah. I've read it 10 times. Yeah. Yeah.

**Chris Gammell:** And so he just talks about the importance of getting out and like, you know, walking and stretching your brain out without actually thinking about things. And, you know, that's like an investment too. So like going for a walk with a dog is obviously, you know, time spent with out in the air and getting fresh air, but also times to crunch on things instead of think about work.

**Dave Jones:** So trying to justify being a lazy ass. Yep. Yeah.

**Chris Gammell:** Yeah, exactly. Exactly. It's fine. What'd you think of that book? I didn't know you've read it.

**Dave Jones:** That's magnificent. Yeah. Life altering, you know. Yeah.

**Chris Gammell:** It was much more heady than I thought it would be, but. Right. Yeah.

**Dave Jones:** It was good. It was good. He's finest work to date.

**Chris Gammell:** That's right. That's right.

**Dave Jones:** Oh, goodness. Anyway. All right.

**Chris Gammell:** Well. What's happened? What's happened? Yeah. Working on some boards. I got my, I'm doing embedded programming. That's new. Not new, new, but I've been working on like actually using GDB. Have you ever done that?

**Dave Jones:** GDB? What's GDB?

**Chris Gammell:** So it's like the, it's the command line debugger for just like Linux in general, like GNU debugger, I think is the GDB.

**Dave Jones:** No, I don't use Linux, so.

**Chris Gammell:** Okay. Well, it's also used as like the backend for a lot of, a lot of like GCC code, right? So. Right. So if you're, if you're like using an IDE, and I'm learning all this stuff too, so take it, take it easy on me if that's, if I'm getting this wrong audience. Uh, but like, if you're using like a, uh, eclipse, right. Oftentimes what it's doing is basically, it's like a generic front end, you know, you have your code window and then you have your variables and you have like your, you know, stepping through code and all this other stuff often, not oftentimes, but sometimes the eclipse window is actually built and it's just sending commands to this backend, which is like GDB. And it's basically saying, Hey, I want to do a breakpoint at main. And it's, so you do like breakpoint main.c and, or sorry, uh, uh, breakpoint main in main.c, right? So that would be like the main function in the main.c file. Got it. And then when you get there, you know, it does a breakpoint like everybody's used to, but it's actually on the backend. And you can just go and manipulate that directly, uh, using something called GDB. And, um, I finally figured out like a lot of the, you know, like I always get really confused whenever I was doing deep debugging of things. Um, but I've had some great tutors so far and that has been very helpful. And, uh, and I've kind of got a better feel for like what it is and, and how things hook together and, you know, like a GDB server runs on the device that you're debugging normally or debugging with. So like a J link would have a GDB server and then GDB on your computer would actually hook into that. So it's like a server client kind of model.

**Dave Jones:** Got it. And that's allowed you to debug what?

**Chris Gammell:** Uh, so debug some, some programs that I'm writing, just like simple, simple blinky stuff, time timers, interrupts.

**Dave Jones:** Uh, see, why do you have to debug blinky, timey, simple stuff? Why do you have to use it? Because it wasn't working, Dave. Because it wasn't working. Why? It wasn't working. Like what was the, give us the, the end, the end result.

**Chris Gammell:** Yeah. So the, the, one of the problems that I chased down was just that I, um, you know, so a lot of, you know, and like, especially coming from like the Arduino world and stuff like that, right. A lot of people come in, I was doing that for a long time as well. And, um, and so like when I was, uh, setting up a timer, right. So a lot of like what you look at in, so I'm using STM 32, right. So that F zero three zero family. And, um, and when you're using a timer, what you're really doing is you're kind of like setting all the variables. It's really just like setting switches in the registers that are there. Right. So if you're like, Oh, I want this, I want this to have a prescaler of, so it's like a 48 megahertz clock. I say the prescaler is 48, 48,000. And then I get up like a one millisecond increment basically. And then I say, Hey, count to a thousand. And the timer hardware. Yeah.

**Dave Jones:** Timer hardware actually does the rest.

**Chris Gammell:** Uh, it mostly, but, but if you don't have everything set properly.

**Dave Jones:** Oh, of course it's got to be set.

**Chris Gammell:** Yeah. Well, that's what it was wrong. Uh, so it turned out I, uh, you know, you know, like the thrashing stage of even, you know, like, I don't know if you ever thrash like I do, not like I'm like a, into metal or anything, but like I thrash, like, uh, I like try a bunch of things. It's not very scientific. Speaking of art, art of, art of motorcycle maintenance. Right. Uh, he talks about the scientific method. I was not following that. Uh, and you know, so I like, I tried a couple of things and it didn't really have any effect cause it was, it was still quote unquote broken. Right. And so I tried these things and like, it had the same output, but the thing was, I actually was changing something that did have an impact, but I, because I was like, I was like, cause nothing was working. Uh, I, I then later paid the price for it. So, um, so basically what happened was I, I set like a repeat timer or a repeater or something like that. So basically I said, Hey, count to a thousand with these millisecond increments. So I thought it was going to be a one millisecond timer, but it turned out, no, actually I said it's a repeat a thousand times. So it was only going to throw an interrupt every thousand seconds and I couldn't figure out why. Uh, and, and then, yeah. So I set a break point inside the, the interrupt function and, uh, and then I saw, Hey, once in a while it does actually trigger. And, uh, so that, um, so I figured out that something was wrong there. Then I just kind of like went back through and read the data sheet again or the user manual and, and then, uh, then it worked.

**Dave Jones:** See, I don't bother, like, unless I'm absolutely desperate, then I'll get out the debugger. But, uh, but before that I'll just use a, uh, print F, you know, to serial or I'll use a lead, you know, actually flash a lead on the, on the product or whatever. Yeah. That makes a lot of sense. Oh, okay. Obviously if, if it flashed that lead, it got into that interrupt routine. Cause yeah, I just add a line of code. That's right.

**Chris Gammell:** Yeah.

**Dave Jones:** Here flash lead, you know, like, right, right.

**Chris Gammell:** But the output of my program was to flash a lead in the interrupt routine. So it, uh, it didn't go so well. Um, yeah. So, you know, so like a lot of this stuff makes sense, but like, it's been nice to kind of just go through it again and spend some time. Like, and like I'm going slow, man, I'm going real slow. Um, but it's, uh, it's nice. It's nice to get a better feel. And the other nice thing about it is that in the meantime, I actually listened to, uh, Jay Carlson who wrote the $1, the amazing $1 microcontroller. He was back on embedded last week and, um, hi. Bingo. Book number two. That's not, no, no, no. That's a, that's a podcast, Dave.

**Dave Jones:** Oh, podcast. Right. Okay. You said wrote.

**Chris Gammell:** Oh, so he wrote a blog post. Yeah. You've read that blog post. We went over on the show, right? So remember it was like comparing like a bunch of low cost micros. Oh yes. Right. Yeah. Yeah. Of course. So that's a great blog post. And if people haven't seen that, I'll link back to him. That's fantastic. Um, but he was back on the show talking about education and embedded, um, education. And so like it just, between him and Tom on the show last week and then reading the Zen and the Art of Motorcycle Maintenance, I had like a religious experience about like education and, you know, I'm just like, I like, I freaked out last week about stuff. It was great. Like in the best way. Like you hippie. I know. Right. And, uh, but in the show, he's talking about a tolic, which is like a, I didn't realize it was an ID company. I never heard of them, but they got bought by ST. And so I tried that out and, you know, it's basically just a eclipse based IDE. Uh, but now that I've been digging under the hood with the other stuff I've been doing, it was like a lot easier, not easier, but it was like a lot clearer. And like, I'm not as scared of the menus now because they're, you know, you've gone through eclipse before, right? It's just menu after menu after menu. And, um, and so I just had a little context on what's going on there and that really helped a lot. So, uh, yeah. Taking my time and digging through some of the, the scarier stuff, quote unquote, but you know, it's been, it's been really helpful for, for getting a grasp on what I should be doing.

**Dave Jones:** Have you ever been so up to your eyeballs, tits up in, in the code and in the compiler and debugging that you couldn't see the forest for the trees?

**Chris Gammell:** Oh, um, I don't, I don't think I've gotten to that point yet, so I'm sure I will, but you have a story about this, I'm sure, right?

**Dave Jones:** I got a classic example. It's not me. It's, uh, David, the other David. Yep. And, uh, it's, it, it was quite public. It was on, uh, it was on my second EV log two channel and he, he often does, uh, he posts these, you know, infrequent, um, updates when he's, you know, working on something on, on the micro supply of course. So it's an STM 32 based, uh, platform with, with the GCC compiler and all the rest. And, and, uh, previously he's done a, uh, he's, he's found a bug in the GCC compiler, right? And he's had that confirmed with the GCC people and he had to wait. Our project was delayed by a couple of weeks until the GCC people could fix it, could actually fix his bug. Right. So, you know, he's, uh, you know, that's how good he is. He finds bugs in compilers. Right. And, uh, so he, so he messaged me the other day, I've been working on this problem and I think I've found another bug in the GCC compiler and it looks like it's really basic. And he was, you know, like he, he tried to explain it to me because I know Jack all about, you know, GCC compilers and, you know, like the inner workings. Sure.

**Chris Gammell:** Sure. Like how it's creating, how it's creating assembly and then, yeah. Yep.

**Dave Jones:** Yeah. Because he's always doing like obscure CC, C plus plus stuff. Right. He's always pushing the boundaries of the compiler. Right. Me, my, my code's just dumb ass. Right. So that's why it always works. Right. Same. I'll never find, yeah. I'll, I'll never find a bug in a, in a C compiler. Right. Right. I don't, don't think I have.

**Chris Gammell:** Hmm.

**Dave Jones:** Anyway, um, might've actually, but anyway, yeah. Not lately. How about that? How about that? Yeah. Not, not lately. His code is more likely to find it than mine. Let's put it that way. And, uh, so, you know, he tried to explain to me and like, and it sounded really basic. And I went, dude, are you sure? Like it can't be this, this is GCC. It's used by millions. Right. Right. And it's like, it can't be this basic. And he, and, but he assured me, yes, it is. You know? And I went, okay, you know, you, you were right last time and do it. So I, I told him to do a video about it. So he did this video and I couldn't make heads or tails of it. It was, you know, it was, uh, he was jumping into routines and it was using voids and, um, it was using, um, uh, statics and all sorts of, you know, um, stuff like that. Mm-hmm. Anyway. Um, and as soon as he released the video, then all the comments started popping up. No, dude, you're using, you're, you're, you're doing it wrong. You're doing a fundamental error. Oh man. The, you, you cannot, you, if you're, if you're in an interrupt routine, you must use statics. I think it is. Um, is it, oh God. Volatile? No, volatile. You must use volatiles inside interrupt routines. Sorry. Yeah. Inside interrupt routines, you must use volatiles. And that's what he wasn't doing.

**Chris Gammell:** Yeah.

**Dave Jones:** And it's like, and it's like, if I remember back to my rusty past, even I knew that. Uh, so it's like, yeah, I've, I've been caught with that before. Uh, way, way back. Yeah.

**Chris Gammell:** That's the tough thing. I think it's, it's nice to have that feedback, but it's tough to like hear it over and over. It's like, okay, I get it. Yeah.

**Dave Jones:** Oh my, I get it. So he had to go, oh God. So he had to do this massive face palm and you know, shit, like shit happens. It was so deep in the, in debugging this compiler that he, and, and doing all this weird stuff to try and work out what's going on. And, and he spent ages on this and then, yeah, it was something as simple as he wasn't using a volatile type inside an interrupt routine.

**Chris Gammell:** I feel like for me, that's like, so like, I know I've been pumping the idea of tutoring lately, but like literally it could be any like, so like when I figured out that other, the problem that I was having was actually just explaining it to my friend. He was like watching over my shoulder and that, you know, that's called like rubber ducking, right? Uh, I'm sure. Rubber ducking? We've never talked about that on the show before? No, I've never heard of rubber ducking. I've heard of that. I've, I've.

**Dave Jones:** Sounds like a bizarre sexual position.

**Chris Gammell:** Uh, no, the idea is that basically you just need someone to talk to and talk through your problem with. And the, and the, the term comes from, you could just as easily be explaining it to a rubber duck. I think that's how it goes. And the idea being that like walking, walking through it and explaining it, like you, sometimes you just go, Oh, wait a second.

**Dave Jones:** Oh, and the penny drops. Exactly. Yeah. You could be, you could talk to someone who knows nothing about it. Exactly. You could be talking to your mom or something.

**Chris Gammell:** Exactly.

**Dave Jones:** You just need someone to. Yeah.

**Chris Gammell:** You just, you really, you just need to be talking it out loud and just triggering different parts of your brain. Cause if you're stuck inside your head, you're, you're, you're, you know, it's, you're, you just keep doing the same things. And, um, yeah. Yeah. And, and, you know, like, and I, between like rubber ducking, that helps a lot. But then, you know, I think other things that help are like keeping notebooks and then like being able to go back over your books and stuff like that.

**Dave Jones:** Well, yeah. Oh, your segue in, but I have to mention this. Um, yeah. David, David was so upset by this. He's gone and written a whole flow charty process thing about how he's never going to make this mistake again. And he wants to actually do this live. Oh, no, no. Next time it'll be different. You know? Yeah. It's something else. I mean, this is, yeah. This is classic. Anyway. Yeah. So he, yeah, he went, he went and solved to ensure that never happens again. And he's going to do a live. If he wants to do a live show where he explains this to people. We'll do it live. That's great. I, I, I want it. Why do you want to do it? Like, are you sure you want to do it live? Oh yeah. I have to do it live. Oh God.

**Chris Gammell:** Okay. Let the, let the kid, let the kid learn. Yep. Teach your children.

**Dave Jones:** Well, let them lead the way. Show them all. No. Yeah.

**Chris Gammell:** Right. Anyway. You're calling me a hippie. Come on, man. You're calling me a hippie.

**Speaker ?:** Right.

**Dave Jones:** You obviously got a segue. Of course I was. Of course I was.

**Chris Gammell:** Dave, after nine years, we know how to do this. Come on.

**Dave Jones:** Yep.

**Chris Gammell:** Anyways, I, I actually, I, I was thinking we were talking about that notebook. We'll talk about here in a second, but I have been trying to keep better notebooks and I've been doing sequential as well. And I know Alicia from Embedded talks about this and I think we probably talked about it on the show, but.

**Dave Jones:** Sequential is in a daily. Yeah.

**Chris Gammell:** Like I keep a daily, but now I keep a daily logbook on the project too. And that's been helpful. Oh, okay. I used to do it.

**Dave Jones:** Every, every new project, you start a new project.

**Chris Gammell:** Yeah. But it's all, it's all digital. So for me, it's Evernote, but it doesn't have.

**Dave Jones:** The newfangled digital.

**Chris Gammell:** I mean, it's nice. I, I, I think it, well, as we'll look at here, I think it's tough to read this person's handwriting, but, uh, but like the digital stuff too, it's searchable and you know, it's just, especially because the reason I'm really doing it, not really doing it, but another, another benefit of it too, is that like, you know, I, I have these short notes that when I, um, put, when I charge hours, you know, so I charge hours, I say, Hey, like I did a board design here today and you know, here's the, here's the Git revision of the, um, the number of the Git, Git commit and stuff like that. If I, if I do that. Um, but sometimes just having more color to it's nice too. And that's what the notebooks act as. So that helps a lot.

**Dave Jones:** So what, uh, software do you use?

**Chris Gammell:** I use Evernote for mine. I mean, just for simple. Okay. Yeah. And I finally found a Linux client. Oh, thank goodness. There's a Linux client that actually has like a localized database. So like I was on a plane and previously I've been using the web thing and it didn't, it didn't work. And it's like the one time that I actually need it on a plane. So, yeah. But you know, any of it at one note works and, uh, you know, Google keep and there's a, there's a ton of them out there. So yeah, whatever works. Uh, but we were going to talk about this. This just popped up on Twitter earlier today. Um, Jason, oh, I forget his last name who runs archive.org had posted about it and I thought it was pretty interesting. So it's, it's, um, from it's, it's in archive.org and it's Joe. Uh, to cure. Yeah. To cure. That sounds right. D E C U I R. Who's one of the engineers at Atari. So he worked on that Atari 400 and 800 and they scanned in these notebooks and from 1978. And it's super cool to kind of like get a peek back into like, like process. And you were saying you, you knew one of the companies that was like listed in there.

**Dave Jones:** Yes. Yes, I did. I was just scanning through before the show and if you flick through to page four, it's got, uh, that they're having a meeting with the Grass Valley. Well, it just says meeting with Grass Valley. And, and to me, Grass Valley is the Grass Valley group, which is a, um, a famous engineering company in Grass Valley. I can't remember which state it is in the U S. It's in the U S. Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And when I was dealing with them in the nineties at my first job, um, they, they were like one of the world leaders in video switching video, uh, you know, uh, uh, the security market. Cause the company I worked for was in this, was in the security market, the video switching, you know, surveillance type market. And Grass Valley group made these, um, they all make like, they make these big industrial, you know, everything's a rack mount thing and it's got these giant boards. And it's got, you know, hundreds of chips on each board and really over engineered kind of stuff.

**Chris Gammell:** And, uh, price to match this time, you know, this might've, it might've been, you know,

**Dave Jones:** so yeah, I don't know what they were working on back then. Anyway, the Grass Valley group. Um, yes. So there you go. They had an interview with them and, uh, but you know, that's just not a discussion between frequency multiplexing digital analog. Okay. So they're talking about talking with the Grass Valley group cause they were use smart cassette. They're talking about the audio cassette interface and stuff like that. Um, so. Yeah.

**Chris Gammell:** And this is for the computers too, right? So I think Atari and I think of the video game. That's like the, this is for the actual eight bit computer system. And so running on 65 O2s and we've had Chuck Pell on the show before. And people should go listen to that episode because Chuck's amazing. Uh, he's the designer of the.

**Dave Jones:** Yep. The 65. It's absolutely fantastic episode. Yep. Yeah. Gold.

**Chris Gammell:** Yeah. We should catch up with him. I don't know what he's doing these days. He was still, he's still, you know, doing engineering stuff. Last we talked to him.

**Dave Jones:** How old is he? Like he's in his eighties. He was in his eighties. He's still sharp as a tack. Yeah.

**Chris Gammell:** Yeah. He really was.

**Dave Jones:** And he was just, oh wow. He was still like doing stuff. Like his work schedule was like bigger than now and bigger than yours. Yeah. Right.

**Chris Gammell:** Right. He was doing a lot of stuff. He's, he's not slowing down. Amazing.

**Dave Jones:** No. He's still consulting for all these companies and yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** So.

**Dave Jones:** And oh, oh, oh, okay. They merged with Tektronix in 1974.

**Chris Gammell:** Who did? Atari did? The Grass Valley Group. Oh, oh, oh, oh.

**Dave Jones:** Grass Valley Group. Oh, okay. I didn't know that a division of, now I do recall. Yeah. Okay. A division of Tektronix. Huh.

**Chris Gammell:** They're not still around, are they? They're not like a brand, are they?

**Dave Jones:** Video and network divisions. They're still around.

**Chris Gammell:** Huh.

**Dave Jones:** Crazy. By the looks of it. Crazy. Yeah. Anyway. Yep. Yeah. I was right. Yeah. No. Video editing, video capture, all that sort of jazz. Yep. That's what they were working on.

**Chris Gammell:** Cool. Cool.

**Dave Jones:** Yep. Same sort of stuff. So anyway, they were just like, you know, one of the go-to engineering groups as well. Like they would help you design your own stuff as well. They were just like a, you know, a bunch of smart people and yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So anyway, this is great. And you flick through it. Like some of it makes absolutely no sense. You really need the author to be here. Right. Right. This is the jog of his memory, right? Yeah. Yeah. Exactly. Yeah. And, but, but then you go into like, um, say page, um.

**Chris Gammell:** I can't read any of this handwriting, by the way. This is like.

**Dave Jones:** No? Okay.

**Chris Gammell:** This is, this is pretty tough for me.

**Dave Jones:** I can really. I can read it.

**Chris Gammell:** I mean, go to like page, I'm on page like. I can read it. Like 40 or 30, uh, 37. And like, I don't know, just this kind of handwriting is.

**Dave Jones:** Really?

**Chris Gammell:** Used for anything. I guess. Yeah. I guess maybe if I like really squint at it.

**Dave Jones:** I haven't written much in this notebook for a while. Instead working on vellums. Vellums. Vellums. Vellums. Which is, uh, film. Which is vellum film.

**Chris Gammell:** Oh, so like doing circuit board layout or something?

**Dave Jones:** Yeah. Something like that. Yeah. Yeah. Yeah. Changes to document. Proposed changes. You can't read this? I can mostly read this. I guess I can.

**Chris Gammell:** Yeah. I can. Yeah. It's just, it's just like all of the letters aren't closed at the bottom.

**Dave Jones:** Right. Okay. Right.

**Chris Gammell:** I mean, you used to do. So I never really did engineering notebooks. I mean, we've talked about the show before, I think.

**Dave Jones:** I've done. I used to keep them personally. Yeah. When I was working on my own projects and I've shown them in one of my videos. Maybe we can link that in. Yeah. Um, I'm going to show another one soon. Cause I want to do a video, um, where that could be handy. And, uh, and a bit like, you know, he's working on a fuse maps for, um, for, uh, PLD devices, like a, you know, a 10 V 20 or something like, like a gal and a pal. So he's doing like fuse maps for these by the looks of it. Um, so yeah, that's, that's great. Yeah. I just love it.

**Chris Gammell:** It's cool to see, but yeah, it is a little, I don't know, like, uh, I know the way they're kept. Like a lot of times it's for patents and stuff. Like that was always the thing that we learned in school.

**Dave Jones:** That was always the thing for our company. It's like, you must sign and date each page because it's.

**Chris Gammell:** Which has changed since the first, first to file versus first to discovery, which was a couple of years, at least in the States that changed a couple of years ago. But, um, but I think they still want the documentation and stuff like that. So I'm not sure. I'd love to hear from people that are listening. Like, I don't know what the, uh, you know, the modern day version of this is. Like if there are online versions or if you have to still take paper notes.

**Dave Jones:** Yeah, please. If you're working at a big engineering organization, are you still using the printed?

**Chris Gammell:** Like the ones that are most motivated by like the, the patenting process, I'm sure have something in place, but I don't know what that would, I can imagine like a GitHub or a, you know, like a code repository at least is, is easy to, you know, timestamp and, and check all that stuff. But, uh, but yeah, it's, it's tough to tough with like more visual things. Like I wouldn't want to have to like take, you know, you can just take pictures or something like that, but yeah. So, yeah.

**Dave Jones:** Well, that was the thing. Like back in the day, like digital cameras weren't a thing. Right. Like taking pictures. What's it like? So, you know, very occasionally you might have a Polaroid camera. Right. You take a photo and you'd literally sticky tape it into your book. Exactly.

**Chris Gammell:** It's like, well, I'm going to take a photo of the book. I'm just going to put it back in the book. Recursion.

**Dave Jones:** And, uh, anyway, this is, yeah, this is, it's just great to look at these. Yeah. Old stuff. So yes, somebody handed these in. And, and of course we're talking about this before the show is that the books that we've engineering books, we've done it company. They're still there. Like it's part of the handover process. When you leave the company, it's like hand over your credit card, hand over your keys, hand over your swipe card, hand over your notebook. Yep. You know, that's kind of, yeah. Yeah.

**Chris Gammell:** It's part of the IP process and everything else. Yeah. Those are, most of the time they're, they're slowly rotting. They're turning into mushrooms, you know.

**Dave Jones:** Have you ever had to go back to like somebody's notebook?

**Chris Gammell:** I, yeah. I mean, of course. Really? Well, I was doing, uh, at Keithley, I was doing, um, release product stuff. So I was, I was trying to transcribe notes from people who had designed the things 20 years earlier. Right. You know, and many times they weren't there. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** The most of it.

**Dave Jones:** And the, what, they were just lost from the archive or what?

**Chris Gammell:** No, no. The books were there. The people weren't. The people had moved on to other companies, you know. Got it. Yeah. Yeah. And so you go and look at like a book about, you know, someone's, and like, that's the other thing. Like it's, this is, I guess this is kind of like the difference between like saying like, oh, well, I, I document things in code, in my comments and code versus like actually writing documentation. Like even have, like at least the codes there that, that helps a little bit, but like, um, you know, having, having documentation about how it's supposed to work and like, and like having that final, that final piece of like, here is the best case scenario instead of here's all the fiddly bits that I thought might've been the right path towards the end product. It's not as useful. You know, the end product is what you're trying to, you're trying to fix. You're trying to, uh, maintain over time. You don't care about how they got there. You just care about the thing at the end, unless there's something very critical that, you know, that's how they got there. That's, there's like some formula that was never published about, about how they found that resistor value.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** So, yeah, I've had to do it. Have you ever had to do it?

**Dave Jones:** I don't recall. That's why I asked because I, I, off the top of my head, I don't, I, I can't recall an incident where I've had to go back to someone's notebook. Maybe it happened and it just wasn't noteworthy to put into my brain, but, uh, yeah.

**Chris Gammell:** I mean, it's one of those things where it's, it's, it's a tough thing to do. And like, this was the only option 20 years ago. Right. I mean, that was just like, yeah, you're going to keep paper, not even 20 more years ago, but you know, like it was just the practical cost-effective option to do this kind of thing. So it makes sense. Um, right. But yeah, it's not, not easily searchable or any of the things that I said about Evernote earlier. Yeah.

**Dave Jones:** If you go to page 96, it's called the Gallup study of personal computers where they're actually, um, evaluating the different computers on the market and stuff like that.

**Chris Gammell:** Gallup, like the polling.

**Dave Jones:** I don't know. Maybe they did get Gallup to do a, I don't know. It's just, just says Gallup study principle findings from the Gallup study. This is a January, 1978. Yeah. So it's like, um, there and there, so there, they've got a list of all these different machines and numbers in there, which I don't know what they're referring to. Are they referring to like instructions per second or, or something degree of confidence? So they've got IBM, Xerox, TI, Sony, RCA, Radio Shack, HP, Sears, because Sears actually had a computer. Lafayette, uh, Parker Brothers. Parker Brothers. Bradley. Those are toys. So they're comparing toys. Yeah. So they're comparing some of the, you know, those shoot them video games. Those ones that you point at your TV with the gun, you know, the photo sensor gun. Oh yeah, yeah, yeah. Uh, Mattel, Hitachi, Heath, Atari, Commander, and Apple was not included. I was going to say, the other one.

**Speaker ?:** That's what it says.

**Dave Jones:** Apple not included.

**Chris Gammell:** You're going to, you're going to hate me for this, but I, I've started reading another book, Dave. Um, but I've been reading, uh, eccentric orbits, the, uh, iridium stories. No. You know, the, the satellite network that was went up.

**Dave Jones:** Oh, right. Yeah.

**Chris Gammell:** It's a really good book so far. It's like all like, uh, it's written like a drama. Like it opens with like, we're going to shut down the system and burn up the satellites. So it's, it's very well written so far. Um, but I didn't, I would, there's a, they get into a bunch of the Motorola history, which is based here in Chicago. Well, Schaumburg, which is outside of Chicago. And like, I didn't really have, you know, I knew Motorola was big. I did not realize the dominance that they were. Oh yeah. Also the name, do you know what the name comes from? No. The Motorola comes from, uh, it's a, it's a portamanteau of motor and Victrola, which is like the old record player. Yep. So it's, they used to install radios into cars and those were motor, the Motorola. They were, they were called, they were named after the, uh, the, uh, the founder initially, but then they just like, people just kept referring to them as Motorola.

**Chris Gammell:** And they're like, okay, great. Yeah. We're changing. Yeah. Right. Yeah. Oh yeah. They're, they're absolutely enormous. They're into everything.

**Chris Gammell:** Well, they were, I mean, they're, I am currently in a building that is the shell of their former selves, you know?

**Dave Jones:** Oh, okay.

**Chris Gammell:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. So this is.

**Dave Jones:** Who owns Motorola now? Somebody.

**Chris Gammell:** So like the Motorola company is still around, but a lot of, a lot of the things that people think about. They bought it. Right. So like, so Motorola, the assets, a lot of it became like NXP. Wait, was it NXP?

**Dave Jones:** Oh yeah. There were lots of spinoffs.

**Chris Gammell:** So NXP, so sorry, Freescale was the, some of the Silicon spinoff, I believe. And then.

**Dave Jones:** Don't try and follow the.

**Chris Gammell:** Yeah. Then that got sold to Freescale, which is now an NXP.

**Dave Jones:** The family tree. You'll go insane. Yeah, exactly. You'll go insane.

**Chris Gammell:** So like, but I think it all got broken up a lot too. Like, so like, and like the phones got sold to Google and then Google sold it to Lenovo. And so that's kind of a dead brand too. So, cause like, you know, the Razr in the early, the. Oh yeah. Early Razr days. Oh yeah.

**Dave Jones:** The Motorola flip phone was the duck's guts. Yeah. Right. Wasn't it? Yeah. Yeah. And I mean, they were. Still is. Like a lot of people are going back. I don't need this smartphone bullshit. Yeah. Just give me an old Motorola flip.

**Chris Gammell:** We've now entered the crotchety old Dave part of the episode. We've already gone through the book episode with Chris. Yep. Now we're into Dave, Dave talking about the good old days. Oh man. I mean, well, they were good. Oh, hey. Battery life was so great. I mean, like I, I told you about that phone I had in Germany, right? Did I tell you about that? No. Oh man. Tell us about your German phone. I had a dual SIM. I had a dual SIM, like feature, what are they called? Feature phones? Yeah. Is that what they're called? So a dual SIM feature phone with an FM receiver and, you know, texting and games and all the other stuff, whatever.

**Dave Jones:** You're texting and snaking like a boss.

**Chris Gammell:** That's right. That didn't have snake actually.

**Dave Jones:** Oh, it didn't have snake. Okay.

**Chris Gammell:** But the dual SIM thing was crazy to me. And it was, of course, 11 euros at the store.

**Dave Jones:** 11 euros.

**Chris Gammell:** It's like insane, you know, like.

**Dave Jones:** Wow.

**Chris Gammell:** Yeah. Wow. I love that. I saw it. It's a great little phone, you know, and you know, it's harder to find those things, I think. Right. The little feature phones. And let me tell you, going back to T9 typing, not easy.

**Dave Jones:** You get them, you see them at the post office. Oh. When I'm at the checkout of the post office under the little counter there, here's your phone for $20. Oh, like a burner phone. A burner phone. Yeah. Burner phone. Yeah.

**Chris Gammell:** We don't have, we have our post office a little different, but yeah.

**Dave Jones:** Right. Yeah. Got it. You're not really allowed to have, because I'm pretty sure, someone correct me if I'm wrong, but you're not allowed to buy a phone in this country unless you provide ID. Sorry, you're not allowed to buy a SIM card.

**Chris Gammell:** Oh, a SIM card. That's.

**Dave Jones:** You're not allowed to buy a SIM card. You can't buy a SIM card without the bastards wanting to track you.

**Chris Gammell:** That's pretty common, actually.

**Dave Jones:** Right. Is it? Okay.

**Chris Gammell:** I mean, like, well, at least not, maybe not common, but at least when I go overseas, I always have to give a passport to buy a SIM card. Oh, really? Yeah. Okay. Yeah.

**Dave Jones:** Right. Okay. Yeah. So. All right. So it's a thing. Mm-hmm.

**Chris Gammell:** Okay. Yeah. It's got tracking, blah, blah, blah.

**Dave Jones:** Speaking of cheapest chips, I won't mention what it is, because I haven't released the video yet, and I've teased people on the forum.

**Chris Gammell:** Okay.

**Dave Jones:** Anyway, there's this. So you're going to tease people here. So segue to ridiculously cheap. I was, you know, surfing AliExpress, as you do. As you do. You know, how it pops up with the recommended things. You know, here's the recommended things. And it popped up with this recommended, let's just say it's a test instrument. Sure.

**Chris Gammell:** Okay.

**Dave Jones:** And it's a bit of test gear. And I went, oh, okay. It's one of those, you know, known, you know, cheap ass Asian brand versions of this product. Right. And, but the price caught me. It was $8.95. And it's like. Is that Australian? No. That was US. Yankee bucks. That's insane. Including free delivery. That's delivered. Right. Wow. That is, I'll tell you what it is after the show. This is, oh, actually, I'll send you a, can I send you a link now? I'll send you a link now.

**Chris Gammell:** I mean, this is just mean for the audience, Dave. Come on. But yeah.

**Dave Jones:** Yeah, I know. I know.

**Dave Jones:** So what's the point about it?

**Chris Gammell:** You're getting to the point about the cheapness that you're saying.

**Dave Jones:** I'm getting to the point of the cheapness of it. And anyway, so I was like, it was $8.70 US, right? Free shipping. So I ordered one of these things and I've got one in my hand now. It just turned up. And sure enough, it works. It seems to meet its specs. The teardown inside looks okay. It is completely no name, right? And it looks like they've actually scrubbed off physically on the product. They've scrubbed off the name and the model number. Right.

**Chris Gammell:** Well, that actually happened when it fell off the truck. It just scraped on the ground. Right. Oh, magically.

**Dave Jones:** Oh, gosh darn it. Yeah. And it's, but the name is on the box. So it comes with the box and all the original accessories and everything. And are you having a look at it now?

**Chris Gammell:** I am, yeah. Yeah.

**Dave Jones:** Right. So you know that these things are normally quite expensive because they're quite precision, right? These things are usually a, you know, let's just say that they're quite precision things. And this exact model, if it's actually under the original brand and name, it normally goes for well over $200 US on eBay. Right? That's what, you know, they sell these things. Yeah. People buy them.

**Chris Gammell:** Yeah.

**Dave Jones:** And I thought it's $8.70. Like what, what is this some sort of like this company's just got the price wrong. They've listed it wrong. So I quickly ordered one and I finally got it. Then I realized, no, there's these other sellers who also sell the same thing once again with the brand removed. And they've all got different stock levels. So it looks like they've all got their own stock. So I'm, I'm, I'm unsure if this is like a one-off thing where. Oh yeah. Sorry. Does it work?

**Chris Gammell:** Yeah. Does it work to all the specs? Yeah.

**Dave Jones:** Yeah. It works. It seems to, it seems to meet its specs. It seems to be bang on actually. And like, I haven't done a full, full review. That's what I'm doing after this show. And, but it's, it's $8.70 for this precision. Like, like normally you'd pay that for a cheap ass. When's this video going out?

**Chris Gammell:** When's this video going out?

**Dave Jones:** Right. Oh, I, I, I, I don't know. It'll at least be a couple of days. Anyway, if it is.

**Dave Jones:** I was going to say.

**Chris Gammell:** All right.

**Dave Jones:** Anyway. Anyway, we, I'll, I'll link in the video if it's already out by the time we do this.

**Chris Gammell:** I just meant we could see what it was otherwise, but yeah.

**Dave Jones:** So I originally thought, oh, I've discovered this company that's got the price wrong. So what I'll do is I'll buy them all up at $8.70. Sell them at $9. Just flip them on eBay for like, you know, a hundred bucks or something, which is half the current price. Less than half the current price. Right. And I'll just sell them and make, make some quick cash. Yeah. And, but then I realized, no, you can't buy more than, you can buy more than two, but if you buy more than two, it's not free shipping and the shipping costs double the, triple the price of the product. Right.

**Chris Gammell:** Right.

**Dave Jones:** So it's like, it didn't, eh, it couldn't be bothered. It's, you know, this cheap no name thing and, you know.

**Chris Gammell:** Yeah, man. Anyway. I mean, this is like, this is just the. What? The.

**Dave Jones:** Did it fall off the back of the truck? No, this is just the market.

**Chris Gammell:** This is basically the, the local pricing of what, you know, you go to China, you get stuff like this cost. I think that's.

**Dave Jones:** With, with the brand deliberately rubbed off.

**Chris Gammell:** Yeah, I think so.

**Dave Jones:** It's like, it literally has no name and no model number.

**Chris Gammell:** Are you saying that it's close enough to another brand that it, it is the same manufacturing?

**Dave Jones:** It is the same manufacturer. I've opened it up and on the silk screen is the correct model number and everything else. And it looks like I obviously don't have the legit in quote marks from the company to actually compare it to, but it looks legitimate. So I'm wondering, is it, are they factory seconds? Are they, you know, did they fall off the, you know, did somebody steal them and they fell off the back of the truck and they rubbed all the names and numbers off them and they're repackaging them? What? Like is, you know, or, or is this, as you said, is this just, I've discovered the local pricing for this product?

**Chris Gammell:** Yeah, I think that's, yeah.

**Dave Jones:** That's my vote. Like I'm about to go through the teardown, go through every chip on the board and add up the cost. Right. Because this is a precision instrument. Yeah. Right. It, it needs precision parts to meet these specifications.

**Chris Gammell:** I think you need a x-ray machine though too, because you might be surprised.

**Dave Jones:** Right. You think, oh, that's not a genuine TI voltage reference, you know, 0.01% voltage reference. No, it's not. But, oh, it, on the surface, it looks legit and holy shit, it's $8.70. Yeah, yeah, man. I just can't believe it. It's got all, it must have all these precision parts in it. Yeah.

**Chris Gammell:** I think more of a philosophical question about all this stuff is like, okay, so now everything is this cheap. Now what? And it's like, I think, I think, you know, it's like, it talks about the cost of value, brand and repairability and everything. Not repairability, but like service and all these other things. Like, honestly, that's what we're paying for is sometimes, you know, like, so like thinking about the software world too, and like open source, like when you're paying for software these days, oftentimes there's, you know, obviously I'm a big fan of open source, but like when you want to, there's, you're paying for someone to yell at, you know? And I guarantee if you're yelling at someone about an $8.70 thing, I was going to say what it was for there for a second, then you're going to yell into the void, I think, you know, like, it's just like, it's just a throwaway thing.

**Speaker ?:** So.

**Dave Jones:** But I, like, I understand that China's cheap and internal China is even cheaper. Yes, yeah. Right? That it appears to us. But this is too cheap. There's got to be, there's got to be something going on here.

**Chris Gammell:** I think, I don't think so, man.

**Dave Jones:** My spidey sense tells me that, like, no way. No way.

**Chris Gammell:** Well, I think, well, I think it might, like. The fact that it has the other silkscreen on it doesn't mean that it's actually the same thing, but it could be just replicated. I mean, like, it's.

**Chris Gammell:** It could be replicated.

**Chris Gammell:** You could have found the low end benchmark as well. I mean, like, that's, that's what I think about is like, okay, it could be a lot cheaper. How cheap? And it's like, yeah, you might've found the cheapest thing, you know, or to get any cheaper than that. Then, then it's like, okay, now we're going to rip stuff off the board. That's not. Right.

**Dave Jones:** We got to do some months in. Yeah. We got to. Right. Exactly.

**Chris Gammell:** And, and, you know, that's the thing. Like, I think any system, you know, gets. Right. Commoditized like that eventually. And it just. I don't. I don't have a value judgment on this. Honestly, I don't. Like.

**Dave Jones:** But, but you can, but you're looking at what the product is. You're looking at what the specs are.

**Chris Gammell:** I don't have as good of a. Right. To scroll down. Sure. I don't have as good of a feel for that as you do.

**Dave Jones:** Yeah. But you come from Keithley. You come from the precision measurement field. Right. What does it cost to get 0.02 percent?

**Chris Gammell:** It's a bit. Yeah.

**Dave Jones:** Right. Yeah. It costs a bit. Right. This is precision stuff. Yet. It's in the price of one of these $2, you know, cheapy multimeter things. It's down in the same price category.

**Chris Gammell:** I don't know. He's like, wow, man. I don't know what to tell you, Dave. Sorry, man. This is just the world we live in now.

**Dave Jones:** Is there a magic supply of these, you know, 0.02 percent, 0.01 percent voltage references from some one hung low manufacturer?

**Chris Gammell:** And you're saying you tested that piece already or no?

**Dave Jones:** Yeah. Yeah. I've tested that piece and it's bang on. It's well within spec. Well within spec.

**Chris Gammell:** I don't know, man. I have no idea. I think the only thing I have to say now is like, I guess I'll buy one, you know?

**Dave Jones:** I guess you'll buy one, but do it before the video comes out.

**Speaker ?:** That's right.

**Dave Jones:** Exactly. I swear thousands of people will instantly just buy two of these. You wouldn't just buy one. You'd buy two so that you can compare them with each other. Oh, I'd just buy one in case they blow one up.

**Chris Gammell:** Right.

**Dave Jones:** It's unbelievable. It's unbelievable. Anyway, I've hit the jackpot. So anyway, I will not be reselling this. I'll do a video and my Patreon supporters and forum supporters will hear about it first so that they can get first dibs on this remarkable thing that I found. I was just stunned.

**Chris Gammell:** Yeah. Well, maybe this just kind of points towards like, you know, software is a differentiator in the first place these days. You know, hardware is so commoditized. Just, you know, just further down that track, you know, it's just hitting, it's now hitting the, it's now hitting the test market. I think it's dubious just because like, I know that good, like you, I mean, I know good components cost a lot of money and, but maybe they found some other source and maybe, you know, that's maybe the best thing about it is someone's figured out how to make precision resistors for, or precision voltage sources in China for much less. Maybe that's different, you know, like it could be artificially priced stuff around here. I don't know.

**Dave Jones:** Wow.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, anyway, a very quick glance, it used a PIC processor in it. It used another, like it looked like it used, you know, like little legit stuff. So I'll, I'll see you after the microscope tear down, you know, you've got to like zoom in on each and every part, you know. Yep. Yeah. But wow. Wow.

**Chris Gammell:** You know, what will not be cheap is the Boston Dynamics spot dog. Did you see that?

**Dave Jones:** Ah, they're selling it.

**Chris Gammell:** They're selling it. Yeah. Yeah. And they basically, they don't give a price. They just have a, you know, contact sales. Right. But they said, I think about the price of a car. And I was like, is that like a, is that like a Civic or like a Tesla? You know?

**Dave Jones:** Yeah, yeah, yeah, exactly.

**Chris Gammell:** I have a friend who works there. He wouldn't answer me.

**Dave Jones:** Right. So, so we're talking, what is the cheapest car in the U.S.? Here, the cheapest car is about $13,000 Australian dollars. So let's say $9,000 U.S. I think that's about the same. It's like a little. Yeah. Right. Okay. Yeah. Right. It's like a little manual, you know, box. Oh, it's not manual.

**Chris Gammell:** It's not manual here, but it's cheap and it's very unsafe.

**Dave Jones:** Oh, no. Ours are actually manuals. Ours are, you know. Yeah, I know. A lot of countries outside the U.S.

**Chris Gammell:** The U.S. very rarely has manual transmission. Usually it's a special order rather.

**Speaker ?:** Oh, okay.

**Chris Gammell:** That's interesting. Right.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** That's interesting. Yes.

**Chris Gammell:** Says the guy who got in trouble when he went to a foreign country and rented a car and realized, oh, no, they didn't have any automatics for me. This is – all of the Europeans right now are going, yeah. Oh, yeah. Why –

**Dave Jones:** European manuals. Yeah. Yeah. Yeah. Yeah. Pussy. Yeah. Yeah.

**Chris Gammell:** I mean, yeah, pretty much. Yeah. They're like, why didn't you just learn it? Like, I just never did. So –

**Dave Jones:** Yeah. Same here. I've never driven a manual car. We've just never had one.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. There you go.

**Chris Gammell:** Guess when the zombie apocalypse happens, Dave, we're – Right. We're screwed. We're screwed. Well, I'm going to grind through first gear when that happens. Yeah, yeah.

**Chris Gammell:** Oh, I'm sure we can grind through it. Yeah. No problem. We're engineers. We can figure it out pretty quick. Well, yeah. Yeah.

**Chris Gammell:** My dad still gives me grief about – I tried learning. My sister had one for, like, when I was in high school. And I was like, Dad, I'm going to be good at this. I play the drums. So I have to be able to use both my feet independently.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Yeah. It was not a good experience. So I'd never learned. Okay.

**Chris Gammell:** All right.

**Chris Gammell:** Yeah. So the spot thing is pretty cool. I mean, like – and it's interesting because it's like – it seems like it's commercially available, right? A lot of these things seem like they're not – you know, you can't just go buy and – I guess you could. But, like, you know, you think about, like, industrial ABB-type arms and similar, like, Juki – sorry, Kuka robots and stuff like that. They're, like – they're so expensive and they're so big. And, like, you just – you wouldn't do it. But now this is, like, actually a robot that's a little creepy. Yeah, it's still a little creepy. But it's – it is accessible to companies and individuals who are – have way too much money – more money than cents, you know? Right. So – and it's, you know, it's fun to watch the robots. So that's the opposite of $800. Now, when we see one of these on AliExpress, I'll be impressed. All right. Well – I think we've got a while on that one.

**Dave Jones:** Are there robots on AliExpress? Can you, like, shop food? I don't know.

**Chris Gammell:** That's a great question.

**Dave Jones:** Robot? Like, is there, like, some – I'm sure it's going to be at Toys and stuff like that. No. Oh, no. Yeah, yeah, there's toys. No. Robot vacuum cleaners.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep, yep. That's it. Yeah.

**Chris Gammell:** Boring. Yeah. Boring.

**Chris Gammell:** Boring. I guess you can't get everything from China.

**Dave Jones:** No. No, no, no.

**Chris Gammell:** Type in industrial robots. You can totally – oh, man, that's pretty cheap, actually. $209 for a three- to four-axis robot? Okay. Interesting. I might be buying a robot later. We'll see. We'll see.

**Dave Jones:** Up to $9,700. The second hit is $9,700 for a four-axis.

**Chris Gammell:** Well –

**Dave Jones:** Wow. All the way from $19.99 for a robotic – Yeah. For a little plastic robotic arm.

**Chris Gammell:** Yeah, that's the meat arm. Oh, yeah.

**Dave Jones:** There's an ABB industrial robot model for $115 US bucks. Yeah, wow.

**Chris Gammell:** I doubt that's actually an ABB thing.

**Dave Jones:** Yeah, no, it's not there. You can't even get on a phone call with ABB for $115. Yeah, right. Yeah. Wow. Yeah, that's – wow. There's some serious kits on there.

**Chris Gammell:** Yeah, it's fun watching – so the robot stuff, too. So I don't know if you've been watching James – former guest James Bruton. He's been doing lots of – he's doing like a more from scratch kind of robot thing. It's like a robot body almost. So it's less legs. And he's been doing some great stuff for like puppetry lately. Recommend people check that out. We'll link in the show when he was on. I keep thinking about him actually. And I was thinking about him for the micro stuff that I'm doing because it's like – so like when you look at how James works, he's not doing – he's doing like interesting like end-use things. But he builds a skill or like a feature that he like uses over and over again. So it was like a big deal when he switched from like an Arduino Mega to like a Teensy. But he just keeps using it. He just has a toolbox of things that he keeps using over and over again. And I really like – Well, I don't know. Like I think about like – yes. I mean we talk about that here but like –

**Dave Jones:** That's how these super productive people do it.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Yeah. They just keep reusing stuff they know even though it's not the best choice. It's not the cheapest choice. Sure. It's not the blah insert thing here. They don't care. Right. They just want to get something done. Right.

**Chris Gammell:** Right. I think that's – and then if you need something super custom at that point, then you go and do the other stuff. I don't know. Of course. So like I think about like my past design history and stuff like that. Like I've usually had the opportunity to go and design a new thing but that's not always the right choice. You know, like sometimes it's just – especially if you're going fast and that's kind of the thing that I've been running into more is just needing to go fast. It's like you just got to grab what's nearby and just get something working, you know. So it's – Yep. So it's a re-education on my part, Dave. Yeah.

**Dave Jones:** Speaking of former guests, Jerry Ellsworth – Oh, yeah. – has just released her new Kickstarter. The Tilt 5 is her new company because she's having a second suck of the sav after – well, no, third suck of the sav because she used to work at Valve doing VR – sorry, augmented reality, AR, at Valve. And then, of course, they famously booted her out and they gave her all the patents.

**Chris Gammell:** Yeah, well, they switched to VR, right? That's the –

**Dave Jones:** They switched to VR so they gave her all her augmented reality patents. She just went in there and cried and they gave it to her. She didn't cry. No, you know what I mean. You know, she – but I worked hard on this and they gave it to her. So they just went –

**Chris Gammell:** I think it was more of a negotiating thing but okay. Give it to her.

**Dave Jones:** Anyway, no, no, no. The story has it is that she just went in there and talked to Gabe, I think it is.

**Chris Gammell:** Yeah, she wasn't just crying.

**Dave Jones:** And she just went, no, but you know, she –

**Chris Gammell:** I think that's a mischaracterization to say. Yeah, I think that's a mischaracterization.

**Dave Jones:** Metaphorically, yeah. She went like, I worked hard on – and they just – he just went, okay, give it to her. And then the lawyers went, are you sure? Right, right. And he went, yeah, just give her the patents. Right, right. And yeah, which was a very unusual move for the company at the time. But it turns out that, yeah – sorry, what was the name of her company? She – Technical Illusion, she started.

**Chris Gammell:** Right, and then that became the maker of Cast AR, which then just ended up switching the name to Cast AR, much like Motorola.

**Dave Jones:** And they changed the name, yeah. So they changed the name to the name of the product, which is Cast AR. And then there were negotiations with everyone, including Disney and I don't know. Everyone wanted to buy them, but then it all fell through. And that's the great stuff.

**Chris Gammell:** That's the great episode we did with Jerry where she was talking about the last – the Silicon Valley BS.

**Dave Jones:** Right, yes. It was great. And so, yeah, and she went, oh, well, bugger that. I'll just start another augmented reality company. Well, she had to buy it.

**Chris Gammell:** She had to buy the assets then from – out of bankruptcy. Oh, did she? Bankruptcy, yeah. Right. Oh, really? Yeah. Okay. Yep. Right. Which is – I mean, like, hell yeah. Like, talk about believing in your work. I mean, like, that's killer. Yeah, yeah. And, like, this stuff looks like – so if you watch – I don't know, did you watch the video and everything?

**Dave Jones:** Oh, I've seen the video. I was kind of disappointed in the Kickstarter video. It was so fluffy. Oh, it was a little bit more – Fluffy, wuffy.

**Chris Gammell:** Fluffy, yeah. It was less technical. It was more like a marketing – Yeah. But that's the market that you're going for, right? Oh, yeah, I know. So, like, she's trying to get people that are game developers and people that are game players and people that are new to the industry, right?

**Chris Gammell:** I know. I know. I know. She's not trying to get you.

**Dave Jones:** No, that's right. Although I did back it. I did back it, so I'm getting the basic kit. Oh, cool.

**Chris Gammell:** Nice. Yeah. And I think that –

**Dave Jones:** Even though I hate 3D, I hate augmented –

**Chris Gammell:** Yeah, so I've tried this out. I mean, I think it's – I've tried out one of the prototype ones, and I like it. I think it's a little bit more immersive – not immersive. It's less immersive, rather. But I like that it's not – I feel like I just take it off and set it down and kind of come back to it. So, like I said at the beginning, I think I said when Jerry was on the show one of the times, I've always been excited about, like – And, you know, because it's a generic thing built on Unity, that it could be tied into, like, educational applications and, you know, visualization. Sorry, Unity? Sorry, Unity is the game engine. Oh, okay. I have no idea. So, she just posted a video today, too, showing how all that stuff pulls together.

**Dave Jones:** Yeah, behind the scenes or something. She said, like, how the development kit works or something. That's right, yeah, exactly. The SDK.

**Chris Gammell:** Yeah, so basically it's like you're – she was just showing, like, how to import the – you know, it's basically having a bunch of scripts to kind of, like, tell you what the hardware is available, what views are available. And then a lot of the Unity thing is it's kind of this standardized interface, and that's how a lot of game developers work. And then you – Okay. Basically, you could use that as the development around stuff. I mean, like, you look at something like that, and then you compare it to something like how – well, I guess I'll use Embedded Tools because I've been using that all episode. Like, how just, like, everything is kind of just works together. Like, it's just – the difference is so stark. It's amazing. Right. You know? It's like a standardized interface. It's like, what's that? I don't get how that works. We need to talk to registers, you know? So. Yeah, right. Yeah. But, yeah, I think it's great. And – oh, the thing in the video that I was going to call out is just the weight that they talk about it. So it's like – there was a review that Norm did from Tested, too. It was, like, 90 grams or something like that. So, like, thinking about – Got it. How light that is on your face, that's pretty cool.

**Dave Jones:** Yeah, that's pretty good. That's pretty impressive.

**Chris Gammell:** So.

**Dave Jones:** It's still a bit bulky. Like, it's still – you know, but it's light. Light is better than bulky.

**Chris Gammell:** Bulky, you're saying, like, volume bulky, right?

**Dave Jones:** Yeah, yeah, it just doesn't look as polished. I don't think it looks as polished as the cast's AR one. Don't quote me on that. But anyway. I don't really know. Yeah, yeah. Anyway, still, yeah, she smashed her target in, like, the first hour or something.

**Chris Gammell:** Yeah, yeah, yeah.

**Dave Jones:** So it's going absolute gangbusters. And I think she didn't make the mistake of taking outside investment this time. I don't know. Do you know about that, if that's correct? I could be wrong about that, but I think it's all hers this time.

**Chris Gammell:** Yeah.

**Dave Jones:** I don't. I'm assuming so. I stand to be corrected.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, as Jerry talked about in that episode she did last time, it was – Yeah. It sounds a lot different. Pros and cons of taking other people's money. Yeah, right, right.

**Dave Jones:** Yeah. Yes, I'm sure she wouldn't get bit twice. Yeah, yeah. So anyway. Yeah.

**Chris Gammell:** Let's – go, Jerry. You can do it. Excellent. Yeah. Fantastic.

**Dave Jones:** Anyway, so yeah, I'll be following that because I'll be getting one. Yeah. Yep.

**Chris Gammell:** That's great, man. Hmm. We only got like a couple minutes left. We – Yeah? Yeah, we blasted right through things. Let's see if we got stuff from a couple weeks ago even. Let's see. That's from three weeks ago. It's been –

**Dave Jones:** What's the scientific method of troubleshooting? What's that?

**Chris Gammell:** Oh, this is when I was reading the art of motorcycle maintenance. I was thinking about that stuff, too. Oh, God. Right. And so it was like – Define the problem.

**Dave Jones:** Do your research. Come on.

**Chris Gammell:** Yeah.

**Dave Jones:** What is that?

**Chris Gammell:** Yeah, I think I was just searching around. Maybe it was the video. I don't remember. But I was thinking about like the scientific method with regard to troubleshooting. Like because like when – so like I said, like I mentioned earlier, like thrashing, right? If you don't like have like a hypothesis and you don't – you know, like if you don't write it down, obviously, it's not science, right? That's a common thing.

**Dave Jones:** Right. That's the difference between science and bumming around is writing it down. That's right. Right. Yeah, exactly.

**Chris Gammell:** But I think sometimes like I'll be on the bench and I'll be like, oh, it's probably this thing. And I'll, you know, move a resistor or whatever has to happen. And then I'll try it. And it doesn't work. And I'll be like, oh, maybe it's this resistor. You know, try that, try that, try that. And if you're not like tracking your changes, you can get into a spot where it's like you're kind of like back in the corner. You have to like either reset all the way to the beginning or you burn up a board or whatever happens. And I feel like the best troubleshooters out there are more scientific about it. They're like, okay, I'm going to – you know, maybe they're not formally saying it or formally writing it down as an experiment. But it is basically running a bunch of small experiments. And I always refer back to like Ben Krasnow talking about that. But one of the codings he was doing is like now I'm on experiment number 88 or something like that. And it's like – Right, yeah. But it is like that formalized method of like having – and like being able to then point back to it and say, hey, look, I'm – you know, on 33, I tried this and this thing – This weird effect happened. Yeah, exactly. This weird effect happened. And maybe that gets triggered later. And if you're not tracking it, you're not tracking it. You're now on try 60. You're not necessarily going to remember. It's like, oh, I remember something happened on 33, but I didn't write it down. You know, like that's kind of like the – so that like the rigor is very tedious, but it's also can be very important, you know, kind of tied back to the engineering notebook thing too. So I don't know. I've just been thinking about that with troubleshooting. I don't know how you normally troubleshoot, but I'm more of a thrasher and I wish I would be – I'm trying to work towards being more of a scientist.

**Dave Jones:** Yeah, I know. I just know I'm not disciplined enough because I – like – because you've got to go in with the mindset from the get-go that you need to document it regardless of how simple you think it is. Like because I always think, oh, look, I'll just solve it in five minutes. Yeah, exactly. Why would I even start documenting this? And three days later, I'm still working on it. No, I'll just – I'll fix it in another five minutes. Right, exactly. You don't need to document it. Yeah.

**Chris Gammell:** And I think that's – at some point usually I then go and write stuff down and then it's kind of like either mental rubber ducking or like I actually go talk to someone about it and like –

**Dave Jones:** Or you don't have a formal process so it's on a couple of post-it notes on your bench. Exactly. Which then get lost and – Right.

**Chris Gammell:** But when I do switch around and I – so I have notes where I started writing down what the different things were. I can go back and look at my notes now. And like, yeah, at that point, like usually that's when I start to figure things out. It's just like it's at the beginning when I – it's always at the beginning, you know, when it's just the – like you said, the five minutes. Oh, just five minutes. It'll just be five minutes. It's never five minutes.

**Dave Jones:** Yeah, yeah. It's that night. Yeah.

**Chris Gammell:** So.

**Dave Jones:** Well, no, sometimes it is. And you just don't think about it. And it's like – and then you get into the habit of fixing things quickly like that. But when one difficult problem comes up and bites your ass, you go, oh, geez, I wish I'd documented all those resistor changes I made to test this. Yeah, exactly.

**Chris Gammell:** Like, yeah. Right. And thinking through like, okay, well, the hypothesis was if I change this resistor from, you know, 47.7 – 47 kilo ohms to, you know, 22 kilo ohms, it's going to do this. And then it's like failure. Or – but, yeah, instead it's just – I just get a pile of formerly soldered resistors around the board. So I need to get better about that. I think we could all do a little better with that.

**Dave Jones:** Have you ever had to go through the solder tray? Yep, yep. The solder tray in your thing where you've deposited all those resistors you put off the board and actually measure, oh, which is that capacitor? What value was that? So you go and find it and measure it. Yep. Oh, totally. Right.

**Chris Gammell:** Because, like, you're doing it so much and then you, like, you pull back the tape and you realize that it's the last pocket and there's no part in there anymore. Yep. Or it was the last part and you're like – and then you fling it across the room with the tweezers, you know. Yep, yep. Good times, not really. Yeah.

**Chris Gammell:** Fantastic.

**Dave Jones:** Yeah. I should get back into that. I should get into the notebook per project because I always had a notebook per project. So I still – and I used to keep them in – like a milliliter envelope thing. Oh, okay. So like an envelope. So I'd have, like, the notebook inside. And I still got some here. Okay. I think I can just see – I can see a couple from here. Yeah. And, you know, so that would not only contain my spiral-bound notebook-y thing that I was using at the time to do all the notes, but it contained printouts of schematics and marked-up schematics. Yeah, that's nice. And other, you know, stuff and things like that. So it would all be in, like, a pouch. So at any time in theory, I could just pull out – this is how disciplined I used to be. I could pull out that package and it's all in that folder.

**Chris Gammell:** See, Dave, what my experience is you just need to have five concurrent projects going and then you basically don't have a choice. You know, you're either going to go nuts or you're going to get more organized. So that's kind of what I've got going. Yep. Yeah, I like that idea. Good luck with that. You know, the paper thing, I can't – I don't know.

**Dave Jones:** No, you can't get over the paper. Yeah. Oh, no, I love a good notebook.

**Chris Gammell:** I mean, it's nice, but I just – I'm really spotty with it. You know, for some reason I keep coming back to the digital thing probably just because I'm always on the computer anyways. Yeah. Yeah. But some people, like, having it right in front of you really can help, you know. Yeah.

**Dave Jones:** Absolutely. Yeah. All right. Well, that's all we've got for this week.

**Chris Gammell:** Yeah, there's more links over on the subreddit. People can always go check those out. So otherwise, catch us on Twitter, you know.

**Dave Jones:** Yeah. I'm going to go work on my $8.70 precision instrument. Yeah.

**Chris Gammell:** I'm going to go buy one. I'm going to go buy one.

**Dave Jones:** Yeah, yeah, man. Go buy one before they all sell out. It's the Dave effect.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Yeah. Yeah. Anyway.

**Chris Gammell:** All right, man. All right. Talk to you soon.

**Dave Jones:** Catch you next time.

**Speaker ?:** Bye. Bye. !
