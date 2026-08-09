---
episode: 58
title: Multicopter, DIY drones & Tektronix - Zappy Zendik Zoilism
url: https://theamphour.com/the-amp-hour-58-zappy-zendik-zoilism/
---

**Chris Gammell:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life.

**Dave Jones:** With a new mic, Chris. Yeah, how do I sound? Sound pretty good. I don't know, was that a peak there? I don't know, that might be our mumble server. It might have been. No, it was me, I think. You succumbed. You succumbed to the convenience revolution. Tell us about it.

**Chris Gammell:** Yeah, I finally gave... Well, so I mentioned in the show when it happened that my USB-based mixer broke. And prior to that, I had bought a real nice AT2020 XLR-based microphone. And basically when the mixer broke, I still haven't got... I haven't sent it back to get fixed yet, but I'm going to probably do that and then sell it. And in the meantime, I'm like, you know what? Screw this. I'm just going to go the Dave Jones laser route and buy a USB-based microphone.

**Dave Jones:** It's not lazy. It just makes sense. It just works. It does make sense.

**Chris Gammell:** You know, I was thinking about it too, and it makes sense from a traveling perspective. So if I'm on the road, I can just bring it with. Whereas before, I had to think, oh, I've got to bring a mixer then too. Exactly.

**Dave Jones:** And you don't have to bring your big arm. You just bring a little desk stand, you know, and you've got your good quality mic with you.

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** Yep. I know.

**Chris Gammell:** So I... Told you so. You did. You told me so. You're right. Yep. Although I will bring us right into the first rant of the day. I don't know if I'd get through security. Did you see the item I had on there?

**Dave Jones:** Oh, I did. This is freaking ridiculous. Only in America.

**Chris Gammell:** Oh, not only in America. Oh, come on. Well, maybe, yeah, because I guess...

**Dave Jones:** This is American shit again. Come on.

**Chris Gammell:** Tell us about it. Yeah, so in Jacksonville, basically, a mysterious box shows up at the City Hall. And I saw this actually from the Cree Twitter feed, which gives it away a little bit. But so a box shows up at City Hall, and they take one look at it on the x-ray scanner because they scan incoming packages because apparently that's what they do.

**Dave Jones:** Because they're paranoid to begin with. I guess so, yeah.

**Chris Gammell:** And I mean, there's been scares before, but yeah, they scan it. They say, oh my God, there's electronics in here. We got to call the bomb squad. And so... So they call the bomb squad and bomb squad takes the thing away and, you know, then...

**Speaker ?:** Yep.

**Chris Gammell:** Take it to the bomb range, scan it again, open it up and say, hey, wait a second, these are LED light bulbs.

**Speaker ?:** Yep.

**Dave Jones:** from the proper manufacturer. It came... It was addressed from a reputable supplier. They could have just made the damn phone call to the supplier and said, do you send us a package? What's in it? You know, what? Come on, it's ridiculous.

**Chris Gammell:** Yeah. Unbelievable. And it's just, you know, I look at it and I'm just like, it's only going to get worse, you know? As long as people... Oh, yeah, I know. ...don't understand electronics or aren't encouraged to look at electronics, I don't think we can... I mean, yes, we could blame movies, but really, we have to blame the...

**Dave Jones:** No, we blame the paranoid US government.

**Chris Gammell:** I mean, there's that, and I think just the, you know, it's a, you know, being a security guard is a low-paying position, and these are probably...

**Dave Jones:** There's something exciting to happen, right?

**Chris Gammell:** Well, maybe that, I don't know, but it's just, I think it's just a general idea that...

**Dave Jones:** Yeah, general paranoia in America, I'm telling you.

**Chris Gammell:** No, not general paranoia, I'm saying general lack of... Come on. Okay, yeah, you could say that, Dave. You know, we know you love your conspiracy theories and bash on the government here, but what I'm saying is that the reason it pisses me off is because it's just a lack of education about electronics, you know? Not everything electronics is a bomb, you know? Yeah, I know. And I'm sure there's some perception bias to if you're looking for bombs and you see something electronic, you're going to see a bomb, but...

**Dave Jones:** Because they actually have these new, I presume, laws in praise for improvised electronic devices. That's the latest buzzword now. They've drilled it into everyone that these improvised electronic devices are freaking bombs, you know? It's crazy. Yeah. I hear these stories all the time. Even years ago, it's not new. There's, you know, some school kid brings a science experiment to school, you know? He made this little thing with custom electronics and it did something, you know? And they called him the bomb squad. Yeah. Because, you know, even though he said, it's just my science experiment, and they went, no, it's not. It's an improvised electronic device. It's like, well, of course it is.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. It's my science experiment. Oh, it just makes me want to bash my head against the desk.

**Chris Gammell:** Yeah, and we've talked to vendors before about it, and we've talked to the people on Twitter before about it. It's tough anytime you have to travel with electronics, because at an airport, it's even worse. You know, every time I go through an airport with like a dev kit in my bag or something like that, I get really worried. And usually the best case scenario is if you put your cell phone in there with it, they'll see a cell phone, and then they'll see some circuits next to it,

**Dave Jones:** and they'll be like, you know? And if you've got cables in there, maybe it'll accidentally look like they're joined together, you know? Give me a break.

**Chris Gammell:** Yeah, so that was at a city hall, but man, it's just sad that there's not a recognition of what it is, because LED light bulbs are kind of boring too. I mean, it's not like there's a lot going on in an LED light bulb. There's some electrolytics, and there's some inductors, you know, basically an offline switcher, but...

**Dave Jones:** And I suppose the LEDs look like little bullets or something, you know? I guess so. They're like little 5-5mm LEDs or something.

**Chris Gammell:** I mean, if these are commercial bulbs, though, you'd think, well, unless these are going in like, you know, replacements for like halogen-based fixtures or something like that, if they've got like the Edison screw terminal, you'd think someone would look at that and be like, well, that's a light bulb, you know? Exactly. Or at least that's a bomb attached to a light bulb.

**Dave Jones:** Exactly. And I assume they're like all individually boxed and they're, you know, because they come from a reputable supplier, you know? And it's like, surely they would have looked like, you know, oh, look, there's a box of 20 items. Whoop-dee-doo, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** It's like, oh, it's crazy. And the thing I don't get is there's a video here, you know, there's a press conference and the police get up there and I don't know, the mayor, yeah, Mayor Brown, yeah, you doofus. Yeah, they get up there and they're not even joking about it, you know? They're not in, ah, it was only light bulbs, yeah, no worries, you know? Which is what would have happened here. But no, over there, oh, everyone acted professionally and in accordance with what they should do and we're very proud of all our Americans. Yeah, God bless America. Yeah, I did notice that.

**Chris Gammell:** We're very proud of how we responded to this and then it's like, well, are you ashamed of how people picked it the wrong way the first time, you know? like, it's a light bulb, come on. It's a light bulb, people. Yeah.

**Dave Jones:** Oh, it's ridiculous. Give me a break. Only in America, from the only in America files.

**Chris Gammell:** Oh, yep.

**Dave Jones:** Oh, we've got another one like that.

**Chris Gammell:** Oh, which one?

**Dave Jones:** Oh, that's the,

**Chris Gammell:** it's the shonky product of the week. Oh, okay, straight to that, huh? Should we go to, do we have the music? Ah, no, music still. No. New mic, not new music yet, sorry.

**Dave Jones:** Right, okay, because nothing's plugged into you, you know. your mixer doesn't work, right?

**Speaker ?:** Yeah,

**Dave Jones:** my mixtures. You've got nothing plugged in. All right. Yep. So, yeah, that segues beautifully into the wonky, shonky, what's it called? The wonky, shonky product of the week. The shonky tonk product, yeah,

**Chris Gammell:** whatever it is.

**Dave Jones:** Okay, whatever, yeah, that segment, the real exciting one. Where is it? It is the, it goes under many names, but it's the, it's the, the, the, no, no, no, no, no, this is the bomb thing.

**Chris Gammell:** The bomb thing, oh, okay.

**Dave Jones:** Yes, the bomb thing. Yes, we have two shonky.

**Chris Gammell:** Oh, we have two, all right. Yes, yes. I gave away next week's.

**Dave Jones:** You did. Yeah. This is the ADE 651, it's, you know, they give it a nice scientific engineering sounding product name, you know. Oh, okay, it's a bomb scanner, right? And, they've sold these to the American government, okay, and they, and they sold them to other countries and they're using them in Iraq and Afghanistan for bomb detection, right? But what is it? It's a freaking dowsing rod. If you don't know what dowsing rod is, Google it. Yeah. I think we can explain that here.

**Chris Gammell:** That's because that's like a cartoon thing too, right? That's where you have like the, the Y shaped stick.

