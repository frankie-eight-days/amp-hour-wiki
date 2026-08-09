---
episode: 636
title: Discovering Cursed Connectors
url: https://theamphour.com/636-discovering-cursed-connectors/
---

**Intro Voice:** This is The Amp Hour Podcast. Released June 19th, 2023. Episode 636. Discovering Cursed Connectors.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. Welcome to the Chip Mystery Hour, whereupon Dave and Chris look at a photo of a board and we're like, what? We're doing a live teardown.

**Dave Jones:** Live teardown, folks.

**Chris Gammell:** Someone else. So Dave and I were commenting that we like the Rode. What is it? The Go 2, right?

**Dave Jones:** The Go 2. Because what you're actually hearing from me right now is the new Rode Podcaster USB mic. Yes, that's right. Which I've done a second channel video on. And then we got to Chris and was talking about the Go mic.

**Chris Gammell:** I actually don't have the Go 2, but I've watched and drooled over them from all the video channels that I review, which is a very dangerous hobby, by the way. Don't watch video.

**Dave Jones:** Yeah, yeah, of course.

**Chris Gammell:** Gear review channels will make you spend money. You don't need to.

**Dave Jones:** You end up buying microphones and cameras and lights.

**Chris Gammell:** Dave actually needs that stuff. I just watch videos of people that talk about these things. No. But it's a really cool product. It's got local recording. Is it 32-bit on there or is it just 24-bit?

**Dave Jones:** Oh, couldn't tell you. But anyway, does it matter? Like, do you need, like, in a wireless mic, do you need 32-bit or 24-bit audio?

**Chris Gammell:** The reason to do, again, because I watch other videos.

**Dave Jones:** As in a dynamic range thing, right? That's right.

**Chris Gammell:** So, like, if you're peaking or if you're really low, some of these modern recorders do 32-bit to have a dynamic range. Yeah.

**Dave Jones:** Yes.

**Chris Gammell:** Anyways, these are meant to be, like, you'll see these in a lot. If you pay attention in, like, interview videos often or, like, YouTubers that you watch, you'll see these little black plastic things clipped onto people's shirts, including Dave. And they're great. They work on their own. They have lapel mic inputs. They're really cool little devices. And so Dave and I were wondering, like, oh, what's inside of it? And I found this photo, which I will link in.

**Dave Jones:** For those who are wondering why I haven't torn it down yet is because they're actually glued together. So you've got to, like, get the heat gun and kind of, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** So, yep.

**Chris Gammell:** Yeah. So we were just looking. We found some photos online of just PCBs. Also, this is the two. Yeah. So this is the Rode Wireless Go 2. Two, which is different. I think there's even different versions of that.

**Dave Jones:** Yeah. The difference between the first version, which I had, I've now got the Wireless Go 2 I actually upgraded is the first one was only one transmitter. So you only had a single mic and a single receiver. But the new Go 2 has two. So if you're interviewing someone, perfect. You put one on you. You put one on your guest. And the other cool thing about it is that it's actually built-in recording as well. I think it's up to eight or 12 hours actual recording internally. So you have that as a backup just in case your Wireless Link went down or you had the wrong settings on the camera or something like that. You can actually pull the audio directly off the actual recorded thing. That was good.

**Chris Gammell:** It's not a person. Because people who do audio and video have been burned enough times. And in fact, I'm actually recording locally now because I don't trust our current setup. So I have a local recorder running, as you do.

**Dave Jones:** Well, actually, that reminds me. I should turn it on now. I should record as well.

**Chris Gammell:** Yeah. I recorded another one last night and I had our guest on two records. It's just, you know, you start to get really, really touching, you know. No, it's great.

**Dave Jones:** I love this thing because I have it in my little portable kit, my little portable camera kit that I take out. And you just whack it on people. I was at the ham radio thing with Dick Smith the other month, right? Yeah, and I was just like this little clip. Like I didn't have to worry about like a cable and a belt pack and stuff like that. So as I was filming people who were talking, you know, so we'll go and hand in the mic from one person to the next. And it was just so easy. All you got to do is whack it straight on their collar.

**Chris Gammell:** And if people start looking, if you start looking, you're going to see this in YouTube videos everywhere. Because it really is taking over. Because it's like instead of like, you know, like a full battery pack, like the traditional lapel mics, like you might see like on stage where they need to have this huge battery. This thing is now just like tiny and you got to charge a lot more. But I think you get like five, six hours out of it.

**Speaker ?:** Yep.

**Dave Jones:** No, it's great. Yeah, I think it's eight hour battery life or something like that. Yeah, I've never run out of battery on it. So it's really low power stuff.

**Chris Gammell:** So Dave and I were looking at this board. And we're like kind of just looking up parts that are on here. You know, the ones that you could tell from the, you know, the big chips you look at first. And there's a big dialogue part on board, which I was just looking at is the headphone amp. Then there's two other big chips.

**Dave Jones:** Is that just the headphone amp or is that the, I haven't looked up that part yet. Oh, really?

**Chris Gammell:** Yeah, I think so.

**Dave Jones:** The biggest part on the board is the headphone amp.

**Chris Gammell:** Oh, sorry. Oh, wait a second, Dave. Oh, wow. This is interesting. Oh, no, coprocessor for Bluetooth. I thought we were going to have a third chip. I'm already kind of giving away the game here. It says single coprocessor platform. It's a smart beat.

**Dave Jones:** It's a smart beat. Anyway, this is the dialogue semiconductor part. It's the DA14195 low power peripheral audio solution. Immerse yourself in audio. It offers USB, Bluetooth, analog, and use cases.

**Chris Gammell:** It's a full microcontroller too. It's got codecs. It's got a whole Cortex M4 on it, M0 on it. So it's like, it's a whole other system.

**Dave Jones:** Yeah, supports 192 kilohertz, 32 bit PCM. Oh, beamforming.

**Chris Gammell:** Six mics for beamforming. Oh, interesting.

**Dave Jones:** Oh, really?

**Chris Gammell:** Wow. Okay.

**Dave Jones:** Well, I'm pretty sure it's only got a single mic in this thing. It's not like a multi-mic array, I don't think. Right.

**Chris Gammell:** So then, you know, following along, there's a huge F antenna on the one corner of the board where the QR code is. And again, we'll post photos here. Then it goes into an amplifier. That's pretty obvious. Like basically a front-end booster for that and maybe some antenna switching. And then there's a chip next to it. So I'm like, oh, that's got to be the Bluetooth chip, right? This thing's Bluetooth. We knew that. Yep. And I look at it and I'm like, okay, these numbers, it says NS2810. And I'm like, wait, NS? No, it actually just, I was reading it wrong. It's N52810. So I'm like, oh, I know. This is NRF52. Bingo. Like that's the low cost NRF52 part family. So that's doing all the Bluetooth processing. Yep. Why don't you take it from here, Dave?

**Dave Jones:** And, well, I've got to pull up the data sheet. Here we go. Right. And so you think, okay, this is, right, of course it's going to use a Nordic semiconductor, right? Because they're like the leaders, aren't they? Very popular these days. They're hugely popular. They have been for a long time, right? And it's got a Cortex M4 processor in there, right? And, you know, it's low power. It can run at 32 microamps per meg. You know, if you actually run from RAM, it's a bit higher. If you run from flash, ooh, an extra two microamps per megahertz. If you run it from flash instead of RAM. But, you know, that could make all the difference. Anyway, it works down to 1.7 volts. Really good, right? It's got Bluetooth built in. So, right, it's pretty much all you need. So all you need is to do this Wireless Go mic is this chip plus a front-end audio ADC DAC, right? Codec type of thing. Codec type thing. Yeah. Right? So that's it, right? So what's the last chip on board? Why do we have another chip? In fact, sorry, you mentioned headphone before. It does not have a headphone jack on it. It's just purely a microphone and a transmitter. Oh, that's a microphone input. Oh, okay. Yes.

**Chris Gammell:** Yeah, got it.

**Dave Jones:** Yeah. Oh, sorry. We are looking at – no. Are we looking at – no, we're looking at the receiver. Sorry. So the receiver does have – It has an output driver so you can go into a –

**Chris Gammell:** Yeah, because that's the other thing. So this is the receiver. So this has – so the faraway person has a transmitter basically. We're looking at the receiver. And then that does have a headphone jack, quote unquote, output. But that's actually – It does have a – That's line level that goes into a camera.

**Dave Jones:** It's line level out which goes to your camera. Yeah. Yeah.

**Chris Gammell:** So that's what the dialogue part's doing. Right. Yeah. So then there's one final one on there, which I thought was kind of – you know, like your brain starts to do this pattern matching stuff. And I'm like, oh, something 2833. And there's another NRF part called the 52833. But this is not that. I thought this might be like a repackaged thing. It's ATS2833. And sometimes tricky chip companies use S's instead of 5. So it could be that this was the S2833 or the 52833. And this thing actually, it turns out, looks like it's the brains of the operation to me.

