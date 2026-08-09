---
episode: 609
title: Open Circuits with Eric Schlaepfer and Windell Oskay
url: https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released November 13th, 2022. Episode 609. Open circuits with Eric Schlepfer and Wendell Aske. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Wendell Aske:** Hi, I'm Wendell Aske. I'm the co-founder of EvilMed Scientist Laboratories, and my background is in atomic physics, and now I make pen plotters. Recently co-wrote with Eric Schlepfer the book Open Circuits.

**Eric Schlepfer:** Hi, I'm Eric Schlepfer. I'm also known as TubeTime on Twitter, and I co-authored the book with Wendell.

**Chris Gammell:** All right, welcome, guys. I'm very excited to talk about this book. We've been talking about it on the show many times. We finally got some copies. Thank you for that, you know, pitching those our way. And boy, oh boy, I'm going to say this many times throughout the show. This is a gorgeous book and lots of beautiful, beautiful photos. So thank you for making this. Yeah, it's already a joy just peeking through it. So yeah, I mean, so Wendell kind of got into some of his background, but let's get a quick background on both of you. So Wendell, you were at NIST, if I remember correctly. Is that right?

**Wendell Aske:** Yeah, I did a postdoc at NIST after grad school, and I spent three years there working on atomic clocks. I actually worked on a single ion optical clock where I trapped a single mercury ion. We probed it and made some very precise time measurements. Oh, that's cool. Worked on some of the most precise lasers in the world and got to learn a lot of stuff.

**Chris Gammell:** Very cool. Very cool. And obviously, Evil Mad Scientist is, we've talked about your blog many times in the show before and all of the various projects you make. Is it emsl.org? Is that right? It's actually evilmadscientist.com, a very long domain name. Got it, got it. Okay, well, it's available. That's great. Yeah, yeah, yeah. Okay, well, we'll poke through there too as well, and we can kind of refer back to things.

**Eric Schlepfer:** Eric, what about you? What's your background? I've been involved in electronics for a really long time. There's actually 8mm film footage of me as a 4-year-old making a complete circuit with a battery and a light bulb and some wire. And I actually got into software for a little bit, ended up getting a degree in electrical engineering, and then pursued a career in the semiconductor industry for a while, and eventually wound up at one of the big tech companies doing hardware design.

**Chris Gammell:** Cool, cool. You know, if you have hipster parents, you could still make a 4-8mm film of completing a circuit in modern day. Oh, this was non-ironic 8mm film. It's just because of what was there.

**Eric Schlepfer:** Yeah, exactly.

**Wendell Aske:** Nowadays, Eric makes open circuits.

**Chris Gammell:** Yeah. Are you doing like the open silicon stuff or something else?

**Eric Schlepfer:** No, what I typically do is design things like clones of old retro sound cards or other things that people like to use in retro computing. And I tend to release those as open source hardware. I've always felt that my time is better spent doing things that I enjoy, like designing circuits, rather than managing sales and shipping and all the rest of the things that go with trying to sell hardware. And so the idea behind open source circuits, at least for me, is that I can do the stuff that I enjoy and then allow other people to get those designs for free and use them however they want. So they can go and manufacture their own boards and sell them to their friends, or they could go on eBay and sell them that way. That's great.

**Chris Gammell:** Yeah. Wendell talked about really precise time and measuring really precise time. And it was about precisely 20 seconds for me to get that he was actually talking. That was a callback to the book name. And yeah, so that was a good one, Wendell. Sorry. It's a little late here. I'm a little, you know, it's been a long day here.

**Wendell Aske:** We both do a lot of open source stuff as well. So perfectly fine call out.

**Chris Gammell:** Yeah. Okay. That's cool. Yeah. And so you guys, I remember one of the things, I remember seeing you've been collaborating for a while, but one of them was the, was it open moss? What was that, that huge circuit board?

**Eric Schlepfer:** Well, there was, there was one before that, actually two before that, that we should probably mention first. Sure. Yeah. Let's get them all in here. Yeah. That was the collaboration on the three fives, discrete five, five, five timer kit, which is a real product that you can buy at a MSL.

**Wendell Aske:** I do the, I do the selling of the hardware, which is this terrible thing that Eric was describing. It is indeed terrible. Yeah, exactly.

**Eric Schlepfer:** And I really appreciate the hard work. I hate my UPS guy.

**Wendell Aske:** No, we love the UPS guy. I know. I know. The courier is like, they make business possible. I'm so happy with them. It's true. It's true.

**Eric Schlepfer:** Yeah, exactly. And it's, it turns out, so the five, five, five timer is not a very complicated circuit internally. And even when I was younger, you could open up a data book and they would actually show you what the internal schematic was. They would show you all the transistors. And I always thought it'd be fun to try and actually build one out of transistors to see if it would work. And I did. In fact, that prototype is on display also at MSL. So I think Wendell, you have that in your cabinet. Yep. And then we decided to turn that into a kit. And so you can go and buy this kit. It comes with all the components you need and solder together your own five, five, five timer. Yeah.

**Chris Gammell:** I believe we featured this when it first came out as well. Cause I remember specifically the screw terminal, like things that made the bent metal legs go on, or I don't know if they're even metal, if they're plastic or metal, what is the material there?

**Wendell Aske:** The first, first version of the kit, we actually had a formed PVC foam legs and they were gray. And then we revised the kit a year or so later with aluminum sheet metal formed legs that really just looked the part so perfectly.

**Chris Gammell:** Yeah. They look really good. Yeah. And just to describe it for people, I mean, so it's a black circuit board, but it's definitely like a blown up version. And you've got all the N channel and P channel FETs or sorry. Yeah.

**Wendell Aske:** So the original prototype that Eric made is this gorgeous piece of circuit artwork. There's no circuit board per se. There is literally a wooden board with little terminals hammered into it. And the individual transistors and resistors are soldered to these little hammered in terminals and this little banana plug jacks on the sides. So it's this wonderful piece of wooden artwork. And the, the genesis of this kit actually was that I had brought a, a giant wooden 555 model that I had made out of wood, CNC routed wood. And he had brought this model. We sat the two things next to each other. These two gigantic inflated 555s, one physical, one electric. And we realized, you know, we should do this thing, right? So we. And the, the one you made, the, the wood one was, that was a footstool. Is that when I remember? That's right. It's just a footstool, a piece of silly giant furniture. So we collaborated on designing a circuit board that would be the right shape to visually look like a dip chip 555. And, uh, I ended up giving Eric a, uh, outline said, make it look like this. And he designed the circuit and made it work there. And we designed a kit around it so that you can solder it yourself. And it's easy and fun to build.

**Eric Schlepfer:** Yeah. I think there's a photo of that prototype around somewhere, maybe on, uh, MSL. I forget if we took a picture of it for the, uh, for the website, you could certainly find it on Twitter. If, if you search around my Twitter account, uh, for those listening, it actually looks a lot like the circuit art that Jim Williams used to construct back in the day.

