---
episode: 403
title: An Interview with Mike Szczys
url: https://theamphour.com/403-an-interview-with-mike-szczys/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released August 12th, 2018. Episode 403. An interview with Mike Stisch. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Mike Stisch:** And I'm Mike Stisch, Editor-in-Chief of Hackaday.

**Chris Gammell:** And that is how you say it, folks. Mike Stisch. I've been correcting people for you, just so you know, like all these years.

**Mike Stisch:** See, now I avoid it myself. I generally introduce myself as Hackaday Mike, at least when I'm at Hackaday Things. When I'm not at Hackaday Things, then I don't. Right, right. Talking to your wife's friends.

**Chris Gammell:** Hi, I'm Hackaday Mike. What's wrong with him?

**Mike Stisch:** Yeah, I answer my personal cell phone. Hello, Hackaday Mike here.

**Chris Gammell:** Yeah, right. You're on with Hackaday Mike. What's hanging? What's hacking? So we are at DEF CON.

**Mike Stisch:** DEF CON 26, yeah.

**Chris Gammell:** Another one. So my first DEF CON was 22 with you.

**Mike Stisch:** As was mine. We had a raging good time that weekend.

**Chris Gammell:** I actually did not enjoy that first one. Really? I mean, we had some fun parties and stuff, but I, so this is an interesting thing we can maybe talk about, is like, DEF CON felt really clicky to me. And like, it's not that I feel, I don't feel upset by it. It's just like, I feel kind of icky. It's like, yeah, like I want to, I want to be part of, you know, this is, it's like a, it's like a FOMO thing. I want to be part of it. And you don't hear about things. You're just kind of like chasing, you know, when things aren't well publicized, you're just chasing party. There's a lot of events and talks and whatever. And literally you, you, you are going to miss things because it's such a big thing, big conference.

**Mike Stisch:** I'm kind of surprised because like, I feel very comfortable just going up to strangers and injecting myself into the conversation and seeing how it goes. And it feels like you have that same skill. Some days.

**Chris Gammell:** I mean, not always though. And I've gotten better at it. Maybe hanging out with you. So we should mention, so background. I just worked for Supply Frame.

**Mike Stisch:** Yes. And Supply Frame owns Akaday. They're wonderful overlords who make everything possible from live events to going to other live events and producing, you know, great pieces of long form content.

**Chris Gammell:** Yeah. Yeah. And you guys have been furiously writing as you, that's always the downside for you. I think it's like you're writing as you're, while you're experiencing it. I have to pop away and get this thing published.

**Mike Stisch:** Yeah. In general, I try to spend part of each day finding a good story and then part of each day writing and trying to get it out. And so for the most part, I have a great time at events, but I have this anxiety that I'm not going to be able to find a cool thing. Right. You know, like you're going to go to a talk that you thought was great and it's not. And then you've been stuck there for an hour. Maybe you get up and leave and feel rude about it. I don't worry about that.

**Chris Gammell:** But I think more so that you're missing other things.

**Mike Stisch:** Yeah. Yeah. And actually speaking of missing things, like it's Saturday afternoon and I still have yet to go to a talk this weekend. Uh-huh. Yeah. That sounds familiar. You know, I like, I really wanted to go to Mike Osman's talk of huge regular on the show.

**Chris Gammell:** Oh, yeah.

**Mike Stisch:** And he, you know, does wireless hacking village stuff. And I went to his talk last year and I think that was probably my favorite thing of the entire year. Yeah, that was fun.

**Chris Gammell:** That was the, that was the, I actually have talked about that because that was the encoding, right?

**Mike Stisch:** Digital spread, digital signal spread spectrum. Right.

**Chris Gammell:** I remember the code that it was like the, oh, it was forward error correction, right? Because it was like you have this huge number and that you can basically dig signals out of noise. I remember that piece.

**Mike Stisch:** Yeah. He took this huge noise signal and he was using new radio. The new radio. Good new radio. Right.

**Chris Gammell:** Derek Kozelsman on the show.

**Mike Stisch:** Yeah. And I had like maybe written some stuff. I definitely read a bunch of stuff about it. And you kind of look at it and you're like, okay, it's graphic. And then you maybe don't understand any more of that. But Mike Ossman has an amazing skill of taking a difficult problem and breaking it down into a very approachable set of things. He also has crowd management skills. So like people were interjecting their helpful little things during it. And he was just not letting himself get off track. But I went out of there feeling like, you know, if I wanted to sit down and study and spend some time on this, this is a tool that's not out of my reach. And that's really cool. Like that's the way I want to feel coming out of a talk.

**Chris Gammell:** Yep. Definitely. While we're mentioning GNU Radio, I should mention Derek told me from GNU Radio, they're having a convention out here, I think in September, October. Really? And they're doing like this. Actually, they have a sponsor and they're giving away like STRs to like all the students that are attending. It was really sweet. So not pitching. That's not sponsored here or anything like that. But it seemed like an interesting thing for people that haven't heard about it.

**Mike Stisch:** So I think it's important because I think that's where everything's going. You know, as we design more things, it's going to be less and less specialized radios if we can.

**Chris Gammell:** Yeah.

**Mike Stisch:** Yeah, totally. Totally.

**Chris Gammell:** So, well, speaking of specialization, how did you get here? That was a terrible segue. How did we get Hackaday, Mike? What is the...

**Mike Stisch:** Oh, how did I get onto the Hackaday thing? Sure. So, I guess maybe I should explain my background, which is that my career is actually as an orchestra musician. Yep.

**Chris Gammell:** Always fun to hear people.

**Mike Stisch:** I always watch as you say that and people are like, what? Yeah. I still play in two orchestras in Madison, Wisconsin. I have two college degrees in music performance and it's like what I always wanted to do. And I'm glad that I'm able to do it.

**Chris Gammell:** You got to say which instrument. Come on.

**Mike Stisch:** Oh, I play French horn. Yeah. And I'm really in a lucky position with the orchestras that I play in because we do kind of everything. I play in... Through those orchestras, I play in an opera orchestra, play in a chamber orchestra, full symphony orchestra. I've played like Beatles tribute concerts and Led Zeppelin tribute concerts. And yeah, so I get a chance to do everything that I wanted except for make a lot of money at it.

**Chris Gammell:** So... Oh, yeah. Oh, musicians. Yeah. I remember that. Yeah.

**Mike Stisch:** Those jobs are like maybe two thirds of an income, no benefits. And so my wife and I, she's also in the two orchestras, have always scrambled for the other part of that living. And going back to like seventh grade, I've been, you know, like computer geek, hacker guy. Um, I had...

**Chris Gammell:** It's just a weird... The music plus tech isn't weird, but it's the fact that you actually made it work. And as the musician... I don't know... I know a lot of people who are in tech who play music, myself included. I don't know many people who are in music and do tech.

**Mike Stisch:** Yeah. I guess there's probably a lot of people who tried to do music and ended up not finding the job. Sure. Right. Yeah, exactly. Yeah. Yeah. I feel really lucky for that. You know, in the orchestra world, it's like somebody has to leave a position and then there's an audition. And so, yeah. So I feel really fortunate. But I started, you know, writing part-time for Hackaday as a way to kind of round out my income. I was also, like, teaching private lessons, French horn lessons, like going to schools. And then also, like, when my wife and I bought a house, we built a soundproof room in our basement. Because you don't want to teach seventh grade French horn players and bassoon players if the other person is in the house or they will go batty. Yeah. But, you know, I kind of moved up and up and up with Hackaday. And then when Supply Frame bought the site in 2013, I had the option to go full-time and really never looked back. It's been an amazing experience.

**Chris Gammell:** Yeah. And that's just about when we, I started in 2014. So, yeah, just about the same time. So, it's been good getting to know you. It's been real, you know. See you later. Yeah. Well, you know. This is the end of the friendship. You're dead to me now. Yeah, right.

**Mike Stisch:** No, but, you know, I do cherish the time that we work together. I felt that both professionally and socially, it was, you were always someone that I could work really easily with.

**Chris Gammell:** You know, the Midwesterners, we get along, you know. Yeah. So, you live in Madison, Wisconsin.

**Mike Stisch:** I do, yeah. And it's much better than any other place. Oh. Especially if you like cheese. You know, it's a great city. It's a Big Ten college town. And it's also the state capital. But it's only, like, you know, in-city limits is, like, 250,000 people. I think maybe the county is, like, 500,000. Yeah. So, there's some stuff going on there. You can always kind of find something to do. But you can also get anywhere in 20 minutes or 30 minutes. Which is cool.

**Chris Gammell:** Yeah. Well, so, to go back to the supply firm stuff, we kind of launched in, well, I helped you and the rest of the team when the Hackaday Prize started. And that's still going, right?

**Mike Stisch:** Yeah, it is. It's in its fifth year now. And it's our global engineering initiative that really looks at, you know, all this creativity and skill and expertise that the Hackaday community has and says, hey, can you spend part of your time actually thinking about something that can make the world a better place for people? And...

**Chris Gammell:** Sorry, man. Yeah. Every time I hear that, I just think of that clip in Silicon Valley first season where it's all people at TechCrunch and, like, they always end their presentation. And that's why we're making the world a better place.

**Mike Stisch:** Yeah. And I, you know, I get the bullshit meter tweaks a little bit when you say things like that. But I do think that there's a chance to move the ball on this. And the thing is, if everyone was like, oh, I have to set out to do this thing in order to make the world a better place, no one would ever try. And if you look at the majority of the projects that are entered are not going to change the world, that's not really the point of them. I mean, I think the point of it is to look at it and say, we have amazing power as individuals to learn things and then to apply that knowledge and to pass that knowledge on forward. And so I often think the, you know, the kit that you're working on for your Hackaday Prize entry this year could end up being the thing that inspires someone that actually does go out and makes a discovery or does go out and start a company or join an initiative. And I think, I always think about, like, how do people get ideas? Where do ideas come from? And I really think it's pollination from person to person to person. Yeah. It's like the medic. Yeah. This is trying to collect pollination of topics into one spot and then kind of, you know, highlight it, you celebrate it. Yeah.

