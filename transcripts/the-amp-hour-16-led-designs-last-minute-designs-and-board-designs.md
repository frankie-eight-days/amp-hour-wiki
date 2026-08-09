---
episode: 16
title: LED Designs, Last Minute Designs and Board Designs
url: https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/
---

**Dave Jones:** Hi, welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life. How you doing, Chris? You made it. I did, yeah, yeah. You had to rush from work. You know, I was so angry today. I was thinking to myself, I know exactly what I'm going to talk about on The Amp Hour today. I was going to do a little dance and I was going to be like, yeah, we conquered the time difference. I finally got a fix. I honestly thought that. And then, nope, nothing.

**Dave Jones:** No, no, because we've been screwed again, haven't we?

**Chris Gammell:** Yep, stupid.

**Dave Jones:** Yeah, because once again, we were both thinking that our, because Daylight Saving, we've been an hour out of sync for the last, what, four or five episodes or something? And we thought, well, Daylight Saving ended at your end, but I thought it was just starting and you thought my one had just ended instead of started or something like that. Now we're two hours apart. Yep. So, what do you do?

**Chris Gammell:** What a mess. What a mess.

**Dave Jones:** Oh, anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** Bloody time zones. What can you do?

**Chris Gammell:** You know, I was actually, I was thinking about switching over to GMT and just going by that all the time.

**Dave Jones:** Right. Just actually changing your actual watch to GMT and, yeah.

**Chris Gammell:** But then I'd probably miss local appointments where I'd be like, oh, yeah.

**Dave Jones:** Exactly. You'd be screwed like, yeah, work and other things. Yep. Meeting the wife somewhere. Right. Yep. Yep. Yep. Yep. Oh, dear. Anyway, we have an action-packed action-packed. We do. Action-packed? Oh, yes. A packed show today.

**Chris Gammell:** Yeah, there's a lot of good, you know, I think we kind of both took it to heart last time that we didn't have enough tech stuff.

**Dave Jones:** Yep. So, I think there's no shortage of that here today.

**Chris Gammell:** We're like oscillating back and forth. Now, we're super nerdy and then, you know, next time it'll have no content that's super nerdy and then back and forth and back and forth. Right. Yeah.

**Dave Jones:** Well, let's start with our usual shout-outs. We have a couple.

**Chris Gammell:** Yeah. Yeah, I could put a couple on here.

**Dave Jones:** You added them in here. Tell us about them.

**Chris Gammell:** First one was a new show by Troy Rank. He talked to me about it. It's about electronic bikes. So, you know, there is the biking aspect to it. But in this case, he also talks about like power electronics. Like his first show, he was talking about someone that had 36 FETs in a power converter on the bike. So, I think that's going to be part of his regular, you know, content is actual power electronics. So, you know, welcome to him and, you know, hopefully he does well. Hope you do well, Troy. Yeah. Yeah.

**Dave Jones:** And next we've got, it's under shout-outs, but it's a triple five timer.

**Chris Gammell:** You know, I was looking at that today. Yeah, I put that in as a shout-out. But just like, I was looking at it today because someone, oh, because I saw a news article about someone making a new one. I forget who it was.

**Dave Jones:** It was the, well, it was the original designer. Zetek came out with, Zetek, who are now diodes in, came out with a low voltage version. Yeah, that's right.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, triple five. They got the original designer back in. I forget his name, but yeah, they got him back in to design a low voltage version. But I think that might have gone by the wayside now, but somebody else is doing another version, aren't they?

**Chris Gammell:** Yeah, I think someone else is doing it. Yeah. So, anyway, I just wanted to shout-out. Like, I mean, how many designs out there? Like, 50, 40 years? That thing came out in 1970. That's even before I was born.

**Dave Jones:** So, there you go. That's how old it is.

**Chris Gammell:** Yeah. I mean, it's just beautiful design, you know, like, not like the most power efficient or anything like that, but it gets the job done and it's amazing. So, I thought that was a shout-out. I mean, people obviously talk about the 555 all the time, but how do you say it? Do you say 555?

**Dave Jones:** Nah, we say the 555. 555, really? Okay. 555. It's always the 555. I've never heard about the 555.

**Chris Gammell:** No, you never have called that?

**Dave Jones:** Even from Yanks. No, no, no. It's always the 555. The 555 timer.

**Chris Gammell:** Yeah, I guess.

**Dave Jones:** Yeah, you just don't have much street cred if you're going to call up the 555. I don't know. It might be big in Ohio. I don't know. Yeah.

**Chris Gammell:** Yeah. As trendsetters in Ohio.

**Dave Jones:** Right. But, yeah, it's awesome. So, a shout-out to a chip.

**Chris Gammell:** Of course. There you go.

**Dave Jones:** Last I heard, they, probably only a couple of years ago, they were still selling over one billion per year. It's insane. It's insane. In case they're still putting them into all those farting toys and stuff like that that are coming out of China.

**Chris Gammell:** Yeah, and there's just so many designs that are out there that are just all these legacy designs that use them. And there's a lot of variance on them, too. I know that LT has these modules that are supposed to replicate some of the functionality. But even that, it's like, well, why bother? When you can get them for like 10 cents, why bother paying the dollar to LT?

**Dave Jones:** I think an expensive one is 10 cents. Because there's such a whole gray market built around the triple five timer as well. Every Tom, Dick, and Harry does a version of the triple five. Yeah. Yeah. Very readily available. That's one part you'll never be stuck with. Oh, it's out of stock. Sorry. Can't get it.

**Chris Gammell:** You'll always be able to get the triple five somewhere. Only if you're like really brand loyal, you know? Right. Yeah, exactly. It has to be Z-Text. Oh, I only touched the TI version. Yeah, yeah. Yeah.

**Dave Jones:** Yeah. All right. Yeah. What? We've got a whole stack of stuff. So let's start from the top. I had one more shout out. Lead drive. Oh, one more shout out.

**Chris Gammell:** One more shout out. Yeah, sorry. I saw an article today about Google's interview questions.

**Dave Jones:** Oh, yes. Okay.

**Chris Gammell:** And they were, so that, you know, like usual interview questions. One was like, how do you figure out how many golf balls would fit inside a school bus? You know, like mind benders, blah, blah, blah. But the one that I wanted to give a shout out to is the fact that they ask what dead beef is. Right.

**Dave Jones:** See, I had never heard of that because I'm not a software geek.

**Chris Gammell:** You never heard of dead beef?

**Dave Jones:** No, I haven't. I'm afraid not.

**Chris Gammell:** It's just an easy...

**Dave Jones:** Sorry, I'm not computer science geeky enough.

**Chris Gammell:** You know, that's kind of on the edge though because the thing is that, and that's what I wanted to talk about is the CS guys might not necessarily know what that is because software gets so abstracted these days. If you get a Java programmer, they're not going to necessarily know what that is. Some CS guys don't even know, like, you know, memory space kind of stuff. So I guess that's kind of like the computer engineering side of things.

**Dave Jones:** Right. Yeah. Yeah. No, see, back... Well, see, I did mine 20 years ago almost, you know. So back then it was like you worked at such a low level that you didn't have any of that sort of, you know, I don't think dead beef was around 20 years ago, was it? I don't know. When does it date to? But it might even be before my time, I'm not sure, but it was always used on bigger systems like the Suns, you know, the Solaris and all those big operating systems, whereas I always worked down at the extremely low level, like, you know, set up, you know, register A and set up register B and, you know, this dead beef thing, just all this. If you had dead beef in there, it was just pissing away eight bytes or whatever, you know? Yeah. So...

**Chris Gammell:** Yeah. No, that's a good point. I mean, but that is what it's for. I mean, we didn't really explain that, but dead beef is a check. Oh, yeah. So as you're looking down the memory and you see dead beef, it's a very recognizable thing and you just see it right away. And so, yeah, I mean, that's understandable. That is a good bit of data you might not want in, like, really, really small embedded systems. But now it's kind of to the point where they're merging, you know, like, even, like, the Arduinos and stuff like that. If you're looking at a memory register, right, and you want to see a recognizable character, you might throw that in there, you know, if you're troubleshooting. Right. Okay.

