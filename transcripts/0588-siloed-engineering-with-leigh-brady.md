---
episode: 588
title: Siloed Engineering with Leigh Brady
url: https://theamphour.com/588-siloed-engineering-with-leigh-brady/
---

**Leigh Brady:** This is The Amp Hour Podcast. Released May 8th, 2022. Episode 588. Siloed Engineering with Lee Brady. Welcome to the Amp Hour.

**Chris Gammell:** I'm Chris Gammell of Contextual Electronics. Hi, and I'm Lee Brady. I'm an electrical engineer here in the Orlando, Florida area. Hello, Lee. How are you? Doing good, thanks. How about yourself?

**Leigh Brady:** Yeah, yeah. Real good. Real good. Orlando, Florida. My brain almost always goes to the Disney parks and stuff like that. Obviously, there is industry there. Exactly. But what kind of industry is there? Where are you floating around in industry right now?

**Chris Gammell:** It's an interesting place to be an electrical engineer. You're absolutely correct that Disney parks, Universal, SeaWorld, and various others are here. Although my understanding is that the majority of their engineering is done out in California. However, they do have people doing qualification and stuff like that here. And it's interesting because they tend to use things like ladder logic and PLCs and things that I'm not very familiar with, which is why I haven't been part of that industry. However, we have UCF here, which is a big engineering school, and they have a good optics program and a good electro-optics program. So they have something called CREOL, which I'm not sure I can remember the acronym, but effectively it's an optics center. So we have a lot of electro-optics here. Cool. One example that you might have heard of would be Luminar, who are doing the LIDAR for self-driving cars.

**Leigh Brady:** Oh, cool. Yeah.

**Chris Gammell:** And we also have a lot of defense.

**Leigh Brady:** Well, I'm sure you run into people working in Disney because, as they say, it's a small world after all. Oh, indeed. Terrible. That was so bad. I was winding that one up for a minute and a half there. Very good. Sounds like you might not be an Orlando native. Is that a correct assumption?

**Chris Gammell:** That's fair to say. Although if any of my colleagues, past colleagues from the UK are listening, they'll probably be making fun of me for my perceived American accent. Oh, yeah. You've been... Yes, I've been somewhat Americanized. Yeah, exactly. Exactly. But, yeah, originally from the UK and spent about the first 10 years of my career working over there in the defense industry. Yeah.

**Leigh Brady:** Yeah, so I definitely want to get to that. You know, we were kind of chatting before the show about, you know, what we're going to cover here. Your background is, like, it's great because it spans different industries and, you know, kind of stuff that might not be... So, like, we talk to people on the show a lot about, like, open source and stuff that is kind of able to be talked about and people might know the names of companies like that. But when you start getting into defense and medical and stuff like that, it's just there's less out there because often there are trade secrets or, you know, there's just... There's clearances and things like that. We're not going to talk about trade secrets or clearances or anything like that, but just talking about the industries themselves and where you've been kind of traveling through them.

**Chris Gammell:** Yeah, absolutely. So, obviously, working in defense in both the UK and the US, kind of through a partnership that not everybody realizes exists, the UK and the US have a partnership, which I believe is known as the Mutual Defense Agreement, whereby basically largely non-classified information and resource more than anything can be shared. So, what that effectively means is that sometimes English engineers and UK engineers come over here and vice versa and just kind of, you know, learn engineering more than anything else. Yeah. Which is what I was involved in. It's very interesting to see how people do things differently in the US to the UK. And some of it's very, very similar.

**Leigh Brady:** Yeah. I mean, if you had to take like a high-level shot at what that difference is, I mean, what would you kind of start to classify it as?

**Chris Gammell:** I think more than anything, my perception at least, was that in the US, things tend to be driven to very specific specialisms. So, you'll have your FPGA engineer, you'll have your analog design engineer, and so on. And they won't really expand too far outside of their box. And some of that, obviously, is an attempt to make sure that, you know, need to know information and so on. But more than anything, I just think it's a cultural thing. So, in the UK, I got opportunity to do, to be more of a generalist, and I would consider myself to be a generalist as an electrical engineer. So, I've done analog design. I've done some FPGA design, some systems engineering, and so on. And I found that that wasn't the case over in the US. People tend to specialize quite early, even sometimes to specialize as early as an internship almost. And come right in, certainly as a junior engineer, as a junior FPGA engineer, or a junior analog design engineer. And then follow that career path, which is interesting, and obviously gives them depth, but doesn't give them necessarily breadth. And I think you can make the argument that depth and breadth have their relative merits. So, I think... That's right.

**Leigh Brady:** I think we've made that on this show many times, actually. Yeah. Yeah. And one thing that, you know, from a personal perspective, I always see the argument against the depth first would be you kind of get pigeonholed, right? So, if you have a deep specialization in, you know, I don't know, like radar systems, then the knowledge is most certainly transferable. But from how hiring practices are, I feel like you're going to mostly be working on radar, in and around radar for a good chunk of your career. And, you know, some people dig that, and they're, you know, and I'm sure there's good money in being a specialist like that. But there's downsides, and, you know, you don't get to see as much or experience new things.

**Chris Gammell:** I think that's true. And I think I was fearful of that. I didn't want to close myself off to other areas of electronics and electrical engineering too early. And also, I found myself, you know, they say the change is as good as a rest, you know. And I found myself, if I was working on more than one area of a particular project, I could kind of put one down while it was, you know, giving me a headache, pick something else up. And that was a good way for me to manage that. Other people manage it in different ways, but that was the way I naturally did it. And I think that's what kept me wanting to be a generalist.

**Leigh Brady:** Yeah, that makes sense. Yeah. I mean, is there kind of a, so now speaking specifically about the defense industry, is there enough of a hump to get over in terms of like clearances and knowledge of the industry practices and stuff like that, that that would then maybe allow a generalist more than in just any other industry?

**Chris Gammell:** Not really. Not in the US, I don't think. I think it's very rare to find a technical hands-on generalist in the defense industry that's right down in the weeds, designing the coalface, as it were. I think that's what's more normal to find is that those people that would be generalists tend to find themselves as systems engineers or engineering managers and engineering leaders. So they find that they're not happy, you know, just grabbing onto one thing and they tend to lift themselves into a position where they can have that technical oversight. Maybe there'd be an integration engineer, for example. Got it. That's been my experience. Whereas I, in the UK, I was actually able to kind of do a project on a certain team and then say, you know, put my hand up to, to, to say I would like to move to maybe a different team and do something else. And that was possible and kind of encouraged. Interesting.

**Leigh Brady:** Yeah. I mean, I, I think, I, I think listeners of the show will find no surprise in that I'm, I'm on the generalist side and I'm interested in the generalist side. I think it, you know, I, I think there's a lot of value and empathy and cross training and stuff like that, but then, you know, you, you don't, you might not have that super deep technical knowledge that you need for something like that. I wonder though, is the, so, you know, you've experienced both sides of the, of the US versus UK. Is there actually like a hiring preference then as well? So like, does that mean that if you are trying to apply for, you know, something at like a defense contract in the US that you have to have that super depth of knowledge or else you won't get the hire in the first place?

**Chris Gammell:** I think that can certainly be true. And I think it's more true the further into your career that you are, obviously entry-level positions obviously have, you know, fewer stringent requirements because they're expecting to train you somewhat more. Although I do think defense in the US, just from my experience of colleagues that I know that have moved industries will value other industries that have a similar structure. Medical, I think is one of them. Automotive is certainly another. Anything that's got regulatory obligations. So anything maybe safety critical, which often transport is. So I think they're kind of looking for that experience. But something else that's interesting about the UK is that I've noticed that there's a big emphasis in the UK on more vocational programs. For example, the company I worked at had an apprentice scheme where they would take in not graduate students from university, but students straight from high school and train them for three years and get them qualifications in things like soldering, board assembly, mechanical assembly, machining, and so on. And some of those people would come out and be technicians in the company out of that scheme. And some of them would actually go on to get their electrical and mechanical engineering degrees. And I found those people to be some of the most valuable people. If you've got an electrical engineer that started out as an apprentice learning how to construct systems from the ground up, they're very hands-on. And then they get the theory as well. I think it's really valuable. Something that I noticed that vocations like that over here aren't pushed as much. A lot of people just feel like they have to go to college. Right.

