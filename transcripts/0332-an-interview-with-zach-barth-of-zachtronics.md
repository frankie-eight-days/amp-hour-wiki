---
episode: 332
title: An Interview with Zach Barth of Zachtronics
url: https://theamphour.com/332-an-interview-with-zach-barth-of-zachtronics/
---

**Zach Barth Of Zachtronics:** This is The Amp Hour Podcast. Recorded January 18th, 2017. Episode 332. Interview with Zach from Zachtronics.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEVBlog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. I'm Zach from Zachtronics.

**Dave Jones:** Hey, Zach. Welcome, Zach. Thanks for joining us.

**Zach Barth Of Zachtronics:** Yeah, it's exciting.

**Chris Gammell:** This one is going to be unusual. Yeah, this is... I'm so confused and amused, but in the best way possible. I just want to say that this is so cool talking to you. First off, why don't you just tell people what you make and what you do? Oh, God.

**Zach Barth Of Zachtronics:** That's the problem, right? Trying to explain it. Sure. I think this audience will have some crossover here.

**Dave Jones:** You make video games, right?

**Zach Barth Of Zachtronics:** We do. So we make video games. So Zachtronics is a game studio. We've been around for years and years now. And back in the day, a long time ago, before we realized it sounded bad, we used to say we made games for engineers. And then we stopped calling it that for a while because who would want to play that? And now we've been doing it for so long that we can actually... It's probably better if I say we make games for engineers because we do. Nice. It started off as a coincidence and then it became a disturbing trend and now it's just true.

**Dave Jones:** That's awesome. Is that because of the whole new hacker maker? Well, not new, but like the last 10 or 5 years, maybe it's really gone solo. And now it's kind of like cool to be an engineer slash maker.

**Chris Gammell:** I haven't gotten the news article about that one yet.

**Zach Barth Of Zachtronics:** I would like to agree, but yeah, I'm not... I don't know how cool it is to everybody. It's not mainstream. To some degree, I think yes. I mean, it's... Okay, so I mean, obviously, success in games is really about getting lucky and getting attention and somehow finding a way to cut through the noise. And I think a lot of times, like more often than not, it's not about talent all the way. Like you have to be talented to some degree, but you really have to be lucky. And a lot of why we are where we are is because we've gotten lucky. We made a bunch of games and persistently, you know, I mean, I started making games for free and then I made a bunch of games for free. And then I slowly started making games that I sell. And it's been... I don't even want to count. Like at least 10 years of making games and putting them out there as Zaktronics. Zaktronics. I'm pretty sure, yeah, it's at least 10 years. And over that time, we've slowly built up. So more and more people who are the right kind of people to play our games, the kind of people who will... I mean, everybody's the right kind of person to play our games. The right kind of people. You hear that, folks? The kind of people who will really enjoy our games, the weird things about them that we'll get into shortly. Like we've slowly kind of gotten the word out there. So like a lot of those people know about it. And it turns out there's a lot of engineers who like games, especially now. There's a lot of programmers who like games. And like they all know us now. And that's great. That's really awesome.

**Dave Jones:** So how can we... Why do we have a gaming person on an engineering podcast? Games for engineers. Explain, explain, explain.

**Chris Gammell:** Well, maybe start where you came from too, yeah.

**Zach Barth Of Zachtronics:** Oh, yeah. So I have an engineering background. No surprise there. So I went to... I got a degree in computer science, computer engineering at Rensselaer Polytechnic Institute in upstate New York.

**Chris Gammell:** Troy, New York. All right. Yeah. Oh, yeah.

**Zach Barth Of Zachtronics:** Yeah. And lovely Troy. Yep. And so I got an engineering degree there. But that was sort of where I started. I discovered like making games. And of course, it just made sense to me that when I was going to make a game, it'd be cool to make games about these things that I was learning about that were really interesting. Nerd. Nerd. Yeah, exactly. Exactly. Yeah. Exactly. Yeah. And fortunately, I was at Rensselaer Polytechnic Institute where most of us were nerds. Built-in audience. Yeah. That's good. Yeah. And it was just normal. And so I was taking classes about computability and learning about these engineering things and being able... It just kind of fit together in a way that I could make games about it. And this is not a common reaction, I think, when most people learn about computability theory. They don't go make games about it. But for me, I did. It's just like how you processed it or what? Yeah. It just kind of made sense. It looked like a game, right? Like the idea of trying to... Like if somebody gives you rules for a state machine or like a character recognition automata that can recognize these different strings and they say, now draw a state diagram that can recognize these strings. That's kind of fun. And I think a lot of people who take these kind of classes, if they kind of get it, that's the part that's fun. The theoretical math part is the not fun part to me. Right. But like kind of designing these little like state machines that would describe these string routines, like that was really cool. And that kind of felt like a game. And so I was learning to make games at the same time. I said, why don't I make games about this kind of stuff? And this is also when... How was it? Not How Did It Gets Made. How It's Made? Is that the... Oh, the TV show you mean? Yeah. There's a podcast now about making movies and stuff that's called How Did This Get Made? So I always confuse that. So yeah, like How It's Made, like the show about like factories and how stuff is made. And I was watching, like this was on TV. This was pretty popular then. And I was like, oh man, it would be so cool to make a game where you build these factories. And you build factories that make things. And like that's kind of how computers work is that you program them to transform inputs and produce outputs. And so there's this big space of stuff that overlaps that I was being exposed to at the time while learning to make games. And it just kind of clicked. And I started making Zaktronics games, which is now apparently called Zack Likes. And the characteristics... I did not coin this term. Zack Likes? I've been doing this long enough that, yeah, like somebody at PC Gamer or Rock Fiber Shotgun, one of them, coined the term Zack Likes for the kind of game we make, which is typically they're open-ended puzzle games. And if you think about like what a puzzle game is, you can think of like a ton of different kinds of games. Like Tetris is a puzzle game. I'm doing air quotes. It is. Tetris is a puzzle game. Bejeweled is a puzzle game. But Portal is also a puzzle game.

**Chris Gammell:** Yeah, that's what I was thinking of.

**Zach Barth Of Zachtronics:** And like there's a whole bunch of different kind of things. Like some puzzle games are really just about pattern recognition. Some of them are about reconstructing a solution that the developer created. Ours are about being really open-ended challenges. And where we give you... We say that in order to have completed this level, you need to build a machine that takes these inputs and creates these outputs. And... But how... Like what your machine looks like, you know, because our problem is defined in such an open way that it just has to... We're giving you criteria, not a state. Right. And so we're giving you criteria.

**Dave Jones:** So it could be an elegant, really optimized solution, or it can be a complete kludge. Exactly.

**Zach Barth Of Zachtronics:** If someone's asking you just to find the path to get to a state, you can't really do that elegantly or not elegantly. But if somebody's saying, here's some specifications, just make it happen. Right? Like you could have like a really hack job, or you could have like something that's like really like fast and efficient. And that's where a lot of... With one of our games, Space Chem, was when we thought to add histograms. And so when you beat a level, you can see a histogram of how everybody else did. And then later, you can see little leaderboards of how your friends did. And it turns out...

**Dave Jones:** I was going to say, do you score points based on how optimized your solution is?

**Zach Barth Of Zachtronics:** Yeah, exactly. Yeah. So one of like our best metric in any of our games that are like this, that follow this formula, is always cycles. Because people, you know, people really understand, like, I need to make this faster. And so with some of our more recent games that are actually about assembly programming, you know, they're literally about cycles of like these fake computers. But even in our more like abstract visual puzzles, it's about like how many like factory ticks does it take to build stuff.

**Chris Gammell:** And so is it a certain type of like brain chemistry that likes this stuff, too? I mean, like even so. So like you said, it's kind of games for engineers, but it's also I mean, I'm sure it's not just that. So do you notice any other characteristics of the people that are playing your games that are similar other than engineer types?

**Zach Barth Of Zachtronics:** Yeah, I kind of think it's it's a kind of thing that would appeal to everyone if they could get like past the sort of implicit difficulty curve that's in a lot of these games. And this is something that we're, you know, we still years and years later after making games that kind of have a formula to them that is this compelling little thing we do. We're still trying to understand like how how can we make these games so more people can play them without bouncing off of them. And I think we're kind of notorious for having games that are really, really, really hard. And it's not that we try to make games that are hard. It's just that in trying to make games that are emergent and open ended, they're often complex. And you often need like a level of systems thinking that you don't for other other games. And so it's it's kind of we dabbled in educational games for a while. And it's we still have no idea like how any of this stuff connects. And like, it's it's kind of hard. I don't know. It's it's above my pay grade. I just make games. I don't I don't understand the human mind. No, that's great.

**Dave Jones:** Targeting kids for stuff. Like, because I would think that this is not suitable for an eight year old, for example, they they wouldn't have that systems engineering thinking or would they? Some of them beat out of them in school. Yeah.

**Chris Gammell:** This is how you can identify the knack. You could use this as a testing method for future engineers.

**Dave Jones:** Your next game must be called the knack.

**Chris Gammell:** The knack.

**Zach Barth Of Zachtronics:** I might pass on that. But we'll see. We'll see. Can't can't promise anything. So we have a lot of people who play our games and have been playing our games. And now they have kids and now their kids are getting old enough where like they want to like get their kids to start playing these games. And we've had some players who like a lot of our games have level editors. So we've had actually some players that have put together like what they believe are a simpler set of levels so that way their kids can play. I sort of have like an inability to relate to kids or any of that. Like I very much like all these games are very much designed for people at like a college level. Right. Not to say that you have to be at college level or like that's just sort of when I started thinking about them. And so there's sort of there's a lot of implicit assumptions and anything that anybody makes, especially these. but we definitely have lots of, you know, high schoolers that I've heard from playing our games. I get emails all the time now. Again, I've been doing this so long that people have played our games over the years and it like it kind of helped them think that they should go to college for computer programming and now they're like out of college and have careers and then they can write back and say, oh, thanks for helping me decide what to do with my life. And awesome. Yeah. So they're, they're games for everybody, but they're definitely. But most optimized for. But yeah, but, but not for everybody. And it's, but it's, yeah, it's.

**Chris Gammell:** Wow. Yeah.

**Zach Barth Of Zachtronics:** It's, it's a post hoc filtering. Not, we don't want to say like, don't try it if you can. It's just you, you might not like it. And if you didn't, it's because of this. Right. Right.

**Chris Gammell:** It's almost like a challenge put out to people too. It's like, we dare you to try these games. Yeah.

**Zach Barth Of Zachtronics:** Kind of. Yeah. Yeah.

**Dave Jones:** Now this is your full-time job, right? But you've been in, you said before the show that you've been in and out of full-time, gaming development.

**Zach Barth Of Zachtronics:** Oh yeah. I mean like so.

**Dave Jones:** How and why.

**Zach Barth Of Zachtronics:** When I, so I started making these games when I was in college and then I got a job at Microsoft where I worked on Office of all things. For some reason, I had a creative, creative energy built up at the end of the day that you needed to.

**Dave Jones:** I need to know, is that as boring as I assume it would be?

**Zach Barth Of Zachtronics:** Oh God. Okay. So I worked on, I worked on something called Visio, which is a diagram.

**Dave Jones:** I used to use Visio. Yeah.

**Zach Barth Of Zachtronics:** I used to use it too. Oh my God.

**Dave Jones:** It used to be pretty good. I mean. It is.