**Chris Gammell:** That's a good point. Yeah. I always think about that too. Like, like on the teaching side of things, like teaching is a noble, not that I'm a teacher. I don't consider myself a teacher. But like, you know, like if you're doing education stuff, you're really, you're passing that stuff on. You're trying to get that next, you know, you're not necessarily going to, you know, solve world hunger or, you know, save the world from climate change or anything like that. But one of your students might, you know what I mean? Like, and like, and there's, there's an important thing there. And it's like, it is just the thing that happens, has to keep happening, you know? So.

**Mike Stisch:** Yeah. And, you know, through music, like in college, I would go and have an hour lesson with my professor every single week, one-on-one in a room with no one else there. And I didn't really realize until after I was out of grad school that like, that's not the experience that most people have. Right. But like, looking back on it, that kind of, you know, that pedagogy of learning knowledge and passing it on is totally alive and well in the hacker world and in the engineering world. That's true. Yeah. Where, you know, like you form a team and then the skills from each person on that team are generally, you know, worked on a one-on-one basis when the need arises.

**Dave Jones:** Yeah.

**Mike Stisch:** And I think you shouldn't have to be working for a company in order to get that. Like, if you're working on a hobby project that someone else has, you know, an interest in it, or if you have a problem, you should be able to like collaborate, you know, using the tools we have with the internet and also the kind of the tools that we have to get together in person. Like, you may not have someone that's right down the street, but you probably have someone that's pretty close to you. And if we can use these online communities to make those in-person happenings occur, Right. There's great power.

**Chris Gammell:** Increasingly rare and more important, I think.

**Mike Stisch:** Yeah. Yeah. And I also think we just need to make sure that we don't end up with this like concentration of engineering all in one place. Like, Silicon Valley is the only place that you can go. At Apple, right. Yeah, exactly. Or at Google, right, yeah. Yeah, I mean, we need it in Poughkeepsie. Yeah, we do.

**Dave Jones:** Sorry, Poughkeepsie, I have no idea. I just pulled that out.

**Chris Gammell:** Mike hates Poughkeepsie. Mike Stish hates Poughkeepsie. Yeah, I mean, so I've actually talked to Alicia from the Embedded FM podcast, who you've also been on Embedded.

**Mike Stisch:** One of my favorites.

**Chris Gammell:** I enjoyed your stories about the Butter Factory. I'll leave those stories over there, so I'll point people over to that. Yeah, the Butter Factory. I'm probably not going to have many notes for this show. The Butter Factory sounds weird, but go listen to that show. That's another great interview they did with you. But me and Alicia have talked about, like, when you move outside of school, right, and specifically for her, she's a consultant. When you move outside of engineering, or even if you are an engineer and you're in a company, you're just moving up, you're 10, 15, 20-year engineer. Like, how do you learn that next thing? You don't have necessarily, you don't have a lesson, right? And so it has to be that more collaborative sit-down with other people and just kind of figure stuff out. You know, and you can pick up tips and tricks. You know, again, the music thing. So when Akiba was on the show, we always talked, he talked about breakdancing, I talked about jazz. But like that idea of like playing with people and like learning in situ like that is like a really important thing where you're replicating what others are doing and you're borrowing it and you're transforming it and moving out of that. So is that kind of what you mean with the Hackaday Prize or what?

**Mike Stisch:** Yeah, I think that when you put something out there, you're like, let's say air quality monitor. We've had a lot of air quality monitors on there. And there's going to be a lot more air quality monitors because it's not like pollution is currently looking like it's improving. Fix that one. Yeah, yeah, you know, I think the more people we have and, you know, our continued need for the lowest possible price on energy for that part of the world, it's going to continue to be a problem. And we're only recently starting to do widespread monitoring in certain parts. And those monitors tend to be, they're not cheap. They're not super expensive, but you do need a lot of them. You need to put a network together. So like having the ability to go out and say, let's look at as many examples of people who have been working on this as possible. And let's see, are there certain sensors that are really popular? Are there certain circuits designed around those that work really well? Why are those choices being made? And do we see a trend here? Do we see the same dead ends being hit? And do we need to find new technology for these? I think one of the ideals of the Hackaday Prize is that it should be an open source project. So people should be able to look at the code that you're using for it. And so what you end up with is, there's a high signal to noise ratio, but there is a place that you can go. And so you can go and find collections of example builds, example code.

**Chris Gammell:** And so do you find that people are actually making appreciable efforts towards open source projects? I mean, I think this is also maybe a hardware versus software type of thing as well, right? There's always that, well, open source hardware is a good thing, but does it actually lead to the next thing, right? And does it lead to the next project? Is there any tracking of that through the Hackaday Prize of like, oh, well, this new project started because of that old project?

**Mike Stisch:** Yeah, and actually we see it more often than you would think. You know, the one that just popped to mind is PCB motors are kind of like a big trend this year. And so I can't pull the name out of my head right now of who did the first one that I saw, but it was a little like six coils on a PCB and a little statter. Well, this was the first one that he did. So it was like a little statter that was 3D printed and had a few neodymium magnets in it. Okay. And basically, I mean, it's like a brushless motor flipped, right? So the stationary part is the coils and you can drive it. And then another person who I think his name is Bobricus.

**Chris Gammell:** Which is not, we'll try and get links later. How about that? Oh, yeah, yeah, yeah. That sounds good.

**Mike Stisch:** Instead of butchering names. Yeah, he went and he's like, you know, this is a good idea, but I think you can get more power out of it if you use like multiple sandwiches of PCBs. And then ended up like doing a proof of concept where this could be like a propulsion system for a tiny, tiny robot. And like shows it like driving across the table. And that was like a direct inspiration from the first project. And then the gentleman who did the first one then came out. Oh, it might have been Bobricus again, who had the strip of coils and a ball magnet that moves back and forth. And then there's another one that's like the coils are in a flexible PCB. And it's really wicked. And what I like about it is, you know, with Hackaday, I often say, if you ask why, it's the wrong question. I mean, really, this is like research and development. And it's waiting for, you know, the person who has the killer app to come and find it or someone to stumble upon it.

**Chris Gammell:** Yeah. Well, I think, too, I've been really intrigued by super low cost stuff recently. Right. So like Espressif is a great example of that. They didn't have a great, they still don't have a great product. Right. It's very impressive for what it is, but it's not like super well done. But like, you can't stop that. That's what I really like about it. And I think that Hackaday actually kind of gloms onto that a lot as well. Of like, oh, that was the other thing with Laura as well. Like, so a lot of the LauraWan stuff, it's just like you can't beat the price. And when you have that, you have a wide range of people who are accessible to it. They can actually purchase it. There's almost no barrier because it is so low cost. And then you get a lot of innovation just purely from that low end side of things. I'm wondering if that's also the PCB motor thing. So you're basically opening up a new market by having low cost PCB manufacturing. That you just have more creativity within that.

**Mike Stisch:** I think absolutely. I mean, we were trying for years and years to add Wi-Fi to everything. And it was really hard. Yeah, right. It was either really hard or really expensive or both. And then all of a sudden, this chip that no one had ever heard of that had a data sheet that could only be read by native Chinese speakers popped out. And everyone was like, can we get this, you know, this whole community popped up. And like got it translated. And that company has since come out with a follow-up product that a lot of people have been using. And basically Wi-Fi is a solved problem at this point.

**Chris Gammell:** Well, I wouldn't say that. But it's a hell of a lot more accessible. And it's crazy now. Also, you see that spinning. Like I saw U-Blocks uses an ESP32. And the Arduino maker uses an ESP32. And all these other things are just like, oh, the new particle mesh chip. Oh, I didn't know that. Yeah, they're using, I think they are. I think they're the one that has Wi-Fi and Bluetooth. It has a ESP32. Oh, right. And the NRF chip on it.

**Mike Stisch:** Yeah, now I remember. Because it's just so cheap.

**Chris Gammell:** You know, like, and it's like, so what happens when everything, all the cost of hardware goes down to zero?

**Mike Stisch:** Yeah, you know, like Juicero, right? You're familiar with Juicero?

**Chris Gammell:** Ben Einstein was on the show last week. We talked about it.

**Mike Stisch:** I wish that every mechanical thing was engineered like that, right? Because I love to like look at it. But the truth is, that's not what we need. That's not what we're going for. And so really, like, good enough is good enough. And with the ESP32 chip, if you're putting out something that needs a really, really beefy processor and has like, you know, just needs to be really super dependable, that's probably not the thing that you're going with.

**Chris Gammell:** Go and pay someone a lot of money to make a thing that will be very, very, like go, yeah. Right. Like the routers who are the guys that make those crazy routers.

**Mike Stisch:** But if you need, you know, something that has connectivity in it and is going to do the job in large volume at a low price, like solve the problem, right? Right.

**Chris Gammell:** Yeah, that's true. Yeah. Yeah, it's like at least a default, a default starting point. And that's kind of what, and then there might be other competitors that pop up to serve that market too.

**Mike Stisch:** Yeah, you prove your concept until you hit your constraint and you say, oh, I guess I can't do it with this. And then you go through the pain of porting your stack to something else.

**Chris Gammell:** That was a mistake. Like, yeah, that's true.

**Mike Stisch:** Maybe you should start high and go low. Right.

**Chris Gammell:** I don't know. It's curious too because that's like, well, you know, people hear me talk about the innovator's dilemma on here. That's like Clay Christensen's book that kind of talks about that a lot of the innovation comes from the bottom up. You know, like you see people, like all the car manufacturers that start with those, like Kia, right? It was a super low cost manufacturer, Honda as well. And then they just rise up from there. And I think a lot of it's just that volume of moving parts, moving stuff through, hitting safety standards, whatever. This kind of, these topics of low cost hardware and more accessible and building communities and learning from others, it kind of all leads us to badge life, which is kind of what we were talking about here. You made a badge this year. Yes. And you are a purveyor of other badges and the badge culture. So why don't you tell me what you think it is?

