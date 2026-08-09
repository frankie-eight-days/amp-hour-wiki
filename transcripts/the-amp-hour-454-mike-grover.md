---
episode: 454
title: An Interview with MG (Mike Grover)
url: https://theamphour.com/the-amp-hour-454-mike-grover/
---

**Mike Grover Mg:** This is the Embar Podcast. Released August 11, 2019. Episode 454. An interview with Mike Grover, or MG. Hey guys, Chris here, and we are deep into the conference summer season, and that's where this episode comes from. This is another on-site recording, and hopefully you're enjoying these. I try and do them where we're actually in the thick of it. Obviously, we're not trying to record while we're in the middle of a crowd, because that would be really loud, but I really like when our guests are doing something with their hands or talking through something, and you'll hear that that's actually the case here. Always love to hear your feedback. If you do or don't like this format, I'd love to hear it. I always still think of the episode. My favorite one is recording the episode on the boat, just because you had the background sounds there. I thought that was a lot of fun last year. And hopefully, you know, that's something that is not going to be every episode. We strive to have good sound quality here at the Amp Hour, but, you know, once in a while, just to be in the thick of things, you know, reporter-in-the-field type of feeling. This is recorded at Black Hat, or rather, you know, after Black Hat one day. I helped out with a training there, and it was a lot of fun, and you'll hear about that here. But people have been asking me, why am I doing stuff with the security? You know, why do I go to security conferences? Because I'm very, very obviously not in security. I, well, I'm just, I don't know what's going on most of the time there. And the answer is because people are doing interesting things with hardware and getting into hardware. And that's kind of the crowds that I like to be around. Obviously, there's badge life as well, which is, you know, people making circuit board-based badges and doing interesting art and code and wearables, kind of all in one. That's, you know, and that's a lot of fun. And it's not necessarily just the crowd that I'm going for, but I think that the security industry as well are realizing how accessible hardware is. And then, as you'll hear us talk about here, it's being pulled into their everyday activities, and it's making the world more secure as a result of that, because it's no longer just a matter of, oh, well, hardware is something that's inaccessible for most people. Now it actually is accessible. So that's kind of why I keep going to security conferences, aside from just the, well, it's really fun side of things. So speaking of, I will be at Chaos Communication Camp, which I think is based around, I mean, the Chaos Communication Congress is security-centric, if not, you know, started from that. But I will be out of that in Berlin next week, and I'll be out there with Alvaro and Jeff Kaiser, or Mighty Ohm, and we'll be recording out there a little bit as well, hopefully. So more shows like this coming up. If you are going to be there, I'd love to talk to you. I'd love to hang out. So please let me know. My DMs are open on Twitter, and you can always email me, chris at theamphour.com, if you're going to be there. If you have any thoughts or feedback about this style of episode, or really the Amp Hour in general, you can always email me or feedback at theamphour.com if you want to go to me and Dave. So that's all for now. We're going to jump in here with MG and enjoy this episode about hardware and the security industry. Did I admit to you yet? Nothing yet. Okay, cool. Welcome to the Amp Hour. This is Chris Gammell of Contextual Electronics, and this is... MG. What's up, MG?

**AT-Tinny's:** Mike River, if you want to call me that.

**Mike Grover Mg:** Yeah, okay. So we're recording as we put together cables, getting ready for Arsenal, which is part of Black Hat. We also have a peanut gallery here in the form of Peter and Joe Fitz. Hi. Hello. And we are currently super-gluing cables together for this Arsenal thing, and this is going to be an implant session. But Mike, you are also into implants. Can you tell us a little bit about it?

**AT-Tinny's:** Yeah. A few years ago, I started playing around with AT-Tinny's as cable implants. Can you define what an implant is first? Yeah, definitely. So the implant has got an existing piece of hardware, and, well, in my case, the implant becomes malicious, but there are alternate types of implants out there. The most notable in the media, at least, become the malicious types.

**Mike Grover Mg:** Right. People care about the stuff's attack. And you share a bunch of these things on Twitter, which I had not seen, and then you handed me back the cable that I had let you borrow right after I saw the video. And so I was a little scared. Right while I was presenting, you were watching. It was great. Yeah. So what was that attack? I mean, we'll share the links, too.

**AT-Tinny's:** Yeah, yeah, definitely. So the base of the attack, regardless of which piece of implant hardware I'm using, has been revolving around something called an HID attack, human interface device. Typically, this is a keyboard. If you're familiar with Hack5's rubber ducky, that's kind of the classic example of this. And what you've got is a small device of, I mean, it can be any size, really, but we're talking implants here, so small. It's a device. It can be an AT-Tiny. It can be just some microcontroller, typically.

**Mike Grover Mg:** Yeah, this would fit inside an actual cable, too.

**AT-Tinny's:** Yeah, yeah, exactly. And, you know, typically they're thumb drives, but this one was fitting inside of a USB cable that looked just like a USB cable. Yeah. And what the HID attack does is it presents itself to the computer, typically as a keyboard. You can also do mice. There's a lot of other things over USB. And you've got, like, a script pre-built that goes into the microcontroller. Sometimes you can do it remotely, but it presents itself as a keyboard and then types a predetermined script. You know, so it's as if I were at your computer on your keyboard typing.

**Mike Grover Mg:** Yeah, it looked like the beginning. So you showed this on a Mac, and it looked like the beginning it was, like, command, spacebar to pull up a prompt. Yeah. Then you opened a terminal, and then you started typing stuff in from there.

**AT-Tinny's:** Yeah, yeah. Yeah, that's the – there's a bunch that I use, and they're very – at least when I show them off, they're oriented towards being very visual so that the audience knows what they're seeing. Right, right. You know, in red teaming type work, which is what I do currently, that you don't want that if your target is there. Yeah, you actually want it to be as fast as possible, low-key as possible, so that it does not get noticed.

**Dave Jones:** Hide the windows behind others.

**Mike Grover Mg:** Yeah, which is a thing. Yeah. When you showed that one that was – it pulled up the screen – what was the screensaver thing?

**AT-Tinny's:** Yeah, yeah. So Buddy Lewis – Let's trade these. Trading cables here. Yeah, definitely. These get super glued, right? Yeah, yeah. Okay. Yeah, Buddy Lewis, Black Sun Research, has – he built a payload, basically. It's just a binary, right, that you open it up on the machine, and it emulates exactly what you expect your lock screen to be, so that, you know, it's got the background all fuzzy, like on a Mac anyway, that you would expect to see. Your user name's there, your user icon's there, password field's there. But it's not actually your lock screen. It's a binary that we, you know, put on there, and it validates your password. Which is super creepy. Yeah.

