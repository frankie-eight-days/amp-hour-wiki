---
episode: 3
title: HP, IEEE, and Human Interface
url: https://theamphour.com/3-hp-ieee-and-human-interface/
---

**Dave Jones:** Hi, welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life.

**Dave Jones:** And if you're paying attention there, yes, we have a new name for the show, The Amp Hour.

**Chris Gammell:** And also a new site too, don't forget that Dave.

**Dave Jones:** Yeah, oh yes, sorry, worldwidewebtheampower.com So hopefully easy to remember and hopefully very catchy. It was certainly a pain in the ass coming up with the name, wasn't it?

**Chris Gammell:** Yeah, it took a while, but we got it in the end and I think it's a good one. And we'll probably catch some stragglers looking for battery specifications or something like that.

**Dave Jones:** That was the hope anyway, yeah. Some geeks out there who are just Googling their mobile phone battery Amp Hour or something. And yep, they'll catch us and they'll get hooked. That's the concept. But yeah, The Amp Hour works. And if you don't get it, why it's called The Amp Hour, if you don't understand it, well, you probably shouldn't be listening, I suspect.

**Chris Gammell:** Yep. Well, it's, I mean, you know, there might be people that catch it and don't know exactly what's going on, but don't want to exclude people.

**Dave Jones:** True. So it's a bit of a play on words. You know, the show's about an hour long, roughly, which is what, well, the two shows we've done so far have been an hour long. And this one will probably be an hour long. So we thought we'd add hour on the end. And then we wanted something short and simple that, you know, was a bit of a play on words. And The Amp Hour sort of popped out. In fact, someone on the forum suggested it. Sorry, I forget the, was it Mike? I think it was Mike, yeah, from Mike's Electronics. It was Mike. Thanks, Mike. Thanks for the name suggestion. Yes, it was, Mike's name was hyphenated, but that's all right.

**Chris Gammell:** And you can't leave out the most important criteria, of course, which is there is a .com available as well.

**Dave Jones:** Oh, yes, that was quite an effort. We went through a whole ton of names and we just really had to rule them out based on we couldn't actually buy the .com domain, which was really annoying.

**Chris Gammell:** Yeah, that's, I mean, we talked about it last time, but that's a big deal these days.

**Dave Jones:** Yeah, absolutely. We're thinking about getting the .fm domain as well, but it's like 80 bucks and I don't think either of us could be bothered. But, yeah, maybe, I don't think anyone's going to snap up The Amp Hour.fm anytime soon, so I don't think it's a big deal.

**Chris Gammell:** I don't think anyone's snapping up .fms. No. We've got $70 laying around or $80 laying around.

**Dave Jones:** Yeah, it isn't a huge amount of money, but just in comparison to a normal .com domain, if you're not into that sort of thing, a normal .com domain is like, you know, $6 or $7 or $5 or something. So, yeah, the .fm, who's the country that's behind the FM thing?

**Chris Gammell:** It's Micronesia. I forget if it's Federated States of Micronesia.

**Dave Jones:** Ah, the Federated States of Micronesia, yes.

**Chris Gammell:** Yeah, so FM.

**Dave Jones:** Right, and they're trying to, they've realized that they've got something that sounds interesting, so they're trying to rort it.

**Chris Gammell:** Well, there's a couple of boutique names out there, but that's one of them.

**Dave Jones:** Yeah. So there you go. It's now called The Amp Hour, and hopefully we'll keep the hour format, and hopefully it'll be about electronics. So far, it's been about domain names, so shall we get into it, Chris?

**Chris Gammell:** Well, before we do, why don't we thank some of our other promoters out there. We got a nice shout-out from Alan over at HackGadgets.com. Oh, yes.

**Dave Jones:** Thanks, Alan.

**Chris Gammell:** Mentioned on the Ubiquitous Make blog, thanks to Alan. I think they probably grabbed some of Alan's feed, so thank you to everyone.

**Dave Jones:** I think somebody submitted it to Mike from Alan's blog or something like that, something along those lines anyway. All these blogs are interconnected and feed off each other's content.

**Chris Gammell:** I mean, I saw a post on Hackaday about the Beagleboard calculator we were talking about last time. Yes, I saw that. And they were lamenting how they were like the last ones to the party, but they were like two days behind. And I don't know, maybe the community is not as big as we thought it was, or else it just takes too long to finish projects.

**Dave Jones:** Well, maybe. And there's so many blogs out there. How can you possibly follow them, especially if it's posted on somebody's personal blog? Yeah, yeah. So it takes, yeah, it's like that LinkedIn thing. If you're on LinkedIn, I know we are, but yeah, it's like, you know, you realize that you're only two people separated from anyone in the industry or something like that. Yeah.

**Chris Gammell:** It's like, oh, yeah, give Steve Jobs a call on a Tuesday and ask him for a coffee or something.

**Dave Jones:** Yeah, exactly. I'm, well, I'm only one hop away from the was, I think.

**Chris Gammell:** Really? Ooh. Ooh.

**Dave Jones:** Yeah. So there you go.

**Chris Gammell:** So everybody should try and friend Dave. So maybe I should try and link into the was. Or yeah, just try and link up, you know, our listeners should try and link up with you and then it'd be two hops away. They could just leapfrog over to you. Yeah, exactly.

**Dave Jones:** We were, yeah, we were only, I think, yeah, we were only one or two hops away from each other. I don't think it's almost impossible to get three or four hops, isn't it? It's that five degrees of separation thing. Yeah. It's like, you know, it's all, you know, it's bell curve related probably, you know, and sort of, you know, it's very rare to get those outlier, be four or five people away from someone.

**Chris Gammell:** Yeah. Well, it only has limited use anyways. I mean, like LinkedIn is nice. You know, you can see what people are doing in industry and stuff, but in the end, it's like, you're not going to just run up and introduce yourself to the was or, you know, anyone that's on there. I mean, maybe you will. As much as I would like to. Yeah. I mean, maybe. Right. Maybe.

**Dave Jones:** I'd love to interview the was because I'm going to be in the US in October and I'd love to, man, if there was somebody I could tee up an interview with the was, I think that'd be terrific.

**Chris Gammell:** Well, you never know. Sometimes you just got to ask. Sometimes you just got to ask.

**Dave Jones:** Yeah, exactly. Yes. I might have to do something like that.

**Chris Gammell:** Well, maybe, you know, another thing we were going to talk about today was the IEEE. I don't know if you're part of that or any professional organization, maybe you can link up through them too.

**Dave Jones:** Yeah. Well, yes, I am a member of the IEEE and I'm not sure why, just because I can be, I guess. You know, I don't really get much value out of it really, but yes, I am a member. Here in Australia, we have the Institute of Engineers Australia, the IEEA, I think that's

**Dave Jones:** Oh, really? Okay. Yes. And is it? Yeah, the IEEA, yes. And Institute of Engineers Australia, and they're, you know, the same thing, pretty useless. You know, some people join, very few engineers actually join it. But I don't know many working engineers who remember, you know, there's a few certified practicing engineers here in Australia because they like having the wake, you know, title after their name, you know. But it really doesn't achieve you anything actually in the industry, really. So, yeah.

**Chris Gammell:** Well, obviously, Dave doesn't know that I was on my way to get my professional degree, but I'm not there yet, so don't worry, Dave. I'm not offended.

**Dave Jones:** That's cool.