**Leigh Brady:** And then you don't have the reference point for why you shouldn't make a one millimeter plastic sidewall or that part isn't machinable or whatever the equivalent is.

**Chris Gammell:** Right. And I'm sure this has been said before, but it's so surprising that this is the same in the UK, by the way. It's so surprising that colleges don't teach soldering or the use of lab instruments. It's kind of assumed that you're going to pick that up. But depending on what your project is when you're at college, you may not pick that up. You may decide to follow a coding type project and never go anywhere near a circuit board. Yeah. But then you may get a job where you're expected to do both. So, yeah.

**Leigh Brady:** Yeah. I mean, I think, yeah, we have definitely, we've probably talked about that many times. Maybe one of the most talked about things in personal interest of mine. But I don't know if there's any solution to it. I mean, aside from maybe taking on an apprentice type scheme, like you mentioned, that would be a step in the right direction.

**Chris Gammell:** Most probably. I'd actually like to see colleges place more emphasis on parts of engineering that aren't just theoretical. I realize they have finite time, but there's not a lot of emphasis on the design cycle. There's not a lot of emphasis on the V curve, you know, the systems engineering V curve from requirements through to detailed design and back to verification and validation. I actually, I don't know if I know that term V curve. The V curve. So this is a system engineering term that I think gets thrown around a lot in defense and certainly also in my current role. Whereby, if you imagine systems design as starting at the very highest level, a top-down approach, as it's often called. You define requirements at a very high level. Let's say we were designing, you know, the classic example of a swing for a child or something. And, you know, the swing must be of a certain height from the ground. The swing must not be able to reach more than a certain height when it's swinging and so on. But you can imagine taking that and then deriving lower level requirements from that. So, okay, well, if it must be this height from the ground, then is it going to stretch when they sit on it? And if there is, then that is going to impact the requirements for the kind of material that holds the swing to the tree. And you could go all the way down to, you know, tensile strengths of materials that you're going to use as a design specification. So that's sort of like the downward path of the V. So we're now at the bottom of the V, if you can imagine a V shape. But then you need to validate up. And so you start climbing the hill. So you would validate the lowest level. Okay, I've bought tensile strength of this. So I know my cable is this and I'm going to test it on a pull tester. All the way back up to, I've now built the swing and, you know, I put my yardstick, if you're in the U.S. or a meter stick next to the swing. Exactly, right. And check that it's the right height. And that's sort of like the V curve of validation.

**Leigh Brady:** Hmm, that's great. Yeah, I'm surprised. I mean, I could picture it all in practice, but I just never heard the term. So that's a really good term to have in the old noggin rattling around. So that's good. And when you say system design, system engineering rather, how do you define system engineering?

**Chris Gammell:** Well, I think it's a process. And I think that that's the biggest part of it. You can, if you're following a process, it almost doesn't matter if your process is quite bad. At least you're going to have consistency. And I think that consistency is what differentiates engineering from design. You could do a great design with poor engineering and it's not very reproducible.

**Leigh Brady:** I guess maybe a different way to say that is, who is a system? Like, give me a project example that like, what is the system engineer in a project normally doing? Because I don't usually hear that term, but I assume that is a person, right?

**Chris Gammell:** It is a person. And classically, they would be responsible for gathering and writing unambiguous requirements. But not only that. Right. That would be their role in one aspect of the system design. They're often also involved in integration, closely with the integration engineer and the validation to design the tests. So, it's kind of a systems, I mean, kind of what it says on the tin, but it is a systems level look at the design to try and make sure that everyone's talking to everybody and that everybody's deriving their requirements in a cohesive manner. And to deconflict requirements, of course, as well.

**Leigh Brady:** So, I guess, then what is the scale of that? Because, okay, so I think about like a, so if we're in a military company and I'm designing a fighter jet, there might be a system design engineer for the entire jet. But is there also one for like subsystems or like, like how small of a, what is the atomic unit of a system engineer? Is it like a circuit board? Is it a component? Is it a assembly? Where does that line need to get wrong? Especially in the military. I think like everything, it depends.

**Chris Gammell:** It depends on the scale of the project.

**Leigh Brady:** I know. Just make something up here though.

**Chris Gammell:** Yeah, right, right. But, but typically you're right. You will have one or two systems engineers to every, I don't know, five or 10 design engineers would be my guess. Really that it's because they're not necessarily doing the hands-on work, but they're more the glue that holds everything together.

**Leigh Brady:** Yeah. Yeah. I mean, like I think about past experiences in product companies and sometimes that would be called a product engineer, product marketer, depending, you know, if they're doing externally facing a product manager, you know, it depends really just kind of, it's because it's like where you're drawing the lines and kind of like the norms within different industries. So it sounds like it's kind of a mix of all those things in the defense industry.

**Chris Gammell:** It is. But I think the thing that would distinguish a project manager or a product engineer from a systems engineer is the systems engineer is typically very technically astute.

**Leigh Brady:** Uh-huh.

**Chris Gammell:** So they're very aware technically of all of the various aspects of the system.

**Leigh Brady:** In a hands-on way as well. Do they like, so do they need to be able to walk out to the manufacturing floor and be like, I can run this through its paces?

**Chris Gammell:** More accurately, they need to be able to ask the right questions to someone on that floor, because especially in defense industry, you know, that there's so many people.

**Leigh Brady:** So this is a high-power explosive, so please don't run it through paces right now. Right, right.

**Chris Gammell:** But you can imagine that there's loads of people in a team doing very specific roles, as I said before. That's typically another thing that I've noticed. The teams are huge in defense. I mean, if you pick a classic kind of program like the Joint Strike Fighter, I struggle to guess, but I imagine there are hundreds, probably thousands of engineers that have worked on that space.

**Leigh Brady:** Yeah, that's the F-35. That's another sub-variance of that, right?

**Chris Gammell:** Right. And that's just one aspect of it, you know. That's just to say the engineers, and that's not really necessarily including all of the support to the engineers, like project management, leadership, and so on. I mean, it's phenomenal, almost unparalleled. I don't know that, I would wonder whether, maybe Apple.

**Leigh Brady:** Well, some people refer to that as a quagmire as well. Yeah, yeah. That particular program is like, oh, yeah.

**Chris Gammell:** Yeah, well, we could talk about that, my opinion on that. But yeah, I think that's, you know, trying to fit a good example of where you probably should design more than one system.

**Leigh Brady:** Yeah, yeah, right. No, exactly, exactly, right? That is something where, I mean, and that also kind of felt like, so one thing that I hear in like defense contracting or the defense industry as well, you know, I start to think about like, just like massive waterfall charts and, you know, massive over, you know, project overages and delays and stuff like that. I mean, I mean, how true to form or fair is that stereotype that I have in my head?

**Chris Gammell:** It can be true on the programs that are very public and very large, like, you know, development of new fighters and development of new weapons and so on. But I'm sure you're aware that there also exists smaller programs. Oh, totally. Yeah, yeah. And I think Lockheed referred to them as IRAD's internal research and development. And those are typically much smaller and probably have smaller budgets because they're research and development. But like all research and development, it tends to be more fun, a little faster paced with a little less restriction. Obviously, when I say less restriction, not pertaining to safety, that's the only thing. But pertaining to things like, you know, programmatic requirements and so on and some of the high level red tape, some of that goes away. So those can be fun to work on.

