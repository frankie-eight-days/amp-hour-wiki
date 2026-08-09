---
episode: 147
title: An interview with Jeri Ellsworth - Absorptive Augmented Actuality
url: https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/
---

**Chris Gammell:** This episode of the Amp Hour is sponsored by Element 14, the global online engineering community that is making it easier to find data sheets, support forums, projects, and a place to purchase dev kits all in the same place. You'll find everything you need to know about BeagleBone Black, Raspberry Pi, Arduino, and more. For a limited time, you can enter to win free products in the Raspberry Pi camera competition running through June 14th. Or you can sign up at any time to try out new products and dev kits for free through the road test program. Learn more by visiting element14.com. This is the Amp Hour Podcast, recorded May 27th, 2013. Episode 147, with guest Jerry Ellsworth. Absorptive, augmented, actuality.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life. Psst, your line is, I'm Jerry Ellsworth.

**Jerry Ellsworth:** And I'm Jerry Ellsworth, and I missed my cue.

**Chris Gammell:** Hey, Jerry. She's back.

**Jerry Ellsworth:** It's been a long time. How long has it been? Two years? It's something like that. Someone on Twitter was saying it's been 100 episodes, so it's not a surprise that I missed my cue to go. You're fired, Jerry.

**Chris Gammell:** You're fired.

**Dave Jones:** Well, thank you very much for joining us, because we know that you're super-duper busy.

**Jerry Ellsworth:** Oh, yes. Things are just going nuts over here right now.

**Dave Jones:** How many hours sleep a day are you getting?

**Jerry Ellsworth:** Well, we just did a big public reveal at Maker Faire, and leading up to that, we were getting like five and six hours a night. It was like 16 and 18-hour days. It was ridiculous. But now that I've come back from Maker Faire, I slept like eight, nine hours a day for the last three days, and took all weekend off. Oh, wow. It felt weird. That's awesome. Luxury. It felt weird. Yeah. We've been going like this for three, three and a half months.

**Chris Gammell:** That really starts to wear on you. That can really make you go crazy at a certain point.

**Jerry Ellsworth:** Yeah, there were times that my partner here, Rick, and I were a little snippy with each other. Yeah.

**Dave Jones:** Yeah, but you're still young and carefree. You can handle it. That's right. Yeah. Come on, suck it up. I keep telling myself that.

**Speaker ?:** That's it.

**Chris Gammell:** So for the three or four people in the world who didn't see the article or didn't hear us talking about it last week, or was it last? Yeah, I guess it was last week. Could you tell us just about the project you've been working on so that we could have a baseline of what you've been doing? Absolutely.

**Jerry Ellsworth:** So I started working with Valve Software about a year and a half ago. And when I got there, I was given the mandate to research everything video game related in the hardware space. So we started looking at input devices, output devices, virtual reality, augmented reality. And a few months into working there, I got really excited about augmented reality and started looking at every type of AR glasses that were out there. Sorry, why is that? Why did AR excite you? At first, it didn't. I thought it was kind of a limited medium to work with. But as we started researching a bit more, I got excited about, hey, you know, there is a lot of things that you can do in this space. And it looks like there might be some possibility for lightweight glasses that someday will be on the market. Right. Yeah. So I really started researching that a lot. And then partway through last year, I kind of stumbled onto this technique that to do AR glasses in a very low cost way, which instead of trying to put the light directly into your eyes, which is the most common approach, we project from the glasses using little micro projectors to a special surface that is highly directional. It's called retro reflective, much like they use for road sites.

**Dave Jones:** On the moon, you know, the Apollo 11 put a retro reflector on the moon and regardless of what angle you fire a laser at, it comes back directly to you. Right into your eyeball, actually. Yeah. It's great.

**Jerry Ellsworth:** Exactly. So we're using this retro reflective material that they use on road signs, like regular freeway signs. They look really bright at a distance. It's because they have this retro reflective property to them. So by using that in conjunction with these little tiny projectors on glasses, we can project out to the surface and 90% of the light that leaves the glasses comes back. So you don't have to project very many photons out to the surface to get a very bright, vivid image coming back. Right. Yeah. Upside is the glasses can be extremely small and lightweight. Downside is you just have to roll out the surface before you start playing your video games. And so that's what I worked on at Valve. That was my primary project. There's a lot of challenges around that. So we started, several of us started working on the head tracker. You have to track the user's head positions. That was a critical piece of it. We developed a head tracker. This actually, most of this happened outside of Valve after getting laid off. We developed a head tracker that uses cell phone image sensors that are super low cost, or like these $1, $2 image sensors. And then we did some tricks in the optical path so that we could detect LEDs with a super high precision. So at three meters distance, we can do sub-millimeter accuracy. Oh, nice. Yeah. It actually, a funny story around developing that. So I put this whole camera system together. I was like, wow, this seems pretty accurate. I gave it to Rick, my business partner. And he started doing the software side of it. And he's like, Jerry, you know, I keep seeing noise. I think there's something wrong with your circuit. And so I get up and I start walking over there. And he's like, wait a minute, step up, jump up and down. And so I jump up and down. It was just me tapping my feet and rolling my chair around.

**Chris Gammell:** It was so accurate that the ground moving, the table actually did it. Is that the idea?

**Jerry Ellsworth:** Yeah. Yeah. It was just like vibrations through the floor. Wow. So to have to, actually, maybe I should take a step back before getting into all the tech. Maybe I should explain what you see when you look through the glasses. Yeah, that's a good idea. And why it's important to have this super high accuracy head position tracker. So you roll out the surface. It's just kind of a matte gray surface. And we can project 3D objects onto the surface, below the surface, at the surface, or above the surface.

**Chris Gammell:** Below the surface? Huh. That's interesting.

**Jerry Ellsworth:** Yeah. So it looks like it's, say you roll out a matte on the, just imagine like a flat surface. You can project as much as you want into the surface. So you could like make it look like on your table, there's this huge void that opens up and extends for infinity. You can have stuff drop down in there. Like one of our experiences that we show is a block type game, like a Jenga type game where blocks are stacked above the surface. But not Jenga, of course, right?

**Chris Gammell:** That's what you guys said in the video I saw.

**Jerry Ellsworth:** Yeah. Yeah. It's called, it's actually, Rick called it Jenga. Jenga, right. Because I guess I suggested Jenga and he knew we'd get sued into the ground if we used Jenga.

**Chris Gammell:** You've got to start in a good spot.

**Jerry Ellsworth:** So the blocks are rendered above the surface. It looks like they're sitting above the surface. And then we have a wand. So with the same type of tracking technique, we can track the end of a wand. And you can take this wand and you can just bash into the blocks and they go flying all over the place. But the Jenga blocks are on a platform that are rendered at the surface height. And then off the edge of the surface, the blocks will fall. And it looks like they're falling, you know, forever down into this huge pit.

**Chris Gammell:** Wow, that's really cool.

**Jerry Ellsworth:** It's a very magical experience. It's cool because you can bash the blocks and sometimes they'll hit this rendered surface and they'll bounce and they'll fly right up towards your face. And your natural instinct is to just kind of dodge them. And then tons of the blocks fall over the edge and you can just kind of lean over the top of the table and you can just watch them fall forever. And they're interacting and bouncing off each other. That's awesome.

**Chris Gammell:** I heard someone else explaining the potential of using this system as like kind of like in the Star Wars, in the first Star Wars where they're playing like that chess type of game or like in Harry Potter where they're doing like the 3D chess. That's also like another type of application you could do for this kind of device.

**Jerry Ellsworth:** Yeah, yeah, we've, well, when I say we, Rick has actually done all the game experience programming on it. They're all very simple. So he has a chess game which he calls Team 4 Chess, which is based off of the game that Valve has called Team Fortress. And so it's very much the battle chess type game. Okay. So you have your chess board and the characters are rendered above the surface. You can put your wand in there and you can direct them where to go. And they move into their different squares and they fight and they punch and stuff. And then when one of them dies, they go flying up in the air and they'll kind of ragdoll and fall down on the table. And if they fall off the edge of the table, they kind of tumble forever, much like the Jenga.

**Chris Gammell:** Yeah. Wow.

**Dave Jones:** So how is this different to virtual reality? How is augmented reality different to virtual?

**Jerry Ellsworth:** So virtual reality, you're cut off from the rest of the world. So that's one of the things that we were researching. It's like, you know, is virtual reality what people want to play? Is augmented reality? Virtual reality, you're kind of blinded from the world. You've got these micro displays or the displays that are really close to your face and you have lenses that will let you focus on them. And you don't see anything around you. So everything is 100% synthetic. Now, augmented reality gives us the option where we can have synthetic or we can do other mixed kind of media things where we put, for instance, we're working on a figurine tracker that allows us to do Dungeons and Dragons or Warhammer type games. So on this map that you lay out, you could put figurines that are tracked with the same LED tracker. And we know within sub-millimeter accuracy where they are on the surface. And for instance, you might put a character down. You'll see all of that character's stats. Or when it's your turn to move your character, there might be a circle that is drawn around the character that shows you how far you can move them. And when it's, you know, if you come within range of another character, they might fight or something like that.

**Dave Jones:** But you are limited to the mat. Yes. Right. Is there any other, have you seen any other potential to do it without the mat? Or is that the enabling technology for the entire AR?

**Jerry Ellsworth:** Probably in the next decade, we're going to see something that you'll be able to just wear and you won't need the mat. But currently, all those techniques are very uncomfortable. And usually, there's a lot of issues. I learned a ton researching this. For instance, the type of AR glasses that put the light directly into your eyes, like Google Glass, you have to set a focal depth on those. Which the manufacturer usually sets those at infinity because that's easiest for people to gaze out to infinity and see the image. But you have a problem if you want to render something on your table and make it look like it's at the table height. Right. Because it's at infinity, but yet you're trying to force it to be at the table. So, you get these conflicting cues that give people headaches and make them dizzy. Nauseous. That's a big problem with a lot of the VR stuff is people are cut off from the world. So, their inner ear doesn't match what they're being presented. So, people get dizzy a lot. Don't get me wrong. The VR experiences that we were looking at at Valve were awesome. And they're continuing on with that stuff. Like, there's Team Fortress on VR and you really, it's very immersive. Yeah.

**Chris Gammell:** Well, that's like Oculus Rift. Is that the newest one? Is that considered VR?

**Jerry Ellsworth:** That's VR. That is VR. Okay. So, you see nothing around you. You're kind of putting these ski goggle things on that blind you.

**Chris Gammell:** But then you can move. Yeah.

**Jerry Ellsworth:** So, our glasses are completely transparent and you can see off to the side. You have peripheral vision. And then...

**Chris Gammell:** Oh, okay. Got it. It's like magical glasses.

**Dave Jones:** So, is this the big decision that Valve made? They went, well, which one? We don't want to pursue both, VR and AR. So, we only want to pursue one. Is that how it went down?

**Jerry Ellsworth:** There was a branch at one point. We were all working for mostly AR. And then it's a tough problem. It really is. And so, there was kind of a branch in the teams where a lot of people went on to VR because they thought it would be an easier thing to do.

**Chris Gammell:** Well, and Valve is known for the... You guys could, you know, move around like that as well, right? Where you... That's like the culture where you could pick and choose the teams and everything like that, right? Yeah.

**Jerry Ellsworth:** So, some of us branched off and we did the AR stuff and some branched and did the VR stuff. And that's kind of how it sat.

**Dave Jones:** Were there food fights in the cafeteria?

**Chris Gammell:** Virtual food fights.

**Jerry Ellsworth:** You know, our team there really got along well. It's... We had super talented folks that we recruited in there. So, Ben Krasnow... We know, Jerry. I know, there have all been guests on the Amp Hour. Yeah. It was really disappointing to be let go and not to be around all those minds because, boy, it was super smart people.

**Chris Gammell:** Yeah. Yeah, that's... I mean, we were shocked when we heard about it, you know? Like, it's tough to hear about. So, it's... I'm glad to see this all working.

**Dave Jones:** So, tell us the story there. Was it actually a... Like, it came as a big shock to everyone there? Have they laid off people before? Is that a first?

**Jerry Ellsworth:** They've laid people off before. It was very shocking to us and our team because almost everyone that touched the AR project got let go. And it was pretty atypical of them. Yeah. The handbook says that you'll be course corrected and you'll be warned if they think you're too far off in the weeds. It's... Course corrected?

**Dave Jones:** Is that the latest management wank word? Yeah. Course corrected. I love it.

**Jerry Ellsworth:** So, yeah, there was no course correction for me. It was just kind of we showed up and they're like, this is your last day and so...

**Chris Gammell:** We're course correcting you to the door?

**Dave Jones:** Exactly. So, they actually masked you straight out. They didn't say, oh, you've got a couple of weeks left to finish up your paperwork or whatever?

**Jerry Ellsworth:** Oh, no. It was a complete surprise to our group and to the other folks in the hardware group. So, whatever. I mean, they made their decision. I had a great time there. It was a good place. It had its frustrations, but...

**Chris Gammell:** It's work, right?

**Dave Jones:** It's work, right? Yeah, exactly, right.

**Jerry Ellsworth:** But, you know, the great thing, they did the right thing because I went to Gabe. He was actually the one that let me go, which was kind of fun. So, I was a little bit upset and I said, you should fund this outside the company or you should just let us have it. And he just turned to the lawyer in the room and said, let him have it. And so, that's what happens. Oh, really?

**Dave Jones:** That's how it went?

**Jerry Ellsworth:** Yeah, that's pretty much how it went.

**Dave Jones:** Because this is the most amazing part of this whole saga to us is that the fact that a company let you take the technology you've been working on there. Usually, they will just say no at all costs, even if it means the technology dies and nobody in the world gets it. I know. If we can't have it, nobody gets it. That's the usual, you know, attitude. So, this is absolutely stunning.

**Jerry Ellsworth:** It is. I don't know why they did it, but I'm glad they did because after revealing it to Maker Faire, we had four experiences that people could try there. And the response was, you know, across the board, like super positive. So, I think people are going to really like this. Yeah.

**Chris Gammell:** Well, it's interesting, too, from a product development standpoint, too, because, I mean, there's no saying that, you know, Valve eventually couldn't get back into this kind of technology, you know, working with you guys. Or, you know, kind of just like it takes an internal startup. And, yes, you are outside the company, but it's not like, you know, there's no closing the doors forever, right? I mean, it's just interesting from that standpoint.

