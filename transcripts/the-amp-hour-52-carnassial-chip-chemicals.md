---
episode: 52
title: An Interview with Jeri Ellsworth - Carnassial Chip Chemicals
url: https://theamphour.com/the-amp-hour-52-carnassial-chip-chemicals/
---

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life.

**Jerry Ellsworth:** And I'm Jerry Ellsworth from Portland, Oregon.

**Dave Jones:** Hey, Jerry. Jerry's in the house.

**Jerry Ellsworth:** Jerry's in the house.

**Dave Jones:** Yep. Good to be back. Fantastic. I think we set a record this morning for the most amount of time taken to get an episode up and running. Yeah, get up and running.

**Chris Gammell:** Yep, that's right.

**Dave Jones:** Yeah, we're just slack. I don't know.

**Jerry Ellsworth:** I had some problems with the Google Plus stuff.

**Dave Jones:** Yeah, we blame technology, don't we? We just... Us Luddites, we have no idea how to drive this stuff.

**Chris Gammell:** And Jerry, for people watching video, Jerry will be frozen the whole time. Unfortunately, video didn't work out for her. But maybe next time. So, that's okay. Right.

**Dave Jones:** And after all the complaints last week, yes, we are going to stick to electronics. Electronics, apparently. Maybe. Are you sure about that?

**Chris Gammell:** Apparently, electronics are important.

**Dave Jones:** Yeah. Well, you know, it'll be electronicky. Yeah. Is that even a word?

**Chris Gammell:** Electronicky?

**Dave Jones:** Electronicky?

**Chris Gammell:** Electron. You know? Something's electronic. I think electronic is actually an adjective.

**Dave Jones:** It is actually the... Right. Yeah. Yeah. There's no need to put the Y on the end.

**Jerry Ellsworth:** Right. We make it up as we go.

**Chris Gammell:** Right. So, Jerry, you are here because we wanted to talk to you about transistors.

**Jerry Ellsworth:** Ah, yeah. You must have seen some of my new videos.

**Chris Gammell:** Yes. We have seen your new videos. Very cool. I have been watching the...

**Dave Jones:** So, if people don't know, Jerry has... Well, there's one video, isn't there? I've only seen one.

**Chris Gammell:** Oh, he was sleeping. That's why, Jerry. She just posted one. Yeah.

**Dave Jones:** Oh, right. Oh, sorry. No. Yeah, I only just got up.

**Chris Gammell:** We do a sleeping, Dave.

**Jerry Ellsworth:** So, some backstory here. About five years ago, I started on this quest to build transistors at home, Chris's favorite subject. And it took me about three years. Actually, it's been longer than five years if all my math works out here. But about three years ago, I made my first transistor. I posted a YouTube video about it and descriptions of how to do it. But it was kind of hand-wavy and I didn't go through all the steps and show people. And for years now, people have been sending me emails about once a month or twice a month saying, you faked that. I can tell. You know, there was a slight hand trick. Oh, yeah. Really annoying stuff. Oh, goodness. So, I had a little bit of time on my hand after finishing a project. And I decided to set up the diffusion furnace and go through the steps again and try to make a little bit more advanced device. I'm hoping by the end of the week, I'll have something, at least a NAND gate or with a little luck, a ring oscillator working. Oh, nice. So, I've been building these transistors with just household chemicals and stuff that I bought off eBay. And I probably have, you know, in the actual stuff that I'm using to make the transistors, you know, maybe $1,000 invested or less.

**Chris Gammell:** Oh, wow. So, less than a chip fab, you're saying?

**Jerry Ellsworth:** Yeah.

**Dave Jones:** Yeah, slightly less.

**Jerry Ellsworth:** Several magnitudes, I'm sure.

**Dave Jones:** Right. But it does still require sort of specialized gear, doesn't it? I watched one of your videos and you had mention of like a thousand degrees oven and all that sort of stuff.

**Jerry Ellsworth:** So, when I first started researching this, I got some books on semiconductor process. And, of course, you get a modern book on process techniques and they talk about ion implanters and plasma etching and all this stuff that's very expensive and almost impossible to do at home. And I actually started going out and acquiring this stuff. I have a plasma etcher and I have an ion beam line. I didn't know that. I have a reactive ion etcher and stuff. What? Chris, you haven't got one? Well, I used to work on those.

**Chris Gammell:** I used to work on those. Come on, everyone's got one of those. That's awesome.

**Jerry Ellsworth:** Yeah, this one's like, it's a TFE barrel etcher.

**Chris Gammell:** Oh, nice.

**Jerry Ellsworth:** It's more of an asher, but.

**Chris Gammell:** Yeah. Yeah, so that's used for getting resist off usually. Right? Mm-hmm. Yeah. That's pretty, that's pretty. How much did you pick that up for? I'm just curious about that.

**Jerry Ellsworth:** Oh, I think it was less than $1,000.

**Jerry Ellsworth:** That's crazy.

**Jerry Ellsworth:** Man. But as, actually I ran into a guy that worked at Fairchild Semiconductor. His name was Peter and I, I'm not going to try to pronounce his last name. There's too many letters in it. G's and, and Z's and stuff like that. But he said, he, he kind of took me under his wing and he told me, well, back in the good old days, we used to do it this way and that way with much simpler equipment. So I've actually reduced it down to just a furnace that can go to a thousand degrees C or a kiln. You can use a pottery kiln too. I have a little tiny tabletop kiln that I've done the same work in. And a CPU fan for doing all the spin coating with some double stick tape on it so you can stick the wafer pieces down. And I'm using vinyl stickers currently for all my masking steps. So I just cut out the patterns I want and stick it straight down to the wafer. And for etching, which this scares everyone because it has hydrofluoric acid in it, I used either use, um, art store glass etchant or this rust and stain remover that you can just buy from the grocery store called Wink, uh, rust and stain remover, which happens to have 2% hydrofluoric acid in it.

**Dave Jones:** Oh, nice.

**Jerry Ellsworth:** People, people always freak out about hydrofluoric acid because professors have put the fear of God into us that one drip of this is going to get on our skin and we're going to immediately die.

**Chris Gammell:** Well, they're talking about like full, was it full molality? Is it modal? Yeah. Molar? Molality? Whatever it is. The full strength stuff. That's what, that's what the scary stuff is. That's, that's what I'm scared of because when you work in a fab, that's what they talk about spilling all over yourself, even though that, if that happens, you're, you're dead.

**Jerry Ellsworth:** Yeah.

**Chris Gammell:** Anything you use enough, I mean, anything you use enough fab.

**Dave Jones:** Darwin has sorted you out, right?

**Chris Gammell:** Well, yeah.

**Jerry Ellsworth:** Anything you use in a fab, they're going to go for maximum throughput. So if you need to etch an oxide off, they're going to use the strongest acid with the strongest concentration possible so they can just run hundreds of thousands of wafers through per hour. You know, at home, you can wait 20 minutes for an oxide etch with the rust and stain remover.

**Jerry Ellsworth:** Yeah. Mm-hmm.

**Jerry Ellsworth:** That's so awesome. That's about it. I mean, a very little, I don't even do metallization. I'm using conductive epoxy for all the contacts and gates.

**Chris Gammell:** Oh, okay.

**Jerry Ellsworth:** And that was, thanks to Peter, he, I was, I picked up all of this sputtering equipment and evaporation equipment. And I'm like, oh boy, this is going to be difficult. And he said, oh, back in the seventies, we were experimenting with conductive inks.

**Speaker ?:** Hmm.

**Jerry Ellsworth:** And so it works, it works great.

**Dave Jones:** Oh, and so does this mean that you're going to use this high, this higher end gear? Perhaps someday. Or are you just going to stick with the lower end stuff for this series of like the stuff that real people can get?

**Jerry Ellsworth:** Oh, for this series, it's all going to be the low end stuff because I have such a learning curve before I can start like bringing up an ion beam line. Right. Yeah.

**Chris Gammell:** You bend it the wrong way and your, your, your neighbor walks out the next morning. They're like, you know, something feels funny. I think I have a foot growing out of my forehead. This is so weird.

**Jerry Ellsworth:** Yeah. You start accelerating ions and crashing them into your sector analyzer. Yeah. You're going to start emitting a lot of x-rays. Yeah.