**Leigh Brady:** Yeah, no, that sounds, that would definitely be the type of stuff. So, I mean, so you did work at Lockheed. This is part of your borrow an engineer program, is that right? Yeah.

**Chris Gammell:** I was at Lockheed Learning Systems Engineering, basically the systems design lifecycle. Oh, cool. Yeah. Which was really, really fun.

**Leigh Brady:** Yeah, so you were hands on. You got to see it. That's great. Yeah.

**Chris Gammell:** Yeah, exactly.

**Leigh Brady:** And you worked, I mean, this is partially nuclear stuff as well? Or is that a separate role?

**Chris Gammell:** Not at Lockheed, no. So the nuclear stuff was in the UK. And also I spent a couple of years at Sandia National Labs, which was good fun as well, where I was qualifying or designing tests to qualify an ASIC that they had made, which was for, it was basically, if you can imagine that you might want to create a chip that would basically be a logic analyzer or a system monitoring chip so that you can make measurements of systems. Mm-hmm. And so the mixed signal chip, which is quite interesting to qualify with analog, obviously, and digital aspects on there.

**Leigh Brady:** Yeah. I mean, for all these things already, like you're, so like we're, you know, we talked at the top of the show about like, you know, having a broad basis of engineering knowledge. Like there's already like a bunch of stuff in here. That's like, wow. Okay. Yeah. That's, that's a lot of different roles and mixed signal in its own is it's a couple of different things there. What is your, what is your preference in these spaces? You know, FPGA versus ASIC versus analog. Where, where do you, where do you find your, your happiest times?

**Chris Gammell:** I think I've got a fondness for analog design. And I mean that in the sense, not, not chip design. I have no idea how to do that.

**Leigh Brady:** Hey, same.

**Chris Gammell:** Op amp type designs, small signal analog, analog front ends, that kind of thing.

**Leigh Brady:** Got it. Yeah.

**Chris Gammell:** And I think I like it most because it's, it's kind of challenging and there's so many things that can go wrong. Right.

**Leigh Brady:** Unlike, unlike FPGAs that might control nuclear explosions.

**Chris Gammell:** Well, it's, it's more to do with how, with an FPGA, I guess things tend to either work or they don't. And, and the bugs can still be hard to find, but I like in analog, how you can find, well, I guess it's the analog nature of analog, right? There's a, there's lots of gray areas in there where.

**Leigh Brady:** Right. How many, how many ways you can think of things goes wrong? Infinite ways.

**Chris Gammell:** Right. But more accurately, how, how right is it? You know, it's sort of working or it's working better. Yeah. Whereas with, with, I think with digital, it is kind of, it's working or it's not working more or less. So there's maybe oversimplification, but.

**Leigh Brady:** Yeah, sure. Yeah. Yeah. I mean, a spice simulator is a lot different than a logic emulator. Right. But. Right. Both are very, very valuable. And one might give you a slightly more definitive answer. I'd probably trust a logic. They're not called emulators or simulators, right? Like simulating. Yeah. Yeah. Right. Yeah. I'd probably trust that a little bit more than, than my spice models.

**Chris Gammell:** Yeah. But like everything, they're only as good as you, the models are only as good as what you put in. And I've seen plenty of examples whereby an FPGA design will simulate. I mean, the classic one is metastability. If you don't take account of metastable states in your design, your simulation will probably work fine because it's not very good at simulating race conditions unless you're simulating post synthesis. Right. Post place and root. But most people, I say most people, that's probably unfair. A lot of people don't simulate that way. A lot of people simulate the design just from the VHDL or Verilog. Yep.

**Leigh Brady:** Yep. They want to see like very, very square waves. Right. And then what does that square wave decode to? And then it does decode and you're good. Right.

**Chris Gammell:** But in your simulation, if you have two clock domains and they're always synchronous. Yeah. But in reality, they're not synchronous. Then everything just went off the cliff and your simulation will never fail. So that's a classic one that a lot of people get caught up on in their junior years. And I know about it because I did too. Yeah. Right.

**Leigh Brady:** Who dat? That me. Right. Yeah. Yeah. Same. Same there. It's been a while for me for that stuff. So, I mean, it does seem like FPGAs kind of carry through your career as well. I mean, is it just kind of a tool in the toolbox at that point or just because they're such specialized things? I mean, I do think of like when I think of super high end FPGAs as well, I think of defense industry because it's like might have been an ASIC, but you're only making 10 of them, that sort of thing.

**Chris Gammell:** Yeah. There's a lot of reasons why defense industry would go towards ASICs versus FPGAs. Space industry is a classic one, actually, which I guess kind of plays into defense. So you may be aware that exo-atmospherically there are charged cosmic rays and particles that can cause problems with electronics.

**Leigh Brady:** I actually blame not only my electronics problems on them, but all my personal problems too. That's right. Like, oh, no money in the bank account? Cosmic rays.

**Chris Gammell:** Yeah. It's almost always cosmic rays.

**Leigh Brady:** Yeah. Cosmic rays.

**Chris Gammell:** But yeah, notwithstanding that Superman has got his eyes on your bank account and is playing with the bits in there. Yeah. You've got the issue of what they call single event upsets, which is a cosmic ray coming, blasting through the crystal lattice and flipping a bit. And you can kind of try and take account of that if you're doing things like CRC checks. But in real time, it may be a transistor that isn't really involved in data. It might be a transistor that's kind of part of a MUX or something like that.

**Leigh Brady:** Yeah.

**Chris Gammell:** So, you know, how do you know what's going on? Right. So if you make an ASIC and you use a technology that's large, which is kind of like archaic to us. Now we strive for small gate sizes, right? But if you have a bigger gate dimension, then comparatively that particle is smaller. And so when the statistics are, it's not going to cause so much of a problem.

**Leigh Brady:** Right, right, right. More energy to knock more electrons into different states or whatever it is.

**Chris Gammell:** Exactly. But then the other option, which is much cheaper than an ASIC, is a lot of FPGA vendors will offer what they call triple modular redundancy, where you can, I think at one point it was native to a specific vendor, but I think it then became offered by others. Basically, you do your logic design and then you click a nice button in the tools that says, give me triple modular redundancy. And what it does is it sets up three copies of the design in the FPGA. And then...

**Leigh Brady:** That is a specialized button.

**Chris Gammell:** Right. But not only that, it links it to voting logic. So you get three copies and whichever two agree, that's the one that it goes with. Wow. And that's just like a macro that gets generated? It's kind of part of the tool set. So just as the synthesizer synthesizes the design and then place and root, unless you want to get into placing on specific cells yourself, which you absolutely can, and all the tool sets let you do that. But if you just say, hey, do your best, fit this design in my FPGA within my design constraints, there also exist tool sets that will do the triple modular redundancy thing for you and say, okay, we'll figure that out and make sure that it works. Which is, yeah, it's amazing.

**Leigh Brady:** Yeah. That is very, very specialized. Yeah. Yeah. So that's another interesting kind of, you know, so we've had FPGA people, you know, of different areas. I did a very, very long time ago. Dave did a long time ago. But then also we've had people on who've done it professionally, maybe at high levels, and then maybe, you know, people doing like zinc stuff and whatever. But then we've also had the open tool chain people on here. And one thing I've always heard is like, look, open tool chain is cool. I like it. But, you know, these kind of like high end, bleeding edge type of triple modular redundancy generating type of systems. It's like, that's just in the vendor tool chains because that's what you have, you know, you're just on the path that the vendors are targeting because they, you know, they're driving their software development by Lockheed or whomever is driving their software development.

**Chris Gammell:** Yeah. I mean, that's absolutely true. Obviously, companies as large as the defense industry are going to be huge players in driving the requirements of what they want to see in the chipsets that occur.