**Dave Jones:** Well, it could be, yes. So they may not be using that Nordic semiconductor part to do anything else but the Bluetooth receiving.

**Chris Gammell:** Yeah.

**Dave Jones:** So this thing's got – Like it even works – it just works perfectly because they have lots of error correcting built in and everything else. It's really rock solid. You want a rock solid audio, professional audio solution. So I reckon that's what the Nordic is doing. I reckon the Nordic is actually using its 32-bit processor. But it's not doing the processing. It's probably not driving the screen and all that sort of stuff. Right. It's just doing audio transmit error correction and stuff like that. Right.

**Chris Gammell:** Well, the thing that was confusing to us when we were looking at this at the beginning was the fact that this ATS2833 is from SmartCore. It's never heard of them. Yeah, they're a Chinese company. But it's listed as a Bluetooth chip as well.

**Dave Jones:** Yeah, this is basically the same as the Nordic part. But we don't see any antenna. It looks like it's a ripoff. It's got Bluetooth built in, right?

**Chris Gammell:** Yeah, right. It looks like this is a ripoff. This looks like a much beefier version on the NRF52833.

**Dave Jones:** And it's actually a Bluetooth audio solution. It's a highly integrated single-chip Bluetooth audio solution. So in theory, all you need for this is just this one ATS2833 SmartCore chip.

**Speaker ?:** Yeah.

**Dave Jones:** You don't need the Nordic. You don't need anything else except the codec, except the analog to digital.

**Chris Gammell:** Well, that was another thing I was thinking too is that what if this is maybe a cost down for later, right? So you move the antenna over later and you test, you know, like you didn't get to testing this at the first point. But then maybe as you have more, for more resources and more time on this thing, then it's like later you're like, oh, yeah, I could use this for Bluetooth as well.

**Dave Jones:** Right. And it does noise reduction, wind noise reduction, echo cancellation. You know, it does a ton of stuff. Build in, it's got bass enhancement, it's got virtual surround effects. It does cryptography as well. So you can encrypt your transmit solution.

**Chris Gammell:** Yeah.

**Dave Jones:** Whoa.

**Chris Gammell:** Yeah, I think it's probably likely if you're, so you're not getting crosstalk as well.

**Dave Jones:** Yeah, you're not getting crosstalk with another. Well, that's probably what they're doing, right? Because you've got two transmitters. Right. This comes standard with two transmitters and they're just randomly coded with a unique ID so that no two transmitters are using the same encryption, I guess. So to speak. Maybe. Yeah. Yeah. Yeah. So I think that's what this. Oh, wow. It's just, yeah. Basically, there are two complete Bluetooth solution chips on here. And it's like, well, why?

**Chris Gammell:** But yeah. Yeah, it was confusing. Yeah. Very confusing. Also, I'd like to call out, this sounds like something. This one has a book. No, before we go, come on, man. I got something good here. I got something good here. This sounds like a Dave thing. I've never seen this on a data sheet before or a product page before. Typical sniff current.

**Dave Jones:** Oh, where's this?

**Chris Gammell:** This is under power management. Typical sniff current. 600 microamps.

**Dave Jones:** For which chip here?

**Chris Gammell:** Oh, for the SmartCores one.

**Dave Jones:** Oh, the SmartCores. I don't have the data sheet. I've just got like a web page. Yeah. I don't actually have the PDF. No, no. It's the product page. Oh, there it is. Typical sniff current. Yes.

**Chris Gammell:** I've never seen sniff current. That sounds like a Dave term.

**Dave Jones:** Sniff current. It sounds like a chinglish. Yeah. Typical sniff current. That's great. Yeah. That's great. Oh, wow. Yeah. Anyway, that's, yeah, this actually has a built-in 24-bit Delta Sigma DAC. So, it's actually got the DAC, which is driving the line out.

**Chris Gammell:** I think this is driving the line out. Okay. Yeah.

**Dave Jones:** Yeah. Yeah. So, this one does. So, what does the other chip do? What does the dialogue do then?

**Chris Gammell:** I don't know. It doesn't make sense. I mean, like geographically, the dialogue is much further from the headphone jack or the line out jack.

**Dave Jones:** So, we've got three, no less than three, 32-bit arm cortex processors that can all do this.

**Speaker ?:** What?

**Chris Gammell:** An abundance of processing power. What? Yeah.

**Dave Jones:** I, like, this is probably an example of where they've simply, like, thrown an arm cortex, a 32-bit arm cortex at every little module they can.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Like, just because they can. I mean, they're in Australia.

**Chris Gammell:** Just go knock on their door, Dave. Just go and ask them about what's going on here. Yeah.

**Dave Jones:** Well, I can.

**Chris Gammell:** Yeah.

**Dave Jones:** Yes.

**Chris Gammell:** Yeah.

**Dave Jones:** Like, obviously, they're not going to give us out their trade secrets, but they haven't. Like, it isn't like they potted this thing, right? You can just open it up and you can see it, but my goodness.

**Chris Gammell:** There's definitely going to be awesome rands as well because this is a popular product. So, there's going to be other things like this. Yeah. Yeah.

**Dave Jones:** What? Other products? Is there?

**Chris Gammell:** I like other knockoffs and stuff.

**Dave Jones:** I've never seen a competing product to the Rode Go mic.

**Chris Gammell:** Oh, nothing that's popular yet. I don't know. Leave it in the comments. Yeah. Yeah.

**Dave Jones:** But I've, yeah, Rode own this market of this little portable clip-on transmitter and receiver with built-in recording now with the second model. And it's just, oh. Anyway, yeah, where are they storing? Where's all the memory? Is it on the other side of the board?

**Chris Gammell:** There's nothing on the other side of the board. There's a photo.

**Dave Jones:** You remember I mentioned this thing has like all this recording, right? So, maybe that's what they're using.

**Chris Gammell:** One-sided board.

**Dave Jones:** It's only single-sided load, is it?

**Chris Gammell:** Yeah, that's right.

**Dave Jones:** Okay. Wow.

**Chris Gammell:** Yeah.

**Dave Jones:** Okay. So, which one has the most memory? Because that will be the one where they're storing during the audio recording.

**Speaker ?:** Yeah.

**Chris Gammell:** I think the ATS-2833.

**Dave Jones:** Okay. 192K of flash for the Nordic.

**Chris Gammell:** So, wait a second. I thought this thing, so this thing is Bluetooth. I thought the, I thought the transceivers, sorry, I thought the, the transmitters or the things that are on the people far away, I thought they talked to the receiver and then the receiver could talk to a phone or a thing. Because there's another thing that looks like an antenna on here too. If you look on the zoomed out photo, I know that we're killing people here that aren't listening. If you look at the back photo, right? And you see there's like a small flex cable. That looks like it's like a low frequency receiver there.

**Dave Jones:** Oh, I'm not. Oh, okay. Yes. Right. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. It's got a, yes, it's a corner and it's got RF on it. Yep. Okay. Yes.

**Chris Gammell:** Yeah.

**Dave Jones:** So is it, maybe it's a, well, is it some sort of dual diversity thing or is it, you think? No, I don't think, no. Cause the transmitter is just that.

**Chris Gammell:** How the things work. I thought, I thought the transmitters, the things that are on the people that are far away, I thought they just talked back to the receiver. I didn't think everything talked to like a phone. I thought it was like, everything talks to the receiver and the receiver talks to a phone.

**Dave Jones:** As far as I know, you can't use these with your phone. If you want to program the, if you want to program them, you have to plug it in via the USB as far as I'm aware.

**Chris Gammell:** Huh? So what the heck is that?

**Dave Jones:** Because you have an app on your battery and that, and you plug it into the USB and then it talks to it and you can set up, you know, you can set up the input gain and stuff like that. Right. And you can set up other stuff. Um, how it actually records, does it record to a wave file or whatever, you know? Um, Dave, I'm stumped. As far as I know, the receiver would not transmit back to the transmitters. As far as I know, it's only one way.

**Chris Gammell:** Oh no. Yeah. I didn't mean that way. I meant to a phone. I, so I thought, I thought the, this is kind of confusing too. I thought the person out so far away from the camera was transmitting to the thing on top of the camera, the receiver, and then the receiver could also transmit to a phone. That's what I thought was working. Maybe I just remember.

**Dave Jones:** Maybe it is. I've never used it in that regard. You don't like it like that. I've only ever used it as a line out, um, thing, which goes to my camera. But yep. Maybe that's actually.

**Chris Gammell:** On the wireless go product page, series two, uh, series four, 2.4 gigahertz digital transmission, 128 bit encryption. There you go. There you go. So it does, right? Yes. Yes.

