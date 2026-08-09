---
episode: 209
title: Headless Units and Baseless Batteries - KiCad Kickoff Kopophobia
url: https://theamphour.com/209-headless-units-and-baseless-batteries-kicad-kickoff-kopophobia/
---

**Dave Jones:** This is the F-Hour Podcast, recorded July 28th, 2014. Episode 209. KiCad, Kickoff, Copaphobia.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Who has released material?

**Chris Gammell:** The hounds, yeah.

**Dave Jones:** You've released a whole bunch of your contextual electronics stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** Tell us why. Tell us what and why and where.

**Chris Gammell:** So, what is all of the KiCad videos that were part of Contextual Electronics? Sweet. Why is because a few reasons.

**Dave Jones:** It wants to be free. That's right. Is the title of yours.

**Chris Gammell:** That's right. That was the post. It was KiCad Information Wants to be Free. Yeah. I thought that was clever. But mostly it's actually because, you know, so like the videos, I was looking back at what version I was on. And if you look at like the KiCad versioning, it's like fourth. They're up into the 5000s now. I was on BZR 4004. And they're up in the 5200s, I think, now or something like that. Like they're really much further along. Not necessarily stable, but like the most recent quote unquote stable build is 4022. But that's just because they don't actually release us anymore. But that's another thing. Right. But basically, so, you know, that stuff's moving so fast anyways that might as well get it out there while people can still use it. And, you know, and because I'm using a piece of free open source software like I want to give back to. Yep. So it just seemed like the right thing to do.

**Dave Jones:** It is the right thing to do. So congratulations. You have my utmost respect.

**Chris Gammell:** Well, thank you. Thank you. Nice.

**Dave Jones:** Yeah. So they're all sorry.

**Chris Gammell:** Although I'll be on my Contextual Electronics YouTube channel. So.

**Dave Jones:** Excellent.

**Chris Gammell:** Yeah.

**Dave Jones:** Terrific. How many videos all up?

**Chris Gammell:** You know, I thought it was only like 38. I counted 38 and then I went back and I'm like, no, there's some missing here. So it'd probably be closer to like 50. I think all told in the KiCad course, it's like with like the Getting to Blinky videos that were already out there, it's like 55 or something like that. And there's a bunch more that I need to be making too.

**Chris Gammell:** Got it. It's up there.

**Dave Jones:** So are they actually, are they like how to use KiCad or are they like more generic in terms of layout stuff?

**Chris Gammell:** Ah, interesting. No, it's actually more about the program itself. Like a lot of the quirks and stuff like that. Because, so like, for example, like putting like a silkscreen graphic and I'm not actually, I've never done that in Altium. And I've done that once or twice in Eagle, but in KiCad it's kind of wonky, like the conversion.

**Dave Jones:** It's wonky in Altium too.

**Chris Gammell:** Is it? Yeah. You'd think that'd be easy. I mean, like that's like what people, that's like the flair that makes boards fun. Yeah. And it doesn't seem that hard, but maybe I'm wrong.

**Dave Jones:** For donkey's years, Altium's solution to that, well, it was last time I looked at my, I don't know. I think they've changed it in the latest versions, which I don't use. But yeah, it was like some script because Altium's very script based. You can write scripts to do a lot of stuff. And I think somebody, I don't even think it was somebody at Altium wrote a script to import a bitmap file and convert it into tracks on the silkscreen graphic. Right. And it's like this became the standard way to import. So you go to Altium's help, you know, wiki or whatever, how do you, how do you import, you know, images onto your silkscreen? It's easy. Go into here, blah, blah, blah. Run this script, blah, blah, blah. And, you know, it's like some, you know, 10 year old script, you know. Yeah. Well, I think that's probably the same thing. It's not built in.

**Chris Gammell:** I think that's actually, that might be how Eagle does it too. And I'm pretty sure it's actually how KiCad, I mean, there's a button in KiCad, but really I think that's just calling a script.

**Dave Jones:** Okay. Yep.

**Chris Gammell:** Yeah. But then you have to, you know, have to actually go in and modify, like for, like, that's like the wonky stuff though. Like you actually have to, if you want to like change the layer it's on, right, you need to, if it's going to be in copper versus in the silk, then you got to change the number and you got to find it. And, you know, it's just these weird formats and stuff like that. So it's a lot of the little stuff that's out there.

**Dave Jones:** So that's a real problem with material like this, isn't it? Is that it does go out of date. If you're showing people how to use a tool, well, you know, it can be out of date in a year easily.

**Chris Gammell:** Oh yeah. Right. Right. And, and, you know, and I, I do call that like even if so, if people look at the KiCad project already, there's already, I think on the newest versions, I know at least the footprint, the footprint names changed. Like the extension on them even?

**Dave Jones:** Yes. Yeah. Didn't, didn't the whole footprint manager, the way it worked changed or something or was vastly improved or something like that? Yeah.

**Chris Gammell:** You know, I, I haven't even touched it, you know, and that's what it comes down to. It's like this in any, any version or any tool, right? Usually when you're at a company, you know, they'll standardize on something because it's such a disruptive event when you do make the change, right? Like even, you know, you have Altium, I don't know what version of Altium you have, but for you to change to the newest Altium, there would be, even if there was a smooth transition, it would still be disruptive. Yeah.

**Dave Jones:** Absolutely.

**Chris Gammell:** Like, especially like, like at a company I've worked at in the past, it was like, we tried upgrading and like the entire structure changes, changed from like a, a file based system where you could actually go in and access the file to a database. Like, like how different is that? You know, like that's. Yeah, totally. That's, there's no coming back from that. You know, like we have an exporter, but not really. Yeah. So. Yeah. So yeah, you're totally right though. It's, it's, it's, it's all changing. And, and, you know, especially with KiCad and the CERN guys jumping in and there's other stuff changing with KiCad soon. So, you know, it's, it's crazy. So might as well get it out there now. And this is still a build that people can get. And I think the, the 4022 is not that much different from the, I have that on different computers. So.

**Dave Jones:** Got it.

**Chris Gammell:** Yeah.

**Dave Jones:** And to go along with that, you've got something else as well.

**Chris Gammell:** Oh yeah. Yeah. Yeah. So KiCad.info is the, the new site. So basically because contextual electronics is still there, it's still, you know, it's still a course for people to, to, that's really the learning about how to do the layout side of things. Like you mentioned. And, but, but the actually about the KiCad and everything else. And I'm sure that, you know, how to do layout will sneak in there as well and schematics and everything else. But I had talked on the Amp Hour in the past about discourse, which was a forum software that I really liked. And that was actually when I was installing it.

**Dave Jones:** Right.

**Chris Gammell:** So that's the, there's now a forum for talking about KiCad specifically because there's really, there's nothing else out there. I mean, there is a Yahoo group for KiCad that some people like, but I'm not.

**Dave Jones:** Yeah. Oh, Yahoo groups have had their day.

**Chris Gammell:** Yeah.

**Dave Jones:** Yahoo groups basically work as an email list. It's still not a bad solution if you just want to correspond with the, you know, email. Like you get all, you know, if it's not a big group and you just want to, but apart from that, no, it's just garbage. No one uses it anymore.

**Chris Gammell:** Yeah. And, you know, I was on, I was back on IRC. I'd forgotten that we have an IRC channel for the Amp Hour. Sorry, folks. But I was, I was back on IRC today and actually I looked on Freenode, which is the same IRC server that we use. There is a KiCad channel. There's a huge electronics channel. There was 600 people in the electronics channel on there. That was crazy. I didn't, I didn't realize.

**Dave Jones:** There were 600 people live at any one time chatting.

**Chris Gammell:** Yeah. Yeah. I mean, I'm sure they weren't all chatting, but, you know. Oh, right. They were at least on the channel monitoring, watching. Right.

**Dave Jones:** So they've left their browser open or they left their IRC program open in that thing up in the corner or something. Right. Yep.

**Chris Gammell:** Yeah. So it's, yeah, there's, I mean, there's stuff out there and that's good. I mean, because no one's going to find something, you know, like not one solution is going to work for everyone. So this one works for me and hopefully it, hopefully it works well.

**Dave Jones:** Yep. Yep. So, yeah. Well, technically we're competing then because I've got a KiCad section of my forum.

**Chris Gammell:** You do. And that's good too. I mean, and like that's a different, so you and I have talked about this off the air before, but, you know, like, like discourse is a new, a newer type of forum software. A lot of people prefer the standard inline type stuff that you have. And, yeah, that's great. The old BBS style. Right. I think having more channels with, you know, if there's, as long as there's people that are interested on each one, that's all that really matters, right? Oh, yeah, of course. You know, it can, if, you know, like the big stuff like the IRC channel, you can get lost in the shuffle there, right? And then there's always like these, you know, these social structures that's set up as well. You know, there's always the wise old hands and the people get yelled at for not using the search bar and stuff like that, you know?

