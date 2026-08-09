---
episode: 131
title: An Interview with Andrew Seddon - Necessary Networked Novelty
url: https://theamphour.com/the-amp-hour-131-necessary-networked-novelty/
---

**Chris Gammell:** This is the Amp Hour Podcast, recorded February 4th, 2013. Episode 131, with guest Andrew Seddon. Necessary Networked Novelty. Welcome to the Amp Hour. I'm Chris Gammell of Chris Gammell's Analog Life.

**Andrew Seddon:** And I'm Andrew Seddon, Embedded Engineer and Co-Founder of CircuitHub.

**Chris Gammell:** Well, welcome, Andrew. Thanks for coming on the show.

**Andrew Seddon:** It's a pleasure to be here, Chris.

**Chris Gammell:** So we actually talked about your startup last week, and then we've had some changes in our guest lineup, and then you were nice enough to come on the show this week. We had actually talked to you about coming on the show a couple weeks from now, but you were able to move up your schedule, and we're really glad that you were able to come on here. So you sent me an email, and you had said, Oh, I have some corrections about what you said last week. And I'm like, Well, you should just come tell us, right?

**Andrew Seddon:** Yeah, it was. So it was funny, actually. But John and I, my co-founder, was sat there listening to the podcast and listening to you guys discussing CircuitHub. And it's a fantastic discussion, actually, and it was really insightful for us because we kind of got to see some of the things that people typically misinterpret about what we're doing. So I think I then pinged you an email sort of, you know, with a couple of corrections for what it is that we're actually doing. And then, yeah, obviously, happy to come on here and talk about it, too.

**Chris Gammell:** Yeah. Well, before we get into that, so why don't you tell us a little bit about your background? Because when you and I first started talking about CircuitHub in general, I was really amazed because, you know, you're doing this high-level software startup with this really beautiful UI and this interesting concept that Dave and I had talked about previously. But you actually come from an embedded engineering background. So where did you start and, you know, what's your electronics story?

**Andrew Seddon:** Yeah, sure. So, yeah, very much from electronics. I mean, some of my earliest memories are, you know, sort of tinkering around with electronics and piecing circuits together. So, yeah, really that's – for me, it's been a big jump to move into the web development space. It's – I started very, very low-level electronics and building circuit boards. And to some extent sort of doing embedded software as well, but certainly sort of moving up into the web, the web side of things has been a big, big jump.

**Chris Gammell:** Okay, cool. And so you started out over in London, right? But then you've kind of moved around a little bit. What were some of the places you worked at over there?

**Andrew Seddon:** Yeah, so, I mean, I actually – so I went to university up in Leeds and did electronics engineering up there. But probably in the last year that I was there, I moved down to London. And when I was there, I basically – so I sort of – although I really enjoyed studying electronics at university, I wasn't sort of so interested in the theoretical side of things. Like I always really wanted to try and actually build stuff. So pretty much in my last year of university, I kind of started, I guess, a kind of small design consultancy. And I kind of had some interest in that from a small startup that was based down in London called TurnSafe. And they were basically doing a really cool project to – it was kind of a safety system for articulated trucks.

**Chris Gammell:** What's an articulated truck? Hopefully, I'm not the only one who doesn't know what that is.

**Andrew Seddon:** Yeah, so an articulated truck is basically it's a truck that pivots in the middle, right? So you have the cab at the front and then the trailer behind. And then the pivot's in the middle of it. Basically, what that company was doing was a mirror that moves at the same time as the trailer moves. Huh. And what's useful about that is that it allows you to see the inputs in the mirror whilst the truck is actually turning.

**Chris Gammell:** Wow.

**Andrew Seddon:** So this system really, really helps with safety. And yeah, so they basically wanted somebody to come down and basically work on a DSP system, an embedded computer vision system effectively. So I pretty much dropped out of my last year of university, went down there and helped these guys to design this system. So I really just kind of fell into doing design consultancy.

**Chris Gammell:** And that was DSP type stuff that was – so it was actually using like camera feedback, that kind of idea? Or what was that? Yeah.

**Andrew Seddon:** Yeah. I mean, but basically, so that system was – it had a camera that looked back at the truck. And so it looked back at the carriage behind the truck. And from that, you can then compute what the angle of the trailer relative to the actual – relative to the truck at the front. Huh.

**Chris Gammell:** Huh.

**Andrew Seddon:** And you can then sort of transform that to come up with an angle for the mirror itself. So it's kind of like a pretty interesting control system, computer vision system there. Yeah. And then the challenge was kind of to get all of that software actually running on an embedded system and kind of make it reliable. And, you know, obviously, if it's a safety system, this thing has to be very reliable. So, yeah. I mean, that was my kind of – that was my first, I guess, real commercial experience with electronics. But certainly before that, I'd been doing an awful lot of things as a hobbyist.

**Chris Gammell:** What kind of stuff was that?

**Andrew Seddon:** So, I guess probably the first project that I can think of that I ended up doing was – I used to be really into model rockets. So, sort of firing model rockets. And what I wanted to do was be able to track those rockets so that, you know, I would know the coordinates, the coordinates of where – you know, how high the rocket was, where it was, et cetera. So, I actually did a project. The idea was I was effectively, although I didn't realize it at the time, was trying to design like a – pretty much like a GPS system. Huh. And this was a really, really early project. And so, I ended up building this kind of – what at the time was a pretty high-speed timer system. So, I had this, like, timer running at 100 megahertz. And the idea being that I'd be able to count the – or time the sort of round trip of a radio signal so that I could then sort of pinpoint the location of this model rocket. So, I sort of put this high-speed timer together and then thought that the whole radio side of it was going to be the easy thing.

**Chris Gammell:** And then I just do some RF and what's the big deal, right?

**Andrew Seddon:** Yeah, exactly right. I mean, the whole sort of Fourier theorem thing was not something I was aware of at the time. So, yeah, that didn't quite work out as originally intended.

**Chris Gammell:** Well, that's interesting. And so, then from – so, this was all still in London though, right?

**Andrew Seddon:** Yeah. I mean, this was generally around London. I mean, I sort of grew up around Cambridge area. So, you know, sort of this would have been, yeah, either in and around Cambridge. I actually had – when I – so, before university, I was working as a – I was working at another startup called Active RF. And those guys were doing basically RFID tagging systems. So, active RFID tagging systems.

**Chris Gammell:** Oh, okay. So, it actually receives the signal. It harvests a little bit of the energy and then actually bounces back an intelligence signal versus just the, you know, the response of the chip, that kind of thing? Or is it something else? Yeah.

**Andrew Seddon:** Yeah. I mean, this wasn't quite so advanced at the time. I mean, this wasn't really kind of energy harvesting. They actually had – actually, it was pretty old-fashioned to have batteries in them. So, you'd have – I guess it's not really how you would think of an RFID tag today, which is kind of a very thin, you know, sort of looks like a bit of paper. These things were more kind of mobile phone sized, I guess. And, you know, they have batteries in them and RF systems so that you would get kind of a low-frequency trigger from, you know, from an RFID gate. And then they would ping back a high-frequency response.

**Chris Gammell:** Huh.

**Andrew Seddon:** Okay. So, that was – yeah. I mean, that was – I originally didn't really actually have any intent to go to university. I'd sort of – I'd been fiddling around with electronics for probably a few years whilst at school. Applied for this job at Active RF. Went in for the interview. We got on like a house on fire. I showed them some of the electronics I was working on. Yeah. And these guys are just great. You know, when can you start? So, that was a really fun year, actually. Yeah. I got to basically do what I was doing anyway but sort of have somebody pay me to do it which was kind of nice.

**Chris Gammell:** Well, that sounds like the classic example of bringing in like a portfolio type piece and then, you know, that being the centerpiece of an interview, right? Where you, you know, you walk in. This is what I made. Let's talk about it. Oh, okay. Let's forget all these questions we were going to ask most people. But, yeah, you know, most people love talking about that kind of thing.

**Andrew Seddon:** Exactly. I mean, I think that's a great – it's a great thing to do because even to this day, if I'm actually interviewing people, I mean, that's kind of how I will sort of pose the interview is that I will try and get them to talk about something that they're passionate about, right? Because I think if you are, you know, if you're a maker, if you're somebody that, you know, you're an engineer and you actually make stuff day to day and you're good at it, you will have projects and, you know, you'll be passionate about the things that you're working on. Yeah. So, yeah, it was a great experience, that initial interview, and I think it's definitely something that's kind of carried on, you know, sort of followed through as I've switched roles in that sort of space.

**Chris Gammell:** Yeah. So, I was going to ask you in general. I mean, I know a couple people over in the UK, but what is the London scene like? I mean, I guess that's something that I don't really have much exposure to. That's the thing I really enjoy hearing about, even within the States, you know, different parts of the country. Like, my part of the country is real big on industrial. Out in California is big on RF and a lot of other things like that. You know, Midwest is generally, you know, military, stuff like that. But what's the London scene like?

**Andrew Seddon:** Yeah. So, I mean, London itself for electronics is pretty barren in terms of hardware itself. Okay. And I think that's simply because there's so much going on elsewhere in the UK.

**Chris Gammell:** Okay.

**Andrew Seddon:** So, I mean, the kind of traditionally, I guess, probably the home for hardware would be Cambridge. Okay. So, that's, you know, sort of certainly where companies like Arm. Oh, yeah. Cambridge Silicon Radio. There's also quite a few sort of semiconductor startups as you sort of on the, they call it the M4 corridor, which is kind of west of London. So, I think generally, like in terms of hardware, it doesn't actually tend to happen in London itself just simply because of the property so expensive.

**Chris Gammell:** Yeah.

