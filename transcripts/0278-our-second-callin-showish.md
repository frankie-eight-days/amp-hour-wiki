---
episode: 278
title: Our Second Callin Show(ish)
url: https://theamphour.com/278-our-second-callin-showish/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded December 16th, 2015. Episode 278. Our second call-in show. Ish.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Who has not seen the new Star Wars.

**Chris Gammell:** Not yet.

**Dave Jones:** Not yet.

**Chris Gammell:** Also, I did have a thing in place. I told Dave before we started the show. If he gives me any spoilers. He's never talking to me again. I'm just never talking to him again, yeah.

**Dave Jones:** He's going to unfriend me on Facebook.

**Chris Gammell:** Oh, the Amp Hour is over at that point.

**Dave Jones:** Right, yep.

**Chris Gammell:** It's just a mortal enemy.

**Dave Jones:** But I've seen it, and you haven't sucked in.

**Chris Gammell:** I am, yeah, I'm very jealous.

**Dave Jones:** I just got back, and I actually missed the call-in show. Because we goofed up the time. I swear I said, finishes at 12, I'll be back at 1. Nope. Nope. Nope. Chris disagrees.

**Arduinos:** Yeah.

**Dave Jones:** Oops. Sorry, people. Who are ready to be. Anyway, we might still be able to have him up.

**Chris Gammell:** Anyways, we did have some people on the line. So what we're going to do is we're going to call them up. And then we'll just patch them in. Like, this is how we probably should have done it from the beginning, where we just have people lined up, and we'll call them and talk to them, and then we'll be done. So first up, we're going to call our call screener, because he didn't get a chance. He did screen calls for us, and then he-

**Dave Jones:** And then I didn't show up. Yeah. Right, right.

**Chris Gammell:** So we are going to call him up now. This is Stu. Hey, Stu.

**Dave Jones:** Hey, Stu. How are you doing?

**Arduinos:** Hi, Dave. You all right? Hi, Chris. You again?

**Dave Jones:** G'day. Sorry I screwed up before. I'm sure. I swear it was Chris's screw-up, though.

**Arduinos:** You would. You would.

**Dave Jones:** So whereabouts are you from?

**Arduinos:** So I'm from the UK, living just outside London.

**Dave Jones:** Pommy.

**Arduinos:** Yeah, indeed. The old dart.

**Dave Jones:** And we've got a delay, because we are on the other side of the planet. So yeah. This is why we never used Skype. Oh, we tried Skype on one of our early shows, and it was just too much delay, and it was, yeah, generally pretty sucky.

**Arduinos:** Yeah, I guess if you're trapped in the voice halfway across the world, then yeah, it's to be expected, I guess.

**Chris Gammell:** Right. Well, we do have a couple drops, too. And we'll keep working on this stuff. So anyway, Stu, so you said you were in the security field, right? Is that right?

**Arduinos:** Yeah, so I'm a sort of IT consultant, mostly focusing on IT security and sort of network security, system security, things like that. Yeah. So I think I ended up stumbling across Dave's YouTube videos a good few years ago, and then started listening to The Amp Hour. Yeah, I think I was saying too early, Chris. Most of it goes across sort of on top of my head, but I certainly really enjoy just listening and picking up what I can.

**Chris Gammell:** Yeah, no, that's really good. I mean, and I think that a lot of our listeners actually are kind of in a similar, like, first off, I'm always... Yeah, many. From like the, like from the DEF CON side, like when I went to DEF CON, I was just like, there's so many people that are in this field. But then when you think about it, just like the number of drops in the internet, and it's just like, yeah, there's so many places that need security and that kind of stuff. I mean, and I'm probably as oblivious in the other direction as you might be on electronics. So I don't know.

**Arduinos:** Yeah, well, certainly my electronics is very much sort of Adafruit and playing with Arduinos and stuff like that. So it's all very hacker, hobbyist in my spare time sort of thing. So, but yeah, I was...

**Dave Jones:** And that's where it starts.

**Arduinos:** Yeah, got the bug, got the fever. I just need to find time to put some more time to it. So cool.

**Chris Gammell:** Well, we do appreciate you as our call screener, even though our call screening is now over. But yeah, thanks for helping us out. We always appreciate people that help us out and support us on everything.

**Arduinos:** I think certainly had a lot of enjoyment out of the show. So happy to give back what I can.

**Chris Gammell:** Awesome. Thanks, Stu. All right, Stu. Well, thanks. And we know it's pretty late there. So we'll let you get going. Oh, yeah.

**Dave Jones:** It'd be like 1am there or something, wouldn't it?

**Chris Gammell:** Yeah, a couple plus. 5 plus 2. 2.05. Yeah.

**Dave Jones:** Oh, goodness. Go to sleep. See you, mate. See you. Thanks, Stu. Bye.

**Arduinos:** Thanks.

**Chris Gammell:** 2am. That's key.

**Arduinos:** Yeah.

**Chris Gammell:** All right. So call on the next one.

**Arduinos:** Hi, Chris. Hi, Dave. Vikas here from Bangalore, India.

**Dave Jones:** India?

**Arduinos:** Yes.

**Dave Jones:** Fantastic.

**Arduinos:** Yeah.

**Dave Jones:** Truly global show today.

**Arduinos:** Yeah. It's 7.30 in the morning here.

**Dave Jones:** Oh.

**Speaker ?:** Yeah.

**Chris Gammell:** We're not sure if Stu, who we just talked to, it's 2 in the morning. Is it any better than 7 in the morning? Because he's probably waking up and he's still not going to bed. Yeah.

**Arduinos:** Okay.

**Dave Jones:** Awesome. So do you have a question for us?

**Arduinos:** Yes. Yes. My question is about an arbitrary waveform generator. So I want to know how it actually works, like the internal working of it, because I'm planning to design one using Raspberry Pi as the backend. So by my understanding, it is just a fancy and high-speed sample player, isn't it? Like, it just loads all the samples into memory and then place it back repetitively. Is that how it is?

**Dave Jones:** That's pretty much all it is. It's a high-performance, high-speed DAC. So there's a high-performance digital analog converter. And it literally is just playing back from the internal memory. You have the waveform stored into memory. Even if it's just a basic sine wave, they will fill the memory up with that, you know, an actual representation of the sine wave and the digital will output that. All of the trick, though, with an arbitrary waveform generator is how you control the memory and segment it based on different frequencies, because you might have one waveform loaded in, and that's the representation of your sine wave. And it'll just do one, like, actual one cycle of the sine wave, but then you've got to repeat that. So you've got to have an architecture that can repeat it at any frequency. But there are multiple ways to do that, actually. You can actually, you know, if you've got, like, 10 meg worth of sample memory, you can actually preload that 10 meg with a representation of the sine wave or whatever waveform you've got, and then at the frequency within that window. So you can have, you know, if you've got 10 meg of memory and you want to generate a 10 kilohertz sine wave, then you could have 10,000 cycles of, like, not doing the math in my head, but you could have, say, you know, 1,000 or 10,000 cycles.

**Chris Gammell:** Yes, 1,000 samples per sine wave, right? Yeah.

**Dave Jones:** Well, yeah, but then it's a trade-off of how many samples you have per cycle at what particular frequency. And that determines resolution then and how choppy it looks, right? Exactly. But the other but is that your output filter on the output of your DAC, because you do filter it, otherwise you end up physically being able to see the little steps. And you can actually do that on your oscilloscope if you put it on the output of an arbitrary waveform generator. I'm showing this on a video somewhere in the past, where if, you know, if you zoom right in and actually turn the amp and then turn the gain of your scope up, then you can actually see the little steps, yeah. And it's also an art to filter out those steps and, you know. Yeah, because you have to filter at every frequency almost, right? At every, yeah, exactly. So there's, you know, so there's a, you know, one school of thought, one architecture where you always run at a fixed sample rate so that if you run at a fixed output sample rate, then you know what your physical output filter can be set to. Exactly, yeah. To actually smooth that off. But, yeah, so there's, it's all about the architecture and there's several ways to do it. It's quite difficult without sort of whiteboards and everything to go into.

**Arduinos:** Actually, the project what I have in mind is like, I'm planning to use a Raspberry Pi as the backend, like the recently released Raspberry Pi Zero. It is just, it's actually quite ideal. So what I plan to do is load it with, it has quite a big RAM memory on it, like 512 megabytes, right? So I can load all of that with the samples, like maybe a sweep waveform. Wow, that's heaps, yeah. Yeah, that's a lot of memory, right? So I can load it with like a frequency sweep or something like that. And then output the samples on the GPIO and have a daughter board with the DAC and the LC filter and an amplifier with offset controls. Yep, you could. So...