**Zach Barth Of Zachtronics:** Yeah, yeah. Definitely. You know, it's hard to make diagramming programs and it was a pretty confident one. So I was, I went to work there at Microsoft and I sort of got like pushed, I was a programmer and got kind of pushed to work on layout and routing. And so I worked on this problem that I knew nothing about that like I could barely understand any of the code because it was like 20 years of like janky like C++ that used to be C and then like C++ was invented and then they started switching over to it. So like I was, it was a bad fit. I'm, I'm, I'm not, yeah, it was, I'm not that great of an engineer.

**Chris Gammell:** You're saying you don't like, you don't like solving puzzles here, Zach? Is that what I'm hearing?

**Zach Barth Of Zachtronics:** I don't like solving bad. Well, so actually that's kind of related, right? It is a puzzle, but it's a bad one. It has poor, it has poor feedback, right? Like it takes forever to learn why. And there's like, you have to learn too much at once to make any progress. And honestly, I think a lot of these things we do on these decisions, like the design decisions we make for our puzzles are all about how do we take this real life engineering experience and make it less horrible, right? How can we improve on it? And so we'll get back in a second. But yeah, so I worked at Microsoft and like I came home with so like wanted to do something important and meaningful, but I made a bunch of games. And during that time I made Space Chem like at night and on the weekends. And it actually kind of took off. And because of all the stuff we've done in the past, we made this game called Space Chem, which was our first commercial game. And it found some people who loved it on the internet and some people on gaming sites back when gaming sites actually like kind of drove things more than they do now. And people loved it. And we sold a bunch of copies and we got it on Steam, right when Steam was starting to do digital distribution and there were way fewer titles than there are now.

**Chris Gammell:** Yeah.

**Zach Barth Of Zachtronics:** That's nice. Yeah, yeah. And so me and one of my buddies, we quit Microsoft and we started a game studio. And we did that. We made Iron Cloud Tactics. We made some educational games. Almost went out of business when Iron Cloud Tactics didn't do as well as we thought it would. That's notably our only non-engineering puzzle game that we've ever made. So we kind of verged off into something weird. And then we made Infinifactory. We made TIS 100. At that point we'd been doing it for a couple years and I got kind of burnt out, honestly. And it's hard when you get burnt out when you run a company when everybody else depends on you to lead the way. Because it's like, well, I need to take a bunch of time off. You guys keep doing the thing that I told you to do. So we just kind of... And having never really been in this position before, we shut down the studio. And so everybody who was there kind of split off and we kept making money off the games. But nobody was actually doing anything at Zaktronics for a period of about a year. I went off and worked at Valve. Actually, before that, I interviewed at Microsoft again. It was just like, yeah, I know this is not happening. I can't go back.

**Chris Gammell:** Right.

**Zach Barth Of Zachtronics:** But I interviewed at Valve and worked there for 10 months. I worked on VR stuff. It was really cool because that's when VR was starting to take off. Yeah. And so I definitely felt like I had to be part of this thing that's happening, which I have since gotten out of my system.

**Dave Jones:** So are you a fan of VR? Did you just think it wasn't as good as you thought? Or are you still a big fan of VR?

**Zach Barth Of Zachtronics:** I think there was a little bit of fear missing out when everybody in the industry was kind of moving towards it being a cool thing. And then now that I've actually seen it firsthand, it's just like, I don't know if this is going to be the... The thing. Yeah. That's my opinion too.

**Dave Jones:** I don't... It doesn't do anything for me. Like it's kind of cutesy, but it doesn't push my buttons.

**Zach Barth Of Zachtronics:** Have you tried the Vive?

**Dave Jones:** No. I have.

**Zach Barth Of Zachtronics:** The Vive is amazing. Like it's so cool. And it actually like adding your hands adds a level of immersion where it's like, wow, it's way more immersive. But like, it's still like as a game designer, it's not like, you know, like I... When I think like, oh, I want to make these kind of games about systems, it's like, wow, it'd be way easier to make this if it wasn't in VR. Yeah. Oh, okay. Interesting.

**Dave Jones:** Oh, I'm sure it adds a whole nother level of complexity. Oh, yeah.

**Zach Barth Of Zachtronics:** And it's, yeah. A whole new dimension of having to be in 3D. And it's, yeah. And it's in there. Yeah. There's so many things. So I don't know. It's good and bad. And it may or may not catch on. Who knows? I don't know the future. But...

**Chris Gammell:** Did you know the hardware group there? I mean, I think all of them, almost all of them have been on the show at this point.

**Zach Barth Of Zachtronics:** Oh, cool. Yeah, I did. I worked on the software side of things, but I worked on like, I worked on a game, but I also worked on like the calibration software when you set up your Vive. Oh, cool. Yep. And so like all of that like had to be done pretty closely with the hardware guys. And also like I, you know, in the past and when I was in college, I had done hardware stuff. I'd made games about hardware. Obviously, it was super cool. So I'd like go over and just like see what they were up to and watch them like hot glue stuff and test stuff and other oscilloscopes. So it was super fun. And that was kind of where the inspiration for Shinjin.io came from. Really? Wow. When I wrapped up at Valve, I had actually managed to find a company called Alliance that would buy Zaktronics because I was tired of running the business, but I wasn't tired of making games. And so we found this like perfect opportunity and we work for them now. And that's how we made Shinjin.io.

**Dave Jones:** How do you shop out a game company like that? Like basically a two-man game company, was it? I'm assuming it's a two-person. Anywhere between.

**Zach Barth Of Zachtronics:** It was, I mean, currently we're four and we've peaked as high as like six or eight.

**Dave Jones:** How do you, like, do you just randomly cold call bigger companies? How do you do it?

**Zach Barth Of Zachtronics:** How do you? Like all things in life, just weird personal connections. Right. When we made educational games, we did it for a company called Amplify that was owned by News Corp. News Corp spent like a billion dollars or something making this like tablet-based curriculum. And a small portion of it was making educational indie games to go on those tablets. And so we were part of that and we made three totally original, way cool educational games for them. And one of the writers there, so after that project came crashing down, one of the writers there ended up at this company, Alliance. I don't even know how he ended up there. But I still knew him from Alliance and then I was joking with a friend. I'm like, oh, find me a million dollars and we'll make another indie game. And lo and behold, we found a company to buy us. Oh, sweet. And it's just, yeah, it's great. We get the creative freedom we need to do our weird stuff.

**Dave Jones:** Are there any downsides that you've found yet to selling it? Not yet. No, okay.

**Zach Barth Of Zachtronics:** Honestly, no. I had to do all the business stuff before and I was like okay at it, but it's really not my strength. Like I'm really like a creative person, not a business person. And so I'm way happier now than before when I had to like worry about all the business stuff.

**Chris Gammell:** Right. That's, and so you're obviously in Seattle. We didn't actually say that at the top, but still in Seattle? Are you working remote? Yeah.

**Zach Barth Of Zachtronics:** Yeah.

**Chris Gammell:** Cool. What is the scene like there? I guess I still haven't been there unfortunately, but.

**Zach Barth Of Zachtronics:** For?

**Chris Gammell:** Software, hardware, whatever.

**Zach Barth Of Zachtronics:** Oh, there's a lot of big companies. There's a lot of big software companies here. Hello, Microsoft. Yeah, Microsoft and Amazon, increasingly Amazon. Oh, Amazon, right. Really dominating the, like they're just, they hire, you know, they're just constantly hiring tons and tons of people.

**Dave Jones:** And vacuum cleaner, they're a, they are a graduate vacuum cleaner, are they? Going around.

**Zach Barth Of Zachtronics:** Just an everybody vacuum cleaner, yeah. So they're like, you know, Microsoft is still huge on the, like one side of the lake and on the other side in Seattle, you know, Amazon is growing and growing and growing.

**Chris Gammell:** Interesting. Does that impact your ability though? Like, I guess I don't really understand where, where game development happens either. I don't know if like, is that like one of the big places that it all happens? Or?

**Zach Barth Of Zachtronics:** There's, it's, it's surprisingly scattered. I think there, there are a lot of game studios here. There's definitely a lot of startup-y indie game studios. Although it's hard to tell like how many of them there are everywhere because I swear to God, there's just like a million. Like there's like an entire VR incubator in Seattle. I just learned about this. Where it's just filled with like all these little startups trying to make VR games and VR stuff. And it's just, there's a lot of like small stuff like that. I'm kind of out of touch. I sort of, I'm not really out like in touch with like the indie stuff anymore. Like when I first started doing it, that was when everybody was starting to do indie stuff. You know, like Braid, you know, Jonathan Blow's Braid had just come out and he made a bunch of money on Xbox Live. And like, and everybody's like, whoa, there's, there's money in making indie games. And that was at the beginning. There were lots of like, like there's pretty tight knit community here. And I was kind of part of that. But like over time, like, you know, like people come and go. A lot of the, I think a lot of the first round indie people, like they didn't make a second game, right? Like we're relatively privileged in that we've been able to make, we have five games on Steam. Plus all the crappy ones I made before. Not a lot of people make like five commercial games as indies. And it's just because it hasn't been a thing for that long. And so like, you know, it gets to the point where now when I try to go to an indie meetup, I don't know anybody there. And it's just like, ah, whatever. We're just in sort of like a weird, like mature, mature, but incredibly tiny and irrelevant space. And, uh, and it's, yeah, it's, it's strange.

**Dave Jones:** There is one thing that I do not see here is that where, where's the apps? Where's the iPhone games? Isn't that where all the money is now? Or is it grown?

**Zach Barth Of Zachtronics:** Yeah. It's, I mean, it's okay. So there's, this happened with Facebook gaming before. Yeah. When farming? Yeah. When Farmville was a thing. Oh, yeah. And Zynga.

**Dave Jones:** Oh, God. Is that crap that keeps popping up on my, that's why I don't use Facebook.

**Zach Barth Of Zachtronics:** So, so years ago, I mean, this was probably like 2008. Like I, I don't know. I'm hazing on the years. It was, it was like in 2008. It was when Facebook and Facebook gaming started becoming really big. And all of a sudden there were tons of people spending tons of money and playing all these Facebook games. And, and people were like, oh, like are all gamers just playing Facebook games now? It's like, no, what actually happened is that all the gamers who weren't on Facebook games kept playing the games they were playing. But all these people who weren't, exactly. All these people who weren't gamers started playing games on Facebook. And so what happened is that by growing out in this new direction and this new audience, it actually, like the, the total number of gamers got bigger. And I think the exact same thing happened with phones is that phone games. Yeah, exactly. It represents a totally new segment of people who are playing games and people who played hard, like hardcore quote unquote games who, when they're on the toilet, need mobile games to play. And, and so like the, the, the pie just keeps getting bigger and bigger and like inexplicably, like on Steam, you know, people have been saying for years that PC gaming is either dead or not dead, but like on Steam, there's so many people buying games and great for us. There's so many people buying really like weird, difficult, you know, challenging, strange games. And I, I don't like there, there is certainly money on, on phones. It is quite possible that it.

**Dave Jones:** Money, hello, angry birds, you know. Or is that the rare exception?

**Zach Barth Of Zachtronics:** It's kind of like from a per title basis, it's kind of the rare exception. Like last, well, I, one GDC, so GDC is the Game Developers Conference. And so like one or two years ago when I was there, we were talking about mobile games and somebody was saying that Clash of Clans, 60% of the money being made on the app store was going to one game, Clash of Clans.

**Dave Jones:** Whoa. Wow. That's a power distribution, huh? Is that how they can afford those TV commercials and crap like that?

**Zach Barth Of Zachtronics:** Oh yeah. With celebrities and Super Bowl.

**Dave Jones:** We've been like, oh, what's the one with, is that the one with Arnold Schwarzenegger?

