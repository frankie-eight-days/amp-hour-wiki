---
episode: 573
title: Mixed Signal Education with Philip Salmony
url: https://theamphour.com/573-mixed-signal-education-with-philip-salmony/
---

**Philip Salmony:** This is The Amp Hour Podcast. Released January 17th, 2022. Episode 573. Mixed Signal Education with Philip Salmoni.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics. Hi, I'm Philip. I run the Phil's Lab YouTube channel and a professional hardware engineering consultant on the side.

**Phil's Lab:** Hey, Philip. How are you?

**Chris Gammell:** I'm good, thanks. How are you, Chris?

**Phil's Lab:** Good, good. I was wondering, because I know you go by Philip, but it's Phil's Lab. So is it kind of like you get into the lab and you relax and you're like, oh, call me Phil.

**Chris Gammell:** Well, it's always a thing, because Philip's Lab, I think, would sound a bit strange. And also, I never know, because I'm from Germany, I'm called Philip. And when I go to England, people usually call me Phil. So I never know what to choose.

**Phil's Lab:** I just like that idea of the lab is your happy place and that's where you go to relax.

**Chris Gammell:** That's true, yeah. Chill with Phil. I think I'll keep the chill with Phil on my channel now. I think it might make that.

**Phil's Lab:** When you do Q&A sessions, maybe you could do that. You could have a pipe and you'd be drinking a glass of scotch or something.

**Chris Gammell:** Perfect, yeah. Put on a little tweed jacket, I think. That sounds good. Perfect. You're giving me a good idea, so I was running out of content for YouTube.

**Phil's Lab:** Fire in the background, yeah.

**Chris Gammell:** Exactly. Yeah, I wish I just had a fireplace back home, I'm afraid. It's a bit lower budget than that.

**Phil's Lab:** Or where you are now. So you're in Denmark now, where the time of year is a little chilly?

**Chris Gammell:** Yeah. Yeah, it's working its way down to fairly low temperatures again. I'm just getting used to it. I thought Germany and England was bad in terms of weather, but Denmark really does beat that. Yeah. Yeah.

**Phil's Lab:** Yeah.

**Chris Gammell:** Yeah.

**Phil's Lab:** How it goes. Well, I knew how it goes. Exactly, yeah.

**Chris Gammell:** Exactly. I mean, after your move now, I guess you can look forward. I guess, does it get pretty hot where you are now? It does, yeah.

**Phil's Lab:** Yeah, it'll get up in the 40C range with a lot of humidity. So like 40C and like, you know, 90% humidity. It's a rough time.

**Chris Gammell:** I'm not sure if I would make the move to such a warm climate, but yeah, not bad.

**Phil's Lab:** Yeah, yeah. We'll see how it goes. We'll see if I melt this here.

**Chris Gammell:** Yeah. Well, I can freeze on the other hand, so I think we'll make a match there.

**Phil's Lab:** Yeah, yeah, yeah. So how long have you been doing the Phil's Lab channel?

**Chris Gammell:** Well, it started off as kind of, I just, I was looking into SM32, how to develop your own microcontroller board, going from Arduino to making something more producible or something that looks more professional. And that was, what was it, May 2020? I was looking into that and I uploaded this like three hour video just for me myself, first of all, just trying to detail how do you make a microcontroller board or with SMB components. And that was really bad audio quality as well. And somehow it got shared around and then took off. So I assume that was the moment where it kind of hit. So May 2020, what's that? Yeah, that's great.

**Phil's Lab:** Yeah, I mean, you started hitting my radar because you were doing stuff in KiCat or KiCat as you call it.

**Chris Gammell:** Yeah.

**Phil's Lab:** And, you know, that's great. I think specifically, you know, like it was the start to finish tutorial piece of it. Like being able to see, like people really love that being able to see everything there. And maybe they, you know, stop it and take a break after a half hour or come back to the next day. But being able to see that whole process is super valuable, especially for people that have never done a board before.

**Chris Gammell:** Yeah. No, and I think that was also the reason. Another thing is like the KiCat, KiCat. I still don't know how to say it and I still miss it up. You say KiCat, right?

**Phil's Lab:** I say KiCat, but it's really KiCat. It's fine. It's fine. Yeah, I never know, to be honest. I can't deprogram myself even if I tried. I've actually thought about doing a fundraising thing where, you know, people could donate to one or the other. And, you know, if we hit a certain threshold, I'll stop saying KiCat. But in my head, it's still always going to be KiCat.

**Chris Gammell:** Yeah, almost like a swear jar or something. Every time you say KiCat, I get to it.

**Phil's Lab:** Yeah, yeah, yeah. That's a good idea. Yeah.

**Chris Gammell:** Okay. Yeah, well, I keep messing up as well. But yeah, but basically, it was the thing. I think I was just scouring through data sheets and application notes trying to figure out how to. It sounds basic now, but at the time, every time I guess you introduce something new, it was quite difficult. Piecing everything together, what did coupling capacitors need? You need certain pull-ups here. What does this boot mode pin do? And I kind of wanted everything in one place. And I guess that then also helped, as you say, quite a lot of other people to see the whole process in one place. Yeah. So as a reference, basically, for myself, it started.

**Phil's Lab:** Yeah, that's great. That's great. And I think that as well with like the, you know, STM32 is this very popular platform. But when people are like, someone might go and see like a black pill or equivalent kind of dev board that's out there, making that leap from like a black pill and knowing that there's STM32 on there. And then like being like, well, I want to build my own board, understanding that piece and like the, all the other stuff you have to look up, like the data sheet that you're talking about. Yes. That's another really valuable piece, I feel like.

**Chris Gammell:** Exactly. Yeah. Just learning how to read a data sheet and pull stuff together. And it, I just feel like it enables so much more in terms of projects, being able to just go to data sheet and then pop that in your design rather than relying on plugging in or using an Arduino board and using these weird GPIO headers that always come loose. I don't know if, what your experience was with that, or if you had something like that, where you moved from an Arduino based system to STM32 or whatever microcontroller you were using.

**Phil's Lab:** You know, for me, it was, I came in from the analog side, so it was always weird for me anyways. Like I got to make microcontrollers very late in the game. I feel like late in the game, late in my career, even, you know, a lot of my stuff, I started out in the analog space. And so it was like, oh, well, there's digital people taking care of that. And, you know, where I was starting at Keithley, they were using like, like 68,000 parts as well. So I was not, I was not super keen to get in on that with like tool chains and all that stuff too. It wasn't until much later where I was like, oh, this just enables all this other stuff. And so, you know, I went the normal route of, I might've had background of electronics, but I went the normal route of, you know, Arduinos and, you know, then using Adafruit, SparkFun type stuff as well. And just learning like that.

**Chris Gammell:** But you started off with analog design, like straight out of uni or how was that?

**Phil's Lab:** Oh, no, no, no. Well, yeah, I mean, I... I went to university and learned a little bit about electronics. And then I went to work at Samsung, you know, ChipFab. Okay. And I didn't want to do that the rest of my life. And that's like a very specific career path. And so then I went back and went to work at Keithley Instruments where my alma mater was. And my friend got me a job, past guest of the show, Dave Young, actually. Yeah. And so that's when I really kind of, that was my true learning. That's what I tell people is like, that's when I really started learning electronics at the age of 25. So, 23.

**Chris Gammell:** Yeah. But that's really cool. Because I... After I graduated, I know for graduates, it's probably a lot harder to find like analog design jobs. But that, to me, is one of the coolest part of electronics is analog design. It's a shame you probably need quite a lot of years of experience to actually then get into that field. I mean, Keithley, they do like measurement equipment, test equipment, right? Yeah, that's right.

**Phil's Lab:** Yeah. Yeah. Yeah, I feel like it's, you know, it's one of those things where it's not as needed these days because of all the other stuff that's out there. You know, like you go... I'm sure you've read like Jim Williams' app notes from Linear Technology, right? Like...

**Philip Salmony:** Yeah.

**Phil's Lab:** His app notes are amazing. But like you go and look at all the stuff that's in there. Like one of his best app notes is how to do a thermocouple, like a really precise thermocouple measurement circuit. And for a long time, that was like... And like it still holds up as a circuit. It's still like a very... You know, it's got like a digital drive circuit with like some logic gates to drive one side of a transformer to send data, you know, so it's isolated and stuff like that. And like it is a very interesting, very cool circuit. But these days, you can literally buy... Well, outside of the past two years, you can just go and buy a thermocouple circuit that is at or better than that performance. And it's almost irresponsible to go and do what he did if you were a design engineer. You know, that's just kind of the world we're living in now. And so I feel like, you know, the analog stuff is like super intriguing, super fun kind of design and debug stuff. But if you were put on the spot by a company and said, design me a thermocouple circuit, it's like that is not the right answer, I don't think.