**Chris Gammell:** Ooh, I'm going to stop you there. That's, Dave knows what I'm about to say. Okay. The problem here is that, so you're going to be using, that's a Linux-based system, right? Because it runs the Raspbian, often they run Raspbian and stuff like that. Yeah.

**Arduinos:** The problem is, so if you have... Yeah, it cannot do such as fast outputs, right? So I plan to use like bare metal programming, assembly level programming. Ah, yep. Okay, that's good. That might work, right?

**Chris Gammell:** It will. And what it will be is a lot of DMA stuff, honestly. I'm not sure about...

**Dave Jones:** Actually, does the processor used in the ARM Zero, I'm not familiar with its actual architecture. It's an ARM something or other, right? Yeah, it's the ROIC ARM chip. Yeah. What you would look for there is to see whether it has, as Chris said, direct memory transfer that allows you to directly funnel from transfer from the memory without going through the processor registers, actually feed it straight to the I.O.

**Chris Gammell:** Right. Like an A to D does as well in the other direction type of thing.

**Dave Jones:** And this is why you don't want to mix up your pins on your I.O. ports. You want to actually use bit zero is actually bit zero on a GPIO port because then you've got, if you don't do that, if you just use random pins, then you have to, you know, then you have to do the processing, heavy processing, to convert the sample from the memory into whatever bits you need to drive. So that's a horrible overhead you don't want. So I'm not even sure if the Raspberry Pi Zero actually has good pinouts like that that allow you to do fast outputting like that.

**Chris Gammell:** Well, Lukas, do you want to do like a PWM type output? I mean, like, so what do you want to, what are you planning to send it to?

**Arduinos:** No, actually, I'm planning to design a daughter board which contains a high-speed DAC, which will take the 8-bit data from the GPIO.

**Dave Jones:** Oh, you want more than 8 bits. You want more than 8 bits. 8 bits is pretty lousy.

**Arduinos:** You mean like an 8-bit bus, though, or an 8-bit DAC? Yeah, 8-bit DAC from 8-bit samples. Like, the whole dynamic range would be just 8 bits. Would that not be enough?

**Dave Jones:** Oh, well, it's enough, but it's a pretty ordinary, you know.

**Chris Gammell:** We're not going to get actual 8 on the output. That's the thing. So, like, on the analog output, you won't get 8 equivalent bits. You never get the...

**Dave Jones:** Oh, you'll get... Yeah, but you'll get fairly close to it with an 8 bit. Yeah, maybe 7.

**Chris Gammell:** Yeah, it does depend, but...

**Dave Jones:** It's all to do with the effective number of bits.

**Chris Gammell:** How fast are you planning to make this thing go? Because, I mean, the 8-bit DACs, a lot of those are going up in the... You know, you can make them go, like, RF-type range.

**Arduinos:** Yeah, no, I have chosen a part which is used for video DAC, so that goes up to 30 MHz. Okay, yep. I think, yeah, I think if 30 MHz is a sample rate, then the output analog bandwidth might be, like, 5 MHz or something, right?

**Dave Jones:** Well, I would start with the 8-bit DAC, because then it's, you know, a matter of you can see how fast it all works. There's no mess, no fuss. And then once you're, you know, once you're fairly happy with that, and then, you know, you might be able to go to a 12 or a 16-bit DAC. So...

**Chris Gammell:** Do you have a part number that you are planning to use, if you're willing to share?

**Arduinos:** Yeah, it is TLC5602. DLT? TLC. TLC. It's from TI, yeah. It's a video DAC. Okay, cool.

**Dave Jones:** I see it. That's a 10-meg sample per second high-speed video DAC. Is that a triple? Because most of those video DACs are three triple outputs. Oh, you get an RGB? Yeah, yeah, for the RGB.

**Arduinos:** No, I think this is a single one, yeah.

**Dave Jones:** It's just a single? Okay, right. Yeah, 8-bit, 20-meg sample per DAC.

**Chris Gammell:** Yeah. Cool. Yeah, and then what about the other one I was wondering about is, because then you're going to need something that actually drives, the DAC usually won't drive... Exactly. ...whatever you're looking at.

**Arduinos:** Yeah, actually, so the DAC would be followed by an LC filter as an anti-aliasing filter. Yeah. ...and then I'm planning to use a high-speed op-amp to do all the offset stuff and amplification stuff. So for that, I'm planning to use an LM318, which is also a high-speed op-amp. And after that, I'm planning to use a power amplifier of some sorts, which I haven't figured out yet.

**Dave Jones:** Yeah. Yeah, you need a... Usually, like, you used to be able to get, like, buffers. You used to be able to get specific cable driving buffers. But if you're going to use an op-amp, like a power op-amp, which you can get, make sure it can drive an actual capacitive coax 50-ohm load, because some of them can't. They actually lose stability if you try and drive a coax load. So just be careful choosing an output buffer there.

**Arduinos:** Actually, I was thinking something on the lines of doing a discrete implementation. Do you think that might be okay? Like, will it be hard? Like a Class A, B style or what? Yeah.

**Chris Gammell:** Oh, okay.

**Dave Jones:** An actual transistor output. You probably don't need to. I mean, if you want to do it just for old-school street cred, then that's... I know, I actually would say.

**Chris Gammell:** I mean, like, because even those... I mean, well, it depends what kind of range you need, too, right? So that would... What you really think about with an arbitrary waveform generator, then, is, you know, you could program in, oh, I want this to go plus minus 10, and you could do that. But then getting a, you know, a high-power output, high-speed, high-power output op-amp is going to be tough then. So if you want to go... If you want to be able to set your output from plus minus 20, you know, then, yeah, you're probably going to want to go with a discrete thing. But then you just have to know that you're going to be swinging that thing around like a sack of rocks, right? You know, that's a lot of... Yeah. To do that fast and that much... Especially if you have any kind of output current, it could get pretty intricate pretty quick, so... Yeah.

**Dave Jones:** And one of the problems here with only 8 bits is that you can't do... You can't adjust your vertical in the sample memory. You've got to actually do it in analog on the output. So if you want a full-scale... Yeah, so if you want a full-scale 10 millivolt output, you're not going to do that in software because you've got no...

**Chris Gammell:** You don't only get like two bits. Resolution left, yeah.

**Dave Jones:** You don't get like a couple of bits. So, you know, so you need to do that on the output. And of course, any good function generator's got to have, you know, like 10 millivolts up to 10 volts, you know. It's got to cover that whole range. So you need not only amplifier on the output, but you also need a good attenuator as well. Yeah.

**Chris Gammell:** So you need to drive the ground around too, like pushing grounds around as... Oh, yeah.

**Dave Jones:** And then if you're going to have DC offset as well, because, you know, you don't always, you know, a good function gen will also have DC offset. So, you know, everyone thinks all this stuff is all, oh, yeah, it's a digital, it's a DDS, direct digital synthesis generator. Everything's in software. Well, no, you open one of them. There's a lot of stuff on the analog output side of things. DC offset, attenuators, amplifiers, yep, filters. Yep.

**Chris Gammell:** So one thing I would say is if you want to get started with like a, I've actually used a dev board before that has one built in. It's a STM8 discovery. Okay. And it's got like one of the demos is a little arbitrary. Well, not really arbitrary. I mean, it's, you know, it's got, it's a function generally. It's got square, triangle, and it's this great little, you know, it's only got one button on the whole board. But, yeah, it like, you know, it uses the output DAX, and it'll push it through DMA, so you can see how that's done in bare metal. So it's nice for the example code. Okay. And, yeah, great little, great little dev board.

**Arduinos:** Okay. Okay.

**Dave Jones:** Have we answered your question?

**Chris Gammell:** Yeah.

**Arduinos:** Have we ruined your day? Yeah. I need to think a lot. I think about a lot of things, actually. Yeah.

**Dave Jones:** I think, I mean.

**Dave Jones:** Well, that was a.

**Chris Gammell:** Yeah, I think that's a great question. I think a good thing to do would be to, you know, hop on like Dave's forum or something like, because there's a lot of people that are doing that kind of stuff over there, and that'll be good for tracking that project, too. It would be really good.

**Arduinos:** Oh, yeah. Yeah. Okay. It's the best place to do it. Thanks a lot, Chris and Dave. A big fan of the show.

**Dave Jones:** Excellent. Thanks. Thanks. See you.

**Arduinos:** Well, that was a good one.

**Chris Gammell:** Yeah.

**Dave Jones:** That was an excellent one from India, all the way from India.

**Chris Gammell:** Yeah, man. So.

**Dave Jones:** Well, basically everything from Sydney is all the way from. Yeah, right, right, right.

**Chris Gammell:** Okay. So we got one more. We've had Stu. We've had Vikas. We've had, I've sent out a tweet to see if anyone wants to send us the last minute thing here. I don't know. But I'm going to call our last, our last pre-done call. Call in person. Let's do it. Make sure I have the right number here. This is Ryan.

