---
episode: 393
title: I've bitten myself
url: https://theamphour.com/393-ive-bitten-myself/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released May 20th, 2018. Episode 393. I've bitten myself.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. Same bloody intro for eight years or something.

**Chris Gammell:** Eight years in August. Oh, there you go.

**Dave Jones:** I had no idea when we started.

**Chris Gammell:** Yeah, it was August. August of 2010.

**Dave Jones:** You get less for murder.

**Chris Gammell:** Yep, yep, yep. We're still doing it. That's it. Yep, yep, yep.

**Dave Jones:** What's happening? What? What's happening? You're struggling with PCVs.

**Chris Gammell:** Now we're even like an old married couple here. Huh? What? What? What? What? Yeah. Yeah, I'm struggling. Well, I've mentioned-

**Dave Jones:** No, you got caught in the usual trap of the manufacturer's comeback and said- and waved the finger at you.

**Chris Gammell:** Well, so the first thing was I was a little thrown off because it was Chinese Labor Day. So all of our Chinese listeners, happy Labor Day a couple weeks ago. So it was already behind, so I was in a rush. And then, yeah, they came back and they're like, what did they say? It was like, you don't have enough clearance here, something like that. Solder mask is too narrow, and they gave me a picture.

**Dave Jones:** Solder mask is too narrow. Very common problem.

**Chris Gammell:** Is it that common? I guess, yeah.

**Dave Jones:** I hear it all the time. Yeah. All the time.

**Chris Gammell:** Yep. Well, and yeah, so you and I were talking before the show about- Well, could you explain the difference of those two terms you said?

**Dave Jones:** Okay. Well, when it comes to solder mask, well, there's only one- I'll say it front. It's better to say it this way. There's only one requirement that the PCB manufacturer has when they're manufacturing your solder mask layer, and that is the thickness of the tray. So I call it the solder mask slither. So if you hear me use the word slither. Slither or sliver? Slither. Slither.

**Chris Gammell:** Sliver. Okay. Can I say it?

**Dave Jones:** Yeah, I probably can't say it properly.

**Chris Gammell:** Slither is like a snake. Slither is like a piece of wood that goes into your finger. Yeah. Okay.

**Dave Jones:** And of course, this solder mask is like the inverse of a copper layer. So it's like, you know, you do a cutout where the pad is, right? And then you have the solder mask between pads, because that's the whole concept of solder mask. That's the magic of it, right? It's useless having a solder mask if you don't have it between your pins.

**Chris Gammell:** It's just equals boards that aren't crap.

**Dave Jones:** Magic, yeah. Right? Yeah. So you want solder mask between the pins on your surface mount parts, whether it's just a standard SO, big ass SO package, or whether it's a, you know, what's the pitch you're working on? What's the pin pitch?

**Chris Gammell:** You're working on a little QFN. It's a QFN7, or sorry, QFN28, so whatever that is, 5x5. So not huge. I mean, not like the small, it's not BGA, but it's not huge.

**Dave Jones:** Is it 0.5 millimeter pin pitch? Because that's usually the start of the pain in the ass category.

**Chris Gammell:** Yeah, I think that sounds right. Yep.

**Dave Jones:** Yep. Right. So that's, anyway, when they're manufacturing your solder mask layer, that's the only thing they care about is how narrow that slither, that trace of solder mask is between each pad. Right. Just like they will have rules for your copper layer, which is the inverse, where they will say your trace could only be 6,000 wide.

**Chris Gammell:** Right. Right?

**Dave Jones:** It can only be 6,000, 6 mil. This is all resolution problems, right? It's a resolution problem. Right. Yeah. Right. And that's all they care about. So as long as you've got that, that's the only thing they should complain about. Now, but there's two aspects to what determines the slither. You don't draw the slither between the pads. What? Is my pronunciation that bad? Slither. Slytherin. Should I? Gryffindor. Sorry. Anyway, you don't draw the lines. I won't say slither. You don't draw the lines between the pads of where you want your solder mask. What you do is you specify what's called a solder mask or pad expansion on your pad. So each pad has the property. If you go in and edit the pad on the copper layer, it has a property. No matter what package you use, unless it's some weird-ass package, it'll have the property. What's the solder mask expansion? I.e., how many millimeters or how many thals it goes outside of your pad. What clearance around your pad it creates. Now, on fine-pitched stuff, I argue that you should set this to zero. Solder mask expansion. Usually you'd set it to, I think, most packages by default are two or three thal. Something like that. So it gives you some clearance.

**Chris Gammell:** Yeah, I was going to say, in KiCat, I think it's six or something. It's six. It's much higher. Right. It's much higher. I think Altium's. Or at least the way they draw it is usually further out. But then, like, yeah, the default.

**Dave Jones:** Yeah, the default. So it gives you some clearance. So what that does is that because all these layers must be aligned, all the copper layers and all the solder mask layers and the silkscreen, all these layers have to be physically aligned when they manufacture your board. Right. And having that expansion just allows for a little bit of misalignment.

**Chris Gammell:** Right. Exactly. So to speak. You can see that on certain, especially with bad board fabs. Oh, you'll be able to see it. Yeah. But even at good ones, right, you could see, like, a little bit of the FR4 around the copper. Yeah.

**Dave Jones:** It doesn't quite. The clearance around the pad is not quite even, and that's one of the inspections you'll do when you're evaluating a new PCB supplier, for example. That's right. You'll go, how good is their alignment? Yep. You know? Yep. So that's, yeah, so that's the thing. So that's what that solder mask expansion by default gives you. But the problem is once you get down to small pin pictures like 0.5 millimeter, you've only got a certain amount. Maybe I should, like, open Altium here so I can have numbers ready.

**Chris Gammell:** Yeah, I was thinking I should have the Kikad open too.

**Dave Jones:** Yeah, yeah. And anyway, people will get the idea, hopefully, considering that this is not a visual medium anyway.

**Chris Gammell:** Right. And so I think, yeah, and I think the thing here is that I, because I was rushed and because they brought it back to me, I was- You had it by default?

**Dave Jones:** Well, I had it backwards. Did you have it by default or did you specify? No, no, no.

**Chris Gammell:** I had specified. I specified three mils. And usually-

**Dave Jones:** Oh, so you told them to do it?

**Chris Gammell:** Yes. Yes. Ah. Well, here's the thing. There's your mistake. Well, yes. And that was part of it. And then because I was backwards, so they basically sent me back a picture that said, you know, they pointed between the pins and it said, too narrow here. Right? And so I'm like, oh my God, I have to open this up more. And that was the mistake. Right? Because I should have opened it less. I had that backwards. You should have closed it. Yeah, she should have set that solder mask expansion to zero. Right, zero. And you can set it negative, too. They don't like that because then you can paint over top of the copper then.

**Dave Jones:** But- That's called solder mask. Well, it might have a different name. But yes, solder mask over pad. You can close the expansion whole. And there are some reasons why you might occasionally want to do that.

**Chris Gammell:** What are some of those reasons?

**Dave Jones:** Oh, well, if you want to- I'm trying to think of a practical example.

**Chris Gammell:** I can imagine if you knew the process really well, I can imagine that if there was like heating and cooling kind of differences, then you might spec that because you're like, oh, well, they always leave too much room even when I spec it at zero. Right? If you knew that. Then you might set it to minus one or whatever. And then they would close it up a little bit.