**Dave Jones:** Yeah, exactly. You tell it, then, on forums. This brings back memories, actually, of when Altium threatened to, threatened me to, and asked me to take down my, my domain name. Which one? Because I, I actually registered Altium for, we probably discussed this like years and years ago. Yeah, maybe. We've been doing this show a long time, so it's years and years.

**Chris Gammell:** Yeah, it's four years in two weeks, I think. Yeah, yeah.

**Dave Jones:** Geez, you get less for murder.

**Chris Gammell:** I know.

**Dave Jones:** Anyway, yeah, Altium, that brings back memories. Yeah, Altium, because I registered altiumforum.com, and it just basically pointed, well, I set up like a separate forum, I think. Right, right. Yes, I did, yeah. Set up a separate BBS forum, and they came along and went, you can't use the name Altium, it's trademark, blah, blah, blah, blah, blah, cease and desist immediately. Right. It's like, yeah, stick it up your ass, whatever, you know, as if I give a shit. Right. You know? Right. Yeah, that was funny. Yep. Anyway.

**Chris Gammell:** Yeah, well, I mean.

**Dave Jones:** You know what else is funny?

**Chris Gammell:** What's that, Dave?

**Dave Jones:** Can we get into, can we get it over and done with?

**Chris Gammell:** Oh, are we going to talk about graphene? Kickstarter. Kickstarter crap, yeah.

**Dave Jones:** Yep. Bullshit.

**Chris Gammell:** Yeah, go ahead.

**Dave Jones:** Or do you want to leave that until the end?

**Chris Gammell:** Oh, it doesn't matter to me, man. It doesn't matter to me. Go ahead. Let's talk about this.

**Dave Jones:** This guy, he started a Kickstarter campaign to do a rechargeable battery, right? And yeah, okay. It's a rechargeable battery. It uses a super cap. In fact, he specifically said it uses a lithium ion super cap. And I went, okay, great. You know, it actually looked quite good. You know, it was the same size as a standard AA battery, right? But he had hacked in a lithium ion super cap and a little voltage regulator board. So it gave out like a constant 1.5 volts over its entire life and then just, you know, shut off. And he had like a separate charging ring on the outside so it could be fast charged and everything else. And, you know, on the surface, it sounded and looked and sounded really good. And then you start to read the claims. Well, it's got 1150 milliamp hours and it charges in 26 seconds. And you start to smell the bullshit. I mean, you're, you know, your technical mind, you know, your mind's just kind of doing sort of ballpark calculations in the back of your head going, that doesn't sound right. And of course, you do the basic math and to recharge a 1150 milliamp hour battery in 26 seconds requires 159 amps, right? Just small problems like that for starters, right?

**Chris Gammell:** And we should point out there too, I mean, because there's beginners in the audience too. And the reason that that's a big deal is that when you have, you know, any kind of resistance in line in your charger, you're going to, that's going to melt, melt.

**Dave Jones:** Yeah. And just getting the connections that are capable of 160 amps, right? This is like really 160 amps is very serious business.

**Chris Gammell:** Yeah. Right. You ever seen those connectors like from, who is it? Like T, I think TE connectivity, a bunch of them have them. I think Molex has them too, but like those things, like the 100 amp rated ones, like even the 100 amp ones.

**Dave Jones:** Oh, yeah.

**Chris Gammell:** Those things are like, they look like duplocs. Yeah, yeah. Duplos, duplos, is that what it is?

**Dave Jones:** Oh, duplo, right.

**Chris Gammell:** Yeah. Like the big, the big Lego type things. They look like that. Yeah, yeah. The big Lego duplo. It's just like all copper. And then, you know, like plastic sheathing.

**Dave Jones:** They're massive. Yeah. Well, this is a problem that Elon Musk had on the Tesla.

**Chris Gammell:** Exactly.

**Dave Jones:** Roadster, right? It charges so fast, they had to invent their own connector for it because there was nothing else on the market that could handle the power and the current.

**Dave Jones:** Right. Yep.

**Dave Jones:** You know, it just couldn't. You know, he talks about like 100 micro ohms resistance in the connector equals, you know, 50 watts lost or something. It's just insane.

**Chris Gammell:** Right, right. Right?

**Dave Jones:** You know, and I think it's what, 300 amps or something it charges at or I don't know. I can't off the top of my head. Yeah, I haven't seen the specs for that. It's a good couple hundred amps.

**Chris Gammell:** There's a lot of fast charging type. So, they have their network now too. And then, I know. Yep. The ABB stuff was always talking. They have chargers now. And like there's, yeah, there's a bunch of solutions over. Especially over in Europe, like Norway and like a lot of those countries all have even more chargers than the US.

**Dave Jones:** Yep. So. That's a lot of current, yeah. Yeah. Because they can charge that car to 80% in 20 minutes.

**Chris Gammell:** Right. You know. Yeah.

**Dave Jones:** And it's just, oh, it's just, it's just crazy. Hang on. 60 amps, 80 amps they're talking about here. Yeah. I don't think it's in the hundreds, but it's in the, you know, it's almost the 100 amp range or something like that. So, you know, and 120 kilowatts.

**Chris Gammell:** Well, you know, that whole square relationship in the power equation, right? I squared R. Exactly. That blows. I squared R.

**Dave Jones:** I squared R is your nemesis as an electronics engineer. I squared R losses, you know.

**Chris Gammell:** And copper is your friend.

**Dave Jones:** Yep.

**Chris Gammell:** And that's what a lot of this stuff tries to go towards. I mean, they try and drop the resistance, but it's like there's no practical superconductor out there, right? And unless you get something that has, you know, practical superconductors, then you either have to go up in voltage and, you know, have a high voltage charger as well and then convert it later or lots of copper.

**Dave Jones:** Well, but even if you have room temperature superconductors, you're not going to get a perfect, you can't just build them into a connector and then just go, well, I've got a perfect connection, right? You've got dirt and grime and crap and surface error and all sorts of, you know.

**Chris Gammell:** Yeah, compression and all that other stuff. Yeah, compression. It's like material science and physics. It's like, yeah.

**Dave Jones:** Exactly. It's like completely all blend together and it's just, ugh. Right. It's nasty. Anyway, yeah, this thing's 159 amps. Thank you very much. Okay. Like, come on.

**Chris Gammell:** So 159 times 159 is 25281 times, given the benefit of the doubt, give them a million. What do you think?

**Chris Gammell:** Yeah, million.

**Chris Gammell:** Million that's still 25 watts lost.

**Chris Gammell:** 25 watts lost in your 1 milli-ohm connection that's right yeah

**Dave Jones:** yeah exactly you cannot you cannot beat the laws of physics captain i can't i'm sorry i don't have

**Chris Gammell:** a scottish accent right yeah it's okay don't bother okay so that's one thing so what else is there so now i was actually interested in this as well because have you ever played with the lithium-ion capacitors that they talked about because those are actually like on mauser's

**Dave Jones:** catalog right that that is you can buy them these are real things yeah yeah yeah they're really

**Chris Gammell:** groovy i i've never played with one yeah i i think i've had a look at the data sheets yeah right yeah they're pretty kick-ass i think that was another thing that was that was kind of fishy so a lot of this is is that there was a couple hackaday articles that brian benchoff wrote uh and then some interesting so there i don't know if i could say this there's some interesting comments on hackaday uh yeah i know but no some people brought this up too like just the available sizes even uh in the voltages needed because you need to also match the the uh you know your voltage rating as well uh for for if you're going to charge at a higher voltage or anything else like that oh yeah of course so it's all because it's trying to fit in that the double a uh shell size the thing

**Dave Jones:** right he he did this campaign saying it's a double a battery it's got 1150 milliamp hours right and it uses a lithium ion capacitor in it so okay people went and checked including myself went and checked the data sheet for these lithium ion capacitors that he showed in the project but in the photos by the way and uh it turns out yeah you can actually fit one of these in a double a battery great i think it's the 40 farad version or something don't quote me but yeah it's like the smallest one they have right and okay it all fits everything's hunky dory this project is is uh you know could look good so far yeah you can physically build it yes you can physically build it you can buy these capacitors and that's what he implied in the campaign was that yeah i just how i need the money to build the boards you know take boards into production and everything else right and it sounded great until you do the math on that again and it turns out that that capacitor that can fit in the double a battery can only has a capacity of like i think it's 35 milliamp hours yeah oops right you know not 1150 but 35 you know and it's just no so anyway everyone called bullshit on that in including hackaday and all the comments on hackaday as you said and on the ev blog for and i was going to do a video on that um but before i could get around to doing that he the guy who's running this came out and said oh no the real secret that i didn't tell everyone is that it's a graphene capacitor but wait there's more there's more and i make my own graphene at home which again you can do it's true people are making this youtube videos out there yeah with the cd thing

**Chris Gammell:** right wasn't that what it was with like uh one of those uh the burners it can burn they can etch like a laser laser etch on the top of a of a cd like the actual label maker oh no i haven't heard that one i think that's what it was they just spread a paste and then they could just basically they just wrote all ones or something like that and it basically created this film on the top yeah