**Mike Grover Mg:** It's like the imagining – it's like looking into a mirror, and then suddenly, like, your face turns into a clown. Yeah. It's like something like that, you know? It's like that kind of – Exactly. It's so out of the ordinary to see something that's bad. Right.

**AT-Tinny's:** Like, you don't expect that. It's like, no, to be phished or something like that for my password, I have to click on something first. Right, right. It's very active. Well, turns out I've got control of your clicker.

**Mike Grover Mg:** So that's – exactly. And your brain, which is like, you know, the biggest clicker of all.

**AT-Tinny's:** Yes. And, yeah, in that example, it was kicked off in a very quick, relatively silent HID payload. So it took about four seconds of on-screen time, and then it minimized – it basically quit out of all the environments that would be visible to the typical user and processed everything in the background. And then kicked off the fake screensaver, lock scream, if you Google that. S-C-R-E-A-M, because it makes you want to scream. Yep. And, yeah, and it validates the password before it even lets you in. It's really hard to quit out of it. And then it emails me your username and password. Hey. And now let's say I have remote control of that. That one needs to be glued. Sorry. This one? Yep. And now let's say I have remote control over your – or over the HID implant, right? Uh-huh. And we put a wireless interface on that, which is something I've also been playing with. Yep. So now I've got your username and password, and that's what you need for a lot of things on a computer these days because, you know, you need administrative access to execute certain things. You know, good security. Right. But it becomes fairly, you know, visually noisy when you're doing stuff. But what if you just wait until this person has gone to sleep or you know they're at lunch, but now you've got their local admin password, which allows you to log in. And, you know, nobody's going to be looking at the screen, so you can push a new payload that does all the really visually noisy things while they're away from the machine. Even if they're really good about locking their computer before going to lunch or going to sleep. Well, you can unlock it and kick these things off.

**Mike Grover Mg:** Which I got yelled at for this weekend by Fabian, who also has been on the show. Fabian was also a trainer at this training that I helped out with, or that Mike did too, and Peter and Joe ran it. That was fun. And Fabian yelled at me because I left my screen unlocked.

**AT-Tinny's:** It was a gentle reminder.

**Mike Grover Mg:** I was gentle. Yes, that's true. There may be some people lurking.

**AT-Tinny's:** Malicious individuals.

**Mike Grover Mg:** Do some bad things.

**Dave Jones:** You didn't have friends in your past that were leaving stuff in your .profile? Yeah, right. You just didn't lock your screen?

**Mike Grover Mg:** I guess not, yeah. I guess I don't hang out with those types. Yeah. So, okay. Well, that's, I mean, those are some pretty scary kind of things. But who's using these kind of things? You mentioned Red Team. What does that mean?

**AT-Tinny's:** Yeah, yeah. So, within the InvoSec space, we've got, you know, in terms of the team colors, right, the classic ones are going to be blue and red team. Red is offense. Blue is defense. So, you know, blue is going to be your typical, you know, kind of what you think of the teams protecting a company, making sure.

**Dave Jones:** That's a military term terminology.

**AT-Tinny's:** Yeah, there's a whole lot of military terminology that gets kind of pulled over. Sometimes that's not so good in the things we want to convey. But, you know, that's for the sake of common terminology at the moment anyway. Yeah, that's what most people are using. There's a variety of other team colors, depending on what we're trying to convey. But for most of that is kind of done internally. But, yeah, so you've got the defense side. And then offense, you have Red Team, where everybody's got a different definition. But the correct one is emulating real-world adversaries as much as possible. You like the bad guys on the area. Yeah, exactly. So that helps test defenses and stuff. No, this is distinctly different than pen testers who are given a scope of, you know, look at my front door and make sure you can't find weaknesses. Versus Red Team's like, can you get through the front door? Right, right. And front door, you mean like a website or something? Well, I mean, it could be your physical front door, honestly. Okay, sure. But it's just because as a simple allegory there. It's like a lot of Red Team jobs are like, here are the crown jewels. Can you get to them? Got it. Versus enumerate all the ways you could get through a specific layer. Got it. Just get all the way to them. So, you know, yeah, absolutely things like this come into play for doing the job. It's also a portion of my job is security engagement. That's kind of engaging the staff and the employees within a company to get them aware of certain things and interested and caring about them. So that also comes into play. It's where you can do awareness training and showing off this cool thing that's producing interesting noise and scary stuff on the screen. Right. Because it shows off in an easy to understand way why you should actually, you know, lock your computer and things like that. Even though, yes, there are ways of bypassing that. It makes it much harder. Right. The more you do. There's no perfect security. But elevating that bar is always the key. It's like, just do more. Make it harder.

**Mike Grover Mg:** Right. Well, that's what we always. So, you know, we've had security people on. Obviously, Joe's been on the show. Yep. Other people that we hang out with here at Black Hat and DEF CON and stuff like that. And it seems like the resounding message is always like people are the soft spot. It's always, you know, and so it sounds like that's kind of tied into. Absolutely. Making sure that they're not that soft. Yep. Or less soft.

**AT-Tinny's:** And a lot of that, you know, there's a lot of, I don't know, certain type of attitude within a lot of InfoSec where, well, you know, the people are stupid or something like that. And, you know, I really disagree with that because it's just bad. It's a bad system. Right.

**Mike Grover Mg:** It's like us versus them instead of like let's all learn together.

**AT-Tinny's:** Yeah. And ultimately the fact that it is on, you know, the end user in this case indicates a bad system has been built. Yeah. Like it shouldn't be. So really, you know, even phishing, right? Like if it was so easy to detect phishing, well, you would have created a script or, you know, something, some piece of technology that catches it for them. Before it gets to the end user. That's right. But you haven't. So, you know, blaming them. Well, no, no. Let's not do that. Let's actually just admit that these, that anytime the security falls on the end user, it's because they have to augment incomplete and generally, yeah, just incomplete security model.

**Mike Grover Mg:** Yeah. Should I move the mill to the room? No, no, no. That's background noise. Yeah, background noise. So Joe's going to be milling PCBs here. And that's actually a good segue too to other stuff that, so this is actually how I first learned of MG is the, and this is actually how, Joe, is that how you and Mike met as well?

**Chris Gammell:** We met over some of the USB stuff.

**Mike Grover Mg:** Okay.

**Chris Gammell:** Last year at DEFCON.

**Mike Grover Mg:** Yeah, so they had met at DEFCON last year as part of this, but Mike does amazing stuff with other mills or Ben's some tools and milling PCBs. And, you know, I really was grateful to be able to sit there and, you know, watch you do this stuff during the training just because it was like, some of it made it more accessible. You know, Dave and I always talk about, well, a lot of the times for like higher complexity boards, it's not really worth it, but I really like the rapid iteration type stuff.