**Andrew Seddon:** Yeah. Would be my guess. And, you know, if you have to set up a lab, then, you know, it's pretty crazy to be paying five grand a month for a lab in central London when you don't need to be there. Right. And, you know, the cost is half as much if you go out to Cambridge, Oxford, Bristol, wherever it may be. So, London itself for the actual sort of hardware scene is on a professional level is pretty quiet. But actually on an amateur level, I think it's actually sort of growing pretty fast the same way that it is or seems to be sort of all over the place, actually. So, they, I think a couple of years ago now, started a hack shop in pretty much in central London. So, last time I checked, I think they sort of had a couple of thousand members. And that's basically a place where you can, you know, they have all the tools set up for you to use. So, you can add your own PCBs, you know, and they have the CNC mills and all sorts of equipment that you can use if you actually want to make stuff. Yeah. So, the actual amateur scene, I think, is, yeah, is really on the up and up. But professionally, it tends to get sort of budged outside of London.

**Chris Gammell:** Yeah. Yeah, it's interesting. I mean, especially in city scenes, you know, like because space is at such a premium that, you know, like hackerspaces can do, they can really do that with, you know, there's no way you're going to, I mean, very few people will have, you know, like routing tables in their apartment, right? Just because it's not economical. It's not allowed sometimes. So, those hackerspaces really benefit from that. And that's great. But, yeah, I've actually lamented that before in the past about, you know, being an engineer. And it's like, well, you know, I'd love to live in like a metropolitan area. But good luck, you know, there's so, it's not that it doesn't happen. It's just very few because of that same problem you said, you know, that even like in a Cleveland, right, where downtown space is not necessarily difficult to find. It's just the amount you can spread out in the suburbs or in the outlying areas is often just so much more. And tax codes are often different, you know, it's just set up that way. And it's kind of unfortunate because you don't get to experience a lifestyle, you know, you have to live a little lower key lifestyle if you want to live close to work. Yeah.

**Andrew Seddon:** It's funny, actually. I mean, I do think things are really changing. I mean, you kind of have these tech shops and hack spaces are springing up now. And I mean, even as much as or as near as three or four years ago, that wasn't really an option. I mean, I know, for instance, now over in San Francisco, they have a tech shop there where you can go and use all of the equipment. And these things are pretty, you know, they're pretty well equipped. They've got a lot of what you would need to do things even on a professional level.

**Chris Gammell:** Oh, yeah. Yeah. A lot of companies will probably see popping out of there in the next couple of years as well. I mean, they're just they're good, not just because of the equipment, but also because of the concentration of other like mounted people. You know, that just that whole kind of critical mass thing really helps.

**Andrew Seddon:** Yeah, for sure. And I think it's things like that that are that are that are really contributing to this rise in hardware. I think, you know, it just it traditionally it has been incredibly prohibitive to get into this stuff on an amateur level because I think the bar is so high now. Yeah. With what you have to do in hardware to do something original.

**Chris Gammell:** Yeah.

**Andrew Seddon:** You know, if you if you're doing something with some with some complex FPGA or DSP and or you're specifically if you're trying to make something for a consumer level, it tends to be very small. And if you if you're trying to make small electronics and, you know, using small packages and high density PCB technology, this isn't the sort of stuff that you can you can do in a tank at home. Right.

**Chris Gammell:** Right.

**Andrew Seddon:** You need this equipment. So, yeah, I think it's fantastic. And I'm I just think it's a shame that it wasn't around five years ago when I could have used it a lot more.

**Chris Gammell:** Right. Right. So. So I guess I guess that leads us into it. I mean, what. So now you are. What kind of programming language is doing like Ruby and high level stuff, JavaScript? I mean, high high level HTML5 type stuff. No JS. Is that right? I'm looking at your LinkedIn. Yeah. LinkedIn. Yeah.

**Andrew Seddon:** Yeah. So. Yeah. We sort of jumped in on the deep end, really. Yeah. We we we pretty much use a JavaScript stack from from top to bottom.

**Chris Gammell:** OK.

**Andrew Seddon:** Well, we actually use we actually use CoffeeScript, which is a one of these newfangled compiled to JavaScript languages. OK. Yeah. And we we kind of I guess we've we've bit off quite a big problem because we we knew what we were going to have to do was pretty cutting edge by anybody standards. Right. Not just cutting edge by by the web development standards. It was it was you know, this was generally a lot more than than anybody had done before in in any field, not just electronics. So we we had to build this application in a in a very different way to a traditional web application, which effectively meant meant writing an awful lot of JavaScript. An awful lot of sort of front end GUI framework stuff, which was very, very different for me.

**Chris Gammell:** So was it was it actually so so obviously for people not paying attention to the first part of the show, we're talking about Andrew's jump to Circuit Hub. But were you doing software before that? I mean, was it like was this something that you had already been doing higher level languages or was it OK? I am an electronics designer. I see something that I want to make and now I'm going to go develop software.

**Andrew Seddon:** Yeah, I mean, I'd always I'd always been involved in software in one form or another. OK, I mean, a large part of what I did was kind of embedded systems development. So it would generally be much lower level, lower level type stuff. So, I mean, I spend quite a lot of time writing C code doing it. I would tend to do either sort of really low level driver stuff or algorithm stuff and quite a lot of kind of optimization of algorithms.

**Chris Gammell:** OK.

**Andrew Seddon:** Which, yeah, is obviously a very different end of the spectrum to writing a web application.

**Chris Gammell:** Right. I mean, like so I am my C code is just horrendous. I've been getting back into it and it's not great by any stretch. But then does someone come and say to me, OK, well, now we want you to go read some high level abstracted, you know, object oriented language. It's like, oh, OK. I mean, so so did you do that to yourself? Was that something like, OK, well, I guess I'll just go learn this stuff. Is that kind of the idea?

**Andrew Seddon:** Yeah. I mean, it was really a really a case of masochism. Yeah. But my head on a brick wall until it until it stuck. Really. I mean, it's funny, actually. I sort of I was looking at some some tweets the other day that I made at the time, basically just in expressing my frustration at how stupid it is to do web development. You know, all of the all of the weird things that you have to jump through to make to make these things work. And it's I think I think the biggest difference is that you're you're you're building on top of other people's abstractions. Yeah. So it's not like you can work these things back from base principles. Right. You know, if you're if you're working on embedded system, you can you can say, OK, well, I can look at the registers and then pretty much everything above that is under my control. And, you know, I can see the code. But when you're working on the web stack.

**Chris Gammell:** And in the worst case scenario, you go and you say, well, whoever wrote this or whoever designed the silicon messed it up. Right. And that's very rare. But then now you're as a web developer, you're looking down on these these abstractions. And you're like, well, there's so many places to mess up. Right. There's so many more variables.

**Andrew Seddon:** Yeah. I mean, it's it's you could you know, you can never comprehend the whole stack that you're working with. You know, you're always sitting on top of somebody else's abstraction. And I think the big thing with that is that it means you kind of have to you have to learn their arbitrary rules and the arbitrary decisions that they've made about how they're going to present that abstraction. So it kind of to me almost feels kind of a lot less pure in a in a programming sense. But it is kind of it's kind of almost countered by the sort of instant gratification that you get where, you know, if you're designing an embedded system, you might you might work for three months to make an LED flash.

**Chris Gammell:** Yeah.

**Andrew Seddon:** Whereas in like two days in web development, you can you know, you can sling up a website. Right. So it's a kind of different. That's the basis of startup weekends, right? Well, it's funny enough, actually, they it seems like they're starting to get some some hardware startup weekends as well.

**Chris Gammell:** Yeah, I saw that announced. I didn't up for her. And who is someone who was co-sponsoring that this coming? Yeah.

**Andrew Seddon:** So so so we're actually going to be co-sponsoring. So we're circuit hub will be co-sponsoring the the hardware hackathon. It's going to be held at Y Combinator.

**Chris Gammell:** Ah, OK. So tell us tell us a little bit more about that.

**Andrew Seddon:** Sure. So we so it's actually I mean, we recently we recently had a lot of circuit hub launch. We've been kind of working away on this for, I guess, probably probably a year in earnest now, actually sort of sitting there and really heads down writing code and testing out, testing out this testing out this product that we're building. And we so so we actually we launched last week. I think this was it was. Yeah. Sort of last last Tuesday. That's all been a bit of a blur since then. So I'm just oh, yeah, just trying to remember. But yeah, I think it was last Tuesday we launched. And yeah, so I think we sort of we mentioned in the press release for that that we we went through Y Combinator at the start of this year. So this was this was kind of January to my end of March time. We we sort of participated in the in the Y Combinator winter 2012 batch. And yeah, it's a fun experience.

**Chris Gammell:** OK, so so the the actual hackathon, though, so that that's a that's going to be when is that when is that happening?

**Andrew Seddon:** Yeah. So so the hackathon, I need to check my dates on that, actually. But I think I think that's pretty I think I just found it.

**Chris Gammell:** Is it is this the right one? Oh, yeah, there you are. Yeah, you're on that list as well. So it's February 23rd, 10 a.m. to 10 p.m. Is that right? That sound right?

**Andrew Seddon:** Yes, that's the one. Yeah. So so you can apply for it now. You can you can go on there and apply for it now. You can there's going to be about 80 teams. Maximum of 80 teams accepted. Yeah. It's yeah. Should be should be good fun.

**Chris Gammell:** And there are other other names that we recognize in here. There's Lockatron, which is the web enabled lock. There's Octopart, which is the the they're not scrapers. They're they they kind of pull in other other like DigiKey and Mauser. They kind of go out to all the different distributors and search for stock and stuff. And then there's Pebble, which is the I think that's the watch, right? There's not.