**Dave Jones:** ah right cool anyway you can make your own graphene yeah so so once again it's plausible right it becomes plausible again and now he's saying oh no what i really need the money for is i need eight thousand dollars to pay the a capacitor manufacturer to manufacture this uh graphene capacitor for for me using my graphene that i give them and it's like yeah dude okay well i'll i'll take your word for it that you've done a deal with a capacitor manufacturer to make your own graphene capacitors okay fine okay i i you know i i i gave him that one yeah and uh and then i did a little bit of research of course as you do in these things and it turns out it's very easy to find that even the cutting edge research of graphene capacitors which are not in production yet by the way right but this guy claims yeah i'll go straight into production is only 12 times better uh 12 times better better volumetric capacity than a than state-of-the-art lithium ion capacitors which he was going to use so even if you multiply 35 milliamp hours by 12 you're still nowhere near his claim capacity

**Chris Gammell:** oh yeah like it's just like so everything falls down 400 or something 410 or something like that

**Dave Jones:** it was 420 or something so so the whole deck of cards on this project just falls down and anyone with you know anyone with any technical knowledge and 10 minutes of googling can prove the same thing yeah and yet he wants us to believe it i mean it's just no sorry that is not gonna happen and and that's that's the problem we've got these days we've got people starting these you know i i actually support him you know making a graphene capacitor and doing all this sort of stuff it's great okay and doing a kickstarter great right but you know just don't go throwing around figures

**Chris Gammell:** that you don't know about and you haven't okay so we need we need a third kickstarter rule change right remember the the big deal was the rule change you need to have production pictures which they have right that's that's what happens now right now we need an engineering notebook worth

**Chris Gammell:** of data verified by a third party calculations and yep by somebody with a gray beard you know yeah

**Chris Gammell:** yeah it's like a stamp of approval from like yeah yeah i give this three stamps of get off my lawn

**Chris Gammell:** lawn yeah well then they can be the categories it's like get off my lawn or plausible or you know

**Dave Jones:** whatever oh goodness and this comes back to the idea that i had quite a few years ago now to actually start a website or a blog or something that actually vetted projects like this yeah you know it's kind of a thankless job i think right i mean oh yeah totally thankless no i couldn't figure out a way to make a make money from it and b make it worth my time in terms of number of views and things like

**Chris Gammell:** that just wasn't going to work yeah it's kind of like snopes for uh because like snopes does that don't they they do that they they do like outrageous claims but yeah it's uh but because it's like that's

**Dave Jones:** such a wide market they get billions of views you know and they can probably make money from it somehow i think they've got like full-time staff and everything yeah probably right right you know

**Chris Gammell:** yeah so hmm yep oh well another one bites the dust i mean this is the same story that we always get right i i i hesitate to bring up ee store again right right no i do love laughing about them

**Dave Jones:** yeah it's the same thing over and over again and well what the hell do we do you know i don't know well you know i think it's only a problem when

**Chris Gammell:** this stuff doesn't get called out right i mean like i've i've heard stories about people getting called about designing stuff it's like in its final days of kickstarter right there and it's like hey can you work on the electrical design for this it's like well what the hell did you just do the

**Dave Jones:** campaign for you know i know it's just there's no that's exactly what happened here the the guy who ran this kickstarter campaign actually saw my blog post and you know complained didn't give any data of course didn't come back with any data but complained that oh i should have why didn't i contact him and he would have told you know it's like dude there's like 10 days left in the campaign you're taking people's money for something that is easily provable you can't produce i mean you know

**Chris Gammell:** it's like and i think i think there's another key in there asking you right i mean it's it's hitting enough of a nerve that people care about it right enough it piques enough interest where people are like oh i'd love to have that and then when you don't right it's like oh yeah i know it's like it's like learning about and and then learning about santa claus again on the same day in case any kids are listening you know i don't want to say anything but

**Dave Jones:** oh dude this solar roadways thing it has gone ballistic you know my video my solar roadways video yeah yeah we talked about some time again it's got like over 3 000 comments now and they keep good lord coming in every day boy you know there's people defending you know oh you've why have you burst their dream you're just you know you're just out to destroy people's dreams and oh fuck oh yeah i'm i'm i'm the bad guy for telling people for telling them people people there is no santa

**Chris Gammell:** claus you know yeah oh he said it

**Chris Gammell:** sagan's listening i don't know

**Dave Jones:** oh it's yeah i don't know you've got it but no like if if you want to spend your own money researching something fine i won't yeah i won't burst your bubble fine you know i'll just have a little giggle and that'll be it but when you start taking people's money and you haven't done your proper you know research on these sorts of things and you won't admit you're wrong and you won't release any data and etc etc no i'm sorry you're just digging your hole deeper and deeper and yeah you deserve

**Chris Gammell:** every bit of criticism you get well i have to say in general uh i'm i'm extremely skeptical about about any kind of energy type thing at all anymore i mean like totally like if people are like i just feel like that could you know that's you always have to you hear energy you just you know eventually someone's gonna stay free in front of it you're gonna be like oh okay or you know like like even the so like there's this ge story right so ge uh there's a spectrum article right uh reputable source i triple spectrum yeah right yeah totally uh talks about fuel cell breakthrough and actually starting production right much more credible because it's ge it's spectrum everything else right and yet i'm still skeptical right i mean like i don't know because it yeah i think part of it for me too is like so often especially with like with portable portable power right i think i can understand turbine moves you know transfer power over ac power lines goes through transformer turns on my vitamix blender and even though i don't have one uh makes me a smoothie right that that makes sense to me i can mostly do that with with like chemistries and stuff like that you know fuel cells batteries uh you know even even like down to the molecular level for like like capacitors and the the dielectric um talking about that stuff like yeah i just don't feel comfortable anymore i'm like yeah i don't believe you i need to

**Dave Jones:** see i know i need to see something else didn't somebody put yet another kickstarter i think it's indiegogo or i don't know bloody hell can't keep up um didn't they put something on there there's a tesla worldwide you know power distribution project and i don't know has it reached its funding i don't know yeah people ask me to comment on this right the warden cliff tower same thing it was like someone

**Chris Gammell:** someone was trying to replicate the warden cliff tower which is supposed to yeah it's push power the ionosphere and then people could get and then free power from their homes and yada yada yada

**Dave Jones:** demonstrably possible okay kind of in some way shape or form you know so it's not totally

**Chris Gammell:** i have to say that's another one okay nikola tesla genius absolute genius i still absolutely i you know it was never built it was never implemented i know that there's a lot of politics and money involved there too but like i still don't believe it i just it doesn't make

**Dave Jones:** sense in my brain the top let yeah the the the top level claims of what it's you know it's going to change the world blah blah blah you know no clearly not but you know there is once again any good thing like this is a hint of truth to it right in some way shape or form what they're talking about is technically possible in some way it doesn't mean it meets their claims but it's you know

**Chris Gammell:** it's sort of yeah okay fine whatever and it's like but what are the boundary conditions right yeah it's like the same thing with those uh those wireless cell chargers right it's like yes those

**Dave Jones:** do work if you're directly on top of them yeah and you're only taking microamp out of it rather than

**Chris Gammell:** trying to charge up a phone battery right no i mean they work they work i mean they they still work with a phone battery with the what's it called the chi that's the it's spelled xi but it's the chi charger there's two different standards now where they actually have on board resident about the same

**Dave Jones:** thing here we're talking about the we're talking about wi-fi charging your cell phone battery no no no

**Chris Gammell:** sorry i'm talking about the uh the pad so you plug in like a pad and then what's your cell phone's on

**Dave Jones:** top of it totally because they're purpose designed for the task no totally but even though as you say

**Chris Gammell:** they're resident coupled yeah yeah right but even those they're very distant limited right i mean like that's still totally oh yeah people have a different get within their mind right yeah yeah that's um

**Dave Jones:** anyway so people wanted me to comment on this and it's like and i got there and i just read the world and i just read the words like you know worldwide energy tower and tesla and yeah it's no stop right like actually that's all you have to do these days is mention the word tesla and you're instantly crackpot you know that's instant tinfoil stuff unless you're gonna have gotten to that point oh by the way speaking of tinfoil can have you seen weird hours new video i did oh my god yeah with the tinfoil conspiracy stuff it starts out all innocent we'll have to post it in oh god we won't

**Chris Gammell:** spoil it for people it's great so he released a bunch of videos and obviously you and i are both

**Chris Gammell:** very big fans of his and he released like a bunch of like all in a row all in different sources it

**Dave Jones:** was actually seven seven videos in seven days across seven different social media sites like

**Chris Gammell:** marketing wise he's a genius but uh oh yeah but what was that song because i'm thinking of the handy song right i'm so handy that was uh one of them yeah i i don't actually know what the i can't

**Dave Jones:** remember what this one's called because it's something unrelated and then all of a sudden the video jumped like halfway through jumps into this wacky conspiracy tinfoil it was so and it

**Chris Gammell:** was so unexpected though i guess i guess we ruined it yeah yeah i know it's just oh we we've probably

