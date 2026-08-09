---
episode: 67
title: BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe
url: https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/
---

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEVBlog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life.

**Dave Jones:** Hey Chris, what's happening in the world of Cleveland?

**Chris Gammell:** Well, right now I have scary children mulling outside my door.

**Dave Jones:** Oh, bloody Halloween.

**Chris Gammell:** It is Halloween and I have been the grumpy old man and I stuffed a bunch of towels inside my doorbell because I didn't want to disassemble it. I wanted to get down here and basically, yeah, they might be out there ringing my doorbell like crazy right now, but I am sitting in the basement without candy.

**Dave Jones:** Why didn't you rig the doorbell to scare the shit out of them in some way? Or spray them with water. Something monster springs out or something and scares the crap out of them.

**Chris Gammell:** That's a good idea, but I didn't have time this year. Maybe next year.

**Dave Jones:** I don't understand this whole Halloween thing. It's so American. It's starting to take off here. There's kids walking around the bloody streets last night. Pay in the ass.

**Chris Gammell:** That'll happen, yeah. That'll happen. Unbelievable. Personally, I love the holiday. It's really not a holiday. It's kind of silly to call it a holiday. I love it because I love the creativity people have in costumes. Oh yeah, that's pretty cool. Especially when people start working in electronics. I knew a guy last year who made himself into a working Game Boy. He took an old laptop.

**Dave Jones:** Yeah, that's cool.

**Chris Gammell:** He took the screen and people could actually play Tetris on him while he was standing there. Yeah, it was really cool. So that's a lot of fun. But on the other hand, yeah, it's kind of silly and the candy doesn't help.

**Dave Jones:** On Halloween, you don't actually have to dress up in some ghoulish, scary thing, right? Is it more common that people are dressing up as a Ghostbuster or something?

**Chris Gammell:** Yeah, I think a lot of it's clever stuff these days. It's not always scary stuff. I personally, I've mentioned it on here before, I'm a super wimp. So scary stuff, that doesn't do it for me. So I really don't like it. Yeah. Pussy. Yes. But the creativity side of it, that's great. I think there's some fun costumes out there.

**Dave Jones:** Right. So what happened? They come to the door and they go, knock on the door, trick or treat. Trick or treat. Yeah. What happens if you go, well, trick, bastard, come on. I've had that happen before. Yeah.

**Chris Gammell:** Yeah. Some guy ended up doing a magic trick, I think. We were all pissed he didn't give us candy. Yeah. We went on our way. It's like, oh, I guess. Oh, okay. Right. Because we shouldn't ask for trick next time, huh? Yeah, right. That's the idea. Yeah. Oh, boy. Yeah. Hey, watch this, kids. I'm going to solder a BGA package to a circuit board by hand. Bet you've never seen that trick before.

**Dave Jones:** That'd be brilliant.

**Chris Gammell:** The kids start booing. They're like. Now, come inside, kiddies. We're going to teach you electronics. Yeah. Actually, I saw that, too. So, there's a hackerspace mailing list in Cleveland. The hackerspace is kind of rebuilding around here because of some stuff that's going on. But one of the people on the list, she was asking about it, and she asked where she could find cheap circuit boards. She had this wonderful idea that instead of handing out candy, because she didn't agree with that, you know, because of child obesity problems, whatever. She was going to hand out electronics kits to kids that were of, you know, appropriate age. You know, you're not going to give it to a toddler, but, you know, like six, seven, eight-year-olds, why not give them a simple LED kit? And then if you've got kids that are a little older, I mean, hey, why not?

**Dave Jones:** Well, I can only see one problem with that is they almost certainly don't have a soldering iron, so.

**Chris Gammell:** Yeah, you know, we were talking about that, and I was saying that the thing I would probably do is, you know, try and, like, laser cut out, like, some cardboards. Really, you just need a way of forming it all together, right? Because you can have kids twisting leads.

**Dave Jones:** Yes, you can twist. Yeah, you can stick components through cardboard, and you can twist wires on the back, and, you know, you don't actually need solder.

**Chris Gammell:** Yeah, like scotch tape around, you know, a CR, what is it, 3022? Is that right? The type of coin cell battery? Oh, right, yep. Is that what that is? I forget what the number is, but. It's a Henny 32. 2032. Oh, 2032. Okay. Yep. Got those mixed around.

**Dave Jones:** If you don't know, that's the diameter. Like, you know, the diameter is 20 millimeters, and the thickness is 3.2 millimeters.

**Chris Gammell:** Huh, interesting.

**Dave Jones:** Yeah. So, if you get a 20, you know, so that's where you can get all these different sizes. You know, you can get a CR2550 or something like that. That means it's 25 millimeters diameter by 5 millimeters thick, and et cetera. So, yeah.

**Chris Gammell:** Well, I learned something on Halloween today.

**Dave Jones:** There you go.

**Chris Gammell:** And even if you just gave the kids, like, throwies, you know, and you just take a 2032 and you just tape an LED around it. Like, that's cool for a kid, you know? They don't necessarily need... It's not necessarily about, like, teaching electronics so much as showing kids that electronics can be really cool. And that's... I think that's a good way to do it. And if you don't mind spending more money than you might be spending on candy. Oh, of course. Yeah, yeah. Although candy's not cheap these days either. I mean, people spend, like, 20 bucks to 60 bucks on candy these days for certain neighborhoods. So, yeah. It's... Why not? Why not try something? Yeah, that's right.

**Dave Jones:** Yeah, you don't need a soldering iron because you can just throw in, like, a little tiny breadboard or something. They're cheap. If you bought them in bulk from eBay or something, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** How much would they cost? They'd only cost a couple of bucks each, I'm sure.

**Chris Gammell:** Or if you got, like, a big perf board and you cut it out, right? I mean, like... Yeah, I think it's a really cool idea.

**Dave Jones:** But then you've got to have instructions to go along with it. So, you'd have to print out, like, a, you know, here's how to build it, kids.

**Chris Gammell:** Yeah. Yeah. It would not be without effort. That's for sure.

**Dave Jones:** Yep.

**Chris Gammell:** But I love the idea. I thought it was such a great idea. So... Yeah, it's great. Much better than candy.

**Dave Jones:** If any of you out there have done it or have heard of it, let us know. That'd be awesome.

**Chris Gammell:** That'd be good for costumes, too. I mean, you see a lot of, like, LEDs on costumes these days, too. Oh, yeah, of course. Yeah. Yeah. Well, speaking of BGA soldering, Dave, have you... Did you see the news today? I've seen the bone. We've been boned. The bone. They have released the bone on the world, yes. The Beagle Board Bone. Or the Beagle Bone, maybe? Are they calling it Beagle... Yeah, Beagle Bone. Sorry. Right. Beagle Bone. Beagle Bone. Okay.

**Dave Jones:** So, they're shortened. It's not Beagle Board anymore. It's just Beagle Bone. Beagle Bone, yes.

**Chris Gammell:** And so, back in episode whatever it was, we had Jeff and Jason on here. And Jason was telling us all about the plans for the Beagle Board Bone. Or the Beagle Bone, rather. Ugh. And it is released. It is released today. So, they finally...

**Dave Jones:** But it's not bone-shaped, unfortunately.

**Chris Gammell:** No, it's bone-colored, so... Yep. And it's interesting that it kind of coincides with, like, the skeleton of Halloween. Ooh. No? No, sorry. Didn't like that. No. Okay. Not at all. Yeah. So, it's great, though. It's great. I didn't really remember what Jason had told us about it, but...

