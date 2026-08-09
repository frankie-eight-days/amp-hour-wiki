---
episode: 373
title: Pedantic or Andrantic
url: https://theamphour.com/373-pedantic-or-andrantic/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released January 2nd, 2018. Episode 373. Pedantic or Edtrantic?

**Chris Gammell:** Welcome to Embedded. I am Elisio White alongside Christopher White here with Chris Gammell.

**Chris Gammell:** Hi, I'm Chris Gammell from the Amp Hour and we're doing our annual crossover episode. Amp-bedded. Amp-bedded. Amp-bedded. It sounds more like embedded. I mean, you guys really get the better...

**Chris Gammell:** Well, we could call it the Amp-bedded Hour.

**Chris Gammell:** It could be the Amp-Bow. Oh, Amp-Bow. Well, yeah. It doesn't sound nice. Anyways, yeah. Happy New Year. Happy New Year. I think we're at the end of the year. We made it. 2017. That dumpster fire. As we talked about in the Amp Hours last episode, they had dumpster fire every year. So, we made it through.

**Dave Jones:** That's the odd numbered years.

**Chris Gammell:** Yeah, exactly. Exactly. So, what's new out there? Anything on fire or what's going on out in California?

**Dave Jones:** No, we didn't get the fires. The Southern California got the fires. We got a lot of smoke for a while.

**Chris Gammell:** And the wine country got the fires.

**Dave Jones:** Which is impressive since... Oh, yeah. Yeah. Southern California is 300 miles from us, so... Oh, it was specifically that smoke? Yeah. Oh, well. Later. We got the wine country smoke, too, but that's a lot closer.

**Chris Gammell:** It is very cold in Chicago.

**Chris Gammell:** Oh, yeah. Yeah. It is four. That's an F.

**Chris Gammell:** There's not enough digits in that temperature.

**Chris Gammell:** Yeah. Right. So, yeah, I was looking at... I was flying in today and I was like, oh, four and minus 18F. So, I don't know what that translates to C, but it's starting to converge. You know, when it starts to converge and when F and C start to converge, then that's a bunch of F and C, you know?

**Chris Gammell:** Yeah. That's when you start looking at California and going, hmm.

**Chris Gammell:** Yeah. Yeah. Maybe I do want to pay that much for real estate out there, huh?

**Dave Jones:** Hey, it got down to 32 last week for a few minutes.

**Chris Gammell:** Oh, oh. Wow. Okay. Yeah. Probably had a water main break or something. Nah.

**Chris Gammell:** All right. So, in the last year... Enough of that. Enough of that. Somebody listens to the show.

**Chris Gammell:** Yeah.

**Chris Gammell:** Chris, you left Supply Frame and went to Hologram.

**Chris Gammell:** Oh, yeah. We have to, like, update our respective listeners if there's no... if they don't cross over, huh? Yeah. Like a true crossover. Right. Yeah. So, I left Supply Frame, who also knows Hackaday and Fine Chips and a bunch of smaller tindy stuff like that. And I was doing product stuff there, and now I'm at Hologram, and I am a developer advocate. Are you both developers? I'd like to advocate for you.

**Chris Gammell:** Is this, like, evangelist?

**Chris Gammell:** Yes. That's another terrible term for it.

**Chris Gammell:** Another form of that title. Okay.

**Chris Gammell:** Yeah. You know, I've been thinking about it. It's like an app engineer, but, like, without needing to necessarily... It's just the enthusiasm, not the actual applications. So... You just exude positive feelings. That's right. Right. I'm all positive all the time.

**Chris Gammell:** What does Hologram do?

**Chris Gammell:** We do connectivity for cellular. So, yeah, devices that need to connect to cellular towers without a cell phone present. So... Telemetry. IoT. Yes, telemetry as well. That's a better term.

**Chris Gammell:** Weren't these cell modems at one point?

**Chris Gammell:** Yeah, that's what... I mean, that's what I'm putting on boards these days. So, like, little U-blocks modems and sequins and... Oh, what else is out there? There's... I guess that's an integrated board is the Pycom. Yeah. So, there's, like, I'm learning a whole bunch of new stuff and wireless stuff and everything. So, yeah, it's been going good.

**Chris Gammell:** And Hologram does the whole thing. I mean, it's... I mean, when you have a cell modem, if I were to go out and just buy a cell modem, I would have to then get a contract and then it would have to go to a server and I'd have to deal with the cell modem to server translation and then the server infrastructure. And Hologram does all of that part, right?

**Chris Gammell:** Yeah, yeah. There's three pieces. So, there's hardware, there's connectivity, and then there's software services, right? And those... It's basically one, two, or three. You could pick any... You don't have to use all... You know, you can use whatever you'd want because, like, people don't want to necessarily use our servers, right? So, they want to bounce it over to AWS IoT. Or they don't want to use our hardware. And that's fine. You could just stick in one of our SIM cards into someone else's hardware and then you use our connectivity. So, it's kind of like you can... Or you could just use our hardware and use someone else's connectivity, but that's kind of weird. So, yeah, there's lots of choices there. And it's kind of just offering all three pieces because... Have either of you done cellular projects before?

**Chris Gammell:** Yes.

**Chris Gammell:** Yeah. It's pretty painful, right? Oh, yeah. Probably ShotSpotter, right?

**Chris Gammell:** Yes.

**Chris Gammell:** Yeah. Yeah. So, you know that pain.

**Chris Gammell:** Well, when we did it, we got the hardware. We worked with the cell modem companies. We dealt with the servers. We did all of it. And it was hard. It was not... You needed a team to understand both the operations side and the software side. Yeah. And now, that team is being outsourced. And I'm not sorry because as solo providers, it was hard to get the cell modems to work all the time. But as a group, having different boards, I mean, I can just see how Hologram and like the Particle.io sorts of things make so much more sense than having to go at all by yourself.

**Chris Gammell:** Yeah. Yeah. There's lots of... I mean, there's lots of really... I mean, Particle's great for hardware. Like I said, Pycom's another one that's great for hardware. You know, and like, yeah, there's tons of... There's tons more providers. I just got a board sent to me from a Tindy seller who's doing stuff that I had never seen before. Like, so, yeah, just like lots of people trying stuff. And, you know, and the really crazy thing is it's not... So, I posted a bunch of links in the subreddit. I'm looking at Laura's stuff as well, LauraWan. And like, I'm excited about tying that stuff into cellular, tying that into Wi-Fi. And like, there's a bunch of YouTubers that are doing that stuff now. It's just kind of RF everywhere.

**Dave Jones:** Aren't we going to run out of spectrum space for all these little devices that are hogging all the limited bandwidth for cellular?

**Chris Gammell:** I mean, well, 2.4 ain't exactly, you know, the wide open Wild West anymore. It's pretty crowded in there. So, yeah, it's... What would I see? There was an article about that a while back. It was like, there's... They're starting to use new white space. So, I think it was 800 gigahertz region. Because that opened up when the TV stuff went away. Maybe it was lower than... I don't remember what the actual... It's somewhere around there. It's below a gigahertz. Yeah, it was. And so, that's kind of open now. And then... So, like, Laura can do 433, 890 through the 880. 886 or something like that. And then 900. So, that's all in there too. And so, there's still like the different bands. But, you know, it's just about how much you're actually using. You're not going to be doing like streaming video.

**Dave Jones:** No. Well, I mean, what's the point?

**Chris Gammell:** Right. Right. Right. How do I let my delivery guy into my house? Exactly. You don't know what he looks like. Yeah. Right. But... Well, so, okay. So, I've obviously explained myself too much. Please explain yourselves to my listeners. Who are you, Alicia and Chris?

**Chris Gammell:** I am logical elegance. And I used to have a partner with my small consulting contracting...

**Dave Jones:** Still do. You just don't pay me.

**Chris Gammell:** Well, I mean, you went and got a full-time job. No, it got me.

**Chris Gammell:** Legally, too. I mean, yeah. You guys are still partners, I think, right?

**Chris Gammell:** Yeah. Yeah. Yeah. So, I'm an embedded software consultant or contractor. And yes, those are different. With contracting, I usually help small companies implement their napkin sketches so that they have prototypes and then they can go off and either try them or get VC funding. And with consulting, usually I help small to medium companies who don't necessarily have another embedded software resource. And they can call me and either chat about their mystery bugs or I can mentor their engineers. That's really fun. So, yeah, that's what I spend most of my days doing. Contracting, writing software, writing stuff.

**Dave Jones:** Stuff.

**Chris Gammell:** Well, sometimes I write documents and sometimes I write encouraging little notes that say, globals are a good thing sometimes. You can do it. But let's try not to have quite this many globals. Yeah. And Chris, you took a full-time job.

**Dave Jones:** I did. Oh, I guess I should have showed up for that. This is like the college test. I was supposed to start this year?

**Speaker ?:** Yeah.

**Chris Gammell:** Not only did it start this year, you shipped something.

**Dave Jones:** Yes. I went from consultant doing similar things that Alicia was doing to full-time firmware engineer at Fitbit. So, if you don't know what Fitbit is, get your head out of the sand. Fitness trackers and smart watches and fitness watches and smart trackers.

**Speaker ?:** Yeah.

**Chris Gammell:** It's great. Yeah. Lots of tiny embedded things, I'm sure.

**Dave Jones:** Yeah. Consumer embedded is fun. Consumer is a different world if you haven't done it before.

**Chris Gammell:** We had, well, some of your former guests as well, Evarro and Jen, who are the reverse engineering podcast, came on and they talked about a lot of that stuff. So, that was insightful. That was good. I mean, and I had said, I thought about it after the fact. I was like, oh, I haven't really talked to many, you know, people who have done consumer stuff. And of course, I talked to both of you and just totally gapped on it, you know. So, yeah.

**Chris Gammell:** I mean, I did toys for LeapFrog and that was even more consumery than Fitbit was because their profit margin was tiny.

**Chris Gammell:** Yeah.

**Chris Gammell:** And a penny really made a difference.

**Chris Gammell:** I think about that. So, I have young nephews now and, you know, they just have like so many blinking loud things. And I can't imagine like having to test that stuff all day long. I can't imagine like having to like repetitively hear, you know, what is it called? The dogs. What are the dogs these days? Pup Patrol? I don't know. Yeah. I'm like learning all these new brands as well. They're terrible. It's all terrible.

**Dave Jones:** So, at least you were doing educational stuff. Educational.

**Chris Gammell:** So, they weren't terrible.

**Dave Jones:** They didn't make any noise.

**Chris Gammell:** They were still chip tuning, right? It's like you can only take so much 8-bit where you're like, yeah. I had, well, speaking of gifts, I bought my parents an Echo and an Echo Dot. Yeah. And I think I'm more in love with it than they are. Yeah. The story repeated over and over throughout the country.

**Dave Jones:** Yeah. We bought one for my parents last year. I'm not sure. I've never heard about it again. So, I'm not sure it actually got put in here. Yeah.

**Chris Gammell:** But even though I didn't want something listening all the time, I have to admit, I do like our Echo. It plays music when I want it to play music and it tells me jokes and it occasionally will tell me facts.

**Chris Gammell:** Yep. And sometimes it'll order, Alexa, order a dollhouse. No? I actually used a toy or something. Anyone listening? A dollhouse? Yeah. What? That was the one where, that was the story where a bunch of people actually had it order a dollhouse when they were on a podcast or a new show or something. So, yeah.

**Chris Gammell:** You got a neat gift this year, Christopher.

**Dave Jones:** I got many neat gifts.

**Chris Gammell:** Well, I was thinking the gift I got you.

**Dave Jones:** Yes. The best gift. Come on, Chris. So, what'd you get? Well, if you've been listening to our show, which, why wouldn't you? Of course. Embedded.fm.

**Chris Gammell:** You can go there right now and subscribe.

**Dave Jones:** I've been messing around with analog synthesizers and she got me. Oh, yeah. She got me this semi-kit, although it's mostly assembled from Moog or Moog or however you pronounce it. M-double-O-G.

**Chris Gammell:** If it's got two O's, it's going to be oo.