**Leigh Brady:** It's to the point where even I remember, this is probably not actually related, but maybe a little related. I remember Xilinx ISE, which I used gobs of years ago, almost 20 years ago at this point. But, you know, the CD installs all had F16s on every CD. You know, there were like 10 of them, of course. Right. You know, like targeted branding even, you know, it's like, oh, okay. Yeah, well, we know what this is for.

**Chris Gammell:** Well, I mean, the amusing thing is that Xilinx ISE is most likely still used. Well, I know I've used it as recently as a year ago because a lot of the FPGAs that are still in production, such as the SPAN 6, are only supported under ISE. Oh. Well, and it's either that or you go pick a third party tool set and buy a license for it, which I believe is probably what, you know, the defense industry will do. They'll use Active HDL and Simplify and all those other good tool sets. But if you're in a smaller company like I was, well, the free tool set's free. So we'll use it.

**Leigh Brady:** Well, and longevity. So I guess another constraint of the industry would be this kind of longevity, right? Like defense, you need 20, 30 year type of supply contract stuff.

**Chris Gammell:** Exactly. And actually, that's a really good reason to network with, if you're not in the defense industry, but you are using, you know, technologies that you're worried will become obsolete or especially in, you know, light of recent events. Bobbogum tap shoes. Right. It's really good to find out what's being used in defense because of the longevity of the programs. So it's my belief that one of the reasons that the SPARTAN 3 and SPARTAN 6, I mean, the SPARTAN 3 went end of life this year or last year, I think it's this year. So it's my belief that that's probably because it's being used in big defense programs.

**Leigh Brady:** Wait, are you saying though, are you saying that, so a design engineer listening right now should use SPARTAN 6 because of that?

**Chris Gammell:** No. I'm saying that they should find out what their industry is currently using or trying to design with, which would probably be things like SPARTAN 7 and Zinc and so on. And notwithstanding that they would go, and it's not just iLinks, of course, I'm sure that they'll be using Intel FPGAs and so on. Sure. But if you know someone and they're saying, oh, yeah, I'm doing the design on a SPARTAN or I'm doing the design on a Vertex or whatever, if you know that they work in a big company, not just a fence, but a company like Apple or any of the really big companies, it's most likely they're going to stick around because why wouldn't a manufacturer keep manufacturing the chips? Right.

**Leigh Brady:** Right. Yeah. So the thing I was going to say there is that, so I've always kind of talked about like chasing the most popular chips, right? I think that that is probably a better bet than something that might get end of life, especially if you have your own long-term type of stuff. However, the thing I wanted to call it with defense contractors is that there are, I forget what it's called, but my buddy's a purchasing agent at a defense contractor. And there's something where they get to jump the line, basically. You know, there's like, it's kind of moot right now because everybody's trying to jump the line, but like there is actually something where if you have, in the US at least, you can get like a bypass because you're making critical defense infrastructure type of thing.

**Chris Gammell:** Yeah, I think that's definitely true. I mean, I don't have a lot of experience with that, but I think that is absolutely true. And obviously consumer electronics don't get to do that. Right, right.

**Leigh Brady:** Yeah, that's what I'm saying. In the tough times like we are now, which, you know, that would be an additional thing where it's like, I would, you know, as a small player and then also, you know, a non-defense player, I would be truly the back of the line. And that would almost be like antithetical to that idea of designing in a popular chip that might be, you know, might have that longevity.

**Chris Gammell:** Yeah, I think that's true. And also, I mean, I might even rescind something I said a few minutes ago about Apple being a good example because of course they do their own fab and they make their own chips. Yeah, yeah.

**Leigh Brady:** See, I think that actually is a good one though for, well, maybe. I don't know. I remember like chasing like sensors that were on phones and stuff like that. I think that that then ends up hitting the secondary market. And usually vendors might not make that, you know, so a sensor vendor might not make it for 30 years. But I do think once they have the IP developed, they might say after, you know, Apple moves on to the next hot thing, they might say, well, we've got all this IP. Can we spin it out as a publicly available part now? Like I'm sure some of the sensors that I use have been, you know, developed for big companies in the first place.

**Chris Gammell:** Yeah, I think that's true. I think also I've had experience whereby working in a very small company, startups and small companies can be kind of kept out of the market if a big company is more lucrative to a particular vendor.

**Leigh Brady:** Oh yeah.

**Chris Gammell:** And I've got experience of trying to develop for specific chips from very well-known companies where the very well-known company plain old wouldn't sell to us, wouldn't give us any data sheets.

**Leigh Brady:** Wasn't Maxim? You could say it's Maxim.

**Chris Gammell:** It's cool. No, no, it wasn't.

**Leigh Brady:** We've said it many times on here.

**Chris Gammell:** It was actually, it was one of the larger Japanese manufacturers of image sensors. But the problem being is you can't get the data sheets either. They're all proprietary. Yeah, right, right. So the path that smaller companies have to take is to go to a third party that's an authorized reseller. But then you're kind of, again, kind of stymied by that. So not only are you a small engineering team.

**Leigh Brady:** Waiting at the drip feed, basically. We're all just, you know, we're just waiting for that tap to turn on. Right.

**Chris Gammell:** And you're a small engineering team. So, and you're trying to compete with larger engineering teams that have better information. It's quite, you know, odds can be stacked against your favor in some respects there. Yeah. So it's difficult.

**Leigh Brady:** It's crazy. Yeah. And actually, this was kind of an overarching theme that we want to kind of talk about as well. Just kind of big versus small. You've been on both sides. You've been in very, very large defense contractors. You've been in small manufacturers. Are there other big versus small type of things that you've seen that you like, don't like? I mean, that's obviously one.

**Chris Gammell:** Yeah. I mean, I think everybody, I won't necessarily dwell on the obvious. If you work in a very small company or a startup, there's almost no red tape and R&D can be as fun as you want. Right?

**Leigh Brady:** Yeah. Right, right, right.

**Chris Gammell:** And especially if a startup has managed to get some good investors, then you've got a nice big budget. And it's kind of like a sweet shop, really. Or I should say a candy shop.

**Leigh Brady:** Both are acceptable here.

**Chris Gammell:** There's candy involved. I'm into it. I don't care what it's called. But obviously then in the larger companies, you have access to big budgets. You have access to leverage, as we discussed. So you get better support for what you're trying to do. Yeah. Yeah. You know, for example, there's certain designs that I've been involved with where you can go directly to the tool manufacturers and have their engineers support you. You even pay them a retainer to kind of develop specific IP or something for you for your specific project, which you just kind of have to model your way through if you're in a smaller company. But then in a smaller company, I think it's good for the generalist because you get to, you know, the classic wear many hats, which is probably a poor way of saying it. But you do get to turn your hand to lots of different things, some of which are not even engineering, which can be awful to people. Good or bad. Yeah, good or bad. Exactly.

**Leigh Brady:** Yeah. I actually, maybe I mentioned this last week. I looked up a Jira video on YouTube the other day and I was like, oh, this is a momentous time in my life. I just looked up how to do something in Jira on YouTube. Like this is where my life is right now. Yeah.

**Chris Gammell:** I think that most non-engineers would be absolutely aghast at how frequently engineers consult YouTube. Yeah. Yeah. And Google to remind themselves either how to do things or to do things that they don't know how to do.

**Leigh Brady:** You know, just got to get like, you know, like the pull cord on like a lawnmower. It's like that, you know. I just need the pull cord and then I can, you know, dive down a rabbit hole or whatever it needs to be. The motor's kind of purring. Then I'm happy to go. But yeah, sometimes you just...

**Chris Gammell:** The classic joke, isn't it, of the guy comes along to fix the engine and smacks it with a hammer and it works and he charges an extortionate bill.

**Leigh Brady:** Yeah.

**Chris Gammell:** And, you know, he goes on to say that, you know, the actual reason for the bill is that he knows exactly where to smack it with a hammer. Well...