**Zach Barth Of Zachtronics:** I don't even know.

**Dave Jones:** He's got one and then, oh.

**Chris Gammell:** Kate, Kate, what's her name? Yeah.

**Dave Jones:** Exactly. And there's a Battleship one with Steven Seagal. Who's advertising some Battleship game.

**Chris Gammell:** Man.

**Zach Barth Of Zachtronics:** So there, it is certainly big in its own way, but like PC gaming is also still big. And that's like, our games probably wouldn't thrive as well on mobile just because the players are different. They're looking for a different kind of experience than on PC. Right.

**Dave Jones:** Okay. So you knew that you wouldn't be successful there, so you didn't even try. We've tried.

**Zach Barth Of Zachtronics:** We ported SpaceCam to iOS, where it did okay, but not nearly as well as on PC. Right. And, you know, PC's our place. Like, that's our favorite platform because that's where the people who are playing on that love our, like they, you know, more so than other platforms, they really are able to find and enjoy our content. Yeah.

**Dave Jones:** Now, here's where I want to get into the nitty gritty of games. Let's start by porting. How easy is it to port something like SpaceCam over to iOS? It's not like, oh, you push a button and it ports over to iOS.

**Chris Gammell:** I guess I don't even know what you're writing code in. I mean, I saw Unity based, right? Yeah.

**Zach Barth Of Zachtronics:** So we write all of our games in C Sharp. And this is before, I mean, like we had like our own custom, with SpaceCam, we had our own OpenGL, like just our custom engine in C Sharp. For Infinifactory and TIS 100, we switched to Unity and we've since switched back to a custom engine in C Sharp. But all of our stuff is in C Sharp because we love it. It's a great language. Which we don't have to worry about.

**Dave Jones:** Did you write the engine first from scratch with the intention that it would be used for multiple games?

**Zach Barth Of Zachtronics:** No. I mean, our notion of an engine is pretty hazy. Like some game programmers will say, I'm going to build an engine and they'll spend like years and years working on like trying to re-implement the wheel. Like our engine, quote unquote, is just like a way that we can draw stuff to the screen and read the keyboard. And just as we need more features, we just kind of hack it in. Like our philosophy.

**Chris Gammell:** It's like an API basically for you, for the game stuff. Exactly.

**Zach Barth Of Zachtronics:** Like during the year that I was at Valve, our like lead programmer, Keith, was like sort of off in the, he went up at the mountain and like discovered a whole new way of programming games. And when I came back from Valve and he came down from the mountain.

**Dave Jones:** There were stone tablets.

**Zach Barth Of Zachtronics:** Yeah, exactly. And it's like, so our philosophy now is very much just like, if you need something, program it right then and there. Like don't try to predict the future. Don't do more work than you have to. Like just keep it, like you can refactor stuff when it sucks, you know, and just try to, like we don't have that many programmers working on stuff. It's just the two of us. So we're able to be really agile and just not do anything that we don't need. And like that's our, our graphic stuff is really like we, there's a thing in games programming where usually, you know, usually in a program you don't want it to run continuously. Like you want it to like seed control back to the user. In a game it just needs to run continuously. And so usually people like they'll split it up into like, oh, you have a draw loop and an update loop. And so like our philosophy is just like, we have one function that just says like, do the game. And it's a very simple, there's a programmer like Casey Muratore who worked with Jonathan Blow on The Witness or something. They were somehow connected. And he had like this, he had this big thing where he live streamed writing a game in a game engine from scratch. And it's very like this kind of like low tech, like approach to games programming. Like he's very low tech, very old school. But like, there's a lot of kind of modern lessons in looking at that kind of stuff. And so I think Keith learned a lot from that too.

**Dave Jones:** Now I will toot my own horn here. I know more about this than you do, Chris, because I have actually written and published my own game. Did you know that?

**Chris Gammell:** Okay. Is it Snake? I don't know, Dave. Like, I don't, I don't know how that's relevant at all. Like looking at these, I'm guessing it's a little bit more.

**Dave Jones:** Way back in the day, way back in the day, Hexagonal, Othello. I wrote my own game. This is like early nineties. So, you know, like, and this is what I wanted to, like, I wrote my own engine in air quotes to, you know, display my, you know, display the stuff on the screen and, and generate the, you know, the images and stuff that I needed. But I look at, well, even games from 15 years, even ones at the time, I go, how the hell do they do all these photo realistic graphics and everything else? How do you, like, it's just mind boggling to me that the amount of detail that goes into modern games.

**Chris Gammell:** The amount of detail to the graphical stuff is very confusing to me as well. Please explain.

**Dave Jones:** Magic. Yeah. Okay. That explains it. End of show. Thanks, Zach. Yeah.

**Speaker ?:** Ta-da!

**Zach Barth Of Zachtronics:** Time now. Yeah. Graphics programming is, is obviously more complicated than I can talk about now. It's, oh God. I mean, there's.

**Dave Jones:** Is there an engine, like, do you, is there an engine off the shelf that does it? I know, like, all those, like the Doom engine and stuff. Like, people can write their own game in a week, their own Doom game in a weekend because the engine's there with all the graphics and everything.

**Zach Barth Of Zachtronics:** Right? So, like, fundamentally, like, it's, it's, it has, it's a beautiful synergy of hardware and software. And, like, you're, you're writing code, obviously, and code can move stuff around in memory. We understand how code works. Yes? Yeah. Yeah. Most days. Most days. Yes. So, um, graphics hardware is the other half of it. And so the simplest, you know, simple graphics hardware is just like a memory buffer. When, when you put, like, ASCII values into it, it mirrors those to the screen and like a grid. And that's like a simple, like, character-based graphics display. And then from there, you could also do like a, like a bitmap graphics. So you have like.

**Dave Jones:** That's about my level is the bitmap.

**Zach Barth Of Zachtronics:** Yeah, exactly. And so that's how, like, a lot of old 2D, like, graphics stuff would work is that each, each pixel is a byte. And then depending on what bits you put in that byte, it changes the color of that pixel. And then there's just a bunch of them in, like, linear, linear memory somewhere. And then that gets drawn to the screen. And, um, that's good for like 2D stuff. And you can do 3D stuff. It's, you know, like Doom, that was done by, in software, kind of figuring out which pixels go where, if there's like a wall at a certain distance and a certain angle. And you're doing that on software, but that's hard. Um, it turns out that, that having to do something for that many pixels, um, is, is, it's slow, right? Because you have to basically like loop over all the pixels or there's like tons and tons of like, people are way smarter than me making this fast.

**Dave Jones:** It's difficult in sequential programming.

**Zach Barth Of Zachtronics:** Exactly.

**Dave Jones:** And sequential processing. Exactly.

**Zach Barth Of Zachtronics:** Yeah. And so people started building graphics cards that were well suited to this, this problem of like, okay, well, instead of doing a small number of things in linear order, we actually need to do a bunch of things in parallel. Like we, we can do them in parallel. I guess I just jumped to the, the, the, the, the punchline, but you know, because these pixels are relatively independent, we can calculate them in parallel. And so flash forward 30 years, like we get to where graphics cards are now is that they're, they're these specialized little computers within your computers. Little?

**Dave Jones:** They're freaking supercomputers.

**Zach Barth Of Zachtronics:** They're, they're supercomputers. Yeah. I guess it depends. Little relative to the physical size. I don't know. They're, they're computers within your computers. We don't have to make any judgments about their size. But they're, they're optimized for parallel, like parallel processing because like the, you take your data for your, your world or whatever. And when you calculate what should show up in a certain pixel, it doesn't matter what shows up in the adjacent pixels to calculate pixels. So you can kind of just like fan it all out and calculate them in parallel. And a lot of graphics programming over the years, like it used to be like in the 90s when they started having 3D graphics cards that there was something called the fixed pipeline, which is where, you know, like there's a setting that you can, you know, like there's a register somewhere that you can write to to turn fog on or off or change the fog distance. And there's, you know, like there's registers and I guess you never actually access the registers directly. Like that's for the job of the driver. But, you know, there's, there's all these different fixed features you can turn on in this fixed pipeline. And now it's very much not like that. There's the, it's all programmable pipeline. And so you write code that then gets downloaded and run on this graphics card, this computer within your computer. And then that determines what it should do for every pixel on the screen. And that's sort of where we are now with, with computer graphics.

**Dave Jones:** So can, can you do that for say a character? Like you've got, like in one of your games here, I'm looking at the screenshot for ironclad tactics and it's got this like human looking character. Do you draw, how do you?

**Zach Barth Of Zachtronics:** So that game is actually entirely 2D. So for 2D stuff, it's still, it's actually really similar to what it was 30 years ago is that we have an image, we have like an image that has a bunch of frames for that animation. And we just, we blit, you know, we copy. Yeah, you're right. Technically it's not. So, so actually ironclad tag is a lie. It's 2D, but it's 3D accelerated. And so we're actually, we're drawing a 3D shape that is just a square onto like the screen. And we're drawing a bunch of squares where we ignore depth and just draw them in order. And like you can, you can take the graphics card and configure it to go into this mode where you can do 2D games. Um, if, if we were doing a 3D game, like Invitifactory, yeah, you would have like a model, you would have like a geometric data that represents a character. And then you take that and you feed that to the graphics card and you tell it like how to, like you give it rules for how to actually like draw the little pixels based on like what color it sees. It's, it's, it's actually really complicated. And, uh, again, over like this, this is above my pay grade. Okay. Well, how do you think we feel, man?

**Dave Jones:** How do you generate like the photo realistic artwork, the characters? Like, do you? A lot of it comes down to lighting. Are there tools?

**Zach Barth Of Zachtronics:** Are there like. Oh yeah. So there, a lot of it comes down to data and lighting, I think is probably safe to say. Anybody who actually knows about this is just going to be like, like facepalming while they listen to me try to explain this. Right. Yeah. Like high res. Okay. So when I was working at valve on VR games, when you're in VR, you can jam objects into your face and it's supposed to feel realistic, which means that for it to look really good, you want it to be like insanely detailed. Right. And I worked on the lab, which is the, the, the valves VR game that came out with the vive and notable, a lot of the content in there is very high resolution. And so when you do take this object and like jam it in your face, you're just like, whoa, it's like, it's real. And so that comes from when you model something, adding a lot of detail, just as data that describes like all the different contours of it. Like you think that if you, if you took something off your desk and scanned it in and captured all of the information about it, you'd have a lot of data, but you'd also have like a realistic representation of it. And so there's all sorts of tricks that people do there. Because if you were to actually like capture every little like pinpoint data, like as like an uncompressed kind of thing, it would actually be a lot of data. And so there's all kinds of tricks where, you know, things are made out of polygons, out of like simple shapes. And then you can do tricks where you like you texture it. So you paint on the surface detail. But instead of just painting on color, you can also paint on information about like how recessed it is into it. And so you can have something that's just a single flat polygon. But you're texturing, you're texturing in detail to say like, oh, this part should dip down and this part should dip up. And then when you go to render it, you can actually do lots of advanced math to kind of calculate what it would look like if it was offset based off of that, that information. And so it's a really interesting problem of, of choosing how to represent your data to like efficiently store something that, because like the end result of computer graphics is it's something that your eyes and your brain perceive. Like we're not really trying to truthfully represent the objects. We're just trying to trick people. And so it's like, what's the most efficient representation for efficiently tricking people's faces and brains?

**Chris Gammell:** And don't they talk about like when you're focusing on something that's where, I mean, like peripheral vision is super low resolution effectively anyways, right? But like something that you're focused on, obviously you're, you're using all the information is coming in your brain. That's, you know, like super high definition as well. If you're like your hands in front of your face, but there is still data around all the other light that's hitting your cornea, right?