**Dave Jones:** It does the encryption. Yeah.

**Chris Gammell:** Okay. Onboard recording. Option record channels separately. 200 meters line aside. Yep. Yep. Yep. Yep.

**Dave Jones:** So we were, we were right about that each when it comes out of the factory, because you don't set up channels on these things, right? There's no ability to do that. So each one comes factory program with its own unique in encryption out of the box. So in theory, you know, 128 bits you're won't ever find. You'd be pretty unlucky to find another, um, you know, uh, transmitter that had the same code as yours. So, yeah.

**Chris Gammell:** Uh, wow. Yeah. And they're not using, it's not Bluetooth either then. That means they're just using the 2.4 gigahertz radio. Did they not say Bluetooth on here? Let's see. Control F. Bluetooth.

**Dave Jones:** It doesn't say anything about USB out to a phone.

**Chris Gammell:** It says USB-C.

**Dave Jones:** Yeah. USB. Yeah. That's, that's how you set it up. Oh, so maybe it, maybe it does actually work as a USB-C, but that doesn't explain that second antenna. You're right.

**Chris Gammell:** Yeah. Yeah. We're not, we're not, we're not getting it, Dave.

**Dave Jones:** If we just spent half an hour analyzing this before we actually started the show, you know, we would, we would have come up with.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Yeah. Yeah. As far as I'm aware.

**Chris Gammell:** I want to see the tear down of the transmitter now though too. I feel like it would be like. Right. Like a down sampled version. Maybe it's like a less populated version of the same board. That would be smart, but maybe it's not.

**Dave Jones:** Hmm.

**Chris Gammell:** You know, what's really bad is if, um, if some of the engineers are listening right now. Right. Yeah. I know. They're just, yeah. They're just tearing their hair out. Yeah. Yeah. Yeah. There's, there's a solution. Come and tell us all your secrets and we'll be fine.

**Dave Jones:** But, but to have three, um, Cortex 32 bit processes.

**Chris Gammell:** I mean, y'all use a lot of microcontroller power.

**Dave Jones:** They're just throwing it around, but I can understand differentiating them between two because one of them, as I said, has to be dedicated to, well, one of them's got to drive the screen and do the user interface, right? Sure. So it's got to do the screen live updating. And then it's also got to do, one of them's got to do the actual, uh, real time recording as well. Right. Cause it actually records. It's got to record both channels, both receivers at the same time and record it to a wave file continuously.

**Chris Gammell:** Um, and I bet the, uh, do you see the small push button, not by the battery, but the other side by the headphone, by the output track? I think, I think that might be the flash. It's an eight pin, maybe like a spy flash.

**Dave Jones:** Oh, okay. You think it's a serial job.

**Chris Gammell:** Oh, or GD, the GD L S C eight. Oh yeah. Yeah. I see that. Yeah. That, that, that. It's just so small these days. It's like, I always expect to see like flash to be big, but it, you know, Silicon's always the same.

**Dave Jones:** Especially memory is just, you know. Yeah. Yeah. Yeah. So they could have a serial. Yeah. Could have a serial flash.

**Chris Gammell:** Yeah. I do enjoy macro shots like this. This is nice. Yeah. It's great. Nice job. Submitter. Possibilis.

**Dave Jones:** Single side load too matters. Yeah. Um, you know, it's, it, it still matters. Absolutely.

**Chris Gammell:** Oh, for like cost and.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. Just cost simplicity at the production stage because they're made here in Australia.

**Chris Gammell:** You know, yeah. They're made here in Australia. Maybe they only have like a hot plate.

**Speaker ?:** Yeah.

**Dave Jones:** Right. Yeah. Right. Right. You think they just have some amateur set up.

**Chris Gammell:** Yeah. Right. Yeah. Just a lot of hot plates.

**Dave Jones:** You know, I would love to know what volume they do these in. Cause it's, it's pretty much, as we said, it's like the de facto standard wireless mic for video, for, you know, people to making YouTube videos and whatnot. Yeah. These days, it's just, everyone's got one. Cause it's so great.

**Chris Gammell:** Maker, Maker Moco. I think that's who it is. Yeah. Maker Moco.

**Dave Jones:** But it's more than the hardware. All this, all, all the magic's in the software. Right. Yes. Yes. And, and, and in fact, I mentioned this the other day, I probably mentioned in my video too, Rode have one of the best, this is not sponsored by Rode, by the way. They just do cool. They just make cool stuff. Right. And, and they happen to be Australian too. So, you know, there's that. Yeah. And, and my mate Doug Ford, if you haven't seen it, he used to be the head designer at Rode mics back, back then when they only did microphones and now they do, you know, more than a heck of a lot more than that. So, well, I guess this is a microphone solution. It's just a wireless solution, but they do a ton. Yeah.

**Chris Gammell:** I mean, you mean like he did analog, Michael, he did like traditional, traditional analog mics.

**Dave Jones:** Yep. Yeah. Anyway. So.

**Chris Gammell:** Did you, did you miss what I was saying before? Have you ever seen Maker Moco? I hope I'm saying it right.

**Dave Jones:** No. What's a Maker Moco?

**Chris Gammell:** Is it a YouTuber? A thing? Oh, okay. Yes. It's a YouTuber. But he has a setup where like, it's got this, we were talking about, I mentioned hot plates, but it's like a, it looks like a, it's like a lead screw kind of thing. And the whole thing like, like kind of settles down onto a hot plate. I don't know how to explain it. If you go to like his most recent video, I'll link it to you. You can watch it. See if I can find the thing, but it's like a hot, hot, hot plate. A hot plate assembly. It's super cool to watch. I mean, it does great videos in general too, but. All right. Cool. Yeah. I'd like to get something like that, but you know, like, I don't know. I'm not doing a lot of. You don't.

**Dave Jones:** You don't do enough to warrant it. Yeah, exactly. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** No.

**Chris Gammell:** But I love watching his videos. As I'm like, it's really great. It is. It's like, basically if you have that kind of setup too, like it's a reason to go and design like that, you know.

**Dave Jones:** The pick and place thing is still not happened for me. That one I was really interested in that was available in Canberra. It, and the guy actually had it up for sale and then I wanted it and then he took it down. He decided to keep it. Well, it's come up for sale again and nobody wants it. It's like, I think I can practically get it for free at this stage. There you go. And, but it's like this obscure brand, which nobody uses and it's just buying trouble. Right. And it's not. And if I make videos on it, I'm not helping anyone because nobody would use this thing. So it's, so the videos, you know, I'm better at like, if I'm going to make videos showing you how to use a pick and place machine, I'm better off just getting one that at least you can buy. You know? Yeah.

**Chris Gammell:** It makes me wonder how many are on the continent though, too. You know, like in terms of like traditional, I guess not traditional, but like, you know,

**Speaker ?:** like common one.

**Chris Gammell:** There's another one that came up.

**Dave Jones:** It's a Yamaha or whatever, but I don't have the space for that. Like I've got to have a big roller door to bring the thing in and three phase power and, you know.

**Chris Gammell:** I'm not sure it's that useful though, either. Like if you get like a high end one that other people aren't going to get, like nobody, if you go and make a bunch of videos about that, nobody's doing that. You know what I mean? Nobody's doing that. It's almost better if you did like a low end one and how to optimize it for.

**Dave Jones:** Exactly. Either an open pick and place or a, you know, or something else. Or one of the new YY1 from Neoden or whatever, you know. So, yeah. Yeah, I know. It's just, it's just all too hard. And then my, I thought, you know, look, I, for my new product that I'm working on at the moment, I can, you know, I can get a pick and place machine for that and start manufacturing myself. And then I realized, well, this new product's actually not going to have that much on it. It's got like one, one, one chip and a few miscellaneous parts.

**Chris Gammell:** It's the artisanal resistor. Artisanal resistor.

**Dave Jones:** The artisanal resistors.

**Chris Gammell:** Hand wound by Dave.

**Dave Jones:** Like it's so simple. I'm actually thinking of selling it as a kit, you know, like as, as in just make it yourself because it's so easy to.

**Chris Gammell:** If you sell it as a kit, I forget who told me about this. Someone who sold as a kit, they said like, you have to like put a thing in there about solder. Like if you, if people like get it, they don't know how to solder. It's like, I have sold kits before.

**Dave Jones:** I trust me. I know. I know what the deal is. Yes.

**Chris Gammell:** I've had stuff.

**Dave Jones:** Turn. This is before the days of the internet that post it back to me with extensive letters and I've checked every single component on this. I've triple checked every single component. Your design is bad. And then I take one. I stare at the board for two seconds and I go, your regulators in backwards, dude. Yeah. You know, like it's just, yeah. Yeah. Like no wonder it doesn't work. Yep. Yep. Yep.