**Dave Jones:** What I have to say is like the accuracy he gets with this board, it blew my mind. Oh, yeah. It's like seeing it in person, how fine actually the traces are. I did not give enough credit to the mills before I saw your work, including soda stuff. It's like you have that too, which is amazing. Soda mask? Spoilers. Soda mask.

**Mike Grover Mg:** Spoilers, Peter. Come on, we're getting to that. Sorry, sorry. Jeez, this guy. Always. Nice. Yeah. So how did you get in? Like, how did you start doing all this stuff?

**AT-Tinny's:** So, yeah, let's see. When it was roughly two years ago when I wanted to chase the AT Tiny approach to this, I mean, ultimately, you know, let's rewind right to then. What inspired me? On Twitter, I saw just a picture of a thumb drive with a firecracker inside of it. And, like, I have no idea if it worked, but you immediately had like this visceral reaction. The same one everyone had. Some people were concerned. Some people were like, that's awesome.

**Dave Jones:** You're saving it too. Yeah.

**AT-Tinny's:** I mean, I didn't make it. I saw it. And, you know, immediately I was like, oh, what if I combine that with a rubber ducky? Because then you could take, you know, the HID attack and then somehow mix in. So the rubber ducky, you have like a very basic scripting language that says, you know, type this, do this, delay. I wanted to add in and explode after command. Because it would be interesting depending on how you did it. Maybe have confetti go everywhere. That's, you know, what was in my head, right?

**Mike Grover Mg:** It doesn't have to be an actual, like, violent thing. It could be an interesting showcase-y kind of thing like you were talking about.

**AT-Tinny's:** Exactly. So the quick thing I realized after cracking open a rubber ducky from, you know, Darren's Hack 5. That's right. Is, you know, it takes up the full space with the flash drive as you'd expect. I'm like, wow, where are... Those have been out for a while though, right? Yeah, exactly. I mean, they are like, they were kind of what set the bar for what that is. And, um... Is that Miller, right? So it was clear that what I would have to do is get the functionality of ducky, at least roughly to some extent, right? In a much smaller package so I'd have more room for activities inside, you know, explosive activities. So that's what I started chasing. You know, there's all kinds of things out there that people have reproduced HID-type attacks on different hardware. Teensies, ATtiny, Digisparks. You know, I started just trying to figure out what is the most minimal circuit. And figured out, you know, the ATtiny is probably the pathway I want to go. So, you know, picked up a Digispark and started cannibalizing a whole bunch of them to figure out the minimal circuit. Got it down to, what, three resistors, two zener diodes, the ATtiny itself. And I think that's it. Nice. Which is, you know, minimal. And, you know, got it into a footprint that, a double-sided PCB that wasn't really... It was done on, like, proto-board and, like, copper tape. Because I didn't really know how to make a PCB. I could draw the circuit. It was like the grid system. Yeah, yeah. The product is, like, SMT pads. It's basically just a bunch of little copper squares on a panel that you're supposed to be able to, like, bridge together for surface mount stuff.

**Mike Grover Mg:** Yeah, so if the people that are listening, we've talked about the Manhattan method before. It's where you have, like, you cut out those things yourself and then you put them on a big ground plane. Yeah. It's kind of like that, but just, like, already pre-cut. It's like they V-scored out copper, effectively, to make them into islands, right? Little square islands.

**Dave Jones:** Instead of separating, you connect this way.

**Mike Grover Mg:** That's right, yeah, yeah. They're already pre-separated, exactly.

**Dave Jones:** Okay, that's cool.

**Mike Grover Mg:** And so that was kind of the first pass at it.

**AT-Tinny's:** Yeah, that was the first pass, and it worked, right? Like, I, you know, took that circuit, added, I, you know, added another resistor and a MOSFET to get the physical trigger portion of it. So it was another GPIO penny, essentially, that would, you know, open up that gate and, you know, use some resistance wire to set off, you know, something fun to throw confetti everywhere. Yeah, it was great. It worked. And, you know, people were like, hey, I want to reproduce that. I'm like, man, I don't know how you're going to do that. This is horrible. So, you know, it pushed me to make a PCB. And that was, man, that's when I was first looking at, like, things like KiCad, Eagle, et cetera. And there's a pretty big learning curve there. I haven't noticed. Yeah, yeah, exactly, right? You haven't noticed.

**Mike Grover Mg:** Joe, what do you think? You're a new KiCad user?

**Chris Gammell:** Oh, yeah. I wrote some instructions to teach people how to use KiCad, and then I followed them, and I learned quite a bit from my students. Nice. Luckily, there's lots of really good resources. And it turns out I have a couple friends who know how to use Krat and use it on a regular basis. Nice. And they were silly enough to come join me for Black Hat.

**Mike Grover Mg:** That's silly. That's great.

**Chris Gammell:** Thank you for having us.

**Mike Grover Mg:** Yeah, that's great. So that was kind of the first step into it. It was kind of a shock to the system at first, but then... Yeah, a bit.

**AT-Tinny's:** But although the thing is, like, I could draw the PCB.

**Mike Grover Mg:** Yeah. Oh, yeah, right.

**AT-Tinny's:** But the thing is, getting over the hurdle of KiCad, I was like, that was too much at the time. Like, look, I know how to draw this. Like, just give me something more simple. Yeah, you want to just make that replica of the thing in the real world. I ended up... Somebody showed me... I can't remember if it's PCB Express or Express PCB. Anyway, their whole model is like, we'll ship you a board. I don't even think they cut it out. Honestly, like, I got a panel of, you know, these little tiny things that I was dremling out. But their model is like, really, really easy software, because if it's not easy, you're not going to use their software. That's right. Or their service. So, yeah, I used that. And yeah, it worked. Cool. Yeah. Kicked out a couple panels. And there we go. That was like, the first attempt at that. Uh-huh. And then about a year later, you know, I got tied up in work and all this stuff. About a year later is when I revisited this concept. I'm like, you know, it would be really cool to extend this and actually make this attack wireless and just see how much more I can do. Yep. So, that's when I decided, okay, it's time to pick up some software, right? And it ended up being Kikad. Yep. And also, it's like, okay, well, I still don't actually know what I'm doing. I don't have an EE background. I was an IT generalist for many, many years. So, it gave me, you know, a fundamental understanding of a lot of things, but not at an EE level. It's like resistors, like, they resist. And capacitors, they're basically just batteries. batteries. That's all I thought. You know, I didn't realize filtering and all these other things. Sure, sure. Like, the Zener diode, that was magic. I'm like, wait a second.