**Dave Jones:** Well, just literally to get larger, like a better clearance, better thicknesses, like a manufacturable thickness on your pad. Oh, you might do it on EGAs, for example. It's not necessarily recommended. But if you go do some research, if you Google maybe what would it be? You know, solder mask closure on BGA pads or something like that. You know, there are techniques. So you can use the solder mask as kind of like an alignment thing. So you've got the larger pad under there because you might have vire in pad, for example. Right? So you might have the vire because, you know, it's so dense. Your package is so dense that, you know, it's vire in pad. And you might close the solder mask a little bit over the pad to help with the ball alignment. Got it. And the solder, you know, and the solder fill in and all that sort of stuff to actually prevent shorts.

**Chris Gammell:** Right, because sometimes they have the ball size, right, is like the maximum width of the ball. And I do want to talk about BGA's later, but it's like the maximum width of the ball, but usually the actual contact of the ball on the pad is smaller because it's, it next down where, you know, because it's a sphere.

**Dave Jones:** Yes, yeah, exactly. And the Phillips form differently than they would with other parts. Right. You know, it's a complex, you know, problem.

**Chris Gammell:** I once met a guy that did a, when I was at Samsung, I was over in South Korea and they, I met a guy who did a PhD in solder. It was crazy. Oh, really? Wow. Solder. Yeah, it was, but like, that was his, I mean, like, you think about the physics of it and like, especially when you're trying to do things super, super high speed or super, you know, you know, high temp or whatever you need to do with it. Yeah. There's a lot of material properties in there. Yep. You and I, we're just slubs that get to benefit from all that.

**Dave Jones:** That's it.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway. Yeah. When, when, what you want to do, the Holy grail of getting your boards manufacturers is you specify everything. Don't leave it up to the manufacturer. Don't go to them and say, Oh, I want three thou clearance on my pads. I've done a video on this where they go and change it willy nilly. Oh yeah. And you know, and they neck down my copper that they actually removed my copper fill around pads. Yeah. And, and that, that actually broke my ground plane in half.

**Chris Gammell:** Yep.

**Dave Jones:** It was like you bastards. Yep. Right. How dare you touch my lap.

**Chris Gammell:** I am surprised at what they, what they are willing to do. Some of it's pretty cheeky. Uh, I've had, I, the one that always gets me is like when you forget to specify, like if you're not sending in fab drawings, which a lot of people don't with modern, like upload services is like specifying where they're allowed to put their numbers, uh, you know, to track the PCBs.

**Dave Jones:** Well, I, I say, I say no numbers. I don't want numbers polluting my board. Piss off.

**Chris Gammell:** Exactly. Exactly. You know? Uh, I once had it where.

**Dave Jones:** Some manufacturers have that option. They have, do you want us to put marks on the board? No.

**Chris Gammell:** Right.

**Dave Jones:** Right.

**Chris Gammell:** Uh, and you can put that in a, in a fab drawing too. Yes, you could. Yeah. I, I saw a example recently where they would put it front and center right in the middle of the artwork and it was an art artistic board. It was like, Oh boy.

**Dave Jones:** It's an artistic board.

**Chris Gammell:** And I had the exact same. So I did the, I did that, uh, the first super con badge. It was just art. It was just a PCB and then people hacked onto it. And it was the same thing where they were like, yeah, why not? Right there, right in the front.

**Dave Jones:** As somebody who's done like PCB front panels for a long, long time. Oh yeah. Right. Right. It's a pain in the ass. Yeah.

**Chris Gammell:** Right. Yeah. Yep. That's a good, that's a good one to know about.

**Dave Jones:** It's almost a differentiator. I'm going to use a service that has the checkbox that's, that says no markings.

**Chris Gammell:** Right.

**Dave Jones:** You know? Oh man.

**Chris Gammell:** There are so many these days. And I, there's just so many. I am not going to list them here. Um, because if I link to them in our show notes, then we like, you think we get a lot of spam email now.

**Dave Jones:** Like, like the number one thing on, on the EV blog forum is PCB company spam. Yeah. Right. Number one thing. They set up sock puppet accounts and they just keep coming. I'm playing whack-a-mole.

**Chris Gammell:** Yeah. Exactly.

**Dave Jones:** Trying to kill all these PCB companies.

**Chris Gammell:** I mean, the thing is like, they're everything. Like, I will say, it is so damn cheap. Uh, and like.

**Dave Jones:** Oh, look, I, I am getting a four board or four, a large four layer board manufacturer, right? Like 30 centimeters by 30 centimeters, right? Quite large. I can get it. I think it's a hundred and I put on Twitter, 175 bucks for five boards of that size, right? You've got to remember, these are not small boards. These are big boards. Normally you pay a fortune for these and they're four layer and it's 175 bucks for five delivered or something, or it's 135. It's ridiculous. Okay. My turn. My turn.

**Chris Gammell:** My turn. Uh, four layer. It's, uh, 180 by 80 millimeters. Yeah. 10 boards.

**Dave Jones:** I'll say piddly.

**Chris Gammell:** I don't actually know. Isn't that the same roughly? No.

**Dave Jones:** Mine's 300 by 300. So yours is 900 square. Or 250 by. Yeah. Right. Huge, right? It's like five times the area of yours.

**Chris Gammell:** Oh yeah. I get you. Oh yeah. You're right. Okay. At least. At least. Yeah. So mine was 135 with stencils delivered for 10, for 10 boards.

**Dave Jones:** Stencils are almost free. It's like 10 bucks for a stainless steel stencil.

**Chris Gammell:** Give me a break. I would say, um, yeah. And if people aren't out there doing stencils, right. Uh, that's, if you're not doing that already, it's yeah. It's a, and if you're not ordering, you know, this is all China. So, you know, your mileage may vary. Uh, you know, do your research. Uh, what's that site? There's a comparison site.

**Dave Jones:** Uh, there is a PCB shopper.com. Oh, shopper. That's it. Yeah.

**Chris Gammell:** So that, and, and yeah, usually we refer people to that. Um, and they've got decent comparison. I mean, honestly, they're, they're doing comparisons. They're also getting paid by a PCB company. So again, take it with a grain of salt. They got, they got advertising. They're up front about it too. Uh, yep. Totally. Uh, but yeah, it's so cheap these days and, and you know, and I love the Osh parks of the world too, like in the Euro circuits and everybody else. So we love them all, but damn, is it cheap these days? Yep. Uh, and I heard six layers are getting cheaper now too. It's just, it's nuts.

**Dave Jones:** It's, it's just nuts. Yeah. Anyway, I've got a design coming up shortly. That'll either be six or eight layer. Oh, nice. So we talked about that before the show, but we won't reveal it at all. Yeah.

**Chris Gammell:** Um, yeah, it'll be interesting to hear, to hear the differences on pricing too, if you start shopping around. Cause I think that's the other thing is that.

**Dave Jones:** The one I want made is not a big board. Like it's like, it's really quite small, but it's going to be eight, probably eight, eight layers. So got it. Very fine pitch BGA and stuff.

**Chris Gammell:** Got it. Yeah. Hmm. Uh, anyway. Yeah.

**Dave Jones:** You mentioned, um, fab drawing before. A lot of people may not know what that is.

**Chris Gammell:** Wait a second. Sorry. I just pulled my calculator out. You said 30 by 30 millimeters.

**Dave Jones:** No, no, no. 300. Oh, sorry. I was talking centimeters. Sorry. I was talking centimeters. I think it's, I think it's 25 by 25 centimeters. That's pretty big. 250 by 250. Okay.

**Chris Gammell:** I was like 30 by 30 millimeters. That's not big at all.

**Dave Jones:** See people like people who've only ever developed Arduino shields, right? They're so used to the pricing on those size boards. Oh yeah. Right. But, but once you go to a larger board, you're taking a whole panel for one board. Yeah. So 300 millimeter wide, you know, you don't get your board for $10 anymore.

**Chris Gammell:** Right. Right.