**Chris Gammell:** Yeah.

**Eric Schlepfer:** That's great.

**Chris Gammell:** That's great. And it, like, uh, you said there was like nails on the board as well. Like a, like a true, the, the term breadboard came from that space, right? Where it was actually like a piece of wood people were cutting bread on and then they hammered nails into it, that sort of thing, right?

**Eric Schlepfer:** Uh, yeah. Little, little terminals. So, uh, with a little ceramic base and a cute little terminal on it, you know, it's art basically.

**Chris Gammell:** Yeah, that's great. That's, that's cool. That's still around too. That's, that's a good, uh,

**Eric Schlepfer:** good showpiece to have in the cabinet. So that was the thing that kind of started it all. And, uh, naturally we started thinking about some other chips that are very well known and well loved by the community. And, and kind of the other obvious choice was the seven 41. Because that's the op amp that everybody gets started with. And it turns out that's not very complicated either. You know, again, it's maybe two dozen transistors and that's it. And, uh, so that was kind of our next collaboration. It fits very neatly in the series. And, uh, then of course we decided to build a surface mount version so that people could use that as a way to practice surface mount soldering. And naturally we also had to change the legs so that instead of looking like those, uh, through hole dip pins, there are those little gallwing surface mount leads on it. So it, it, it definitely looks the part.

**Chris Gammell:** That's great.

**Wendell Aske:** So we've made both of these in SOAC packages, so to speak, that are matched exactly in scale to the dip counterparts with half the lead spacing and so forth. And they have these little tiny screw terminals you can use to attach your wires to them.

**Chris Gammell:** Oh yeah. Cause they're actually operational. Of course. Oh yeah. That's great. That's great. Yeah. And I mean the fact that it is surface mount, uh, you could practice as well. That's, that's really cool. Have you seen them being used, uh, kind of out in the world as like, uh, educational pieces or just kind of show pieces where, where do you see them actually being used?

**Wendell Aske:** We do actually see quite a lot of sales to community colleges where people are getting a whole set of them. We've also seen classes where it was obvious that, uh, somebody told all of their students to buy one. Cause we suddenly got, you know, 40 orders from San Diego. Uh huh. Yeah. To individuals. So. Right. There's definitely some use of it. It's not that every college is using it, but there certainly are a few out there. Yeah.

**Eric Schlepfer:** One of the nice things about the kid is that it makes it possible to make modifications to the circuit and to hook an oscilloscope to internal nodes and kind of explore just how the chip actually works, which is really neat.

**Chris Gammell:** Yep. Yep. This, yeah, it's, it's railing because of the bad setup that I did on the outside, but now we can see what happens on the inside. Exactly.

**Wendell Aske:** Yeah. And if your setup from the outside is bad enough to blow out a transistor while you can go in and fix it.

**Chris Gammell:** That's true. Yeah. That's nice too. I didn't thought about that. And it's, I mean, it's crazy just to, I mean, even just to have that conversation with someone, you know, I, I remember the first time I used an op amp for, well, the first time I saw an op amp was on a page as a triangle, right? That's probably the most confusing way to get introduced to one. But like, but then you actually see it and you're like, Oh, okay. It's like a real thing that doesn't, it's not very triangular. I don't know where that came from, but I get it now. There's a thing here, but then it just, yeah. I mean, the actual telling me that it's full of transistors and there's all this stuff here, you know, it's, it's, I feel like it's presented in such an abstract way that to, to get down into the actual fact that there's transistors, you know, operating there is, is very important from a kind of piecing altogether.

**Eric Schlepfer:** Yeah, definitely. If anything, when they start teaching it, they typically start with the ideal op amp, which isn't really the best place to start. So it is a model, but it's a little bit of a confusing model. Yeah. So if you start with the model where you're just simply taking the difference between the two input voltages and then multiplying that by a gain, that's way easier to understand. Yeah, I agree.

**Chris Gammell:** I agree. I think, I think it's done because the professors want to be able to teach math and KVL, KCL right away, that sort of thing. I think it's used in that, in the purpose for that. And yeah, it's, it's, it's, it's a rough introduction. I, you know, I went on to work with top amps a lot later and I was like, oh my God, three years later. I'm like, yeah, yeah. I started to get this done.

**Eric Schlepfer:** Yeah. You can definitely get into trouble with ideal op amps. Uh, it's a joke. One time I put together a fake data sheet for an ideal op amp and, uh, spread that around on Twitter for a while, but it's one of those things where you, you read all the specifications and you just realize how horribly contrived the ideal op amp is and just all the different unrealistic properties of it.

**Wendell Aske:** I had a college class where, uh, the professor told us to measure 20 properties of an op amp, which included, you know, input offset voltage and all those things. And didn't give us any clue what those things meant or how to measure them. And it was just sort of the most horrible days of my life and, uh, learning how to do electronics.

**Chris Gammell:** Yeah. That's, that's rough too, because it's, it's like, uh, you know, it's something that really matters quite a bit, but it's just without context there. Like, you know, like where do you, where do you even start? You know?

**Wendell Aske:** And that was the first day that Horwitz and Hill saved my life.

**Chris Gammell:** Yeah. There you go. There's the, there's the, there's the title of the episode right there. That's great. Yeah. Well, I was thinking about the, is it open Moss? Is that the name of the big processor thing? You're thinking of the monster 6502. Monster. That's it. I was thinking about that recently because the super con badge had the similar kind of like light up blinky nature with all of the processing with all the, uh, you know, the various stages of a processor passing through it. That was a four bit computer that at the, on the super con badge, what was the monster 6502?

**Eric Schlepfer:** Yeah. So that was, that was a really interesting project. It, it kind of started out oddly enough with the 555 timer kit. And Wendell, you could probably fill me in on the details because it's a little fuzzy for me, but there was an event. I think it was either a bring a hack dinner or a, a maker fair after party type of event. And, uh, we're,

**Wendell Aske:** it was the, uh, after party at BJ's after maker fair bunny was there. He was having a good night.

**Eric Schlepfer:** And that was the one that Jerry Ellsworth had set up. Yeah. I remember that. Yeah.

**Chris Gammell:** Yeah. Yeah. Do you know, that is actually the basis that is that specific event. that was the basis for starting supercon because really yeah well so like you know so i was working at supply firm at the time and and got to hang out with all the hackaday folks and like we would all go to that event which was after maker fair and we were so it was like sophie and myself and alec our boss and mike stish and like and we all were like sitting on matt bergman as well and we were all sitting around and we're like you know all i really care about is that party after after maker fair what if an entire conference was that party after maker fair and that's like literally that is the thesis statement for supercon ha and it i think it delivers honestly it was a that's all yeah that's why i just want that every day of the year right every meetup i do every conference i go to i want it to be that experience at you know bj's after after maker fair that was yeah exactly the