**Jerry Ellsworth:** Yeah, it is interesting. Yeah, I'm baffled and disappointed, but I'm very excited that we have it, though. So, and it looks like, you know, in some ways we might be better off, you know, because with Kickstarter and all these other avenues we can go down to get it out to market. Yeah. It might have been more difficult inside Valve to get traction because Valve does their type of games, which are first-person shooters. And we're talking about a type of game which is like board games and figurines and magic wands interacting with virtual characters, completely different. So, I could see how, like, it might have been confusing to folks in there, what in the world we were doing off in the corner. Sure.

**Dave Jones:** But it's ultimately, I think, very smart on their part because they know that, you know, you guys are close to them. And if the technology takes off, they can likely come back into the space and start working with you guys.

**Jerry Ellsworth:** Oh, absolutely. We're still, we still communicate with all the folks over there. Like, there's no hard feelings with the hardware group over there. We put together an awesome team and we were all, like, super hardworking friends. I mean, it was very common for us to, like, we'd come in at 11 o'clock in the morning, you know, normal engineering hours. And we'd recruit during the day. You know, we'd try to get more people on the team and doing all this, like, day-to-day kind of stuff. And then we'd work until 1, 2, 3 in the morning sometimes on each other's projects. It was, it's really a...

**Chris Gammell:** Just a party, huh?

**Jerry Ellsworth:** Let me guess, everyone there is single, right? Nobody's married with kids. No, no, some people had family. But, yeah, you know, everyone got to choose their hours that they worked and, like, folks with family, yeah, were out of there earlier. But, yeah, it was very often that we would work because we were so passionate about our various projects. So, yeah, we're all friends and we still communicate and collaborate. And, yeah, maybe someday they're going to see the value in it and come back to us. Yes.

**Chris Gammell:** Yes. Ha-ha, I told you so. Well, it's tough, too. I mean, because, I mean, also, you guys are showing this off at a much earlier standpoint than most engineering companies would, right? I mean, that's another thing that's very different that maybe a bigger company wouldn't let you do.

**Jerry Ellsworth:** Yeah, absolutely. We'd always talked about releasing stuff very early at Valve, but probably not this early. No. The only reason we showed it was... Hot milk glue and... Oh, God. Lots of hot milk glue. The only reason we showed it this early was because of Maker Faire. And it's like we didn't want to miss this chance to get it out to the people who would really appreciate, like, every bit of hot glue and blue wire on it.

**Dave Jones:** And there's a whole bunch of media there as well. That helps.

**Jerry Ellsworth:** Yeah, the press, we were very nervous going into it because it is, you know, we hadn't done any ergonomics on it. The hot milk glue and JTAG connectors hanging out the side of the glasses. We suspected we would get, like, you know, flayed by them, but actually there was... Hammered for... Yeah, right. The media really appreciated that we were there so early and the wow factor of it, just because it worked so well, you know, it paid off big.

**Dave Jones:** Yeah, that could have gone either way. Like, they could have, if they chose to, they could have really hammered this, oh, what a piece of, you know, slapped together garbage, you know.

**Chris Gammell:** Well, they probably would have if it didn't work, right? I mean, that's the difference is that it works.

**Dave Jones:** Oh, well, if it didn't work, yeah, exactly. If it works, well, you know. Yeah.

**Jerry Ellsworth:** I was super honored. People were waiting upwards of an hour just to get in to take a look at it. Wow. Wow. The word got out that this was a thing that they had to see around Maker Faire and it was a constant line, like an hour long. So, some of our staff went out there and walked up and down the line and talked to them and tried to keep them entertained and like... Staff?

**Dave Jones:** Well, there are... Staff? I thought it was just you and Rick. No, so there's... Or did you hire some people?

**Jerry Ellsworth:** So, there's three of us from Valve that were all at go at the same time and we're all working together on it. And then there's some... We have an artist that came on board, Tara, who was at Lucas Arts that just had a layoff, unfortunately.

**Chris Gammell:** Oh, yeah, they just did. Yep.

**Jerry Ellsworth:** Right. And a lot of our friends, like, believe in it and they help us part-time. So, there are a few folks that just came out to help us with all the craziness. And thank goodness because it was beyond what I expected.

**Chris Gammell:** Well, yeah, because you guys got to do interviews and stuff, too. And, you know, you want to walk around the fair still, right? And then, of course, you've got your usual throng of people probably waiting to talk to you anyways. So, you just have a Jerry Ellsworth booth, usually, let alone having, you know, a bunch of VR or AR glasses, right? Mm-hmm. Yeah.

**Dave Jones:** So, is the... So, now you've got a startup. Technical Illusions is a very cool name, by the way.

**Jerry Ellsworth:** It only took us three days to come up with that name. And it took us three months to come up with the name CastAR for the gaming system. Which actually happened on the ride down to Maker Faire. Right. We've got to have a name, guys. Quick. We were beating our heads against the wall on the name. We thought Mirage. We thought even Campfire was suggested because it's a social gaming experience. Each person wears their glasses. Oh, right. So, hook to their cell phone and you'd be playing your Warhammer.

**Dave Jones:** Mm-hmm. I think CastAR is a good name. I think it fits. It's nice. It isn't too wanky.

**Jerry Ellsworth:** Yeah. We thought there was a lot of symbolism in it, I guess.

**Dave Jones:** Yep. So, now you're a startup. I assume you don't have any funding at this stage. You're sort of eating dog food and... Lots of ramen noodles. Funding it yourself at this... Right. Funding yourself at this stage. Is that the goal? Everyone just chips in and works for free?

**Jerry Ellsworth:** Yeah. It's all coming out of our... Works for free? Yeah. It's all out of our bank accounts. Like, these prototypes are pretty expensive to put together on a onesie-twosie basis. And so, all that money is coming out of our pockets. And it took us quite a while to get all the legal paperwork done with Valve. So, we couldn't even show it to investors up until a few weeks ago. It was... It was... Actually, we were very nervous that we wouldn't get everything finalized. We could get to even Maker Faire. But it all pulled together in the last minutes.

**Chris Gammell:** As it happens. Yeah. So, what are you hoping for?

**Dave Jones:** What are you... Are you hoping for venture capital funding? Or do you think that crowdfunding is the way to go? Or a mixture of both?

**Jerry Ellsworth:** I think it's going to be a mixture of both. I think probably first will be Kickstarter. I think our major goal over the next few months is to expand the game experiences so that people can look at the experiences and say... Instead of just saying that's a cool tech demo that we'll have some games that people will be like, I want to play that. And there'll be a good reason for them to buy, not just because it's cool tech.

**Dave Jones:** So, you think the game is more important than the hardware at this stage? Possibly. I mean, they're both important, clearly. You can't give people Hotmail prototyped... Exactly. Exactly. Exactly.

**Jerry Ellsworth:** I think the hardware is far enough along that we can prove that we can make it to the final product. Yeah. You know, with my background in toy design and mass manufacturing, that's kind of a given that we're going to be able to make it. But I think the burden on us now is to show that there really is compelling game experiences. And we also have an issue where we're talking about something that is so 3D and so immersive.

**Chris Gammell:** Yeah, how do you show it, right?

**Jerry Ellsworth:** Yeah, how do we express that in 2D? And that's been a problem.

**Chris Gammell:** How do you make the Kickstarter video? That's the important question here.

**Jerry Ellsworth:** Exactly. So, one of our goals is we're going to try to hit up every public event we can. We want to let as many people as possible see that it's for real. Yes. Because until you actually put the glasses on and you see a zombie run right up to you, you don't really get the idea.

**Dave Jones:** You don't understand until you try it. Well, I was going to say, after you launch the Kickstarter campaign, make it a long one and then go on a 50-state road trip. You know, have to drive around in a van and hop in the back and you can try out the experience.

**Chris Gammell:** And, you know, that's the way to drive around vans with no windows and then you offer candy. People just come right up to you. It's a classic advertising.

**Jerry Ellsworth:** I just got rid of my old pinball moving candy van. I know.

**Chris Gammell:** That would have like plumbing. Didn't it have like the plumbing scratched out on the side or something like that? I remember it being an old junker.

**Jerry Ellsworth:** You're looking like blue sky plumbing or something on the side.

**Chris Gammell:** Classic. That's too bad.

**Jerry Ellsworth:** So, yeah, that's our short-term goals. The next few months we're really going to push on the game aspect of it because the figurine tracker is almost done. So, that's what people are really anxious to see is like really the mixed real world and synthetic world demos, which we – in the lab we had some, but we just couldn't take them to Maker Faire because it was just – yeah, it was just too rough. At Maker Faire, maybe I should take a step back and talk about the experiences that we showed. We had the Jenga block, which I described, which people really reacted to very well because it was very relatable and the physics and everything felt good. We had a flying game where we had a cockpit kind of simulator where you just took a couple pieces of this reflector and you set it up in kind of a semicircular pattern on your table. And then you just steered with your head, so you just kind of moved your head where you wanted to go. It felt pretty magical because it just felt kind of like it was reading your mind where you wanted to fly to and your hands were free to do other stuff. We had a RFID example of where we can use cards. You can put cards down and then two characters would grow up out of the cards and go fight in the middle. We learned something interesting about in that experience where when the two characters fought, it was kind of comic book style. It would say kapow, boom.

**Chris Gammell:** Like old Batman?

**Jerry Ellsworth:** Yeah, but we made them zoom up towards the user's face. Oh, wow. We noticed on that game, out of all of them, people actually tried to reach into thin air and like touch things, these words that were flying, which was kind of interesting. Huh.

**Chris Gammell:** Okay.

**Jerry Ellsworth:** And then for our last example, we had a two-player game where you used just joysticks and you wore the glasses, but you were using the same surface and you each got a unique view. Because of the retroreflective properties of the surface, each person standing around the table doesn't see the other person's view. So you can have as many people as you want using the same surface and you can present them with whatever you want rendered. So it was a zombie game where you ran through a maze and you could peer over the top of walls by moving your head and you could chase each other through the maze also. And the whole maze kind of scrolled. So each person was in a different part of the maze and you'd only come across each other every once in a while.

**Chris Gammell:** Huh. So how does this look if you're a third person looking at two people playing, right? Does this look like two people kind of shining blocks of light down on the page? Is that all it looks like as an external user?

**Jerry Ellsworth:** Yeah, usually it looks kind of crazy depending on what they're doing. Like the Jenga game, for example, you just kind of see a matte gray surface and someone has a wand, which we created a tracked wand. So it's just a person waving the stick back and forth vigorously in front of a gray surface and laughing and like dodging their head back and forth.

**Chris Gammell:** Huh.

**Jerry Ellsworth:** But if you have another pair of glasses on, you can see, for instance, they'll be facing forward towards the blocks and you can walk around to the side and you can see the view of what it would look like from the side.

**Dave Jones:** So it is like a 3D effect. It is. It's very 3D. How does it compare to regular, like you go to the movies and see 3D? Is it the same as that, similar, but it's interactive?

**Jerry Ellsworth:** It's much different because if we go back to the head tracking, since we can track your head position, distance, rotation, and pitch within sub-millimeter accuracy, when you walk around the table, for instance, for the Jenga game, it looks like you're walking around the Jenga stack.

**Dave Jones:** Yeah. Right.

**Jerry Ellsworth:** It's much different than a 3D movie when 3D movies, to me, often feel awkward because I move laterally and there's no parallax.

**Dave Jones:** With this, you move. Yeah, I hate them. I just refuse to watch 3D movies. I think they're awful. Yeah. Personal opinion. Sorry.

**Jerry Ellsworth:** Well, it feels awkward, right? Because you don't have parallax and with this you have parallax. Yeah, that's right. So you move side to side and you actually get presented with the correct image where you get the wrong image, which is disturbing to many people. Yeah. That's some of the stuff we discovered is like when you present people with the wrong image. Mm-hmm.

**Dave Jones:** Like if... Their mind just spasms. Yeah. If you're going to move your... They'll burp.

**Jerry Ellsworth:** And it'd be very subtle too. Like if you move your head one inch, you want the graphics to actually move one inch. If you move it one and a half inches, people will pick up on that incorrectness and like they'll feel uncomfortable with it.

**Chris Gammell:** So would it be possible to do this kind of stuff in a movie? So if you had like the same kind of reference tracking point on like a screen somewhere and everyone's glass... Everyone had smart glasses on instead of the passive glasses like they do now. Would it be possible to create those parallax effects and everything, you think?

**Jerry Ellsworth:** Oh, absolutely. Okay. Yeah, there's actually some cameras out there that do full 360 degree views of the scene and record all those different angles. Yeah. So there's some people that have been with the virtual reality glasses doing some experiments where you rotate your head. Like if you're driving in a car... Yeah. ...you look off to the side and it looks like you're looking out the window.

**Chris Gammell:** Yeah, it's like the Google car, the Google Street View car kind of has that, right? Where it maps all 360 degree bubble around the car. Kind of that idea.

**Jerry Ellsworth:** Parallax is a trouble. If the information isn't there, it's hard to synthesize parallax information. But someday, you know, as things progress, they could probably interpolate that kind of thing.

**Chris Gammell:** Well, camera makers have to go somewhere, right? Once you're not a room with resolution, eventually you've got to throw new features in or else people won't buy your cameras anymore. Exactly. Which is the reason I think they make 3D movies is because they're just trying to charge more per ticket and... I don't know.

**Jerry Ellsworth:** I just saw that they're doing some like 4K television now. They just keep upping the resolution. They're probably desperate to find their next big thing. They are, yeah.

**Chris Gammell:** Well, hopefully they figure out. Well, they should acquire us. It's all it is. Yeah, that's the next move.

**Jerry Ellsworth:** We're open for acquiring, folks. Sony?

**Chris Gammell:** Get in early, folks.

**Dave Jones:** Is it seven or eight digits? It's...

**Chris Gammell:** Keep going, man. Keep going.

**Dave Jones:** Yeah, keep going.

**Chris Gammell:** Ted, why stop there?

**Jerry Ellsworth:** All right.

**Chris Gammell:** Yeah, well, we'll see. The technology is so fledgling. You could get in on the ground floor today, folks. That's right. Put in your bids now.

**Jerry Ellsworth:** Make your deal.

**Chris Gammell:** Sign up on our... We'll have a Google Docs spreadsheet. You can just... It'll be a Chinese auction. You just bid what you can. And then, you know, top bidder will be ignored vigorously for a better offer.

**Dave Jones:** Well, that's always the dilemma, though, isn't it, with this startup? Like, you know, you ultimately want to sell out and get rich, but then you don't want to give up your baby. Yeah. Right?