**Dave Jones:** See, I wouldn't have used dead beef. I would have used hello world or something, you know? Well, no, because it's hex, too. That's the other thing. Well, it's hex. Yeah. That's the whole idea is the word dead beef can be, you can come up with a better word than dead beef out of hexadecimal characters.

**Chris Gammell:** Really? There's feed beef. There's, what else is there? There's dead, no, not dead. I'm sure there's a lot of good ones. If you have good ones, people can throw it in the comments section. But, you know, there's some good ones out there. I mean, you only get A through F, so.

**Dave Jones:** Yeah, I know. But surely there's better words than that. Anyway, I had never heard of it, so that was news to me. But, yeah, I hate those Google interview questions. I've been to a couple of job interviews where they try and copy that Google technique of asking these men's type, you know, the high IQ club. They're like these puzzle questions. Yeah. They're stupid, you know? They're just, they have no relevance whatsoever, so. Right.

**Chris Gammell:** Yeah, I just don't like them. They probably expect a certain level of skill to start with, you know, either from filtering and then they want to get the super duper top people.

**Dave Jones:** But, you know, they can have them. But the people who answer those men's questions aren't necessarily the people who are going to be the best at what you want them for. Yeah. I agree. Yeah. You know? Yeah. If I'm hiring a guy who has to do PCB layout or something, I don't, guy or girl, then, you know, I don't give a shit if they can answer men's questions. Jeez. You know? Yeah. Show me your boards. Right. Yeah. That's, anyway. I don't like them. And, yeah, there's a bit of a trend of companies doing that, asking these questions. It's all trendy to be like Google and, you know, Microsoft as well do the same thing. They're famous for doing that as well. Yeah.

**Chris Gammell:** Well, they're going to start running into problems, too. I mean, like, either they're going to have to start making up their own riddles or, because these are basically what they are, or they're going to, you know, they'll get something new and blah, blah, blah. Yeah. Yeah. I still like...

**Dave Jones:** And the problem...

**Chris Gammell:** No, go ahead.

**Dave Jones:** Sorry. Well, the problem is you don't know whether it's a trick question or whether or not, you know, there's a real smart-ass answer or whether or not it's just they actually want a genuine answer, like how many golf balls in a, you know, they just want to see your process of calculating it. Whereas, you know, you think, oh, do they want the smart-ass answer? Right. You know? Yeah.

**Dave Jones:** Can you imagine that? You're in an interview and you're like, one, one golf ball can fit in a golf ball.

**Dave Jones:** Because it's a big freaking golf ball because you didn't define the size of the golf ball. Yeah. You know. Yeah.

**Dave Jones:** And then they just kick you out.

**Dave Jones:** Yeah. Exactly. Because you're a smart-ass instead. Yeah. I know. That's why I don't like those questions. That's funny. There's just so many ways to answer them. I know.

**Chris Gammell:** I've asked a question like that and I think it was one of the few times I've done that and then I just got like the deer in the headlight look and I'm like, I felt really bad, you know? And you feel really bad and then you're like, oh, I guess I won't ask this anymore.

**Dave Jones:** Exactly.

**Chris Gammell:** Oh, dear idiot. Yeah.

**Dave Jones:** All right. Well, we wanted to talk about lead drivers, didn't we?

**Chris Gammell:** Yes. Yeah, definitely. I saw your project starting up and I'm doing a little bit of that too.

**Dave Jones:** Oh, okay. Doing some lead driver stuff, huh?

**Chris Gammell:** Yeah. Yeah. Are you doing? Okay.

**Dave Jones:** Well, if anyone hasn't seen it, we can put up a link. I was doing a lead drive, RGB lead driver thing at work. It was one of these, which we'll talk. Another thing we want to discuss is the crisis engineering. Oh, yeah. Yeah. So we'll get into that later. We'll keep it separate. But yeah, I've got these RGB modules. I was mucking around with these RGB modules the last week. I've been flat out on that. And yeah, I sort of caught the bug. I think I will do some RGB modules as a personal project. Oh, nice. Because I reckon there's a... Because you can buy these full-color RGB matrix modules from SparkFun, but they're like $60. Well, I reckon I can easily do the equivalent or better for half that price. So yeah, I think I'll have a go at that to try and make some low-cost RGB matrix modules.

**Chris Gammell:** Can you explain how the... So you buy the actual panels themselves, is that correct?

**Dave Jones:** You buy the RGB module, which has the matrix of the RGB leads in there, but there's no circuitry. They're just interconnected in the row column matrix thing. And then you've got to put some sort of... Wrap some sort of driver around that. Usually it's a microcontroller with some shift registers or something like that. A lot of people do it with shift registers. Okay. And then... That's because, I don't know, they don't want to use a big microcontroller. But I think a better way to do it is just to use a big-ass pin count microcontroller to drive the... What is it? 24 RGB columns plus the eight rows as well. So yeah. And there's many different ways. You can buy dedicated driver chips, but they're generally hard to get. So you want to avoid those from the likes of Maxima or whoever make these dedicated chips. And they're really nice, but they're like $8 a pop and you can't buy them. So yeah. Yeah.

**Chris Gammell:** Well, that's actually what I'm working... I'm designing with those because I'm doing a higher power situation. But I was going to ask you about those modules a little bit more. So explain to me the anode cathode. Like what's the hookup of those? I mean, like, so you'd be driving an individual single LED with a micro pin then with your idea?

**Dave Jones:** Well, you basically can't drive... Well, you can drive a single LED, but you usually drive them as a column, as a row or a column, depending on how they're configured. So generally you will output the, say, eight bits for the red. So you might drive a red column with eight bits and then you turn on that particular row. And then you switch to the next row and you multiplex the whole thing. There's actually, I'll put up a... There's an Agilent application note for driving RGB matrix modules. And it's quite detailed. Okay. Yeah. That'd be great. You'll have to remind me to link that one in. Yeah. Yeah. It's not something that you can easily explain on radio. It's easy and it's much better just to show people a diagram of how it's wired internally. And yeah, but it's basically rows and columns and you have to do a matrix. It's totally whole-deplex driven. So you can't just drive an individual LED, you know. So you've got to do them row-column based.

**Chris Gammell:** Okay.

**Dave Jones:** And it can get quite complex, especially if you want multicolors, because then you've got to do multiplexing and PWM at the same time. Interesting. So yeah, yeah. If you want the very colors, otherwise you just get the one fixed color and you can mix red, green, and blue and you can produce however many colors it is from those. But if you want the graded intensity, you've got a PWM as well.

**Chris Gammell:** So are you throwing actual digital signals to the module and then the module has its own internal drivers? Or are you actually pushing current?

**Dave Jones:** These modules, which I did, don't. They're purely just a shift register-based thing, and it's all controlled via the one main CPU, which has to do everything. But as you'll eventually learn with these sort of things, if you've just got the one processor trying to drive 50 of these modules, it doesn't work. Yeah, it'll brown out. The bandwidth requirements are just so massive that you just can't do it. I think that's where I'm confused. It's better to have a local CPU just dedicated to that one 8x8 LED matrix, and then the CPUs talk to each other and share the data and all that sort of stuff.

**Chris Gammell:** See, I guess that's where I'm confused because I'm not sure. So you're not driving, though, the individual LEDs with the current output of the micro, are you?

**Dave Jones:** Well, you're actually driving them with the current output from the shift register. Okay, yeah. Well, I'm not doing that in this particular design, but the design I'll do personally, I think I will actually do that. I will drive it directly with the microcontroller because you'll only have to turn like 8 on at once, and if you've got 30 milliamps per LED, that's probably just within the maximum total pin current specification of the micro. So you can actually drive them directly from the micro or from the 7.4 HC 595 driver or something like that.

**Chris Gammell:** Okay, yeah, that makes sense then. Yeah, that's a cool idea. I kind of like that. Yep.