**Mike Grover Mg:** Well, that still is even if you have an EE background.

**AT-Tinny's:** Oh, yeah, yeah, exactly. Like, okay, diodes I kind of get and, you know, everything else. There was so much learning to be done in the circuit I would eventually create. But the other mill that I picked up, the used other mill, right around the time Joe was picking these up, like, he actually had bought all of the used other mills in existence the day before I went looking for one. And, you know, luckily I found one in the local area a few days later. But I picked one of those up. And the really interesting thing is the way I go about learning stuff, like, within code anyway, it takes some existing code. Sure. You start modifying stuff. You compile it, run it, and see what changed, right? Right. You kind of understand you have a general intuition of what will and won't change. But there's a lot of, you know, break, test, break, test, break, test. And it's way harder to do. Right, it's the iteration cycle you're talking about. Yeah. Yeah. Like, to some extent, on simple circuits, like I did with the DigiSpark, that kind of works for, like, reversing it. You know, I still went through probably, like, 10 or 15. So, like, oh, that's too much, or I shouldn't have removed that because I just fried something.

**Mike Grover Mg:** And what is the DigiSpark?

**AT-Tinny's:** The DigiSpark is basically an AT-Tiny85 that, you know, bit bangs USB. Bit banging is probably very familiar to your crowd. Can I be explaining? But, yeah, you know, we're a microcontroller, like an AT-Tiny that does not have USB, has the microcontroller turning on and off. GPIO lines rapidly to simulate the digital signal that is USB. Right. That's bit banging.

**Mike Grover Mg:** Instead of having the physical, the controller chip, the USB controller in there.

**AT-Tinny's:** Exactly. Yeah. That's cool. And I forget where I was going with that. Oh, I was asking about the DigiSpark. Oh, yeah, that's what the DigiSpark is. It's a very small package. It's, like, one inch by one inch. Got it. Okay. Which still was too big. I first started, like, shaving off. It just didn't work. I just ripped stuff off. So there was a lot of extra stuff on there, like LEDs. But, yeah, so the mill allowed me to make so many bad circuit boards to the point that, you know, oh, this shouldn't, you know, this pin needs to be grounded. Oh, we shouldn't short it. And, you know, fried a lot of stuff. But I could very quickly turn around a board, push it in the key cad, mill it, you know, 20 minutes later. You know, I was doing double-sided for the most part. So maybe it's an hour. It depends on what I'm trying to do with it. Kick that out, sort of things on, and test it. And that was awesome versus having to send it off to a shop and, you know, wait however many days, a week or two.

**Mike Grover Mg:** That's actually something Joe said during training, which was, like, the number of iterations you get. Yes. It's so much higher than, like, and that really, like, thinking about my early days, like, I think I made one PCB in, like, a year. Yeah. You know, that first time I did it. I wouldn't have learned anything. Yeah, exactly. And it's, like, it happened to work, but it didn't, you know, it didn't get a lot of the, oh, this is going to work, this one isn't. And the cost of mistakes is much lower now. Absolutely.

**AT-Tinny's:** Absolutely. And I can only imagine how powerful that is to somebody who already knows what they're doing and can get things out, like, really fast.

**Mike Grover Mg:** Yeah, but I think that, like, so, like, at least from my perspective, like, I was always holding myself back from that because it was, like, the cost of, because there's physical cost of the parts, too. Like, it's nicer to have, obviously, parts are getting cheaper all the time, more powerful. Yeah. But, like, I think thinking about it in terms of, like, modules and, like, focusing on, like, just building up small circuits at a time as well versus one big circuit. Like, I remember the first, one of my first gigs, one of my first jobs, rather, we were working on boards that were, like, $600 in production. And so, like, they would spend six months on a board rep, right? And there was a huge cost if anything was wrong on it. Yeah, yeah. Yeah, and you'd cut and jump and you'd fix everything as you needed to, but it was just, you know. Interesting. Very, very top-heavy kind of process to do that.

**AT-Tinny's:** Is there software out there that will allow you to emulate a lot of the, you know, the running and the failures that I was testing?

**Mike Grover Mg:** Oh.

**AT-Tinny's:** Shorts, lack of pull-downs, things like that.

**Mike Grover Mg:** I don't think, I mean, like, yeah, I guess you could simulate, like, in Spice or something, but it's not going to be the same as hands-on on the bench, right? Yeah, yeah, exactly. Yeah, and it's just, like, the, I think, getting the experience, like you're talking about, too, it's, like, that's super, super critical. Yeah, absolutely. Yeah. So then you started to make it kind of crazier, though.

**AT-Tinny's:** Yeah. I mean, the first thing, it's way easier to solder when you've got a solder mask, but, you know, the most common method of doing that was, you know, UV reactive solder goo that, you know, spread on the top of the PCB. And then on transparency film, you print out the inverse of what you want to cure. So, you know, the solder pads typically are the black areas, and you expose it for a few seconds, and the black pads block off the light, and then you wash it, wash off those black, what was under the black pads with some alcohol, and then you fully cure it. And it worked. It totally worked. It's just, you know, it wasn't, it was really fiddly, it was messy, a lot of in and out of the mill. You also have to, like, get the alignment, right? Yeah, the alignment was so fiddly. And, you know, the printer I was using was literally the cheapest I could find on Amazon, because I bought it for this. So, you know, little holes in it that you'd have to, like, paint over, triple up the transparency. It was all right. But I did it once and realized there's got to be better. Yeah. So, like, hey, I got this mill in front of me. It has a Z depth granularity of, like, point, I think it's 0.01 millimeter. Uh-huh. Like, man, that's got to be enough. Like, 3.7 mils or something? Oh.

**Mike Grover Mg:** Is that 37 mils to the millimeter? I can't remember. Or 0.... What's... 0.01 millimeter. What's that in mils? 0.01. I don't remember. Yeah.

**AT-Tinny's:** I'll look that up while we talk. Yeah. But, um... I'll do it, yeah. Yeah. It was so tiny. But, you know, the board has to be very flat. But ultimately, what I did is just cured an entire layer of solder mask over there. Yeah. And then I would feed the, um... The inverse of that, basically. Or you could also use the paste. Right. You know? Right. Because that would then... Yeah, exactly.

**Mike Grover Mg:** ...approximate that space where you're trying to get something done. Exactly, yeah.

**AT-Tinny's:** You know, figure it out there. Basically, turn that into an SVG and import that in as, like, an engraving layer. And just slowly nudge the head of the mill down until it's just hovering over, maybe slightly going into the copper sometimes. Right. Um... And that worked. And, you know, you've got copper exposed underneath. So...