**Jerry Ellsworth:** I want to see this make it to market because I devoted so much time to it. I believed in it when I was at Valve and to the point of rocking the boat. And then I continued outside the company. And we really believe in it because it's something very special that people... It's experiences no one's ever seen before. Yeah. So, I'd be very disappointed if it never made it to market. So, I'm going to do everything I can to get it out there.

**Chris Gammell:** Plus, you know a lot of the capabilities, right? I mean, you know what you could do with it. So, you have a very unique view of that. Whereas, people are just kind of... As you learn about the technology, you can't necessarily know everything you can do at first. But, you know, you've been looking at it so long. Of course, I could do this and that and this and that, right?

**Jerry Ellsworth:** It surprises us every day. So, things that we thought would be fun weren't fun and things that complete...

**Dave Jones:** Right.

**Jerry Ellsworth:** You know, things that you wouldn't think would be fun are just the most hilarious fun things that you could ever do with a sim. So, it's a completely new space.

**Chris Gammell:** We got to have some examples here. Okay. Like mundane stuff or what?

**Jerry Ellsworth:** We thought that Super Mario Kart would be the funnest game on this, which is a game where... Yeah, of course it would. Yeah, it's like your little go-karts moving around. Yeah. So, well, let me back up and explain Rick's methodology with the software and how he's able to do these. And then I can talk about this. So, we knew nothing about this space. We knew we needed to develop quickly so that we could try a bunch of different things. So, he made a game prototyping system which uses the scripting language called Lua. So, he can put games together, simple games. They're not full-fledged, but simple games like the Jenga block game or this racing Super Mario Kart game in several hundred lines of code. I think his biggest... Wow. His biggest game is like a couple thousand lines of code, which is that zombie maze game, which has all kinds of features. Unbelievable. Yeah. So, it has all these primitives that you can use that allows you to access the head track information and do physics and stuff. So, you can work really quick. So, he used his game prototyping system. He put together this Super Mario Kart and we put people on it to try it. And they just sat there like they were sitting on their couch playing the game.

**Chris Gammell:** Passive.

**Jerry Ellsworth:** Yeah, file. Right? They might as well watch it on a plasma TV. Why use this?

**Dave Jones:** Yeah. Got it.

**Jerry Ellsworth:** Then other things like the flying game came out of a different... Where you just point your nose where you want to fly. Came out of an experiment like what if we had the maze game and you just bobbed your head like a couple millimeters down and that would indicate that you want your character to hide behind a wall to like crouch down. Yeah. Which worked out really good and was kind of cool. But then it was like three in the morning like, hey, why don't we add this to your voxel terrain simulator that you built that wasn't terribly fun to play with. Combined those two and then all of a sudden we came with this game where you felt like you were a bird soaring around and it just kind of... Yeah. Awesome. Yeah. It's all brand new and very surprising what's fun and what's not.

**Chris Gammell:** That's really cool.

**Jerry Ellsworth:** So what we hope to deliver is the glasses, a starter kit that will give you a wand, the glasses, and a surface for sub $200.

**Chris Gammell:** How did you come up with that price? I've heard you say that a couple times now. So is there like a price that you guys saw on the market that we're like it has to be less than $300 or $200 or whatever it is?

**Jerry Ellsworth:** If we had a big company to back us, we could probably do it much lower than that. But from day one when we started developing this retroflective tech, we were very sensitive to cost. So we always kept that in the front of our minds. Like we can't use $80 camera sensors. We've got to use the $2 ones. So we've got to find a way to make that work. We can't use laser projectors even though they have better properties. We have to use liquid crystal on silicon because it's going to be $5 a module. And so from the beginning, we forced ourselves to make the lower cost stuff work up to the standards that we needed instead of going.

**Dave Jones:** But you're talking about like spinning ASICs and stuff like that, which requires huge NRE costs. Usually, yeah. How do you amortize the cost over X number of units?

**Jerry Ellsworth:** So we're going to have a single chip on the headset itself, which is going to do all the tracking. So currently, all of our tracking is done in an FPGA. So we're tracking all these points that are embedded in the surface, which there's an array of LEDs that our camera looks at. That's done in FPGA. And then we have some high-speed serializers that are bringing the video stream up to the glasses and doing all the Pico projector work. So all that's going to be integrated into these metalized gate arrays. So that's...

**Dave Jones:** Ah, right. So it's not a full ASIC. It's a gate array.

**Jerry Ellsworth:** Yeah, instead of being able to do the ASIC for a dollar, it may cost us $4. But it's a nice in-between.

**Dave Jones:** Yeah. Yeah. How much does it cost... For those who want to do stuff like this, how much does it cost in the NRE side of things to do a gate array like that, of that complexity?

**Jerry Ellsworth:** So I got introduced to these metalized gate arrays back when I was doing toy design. And it's kind of the workhorse of the toy industry because it's not the cheapest, but it allows you to quickly make these designs. And then next year, you can just do another design very inexpensively. So they're about $10,000 per mask layer. It may have gone up in the last few years, but it's still...

**Dave Jones:** And how many mask layers do you need typically for something like this? Three to four.

**Jerry Ellsworth:** Okay. So it's not exactly cheap, but it's...

**Dave Jones:** No, but it's relatively affordable as far as ASICs go.

**Jerry Ellsworth:** Yeah, it's not a half million dollars like a 65 nanometer mask set. Yeah, yeah. Trade-off is per part piece, or per part, you're going to pay a bit more. But they're great. Atmel has a service that does this, ChipX, eASIC. There's a lot of companies out there that have a lot of these underlayers. So for those that don't know, the metalized gate arrays have an underlayer, which have different things like serializers on them and memory blocks and multipliers and just a sea of gates. And then you just... You apply these metal layers to make all the connections. And so you're only buying the metal layers because they've already put the money out.

**Chris Gammell:** Because it's cheaper to just make everything... Yeah. Got it. Over and over again to have a standard set underneath, right?

**Jerry Ellsworth:** Yeah. So you just have to fit within the features that they provide you.

**Dave Jones:** Which... Got it.

**Jerry Ellsworth:** So luckily, our design's using quite a few gates, but it's not going to fall outside the metalized gate array realm.

**Dave Jones:** Oh. How easy is it to move between the vendors? What sort of tools are you using for that? So let's treat our technical audience here by...

**Chris Gammell:** The gamers might want to, you know, if you're just purely gamers... Yeah, yeah.

**Dave Jones:** Because I'm sure there'll be a lot of gamers who've never listened to the Amp Hour before just listening because you're on here talking about this sort of stuff. So we have to serve our existing Amp Hour audience.

**Chris Gammell:** This is an electronics podcast. We should tell people that are new to this too.

**Dave Jones:** That's right. This is not a gaming podcast. I'm excited. I love learning out about this stuff.

**Chris Gammell:** Diving into nerd zone.

**Jerry Ellsworth:** So currently, I'm using Altera FPGAs, although for like intermediate design, I might go to a lower power chip, maybe a lattice part. So typically what I've done is I've used the Altera tools or the Xilinx tools, whichever FPGA vendor, and I do the designs and the simulations all with their tools. And then when it comes time to convert it to the Gatorade, then I'll go work with Atmel or one of these companies and I'll actually sit in their facility and use Design Compiler, usually, which is the synthesis tool.

**Dave Jones:** You've got to go physically sit in their facility?

**Jerry Ellsworth:** Well, that's how I did typically in the past because they were on all these Sun workstations and it was... Yeah.

**Dave Jones:** Oh, okay. So it's not something you can do on the desktop. You can just download from their website and do it home?

**Jerry Ellsworth:** You know, they might have tools these days. I haven't done one in about five years, so...

**Dave Jones:** Right.

**Chris Gammell:** That's good to have people there too, though, if you have questions and stuff, right? I mean...

**Jerry Ellsworth:** Yeah, when you're going to be spending 50 or 60K, you kind of want to make sure that you're going to get it right the first time, which I have some horror stories of getting some inversions wrong on IOs and just barely being able to save the chips because I... Software guys to the rescue to help me out. Yep.

**Chris Gammell:** Just invert this and then invert it again and then again. Exactly. Yeah.

**Dave Jones:** So how much risk is there going from your taking your VHL or Verilog? Which is it? Actually, right now I'm using both. Oh, okay. Combo. Yeah. Right. So how much risk is there going from that design to your Gatorade?

**Jerry Ellsworth:** There's a bit of risk there. So it's all on the test benches that you make before you go in. Right. And how much coverage...

**Dave Jones:** Are the test benches transferable? Like, can you use the VHDL test bench on the Gatorade tools? To some degree, yeah.

**Jerry Ellsworth:** Right. As long as you're working at the IO pads and kind of working your way in, you're pretty safe. Got it. But there's... Personally, for me, it's very difficult to go from a behavioral simulation that I'm using on FPGA to actual timing-driven simulation on the ASIC. So there's always a bit of risk there that your timing isn't going to be exactly the same. And that's... Got it. There's another almost horror story that I was able to save a chip where I tri-stated a bus for one clock cycle. And I didn't even realize it because I was working mostly in behavioral simulation. And by tri-stating this external bus, the bus was floating for a while and I was getting wrong data coming back in. And I'm like, oh, my God. Yeah.

**Chris Gammell:** Something latched and you're like, oh, hey, that's garbage. Oh, my goodness. What's going on?

**Jerry Ellsworth:** When I got the, you know, 100,000 chips back and they were all doing this, like, weird quirky thing. Ignore. New bear. No, that's not new bear. I just added some capacitors to the data bus. Yeah, exactly. It's a pretty dirty hack, but it worked.

**Chris Gammell:** Yeah, exactly. So, what about the... So, you know, so you have all this stuff beforehand. Sorry, you don't know which chip fab you're going to go with beforehand, right? So, how do you design for their process? I mean...

**Jerry Ellsworth:** Okay. So, one thing that I always do, I kind of learned a long time ago, is, like, avoid the FPGA vendor's specific IP at all costs. Oh, yeah. Yeah, they'll take you to town.

**Chris Gammell:** Yeah. Buy it from them, right?

**Jerry Ellsworth:** Yeah. I have stories around that, too, but...

**Chris Gammell:** Experience talking here, folks.

**Jerry Ellsworth:** Oh, boy. Yeah. So, avoid those. Like, make sure all your I.O. pins are at the top level. So, that's, like, the number one thing that you've got to do, is you've got to switch over to the I.Os that the chip vendor has. Memory blocks, make sure that those are in a separate wrapper, because their memory blocks are going to be different than the FPGA vendor's memory blocks. Multipliers, you're not always going to get multipliers, so you may have to, like, do your own... Shift and add multiplier or something in there. So, plan ahead to have, like, different... Also, yeah, plan ahead in your design to be able to have different numbers of clocks. Okay. Like, one vendor's RAM may take two clocks to do a readout, and FPGAs, you might be able to do it in one clock. And so, leave that kind of flexibility when you're doing your design.

**Chris Gammell:** So, lots of modularity. Is that kind of the key? Like, a lot of top level modules and stuff to break it up like that?

**Jerry Ellsworth:** Yeah. The closer you get it to the actual RTL that you're going to use in the ASIC, the safer it's going to be when you actually do the conversion.

**Chris Gammell:** Okay.

**Jerry Ellsworth:** So, if you have to move from, you know, some multiplier to a different multiplier, it's pretty risky.

**Chris Gammell:** Yeah. How does it look from a... So, you said that they have, like, the built-in serializers, right? And a lot of FPGA vendors have that, too. Is it kind of like then just calling a library to actually use that kind of stuff, and it compiles, you know, out of sight, out of mind kind of thing? Or how do you actually implement the stuff that they have there? Yeah.

**Jerry Ellsworth:** It's typically there'll be, depending on how, what the piece of IP is, sometimes they'll give you, like, a RAM compiler. So, you can actually put in all the parameters, and it'll generate the wrapper for you, and it'll infer that memory for you. So, other times, it's more manual, where you're actually having to, you know, go through and tie all the ins and outs of your, that piece of IP up correctly. That's, for instance, my IOs that I got inverted. That was one of those things that I couldn't infer an IO. I actually had to wire it up myself, and I, their tri-state or something was a different inversion than what I was using in my design, and I botched it. Yeah. Yeah.

**Chris Gammell:** It's crazy. Yeah, and I mean, that's where naming really comes into play then, right? I mean, like, if they just naturally invert something, they don't add, like, an underscore N or however they notate it normally. It's like, oh, you're screwed.

**Jerry Ellsworth:** Exactly.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** It's going to be, the serializers are going to be kind of a challenge for us, because, you know, really, I'd like to, right now I'm using these really high-speed TI serializers to bring the video up, but they're just, they're going to, I can't use them. They're going to use an $8 part in the glasses. Yeah. Right. So, I'm going to have to use what they've got and serialize the video up that way. So, I'm going to have to somehow find a way to choose something in an FPGA vendor that's close to the, what the underlayer for, say, Atmel or ChipX or one of these companies will supply. Mm-hmm. So, that's how we're going to get the cost down.

**Chris Gammell:** Oh, yeah. Right. Pull it all in. So, like, that's a CERDES, though? Like, is that the idea? Like, how on FPGAs these days, they're all, like, the CERDES type of IP that's built in, and then you're saying that that will be the similar thing to the chip vendors?

**Jerry Ellsworth:** Yeah. So, I'll have to find something that will mimic that so I can prove out the design in real hardware before we actually go and we spin the chip. Okay. So, that's the only thing I have anxiety about right now is the serializers that I'm not going to be able to find something that's equivalent in an FPGA so I can actually test wire length.

**Chris Gammell:** Yeah. How fast are we talking here? Right. Are we talking, like, the gigasample type of stuff? Yeah. Because I think the FPGA ones are, like, six now, like, six and 26 kind of speeds.

**Jerry Ellsworth:** Unfortunately, a lot of these Gatorades don't have the super high-end serializers. So, unfortunately, instead of going one wire up, I'm probably going to have to do three, four wires up to get the video up.

**Dave Jones:** Is that an issue, though? Why wouldn't you do that as a matter of course? I would have thought that would be safer.

**Jerry Ellsworth:** Well, as much flexibility as you can put into the ASIC as possible and future-proofing it, too. So, if we go to, you know, higher-resolution micro-displays, we want to have some of these serializers there that we can enable or disable.

**Dave Jones:** One of the big questions on the hardware that I've got, how much power do these two Pico projectors take?