**Mike Stisch:** What I think badge life is. Yeah. I think badge life is the art of spending way too much time and way too much money exercising your creative demons through hardware.

**Chris Gammell:** That is a great way to say it. Especially because as someone who, I think my last count was over four figures of hardware that I put into it and didn't get anything out of it.

**Mike Stisch:** Oh, you did not. Oh, I'm into it for about $550. That's not bad. Yeah. When I told Amanda, she was surprised, but I think okay with it. I mean, it could have gone worse. It adds up. Yeah, yeah, definitely.

**Chris Gammell:** Well, and I think that people listening who are hardware people are not going to blink an eye at thousands of dollars. It's just like, why are you doing that? I think that ultimately that's the real question. Why are you doing that?

**Mike Stisch:** Yeah. So first of all, I'm doing it as a thank you to badge makers who have just given me free badges for the last four years. Right. You know, I'd like to go back to that DEF CON 22 that we were at. And you said you didn't have a great time, but I had a great time. Yeah. Like one of the first days, I just ran into these like five guys who had these big skull and crossbones, white silk screen with blinky LEDs all over it. And I was like, what is that?

**Dave Jones:** What is going on here? Yeah.

**Mike Stisch:** Yeah. Because it wasn't the official badge. You know, I'd already been playing with the official badge and it was a ton of fun. And these were the whiskey pirates. And they're like, come up to our room. And then I went up and it was like, I thought it was going to be like the Michael Scott, you know, hotel episode where you go in and it's like flashing lights. And it's like, there's a bar over there.

**Chris Gammell:** There's Apple schnapps.

**Mike Stisch:** They brought in like a stand up pay telephone. They had a stand up coin op machine. They had a complete rework stage. I mean, there's just like stuff everywhere. And they're like, do you know how to solder surface amount LEDs? And I'm like, yeah. And they're like, can you populate a few of these badges? And I'm like, sure. And so we just sat there with the music on. There were like seven or eight people like populating these badges. And I had a really great time with it and, you know, like ran an article on it. And I think like the next year I pulled it out and like did a video preview of it. And I think that's how I got connected with the Anodexor guys the next year is I did the video. And then they're like, hey, do you want to have an early look at this badge? And I would like to put in a plug here. Hackaday respects press embargoes. And we love to get our hands on awesome hardware ahead of time. So go ahead and get in.

**Chris Gammell:** Right, cuts down on anything to do at the conference, honestly.

**Mike Stisch:** Yeah, yeah. And just, you know, I don't want to be under a really tight deadline for turning around great content. So like Brian and I, Brian Benschef and I got a hold of the badge on Thursday morning. And then it was like we were standing at the circle bar down right outside of the DEF CON entrance, like on the Wi-Fi, on the cellular hotspots, like trying to get the images uploaded because the bandwidth is horrible. The spectrum is horrible. And get an article out, you know, like by 1 p.m. the day that the badges were released. I don't know, maybe I can beg DEF CON next year for an early look, but I doubt it.

**Chris Gammell:** Oh, yeah, I doubt it too. Yeah, and so, I mean, like, I've been trying to explain it, like I think on the show and just elsewhere too, and I kind of got sucked in. I don't know why I like it. I don't, I'm not sure if I like it. It's gotten, it's, there's money involved now. Yeah. And I think that there's been pushback from people like, oh, well, people are like making tons of money on it. It's like, it's like, it's like the lowest paid work you can pretty much do.

**Mike Stisch:** Yeah, I think that's revenue. Like they're making tons of revenue on it. Exactly, yeah. That is the confusion.

**Chris Gammell:** There's, yeah, so like, and it's, I think the reason I like it is that I get to talk to people who are doing low volume manufacturing, who are doing it coming from different spots or coming from the software world often. They're doing creative things for no good reason, right? And, but like, there's some really cool things in there, right? There's, I mean, we've seen some of the things, well, I'm sure that people can go and read your articles about DEF CON and the badges that are there. But there's just creativity and it's kind of just for funsies, you know?

**Mike Stisch:** Yeah, and I had, I had been involved with the Hackaday badges for conferences for the last few years. But it was mostly, yeah, but it's mostly like a herding cats. I think you had, you were much more into the hardware, like sourcing. I was helping. Dealing with sourcing problems. Like, I didn't really deal with any of the sourcing problems. I didn't deal with the hardware design stuff. I like ported some games and, you know, maybe did some menus. And so I was like, you know what? I kind of want to do all of that. So this year on like July 1st, I'm like, you know what? I have a couple hours. It's a Sunday afternoon. I have an idea. Let's lay out a circuit and see where it goes. And then it was mayhem for like the next three weeks. And, you know.

**Chris Gammell:** And beyond.

**Mike Stisch:** Yeah. Amanda would go to bed at like 1030 and I'd be like, oh, I'll be there in like an hour. And then like five hours later, I'd be like, oh, it's 3.30 in the morning. Let me put this PCB order in before I go to bed. Yeah. But, you know, despite that, it was a ton of fun. And like just encountering, I really like encountering new problems and new puzzles in that. And then also like learning the stuff that I should have learned before like PCB or plane stitching, via stitching in KiCad, which I ended up finding your tutorial. And then I was like, it's 3 in the morning. I'm not following this guide. I'm doing it the wrong way. But I hear that's fixed in KiCad 5. And 5.5. Yeah.

**Chris Gammell:** It's a new thing.

**Mike Stisch:** Yeah. So I'm excited about that. I routed buttons wrong. So I routed to the two permanently connected parts of the momentary push switch. Oh, geez. Yeah. And other than that, I didn't make any PCB errors. That's good. I was so... Well, let's talk about the badge real quick. Oh, yeah. So like what is your badge? My badge is called the coin-op badge. It's whenever I see Galaga or Galaga, as some people say, I have this visceral reaction. My brain just goes, you should go play that. Like it's a totally fun game. Do you have any quarters on you? Yeah. You have quarters.

**Chris Gammell:** We could do this. We got time.

**Mike Stisch:** So I was like, you know, I kind of wanted to do this shit from Galaga. Because it's awesome. Yeah. And it's also... I don't have great art chops. And so it's just pixels. And I can definitely do just pixels. Blocky. Yeah. Looks like a ship. Yeah. Yeah. And so I'm like, all right. I looked it up. It's mostly white. It's got some red and blue on there. I'm like, perfect. I'll do white solder mask and then put red and blue LEDs on there. I designed the circuit first and then picked out footprints based on... I wanted a TQFP that was at least 32 pins. And so that set the size for the badge. I think each pixel is six millimeters on it. It ends up being 90 millimeters by 96 millimeters. It's got the cutouts for it. And then just runs off of a coin cell on the back, which is the other part of the coin op play on words. Yeah. That's great.

**Chris Gammell:** That's awesome. Yeah. And it's... Well, you said it's at mega, right?

**Mike Stisch:** Yeah. So I went on DigiKey and just narrowed things down by that TQFP so I could solder it. I got it. And then 32 pins because I wanted direct drive. I wanted 32 pins or more. Oh, I see. To get that number of abilities. Yeah. And so I found an at mega 48 that's automotive and the skew is obsolete. So I got the parts for 52 cents a piece. Nice. Which was one mistake that I made because the 4K of programming space ran out pretty quickly. And I think I could have done with a little more speed than the 8 megahertz internal oscillator. So I think if I were to do it again, I would have paid a dollar more per board. I made 59 of them. So we're talking about a $60 choice to not have dealt with programming space, which bit me a couple times. Right.

**Chris Gammell:** But maybe it also saved you. You're like, all right, well, you get to the end. You can only do so much with the programming. You're like, I'm done.

**Mike Stisch:** Yeah, there are some things. I'm really proud of my power down sequence, which puts it into low power sleep mode. I measured it at like 0.1 microamps.

**Chris Gammell:** Are you going to post a video of it anywhere, maybe?

**Mike Stisch:** Oh, yeah. I have a time lapse of the assembly process, too, which I think is pretty cool. Okay. I did record it like me speaking about the features and stuff, but I haven't edited yet. Okay. Maybe by the time. Yeah.

**Chris Gammell:** We'll get it up eventually.

**Mike Stisch:** Yeah. But what were we talking about? Oh, the low power sleep mode had a bug. So when the badge is asleep, it's looking for a pin change interrupt. I have pull down resistors, and then the buttons are connected to VCC so that you're not burning a pull up resistor while it's off. Yep. And the AVRs don't have a pull down resistor internally like an arm would. Yeah. So, but when you first press that, I don't want it so that if you put it in your bag, it's just going to turn on. So there's like a confirmation power-up sequence, and it's a while one loop. And it's just looking for a button up or a button repeat from the debounce sequence. Right. And it appears in the first rev of firmware, I'd somehow get into that loop. So I think maybe static electricity was causing a pin change interrupt, or something. You know, it's hard to replicate this, but it would be like...

**Chris Gammell:** You need to make a bag testing chamber.

**Mike Stisch:** Well, it's like when you set it on a desk, I can't get it to happen, but when I put it on a lanyard room and I can walk around, it happens. And the problem is when I went to fix the bug, I was out of program space. So I had to optimize my code to fit the bug fix on there. But I also would have had time to do things like when you first put the battery in, it should give you an indication of what rev of the firmware you have, and I didn't have room for that. You know, that kind of stuff. Right.

**Chris Gammell:** So that's the thing I really like about the projects you do. You like these low, low level. You like getting in the registers. You like writing all that low-level firmware. I remember the 1-bit Pac-Man. That was a favorite of mine that you did.