**Mike Grover Mg:** So how thick was... So, first off, it's 0.394 mils. That's how... That's the Z-height resolution.

**AT-Tinny's:** That's tiny.

**Mike Grover Mg:** Yeah, that's crazy. So, what is the, uh... What was the thickness of the solder mask you were putting on there?

**AT-Tinny's:** Uh... Oh! So, I'm not actually sure. Basically, what I would do is lay down two strips of scotch tape. Uh-huh. And use that as kind of a shim. Uh-huh. Just two parallel ones on each side of the board. Uh-huh. And my boards were, like, all of them are basically one square centimeter. Right, right. So, it worked. And then take a credit card and just skim the solder paste down that.

**Mike Grover Mg:** And it leaves a... Oh, I see. So, it's like a... It's like a ad hoc solder... Or solder's paste stencil.

**AT-Tinny's:** Yeah, very similar. So, you get that thickness though, you're saying. Exactly.

**Mike Grover Mg:** Interesting. And then you just cook that.

**AT-Tinny's:** Okay, so the thickness of a piece of tape. Yeah, exactly. Exactly. So, the thickness of scotch tape. Uh-huh. And then when I say cook it, uh... You know, expose it to UV light. Yeah. Uh-huh. Uh-huh. For however long. A couple minutes. Depends on the color, actually. Black is a pain to cure. Yeah. Because it takes more to absorb my light. Yeah. Same with white, actually. Because it's still... Uh-huh. You know, it's not as anywhere near as transparent as the other stuff. Sure. Sure. But, uh... Yeah, and then you just engrave out the other portions of that. Now, uh... It's good saying here. I would... You know, a few months later... It still was never good enough because you have to be really careful. Because the board itself is never perfectly flat to that degree of granularity. Sutter? Okay. You need a solder? No, I just need a cable. No, that's fine. It's fine. Okay, cool. Um, so... Yeah, it was never... The boards were never that perfectly flat. And when you're dealing with... I think the copper is either half ounce or one ounce at best. Yeah, right. Really thin. So, you get barely any degree of error there. So, sometimes what I would start doing is visually check. It's like, oh, this part of the board, copper is exposed, but not this part. So, I start adjusting the SVG and, like, covering up the pads and just keep moving it along. You know, it worked. And you probably could automate that. But ultimately, in the CNC world, there's something called drag tips, which took me months to get to this point. But drag tips are basically... It's kind of like a pogo pin.

**Mike Grover Mg:** Is this like the circular thing for probing, or is this a different thing? Um... Oh, drag tips, you mean it's like an adjustable head?

**AT-Tinny's:** Yeah, it's a spring-mounted engraving tip. Oh, wow. So, I'm using engraving tips. They're very... They're just like a V or sometimes pyramid-shaped. Right. But you get a very sharp point at the tip of the mill, or the end mill, which is typically .005 mils. Crap, I can't remember. .005 millimeter? No, these are mils. I can't remember exactly. I'll have to look them up. But a very, very small engraving surface. Got it, got it. That allowed me to do QFN and some very light BGA stuff eventually.

**Chris Gammell:** Wow.

**AT-Tinny's:** As long as there weren't any center pads, of course. Right. But ultimately... Where was I going with that? The...

**Mike Grover Mg:** You're talking about the adjustable height engraver tip thingy?

**AT-Tinny's:** Oh, yeah, yeah. So, the drag tips. These are... You take those and stick them inside of a larger enclosure that allows the whole thing to be spring-mounted. Wow. And this is... It's for engraving, typically on like glass or some hard surface. So, basically, the spring then kind of determines how much it's pushing down. Exactly. So, you increase the Z-depth and it increases the pressure. Ah. So, via the spring. So, I actually loosen them up with some like feather-light springs. Uh-huh. Really light. And you slowly drop it into place. Uh-huh. And then you've got a lot more margin of error because the solder mask is way softer. Uh-huh. So, it bites through that real fast. Yeah. And then when it touches the copper, it kind of just hovers over there. It probably skims off a tiny little bit, but almost none.

**Mike Grover Mg:** Wow.

**AT-Tinny's:** Like, I wasn't going through just instantly. You got to make sure that the tip does not kind of be... It doesn't drift off of the copper. Uh-huh. Because FR-4, which is primarily what I was using, you got to be careful with that because it's fiberglass. But as soon as it would touch off the side, it would just bite much deeper. Uh-huh. So, make sure, you know, the milling pattern keeps you on the copper. And then that tip worked really well. There's a lot of them out there and I'm still experimenting. Uh-huh. The right one, but I want to find something that's very cheap for everybody to be able to access.

**Mike Grover Mg:** Right.

**AT-Tinny's:** Getting close.

**Mike Grover Mg:** Yeah. That's good. That's good. Okay. Um, okay. So, we're going to switch tasks. We're not going to switch topics. We're going to switch tasks, though. We're going to switch over to folding stuff. This is definitely a hands-on kind of thing. Oh, thank you. So, you mentioned BGA as well. So, like, what are you... I guess maybe the question that I really should ask is why not take it to a PCB fab and just, like, keep iterating like that? Definitely. Like, having... So, one thing that I've seen is, like, a pipeline of, like, you know, you have a bunch of boards coming back. From a cost perspective, it's a little bit higher, but from a, you know, what's on there, it's a little bit more process controlled.

**AT-Tinny's:** Yeah, definitely. So, I mean, it's definitely the right pathway in a lot of instances. For me, the first thing that kind of restricted me from wanting to do that is that I didn't have any experience with these things. Sure, sure, sure. And it's like, okay, well, you know, how do I know the pinouts or what I need it to be? Like, half of these components, regardless of what form factor the package was in, didn't have experience with them. So, that was part of it. There's also, you know, okay, I get the board back. Oh, how am I going to put the BGA on?

**Mike Grover Mg:** Right, are you going to do it? Yeah, if you don't have the knowledge of that stuff.

**Speaker ?:** I don't know.

**Mike Grover Mg:** It's like, I've never soldered BGAs to a board before. Sure, sure. So, it was just more of a privacy kind of thing, like a...

**AT-Tinny's:** Just test it out. Yeah, try it. Learn how. Get a general idea first, and then, yeah. I'm sure. I guess you probably learned a lot of the tough things up front. Yes. I mean, even things like, do we do solder mask-defined or copper-defined pads and things like that? Yeah. I could at least test that out, and the difference is, and luckily, the BGAs I'm working with, while probably small in pitch, I think they were going down to .35mm pitch. Whoa, really? Yeah, yeah, exactly. Whoa. And I got those on the mill just barely, and I can explain that. Yeah. But they were all, luckily, nothing was a center pin, so we're dealing with like four and six ball BGA components. Uh-huh. And when you're, you know, shoving stuff inside of a cable and just very tiny implants, that does become pretty important. Sure.