**Chris Gammell:** I don't know what your experience has been with that. No, I completely agree. It's always... But as you say, it's kind of the fun of developing or understanding what actually goes on in an analog circuit. But then the delay, you would just choose an IC to do the job for you and could do it a million times better. I had the same thing when I was quite into audio electronics. And if you want to just design your own discrete operational amplifier, for example, yeah, you might get lower noise levels. But the effort and the gain versus just buying like, you know, an E5532, it's like marginal compared to the design cost and board space and so on.

**Phil's Lab:** Yeah.

**Chris Gammell:** But I just love it as a learning experience. And I wish there were just more jobs or maybe I was born too late. I should have been born, you know, 20, 30 years ago to be able to do that kind of stuff. But yeah. Yeah, maybe. Maybe. Jim Williams didn't have like a... Almost like a cookbook or something where he had some really tough analog design questions. I saw that on a YouTube channel called like DevTTYS0. I don't think the guy actually still runs it anymore. But he was looking like some Jim Williams. Really bizarre questions on analog circuitry. And that's really something mental to test your knowledge.

**Phil's Lab:** Yeah, that's a good... I mean, it's a good way to do it. I don't know about the specific test.

**Chris Gammell:** Yeah.

**Phil's Lab:** I know that I have the books where they kind of packaged up all of Bob Dobkins and Jim Williams' app notes. It's called Analog Circuit Design, like volume one and two.

**Chris Gammell:** Yes.

**Phil's Lab:** Yeah. That's interesting to go look through. But I don't know about the test you're talking about specifically.

**Chris Gammell:** Yeah, I can't remember. I'm not sure it's entirely a test. It was basically a book with a collection of examples. And he would give you a circuit and then tell you, or how do you design a circuit to do this certain function?

**Phil's Lab:** Oh.

**Chris Gammell:** For the life of me, can't remember it, of course, now. Okay. Yeah, on that YouTube channel, as I said, I think that's where you can find it.

**Phil's Lab:** Okay. I'll go look at that. Yeah, that's the DevTTY, you said zero?

**Chris Gammell:** TTY is zero or something like that. Okay. It has some pretty cool videos on like, you know, silent key filters, a lot of analog electronics. It's a shame he didn't continue with his videos, but.

**Phil's Lab:** Yeah. Yeah. I mean, as you know, the stress of YouTube is, it is a harsh mistress. That's true. Always wanting more. Exactly.

**Chris Gammell:** Yeah. But you just went, you then went away from analog design or how did you then progress after Key3?

**Phil's Lab:** I know I went to an industrial, I went to ABB after that. Okay. Big in Europe, right? Yes. And then after that, you know, into marketing type stuff. And yeah, I kind of took a right turn and then came back to it, you know, came back to the, the technical side. That's what I've been excited about. Yeah. And, you know, like it's wanting to build stuff on an everyday basis. And I don't know, it's just the stuff that we, you know, both of us like doing, right? It's like building up circuits and stuff like that. I mean, you, you have all these designs. One of the things I really like about your videos is that you have a lot of stuff around like mixed signal, which I feel like is kind of a, you know, it's kind of getting into that analog side of things and all the analog considerations, but still using all these chips that require, or that, that maybe you don't have to do all the discrete analog design.

**Chris Gammell:** Yeah. No, thank you. Yeah. It's, it's kind of also the thing because I'm a musician and I've always wanted to kind of combine electronics with audio. And as soon as you want to combine audio with electronics, it's going to have to look at some sort of analog side, especially if you're, I was making or designing this guitar pedal, this effects pedal, which you can essentially reprogram to do distortions over like reverbs, delays. And of course for any ADC or DAC, you're going to have to design the analog circuitry around it. And once you've done it like a couple of times, you know how to do it, but yeah, it's this kind of mix and boundary, which I think is quite interesting, not getting too deep into designing the best analog front end or the best, you know, DAC interface, but yeah.

**Phil's Lab:** Something between. I think balancing costs too, right? I mean, that's, you could spend $30 on a DAC and it's like, all right, well that might have the specs you think you need, but like, can you optimize so that you can spend $2 on a DAC and, you know, still make it sound pretty good or, you know, like all of the engineering trade-offs that are required, especially audio where kind of people have an idea of what they think they want, but then actually like tying it back to truly needed specifications has got to be kind of tough.

**Chris Gammell:** And that's the thing. And you see all this audio hype, you know, 24 bit analog digital converters running at almost 200 kilohertz of a sample rate when it actually comes down to it, you know, much low is even fine and just finding that kind of balance. Right. Yeah. But no, I think it's a really interesting field, mixed signal. And that's also, as I guess shared with you was the mixed signal course that kind of tries to at least outline some of these design procedures, both on the analog and the digital side. And I kind of wanted to summarize at least my findings over the last few years into something that is kind of accessible for someone new to that field.

**Phil's Lab:** Yeah. Well, let's talk about the course. So you have a new course available. This is on, it's hosted on the same, on Robert Ferencz's Fedevel site, but it's your course on there and people can follow along and do it. What's kind of like, what's the outline of the course?

**Chris Gammell:** Yes, exactly. So it's hosted with or by Robert Ferencz who runs Fedevel Academy. His kind of sub site is called Fedevel Education, where other people that are invited can publish their own courses. So yeah, the outline of the course is essentially starting you through a whole design procedure for a mixed signal product or prototype. So you're given a very basic design description. So it should be a USB based signal generator and signal analyzer. You're trying to minimize cost. And how do you go from a really very vague design description to a final product that you can order at a manufacturing house? So I start off giving you the design description and then deriving the system requirements kind of step by step. What does the USB need to be capable of? What kind of data rates you need? And that means what kind of USB protocols do you need? What microcontroller with flash and RAM and so forth, leading through analog circuit design, digital circuit design, and then in key card, which is V6, which has also just been released or last month, I believe.

**Phil's Lab:** Exciting. Yeah.

**Chris Gammell:** Through PCB layout and routing, how to choose parts, how to cost optimize, how to design interfaces, and then actually getting it ordered. So it was kind of hard to pack all that information in, you know, five-ish hours. But I think it gives you...

**Phil's Lab:** Yeah, that's a ton in five hours. Yeah. And that's the thing.

**Chris Gammell:** I mean, if you can, leave a link to the course description. And it is just the description of the course or the content, though, just like in bullet points as a list is quite a number of pages. So I hope it's hard. I don't know, with your course, also finding the balance of how much information do you put in, how long do you make the course and the lessons and so on. So I wasn't sure being that this is the first course.

**Phil's Lab:** Yeah. I think what you're going to find is this is definitely like intermediate level. I think this is... You're going to need a lot of people that are interested in this sort of thing because of the audio. And I think you're going to get people taking it. Unfortunately, they're probably going to not have... Hopefully, they can just follow along, which I think there's always value in that kind of building muscle memory, following along, watching you do layout, copying the layout. That actually has a lot of benefit. But if they then are like, all right, I'm going to go design my own custom thing now, it's like, ooh, yeah. Yeah. You know? Yeah. That's a huge jump. And I always like to think about... Akiba, who we've had on the show a couple of times in the past, he and I used to talk about... He would always talk about breakdancing. I would talk about jazz. But I feel like in the same way, the first thing you have to do is learn how other people did it, right? You know? Yeah. Charles Mingus didn't play a banging solo the first time he played. It was like he would learn the classics first and all of the basics and how music is structured. And then eventually, you start to modify and play. And I feel like this is... Like having these kind of examples on your course or Robert's courses or my courses, like it's just about at the beginning, just following along. And as I tell people, so many other things can go wrong. Just try and follow the example first and make sure you get through it. And if not, you'll learn a lot from that things going wrong.

**Chris Gammell:** Exactly. It's almost like a thing when you... The first step when I look at a new IC is look at reference schematics, reference designs. And in essence, it's what you say. You look at the reference design. Just think, okay, how the hell am I going to do that? And just go through part by part. And I hope the course kind of details that a bit more, that you're not on your own. Yeah. Kind of guide it through. And I also found that not a lot exists on actually choosing or how to select parts. And it's questions I often get on the YouTube channel as well, is how do you even... You begin, how do I know I need this STM32F3 parts or this specific resistor? So, yeah.