**Dave Jones:** Right.

**Chris Gammell:** Yeah.

**Dave Jones:** Which is why I was shocked at this price for a four, with four layer boards, five of them at this panel size. Yeah. That's. But this company, I won't name them. Right. This company was, you know, like half the price of anyone, of the next nearest one. Right. Well, and that's what it was like.

**Chris Gammell:** That's what it's good to shop around for. Cause it is those corner cases. Yeah.

**Chris Gammell:** Like some of them are better at six layer. Some of them are better at two layer. That's right. I think it would be interesting.

**Dave Jones:** their manufacturing process is optimized for a certain uh cost and layer size and all that sort

**Chris Gammell:** of jazz so yeah how often are you going to six layer these days or what what puts you over the what makes you like think right at the beginning that you're going to be at six layer is it is it

**Dave Jones:** if i use a bga part okay if i use a bga part it's all but like unless it's a small bga part where you can fan out and i've done a video on this where you can fan out the uh the layers fan them out all on on one or two layers um but once you go to like four or five i think it's five pins deep um on your bga like five rows deep or whatever you're instantly at four layers anyway probably six right and generally you're going to want a ground and a power so if you're using four layers you've just pissed it away so you automatically go to six you have to you need those extra two signal layers

**Chris Gammell:** yep okay so just because that was another thing on my list this week was asking so i'm considering doing a bga and it is a 0.4 mil uh millimeter uh pitch ah and so pretty tight already um yep so

**Dave Jones:** so you think so if you if you heard that it's like a i'd be well as i said it's the number of layers but most likely yes i'd be i'd be thinking you know six layer but but some of them like it like it depends how many pins on the bga how many rows it determines how many rows because you're going to add that sort of pin pitch you can only get one trace you can only fan out one trace from the inner

**Chris Gammell:** row pins right you're saying like escaping past the outer row pins escape sorry yes that's the correct

**Dave Jones:** term yes okay actually escaping those pads out you can only do it and then you know otherwise you've got to drop the vias down and then right then you're doing like via in pad at that point and well i did you you try and avoid via in pad right right because that's another thing that impacts cost right oh yeah it does and you know if you want to do that correctly and professionally then you've got to talk about plugging your vias right oh right then then they've got to be plugged so that the solder doesn't wick down the things when you you know when you when you paste it when you use your solder mask stencil and you paste you know put your paste on those bga pads you don't want to wick in right down and it will it'll suck all the solder down and then you'll get a crap solder you won't get a proper fillet on your ball so you know it yeah one thing leads to another and

**Chris Gammell:** yeah have you ever done videos about about uh breaking out views or uh bgas rather i've done

**Dave Jones:** fan out yes if you search youtube for pcb vga fan vga bga fan out yeah you'll probably find my video

**Chris Gammell:** okay all right i'll find i'll link that in uh yeah you know i just i i don't know why i've never gotten to that point i guess but i mean probably because usually the things i'm doing do not have micros you know what i mean like i guess sometimes they do but if there's anything that big then it usually went off to another another designer when i was at a job or something you know it was never chris

**Dave Jones:** gammel from gammel you're like crick who dave who am i christopher gammel from chris gammel's

**Chris Gammell:** analog life uh-huh remember that i do remember that yeah you my website you know like so yeah of course you don't use you know oh oh you're saying just the analog piece yeah exactly right yeah yeah or like i would be making a plug-in board for an embedded platform that i could just plug into

**Dave Jones:** right so arduino headers stuff like that i just checked and yes if you search youtube for bga fan

**Chris Gammell:** out i am number one sweet uh okay yeah i'll follow that stuff i don't know i i've got another board that i'm doing where i don't know like sometimes it feels i guess the decision around going to bga these days too it's i'm not particularly size constrained in most things i do it's more of a can i do it can i learn it um yep and am i placing it myself i guess that's the next the next

**Dave Jones:** layer just doing it from an educational point of view that's one thing if you're doing it from a needs-based thing it's like the chip i want is only available yeah in the ask bga then you're

**Chris Gammell:** forced to right right well i'm never doing any like the and that does happen a lot with the the super super dense stuff like fpgas and stuff a lot of things you've done in the past right yep yeah i'm not it's i'm not even close to that because the right no when you got to fan out like

**Dave Jones:** a 1400 pin bga you know and it takes you you know yeah and it takes you days and days just to right you know um you know escaping a maze you know yeah right well there's there's auto tools like in i don't know about uh keycat but in altium there are you know automated fan out tools so you can actually just go fan out you know you can put in a 1500 pin bga and go fan it out oh really you know it's not quite that simple but but once you define the layers you've got the constraints and you well you're basically yeah you set your drc so you set your rules and then you set how many layers you want how many signal layers you've got and you just go fan out you know that's nice it'll it'll you know and it's it's often it's a reasonable start you know yeah so but but the good part about that is that it fans it out just outside the package right and then that's where your bga pin swapping comes in right so when you've got such a huge package like that often you've got flexibility because it's an fpga right say it's an fpga like a programmable it's programmable so you've got flexibility in how you do things so once you've fanned it out then what you do is the rest of your circuitry around it you i am sure i've done a video on this as well somewhere is that you use you route the traces in but you don't connect them up uh-huh to to the pins right you just route them in to whichever pin is most convenient right and and then there's a tool there's then there's an fpga pin swapping tool so you run that and then it's it's magic it looks so fantastic when it's doing it and then it matches up because the pads the pads are almost touching and sorry the traces are almost touching right so you've if you can visualize the bga with a all the tracks fanned out and then the trace is coming in but there's a gap between all those traces they don't actually hook up and then it can figure out based on that which ones are the nearest and it swaps all your pins magic and then it joins them all up huh that's nice and it's great and then you can undo that at any point because it actually lays down those tracks as a special uh thing like there's like programming it as a swappable pin as a swappable track so you know so it doesn't you know you can just go undo that and it'll you know yeah at any point that's great you know so would that be every time you use that that tool that that not every if i'm doing a large pin count bga not every time because there's some special there's often there's always special requirements you know you've got no this these pins have to be the correct one in the correct quadrant of the fpga oh yeah because they're often breaking the quadrant of clocks they've got local quadrant clocks and things like that so you've got to you know and there's always you know dozens and dozens of special requirements that you need i'm amazed when this stuff works sometimes you know oh yeah i know it's that's why you know laying out a professional large huge you know pcb can take a month oh sure yeah you know it's not and that's with those fancy tools right yeah yeah yeah exactly you know there's there's just so many little things you've got to do and take care of and things like that you do it step by step and yeah well i saw anyway oh go ahead i want to get back to pcbs for a minute i'm just looking at this company who shall remain nameless but they claim to be china's largest manufacturer of prototype pcbs i'm just stunned at the numbers here that they're throwing at me okay they have over 200 000 customers but this is the stunning bit they get 8 000 online orders per day are there that day are there really that many people

**Chris Gammell:** that are doing that come on that's what they claim i bet what the release i've i've done a little bit of exaggeration on the web myself i bet they're getting 8 000 visitors to their site per day and

**Dave Jones:** they're saying that that's their they're saying online orders they're saying online orders or they

**Chris Gammell:** really are huge i mean like are they maybe they yeah i they claim to be china's largest pcb

**Dave Jones:** prototype manufacturer and it's just it i how would you logistically hand i don't care how many machines you've got how would you right you know how would you logistically handle that many orders so if you're getting 8 000 or let's let's say you're only getting a thousand orders per day let's say it's one eighth of that right yeah that is still a metric buttload of orders right and some of those orders

**Chris Gammell:** by by statistics are going to be for hundreds of boards at the time right i mean it's not going to