**Chris Gammell:** So yeah, Pebble is the smartwatch. Yeah. Yeah. And then Uproader and then Y Combinator are doing that as well. So all great. That's kind of like the you guys. All of you are kind of like the intersection of hardware and software. And kind of getting stuff done. So that's cool. That's really cool. I don't know. So what do you think? So you've been doing an embedded for a long time. You get 12 hours to do hardware. And really, it says 10 a.m. to 12 p.m. So here's the schedule. Registration, ideation and team formation for two hours from 8 to 10 a.m. Hacking tools and hardware. How to 10 to 12. Lunch is an hour. Hack for six hours. Dinner for an hour. And then prizes for two hours. And all I can think is I can hardly get CAD set up in six hours, let alone actually making something. How would you go about doing this kind of thing?

**Andrew Seddon:** Yeah. So, I mean, nobody's expecting you to kind of, you know, walk away from this thing with a complete product. I don't, you know, you've got to have a realistic expectation here. I think the main thing here really is to, I think it is entirely feasible to have a, by the end of that time, have a very solid idea of what it is that you're going to do. And a kind of pretty well sketched out in CAD diagram, you know, of what you're going to make. And I would say probably for, it depends on the sort of the complexity of what it is that you're trying to achieve, right? I mean, if you're trying to make something very simple and you can kind of piece this thing together out of dev boards, then I guess it's actually feasible that you can have something working by the sort of end of that time. But at the very least, you know, you're going to be well on your way to having something put together. But, yeah, I think if, you know, there'll be a range of dev boards available. I think that, you know, there's going to be some Arduinos floating around.

**Chris Gammell:** Yeah.

**Andrew Seddon:** And a few other dev boards. Yeah, Wi-Fi shields. So, I think it's entirely possible.

**Chris Gammell:** Yeah, all that kind of stuff.

**Andrew Seddon:** So, I think, you know, it will be possible to put together some interesting projects. It's over the course of the day. But, you know, if you're doing something more substantial, I think the goal is to sort of be well on your way to actually making that rather than actually having something physical in front of you.

**Chris Gammell:** Yeah. Yeah, that does. It's very fast. But I guess as long as there's bounds on expectations, that's what's important.

**Andrew Seddon:** Yes. Yeah. That's it. To be realistic. And, I mean, of course, this is, I mean, to some extent, we are hoping this is kind of a temporary situation. That it will, in fact, be feasible to prototype hardware over the course of a day and get it manufactured in those timescales, right? I mean, that's certainly something that we're sort of hoping to achieve at CircuitHub is to make that design and manufacture process as quick and cheap as we possibly can. Yeah.

**Chris Gammell:** Yeah. All right. Well, so let's talk about it a little bit. So maybe people didn't listen last time. You know, could you give us a quick overview about, I know it's been like a half an hour, already half hour into the show, but how do you see CircuitHub? How would you explain it to someone?

**Andrew Seddon:** Yeah, sure. So basically, we are a crowdsourced electronics parts library, and we work with your existing EDA tool. So effectively, what this means is that you can go on CircuitHub.com, search for the part that you're interested in using. You can then click a clicker button, and we will synchronize the libraries for that part to your local computer in the EDA format that you use. So you can then open up your EDA tool, and the part is then available. You can drop it into your schematic, and it comes in complete with footprints and all of your sourcing information intact. Okay.

**Chris Gammell:** So when the stuff is stored on – okay, so I guess you kind of walked us through there. So say I find a resistor. For some reason, I don't have an 0603 resistor on my current CAD tool, right? And, okay, I say I'm going to go on CircuitHub. I'm going to select it. I'm going to hit download. It will show up in my Dropbox folder that has been specified. But then there's formats, right, between different CAD programs. So what are the different ones that you have support for?

**Andrew Seddon:** Yeah, so right now we support Altium, Eagle, and Orcad.

**Chris Gammell:** Okay.

**Andrew Seddon:** But the goal really is to support every tool. So I know you're a big KiCad user. So that's definitely – that's actually been our most requested tool to support. So that's kind of next on the list. But we really want to support all of the tools, sort of JEDA and the mental graphics tools. Yeah. Eventually pretty much everything.

**Chris Gammell:** Okay, okay. So when it's on the server, though, is it actually stored as like an actual file that's specific to Eagle? I forget what the footprint files are called, but like – or specific to Altium? Are they actually stored like that or do you guys actually generate them?

**Andrew Seddon:** Yeah. So I think this was kind of the misconception from your show last week.

**Chris Gammell:** Yeah.

**Andrew Seddon:** What we actually do is – so we actually let you create the symbols and the footprints directly on the site. So we have an editor where you can input the symbol, put the pins for the symbol in. And we have an editor where you can create the footprint. What we then do after you've done that as a user is that we then convert that to all of the different EDA formats on the back end. Ah, okay. So it's not the case that, you know, you would upload an Altium symbol or you would upload a KiCAD symbol. And those are then siloed into different EDA tools. It's actually every single symbol and footprint is appropriate for every CAD tool.

**Chris Gammell:** Oh, okay. So the upside of that, of course, is that you do – then once you add new tools, it's all abstracted out, right? So it's just like pad here, pad here, here's the space, and you generate it for whatever the rules are for each program. The downside being that you can't – so I guess most people would probably expect that you could – I know I would – that you could then take an existing library, upload the whole thing, but then you have to deal with all the weird part namings and all that kind of crap that's in there usually. So instead, now you say, okay, well, we have to start from scratch. You have to put in – well, not everyone has to, but one person has to put in an 0603 resistor, and then once that's in there, it's then available to everyone, and then it can be sent out to the world. Basically, anyone can select it. Any tool can – it can be generated for any CAD tool, and then anyone can download it.

**Andrew Seddon:** Yeah, so we sort of – we have taken the decision really that we really felt that this thing had to be universal, right? I mean, there's no – there really isn't a kind of leading CAD tool. You speak to 10 engineers, and you're going to get at least five different CAD tools, you know, and often engineers will flick between different CAD tools for different purposes, right?

**Chris Gammell:** Yeah, I mean, personally, I use KiCad at home because it's free, and I want it to continue being free, but, I mean, at work, I never have a choice, you know? It's just like whatever you're forced to use. When I've consulted in the past, I've been, you know, forced into other tools, and it's just like, okay, well, you've got to learn it. You've got to learn it.

**Andrew Seddon:** Exactly, exactly, you know? So you'll end up using these kind of bunch of different tools, and right now, you know, your libraries are going to be siloed into those individual tools.

**Chris Gammell:** Yeah.

**Andrew Seddon:** So you might be creating the same parts if you're using Altium or Warpad at work, but then when you get home, you're using KiCad or Eagle. You know, you can be repeating that same work between the different tools. So we kind of took the view that really what you need is you need kind of one definitive source of that data, and what you want to do is you want to make it really, really easy to create those symbols and footprints, right? So that even though you can't necessarily import your existing stuff, you will either find your existing parts already on CircuitHub, and if they're not, it will be super quick and easy to import them from, you know, from the raw data sheet. And there's a whole lot of really nice things that kind of fall out of that in terms of being able to maintain a lot of structure to that data. And we think kind of one of the biggest problems when people have attempted this before is that they've not enforced enough structure onto the library. Right. So, you know, you'll find this. If you go to component manufacturers' websites, you'll often be able to download their library, right, which will have like 100 symbols in it and 100 footprints. And then it's five years old and you can sort of pick through it and try and find the appropriate matching things. But by the time you've done that, you may as well have just created it yourself from scratch, right?

**Chris Gammell:** Yeah, right, right.

**Andrew Seddon:** And we sort of feel that the problem there is actually that there's not enough structure in the data that you can trust it. So what we really didn't want is people kind of like mass importing their existing libraries and including stuff that they may have created 10, 15 years ago that they haven't checked, you know, that may not even be correct.

**Chris Gammell:** Right. It's like LM324-1, LM324-1-old, LM324-1-don'tuse. Exactly. All of those, you know.

**Andrew Seddon:** We've all done it, you know. We've all done it. And if you've been designing long enough, then you kind of end up with this, you know, this library that, if you're anything like me, I mean, I've sort of carried my library from one place to another.

**Chris Gammell:** Yeah.

**Andrew Seddon:** And you end up with this, you know, there's stuff in there that they don't even manufacture anymore. There's five copies of the same thing because I couldn't find the old thing.

**Chris Gammell:** Right. And, you know, all the quirks, you know, what not to use. It's, oh, I don't use that one anymore. That one's no good. And then someone else tries to use it. And they're like, well, why did you use that?

**Andrew Seddon:** Exactly. This is funny, right? I mean, this is why, I mean, I've kind of, I've worked in smaller organizations. I've worked in larger organizations and it's always surprised me how that people don't even really share libraries in larger organizations, right? Yeah. You'll still have, engineers will just keep their library siloed individually. And that's because they're filled with quirks and they know what those quirks are. And, you know, you don't want to give your library to somebody else and then be responsible for.

**Chris Gammell:** Well, yeah. And you have legacy designs, right? You don't want to have to go back and then say, oh, is this using the old library versus the new library? Do we actually take the, you know, when do we make the cutoff? What do you do with all the new stuff then, right? There's just so many different layers. I mean, some of which will actually run in, people will run to, you know, if they, even if they're using old libraries, right? And then they say, okay, well, we're going to start using CircuitHub to actually use it as a repository. Okay. Well, then what about, okay, we're doing this on February 1st. Well, what about designs that were before February 1st, right? I mean, like there really are, there's always going to be these kind of backwards compatibility issues that are just tough to deal with.

**Andrew Seddon:** Sure. So, I mean, that's really why we said, okay, let's allow people to actually do the creation of the symbols and the footprints on the site. And let's keep that process well-ordered as well. And let's record everything that gets done. So, I think that's kind of one of the most important things is that pretty much every interaction on the site is actually audited. So, if something gets changed, we're always going to know about that. And most importantly, we also know who that change is important to. So, for instance, if you, let's say that you use a part that has a symbol designed by somebody else.