**Dave Jones:** You get two coat hangers, right? And you bend them 90 degrees, right? So you've got two metal bits of coat hanger and you have one in each hand. And the idea is you walk along and you try and keep them straight. And every time you walk over, usually water, right? It usually, that's where its history comes from. It usually comes from water detection. And, you know, so you walk along and when you walk over water, all the thing that you're trying to detect, you know, people claim different things in this case, bombs and explosives and all sorts of stuff. Then the metal bars are supposed to suddenly move, you know, they move at 90 degrees and flick around and, you know, and it works on, you know, psychic energy and, you know, field force energy and insert wank word, you know, insert. I've got one. I've got one. Yeah.

**Chris Gammell:** So apparently on Wikipedia, they also call it dousing. They say dousing is also known as doodle bugging.

**Dave Jones:** Doodle bugging. I haven't heard that one before.

**Chris Gammell:** Apparently it's only in the U S but. Right. Citation needed.

**Dave Jones:** Anyway, it's also called the Ranger tell as well. And I think the U S government or some branch of the government has actually banned it now. And they're, they've sent out a press release to all their, a release to all their agencies, not to use it. Cause it's a scam. Yeah. And which is, which is exactly what it is. So, and you know, when you get, when it's advertised as, you know, it's a pretty fancy looking device. And when it's advertised as have it, as actually it doesn't require any batteries or anything else, you know, then, well, you've got to start to worry. It's like, Hmm. Yeah. Let's no, no,

**Chris Gammell:** it'll harvest wireless energy or something.

**Dave Jones:** Yeah. It harvests, the harvest. And now I don't know. You've got to go read it. It's real. We'll put the links in there, but it's ridiculous. And you can get these fancy plugin modules for different types of, you know, explosives or different things you want to detect with it. So the sky is the limit with this thing. You can just get a plugin module that plugs into it. No batteries. Of course you just plug it in. And magically it, uh, it detects all these plastic explosives. And of course, uh, James Randy is on the case. I love James Randy's brilliant.

**Chris Gammell:** Oh,

**Dave Jones:** the skeptic, uh, the skeptic, the James Randy foundational or whatever it's called. Yeah. He basically exposes all scams like this and, and he exposed it and he offered him the James Randy million dollars. Oh, speaking of Randy, I think we've got a caller.

**Chris Gammell:** I think you need to turn off your telephone. That's what I think.

**Dave Jones:** Randy from Hicksville.

**Chris Gammell:** And we should mention that it was actually Scott Harris who sent this in. Uh, he sent in a bunch of good ones on the suggestion page. Yeah. And, uh, we love when people send this kind of stuff in. It was awesome. That's, that's a good one. Yeah.

**Chris Gammell:** It's brilliant.

**Dave Jones:** So anyway, wonky and James Randy, yeah, he exposes all sorts of stuff like this. And he offers famously the James Randy million dollar prize to any skeptic or any other, um, company with shonky products, including the, uh, famous audio cables, you know, the, Oh, the, uh, monster. Yeah. The monster cables and all the rest. Um, yeah, he, he offers a million dollar prize. If you can, you know, scientifically prove that you can hear the difference. Who needs it? Yeah. Who needs science,

**Chris Gammell:** Dave?

**Dave Jones:** Those double, those pesky double blind experiments. Yeah. Right.

**Chris Gammell:** It's what it feels like. That's, what's important. How, how sciencey it feels, you know, that's what I'm going for.

**Speaker ?:** Well,

**Dave Jones:** that's what some general in Iraq or whatever in the, or Afghanistan or somewhere, some general came out and said, I think this, this product works, you know, this, this bomb detection product, it works. I know it works. I can feel it in my bones. You know, I don't need, you know,

**Chris Gammell:** I can feel it in his bones when it doesn't work.

**Dave Jones:** Yeah. Exactly. Yikes. Oh, anyway, what a scam.

**Chris Gammell:** Yeah.

**Dave Jones:** Unbelievable. But, but they duped, like they, they, they duped government agencies. They bought this thing.

**Chris Gammell:** Yeah. Like 800 bucks a pop or something.

**Dave Jones:** Oh, it's how much?

**Chris Gammell:** I think it's at 800 a pop for 800.

**Dave Jones:** No, I think it's more 80,000 or something. It's really expensive. I think it's hugely expensive anyway. But at least they had the good sense in the end to actually, um, get some department to run some tests on it. And sure enough, it didn't detect shit. You know, even when there was a truckload of explosive right next to it, you know, when they actually did the double blind experiment, it didn't work. Yeah. You know, go figure.

**Speaker ?:** Anyway.

**Dave Jones:** Science. But mysteriously, when, when, when somebody knows that the bomb is in there, it works. You know? Yeah. It's like, yeah, as all dowsing rods work when you know it's there, the mind works in mysterious ways. Uh huh.

**Chris Gammell:** Uh huh.

**Dave Jones:** Oh boy. There we go. Don't get me started. Chunky products. Yeah. And we've got a, another good one next week. Yes. Save it for next week.

**Chris Gammell:** Definitely. Let's get some shout outs. We haven't had shout outs in a while here. Do it. So first up we had, uh, so fake E equips, uh, that's, you know, a site that's been around for a little while now, but he actually, uh, made a bingo board for the amp hour. Have you seen this Dave?

**Dave Jones:** I wanted to see it, but it doesn't work here. I, I get error 404. I know. Oh, that didn't work.

**Chris Gammell:** Okay. Maybe just to go to the site or something. I'll, I'll try and fix the link there, but, uh, yeah, he's good. So there's a lot of fun. Bingo. Yeah. No, amp hour bingo. I mean, yeah, it's yeah. So we can get, you can get a, a mark for, uh, when Dave shows his age or when David insults the USA, we already got that one today. Uh, when Chris talk, when Chris, uh, starts a rant, we got that one today, man, we're, we're doing well. So, uh, he's got a couple of different incarnations and, uh,

**Dave Jones:** I want to see this fix the link, please. Oh, come on.

**Chris Gammell:** Just go to this page. You can go, you can find it. Come on, man.

**Dave Jones:** Little, little web food here. Come on. Little web food. Well, I did.

**Chris Gammell:** Oh,

**Dave Jones:** I'm sure I did. Where is it? Down there?

**Chris Gammell:** There you go, buddy. There's a, there's a little help from me. Oh, yeah.

**Dave Jones:** Bingo. Here we go. Okay. All right. Day shows his age.

**Chris Gammell:** Yeah.

**Dave Jones:** I'll send you a dollar. You can buy a clue. All right. Dave and Salty. Yeah. Homemade IC argument.

**Chris Gammell:** We could just do this right here. We should, we shouldn't be looking at this because, uh, we could, we could just do it off, do a line in a row and, and everybody would win, you know? This is,

**Dave Jones:** this is brilliant. This is like a template for the entire show. Mighty O makes a guest appearance. Right. Next week.

**Chris Gammell:** Maybe. Who knows?

**Dave Jones:** A, a non electronic related tangent. Yeah. Open source discussion. In reference to Dilbert world.

**Chris Gammell:** Yep.

**Dave Jones:** Discuss green technology. We kind of got one of those in today. Yeah. Talking about the LED light bulbs.

**Chris Gammell:** It's kind of sad that we really fit in the same mold every week. Maybe we should start branching out here today.

**Dave Jones:** I know. Maybe we should. Women in engineering discussion.

**Speaker ?:** Yeah.

**Dave Jones:** Hackerspaces. Oh, one that's missing. Ham.

**Chris Gammell:** Ham.

**Dave Jones:** You're always talking about Ham now. You're right. You're right.

**Chris Gammell:** That's, that's gotta be the next, the next gen. Well, he's got a couple more, so we'll have to, we'll have to post that up, but yeah.

**Dave Jones:** I don't know about Jerry Ellsworth makes a guest appearance. Come on. What? She's only been on once. Twice now. Twice. Twice. Oh, there you go. Okay. Fair enough.

**Chris Gammell:** She's no Jeff Kaiser.

**Dave Jones:** Right. No.

**Speaker ?:** Okay.

**Dave Jones:** You heard it here first, folks. Jerry Ellsworth is no Jeff Kaiser.

**Chris Gammell:** Yep. Yep. I wrote in the, in the comment section of, of the site once, I was calling, I was calling him the, Ed McMahon of, of the amp hour. I think, I think I want that to stick, you know, cause, right.

**Dave Jones:** Yes, sir.

**Chris Gammell:** I don't,

**Dave Jones:** I don't get that. I don't get the, Oh, so on,