**Dave Jones:** be like right it's not like those are all single pcbs either well but this is a prototype house i guess they probably only do prototypes right so uh you know small quantity like single panel everything's kind of you know i guess but how do you like that if you're getting a thousand orders per day that means you have a pipeline of a thousand boards being manufactured at any point and then you're shipping a thousand boards per day you're you're drilling a thousand boards per day you're electrical

**Chris Gammell:** testing yeah how many bits are you going through as well like i mean well granted like you know they

**Dave Jones:** might have 50 designs on a panel oh sure yeah right but still man just just the automation they have they must have in place to do that let alone 8 000 yeah i'm just stunned by that that number is just

**Chris Gammell:** ridiculous we're out of our element dave yeah i know it's just we guess we won't be starting a

**Dave Jones:** low-cost board house anytime soon right so if i if i'm going to go visit a pcb house in china um i'm

**Chris Gammell:** going to go visit this one holy crap i want to i don't know if i want to go to like i want to go to a lot of places in china i don't know if a pcb house would be one of them yeah it takes the magic away no i mean i just want to be the one of the chemicals you know like yeah well that's it oh yeah like it's

**Dave Jones:** a filthy dirty right exactly right yeah it's horrid and you know it's just yep yeah anyway

**Chris Gammell:** well speaking of uh boards did i see that you were using ki-cat again did did i well yeah i had a go i did

**Dave Jones:** a one and a half hour no no it was like a three hour live stream was it uh-huh i don't know it's on my second channel you can link it in yeah i did a yeah of me literally installing it and uh using it

**Chris Gammell:** i just jumped ahead and i'm like oh a half hour in he's still he's still installing okay

**Dave Jones:** was i oh well i was talking about it was kind of an improptive live show no no no judgment here man and uh was was that on twitch or was that on youtube i think it was youtube maybe both okay

**Chris Gammell:** yeah anyway well what did you think i mean coming back to it you were oh i was like it it didn't piss

**Dave Jones:** me off all right hey moving on up in the world like there was something you were using someone else's design too right so that also i was importing someone else's design i wanted to make some small changes that comes on to this four layer large four layer board that oh god if you watch the video you know exactly what i'm doing um yeah i just wanted to convert it from a two layer board to a four layer board yeah and in the end like and and i estimated that if i wasn't doing the live show right which is you know interacting with people and doing it if i was just sitting down focused doing this installing ki-cat and loading that board in and converting it figuring out how it works without watching any tutorials or reading any manuals or anything and changing it from a two layer to a four layer board adding ground planes and doing the whatnot um i figured it would have taken me i

**Chris Gammell:** don't know less than an hour no but that's as a as a long-time designer i think that's as a long-time

**Dave Jones:** pcb designer which can often be a hindrance because i'm expecting things to work in certain ways which was annoying things i found in the software and quite frankly they there was some yeah oh well i don't think

**Chris Gammell:** anyone's it's not a stress to say that you know ki-cat has a bunch of quirks and ui in in in terms of ui yeah yeah yeah but the same thing happens to me with altium so every time i'm like okay what the

**Dave Jones:** hell am i looking at well altium has uh inconsistencies in terms of many different ways to do things

**Chris Gammell:** right the same thing right it's famous for that years of baggage right that's what yeah yeah years of

**Dave Jones:** baggage yeah years of years of direction changes in development but because we actually released it oh we can't just drop that so we choose a better way to do it and it and the old way to do it's still there so you know yeah so it has all that baggage uh but ki-cat has inconsistencies in in terms of uh you know um it working one way with one object right and you expect it to work the same way with another object but it doesn't right so clearly somebody hasn't thought about that yeah even just no no i'm talking just at the pcb level oh really yeah i'm talking just in the pcb tool it was like i could you know i could double click to edit that item but i can't double click to edit this item it like that doesn't you know that's inconsistent and i find that infuriating you know

**Chris Gammell:** who double clicks man mouse over hit e it's the hot keys hot keys are life anyways yeah that's just quirks yeah okay uh i was listening to an interesting conversation between our two rival podcasts so they uh the embedded and macrofab crossover show um right and it was very interesting how many how many viewers they got uh well the listeners they're listeners listeners listeners um i i don't know dave uh right uh uh but it was interesting hearing parker and steven uh try and explained so and they're the macrofab podcast is parker and steven uh explained to alicia and chris of embedded fm uh why why hardware uh footprint libraries aren't like software libraries and right i i was kind of i was it was nice i was doing what our our listeners are probably doing during this show very often i was yelling at my radio uh uh tell us it was just like it was just you know but it wasn't yelling actually it was just like i was just kind of like nodding along nodding along nodding along it's like ah oh they missed it uh but it was basically alicia was asking about like why why doesn't this happen why can't it just be more like software and right uh the answer is because the interfaces are different and because there's no way to verify in my opinion so like uh there are no universal footprint tools for you and i to both share right right and if there were if there were standard apis whatever that would be in hardware or visual i suppose then we might actually be able to do it but i i think that that's ultimately where it comes down to is like because there's no standardization between tools it would be like if uh if like oh boy i'm gonna get myself in trouble here if different idees uh displayed characters differently and right right like or like if uh so you write a library in c but iir only allows spaces and kyle only allows tabs now people are yelling at the radio you like that you can't yell back we can't hear you dave can you hear them i can't hear them uh crickets but it would be like it would be like the same it would be the same library but it would be displayed you know like it wouldn't accept it right and uh i think i think ultimately that's the answer maybe

**Dave Jones:** you have other insights on the on the library thing in in terms of you know you're talking about the holy grail of right ecad which is reuse right right of course reuse and that was old altium's you know nick martin was absolutely yes positive that oh yeah no you wouldn't need to lay out your own board in the future that was the you know at one point that was the key marketing point for altium is that no the future is going to be people don't lay out their own boards right everything's been designed everything's modular you you need a power supply you drop it in it's done including the layout it's like

**Chris Gammell:** and you know right and that's also continued by our our mutual former co-worker matt bergeron who's now running eagle and right and he's actually making some strides towards it i'm actually pretty impressed with some of that stuff so some of the eagle stuff he's actually doing like some module based things where it's like oh i need like a power like you're saying a power supply and it's it's within eagle but it's you know it's click and it kind of pulls in the schematic block and it pulls in

**Dave Jones:** the layout block it can make sense but once you once you step out of the easy peasy cookie cutter design which is most designs 99 you know like of any industrial design no you've got to do something

**Chris Gammell:** different well yeah and i think the other thing too is that is the vertical nature of it all right so so and and that might be why matt has a shot at it because you know autodesk is pretty uh monstrous uh and you know like having vertical integration where like if if you can actually get every vendor to go for that then maybe right but more than likely they're they have to play multiple fiddles as well right so they have to you know a ti of the world not only has divisions within their own company but then each company you know like some of the designers there are using altium sometimes they don't provide any footprints sometimes they don't provide anything and it's like but yeah

**Dave Jones:** well the other thing is most professional pcb uh layout engineers are highly creative and protective of their creative work so it's like um it's not invented here since rome it's like you've given what you you want to give me an example pcb layout and you want me to just drop it in piss off i know what i this is like this is art to me you know i'm you're not going to tell me you know how to paint a picture and i you've given me a quarter of the picture then i'm just going to build around it no bugger off you know

**Chris Gammell:** well i'm okay with uh wow oh wow my voice just gave up um i'm okay with a lot of like example designs but i'm not sure about the exact thing of course yeah yeah and i've i've done collaborative designs