**Phil's Lab:** Yeah, I think about like, you know, like you tell someone, all right, you're going to go choose an op amp. And they're like, okay, where do I go? And you're like, oh, you go to DigiKey. And they go to DigiKey and they're like, whoa, what is going on here? Yes. Exactly. Well, the thing is, you learn to like it. Yeah. Exactly. Yeah. There's other flavors. You can try Mauser if you want. You can go to Element 14 if you want. Really, you know, pick your poison, folks. It's...

**Chris Gammell:** Yeah. Yeah.

**Phil's Lab:** You got all the parts. So, I don't know what you... You don't have a choice.

**Chris Gammell:** Yeah. And it's just so... It must be... I mean, it still is overwhelming, right? Going to like a mouse or DigiKey part search and just, okay, what do I actually choose? But kind of over time, I guess you also like develop your favorite parts or familiarity. So, you're always like... I go to STM32 for a microcontroller. Someone else might go to TI or Microchip. But you kind of build up, I guess, a little like parts reservoir. Things you always want to go with.

**Phil's Lab:** Yeah. Yeah. Yeah. I always talk about like a mental library. I think that's... You know, and one thing that's nice is like, you know, watching videos like yours, even if I'm not, you know, yours or Robert's or Dave's or anyone's like that, right? One thing I'm doing is just kind of filing just the names in the back of my head so that when I hear it later, when I hear an idea later, like, oh, I need to do, you know, a DAC circuit. Oh, I can watch Philip's video on McSignal stuff and just go and look at that and use that as a reference and then almost having that as a, like a centralized location to start my search party out from, you know, like, oh, I want a 16-bit DAC or I want a 12-bit DAC. And here's the stuff that Philip thought was important. And do I think all this stuff's important around it as well? It's just so hard to, when you look at all the specs that are on a spec sheet, to know what to care about.

**Chris Gammell:** Exactly. Yeah. And it's even harder if you're doing this on your own or as a hobby and having no one to ask. So in a company, I guess it's different because you usually have a mentor. I don't know. I guess when you started at Samsung and then Keithley, I guess you had people around you to, I guess, supervise or design review.

**Phil's Lab:** At Keithley, there was not only was there, you know, mentors, like unofficial mentors, but then we would have, there were so many analog engineers there. We would have a meeting like with like 15 to 20 analog engineers in a room just talking about analog topics. And it's like, man, you can't, you literally couldn't pick a better place to like learn about that kind of stuff. That is really cool. So that, I feel very grateful for that.

**Chris Gammell:** That's really cool.

**Phil's Lab:** Yeah. It's not common, right? I mean, like, I don't know how you would do that otherwise.

**Chris Gammell:** No, it's also a thing. It's one thing I've also been noting because I've been working with startup for, I guess, one, one and a half years almost now. And that's the thing. I am the only guy doing electronics. So having no one to ask, it's kind of cool, of course, having the responsibility to make a product just by yourself. But especially like I haven't, I graduated about, I don't know, three years ago. So I'm not the most experienced person. So all of the course would be nice to ask someone else. And just joining a startup, I found that quite difficult. Like, who do you actually ask? Because no advice is really free. Of course, you can go to YouTube and sign up to courses. But yeah, in that sense, it would be good.

**Phil's Lab:** I found in the absence of, you know, so I also was at startup. I'm currently at startup. I mean, like, I, I find that like, you know, a lot of it is, you know, you could do media type stuff, you know, finding people on YouTube, like you mentioned, if, if your company is big enough or has the connections, or even if they don't, you could probably reach out. And, you know, like, I think applications engineers are like my life, lifeline for everything, you know, and, but like trying to get their attention is usually the tough part, if, you know, especially at a startup, but some of them are like, oh, startups, that's fun. You know, so, you know, lean into that sort of thing.

**Chris Gammell:** So you actually sent them just a mail asking, can you detail this or how do you do it?

**Phil's Lab:** Really? Okay. Yeah. And actually the best ones I find are actually, you know, there's the, the specific ones that like a chip company. So if you try and find like an ST, like app engineer, that might be tough. But if you have like a distributor with like some technical resources, I feel like they're like, if you can just like do a call with them and just talk through a design, because the other nice thing is, is the trade there is usually the information, right? They want to know like, oh, well, Phillip's got this design and it's got a DAC and an ADC and a microcontroller and all these other things. And they want to suggest other stuff in there. And so if you're willing to, you know, kind of open the kimono a little bit and show like, oh, here's what my design kind of consists of. They're going to be like, oh, well, let me offer you some more parts. But in doing so, they can often offer you advice and, you know, some guidance, which is very, very helpful.

**Chris Gammell:** That's a very good tip. No, I will definitely try that in the future.

**Phil's Lab:** Yeah.

**Chris Gammell:** No, that's awesome. Yeah. I mean, I've been trying to explore this via the YouTube, at least having that as a backing to say, okay, you know, you're not just an individual asking for a little advice. You can always kind of in return ask for a promotion or offer promotion and try and do that to ask for advice. But that's a, I'll definitely go with that. That's cool. Yeah.

**Phil's Lab:** Yeah. I think, you know, and it is this like, it's this weird kind of ad hoc network of people, you know, really to truly based around like commerce and money and stuff like that. So there is always that value transfer. But the nice thing is if you stay away from the sales side of it, right? If you don't like, you don't usually talk to a sales engineer, you just try and get to the technical person as fast as possible. At the end of the day, that's going to be a nerd. And like, I want to just talk to nerds. Like that's, now I want to geek out about a design and just like, oh, like, you know, I thought this was, you know, here's, you know, if you lead with like, oh, I had a problem with this, they're going to be totally into, you know, digging into that problem. I feel like.

**Chris Gammell:** So, yeah, no, that's a good point. Yeah.

**Phil's Lab:** Yeah. Have you, have you experienced that all in like, like in Germany or in Denmark? Have you, have you been in touch with that crowd?

**Chris Gammell:** Well, it was mainly at university. So at university, I was lucky enough to find a group of people who just loved engineering, loved, even though it's like, it's, it's kind of a beginner level, right? You're just learning about basic circuitry and how to root things up. We didn't have even have anything about, you know, PCB design at university, which is another thing I find bizarre.

**Phil's Lab:** Yeah.

**Chris Gammell:** Same. But yeah, just nerding out with people. I, I found it with a, with a friend of mine at the time, a drone club, you know, may building fixed wing aircraft and just being able to nerd out and try and figure out this system, which no one's worked on before, at least at our level was pretty cool. And just being able to nerd out and the same thing in a startup. You're just surrounded by people who are passionate about making technology, especially an engineering startup. And yeah, I mean, I haven't actually worked in, I worked on a larger aerospace company for, for very few months when I, when I left university, but that just wasn't for me. So I'm, I don't think I'm just the person to work in a large company, you know, nine to five and do that thing. I prefer this kind of work.

**Phil's Lab:** Yeah. I mean, the benefit of a big company is like you often, you'll be able to find other people that might be a mentor or, you know, technical resources, stuff like that. The downside is they're going to be like, well, Philip, you just designed this one little tiny part and just make sure it works perfectly and go to all these meetings, please.

**Chris Gammell:** And that's exactly the thing. It's that trade-off of having the like little responsibility versus having people to ask. And I prefer the startup life to be honest, just having that responsibility, trying to figure out a problem by yourself, of course, with a team of other people, but yeah, I don't know. But you, I mean, Samsung is a huge company, so I guess you had, and Keithley as well. So I guess you had the more, I don't know, traditional route to start with.

**Phil's Lab:** Yeah. I mean, Samsung was like a totally different thing. That was a, that was a chip company. So like that, or sorry, that was a chip fab. So I was not even doing electronics. I was doing process engineering. But at Keithley, yeah, I mean, that was, that was pretty, the only reason that there was, that I was able to like put hands on to like deep technical problems is because it was a pretty small company. Actually, it was only like, I think it was like probably 50 total engineers, but they had like a product line that had like 20, 25 products. And so, and I was doing like, you know, product, new products or, you know, release product support. So that helped too. You know, just being the repair, you know, a lot of people talk about being in repair first is a, is a great, a great way to see a lot of problems with finished designs and that sort of thing.

**Chris Gammell:** And that was straight after uni, university, you said, right?

**Phil's Lab:** That was, yeah, like two years after university.

**Chris Gammell:** Okay. But did you have anything about PCB design at university?