**Chris Gammell:** Yeah. I don't know. I wonder about how much, you know, it seems like IEEE and the big, you know, engineering organizations, it seems like they're kind of, not outdated, but they're definitely a legacy, you know, where that used to be the only way you could talk to other engineers. Well, not the only way, but it was a good way to link up with people. And I just wonder about the viability of them these days. They always promote that, oh, we're so important, but I don't know. I don't know how important they are.

**Dave Jones:** Well, that was actually one of the themes of the Australian documentary, electronics industry documentary I was working on, you know. Oh, yeah. Were these industry bodies actually relevant anymore, you know? Do they have a purpose or have they been supplanted by the, you know, just the internet and the communications, you know, the whole internet thing and LinkedIn and everything else. So, yeah.

**Chris Gammell:** Well, I think some of the value they add is like the, you know, they still do standards, so that kind of stuff's good, you know, like, it's nice. Oh, yeah. Yeah, for sure. I mean, I don't know why they keep sticking with the 802 dot whatever, but it seems like everything's 802 for, I mean, it's probably just the wireless base standard, but, you know, it's nice to have those things so that, you know, devices can talk, but in terms of the professional development, I don't know.

**Dave Jones:** Yeah, not, yeah, I don't think, yeah, I think they should just become like a standards body and that's probably it, you know. I don't know. It might be different in other countries. I don't know how it is, but here in Australia, no one really gives a toss, so.

**Chris Gammell:** Yeah, and there's local bodies too. I mean, like the Cleveland one is, they've done some events and, I mean, I got to listen to some cool speakers going to that, so that was cool, but it's not like I'm like chumming up with the, you know, local engineers from that because it's like, well, I'm going to listen to someone speak, so.

**Dave Jones:** Yeah, exactly. Well, we have the same thing here. The Institute of Engineers, they organize, you know, lectures and things occasionally and they're, you know, I've been to one once and they're pretty dry and boring, but hey, they do organize these, you know, these industry events and things like that, so, yeah. But I don't know what the future holds for these bodies, you know, I really don't. They'll just organically change with time as they see it or they might just cling on, you know, to what they've got and maybe they've got no one in charge who understands the, you know, the modern way things are done, so.

**Chris Gammell:** Or maybe we're just totally out there being on the internet. Maybe the engineers are actually, maybe we're just, you know, we're the one-off weirdos and everybody else is hanging out at those meetings, you know.

**Dave Jones:** Yeah, us freaks who have blogs and things. Yeah, gross. God.

**Chris Gammell:** Get a life and go to a meeting.

**Dave Jones:** Exactly. We need to be more restrained, professional, and wear a tie and, you know, be really, oh, yes, none of this trash talking, you know, products and companies and the industry.

**Chris Gammell:** The throwbacks to the old days. Yeah. Well, that's one of the things, another thing I wanted to talk about today was the, you know, I talked to you right before we started taping, but the scandal with HP, I don't know if you want to talk about that at all, but the.

**Dave Jones:** I only read a bit about it. Yes, please. HP is one of my favorite topics. I love HP.

**Chris Gammell:** I know. Well, and, you know, if you don't, if you haven't heard the story yet, basically the CEO got caught, you know, funding or, you know, expensing out these dinners with this consultant lady who he's hitting on or something. I don't know what the story is there, but, you know, they said there's no, it's starting to sound like a tabloid, right? Right. Yeah.

**Dave Jones:** That's all right. Let's, let's so go there. Let's do it.

**Chris Gammell:** Oh, yeah. Yeah. That's, that's a subtext for this blog. Engineering, electronics and intrigue. Anyway, so.

**Dave Jones:** Well, let's, let's cut to the chase. He was after a root. There you go. There's a soundbite for you.

**Chris Gammell:** All right. All right. You heard it here first.

**Dave Jones:** Yes. Controversial Dave Jones again. There you go. I reckon the, uh, H, I have no idea about the story, but there you go. That's a rumor I'm going to spread that the, uh, former CEO of HP was, was, uh, fishing for a root as we say here in Australia.

**Chris Gammell:** Yeah. I've never heard that one before. That's another. Okay.

**Dave Jones:** Well, there you go. Uh, yeah. Everyone in the U.S. Another bit of Aussie culture, huh? Anyway, uh, so basically. Something to do with a female employee. Was it the employee or?

**Chris Gammell:** Yeah. It was like a contractor. She like, she was like a social director. Anyways, long and short of it is he expensed all these dinners. He shouldn't have. Uh, they don't really know what's going on. So they, they tossed him out. And, uh, but on the way out, of course, you know, why not give him $35 million on the way out the door? Because that's what I figured would happen if I ever left my job, right? Or you would with yours too, right, Dave?

**Dave Jones:** Yep.

**Chris Gammell:** I mean, well, why wouldn't they just give him a, uh, you know, $35 million check, uh, for, for doing something wrong?

**Dave Jones:** Well, that's right. But it's usually to get rid of them quietly, you know, it's, um, that's well, and, and because that's the way it's done in big business. It's the golden handshake, the golden parachute. It is, it happens in Australia and every other country I've read about. It's just, you know, it's just the way the big industry like that works. These companies, they sign these people up or everyone on the board and the directors, they've all got these deals. So, you know, it doesn't surprise me when somebody gets booted out, you know, in Australia, there's a famous case of Telstra, which is our national, um, national telecommunications body. And the head of that, he was only there for, you know, a year or two. And he took the, um, you know, he basically took the company down the toilet and he walked away with his, you know, 30 or $40 million. Thank you very much. And, and the heads of banks do it all the time that, you know, they, they are the bank CEOs, you know, some of them get $40, $50 million. Yeah. All off from walking away, including options and things. So, geez, you know, well, the thing I really want to say about someone was going to pay me 12 million bucks, I'd, I'd leave my job too.

**Chris Gammell:** I know you'd go pay for some dinners with some, some lady, right?

**Dave Jones:** I mean, exactly.

**Chris Gammell:** Yeah. Yeah. But the thing I wanted to say about it, I mean, basically, I don't know if you've ever, uh, read about them at all, but like, I've been reading the biography of, uh, the guys that started, uh, you know, Bill and Dave. Dave. Yep. The HP way. Yeah. Yeah. No, not the HP way. It's, it's, uh, it's another one, but it's similar. I mean, it talks, it, it quotes the HP way. The HP way is the, the book that they wrote. That's what, uh, I don't remember if Bill or Dave that wrote it, but this is actually more of a biography about how they started the company and, you know, they're bringing their products up and you just read about these guys and like, I don't want to say saints, but like these guys were awesome. I mean, like you read about them and like how they ran their company and like, man, they gotta be rolling. I think they both passed away, but what, at least one of them did. I think they have now. Yeah. Yeah. And they gotta be rolling over their graves seeing this guy. I mean, first Carly Fiorina, like that lady messed everything up and just put their company on the toilet. But, and then this guy, I mean, apparently he brought things back, but he's, I mean, not exactly the best, uh, the most ethical businessman here. And, you know, like, but you read about the original guys and their engineers and their, I mean, they did their own product design. They brought this company up from nothing. They like, they helped bring Silicon Valley up to what it is today. Basically they, they helped bring Stanford up to what it is today. Fred Turman is the guy. He's one of the professors they talk about at Stanford. And those three guys, I mean, they basically help bring Stanford to where it is today. It's, it's unreal reading about it. And.

**Dave Jones:** Oh, absolutely. I mean, if you've been to the HP garage in, uh, I don't know if you've been there, but, um, yeah, I've got my photo in, taken in front of the plaque and it's now a national historic monument, the HP garage and the plaque there, it was the founding place of Silicon Valley, you know, basically they single-handedly, as you said, um, Bill and, um, Dave and the, um, and the Stanford guy, um, basically founded Silicon Valley like we know it today. So. Yeah.