**Zach Barth Of Zachtronics:** Yeah. It's the, the fact that we're, yeah, exactly. So, and rendering is a lot like that. And that we're, there are, there are things about human brains that we're taking into account here and we can take shortcuts because of it. Same thing with like lighting. You know, there, there's lots of ways that you can, this is things that people started figuring out in the eighties and nineties and probably before that too, that you can kind of light, lighting is complicated. The behavior of light is super complicated, but we can kind of cheat. And there are simple models that we can use that actually come progressively, you know, closer to accurately representing light. But, you know, back then it was just like blend and fong shaders or like these classic shaders. Shaders is a term for like graphics programs that determine like how to draw pixels and how to color stuff. And so there are these simple models that people were like, people were really impressed, right? Because it's like, wow, it looks like a real thing in a computer. You know, like nowadays it's all about like ambient occlusion and making it so, you know, like, it was like light is actually scattering all around and bouncing off of surfaces. And it's, you know, you could on one hand calculate how every like little photon of light bounces, but that's, that's hard, right? And that's one of those things that computers aren't good at naturally because it's not like a good sequential problem. And so some people move towards ways that you can calculate that data real in real time, right? Like ray tracing is all about that, but yeah, real time ray tracing isn't quite here for games yet. Or it might never be, who knows?

**Dave Jones:** And, uh, is that because of the processing power required?

**Zach Barth Of Zachtronics:** Yeah, it's, it has, it's not, it's not convenient the way that like the, the, the N squared, you know, kind of the, the, the, what do you, what do you call that? It's been too long, but like the, the, the, the number of iterations you have to do is not convenient for quickly doing it. Um, but they'll do things where like they'll, maybe they'll, they'll fire off those calculations and not real time and then save the result out and then use that as again, like texture data coming in. Um, or you can just paint on something that looks like ambient inclusion and call it a day, like in the texture, you know, we, we did a lot of that with Infinifactory. So all these like fancy rendering techniques we're talking about are things that are generally like, we did not take advantage of because we're, we had like one artist working on, you know, the game for a lot of it. And, and, uh, and when we, when we scaled up, we still had to do it in a cheap way. I mean like, God, like call it. So call of duty, a game like call of duty, like a person, artists, an artist will spend like months and months and months making a model of a gun. Right. Yeah.

**Dave Jones:** That's crazy.

**Zach Barth Of Zachtronics:** Because it's like, it's, it's so big on the screen. Like it's a character in the game is this gun and they take forever to make. And we're like, we don't have that kind of resources. Like we have to make, you know, a game with a very small team very quickly and we have to do the entire game. And so we did a lot of like really cheap techniques, like, you know, just kind of painting on ambient inclusion to make the blocks look. And it's like, yeah, yeah, that'll pass. That'll work. We actually, amusingly, we, our artist was really fascinated with like PlayStation 2 era games because they didn't have a lot of these techniques, but they made some really pretty looking games just like, like by painting on the right stuff. And he's like a painter, um, like a, like a digital painter. Like that's like his kind of focus area. And so we, we took all these old techniques from old games and kind of resurrected them and made a pretty attractive looking game considering how little like resources we had.

**Chris Gammell:** Yeah. Is it possible to... About that though. The, um, I mean, so, so sometimes some of your games also take on the more low res look, right? I mean, like some of that is played, you play to that as well or no?

**Zach Barth Of Zachtronics:** I mean, uh, in the past. So I used to do my own artwork in the past. And so that was like many other indie games, indie game developers before, I guess, uh, before they were doing that thing. A lot of people make pixelated games. Uh, before that I discovered too, that, Hey, as an untalented, not artist, I can make shitty pixel art and it'll pass as like, this looks like graphics. And, uh, and I think you still see a lot of that now with indie games, just because pixel art is accessible in a way that traditional art, like game art is not.

**Dave Jones:** Now we have to ask about this because on your Wikipedia page, you are credited in the first line as basically being the inventor of the genre that Minecraft, that led to Minecraft.

**Zach Barth Of Zachtronics:** Yeah, definitely. How does that? That's the thing.

**Chris Gammell:** So why weren't you Minecraft?

**Zach Barth Of Zachtronics:** Uh, because, so there's, I mean, there's a lot of reasons. Okay. Um, most importantly, I didn't, right?

**Chris Gammell:** I, I actually, I don't know much about Minecraft other than I know it was big, but.

**Zach Barth Of Zachtronics:** It is, it is a very big game. It is perhaps the biggest indie game of all time.

**Chris Gammell:** No kidding.

**Zach Barth Of Zachtronics:** How much is it?

**Dave Jones:** How much did they sell it for?

**Zach Barth Of Zachtronics:** So he sold it to Microsoft for two and a half billion dollars. Two and a half. I'm pretty sure. Jesus. Yeah. Yeah. Right. And that's, and that's after it had been out for many, many years and had made them a bunch of money. And yeah, it's so, so I, I started the genre with a game that was nothing like Minecraft. And I think like, like any kind of creative person, right? Like the, the, the way, the way you achieve creative success is that you, you come up with some ideas of your own and then you look out and see like, where is the, where's the genre at currently? Where, what's the state of the art? You know, like what, what in there would really synergize well with what I want to do. And that's absolutely what happened. It just wasn't me who did it. So, but somebody's got to take that first step.

**Dave Jones:** Yeah, of course. So, so are you well known for this? Does it lead to fame and fortune or everyone's, everyone's, yeah, I was going to say.

**Zach Barth Of Zachtronics:** Well, I, my life is a lot more low key than his. So in some ways I think I am, I'm in a better position. I don't, I don't know if I could have taken all of that.

**Dave Jones:** Oh, you couldn't handle the billion dollars, you know, that would have been.

**Zach Barth Of Zachtronics:** Well, with a billion dollars comes a lot. You get billionaire problems and billionaire problems are serious. So I'm not even kidding. You really like it totally. It just distorts everything from what I've heard. I guess I don't say that with any sort of having been there, but yeah, it's dodged a bullet there.

**Chris Gammell:** I guess the thing that I wonder about is I don't quite, I saw I've seen Minecraft. I'm looking at Infiniminer, which is your game. What is it? What is the difference? I'm sorry. I, I, it looks so.

**Zach Barth Of Zachtronics:** So the difference is that Infiniminer has like a cool mechanic where you build stuff out of blocks and like a pretty terrible game that wraps it. And versus in Minecraft, it has the same awesome block building mechanic, but it has what was actually kind of a novel like mechanic at the time, which is it was once described at a GDC talk I went to as fantasy of labor, which is where you get to do fake work. Right. And so Minecraft is all about like, you go around and you, you punch trees and you get their wood and then you can build stuff out of that wood. And right. And if you just had wood, it wouldn't be as satisfying because you punched that tree and got that wood. And this is sort of like, it's a thing that's going on in game development right now, which is where there have been so many, like there's just been this huge renaissance of like arguably like bullshit game design stuff that makes games super addictive. Right. Right. Like crafting and like, like, like there's all these kinds of genres that are like, especially on PC are really popular and they're kind of descent, like Minecraft kind of got there first. Like Minecraft was the first game to popularize these kinds of things. And I think arguably like, like sure, the block building part is an important part of Minecraft and part of the fun. But like the fact that it was one of the earlier games to really just kind of drill down and be all about these super compelling addictive mechanics. Like I, that's really, I think a huge part of the success.

**Chris Gammell:** Yeah.

**Zach Barth Of Zachtronics:** And it really set the stage for like game development now, which is all about like on mobile games, especially, right? Like it's all about like trying to set up like compulsive gameplay stuff to get people hooked. I don't want to ramble too much because I sound like I'm crazy, but.

**Chris Gammell:** No, no, no. So like I, I told you when I was emailing with you that I actually don't, I don't play video games very specifically because I almost failed out of college because of them. Because I, I. Which one? Uh, it was, uh, Return to Castle Wolfenstein. Uh. Oh, wow. Yeah. Yeah. Not, I mean like nothing special, but it was just like.

**Zach Barth Of Zachtronics:** That's not even that good of a game, is it? I know, but I just.

**Chris Gammell:** You know, and every time I've tried since, it just is the same thing. And I just said, never again. I, like Kerbal, right? So I've talked to, uh, friends about Kerbal. They're like, oh, it's such a great game. I'm like, that's awesome. The space program for those. Yeah. I will never ever play it because. Yeah. I'll go nuts. I'll just.

**Zach Barth Of Zachtronics:** Some, some people say that about our games, especially. They're just like, why would I play this game when I could just write actual code?

**Chris Gammell:** Well, and so that's what I wanted to get towards. So you mentioned like, okay, people doing work, you know, like fake, fake work, whatever you called it. Right. But. Yeah.

**Dave Jones:** They're still playing games. Don't make any.

**Chris Gammell:** So, so where, where is the crossover? I mean, are people, are people learning assembly code from your game? Are they learning electronics assembly from Shenzhen I. Oh, I mean, like what, what do you, what do you see? What do you expect to see from this? Are we going to see the next brand of the next, the next generation of electrical engineers coming from.

**Dave Jones:** I think they're learning and interest rather than they're possibly learning some system skills. I would imagine. I'm sure Zach can set it straight, but I think it's more of an interesting.

**Zach Barth Of Zachtronics:** Yeah. It's like our games are sort of deliberately not, not transferable that we teach, we teach you things that we made up. So that way they'd be easy to teach you. And real life is not so convenient. I was just going to say the exact same thing. Yeah. There is somebody on Reddit who is like, wow, like I'm surprised by how close Shenzhen I.O. is to real life. They started doing some Z80 assembling for the Game Boy. And they talked about, they wrote this huge write up about like, well, it's, it's totally different in these ways. But, you know, like there's some, you know, like, but there are some similarities in the core. Like it's, it's not that they learned how to do it from that, but like it kind of primed them a little bit and they can see like once you know multiple things and you're able to compare them, you know, like it kind of gives you a context to learn new things more easily. Like people who learn lots of languages, right? Like you can say, oh, it's like this, but different as opposed to having to learn it for the first time where it's not like anything you've ever seen before.

**Chris Gammell:** Well, and tenacity as well. I mean, to be honest, it's tenacity, right? I mean, so we talk about a lot on this show. We've had guests to talk about as well. Like electronics is hard because you have to just keep trying it, right? You have to, or coding, you know, programming is hard because you have to keep trying new solutions. And that seems like that's precisely what you're, you're teaching, right?

**Zach Barth Of Zachtronics:** I kind of suspect that's more of a selection bias than an actual like teaching. Like I don't, I think, I don't think our games teach you how to be patient. I just think they punish you if you're not.

**Chris Gammell:** Right, right. But I mean, the same way with electronics though, like, you know, like you don't see people that are impatient, like building huge circuit boards, right? They're, they just, it just doesn't work, right? I mean, like it's. Yeah, exactly. Yeah. There is that same, that same bias. So.

**Zach Barth Of Zachtronics:** Yeah, definitely. I do want to separate, like when I talk about fantasy of labor, like their, their games, like our games could kind of be considered like fantasy of labor, but it's like intellectual labor, there's, there's other, a lot, a lot of other games that are just like, you're just doing like, you're, you're punching trees and stuff. You're clicking a button a bunch, you know, like incremental games are sort of like a purified distillation of this where you're just like clicking a button to get more points. And then you spend those points to get machines that get you more points and like, you know, you gotta, gotta make that number bigger. Yeah, exactly. Exactly. Yeah. Like there's something wired into us where we love gathering and hunting and stuff.