**Phil's Lab:** No, no. My first design was actually, my first layout was in Eagle, not watching YouTube, just like talking to people. Yeah. At actually did, uh, YouTube had not started yet. That makes me sound old. Okay. Okay. What was that before 2007? Yeah. Yeah. Yeah. YouTube actually had just started. So it was 2008. I started it at, uh, Keithley and, uh, wow. YouTube wasn't a thing yet. So, you know, just like following guidelines from other people at the company and using Eagle and back when Eagle wasn't owned by AutoCAD, it was like a German, just the German company that started it, had it around for many years. So, yeah. Yeah. Yeah. Boy, Philip, that makes me feel old. I got to say. I'm sorry. No, better cut that out. No, no, no. It's great.

**Chris Gammell:** It's great. It's great. Yeah. No, but, but yeah, I just thought it was such a shame because to me, PCB design is actually one of the most fun parts. And actually it's not just connect the dots, right? Right. It's controlled impedances, spacing, God knows what, stackups, and it's a whole another side to engineering. I hadn't been even exposed to at university. Yeah.

**Phil's Lab:** Yeah. I feel like, you know, at the university level, I asked that. I remember like asking this, actually, I went to, I went to a thing called the electrical and computer engineering department heads association. Okay. And I remember asking a question at like one of the round tables that was kind of in this realm of like, well, why, you know, why aren't you teaching these things that are practical and, you know, that like people want to learn and stuff like that. And they're like, well, uh, you know, students will learn this over time and we don't have time to, to like, to learn all these programs or something like that. It's like, I don't care. Like that's your job is to like teach people this stuff. I don't know. I feel like it's, it's looked down upon maybe in like the, up the echelons of, uh, you know, ivory towers of education.

**Chris Gammell:** But yeah, maybe, I mean, I, yeah, I understand the fact that you should expose students as much as possible to introduce topics, but in an electronics engineering degree, not even mentioning PCB design or actual circuit design, I find is a bit, bit odd. Instead we proved, I don't know, like vector calculus, like Stokes theorem or Gauss's law and things like that. It's a bit of a shame. Yeah.

**Phil's Lab:** I do feel like it would be a good way to, it almost would be like a good way to, as like framing for discussions, or I guess it'd be probably more base physics, but like talking about Maxwell's equations and talking about it, like using a PCB trace as a, as an example. But I feel like that because of the separation maybe between physics and, and electronics or electrical groups, maybe that's why I'm not sure.

**Chris Gammell:** Yeah, no, I agree. No, but it's no, it's a shame, but I, I, I just hope, cause a friend of mine actually introduced me to key card when I was at university. And it was like, you know, you see the cool black background, these Toronto, looking traces and that kind of got me hooked to start with, but it wasn't actually the university doing that. It was through a friend. So very thankful to him for introducing me to that.

**Phil's Lab:** That's great. That's great. Yeah. How it all started. And so that was in, was that in service of that, uh, that, uh, the, the fixed wing group that you mentioned?

**Chris Gammell:** That was actually a different guy. I, we went to the same, well, the same university, same course, same year. And he, I don't know how he got onto PCB design, but he just showed me this program, gave me the first little pointers and that was, that's the, I know.

**Phil's Lab:** And then you're hooked for life, right? Then you're hooked, right? That's the beginning and the end. Sorry, man. Connect the dots for adults. I mean, perfect.

**Chris Gammell:** Yeah. Yeah. No, it was only a surprise because it opens a whole world I didn't even know existed. And it's, yeah, it's a nice thing to be able to do because in these days, also with S and D components, it enables you to go away from, I don't know, not to sound derogatory with this hobbyist electronics, you know, where you have these dip components or through hole resistors enables you to explore so much more of electronics, just being able to design PCBs. I found at least.

**Phil's Lab:** So I think the, you know, the, the hobbyist stuff, or even just the, you know, the beginner stuff of like point to point wiring and breadboards and stuff like that. I think that's an important stage in the process. But like you said, I mean, like, I feel like it's just talking to people about like wanting to put your thing out in the world, just talking about like vibration on a quadcopter or a, you know, fixed wing. It's like, yeah, that, that, that breadboard is not going to work. And talking through it with people that are like, okay, yeah. So how do we make this more permanent? Well, circuit boards the way. And, and, and I think that transformation is, is very helpful for people.

**Chris Gammell:** Yeah, no, definitely. As you say it, like breadboarding definitely has its place and is great. And also for audio, like if you're just trying to, you know, design different filters or anything like that breadboard, you can't beat that. Yeah. But, but enabling the use of these really small chips or FPGAs or God knows what, I think if you can design PCBs yourself, it's such a plus. And also, yeah, just working on projects, at least that's what I found with employers being able to have your own project, have designed PCBs. That was a huge plus.

**Phil's Lab:** Oh yeah.

**Chris Gammell:** Makes you just really stand out.

**Phil's Lab:** Standing out in the marketplace. Yeah, totally. Totally.

**Chris Gammell:** Yeah.

**Phil's Lab:** People that are watching your videos. I mean, so you get a lot of feedback, people that watch the videos and stuff like that. What are people coming in with knowledge wise? I mean, I guess people coming to the course now, but coming to YouTube prior to that, what is the, you know, what is the level of people coming in?

**Chris Gammell:** I think it's quite mixed. So I would say it's usually beginner intermediate. I think it is that stage where you're kind of, you've, you've explored most of the capabilities of Arduino and then you're looking into, for example, how do I put the 80 mega that is used in an Arduino on a PCB? So, so that kind of level. So a lot of times university students studying electronics, hobbyists, advanced hobbyists, that kind of, kind of area. I don't think, you know, many professional people watch the videos. Maybe you do, but judging by the comments, it's, well, yes.

**Phil's Lab:** I have people, other people, uh, listen to The Amp Hour. We've referred to it before. So, yeah. Okay. I think you'd be surprised. I mean, like it's, there's a lot of, that's the other thing too. Like, you know, even when you've been doing this for a bunch of years, it's, I can still learn a ton of stuff. I have learned a ton of stuff from your videos. So like, you know, like that's the, that's the great thing is just like, uh, being able to see lots of, having lots of examples at hand, much like the Jim Williams book of application stuff, it's just like, it's so nice to be able to see that. Even if I'm like, oh, I think I know this, it might be something small within that circuit that I could, I could then go and crib later, you know?

**Chris Gammell:** Yes. No, true. That's a good point. Yeah. And I also, I've tried to initially started all, you know, with key cards and PCB, but I've tried to like branch out a bit with like signal processing and control systems. So luckily the viewers responded well. And I kind of follow the channel along that way as well. Cause I know many, what kind of stuff are you doing there?

**Phil's Lab:** Yeah.

**Chris Gammell:** So a lot on various fundamentals of signal processing. So how do you design IR or FIR filters, mainly digital signal processing, and then also stuff like sensor fusion, extended Kalman filters, how do you do state estimation? How do you design a control system given, you know, a certain system, kind of a mix of different things that I've personally find interesting and have needed in personal projects.

**Phil's Lab:** Yeah. Yeah.

**Chris Gammell:** So.

**Phil's Lab:** Yeah. I mean, you got to figure other people are going to be doing that stuff too. And I feel like the, something like a Z transform too, that's something where, you know, you learn that in a digital processing class and it's like, Oh, okay. I understand the math, but like actually like using it in the real world and like needing it for a filter design. It's like, Oh, wait a second. This exactly. I wish, I wish they would have started with that. I hope that a, you know, a college professor puts on your video first thing and is like, Hey, here's why you really need this.

**Chris Gammell:** Exactly. And it's, to me, that is still talking with like Z transform digital systems. Just the fact that you can add numbers in a certain way and multiply them in a certain way gives a different frequency response is mental. Like, yeah, totally. Right. It's yeah. What was it? The Fibonacci series. You know, you can write that as a linear difference equation, take the Z transform of the difference equation of the Fibonacci series. And it has a frequency. It doesn't make sense, of course, in that, in that context, but just the fact that you can do that. Yeah. I always thought it was mental, but yeah. Yeah. On that note. Yeah.

**Phil's Lab:** But I think that's good though too. I mean, I think it's like showing the, the wonders of the, you know, the math and the physics that's all around us. But at the end of the day, you know, I feel like that is just the, you know, kind of go back to the education piece. That's the step that always kind of gets skipped. And it's, it's at least what I was the hungriest for because I had such a hard time, like sticking with it and like understanding why I should be doing these stupid problems over and over again. And it's like, but you can do all this cool stuff with it. You know, they should start with the cool stuff. Always start with the cool stuff. Exactly.