**Mike Stisch:** That one wasn't very low, though. So 1-pixel Pac-Man was fun. The low thing you're thinking on that is I looked at cell phones. I'm like, no one can beat a cell phone screen. It's just so amazing. So I'm like, if you're going to build a project and put a crappy little 2.4-inch TFT that's not very bright on there, everyone's going to be like, this thing sucks compared to my cell phone. But then that smart matrix came out, which was using those commodity panels, 32 by 32 RGB LEDs run by a TNC 3.2, which is Paul Stoffergen's board that has a ton of great DMA code for driving those LEDs. And I'm like, huh, I wonder how many tiles classic coin-op games have. And so Pac-Man has less than 32 by 32. It's like 30 by 26 or something. Oh, really? Oh, wow. Yeah. And so I'm like, the entire Pac-Man game can be represented on this if you just don't make the sprites. Don't add detail. Yeah. And so, you know, like the walls are a blue dot. Yep. And the pips are like a white dot and Pac-Man's yellow and the ghosts.

**Chris Gammell:** I never noticed what they're called.

**Mike Stisch:** The pips are the things you eat. I think they're called pips. Oh, I didn't know. Well, it's like what's on a die, right? Pips on a die. Maybe they're pellets because the big ones are power pellets.

**Chris Gammell:** Oh, okay. I'm not like arguing any of these things. I just didn't know.

**Mike Stisch:** So this might be getting a little too far off of Amp Hour Fair, but the AI in Pac-Man is fantastic. So it's moved around like the website got bought, but there's something called the Pac-Man dossier. And it's got the reverse engineered rules of all the AI from the original ROM. Right. And it's fascinating and it totally ruins the game for you. Right.

**Chris Gammell:** Because you then start to see the code, right? Yeah. Yeah.

**Mike Stisch:** But it like...

**Chris Gammell:** Well, it's done with like logic chips though, right?

**Mike Stisch:** Yeah. And so what it is is each ghost, every time they get to an intersection, is making a choice on whether they should turn right, left, or go straight. And then what they're trying to do is get...

**Chris Gammell:** Wait, we should say spoilers. So if you're a big Pac-Man aficionado... Yeah.

**Mike Stisch:** Don't listen to this next part. Right, right. But they basically just set a coordinate that the ghost is trying to get to. And it says, if I turn left or right or go straight, is it going to be the shortest route? Yeah. And then in order to make them look like they're actually doing something, when they're chasing after you, some of them are like...

**Chris Gammell:** It's based on the color, right? Yeah. Blinky.

**Mike Stisch:** Pinky, Pinky, Blinky, and Bartholomew. I'm pretty sure it is. So I think it's Dot. I think the last one's Dot. But you know, like the red one, Blinky, let's say, is actually chasing you. But another one is chasing like five points in front of you. And another one is chasing like the reflected angle of you and stuff. Like really simple math tricks. But when you stack them all together, it becomes like a really interesting thing that tricks your brain into thinking you're seeing intelligent behavior.

**Chris Gammell:** Yeah, right, right, right. Yeah, algorithms and stuff.

**Mike Stisch:** Yeah, that was a really fun project. The only thing I didn't get to do was add music. Oh, right. And that would have been perfect. Some day. Still time. Yeah. Still time.

**Dave Jones:** Yeah, yeah, add it to the bucket list. Yeah, right, of course.

**Chris Gammell:** Just add it to the bucket.

**Mike Stisch:** Yeah, that one was frustrating because, you know, the libraries for the screen were already in place and they're using the Arduino IDE. And I like to write in C and I have like libraries of things that I go back to in C. And it's a real pain in the butt to include your C files in like a multi-file Arduino project. Yeah, right, right, right. And I recently did it again. And I had built a blinky hat for DEFCON 22, the first one that we went to. That was the hackable hat, right? Yeah. And I actually brought it into my hotel room. Oh, really? I haven't busted it out yet. But that was like WS-2812 strips and I built it in a super short period of time. And I needed connectivity to a real small Wi-Fi router. And so I ended up going with an Arduino board because it's got USB and you can plug it into a router. Router's running, open wart, which has like Linux so you can like cat or echo commands to the board. And I went to like build a new version of that hat this year because LED technology has come so far. And so I started writing the software before these flexible LED panels came. I got 8 by 16 RGB LED panels. I got four of them. So a thousand of these great super bright LEDs for like 80 bucks delivered. It was amazing. Yeah. Yeah. So I got these panels to make a new hat. And so I started to pull that software out again. And I went through like the exact same problems I had had before with putting libraries into it.

**Chris Gammell:** Again, this is Arduino IDE.

**Mike Stisch:** Yeah. So with this hat, it's so many LEDs that I don't want to deal with having to push out the communications. And the price was because these are 2812s. They weren't the APA 102s, which I think are a little more fun to work with. And so I wanted, Paul has another library, Paul Stopprogen, the TT 3.6 has a library called Octo2812, I believe, that's using, again, DMA to push out basically a frame buffer to these. So you don't have to deal with the speed problems that you would normally have. It's a really good way to write for it. The problem that I ran into is I didn't think about quiescent current. Oh, yeah. And it's like 900 milliamps when all of these are off. And I... When they're off? Yeah, yeah. When you're not even showing any LEDs. It's 1,000 LEDs. It'd be cut down, I think, to like 880 for the circumference of the hat.

**Dave Jones:** Right, right, right.

**Mike Stisch:** But I really believe if you're going to build a blinky hat to wear around, everything's got to be inside the hat. You can't have like a cord going down to your backpack. It ruins it. You might as well make a backpack that's got lights on it.

**Chris Gammell:** Right, and then it looks like a Ghostbuster pack.

**Mike Stisch:** Yeah, so then I started looking into how I'm going to supply current for this whole thing. And I'm looking at drone batteries and how I'm going to regulate that. And I'm like, I might need active cooling.

**Chris Gammell:** You're going to need a sprinkler system for when your hat starts on fire.

**Mike Stisch:** Yeah, I'm like, I don't want to burn my hair off. And then, of course, if you have active cooling, it means you have a fan. I'm like, if you have a hat with a fan in it, you need a smoke machine. Because you've got to have smoke coming out of it.

**Chris Gammell:** And this is how it all starts.

**Mike Stisch:** Yeah, so maybe next year, that's when I kind of like swapped priorities and started with the badge.

**Chris Gammell:** You could do like a vaping people. You could get some vape fluid.

**Mike Stisch:** Huh, actually, that's a really good idea for a smoke machine is to break down a vaporizer. Yeah, have you seen that done before?

**Chris Gammell:** No, I was just thinking. That's where you see tons of smoke these days, especially so I'm not used to Vegas style. Like, everybody's smoking. Everybody's using vape stuff. And it's just like, oh, my God.

**Mike Stisch:** Yeah, I don't know if it's a Vegas thing or a DEF CON thing.

**Chris Gammell:** Maybe it's just whatever the crowd is. I don't know. I'm not around that much.

**Mike Stisch:** Yeah, but that would be a great source because it's already portable power supply, portable heating element. Might be a little battery. Yeah. Huh, well, thank you.

**Chris Gammell:** Let's talk about the, so you mentioned the Arduino IDE. And, I mean, you are, you're interested in the low-level C stuff. Anyways, this is a topic that comes up on Hackaday a lot of like Arduino. And, like, you know, like, it's kind of like when you welcome people in the community and stuff, too. It's like sometimes there's pushback on that stuff. I mean, what do you see as the editor of Hackaday of, you know, around that? You know, you're pushing out articles all the time of somewhere between beginner and advanced and, like, you know, how people react. And we don't need to talk about the comment section, but, you know.

**Mike Stisch:** Well, I think just generally as an editor, it's great because it kind of gives people a thing that they can look for. Like, if you're, like, getting into Embedded and you're like, oh, which chip do I use? You know, like, the Arduino name is, it's a brand, it's a movement, it's, you know, it's a compatible, a compatibility layer. That's true. You know, it's kind of like a catch-all that means, like, blinking stuff with a microcontroller.

**Chris Gammell:** It's simpler than it would be otherwise, right?

**Mike Stisch:** Yeah, and so I think it's a really good way to kind of just say this is the kind of general cloud of topics that's going to be discussed in this article or, you know, this set of articles. So I think that's really good because people who don't know what they don't know can actually find their way in. Whereas if you run an article that's like, you know.

**Chris Gammell:** SGM-32, F4-0, right? Yeah. F4-0-1, right?

**Mike Stisch:** Yeah, exactly. And actually what we've seen is, like, the ESP8266 is, like, the same sort of thing. So we have a lot of people that are coming in, you know, like, looking for, like, okay, I have this thing. I got it to do one specific thing. What else can I do? And that's one of the places that people use Hackaday a ton is, like, the kind of, like, new ideas and, like, things that didn't work but were kind of cool. Right. You can often unearth them there. Yeah.

**Chris Gammell:** So it's almost like the memetic thing again. It's like you're kind of just following these, the scent of, like, well, maybe this is next, maybe that's next, this is of interest, that kind of thing.

**Mike Stisch:** Yeah, I really think the badge life thing is kind of indicating the next thing. And I compare it to Arduino. Oh, that's interesting. So, like, Arduino, before Arduino came along, kind of the precursor to Arduino is, like, programmers and compilers started becoming more widely available. And so you started to have this influx of people that were, like, actually doing things. Like, for instance, you know, a guy with a couple of music degrees playing in two orchestras, Mike Stish, was like, hey, I want to try to program some microcontrollers. Oh, I can afford some ATT 13s. Right. And then I can build a DAPA programming cable with, like, two resistors and some ribbon cable. Yeah. And that's actually how I started. And I, like, immediately bricked one of those chips and then, you know, like, six months later ordered a proper programmer. Right. But it's, like, that path where it was accessible, the information was there, the tools were pretty cheap, was open to me. Yeah. So I think with badge life, especially this year, they have the add-on standard, which is called the shitty add-on standard, which is unfortunate. But... Silly add-on standard. Yeah, yeah, yeah. I'm going to do the superb add-on standard for next year. Right, right. But I think that that is, people who are, like, looking at badges and are, like, I really want to do that. I don't have time to build a big puzzle and, you know, like, figure out the protocol for, like, a parallel TFT display and stuff like that. Can be like, oh, no, I'm just going to make a creative badge and lay it out as a circuit board and solder on some parts. And that gives them the, you know, the skill of, like, what does it take to export Gerber files? And how do you find the fad that you're going to have doing it? Yeah, right. Yeah, how do you make sure you get your footprints on the right side of the board with the right orientation?