**Chris Gammell:** Yeah. That's it. I mean, it's a great book to read and it's called Bill and Dave. It's a great book, but you know, you, you, you hear about all this stuff now and you hear about these guys that are, you know, this guy had like, he was like a business major from some, I don't even know where, but like, you know, he, he worked his way up to the company. That's great working hard, whatever. But then you get to the top and $30 million just to, just to set foot outside the door. And, you know, we wonder why kids don't want to go in engineering these days when, oh, well, either I can go be a grunt engineer there and, you know, get paid X number of dollars, or I can go, you know, do whatever the hell I want to and walk out the door with a golden parachute. Uh, I wonder which one I'm going to do when it comes to time to study. And it's like, you know, we wonder why there's problems these days. And, and I would point to that as one of them.

**Dave Jones:** Exactly. Well, actually that raises another interesting point. We'll come back to HP, I think. But, um, as you said, um, when kids decide what they want to study, well, um, that comment there just, just reminded me that really, I think the, the, the best engineers are going to be the ones who already know that they, that's what they want to do. You know, they don't make the decision. They don't, you know, finish high school and be, you know, they're 17 or whatever. And they go, right, what am I going to do for a living? You know, I, I've typically found those ones don't make the, you know, those don't turn out to be the good, some, some of them do, but you know, on a whole, I think the, you know, the really good and talented engineer or the really enthusiastic and passionate engineers are the ones that, you know, have known they've wanted to do that all their life. And that's what they just do. Yeah. I mean, yeah, they're looking around. Oh yeah. I'll do engineering because my friend's doing engineering or my parents want me to do it or something like that.

**Chris Gammell:** So yeah. I mean, they're looking around the garage at home or their workshop and they're like, Oh, Hey, I work on a, you know, like the whole, the whole maker community. That's why it's so great because you know that these kids are going to be graduating high school and maybe even if they're, their math grades, aren't that great, they're going to be looking around and being like, well, I really enjoy this stuff and maybe I can get better math grades or maybe I don't even need to go to a university because I've, I've been working on it so much. And exactly. That's, I mean, that's why the whole movement kind of excites, excites the hell out of me because I mean, that hasn't, I mean, there's been, there's been, you know, ham radios helped a lot and stuff like that, but, but man, if it keeps going. And, uh, it's going to be good. That's going to be really good.

**Dave Jones:** It's massive. You know, you've got tens of thousands of kids learning to solder these days. You know, it's just, it's just incredible. How cool is that? You know, I, I really didn't picture this five, eight, 10 years ago. You know, I thought, oh, electronics is a hobby. We've mentioned this. We've talked about this before, but I thought it was near, you know, it was near dead. The last nail in the coffin. But no, geez, it's coming back and kids seem interested. I, I just can't believe it. I'm still in shock.

**Chris Gammell:** Well, that's yeah. You know, some, uh, another thing we had on our list is, uh, and probably relevant to that because the hobbyist market is a discrete components. And, uh, you know, it's a lot harder if you have to have an SMT reflow machine in your house, toaster ovens work sometimes as you could probably find projects online. But, uh, what, what happens if those go away? Right. I mean, uh, how long do you think those are going to stick around?

**Dave Jones:** Oh, there's no question that the through hold discrete components are going to be around for at least the next 20 years. You know, they're just going to be around forever. Really. I can't see when they're going to die because there is still a need out there. And, and the Chinese, uh, uh, gray component market just keeps churning them out because they're still cheap and easy to produce and they're, you know, easy to assemble. And yeah, it's just, uh, yeah, that's a good point.

**Chris Gammell:** Cause it's not going to stop. If you open up a, if you open up a, you know, a toy these days, you know, you're not seeing like just a micro or anything like that. You're always seeing like, you know, you're still going to see a NPN transistor and a couple, you know, probably through hole resistors on there. And it's actually surprising. I mean, if you, if you haven't opened up a toy in a while, it's, it's actually, I mean, the advanced toys are still pretty, you know, they're, they're, they're interesting to look at, but you know, like the, the, the talking, you know, stuffed animals and stuff like that. Those are still pretty simple, uh, pretty simple machines.

**Dave Jones:** Oh yeah. They've, and they've got, I've opened up a few of those over the years and they've just got like a Baker light PCB, you know, it's not even an FR four. It's the old punched holes, you know, because it saves 0.1 cents on the cost and they're through hole and you know, and it's just, it's just incredible. Even if you open a modern TV or something like that, you'll find, you know, all of the power supplies, right? Yeah. Yeah. That's right. Every power supply is all through hole components. Yeah. Well, that's a power thing too. On a single sided PCB.

**Chris Gammell:** Yeah. Yeah. It's interesting. I, uh, I, I, sometimes I volunteer with a, a group around here that, that actually, uh, modifies toys for, uh, for handicapped children. So you, you know, you, you wire in different plugs basically. And then there's like a universal hookup and, uh, and that's great. Cause that's, that's, that's how I see a lot of like the, the, the lower end toys and seeing how like those, the actuators on there and everything. And that's, I mean, it's just amazing seeing you're like, Oh, that's, that's it. Yeah, exactly.

**Dave Jones:** I know it's very low tech. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** It's not much in there, but yeah. Everyone talks about the distant demise of discrete components and it's just, it's just not happening as, you know, even the evidence like the, uh, TI launch pad, you know, they've all out there. I think I've mentioned this in the blog or somewhere. They've, you know, their new range of TI MSP 430s, they still come in dip packages. Why? Because, well, there's a need for it. There's a need to just, um, either, you know, either actually do a prototype of something or, or just, you know, um, not, not everyone's going to go to SMD.

**Chris Gammell:** And also sometimes when you're, you know, it's a winter day and you're wearing wool socks and you walk over to your launch pad and you zap it, you need to just switch it out real quick. I mean, yeah, exactly.

**Dave Jones:** You need to, you know, need, sockets are important. Yeah. You just whip it out. That's not a new one. And yeah, yeah. No, through hole components. No, anyone who, uh, who says through hole components are going away. No, they have no idea.

**Chris Gammell:** Yeah. I mean, it's, it's tough because a lot of the, the fancy ones are, are, are, you know, and the, and the actual, uh, SMT components that there are, that are out there, they keep getting smaller, but you know, what are you going to do about that? I mean, you're not going to, even if you have a reflow machine at your house, like, like, uh, you know, Adafruit, they have that in the, in their office, right? They have a reflow there. Yeah. And, uh, but they're not doing BGA there because you, then you need like x-ray and you need to be able to line it up real well.

**Dave Jones:** Exactly. It becomes a pain in the ass here. Yeah. So there's, you know, BGAs and chip scale packages and all those sort of, you know, flip chips and all those sort of things, you know, they're, they're designed for high volume, you know, mass produced, you know, items that you spend a fortune setting up and getting those right, you know? And, um, and, um, unfortunately a lot of specialized custom chips these days are, are only available in, you know, surface mount, surface mount packages. That, that, that's a big problem in the industry. Um, if you're trying to do your, you know, if you're trying to make a hundred of something, you know, and the chip's only available in a micro BGA, then you're, you know, you're pretty much screwed.

**Chris Gammell:** Yeah. Well, it kind of points towards, uh, another market that's kind of opening up too, where there's like these quick turn board, like we talked about that a little bit last time about, you know, board houses that'll not only make your board to populate them, but that's just going to have to be more of a reality now where you're not, you have to just have someone do it for you because what else you can do about it?