**Dave Jones:** ruined it for people now right we should have just said go watch this video and then that would have been right but it's so good oops oh it's called foil okay yeah it's it's uh foil yeah yeah right makes sense yeah it starts out yeah it's about using alfoil you know right right sorry aluminum foil for you yank aluminum aluminum aluminum transparent aluminum yeah um yeah oh anyway it's great it's just awesome and uh there's another couple of i've been getting into videos recently people have um this group i had never heard of here we go we're going to talk music okay go oh yeah i saw you post about them yeah they've been doing stuff for years man i know and i've only just caught on to their videos oh my god they've got this rube gold rube uh goldberg machine video oh yes yeah it's just fantastic and they do it as like a single shot video yep you know it's just fantastic yep it's fantastic yeah just

**Chris Gammell:** like that uh there was a honda one that did that too there's a honda commercial that did oh yeah yeah

**Dave Jones:** i've seen the ad yeah the honda ad where they take all the parts from a car and they make music

**Chris Gammell:** out of it and yeah yeah yeah anyway i mean i think they design a lot of their own stuff too because i know they they were at the white house maker fair i know they had a video oh okay right yeah cool

**Dave Jones:** yeah they're just they're great i'm sold i don't care about the music well they actually the songs aren't bad you know yeah i mean but i'm in it for the video clip yeah right yeah right that's okay

**Chris Gammell:** yeah they have a couple other ones that are like a lot of stop animation and stuff like that they do some really cool stuff i mean like obviously you and i do you do more much more video than i do but uh

**Dave Jones:** that still takes a lot of time like oh i know i that's as the yeah the the video producer side of me i'm a i'm a video producer now if you didn't know yes yes like um yeah the video producer side of me just knows how much work is involved in that and holy crap you know and then the technical side of me knows how much work is involved in setting up all the perspective stuff that knew that i think was one of the latest videos has all this perspective oh fantastic anyway go watch it we'll post a link to it yeah i won't i mean speaking of um video skills with a z and skills yeah i've been my camera pain in the ass freaking camera lost i lost a whole day's worth of shooting and research as well on a video that hurts man that really that hurts that hurts no matter how you're doing it right

**Chris Gammell:** like when you uh i know you're pulling stuff off a uh you know a usb drive and that fails i mean

**Dave Jones:** anytime you lose data like that that hurts yep especially when it was a one-off thing i was well i know i can i can i can redo it right but it was a whole day's research i was shooting video of me looking through every copy of uh the old radio tvs and hobbies oh yeah yeah magazine right so i and i didn't record which episodes which uh which issues it was and which page i found the stuff that i recorded because i didn't have to right it's on the camera right of course right it's on the camera so so now i put all i'd neatly packed all the magazines away and now i've got to start from scratch again because i don't remember which issues they were i systematically went through from issue one to you know to find all this shit and oh anyway i pressed record on my camera and it didn't record it turns out there's a bug in the camera that if you insert the memory card with the power on then there's a chance that not not not always this is not always reproducible but there's a chance that the bug will happen and it will read the card fine but it and it will appear to write to the card fine i.e it pops up on the screen with a little red record symbol and the timer and yep i'm i'm recording everything's hunky-dory you know v u level meters going every yep and but it doesn't write anything to the card jeez and and you don't find this out until you finish the entire shoot yeah because i don't because i don't review my material uh back generally when i'm shooting my material material i don't go because you know it's a pain in the ass i've got to actually put the camera into a different playback mode then i've got to scroll through and find it and press it and dick around with the touch screen and play it back and then i've got to go back into the camera mode then i've got to reset my exposure and blah blah blah you know so that's why i don't check my material generally after i um until i finish the entire shoot i get back to my computer and i go upload and where's my hundred files what and no i couldn't recover them either so that that really hurt that's so hurt yeah that i cried in the fetal position yeah it was just so bad anyway so i got so angry that i went bugger this i'm going shopping for a new camera and do you think i could find a new camera no of course not well you're kind of choosy though too so oh but i i think my needs are incredibly simple but there's no perfect camera out there that suits my needs it's not hard i just need a camera that can a mix audio in the camera give me proper vu meters on there right actual real vu meters not some toy kitty consumer you know little wanky surround sound meter right and and i need a big high resolution screen on it i need a killer battery life i need the ability to take macro lenses and you know so

**Chris Gammell:** here's a good question sorry is this is this an action so we talked about the the project r last week when nadia was on right and i always think about this stuff with modular is this actually a good opportunity for modular right would you would you actually benefit from a modular system at that

**Dave Jones:** point well cameras are kind of pro cameras are kind of modular in that it's they're usually just a camera and then you add all sorts of stuff on you add your focus pullers you add your lenses you add your external hard drives you add your external monitors you add blah blah blah blah that's what happens when you get up into the pro realm the the the camera is just a camera it's just a sensor and that's you know that's you know fairly much it everything else is sort of modular so right yeah well man but then you end up with this huge franken monster rig which you know for average day-to-day

**Chris Gammell:** use it just sucks ass right and so right well i think the same thing applies though right so like you know if you did want to shrink it down right they're going to try and modularize a phone right same kind of thing moving it back down right right scale i don't know because then they're trying to sell stuff that's on the low end and you know what i mean like and then there's always upgrade paths and people always try and hack the upgrade paths and stuff like that and always gets well

**Dave Jones:** look for me for me with these cameras usually the problem like there's nothing wrong with my current camera this bug aside right my current camera would be absolutely kick-ass perfect if it just fixed a few things in software like the ability to easily replay the last clip that you just shot i mean doesn't that see like and and i've looked at the latest version of my my camera's now two generations uh three three generations back right so i looked at the latest canon of this series and i thought surely they've fixed all that not same shit still in there you can't play back a clip you've just shot easily you just can't do it although actually it does there's a feature in there that allows you to do it but get this right it plays back only the last four seconds of that clip and there's no audio

**Chris Gammell:** what what who thought of that why right why well someone at some point someone at some point had a user story right that's how software people do it right they have user stories and some user

**Dave Jones:** somewhere you know that or they guessed right it's like just simple shit like that and you know and it just frustrates the hell out of me and i look around and not no other camera you know can do it and they don't you know make that a fee there should be a button on the camera or a or an assignable button these cameras have assignable programmable buttons why can't i assign it to play back the last clip that

**Chris Gammell:** i shot well dave maybe you should uh skip this whole uh the skip the the open source dmm like you've always talked about and just go straight to the open source camera right well no look it comes down to it

**Dave Jones:** the best tool for the job is always going to be a dedicated tool right a proper tool when you're trying i don't know modular maybe can work but as i said this is like software so unless you unless it's like open source software and you can hack on and you can get little apps for it or something and somebody can write an app that replays the last clip okay great that's a way to solve it

**Chris Gammell:** yeah yeah that stuff's pretty pretty locked down probably like uh firmware wise yep exactly totally

**Dave Jones:** yeah i don't know one of my um sony my sony still camera you can get apps for that apparently i'm not sure how easy it is to write apps i think it's you know incredibly difficult but yeah you can actually like download apps to it to do different things oh yeah well i don't know those things are moving to

**Chris Gammell:** android as well like they just kind of yeah yeah they figure that stuff will go on there who doesn't need pandora on their fridge or their camera while they're doing stuff right i'm sure pandora isn't

**Dave Jones:** does anyone else have any example of a when you need a tool that's just not right and you just can't no matter what you do you can't get the right tool for the job does anyone else have that problem or is it just me or am i being too fussy i don't think i'm being too fussy is it too much to ask the stuff i'm

**Chris Gammell:** asking for i mean i mean uh i can say after just about four years you are pretty fussy but uh i don't

**Dave Jones:** know about in this case so no but yeah surely just the ability to replay the last clip you shot yeah with a single button is that you know i i would have thought that it'd be something everyone needed or a huge number of people needed right all right anyway anyway calm down deep breath all right

**Chris Gammell:** dave let's get you nice and calm down by talking about headless bench instruments

**Dave Jones:** oh great yeah you're gonna boast here aren't you about some is this the national instruments one or is

**Chris Gammell:** this a new hp one or what is there an hp one as well i don't know i didn't see that one oh well

**Dave Jones:** agilent have actually agilent um i only found this the other day through a local dealer um they're selling this new agilent it's like a little like a ruggedized tablet kind of thing which actually connects to all their wireless multimeters in their wireless products so it's actually you know the the the the head it's like an lcd head it's a rechargeable you know i'll try and find a link for it and um yeah and it's like a right it looks actually quite nice and i think it's a great idea and

**Chris Gammell:** yeah but yeah especially if you had a bunch of bodies like like installed in the field oh yeah

**Dave Jones:** oh totally yeah yeah yeah yeah well the whole idea is like this this hazardous installation thing which fluker really pushing now fluker so pushing all this wireless stuff they got this new range of wireless multimeters they've got one sitting here it's like meh you know but but for the market for the market they are trying to target it's it's fantastic you know you're in all these hazardous environments you go put your multimeters in there and you shut all your interlocks and safety interlocks and everything else and then you can stand outside with your mold with your little tablet thing and read all your yeah different sensors you know right voltages and currents and