**Dave Jones:** before not not by choice by you know force where somebody lays out one half of the board and i i lay out the other half and it's like it it never works it never it's stretching it yeah stretching it it's stretching it yeah yeah yeah yeah but at at the end of the day it's not like you can just bring the two together and go and then publish right well you know send that to manufacture somebody at the end of the day has got to take that board and then tidy the whole damn thing up to make it kind of you

**Chris Gammell:** know yeah consistent well and i think i mean i think there are strides too so i think that like uh on the footprint side right so and that's ultimately what what they were talking about that

**Dave Jones:** oh the footprint side is is is mainly doable at least it gives you a decent start like there's nothing like there's there's nothing better than the action you know like i don't want to have to

**Chris Gammell:** create footprints right right and well and there are there are strides towards that right so like ee concierge is um former upverter um zach uh from upverter was doing that and now it's part of ultium um natasha from snap eda is working on that as well as a third party offering there's always been that uh universal librarian what's it called uh something like that universal librarian something with librarian ultra librarian um so all of the all of those are potential solutions and you know a lot of them are pay per footprint though so the most people then go oh i don't want to do that you don't

**Dave Jones:** want to do that right right but but but for a big company that can save you time right right right it's replacing the librarian right i mean we we had that inside that was the luxury i had inside outium it's like oh i need this new uh you know 1500 pin bga part please and i want a 3d model with it thank you very much and we had people who would do that and that was great you know because that just you know took so much time you know saved so much time especially on the schematic people think it's just the the footprint it's not it's on the schematic symbol side is a big deal as well 1500 footprints you got to put that on both right yeah but once again you may not be happy with the foot with the uh with the schematic symbol you know you may like it may not have the pin flow you want you might be a fanboy of having all the inputs on one side and all the inputs on the outside or you might be a fanboy of having the pins actually match the physical layout of the door and all you might go or you might swap between those depending on the requirements right you know so yeah but at least you've got it there ready to swap around you know at least you can like it's much easier to go in there and just move the pins than it is to create them all from scratch and you know check it and all that sort of jazz so right yeah this saves a lot of time if you can if you've got the part already existing so yeah oh totally there's a there's a lot to be said for that yep hmm yeah i mean and

**Chris Gammell:** yeah at the end of the day it's like i don't know i so and they were also talking so so the the embedded macrofab crew is was also talking about like it and i was kind of on parker's side and you know i've talked about this on the show and the two i'm just paranoid right and i'd rather at the end of the day i'd rather be be the person that messes up versus having someone else mess me up and i

**Dave Jones:** know that sounds stupid but but you've been when you've been bitten so many times it's like i've

**Chris Gammell:** bit myself man yeah yeah exactly yep i don't know yeah it's it's just it's not a solved problem yet but it's it's getting better so take take take uh take hope folks yes it is yeah anyway yeah so i've

**Dave Jones:** got sitting right in front of you and i have in my hot little hands what's that my custom lcd oh i saw that on twitter how did it turn out yeah if you well i haven't actually seen the segments yet i haven't actually lit the thing up okay um i i could just manually do it on a breadboard here but uh david's working on the software to drive it got it um so once once we've done that then uh you know he built up a little demo board and we got is it is it a standard driver for that thing or how do you actually drive that oh we're using now well if you watch my previous video you would know my part three or whatever it is i haven't been sleeping much lately even when i watch stuff i don't remember it that's all right it's uh we're using a whole tech driver it's what is it the 61 oh god i forget the number sorry but um anyway yes i'm we're using a whole tech um lcd driver chip so it's an eight common 32 segment driver and we've got eight eight commons on this i think and uh i can't remember

**Chris Gammell:** the exact details i will link the video in at the very least and maybe i'll re-watch it just for you

**Dave Jones:** there are some there are some micros that have enough commons and enough pins to drive this but you know it puts you in a different price category i think we've discussed this before it was cheaper to go for the external driver chip than it was to move up to the next level of micro needed to have enough pins to drive this right so there were you know it was just a cost and pcb trade-off it means that you can you know the micro can be on one side of the board and the lcd driver can be on the other and there's just a spy bus between them you know it's much easier from a pcb layout right

**Chris Gammell:** and signal integrity and everything it's not super fast no no no no it's not fast no right so it's not

**Dave Jones:** but you know just from a layout point of view and you know it's just a nicer to segment your design like that uh and rather lock you into some uh because the problem with micros is like the problem with be um with fpgas right the the problem with fpgas the time-order problem is that if you want more logic elements right if you want to put a big design in there you have to get a larger number of pins

**Chris Gammell:** oh yeah right you've talked about that before right right well you know it's it's the number one thing

**Dave Jones:** that you know and every time you talk to the fpga vendors about it they all go yeah i know everyone complains about it sorry right you know and yeah so i think yeah even if they just were completely

**Chris Gammell:** consistent within a category but you're right it's just the marketing they only they only allow so many

**Dave Jones:** crossovers within an area and they just said sorry there's just not enough market for that for people who want a huge number of logic elements and 20 pins you know it's just anyway and and it's kind of um the opposite for the microcontroller if you want more pins well no it's the same thing if you want more pins right because you've got to drive all these lcd things right you've got 32 pins just for those plus the eight commons so you've got at least 40 pins dedicated to the lcd right right then if you want the larger pin count that has the larger number of commons with the lcd driver built in you have to go the larger package and the larger package comes with bigger memory right it comes with 128k of sram instead of 16k and you're paying for the bigger die yep to get that you know so so the chip is like three times the cost and that's why for us it's cheaper to use the external lcd holtec driver chip right than it is to find a bigger micro in the same family well i'm guessing the holtec chip is probably a little older too right oh it's older and it's dedicated and it's used in all sorts of things right you know commoditized over commoditized just bought a high whole tray of them for a hundred bucks or whatever yep yep so anyway um yeah it's a trade-off but then you've got another bomb item right and then you've got another thing that could go obsolete and another thing that could go obsolete you might have supply problems with that so you know and it's not a readily available chip right we can't buy

**Chris Gammell:** this a digi key right right so it's you know you have to buy it at quantity from from the distributor

**Dave Jones:** or from a from the actual manufacturer we got at this in this case we got it from the distributor found a distributor with stock and uh we just ordered those and they came within like two days oh nice it was great yeah and we bought a whole whole tray of them because they were so cheap we thought well we only need like five of them to get our prototypes but hey we might as well order a whole tray of 250 of them you know yeah right like right yeah so okay anyway yeah so we're doing that so i haven't yeah um but let me i i sent you i just sent you on uh googly messages um the manufacturing process flow chart for manufacturing and lcd have a look hello

**Chris Gammell:** we've lost sorry no no i'm here sorry i had a mute uh so this looks like uh wow this looks like a

**Dave Jones:** quasi chip process almost yeah basically and this is one of the comments i had in when i did my previous lcd um you know do it yourself lcd video somebody commented that oh why don't you just make it yourself it's so easy look at um look at the applied science channel there they did their own lcd look

**Chris Gammell:** at somebody else did their own lcd right and did one yeah sure yeah you know yeah one segment also

**Dave Jones:** look at the chemicals that are used here yeah exactly look at all the processes i'll count them two four six eight ten twelve fourteen sixteen eighteen twenty twenty two twenty more there's about

**Chris Gammell:** 35 processes expensive as an employee but he ain't that cheap you know and he's not making that many

**Dave Jones:** yeah yeah let's let's call it like 35 different manufacturing steps cleaning and photo is this coating exposure developing etching cleaning polymide caution code caution coating oh oh yeah coating yeah curing mercury and break off heating burnish visual electrical inspection cell scribbing whatever the hell that is scribing yeah yeah scribing um you know and it's probably like actually

**Chris Gammell:** out outlining like the actual cell so that it right yeah oh so

