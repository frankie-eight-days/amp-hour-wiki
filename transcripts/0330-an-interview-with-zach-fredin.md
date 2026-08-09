---
episode: 330
title: An Interview with Zach Fredin
url: https://theamphour.com/330-an-interview-with-zach-fredin/
---

**Zach Fredin:** This is The Amp Hour Podcast. Recorded January 4th, 2017. Episode 330. An interview with Zach Fridin.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Zach Fredin:** And I'm Zach Fridin of Neurotinker.

**Chris Gammell:** Welcome, Zach, my old friend. How are you doing? I'm doing all right, Chris. How about yourself? I'm good. I'm good. Thanks for being on the show. Dave's obviously out this week. Sorry he can't be here. But I'm glad to talk to you because, well, I've known you for, what, 10 years now? Pushing 10 years? Maybe a little bit less.

**Dave Jones:** 2004, I think. 2004. 2003. Fall of 2003. Yep.

**Zach Fredin:** Wow.

**Chris Gammell:** Yeah.

**Zach Fredin:** Yeah. It's been a while. We went to school together. Oh, yes. We should say that.

**Chris Gammell:** Yes. So me and Zach have known each other. And I have watched with glee as Zach and my worlds have kind of collided. You actually didn't start in the electronics world. But then you are now, well, you're just a superstar around here. And people might not know that you're doing this stuff, though. So that's why I wanted to have you on. And I think you're doing some really interesting things. So why don't you tell me a little bit about where you come from and where you're going?

**Zach Fredin:** I appreciate that. Thanks. Well, my background isn't formally in electronics. I was kind of more of a hobbyist growing up. But I mentioned this to you earlier. I studied metallurgy when I was in college because I learned how to solder when I was younger. And we studied phase diagrams and learned about eutectics and all that. And I thought it was very interesting. So I got back into electronics with this Neurotinker project. So that all started a few. Do you want kind of the whole story? Like do you want me to give you the history of where we come from and all that five minutes sort of deal?

**Chris Gammell:** Sure. Yeah, do it.

**Zach Fredin:** Okay.

**Chris Gammell:** Makes it easier on me, man.

**Zach Fredin:** Yeah, yeah. So go back three years. My wife's an architect. We live in Minneapolis. And we were having brunch with a bunch of our architecture friends. And a guy named Andrew Salveson came to brunch. He was another architect. And he had done a project for his final project for school, for grad school, where he wrote a plug-in for SketchUp in Ruby that would essentially make a bunch of boxes in SketchUp. So SketchUp is like Google's soft modeling program.

**Chris Gammell:** Formerly Google's. Now Trimble. Yes.

**Zach Fredin:** Okay. Yeah, there you go. They sold it out. Sorry. Really? Didn't know that. Okay. Okay. Well, anyway, so he was interested in neuroscience. He was interested in how he could connect that in with design work. So he wrote a program that basically instantiate an arbitrary number of boxes in SketchUp that you can then connect into networks. And then each one of those boxes would behave like a biological neuron. So you could send signals through this network. And then the output of that network would be used to define various dimensions in the model that's kind of kept off screen. So he used it to make neuro-derived architecture essentially as kind of an exploration. So it's very abstract and very interesting. And he was kind of telling me about this at brunch. And I was like, what's a neuron? So it turns out neurons are – we have 86 billion of them in our brain and they're little processing cells. Yeah, that's it. Just 86 billion, give or take a couple billion or whatever. And they're basically just threshold detectors. So you have like an internal membrane potential and that membrane potential is affected by external stimulus. And once that membrane potential exceeds a threshold, it fires what's called an action potential and sends signals downstream. And what's important is that if you don't exceed that potential, the neuron doesn't fire. It doesn't fire until you actually get above that threshold. And there's all sorts of ways that inputs are weighted and the whole membrane potential concept is based on sodium and potassium channels and ionic concentrations. And it's fairly complex, but you can kind of distill it all back into this basic idea of threshold detection. So he thought that was really interesting. He built this model in SketchUp that would have these little boxes changing colors to represent the internal membrane potential of each box as if it were a neuron. And I was like, oh, that's really interesting. And he was like, yeah, and I want to make it, you know, like I want to make it into a physical thing. Like I want to make Legos for neuroscience. Like, yeah, that sounds really neat. And like, you know, be able to connect them together in a modular way and just kind of see how information propagates through the network. So me and Andrew kind of like started on this without really an intention of bringing it into the educational world. It was more just an exploration. But because we were doing it on nights and weekends using our own money, we wanted to make it really cheap. So, you know, kind of came up with some basic requirements, how many inputs, how many outputs, how we do indication, distilled that down to the cheapest microcontroller we could find, which ended up being an ATtiny44A and spun up about, I think, 120 boards. So that was in that would have been in the spring of 2014. So we spun up 120 boards and then reflowed them in a toaster and kind of did that whole deal. And then me and my wife and him and his girlfriend got a crimper and some wire strippers and like made this little assembly line in our dining room and like assembled all these axons, you know, or, you know, all these connector cables that would allow you to form the network. Then somehow figured out how to get all the programming to work. It was all very neat. It was all very like blinky and kind of abstract and you could you could take 20 of these boards and you could build a network that you could then inject signals into and they would do it would do unpredictable things. So each processor is very simple, but they're also, you know, completely asynchronous. And they're all, you know, everything operated on timer interrupts or I'm sorry, pin change interrupts. So it was all like very responsive. And each one of the boards used the internal RC oscillator of the chip. So each one was a little bit different. So you had all these things that would make the network behave in strange ways. And you could you could like.

**Chris Gammell:** Does the RC thing actually replicate? I mean, is that I guess neurons wouldn't be synchronous either, right?

**Zach Fredin:** Yeah, they wouldn't. They would have, you know, they would have different time constants. The more important thing is they have different weightings. So the weightings of the inputs are what really change. So when you're when you're learning things, you have new neural connections that are being formed. And then you also have the relative weightings of different connections that are kind of changing constantly as you as you learn as you learn new things. That's what we wanted to emulate. Right. And then we kind of backburned the project a little bit. Andrew ended up moving to New York City and joined a fancy architecture firm out there. And I worked on some other projects. But I ended up publishing all the all the documentation online. We open sourced the whole thing and put it on put it online on Hackaday. And I got an email would have been two years ago from a neuroscientist at Boston College. So he was a neuroscience professor. And he told me that he was basically working on the same thing as a teaching tool. But he was like what he said, you know, 10 years behind where we were. He was using Arduino boards and like trying to get a single one to work. And we had made 120 of them. And this is super cool. I want to use it in my classroom. This is great. You should, you know, we should start a company and we should make this a thing. Which was crazy.

**Chris Gammell:** Okay.

**Zach Fredin:** Yeah. I mean, so just for context, I was at the time I was a sales engineer. I sold process instrumentation and control valves. So like you have a grain silo in rural South Dakota and you want to know how many beans you have in it. Like you put one of our radar transmitters on top of it and it sends a 4 to 20 milliamp signal back to your PLC. And you have a little display and all that.

**Chris Gammell:** Which is pretty cool too. But yeah. It's pretty cool. Not quite neurons on a, you know, board you made yourself, right?

**Zach Fredin:** So our radar transmitters were pretty awesome. They are. What, what, Chris, what frequency do you think they operated at?

**Chris Gammell:** For radar? For radar. 28 gigahertz. 72 gigahertz. 72 gigahertz. Yeah. I should have guessed that because that's what, what's his name? Charvat does and Tony does. All the, a bunch of the radar, all the radar weirdos who have been on the show in the past. They all do that stuff. That's awesome. Didn't know that. Yeah. Tony Long, he does, he does that stuff for fun. He's a, that, well, that's great though, right? You've already got, you've got a story right here about something you're doing for fun that turned into something crazy. So.

**Zach Fredin:** Yeah. But doing radar stuff. God bless y'all. That is awesome. Yeah.

**Chris Gammell:** Yeah. No, it's, it's really cool.

**Zach Fredin:** Anyways, go ahead. Sorry. Yeah. No, no, no worries. No worries. I could, I could talk about process instrumentation for too long. So we should get back to this, I suppose. Where, where was I?

**Chris Gammell:** So you were doing that though. You're saying that it was so far removed from.

**Zach Fredin:** So far removed from what I was doing. Yeah. So I got this email and I remember reading the email and looking at my wife and saying like, holy crap, this is crazy. That is weird.

**Chris Gammell:** Yeah. No, I, I talked to people about, so I talked to people at Hackaday about that stuff too. And I think that that's really great. Like that is a success story, I think. And I'm not sure how many times that's happened or how common that kind of thing is. Honestly, I greet those emails with skepticism normally. So the fact that you didn't is, well, maybe you did. I mean, what was that like at the beginning?

**Zach Fredin:** So, so what happened actually, I think the thing that really closed the loop is that I Googled his name. His name's Joe Berto. He's, and he's now my, now my business partner. I Googled Joe Berto's name. And when the Google search results came back, the first listing was his Boston College bio. That can be faked. No, no. So the link was, the link was purple because when Andrew and I a year ago had been thinking about trying to like see who else was in the world of neuroscience generally, like we happen to have been like just searching for neuroscience professors to talk to. That's great. And his name popped up and like, I didn't clear my browser history for a year. So the link was still purple. I was like, why is that link purple? And I clicked his name and recognized the picture. I was like, all right, this is weird. That's great. That was really good. It was interesting enough that I, that I flew out to Boston and met, and met with the guy. Help that I have, I have a friend that Boston Dynamics. So I was able to like squeeze in a visit to Boston Dynamics and play with robots for a while.

**Chris Gammell:** I know that guy too. Yeah, you do. Yeah. I got to meet those same robots and that for people who don't know, if you know someone there and get there as fast, like, I don't know, I don't know if it was special that we got a tour, but man, that was.

**Zach Fredin:** Yeah. We went on like, we went on like a, on a Sunday and we were just able to spend a couple hours and. Did you ride one of them? No. I didn't ride. I didn't ride one of them. I got to get pretty. On a Sunday. I'm not sure. Yeah. Yeah. Didn't get to see any of them run. I heard that was back. That was back before the latest iteration, back when they were like really, really loud. Cause they all had to have these like onboard power systems, you know, that were like gas powered hydraulic motors and all that. Right. Right. Um, so I didn't get to see him run, but it was, it was still neat. Anyway. So went to Boston dynamics and then the next day went to Boston college, met with Joe Burrow. Um, and we like sat in a conference room for like four hours. Um, and we drew this big Venn diagram on the board that was just like two giant circles that like barely intersected on one side. It was like, Zach tinkers with electronics, knows how to solder, like already built a bunch of stuff. Joe actual legitimacy in the world of neuroscience, like has been in the classroom before. He knows what he's talking about. Yeah.

**Chris Gammell:** Let me just say up front, you sounded like you knew exactly what you were talking about when you were explaining neurons before. So that's pretty good. Yeah.

**Zach Fredin:** Everything I know about this project is what I've learned because I had to, to like make neurons simulations accurate. It turns out when you're like, when you need to make an accurate simulation of something, like you have to learn a lot about it. Uh, yeah. So that's, I don't know.

**Chris Gammell:** It's called fake it till you make it, I think. Right?

**Zach Fredin:** Exactly. I've been doing that my whole life. Exactly. Um, but yeah, so we had, we made this, uh, this Venn diagram and like had this very narrow intersection where it was like neuro tinker. No, I don't know if we come up with the name then or maybe a little bit later, but, um, and the neuro is obviously Joe and the tinker is obviously Zach, you know, so we kind of came up with it that way. Um, but then, um, so that was like February of 2015 and we, um, you know, we're like, all right, we both have to have full-time jobs and we have mortgages and things. So like, that's what do we do? Um, so he had, he, he was familiar with the SBIR program, a small business innovation research program, which, uh, for folks that don't know is a grant program that's funded by the small business administration, uh, in the U S and it's designed to, um, stimulate the creation of small businesses that are focused on very high risk, high reward technologies. Um, and what's interesting about it is that they devote $20 billion a year to this and they don't really tell anybody much about it. So it's pretty close to the amount of like seed funding that's available, you know, from angel investors and all that. I mean, it's kind of in the same order of magnitude only, um, you don't have to pay grants back. Like you have, you have to tell them how you're spending the money and you have to like, you know, you're legally obligated to do so, but like, it's not an investment. It's a, it's a grant. Um, so he was familiar with that program. Um, and then the, the, the SBIR then filters down through different agencies. So we, we applied for a, we, we basically like went on a couple agency websites. So first the National Institutes of Health, um, we found a grant proposal for, um, like a STEM education gaming thing. So we, um, applied for that one. Didn't get it. Um, and then the.

**Chris Gammell:** Well, and that's an interesting point too, because I, I, I, I remember when I first heard about SBIRs, I was interested that they weren't open-ended. I was always like, oh, well, why wouldn't they just fund research that people propose? But it's, it's that basically the, like you said, the, the institution, like the, um, what was the one that you first applied to? IH, National, National Institutes of Health. Right. So like they have, they have someone internally who's like, you know what would be really great? And then they, and then they put that out there, right? That's exactly right. Yeah.

**Zach Fredin:** They have a, they have a, they have a series of prompts. They have like a series of RFQs essentially that they put out that lasts for a couple of years. And it's like every May, like May 15th is the NIH deadline for the SBIRs. And it's like, you have 20 different categories and your thing needs to fit that category. So that, that one was called the, the official prompt was serious STEM games. So it was like, you know, science, technology, engineering, and math games like brought to the classroom. Um, so it was, it was, it was a neat idea. We actually, uh, we were able to partner with the guys at MIT game lab to like write, write our proposal. And like, I think we had a pretty strong idea, but, um, I don't think we had really thought through the gamification that well. I think we had just been like, Oh my God, this is a grant thing we could do. And like, Hey buddy, it is a game. Of course it's a game. Yeah. Like Legos are a game. Um, so then, so then we, um, you know, we kept looking, we actually didn't hear back on that one. We, uh, we, until after the deadline for the next one we were looking at, which was, um, through the national science foundation. And they had, they had a, um, a grant called, um, educational applications. So it was just like a general educational science grant program, you know, for like, for novel, novel technology concepts for education. Um, so we applied, we applied for that one too. And we ended up getting it. Um, which was crazy. It was like, we, we applied in June and then we didn't hear anything for four months. And then we got an email in September that was like, Hey, we need you to answer these 10 questions. We got the email Friday at like six o'clock in the evening central time. And they were like, we need you to answer these 10 questions by Monday morning. Um, like literally it was like, they were like, you know, this, these would be like the essay questions, you know, when you're in high school and you're like, all right, you like, you can't just fill this in. You need to like write two paragraphs about it.