**Dave Jones:** And then they're multiplexed, so the average current goes down, and so you aren't actually exceeding the total average current consumption for the pin. I think it's interesting. If you're not aware, well, you are, but the viewers out there might not be aware that chips, including microcontrollers and 7.4 HC devices, they will have two specs for output current for each. They'll have an individual spec for just the one pin. It might say, you can't draw more than 30 milliamps maximum from this one pin, which is great. You know, you think, oh, I can drive a LED directly with that. But then they'll also have an additional specification on top of that, which says you cannot exceed a maximum of 200 milliamps on the ground pin or the power pin. Right. So while you can drive, you know, you might have a 100-pin microcontroller, but you can't get 30 milliamps out of each one of those pins because you'll exceed the maximum ground or power pin current. Right.

**Chris Gammell:** And that's usually package limited or...

**Dave Jones:** And that's usually limited by the package and the bond wire going over from the one power pin you're using or something like that. Yeah.

**Chris Gammell:** That'll be an interesting tradeoff because I'm guessing you're going to have to go with a really small micro to try and get your costs. Well, not that small, I guess, but...

**Dave Jones:** Well, it's physically a small module too, so... Oh, okay. Yeah, I... So, yeah, that size... Yeah, I need a small... Yeah, it might be a... Yeah, I might even have to use the dreaded, you know, flip chip or BGA or something like that. Oh, God. God help me. See, I don't think that would get cheap though.

**Chris Gammell:** That would start getting expensive, I think.

**Dave Jones:** No, no, they're very cheap. Very cheap packages. They're generally cheaper than the dip and the QFK because they don't have to put the bond wires in then because the ball is directly on the back side of the... It's on the substrate or something. I think it's a cheaper manufacturing process. Don't quote me on that, but I think, yeah, that's one of the advantages of those chip scale packages and the BGA is that they physically less work to actually manufacture the actual package. Oh, okay. So...

**Chris Gammell:** I had thought that they were... I mean, dip is one thing, but I didn't think QFP was that much more, so... Right.

**Dave Jones:** Well, that's the same thing because you have an individual bond wire, so you've got to have the little robot arm that comes down and welds on each little bond wire from the pad to the pin and stuff like... It's like... It's fast, you know, the robot arm comes in... Yeah. But hey, you know, if it takes an extra second, well, you know, you add that up over time and, you know, you can only get, you know, 10,000 chips a day instead of, you know, 100,000. So, yeah, it all adds up.

**Chris Gammell:** That's good, man. That's real good. Oh, anyway, nothing about LEDs. Yeah. Well, no, it's, you know, that's really good. Okay.

**Dave Jones:** What else have we got? Next up.

**Chris Gammell:** Next up.

**Dave Jones:** Oh, well, you wanted to rant about the size of packages. Oh, yeah. Go for it.

**Chris Gammell:** Yeah. Well, I mean, I was actually, you know, I'm actually running out of room. I mean, that's a personal problem running out of room on a computer now, but the, you know, because my hard drive is only so big, but it was, I was going through uninstalling everything. And the, you know, I'm starting to see these packages being like three to four gigabytes. And it... Yeah.

**Dave Jones:** Oh, I'm sorry. I thought you were talking about chip packages, but you're not. You're talking about the software development packages. Yes.

**Chris Gammell:** Yes. Yes. Yes. Yes. So, like, FPGAs. Yes. I mean, FPGAs are usually a little bit worse, but even, you know, like, I was doing micro stuff for, like, for, like, free scale chips and, you know. Yeah. Just these huge, huge, because they have to pull everything in. And I don't get why they're not, they're not, like, on-demand kind of applications, you know? Like, why, why isn't it like, okay, I'm using, you know, an Atmel 328, whatever, you know? Like, okay, now I go out, I go to the web, I get all the latest software, and then I pull that down, instead of pulling down, you know, there's, like, this archaic system where they pull every single chip that's available, every board support package, all in at the same time. I have to wait, because I have a slow internet connection to get all down, then install it. It takes up, you know, some decent percentage of my computer, and then I'm screwed. You know, like, I start running out of room, and I have to actually uninstall then. So, it's ridiculous. I don't know.

**Dave Jones:** Well, first of all, you've got to step into the year 2000 and get a decent-sized hard drive and internet connection. But, you know, yeah, I know what you mean. And I work at a company that does this sort of thing. And, yeah, it's all one package. You have no real option. You download the whole thing. And I don't quote me on this, but I believe it's done because it's just easier to develop. It's easier to keep track of. It's easier to, when you generate the build every day, when you're in the software development process. I guess I'm not geeky enough to understand it all. But, yeah, but basically they build packages every day. And if you don't, if you keep everything separate as, you know, you've got a hundred different things you can download, I think that's harder to manage from a software development point of view. So, I think there's reasons why all these companies do it as one big build is the term, is the actual industry term for that. Right. A build. Yeah, I know. Yeah.

**Chris Gammell:** I'm sure there are some real reasons there. Yeah. It's enough for me to get angry because, you know, I understand the hard drive argument that's out of my control, unfortunately. But even aside from that, you know, like, these, I think they're very unwieldy. You know what I mean? Yep.

**Dave Jones:** Yep.

**Chris Gammell:** I don't want to knock them too much because they let me make stuff. But come on. Come on, man.

**Dave Jones:** Yeah, I know. Well, you know, it's the same thing with the EDA packages. Now, all I want to do is a schematic and PCB, but, oh, what I've got to install 3D, FPGA, micros, drivers, 10 million different libraries and, oh, you know. God, I just want to lay out a triple five timer on a board. I know.

**Chris Gammell:** Yeah. Yeah. Actually, did you, so you had posted a thing about the Amanda Wozniak's, was his video about hardware? Oh, yes. Did you get that quote in there? If you think Microsoft is bad, you haven't touched cadence?

**Dave Jones:** Oh, yes. Yeah, I saw that. That was awesome. I thought that was awesome. That was good. Yeah. Actually, we should talk about that now. It was something I wanted to discuss. I posted it on my blog because I thought it was kind of interesting and people, you know, might learn something from it. Yeah, this cool chick, Amanda Wozniak. No relation to the Woz, the Steve Woz. Right. She says that up front. Yeah, she says that up front. Yeah, she gets sick of, oh, are you Steve Wozniak's sister or something? No, daughter. No. Don't know him from Bar of Soap. And she did this video presentation at DEF CON or one of those hacker conventions. You know, I'm not sure which one it was. And it's called Hardware Will Cut You. And it was a 20-minute... Cut you.

**Speaker ?:** Yeah.

**Dave Jones:** Cut you, bitch. Cut you. And it was a 20-minute rant. It was quite good. It was like a PowerPoint slide, extremely fast-paced. She talks even faster than I do, which is bloody incredible. And she... Yeah, it was interesting comparing the hardware design process to the software development process or something like that. Yeah. And it was more targeted towards software people who wanted to get into doing Arduino stuff and encouraging them to get in. But, yeah, a lot of people commented that she was too crass and condescending. And there's lots of swear words in there, more than me. Yeah. She does drop the F-bomb a couple of times, which I try and avoid. I really do my best to cut the F-bomb out of this show and the live shows. Yeah. Well, that's good. So, yeah. But, yeah, she was, yeah, really full-on. And I thought it was kind of fun, but... Yeah, I didn't think it was that bad. A lot of people took offense.

**Chris Gammell:** I don't know. Well, yeah, I don't know. I got to hear Lamore's talk at the Open Hardware Summit. I thought, you know, very similar to that. You know, it was just like, she's just BSing with her friends. Like, I don't get what the problem is. And I think, I mean, like, other people were saying that, oh, she's talking down to people. I think she just knows what she's doing. I mean, she... Yeah. I mean, she sounded legit to me. I mean, she definitely knows the hardware process. She's experienced it. Oh, yeah. And she was showing that she was kind of pissed about it.