**Chris Gammell:** You just don't, I mean. Yeah. But I mean, I guess if your, your neighbor's dog is a little too loud or, you know. Nuded.

**Dave Jones:** Yeah.

**Jerry Ellsworth:** Actually, I have that problem. So that could be good.

**Chris Gammell:** There you go. Yeah. Because some, I mean, some walls aren't going to stop those ion beams, right? I mean, depends on what it is. If it's the heavy stuff, it's probably going to get stopped. But if it's certain types of beams, you're not going to stop it with normal, you know, clothing or.

**Jerry Ellsworth:** Yeah. I don't know if ions would emit from the chamber, but because it's awful thick metal. Yeah. They do have, you can extend electrons into the atmosphere through very thin metal windows. I think it's like titanium or something. But that's like super exotic stuff that they experiment with for medical applications. And so I think x-rays would be my biggest worry. So I should get some lead blocks.

**Dave Jones:** Would that, what? So the, so they actually go through the thin wall, do they?

**Jerry Ellsworth:** Yeah.

**Dave Jones:** Yeah. Is that some quantum thing? Is that some, I assume that would be some quantum thing where it's, you know, it, you don't know where it's going to be. So it can actually jump through the wall. It can actually jump to the other side of the wall, like quantum tunneling and stuff like that.

**Jerry Ellsworth:** Yeah.

**Dave Jones:** Yeah. I'm talking out my ass here. This is why you are. You totally are. Yeah. You're talking about x-rays getting through a wall? That's how quantum tunneling transistors work, isn't it? No, no, no.

**Chris Gammell:** X-rays get through a wall because of the wavelengths of the x-ray. I think. That's what I think. Maybe I'm wrong about that too. The energy and the wavelength, I thought that's what gets x-rays through stuff.

**Jerry Ellsworth:** Well, okay. The reality of every atom that we're made of, there's, you know, the nucleus, which is very dense. And then you have all these electrons whizzing around and the distance between those is massive. So, you know, if you make a thin enough surface, you know, electrons will go zipping through and won't collide with anything. Some will, but many will go straight through.

**Dave Jones:** Yeah. Actually, we are made up of 99, I think it's like 99.9% empty space. Our actual bodies, all of our atoms are just empty space, really, mostly.

**Jerry Ellsworth:** I actually experimented with quantum tunneling and I haven't achieved quantum tunneling yet. There's a process called light emission by quantum tunneling. I forget the exact acronym, but you make aluminum oxide layers so thin that it emits light when the electrons tunnel through to the surface on the backside. So if you have a transparent conductor, aluminum oxide, and an aluminum backside conductor, statistically, these electrons will be on, you know, the far side of this oxide. And this will, when this happens, it emits light. And it's kind of a cool process because depending on the voltage and field that you apply, I think it starts off with like a dull red glow. And as you increase the voltage, it goes up to a white light. But the efficiency is very low.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** Someday I hope you make that work.

**Chris Gammell:** That would be very cool, though. Yeah, that would be awesome. You should call Adafruit and they'll make some clothes out of it or something like that. I think it's fine.

**Jerry Ellsworth:** In all the literature, it seems like it's very dim. It's something you'd probably have to look at in the dark. Yeah.

**Chris Gammell:** That's really cool. Yeah.

**Jerry Ellsworth:** So you guys were talking about the conductive pen a few weeks ago. Oh, yeah. Yeah, that's old.

**Dave Jones:** See, I told you, Chris. Which is not new. I know, I know. You were talking about, you know, I thought that was where that new story came from.

**Jerry Ellsworth:** I was so frustrated when people were sending me these links over and over and over again, like, ooh, a new pen that writes silver ink. I had one when I was a kid. I know. I'm sure I did, too.

**Chris Gammell:** Well, I think you guys know I still am a kid. I mean, look at this.

**Jerry Ellsworth:** Oh, yeah, you are. Oh, you know, age is creeping up on you there, man.

**Chris Gammell:** Oh, I know. Yeah. Good thing this camera doesn't zoom in. See the wrinkles.

**Dave Jones:** Right on that baby face. Yeah, there we go. Oh, goodness.

**Jerry Ellsworth:** So anyway, I'm very excited about doing all this home chip stuff. Yeah. I want to see more people go and experiment with this because, if anything, it's a great learning experience, and it's not too difficult. It's surprisingly easy. It takes me about, I don't know, 12 hours to make a transistor that works, and about the same amount of time to make one that doesn't work. Yeah.

**Dave Jones:** But surely, Jerry, you... Most of the time you're just... Surely you aren't going to... We've got that delay audio thing happening. Real professional radio here, folks. Yeah, well... We're a bunch of amateurs, aren't we?

**Jerry Ellsworth:** Most of the time when you're making the chips, you're just waiting around for thermal processes to happen. So you just stick something in the kiln or furnace and just wait six hours.

**Jerry Ellsworth:** Yeah. Yeah.

**Dave Jones:** But surely, Jerry, you aren't going to buy into Chris's original fantasy. What? That, you know, we'll all have chipmaker machines and it'll be a revolution. Here it comes. Please tell me you don't buy into that. I know. We saw this coming, Dave. I know. You guys hyped it. You guys poked me. Yeah, there we go.

**Jerry Ellsworth:** No, I think it's going to happen eventually. Maybe not in our lifetime, but it's probably naive to say that it's not going to happen. You know, it's...

**Dave Jones:** Sure. I agree. But yeah, it's not going to happen in our lifetime probably, right? Yeah. Because there's all those, you know, there's all those really simple things like, oh, packaging, testing, and the fact that you can buy a 50-cent microcontroller that's already packaged, tested, and has a complete data sheet and everyone else can buy it too. How do you compete against that? It's one of those, you know. And then the other argument Chris was making is that, oh, but you can make your own custom chips. Well, it wasn't that the idea of FPGAs, you know. So, really, it's pointless.

**Chris Gammell:** I'm sorry, Chris. You lose again. You know, the nice thing about video, Dave, is I get to give you a death glare while I listen to you.

**Dave Jones:** And the good thing is, is I just totally ignore it.

**Jerry Ellsworth:** And with my frozen video, it just looks like I'm hungry. Yeah.

**Dave Jones:** The frozen video is great. It's just Jerry sitting there with a finger on her lips. Staring at a chicken. Yeah. So, you're staring at a chicken. What is that? That's her microphone. That just covers up my microphone. Yeah. All right.

**Chris Gammell:** So, I like Jerry's argument, though. So, what was it, Jerry? The, like, 50 years ago, people didn't think they'd have machines that made ice cubes in their home or something like that?

**Dave Jones:** Yeah, but it's incredibly easy to make ice cubes. Come on, guys. You can't make the, you can't extend like that. You can't make the comparisons. We're talking about ridiculously small technologies to get any useful chip. It's just not going to happen. I think the, no, man. The economy is of it, too. As Jerry said, within our lifetime, right? And the economies of it, it's just pointless. It's not like the original flame of a 3D machine, of a 3D make-a-bot. That was your original comparison. And you've wimped away from that one since day one.

**Chris Gammell:** I haven't wimped away from that one.

**Dave Jones:** You have. Come on. Totally. Totally. Oh, I don't know. I'm not even going to argue this anymore. It's pointless.

**Chris Gammell:** It is pointless because we don't know what the technology is going to be needed. That's the problem. We don't know what the technology needed is going to be, so.

**Dave Jones:** And, well, no, I can tell you. If it follows the timeline for semiconductor manufacturer for the last 50 years, then it's going to be, the answer to that question is more advanced. More advanced than the already unobtainable technology you can get at home. So, sorry. It's just not going to happen.

**Chris Gammell:** But you run out of headroom eventually, too. So, now they're going to like 450 millimeter wafers, right? Or 12-inch wafers. And they're not even going to break a profit for, what, like five years on a fab? So, eventually they're going to run out and they're going to say, well, we don't want to make chips anymore because it's not economical, right?

**Dave Jones:** Right. So, the whole industry is just going to stop because no one's going to make money out of it. I don't think that's going to happen.

**Chris Gammell:** Exactly. I think they'll push the chips that go into the iPad and everything else. And then, eventually, I think that the small makers might not be able to get chips they need.

