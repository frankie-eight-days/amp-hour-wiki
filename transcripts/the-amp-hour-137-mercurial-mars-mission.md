---
episode: 137
title: Mars, System Design & NAND - Mercurial Mars Mission
url: https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/
---

**Chris Gammell:** This is the Amp Hour Podcast, recorded March 19th, 2013. Episode 137, Mercurial Mars Mission.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life. What's up, Chris? Happy St. Patrick's Day to you, Dave. Well, that was yesterday. I know you're not a green beer drinker, but some of us are. Yeah, no, I don't do anything like that.

**Dave Jones:** How many listeners do we have from Ireland?

**Chris Gammell:** Oh, I don't know. I should check that. Do we have a stat on that? Do a little soft shoe. I can look it up real quick. Oh, go for it. Do your thing. Live here, what? What's new in Australia?

**Dave Jones:** What's new is that I'm pissed off.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Oh, man. I can't believe it. I spent hours shooting this teardown. And there were like 80 clips or something. Well, there were like 100 all up or something. But after the 20th clip, the stupid camera decided to corrupt all the files. Oh, man. And I didn't know. I'm pressing record. The record button comes up. Everything's fine. Like, I trust my camera. I've done hundreds of videos with it, right? And no, then I walk over the computer happy. Oh, yeah. Just finished my teardown. Ha-ha. I'm going to edit this thing. And I stick it in. And I copy all the files over. I put them in my editing program. And I go, where's the rest of them? And it turns out, no. It didn't save like 80 of the clips.

**Chris Gammell:** Oh, man.

**Dave Jones:** And then, of course, I'm an idiot, right? I think. I've had like little quirks like this before. And I'm an idiot thinking that I can actually. It's faster to attempt to recover the files, you know, and do that than it is to just go and just go. Look, I give up. I'm just going to go reshoot the whole bloody thing, right? So I spent hours trying to recover the files only to discover that, of course, you know, they can't recover. Yeah, it got like 80 files back, but they're all mangled. They're chopped. The first thing, the start of them is all chopped off. And, you know, I, you know.

**Chris Gammell:** Yeah, you start wishing you knew how to like do software and like, you know, like bit wrangle and all that stuff at that point, right?

**Dave Jones:** Maybe. Yeah, because the data is like on there, right? Yeah, it's there in some form. But, yeah, I tried like two or three different. It's just shifted by one bit. Yeah. Exactly. I tried two or three different recovery programs. One of them found 80 files and I thought, oh, yeah, great. And then, you know, you delve deeper into it and, no, they're just no good. So after many hours, three, four hours of trying to recover this shit, I had to bite the bullet and go, nah, just give up. Just go reshoot the whole thing. Right.

**Chris Gammell:** And there is no version control for videos, huh?

**Dave Jones:** No. No.

**Chris Gammell:** I was thinking about version control today. I was thinking about like Dropbox and if that would work for actual version control. And I don't really think it would.

**Dave Jones:** It doesn't work for video because it's a bandwidth thing, right? I still use sneak in it. Oh, yeah, that's huge. I edit at home, right? Mostly. Sometimes I edit here. Yeah. And I tried to edit the teardown here the other day. But, yeah, so I've got to take it home on an SD card. Sneak in it. Oh, yeah. You know, I've got to. Yep. Yeah. It's the only thing that works.

**Chris Gammell:** What, did it get corrupted? Did your data get corrupted in transit? Did you get some water on it or something? Sweaty pockets or something like that? No, I'm pretty sure I know what happens.

**Dave Jones:** Because these DV cameras, these HD cameras, right, they save it in the standard file format for HD, you know, which is all in the directory structure. It's in stream and then it's in, you know, blah, blah, blah, blah, blah. And the camera, because it's got internal playback stuff for this, it actually generates, and for each video file, it generates an associated file that has like a thumbnail and everything else. You know, and like an index of how long it is. So I can replay them and all that sort of stuff. And I don't erase any of that. So when I erase the card, I just erase the video file. So all those existing other ones are in there.

**Speaker ?:** Oh, no.

**Chris Gammell:** So it associated them? Yeah. So that. Yeah, and it doesn't always do unique numbering either.

**Dave Jones:** No, exactly. Because that's the thing. If I erase the card, it starts from the unique numbering one again. Whereas if I just erase the video files, it just counts. The next video will count from $300.

**Chris Gammell:** See, that's why they should do like a hash or something. They should do like a CRC on like the date and, you know, like how many videos you've taken, you know, like a counter or something. But then you'd have to have flash on the camera or something. Oh, that sucks.

**Dave Jones:** And the other thing I hate about the camera is that I've been every month since I bought it, like, you know, I don't know what, two years I've had the bloody thing now or something. I've looked for a firmware update because it came with the original, like 1.0 firmware. And I thought, this is their top of the line camera, like prosumer camera, right? So, like, surely it would be the one that they, you know, do the most, pay the most attention to in terms of firmware updates to make sure it's, you know, professional and reliable and all that. No, they've never ever released a single... No, no, they've already sold it to you.

**Speaker ?:** Yeah.

**Dave Jones:** But they do it for other cameras, like little PCI-300 ones, right? They'll give you a third firmware upgrade, you know? But they won't do it for, like, they won't give you improvements on their top of the line camera.

**Chris Gammell:** They're still selling the hardware and everything?

**Dave Jones:** And they still sell it. Well, they just bought out a new one after two years, you know, but it's not much different.

**Chris Gammell:** That could put the kibosh on the updates sometimes, too.

**Dave Jones:** Yeah, but it was two years. Not a single firmware update in two years. That does suck.

**Chris Gammell:** That's the tough problem with all kinds of consumer stuff, right? I mean, it's like, at a certain point, you wish they'd just, you know, give you a disc and be like, you update it, you know? You write the firmware updates. Hey, holes.

**Dave Jones:** But that's their business, you know? You think they would have somebody, at least one person, dedicated to, like, just, you know, bug fixing and maybe, you know, adding the odd feature here and there, you know? No way, man.

**Chris Gammell:** Especially to their top-end gear. No, they'll just, you know you're going to buy another one in two years. You know, that long-term support stuff, that's a tough business to be in. I know. You know, like, when you're, because, you know, you don't ever get the friendly calls from someone two years down the line like you, right? You get the calls from someone from 20 years ago. Why don't you support me anymore? Oh, my God, I can't believe this.

**Dave Jones:** You need to do all this work now. I bought your universal programmer 20 years ago. Why don't you support the latest chips? So, you know. Yeah, exactly. You know? It's a tough problem, you know? It's a shit business to be in if you have to maintain all stuff.

**Chris Gammell:** It's not just consumer stuff, either. It's across the spectrum. No, no, no.

**Dave Jones:** It's hardware. It's oscilloscopes. It's whatever. Right, exactly. Yeah, yeah. Yeah. Absolutely.

**Chris Gammell:** And, you know, I mean, I'm sure many of our listeners know this one, too. Like, when you have to keep the build tools around, right? You have to, like, rebuild firmware or software. Oh, yeah.

**Speaker ?:** You know?

**Chris Gammell:** Like, you've... That's a tough business to be in.

**Dave Jones:** Yeah, you've got to keep an image of the disk from 1983 because they're the tools, you know.

**Chris Gammell:** Not even that. You have to keep the hardware because that disk from 1983 only works on an Amiga 500, right? That's right. Whatever you're using for a build tool. I had a... My old job, I had a computer in the next cube over that was sitting there humming along. It was some, like, you know, ancient Unix machine. But about every three months, the bearings on the fan would go out. So, it would start... Wee, wee, wee, wee, wee, wee, wee, wee, wee, wee, wee, wee. You know? It's just like... And what are you going to do? It's like, you've got to build with it. So, yeah. You keep it around. You shoot some lubricant in there and it quiets down a little bit. It chugs along. But those Unix machines, they keep going, man. That's great.

**Dave Jones:** Yeah, yeah, yeah. They stay up for years. Decade. Yeah. So, if I listen to... I would be interested in that. You know? What's that? Like, I had Windows, like, 3.1 machines at work that would be up for five years. Not a problem. It would only fail because the hard drive failed, you know? Yeah. I mean, or the power supply failed.

**Chris Gammell:** Well, a lot of times, if they're not on a network, that helps too, right? I mean, if it's a build machine on a network, that usually gets dicey because then, you know, newer computers want to talk to it and stuff. And then they can get crap on there.

**Dave Jones:** Yeah, no, but if they've got an old, robust operating system that didn't do much, you know, then... Right.

**Chris Gammell:** And it doesn't try to update itself too. That's the other thing, you know? Yeah. If it's on a network, it's like, oh, I'm going to go look for updates.