**Dave Jones:** Well, yeah, she kind of had... Everyone said, oh, she's got an axe to grind against, you know. But no, I think she just didn't want people to, you know, things are genuine. She didn't want people to experience the same crap she went through.

**Chris Gammell:** Yeah.

**Dave Jones:** During the hardware development process. And she just, yeah, speaks her mind, I guess.

**Chris Gammell:** Yeah. I really like, I mean, I like the content a lot. I thought it was very, you know, to the point. It was concise for the development process. So all of that stuff was good. And definitely my favorite analogy she made was when she was talking about, you know, software versus hardware. She's like, software, you know, you can make stuff at your desk. You can do a build from scratch or whatever. And, you know, you can do it in a day or whatever. And she explains that that would be like writing a program, sending it on your grandmother to on index cards or something like that. And then a knit is a zero and a pearl is a one. And then later she's... A pearl is a one.

**Dave Jones:** And then please knit me this program. Oh, it's brilliant. And it takes you a month.

**Chris Gammell:** Yeah. That's a great analogy, I thought. It's very good. Yeah.

**Dave Jones:** Yeah. So there was some good stuff in there if you get past the, yeah, the swearing and everything else. So, yeah. Yeah. I don't know. But, yeah, a lot of people seem to take offense to it. Well, you know, each to their own. As I've learned, you can't even please a minority of people. So don't even try. Just be... Just do what you want to do and be yourself, basically.

**Chris Gammell:** Maybe one time we should have an episode of The Amp Hour where it's all like sweet. And then you place a resistor. Oh, don't worry if it blows up. Yeah. Bullshit to that. Yeah. Right. Screw that. Yeah. Yeah. So I like that. I'm glad you put... Where did you find that? Did you see that on Adafruit or where did you...

**Dave Jones:** No. Somebody posted on my forum. But apparently it was on Adafruit and all the other blogs as well. Yeah. Apparently I'm a week late. So... Yeah. Yeah. Because I don't have enough time to follow all these blogs.

**Chris Gammell:** You know, I feel like lately I could just follow Adafruit because they... I mean, they've been getting up a lot of content lately. So... Yeah. It's them and Make. I mean, I've been following them. And actually I posted something about those two. I just saw it recently, just today. They're having a design contest. Do you see that? Yes. Buy, break, and build. Or I guess buy, break, build. And it's actually going to be hosted on Hackaday. And then it's sponsored by Adafruit and Make. Like, Adafruit is supplying the prizes. And I think Make might be as well. Yeah. And basically what you do... It looks awesome. You take one of those dancing Santas. You know, it's like playing Jingle Bell Rock. Yeah, they make, right. Yeah. Those little... They got like motors inside. Yeah. Super cheap stuff. You know, a little tiny control chip, whatever. And so you know someone's going to be circuit bending on that kind of thing. And someone else will drive something else. But they have different prizes based on what you take out of the Santa and then make into something else. So I think it's a really cool idea. I mean... It's very cool.

**Dave Jones:** Just don't get too excited over the prizes, kiddies. I think it's like a minty boost or something like that. I mean, it's for the fun, I think. It's not major. No. But Adafruit have another major design contest, which I think somebody's close to winning, which is $2,000 first prize. Oh, the Connect prize. For anyone who can tear down... Sorry, anyone who can release open source drivers for the new Microsoft... Yeah. I can't pronounce it. I forget how to pronounce it. The little 3D... Connect. The Connect. Yeah. Yeah. Or something like that with a K. Yeah. With a K-I-N. K-I-N Connect. Yeah. Fancy spelling. Yeah. I think someone's very close to doing that. Now, I just had a fleeting thought yesterday after I saw that. I thought, well, I hope Microsoft doesn't sue them because here they are encouraging people to affect... Giving prize money for people to break their technology, basically. So, yeah. I don't know. No.

**Chris Gammell:** Well, you know, they were talking about... I was listening to Ask an Engineer yesterday, which is their Saturday program. And they were talking about... And they make a really good point. You know, Phil Taron was talking about it. He said, you know, we... There is nothing against... You're allowed to do whatever you want. It's your piece of equipment. You know what I mean? You're allowed to do that. Yep. So, what were two people?

**Dave Jones:** Well, there are lawsuits. Well, no. I think there's a recent lawsuit, which... I might have been here in Australia, but it has implications anywhere in the world. It basically... Against these game console modding chips, right? And basically, the mod people lost. The court said, no, basically, you don't have the right to mod that console to get around the actual software protection built into that console. You don't have that right. And it was made big, big news several months back. So, yeah. I don't know. The lines are still blurred on that, I think. So, don't underestimate the power of the blood-sucking lawyers.

**Chris Gammell:** I was going to say, I think that's a load of crap. I think that... Oh, yeah. Totally. Oh, yeah. Totally. If I'm paying money for something, I'm allowed to smash it into a brick wall if I want to. And I'm allowed to open it up, and I'm allowed to use it however I want to. Now, if you want to hit me later, if I'm doing modding, and then I go and download an illegal game, and then I use it for... And that's why I need the modding. Yeah. Then the illegal act there is the downloading of an illegal game. Well, yeah.

**Dave Jones:** I think you're allowed to personally do it in your own home. But as soon as you distribute the information, then you become liable. Or something like that. That's the whole idea behind this mod lawsuit, which the game... I think Sony bought it in. You know, Sony started suing all the people selling these mod chips. And they... Yeah, basically, you didn't have a right to sell this mod chip, I think, was the end result.

**Chris Gammell:** See, now, that's different, though, too, because you're selling a product... If you're selling a product where you actually are selling like a... You know, if you sell a radar jammer, right? I think that's the same kind of thing, right? So you sell a radar jammer... It's illegal, yeah. Yeah, it's illegal, right? To sell them. But if I go out and I make a radar jammer, that's all on me. You know what I mean? So I think it's the fact that they're selling the chip. That's the part that's illegal. Not that people are doing it. So...

**Dave Jones:** Yeah, I think so. But yeah, from what I read, the lawsuit... Yeah, the judge said that basically, no, you don't have the right to do it to your console. I think that was the big uproar over that. Oh, okay. Anyway, let's not... Yeah, let's not harp on that. That's not really our domain. Yeah, it's bullshit. I know. So...

**Chris Gammell:** I think it's great to do it, though. I don't like it. Oh, yeah, it's great. Have you seen the thing in action, the games?

**Dave Jones:** No, I haven't. No. I saw it on... But yeah, they can track your movement in real time, 3D. Yeah, it's really cool. So you don't need a hand controller anymore. You just wave your hands around.

**Chris Gammell:** Yeah, it's really great. I think it's a great idea. Yep. So... Awesome.

**Dave Jones:** And yeah, I think some guy's very close. I saw some video of him. You know, there's like this figure and he pulled out the video and... Yep. Yeah, he was actually, you know, he stood in front of the camera and it tracked his hands and his feet and... Yep. Awesome work. So... And it was within a day of them posting up the contest or something. This guy had done it.

**Chris Gammell:** Yep.

**Dave Jones:** It was like crazy.

**Chris Gammell:** Yeah, it's great. Oh dear.

**Dave Jones:** And we have a discussion point. Now, where do we draw the line between scientist and engineer? You wanted to... You added this one. Go for it.

**Chris Gammell:** Well, I was hoping you would answer that, Dave. Oh, right. I was... Right. I mean, I have thoughts about it, but I don't know. Like, you know, like, I think about it like on... So your favorite show, right? The Big Bang Theory, right? Yep. The one guy is an engineer, but, you know, they're all nerds, right? Yeah. And what is that line, really? I mean, the fact that he's... You know, and even in schools, a lot of times that line is blurred. You know, there's people getting a PhD in engineering. Well, what's the difference between that and a PhD in science? You know what I mean? I know there are actual differences, but...

**Dave Jones:** Well, I always make the difference that, you know, science and scientists are at the academic level, so to speak. They can be at the practical level in there. There's your scientists, you're producing drugs, but I sort of more associate science with the, you know... You know what I mean? Drugs?