**Dave Jones:** It's a self-sustaining industry. Always has been, always will be. Can I get a second to chime in here?

**Chris Gammell:** Of course. Go for it. That's what you're here for.

**Jerry Ellsworth:** Yeah, exactly. I just don't want to get into the yelling over each other match here. Oh, yeah. Oh, that's half the fun. I know. I know. So, we look at, we'll take your argument, Dave, about the 8-bit micro a few weeks ago. As the technology gets better in our home, it may be 100 years out or 1,000 years out, you know, very simplistic devices are still going to have a purpose and a use. I totally agree. And as these two technologies cross, you know, as we can start manufacturing more complex stuff at home, you know, things that are useful as 8-bit micros will be possible. And then, they could be integrated into your kid's toy that's 3D printed and has some kind of, you know, built-in motor.

**Dave Jones:** Quite possibly. Exactly. But Chris's original claim was that it would happen, I think it was at 20 years. Chris, was that the original, when did we first argue this? Like, back in episode one or something, was it? I don't know. It was like 20 years. And I instantly, my bullshit detector went off and I just said, no, straight off the bat, it's not going to happen in 20 years. It's not going to be a revolution. Would you agree with that, Jerry? 20 years is just too soon. You just won't be able to imagine. That's probably a little aggressive.

**Jerry Ellsworth:** But, you know, in the 80s, I would have never imagined. A little aggressive. I would have never imagined I'd be carrying a computer in my pocket that I could make phone calls on. So, it was beyond my thinking at that time that that would even exist.

**Dave Jones:** Sure. But surely you can't make the stretch that, you know, it's taken, what, 50 years for semiconductors to get to the point where we can buy them and use them, you know, so massively cheaply and have such huge integrative functions in them. And to think that within 20 years, you're going to be able to make them at home using this massively advanced technology. I don't know. It's certainly not going to happen with silicon. No, I'll tell you that it's not going to happen with silicon, right? You've got to agree with that, Jerry.

**Jerry Ellsworth:** Sure. There's Moore's law. Now we should make up Chris Gammell's law. Ooh. Oh, Gammell's law. Yeah.

**Chris Gammell:** The Gammell hypothesis. Yes. Yes. Totally unproven.

**Dave Jones:** Yeah. Right. And totally unobtainium. Feeling completely made without obtainium.

**Chris Gammell:** Ray Kurzweil, and I'll just be coasting on some predictions I made 20 years ago and just keep on publishing and going on shows and everything else.

**Dave Jones:** No, seriously, it's not going to happen with silicon, right? It's just too, it requires too many advanced manufacturing processes. It might happen using some other, these new organic printed things or something like that. Perhaps that would, as far as I see it, that would be the only hope that you'd see something like the chip maker bot within the next 20 years. It won't be using silicon. No way.

**Jerry Ellsworth:** There's some issues with silicon. And actually, this is a point that I want to bring up because so many people ask me about doing this. Like, for instance, it's drop dead simple to make solar cells at home with this same process. Yes. But the thermal cycles to do all of the processing of the chips make it not worthwhile because you have to put in, you know, I don't know how many watts that is to run a furnace at 1,000 degrees C for six hours to do this. Yeah. That's not all. How is that? Yay. The amount of energy that this little solar cell is going to produce, you know, will never repay the amount of energy you put in to run this furnace. And that's where silicon really fails is the thermal processes are expensive. If you have a factory where you keep the furnaces up to temperature and you're constantly feeding wafers in there, you can get that cost per BTU down to, you know, fractions of pennies.

**Dave Jones:** BTUs, huh?

**Chris Gammell:** British thermal units.

**Dave Jones:** I know that's the unit that's used and commonly used in the industry, but it's so archaic, really, BTUs. I love it.

**Chris Gammell:** I think it's great.

**Dave Jones:** Yeah.

**Chris Gammell:** I love the conversions too. I've used it. It's like the stupidest number of conversions too. It's like 6,500, 400, you know, whatever it is.

**Dave Jones:** Right. I love it. Brilliant. Yeah. And that's the problem with solar cells on your roof too. You know, we've talked about this before, you know, what's the cost benefit thing of having solar power on, on everyone's roof, as opposed to having a huge solar installation somewhere, you know, it's much more. It's more cost beneficial to have a huge solar installation than actually manufacture all of these smaller solar cells for roofs. I think that's a different argument. I mean, I agree with that. It comes down to a similar thing in similar concept in the end, though, that it costs too much in terms of energy to manufacture these individual solar cells. You're better off spending the money and the energy manufacturing larger solar systems, basically. Yeah. Yeah.

**Jerry Ellsworth:** The argument's been made over and over again that if it wasn't for huge subsidies, solar cells wouldn't be all that lucrative. Yeah. Because it really is difficult to make crystalline silicon. And that's why there's so much research out there into, you know, polymers and amorphous silicon. And, you know, to make crystalline silicon, it's insane. You take sand and you throw coal into it, the thing that we're trying to reduce in the atmosphere. You melt this down to a huge slag. And then you dump it in acid and you dissolve it. And then this acid, you do a reaction with it that produces silane gas. And then you run it into these reactors that deposit out pure silicon on these long rods. And then you take that and you remelt it again. And then you draw it out into a boule. And then you zone refine it with these huge induction heaters. You know, the amount of energy it takes just to get to the point where you make your wafers is insane. And then you have to polish it and then do all the thermal processes.

**Dave Jones:** Yep. And then you start on the actual manufacturing process. Then you start on the printing processes, right? Yeah. It's just, that's crazy.

**Chris Gammell:** Have you guys ever seen the video of the slow motion capture of a boule being drawn out from a silicon?

**Dave Jones:** I think I have seen that a long time ago.

**Chris Gammell:** It is so cool. They start with a little seed. And it's just like an old, I think it's the tip of an old one. And then they dip it in there and then they rotate it really slowly and they draw it out. It looks like the way you would get like cotton candy out, you know, except it's amorphous silicon. Except it's way cooler. It's like thousands of degrees, you know? Awesome stuff. I'll try and find that and link that in the notes because, man, it's cool to see.

**Jerry Ellsworth:** There's a good set of videos out there on the Japanese semiconductor industry that goes into the history of how the Japanese copied all the U.S. technology. And it's very fascinating how they made a lot of shortcuts for like drawing these boules out. Things like huge buckets of water with a hole in the bottom of it where the water would drain out and there was a float thing that would follow the water as it drained out and that would pull the boule up. Really? Absolutely fascinating. Well worth finding it.

**Chris Gammell:** Yeah, I'll try and link that in too if I can find it. Fantastic. So I wanted to mention something.

**Dave Jones:** So is that enough of, well, go for it.

**Chris Gammell:** Well, actually I was going to, I wanted to mention something because we were talking about organic. There was actually an announcement yesterday or two days ago. There was the world's. You were telling the story. The world's first all organic processor. You guys hear about that? There's a story on Elector.

**Dave Jones:** No, I haven't seen it, no.

**Chris Gammell:** Yeah, it's on Elector.

**Dave Jones:** We've got the link here. Let me check it out.

**Chris Gammell:** Yeah. It's 45 on our list. Yeah. And so basically...

**Dave Jones:** And it operates at a massive six hertz. Yes, that's right. Six whole hertz. That's hertz, people. Yeah. Cycles per second. Yeah.

**Chris Gammell:** As opposed to gigahertz for standard ones.

**Dave Jones:** Or even megahertz, which is what the early micros worked at. You know, six megahertz was a hugely fast micro back in the day.

**Chris Gammell:** Yeah.

**Dave Jones:** And so that's actually...

**Chris Gammell:** That was before you were born, Chris? That's right. They were making that comparison. They're comparing it to the 4-bit 4004 from Intel.

**Dave Jones:** Oh, right. Oh, right. Yep.

**Chris Gammell:** And that was in 71.

**Dave Jones:** What frequency did the 4004 run at? Jerry, come on. You're the vintage processor expert, aren't you? Sorry. I don't know. You don't know off the top of your head. Oh, fail. Oh, come on.

**Jerry Ellsworth:** The early calculators ran very, very slow. In fact, I got some of these old 70s calculators and I would hook little piezo speakers up to them and listen to the whir of the processing. Oh, nice. Yeah.