**Chris Gammell:** phases and works great unless it's a uh anechoic chamber where you're trying to test rf

**Dave Jones:** right yeah you might have a bit of a problem yeah yeah i think that i mean they're doing that stuff

**Chris Gammell:** because that's where the money is i'm guessing but you know that's interesting too because that stuff that is a real problem to solve i suppose you had to put wires yeah totally you know some kind of

**Dave Jones:** barrier in the past so the the the problem is marketing get carried away with it and think

**Chris Gammell:** it's a solution for everybody right right you know and it's like the cost associated with it and that's

**Dave Jones:** yeah exactly say with these headless instruments right yeah yeah okay they've got a niche market right no denying that it's great but it's not a solution for everyone it's like well with so this

**Chris Gammell:** national instruments one is is uh it's a bench instrument right and so yeah this one kind of makes sense for them just because uh you know they already make all this pixie cart and stuff like that you know they pxi or pixie i call them pixie but i don't call them pixie no you say pxi yep pxi okay i like pixie it sounds it's like it's whimsical uh no you know like they already have all this stuff anyways and they're also you know basically they have they have a software interface that already makes sense for this right basically they already have they already abstract out other instruments as it is you can write drivers for keithly gear agilent gear fluke gear and and control it well that that's

**Dave Jones:** basically their market that's their thing that's what they do well it's not all they do but that's

**Chris Gammell:** one thing that they get paid a lot to do because they yeah they'll do like cal stands right like cal stands will run on on national instruments and you know they're easy to replicate and you don't need to code and that yep has some benefits for people and data logging is easy and stuff like that so yeah so that makes a lot of sense and i think that this is kind of a natural extension of that um it's interesting because they're they're saying pc which makes sense right but then they have ipad

**Dave Jones:** which is different uh yawn yawn surely you can do it on an please tell me you can do it on android well not yet but i'm sure that they'll push that so ipad only not forget it don't talk about it anymore no no that's it don't even talk to me no not on my show damn it okay let me know that ipad talk

**Chris Gammell:** you right right well no it is interesting too though because it is why it's wi-fi based uh right so it's not wired as well um you know i i don't know it's just it's interesting because you know one one argument for a scope like especially for like a scope um like i talked about that that wireless scope that we saw at makerfair this past year as well you know you start to run into data problems right you when you think about all right the amount of data that like uh mdo 3000 can do scope yeah exactly i mean it's a lot of data right and it's not necessarily that you're going to view all of it but if you're streaming it like streaming data is always a problem even if it's connected by you know two gigabit ethernet ports you know like there's still you still have to stream it back you have to get it there reliably if there's any you know it has to be deterministic right so that means like i've worked on a problem like this in the past where you know you couldn't even use tcp because it had to be deterministic all right i'm definitely talking through my butt right now but i remember there was something like what is there was a saying it was like tcp is it'll get there eventually uh you're right you know it'll get there but not the first try and udp is even

**Dave Jones:** something like ethernet all right even something like ethernet is not deterministic it's got a

**Chris Gammell:** random backoff retry algorithm right but i think udp is like more like streaming i think right that's where i'm really talking about but i know that's used for video stuff a lot so right and like high

**Dave Jones:** high data rate i certainly i certainly know what you're talking about yeah yeah so uh yeah there's

**Chris Gammell:** there's no guarantee with streaming though right there's any any a number of things can interrupt that right you could have a cable that gets bent you start to you know you start to introduce uh you know unknown delays you start to mess up streaming packets and stuff and you start losing packets and all this other crazy stuff and so wi-fi takes that to another level where it's like oh well crap you know like it's not like not like the wi-fi spectrum is exactly empty so um exactly or

**Dave Jones:** or or someone farts across the room and you know and bingo you know i get lost you know right i mean

**Chris Gammell:** so if you look at the specs it's nothing like this isn't like anything magical either right it's 100 megahertz on dual channels right for uh for the scope uh gigasample you know like it's really there's i mean like there's nothing here it's like you could tell they're doing stuff like like the the analog discovery kit did where it's like you're basically taking advantage of you know commodity level silicon right good you know expensive commodity level but it's not like they're not making custom i'm guessing they're not making custom silicon like a tech or an agilent does and for the scope so they're just kind of you know it's just like you're seeing it it's just gonna trot along like like uh plot along like like uh this whatever the silicon available is so

**Dave Jones:** speaking of tech and processing and plotting along oh yeah nice nice one dave dude get your go and take your agilent uh agilent sorry tectronics yeah mdo 3000 scope which you have i do have one yeah thank you techno turn it on yep do i actually do this is it actually in in front of you now it's off to the side but i could i could all right well yeah well turn it on switch it to rf mode uh-huh and then set the uh resolution bandwidth filter to 300 hertz or below below you know like go from like zero to two megahertz or

**Chris Gammell:** something oh is that the one where it takes like 30 minutes to actually update yeah i did that by

**Dave Jones:** accident just the updating yeah i know and it's not just updating it kills the keyboard it does i

**Chris Gammell:** know it kills everything and i was so confused and then i looked at it i'm like oh that's a spectrum analyzer that's a really small bin that's like it's like what like 0.001 hertz or something

**Dave Jones:** like that for the sample range yeah yeah yeah it's crazy right and yeah granted it's it it has to process you know gigabytes worth of data right it's got to process a buttload of data right but um yeah like just don't disable the keyboard like the user interface because if i want to cancel that or maybe use a cursor for the stuff that's already on the screen while you're taking half an hour in the background to process a new screen's worth of data fine yeah you know like and yeah but that's a that's

**Chris Gammell:** a bug i mean that that's something that could update it right i mean like that is that is a bug for

**Dave Jones:** or it could be inherent in the processing architecture that they've chosen or the operating system architecture that they've chosen so what do you mean like because it's like context switching

**Chris Gammell:** or it's like switching away to a task that that's really high intensity yeah to a task that that

**Dave Jones:** chews up all the resources and they're not and then not releasing that task to go into the user interface i have to imagine that stuff is decoupled right i know you would think so but it's not you've used it it's awful right well i just don't turn it down that low who turns it down to

**Chris Gammell:** 300 hertz i did by accident but yeah don't do that that's the simple i mean like i did i wasn't asking

**Dave Jones:** much i've got a video which i'm about to release exactly after this where i do a zero to two mega hertz spectrum and i've got a 300 hertz uh resolution bandwidth filter right i don't think that's a quite

**Chris Gammell:** unreasonable you're sweeping with 300 300 hertz filter that's what you're you're doing well well

**Dave Jones:** this thing doesn't sweep because it works differently it's not a real spectrum analyzer in quote marks you know anyway but you know it's a zero to two megahertz right span with a 300 hertz resolution bandwidth i don't know right and megahertz on a gigahertz i mean like

**Chris Gammell:** that's that's way out of the range like that's i think that's the wrong you you are the one who

**Dave Jones:** says wrong tool for the job right i mean like that yeah well but you know come on

**Chris Gammell:** i think you're i think you're you're whinging for the sake of whinging but i do agree it's broken yeah you agree it's broken thank you i do agree but you are not right you are not right at all that's that's like being like oh well you know my my six and a half digit dmm isn't uh properly measuring my ac mains it's like okay well no no i'm sorry no it should no it should do this i

**Dave Jones:** understand that's got to process a buttload of data but it shouldn't lock up the keyboard yeah i i have no problem with it waiting 30 seconds for a new screen with a data fine but just let me bloody

**Chris Gammell:** yeah all right i'll give you that okay yeah yeah because you're right you do that for spectrum analyzers too right you'll just turn it way down you wait for that huge sweep right yeah

**Dave Jones:** well yeah i i put it side by side with my rigol one right my which is a like a real sweeping spectrum analyzer right and and i put it side by side exact same settings right and yeah they took you know it was slow to update the sweep i could actually physically see it sweeping across the screen okay on the on the rigol one you can physically see you know it updates each point you know as it sweeps across of course and but i could still use the control panel right and stop it anytime i want or go into menus and set other things up while i'm waiting and you know like holy crap you know and the tech just doesn't do it sorry fail okay the end well next subject

**Chris Gammell:** uh what is the next subject there was something else oh cleveland cleveland is detroit

**Dave Jones:** what about cleveland yeah we have a hardware start up cleveland every week well you know i live here

**Chris Gammell:** we talk about sydney we talked about the maker fair two weeks ago that's a sydney maker uh cleveland is uh is trying to do a hardware startup thing it's uh it's really weird as in like cleveland like the government no it's actually it's a it's a um it's a local like tech group it's called uh shaker launch house shaker being the city that it's in and it's this old uh car dealership and basically they got some grants and they're trying to fund hardware startups and it's it's really weird i have to say like being this close to it it's it's i mean i know that i know some of the people there they're they're very nice um and they you know they say that we have nasa here and a bunch of industrial places but uh you know we might do hardware here i don't think we do startups that well we'll see how this uh we'll see how this goes we'll see if i end up as a uh as an advisor or