**Chris Gammell:** uh, Oh, crap. Johnny Carson. So Johnny Carson was a show, a late night show in the U S real famous one, right? And, and, uh, Ed McMahon would just sit on, on every show. He'd always be sitting there on the couch and all these, all these celebrities would come out. They'd, he'd always just be there, you know, cracking jokes and he'd just be there. So that's, that's our Jeff. Right. Jeff Kaiser is our, uh, our Ed McMahon. There you go. Fair enough. Okay. Uh, let's see another shout out. So, uh, new podcast, a little bit young, but, uh, it's up and coming and they call it zombie tech, zombie tech, because cool talking about how, how to serve things. That's like the basic question. I think they've been asking all their guests, you know, how, uh, you would survive the zombie apocalypse. Yeah. Yeah.

**Dave Jones:** I keep hearing about this zombie apocalypse. See, I'm not into zombie movies. It's a, it's a, but it's a very geek thing. If you, if you are, then you're passionately into everything zombie. Yeah. I, you know, yeah, I don't know. And everyone talks about the zombie apocalypse.

**Speaker ?:** Yeah.

**Dave Jones:** Zombie apocalypse. I'm going to get that word right. I'm a professional radio announcer.

**Chris Gammell:** There we go. There we go. Yeah. So, I mean, they, they are electronics. It's so, it's the toy makers crowd, uh, that toy makers hangs out with, uh, you know, Savage Circuits people a lot. So it's kind of like that, that crew and, uh, you know, good people there. They talk about some fun stuff and, and, uh, they've been picking up their, their podcast stuff and yeah. So welcome to the scene. I, I love it when more people come on the podcasting scene, you know, I need, I need stuff to listen to. And, uh, absolutely. I can't listen to Dave anymore than I already do. No,

**Dave Jones:** I know it's pretty tough, isn't it? Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** No, it's excellent. I went to this, I've downloaded it, but I haven't listened to it yet. Um, one thing I don't, I, I want to see on this site is a, uh, is, is a way to actually play it right there on the site. Like we do with the air power. Cause I, that's what I do with ours. You know, I, once we finish the edit, I do actually listen to the air power back to, you know, because it does sound different after, well, it sounds different to me anyway, after it's edited and I don't know, just sounds, yeah. So anyway, I usually listen to it again and I play it through the website. So I use the little player there and I like just being able to hit play and, you know, it starts rather than have to download the whole thing. And anyway, it's just, yeah,

**Chris Gammell:** we use pod press. If people don't know, we, cause we have a WordPress site. So nice and easy way to do it. If people are thinking about starting to start a podcast,

**Dave Jones:** definitely use pod press makes it easy. And then you get all the stats and yeah. And then it integrates into all the RSS feeds and generate, handles all that for you. It's really nice. That is nice. There you go. So everyone should get a mic, a USB mic, right, Chris?

**Chris Gammell:** Oh yeah, definitely.

**Dave Jones:** And start a podcast radio show. Cause there's not enough out there. Really? I don't think.

**Chris Gammell:** I don't, I don't think so either. I mean, I think there's a lot of, there's some, at least in the electronic side of things. I mean, like you can get into the tech side of things. I mean, there's a whole twit network and they have tons of shows, but if you want to get away from the gadgety side of things and, you know, shoot some bull about electronics, you know, there's, there's only so much. They got hand nation, which we do occasionally. Yeah. Well, we don't want to do it too much. Speaking of electronics though. So there's a new site that might've been inspired by you. Is that right, Dave?

**Dave Jones:** Yes, I think I do believe so. They contacted me very early on and told me about it. And they mentioned that I think they were, yeah, they saw my show and they liked it and they thought they'd do their own, which is absolutely brilliant.

**Chris Gammell:** Yeah. So it's called the signal. Oh, go ahead.

**Dave Jones:** Yep. No, it's called the signal path.com.

**Chris Gammell:** Yeah. And so it's all YouTube based, right? And,

**Dave Jones:** and it's all, it's same as mine. It's all a YouTube based past. They have like a, you know, a blog site as well, which they post to. Yeah. So yeah, it's pretty much the same format as mine and yeah. And it's excellent. The content's great.

**Chris Gammell:** Yeah. It's a bunch of guys from Toronto, I believe. And they talk about a lot of, you know, it seems like more like basic concept kind of stuff, like talking about like their, the first post right now is about op amps and PWM and, you know, so definitely useful stuff and, and more of a, you know, like the straight technical stuff. So maybe a little less off the cuff and more planned out, but definitely. Yeah.

**Dave Jones:** Mine's more random. Yeah. There's this pretty much focusing just on, you know, how things work, circuit techniques, things like that. So yeah, it's excellent.

**Chris Gammell:** It's great though. Yeah. So welcome to it guys.

**Dave Jones:** And they do have a tear down too. There's actually a product tear down there, which is quite good. I've watched that.

**Chris Gammell:** Yeah.

**Dave Jones:** And yeah,

**Chris Gammell:** that's good.

**Dave Jones:** Excellent show. I don't mind competition at all. It's good. I encourage it.

**Chris Gammell:** Keeps Dave on his toes.

**Dave Jones:** Speaking of which, I should link to them from my site actually. Yeah. Because if, if you're producing good, original blog content, tell me, and I'll add your link to my site. And yep, you'll get, hopefully get a lot of hits from it. Cool. Because I like encouraging other people who produce original content.

**Chris Gammell:** Me too, man.

**Dave Jones:** Yep. Love it.

**Chris Gammell:** Hmm.

**Dave Jones:** Speaking of Roy Eltham before, I, I'm pretty sure it's him. Excuse me if I'm wrong, but I follow him on Twitter and he always tweets these updates. He's got this jogging thing where he, he, he actually goes out jogging. He must have like a sensor in his, you know, shoe or some GPS sensor or something. And you can follow him on a map where he's jogging.

**Chris Gammell:** That's pretty cool.

**Dave Jones:** In live. Yeah. It's very cool. So I might have that wrong. Sorry, Roy. No, I think that's you. I think you're right. I think that person.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Speaking of, it's just cool.

**Chris Gammell:** Better hope that doesn't go on with a zombie movie, right?

**Dave Jones:** Yeah. The, the, the zombies are fighting. Yeah. How not to survive the zombie apocalypse. They can attach a GPS sensor to you and, and stream it live on the internet. there you go.

**Chris Gammell:** There you go. And,

**Dave Jones:** and it's overlaid on Google maps. So they can,

**Speaker ?:** you know,

**Dave Jones:** it's easy. So you can watch them in, in real time. Like it was running along the beach the other day. I clicked on it and I could see him moving along the, next to this beach, you know, somewhere. It's very cool. Yeah. You can stalk people from a distance. Yeah. Right. Brilliant. Yeah. It's, you know, like, like some criminal, you've got a GPS, you know, ankle bracelet on, you know, and they can follow you everywhere you go. How would you defeat one of those, you know, GPS ankle bracelets? I, I, I'm sure, I'm sure they have those in the U S don't they? Yeah, they do. If you're a criminal and you get, get released on, on parole or something and they want to track your movements because you're dangerous or you're, you know, you're dodgy or something,

**Chris Gammell:** then they strap a GPS ankle. Because I think that they, uh, they do it with like a check-in signal. So it's not just like a, you know, uh, it doesn't just receive stuff. It actually has to bleep like I'm alive. I'm alive. And here I am. Right.

**Dave Jones:** And, and if they lose the ping, then the, then they rush to your door and try and hunt you down with shotguns. Right. That's right.

**Chris Gammell:** So you got to try and either duplicate it and then, you know, take over that signal or I don't know. Oof.

**Dave Jones:** That'd be cool. Well, you'd need an RF, um, scanner to actually scan what it's pinging out and what it's receiving. And then you could duplicate it. Yeah. There you go. There's a, there's a nice project for someone. Yeah. For a criminal that happens to be. Anyway, it'd be technically fascinating.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. I like it. I think it'd make a good project.

**Chris Gammell:** Well, speaking of breaking the law, how about we talk about, uh, things that almost destroy cars,

**Dave Jones:** but then they would blow you up because it's an improvised electronic device.

**Chris Gammell:** Oh yeah. No, that's, I think that's more movie stuff. I don't think, uh, yeah. Sorry. So yeah. How about we talk about this, this video, Dave? What do you think? You seem, you seem to like it when I showed you it before.

**Chris Gammell:** I almost wet myself.

**Chris Gammell:** So tell us. So I, I watched the DIY drones list, you know, I, and you're doing a, you're doing a, uh, hexapod soon, aren't you? Didn't you say you're doing that?

**Dave Jones:** I am. Yes. A friend and I are going to try and build a canyon navigating, uh, hexcopter. Yeah. So I watched, if we could find the time to do it, you know, we're on the verge of starting it, buying gear and yep.

**Chris Gammell:** Yeah. So, uh, you know, the, it's why I watched the DIY drones list. It's because it's cool builds and, you know, great news and stuff like that. And so they posted a really interesting story, uh, the other day. And, and, uh,

**Dave Jones:** I'm sorry, we're, we're, we're laughing because we've seen the video. We've seen the video. Yeah.