**Leigh Brady:** That's right.

**Chris Gammell:** I consider that I spent four years in college learning exactly what to type into Google to figure out what I need to do. Yeah, yeah.

**Leigh Brady:** Well, that's an important one too, you know, as long as Google's available. It's true, right. Yeah, yeah. So we were kind of talking about big versus small. I mean, is that kind of the... I mean, so I guess, do you have a preference? I mean, do you... You're back kind of in the big world, it feels like. Are you missing things from the smaller world now?

**Chris Gammell:** Not really. It's interesting. I think that there's a middle ground, a Goldilocks zone. Typically, you find that...

**Leigh Brady:** It's like you're at a company of like 150 people and they hire the 151st, you're like, I'm out.

**Chris Gammell:** This isn't for me anymore.

**Leigh Brady:** Exactly.

**Chris Gammell:** I mean, I think where I am right now is kind of nice because it's... You tend to find that some companies go around buying up other companies, especially startups or smaller companies that have reached that kind of critical threshold. And I feel like that's where I am now, although the company has been a long time since it was acquired. But it still has that feel of like a smaller team with a specific goal, yet you get the support and the good parts of a larger company. Obviously, you get some of the bad parts, some of the red tape. But yeah, I think it depends on really the kind of person that you are. But I think it also... I think every engineer should probably do a bit of both. You know?

**Leigh Brady:** Yeah, that's good advice. When in their career should they do any of these?

**Chris Gammell:** Well, it's my belief that it's better to do it the way I did it, which was an accident when I did it. So I went for the large company first. But the reason I think that's a good idea is because large companies have many, many opportunities within them.

**Leigh Brady:** Yeah, yeah.

**Chris Gammell:** Often they have graduate schemes. I was actually on a graduate scheme when I came in. So, you know, a specific scheme geared towards exposing new graduates to different areas of engineering so that you get to figure out what you like and what you don't like and what you're good at, what you're not good at.

**Leigh Brady:** Yeah, the grand buffet of engineering specialties that you could snack on.

**Chris Gammell:** Right. And I mean, and it's probably no surprise that, you know, many engineers come out of the graduate scheme saying, oh, I want to be a project manager. Don't want to be an engineer.

**Leigh Brady:** Yeah, yeah. Well, that's great.

**Chris Gammell:** Okay, that's fine. Right, right.

**Leigh Brady:** It's better to know that up front than to spend 10 years or 20 years miserable as an engineer and be like, and then, or even in a much more positive sense, like, you know, they have an aptitude for project management and they're going to be a great project manager. That's actually even better, right? Exactly.

**Chris Gammell:** The other good thing about large companies for younger or more junior engineers, less experienced engineers, is that they have large budgets and almost always have a training budget.

**Leigh Brady:** Yes.

**Chris Gammell:** Which is specifically meant to be spent on developing people and making them better. That's not to say smaller companies don't want to do that. But, you know, if it's a choice in a smaller company between developing the new product or, you know, spending 20 grand training, you know, three or four engineers, most often they'll want to develop the product.

**Leigh Brady:** Yeah.

**Chris Gammell:** So I think you can really bolster your resume and get good experience as a more junior engineer in larger companies if you do that right out of college. But I think 10 years is your limit to get out. And if you don't really get out, then you're not going to get out.

**Leigh Brady:** Yeah.

**Chris Gammell:** That's kind of the problem.

**Leigh Brady:** Yeah. Another one in there, I am in agreement with you on this. I'd say the other one that's in there is probably kind of tied into what you're saying here is the mentorship aspect. And, like, usually, you know, there are formalized mentor programs. But I think it's just being able to, you know, in big teams, you're going to experience a lot of people, different personalities, different archetypes, different people you may or may not want to hang out with after work. But I think you can almost always, you can learn things even in the worst case scenario of, like, that's not the kind of engineer I want to be, you know. Or I'd rather have a different outlook on life or whatever. I think that is a large piece. When I hear people coming out of college and then saying, like, oh, I want to go straight to a startup, I'm like, you know, you're going to get a lot of really cool experiences like that. But you're not going to have the, you know, then you're going to be a little bit more in the open for trying to find a mentor or someone to lean on. And, you know, you pay for design reviews. You just have to work harder, it feels like, on that, on, like, building your own, your rails, basically, to make sure you don't proverbially go off them.

**Chris Gammell:** Yeah, that's definitely true. And the individuals that I've observed that have come out of college and gone into startups or even tried to start their own companies, the ones that were successful were, they just weren't like us mere mortals, you know. They were extremely gifted engineers. Yeah. And they were gifted not just in engineering, but they had business acumen and they seem to have almost sixth sense for being able to figure out where they should go, what they should do and what they should learn next.

**Leigh Brady:** Yeah. Yeah, we had Phil on from Phil Salmoni from Phil's lab. And I feel like he's, you know, very talented, younger engineer, went out on his own pretty early. But even he kind of expressed the same thing. He's like, you know, how do I find people to work with? I think he is designing that for himself now. And he's already a very talented engineer. I'll link that show in, too. But, yeah, it's a tough thing, I think. You know, it's just you have to understand that you might be kind of jumping in the abyss. And there's some excitement there, but it could be also frustrating.

**Chris Gammell:** There is. And it's interesting you mentioned the mentorship aspect because you've reminded me of another quite big stark contrast between the UK and the US that I noticed, at least. So in the US, I'm sure you're aware, we have the professional engineer, the PE, which you can study for and get. But most people don't really do that unless they're working in some aspect of civil engineering.

**Leigh Brady:** In power engineering, I feel like, and building engineering. Right, exactly. Electrical versus electronic, I feel like.

**Chris Gammell:** Right, that's absolutely true. Well, the UK equivalent, and I'm not sure it's really an equivalent, is the chartered engineer. And chartership is much more different to that. I was a chartered engineer when I was over there. I actually haven't maintained it.

**Leigh Brady:** Yeah, I'm an EIT. I never went for a PE, personally.

**Chris Gammell:** Right. And it's basically, as you said, like an organized mentorship thing, but they split it into five aspects, five different categories to do with, obviously, technical proficiency and use of innovative technologies, but also interpersonal skills. Oh, that's nice. And designing with environmental, designing with your impact to the environment and the culture and the people around you. So they tried to make it very holistic. And in order to become chartered, you have to be mentored, submit your intent to be chartered. And then it's not an exam. It's done via interview, where you present work that you've done and kind of show that you've actually done stuff on the job. So it's much more geared to show me you're an engineer now, not can you pass another exam?

**Leigh Brady:** I like that. Yeah. I like that. I mean, it's tough because it's subjective then, right? And there's probably a jury or equivalent and there's always stuff with that, potential politics or whatever. But I think it has the most flexible outcome because of the work that you're doing specifically versus knowing the load forces on a pulley system.

**Chris Gammell:** Exactly. Yeah. And it's about trying to further the profession. Right. Yeah. And make sure that the profession is generating engineers that are conscientious and are designing things that are going to be useful to people, but also are not going to be harmful. Which I think is a good idea. But, you know, it can, I think it does an excellent job of not straying too far into what might be considered kind of, you know, hippie kind of tree hugging ideas, you know. Yeah, yeah, yeah. But it does.

**Leigh Brady:** It's a real reality you're saying.

**Chris Gammell:** Right, right. It stays in the right side of that and just says, well, you know, what are you actually doing when you're considering your designs? What did you do to make sure that, you know, have you thought about how this product is going to be disposed of? And the electrical waste is going to generate and so on, which I think is very important.

**Leigh Brady:** That's great. I, you know, that it would be, if people are listening and they know some of the things in the US, I would love to hear about it. I, I don't think the PE is that. I don't, I mean, there are very important reasons for the PE, but not, not, not that. Maybe we could start something like this.