**Dave Jones:** Yeah, no. That's a modern thing, you know? That's true. Back in the days of Windows 3.1, well, there was no internet, you know? Sneaker net. Yeah, they just... Sneaker net. I mean, Windows... Yeah, I mean, Windows 3.1, I think, was the one that really added networking capability. Correct me if I'm wrong, but like 3.0 didn't have it. And the big step up, oh, it added networking, you know? Yeah, right, right. Or something like that. So, you know, but back then there was no internet, you know? Well, there was, but not as we know it, you know?

**Chris Gammell:** Yeah. All right, so to answer your question from about 10 minutes ago, let's see, which show was this? This was... Oh, yeah. You were getting the stat. ...show 130. We had about 5,600 listeners so far, which is awesome. And 73 of them were from Ireland.

**Dave Jones:** Wow. All right. What percentage of that? Is that 73 divided by... 73 out of... What is it? 5,000? 5,000 odd?

**Chris Gammell:** Yeah. That's a... You know? Yeah, it's really interesting looking at this stuff.

**Dave Jones:** Yeah, 1.5%.

**Chris Gammell:** Yeah, it's not bad.

**Dave Jones:** Wow.

**Chris Gammell:** And there was... Let's see, what was the lowest numbers? We had one person from Colombia, one from Senegal, Ecuador. I mean, like, it's cool. It's like everywhere. That's awesome. Yeah, I know, right? Yeah, yeah. And we had some people write in, you know, like about where they are. I think there was... I forget the one. I think there was someone... I forget what country it was. It was a really small... It was like St. Kitts or something like that. I don't remember. But, yeah, small countries.

**Dave Jones:** That's one of the things I love about my mailbag, you know? I'll get, you know, a mail from not only some country, but, you know, just from some small town somewhere, you know, in the middle of nowhere. And it's great. And that's not new, you know? This is back in the old days when I used to get letters, you know, for my projects. People would order my stuff, you know, they'd send a letter or they'd send a letter to me, you know, a handwritten letter. And it'd come from...

**Chris Gammell:** Self-addressed stamped envelope. With a self-addressed stamp.

**Dave Jones:** Yeah, the nice ones would send a self-addressed stamp envelope, but the others would expect you to actually buy a stamp, lick it, and send a reply back to them. Yep. Yep.

**Chris Gammell:** Man. That's... Oh, man. Yeah.

**Dave Jones:** And then you'd get, like, kits in the mail, you know? Somebody bought your kit or something like that, and it didn't work, so they'd just send it back to you, you know? So you just open your mail one day, and there's a kit with a note saying, fix it!

**Chris Gammell:** Fix it. Send me a refund. Sorry about the gum I stuck in there.

**Speaker ?:** Yeah.

**Dave Jones:** And you just take one look at... You know, and you get the letter that, you know, Smartice says, I know all about electronics, and I've spent hours thoroughly inspecting and testing this thing, and there's nothing at all wrong with my soldering and assembling, and it must be your stupid design. So you have... Oh, yeah. You're obligated to fix it, otherwise I'm going to tell the electronics magazines on you, and...

**SPEAKER_01:** And I bought this 20 years ago.

**Dave Jones:** So you look at it, and in 30 seconds you go, your input regulator sold it back to front, dude. So you... It's like, well, you couldn't even measure the supply voltage, you dickhead.

**Chris Gammell:** The last thing I meant to look at.

**SPEAKER_01:** Whoa, you know. Oh, boy.

**Dave Jones:** Yeah. It's crazy. Fun. Fun days. Yeah.

**Chris Gammell:** Can you imagine getting a call like that from Mars? Eventually, you know? I would love to. Oh, that'd be crazy.

**SPEAKER_01:** I ordered your kit, it took me six months to get it, and now I got it, and I'm sending it back to you. I've been living on this planet for 14 years now, and I've never been treated like this by customer service. And it only got up to 1,400 degrees during the re-entries. I stored it at a totally safe location in the nose cone. It only took 30% of all the heat on the re-entry. Oh, man.

**Dave Jones:** Yeah, I like this thing you've added. What kind of electronics should we bring to Mars?

**Chris Gammell:** Yeah. Yeah. And it's coincidental. Right. They're asking for volunteers now, finally. Finally! Really? And I know that I said that I would volunteer to die there. I think you might have agreed the same.

**Dave Jones:** If I was young and single, it'd be, you know, it'd be a choice.

**Chris Gammell:** I asked the wife, and she said, hell no.

**Dave Jones:** See ya. I think that was the response. Right. Yeah. Oh, boy. Yeah.

**Chris Gammell:** Yeah, they stated, you're not coming back. That is the first people going there, you're not coming back. And I don't know why people would expect that anyways.

**Dave Jones:** But people are going, apparently. Well, see, I haven't read this whole thing or watched the video, right? People will die on Mars. I haven't watched it yet. But there's no reason to do that. Now, this is coincidental, because at the moment, I am actually reading the leading book on how to get to Mars, explore it, and get back, and do it safely and do it cheaply. Right? And it's by a guy named Robert Zubrin, and he's like the world's leading expert on getting to Mars. And it's a great book. I haven't finished it yet, but it's awesome. It's called The Case for Mars. And it all, should I tell you the whole history?

**Chris Gammell:** How about a concise history?

**Dave Jones:** A concise history. Okay. Well, the concise history was back in 1990. I could be wrong. Bush? I think it's, was it the previous Bush? I don't know. Yeah, that'd be the early 90s.

**Chris Gammell:** It would be Herbert Walker Bush.

**Dave Jones:** Yes. Yeah. And he got up there in front of the Smithsonian Institute and said to the world, we're going to Mars. You know? And yeah, everyone went rah, rah, rah. And he was surrounded by Neil Armstrong, Buzz Aldrin, and you know, everyone else. And yeah, we're going to do it. Right? And of course, so he told NASA, right, go and give us a plan. So NASA came up with what's called the 90-day plan. Yeah. Right? Because it took him 90 days to do the report. Right? And it was going to cost $450 billion. And it was so hideously complex, it'd be the greatest engineering feat in the history of the human race. So yeah, Congress just went, yeah, right. And it just died. Right.

**Chris Gammell:** And when you look at the relative cost too, I mean, like, it's not like the original, the moon mission was cheap by any, you know, stretch. No. Well, no.

**Dave Jones:** It was about $80 billion adjusted, right? But this was going to be $450 billion minimum, right? And of course, you double that, right? Because, you know. So it was probably going to cost a trillion dollars. So this Robert Zubrin, who worked at Martin Manetta, Martin Marietta, I'm probably pronouncing that wrong. One of, you know, the rocket companies or whatever. Martin Martin? No, no. No. Okay. Martin Marietta or something. Anyway. I don't know. Anyway. Yeah. That company formed a little task group. They said, this is ridiculous, right? This plan's a joke. So they formed this little task group with, this guy was in it, and they came up with an idea for what's called Mars Direct. And it's going to Mars, get in there, stay in there for a long time, get in there directly, stay in there for a long time, exploring the damn thing, and then continuously exploring it, mission after mission after mission, and do it for like 15 to 20% of the existing NASA budget. Right? Really cheap.

**Speaker ?:** Nice.

**Dave Jones:** Yeah. And, of course, NASA didn't like that. Why?

**Chris Gammell:** Wait, wait, wait. Were they supposed to come back, though? Is that the idea, or no?

**Dave Jones:** Yeah, yeah. Yeah. Absolutely. Okay. So send people back. And it was fully redundant, and everything. They had backups upon backups. Very safe. It's a genius idea. I'll link in a video. There's a documentary on it as well. I think I'll have to watch this book or read this book, rather. Mars Direct. But there's a video that sort of covers it all as well. There's a documentary on like BBC or something about it.

**Chris Gammell:** Okay.

**Dave Jones:** And the reason that the NASA one was so, and this ties into engineering, right? This is why, the reason why the NASA one was so hideously complex and expensive is because internal politics, right? They wanted to make use of everyone's pet little project, right? So all the people who wanted the moon colony, they said, oh, well, you've got to make a colony on the moon first, and then use that as your staging base to go into Mars.

**Chris Gammell:** A true design by committee, right?

**Dave Jones:** Uh-huh.

**Chris Gammell:** We'll pull in this element, and this element, and this element, right? Yeah.

**Dave Jones:** So you had to pat on the back every little pissant idea project with inside NASA, right? Everyone's wet dream project. Perfect. So this system ended up being, yeah, you assemble this massive space station in low Earth orbit, and then you go to the moon, and you set up a colony on the moon, and you set up these giant, and then you build on the moon these giant intergalactic-

**Chris Gammell:** Then you go to an asteroid. Then you go to that, right? Then you go to that, right?

**Dave Jones:** Battlestar galactic-sized ships, right? That then fly to Mars, and then stay in orbit around Mars, because there are people who want to do science in the orbit around Mars, so you have to, you know, scratch their back as well. So you've got to stay in orbit. So you do all this, you spend $450 billion to spend like two weeks on the surface, then come back, and that's it. It's ridiculous.

**Chris Gammell:** That is ridiculous.