**Chris Gammell:** Okay.

**Andrew Seddon:** And they then change that symbol. You're going to be notified of that change. Okay.

**Chris Gammell:** It's like a subscription list almost, right? It's like a, or like a Wikipedia notice when some article gets changed.

**Andrew Seddon:** Yeah, pretty much. Right. So, you'll, we actually, right now we will propagate those changes automatically. So, you will get the updated information and you'll be notified about what has changed. Now, it's then up to you within your EDA tool whether you want to pull that change into your schematic, right? So, your library will have updated, but you can then decide whether you want to pull that change into your, whether you actually want to pull that change into your schematic. But you can, you can take a look at the, at the diff and see, okay, well, you know, this pin's moved or this pin's been corrected, whatever the change may be. And then you can then decide yourself.

**Chris Gammell:** So, so you're saying that, okay, so I'm using a library apart from the library you created, right? It's synced naturally with Dropbox. You make a change to it. I get a notice about it, right? You change a pin spacing to get better voltage spacing or pin shape or a pad shape, rather. Are you saying that the Dropbox will then automatically sync it to my computer whenever I'm connected? Exactly. Yeah. Oh, interesting. That could be dangerous.

**Andrew Seddon:** You, you will, you will know about the change, right? So I think the important thing here is that, you know, this, this, essentially what we're saying is that the biggest thing that we're currently missing from the site is that we don't really have a social proof system yet. Okay. So what, what, what, what is kind of important about all of this is that, that, um, the way that we save people time is, um, because you don't have to, you can, you can implicitly trust the data on the site, right? So, um, when you look at a symbol, you want to know that as the correct symbol for this part. And you want to know that because a hundred other people have said that it is. Okay.

**Chris Gammell:** Yeah.

**Andrew Seddon:** And, um, that is, um, I mean, that's the thing we're working on really hard now is.

**Chris Gammell:** Yeah. So it was an actual, like an active system of like review and checks and balance kind of thing.

**Andrew Seddon:** Yep. Pretty much. Um, that's, that's the idea. So, so you, you, you will, um, you know, you, you, you will be notified straight away of any change and, um, you will have the option to accept that change. And, um, uh, you will, you will also be able to, uh, see, um, who else has approved that change as well. Right. So if, if, if, if, if there's a symbol and it's got a hundred people say it's okay, well, you can be pretty sure that it's, it's okay. So it's then up to you whether you want to then manually check it as well.

**Chris Gammell:** See now. Okay. So I was, I was just thinking about how I use a network connected library at my work. Right. And I have in the past as well, where it actually go. I mean, and a lot of CAD programs are like that, right? You know, if you're in a company, you have multiple seats of a license and you have a librarian, right? The librarian being the person that monitors parts and actually creates parts often. I guess those are often changed at the same time as well. Right. So if I, you know, pull in a part on February 1st and then the librarian changed it on February 2nd, then I made a new schematic on February 3rd, then I potentially could pull in a different part. So I guess in that case, you guys are just acting as the librarian, right?

**Andrew Seddon:** Yeah. Yeah. Pretty much. That's, that's, that's, that's it really is that, you know, we allow everybody to act as a librarian for everybody else.

**Chris Gammell:** Yeah.

**Andrew Seddon:** So the, the, the kind of, the kind of core principle is that the more eyes on this, the better, because I mean, if you think about how this kind of works, works anyway, like, you know, you, you're, you're going to get sign off from, from multiple people. Right. So if you, if you've got a, if you're creating a library, you'll, you know, you'll maybe get sign off from a librarian and a couple of engineers or something like that.

**Chris Gammell:** Yeah.

**Andrew Seddon:** Um, so we really just want to allow everybody to do that at a larger scale.

**Chris Gammell:** Yeah. Well, and that's good too, because I recall at past companies, it's like, okay, the librarian is going on vacation for the next week. Make sure you have everything you need right now. Right. If there's a librarian, then you have a place to go for approval. And if you don't get it in time, it's like, well, you didn't get it in time. Good luck. It's also Chinese new year. You know, it's like, screw you.

**Andrew Seddon:** Well, I mean, you're, you're lucky if you actually had a librarian to do this stuff. Right. Um, yeah, that's true. I mean, a lot of times, you know, you, you'll, you'll get stuck doing it yourself. And, um, I mean, personally for me, that, that was never one of the interesting parts of the whole design process.

**Chris Gammell:** Um, that's true too. Yeah.

**Andrew Seddon:** I, I, I always kind of hated that, that point where, you know, you've, you, you selected pretty much most of your components and, um, you know how the design is going to look, but now you've got to get it all drafted up. And then you sit there for the next two weeks, getting all your symbols and your footprints in order. And, you know, it's just a, it's a painful process. Um, yeah.

**Chris Gammell:** And it's actually different tool to tool as well. So like you guys cover both Altium and, and Eagle, right. And I know that in Eagle, it's actually linked together where it gets, uh, I'm pulling LM324. It already has a footprint associated with it. If there's an LM324 dash SOIC8, then that might have an SOIC8, whereas the other one might be like a dip package. Right. And so that's actually connected at the, when you, when you pull it in your schematic, a lot of tools like Altium, KiCad, a lot of those, you're actually just putting in the schematic symbol. And then at the time when you're pulling it into the layout side, you actually, that's when you assign the, the package type. And, and when I, when I first switched over to Altium, cause I'd use Eagle first and I'd used a couple others before that, um, the, I had never done that association before. And, and that's when it really hit me that, yeah, you, you're the librarian at that point with those kinds of tools where you're pulling it in like that. If you don't have all the footprints set up and in an easy to recognize manner, uh, then you are, you're, you're, you are now a layout, a footprint maker, you know?

**Andrew Seddon:** Yeah. Yeah, exactly. I mean, it's, it's funny actually, I mean, there's, there's a, there's a compromise there, right? Um, I mean, ultimately at some point in the design process, you are going to have to make those decisions. And I think different tools just allow you to make those decisions at different points in the, in the design phase. So, um, you, you, I think you tend to find with the kind of a lot of the, um, professional level tools, they, they require you to kind of get everything correct up front. So, you know, they, they kind of work on this assumption that you're going to have a librarian, um, who is going to produce correct data. And then you're then going to go on to step two, which is design it into a schematic. And then you're going to go on to step three, which is, you know, put it into a layout.

**Chris Gammell:** Right. And those might be all different people all every time, right? It might just be different steps of the process, very siloed. So yeah, you have these handoffs that have to be very discreet.

**Andrew Seddon:** Exactly. And, um, and then some of the more, um, uh, the tools for hobbyists, um, you know, if you look at something like Eagle or, or, um, uh, KiCab, then, um, they're much more free form. As in, though, you know, they will let you, uh, place just a schematic symbol. And then at the point at which you're doing layout, you get to do the association.

**Chris Gammell:** Yeah.

**Andrew Seddon:** And, um, there's benefits to both. There's benefits to both. But, um, I think if you think really about why, um, people want to do the second process, it's because, um, they don't want to have to think about library creation up front. Um, but that's kind of, that's really a shortcut, I think, to the correct solution, which is just that it should be super easy to have.

**Chris Gammell:** Yeah, short term versus long term, right?

**Andrew Seddon:** Yeah, it should be, it should be super easy to have a hundred percent correct part in your schematic straight away, you know?

**Chris Gammell:** Yeah.

**Andrew Seddon:** Um, and that's, and the reason people don't do that right now is because they don't want to go off and spend an hour creating that correct part. Right. But if it was very easy to, um, just click a button and, and have that a hundred percent correct from the beginning, I think people would probably do that.

**Chris Gammell:** Uh, well, I plan to, uh, so, so, so tell me about your, your target audience here. Cause so with, throughout all of this, all I can imagine is, you know, past mentors, current mentors, you know, gray beards galore in the analog field, just kind of sitting in the corner, just shaking their head. No, and just scowling at me. No, you're never, you cannot, you're not new. Do not do that. I will rip you apart at your design review. So what is your target audience here? I mean, is it, is it those guys or is it someone else?

**Andrew Seddon:** Yeah. I mean, it's, it's, um, we're really building it this for ourselves. Um, I mean, this is, uh, this started as, as a, as a passion project. Um, uh, first and foremost, um, this really started as a, as a passion for never having to do library management again. Yeah.

**Chris Gammell:** That's the best project where it's like, I am so pissed right now. I just have to fix this.

**Andrew Seddon:** I will learn web development. It turns, it turns out though, the logic for that is that is actually slightly backward because when you start a business, to deal with something that you hate doing, it turns out that you end up doing that all of the time.

**Chris Gammell:** Oh, right. Yeah. But you know, it's like, you're, you're like a martyr, right? It's like, I, I am taking this pain upon myself. So you do not have to anymore.

**Andrew Seddon:** Exactly. Exactly. That's the, um, and there's, you know, don't get me wrong. There's a, there's a lot of other fun aspects to it as well. So, um,

**Chris Gammell:** the funny thing is that, is that you can get so fried from it doing it so often, right? As, as you are working on this, that you may never want to actually, you might not even remember how to do it by the end, right? It's like, you're so deep in all the details of everything. And it's like, you know, you get all these obscure corner cases that it's like, well, what do you mean? I just hook up the footprint.