**Dave Jones:** Neither do I. Yeah. It's got a real high-powered, you know, ARM processor on it. And... Is it ARM or is it the OMAP? Sorry. I...

**Chris Gammell:** I believe it is ARM because it's the... Yeah. And even OMAP has an ARM inside it. Oh, of course it does, yes. Yeah. Yeah. So, OMAP has, like, the... It's, like, a module-based thing in there. Yeah. It has multiple processors and stuff. But, yeah, I actually... I talked to Jason today online, and he mentioned the reason they had to wait until today is this chip, the chip they're using on it, was just announced today. So, this is a brand-new chip. And so, that's a good sign because that means you're probably getting leading-edge kind of stuff. And probably one of the...

**Dave Jones:** And what's different about this chip? What's new about it?

**Chris Gammell:** Oh, I don't see a link on your... Putting you on the spot. Yeah. Yeah. I'm going to...

**Dave Jones:** Anyway, one exciting thing they've done is they've... And they're deliberately advertising is that they're no longer using those little half-a-beezdick-sized pin-pitch BGA devices. Half-a-beezdick being 0.4 millimetres. They're using... Yeah. They've gone from 0.4 millimetre pin-pitch balls on their BGA devices. They're using a 0.8 millimetre pin-pitch so that, you know... Because the whole idea of this thing is that it's open-source and you can make it yourself, right? You can customise it. You can build your own custom board. And, well, you know, if you have to use a 0.4 millimetre pin-pitch device, you're screwed, right? Yeah. You know, it's not easy. Your boards are more expensive to manufacture because the tolerances are all tighter on the solder mass and the... Right. And the etching and all that sort of stuff. Ah, yeah. It's just a pain in the ass. But they've jumped to 0.8 millimetre pin-pitch. I presume on all the devices, all the BGA devices, because I can see at least one, two, three, four, five BGA devices on there. So, maybe not. Oh, no, they're... No, some of those are land-grade stuff, yeah. Yeah, they're a big deal.

**Chris Gammell:** Yeah, there's FTDI chip.

**Dave Jones:** Leadless chip carrier, one of those. Yeah, yeah. Okay. But still...

**Chris Gammell:** Yeah, it seems like the Sitara. It's a Sitara-based chip, I believe, so... Sitara? Yeah, it's one of their families. What's that? It's like a TI family. It's like a mid-range family, I think. And they're not bad. Honestly, I don't know much about them yet. But, you know, the stuff they're promising with it, I mean, the stuff that Jason told me about was interesting was the fact that they're actually pushing this more as a... What do you say? Angstrom's... He said, Angstrom has been more of a focus than it was in the past, and we're actually trying to produce a software experience, something they avoided in the past. So, before it was more about, you know, hardware hacking and, you know, getting really down in there. Now they're kind of trying to abstract it out and use this as a building block, which you can see because they have a lot of headers similar to, like, an Arduino or, you know, for creating breakout boards, which is cool.

**Dave Jones:** Are those headers compatible with the old version? I'm not that familiar with the old version.

**Chris Gammell:** I don't know.

**Dave Jones:** I presume they're compatible.

**Chris Gammell:** No, they're not. No, they're not. Because the old one didn't have that many I.O., which is a good... I mean, it's a good thing there's more I.O.s now. Oh, okay, right. But if you look at the BeagleBoard XM, I don't believe it had all those I.O. This looks much more like an Arduino Mega type of layout. Absolutely.

**Dave Jones:** Have they got the pin pitch right?

**Chris Gammell:** I'm sure. That'd be pretty big oversight. I think Gerald's pretty good about that stuff. Okay. Yeah, we'll say... I'm excited about it, so... Tell us the price, son. Oh, yeah. 89 bucks. Man, that's a good sign. That's a really good sign.

**Dave Jones:** For the amount of power that you get on there, that is pretty good. Because what was the original BeagleBoard? Over 200 bucks.

**Chris Gammell:** Yeah, original was, like, 250, I think. Yeah.

**Dave Jones:** And then they bought it down to 150 odd.

**Chris Gammell:** Yeah, for the XM.

**Dave Jones:** Yep. Now they've almost halved that again.

**Chris Gammell:** Yep. And, uh... Interesting. I mean, it's getting to the point where I think that, like, TI is probably going to be throwing these things around. You know, they'll just give them away. Um, at least I hope so. I mean... Right.

**Dave Jones:** Well, it's a bit hard at that kind of price. Yeah, but still. I wonder how many they actually manufactured up front to get that sort of pricing.

**Chris Gammell:** Yeah, for the demand and everything. I'm not sure. I mean, they're going through distribution. So, I saw Adafruit's carrying them, and I know DigiKey's going to carry them. So... Okay. Okay. Is everyone going to sell it at the same price? Well, they say that's their suggested, so maybe some people will cut the margin, but it'd be silly if they start.

**Dave Jones:** So, they must have a reasonable margin on that if they're selling them through resellers, because those resellers will typically market up, you know, 40, 50%.

**Speaker ?:** Yeah, 40.

**Chris Gammell:** 40%. Yeah.

**Dave Jones:** You know, something like that. So, maybe they're manufacturing it for under 50 bucks.

**Chris Gammell:** Yeah, they'd be, what, $36 less? So, 90 minus 36 is 54. That's not bad. 54 bucks for that. And it's not like a huge board, and like you said, the layout's easier now that it's, you know, bigger pitch BGA balls. So, that's, yeah, that's great. I don't know. So, when I was talking to Jason, though, he was saying that, you know, it's kind of, because it's so early in development, they're releasing it, but it's going to be kind of rough around the edges. So, if people are interested, I mean, they're going to need help supporting it and bringing it up. And I don't know. It's an open source project. It's a big, big company doing an open source project, and it's still going. And I definitely tip my hat to TI, and even more so Jason and Gerald and the whole BeagleBoard team. I mean, I know people know they're great people, but I just want to say again, it looks awesome. And the fact that they're still doing it is a really good sign.

**Dave Jones:** Yeah, it's fantastic.

**Chris Gammell:** I love it. Kudos.

**Dave Jones:** What's that connector on the end? Is that a USB connector on the bottom end of it? It looks like a big...

**Chris Gammell:** Let's see. That's weird. It looks like Ethernet on the bottom side, and then...

**Dave Jones:** No, Ethernet's on the top.

**Chris Gammell:** Oh, then the bottom, yeah, the bottom is USB. That looks like, yeah.

**Dave Jones:** Like a USB-A or something.

**Chris Gammell:** Yeah, and it says it's able to do USB device. I thought it said. It said somewhere on the page.

**Dave Jones:** Okay, I would expect it to see a USB micro.

**Chris Gammell:** Yeah. It's a USB 5s. Anyway... Sorry, I don't know much more about it. Maybe we can have Jason on in the future and talk more about it.

**Dave Jones:** Yeah, interesting. And it comes with a 2GB card as well. There's a microSD card. That must be... Oh, no. That's the micro... That's probably... Is that the microSD socket? Oh, that?

**Chris Gammell:** On the bottom. Oh, maybe.

**Dave Jones:** I don't know. Anyway, it's got a microSD. Maybe it's on the bottom. Soldered on the bottom. We need more photos of this thing. Yeah, there's a video.