**Chris Gammell:** Hey, so I sent you that video of the, at the timestamp. You can go watch that if you want to, if you want to discuss, if not, no big deal. Great channel though. Highly recommend it. I will link it in the output and output thing as well.

**Dave Jones:** Oh, it lowers on a bunch of grub screws.

**Chris Gammell:** Yeah. Isn't that great? Yeah. Yeah. It's like, like, like, like Z, what are they called? Uh, ball screws. You call them ball.

**Dave Jones:** Yeah. Yeah. Yeah. Ball screws or whatever. Yeah. They're called.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** So there's two. So it comes.

**Chris Gammell:** Yeah. It looks like a custom thing, right?

**Dave Jones:** Yeah. It's like a custom hot plate. And then it lowers the board. The whole idea of the two, uh, worms on the side.

**Chris Gammell:** I think that's why.

**Dave Jones:** Right. Yes. Yeah. So you can leave the element on and then it lowers the board down onto the hot plate, leaves it there until it does it. And then, you know, leave it there for X number of seconds.

**Chris Gammell:** It's on its own plate. So it's like a separate plate. And then there's the element below it. And then the plate. And then it lists it back up.

**Dave Jones:** Then it automatically lists the board back up.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** That's actually. Yeah.

**Chris Gammell:** It's pretty, pretty clever. Yeah.

**Dave Jones:** It's not bad. I don't mind that at all. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Because otherwise. Yeah.

**Chris Gammell:** I tried to contact Maker Mocha before. Right. If anyone knows, if anyone knows this person, I'd love to talk to them, but no, no responses. So.

**Dave Jones:** So this is the hot plate equivalent of a conveyor oven.

**Chris Gammell:** Yeah. Yeah. It's like an automated hot plate. Yeah. Versus like, yeah. Yeah.

**Dave Jones:** Yeah. Because if you don't know how a normal reflow machine works, it's a conveyor belt. Your board comes out of your pick and place machine. It goes on the conveyor belt and then it goes through the oven, which usually has five different stages of heating. But anyway, it goes through and then it comes out the other end. And then it's, you know, super hot when it comes out, but it's all timed perfectly so that it's, you know, whereas you can't do that with the hot plate. You've got to physically put it on the hot plate and you've got to physically take it off. So this is a way to do that.

**Chris Gammell:** Yeah.

**Dave Jones:** But just in an automated way by lowering it down on these, you know, on this plate that comes down to a tetan to hook onto the hot plate.

**Chris Gammell:** That's really cool.

**Dave Jones:** Anyway.

**Chris Gammell:** It's very clever.

**Dave Jones:** Yeah. I like it. Anyway, he's doing this little robot. This is really cool. Yep.

**Chris Gammell:** Yeah. Make a moco. Yeah. Awesome. Yeah. They did a GPS Laura tracker thing in the past as well. Just like really great. Yeah. High quality videos and very in-depth ESP32 designs. So I'm very impressed.

**Dave Jones:** Yeah. That is very impressive. Yep.

**Speaker ?:** Yeah.

**Dave Jones:** It's a PCB robot. Basically. It's a, you know, the motors are on the board and yep. Yep. Yep. It attaches to these. Well, what are these multi-axis wheels? The wheels that can like go in any direction? Omni wheels.

**Chris Gammell:** James Bruton uses those in a bunch of products too. Right. Yeah. Yeah. Yeah.

**Dave Jones:** Very cool. Anyway, I like that. That is awesome.

**Chris Gammell:** That's great. Dave, I'd like to discuss my sins and what I may have made sins.

**Dave Jones:** What have you done this time?

**Chris Gammell:** I know. I know. Okay. Here is a question. Is it bad of me? I'm making a one or two of design, you know, just like a one-off. Right. Yeah. I went on Amazon and I'm like, I have three conductors. I need to, I basically, I needed to make like a panel pass through and I was like, I have three conductors. Show me what you got, Amazon. And I was like, Ooh, that one's nice. So what I may have done is I may have created something that looks like, uh, some other standard to plug into it, but it's just for me. Right, wrong, or indifferent. Uh, you, you, you, you be the judge.

**Dave Jones:** Okay. Send me a link.

**Chris Gammell:** Oh, uh, yes. I should probably have that up. Yeah. Actually, that's the thing. I don't even know what it is. Like it's that like low. Um, risk for me. Like, I don't know anyone. I don't know what this vendor is. It's literally like, I looked at this thing and I'm like, I need a connector. And it could be like, someone's going to be like, Oh, I could go and plug a, you know, a standard flippity flobbity into that thing. You know, a flippity flobbity, you know, whatever, whatever the standard might be. I obviously don't know what that standard is.

**Dave Jones:** Okay. I'm having a look now.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** It's like, Oh, okay. So it's, you're just using a three pin metal.

**Chris Gammell:** I don't know what it is. Yeah. It's got like a, it's a microphone.

**Dave Jones:** It's a, it's a dinny microphone.

**Chris Gammell:** According to Amazon.

**Dave Jones:** This would be like, you'd using like a, uh, yeah. Some sort of cheap microphone interface, something like that.

**Chris Gammell:** It kind of looks like that. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** And so that was like another option. It was like, Oh, you could use a, uh, XLR style connector, which would be too big for what I need. But like, you know, I've seen XLR, which is like a true microphone, a balanced input kind of thing. I've seen those abused before. Um, and they make those with more than you standard. And for microphones, there's three pins, you know, they make four pin, five pin, whatever all the way up.

**Dave Jones:** This is just a regular three pin din.

**Chris Gammell:** I think this is just din. Is this din?

**Dave Jones:** Yeah. Yeah. Din. A din.

**Chris Gammell:** How do you define din in this way?

**Dave Jones:** Din is a circular connector. Um, I, I don't actually know the origin of the term. Um, but if you search for a three pin din connector.

**Chris Gammell:** Probably something in Deutsche Industrielle, something like that. Din rail is that actually is in din rail. I know that the din in din rail is Deutsche something because it's German. Yeah.

**Dave Jones:** And then you've got the, um, any version of that, which is a mini din, which is used for the, uh, PS2 keyboard, you know, the, you know, PS2 keyboard. Oh, that's a, that's a five pin. Is that right? Yep.

**Chris Gammell:** Yeah. Yeah. Yeah. And that's gotten bastardized before too. That's also what kind of looks like the MIDI, the MIDI connector also kind of looks like that too. It's got six or seven. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** It's a din, isn't it? The MIDI. Yeah. Yeah. I think so. Yeah. No, uh, congratulations. You've stepped into the 1970s.

**Chris Gammell:** Yeah. Right. Exactly. This is like, I just want a cable. I just want a cable. That's not going to rip out the bottom of my thing that I'm trying to make. You know, I'm trying to make a cable assembly that it won't rip out.

**Dave Jones:** And, uh, granted you, you are using the screw locking din rather than just the friction fit din.

**Chris Gammell:** Yes, that's right. Yeah. That's the, that's the thing I don't want it to rip out.

**Dave Jones:** That is a step up. So.

**Chris Gammell:** Oh, that's, that's the fancier version.

**Dave Jones:** Oh yeah. Fancy, fancy. Yeah.

**Chris Gammell:** Yeah. Yeah. This is $4 per pair on Amazon. So.

**Dave Jones:** Oh, when I was a boy.

**Chris Gammell:** Jeez. I mean, that's the thing I'm buying two though, at a time you buy two at a time. You're going to pay whatever the price is.

**Speaker ?:** Yeah.

**Chris Gammell:** Right. And basically on Amazon, you can't get anything less than like seven bucks. Cause I think less than that, it's not worth it for them to actually put it on the shelves at Amazon. Cause they take so much, but yeah. So that's what happens when you're, you're doing last minute engineering like I am, but. Yep. Okay. So I haven't seen, but it's, uh, I'm not, I'm not going to win any design awards. Is that what I'm hearing? Okay.

**Dave Jones:** So the, uh, title of today's show is Chris discovers din connectors.

**Chris Gammell:** Oh my goodness. Discovering the seventies. Uh, one, one part of the time. Yeah.

**Dave Jones:** I thought it was something obscure. Like, you know, you talked, you hyped it up. Like it was.

**Chris Gammell:** That's obviously I don't know what it is though. You know, like I'm like, uh, you know, I'm a millennial discovering this, uh, magical new technology.

**Dave Jones:** This R is.

**Chris Gammell:** Dave, I have this magical machine. It goes back and forth and, uh, it goes up a little, one level at a time. And it squirts plastic out. It's called a 3d printer. Have you heard of all these? Yeah.

**Dave Jones:** Oh goodness. Next thing, you know, you'll be, uh, using, uh, you know, DB 25s and.