**Chris Gammell:** So basically there was a, uh, electronic multicopter. So helicopter being, you know, like single or dual rotor one, you know, one sideways and one, uh, horizontal. And think about a multicopter being like a quadcopter, but just with more rotors. And this guy was riding in it. So I hadn't really ever seen. So I think it was a couple of different things. It was, it was, uh, you know, they, you don't normally see like electronic helicopters, right? Just because of the power density you need in order to actually get lift, you wouldn't be able to fly for that long. And then the redundant backups and everything, it's just much more, uh, much more plausible to use, uh, fuel. Yeah. Fuel based motor. Right. And, uh, so this guy's trying it with a bunch of batteries and a couple rotors. And, and we're kind of calling this into question if this is legit. We are. Yeah. It doesn't look legit, but it doesn't really matter because it's so hilarious. But basically this guy is, well, Dave, why don't you take it from here? I'm sure you'll give a great narrative of what you saw.

**Dave Jones:** This guy's, first of all, he's, he's, in his front yard. Okay. He's on his driveway. Picture this. He's, he's there on his driveway in this big quadcopter. It's got like six blades on it. He's sitting in the seat there and, and he starts it up and the person who's filming it is hiding behind the garage or something. Cause they don't want to get their head chopped off. And so he's sitting there and he starts it up and it sort of does a few little bumps and tries to get off the ground. And then it, and then it tilts backwards and it drags himself backwards down the driveway, almost onto the road. And it looks like blades fly everywhere. You know, it's just, we don't want to like, award winning. Yeah.

**Chris Gammell:** Like he would have been, he would have definitely won a Darwin. Like the guy's not wearing a helmet. He's wearing a hat. He's not wearing a helmet.

**Dave Jones:** He's wearing a cap, right? As you call them in the U S and he's wearing a t-shirt and shorts. And there he is, you know, and here I'm watching it now and it sort of tilts back. And there he goes, whoa.

**Speaker ?:** Oh,

**Dave Jones:** I can picture him hitting the kill switches. Yeah. And there it is halfway on the road.

**Speaker ?:** What?

**Dave Jones:** You gotta be shitting me. Right. And it looks fake. Cause it's very grainy footage. And, and the sky is perfect.

**Chris Gammell:** Wherever he was filming, it was just, it was perfect weather, you know?

**Dave Jones:** And I don't know. There's something about it. It just screams, you know, fake. Because if it was me, I, you know, and I would have, he would have spent months building this thing, right? It's a huge build. Yeah. And surely you'd be so proud of it that you'd do a video like, you know, showing people the quadcopter first. Here's my, here's my, you know, personal quadcopter. It's going to revolutionize the world. And here's the batteries and, you know, everything else. You'd show people around it, but no, all we get is this grainy footage of somebody behind the garage, watching this quadcopter, try and take off from the guy's driveway. Yeah. I, I don't know. I don't know. Apparently he's a member of the do it yourself drones forum. Yeah. So, you know, I don't know. Apparently there's no other details about it. So this is the first time anyone's heard about it. It suddenly magically appears this.

**Chris Gammell:** Right. So take it with a grain of salt. I mean, there could be, you know, it could have been faked. I mean, it looks kind of like digitally enhanced, but it's, it's so hard to tell these days. I mean, it's,

**Dave Jones:** but the funny thing is, he didn't bother making it a public YouTube video. It's a, it's a private one. And he claims that he doesn't want it to go viral. Cause it's embarrassing.

**Chris Gammell:** Yeah.

**Dave Jones:** I think he missed a perfect golden opportunity there to go viral, get a million hits. And then YouTube would come running to him. Oh, you want to be a partner? And you know, I, yep.

**Chris Gammell:** Yeah. Anyways, he, he, he also talks about the actual system. I mean, that was another thing that was interesting to me. I mean, aside from the hilarious video and I'm glad he's safe to be, to be honest, I'm glad he's okay. But, uh, he's talking about, so he actually was using, he was doing a, you know, I think he was, I mean, it was from battery. So it was all DC and at least to start, I'm not sure if he goes to AC, I can't imagine he would, but, um, so he's using lots of MOSFETs though. And, uh, and he calls them, what does he call them? Magically obliterating smoke and fire emitting transistors. He's a MOSFET. Yeah. Yeah. So he's probably using like an H-bridge or something like that to drive the motors or whatever, however he's doing it, you know? Um, yep. But basically one failed short. And so his whole system, yeah,

**Dave Jones:** but I did see some smoke coming out of one of the rotors, one of the motors there. There's sort of, you can see it. And he claims that the poor video quality is cause he used USB instead of fire wire to copy it off the camcorder. Yeah. Yeah. I, I don't, I, I hope it's real cause it's so freaking hilarious, you know? And it's,

**Chris Gammell:** it's interesting reading about like just the technical challenges he's talking about. I mean, and this stuff makes it seem real at least. So, I mean, again, we still have to be a little bit skeptical about this, but he was talking about adding snubbers across the MOSFETs to, you know, reduce the ringing and, uh, adding fuses. I was kind of surprised he'd hadn't thought of that, but maybe if he's newer to design, you know, maybe he just did use a, I guess there is no line fuse there. So there's no thing there, but he's going to put fuses on the, on the, on the rails at least. So high current dumps when you're, when you're fat fail short, you know, that, that'll burn up. But, uh, man, that's crazy.

**Dave Jones:** Yeah, I know. It's just insane. And seriously, he could have easily won a Darwin award there. One of those blades could have chopped his head off. You know,

**Chris Gammell:** I'm just really glad he didn't get more air. I mean, like he kind of tilts and he gets like maybe a half second of air, but imagine if he did get up, you know, 20 feet in the air and then,

**Dave Jones:** yeah,

**Chris Gammell:** well then what?

**Dave Jones:** Well, I, I'm interested to know, is it fully manual control or is it, um, is it actually, you know, like a real quad cop, is it, is it actually stabilized via, via computer? You know, um, is it,

**Chris Gammell:** I don't know. Well, usually the algorithms, right?

**Dave Jones:** They're very, they're so difficult to control manually that you can't almost, you've got to have them, you know, gyro stabilized. They've got to actually have tilt sensors in. They have so only software can do it quick enough to actually keep, keep a, um, keep one of these things stable. So I don't think he could drive that manually. That's if he is, if he did, that's probably why he crashed.

**Chris Gammell:** Well, no, he said the, the, the FET failing is what did him in, but.

**Dave Jones:** Oh, well, yeah, I, anyway.

**Chris Gammell:** Yeah. I would say next time, buddy, try it on grass. That would probably be it.

**Dave Jones:** Try it in a park. Yeah. Yeah. With one of those full, uh, mesh, you know, chainmail suits on, you know, those old fashioned, you know, medieval chainmail suits.

**Chris Gammell:** The black knight. Yeah.

**Dave Jones:** The blade doesn't come in and chop your head. It's just a flesh wound. Anyway, we will embed the video because it's so hilarious.

**Chris Gammell:** It's, it's a good, it was good. I liked it.

**Dave Jones:** Anyway.

**Chris Gammell:** Oh,

**Dave Jones:** we're, we're probably ruined it for everyone. We probably should have just said, watch this video. It's freaking. Yeah. You know, I don't know.

**Chris Gammell:** Yeah. Sorry. If we have ruined it for you,

**Chris Gammell:** we have news. We do go ahead.

**Dave Jones:** This week, including making fun of Chris.

**Chris Gammell:** That's great. Yeah. Anyway,

**Dave Jones:** the latest news as of today, August 30th here in Sydney, at least, Tektronix have, are releasing a new oscilloscope, groundbreaking oscilloscope. And it's revolutionary. Go to a scope revolution.com. And they, it's all starting today. You can watch the videos and webinars and all sorts of stuff, including other content from someone you may know. And yeah, you can get behind the scenes looks at how the scope was developed and, anyway, it's, and you can win 30 grand in prizes or something. Wow. So yeah, if you want to know all about it, go to scope revolution.com. It's happening today and they claim it's the biggest, you know, advance in a long time. And it includes analog, digital, and RF. That's all we know. There's this mysterious black silhouette scope on the website. I'm signed up. There you go. You signed up?

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Excellent. Anyway, I wanted to say more about it, but Chris vetoed it because he's a pussy.

**Chris Gammell:** Yeah, a bit, a bit.

**Dave Jones:** Yep. And we might be able to explain next week when the news is old.

**Chris Gammell:** Yeah.

**Dave Jones:** But anyway, yep. I didn't want to ruffle feathers here on The Amp Hour hosting panel. So I said, yeah, whatever, Chris. Okay. You can be a pussy if I can make fun of you on The Amp Hour. So there you go.

**Chris Gammell:** That was our deal. Dave is allowed to make fun of me.