**Dave Jones:** Yeah, except it's not. Moo. No, it's actually, yeah. It's Moog. Yeah. It's a very small analog synth, one oscillator, but it's got their usual filters and stuff, but it's for tinkering. So, it comes with a PCB and a case and you have to put it all together. But the PCB has a bunch of test points on it and the silkscreen on the PCB is like a block diagram. So, each section of the synth, whether it's the oscillator or the filter or the envelope generator, all that stuff is silkscreen and marked. So, all the components for each block are ganged together. So, you can kind of tell how, just looking at it, how it works. And then it's got all these signals brought out. So, you can experiment with it. It's even got, it had like a piece of perf board. A little perf board area. As part of the PCB. Oh, nice. Yeah, like a prototyping area. And I guess they produced this for like a conference for engineers a number of years ago and everybody freaked out and said, you got to sell this. So, they started selling it. So, I've been playing with that and playing it in my other synths and making some very strange noises. It's been pretty fun. It's great. Yeah, yeah, yeah.

**Chris Gammell:** And is that like one where you actually have a keyboard that controls that or what actually does that?

**Dave Jones:** It's got some buttons that do a full octave on the front. And then it has, since it has all the control voltage inputs, you can hook it into control voltage equipment. So, there's a lot of keyboard controllers that output both MIDI and control voltage. So, you can control it with a keyboard. It takes some work and you have to calibrate it. But it doesn't work.

**Chris Gammell:** Nice. How many different synths did you get for these holidays? Was it four or was there one I missed?

**Dave Jones:** It was four. It was four.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. Because I got three. My parents got me two of the little teenage engineering pocket couches. Oh, those are so fun. Yeah. And you got me one. So, I have way too many synths.

**Chris Gammell:** I saw John Park showed a picture of this box he made. He's at Adafruit doing project stuff. He had a box he made to take on an airplane to compose stuff, to compose chip tunes on the airplane. I thought that was awesome. Also, it would be super freaky.

**Dave Jones:** What are you doing?

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. They look a little weird. They kind of look like old calculators.

**Chris Gammell:** Yeah.

**Dave Jones:** That's great. Where do we hear your music? That music? Nowhere yet. Yeah.

**Chris Gammell:** But there is a place. Okay. You did start a new music thing.

**Dave Jones:** Yes. My brother and I have been working on it slowly. We released one single. Nice. If you care, you can go to 12ax7.fm. 12ax7. Like the tube. Yeah. That's the band name. Nice. All right.

**Chris Gammell:** You'll get people just for that, you know?

**Dave Jones:** Yeah. It's instrumental guitar rock and that tune is sort of mainstreamy and the other two we're currently working on are getting weirder.

**Chris Gammell:** Nice.

**Dave Jones:** Yes. Maybe another month or two before we release those.

**Chris Gammell:** So I was listening and you were talking about this kit on your show at one point too. Which episode was that? The latest one?

**Chris Gammell:** Probably not.

**Chris Gammell:** Which kit? Oh? You were talking. Oh wait. Maybe you were talking about it somewhere else? I don't know. I had a different kit. I heard you. Yeah. Well, I heard you talking about a synth at some point.

**Chris Gammell:** Yeah. I want to refer people to that.

**Dave Jones:** That one is a little noisemaker synth and that was a full electronic kit you had to solder and do the full deal. That was the Bastl Castle, I think.

**Chris Gammell:** Was that? Yeah. Oh, okay. Yeah. It was back to show 223 of yours. Okay. So, Alicia, what'd you get?

**Chris Gammell:** Oh, I got a fantastic picture of a narwhal roasting a marshmallow on its horn.

**Chris Gammell:** Okay.

**Chris Gammell:** That was why I got it too is because we looked at it and we both started cracking up like right away. And every time I look at it, it's hilarious.

**Chris Gammell:** Is this like a full like living room print or? It's...

**Chris Gammell:** It's a hand-done collage of different papers. Oh, nice. So, it's an original but it's not like a super expensive, super large original.

**Dave Jones:** It's, you know, 8 feet by 10 feet.

**Chris Gammell:** No, it's like 24 inches by about 10 inches.

**Chris Gammell:** Okay.

**Chris Gammell:** And then my company, which you might say is just me because people have abandoned me.

**Chris Gammell:** I was going to say the IRS would say what? Yeah.

**Chris Gammell:** I got a Jtrace Pro, which is a super fancy... What's that? So, you know, there are programmers like for Arduino where it just programs it and then you have to use printf or something to debug the chip. And then there are more proper debuggers like Jlinks or Stlinks or even the Blackmagic probes where you can download code, you can flash the code, and you can also use GDB or some other debugger in order to look inside and see what's going on. And the Jtrace, and there are a few other things like this, but the Jtrace not only does the flashing and the debugging, it stores a lot of extra information so that you can backtrace to where you were, you can backtrace everything. So, instead of saying, show me the current variable X, you can say, show me what X was 10 cycles ago or 1,000 cycles ago or 20,000 cycles ago.

**Chris Gammell:** And how much memory is there? Is it like a ton?

**Chris Gammell:** It is just an absolute ton. I mean, it's insane. And the idea is that you can, you know everything about what's happening and you don't have to fiddle. Usually when you're debugging, you have to find, you have to break in just the right spot and you have to maybe change a few things so that you go down this path. The idea with this is you just let it run and then you sort it out and it's all done.

**Dave Jones:** Well, I mean, it does a lot of other things too, right? You can use it for profiling so it'll tell you where you spend all your time. And it's instruction accurate so you can really tell where things are.

**Chris Gammell:** And it's got some onboard current monitoring.

**Dave Jones:** Oh, I didn't know about that.

**Chris Gammell:** I think so. I don't know how to use it.

**Dave Jones:** Connected to what?

**Chris Gammell:** Well, I mean, this is one of those things that if you had a 20 pin connector, it would be really nice. You'd get all this information. But even with a five pin JTAG style connector or even a two or three pin SWD style, you still get some of this.

**Dave Jones:** Yeah. So for most trace, like the double E has to bring it out for you.

**Chris Gammell:** Yeah.

**Dave Jones:** And it's only on the ARM Cortex processors.

**Chris Gammell:** Yeah. The one I got was only for Cortex, which I spent a long time trying to decide whether I was okay doing Cortex-M or if I thought we were going to be doing a lot more A's and R's this year.

**Chris Gammell:** And the A's and the R's are like the more Linux-y style? Is that right? Or?

**Chris Gammell:** R's have redundancy in them. So it's multiple processors in one chip. And they're good for automotive and medical and space, the areas that you really don't want it to screw up.

**Dave Jones:** But the R's are still A-series.

**Chris Gammell:** Right. And then the A-series run Linux usually.

**Dave Jones:** They're big, big, full mobile phone chips.

**Chris Gammell:** Not the M's, which are kind of small and very, very cool and very cheap, but kind of small.

**Chris Gammell:** Right. Yeah. Yeah. Resource constrained, right? Yeah.

**Dave Jones:** Well, they don't have memory protection. Well, they sort of, they have some memory protection, but it's not enough to run a Linux-style operating system.

**Chris Gammell:** I mean, you couldn't run much else besides a tiny stripped-down Linux. What about you, Chris? What did you get for Christmas? Or gift-y or whatever.

**Chris Gammell:** Yeah. Yeah. Yeah. Boring stuff from, you know, just like warm clothes for me. But I had bought myself a HackRF. So, I finally jumped into that. What is it? That's Mike Osman and Great Scott Gadgets. It is their SDR. So, it is basically a troubleshooting tool using GNU radio. And so, as often listeners of the Amp Hour would know, Mike Osman's been on our show a whole ton. And so, he's always talking about that stuff. But basically, it allows you to do SDR in a graphical, or sorry, you can do RF stuff in a graphical manner. So, you can basically, you know, make an oscillator, and then you can push it in. You know, then you can downsample stuff and, you know, basically push around in the spectrum. And then you can actually, you know, change sample rates. You can, what do they call that? Oh, my signal stuff is failing me. Decimate. Decimate. Thank you. Yes. Decimate and interpolate and all that stuff. And basically, do DSP-type stuff without much hassle.

**Dave Jones:** So, is that asterisk? That sounds like software, though.

**Speaker ?:** Yeah.

**Dave Jones:** That sounds like the software. So, there's a hardware part, I assume.

**Chris Gammell:** Yeah. Oh, yeah. So, the thing I bought is like a $300. Basically, it is a NXP part that then basically goes to an RF front end and then an antenna. And basically, it's just like, so like I've explained it for Mike, when I've talked about for Mike before, I said it's basically like a software interface to RF. And it's great for that stuff. So, it's pretty cool. I mean, it's. Yeah. And so, I didn't realize GNU Radio is actually basically just doing a graphical block and then writing Python on the back end. So, it's just generating Python. Okay. And you can hook things together. And yeah, it's really great for troubleshooting and hacking and, you know, kind of figuring out what's going on in the spectrum. So, that's pretty neat.

**Chris Gammell:** You have a such a fine radio too.

**Dave Jones:** I have one of the RTL-STR dongles. Yes. Which is a little $20 thing that does something. I haven't played with it that much.

**Chris Gammell:** Right. Yeah. So, that one's basically, that's a TV tuner. That's an old TV tuner. And then it, you basically can look at, yeah, you can basically kind of slide around. You can slide the frequency around so you can tell what frequency you're shifting from. Right. So, you know, if you're trying to look at signals up at 2.4 gigahertz, you basically tell the device basically says 2.4 gigahertz and then you, you know, shift it down into baseband. And then you can look at it in something like SDR sharp. Right. That's. Right. I assume what you're doing with it. Yeah. That's just received though. And you can tune all the hand bands and stuff. Yeah. It's just received. So, that's just received. With the HackRF, you can actually transmit as well, like low power. But, so that's pretty neat.

**Chris Gammell:** You are responsible for using your HackRF1 legally.

**Chris Gammell:** That's right. Yes. I think, I think the low power really helps a lot of that stuff. But yeah, it's not hard to change low power to high power. Yeah. Right. Amplifiers, huh? So, yeah, I have, I had a lot of trouble getting it set up, to be honest. It was, it was much more difficult than I thought that would be. They basically say you should use Pen2, which is a distribution of Linux, which is based on Gen2, which itself is not super friendly. And, and my mistake is I cannot. Why did they choose that? I think it was just what they were on. It's like a security based Linux thing. So, it makes sense that, you know, the security people would be doing that. But, um, my mistake was I kept trying to force the issue. I was like, oh, I'm going to have my Mac, MacBook Pro with me. I'm going to try and put on the MacBook and just trying to get, uh, you know, stuff installed as a secondary OS and, uh, it's just, it's a hot mess. And plus it's got the USB-C ports. So, like, I'm just, I'm, I'm like, all right, well, I just need to buy a computer just for that. I know that's not actually, like, if someone heard me say that who was with an hack RF, they'd be like, oh, get a Linux, a Windows computer, a Linux computer. But, um, yeah, my experience with Macs has been very, very poor so far. So, um, but otherwise, yeah, you know, I'm sure that you can both commiserate on using Macs fault.

**Dave Jones:** I'm not sure it's the Macs fault that a completely obscure distribution of Linux has been chosen. I don't know.

**Chris Gammell:** You ever tried, like, installing, uh, like, just even Ubuntu on it? Like, on, oh, yeah, maybe I'll have to ask you more about that after the, after the show. I'm having a lot of trouble with that, so. And I'm talking, like, no, no VMs, though. Like, I, so, like, I had asked, you can't use Bootcamp. You have to use, you have to basically use, like, a, a different boot start thingy. I'm sure that people are going to write in and be all angry about this stuff, but I'm just, I've really struggled with it, so. Yeah, if you can't use a VM, that gets trickier.

**Dave Jones:** Yeah.

**Chris Gammell:** Right. I did a VM, but, like, basically, it's so, the couple, the hardware is so coupled that, like, you get all these over, overruns really, really quickly. So, it's, um, yeah, I've just got to try it elsewhere. So, with Linux, I mean, so with Ubuntu, even, there's a, there's a build for it now as well. And that's, and that's what Dominic, one of the other software people at Great Scott told me to use. So, um, it's better. Yeah. Uh, yeah. So, I got that. What are you going to do? And I got a bunch. Oh, um, well, so, yeah, the, uh, so I'm playing with LoRa modules, like I mentioned at the beginning. And, uh, so basically just having troubleshooting for that and just kind of seeing what's going on there. Obviously, I'm doing cellular stuff. So, just kind of peeking at the spectrum and having a better grasp of it all. Bought yourself a work tool. I know.