**Chris Gammell:** Ah, yeah. Yeah. Yeah. I mean, you can get those populated, I guess. I mean, that's the thing though. Like, I just mean, what I really mean is, uh, I've seen stuff. I've seen connectors bastardized before, right? Like, uh, uh, employer I used to work for, uh, had a RJ 45 connector that was definitely not ethernet, you know? And, you know, you could say that RJ 45 isn't actually technically wasn't what ethernet started with, but I'd say these days it is standard to be ethernet. Um, and that's confusing to me. And other times I've seen other connectors where it's like, don't plug that other thing into here because it won't work. Uh, you know, like that sort of thing. And, uh, sometimes you're just looking for a connector though, you know, should engineers

**Dave Jones:** be scolded over non-standard use of a connector on your product? Like, you know, because you see this all the time. You think that, oh, this is an RJ 45, right? It must be an ethernet and you plug it in. No, it's some custom bloody, you know, interface.

**Chris Gammell:** It's just because RJ, well, that's the thing too, is because the commoditization of high volume things like ethernet basically drives the price down to people like, oh, that's a, that's a good price for a connector. And it's a standard connector.

**Dave Jones:** You can buy the cables and you can, you know, like it's all, yeah, you don't have to make your own custom cables. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** So that's problematic, you know, but I, yeah, I guess maybe we should just put warning labels next to these things that like not ethernet or not. Yes.

**Dave Jones:** It's all in the labeling, but you know, it's got to be like nice, big, bold font, you know, like, yeah. Yeah. Yeah. Hmm.

**Chris Gammell:** I don't know.

**Dave Jones:** I think it's perfectly adequate. I like, you know, I've done it a million times. I can't be judgmental, you know?

**Chris Gammell:** Yeah. Cause well, the other, the other option I feel like is to like go and get a custom cable made, right? Like maybe custom housing.

**Dave Jones:** Yeah. Get a custom cable and a custom connector. And there's somebody who's been involved in custom connector design. It's yeah. The, you know, the major manufacturers, you can go to Amphenol and say, you know, please build me a custom connector. Yes, sir. No problems. And I'll charge you for it.

**Chris Gammell:** I'm sure your, I'm sure your quantities are up in the million, sir. Right. If not, we have a standard NRE. Yep.

**Dave Jones:** Oh, somebody posted this. Oh, where is it? I'm going to have to find it now. Oh my God. I retweeted it the other day. It was this connector. It was the, I can't remember what brand it was. I'm going to find it. So you keep talking and I'll find me. I'll find me. It was a modular connector. It was like, it was one of those ones where you can actually design your own, like, like you get a standard big outer shell, right? It's designed for like a big, like a huge cable. Right. And then you can plug, plug and play your own little, um, you know, Oh, I want a four pin mollusks in there. Oh, I want some fiber. Oh, I want some big high voltage.

**Chris Gammell:** Was it like for, um, for like water, water resistance. That was like the shell piece, like the keeping it like IP rated.

**Dave Jones:** It's not really waterproof. I don't think it's just like, if you need, you know, if you've got some big industrial bit of kit or you've got some spacecraft or something, you want to interconnect all these cables and you've got all these different types of.

**Chris Gammell:** I've seen that before with like, even, you know, they have a 25 pin DIN, you know, something that's massive on its own. And then it gets like outer molded basically with plastic or something in order to IP rate it, but it's like, well, we needed to make the standard cable or we already knew how to use these other types of cables. And then internal in the shell, it's, uh, you know, some, some standard thing that you'd expect to see unshielded, unprotected, whatever. It's just being reused a bunch.

**Dave Jones:** Right. Well, I'm having no luck finding it. So anyway, there are companies that make these modular connectors, um, and you can pick and choose your own things to plug into them. So very impressive stuff. Yep. But, but you know, there's a, there's a, um, thing on cursed connectors on Twitter. I think it is.

**Chris Gammell:** Oh yeah. Uh, I haven't seen cursed connectors, but cursed connectors is I think a, uh, yeah.

**Dave Jones:** And they, I think they just published photos of like weird ass connectors. Yeah.

**Chris Gammell:** I feel like we get to set the mid journey on that, on that one as well. Oh, right.

**Dave Jones:** Yes. Yes, we could. Yeah. Yeah. We could let that rip. Maybe we could do a, yeah. The thumbnail for this one will be a mid journey. Who can, which one of us can produce the best, uh, mid journey cursed connector. Yeah. Yeah. Yeah. Yeah. But it's going to come out all mongey arty looking. That's not going to be realistic. So yeah. I hate that. Anyway, bloody connectors. Age old problem. And do you, that's the thing. Like if you've got a, like you're building an industrial bit of kit, right? Big industrial machine or something like that. Do you have, you know, 20 million cables? Do you try and feed them all through the one connector? Do you have 20 different connectors and then you tie all, then you bundle all the cables together and your cable time all together. And then they come out like a big octopus lead, you know, with 10 different connectors or, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Age old problem. Anyway.

**Chris Gammell:** I am staring at a particularly heinous connector right now, which I'm not allowed to speak ill of can anymore. Oh, right. Yes.

**Dave Jones:** Because you had it all explained to you.

**Chris Gammell:** I did. I did. It was fantastic. I enjoyed that a lot of it. But the connector is still beefy as hell. I'm sure, you know. I've yet to, I've yet to, I haven't. So I have in front of me, I have a can reader and I have a can simulator and I've yet to get the guts to go and plug this into my wife's car. The reader. And I know it will be fine. It'll be fine. But like, I just, I haven't, I haven't figured it out. Although one time, I don't know if I mentioned on the show, one time I was like, I was cleaning up the, like the floor mats in my wife's car because I, I, I got rid of my car when I moved to Chicago. And so I don't have a car. And, um, and so I was cleaning up the floor mats and I like looked up and there was an LED on and I'm like, what is going on here?

**Dave Jones:** I, I, I thought you said, did we talk about this? I thought, no, but I thought you said four mats. And then I realized you're saying floor mats. Floor mats. Floor mats. Floor mats. With an L. Floor mats. It's like soda. It's like soda. You're dropping that L there.

**Chris Gammell:** No, that's just me not speaking clearly. Yeah. I normally say floor, floor mats. Floor. Yeah. Anyways. Right. Okay. And so there's an LED on and I'm like, what is this thing? And then I went and I pulled this thing out and there was, and I was like, what is going on right now? I open it up and there's a cell modem in there and it was plugged into her OBD2.

**Dave Jones:** And I'm like, what? Is this like a tracker or something?

**Chris Gammell:** Is someone tracking this car? And it turned out it was like she had gotten one of those insurance trackers basically. So like there's this whole thing where like in the U S at least, I'm not sure in Australia, but in the U S. I've never heard of it. What's that?

**Dave Jones:** I've, I've never heard of an insurance tracker.

**Chris Gammell:** So insurance companies now in the U S.

**Dave Jones:** I can see where it's going. So they pay you money. So you get a lower premium or you get a lower premium if they know where you are.

**Chris Gammell:** Not if they know where you are, but if they know, they need to be able to send the data back to the servers, but they, they measure acceleration. They read off the speed.

**Dave Jones:** Oh, if you're a Radica driver or something and then your premium goes up if you're a crazy driver.

**Chris Gammell:** Well, they say it in the other direction, but yeah, I think that is true actually. So it's like, I'm sure that's what give you a lower rate as long as you're safe. But then I think it's like, you know, it is punitive if they, if they see you're a nutso driver. Yeah. Wow. Okay. Yeah, it's creepy.

**Dave Jones:** I'm not aware of that here. I don't think that's a thing.

**Chris Gammell:** Yeah. Wow. It's, it's, and the thing is she, she had stopped using it. So she had switched insurance companies, but the thing was still plugged in. So it was still transmitted. I was like, Oh my God.

**Dave Jones:** It was still getting the data. It was so creepy. I ripped that out.

**Chris Gammell:** Yeah. Yeah. Yeah. It creeped me the hell out.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. And now I make those things.

**Dave Jones:** So it's gone, right? You, you actually ripped it out. Tear down. Do a tear down video.

**Chris Gammell:** Ah, I think I threw it away because I was freaked out.

**Dave Jones:** Oh.

**Chris Gammell:** Yeah. You were creeped out. You know the other thing too? No, I know it was, it was actually okay at that point because it was, I looked up the modem and it was a, um, it was a 3g modem and those got sunset.

**Dave Jones:** Oh, right. So you guys don't have 3g there anymore?

**Chris Gammell:** You don't either, Dave. Nobody has 3g anymore. No.

**Dave Jones:** No, Australia still has 3g.

**Chris Gammell:** Nope.

**Dave Jones:** I think it's being phased out, but let's see.