**Eric Schlepfer:** basis it was just fantastic and there was just so many uh so many smart and creative people and so much communication going on lots of ideas and things like that floating around and so we we had this little thing with us and uh somebody came up and made a not really a sarcastic comment but like a you know a little bit like a challenge like oh that's cool but could you do an entire

**Chris Gammell:** processor that way oh man you don't remember who it was or you do it was bunny was it bunny it was

**Wendell Aske:** bunny oh man of course he was uh he was uh off the cuff estimating how much surface area he said and he said probably about the size of that table right there pointing at one of those tall cocktail tables

**Chris Gammell:** high top yeah yeah yeah and he's not he wasn't that far off yeah order of magnitude at least you know

**Eric Schlepfer:** yeah yeah a little bit smaller than that i i think we did some some of our own uh fermi estimation to kind of figure out ballpark what it would be and that was kind of when i started considering the 6502 as a candidate for the processor so for people who don't know what that is it's an early 8-bit microprocessor it came out in the mid 70s and it rests at the heart of a lot of classic 8-bit computers from that era from the 70s and the 80s and so things like the apple one the apple two commodore 64 nintendo entertainment system at their heart they all have this 6502 processor uh yeah keen listeners

**Chris Gammell:** and rememberers will remember we had uh chuck petal who's unfortunately passed away he was on the show back in uh episode 241 so that was 2015 so i'll link that in as well but chuck was amazing we should

**Wendell Aske:** say explicitly should say explicitly chuck was the designer of the 6502 yes sorry thank you thank you

**Chris Gammell:** that's yes very very clear there we were introduced from bill hurd who had used to work with him at mo at moss or moss moss what do you say there mos yeah okay yeah so so it's mos it's a really

**Eric Schlepfer:** interesting design and i hadn't really gotten familiar with it before the the challenge i guess you could call it and the reason that i picked it is because it had the lowest transistor count of any common popular 8-bit microprocessor that i could find and i didn't know how it worked in fact i did not even know 6502 assembly language so i i had had exposure to computers that used it but i'd only

**Chris Gammell:** programmed them in basic got it yeah and and most people were operating at the assembly level when it came out of course right i mean they weren't basic wasn't a thing till later uh yeah when it first came

**Eric Schlepfer:** out uh basic came along very quickly because basics had existed on other architectures and those

**Chris Gammell:** quickly got ported over to the 6502 cool yeah well i'm looking at the specs on the uh monster 6502.com which has its own site very nice total part count 4769 holy moly that's a lot of picking and placing it really is it's a good thing i don't do that by hand yeah i mean it's a full-size panel that's on this

**Eric Schlepfer:** board i mean this board was basically a full-size panel it's it's not quite a full-size panel it's it is large but it doesn't quite fill the full panel it is the only thing that gets to run on that panel

**Chris Gammell:** though yeah right yeah definitely yeah yeah wow that is really cool yeah what else what else can we say about it i mean well the leds so the leds were a add-on just to make it more visible is that right

**Wendell Aske:** no those are on the original uh mos 6502 you just can't see them because the black plastic dip that's

**Eric Schlepfer:** right yeah yeah they get you gotta get the special epoxy version order to get it right yeah something like that now that i put a bunch of the uh the idea behind the leds was to be able to view everything that maintains a state and so that includes all the registers all the register bits a bunch of internal latches things that contain the instruction register timing state machines all of that comes out to leds so by single stepping through code you could actually see the entire processor state at every step

**Wendell Aske:** it's a led bugger that's right nice did you just come up with that i i regret that i did yes

**Chris Gammell:** so i i am you know scrolling i i must have come upon the site in the past but this is implying that you're going to make this to the available to the public is that is that correct

**Wendell Aske:** it is but we are really hamstrung by the uh chip availability crisis ah i got it and one of the things to know is that a 6502 it's just a cpu if you actually want it to do anything including just you know run some blinky lights to show that it's alive you're going to have to put that into a computer so eric designed a wonderful tiny computer that we hide in that picture frame that you can see on the monster 652 site it's in the back and it emulates the entire rest of the computer the ram the rom the clock a you know input output all the things you need but it's a stm 32 that's running that and that's like a great idea in 2016 2017 when we were gearing up on this project and now it's just like are we really gonna yeah yeah port it to the rp2040 or something we're we're just kind of dragging our heels and hoping that there will be some signs of clear skies that will say go ahead this project isn't time critical in a sense it is critical that is done really well when we go whole hog with it because it is very expensive yeah definitely yeah and i mean

**Eric Schlepfer:** this is meant as a showpiece right that's kind of the idea oh absolutely uh in fact wendell uh you put together uh essentially a museum quality uh shadow box frame for it anti-reflection glass ah very important yeah yeah this is something that you could hang up on your wall and uh you know everyone that comes into your office is going to see that and have their mind blown for a while

**Chris Gammell:** yeah definitely yeah that's cool i mean you could go to a esp32 and then make it a wi-fi connected as well you could pass new programs to it or something yeah i mean there's there's a couple of different

**Eric Schlepfer:** options we're looking at i did look at the rp2040 but unfortunately it doesn't have quite enough iopens

**Chris Gammell:** to uh to control it got it well that thing is beautiful i got to see it at maker fair uh you guys were actually running demos i think you're running it as a computer right you had it plugged into a bunch of other stuff that made it possible yeah that's right that's cool yeah yeah it is amazing how the 6502 kind of just was so influential in the in the industry and it's i mean how old is it i was in the 50 50 years old uh came out in 1975 okay so we're getting there we're getting there yeah damn crazy well that's really cool there is a sign up at the bottom of that page as well if you want to get notified when it's available so i would recommend enthusiasts do that sort of thing all right well speaking of enthusiasts let's get to the the main event here and talk about this book because i am an enthusiast and i everyone i see talking about it on twitter otherwise is also an enthusiast first off what is the thesis statement for the book i would say that the thesis statement

**Wendell Aske:** for open circuits is there is gorgeous design inside of your electronics and you just haven't

**Chris Gammell:** seen it yet all right yeah that's good just gotta just gotta cut things in half or wait until eric and wendell do it so so let's talk a little process then how the heck did you cut all these things in half and get them to the point where they are so if people don't know this is basically showcasing the guts like wendell sort of said and you guys actually have the photos of like a lot of cross sections it seems like but it seems like that would not be that is a non that is a non-trivial

**Eric Schlepfer:** thing to do to get those cross sections it is much much easier than you might guess really vast majority of those samples were cross-sectioned using ordinary hardware store sandpaper oh

**Wendell Aske:** interesting easy easy is relative technically easy it's technically easy but uh this sort of crosses the line past the amount of work that somebody requires to the point that you must call it art because there's no other possible justification for it got it i mean so like i guess we should also