**Andrew Seddon:** I mean, I'm, I'm, I'm personally really looking forward to getting back and doing some electronics design and kind of actually being more on the usage, uh, usage side of, uh, of circuit hub. Um, it's something I haven't, I haven't had the opportunity to do for, uh, some time now. So, um, I'm sort of, sort of looking forward to that, but, uh, yeah, I mean, sort of in answer to your question of who it's for, um, I mean, uh, both, um, both Jonathan and I, Jonathan, my co-founder, uh, um, have done electronics at pretty much every level from, um, tinkering around with stuff in, in, in, um, in our, you know, garages, uh, right up to, uh, consulting for, for large corporations. And, um, we are basically making this for ourselves. Um, so we hope that it's going to cover the full, um, the, for, the full range. Um, now in practice, that means that, you know, you, you're always going to get, uh, should we say, um, cranky pants, your early adopters are always going to be people with my, who are much more flexible. Right. And, um, if you, if you are a kind of hobbyist or a warm man band, then you can just turn on the dime and you can say, okay, this looks cool. I'm going to use it. But if you're working at a large, um, in a large enterprise environment, then you've got to go and convince 10 people that this is what we should be doing. And this, then that sort of stuff takes a lot longer. So, so we really anticipate.

**Chris Gammell:** And you might have a librarian that doesn't want to lose his or her job. So then they're, no, you can't do that.

**Andrew Seddon:** Yeah, sure. I mean, there's, but I mean, the interesting thing there is right. That, um, like librarians do, uh, do use tools. So there's nothing to stop. Um, there's nothing to stop your librarian using circuit hub and then just becoming more productive. Um, yeah. You know, we, we, we think this is very much not a zero sum, uh, equation here. There's, you know, there's a lot more, um, I mean, we, we think that if it was, if it was easier to, uh, design and manufacture electronics, there would be a lot more electronics in the world. Okay. Yeah. Um, so, so if we can make that, if we can sort of make this process easier, um, there's going to be, um, you know, it's hopefully just going to be great for the industry. Uh, so that's perhaps quite a grandiose thing at this stage when we're a small startup, but that's the dream.

**Chris Gammell:** Oh, well, that's, that's okay, man. You got to dream big. You gotta, you gotta shoot for the stars. That's important. Um, so what about, what about like the public versus private type of thing? I mean, so, so like you, you mentioned the, the big corporation type environments, right? Where, uh, but I, I know that, that ones I've been in before, you know, if you, if you went to someone and said, okay, well, I have this great tool and I have it so that, um, you know, a library makes it easier on the librarian. There's, you know, it allows multiple, uh, ranges of feedback for parts, uh, part creation. So you have, you really cut down on, on potential errors and then you say, but also it's on the internet. So, you know, you have to, you're pulling from the internet and other people are seeing your footprint designs and then everybody goes, and then you get booted out the door. I mean, is that, is that something you've run into yet or is it just like a, well, who cares?

**Andrew Seddon:** Yeah. So, um, I, I, I'm surprised actually that we haven't run into this issue yet. Um, it's, uh, it's, it was something that I would, that I was also worried about, I guess. Um, I think there's, there's probably, um, I expect, I expect we will at some point. Um, I'll, I'll say sort of first, but, um, I think you've got to look at, um, corporations becoming a lot more open in general. Um, the kind of use and publishing of open source, both in terms of software and hardware. And, um, you know, how much information are you giving away? Um, or how much, you know, kind of intellectual property are you giving away by publishing your symbols and footprints? Um, and if you, if, you know, if this corporation thinks that's, there's too much information, then they can choose not to use circuit hub or, um, and if they think it's okay to be giving that away, then, then they can use circuit hub. Um, I mean, right now, all of our, our, our default policy is that, um, that pretty much everything is public, right? So if you, if you create a symbol or you create a footprint, it's going to be public by default.

**Chris Gammell:** Yeah.

**Andrew Seddon:** Um, that's not to say in future that we won't, um, have, uh, privacy options. Um, that's potentially something we could look at if there was, if there was demand for it.

**Chris Gammell:** Well, it's interesting because I thought about it like, well, you know, you could, you know, you guys as a company, you know, at circuit hub as a company, you could eventually, you know, package it all up and sell it to an enterprise. You know, kind of like how Google does with like Gmail and stuff like that. They actually sell servers, right? But at the same time, it's like the entire value of, of the thing is that, no, there's lots of people looking at it. If you then constrain it to, you know, 50 or a hundred engineers, then you run into the same problems that you have with the library. Now, the actual value in it is that there's more people looking at footprints and especially on common parts, right?

**Andrew Seddon:** Yeah. I mean, that's, that, that's exactly what we think is, is that we want to try and avoid this getting fragmented, um, because the value is in having one place to go for, um, for this information. Um, and if we start, um, creating, we're just going to contribute to the problem if we allow people to go off and create their own siloed, um, libraries, you know, we, we, we, we could, for instance, provide a kind of enterprise install. Yeah. Um, but, um, you know, the real benefit is if we can just get everybody to contribute to this one shared library, um, then, you know, we don't, we don't, it's just, it seems to me like there's this crazy situation right, right now where there's, there's so much duplication of work. And, um, I think what, what frustrates me most about this is that, um, it's, it's duplication of mistakes.

**Chris Gammell:** Um, yeah, yeah.

**Andrew Seddon:** And, and those mistakes are just incredibly costly in, uh, in time and, and, and, you know, money. If you, if you get something wrong in your symbol or footprint and you get that all the way through to fab and you get your board back and, and it doesn't work. And you spend three days figuring out why it doesn't work. And then you realize that you mixed a couple of pins up.

**Chris Gammell:** Yeah.

**Andrew Seddon:** Which has happened to us all. Um.

**Chris Gammell:** Oh yeah. I was, I was going to mention before when you were talking about, you know, sharing foot or libraries with someone else. My first board working in a, in a, in a corporate environment, I borrowed, you know, senior engineers library. And I'm like, of course it's going to work. Right. And then, you know, I get my first board back, spend two weeks debugging it and then find out, you know, because footprint errors are so hard to detect because it's the last thing you expect. Um, I found out. No, yeah, yeah, yeah. That, that, that enable pin, you weren't, you weren't pulling, you weren't doing that, right? Exactly.

**Andrew Seddon:** I mean, I've, I've just seen it happen so many, so many times. Um, and, and, um, you know, it's going to be happening on the same parts for, for different people because everybody's creating their own, their own silo data. So it would be much better. I mean, if that mistake has to happen, then at least let's, let's have it happen once. And then that, that should be the only time that the mistake happens. Um, and, and that, I think that is going to be the real benefit, um, of, of circuit hub is that, um, if, if there are any mistakes in the data, you know, we'll, we'll try our hardest to make sure it's a hundred percent correct. But, you know, that's, that's, that's the goal, but, um, the, the, the kind of backup plan is that if, if anything does go wrong, then it only goes wrong once. Um, it goes wrong, wrong the first time. And then for everybody else from then on, it's, uh, all the data is, is correct.

**Chris Gammell:** Yeah. Well, and it'll be nice when, I mean, like, as you guys, you know, continue to grow and continue to get numbers, right? If you have some kind of feedback mechanism for, okay, this part was wrong, right? And you have that, you know, I don't know if there'd be some way to compare it to like a, you know, uh, uh, individual installation environment where, you know, like a big corporation where, okay, this happens twice a year versus, you know, once a year with circuit hub, that kind of thing. Like, you know, if you have those kinds of comparisons, then eventually that, that kind of adds to it. But, you know, you need to get that momentum going first to actually have all these cases and have, you know, basically if something's going to go wrong, you need it to happen so that you have the data, right? You can't just look and say, well, nothing's gone wrong yet. So a hundred percent effective.

**Andrew Seddon:** Yeah, exactly. Yeah.

**Chris Gammell:** That's a tough one.

**Andrew Seddon:** I mean, clearly, yes, we, we, uh, yeah, we need, we need to, um, sort of get a, uh, a bigger library, um, a bigger library available. I mean, that's, that's really one of our, um, one of our focuses right now, um, is just to get a, get a whole bunch more content, um, on the site. Um, and, uh, to keep that, that content as high quality as we possibly can.

**Chris Gammell:** Right. Yeah. I mean, that's, that's another thing I was going to ask you about. I mean, how, you know, you mentioned the, the fragmentation and siloing of, of, you know, libraries and footprints and everything else. How, how do you become the, the one, right? I mean, like, that's, that's the tough part that, you know, with a concentration of power like that, how do you, I don't want to say power, that's not the right word, but the concentration of information like that, um, there is risk in that. And I think that's what some other people look at and they say, well, I don't want it to just be based on one company or one thing. I mean, how, how are you guys trying to fight back against that, that concept of needing the, to be, to get that mass?

**Andrew Seddon:** Yeah. Well, I think the, um, the, the, the kind of base in the whole that, that we've got there is that you, you end up with all the data on your computer, right? So, um, you can at any time decide that you don't want to use circuit hub anymore. Oh yeah. And, um, you then have, uh, you, you've lost nothing, um, in terms of, you know, you, you, all of your data is still intact. Um, so you could simply go on and link your Dropbox, never log in again. And you're still going to have all of the libraries that you had before. Um, it's all copied locally to your computer. Um, of course you're now back in the stone ages. Um, if you want to then do any more design work, so I'm not, it's probably not a good idea. I'll just put my library and send it to you. Yeah, exactly. You know, so, um, but, but I think that is, um, that, I think that gets around a lot of, a lot of the, the kind of fear, um, or, you know, of, of, of sort of tying yourself to, uh, tying yourself to one service. Yeah.

**Chris Gammell:** Yeah. I guess, I guess a lot of, yeah, a lot of, a lot of my concern would be, you know, if I was going to a service where it started out free, right. And then eventually it's like, okay, well, you know, it's the new year and now it's a hundred bucks a month to access your footprints that you put in. You know, if, if it was like that, then that's really dangerous. Right. But if it, like you said, if it's all locally, um, then that helps a lot.