**Chris Gammell:** I bought myself a work tool.

**Chris Gammell:** I mean, yeah, my, yeah, my business bought me a work tool. So, yeah, I think it's a similar kind of thing. Uh, yeah. And, uh, it's, I don't know. It's, it's an interesting, I just, I, I, I wish someone would have showed me this. So, like, you can just go and watch, uh, I think I mentioned this on the last amp hour, but you can just go and watch Mike Ostman's, like, intro video for it. And I just wish that something like that would have been around, uh, when I was learning signal stuff. Like, just, just show, show me that, right? Show someone hooking stuff together. You're basically, you know, you're demodulating a FM signal, you know, you're using some blocks. So, yes, of course, you're hand waving a little bit there, but man, at the end that you have, like, an audio signature, like, it's just, it's fantastic. You know, it's, it's, it's context. And, and, uh, and that's what I, I really missed about the, my learning process in school. And I think we've talked about this, you know, endlessly now, but like, but like these kind of tools are just, make it so clear, even at the beginning. So, like, I was listening to your show. Your last show was with, uh, the Udacity person. Yeah. Yeah. It was great. And I sent you, I sent you that, um, so he talked about the, the Dreyfus, or you, you told him about the Dreyfus model, I think.

**Chris Gammell:** Yeah. Yeah. We, we talked about it to him, which was a little odd because I was hoping, I was hoping for a pedagogy from Udacity, but.

**Chris Gammell:** Yeah.

**Chris Gammell:** That wasn't Anthony's bottle of wax, so that's fine.

**Chris Gammell:** Oh yeah. And I, I meant to tell you this on, on, uh, the secret Slack channel that I'm on with you guys.

**Chris Gammell:** You can't say that out loud. Oh no. You have to type into us instead.

**Chris Gammell:** Yeah. Sorry. Um, the, uh, I, I learned from Mel. So I had sent you both, uh, a comic about, about the Dreyfus model. Uh, it's a, uh, by, by a friend Mel and Mel told me, uh, or something very interesting. Pedagogy is the wrong term. Is it? Did you know that? No. It's andragogy. Andragogy.

**Chris Gammell:** Oh, because we're adults.

**Chris Gammell:** Exactly. I was like, oh my God. Yeah, of course. Right. But it's like, that's just the, the accepted term is pedagogy. Right. But it's actually, yeah, pedagogy is for children.

**Dave Jones:** Are you being pedantic or andrantic now? That's very nice.

**Chris Gammell:** Pedantic or andrant. I think we've just found a title for the show. Uh, yeah. Uh, I, I don't know. Um.

**Chris Gammell:** I'm sticking with pedagogy because.

**Chris Gammell:** Because people know what you're talking about. Yeah.

**Chris Gammell:** Or at least they, they have heard that word.

**Chris Gammell:** Right.

**Chris Gammell:** Uh, but I, I will accept that it is wrong. Just like how, when I say lead sentence, Christopher corrects my spelling on that. And I'm like, yeah, still don't care.

**Dave Jones:** Right. Well, this is an exciting tour through linguistics.

**Chris Gammell:** Uh. Well. So the Dreyfus model though. I love the Dreyfus model. Right. And, and, and you were both talking about that. Uh, but the Dreyfus model is great because it's like these different stages of like, I, the, the thing that I loved about Mel's comic is, is basically like you're, you're going to cook a thing. Right. You're going to cook a thing. And the first thing that, that, that an absolute beginner asks is like, you need to say like, you crack an egg into the bowl and here's what an egg looks like. Like, that's the stuff that you don't even think about. Like, oh yeah, of course. Someone who's an absolute beginner needs to know what an egg actually looks like. And I, I love that. I just, I don't know. It was, it was great. I will post that comic. So.

**Chris Gammell:** It's a great comic and it, it doesn't, it shows you the Dreyfus models. Um, and it kind of, I mean, there's been a few people who have been talking about how you don't teach experts the same way you teach novices.

**Chris Gammell:** Yep. Yep. Um, so Daniel Spalding is, is a, is a book about teaching adults as well. And he talks about that. I've talked about that, I think before. So.

**Chris Gammell:** What is it?

**Chris Gammell:** Daniel Spalding. He has a, it's, I think it's just an ebook. Um, Daniel Spalding is a book called Teaching Adults and it specifically covers that.

**Chris Gammell:** Oh, it's funny. I'm looking at a book, How to Teach Programming and Other Things.

**Chris Gammell:** Oh, okay.

**Chris Gammell:** Um, which I don't think is the same person. It's How to Teach is his site. Okay. But he talks about how a novice with computer programming may not understand that there is a difference between, that there is no real useful difference between cutting and pasting a program into something and typing it in character by character, that those are identical to a compiler or to an interpreter. Uh-huh. They're not even wrong. There's no, there's just no mental model and how, how you have to build things up. And I think, I think if more people know about the Dreyfus model, we can start talking about the things inside there and how you can, oh, you sent over a link, um, the advanced expert. So the Dreyfus model starts out with the novice where you really don't know anything. And then the advanced beginner where you start to know things. And then the third level is competency. So that, that kind of, most people know what those three things are. And you sent over an article that talked about the advanced expert where you, instead of becoming competent, you wander off into your own little branch and you can never really become competent from there because you have like defined your own science. And so you can't go beyond that. You have to know that you're a beginner in order to learn more.

**Dave Jones:** It's never like Dunning-Kruger lives. Yes.

**Chris Gammell:** It's, it's the, it's the lane that, uh, that you wander down, right? Yeah. I'm, uh, well, and I think this is actually pretty, pretty poignant because I'm kind of in this realm of like, I'm trying to relearn software. Um, and, uh, I'm really, I'm really struggling. Like I'm really having a tough time and I don't really know where to go next. And like, you know, people point me to like, oh, coding bootcamps.

**Dave Jones:** Yeah, yeah, yeah. That's all one size fits all stuff. So I would ask you since you didn't ask her advice, but sure. So hasn't stopped you in the past, man. What do you want to do with it? Okay. What would be the first question? And, uh, how are you attempting to learn now?

**Chris Gammell:** The answer is, uh, I want to do my job. Okay. And, uh, how am I attempting to learn is going like, just like screaming and, and Googling stuff, um, pretty much.

**Chris Gammell:** So, so this is, this is a case of definitely, um, do what I say and not what I do, but getting frustrated doesn't help.

**Chris Gammell:** Oh, okay. Well, I'll just stop doing that. Click.

**Chris Gammell:** Yeah.

**Chris Gammell:** Just turn off like that. Uh, when, uh, data in, in Star Trek, he just like turns off his emotion chip. You have just, oh, okay.

**Dave Jones:** Turn off your frustrator chip.

**Chris Gammell:** Yeah. That was easy.

**Dave Jones:** But for your job, I mean, what do you need to, what, what, my job these days is, no, no,

**Chris Gammell:** no, it's, it's not secrets. It's like basically like making tutorials. Like I just have to go out and like, so like the hardest thing is when there's a new platform, right? You have to kind of just go and make examples for people and you have to learn stuff and you have to struggle. You're basically just struggling for people so that they have a starting point. And, um, and some of it is just, I mean, some of it literally is tenacity. Right. And like, and I, the thing I always emphasize is that like, when I, when I think of something like Ben Krasnow who I, you know, hold up as, you know, uh, you know, the, the great prototyper, right. It's, it's, it's just tenacity. Right. Or like, or like Sammy Kamkar, right. Sammy is like super tenacious and they, people like that, you know, they just, or Micah, Micah just, you know, just keeps trying different things and has, is, is, uh, methodical about it. Right. That, that whole, like, so I, I, I've been meaning to, to laser cut a thing above my, above my bench, but just say experiment first. Right. So like the best prototypers, the best people doing this stuff, they're, they're not necessarily like, I'm, I'm just kind of floundering, but they're, they, they basically say, I want to try, I have a, I have a, I have a thesis or, uh, I have a, uh, what's the word?

**Chris Gammell:** I have a goal, uh, uh, no scientific thought on how this works. I mean, hypothesis.

**Chris Gammell:** Hypothesis. That's the word. Thank you. I have a hypothesis and here's what it is. I'm going to try X, Y, Z and I try it. And then do I meet the hypothesis? If not, you know, cycle back through, like basically applying the scientific method to prototyping is, is like a goal of mine. And I, I really struggle with it. I mean, like it's because there's so much information out there as well. Like, so there's also the whole, you know, tuning out the world and not getting super frustrating and just Googling everything.

**Dave Jones:** Yeah. That's a rabbit hole. I mean, you're talking about learning coding and that's not my approach. That's not my approach until I'm debugging something or there's a problem. Um, so I'm trying to think if, what, what, what, what I wonder about. Like, should I be going back to basics? Well, why, why are we the worst people to ask?

**Chris Gammell:** I don't remember how to teach somebody how to program. I mean, I mean, I mean, you, I know how to teach somebody how to learn stuff, but not right.

**Dave Jones:** I mean, somebody asked me pointers and I'm like, here's where I'm headed with this. There's the tactical part of programming, right? There's the, I'm programming in C and I know about these data structures and I know how pointers work. And then there's the mindset of programming, which is, I know how to structure a program. I now know fundamentally how a computer thinks. And I, before I even start typing, I have some idea for how this, this program or library or set of things I'm working on are going to be laid out and communicate with each other and what the memory is going to be doing. So my worry is if you start, if you start with the prototyping stuff, you're kind of in the tactical zone and you know, that, that seems like an easy place to get into trouble. So, um, if you don't have some of it is, is like the blank sheet of paper problem, right?

**Chris Gammell:** Like that's, that's kind of what I'm talking about here is like, sometimes it's just blank sheet of paper. It's like, okay, well, and, uh, there was a link that I, I, I had put on our list here from Dan Liu as well. He, he talks about, uh, at one point where he basically started having, he had a mentor that he went to and he kind of just kept, uh, he basically built confidence of like, uh, the blank sheet of paper problem, right? Of being able to like go and well, he, he basically was kept, uh, he basically kept, being presented with harder and harder problems. And then at a certain point it's like, well, I can just go and take on any problem. It's like, yeah, of course. Right. I mean, that's if with enough time and the internet, you can pretty much do anything. Um, and I, I think that's kind of, that's the blank sheet of paper problem, but the rest of it is the, okay, now you have a blank sheet of paper. What are you putting on that paper? Right. And like, how do you, what are the generally accepted methods or even like, where are the resources to go towards so that you can pre-fill some of that sheet of paper? You know what I mean?

**Chris Gammell:** So I listened to a new podcast, um, that one of our listeners, uh, is the host of the function podcast.

**Chris Gammell:** Oh, Tom Anderson.

**Chris Gammell:** With Tom Anderson. Yes. And, um, one of the ones they had was talking about notebooks and how if they get nice notebooks, they'll never use them. And they now have decided that when they get nice, nice notebooks, they put something on the first page and thereby it's ruined. It doesn't even matter what they put on. They're going to ruin their notebooks so they can use them.

**Dave Jones:** Right.

**Chris Gammell:** I feel that way about the blank sheet problem. Put anything down. Put, how are you going to debug it? Put, put, how are you going to use printf? Put hello world. And now it's not a blank sheet anymore.

**Dave Jones:** Write the problem down.

**Chris Gammell:** Write, write down the problem statement. That's good. Use the scientific method. You know?

**Dave Jones:** Yeah.

**Chris Gammell:** What is your hypothesis? What is your problem? Um, and, or, or write down something utterly generic. Like many of my projects have a debug console at one point in their lives for manufacturing or for debugging or sometimes a serial console. So I start with a serial console and that means I need a UR. Now what are my other hardware inputs and outputs? And so I need drivers and now I can test them all from the serial console and build up my whole system. And it's, it's a lot about not having a blank sheet of paper. It's about having these Lego blocks that you toss on the paper and then you can figure out how to put them together and what glue logic you need. Is that helpful? Or are you like, where did the semicolons go?