**Chris Gammell:** Yeah. And it's, it's almost like when I was at university, my main resource was YouTube, because as you say, that's where you see kind of more practical things. You get exposed to the university, but then to me, it was the university of YouTube kind of filling in those gaps and seeing how you can actually implement that.

**Phil's Lab:** Yeah. Well, Philip, let me tell you the other things that didn't exist when I was at university. Oh God. Yes. Sorry. I'm sorry for bringing that up again. The iPhone. Exactly. Most of the internet.

**Chris Gammell:** Gmail. Fair enough. You definitely had it harder. My dad always tells me about, you know, the slide rules and not having a calculator. So that's even further back.

**Phil's Lab:** I can't even, yeah. You know, I was just re-listening to the Richard Feynman, surely you're joking, Mr. Feynman. Yeah. And he was talking about just like how proud he was about like the being able to estimate like log tables and stuff like that. I was like, why the hell would anyone care about that? And it's like, oh, actually that makes you like a thousand times more capable as a physicist because there wasn't the calculation capabilities then. Exactly. Yeah. Oh man. Yeah. Yeah. How have we moved on? I'm not trying to be like, you know, kids these days, even though I did say that last week. I think it's actually great. I think that it lets you get to the fun stuff faster, right? It lets you get to the application level stuff faster. Exactly. Instead of getting bogged down in the like, oh, you know, how do I, why do I even care about any of this stuff? It's just straight to the, well, I need this tool. Here's this tool. Here's how you do it. Watch the video and then you're good to go. You know, it's great.

**Chris Gammell:** Exactly. Yeah. And it just drives everything further as well. To me, faster, right? I mean, it's crazy. Wasn't it like on a, on a credit card, you have more computing power than the first moon landing had? Yeah, probably. Yeah. It's stuff like that. Stuff like that. But no, it's cool. I mean, what, as you say, kids these days, what toys they can play with and they don't have to, you know, use an abacus or something.

**Phil's Lab:** Right. Right. It's pretty cool. So then I think, I think that then the challenge is when you have all of the world's knowledge at your fingertips, it's like literally it's a, it's an attention problem at that point of like, okay, well, I know I want to do this thing. I know I want to make a guitar pedal. Yeah. How do I do it? And then it's like, because I don't know about you, but I've been on many a rabbit hunt down a rabbit hole and, you know, I've been on Wikipedia and just like, I, by the end of it, I'm like, I don't even know what I'm looking at anymore. I just wanted to find an op amp and now I'm, you know, 15 pages deep on Wikipedia. And it's like, why am I looking at this?

**Chris Gammell:** I very much know the feeling. Yes, definitely. It's also a thing being able, like not knowing what to choose, what to do next. Because there's so many cool projects or things to do. Or even just looking at the details, like you look at an op amp and then you look through, okay, how does an op amp work? What does the input stage do? And then you dive deep and deep and you kind of want to explore that and be able to do that. I just have such a hard time choosing what project to do next. Because they all just sound like pretty cool. I don't know how you do that. Or you even have the time outside of work to do your own projects.

**Phil's Lab:** Yeah. I mean, these days I don't. Okay. Yeah.

**Chris Gammell:** Yeah.

**Phil's Lab:** But I think, honestly, having like a secondary hobby, though, that feeds into it, that has been, I think that's a great way to do it. I mean, you've actually posted music videos, I believe, in the past as well. Yeah.

**Chris Gammell:** Yeah. Yeah. I try to design, when I have the time, guitar pedals, guitar amplifiers, either if they're just analog or, you know, mixed signal. I think that's, as you say, it's cool being able to combine both of your interests. Or if you have more, of course, multiple of your interests. And I think that's even what almost got me into electronics. So I started playing guitar, I don't know, 15 years ago. And I always thought, okay, like, how does this guitar pedal even work? This is distortion, even though it has a single transistor and a couple passes around it. And then finally being able to design it yourself and understand that it was, it's really rewarding. Yeah.

**Phil's Lab:** No, that's great.

**Chris Gammell:** That's great.

**Phil's Lab:** And I think having that, having that goal in mind is really important too, because you know, you want the pedal at the end or whatever. You've seen, you've probably opened up other pedals. You've seen what's involved, that sort of thing.

**Speaker ?:** Exactly.

**Chris Gammell:** And it's, it kind of repeats everything. Once you've seen like one guitar pedal of a certain type, like a distortion pedal, you've almost seen them all. And it's interesting to play around with that and then copy a bit and kind of go along. And what kind of interest did you have that merged with electronics? Was it also audio or music?

**Phil's Lab:** It was some audio stuff. I mean, I don't even know it anymore. You know, I got into some of the Badge Life stuff. So like doing blinkies and, you know, just stuff that I found laying around. Yeah. I don't know. It's probably not the same. I mean, test equipment stuff a little bit, but not nearly as much as people like Dave. Yeah. So, yeah. Yeah. I never really had like a really good, you know, I remember talking, I remember talking to one of the engineers at Keithway actually. And I remember asking him like, well, what do you, what do you do when you, what kind of stuff do you work on at home? He's like, I spend 50 hours a week working on really intense analog circuits. When I get home, I ride my bike and I'm like, oh yeah. Okay. Okay. You know, like, yeah. And, uh, I think there is that, you know, sometimes like if you're using up all your, your daytime hours and electronics, like some people I know that, that are like the best at electronics are the ones who are like doing software all day. And then they come home at night and they work on electronics or that sort of thing. So, uh, usually what I would do is I would work on electronics in the day and then I'd come home and talk about them on the podcast. So like I would say podcasting was my hobby, you know?

**Chris Gammell:** No, I mean, that's, that's also sounds like a better balance. I always find it hard to strike because at work here, you have to do, you know, certain projects. Yeah. Yeah. And then if you have certain other also electronics or engineering projects that you want to work on, you have to do it afterwards. So yeah. Yeah. It's for me, it's easy to slip on into the state of just doing electronics the whole day. So I have to stop myself.

**Phil's Lab:** Well, you know, luckily we have the part shortage to deal with. So, you know, that, that is like a, it's like a governor on our activity and output. So how has that been going with the, I mean, it's all your, all your videos are STM 32 based. Uh, how's, how's, uh, how's it all been going for you?

**Chris Gammell:** That's been interesting. Yeah. That's yeah. That has been very interesting. It's luckily passives aren't out yet. So at least that it only needs to have to redesign for the, for the microcontroller. The thing is also sensors. And as you said before we started recording also with a, you know, switching converters, it's just a real, but another on the positive side, I've been very good at, uh, you know, making footprints. That's true. Yeah. Yeah. Yeah. Every week I have to make a new footprint, a new symbol for that. And then, yeah. Yeah. I mean, it's a bit of a challenge to also just then find parts or minimize the design time you need for then redesigning. So maybe in that way, it's also a good, good practice. And it'll be so nice when it's back to normal at the end of this year. Hopefully at the end of this year. Hopefully. Yeah. Yeah. Just to have the freedom again to choose.

**Phil's Lab:** Yeah. Sorry. I think one thing that's going to come out of this actually is, um, when I think about like moving up the stack a little bit and like, uh, the amount of like maintenance that you'll need to have in order to like maintain multiple versions within organizations. So like thinking about people that have 15 revisions of their circuit board and like, what if they have to target something differently? You know, if it's like a power converter, okay, no big deal. But if there's like a sensor difference now you're, you just branched your firm, your firmware and you have to say like, oh, well, Rev A has, you know, this, the BME 280, but Rev B, we can only get the BME 680. And so it's like, so now you have different firmware maybe, and it gets loaded differently. So I think what's going to come out of this time is like better tooling around that sort of thing and just really more attention to it because it's been necessitated by the silicon shortage.

**Chris Gammell:** No, that's actually a good point. I hadn't thought about that. It's going to be like some sort of end dimensional branch that just branches out on firmware. Yeah. Okay. That's a good point.

**Phil's Lab:** I mean, the downside is that it's going to, uh, I think it's going to, you know, people are going to be dragging these, these, uh, things. This is just going to be baggage in organizations for years and years and years. Yeah. Yeah. Because, you know, if you've say you have put out five different versions of your product and you've, but you've made a hundred thousand of each of them, it's like those things are not going away anytime soon. So you have to support them and test them.