**Dave Jones:** I think we're a very sad, sad species. So I think we're trying our best. We're doomed.

**Chris Gammell:** So what's, what's your take on like dystopian, like a ready player one type stuff? You got any feelings? Oh, I couldn't, I couldn't read that book. You couldn't like it, you said?

**Zach Barth Of Zachtronics:** I couldn't read that book. I couldn't get through it. Oh, I loved it. I don't know. I mean, you gotta be more specific, I guess.

**Chris Gammell:** Like, I don't know. Like the whole, like, I guess it's a, that's another tie to the VR type of thing, but like, you know, it's a VR dystopia where people are all living in the games, but also there's, you know, there's the educational component to it as well. Like that's the, the positive stuff they talk about.

**Zach Barth Of Zachtronics:** Yeah. I don't, I, this is something I actually think about a lot. Cause when I, when we were making educational games, I actually had a bit of a crisis towards the end of realizing, oh God, nobody is learning anything from these games. We're literally just funneling money, like from like by proxy from schools to make games that we think are fun, but like, like nobody's going to learn anything. And it's like, but it was, it was actually, it was pretty hard. I had a hard time. Like we had, we stopped making educational games and I kind of lost interest because it's like, they're not, they're not really working. And cause they, we're making games, but like they have to be fun games. But in the process, like it sort of like loses its ability to be educational because it turns out that like education is not really well defined, like what that means. And I think that's sort of like, to answer your question, the thing I learned through all of these games and making this stuff is that like, you know, like, like games, like escapism isn't evil and education isn't good. Right. And I think a lot of people talk about education is especially like, it's a, like a kind of monolithic valuable thing. Right. But like, it's like education. Yes, exactly. Yeah. Everybody can get behind that. Yeah. Like it's, it's not like, it's, that's kind of not how it actually works. And, and you just kind of can't approach it like that. You can't think about it like it's a monolithic thing and like, it's not, you know, it's, I don't know. So when I, when I think of games, it's like, you know, not all, not all games are, are bad and escapism isn't bad. And like, to some degree, like people need, you know, we're, we're getting all this, this like leisure time through all of our technology, but like, that doesn't mean we necessarily have anything good to do with it. And so in some ways, like making things to do for fun, like is, it's kind of an important thing as much as anything else could be considered important. Sure. Yeah.

**Dave Jones:** I think education is not that valuable unless there is the interest to go along with it.

**Zach Barth Of Zachtronics:** Absolutely. Yeah. And just as like in the service of being a human being, right? Like we, we have to do something, you have to do something to make a living, right? Because you have to be productive in some way that matters to people. And, uh, and you, you often need skills to do that. And, and like, that's, that's it.

**Chris Gammell:** So, okay. So what about, what about this? So people are taking your, so what, the way I first learned about Shenzhen IO is I was on YouTube and I was clicking around and all of my stuff is, all the stuff I look at on there is electronics. And then, so I started recommending these, these videos on there. And then I saw people were using it to build Tetris and I was like, what the hell am I looking at? So what, what's that?

**Dave Jones:** What's going on? So they're using your game about programming to create a program that plays a game.

**Zach Barth Of Zachtronics:** Yeah. So our, our games, a lot of our games are, they're sort of engines in the, like, in the way that like we, we create the set of tools that allows players to emergently combine their parts in order to accomplish a goal. And for the, the core part of the game, we, we tell you what, we give you that goal. We say, you know, like in Shenzhen IO, like in Shenzhen IO is all about building fake electronics. And so these, these, these, yeah.

**Dave Jones:** Right.

**Zach Barth Of Zachtronics:** Close to our hearts. Up your alley. Yeah.

**Chris Gammell:** Me and Dave also often build fake electronics on this show. Yeah, yeah. Ours are probably faker. I don't know. We don't build much.

**Zach Barth Of Zachtronics:** So we, we, you know, we, we, we, we set out these challenges. Like we'll say like the game takes place in, in like the near future. You're an engineer who couldn't find a job because all the electrical engineering jobs are mysteriously gone. And so you, you move to Shenzhen, China to, to get a job and build some stuff because that's what you were meant to do. And, and so, you know, you, you, your character, you go to China and you, you get a little job at this little engineering company that's making, you know, they're making stuff.

**Dave Jones:** And you have to use squat toilets and, you know.

**Zach Barth Of Zachtronics:** I'm like, oh, we don't go into that part.

**Dave Jones:** Why are you going to that sort of dip?

**Zach Barth Of Zachtronics:** Yeah.

**Chris Gammell:** Dave's realism is not, yeah. Too deep, man. Too deep.

**Zach Barth Of Zachtronics:** We, we have been, we have been told that we, we did a lot of research and we interviewed some people. I want to hear about that at some point as well. To capture. Yeah, yeah. We interviewed Bunny like everybody else who needs to know about Shenzhen. But, but it was really good. Yeah. So we, it's about that. So, so you're working at this company and like the product managers there are like, hey, we think there's great demand for a, an electronic sandwich maker that for Americans and like they push a button, it'll make them a sandwich and a little American flag will pop up when it's done. And. You have to say sudo first.

**Chris Gammell:** What? You have to say sudo first, right? Oh yeah. Yeah.

**Dave Jones:** Yeah, exactly. Can you please make it so that if they make an internet of things device, it like explodes and locks them out of the game permit.

**Zach Barth Of Zachtronics:** So we've got, we've got some, some stuff that's kind of jabs at current technology. Nice. Like there's a little buzzer that goes on your VR helmet. So when somebody rings a little doorbell, it buzzes your helmet, so you know, to like stop doing what you're doing in VR and like, like, like that they need your attention. Yeah. Yeah. Come back to reality. Pull up your pants. So we have a lot of, we have a lot of jabs like that. It's sort of like the current trends. I think we, we have, we have some spam. You get spam. All the stories told through email. Yeah. And so you get spam and one of our spam is about antivirus for your house because like your fridge will get infected and all your food will go bad. And like internet of things kind of like, Dave had his food all go bad.

**Chris Gammell:** And he's, he's, he's vacation.

**Zach Barth Of Zachtronics:** Yeah. Was it a Russian hacker or was it just a general purpose? It was a dodgy circuit breaker. Oh, okay. Well, that's, that's, those are old school problems. This game takes place in the future. Russian hackers.

**Chris Gammell:** Yeah.

**Zach Barth Of Zachtronics:** Well, yeah. So, um, yeah. So I forget how we got, oh, right. So, so the challenge is we, to finally awkwardly get back to your question. Um, so, so our, our, we give people these challenges like build, you know, build this VR buzzer. So what it is is that there's an input for, uh, like a, a signal, like a radio is gonna, I think it was like a radio, there's like a radio receiver that tells you when the button is pushed. And you need to create like a little alternating pulse to drive this little like vibrating buzzer thing. So that way the person will know that someone wants their attention. And the puzzle is actually framed as, um, there's a little like story thing that explains it. And then there's a set of timing diagrams. And it says like, here's your input. Here's your output that your circuit should generate. And so we give you this timing diagram with the story and it's your job to assemble microcontrollers and electrical components, like all these fake electrical components to generate the specified output when the input happens. And then you run it through a test suite and then we've verified that your, your thing is what, you know, like the, the, the beauties of automated testing. It verifies that you built what you were expected to do. And, uh, and then you win the, you, you've solved the puzzle. And because you've solved it, we can then, we can then compare your score against everybody else. We can say, you know, how much did all the components cost that were in your, your solutions? You know, like how many years did it cost you to, to, to design your thing? And like each chip has like a little cost on it. And I literally cannot believe anyone does this for fun. Oh, so many, so many people do this for fun.

**Dave Jones:** I was going to say, this seems like the most colossal waste of human, you know, capability in, I love it so much. What are you doing to our species? What are you doing?

**Chris Gammell:** Welcome to the future, Dave. People could be doing real stuff. This is, this is, this is frigging 2017, man. Yeah. This is great. I love it. It is.

**Zach Barth Of Zachtronics:** So the, the beauty I think is that you don't have to, like, it's, it's so, like, so I, I did electronics in college and I did programming in college. And there's a reason that I only do one of those now. And you were talking before about require, like electronics does require a lot of patience and tenacity that I don't have. And I think that's the beauty of a game in which I'm in. Well, in that style, though. In that style. Right. You have patience and tenacity. You've built this. No, I have less. I have strictly less. And that's why I write software.

**Speaker ?:** Come on, man.

**Zach Barth Of Zachtronics:** You're building a huge game. No. But it closes the feedback loop. It does.

**Dave Jones:** You can write a routine and it runs and boom, you get that little hit. Yeah. I've got LEDs. I've got LEDs. Come on. That's cool. Yeah. No. There's a much bigger, there's a much bigger, much bigger threshold hysteresis type level that you have to get through with hardware than there is on software.

**Zach Barth Of Zachtronics:** So by making a game about the joys of hardware, you know, like it's something that like people will dabble with their Arduinos, but they're never going to be able to quote unquote like make a bunch of stuff. And there's also like a story element to it, right? Like you get the story that goes, you get to be part of the story. You get to learn about a subculture of engineers in Shenzhen that is a real thing that's going on now. So like it hits all these different things. We try to make our games be like, I think of it as like, you know, like some games are made to be like really easily digestible. They're smooth. They're round. They're perfectly polished. Like you can't even pick them up because they're just like ours are like really nubbly and they have all these little bits coming off that are interesting and give it texture. And that's what we try to do with our games is make this little package of just like, you can just like immerse yourself into this world where, yeah, you go work there instead of like killing stuff. But like it's still just as real and it's intensely satisfying to the right kind of person.

**Chris Gammell:** If anyone listening right now happens to be in Shenzhen or knows people in Shenzhen, and if you ever, if you ever see this on a resume, you have to call us or email us or do anything to get in contact with because then you know it's going to happen, right?

**Zach Barth Of Zachtronics:** I mean, at some point. We get a lot of jokes about that. People saying like putting, oh, I beat TIS 100. They put it on their resume or something. Somebody has probably. I mean, is there value to that? I mean, like there must be, right?

**Chris Gammell:** Like I refuse to believe this is entertainment only. That's what I'm getting towards.

**Zach Barth Of Zachtronics:** I think that's the beauty of it is that it's entertainment. So I was going to say one thing. You thought that was ridiculous. The game doesn't have any tutorials in it. Instead, it comes with like a now 40 page manual that's filled with data sheets and application notes. We sold it as a binder at the beginning when the game came out. Yeah. So and they're all written. Everybody's like, oh, my God, this is like there's there'll be parts that are missing because you only have the English documentation and you only find out from your Chinese co-workers halfway through the game that there's a better way to do something. And there's there's a data sheet for like a PGA kind of like Gatorade thing that's only in Chinese. So it's completely untranslated. So you have to go online and like find out like what the data sheet says because it's all in Chinese. Like we did all that kind of stuff. You are sadistic. But it's great. It's immersive and realistic. Yeah, of course. Oh, my God.

**Dave Jones:** To answer your question, Chris, is it of any value? It's it's a relative thing. It's better than playing Minecraft.

**Zach Barth Of Zachtronics:** I think there's better in Minecraft, too.

**Dave Jones:** From a resume point of view, if I saw somebody had on the resume, oh, I got one million points or whatever.

**Chris Gammell:** Well, what if they built a 60 someone built a 6502 in Minecraft, though? Like, what about then? I don't know. Like there's there's like nuances to it, right?