**Chris Gammell:** Oh, no. I mean like a lot of that stuff. I mean, well, I think these are two different problems too. Some of it is the, where do the semicolons go? Like what was it? Oh, it was at Supercon. I opened up Mike Harrison, you know? And so that's the opposite problem, right? So one's the blank, blank page problem, right? Of just like, all right, what's, what's first, what's next? The other problem is, okay, now you're starting from someone else's project and you open up and you're like, oh my God. Yeah. That's a different problem. Yeah. Right. And that's, and that's another problem. I mean, that's probably a little bit, well, I don't know actually what would be more likely these days. I guess, I guess if I'm Googling around and I'm trying to like, you know, piece together different things, it's kind of how fast can you, how fast can you take in what someone else has written or, you know, is trying to do and then make it your own. And that, I think some of that is just where does, not is where does semicolon go? It's what, what the hell is that? What are they doing there?

**Chris Gammell:** That becomes a lot easier if you've ever implemented anything similar, because then you know what the structures are, you know what the overall, like if you're doing signal processing, you probably need an amplifier. You probably need some sort of filter. And so when you're faced with a giant schematic, you start breaking these things down into blocks and the blocks you understand. And you have to do that with software too. If you're looking at a giant wall of software, hopefully they've broken it into some blocks for you just by files.

**Dave Jones:** But it's still going to have stuff that's video syncred. It's good. I mean, if you've never seen a linked list implemented in C, you're not going to know what you're looking at. Right.

**Chris Gammell:** And they're going to call it LL instead of linked list. So you're not going to be able to look it up.

**Dave Jones:** Or why would they do that? Pointer stuff, array stuff. Yeah. Yeah. I think diving into the deep end is not probably a healthy activity.

**Chris Gammell:** Well, there are some good sites. I mean, SparkFun and Adafruit both have a huge amount of code and they write their code with the intention that it is read. And that is a lot different than some of the open source projects that are written with the intention that it's my project. You can just get off my lawn.

**Dave Jones:** I don't think you can learn by reading code. Not initially. I think initially that's really hard. You need to do exercises and implement stuff. And that's the hump to get over because you can't really do anything exciting yet. And if you try to do something too exciting, you're just going to get frustrated. I mean, that's why courses are structured the way they are, right? I mean, you do a bunch of boring exercises.

**Chris Gammell:** Well, sort of. I mean, so I've been working on that for my course as well. If people don't know, I have an online course and I teach people hardware and thinking about and this is how I met Mel as well and learned about Dreyfus method. I was kind of starting to restructure some of my course and thinking about this because, I mean, well, so both of you, you know, are learning and or have learned hardware. And so, you know, as well, it's a similar kind of problem of like, like, why is, why, why resistor? Why, why is capacitor? And right. I mean, it's just, it doesn't make any sense at the beginning. And, you know, and obviously people start with math and they go, oh, well, let's, let's do some calculus. And so, yeah. So, yeah. I mean, I agree that like some rigor is helpful there, but it's that balance of like, where do you introduce it? I think that's the really, that's always the problem. So.

**Chris Gammell:** Just, just in case nobody has heard, what is this thing that you're talking about, about teaching electronics? Is there a name for it?

**Chris Gammell:** Yes, there is. It's called contextual electronics. Thank you. Yes. It's a course that I teach online and there's a lot of free stuff too. So like getting to Blinky is the, it's meant for getting started in ChiCab, but it's also a good introduction to doing layout just in general. And so it's basically a five, five, five timer with some, you know, like what do you need to, to get a small circuit blinking? Because blinking is the hardware equivalent of hello world. And then there's a small one as well for doing a blinker for Raspberry Pi, which is even shorter. And then there's a bunch of courses around building devices for that aren't blinking, just blinking. So, yeah.

**Chris Gammell:** I thought I would go through, I went through one of the short ones with the getting to blinking and installing KiCad and all of that. And I thought I would just do it and learn it enough that it was something I could see if I wanted to do more of. And I, I got to the end and there was no way that I could fail to send it off to Osh Park to get the board. I didn't actually stuff the board, but I did.

**Chris Gammell:** But you held it in your hand.

**Chris Gammell:** Yeah. There was something about getting to hold it in my hand that was exciting.

**Chris Gammell:** That's super exciting. That's a great feeling. That's like a dopamine rush. It's all about the dopamine, right? So, yeah. That's great.

**Speaker ?:** Yeah.

**Chris Gammell:** So, I did like, I liked the parts of contextual electronics I have taken. I think that it is very cool. Unfortunately, I have gotten very sucked into more software instead of more hardware lately.

**Chris Gammell:** So say we all. I mean, I think the, I like the comparison though about the looking at schematic and blocks because that was like a, so I think there's like different moments in hardware. Like for my own, my own journey where like certain pieces of the matrix kind of fell into place. Right. So like actually being able to visualize current in a circuit is a huge difference. Um, and then being able to actually pull out like being able to visualize blocks in a schematic and saying, oh, well that piece is just an amplifier, but with other stuff around it, that's a filter, blah, blah, blah. Right. And, and like hooking things together like that in my mind is super important. And so I assume that that's an analog to what you're talking about with the code piece as well. Whereas I just, I haven't, yeah, I haven't, I haven't figured out the blocks yet. So I, I can't just look at it.

**Dave Jones:** Yeah, exactly. Well, but that's, that's one way to start analyzing it too, because code is naturally structured as blocks. If it's written well, you know, you have individual functions that are supposed to do one thing. Um, and then you, so you can find the top level and start, start diagramming it, but you really do have to diagram it. You can't try to hold it in your head, but yeah, some of the, I mean, at interviews, some of the most deep questions I've ever gotten have nothing to do with code. It's, it's been like, uh, well, we're building the system to do this. Uh, give me the block diagram and you can, you know, you can start pretty high level and then start get to a lot of details that way.

**Chris Gammell:** Right. Yeah. And that's like pattern matching, right? That's human stuff, right? It's like, okay, well, I've seen this a hundred times, right? 90 of them have been this way. It's probably going to be this way, but maybe not. And you can discuss it there. That's experience.

**Chris Gammell:** And are you, what languages are you looking to write in?

**Chris Gammell:** So I'm doing C, I'm doing some MicroPython, CircuitPython, MicroPython. Um, and then my goal this year is to, well, I mean, Python as well, just like higher level Python. Um, but maybe do some JavaScript.

**Speaker ?:** Yeah.

**Chris Gammell:** I mean, I don't love JavaScript, but it's very useful. And it's, it's between C and Python.

**Chris Gammell:** I was inspired by Micah too. Yeah.

**Dave Jones:** I mean, like, as someone who works on a product where, where, you know. Right.

**Chris Gammell:** Your apps are written JavaScript.

**Dave Jones:** The SDK is JavaScript. I can say nothing negative.

**Chris Gammell:** You can say lots of things negative.

**Dave Jones:** No, it's actually, it's really cool. I've listened to your show. Yeah. It's the fastest damn thing to get going to write an app for something. They did a really good job. So I can't, I really can't say anything bad about it. It's great. Yeah.

**Chris Gammell:** Yeah. Sometimes we make fun of JavaScript, but we, I, it's, it's only because we're C programmers and we fought hard for that knowledge. So we have to protect it.

**Chris Gammell:** I think some of it is like, I get a little frustrated when I'm like, when I see what, like people like shoehorning it. Right. So like, like running hardware with JavaScript, I get the draw. It's like, oh, we're going to pull more people in. And I'm, I'm more for that than I used to be where I'm like, oh, okay, well, yeah, more people doing hardware is just a generally good thing. But it's like, all right, man, you could say the same thing about Python, I suppose, or CircuitPython, but like, you know, eventually you got to dive, dive down.

**Dave Jones:** It doesn't go away. People are trying to shoehorn things and all the time. Yeah. Right. Says, says the person who is trying to block his shoe.

**Chris Gammell:** Says the cobbler, the cobbler's assistant.

**Dave Jones:** A lot of rust going around. Oh yeah. Oh, interesting. A lot of people really interested in rust and trying to, trying to make it go places that probably shouldn't yet. My eyes just glaze over when I hear about that stuff.

**Chris Gammell:** Raspberry Pi and BeagleBone both made JavaScript so easy. And Python on those are so easy that I understand you start using those, you start wanting to do more hardware and you don't want to have to deal with C. So yeah, I totally understand that. But I agree with Chris, a block diagram, totally the way to start.

**Chris Gammell:** Like start teaching or start projects?

**Chris Gammell:** Start projects. You don't need to know what's in all the blocks, but...

**Dave Jones:** And analyzing other people, like you said, when you are faced with code you've never seen. Yeah. That's true.

**Chris Gammell:** Yeah. I, uh, so another thing that I've been, so, um, I think we have goals on here. We talked about goals for 2018.

**Chris Gammell:** Oh my God, do we have goals for 2018? Yeah, we do have goals for 2018.

**Chris Gammell:** Someone wrote it. I didn't, I don't know if it was me. It might've been me.

**Dave Jones:** Definitely wasn't me. I just saw this diagram an hour ago.

**Chris Gammell:** Um, yeah. Uh, so my goal for 2017, which did not go super great was to get better at iteration. And, uh, I think that's a really big piece too, because it's kind of what you're talking about. It's like, I, I think a lot of this is still residual school stuff personally. Like you need to get it right. It needs to be right the first time. And it, you know, you, you know, it's like that, that's a really bad, I'm very against that because the best people just iterate and understand that there will be iteration, including for hardware. Right? Like, so yes, I want to get my circuit board right the first time, but it's not the end of the world. If it's not right the first time, um, you should send it out. Right. Um, and a lot of people get hung up on that piece, especially cause it's so cheap these days. Um, same thing for code. It's like, yeah, it might not work, but then you just recompile it and try it again. Um, so.

**Dave Jones:** Some of that, I mean, I, I, I agree with that. Iteration is important and getting good at it. I do think sometimes easy, easy iteration, uh, becomes an excuse to not think.

**Chris Gammell:** I'm a monkey typing at a keyboard and I will just type all the options.

**Dave Jones:** And that's not an accusation. And I do this all the time. Oh yeah. I'm debugging. It's like, okay, I'll just change this line. Well, there's this parameter. I'll just change it. You know, there's only 600 possible combinations. So how long. Finary tree. At one minute. At one minute. That'll take me the weekend. Compile and download. That'll take a 10 hours. So I'll just do that. But, but you know, or I could go sit and think for two hours and oh, that's the actual problem. Yeah. Right. So yeah, there's a balance, but.

**Chris Gammell:** Yes, it is a balance. I actually, I have a theory that, um, so every time I see people using an other mill, I think the other mill, which I love as a tool. I think that that is a saw. I think that that company has been bolstered by software people. They see hardware and they go, I need to iterate faster. And I will do anything to, to do that. And I think, I think the other mill is a path forward. I don't know if it's the only path forward, but software people are like one of the main clients there. Um, cause I look at it, I'm like, I can't use that for much. So.

**Chris Gammell:** I would use it for jewelry and fun things, but not, not for boards. I never really understood the board thing.

**Chris Gammell:** I just, I love solder mask, so gotta have it. You know? Uh, yeah. Not everybody does though. So.

**Chris Gammell:** Okay. So that was the not goal for 2017. Do you have actual goals for 2018 or are you just carrying that one over?

**Chris Gammell:** I have themes, which is like the biggest cop out ever. Um, but basically when I came up with, uh, I should probably publish it this year if I'm going to talk about it here. Um, so yeah, I had other ones for 2017. So iteration was the first one. I did okay on that. Uh, uh, was that the other one from last year? Flexibility last year. Not great. And then temperance. I did get on that. Uh, and so this year I have experiment slash risk taking. That's the big one. Uh, produce efficiently and then tell stories. Those are my, my three themes for 2018. And, um, produce efficiency efficiently is something that I'm very about. I have been about because like, like just basically reducing overhead on projects, you know, being able to iterate faster means you need to lower your overhead. So like video editing was a big one in 2017. Um, so, but you know, that's like workflow stuff. So like just improving workflow so that you can iterate faster and you can, you know, it's, uh, there's a lot of stuff in there or layers in that, that thing. But, uh, tell stories is pretty self-evident, I think. Um, and then experiment risk taking, I think is also, uh, you know, but that's also like trying RF. RF scares the shit out of me, to be honest. Excuse my French. Uh, uh, it's, I don't know why. It's just always scared me. I've never, you know, I have a ham license and I've never used it. So, uh, 2018 is the year of RF. So.