**Chris Gammell:** go to the book site here as well which is opencircuitsbook.com you can follow along and purchase your copy there but there's some example photos that we'll be referencing here so the first photo in the gallery is a 3.5 millimeter jack and it shows like the gold and the blue and you know basically the cross section of that that was just sandpaper or bandsaw and sandpaper the there's actually two

**Wendell Aske:** different techniques here there's a 3.5 millimeter plug and there's a 3.5 millimeter jack and they're actually done separately the 3.5 millimeter jack was cut by eric i believe just using sandpaper and

**Eric Schlepfer:** great amounts of patience well we did some experiments with that the jack we also attempted

**Wendell Aske:** on the mill uh the this jack was i believe cut on the mill uh there's actually a picture in the back of the book on the section of how we made the book showing how this very jack was cut

**Eric Schlepfer:** okay good so that's a good yeah the plug was sandpaper though that was yeah that was just me and uh sheet of sandpaper and uh little water isopropyl alcohol and a lot of time yeah a couple

**Chris Gammell:** couple of bob's burgers episodes and bob's your uncle yeah yeah pretty much that was my go-to layout show you know i was doing layout and just had bob bob on the corner just talking about burgers

**Eric Schlepfer:** i usually put on podcasts and stuff so uh typically i'll never listen to them never listen to them myself uh so it was you chris you made this cross-section oh i made it possible oh uh actually i think at the time i was listening to uh embedded.fm so well that's a good one too and you guys have been

**Chris Gammell:** on embedded is i know yeah enemy podcast uh you guys have also also been on that show we should refer to that you people can go and hear you guys on that show they got to you first they did and they

**Wendell Aske:** asked orthogonal questions so don't worry about it oh great i'm sure i will duplicate some stuff i did

**Chris Gammell:** listen to it but it was a while ago so like what else could people expect in the book generally like is it classified by type of electronics uh is it classified by you know how how is it laid out how how did you want to kind of walk people through electronics as a viewing medium so this is really a

**Wendell Aske:** survey across all of electronic components not really all of electronics so we don't show you for example what the inside different types of radios and food processors looks like or washing machines or different types of other appliances and electronics but it's really trying to show showcase different types of electronic components and we organized it by what an engineer would typically call most of these components we have a section of passive components a section of semiconductors a section of cables and connectors we also have a retro tech section that is primarily obsolete things which we started out with an incandescent light bulb sort of as a joke and we have a section of composite devices which was sort of a catch-all for components that have other components in them but also circuit boards and at the end there's a section about the making of the book cool i hope i didn't miss any oh yes there i did miss one there's a section on electromechanics which is uh switches and motors and things yeah we tried a bunch of different ways to organize the book

**Eric Schlepfer:** and and this one really felt right everything kind of gelled yeah that's great that's uh i mean

**Chris Gammell:** thinking through like how how i think about components and stuff like that too it does kind of line up with a lot of that that sort of thing so the retro tech is also like stuff that i didn't really think about you know like uh so like neon neon lamps are one thing where i i've just i've never actually designed with them so i wouldn't i wouldn't think what's inside of those sort of things that's sort of a remarkable example

**Wendell Aske:** because it is such old technology it is literally a vacuum tube and yet they're still built into so many things that are manufactured now like light switches for your house that glow just when they're energized or uh extension cords that have a light in them are all neon bulbs i'm sure some uh some

**Eric Schlepfer:** listeners are shouting right now it's not a vacuum it's filled with neon

**Chris Gammell:** that's a good point that's a good point yeah it's interesting as well because i just actually finished kathy's book i forget kathy's last name shoot she was just on with dave a couple weeks ago and uh about the history of electricity and so i've i've been actually going back through and reading about all of the historical how things were built and designed and you know discovered and stuff like that and especially in the retro section you know like all i mean really all of these things it would just been so completely mind-blowing as people were building these things up and now it's just stuff that is lit it's all around us and we've it's it is so prevalent that

**Eric Schlepfer:** that we just forget about it all the time one thing that really struck me when we're doing research for the book is that the old style of components not just stuff in retro tech but stuff that's even older than that they're made using very natural materials you know lots of brass and and wood and some very early plastics and things of that nature and nowadays everything is synthetic so it's some variety of plastic with some fiberglass and it's it's a much longer supply chain if you will so there's a much longer distance between that finished good and the raw materials that went into it what did we have that had wood in it i don't remember yeah uh well we had some early plastic and i think it was the capacitor that i think might have had uh like sawdust or something like that and yeah kind of bakelite style now phenolic of course is kind of a impregnated paper so

**Chris Gammell:** i think we have one that's like the ordinary phenolic's like the one that you see in like really low cost like single-sided designs right like power supplies but it's really like a tv it's a funny

**Wendell Aske:** word because uh phenolic used to mean just uh plastics are made with phenol resins things like bakelite and so on but the term phenolic really does include every fr4 technically as it's used that uh every type of composites that are of a certain class are all regarded as phenolics but it's interesting uh such different meanings of the term yeah speaking of fr4 uh when you were

**Chris Gammell:** kind of getting into some of these things i mean were there concerns about just breaking stuff apart like uh like fiberglass and just being in the air that sort of thing yeah in general you want to avoid

**Eric Schlepfer:** getting uh fiberglass dust into the air so it's it's just really not good for you and uh so typically uh sanding you want to wet sand uh make sure you've got good ventilation all of that another good one is that when you're done you don't want to dry wipe any of the surfaces because that'll generate dust so you go in with wet wipes to make sure that's all kind of cut down so it's one of the excuse me it's one of the reasons why i recommend that people actually don't try some of this stuff at home unless they understand all of the uh ppe that they need to do it safely yeah yeah that's a good point and some of

**Wendell Aske:** them things like nixie tubes there's mercury in those you really oh really are going to come across nasty stuff just take stuff apart randomly you need to be aware of it yeah definitely and in fact some

**Eric Schlepfer:** other components like uh certain kinds of power transistors uh use beryllium oxide in their construction and that is quite hazardous to cut into okay so that does require some specific knowledge about what has that stuff and what doesn't have that stuff and so there are definitely items on our list that we looked at and said you know what this is not really safe to cross section so we'll just skip

**Chris Gammell:** that yep yeah where i mean did you guys have to was it generic enough stuff that you were just kind of sourcing it from on the lab or did you have to kind of hit up the rapidly shrinking uh surplus stores

**Wendell Aske:** of the bay area a lot of the stuff is from our personal collections and a lot of it is from the strip-less stores some stuff we got on ebay specifically for the project if we know that the book was going to do so well we might have spent a little more on getting some esoteric components from uh online sources oh like uh did you leave stuff out specifically because because of cost or just struggle or whatever it's it's a funny thing not every sample that you get your hands on is going to turn out to be a good photograph or a good subject to describe and so some of the some of the parts that eric put an immense amount of work into preparing we just ended up not using because we couldn't get a good enough photo of it just wasn't going to be photogenic enough and we can buy some exotic chips online but if you don't really have great confidence in it it's a