**Dave Jones:** Well, exactly. I mean, if I had to design in a micro BGA or a large BGA FPGA into a high design, I'm not going to get a toaster oven at home and do it myself. I'm just going to go and pay someone 50 or a hundred bucks to load the first prototype up.

**Chris Gammell:** Yeah. And it's worth it to pay that. I mean, that's almost like paying for quality there. Well, not necessarily quality, but you're paying someone to take that risk off your hands in that case because, you know, you need to make toast the next day.

**Dave Jones:** Yeah, exactly. And, you know, and I don't want to waste, you know, $500 chips, you know, some of these BGA, you know, if you've got a big FPGA or something, it can be, you know, a hundred bucks for the chip, 500 bucks for the chip even. So, you know, you really don't want to be doing a trial and error thing to try and get that right. You want to give it to someone who's done thousands of them. So, yeah, no contest at all.

**Chris Gammell:** Yeah. It's interesting to, I mean, like how you were talking about with that, you know, the hundred dollar FPGA and you and I were talking a little bit before the show about the, you know, just the span of electronics and how far it goes from the, you know, like I'm not touching hundred dollars. You can get like $600 FPGAs these days, you know, like the Vertex.

**Dave Jones:** You can get ones that cost $2,000 if you're really that. I know. It's crazy.

**Chris Gammell:** Who does that? I mean, military probably, you know, whatever. Yeah. Yeah.

**Dave Jones:** Very specialized military applications or specialized industrial applications where, yeah, you've got 10, $2,000 chips on the board and the board's worth more than a car, you know? Yeah. Yeah. Yeah. But that happens. There's a niche industry out there for that. Oh, yeah.

**Chris Gammell:** Yeah. And I mean, but it's just, it's just interesting to see how far it spans because, I mean, you look at like, you know, a lot of, a lot of your viewers on EEV blog are hobbyists, but, you know, you'll also get people that are, you know, they're working on the $2,000 FPGAs and just kind of like how, how does, like there's some people that are seeing stuff that, that you and I probably will never ever fathom, you know? Oh, absolutely. Like some of the top end stuff. Yeah.

**Dave Jones:** And there's people who's doing ASIC design and things like that. Yeah. So, you know.

**Chris Gammell:** I don't know, the, the high speed, the high speed things too. I mean, like there's, I mean, I was, the reason I brought a lot of this up is because the, you ever seen current feedback op amps before?

**Dave Jones:** Oh, yes. Yep.

**Chris Gammell:** Yeah. I mean, like that's a, that's the kind of part that I was really interested when I first learned about it because, you know, it's a, you know, most op amps are voltage feedback and those are kind of the kinds that you see every day that, you know, you know, all the standard equations for, but, but then you start looking at current feedback ones and you're just like, whoa, what's going on here? Why are they doing this? And it's actually for speed and it's, and it's just this whole, I mean, I work in analog stuff, but that's just a whole section that I've never seen because I work on the slower, the slower side of analog before. So when I started looking at these things, it was just like, well, this is really cool, but I don't really need this right now.

**Dave Jones:** Well, that's right. I mean, I, I can remember my, um, uh, a job that I had, I started, you know, it was 12 years ago or something. Well, no, it was longer than that. It was about 15 years ago now. And my first day on the job was, um, uh, I had to troubleshoot a charge amplifier and it's like, what, you know, yeah, I kind of understand the concept of a charge amplifier, but I've never, I've never had to design one. I've never used one. I've never, oh, what a, you know, I really had no clues. So it's just one of those more obscure, um, things that not everyone, you know, actually, you can't possibly have experience in absolutely everything. It's just impossible.

**Chris Gammell:** Well, what did you do that? I mean, 15 years ago, there was no Wikipedia. So what were you doing back then to, to kind of pick out where to start? I mean, where did you, where did you start with that kind of thing? Cause I, I mean, I've run into that and I know that people listening to this have probably run into that before, but I think the de facto standard today might be, oh, well, you know, type it into Google, type it into Wikipedia.

**Dave Jones:** Exactly. It's easy. Yeah. No, back in the, back in the pre, pre day, you know, the pre communications, prehistoric days, you know, I just had the books on my shelf. That was it, you know? So I'd have to reference those or I'd go and ask somebody, you know, can you explain the circuit? Or I had to find another product which, uh, used that particular circuit and see if they had any, um, you know, technical reference manuals or something like that, which should explain the circuit operation. And yeah, you know, you could spend days just hunting down an X line or even a circuit diagram from what a charge amplifier did. So yeah.

**Chris Gammell:** Yeah. It's kind of amazing that the, uh, you know, like people wonder about like the, we talked last time about, about like product life cycles and how it's getting a lot faster and everything. But you think about that, that element right there. I mean, if you're cutting days off your investigation period, I mean, of course they're going to want it faster. Type it into Google. Doesn't it pop? You should just have a product pop out the other side, right? I mean.

**Dave Jones:** Yeah. Well, it's, yeah, it's totally different. Well, back then, right? You would have, you know, the company would even at home here, you know, I would have hundreds of data books, hundreds of application notebooks, you know, textbooks and, you know, dozens of them. So you could just walk in there and browse for hours and you'll probably eventually find something that'll lead you onto something else. And, you know, they, they, they sort of had hyperlinks in the books, so to speak. They would say, oh, go and see application note AN56, you know, so you'd, you know, oh, I think I've got that somewhere. So you'd find another book, which just had all the application notes in it and you'd go and, you know, flick through that and you'd eventually find it hopefully.

**Chris Gammell:** Yeah. Yeah. Yeah. I mean, it's, it's amazing today that like now we have message, I mean, we got like your forum. There's a, uh, another shout out might be for chip hacker. That's one of the forums that I'm on. It's actually like a stack overflow style. I don't know if you've ever been on stack overflow. Yeah. Yeah. And so that's, I mean, there's a lot of cool, cool resources out there. And to the point where you can almost just go out and ask people, ask these communities that, man, probably didn't have that 15 years ago, other than calling your neighbor, calling someone else that you might know in another company, right?

**Dave Jones:** Yeah, exactly. Or you just did the legwork and did it yourself, you know? Yeah. Yeah. And, um, and you'd eventually find it or, you know, you'd just bluff your way through until you found the required info you had. But, um, yeah, the, the forums these days are amazing. You know, you can ask any question and almost get an instant answer. Yeah. To anything. It's, you know, it isn't just our industry. It's anything at all, really. So. Yeah.

**Chris Gammell:** Yeah. And, well, I guess a little self-plug there would be, uh, you know, if you have any questions for us, there's, uh, you can, you can always ask them on the, uh, the new, the amp hour.com site or, uh, the, uh, EEV blog forums. Those are always, uh, pretty active too. So a little, little self-plug there.

**Dave Jones:** Yes. If you've got, uh, yeah, if you've got questions you want us to answer, like an ask an engineer type, uh, thing, then.

**Chris Gammell:** Just a little less live.

**Dave Jones:** Yes, exactly. It's not quite as live. Although, you know, I can see maybe eventually the, uh, this radio show in the future morphing into sort of a live, not a, well, maybe we'd have, you know, people on live who can join in, um, or we might have a chat forum live, you know, where something like that. But yeah, I don't know. It's, uh, working in its current format. So we'll stick to that for now. Yeah. But yep. Happy to answer questions.

**Chris Gammell:** Yeah. So that's good. What about, uh, you know, another question I had, it was about, uh, open source tools. That's another thing that might not have been as prevalent 15 years ago. What, uh, have you ever, do you ever do any like, uh, open source software tools or anything like that?