**Chris Gammell:** And that's true. I also wonder how it's going to be because people probably overbuying or hoarding. Yeah. You know, certain ICs, how that's going to like, if it's going to overshoot once production starts ramping up again and then people don't want to buy and then we'll shut it down. I wonder how that is going to run out as well. Uh, interesting.

**Phil's Lab:** Yeah. Like, will they just like use up their in-house stock and stuff like that?

**Chris Gammell:** Yeah. And if it'll settle again, I mean, I don't actually, what was actually the main reason for causing it? Do you know? Cause people say, you know, it was, it was Corona, it was some fire and some factory. Do you actually know? I'm not too informed.

**Phil's Lab:** Not, uh, not specifically. I mean, I think, I think there's been a lot of push pull around Corona, but I think a lot of it has been like reacting to reacting, you know? So like I talked to a friend recently and he's like, yeah, I switched, you know, I had to switch microcontroller platforms. I'm like, okay, well, you know, that, that happens. Uh, it sucks. But, but he's like, yeah, then I just like bought three reels of the components. I was like, oh. And so then you think about how that hits the supply chain then, because now, yeah, maybe there was stock of that one part before my friend bought it out. But now whoever was planning on that stock being in distribution has just hit the same problem. And so it just kind of like moves down the chain, you know, it's like.

**Chris Gammell:** Yeah. Yeah. And also, I mean, for companies that have enough capital to deal with that, I guess it's still kind of okay. So if it's a big car company or gone as well, but, but hobbyists and also as I've seen in the startup, it's a real, real trouble. And, and you, I mean, luckily like governments and loans and God knows what are usually more lenient because of the chip shorted end because of Corona, but it's been a real, real problem having to redesign, not being able to get enough chips. And if, yeah, if you don't have the financials to actually purchase a certain amount to fit your design or production needs, that's a, that what I've seen is a real problem.

**Phil's Lab:** Yeah. No, I mean, I think, I think that's gonna, you know, there's, we're two years in now and it's like some companies are just like running on fumes and running on their backs, you know, their back stock basically. And just hope, you know, just clearing out their shelves and selling everything underneath themselves. But hopefully, you know, hopefully the builds are going there. I think also hopefully like the, you know, the distributors are giving credit and stuff like that too, or CMs are giving credit, but yeah, it's tough in the small, the small kind of volumes. I mean, what, what kind of volumes are you usually designing in?

**Chris Gammell:** Usually for, in the startup, at least for like the 50 to a hundreds, which isn't huge, of course, in comparison, but then, then again, it's an early stage startup. It's existed for just over a year, but it's still at a volume in that if you need, I mean, a certain PCB I was making fairly complicated, you know, over 500, 600 parts, various different ICs. And you have to redesign for all of them or have those in stock for a hundred. And then times, I don't know how many components are on that board. That can be a serious problem for startups. So yeah.

**Phil's Lab:** Yeah.

**Chris Gammell:** I don't know. I mean, as a consultant, how much of you had a problem with that when you're doing designs for clients?

**Phil's Lab:** Yeah. I mean, basically it's just having hard conversations with them. Be like, look, here's the reality right now. You can either buy and hold all this stock up front so that you're certain that you can build this thing. And even still, you know, you're going to make some, some, uh, hard decisions on what is or isn't in your product because of that. Or I'm going to, you know, as the consultant, I'm going to redesign it three times just to work with whatever's there. And then there's just less reliability. Like, so then it's either I have to put more testing towards it or we have to just kind of cross our fingers or, you know, and so it really depends where it is in the life cycle of the product. But it's just a, it's just a crap situation all around. It just sucks. It's still fun. Like people have been saying on Twitter, it's just not fun to be in hardware right now. And it's like, it's not, but it's, um, it's important.

**Chris Gammell:** Exactly. Yeah. Yeah. No, it's been kind of stressful as you say, because every time you make a design change, even just designing on it, making a small change, but having to change ICs every single time, it's the most stressful thing waiting for your boards to come back and hoping they'll work.

**Phil's Lab:** Yeah.

**Chris Gammell:** Right. Exactly. Yeah. Yeah.

**Phil's Lab:** You know, and so like, I think, you know, again, like other like silver lining type things are like, there's going to be modernization of documentation systems just because you have to like, you know, there's just more churn right now. Like, so everything that, that churn results in, I think, you know, so you need to be able to document it better. You need to be able to write more flexible firmware. You need your sourcing groups to be a little bit better about maybe paying for things up front where there's, they were like net 30, net 60 before, you know, it's just like you do what you got to do, but I think, I think it'll be operationally better for companies at the end of the day.

**Chris Gammell:** Yeah. No, that's, yeah, that's pretty, very true. And there's also, aren't they making new like fab houses or fab plants in the U S now because of this? I mean, that's going to take ages. I assume to even set up.

**Phil's Lab:** Yeah. And they're all targeting at the top end, you know, like that's the real problem is that like, yeah. So Intel might be buying new or, you know, putting up new fabs or TSMC is talking about putting some second gen fabs here. Um, Samsung's growing my, my own employer, but it's like, that's, that's not what I care about. You know, I, I want TI to put, you know, I want TI to reopen their, their Richardson plant to full capacity. And like, I want some of the Silicon Valley plants that are doing like 300 nanometer or sorry, a hundred millimeter wafers and stuff like that. You know, it's just like the stuff where it didn't make financial sense and they all moved it overseas. And now it's like, no, no, no. Open those back up, please. Yeah.

**Chris Gammell:** No, definitely. Definitely. Yeah. Yeah. But, but how do you do it then on like a personal level, like as a, for your own personal projects, if you work on them, do you just design it like, you know, a week before and trying to send it off as quickly as possible or.

**Phil's Lab:** Uh, I have taken the tact that I will not, I will not send out a circuit board for design until I have the parts in hand. Yeah. Cause it's, I've gotten burned so many times. So basically my, my latest design, I ordered a bunch actually from LCSC, not from, not from digi key because there was a bunch of stuff I couldn't get. And so I bought a bunch of parts like enough to build 50, even though I only need five. So I'm part of the problem. Yeah. And, uh, and then I sent off the board because I was just like, I, the time, the time to wait that, that small amount of time is, is worth it. Uh, versus getting to the end and then being like, Oh, no, that's true.

**Chris Gammell:** Yeah.

**Phil's Lab:** How about for you?

**Chris Gammell:** Well, because I, I'm luckily enough to be sponsored by JLC. So I can use their services with the PCBs and they also have their, you know, that parts library. So in a, in a way, of course it's great because I can just use them and I know what I'm getting, but I can't like pre-order parts unless they're like a minimum quantity. So I don't want to get a thousand SM32s because I'm bankrupt. But, um, yeah. I, that's makes it hard. So I have to design really quickly. So usually I, I mean, I design fairly simple boards for the YouTube channel and that's pretty much where I use JLC PCB for. So I can do it like a day or two in advance and then just try and order it. But of course, sometimes that doesn't work out and the parts do go very quickly. Yeah. Yeah. So yeah. Yeah. I mean, I've been designing this FPGA, you know, the sidings, zinc, uh, FPGA system on chips. Yeah. Yeah. I've been designing all of that and that's where I have gone the route. Like you have like pre-ordering the parts, getting them in and then finishing design. Wow. So yeah, that's, that's kind of route I go with, with more involved projects.

**Phil's Lab:** And that's like a lot per chip too, right? That's like a hundred dollars minimum per chip as well. Exactly.

**Chris Gammell:** And they've gone up as well, the prices for that.

**Phil's Lab:** So yeah. I'm surprised everybody's not charging a thousand dollars a chip at this point.

**Chris Gammell:** Yeah. Yeah. No, exactly. So no, but that's actually quite a cool little project. I'm trying to make like a system on module for the zinc. Cause I've. For work or for fun? Just for fun, to be honest. Oh, cool.

**Phil's Lab:** Okay.

**Chris Gammell:** I wanted to make for first a flight control system based on the zinc, just, just to, to see or some sort of general controls. And then I think, okay, I could also use this for like audio processing. So instead of making a dedicated board for each, I just went the route of making a system on module that I can just plug in, you know, via board to board mezzanine connectors. Okay.

**Phil's Lab:** So you're kind of going modular at that point, right? You're, you're.

**Chris Gammell:** Exactly. Yeah.

**Phil's Lab:** Yeah.

**Chris Gammell:** Yeah. So it's been interesting to like rooting DDR memory, rooting out a BGA with like fairly fine pitch and adding peripherals. So that's quite different to the stuff you usually see on the YouTube channel. Yeah. But of course, quite a lot, quite a lot more involved than, than like STM 32 designs or something like that. Yeah. I mean, have you, have you done a lot of zinc stuff for a lot of FPGA stuff in your work?