**Dave Jones:** And Ryan has no idea we're calling him, right?

**Chris Gammell:** Yeah.

**Dave Jones:** Hey, Ryan, you won a million dollars.

**Chris Gammell:** Hello? Hey, Ryan. Hey. It's Chris and Dave. Hey, Ryan. You got a hold of Dave? Awesome. I did. He's here. He did.

**Dave Jones:** He did get a hold of me.

**Chris Gammell:** This slack ass is done watching Star Wars.

**Dave Jones:** Oh, yeah. I checked your Twitter page and I figured that's what you might be doing. All right. Sorry for calling you out of the blue like this, but we are live on the air now and we thought we'd just call you on Skype and, yep. Surprise. So, Ryan, you're down in Georgia. Is that right? Yes, I am. For those of me, those like me who have no idea where Georgia is. South, east, U.S.

**Chris Gammell:** North of Disney World. North of Disney World.

**Dave Jones:** North of Disney. North. So we're talking north of Miami here. North of. Yeah, exactly. Yeah, right. State of Buffalo. Right. Ah, okay. Right. Got it. North of Miami and south of New York.

**Chris Gammell:** Yeah. So you had talked to Stuart, our call screener, but what did you want to ask about?

**Dave Jones:** I wanted to ask about what's the best test equipment to get on a budget. Because I have multimeters and a little kit oscilloscope I built myself, but I've started doing some more advanced projects like with PWM and stuff, and I find myself more and more needing like things like a two-channel oscilloscope or a signal analyzer. And I just wanted to ask, like, what's the best option for like a budget, a modest budget?

**Arduinos:** Anyways.

**Dave Jones:** Well, the first question before I jump into a monologue.

**Chris Gammell:** Hey, I got opinions too, man.

**Dave Jones:** How much is your budget? Because, like, is it $200? Is it $2,000? Is it $20,000? Like, what? It's like $200 should be manageable. I watched your... I'm actually a student, so I watched your video on the digital and analog discovery and talked to my engineering teacher about it, and as it turned out... Ah, yes. As it turned out, my engineering teacher was actually a beta tester for it a year ago. Ah, okay. That's not bad value if you're only looking at $200 budget, because my standard response here is just buy the Rigol DS-1054Z, right? It's a four-channel scope. It's 50 meg. You can hack it up to 100 meg. It's $389 or something.

**Chris Gammell:** And as I was telling a student today, too, I was saying, you know, even if you get in a pinch and you're doing a spy bus or something like that, you can self-decode if you really need to. You could put four lines on a spy bus and self-decode, so...

**Dave Jones:** But it's got that built in. Like, when you hack it, you get all that stuff. You get all the decoders and everything. Oh, I didn't know. Yes, I actually saw that. Yeah, but that's probably double your budget. When you're talking about a budget like yours, like a few hundred bucks kind of thing, it's pretty much a toss-up between an old second-hand scope or something like the analog discovery.

**Chris Gammell:** And we should mention, well, there's a new one, though, too, right?

**Dave Jones:** There's a new version, which I have not seen. Is it the same price? Is it like $89 or $99 student price?

**Chris Gammell:** No, for students, it's $200, I believe. Oh, is it? Right on the nose.

**Dave Jones:** Right, okay. It's $179. Okay. Okay, student price, right. Then it's probably worthwhile. I mean, it's not a real scope in quote marks. You know, it doesn't have a real input vertical attenuator. That's one of the main problems, you know. Yeah, it's... But it works and it does lots of useful stuff. So there's no reason I would be stretching my budget by an extra $50. I'd be getting that, plus I'd be getting maybe an old-school second-hand analog scope for $50. Don't pay more than $50 for an old-school analog, but they're very handy. Although, a lot of problem with students is space.

**Chris Gammell:** Yes.

**Dave Jones:** Physical... Are you living in a dorm or something like that? That's, you know... I'm actually a freshman in high school, so about 15. I have a little garage workshop that I keep with my stuff. Oh, so you're at home with... Oh, okay. Cool. It's starting early. That's awesome, first off. So you have... That's really awesome. So you have... Yep. Excellent. And I can tell you, old-school analog scopes really get the girls. The girls love old-school analog scopes. Yeah. Yep. I'm just putting it out there.

**Chris Gammell:** If you do... If you scope curls, you know, you can work on the biceps.

**Speaker ?:** Right.

**Chris Gammell:** Overhead scope presses. Yeah.

**Dave Jones:** Hey, you want to come over and see my... This is just figures, you know? Yeah, definitely. Definitely. That'd be great, but I don't know if I can... So because you have the space, I mean, come on. Christmas is coming up. Christmas presents. What do you want for Christmas? Mum and Dad, give me a Rhygol scope, please.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? Is that like a... Yeah. Yeah, I mean, the analog discovery, it's... You know, it's perfectly fine as a USB scope, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** It certainly has the same sort of limits.

**Chris Gammell:** I would say, if... Like Dave's saying, if you can stretch your budget at all, and I know that we're saying this is... Like, that's... It's tough. Yeah. Like, sometimes it's a hard thing. But if you can... Like, so here's what I'll say is, like, anyone that I've ever met who went and just dove in and did buy a scope, you know, like, you know, the four-channel Rhygol or something, or two-channel. Like, it used to be. I've never heard anyone be like, oh, I wish I... I've never heard buyer's remorse for scope.

**Dave Jones:** Yes. You know?

**Chris Gammell:** Like, that's... Yep. That's the main thing. Could you... Could you go through what you already do have? Because you mentioned you have some stuff already.

**Dave Jones:** Let's see. I have a multimeter and a nice temperature-controlled soldering iron. It's like a rebranded weller. Oh, good. Yep. As long as it's temperature-controlled, okay, it'll do the job. Yeah. I have a little power supply I built from a wall wart. Excellent. Building your own power supplies is a good way to learn and also get valuable test gear, too. So, yep. Definitely keep doing that. To be honest with you, I just sampled a bunch of regulators and put them in parallel.

**Chris Gammell:** Put them in parallel.

**Dave Jones:** Ooh, okay. As long as they're fairly well matched and you put a small current limiting resistor on the output and current sharing resistor on the output of each one, you'll be fine. But you'll probably get away with it. I mean, it's not good design practice, but, you know. I was looking at the, like, just getting in all the ATX power supply from a computer or something. And using that. There's a lot of people who do that, yeah. Yeah.

**Chris Gammell:** That's what the BenchBuddy that I built was, built was based on an ATX, but it's got a bunch of other stuff.

**Chris Gammell:** But, yeah. I mean, you can just get, like, a... I think Dangerous Prototypes has just, like, a breakout for it, so it'll just... Yeah. It just puts it out to a banana clip pin. That's a nice thing, too.

**Dave Jones:** Yep. Yep. Definitely. Um, let's see. I have a one-channel oscilloscope that I built from a kit, like, SparkFun selfie kit. Ah, yeah, there. Yep. Toys. I got it. Yep. Yeah, pretty much. I was able to look at simple waveforms on it and stuff, but not much. But my school has some pretty cool stuff, too. Like, they have a whole electronics club that they just recently redid, so I get to go and use that during lunch sometimes.

**Chris Gammell:** That's nice.

**Dave Jones:** Excellent. Like, a whole ton of tech scopes and digital analog Fluke 87s, I believe, and a bunch of other stuff. Ask them if they're chucking out any of those old tech analog scopes. Yep. I was going to say that, too. That's the thing.

**Arduinos:** I need to ask about that, because I asked my teacher, because I was helping him clean

**Dave Jones:** out in the back room the other day, and we found a couple interesting things, like an old ham radio and whatnot I'm trying to repair. But there was also a whole stack of analog scopes, and he said he didn't really know, and they were a school property and whatnot, but I might want to ask about that. Yeah, definitely. You are in the right place. You are in the right place at the right time.

**Chris Gammell:** First off, volunteering for sure, but what I would do is I would just say, hey, can we put a note on here? So, like, just put a note with a date found, and then in six months, if you go back to it and you say, look, these haven't moved. No one's touched these in six months. Now can we make a decision? And if not, you say, updated, you know, now the new date, you know, June, whatever. And, like, just keep doing that. And eventually, someone's going to be like, oh, yeah, we're never, ever going to use that stuff. So, yeah.

**Dave Jones:** I'm surprised they haven't written those off already. I mean, most, yeah, well, maybe they have. I don't know. But, yeah. So, definitely keep howling them about that, because the squeaky wheel gets the oil. The squeaky wheel gets the analog scope. I actually have not gone up the chain other than my electronics teacher friend. And it's a funny story. I don't actually take his class, but I went and showed him earlier this semester a little five-on-five timer piano schematic. I made an eagle and got a board made up and everything. And sometimes he gets me during lunch. So, pretty cool.