**Dave Jones:** No, I, I really haven't worked on any of those open source, um, projects. I, you know, I'm too busy working on my own stuff to contribute to, you know. Open source projects. But yeah, things, things like the bus pirate and stuff like that are really quite neat, you know, they, um, it's, you've got to watch out for those open source tools because often they will get, um, you know, too many cooks spoil the broth and all those sort of sayings, you know. So yeah, it's just not as focused a tool as it could be if just one person with a great idea actually just implements it themselves. So, you know, there, there are exceptions to that. There are good products, good, excellent open source products out there, but there are others that are just trying to be a jack of all trades and, you know, um, yeah, don't really cut it for, um, for, you know, some niche use you might need it for.

**Chris Gammell:** So yeah, well, I mean, there are some good examples like, uh, you know, maker bot. I mean, that's more hardware side too, but there is a software. Yeah. Yeah. The maker bot. But I mean, yeah, open source hardware might be, I mean, you talked about open source hardware before about, about your unnamed project of unknown origin, but, uh, oh yeah.

**Dave Jones:** You know, I've released a couple of open source projects. Well, everything on my website is open source basically. It's just, it didn't really have a name back then. Um, you know, I was putting, just free. Oh, I was putting projects on my website, you know, 12, 15 years ago. It's not a, you know, in the midnights, I have my website up there and, you know, I was putting project information on there and I love finding old websites.

**Chris Gammell:** I love finding like the old ones, like, uh, like on stumble upon, if you ever use that, where you can just like click through and find like these, you know, these pages that look, they honestly look like they're from, you know, early nineties with like the dancing baby and everything like that.

**Dave Jones:** Oh yes. That's what mine is pretty much like. Yeah. All of my old sites are pretty embarrassing, you know, but. Well, I mean, it's not a big deal. It's all about the information. No, no, the info's there and I still get, you know, they're indexed on Google. I get massive number of hits on them. It's just phenomenal. Oh yeah.

**Chris Gammell:** Yeah. I mean, cause in the end it's, it's just about getting the data there. I mean, I, I found one that I, uh, it was just, you know, a couple of transistor projects that were real fun to play with just single, a single transistor product, uh, project where you're just making like a buzzer or anything else, you know, just current source. And, uh, you know, it's, it's great to see those kinds of things because, you know, you figure that was probably photocopied and passed around before that. And before that, you know, it was just, you know, other engineers were passing it to you or other, other hobbyists. So it's, it's fun to find those kinds of pages, even if they are a little as embarrassing, as you said.

**Dave Jones:** Well, but, but that's the thing. I mean, with, with Google indexing everything, you can, you know, type in your, you know, I, I want to transistor current source, you know, you type that in and bingo, you know, it might find someone's little page. It doesn't have to be on Wikipedia or something like that. You know, you can, um, if, if you've got good, you know, you can have really good content just on one page with one circuit, you know?

**Chris Gammell:** Yeah. Well, what else do we have on the, uh, agenda today, Dave? Do you have anything else?

**Dave Jones:** Um, well, I, I actually wanted to go back and visit the HP thing. Oh yeah. Um, because, uh, I mean, you seem to be quite shocked about this whole HP golden parachute thing. Is that golden handshake? Is, is it that unusual in, in the US for someone to get something like that?

**Chris Gammell:** No, I think we invented it here. Uh, right. Okay. There you go. Uh, I mean, I'm not, I'm not shocked by it in, in any uncertain terms because, you know, you see it every day, but I think it's the, the contrast of HP. Uh, I mean, my own experience about reading about it recently and just like their beginning, you know, like they were, they were pretty humble beginnings. I mean, like they were, Oh yeah, absolutely. I was even reading about the, uh, the first product that came out with today. I was, I, I don't remember how I got to it, but it was talking about, I was reading about oscillators today and that was one of the first HP products, the 200 day.

**Dave Jones:** It was the 200 day, the famous 200 day. Yep.

**Chris Gammell:** Yep. And I mean, like you read about that and like, you know, it's obviously back then that was, that was a really big deal back then. But I mean, you look at it today and just like, uh, it's the, you know, it's an oscillator. Yeah. That's good. That's really cool. I mean, like it's, it's a good bit of history, but like you think about how small the electronics industry was back then and how, I don't know if you ever heard about when they were making their boards. Oh, I forget who it was, Bill or Dave. They were, they were, they were setting the boards in his wife's oven. They were using her oven.

**Dave Jones:** Oh yes, that's right. I mean like, and then they've, they've actually still got that oven in the house. If you actually go to the house there. Yeah. I believe so.

**Chris Gammell:** Wow. I mean like, and then you go, you fast forward, what has it been like 70 some years and now you got some, I don't know. I don't want to swear. I don't want to swear. Yeah. Come on. Yeah. I was going to say, I don't want to swear too much on air, but.

**Dave Jones:** Ah, then I'll do it for you. Some dickhead wanker. Yeah.

**Chris Gammell:** And you know, and it's just, it's tough to see that kind of thing because I mean a lot of, you know, HP is a monstrous company by now. You know, they split off in Agilent. They split off into, I think, I don't know if they were Cree. I think that might've been their lighting division. But you know, they split off a couple of times too. And it's just rough for seeing that kind of thing these days.

**Dave Jones:** I mean, I. Well, I was devastated when Agilent split off and they lost the HP name. Because as far as I'm concerned, I don't give a toss about HP the company anymore because they're not the ones who, you know, they aren't the traditional test equipment company. You know, it's Agilent. So I only really care about Agilent these days. You know, I couldn't give a shit what HP do, really. And I have no comment about Agilent. Yeah, you know, apart from them having the name and they're, you know, trashing the name through doing God knows what. But, you know, I was devastated that when the computer division of HP, you know, the printers and all that got the HP name and the test gear, you know, was forced to change to Agilent. I still call them HP. I don't know about anyone else. But, yeah, you know, yeah, I find it hard to transition to the Agilent name. I'm getting more and more used to it. What is it? 10 or 12 years later or something. Yeah. At least, I think. I think it's about 10 years. But, yeah, you know, it's one of those things. Yeah, I mean, you're right, though.

**Chris Gammell:** It's like HP is, now it's all like, you know, made in China. I mean, we talked about Foxconn last time. They're one of the companies that uses a lot of Foxconn labor to, you know, just make their crappy little mice and, you know, make their better products, too. Don't get me wrong. I mean, they're making good products, too. Oh, no.

**Dave Jones:** HP make good products, yeah.

**Chris Gammell:** Yeah. But, you know, it becomes this behemoth of, you know, cutting, not cutting corners, but cutting people. Like, this guy, Mark Hurd, the one that just got fired, the CEO, I mean, like, that's what he was known for is basically cutting people. And I mean, like.

**Dave Jones:** Oh, right. Yeah.

**Chris Gammell:** You know, like, when it gets to that size, you kind of question, it's such a big thing to move that, like, of course no one's going to question the, you know, getting $30 million a year in salary because you're never going to see that. You know, if you're working in HP even as a top-level engineer or even a top-level manager at a division, you're never seeing that guy. I mean, you're never seeing anybody.

**Speaker ?:** So.

**Chris Gammell:** No, of course not. Yeah, that's more of a corporate culture than it is an engineering culture. And I guess it just stings a little bit because I have been reading about it. So I think that's really where it all stems from.

**Dave Jones:** Yeah, well, have HP lost the HP way? I mean, that's one of the questions. Yeah, that is a good question. If you haven't read the book, the HP way is the name of the book written by Bill and well, I think it was only written by Bill or only by Dave, but it basically describes their management technique. And HP are not only famous for the test gear, but they're famous for inventing the management technique. The MB, what is it?