**Dave Jones:** Yep. You're a pussy because as you can probably tell, I know a little something more. So yes. Anyway, it's August 30th here in Sydney. See, Chris is concerned because it's not August 30th over there in the US of A, which is the center of the world.

**Chris Gammell:** No.

**Dave Jones:** Yes. Come on, you guys. Anyway, it's happening at 8 a.m. Pacific Daylight Time, August 30th. So that's like, I don't know, 6 p.m. tonight, Sydney time or something. Whatever.

**Chris Gammell:** One p.m. Anyway, it's all happening.

**Dave Jones:** ScopeRevolution.com. Check it out. And I can say, I think it will be cool.

**Chris Gammell:** Yes, he can say that.

**Dave Jones:** Yep. Anyway, check it out. And we can talk about it next week.

**Chris Gammell:** All right. We'll do that. Pussy.

**Chris Gammell:** Yeah. So did you see this thing where there was a rumor about TI possibly selling off the OMAP?

**Dave Jones:** I hadn't heard about it until you put it on the list. But yeah. Why?

**Chris Gammell:** Why might they sell? It's my first question. Well, first off, they said that they will not sell.

**Dave Jones:** Right. Are they trying to kill the rumor? I don't know. Maybe they're trying to pull an HP. Or are they trying to start one?

**Chris Gammell:** No, I think, well, they, so the rumor, or whatever it was, you know, the conjecture was started by E.E. Times, you know, weirder things have happened, right? Right. And basically, finally, like a day later, they said, no, no, no, we're not selling that. I'm not sure where they got their, they probably got some kind of, you know, anonymous tip or something like that. And they wanted to crack the story.

**Dave Jones:** Right. Okay. Yeah.

**Chris Gammell:** And, and, you know, it doesn't mean that they still won't, but it just means that at the time they said, no, we're not doing that.

**Dave Jones:** Why can't we do that here on the Ampound? Why can't we, if you, if you work at a secret, if you work at a company and go, you know, use like a, a secret email account, email us rumors, and we'll put them on the air. That'd be awesome. That would be, yeah. I was going to say, Hey, I'm safe. I'm in Australia.

**Chris Gammell:** Yeah. Yeah. No worries. Chris will get sued. Definitely no Australian people that have ever gotten sued for leaking information before, Dave. No. Yeah. Or anyway, extra dated or anything. Right. But yeah, I don't think that would be a big deal.

**Dave Jones:** Talk about it next week. All right.

**Chris Gammell:** What?

**Dave Jones:** I want to talk about it today. It's August 30th here. Oh,

**Chris Gammell:** you're still talking about that, huh?

**Dave Jones:** I am still talking about that.

**Chris Gammell:** Yep. Yep. Yep. Anyway. Anyway. Yeah. So they said, they said, no, I mean, they're, they were talking about Intel buying it. I mean, the thing is with these big companies, you know, like TI selling Intel, it's like, well, if they keep it around, who gives a crap? You know, like, and they're basically, the idea was no Intel, or they're saying that Intel doesn't want to necessarily just use the Atom anymore and they need another, another platform. But the thing is like the OMAP and the Atom, I think they're kind of in this, they're starting to converge in the same spaces, you know, Atom is not that small of a processor.

**Dave Jones:** Yeah, but isn't the Atom still just a processor? Whereas OMAP has everything in it. It's got display drivers and the whole works. I don't know. I haven't been following the Atom thing. Is it like an integrated micro kind of, I thought it was just like, no, it's just a raw processor. Yeah, that's true. You've got to add everything around it to make it useful. Yeah, that's true. Whereas the OMAP, and the OMAP they're using tablets and they're using, you know, all sorts of, you know, gadgets, because it's, everything's built in, you know, it's got a LCD drivers and, and memory built in, you know, we talked about it before. It, it has the, it has the flip chip RAM on top of it inside the one chip. The, the, it has a second die in there sitting on top, which actually has the memory on it. So, which is absolutely brilliant.

**Chris Gammell:** Yeah.

**Dave Jones:** And yeah, didn't we talk about like the thousand page data sheet or something?

**Chris Gammell:** 5,000, I think.

**Dave Jones:** 5,000. That was with Jack Gansel, was it?

**Chris Gammell:** Yeah. Yeah, I think so.

**Dave Jones:** I think we, yeah, we, we discussed that. But yeah, it's very cool.

**Chris Gammell:** Yeah. Uh, yeah. And I mean, we can hear more about it next, actually. So next week we should announce that, uh, Jason Kreidner, the Beagle Board Project is supposed to be on the show. Um, so we can ask him more about the OMAP itself, but, um, I don't know. It's, I thought it was more interesting from a, you know, rumor and response kind of thing because E, E, E times is all miffed that, you know, the, uh, that they didn't respond right away in the first place, but. Yep. So I don't know. It was. Maybe they're,

**Dave Jones:** well, maybe the rumor is true and they're just, you know, they're not allowed to say because they're a bunch of pussies as well.

**Chris Gammell:** Yeah. Dave's, Dave's new favorite word. Yeah.

**Dave Jones:** I just, yeah, I just like it. I hate secrets. Like a big open world, you know, it's much nicer. Anyway.

**Chris Gammell:** Yeah.

**Dave Jones:** I do keep secrets. You know, if I'm contractually obligated to keep secrets, then I do.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Yeah. Anyway, not happy.

**Chris Gammell:** I know.

**Dave Jones:** Oh, Matt, but why? Yeah, that's a, I'd, I'd love to know where the rumor came from.

**Chris Gammell:** It actually says on here, it says, yeah, it says on the, actually kind of a good name for a site, the technology news site, semi-accurate.

**Dave Jones:** That's a good, I like that. That's a good name. Oh, that is brilliant. Yes. Semi-accurate. There you go. You'll post your rumor. Maybe we should use that as a rumor source, you know? Yeah, there you go. Well, we can talk it up semi-accurate.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh, that's brilliant.

**Chris Gammell:** And they were actually talking about, uh, Broadcom trying to buy it maybe, but I don't know. That's all this kind of big, big chip manufacturer games, you know, like it's, I don't know, as long as they don't kill the chip, it's not that big of a deal for the, the end, the end product people. And, uh, and actually that's what got me talking to Jason and ask him to come on next week is, you know, I asked, you know, what happens if the OMAP actually did get sold? And he said, well, not too much really. I mean, it's, he's, he's tried to keep the Beagle board separate. So, uh, right. Yeah. So we'll hear more about that next week though. Yeah.

**Dave Jones:** I, I can't see any reason why they'd sell it. I don't, are TI in financial trouble? I didn't think so. No,

**Chris Gammell:** I don't think so. No.

**Dave Jones:** No. And, and it's a massively popular product as far as I know. But, uh, yeah, if they did, well, maybe other companies have realized it's massively popular and they want part of the, and they want the action. So they're willing to pay a, a crap load for it. Yeah. I don't know.

**Chris Gammell:** Yeah.

**Dave Jones:** No idea. Interesting. So yes, if you've got a good rumor, send it to us.

**Chris Gammell:** Dave wants your secrets. He's willing to pay.

**Dave Jones:** But if it involves certain companies that Chris is scared of mentioning, then yeah, it won't get on the show.

**Chris Gammell:** Yeah. Pussy. Yeah. Well, yeah. That's, that's four times now, Dave. Four times. I think you topped out at five.

**Speaker ?:** Okay.

**Dave Jones:** Does that, right. So I've got one pussy left, have I?

**Chris Gammell:** That was it right there. Oh,

**Speaker ?:** damn it.

**Chris Gammell:** So speaking of TI, they actually, they, they came out with a new mobile, mobile app, mobile. I don't know. Have you ever, do you ever use the mobile, mobile stuff like the Mouser or the DigiKey apps?

**Dave Jones:** God, no. I barely even use my phone. Oh, okay. It just, you know, it's never, never, never has charge. I don't make, I don't talk to people on a phone. I don't, I don't talk to people. Cause I, cause I sit in front of a computer, you know, 18 hours a day. I don't, I don't need to use my phone. I don't go out anymore. You know, I stay at home. Yeah. I don't know. I mostly eat through a straw.

**Chris Gammell:** Yeah. Yeah. Right. I don't know. I just, I think about it, like even like any kind of apps like this, you know, like I, I found one actually, I, I just wrote about how I got a Nook and, and I actually got Android on that thing. But, uh, you know, I found a circuit app on there and, and it was kind of silly. It's like, it's, it's like beginners, like doing resistive dividers, stuff that if you're using that app, you probably shouldn't be working on circuits, that kind of thing. But, uh, um, yeah, this, I don't, I don't know. Like, I feel like there could be some usefulness in like mobile apps from like, like, especially like DigiKey and Miles or like distribution, people that are going to ship, be able to ship you stuff directly. That could have some use.