**Eric Schlepfer:** little harder to go out and do that yeah there's there's always the risk that you spend a bunch of money to buy something and then you go and you cut it in half and look at it and it's not very

**Chris Gammell:** interesting yeah poor little component it was sacrificed for nothing for a good cause yeah yeah that's true you know i have to say this book even though the style is very different right this is a lot of bright colors and obviously it's cross sections and stuff like that i can't help thinking about the way things work you know like that is just that is a formative book in my in my past i would just sit there reading and rereading it over and over again and i have to imagine a young person getting this sort of thing is just going to be like marveling at this yeah i think that's right

**Eric Schlepfer:** in fact i've heard the same thing from a number of other people the way things work actually really impressed me when i was a kid too that was definitely one of my go-to books growing up along with a much more obscure book with sort of a similar similar style i guess but far more technical so they had technical drawings instead of the sort of cutesy pencil sketching and uh it was apparently made by a german publisher and translated in english i wish i could go and look it up for you but uh i don't remember what it was called offhand okay well maybe we'll maybe we'll find out later

**Chris Gammell:** if so i'll put it in but uh yeah i mean if it doesn't have little mastodons like you know pulling the cd drive i don't know if it's really going to work for me those are so great you guys should have snuck at least one or two into your you know little easter eggs or something here right

**Wendell Aske:** surely there's one hiding in your photos we have a few subtle phrasings that are could properly be classified as jokes and there's one illustration that you might find that could be properly classified as a joke as well we didn't quite go quite as far as the mastodons though

**Eric Schlepfer:** got it okay all right and i think there's also a little secret hidden in the end sheets but uh you'll

**Chris Gammell:** just have to get the book oh yes there is indeed i guess so yes i mean in all things here obviously you know no matter how how well we try and describe these things i don't think we're gonna

**Eric Schlepfer:** possibly do it justice i was gonna say amazingly enough if you if you view the pictures on the web they're gonna look great right so you can go to the opencircuitsbook.com and see some samples those pictures don't really do the book justice because if you have the book in your hands and you open it up and you look at the picture it just looks 10 times better than what you see on the screen

**Chris Gammell:** yeah yep yeah i mean and it is like you like we were talking about before the show you said this is meant much like the way things work this is meant as a coffee table book kind of sit out leap through it discover new things yeah exactly that's great what surprised you what surprised you as you were

**Wendell Aske:** kind of discovering the inside of the guts of these things every day was a new surprise every single thing we opened had something inside we hadn't really thought about or sometimes when you cut something you're intimately familiar with at a funny angle you find something you're not familiar with and it was really it was really really hard to choose which angles to show of things and which subjects to include because there was just so much we could have made the book three times as long not that that's necessarily an advantage but it was just one thing after another and maybe that itself is the surprising

**Chris Gammell:** thing that it didn't get boring that it didn't like you didn't tire of the of the surprise or that it

**Wendell Aske:** didn't stop being surprising well we cut into a whole lot of things we hadn't cut into before and i'm not sure i can uh uh let me actually one example uh we have a circuit board from a smartphone that we cut at a steep angle not just a cut through it but it is like a 15 degree angle through it maybe 20 degree angle oh that was one of my favorites so it's like a ramp right like a ramp and you think okay so what big deal but because it's cut that way you can see each of the layers of copper sitting above the one below it and extending sideways and you get sort of a isometric view through the circuit board seeing this such three-dimensional nature and you see a via there as a circle yeah suspended in space and it really hammers home that this is a three-dimensional thing it's a view that all of us are used to in the cad software when you rotate it maybe but it's uh visceral to see it in real life

**Chris Gammell:** yeah that's great it almost kind of reminds me of i'm looking at it right now i have it up on my screen but it kind of reminds me of like uh if you had a circuit board and then it was like the sun was setting on it you know it's like casting a shadow basically you know that kind of is what it what it feels like to me but it definitely the that any kind of cross section you get like these really cool views of like the how the layers interact but then when they start to when it starts to tip

**Wendell Aske:** like this and go to an angle you see even more in your book refer to page 233 that's right yep that's

**Chris Gammell:** good call yeah we should call that out probably when we say this stuff uh we we should have put in like that little tone like they used to do on the ah the records right ding page 233 and of course we can't forget that's gonna age me right there guys you know that that is first off i said record and uh you know but they must still have that right i guess yeah just i just search for

**Eric Schlepfer:** it guys just ctrl f yeah and of course we can't leave out the cover photo i think that's a wonderful example of a very complex uh circuit board that uh even people who spend all day long designing pc boards typically don't see you know you're looking at it from top down and everything is flattened out and half the layers are hidden and to see it from the side like that i think is is really quite something

**Wendell Aske:** that's great that's actually from the same circuit board that we cut at an angle oh really okay so that

**Chris Gammell:** one got that one got a lot of uh uh top billing on it's a 10 layer board there's a lot to see man someone handed me where was that i don't remember who did it but someone handed me an ipad board like an unpopulated ipad board and i got to like take some close looks at it and just it's unbelievable and that was probably five six years ago no probably more than that even now probably 10 years ago it's probably a 10 year old ipad board it's just like unbelievable what they're doing there like every year it just gets more and more complex it's pretty yes it's not quite

**Eric Schlepfer:** as more complex as you might think pcb technology although it definitely gets more advanced it doesn't get that much that much more advanced so you know you're going to use hdi which is high density interconnect and you know they can improve how close together the lines can get and and uh you know trace widths and all of that but you know it's it's not really the the the huge leaps and bounds improvements that you might suspect but you will see interesting innovations in packaging like this particular cross-section on the cover i really like the fact that you can see this system and package that's soldered to the board and then inside that it's got several chips that are stacked with other tinier pcbs in there and then i think there's a pop ram which stands for package on package and it just looks really quite stunning when you realize that this thing has so many layers it's it's a three-dimensional structure yeah yeah that's really cool i i was thinking as

**Chris Gammell:** as i asked you guys the what was surprising i remember a component where i forget i think the pot the top might have popped off of it maybe it was maybe someone had etched it down but like it was uh one of those like usb isolator chips and i remember like looking inside and it was the uh toroidal kind and so it was like oh yeah it's like there's like little transformers in there and they're just like you know coupling it was like just coupling between the two across a barrier interface i'm like oh yeah that's how that works that makes sense it's like you know it's like when you but like so much is hidden by the the polymide outside you know like that is just like you don't you don't think about it and then now now we get some views inside so that's pretty cool what um you'd a bunch of stuff around bgas as well did you think about doing any like kind of uh uh cat scan not cat scan ct scan style things i mean or did you want to have it all