**Dave Jones:** You know, it's a joke, but that's common in engineering, right? It can be, yeah. Yeah, internal politics in big companies dictate you don't do it the best, cheapest, and most efficient way. You do it the way that scratches the most backs within the company.

**Chris Gammell:** Yeah, I mean, it depends on the company and the groups in the company. Of course. Yeah, that can definitely happen. I tweeted about that earlier this week, too. Like, just in system design, just how many decisions are not necessarily made by an engineer. You know, like, managers make a lot of decisions because the buck often has to stop with them, or, you know, sometimes at higher levels, the decisions are made up there because of pet projects or internal politics, oftentimes purchasing makes decisions because of part availability, or, you know, just they don't like a certain supplier. We've never heard of that. Happens all the time. Yeah, exactly. So, I mean, there's just so many levels where decisions are actually made. When you finally, you know, if you cornered someone and said, who made this decision? And if you cornered the design engineer every time, it's not always going to be them. You know, it's just, and when there's, like you said, there's pet projects to be fulfilled, it can get really messy really fast.

**Dave Jones:** And when you've got a big company like NASA with lots of, you know, they investigate so many things. Well, not only subcontractors, but they investigate so many things and technologies. They have so many ideas that, you know, there's a, when something like Mars comes along, when people start smelling the money, you know, they go, woohoo, I can get some money for my little, you know, wet dream project, you know? And that's, that can happen in big engineering companies as well as NASA, you know? Oh, you've got to reuse my code over here in my processor, in my project, right? Because it's the duck's guts, right? And we should standardize that across all of our company products, you know, even though it's not the best or most efficient or the cheapest. Right, yeah.

**Chris Gammell:** It might actually be better to rewrite the code or outsource it or something, right? Yep. Yeah. Yeah, it's weird because you need that, you almost need that, like, that focus on the final goal, right? More than anything else. Yeah, yeah, exactly. But oftentimes it's more internalized, it's more team-based or nationally based.

**Dave Jones:** Yep.

**Chris Gammell:** There's, someone sent me this, and I had seen this before, but there was, when I was kind of ranting about the, no, I wasn't even ranting, I was just talking about where those decisions are made. Someone sent me this, this tree swing, the, I'm sure you've seen it before.

**Dave Jones:** Yeah, yeah, I've seen it. Yeah, I used to have it posted up on the walls at the office. Exactly.

**Chris Gammell:** So people could look at it, but it's just basically all the different ways, you know, if a customer comes and says they want a tree swing, all the different ways that it's interpreted by everybody, and it's really, this is actually an even more extended version of it than I've seen in the past, but there's some good ones. So people should definitely check that out. I don't want to ruin it on here, because if I talk about the whole thing, it's just like, eh, boring. No, no, yeah, no.

**Dave Jones:** It's, you know, photos tell a thousand words, pictures tell a thousand words, and yeah, it's just hilarious. Yes.

**Chris Gammell:** So if you were going to Mars, though, what would you, what would you bring? I mean, I guess, I don't know, it's kind of tough to know, because we wouldn't know exactly what the mission would need to be, but I'm sure there's some things that we know.

**Dave Jones:** Well, you know, as it talks about in this, you know, power is everything, right? With power, you can generate, using the Mars, using carbon dioxide in the Mars atmosphere, you can generate fuel for your rovers, for everything else. You can generate, you know, oxygen, and you can generate water, and you can generate everything else. And, yeah, but no, one of the most important, what would I bring in terms of electronics, you mean? Yeah, yeah. Well, you've got to bring entertainment, because one of the biggest deals there would be, you know, would be boredom, cabin fever, right? It's a real psychological condition, the old cabin fever thing, where you used to go on the small ships, and you, you know, the thing which you lived in would not be much bigger than my lab here, right? Right. And you're stuck inside that.

**Chris Gammell:** Oh, that might be luxurious, too. I mean, first off, it'd be full of crap. Yeah, exactly. Walking over shit on the, yeah.

**Dave Jones:** And, you know, so you would bring, yeah, things which keep you... Reddit.

**Chris Gammell:** I'd bring Reddit if I could. Reddit. I'd bring, like, the slowest image you are downloads ever.

**Dave Jones:** Yeah. And that four-hour lag's a bitch for real-time chats on forums. It really is, yeah.

**SPEAKER_01:** Do they pick a pope yet? Do they pick a pope yet? Yeah. Oh, boy.

**Dave Jones:** But then again, that stuff is trivial. Like, these days, right, you can take the entire world's history and every book ever written to Mars on in a little, you know, in a briefcase. You know, I mean, it's...

**Chris Gammell:** Yeah, the Hitchhiker's Guide, right? Yeah. Right.

**Dave Jones:** So, you know, I... Yeah, no, that's a good point. I think it would be stopped to keep you... Things to stop you going insane.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** You know? Yeah. Because that would be the biggest fear. Unless the colony starts getting to thousands and huge and everything else, then the spaces you live and work and you're confined in are, you know...

**Chris Gammell:** Yeah, that'd be rough. Yep. That'd be really rough.

**Dave Jones:** Yeah, and it'd be tough. So, that is the toughest part of this whole Mars thing, is how to stop people actually going insane. You know, because you're cooped up in, you know, you've got the fear of never going home. You know, you're cooped up in this tiny, you know, five-meter-by-five-meter space and, you know, to go outside is quite an ordeal, right? Yeah, that's true. You know? And, yeah.

**Chris Gammell:** I'm sure not crashing into a planet surface would be a good goal to shoot for, too, but... Right.

**Dave Jones:** And they talk about, like, read... They actually talk about this in books, stuff to... And a previous book I read on Mars as well. He's been prepping, folks. I'm prepping. I've been prepping. He's just going to work on the wave. I'm a Mars fetish at the moment. So, that's why this is quite... Yeah. Yeah. Well done. And, anyway, this book, the previous book I written, is written by an Australian guy, actually. Oh, cool. Yeah. And, anyway, they said one of the biggest things is you have to take stuff to redecorate the interiors every so often. Really? If you do that every... Yeah. If you do that every couple of months, it stops people going insane and getting cabin fever.

**Speaker ?:** Yeah.

**Chris Gammell:** I bet that's tough, too, because, I mean, like, we all know this feeling, right? It's like you're in the lab all day. You're under, you know, fluorescent lighting. You're soldering nonstop for six hours or something like that.

**Dave Jones:** And there's no windows and there's... Right. Exactly.

**Chris Gammell:** And the only thing you want to do is, like you said, it's a change of scenery. You know, you want to go outside. Even if you go to a different... If you go to your basement, some people do that, right? I mean, I might be in a basement right now.

**Dave Jones:** Some people go to the lab next door and have a chat with somebody else. Yeah. Oh, what project you're working on? You know? Right. Exactly. Or, what about so-and-so? Isn't he a dickhead? You know? I mean, you just want to get out of there. My manager's making all my decisions for me. That purchasing department, this. Let's go outside for a fag. You know? Mm-hmm. Yeah. That's all part of... You know, people just need to get out once in a while. You need to take a break.

**Chris Gammell:** Yeah. Not going to go for a smoke break outside on Mars, huh?

**Dave Jones:** They realize that you could probably last about 30 seconds. Oh, really? Out there. Yeah.

**Chris Gammell:** You know, I learned that from Total Recall.

**Dave Jones:** Yes, exactly.

**Chris Gammell:** Your eyes bugged that little bit.

**Dave Jones:** Oh, yeah. I think they went for about a minute on Total Recall, so I think it's a bit unrealistic. But, yeah. They say, yeah, you've probably got 30 seconds before you die. So, yep. Nice. There you go. Bit of trivia. There you go. Bloody. Well, since we will not be going. Tell me, what would you take then? I mean, I...

**Chris Gammell:** Well, you know, like we've talked about in the past, it would be spares, a lot of spares. But it would be tough because, you know, I don't know how much it would be...

**Dave Jones:** You should take one of those chip printing machines, right? So, just like on that movie we talked about, not movie, the TV show Terra Firma.

**Chris Gammell:** Yeah. That would be helpful. Where they had those chip printing machines. There were... You know, we've talked about that a little bit in the past. But even, you know, like, yeah, electronics for that kind of thing. I think really, you know, having modular type of components that you could then build up, right? You wouldn't be able to have the most, you know, compact things ever because as complexity goes up, so does, you know, so does the failure rates. You know, they just...

**Dave Jones:** Which means that the systems would have to use all common parts. You know, somebody who designed the power system and somebody who designed the, you know, control system for the rover, they should probably use interchangeable modules. That would be a smart thing.

**Chris Gammell:** Yeah, you want to talk about a system design nightmare. Try getting two engineers to agree on the same capacitor manufacturer. Yeah, exactly.

**Dave Jones:** Now, what about the ESR characteristics? And that's important because you can end up in the shitter just like they did on Apollo 13. Yeah, exactly. Where the...

**Chris Gammell:** Dump the parts on the table and...