**Chris Gammell:** Management by walking around.

**Dave Jones:** Management by walking around. And basically, yeah. Yeah. It involves the head honcho just walking around, going to talking, you know, to the guy on the shop floor, on the production line. Yeah. Hey, how's it going? You got any problems? Tell me, direct.

**Chris Gammell:** Shake your hands. Yeah. What's bothering you these days? Yeah. I mean, it's brilliant. And I mean, you know, they're engineers, so that helps. Yeah.

**Dave Jones:** Well, that's right. And, you know, when companies get as big as HP do, well, they don't bring in engineers to run it anymore. You know, the entire board, yeah, they might be token engineers, but they've never actually probably never designed anything. Right. Or they're just, you know, full-time, you know, they're just, you know, just managers and MBAs and everything else.

**Chris Gammell:** Yeah. You know, reading about that stuff with the business side of the thing, it's one of my favorite things reading about that was they, one of their big things was they always had a beer bust on Fridays. And then they always, I think it was just Fridays. And then they always had coffee time where, like, the bell would ring and at 10 o'clock, no matter what, everybody goes and grabs some coffee and a donut and eventually they get rid of the donuts when people start worrying about weight and stuff. And, you know, it's brilliant, though, because then you go and you talk to your coworkers, even in a calm manner, you know, like when you're not, like, stressing over a project. And that not only, you know, makes you bond to your coworkers, but you're probably going to get talking about work at some point. And it might tip off a different part of your brain that it wasn't active before. So, I don't know. I guess I look up to the guys, you know, just from my short amount of research in them. And that's why it really got to me, I think.

**Dave Jones:** Yeah, absolutely. Well, I was actually trying, I was thinking about while I'm in the US, I thought maybe I can get a tour of the HP garage. I've been there, but it's always locked. It's not open for public access. Oh, really? I was, yeah, I was hoping that with my newfound EEV blog fame, maybe they will give me a tour and I can take everyone through the HP garage.

**Chris Gammell:** That'd be pretty cool.

**Dave Jones:** That was, yeah, I haven't, you know, I've done nothing about that apart from think about doing it. So, I might have to contact HP and see if that's actually possible. So, if anyone knows who to contact there, who to talk about, you know, to getting access to the HP garage and the HP house, then yes, please do. Please send me an email because I'd love to get a tour of it. That'd be awesome.

**Chris Gammell:** If you ignore the bad things we've been saying about this guy, I mean, hell, we've just given 20 minutes of airtime to talking about HP. So, maybe they owe you. I don't know. I don't know how this radio slash podcast thing works. I'm guessing we're probably not owed anything.

**Dave Jones:** No, probably not. I think we're, oh, I'll probably get slapped with a cease and desist letter from their lawyers for calling there. Stop talking about us. For saying the guy was after a bit of nookies. So, there you go. Completely unfounded accusation on my part, but I don't give a toss. I'm in Australia.

**Chris Gammell:** Yeah, come get me.

**Dave Jones:** Yep, sue me. What are they going to do? There you go. I'll have to read more into that because I love those sort of scandals when, you know, we had a same scandal here in Australia just recently. There's a $30 million sexual harassment lawsuit. I think $35 million. Yeah. Some woman who worked for David Jones, believe it or not. Not me, but the actual department store.

**Dave Jones:** The same name. Yeah, they're a huge, prestigious department store here in Australia. And this is not electronics related, of course, but it's a good story. And, yeah, he liked to be touchy-feely with the female co-workers. And one of them took offense to it. And, yeah, it's, you know, front page news of all the newspapers. You know, the David Jones CEO step, you know, was forced to step down. Yeah. And I'm sure he got his golden parachute too. It was probably, you know, $10 or $15 million or something as well. But, yeah, he stood down. And now it's all a huge scandal. And it's, yeah.

**Chris Gammell:** Well, maybe we should have a little PSA here, you know, a little public service announcement. Attention, dudes. This is not the 50s. Move on with your life and stop doing that. You will get sued. Dude. Exactly. Because, I mean, that was the same thing that happened at HB. That actually, it was a sexual harassment suit that kind of broke the whole thing open because that's public record. Right. Okay. And that's actually what tipped it all off, I think.

**Dave Jones:** So, yeah. Right.

**Chris Gammell:** You know, come on, guys. 2010.

**Dave Jones:** Exactly. Get with the program. Yeah. Those women are more powerful than you are, dude. Just learn to live with it. Yeah. I mean, you know, with the female CEOs and everything these days, you know, it's a weird, we had a female CEO at our company. You know, it's just so common these days. Yeah. It's a good thing, too.

**Chris Gammell:** You know?

**Dave Jones:** Yeah. It's great. Certainly, certainly not the 1950s. That's for sure.

**Chris Gammell:** Yeah. Well, I know there's absolutely no segue here, but the thing I really wanted to talk about was, you know, human interface kind of stuff. And, you know, you and I had talked about that with the, there was a story about the MSP430 watch on Hackaday, I think. How they're, what was it that was doing?

**Dave Jones:** They converted it into a mouse, which is like, yeah, okay, so it's got an accelerometer into it. It makes sense. I don't know what the big deal was, you know? Yeah. Because, yeah, it hooks up, it simulates a mouse, and you wave your hand around, I guess, and you can actually, I think you can actually click. So, if you go like that, that's the mouse click, you know? So, yeah. That's pretty cool. Oh, yeah, that's kind of neat. So, yeah.

**Chris Gammell:** Yeah, I just, I think that that's a really big field that's kind of still emerging is like the, I mean, accelerometers are there, obviously, and you've got pressure sensors and temperature sensors. But, like, what is, I mean, you think about, like, we're still using keyboards right now. I mean, like, you and I are using microphones, obviously, but, you know, like, what, I mean, there's no detection in these microphones. Nothing's, you know, we're not flipping any switches with this, and it's been around. Exactly. What do you think the future is? I mean, like, I don't know what it's going to be, but.

**Dave Jones:** Well, everyone's talking about voice recognition. They've been talking about voice recognition for 30 years or something like that. Yeah. I played with a voice recognition chip back in the early 80s, you know? Yeah. It recognized 20 different words, and where's it come? Well, it's come a fair way. They're reasonably accurate these days, but it still hasn't found its way into anything, and I don't think it will for quite a long time. There's just too much variability.

**Chris Gammell:** I know, yeah. I mean, like, even look at you and me and how I say Aussie.

**Dave Jones:** Yeah, exactly. Yeah, I mean.

**Chris Gammell:** I doubt there would be a chip that could possibly discern what the hell you're saying. I mean, that's true.

**Dave Jones:** Well, there's not. If you go to YouTube, you can turn on, apparently, you can turn on the closed captions. Oh, really? And it automatically tries. Yeah. It automatically tries to recognize your voice, and it does a horrible job with my Australian accent. So you'll see subtitles. I didn't put those subtitles there. You can turn on the closed caption thing, and it just talks gibberish. That sounds like a fun game. It's absolutely hilarious to watch it try and interpret my Aussie voice.

**Chris Gammell:** Yeah, maybe we can get someone to try and post a transcript of that sometime and see if you say it. I mean, even when you're saying it really. Somebody did on the forum, I think. Oh, really?