**Chris Gammell:** Again, easier in 5.0. We'll see. And actually, a ton of... I've been really happy, too, and I think this might be another reason that I'm particularly biased for badge life stuff is, like, a lot of KiCAD users, it's great.

**Mike Stisch:** I'm a KiCAD person myself. People can use whatever they want, but it does make me feel good to see people giving it a try. Yeah, exactly. But, you know, it's, like, people might decide after they've used KiCAD, like, they just download it because it's available right now, that, like, oh, I've heard about, you know, Eagle or Circuit Studio or Altium as a big beginner tool, I hear. Yeah, right.

**Chris Gammell:** It's had this pile of money sitting around.

**Mike Stisch:** Yeah, I don't really care what people use. I think it's gatekeeping. So you're asking about, like, what do people think about Arduino? So the people that don't know, on Hackaday for years, we'd run an Arduino project and people would be like, ah, Arduino. I don't particularly care for the IDE, but, you know, I don't care for any IDE. I generally like to use a text editor and type make into the command line. Oh, man, he's one of those. I am sometimes and I'm not other times. Like, I use the MP Lab for the Hackaday badges. That's a PIC32. And, like, that comes with its own set of problems. Sure, of course. But it allows you to do things like navigate by function, which if you're just scrolling in a text editor, once you get to about a thousand lines, that gets old really quick.

**Chris Gammell:** So I just had something pop in my head of, like, Mr. Meeseeks, like, screaming, like, technology is pain. Everything is pain, Mr. Meeseeks. Right, yeah. I mean, that's what it comes down to, though. It's like, so I, and I, and that's what made me switch over, you know, the, from being not, not a Hackaday commenter, but a, you know, someone who was like, oh, whatever. But it's like, you know, whatever works, you know, just get more people in the door. That's all that matters, you know. And I think that that's good for Badge Life and Defcon and all this stuff and just seeing where it happens.

**Mike Stisch:** Yeah, and with everything, you know, we're talking about the Hackaday Prize before. And I look at the projects that are coming in and I look at some of the really young competitors, anyone that's 13 years old or older can enter. And I'm like, what's going to happen when these people are, like, 30 years old and start to, like, run engineering teams? Like, it is so incredible. You think it'll take that long? Yeah, I mean, they're probably founding companies. You had Sam on, Sam Zalouf, right? And so Sam Zalouf's the guy who did lithographically produced integrated circuit, like, in his garage, basically. And I'm like, the fact that you can go out and get enough, like, used equipment and enough knowledge and, like, access to the chemicals. And then the fact that we have this structure set up to, like, celebrate these people on the Amp Hour or on Hackaday or, you know, anywhere. Just generally YouTube as well, right? It is just a great time to be alive. A lot.

**Chris Gammell:** I mean, let's just say it like it is. There's a lot of crap on the Internet, right? There's a lot of bad stuff out there these days. However, I think that, yeah, like, this is the shining light kind of stuff of, like, makers like Sam and just people doing Ben Krasnow. Someone I always hold up is, like, where the hell that guy got from? You know, like... Yeah. And, you know, it's just great, though, right? And it's... I think that usually my first reaction is, I'm not doing enough. I'm not doing... You know, like... Yeah. Like, that kind of, like, stress of, like, oh, man. But, like, once you get past that, I think, when you, like, really just start to, like, be like, oh, that's awesome. You know, if you can just have that, oh, that's awesome reaction and then be like, I wonder if I can use that. You know, stick that in the library of your brain and then pull it back out and go back to the Hackaday article later. That's really helpful, I think.

**Mike Stisch:** Yeah, I think a few things about that. I mean, first of all, you're always watching someone else's highlight reel. Of course. Yeah. That's a great reminder. It is. It's really tough. My brain has trouble, like, learning that lesson. And I often compare myself to the snippets I see of Ben Krasnow. But... Yeah.

**Chris Gammell:** But also, like, bad life, too, right? We see a lot of people that are just, like, selling these finished pieces of art that are, like, you know, and they're just, hey, it's this thing. It's like, the Bender badge is... And that XOR, the DC26 Bender badge, which is amazing art and all that stuff. And we talk to the team, we know them. Like, that's six people doing... Like, I, you know, I've talked to them at one, two in the morning.

**Mike Stisch:** Yeah. It's a lot of work. So, yeah. Yeah, I'd encourage people to go look at my review of that badge for this year because I psychoanalyze the team based on the art that they've done for their badges over the last three years.

**Chris Gammell:** Oh, that's right. You said the progression is things get more worn out, right?

**Mike Stisch:** Yeah, like, half of Bender's face is, like, falling off at this point. I'm like, that's the stress of badge life. Right. But, I mean, really, they have... So, you mentioned before there's a lot of money in it. So, there's a lot of money in it for people who are making a lot of badges. Like, it costs a lot to, you know, order that many components. Right. It costs a lot to... A lot of cash flow. Yeah, to set up a contract manufacturer and that sort of thing. I believe their Kickstarter was $47,000. There's a lot of accountability there. Yeah. And, you know, if you have... I don't know how many they had. Let's say they brought 400 badges to the conference or whatever. Like, you have to sell those. Yeah. Like, there's a lot of inventory locked up there. I don't want that at all. Exactly.

**Chris Gammell:** Yeah. Well, and that's the other thing is that, like, so, you know, knowing the people we do, like, some people are here, like, working the whole time. And, like... And so, I will give the update on my badge. My badge, I didn't finish it. I didn't... I mean, I got the hardware done. Mike and we should talk about the assembly piece, right? Yeah. Yeah, that was good. But, I just didn't get to the firmware in time. I had a lot of stuff going on. It's like... Nope. And... But, I could have been sitting in my room writing code the whole time. I don't want to do that. Right? Or, I could have been sitting and soldering the whole time. I don't want to do that. I want to meet people.

**Mike Stisch:** Chris at the bar just before dinner last night. And, he had this badge out. And, I'm like, hey, Chris, you know, like, is it blinking? And, he said, no. And, I'm like, well, you know, like, show me your code. I'll write some visualizations for you. I bet I can do that right now. It'd be great. And, I said, do you have a heartbeat yet? I just... No. No heartbeat at all on that badge. I think that's awesome. It's a cradle death. Yeah. But, you have an LED driver on your badge. It is a Charlie Plexed LED driver, right? Yeah. So, my number one tip on a situation like that is always connect a single LED to a single pin. So, you can get your one-bit debugging code out of that. That's good. Because, getting the protocols on those chips up and running, I don't want to... A lot of libraries. Yeah. I don't want to be analyzing the signals with an oscilloscope unless I absolutely have to. I just want to, you know, get some iteration and be like, am I sending one I think I'm sending? Right. And that sort of stuff. Yeah. But, yeah, I think that there... By and large, it's a small number of people who are doing a huge number of badges. Yeah. And I think that the community spirit is still really strong and still growing of, let's do something creative. You know, I set out to do 59 badges. Like, I gave away half of them to people, like, almost within the first two days. Because, oftentimes, they're like, yeah, here you have my badge. Like, just kind of showing off, you know, what you were able to build and, like, telling those stories about routing the buttons wrong or making... Right. You know, not being able to do a fix in your power down because you don't have code space. Right. And just kind of hearing what went wrong with other people's badges and then, like, where that inspiration for each of them came from. Yeah.

**Chris Gammell:** Trading stories, that kind of thing. Yeah. Well, and you were super generous and you came to Chicago on a weekend and helped me to relearn the Pick and Place together. So, the Neo Den 4 Pick and Place that's out of my workspace, that was one of my goals for, like, doing all this and having a god awful amount of LEDs is to learn that process, right?

**Mike Stisch:** Oh, yeah. And I'm glad you did. You know, I kind of had this epiphany earlier in the year that I'm like, I've always thought to myself I'd love to be an embedded engineer. And I think I was talking to you and you were like, well, why don't you spend some time and, like, get some of the skills that you've never done before? Right, right. So, when you said you were going to do Pick and Place, I'm like, I'd love to come down and see that. I've never been involved in a Pick and Place process before. And do you see that thing's about $10,000?

**Chris Gammell:** Yeah, about $10,000.

**Mike Stisch:** It's, again, just like this whole thing of, like, the next thing is availability and manufacturing. Right. I mean...

**Chris Gammell:** I think there's another one that, I forget the name of it, but there's another one that came out. And SparkFun has, I think Nathan from SparkFun has one. And a couple other people I mentioned, talked to here, have them now. Really low cost, you know, like, $3,000. Wow. Pick and Place. And it's, yeah. So, that's another one that's, like, again, like, so we've, me and Dave have talked about it on the show a lot of, like, should you have a Pick and Place? There was a Joe Menard talk at HDDG, which is a supply frame thing that I point people to a lot of, like, don't do Pick and Place, right? But I think at the end of the day, the accessibility of electronics in general, specifically Badge Life but other things as well, it's like, well, maybe it is getting to the point where if there's a market for it, if you have the need to make enough stuff, maybe it is worth the time to do your own things.

**Mike Stisch:** Well, I think you have it figured out. So, what you should do, if you can, is find a co-working space that has one.

**Chris Gammell:** Oh, yeah, versus buying your own. Yeah, totally.

**Mike Stisch:** Yeah, and spec it out. Also, that lets you figure out if you want to get the $10,000 one or if you want to get a one. Right, right.

**Chris Gammell:** Right, as your business grows and you want to build your own.