**Andrew Seddon:** I think, I think the other thing that, I mean, trust, trust is something that you accumulate over time, right? Um, it's, we, we, we have, we have pledged, um, that, um, what you currently see on circuit hub in terms of all of the library management will always be free. Um, we, you know, we will, we will never charge for the, um, never charge for the core product that you currently see. And the, um, really the, we, we, we think this is kind of where efforts in this direction have failed before as well is because a lot of them have kind of been paid for products. Right. So the question, the proposition to people is, okay, um, you pay me money and then I will let you contribute to our library and we will then share that to other people. Okay. Um, which is just entirely different to, um, to this is, you know, this is a publicly available resource for everybody to use. Um, so, so we really felt that the only way to do this was that it had to be free. Right.

**Chris Gammell:** Well, the other model there is, you know, you pay me money and then we'll get someone here to do it. Well, we'll get someone here to make library footprints, right? Like, like having an onsite librarian instead of, you know, the users making it and then, and then it's a subscription type service as well. So that's another option, which is out there.

**Andrew Seddon:** Yeah, it's, it's, there are pros and cons to both approaches, right? Um, I mean, we, we, we just think that we really just want to concentrate on making this the easiest way to manage your library. Um, and, um, and just keeping that free and available for everyone. Um, the, the, the thing is that if you, um, you know, there should be a shared resource, um, for everybody so that, you know, everybody, everybody sort of hates doing this process, right? Everybody hates library management. Let's just allow like everybody to help each other out, um, take some of the workload off each other and then just kind of, and get this problem nailed. Um, so, so, so that, that is, that is always going to be free. And, um, in terms of like the, the, the, the, the trust issue, um, as in, you know, okay, well, um, you know, is, is, is, is this thing going to be shut off six months from now? Um, that's really something that I think you accumulate over time. Um, you know, as, as, as, as we're around for, um, for a longer period of time, um, people will, will, um, you know, we, we, we, we were aware that we have to earn people's trust.

**Chris Gammell:** Any, any plans to open source any of the code or anything like that?

**Andrew Seddon:** Yeah, we do actually. Um, so we, we very much want to open source, um, a whole bunch of code out of this. Um, we've got, I think we currently have about 20 open source projects on GitHub.

**Chris Gammell:** Oh, wow. Okay.

**Andrew Seddon:** If you go to, um, github.com forward slash circuit hub, you'll see a whole bunch of stuff that we've, um, that we've put up there. Um, our kind of default policy internally is that it's open source unless you can come up with a good reason why it shouldn't be.

**Chris Gammell:** Yeah.

**Andrew Seddon:** So it's like, like we, we, we kind of on almost everything. Um, the default is while it's public. Um, and then you've got to come up with a damn good reason why it shouldn't be public. Um, and, uh, the main reason for the kind of main web application not being public is to keep everything secure. Um, and, and also to some extent to avoid fragmentation, right? We don't want, we don't want kind of circuit hub one, circuit hub two, circuit hub three. And then the whole value of this shared library gets diluted. Um, we, we really do think there's kind of one shared resources, um, is worth doing.

**Chris Gammell:** Yeah, no, that's, that's very true. And, and, and, you know, it kind of reminds me like a stack overflow type thing where the, the backend is all, you know, open source. You could run your own, but at the same time, the value again is in the people. It's in the, the, uh, you know, the critical mass of, of information there, right? That's, that's what they go for. Um, and, and that's, that's why it's been successful.

**Andrew Seddon:** Yeah, exactly. I mean, the, the, we, we, we really sort of see it that we're building a tool to allow the, allow everybody to kind of curate this library. Um, and, you know, what's going to be really valuable there is, um, is this big shared library of information. Um, yeah, very much like Wikipedia. So, um, we, we definitely want to, I mean, we, we build on pretty much almost exclusively on top of open source. Um, so I mean, we're, we're big users of, um, of Node.js and, uh, MySQL and, you know, the whole stack's kind of Linux from top to bottom. Um, so we, we, we use an awful lot of open source and, um, we, we, we definitely are and want to contribute more back, uh, back on that front. Um, I think, I think for me, it's just a really cool way that companies are going is that, um, I think there's this kind of great model, um, that I think is also applicable to hardware. Where you, you kind of, it's almost like 80% of what you do is, is common across everyone, right? So in software, you use these open source, uh, software projects. In hardware, you use publicly available designs. And you then take that and you add your, your extra sort of icing on the cake, um, which is your, your kind of differentiator. Um, so, so that's, that's really what we want to do is kind of make as much as possible open source. Um, and then, uh, and then sort of keep our little twist on it, um, on the top.

**Chris Gammell:** So what about the, uh, so you mentioned the, the core tool will always be free, but what about, uh, you know, eventually I'm guessing your generous investors would like you to make some money. Yeah. So what are, what are, do you have any potential plans for that kind of thing or is it more of a work in progress?

**Andrew Seddon:** Yes. I mean, there's really two, there's, there's, there's sort of two things that we, we set out to, um, to, to really, uh, to, to really crack, um, which is the design and manufacture. Of electronics. Okay. Um, so, uh, we will be moving a lot more into the kind of manufacturing, uh, side of things. Um, and I like it, I like it. Yeah. That is, that is kind of really where our, um, where our business, uh, where our business model is, um, is, is much more to do with the manufacturing of things. And then that allows us to, um, or the hope is that will allow us to, um, you know, keep all of this information public, um, because we have this business model on the backend.

**Chris Gammell:** Yeah, that's great. I mean, yeah, that's, that's, that's what a lot of, a lot of great businesses have been doing with, with being able to have a big, you know, community. Like, like, uh, 3d robotics, right? Chris Anderson's company. Very, very similar. DIY drones isn't officially part of that, but there is, you know, this big open source community that's funded by a lot of, uh, you know, help from, from smaller companies behind it. And then, you know, there's, there's actually a commerce component to it as well. So that's great.

**Andrew Seddon:** Yeah. And I mean, I, I think, you know, um, this is, this is, um, it's a, it's a kind of great, great model. I think that works well here because it just allows us to, I mean, one way or another, we, we, this, it would be very difficult to do circuit hub. I think as a kind of a completely, um, a completely open source, um, amateur project. And I can tell you that because I tried, uh, John, John and I actually both tried to do this, right. You know, we, we, we were kind of just doing this as a spare time thing. Um, and, uh, you know, the, the idea is that, you know, we would just work on this in our spare time and we'd throw it up there and, you know, hopefully people get some use out of it. But the trouble is, it's, it's kind of just such a big problem and, um, you really, um, you really just need a lot of focused effort, um, to get it solved. And, um, one of the most effective ways to do that is to, um, is to turn it into a company. Um, so, so, you know, that, that, that's what we've done. And then obviously that means that, uh, um, we then need this sort of business model on the backend. And so that's, that's where the kind of manufacturing, uh, the manufacturing side of things comes in.

**Chris Gammell:** Well, that's very cool. Can you, uh, can you tell us anything about, about the, it becoming a company? I mean, how did, how did that get started then? I mean, if it was a hobby project, did you go and approach, uh, Y Combinator or who was the other one? Google was funding some part of the company as well. Yes. Where did, where did it all start? Was it you approaching them, them approaching you? Was it kind of like a little bit of both?

**Andrew Seddon:** Yeah. So, so it was basically, um, so, so, so, I mean, this, this is something that I've been thinking. About for, for quite some time now. Um, and, um, basically kind of sort of started hacking around on. And, um, I, I was kind of sort of busy putting together a, uh, busy putting together a sort of prototype circuit hub and doing a bit of research at the same time. Um, and, um, I came across a paper that, uh, my co-founder Jonathan Friedman had published, um, over at UCLA. And, uh, he had basically, uh, published a, uh, a paper that was kind of describing a lot of the same pain points that, that I was experiencing. Um, and, and some similar aspects to the, uh, to the system that I was building, uh, at the same time. Um, so I, I think initially sent John an email and, but, and just said, you know, Hey, this is, this is cool. I'm, I'm working on something similar. We should, we should probably have a bit of a chat about this. And, um, yeah, we kind of, uh, you know, exchanged a few, exchanged a few emails back and forth, found out we had a, we had an awful lot in common. And, um, I, I ended up going over to, uh, John was over in LA at the time. Um, so I ended up going over to see John and, uh, we just had a complete mind meld really. Um, we, we were both, uh, electronics engineers from, you know, as I say, from, from, from hobbyists, from, you know, being, being very little and doing this thing on an amateur level right up to, uh, to, to doing it professionally. Um, we, we just, we just chatted for, you know, pretty much a day straight. And, um, that conversation pretty much consisted of us both complaining to each other about how electronics is currently done.

**Chris Gammell:** I have no idea how that works. Uh, I have never talked to another person and just complained to them for an hour a week every week across great distances.

**Andrew Seddon:** Yeah. That's, that's really how, how the conversation would go. So it would just be like, Oh God, I'm so frustrated with, you know, this aspect of electronics design. And then, and then we, we would just sort of fight that back and forth. Like, and, um, we just, you know, really, really, really had a meeting of minds there. So, um, after, uh, so, so I sort of, I sort of stayed over there for, um, for a few days and then, um, we, uh, I ended up coming back to, ended up coming back to London, but, uh, but we kept in touch and kind of at that point, like we didn't, we didn't really, um, we didn't really sort of, uh, think, Oh, okay, great. You know, we're going to go off and do this, do this startup and, and, and sort of do this thing seriously. Um, we were kind of like, cool, let's work together. You know, we both see this, uh, we see this common problem and we're, you know, we're really interested in it and we're both working on it anyway. So let's, you know, let's see how we can get this thing, get this thing working together. Um, so, um, we, we basically just sort of carried, carried on like that really. Um, we, we were both sort of hacking away on our solutions. John was actually working primarily on the kind of manufacturing side of things. I was working much more on the parts library side of things. So, so it fit together really nicely. You know, we, we, we both, we both saw exactly the same problem, but we'd started from different ends. Um, so, so we were like, this is great. You know, um, um, you're working on one end of the problem. I'm working on the other. Let's, let's join up. And we, we, we, we kind of got a, got a complete solution to this. So probably over the course of a few months, we, we, uh, you know, we, we sort of started to realize, okay, well maybe, maybe we've got something here. Um, this, this looks, looks pretty interesting, but, um, you know, we really, we really need to put some concerted effort into this and, and, and actually sort of do this for full time. Um, so we, we kind of, um, I would say it was towards the end of, um, yeah, it was the end of, uh, last year. Uh, we put a, an application in for two Y Combinator. Um, and I think this was, this was literally the, the deadline day. Um, I think I was looking at a post on, on Hacker News.