**Dave Jones:** It was very much in the audio frequency. I think it was like 600 kilohertz.

**Chris Gammell:** Yeah. That's awesome.

**Dave Jones:** I think it might have been as high as 600 kilohertz or something like that. But I'm sure it was in the hundreds anyway, not down in the tens of kilohertz for the 4004. Although because it was a completely static device, wasn't it? You could run them at zero hertz. You can run them at 0.1 hertz if you wanted to. Yeah.

**Chris Gammell:** You flip it with a little switch. That's how you're clocking it. Yeah.

**Dave Jones:** You could actually.

**Speaker ?:** Yeah.

**Dave Jones:** I think all of the early processors, weren't they? Almost all of them were static devices. You could actually run them at. No.

**Jerry Ellsworth:** A lot of them. Like the 6502 was dynamic. You couldn't suspend the clock. Okay. I mean, that's how they saved a lot of spaces. You know, they just used the nodes between inverters to be storage lines.

**Dave Jones:** Okay.

**Jerry Ellsworth:** Or in between tri-state buffers, I should say.

**Dave Jones:** Hmm.

**Chris Gammell:** This is why I'm glad you're here, Jerry, because I wouldn't be able to call Dave on that one. I'd be like, oh, okay. Whatever. Hey, great job, Dave.

**Jerry Ellsworth:** Here's a fact of the semiconductor industry. It's much like the auto industry. There's this momentum going forward. Processors and semiconductor process has been done with optics and silicon for so long. And it's easier to do incremental changes to that process. That's why they've pushed lithography, you know, well beyond what they thought was possible. Oh, yeah. It's just, it's easier to do that than develop some other technology, say, with polymers. And, you know, polymer technology is kind of left universities and, you know, little startup companies trying to be aggressive. And so, of course, they don't have the funding of, like, Intel and other companies.

**Dave Jones:** Yeah, true. Well, it's probably like the early days of the silicon wafers, right? It just takes decades to get, you know, a decade plus to get these things to actually refine all of the processes before you can get to a point where you can make a usable part and stuff like that, right? So, exactly. It's, you know, they're starting from scratch, practically. They're going back to, you know, 1960 or something. It's very interesting. I have some. Well, not really. They have, you know. But still, it's a very, you know, when you've got a new technology, you can't just go, you can't just apply the old techniques that you use with silicon that you've been developing for 40 years, I don't think. Like, maybe I'm talking about my ass again, but I would expect if you start again with, you know, some flexible polymer thing, then it's a totally different ballgame.

**Jerry Ellsworth:** You know, it's interesting as I have these books. So, to develop my home process, I started going for older and older books. And I found books from the 60s and 70s where they talk about these processes that they tried. And it's very fascinating. Things that were tried were abandoned because, at the time, you know, they couldn't run 100,000 wafers per hour through a fab with that technology. But you're seeing some of this stuff go full circle and come back again. For instance, MetalGate on MOSFETs was abandoned in the 70s because of some limitations. And Intel, in the last three or four years, has switched back to MetalGate because polysilicon and silicides don't work for down at these really small feature sizes. So, now you're using refractory metals, all this stuff that was pioneered in the 70s but forgotten.

**Chris Gammell:** Right.

**Jerry Ellsworth:** I love it.

**Chris Gammell:** And now they herald it, too, as, like, the next big thing, too, right? Oh, right. Of course they do. Hey, Jerry, I wanted to mention, too, about the... So, you mentioned about using litho, too. And I saw a news story about Samsung hitting 20 nanometers. And I thought that was interesting because that means they're still using 193 nanometer wavelength on their optics. So, that's their base wavelength. And then they do the rest with basically water. And they play some tricks. And then they double pattern and everything. But I thought that was interesting because that means they're getting from 193 down to this 20 nanometers to get the smallest feature size. And that's the newest thing.

**Jerry Ellsworth:** It's amazing what they're doing with optics. So, for the mask sets to do below the wavelength of light that you're using to do the imaging, like, if you want to draw a rectangle, they're putting these serifs just kind of like a font. So, there's little dangly things that hang off of each of the... On the main master mask that's at the full, you know, the larger resolution. And then that's interacting with the light wavefront and twisting it around. And by the time, like, all this magic happens with these wavefronts, when it actually strikes the photoresist on the wafer, now you have these interference patterns that are causing, you know...

**Dave Jones:** Very cool. Very cool.

**Jerry Ellsworth:** Far below your wavelength of light patterns to be imaged. And that's why it costs a million dollars to have a mask set made. It's incredible. It's like... Every chip that I've worked on that's been, like, 65 nanometer and these really tiny ones, everyone is just sweating bullets the couple weeks while we're waiting for the masks to come back. Oh, yeah. For sample chips. Like, did it really work? You know, because there's...

**Dave Jones:** That's scary.

**Jerry Ellsworth:** There's so much processing. It takes weeks and weeks of computational power to figure out all these little serifs and features to put on to the masks.

**Chris Gammell:** Have you ever known anyone that was in charge of messing one up? I messed him up. Did you? Awesome. That's right. You heard it here first, folks. Don't blame me. I'm just a contractor. And now she makes videos.

**Jerry Ellsworth:** Yeah, exactly. I don't work on back end, but I've messed up designs that have made it all the way into masks. And then you start scrambling and you do engineering change orders and stuff. Yeah, the good thing is, you know, if you plan ahead and put uncommitted gates and different things onto your parts as a backup plan, you only have to change some higher level metal to fix a lot of these things.

**Dave Jones:** Right. So there's almost a get out of jail cheaper card, not get out of jail free.

**Jerry Ellsworth:** Yeah, and tens of thousands instead of hundreds of thousands.

**Dave Jones:** Hundreds of thousands. Nice.

**Chris Gammell:** So a little more difficult than adding a resistor here or there, right? Exactly. That's the stuff I'm used to.

**Jerry Ellsworth:** One of my chips I designed, this was actually a set of cheap mask sets, but I fixed it out in the field because I forgot to reset a flip-flop and it would power up randomly and it didn't show up in my simulations. And so there was a test pin on there for JTAG. So I just toggled the test pin before my master reset and I was able to get in there and reset that flip-flop to the state I needed. So I was sweating bullets over that. I wanted to run to Mexico because there was so much money on the line. Oh, my God.

**Dave Jones:** Sweet.

**Chris Gammell:** Oops.

**Dave Jones:** Speaking about companies and stuff like that, you mentioned before the show, Jerry, we were talking about warm, fuzzy feelings about companies because you're going to be doing some work for a company very shortly who probably has one of these warm, fuzzy feelings. Or maybe not.

**Jerry Ellsworth:** Or maybe not.

**Jerry Ellsworth:** So I've been talking to Intersil. Remember that old company from the 70s and 80s? From the 70s. Yeah. Intersil.

**Chris Gammell:** They make transistors or something. Is that right?

**Jerry Ellsworth:** See, unfortunately, no one knows what they make because they're one of these companies that got bought up by some big monolithic company and lived under the umbrella of this large company for a while. And kind of vanished, really. Languished in the mindset.

**Jerry Ellsworth:** Is that the right word, right?

**Speaker ?:** I don't know.

**Jerry Ellsworth:** And now they've been kicked out and they've spun out on their own. And now they're struggling to be seen because no one thinks, you know, to design in Intersil parts. No. We all have our warm, fuzzy feelings about national or linear technology. Or Maxim.

**Dave Jones:** Who everyone's famous for having a warm, fuzzy feeling about. But in that case, it's, you know, once bitten, twice shy. But yeah, I mean, I wouldn't think Intersil. I, you know, I just get the impression, yeah, they're that 70s company who got bought up and, well, they don't really do anything. It's just a shelf company now. That's the industry slant that I get from Intersil. So, yeah. Yeah, they need some good marketing, I guess.

**Jerry Ellsworth:** Yeah. So, I'll be helping them out doing some videos. And we're going to do a really cool project. Maybe I should keep it secret until another. Yeah. Yes, definitely keep it secret. I haven't signed on the dotted line that I'll be doing it yet. But it looks like it's going to happen. And it should be a lot of fun.