**Chris Gammell:** If you watch the video, you'll see Jason talking. They have tons of techno music playing, and I made fun of him about that earlier. Right. Nice. Lots of fun. Yeah. So, great job. Excellent. Great job, BeagleBoard team. Keep it up. And we'll look forward to hearing more about it.

**Dave Jones:** And it's... Really, it's... You know, it's not for simple stuff. You know, if you're using one of these to flash an LED, you know, it's gross overkill. Right. It's designed for...

**Chris Gammell:** Well, to start up the application, that's fine. But yeah. Yeah. Eventually, I think... Oh, yeah.

**Dave Jones:** No, to start up and learn about it. But if you're using it as a doorbell controller or something, then, you know, come on.

**Chris Gammell:** Yeah, they were talking... In the video, they mentioned 3D printing, right? So, like, a MakerBot or an Ultimaker, one of those.

**Dave Jones:** Something that has a large amount of processing that needs to happen. You know? Right. Right. Large amounts of real-time processing and stuff like that.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Because this thing probably runs at, what, a gig? 500 megahertz or something?

**Chris Gammell:** I don't know. A gig? I don't know. Keep asking me all these questions, Dave. It looks like a gig based on... Oh, that's the BeagleBoard XM video they posted in there. But yeah. More details to come, guys. There's a lot of stuff printed up on the internet, too. So, if there's any other information out there, we'll try and link it in. Yeah. And Dave, stop asking questions, man. My turn. Sorry, dude. I get to ask you a question.

**Dave Jones:** Yeah, go for it.

**Chris Gammell:** Do you have a home yet? Do you have a home? I do have a home. Well, kind of. Kind of. I've paid a deposit. Hey, hey. The Nerd Cave is in the works.

**Dave Jones:** It is. It is. And I shot some video yesterday. Oh, you did? Great. All the lights were out, yeah. But I had my headlamp on. But I've got my headlamp. So, I'm shooting this video with my headlamp on.

**Chris Gammell:** Your true cave exploring experience came into play there. Yeah.

**Dave Jones:** So, I'll probably upload that today. Oh, boy. That's great, man. Actually, I'm in two minds with that. I need. You know. Because I do these silly. You know. Like, I uploaded a video yesterday of some firmware. Like a firmware. High goal scope hack. Right? Yeah. It was only like a minute long. It was my shortest video ever. You know. And I didn't bother numbering that. You know how I number each episode?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Which is something I started with. You know. Now, I'm up to 120 something. Oh, 212 you're on. Sorry. 212. Yeah. And I'm always in two minds. Do I number these little short little clips that I upload? Should I bother numbering those as episodes in quote marks? You know. Because it's not really an episode. Because I didn't edit the thing. It's just like I. It didn't even go through my editing software. It doesn't have the usual outro or intro or something like that. It's just a random little video which I'm uploading. So, I'm. I don't know. People out there. I don't watch your videos. Should I be numbering those? I don't know.

**Chris Gammell:** Yeah, I know. You don't watch my blog.

**Dave Jones:** And I don't read your blog. And yeah.

**Chris Gammell:** There we go.

**Dave Jones:** Yeah. But yeah. I don't know. I just feel as though I didn't put any effort into it. I just hit record and spoke for five minutes. And I press stop. And I upload it straight to YouTube. Does that warrant an episode number? Or do I have to actually put some work into editing the damn thing before it warrants a number? I don't know. Tell me.

**Chris Gammell:** Hmm. I don't know, man.

**Dave Jones:** There's people out there that say they like the numbering thing so that they can keep track of, you know, they can actually, oh, it's number 52, you know.

**Chris Gammell:** Right. I haven't seen that one. I saw 51, right? Point to, yeah. Yeah. Yeah.

**Dave Jones:** So, I don't know.

**Chris Gammell:** Anyway. Speaking of things people complain about, how about one of our favorite complaint items? Eagle. Eagle's coming out with a new promo. They got a new promo out for their Eagle 6.

**Dave Jones:** They do. Yeah. But it's not actually out yet.

**Chris Gammell:** No. It's just a promo right now.

**Dave Jones:** Can you even, I don't even think you can down, maybe there's some beta testers. I don't know. If you're a beta tester, let us know. If you're not under NDA, or even if you are, eh, who cares? Oh, yeah. That's great advice there, Dave. Just tell us. Yeah. Yep.

**Chris Gammell:** Yeah. Why not? Yeah. They got a list of things that are new. So, there's some good stuff. And this is, I mean, this is exciting to see what they're going to do with this stuff. They had talked about it previously, the XML database stuff. So, hopefully they-

**Dave Jones:** That is the main change, right? The XML data, they've gone away from the binary format. Apparently, it doesn't support the old format anymore.

**Chris Gammell:** Oh, so this is going to be like a hard stop once you update? Yep.

**Dave Jones:** Once you update, you go to- There's probably a converter available, right? Right. But it's one direction. Obviously, right? If there wasn't, they'd be shooting themselves in the foot, Altium style. Hey. Ka-ching. And, yeah, but that's apparently the big thing, is that they've gone, you know, they've switched over completely to the new XML file format. It's all open so that, you know, which is great. Fantastic.

**Chris Gammell:** Yeah, it should help with, like, diffs and stuff, too. That's what a lot of people were asking for. I think that's the reason a lot of people were asking for it, was for doing, you know, version control and that kind of thing and tracking changes. Right.

**Dave Jones:** And, yeah, I like- And you can do that better if it's text-based. Yeah, yeah. Well, there's ways to do it when it's binary-based, but, yeah.

**Chris Gammell:** Yeah, but not really, because if you think about a diff program, right? And actually, I don't know if it's on the list, but Evil Mad Scientist Labs, they had a great post about visual diffs and how you could do that. Because, you know, a lot of people in the open source hardware community are big about, you know, using GitHub or something similar like that, sort of vision tracking. And that's important in anything, right? How do you really do a diff between a schematic, right?

**Dave Jones:** Well, it needs to be built into the actual program like it is in Altium. Altium have their own built-in diff things, and it highlights, you know, stuff for you, and it handles that sort of thing. But, yeah, but then it's got to be built into the program, and then, you know, people- It's just another feature that they've got to work on.

**Chris Gammell:** If it's not there, it's tough then, right?

**Dave Jones:** Oh, yeah, yeah, of course. Yeah, I guess, yeah, this schematic, this XML thing is a way to do that, right? Because then it can highlight this text difference, and then the text is, I would presume that it's actually readable, right? So it says, you know, 7400, you know, you've added this-

**Chris Gammell:** It's like tags, rather. That's how XML works. Tags, yeah. Yeah, so if you say part, you know, bracket part, and then around 7400, right? Yeah.

**Dave Jones:** So you can see that you've added that part, because then that'll be extra text in that file that wasn't there before.

**Chris Gammell:** Right.

**Dave Jones:** Right, so that's the- Yeah.

**Chris Gammell:** Yeah, and that's the tough thing with binaries, is like if you do the stupidest version of a binary diff, then you'll say, okay, well, this file says 1001. And then you might shift everything by, you know, if you insert a zero somewhere, then everything shifts by one bit, and everything looks wrong at that point. Yeah, yeah, it's wrong. And so that's where binaries really, that does not work well. And that's actually a problem with FPGAs, too, is like if you try and, you know, if you have a bit file that you create from an FPGA design, then that's impossible for- And I've actually asked this on Twitter before, too, because I've had trouble with FPGAs and revision tracking. You know, there's certain files that just don't play nice. Right. And for some reason, it's not like, it's not really integrated into Xilinx or Altera, as far as I can tell. Maybe I'm wrong about that. But I had never seen a built-in tool. It was always, you know, it always had to go external. So I'd be interested if people do know about that. I'm still always looking for good ways for revision control tracking of FPGA stuff, like VHDL or Verilog.