**Chris Gammell:** Right. You need to spend all weekend. Yeah.

**Zach Fredin:** And it was, what was really interesting is like the, the, the NSF is all about, you know, with, with the SBIR, they're, they're trying to commercialize technology. Like they don't want you to just, you know, be, be fed by the government for the rest of your life. It's like, no, we're trying to kick you guys out of here. We've got grad students for that kind of thing. Yeah, yeah, exactly. So, so, so the grant director wrote us this email that was just like, look, you know, you guys need to dig more into how this is commercially viable and you need to tell me what my return, like how I get my return. And we were like, what do you, what do you mean? He's like, you know, like my ROI. Do you, do you want to kick back? It's kind of. Yeah, exactly. It's like, no, like they consider their ROI to be the tax revenue they get from my employees 10 years down the road. They're like, that's, that's how you need to quantify it. Which I mean, like anytime you do like a pitch competition and you talk to investors, like you always put together these growth, this growth plan with revenue and all that other stuff. And so it's kind of the same.

**Chris Gammell:** Yeah, but that's usually a direct thing for, for investors. They want their specific money back.

**Zach Fredin:** Yeah, they want to figure out how they can, you know, kick you to the curb and leave in five years with all their money as opposed to like forming a sustainable, profitable business. Well, I'm sure if Abidon's listening. I'm a little snickle. Oh, inappropriate.

**Chris Gammell:** No, that's, I think Abidon hopefully was different. No, no, yeah, totally different. Yeah, no, I, you know, I've seen stories too. So yeah, it's not, it's not, it's a different model that you're saying in general. It is, it is.

**Zach Fredin:** They're, they're, they're really interested in, and the other thing is that they're interested in stuff that isn't really fundable any other ways. I mean, we, we were like, we want to create electronic neuron simulators for teaching people about neuroscience. And like, we talked to a couple of investors about that, you know, angel investor types that would be the folks that would be looking at funding things at a couple hundred thousand dollars for six months to see whether or not it's feasible. And they were just like, interesting. Well, let me know how, let me know how that goes. Like, oh, great. You should go on Shark Tank. Shark Tank. Yeah, perfect. The sharks would just love talking about neuron simulators. Yeah. Yeah. So that was cool. So anyway, so anyways, yeah, September, we, we started hearing answers and then like went back and forth a couple of times. And then, um, was it like November or December 20th, we got our formal award letter. Um, and our grant start date was January 1st. So we like quit our jobs and went full time. And that was, that was January 1st of this past year. Um, and the grant.

**Chris Gammell:** So I, I don't, I don't think this is, is this normal? I mean, like, is, did it, did it having a professor? Uh, did, had he ever done that before? Is this, is having his like pedigree important?

**Zach Fredin:** So he had, he had applied to one previously and he was not successful with it. But generally, um, like when people ask me that, I'm like, no, I, like, I don't have a PhD. I, I'm not an electrical engineer. I just built something that people liked and supported.

**Chris Gammell:** No, no, no, I'm not talking to that. I'm, I'm actually talking about the people that are in the audience listening right now who are grad students or PhD students and they filed 300 applications for funding and nothing came back. I mean, you did two.

**Zach Fredin:** So talk, talk about like the, talk about how to get these grants. So the SBIR that we applied to has an acceptance rate for that, for that class. It was like around 12%, um, 12, 13%, something like that.

**Chris Gammell:** That's not bad. It's not.

**Zach Fredin:** It's really not. And like, that was actually on the low end there. The, the previous class I think was more like 17, 16, 17%. Um, so the things that you need, the, the grant has like a, there's like a window of time you could submit your application between like mid May and mid June. And before mid May, you need to write an email to the grant director. It's like one guy or one, one man or one woman, like sitting in some office in Bethesda, who is the grant director for that program. And like, write them an email and tell them what your idea is. And they will get back to you within 45 minutes because that's their job. And they will set up a conference call and you will talk to them for half an hour about your idea. And they'll be like, yeah, you should apply for the grant. Or they'll be like, no, you shouldn't apply for the grant. Like, that's not a good fit for my program. Like they'll just tell you whether or not it's a good fit.

**Chris Gammell:** Um, but it doesn't, it doesn't say that on the application.

**Zach Fredin:** So you're saying that this is a, if you read through like the NSS recommendations for how to apply for the grant, it says, email your grant director. Here's his email address, but make sure you email him before he starts to get all these applications in so he actually has a chance to talk. Like that's, they make themselves completely available, but like a lot of people just throw an application out there and don't have the conversation. Um, so we, right.

**Chris Gammell:** So this is, this is like a professor office hours kind of thing where it's like, Hey, I was here the whole time. You're the one who didn't come in until two hours before the test, right?

**Zach Fredin:** That's literally exactly what it is. Um, so, so email the grant director, let them know what you, you know, and get on the conference call with him. Um, and then the other one is, um, letters of support are incredibly important. So they, they're like really limited. You can only, you can only submit three letters of support per, you know, for the phase one grant. And like, you should have a letter of support from someone that says, this is an excellent idea. And if it's successful, I want to buy this many of them. And I represent this percentage or like this size audience. Um, and you need like a, you know, so you get a letter from a potential customer. You get, you get a letter from like, you know, in our case, someone who thinks it's technically feasible to do it. Um, like, yes, this is, this is, uh, you know, I have been in neuroscience for a long time and I could see this, you know, being possible to simulate. Like, so, so like you have to build, you build this credibility and based on the people you get your recommendations from. So like one of them, one of them we got was a neuroscience professor. And, you know, one of them we got was, uh, like a, I don't know if it was a super intent, a superintendent. I always say super. Yeah. Like the ed tech world and I meet a superintendent. It's really, it's really bad.

**Chris Gammell:** Have you, have you said that to someone who's actually a superintendent?

**Zach Fredin:** You're like, you're like, almost like, cause I, cause before I meet them, I'm always thinking about that line. I'm like super Nintendo. Don't say super Nintendo. So it's, it's going to happen at some point. I just, I just know. Oh my God.

**Chris Gammell:** Oh, you gotta, you gotta start filming all your meetings or something.

**Zach Fredin:** Make sure it's a, make sure it's like a small district or something. Um, so yeah, so letter, letters of support. And then like just making sure that you dot your I's and cross your T's on like what the application wants. There's like the, there's like a two page checklist. That's your application is 60 pages long and there's a two page checklist. That's like, make sure you have this, this, this, this, this, this, and this. Make sure it's not over the page limit. Make sure, you know, just like, make sure you follow all their, your bureaucratic requirements. I mean, RTFM is what you're saying? Yeah, exactly. Um, cause I think a lot, a lot, uh, fail because they, they don't get that. And if you, if you pass a scientific merit review, um, or you're like in the top half of the re of the respondents, like if they convene their committee and they, they're like, Hey, this is not absolute garbage. Uh, I shouldn't say that. Um, you're saying that 90% is showing up, right?

**Dave Jones:** Yeah. 90% is showing up, showing up with like a finished application.

**Zach Fredin:** You can't see this with the microphone, but my head's in my hands because I think I just, I didn't mean to insult anybody by saying that. What I mean is that.

**Chris Gammell:** No, no, no. I mean, so what I heard is that you say, you're saying that some people just chuck it out there because they're chucking it out to everyone, right? Just, they're just spraying and praying. Exactly. With grants. And so I, I don't think that you said something bad there. Okay. Okay. If you did, they're, they're idiots anyway.

**Zach Fredin:** Yeah. Well, and the point is if you're, um, if your application is halfway decent, you will hear something back. You'll, they'll, they'll tell you why they rejected you and then you apply again six months down the road.

**Chris Gammell:** See, now that's really nice. I mean, I wouldn't expect that at all.

**Zach Fredin:** It's awesome. Yeah. Yeah. Yeah, totally. Um, and it, and it's, and it's a pretty broad ranging program. I mean, they, it's small business administration and they define a small business as any company that has less than 500 employees. Um, so yes, it's not, it's not only startups. There's also large companies that like, well, what I, what I would consider a large company, you know, with 480 people where they have like two guys that are like, Hey, we want to do this in a year. So let's submit an application for it. And they're able to do that. Yeah.

**Chris Gammell:** Um, oh, and it gets crazy too. I mean, I, I remember the first conference I ever went to. Um, I, I was watching this talk and it was this guy talking about like a wireless sensor was measuring acceleration, but it was mounted on a frigging like Apache helicopters rotors or something crazy like that. And he was in, but he was in stage three. And so he was getting like millions of funding, you know, like, and because it was a military project too, obviously there's high costs there. But I mean, like that's, that's, that was my first, I'd never heard of that before. And I was just like, my jaw was on the floor. Like, holy crap, you can, there's a lot of funding out there. Yeah.

**Zach Fredin:** And a lot of the, yeah, I should say that essentially every other category of grants, um, within the, so we went to this, this NSF conference where they convened all the people in our SBIR cohort for phase one. It was like 200 companies. Um, and of those, like 20 of them are educational applications. Uh, and we were definitely like the bottom 20 in, in terms of like, this is a bad-ass thing that you're building. It's like, oh, we're building this app to like do blah, blah, blah. Or we're building electronic neuron simulators. And then there's like the opto electronics group that are like, yeah, we're building like optical phased arrays. Do blah, blah, blah, blah. We're replacing eyeballs.

**Chris Gammell:** Oh, oh, cool. Oh my God. Yeah.

**Zach Fredin:** You like, you sit down at this conference, you're like, so what are you guys working on? And it's like, wow. Just, you hear amazing stories about this stuff. Um, then you, then of course you're like, yeah, I'm doing laser stuff and surgery stuff or whatever. Is that invite only? How did you, how did you get to that? Yeah. It's like their, it's like their phase one bootcamp. So it's only owners of the companies that got phase one grants.

**Chris Gammell:** Um, okay. Cause I, I mean, that sounds like that would be like just to, to hear the ideas kind of stuff. That would be great. Are you guys listed somewhere online that maybe the other people are too? Cause I would just be curious.

**Zach Fredin:** Anybody that gets an NSF grant, anybody that gets any of these grants, it's publicly listed. Um, there's like, there's some maybe not great website run by the official government that does it, but there's also a lot of people that scrape those websites and put it into a much more searchable format. And I know this because like, as soon as we got the grant, we started getting all of these like snail mail. Spam. Yeah. So, oh my God. There's so much man like, oh, NeuroTanker, we do this. Oh, we want to help you. Um, right. So yeah. Right. Like when you buy a house too, where it's like, do you need moving help?

**Chris Gammell:** Do you need landscaping? Yeah. Oh my God. So we, some, you're listed somewhere.

**Zach Fredin:** So we got a, the best, the best one was we got a, we got a trademark on our logo. Um, both the name, the name NeuroTanker and the name NeuroBytes, but also we got a, we got a trademark for the graphic design of our logo. Um, and we started like two months after it actually went out in the USPTO Gazette. Um, I started, I started getting these like, you know, snail mail notes from like all over the, all over the world that, that would have like a really poorly cut out photocopy of my logo, like pasted onto this letter that was like, we want to help you get trademark protection in like Uganda or whatever.

**Chris Gammell:** Oh man. Enterprising individuals. Let's just call them that. Right. That is, that is nice. It was interesting. Yeah. So lesson learned. I was always surprised that the, I got, I've got a design patent and thank God I moved. But, um, at my old address, at least I, uh, uh, I was surprised there was never spam from that. I always figured there would be, you know, like, like why wouldn't recruiters look that stuff up and be like, oh, engineer. Totally. You know, I'm surprised.

**Zach Fredin:** Yeah. I'm surprised you didn't either. That's, that's interesting. Cause I get, it's calmed down a little bit, but I think, I think whenever the Gazette, cause they had, they like published this USPTO Gazette that has like all the new trademarks and I assume all the new patents in it. And it's like, it's got the mailing addresses, like it's all public information. Oh yeah. Yep. That's why you get PO boxes. Yeah. Lesson learned on that one. Man, big mistake, Zach.

**Chris Gammell:** Yeah. Um, so, okay. So, uh, so that's, so you guys got a stage one. That's great. Congratulations. Um, and I remember when you taught, you were talking about it at Facebook, uh, and you were just like, Hey, I'm quitting my job. That's new. That's different. Yeah. Um, but so what, what comes after this? So, I mean, stage two, stage three, is that, are you guys like, what's the requirements for that?

**Zach Fredin:** So we, um, so we, we finished our grant, you know, we finished up at the end of June. Um, and you basically like, you get this chunk of money and you have to spend all but 7% of it by then you get 7% that goes towards the capitalization of the company, um, that you can kind of use, use towards whatever. Um, and we, um, what we, what we learned talking to people was they're like, you want to keep every penny of that if you can, because if you want to, if you want a stage two grant, like they're going to give you, they're going to put you through this audit to basically say, if you're like, see if you're financially solvent enough to support a larger grant, because you need to have enough money to get the credit and like just support every, you know, all the administrative stuff. Um, so we really didn't want to spend any of that, but what we were able to do is, um, do a pilot run. Um, we were able to fund a pilot run and sell a handful of kits into a few different, um, a few different classrooms, which is pretty cool. Um, so we now have a user base of like, I don't know, 20, 20 classrooms between high school and college that are, that have the latest neuro neurobytes kits. Um, so that's what we've been doing for the last, a lot of the last couple of months is like following up with those people and seeing what their experiences are and working with them to build curriculum and so on and so forth. Um, and we're like in the very final stages of our last audit to get our phase two grant, which is really, which is really exciting. Um, so I, I really wanted to come on the show and be like, yeah, we're going to get our phase two grant. And we got our, we passed our merit review like two months ago and we, um, you know, we're, we're going through the audit essentially right now. And like any day we're expecting to hear something positive back. Um, and our, and our plan with that is to really, that's going to get us through the rest of development and through commercialization.