**Dave Jones:** I have a ham license and I know how to use it. No.

**Chris Gammell:** All right. You're not afraid to use it, huh? No. Uh, do, do you have any goals? I don't do that. Mm. Good policy.

**Chris Gammell:** I have a couple of goals. I don't know if they're 2018 specific. I remember one year I had a resolution to have a resolution every week for the year. That's right. That was pretty amusing that every week I would try something different. And they were things like go out after dark to do things at least five days out of seven or not eat any sugar for a month was probably what killed the whole thing because a month was way too long to go without sugar. And, um, and that was, that was pretty cool. That was very adventurous and led to lots of different interesting things. Um, between eating grains for at least three times a day or, or baking bread. It was, it was fun. Um, but I don't think I have anything like that this year. I've been on a kick of learn hard things. Learning easy things is fun, but everyone can learn easy things. If I want it to be relevant career wise, I need to learn hard things because not as many people will be able to learn hard things. And if I can mix them together the right way, then it will be very useful.

**Chris Gammell:** Do you have examples?

**Chris Gammell:** Well, like I've been doing computer vision and, and robotics and machine learning. And I have been trying to learn all three of these things and it's really hard to do all of them. And I took the Udacity self-driving car class for the term one, which had some computer vision and some machine learning, but that was very much at the Dreyfus, uh, beginner, advanced beginner stage.

**Chris Gammell:** What does an egg look like?

**Chris Gammell:** No, it got past the, it got past the novice of what is the egg.

**Dave Jones:** I was doing some pretty, I mean, I don't know how easy these things are, but some of the exercises I was looking at what you were doing going, whoa, what, really? Like, oh, the car is, you know, it's marking all the lanes and you have to take their video driving and mark all the cars. Like, wow, this is really sophisticated stuff. And you're only a couple of weeks in. So it seemed cool from the outside.

**Chris Gammell:** It was cool. And I learned a ton, but I was following their recipes.

**Chris Gammell:** Okay. Right. Right. So it's like cocktail party. Cool. Right. It's like, oh, wow, that, that has like some flash to it, but you're saying that you couldn't, it, if you didn't have the recipe, you wouldn't necessarily go far.

**Chris Gammell:** Well, I am saying that I started that way. Um, I have been working on my own robotics, AI computer vision project. And without the information from the class, I would have a whole bunch of things. I don't know. I would have 95% unknowns, but because of the class, I, I learned Python much better. I learned open computer, open CV much better. Um, and so now as I'm trying to solve my own problems, I'm down to 40% unknowns, which that I can start looking up that I can Google, I can read the books, um, and I'm not completely bewildered. Uh, and that's been leading to some neat things that I didn't expect.

**Dave Jones:** That's the thing I was thinking, I didn't say well, we were talking about learning is you kind of have to have a hook. You kind of have to have a hook to learn. Knowing what to Google for. Well, that, but you know, you need like to learn C or Python. You, you got better at C at Python by taking this course about machine learning and machine vision, not about Python. And so you had a, you had a good hook to get you interested and, you know, kind of backdoor teach you Python. So I think that's really important and it's hard to find the right hook sometimes.

**Chris Gammell:** Well, it was, I mean, so you mean like a project though? Like that's, that's the hook you're talking about?

**Dave Jones:** Yeah, a project or, you know, a course or something. Totally. But it's not, you don't go out and say, oh, I want to learn Python. So I'll take the Python course necessarily. No, I totally agree. Right.

**Chris Gammell:** No, exactly. And I read a lot of their Python. And so some of the things like some really bad ways of doing lists and slicing them, I got better because I was looking at how they were doing it and it was much clearer and simpler and probably a lot faster. I mean, that was, that was part of the thing. I wrote a book. I don't know if your listeners know that. Heck, I don't even know if my listeners know that, but I did write a book about embedded systems.

**Dave Jones:** Hey, we've all plugged something this episode.

**Chris Gammell:** I was going to say, yeah, it's good. It's good. You're doing that. Also, people may remember this from when you were on the show the first time. I think we talked about it then. Episode 187, Wirewove Worshipping Wookieist. Back when we did that whole mess.

**Chris Gammell:** But a lot of the pitch for my book was that you would only learn half the book. The other half of the book you'd already know. It was for people who already knew some computer science or people who already knew some electrical engineering. And the idea was you would cantilever off the knowledge you had into the other half. And I think that's important. I think it's important for me as I learn because I need to attach it to something or I just don't. I see it and it goes by and I don't catch it. So, yeah, with the Python, it had to be part of machine learning because I really wanted to learn the machine learning part. And even the machine learning had to be attached to something, which is why I have my little typing robot. And that's really just attached to my sense of humor because it's so ridiculous.

**Chris Gammell:** Right. So, do you think that's enough of a draw? If you had, okay, so say your dogs needed computer vision help to do something, right? Would that be a different draw? Like, is the typing robot itself enough of a draw?

**Chris Gammell:** It is for me. Of a project. It wouldn't be for everyone. It is for me because career-wise, the ability to identify and react to environmental stimulus through a robot in which I can explain the kinematics and the drive mechanisms, that's all career-wise very good for me. Got it. But if I was a home hobbyist and I really didn't care about being able to talk about these in job interviews, then, yeah, being able to open the door for my dog when it wants to come in. Totally different set of things. Maybe I wouldn't be spending nearly as much time doing matrix math. Maybe I wouldn't be spending nearly as much time drawing out what I'm learning and trying to make sure that I can explain what I'm learning. Different paths are great for different people. But for me, for 2018 and for last half of 2017, it's been learn hard things because that's what I need to do. I think I spent too much time learning easy things, learning fun things. And I forgot some of that tenacity and some of that resilience that I needed to stick with it.

**Chris Gammell:** Yep. I always tell people about that too with like, you never learn hardware when you're actually manufacturing it. Like in volume if you can, but if not, I mean, even if it's low volume, you just don't realize how much stuff will go wrong. And, and that's why you always read about people like, oh, well, our stuff's 18 months late because we forgot about A, B, and C. It's like, we didn't forget about it. You probably just didn't know about it and you didn't think to ask people because you don't know what to ask. So that's, that's tough.

**Chris Gammell:** And so you try it. I mean, that's the iteration part.

**Chris Gammell:** Right. But, well, yes, but I think that the, the thing is like finding a mission also helps, right? For some people it's like, oh, I have a Kickstarter. I want this thing in the world. Then they, then they finally go for it. Yeah.

**Chris Gammell:** Oh yeah. Applications always matter to me. I mean, the typing robot, it's, I'm hoping at the end it is nearly performance art, even though there are plenty of other robots that can type. The combination of the cheapest possible robot arm and the ridiculously expensive intelligence and, and the two cameras that require it, it's just going to be very silly.

**Dave Jones:** Yeah.

**Chris Gammell:** It's really ridiculous. Yes.

**Dave Jones:** And that, who specified this?

**Chris Gammell:** It, it, it makes me laugh and that's what I wanted to do. Laughing.

**Chris Gammell:** Right. Right. There was a, there was an article I posted too about, it was, I mean, it was definitely an auxiliary industry. It was about reading though. And about like people teaching like literature. And it was kind of in the same realm, right? Of like the struggle is the important thing, right? Or the, what did they say? The, the difficulty is the point. You know? So like finding these hard problems that you're talking about is like its own reward. I mean, obviously you get to solve the problem, but you also get the stuff by proxy. You get the information and the knowledge by proxy. So that's, that's a good, I think that's a really good goal to have. I mean, or goal or theme or whatever it is. So.

**Chris Gammell:** I think the other theme is mental health this year.

**Chris Gammell:** Yeah. Yeah. A little too much work last year?

**Chris Gammell:** No, no, actually it wasn't too much work. Um, I don't know what it was.

**Chris Gammell:** Okay. Was this, oh, you posted another podcast that I started listening. The, uh, Thwad. Someone posted this.

**Chris Gammell:** Oh, oh yeah. No, that was, that was, uh, yeah. So I started listening to this APM NPR podcast. Um, the hilarious world of depression.

**Chris Gammell:** Yeah. Uh, it was really good. The one with Jeff Tweedy was really, really good.

**Chris Gammell:** I haven't heard that one yet, but it's, it's really high functioning, really funny, smart people talking about their struggles with depression. And, um, the thing I have most taken away is that I need to stop pretending that I don't have a problem or that I have a little problem and I need to go get some help. Because I clearly have a big problem. These people are talking about their problems as having a big problem. And I'm thinking, oh, that's not that big a deal. I deal with that all the time.

**Chris Gammell:** Maybe I need to see somebody about this. Yeah. No, I think it's, it's, it's, and it's very, I think in engineering, especially like, you know, like smart people have this stuff and they're like, well, I can think my way out of it. It's like, well, sure. That's not always, that is not always, uh, sometimes it's chemical. So I've been to therapy. If it's, you know, that's, I'd say wonderful thing. I, I love it. I, it was a great time for me. Not a great time. It was a terrible time, but like, you know, it was a very helpful thing. And I think that, you know, if people, you know, if it's out there and people realize that it's, it's more common than they think. Yeah. I think it's a good to go talk to someone, you know?

**Chris Gammell:** See, you're so lucky. I've been to two therapists in my life and they both sucked. Like really, like one, after I left, I was way more messed up. The other one kind of looked at me as a high functioning engineer and was like, oh, well, we don't need to see each other anymore. And I'm like, yeah, I haven't even started to tell you my problems because honestly, I'm not the sort of person who can just tell you on the first date.

**Chris Gammell:** So you're right.

**Chris Gammell:** We don't need to see each other anymore.

**Chris Gammell:** Right. No, I've had, I've had bad ones too. So, um, I've had good ones and bad ones. So, you know how many.

**Chris Gammell:** Yeah. And well, in that hilarious world of depression talks about it, it's, you do need to go through four to six in order to find one. And even that is, that's average, not, you have to find one that can deal with you.

**Chris Gammell:** Yep. Yeah. So yeah.

**Chris Gammell:** Mental health 2018.

**Chris Gammell:** I like that.

**Chris Gammell:** Um, see, I have questions from listeners for hardware things that we couldn't answer.

**Chris Gammell:** Oh, I will join you in not being able to answer them. Go ahead.

**Chris Gammell:** Um, there was one from Tyler. Uh, his question is, how can he make prototyping cheaper and faster? See, this is such a softball question for you. He says, my college taught wire wrapping. What was it like 1920? And it was basically tortoise.

**Dave Jones:** What is it with the DVD commentary?

**Chris Gammell:** I'm currently considered using KiCad because it's free and ordering PCBs from something like Oshpark. A lot of the homemade PCB solutions don't look appealing. Maybe we can recommend something. Can we recommend something?

**Chris Gammell:** Sure. Yeah. Okay. That's pretty easy. Yeah. You're right. That is a softball. I mean, but here's the thing I'll say, right? Uh, whatever you pick as your first CAD program, you're probably getting used for a long time. So keep that in mind. Choose wisely. I mean, like, and it's not, I, I, I have gotten past the point where if people aren't using KiCad, KiCad, whatever, I don't care anymore. Uh, I still want to help people with electronics problems, but I teach with it. So that's why. And I think it's actually pretty great. So yeah, uh, I think Tyler would definitely benefit from that. I would also caution though, as well, I jump into using PC, uh, layout programs way too fast. Um, you know, don't necessarily wire wrap, but man, uh, uh, Skywire and like just duct tape stuff together and like the best prototypers, right? So like, I, I like talking about the best prototypers I talked about, like Ben and Micah and everyone like that. Like they, they bodge stuff at first, right? They take existing solutions. So Alan, uh, uh, Yates, who's also been on the, on our show before. And I think your show, yeah, your show too. Um, so he talks about as well, uh, Jerry, all these people that were, uh, Jeff, all these people that have been at valve and elsewhere, uh, the best prototypers, I think they take what they can, they do the most they can with the hardware they have. And so if that's wire wrap, that's fine. Right. Uh, if it's, you know, a, um, development board where you're then wiring in a sensor, right? So you have a sensor board breakout and you're wiring, you're just literally wiring two boards together. That's great. If you're using a breadboard, I'm not a huge fan of breadboards, but sometimes that is the solution. So, uh, plugging stuff together with those wires, uh, and up until like about 10 megahertz or so, you don't really have to worry too much from there for sure. Yeah. The layout and, uh, learning that stuff and start small. Like we talked about on the show already. So get something to blink and, you know, maybe Kaikad's the way for you. So, uh, Oshpark, of course, I love as well. So.