**Zach Barth Of Zachtronics:** Oh, yeah, but that's a special case. That kind of takes back to your question about Tetris is that so there is a game. There's a core game in Shenzhen. But the engine that we provide to allow players to solve our puzzles is also an engine that they can use to build their own things. In fact, we provide tools for this purpose. And so there is a in Shenzhen, there's a component where you can load an image into the game and create like a custom LCD screen, like an old like 1980s LCD game. Yeah, yeah, yeah. And like they can be touch sensitive. So when the user clicks on it, you get data back from it about where they touched. And so you can use these things to create your own like open-ended games within the game. And for us, that's like a thing that's fun for players and also like a marketing thing, right? Because when people make something cool, they share it. And then they're like, oh, what's that? Oh, that's a game.

**Dave Jones:** You would share it. Yeah.

**Zach Barth Of Zachtronics:** Yeah. That's a big part of how we do marketing is just to make a game that allows players to be awesome in a way that makes them want to share it with their friends.

**Dave Jones:** I was... That's awesome. I'm going to say here, though, but I can predict the future here that it's like people watching playing video games instead of actually playing them. I can see the same thing happening here with Shenzhen.io. Somebody builds a game in Shenzhen.io and then people don't bother building their own games. They just download and play the game inside Shenzhen.io.

**Zach Barth Of Zachtronics:** That's true with some games. I don't think... Shenzhen.io probably isn't complicated enough. You kind of need something like... There are a lot of spatial constraints in Shenzhen.io that makes stuff like that hard. But there absolutely are games. Like there's a game called Gary's Mod, which has been out for forever. Oh, I've heard of that. And people don't really play that game. Some people kind of play that game, but more so they play games that other people have created inside of that game. Yeah. Oh. And it's like a game that's also a game engine. And there's stuff like that that pops up, you know, like StarCraft, right? Or WarCraft, like those real-time strategy games. There's a map that somebody made with custom rules birthed an entire... Like what is now the most popular game genre? Arguably MOBAs, right? What? So do you know what a MOBA is? No. Okay, so MOBA is multiplayer online battle arena. It's basically a game where you control a character and it's like a 5v5 team battle. And you're trying to... Like everybody has like their own special moves. So like maybe somebody's really fast and can do a lot of damage quickly, but has low health. So if they're stuck somewhere, they'll die instantly. Like you have all these characters that are asymmetrically balanced. And then you fight against other players who are controlling them. So you do like five on five, like real human versus human battles. And this is like a huge, like unbelievably huge genre now. People play esports. People get paid way more than you and I ever will to play these games and win them. But this game genre was actually birthed out of just a map that somebody made like in old real-time strategy games, which is now a genre that's arguably dead. Some of them allowed people to create their own maps, which had their own rules. And so somebody made a custom map with custom rules where you controlled a single unit instead of a bunch of them like in RTS games. And you fight against other players. And like this one map birthed like a genre that now dwarfs the original game from, you know, the games from which it spawned. That's crazy. And that was people playing a game inside a game. Yeah. There's something wrong with the human race. No, no, no.

**Chris Gammell:** That's a million monkeys with a million typewriters problem, isn't it? Like if you give people, if it's a big enough thing and then people want to be creative with it, it's just the medium they're given to do it, right? Yeah. I think that's a positive thing, actually. And that's why systems like yours where you do have these open-ended, I'm sure that that probably breeds it even more than other systems, right? Like you're not going to have a first-person shooter without a map modding type thing that's going to go and create something new, right?

**Zach Barth Of Zachtronics:** Yeah. So a lot of our players are programmers, and so they do very programmer-y kind of things in it. So they might not go viral in the same way as a MOBA. Oh, right, right, right, of course. Yeah. But yeah, I mean, it's like, I mean, right now we're using a tool that was made for a different purpose to record this podcast, right? And it's allowing, it's a creative tool. It wasn't even a creative tool, but it's allowing us to do something creative and make something and share it with people. Right.

**Chris Gammell:** It's like ricochet effect or just, you know, the assets are so worth it.

**Dave Jones:** Well, that's the key word. We're making something and sharing it with people. Like, what's your opinion of these people who just sit there and watch PewDiePie play?

**Zach Barth Of Zachtronics:** Weirdly, he's creating something that people want, right? Like he's entertaining them. He is, obviously. In the same way that people, whoever's listening to this, they're like doing whatever and just listening to us, right? But like they're...

**Dave Jones:** Well, yeah, I'm doing the same thing. Hopefully they're siddering, right? Yeah, exactly. But it's, yeah.

**Zach Barth Of Zachtronics:** Yeah, I think it's exactly the same. And I think it's definitely, from a content perspective, it's cheaper to produce than like a game, right? Like a game takes us at best like four months. For many people, like a lot longer, right? You just kind of have to work at something for months and years and then you create something that people can enjoy. But I mean, it's all content. I don't know. I think our content's pretty awesome. Yes, and I want to get back to that as well.

**Chris Gammell:** So where... So first off... Okay, so these are just kind of adding on to one another. You said Shenzhen was kind of... The Shenzhen IO is kind of from the Valve group, but also just other experiences. What kind of research are you... What are you doing? What are you doing? You say you talked to Bonnie, but like, did you go over there? Did you work there? Like, who... Oh, no. Who is advising you on all this stuff?

**Zach Barth Of Zachtronics:** So first off, I mean, like, we... It's hard to say like, oh, our stuff is so authentic that we know despite having never been there. No, we've actually had like a fair number of people like who were either like expats who worked in China or people who are from China. We're like, wow, this is really like... This is stunning. Like, the developers must have lived there and worked there because it's stunningly accurate. So I'm not just trying to toot my own horn, but trying to establish some of the stuff we've seen.

**Chris Gammell:** I mean, it looks as legit as anything I've seen. So like, that's... But not that much, you know?

**Zach Barth Of Zachtronics:** So we've... Our writer had been to China a couple times, like when he was like in high school and college. And I've actually... I've been to... I went to Japan and Korea, but not to China. But that's where I learned a lot about like the excitement of traveling somewhere where you have no idea what's going on and being completely in over your head. But she's like, we can go to Korea for a couple days. We can wing it. I don't know any Korea. So it was exciting. But like, none of us have ever worked in Shenzhen. You know, I've never really done like an electronics job. But we've been able to... Like a combination of like, you know, I read a lot of stuff on the internet about engineering and engineering culture. And, you know, we talked to Bunny about sort of like the Shenzhen, you know, the same thing he tells everybody about when they want to know about Shenzhen. About just like what it's like with the factories and how like iterative they are and like their unique take on IP that puts them in an interesting position to be able to innovate. Yeah. I'm not trying to take a stance, you know. No, no, of course. I'm not moralizing. Don't worry.

**Dave Jones:** So you mentioned that you had a writer there. What is your team? What is a team made of that you need to make a game like this? So... You said you had an artist, I think. You had a graphic person.

**Zach Barth Of Zachtronics:** Every team has a different composition. We run with... So I do design and programming and like creative direction, like studio head kind of... There's a reason that we're called Zachtronics and my name is Zach. So I have my unique position. And then we have a programmer who does... Also does design. We went to college together. So we've been designing stuff together for years. But they're doing the grunt programming? No, they do the hard programming. He's much better at programming than I am. The guy, the one up the mountain. Yeah, the guy who went up the mountain and came back with a whole new way to make games. Yeah. And then we have an artist, Kyle, who he... I mean, we found him through like a friend of a friend of a friend kind of situation. And he is our core artist now. And he did the art, like all the art for Shenzhen.

**Dave Jones:** So how do you draw the art? Do you like sketch it on a tablet or something?

**Zach Barth Of Zachtronics:** So yeah, he uses a big, like a big honking Wacom tablet or Wacom tablet. And it just drives directly and controls the mouse, but has like information about like pressure and pen tilt and stuff. And so he, you know, his approach is very like painterly. And so he just kind of paints stuff and uses brushes and just like a real painter would cover paint with other paint to create like blended and stuff that he just paints stuff. And if you look at Shenzhen, you'll see it's not rendered. Like it's not 3D rendered. It's all 2D sprite work. And like all the little like highlights and low lights and lighting information is all painted in. And they're all just 2D sprites and we just composite them in code. So like he's very like 2D painterly. He also did a lot of the art for Infinifactory. So where we actually, he would paint like a, like do a little sketch of what the 3D block should look like. And then we shipped it to a studio in the Philippines that did the modeling for us. And then they would ship it back and then he would paint the textures to have all the little details that he wanted. And so like he's not much of a 3D guy, but we were able to work around this by having somebody else do the hard part for us. That's great. That's three people so far. And then the fourth is our writer who is Matthew. He does writing and he does music and he does sound. And so like basically like the whole, like the tone, like he, the tone like both from like a story perspective and musical perspective, which in my mind are like super interleaved, right? Like you can tell people one thing with the story, with the words, but your music needs to go along with that and like inform their emotions on it too. And so the fact that we have somebody in-house doing both of them now, when we used to kind of outsource a lot of that stuff has been like, I think a huge improvement for our process.

**Dave Jones:** Can you see our games that complex these days or people have such high expectations? Is it impossible for a single person to do it all and produce a compelling modern game?

**Zach Barth Of Zachtronics:** I mean, I would say anecdotally, not at all. I mean, there's a game that just came out last, I guess like last year or the year before called Stardew Valley. It was one guy who worked on it for years and years and years and it came out and he's now like a multimillionaire. Good on you. Right? It did very well.

**Dave Jones:** Is that the exception?

**Zach Barth Of Zachtronics:** Every indie game is the exception. Right. Right? Like you can't just go into and just say, I mean, honestly, it's like that with a lot of businesses, right? Like you can't just go in and say, I'm going to be a successful, like this doer, right? Like you have to have an angle. Electronic YouTuber. Yeah, yeah, exactly. Yeah, yeah. You have to have the right set of circumstances that make it possible. And it's especially true with games, but it's also true with literally everything else.

**Chris Gammell:** Yeah. Man. Fascinating. So, okay. So, I actually remember the first one that I saw of your stuff and I was super confused and I don't actually know how to say it.

**Zach Barth Of Zachtronics:** Constructor? Oh, Ruck Engineer.

**Chris Gammell:** Ruck Engineer? Is that how you say it?

**Zach Barth Of Zachtronics:** Ruck Engineer? I don't know. It's like a made up. It's supposed to look like it's German, but it's really not.

**Chris Gammell:** Yeah.

**Zach Barth Of Zachtronics:** That was like my first big popular game that was on Hackaday. Yeah. Years and years ago. That was how we got started is that I made that game and I managed to get it on Hackaday and all of a sudden a bunch of people found it and were looking at my stuff and they were all like engineers and engineering type people. Yeah. And it took off from there.

**Chris Gammell:** That's literally what you actually started though too?

**Zach Barth Of Zachtronics:** Kind of. I mean, I'd made games before it, but that was the game that put me on the map, quote unquote. I mean, it would still take years and years and years until I made like a dime off it. But that was what got it started. Well, I just remember. And that was back in like the blog era of internet.

**Chris Gammell:** Yeah, right. I remember because it was like, so it's like you're probing on a board for like security stuff, right? Or is that another one?

**Zach Barth Of Zachtronics:** It's about reverse engineering. So there's only like four levels, but each level is a device that you have a voltage quote unquote. It's all like fake electronics, but it's probably the closest to any kind of real electronics that we've ever done. You have a voltage probe and you also have a thing that can generate voltage pulses. And then you have something that's kind of like a JTAG kind of thing where you connect it up and you can read and write registers inside the chip. And then you have a serial port where you can read and write serial data. And there's all these little test points in the boards and you hook up the probes and try to figure out what they are and what they do and how the device is working. And you try to like get it to, you hack it to get it to do something.