**Dave Jones:** I just like keeping track of it manually. You know, I don't use these revision control tools.

**Chris Gammell:** You know, I used to be like that. And I've had a boss like that, too, where he would just zip up entire files and he'd say, Okay, today's October 31st. This is the file. This is a set of files. And I like that idea because it's a, is the basis of it is storage is cheap. Messing this crap up is really expensive. And I get that, but it gets messy. It gets really messy, I think.

**Dave Jones:** I mean, it depends on the project. You know, if you're just working on your own project and it's not that hugely complicated, nobody else is touching it. You know, you can almost go, why bother? Right. Especially if it's just, you know, a hardware project. You're fully in control of it. It's all in your head as well. You know, you're, you know, you've got this human brain, you know, it can do things.

**Chris Gammell:** A brain. I've heard about this. Yeah. Brains.

**Dave Jones:** Whereas if you've got source code and you've got, you know, a hundred different files going into it and you've got different people where, you know, of course you need.

**Chris Gammell:** Yeah.

**Dave Jones:** Version control tracking.

**Speaker ?:** Yeah.

**Chris Gammell:** And you need like automatic builds, all that other crap, too. Yeah.

**Dave Jones:** But if you've got just a little hardware board you're working on, it's got one schematic. Well, you just keep the latest schematic there. That's it. That's your, you know, you have the latest version and old ones you might, you know, just zip up or keep them there just in case you wanted to go back. Yeah. But generally speaking, you know, you don't want to do that. You want to just build upon what your current version. Your current version is the latest. That's the only one you ever work on. And you build upon that. And, you know, that's easy. Yeah. It's easy to keep track of.

**Chris Gammell:** That's true. And, yeah, it's when it's smaller for sure. I've seen that before, too, with, you know, hardware projects in general. It seems like, you know, we've talked about design by committee and how crappy that can turn out. But sometimes it's a reality where you have to have multiple designers on a project. Oh, of course. Yeah. And that really does get messy. I haven't seen, the best I've seen is people splitting up pages of a schematic, but then even integration of trying to get all that stuff together starts getting messy. Yeah. So I've never really seen, and even on, like, open source hardware projects that we've seen, it seems like it's a much smaller team. Like, the Arduino team isn't big. And, you know, you see a lot of smaller boards. They're just not big teams. And I don't know if it would be possible to have a really, really big type project like that. Because if you've got everybody spaced out and everybody's working on different parts at different times, how do you really integrate that when you have to buy a board at some point? You know, at some point, someone has to say, well, you know, go buy that PCB, right? Yeah, yeah, exactly. Message.

**Dave Jones:** Yeah, I've been there, done that. You know, we've had, like, at companies, we've had multiple people working on libraries and things like that. And we had to use, you know, Tortoise version control and, you know, the Tortoise slash SVN, you know, version control. Oh, yeah, yeah, yeah. Individual library files get checked into that and blah, it's all, you know. Yeah. Yeah. It gets big and complicated.

**Chris Gammell:** Yeah, I'm sure it seems complicated right up until the day when you need to back or, you know, recover all your backups and it works nice. Yeah, yeah, exactly. I'm sure the day when it doesn't work, you're like, oh, crap.

**Speaker ?:** Yep.

**Dave Jones:** Yeah, but I, you know, for my own simple projects, I don't use version control for any, I don't have version control on my machine here. I've got no form of version control. No, I just don't need it for my own personal projects. You know, I've got a project subdirectory and then there's each separate project has a subdirectory and then there's firmware and there's hardware and then there's, you know, the latest files and then there's a backup subdirectory and all that gets backed up and I just work on the latest version.

**Chris Gammell:** And all the software people out there listening, take it easy on Dave. We know that the comment section will be filled with vitriol and don't worry about it. He's just a, he's just a solder junkie. Come on, just take it easy on him. It's cool. It's cool. Yeah. So speaking of Eagle, did you see my, my KiCad tutorial?

**Dave Jones:** Yes, I did.

**Chris Gammell:** Yeah. Self promo. All right.

**Dave Jones:** All right. Hey, you've done a second one. Is that finished?

**Chris Gammell:** I'm in process. Yeah. Right. Okay. It's interesting. It's, it's, it's an interesting tool. I like it. It's, it's not as bad as I thought it would be. I really did. I really was a little worried, but I think if people can do Eagle, if they can do, you know, Altium, I think you'll probably miss some, some features, but more so from Altium than you would from Eagle. But of course. Yeah. Yeah. It's, you know, it's, it's pretty damn free. I'll say that. Right. And someone told me about, someone on Twitter said that you can actually import Eagle libraries, which is the stuff I'm struggling on right now. Yes. Because I'm rebuilding all my libraries. Right. And I don't like that. So.

**Dave Jones:** So you've made the conscious decision to switch to this or you're just trying it out or.

**Chris Gammell:** Yeah. At least on the project I'm working on, I'm going to take it all the way through.

**Dave Jones:** Okay.

**Chris Gammell:** Because you need some kind of driving force behind it. Otherwise I'll just keep sitting there.

**Speaker ?:** Oh yeah.

**Chris Gammell:** Of course.

**Dave Jones:** If you just.

**Chris Gammell:** Not doing it.

**Dave Jones:** Fart ass around with it, you know. Yeah. You don't do anything. You've got to do a real project on it.

**Chris Gammell:** Right. And that, yeah. So I figure hell or high water, either, either I'm not going to get the thing done at all, which is a possibility, or I'll, you know, I'll actually get it done with, with KiCad and see how it all works out. Yep. And we'll see how it goes.

**Dave Jones:** Now there's some rumor with Eagle. I don't know if it's true or not, so don't shoot me down, but that. Water cooler stuff going on right here. There will be no more free version.

**Chris Gammell:** Really?

**Dave Jones:** Yeah. That's a rumor going around, but I don't know if it's true or not. So if there's anyone from Eagle listening, please. Please. It can either confirm or deny that there will be, it'll stay exactly the same as before. That there will be a free version.

**Chris Gammell:** That is the opposite of what we wanted. That's the, uh, the Freeagle campaign, which fizzled, uh, we should, we should mention. Totally fizzled.

**Dave Jones:** No, it's still there. Free Eagle. Oh, Free Eagle. Free Eagles. Free Eagle. Free Eagle. Free Eagle.

**Chris Gammell:** And the CAD soft.

**Dave Jones:** Because it's ridiculous. I've got to say it again.

**Chris Gammell:** Yeah.

**Dave Jones:** If you want to design a single-sided board with two LEDs on it, but it's longer than 160 millimeters, you've got to buy the top-of-the-line package for a thousand plus dollars. Are you shitting me? That is ridiculous.

**Chris Gammell:** Yeah. Yeah. That should change the rules. You know what, though? That's what I said. I said to someone, I said, well, I, if I can't change it, all I can do is use other versions of other things.

**Dave Jones:** Use something else. Vote with your feet. Yeah. Exactly. Yeah.

**Chris Gammell:** So that was the thrust behind me switching over. And I don't know if it's going to work, but I think if more people do switch or they switch away from Eagle, that'll show right there. I think if they stop seeing uptake and projects using Eagle, then yeah, you're going to see other stuff there.