**Chris Gammell:** Well, I think you're right on the right path, man. Just keep doing what you're doing. Cool. So, we'll call you back in, like, five years when we're ready to retire from the amp hour. We need a new person, right?

**Dave Jones:** So, he's got a multimeter. He's got a power supply. He's got a solder and iron. Yeah. You really need a decent scope. Nothing beats a bench scope, you know? They're just so nice. They're just so nice. Because that's the main limitation with the analog discovery. I mean, it's just got a single voltage level input. That's it, right? Single gain input. You can't. It's got no vertical attenuator. But the advantage of it is it has, like, a 16-bit converter or something, right? So, you know, so you can digitally zoom in on low-level signals and, you know, stuff like that. Although the new one, I don't know about the new version. So, maybe it's got, like, an attenuator on the front end for higher voltages. I don't know. But if it's got a standard 1 meg, because these things don't have BNCs on the input, do they? I think you had to, with the old one, you had to buy, like, an add-on board that you could plug in BNCs and regular probes. Yeah, the new one you do, too. Oh, okay. Right. Well, maybe you don't. I think that board might even be a bit expensive. So, maybe you can actually, like, get your own front-end board made up that has a BNC on it. And then you can buy standard scope probes. That'd be kind of interesting. And then, at least, you've got a 10 to 1 attenuator on the front so that you can actually measure higher voltages, you know, like 5 volts, 10 volts, or 20 volts. I don't know what the input of the analog discovery is. I believe I actually have, for my toy scope, a selectable attenuation probe. Yep. Like, you can switch between 1 and 10. And it shouldn't be, if I got an analog discovery, it shouldn't be hard to just make a BNC expansion board for it because it's just a bunch of traces. Exactly. Easy. That's it. That's it. There's no circuitry. It's just a bunch of traces going to the input. Because I think the analog discovery has a standard 1 megohm input impedance. And if it does, then your scope probes, your switchable times 1 times 10 probes will work with that analog discovery. So, yeah. Yeah. I would definitely look at doing that. Because, and even, you can buy a pair, like, you can buy two switchable times 1 times 10 scope probes on eBay for, like, $12 delivered. You know, they're so cheap. They're so cheap. Yeah. Because this is actually a two-channel scope, the analog discovery. So, yeah, if you buy that and get two scope probes with it, there's your $200 and make up a little board and Bob's your uncle, I think.

**Chris Gammell:** Yeah. I like that. Yeah. Yeah. Do you think you need any, like, guarding traces or anything like that on there, Dave? Or no? Or just have a good ground plane? No.

**Dave Jones:** Just rock it straight in. Yeah. Nah. Don't worry about it. She'll be right. No worries. Do you know if the 1054Z has, like, a USB, not a USB host, but a USB guest, like, you can hook it up to a computer and take measurements and stuff? Yeah. You certainly can. Yes. Yeah. The software's not that great with it. The Rygol software is a bit meh, you know. But yes, yes, you can operate it remotely from the PC. And they've got, like, front panel interface software where it, like, duplicates the front panel, I believe. But also, you can send a command. So you can write your own software to make it, you know, to get the data out of it and stuff like that. So, yep. Yeah. Easily. And there's a bunch of example code out there. If I recall correctly, the scopes in my school are TBS 1062. Oh, TechTronix basic scopes.

**Chris Gammell:** The crappy, like, little, like, four-inch screen, like the old gray screen.

**Dave Jones:** 30-year-old architecture, 2.5K of sample memory. Oh, they're, oh, man. They still sell those. I can't believe it. But, hey, they're perfectly usable scopes. Don't get me wrong. They're, you know, if you can lay your hands on one of those, oh, yeah, right? That is a real scope. The ones I saw on the back were the same ones that we have out front. They're just LG. I don't remember the model number, but they're analog and everything. I was trying to hook the 1062 up to the computer by measuring a servo signal off an Arduino. Oh.

**Chris Gammell:** Interesting.

**Dave Jones:** But just remember that the Rigol 1054Z craps all over that TechTronix TBS scope. That, you know, there's chalk and cheese between them. Oh, so hard. Well, I mean, it was nice talking to you.

**Chris Gammell:** All right. Cool. Great. Thanks for calling in, Ryan. Thanks, Ryan.

**Dave Jones:** Keep it up, mate.

**Chris Gammell:** Thanks for doing what you're doing.

**Dave Jones:** Excellent. Thank you. See you, mate. See you.

**Chris Gammell:** See you. All right. That was great. Yeah. 15, mate. There you go.

**Dave Jones:** That's awesome. Yeah, 15. Yep. And see, that's the idea of being, you know, people wonder, oh, how do I get an analog scope? He's doing the right things. He's not even taking the electronics class. Hasn't even got that teacher. But he's going talking to that teacher, getting in the lab, right, after school hours or whatever. And, you know, and playing around. And he's in the right place. And it's people like that who get the stuff. Yeah.

**Chris Gammell:** Yeah. It's, yep. If there's a, other ways that I've gotten gear in the past has been the junk bin. Yep. That's always a good one. Exactly. Yeah.

**Dave Jones:** But if you can get it before it goes in the junk bin. Of course.

**Chris Gammell:** Yep. Yeah. No, mine was pieces that I had to put back together. So. Yeah, exactly.

**Dave Jones:** Because people physically toss them in the dumpster. It's, you know, when you actually have to climb into the dumpster, then people don't usually just, oh, gently place it in the dumpster. You know. Right, right, right. Just in case someone might want this one. Might, might want it. Exactly. Yeah. No. So that's great. Yeah, we got that one. Two excellent calls. That worked well. Just Skype.

**Chris Gammell:** Yes. Now what?

**Dave Jones:** Now we have a regular show, dude. Now it's you and me, man. Come on, be professional. Oh, man. Come on.

**Chris Gammell:** Yeah. Okay. Mano a mano. Yeah.

**Dave Jones:** Come on. We've got a Reddit list. We can talk about Star Wars.

**Chris Gammell:** No. We cannot. All right.

**Dave Jones:** Anything but. Anything but. Just can I say a few. It is awesome. Okay. JJ Abrams does not disappoint. This thing is freaking. It is real Star Wars.

**Chris Gammell:** Tempted fate here, man. It is. Oh, mate. I'm telling you. Yeah.

**Dave Jones:** And am I allowed to say it's like shot on real film? No.

**Chris Gammell:** Don't. Digital rubbish. Don't do this, man. Don't. You're telling that line. I'm just saying. Right. Yeah. Don't do it.

**Dave Jones:** Anyway, it's great. Don't do it. And I've seen it. You haven't. No, no, no, no, no, no. Okay. Let's. Some.

**Chris Gammell:** Right.

**Dave Jones:** Microchip are buying Atmel. No, they're not though. That's the thing. So I keep seeing all this stuff. Like what the hell is going on here? They were already bought. Weren't they? No, they were in negotiations, but it was nothing was signed apparently. And then microchip have come in in the side. And apparently Atmel were hedging their bets. They're going, oh yeah. That we, who was the company was going to buy them? Bloody dialogue. Yeah. Right. Dialogue. And they were going, oh yeah, okay, we'll do a deal with you. But they were still seeking, they were secretly doing also a deal on the side, showing the books to microchip on the side as well. So now. As well you're coy minx. Oh yeah, why not? You know.

**Chris Gammell:** Batten eyelashes at every suitor. At every.

**Dave Jones:** Yeah, right.

**Chris Gammell:** Oh my.

**Dave Jones:** Come and check my book. I'll open my book.

**Chris Gammell:** Hello boys.

**Dave Jones:** Yeah. Check out my book.

**Chris Gammell:** What, what do you, what do you, I mean, I, I don't really care. I mean like, I.

**Dave Jones:** All right. Well, this is not the first time.

**Chris Gammell:** Eventually they all make ARM processors.

**Speaker ?:** Right.

**Dave Jones:** Well, microchip tried to buy Atmel years ago and Atmel blocked it through a shareholder thing. Yeah, like shareholder stuff. Yeah. Yeah. It was, it was like a hostile takeover. Microchip tried to buy all the shares and did do a hostile takeover, but they lost. So, um, yeah, I, it's.

**Chris Gammell:** I mean, what do you think about it personally? I mean, you use pick stuff before you've used Atmel stuff before.

**Dave Jones:** Yeah, I've used both pick and Atmel. I use them almost interchangeably.

**Chris Gammell:** It seemed like people on the, uh, on the subreddit were not very happy about this.

**Dave Jones:** All right. Well, well, who was it? The microchip fanboys or the Atmel fanboys? Yeah.

**Chris Gammell:** Uh, I think it was Atmel. Atmel.

**Dave Jones:** The Atmel fanboys, of course. Yeah.