**Dave Jones:** that the ink stays in the well yeah exactly right yeah yeah wow this is this is cool though right yeah and and i got these i got five samples right for a hundred i think it's 135 us dollars including the tool in charge yep yep including the tool in charge right yeah it it actually took quite a long time to get them it's not a fast i mean you know if you want to be bummed up the process

**Chris Gammell:** there's not eight thousand orders coming in a day no no that's it right but like it and like to think

**Dave Jones:** that you could possibly make your own is is is just ludicrous just like you can't make your own four-layer pc you're just mad if you try and go and make your own even two-layer yep pcbs you're just mad i agree right unless you have some specific requirement to get it that day or you know i like

**Chris Gammell:** yeah it's just no it's just oh you're talking about like uh uh what's it called board milling

**Dave Jones:** oh yeah board milling but but then you don't get your plated through holes which you there are processes to do that but then you don't get your solder mask but there are processes to do that and it's just such a involved messy process why would you do it yourself when it's dirt cheap yep and these and this is a manufacturable part i can now even though there's samples i could go drop this in a in a finished product right right i mean it's just it's just incredible like it's it's the it's the real deal yep um so i'm not sure if there are slight differences between the sample manufacturing process and the full production uh process like you know i'm not sure if there's you know like if the ink's not as good or or or whatever right i'm not not sure of the deal there but

**Chris Gammell:** jeez it's like come on 135 bucks i'm guessing that the person that said that did not uh does not manufacture many things that's no they don't that's what i have to guess uh you know i've been

**Dave Jones:** on the internet once or twice but but it's a reasonable question right they it was a question right it sounded like an accusation you know no no no it was a statement it's like i saw somebody do it on youtube so why don't you go do it right kind of thing you know it's like yeah they made it look easy yeah but they didn't mention the 20 steps they had and all the specialized gear they had to produce which is you know i don't want to take anything away from it's brilliant that they made their own oh sure sure sure lcd and whatnot you know it's like the you know the kid who made his own chip yeah yeah fantastic sam who's been on the show right yeah exactly sorry i forget his name right sam's a loose yeah sam's live and like absolutely brilliant hats off you know we we are not worthy yeah but sam wouldn't have said that he would do it as a production thing either right someone went to him and asked him but people see this that's the problem people see the final video and they go oh geez you can just do it yourself yeah but people also see

**Chris Gammell:** wrestlemania and they they go and you know suplex someone in the backyard you know then they break their neck right so yeah right don't suplex people wrestling isn't real oh dear oh dear yeah no it's real but it's well it's done by professionals though and it's done by

**Dave Jones:** professionals they've trained for years and years exactly do it without with hurting themselves minimally right it's still bloody hurts yeah that's true that's true um you know right they get paid for yeah yeah but they get paid for it yeah and they know how to fall with it do you know that the

**Chris Gammell:** worldwide western the worldwide wrestling uh whatever it is wwe they're actually wwe they're a public company did you know that now are they i didn't know they're a public company now isn't

**Dave Jones:** that insane how do we get on to wrestling i'm i'm a bit of a wrestling fan boy because i grew up in the 80s well i grew up in the 80s you know i grew up in the hulk hogan era you know i mean it was

**Chris Gammell:** in the 90s i used to watch tables ladders and chairs man that was like a yeah right that was the thing that was the pay-per-view yeah yeah young whippersnappers i would not have guessed we would have gotten under wrestling today no no no you know never could have guessed electronics is like wrestling in that remind me to fill something in there later no you're on your own dude i'm gonna leave you hanging uh yeah in that sometimes it's not real uh isn't this like a couple episodes in a

**Dave Jones:** row we've mentioned wrestling no didn't i i mentioned outback jack the other was i'm sure it was on this

**Chris Gammell:** show yeah you might have yeah you might have mentioned that but i don't remember why no

**Dave Jones:** no no sorry no no no it wasn't on this show it was on a live show oh it was on one of my live shows sorry i did yeah got it because we shoot this live in quote marks right right you know or shoot we record this live in quote marks yeah uh hey so i want to get back to those boards too um

**Chris Gammell:** so the thing that i was looking at putting a bga on like i said it was just a challenge but it was just a so i was gonna actually put it next to a monster one of those monster um not monster 16 by 16 millimeter uh laura modules the hope rfs have you seen those yep so that's like what's on the monster that's not like i know how tiny is that well but the the the micro that would go next to it is a two by two millimeter and the cortex m0 so that's why it like two by two millimeters yeah that's a micro that's a that's that's a micro controller yeah in what package let me look it up i think i have it here somewhere um like that like i said it didn't need to be that small but i was just looking and i was like oh well i've never done a bga so i mean that must be

**Dave Jones:** like an eight pin package two millimeters by two millimeters it must be like one of those little

**Chris Gammell:** wrong about this like sc23 packages or something it was it was a w a clsp yeah the chip scale package um it was a 35 pin so it's six by six with one with one removed hold on and it's a two millimeter by

**Dave Jones:** two millimeter package hey where's this thing are you are you sure about your no i'm not sure about

**Chris Gammell:** it at all uh it's the sam d 21 e 16 b so if i click on that here's the digi key page for you okay uh it is where do i check the size oh sorry please 2.82 by 2.53 sorry ah right so two and a half by two and a half pretty much but yeah it's a x it's way too small wl csp so like it's like the dumbest one to start with probably right i should be doing like a 0.8 millimeter pitch or a one millimeter pitch but they don't yeah but i wasn't looking at that you know what i mean and i just i was looking at this as like a a thing you know it's just like oh bga i should try that you know that kind of thing

**Dave Jones:** so yeah maybe but it's a bit of a world of hurt really right well totally yeah right yeah yeah yeah it just changes the requirements of your design for no good reason exactly exactly if you have a good reason for it like i've used packages this small but you know for good reason right right you know because i could just as easily go to a qfm because they're going to be implanted in somebody's head right you know size right right right right yeah you know it's like yeah it really

**Chris Gammell:** matters but yeah yeah no no i i i doubt i'll end up doing this but i i was just looking at it and i don't think i think that is the one they make but this is definitely chip scale so basically this looks like it's bonded maybe maybe it's flip chip i don't know i don't think they do that for the little micros but um it's small uh but what i what i was getting at really though is uh mentioning that hope rf module i was wondering did you ever end up getting your laura gateway working no i didn't you

**Dave Jones:** didn't what was the i know sorry i didn't follow up the guys offered to come in and install the firmware and like it has to be it had to be custom firmware because it's it's an australia specific thing oh really hadn't yeah it was some issue with australia and the compilation of the code wasn't compatible with here or something and they had to do like a custom compile or something okay and yeah they i think they offered to come in but i i never followed up on that i just so that was the things network stuff at the time that was the things network yep okay um i was bitterly disappointed that it just didn't work out of the box like you promised it would i didn't promise that i even bought the one you recommended you went this is the dark scouts i i just said that's the one that i

**Chris Gammell:** talked to richard about on the show so right anyway on episode something something which i'll link below uh uh yeah so that's too bad though okay i'm just really so like i'm interested in the that i have i've communicated between modules right with just the laura protocol not even protocol the with laura chips right uh and that's what 915 megahertz and you use the same ones in australia right yeah yeah so it's 915 here 915 there 868 in europe right um and so i've communicated between the chips but i have not i've not set up a broader like um network or laura wan which is the which is what we talked about

**Dave Jones:** in the past yeah so uh okay well so you're just leeching off someone else's um access portally