**Phil's Lab:** A lot of my age is going to be showing here again. The last time I did anything professionally with a FPGA, it was the Vertex 4. Oh, wow. Okay. Yeah. It's been a long time. So. Okay.

**Chris Gammell:** Well, at least you didn't say like PL or PLA circuitry. Yeah.

**Phil's Lab:** No, that's more like Dave's. That's like Dave's realm. He did a lot of CPLD and PAL stuff. Okay. But he also did, to be fair, he also did a lot of other FPGA stuff after that. Okay. I feel like this is another like application level thing. I feel like audio could play well in this realm. A lot of, like anything like streaming is really good in that way. Yeah. But, you know, just the smaller stuff that I'm normally doing, it doesn't feel like that's as necessary.

**Chris Gammell:** Yeah. No.

**Phil's Lab:** How has it been on the, on the software side, like actually setting up that, the software tool chain for, for doing like an audio thing with the zinc?

**Chris Gammell:** So it's, I mean, the whole zinc thing is in general, also with FPGAs is quite a steep learning curve. So luckily the tools from Zilinx and I believe also from Intel or whatever they used to be, Altera. Altera. That's right. Yeah. I mean, luckily they're free for, for most chips they have, but it's quite a steep learning curve. Just setting up and writing your own like VHD or Verilog and then setting it up. And I haven't, I'm still yet to produce those boards. So I've done the layout and routing and the schematics. So actually doing a board bring up for something you've designed yourself rather than using, you know, like a digital board or some sort of developer board is that's to me still something that lies ahead. So that'd be interesting to see how that board bring up goes. Also like things like testing DDR, you know, writing a script that actually tests that your board layout works. And they're not exactly like cheap to produce these boards when you have goodness how many layers with impedance control and you're doing it as a hobby thing. So that'll be interesting to do.

**Phil's Lab:** How many layers of the board have to be for a zinc chip?

**Chris Gammell:** So six at least I'm doing it with eight just because, because at least from my experience is if you go over eight, it's kind of not poolable usually. And it quite increases the cost also if you want to control impedance. So eight is what I'm trying to do.

**Phil's Lab:** I didn't know. I haven't actually seen any pooled services for eight layer. I've seen two, four, six for sure.

**Chris Gammell:** So I have the, I don't know. I usually use Euro circuits otherwise for work and for, for, for, for, if I can't use like the JLC. These would be parts catalog. So they, I think have a pooled eight layer. Oh, cool. Which is fairly inexpensive, but that of course is in Europe. So for us customers, I'm not sure how.

**Phil's Lab:** It's not too bad actually. I mean, Euro circuits is, is, you know, pretty big name for going across the pond, but, but yeah, they're DFM tools too. Really, really great. I love those. Yeah. Yeah. Oh man. Yeah. So useful. Saved my butt once. Yeah.

**Chris Gammell:** No, definitely. It's, that's really, and they're really quick as well. So I'm very happy also with work with them. So, yeah. So hopefully that will come on the YouTube channel at some point, some sort of zinc based tutorials.

**Phil's Lab:** And yeah.

**Chris Gammell:** But that is.

**Phil's Lab:** I feel like that's another big shift though, too, is like, you know, so now you're like, okay, you're learning circuit design stuff. And people are like, all right, I get that. And it's like, okay, well, we're going to do, you know, processor stuff. Okay. Yeah. I get that. And now FPGA stuff is like, oh, shit. Yes. You know, it's just like a whole different paradigm of like how to think about programming. It's barely programming. I mean, it is programming, but it's, it's, it's very different that way.

**Chris Gammell:** Exactly. But I hope it's like kind of like, I'm learning with this as well. And I hope you can kind of like the take the viewers along as cheesy as it sounds, but like for the ride, you know, that I'm learning and trying to show, okay, I've moved from STM 32 to something like, you know, something like that.

**Phil's Lab:** So what, so have you done like the digital board side of things in the past?

**Chris Gammell:** Exactly. Yeah. So I've got a couple of like the, you know, the RT one, which is the Spartan.

**Phil's Lab:** Yeah.

**Chris Gammell:** I got the Zybo, which is the zinc one. And it's, of course, useful to kind of like then build up or code for those and then use some of those ideas to bring that into your own board. So luckily digital and has a lot of these reference schematics available. And then quite frankly, I am copying quite a fair bit from them just because it works. But I think as a first.

**Phil's Lab:** It's just like we talked about the beginning. It's like you copy it and you're still going to mess stuff up just because you're copying it. And you'll learn from that, you know? Yeah.

**Chris Gammell:** You root everything but one line correctly and you can throw the whole board away.

**Phil's Lab:** Yeah. Right. Now you'll be sitting there with a very tiny drill drilling out that layer three plane.

**Chris Gammell:** Yeah. Looks great. Always these spider webs of cables running around. But yeah. But no, I think that's to me, that was the way of just doing it. Just playing around with development boards. I guess that's most people's roots, I guess. Right.

**Phil's Lab:** I think so. Yeah. I think that, you know, like that same kind of like just following other people's examples and all the samples that are out there. I've been really surprised, you know, as I meet more people kind of in the firmware software realm that are like really good at stuff. The ones who like wow me with their like ability to turn around a demo really quickly or like people like hackathons back when those were a thing. Yeah. The ability to be able to replicate a demo feels like magic to me because like you have to kind of like take in all of the stuff that is, you know, tangential to maybe an idea. You then have to be able to follow directions very well. Obviously, that's its own kind of skill. But then like being able to like knowing what knobs to tweak then too. It's almost like when people are looking at DigiKey and they're like, I don't even know what to look at or what to tweak. When I look at like an API, I'm like, there's so much stuff here. You know, like it's just like and like being able to like sit, you know, have a little discomfort with it. But then like being able to be like, all right, I know how to do this. I know how to interact with an API. And like and then like which knobs to turn. You can do some really cool stuff there. And you're going to learn so many other things in the process because, you know, the tool chain might break or whatever else. So it's its own kind of skill set, I feel like.

**Chris Gammell:** No, exactly. Yeah. No. And it's and it's cool just being able to explore all these different areas and then just build up and build up. So yeah. I wonder what's next after that. But let's see. Yeah.

**Phil's Lab:** Building a spaceship or something, man. Exactly. Right. Yeah.

**Chris Gammell:** Because FPGAs always seem to be like the pinnacle. Like once you've reached FPGA level, you know, what's beyond that in the digital domain. But I just think it's pretty exciting. Just again, opens more doors. It's like moving from Arduino to SM32. And then that's the next thing.

**Phil's Lab:** So yeah, I think that's good. I think about like, you know, because FPGAs are so good at like high speed and like, you know, fast throughputs type of stuff. I always think like that's a really well targeted at like learning video or learning like high speed protocol type stuff. You know, like being able to push a lot of data around. That's where FPGAs really shine. And I feel like if you can find interesting applications there, you know, maybe you make a filter that goes into your camera because you do all these YouTube videos. Right. So.

**Chris Gammell:** Exactly. Yeah. Somewhere like that. And also kind of maybe trying to also ease the learning curve for others because it is quite steep, especially FPGA. So yeah, I hope that I can, you know, make a video or two just demonstrating like this will get you maybe started quicker. But yeah, let's see. That's the goal for this. Yeah. But let's see.

**Phil's Lab:** Yeah. I think even if people are picking up like, you know, just a thing here or there from the overall video, then that's still, it's still valuable. You know, like, like we were kind of talking about at the beginning with like, you know, so I look at a Jim Williams app note and I look at like, again, back to that thermocouple circuit. Most of that, I'm like, that's, this is not for me, but there might be, you know, one thing that's in there that even if I just learn it for that one thing and put that in my mental library, that's super useful. You know, I might run into a similar problem later and be able to refer back to it and then really dig in. And so same thing with FPGA is I feel like it's like, if you can kind of take a zoom back and say, not just here's how you do it, but here's why it's important. And that's what a lot of your videos do well is like, then, then people can, you know, come back to it as they need to.

**Chris Gammell:** Yeah. No, no, no, yeah, exactly. No, I hope that can, I can do something along those lines. It's always, I don't know. I mean, also, do you still do courses as well?

**Phil's Lab:** Well, my courses are still there, but I'm not, I'm not actively designing anything new. Yeah.