**Chris Gammell:** Okay. And so, uh, the plan is always to take people to a stage one, stage two, stage three, as well. I, I don't really know this stuff.

**Zach Fredin:** Yeah. So, um, at least, at least for this program, this program doesn't have a stage three, um, NSF just does stage one and stage two. But when, when you apply for stage one, they, they review your application as if you're going to apply for stage two as well. Um, it's kind of expected that like, you know, in our case, like, well, we got to the end of, a lot of people get to the end of stage one and like, they, they still are working on their MVP. And we're like, we got to the end of stage one and we're like, we just finished our 10th prototype iteration. We made 500 of these things and we sold them to like a bunch of classrooms. So like, we were pretty far ahead of the game.

**Chris Gammell:** Um, but basically if you, and then they're like, Zach, come on, man, we're making eyeballs.

**Zach Fredin:** Yeah. We're doing cooler stuff than you. We're, our, our stuff isn't just like a little circuit board. No, your stuff's really cool.

**Chris Gammell:** Actually, we will need to link in videos and stuff of, of yours working as well. Okay. That is definitely a, we'll have to do that at some point.

**Zach Fredin:** I will find some good videos. Hopefully we have those.

**Chris Gammell:** Um, yeah. So, uh, can you tell us the relative amounts if you don't mind? I don't know if it's.

**Zach Fredin:** No problem. It's all, it's all public to our phase. Our phase one grant was $150,000. Um, and the phase two grant is $750,000. Um, so it's over two years. Um, and for us, our phase two grant supports, um, myself and my partner and, um, renting space and doing a whole lot of prototyping. Um, and we're also funding a series of curriculum development workshops this coming summer and, like, hiring an intern and, um, working with a number of different contractors. And, um, so there's a, there's a, when you, when you put the grant application together, you basically like have to lay out a, an array of buckets and you're like, this is the relative size of these buckets and this is how full I need each one to be. And like, this is what I'm going to spend them all on. And then if you screw that up in like three years, two years, you're like, oh my God, I needed more in this bucket. You have to like submit 10 pages of paperwork, but it is possible. I mean, as long as the money's allocated, you're able to have some flexibility. Um, they really emphasize it. Like we are the government and we do run slow and we are bureaucratic and all that. But like, we also understand that your startup and like, you may need to like, they use the word pivot, like at, at our workshop, they're like, you may need to pivot. I'm like, do you know how much paperwork that probably is if we have to pivot? Um, but they, but they said the word. So we're like, all right, you know, they're, they are, they're on the same team as you. You just have to like, kind of be late to go through all the, all the headache of it.

**Chris Gammell:** Um, well, that's really, no, that's encouraging though. I mean, like, so honestly, so like I said, I, I had a very limited experience with SBIRs that after I went up and talked to that guy after the fact, he's like, yeah, only people who have ever done these before get them. And I'm like, uh, well, how does anyone ever get started then? Yeah.

**Zach Fredin:** So, so here's, here's something I can offer to your listeners. And it's something that Joe and I have decided that we're willing to do. Um, when we were applying for a grant, the most frustrating thing was that we had no idea what a grant application looked like. Um, which was like, it's crazy. Like a lot of people get these grants every year and like, you will never find like a successful application online.

**Chris Gammell:** Publishes one online.

**Zach Fredin:** Um, yeah. So if anybody wants our grant application to see what a successful SBIR grant application looks like, send me an email. Um, okay. Zach at neurotinker.com. Let me know. Um, I don't want to share it publicly, but we have sent it out to many, many interested people that just, you know, like want to see what, see what sample grant is. I can't share it publicly because it's like, it does have some names in it and I just shouldn't publish that, but I'm more than happy to share it with any interested parties.

**Chris Gammell:** I'm always surprised when they don't do that with like the, like even formats of what they're looking for. Maybe that would, maybe that's too constrictive or something, but like, it seems like that would just lower their headaches too, but whatever. Okay. Well, that's, that's a very nice offer. That's very good. That's great.

**Zach Fredin:** Hopefully it helps someone out.

**Chris Gammell:** Yeah. Okay. So, uh, 150 K to start with, uh, that's as we talked about, I think when Avidan was on, he said they give 500 K as a, like an seed investment, but same kind of thing. It's like, that's with hardware, that's not that much money actually. I mean like that goes pretty fast. Yeah. So, so you started getting into manufacturing. What, what was that experience like for you?

**Zach Fredin:** So we, um, it was hard. I mean, it was, it was really, it was really difficult. We, um, had to figure out, we had to be really careful about what our quantities were. So, um, the biggest pilot run we did using phase one money, um, was 500 pieces. Um, and it was, it was kind of the first, the first board that I didn't put together myself in a toaster oven. I actually worked with the contract manufacturer and had them source the PCBs and actually source all the components and do all the assembly and all that stuff. Um, and we, like, we wouldn't have been able to do more than 500.

**Chris Gammell:** Um, and just cause it just, you're just saying cashflow.

**Zach Fredin:** Just cause of cashflow. Yeah. I mean, just because of what our costs were. Um, and for our phase two grant, we're not expecting to do many more than that either. I mean, it's really just, and you're, and you're really not allowed to either. Like you're not allowed to fund a production run using the grant money. In our case, we were allowed to like fund a pilot run and then we got permission from our grant officer to like sell a couple of the boards as a means of demonstrating our commercial potential.

**Chris Gammell:** And then roll that back for more, for more boards at the, after the fact.

**Zach Fredin:** Yeah. But, but, but we're not, but we're not allowed to like, oh, take that 750 K like, well, let's, let's earmark 150 K of it for the end of phase two. Um, and we'll just like do a big run and that'll be like our kickstart, you know, like you can't, you can't do that. Um, so, uh, that's, so that's, that's really the challenge. And, um, you know, one of the things we've talked about and one of the things that they encourage, they have this, this phase two B program where like they'll do matching investment. Um, if you, if you find an investor, the NSF will match those funds. Oh, that's pretty cool. You know, if you qualify and so forth. So that's something we've talked about is like, well, maybe we will need to take on private investment at the end of our phase two period so that we can spool up a production run. Um, we also have like talked on and off from the, you know, probably since, I don't know, like 2000, 3000 BC or something. Like we've been talking about it forever, like about doing a Kickstarter campaign and we just keep pushing it off because we're like, it's kind of a big distraction at this point and we don't need to do it. So we're not going to do it.

**Chris Gammell:** You would switch into marketing and PR mode and that sucks.

**Zach Fredin:** Well, I'm like, and so a weird thing about the grant is like, you're, it's like an, it's an R and D grant, you know, you can't spend the money, AKA you can't spend your salary time on sales and marketing.

**Chris Gammell:** Oh wow. Okay. So that even includes time. Oh, that's interesting. Yeah.

**Zach Fredin:** Yeah. Well, cause like, you know, you, we have to keep time cards. We're a government, we're like, we're on a government contract and we have to have a time card. We have to like print it out. We have to sign it. Oh wow. You know, we have to do all that stuff.

**Chris Gammell:** Yeah. I was wondering about that too, because you mentioned like, so like the, in the example of like selling boards, does that money then go into a separate, like, do you have to keep two sets of books effectively of like, well, this is money that is unexpected income. Like no one's actually expecting to make money.

**Zach Fredin:** We basically had to keep really close track of it and we weren't selling, we were basically selling the stuff at cost. Oh, okay. Yeah. So we weren't. Yeah.

**Chris Gammell:** Cause then you're not really testing the market either, right? You're testing, I guess you're getting the product out there. Yeah.

**Zach Fredin:** But I mean, we're selling, we're selling, in our case, we were selling it at cost for a pilot scale run. And the way our manufacturing cost kind of works out is like, well, we were, we were able to test a few price points. And as we scale, you know, based on the, we, we were able to get pretty, a pretty wide range of quotes from our contract manufacturers. So it's like, well, as we scale at these price points, like we will get this ultimate gross margin eventually. And then, oh, and then, and then a microchip bought Atmel and the cost of my processor doubled and that increased my bomb cost by 10%.

**Chris Gammell:** One of the casualties. Did you see that change?

**Zach Fredin:** I know, I like, I know nothing about that world. It is probably a coincidence, but I just remember, I just remember like looking at those digi-key prices back in February and I was like, ooh, 45 cents a piece. And like now they're 89 cents a piece, you know, in the same quantity. So, I mean, for all I know, it's like the ATtiny88, which is the chip we are using now. Like it probably goes into some automotive product that, you know, just happened. Oh, it's, we're not making that anymore. And like global demand for them. Yeah.

**Chris Gammell:** Sourcing stuff. No, that stuff gets weird no matter what. But, but still like the correlation in your brain is.

**Zach Fredin:** Yeah. It's, it's really fun to blame that. To blame the acquisition on that. It's like a really convenient target. So that's what I use.

**Chris Gammell:** Yep. Good. Everybody needs a source of ire. So.

**Zach Fredin:** Yeah. Exactly.

**Chris Gammell:** Okay. So let's talk more about the manufacturing stuff. So you said 500 pieces, single, single micro on boards. You're not getting more than 500 pieces. That's pretty rough right there. So you're not even buying a whole reel. Yeah. Yeah. Does that mean that you, well, are you getting any kind of volume discounts at all or no?

**Zach Fredin:** Yeah. 500 pieces. When I, when I was selecting a contract manufacturer, my, my first, my first priority was like, I wanted someone that was local because I wanted to go actually be able to see them do the work. Uh-huh. And this, like, it even sounds stupid to say it, but like, I really just wanted to watch my birds run through the machine. And it was great. I don't think that's stupid. It was awesome. I was able to like go there and they were, they, they, like, the plant manager was amazing. He like, he let me go in and they like moved all of the like ITAR controlled stuff out of that area. So I was able to actually come in and videotape the run. Oh, wow. That's nice. The QFN package going through the X-ray and like videotape the, the pick and place going and the stencil printer and all that. So I picked, I picked this, this contract manufacturer because they, they're able to, you know, they were able to quote me, you know, a 50,000 piece run too in the same, in the same building. So 5,000 pieces was like on the, or 500 pieces was like the very, very bottom of their capability. They're like, we are using our smallest machine and we are only running it for like an hour and a half to do this. So a good portion of that was non-recurring. There was like the non-recurring engineering and also just like, I know they built a lot in, on a per piece price.

**Chris Gammell:** Oh no, of course there's that stuff. Did, did you think, I mean, did, did, was that a marketing move on their part? Did they expect higher growth or did you just charm them into thinking? Cause I mean like, it sounds like there are a medium to large, larger volume. Yeah. Yeah.

**Zach Fredin:** No, it was, I think it was a, I think it was a marketing thing on their part. I mean, they, yeah, they, they definitely, they definitely took a bet on us, which I really appreciate.

**Chris Gammell:** Well, I think you're supposed to say their name now, Zach. I think you're supposed to give them some marketing.

**Zach Fredin:** Yeah, it's a Keytronic EMS. And they're, they're based out of Oakdale, Oakdale, Minnesota. And they actually have a couple, they have a couple different branches around the, around the U.S. But I use the one in Oakdale because it's 20 minutes away.

**Chris Gammell:** That's great. Yeah. I mean, well, and I think you mentioned either before the show or during the show that there's a bunch of medical stuff too. So, I mean, I'm guessing that's, that helps at least to have local CMs, you know, and everybody has that.

**Zach Fredin:** Yeah, yeah. So, Minneapolis is, is, is like world headquarters or maybe not world headquarters, but is a, is a hotbed of like the medical device industry. So, you know, like St. Jude Medical and Medtronic and a bunch of other ones. I'll bet you have listeners that are employed by the other ones and I'm forgetting them. Boston Scientific, that's a big one. So, I talked to any of the CMs around here and a lot of the work they do is medical device oriented. Right. But that's kind of, I mean, that kind of works out because medical devices nowadays have a pretty wide range of quantity requirements. I mean, there's definitely electronic medical devices that like, they're going to make a million of them a year probably. Oh, sure. I'm 500,000 a week. You know, so they, so they, you know, just because they're doing high end stuff doesn't, doesn't mean they aren't also built for, for reasonable scale, I would say.

**Chris Gammell:** Yeah. I would say the only downside would be if they had price, if they had priced in like the, if there's any kind of like certifications they need to get and then that's priced into everything they quote. Yeah. Like if they don't maintain separate lines and stuff like that for the non-certified, then that would be the only thing I would think. But I don't even know what I'm talking about with certified. I don't even know if that's a thing. Certifying. I assume it is. There's some kind of ISO something. Yeah. I think there's an ISO for medical stuff.

**Zach Fredin:** Yeah.

**Chris Gammell:** That's great. No, that's good. That is really nice to have at local. So, did any problems crop up where the local actually paid off? Yeah.

**Zach Fredin:** Yeah. Yeah. Actually there did. I, I, I was like ready to pull the, you know, turn the key on the run. And they're like, oh, digi keys out of JST GH four position connectors. I'm like talking about six months ago, I checked the inventory. They had tons of them and they're like, wow. Zach needs to learn his, Zach learns his little lesson.

**Chris Gammell:** But so I had, I had six months ago. You bought them then, right Zach? Well, okay.

**Zach Fredin:** Yes. Yes, I did, Chris. Um, so I did a 200 piece run in my toaster oven. Uh, lesson learned there as well. Very tedious. I actually made, I made a little pneumatic pickup tool with an aquarium pump. Um, it works. Like I, I was.

**Chris Gammell:** No, no, no. I meant, I meant, I meant, you said, you said you needed the 500 pieces or whatever, however many it takes. I'm getting, I'm getting there. I'm getting there.