**Chris Gammell:** thing are you yeah well that would be i mean like hopefully this would be both modes but like so being able to talk between them but also maybe setting up a little a little wham network well i i don't know uh right i i'm still pretty early in the process you know come back to us when you do know got it okay right if there's one thing about amp hour it's only the finest most complete thing that we

**Dave Jones:** discuss on here dave finest high most highly researched right yeah yeah right right speaking of which we're just gonna go in and because we're almost up wow yeah too much pcb talk on topic yeah oh virtual high five all right for us and um yeah so we'll now talk about things that we have not researched and uh yeah yeah look i'm sick of these like i don't like a kickstarter what is it kickstarter have a new studio badge hardware studio badge on projects oh yeah where they're teaming up with avnet and drag and we've had dragon innovation on the show and they're good but i like yeah so

**Chris Gammell:** that's scott miller we've had him on the show yeah um and that was a great show yeah like but but

**Dave Jones:** it's up to well avnet this has failed on indiegogo and on kickstarter before like you know it's been avnet approved right so oh oh it must be a good idea the problem is people see this badge as that this is a good manufacturable you know like they're gonna like a good product idea and they're going to be able to deliver on the product whereas these people these companies who certify this don't give a shit about that all they go is yeah we can buy all the parts no problem they're going to be able to manufacture the hardware right you know we've also talked they don't vet the idea and the

**Chris Gammell:** yeah you know like the concept of it well so we've talked so when zach donald was on the show too so zach runs some of the hardware stuff for kickstarter and so he's involved with this um and so i think in general i i do agree so like i like what zach's doing and i the last i had talked to

**Dave Jones:** him about it was i would trust them more than avnet yeah i trust them more than avnet you trust two more i would trust them i would trust dragon innovation uh dave i hate to tell you dragon innovation is

**Chris Gammell:** avnet they got blocked by avnet they are yes oh well okay all right thanks for that right okay got that right in the yeah so dragon innovation has been so if people listen to the show that was scott was on many years ago but basically scott used to be at irobot but then he was basically helping take people take designs to china and doing introductions in factories and stuff like that and it it's a service right it was basically like a consulting service around that so then they've been moving into software they got purchased by avnet avnet is a many but tens of billions of dollar distributor large octopus right it's avnet and arrow are the two big distributors in this in the states at least and maybe broader worldwide um so a lot of people know those names but um like you said indiegogo and arrow did that kind of verified by now this is like a verified by yeah i i i don't know it's just

**Dave Jones:** like it's a c like people see this as a seal of approval that this concept is going to work and and the problem with the kickstarter and indiegogo fires is that the concept is just you know like stupid right it's just not going to work wait dave you can buy the pass tell us how you really feel right well you said i'm wasting my time on the debunking you know oh what so you have to do it

**Chris Gammell:** right like oh it's just so what is what is the problem here so so you don't like that there's a

**Dave Jones:** badge i get it um well no like it's not bad in that but it doesn't really to us in the know right we we we know what it means it means oh they've checked that they can buy all the parts and they're all

**Chris Gammell:** available whoopty freaking do right i think you know like that's if that is all it is then that's that's not enough right but but at the end of the day it's been up until now well so like they they have a big picture on this digital trends article about the coolest cooler right but like how much of that is i mean like there's sourcing nightmare right i mean that's a huge right what is it injection not even injection molded right that was probably vacuum formed like those huge things i mean it's almost like you you almost have to base it on well luck and you can't really calculate that you need to base it on like past experience like have you lined up all your suppliers is your supply chain in place you know is your cash flow secure did you get good payment terms and like all of these things like i don't think they're gonna would they even showcase that to uh the audience i don't think they would honestly the thing that i wish they would show is that they showed like how many are in stock when they start the kickstarter right yeah because that's even even that doesn't matter

**Dave Jones:** because someone can come along and gobble it all up right and it's gone and then oh no no sorry i

**Chris Gammell:** mean how many finished products are in stock right so if you show that you've built a hundred coolest coolers you at least know i mean like and that's still not a guarantee right going from a hundred to a hundred thousand is a huge scaling problem and you might have to find a whole new factory they might just be like no we can't do that what are you talking about you know yeah i know right you might be going to a prototype pcb fab like we talked about and you need to start going to a you know a large scale fab and like it's just a whole other set of constraints but my yeah my problem is not so much

**Dave Jones:** oh they couldn't deliver because they had logistical or some other problems like shit like that happens it's you know it's the promise like the batterizer for example that just promise all these ridiculous things that are just demonstrably untrue yeah you know yeah and i think that is kind of the problem is

**Chris Gammell:** that basically it requires a subjective view and i don't think companies are going to do that right because no at the end of the day because that's not their business right people want to get paid regardless and i think that yeah this makes sense for you know an avnet in the first place because if you know it's good marketing for sure and if uh if these campaigns go through uh that's good because they sell more parts but honestly it's probably peanuts compared to like you know if avnet's serving like uh you know a huge industrial customer in the midwest uh as they may have done in the past you know like it swamps every project on kickstarter combined you know so it's probably mostly marketing which is fine we we get that um no yeah it's getting their name out but i think i think honestly the the the the thing i my personal view on it is that it's better than nothing um and if someone came to me and said well we have this sticker i'd be like okay great you know like you've checked a box

**Dave Jones:** see that's the problem it allows the marketing to take hold it's once again it comes down to like a batterizer is a classic example of this right they went and got the thing ul tested right and then they marketed the shit out of that look this is real ul tested it they're the most reputable company right with a hundred year history right right and then use that to prove that their product works right in quote marks you know right actually that just means your house won't burn down or that

**Chris Gammell:** ul guarantees your house won't burn down which is like okay and yeah it was total and utter bullshit so dave is this like is this a market opportunity here we could like start a give us your spec sheet

**Dave Jones:** about this years ago we did oh man it was like yeah we talked about doing this third party well no you talked about it'd be like yeah well right yeah i kicked that yeah which a couple of people have done or something and a website but not any website but i you know i briefly flirted with the idea of like a service where i would vet your idea right and then i would go yeah this is not full of shit right right you know it'd be a you know a no bullshit stamp on your you know it's still a stamp it's still a stamp right and then i realized no that's just a world so what do you think okay

**Chris Gammell:** maybe taking this objective out of it is there an objective way to look at this though because i i i don't think at the end of the day there is right there's no way you can tell like no one predicted there's a capacitor shortage but there is right and it's like i know that that's why i say i don't

**Dave Jones:** blame any uh necessarily blame any indiegogo or kickstarter projects that that you know fail because of logistical problems or whatever i mean you know shit happens i mean shit happening on my own kickstarter you know so i can't you know yeah blame other people right so i just blame you man for that i mean that stuff happens it's when you know the thing that gets under my skin is the

**Chris Gammell:** bullshit right right just just the badging and nothing else right yeah it's yeah that's difficult i don't know if like and i think i've actually talked to zach about this because he comes to town here and i i like talk i mean like i do like talking about this stuff like it would there would be a very big benefit if if there was a um you know if there was a a true way to to prove that there was

**Dave Jones:** you know a likelihood of success right yeah well see to me it's not necessarily the success it's the problem that needs to be solved in indiegogo in particular are the bullshit products yeah but that's a different problem i think like yeah well they are two different problems they're totally

**Chris Gammell:** different problems but yep um yeah i agree that i wish they would i mean i saw a good campaign the other day but that's yeah that doesn't absolve the other ones right so that but that is a different

**Dave Jones:** issue i think yeah but yeah the problem is yes you're right in that yeah this is going to help right it helps on the logistical side of things right it can you know there's things you can do to help there and this is one of them right right to help ensure that not not ensure that's the incorrect word help the chances of a product actually you know being delivered in a reasonable