**Dave Jones:** I think just out of principle, I won't promote Eagle. I've thought about it because everyone, right? Because it's what everyone uses in the open source hardware thing, right? Because it had that free version available. So I've got the bootstrap and the kickstart and, you know, it got that foothold in the industry. But yeah, I just, I just don't like their pricing structure. It sucks. So Eagle, I'm not going to support you. Screw you. I'm going to support that.

**Chris Gammell:** I mean, what if tomorrow they open it up and it's free?

**Dave Jones:** Well, then you'll be my best friend. I, you know.

**Chris Gammell:** All right. He is. He is. He can be bought folks with free. No, not bought.

**Dave Jones:** Yeah. By doing the right thing.

**Chris Gammell:** Yeah. Yeah. Yeah. I agree. I think the structure needs to change, but. Yep. They'll figure it out.

**Dave Jones:** Everyone agrees that it's shit. Yet they still persist with it. Yeah. Everyone I seem to talk to about it. Oh yeah. You know, I don't like using Eagle, but it's what everyone uses. And I don't like their pricing structure. And I don't like the limitations and how they've structured them.

**Speaker ?:** And.

**Dave Jones:** Ah.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, not happy. So please. Yeah. If that rumor is. Well, if that rumor is true, then it's crazy. They'll be out of business before you can say key cad.

**Chris Gammell:** I would be interested to see how much they're.

**Dave Jones:** Or dip trace or any of the others.

**Chris Gammell:** Yeah. Jita. Right. What else is out there? Jita.

**Dave Jones:** Yep. Well. Design spark. Yeah. Jita and key cad are the only true open source free ones. I think.

**Chris Gammell:** Okay. Okay.

**Dave Jones:** If there is another one, please let us know.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Yeah. Definitely. Definitely. What about this? With key cad. I want to know. I think I had a look at their website once. Can you actually download just a compiled windows installation? Like. Yes. I. Yeah. You can.

**Chris Gammell:** I have windows. I have it on my windows machine and I have it on my linux machine.

**Dave Jones:** Oh. Okay. Yeah. Because. Oh. I. I looked and they went. Oh. We kind of. We do support windows. But. You know. You go compile it yourself. Or some. Weird shit like that. And I don't want to have to compile the damn thing myself. I just want to. Here's the download of the installation. You know. With the XE. You know. Install. XE. Or.

**Chris Gammell:** Down. Oh. Yeah. They got tons of stuff. So. They got official builds for Linux and Windows. Oh. They do. Okay. It looks like. Snapshots. They've got. So. I think third parties then have unofficial builds for. Specifically. For. Ubuntu. Mac. Right. They've got all these logos. I don't even know what the hell they are. Debian. Right. Fedora. Gentoo. Yeah. A lot of the Linux builds. So. Got it. Is that Red Hat? Free BSD. Man. I. I do not know my logos. They keep changing on me. You know. You think. Yeah. I can't talk. I wouldn't know them either. So. Yeah. I'll put. I'll put a link to it if people are interested. I think it'll be good. If. You know. If there's more. And that's the thing. If there's more libraries. And if there's more people using it. Then there's. Yep. Critical mass. And then. Part vendors start making libraries. And everybody starts making libraries for it. And that's what it really comes down to. Yeah. Is ease of use. Because. Everybody else is using it. So.

**Dave Jones:** That's the thing.

**Chris Gammell:** Yeah. And I. It's kind of like Eclipse. Right. Eclipse is an IDE. The people.

**Dave Jones:** Yes.

**Chris Gammell:** That first poo pooed for. You know. Being an open source. Code development thing. And now. Every vendor. Nearly every vendor. Offers some kind of. Either Eclipse plug in. Or an actual build around Eclipse. And it's just a lot of. Development environments. Are now. Eclipse based. And I might be talking on my butt on that one. I mean. That might be. I don't do something for that often. That might be a slight exaggeration. I don't know. Yeah.

**Dave Jones:** But yeah. I see it more and more often these days.

**Chris Gammell:** Yeah. Yeah. I've seen it for big FPGA vendors. I've seen it for. Yep. Software. So. And I like it. So. Excellent.

**Dave Jones:** Yeah. I think we need that. Foothold. You know. Like people start using a. An open source package. And then. You know. Get that. Once that critical mass is reached. And then that package will be the de facto standard. Yep. And it just hasn't happened yet.

**Chris Gammell:** Yeah. And you see something. Unfortunately it's Eagle.

**Dave Jones:** Which is a commercial package. And. Well. You know. Yep. And it's not that great. Apparently. People keep bitching about it. Yeah. I've lost count on the number of people. Number of people who said. Oh. I use Eagle. But I hate it. But I use it. Because everyone else uses it.

**Chris Gammell:** Yeah. I've used it. Boy. A decent amount. I like. I like it. Once you get used to it. It's okay. It's like any CAD package. Yeah. Yeah. Yeah. Of course. Yeah. Yeah.

**Dave Jones:** All right.

**Chris Gammell:** All right. We've got. Done with.

**Dave Jones:** The update. On the 7400 competition.

**Chris Gammell:** Oh yeah. So. Were you a judge for that? Were you allowed to. I am a judge. You are a judge. Yes. I thought we had that on the list. And I wasn't sure. So.

**Dave Jones:** Yes. I am a judge for that. And yes. We have. We. All the judges. Chose their top 10. Projects. Nice. I think there were 70. 71 entries. That's great. And yeah. And. We chose our top 10. And from there. I haven't. We just got an email this morning. About the rules for judging the next round or something. But yeah. I think that. You know. There's a whole bunch of prizes. So there's more than 10. Prizes. So obviously we've got to divvy those up somehow. But yeah. There's some really hot projects in there. And. Yeah. Yep. But. As we expected. It is. Because there wasn't a narrow focus. Mm-hmm. On the project. It was very open. And then. We got a. Bunch of very open type projects. So. It's hard to compare them. You know.

**Chris Gammell:** Yeah.

**Dave Jones:** How do you compare. You know. Some video game system. With a. You know. Some clever little lead flasher. Right. Or some. You know. Right. Right. It's just. Yeah. It's very hard.

**Chris Gammell:** So it would have been better. If it was like five chips. Instead of. All. 74 series logic.

**Dave Jones:** I. Well. I don't think. You know. I just think it doesn't work. As well. As a contest. As it could have. If it was more narrow. As which contest Dave. Like the triple five. Oh. Like the triple five contest. Or like the one. We've talked about the micro controller contest. Yeah. You limit it to either. Yep. Eight pins. Or you limit it to one K of memory. Or you. Yeah. You know. Somehow. You know. Really strict limitations. I mean. This one just said. You know. You can use. Oh. You don't even have to use 7400. You can use 4000 series. And you can do whatever. You can use a million of them. Or you can use one. Or you could.

**Chris Gammell:** Oh. Yeah. I. Yeah. I still. I'm not willing to run it. But I'm still behind the one K memory. I love that. It was not my idea. I forget whose it was. But like a pick. Or anyone else. You know. One K memory. Kind of micro competition. I think it's brilliant. Because that'll bring focus on.

**Dave Jones:** I've been thinking about recent. That recently. And there might. Be something going on in the background.

**Chris Gammell:** Ooh. There. Yeah. Possibly. So. So. I could be a judge for that. If you run it. And then I could make snarky comments. About how I didn't jump in the fray. All right. I like this. And then I could. Yeah. Shovel out prizes. And videos. And yeah.