**Dave Jones:** Yeah. That sounds like fun. So, if anyone else has got a warm, fuzzy feeling out there about companies, tell us. Leave a comment. Which company do you have? You know, you just don't touch because you don't really know why. Or, like, either you don't touch or you use all the time because of just a warm, fuzzy feeling that engineers get, really.

**Jerry Ellsworth:** I think some companies just fell into this on accident. Like, I don't know why I feel so strongly about Altera. They've never, like, given me any love or anything. In fact, they've kind of ignored me a lot.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** But yet, I keep designing, or for years, I've designed their stuff in.

**Chris Gammell:** Yep. Yeah, got to get them young. That's the problem, you know. And that's why they give kits to schools. And it's smart when they do, you know, donating to education and everything else. It's damn smart because you grow up learning about something or using something the first time. And you just keep using it. I know that's, I've seen that before.

**Dave Jones:** And I wonder if that's the reason why a lot of, a few companies are trying to jump on the, you know, the hacker-maker bandwagon now with their chips, you know, with their micros and stuff like that. And it's brilliant if they do. Whether or not they actually understand that warm, fuzzy feeling that people grow up trusting, you know, some particular brand or something like that. You know, if you grew up with, you know, your first micro was a pick or something like that, you're going to have a warm, fuzzy towards picks for most of your career unless they piss you off in some way, really. You know, it's the same thing with other companies. And that's how Pick made their big thing, I think, is that they started out, they were the only ones who would, you know, really do sort of, you know, really entry-level micro sort of stuff. The others just didn't care about that sort of thing.

**Jerry Ellsworth:** I think you hit a nail on the head there, Dave. You should, or these companies should be giving out developer kits and free samples like it's candy.

**Chris Gammell:** Oh, yeah. Yeah, I know. You think about it, like, and we might have talked about that on here before, but you think about how much they spend on, like, advertising. At a certain point, it's just more economical to give this stuff away to people that will use it, you know, and then they're going to tell their friends.

**Dave Jones:** Or advertise on our show. Sorry. Oh, don't forget that. Waving my hands here. No, they must. Yes, no, advertising is important, but it's got to be at the right end of the stick.

**Chris Gammell:** Well, we can hand out these kits. I mean, who cares? We'll hand them out to people. Awesome. Yeah, I mean, but I really do believe that. I think at a certain point, you know, giving kits to people, you know, get them in the hands of people who will either learn on them or develop with them. Yeah. That's money.

**Jerry Ellsworth:** Or maybe not even develop anything with them. Just that, like, hey, this company went out of their way and gave me something. Yeah, exactly. I couldn't use it, but.

**Chris Gammell:** Yep. That's true. That's, like, that's a very basic human thing, too. Like, when people are selling stuff, they always try and, you know, give you something, even if it's something silly like a pen, because then you feel obligated at some level, which is weird.

**Dave Jones:** Hey, well, I'll tell you what. Back before your day, Chris. I'm so young. Data sheets. Data books were the big thing. You know, if a company gave out that some companies were so strict on giving out data books that you just wouldn't touch them. Whereas the ones that would give out the data books like candy or they'd sell their data books in the local stores and stuff like that, you ended up using their parts. Because this was, you know, pre the internet and, you know, all that sort of stuff. So you really had to design. The only info you had was in those data books. And if you've got, you know, national data books on your bookshelf, well, you're going to be using their parts, right?

**Chris Gammell:** Yeah.

**Dave Jones:** It's just, and it's a similar thing these days.

**Chris Gammell:** Wait, what's it? Oh, you mean with parts these days, not necessarily. I don't need a data book, personally.

**Dave Jones:** With kits and things like that. Yeah. The companies that give their stuff away and put and get their stuff in the hands of people are the ones who will ultimately win, I think. So, yeah, my, you know, and, and even to this day in my bookshelf here, I keep TI and national data books because they're the ones who, you know, freely, they're the easy to access, easy to get data books back in the old days. And I, you know, even to this day, I still have a warm, fuzzy feeling about those companies because I happen to get their data books.

**Jerry Ellsworth:** So I think it's a big deal. There's some kind of nasty things about the semiconductor industry that I don't like as far as like trying to get information. There's the, the in-between sales reps between these companies that you have to interface with all the time to get a data sheet sometimes or get a sample part. And it's all about, you know, getting there. It's all about volume. Right.

**Chris Gammell:** And we're not talking about how loud Dave's talking today.

**Dave Jones:** No.

**Chris Gammell:** Talking about how many parts you set or how many parts are going to be designed in your products, right, Jerry? Exactly.

**Dave Jones:** That's the big million dollar question. Yeah. They always ask that. What's your volume? What, what's your production volume?

**Jerry Ellsworth:** And, and I've worked for companies that have that mentality where, you know, I've asked them, well, why don't you put these parts out so people can get them? And they say, oh, well, you know, we only want to go for the top tier companies like Sony's and stuff like that. They want to get the million chip sales and they don't, they don't get it that engineers like us will call out these parts when we go work for the Sony's and the big companies. That's right.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** And it's partly laziness and, and maybe lack of resources they want to throw at supporting, you know, the questions they're going to get by putting these parts out there.

**Chris Gammell:** Yeah. And to be honest, the, and that's kind of the old model, right? I mean, that's kind of how they always had to do it because you have, if you have 10 sales people, then you, or 10 reps or whatever, then you can only, you know, have them cover if they get five accounts each as 50 accounts, right? So you're going to get the top 50. But the nice thing is that you can hire nice people like Jerry or Dave or, or the amp hour because I don't do videos myself, but you know, and you can, you can do social media type stuff and boy, if that's not a plug, I don't know what is.

**Speaker ?:** Yeah, exactly.

**Jerry Ellsworth:** I think sales reps, you know, should go the way of the dodo. I mean, that's just so, you know, outdated.

**Dave Jones:** Yeah. It's so, okay. It's just in today's when everything's available online and here's the rant I wanted to do. It comes up on the forum all the time. People are pissed off at these companies who make you sign an NDA to get a freaking data sheet. Give me a break. Are you talking about unreleased? I am not going to, I'm going to boycott not only that part, but I'm going to boycott your freaking company because you're, you pissed me off.

**Jerry Ellsworth:** Yeah.

**Dave Jones:** Engineers are fickle. Don't piss us off like that. Say NDA to get a bloody data sheet. Are you talking about your break time? I've had to go through like a local rep who will just give me the data sheet on the sly because they also hate the, you know, the thing that you have to sign an NDA just to get the data sheet. So here it is. Psst, psst, buddy. Hey, you know. Want to buy a data sheet? Want to buy a data sheet with the trench coat and the whole. Yeah. It's just bullshit. Give me a break. Those companies deserve to fail. End rant. What else have we got on today's list?

**Jerry Ellsworth:** That we should keep sales reps around.

**Dave Jones:** Oh, well, yeah. That's about the only good thing I've found.

**Jerry Ellsworth:** Okay.

**Chris Gammell:** So. Are you talking about companies that, is it like for an unreleased part? Is that what you mean? I don't know.

**Dave Jones:** No, no. No, no. These are just regular parts, but they just deem them to have proprietary information in them or some crap like that, you know.

**Chris Gammell:** But you could get the data sheets online or no?

**Dave Jones:** No, no. I can't. There's a link there that says download data sheet and then, you know, you hit it and then it says, oh, you have to sign an NDA first, you know.

**Chris Gammell:** Sign an NDA, not just sign up for a, the site?

**Dave Jones:** No, no. It isn't just sign up for the site. No. You've got to have, sign up for an NDA or you've got to contact. Some aren't like an NDA, but you've got to contact them and then they will suss you out whether or not you're worthy to have their data sheet.

**Chris Gammell:** You're talking about the sales funnel. Yeah.

**Dave Jones:** Yeah, right. Yeah. You're in the funnel now. Yeah. I mean, they're sucked into the funnel. Well, I just don't enter the damn funnel. That's a great description of it. It really is.

**Chris Gammell:** You can shove your funnel right up your backside. That's what you can do. That's the one that, that's, that's what they call it. If you didn't know, that's what they call.

**Dave Jones:** Oh. Yeah. Yeah. That's a real term.

**Chris Gammell:** Yeah.

**Dave Jones:** Nice.