**Chris Gammell:** Yeah. No, no, that makes sense. Uh, I, I agree. If you can find a dev board that's even the least bit simple, similar to what your goal is, start there. I mean, you can go pretty far.

**Dave Jones:** The modular world is pretty extensive these days. Modular is awesome. Right. So you can get. Yeah.

**Chris Gammell:** I've been pointing people to Tindy, Tindy very often. I mean, obviously I used to work at the company that owns Tindy, but like more and more people are putting stuff on their Tindy, eBay, you know, uh, you know, maybe even looking on like a hack day IO or a hackster and like finding people that are already doing it and be like, Hey, do you have any extras? Like just like reaching out to people too. You never know. And, uh, and they might point you to stuff that they've used too. So a little bit of extra legwork can save you lots of time because nothing's worse than, you know, like getting all the way through a design cycle, right? You're designing a breakout for a sensor and then you make a mistake on the board and you got to do another cycle there. It's like, if you can pay a little more, even, I know that's, they asked, um, cheaper and faster, right? So cheaper, sometimes it's worth it. It is cheaper to pay a little more. That sounds stupid, but. Well, the cheap and good axes, right? Right. Right. Yeah.

**Chris Gammell:** Well, there's even just the cheap and fast. I mean, if you get a dev board from SparkFun, maybe it's $30. Maybe all of the parts on it only cost about five. Well, if you make your own and you don't even count your time by the time you have made a board and stuffed it.

**Dave Jones:** Right. It's a lot more than 30 bucks. And one of the one. Yep.

**Chris Gammell:** Yeah. That's the difference between prototyping. With prototyping, buy off the shelf if you can, because it will be cheaper. Now, when you're, when you start making 10 and then a hundred and then maybe a million, you, the economies of scale are not the same as they are when you're making one or three.

**Chris Gammell:** Right.

**Chris Gammell:** So, yeah.

**Chris Gammell:** And at that point, someone else might be doing your layout anyway. So, yeah, it's somewhere between about five and a hundred. You're probably gonna have to make your own board and you probably have to learn some methods that you might not already know. So, um, but that won't be faster. Kidding. Yeah. Yeah. Yeah. So, um, I don't know if we had, did, did that answer the question or no? I think so. I think so. I think my problem is that I've gotten into the, I've, I've gotten so far into like the pay, pay to solve my problems stuff these days. Yes. Like I pay for software now, like happily, like I have a smile on my face when I pay for software. Like 10 years ago, me is like, what are you doing? Just struggle with GIMP for a while longer. Um, no. Inkscape isn't so bad. Yeah. Right. Um, so yeah. And like these days though, like I just love paying a little bit more and for like solved problems. Right. So like both of you are fans of the Salie. I think Salie is fantastic. That's like a logic analyzer with like a really intuitive interface. That's a solved problem now. Same thing with like, I like the analog discovery too. You've talked about that too. Like from test equipment side of things, pay for that. No problem. Software pay for that. No problem. Breakout hardware pay for that. No problem. Granted. The caveat here is hardware is expensive. It's so expensive. So just keep that in mind.

**Dave Jones:** That's cheaper than it was. I mean, a logic analyzer.

**Chris Gammell:** Cheaper than it was.

**Dave Jones:** You know, the first time I used a logic analyzer was this giant thing from HP that probably came with a personal support engineer. Yep.

**Chris Gammell:** Yeah. And it's getting better and better. Like, I mean, like, well, like, like just even looking at the number of Tindy sellers, there's so many people doing that. Or if you watch, uh, so I was just watching that's the funny sounding Swiss engineer. He calls himself, uh, Matthias, I think, uh, one of the YouTubers, he does, he does mailbags and then Mick makes does mailbags and Dave, my cohost does mailbags. And like, I'm just thinking about like, how many people are sending boards around to everyone? Like what a, what a wonderful world we're living in where there's just hardware floating through the postal system to, to random people. Well, obviously YouTubers, but like.

**Chris Gammell:** We, we, we got, we got random hardware and it wasn't because of the show.

**Chris Gammell:** Whoa. Really?

**Chris Gammell:** BMW sent us this package. Oh God. And in the package.

**Chris Gammell:** This is a different reason though.

**Chris Gammell:** You, so you open up the container. It's a little booklet. It's a little booklet. And then there's this booklet.

**Chris Gammell:** Yeah.

**Chris Gammell:** And it's, it's, it's like a hardbound picture book. So it's, it's.

**Dave Jones:** Not super hardbound, but it's cardboard. It's, it's solid. Yeah.

**Chris Gammell:** And then you, you open up the right flap and then you open up the left flap and a video starts playing and music starts playing. And there's a video player in this little book thing.

**Dave Jones:** They snail mailed a YouTube ad to us.

**Chris Gammell:** They, they snail mailed a YouTube ad. And when I pushed skip, there was no good video afterwards.

**Dave Jones:** It's like a five inch 800 by 500 display with a speaker and. It had a pretty big resolution in there.

**Speaker ?:** Yeah.

**Dave Jones:** Wow. Yeah. So she tore it to shreds. And, you know, it's got a.

**Chris Gammell:** And there's pictures that will go online at some point, right?

**Dave Jones:** It's got a high, it's got a, some arm chip from all winter, I think. And, you know, flash and RAM and display.

**Chris Gammell:** And a USB port. Yeah. Which I will so not plug into anything. And you, you thought that you could change out the video on the USB port. Apparently this is some sort of video greeting card that has been going around this whole thing.

**Dave Jones:** Yeah. Somebody's got this. I've seen these before. Yeah. But it was.

**Chris Gammell:** But they're not cheap. They're like 15, 10, 15 bucks each. But the thing is, if you buy a BMW, I mean like, so, okay, let's, let's do some, you know, some analytics.

**Chris Gammell:** But we are not really BMW customers.

**Chris Gammell:** Yeah. I've never heard of BMW in my life. Well, you are fancy car customers. Let's be honest about that.

**Chris Gammell:** We are specific fancy car customers.

**Dave Jones:** Well, I'm the sort of fancy car customer who's not going to buy a car because you sent me a video player.

**Chris Gammell:** I, it was a negative to me. I'm like, come on. I'm like, come on. Can't you have like put this into your car?

**Chris Gammell:** I mean, the i8 is a beautiful car. I don't know if you've seen it. It's a beautiful car. So. Kind of looks like it is. I'm 11 in the back. I mean, I think it's beautiful, but yeah, I, I can't afford any of these cars. So yeah. Also, I don't have a car. So, you know, there's also that. Did you give up a car going to Chicago? Oh, you didn't know that. Yeah. I haven't had a car in a year and a half. That's fantastic. Yeah. I drive a car every like six months now. I just drove one in the snow. That's a great way to get reintroduced to that, to that experience. Yeah, no, it's, it's, I'm, I'm on a train line here. So it's, it's great.

**Chris Gammell:** Wait a minute. You, you were texting with me and you said you were in, I thought somebody else was driving. Yeah, my dad was. Oh, all right.

**Chris Gammell:** Yes, we were texting. And yes, I did say I was driving. I was not actually driving at that point. I was in a car a lot this weekend.

**Chris Gammell:** Gosh, don't text and drive.

**Chris Gammell:** That's right. I agree with that. Yeah.

**Chris Gammell:** Yeah.

**Chris Gammell:** I'm all about the self-driving. I'm, I'm so excited for the self-driving car thing.

**Chris Gammell:** Me too.

**Chris Gammell:** Like, I don't need that. I like, I mean, I have self-driving cars. It's just the, the compute, I've, I've said before, it's a meat controller, right? It's not to disparage, you know, Uber and Lyft drivers, but like, they're getting replaced and like, I'm not going to miss them that much. You know, like they're. Yeah. The conversation isn't that great.

**Chris Gammell:** Fantastic conversations. When you come to the Bay Area, I hear every single one of them is an entrepreneur who tells you all about their ideas.

**Chris Gammell:** That doesn't happen here.

**Dave Jones:** I guess in LA, they tell you all about your screenplays.

**Chris Gammell:** Yeah. In Chicago, they talk about sports. So yeah. Hard pass. Yeah. So I'm excited to see the video, the pictures of this, this video player, but you know, it's just, it's just economics, right? If they send out a thousand dollars worth of, of video players to random people and they're, you know, you're being targeted somehow and one person buys it, that pays for itself. So boom. Advertising. Advertising.

**Dave Jones:** What a colossal waste. What a colossal waste. Merchandising.

**Chris Gammell:** It's a colossal, and I hate throwing it away. I mean, we'll take it to some electronics place and throw it away properly and maybe I'll clip the lipo off because you can never have too many. Oh, that's a big lipo. Yeah. I'll take that. I need that. Yeah. A couple hundred milliamp hours.

**Speaker ?:** No.

**Chris Gammell:** It is. That is super wasteful. 4,000.

**Chris Gammell:** Really? Yeah. Yeah. It's, it's sad that that's like throwaway because it's like, okay, well that's, that's some harmful chemicals and yeah, most people are not going to recycle it. So that's, that's a big drag.

**Chris Gammell:** I'm not, and I'm not even going to attempt to recycle the display and anything I want to use because I don't want to deal with writing your driver for that display or sourcing it. If I want to make more than one, I'll just buy one off of it. Right.

**Chris Gammell:** Yep.

**Chris Gammell:** SparkFun or whatever. Sure. Another question from Embedded Listeners for Hardware and this one is from Stanley on our Save Your Board episode with Charlie Ladd. He liked the discussion of what good hardware documentation entails, but he worries that his documentation is lacking. And he wanted to know if, if we would be willing to send an email sample so he could get a better handle on what he should be shooting for. But Stanley, we didn't do that. And I think you probably sent this like six months ago. My email is so, I'm not good at it.

**Chris Gammell:** 2018, you declare email bankruptcy?

**Chris Gammell:** Let's just say anybody who wanted a sticker had already emailed me before December 15th, has not gotten their sticker by the end of January, should email again. Because I am right now, I have sent out all of the stickers that I'm supposed to send out. I have not replied to the emails. I am declaring bankruptcy for emails sent before January or before June. Sorry. Because I'm going to admit, I'm not going to reply to them. Sorry, Stanley and probably Tyler. We're replying to his email right to Cincinnati.

**Chris Gammell:** I mean, yeah, they're getting front and center. It's just, they probably stopped listening because they felt slated.

**Speaker ?:** Yes, exactly.

**Chris Gammell:** Yeah. Do you have ideas for good documentation? Good documentation. For hardware, oh, I'm trying to think of the best hardware. Yeah, go ahead.

**Chris Gammell:** When we talked to Charlie, we talked to him about how the hardware engineers have to read a lot of the data sheets. And as they're preparing the schematics, they have to do a lot of the address lookup and how are you going to program it in order to verify this part will work. And that the firmware engineer should check all of that. But oftentimes, the firmware engineer has to redo all that work because the hardware engineer doesn't document it. And I still find that that happened recently with the project. And I do find it frustrating. I mean, you want me to change this dual pot to control this voltage and current system. I'm happy to, but can you give me like five values of what you expect so that when I do it, I know whether or not I'm doing it right? Maybe I'll have them swapped. Can you just give me some examples?

**Chris Gammell:** So like testing criteria almost?

**Chris Gammell:** I want a few testing criteria for the things that software can change. I want to know GPIOs, should they be inputs or outputs? Turned out I had an output because it said out. And so I naively thought that if the net name had the word out in it, it should be an output from my processor. But that wasn't true.

**Chris Gammell:** So I think this is a place where the software hitting the hardware world is really good because this is kind of like an API idea, right? So like ultimately what knobs can I turn, that kind of thing, like on a board. Detailing like all this stuff, like what could possibly go wrong is kind of tough because I don't know everything that can go wrong.