**Chris Gammell:** 3g Australia. Um, at least everyone in the U S all of the 9th of May Vodafone will shut its remaining

**Dave Jones:** 3g servers off like a 3g services off. Okay. Oh, so maybe this year Telstra will follow in June, 2024. So it's still a thing here.

**Chris Gammell:** Oh, it's still a thing there. Okay.

**Dave Jones:** And Optus will be going until September, 2024. Yeah. The U S I think AT&T was the last one.

**Chris Gammell:** Yeah.

**Dave Jones:** All right.

**Chris Gammell:** So AT&T shut down in late February. So, but yeah, we were, we've definitely been like on the edge. And the reason is because they're basically, they're repurposing the spectrum for 5g, right? So to use it for higher panelists, stuff like that and different protocols. Um, 2g is still available in some parts of the world. Um, I think the U S it's mostly shut down as well, but like, basically it's a, it's a bad time. If you have 2g, 3g things out in the world, you hopefully you got the notice a long time ago because that stuff is starting to, to go the way.

**Dave Jones:** See, I would not have noticed that. Cause I've got, I think the only 3g thing I've got that transmits back as my home solar thing, which, which if it didn't fail, because I've, I've done a video on where it actually, it failed inside, like it actually failed, um, which is, I think the first one ever to fail or something. Trust me, you know, trust it to happen to me. Right. Anyway, it's this Australian product that moduses my solar and it transmits, got a little SIM card in it transmits back on, on a 3g. And now I've got one of the earliest 3g models, um, which just after I got it, apparently they started doing the 4g ones cause they knew the 3g would eventually get shut down. That's the thing.

**Chris Gammell:** Right.

**Dave Jones:** And it, it would have just stopped working, you know, it would have just like, yeah, bam. So anyway, now I have a 4g one installed, so it's not a problem, but yeah, that's something that would have just stopped working. I probably wouldn't have noticed. I don't know. Or maybe they would have sent me an email saying, you know, we, we have you on record as having a 3g.

**Chris Gammell:** Time to buy a new one. Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. I'm guessing some of the, some of the support requests on that are the people being like, uh, I looked at my stuff and nothing's transmitting anymore. Where's my data? Yeah. Yeah. Do you still use that often? Do you find yourself using that a lot?

**Dave Jones:** Oh, no. Only when I need to, but it's there. Right. So the data is, it's all on the network. So it's all, you know, the data is all there. So I can pull up like a 12 month graph, you know, something like that. Yep.

**Chris Gammell:** Yeah. That's nice.

**Dave Jones:** Yeah. So I don't use it on a daily basis.

**Chris Gammell:** It's just. Right. Yeah. I'm sure it's like one of those things where you like, you check it every day when you're getting started, like, cause you're like excited about it.

**Dave Jones:** Yeah. It's a thing. Cause you're excited to know how much your solar system produces. And then you might use it in winter time to check, you know, how much like. Oh, sure. Sure. Then after that, after, you know, the first year, then yeah. Yeah. It just becomes a thing that you might use occasionally to pull some long-term data from.

**Chris Gammell:** That makes sense. Yep. Yep.

**Dave Jones:** But it has to be there, right? It, it has to be transparent. Yeah. Yeah. Yeah. Yep. Yep. Anyway. My, my other system failed. Cause I changed shoe phones. Right. So I got a, well, I knew second, cause I'm a tight ass, got a secondhand shoe phone. Right. And it's got.

**Chris Gammell:** Shoe phone is your, uh, is your reference to your smartphone?

**Dave Jones:** My mobile smartphone. Yeah. They're called shoe phones. Yeah.

**Chris Gammell:** Yeah. Like that's a, what a Maxwell smart reference.

**Dave Jones:** Maxwell smart. Get smart. Yes. Correct. Yep. Yep. I won't laugh at you now. Yeah.

**Chris Gammell:** Steve Carell, right? You know, come on, just make it a joke. Just make it a joke. Yep.

**Dave Jones:** Them's fighting words. Yeah. Them's millennial words. Yeah. Right. And, um, yeah. And I've got an older, cause I've got multiple solar systems. I've got an older one, which I have to connect with Bluetooth. Then I've got to use a third party app on my stupid shoe phone, which then I've got a periodically like every month or something. I've got to like down, download all the data via Bluetooth, like log data in the solar, in the inverter. So I download all the log data and then uploads it to pvoutput.org, which is a second system that I use for long-term monitoring.

**Chris Gammell:** PV outputs like a, that's like open source or that's, that's like a brain.

**Dave Jones:** No, it's a, no, I don't think it's open source.

**Chris Gammell:** Oh, okay.

**Dave Jones:** All right. Anyway. Um, and yeah, it's my new shoe phone just doesn't work. It just doesn't, the app just doesn't work on my new shoe phone. And so I haven't got data for months. So I just haven't been bothered to, well, I've tried to solve it and I can't. So it's like, yeah, it did that. That system now doesn't work because I don't have the fricking app that works. Right. You know, it's like, Oh God. Yep. Anyway, actually I might, that's what I might do. I might, I still got my old shoe phone that I replaced. I might actually take that home and, um, just use that every month. I just turned on every month and use it as a portal. Yeah.

**Chris Gammell:** I mean, if you can do wifi, right, you don't need a, need a SIM card in there.

**Dave Jones:** Yeah. No, no, I don't need a SIM card. No, I can just, yeah. I can just turn it on and keep it charged up every month. Yeah. Yeah. I'll do that. Damn it.

**Chris Gammell:** All right.

**Dave Jones:** Yeah. Ava's decided. Why didn't I think of that? Anyway.

**Chris Gammell:** I have spoken.

**Dave Jones:** Oh boy. Anyway. Yeah.

**Chris Gammell:** Uh, well thinking, speaking of things off in the future, uh, and I guess topical, but not really a big deal and not surprising at all. Uh, Autodesk has officially.

**Dave Jones:** Oh yeah. Yeah. Gonski.

**Chris Gammell:** Yep. 20, but not June, 2026. Eagle. Eagle is Gonski. Sorry.

**Dave Jones:** Eagle has flown the coop.

**Chris Gammell:** That's right.

**Dave Jones:** Yep. Yes.

**Chris Gammell:** It's, uh.

**Dave Jones:** Thanks for all the fish.

**Chris Gammell:** Yep. Yes.

**Dave Jones:** I mean, it's not going to be until like, it's not for another couple of years. Right.

**Chris Gammell:** That's right. Yep.

**Dave Jones:** But they have announced it, which, which, which means don't bother using it anymore. Basically just, you know, like change now.

**Chris Gammell:** I mean, they're, they're trying, this is in line with what we expected, right? They're, they're investing all their time in a fusion 360 or fusion electronics, I suppose. Definitely.

**Dave Jones:** Which is a spinoff of Eagle from a code from the PCB. The SB module in fusion is actually Eagle, right? That's where it came. That's where the code base came from.

**Chris Gammell:** Yeah. I don't think the code base, I think the, the, um, the design and stuff like that. I think it was a bottom up rewrite.

**Dave Jones:** Oh, really? I don't think they used. Yeah. Yeah. Yeah. You don't think they used any Eagle code. Really?

**Chris Gammell:** Why? I'm talking out of my butt. I don't really know, but I, the Eagle code is really old, really, really, really old. So I, I, that would be, it would be tough to make that smush together. I'm guessing. Um, so I, you know, it's end of an era, but also I think it's really just an inevitability given the fact that they were bought by Autodesk. Like this is what happens.

**Dave Jones:** So Autodesk don't want a hobby solution. That's that, that isn't their business. Right.

**Chris Gammell:** That's right. Right.

**Dave Jones:** Yeah, totally.

**Chris Gammell:** So, uh, good luck. I think it's great. Yep.

**Dave Jones:** And, uh, and technically, unless you've got an older perpetual license version, that's

**Chris Gammell:** right.

**Dave Jones:** Um, you're screwed, right? Because you, it simply will stop working. Right. Yeah.

**Chris Gammell:** I think the thing is they're going to stop selling licenses to it. So like, that's really how they kill it. Yeah, but it's a, but you can't buy it. You can't buy it.

**Dave Jones:** But it's a phone back to the server to enable things, isn't it? If you're on the monthly thing, if you're on the subscription, isn't it, it will simply stop working if it can't talk to the server, right?

**Chris Gammell:** Uh, I think so. I'm not, I'm not sure. So I think it's going to stop. I haven't had Google on my computers in a long time.

**Dave Jones:** There is an older perpetual version. So you pay for it. But then, uh, six months after they bought it, once again, which everyone predicted they would go to a subscription model. So if you bought into the subscription model and you don't have. That, uh, uh, perpetual version, then yeah, you're, you're screwed. I think, I think it will actually stop working.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. So, um, ouch.