**Chris Gammell:** I don't think it's fanboys, but it's just people with, I mean, that's the thing. Like, I think most people pick one or the other. Right. Uh, so I, I, I don't do micros normally. Right. Right. Oh, okay. Well, uh, big companies get bigger.

**Dave Jones:** Yeah. Well, you know, but there's gotta be like massive overlap there. That's the thing, you know?

**Chris Gammell:** Well, would there not? Like, I mean, like, okay, you gotta figure is, is Atmel gonna, or is, would they just kill product lines? That's what, like, things like this don't make sense to me because they're so similar. Like, I would think the dialogue line makes sense.

**Dave Jones:** Well, Atmel don't, don't get a say in it, right? Oh yeah, like dialogue probably makes more sense for them to buy it, but let's, let's assume that microchip buys them. Right. What, because that's the more, that's the more interesting thing, right? If microchip buy them, there's, you know, huge overlap. I mean, they're both, you know, like top five in the, you know, eight bit micro market. You know, um, I don't know where microchip sits in the 32 bit market with their pick 32, but they do have a loyal customer base with their pick 32 and you can bet your bottom dollar, the pick 32 management group don't want to get their ass canned, right? Because, you know, they don't want microchip to switch to arm, right? Which of course Atmel have, um, some, um, you know, some fairly decent arm, uh, processes. Yeah.

**Chris Gammell:** They're doing that SAM 20D thing, right? That's their.

**Dave Jones:** Yeah. Yeah. All those are used in low power calculators and they're used, you know, they, I don't think they've really got a, oh no, no. They do have like a real, a fairly decent grunty high power, uh, which pick, which microchip don't have, you know, their, their, their pick 32 is nice, but it's not really out there competing with the high end arms. Um, last time I looked anyway. Um, but yeah, there's going to be lots of internal management groups, you know, it's, it'll be group infighting, you know, there'll be fistfights in the canteen, you know, when they merge, it was like, it'd be funny to watch actually, but you know, but yeah, no, somebody's got to go. I cannot see microchip buying Atmel and just not eventually trimming the fat. Well, okay.

**Chris Gammell:** So here's the same thing that I'm going to say the same thing that I said at the free scale, but I was totally wrong about them too. I don't get why there's such, I get it and I don't get it. Like, so I get that everybody is asking for arm chips and yet, so like microchip has the pick line and it's, you know, very successful over time. Maybe it's not keeping up or anything like that, but like, even just as a point of differentiation, like we're not making arm, we're making something else. You're like, I don't get like, and so free scale had that too with a cold fire line and you know, they had the core IQ stuff and like, and now like free scale is so hardcore in the arm stuff. And it's just, I, I just feel like it's, it's very short sighted. Like it feels like it's just a management decision because it feels like, oh, well, we're going to chase this trend right now. And also we get to save money because arm's doing all of our research for us. And it's like, yeah, you jackass, but that also means that everybody else gets that same thing as well. Like I said the exact same thing. Remember when analog devices said that, oh, we're not going to be doing new. I mean, it wasn't all, they weren't canning all of their new analog process stuff, but they were basically like some of the older ones. Yeah. No, they said like T we're going to let TSMC take, you know, develop and then take our analog tech or develop the analog technology, like the actual fab stuff. And it's like, that is your frigging competitive advantage. Like that's the thing I don't get. Like all of these frigging MBAs, like, do they skip that part? I get the part where they want profit. Cool. Awesome. Everybody likes money. Great. Did you skip that part where like a differentiating factor in a marketplace? Is it like, does no one pay attention to that anymore? Is it like, well, no, no, no. We all want to be arm processor, you know, makers. It's fine.

**Dave Jones:** Well, they did. Cause like when I spoke to Steve Sangy, the CEO of Microchip, like five years ago, right? Yeah. He said exactly that. We don't want to get into arm because you've got to pay the arm tax, right? And, and there's no point of differentiation. There's no money in it. Ultimately, right. And ultimately it's a losing bet. And you can see that these days with the, you know, the cost of arms, these arm processors just keep dropping to dropping, dropping to where they're, they're 50 cents are almost free. Yeah. Right. And it's like, you can't make a sustainable business out of that or not, not with as many players as we have now. So, you know, right.

**Chris Gammell:** Right. Right. What I know, and I, I mean, I am sympathetic on some of these things, right? So like arm stuff, they're like, well, everything is dropping in price. So we have to chase that trend. So we get some piece of what's left. Okay, fine. You want to say that? That's fine. Yeah. You could say that, but knowingly that you're going to not, your revenues might look, they go up, but yeah, over time, you're just going to get eaten by, you know, some fab who just goes straight to arm and make some variant. Fine. Then the same thing goes with chip, with fab technologies, like fabs are super expensive. So they're all, they're all cut and running. And then they say, oh, well, we'll go to TSMC or we'll go to, you know, UMC or anyone who's making stuff as like a foundry business. And that's fine too. But you have to know, like, so maybe for micros, that makes sense. But for the analog people, it's like, guys, that's all you have left. There is nothing else. I don't buy it based on how pretty your logo is. Maybe supply stuff, but like not, like, I don't know. It's just, maybe there's some piece that I don't understand here and I'm sure

**Dave Jones:** there is, but I don't know. You would have to look through the entire portfolios of microchip and app mail to see where the overlaps are. And maybe, you know, microchip want to keep running the arm separate, maybe hedge their bets, right? Oh yeah. Okay. We don't have to pay to develop arm. Bam. We're ready to go. We've got stock. If we buy app mail, we can just, we've already, we're buying their client base as well. Right. So they might continue to sell those arm chips. And if they don't perform, then they might just chop them off later. Yeah. Right. But, you know. Well, but like

**Chris Gammell:** any other growth situation too, it's like, you know, yeah, you're getting bigger. That's good for the bottom line and survival and stuff like that. But like the thing that it feels like they never do is they don't take into account the business they're going to lose from their current customers. So someone who's been buying pick chips. So I think like Voya and, you know, just people that do pick stuff. They're like pick fanboys. Like you, you know, you always say fanboys, right? Yeah. Like that's all they know. And, and it starts to threaten that group. Then you start to lose business from the group that you thought was going to be stable. You know, it's like, yeah. Right. It's like, oh, we'll just add this little thing over here. And, and then,

**Dave Jones:** well, all I know is that microchip aren't stupid and they've already, and now this is, they're a second attempt to buy Atmel. So there's, it's gotta be something in it for them. And you probably don't know unless you audit Atmel's books and, you know, you know all about the internal politics and stuff. So anyway, I don't know. I don't either. What would our audience prefer? Dialogue by Atmel or microchip by Atmel? Or maybe somebody else will come in to save the day. Yeah, exactly. Maybe, maybe. What do you reckon, Chris? We've got enough cred. What do you reckon? We can go out there. We can go raise some money, Dave. Yeah, raise some money. Venture capital, maybe a crowdfunding campaign and we can buy Atmel. What do you think?

**Chris Gammell:** Yeah, I wouldn't buy Atmel. Sorry. I like the people I know at Atmel. I like Atmel. But like, come on, man. It was all retrospective. They're like, oh yeah, no, no, no. We were part of the Arduino thing. Yeah, no, no. We're totally into this now. Like, do you remember at the beginning? It's like, no, they didn't give a crap at all. And it's like, now it's like, oh, well, it's a

**Dave Jones:** marketing channel. Yeah, that's great. Yeah, but they still don't. And a lot of people keep saying this, oh, you know, Atmel is so valuable because of the Arduino. It's nothing. It's nothing. It wouldn't even register on the balance sheet of, you know, the bubble. Well, I don't know about that. Maybe. Well, you know, like hardly. It'd just be a speck in the ocean, you know?

**Chris Gammell:** I think the thing with that is like, okay, so it's a process that it's an 8-bit micro that they've done nothing to since, I don't even know when that was made, the 90s? The 2000s? I don't know when the 328 came out. But like, okay, they're not developing new stuff for it. Fine. And it's just like, when you talk about like new customers coming in though, good God, like, you know, every high school kid now at least has seen an Atmel chip, but probably one of the first ones they've seen. So yeah, that's worth something, you know, like from the marketing

**Dave Jones:** perspective. Only if you're a long-term clever thinker, which a lot of these people aren't. They're looking for the next six-month, you know, half-yearly report. You know, that's

**Chris Gammell:** all they care about. That's a problem no matter where you go. Exactly. Yeah. Public companies are tough like that. So anyway, we've got comments down below.

**Dave Jones:** Let us know what you think about the microchip Atmel thing. Yeah. Yep. Next.

**Chris Gammell:** Yeah. What about, speaking of companies that are in weird places, what about Jerry and Rick over at Cast.AR? I saw you posted this.

**Dave Jones:** I added this because I'm, yeah, because I back their, yeah, I back their project.