**Dave Jones:** But it would have to be limited.

**Chris Gammell:** For sure.

**Dave Jones:** To something like that. It would. Like. I was thinking. Would you limit it to like an 8 pin. Like. Say. Say. An 8 pin. Micro. Oh. So there's. I. I'm more.

**Chris Gammell:** Less peripherals.

**Dave Jones:** Yeah. But I'm more of the opinion. That you'd limit it to code size. So that you could use. Any. Yeah. You could use a huge 32 bit arm. With a thousand pins on it. But you could still. Yeah. You know. You can only. Because I think if you limit it to the 8 pins. Which is something I think we've discussed before. Then. It's. You know. You're limited in the amount of. IOs. So some of those 8 pin chips. Can have lots of. You know. They can have 8. What. 8. 16k of memory in them. Can't they. Some of them are quite. Beefy little. Oh. Yeah. Yeah. Yeah. Yeah. Yeah. Because it's all.

**Chris Gammell:** It's just about the IO versus internal memory. You're saying.

**Dave Jones:** Yeah. Yeah. But limiting. And then you. You know. There's only so much you can do with 8 pins. You know. And then you've got to have. Lots of external circuitry. If you want to divide. And stuff. Yeah. Yeah. Yeah. You want to get something clever. Like you want to drive. You know. A thousand leads with 8 pins. You know. Stuff like that. But I think it'd be cooler to have. You know. Like. Yeah. Like a 1k limitation. Or 2k. Or something like that. So then you could use a thousand pin. Chip if you wanted to. And. You know. You're limited to. You know. So you can drive a thousand leads. But you've still only got 1k of memory to work with. You know. Right. Yeah. Exactly. I think that'd be. That'd be very cool. Yeah.

**Chris Gammell:** So. Well the thing that I always do like about contests. Is that. And this one. This one included. Is that it kind of just brings focus back to it. Because I mean. I think a lot of people that are new to the field. Don't know 7.4 series logic. You know. Just the. Yeah. Of course. And how important it was. And from that perspective. I think. You know. It's brilliant. You know. Like. And even a 1k contest. Or a 5.5.5 contest. It's just about the focus on it. That's what's really important. So. I like that. And. Yep. I also like that Dangerous Prototypes is running this and not me. Yeah. Yeah. Exactly. And.

**Dave Jones:** It's bad enough being a judge. Yeah. Yeah. Let alone running the thing. And. But that's the thing. Like. I would love to see a true cross vendor contest. You know. If it was like an 8 pin or a 1k micro. I'd love to see every major micro controller manufacturer get involved and offering free kits.

**Dave Jones:** You know. So you could choose the vendor. You know. It's not just one big. You know. It's not just microchip. Or Atmel sponsoring it. Or TI. Or something like that. Yeah. You know. Yeah. Exactly. You know. You get. You know. You can use anyone's micro. Or even a soft micro in an FPGA. Right. Even a soft core. Or something like that. Yeah.

**Chris Gammell:** Maybe. Well. That might be kind of. Because then you could put everything in logic around it. Man. That would be sick. If you did 1k. Yeah. Yeah. Yeah. Okay. Yeah. I could make something pretty great if you put an FPGA around it. You know.

**Dave Jones:** Yeah. All right. Yeah. Yeah. Yeah. You'd have to draw the line there. Right.

**Chris Gammell:** Yeah. Oh man. Okay. That'd be fun. Right. Well. Anyways. 7400. 7400. Is that how you say it? 7400. How do you say it? 7400. 7400 contests. Yeah. So how. I mean. Favorite. We should just wait. Is that kind of the idea? We should just wait for you.

**Dave Jones:** I'm not allowed to say who my favorite is.

**Dave Jones:** Okay.

**Chris Gammell:** And what about dates? When is that stuff all getting announced? Any word on that?

**Dave Jones:** Not it now. The judges. I literally got an email this morning. I haven't read it yet. Okay. About the second round judging. So it's in progress, folks.

**Chris Gammell:** All right.

**Dave Jones:** So thank you to everyone who entered. Some of them are just awesome.

**Chris Gammell:** Yeah. Yeah. I've seen them popping up here and there. Lots of fun. I like them all in.

**Dave Jones:** And as usual, quite a few people entered old projects. You know. They had some old project they worked on. And well. You know. That's fine too.

**Chris Gammell:** Yeah. Not a big fan of that.

**Dave Jones:** And as usual, there was a big discrepancy between documentation, you know, and videos and stuff like that. And some people have none at all. You know. Here's a schematic and here's a photo of the thing and that's it. You know. It's like, well. Eh. Okay. If it was clever enough, then, you know, it's going to get marked up there and might have made the top 10. But generally, I don't think so.

**Chris Gammell:** Yeah.

**Dave Jones:** Or people that do video, just add some commentary, folks. You know. I know it's, you know. Like, you don't have to be on camera. But just, you know, talk into a microphone and say, here's my project. You know. Yeah. Yeah. It's a bit more personal and, you know. Even if it is as simple as that. Here's my project and I spent, you know, two weeks on it and I just got it done in time. And look, it flashes these leads and does this. Blah, blah, blah. You know. Very quick and simple, but make sure you add some commentary to your videos. There's nothing more boring than watching a five-minute video with no commentary.

**Chris Gammell:** Right.

**Dave Jones:** So, yeah. Just, you know, leads flash and things like that. No. Just voiceover, folks. Please. Right. It'll help your chances a lot.

**Chris Gammell:** Definitely.

**Dave Jones:** Yeah.

**Chris Gammell:** Speaking of commentary, when you're doing commentary and you're publishing articles even, make sure you proofread before you send things out. IEEE had a bit of a snafu.

**Dave Jones:** Have you screwed something up, Chris?

**Chris Gammell:** No. IEEE did.

**Dave Jones:** Oh. Oh, yes. This is brilliant.

**Chris Gammell:** You were so excited about this.

**Dave Jones:** Oh. This popped up in my email box. Get ready your amp hour bingo sheets, folks.

**Chris Gammell:** Yeah.

**Dave Jones:** Because not only are we going to mention the IEEE, we're going to mention Arduino, and we're also going to mention women in engineering. So, this is great. What it is, is that they sent out an email alert to readers that, you know, if you sign up, you're in this tech alert email thing. And with this article entitled, With the Arduino, Now Even Your Mum Can Program. That was the, you know, big, you know, big email blast to, I don't know how many tens of thousands of subscribers they got. And apparently, well, at least one person complained, I'm guessing. Oh, I'm sure more than one.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. So, they had to, well, the actual title of the article is The Making of the Arduino, where they interview the makers of the Arduino and how it's evolved and all that sort of stuff. Right, yeah. I think it's a good article. Yeah, it was. Yeah. But the, someone complained about the title, which was only in the email. The article was called The Making of the Arduino. So, that was fine. So, whoever sent the, whoever sent and approved the email blast, it was probably getting their ass kicked now. Oh, yeah. Because someone complained and that, you know, it's, hey, sexist, you know. Yeah.

**Chris Gammell:** Yeah. But anyway. And the thing is, I think it's just from a former era, you know. It's like, oh, your mom could even do it, you know. Now, personally, I would have written, your grandparents can even do it, right? You make it.

**Dave Jones:** Yeah, it's not that offensive. You know, I mean, you know, lighten up a tad. Well, the thing is, there are a lot of moms out there. It's a common expression.

**Chris Gammell:** Right.

**Dave Jones:** Yeah, I mean, it's a common expression. Right.