**Zach Fredin:** So when I did the 200 piece run, I, uh, the connectors were cheap enough. Like when I bought them, you know, if I bought a large quantity of them, I just bought a whole reel and I happened to have enough left on my reel, um, that I was able to bring it. I drove it to the plant and yeah. So, so I, so I, this is the other reason these guys are amazing. I, uh, I called the, I called the, you know, the person that quoted me the project. I was like, look, I, you know, I don't need all 500 of them right now, but I really need a hundred of them because like the university of Minnesota just, you know, they bought a couple kits and like, I need to, they're starting their class next month. Um, so these lead times aren't going to work. And, and they actually agreed to like take the reel that I had loaded as a partial. So they had to like, you know, do all the re-taping and all that. And like loaded on the machine, they ran 120 boards for me and I was able to get them to the, to the school. I was able to deliver them for the kids, Chris. It was great. It was a bite. Was it before Christmas? Did you make it before Christmas? I got it before Christmas. And then, you know, then they just followed the standard lead time on the rest of the connectors and they ran the balance of the run. And they didn't, I mean, they didn't even charge me for the, you know, for breaking the run up into two parts, which was just amazing.

**Chris Gammell:** No, that's good. No, that, that's what you were getting. I didn't, I didn't realize that. That's awesome. So being able to get there and just have that relationship, that is very nice. It's really interesting.

**Zach Fredin:** Yeah. It's in, um, and to be fair, I, you know, I, I, I owe it. I don't know. I go, I go back and forth on this a lot, but I know at some point I owe it to my, my investor, which is, uh, people like you, Chris, to, to, to get the best value. Um, that was a, that was a callback to like you being a taxpayer and like me getting a grant. Oh, I see. I see. Thank you.

**Chris Gammell:** I was like, I haven't, did I buy a kit when I was drinking beer with Zach? Nope. Nope.

**Zach Fredin:** Nope. Um, no, I mean like we, you know, we have a, we have a responsibility to like be financially efficient. Um, so I, I do need to look at other ways of sourcing it. You know, I need to look at going overseas and all these other things.

**Chris Gammell:** Yeah. Um, which is kind of counterintuitive too, because you'd think that they would build in something where it's like, oh, well value versus generating more tax dollar tax base by manufacturing in the U S kind of thing.

**Zach Fredin:** Yeah. You know, it's, um, it's not really called out. Um, I don't know. It's, it's, it's, it's kind of, and the other thing is like, oh, you get all your, maybe you get all your prototypes made under the grant by U S suppliers. Then like, as soon as you scale and you're out of grant, you just like kick it all overseas. And there's not, there's probably not much they can do about that. Um, right. So for me to just kind of simplify it and say like, well, I, you know, I like having videos of the parts going through the pick and place and like being able to like, you know, shake the guy's hand and actually like turn the key on the machine and all that. Um, it was, I don't know, it was in some ways an educational process for me, but, um, but then, you know, but ultimately like, so look at, we look at the cost of doing business with them and what, what the, what the finished cost is for, you know, large quantity production. And we look at what price the market's shown it will support. Then we look at like, you know, what's in between those two numbers and we're like, well, actually we can run a sustainable business based on that. It's like, why don't we focus on like, it's pretty much just Zach. So Zach, why don't you focus on like, you know, actually writing firmware?

**Chris Gammell:** Oh God, I hate firmware. Um, well actually I was going to get, I wanted to ask about that too. So, okay. So this thing has an AT tiny, 88, 88, still the 88 and more, cause I think I was trying to push you towards an F zero STM 32.

**Zach Fredin:** Yeah. So we're actually, we're actually looking at the STM 32 F zero as a potential, um, a potential next generation board, um, for a number of reasons, but the current, the current product has the AT tiny 88 and it's pretty well tapped out in terms of its capability. So it's, um, we have, uh, in, in neuroscience terms, we have five dendrites. So we have five inputs and then we have two axon terminals. So two outputs, um, each, um, each, uh, dendrite has a sense line to figure out what type it is, whether it's an inhibitory or an excitatory connection. So whether it lowers or it or raises the membrane potential. Um, so you have 10 IO ports on the input side and then essentially four on the output side. Cause we wanted the flexibility to be able to toggle them individually. Um, then they each have two switches and they also each have an RGB LED. Um, that's, that's gotta be PWM with a eight, eight PWM, um, which is more PWM channels than the AT tiny has. So it's done in software, um, which is, I don't know. It's so that's a, that's a, that's another thing where, um, you know, if any, if anyone takes a look at our boards, um, you'll, you'll see that aesthetics are somewhat important to us and the LED in particular is important to us. It's a bottom mount RGB LED. Um, so what does that mean? Like bottom mount. Yeah. So it shines down through the board. Um, which allows you to do kind of neat, yeah, kind of neat design things. It just really cleans up the, cleans up the, the, the, the look. And then also, um, I have like a three millimeter hole that's right in the middle of our logo where the LED shines through. And I plated the entire hole through. I actually, Keytronics called me up and they're like, you have the three millimeter hole there. Like it's plated through.

**Chris Gammell:** Like what are you doing?

**Zach Fredin:** Um, but it looks great. So like the LED, like it shines off the plating and it looks really awesome. Like really improves.

**Chris Gammell:** And you guys do have that impulse. So like when the impulse hits one of these little boards, that thing really frigging flickers. I mean, that thing goes high. Yeah. Yeah. So I guess that probably makes it shine even more.

**Zach Fredin:** And that, and that just means like we have to make sure we have enough resolution because normally the LED is running at like 10% brightness. Um, and then when it flashes, I want to be able to flash it at a hundred percent. So it's like really noticeable. Um, and that was, I don't know, that's been an ongoing challenge for me. It's like, I, every time I like update the firmware, I like grab a neuron and I wave it around and like see how far the, the dots are apart from each other. I'm like, that's not good enough. You need a higher refresh rate. I see. Right. Um, yeah. Right. So all sorts of reasons we want to move to a 32-bit platform. The math, the math that we're actually doing, um, some of it would really benefit greatly from being able to count above 255. Um, so, um, so something, something, something we're looking at, um, from a, from a user friendliness perspective too, you know, we're, we're really serious about keeping this subject open source because we think someday it would be cool for someone that's actually like studying real neurons. Someone that's actually a neuroscientist that's like in the lab using their probes to like probe the signals on an actual neuron can try to emulate that in neurobytes. Um, and then they'll contribute to our open source firmware and they will, you know,

**Chris Gammell:** Right. So like profiles of different neurons.

**Zach Fredin:** Profiles of different neurons. Exactly. Like, you know, there, there's, um, Bruce Land on hackaday.io actually sent me, uh, he commented on the project a couple of years ago and linked to a guy named Eugene Izikovic that basically in the, in the early 2000s came up with like a really computationally efficient way to emulate all different kinds of neurons, like the fast bursters and like the, um, all the other kinds. I don't know. And he, and he like had a set of differential equations that you could plug different coefficients in. It would like with those specific values would simulate XYZ type of neuron.

**Chris Gammell:** Yeah. That saying a differential equation, it's like, Oh yeah, you better just get some floating point in there. Yeah. Yeah, exactly.

**Zach Fredin:** So, so I actually, I wanted to emulate, I wanted to actually run his program on, on our microcontroller and I, um, I went down this like really, really deep rabbit hole of like, basically, um, I wrote this like program that would iteratively optimize a set of coefficients around, I don't know. I got it to, I got it to work on the ATtiny with a specific set of coefficients, but it's not optimal and it took a long time and it's computationally difficult enough that it really affects the LED refresh rate and it flickers and then everything. Oh, I see. I see. It doesn't look good. Yeah. That makes sense.

**Chris Gammell:** Um, okay. So wait, uh, so one more thing here. So now, um, okay, so you have, so again, people are gonna have to look at a picture to see what you're talking about, but you basically have put in the silk screen and in the gold or well in the plating, whatever looks like a neuron in there. The shape of the board looks kind of like a key where there's like a bulbous end and like a narrower end. Right. But then you mentioned connectors are on the edge. So then what does this look like when they're all plugged together?

**Zach Fredin:** So, um, when you're actually, how does one plug them all together? I suppose. Yeah. When you're actually working with it, the, um, all the components and everything are, it's designed to be face down on the desk. Um, so when you're looking at them, you know, you just see the neuron, the gold neuron shape and you have the flashing light in the middle, um, to, to connect them. Um, the connectors are all, um, side entry locking JST four position connectors. So you kind of get a thumb and forefinger and squeeze the connector together and pull it in or put, push it in or pull it out. Um, and the cables are different lengths. So we have, we have a stubby cable that's like an inch and a half long. And then we have a longer cable that's like eight inches long, um, that you can use, um, red cables for excitatory signals, green, uh, blue cables for inhibitory cables to, to form simple networks.

**Chris Gammell:** Um, and is it built into the cable? Like where is the coding built in? Is it in how you plug it in or is it built in how the cable is built or how do you actually tell? Yeah, actually.

**Zach Fredin:** Um, so, so as it stands right now, excitatory cables have three conductors. So they have power, power ground and signal. And then inhibitory cables have four conductors. They have power ground signal and type. And the type pin is just held high all the time. Um, so the, uh, the microcontroller looks for the type flag. And if it sees that it identifies it as an inhibitory input, um, which is not the most efficient way to do it. But, um, and then for inhibitory cables, we made them blue and excitatory cables, we made them red. So you can physically tell the difference, but every once in a while you have a student that's like, why do the excitatory cables have one fewer conductor than the inhibitory cables? I'm like, ah, excellent question. Let's go on a really off topic tangent about electronics for a while.

**Chris Gammell:** Yes, but I wanted to talk about the whole time anyways. Excellent. Excellent. Yeah. You get the really curious ones.

**Zach Fredin:** Yeah. I go into, um, there's a local high school, um, Patrick Henry high school in Minneapolis that I go into. I've gone into a couple of times, um, cause I have an engineering teacher that I work with and, um, he's like, come on in and like talk about your startup and like teach them about neuroscience for a while. Um, so we like talk, talk about neuroscience. We have a little, um, patellar reflex kit that's got like a 3d printed leg and you build the neural network that like makes your leg kick when the doctor smacks it with a hammer. Yep. Um, that's all well and good, but then like, I get really excited when I get to show them ChiCAD and like teach them about schematic design and stuff like that. Nice. Yeah. I'm indoctrinating those, those impressionable minds on using ChiCAD. It's great.

**Chris Gammell:** That's awesome. Yeah. Well, you know, I approve. Uh, that's no, that's good too. Cause I think, well, it's interesting from a lot of these perspectives where it almost could drive the conversation a little bit, right? I mean, like thinking about the tools that we used in biology class, right. Or the tools that we used in a lot of different classes, I suppose in general, like there weren't many electronics demos, right. Even if they were simulating something else. So it could be kind of an end around to go and teach kids that, Hey, electronics actually make this cool thing. I don't, I don't know. Like it's, I think they understand electronics are a thing, but not that they are tangible like, like you're doing, you know what I mean? Like, it's more like, Oh, I have an iPhone. Right.

**Zach Fredin:** Yeah, no, no, exactly. We, um, you know, the, the, I think it was the department of education or some, some group within there did a, did a study on like how, how we improve STEM retention. Like kid graduates from high school and wants to study a STEM topic. And like, how do we improve the likelihood that they'll actually finish it? And one of the factors they found to be important was studying STEM topics in a multidisciplinary fashion.

**Chris Gammell:** So like, Oh, that's great.

**Zach Fredin:** Studying engineering while you're studying biology, for example. So we're like, we're really keen to bring all that stuff in kind of as soon as we can. Um, and what's, what's neat is like, I, I would do this thing in the, in, at, at Henry where I would, um, I'd pass a neurobytes board out to all the students. Um, and I'd be like, all right, now flip it over. So you're looking at all the little boxes and the soldery ball stuff or whatever, um, connectors and like black things. Look at that really closely. Yeah. Yeah. All the, all the silvery things, the little purple buttons and the little, you know, the tantalum capacitor and all that. Um, and I was like, and I look up at the overhead and I would have a full screen, like close up view of the KiCad, you know, with just the, just the, uh, copper, you know, the copper layer on the back of the board. And they would like, they would kind of like hold it up and like look at the board and like you would see like a series of light bulbs light up and like, Oh my God, like that's,

**Dave Jones:** you know, what we're seeing there is actually exactly what I'm seeing right here. And then like, then we'd go back to the schematic and they'd be like, Oh my God, and that's that. And well, okay.

**Chris Gammell:** I just imagine some of these kids failing their, their, their, their, their neuroscience final though, because they're like, Oh yeah, you know, you just hook things up and KiCad. That's how, that's how the neuron works. Yeah. Yeah. It's all about it. It's all about that. Yeah.

**Zach Fredin:** And of course not all of them got that excited, but we had a couple that were like really pretty stoked about it. That's good. Yeah, absolutely.

**Chris Gammell:** I like that multidisciplinary thing too. I, if you have, if you have the source for that, I'd love to see the article about that.

**Zach Fredin:** Let me see if I can, let me see if I can find it and I'll send it over again.

**Chris Gammell:** Yeah. I've been saying, um, the, uh, one of my goals for the show this year is to do stuff where it's more, you know, like we talk a lot of, we talked to a lot of people that are doing electronics and stuff like that, but I'm actually interested this year and getting people on the show that are like using electronics in their work, understand electronics and, but then actually even need more help with electronics. Right. So like, so like, I mean, not that you don't like, you know what you're doing here, but like I was thinking about like, um, so like environmental concerns stuff where they might have need sensors or new, have new challenges, that kind of thing. Like I am actually very interested in that. And if people are listening and they know of stuff like that, I'd love to hear about it. So just want to get that out there. I guess it is a new year.

**Zach Fredin:** I think electronics, there's, there's a huge opportunity to reach out to other parts of the community, like beyond the electronics community. It's like design, you know, we're at such an interesting point where like hardware is so cheap and it's so easy to develop and you can do such amazing, cool things with it. It's like, there are, there are more interesting applications than like any of us will ever figure out. Like we need to, we just need to get that stuff. We need to push it out as far as we can. And then someone that's like in some way far off field is going to find some crazy, amazing application. Like that's where the magic really happens.

**Chris Gammell:** I think, honestly, I think the big thing is like the, we need the Zacks to meet the Joes, right? I mean, like you met Joe who's already in this field. You understood the electronics piece. And then there was a cross, you almost like need that as like the, as the format for, for other teams where they need, they need someone to be doing it like hands-on hardware, but it's still, I mean, it's obviously a very interesting application. So, so that's the stuff that I'm, I'm very interested in the new year and hopefully, hopefully we can find more people like your team like that. I think that's, that's really cool.