**Chris Gammell:** They're a Kickstarter project. I thought I bought like a cup of coffee or something. I didn't get an email though.

**Dave Jones:** Yeah. I, yeah, I bought a, yeah, I don't know what level I backed at, but I backed it somehow. So I get the updates and, but the updates freely available on this side. It's not, it's not just for us backers. And basically it's been over two years. I think they finished in October two years ago. So it's been over two years and they basically have not delivered. Although I think they delivered the early backer starter kits, which was like 10 of them or something. Don't quote me on this. Yeah. No, they have gotten some. They've delivered some of the developer stuff. But basically, yeah, but basically the bulk of the backers who just wanted their Cast.AR glasses, they basically have not delivered. And in the meantime, they've of course taken on capital funding. I can't remember who it was. They took on money from somebody.

**Chris Gammell:** Playground. Playground, whoever the hell they are. So that's the, started by Andy Rubin and Crud. I forgot the other guy's name. Bob? I don't remember. Anyways, Andy was the

**Dave Jones:** one who started Android. So. Right. Yep. Anyway, so the interesting part about this is because Jerry and, um, what's his name? Rick. Her cohort. Rick. Yes. Thank you. Sorry, Rick. If he's listening, he probably is. No, no, no. He's got, no, they got too much time on it. Not enough time on their hands to listen to our show. Anyway, they always wanted to make a business and that was what Kickstarter is traditionally all about, right? They wanted to build a big business, not necessarily, not necessarily just, you know, make some glasses and ship them, right? They wanted to, they were building a company and that's what they wanted the money for. And so they've ultimately decided now this update, you can read it for yourself. They've decided that we're not really going to deliver our original promise to our Kickstarter backers. What we're going to do is focus on a, a real high end, like a proper polished consumer product. Yeah. It's not high end. It's not high end. Well, no. Well, yeah. Okay. So we're, we're focusing on, on a consumer product, right? A real slick consumer product. And you'll get one of those when we've done it, but we're not going to rush out and, and finish some half assed. I'm not quoting them properly, but we're not going to finish some half assed product just to ship it to backers to keep them happy.

**Chris Gammell:** Well, yeah. And so Rick also wrote about the, uh, you know, there's no software for it either. So like this stuff's going out to developers and it's been slow, but there's, there's, there's

**Dave Jones:** no apps. There's no, and they're saying, yeah, if you're a backer and you're interested in it,

**Chris Gammell:** you're going to get this thing. It's gonna be like, yeah, now what? You know? So, so, but

**Dave Jones:** that's interesting. It's a, it's a real interesting decision because you know, it's a conflict, like you want to deliver to your backers, right? But then you also wanted to form a company and have a nice finished polished product and you probably can't focus on both. So they've had to make the decision to go, go for broke with the polished consumer product. And I think they are offering money back or something. They're saying something about a refund. So you can choose, I think as a backer, you can choose to get a refund or hang in there for

**Chris Gammell:** a, no, no, no, no, no. So if you backed at the hardware level, you get a refund and then you also will get a coupon for one. Oh, you also get a coupon. Yes, that's right. So they're

**Dave Jones:** being extra generous. So they're giving you your money back and you'll get a free consumer one when it comes out. Yep. Exactly. Um, so that's pretty generous, but yeah, but it's basically failing to deliver essentially. So they've made the choice that, you know, sorry, but we're not going to deliver what we promised. Yeah. I mean, I think it's, but, but they're not taking the money and running there. Actually, this is a quite a good deal because you get your money back and get a consumer version. So, yeah, no, I think, I think this is a nice new standard. If this becomes a thing, you know, it is a very nice way out. That's what I'm saying. Yeah. It is a very nice out. Right. Um, very, very generous. So yeah, so it should be because they've got a lot of funding now. Right. And so obviously they've decided to use some of that funding to refund the backers because obviously they've, after two years of development, they've already spent all of the money that they got from the backers. You know, that's almost a given. Well, now is the point in the show when Chris mentions

**Chris Gammell:** that it's, it is Kickstarter and there's no should in there, right? These people, anyone who gave money knew the risk that it might not happen. And I mean, even with, you know, we've had Jerry on the show a lot, it's still possible that something could have happened. It's hardware. It's, um, yeah, it's, so no, I don't think they should have done anything. It's very nice that they did, but, uh, and I hope this is a new standard, but yeah, I don't

**Dave Jones:** think that this is the, no, I mean. Oh, well, no, they, if they didn't deliver, they should, I'm going to use the word should, they should have given the money back. Right. Especially when they've got outside funding, they should have given their money, but they've done more than that. They're giving you money back and giving you a free, you know, uh, three consumer one when it's done.

**Chris Gammell:** I just don't agree with should, but that's fine. What? We can, we can differ on that. That's fine. Yeah. We can totally know it's a difference of opinion. Yeah. No, really we can.

**Dave Jones:** I thought it was, I thought it was the Kickstarter terms and conditions. You, if you cannot deliver your promise rewards, you will do your best to refund people their money. Well, yeah.

**Chris Gammell:** It's in the terms and conditions. Sure. I'm sure that there's a lot of, there's, there's not like you can't go after them for a lawsuit though. You know what I mean? Like, it's like,

**Dave Jones:** yeah, your name would be not pretty. Yeah. But of course, but come on, you can't.

**Chris Gammell:** Dave, I'm just saying that like, it's different than should it's, it's, it's good that this happened. This is the best scenario of a bad scenario. That's what I think.

**Dave Jones:** No, I think, I think this one, okay. If they've spent the money, okay. And the money's all gone.

**Chris Gammell:** Dave's ready to go to the bat over verbiage here. All right. Yep. Right. Here we go. I can dial in our lawyer. We can call up a lawyer. We have a lawyer? We have a lawyer.

**Dave Jones:** If they've spent the money, then there's no money left. Well, sorry, everyone lost their money. Right. It's a loser. But, but they got venture capital funding, right? So which puts them in the should category. Okay. Because they've got all this outside funding, then they've got money again. And if they've got money, they should refund their backers if they're not going to deliver. Because that is the Kickstarter terms and conditions.

**Chris Gammell:** Disagree still. I think that you could, you could string people along and say, we're going to deliver. It's just going to be longer.

**Dave Jones:** No, of course you could. Of course you could. Right. But that would be, that would, then they'd be dishonest and everything else. And of course they're not dishonest, right?

**Chris Gammell:** Let's share it. I'm going to do an experiment here, Dave. What? I disagree with you and I'm done talking about this. Ah, dude. Shall it pass? Why? Will we be able to move on? Can we move on? No? Wuss? No, I'm not a wuss. You just don't want to take me on. It's not taking you on, Dave. I disagree with you. I'm not going to change your mind. Would you agree with that? Yeah, probably. Yeah, okay. Let's move on. Did you see the, speaking of video games.

**Dave Jones:** Probably not. I've been too busy watching Star Wars. Sorry.

**Chris Gammell:** Oh, yeah. Did you, the Steam controller, the video of the Steam controller? No. No. It's a YouTube video. And so Valve. Speaking of Jerry, that was a good segue, by the way. And basically, so people we know are working on this controller still. Yes. Yeah, we do. They're still there, which I'm surprised. And there's parts made in all over the world, but basically they show that it's assembled in Illinois. And they show all of the industrial automation of like the button. So actually, they show it being pulled off the mold.

**Dave Jones:** Oh, that's the one that you tweeted.

**Chris Gammell:** Yeah. Oh, dude.

**Dave Jones:** Oh, I had no idea that was the Steam one. I thought that was like an Xbox controller or something.

**Chris Gammell:** No, that's a Steam controller. And so then they have robots that are testing the, I mean, sorry. Yeah, that's awesome. I was corrected. They're not robots. What are they? So Sophie, who helped, or who set up the Supercon, she said, it's only a robot if you don't know what it's going to do. So this is a...

**Dave Jones:** That's a good...

**Chris Gammell:** Yeah, which is awesome, right? I was like, oh.

**Dave Jones:** Line in the sand definition.

**Chris Gammell:** Yeah, exactly. So this is industrial control because it's a single use.

**Dave Jones:** It's an industrial robot is their traditional name.

**Chris Gammell:** Yeah, I don't know what the... Yeah.

**Dave Jones:** Yeah, that's their name. I've known them for 30 years. I don't know how it goes. Industrial robot.

**Chris Gammell:** Yeah. And so, yeah, so this... But basically, they're all single use arms and levers and all this other stuff.

**Dave Jones:** Oh, yeah. No, no. They're all purpose designed.

**Chris Gammell:** Yeah. Yeah. And it's, oh, it's just, it's a symphony. I mean, like, and the video making, too, is just really...

**Dave Jones:** Oh, yeah. The video making is first rate. Yeah, that is awesome. They spent a lot of money making that video.