**Chris Gammell:** Yeah, that's a good question.

**Dave Jones:** Because when you do a final pair of glasses, I mean, how long is a battery going to last pumping out, I presume, a couple of watts of life? I know the answer to this. Each if it's under, like, a...

**Chris Gammell:** Yeah? Yeah, they don't use batteries. Right, Jerry?

**Jerry Ellsworth:** No, actually, we want to do battery power, so...

**Chris Gammell:** Oh, okay. Never mind, then. Yeah, we don't want to...

**Dave Jones:** Oh, wrong. Wrong. Well, I'm sure your... So, your prototype didn't use batteries. It just had wires coming off. Is that the... Absolutely.

**Jerry Ellsworth:** And early access developer-type kits will certainly be wired, but...

**Dave Jones:** Oh, there'll be wired glasses. Okay, there won't be battery. Okay, right. So, that... But anyway, that question is still valid. How much power do these things take? I'm just curious. I don't know.

**Jerry Ellsworth:** So, we're still working through all the power budget on it. Right now, we're burning way more power in our FPGA, just because it's not very efficient, and I haven't really done much clock gating or any of that yet. So, it's still really early to say, but the retroflective surface is 90% efficient. So, the glasses, when you don't have the surface there, if you just, say, project onto a white piece of paper, you can't even see. Yep. There's so few photons going out. So, actually, the LEDs that are illuminating the L-COS panels are not very bright at all. Okay. So, that's actually going to be a small factor in the actual total power budget. It's the DSP that's doing all the image tracking. It's probably going to dwarf the LEDs.

**Dave Jones:** Right. So, that's totally different to, like, consumer camcorders and cameras that now have these Pico projectors in them that are designed to be projected on a wall. They need much greater illumination.

**Jerry Ellsworth:** Yeah, because there's so much scatter. So, if you just project on a wall with these glasses, you can't see anything. So, that's the magic of the retroflective surface. And luckily, the surface is really inexpensive and can be rolled up and stashed away.

**Chris Gammell:** And you can add stuff to it, right? You can add, like, tracking and everything else.

**Dave Jones:** Exactly. And...

**Jerry Ellsworth:** Yeah.

**Dave Jones:** Well, that's the other challenge, isn't it? Adding tracking around the edge of the surface?

**Jerry Ellsworth:** So, we're using LEDs. They're IR. They're invisible. And they're modulated so that we can tell the points. We can tell them apart so we know your orientation around the surface.

**Dave Jones:** So, each individual LED around the surface has got its own modulation? Yeah. It's ringing out its ID. Oh, okay. Right. So, that's like an 8-bit ID number or something, is it?

**Jerry Ellsworth:** So, temporarily, we're keeping track of their IDs. And then, we're tracking their position over time. And then, wands or figurines and all these other things, these props that you might make for the system will use the same type of tracking LEDs embedded into them.

**Chris Gammell:** So, how do you start doing, like, unique identifiers? And how do you determine... I guess it would be like a set. You have to have a set that only has so many unique IDs? Or are you actually putting unique ID chips on there? Yeah.

**Jerry Ellsworth:** So, our initial plan, what we're going to deliver for folks to experiment with, folks that want to do more than just consume the games, is we don't plan on hiding our modulation scheme on the LEDs. So, if you want to make your own figurine, you know, maybe you'll get a microcontroller and just do it yourself. We want to provide the APIs and the prototyping system. So, if you want to just experiment with the prototyping system, you can make your own game experiences that way. And then, you'll have access to these... All these points and IDs that are coming down from the tracker. Then, the APIs for those hardcore game developers that want to hook it to their own custom game stuff. Or, there's actually a lot of people... It was interesting going to Maker Faire. There were a lot of folks that were coming up with very interesting uses for this, like surgery simulators or teaching aids. Operation becomes gross. Yeah, operation. I want to use it on my oscilloscope. I want my oscilloscope trace. So, I just, like, put my circuit down there and I wear the glasses. And then, I'm just working on one of these mats. And then, you can just see...

**Chris Gammell:** Tony Stark style, right? You actually, like, you put on some... You get the... What's that new hands... Where you can put your hands into the field and it tracks that as well? I forgot the name. Oh, the leap motion. Yeah, leap motion. That's a cool thing, too.

**Jerry Ellsworth:** Yeah. So, hopefully, we can get some integration in there for things like leap motion and connect. We don't want to own the entire space. We just want to have a little piece of it. And then, people use the peripherals that they want.

**Chris Gammell:** Yeah. You're not thinking big enough, Jerry. I need to own it all. All of it. The whole world. I can't help thinking that eventually someone's going to look back and be like, what the hell were they thinking not charging more for this kind of thing? Like, I know that's, like, my inner business brain talking and it's, like, really terrible. But, honestly, you guys are making some really cool stuff. And it seems really reasonably priced. And I guess that's a really good way to get in the market.

**Jerry Ellsworth:** Well, it's really early. You know, I don't want anyone to, like, commit us to that price point. We may, like, discover that. Of course. Yeah. We botched our first three Asics or something. Yeah. And now we have to charge more or something.

**Chris Gammell:** Jerry needs a new pair of shoes.

**Jerry Ellsworth:** We, uh, well, we envision, uh, you know, folks will have their glasses. They'll go over to their buddy's house and they'll all sit around the table and they'll hook it up to their cell phone and they'll, they'll play together. But if it becomes too expensive for a system, then.

**Chris Gammell:** Yeah. That's the doom of a lot of systems, actually. I remember, I remember hearing about some of those where they just, they're like, oh, yeah, $600 a system or something. And no one buys it. You can't get any, you can't get any foothold then. And, and games are usually where they usually make the money anyway, so.

**Dave Jones:** Well, they reckon that $300 is the, is the, uh, consumer price point where people, if it's under 300 bucks, people sort of just, you know, it's an impulse buy. If it's over, they sort of go, you know, yeah, exactly.

**Chris Gammell:** So I have a question about the cell phones. Cause I was intrigued by you saying you're hooking up to those. Um, cell phones are, uh, notorious for having very slow interfaces to them. How the heck are you going to actually talk to them? Are you, are you planning on doing wireless eventually?

**Jerry Ellsworth:** Oh, so a lot more cell phones and tablets are, are coming out with HDMI out. So that's what we need a digital video interface.

**Dave Jones:** Oh, right. Yeah.

**Jerry Ellsworth:** And since all of our tracking is done in hardware, it's actually a very, very slow data stream going back. The only thing that we need to be very careful about is that there's a very low latency going back. Yeah. One of the challenges in augmented reality is that, um, if there's latency, say from the head tracker, you move your head and it takes four or five frames to update. Uh, it makes it look like all the objects that you're rendering in the world just jumped to the side. They don't track smoothly. Right. Yeah. So we've actually done a lot of work to keep the frame rate up to 120 Hertz. The tracker's running at 120 Hertz.

**Chris Gammell:** Which doesn't sound like much, but for video, that's a ton. I mean, most videos, what? That's a lot. Yeah. 30, 30 Hertz or is that right? Or 60 Hertz? I'm not even sure. In Australia, it's 25. Does that translate to frames per second? That's what I'm thinking is, is FPS. Is that, is that the same thing? Okay. Cause like movies are 24 and home videos are 29 or 30, right?

**Jerry Ellsworth:** The real magic started for us, um, over a hundred Hertz is where it really started feeling like these Jenga blocks or Jirga blocks are, uh, Jirga, Jirga, Jirga. Are on the surface. Okay. Yeah. And, uh, along with some prediction. So you can predict where your head's moving. So with this, with prediction and having very low latency, uh, it really looks like as you walk around the table that those blocks are really there. And when you smash them with a wand that they're really flying up towards your face.

**Chris Gammell:** Why a hundred Hertz then? Is that just based on like human reaction times and stuff like that or what?

**Jerry Ellsworth:** I'm not really sure. Uh, we tried 60 Hertz was pretty good, but getting over a hundred Hertz really, really looked good. Okay. And so all the demos that we presented at, at maker fair were, um, at least over a hundred Hertz.

**Chris Gammell:** Okay.

**Jerry Ellsworth:** And modern, modern cell phones are getting really, really powerful. There's some hot stuff in the pipeline. That's good. You know, coming out for chips.

**Chris Gammell:** So, so you're saying though that the, so data going back down the pipe to, to the cell phone, are you talking, you can't talk through HDMI, can you? Like how are you actually input data? I, I, that's the thing I'm not, always not sure about.

**Dave Jones:** Like there's no way to hook to a data standardized interface, you know, for these glasses to work with sort of any gaming system, are you looking to provide an interface for each system or are you going to leave that up to the manufacturers or?

**Jerry Ellsworth:** Many cell phones these days have USB on the go and they have digital video out. So our plan is to use USB and, and, uh, HDMI out.

**Chris Gammell:** Okay. I didn't realize, I didn't know that cell phones were going to USB on the go. Cause that's the one where it goes, uh, both it can do, it can be host or it can be a device, right?

**Jerry Ellsworth:** Yeah. We're going to see more and more devices like that. Okay. So, so currently if, if for the radio listeners, so I can describe what the glasses look like. Um, the glasses, the current ones are kind of big. Uh, and weigh several hundred grams, lots of hot glue on them. The, uh, so we've actually mocked up using real projection engines, what we think we can do for the glasses and they're about 60 grams of weight. And then with the serializers, we've reduced it down to just a few pairs of, um, micro coax down the cable. So the cable that we're currently using is about what you would, uh, you would think of for like a earbuds, like iPod earbuds. It's about that thickness. And that's what we demonstrated it at a maker fair. And then it goes to a box and this box doesn't have to be very big, but this is where, um, if there's a battery, um, that's where it would live. And then there's some receivers for the HDMI video. So there's not much going on there. And then from there, that's where the connections go to your PC or your tablet or your phone. Right.

**Dave Jones:** So all the processing is still done in the glasses.

**Jerry Ellsworth:** Yeah. We need it close to the image sensor because we want, we actually pull the data off the image sensor and we process it immediately that we get the latency really low. So it's right up next to the, the image sensor, just screaming along as fast as it can go.

**Dave Jones:** Yeah. You can't send it down a couple of meters of cable, right? No, unfortunately not.

**Chris Gammell:** Yeah. Cable gets it real expensive then. And even, even then, right? I mean, even with optical, it's still, you probably wouldn't be able to do it. Yeah. There's still latency in optical, right? So.

**Jerry Ellsworth:** Yeah. So, so yeah, the, there's, there's going to be one ASIC that's sitting up on the glasses that it's doing all this image tracking. And that just sends point data down to the cell phone. And that's also a huge thing doing most of the processing and the ASIC that way the, the phones, which are still a little bit anemic as far as processing need to, you know, we can't have them processing entire frames of video. They're just a way to, to do it. So it has to be done up on the glasses.

**Dave Jones:** So ultimately what's the data rate coming back from the glasses after it gets out of the ASIC? You said it's low, but is it kilobits? Is it megabits?

**Jerry Ellsworth:** Um, so we're actually on our current prototype, we're just using a hundred and was it 115 to, um, RS two 32. Right.

**Dave Jones:** Serial. Oh, okay.

**Jerry Ellsworth:** And we're not even close to saturating that.

**Dave Jones:** So ASCII out, right? Old school. ASCII position, you know? Great. I love it.

**Jerry Ellsworth:** Yeah. It's, um, we may just leave that exposed. Who knows? Um, we were talking to some folks at Maker Faire that were looking at our tracker and they're like, wow, we want to do robotics with that. Yeah. Like, oh sure. Yeah. Maybe the tracker is something we split out and let people, uh, you know, do other stuff with.

**Chris Gammell:** Number one feature requested Maker Faire, of course, is hackable, right? That's the, uh, that seems to fit.

**Jerry Ellsworth:** Well, if anyone knows my projects, I always try to make them hackable. So like the Commodore joystick and this one will certainly have Easter eggs. Ah, yes.

**Chris Gammell:** Then we need to ask. Are there any like fart jokes in this one as well that we should expect? You hit a Django block and it, I don't know. Melt into a puke or something. I don't know.

**Jerry Ellsworth:** You'll, you'll just have to, uh, fund the Kickstarter so you can see. Oh, nice. See what I did there? Enjoying one of the roadshow tours. Yeah. Yeah. So, well, this, this will be different though. I was always like getting myself in trouble with other companies by adding Easter eggs. So, but it's, you know, it's Rick and I's company. So it's just me and Rick. Exactly. I'm the boss.

**Dave Jones:** Yeah. So what do I think you'll have to bring on other software people? Because there's a, you know, there's an awful lot of software, which is gonna, you know, if you want to develop real apps and real demo games and stuff like that, that's a lot of work. I would suspect being a non game programmer. Yeah. You're absolutely right.

**Jerry Ellsworth:** So as soon as we get funding, we're going to have to start staffing up. We're, we're staffing up right now, but you know, it's coming out of our own pockets. So it's kind of limited, but, um, this actually will turn into more of a software project than a hardware project in the end. Just like what you said earlier, the revenue streams will probably come from, uh, software more so than hardware.

**Chris Gammell:** Yeah. Not just the game industry.

**Jerry Ellsworth:** Our hopes is to, uh, offer a place to curate, um, other people's stuff. We want people to make money on this. We want people to make things and give it away. Oh, like a marketplace kind of? Like, like, uh, apps almost? At least direct people where they can go and get it. We don't want to be a, you know, walled off garden like some, like Apple and some of these places where I can't even, you know, if, if I write a program, I can't even give it to you guys. I have to go through Apple to deliver it. So we hope to be more open than that.

**Chris Gammell:** That's good. I think that'll, that'll pay dividends for you guys. What about, uh, so once you get funding, I mean, is this, uh, is this like Jerry hops on a plane or are you going to go to China for a while you think? Or, or what's the, what's the, I mean, is that, is that, or is that looking too far forward?

**Jerry Ellsworth:** Well, I'm, I'm accustomed to doing manufacturing in China and I'd like to do it domestically if possible, but I just don't know if that's possible yet. That's something we're going to look at. Yeah. Okay.

**Chris Gammell:** But, uh, well, I mean, I, I wasn't even asking about that. I mean, I expected people, I expect people to go to China, honestly. I mean, like that's the, that's kind of the Kickstarter thing. Obviously you've done it before. So that, that would be the different point from a lot of Kickstarter projects is people are, you know, they're like, Oh, I got to go to China. And now you're just like, Oh, I have to go back to China. Okay. No big deal.