**Zach Fredin:** Yeah. No, I think that's a great idea. I think your, your, your, your day job does a pretty good job of that. Oh yeah. I do say so myself. You guys are doing great work over there.

**Chris Gammell:** Hackaday IO is, is definitely a good meeting place like that. I think, I think there are more places that, you know, like that, that kind of stuff. If it, that is the hard part, right? I mean, like, I don't know where biology people hang out. I don't know where neuroscience people hang out. And so, well, I just joined a new hardware space in Chicago and I did find out there's another, there's actually a bio startup place. So I'll probably go poke my head in there at some point. It's like a medical device startup called Matter around here. So. Yeah.

**Zach Fredin:** I think I saw that picture. I don't know if you like posted on Instagram or something. I think I saw a picture of that, of that space though. It looked awesome. Like you guys all have like work pictures and stuff, right?

**Chris Gammell:** That place is so big. Man. 63,000 feet. There's 10 different types of workshops. It's, it is like, and like, and the fact that it started, like I've talked about on the show before, but like the fact that it started right when I moved here is like, I mean, it's just like fate. That's crazy. So. That's so awesome, man. If there are people in Chicago, we're looking for more people to join and more people to help build stuff because it's like, oh, Hey, we're supposed to open in six weeks. So. Yeah. Oh, that's awesome.

**Zach Fredin:** Well done. How many, how many people will it support? Is it like a workspace for a couple hundred people at a time or is it? Yeah. Oh yeah.

**Chris Gammell:** I mean this thing used to, the facility itself used to, it used to have three full, like, you know, like the super long SMT lines. Oh yeah. Yeah. It's just like pick in place after pick in place, then goes into reflow.

**Zach Fredin:** With like the giant Quiznos ovens and like. Yeah, exactly. Quiznos ovens.

**Chris Gammell:** Yep. Yep. Quiznos ovens. Uh, and, uh, yeah. And so like it was three of those with full, like, it's just nuts. And they, yeah. So.

**Zach Fredin:** Do they keep one by any chance? Do you guys hold on to any of the capital equipment from that place or is it all stripped out?

**Chris Gammell:** Uh, they left a bunch of stuff behind and, uh, not the line, but someone else, they actually brought in a separate company, uh, that's going to be doing in-house pick a place. So.

**Zach Fredin:** That's fantastic. That's amazing.

**Chris Gammell:** Yeah. Yeah. I'm very excited. Yeah. You'll have to just come down and visit. You're not that, I mean, you're not that far, right? It's what? I will. I will. Yeah.

**Zach Fredin:** No, I'll just screw it, man. I'll just drive. It's not a problem.

**Chris Gammell:** I actually don't know how far away we are. How far is Minneapolis from?

**Zach Fredin:** We're like six. We're like six hours.

**Chris Gammell:** Yeah. So that's like an hour flight. It's not bad. Yeah. Cleveland to Chicago. Yeah. Okay. So you mentioned the stuff you hate. Let's talk about that. So, uh, what, what do you have to do to program these things? I mean, like, so you mentioned the math, but then the, the, when you've said at the out, the outset of like the, the threshold seems like it's easy, but it seems like there's a lot of nuance there in terms of models and stuff.

**Zach Fredin:** Yeah. Um, it's, it's, it's interesting. Like we, we, we started having bugs because we weren't listening to inputs the way we should, if that makes any sense. Like we were, we weren't driving the inputs based on pin change interrupts. It's like, well, so we're missing an input by like a couple of milliseconds because we're only checking it when this program loop goes by. Um, but when you build a big network and it's all, all the information is shooting around asynchronously, like it, like it makes a difference, you know? So the timing thing becomes a big, a big deal. I think the, I think the hardest thing we've had to consider were the, were the connectors though. Um, you know, because I, I really wanted to be able to have something that was, um, small, you know, I wanted something that wouldn't dramatically change the form factor of the board. I wanted to be able to get seven, you know, seven user friendly connectors onto a board that's like, you know, 30 by 60 centimeters or 30 by 60 millimeters or whatever. See, I'm trying to switch units a little bit. Um, so 30 by 60 millimeters.

**Chris Gammell:** Yeah.

**Zach Fredin:** So like that would be like one and a half by two and a half inches.

**Chris Gammell:** Oh yeah. Okay.

**Zach Fredin:** Yeah. We want seven connectors on there. Each connector needs to have four positions. Um, and it needs to be able to handle pretty small. Yeah. Well, we like, we want to be able to handle close to an amp if we can, you know, so we're trying to use 26 gauge wire, um, an amp, why an amp? Um, because we want to be able to make a really long chain of them and then put a servo on the end of it.

**Chris Gammell:** Um, so like our, yeah, it's daisy chain. Okay. So, and these things are powered off the line, right?

**Zach Fredin:** That's, that's arbitrarily daisy chain. Um, as long as someone wants and you, you know, you need to be able to power it from anywhere in the network. And then like, and there's a motor mode that, you know, converts one of these things to directly PWM, uh, you know, a hobby servo. So it's like, well, now you have like a 300, 400 million amp load at the very end of this chain. Um, so it's kind of been like this design exercise that has to like go all the way back into like, what is the intended neuroscience circuit you're building? Like, does it make sense to ever build a chain that's like 30 neurons long that ends in five motors? Like, well, if it doesn't, we don't have to design around that.

**Chris Gammell:** But, um, we can't, we still kind of are defining the, the, the limits of the solution space. Right. Cause then you can list that of like, do not do this, this, and this. Yeah.

**Zach Fredin:** Yeah. And we really don't want to put any limits on the actual users. I don't want to have to tell them like, don't connect them this way or like something will catch fire. It's like, well, and that'll happen, you know?

**Chris Gammell:** Um, so, and, and also those things. So I remember when you showed it, so you guys were demoing at Maker Faire. Yep. Yeah. Um, the, there was a loop as well. So like, how does that end up? Does that affect the power or is the power only going one on one pin? So it doesn't really matter.

**Zach Fredin:** Yeah. The power just, the power just kind of feeds into the network in one place. Um, and you're going to have, you're going to have like some voltage drop as it goes from place to place, to place, to place. And like, once you build a really complicated network, calculating what, you know, what the voltage should be based on all of these different connections becomes like the resistor grid problem from school. Oh yeah. It's like, well, let's just plug it in and see if it works. It's a little, um, so what, you know, one of the things we've done is we, we put regulators on board each, each device, um, so that we can handle, you know, a one volt drop essentially maximum, um, which kind of, I mean, that accommodates, that accommodates a lot. But, um, so the, so the challenge I have with connectors though, is that like any, you know, any connector that's not designed to be consumer facing, that's like not a micro USB and not an eighth inch phono and not, you know, X, Y, Z. Um, like the board to board connectors that I wanted to use, they're, they're, they're never rated for more than, you know, 35 to 50 insertions because the manufacturer designs them as an assembly aid, you know, it's like, well, in 10 years, if you swap this board, like you're going to have to unconnect it once and then connect it back in again. And they, um, and you know, in some cases they'll design them so that like this connector can sit around for five years and like maybe a non-ideal environment. And when you connect it, it'll, you know, connect aggressively enough to scrape off all that corrosion and like the first time and still hit our resistance, you know, measurement. And as it was explained to me, it's like, well, sometimes that aggression, you know, comes at the detriment of long-term reliability. Cause like now you plug and unplug that thing and it's like, there's no oxide layer left to scrape off. Now you're just damaging things and loosening it up. Um, so, so I, I had a lot of conversations with JST. I've, I've gotten to know my local value added reseller who I use to actually buy my cable assemblies. Now I, I bought the crimper and I crimped a lot of cables, but now I pay someone to do that. Um, but, but I also have gotten to know the JST regional regional rep. We actually have a JST regional sales manager that's local to Minneapolis because they do so much business in medical devices. So I can kind of talk through him to the factory and talk to the local guy. And, um, and of course like every conversation I have, they're like, yeah. And, um, no one's ever going to tell you it's for more than 50 connections. And I'm like, come on, man. Like real, like what connector can I use though? And they're like, well, you could wait. So you're doing what gold flash on that? I'm not doing it. At this point, we're not doing any of that. We're just, they're just, um, the standard ones, which I think have like a nickel plating on them. Um, so I'm actually, I'm actually getting a sample of the gold flash ones later this week. Um, actually tomorrow.

**Chris Gammell:** I mean, that's the thing that like the gold stuff that'll wear off real quick.

**Zach Fredin:** That's the thing. Yeah. I could go gold flash and it's like not that much more expensive, but gold flash is really like corrosion resistance before you plug it in that first time. It's like, well, or you could do gold plating and like those connectors are three times as expensive. And, and, and the connectors already represent, um, you know, 30% of my bomb, which is crazy. Like, you know, yeah, the connectors are. Okay.

**Chris Gammell:** So I'll ask, I'll ask the, the a-hole question. Why are you still using branded JST connectors?

**Dave Jones:** Uh, yeah, no, that's, that's a, that's a fair point.

**Chris Gammell:** I'm, I mean, only because I see the same thing. So like the most of the time when you see people using like those lithium ion batteries, like, uh, well also, cause I see a lot of search results too in my, in my work. And, uh, you know, like, uh, there's this like one brand that's really like, it's got this obscure part number, but you just see people searching for it all over. I mean, it's not even like that this is secret inside stuff. You could see this on like, like if you go to find chips, we, we show a lot of the searches and, uh, in like, like popular searches and it's in there, you know, like, it's just like, these are parts that people are searching for because they need, it's the same problem you're running too, of like low cost stuff, low cost connectors.

**Zach Fredin:** I guess, I guess part of it is that the, the failure mode for my connectors will be kids getting frustrated and throwing it in the trash. Um, you know, because it'll, it'll just, it'll just be like an intermittent issue. Like you'll, every once in a while you'll plug a certain cable into a certain neuron and like the light won't turn on or it'll reset the microcontroller or it'll do something, you know, it'll do something weird. Um, so I, so I have like a really, there, there, there's a really high risk of severe customer dissatisfaction. If we have issues with the connectors that are, that are intermittent. I mean, if they break, if they break one off, uh, the board, like it almost never happens. And when it does, it's very clearly cases of like abuse or they pull, they pull the crimps out. Like I had a kid at Maker Faire that pulled the crimps out and it's because he grabbed two neurons and like just was ripping them as hard as he could. And just like, boom, breaking cables.

**Chris Gammell:** And I was like, no, that's, that is a tough audience right there.

**Zach Fredin:** No, no, it was great. That's like the only time we've actually had that kind of failure, but the, but the insidious, like bad connection, like, you know, wiggle it a certain way and the light flashes or you get a high resistance. Like I can't, I can't accommodate that. And like, and I was, I was a sales guy for a couple years. So maybe I have like an unnatural respect for sales engineers, um, that maybe, maybe isn't common, but you know, I was having a conversation with the, with the value added reseller, my sales engineer from them. He stopped by the other day and he was just like, look, I, you know, I've, I've had customers that like bought the real JST header and then they got knockoff JST pins and like they had intermittent field failures five years later.

**Chris Gammell:** And like, oh no, no, no. Yeah. I get the quality argument. I'm just saying that like, that's, that's just, I mean, that's as long as you're measuring that stuff, right. As long as you know that the quality is important to you, then it's like, yeah, of course you're going to pay for it. Right. And then maybe you just charge more for it. And it's like, but then you, you also work that in your marketing where it's like, well, this works.

**Zach Fredin:** Genuine JST connectors.

**Chris Gammell:** No, not like that. I will totally say that though. I'm, I don't know. I've been. Yeah, but nobody knows what that means. I mean, like, it's not like, like there's a neuroscience high school teacher somewhere. Well, I don't know. Maybe they could. Um, maybe it's a thing.

**Zach Fredin:** But so, so, so to your, to your point though, I should, I should test it. I, um, about a month ago, I eBayed a, a, like a five and a half digit four wire multimeter and a set of Kelvin probes and a, um, GPIB connector, which is like, or, you know, the, the old HP, um, like 36.

**Chris Gammell:** The HPIB, the IEEE 488. Yeah. Yeah.

**Zach Fredin:** So I, so I, I bought the, um, the ProLogix adapter and I got it to work from the command line. So I can just like, I, I set it up with a test jig and I put on like some Netflix thing and I just sat there mindlessly like plugging and unplugging it for three hours or two hours. Um, and I was able to test a connector to 2,500 cycles. Um, and actually like data, like see how it aged. And, um, it's really, it was really interesting. I, I only did it once. I needed to, I needed to try it a couple more times with the same thing and then I need to, I want to try it with, you know, their gold.

**Chris Gammell:** Wait, you did 2,500 insertions?

**Zach Fredin:** Yeah. Yep.

**Chris Gammell:** Yes. Good Lord, man. That's a, that's a lot of plugging and unplugging. How's your finger afterwards? Fingers afterwards.

**Zach Fredin:** Whatever. You gotta do what you gotta do. Um, I get, I get some serious connector.

**Chris Gammell:** Serious.

**Zach Fredin:** Yeah. I got connector fatigue. I need to do the rest of the day off. Um, no, on that note, I actually just hired an intern though. So Jared, if you're listening to this, you're going to be on connector testing duty probably starting next week. Oh man. Get ready for that.

**Chris Gammell:** That sucks.

**Zach Fredin:** Yeah.

**Chris Gammell:** And also, that's nice. You're getting it.

**Zach Fredin:** In all seriousness, I, um, I found this guy, um, because we sold, we sold these kits to the university of Minnesota and they were using them in their neuroscience capstone lab course. They had like neuroscience students were like, as seniors, they needed to build some neuron circuit that they had learned about in their undergrad and then like defend it to their teachers and use neurobytes for that, which was kind of cool. Um, and then, um, this guy emails me and he's like, Hey, um, my girlfriend's a neuroscience major. I'm an electrical engineering and physics major. And I checked out your website and I got to play around with her kit when she brought it home and it was super cool. And I want to be your intern. I was like, sounds good, man. Stop by. Which was great. It's like, I had no idea how to hire someone and now he's my intern.

**Chris Gammell:** So it's awesome. I was just going to say if, uh, you know, if someone emails Zach, uh, he he's two for two on people emailing him and then, you know, changing, changing the course of his life in terms of personnel.