**Dave Jones:** It is. Yeah. It's a real wank term. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Speaking of that sort of stuff. Oh. Very similar thing, which somebody mentioned when I did the review of the latest Fluke 87 meter. This, they actually gave me a pre-production meter to actually review, which was awesome, which fixed the GSM issue. Anyway, I noticed that they had removed the patent marks off the back of the meter. You know, if you own a Fluke 87, if you have a look on the back, it has, you know, this is covered by X patents and it had like two or three patents on there. But the new meter doesn't have it at all. They've actually removed them. Um, and somebody mentioned that, um, you can actually get fined for putting expired patent numbers on a product. You can get fined like a hundred bucks per item or something like that. So if you sell, you know, 10,000 multi-meters, you, you can be, uh, you know, you can pay like a hundred dollars per item as an infringement kind of thing. So, um, and, and I've actually had that confirmed that it's not, you know, it's not into law, but, but you can actually get sued for putting fake, you know, expired patent marks on things. So yeah, companies have to be careful. Um, that's, I'm not sure how I got onto that, but anyway.

**Jerry Ellsworth:** I wonder how that applies for patent pending. Everyone puts patent pending.

**Dave Jones:** Everyone puts patent. No, this is like expired. Yeah. This is when the patents come to the end of their term. Like, you know, these are probably old flute patents, you know, 20 years old or something back in the eighties when they actually designed, when they were leading in multi-meters and started, they were doing all this innovative, you know, ASIC stuff and things like that. So do either of you guys have patents? Yeah, it's interesting.

**Chris Gammell:** I don't know if I've ever asked you that.

**Dave Jones:** I've, I've got one technically. Yep. And I, technically I had another, uh, uh, one that was a patent pending as well, but yeah.

**Jerry Ellsworth:** I went through the process. You know, me and patents. None of mine were issued. It's a, it's a long drawn out, annoying process.

**Dave Jones:** Yeah. Yep. I've got, I've got one that was issued and one which was a patent pending, which my brother-in-law, who's a patent attorney, talked me into, oh, you've got to, please, I can write your patent for this. Oh, all right. I'll humor you, you know, write me a, write me a patent for it. And yeah. Oh dear. Never again. Hate patents. Unless I come up with such a cool, massively innovative industry changing idea that, yeah, maybe.

**Jerry Ellsworth:** So I ran into a bunch of fluke guys up at a pinball show in Seattle and they set me up with a bunch of fluke, uh, gear. I can't remember the number off the top of my head, but it's a really nice meter.

**Chris Gammell:** Yeah. I saw that in your video, right?

**Dave Jones:** Yeah. They're like, whoa. Oh, that's yeah. You've got the fluke 289, I believe there, Jerry, I saw in your latest video. Sounds right.

**Jerry Ellsworth:** Uh, they're like, well, we're, they said, we're tired of seeing you use these $2, um, volt ohm meters. Right. And I told them, I said, well, I'm still going to use the $2 volt ohm meters because, you know, I don't want people to think that they have to have an $800 meter to do, you know, something where 10% accuracy is fine.

**Jerry Ellsworth:** Yeah.

**Dave Jones:** Yeah. That's what happened when I first started my blog. I was using, oh no, I was using a fluke actually. I was using a fluke 87, but, uh, uh, the German company, um, came along and they just went, well, we don't like you using fluke. Use our meters in your videos. You know, here's an expensive, you know, $800 Gossen meter. Well, thanks. Okay. I'll, I'll use yours in the videos. You know, I'll, I'll, I'm a bit of a whore that way. I'll use the most expensive bit of gear I've got on video. I, I don't need to make a statement that, you know. Yeah. Because I, I, I say it all the time, you know, horses for courses. You use the tool that's, you know, you use a tool that's right for the job if, you know, and you can get away with using a $10 meter if you want.

**Chris Gammell:** Jerry, you should have turned to them and been like, uh, I made these in my kitchen. 10% accuracy, probably going to be enough. Good enough.

**Jerry Ellsworth:** Exactly, exactly.

**Chris Gammell:** Man, that's, I want to see, I, I had a couple other questions for you about the, about those. Where did I put these? Uh, so you said you, you, I wanted to ask you about the, how you did the masking. You said you did that with vinyl tape. Would you ever do that with photo at all? Like any kind of photo lithography or anything like that? Even real?

**Jerry Ellsworth:** I've, in the past, yeah, in the past I experimented with that and had, uh, some failures. There's, there's a lot of steps to doing, uh, photo processes on semiconductors because the surfaces get a little funny sometimes. Sometimes you have to grow oxide over the bare silicon. So it's, uh.

**Chris Gammell:** So it'd fall over, right?

**Jerry Ellsworth:** Yeah, yeah. Because silicon's kind of hydrophobic and, uh, bare silicon.

**Dave Jones:** That's a great word. I'm sorry. Hydrophobic. Hydrophobic. That's just, it's a brilliant word. Word of the day.

**Jerry Ellsworth:** Yeah. And so I, I didn't have a lot of luck. I tried a little bit this weekend and didn't have much luck with it. I, I, the bottle of photo resist that I have says shelf life six months and it's probably three years old. So that could explain far from. So I may have to regroup and reorder. But then you still work, won't it? It just takes a bit longer? Is that the, I, I probably. Is that the deal? I don't know. The, the traces just fell off, but. Yeah. Chances are. That's great. It was three years old when I bought it. So. Yeah. So yeah, the vinyl sticker actually works very well and you can make transistors that work with huge channels on them. And people often ask me, why do MOSFETs at home? Why don't you do bipolars? Actually, you know, bipolars are a little bit more difficult at home because you need a furnace that's very accurate because you're doing a diffusion to, to make your emitter and collector meet the base in the middle, but you can't overrun the two or you'll have no base left. And that's a thermal process, a thermal plus time process. And it's much easier just to grow oxides for a MOSFET and just look at the color of the oxide to know that you've got the right thickness. Yeah.

**Chris Gammell:** Man. Yeah. I really like that curve tracer you used too. I thought that thing was awesome. The old school curve tracer.

**Jerry Ellsworth:** Oh, I love, I love curve tracers. Yeah. Tech 575.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** Classic. It's great because I can just hook anything up to it I want, like a power supply and, you know, drive the gate to a negative rail way farther than it's, it's the 575's rating. I don't have to worry about it because it's all vacuum tube. Take that.

**Dave Jones:** Tubes.

**Chris Gammell:** Tubes.

**Dave Jones:** And it actually warms up the shop in the middle of winter, right, Jerry? Exactly. But the furnace does a good job of that. Right, yeah. Very inefficiently, but nah, well.

**Chris Gammell:** So, uh. Bonus. So we, uh, we've been doing, Jerry, have you, have you listened to the latest episodes? I remember you said you were listening to older episodes a while back. Have you heard any of the most recent ones?

**Jerry Ellsworth:** Uh, probably within, uh, a week or two.

**Chris Gammell:** Oh, okay. So, yeah, we started doing This Day in Nerd History. Have you heard that one? That new segment? Okay. So we actually have one. And we have one that's kind of relevant today. So we talked about the 4,000. Yeah, we did. The 4,004 is the, uh, we talked about how the.

**Dave Jones:** 4, 4, 4, 004.

**Chris Gammell:** 4, 004. Oh, God. Here we go again. 4, 004. Yeah. Okay.

**Dave Jones:** Triple five.

**Chris Gammell:** Triple five.

**Dave Jones:** Yeah. Eight. The 8088. Eight. Not the 8088, you know, and the, and, and it's the 8080, not the 8080. So, yeah.

**Chris Gammell:** Sorry, Chris. Whatever, man. I, to each their own, you know, that's, that's fine. I don't care. All right. Anyways. 4,004. Yes. 4,004. Uh, it, today in history, uh, 1968 Intel Corporation was incorporated. So, that was, uh. That's pretty huge. Yeah. And interestingly, uh, I, I didn't know this. Andy Grove is apparently a Hungarian immigrant. I mean, this is just the, the thing I found about it. But he was the founder of Intel and he's a very big advocate for the industry still. And, uh, you know, rest is history from there. 4,004 or four, what do you call it? 4,004. And then they went on.

**Dave Jones:** 4,004.