**Chris Gammell:** time frame to a reasonable quality right if i was going to do this i would i would take cues from my elementary school teachers and i would set up a rubric what's a rubric it's like uh um oh man you never had to do rubrics huh uh it was like it's a scoring system for something and basically i mean it's just a scoring system really but it would be like in different categories you know you might set from one to five right so it'd be like supply chain readiness you know do you get a one two three four or five and then uh you know founder uh so like a kickstarter uh what's it called uh pedigree like pedigree of of the founders right so like have you built something before one two three four right and then basically the end of the time you get like the score and you could maybe promote that but again like the objectivity is so tough there right because if if someone came in they're like well i'm uh successful you know i've i've started up three clothing lines uh and now i'm going to be making electronics like they've made stuff but has it been in the electronics industry it's like i don't

**Dave Jones:** know but even if you're the world's most experienced person you can come a gutzer on a single part sure right how many parts are in your average electronic product a hundred right yeah on on average easy right right you know like in any any one of them can become a well a good majority of those can become a showstopper yeah totally i for whatever reason you know i have written about this in the

**Chris Gammell:** past dave yep yep so i shit happens for uh what do they call it uh uh hardware design first be perfect uh what first be perfect yeah the first step of of any hardware design is to be perfect

**Dave Jones:** is to be perfect otherwise you can't you know less than perfect doesn't work right exactly exactly

**Chris Gammell:** right that's that's the hard part of hardware right is like it is like there's occasionally yeah if

**Dave Jones:** you've got a capacitor shortage okay you might be able to do some things substitute some stuff you might even be able to leave a few caps out oh yeah you might be able to even do some muncing muncing yes right you know like there's but some other things like like my if i can't get this lcd controller chip i'm screwed right right there's no other way around it right oh you start from scratch right yeah i i would have to i would have to maybe you know let's let's take that last thing we'll do on the show today let's take the case okay i've got 10 000 bare boards manufactured right so i don't want to go like and everything i've got all my parts for my new micro supply right and and and the kickstarter people are breathing down my neck and i need to solve this but the company you cannot buy this lcd driver chip anymore you've exhausted all the supplies in all the world right and it's a six month lead time to make new ones all the company folded they discontinued whatever right or fabs burnt down that was the only place they made it right that happened with the uh hard drives in philippines yeah earthquakes tsunamis whatever you know like yeah that shit happens right and okay so what do i do um i you can redo the board right you can re-spin the board to use a different microcontroller to do that right but let's say i've already yeah but let's say i've already got 5 000 boards made and populated all for the except for the lcd controllership right so you don't want to throw away all that i think

**Chris Gammell:** even worse than that what if you already got what if you already got compliance right what if you already got yes right fcc compliance on something and you're like okay now i'm making 10 000 it's like oh my

**Dave Jones:** god right so what are you doing that case well what i would do is probably um find another lcd controller chip and then build a daughter board like that get sold to that on a daughter board which then hopefully it's a large a smaller footprint than what's you know because that'd make it easier um in this case it's not anyway it's just to see you know and then you can bodge that onto the board

**Chris Gammell:** right and someone says 10 000 times you have to do that you'd be like well it's cheaper than starting

**Dave Jones:** over it's cheaper than scrapping you know yeah exactly it's cheaper than redoing the whole thing you know i might have changed software of course but you know that's nothing right you just change

**Chris Gammell:** your lcd driver you were describing my old life at keithley instruments of dealing with obsolete

**Dave Jones:** parts on a regular basis yeah component obsolescence engineer is a real job yeah yes it is and yeah so that's what you would do you know there's ways around that but right you know but at that point right

**Chris Gammell:** if you're if you're like looking at it as a judgment on a kickstarter project at that point you're

**Dave Jones:** already late right you're oh yeah yeah you've already got a timeline of yeah yeah like i'm i'm three months late you know i i promised delivery in march april may yeah i'd know in technically end of march i think i promised okay for the main backers i was yeah i think i was two months late for the first backers and now i might be three months two to three months late for the second backers but

**Chris Gammell:** yeah and that would be another thing that goes on the rubric is like all right well dave has dave has delivered what two two kickstarter projects on time delivered two kickstarter projects right you would get a four for that uh maybe a four for past updates right but it doesn't matter at this point right i mean it doesn't matter shit happened right you know like right we had no

**Dave Jones:** visibility that that the range switch was gonna you know that there'd be that technical hiccup in the final product we had no foresight to that no one could have right yeah so i guess that's a good

**Chris Gammell:** question too is like would would a stamp on the board or sorry a stamp on your page have mattered in that case and i don't think it would have no right no it wouldn't have right well you know i mean

**Dave Jones:** you know the the project is shipping now you know it's not like it completely failed right we're shipping we're just late you know just a couple of months late yeah um but yeah i yeah but but the problem it it looks and feels worse than it is this failure to deliver this kickstarter you know because the kickstarter finished in december right and now it's may so it feels worse but but the promised dates aren't that far out you know yeah like it's not it's not six months late you know so but it feels like that because it's the well you've been thinking about it for so long right yeah yeah exactly right so it feels really bad from my perspective and maybe from other people's perspective but they don't take

**Chris Gammell:** someone who's purchased and put down money and yeah yeah back in december they paid their money back

**Dave Jones:** in december but they you know don't take into account that oh it was always a march delivery you know it was always going to be end of march was the promised delivery date so it's like you know so technically it's only a month and a half past at this stage you know yep so yep and we have ships up so technically it's yeah it's a month and a half late on the second backers so you know yeah but it feels worse so there you go hear that folks dave is dave is feeling regret it's yeah dave has feelings too bit frustrated yeah you know yeah yeah anyway yep all right man and we can't and the problem is we can't ship them all at once i wish we could like ship right 2 000 units in one day but we just

**Chris Gammell:** yeah well logistics are a thing just can't yeah

**Dave Jones:** yeah and and and the manufacturing pipeline you know these things take a long time to calibrate each unit you know they've got a color you know some you know and there's a human somewhere in a calibration house that has to calibrate every range of every unit there's like i if you look at the calibration sheet there's like a hundred different calibration points that they're all you know

**Chris Gammell:** yeah i used to work in test equipment i actually know how that works yeah yeah yeah you know all about it and it's a complicated i've been in that room i've sat in there many nights uh time consuming process it is it is yeah it helps when you charge a lot per unit uh oh yeah yeah exactly

**Dave Jones:** no so there's a throughput limit there right you know right how many each one needs a new test stand

**Chris Gammell:** and doing its own thing right so anyway i'm sure i'm sure we could talk in the future about uh the the the beauty of self-test if possible right oh yes yes we can maybe we should schedule that for

**Dave Jones:** the next show yeah that sounds good buy it buy it what built-in test equipment oh you didn't call it that no no or bist built-in self-test no i called it no you'd never use the acronym slither oh what's what slither slither slither what does slither stand for no nothing it's just what you're saying at the beginning of the show okay right okay very good segue taking the piss yeah right or whatever the term's called when you bring back a joke from what's the term called is it does anyone know the term for when you like you know you're doing a one-hour stand-up comedian in comedy show and you're like and you say something you know earlier in the show and then you mention it later yeah there's got to be a word i'd say that's a callback yeah oh callback is it okay right yeah it's a callback

**Chris Gammell:** joke okay all right man well i will call you back next week how about that yeah boo all right i guess

**Dave Jones:** i'll still be yeah talk to you later catch you next time

**Chris Gammell:** okay take my take my amp hour pills amp hour pills yeah this one this one is the the snark pill what pills are these and this one is the piss and vinegar pill what's that oh they're both just slang on no they're both just vitamins right

**Dave Jones:** yeah you you