**Chris Gammell:** Yeah.

**Zach Barth Of Zachtronics:** And the story of it, you're like a, you're an engineer for like some group of like, like rebel group that's fighting against, like, I don't know, it never goes into explaining any of it, but you're part of some sort of like military resistance and you're hacking stuff. And so like you hack open a lock and then you hack them open, you hack like past like a biometric thing on a gun. And then you, you hack like a, like an encrypted like communicator and try to find out a message and you, you hack a, like a bomb that's about to explode in your face. Yeah.

**Chris Gammell:** And yeah, I think I heard about this from, from Joe grand. Maybe we talked about it when he was on the show too. So he was on the show a long time ago, but yeah, I think he was the one and I was, cause he was, he does like a lot of the J tag reverse engineering stuff. So another, another fan of your work. I just remember being very frustrated with it.

**Zach Barth Of Zachtronics:** Yeah. It's the game, like the further back you go in our back catalog, the more frustrating and awkward our games get. We have brute forced our way through learning how to make more usable games. And even then I think a lot of people would say we're not there yet.

**Dave Jones:** So you, so you get feedback on that, like this is too hard and I just give up.

**Zach Barth Of Zachtronics:** Oh yeah. I mean, when it, when we started, it was, we got feedback from people complaining about stuff. We've since like a long time ago switched to metrics. After, after space chem, after space chem came out, we, I got invited to go out to lunch with somebody, with Robin Walker from valve. And this was way before I worked there. And, and he was asking me a bunch of questions. He's like, how do you know, like if your levels are working? How do you know if it's too hard? I'm just kind of like, uh, like I didn't have a good answer. And, and that was sort of what it dawned on me is that like all these kinds of things that we'd like to know, we could totally figure them out if we started instrumenting our, our, our code and adding metrics and finding out what people are doing. And so now.

**Dave Jones:** So, so it feeds data back to you as it does. It does. Right. Okay. And like everybody literally. Some people don't like that though.

**Zach Barth Of Zachtronics:** Yeah. Every, every application you run is feeding data about you back to headquarters. Yeah. Sorry. So yeah. Sorry. Yeah. We, we keep it.

**Chris Gammell:** Yeah.

**Zach Barth Of Zachtronics:** Yeah. We, yeah. It's weird. It's creepy. Right. You realize like if we're doing this casually, literally everybody else is too. And if we keep it anonymous, um, it's for people listening on the amp hour.com right

**Chris Gammell:** now, we're also tracking you to Google analytics and listen. And like, it's like, of course, right. We all do that. Yeah. Anything streaming for sure.

**Zach Barth Of Zachtronics:** Yeah, definitely. So the most important thing, the only data that I really care about, honestly, is the, the data that has, has benefited us the most so far, which is knowing which puzzles people beat, which they don't, how long it takes them. Uh-huh.

**Dave Jones:** Um, that would be the main metric would I think would be how long it takes.

**Zach Barth Of Zachtronics:** Because it's a puzzle game, especially we really want to know. We used to just have to go off people saying like, this level's too hard. Uh, and like, that was it. That was all we could do. Right.

**Dave Jones:** And like, have you pulled out data where there's like, you've found out what the attention span limit is before people give up? Like, is it 10 minutes?

**Zach Barth Of Zachtronics:** Is it? I don't know why. That's the problem with metrics. You never know why anything happened. You just know that it did. So the one, the one thing that was super useful is that when we launched Infinifactory, we put a survey at the end of every level. Ah, that's a good idea. And so we were collecting objective data, but we were also asking people subjective questions. And we were able to find stats that correlated with like answers to questions. Like it turned out that there was a pretty direct, we're not really statisticians. So like none of this is really like true. What was the n factor? Zach? Yeah, yeah. I don't know. 93% confident. I wish I, I don't even know. I would say I wish I knew, but I don't even care. So I'm sufficiently confident that there is a link between players who self-report that a puzzle that they just beat was too hard with the number of people that load up a level and then never beat it. And just like usually just quit playing the game. Like as they get to that puzzle, they're just like, nope, I'm done with this game. Right. It actually correlates pretty directly. Like they spike in the same place with people saying like I was able to beat that level, but I think it was too hard. Because you really can't take the opinion of somebody who hasn't beaten something. Because of course they're going to say it was too hard because they gave up. But somebody who is able to beat something and then says, no, I was able to beat it, but that was too hard. Right. Like that's more of the kind of thing we want to calibrate for. And so we use that now. And so with Infinifactory, it was really obvious. We could see these huge spikes where like it turns out that for a game, even though the game gets harder, people complaining about the levels and saying they're too hard, should actually be flat. Right. Because you want people to be constantly challenged. And we could actually see that for the most part, it was constantly flat. And then there were a couple levels where it spiked up just for no reason. And that told us that those are the puzzles that we should change and make easier.

**Chris Gammell:** So do you actually go and change the game, the puzzles then to make, like do you update the games over time then?

**Zach Barth Of Zachtronics:** Oh, yes. Absolutely. I mean, so the beauty of releasing a game on PC is that we could release five updates a day if we wanted. On Xbox, they charge you like $10,000 for an update, like if you do it too often. Like it's crazy. They charge you tons of money and you have to go through cert again. And you have to like go through all these. Like on Steam, it's literally I push a button on my computer. And then like five minutes later, everybody has the latest version of the game. And I can do that as much as I want, as often as I want, whenever. It's amazing. So we push changes all the time. And with Shenzhen specifically, I had a really hard time figuring out like how, like what order to put the levels in for Shenzhen because there's not really like a direct increase in skills. Like it really is just like build this thing, build this thing, build this thing. And like it can vary wildly. And so I was constantly throughout the game rearranging the puzzles in it and adding them and changing them.

**Chris Gammell:** And so, okay, critical question then. Does that mean that at some point you can have an engineer in the game listening to the amp hour while they're working? What does that mean? To this show?

**Dave Jones:** You could stream our audio directly into the game.

**Chris Gammell:** While your coworker in Shenzhen is, you know, working.

**Dave Jones:** Or you can play EEV blog videos in a side window up on the screen because this is what real engineers do, right?

**Zach Barth Of Zachtronics:** We're just trying to, you know, abuse the power. You're proposing features. Yes. I guess so. I'm sorry. We're done active development on the game right now. So we're not planning to add any features. Yeah. Next time, maybe. All right. Fine. I do have a funny EEV blog story, which was when we were ramping up on Shenzhen, we had a little party at my house where we hung out and we went out for dumplings and we watched a bunch of videos on YouTube about all the things that were related to this game. And part of that was explaining how electronics works to our artist and our writer. And so the way to do this, of course, was to fire up some videos of EEV blog where you're tearing stuff apart. And it's like, oh, yeah, you see that thing right there? Like, that's what that looks like. Because we're really going more for like a visual feel than anything. Like, our artist doesn't actually need to understand electronics because it's not real, but he needs to know what electronics look and feel like. Wait, you did this at the end of development? After you were done? No, the beginning. Oh, the beginning. Okay. Yeah.

**Dave Jones:** And he needs to know what stuff to get excited about and what stuff not.

**Zach Barth Of Zachtronics:** Exactly. And so we, specifically the video we watched, I'm pretty sure we watched the whole thing, was tearing apart the weird German prototype touchscreen computer. Oh, that tablet thing. And it was just like glued together and it just kept getting worse and worse the further you go. Yeah. So we watched that.

**Chris Gammell:** That's awesome.

**Dave Jones:** That has now reached almost a million views. That's what my second most popular video now. That's crazy. There you go. Oh, man.

**Zach Barth Of Zachtronics:** Yeah. So that informed a lot of Shinjin, apparently.

**Chris Gammell:** Brilliant. Yeah. All right. Great. Thanks, Zach. This is great. I'm not going to hear about this all the time for the rest of my life now. So, okay. So one last question. I am, we could talk, I could talk a year off all night and we shouldn't do that, but. I don't care. I have no plans. I am so curious just about this educational piece. I know that you said it's not important, but like there's got to be something here, right? And I mean, I do education. Dave does education. I'm very interested in this. But like, what about just the assembly, right? So you're doing, so another game, TIS 100, right? That's, that's actual, that's assembly. But like, is it, is that legit? I mean, is that, is anything real? That's legit. That's legit.

**Zach Barth Of Zachtronics:** That's legit. That's legit. Yeah. So if you could see me right now, I'm kind of smirking, right? Because like, I mean, like our games aren't, our games aren't educational with a capital E, right?

**Chris Gammell:** Yeah. I don't want it to be like, I don't want it to be institutionally educational. I just want it to be like glancing education. I want someone to be like, oh, okay. I think I get this now. I, it's, I don't, you know.

**Dave Jones:** Why, why didn't you use real Atmel or microchip opcodes, for example? Why, why not base it on a real processor?

**Zach Barth Of Zachtronics:** Yeah. So the, the interesting thing. So this is actually a thing a lot of people, we actually get asked this question a lot when we talk about this game with press people and they're like, why didn't, you know, like, why, why didn't you like, or what language did you pick? Or why didn't you use an existing language? And the reality is that from a game design perspective, the language is part of the game design. And in fact, it's the most important part because the, the language sets out what you can do and it sets out how you learn it. And it actually dictates everything about the game is that up until like the last minute of developing Shenzhen.io, we were changing the language and specifically like there were, oh God. So this is, it's sort of a nuanced thing with the game. So we have two ways that there's two kinds of inputs and outputs in Shenzhen.io. We have, this is, this is a funny thing. Okay. So originally there were three, there were analog, digital, and something we called X-Bus, which is like our version of like a, like an SPI or an I2C kind of thing. Right. And we had, I'd made this distinction between analog and digital signals because, you know, like not, not every pin on a microcontroller is an analog to digital converter. Like there, there are limitations there. There are asymmetries there, but like trying to explain to our writer, like the difference between analog and digital, like he just was not. But like the reason why is because there's really not like a difference. Like they're kind of like, like digital is just like, the idea of a digital signal is just kind of like a convention built on top of the fact that everything is analog. And, and, and so like, we're just like, wait, this isn't helping at all. Like we should just get rid of, you know, if we want to do like a sine wave or a square wave, like on, on like an analog thing, we can, it's fine, it'll work. And so we simplified that the notion of them being separate just down into one thing, but we couldn't call it like analog because it's not really analog. It's, it's actually discrete between zero and a hundred, you know, like incrementally integers. And so we called it simple IO because it's simple and it's just a number. And the way it works is that when you output a simple IO value, you just set it and it's just constantly outputting that value until you come back to it later. Like it's latched. Um, and then, and you can read it at any time from another thing, reading it. And then we have X bus, which is like our, I sort of like our SPI I2C kind of thing where you can like a processor can go to write, but it won't actually, it'll block until somebody else goes to read, which will also block if there's nobody else writing. And then, but once there's both a read and a write, they'll stop blocking and then they'll transmit the value. And like, it's, it's a clean, like, you know, it's a synchronized protocol. And this allows you to send values between different nodes without having to worry about timing. Cause it'll just automatically pause until, but we have this extra, and that was something we did in, in TIS 100. Everything was the equivalent of X bus that it was, you were, you were programming this like multi-core computer with like an insane number of cores, but they were all synchronized and could send data back and forth. So sort of like a transputer architecture or like a green arrays kind of chip.

**Dave Jones:** Wow. Whatever happened to transputers? We made a game about them. That's why they were the thing back in the eighties.