**Chris Gammell:** Yeah. And this is not new news either. This is, we haven't recorded in a while. Yeah.

**Dave Jones:** No. And the obvious question is, well, why don't they just make it free? You know, they, why don't they just give it to the world? You know, it's because, well, you know, that.

**Chris Gammell:** I think they bought the, you know, like they bought the user group as well. They're trying to, I think they're trying, I mean, like, you know, to their credit, they're trying to gently nudge people, right? They're trying to say, Hey, look, this is a, they, they want to transition people to the paid solution.

**Dave Jones:** That's why they won't give it away for free. They won't go, okay, we're going to convert it back to a perpetual version. Here is the final release. Here it is. Give it to the world for free because then no one would buy fusion 360.

**Chris Gammell:** I think that's right. Yeah. I think they're trying to, they're trying to make people decide. And I think, you know, they bought this group and they're trying to make the group there and, and they've decided at some point it's not worth supporting that anymore. And it's a decision. It's fine.

**Dave Jones:** Like I said, maybe in 10 years time or something, cause that's what Altium did. Altium, like 20 years later, they went, here's DOS. Here's the DOS version for free. You can have it. It's free. Go for it. You're not.

**Chris Gammell:** Yeah. Right. They got enough, I read calls from the gray beers and they're like, get out of here.

**Dave Jones:** Yeah.

**Chris Gammell:** Go on, get. Yeah. Yeah.

**Dave Jones:** Anyway. Yeah. So it's free. So technically you can get Altium for free. It's just the old DOS version, which is great.

**Intro Voice:** Some people prefer it that way, Dave. My goodness.

**Dave Jones:** Number of boards I've done in that old DOS version, you know. That was the duck's guts. Auto Tracks. 1.61 was the last final version. I still remember it fondly.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Or if you were anyone, you had the 1.61 ND, which was the no dongle version. Because it was hardware dongle. Oh, I see. Got it. Yeah. Yeah. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** And then they did actually release an official no dongle version because some, you know, clients from the military or something said, hey, we can't have these dongle things. So, you know. Right. So they made a no dongle version and then it spread around.

**Chris Gammell:** As it does. Like wildfire.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Oh, boy. Yep. So everyone had a copy of 1.61 ND. It's great. Got it. Those were the days. Anyway. Can we also talk about old school? Speaking of old school.

**Intro Voice:** Sure. What have we got?

**Dave Jones:** They don't make PCBs like this anymore. I added the link just before the show, but I'll send it to you right now. Here you go. I got it. I see.

**Chris Gammell:** Holy moly. Yeah. No, they do not. This looks like this is a store. This looks like this is a tray that you've like pulled out of a drawer and it's just got all your, storing all your chips on it. Yeah.

**Dave Jones:** But this was so common back in the day. Let me explain.

**Chris Gammell:** I don't miss this era, Dave.

**Speaker ?:** Yeah.

**Dave Jones:** Let me explain what we're looking at. We're looking at a board that's probably a couple of feet long, right? Yeah. It's probably 800 millimeters deep by 500 millimeters wide or something, right? Yeah. So it's like half a square meter board or something, right? It's absolutely enormous. And every single square centimeter of this thing is filled with a dip chip.

**Chris Gammell:** Yeah. And there's big edge connectors. It looks like this whole thing's slotted into like a server rack or something like that.

**Dave Jones:** It's slotted into a server rack and it's got the flippy things at the front. Yeah. So it's slotted into a big, a huge, deep rack. The card edge flippers. Oh, the locks. So if you have a look at the top. Yeah. Yeah. The locks. The card edge locks. Yeah.

**Chris Gammell:** Yeah. You're right. Yeah. Okay.

**Dave Jones:** Right. And yeah, so that's what we're looking at here is it's just absolutely chocker.

**Chris Gammell:** Is your smart fridge chirping at you? Is that what I'm hearing?

**Dave Jones:** That's my shoe phone. That's my bloody shoe phone. Your shoe phone. Yeah.

**Chris Gammell:** Man, it doesn't even turn off the shoe phone.

**Dave Jones:** I'll see his call and it's probably Mrs. Oh, no. It's telling me to record the amp hour. No, hang on.

**Chris Gammell:** Dave's got the wrong time zone. He's got the wrong time zone on his phone.

**Dave Jones:** No, it's somebody called me. Hang on. We'll find. Oh, yeah. It's Mrs. Eve eBlog. Uh-huh. I don't.

**Chris Gammell:** Oh, okay. So.

**Dave Jones:** I don't think she knows we're actually recording this morning. That makes sense. Yeah.

**Chris Gammell:** The Mrs. Here also, I didn't tell her. Right. I'm in a little trouble for that one. Anyway. Well. My favorite thing on this, just from the photos, is the last photo. You saw that one?

**Dave Jones:** Oh, hang on. Last photo. Let me scroll through. This is gorgeous. Oh, the backside. Yes. I actually posted this on Twitter. It's the backside. Oh, my God. This is amazing. It's the silkscreen.

**Speaker ?:** It's the index.

**Dave Jones:** Yeah. It's the silkscreens on the bottom because they don't have room to put the silkscreen on the top because all the chips are butted up against each other.

**Chris Gammell:** What I'm really imagining is the intern that has to lay on his back underneath the board while you're debugging. Yeah, yeah, yeah. Four up three to the right. And it's like, you 402.

**Dave Jones:** Been there. Done that, dude. Yeah. Yeah.

**Chris Gammell:** Oh, my God.

**Dave Jones:** Yeah, yeah. Yeah, because there was no room.

**Chris Gammell:** You get the paper next to it. Yeah.

**Dave Jones:** This is how it was done back in the day. You did not have room on the top to put the silkscreen designators because you had to jam everything in.

**Chris Gammell:** The 0.1 mic or the 1 microfarad, like the yellow caps just on the end of all of these things, the exact same cap everywhere, the through-hole ones. Oh, man. Yeah. I don't miss this era at all.

**Dave Jones:** They're all horizontal because that's how you routed these things. There are routing-optimized two-layer or four-layer, six-layer, eight-layer routing algorithms that are optimized for all the traces going one direction on one side of the board, and they all go on one direction on the other side of the board. Because you don't want to go diagonal across the board or something like that. Then you wipe out all your routing room, right?

**Chris Gammell:** We live in a society, Dave.

**Speaker ?:** Right.

**Dave Jones:** And there's not a single bodge wire on it.

**Chris Gammell:** I mean, maybe.

**Dave Jones:** I don't see a single bodge wire.

**Chris Gammell:** Maybe they staked one. There's actually a pretty solid layer of dust, which is another good sign of it.

**Dave Jones:** I would so want to buy it. I would love to buy this. It's currently on eBay, but it's like $400, $390 or something.

**Chris Gammell:** Holy moly. Yeah. What is this? Intergraph Corporation Vintage Board Service.

**Speaker ?:** Intergraph.

**Dave Jones:** It's a graphics server or something. I think it's some sort of. Yeah.

**Speaker ?:** Oh, my God.

**Dave Jones:** Yeah. This era of computing, it's insane to me. I'm staring at them right now. I've actually shown them on my blog before. I've torn down many old school items like this. Yeah. And just giant racks of dip chips. And they're all socketed, too. Socketed.

**Chris Gammell:** I was going to say. They are all socketed. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** And not just the ones that you're taking into program.

**Dave Jones:** Oh, evil. Single wipe sockets. Not even dual wipe, let alone machine pin.

**Chris Gammell:** Single wipe is the mechanical.

**Dave Jones:** Single wipe is the contact. The contact is only on one side of the socket. Got it. Whereas a dual wipe, you'll have like a spring contact with contacts on both sides. Got it.

**Chris Gammell:** So if the corrosion happens, you've got a little more chance.

**Dave Jones:** You've got more chance of it being on. Yeah. Because it's on two sides.

**Chris Gammell:** Maybe that clears the. It's using so much current, it just clears the short itself. What are the yellow ones? The yellow 16 pin dips. And like the. Yellow.

**Dave Jones:** Oh, they would be resistor networks.

**Chris Gammell:** Dude. Oh, really?

**Dave Jones:** Oh, you young whippersnapper. No, no, no.

**Chris Gammell:** Well, there's like, I figured the little ones or the thin ones were resistor networks. Yes. But there's some other socket.

**Dave Jones:** There. The thin ones are usually single, usually the pull-up packages. But the dip ones, the dip version, they're actually usually the individual resistors in there. So there's like eight of them in. Yeah.

**Chris Gammell:** You know. For like op amps though? Or like for what kind of purpose?

**Dave Jones:** 16 pin dip. Oh, you could use them for series, you know, series termination resistors, stuff like that.

**Chris Gammell:** Oh, okay. You can use them.