**Dave Jones:** they've come out with all these apps. And so, I think fine chips have got an app and all that, you know, like, well, you know, you're really not going to do that sort of work on your phone. Yeah. It's, I, I just, no, I don't see it. I think they're just doing these apps because they can, and they think it's cool. And they think, you know, it's not, people aren't going to use them. Well, this,

**Chris Gammell:** this thing looks like, it looks like a part lookup table, you know? So it looks like they might've just developed it for their Salesforce, which is monstrous. And then they said, well, okay, let's just push it out to the public. And if that's the case, it's like, well, yeah, don't expect people to use it, but yeah. Yeah. I know my friend has used the, the digi key, like, cause they have like a scanner built in, so you can just take a picture of the label. He said that's pretty useful. okay. Right. Yeah. Yeah. I can see that.

**Dave Jones:** Fair call.

**Chris Gammell:** Yeah.

**Dave Jones:** So you can just go through with your phone around the workshop and you can just scan all the things and yeah, I need to reorder those. Yeah, exactly.

**Chris Gammell:** Yeah. That's the idea. I mean, if you keep the label around, if you're, if you're a person that likes to put the bags in or, you know, like put your parts into bins, then you better get to keep the UPC with or whatever. So,

**Dave Jones:** or if the labels don't fade, which I ranted about on Twitter. Yeah. Once I went to look through my box of parts and all the digi key labels are freaking worn off. They've, you know, all of the prints just, you know, vanished. Like thermal printed or something. Yeah. They're a thermal thing. You know, so I tweeted it, you know, big, angry tweet, you know, and, really get that emotion out, you know, and digi key replied and said, Oh yeah, we're aware of that. We've fixed it. All new labels shouldn't do that. You know, sorry. It's like, yeah, bloody annoying. Anyway, there are apparently ways to read it though, because even though it's faded away, you can, under certain thing, and there's, you know, you can do certain things to it. I don't know. You can apply something to it and it can come back. Somebody tweeted a couple of things. Like lemon juice? Like a, like a 10 year old spy kit kind of thing. Yeah. That's it. Yeah. Lemon juice. Oh boy.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. There is a map on the back of the Declaration of Independence. That's right.

**Chris Gammell:** That's horrible movie.

**Dave Jones:** Yeah. Oh, it's great. Come on. It's a great popcorn movie that one.

**Chris Gammell:** I don't know. I'm not a big Nick Cage fan myself.

**Dave Jones:** Right. Yeah. Yeah. He's made some shockers. Let's not go there.

**Chris Gammell:** Yeah. Yeah.

**Chris Gammell:** Hmm.

**Chris Gammell:** So, uh, speaking of people that say bloody and talk funny like you, uh, do you see this, uh, make magazine that, uh, pointed out this, another YouTube, uh, star, but he does high voltage stuff. Do you see this guy?

**Dave Jones:** Yep. I'm well aware of him. He's a, uh, very popular fellow on the EV blog forum. People like, people call him the nutter. The nutter. The nutter.

**Chris Gammell:** Yeah. He is crazy. Yeah. He is crazy. Yeah. Yeah. And, uh,

**Dave Jones:** he does these weird high voltage, high energy stuff in his, in his apartment or his attic. I think it's his attic. I saw. And, and he, and he stepped it up a couple of months back. He actually got this, uh, woman on, you know, to look and talk all sexy. And yeah, I saw that one. It was, it was hilarious. Oh boy.

**Chris Gammell:** Yeah.

**Dave Jones:** He's anyway. Yep.

**Chris Gammell:** He's crazy.

**Dave Jones:** He's built up quite a cult following. So, so his, yeah,

**Chris Gammell:** his, his first one on here, he's, he says, it says it is erasing a CD with, high voltage, but he's basically just obliterating a CD. I mean, he's just removing all material from it. It's amazing.

**Dave Jones:** I know.

**Chris Gammell:** Yeah.

**Dave Jones:** And, and people have called into question his knowledge and ability and stuff like that, you know, and safe use of safety.

**Chris Gammell:** Maybe. Yeah. Yeah.

**Dave Jones:** So he, I think he actually responded to that and he did a whole video on safety or something, I think. So here we go.

**Chris Gammell:** Big capacitor safety. Yeah. Nice.

**Dave Jones:** Yeah. Anyway, it's freaking hilarious. Yeah, I know.

**Chris Gammell:** Wow.

**Dave Jones:** In a, yeah.

**Chris Gammell:** In a real. In a 38 microfarad, five kilovolt capacitor. Wow. That's unreal, man. Some people, you know, they just keep stepping it up. They're like, oh, well, a hundred volts. Yeah. Why not? You know, a thousand volts. Okay. A hundred thousand volts, you know, like,

**Dave Jones:** he's just going to buy the biggest shit he can on eBay. Yeah. Yeah. Yeah.

**Chris Gammell:** He's got like, those are like transformers from,

**Speaker ?:** man,

**Chris Gammell:** that's like power line stuff. That's crazy.

**Chris Gammell:** Yeah. I know. It's nuts. That's cool though.

**Dave Jones:** No, I know. Yeah. I got a bit. And blowing shit up on YouTube gets views. I'm telling you. It does. That's it. If you want to, if you want to become a YouTube celebrity, just blow something up. So that's why I'm telling you that quad copter guy, Mr. Golden Opportunity.

**Chris Gammell:** Almost blowing himself up.

**Dave Jones:** Yeah. Well, almost killing himself. Yeah. Darwin award winner. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Cause yeah, those, that sort of stuff, you know, even, you know, if you injure yourself or you'd nearly kill yourself or you blow something up, you know, guaranteed views. Or if you have stupid cats that do something funny. Yeah. Hey cats.

**Chris Gammell:** Yeah. I'm not a big fan either.

**Speaker ?:** Hmm.

**Dave Jones:** We've got a, uh, there's a scam on Kickstarter. Did we talk about, we didn't talk about this. We didn't talk about this. No, we meant to.

**Chris Gammell:** Yeah.

**Dave Jones:** What is it? It's, um, for some,

**Chris Gammell:** what's, what's the project? Oh, so it was a, uh, it was a light. It was basically like a, a outlet controller, basically. So a computer controlled outlet. So for flipping off lights, it's flipping off, uh, right.

**Dave Jones:** So it's a home automation type. Yeah. Yep.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** It's called the, uh, tech sync power system.

**Chris Gammell:** Yeah, that's right. And basically, uh, so it was geekscape who wrote about this and, and, and I follow Andy on, on Twitter and that's how I found out about it, but he did a pretty good review about it cause he was a backer, you know?

**Chris Gammell:** Right.

**Chris Gammell:** I, I, I can imagine that would be very frustrating if you're, you know, you emotionally buy into a project like this and then, Hey, it, it was a scam. Sorry. Uh,

**Dave Jones:** well, so they think, right? Yes, that's true. Everyone's just assuming it's a scam because the guy isn't replying to emails and he's not saying the right things and I don't know, something like that.

**Chris Gammell:** Yeah. So,

**Chris Gammell:** and, uh, so it had like a $2,000 goal, you know, he made a video at the beginning and, uh, $2,000 goal. He got 27,000 and then finally Kickstarter said, no, no, we're going to stop this right now. So I,

**Dave Jones:** I think he may have canceled it though. Didn't he cancel it? I'm not sure if, who was the one who actually did the canceling?

**Chris Gammell:** Oh, I thought it was, I thought it was Kickstarter that did that.

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** And, uh, and, and it was, you know, almost too good to be true. Like you, you, you pledge a $20 and they will ship you one of these, you know, automated wall outlet things. Um, that's including shipping it. Like, I don't know. I don't think you can manufacture such a system so cheap and afford to ship it to people for 20 bucks. It's just, right. And that's,

**Chris Gammell:** that's the real thing. I mean, like that's where people should have started smelling some, some nasty.

**Dave Jones:** And if you, and if you, and if you pledge 45 bucks, they'll ship you three of them.

**Chris Gammell:** Right.

**Dave Jones:** Um,

**Chris Gammell:** Oh, I thought the $500 one was really where, uh, that's where it really started to get.

**Speaker ?:** Yeah.

**Dave Jones:** When they come and personally install it or something.

**Chris Gammell:** Yeah. You get 25 wall outlets and switches and they come in personally, put it in and set it all up for you. And it's like,

**Dave Jones:** and, and they'll, and they'll cook you dinner as well.

**Chris Gammell:** And it's like, at that point, uh, you know, you don't have money even to get there mostly, you know, like. Yeah, exactly.

**Dave Jones:** Yeah. Consider it and be all over the U S you know, there's, there's no limit. Um, to, I remember, um, uh, MC, uh, Hunter lot, who's a nerd core artist. He, he did a Kickstarter project and he would, you know, but it was like five grand. So for five grand, he would personally fly to your house and actually do a performance in your lounge room, you know, but it was five grand. So, you know, you, you know, something like that's genuine. All right.