**Mike Grover Mg:** Yeah, some of the size constraints that you have are pretty... Like, what are the envelopes of the cables that you're looking at here?

**AT-Tinny's:** Um, the ultimate PCB, uh, just the, yeah, the entire envelope is going to be roughly, let's call it 11 millimeters by 8 to 9 millimeters. Okay. So it's a, yeah, tiny, tiny little thing. Yep, yep. So, you know, I got a lot of experience there, and it's hard dealing with these. You know, home reflow, the whole thing. Sure, sure. At home, so.

**Mike Grover Mg:** Kind of set up like a bespoke PCB, like advanced PCB manufacturing service without, yeah. It's, it works. It's kind of relearning everything, too.

**AT-Tinny's:** And, and ultimately, you know, we're here at Black Hat and DEF CON, and I decided, didn't have enough time to go through the process with an assembler for some of the cables I'm making, so, yeah, I did that at home. It took me hours per board with high failure rates, but, you know, it's what I know now. Yeah, right. And hopefully soon I will know, you know, the process with manufacturers to do that.

**Mike Grover Mg:** Right, right. So, see how much, and that'll be interesting, too, is like seeing like as, as you were like able to give them recommendations and stuff, too.

**Chris Gammell:** Yes. Thank you, Jesus.

**Mike Grover Mg:** So, seeing what, what they do. We have Peter and, and what are you going, what are you going on there?

**Dave Jones:** Oh, I'm making pogo pin adapters.

**Mike Grover Mg:** Oh, that's right. So this is actually something, this is what Joe and Peter were talking about. They've been doing like a kind of vertically mounted, like off the edge of a PCB to get like a finer pitch. And it's pretty tough to do, actually, just because the pogo pins kind of roll, you know?

**Dave Jones:** Yeah.

**Mike Grover Mg:** So that's a tough thing to do.

**Dave Jones:** Yeah.

**Mike Grover Mg:** But it's good for, for doing, uh.

**Dave Jones:** Now Joe gave me like modify it and now I'm screwing up. Right.

**Mike Grover Mg:** Well, it's almost like the, what's that cable type? The, the tag connect. Yeah. Oh, tag connect.

**Dave Jones:** It's a lot cheaper.

**Mike Grover Mg:** Yeah, it's like a homemade cheap tag connect.

**Dave Jones:** I actually make my own tag connect. Esk things. Esk things just with connect, with taking a connector, soldering the pogo pin to the connector and then molding over with the hot glue around to have a handle. That's good idea. It works great.

**AT-Tinny's:** Yeah. See, that's the other thing the mills are great for. That type of setup. I need, I need a breakout board or whatever it may be. Even with components. So I, basically every component I ended up using, uh, I create a breakout board for it. Uh-huh. It breaks out to 2.5 millimeter pins, right? Right, right, right. So I can breadboard on it. Yeah. So I can breadboard on, you know, these sub one millimeter BGAs. Right. It's great.

**Mike Grover Mg:** Right. Which is kind of crazy too because even when you buy a dip part these days, it's effectively the same thing. Just internally, they're bonding out the chip, the tiny, tiny bit of silicon up to these huge lead frames. Yep. So it's, uh, that's good. That's good to be able to do that. And it really opens up a lot of, of capabilities for you. Definitely. Things that I would, might just discount and say, oh, I can't use that part. Yeah. I need a bigger lead frame thing. Yeah, definitely.

**Dave Jones:** Yeah. After the workshop, I'm definitely like, oh, maybe I should have one of those nails actually. Handy.

**Mike Grover Mg:** With help. I think a lot of people walked out of that, uh, walked out of that workshop thinking that. And it's, I mean. I wish they were not as expensive though. Yeah. Yeah. So like, I'm not affiliated with them in any way. Yeah. For the record. I just think it's a good, good, uh, tool. Yeah. Yeah. Well, so when would you say someone should get one then?

**AT-Tinny's:** Oh, uh, it's a, it's a personal decision, but, um, I mean, there are a lot of different types of mills out there. Uh, it depends what you're milling. I like the enclosed nature of that. It's not fully enclosed, but there's vacuum systems you can put in it and, and further helps for FR4, which is going to produce a lot of glass dust, which you don't want to inhale. Yeah. Um, probably hook up some vacuum systems, uh, cheaper open rigs and stuff like that. Yeah. 3D print some holders or something like that. Yeah. Uh, you know, it's your health if you make your decision. That's right. But, um, yeah, it's, it's kind of depends on, it's a, you know, it's a very budget versus capabilities. What do you have access to already that can augment some of this? Yeah. What did you guys pick yours up for? So you guys, you both got them used. Yeah. I got a used, uh, like four or five year old modern model for about 900 bucks. Oh, that's not too bad. Um, what'd you do?

**Chris Gammell:** I got the, uh, Bantam tool, uh, sorry, Bantam tools mill as well as, uh, two other mill pros, which are the current model. Uh-huh. Um, and I got them between like 2,000 and 2,000 each.

**Mike Grover Mg:** Okay. Okay. All right. So like 30, 40% off premium. Yeah. Off on retail, right? Yeah. I think the list is 3,400. 4,000. Oh, did they just go up? Bantam went up to 4,000. We were looking at it with some of the, some of the students in the class were doing stuff. Yeah. The crazy click count. Yeah. Yeah. Yeah. There you go. Thank you. Um, yeah. And I mean, that, that is an investment. And when you, so like one of the things that I was pushed on when I was buying a mill mill was like, you know, you should really get, first off, get manual milling experience, which would have been good. But then, like, what's the cost of the amount of things that you really want to do? And then how many, you know, how much would it cost to send it out for that kind of stuff? Yeah. Yeah. It sounds like you might be approaching though, that at least the $900 that you paid for yours. Oh yeah, definitely. You definitely probably spent that much in PCB spins.

**AT-Tinny's:** Yeah.

**Mike Grover Mg:** Oh, absolutely. And for me it was education.

**AT-Tinny's:** It was the cost of a milling course or a PCB course. Right. Right.

**Chris Gammell:** With the mill, you can buy time. Yeah. True. And like when we do it in class, we're doing a two day class and you need to like have a chance to make a PCB and see it work in two days. Right. And not only that, you want to have it happen over and over and over again. That's how you learn things. You make mistakes. You see them happen.

**AT-Tinny's:** Great.