**Chris Gammell:** I'm sure that they get tons of good stuff on the last day.

**Andrew Seddon:** Yeah. It's, I, I, I sort of remember actually, cause the, um, there's, there's a post that goes up basically saying, you know, it's deadline day. Um, and, um, I sort of saw that up on Hacker News. I mean, I've been reading Hacker News for, uh, for years. Um, anyway, just, you know, all sorts of interesting stories on there. Uh, so like I thought, okay, well let's, let's ping a, let's ping an application off and see what happens and really sort of think too much more of it. Uh, so we did that and no and behold, sort of a month later, we, uh, we got invited, uh, for an interview, um, over, uh, over in the valley. And, um, yeah, so, so we ended up going over there. Uh, something must have gone right in the interview and they asked us to come and participate in the, uh, in the winter 2012 program.

**Chris Gammell:** Wow.

**Andrew Seddon:** Um, which I, I, I think what they saw was that we were just, we, it's funny actually, we, we kind of just did, we kind of did exactly the same thing that we did in our initial discussions, but just did it in an interview. So really just sit there and complain to people about how electronics is currently done. It's, um, so he, so we just like, um, uh, really just sat there saying, you know, how, how, how much work is currently involved in this process of, uh, of electronics design and getting how tough it is to get things manufactured. And, you know, we, we both, um, we both felt all this pain doing it. And I don't think they really had a clue what we were going on about. Right. Cause these, these are all software guys. Um, aside from, uh, so, so fortunately actually, um, Trevor Blackwell, who's a partner at Y Combinator, he's a, actually a robotics guy. Oh, thank God. Yeah. Yeah. So that, that was awesome. Like, um, we, we, you know, we were able to, um, Trevor was, you know, sort of really understood what we were, what we were going at. Um, but, uh, everyone else is kind of software guys.

**Chris Gammell:** I just imagine them looking at you and being like, Oh, look at the little hardware guys trying to do web applications and then you being like, and also I know electronics. Exactly.

**Andrew Seddon:** And of course, even, even, and this was, this was, um, this was the start of the year when, when hardware was still pretty uncool. Which is crazy. There's been a year. Yeah, exactly. I mean, it is crazy to think how much has really changed in this last year. I mean, there's been, there's been quite a few, I think, pivotal things that have happened, but, um, yeah, back, back then, you know, hardware was still pretty uncool. Um, so, uh, so, so yeah, we, we were really surprised actually to be accepted. You know, everybody else is, is doing these, these, you know, sort of, um, social mobile Facebook sales type things. And here we are sort of, we want to make this, you know, universal parts library. And everyone's like, well, what's a parts library? Why do you need that? And then, you know, we have to explain, we have to explain everything from base principles and then we'll make you a video. Yeah. I mean, one of the first questions we, we, um, we always, or one of the, the most, um, people tend to be surprised that, uh, this thing doesn't already exist, right? Like, so you, you explain to them what you're doing and then, and then people are like, what? So this doesn't already exist. And we're like, no, it doesn't. That's why we're building it. Yeah. Um, so, uh, yeah, so some, some sort of quite interesting, uh, interesting conversations there. But, um, yeah, I guess I just saw that, you know, we, we were passionate for, um, passionate about what we're building and building it for ourselves and, uh, decided to, uh, take a punt on us.

**Chris Gammell:** That's great. And then, so then Google also got in on it somehow. I'm not sure how that stuff, I've heard that once you get some funding, then other people sometimes come in on it as well. Yeah.

**Andrew Seddon:** So, I mean, the, the, the way Y Combinator works is that you essentially spend, um, you spend pretty much three months, uh, coding for 20 hours a day. Um, and, uh, yeah, it's pretty, it's pretty intense, right? Um, I mean, I, I think probably the, the, the, the single biggest benefit of Y Combinator is like the, the, the, almost like the weight of expectation. Um, because, uh, everyone out around you. You is working so hard. Um, it's kind of difficult not to as well. Right. I mean, if, um, you know, if the guy next to you is working 20 hour days, well, you're going to work 20 hour days as well. Um, so, so, so.

**Chris Gammell:** Which can suck sometimes, but it, it sounds like a very exciting situation there.

**Andrew Seddon:** If you're working on something that you, that you love and you're passionate about, it's, it's, it's not so bad. Right. Um, right. I mean, yeah. Would, would I sit in front of a computer coding for 20 hours a day out of choice? Probably not. But for, for a kind of, you know, for a, um, for a period of time, it's, um, you know, it's, it's, it can be a bit of a rush. So. Yeah.

**Chris Gammell:** Yeah. Yeah. Yeah. I just meant like, if you were like on a salary, right. And then you're forcing you to work 20 hours a day. That's when it's like, that's what I think of initially. And then it's like, no. But if, if it was like in my lab, it's like, yeah, that's my weekend. You know, it's like, that's great.

**Andrew Seddon:** You know, I've done it at jobs as well. I mean, I think it's, it's, it's more about if you're interested in what, in what you're doing, I suppose. Yeah. Um, so, uh, so yeah, it's, it's kind of this intense period, but then, then in the end of that, you do, uh, what's called demo day, which is, uh, where, where you, um, present to investors. Um, and, uh, that, that is basically, you know, you, you, you do a very short pitch and you, you explain to people, uh, what it is that you're doing and, you know, um, hopefully you've got some business behind what, what you're doing. Um, and, uh, from that, you then, uh, you then attempt to raise investment in the kind of weeks, uh, the weeks after demo day.

**Chris Gammell:** So did demo day already happen?

**Andrew Seddon:** Uh, yes. So, so that happened, uh, that, that was the, um, that was in March for us. So, so, so we did that. Um, and then we sort of, uh, we, we actually closed our funding round sort of pretty quickly after, um, pretty quickly after demo day.

**Chris Gammell:** Oh, so this is all still, this is all last year. Yep.

**Andrew Seddon:** So this was, uh, this was a year now. Yeah. I mean, uh, since, since we, since we started Y Combinator is yeah, pretty, pretty much, uh, just a little over a year now. Um, and, uh, it, it turned out, I mean, we, we were actually in quite an unusual situation compared to most other people because, um, uh, the problem that I would say probably the vast majority of Y Combinator companies have is, is that, um, they don't know that they're making something that people want, but the actual technology to produce it tends to be quite simple. So if you, if you're making a, you know, a photo sharing application, for instance, then the actual technology side of that is pretty, it's pretty easy. You know, you can, you can put a prototype together inside of a week, but what, what's really difficult is, um, figuring out whether people want to use it and building something that people want. Now we kind of almost had the opposite problem, which is that, oh, if we can make this, people are going to want it, but it's a very technically challenging project. Um, and, and actually figuring out exactly how all of this stuff should work and how we're actually going to go around building it, um, was, was actually a huge, uh, you know, huge chunk of work, which is, um, which is, I guess why, why we have taken sort of quite a lot longer to release than, than your, than your typical web startup is just because we had an awful lot more software to write.

**Chris Gammell:** Yeah. Hmm.

**Andrew Seddon:** Um, so, so it's kind of a, it was a, you know, a different, a different problem to most IT startups, but, uh, in some senses a nice problem to have, I suppose. It's, uh, it's at least technical problems can always be overcome. It's just a case of how long it takes.

**Chris Gammell:** Right. Yeah. That's a, that takes a little while, huh? Yeah. Uh, well, that's great. That, I mean, that's, that's really good. I, I, I didn't actually realize, I thought that you guys were still in the, the Y Combinator part. I thought you still had a demo. I didn't, I didn't quite understand that. So that's, that's really interesting though. And, and I heard that some of the new, so we had seen a tweet from Paul Graham, one of the guys that runs Y Combinator, uh, that some of the most, that there are more hardware startups. They're doing more hardware startups now. And then there's other, there's accelerators that do that same kind of thing. Bolt, uh, starting up and then, uh, Accelerator is one we've talked about before. And I think there's other ones as well now, like Lemnos Labs and a couple others where there's actual accelerators happening.

**Andrew Seddon:** Yeah, for sure. Um, I mean, um, so unfortunately I don't know which of the YC hardware companies are actually publicly, public yet. So I'm not, not gonna, um, not gonna out any of those guys, but there are, um, there are, uh, yeah, there's a bunch of hardware startups inside of YC now. Um, and I think, you know, you can tell from, uh, from PG's tweet that, um, you know, they, they, YCC, uh, see quite a lot of promise in, in hardware startups. And, uh, uh, this, this is, I mean, as we talked about, it's a pretty new thing. Um, I mean, we, we had, um, I guess in our batch, um, a couple of, yeah, so we, so we, we had, uh, I guess one genuine hardware startup in our batch, um, uh, Pavises who are doing, uh, uh, software defined radio. Uh, what was the name of it again? Uh, it's, uh, sorry, I think I mispronounced that. It's Pavises. Um, that's, uh, P-E-R-V-I-C-E-S, I think. Yeah, Pavises. Um, and those guys are making a, uh, software defined radio, um, which involves a big, uh, big hardware, big hardware component. So, so that, they, they were probably the only genuine hardware startup in, in our batch. I mean, there was a couple of other companies that were kind of toying with the idea of making some hardware. Um, but now it's, uh, yeah, it's a different, uh, different kettle of fish altogether. Um, there are quite a few genuine hardware startups going through, uh, going through Y Combinator as we speak.