**Wendell Aske:** to stay physical it it uh it was a really interesting question we thought about early on maybe doing some microscope photos maybe doing some other things uh we do have friends who can grant us access to 3d x-rays and other types of tomography but uh it uh something very visceral and very real about having these pictures that are not they're not the computer models and they're not reconstructed models they really look like you could just look at this if you had a magnifying glass and see this and we tried to keep that aesthetic throughout i'm not sure that's necessarily the best thing to do it may be more informative to show other technologies but i do certainly like it from an aesthetic perspective that we have this consistency one of the things that really strikes me

**Eric Schlepfer:** is that the the x-ray cts and all that they can look really amazing especially if you have kind of that technical background and so you kind of know what you're looking at at the same time it's monochrome and for a lot of people it's color is something that's just really interesting and attractive to look at and so that's one of the reasons i think why we tried to stick with colorful components and i think we went and seeked out many of those on purpose just because they really popped and looked really good in the photo yeah that's a good point yeah it does it does

**Chris Gammell:** definitely like it helps offset things and silicon kind of gets that rainbow sheen sometimes but you gotta you gotta get lucky and that that china if you're doing you know photons instead of electrons or whatever whatever you're shooting through the board or reflecting off the board that sort of thing what's next for you guys i mean what's the other books not in the near future yeah i would say that uh

**Eric Schlepfer:** i i i'm gonna need a while longer to forget the trauma of the first book before i consider making

**Chris Gammell:** another book okay let's let's hear it here though like so what is it about books that makes it tough because i feel like many people in the audience myself included are you know i could write a book

**Wendell Aske:** someday so like what is what is the slog part of a book there's a few different slogs the we did the essentially the core photography cross-section cutting and writing in a nine-month stretch it was interrupted by we actually took a year off when the pandemic hit we just sort of set the book project aside and worked on other things but we came back to it and the total amount of time we spent on it was really about nine months but they were nine months of it being effectively a part-time job to work on it and then we had essentially a one-year editing process oh my yeah we had a very very good editor assigned to us by no starch press and i thank them profusely for putting the resources into the book to make it come out really well but you know he would ask the question okay what does that mean and it would be something like but you know you know what that means right no he doesn't know what that means we use all kinds of jargon constantly that we don't even think about because we're so used to it

**Chris Gammell:** and he really forced us uh do you have an example that uh that like kind of made you made you realize this aside from your editor saying as much ah eric can you think of a good one we had a long discussion

**Eric Schlepfer:** about multiplexing in one spot and some of the it got really complicated and we realized that there's just some of that stuff is so hard to describe and it just took attempt after attempt the other thing to realize is that we're not trying to write a textbook right we're trying to write something that's accessible to a really broad audience and so it's good to provide some detail but because there's a limited amount of space there's just only so much that you can explain and then on top of that you can't use all that jargon it's just not going to be understandable it's going to put people off in many cases and then at the same time you can try to simplify things but you can't you can't put something down that's technically incorrect so it also has to be correct too and so all those constraints acting it together made that text really really difficult to write yeah i always

**Chris Gammell:** like the uh the experiment that randall monroe did with the upgoer five i feel like that's like a perfect thing in like the technical communication thing where you're like if you actually limit yourself when words it has a very certain like stilted feel to it and he used it to great comedic effect but like but you need certain you need to like to you need to define things up front and then keep that in people's brains or remind them about it and like you said you're not you're not trying to write words and words and words so yeah i can imagine that's the brevity is is is the tough part

**Wendell Aske:** one of the tough parts so uh one of my professors once gave me this wonderful piece of advice he said if you really understand something you can explain it in any interval of time and i think that's really true that if you really do understand a subject deeply you can to any individual person explain it to them in you know one sentence or a book at varying levels of precision not different accuracy window i'm

**Chris Gammell:** just i'm not realizing i don't i don't understand electronics i think because i don't think i could

**Wendell Aske:** explain things in a sentence or two well i'm sure you could so for this book we had not just that challenge of explaining something to this amount of space but we also have a separate challenge which is you have to explain it to these widely varying audiences it's not just that you have to explain this to a lay person who has done zero electronics you also have to make this such that the person who designed that component when they open up this book they'll kind of nod their head and say yeah that's simplified but it's basically right okay like design the actual thing that you're photographing

**Chris Gammell:** you're saying they're gonna look at this book man that's that's a lot of pressure i mean the old stuff at least they're you know they're probably retired or yeah but yeah you're right that's really i i have not thought about that there's going to be fan mail and uh angry mail not not much of the latter yet that's good good also you can just uh you know i think if you force people to write a letter in it'll it'll cut down cut down on stuff please write to the following address with a self-addressed envelope that sort of thing you know yeah we'll only accept it typewritten paper preferably with this electric but that's right yep that's great yeah so i i can imagine that that would be something that you'd want to do rarely but i i imagine there's a lot a lot more photos and and that sort of thing that you guys could do certainly the subject matter is not prohibitive

**Wendell Aske:** and maybe we'll do a uh extended edition if there's interest someday yeah but a book project is just a huge commitment of resources and both of us have lots of other things that we work on so we're not

**Chris Gammell:** eager to jump back into it what else are you guys interested in uh in life and and work and tech what what are your some of your upcoming projects you're willing to talk about that is a

**Wendell Aske:** shortened shortened version of that question uh well my my day job i designed pen plotters for evil mad scientist and i've been working on next generation pen plotter hardware for quite some time and i maintain the software and also do a lot of community support so i have a lot going on there and then i also run a project blog where we occasionally post things these days we used to post a lot more but we're so busy with the big projects and eric has got all kinds of projects going on oh yeah like you

**Eric Schlepfer:** wouldn't believe people often ask me how am how am i able to accomplish so much and i say well i've got about maybe a 10 to 20 success rate so my secret is just starting a lot of projects yeah only publishing the good the the things that you want to talk about right so that's what people usually see and and so then they come up with that assumption so anyway i spend probably too much time on twitter at least for now we'll kind of see how that uh shakes out well yeah plotter twitter is

**Chris Gammell:** another thing right so the pen plotter has a hashtag that's fun to follow but may may have to go to

**Wendell Aske:** plotter master don the problem is that's not a portable hashtag and so the community is kind of realizing oh we better not make a branded hashtag this time oh yeah right right like plotter plotter

**Chris Gammell:** plus days or something like that huh like uh hashtag pen plotters what's going forward okay okay it does it just doesn't have the same ring to it yeah and uh the the plan plotter that you work on window is

**Wendell Aske:** called uh it's called the extra i was hoping for a plotter tutor plotter tutor like the like like a

**Chris Gammell:** teacher oh two oh mastodons don't have tweets they have toots oh really i didn't know that i'm i'm a very nascent user of mastodon i i'm basically a stalker right now or a lurker i suppose um i've been a stalker much longer uh uh yeah no that's that's interesting uh that's that's out there but yeah i mean eric obviously you post on tube time a lot as well on twitter yeah yeah so that's kind of uh