**Jerry Ellsworth:** Oh God. I got to go back to China. Yeah. Yeah. That's actually, I've been kind of following a bunch of Kickstarters over the last few months and it, it's kind of a pitfall for some of those guys is they're like, Oh, we're going to make this thing. But they've never done it before. And then they go, they've never done it. They find out that China's hard.

**Dave Jones:** Even if you've done it before, I mean, things can go wrong. Yeah. And, you know, and you can be back to square one and Oh damn. Or more, not quite square one, but you know, um, it's just little things can, uh, really, you know,

**Jerry Ellsworth:** That's why we suspect that we're going to take secondary funding besides Kickstarter. I mean, we, we suspect, especially since Maker Faire and how people were really positive about it, that we'll probably do fairly well on Kickstarter.

**Chris Gammell:** Oh, hell yeah.

**Jerry Ellsworth:** But, um, I, I guarantee you will. Yeah. But we, but the software side's what's really going to make it magical. And we'll probably have to take on some investment from VCs at that point, but it'll be interesting. Uh, Not, not many people have gone down this route before. So it'll be interesting to see if, how VCs react to us saying like, Hey, we've got, you know, Brand new gaming system. Yeah. We got, uh, you know, a hundred thousand in the bank or whatever that money we get from Kickstarter is. Yeah. It'd be sure nice to have another 5 million.

**Chris Gammell:** Yeah. I could get a lot of chips for that. I'll trade you all my C64 chips. You could tell them that, right? Use that as collateral.

**Jerry Ellsworth:** Oh, there we go. Yeah. My retirement fund is all my C64 chips.

**Chris Gammell:** Maybe while you're over there, you can get them all packaged up too. You can be like, Oh, well, since I've already done, you know, get like the, the sweetheart deal of like, well, we got all these Castor chips and yeah, you just package those old C64 chips because I just have the silicon.

**Jerry Ellsworth:** I'd love to do something with those someday. Yeah. And it looks like it's going to be off in the future somewhere.

**Chris Gammell:** Oh yeah. Yeah. You're going to, you're going to be busy. I'm guessing this is the last time we talked to you for a couple of years.

**Jerry Ellsworth:** Maybe.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** It's going to be, yeah, it's going to be pretty crazy. It's going to be fun though.

**Chris Gammell:** Good crazy.

**Jerry Ellsworth:** I, it's interesting being on this side of a startup. I've done contract work for a good part of a decade and walked into a lot of startups been like, you know, number five or six person in the door and we're starting from scratch and they're just getting their funding and like seeing it from that perspective now reversing the roles and being like the one out trying to scrounge up the funding is, it's quite different.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** Not only do you have to do all the design work, you have to do the funding part of it too.

**Chris Gammell:** Well, I think you're doing it right though. I mean, having the prototypes to show is, I mean, that's ahead of a lot of startups, right? A lot of them are vaporware and not a lot of them, but some of them are, right? Yeah. You know, where it's like, you're just trying to kind of go on an idea first because you don't have the money to even bootstrap the stuff and the fact that you guys are bootstrapping the early protos, that's a really good sign. Yeah.

**Jerry Ellsworth:** Rick and I thought that was very important that we get it out there really early and show that it's real because there is so much vaporware out there and especially around gaming hardware and we were talking to some folks that wanted to look at it and they were really very dubious because we were trying to get some meetings going. We were like, hey, this is, guys, this is what it is. You know, stop by the Maker Faire booth and like kick the tires. We're not, you know, there's no sense for us to try to like, they were wanting us to do some videos and supply them with a bunch of stuff and she's like, hey, just come, come just take a look at it. It's real.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** And it was pretty nice when they came out and they actually tried it for the first time. They're like, holy, whoa. Yeah.

**Chris Gammell:** They're probably pissed that they didn't get to see it privately first, but, you know, like that, that's just, that's a good thing to show. I mean, that's, that's really different. That's cool. Yeah. I have to, I have to say, I, I want you to be careful with VCs. They seem, I don't know, it seems like some of them are really good, but some of them just, eh, eh, I don't know. All of them, come on. Not all of them. Some of them do, I mean, some of them do good work, right? I mean, like there's, there's some good ones out there, but some of them just scheme.

**Dave Jones:** No, but ultimately it doesn't matter who they are. They're in it for the money. They want to make a massive profit for their risk. End of story. Yes. Yeah.

**Chris Gammell:** You're not wrong.

**Dave Jones:** You know, there are no nice VCs. They're all the same. Yeah. Some are nicer people than others, but ultimately, no, they put, they invest in risky stuff and they expect a large return for that large amount of risk.

**Chris Gammell:** Yeah.

**Dave Jones:** And they will, and they will pressure you into doing all sorts of things to achieve that end.

**Jerry Ellsworth:** So. And they're, they're very good. A lot of times to give you just enough to get you on the edge of success. Yeah. When you are desperate for that last little bit of money, then it's like, well, for another 50% of your company, we'll. Yeah. Yep.

**Chris Gammell:** I've certainly seen that. That's no fun. So be careful. Not nice.

**Jerry Ellsworth:** Well, that's why I'm excited about the crowdsourcing.

**Speaker ?:** Like.

**Jerry Ellsworth:** Yeah. Right. Yeah. We want to show. Yeah. Show. This is for real. We're, we have this credibility. We've done this before. It's, it works. And. And.

**Dave Jones:** But you've got the pressure to produce then. If you know, you get 10,000 people backing it, then you've got 10,000 people screaming at you. Where's my glasses? Where's my glasses?

**Jerry Ellsworth:** Which is actually a kind of scary thing because the production runs that I'm used to is in the hundreds of thousands in toys. Yeah. So we are. This will be under 10K, right? Yeah. I mean, I, I don't know in the history of Kickstarter if there's any projects that have sold more than like 10K, but that's probably pretty typical for a Kickstarter that's very successful. Yeah.

**Dave Jones:** It's usually a couple of thousand I've been seeing for hardware type projects, but because this is a gamer one and gamers go crazy about this sort of stuff, you know, you could reach

**Chris Gammell:** five figures. And that was, I think, I think that was 60,000 watches, I think, but that was, that was a lower cost as well.

**Jerry Ellsworth:** Oh, was it? Oh, okay. Yeah. They really, they knocked it out. Oh yeah.

**Chris Gammell:** But they got, yeah. Is that right? I might be wrong about that. It was a lot. It was like a hundred dollars a watch. I think you might be right. Yeah. Cause it was, yeah, I think it was like 60,000 watches or something like that because then there was, you know, the different funding levels and everything too. So that's.

**Jerry Ellsworth:** So we're crunching a bunch of numbers, like scenarios. What if, what if only 10 people order or what if a hundred thousand order?

**Dave Jones:** So we, we want to try to be prepared.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Yeah. It's important because that changes the entire game, doesn't it? In terms of manufacturing and, and actually designed for manufacturing. Exactly. Really. I mean, you, you may have to make some large design changes based on how many orders you get. Really. It's, it's unfortunate.

**Jerry Ellsworth:** I would suspect. The difference between NRE for manufacturing a thousand units versus a hundred thousand units is not much.

**Chris Gammell:** Right. Yeah.

**Jerry Ellsworth:** And it's all the same amount of work.

**Chris Gammell:** Yep.

**Jerry Ellsworth:** Yeah.

**Chris Gammell:** And then they want to charge you again when you go back after that first thousand, right? They're like, oh, well, you want another thousand? Ooh. Oh, yeah. There is a fee. Well, you could just do what Google does. I mean, you could just charge $1,500 per, per prototype, basically, effectively. Right. Suckers like me might pay it.

**Dave Jones:** You've been sucking into buying. Yes, Chris. You suck it into winning. Winning. Your Google Glasses. Yeah.

**Chris Gammell:** You should have people win it, Jerry. That's the idea.

**Jerry Ellsworth:** Yeah. Right. I miss that. Was it Google Glass you had to win?

**Chris Gammell:** Yeah. You had to do stuff on Twitter and Google Plus. And if you said what you're going to use it for, they would pick something. And I just put some random stuff on there, like building hardware around it. And they're like, oh, yeah, you won. But it didn't matter. A lot of people just said I would use it to video record stuff. And yeah.

**Dave Jones:** Anyways. By winning, they meant you get the opportunity to buy it first for $1,500. You don't actually win anything. You just win the opportunity to buy it. Yes. Ah, gotcha.

**Jerry Ellsworth:** You know. Well, now we brought up Google Glass. The number one thing that we get asked is what's the difference between this and Google Glass. Oh, yeah.

**Chris Gammell:** Everything, right? I mean, like that's everything. The similarity starts with the Pico projector and ends with the Pico projector, right? Yeah. Pretty much.

**Dave Jones:** Yeah. Oh, goodness. Do you actually have any competitors in this space at the moment? Is there any other Kickstarter projects or any other startups or people doing similar?

**Jerry Ellsworth:** Well, to what you want to do? I think Oculus is probably the adjacent. I mean, they're a different experience. But there's a lot of overlap. So that's pretty cool. The there are some consumer products out there, but they're all really expensive. They they're usually typically the collimated displays set to infinity and they go project directly into your eyes. And they're usually very limited field of view. Quite different. The best thing that we saw was there was like a Korean company. I forget the name of it right now. But they had a these really they're kind of heavy, but they were pretty wide field of view glasses that actually worked fairly well. But they have no tracking, no audio on them. Oh, the audio. Oh, boy. I can't. Oh, I can't wait to. So it's the thing I'm the most excited about. Since we have head position, we can do all kinds of fun things with audio. Yes, of course. Yeah. A little zombie standing on the table. You could put your head right down next to the zombie and hear him whispering or something.

**Chris Gammell:** You'd be like, what are you saying, little zombie? All right. That's awesome.

**Jerry Ellsworth:** So I suspect that there's going to be entire games that just use head position and sound and almost no graphics at all.

**Chris Gammell:** Oh, like, yeah, I can imagine. Oh, man. Like, where in the world is Carmen Sandiego? You could totally replicate. I mean, all the board games of like youth, you could totally replicate all of those, which is so much fun. Like Risk. Oh, my God. Risk would be amazing. So what about the tracking, though? I mean, so you said that you have the vision tracking, right? You're actually looking at these modulated LEDs and stuff. But then, and I do have a question about that. But then also, you said you're just using like, is it just like a nine axis controller? Is that the idea for actually like moving your head and everything with like where it streams out data? Or are you not allowed to say?

**Jerry Ellsworth:** So, yeah, sure. I can talk about it. It sends out points, which are just X, Y, and some other magic sauce that we have in there. And that goes out to the host, which then solves for world position. So there's a math behind that that figures out where you are in the world from all these points that are coming down. And that's pretty much it. So if you rotate your head, we can detect the rotation. If you move laterally, we can pick that up. We can, anywhere within a volume, we can figure out where you're at. Right, and there's like a practical volume, right?

**Dave Jones:** And this is just done with the IR?

**Jerry Ellsworth:** Yeah, IR LEDs.

**Dave Jones:** Right, okay. So it's just IR transmitting from the surface and then the... Cameras on the glasses. What type of sensor? Right, you've just got a camera. How many pixels?

**Jerry Ellsworth:** It really doesn't matter on the pixels all that much. It does affect the precision. We're just using a standard HD image sensor right now from a cell phone. And it's the really, we were using the, honestly, it's a really crappy rolling shutter image sensor. Yeah. Which there was a lot of debate within Valve that if, whether it'd work. And we never got that far within the company. But as soon as we got out, we're like, all right, they've got their tech. We can't use that. So we got to do our own. So we went down this other path and holy smokes, it worked.

**Chris Gammell:** Wait, so you're not actually doing, you don't have external, like an IMU type of chip, external? Is that what I'm...

**Dave Jones:** No gyros, nothing.

**Chris Gammell:** Oh, okay.

**Dave Jones:** It's all absolute. It's just the angle, it's just angles and math. Yep. That's it. Lots of math, huh? It's all absolute. Yeah, lots of math. So... Well, basic trigonometry, huh?

**Chris Gammell:** Wow, that's really good. So, okay, so then the other question I had about that is, so the camera's only looking at the IR LED, is that the idea? Is that, that's all it really does is, well, all of the LEDs?

**Jerry Ellsworth:** Yeah, so the reason we didn't use IMUs, they're pretty good at very short time spans, like they know that you moved, but they're not good at anything... Drift. They drift extremely badly. They, you can't do any kind of translation with them, they can't figure out, you can't figure out if you moved laterally with them. You can figure out rotation and you can use gravity to figure out that. You can use, there's magnetometers, which you can kind of figure out rotation, but...

**Dave Jones:** Now it's getting ugly, yeah.

**Jerry Ellsworth:** It's, yeah, it's kind of a dead-end path using that. It's not accurate.

**Chris Gammell:** Yeah, yeah, you need to filter the crap out of them. My buddy did a project on that, and basically the math on that is, right, accelerometers, you need to basically integrate them twice, and then if you think about any jitter in the acceleration, then that translates into huge errors in your integration. Oh, yeah. Two times, and yeah, so that... Jerry said it, it's a complete dead end. Yes.

**Dave Jones:** You just cannot make it work.

**Jerry Ellsworth:** It works great for cell phones and things. Oh, yeah, for those limited apps. Yeah, for those things to look like, they're really locked to the world, but if you want to have something around your figurine and you want it locked to the figurine, you've got to have absolute measurements, so that's why we're doing pure optical. Yeah. And so, the majority of our time after leaving Valve was just refining this tracker, and that's what's really special about our system is, at Valve we had a system that was like $20,000 or $30,000. It was like a really military-grade tracking system, and we're achieving that with like $8 worth of parts. Oh, excellent. Yeah.

**Chris Gammell:** That is magical.

**Jerry Ellsworth:** That is really impressive, Jerry. I didn't, it surprised me too that we got that kind of accuracy, we just kept pushing it and we kept like futzing with optics and we're like, oh, it just got better. Oh, hey, it just got better, and then pretty soon it's like, our very first experiments in the space, the jitter was so bad from, we were doing full frame capture, sending it down to the PC, the PC was looking at these markers, these paper markers. And the result looked like you were in a bouncy car or something. These little characters were jumping all over and bouncing, and now it's just rock solid. You can get down and you can get really close to them, and there's just a tiny bit of jitter, but it's pretty acceptable.