**Chris Gammell:** 8,008 and everything else.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. You know. Now you're learning.

**Dave Jones:** Lots of good engineers come out of Hungary. It's a, you know, lots of good software programmers. I think we talked about this before. There's the, there's the Hungarian method, which is a method of programming. I've never heard of that. Um, which comes out of. We talked about that? Yeah. I think you could. Yeah. I, I've mentioned it somewhere. Oh, maybe it's on one of my live shows or something like that. I mentioned it perhaps, but.

**Chris Gammell:** Yep. Care to expound upon it?

**Dave Jones:** And, um, uh, Charles, um, Charles Simonyi, if I pronounced that correctly, who's, um, if you've heard of him, if you follow the history of Bill Gates and Microsoft, he was their key software architect back in the very early days. And he did windows and, you know, office and all that sort of stuff. And, um, yeah, he's from Hungary, I think. So, and he, he wrote a seminal paper on, um, on, you know, some programming methodology or something. So that's apparently why Gates hired him. And, and apparently it didn't work that well, but, um, he was a shit hot programmer anyway. So they, so they went with it. Yeah. Talent overcome, uh, talent overcame theory there, I think. So anyway, lots of, yeah, lots of good engineers come out of Hungary for some reason.

**Jerry Ellsworth:** So, uh, one of the first products that Intel made was, uh, dynamic memories, which were, uh. It was. And, uh, they were able to make more dense memories because they came up with this technique of, um, annealing the oxide layer or the, the, the layers over the metal. If I'm, oh, maybe over the polysilicon to smooth it out. So there wasn't sharp edges. So that was like their big thing and, and gave them a huge advantage over all the other, uh, chip manufacturers of the time.

**Chris Gammell:** Yeah. I can't imagine. So you were talking about how you, the, I'm a, I figured your, was it Peter? That was your mentor's name?

**Jerry Ellsworth:** Mm-hmm.

**Chris Gammell:** Uh, I just.

**Jerry Ellsworth:** And I'm sorry, Peter, if you listen to this, I, I cannot say your last name.

**Chris Gammell:** It's okay. It keeps them anonymous. That way people don't come bug them about, they can come bug you now about, about processing tips instead of him. Right. Exactly. There you go. Yeah. Yeah. So I, I talked, so I used to work in a fab and I talked to the guys there, you know, about, you know, old war stories and stuff. And they told me about just like how the processing used to be there and just how incredibly noxious the entire environment was. They'd be like these open etched chambers and everything else. Nice. Nice. I just can't even imagine like back then, you know, like you see the first transistor too, that, it was a Shotkey that worked on that or, and a couple other guys. Barden, Shockley, and, uh, oh God, who's the third dude?

**Dave Jones:** Come on. Bardeen. Thank you. Bardeen. Yes. So yeah, you. Who didn't like each other apparently. That was, there's the famous photo of the three of them. Punching each other. You know, standing there over the microscope, you know, like they're, you know, they're standing there over the microscope. One of them's looking in. I think it's Shokky or someone looking, oh Bardeen, looking into the microscope and the two others standing there. Apparently that's the only time they wanted to be in the same room together. They apparently hated each other or something like that. So the, so the story goes. Anyway, a bit of trivia there.

**Chris Gammell:** That'd be funny if that was, you ever seen that Farside comic where they talks about like scientists playing jokes upon each other and they show like the guy dropping acid under the other scientist's neck. All right.

**Dave Jones:** No, I haven't seen that one. Cool.

**Chris Gammell:** Jerry, you can do that once you're done burning yourself with hydrofluoric acid, right? Exactly. Hydrofluoric acid. Watch this. I'll play this trick on Chris. Just get a fly to Cleveland, of course, in order to drip acid on my neck, but you know. Any, what was that? I don't even know. Oh, just the noxious environment. Yeah, it was, I mean, it seems.

**Jerry Ellsworth:** Well, a lot of those places are super fun sites and for those that don't know what a super fun site is, that's where the US government comes through and cleans up all the toxic chemicals they dumped right into the soil. It's amazing. Rumor is that the old Fairchild plant somewhere in Silicon Valley is just like all boarded up around it and it's completely toxic.

**Dave Jones:** Glow in the dark, huh? Exactly. Yeah, well, back in those days, there was no occupational health and safety. There was no EPA. There was, you know, you just got away with anything, really.

**Chris Gammell:** Maybe. These days, everything's so, you know. Maybe Andy Grove started Intel just as a front and now with all the radiation and chemicals he's exposed to, he's actually a superhero. I was going to say, he's a superhero. Is it?

**Jerry Ellsworth:** With a superpower. Silicon man.

**Chris Gammell:** Yeah, the incredible nerd. Our hero. Yeah.

**Dave Jones:** Fights for truth, justice and the nerd, why? Oh, love it.

**Jerry Ellsworth:** So guys, I listened to podcasts a couple weeks ago where you were debating the advantages of software-defined radio.

**Dave Jones:** Yes. Did you want to cover that real quick before we run? Yeah, we were talking about you. Oh, I don't know. Yeah, very, very quickly if you want.

**Jerry Ellsworth:** Yeah. So you guys were debating, you know, why do software-defined radio.

**Chris Gammell:** And I totally botched it.

**Jerry Ellsworth:** I wanted to jump out of my vehicle as I was listening to that.

**Dave Jones:** Yeah. Well, my comments were based on no knowledge at all of software-defined radio. They were just based on, you know, things I'd, you know, just things in the, just hunches, really.

**Chris Gammell:** People were asking on Twitter, too, did you hear our crankshaft, camshaft mix-up? They thought that you might have actually crashed your car when you heard that one.

**Dave Jones:** You crashed your car when you heard that, yeah. I saw those comments. Funny. Yeah. Anyway, software-defined radio.

**Jerry Ellsworth:** Tell us. Okay, so, yeah, I'll try to keep it brief since we only have three minutes. Yeah, but... So for years, we've had crystal sets and regenerative receivers and super heterodyne receivers. And, you know, they worked great. And you could tune any frequency you wanted with them, pretty much. But in the last couple decades, we've had the advantage of high-speed digital signal processing where we can eliminate a lot of the analog circuitry and do it mathematically inside of a DSP or a CPU or an FPGA. FPGA. And the huge advantage of doing this over, say, a super HET receiver is there's a lot of advantages. But one is that once you get everything into the digital domain, there's very little phase errors. There's no phase errors that you have to deal with. So in a lot of ways, you can do processing in a very perfect way. And other... Some other advantages... Perfect way.

**Dave Jones:** Sounds very utopian.

**Jerry Ellsworth:** All right, maybe I'm not describing that right, but it... More precise.

**Chris Gammell:** I understand what you're saying. Yeah, there's less physical effects in order to deal with.

**Dave Jones:** No, is it actually... Is it more of a... Let's say from a power perspective, which would be a more power-effective approach?

**Chris Gammell:** Digital.

**Dave Jones:** Is there a huge amount of processing? I assume a huge amount of processing required, DSP processing. Well, when I say huge, not a room full of DSPs, but a fair bit of crunch in there.

**Jerry Ellsworth:** All right. I'm going to have to pull some of this out of my behind, but... That's what we do here on the AMPL. Exactly.

**Chris Gammell:** We've done it for an hour so far, right?

**Jerry Ellsworth:** Yeah. Since I can't qualify how much my FPGA is consuming as far as current, but... So in a super head receiver, you almost always have a front-end amplifier, which is a smaller amplifier. And then you go into a mixer stage. And then the following stage, you have very steep filters and very aggressive filters. And your intermediate frequency has to have a very, very strong amplifier. And so a lot of times, your intermediate frequency will be... Our intermediate IF amplifiers will be consuming tons of current to be able to drive all these crystal filters.

**Chris Gammell:** Yeah, that's a lot of bit-flipping. Or a lot of flipping, right? Yeah. Moving around, at least.

**Jerry Ellsworth:** With software-defined radio, you don't have to have a front-end amplifier at all. Sometimes you don't even need to have a front-end bandpass filter. So there's very little insertion losses for things like filters. And then when you do direct conversion, you go directly from RF down to a very low intermediate frequency. So that means that you're using amplifiers, which are just off-the-shelf op-amps and instrumentation amplifiers that work in the kilohertz range. So your amplifiers are simplified. And your filtering is now closer to the analog frequency. So you do everything with R's and C's. So just RC filters. So you don't need to be consuming all that power. So now the question is, once you digitize that and get that into the FPGA or CPU or whatever, does the CPU do that efficiently? Take more than...