**Dave Jones:** something might ask me to advise or something it's very interesting that you mentioned that um there is a star i had no idea but by a chance meeting the other uh a few weeks back i uh ran into somebody who i knew who works for who now works for a startup x slash accelerator slash incubator slash venture capital funding company here in sydney and that's what they do right that's what they do yeah and anyway i'm doing speaking of maker fair and all that i'm doing a fireside chat with the ceo of this he wants to interview me in a fireside chat at the uh fair at the sydney maker fair so that's going to be on august i think 16th don't quote me august 16th 12 30 12 30 to 115 or something anyway be there or be square yeah um yep and we're going to have a chat about i don't know yet we're still hashing it out but anyway it's been organized well i mean we should

**Chris Gammell:** we should square about this right because this is uh this is this is going to be something that our listeners are interested this is not this is not a trend that's slowing down i think it's it's only speeding up right and um let's be honest and frank about what hardware accelerators need right they need a pile of money and right and sometimes and interestingly sometimes the people that start accelerators don't even have that they actually go out to investors that go out they go out and they say we we have the knowledge we're willing to you know do this kind of stuff and you know you invest in us and we'll invest in them and then you know and then the investors get to also have first dibs at the people that are part of the thing they get a certain percentage yeah right exactly and so out of the cherry and it's not like a bad thing it's just you know i think that we there was a lot of these accelerators outside of hardware to start with as well uh you know there's always software app based ones oh yeah um but we're gonna see more and more of these as

**Dave Jones:** hardware now and uh yes that's what this mob want to get into they've been software but they want

**Chris Gammell:** to get into hardware well and that's the same thing here in cleveland right and i think that right like as much as i like the people in cleveland and i'm sure that the people in sydney's are very nice as well we're going to be seeing this where if people are listening are interested in this kind of thing you got to ask yourself what are you really getting there and there's and there's sometimes it's worth it right like i think that like oh yeah oh totally you know like some of the some of the big ones like bolt and lemnos and all those like they have it's not just having equipment right anyone can buy a laser cutter and a 3d printer and everything else that they're going to have there yeah right but it's going to be about connections and it's going to be about mentorship right and those are the big ones i i think that that's the big stuff and then it's going to be how much money they want to give you for your you know your idea effectively at the beginning because that's all it is um right yep so yeah man just i advise our listeners you know listeners are going to be tempted because i think a lot of our listeners are you know doing interesting things with hardware they're going to be tempted by this kind of stuff you know they're going to be told great stories about why they should leave their jobs and work on a project full-time and develop that sensor connected to bluetooth connected to a phone again or they're as alicia likes talking about uh the uh the smart watches all the or all the the fitness trackers that are out there like yep you know it's just just be careful guys it's it's oh here comes the bandwagon

**Dave Jones:** well there goes the bandwagon bye right right yeah i think we talked about that like a year or two

**Chris Gammell:** ago you know we kind of saw it coming and this is kind of like we always yeah yeah i mean it's it's there now right the money's there there's enough like you know there's been enough nests type stories there's you know all of the people with the money have seen they've read the article about

**Dave Jones:** how hardware is a thing and how they should still only like what one in a hundred if you're lucky they make a huge success of themselves you know yeah like yeah well you know i haven't done this i don't know uh i don't know what to say about this i haven't done it either i can't picture myself going well what are you going to give me that i don't already have you know that that i can't buy like i could go and get a crowdfunding money and then i can well okay i can with that money i can you know hire somebody who can actually design a case for me and i can hire somebody who can you know manufacture stuff for me and yeah things like that i don't know what do you bring to the

**Chris Gammell:** table i don't know man i think i i look at all these things like even the good ones i look at them and i'm like you know like they talk about like their expectations of like oh well we want to be profitable in two years and we want to ramp our growth and it's like yeah yeah ramping growth is hard no matter how big you are right if you're ge or abb or anyone else out there like it's just a hard thing to do like apple has legions of people and you know a large number of factories in china that are dedicated to ramping you know like that is a hard hard thing to do so it is and you know and

**Dave Jones:** a lot of these people start up these businesses because they just want to do that they just want to start a business and to me that's always been the wrong way to do it it's like you've got an idea that you're passionate about you start off you bootstrap it right and if it's successful it's successful if it's not okay well okay you've had your fun go on with something else you know it's but you don't have to you know have this grand vision of building some gigantic business you know the first thing a lot of people do when they get this kickstarter money i think we talked about this the other week is that you know they they fail because they get all you know they get their million bucks on kickstarter and then they go out and they hire a ceo and they hire a marketing person

**Chris Gammell:** and they hire a bloody you know and if you're part of a you know a network or an accelerator or something like that they're going to push you to do that too because exactly exactly growth is a

**Dave Jones:** thing growth you can only have growth oh and you've got to have a ceo who knows what they're doing and you've got of course you've got to have a marketing person and then you have to got to

**Chris Gammell:** have a logistics person and you know and eventually you get to go back and be the scientist or the engineer back in the lab again but then you you have a new boss who yells at you about not growing fast enough hey yeah so uh there's messiness coming to the heart i mean like this is not new obviously but i think we're gonna see like like like i think the way to say it is if cleveland has a hardware accelerator as much as i like those guys uh that's your story folks uh

**Dave Jones:** well i'm surprised that there was that there was actually one here in sydney and as big as they are yeah um which is great and they offer a good service for those who need it but just make sure that you

**Chris Gammell:** need it that's a great way to say it yep exactly yeah yeah but that's the problem with a lot of these

**Dave Jones:** people they don't know that they need it whether or not they need it so so it's so they're easy to be sold to you know they will it's it's like um it's it's very similar to all these you know youtube partnerships if you're a youtube content creator you'll get bombarded with all these requests from you know come and join us we'll offer you everything it will make you a huge success and turn you into the number one person you know yeah and look at all these other people who have joined us and they're successful and well they're not successful because they joined you they're successful because they were talented and they had you know the right thing at the right time you know and they made their own success you you're just taking a cut you know yeah like how much have you really helped them in most cases zero you know like yeah no you know you can grow on your own it's not well and i think the

**Chris Gammell:** other thing that we should mention here too is that so we say hardware right we have a very particular yeah uh version of hardware in our head and stuff like that and totally uh actually so a piece by ben einstein who who started the bolt accelerator in boston actually talks about this uh um very deliberately actually about why hardware is interesting right now and it's because yeah it's a lead-in to an app ecosystem right if like you know you look at all the companies that are like doing really well right it's it's uber and it's facebook and also you know like it's still places where you know you control it's nest right like nest is a lead-in for it's the the the nest system on your wall is the lead-in for the data back end right and that's where the money is and it's kind of crazy to think about but it's uh but ben ben wrote a great piece about it i mean like honestly he he wrote out the costs and like you know the risks between uh you know selling someone a piece of hardware or just trying to get to get them you know paying to get them to you know have your app through advertising wherever else and hardware wins and that's kind of crazy right i mean that's but that also speaks to the the type of hardware that they're going to look for and yeah i'm not sure that's what i want to do you know

**Dave Jones:** like no exactly it's like you've got an idea for a niche bit of hardware which just exists in its own right it's got no desire need or want to desire to connect to the cloud or be app based or you know whatever or offer a service or you know i mean right when you think about the things that are

**Chris Gammell:** actually going to like increase or uh what do they call it uh i think that's the vlog brothers they decreasing world suck uh i haven't heard that one yeah yeah decrease world suck uh you know like things that are actually going to help people is uh you know it's going to be stuff that's might not be connected so i just that's another thing to keep in mind i don't know we're being downers again yeah your kickstarter won't work no you shouldn't take money for your product idea

**Dave Jones:** that's stupid but i you know i think we've got data to back it up there's so many that fail because you never hear about the file everyone just sees the success and then that's all they will promote

**Chris Gammell:** to you is the success stories and well yeah what do you think about this uh so so like little bits we've talked about little bits before uh oh yeah what do you think about their do you see their internet module no i haven't looked at this stuff for a year or so yeah so well people don't know they've got those like snap together things they have an internet module and um you know it was interesting so they were at uh aya the uh the ceo she she talked at uh yep at solid con as well and it kind of crosses over into this space of like people starting hardware companies too right because it's not just people that are doing hardware in the past it's people that are interested in hardware you know people maybe software folks that are interested in getting into hardware and stuff like that and that's great right and i didn't actually think about it but some people are doing things like using little bits for for prototyping just as like a concept and then you bring it to someone like dave or you know me or a consultant obviously people that i'm not doing that right now but uh yeah uh dave's not either but a consultant who who could take that idea right it's basically at this point it's a a concept and then turn it into something that's different re-engineer it into a

**Dave Jones:** yeah and i had something that's actually practical to manufacture it and i had never really thought