**Chris Gammell:** Yeah.

**Leigh Brady:** Should we start a US based standards party? Ooh, that's exciting.

**Chris Gammell:** I'll ask the IEEE if they want to give us some money to do so.

**Leigh Brady:** Oh God. Yeah. Yeah. Like, well, please submit a 45,000 page paper and.

**Chris Gammell:** A triplicate, of course.

**Leigh Brady:** Yeah, of course. Of course. Yeah. Yeah. Oh man. Yeah. Okay. Well, I also wanted to talk about, so we kind of danced around a little bit, but I think our first guest who's worked. I mean, so defense is not a super common thing here, but specifically nuclear in, in the defense industry. So, what's that like? Nowhere near as sexy as you might imagine. I actually didn't, I didn't, frightening is probably a thing I would say, and then probably bureaucratic would be another, I would assume.

**Chris Gammell:** Yeah. Yeah. Yeah. Heavily, heavily regulated industry, obviously. Probably the most regulated industry I could think of, and I think that that's a good thing. It's not in any way really dissimilar to other aspects of defense apart from the heavy regulation. And it's very interesting to see how you go about designing something to be very, very safe. So, I think it has a lot of parallels with other safety critical systems like self-driving cars or transportation. Because obviously, one of the ways that safety critical systems are designed, especially if you're designed to the IEC standard 61508, is that they are assigned a safety integrity level. And I think from 1 to 4, with 4 being the highest, and the level that you assign is dependent entirely upon the consequence of something going wrong. And so, obviously, you can imagine nuclear weapons industry, the consequence of something going wrong is very, very high. Yeah.

**Leigh Brady:** I feel like, actually, that's a good point, too. I should have said, I said nuclear, but we're talking nuclear weapons here. This is especially, like, this is, this is a little weird. I mean, this is a little odd for amp hour, I think, you know.

**Chris Gammell:** Yeah. And, you know.

**Leigh Brady:** How do you feel about it? I mean, like, you're not in it anymore. So, what was your, what was your take when you were, like, moving into this space?

**Chris Gammell:** Yeah. I mean, I kind of honestly applied for a bunch of jobs at a job fair, and this was one of them. And this is the one that fruited. It was, it was good. It's the, they don't just do that. You learn about a lot of different things, and you work on a lot of different aspects of stuff. So, a lot of the industry is also geared towards non-proliferation.

**Leigh Brady:** Sure.

**Chris Gammell:** Yeah. So, you have to, there's a lot of work that goes on into verifying non-proliferation, which is very difficult. Because you imagine, how do you go into a, even if it's a friendly country, and say, and they say, we don't, you know, we haven't got any nuclear weapons, and we'd like to verify that, please. And they say, well, we don't really want you looking at our... No, no, we promise. We promise. Exactly. I swear. So, it's lots of interesting ways to do that, and technologies surrounding that. But, yeah, it's a, I do think that it can be looked at in two ways. Obviously, these things are incredibly destructive. It's an odd place to work when you go to work every day hoping the thing you're designing or working on is never going to be used.

**Leigh Brady:** That's right. Yeah. Yeah. I mean, I've kind of heard of the, when I've talked to other people in the defense industry specifically, they always focus on defense, right? It's never offense. You know, some weapons are used defensively, and that's, you know, neither here nor there. But it seems like from a kind of a mental survival kind of piece, like developing these things, it's like, well, we focus on the defense piece. And then how they're used is how they're used.

**Chris Gammell:** Yeah, I think that's true. I think it would be churlish of me to say I never had any kind of thoughts or inner conflicts about what I was working on. But the UK pushed, they don't even call them nuclear weapons. They refer to it as the nuclear deterrent. And the idea is that it is a deterrent. I suppose it's kind of the idea that I'm sure you've heard of mutually assured destruction, the idea that if everybody who could possibly hurt each other has the means to hurt each other, then no one will hurt each other, which is kind of a weird way to... Indeed, it is mad. Mad world, right? And I totally agree with that, that it is kind of strange and it is kind of mad. But then there is the statistic, of course, since the Second World War, that there haven't been any wars between nuclear powers.

**Leigh Brady:** Yeah, I mean, honestly, with Ukraine, we're right back in this too, right? I mean, it's interesting, not interesting, it's sad and terrible. I mean, honestly, it breaks my heart every day. But I don't know that would have happened if it was like, Ukraine used to be nuclear and now it's not. They gave them up and whatever, whenever that happened. So it's kind of crazy like that. It's just...

**Chris Gammell:** Well, I'm not sure that the Ukraine ever had nuclear weapons. Maybe they did. I'm not sure. No, I mean, they did as part of like...

**Leigh Brady:** Oh, when they were part of Russia. From when they were part of the USSR, they had weapons. They gave them up based on a trilateral treaty between, I think, the UK, US and Russia, saying that there would never be any kind of action against them, yada, yada, yada. And not so much. But, I mean, so just as like a... Here's the real thing. I didn't think... Prior to three months ago, whenever the Ukraine aggression started, like Russia aggression against Ukraine, I didn't have any fears of nuclear war, right? I mean, like, it's always been an ever-present threat. But I never, like, as an adult thought, like, oh, I might die in an atomic fireball tomorrow. But, like, those thoughts came back, right? And it's just like... But there is this peace, like you're talking about, that prevents it, which is crazy in its own right.

**Chris Gammell:** It is. I think it's definitely an odd time to be alive, with all that's gone on in about the last two or three years. But I also am comforted by stories that I've read of instances during the Cold War, when, you know, the control room in Russia... Yeah, yeah. You've heard about this, had lit up, and was indicating that, to all intents, that the US had launched a nuclear attack. And obviously, it was malfunctioning. And the person in charge of that decided that they would not retaliate, even though they had the means and the authority to. So, just because there is one crazy guy at the head of a government, I like to think that there are at least a few people in the chain of command that aren't as crazy. But maybe it's wishful thinking. Maybe it's my way of going about my day. Yeah, right, right, right.

**Leigh Brady:** Okay, so now, there's obviously a large ethical kind of piece there that we were kind of talking through a little bit. But I get what you're saying. I mean, I hear you on these things.

**Chris Gammell:** Ethics is important. And I don't expect everyone to agree with that either. Yeah.

**Leigh Brady:** On the internet, Lee? What are you talking about? Everybody agrees with me. Internet. Yeah, that's true.

**Chris Gammell:** That's very true.

**Leigh Brady:** So then, okay, so then, boots on the ground, designing this stuff. I mean, did you ever, so you're developing like embedded systems around it and stuff like that. How much, how do you even do field tests, like testing? Like, how do you test this stuff?

**Chris Gammell:** Well, the electronics control systems can be tested standalone because they're very much like any other electronic subsystem. You just, you create test boxes and you have the expected inputs, the expected outputs. And so that can be tested. In terms of actual nuclear testing, no nuclear testing has gone on for a long time. Certainly not while I was in the industry.

**Leigh Brady:** Yeah.

**Chris Gammell:** And it's all done in simulation. Huh.

**Leigh Brady:** Yeah.

**Chris Gammell:** So there's lots of modeling goes on. And there's actually a large, I think the, certainly the UK's biggest laser. I think it might be one of the biggest in the world, near Reading in the UK, which generates incredibly hot temperatures. And it's used in academia in the UK to study fusion reactions and so on, but also can be used.

**Leigh Brady:** Only 30 years away. Only 30 years away. Exactly. Yeah.

**Chris Gammell:** And so they use that too for, for, for improving the models of, of, of the weapon systems as well.

**Leigh Brady:** Yeah. So to tie back in the systems engineering piece that you talked about then. So we don't need any specifics, but like what gets pushed on the chain? Is it like, is there a new specification of like, we, we had X last year, five years ago that we designed and deployed. We now have to do Y and the improvements are Z. Is there like, are there high level dictums like that, that some people, someone's came up with some kind of like better mousetrap to use a terrible, terrible, uh, algorithm.