**Dave Jones:** Well, certainly things you've seen, right? And you can call those out to people who might not have had that experience.

**Chris Gammell:** So I'm probably not a good example of this because I'm not very good at documentation. But yeah, what is some good guy? I guess I've seen some in the past, but it depends too. Like, so like development board documentation is pretty bad usually. Um, but like my, my favorite development boards are like the ones like, so the different layers of, of abstraction almost. It's like, okay, the first thing that I get with the development board is how do I make it do interesting things? And usually there's apps or some kind of thing that interfaces to that. And then it's like, okay, now I need register maps. Like what, what, what am I going to do if I'm going to go program myself and then lay out stuff so that I know that if I go copy it and I can just replicate the thing as easily as possible. So it's like those kind of three layers of, of abstraction kind of, um, did I answer any of that stuff? I don't think I did. I'm sure hearing that.

**Chris Gammell:** No, I think.

**Chris Gammell:** Do we know what Stanley's working on? I guess that's the other question.

**Chris Gammell:** No, I, no. Uh.

**Chris Gammell:** Also, who's Charlie you're talking about? Charlie was. Charlie was the guest.

**Chris Gammell:** Um, Charlie and I worked together like 20 years ago and then again, like 18 years ago. He's one of my favorite double E's partially because he would send me Excel sheets that would tell me what the GPIOs should be inputs or outputs and whether or not they were special, which I guess like cube MX outputs that now, um, which is nice. But even then, if, if there were things I needed to know that I might miss, like it's really important that you start these chips in this order. Hmm. That sort of thing was, was always on the schematic. It was like the schematic was the interface between hardware and software and there were support documents, but I didn't have to go learn it all myself.

**Chris Gammell:** Yeah, that's good. I mean, I guess, yeah, the power of stuff is, is very important. I, and I'm, I've seen some really bad schematics. Um, I've probably mentioned them on the show before, but like some where they're just like, they, they were in some competition to squeeze as much stuff into a sheet as possible. Um, I was really proud of a student of mine, uh, who started like documenting and like adding pictures into KiCad. I didn't realize that was possible. So like, here's what this waveform should look like. And it was a screenshot of the waveform. That was killer. That's nice. And it was like in like a bounding box. And like this, this part is doing like a, a, uh, you know, a sine wave generation and here's the sine wave and this is what it looks like. And like, and then it was all hierarchical as well. Like that was great. Um, so I've seen different levels of that, you know, uh, I'm not sure, maybe it'd be better to like build a database of good versus bad, but I, I don't really have that, you know, because not everything is open. Right.

**Chris Gammell:** I think that's what I want. Uh, and maybe that's, maybe there's somebody out there who already knows that I want an open hardware project that has all the documentation, um, done well. And sure there are schematics and sure there are, it's, it's really nice to get a Gerber file when you're talking about open hardware, but what about all of the documents that go towards making the software more possible? And that doesn't work for small dev boards that are like accelerometer, uh, test boards. This only really counts if you have a processor and a couple of some things and, and then it would be really, yeah. So listeners, do you have, do you have an open source hardware that you can point us to that you would be like, this is good hardware documentation. This is what software engineers probably need when they're developing for my platform, for my open hardware platform.

**Chris Gammell:** I like that from the different perspectives too, because when I think about really good documentation, usually I'm thinking about like, well, what does a manufacturing engineer need to know? Right. Cause that's a totally different thing of like, oh, well, you know, here's the markings and make sure this part, this part is really tricky, blah, blah, blah. Like the footprint on this is really bad. This one always flips up, you know, tombstones in, in assembly. Right. That's, that's what the manufacturing engineer wants to know, um, versus the software engineer doesn't care about that.

**Chris Gammell:** Exactly. And there really are different perspectives to this.

**Chris Gammell:** Right. It's like a empathy thing, right? That's what Chris Speck talks about all the time. It's like empathy for different engineers. Um, what do they care about?

**Chris Gammell:** Yeah. Because someday you may be the software engineer, you may be the hardware engineer. You never know what's happening here. We do seem to change around.

**Chris Gammell:** Hmm. Yeah. I guess mechanical engineer would care about like part height and like things that are.

**Chris Gammell:** I remember making a board and I, I had a doubly friend help me and it turned out that neither one of us had looked at the part heights with the case. And then I had to like machine out part of the case because the screw, uh, holder. It, yeah.

**Chris Gammell:** Here's the thing. Mechanical engineers are all, let me tell you about mechanical engineers since they're not here to represent themselves. They always try and make the tightest, sleekest looking damn thing. And that's always their problem. Right. And, and of course it looks nice. Uh, but yeah, it's, it'll get you.

**Dave Jones:** Don't get me started on chemical engineers. Yeah.

**Chris Gammell:** Yeah. Do you actually work with a bunch of them too?

**Chris Gammell:** No.

**Chris Gammell:** Okay. No, yeah. I used to work with a bunch at, uh, Samsung. They're, they're very process oriented.

**Dave Jones:** They're, they're, they're, they're pretty great actually. Yeah. Civil and chemical engineers are probably, then mechanical engineers are probably the rigor, the rigorous ones. And then double A's and then software. Yeah.

**Chris Gammell:** We'll talk about long cycle times, right? They go change a bridge or, uh, or a chemical process. They literally can just blow up. So, yeah. Uh, all right. Uh, did, did we answer that question or no? I don't know if we did.

**Chris Gammell:** I, I think the real way to answer it is to ask for our listeners to answer it for us.

**Chris Gammell:** Oh, okay. Fancy. Fancy. Yeah.

**Chris Gammell:** I think that covers, uh, everything on our list. Um.

**Chris Gammell:** Really?

**Chris Gammell:** Well, I was skipping a few things.

**Chris Gammell:** All right.

**Chris Gammell:** I don't want to talk about predictions for the future. I don't really have any.

**Chris Gammell:** I don't either. Things will get worse and better.

**Chris Gammell:** Things will get mostly better, but people will complain more.

**Dave Jones:** Predictions are very hard, especially about the future. I don't know who said that, but.

**Chris Gammell:** Thanks. Uh, what, what are you guys reading maybe? Maybe that's a good question to end on. Cause that's always like futurist, futurist stuff. Also.

**Dave Jones:** All right. All right. I'll, I'll be, I'll be the, I'll be the, the, the, uh, appropriate for the show. Did I say something? I'm reading, uh, I'm reading build your own transistor radio. Yeah. Sounds like a book for four year olds, but I'm already totally confused after about eight pages.

**Chris Gammell:** Oh, that's, that's Ron. That's Ron Kwan. Yeah.

**Dave Jones:** Former guest of the Empire. So it's, it's, it's very cool. Um, but it's not, it's not simple.

**Chris Gammell:** It's no, that's a hard book. Yeah.

**Dave Jones:** Uh, yeah. So I'll probably go through some of the exercises in there and build a few of those things.

**Chris Gammell:** Uh, and I, and Ron doesn't make simple circuits either. Like, I mean, they are simple circuits, but he, he, there's another prototyping method. He, he does like dead bugging and stuff like that. And clapper clad.

**Dave Jones:** Yeah. He mentioned copper clad.

**Chris Gammell:** I'm like, what?

**Dave Jones:** No, not doing that. Yep. Okay. Yeah. What else am I reading?

**Speaker ?:** Yeah.

**Chris Gammell:** Uh, you have an SDR book too.

**Dave Jones:** Yeah. Yeah. Yeah. Uh, a book about, uh, things to do with the RTL SDR, which also has a lot of detailed, detailed kind of background electronic stuff. So, but more software. Okay. Um, so yeah, cool stuff like that. What was the laughing about? Is that, she's, she's usually the one reading the kind of books that I just mentioned.

**Chris Gammell:** So, I, so what are you reading? So my Kindle, so, so I have, I have a Kindle, uh, which I usually read at night. Um, and it usually has nonfiction on it. And for that, I recently finished a book about jellyfish. And, um, then I am currently reading a book about surviving in the wilderness because, you know, these are things that are important.

**Chris Gammell:** Well, you guys live in the wilderness, so you never know.

**Chris Gammell:** Um, but the laughter was because on my iPad, which is where I do most of my reading, my Kindle app is broken and it won't sync to Amazon. Um, and then, so I need to delete the app and then reload it entirely. But I have many downloaded books. This is essentially.

**Dave Jones:** And she can think of no method of keeping track of which books had been downloaded and re-downloading them later other than to read them all before deleting the app.

**Chris Gammell:** This is my to be read pile. And so, yes, I, I have, uh, I actually have taken a few days off with the holidays and have just blown through a large number of books.

**Dave Jones:** Yeah, you only have 57 left to go.

**Speaker ?:** Jesus.

**Chris Gammell:** As of today, I only have 52.

**Chris Gammell:** When you say downloaded books, are these non-52? Are these non, non-Kindle books? I don't get it. No, these are all Kindle books.

**Chris Gammell:** But they're books.

**Chris Gammell:** So when they re-sync when you download again?

**Chris Gammell:** No, because.

**Dave Jones:** No, because she doesn't know which ones they are because there's 800 books in our library.

**Chris Gammell:** Actually, there's something closer to 1,300 in our library.

**Chris Gammell:** Can't you mark them in the Kindle app?

**Dave Jones:** I suggested perhaps writing them down on a piece of paper. That works too, right? Yeah. That wasn't acceptable. The old ways are the best ways.

**Chris Gammell:** These are my to be read books and it's time for me to read them. And I have just been clearing them out. Okay?

**Chris Gammell:** That's great. Okay. So what else is on your list?

**Chris Gammell:** I finished the non-fiction book about elephants, which I do sometimes read non-fiction on my iPad. I read a terrifying book about mermaids.

**Speaker ?:** Yep.

**Chris Gammell:** You heard that right. Mermaids.

**Dave Jones:** That one's non-fiction?

**Chris Gammell:** No, that one was fiction.

**Dave Jones:** Can we really be sure?

**Chris Gammell:** I don't know. Although it went really strangely well with the jellyfish book that I was reading at the same time.

**Dave Jones:** Yeah. Right. You opted not to download the book about cannibals because I didn't want to hear about it.

**Chris Gammell:** You didn't let me read the book about cannibals for reasons I don't understand. Did you think that I was going to become a cannibal?

**Dave Jones:** No, I thought that you would provide me with cannibal facts, which I care not to hear. Right. Yeah.

**Chris Gammell:** Chris does often have to hear about whatever I'm reading about. I finished Cat's Eye, which is an Andre Norton book. She is a very famous science fiction author, but older science fiction, not current. And that was, sometimes the older science fiction, you just read it and you're like, wow, the world sure has changed. And this was not like that. This was very good. Yeah. I don't really know if I want to go on because it's sort of embarrassing. Yeah.

**Dave Jones:** If you ask Alicia what she's reading, we could do a whole podcast.

**Chris Gammell:** Yeah, it really could. Let's just say yesterday was a three novel day.

**Chris Gammell:** Wow. That is.

**Chris Gammell:** But I should be reading Tim O'Reilly's WTF, What's the Future book? Because he will be on our show soon. Yeah, I know. And, you know, I really was excited about this book because it's What's the Future? And I'm like, okay, let's talk about robotics and machine learning and cars and flying things and rockets. And there's so much future that's awesome. And for the first, like, 100 pages, it's all been about history. And I'm like, I don't care. Don't care. Just don't care.

**Dave Jones:** That's not even the future. That's the past. Right. Should be WTP.

**Chris Gammell:** Then we made a website. And I'm like, yeah, don't care. I was in college then. Yeah, don't care. So that's been a little tough, but I'm still looking forward to talking to him in a week or two.

**Chris Gammell:** That'll be good.

**Chris Gammell:** What are you reading?