**Eric Schlepfer:** turn into a big community of people who are uh into electronics and retro computing and all kinds of uh interesting things like that so i kind of use that as a as sort of a running lab notebook of things

**Chris Gammell:** that i'm working on in the home shop could you give us a sampling of recent recent projects you

**Eric Schlepfer:** talked about so i've been working on a replica apple one and it's been a really interesting challenge because the board i got from a friend and he built the replica based on photos of a real apple one oh and he drew it up in adobe illustrator wow yeah well it does help that it's a two-layer

**Chris Gammell:** board right so that's all right right that helps on one one in front but still that's that's uh i remember hearing about someone someone that did that like professionally they would do that they would use illustrator for like modern boards not not like not like tracing out old ones yeah he was

**Eric Schlepfer:** telling me that uh the fab vendor really hated the gerber files because of course he started in illustrator there's a ton of extra geometry and stuff but the problem is is that there's a couple of mistakes i mean it's not perfect it looks really good as a display piece but part of the whole challenge of building it up besides you know having a bunch of dead ttl chips to deal with was the fact that there were actually a couple of connections that were either missing or wrong and so it was really a big troubleshooting adventure come on was

**Chris Gammell:** what are you doing here man i just yeah can you imagine like you know you were getting scrutinized with 50 years later i guess it is that's that's pushing 50 years as well right i mean like and it's just like yeah i made that mistake 50 years ago what are you gonna say do about it you know

**Wendell Aske:** it's like every time somebody talks about the arduino pin spacing yeah exactly it's just it's

**Eric Schlepfer:** how it is just deal with it yeah there's a whole community of the apple one folks and they actually have all these uh mods and improvements and they're all designed to go on the back of the board so it still looks like an original apple one uh how how big is that community uh there's quite a few people there's uh i think it's apple fritter is uh where you can find uh most of that activity okay that's

**Wendell Aske:** good good pointers so uh eric you're gonna make that thing with the variable clock rate

**Eric Schlepfer:** the variable clock rate uh i mean i i could try but the video circuitry is kind of entangled with the timing of the whole board the reference of course is to the monster 6502 because it has a limited clock speed uh it runs up to about 50 kilohertz and then it starts to lose its marbles for various reasons yeah capacitance in the board and such yeah yeah exactly so there's there's a few computers i've been able to connect it to so far such as the aim 65 and of course my homebrew computers but the big problem is that a lot of those early machines entangled the basic timing cycle with the video generation and the apple 2 is a very famous example of that

**Chris Gammell:** yeah i um i've never really got into the the vintage side of things i think i'm just a little too late and a little too not knowledgeable uh but i did get to go to the computer history museum and just kind of like wandering through there it's just unbelievable seeing like how much how much people did with so little you know what i mean like that of course you guys know but like uh you know just the the fact that anything worked on those machines is amazing to me

**Eric Schlepfer:** yeah exactly um for me it's actually a great learning experience because i get exposed to all kinds of interesting design techniques that may not be quite so common anymore you know everyone just stuffs everything in a giant soc and all you have to do is just hook up the wires but back then there was a significant design effort that went into uh getting these things to work properly uh what what were some of the challenges there a lot of timing challenges so back in the day people didn't use synchronous logic quite as much uh what that means is synchronous logic is you've basically got some combinational logic in other words just a bunch of gates the output of which goes into a d flip-flop yeah and then you have multiple stages of those cascaded and that's kind of the whole design of things but back in the day when you're really limited on the number of gates that you could put into a design people used asynchronous techniques a lot more where you have combinational logic going into different inputs on different kinds of latches so you might have a set reset latch or a jk or something like that or you might build your own latch out of combinational logic and so there's all kinds of weird little timing issues that you have to deal with and it makes the design incredibly challenging one of the biggest innovations of hdl based design is that it kind of solves that for you because you just simply follow this little strict template and then you can take advantage of all these analysis tools and so timing is much easier with that kind of a modern design paradigm yeah i always think about the like uh the errors i used

**Chris Gammell:** to get when i was doing fpj stuff and i was always like you know you didn't make the clock rate and just kind of visualizing like you didn't all of your logic didn't get to like this deadline basically where the the clocking was based on physics and how far it could get across the chip

**Eric Schlepfer:** and that sort of yeah exactly and it's it's not complicated what it does is it looks for the worst case longest timing delay path in your logic and says that's your max clock speed and that's it

**Chris Gammell:** i can imagine that's a nightmare to debug though because like if you're not making timing in this asynchronous manner it's just like you're just chasing ghosts all the time yeah it makes it very challenging so you know a one or two two uh channel scope was probably not your you know it's better

**Eric Schlepfer:** than nothing but it's not not easy yeah my i would say my most frequently used tool for that is the sale logic pro 16 yeah and so you get 16 channels pretty easy to use and i've used it for debugging

**Chris Gammell:** all kinds of crazy issues yep that's awesome uh on other retro type computing you've been doing as well

**Eric Schlepfer:** i mean is there other things you're building there all kinds of stuff going on i i dug up a what's called a stringy floppy which is more of a restoration and investigation project than it is something that i'm designing but it's basically a miniature tape that was designed as sort of a floppy disk replacement for computers in the late 70s and it doesn't store very much data but it has some interesting design principles that made it a very popular choice for a very short couple of years until the prices of the five and a quarter inch floppy drives came down to the point where people all switched over and uh so it's it's very old archaic hardware that has essentially no documentation and so i've been going in and reverse engineering it to try and figure out how it works yeah that's cool

**Chris Gammell:** that's really cool i'd never heard of that you said stringy floppy or just stringy floppy stringy floppy interesting yeah i mean that is interesting i mean like so you guys live you guys are in the core of it right you guys are basically like in silicon valley and like we mentioned that a lot of the surplus stores are shutting down and unfortunately a lot of the pioneers are aging or have passed away and it's just like how do we how do we preserve some of this stuff you know you both of you have done a lot obviously i mean you have stuff that you're preserving in print now but like and you're doing projects both of you that are are preserving kind of history and getting people interested in this stuff but how do we preserve it and i guess more importantly should we preserve it is it is it

**Eric Schlepfer:** worthwhile to preserve it absolutely i think a lot of it is getting the word out uh getting the stuff documented in places like the internet archive and other documentation archives so not just documentation but details about the design uh so one of the things that is kind of at the front of my mind after recent events on twitter is i realized that a lot of this documentation that i've put together if it's not something that i've put on github and it's related to a reverse engineering project it's stuck on twitter and the future of twitter is a little uncertain and so i want to make sure that all of that information will still be available to people regardless of that you know

**Wendell Aske:** chris by the time this uh a podcast is released uh the situation on twitter's could be very different than it is today yeah anyway i've downloaded my data archives i hope you have too i have absolutely