**Dave Jones:** Drugs.

**Dave Jones:** Only drugs. You know, like if you're, you know, scientists working at it.

**Dave Jones:** You're making drugs. That's it.

**Dave Jones:** You're making drugs. That's it. Well, you know, but I see it as, yeah, the scientist is more academic. They do theory research, and the engineer does practical implementation side of things. I know it's totally, you know, they're all totally blurred, but that's generally how I see it. Right.

**Chris Gammell:** Yeah. But I mean, like there's... I don't know. Is that right? I think that is... That's a great explanation, but I think then, you know, I think about people I know that are doing PhDs, right? And basically, you know, they're doing a PhD in mechanical engineering or electrical engineering, and at the end of the day, they're basically doing... They're scientists. You know what I mean? Like, they don't call it that because they're focusing on a certain discipline, but it's... What's the difference, really? You know, you're getting grant money. You're going out. You're forming hypotheses. You're testing hypotheses. And maybe the difference is you're making something in order to test them versus, you know, doing theoretical...

**Dave Jones:** Well, that's the thing. As a scientist, you're more working, or as a PhD researcher, be it engineering or science, you're working at more at the fundamental physics level or at the, you know, a more fundamental level than engineering is a higher, more abstract system level thing. You know, you take the stuff that the scientists actually produce and you do something practical with it. That's, you know, I don't know. The lines are too blurred. We probably shouldn't even talk about it, really, because we're just ultimately going to be wrong in some way, shape, or form. Yeah.

**Chris Gammell:** Yeah. Well, I mean, I had Mythbusters as an example, right? So, I mean, those guys are... Mythbusters, yeah. They say they're doing science, but, like, those guys are making stuff every day. You know, they're testing out hypotheses by making cement trucks blow up.

**Dave Jones:** To me, that's engineering. I mean, yeah, right? It's using scientific principles, but it's not science. It's me. Right, scientific method, right. They're doing, you know, junkyard engineering, just cool backyard engineering.

**Chris Gammell:** Yeah. So, I don't know. It doesn't matter, really. I just... I thought it was an interest... No, no, it doesn't. I don't even remember when I wrote that. I was just thinking about it and... Right, and it popped on the list, huh? Yeah, it got on the list. I was thinking so many tech subjects last week. I was like, I gotta get something!

**Dave Jones:** Yeah, because it was... Yeah, the list was looking a bit slim there for a while. Yeah, it was last week, yeah. Oh, dear.

**Chris Gammell:** Well, speaking of engineering, let's hear about your scramble. I mean, you were talking about that earlier with the LED boards, but... I mean, if you're an engineer, I'm sure scientists do it, too. No disrespect. But, you know, if you're an engineer, you probably had the 11th hour scramble.

**Dave Jones:** You probably have. It's happened without fail at every company I've ever worked at, even on my own projects as well. Not so much, because, you know, I can go, oh, I don't give a shit, I'll do it tomorrow. But, yeah. Yeah, the 11th hour design scramble where, you know, in my case this week, I had to make a deadline for a trade show. So, it's a fixed deadline. You know, you have to produce this product. It has to be, you know, there at 10 a.m. on the trade show stand. Wham! You know, that's it. There are no, you know, it's either all or nothing. You have to do it. Yeah. And for somehow, we always seem to do it, you know? And in this case of the RGB boards, which had to be at this trade show, and I want to know how we're able to do this. Are engineers more productive under extreme pressure? I think they are.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** You know, and because, yeah, I had a week to produce this board from nothing. It was, you know, basically, we had to produce it, populate them. We had to build 20 of them by hand because, you know, we only had like 10 days or something. So, we couldn't send it out to be contract manufactured because it takes five or 10 days just to arrange that. Yeah. Let alone do it. So, we had to build 20 of these boards in-house. We had to design the PCB, lay it out, get it manufactured overnight in Taiwan because we couldn't find a local manufacturer who would do it quick enough. Wow. Because it's all, you know, if you've done the Gantt charts and you know that, well, you can't build the board unless you physically have it. So, you know, that process has to come after the timeline of building, you know, getting the board manufactured and then you've got delivery. How long does it take to, you know, get here from Taiwan? And, oh, and so, but yeah, and we did it with time to spare in the end. So, oh, I don't know. It's just crazy.

**Chris Gammell:** Well, then, if you did it with time to spare, how is it 11th hour? I don't get that. I mean, you just mean like short timeline?

**Dave Jones:** Oh, well, it's a, well, it's just a short timeline. I mean, I've done ones where I've actually been on the trade show stand actually hooking stuff up, getting ready. People are walking through the door and we're literally finishing it with minutes to spare. Don't look, don't look, don't look. Yeah, it's like we're hoping that it'll take people time to get through the doors and get to, you know, the other side of the hall before we actually finish this thing.

**Chris Gammell:** You always bring the basket of emergency muffins to distract them. You're like, oh, and we have muffins over here.

**Dave Jones:** That's what the hot chicks are for in the hot can. They'll gravitate towards those stands first before they get to you. And yeah, that's how, you know, that's how 11th hour it could be, you know?

**Chris Gammell:** You actually hire the hot ladies for other stands so they'll actually stay away from yours when you're not finished.

**Dave Jones:** Exactly, they'll stay away so we can screw everything together and get it bloody well working. I don't know. But it's, yeah, it happens. Every, every company does this, be it for a trade show or something else, you know? Yeah. They just put in these ridiculous deadlines. You must be finished by this day. And, you know, but if, if we were, if we couldn't get that PCB manufacturer to manufacture that board within 24 hours for us and ship it out, we were screwed. Yeah. You know, the whole thing, I, I probably would have had to resort to making those boards by, by hand and they would have looked shit, you know? They would have been a crap and they wouldn't have even been a tin plate thing. I could have run solder over all the tracks to tin plate it maybe, but, you know, it would have been really crap looking and.

**Chris Gammell:** Yeah. It would have been like Sharpie, Sharpie etched and everything.

**Dave Jones:** And if, and if any one of those little processes didn't come in, if we couldn't get the parts in time or whatever, then, you know, you're screwed. But somehow it all always seems to work. You always seem to find a way.

**Chris Gammell:** Man, that's pretty good. I mean, I guess, I guess the, there's two things that are, I think the one thing that, that allows it to work more often than not is the, the global marketplace in that case. I mean, the fact that you can get it fabbed in Taiwan overnight, that's, that's kind of ridiculous.

**Dave Jones:** It's, it's pretty, yeah, I know.

**Chris Gammell:** You know, I don't know about 20, 30 years ago. I don't know if that would have happened just because you would have had to find a local guy, then you would have had to squeeze it in or, I mean, you probably still paid through the nose for that, right? I mean, that's usually the trade-off too.

**Dave Jones:** Oh, yes, yes. We, yeah, we paid big, big money for those blank boards, you know? Yeah. Yeah. So, I mean. Yeah, it's crazy. But I think it comes down. I think, yeah, it's that. And the, I think, you know, a good engineer is capable of just doing the timelines in their head, knowing that, oh, shit, you know, I know we have to push the button today on that board to get it, you know, in time. And you just know how long things instinctively take. Yeah, that's an experience thing. Yeah, it's just, and it just all comes together. And you know where the key points are. Like, if we don't get this board, well, the whole thing's off. So. Yeah, exactly. You focus your energy on getting that board. And then you, you know, you know, okay, the parts are relatively easy to get. And if we can't get them, I can find substitutes and, you know, all that sort of stuff. So, or we can make do, or we can salvage parts off old boards, or we can, you know. Yeah, so that, so the parts might not be as important as the bare board, for example. So, you know where your priorities lie. Right. That sort of thing. So, but, you know. Yeah, it all seems to happen. And you don't do Gantt charts for this thing, and you don't have meetings. You don't sit down at a meeting and do a Gantt chart of, okay, we need this board by this. Some companies do that, but, geez, you spend more time doing that than actually making it happen. So. Right, yeah.