**Chris Gammell:** It is an exciting time to be in hardware, that's for sure.

**Andrew Seddon:** It is, it is. I mean, I said to you before the, uh, before the interview, I'm kind of, uh, it's, it's slightly frustrating to me to be going the other way, um, to be going from hardware over to, uh, hardware over to web development. Yeah. And, uh, all the cool kids seem to be going from, from, uh, web development over to hardware now. So.

**Chris Gammell:** That's okay, man. You're just bucking the trend. I'm sure in a, in a couple months it'll swing back or something. I'm, I'm, I'm unfortunately stuck in the hardware side cause I have no clue how to code.

**Andrew Seddon:** It's surprisingly similar, right? The problems, the problems are, uh, it's all engineering at the end of the day.

**Chris Gammell:** Yeah. You've never seen my code though. It's so, um, one last thing I wanted to mention was, uh, so you're actually calling in right now from Mexico, right? Yes. Yes. Indeed. Yes. Um, so, so what, what is the reason behind that? I mean, we were talking about that a little bit before the show, but there's actually, um, it's kind of like, it's kind of relevant to news right now. Right. I mean, so, so you don't have citizenship in the U S but you're being funded by a U S company as well. So like, what's the deal there?

**Andrew Seddon:** Yeah. So, um, we're kind of in this crazy, crazy situation at the moment where, um, it's, it's actually incredibly difficult to, um, to get a visa for the U S if you, if you are a founder of a company. Um, so, um, I, I hold a British passport, my co-founder, uh, uh, John has a, has an American passport. So no problem there. Um, and, uh, we, we have a team members from, um, South Africa. And the Ukraine, um, we've, we've actually recently just managed to, to get pretty much everyone except me into the U S. Um, and, uh, whatever. Yeah, exactly. It's this, um, and unfortunately it's a, it's a very common, very common, uh, story. Um, the, uh, the immigration system just really isn't set up for, um, for sort of modern startups. Um, it's, it's, it's kind of, I think a lot easier if you, if you are, you know, if you're a founder of a large publicly traded company or something, for instance, then, you know, these, these things get a lot easier. But, um, if you, if you're actually kind of doing a, um, you know, doing a, doing a startup on a, on a smaller scale, it's still incredibly difficult to get into the U S. Um, so, um, we are, uh, currently, um, or we are going to be convening in Mexico for the next, uh, for the next three months. Um, getting, getting a team together here. I've just spent the last week, um, getting a, uh, getting a place sorted for us all to, uh, all to work from. And, uh, yeah, we're going to be, uh, we're going to be working out of a, um, uh, sort of work, uh, I guess, uh, uh, apartment. Um, or condo as the Americans, uh, as the Americans say. So we'll be living, living and working out of that for, uh, for the next three months, which has some fringe benefits.

**Chris Gammell:** Yeah.

**Andrew Seddon:** Well, are you over on the coast somewhere?

**Chris Gammell:** Is it? Yeah.

**Andrew Seddon:** So, so actually, um, uh, sort of in Playa del Carmen, which is, um, it's kind of about, uh, it's about a 45 minute drive south of, uh, of Cancun. Um, and.

**Chris Gammell:** Could be worse. You're right. Could be worse. Yeah. Oh, it's right across the bay from, uh, Cozumel, huh? It's right across the street.

**Andrew Seddon:** Yes, that's it. Yeah. I mean, it's a, it's a very nice, um, it's a very nice place to work from, from, uh, you know, for a few months. It's pretty, uh, it's, it's, you know, it's a pretty quiet and a good place to get some, uh, get some stuff done. I can't say the same for 45 minutes, you know, north from here. I think, uh, Cancun is a bit more, um, a bit more rowdy.

**Chris Gammell:** A little more party oriented. Yeah. I mean, you compare it to London too. I mean, right. I'm sure London is very similar to Cleveland in February. Well, maybe, might be a little snowy or here, but, uh, yeah. It probably doesn't hurt to go there.

**Andrew Seddon:** When I left, it was, uh, it was snowing. Yeah. But, uh, yeah. Bright, bright sunshine here. So that's, that's kind of one of the, uh, one of the fringe benefits. We figured, you know, if you've got to be, um, if you've got to be stuck in front of a computer for 20 hour a day writing code, then it may as well be sunny outside.

**Chris Gammell:** Yeah.

**Andrew Seddon:** So maybe we don't need reform after all.

**Chris Gammell:** Just have every startup go to a tropical location, which is crazy, right? I mean, like you think about it. So first off, I totally agree with you. You know, like the, that, that is totally ridiculous that that's the case. I mean, I think any country that's that U S uh, irregardless of this, you know, like any country that doesn't let in companies that are going to create jobs and, you know, do startups and, you know, have taxable revenue and stuff like that. Countries that don't do that are ridiculous. Um, but that being said, uh, you know, the U S is going through this right now and, and there's a little bit of support for it, but man, you just think it'd be so much easier and it's, it's a damn shame. It's not.

**Andrew Seddon:** Yeah. I mean, it's, it's funny actually. It's, it's, it's a lot easier going the other way, um, into, into, uh, into the UK. Um, we actually, yeah, it's, it's, it's far easier, um, to get, to be a founder going into the UK. Um, and I would guess probably elsewhere in Europe as well, but it's just, it's just particularly difficult to the States. Um, I, I don't know why that is. Um, I mean, I, there's a, there's a whole bunch of interesting stats out there. I mean, if you, if you look at the problem logically, it's, it's clearly, um, it's clearly the wrong situation. You know, there's, there's an all, uh, tremendous amount of startups that are, um, are founded by, um, uh, founded by immigrants. And, um, it's, uh, it's something that needs to change. Um, and I hope it does. I mean, we, we, we just kind of take the view on it that, you know, it's not going to hold us back. And, um, it's, this, this is one of the other nice things I guess about doing a, um, doing a web startup versus hardware startup is that, um, we can be a bit more sort of flexible in location because pretty much give us an internet connection and some laptops and we're good to go.

**Chris Gammell:** Um, so that and some, uh, energy drinks and some Funyuns and everything else, every other, uh, stereotypical, uh, coder food.

**Andrew Seddon:** Pucer and Red Bull. Yep.

**Chris Gammell:** See, now it has to be tacos and, uh, uh, Red Bull. Red Bull. If you're in Mexico, right? I'm sorry. I'm sorry anyone to speak Spanish. I apologize.

**Andrew Seddon:** Yeah. They have, they have all sorts of crazy energy drinks out here. So, uh, yeah. Oh, good. Yeah. We'll be sampling them at some point. In those late nights. Oh, that's great. But, um, we, we've been working as a distributed team for, uh, um, for I guess the last, uh, the last few months. So it's, um, yeah, it's nice to sort of get everybody together in the same location and, um, and, uh, sort of do that for a few months. Makes a nice change.

**Chris Gammell:** Yeah, definitely. Well, I've, I've taken up a lot of your time here and I really appreciate you talking, uh, to me about this and, and, uh, you know, giving our listeners a chance to better learn about circuit hub. What can our, uh, listeners do to help contribute? I mean, is there, is it, uh, is it just kind of sign on and start making footprints or, uh, are there tutorials to get into workflows easier?

**Andrew Seddon:** Yeah, I would, I would say, um, you know, we, we need as many people as, as, as possible to, um, to, to contribute, um, pass and symbol information. So, um, it's pretty quick to, to sign up and, and take a look at tutorial. Uh, and you can kind of see how the process works. Um, we, we, we, we're making it easier. Um, but, um, it's, it's pretty easy right now. And, uh, yeah, start creating parts and symbols and footprints and, and, um, using the, using the site. I think that would be the best way to, uh, to help out.

**Chris Gammell:** Are you guys doing, uh, have you taken any notes from your fellow YC, um, companies that like having, uh, badges and, you know, check-ins and that kind of thing on the site? Is there something where you can share that, oh, I've got the SOIC eight footprint for Uncircuit Hub and go check it out, that kind of thing?

**Andrew Seddon:** Yeah, maybe. Maybe? We'll see.

**Chris Gammell:** I think it's, I mean, as much as it sounds ridiculous, sometimes I think incentivizing and, you know, gamification, sometimes it can be kind of weird, but, you know, like, like Adafruit's like badge system. I love that. I think that is so, uh, great. I mean, not, not even just for kids, but just in general, you know, having a way to show that you're contributing, you know, like there's, there's pride in it and there's also, you know, there's, there's legit, there's legitimacy in it. You know, there's something you could potentially be didn't put it on a resume or put it in a portfolio.

**Andrew Seddon:** Yeah, that's, that's interesting actually. I mean, it's definitely something that we'll, um, that we're going to be looking at. Yeah.

**Chris Gammell:** Cool. Well, uh, in the meantime, people can find you on Twitter at Seddon Andrew, right?

**Andrew Seddon:** Yeah, that's the one. Yeah. So, uh, last name, first name.

**Chris Gammell:** And then Circuit Hub is also on there?

**Andrew Seddon:** Yes. Yeah. So, uh, so twitter.com forward slash Circuit Hub and obviously circuithub.com.

**Chris Gammell:** Yeah. Yeah. Of course.

**Andrew Seddon:** People should probably go there first. Yeah. Yeah. That's, that's probably your first stop.

**Chris Gammell:** All right. Great. Well, Andrew, thank you so much for being on the show. We really appreciated, uh, hearing about it. And we, we look forward to seeing your progress and seeing Circuit Hub become the, uh, the place for finding, for finding and contributing parts and footprints.

**Andrew Seddon:** Fantastic. It's been, been a pleasure, Chris.

**Chris Gammell:** All right. Well, people should check out circuithub.com and see y'all next week. We'll see you next week.