**Chris Gammell:** Yes. Yes, they did. Yes, they did. But also, they're assembling...

**Dave Jones:** They most likely hired an external company to come in and shoot it.

**Chris Gammell:** Yeah. Yeah, but they're assembling in the US. Which is also interesting, right? Awesome. I mean, like, that's not... So, first off, when I watched it, you know, we've talked about robots a lot on here. I talk about robots a lot. You always scoff. This is the kind of thing where... Okay, so watching these things be assembled, right, these controllers, they're basically, you know, they're putting in buttons... They're putting in the plastic coating for buttons. They're testing out the little thingy-dingies. The thingy-dingies. Yeah, you know, like, little touchpad thingy-dingies. Like, this would be a factory in China, right? This would be people.

**Dave Jones:** They're robots! They're made of people! Oh! And once you've put the NRE for something like this in... Yeah. It is super... You know, it is much... Runs much cleaner and much more efficient.

**Chris Gammell:** And then you crank it, right? Exactly. It's all at front cost, and then you go. Yep. You know, like... And then...

**Dave Jones:** I wonder...

**Chris Gammell:** Yeah, go ahead.

**Dave Jones:** I wonder how they made that choice. Like, how many of these, you know... Because they would have had to come back from sales and marketing and go, we're going to sell... We can guarantee we can sell 10 million of these controllers, right? And then they go... The boffins go away, and they, you know, punch their calculator keys, and they come back and say, yep, it's cheaper to spend 10 million dollars to automate this factory, you know?

**Chris Gammell:** Well, and this is the future, though. I mean, this is the new deciding point, right? Where it's like, okay, yeah, and you're right, it's based on volume. It's based on taxes.

**Dave Jones:** Oh, there's nothing new here, dude. This is not magically new.

**Chris Gammell:** No, no, no. What the new part is...

**Dave Jones:** It's been business 101 for the last 30 years.

**Chris Gammell:** No, no. The new part is the changing labor rates in China. The increasing... The continual increase in labor rates in China, right? And the amount of, you know, factory space you might need to spin it up, stuff like that.

**Dave Jones:** Have you seen my interview with the Siglant CEO? Yeah, exactly. That's what I'm thinking of. He talks about that. Yeah, he confirmed that, yes, it's a big problem for them. Just in the last couple of years, three years, I think he said, wages have doubled in China. Not only factory production workers, but engineers have more than doubled as well. So, you know, yeah, everything's... And, you know, you can probably expect them to double in another couple of years as well, you know? There's... Like, the growth hasn't stopped there, I don't think. Right. Their wages growth hasn't stopped.

**Chris Gammell:** Yeah, you have people trying new things and just the continuing costs of ever-denser cities too, right? You think about people moving to a town and, you know, the real estate prices go up, so the labor rates go up to match and that kind of thing. And then you got the whole...

**Dave Jones:** So, why Illinois? Illinois is cheap backwater. Like, is it? Like, Illinois... Sorry to all the people from Illinois. No, no, no. So, that's where Chicago is. I don't... I never hear about anything being made in Illinois.

**Chris Gammell:** So, Chicago's in Illinois, but the real thing is... Right. A lot of...

**Dave Jones:** Yeah, but where... Right. Is it out in the sticks? Probably, yeah.

**Chris Gammell:** So, like, I didn't see... I didn't remember what the town was, but actually, there's a ton... Like, literally a ton of residual stuff because if you had a Motorola phone in the late 90s, it was made in Illinois. I mean, like, that's the thing. Oh, okay. Right. Like, Motorola is from Chicago. Like, that's...

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** Yeah, yeah. So, there's... So, I have a friend who's a guy here... He's living here now, but he used to be a purchasing agent out there at Motorola. And he would just... And then he had local fabs and everything like that, too. And he would just be placing, like, orders for, like, 10 million boards at a time kind of thing. Like, can you imagine signing that for a contract?

**Dave Jones:** Yeah, that's insane. Yeah, yeah. Just, you know, phone up casually.

**Chris Gammell:** That was his entire job, was just PCBs. Like, that's it. Wow. And I don't think it was just him either.

**Dave Jones:** So, have Steam done a Tesla and gone around the country and go, right, where is an empty factory that... In a town that will give us, you know, and a state that'll give us fantastic, you know, tax rates. And they're so desperate to have jobs back there that we'll get it for practically free, you know?

**Chris Gammell:** Well, Illinois is not usually known for its upfront business practices. Like, almost every mayor of Chicago is... No, no, sorry. The governor of Illinois, like, always goes to jail. It's like, there's a long string of, like, governors going to jail. You know, like, it's really... I think it's the governors. Maybe it's... No, yeah, I think it's the governors. That's hilarious. There's just, like, so much corruption.

**Dave Jones:** What a politician actually goes to jail?

**Chris Gammell:** Yeah.

**Dave Jones:** Have I entered an alternate timeline?

**Chris Gammell:** Yeah, this is the PSW timeline. Post-Star Wars. PSW? Yeah.

**Dave Jones:** Ah, right. Okay. Right. Where they've abolished all lawyers. Is that the one? Yeah, right. Is that the one?

**Chris Gammell:** There's... Balance has been brought to the force, Dave. Right. Yeah. So, no, but no, you're right. And I think that's chasing that kind of, like, you know, and honestly, a lot of that kind of stuff, when you look at the setup, so much of that is talent, right? When you think about... Oh, yeah, yeah, yeah. You need machine builders. You know, like, you could have someone that's doing an actuator that, you know, is going to do 10 million, you know, 100 million, a billion touches on something, and it needs to work the whole time, but if you pay that up front, same thing. If it works great, if it, you know, if you can optimize that out, yeah, you just, you can, like, so we've talked probably before, maybe we haven't, you know, dark factories, right? That's kind of like, that is the manufacturing dream, where you turn on the thing, it's cranking them out. I think we've mentioned it. You turn on...

**Dave Jones:** And you don't need... No, I don't think so. And you don't even have to turn the lights on, because they're so... Exactly. They're so reliable that, well, why even, you know, spend money powering the lights, because there's no one there.

**Chris Gammell:** Right. Yeah, and the only time you ever need anything is if there's, like, a, you know, interruption or something like that.

**Dave Jones:** But real factories do not work like that. Of course. No, yeah.

**Chris Gammell:** It's just impossible. Even in a fab, it was, which is, like, I think one of the pinnacles of automation. Like, it's just, it's still, you're going to have issues, you're going to have... Honestly, some of the problem is the humans get in the way, but...

**Dave Jones:** Okay.

**Chris Gammell:** You ever been hit by a foop?

**Dave Jones:** What's a foop?

**Chris Gammell:** A foop is what holds the wafers. All right, okay. Front opening unifying pod.

**Dave Jones:** Or is foop the sound it makes when it whacks them on the head, is it?

**Chris Gammell:** Exactly. Right, right. Right. It's when they slide you in the body bag after you've been conked out.

**Dave Jones:** Right, yeah.

**Speaker ?:** Foop.

**Dave Jones:** Well, those wafers are razor sharp. You can lop somebody's head off with one of those puppies. Jeez, just imagine the paperwork involved in that.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Wow. No. Foop.

**Chris Gammell:** Foop. It's a fun word to type, too, I've got to say. I'm just writing it on our list here. Oh, goodness. What is the last... We're probably running down out of time. No, actually, I'm going to tell you what I want to talk about. I'm falling. I found this link on Hacker News. I'm not sure if this is why someone posted it, but I thought it was hilarious. I can't sign into Google Calendar on my Samsung refrigerator. So it's on the Google support forums, right? Right. And it's a thing. It's a... I have a Samsung RF blah, blah, blah refrigerator, and the app's been working great, but now I can't do it. And it's like... Like... Oh, we're in the future.

**Dave Jones:** And it's like... And the first response is like, your fridge needs a software update to use the new API. It's like, we have entered an alternate reality.

**Chris Gammell:** IoT, folks.

**Dave Jones:** Oh, God.

**Chris Gammell:** Internet of stupidity. No.

**Dave Jones:** Yeah. Although I can imagine, because like, the fridge is traditionally the center point of the house. It's, you know, like it's where people are going to hang around the most. And it's where you put your calendar. Like, we've got the calendar on the fridge that must be obeyed. You know, I've got a wife that must be obeyed. And the calendar on the fridge is like the holy grail. Oh, yeah. And she makes the calendar. Can you get her to put the app on there? And if it's on the calendar.

**Speaker ?:** You know.

**Dave Jones:** And, of course, when... Yeah. And, of course, when I ultimately forget something, go, right, Saturday, what are we doing today? Look at the fridge. You didn't know that. Blah, blah. You know.

**Chris Gammell:** Right, right.

**Dave Jones:** The API isn't working.