**Dave Jones:** Yeah, the lunar module and the service module used... One of them used square carbon filters. The other one used round. And when shit hit the fan and they had to use the limb as a lifeboat, right? Look, these round filters don't fit in the square... All the square ones don't fit in the round hole.

**Chris Gammell:** Yep.

**Dave Jones:** You know?

**Chris Gammell:** Crazy. And it almost cost them their life, right? I mean... But, like, imagine the specific... The logistics of that. Getting, you know, a new part approved. It's like... First off, you'd have... You'd have every vendor in the world trying to buy you... You know, if you had, like, an extended Mars mission for 30 years... And they're charging, you know, $10 a cap because it's radiation hardened or whatever... Right. You'd have vendors trying to buy you lunch... 10 bucks, that's cheap. ...at breakfast. Yeah, yeah, exactly.

**Dave Jones:** It's...

**Chris Gammell:** Oh, man. Yeah.

**Dave Jones:** I was talking to... On the flip side of that, though, it actually can be better and cheaper because if you've got... If you have to use... If you're forced to use somebody else's module, well, all the decisions are made for you. Right? That's true. If you have to be compatible with that module. So sometimes it's a good thing that those decisions are made for you. Because a lot of engineering, you can get bogged down in the details of choosing.

**Chris Gammell:** Yeah. It's such...

**Chris Gammell:** It's your boundary conditions, really. Like... Yeah, yeah, it does. I had a previous job. I had that where I wasn't allowed to... I wasn't... I was allowed to, but I was discouraged from...

**Dave Jones:** He wasn't allowed out of the lab.

**Chris Gammell:** The lunar module. He wasn't allowed to touch anything. He wasn't allowed to do it. Yeah, I was a new guy. No, that was me. You know, like, you... You know, when you're discouraged from registering new parts, right? That can just be a drug, right? You know, you see a new part, you hear about it on the amp hour, or you see it on, you know, a website. It's like, oh, I want to use that part, right? You just register it, you know, get the footprint done, and you go, right? Well, then your part catalog starts to balloon to a thousand parts, when you probably can get away with 250, maybe, you know? Yeah. And so when you're constrained like that, it just becomes a new boundary condition. You say, okay, well, I already have these caps, so I might as well just use them. And now, instead of speccing in a, you know, instead of speccing in a 4.7 microfarad cap, I just use two 2.2 microfarad caps, you know, like that kind of thing. And then you just kind of design around that. And that, you know, space constraints notwithstanding, that can be a really good way to design, I think. I mean, I think there's a lot of benefit to that.

**Dave Jones:** It can be. There is a lot of benefit to having the decisions made for you. Yeah.

**Chris Gammell:** Absolutely. I would put it like decisions made for you, but just boundary conditions. That's what it's all about. Well, yeah. I think engineers thrive with boundary conditions, personally. I mean, you tell me that I have, you know, four square inches of PCB, and I need to have three different, you know, functions happening, and here's the box of parts I can use to do it. I'm going to try and do it. That's a puzzle, you know? That's like, let me at it, man. If it's like, well, make something.

**Dave Jones:** You only have seven days left to do it. You've got to do it by the state. Exactly. And we'll do it with a bloody 10 minutes to spare, because we're geniuses. Right.

**Chris Gammell:** And you have to use leadless solder. Ugh. Yeah. Yeah. Ah, boy. So there you go. Yes, boundary conditions. They are good. Boundary conditions are good. Sometimes. I like them. Yeah, yeah. You don't want it to be...

**Dave Jones:** Unless you're working on your own personal pick project, right?

**Chris Gammell:** Yeah. Yeah, that's fun to kind of push the limits. You know, you can... Do it. Who is it? I forget what... Jason Tautic, I think? He designed in a breakout board for that lightning detector circuit. Right. You ever seen that? I think we talked about that chip before. It detects lightning strikes somewhere within some range.

**Chris Gammell:** Right. You know, it's like... Very few people get to design that in with an actual purpose. He just designed it in because he wanted to. I think it was Jason. But, you know, it was just like a fun chip to use. You know, if you're doing pet projects, you can just put those in, right? If it's like... Yeah, yeah, exactly. You know, you're not necessarily going to inspect that in unless it's probably designed for your industry. And it's... It's getting worse with that kind of like specific application stuff. I was talking to a big chip manufacturer the other day. And I was like, you know, well, I want to hear about new parts. Tell me about all your new parts. And they're like, well, there's only so many that are for your industry. And I'm like, yeah, I know. But just tell me about all of them. Because oftentimes, I already know about the ones for my industry. Yeah, yeah. Of course. I want to know about the ones for Dave's industry. Or, you know, some crazy aerospace application. Because it's when you get to refactor those already existing parts. That's when you get cool stuff.

**Dave Jones:** You get innovative products often. Exactly. You come up with innovative ideas. Because this part was designed for the seismic industry. But, hey, if I go use it over here in the audio industry, hey, magic happens. You know?

**Chris Gammell:** Exactly. Yeah, there was actually a part last week that I saw that... I really don't know where I'd use it. But it was a cool part. It's a microchip part, actually. I think I told you about that after the show last week. Oh, the... Yes, the wireless... Is this the... Sorry, the body sensing thing? Yeah. I got to search on the Reddit. Sorry. Yep. But, yeah. So, it's a part from microchip. Yeah. So, you can get a kit, too. But, basically, you can put the... It's like an RFID tag. But instead of actually, like, beaming it over... RF. It goes through your body. Yeah. It uses your body as a capacitive channel, basically. So, you think about having this thing in your pocket. It's, you know, touching your skin or whatever. You go and you reach for your door handle on your car. It does a transfer of the ID on that chip through your body. So, it's not just flying through the air. And then it says, okay, well, this is Chris with ID 11449. Right? And then it unlocks the car. And it's like, whoa. I mean, it's not, like, super crazy. Like, the technology within it is not, like... No, it's been done before, right? It's not necessarily new. But, hey, it's a chip so you can just buy it, right? Exactly. Yeah, yeah. Oh, they call it Bodycom. Yeah. Right. Boring name, but... Yeah, it's pretty bad stuff. I mean, yeah. I don't know. I think... And, you know, the application I really like is thinking about that last Bond movie where he had the, you know, the... Oh, the God. Yeah, the Walter PPK, like James Bond always has. And they were talking about, like, matching his palm grip. But this same kind of thing could happen where you could, you know, sew it in your clothes and only, you know, only, like, only your power tools work with you or only your, you know, weapon works with you if you're a police officer or something like that. You know, like, that's cool. That's really cool. I don't know. I was geeking out about this last week. No, totally. I can dig it. Very, very nifty. I like it. I like that kind of... Okay.

**Dave Jones:** Speaking of nifty, there's a NAND-based computer.

**Chris Gammell:** Yes. This is fancy.

**Dave Jones:** People have done these before, you know. It's nothing new. It's, you know, everyone's probably had the idea to, you know, I'd love to do something like that, you know.

**Chris Gammell:** I have never said that I wanted to do something like this. Really? I will never say that... Ah, dude, this is terrible. I don't know if you want to waste six months of your life.

**Dave Jones:** Yeah. It's a great way to do it. You know, very therapeutic. I don't know. Anyway, he's built a whole computer out of NAND gates. As you do. Because with NANDs, you can do anything, right?

**Chris Gammell:** Yeah. You tweeted that today, didn't you? Yeah, I did. You said that on the forum. On the forum, you said that.

**Dave Jones:** Yeah, I said, no, I said, forum or Twitter or somewhere, yeah.

**Chris Gammell:** Yeah, yeah, yeah.

**Dave Jones:** Yeah, I said, what's the most popular chip? Yeah, that's right. It was the forum. Somebody asked, what common chips as a hobbyist? Yeah, what chips should we get? What common chips should I stock? And I just said, well, you can build anything out of NAND gates. Yeah, just one. Yeah, it's true. You can build counters, computers, flip-flops. You can build everything just from a common NAND gate. So, yeah.

**Chris Gammell:** You probably would want to, though.

**Dave Jones:** I mean, this is really cool. Here's an example of why you wouldn't want to, right?

**Speaker ?:** Yeah.

**Chris Gammell:** Well, no, it's not even this. I mean, this works, right? It's the problem of, oh, well, this LED isn't lighting now. Oh, crap. You know, it's like chasing that all the way back through the system. You know, that kind of stuff is, you get to know it really well, though. I mean, from a learning perspective, nothing beats this. It's fantastic. It's like, so my buddy did this with, like, a 6502 computer. A lot of people are into, like, the 6502, you know, building up old stuff like that. Uh-huh. I just didn't, eh. Eh. Eh. I don't know. You young whippersnapper. I know. Yep. Well, I mean, like, you know, when you look like a Raspberry Pi, it's like, but it's just what level you want to live on, right? If you want to live in the software level, then you go do software stuff. Yeah, of course.

**Dave Jones:** You don't give a shit about hardware like this, right? It's stupid, right? This is the dumbest thing you've ever seen.