**Dave Jones:** Somebody's actually posted some screenshots and stuff like that, and I just, oh. Oh, that's awesome. It's hilarious what it comes out with. It's just unbelievable. But yeah, like, you know, nobody wants to sit there and train their new product with their voice, and then, you know, it won't recognize you if you're upset or stressed or whatever. Yeah, yeah. It's just not going to work, you know. That's why the keyboard is still around, you know. Yeah. And it will be for, God, you know, the foreseeable future, which is, you know, 10 or 20 years at least. Yeah. I think it'll be around for the next 100, probably. Yeah, I mean, there's always. The keyboard is just so good.

**Chris Gammell:** You've got to get in there somehow. You've got to get text in, right? I mean, so.

**Dave Jones:** Yep. And you want it 100% accurate, you know. You don't want to be dicking around. Obviously, you've never seen my typing. It's bad enough that if you suck at typing, you know, or you're an engineer and you can't spell, you know. Right. What was yesterday? Oh, sorry. I was just going to say the famous line. Ah, forget it. Oh, error between. Let's not go there. The error between desk and chair. And then I couldn't spell engineer and now I are one or something like that. Oh, man. Engineers can't spell, which is the classic stereotype.

**Chris Gammell:** Yeah, not as big an issue these days as spell check. But, I mean, the interface thing, I mean, I don't know. I see it going a couple of places. But, yeah, I guess you're right about the speech to text kind of thing. I mean, you think about it. If they ever did perfect that, I mean, not even perfect it. If they got a little better and then you get, like, Google Translate. I mean, I don't know if you've ever tried Google Translate before. Yes, I have. Yeah. That's pretty great, I think. I mean, for what it is, it's pretty good.

**Dave Jones:** It works pretty well. Yeah.

**Chris Gammell:** I mean, you combine those two and basically you have a universal translator. Now, I mean, you don't want to use it at the UN and discussing, like, some kind of war sanctions. But, you know, that's still pretty cool. I mean, I made a list a couple years back about, you know, like, inventions that I think, you know, would change the world. And that's definitely one of them. I mean, you think about people getting on the same page for language. That's definitely one of them. So, I mean, you combine those things.

**Dave Jones:** I totally agree, yeah. Yeah.

**Chris Gammell:** I don't know. The one thing I did see last week, I don't know if you saw it, was the Waterloo Labs.

**Dave Jones:** Oh, yes, I have.

**Chris Gammell:** Those guys down in Austin. They actually, there was a bunch of views on it. And it was on all the boards, too, about the iMario where they hooked up, like, I think, instrumentation amps to people's eye sockets. Oh, really? Yeah, and they detected which way their eyeballs were looking based on the polarity it was flipping. Apparently, your eyes have, you know, send some kind of synaptic response there. And basically, I didn't get a chance to watch the video yet, but basically, they can control Mario with their eyes. And you look up, he jumps, and, you know, you look left and right, and he goes left and right. I mean, so maybe that might be another way to interface the people, but it's still pretty young.

**Dave Jones:** Well, they're doing that optically now, aren't they? You don't actually have to attach sensors. You can actually get face, you know, software which you can stare into a webcam, and, you know, you can move your eyes, and it, you know, it can move a robot or something like that. So, yeah, it's... Yeah, that's not quite...

**Chris Gammell:** I mean, because you get eye jitter then, too, but, like, when it's, like, a really... The thing that's nice is it desensitizes it, because, you know, then when you're... you mean to look left, you're looking left, whereas if you're staring at something straight on, your eyes are always jittering, too. So, you gotta get that... you gotta get that out, too, but... I don't know, uh... So, that might be another way to... I don't know, there's the accelerometers right now, and maybe you can count that, but...

**Dave Jones:** Yeah, gyroscopes and accelerometers are big, and there's, you know, I... All these, um, user interface, you know, they're always going to be niche, you know? I don't think any one thing is just gonna, you know, take over the world. It's just, you know, it's just not really possible. There's just so many permutations and combinations of things that you have to do out there, you know? Ways you have to interact with a product or a computer or something like that, and it's just... Yeah, there's one no universal solution, I don't think.

**Chris Gammell:** Which is good for us, too, because, I mean, then we, you know, have jobs. Yeah, well, exactly, yeah. Not necessarily human interface, but, uh, you know, if there weren't niche-y little places where people could work on electronics, I don't think I'd have a job, and I don't know about you.

**Dave Jones:** No, I probably wouldn't either, that's right.

**Chris Gammell:** Yeah, so, I mean, in that regard, it's good that, you know, there are not just one solution for electronics, and that'd be boring anyways.

**Dave Jones:** No, yes, it would, but, yeah, I find the whole user interface field quite fascinating, you know? Yeah, and it's... I've, you know, I'm laying out boards, you know, I'm constantly thinking, oh, I'm laying out boards, and I'm using the mouse, and I'm using the keyboard, on, you know, a very complex operation, you know? Yeah, yeah. I'm always thinking, you know, how could you simplify something like that? You know, I've got it all up in my head, you know, the layout of the board, and what I want, and it's all flowing out, and I've got to translate that into key presses, and mouse clicks, and drags, and, you know, ah, if there was some...

**Chris Gammell:** And plus, now you have 15 years of experience doing it that way, so then you have to try and break away from that, too. That's right. Yeah, it's a tough... Go ahead.

**Dave Jones:** Yeah, but you see in the movies, like, Avatar, I don't know if you've seen Avatar. Yeah. I'm sure you have.

**Chris Gammell:** Yes, I have.

**Dave Jones:** Yeah, you know, how they have their, you know, everyone made a big to-do about all the big touch panels they had, and stuff like that, you know, I think there's a big future there. Yeah. You know, because I would, you know, I can picture myself, you know, like, when I'm laying out a board, for example, like, sitting at a large, just a large glass table, and just doing hand gestures, you know, like, yeah, I want to drag that part over there, and doop, doop, you know, all that sort of...

**Dave Jones:** You know, hand gestury kind of stuff.

**Chris Gammell:** Minority Report, you ever see that movie with Tom Cruise? Oh, yes. Yeah. I think that was, like, a big one where they did that, too. Yeah. I saw that, you know, Microsoft actually made a table that did that at one point, but it was, like, really clunky, you know, where, like, you could put a camera down on it, and then it would, like, show, it would, like, kind of, like, fan out all the pictures, and you could throw them all over the table and everything. Yeah, I think it's called...

**Dave Jones:** I don't know. Was it Smart Table or something like that? Yeah. Or something they call it? Smart Canvas or something they call it? I don't know. Yeah. But it's just so expensive, though. Yeah, I mean, I think that's where a huge future is there.

**Chris Gammell:** Yeah. I mean, yeah, and you see it, too, in the chip market. Like, any time you talk to a chip vendor these days, they're like, oh, can I tell you about my capacitive touch sensor and blah, blah, blah, and it's like, well... Oh, yeah. I don't really care. Sorry. Oh, really?

**Dave Jones:** Oh, I think they're very cool. I mean, you know... Well, they're cool, but... Every... Yeah, I think I can see five years down the track, every pick and every AVR and every other microcontroller on the market is going to have a capacitive touch sensor interface. Yeah, I... No, I don't think so. I think they're really pretty cool. I mean, I don't doubt that... As much as I... You know, as much as I like the, you know, a nice, good, you know, nice, good push-button switch or a nice knob, you know, I can really see the future in the capacitive touch sensor interface for sure.

**Chris Gammell:** Well, I mean, I don't doubt there's a future and I don't... I mean, it is cool. I don't want to backtrack on what I said and let you win here, but I don't think that that... I don't think that they're... You know, I don't think it's going to be useful enough to the tiny little market, you know, like that kind of stuff that it's going to be useful. And even, like, I just think that they're going to be everywhere, but they're still going to be niche-y, you know? Like, I don't think they'll be everywhere, everywhere. Because even if you have the tiny AVR or a MSP430, it's still pretty intensive to get all that information back out and then, you know, use that as your interface device, so...