**Mike Stisch:** Yeah, but I've got to say, when we turn that machine on and it starts moving around, it's like, whoa. Yeah. It's just amazing. And, you know, like, I know from having looked at it before that they have a downward-pointing camera and an upward-pointing camera. But until you actually see it on the screen and you're, like, clicking around to move it. Yeah, right, right, right. Probably the most delightful thing was we put a test capacitor on and it, like, we had the offset wrong and it tried to put it in a mounting hole. Right. And so we had this capacitor, like, on end in the mounting hole showing on the, like, macro view. Right, right. You have, like, that was so awesome. Yeah. We did get it working. We did.

**Chris Gammell:** Yeah, yeah, yeah.

**Mike Stisch:** Six hours and almost lost our lives to lithium.

**Chris Gammell:** Oh, yeah, yeah, that's true. Lithium battery. I don't know if I mentioned them on the show yet. I had a, we had a battery go off, right? Not we. Someone. We didn't do it. But, yeah, someone was working on lithium-ion batteries while we were trying to get this thing done. We were already stressing that. And someone punctured a link to the lithium-ion. They were closing a case, which had it. And this thing started sparking and letting off, and off-gassing and just scaring. It was like a Roman candle. It was like. It scared the shit out of me. Yeah. I had not run. And I think I told you this, too. I've never run for my life before. That was the first time I've ever run for my life.

**Mike Stisch:** You have good instincts, Chris. I. Actually, you don't, because you said you froze, right?

**Chris Gammell:** I first froze, and then I. You don't know what it is at first.

**Mike Stisch:** No, I thought that they. I thought it was like. I thought it was a joke. Compression. Compressed to error. Yeah, right. And then I saw the, like, the Roman candle, and I'm like, is someone grinding? And I'm like, no, this is bad. Right, right, right. Yeah. Yeah. Danger will happen. Danger.

**Chris Gammell:** Yeah, right.

**Mike Stisch:** Yeah. Yeah. But using the pick and place, I thought. The company had YouTube video tutorials, which were.

**Chris Gammell:** We're not bad, right?

**Mike Stisch:** No, they, like, walked through the parts that you needed to walk through.

**Chris Gammell:** That's okay. What's up? Of course, yeah. Yeah. Yeah.

**Speaker ?:** Sorry.

**Chris Gammell:** That's okay.

**Mike Stisch:** The company that makes the Neoden 4 had tutorial videos. Yeah. And they basically had the parts that you needed to do shown off pretty well. They didn't go into every detail. Right. And that became really an issue with the offsets. Like, we got the file format for it figured out pretty quickly.

**Chris Gammell:** Right. So you wrote a Python script, and I'll be posting. Well, we'll post that somewhere. But I ended up going back and making a video to show that. Like, at some point, you just need, like, a start to finish. Just show me how you're doing it. And that's what I ended up recording, and hopefully I'll have that out. But, uh...

**Mike Stisch:** Yeah, like, KiCad will kick out everything you need in a position file, POS file. Right, right. But it's not in the... Yeah. It's not in the format that the Neoden... Is it Neoden? It's Neoden. It's not in the format that the Neoden needs. And there was weird stuff. We found, like, a blogspot page from, like, last year or something.

**Chris Gammell:** Yeah, you're plumbing the depth to the internet just to see what Google's found.

**Mike Stisch:** Yeah, and that was the one that told us that KiCad does 0 to 359 degree rotation, but the Neoden does negative 180 to 180. Right. And when you load your file, and it needs to be a CSV, when you load it in, it won't give you any error. It just won't do anything. Right.

**Chris Gammell:** That is... So we should also mention, like, so, like, the tutorials were okay. They really were. And a lot of people said they've also gotten it working from that. But, honestly, I think the hardest thing is that this was a panelized design. And so taking it from one board, which I think is how a lot of people use it, you know, they secure the board down, then they do it from there to the final working thing. That's where the translation didn't happen. I think also a lot of people come from Eagle, and there was a UOP script that helped with that. So just kind of a... At the end of the day, you're translating to this end format and not the other way around. Yeah. So... Yeah. So that script was good. You wrote... Ultimately, I think the thing that we finally figured out, like, in the eighth hour and the ninth hour of working on this thing was the... Everything is... Let's see. So everything is referred to that first component that's on your list. And that's how they show it, at least in the videos. But then it was all about, like, you had to then give a relative measure to where your fiducials were. And that's the thing we could not figure out. Ultimately, that was from looking at someone else's files who had already used it. That's what helped.

**Mike Stisch:** And you have to do that in KiCad. Yes. So you have to set the origin in KiCad to match what that offset is going to be to the first component on your list. Yeah.

**Chris Gammell:** Yeah. Right. Right. So if I had... So I had the first... It was like R1 was the first component. Or D1, I guess it was, because it was a diode. So D1 was the first component out of this, you know, huge array of LEDs that I was doing. And then it was like, that was 0, 0. Everything was referenced to 0, 0. So, like, D2 was at, you know, 4 millimeters over, 1 millimeter down. And then you also had to say, from 0, 0, where is the fiducial? The fiducial is over 60 millimeters to the right and 50 millimeters down. It would go and find that. It was like a circle. And then it would recognize that. And that's how it knew where everything was. Because there was 4 per panel.

**Mike Stisch:** And they show you in those tutorials, like, how to set that fiducial. But they don't make the connection on what the importance of that is. And, like, the labels on the interface do not make that clear.

**Chris Gammell:** And it's all... That's... The fiducial is a... I think the thing that tripped me up most is that the fiducials are a relative measure. So, it's going from 0, 0 to the fiducial on a single PCB on the panel. But the thing is, you could go and seek for it. So, like, one of the functions of a Neodend is you can click, turns on the camera, and you can go and seek it around. Then it becomes an absolute... You know, within this 400 by 400 millimeter space, you can then give it a coordinate. And that is not the way to do it. That's not what you want to do.

**Mike Stisch:** But we got it working. And it worked great. The one thing that we didn't do is center the camera on the tray of LEDs. So, there's a void on the LEDs. And you said that became a problem with the bottom of the board.

**Chris Gammell:** Bottom of the board was totally... Actually, a totally different problem. So, the nice thing... And the reason that I think this is a really good candidate for if other people are doing it... If you're doing an array of LEDs, it's all the same component, right? If you're doing... I did three picks, three places, three picks, three places, three picks... And that went pretty fast. On the backside, now you have lots of different components. It was not calibrated for the different types of components. So, it had resistors, capacitors, all these different things. And then the pick heights were different. These are... I mean, we're literally repeating... Like, we talked about education before, right? We're just trying to pass on the things that have already been learned. People are probably listening. They're like, well, why don't you just use the manual... Whatever. It's like, well, we're trying this new super low-cost thing.

**Mike Stisch:** But I got to go back to the Arduino example again. Like, embedded programming and then Arduino meant... Like, there's this wealth of knowledge that all of a sudden became available.

**Dave Jones:** Right.

**Mike Stisch:** So, if you're making a video about this and you're posting, you know, a script that we had used... Yeah. And then we found the Blogspot article. We're just like in the very trickle of information. And then at $10,000, it's kind of like the expressive thing. This is not the best pick-and-place by any means. No. Right. But you know what? If you're in the badge life and you're just trying to get, you know, 200 of your boards, you know, populated or...

**Chris Gammell:** Yeah. Well, I think the big thing is that... So, like, out of this whole experience, I learned to pick-and-place. But the other thing that I've said coming out of this is there's no reason for me never to panelize again. Right? I will always panelize boards from now on because why wouldn't I? Right? And just... At least I have that option. And if I don't, then I'm just putting my own parts onto a ridiculously large board. But who cares, right? And, like, that just changes my working flow. And that's something I've learned out of this as well. I don't know if you would do the same.

**Mike Stisch:** Oh, well, since I know you and I can drive a couple hours down to Chicago, I'm definitely going to panelize if I can...

**Chris Gammell:** I mean, so, yeah, so, like, as a comparison, right, you said you got, what was it, four boards done in how much time?

**Mike Stisch:** 90 minutes. Right. And that's placing by hand with a, you know, hacked aquarium pump. Right.

**Chris Gammell:** And you made 60, so that's at least, so it's, like, 15 times 90 minutes. That's, like, 45 hours, right? No?

**Mike Stisch:** I think, like, 22 hours. 22 and a half hours, right, yeah. At some point, I realized I had 22 hours of assembly ahead of me, so somewhere around there.

**Chris Gammell:** And that's in a good time, right? Yeah. And so, like, if you could go and drive for three hours, two hours?

**Mike Stisch:** Two hours, yeah, and run all the boards. But also, like, I'm doing it in a toaster oven that doesn't have, like, a PID controller on it. Flows and right. Yeah, and you at M-Hub had the pizza oven. It's a solder oven, but it, like, conveyor is like a pizza oven.

**Chris Gammell:** It does look like it, yeah.

**Mike Stisch:** And that just did a great job of cooking those boards. This is the first time I've used a solder stencil. Oh, yeah, okay. And I didn't, I just did whatever Kaikad spit out, and I had these really tiny 16-pin resistor arrays that are 1506 parts, and it bridged 100% of those. Yeah, right, you've done a lot of work. Yeah, in my time-lapse assembly, you can see me with a solder wick on every board in the flux, and then cleaning the flux off, and grinding my teeth the whole time.

**Chris Gammell:** Yeah, so it's been interesting, kind of, like, so, like, you're talking about the pain of learning, I'm talking about the pain of learning. And some people kind of skip that step, again, limiting it to the badge life crowd. Like, some of them went straight to assembly, and I think that might have been the right move for a lot of people. It's like, you just skip that step, and...

**Mike Stisch:** Let's step back. There's still pain in going straight to assembly. That's true, that's true. Come on. Yeah.