**Chris Gammell:** So, how do you, okay, so another question is, so with the IR LEDs, right, that's how you used to track it. As you, like, you said you could kind of move down towards the characters and you could kind of, you know, like, say you could whisper, or they could whisper to you or whatever. Um, as you move towards the actual surface, do you ever lose track of the LEDs? Like, do things get in the way, or if, depending on how you move your head, do you lose track of absolute position because you can't, you're not pointed right at the LEDs anymore? You could, yeah. What happens then?

**Jerry Ellsworth:** Um, so, uh, right now we have one cluster of LEDs, just mainly because we didn't have time to work on putting them all around the edge. Uh-huh. So, we have over a hundred degree field of view on our camera. Oh, that's pretty wide angle. It's really wide, so you can actually be, like, way off axis and still track. Uh-huh. Um, but if you put your hand in front of the camera, which is dead center between your eyes, you can lose track that way. You can actually get within inches of the surface. Huh. And currently with only one cluster of LEDs on there, you lose track, like, four inches away or something. It's pretty good. Uh, definitely need some improvement there as far as, like, having robustness by having more LEDs around the surface. Okay.

**Chris Gammell:** All right, so as the playing field kind of evolves, you might be able to change that and make that...

**Jerry Ellsworth:** So, you need a certain number of them. You need about five points. For, like, triangulation and stuff? Yeah, to keep track of the surface. So, you get below that and things go bad really fast, but...

**Dave Jones:** So, your key technology here is the imaging, ASIC, and processing. Is that what you see as your key technology? That's it.

**Jerry Ellsworth:** Actually, with all the work, it's been, like, a year and a half worth of work. We looked at everything, like, laser projectors right into the eye and just, like, all the display tech. And when it all, like, in the end, the display tech ended up being, like, the simplest thing. It was just Pico, dual Pico projectors for a stereo image. And it all boiled down to, like, $8 worth of electronics for the tracker. Right. And that's the magic. It's, like, get the total bill of materials down to a point where we can sell it for the slow cost. So, yeah, it's disappointingly simple in the end.

**Chris Gammell:** No, it's... No, there's a lot of magic in there, to be honest. I mean, like, that's a lot of math. It sounds like math. A lot of math.

**Dave Jones:** Yeah, but as a startup, you've got to have a sellable core technology. That's quite important. Not just, oh, we got our bomb costs down to, you know, $8 or whatever. Yeah. Something like that. So, you said it before, like, a lot of people could use this in other areas, not just, you know, glasses and gaming. They could use it for other types of tracking. That's where you could potentially sell the, you know, the imaging tracking ASIC, for example.

**Jerry Ellsworth:** Exactly. Yep. Exactly. Who knows where it's going to extend itself beyond. And we hope to be on a, you know, the gaming side of the revenue stream, too. You know, we think we're creative and have good game ideas. Definitely.

**Dave Jones:** So does everyone, though, unfortunately. I know. I mean, you know, I mean, how many bloody games are there out there? It's incredible.

**Chris Gammell:** I am amazed that this market continues to be so big. I mean, I shouldn't be, right? But I grew up in, like, you know, a lot of games around me. But, man, it is big. People just keep spending money on it, you know? It's just, it's insane to me.

**Jerry Ellsworth:** What's the dream that people have painted since we were kids on Star Wars? And finally, you know, finally all the tech is here so we can have a comfortable, you know, non-headache-inducing experience. And, you know, people have tried it in the past. Yeah. And they haven't quite been able to pull it off with the tech. Yeah. You know, with cell phone cameras pushing everything forward and microprojectors for cell phones.

**Dave Jones:** The question remains, though, will people, is it, will they just go, wow, for a little while and then cast it aside? Nah. See what I did there? Pun. Sorry. Or, you know, like, will it be a long-term, I mean, that's the question. Will it be a long-term technology or will they just play, oh, this is fun, this is fantastic, wow, but I don't want to play it all day kind of thing? Who knows? I mean, that's the risk, I guess. Well, personally, I'm biased, of course.

**Jerry Ellsworth:** Of course. Of course. But I think people are looking for the next gaming experience that's more social. You see it. Like, board games are really hot.

**Jerry Ellsworth:** Warhammer is really hot. All these figurine games, it's like...

**Dave Jones:** But they're incredibly low-tech, you see. They're old school, right? Roland Dyson. Exactly.

**Jerry Ellsworth:** But for me, personally, like, I would love to play, like, a Warhammer figurine-type game, but my friends have been doing it since they were in high school, and they understand it, and I don't. Oh, yeah. And so the hurdle of actually... The hurdle of trying to, like, figure out all the stuff about it is... It keeps me from doing it.

**Dave Jones:** There's a lot of culture involved in that. It's not just the game itself. It's...

**Jerry Ellsworth:** So if I don't have to set up for two hours, if I can, within 30 seconds, roll a mat out and start playing some kind of figurine game with my glasses, that's very appealing to me.

**Chris Gammell:** What about... Are we going to see this in a pinball game sometime soon, too? I mean, what's the...

**Jerry Ellsworth:** Gosh, yeah, we should. Hook it up to visual pinball.

**Chris Gammell:** Yeah, yeah.

**Jerry Ellsworth:** And why don't we throw in the home chip lab, too? We could use it to monitor the... Oh, Jerry, you cut me so deep.

**Chris Gammell:** You cut me so deep, Jerry. You're supposed to be on my side here.

**Dave Jones:** All of our new audience today who are listening, all the gamers who are going to have no idea what we're talking about and we won't even try to explain it. It's a bit of an in-joke here on the show.

**Chris Gammell:** Yes, yes. Come back and you'll hear Dave rant on it forever about how wrong I am. Because you're wrong, dude. Because I'm wrong, of course. Right.

**Dave Jones:** That's right.

**Chris Gammell:** Jerry, once this is done and you make your gajillions, can you go off and fix that and make that happen next? Absolutely. Okay, thank you. Absolutely. Thank you, Jerry.

**Jerry Ellsworth:** I'm so happy to be back. Yeah. You know, it's...

**Chris Gammell:** The land of living.

**Jerry Ellsworth:** Working at... Yeah, working at Valve, I had to be so secretive. And it was kind of like radio silence. All I could do is go on Twitter every once in a while. I'm like, ha ha, I'm working on something cool. Yeah. Stay tuned. I couldn't talk about it. Yeah. And really, I'm a nerd at heart. I love coming on shows like yours and being... We love sharing and... Yeah, talking about what baud rate we're using to communicate point data to the host. It's just like, oh yeah, that's the communication I should have been having all the time.

**Speaker ?:** Yeah.

**Dave Jones:** But that's the problem with all large corporations like this. I mean, they really don't like you doing stuff outside or talking about the company's stuff. It's... It's risky. Is it more secretive at Valve or is it...

**Chris Gammell:** She can't say. It's secretive.

**Dave Jones:** Or is it just normal? You know, it's just... You know. So, like, the first day when they came in, did they... You know, did you have to sign a form saying, I will not say anything on Twitter? You know?

**Jerry Ellsworth:** Valve, as far as other companies, is far more open and encourages the employees to talk to their fan base. Because... Right. Unfortunately, it's no management in there to, like, guide us. So, it becomes a debate. You know, it's like, I just said something on a podcast. And then your colleagues are like, oh my God, you just revealed something. And it's like... Right. You're more accountable to your colleagues. And then it becomes... Felt awkward, like, trying to talk about stuff.

**Chris Gammell:** Oh, there's the talker over there. Let's not sit with her at lunch today. Yeah, exactly.

**Dave Jones:** So, did you feel bad about that? Like, not being able to... You know, A, release any info. And B, have any time outside of Valve to work on your own stuff that interests you? I...

**Jerry Ellsworth:** Going to Valve, I took it very seriously, like, building that team. So, I put in insane amount of hours. It was incredible, the amount of hours I was putting in, trying to build the team up. And work on these projects also. So, like I said earlier, it's often we'd recruit during the day, have our various meetings during the day. And then we'd work way into the night because we were all passionate about building things.

**Speaker ?:** So...

**Dave Jones:** How many people did you end up in the hardware team? Or is that proprietary company information? Yeah, I probably shouldn't say that. Yeah, I probably shouldn't say. Yeah. Well, we know that, you know, there were like four who were on this show.

**Jerry Ellsworth:** There's at least those four. I wish them all the luck. I mean, they're all my friends in there. I want them to, like, they... There's some cool stuff they're working on. And I hope it makes it out there. Yeah. Because, you know, I want to own some of the stuff they're working on.

**Chris Gammell:** Yeah, definitely.

**Dave Jones:** Even if it is the competing VR.

**Chris Gammell:** Yeah. So, what about, like, so, like, you're in charge now, right? I mean, you and Rick are both in charge. But, I mean, you, like, have a company now. Like, are you going to have to, like, be a finance person, too? Or what's the... I mean, is that kind of... You get to hand that off to someone?

**Jerry Ellsworth:** Um, so Rick is officially the treasurer and vice president. I am Madam President. Oh. And what else... She's the boss. We had to divide the stuff up.

**Jerry Ellsworth:** So, it's like... No, it's really small. It's... Yeah, for now. It's actually really fun. There's, like, five of us working on it pretty much full time. And it feels very much family-like. It's all in Rick's living room. He has this big, like, family living room. That's awesome. So, day after we were let... Day after we were let go, I grabbed up all of my scopes and my laser cutter. And I... We're like... You know, damn it. We're going to do this thing. I don't care. Yeah.

**Dave Jones:** You stole all the company lab, did you?

**Chris Gammell:** Well, my own stuff. Yeah, right. I was going to say. Rick, do you have room for 80 pinball machines?

**Jerry Ellsworth:** Oh, actually, Rick... So, I had a bunch of pinball machines at Valve. They're all sitting in his entryway right now because that's as far as they made it. Yeah, nice. They're all folded up.

**Chris Gammell:** Oh, no. Oh, they're not active.

**Jerry Ellsworth:** They're not active, sadly. There's no room. So, there's five of us working out of here. So, it's all at Rick's house. The laser cutter's here. I have my little mini lathe. I have to turn a few things to do some of the optics. And we're all just piled in his living room. So, it feels really family-like because, you know, we'll get to be about 7 or 8 o'clock at night. And we'll cook some food. And we'll sit around. We'll watch a... We got a DVD set of Scrubs, the comedy. Nice.

**Chris Gammell:** I love that show. That got me through Korea.

**Jerry Ellsworth:** So, we've been watching a couple of those a night. And it's great. The creativity is awesome because we're just all on top of each other. And we're going to... That was one of the great things about Valve is they encourage people to be very close to each other. Like, artists were close to programmers and electrical engineers near mechanical engineers and stuff. And that's exactly how we're structuring our group. It's like everyone is just right there in the mix. And we hope to continue that forward after funding. We get a real office and staff up more. Yeah.

**Chris Gammell:** Yeah. Yeah. It's interesting how that stuff changes over time.

**Dave Jones:** You pretty much have to devote your life to this, don't you? You can't really just do a, you know, punch in 9 to 5 and... We could, but it would just take forever. It's...

**Jerry Ellsworth:** I used to always say at Valve, we were working... You know, the team was so small there that each of us were doing the work of five engineers. And it's still the same outside in our group. It's like Rick is doing amazing stuff with the software. I can't believe how much software he churns out, but it's taking him 16 to 18 hours a day to do it. It's all temporary, though. It's like we know that there's the end goal here of Kickstarter. And after that, then we can get real staff and, you know, we can ease the load up. Maybe we can do some 9 to 5s every once in a while.

**Chris Gammell:** Yeah. Or take a day off. You just had a day off, right? Or take a day off well better.

**Jerry Ellsworth:** I did. I took all weekend off. It felt weird. Yeah. So the first day, I'm like, oh, this is so awesome. I just slept eight hours. And then by Saturday, I was like...

**Chris Gammell:** I'm bored. I had to grab my laptop. Yeah.

**Jerry Ellsworth:** And I started working on some of the RTL. Yeah. And then by Sunday, I'm like, well, we agreed that we wouldn't work on it, so I can't go over to Rick's. And I've done everything I can on my laptop. And I was getting pretty antsy.

**Dave Jones:** So I'm glad to be back today.

**Chris Gammell:** That's good.

**Dave Jones:** Because time off is more important than just doing a continuous 9 to 5. Because anyone who's developing, any engineer who's developing something knows that if you just go, oh, I've got to stop now, when you're on a roll.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? You can miss some good stuff. Like, oh, I've got to stop and go home now. You just, oh, then you've got to reset yourself for the next day or the next week. And it takes you, you know, ages to get back into it.

**Jerry Ellsworth:** Exactly. But this is such a fun space. It's so fun to come in and try these experiments as far as user interface. It's like sometimes we just put LEDs on a box and we use that for a prop and we move it around the surface. And it's like, oh, my God, look at these lemmings. They're getting crushed by a box. Oh, that sounds really fun. So, yeah, it's super fun and super hard work.

**Chris Gammell:** What about timelines? I mean, are we saying, like, Kickstarter in a month? Three months? What are you thinking?

**Jerry Ellsworth:** We don't know. We really want to make sure that we have our act together. Again, the game experiences. And we want to be damn sure we can hit the price point. Yeah. So we have to actually start doing the dance with vendors right now. You know, the dance of, like, here's our projected volume. Oh, God, I hate that stuff. It's so tedious and annoying.

**Chris Gammell:** Yeah, and they want all the details up front. You're like, I don't know. This might not sell.

**Jerry Ellsworth:** Exactly. So, you know, that's part of my task is to do the vendor dance.

**Dave Jones:** Right. What about a better prototype? Because if you show that sort of prototype on the Kickstarter video, people might go, oh, I don't know. You know? Because you have to show your real prototype. That's part of the Kickstarter rules now. You can't just do that nice 3D video, you know, 3D rendered product thing anymore.

**Jerry Ellsworth:** Yeah, I think we can write on our old prototype for a bit. We have some parts being assembled for the next revision, which is going to be closer to the 60 gram weight prototype. Yep. We're not going to hit the 60 grams in the next one.

**Dave Jones:** No, but it will look more self-contained and more professional, right? Yeah.

**Jerry Ellsworth:** So there's actually, I've got to do a new board layout. Right now, I didn't really try to miniaturize the boards too much. So there were just two-layer boards with a TQFP 144 FPGA on them. So they're just like huge. It's pretty amazing. We jammed them down into the size. So now I've got to do a multi-layer board and put a micro BGA FPGA down there. Hopefully go to, see if I can talk to Lattice or one of these companies that have an FPGA that will run cooler than the Altera one that we've got. Oh, yeah. That was actually an issue. It's that right between your eyes is where the FPGA was sitting. It's a feature, Jerry.