**Chris Gammell:** So I got started with small batch PCBs and, you know, I'm always worried about making the patches and I get them and there's a mistake and it takes another two weeks. Yep. So if you can compress six months of learning into two days, then that's when the mill's worth it.

**Mike Grover Mg:** Yeah.

**Chris Gammell:** Yeah. Right.

**Mike Grover Mg:** Well, and especially because you're doing it bundled.

**AT-Tinny's:** Yeah. Right. Right. Right. Or if you can build some educational session less than an hour before it starts. Yeah.

**Chris Gammell:** I have admitted that perhaps the reason I made this class was specifically to buy myself a PCB mill.

**Mike Grover Mg:** We won't conjecture there. That's great. So then you had mentioned you're using FR4, Mike. What are you? So why FR4 versus FR1? FR1 is what is normally used, right?

**AT-Tinny's:** Yeah. So a few reasons which may be incorrect, but I want thinner than 1.6. Oh, okay. My boards are typically 0.6 or 0.8 millimeters with my current needs. It may go smaller, especially if I start playing with more than two layer. Oh, really? Yeah. Soon I may start playing around with that. I see a few pathways to make that happen. I just haven't had a need yet because also when I'm prototyping, I do want the end result to be as close as possible to production stuff. And I prefer to stay in the cheaper two-layer PCB territory because the cost goes up.

**Mike Grover Mg:** Sure, sure. And actually, that's an interesting point, too. So Jeff Kaiser, who's been on the show a bunch, Mr. Mighty Home, he talks about he had an LPKF at a past job, but the hard thing there was he had to redo his board, even the layout around single chips. He was doing it for prototyping. Yeah. But then if you did a larger design, you'd have to go and pretty much redo the design for a PCB fab because you might not do it that way if you weren't making it yourself.

**AT-Tinny's:** Yes, exactly. So there's some variance there. I would say that the end result that goes off to a fab shop, definitely influenced by the mill boundaries to some extent. Maybe I'll shrink the trace width and stuff like that. And I also kind of have found that I need to stop trying to force it to exactly what production is going to be with maybe, I guess, high-speed stuff. It's a great example. Oh, sure, sure, yeah. Unless it's all on one side and kind of get close, but it's hard to perfectly control the trace width.

**Dave Jones:** Yep.

**AT-Tinny's:** There's variances there. But yeah, so the other reason with FR-4, it's also, so with the thickness, it seems to be way more commonly available. I'm sourcing from like eBay and Amazon, mostly eBay. Yeah. And that's, it's all FR-4. Oh, okay. And I guess, you know, because it's just a fab that's like cranking out probably blank boards. Yeah. They're probably just chopping up copper clad stuff. Right. Which makes sense. I mean, that's going to be more available. Right. And it's, you know, of course, more heat resistant. The adhesive that, you know, holds the copper to the substrate seems more robust.

**Mike Grover Mg:** Yeah. So it's a little bit easier on reflow then too. You can kind of give them more heat shock.

**AT-Tinny's:** Yeah. Granted, when I had issues there, it was because I was using like a really cheap reflow station. And despite setting it to like 240, 220, the FR-4 a few times actually blackened. Oh, yeah. Yeah. So I'm guessing it wasn't quite accurate in terms of its heat output. Yeah.

**Dave Jones:** This is the first thing I modify on my Chinese reflow ovens is the thermal couples because they are using, or the thermal couple interfaces. Yeah. Okay. Because they are very inaccurate if you just use up amps that are on their control board. Yeah. Yeah. Right. Right.

**AT-Tinny's:** And they're definitely more mechanically robust too. Yeah. Sure. Sure. Sure. And they're just going to hand them and snap them off of things or just use things that are needing to be mechanical supports. Yep. And that's, it's nice to have.

**AT-Tinny's:** It's like half your paper pile there.

**Mike Grover Mg:** It's faster than me. No, I have a smaller pile. Oh, I see how it is. Okay. So talking about the mechanical side of things then, so like, what are you, so you're building out these cables. Yeah. Are you building out the whole cable? Are you retrofitting? What are you?

**AT-Tinny's:** Yeah. So true to the implant name, I am putting the assembled boards inside of the cables. This does include basically creating a, you get a sacrificial cable effectively and replace the USB-A portion of it with an unused boot.

**Mike Grover Mg:** Yeah. Shell. Shell. And that's actually a good visualization too. So this is on the USB-A side. That's about how much space you're working with. Exactly. Yeah. In terms of Z height as well, which is, you can't really bulge it out.

**AT-Tinny's:** So with, so that's the other thing. Like, I think the height of a USB-A connector is going to be about four millimeters, but all of the repair ends that you have, you really only get about two millimeters to work with. Right.

**Mike Grover Mg:** So that also explains the 0.8, 0.6 millimeter thickness PCB. Exactly. You're really starting to butt up against your, the Z height of your components.

**AT-Tinny's:** Yeah. So that, that does restrict on a lot of stuff. Even some of those really cool antennas that I want to play with that, you know, work above ground planes and stuff.

**Speaker ?:** Uh-huh.

**AT-Tinny's:** Uh-huh. They take a little bit more space than I have without getting really thin on the boards. Right. Right. And so did you, you had mentioned that you have a new type of thing that you're working

**Mike Grover Mg:** on?

**AT-Tinny's:** Yeah.

**AT-Tinny's:** So chasing the cable, using the mill to chase where the cable can go, using wireless chips out there that enable the same type of attack, an HID attack, your keyboard or mouse, anything over USB really. Yeah. And, uh, do the same thing. So the, the change here is that typically HID devices are attacker deployed. So the attacker gets physical access to the machine, or sometimes you can kind of trick somebody into plugging in a USB drive that says something interesting on it, but they're going to, they're going to notice. Right. So if you've implanted inside of a cable, that becomes, uh, in a sense, victim deployed here. So it's, they are keeping it on their machine. They don't know it. Oh, right. And if you have remote triggering or remote, um, code deployment, you can update that on the fly and trigger it on the fly when you want as an attacker. Right. Right. And that's, that has a lot of advantages.

**Mike Grover Mg:** So this would be, uh, I think one of the examples you gave or maybe Joe gave was like, you leave it in a conference room or you send them a free cable replacement that it looks like it's coming from a manufacturer or something like that.

**AT-Tinny's:** Yeah, exactly. Um, honestly, a lot of these cables look identical. So, you know, swapping it out, leaving it somewhere nearby. Yeah. Some of the cables are expensive. Yeah, exactly. Some of those cables are expensive, you know, $20, $30 USB cables. That's going to be something.

**Mike Grover Mg:** Replacing your MacBook charger. Holy shit. Oh my God.