**Chris Gammell:** Kind of, but the, the, the, the, the timescales are vast. Uh, in the order of 30 or 40 years for developing new systems depending on. Oh, wow. Yeah. More often than not, it's things like, uh, an upgrade. Upgrades in the terms of just things degrade over time. Oh, sure. Sure. Right. So, uh, that kind of thing, uh, parts.

**Leigh Brady:** I guess sourcing, like we talked about earlier, like. Exactly. Can't get this part anymore. We need to redesign the system. Exactly.

**Chris Gammell:** And requirements come down from ultimately the government in huge, great big swathes of paper, um, that then get disseminated and digested and broken down.

**Leigh Brady:** Uh, last question, uh, uh, a cheeky one, uh, before we move on to your next stuff. Did you ever wear a white lab coat? I feel like it's kind of a requirement as part of. It's interesting.

**Chris Gammell:** I don't, I don't think I did. And here's, what's kind of funny. What I discovered in, in the industry, all the scientists wore lab coats and Metallica t-shirts and all of the engineers wore suits and ties.

**Leigh Brady:** Interesting. Yeah. I mean, good on the scientists for, first off for having Metallica underneath. That's interesting. Yeah.

**Chris Gammell:** Yeah. I, I, I kind of veered more towards the Metallica t-shirts and in some respects was not well received. Uh, but, um, but yeah, it's, uh, it's kind of funny. Yeah. And so, yeah, British engineer, suit and tie, a jacket, U.S. engineer, chino and polo shirt.

**Leigh Brady:** Yeah. Yeah. That, that, that fits my experiences. Well, actually, I don't, I don't know if I know too many UK engineers, but at least the, I can, I can verify the, uh, the U.S. version. So, yeah. Okay. Uh, so you've moved on from this industry. You've moved to actually different industries. And I should, I should mention you've, you were introduced to, to the Amp Hour by, uh, Carmen Parisi, past guest of the show and former guest, former host of, uh, the engineering commons. Uh, you guys work together at Wasatch. Um, we talked about that a little bit, but that's a photonics company, right?

**Chris Gammell:** Yeah. Yeah. So Wasatch Photonics, where, where I met Carmen is a spectrometer company designing Raman spectrometers. And, uh, those are devices used basically to measure light by wavelength and you can use those to do all kinds of cool stuff. And I kind of, I really like working in that industry. There's lots of really cool, uh, applications for that from drug detection to, you know, medical applications as well.

**Leigh Brady:** Yeah. Yeah. I mean, this is interesting too, because like, so you had another optics company on your thing. I mean, like in terms of like crossover, you know, I wouldn't think, you know, going from like defense contractors specifically to an optics company. But like, when you look at any kind of a system like this, it's like, all right, high speed signaling and FPGAs and stuff like that. It seems like, oh yeah, that starts to really match up.

**Chris Gammell:** Right. Like, for example, there are lots of good reasons in a, in a, in an optical environment why you'd want to use an FPGA, mainly because the sensors require really tight timing. And maybe you could do it with a micro controller and a real time operating system, but you probably need quite a beefy one. Um, and FPGAs and CPLDs perhaps are really suited to that tight timing and parallel processing. So it's, uh, yeah, it's, it's, it's quite an interesting application for FPGAs because most people I think consider FPGAs to be the workhorses of digital signal processing.

**Leigh Brady:** Yeah.

**Chris Gammell:** And, and so on. Whereas this is much more about exploiting the tight timing relationships of clock signals to accurately move charge across the CCD basically. So that's, it's kind of really, really cool. Yeah.

**Leigh Brady:** That's great. That's great. I mean, yeah. And I think, I think any kind of like signal chain types, usually signal chain or single, you know, signal path type stuff. I started thinking, well, maybe signal paths RF as well, but like FPGAs start to filter in the back of my mind. It's like, uh, you're probably gonna start seeing those on a board.

**Chris Gammell:** Yeah. Yeah, exactly. The interesting thing is though, that FPGAs tend not to be very good at doing stuff like, uh, handling USB comms. I mean, it can certainly be done, but. Right. Most people know how to put down a microcontroller and often the microcontroller is going to have a USB five built in. So, okay, now I've got USB comms. So if you want to make a USB device that, uh, works with the CCD, most often you put an FPGA and a microcontroller in there.

**Leigh Brady:** Ah, gotcha. I mean, they're starting to smush those together a lot too, right? That's common, more common these days, but.

**Chris Gammell:** Absolutely. Like the same part that I think we mentioned before. Yeah. And then you've got smart fusion and all those others, but sometimes the problem with that is that you can end up with power density issues. Oh. Oh. And also a lot of those parts are meant with, uh, meant for use, not for embedded systems. So if you're trying to make a system that's handheld or embedded. Oh yeah. Battery powered or something like that. Yeah.

**Leigh Brady:** Battery backpack. Exactly. Yeah. Yeah. Looking like a proton pack on your backpack. Yeah, exactly. Oh, interesting. I mean, it also kind of feels like, like Wasatch specifically photonics in general, like, like it is kind of tested measurement as well. Like just kind of these low volume, high specialized, that sort of thing. And now you're, you're currently at Phillips in the medical space as well. And that kind of, again, it's medical now. We were kind of wanted to talk about medical and you, you had mentioned earlier, like medical kind of sometimes crosses over with, with defense as well, in terms of regulations and stuff like that.

**Chris Gammell:** Right. And I think the medical industry is obviously a highly regulated industry. Uh, it's just different regulations. And the way those regulations get applied is slightly different. But for example, the FDA independently audits medical device companies and medical, um, instrumentation companies. And, uh, the way in which you design the devices has to be done such that you can, uh, provide the evidence. To the FDA that you've done your diligence. Mm-hmm. In your design. It's not, it will be no surprise. To anyone if they, you know, if they're not familiar with it to see how it works. But it is, it is diligent, it is stringent. And I am grateful for it because I, you know, we're all probably going to be patients at some point in our lives. And I want whatever I'm hooked up to, I want to make sure that someone did their diligence. Right, right.

**Leigh Brady:** So, yeah, it is definitely like a more kind of conservative design approach overall. You might not be on the hottest new part. You might not have the hottest new thing. But do you really care about that when you're hooked up to the machine? Oh, no, this doesn't have Wi-Fi.

**Chris Gammell:** Well, some of that's true. But actually, I found the medical device industry to be much more open to the use of newer technologies.

**Leigh Brady:** Oh, interesting. Okay. But is the FDA also in that camp or no?

**Chris Gammell:** Well, I think so. I mean, because it's not, the FDA is not really, they're not someone that I think are going to prescribe to you what you must use. They're going to, they're much more interested in prescribing to you the kind of diligence you have to do to prove that your device is safe.

**Leigh Brady:** Interesting. Okay. So, it's just telling what you're going to, like any kind of like audit or ISO process type of thing where it's like, you need to write down what you're going to do and you need to prove that you did that sort of thing.

**Chris Gammell:** Right. It's kind of like ISO on steroids, I guess. Yeah. You know, it's like, it's very much more involved than ISO because it has to be. But it is something that is geared towards making sure that something is diligently safe at all levels. So, it's less concerned with the implementation and it's less concerned with the specific solution. It's more concerned with, given a certain solution, can you prove to me that it is safe? And so, if you choose a technology that is hard to prove is safe, then yeah, that would make it difficult. But that doesn't preclude you from using newer technologies so long as the way in which you do your implementation.

**Leigh Brady:** Right. And I imagine companies that are selling into that space too, they also have an onus of wanting to show the engineers that might design it in that it's, hey, look, this is easier to get through because we document X, Y, and Z.