**Chris Gammell:** You know, I've actually studied some of this stuff before.

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** Right. So, you know, like you were asking about, like, why does it always work, and why doesn't this happen on regular projects, right? Yep. And so, and I mean, it's been out there before, but like, or it's been out there for a long time, but like, just the iterative design model, there's actually like a whole ton of stuff about that now. And I've been studying some of that stuff with my coworkers about like, you know, basically you try and time box yourself. So, like, instead of saying, so, so like, say you have a project.

**Dave Jones:** Time box. There's a wank word. Yeah. Time box yourself.

**Speaker ?:** Yeah, it is.

**Dave Jones:** Sorry, I haven't heard that one before. That's quite novel.

**Chris Gammell:** Well, you might hear it in the near future. Who knows?

**Dave Jones:** Right. Okay.

**Chris Gammell:** Chris Campbell management method from a guy who's not a manager. Yeah.

**Dave Jones:** Green belt. Oh, God. Yeah. Yeah, I know.

**Chris Gammell:** But the idea is, you know, it's very, very intuitive once you start learning about it. But like, you think about like a project, right? So, so you go out, Dave, and you say, okay, I'm going to make a RGB module, but it's going to be, it's going to be 20, 20 meters by 20 meters. That's right. I put that in metric for you. Okay. So it's going to be huge and you need to figure out how to do that. Right. And so you, you have, you know, you together with your whole team and you say, all right, we have a year to do this. Right. And at the beginning of it, you know, the first thing you're going to start doing is what's that besides, you know, figuring out your project plan.

**Dave Jones:** Oh, you, you figure out the, the, the system, how the system's going to work.

**Chris Gammell:** No, that's not true.

**Dave Jones:** I get straight into the engineering.

**Chris Gammell:** That's wrong.

**Dave Jones:** That's right for me.

**Chris Gammell:** That's wrong. Nah. Nah. You know what you're going to do at the beginning? You're going to do nothing. You're going to do nothing because it's a year away. You know what I mean?

**Dave Jones:** Well, well, I was about to say that because you put in like, it's a year. The last thing you should do is say, we've got a year to do this, guys. Exactly. You should say, we've got till the end of the month. Yeah. You know, and then the pressure's on. So that's kind of the whole idea. Exactly. And you become more productive. Right.

**Chris Gammell:** And that's the same idea here. I mean, you're productive because there's like a very well-defined date, right? And so this whole system I was studying was like, you start pushing in those dates to like two-week increments or something like that. And then, you know, at the end of two weeks, you have to have something done. And maybe you don't, I mean, either you're self-motivated or, you know, you got to, you know, show it in front of some other people or something like that. But there's, there's a very definite date. And there's actually like studies out there about like how that can actually push together projects a lot more efficiently and, you know, like predictably. Yep. So I don't know. I thought that was cool.

**Dave Jones:** Well, it's, well, then it becomes organized chaos if you're trying, you know, if you, if the dates are too small, you know, if they're too compacted, if your time box is, is actually too small, then, you know, it just becomes chaos and engineers go crazy. And, you know, well, yeah, I think, I think two weeks is okay. There's fistfights in the corridors and there's, you know, people quitting. I think every day would be tough, right?

**Chris Gammell:** Because then it'd be like. Well, yeah, exactly. You've got to have something done by the end of the day. Yeah. Three o'clock, got to go show my manager what I did. That would be like preschool, right?

**Dave Jones:** That's called micromanagement. Yeah. Yeah. That would suck. And it pisses every engineer off. No engineer likes to be micromanaged.

**Chris Gammell:** No, definitely not. I agree. No. And if they do, they're probably not doing it right.

**Dave Jones:** Exactly.

**Chris Gammell:** Yeah. But I mean, I think it's just kind of getting to that, like kind of pushing yourself for a very fixed deadline. And I won't, I won't say the T word again. I promise that the wank word, as you said, but you know, I think it's, I think it's a cool idea. I mean, and, and, and stuff I've seen that kind of, kind of verifies that, that it works. So, and I mean, I've done it myself too. So I like it.

**Dave Jones:** Yeah. And it does work. And yeah, engineers are more, are more productive under pressure. Otherwise we're, I think we're probably inherently a bit lazy. You know, because we'll, we'll, we'll actually do the fun stuff and then you won't want to do the hard work, you know, cause you'll want to continue to do the fun stuff. So yeah, you'll just, you know, all that hard work you'll actually put off.

**Chris Gammell:** Right. Yeah. I mean, it's like, so say you're going out to make a board, right? And I want to talk about boards today too, but what, what's the fun part there? You know, you want to go out and you want to just go start doing layout, you know, you want to put down some parts and start doing layout and get it done and get a board and start building it. You don't want to go do part research and you don't want to go figure out the most cost effective option or anything like that. You just want to do it and get it done. But sometimes you actually have to do that other stuff.

**Dave Jones:** Yeah. Because the most important thing might be the cost of the board, you know, that might be your number one requirement.

**Speaker ?:** Yeah.

**Dave Jones:** So these days it seems to be great. You know, I've got to spend a month researching parts. Great. Yeah. And then by the time you finish that, they're all out of date and they can't get them anymore. Yeah.

**Chris Gammell:** I was complaining about that this week too on Twitter about the, uh, the costs of small volume boards and I'm making, I'm making this board that's probably like, you know, two and a half square inches. And, uh, it's, it's so expensive, you know, like hundreds of dollars a board.

**Dave Jones:** Rubbish. Go to PCB card. It's 50 bucks. Yeah. Who are you using for that sort of price?

**Chris Gammell:** That was, that was sunstone. I don't know. Sunstone was pretty good.

**Dave Jones:** Yes. No. How many layers do you get though? No, they're fairly expensive. Go to PCB card and a board that's only two inches by two inches will cost you, um, is it like a four layer, two layer? How many layers?

**Chris Gammell:** Four layer with, I need, I need solder mask and, and, uh, yeah, well that's obvious.

**Dave Jones:** A four layer board will be 60 bucks tooling cost. I think plus maybe $10 each for the board.

**Chris Gammell:** Um, how fast does that go though? That's the other thing.

**Dave Jones:** Oh no, that's a 12 day turn for a four layer board. They will do eight days for, yeah, exactly. Yeah. So that's the same board. If you want it one, one day in Taiwan, like we got, you know, it's, you know, a thousand dollars. Yeah. Yeah.

**Chris Gammell:** I mean, it's, and it's always the trade off, you know, I wanted a two day turn and like that, uh, well that kind of stuff gets up there fast. I mean, like, I don't know. I, I like it. I, I like the, the fastness of it, but yeah, you know, like you got, you really got to pay for it. So I mean, and if you, and if you really have the time, you can go to like, uh, me and Jeff talked about with, uh, lane, the PCB.lane.org. We talked about that and he bundles the designs together and that's going to take months. But I mean, if you got the time, I think it was seven bucks a board or something like that.

**Dave Jones:** So yeah, that's great. Well, actually this isn't on the, uh, yes, this brings me into a point. I did have it on the list. Uh, free samples. Um, I just wanted to do a quick, I was going to do a drive time rant on it, uh, this morning actually. I most likely will, but, um, yeah, I mean, everyone craps on about free samples now. And I, I used to use free samples extensively back in the day with Maxim and other companies that do great free samples, but there's lots of, there's lots of negative reasons not to get free samples. One, it takes, it generally takes a fair amount of time. You know, you won't get your parts, you know, you won't get them within a day or two, which is what you want. I don't know, man.

**Chris Gammell:** I get some pretty fast parts.

**Dave Jones:** Oh yeah, but it's not as fast as getting it from Farnells, you know? Well, yeah, it's different. Maybe it's different in Australia, but, and often the, um, to get the samples, you might have to go through a local distributor or something. Once again, this might be an Australian thing. You go through a local distributor and they want to know all your details. They want to know what project you're working on, how many are you going to do and all that sort of shit. And it's like, and they phone you up, you know, later, can we help you? And, oh God, I just wanted two chips. Yeah. You know, leave me alone.