**Speaker ?:** Right.

**Dave Jones:** It's this new computer, right? But at the same time. Why? You just wasted, you know, how many hours of your life building that thing, you know?

**Chris Gammell:** Right. But it's cool, you know? And this guy did it all with point-to-point wiring.

**Dave Jones:** Point-to-point wiring. It's not wire wrap. At first, you might think it's wire wrap, but no, it's point-to-point soldered wire. Yeah. So it's using perf board.

**Dave Jones:** And then he's just, like, green. Well, like, he hasn't even used different color wire. He's just, like, green wire. Yeah. He's got a thousand meter spool of wire, and he's going to use it.

**Chris Gammell:** Yeah. That's the two things he got. He got socket, or three things. He got sockets, NAND chips, and green wire.

**Dave Jones:** Yeah. Thanks, Grandma. Great birthday present. And it's an absolute mess. You know, I've built stuff like this. I've built one-off, you know, maybe the size of one of his boards. He's got, what, one, like, you know, half a dozen, six or seven boards or something. Yeah. All with point-to-point wiring like this. And it's just, wow, you know? Like, I wouldn't do that today. I would, you know, do a proper PCB. And then, because this is a one-off, right? Nobody else is going to replicate this, right? Well, maybe. In some form. It's so much blood, sweat, and tears. Because, well, yeah, somebody might take your schematics. They might take your schematics and then go build a PCB. But no one's going to build it using point-to-point wiring like this. Right? You never know, man. You never know. Well, you never know. But, hey, the odds are low, right? That more than one person is going to make one of these. Yeah, maybe independently. I'll say that. We were discussing this before the show very quickly. Like, see, I used to do this back in the 80s, right? But now I wouldn't do it, right? Because, well, I like to share my projects with everyone else. And I get a bit of a kick if somebody else builds it as well, right? And I know that chances of somebody else building this is zip, right? So that's why I would have done this. I can dig the idea of doing this. I'd love to do it. But I would design it on a PCB and then, like, maybe sell the blank boards or something. Or at least release it as open-source hardware so that at least some people can, you know, get the thrill of building this thing up. And really, I don't think the thrill...

**Chris Gammell:** It's a new DFX almost, you know? It's like there's DFT, design for test, design for manufacturing. Oh, yeah. And now this is DFS, design for sharing. Right? It's like the new...

**Dave Jones:** I like it.

**Chris Gammell:** Yeah.

**Dave Jones:** Design for sharing. Trademark. There you go, folks. We've come up with a new industry term here on the Anbauer.

**Chris Gammell:** Design for sharing. Trademark term. Do not use it without asking. Right. Yeah. Do not share this term.

**Dave Jones:** And see, now I think the value in this, right, is actually, you know, figuring out how the thing works just with using NAND gates, right? How you build it is irrelevant. That's why I think it's a stupid idea to build it using 10,000 point-to-point wires, right? It's, you know, it's dumb. You don't learn anything by... No, you learn something. ...by doing point-to... No, you don't learn anything by doing point-to-point wiring, right? You learn how to make good solder joints. You learn how to make good solder joints. ...is when it fails, right? Yeah. ...is when it fails, and you have to debug the thing, and it becomes a pain in the ass, right?

**Chris Gammell:** That's a good... It is, but the... How did you learn how to troubleshoot, Dave?

**Dave Jones:** Yeah, exactly. But by the... But just the aspect of soldering 10,000 freaking wires point-to-point onto this thing doesn't teach you anything in itself. It does.

**Chris Gammell:** It teaches you the value of a good solder joint. It teaches you the value of taking your time. It teaches you the value of checking your work.

**Dave Jones:** But you don't have to do it 10,000 freaking times.

**Chris Gammell:** Yes, you do. Oh, I disagree. Man, we were talking about, what, repair with Mike Harrison, right? That is a perfect example. You could say, oh, well, I don't need to learn how to troubleshoot, you know, a 10K-ohm resistor, right, knowing when it's blown. But when you see it 13 times in a row, you're going to start assuming... I agree. ...you're going to start rolling stuff out.

**Dave Jones:** I totally agree. Right. But you can learn this by doing this once and then never doing it again, right? I'm sure this guy who built this, I don't know who it is, learnt the value of that a long time ago, right? There's no need to build up something with 10,000 point-to-point bloody wires on it for each new project you build.

**Chris Gammell:** Oh, okay. You're saying it's a repetitive... That's what I'm talking about.

**Dave Jones:** No, you've got to learn the skill once, right? But then after that, it's pointless, right? Just like, for example, a lot of people will argue that making your own PCBs does not teach you electronics. It's not an essential skill. It's almost pointless to learn to etch and produce your own boards, right? There's no value in it as far as an electronic skill set goes, right? Right. Maybe from an economic standpoint or a time standpoint. Yeah. That's why I don't make my own boards anymore, right? There's just no value in it.

**Chris Gammell:** Right. But you would say that doing it once or twice, you know, it's the point of mastering.

**Dave Jones:** Maybe do it once or twice to understand the process of over-etching and stuff like that, you know, and yeah, things like that, right? Maybe.

**Chris Gammell:** You don't have to do it to the point of mastery anymore, though. I mean, like certain things, like you would do it because you want to master it because then you're going to have to use it a lot, but maybe mastery isn't the point anymore. It's more of context, right?

**Dave Jones:** The thing with troubleshooting, right, you only have to make a mistake once and you learn, all right? If you drop that 10,000 piece of equipment, you've learned something, right? If you've blown up that, you know, that prototype board because you hook the wires up backwards, you, that's, that's etched in your mind, right? You don't have to do that 10, you don't have to blow up a thousand boards to realize, nah, come on.

**Chris Gammell:** No, but seriously, like I, it took me a long, I mean, like with, so assuming you don't have, you know, outside help, right? It took me a long time to learn the value of flux in soldering, right? I know it shouldn't have taken me as long as it did, but it did, you know, like that's just something that it, you know, I just had crappy soldering for a long time and then it would bite me certain ways. It was, you know, small nibbles that ended up getting me, you know, like, you know, a joint would break or, or, or, you know, uh, I'd have like an intermittent, you know, performance.

**Dave Jones:** But you've got to think, you've got to admit, there's many things like applying power to your board backwards or something like that, that, you know, can be a very expensive, costly mistake and you only do it once and then you learn, right? Like to power up your board using a, you know, using a current limited power supply first or something like that, right? Yes. You know, or you touch the hot end of the soldering eye, right? You don't have to do that a hundred times to learn that, well, that's dangerous, right?

**Chris Gammell:** Yeah. Or you, uh, you have butterfingers with those really sharp tweezers and it starts to go towards your lap and you're like, you're like watching in slow motion, you're like, oh!

**Dave Jones:** Or you're using, uh, you're a soldering SMD part, you've got them all on the bench and you sneeze and then they all just go everywhere and you've lost them, right? You only have to do that once to realize that, you know, I mean.

**Chris Gammell:** You're down to your last part and you've got, you've got to end your tweezers and then you squeeze too hard and it goes across the room.

**Dave Jones:** So yes, this mastery thing, you know, doing it to work in 10,000 hours on something, you know, it doesn't apply to everything, right? Some things, it's just once. Well, yeah.

**Chris Gammell:** And the mastery thing, there's an asterisk with that too. You need, uh, I think anytime they say with the 10,000 hour rule or the mastery, you need to have directed work and directed feedback, right? So if you, you know, if you grab the hot end of the starting iron, you need to not grab it a hundred more times before learning. You need to recognize it and then modify behavior. If you don't do that, then the 10,000 hours is worthless.

**Dave Jones:** Well, of course. But usually there are, they're usually the things that take 10,000 hours to master are usually quite complex, like PCB layout or something. Yes. Or, you know, yeah. I mean, you know, RF design or something, right? You know, so they're usually complex subjects, but, you know, so it doesn't, it doesn't apply to really dead-ass simple things.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** So, yeah. Huh. Well. There you go.

**Chris Gammell:** It's good that, uh, his awesome project got us yelling at each other. Yeah. It's great.

**Dave Jones:** Sure people are loving it.

**Chris Gammell:** Yep.

**Dave Jones:** Anyway. So, what? No, I just think it's, yeah. Point to point worry. God.

**Chris Gammell:** Well, do it, like you said, do it once. I thought you meant to never do it. I think, I think doing it once is.

**Dave Jones:** Oh, no, no, no. See, I've done, as I said, I've done this once myself. Well, this was because you had to back in the day, back when I did this, right, in the 80s. Well, you know, I didn't have a freaking CAD program, right? And to make your own PCB, right, you couldn't get one made commercially because it would cost you $1,000, right? Right. It doesn't cost you $30 from freaking IT studios that it does these days, right? And even to make your own, and it takes so long to drill, to etch and drill 10 of these boards that, well, you may as well just use a perf board, you know, so I can understand from just getting into it, you know? Just bang. Well, I don't want to lay out a board and do everything just point to point, right? Right. So that's, you know, yeah. But what a dog to debug.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Because it almost certainly didn't work first go.