**AT-Tinny's:** I'm probably going to pick that up because it's in my driveway or, you know, wherever maybe.

**Mike Grover Mg:** Right. And that actually is an interesting kind of tie back to a attack that you probably knew about was the one with the, uh, the, what was the thing where they, they jumped the air gap with the, uh, the, uh, the centrifuges, you know?

**AT-Tinny's:** Oh yeah. Uh, Stuxnet. Stuxnet. Yeah. There was a series of things that they did there.

**Mike Grover Mg:** Sure, sure, sure, sure. But yeah, exactly. But like, it might've been like they left a USB drive in a parking lot or a similar kind of thing and someone just plugged it in and started using it. Exactly.

**AT-Tinny's:** And while your computers may be isolated from RF, we will, are your peripherals. Right, right, right, right.

**Mike Grover Mg:** Yeah, exactly. So, yeah. That's pretty crazy.

**Dave Jones:** Hmm.

**Mike Grover Mg:** So, so then what are some of the things that when you have RF going in there then, do you have to be nearby as well? Is there, are you looking at broader like cellular type things or sticking close by and just seeing it?

**AT-Tinny's:** So, um, in this current iteration, it's, uh, 802.11. Uh-huh. So, I guess with the current setup, I'm probably getting about a hundred yards. Uh, not, that's to something like an iPhone or, you know, some, some smartphone antenna. Sure. If I had a laptop or something with a much more robust antenna, I could get a lot more range. Uh-huh. But, um, that's, you know, it's joining a network and the thing with networks is, you know, if you control them anyway, you can extend those. So, yes, if, if I wanted to do a direct connection to this cable with the device I'm using to attack, yeah, you guys, it kind of, you know, within Wi-Fi range. Sure. Um, you can also program things to, you know, go off at certain times or with certain triggers if you want. Uh-huh. And kind of extend it a little bit in a sense. But, I could also have it connect to an access point that's nearby that I control. Sure. Maybe, like, a Wi-Fi device that's basically a cellular connection back to wherever you want. Right. Um, now it's on, on the internet and you can go from halfway around the world, connect to that cable. That's right. Because you've got additional devices in this, this attack surface.

**Mike Grover Mg:** Yeah. That's awesome. That's awesome. So, what about this, uh, so I have to bring up the, uh, the video you put out recently. Yeah. The, uh, so it was a bit, uh, not controversial, but it was, uh, eye, eye, attention grabbing. Yeah. Absolutely. What were you going for with that?

**AT-Tinny's:** You're talking about the soldering one? This is the, the, the spoon. The spoon. Okay. Okay. The thing with the spoons. Just making sure. Um, yeah, um, I, I, I get some things in my head and they sit there for a while and eventually they, they need to come out and, you know, maybe video form. And this, this was one of those. And, you know, kind of bridged a few things together here. A lot of people, when you talk about surface mount components, for whatever reason, they think that must have been done with a soldering iron, which makes it very intimidating because that is hard to do. But a lot of people, if you show them, uh, solder paste methods, wow, that's actually way easier. Much more accessible. Exactly. So that's one, one concept I wanted to build into this. And also just, you know, how scrappy can we get with, with that method? Cause you know, I've seen a lot of stuff, you know, people are using skillets and stuff, but, um, you know, how ridiculous can we get to, because that makes it fun. Right. Right. You know, it's like, Whoa, what is this video? I, I, what am I looking at? So I was very confused at the beginning. Yeah. I already had a bunch of, uh, little tiny searches I was using to play around with a variety of different fluxes to figure out what was best for BGA reflow. Right. Um, looking at those, I'm like, Oh my God, this fits really well with this other idea I had in my head of like using a bent spoon, which is typically only seen as having one purpose or, you know, being very closely tied with one thing. Just heroin. Yeah. Heroin use. Yeah. Yeah. There's that.

**Mike Grover Mg:** So that was the, uh, that was the theme of the video effectively. Yep. So, you know, not saying we're promoting it. It was just meant to be attention. Right. I mean, if you happen to know what that is, it'll, yeah.

**AT-Tinny's:** So there's that layer. Right. Um, but yeah, I was, uh, using, um, a very amber liquid inside of a tiny, I think it was a one mill syringe, one milliliter syringe, uh, a very tiny one, uh, to dispense the flux. But basically the concept here was really, really sloppy solder paste applied to a board. You put the components on, put a bent spoon over a candle. Now, in this case, the bent was to prop up the spoon over the candle. Right, right. I'm not quite hot. But, uh, um, so yeah, that, uh, that allowed reflow and it worked.

**Mike Grover Mg:** Yeah. That's great. It was, I mean, it's just, I think it's, and like you said, I mean, you said that the people kind of looked at that, obviously it was an attention grabbing video, but then it was like, no, no, no. Hardware is actually accessible and you can do these things. And I really liked that. Yeah, exactly.

**AT-Tinny's:** And yeah, hardware is addicting too, right? Of course. Yeah.

**Dave Jones:** Right. How do you, how do you realize your electronics and hardware creation becomes an addiction, right?

**Mike Grover Mg:** Yeah. Exactly. Yeah. So on the, uh, so all this stuff is implant things and I'm not sure if we gave, we didn't tie it back to the actual, uh, the thing that was, I'm looking at Joe's power supply here and he's got the stickers that say, I want to believe. And it's a picture of the super micro implant. Is, is this like a broader concept or is this where a lot of that stuff started? Where, when did implants kind of become a thing in the security community or known in the security community?

**AT-Tinny's:** I'm going to defer to Joe on that one. Cause one area. Yeah. Also the hand go up once. Okay. When I, when I was describing the, uh, inaccuracies of the spoon.

**Mike Grover Mg:** And unfortunately that's right about where our recording cut off. Um, not really sure what happened. I apologize for that, but I did want to make sure that you all have Mike's information. Uh, so the best place to follow him is on Twitter. It's underscore MG underscore. And that's Mike Grover. Once again. You know, we had a really good time talking about all this stuff and doing this while we were kind of working through some of the, the, the things we had to get through like folding paper. I do now realize that folding paper right next to the microphone is a little loud. So I do apologize about that. Hopefully that didn't take you out of the, the listening too much. Following Mike's stuff is, is really great though. And, uh, you can see more of his background and more of the things that he's working on. Really exciting things coming up from him. So I do recommend you check those things out. Also, mg.lol is his personal site. So that's where he posts a lot of the videos that we talked about. We'll have all these links in the show notes. Once again, thanks for listening and we'll catch you next time.

**Speaker ?:** Bye. Bye. administered administered administered administered