**Zach Fredin:** It's pretty awesome. I haven't, yeah.

**Chris Gammell:** Zach, I have a bridge to sell you. I re. Yeah.

**Zach Fredin:** No, my, my wife is an architect. Um, so that means she knows a structural engineer that she'll check on it.

**Chris Gammell:** Yeah. Oh man, that's, that's good though. Um, okay. So, and so I guess one last question about this stuff, cause you, you, we have one or two other things on the list. Yeah. Um, but like who, who was using this stuff? I mean, so you mentioned colleges, but are high schools doing it? I mean, where do you see it going in the future?

**Zach Fredin:** Yes. High schools and colleges. Um, we've, we've kind of gotten in, in terms of the number of kids we have out in the field, we, we kind of have a 50, 50 split between the two of them. Um, the challenge is finding high schools actually are teaching any neuroscience. Um, but we've actually, like when I was in high school, I took biology when I was in ninth grade and I learned about graphs and photosynthesis probably. Um, but like now. Oh, well, you know what else you learned?

**Chris Gammell:** Cause everybody learned.

**Zach Fredin:** Oh, right. The mitochondria is the, uh, the, uh, what are they, what are they, um, I don't know,

**Chris Gammell:** I don't know, Chris. The mitochondria is the, the. Someone's shouting at their, their podcast player right now. It's the powerhouse of the cells. Right. Right. It's the powerhouse of the cell. I knew there was some specific term you wanted me to use. I, that's always quoted on Reddit too. So I always see that.

**Zach Fredin:** The powerhouse of the cell. Interesting. It's a good one. Um, yeah. Yeah. So, so anyways, now, now we go into high schools and I, you know, one of them has a, like an anatomy and physiology class. Like that's what they learn about. And anatomy and physiology, you'll have a month of neuroscience. Um, oh, and same with AP bio and AP psych. I mean, their classes like that, they're starting to have, you know, one week or maybe two weeks of, of neuroscience content. Um, which is getting to the point where they can justify buying a set of kits for their classroom. Um, it's kind of.

**Chris Gammell:** Right. So maybe it's not like all kits for all kids, but it's. Yeah.

**Zach Fredin:** The way we're talking about it is like, well, we're, we're, we're putting together a kit that's going to be around 150 bucks and it's good for two to three students working in a group, you know, and we can provide up to two weeks of curriculum, you know, classroom curriculum for that. And you're going to need to buy 10 kits for your classroom. So it's $1,500 investment, which is depending on the school, often something that they're able to pay for without having to go to the district level, which is, I don't know. Oh, that's nice. When you're, when you're, when you're dealing in, in what we're learning is when you're, when you're in education, like you have to think about, you really have to think about like your distribution chain and, and, uh, you know.

**Chris Gammell:** Yeah. I was going to ask about that too, because it seems like, so like people, I guess MakerBot was famously trying to sell into a lot of schools and I think they did succeed, but I think they had a huge. Salesforce for that kind of thing. And it doesn't sound like something you'd want to be doing again.

**Zach Fredin:** Yeah. I mean, our, our plan at this point in the, in the short term is direct sales through our website and, um, getting, getting word of mouth publicity at like the National Science Teachers Association conference and at Maker Fairs. And, you know, there's, there's, there's groups like that. Um, and then eventually, you know, we, we need to get involved with a, with a classroom product distributor. I mean, there's guys that go, guy, you know, people that their company goes to the schools and, and, and sells these solutions. And, you know, we're, and we're trying to.

**Chris Gammell:** Do they, do they all have a curriculum attached to it too?

**Zach Fredin:** Yeah, typically. Um, so that's part of, that's part of what we're doing. That's really more Joe's, Joe's side of what we're doing. Our phase two grant is doing a lot of curriculum development. So worksheets and like general lesson plans and pictures and videos. And, um.

**Chris Gammell:** No, that's great though. I mean, like, that's the thing I, I didn't realize. I had talked to a chip company who actually does, um, some university stuff and they just like hand professors entire labs. And I'm like, oh, I, I always thought they did it themselves. I don't know why I thought that. Like. Not, not most of them. All of them. I mean, like it, it makes sense, right? I mean like that. And it's, it seems like a good idea. I mean, obviously the chip company has a vested interest in doing so because then they get their chips in front of a lot of smart kids. And, you know, like it's definitely a sales technique, but I just, I don't know why I never thought that that would be a thing.

**Zach Fredin:** I'll tell you, I'll give you some perspective on what makes like coming from the electronics hobbyist world. Um, what I thought was an interesting representation of how that supply chain is different than I'm used to. Um, one of the classrooms I went into had 20 Arduino kits, um, and they were all genuine Arduino. You know, you know, they were all full price Arduino UNOS. Um, and they came in parallax boxes like from the parallax company. Um, okay. I didn't like, I don't know. I thought that was interesting. Cause I always associated parallax with like the propeller and the basic stamp and all that stuff. And like, maybe they've come to an agreement recently.

**Chris Gammell:** Oh, well they're just, I'm sure they're a distributor though too. I mean like that, that's pretty common where they'll, people will distribute other stuff. No, that's, that's true. And then they can sell full solutions. I was, I was thinking you were going to say, and then I found out each cost kit costs $200 or something that that's what I expect. Honestly, that's what I expect in education is that they, you know, they kind of take them by the horns because they, because there is more money to play with sometimes, not always, of course, there's a lot of funding problems in the U S but like, just that there are, you know, it's kind of, if you're going, if you, if you are capable of selling into a system like that, then you also went, once you are in, then you charge more.

**Zach Fredin:** No, that's, that's, that's certainly true.

**Chris Gammell:** Huh. Well, that's a, so like, what does a kit look like for you, your stuff?

**Zach Fredin:** I mean, like right now, so we're putting together a kit that has like six neurons and a power supply and a couple of switches and a bunch of cables and like a little carrying box. And you can do, you can do a decent number of experiments with that. A lot of the work we're going to be doing the next year is going to be building out our ecosystem. So like we built prototypes of like light sensor modules that allow you to build little photo receptors. Then you can build a model of an eye that then has like the layers of, you know, cell neurons, you know, in the, in the retina and sound sensors and, you know, other output devices. So like an audio, a little audio output, like beepers. So you can like hear every time a certain part of a network fires. And we just want to, we want to kind of create more, more basic building blocks that students can use. So it's, it's less like, well, here's the five things you can do with this kit. Right.

**Chris Gammell:** Plug this together, do this, this, and this, and then you're done. Yeah, exactly. Done everything by neurons ever again.

**Zach Fredin:** We're like, we're, we're, we're close, but we're not to the critical point where like, this is fun to play with on its own. And like, that's, that is completely where we have to be. Like we need to have, we need to have a product where like someone does the, you know, does the five lessons and they're like, oh my God, we can plug this together and this together and grab all these other sound modules and like build a little neuron synthesizer, you know, or I mean, it'd be really easy to build like a little sequencer, for example. Right.

**Chris Gammell:** Yeah. I mean, it sounds kind of like, I mean, I don't know if you dislike or like the analogy, but I mean, it's kind of like what Little Bits does too, right? I mean, Little Bits.

**Zach Fredin:** Oh, no, absolutely. Absolutely. Plug that stuff together. They're a company that we, we've learned a lot from and are certainly someone we look at emulating in some cases. Their, their, their fundamental concept of like a, a ground and a power rail that's shared is one that we take. Their pure, pure, their purely analog design is not one we take. I mean, the concept of neurons is that they're like kind of internally analog, but externally digital and rate controlled, you know, whereas Little Bits is like zero to five volts, you know? Um, and then their magnetic connector as well. Amazing and novel are also just not at all suited for what we're doing because we need to have such a higher density of interconnections. Right. Right. Um, but, um, but yeah, I mean like a lot of the stuff they've done in terms of like their kit packaging and like, um, how they've built.

**Chris Gammell:** Oh, their design stuff is very nice. Yeah. Oh, it's amazing. I mean, a lot of their stuff is great. It's just that it seems like their scale is a lot higher too in terms of the, I mean, they raised, God, how much money did they raise?

**Zach Fredin:** $60 million was the last round.

**Chris Gammell:** I don't know what the hell the investors are thinking with that, but then again, I don't know. Like maybe there, maybe they will be like educational piece, I understand, but.

**Zach Fredin:** Yeah. There's some, um, there's some big, I mean like there's some big companies that have bought large, large kits. I know that. Um, they had a pop-up shop in Manhattan. I visited actually, which is pretty cool.

**Chris Gammell:** Oh yeah. Um, and they're at the, uh, New York, uh, I think MoMA, I think.

**Zach Fredin:** Yeah. Yeah.

**Chris Gammell:** Um, we probably went to, went to that museum with the same person who we know.

**Zach Fredin:** True. Yeah. Yes. Um, but what's, um, what's really interesting about little bits is that they, um, they still have a commitment to like this open source idea. So they still release all their schematics and you can still like, what I really like is that you can still buy the connectors and I hope they keep doing that because I've been, um, I've been buying like their magnetic connectors and building little neurobytes interface boards. Oh, that's cool. When we, when we build our model of the eye and we needed a light sensor that was like easy to adjust the scale and the span of, and like operate on five volts and gave me a voltage output. It's like, well, a little bits already has those boards. So I'm just going to grab a bunch of those.

**Chris Gammell:** Yeah. Yeah.

**Zach Fredin:** Um, and that works pretty well. That's cool. I don't know if it's something we'll do forever, but. I don't know.

**Chris Gammell:** They were trying to do that where they like had like people recommend boards for a while too. And that, I think they stopped doing that. Unfortunately. Yeah.

**Zach Fredin:** I talked to, I actually talked to one of their, um, when I was at maker fair, one of their, um, one of their R and D engineers, like it was at New York maker fair. So they're based in New York and he happened to be there. And like, he was checking out the model of the eye. I was like, Oh yeah. And we, we, I hope that little bits is okay with us doing this kind of joking around. He's like, we're fine with it. Like, ah, damn, that's cool. Um, then we talked a lot, we talked a lot about kind of the challenges that they faced in, um, you know, you know, maintaining that program essentially. And it was like, yeah. Oh yeah. I can only imagine. Yeah. I mean, it, it sounds good on paper, but it's like, well, how much, how much support can you really give this? Like in terms of engineering, like once, once you actually have this idea, it's like, well, now to get it from this idea and this prototype into production is like actually many, many, many engineering hours. And like, now we have to look at whether or not the market will support that.

**Chris Gammell:** We often talk about that on the show of ideas aren't really worth much. So they're nice, but yeah, it's the, the other stuff is a hard part. Yeah. Yeah. Totally. Um, so speaking of new ideas, you have new hardware actually, and you've been playing with, uh, and I wanted to talk a little bit about it because you had mentioned kind of some of the struggles with it.

**Zach Fredin:** Yes. I, um, I, I only had one, I, I don't like doing Christmas lists, but I, the only thing out of my Christmas list this year was a Lepton sensor. Um, the, um, the 60 by 80 FLIR, um, SPI thermal imaging sensor. Um, so I got one of those, which is awesome, but I haven't really played with it at all. Um, but it seems like a pretty straightforward device. Um, I know Mike Harrison has done a lot of, he did a lot of the early documentation on that. He actually like pulled a Lepton out of a commercial module before FLIR made them available for sale, uh, and released the data sheet. Now you can, now you can buy the modules one, you know, single piece on DigiKey and download the 50 page data data sheet that like tells you the entire protocol and all that. So it's not really a reverse engineering thing anymore, but, um.

**Chris Gammell:** So, you know, I mean, some like creatures though, they, don't they react to like light on certain, I mean, I guess you already have a light sensor type thing, but would it be possible, would you need a lot of processing to, to take like a, a sensor like that and then have a neuron react to that? Yeah.

**Zach Fredin:** So, so I think what I'd probably do instead is I would get a, essentially like a single pixel microblometer, you know, a single, a single long wave infrared sensor and as opposed to a 60 by 80 pixel array. Um, it's cause it would be, it would be scaled more appropriately kind of to what our, what our network does. Or we would, or we would use that, um, what's that Sharp? I think Sharp makes a microblometer that's like four by 16 pixels. Um, there's a couple projects.

**Chris Gammell:** Yeah, there are a couple out there now cause I keep seeing these, these, uh, thermal cameras that pop up.

**Zach Fredin:** Yeah, yeah, exactly. So this one, this one is, is, it's a little bit, I mean, the 60 by 80 is small by, small by camera standards, but for a thermal imager, that's like massive, you know? Yeah. Um, but yeah, that's more just for, for playing around with. Um, then my, um, my, my squadron of ESP 32s finally arrived. So I ordered a, a handful of the ESP 32 S boards from seed studio back in like, I don't know, September. And they finally arrived and much after that. Um, and they're just the, the basic board that's like just the module and you can solder the module down onto their breakout that just has like a, a reset and a IO zero. Um, but it's a neat little board. Like I, I, I was able to, I use like an FDTI FTDI, um, you know, one of the TTL serial adapters. Um, I was able to program it and upload some sample code on it. So I made it, I made it into a little access point that like served up a little monk, had a little Mongoose server on it and like served up a little website and spat like open all the open local SSIDs onto a serial terminal and stuff. And I haven't done much beyond that, but it's, um, it's a really neat little device.

**Chris Gammell:** And it doesn't have the Bluetooth on it though, right?

**Zach Fredin:** It does. And it's like, I don't think the Bluetooth is really documented at this point. It's like, um, and, and, and, you know, the, the sample programs I was running and then modifying very slightly, um, that I found on like ESP32.com and ESP32.net, like the official forum. And then the, the, the site that has like the listing of all the people that have done projects with it so far, basically. Um, like I checked out a bunch of those and like a lot of the documentation was like a couple of days old when I was uploading it. So it's, um, very much a new thing, but, um, but yeah, ultimately, you know, it's a pair of, um, what 240 megahertz, 32 bit processors that run free, free RTOS. Um, and then, uh, you know, a Bluetooth and Bluetooth classic Bluetooth, low energy and wifi. Um, and the wifi can do like access point mode and it can do scanning and, you know, all this other stuff, um, all on this little tiny chip that's really cheap.