**Chris Gammell:** Yeah. But I think in all these cases, right, it's all about that learning that next step, because the real thing I learned is, you know, manufacturing sucks. Like, I've always known that, you know, it just, it does, it still sucks. And it's, every time someone's like, I think someone, I was talking to someone here at DEF CON, they're like, yeah, I brought a Volterra printer. Remember those?

**Mike Stisch:** Yeah. That was huge when you were at CES. Yeah, right. Like, it was the, it was the sweetheart.

**Chris Gammell:** Yeah. It's like, it's cool, but like, yeah. Anyways, I think that that was like an attempt to solve the same problems, but it didn't, you know, like, it's, there still isn't, you know, if, if it was going to get easier, it would have gotten easier already. And so, there's still a lot of manufacturing issues, and just making things is hard, right? And even making stuff is hard, right? I mean...

**Mike Stisch:** I just wanted to know the stuff that you're not going to learn reading a recount of it, you know, like, until you actually, like... That's a good point. Yeah. Until you burn your fingers on the solder wick, you know, 59 times. Yeah, right. You don't really know why you don't want to manually rework bridged components if you can avoid it. Right.

**Chris Gammell:** But that's not something where you would consider again, well, before you make your next board?

**Mike Stisch:** Well, to tell you the truth, so I ordered 15 boards, and I ordered another 40 boards, and I ended up getting 59 boards total. But if I had, if I hadn't had to, like, redo all the traces, I would have put a larger package on, on those other 40 boards. Ah. But at that point, I'm like, well, if, if none of these get assembled, it's fine. I don't have time right now. I kind of front-weighted my, my design process. So, I think in about 10 days, I was staying up, like, till 2 or 3 in the morning, like, every night. Yeah, yeah. Working on firmware, because I did have a, I did have an Amega 328 on hand that I could prototype with, and then, and then go to the other chip. But once I went, once I had the first set of boards, and I knew that it worked, I didn't really want to do, like, part changes for the other side. Yeah, right, right, right. Not just because of assembly time, but because I couldn't have done a third spin of boards before DEF CON. Right, right.

**Chris Gammell:** Time ran out.

**Mike Stisch:** Yeah.

**Chris Gammell:** Yeah, makes sense. Well, what about other, I guess, I mean, this is, this is not one of the short episodes, like I did a tour camp. This is, obviously, this is pushing now already. But what are some of the other, you know, you mentioned that, like, the stuff that we see in badge life now will be, are trends that are already in process, right? Yeah. So, what are, you know, you as someone who has to cover all these things as well, what are some of the trends you're seeing?

**Mike Stisch:** Oh, geez, that's a, that's a question to put me on the spot, isn't it?

**Chris Gammell:** I can start you off. Yeah, please do. I saw ESP32s everywhere. You as well? I mean, I don't know. I saw, at least of the badges I've seen, it's 10, at least. Yeah. Why do you think that is? Cheap processing. I would know this because I put that on mine. So, like, I don't care about Wi-Fi. I don't care. Someone, like, left me a message, like, you know, you have Wi-Fi on your thing. I'm like, I'm going to turn it off. You know, like, it's $6 for a module that, like, is done. And then if I wanted to turn on Bluetooth and Wi-Fi, I can. And it's a dual core, you know, it's a PowerHog, but it's dual core, multi, you know, tons of peripherals, whatever. Like, that is something.

**Mike Stisch:** Yeah. So, it runs really fast. I mean, I think you could go with, like, a free scale chip and get a similar thing.

**Chris Gammell:** Yeah, but it's also big. It's bulky. You know what I mean? Like, it's accessible. So, you're not soldering down the chip itself. You're soldering down.

**Mike Stisch:** Huh. I would go the other route and say that the module is more of a pain to solder down than chips are.

**Chris Gammell:** I guess there were some issues with that.

**Mike Stisch:** It just goes on what you're doing. Like, I like to be really close to the hardware. So, I feel like I don't have a good understanding of the SDK for the ESP32 already. That's true. And so, like, there's a pain barrier for me to get into it. And I haven't generally done stuff with Wi-Fi. That's true.

**Chris Gammell:** You wouldn't want to do low-level code on, like, a dual core. No.

**Mike Stisch:** And I'm more likely to do something, you know, hacky. Like, oh, I want Wi-Fi on this project. I'm going to put an ESP8266 as a secondary chip. And then, you know, use a UART to talk to it. Yeah, right. The other thing is, like, I'm always thinking about power and, you know, processing tightness. And I think when you go to those beefier chips, not just the ESP32, but, like, once you start to get to the bigger arms, you're relying on, like, peripheral libraries from the manufacturer. Sure. I don't know what those are doing. I don't know how long it's going to take.

**Chris Gammell:** You don't trust anyone, huh?

**Mike Stisch:** Yeah. Yeah. I have control issues, maybe. I certainly have used those. But I know that if I'm going to go and use that, I have to give up on this ideal of, like, really tight things that work well that I'm going to be able to debug. Right. Right. Okay. So, all right.

**Chris Gammell:** So.

**Mike Stisch:** So trends. You know, I don't see huge hardware trends right now. The trends that I see are in, like, leveraging tools that work with a lot of data. So I think, like, people that are using, like, TensorFlow and trying to get into. On badges? Or are you saying more generally? Oh, okay. You're just saying, like, I see trends stuff.

**Speaker ?:** Oh, yeah.

**Chris Gammell:** Trends in general. Okay. I was saying on badges, but, yeah, more generally trends are interesting, too. Oh. You see this as, obviously, you've seen tons of stuff coming to the Hackaday blog. You know, what gets submitted. Yeah.

**Mike Stisch:** It's a crazy amount of things that are coming through. But I think, you know, TensorFlow just put out, like, officially supported binary for Raspberry Pi. Oh, cool. Which is, I think, a big development. My issue is, and this is maybe going to make me sound really stupid, I haven't seen any compelling uses of neural networks.

**Chris Gammell:** I believe I just saw the other day a robot that finds Waldo for you.

**Mike Stisch:** I saw that one. That hand was very specific on where Waldo was going to be. No, I think that I see neural network things that are doing things faster than we would have been able to do in the past. But I'm not fundamentally seeing things that immediately make me go, like, oh, neural networks. The future has arrived. Yeah. And so I think if you want to go back to badges and back to embedded, I'm really optimistic that we're going to be able to use training sets to really increase what we can do with small microcontrollers by preloading the training.

**Chris Gammell:** Like OpenCV on microcontrollers?

**Mike Stisch:** Not necessarily OpenCV because you generally need a lot of processing power to deal with video. But it's more like, you know, batteries are not really getting better. It's true.

**Chris Gammell:** They are on a linear path, whereas everything else is on a different one.

**Mike Stisch:** But chips and chip makers seem to be doing really well on getting to be lower and lower and lower power. So I think we're going to see a really big push to take high computing power stuff that has a lot of power and find a way to optimize it to work on the really low power chips so that we can get around the battery problem with portables. Got it.

**Chris Gammell:** So almost like how the prevalence of cell phones drove the growth of Class D amplifiers because you can't be running a Class AB amplifier on a cell phone because why would you, right? The sound quality is good enough with Class D and obviously it's still pretty good and chips for current effectively for what it is.

**Mike Stisch:** Yeah. So, you know, the uses are out there somewhere. And I like to see people doing simple things that don't, you know, push those boundaries but teach them about what is machine learning, what are we doing with these data sets. And because, again, if you fast forward, you know, if it's like a 16-year-old in high school who's really into this has a lot more time than, you know, a 21-year-old engineering student who has other things going on.

**Chris Gammell:** Or a 30-plus-year-old engineer with... Yeah, maybe.

**Mike Stisch:** I mean, once you kind of get settled into your job and you start to be able to handle it, I think you get the curve goes back and you get a little bit more time. But at that point, you have maybe other priorities in your life like, oh, I went through college and I didn't do all this other stuff and now I want to have a family and take vacation and that sort of thing. I really look at the teenagers that are in high school and I'm like, can we get them to look at doing engineering things as their hobby instead of, you know, playing video games or, you know, something that's not quite as creative. I love video games. It's a great outlet. But I think the people who are, you know, spending their time and staying up too late and like doing this like self-learning thing in their mid-teens, they're the ones that are going to end up being really driven because they get to college and it's not like the first time where they've had to do labs and stuff. They've been doing it the whole time. You know, I think they just end up with a big head start. And so if we can get, you know, younger and younger people like that gateway drug of Raspberry Pi to get into like neural networks, the killer thing that can come, I think that's one path to it. I should also say I feel like I'm being unfair. We were on an article a couple of years ago. I think Cameron Coward wrote it where he had interviewed a couple of people that are like serious AI researchers. And one of the things that they said is that we keep moving the goalposts on artificial intelligence. As soon as we do something interesting, it's so obvious that everyone looks at it and says, well, of course it should do that.

**Chris Gammell:** Of course you have a thing sitting on your kitchen counter that listens to you all the time and starts playing Spotify for you.

**Mike Stisch:** I totally get that. And I still do it anyway. Yeah, of course. What have you done for me lately? Yeah, yeah, exactly.

**Chris Gammell:** Yeah, okay. So trend-wise though, it's more broad-based of like these, like you said, data set. I think so.

**Mike Stisch:** That's the things that when I see it, I'm like, whoa, that stuff's really going fast and we're getting a lot of new activity there. Yeah.

**Chris Gammell:** I mean, I'm curious too about the, I mean, again, to bring it back to the Badger Life stuff, I guess, is like, you know, people doing hardware and getting into hardware are very software focused. And I'm always actually, usually they're software people that are doing hardware to learn or for fun or whatever. And I'm very curious about what that's going to do from a trends perspective of, like, I mean, I use Git for all my hardware stuff. I wasn't doing that five, six years ago. And I think it was the influence of people that were software focused that just brought that to my attention. And I'm like, oh, that's a good idea, right? Not saying it didn't exist before that. I'm just saying that that's my personal experience with it. And I wonder what other trends are going to happen there as well, you know?