**Dave Jones:** Just anything.

**Chris Gammell:** Oof. Yeah. This gives me a little anxiety looking at this, to be honest. I wouldn't have made it in this era, Dave. No. I don't know if you're making it in the current era either. I'm not sure. You know. Yeah. I don't know. I wonder about that. Like, you know, I do wonder like if I just kind of squeaked through university and stuff like that. Like I just happened to make it through, like, I think about like, like 30 years prior, right? Where it was like, you know, all physics and like, you know. Yeah. Yeah. It was. Yes. I don't think I would have made it then. Right. I don't think I would have made it to be honest.

**Dave Jones:** Yeah. I probably wouldn't have made it.

**Chris Gammell:** Yeah. Yeah. I mean, that's just a different class of engineer. And it's like a different, I don't know. I just think it's, I don't think I would have made it. I would have maybe been like a technician if I was lucky, you know.

**Dave Jones:** Right. Right.

**Chris Gammell:** If I'm, you know, I'm kind of like technician now, but yeah.

**Dave Jones:** Well, this thing is like, I'm surprised that they don't, didn't use some gals or pals to actually consolidate some of these.

**Chris Gammell:** They had some non-dip stuff further down the board. Yeah. There's actual processes. We've got a lot of descriptive stuff. There's a, oh yeah, 68,000. There's an MC 68,000. There's a 68,000 process.

**Dave Jones:** But it's all, most of it, 80% of it is like 74 series logic. And there's some RAM up the top. So they've got a big array of memory.

**Chris Gammell:** Yeah, like one of the big areas, right? Yeah.

**Dave Jones:** Yeah. So, and there's some analog stuff down the bottom. Or is that just pals? Like they've got like pots, they've got sealed pots down the bottom of the board. So, yeah. And then it looks like there's got a real-time clock board maybe with a battery on it.

**Chris Gammell:** Uh-huh. So, yeah. Former battery. Like an atom. Bob of glue. Yeah. Yeah.

**Dave Jones:** Yeah, if I check out that part number, that's got to be a real time. Oh, there's a Dallas semiconductor. Oh, it's been chopped off. Yeah.

**Chris Gammell:** Yeah. I'm not sure this thing's going to work, Dave. I hate to tell you. No, no.

**Dave Jones:** I don't think it's going to work. But, oh, yeah. No, it's just a classic example. I've seen bigger. I've seen bigger than this. And I've like physically worked on bigger boards.

**Chris Gammell:** I just feel like I can like see, I can like feel my fingers getting poked by all of the through hole things. Oh, yeah. All the through holes. Yeah, you get like the puncture wounds. Yeah, yeah.

**Dave Jones:** I used to work as a production tech. That was my first job. And first, it was these cards, was these types of cards with the 19-inch racks and the pool How much did it flex?

**Chris Gammell:** If you didn't pick it up right, like so say you just picked up one end. Oh, yeah. With the whole thing just like crack in half.

**Dave Jones:** No, it doesn't. But there is warpage. And it depends on the orientation as well. Like if, because all the chips were in one direction, that actually adds some stiffening to the board in that orientation. Whereas if you hold it on the opposite. So this board, if you held it on the top and the bottom, it would flex more than it would from right to left.

**Chris Gammell:** Yeah. Oh, interesting. So like you're saying, if you held the long sides, it's okay. Yes. If you held the short ends. Yeah. Because this is like a, what's the aspect ratio on this thing? Like a five by two.

**Dave Jones:** Yep.

**Chris Gammell:** Kind of. Something like that.

**Dave Jones:** Although this one's a bit different because the, because it uses socket. So if the chips are sold in, it's a bit more rigid because the chips actually work as a physical stiffener as well. So yeah. That's crazy. I've worked on boards that have to use physical stiffening rods in them. Yeah. Like metal rails. And they sold it down to the board. Yeah. Yeah. And then, and then there's the classic ones that have, and then the bars, not only can you use them as stiffening bars, but they're also bus bars as well. So, so your ground and your power can go right across the board on these huge bus bars.

**Chris Gammell:** Right.

**Dave Jones:** So you would have layers of bus bars in there going across the board. That's a spacey bus bar. It's great. Yeah. It's, it's fantastic stuff. Yeah.

**Chris Gammell:** Oh man.

**Dave Jones:** Yep. And these ones would not be hand route. These would be completely auto routed. Oh yes. I can see some of the traces, right angle traces everywhere. Yeah. Yeah. Yeah. These are all a hundred percent auto routed. Yeah. Yeah. Because that's what you did back in the day. You laid out all the chips, all, all in the rows and the, and all pin ones all facing the same direction. I guarantee you probably won't find a single chip on here with pin one in the opposite direction.

**Chris Gammell:** I betcha. I think I've already proved you wrong. Yeah.

**Dave Jones:** Oh really?

**Chris Gammell:** Oh no. That's just marked differently. Oh, that's weird. I've seen one where there's like, most of them are in the bottom left, you know, in the orientation of these photos.

**Dave Jones:** Oh, I see what you're talking about. I can see one with two dimples.

**Chris Gammell:** I can see one with two dimples.

**Dave Jones:** Yeah. Yeah. Yeah.

**Chris Gammell:** But it's definitely the top side. I think that's, you could tell like, cause it's also got the, yeah, like the cutout dimple.

**Dave Jones:** Yeah.

**Chris Gammell:** Right. Where it's like a, like a half moon on the, on the short side of a chip. Yeah. And this has been an episode where we've been trying to describe a lot of things. I'm sure it's very frustrating for us.

**Dave Jones:** It's very frustrating. Yeah.

**Chris Gammell:** Dave and I are doing fine. We can make it a video podcast, I guess, but you got to look at our ugly mugs and you don't want to do that.

**Dave Jones:** No. You see Dave.

**Chris Gammell:** He's yeah. He's fine. No, you've seen me too many times. Yeah. Yeah. I'm all unshaven. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** I barely leave the house. Why do I need to do anything? I'm going to haircut in weeks.

**Dave Jones:** I got a haircut yesterday.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Home, home, home haircut. So you can rate it. Oh really? Oh wow. Saving money, huh? Yeah.

**Chris Gammell:** The economy's taking a downturn. Here we go, folks. I actually enjoyed it.

**Dave Jones:** It started with COVID.

**Chris Gammell:** You two things, not what it used to be. Right.

**Dave Jones:** Yeah. Got it. Save money where I can. Yeah.

**Chris Gammell:** No, my wife gave me haircuts during COVID. It was fine. She did a nice job. Yep. I think, I like the experience of going out and getting one though. It's a little different.

**Dave Jones:** Oh really? No. I don't. Yeah. Like going to local honey laundering operation at the local shopping center. I swear it's a money laundering operation.

**Chris Gammell:** Yeah. Yeah. They don't actually catch your hair.

**Dave Jones:** Far too many guys hanging around there that don't look like the cotton hair. Let's just put it that way. I see. I see. Got it. Got it. Yeah.

**Chris Gammell:** They do say Australia is the shadiest of places. Yeah.

**Speaker ?:** Right.

**Dave Jones:** And let's just say that they're all of one particular. We'll give you a haircut. Yeah. We'll give you a haircut. Cheap. Cash. Cash. Yeah. Yeah. Oh boy. Yep. So I'm sure they bring in a pretty penny. I'm sure they actually earn a lot.

**Chris Gammell:** Right. Right. Right. Right. Yeah. They always say that the money is in the haircutting. Yes.

**Dave Jones:** Only 10 people walk, walk through the door, but they have a hundred thousand dollars in cash income.

**Intro Voice:** Yeah. Right. Right.

**Dave Jones:** I love it. Yep. Money laundering for the day. Anyway.

**Chris Gammell:** Is there anything else we should talk about? I don't know if there's any. I mean, thanks to our buddy, Unmanaged, to keep doing that stuff. Next week will be CN Lore. I actually recorded that interview yesterday and it went fantastic. It's the CH32V003. Oh, yes. The part that you also tested. He's got a library. And so we talked all about that and low level chip design and RISC 5 parts. So it turned out pretty great. Cool bananas. All right. That's it. I will be in Prague. I'm not sure when the next show is after that. So Dave and I will discuss that after that. I will be in Prague. If you're in Prague for Embedded Open Source Summit, please do find me. I will be at a booth and walking around and giving a talk.

**Dave Jones:** As always, there will be a prize if you can catch Chris looking. And absolutely depressed sitting on the stand. Yeah.

**Chris Gammell:** Maybe not depressed, but probably jet lagged. Jet lagged for sure.

**Dave Jones:** Yep. Have fun.

**Chris Gammell:** Thanks. See you. Catch you next time.

**Dave Jones:** Bye.

**Speaker ?:** We'll be right back.