**Chris Gammell:** Yeah. That's... No, that's a good... Actually, that is a good point, though. Yeah, no, that's true.

**Dave Jones:** So, hence, I can understand why building, you know, an internet terminal into the fridge door, you know, so that... Yeah, I guess that makes more sense than...

**Chris Gammell:** Yeah, it's just a screen. It's just a screen bolted on. You can just as easily... Yeah, screen. Yeah, exactly. Like, glue a tablet to it, right?

**Dave Jones:** You could... You wouldn't have to use a glue. You could have magnets and... Oh, yeah. Good point. Yeah. Yeah.

**Chris Gammell:** Fridges and magnets. You and your technology.

**Dave Jones:** But then how do you recharge the thing? You know, you've got to have... Yeah.

**Chris Gammell:** U-beam.

**Speaker ?:** Ha!

**Chris Gammell:** Sorry. No, I don't want to go there. I didn't say it. I didn't say it. I didn't say it. Editing that out.

**Dave Jones:** Have you seen my U-beam infographic? No, don't.

**Chris Gammell:** Please don't. I don't want to talk about it. Oh, my God. Why? I get so angry, Dave.

**Dave Jones:** I like my U-beam infographic.

**Chris Gammell:** Dave, I get so angry. That's the problem. Like, it's so frustrating. I shouldn't have said it. See, I know these things. They fly out of my mouth. They go, oop. Yep. Oh, well. Okay. One other... Two other things. One is this telematics... No one liked this one on Reddit, but I thought it was really fascinating. Telematics to track workers every move. Basically, UPS has been... So this is kind of the robot thing as well. But they're tracking so much stuff in a UPS van, which is a delivery van here. Like a... What do you call it?

**Dave Jones:** Yeah, yeah. That's fine.

**Chris Gammell:** No, no, no. But you call it something different than post, though. You call it...

**Dave Jones:** No?

**Chris Gammell:** Anyway. No? So they measure everything, though. Is the seatbelt clicked? How long did they take on a bathroom break? Like, did they lift properly? Oh, right. Okay. So this is like the sensor output, right? And what's really happening is it's getting to the point where it's ignoring that these drivers are human, right?

**Dave Jones:** Ah, human.

**Chris Gammell:** I was going to say that, yeah. And so, like, what do you do, right? I mean, like, obviously...

**Dave Jones:** I just need to take a break. Like, I've been driving all day. I need to get out and stretch my legs, you know?

**Chris Gammell:** I mean, like, there is some very legitimate stuff here. And what it really comes down to... So another thing, kind of going back to the China talking about labor thing, like, so this is going to be a huge... On the path to... I'm kind of quoting my own tweets here, but this is stupid. But on the path towards, like, full roboticism, right? Like, everything being robotic. We talk about, like, Amazon delivery with, like, drones or, you know, those little automated cars and stuff like that. On the path to that is something like this, like, totally censored, totally using a lot of sensors, that is, you know, tons of measurements and big data, blah, blah, blah, blah, blah, buzzword, buzzword. But there's going to be tons of labor disputes in there. Like, another example is right now I tap a button on my phone, a car shows up with a human driving it, and I don't talk to them. And then I get out of the car, and then it just automatically pays. It's Uber, right? Like... Oh, right. And...

**Dave Jones:** What? You don't talk to the person. You don't have to. Seriously?

**Chris Gammell:** Sometimes I'm on the phone. I mean, usually I do, but I don't have to. You're a rude, rude bastard. Sometimes I'm doing something. Talk to the person. Sometimes I'm doing work, Dave. I have a difficult... Bloody hell. I'm on Reddit. Come on. Sometimes I have a lot of Reddit stuff to read to put on our list. But anyways, but the idea is, like, the people that are there, that's the people that are going to be replaced by self-driving cars if that ever comes to fruition, right? Right. And at some point, they're going to be like, hey, wait a second. This is a job. I like this job. I want to keep this job. Like, everything where it goes from that automation point of, like, app and humans to eventually, like, app and robot is, like, there's tons of labor dispute coming there. And it's going to be weird, right? So even, like, going back to the Steam controller, it just leapfrogged that and it just said, nope, full automation, full robotic automation, right? And... But imagine if they would have started with humans assembling and then eventually they replace it, then there would have been all this strife. And so that might end up impacting... So what the idea is that between the automation point and robotic point, there's tons of strife. And I think it's the 21st century labor dispute is going to be based on, you know, that.

**Dave Jones:** Robot wars. Yeah.

**Chris Gammell:** I mean, yeah. I mean, it's going to be like... I don't think it'll be the level of the Luddites, you know, like, that was, you know, they went and destroyed all the looms because the looms were the automation of the day. But I don't think it'll be like that, but there's going to be something going on there. It's crazy, man. So I maintain, start building robots, folks. It's the only job in the future. Yeah.

**Dave Jones:** No, I think there'll be a niche market there for taxi drivers who actually want to talk to you.

**Chris Gammell:** What about... What's the one in Total Recall?

**Dave Jones:** Johnny Cab. Johnny Cab. Welcome to Johnny Cab. Yeah.

**Chris Gammell:** That bobbly head.

**Dave Jones:** How's your day?

**Chris Gammell:** The other thing I wanted to mention...

**Dave Jones:** Sorry, no. It was a hell of a day, isn't it? Oh, sorry. That's right. Yeah, yeah. That's what he says, yeah. Yep. We will have to make that the graphic for today's Ampour.

**Speaker ?:** Oh, I like that.

**Dave Jones:** Where, you know, Arnold Schwarzenegger is, you know, like choking Johnny Cab. Johnny Cab. Yeah. Yep. If we can find that image. Okay.

**Chris Gammell:** Did you see the thing about plastic chips? Plastic what? Plastic chips.

**Dave Jones:** Plastic chips. Oh, come on. Yes, I did see it.

**Chris Gammell:** Yeah. I don't really agree with this yet. I think that the molecular imprints folks are interesting, but I don't think that that's the way forward. I don't know if you know what that is. It's basically like a stamp, basically. Yep. Yep. I don't think that's the way.

**Dave Jones:** No. Even you admit your goals. No, no.

**Chris Gammell:** I think it's coming. I just don't think that's. No. I think that the, like, what makes the stamp then? That's the idea is like.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** That, I mean, maybe that's etched or something. I don't actually know how they make the actual stamp itself. But the idea, so the idea we're talking about is like they, they put down this liquid with like an inkjet and then to get the additional resolution, they use a physical means, which is the stamp. So it's this molecular imprints does like a, they press it down and then that fills these little divots and yada, yada, yada, yada, yada. But like the idea, like, even if it's that small, how do you maintain those divots over like multiple impressions? Right. That would be the tough part. Right. So I don't think that would be what it was. I like it that it's, it's like the whole idea. Oh, yeah, no, it's cool. Yeah. Well, no, no, no. I mean, like the difference. So a lot of people, when they talk about like printing chips and they're just kind of printed technologies, they always do rastered. Right. So like scanning across with lines and they might do laser, laser ablation, stuff like that. That's just never going to work because it's too slow. Right. That's the difference between like a FDM 3D printer versus an SLA one. SLA, you just single shot. It just, oh no, some of those raster, I guess.

**Dave Jones:** Yeah. No, it does.

**Chris Gammell:** What's one that doesn't raster?

**Dave Jones:** No, I don't know.

**Chris Gammell:** There's some that don't raster. They just do a single shot.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** The single shot always goes faster because you just, it's, yeah, the resolution's harder to get. Parallel. Yeah, exactly. It's parallel versus serial. Exactly right.

**Dave Jones:** Yeah.

**Chris Gammell:** I'll keep holding up.

**Dave Jones:** Can we stop talking about chip printers? Getting nervous? Can we actually get back to what matters that I've seen Star Wars and you haven't?

**Chris Gammell:** I think we have a more important thing and it's actually back to the Steam Controller. Next week, are you ready for this?

**Dave Jones:** Yep.

**Chris Gammell:** Jeff Kaiser returns to the show.

**Dave Jones:** Yes, sir. Yes, sir.

**Chris Gammell:** Well, I think this is going to be the second year straight that he will be on our Christmas adjacent show. So, I'd like it. I like this as a trend. It's all right. See you then. Yeah, man. See you then. I'm excited. bye

**Dave Jones:** this isn't nearly as smooth as the uh

**Chris Gammell:** as the apple we're using but it's uh it's cheaper too i mean that's the other thing we were we were sitting on when we were sitting waiting it was charging us man oh yeah but

**Dave Jones:** we've got money for that that's why we've got patreon i know patron supporters i was just i

**Chris Gammell:** was telling a friend the other day i was like no yeah i know i know uh i was telling a friend though the other day i was like it's a totally new experience paying for phone calls totally new old experience