**Chris Gammell:** Yeah. Oh, man. I've been debugging lately, and spy is not my friend. Do you ever do any spy bus stuff?

**Dave Jones:** See, I don't call it spy. I call it SPI. Yeah? I've never used, I've never liked or used the term spy. Why is that? I don't know. Just never have. Nobody I know ever does. Well, here, like that I've worked with.

**Chris Gammell:** Yeah, but you guys say the LEDs, too, don't you? You say LEDs instead of LEDs.

**Dave Jones:** Oh, yeah, yeah, LEDs, yes.

**Chris Gammell:** Yeah, well.

**Dave Jones:** I mean, no, it's a, I don't know why. Ask me why, I have no idea, right? It's just because nobody else, nobody else I've worked with does, right? Yeah. It's just, you know, I don't know. People pronounce things differently everywhere. Yeah. It's just a fact of engineering. In the global world we live in. So I'm not wrong by saying SPI. You know, a few people take just a task on it. You know, let's just call it spy. Just different. It's easier. Different.

**Chris Gammell:** You know?

**Dave Jones:** Yeah. Yeah. I don't know. But I found it seems to be a Yankee thing. What? Am I right? Saying spy?

**Chris Gammell:** Yeah. I don't know. You're the only Australian I know. Well, not the only one I know, but. Right. You're the only one I talk to regularly. Well, there you go. A hundred percent of people in Australia call it SPI. Yeah, exactly. That you know, call it. Sample size of one. Call it SPI.

**Dave Jones:** Well, shall we get into Bode and Bode?

**Chris Gammell:** No. No, we should. And Bode?

**Dave Jones:** Plots? No.

**Chris Gammell:** No.

**Dave Jones:** No. All right. Let's not go there. Been there before. Flogged that one to death.

**Chris Gammell:** So do you ever do anything with SPI bus, though? Are you ever. Yeah, of course. Yeah.

**Dave Jones:** Yeah. Why?

**Chris Gammell:** What are you. What problems are you having with it? So the main thing that I had is the different modes. I didn't. I knew they were there, but it's like one of those things. It's like it's like checking a footprint. Right. It's like the last thing you look at. And so about three days later, I'm kind of like staring at this thing and I'm, you know, getting garbage back for three days, which probably shouldn't have happened. But. Wow. Yeah. Three days. Yeah. You know. Yeah. These things happen. But three days later, I'm like, oh, nothing's, nothing's lining up.

**Dave Jones:** Yeah.

**SPEAKER_01:** Dearity.

**Chris Gammell:** So how did you find it in the end? How did you? You know, it was. So that's another thing, too. You know, like you. So, you know, you're throwing garbage into a, you know, a system. I was just kind of thrown into a microcontroller and getting these readings back. And, you know, I suspect memory corruption. I suspect all these crazy things. You know, your brain goes every which way. Yeah. Yeah. And then eventually what I should have been doing from the beginning is been scoping it. But I, you know, I had to unhook the board at some point.

**Dave Jones:** I was going to ask, like, yeah.

**Chris Gammell:** Right. Yeah. Rookie mistake, right? Yeah. But it's just amazing the kind of stuff that you figure out that way. I mean, I know that this is nothing new for anyone, but it just was a gentle reminder.

**Dave Jones:** Well, see, sometimes you never have these problems because usually it just works, right? You know, you're using off-the-shelf, you know, module, you know, SPI interface module, you know, off-the-shelf code for your micro. It's got the SPI hardware in it. You use the example code from that. And it just, you know, you hook it up, you ship, and it just works. Yeah. You just throw it in there. So you never find it. As we've always said, you know, troubleshooting stuff is the best way to learn because, well, you know, if you just build something up and it works, what have you learned? Well, you know. Right. Not much. You learned you're awesome. That I can solder 10,000 point-to-point wires. Yay, I'm a hero, right? Yeah, exactly. But when that, you know, NAND computer doesn't work, that's when you, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** That's when you learn a lot. And same here, right? You wouldn't have learned about all that stuff if it didn't fail on you.

**Chris Gammell:** Yeah, yeah. And so, of course, the things I learned also were, you know, putting in, it was all software side, really, because that's the thing I was least confident about, right? I mean, like my software, my firmware is always weak. It's always just crap code, you know? And so I start throwing in test statements everywhere, and that ends up messing other things up, you know? Yeah, yeah, yeah. This is a test, you know, erase this later, that kind of thing. Don't believe this result. But, yeah.

**Dave Jones:** Did you write your own SPI routines? No, no, I had hardware. No? You had hardware? Have you ever written Bitbang? I haven't. In the face of, like, I squared C and stuff like that? No. SPI? You've done a lot of that? Yeah, yeah. I've done probably every bus in Bitbang before. Yeah. Yeah. I've written my own from scratch.

**Chris Gammell:** It's heavy duty to do that kind of stuff. You just got to sit there and just chunk on it, you know? It's just so wasteful.

**Dave Jones:** Well, when you sit down and do it, it's not as hard as you think. You know, if you want to implement... No, no, no. You know, especially if you just want to implement the simple, like, the bare bones just to get your chip talking, you know? Yeah, yeah, yeah. It's not necessarily that hard. Yeah, if you want to do the whole bells and whistles one that you're going to release as open source hardware, you know? Like, open, you know, source or whatever, then, yeah, it's a different, you know? Yeah. Yeah. Well, it's the same thing on the I2C bus, you know? There's different modes and different things. And, you know, well, you don't have to implement all of them.

**Chris Gammell:** You don't want to write, like, a super flexible, yeah, super useful everywhere, you know? Tons of code reuse. You just want to get it cranking.

**Dave Jones:** Yeah, you just want to get it working. So you write your 30 lines of code and it's done, you know? I mean, bang. Well, I didn't mean...

**Chris Gammell:** I didn't mean... It was, like, resource intensive on the processor side. That's what I meant, because you're just sitting there, you know... Oh, yeah, yeah. ...clocking on a certain GPIO pin or something.

**Dave Jones:** Yeah, no, I don't like... No, I love using the hardware modules, which is common these days. But, hey, you know, 10 years ago, you know, 10, 15 years ago, finding a micro that had a built-in, you know, I2C or SPI hardware or a UART even, right? I've had to bit bang my own UARTs, right? Because, well, the cheapest... Really? Because the bottom-of-the-range chip didn't even have a bloody serial UART in it, right? Yeah, I guess they take that for advantage. Yeah, you take it for granted these days. Take it for granted. You take all of them, right? You go, oh, I'm going to pick any Atmel micro or any microchip micro, and it's going to have an SPI. It's going to have an iSquad C. It's going to have a serial UART, right? It's just a given these days.

**Chris Gammell:** But, you know, it makes sense from the hardware manufacturers, too. I mean, you look at, like, certain parts. Like, I always looked at, like, Freescale parts like that. It looks like, you know, like some of their newer stuff that they put out, they just... It looks like they're just, like, pulling stuff off the shelf and just throwing it in there. It's like, oh, I have a fix of chips. You know, that kind of thing, you know? It's just like, oh, okay, well...

**Dave Jones:** That's how they design these chips. They have all the Verilog or VHDL, the high-definition code that they, you know, that they use for the ASIC, right? And they just go, well, we'll whack it in, right? And then the compiler, you know, it generates all the silicon, right?

**Chris Gammell:** Yeah.

**Dave Jones:** And, you know...

**Chris Gammell:** I have no idea how that stuff works, man. All that back-end, like, testing and all that crap.

**Dave Jones:** All that back-end ASIC and all that, yeah. All that layout software. All the cadence, you know, the high-end cadence ASIC. Yeah. You know, chip, you know, design stuff. Yeah, but it handles it. That's how they do it, right? They've got all these high-level modules and they go, right, well, it's trivial for them. You know, it's a couple of minutes' work to say this chip is going to have two SPI modules. And they just drag them in. You know, I mean, it's... Yeah.

**Chris Gammell:** Too easy. It's nice. I tweeted about that earlier this week, too, because I got to talk to some product definers and stuff like that. Product definers? Definers, yeah. So, like, they're, like... What they really are is, like...

**Dave Jones:** Is this their business? Is this their title on their business card? Yeah. I'm a product definer.

**Chris Gammell:** Yeah, a lot of times it is.

**Dave Jones:** I don't do any real work. I just define shit.

**Chris Gammell:** No, but that's the thing. So, these are, like, engineers who are, like, really good at what they do, though. Like, they're, like, basically moved... They keep moving up the chain in terms of, like, you know, they start designing modules. This is, like, chip manufacturers. And then, eventually, they become system... You know, they get more and more parts of the design. And then, eventually, they go out and talk to customers. But I like these guys because they're often... You know, they're almost always former engineers or still acting as engineers. Oh, of course. Yeah, yeah, yeah. And that, you know, like, you go into a meeting with an engineer versus, like, just, like, a pure marketer. I mean, there's been a lot of good marketers I've talked to, too. But, you know, you talk to them and you hear them, like, going through the design decisions behind, well, we decided to do this because of, you know, this geometry or this process. That is just awesome. You know, like, when you know there's some kind of, like, logic behind the decisions there, that just gives me warm fuzzies, you know? Exactly.