**Chris Gammell:** I, yeah, I don't really understand where that's going to, I, I, I, I've been talking about the 32 a lot, sorry, the 8266 a lot, just cause like the, the low cost of that kind of thing. And the P the fact that people are like on, like, like you mentioned on Hackaday IO or other places, like hacking on these things and just using them for weird little projects. And, uh, you know, it's, there's something there. Like, you know, I, I, we cringe when we say IOT, but like when you talk, you want to talk about like actual things out in the world, changing stuff. I think projects like that, um, like that's, that's, that's what's really going to do it. I personally think. Yeah.

**Zach Fredin:** I think there's, I don't know. I think probably in the minority of your listeners and certainly in the minority of your minority of like electronics hobbyists, but like the whole IOT thing is, I don't know. Chris, do you ever, this is like really going to be super nerd, nerdy. Um, did you ever watch Battlestar, like Battlestar Galactica, the show? I never did actually. No, sorry. So the, the captain. I know a lot of people that like it. Yeah. So the captain of the show, Lee, is it Lee Adama? I think it was the, the, the, the captain of the Battlestar Galactica, which Battlestar is a class of ship. And the Galactica is the one that he commands. Um, and the Galactica is the only one that survives like this massive apocalypse at the very beginning of the series. Um, and it does so because Captain Adama like refused to network the ship. He's like, I don't want the ship like becoming sentient and like being able to communicate every little thing that's going on in every little bit of the ship continuously. Like I need to have like the, the dead, you know, the dead man switch or whatever. Um, I mean, there's more to it than that, but just the idea of like sensors becoming more and more ubiquitous in our lives. Um, I think it's something to be careful with.

**Chris Gammell:** Right. Well, I was going to ask if you're a, you know, if, if, so you think that the, uh, the neurotinker is going to end up training the, you know, the young scientist that ends up creating AI or implanting electronics into, into a neural net or a neural, a human neural system or something.

**Zach Fredin:** Well, I don't know. So we're, you know, one of the, one of the operating modes we're going to put in the next iteration. And this is one of the reasons we want to go to the 30 kill all humans mode. Is that exactly?

**Chris Gammell:** Yeah, totally. Yeah.

**Zach Fredin:** Um, no, the, um, you know, is a, uh, a LTP mode for long, you know, long-term potentiation, which is basically the process in which a neural network changes weight, you know, relative weightings of inputs in response to semi, to stimuli. So essentially learning. Um, so right now our networks are static, you know, you can, and they're, and because of that, you know, you, you show it's like an artificial neural networks person. And they're just like, Oh, like you flash LEDs. I'm like, well, no, we teach people about biology and we have different goals, but, but once we actually can build the flexibility into the system to change weightings and actually change based on stimuli, we can actually start building things, you know, really, really simple circuits that learn. Um, having said that, like neurobytes will never be able to match what artificial neural network guys were doing 25 years ago, because like right now they're dealing with, you know, 50 million node networks, you know, like, you know, that would require 50 million neurobytes at 20 to 30 amps a piece. Just the connectors alone. Just the connectors and power plant is going to be a problem.

**Chris Gammell:** Um, but yeah, no, but so wait, and how are, how are they doing that? Are they doing that on chip somewhere is just simulation?

**Zach Fredin:** From what I understand it's, it's, it's done, you know, people have done it, like done it in FPGAs and in ASICs and so forth, but I believe most of it is just done on normal PCs and like using, using GPU processors and stuff like that. And I guarantee you, there's a lot of people listening to your podcast that like know a lot about that. And I hope that they, I hope that they bring it up because you should, you should get some artificial neural networking guys on here. And I would love to talk to them.

**Chris Gammell:** I have no idea about any of that stuff. Yeah. That's a great application.

**Zach Fredin:** Every, every, every maker fair I go to, I have one or two of those people that show up and they just blow my mind. And it's, it's really, it's really fascinating. Um, but yeah, I mean, to that point, I think, you know, our core, our core mission is to like get 13 and 14 year olds to start thinking in terms of like membrane potential and thresholds and weightings changing. And like, so yeah, you know, you, if you can have someone that starts to intuitively understand how a network can learn, um, you know, that's, that's the hard part. It's, it's a little easier to, for them to scale that up to a massive network once they understand the basics. But I think it's, I think what we're trying to do is really blunt the leading edge of the learning curve in terms of, in terms of neuroscience and so forth. So yeah, no, we, we could be partially responsible for the AI singularity and all of those horrible things. Thanks, Chris.

**Chris Gammell:** They'll call it battle, battle star gazakita.

**Zach Fredin:** Yes. Right. Did you, you must've written that down ahead of time. That's impressive. I did not. That was terrible. I'm sorry. Uh, so, so, so, so that's me. That's, those are my new parts. I want to hear about the new parts that you have that you're going to be building stuff with.

**Chris Gammell:** Do you have any, any, uh, no, nothing super new. What did I get? Um, you know, so I, okay, so this is actually learning related because, okay, so you're, you're talking about teaching high school kids and sometimes when I'm writing code, I feel like I'm an elementary school kid, but, um, I was going nuts over, so I mentioned on the show, we had Tony from Adafruit on and he was talking about MicroPython and stuff like that.

**Zach Fredin:** Yeah, yeah, I heard that episode. Yeah, yeah.

**Chris Gammell:** Yeah. And I was just going nuts because I was trying to program these sensors and I just couldn't get it to work. And, you know, so sometimes I think the thing is with like kits, the important thing about kits is the fact that they're all the same. And so what I did is like Tony had a bunch of tutorials and I was trying other sensors and just trying to like, you know, figure out what would be different. And just cause I had them on hand and, and I thought it was going crazy, but then I tried this, they were like SparkFun sensors. So I tried the SparkFun sensors with the Arduino board that worked fine. And then I tried them again with the MicroPython thing that wasn't working. So I'm like, you know what? Screw this. And I went back and I just bought all the stuff from Adafruit. That I, you know, like the, just the sensors to have the exact example. Like that is such a key part in learning when you're starting out of like, just, I just want the muscle memory at the beginning, you know, like, or like the learning path you're talking about. Like, I just need to see, I just need to get to the end of it. So I mean, it's just, I just got some new sensors.

**Zach Fredin:** That's awesome. And I, that point that you made, I completely agree with though too. I mean, I, I was playing around with the STM 32 F0. I had like some of their, you know, their discovery boards. Yeah. And I wanted to, I wanted to get a ST link and the, the command line tools working on it. And I wanted to use LibOpen CM3 and all this other stuff. And like, the only way I was eventually able to get it to work is by exactly duplicating everything that someone else had done. Um, which is, yeah. Yeah. So, um, cause that, cause that, that's what happens when you're dealing with like layers of abstraction and you're like, oh, well I have, you know, the LM 3974 D F instead of the DC. And it's like, oh, the DF.

**Chris Gammell:** You're just looking for whatever's different, right? Yeah.

**Zach Fredin:** Like the DF uses like a different speed I squared C bus or like it's got a different address or it's got something else that like is dealt with in your abstraction layer way off to the side. Like, like you don't ever want to have to touch and it just doesn't work.

**Chris Gammell:** You didn't know that Zach. Yeah. Come on, man.

**Zach Fredin:** Read the manual. Um, no, but you know, and, and on the manual thing, you know, back to the ESP 32, that's, there's kind of this double-edged sword where they're like providing this really low cost device, um, and they're crowdsourcing a lot of the documentation, but then.

**Chris Gammell:** It turns out the cost is in the paper, huh? Yeah.

**Zach Fredin:** Well, but I think about what I do at Neurotinker and they're like, I, I, I would never use a part that didn't have a data sheet that I could rely on. Um, and that's a liability. And I'm just saying they don't do that and they, like, that's probably not a great example, but I think just in, just in general, um, there's this balance where like you're tinkering around with stuff and getting it to work quickly. But if you actually want to scale it up, like you need to understand the supply chain and you need to understand like the device specifics that are in the data sheet. Yeah.

**Chris Gammell:** Yeah. No, that's, that is a huge piece, right? That'll bite you every time. It's like, oh yeah, no, you're buying the wrong. Yeah. That's, that's not good down to minus 40 C or something like that. Yeah. Oh, I guess I should have checked that. We do have to worry about that in Minnesota. That's true. You guys do. Yeah. Yeah. Not much warmer here to be honest. Yeah, that's, that's true.

**Zach Fredin:** So, so, so what sensors, what sensors did you get with the Adafruit deal?

**Chris Gammell:** So I got a couple of sensors, uh, oh, I don't, my box is in my, my book bag. Like, uh, but it's just a simple temperature sensor, like an I2C temperature sensor. Like, I think it's a MCP, maybe, maybe not. I don't know. That's the other thing where it's like, you're treating like sensors now where I'm just looking at is on this specific thing as just like code. Yeah. You know, it's like, oh, but eventually I'd have to dig down into it. Um, but, and then I've got, I got one of the screens as well. Cause I've never really done it. I've never done any display stuff, even with like simple displays. Oh, okay. So I got some of their display stuff and I'll be trying that out. Yeah. You know, my goal, I think I've said on maybe last week's show or the week before, but my goal in 2017 is for the show is like I mentioned to get more people on application wise, but for me is to, um, to do more prototyping in general, just like, and I think you, I mean, you do, you do a lot of prototyping with your, your soldering method, right? You do a lot of cut and solders type stuff. Yeah. Yeah. I always get really caught up in like, oh, it needs to be a board, blah, blah, blah. Yeah. And I think, I think you're doing it right, to be honest.

**Zach Fredin:** Yeah. So I, I, um, I had this, this, I'll give you an example. I don't want to like waste your entire evening or whatever, but I had a example where I constrained myself when I was prototyping. I think it's really important to do that. Um, so I, I, um, have a, like I, we have a cabin in Northern Minnesota that has like no cell phone coverage and no internet access and all that stuff. So I lugged, I lugged my oscilloscope, my soldering station and like all of my parts and all this other stuff up to the cabin. Um, and the objective was to build a oscilloscope for the neurobytes where you could like visualize the membrane potential essentially. So it's like, you could plug this thing into a neurobytes board and it would graph in the time domain, you know, the, the, the real time membrane potential value. And you could actually see the spikes and all this other stuff.

**Chris Gammell:** Um, and the only doc, so where you missed out on something that you said you brought with you, what did you bring with you on like manuals and stuff? Okay. So, yeah.

**Zach Fredin:** So, so before I left, I was very careful about what I, what I brought. I brought, um, and this will be like a big plug to the work that Paul Stofgren has done. Um, I brought, I brought my Teensy 3.2, um, and I brought one of his 240 by 320 TFT LCDs. Um, and I brought the entire book that he printed out and passed out at the Hackaday Super Conference in 2015 when he did his audio workshop. Oh, his workshop. Yes. Because it was like, it was like written documentation that was like, this is an SPI display and like, these are the pins that you need to use. And then this is the library that you download and this is how you get pixels to do this, this, and this. And it was just like, you know, once you have, I basically was able to like know when I left Minneapolis, like I have all the documentation I need. Like I have two PDFs and I have this binder and like, I know I should be able to mash those together and be able to like master this display. And then I brought.

**Chris Gammell:** Make a thing. Yeah.

**Zach Fredin:** And I like, so, so I knew I could figure it out on the code side and then I brought up like a couple of pieces of FR4 and a razor blade and some flux and like a bunch of solder and like, well, I don't know, like the cut, you know, the, the carve FR4 and apply flux and then like solder it and kind of Manhattan style ish. I think it really lends itself nicely to getting breakout boards to behave. So if you have a bunch of, if you have a bunch of modules and you want them all to be in the same place, you can just, rather than solder on straight headers, you can solder on 90 degree headers. So they have like a flat side and they just kind of surface mount to a piece of FR4. Right. And just point to point wire it from there and put in resistors and stuff. And it ends up being suitably compact and durable and something that you can make that day.

**Chris Gammell:** Well, I think, I think followers of the subreddit or the Twitter account may recall, I've tweeted at least two of your masterpieces. One that I saw, I think was part of the scope thingy. Yep. Or it was at the same time that I saw it. I think that's probably right. And the other was that when you took a QFN and you were soldering enameled wire to it. Oh, yeah. I still don't remember why you said you were doing that. You just yelled at me for posting it to Reddit on your behalf.

**Zach Fredin:** Yeah, because I didn't get it. Chris, I didn't get any karma for that. Sweet, sweet karma. We've both been on Reddit for a while, man. I checked out your account. You've been, what, eight years? I mean, it's almost as long as me. I have nine years. No big deal. I'm not counting. But I did check it before we got on today.

**Chris Gammell:** How many points? How many fake karma points?

**Dave Jones:** Okay, okay. Less than you. So I could have used that. But not a big deal.

**Chris Gammell:** Post to the subreddit. You're right. Post to the Empire subreddit. You will surely get that. We'll do.

**Zach Fredin:** I will do that. I will do that. But yeah, no, to answer your question, I had bought a couple of Texas Instruments 16 channel constant current LED drivers just to play around with them. And I just bought the ones that came in 24-pin QFN packages. So it's like, well, if I want to use this on a breadboard, I got to dipify it. Yeah, I don't know. I got into this hobby because I'm obsessed with soldering. Like, that's where I have to remember, like, that's where the passion for me comes is like getting the soldering iron out and physically melting metal and making stuff stick together. Like, that's it, man. Like, flashing LEDs are great, too.

**Chris Gammell:** Where did that come from? I don't, like, did your parents solder?

**Zach Fredin:** Yeah, so when I was like seven, my great uncle, who was an electrical engineer, he gave me a VHS tape, and it was the Heathkit Guide to Soldering.

**Chris Gammell:** Oh, my God. Do you still have it? I don't.

**Zach Fredin:** Like, my mom might have it at home. I got to check when I'm back in Columbus. I'll take a look because it's amazing. Like, it gives you all the good practices. And, like, you know, clean everything and use flux. And, like, this is what raw and core flux solder is. And, like, don't use the acid core flux that your parents have for sweating pipes. And, like, so what was really interesting is, like, you know, we're using 60-40 solder. It's like, well, tin melts at, like, 400-something Fahrenheit and lead melts at 600-something Fahrenheit. And, like, solder melts at 270. And, like, why is that? And then they show a picture of a binary phase diagram. And, like, I don't know. I told you this, like, before we started. But, like, that's why I became a metallurgist. It's because, like, I remember seeing a phase diagram when I was a kid and, like, learning why my soldering iron could melt a tin lead alloy. But it couldn't melt tin. And it couldn't melt. Or it could. But it would take longer. Yeah. So it's an amazing video. But, of course, it doesn't talk about service-bound stuff.