**Chris Gammell:** It's a feature. As you kill zombies, you heat up. That's right. You know, it's like, oh, I can feel their juices splashing. It actually. Something.

**Jerry Ellsworth:** In the lab, it wasn't too bad because we'd turn it on for an hour and we'd turn it off. But when we were at Maker Faire, it was running all day and it was heat soaking for hours. Right. And it wasn't uncomfortably warm, but people, like a lot of people commented on it. So we need to like show that it's not going to run warm at all. Yeah. And really, when we do the shrink down to the metalized Gatorade, it's going to run like way cooler. I know.

**Chris Gammell:** Yeah, it's amazing how much energy you waste on FPGAs, but you just get the flexibility. So it's that much better.

**Jerry Ellsworth:** And it's kind of band-aided together right now. Like all my RTL is just, I was grabbing IP that I generated back in the Commodore 64 joystick days. Nice. Like it has a little 6502 hanging out in there. Yes. And it's got my custom pixel pipeline going in there and like nothing's gated. So like even in the blanking, it's like, I'm happily figuring out where points are, even though there's no data there.

**Chris Gammell:** Yeah. That's awesome.

**Dave Jones:** We have a whole bunch of Reddit questions. I think we answered a lot of these. Yeah, we did. Is there any we haven't answered?

**Chris Gammell:** Some people are asking about the source code. I mean, like, so, you know, I was going to ask about this actually. I mean, you're not, are you going to patent anything or no? Is this kind of too late by this point?

**Dave Jones:** Oh, please don't.

**Jerry Ellsworth:** Please don't. I'm sorry, Dave. I do have some patents. Oh, no.

**Chris Gammell:** No, that's it. We're working on patents.

**Jerry Ellsworth:** No, you evil person. I know. But you know.

**Chris Gammell:** You have to at a certain point, right?

**Jerry Ellsworth:** We have to also look at the value of our company. At some point, VCs might, like, what kind of moat do we have around our tech? And a patent portfolio is part of that.

**Chris Gammell:** Well, you have some of it you get to encapsulate in the ASIC and the FPGA right now, right? I mean, like, there's some of that stuff where it's just, that's just a case of trade secret, right? You're not going to just give all that stuff away anyways. Even, I doubt you're patenting that side of it, right?

**Jerry Ellsworth:** Yeah. Some of the algorithms and stuff that we're working on and some of the optics tricks and stuff, we are trying to protect that stuff.

**Dave Jones:** Right. So it's more technical, not, you know, a patent for, you know, AR glasses with two Pico projectors and, you know. No. No. Well, that's a step in the right direction at least.

**Jerry Ellsworth:** I'm not, I try not to be an evil person most of the time, so. Yeah.

**Dave Jones:** But we're not going open source. No. Okay. Well, you're going open sourcing so far as the protocol, the interface, right? Yeah. We want people to happily use our stuff. But you won't be able to download your VHDL and Verilog code for your Gatorade or something like that.

**Jerry Ellsworth:** No. That would probably put us out of business right away. That's my theory.

**Dave Jones:** And it would be pointless too because, you know, nobody's going to want to, you know, the only person who's going to want to develop, you know, and take that and develop something with it is a competitor. Exactly. Is somebody who wants to put you out of business. Yeah, exactly.

**Chris Gammell:** Right. Until the chip printers come online, then there's really no point. Exactly. Yeah, that's the main thing we should think about. With AR glasses for the interface. Yeah.

**Jerry Ellsworth:** So, but yeah, APIs are going to be open. We want people to develop for it. It's a chicken and egg. If there's no software for it, then why buy the hardware and, you know, vice versa?

**Chris Gammell:** Yeah. Yeah, my Jaguar never had it.

**Dave Jones:** So, do you see your revenue stream coming from the hardware or do you ultimately see, like, license rights or how do you see that? Because there's got to be money coming in from somewhere. How do you see it?

**Jerry Ellsworth:** We see multiple revenue streams. I'm a toy designer. I'd like to work on some of the props and various things that go along with it. Right. Yep. We see selling software and the actual hardware, the glasses themselves. So, there's multiple angles that we can get revenue. Yeah.

**Dave Jones:** Do you, like, sometimes a lot of companies will not make a cent on the hardware. The hardware is basically at cost to enable you to make money on the software and the other. Yeah.

**Chris Gammell:** Or at a loss.

**Dave Jones:** Spin-off effects. In fact, they, yeah, or at a loss. Because that may be required. Because if you find that, ooh, hardware is more expensive than that magic $300 price point, you know, you may have to take a loss on the hardware in order to, or break even in order to make your money elsewhere. Yeah.

**Jerry Ellsworth:** Yeah. I mean, that's one of the things that we were considering when we were under the umbrella of a bigger company that could do that. But it's a little too scary for us to think about that right now. So, I think everything's got to generate a little bit of revenue or at least break us even.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. You wouldn't be selling it at a loss. You would be at minimum breaking even or shooting for a... Yeah.

**Jerry Ellsworth:** Looking at my bank account going down quickly, putting this together. Don't worry.

**Chris Gammell:** You're making it up on volume, Jerry. It's cool. Yeah.

**Jerry Ellsworth:** Like the underwear gnomes. Yeah. There you go.

**Chris Gammell:** It reminds me of the jiken. I think the last question that... I didn't have it written anywhere. I didn't see anyone else write it anywhere. But how do people work for you? Because I know that people are going to ask that. Even if they're software people. Should we set up a Google Docs? Like what people are willing to do to sell their soul to work for... What's the name of the company again? Technical Illusions. No, that's right. Technical Illusions.

**Jerry Ellsworth:** On the Cast AR system. That's right. Yeah. Well, right now we're being very conservative about letting people come work over here. Since it's kind of cramped. Yeah. Folks that are fans and friends have been helping us out here and there. On art and sound and programming. But until we have funding in a real office, it's going to be pretty limited.

**Chris Gammell:** You can pay people in pinball plays right now, right?

**Jerry Ellsworth:** Exactly.

**Chris Gammell:** You get three quarters, but you can keep cycling through the machine. So, you know. Exactly. You can spend that however you want to.

**Jerry Ellsworth:** I'm actually really, really excited about getting our studio up and going.

**Jerry Ellsworth:** Because, you know, this is it. We get to choose, like, all the coolest people that we want to work with. Yeah. And there's not going to be, like, the old guard that's going to come through and mandate things. Like, we get to set the culture right now.

**Chris Gammell:** Well, you're the old guard. That's the best part, right? Yeah, that's it. Yeah, three months old. Yeah, exactly. Whatever. Senior. You can start hazing people.

**Jerry Ellsworth:** Back when I had my computer stores, that was one of my favorite times in my career. So, I had my computer stores. I had some employees working with me. We felt, it feels, this feels a whole lot like that. But, family, you know, we sometimes squabble a little bit here and there when the things get tense. But, you know, we're all really, we like each other. We have good personalities. That's good. If I don't say so myself.

**Dave Jones:** On Reddit, George Hahn has a question which we have pretty much covered. But I think there's an interesting angle to it. He's curious about the ASIC. How much functionality do you decide to put into the ASIC? Because the FPGAs have that refilled, reprogrammable, reconfigurability. So, I know it's a trade-off against power and, you know, cost and everything else. But with that ASIC, you do lose that flexibility. How are you treating that? Are you just going to go, right, we're going to put these features in and that's it. Too bad. Can't do anything else in the future. We'd have to spin a new ASIC.

**Jerry Ellsworth:** Exactly. So, for the ASIC, we want to add as much flexibility as possible. That's why we have that little 6502 hanging out in there that does a bunch of stuff in the blanking period. That way we don't hard code anything. So, we try to offload any kind of, like, low.

**Dave Jones:** Right. Low speed stuff on it. So, it's actually a processor. So, it's actually all processor-driven in there, essentially. Is that what you're saying?

**Jerry Ellsworth:** Well, all the state is driven by a processor. It's actually a pixel pipeline that's doing all the detection. So, that's actually a little scary. You know, if we design this thing and a year down the road, we decide, well, geez, if we only had changed this one parameter. Exactly. That's the trap, isn't it? It is. That's every ASIC that you design. And you have to kind of try to figure out what's going to be completely flexible. And going completely flexible, usually the trade-off is it's slower performance. Mm-hmm. And what's going to be hard-coded.

**Dave Jones:** So, you absolutely cannot do this project without a gate array ASIC. Is there no avenue to do it with some low-power FPGA or something like that? Man, cost. We could do it with an FPGA, but it's cost. Well, yeah, but, you know, it's cost. But it depends on how big. I mean, you can get, you know, a dollar FPGAs, but you can't pull that in them. Yeah, no, you can't do video.

**Jerry Ellsworth:** Yeah, that's the unfortunate part is unless Altera or Xilinx, hint, hint, hint, wants to get this design win and gives us a competitive price to persuade us not to go down the route of the metalized gate array, then I don't think there's much option to hit our price point. I mean, we could add $100. So, it's just price.

**Dave Jones:** Yeah.

**Chris Gammell:** It's just price. I've never heard of a ride like that. We could add $100 retail. That would be a crazy win for an FPGA. You know, like, it's just, I've never heard anything like that. Maybe volume, but that's just not their market. I've tried.

**Dave Jones:** Maybe they can sponsor it. It can become the Altera cast AI glasses. Yeah. You know?

**Jerry Ellsworth:** I sell naming rights. No way, man. Well, you know, I tried that with the toys. Yeah. We were doing all these metalized gate arrays and, you know, I went to the, like, Altera and Xilinx and said, hey, you know, you have hard copy for these really big FPGAs. You know, you're like $1,000 FPGAs down to like $100 hard copy version of it. Yeah. Would you ever consider doing, like, a Cyclone hard copy? You know, go from $15 down to a buck. Nope. And they pretty much just, like, get out of here, kid. Yeah, right. You're wasting our time. That's chomp chine shit.

**Chris Gammell:** Not the market, man. They're making good money like that.

**Jerry Ellsworth:** Unless something's changed, they're not interested. And that's where Atmel and ChipX and eASIC and some of these other companies step in and-

**Chris Gammell:** Make it up on volume.

**Jerry Ellsworth:** Yeah. I mean, it seems pretty lucrative to me. They made quite a revenue off of us in toys.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** You know, they're making money on the masks and having us sit there. And then they're making money on the per part.

**Chris Gammell:** Yeah. That's interesting business. I think you could- We could probably talk to you about that just for another five hours. Just because-

**Dave Jones:** Yeah.

**Jerry Ellsworth:** I really wish there was something in between. Like, there- As a designer, I would love to have something between Metal Eyes Gatorade and FPGA. Something that would bridge the gap. Like, I could foresee getting rid of the $20 FPGA and putting a $8 part in there.

**Dave Jones:** So, what is your price target for your ASIC? I mean, like, can you get away with a $20 part? Or is it a, you know, or it has to be sub $10 or $5? Yeah, we're looking for less than $5 on the ASICs.

**Jerry Ellsworth:** Wow.

**Dave Jones:** Okay. Yeah, that's pretty restrictive, isn't it? Yeah.

**Jerry Ellsworth:** Especially at that sort of volume. So, we're going to eliminate $30 to $40 worth of electronics on the headset just by- Right. ... doing this, which will be huge as far as the-

**Dave Jones:** getting the cost down. So, the electronics is a large cost component of the final product. It's not the screen. It's not the plastics to get the molded glasses. It's not the Pico projectors. It's- Oh, for- Well, it all adds up, obviously.

**Jerry Ellsworth:** It all adds up. You know, nickels and dimes you to death. Mm-hmm. Yeah, by far the most expensive thing in the whole design is the micro displays. Mm-hmm. Right. So, we're still doing the dance on those.

**Chris Gammell:** Yeah.

**Dave Jones:** Mm-hmm.

**Chris Gammell:** We'll sell a million, maybe. We'd like to. Over 10 years.

**Jerry Ellsworth:** If you give us the right price now, we can sell a million.

**Dave Jones:** Exactly. If you give us the wrong price, no. Engineers have a hard time lying when it comes to- I know. ... stuff like that to vendors, don't we? We're just too honest for our own bloody good. Yeah, you need to put in salesperson.

**Jerry Ellsworth:** Yeah, I'm always in trouble because of that. I'm- Yep. I'm a very candid person, and I'm sure Rick's going to listen to this podcast, and he's going to be like, you said what to them? We're sorry, Rick. And you're talking about our actual costs? Yeah. Oh, my God.

**Chris Gammell:** She's the president. She's allowed to. You said you're president, right?

**Dave Jones:** Well, any experienced hardware person can guess your costs anyway to within a reasonable margin, I mean, you know.

**Jerry Ellsworth:** Yeah, folks that are- It's not hard. Been around the block a few times, right? Exactly. Yeah. If we're going to do sub $200, you can guess exactly what the glass is-

**Dave Jones:** Yeah, I can guess that you need a sub $10 processor, you know? I mean, it's not hard. Yeah. Yeah.

**Chris Gammell:** And plus Dave will do a teardown anyways once he gets one, so. There's just one blob of epoxy under here.

**Jerry Ellsworth:** Exactly. Damn you, Jerry. Yeah, I know. It's not that exciting.

**Chris Gammell:** That'll be fun.

**Dave Jones:** What about, like, tooling for glasses and stuff like that for the plastic? Like, you know, how are you going to do these, you know, the $10,000 for the Kickstarter? Maltz have gotten cheaper, man.

**Chris Gammell:** They've gotten cheaper lately.

**Jerry Ellsworth:** Okay. So, we think we've got it figured out to what we're going to do as far as the sub-assembly, because there's some, it needs to be dimensionally stable, you know, micro displays versus the camera. Oh, yeah. So, that'll be a bit of a floating assembly, and the glasses themselves will be kind of decoupled from that. Oh, okay. You can't be bending the relationship.

**Dave Jones:** Is that critical due to the nature of the tracking?

**Jerry Ellsworth:** Yeah.

**Dave Jones:** So, you can't have the projectors moving around. So, you can't have the plastic expand. So, you can't have the plastic expand when you put it on your head and it heats up and all that sort of jazz.

**Jerry Ellsworth:** We can tolerate a bit of that, but we can't tolerate, you know, someone putting it over the top of their snow cap or something and bending the arms out and having the two projectors angle in or something. Ah, got it. Yeah. Now, without a weird effect. So, that's some of the challenges we're going to have to work through. Yeah.