**SPEAKER_01:** Oh, yay! People know what they're doing! Yeah!

**Chris Gammell:** Yeah! Yeah! Yeah!

**Chris Gammell:** Oh, boy. It's great.

**Dave Jones:** But they don't necessarily because all these so many... This is a thing that ticks me off. There's so many variations on these chips these days and they're all buggy. They're every single one of them. Why can't they just stick to, you know, a dozen types of chips? They've got everything built in, make zillions of them, so get the cost down, and they're fully debugged and they've gone through 10 silicon revision levels, you know what I mean? Oh, because money. Yeah, I know. Yeah, you know. You know how it is. Yeah, you know. We had the guys on here talking about from Touchstone, right? And they were talking about, yeah, they're, you know, there's business reasons to, for them to do as many variations of the chips as possible, right? Yeah. There's legitimate business.

**Chris Gammell:** Oh, that's going to get so much worse, too. I mean, from the SOC, the silicon-on-chip kind of, like, system-level stuff, too. Yeah, it's terrible. Every time, I think I've said this before, but every time I meet with, like, you know, high-level vendors and stuff like that, talking about new, you know, modules they're doing and everything, I'm like, dude, you're killing me here. You're taking my job. You know, like, on one hand, I'm like, oh, this is going to be easy. On the other hand, I'm like, seriously, this is what analog designers used to do, and now it's all inside a little chip, and I just talk to a spy. It's like, screw you guys. What a job. So I'll just have to do my own thing eventually, you know? That's going to be, that'll be it, you know? We'll all just be mashing stuff together and talking to spy over it, you know? Like, it's moving to higher levels of abstraction. And then...

**Dave Jones:** So you can't see yourself doing this sort of shit on Mars, can you? You just, you know, you can't see yourself sitting down there with a scope trying to debug something to get something fixed or working, right? You just, everything modular, right? Probably.

**Chris Gammell:** Unless you really needed it, right? I mean, you'd need to go back and pack stuff apart.

**Dave Jones:** Well, if you were absolutely desperate and it was the last backup that failed, you know? I mean...

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, maybe.

**Chris Gammell:** Yeah, I think from, yeah, from a system-level design thing, if you're tearing panels apart while you're on a board, you're probably doing it wrong.

**Dave Jones:** Yeah.

**Chris Gammell:** Shit has probably hit the fan.

**Dave Jones:** Well, they said that, you know, two of the four people that would go in a Mars direct trip, right? They realised the optimum number of people would be four. Then, you know, two of them would have to be... Robots. ...maintenance repair.

**Chris Gammell:** Oh.

**Dave Jones:** Cluey people who could fix shit, you know? The tinkerer.

**Chris Gammell:** Yeah, exactly. Now hiring makers for the mission. Yeah, so it's interesting, the makeup of, you know, what skill set people need.

**Dave Jones:** But, yeah, none of it was, like, to the level of detailed design knowledge. It was more of, you know... Well, think on your feet, kind of survivor type. ...you, you, you, say, Heath Robinson-ish kind of, you know, fixing, repair kind of... Heath Robinson? Who says that?

**Chris Gammell:** Is that, like, someone that's older than me?

**Dave Jones:** It's a Yankee. That's a cobbling together of shit, isn't it? Have I got the terminology wrong? I've probably got it wrong. Probably embarrassed myself. Heath.

**Chris Gammell:** Heath? Cliff? Heath Cliff.

**Dave Jones:** Heath Robinson-ish. He's best known for doing eccentric machines. Sorry, yeah, I... Probably, yeah, not the right terminology.

**Chris Gammell:** I'm sure... No, it could very well be me. I mean, you know that.

**Dave Jones:** Yeah, but it means to get something weird working with everything you have available, you know, kind of cobbling together, kind of, you know, kind of like a MacGyver, you know? So two of the people would go, they have to be MacGyvers, you know? They've got to fix stuff.

**Chris Gammell:** Yeah, a rubber band and bubble gum and... Yeah. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** I imagine... So, you know, like, when you're, uh... When you got, like, a bunch of new boards in, and you blow up the first three, and you kind of label what happened to them, and you kind of toss them aside? Yeah. Can you imagine that, like, on a Mars mission? Just having, like, a bunch of boards floating around and be like, oh, yeah, I blew those up. I really shouldn't have, because now we can't breathe. Well, the good thing is Darwin works a treat in that case.

**Dave Jones:** It does, yeah.

**Chris Gammell:** Yeah. What, the people that breathe the least? Yeah, people who do stupid things will...

**Dave Jones:** People who do stupid things will ultimately remove themselves from the gene pool, you know? That's true. They will kill themselves. They'll get themselves cooled, and they can't reproduce, and, well... I think if you go to Mars, you probably can't anyways, but... All right. Yeah. Man. Jeez. What else is... We've been yapping on for an hour about what? Oh. Nothing. Mars and shit. Mars and swings and spy bus. Bloody hell. That's a good show.

**Chris Gammell:** We've got through nothing we had on the list. Well, we can get some things in here, I'm sure.

**Dave Jones:** Ian Ross, president of Bell Labs, died at 85 years of age.

**Chris Gammell:** Yeah. That was a loss.

**Dave Jones:** Noteworthy? I don't know.

**Chris Gammell:** Yeah. I guess so. I mean, like, you had a Bell Labs, of course, right? Chris's care factors, yeah. Well, I mean, it's not like, I know him. You know, it's just... No, exactly. I don't, you know. Yeah.

**Dave Jones:** But no, he was an important figure in the history of development of electronics and technology and, you know, yeah. Yeah. And of course, Bell Labs, you know, if you haven't heard of Bell Labs, well, get the hell out of the industry, you know? Or you're so... Or go on Wikipedia would be the nicest thing.

**Dave Jones:** We're just going to whack you over the head and go... Order you to go...

**Chris Gammell:** Let's say go to Wikipedia and start reading. Exactly.

**Dave Jones:** Go to Wikipedia and learn about Bell Labs.

**Chris Gammell:** Yeah. Yeah. So, yeah. What was the thing I was going to bring up? Oh, so we had... I had someone contact me about something called Circuit Lava. This is kind of an interesting concept of like...

**Dave Jones:** Oh, it's not another bloody online tool. It sounds like the name of another online schematic tool or something.

**Chris Gammell:** No, this is like a marketplace, actually. So, it's like... It's like you design... Marketplace for what? For circuit design. So, it's like you have a fully formed, tested circuit, like a DC switcher, right? Spy bus. You've got a spy bus in your face board. Yeah, yeah. No, no, no. But like more of a PCB level, you know, like a... Right. Like a 533 switcher. Right, okay. Yeah, yeah, yeah. You have these completely tested and long-term supported ideas, basically. So, Dave, you would design a 5 to 3, 3 volt switcher with like an LT part or something like that. You package it up. You show the test. You have all the results. You have input ports, output ports, modular design. And then you put it on there and you say, because it's a relatively simple design, but I'm willing to support it for, you know, five years or something like that, it's $5. You know, some very nominal amount for like something simple. The more, you know, if you did like a big DSP circuit, then you would actually, you know, charge more and everything if there was like firmware involved. But this is kind of a new idea that's out there. And so what they're doing is they're looking for potential designers, basically. I was contacted about it. Right. It's tough. Yeah, well. No, no. I knew that side was coming, right? Do you want to hear my opinion? I know what your opinion is already. But before you do, let me just say this. It's interesting because I know what Dave's going to say. Dave's going to say that this information is already out there and a lot of people would be willing to do it themselves. And I do agree with that. But, you know, I've been thinking about this a little bit and I even told this to them. I was like, well, you know, I'm not sure I'd be able to ever use it. But on the same side, there are people out there that would, I think. And so it might be niche thing. But everything starts as niche.

**Dave Jones:** If they think it's mainstream, I'm telling you it's going to be niche. Okay. This concept is not new. It's been around for a long time. Even Altium tried it, right? Altium's concept of the future of electronics design, right? This is a company that thinks about this sort of shit, right? Well, yeah. Okay, well, they get brain flashes. Except for who they hire. And, right, and they think, yeah, right, everyone's going to be, everything's going to be modular, right?

**Chris Gammell:** Yeah.