**Chris Gammell:** Yep.

**Dave Jones:** Um, but, and it's MC front a lot. Um, he's famous.

**Chris Gammell:** So you would have paid that if you would have come to Australia probably, right? Yeah. If you flew to Australia, yeah,

**Dave Jones:** five grand, turn up to my next birthday party and do a gig. Yeah. Awesome. But yeah, I, it's just, nah, you know, it just smells funny. This one.

**Chris Gammell:** Yeah. Yeah. So it's too bad. I mean, it's cause we've talked to a Kickstarter on here and there's been a lot of great, I think they're, they're really starting to crack down on stuff and, and it's tough with like hardware projects too, because if you have people that have a concept and it's like, they have good intentions and a good idea, but not like the manufacturing side of things. I mean, it's, it's tough to try and say that up front. I mean, like, so.

**Dave Jones:** Well, I called out one quite a, many, many, many episodes ago. Now it was, um, uh, a pair of sunglasses that had a built in, you know, uh, built in high def recorder or something like that. And you can actually buy those now, but not from the Kickstarter project. I don't think, and they had all these great 3d concepts and I looked at it and I instantly went, well, I don't think you can build it into that. You know, I don't think you can actually make it that small and make it look that good as the 3d, all the 3d models claim, you know, look, we'll ship you one of these funky looking pair of glasses with a hidden HD spy camera.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** You know, and I'm just, and you can actually buy it. Yeah. You can buy one commercially and it looks, you know, and once again, it's much bigger, you know, it's got the huge thing for the battery on the side, not huge, but certainly a lot, lot bigger than what this company were claiming. And they were, you know, saying they'd be able to sell it for, I don't know, some low cost, you know?

**Chris Gammell:** And yeah,

**Dave Jones:** nah, I, I called, I haven't followed that one up. Maybe I should,

**Chris Gammell:** um,

**Dave Jones:** maybe they've proved me wrong, but yeah, you've got to be careful because as you said, a lot of people have good intentions for stuff like this, but it, but it falls over. They just, you know, they don't know how much effort and, uh, money and time and, and, and resources are involved in actually getting a real kick-ass looking product to market. So,

**Chris Gammell:** yeah.

**Dave Jones:** I know.

**Chris Gammell:** You know, you should, you should contact eScape. I just saw that they're actually from, he's from Melbourne.

**Chris Gammell:** Oh, right. Okay.

**Chris Gammell:** There's a hackerspace up there, hackmelbourne.org.

**Chris Gammell:** Oh, okay.

**Chris Gammell:** And, and of course, then we just, you know, completed a square, I'm sure for, uh, the, uh, bingo. So,

**Dave Jones:** so is this the, uh, tech start guy? Is this the power? Is this the power project? He's from Melbourne. Is he?

**Chris Gammell:** No, he's the one that called it out. The one that the site. Oh, right. Okay. Yeah. Cool. Yeah. And you're going up to Melbourne, right? I'm going to Melbourne.

**Dave Jones:** I'm going to Melbourne in a couple of weeks. Um, what was that for you? Um, that's for the, uh, show, the electronics show.

**Chris Gammell:** Oh, the E, E X at the end. Electron X. Yeah. Electron X. Yeah.

**Dave Jones:** X show. It was in Sydney last year. They alternate between Sydney and Melbourne usually. Yeah. Um, so it's in Melbourne this year. So I'll be going as well as, um, hopefully, um, blogging a whole bunch of other stuff. Um, maybe, but I'm after ideas. So if you know of something in Melbourne that I should, uh, go and see and, uh, blog, then please, uh, please tell me.

**Chris Gammell:** I think the Melbourne hackerspace, you should go there.

**Dave Jones:** And Melbourne hackerspace. Yes. First suggestion. I think.

**Chris Gammell:** Yep. All right. Absolutely. Yeah. Well, I think we're getting down to the end of the show. So we should probably go to the.

**Chris Gammell:** What?

**Chris Gammell:** Yeah. Well, we got. That's flowing.

**Dave Jones:** That's ridiculous.

**Chris Gammell:** Oh, sorry, man. What have we talked about? Nothing. Who cares? Who cares?

**Chris Gammell:** Ah,

**Chris Gammell:** anyway. So how about some, some, uh, day in nerd history? Please. Okay. So, uh, on this day, the 29th, because it's the 29th, actually, it's not the 30th as, uh, as certain people have pointed out. Uh, bloody 30th. America's not the center of the world. Charles F. Kettering was born. He's the, uh, bloody yanks. He had a bunch of patents basically for a national cash register and, and, uh, and Cadillac and General Motors and everything. And basically he, he did set up a bunch of the research at General Motors back when, you know, General Motors was a good thing. Uh, and they, they cranked out a lot of, a lot of technology basically. You know, they, uh, yeah. So, and, and actually Kettering is the one they, they named, uh, uh, General Motors Institute was renamed Kettering University, uh, a couple of years ago. Right. In honor of him. So, yeah. Very cool. Yeah, definitely. He, you know, he did a lot of cool stuff too. He, uh, electronic starter and,

**Speaker ?:** uh,

**Dave Jones:** diesel locomotives.

**Chris Gammell:** Yeah.

**Dave Jones:** Wow.

**Chris Gammell:** Stuff for the grid, you know, like lots of really good stuff that, you know, a lot of, uh, the basis for other technologies.

**Dave Jones:** And he was on the front cover of Time Magazine in 1933. So he must've been important.

**Chris Gammell:** Ah, come on. I was on the cover of Time Magazine a couple of years back. Were you? Yeah. So were you. Was I? That's stupid. The person of the year is you, you know, like remember they did that?

**Dave Jones:** was it? Oh, no, I don't remember that. You didn't see that one? Oh, what a way. I know.

**Chris Gammell:** Yeah, it was really stupid. Okay. I have to check that out. Apparently some people put that on their resume too. Can you believe that shit?

**Dave Jones:** Oh, really? Oh, give me a, right, instant, you know, I'm going to boot your ass out the door right there.

**Chris Gammell:** Right in the trash. Yep. Yeah. Yeah.

**Dave Jones:** That's pathetic. Really?

**Chris Gammell:** Yeah.

**Dave Jones:** Oh boy.

**Speaker ?:** Yeah.

**Dave Jones:** I remember back in the eighties when the personal, when they didn't have the, they had the first object on there as the Time Magazine person of the year was, was the personal computer. Oh. Back in 83 or something. I don't know, something like that.

**Chris Gammell:** Uh huh.

**Dave Jones:** And of course, you know, big uproar. Oh, you've ruined Time Magazine because you didn't put a person on there. You put a stupid computer, you know?

**Chris Gammell:** Mm hmm. No.

**Dave Jones:** Yeah. All that sort of thing.

**Chris Gammell:** Mm hmm.

**Dave Jones:** Ah, well.

**Chris Gammell:** Yep. Yep. Well, any, uh, any final words for the, we've got probably one more, one more thing in us here.

**Dave Jones:** I've used up my quota of that word. Oh, the P,

**Chris Gammell:** not that word. That's not the word I was talking about, Dave.

**Dave Jones:** I can't throw in another one. No,

**Chris Gammell:** no,

**Dave Jones:** no, no. All right.

**Chris Gammell:** Yeah.

**Dave Jones:** Are personal robots ready to go mainstream? You've got on the list.

**Chris Gammell:** I do. Yeah.

**Dave Jones:** At 285k. Yeah, I don't think so.

**Chris Gammell:** And so that's actually the, uh, the Willow Garage. I mean, we've talked about Willow Garage, I think, before. They've had a couple. I think so. Yeah. Personal Robot 2, PR2. And they've been popping up everywhere. You know, it's, the thing is, it doesn't look like that advanced of a robot, but when you actually hear them talking about it, it actually is, it's really advanced because you think about all the, you need to have like localized sensors because if you have something gripping, like say they show getting a beer, right? If you have a robot arm extending and grabbing a beer, you don't want to send the data all the way back to the central unit. You want to have a local unit that just sends back, okay, now I've grabbed it. You know, they want to have localized control on all these servos and everything. So it's actually really complicated.

**Dave Jones:** Oh yeah, I can imagine.

**Chris Gammell:** Yeah.

**Dave Jones:** And they talk about a robot kit at the moment.

**Chris Gammell:** Oh yeah. Which one?

**Dave Jones:** It's the, micro brick. It's the micro brick.com. It's a little hobby, a toy, you know, little toy robot kit. Yeah. It's got little wheels in it. It's got a pick in it. It's really cool. I haven't built it yet, but it looks like fun.

**Chris Gammell:** Yeah. That does sound like fun.