**Chris Gammell:** That's true. I think a certain amount of similarity can help. The other thing that I found is that, and this is similar in the defense industry, I think, a lot more time and effort is spent on, I won't say doing things to death, but lots of analysis, lots of data to back up things. Lots of, so for example, let's say in a startup, you want to measure a signal, you pick an ADC that you think meets your spec and you put it on the board and okay, let's go.

**Leigh Brady:** Way you go. Yeah, yeah.

**Chris Gammell:** Well, maybe here we'd pick an ADC in the medical device industry or defense industry, pick an ADC and it's got a spec on the data sheet, but we're going to test it and make sure that we're getting the spec that's on the data sheet.

**Leigh Brady:** And not just because you have interns available, you're saying, because it's a cultural thing internally that it's-

**Chris Gammell:** Well, the interns, yeah, the interns and co-ops got to do something. Yeah, well, they're still going to do it.

**Leigh Brady:** I mean, let's just be honest. I'm not doing it. I did that when I was an intern.

**Chris Gammell:** Right, but it's more like, I mean, you can imagine that it's not, I don't think it's the, you know, we don't trust the companies to over-inflate their specs or something on the data sheet. That's not the case. It's much more, you take a component and you implement it. Did your implementation cause a problem? Did you implement it correctly? Did you implement it in a way that wasn't quite how it was implemented and tested when the data sheet was written and so on? So you can see there's lots of traps and pitfalls that you could potentially fall into.

**Leigh Brady:** Yeah. That's interesting. You know, and actually that is consistent with the, my test and measurement equipment experience at Keithley. There was definitely that as well, because it was like, nobody's, the only way you're going to find this otherwise, if you're not testing it up front and have an ongoing like test process around it, you're going to find out the hard way by, you know, it gets all the way to do it. And they say, Hey, this isn't meeting specs because we're also testing our equipment. And so it's just like better to measure throughout the process. It sounds like then it's not codified. You know, like the FDA is going to do some kind of testing along the way or verifying that you are testing along the way, but it becomes a cultural thing then internally at the company that testing is a way of, of covering, covering for that eventuality. Right. Right. Exactly. I think that's exactly right. When you go into an interview. So like, because you kind of move between these different industries as well. When you go into an interview, like a, with a Phillips in a medical space like that, do you, do you talk about like, well, in the defense industry, I did this kind of process. And, and that's why I think like, do you try and make that connection yourself? Or was it more like they were targeting because you had those, those past experiences?

**Chris Gammell:** No, I made that connection myself. So, you know, I, I, I'm, I saw that, you know, I'd be interested in working with this medical devices because it seemed very different to what I'd done before. But also I could see that it was an opportunity to apply stuff that I knew how to do. So a new application of, of old, old ideas, I guess. And I assumed, and I guess I was correct that, you know, if you've worked in heavily regulated industry, then a different set of regulations isn't really that difficult to come to terms with or understand or use. It can be interesting, but you've, you understand the concept, whereas I know a lot of engineers that have worked in a lot of small companies and become aware through, you know, a chat over a beer or a coffee of the kind of things that I've had to do to satisfy certain requirements. And they, at first, are kind of like incredulous and, oh my goodness, why would you want to have to do that? Which I can understand if it's not your thing, but also that they just weren't aware of that because it never had to, it never really occurred. Never had to think about that.

**Leigh Brady:** Yep.

**Chris Gammell:** Yep. So, I mean, the closest that really comes to is like CE marking and FCC marking. And that honestly is, for most devices, is really not that hard and not that stringent.

**Leigh Brady:** Right. Yeah. I've talked about many times in the consulting space as well. Like, I think when, when Charles was on, Charles Elwood was on the show most recently, we kind of talked about this as well, where like, as a consultant there, by almost definition, there's nobody there to check your work. Right. So you have to become that person that checks your own work. And, and like the best consultants like Charles, I think, check their own work and they show they can do this kind of stuff. And one of the things that I was surprised by coming into that space was first off, there, there, there was no safety net there. Right. So you have to become your own safety net. And then when I learned about a new specification or requirement around that sort of thing, like a, you know, a certification, it's like, then you just have to learn how to become the specialist of that certification as well. And like you said, it's not like, usually not overall, this out of left field thing. It's just, you need to know that you have to do it and you have to go find the specification as it's written. And then you have to learn all of the nuances of it. But then once you have that, it's like, okay, now I know how to apply this.

**Chris Gammell:** That's definitely true. But I think there's a subtlety to it. And that is that one of the guys I work with now, he kind of has a mantra that two people working in a team are worth three. And, and I kind of think that's true. I think with the best will in the world, you can be a consultant trying to be diligently cross check and double check everything you've done and interpret things, interpret standards. And you'll probably do a good job of it. But when there are other people with different perspectives that can challenge your ideas.

**Leigh Brady:** Oh, I have no doubt of that. I'm just saying in the, in the scenario where you don't have that, you need to be at least as good as one and a half. I think, you know, like, I think, right. Like, yeah, two is, yeah, definitely. I, that's a great maxim.

**Chris Gammell:** I think, I think it's just, you know, what I was trying to say is that that's a huge challenge. It's a really huge challenge to work like that. And it's actually something that I personally don't enjoy that much.

**Leigh Brady:** Yeah, that's interesting. Yeah. I mean, especially because, well, like, kind of we talked about ebbs and flows between bigger companies, smaller company. Now back in the bigger company, you do have, you know, there's the downside of more people, more bureaucracy, more, you know, kind of red tape. But the upside is more people checking your work, you know, especially that how that might play into younger engineers experience as well. More people checking your work, more structure, that sort of thing.

**Chris Gammell:** Yeah. And more often than not, more ideas, more people trying to challenge your ideas.

**Leigh Brady:** I don't always want that. But yeah, I think at least a little bit of challenge is good. Yeah. Yeah.

**Chris Gammell:** Yeah. I mean, I came from a place where I was the most senior engineer in a small company. While it was really good in some ways, in other ways, it can be fun to have the responsibility of decision making for certain things. But it can also be a burden. Yes. And it's good to have, to not, basically not be the biggest fish in the pond, I guess, if that makes sense.

**Leigh Brady:** Yeah.

**Chris Gammell:** So I really, really like the idea that, you know, there are people that will, not to say that, you know, I rule with an iron fist or something. We heard it here, folks. Right. Exactly. But it's good. It's good when you've got different people from different walks of life and different engineering disciplines and more engineering disciplines in a bigger company, of course.

**Leigh Brady:** Yeah.

**Chris Gammell:** Coming to you with different ideas and trying to challenge your ideas and trying to make them better. So it kind of broadens your horizons.

**Leigh Brady:** Yeah, definitely. I think, like you said earlier, I think, you know, having both in your experiences is going to enrich your abilities as an engineer and your job experiences. There's ups and downs to both, but it's best to just try it out and see what you prefer and where you are in life at the time.

**Chris Gammell:** Right. And if you prefer neither, you know, I think it actually gives you a good, if you decide to go out on your own and start consulting or something. I mean, if you look at any consultant that anyone has ever really hired, they didn't do that out of college. They've gone and earned their stripes somewhere. And you have to do that. Yeah. I agree.

**Leigh Brady:** Lee, thank you so much for telling us about all this wide variety of experiences. And, you know, just I think your experiences have really spanned across industries and size of companies and cultures. And, yeah, it's just been really, really cool to kind of catch the ebbs and flows of your career and talk through them here. That's great. Thanks for having me. It's been a pleasure. Where can people find you online if they want to catch up more or see what you're working on?

**Chris Gammell:** Well, I'm on LinkedIn, Engineer Lee, which is, you know, easy to find me. So, yeah. And I hope to enjoy watching future podcasts from your channel as well.

**Leigh Brady:** All right. Thanks so much. We'll chat soon. Thanks.

**Speaker ?:** Bye. administered administered administered administered