**Chris Gammell:** No, it's a thing of also coming up with, with content, I guess, for YouTube that is different or not already on YouTube. So I hope that's one thing to add, as you say.

**Phil's Lab:** Yeah, I think, you know, it doesn't even have to be that different. I think, you know, like it's, there's, I, I remember like when I started doing courses and stuff like that, I was like really worried. I was like, oh no, someone's going to do exactly the course that I'm doing. And then I was like, yeah, but actually that would be great because then there would be different ways to see the same thing as well. You know, like, and I was thinking about it because it was like, I was going to invest all this time and then, you know, no one was going to be interested, but people are going to be interested because of the way I do my stuff or the way you do your stuff. And like, people are invested in, in you. So I feel like that is also. That's a good point. Yeah. They're coming towards, you know, like I'm sure that many people that are signing up for your course, hopefully some people here listening are interested and I would recommend it. That'd be very nice. But, uh, I'm sure a lot of them are going to be people that are already familiar with your videos and like your style.

**Chris Gammell:** Yeah, no, no, that is a good point. Yeah. And even if it's just something, as you say, it's a small thing you pick up, I guess that's, that's, that's all even worth quite a bit. It doesn't have to be the whole, I mean, I guess a lot of people will be familiar with most of the content in the course, at least if they're signing up for it. But if you can just pick up one or two things that will improve your designs in the future, then I hope that's worth it. Yeah.

**Phil's Lab:** Yeah. Yeah. I think watching, watching other people design, you know, it's like, uh, what's a good example. I mean, like watching other people paint, right. Is you can learn stuff from their technique and you might watch the whole painting, but only take one thing out of it, but it's still a worth worthwhile thing.

**Chris Gammell:** Yeah, no, exactly.

**Phil's Lab:** So let's talk a little bit more about the course to close this out. I mean, so, so we kind of talked through some of the, uh, the various sections there, but was there anything there that like you think is something that is in every design that people should be like focused on? Like, uh, pull up resistors or ESD protection. That's using one example there.

**Chris Gammell:** Yes. No, I mean, on the point of ESD protection, I think that is also something I get asked a lot about. And there's actually quite a lot of detail to choosing the right ESD protection, you know, depending on what bus speeds or signal speeds you're using, uh, what frequencies you're interested in or what voltages you're running at. So that is listed in the course as well. I can't go into, or don't go into much detail given the time of the course, but these small things that oftentimes in the YouTube videos, or because maybe even ESD protection is integrated into, uh, certain chips that SM32 might have internal ESD protection. But of course, ESD protection should be placed, for example, close to a connector. It should be rated appropriate to what voltages you'll be working with. Small tips like that, that you maybe not usually find in maybe the YouTube videos I'm doing. So it goes into more and more detail rather than, okay, here's a chip, here's some pull up resistors. It's kind of the whole process you need to think about when you are designing a product, even if it's just a prototype. Yeah. So yeah, it's just hopefully just little tidbits, kind of a whole span. It's fairly broad. And, you know, even with like ESD protection or EMI filtering, you could make a whole course just about that. Totally. Yeah. So it's almost like presenting you with these ideas and showing you how you can maybe develop them further. So I give like references and links and other videos to help you out or set you on your path, what you might need. So as long as you know something exists, I guess you can always track it down and further.

**Phil's Lab:** Yep. Yeah. We actually mentioned that on the show last week. I had my friend Charlie, who's an educator on, and the what to Google for problem, right? And it's basically you're giving people a list of what to think about. It's almost like a checklist of things to think through. And then once you do that, it's like, all right, I want to know a ton about ESD. Well, this isn't where you learn that. You learn that on, you know, someone else's site.

**Chris Gammell:** Yeah. And that's exactly it. Like starting the spark or whatever you call it, right? Just showing people this is what you probably will need. Here's the basics of choosing it if you want any more details out there. But this is just like rules of thumb. I had one actually good, very good university lecturer. He was the only one who actually taught proper circuit design. And especially also in analog electronics, when you're just designing circuitry that's supposed to work, not very precise circuitry. It's all about like rules of thumb. And I kind of like that approach that you get given certain rough guidelines. And if you want, you can dive deeper. Yeah. So that's...

**Phil's Lab:** If I think back to like my time with the Keith Lee analog engineers, that was a lot of what I... You know, like we'd be sitting around a whiteboard. And I remember Matt, one of the guys that was older than me, not too much older, but had been there a while and definitely knew his stuff. And he'd always talk about these mantras, you know, just like, all right, we're talking through a circuit. And we're like, all right, and we know that V equals LDI DT. And so because of that, when this inductor gets cut off over here, we're going to see a voltage spike. And it was just like ways that he would talk through circuits. And these, you know, that's not really... That is an actual law, not a law, but like that is an equation around guiding voltages and stuff with inductors. But like having that as a mental model then to then build out the rest of your knowledge around the circuit is super, super useful. And I feel like the experience is just kind of like knowing where to apply that and how it's relevant to a circuit.

**Chris Gammell:** Yes. No, exactly. Yeah. And yeah, with the course, I hope that'll help some people out just to set them on the right path.

**Phil's Lab:** I think you will be that guiding voice. Yeah. I think that's the idea. Yes. Yeah.

**Chris Gammell:** No, I do. I do very much hope so. And of course, as always, any positive or negative feedback helps me out as much as it does people who, you know, sign up for the course. Because I'm always still learning as well. I guess everyone is.

**Phil's Lab:** Yeah. Yeah. Yeah. That's great. I think having those pointers to where to dive in deeper. Yeah. And like, and just follow along and see what you're doing. And hopefully, yeah, I mean, is the idea that people should be following the course exactly and have the same output as what you're creating?

**Chris Gammell:** Close to. I mean, ideally, I give, I give the schematic files. I give the parts libraries, but I don't give the final board layout and board routing. That's what I designed. Because that to me is the part which makes the most sense to do yourself for every student to do themselves just to go through the motions. Where do I put my VAs? What traces do I use? Just watching will not teach you anything. I think like I've always just learned the best by actually implementing what I've been taught. Yeah. So to me, that made the most sense not to include those files because it's easy to say, yeah, he did it. I'm sure I can do it myself rather than having to do it yourself.

**Phil's Lab:** Yeah. Yeah. Yeah. One thing I used to do with contextual electronics is I would give them like a commit number. So I'd be like doing commits throughout the process. Each video would end with a, you know, I'd commit the code to GitHub. And so it's like, okay, so if you want to practice this specifically, go to the commit before or go to the commit after, delete all this stuff, and then start over from that same spot. And you just have like a, like a part placement kind of thing. And then your parts are already placed. You just do the layout. That's the thing. Yeah.

**Chris Gammell:** No, I think that's, yeah, the great way, a really great way of learning. Actually, you have to do it to be able to learn this kind of stuff. So.

**Phil's Lab:** Yeah. Yeah. Even though I'm not a gym goer, that is the equivalent of getting your reps in, I believe. Exactly. There we go.

**Chris Gammell:** Only practice will, yeah.

**Phil's Lab:** Practice makes perfect. Is that what we're going towards? I think so. Isn't that the usual saying?

**Chris Gammell:** Yeah.

**Phil's Lab:** I'd say it, practice makes better. Yes. No perfect, no perfect involved.

**Chris Gammell:** The limit tends to being perfect, but never gets right. Yeah.

**Phil's Lab:** Right, right, right. It's a, it's a infinite series. Yes. There we go. Yeah. Cool. Philip, where can people find you, your course, your YouTube channel? How do people find you online?

**Chris Gammell:** Yeah. So if you just Google Phil's lab or type Phil's lab into YouTube, it should hopefully be the first thing that pops up. And I also have videos on that channel to anything about hardware design and electronics, signal processing. You'll also find links to the course. If you want to go to the course, you can do, go to phils-lab.net forward slash courses. And that will show you all the course content, what you need to know, and also a link of where you can sign up. So that should get people going.

**Phil's Lab:** We'll have some links on here as well. And yeah, I highly recommend checking out Philip's videos. And this course is a great next step to really dive in deeper. I think people could really benefit from that sort of thing.

**Chris Gammell:** Yes. Well, thank you so much for having me on.

**Phil's Lab:** Yeah. Thanks for joining me. It's been great. It's been great to catch up with you and talk through education and electronics. I look forward to future videos and seeing what you do next.

**Chris Gammell:** It's been great to talk to you. So thank you so much.

**Phil's Lab:** Bye-bye.

**Speaker ?:** We'll see you next time.