**Chris Gammell:** about that as a prototyping platform but it was kind of interesting brain switch because you know at that point it is about accessibility to you know if you if you would make something move right if you have a little servo it doesn't have to be full power it just has to say and this would move next right you need a explanation right to show someone and uh i don't know i think it's interesting i think that little bits is still pretty pricey like because i always viewed it as like a toy right i i thought of it as like a toy and a way to learn about electronics but yeah that's how i thought it originally was yeah and i mean it is a way to learn about electronics but uh but man is expensive uh just because you i haven't looked at the problem well you need so many pieces no you don't need so many pieces you know there's like starter kits and like it's like 100 bucks to start and stuff like that and it's like i think like six or eight pieces and stuff like that and you know it's just but i can totally see

**Dave Jones:** their hardware costs yeah oh yeah because they snap together with little magnets and you know it's all very jazzy um but yeah i know but there's just a baked in cost there because you're putting

**Chris Gammell:** everything on its own pcb and there's the connection points and stuff like that so i mean like like for what i think it's a really interesting platform and uh i think it's it's cool for you know like and like thinking about that as a prototyping tool as well like you think about someone who's a you know who could write an app ecosystem and then go show a prototype with this to uh someone i think it is it's very interesting but i don't know what else is past that you know i see them everywhere so i thought it was worth bringing up

**Dave Jones:** there you go i see well there's so many of these prototyping platforms these days i mean it's just you know like the the ability to be able to uh uh you know if you've got a concept or an idea the ability to be able to test that out yeah is you know it's just fantastic these days yeah but in in the end it still comes down to the same problem hardware is hard to make yeah right you're gonna

**Chris Gammell:** still have to do something custom if you want to get your cost down enough to to make uh yeah a

**Dave Jones:** reasonable product especially consumer holy crap i'm looking at how many people are employed at little bits now how do you find that it's on their team page oh little bits cc dot little little bits dot cc holy crappyola oh we're talking three um two four six eight ten we're talking 50 60 employees or something like

**Chris Gammell:** that wow to design well and they're vc backed as well and they're open i mean like that's what

**Dave Jones:** happens yeah that's what happens when you get vc backed like this that's what you do you go out and you hire a buttload of people and without going well is it actually necessary well and i'm not i'm not talking them down in any way it's fantastic okay they're growing a great business they've got a great product okay fine i'm just saying you know like that's the direction that everyone thinks you need to go in you know you need to get this vc funding you need to get millions of dollars you need to hire 20 people and you know do you i don't know what's what's wrong with being the world's best at at making this one little widget and being you know a guy in your garage earning a million bucks income a year just on your own what's wrong with that why do you have to grow a a company and a you know and and sort of you know because the the odds of failure become larger i think as you grow like this yeah well yeah you got a bigger if you miss if if that bandwagon just you know sails off into the sun you know sunset and you're left high and dry you're you start scrambling oh no how can we change direction and move to new markets and keep all our hundred employees fed you know and all that

**Chris Gammell:** sort of jazz and well yeah yeah well yeah man i don't know but then again i'm not a big yeah i will

**Dave Jones:** well both of us right we're not very big businessy kind of people yeah well i think you know we've

**Chris Gammell:** talked about this before but we're we're kind of stuck in that same uh we're kind of basing our business on our selves right yeah i might be able to get out under it a little bit more than you to do

**Dave Jones:** yeah yeah right yeah you know i i always base everything on what my ability to be able to do stuff is you know the last thing i want to do is hire somebody to do it i right now if you want to

**Chris Gammell:** if you know if if you take on money and they expect you to grow it's like well yeah you got it right you got to make that money you've got it yeah exactly yeah that's that's that's the idea so so yeah so uh you know hopefully do well i think there i think that's it's it's interesting now that they so they have this this internet module now though so like basically you know now it's even

**Dave Jones:** it's easier to prototype this is the cloud bit is it yeah right the cloud bit yep yeah right

**Chris Gammell:** yeah so now you know now people can make connected devices prototype with that kind of thing and then later you can spin it into something else so it's interesting you know we'll see see i i would actually be really interested to see you know if there are uh if people know about stories or you know something like a device that started as like a prototyping platform like this that then got rolled in i mean not like i mean like arduino you could say the same kind of thing right but you know the stories

**Dave Jones:** i see it they've they've stayed pretty much true to their original thing i mean they they don't have they haven't really tried to branch out into much else they've got like you know half a dozen

**Chris Gammell:** arduino boards and that's it no you're no no you're wrong on that one oh yeah i'm totally wrong oh i haven't caught up have i yeah they released a bunch of like maker fair rome last year they're like partnered with a bunch of people and now they're kind of more of a licensing type company you know

**Dave Jones:** it's like because oh okay you know now they have a bunch of linux baseboards everything else and

**Chris Gammell:** there's just all right yeah but i don't think there's any right vc money there i don't we should stop talking about vc stuff that gets so gross and yeah we're just yeah not entrepreneurial enough are we no uh no it's uh well well well they talk about you

**Dave Jones:** know don't be scared to fail it's like well i'm not scared to fail but i think failing is just stupid right i mean if you build something up so big that you know that you know you you should know what the risks are and the risks are you know and like i'm not going to go into an area that i know is incredibly high risk of failing because i think that's just stupid right i'm just like i i don't know i just like to play the odds you know that's why i like the bootstrapping thing yeah you know that's why you know yeah okay you you you make 10 of something you make a little bit of profit okay you make another 20 then you make 100 then you make a thousand and you build up your money you build up your cash you don't take on all this credit and you know everything else and it's like i can never understand it well yeah and that's that's the difference though like that's

**Chris Gammell:** that's a company that's going to take you know five ten years to build up and that's that's good right i mean i think that's a good way to do it like good enough for bill and dave good enough for me man i mean granted that was a different time right that was they had military contracts and everything else too but like but like yeah i mean like that is how a lot of businesses are built especially in hardware over time so it's uh yeah growth is growth your odds of success are much

**Dave Jones:** higher your odds of failing are quite small you know and and if you do fail well okay you haven't lost any money you haven't lost any you know i think the bigger risk is nobody wants to buy your product anymore yeah you know yeah then there's stagnation and you know things like that but you know still yeah yeah let's stop talking about we're probably talking out our ass we yeah we

**Chris Gammell:** probably are uh what else did you want to mention i what i wanted to mention something else this week uh oh the little box challenge you see this thing the uh the google oh yeah yeah yeah a lot of people

**Dave Jones:** have wanted me to i haven't actually looked into the real details of it yet anyway google are offering

**Chris Gammell:** what what is it a million bucks a million bucks for a micro inverter that uh they specify the power density for it and it's oh it's also ieee as well that's a 50 watts per cubic inch oh yeah i didn't

**Dave Jones:** know for the uh for the ieee oh yeah there's a big logo at the top yeah okay yeah kilowatt scale inverter at the highest power density at least 50 watts per cubic inch yeah okay right so it's got to be at least one kilowatt they just say design and build a kilowatt scale inverter yeah and they

**Chris Gammell:** give a nice 50 watts per cubic they give a nice uh scale for there as well and yeah it's a nice nicely designed website and everything uh yeah so it's interesting uh we'll see how this this plays out i mean like i think if you look at the problem right now right like we we've talked in the past about we we've talked out our butts on the past uh about uh yeah you know the efficiencies of inverters and stuff like that when we were talking about solar stuff yep um they're pretty efficient right now right but it's about also shrinking it down getting rid of uh you know large larger components stuff like that so that you know they're talking about gallium nitride and silicon carbide stuff like that but it's a matter of actually implementing it and doing it reliably over time

**Dave Jones:** so i see this more as a not a mechanic a a thermal engineering challenge than anything else you know yeah um it's like and and the problem with this is right because it's such a thermal challenge and the electronics isn't cheap to prototype either you know at this sort of scale um in fact my my mate uh i showed it to my mate doug you know he's he does power supply right he's a right guru and he said oh yeah i would have a crack at it if i had a spare you know 10 to 20 grand to throw around and right you know and a buttload of time right and yeah it would take you you know and i was estimating the same thing yeah it might take you you know 10 or 20 grand to really prototype this successfully you know it needs some serious money you know i'm just throwing that figure out

**Chris Gammell:** there floating it but well i think so they list other sponsors on there so like cree we've had john edmund on the program before you know he talked about a lot of silicon carbide stuff they're saying that some of the stuff they'll probably give away you know i'm sure that they all want their parts in the final design stuff like that so they'd probably give away some of that but but you're right i mean spinning boards and you know testing this stuff yeah it's i mean spinning metal and you might have to

**Dave Jones:** liquid coolant or some other solution to cool this thing down you know it's going to get expensive pretty quickly right and you know you'd want to be sure of yourself you'd want to be really sure of your idea you know if you start just going like you can't just dick around with this on a breadboard right you've you've either got to go all or nothing right right you've either got to devote a ton of time to it and a ton of money or don't bother is my opinion on that yeah i mean go big or go home

**Chris Gammell:** yeah yeah oh here they go i clicked other specs as well and they have uh two kva loads power density 50 watts per cubic inch uh power factors are 0.7 to one uh yeah people can know this crap but

**Dave Jones:** yep we'll be taking it has to be no more than 40 cubic inches inches i know that's what i was saying