**Chris Gammell:** But there are a lot of moms out there now who are in electronics or whatever else. And it, yeah. Yep. I'm sure that that was not well received. So, I think it was a, yeah, a clash of expressions.

**Dave Jones:** And there's a lot of tradition there in calling, you know, in this case, actually giving the feminine form to it, right? It's almost French, isn't it? They have feminine. You can know about French. Right. Anyway, that's about all I know about the French language. Anyway, and like, and also, you know, the male side of the things, like, you know, mankind. And I say guys like a lot, you know. I'll go, hey, guys. But it's a bunch of girls, right? It's three girls. I'm going, hey, guys. Because it's a generic, you know, I don't mean to imply that you're guys, you know. You know what I mean? But it's just a generic expression. Right. It's just a thing from the past, really. I know. It's not a big deal, I don't think. Anyway, someone bitched. And here's the response. And I'll quote from Susan Hassler, who's the editor-in-chief of IEEE Spectrum, a woman. And here it is. I'm an IEEE member and a mum, and the headline was inexcusable, a lazy, sexist cliche that should never have seen the light of day. Today we are instituting an additional headline review process that will apply to all future tech alerts, so that such insipid and offensive headlines never find their way into your inbox.

**Chris Gammell:** That might be taken over the edge a little bit, but yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** She should have just said, the guy that writes email headlines is a dumbass. The people in charge of the sacking have been sacked.

**Speaker ?:** Right.

**Dave Jones:** Anyway, it was hilarious. I thought it was a ball terror. I almost wet myself when I opened the email. Yeah. It was hilarious.

**Chris Gammell:** Like I said, I would have written that as even your grandparents can do it, but maybe grandparents would have gotten...

**Dave Jones:** And they still would have gotten, you know, someone would have got offended. You're going to offend somebody with anything you do these days. Harden up, people. Please.

**Chris Gammell:** Now, the real question is, personally, my mom is not technical at all. I do think that with an Arduino, my mom could program.

**Dave Jones:** I think so, yeah. I think my mom could do it too.

**Chris Gammell:** I think, you know, a technical, someone whose mother is technical is probably a little less surprising. But yeah, I think my mom could program with Arduino. So it's, yeah, that's pretty cool. Headlines aside. Keep digging, Chris. Oh, yeah. Oh, yeah.

**Dave Jones:** But yeah, come on. Lighten up. It's not a big deal. You know. Anyway. Someone had a bitch about it and she took it as offensive because, you know, well, she's the editor-in-chief and, you know, and she's a woman. And well, yeah. Oh, boy. Anyway, I thought it was hilarious. There you go.

**Chris Gammell:** one other thing about girls in engineering i actually saw this uh there's a white house um obviously u.s they had a obviously right uh not just a white house in some country but they have this really great uh series on their site about like uh women women engineers and scientists basically telling them to break shit like that's like the basis of this video it says start breaking stuff that's that's the name of this entire campaign i love it well so

**Dave Jones:** this is a white house campaign this is a government campaign uh yeah yeah from the office of science and technology policy oh right yeah we've talked about that yeah before haven't we yeah yeah it's

**Chris Gammell:** great so if you should check out the video too i'll link it in there but uh yeah awesome good advice good advice great shit yep exactly what else did we want to talk about we wanted to talk about india too

**Dave Jones:** there is um an indian thing where they've doubled is is this actually they've doubled the amount of engineering schools in the last five years that is that's that's pretty huge right that's a lot of schools yeah basically they're saying it's too too excess well go for it explain oh basically they

**Chris Gammell:** keep seeing all this demand but now they've kind of overbuilt so much that they're gonna have like too much they're gonna have too many seats and too many uh too many spots for potential grads and oversupply of engineering schools and yeah yeah oops yeah let's see in tamil nadu there's a there's 527 engineering colleges and that's just in one area basically wow so yeah that's that's a lot uh so it's crazy it's interesting i mean you wonder about quality too well yeah i mean you know where do all the teachers magically appear from right exactly you know if it's just uh you know a degree printing factory then it's it's all going to come from yep you know it basically it's going to be the same thing in the u.s you could have or anywhere really you could have thousands of schools but it's still going to be the the top talent is going to come from the top schools so and there are some really great schools in india um but it's just it's amazing how many there are at the bottom and how much demand there actually already is for engineering uh so i thought that was impressive

**Dave Jones:** but apparently they gambled wrong and they're not then and they can't fill them right and there's 44 000 seats that have no takers so the supply is higher than the demand oops

**Chris Gammell:** obviously we don't need new engineering colleges the official explain yeah real estate something like

**Dave Jones:** that yeah something like that yeah real estate i always wonder about that like you know they build these new you know uh office parks where i'm buying into you know mine's not that new it's about eight years old or something but you know they're popping up everywhere around here and well where do they magically find all the people to fill them you know are there that many people like me sitting at home running their home business going oh wow it's you know i need to move out and jump into an office

**Chris Gammell:** building i don't think so no it's crazy yeah that's been a big like rabbits what real estate developers

**Dave Jones:** yeah yeah and bloody buildings they're just it's crazy around my place here there's an 18 percent uh vacancy rate um in new office complexes so that's a combination of that they've built so many in such a short amount of time and we've got no public transport out here and you know yeah so yeah sort of a combination of issues so i'm surprised that they can even get 80 full yeah right yeah

**Chris Gammell:** speaking of replicating how about robots did you see this new uh creepy creepy creepy creepy robot speaking of halloween you're freaked out i am so freaked out so there's it is yeah awesome to watch

**Dave Jones:** it is very it is very weird it is very creepy it is like terminator creepy so i i have a friend who

**Chris Gammell:** works there here it's it's at boston dynamics and uh they're the people who did like alpha dog and uh uh what are the other ones uh big dog so they're like a lot of like pack carrying kind of robots meant for carrying large loads whatever and i i don't know if we i think we posted a video recently but now this is just a straight up it's called pet man and it sounded like you watch the video and it's just it's just walking i mean it's just it's it's a full upright you know it's got arms and

**Dave Jones:** legs and it's a full upright walking robot and it's walking on this treadmill and it is so human like

**Chris Gammell:** it's very human like super super creepy uh yeah and it was a little bit but it doesn't have any

**Dave Jones:** hands it's just got like these tubes for arms you know like the the the feet and legs look reasonably realistic you know well you know kind of um but yeah the the arms are just these tubes right he's he's actually got some some form of shoe on yeah like the looks of it and uh they're real shoes there's these cables unfortunately he's not fully autonomous there's these cables

**Chris Gammell:** dangling down from the roof that you know yeah well if you pay that much for a robot i don't think

**Dave Jones:** you'd let it just go free uh either right and also you know and he's doing like push-ups and the robot actually does push-ups and he does you know stretches and yeah i'd love to know what what sort of senses does it have like can it actually you know does it know not to kill people right does it follow the um three laws yeah three laws of robotics yeah oh man it's just i don't know it's it's scary

**Chris Gammell:** like honestly i look at it i'm just like you know you see a lot of popular cultural references terminator

**Dave Jones:** kind of stuff you're just like it looks like um one of those robots they had in the one of the thunderbirds episodes if you're a thunderbirds fan you might know what i'm talking about where they're they've got these automated robots at this nuclear plant are you a fan of thunderbirds chris i'm not no i don't i don't know any thunderbird stuff oh maybe i'll check it out my entire childhood watching thunderbirds i know them all back was that the uh the was that like the puppets they're not puppets were they marionettes super marionettes super marionettes you know actually i know that's an insult that is like calling a star trek fan a trekkie they're a trekkur you know you you insult them