**Mike Stisch:** Well, that's a good point. I see a lot of MicroPython.

**Chris Gammell:** Oh, that's true.

**Mike Stisch:** And I see people doing like serious stuff with MicroPython. Yeah. And again, I like the low level stuff, but like I had a one bitsy that you can flash MicroPython onto. And I did it. And I was like, I got in there to the interpreter prompt, like you serial into it. Yeah, the rebel, yeah. Yeah. And then like you can type help. And it'll like tell you like what the pin mappings are. Yeah. And you don't have to like look it up. And I'm like, wow, that's actually like. A flow of endorphins. Yeah, you know, if you don't need a really tight timing for something and you're just trying to make things happen when they should happen. And you're just trying to get, you know, something hammered out really quick, which is how I use Python anyway. Right. I use Python for it. That's what I use for the Neoden. Oh, yeah. You know, I use a lot of text manipulation. Yeah. Yeah. And, you know, like if we're doing an article and I need to put like, you know, 20 bullet points that link, that have a title and link in them into HTML, like I will not cut and paste that. I'll generally like just script it in Python really quick and then cut and paste the HTML in. And I think the ability to do like rapid prototyping on hardware like that, especially for people who are already really comfortable using APIs and looking up, you know, references, that is another gateway drug for, you know, getting to hardware. Anything innately, everyone wants to be into hardware. Like who doesn't think a smartphone is awesome, but it's a black box for most people. And so once you start to pull back that curtain, then they're like, I didn't even know I could do this. Like, what else can I do?

**Chris Gammell:** Right. Yeah. It's going to be interesting to see how that stuff changes over. I think the, you know, the accessibility thing and making hardware more accessible, there's still going to be some barriers. He says this. He has a KiCat hat. Bouncing on his knee, but yeah. Yeah.

**Mike Stisch:** This is why it's coming, like you said, from software into hardware. It's like everyone has a laptop. If you're working in any kind of, you know, engineering type of field, you have a computer available to you. And so doing software stuff is the first thing you do because once you have the computer, there's really nothing else. Right. You know, an internet connection is really what you need. But with hardware, you've got to have a bunch of gear. Right. You know, even at its most simple, you've got to have, you know, a USB to serial cable and some type of breakout board and some type of power supply. Yeah. Right. I guess they do make USB, you know, dev boards that that's really all you need. But it's still something else. And then if you've never bought a bare board before, like picking out which one you're going to do, like there's a barrier there.

**Chris Gammell:** Yeah. And it's kind of like how do you get started into that and is it friendly enough for people to be welcomed in? Yeah.

**Mike Stisch:** You know, and then people are like, we need to be teaching this in school. I think that's really tough to, like, you know. Right.

**Chris Gammell:** Blanket statements are always tough. Yeah. Yeah.

**Mike Stisch:** So, yeah, I don't think you're ever really going to get over that. I think what you're going to do is you're going to have so many examples that are like, you know, ooh, candy, you know, type of experience that then you start to attract towards the people. Like a $5 Raspberry Pi Zero. Like, that's pretty incredible. And then people are like, oh, I can play video games on this. But then at some point someone's like, oh, I can hook up lights and then blink the lights. Right, right, right. And then when you start looking, eventually you get people like, oh, GPIO on Raspberry Pi is actually, you know, kind of janky. You should try X, Y, or Z. Right, right. Kind of go from there. Yeah.

**Chris Gammell:** Yeah, well, it's exciting. I mean, I saw someone wearing a, well, you talked about your hackable hat. I saw another version of a hackable hat. It had a Raspberry Pi on there. It was just an access point broadcasting. It's like, come hack the hat, you know. So it does open up those new things. And it is interesting to see when that happens. What are some other, so I guess as last things, what is something you wish you could share about DEF CON specifically with people? So that they might think about coming here or doing Batch Life or any other conferences. Oh, I guess there's other conferences we could mention real quick as well.

**Mike Stisch:** Yeah, so a conference I'm really excited about is coming up this November. Yeah. Second, third, and fourth in Pasadena, California. This is the ultimate hardware conference whose title is the Hackaday Super Conference. All these superlatives.

**Chris Gammell:** I never was a fan of the superlatives, but.

**Mike Stisch:** But it is really an amazing conference. I was blown away. Yeah. Well, you were a big part of it and continue to be. You're going to be there this year, right? I will be there. I will be there as well. I'm totally looking forward to it. I was blown away by the hardware hacking every year, but especially last year. So we added like Friday afternoon. Oh, yeah. And it was going to open up at noon. And we had people like showing up at 10 and they'd be like, hey, is it like open up yet? And like by noon, all of the soldering stations were completely full and then remained completely full through the entire weekend. Yeah, right. And just had amazing hacks. Like these badges had OLED, color OLED screens on them. And then I think his name is Ben, put two of them together and made a VR. Oh, yeah. Like hooked them together. Yeah, and then it had parallax. So like the two images matched and like I tried it and it like actually worked. There's just like crazy stuff going on too. People bring demos. So Elliot Phillips, who's a Hackaday editor emeritus, brought that thing that was like two buckets that you put on your head. Oh, yeah. And then they're connected by like a flexible HVAC condo.

**Speaker ?:** It's like a dryer hose.

**Mike Stisch:** Yeah, yeah, yeah. Yeah, and so it's like echoey and you can hear back and forth between each other. And then like each person has a control that affects these flashing lights for the other person. And I don't know, it's just like a really interesting experience. Yeah, right. And then, well, there's serious talks. I mean, it's really a conference about hardware creation. We have two talk tracks and we have workshops and that sort of thing. But it's really the people that are there. We call it the hacker village. But it's this community of people.

**Chris Gammell:** It's an alley out back.

**Mike Stisch:** Yeah. And I go through that alley at like each turn of the hour and I'm like, okay, time to go back into the talks now. Like everyone's just having so much fun interacting with each other that they're like, oh, yeah, I wanted to see that person talk.

**Chris Gammell:** I think that in real life IRL, that's an important thing. You know, it's hard to find these days. Finding like tribes of people, you know. Badger Life is like that here. And, you know, Hackaday Supercon is like that too. So kindred spirits.

**Mike Stisch:** Yeah. And I think, you know, DEFCON has a ton of tribes of people. And I feel that the majority of them are happy to welcome new people to those tribes. Yes.

**Chris Gammell:** And I've learned that since. I guess I should follow up with that too since I said it was, it felt clicky. But it was because I didn't know what I was looking at at first. And then subsequent things it felt much more, you know. And it's like, I think the tact you took was right. It's like get to know people. Take a chance.

**Mike Stisch:** Yeah. I had someone on Twitter this year be like, well, I'm not very outgoing. And it's like grab a piece of hardware that you've built. Like I'm just standing in the hallways with this Galaga badge. And people are walking by pointing at me yelling, Galaga badge. And that's like that's your icebreaker right there. And, you know, you could try that anywhere. But it works better at hacker conferences. It does. It's weird at the supermarket.

**Dave Jones:** Yeah. Yeah.

**Mike Stisch:** Actually, so I was, we play these outdoor concerts with the orchestras. And it was like a beer tent afterward. And we're standing at the beer tent. And then I brought the badge because I've been telling people what I've been doing. Right. Exactly. Yeah. And, you know, I get this like really bright blue and red lights blinking. I'm the only one with it. And my wife's looking at me. And I'm like, people don't want to see blinky lights. She's like, no. So I had to shut it up. Cool it, nerd. But I'm not embarrassed. Yeah. Good.

**Chris Gammell:** Good. Well, thank you for talking to me, Mike. Where can people find you online? And how do you spell your name?

**Mike Stisch:** Oh, yes. I can spell my name for you. Well, first of all, go to Hackaday.com and read the amazing editorial work that our entire staff is doing. And Hackaday.io is our community site. Please, we would love to see your projects. Post up about it there. My great advice is post project logs as you go.

**Chris Gammell:** It's better than, don't say you'll do it at the end, right?

**Mike Stisch:** No, it's too big of a job. No one's ever going to do that. And, you know, crappy project logs are better than no project logs.

**Chris Gammell:** And it draws people to you for getting help and advice.

**Mike Stisch:** Yeah. You can form a collaborative team there. I'm also trying to build up to a million Twitter followers. Oh, yeah. How are you doing on that? Yeah, yeah. I'm not...

**Chris Gammell:** One two thousandth of a million. Yeah, yeah. I'm very small.

**Mike Stisch:** So, yeah. So follow me on Twitter. It's really easy. It's at S-Z-C-Z-Y-S. Yes. Yeah. I had my most, like, influential tweet ever this week. Oh, yeah? Because I tweeted out about that article that we got out right away on the original DEF CON badge. Oh, yeah. And it got, like, 100,000 impressions or something. Right.

**Chris Gammell:** We didn't actually mention that, but I think there will be other, hopefully other coverage about that Toymakers badge is great.

**Speaker ?:** Oh, yeah.

**Mike Stisch:** That's incredible. You've got to have them on. Yeah.

**Chris Gammell:** Well, we'll point people to your article in the meantime. Oh, thank you very much. All right, Mike. Thanks for joining me. It was a pleasure. It was a pleasure.

**Mike Stisch:** You know, I was on NPR. What? I was on Science Friday. Really? I didn't know that. Oh, for Hackaday Prize? Yeah. I used my NPR voice. Let's hear it. Hi, this is Mike from Hackaday.

**Dave Jones:** I'm Terry Gross. No, but, like. Welcome back to Fresh Air.

**Mike Stisch:** You go to, like, the local affiliate. Right, right. And it's, like, live, right? Yeah. And so they sit you way ahead of time, and you're sitting in this, like, dark, you know, quiet. They've got all the.

**Dave Jones:** Can I get a cup of tea, please? Yes. Chamomile. Chamomile. Shweaty. Shweaty balls. Shweaty balls.

**Mike Stisch:** The official food of NPR. Yeah.