**Chris Gammell:** You know, you know why that happens though, is because they got to tie it back. And I mean, that's like the whole, that's like the sales versus engineering thing, right?

**Dave Jones:** Like they want to funnel people and blah, blah, blah. Yeah. So we just want to party.

**Dave Jones:** Yeah. I know. Exactly. And, and, and the other thing is, yeah, you may get free samples. Great. But can you get them when you go into production? That's the thing. So, you know, I, I, I know people who design everything using free samples, entire board and they build their one board. Great. Look, it didn't cost me anything, you know, or it cost me very little, but they're all free and they won't go, okay, we now have to make a hundred of these. Oops. No, I can't get those. Any of those chips because, you know, they were some obscure part that they got for free. Yeah.

**Chris Gammell:** So you'll say you'll, you'd rather go to like a DigiKey or a Farnell.

**Dave Jones:** I'd rather go DigiKey mouse. Well, Farnell's in Australia. It, you can order one, one single resistor that, that costs a cent and they'll deliver it to you for free. Nice. So there's no advantage. You know, if you want a chip, I can have it same day for a dollar from Farnell's rather than going through all that rubbish to try and get a free sample from the manufacturer. It could take a week or more. You know what you should do? With all the crap that goes along with it.

**Chris Gammell:** Next time, next time Farnell pisses you off with their credit card policy, you should put in, you should put in four different single resistor orders in a day and keep doing that until they respond. You know, we, why, why did we spend $800 on shipping resistors to Dave Jones? I don't get it. Exactly. Oh, he was angry. He was angry. Sorry.

**Dave Jones:** Yes. Anyway, they, they actually apologized. I got a phone call from the head honcho and yeah, they apologized about it. Oh, yes. Well, they said they'd fix it last time, but yeah. Yeah. So I take that with a grain of salt. Anyway.

**Chris Gammell:** I like your idea though about the, I mean that, that, I mean sometimes you just got to like, you know, that, that kind of theme pops up over and over again. You know, you got to pay for quality. In this case, you got to pay for just the assurance.

**Dave Jones:** No hassles or just the assurance that you're going to have the parts, you know. Exactly. Yeah.

**Chris Gammell:** And that makes sense, especially if you, if you have like the system set up to get it really quickly. Now, if you have to go through a whole process to get a part. Oh, no. That's a little different, but I mean like.

**Dave Jones:** Yeah. Well, some companies I've worked at to buy that, that one resistor from Farnell's, you know, you've got to go and get and raise a purchase order and get it signed by three different people and it's all going to be in triplicate and yeah, then it becomes stupid. Yeah. Right. But now, you know, I've got my own company credit card. I just whack it in and you know, the parts on my desk within, you know, a day or less. Yeah. That's great.

**Chris Gammell:** That's really great.

**Dave Jones:** Yeah. Yeah. Well, that's, that's the other thing, you know, an engineer can be so productive companies out there. If you're in, if your design engineers don't have a credit card, well, bloody well, give them one. They'll be 10 times more, more, more productive. I guarantee it.

**Chris Gammell:** I love that idea. I was, I was trying to pitch that to my company and, and they didn't, they weren't going for it. I think sometimes it's an accounting thing too, but like. It is, but you know, like. You've got to trust your engineers. So I mean. Yeah. And that's, that's another like a management. I don't know why the hell I'm looking at so much management stuff. I'm not going towards management, but like, that's another thing. That's another thing they talk about though. Like you push it. And that's a Toyota thing, right? You know, you push your stuff down as far as you can down the chain. You know, if you have a guy that's turning a wrench and he needs another wrench, he should be able to go get another wrench. You know, if he has to go talk to the VP in order to get a wrench, you're never going to get anything done. So.

**Dave Jones:** But that's how it is in some big companies, a lot of big companies. Yeah. Most companies I've worked, most engineering companies I've worked at work with that big company mentality. You know, every, you have to be accountable for every last cent and you know, it's just stupid. Yeah.

**Chris Gammell:** And if there's any managers listening to this, I don't know if there are, that's the thing. I don't know if any of our listeners are managers, but if you are and you don't want to let us know who you are, just let us know in the comments that you're listening as a manager because I'd be interested in that. You don't have to say who you really are. Don't troll us, please. Don't pretend you're a manager. But if you really are a manager, I'm interested in that because I don't know. I don't know who listens. I mean, we have some people that listen or we know some people listen because of that survey, but I don't know.

**Speaker ?:** So.

**Dave Jones:** Yeah. Managers. I have no, I'm just assuming not, you know, because managers don't. Give a shit about practical engineering. Oh, that's not right. Shows like this or blogs or they don't, you know, because they're professional, you know, I don't know a single manager who's actually like a real manager manager as opposed to just a token manager who's actually a real engineer, but a real, you know, a manager's manager, you know, he's got his MBA and everything else. The ones, I don't know a single one that actually goes out and actually takes an active interest in electronics and engineering, you know, outside of, well, work is management to them. It's not engineering and technology. It's.

**Chris Gammell:** Really? Yeah. I mean, my. I don't, I don't know any of them. I know at least one manager who's very active on the side. He makes his own boards and stuff. Yeah. I don't know. I think, I think it happens. And so.

**Dave Jones:** I'm sure it does. But yeah, I think it's fairly rare. It's more the exception than the rule. That's for sure. Yeah.

**Chris Gammell:** I think, you know, once you start getting up into this, I never really knew what management was when I was like, you know, getting started and stuff. Yeah. But I realized it's a lot of like, you know, because they take care of projects and they kind of make sure things are going right and if people need help and they always say that. Well, that's what they're supposed to do. They don't always do that. Well, okay. Yeah. Okay. So, so best case, but I mean, they always, well, you ask a manager what they do and they say, oh, well, I remove barriers. I've heard that a couple of times before, right? Yeah. Right. And then, yeah. So whatever that is, right. But what it really is usually is, is budgeting. You know, you got to figure out where's money, money's going and like that.

**Dave Jones:** Money and people. You have to budget people as well. You know.

**Chris Gammell:** People are money though too, because that, I mean, they, people translate to money. So I think a lot of times that's, that's usually what ends up management being, you know, like you kind of just making sure that the money, the numbers add up. So I don't envy them.

**Dave Jones:** Time, money and resources. They're the three keys to management.

**Chris Gammell:** Yeah. I don't envy them. Not at all.

**Dave Jones:** No, no, it's a shit job. Yeah. Anyway, just, yeah. Give them, give them credit cards, chaos, and we're much more productive. Exactly. Right. It's easy. You don't have to do anything as a manager. The chaos model. Give us the freedom to do shit and we'll, we'll do it.

**Chris Gammell:** So yeah, it works every time. Just hire Dave. He, it works out great.

**Dave Jones:** Don't, don't worry.

**Chris Gammell:** Just hire Dave.

**Dave Jones:** And I'm just going to tell you you're a dickhead and you add no value to the company as a manager. So you may as well not exist. Just. Oh, that's not good. Exactly. Hey. Eeks. Oh dear. Yeah. No, I know.

**Chris Gammell:** So I want to talk about, I wanted to ask you about some, some layout stuff before we end because. Oh, right. Okay.

**Dave Jones:** Oh, how much time we got left? I think five, five, six minutes.

**Chris Gammell:** Five minutes. Let's go. All right. So, so you've been doing layout for a long time.

**Dave Jones:** No, I've been doing layout for 20 years more.

**Chris Gammell:** Long, long time.

**Dave Jones:** I used to be a full time PCB designer. Yep.

**Chris Gammell:** Yeah. And you know, I've done a couple boards, not, not a lot, but, but like, where do you start when you start a board? I mean, I don't know. I know you've done some, some EEV blog stuff on this, but, but like mostly I'm always kind of, and I was talking with, oh shoot. I forget who it was someone on Twitter about, about ripping up boards and stuff like that and how you have to always start over and just planning and stuff like that. And yeah. And the planning, it seems like that, that's just like the most critical thing that always gets skipped. So where do you start?