**Chris Gammell:** if you call them a trekkie well the reason i know about thunderbirds then is because of that team america world police there was a the guys that made south park it was the same yeah the same stuff yeah super marionettes oh don't tell them to talk about my puppets that way those are creepy too just in case anyone else was wondering about my position on uh marionettes

**Dave Jones:** those are creepy too uh yep but yeah it just just the look of the robot reminds me of these centuries they had in this nuclear place and they yeah yeah yeah yeah well i know robots that i'm i'm

**Chris Gammell:** a little bit less creeped out about but still kind of creepy is uh there's not there's another article about uh agrobots that and there was a hackaday article about it and there's a robots.net article about it but basically this is kind of the future of farming uh and it's really a great idea i mean if you think about the amount of people you need in order to really produce the amount of food that we'll need on this planet right you need robots eventually now granted those robots might come and kill you and use you as food but yeah i love it yeah uh anyway i don't think it's creepy i think it's cool it is cool i mean like in terms of like uh sensors and motors and everything robots are i think robots and quads quadcopters i think they're like they're they're like this amazing amalgamation of of like everything that everything cool that people want to work on you know control systems um so i mean great field and a lot of growth too and man especially especially like the uh you know from an industrial standpoint too right we've talked about manufacturing on here before the future is not hand assembled you know like the future is robots so learning how to fix robots or design robots or anything like that there's there is a lot of benefit in that maybe less on the fixing because i think they'll just do a lot of replacing but uh

**Dave Jones:** but there's a lot of college courses that now you know combine electronics with the mechanical mechatronics sort of you know aspects yeah yeah hechatronics and they you know and you basically you become a computer slash robot slash electronics slash person you know a slasher yeah you're a slasher right yeah so you can go and compete in battle bots or something like that yeah what's it called i don't know uh anyway it's not battle bots anymore is it oh something else i've never watched any of them so america oh i love them anyway it's great speaking of education there's an article which you put on here a silicon valley new hiring strategy where someone has dared to ask why hire a phd when a self-taught kid is just as good right and then and uh yeah they're talking about software here right there right especially because they're getting so hard so hard to find yeah whereas you know the silicon valley startup companies are they have these notoriously strict standards you know they want to hire the best graduates from stanford and mit and all that sort of stuff you know but yeah yeah but this article is asking you know is it well is it is it a science or is it more of an art you know or a craft that well you know if you're taught formally you may not be as or some well no let's put it the other way somebody who's self-taught could be as good or better than somebody who's formally taught and yeah and that is it well the answer is yes it's certainly true you can be i think so too and there's proof of it too that

**Chris Gammell:** there's another article on here like from the bbc about germany and you know they have this amazing apprenticeship program it's basically like being on a co-op it's like a co-op on crack basically you know or an internship on crack it's it's just basically that and not only that then you have the employers co-developing curriculum so that you're actually learning what people need to know so then instead of being in your programming class and learning java and the employers say no we actually still need you to learn c i'm sorry right right yeah which is a gripe of mine personally but right you know like i don't do tell why is it a gripe why because it because if you start with java you're so high up you know it's such a abstracted high level language that is your beef yeah yeah right yeah i mean right i think a student learning java doesn't really understand memory until they start learning c or something you know assembly or anything like that right until you get into further courses like programming in terms of software and actual like software concepts and object oriented all other crap that's important but you don't understand how stuff actually works right the best embedded programmers out there know how to manipulate memory on a on a bit by bit level basically and if you get some kid who's learning java or god forbid you know lab view is like script kitty yeah i mean like and i have seen courses where uh lab view is the intro programming class don't get me started on that one yeah okay um yeah i mean how are you really going to know this now maybe the argument is you'll never have to right people that go work in a lot of industries you won't have to and it's true right but then what you have to do is you have to start breaking out your curriculum so you have hardware people that are learning c to start with right you can't generalize your classes anymore in a university you have to have intro classes that start in c or in java or whatever else

**Dave Jones:** right and you could argue that it can end there it depends on what your end use is you don't have to learn that high level shit if your job is if your industry is all low level stuff true right and vice versa if you're working in some high level industry you don't you know like if you're working in you know some uh you know if you're one of these um uh people who get sucked in by the finance companies to develop you know these algorithms for yeah we talked about them before these you know get paid a shit buttload of money to work on these algorithms you don't give a toss about low level stuff you're

**Chris Gammell:** maybe a lot of those guys are doing fpgas these days i mean oh yeah true it's getting down to the

**Dave Jones:** hardware level but you know what i'm talking about right there are these high level apps where it just doesn't matter a rat's ass right like and there's whole industries where it doesn't matter a rat's ass right so you know i mean it's they're they're almost two different fields yeah yeah that's

**Chris Gammell:** true that's true well when we start the amp hour school day we will make sure that software people are not allowed no i'm just kidding yeah exactly you get out you get out of here software guy your favorite programming language is soda that's right you wire wrap that board point to point for everything bga is included

**Dave Jones:** flip that bastard on its back stick it down the superglue and bond out you know a thousand wires out of that yeah when using those stinking reflow machines yeah it's for wimps you're gonna hand solder that puppy ah boy oh boy yep i love it ow amp hours up dude is it

**Chris Gammell:** yeah sad just pissed it away we did it's been half of it answering the door my trick-or-treater that was actually a trick me i was playing on my wife by accident

**Dave Jones:** oops oh well all right we have no wonky shonky product this week oh no it's too bad we'll have to find something for next week so if you've got something that's just a complete load of garbage

**Chris Gammell:** send it to us please yeah or if you don't like that if you don't like the shonkies let us know too we we haven't heard otherwise i've seen a lot of people really like them and i've i've loved making

**Dave Jones:** fun of them so oh yeah yeah it's brilliant yeah our our goal is to get sued one day

**Chris Gammell:** yeah hopefully in australia not in the u.s

**Dave Jones:** well all this weird all this shit comes out of the u.s you do realize this i know oh i totally know

**Chris Gammell:** yeah so you're the one getting sued dude i know great thanks dave yeah no worries all right you can find dave on twitter at eevblog find me at chris underscore gamel or alternately in jail once dave gets me convicted uh and uh or leave a comment on the site we always like that too yep chris.gamel

**Dave Jones:** at uh sanquentin.com what's the i don't know what's a generic uh sing sing sing maybe or alcatraz

**Chris Gammell:** alcatraz isn't open anymore but yeah no it's not well it's open to the public oh yeah yeah

**Dave Jones:** do you know there's tunnels under alcatraz i've i've been down in them oh yeah i've just seen the rock right no well yeah it's not quite like the rock but but there are underground yes there is an underground section underneath the cells where they used to put the really bad prisoners they used to lock them down under the under the bottom there and uh yeah i've been down there on a special tour

**Chris Gammell:** how much i'm learning from the foreigner i've never even been

**Dave Jones:** well that's right well before last year you had never even been to the uh good west coast have you

**Chris Gammell:** yeah there's no time who's has time really who has time ah well all right well we're out of time so we'll see you guys next week see ya

**Dave Jones:** and i will continue the show on my own oh boy this was my original intention actually when the amp hour first when i first got the idea for the amp hour which was before the blog actually um which was before my video blog i thought well you know who's going to want to listen to me just rant on by myself you