**Dave Jones:** Oh, it kind of is, but I'm... Even now, when I do a new project, I'm thinking, right, you know, it needs some switches on the front panel. Well, they're going to cost, you know, five or ten cents a pop, you know? And if I need a few of them, well, my chip comes with a capacitive touch sensor interface. Why don't I use that, you know? It's... Yeah. So, I'm always sort of thinking there, you know, how can I actually, you know, lower the system cost there? And that's one of the ways, you know? Because you have to design your PCB anyway, so, you know, if somehow you can, you know, add in a switch for free, then why not?

**Chris Gammell:** Are you talking about the switches where you actually just, you do it in the trace where you have that? You do it in the trace in the PCB, yeah. Ah, okay, okay. I thought you were talking about the LCD, because, I mean, that makes a lot of sense, right? I thought you were talking about, like, the LCD cap touch where you have, like, the whole

**Speaker ?:** matrix.

**Chris Gammell:** Oh, no, no, no.

**Dave Jones:** That's an entirely different concept, really.

**Chris Gammell:** Yeah, you know, that's great, then, because then it's just integrated in the board. I mean, that's smart.

**Dave Jones:** Oh, yeah. Yeah, it's fantastic. I think there's a huge market there for that. Yeah. And so do all the vendors, because they're all coming out with... Almost every micro on the market now has a cap, you know, touch-sensitive cap interface. So, yeah. Oh, okay.

**Chris Gammell:** I was talking about the, you know, the discrete chips. Have you ever seen... That's what I was talking about with the vendors talking to me about it. Like, they're always like, oh, well, we have this, you know, LCD sensor chip, basically. Yeah. And that's what I was talking about before, so... Right. Different wavelengths, I guess. Different wavelengths.

**Dave Jones:** Yeah, absolutely. There you go. And we've got the Skype thing here where we can't... Oh, yeah. If we talk over each other, it just sort of dies on us, which is really quite annoying.

**Chris Gammell:** Yeah. Well, any other...

**Dave Jones:** I'm sure you guys can't hear it at your end, but, yeah, if we talk over each other, we can't hear, and that actually distracts our train of thought, and, yes, and we get lost sometimes.

**Chris Gammell:** Yes, we do. So, any other interface devices you see on the horizon? You got CapTouch, you got maybe vision tracking?

**Dave Jones:** Yeah, the accelerometers, the gyroscopes, they're huge. Everyone's doing that nowadays, so you can, you know, shake a product, and everyone's coming up with these new concepts. You know, you've got your accelerometer, you know, you might shake something, or the new Ti Watch, as we said, you would actually click like that, and that would simulate the mouse click, which is kind of neat, but it's not very practical, I guess. And, you know, but those things have been around for 30, 40 years. You know, the old lamp, you know, the bedside lamp where you clap. Oh, yeah, the clapper, yeah. You know? You know, God knows how many decades they've been around for, but, yeah, I think people are going to come up with, keep coming up with these, you know, great user interface ideas, and, well, some of them are just going to be, yeah, neat concepts, but, you know, they're not very practical, but.

**Chris Gammell:** Yeah, the one you've been seeing for the past 30 years, like the heads-up display. I don't know how many times I've seen a, you know, oh, brand new heads-up display, and then it's like, you know. Well, where'd it go, guys? I'm waiting.

**Dave Jones:** Exactly, they've been around for 40 years, at least, I think.

**Chris Gammell:** Yeah, I saw that there was one guy that he made like a, that might have been a hackaday, or someone like that, it was talking about, he had a whole computer, and then he made his own heads-up display with it, where you could actually, like, he, I mean, he looked like uber nerd, but it was, like, awesome, where he had, like, a keyboard across his chest, like a, like a band of ear, and then, you know, it is, but, you know, that, he had that, so, you know, maybe that, maybe that's the future. Maybe it'll be in your glasses, guys.

**Dave Jones:** Exactly. Well, I think there's a big future in these virtual keyboards. Have you seen these? Yeah, yeah, people projectors. On the phone, they, they, they actually, actually project a keyboard onto the desk, and you just, you know, it's got a little camera, and it watches where your fingers go, and you can put a keyboard anywhere, you know, up on a wall, on your desk, on the floor, doesn't

**Speaker ?:** matter.

**Chris Gammell:** Yeah, that's, that's using the Pico projectors. I was, I was talking to someone on, I think Chip Hacker about that, because there's a development, you can get, like, 350 bucks, you can get a, a TI development kit, where it actually talks, like, VGA, or HDMI, or something, and it'll actually project it for you, and it's like, it's only, like, seven lumens, so it's, it's kind, it's kind of faint. Yeah, yeah. Ah, right. But, I mean, that's pretty cool, I mean, like.

**Dave Jones:** That is very cool.

**Chris Gammell:** I mean, like, you talk about, like, you know, say you have your, you know, your, uh, Android smartphone, and you're hanging out with your buddies, and you're like, hey, let's watch a movie, and you plop your phone on the table, and you just kind of start projecting on the, you know, you start projecting on the screen, that, that's, that's pretty cool. That is awesome, yeah. I, I do see a, a market for, uh, you know, digital, uh, graffiti, you know, set up one of those things somewhere, and project some lewd images up on a wall.

**Dave Jones:** I've seen that, yeah, that's, you know, and, and you can express yourself and leave nothing behind, you know. Yeah. Except the $600 smartphone. I could, I could really get into that sort of thing, it's, yeah, it's just great. Oh, there's so many ideas, so many time, you know, so many, so much cool stuff to work on, and, well, let's segue to that. We're out of time, I think. I think we are. We've done our hour, haven't we?

**Chris Gammell:** I think we are. Yeah, uh, our amp hour, I guess.

**Dave Jones:** We have to live up to our name, the Amp Hour, there you go, is the new name for the show, and so we'll call it quits. It's been a good one, I think, Chris, as usual.

**Chris Gammell:** Yeah, we, we, we meandered a little bit, but I think, I think we got through everything we wanted to, uh, I just want to remind everyone, if you want, if you got, there's a suggestions tab on the amp hour.com right now, and, uh, you know, if you are HP or Cree or anyone else and you're listening, there is an advertising tab as well, which is underutilized at the moment, and we'll see how that goes. Yeah, absolutely. We might not really be able to make a buck from it. Not, uh, yeah. Anyway. Not, not holding my breath.

**Dave Jones:** Yes, exactly. And, um, yeah, and also feedback on the format of the show, too. I mean, I think we covered a lot of stuff today. We did, yeah. I think there was, you know, four or five, half a dozen different, uh, things we talked about, if you like, that sort of, uh, sort of random, um, format, or do you prefer just to cover one or two, um, topics and keep it simpler? Let us know.

**Chris Gammell:** Yeah. And, oh, and also the, uh, site design, we already got some good feedback from the EEV blog forum, but, uh, you know, I just, uh, worked up some CSS crap, and, uh, it's not the best. I'm not, I'm not a designer, you know, not a graphic designer, at least. So, you know, if you got any feedback, if anything doesn't look right, or it's not rendering right, just leave that in the comments, too, and, uh, and I'll, uh, try and fix it.

**Dave Jones:** Absolutely. Well, thanks for listening, everyone, and we'll see you next time.

**Chris Gammell:** Yeah. Thanks a lot. Bye.