**Chris Gammell:** I am chugging my way through the Isaacson Ben Franklin book. And yeah, it's great. It's going slower than I thought. The thing that really bugs me is, like, it's getting towards the end of his life and I'm only 55% through the book. So I'm just hoping there's a lot of footnotes at the end. I haven't looked ahead. I probably should, but we'll see what happens. And then I was real stuck on – so I went through five different books about learning. So Teach Beyond Your Reach, Mastery by George Leonard. That's a great book. That's actually by a kickboxing coach. He talks about, like, becoming a – he talks about loving the plateau. That's a great lesson. That's pretty much the summary of the book is to love the plateau. Learn to love the plateau. So, like, as you're learning, like, computer vision, you just need to, like, work on the practice. And then you make these, like, leaps and bounds forward by getting better at the practice. So that's how you learn hard things. Thinking fast and slow is –

**Chris Gammell:** But that's really hard.

**Chris Gammell:** Of course.

**Chris Gammell:** Well, I mean, sometimes that's, like, the opposite of the message of peak, which is you can't get better if you just keep doing the same thing. You have to find ways to work hard to get better. I guess his plateau is probably still working hard at it.

**Chris Gammell:** Yes, it is. And it's having a directed plan. So I used it a lot for, like, my piano practice, thinking about that stuff. Because, like – and so, like, what I did is I went to my teachers who were taking it way too easy on me. And I was like, look, no, I need a practice regimen. And that has been killer.

**Dave Jones:** Now, the hard thing – Getting music instructors to get you stuff like that is so hard.

**Chris Gammell:** Because they just listen. They're like, yeah, they'll be like, oh, whatever you want to do, you know, just play a song. It's like, no, no, no, I need a practice. And so that was great. I've been thinking – I have a list going of, like, what does it look like for an electronics practice, right? What is – but then that kind of balances against – with piano, it's like, oh, scales. I need to know scales. Okay, great. Like, with electronics, yeah, I need to know soldering. But, like, so maybe bold port is, like, a good prescription there for, like, soldering every day or not every day but, you know, on a regular basis. But, like, I have a list going of, like, what does electronics practice look like, you know? And then – so that has been a very useful book for just kind of thinking through those things. Another one is Understanding by Design. That's not very foreign because it's a – I got sold a PDF book on Kindle. What? How? Wait. I could have done that anywhere. Why did they do that? I can't read it on my Kindle. Or my – yeah, my – that's what it's called, right? The Kindle. Yeah, I couldn't read it on a Kindle because it's a PDF. Making Learning Whole. That's one that Mel, my friend Mel, suggested. And then How to Be Miserable, the 40 Strategies You Already Use. That's a self-help book like crazy. But that's actually from the CGP Grabe video if you haven't seen it. Oh.

**Chris Gammell:** He's got some really neat videos.

**Chris Gammell:** Oh, he's great. He has one about seven ways – it's based on that book, but Seven Ways to Be Miserable. It's, like, a summary of it. And it's so good. It's about depression too. So, it's, you know, basically, like, stay inside, don't exercise, you know, all the usual things. So, it's very tongue-in-cheek.

**Chris Gammell:** The one ways to maximize misery.

**Chris Gammell:** Yep. All right. That's the one. Yeah.

**Chris Gammell:** And then you started to say thinking fast and slow.

**Chris Gammell:** I don't – I am not a fan of this. Maybe I'm only 10% in. Oh, here we go. Here we go.

**Chris Gammell:** No, I can see not being a fan of it. It is a trudge.

**Chris Gammell:** Yeah. Does it get better after 10% in?

**Dave Jones:** What do you like about it? Maybe that's about – 10% is only 1,000 pages, right?

**Speaker ?:** Yeah.

**Chris Gammell:** So, having heard you, I think you like to know how to use something before you want to be bothered whether to dig into why it's important.

**Chris Gammell:** Correct. Yes. I'm very – I'm engineer, not scientist, right? So, like, I don't want to know the basis of all the universe. I want to know how do I use the universe to my advantage.

**Chris Gammell:** So, go to the first page of each chapter and then take a page back. At the end of each chapter, he tells you how to implement all of the things he's – or he gives you high-level implementation on the things in that chapter. I like that. It's got really good stuff. If you read the whole thing, of course, these other things are going to make more sense and they're going to stick a little better. But if you're the sort of person who wants the action before you want the understanding, then do that.

**Chris Gammell:** It's like context or something, huh?

**Chris Gammell:** Yeah. Yeah.

**Chris Gammell:** No, that's great. Yeah. That's really good advice. I like that a lot, actually. So, okay. I have to – okay. I will be a little bit of a fanboy of my own company. They have, like, the – which we copied totally from Buffer, but it's the best perk ever. Any Kindle book I want, I can just buy. Wow. A company will pay for it. Personal or professional. It is – What? So, it's copied from Buffer.

**Chris Gammell:** Can I work there?

**Dave Jones:** Alicia can never work there.

**Chris Gammell:** Can I work there just for the benefits?

**Dave Jones:** She will bankrupt your company. I know. Right.

**Chris Gammell:** And you don't even have to just – I mean, because I buy almost all of my books from Kindle daily deals. I almost never –

**Dave Jones:** We will still bankrupt the company.

**Chris Gammell:** Yeah. That's awesome. That is awesome. Yeah. It's a great – that is the best perk I've ever heard of, too. Like, because it's just so out – like, oh, I don't have – like, I told my family for Christmas, I was like, sorry. You know, you can't – like, I always ask for books, right? It's just a thing I've done since I was zero. Well, I didn't ask. But, you know, like, it's just always been a thing when I – holidays and stuff like that whenever someone's giving me a gift. But now it's not really a thing. So. So, yeah.

**Chris Gammell:** Do – is this off of your Amazon account? Or do they keep the books?

**Chris Gammell:** Yeah, that is how they – no, no, that's how they do it. So, it's my account. It's just a reimburse thing.

**Chris Gammell:** But it's just a mental thing. It's so weird, right? It is just a mental thing.

**Chris Gammell:** Because it's like you see a $30 Kindle book. You're like, oh, $30.

**Dave Jones:** But now it's like – I have no problem with that. I want to learn that thing. If I want a book, I'm just going to buy it. I don't care how much it costs.

**Chris Gammell:** I was so excited when Chris finished the book he was reading and saw that Artemis was out by the year. Oh, yeah.

**Chris Gammell:** Yeah, yeah.

**Chris Gammell:** Because there was no way I was going to buy it at full price. And he just pushes the button. Now I have it and I can read it. As soon as I finish the other 50 books, I will totally be on it.

**Chris Gammell:** Do you two share? Yeah. Yeah. A Kindle account too? Okay. Yeah. So, that means Chris sees what you buy on daily deals each day? Yeah.

**Dave Jones:** I don't like the deals. And I get the ads that are definitely targeted to her because she probably reads 10 times as much as I do.

**Chris Gammell:** Maybe you'll like sea anemones. Yeah, that's not what I get.

**Chris Gammell:** Yeah, I do read romances sometimes. Oh, okay. And if you are the sort of person who even reads like one romance out of 10 books, they mark it heavily because most romance readers read a lot. Yeah.

**Dave Jones:** So, my Kindle usually has some bare-chested dude staring from the front of it. Got it. It's fine.

**Chris Gammell:** No, the fact that I also read mysteries and sci-fi and nonfiction, they don't care. It's all about the romance novels.

**Chris Gammell:** Right, right, right. It's where the money comes in. Wait until that video ad comes in the mail. Right? You open up the little video portfolio thing and it's Fabio. Okay, well, I think we should end on Fabio. What do you think?

**Chris Gammell:** Let me just write that down as a title.

**Chris Gammell:** Jesus. Yeah, right. I would like to actually have a Star Wars spoiler discussion in the outro. Is that okay with you? Okay.

**Chris Gammell:** Yeah, that's fine. So, okay. So, now I was just saying thank you all for listening. Thank you to Christopher for producing, co-hosting. Thank you to Chris Gammell for being our guest or for being a host on his show. We don't know.

**Chris Gammell:** If you heard any ads in this thing and you didn't hear them here, you know, we didn't put them there. We didn't.

**Chris Gammell:** No ads. No ads. We still have a Patreon. Everybody has a Patreon.

**Dave Jones:** The Empire has a Patreon.

**Chris Gammell:** You don't get anything from being supporters, but we do love you slightly more.

**Dave Jones:** We love you. Yeah. Yeah. They're the best. Have a good year.

**Chris Gammell:** Happy New Year. Yeah. Happy New Year. 2018. 2018. I think it'll be a good one.

**Speaker ?:** I think so, too. Bye. Bye. Okay.

**Chris Gammell:** Spoilers. Spoilers. Spoilers. Wait a minute. Do you have... You were going to hook up one of the synths so that you...

**Dave Jones:** Nah, it was too far.

**Chris Gammell:** Oh, man. Do you need... You could have played us into, like, Spoilerland with Star Trek sounds.

**Chris Gammell:** Oh, we could... Star Trek sounds? You know, if you want to come up with a sound... Oh, my God. We did it again. You could make a custom... It's annoying. You could make it a custom Ampedded theme if you wanted. You could intro your music like that. How much time do I have?

**Dave Jones:** Amped power, embedded, and the Emperor's March. No. Don't give me ideas like that, because that's not actually practical.

**Chris Gammell:** No, I mean, like, you don't need to... You don't need to remix any of our stuff. I mean, like... Yeah, no. Use your Blippi stuff and just make, like, it custom. That would be great. All right. It could be super simple, too.

**Dave Jones:** I will... I will endeavor to do that... Write us original music. ...in the next 48 hours.

**Chris Gammell:** Right, right.

**Dave Jones:** That's right.

**Chris Gammell:** Okay, so here is... Did you like the Star Wars movie?

**Dave Jones:** I loved it. Oh, my God. Of course I loved it. Oh, good. Because we know people who didn't. And they just... You know, whatever. Yeah.

**Chris Gammell:** What a bunch of... Yeah. Here's my thing. Did you see BB-8 with the carbon resistors? What was up with that? I loved that. It's always with the resistors. You know, I have the same thing in... You know, I love Andy Weir, but like the whole, like, power drill thing, where he's like, oh, you just do like a resisted divider. Like, that's literally my only argument, or my only point against the entire Martian book is just the resisted divider in the power drill thing.

**Dave Jones:** You know why they do that, though? It's like the one component that at least a fair number of people know, oh, that's some sort of... I know. Oh, resistor. Right. Right. Right.

**Chris Gammell:** Did you notice how Chewy stocked up the Millennium Falcon before he went to go save the refugees? It was good that he put all those porgs in, because they were going to be delicious.

**Chris Gammell:** Is this like the, did Chewy actually eat porgs discussion? I've read about that. Chewy's still the best. I don't either. She thinks he stocked it with snacks. Yeah. That's why there were so many in there. I think so, too. I mean, like, they were talking about, it was like, they were nesting in there, but yeah.

**Chris Gammell:** Yeah, sure. Self-regenerating snacks.

**Chris Gammell:** Yeah, right. Snacks on snacks. Yeah. So, that's really all. I was just, I was very dismayed that, like, why resistors? I don't get it. Why not just make it look like future-y panel?

**Dave Jones:** They were sort of, they were sort of not, I mean, they didn't look exactly like resistors. They were resistors. They were a little different.

**Chris Gammell:** They were, they were, they were carbon film resistors. They were big. Or not even, they were like wire-wound resistors. Like, they were like, yeah.

**Dave Jones:** They were space resistors. Space resistors.

**Chris Gammell:** Porgs are secretly puffins. Yeah, right.

**Chris Gammell:** With cuter faces. Well, maybe not. Yeah, no, I loved, I loved it, though. So, I guess that's all I have to say.

**Dave Jones:** That's not how you fix electronics. You don't just stick metal bits.

**Chris Gammell:** Stick your head against it. Yeah. So, it works.

**Chris Gammell:** That's how I fix it. It must be why it never works.

**Chris Gammell:** Yeah, right. Right, right. Like, they were doing it like, it was like a, like a, like a slapstick, like putting your finger in the, in the leaky, you know, leaky wall kind of thing. Yeah.

**Chris Gammell:** Wait a minute. I get it, but like. Isn't, aren't electronics just like water?

**Chris Gammell:** I mean, that's what the analogy is. That's true. That's a good point. Yeah. I didn't think about that. Uh, yeah. Yeah. Well. Okay. I guess I'll stop recording now. All right. Looks like my computer's slowing down. It's a good sign. Uh.

**Speaker ?:** Uh. Thank you.