**Dave Jones:** It is the most critical. Where do I start? Well, you've got to, you know, step number one is to ensure you have a proper schematic and it's finished and it's, and it's got the design notes on there that you want. Like, oh, this pin must be star grounded over to here and stuff like that. You know, you've got to plan all that stuff and it's got to be on the schematic and then you have to ensure that you have all your footprints right. And you have your, you know, them, all your library components are correct. And then you dump it once all that's, you know, you might spend a month doing that.

**Chris Gammell:** Yeah.

**Dave Jones:** But if, if that's correct, you know, that's, that's probably, you know, a good half of your work done and then you dump the components onto the PCB and you group them. That's the other thing. You don't just start, you don't try and place all the parts at once. You do little subgroups. Okay. I've got an amplifier. Well, it's an, you know, it's an op amp with a bunch of passive components around it. You group those together. You route those in a little block and you do everything building block style and then you move the blocks together and, you know, but it's.

**Chris Gammell:** Man, that's the boring part too, isn't it? I mean, like not the blocking, but the upfront stuff, that just sucks, you know?

**Dave Jones:** Well, Ed, the, the old adage is that designing a PCB is 90% placement. Yeah. If you've got good component placement, the routing, you know, is easy. Almost, you know. Right.

**Chris Gammell:** Because then you don't have to do all the super jump through four layers and scoop it back up. Yeah.

**Dave Jones:** And you don't have to run signals from one corner of the board to the other and stuff like that because you laid it out and modular and, you know. Right. Same with your schematics as well. Your schematics are supposed to be organized logically. So the signals flow usually from left to right. Yeah. Some people might do it from, or, or, you know, cause if you do it, the Bob Pease style, I don't know if you've seen Bob Pease's schematics. They're just, they go left, right, up, down, diagonal. They're all over the shop, you know? Yeah. There is hand-drawn schematics and they're a mess. They're not, they don't have a logical flow or a logical block separation to them.

**Chris Gammell:** So yeah, I haven't seen them, but I've seen similar schematics before and those are just like, cause you're so used to it too. And then you start seeing like signals coming in from all over the place and you, and you just start scratching your head. Like, I don't know, I don't know what's going on here, but my friend actually has a really good technique for that actually, where he, uh, he takes highlighters of different colors and he tries to separate all the signal lines and the power lines and the grounds. And then when you look at it, as long as you're not colorblind, apologies to those who are, uh, you know, you have a really like block view, you know, like you don't think that a signal line is now a power line. So that's actually kind of a fun tip for people if they have a lot of highlighters laying around.

**Dave Jones:** Well, yeah, you're, well, that's the old way to do it. A lot of the days these, the EDA tools you're using will take care of that for you. You know, they have a modular bus approach and you can, you know, do lots of graphical stuff on there. So they can draw boxes around things and, you know, the analog, yeah. Analog, very analog. Analog, right. Yeah. On the back of a napkin. Yeah. Yeah.

**Chris Gammell:** I mean, I deal with schematics that are like old, man. I've, I've seen stuff that's in some old CAD packages that don't even exist anymore and that just gets messy. Yeah.

**Dave Jones:** But yeah, PCB design and layout is an art. Oh yeah. You know, it, it really is. It's not something that you can easily teach. Um, you know, experience must, you know, will ultimately teach you the most efficient way to do it. But yeah, you know, but the same, the old adage again, if you give the same design to 20 different designers, they'll give you 20 different layouts. Oh yeah. There's no one right way to do it.

**Chris Gammell:** That's good.

**Dave Jones:** Every, every layout is going to be different. They'll place the parts differently. They'll route it differently. They'll have different thought processes. Yeah. Oh, I couldn't even start to discuss it. Don't want to get you started on that. But yeah, I might try and do it. Everyone's, everyone always asks for that. Do a blog on how, how I lay out boards properly. And oh, like, geez. Yeah. I mean, it's almost to the point where it's like trying to teach painting, you know? Yeah.

**Chris Gammell:** Yeah. That's a good, that's a good analogy actually.

**Dave Jones:** You know? Yeah. Okay. How do you teach it? I don't know.

**Chris Gammell:** Do you know who Bob Ross is? Do you know who that is? Bob Ross? No, never heard of him. He was on the public broadcasting in the US. And he had this huge afro. And he would, he had the softest voice. And over here next to the mountain, happy trees. We're going to have some little happy trees. So Dave, if you could find some videos and do that for next year at Halloween, that would be the funniest thing I'd ever seen, I think. You know? Right. Happy trees. Happy resistor trees. Happy ground trees.

**Dave Jones:** Oh, no, that's, that's too happy missionary fairy for me. No, no, no.

**Chris Gammell:** He's, it's so great. I used to watch that when I was a kid. It would be like, you know, I'd be homesick and I'd be watching that on PBS in the afternoons and just like watch him like he'd do these paintings from, from scratch. It was great. So I think you should do that. If you're going to do it, do it that way. It'll have a lot of flair. All right.

**Dave Jones:** Happy trees. Oh, God.

**Dave Jones:** No, no, no. I couldn't, I couldn't bring myself. Couldn't be. Oh, come on. Oh, well.

**Chris Gammell:** Maybe I'll have to do it. Not to worry. Yeah. Well, before we go, let's mention Carl's documentary real quick. I think that's, that's coming out soon, right? Oh, yes.

**Dave Jones:** Carl's doco. Yes. The Australian electronics documentary, which we mentioned last time. It was originally supposed to be just a single doco, but he's interviewing so many darn people now getting so much historical, valuable historical information that he's going to turn it into a three-part doco, which basically spans timeframes. That's what he's thinking. Oh, cool. And then up to 1980s and then 1980s onwards. So, you know, and how things have changed, how the Australian Elishon is, it's still Australian specific kind of thing, but it has parallels all over the world. So, yeah. Yeah. It's just going to be so awesome.

**Chris Gammell:** Because, I mean, I only have limited experience in mainly like you and John Oxer and John Boxel from Tonic stuff and, you know, just online stuff.

**Dave Jones:** Well, John Oxer's in it, actually. He's in the doco. Yeah, I saw that. Yeah.

**Chris Gammell:** That's great. That's really great.

**Dave Jones:** And, yeah, it's going to be fantastic. He's got so much material. He could release a six DVD box set of, you know, this thing. Seriously. And one person would buy it. Well, no. I reckon he'd sell hundreds of them, actually. I think it'd actually be quite popular.

**Dave Jones:** I just meant that much length. That's a lot of length. That's a lot of geek watching. Yeah. Yeah. Anyway. Yeah. So, that's... And he's hoping to release another trailer shortly. So, that will go up on my site, as per usual. Great. Great. I can't wait to see it. Yet another teaser. So, yeah. It just keeps finding people because he talks to someone. They go, oh, you should really talk to this guy. Yeah. You know? And then he goes and he's flying all around the damn country interviewing people, you know?

**Chris Gammell:** That's great. That's awesome.

**Dave Jones:** That's fantastic. Yeah. And there may... Well, no. I won't talk about it. But we're thinking about an official premiere and all that sort of stuff as well. Oh, cool.

**Dave Jones:** Cool.

**Dave Jones:** And red carpet. If we can maybe get something like that happen. Yeah. Here comes Dick Smith. And here comes Dave Jones. And here comes Leo Simpson.

**Chris Gammell:** If you guys need me to announce on the red carpet, I'm willing. I'm willing to fly out there. Okay. You can fly out. Just pay for my ticket and my lodging and my food and my entertainment costs.

**Speaker ?:** Right.

**Chris Gammell:** Cool. Yeah. All right.

**Dave Jones:** All right. Well, that's enough for the amp hour.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** I don't think we got through half the stuff we had on the list, actually. No. We had a lot more cool stuff on there. So, carry over.

**Chris Gammell:** Yep. Yep. Great, great, great. It's been a good one. All right. Thanks for joining us. Bye-bye. Bye-bye.

**Speaker ?:** Bye-bye.