**Dave Jones:** Everything, right, you don't have to design that switching converter anymore. It's already done. Modular. Take the everything, like the PCB layout and everything. This was Altium's plan, right? Take it. You don't even have to do the layout. Take the modular. Yeah. Choo, choo, choo. And put them everywhere. And it doesn't work. Okay? It's never going to work. It's very, it'll work for a few people. Very niche, right? It's a tough problem. But for mainstream stuff, it's never going to work, right? Right. Because there's already, because there's so many design constraints in your, in engineering as we've talked about. Can you use this part? Is it already an approved part in your system? Is it, you know, does it meet the form factor you require? Does it require, you know, does it meet the price performance target you require? Does it meet the size factor? Does it meet the soldering technology? Does it, you know, is it the correct packages that your assembler can handle? Is it, and there's like a dozen different decisions where there's a, here's the thing with this thing, there's a dozen different reasons not to use that module than there is to use it, right? There's 10 times more reasons not to use it than there is to raise it.

**Chris Gammell:** I think it depends though. I mean, like, so, so in certain situations, right? So, so, I mean, everything's moving to higher levels of abstraction. If, if you're able to piece together circuits, I think, and, and you're able to actually, you know, say, say you're just trying to define it from a system level, then, then this could work. And, and that's, and that's the interesting side of it. I think you're right when you have.

**Dave Jones:** Sure, but into a final commercial product? No. Sure. If you're lashing together a, you know, a product, you know, an ATE test system for production or something, sure. You don't want to dick around designing all the, you know, it's like, oh, here's a module. Yeah, I'm going to use that, that, that, and that. And you build a one-off or 10-off, right? Fine. But, you know, it's, there's limited appeal to this. I'm telling you. I, I looked at doing this. I was going to do this 20 years ago. I was going to make a business out of selling modular electronics, modular systems like this that you plug together, right? It's not new. I've investigated extensively 20 years ago and it was not viable then. It's not viable now.

**Chris Gammell:** I'm sorry. Well, hey man, don't, don't rain on parades if you didn't, if you didn't, uh, you didn't go through with it.

**Dave Jones:** Sure, have a go, but like, don't, don't think it's going to be the future of electronics because it's not. Practical considerations always rule.

**Chris Gammell:** I agree with that. I mean, like, so, so what I, what I told them is, you know, like I think about it from my perspective of, so first off I had the same kind of, uh, the same kind of situation where I was like, well, well, damn it. There goes that part of the job too. Right. I mean, like, seriously, that, that, that, that, that, that, that, that, that, that, that was like, what's left for me?

**Dave Jones:** I have to learn a lot of code. A cleaner can come in and assemble your, you know, assemble a new product, you know?

**Chris Gammell:** Yeah. Yeah. All right. But, uh, you know, so, so there, there was that side of things, but, uh, but on the other side, it's like, well, I, you know, like I'm not sure I'd be able to use it, but at the same time, like I can very, very well think of some situations where, where people could.

**Dave Jones:** Of course. I wouldn't put it out there. I would have told them the same thing. I wouldn't use it myself, but I can think of many reasons why somebody can use it, but I'm going to be honest and say, I can also think of an order of magnitude more reasons why people won't use it. So just take that. Just, you know, you, you know, you have to tell people the truth, right? Yeah. You've got to tell them the truth that in my experience, that is the case. So, well, you know, if you think I'm wrong, fine. I could well be for a lot of.

**Chris Gammell:** I was watching this, this presentation about, uh, I forget. It was about startups though. It, and, and it was about funding and, and basically like when people, uh, start, did startups for like, I think the example they gave was dog food and they said, well, there's, you know, a hundred million dogs in the world or their dogs eat a hundred million cans of dog food today and we can get 1% of the market. How hard is 1% of the market? It's like, yeah, but you know, it's those kinds of considerations, right? Like, especially when there's, when there's a critical mass needed in, in, in order to actually move forward. It's like, you know, 1% is tough. Right. And then, you know, getting practical considerations. Right. Right. You're getting from 0.1% to 1% is tough.

**Dave Jones:** Simple things like in terms of dog food, how do you actually get your product onto the shelf in the local supermarket? Right. It's like, you know, it doesn't matter. You know, you can have the greatest ideas in the world, but you know, the practical considerations could kill you in the way the, the way the market works and the way the industry works.

**Chris Gammell:** Business is hard. Yeah, exactly. Circuit's good. Business hard. Oh boy. All right. Anything left on the list? I don't know if there is. Oh, I don't know. Oh, people should go.

**Dave Jones:** Oh, there was chip printing stuff. One of those flexible circus stuff, which, you know, excites you. And yeah, well.

**Chris Gammell:** Yeah. Subreddits. The IEEE. People should go to reddit.com slash r slash theamp hour. You can either add in, add your own stories throughout the week or just read stuff we didn't get to. And you can vote them up. You can vote them up, vote them down. You can make comments. You can yell at me for posting too much. Whatever you'd like to do. One thing that we should mention is Bunny, Bunny Huang has a great letter about releasing his book on hacking the Xbox. I haven't read that yet. That is a really cool letter. Right. You should. That's really good. Yep.

**Dave Jones:** I will.

**Chris Gammell:** Yeah.

**Dave Jones:** And there was something that got voted up here about a Raspberry Pi based pick and place machine for less than 2K. Once again, it's not going to happen. Practical considerations are probably going to kill it. I haven't even looked at it. And I can already tell you that practical considerations are going to kill it.

**Chris Gammell:** Yes, yes. No, no, no, no, no. Yes, no, no, no, no, no.

**Dave Jones:** That's what I like to think I'm good at, you know? That's what the experience brings you.

**Chris Gammell:** We can make the show like two minutes long, right? Go to the subreddit. Number one, yes. Number two, no. Number three, yes. Number two, no. Four, no. Done. Get out of here. See ya. Amp hour out.

**Dave Jones:** I don't have to do all the Mythbuster-style testing to know whether something's, you know, plausible or not.

**Chris Gammell:** Mythbusters is more like opinion givers.

**Dave Jones:** And I reckon probably 80% of the time I'm going to be right. Oh, yeah. You know, it's good enough for me. We've talked about it before. A pick-and-place machine is a low-end pick-and-place machine. It's just not practical. It has such a narrow window of usability that it's, you know, it's just not going to work. It can't work.

**Chris Gammell:** I don't know. Ian's doing that from Dangerous Prototypes, too. That's another thing we were looking at. He's got a Chinese one. He's got that 4,000-hour Chinese one. Oh, has he? Going through that. Oh, right. I haven't seen it. Does it work? Yeah. Yeah, it does. It's pretty cool. I mean, the menus are all in Chinese, but it looks cool.

**Dave Jones:** I thought they didn't do anything in-house. I thought they had a...

**Chris Gammell:** Yeah, they're starting to. They're starting to.

**Dave Jones:** Oh, right. Oh, why is that? They want more of the 10% cut than they're getting from Seed Studio?

**Chris Gammell:** Well, you know, reshoring. It's a thing. Oh, reshoring. Oh, wank word of the day, folks. Insourcing. Reshoring. Yes. Yes.

**Dave Jones:** Reshoring, yes. Okay. Oh, I'm going to have to have a look at this. Okay, it's only a five-minute video. There you go. Yeah, imagine that. Yeah, there it is. Yeah, I got those, actually. Boom. Oh, no, I do. I just uploaded a video that's only five minutes. Because I extracted it from another 20-minute video, which was in turn extracted from another one-hour video. Yeah. So, yeah. Yeah. Well, anyway.

**Chris Gammell:** All right, so last thing. Last thing for real. We've already got 400 responses for the survey. That's awesome. Excellent. Thanks, guys. So if you haven't filled out the survey from last week, please do so. Remember, we're giving away t-shirts. We're going to do drawings. More than one t-shirt. Don't worry about that. It's to people that participate. And for people that were filling comments in on the page that posted the survey, you actually have to fill out the survey to be entered in the contest. Bastard. So. Bastard. Thanks, everyone. It's been great feedback. You'd be surprised how many people think Dave talks over other people. I might have filled all those in. We'll see. Of course I do. That's my style.

**Dave Jones:** Take me or leave me. Talk over me, Dave.

**Chris Gammell:** Don't talk over me.

**Dave Jones:** Just don't try and change me. What?

**Chris Gammell:** What? I didn't hear you say I was too busy talking. I know. I know. All right, guys. We'll see you next week.

**Dave Jones:** Well, I won't because I won't be here. Oh, yeah.

**Chris Gammell:** I'll see you next week. Well, Dave's going on vacation. I'll be here.

**Dave Jones:** Yeah, you're doing whatever. I don't care. You can, you know. We'll see. Yeah.

**Chris Gammell:** Surprises.

**Dave Jones:** Couldn't care less. I'm taking a week off. Good. See you. Bye.

**Chris Gammell:** So before I was taking the dogs out, and I don't know why. I think because yesterday was St. Patrick's Day. Nah, right. I kept doing this voice. I said, look, look. I'm your farter. I'm your farter, Luke. What? I have no idea where it came from. Maybe my dog farted or something. But whatever it was, yeah, I started doing Irish Darth Vader. Yep. Luke, I am your farter. Oh, dear. That's sad. That's sad.