**Chris Gammell:** It's a video, though. I'm trying to see if I can find it on YouTube right now. It was called the Heathkit Guide to Soldering. Is that right?

**Zach Fredin:** Yeah. Heathkit Learn to Solder or something like that.

**Chris Gammell:** I want to say it's, like, 45 minutes or an hour long or something like that. Oh, dude. You've got to digitize that. I mean, like, Heathkit, I know people are going to say, oh, they're coming back. Whatever. They're not coming back. Yeah. Oh, man.

**Zach Fredin:** I mean, I appreciate the aesthetics of those kits they released. But, like, they're, no, it's not the same.

**Chris Gammell:** No, that's a different era, right? And it's fine.

**Zach Fredin:** So the other Heathkit thing that I have that was really cool is they had a bunch of recorded, like, they had these big binders that, like, had all these project plans and stuff. But they also had these, like, really thin records. They were, like, the thickness of a transparency sheet. But it was, like, a 45-minute, you know, record. And they were just really fun.

**Chris Gammell:** Wait, were they the ones that you, like, oh, the paper records? Were they paper?

**Zach Fredin:** Well, it was, like, plastic. It was, like, blue plastic or, like, red plastic. And they were, like, as thin as a transparency sheet.

**Chris Gammell:** No, no, no, no. I just remember, like, McDonald's. I remember when I was, like, really young. McDonald's gave away a record that you could play. But it was, like, a toy record, basically. That's awesome.

**Speaker ?:** Wow.

**Zach Fredin:** I'd want to be involved in, like, the engineering of that, of that, like, that supply chain. Like, figuring out how you can stamp paper records for, like, essentially the cost of stamping paper without a record.

**Chris Gammell:** Yeah, yeah, yeah. It was, well, even just seeing how actual records are made is there's some great science there, too. But, like, just, like, the wax press and stuff like that.

**Zach Fredin:** Have you seen Ben Krasnow? You know what else? When he did the video, like, the GIF of his SEM watching the head, like, the head of a record. It was so cool. Yeah, yeah. And he ended up just, like, having to take a whole bunch of images and then, like, stitch them together on his SEM. But very neat to see that.

**Chris Gammell:** No, that's what it was. So, we did, like, on conference day that I think I mentioned on the show in the past. But I think I mentioned that last week. But one of my other coworkers went over how records were made. And then she referenced Ben's video and showed us that other video on how records are pressed. That's awesome. Yeah, it was really cool.

**Zach Fredin:** I'm glad people are, like, still interested in documenting that technology. Because I think at some point, someday, like, the need to really precisely measure, like, 90-degree out-of-phase tiny bumps using a stylus. Oh, but it'll be relevant to someone in, like, 30 years. And they'll be like, oh, my God, this already exists. I just need to find a record head from, like, 100 years ago. Find me a hipster. Find me a hipster. And in Minneapolis, we have those.

**Chris Gammell:** Oh, yeah? Up there, too, huh? Yeah. They're everywhere, man. Yeah, it's all right. Okay, so still, are you doing a... I feel like there should be, like, a soldering challenge. You know what I mean?

**Zach Fredin:** Yeah, so there was one. And it was posted on Hackaday, I think. Like, six months ago, someone made a board that, like, basically was, like, a 555 LED flasher. And you just made it, like, five times. You made it with dip. You made it with, like, SOIC. You made it with TFF, whatever the smaller SOIC that's wider. And you made it... I don't know if you made it with a QFN or not. And then the LEDs, you go, like, from, you know, T1 to three-quarter insertion LED. Then you have, like, an 0805 and an 0603 and an 0402. Oh, cool. And then, like, the idea... And then you have, like, a resistor and a capacitor for each one. The idea is, like, you solder this together as fast as you can. And if they all blink, then you, you know, you're timed and all it or whatever. And I've been meaning to...

**Chris Gammell:** Kind of like that scene in Social Network where they're, like, they're drinking tequila and they have to, like, break into a server. So, like, we should do that. Exactly. Except it should be bourbon. And we should use really hot soldering irons. Yep.

**Zach Fredin:** Yep. No, I agree with that. And, yeah. So, I'll see if I can find that. I'll see if I can see the link to that, too.

**Chris Gammell:** I've planned for a while. I haven't done it yet. But I do have plans to make an obstacle course. But it was more about bodges than it was about fast soldering.

**Zach Fredin:** See, I think we should do a collaboration on that or talk about it more. Because I really think that would be fun. And you do it standardized and you, like, have the whole thing out there so anybody can spin the boards up. And you have standardized components. And it's like, anybody can, like, get their own time on this and see where they stand. And we need to, like...

**Chris Gammell:** Oh, I was just honestly just going to do, like, a... You just need, like, a reel of zero ohm resistors. Because then what you do is you put a final resistor in line. And then if the LED lights up, then, you know, like, it's all tied together. That's a really good point.

**Zach Fredin:** Yeah.

**Chris Gammell:** And then the idea, though, is, like, you know, you have to TP two resistors. Then you have to... I always call it stonehenging. I don't know if other people call it that.

**Zach Fredin:** Yeah, the graveyard. The graveyard of tombstones, man.

**Chris Gammell:** That's right. And then...

**Zach Fredin:** Oh, I see. I see. When you put one up and you put another one up and you put a third one to bridge it. Right. Yeah.

**Chris Gammell:** When you need to put three resistors in line on a single resistor's pad, right? Yeah. If you want to make three resistors in series. And then another one would be, like, you don't need to double stack. That's easy. Whatever. Oh, yeah.

**Zach Fredin:** Did you see the guy on Reddit that did, like, a 20 stack? It was... I think it was on the PCB Reddit, maybe.

**Chris Gammell:** I did see that one. Yeah. Yeah. It was ridiculous. It was like, when you really need a lot of power in a resistor or something like that. Yeah.

**Zach Fredin:** It's like, you need new traces, man. You breathe on it and it flips over, but...

**Chris Gammell:** Well, and then today I was tweeting with Micah Scanlime on Twitter and she had posted, like, a bodge to, like, flying wires. And I had proposed that that be called an alien landing or something like that. But I was thinking, like, sometimes you need to do that, too, where you're going from, like... If you need to go from a resistor to, like, a via, right? You need to, like, solder to a via. That's happened a lot for me where... Oh, yeah. You need to just access some other point or you need to cut a trace. You need to scrape a trace. That's... Yeah. So...

**Zach Fredin:** Yeah. I think a bodging... Something bodging related would be a good one. I don't know. I see it posted, like, posted a lot where it's like, oh, it's like the ugly, ugly style

**Dave Jones:** or the ugly way. It's like, no, I think...

**Zach Fredin:** I don't know. I think it's neat. I really like it. And I've gotten really into this clear polyurethane wire. I get this... It's like 34 gauge. I bought a spool on Amazon. It's like 2,000 feet of this stuff. And it's polyurethane insulated. So you just, like, touch it with a tinned iron and, like, dip it in flux.

**Chris Gammell:** So it's kind of like the magnetic enameled wire?

**Zach Fredin:** Yeah. It's essentially a magnetic enameled magnet wire. Um... Yeah. That's exactly what it is. It's 34 gauge. That's impressive. 34 gauge, yeah. Which is about... It seems about right. Because that's, like, small enough that you can basically... You can basically tack it on, you know, stuff that's 0.5 or 0.65 millimeter. Yeah. You just kind of do it in the right order.

**Chris Gammell:** Do you use magnification or no?

**Zach Fredin:** I have, like, a 3X ring magnifier that I use. That's it, huh? Yeah. You know what else I use?

**Chris Gammell:** I don't know.

**Zach Fredin:** I use lead-free starter exclusively.

**Chris Gammell:** Whoa. Yeah. Them's fighting words. Well, you know what, actually... I know.

**Zach Fredin:** So I throw down the gauntlet. Anything that you can do with lead-free starter, I can do with lead-free starter.

**Chris Gammell:** I'm squarely in the lead-free world now myself because my lab is in my kitchen.

**Zach Fredin:** Yeah. Well, and I, like, I make kids' products. I make stuff that, like, middle schoolers are going to handle at, like, a Maker Faire. You know, you can't... You can't mess with that idea.

**Chris Gammell:** I'm fine with that, though.

**Zach Fredin:** Well, yeah. I don't know. It's not that hard. It's not that different. Like, I don't know. I don't think the kid's going to, like, build a nuclear submarine that needs to be worried about pin whiskers. And, like... So the two issues with lead-free solder is, like, it's got to operate at a higher temperature. It's like, oxidation and all the temperature-related shit is a little bit harder. And the solidest to liquidest distance is a little bit longer. So, like, 60-40 solder is, like, very close to the eutectic. So, like, when it solidifies, it solidifies almost instantly. But, like, lead-free solder, from my understanding, you just... You have to be more careful when it's solidifying that you don't move it around or you'll get cold joints. But, like, I don't know. I think it's just... You just get used to it and then it's not an issue anymore.

**Chris Gammell:** Yeah. No, I think that's the right... The way I think about it is you don't tell a kid that beer's awesome, right? You let them realize it's awesome when they turn 21 or around thereabouts, right? Yeah. And that's what they'll figure out with lead-and-sodder, too. They'll be like, oh!

**Zach Fredin:** Yeah, yeah.

**Chris Gammell:** This is great.

**Zach Fredin:** But I didn't need this in my youth. I look at it from a... Like, just a... It's a more somber perspective, I guess. But, like, if we want to bring more people into the hobby, the way to not do that is to have lead-and stuff. Well, like, so the real danger with soldering is, like, the flux vapor. Like, the lead's never going to hurt you unless you, like, eat a spool of solder. Like, that's been established. But, like, at this point, like, we've lost the marketing contest against lead. Like... Oh, right, right, right. Like, you just can't have lead in stuff anymore, you know? And, like, whether or not it's superior in every way, like, it's kind of irrelevant if you actually want to get mom to, like, let little Johnny solder stuff, you know? That's a good point, yeah.

**Chris Gammell:** That's... Yeah, especially for educational stuff. Yeah. Yeah, just in general. I think that's a really good point.

**Zach Fredin:** Yeah, yeah. Bring on the hate. But I'll tell you what.

**Chris Gammell:** I'm not going to say it's not awesome, but I'm... It is awesome, but I think that you make a very solid point there.

**Zach Fredin:** Well, honestly, the biggest disappointment is, like, leaded solder always just makes a nice fucking joint. Like, it's not even, like, that it's a better... necessarily a better joint. It's just always shinier. It's, like, way shinier. Yeah, that's true. You know? And it's... Right, it's not dull. Yeah, it's frustrating, but you get used to that.

**Chris Gammell:** Well, Zach, we are now an hour and a half plus in. Is there anything we missed? Oh, man.

**Zach Fredin:** I don't really think so. I just... Thank you for getting in touch with me, man. I really... It's been an honor, and I've really appreciated the time. It's been fun to talk to you about this stuff. Yeah.

**Chris Gammell:** No, I'm glad that we've... It's really been awesome. You've been tailed on similar interest here.

**Zach Fredin:** Yeah, absolutely. And I will come out to Chicago sometime, too. Actually, yeah, that'll happen soon. Excellent. We'll have, like, a...

**Chris Gammell:** You might want to wait until summer, but... Yeah, yeah, that's fair. You should come out... You're used to the winter.

**Zach Fredin:** Come out to Minneapolis. You should come out to my cabin this summer. Boom. Do it.

**Chris Gammell:** You know, so we did actually talk about the whole idea of an isolated design contest at some point, so maybe we'll have to play on that idea some more. I think that's very impressive, by the way, and...

**Zach Fredin:** It's a really fun way to constrain yourself. It can be... I mean, it can also... Like, it could have been horrifyingly frustrating if I had, like... Yeah, right. You know, left my Flux at home or something.

**Chris Gammell:** And then I made Flux out of TreeSap.

**Zach Fredin:** Yeah, totally. Ish. Yeah. Or, like, I had to use plumbing solder or something like that.

**Chris Gammell:** But, yeah. No, no, I just mean, like, the isolation piece, too, of, like... I'm so addicted to, like, just Googling data sheets or Googling solutions. Like, it really does change how you figure stuff out. And I think that... Like, I saw former guest Todd Bailey. I follow him on Twitter. And he was talking about, like, he isolated himself over the winter break and read the USB standard. Wow. Which seems like the only way that you could probably read that.

**Dave Jones:** It's like 1,000 pages or something, isn't it?

**Chris Gammell:** Yeah, dude. That's crazy. I think there's beer involved. But that's awesome.

**Zach Fredin:** I mean, that's good.

**Chris Gammell:** But, yeah.

**Zach Fredin:** Well, I mean, if you can make it to northern Minnesota in the summer, certainly not winterized, I would be happy to... But I would be happy to host an isolated electronics design party. That would be fantastic.

**Chris Gammell:** That'd be cool. All right. Well, thanks, man. And where should people find Neurotinker?

**Zach Fredin:** Oh, Neurotinker.com. My partner, Joe, runs our Twitter account. So that's at sign Neurotinker.

**Chris Gammell:** It's N-E-U, right?

**Zach Fredin:** N-E-U-R-O. N-E-U-R-O. Yeah. N-E-U-R-O-T-I-N-K-E-R. I had to check my sticker on my phone. And I run our Instagram account, which is also at sign Neurotinker. And then if you want to read, like, kind of an exhaustive history of the project, search for neurobytes on hackaday.io because that's where all of the documentation for the last two and a half years has lived and will likely continue to live.

**Chris Gammell:** Right. And I'll link all those in as well. Yeah.

**Zach Fredin:** Cool. Thanks a lot, man. This has been a lot of fun.

**Chris Gammell:** Awesome.

**Zach Fredin:** Thanks, Zach. We'll talk to you soon. Yeah. Sounds good.

**Speaker ?:** Bye. Bye. administered administered administered administered administered administered