**Dave Jones:** Great for the kids, you know,

**Chris Gammell:** nice little robot kit. You know,

**Dave Jones:** it follows your round or it follows the infrared remote. You know, you got a little infrared remote control and you can make it, you know.

**Chris Gammell:** Oh, make it dance and stuff.

**Dave Jones:** Make it dance and do whatever. I don't know. Torture cats.

**Chris Gammell:** Right. But it looks fun. It looks like fun.

**Chris Gammell:** If you got one of those things that had an LED on, or the infrared LED on one side and then a laser pointer on the other, you know, you could really mess with some cats there.

**Chris Gammell:** Cool.

**Chris Gammell:** Yeah. So it's, I mean, they're talking about it coming down in prices and stuff. It's still probably, they said, it used to be $400,000. Now it's $285,000.

**Dave Jones:** We're supposed to have our own personal robot by the end of the eighties.

**Chris Gammell:** Were you really?

**Dave Jones:** I didn't know. Yeah. What is that? Come on. Or nineties or something. Somebody predicted, you know, everyone predicted because you could buy these little robots, which went around in the eighties, you know, and that, that would actually hold your coffee, you know, they'll hold a can of beer and you can, you know, command them around. Yeah.

**Chris Gammell:** It wasn't a, it wasn't RoboCop held in 2004 too. I thought I saw someone.

**Dave Jones:** Oh, was that when it was set? Was it? I thought so. Was that the time period? Oh, okay. I thought so.

**Chris Gammell:** I thought I saw someone talking about that.

**Dave Jones:** Okay. Yep. Where's our RoboCop? I think that was supposed to, there was, I read a news report that there was a random news report alert that non-electronic related. Sorry. Hey, is that a bingo? Yeah, it's a bingo. Yeah, there you go. Excellent. Um, that is some, uh, where they filmed it, where they filmed RoboCop there, the council's, uh, trying to put in a statue of RoboCop in the town. Yeah. That's in Detroit. Yeah. It's in Detroit. Oh, it's in, it's in Detroit. Okay.

**Chris Gammell:** And I think they passed it too.

**Dave Jones:** Oh, did they? Okay. So there's a cool statue of, uh, RoboCop, just like there's a Rocky statue, you know? Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Other things. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. So Detroit's known for RoboCop now. It's not known for the automobile anymore, huh? Cause that all went to shit. Yeah. So, yeah. But we've talked about that here on before, before. Yeah. They're coming good again, Detroit. Yeah. Yeah, definitely. A lot of the,

**Chris Gammell:** a lot of the hacker spaces and an industry coming back there. It's, it's a good sign. I mean, they're still small, but you know, my Midwest brethren over there, you know? Right. Okay. I'm still in the middle. I'm still in the middle.

**Dave Jones:** Right. There's a camaraderie is there between the, uh, people in the middle. Is that the,

**Chris Gammell:** yeah.

**Dave Jones:** Right. I mean, what we got to say is the people down, down South, like, uh, Randy from Hicks. Oh yeah. Randy.

**Chris Gammell:** Right. Right. I don't know. It's like, yeah, people like the Midwest is a, it's a, it's an interesting place. You know, it's, it's not like the easiest place to live. The weather sucks and the, uh, you know, there's a lot of overweight people here, but that's a lot of the U S and, you know, an industry is gone. I mean, there's a lot of industry that isn't here because it was based on manufacturing. So, uh, you know, it's definitely taken its lumps, but, uh, I don't know.

**Dave Jones:** Do you have an item on here about, uh, they should have like, got local green cards for each, um, each state or something to try and keep people in the state working in the state.

**Chris Gammell:** Oh yeah. That was, that was actually more about like people that are coming to the U S from outside to, to go to school. And, and yeah, I mean, that's, that's like an H one B thing. And, you know, people always feel real strongly about H one B visas and, and understandably. So like H one Bs are actually, that's actually the visa given for people that are coming in to just work from out of the country. Right. So if I'm, if I'm, you know, Chris corporation and I can hire an engineer in the U S for 50,000, I might be able to hire, uh, uh, H one B, you know, person for, you know, 30,000 or, or even 50,000. But the, there's lots of restrictions and, you know, it's, it's not a great system really, but a green card is a little bit different. Basically the, the point there being, why don't we just staple a green card to diplomas? That's kind of the idea. And that's been said a lot of places. I definitely didn't come up with that, but I agree with that. I think if you're good, if you're going to be the U S or if you're going to go to Australia to study, you know, like you want to encourage those people to stay there. That's, that's the main thing that I like about it is that if you've got these smart people coming to your, your country to study, you want those smart people to stay there. And yeah, especially the U S, which is known for, you know, like a lot of different cultures, I think, man, we same here, same here, even,

**Dave Jones:** even more so, I'm sure.

**Chris Gammell:** Yeah. It's known more so for.

**Dave Jones:** Australia is very known as a very multicultural country. It was multicultural, but so was the U S, you know, I just watched an interesting doco about the U S and how New York was founded on all the immigrants and all that sort of,

**Chris Gammell:** you know,

**Dave Jones:** thing. So, yeah, but it's a very same thing here in Australia. And, and yeah, like there's lots of, um, back in, Oh God, we've mentioned this on here before, I'm sure, but back in the thirties or forties or something, when we were having all these immigrants coming in, we would actually tell them where they had to go and live. Oh, that's right. You've got to go to this city, this town, but now, you know, it's a free for all where we invite more people into this country to come and stay here than anyone else. I think we're right up there and they all want to come and live in Sydney or Melbourne. No wonder our bloody cities are overpopulated. You know, and housing's the highest in the world because the actual housing prices, because everyone wants to live in the same spot. Everyone wants their McMansion in there, you know, on their 800 square meter block of land in Sydney, you know, God, no wonder every house here is a million bucks plus. It's crazy. So yeah, I think, yeah, it should be the same thing, you know, and you should, yeah, you should be able to, if people come into your country, you should be able to say, well, okay, you go to this state or you go to this city or something. Oh, well, that's not what I was saying. Well, I'm saying that. I know you're saying that. I'm going further.

**Chris Gammell:** Oh yeah, you are. Yeah, this is, I mean, this was talking, I mean, this article came from.

**Dave Jones:** Wouldn't you get the same problem there? you would have, everyone wants to go to Harvard or everyone wants to go to, you know, some, some uni to study or something. Yeah, but that's, that's a good thing. Other people.

**Chris Gammell:** That's a good thing.

**Dave Jones:** Doesn't that push out locals and raise the prices up and study and all that sort of, well, isn't that bad?

**Chris Gammell:** I think that, I think that, uh, that's a good thing that would raise standards in the U S then. I think personally, I mean, if you have, you know, Harvard is already like a super prices, raises prices, maybe, but education was on the backside.

**Dave Jones:** It's star ranking, right? Yeah. But, okay.

**Chris Gammell:** That's not the concern here. The thing is that if you have people that are coming in and doing all this stuff anyways, right? They're going to Harvard, they're going to MIT, right? They're these brilliant kids from out of the, out of the country. And then previously in previous years, you know, when it was a little easier to get a visa or a little easier to get a green card, then they would stick around and start companies, right? That, that's, that's the basis of it. And now they're going back to China because there's tons of industry over there or India because there's tons of industry over there. And they're, that's where they're starting the companies. And it's like, well, why not start it here? That's, that's the main, that's the main thrust of the idea. And, and that's something I totally agree with. I think, you know, if you have people that are going to come into this, come into your country and create jobs and it's like high level, awesome jobs, like technical jobs, that's, that's what I want. And that might be getting a little too political for people there, but, you know, I think, I think it's a good, I think it's a good idea. I mean, at the base of it, however, it's, I mean, let's be honest, nothing's going to happen in the U S or anywhere else for that stuff, but yeah,

**Dave Jones:** yeah,

**Chris Gammell:** I, I like the idea,

**Dave Jones:** but it's good to dream, huh?

**Chris Gammell:** Yeah, definitely. Definitely.

**Dave Jones:** And on that note, our amp hours up.

**Chris Gammell:** It is. We'll be back dreaming next week, next week though. And we'll probably have a, a special guest next week. Two of them. Yeah.

**Chris Gammell:** Two. Oh, it's going to be crowded. It will be crowded.

**Speaker ?:** Woo.

**Chris Gammell:** All right. Well, all right. See you then. See you guys. So Dave, did you hear the news about Steve jobs stepping down from Apple?

**Chris Gammell:** Uh, no. Who's Steve jobs? Never heard of him. Apple.

**Chris Gammell:** All right.

**Chris Gammell:** You don't got those in the fridge.

**Chris Gammell:** Guess we'll just ignore it.

**Chris Gammell:** What the hell are you talking about? Are you just mumbling U S garbage again? What are you doing? Yeah, no big deal. All right.