**Chris Gammell:** yeah yeah yeah i mean uh and it does actually it's interesting too you know so thinking about you know early early computing and really even early internet you know actually like there was no kind of there was no cloud it was just your own computer and someone else's computer but like but like running your own site your own documentation anything like that can go away you know and so obviously we want to support internet archive and that that sort of thing is to stick around but twitter internet archive all of them it's like you kind of just need to have at least like you said with github you know some people are going to have local repositories that sort of thing so it's just it's almost like making sure there's enough information out there but then also that it's spread out enough and not enough

**Wendell Aske:** people's computers is back up well one of the things that's going to happen in in times of uncertainty like this like one of the problems if twitter were to go away their link shortener goes away and so much stuff wow yeah that is just you know linking from one place to another on the internet that doesn't even involve twitter really directly is using their link shortener this is just

**Chris Gammell:** catastrophic yeah yeah that's like fabric fabric of the internet basically at that point huh link shorteners are kind of a terrible idea well unless you want to track a link you know unless you want to see who's clicking your stuff then it's then it's great commerce and being tied up is is a part of the part of the problem i think it's just also temporary

**Eric Schlepfer:** and that's i don't know that's something i come to realize over the last couple of days uh looking at alternative platforms and stuff like that is you know they each have their pros and cons but it really makes you realize that so much of this stuff that we deal with is is really temporary that's why you should have a book i just print out all the tweets i like it yeah boy that'd be a lot of

**Chris Gammell:** a lot of paper and a lot of spam a lot of paper i don't know your tube time archives on twitter

**Wendell Aske:** make a pretty good book you sure you don't want to do another book this year there you go yeah

**Eric Schlepfer:** uh my eventual goal is to turn all of that into a static web page so i'm hoping with a crappy python script and uh the downloaded archive i could probably pull something together that's a great

**Chris Gammell:** idea anything with an image definitely goes in that sort of thing any replies exactly don't go in

**Eric Schlepfer:** any memes stay out i get you know honestly that's the hardest part is that there are a lot of really good people in the community that comment very frequently on my tweet storms you know on particular restoration projects and i came to realize that really uh tube time is not just me but it's it's everybody else who participates yeah you know because i'll go in and say hey i'm working on this thing and then somebody will reply and say well you know i designed that back in the 80s and then i'll go and reply and say well i got a bunch of questions for you and all of that gets somewhat preserved on on twitter you know it's a little hard to search for sometimes but if i can find the thread and i keep a whole set of bookmarks of some of the projects that i've worked on then i can just click on that find their comment and go oh yeah that's right they said such and such

**Chris Gammell:** yeah we need like an internet archive just for electronics twitter that's what we really need yeah exactly yeah yeah it is it is tough too like not that you know obviously we're here to talk about your book but the because the three of us are denizens of twitter and uh you know and lamenting its potential downfall people often ask me like well why do you why do you on there like last night i was trying to explain some stuff about it to my wife and she's like well why don't you just leave i was like first off i'm addicted okay let's just get that out there and second off like it is you know it's an ad hoc community it's asynchronous like it's i don't know it's open you don't have to have an invite you know like all of those kind of things that like it's it's the lack of walled garden right so like that those things are all good and you can kind of peek in on other people's conversations i can see you to you as tube time talking to the 80 1980s designer that sort of thing i can glean knowledge from that like yeah and so like i don't know i just want that that style of thing doesn't have to be twitter but that kind of like discourse i want my life and i want to be able to view it be part of

**Eric Schlepfer:** it you know and that's one of the reasons why i've been looking so seriously at mastodon but it does have some big issues uh not necessarily technical issues although it does i mean i'm not really referring to that it's it's it's kind of a cultural issue because the folks that i see on mastodon are too much like me right so they're technical people doing technical things and one of the biggest appeals of twitter to me is that it's such a broad audience i get all kinds of interesting people looking at my stuff that don't really know what's going on and will ask questions and so there's sort of this educational aspect to it as well you know you won't believe how many dms i get from people that are confused about something and i found it really rewarding for everyone involved to go in and respond and answer folks's question i mean it's it's great it's a great interaction and uh i think every everyone benefits from that whereas mastodon it has this sort of barrier to entry like you kind of have to figure out how it works and some things are a little confusing especially if you've uh never looked into it before and so i think that's kind of off-putting to a lot of people that have no problem with twitter or instagram or some of the other platforms out there yeah yeah it is kind of like uh

**Chris Gammell:** almost like the when you guys had the monster 6502 at maker fair like same kind of thing where like people are walking up they might just be walking by and be like oh that's cool walk on no problem but they might be like no i'm into this and like now i want to you know they go and take like a ben eater course to try and learn more scroll back through your tweets to learn more just sit there listening

**Wendell Aske:** as you're explaining it that sort of thing like yeah yeah we actually have the monster 6502 set up and running on our front uh desk at the office right now and sometimes people walk by and they're just walking by we don't have a sidewalk here but if there were a sidewalk they'd be walking on that and we've had people actually stick their head and say what is that just out of nowhere is that skynet because it looks like skynet no i know it's not had somebody say what is that monitor showing and that was the funniest one to me because that's a good one uh yeah that there is the internet my friend that's yeah the internet's grandfather right there yep yep that's where it all started

**Chris Gammell:** man well uh let's let's make sure people know exactly where they can go and buy this beautiful uh book and uh have so they can scroll through it and marvel at it like i do i would recommend that if

**Wendell Aske:** you'd like to get the book you go to opencircuitsbook.com and we have a list of resellers of the book right there you can get it direct from no starch press my store evil mad scientist has signed copies while they last and links to other sources as well great and where can people find you in the short or long term uh you can find me at evil mad scientist.com and uh i hope that's long term yeah that that one is

**Chris Gammell:** well you you as long as you don't you know miss the domain registration you'll be you'll be fine

**Wendell Aske:** yep i mean i've also got uh windell.oskay.net so but that's mostly my uh leftover pages from the 90s yeah my vestigial web presence they do stick around huh eric how about you and i've of course have the uh

**Eric Schlepfer:** the twitter account at least for now uh so that's uh tube time us and i also have a blog which uh every once in a while i'll update and that is uh tube time dot us so you can see the relationship anyway if twitter's not around uh i'm also on mastodon as uh tube time at uh mastodon.social great and i think i have maybe one or two posts there maybe more yeah we'll be forthcoming so we'll see

**Chris Gammell:** how that goes yeah yeah we'll see how it all goes well guys thanks so much for uh coming out and explaining the book today it's been really really great to hear about it good talking to you both i hope we get to hang out again in person soon and i hope people pick it up i think this is going to be many many coffee tables will be adorned with it in the in many bookshelves well it probably won't sit on the bookshelf it'll probably be down this is like a bedside table kind of book you know view it view it before you go to bed and dream of circuit boards and chips and stuff like that dream of circuit boards and chips all right well thanks for coming today thanks chris well thank you so much

**Wendell Aske:** you