**Dave Jones:** Yeah, exactly. I don't know. It's an interesting question. If somebody knows, let us know. There is... If you've got some numbers on that.

**Jerry Ellsworth:** There's different ways you can do the processing in the FPGA. So there's more aggressive ways. The way I did it in my video is I did it a more aggressive way where I did a Fourier transform and I converted all this data into the frequency domain. Then I did my work on it. Then I transferred it back into the time domain as audio. So you can actually do... I think it's called phasing. So you can do this digitally and it's a simpler way to do the processing but less flexible.

**Dave Jones:** So do you have to do it in the frequency domain or can you do it still in the time domain as you actually capture it?

**Jerry Ellsworth:** You can do it in the time domain or frequency domain. There's processes. Right. But as you start making fur filters with multiple taps, it becomes increasingly difficult to make really good fur filters. So at some point there's a trade-off to go from time domain into the frequency domain. Right. Got it. So... Yeah, yeah. So... And there's some other advantages too as far as you're not throwing away as much information when you're doing the down conversion. So... Okay. With a superhet receiver, you're throwing away 50% of your information. And with a IQ, it's what is called a in-phase and quadrature direct conversion receiver, you get twice the bandwidth to work with and twice the information. So you can do image rejection inside the FPGA and you don't have to have these aggressive filters. I don't know if that's making sense. I'm trying to condense down a very complicated subject into three minutes.

**Dave Jones:** No, that makes sense to me. I think there's...

**Chris Gammell:** It's a tough thing to do because if people know about like baseband shifting, that's a big jump right there, right? I mean, you have to try... If you try and step back and say, oh, well, you multiply frequencies and everything and it shifts down to baseband, that right there is a huge concept in itself. But if you say, okay, you do some magic, you know, not magic, but you do something and then you're processing more audio and you're doing it in the digital domain, then it's like, okay, well, it's kind of hand-wavy, but it'll probably get you to the point where, you know, you say, this is the important part of radio. Learn this later and let's move on. Right. Right.

**Jerry Ellsworth:** It's kind of sad. I made this video. I put a full like month into this video. I mean, really hard work to make this thing. Wow. And, you know, my time limit was...

**Dave Jones:** You work too hard on videos, Jerry. I know.

**Jerry Ellsworth:** I'm telling you.

**Dave Jones:** I know, but it's fun. As a fellow video blogger, you spend far too much time producing videos.

**Jerry Ellsworth:** Well, part of this video is a middle finger to a certain company that some of their engineers treated me really badly during an interview. Take that. Yeah, I pretty much just came back and made the circuit that they were super critical about.

**Chris Gammell:** That's so awesome. I love that. I think that is so great. So up yours. Yeah, I hope they watch that and they're like, oh, wow. I hope they don't say, well, we should just use that then. No.

**Jerry Ellsworth:** It's kind of sad. I put all this work into it and it's kind of lost on a lot of people. They don't quite get the coolness factor of it, which is a little disappointing. Like the simplest things I do sometimes, like gluing a Nintendo and a video screen to a purse gets all the attention. And then these really cool things get no attention.

**Dave Jones:** Complex, you know. Well, that's the thing. Everyone's cool idea of cool is different. That's just human nature. There's nothing you can do about it. Like some people like some of my videos, some hate them. You know, it's like.

**Chris Gammell:** Well, I think it's more of a. Can't please everyone. I mean, it's almost beyond to the point where like they don't understand the significance of it, right? I mean, there's.

**Dave Jones:** Yeah. But even what should they? And that's the other question is, you know, should they have to understand the significance? Some people just don't care about that particular subject or thing. Should they? Should they have a loaded question? They just couldn't give a toss. Yeah.

**Jerry Ellsworth:** But the amp hour listeners would certainly think it's interesting and get it.

**Dave Jones:** They would be intelligent enough to.

**Jerry Ellsworth:** Because they're higher caliber than the average Joe.

**Dave Jones:** Well, I mean. Right. Than the average. Than the average YouTube. That's true. Oh, my.

**Jerry Ellsworth:** It doesn't take much.

**Chris Gammell:** Yeah. I mean, I've been saying for a while, too, that if people haven't seen. Go to Jerry's Jabber channel. That's where the real good stuff is. Because she's actually showing how you're making it instead of just the result video. I mean, I really like the Jabber videos better. Because it's. You know, even if you try and fail something and you tape that. That's. That's just as good to see, I think. Jerry.

**Jerry Ellsworth:** Well, my other channel. I also try to show how it's done. But it's more. It's more perfect. It's like I leave out all the failures.

**Chris Gammell:** It's the cooking show. Right. It's like. Oh, right. And so we put it in the oven. And then 35 minutes later, it comes out looking perfect like this. Right. Yeah. That's the cooking show thing. You know.

**Jerry Ellsworth:** And it's interesting. Some people get really pissy with me if I put that stuff into my regular channel. It's like, well, you didn't. You didn't actually show the completed project. You only showed part of it. And it was like really frustrating.

**Dave Jones:** You fell for their trap. You made the mistake of listening to them, Jerry. I know. I know. And then you spun off a new channel. I think the new channel is great. I think it's great.

**Jerry Ellsworth:** Give them the middle finger and tell them to stick it. Yeah. I think it's working. I mean, I see where some people are just passively interested in the final result. And they don't want to know, you know, how many times I melted my bones with hydrofluoric acid. Did you do that? I heard about that.

**Chris Gammell:** Jerry Ellsworth, now without hands. Exactly.

**Dave Jones:** Mutant. Yeah. Two nubs up.

**Jerry Ellsworth:** Yeah.

**Jerry Ellsworth:** Yeah.

**Jerry Ellsworth:** Yeah.

**Dave Jones:** Should we end the show on that?

**Chris Gammell:** We're already six minutes over. Yeah, we're a bit out. I did go and check. I don't know if people could hear me leaving or see me leaving. But our video did cut out. So you get about 15 minutes of just a... We'll just put Jerry's screenshot up there and just hold it up for the rest of the show. But yeah, who cares? We appreciate people paying, you know.

**Dave Jones:** I don't think anyone watches the video anyway, do they?

**Chris Gammell:** Thanks for being patient to people who do watch the videos. You know, whatever. We appreciate everybody who watches or listens.

**Dave Jones:** And we do have a proper Ampower YouTube channel now. Yes. So if you want to subscribe to The Amp Hour YouTube channel, that's where the videos will be. I will not be uploading them onto my channel now because, well, I think it just annoys people. Yep. I agree.

**Jerry Ellsworth:** Oh, don't listen to them, Dave. Don't listen to them.

**Dave Jones:** Oh, there we go. I'm not going to listen to them. But you can't have it on YouTube twice. There you go. It's got to go in one location. So... Fair enough. I think it's better if we just have our own separate channel. And people can subscribe to that if they want to or not. You shouldn't start a second channel, Dave. No, you shouldn't start a second channel.

**Chris Gammell:** Man. But considering that this is a joint feature... I'm going to be fun of Dave more when you're here, I think.

**Jerry Ellsworth:** Right. Bad influence. And it always fails. Yeah, well. It's always an epic fail. Well, thanks for having me on, guys. It was great and fun. It's always a blast.

**Jerry Ellsworth:** Thanks for coming. Sorry for walking over the top of you guys so much.

**Chris Gammell:** Walking over the top.

**Jerry Ellsworth:** No, that's the whole idea.

**Dave Jones:** Okay. All right, well... And, of course, I win the chip maker thing. To be continued. To be continued. It's just garbage.

**Dave Jones:** It's just not going to happen, dude.

**Jerry Ellsworth:** If I'm doing it at home, it's going to happen everywhere.

**Dave Jones:** Yep.

**Jerry Ellsworth:** Right. Right.

**Dave Jones:** Thanks for joining us, everyone. Thank you. Thanks, Jared. Bye.

**Dave Jones:** Bye.

**Speaker ?:** Bye. Thank you.