**Dave Jones:** Is there any, like, self-calibration? Is there, like, do you, the first time you use it, do you calibrate? Is it factory calibrated once and that's it? Or each individual, or do they even need calibration? Or is it, like, so dimensionally stable that you don't have to bother?

**Jerry Ellsworth:** There is a calibration process that we go through here, but that's because we hot glue all of them together. Yeah, yeah, exactly. Yeah.

**Dave Jones:** But in the final production, do you envisage that there's going to be a calibration step in either manufacturing or by the user?

**Jerry Ellsworth:** No. No, we don't expect that to be the case. We expect to manufacture them with tolerance and then that tolerance should be within.

**Dave Jones:** Right. It should be good enough. Yeah.

**Jerry Ellsworth:** Yeah. Yeah. You don't have to be accurate within, like, one pixel accuracy with your magic wand that you're poking at things. But if you get off by 10 pixels, that's pretty bad. You notice that. As far as tooling, I imagine what we're going to do is soft tooling. We'll do aluminum inserts for the plastics. And since if we go the Kickstarter route, it's going to be pretty low volume, so we can just, you know, shoot out of an aluminum tool and it'll wear out pretty quick.

**Chris Gammell:** Yeah. Yeah. Then you cut steel later. That's when the fun begins.

**Dave Jones:** Are you going to have to bring on, like, an industrial designer to do all the, you know, 3D caddy?

**Jerry Ellsworth:** Absolutely. That's one area that we don't have a mechanical engineer yet. Most of the work has been left over from Valve. Like, some of the frames and stuff came from our mechanical engineer who was also let go at the same time. Well, just steel your mechanical engineer from Valve. He was let go also, unfortunately. It was kind of a bummer. But he went off and got another job before we got our feet under us again.

**Dave Jones:** Is there now a clause that you can't – this often happens when you leave a company. There's a no poaching clause that they make you sign. Or it's in your original agreement or something like that.

**Jerry Ellsworth:** Yeah, I didn't sign anything.

**Chris Gammell:** That doesn't work in some states, though, too. Like, California, that actually doesn't work. Oh, okay. So you can't – Oh, okay. They can't be enforced, apparently. Right. Interesting. I've been told. There you go. That's fun, though, like, doing that kind of mechanical stuff. Like, I mean, you've done mechanical stuff before, Jerry, right? I mean, like, you do machining.

**Jerry Ellsworth:** I have a good idea of what we – yeah, I'll be able to talk to our mechanical engineer. Yeah. And be able to relay what I'm imagining. Yeah. I think they'll –

**Dave Jones:** But not do the grunt work.

**Jerry Ellsworth:** Yeah. It's better to have someone run the tool that actually knows it. So Tara, our graphics person and animator, also has a background in industrial design, which is quite different than mechanical design. So she's actually working on concepts of what the classes might look like, and then she'll work closely with our mechanical engineer once they come on board to do the actual engineering and choice of materials. Like, it's going to take a little bit of research to figure out what the right plastics – you know, is it going to be a liquid crystal polymer? Is it going to be some kind of nylon? Yeah. You know, it's got to be rigid enough that when you – some kid, like, bends the arms out or something. Yeah.

**Dave Jones:** And herein lies the problem. You can't get that person unless you get funding. And you can't get funding unless you do your Kickstarter campaign, unless you get funding from somewhere else. And then – but then in your Kickstarter campaign, you've got to put a deadline to when you're going to deliver this stuff. So you haven't even made those decisions yet. It's – you know, that's why it's sort of like, you know, 80% of Kickstarter campaigns are late.

**Jerry Ellsworth:** Yeah. It's – you get going, you find out it's difficult. Like, it takes a long time to – We hope that we can have a lot of our team lined up, but we're going to have to – like, as soon as we get Kickstarter funding, we're going to have to hit the ground running and start recruiting like mad because, you know, people aren't going to want to wait a long time for these glasses. So we're going to have to be aggressive and come up with some schedule that people will be happy with. Yeah. So that means we've got to get people working on this immediately after we get funding.

**Dave Jones:** Yeah. That's right. But ultimately, unfortunately, for a complex hardware project like this, you essentially have to sell a promise. Like, you've got your prototype and everything else, but there's a lot of steps to actually deliver a final product.

**Jerry Ellsworth:** Well, luckily, this isn't my first time to the rodeo, so – No, no, of course. We can at least – we can at least be close to a ship date. Yeah. Or if not, hit it right on since we've – Rick has a background in shipping games. I have a background in shipping consumer products and designing them. So within a few weeks, we should be able to – I mean, within a few weeks of our deadline, we believe we can hit it.

**Chris Gammell:** Yeah. And plus, if you don't – what, is the president going to fire you or something? I mean, come on, right? That's right. Yeah.

**Jerry Ellsworth:** I definitely don't want to be in the situation where I'm months and months overdue. I saw some of these kickstarters and how upset people get when – Oh, yeah. Very.

**Chris Gammell:** Yeah. It's better to be realistic than optimistic.

**Dave Jones:** And if you don't update them either, if you don't keep them constantly updated, then they get nervous. And then all the rumors start that, oh, you've done a runner and all the rest of it.

**Jerry Ellsworth:** I hope – I think everyone else is on board around here that we're going to be very open about what's going on because it's to our benefit. Like, here it is. This is the facts. This is what's going on. These are our costs. This is – Yep.

**Chris Gammell:** Yeah. And it'll be educational too.

**Dave Jones:** I don't know why everyone does – I don't know why everyone who runs a Kickstarter campaign doesn't do that. Unless you're actually running a con, you know, why wouldn't you be 100% open all the time? I don't understand that at all. Why would you – you know, if you know you're not going to be able to, you know, hit your target, just say something.

**Chris Gammell:** Because you don't know yourself, right, if you don't know what's going to happen next. Jerry has the experience, right, with the hardware and Rick has the experience with software. But if you're just kind of grasping at straws, like, oh, I guess we'll ship it next. No, you'll design plastics next, you know, like that kind of thing. Yeah, yeah, yeah.

**Jerry Ellsworth:** Yeah, I don't envy some of these people that are struggling with that for the first time.

**Dave Jones:** Because it's too easy to take people's money with an idea, right? You sell an idea on Kickstarter and you take people's money and then, you know, you go, oh, okay, yeah, I can – I'll just get somebody to do it all for me. I pay someone to do it all for me and, you know, it all falls in a heap. And, yeah, when you don't know what you're doing. So, yeah. Unfortunately, you guys do, which is good. So – Yes.

**Jerry Ellsworth:** Excellent. We're excited. This is – I can't wait until you guys get to actually put the glasses on because – Oh, yeah, you're making a trip to Australia, are you? Oh, maybe. There was a conference. I'm trying – I can't remember the name of it right now, but they were pestering me to come out. I don't know if I'll actually do it.

**Dave Jones:** Well, if you can get a first-class ticket out of them. There we go. It's only a 15-hour flight. Lots of time to write code, so.

**Chris Gammell:** There we go.

**Dave Jones:** I'll have my FPGA sitting there on the –

**Chris Gammell:** Yeah, your programmer on your lap, right?

**Dave Jones:** And good luck getting that through, you know, airport security. You know, you bring in all this rough-and-ready hardware onto the plane. You know, all this hacked together, improvised electronic device. Hey, you guys would probably like this story.

**Jerry Ellsworth:** Do tell. All right. So, it was back when I was doing a toy design, and it was before they had all these power outlets on the plane, so you didn't get power on the plane. And I was doing this cross-country flight that was going to be like five hours, and I had to get some of this stuff done. So, I went out and got a battery backup UPS. Oh, God. And it has a little beeper speaker in there. Yeah. I opened it up, and I crunched the speaker out so that it wasn't one beep. Yeah. And I went through airport security with this UPS in my bag. Oh, God. And they stopped me, of course.

**Chris Gammell:** Well, because it looks like a bomb, right? I mean, like, it's a big chemical chamber.

**Jerry Ellsworth:** Yeah, they look at this thing. It's a lead-acid battery, and it weighs, like, 10 pounds. Yeah. And they're like, we can't x-ray through something in your bag. Can we take a look at your bag? So, they pull this thing out, and they're like, what's this? And I go, oh, that's just a surge protector. And they're like, it's warm. I go, oh. I go, it was plugged in before I came here.

**Chris Gammell:** Yeah, you know designers these days. They can't do anything right.

**Jerry Ellsworth:** So, I get to my gate. I plug the UPS in. And to get this thing going before I got on the plane, you couldn't just start the thing without it being plugged in. So, I had to plug it into an outlet.

**Chris Gammell:** It's got a pull cord. And carry it on all powered up.

**Jerry Ellsworth:** Yeah, get the power switch on, you know, tape the power switch so it couldn't get bumped, and then pull the plug. And I ran off this UPS for, like, two hours, so I got an additional, like, two hours plus what my laptop had.

**Chris Gammell:** Oh, nice.

**Jerry Ellsworth:** What do you think? Genius or what?

**Chris Gammell:** Genius because you got away with it. No, you got away with it. That's how it works. That's really good.

**Dave Jones:** Was this pre or post 9-11? Post.

**Chris Gammell:** Yeah.

**Dave Jones:** Right, okay. I'm surprised then.

**Chris Gammell:** Hey, man, when you need power, you need power. So, that was very ingenuitive or whatever the word is.

**Jerry Ellsworth:** Another post 9-11 thing that I did that was probably not very smart is I had an old cell phone, one of these flip phones. And somehow I managed to plug the wrong charger into it and blew up the charging circuit. So, I put two alligator clips soldered to the battery and drilled a hole through the case. And I would just hook it to my bench supply and put a little charge on it. Yeah, trickle charge. Yeah. Yeah. Trickle charge my lithium battery in the thing. So, I went through security with this thing. And I went through a couple times and they never really looked at it. Oh, my God. One time they, like, saw the alligator clips and they freaked. They're like, oh, my, what is this? And I had to dismantle it for them.

**Chris Gammell:** Yeah.

**Jerry Ellsworth:** I'm like, really, it's a cell phone. Look, it's just hooked to the battery. I'm an electrical engineer. Trust me. Let me go.

**Chris Gammell:** And it works. Yep. Yep.

**Jerry Ellsworth:** You just have to have conviction. Exactly. You're just like. Confidence. Yeah, yeah, yeah.

**Chris Gammell:** It's all in the swagger.

**Speaker ?:** Yeah.

**Dave Jones:** It's all in the delivery. Oh, brilliant. This is now our official longest.

**Chris Gammell:** Way longer. Yeah.

**Dave Jones:** Episode ever. Oh. We blew two hours. Two hours. I'm sorry about that, guys.

**Chris Gammell:** No, this is, I guarantee.

**Dave Jones:** That means two hours of work you didn't get done. The project's not going to happen now. Oh, God. I got to get out of here. We've got a Kickstarter to do.

**Jerry Ellsworth:** Yep.

**Chris Gammell:** Well, you have the site now, right? You have the.

**Jerry Ellsworth:** So, it's technicalillusions.com.

**Chris Gammell:** Okay.

**Jerry Ellsworth:** And we're going to do blogs. Oh, good. There. And we're going to YouTube videos. Any live feeds?

**Chris Gammell:** Oh, yeah. Any live? The old school. I don't know.

**Jerry Ellsworth:** That would be interesting.

**Chris Gammell:** You can get the.

**Jerry Ellsworth:** I haven't done a live feed in a long time.

**Chris Gammell:** The chat to speech thing going out again, right?

**Dave Jones:** Oh, right. With my computerized voice jumping in.

**Chris Gammell:** Yeah, there you go.

**Dave Jones:** That's bullshit. That's awesome. I miss those days. Sorry, that's an in joke for anyone who's seen Jerry's old live shows. Yeah.

**Jerry Ellsworth:** We had sound bits from Dave. And then the IRC chat room internet could choose words to say in phrases. Utter rubbish.

**Dave Jones:** Yep. What a bunch of dickheads.

**Jerry Ellsworth:** Well, before we go, I feel like I might have been a little bit too hard on Valve. I should at least say that there's really not. I mean, I'm disappointed that I'm not at Valve.

**Dave Jones:** That you got the ass. Yeah.

**Jerry Ellsworth:** Yeah. But, you know, a lot of my friends are there and I wish them the best of luck. And if they're listening, you know, love you guys. Can't wait to see what you guys come out with.

**Dave Jones:** And they gave you the technology. They did.

**Jerry Ellsworth:** It's so awesome.

**Dave Jones:** They actually allowed you to keep the prototypes and everything. So the prototypes are Valve. Yep. We walked. Prototypes, aren't they?

**Jerry Ellsworth:** We walked in a week later after getting a verbal agreement. We walked out with the contents of our lab. I mean, they just let us take everything.

**Dave Jones:** Wow. Except the equipment.

**Jerry Ellsworth:** Yeah. I couldn't keep my $30,000 scope. Oh. Oh.

**Dave Jones:** I know.

**Jerry Ellsworth:** Now I'm back to, it's really, it's terrible. I'm working with this old, like, 100 megahertz scope that everything looks like DC. I'm working on these gigahertz serializers and it's, I don't even bother pulling the scope out because it would just be like a DC bias.

**Chris Gammell:** Yeah. I'll just check that one bit to see if it fired or not. Wow. That's horrific. Well, thanks for being on the show, Jerry. We really look forward to seeing what's next.

**Jerry Ellsworth:** Yeah. Well.

**Chris Gammell:** Keep tabs on you.

**Jerry Ellsworth:** When we get closer.

**Chris Gammell:** And we'll, you know, we'll throw guests your way too. Once we have them on the show, we'll send them your way to, you can hire them.

**Jerry Ellsworth:** Yeah. There we go. Yeah.

**Chris Gammell:** We will be the recruiting arm of technical illusions. Just like we were. Just for the valve hardware.

**Dave Jones:** Awesome. Awesome. Thanks, Jerry. It's great. I'm sure a lot of people are going to really appreciate this episode. Thanks, guys.

**Chris Gammell:** All right. We'll talk to you soon.

**Dave Jones:** Now get back to work.

**Chris Gammell:** This episode of the Amp Hour was brought to you by Element 14. The beginning of every good project, like Jerry's, is held together by duct tape and hot glue. But there is also usually a dev board underneath, powering that new idea. To learn all about the latest kits, discuss them with others, and quickly purchase them at competitive prices, check out element14.com. We'll see you soon.