**Chris Gammell:** before they didn't know love for the metric you know like maybe it changes based on what maybe if you put in dot au maybe that'll change right come on google oh it doesn't exist and it's gotta be no

**Dave Jones:** more than 60 degrees during operation anywhere on the outside of the device that can be touched well what does that include ambient well at what ambient because your device is always going to be ambient plus so if your ambience yeah if you're in australia in summertime in bloody north australia right you're going to be 40 degrees ambient right before you even start yeah but i think it's just about

**Chris Gammell:** so that means and if you're in if you're in cotter right and it's 120 f or whatever that is it was at

**Dave Jones:** 45 c or something uh yeah you you that sucks what wait here i am down in antarctica shooting my video that's right yeah yeah it's only got to 60 degrees it's fine that's right our base assumption here

**Chris Gammell:** folks is that we're gonna always be running this in cleveland in december uh that's it

**Chris Gammell:** cleveland wins yay yeah so do you know what topology i don't really know any the only inverter type uh topology i know

**Chris Gammell:** is just like uh is like a royer oscillator that's the one that i always think about but that's like

**Dave Jones:** really old and and no i don't know inverter i'm not into that sort of thing i couldn't tell you off

**Chris Gammell:** the top of my head it'll be interesting to see if it's uh because i mean like you think about what you're trying to drive you're trying to drive there are some you know some crazy loads right you think about trying to drive a compressor on like a fridge or like a you know a i don't know what you what the load has to be if it's have to be reactive or whatever um almost output 240 volts 68 hertz ac single phase power um but you know if you're driving like a fridge right like a fridge in australia

**Dave Jones:** right that runs on 240 uh that's a that's interesting that they specified 240 i thought it'd be very yank

**Chris Gammell:** centric uh i'm guessing is so that it could be used in all locations right i mean if if this right oh okay this is likely a do good for the world type of thing as well right whereas you know

**Dave Jones:** that's what they say yeah that's why they're saying 240 volts at 60 hertz well here it's 240 50 hertz right everywhere that is 240 is 50 it's adjustable so that means yeah okay right yeah so it's got to be capable of that maximum output voltage right and frequency got it yeah yeah so

**Chris Gammell:** dave and i will not be entering this but uh we do wish everyone luck i think i mean it's really cool i mean like look anytime there's there's money that is put forward for big competitions like this uh or open connected devices like the accadade prize uh you know it's a good thing right there's it's it it hopefully motivates people to do it but i think ultimately you know it's going to be people that can dedicate a lot of time to it i think you're you're right you're right on the money

**Dave Jones:** about that time and and and money as i said you won't prototype this on a breadboard right don't even think about it right it's just not going to happen right so like is there any runner-up prizes and does a prize get awarded if somebody gets so close but not quite you know i mean do you still get the money and nobody else did it but your design got so close but you're only got 94 efficiency instead of 95 you know yeah right right like i do not know right they do mention grand prize so maybe

**Chris Gammell:** yeah but hmm it's interesting that it's a uh uh like the power is kind of boring too i mean like this is an important thing but like power is kind of boring it's very incremental changes these days too so

**Dave Jones:** they are asking for some big changes so and then it must comply with the emc fcc requirements what are you supposed to do you go and spend five ten grand to get that tested maybe they expect uh how did emc engineers to do that stuff you know like yeah i this is big big money big time or go yeah yeah you could have a big so we'll see i'm afraid yeah that's not the yep yeah why why they can't have you know you know a 30 000 prize for you know best concept or something you know even if it's not practical i don't know yeah just you know like i'd be very curious to know how many entries they actually get yeah yeah they said they're taking if they get a lot of you know try hard tire kickers you know here's my breadboard circuit it really works really does trust me you know and they all speak like that you know right of course

**Chris Gammell:** what about this uh so this you put an interesting link on the on the subreddit too um what is this

**Dave Jones:** eda solver thing i was interested oh i just i just got the yeah i just got this this morning i'll have to forward you the guy's email just literally popped up this morning i haven't looked at it hadn't tried it but his concept is um hang on let me call up his email and uh here we go oh no wrong well it links

**Chris Gammell:** it links to eweb at the bottom so i don't know if he's is he part of like aspen is it aspen labs or something like that i know that they did some other stuff for them i don't believe he's well he didn't

**Dave Jones:** say he was associated he's an engineering student going to the university of tennessee oh cool okay he's yeah um basically it's a um the website uh takes translates your project requirements into a json format oh json who doesn't love that right well i don't know about json it's like xml that's the

**Chris Gammell:** way to think about it remember we mentioned this the other week you said json but i've never what's

**Dave Jones:** json i've never played with you know whatever okay and then he's got an algorithm which takes care of finding parts and pin connections that support each other for example this works great for microcontroller projects of robots for example he says it can be used to find the cheapest arduino model that supports 10 servo motors and matches the pins in such a way that the i squared c ports are still preserved so it can be thought of as a project's requirement to schematic generator hmm if that makes sense anyway that's all he says in his email um so yeah it's like and and it's it's uh open source in that you can put you can add your own products to the github repository yeah so that you know if you've got you know you can add all of the arduinos you can add all of the ti launchpads you can add any other components you like doesn't have to be you know development boards and then somehow yeah and then you can add all that data in there and then the algorithm will search everything and you put in your requirements and goes you need to use the arduino uno you know

**Chris Gammell:** to match your requirements or something i don't know well it's interesting it's an interesting

**Dave Jones:** auto router of uh part picking david and the auto router of parts picking yeah i mean yeah in theory that's what it's designed for it'll pick your parts if you had a big enough database yeah yeah

**Chris Gammell:** i mean it's really cool that's a cool idea i mean like um it's a it's a cool idea totally agree

**Dave Jones:** yeah yep so it pulls in costs and everything too yeah i you you would have to try it in practice you'd

**Chris Gammell:** have to try it in anger right yes to see if it's really useful right um and of course it's a chicken

**Dave Jones:** and egg thing you've got to have a big enough database to begin with before it becomes useful

**Chris Gammell:** yes i know about that that is my new job

**Dave Jones:** because it's you know but because it's a public um you know a github thing yeah in theory you know it needs enough people to like it enough to or believe in it enough to go and add enough parts to it and then you've got to trust that people have added those parts correctly and they're usable and blah blah blah and there's no errors in it blah blah blah so yeah anyway it's an interesting idea it's a bit out of the boxy i like it okay yeah i'll have to try it out there there is actually a live demo i haven't actually yeah i just clicked that i didn't i didn't get it at first so right okay right maybe it needs more explanation yeah all i see is a lot of code being executed and it's spat out a five millimeter rgb led and a motor drive board and a something and cost like it's got you you need three of these and they cost x each and it's spat out you have 30 components that take a power a total power of 51 watts and cost 159 dollars and here are the pin connections yeah so like it it literally like kind of does fit his thing of like it's almost like spits out a schematic netlist kind of schematic thing and bomb kind of thing from your project requirements

**Chris Gammell:** for want of a better word yeah well that's interesting that's the example we'll see if it you know you got to put you got to put it would you say you have to try it in anger yeah yeah gotta try it in anger i uh you spoke you said uh led stuff i i tried out a uh those led strips have you ever tried those the programmable led strips i got one i haven't they're dime a dozen they are yeah but uh i have to say i i'm never i'm never it never ceases to amaze me like you know i could do the most interesting electronics on day you know 45 and on day 46 if i blink leds it's still it still does it for me man i don't know it's really all i hear about are these uh art of fruit

**Dave Jones:** neo pixel things yeah that's what i got that's what i got oh right they're cool they're cool things yeah they're cool i'm just sick of hearing about them like everywhere i turn people are you know talking about these bloody things well you know why they're cool right i don't know

**Chris Gammell:** they have like uh they have three leds a processor and a regulator on the individual rgb driver on each

**Dave Jones:** one on the chip flexible and you're right yeah and it's a single input right serial input yeah

**Chris Gammell:** serial input it's all daisy chain yeah yeah it's cool man it's cool everybody loves blinkies all right look like burning man's coming up you know there's always blinkies there i'm never going to that but uh all right at least i don't think i am yeah i don't know anything else we should talk about this week i don't know there's other stuff that's interesting on this list i think people should check out jack's new uh video about getting names right in firmware that was a good one yeah

**Dave Jones:** nah look we're being on for an hour and a half that's enough of our bullshit i know

**Chris Gammell:** yeah mqtt squink go check out the subreddit there's always good links there

**Dave Jones:** it's mostly we just don't we don't need to do the show it's redundant just every week go look at the

**Chris Gammell:** sub right right every week and then you and i talk about cameras and hardware startups all right man cool uh yeah i'll talk to you next week yes so

**Dave Jones:** oh yes and if you want to meet me go to the maker fair in like a couple of weeks um oh i think we'll be doing a show slightly before then but yeah yeah probably anyway yeah uh next week's guest is not

**Chris Gammell:** confirmed yet so i cannot announce it although it is an exciting one so yeah i will announce it on the site if it all goes well all right cool man talk to you next week

**Dave Jones:** bye you

**Speaker ?:** you you you you you you you you