**Zach Barth Of Zachtronics:** Yeah. Well, they're coming back. Thanks to us. So, but yeah. So, so we have, we have some blame on X bus and, and now I'm struggling to remember why I started talking about this.

**Chris Gammell:** Well, just the, the, I was asking about the realness of the, of the assembly language. Or, and Dave, that's why, why you said, because you were changing the language up until the last minute. Oh, yes.

**Zach Barth Of Zachtronics:** Right, right, right. Okay. Sorry. So, so there's also this thing that makes it more complex in Shinjin IO, which is that there's timing diagrams. And so the way you kind of do it, the way you generate a square wave is you'd, you'd write, like you'd write a value of a hundred to your simple IO pin, and then you'd sleep for one time unit. And then you write a value of zero, and then you sleep for one time unit. And then, you know, that would do what you would expect. That's kind of like a microcontroller-y thing. You're bit banging out like a square wave. And, and, and we wanted to have that be a thing. And then the question comes like, what happens when things are blocked? And then like some, like, so say you go to, like you have one, you have two nodes. One goes to write to the other one with X bus, so it's blocked on the right. But then the other one goes to sleep. Well, naturally the thing is just that, like the, because one of them is sleeping for one time unit, and the other one is blocked on that other one, time would just advance while it was blocked, right? It's kind of an abstract concept. It's hard to explain. But the idea that like when something is blocked on a reader or write, time should be allowed to pass if everybody else is sleeping, because it kind of simulates, like, we're not actually, we're not simulating stuff in discrete steps, like a thousand, you know, microseconds or whatever, you know?

**Dave Jones:** I guess the problem here is that Chris, both Chris and I can... We're trying to solve the actual problem here. Imagine that all this is possible by simulating a real microcontroller.

**Zach Barth Of Zachtronics:** Yeah. So... So why not? Yeah, well, yeah, exactly. So, so the problem...

**Chris Gammell:** It's less fun, it sounds like, I mean, like, honestly, it sounds like it's less fun and less flexible and less, you've got a lot of other crap to deal with, honestly.

**Zach Barth Of Zachtronics:** Yeah, well, so we get to the thing that I... I'm almost done. I'm sorry, I'm wrapping up. So, so we had this problem where everything could get stuck waiting on each other and then time would pass and none of our playtesters could figure it out. And it was like, from a programming standpoint, it was totally correct. And some of our really advanced players who were playtesting it totally understood and most of them didn't. And so we actually had to change the language and change the way that like the architecture worked in order to like make it behave in a way that people were able to learn. And if we were using an off-the-shelf language, we wouldn't have been able to do that.

**Chris Gammell:** Right. You would have put like a tool tip or something like that to be like, no, you have to do this now.

**Zach Barth Of Zachtronics:** Yeah, exactly. A little Microsoft paperclip pops up and helps you. That's sort of the beauty. Yeah, exactly. Right. Honestly, we actually, we have a mascot called Chippy. Who's a chip. Who pops up and offers you tips. But they're interface tips. So it's appropriate. Oh, it's all tied together. Oh, God. Yeah, our mascot. Somebody cosplayed us and there's a picture on Steam. But yeah, so. It's fantastic. The beauty of. I cosplayed. The beauty of these games is that we're creating the entire system and like a real, if we were actually trying to teach something real, which was the case when we were making educational games, you don't get to tweak your system. You just have to. Yeah, yeah. If there's something that's hard to explain about starch metabolism, you just got to hike up your pants and explain it anyway. And like if people don't get it, well, that's on them. Right. Like, and versus we're allowed to kind of change the problem to suit our solution. And, and that's why, that's why I wouldn't call our games like educational with a capital E. But like in reality, like you start getting into some pretty hairy stuff about like, well, what does educational even mean? Edutainment. But there's no point in calling it that because nobody wants any of that. Right. Right. Yeah, of course. Okay.

**Chris Gammell:** So I'm going to pull another fiction reference back in here. Have you ever read Diamond Age? How about that one?

**Zach Barth Of Zachtronics:** Oh, yeah, absolutely. That was actually, the idea of that was hugely inspirational when we were creating educational games.

**Chris Gammell:** Okay. That's awesome. So if people don't know, there's basically a primer in there where it interacts with the child using it and that helps to learn. But like what you're talking about, you could keep doing, you could keep like modifying this language so that it, you know, goes more towards your, I don't know. Like, yeah.

**Zach Barth Of Zachtronics:** But there's almost no value in getting, making a bunch of like, you know, AVR programmers, right? Like. It's true. I know. Like it's just not, and I think that's kind of the thing is with any kind of education you're assessing, like, like it's easy to just say that like it's good for the sake of education. But it's like, in reality, it's like, oh, like we don't need to teach those skills, right? No, we don't. Because no, there's hardware and software platforms out there that do that. And it changes all the time. And people pick it up if they need to and they won't if they don't. And it's like, we're really here trying to make something that's, that's fun, but in a way that maybe is not, a way that is different, like fundamentally different from a game about murdering people.

**Chris Gammell:** Well, I like that. But I think maybe even at the end of the day, again, they might be learning all these other things that like, like you said, AVR, you don't need to teach AVR because that might go away some point, you know, or anything could go away at some point. But if you teach the underlying concepts and the, you know, you kind of train the tenacity muscle and, you know, like all those other things. I know you'll never call it educational, but I, damn it, I'm going to think of it as educational because I don't know, I'm going to tell everybody about this thing. Like, it's crazy.

**Zach Barth Of Zachtronics:** I, I kind of feel like there's a notion of like how maybe not educational something is, but how enriching it is. That's a much better word. We all know that there's some entertainment out there that's like junk food. Yeah. And there's some of it that's a lot, that's less like junk food. And like, you know, it's on a spectrum. It's up, it depends on who you are. And like, it's, you know, so we, I like to think we're making something that is healthier than a lot of the other options out there. Certainly. I mean, I'm certainly a snob, right? Like I, I hate mobile games. I think they're like, you know, a vast majority of them are a blight on society. I used to feel really conflicted because I was like, I'm a game designer and they're a game designer. Are we doing the same thing? It's like, no. Like people who make slot machines are also game designers. You're trying to justify your existence. Yeah.

**Chris Gammell:** Like the, like in Rick and Morty when Jerry's just popping the balloons on the, on the tablet. He's just, that's all the game is, is popping balloons.

**Zach Barth Of Zachtronics:** Yeah. Yeah, exactly. And it's like, they're, they're making a different product. They're doing a different thing than we are. It's okay. Like it's, I don't have to compare myself. I don't have to feel bad because they make like buckets of money doing stuff that I would never do. Bastards. Yeah. It's okay.

**Chris Gammell:** You did say too, like, so when we were talking, you were, you were like, you were, you seem like you were more encouraged to come on the amp hour versus like a video game podcast. Is there like cultural stuff that's different? I mean, like, I know that we are not video game, obviously, but like, is there something about the video game industry that is not fun?

**Zach Barth Of Zachtronics:** Games are kind of boring, like as a topic, right? They wouldn't get it. They probably wouldn't get it. A lot of them don't get it. And honestly, I don't get this stuff, Dave. I don't know what he's doing. If you guys, you guys should play this. Honestly, it would be awesome to see Dave, especially see you do a let's play of the beginning of Shenzhen.io. Let's play. Like, it would be incredible because you could complain about all the stuff in it. That's ridiculous. That's easy content, actually. It is.

**Dave Jones:** I'm looking for some, I feel lazy at the moment. I'll do some easy content.

**Zach Barth Of Zachtronics:** I'll send you guys copies. That's not, that's easy to do. Yes, please. Yeah. So, okay.

**Dave Jones:** It's for Windows, is it? Because I'm a Windows person. Is Windows, Mac and Linux? Yeah. Okay. Yep. Yeah. Definitely. Yes, please. I will do a let's play.

**Zach Barth Of Zachtronics:** Oh, I was going to say, these games come from a place of being passionate, not about gaming, but being passionate about engineering, honestly. And like, I express myself through games as a medium, but it's really about like, I honestly don't have a passion for games in general. Like, there are people who do, and you can see by the games they make, they're very gamey games. Like, this is all, I have a passion for things about. This tastes a little gamey. Yeah. Yeah. Yes. Maybe a little bit, but yeah. I don't know. It's a passion for engineering, and I feel like that's something that's easier to talk about when we're focused on the engineering and we can talk about the engineering part.

**Zach Barth Of Zachtronics:** Yeah. Yeah.

**Chris Gammell:** Well, Zach, I, this has been the most unbelievable and wonderful discovery that we found, we found out that you're doing this stuff. Obviously, I'm so glad you are doing this stuff. I mean, whatever. Me too. If it's enriching, if it's education, I don't care what it is, it's awesome. That's all I know. And thank you for doing this. It's really cool. Yeah. I'm glad you guys appreciate it. Where can people find you and how do they, how do they purchase this game? Because I think some of the people listening are going to be like, hell yes, I'm doing this.

**Zach Barth Of Zachtronics:** Oh, yeah. So, yeah. For the record, yeah. Even if you've never played a game before, these are a great way to start playing a game if you're also an electrical engineer, because you've got the hard part down. You just have to figure out the part that all the 10-year-olds manage to figure out.

**Chris Gammell:** Right, right, right.

**Zach Barth Of Zachtronics:** So, all of, if you go to zaktronics.com, you can find all of our games. The best way to buy them, we don't actually sell them directly. They're available on a platform called Steam, which is like the world's biggest like game buying platform for digital games. So, what you do is you go on Steam's website and you sign up for an account and then you'll download the client. And I know, it's pain in the ass. It's DRM. You make a Steam account and then you can buy games on it and it adds them to your library and then you can download them and play them from anywhere. And this is by far like the best way.

**Dave Jones:** My enthusiasm level, sorry, has just dropped 10 points.

**Zach Barth Of Zachtronics:** The other way to buy most of our games, but not all of them, is on a site called like Good Old Games or the Humble Bundle Store where we sell DRM-free versions of most of our games. And you just, you make an account so you can give them money and then they just send you an installer that you can download.

**Dave Jones:** That sounds, that's my level.

**Zach Barth Of Zachtronics:** But Shenzhen.io is not yet on GOG, but it's on Humble Store. So, if you need DRM-free.

**Dave Jones:** Anyway.

**Zach Barth Of Zachtronics:** Okay. Yes.

**Dave Jones:** All right.

**Zach Barth Of Zachtronics:** Yeah, but you want the Steam version because it has leaderboards and then you guys can add each other as friends and then you can compete with each other. And so, this is the thing that's benefit, you know, the upside of DRM is that you get fun free features for giving away your soul and you can compete with each other. So, when you beat a puzzle, you'll see that, you know, Chris, for example, you'll see that Dave did better than you.

**Chris Gammell:** I am so terrified that my fraudulent nature will be called out. And in big block letters, you know? Yeah.

**Zach Barth Of Zachtronics:** Or maybe Dave's fraudulent nature will be called out in big block letters. You'll have to find out. Yeah, that's scary.

**Chris Gammell:** Awesome.

**Zach Barth Of Zachtronics:** But yeah. And my email, honestly, like if anybody gets confused with how to buy our games, my email address is on our website at zach at zachtronics.com. You can email me and I will tell you how to do it.

**Chris Gammell:** Yep.

**Zach Barth Of Zachtronics:** Awesome. We're very easy to reach.

**Chris Gammell:** That's great. Well, Zach, thank you so much. Thanks for having me. It's been awesome. I guarantee we'll talk to you soon because I want to talk more about this stuff. Sounds good. All right. Thanks, man.

**Dave Jones:** Thanks, bud. Catch you next time. Bye.
