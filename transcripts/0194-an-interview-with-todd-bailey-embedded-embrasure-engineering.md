---
episode: 194
title: An Interview With Todd Bailey - Embedded Embrasure Engineering
url: https://theamphour.com/194-an-interview-with-todd-bailey-embedded-embrasure-engineering/
---

**Todd Bailey:** This is The Amp Hour Podcast, recorded April 14th, 2014. Episode 194, with guest Todd Bailey, Embedded, Embrazer, Engineering.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Todd Bailey:** And I'm Todd Bailey. I'm an Embedded Systems Contractor in Brooklyn, New York. Hey, Todd. Hey, Todd. Welcome to the show. Hey, guys. Good to be here.

**Chris Gammell:** Forgot the most important and Cleveland-ish native, I believe.

**Todd Bailey:** I can't claim bone thugs as much as I'd like to.

**Dave Jones:** Well, that's okay. But he doesn't live there anymore, so it can't be that great. Oh, no. No one ever says great.

**Todd Bailey:** Well, this is a problem with Cleveland people in general. It's that, you know, the good ones tend to go. No offense.

**Chris Gammell:** No, it's okay, man. It's okay. It's okay. Oh, dearie. So, it was good talking to you. Well, you know, it's been real. Yeah, all right.

**Todd Bailey:** I'll see you around Thanksgiving. Yeah, that's right. We'll have a beer.

**Chris Gammell:** So, yeah. So, I met you. Obviously, you come back for holidays. And I think I actually started hearing about you from all of your interest in Jim Williams stuff and analog stuff. So, you're the weird mix of, like, analog and embedded. What the hell's going on with that?

**Todd Bailey:** Well, all right.

**Dave Jones:** It's called normal electronics, Chris.

**Todd Bailey:** I would say to a proper zealot, right? There's a continuum, right? Like, at the one end, there's, you know, a diode with a P and an N, right? And then at the other end, there's C, which is talking to, you know, a lot of P's and N's. But it's all electronics.

**Chris Gammell:** Yeah, okay. I like that. So, you take a holistic view of the industry and all the way up until you start writing high-level code and then you start running away like me.

**Todd Bailey:** Yeah. I mean, I've even had to do that, too. You know, it's not my favorite thing. You know, I think it was Jim Williams, maybe, or somebody who said my favorite programming language is still Slaughter. It's from the Jim Williams book. It might not be Jim, but I prefer to work in hardware. But anymore, it's a rare day where a circuit is all analog.

**Chris Gammell:** That's true. Yes, I agree with that. So, how did you get here? Because that's another thing that I'm interested in with you is your background, getting to the point you are now. So, what's your background?

**Todd Bailey:** So, I'm a contractor now, and I started out – I think I know the story that you want me to tell. And I started out – my degree is in English literature. It's from Oberlin, which is a college in Ohio, which is a hootsy-tootsy college that mostly teaches kids how to have funny haircuts. It's true, folks. It's true. No offense, Oberlin alumni. They're not listening.

**Chris Gammell:** Which is why it's so interesting, though, right? Honestly, like I heard that the first time I met Todd. I'm like, oh, wow. That's just an interesting point.

**Todd Bailey:** Yeah. So, I started out going there, and my degree is mostly in, you know, postmodern literature and what have you. And it was a great degree, and I was happy to get it. But during that time, my dad was an electrical engineer, and I grew up – you know, I had one of those 20-in-1 electronics kits. Yay. And, you know, I knew how to use a – yay. And I, you know, I knew how to use a multimeter from science fair projects and stuff like that. And in college, I worked doing sound. You know, it was a time when I still thought that was cool. But the good news about that was is it got me repairing amplifiers and using an oscilloscope. And towards the end of my college career, I took one class, and I weaseled my way into a class in digital and analog circuit design that had Horowitz and Hill as the textbook. Which was – I am sure that everyone who's listening to this knows of Horowitz and Hill, but if you don't – Yeah. Well, it's the book. So, I think that had a lot to do with it. I had two really great professors in that class, and my first – you know, I got my hoity-toity degree in English, and my first job at a school was in a stereo repair shop.

**Dave Jones:** Because there's no jobs in literature.

**Todd Bailey:** Well, there was a screw-up, too. I mean, I got out of school, and what I really wanted to do was be in a rock band, right? Right. So, I spent a lot of time, you know, writing on a typewriter about rock music, like a doofus.

**Chris Gammell:** Like an Almost Famous? Almost Famous, yeah. James Cameron. Right.

**Todd Bailey:** Name a bad rock movie, and I've probably seen it.

**Chris Gammell:** Detroit Rock City.

**Todd Bailey:** Almost seen it. Both Detroit Rock City and Almost Famous made it into my thesis. Nice. Anyway, so, I spent a lot of time screwing around, and I worked repairing stereos because I wanted lots of time to, you know, waste playing scales in my basement. And during that time at the stereo repair shop, you know, you spend a lot of time. Again, one of the reasons I think I liked those Williams books so much is there's an essay called The Importance of Fixing, right? And I read that essay, and I was like, this man has the right idea. Because, like, sitting around with your hands inside a broken thing and getting shocked and getting cut and, like, you know, wasting a bunch of time and looking at similar circuit topologies over and over and over again is a great and humbling experience. I agree. And, like, five-time timers and stuff that everybody starts with in analog. And I was probably 22 at that point. And, you know, as time went by, I kept doing that sort of thing, and I kept working at, you know, dumb young person jobs. And, uh... Such as? I worked at... After the stereo repair shop, I worked in a bar.

**Chris Gammell:** All right, yeah, yeah. Is there a record store in there, maybe?

**Todd Bailey:** I actually, I worked in a club. I worked at the Empty Bottle in Chicago. Nice. Again, cultivating my cool points, not exactly cultivating my engineering career much. This is the stuff that doesn't make it into my LinkedIn profile.

**Chris Gammell:** I was going to say, though, too, like, Todd has successfully already bridged the gap between engineering at this point or, you know, even just technical stuff at this point to being able to meet people of the opposite sex. That's pretty good. That's pretty good to start with, so...

**Todd Bailey:** Well, you know, don't... No comment. Right. So, anyway, during this time, I got into building bigger and bigger and goofier and goofier circuits. Most of them were audio-related, and at some point... The girls went away. Yeah. At some point, the girls didn't show up anymore. There were never a whole lot there to be given. It was a small distance to travel. Right, right. Okay. So, I built these synthesizers, and at some point, I... When you build a synthesizer or an audio device and you want to have a bunch of functions in it, you usually end up building a sequencer or a set of switches or something like that. And I was like, God, it is so annoying to have to make these big boards of 4,000-series CMOS logic. There must be a better way to do logic in a smaller package. And I was like, oh, well, you know, I could learn to program. And it seems... Oh, no! But I bet it would be candy. And the funny thing is, you know, I got a... At that point, it was probably 2001 or 2002, maybe. And I got a PIC microcontroller and learned assembly for it. I programmed a little bit for the Commodore 64 a long time before that. But it was the first, like, you know, honest-to-goodness programming that I had done or that I was actually remotely interested in. And the funny thing is, you know, no one really cared that I could... Like, at that point, I knew, you know, like, I could make... Like, I made a really simple RFID circuit at that point. Nobody really cared about that. But people did care all of a sudden once I could program an assembly. And so I would get asked to do odd jobs for people and build weird stuff for people. And I ended up meeting a guy at a bar who was an engineer at a toy company. And it was this... It was... I remember, you know, there were no Arduinos at this point. And I think it was some listserv that a friend of mine sent me a link to. And it was for artists who use microcontrollers in their art. And I was real curious about this. And so I went to it and I met this engineer. His name is Dima. He's a professor now. And he was bringing in a USB oscilloscope. And he was going to show everyone his USB oscilloscope. And I had built some stupid microcontroller circuit that, you know, I think it took serial input and changed light colors or something. It was not very impressive. But, you know, I brought it in and he brought in his oscilloscope. And I started talking shit about his oscilloscope because I was like, look how terrible the display on that thing. How does anyone debug a circuit with this? And, of course, he's really cocky. And he's like, who are you? You work in a bar. And I was like, well, it's true. I do work in a bar. But that trace looks terrible. Making friends already, huh, Todd? Anyway, you know, so we got into it about oscilloscopes. And he was like, what, you know, do you have a scope? And I said, well, yeah, I have this tech 454 is the scope that I have. But it was just broke for a little while. And I just got it running again. And he said, wait, wait, you can fix an oscilloscope? And I said, well, yeah, you're an engineer, can't you? You're fixing an oscilloscope? And the interesting thing was I had no concept of what it was really that engineers did and what the difference. I just assumed that whatever it was that I was working on with a voltmeter and oscilloscope and Horowitz and Hill was somehow fundamentally different than what engineers did. And I was like, whatever they're doing, they're working on cell phones. You know, they know what S parameters are. I don't know. They know something that I don't know. And what you started to learn is that's true sometimes. They did. There were a lot of things they didn't know. But there were things that they were just doing the same stuff I was, right? They were like reading data sheets and scratching their heads. Anyway, this guy and I got to be good friends. And he was like, you know, if you are tired of working at a bar, perhaps you should interview with this toy company. And, you know, I was really curious. I was like, I could get paid to do electronics. And so I did. And they pretty much hired me on the spot. And, you know, thus began a bunch of 80-hour work weeks for many years of my life designing toys. And, you know, the first month was really awkward because I was like, I can't screw up my bar job. What if this engineering thing doesn't work out?

**Chris Gammell:** Engineering is not that stable, guys. Come on.

**Todd Bailey:** It was true. I was like a Russian kid with a turnip. I was like, I can't, you know, what if. I don't think they're going to figure out at some point that I actually, like, you know, that I don't know something. And this isn't going to last. And I'm still doing it today. And I don't work at a bar anymore. So, so far, young Todd Bailey was wrong.

**Chris Gammell:** So, so just like imposter syndrome, that kind of whole thing. I mean, pretty, pretty common in a lot of engineering, right? Is it? Oh, yeah.

**Dave Jones:** We were talking about it last week. Fake it till you make it, right? Well, yeah. Is that the motto?

**Todd Bailey:** Fake it till you make it? Yeah. Yeah. I was hoping engineering was a place where that didn't happen.

**Chris Gammell:** No, wait. No, it's all just, I mean, like, okay. So some people know exactly what they're doing. But I mean, like, I think, I think a lot of times, you know, it's like, oh, I can figure this out, right? I mean, that's, that's kind of the whole engineering mindset to me is that.

**Todd Bailey:** Yeah. That's different.

**Dave Jones:** You have the tools to figure it out. I mean, we're always on this show saying that you do your four years of engineering degree and you come out knowing nothing. But you know, but in theory, you should have enough tools to go out and learn, you know, that's the.

**Todd Bailey:** What you should have at that point is your pride, right? Like, you should have the idea that, you know, you can do a thing. You know, and that'll bite you tons of times, but it'll help you too.

**Chris Gammell:** Right. During the learning process, of course, right? That's what it really is, is the learning process. I'm, I'm, I'm interested by this tie into the toy industry too, because obviously, Jerry, who I think you know as well, I'm always interested. I thought there was someone else too, but I mentioned it the other week, you know, like this tie in with the toy industry, you know, it's, it's, it's very interesting to me. And it's such a crazy business. Obviously, I've heard you talk about it a lot. I've heard Jerry talking about it a lot, but it seems like it's just the gauntlet for learning and, you know, quick terms. Return, elegant solution type of stuff. Oh, it was Alicia. She was talking about it. That's who it was. That's who it was on the show.

**Todd Bailey:** Um, there are a lot of great things about toy design. Uh, there are some less great things about toy design too. Um, one thing about it that's really, really good are number of iterations, right? Um, you build like the company that I worked for is called, uh, big monster toys. They're still around. They still rule. I still do jobs for them. Um, and the, the longer I am away from that job, the more I realized that they are, they were a great shop and a first experience in proper engineering that I, I couldn't, I couldn't have gotten luckier. Um, but that, uh, that was in Chicago and that place probably made, I want to say like 200 toy prototypes a year. Holy crap. Wow. Yep. Yeah. And you know, not all of those were electronics. Uh, you know, there were, there were a lot of plush toys and stuff that came out of there that I'd never had hands on, but I had, I touched a lot of those things. Um, and of those 200, I think the, the business model for a place like that, uh, BMT was an invention house. And so the idea is you're, you're, you're bros with Hasbro and Mattel and a handful of smaller toy companies. And they come in and you pitch them ideas. Like, you know what they're into historically and you know what their lines are. And so Mattel comes in and you try them, try and sell them the next Barbie. Right. Uh, and they'll either bite on it or they won't. And if they do, they take it away. Most of the time they send it back, but sometimes they take it away and they keep it.

**Dave Jones:** As in the, as in the physical prototype you're talking about.

**Todd Bailey:** Well, there's lots of ways to sell a toy. And I think, I think my old bosses would have been like, well, the best way, right. Is to, is to make a crayon drawing and have a great concept and sell this thing, which is, uh, in ether and still get paid for it.

**Dave Jones:** Because it doesn't take much effort to do a crayon drawing. Right.

**Todd Bailey:** Yeah, exactly. In real life that, that rarely happens. So, uh, one of the great things about BMT is they weren't afraid to really make a prototype. Uh, so, you know, I, your, your sales go up a whole lot when you show someone the thing that they're buying. Um, and in fact, you know, the great thing about that shop was it was, you know, there were machinists there, there were model makers, there were sculptors who were really, really good. We could build pretty much anything. And it is, it was mostly old handy guys. There wasn't a whole lot of computer aided machining. There was a little bit, but not much. Uh, and then there were a couple of nerds whose job it was to, to code whatever it was and build whatever circuits that were going to go into this thing. Um, and we could, I mean, regularly, you know, if we couldn't make a thing that was better than production, we were not doing our job. Right. So, uh, so the good thing about it was that you did this all the time. Um, you know, and of those 200, you maybe sold 10 in a year and of those 10, maybe, you know, you maybe like two or three or four made money, but they made a lot of money. So, so, uh, so it was this model where you really had to crank through stuff. And, uh, and that was good because, you know, I remember the first circuit that I worked on there, it was for a toy that never got sold. And I think they probably gave it to me because it was, you know, they knew I didn't know what I was doing yet. It was doomed. And it was, yeah. Uh, it was, it was called, it was called beast in a bag. And, uh, uh, and beast in a bag, I built this, I still was real soft on programming. So, you know, beast in a bag, the idea was they were like, it's got this really loud motor in it and it has to listen to, you know, the player talking to it. And when the player makes sounds, it has to respond. But I was like, you know, it's got this microphone right next to this motor. Whenever the motor kicks on, you pick up a bunch of mic, uh, you pick a bunch of noise on your, uh, on your microphone and, and, you know, the toy, so I can't handle that very well. So, you know, I went to all this trouble to try and like sample audio in different points and figure out what, you know, the best way to solve this problem and did a terrible job and it didn't really work. And, uh, and after a while there was this one, there was a contractor there who's now, uh, a great friend of mine who, uh, taught me a ton of stuff. His name is also Todd. Um, and I, you know, they were like, you know, you Todd Bailey, if you ever have trouble, you can call big brain Todd, uh, and ask him for advice. And I was like, I'll be damned if I call big brain Todd and ask him for advice. Uh, I'm gonna figure this out. And eventually after beating my head against this, I did. And he was like, you know, and this guy is, is a, you know, has forgotten more about programming than I will ever know. Uh, and it was like, oh yeah, yeah, that problem is really, really hard to solve and they're never going to solve it in production. And so what I do is just run the motor and don't listen while you run the motor. I was like, that's what you do. You just cheese out like that. He was like, yeah, it's the best solution. It only takes half a second and it, you know, and the thing works right. Uh, so you learn those lessons like, like that, that like, you know, I still would probably be working on that circuit. The good news is you, you, you have to throw that away, right? Like I threw away that turd and moved on to the next circuit with a lesson learned. Uh, and it's, that is one of the things that's really beneficial. Like being able to touch many different kinds of things, uh, and being able to go through, uh, lots of iterations. Those are beneficial things, you know, and, and always making a thing that the goal is to have it physically produced. Uh, you know, there's, there's an idea that you can't, you really don't prototype very much if you know that it's unbuildable. Um, occasionally we would, we made a rock'em sock'em robots that shocked people. Uh, and we did that, and we did that, uh, and we did it for fun. Uh, we were like, yeah, that's never getting sold.

**Dave Jones:** Kids love it when they're, when they're conscious.

**Todd Bailey:** They do love it.

**Dave Jones:** What would happen if you had a really, you thought it was a spectacular idea, but you had no idea how to produce it or if it was producible, would you still pitch it because it was just such an awesome idea?

**Todd Bailey:** Hmm. Maybe. It usually wouldn't get that far because the people at the toy shop knew what was producible and what wasn't. So someone would come up with an idea and, you know, if it took a lot of work to bring into the prototyping world, it usually wouldn't make it that far. Got it. Uh, occasionally there were toys. I mean, it's like, it's like the end of Raiders of the Lost Ark where, you know, Indiana Jones brings the Ark back and they're like, you got this Ark, what are you going to do with it? And they put it in the warehouse with all the other Arks of the Covenant. Uh, the back room at that place is like that. Like you walk back there and there are, you know, it's the, it's the land of forgotten amazing toys. Uh, because it's not always the, it's not always the good ones that sell. Uh, of course. Yeah.

**Dave Jones:** Yeah. Yeah. So you get pretty done. It's the farty gnome that sells, right?

**Todd Bailey:** You know, it's the, anymore, it's the branded that sells. So the, uh, the, like the new creative toy, which is out on its own is, is often less likely to sell than the Dora the Explorer branded birthday cake or what have you. Yep.

**Todd Bailey:** Uh, which is one of the reasons. Yeah.

**Todd Bailey:** Yeah. Well, there's, there's more signs of the times in the toy industry, but, uh, I haven't jibbered about that too long. Anyway, toys are great. There, there are things about them. You know, you're never going to get to make a wildly precise circuit in toys and you're not gonna, you know, use a processor that does a whole lot in toys. Uh, you know, and that's one of the reasons why ultimately when I left, I was like, I would like to spread my wings. And, you know, there are, there are great, great engineering challenges in the toy world and I still find lots of them very hard. Uh, but you know, there were things that I realized I was never, ever going to get to work on, uh, if I stayed there and I was curious to see what they were like.

**Chris Gammell:** Huh. So, uh, what, what was next?

**Todd Bailey:** Um, well, shortly after that, uh, so I, I worked there for, I think three, four years, um, and was, uh, the, the chief engineer there when I left. Um, and I, I became a contractor and at the time, um, you know, I didn't know what that would mean. I, my, I had this plan, right. And the plan was, uh, I, you know, I was like, man, one day, you know, this is rocker dude, Todd talking, uh, one day, wouldn't it, wouldn't it be great to make a living? Uh, somehow with electronics, uh, to pay the bills, uh, touching a soldering iron or something. Um, and that job provided that. Uh, and it was really cool. And I was like, oh man, all right, well, what's next? What's next is maybe wouldn't it be, would it be possible for me to not only, you know, keep my fridge full of, uh, domestic beer and organic peanut butter. Uh, would it, would it also be possible for me to be my own boss and do that? Uh, and so the next step was to try and do that. Uh, and so I, I left and I had a handful of clients. Um, some of them were, most of them were at that point were toy clients and a couple of artist clients that I built stuff for. Um, and my overhead was really low at that point. So I could have a not so great year. Um, and, uh, and still it was fine. Um, and so, you know, for the first year or two, first year, I guess I lived in Chicago, uh, and I built, you know, people's art projects. I, uh, would try and design little circuits and sell them, um, you know, to, to bridge the gaps. Uh, and, um, you know, as, as time went by, I got, uh, I got more and more clients at work started getting better and better and I moved to New York and as time went by, you know, pretty much exclusively through, through word of mouth and, uh, a little bit through schmoozing, uh, you, you meet, you meet, one thing about being a freelance embedded system engineer is there aren't very many of us. Um, and that's a good thing as far as finding work goes. And a thing that's not so good is there are really not that many people who need what you do. Right. Uh, I think it's increasing though, honestly.

**Chris Gammell:** I mean, these days at least, I don't know if you've seen that.

**Todd Bailey:** I could, I could, I could talk about that at length, but, um, anyway, so, so the path was, it was, you know, it was a parent with electronics, parent being your own boss with electronics. And then I was like, Oh, I think the next thing is to try and design and sell my own products, which I, I had a brief stint with and sometimes still flirt with. Uh, but I realized that I'm not that great at that. Like I'm not a wonderful sales person. Uh, I like building stuff. Um, and I get real fired up about that. And then once it gets to like move in units, uh, I find that I'm a whole lot less effective. So, so once that sort of went away, I was like, well, you know, for now, until I find a different goal, I just, you know, this is going to sound real afterschool special, but, uh, I want to be the most badass engineer that I can be. You can do it. Is that the response? You're on. Uh, that's, I was hoping you could do better, but I'll take it.

**Chris Gammell:** I was going to say like the theme music would kick up at that point and like montage kicks in the room.

**Todd Bailey:** You're like, believe it or not, I'm walking on air. So, uh, what did, what did that involve?

**Chris Gammell:** I mean, uh, was that like, just like self-education, that kind of stuff and like learning more by taking harder jobs, that kind of idea?

**Todd Bailey:** Yeah. Well, so what you were saying before about, uh, fake it until you make it, um, the, what I, what I hope you were saying was, uh, you can take a, you know, someone will ask you if you can do a thing, right? Someone will say, I need you to build, um, um, you know, something which moves and lights up and also talks to God. You can be, you'll be like, okay, okay, okay. Yes. And you're like, yes. You're like, you're like, okay, well, I can definitely make something that moves and lights up. And I've, you know, I've never made something talk to God before, but I can, I can take a shot at it. And, and if, if your client is like, well, we can't find anyone else who's going to do a better job than making it talk to God, uh, why don't you take a shot at it? Then, you know, then that's the best possible situation you could be in because everyone's on the same page. You're not promising something you can't deliver.

**Dave Jones:** And they still expect it though.

**Todd Bailey:** They expect it. If you tell them you can do it, if you're, if you're, if you're square with the client, like my policy has always been to tell a client it's going to cost more than it does. And then deliver under and tell them it's going to be rough if you think it's going to be rough. And if they still, you know, it's like if, if you set them free and they come back and they're, they're a good client.

**Todd Bailey:** And they love you.

**Todd Bailey:** And chances are, chances are it means that they, and then if you do it, you know, they're super excited. And these are a huge danger.

**Chris Gammell:** Well, these are usually customers that you've, you've worked with before too, right? You wouldn't do this for an initial one, right?

**Todd Bailey:** Oh, I definitely would. Oh, you would. Oh, okay. Oh yeah. It's, it's, it's important. Uh, you know, the more clients, the busier you get, um, the more leeway you get to screen your clients. Um, so, uh, so, you know, at some point you, your spider sense tick kicks in a little when, when clients call you and they want an unrealistic thing. Um, and you know, you, you maybe explain to them in the gentlest possible way that what they're trying for is very, very difficult. You're a frigging idiot. Well, sometimes they are. Sometimes there's just dumb. And sometimes, sometimes it's just that they are inexperienced. Right. Right. Uh, and the, and the way, the way that you go back and forth in that sort of conversation determines a whole lot how, like, like you're like, I think I, I maybe can appreciate how this relationship is going to go. So, so, so giving a client, uh, you know, a healthy dose of honesty, um, is never really a bad thing. Cause the worst thing that happens is you lose a job you didn't really want anyway.

**Dave Jones:** Here, let me punch you in the face with my honesty fist. Yeah. Let's back. Oh, goodness.

**Chris Gammell:** So, uh, did that device talk to God or what happened?

**Todd Bailey:** Uh, you know, it never did. No. Okay.

**Chris Gammell:** I suppose you wouldn't be on the show if it did, right? You'd probably be elsewhere.

**Todd Bailey:** Uh, no. I mean, I still, I still just get a check at the end of it and, you know, they go on and patent talking to God. Yeah. Right, right. Right. Right. Okay.

**Chris Gammell:** So, so some of these devices, so, uh, you, you said you, you actually cranked out some of your own devices as well that you didn't like it. What were, what were some of those?

**Todd Bailey:** Um, I think the first thing that, uh, well, I mean the first, very first thing that I tried to sell was, uh, it was a synthesizer kit. It was a single tiny printed circuit board that I sold on tour with my rock band. Uh, and let me tell you, I cannot think of a, of a worse business model than that really. Uh, where you're like, oh, I'm going to go. Like I'm drunk. You're drunk. Here's a bag of parts. Uh, I think maybe one or two of those ever got made. I think I maybe sold 20. I think, you know, I marked up, I maybe, I maybe, I maybe marked them up by like $2. I was like, I'm going to make $2 on each one of these kids. Uh, it was terrible. Uh, so you say you're not doing business. Is that what you said before? Well, that was, that was, again, that was like, I was thinking of it as tour merchandise at that point. Right. Right. Not as, you know, I was, I was like, we could sell this seven inch record or we could sell this synthesizer and I, you know, and I can make two whole dollars on this instead of $1 on a seven inch record. Uh, so in my mind I was, I was bank rolling. Right. Uh, and, uh, so I think that's the first thing I sold. I designed this binary watch that I sold a handful of a long, long time ago. Uh, and then the first thing that I sold any, any number of, and you know, by number, I don't mean a lot. Um, I mean, you know, hundreds of, uh, was this, uh, open source digital sampler, uh, kit called where's the party at?

**Chris Gammell:** That's what I was thinking of. Yeah.

**Todd Bailey:** Yeah. There were a lot of abortive attempts before where's the party at. Um, well, where's the party at was this, uh, was this idea. I got asked to talk, uh, at this thing, um, called the bent festival, which is a circuit bending festival. Um, you guys know about that world?

**Chris Gammell:** Uh, I know the world, but I don't know the festival. It's like where people take, uh, toys or synths or something like that. They, they tweak parameters, usually like resistors. They put in pots and then they make the things go.

**Todd Bailey:** We, we, we, we, right. That's right. That's relatively accurate. Yeah.

**Chris Gammell:** Uh, um, then people dance to it for some reason. I don't know why.

**Todd Bailey:** People dance to, people dance to a lot of things. They do. Uh, but, uh, you know, I, I had a real soft spot for this community. Um, just because it was, again, it was a bunch of people who didn't, you know, were under absolutely no obligation to be doing electronics and made, you know, spent the small amount of money they had on these hopeless projects. Uh, and, and, you know, strangely that resonated with me. Uh, and I was like, you know, you guys are fearless and you like electronics and those things put you ahead of a lot of engineers already. Uh, I agree. And, and, you know, if only you, you could learn a little bit about how circuits worked, you, you might be dangerous. So, uh, at the time, um, and maybe still in that community, uh, people really, really love the Casio SK one. Uh, and the Casio SK one is this toy sampling keyboard. Um, which, uh, you know, which is like you, you sample your dog barking into it and then you can pitch your dog barks up and down and play happy birthday with dog barks or broken glass or whatever. Uh, and, um, and people love this thing and, and, you know, they would circuit bend it to make all kinds of, of strings of random noise and people were way into it. Um, and these things on modified would go for hundreds of dollars on eBay. Uh, and I was like, you know, guys, it's, if you, you can do that or, you know, it's not that hard to just make a thing that does that. And then you can program it to do whatever sort of string of glitchy garbage you want it to do. Uh, and you can still, you know, you know, wipe your tongue on it or whatever, if that's your thing, uh, you can, you can even optimize it for tongue wiping. Like I can bet you, I can make a circuit which responds better to tongue than the Casio SK one. And Lauren born of this was where's the party at, um, uh, where I designed a digital sampler. Um, and I gave a lecture about how digital samplers worked. And the idea originally was to try and get people excited about learning electronics and, and I made maybe five kits. And what I found is people were sort of excited about learning electronics, but they really wanted to buy this thing. Right. They were like, Oh, that's, that's, you know, they thought of it more of as a product. And I was like, well, all right, that's not what I was going for, but I'll, you know, Hey, why not? So, uh, so I sold a couple hundred of those, um, sloppily. And, uh, you know, this got out there in the world. Um, and I designed a second rev of where's the party at, which is still in boxes, still on my shelf. Uh, and, and, you know, there's 300 of them. I can, I can look at them right now. Uh, and I've just like, have not been as motivated probably as I should to sell them because partially because I did it already. And partially because it's like, once you start to, I mean, this is, this is, I mean, what I'm about to say, I suppose is the beginning of the end for engineers, but partially because, you know, I've worked on harder things and I've, I've made more money. Uh, and so, so there's no, there's no financial motivation for selling where's the party at anymore. And the, the technical side of it isn't nearly as challenging as it was when I first did it.

**Chris Gammell:** Right. So it's the refining now, right? It's the, it's the, it's the product stuff that's less important than, or less interesting than the R and D stuff.

**Todd Bailey:** Well, it's, it's the product stuff. And you could, you could say it's about cost reduction too. And you can honestly say it's about getting a thing out there, uh, which is still cool and it's still pedagogical and I still believe in, but it's not, it's not the, it didn't not have the appeal that it once did. Right.

**Chris Gammell:** Different skillset.

**Todd Bailey:** Yeah.

**Dave Jones:** Yeah. I've done that. I've actually discontinued, uh, kits slash projects that I've been selling, even though they're still selling and they're popular, people are giving me money, but I'm just not interested in it anymore. So, you know, yeah, just couldn't be bothered. Not sorry. I'm not going to make any more.

**Todd Bailey:** Yeah. Uh, well, hopefully where's the party at? I have a personal goal for that to come out this year sometime.

**Chris Gammell:** Uh, you heard it here first folks.

**Todd Bailey:** You can actually people have been hearing it on the forum for about three years now, but, uh, moving target. But, uh, but I really would like to get that out of my life. Anyway, that was my first sort of product experience.

**Chris Gammell:** What you should do is what Dave did. He said he was going to do the, uh, the microcurrent gold for about two years and then he finally just did a Kickstarter and that.

**Dave Jones:** That prompted me to, yeah, to actually.

**Chris Gammell:** Put his ass into gear, right? Gear and do it.

**Todd Bailey:** That's right. A proper deadline is a great motivation. Yeah.

**Chris Gammell:** Of course, of course, if you do a Kickstarter, you might have to make a bunch more than 300. So that's a whole other set of, set of issues. Still shipping the bastards. Yeah.

**Todd Bailey:** I mean, the other thing is like, how snotty do I sound right now? Like, that's the other thing that's like, that's like, it's hard to sit with, right? Where you're like, you know, how many years ago was it where I was like, I just want to make things in my house with my car and I'm like, I can't be asked for like, you know, in number of thousands of dollars. Boring. Like, so it feels, it feels, it feels jerky to even sort of have this conversation, but you know, it's the truth.

**Chris Gammell:** I think your solution is to sell it to someone else and have them do it. Honestly, that's, that's. You know, the part.

**Todd Bailey:** Yeah, maybe. I don't know what the solution is there. I think the solution is to get it out of my life and then move on. All I want to do is kill it.

**Chris Gammell:** So I can make new things. Okay. So what, what about after that then? I mean, so that was another phase. What did, oh, are you still, are you still not allowed to talk about this big door thing? I mean, I know I said big door thing, but.

**Todd Bailey:** I can't talk about it a ton. I mean, so one of the problems about doing freelance stuff is you can talk about the fun jobs you do, but the jobs that are the challenging ones usually are NDA'd. Yeah. So I can say, I can say I made a bunch of robot doors for a fancy house in the Hamptons, but I can't really talk about it a whole lot more than that. Yeah. But it's a hard job. It took a bunch of years. You know, there's a bunch of single board computers. They have to live in a marine environment. You know, they have. For a door that opens? Uh-huh. And it also closes. All right. Features. Okay. Well, that complicates it. Yeah. But, yeah. No, there's 63 of these things. They weigh about a ton each. You know, the glass in one of these costs 20 grand. And they, you know, I ended up designing this power line communication system, which goes all around this house and allows these doors to talk to each other. I ended up designing a protocol for communicating over this power line, building all the circuits for it, building all the boards that went in each of these doors, building the hardware, which coordinates all these door systems. There's pneumatics in this. It was really hard and very stressful, and it took a lot of hours, but it's more representative of the sort of job that I would do now.

**Chris Gammell:** Yeah. Right. I'm amazed that, so, like, that's a job where I think about, you know, that's, you know, being hired by a, you know, small company or a group of people or, you know, whatever for that kind of stuff. And it's just like, I never would have thought of that. You know, I always think engineering, you know, bigger projects. Obviously, I've always been part of, like, bigger companies and stuff like that until recently. And just thinking about, like, but yeah, people do hire for that kind of stuff, you know? Like, and that's where a lot of the interesting problems lie, you know, the more I hear about it.

**Todd Bailey:** Well, it's, you know, recently, you know, the more sort of legit you get, the more engineering gets broken up. Like, when you're, when I was young, I was like, engineering is this one unified thing. And as you get older, as you get more into it, you split it sort of finer and finer. So, so what I'm doing, I would call applications engineering, right? Which is where I'm not designing an IC, right? I think that's where a lot of really hard, really awesome work is. I don't have the skill set to do that. And I don't, I, I, nobody, as far as I know, is hiring freelance ASIC designers, right? Uh, so.

**Chris Gammell:** Maybe.

**Todd Bailey:** Or maybe they are.

**Chris Gammell:** Depends on what kind of ASICs, I think, but.

**Todd Bailey:** Yeah. Uh, nobody has asked me to, to tape out an LM324. Uh, so, so, uh, so, you know, in, in, uh, so there is a lot of interesting work that goes on. And again, much like the toy world, you, you get these, these things come across your desk and you get asked to do jobs, which are varying lengths, right? You know, anywhere from a couple of days, I just finished a job this weekend, which was a couple of days long, which was a blast. Um, you know, to a couple of years, like the store job. Uh, and they're, they're very different and they're all sort of applications-y based. So they have the good things about the toy job and that you're working on different stuff all the time. Uh, but the, the net is a lot wider and you find yourself being different things to different people. Right, right, right, right. To some, to some, to some people I'm a programmer and to some people I'm a hardware guy. Um, and, uh, it's cool. It's cool to be able to do all those things.

**Chris Gammell:** Yeah. See, I always call that system design. I don't think, I mean, I guess it's application like, uh, cause you're, you're saying like you target different applications. It's system engineering. Yep. Yeah. Cause we're still piecing together single boards, like you said, and then designing our customs as custom hardware as we need it. But, um, yeah, I mean, there's a lot of interesting pieces in there for sure. Uh, last time you and I talked, you said, I, I, I mentioned to you last time we were having beers and I said, I, uh, I was interested in your work with artists as well. And I think you cautioned me against that. Why was that?

**Todd Bailey:** Oh no.

**Chris Gammell:** I mean, I'm not saying you said every artist is an a-hole or something like that. I'm just saying that you, I mean, that's just good advice you gave me. Cause I, I just want to, you know, have you share your experience about that.

**Dave Jones:** Well, cause our, our, uh, mate, Mike Harrison, of course, he's, um, he works with, you know, that's, that's, he's, he's a freelance, uh, designer and that's what he mostly does. I think is don't work with artists, those big art installations, you know, big letter rays and all sorts of arty installations.

**Todd Bailey:** Right.

**Chris Gammell:** Um, well, there's sort of the, maybe I should take a step back and say, not, not that you caution me against it, but just what is your experience with working with art type installations and stuff like that? Is it a different set of challenges or is it, uh, is it, is it similar to other type of, uh, consulting jobs you've had?

**Todd Bailey:** Yeah. I mean, ultimately it is. Uh, you know, the one cool thing about art jobs is you, you have the most arbitrary requirements for them, right? Like, uh, the, the set of requirements you get don't necessarily make functional sense. Uh, but they're just as valid, you know, like somebody is like, I need this thing, which normally, you know, uh, like I can't stand having a ugly heat sink or, you know, I like this thing, which would normally run on a motor, you know, I don't like the way the motor sounds. So can you use a fundamentally different kind of motor, right? Or, or something, you know, problems like that are real problems, right? If, if they become that in, in an art context. Uh, and so those, again, it's cool because it puts constraints on you. And it also, you know, some of the best clients I've had in toy or art clients, they like, you know, they'll try and, and, um, get an idea across to you, right? I want it to be like blah. Uh, and you have a certain amount of leeway in, in solving a problem like blah, uh, where blah in this case is like an idea or a feeling or something, which is an engineering problem that you don't, you know, come across in, in, you know, capital P proper engineering a lot. Uh, so that's fun.

**Chris Gammell:** Um, is that, is capital P proper? Like where you're wearing like a monocle and like drinking tea while getting project requirements?

**Todd Bailey:** I thought that was the one where I had a, when I had a cape on when I was standing in a corner with my fists on my hips. Uh, um, no, uh, so, so that's a good thing about art engineering. One, you know, like the flight of fancy involved in art engineering is great. Um, and it's, it's one of the things that makes it fun. One of the problems with art engineering and probably the biggest problem I have with it is, you know, take at, at one end of the spectrum, you're totally can't be asked about it. Engineer who's been at some job, it doesn't, you know, it's just like, you know, working for the weekend and has this thing that they need built and they talk to you and they want it done. Um, the amount of, of personal investment they have in that project is small. Uh, with artists, most of the time it's one person or a small number of people and they are deeply invested in the thing that they want you to build. Um, that can be good, but, uh, they usually are also broke. Uh, and so they, and there are times like this is, there are huge exceptions to all of these rules, but generally speaking, it's, it's really hard to be a hard ass, right? Uh, like, you know, you're doing like, I do this stuff, you know, for a living and I do it for fun, but the two are not, it's, it's a good idea. It's been my experience that it's a bad idea to mix those two things, right? Like you do projects for yourself and your friends for fun. Uh, and you do projects for clients for money. Uh, and, um, you engineering or you, uh, you know, I like to, I like to see myself more as like Ryu from street fighter, but, uh, but, uh, but the point is, you know, you get in the situation where somebody is, is deeply cares about their project and they really want you to do it. Uh, and they really believe in you and it's really, it's this sort of warm, fuzzy feeling and you have to be like, I'm sorry. Like, uh, you, you have to either put yourself in a situation where you do a bunch of work for free, uh, potentially, or, uh, you know, the other thing that gets tied up is, is one, one liberating thing about doing art, right? I remember back in the day learning that artists didn't always make their own art. Like, uh, do you know who Namjoon Pike is? Namjoon Pike, uh, is an artist that made, uh, a bunch of media art, uh, back in the sixties and seventies and he built a TV synthesizer. And I always thought this thing was the shit. Um, and at one point this Russian guy who hired me for this toy job, you know, turns to me while we're slaving over some toy and is like, you know, he didn't make that right. You know, his tech made that right. Oh, really? And I was like, no fucking way. No way. You don't know. And he's the artist. He made the art. That's what artists do. They make the, they make the art. And Demo is like, ha ha ha ha ha. How much do you have to know? And then that was my job. Like for a bunch of years, that was my job to make other people's art and sign their name to it. Uh, and what you realize is that tech probably didn't care. Uh, and I didn't ultimately after a while care either. Right. Like you realize that the, the games are different, right? Like an artist is good at things that I'm not necessarily good at and they're interested in things that I'm not necessarily interested in. Like I, like in some ways it's the best of, I get the great part of the job, which is somebody comes up with an arbitrary goal. You solve it. Uh, you get paid, you go to a fun party and then it's, and then, and then, and then, and then, you know, and like maybe you get your hands shook in and maybe you don't and you know, and you, and you move on with your life. Right. And this poor artist has to validate this thing in, in the big gray goofy world of, of history, which they are probably better equipped to do than you are. There certainly are like, like typically when someone will ask me about a piece of art, I will, you know, I will be like, I think it's cool. Or I don't think it's cool. Or it works, it works very well or it's built very poorly. Right.

**Chris Gammell:** That over there is, is gray and that one's green.

**Todd Bailey:** You know, so like, so the extent of, of, um, hyperbole, I guess that I'm willing to do about art criticism is, is, you know, it's just different than it would be. So I, I like my part of the job and I, I realized that I kind of don't care about, uh, the assignation that would, that would come along with that sort of thing. So that's a good, I suppose that's, if you're, if you're, if you have your head on that way, um, building art stuff can be, you know, can be a good time.

**Chris Gammell:** Yeah. Focus on the design and the interesting, fun, buildy stuff. Right. Yeah. So, uh, some of this, uh, this build stuff for your friends. Uh, I think we talked about it on the show whenever it came out, but this, uh, this crazy ass, uh, game sent the monitor driving. I, I don't even know what it is. I remember there's FPGAs and there's like spaceships. So what is this thing?

**Todd Bailey:** Vec, Vec9. Uh, so Vec9 is this, uh, one of my buddies, um, the guy who got me the job that I'm working in, the contract that I'm working at right now, um, uh, who's now one of my coworkers is a friend of mine. Um, and he dragged home an Asteroids G05 monitor. You guys know what an Asteroids cabinet looks like?

**Chris Gammell:** Yes. Uh, I think so. You're too young, Chris. I think I am too young. Is it the one where it's actually like the, you sit both sides of the table? Is that the idea or is that the, is that a different one?

**Todd Bailey:** Um, they do make a, I think they do make an Asteroids cabinet like that, but the, the salient point about the Asteroids cabinet is it was built at a time, um, before monitor technology for arcade games was codified. So, you know, in the, in the real early eighties, um, arcade games made a lot of money and you had a bunch of people trying to solve arcade game problems in lots of different ways. And you see this, um, you see this proliferation of different kinds of hardware out there, uh, where, um, you know, you'll get odd controllers, like, you know, you'll get the Akari warriors controller that turns, or you'll get, uh, you know, all manner of spinning discs and strange black lights and cabinets and, uh, you know, and atypical controllers. And in this case you, with Asteroids and a few other games, they're out there. You got an atypical monitor, um, star Wars, the star Wars game was like this too. Uh, where you have a monitor, which draws with vectors rather than rasters, like a, like a typical CRT might. Um, so the fundamental thing about this Asteroids cabinet is it has a different CRT, uh, and it draws like an oscilloscope, um, or a radar, uh, and not so much like, uh, a television. And consequently it looks crazy. Uh, you know, there are, there are tracers and trailers and these, these dots that'll burn your eyeballs. And, uh, and it looks, it looks, it looks amazing. And the lines are, are, you know, it's this game with incredibly crusty graphics and incredibly straight lines. Uh, and it looks, it looks, it, it looks really weird and it looks really cool. Um, and anyway, one of my buddies brought home, you know, just, you know, dragged home one of these monitors and was like, I bet we can do something with this. Uh, and we got all geeked about it and we're like, let's try and make a video game with it. And, and, you know, rapidly, you know, blew up the amp board on this monitor a couple of times. Uh, the repair shop experience came in handy. Uh, and, um, ultimately, uh, you know, this game, it's sitting on my bench right next to me right now, but it has this ancient transformer from, uh, an original Asteroids game. It has this monitor, which has been repaired a bunch of times now. And the deal is you don't, um, in a normal arcade cabinet, you could send some combination of RG and B to, uh, the guns on the, on the display. Uh, with, with this device, you don't, uh, you send XY, uh, to it, but it's not like a scope where you just send it where it's high impedance and you send it, you know, whatever, you know, whatever signal you want and scale it such that it's useful. It's, it's relatively low impedance input and it's real fast. Um, and you need to be, if you want to draw these vectors, you have to generate, uh, you have to generate vectors, uh, which means that you have to, you have to take into account the inductance of these coil windings that are on, uh, these yokes that are on the side of this monitor. And you have to take into account the hardware design of the amplifier, uh, and you have to drive this relatively low impedance, you know, this power amp, which has not much in the way of preamp on it. Um, and you know, anything you do with that circuit has an artifact on it and the screen, which you can really see because of the way that this monitor is built. So our, our idea was, well, you know, the guys at Atari, um, actually one of the times I went out to analog aficionados, I met one of the guys who worked on the Atari team, uh, that worked on vector games, uh, and went over to his house and brought him some cookies and we talked about vector games. Uh, and those guys, right. They were, they were, they were, uh, they were really, really smart and they were really, really motivated and, uh, they made some really great solutions. And we were like, you know, it's umpteen years later. Shouldn't we be able to do just a little bit better than that? Uh, given the state of the art today. And that was sort of the goal was to be like, how hard can we push this piece of hardware to display crazy 3d stuff? You know, which it never, you know, the original designers never would have envisioned it doing. Uh, and to that end, um, my buddy, uh, Andrew, um, uh, Andrew designed, uh, this FPGA, um, which is basically a graphics card. Uh, Andrew Ratano is his name. Some of the details are on his website. His, his, his net name is, uh, Batsley Adams, but he, uh, he designed this, this, what's essentially amounts to a graphics card, um, which you stream, uh, you know, a bunch of commands and vector data into, uh, and it, it hangs out clocking out, um, information to a DAC in this configurable way to be able to tune this thing to this monitor. And then I designed, uh, this high speed, uh, relatively high current DAC board, which hooks up to this FPGA, which drives, um, the amplifiers on board this monitor. And then, uh, from there, um, you know, then actually, uh, so at that point, you know, we could, we could crudely draw, you know, triangles and squares and stuff.

**Chris Gammell:** How much, how much current are we talking about here? I mean, like what's, what is the current load roughly? Of the monitor? Yeah. Like one of the, one of the signal lines that you're driving, you know, like, so like, what are these swings that you're, you're driving with this DAC board?

**Todd Bailey:** I mean, they're not nuts. They're, uh, they're probably plus and they're plus and minus 15 volts for the X and Y, I think, uh, maybe plus and minus 15 and plus minus 10, uh, at 20 megahertz. Um, and I think there may be one of the lines is I think one K and the other one is like 220 ohms or something like that. Uh, so, you know, they're not, I mean, it's not driving a speaker at 20 megahertz. Um, but it's, it's enough that like, if you get ring on that circuit, you will sure see it. Uh, so it has to be clean. It can't, it can't, uh, it can't suck. Um, but, uh, you know, it was fun to design that. Right. And you, and you have all these weird, strange requirements. Like it has to go really fast, but it's relatively, uh, you know, it's got these, these, uh, it runs at 60 volts. Right. So like, good luck finding op amps that work that way.

**Chris Gammell:** Uh, they're coming, man. They're coming. New high, high voltage processes.

**Todd Bailey:** Uh, yeah. Bulges keep getting higher as years go by. That's what I heard.

**Chris Gammell:** Uh, seriously. I think Maxim has a new process. Like for real. I think they're, they're moving up that direction.

**Todd Bailey:** So for like electric cars and stuff.

**Chris Gammell:** Yeah. Yeah. Like that. I mean, because they're moving in the market, I think of what they're doing, they're just making the trenches bigger, but you know what I mean? Like for these big fats, but, um, anyway, so blah, blah, blah.

**Todd Bailey:** So we built this thing and then actually the funny, the funny, the funny thing is like, you know, we finally get it to the square display like a square on the screen. And we're like, ah, damn, now we need to make a game out of it. So the whole thing, like this hardware gets to work pretty well. And, uh, we're like, you know, now we got to program this video game. So all of a sudden it turns into this 3d programming problem. Um, where, you know, if, if we were trying to write a video game for a PC or something, uh, there's a ton of libraries you can use. Uh, you know, I'd done, uh, just a hair of open GL stuff. Um, but because this thing thinks about the world in terms of vectors, uh, and because it's rendering to this bizarre piece of hardware, um, trying to shoehorn, uh, like a graphics library that you'd use for your actual monitor, trying to use your GPU for it is, is real kludgy. And so we were like, well, you know, we'll just solve it by writing a 3d engine. Um, which, uh, was not trivial. And, uh, it's like, you know, like you, you start to like, I had always been real soft on, you know, dot product and cross product and vector math and that sort of thing. And it was this, uh, it was this, um, because in real life it's, it's rare that I apply those. Uh, and, and, uh, and it, you find that it's this, we wrote a simulator for it so you can simulate the vector game on your PC so you don't actually have to boot up this hot, dangerous monitor all the time. And, uh, and, uh, 60 volts, man. It's 60 volts, but you know, it's got all these x-ray warnings on it. Like the phosphors kick off a ton of radiation, I guess.

**Chris Gammell:** Hey guys, I'm firing up the test system. Put on your lead underwear. Yeah, right.

**Todd Bailey:** So, and it's like, you know, there's like mad transformers all over your bench next to whatever you're working on for your job. Uh, so, uh, anyway, uh, the problem got a lot bigger, um, you know, and we got really ambitious about what we wanted it to do. And it got to the point where we have, you know, like 3d models flying around the screen for, you know, this is weird Vec9 engine for this thing. And, and, you know, when you blow up a, when you waste a bad guy, like he flies apart into vectors and they, you know, have particle effects and everything. And it looks bad-ass. But again, uh, you know, originally actually the game is about, uh, uh, cosmonauts, uh, awaking from being frozen in space and blowing up Chicago. So, uh, so, uh, so right now it's about rescues. Yeah, totally. It's about rescues. And, uh, and it's got a, it's got a, we put a secondary monitor in the thing and has this green screen CRT monochrome, uh, from like an ATM that like hangs out in it that like shows a picture of your co-pilot Leica. Uh, and, uh,

**Chris Gammell:** there's video of it and we'll put, we'll post that in the show notes as we have in the past. Uh, it's, it's fun to watch.

**Todd Bailey:** Anyway, I guess the whole point of this is also like, I guess this is like, what is this about? I don't really know. It's like, there's this one hand clapping thing. There's something that's like, like there's, there's these, where's the party at's that are this awesome project, but not quite done. And then there's this vector game, which is this awesome project, but also not quite done. Uh, so I don't know if you guys can solve that one. I, I, I'd listen to that amp power.

**Chris Gammell:** So, so the tagline is Todd Bailey. He'll finish projects if you pay them. Otherwise they're just cool.

**Todd Bailey:** I wish, I wish I could take issue with that statement.

**Chris Gammell:** I know. Well, it's right though. I mean, like, it's like when you're solving, you, you are in, it sounds to me like you're in it for the technical challenges is once you get past those, it's like, well, what's the point after that? And that makes a lot of sense. You're doing it for you. So that's, I don't know. So, so I should say, I was going to say at the beginning of the show, Todd has been one of the most, uh, enthusiastic person I've ever, ever met about hobby electronics. I mean, obviously I talked to Dave every week, right? So, so that's, that's, that's saying a lot. I mean, both of you two, I mean, both of you are like just so into it, right? I mean, and it seems like you're both always on too. So I, I think that's, that's worth stating as well.

**Todd Bailey:** Uh, well, thanks. You're welcome. Uh, keep it up. I don't, I don't, I don't think of it as a hobby for what it's worth.

**Chris Gammell:** Right. Well, but I mean, like, so I consider like this stuff though. Like, so like the, where's the party at? And I guess maybe you didn't consider that at the time, but I mean, there's this game. You're never, I mean, are you ever going to commercialize it? I think of that, like you, you're working on that kind of stuff on weekends and like doing FPGAs and vector math on weekends. I hate to tell you, man, if there's no, if there's no profit motive at the end, that's, that's a hobby, I think.

**Todd Bailey:** So the older I get, the more I consider what you're saying. Uh, and the more I'm like, is that really true? Right. Like the whole reason I have a job is because of this hobby. Right. Uh, I think it's more like when I think anymore, like as I get older, I'm like, am I going to be a, uh, like weird shut in, you know, who like hangs out with transistors for the rest of my life? Maybe. What does that mean? Like what are, like, like working at a, so I have this contract where I work on a fancy defense stuff now, um, which we've talked about off the air and can't talk about on it. Uh, uh, and you know, at that particular job, um, the people there are not weird. Like they're not strange zealots. Uh, they don't listen to this podcast. They, uh, you know, they're, I don't know. Uh, they're missing out a whole segment there. A whole market segment. Um, they're, they're like, they're people who do their job and they go home. Um, right. Yeah.

**Chris Gammell:** I've worked with people like that as well.

**Todd Bailey:** Yeah. Totally. And, and the whole reason why I have an English degree and can be in there, like getting hired to do this stuff is because of, of this, this bug, right? Like that a handful of people have. Uh, and you know, I have this, I have this idea that I'm like, you know what a hobby is? A hobby is like cooking. Like I like cooking. I'm not great at cooking. I'm never going to be a professional chef, but I can make a scrambled egg. Uh, and like, you know, I like, like, like, I like normal people come home and when they have a hobby, their hobby is not what they do for money. It's not like they just turn the meter off and keep making eggs. Right.

**Chris Gammell:** Like a line chef at Denny's. You mean like coming home and like being like, I'm going to make another grand slam.

**Todd Bailey:** I'm going to, I'm going to, I'm going to perfect my chopping my onion because you know, if he does that, he's probably not going to be a line cook at Denny's for that long. Right. So, so like, so, so like the, the word hobby to me now means this thing that like normal, like relatively mentally healthy people do that doesn't have anything to do with their job. Uh, and for me, I'm, I'm like, I don't know. There's, there's this differentiation that I have where like, like people who, people, like people in all stripes of life who work too much basically have this thing where they do it because they take either self validation from it or it's just what they like doing better than anything else. Uh, and at that point I'm like, there's, there are like some gray areas with hobby there that might be valid, but they might also not be. So, sorry. Yeah. Sorry. That was a digression.

**Chris Gammell:** No, that's okay. I mean, so Dave, I mean, Dave, you probably, you have, you weigh in on this too. I mean, you say that you always do the hobby stuff at home as well. Right. I think, I think we're all in the same boat here. I mean, well, probably you two more than I am, but. My video blog is my hobby.

**Dave Jones:** Yet it's also what pays the bills every day. You know? Right. To me, it's still a hobby. It's me just coming to the lab and bumming around. You know? It's still, there, there is a, for me now, there is no differentiation between work and hobby.

**Chris Gammell:** Right. Right. But I think Todd's point is that that would never be considered a hobby in the first place. Right. It's just, you've always been working towards doing whatever you want to do. And that's kind of, you know, working on stuff that you enjoy, working on what you want to do. And it's like, yeah, you know, like that's.

**Dave Jones:** No, I, I think it's got to be a hobby. If you're not working, you know, towards an end of making money doing that particular project, then it's a hobby. Sorry. Sorry. So if you're dicking around with your little arcade, you know, vector arcade game machine, that's a hobby. First, first of all, it's not little.

**Todd Bailey:** And second of all. It's going to be hot. Second of all, second of all, I would, I would take, you know, like to complicate this notion of the hobby, which is, you know, tell me to shut up. If this is, you know. No, I'm into this, man. Let's go deep. I'm like, you know, take, for instance, a band guy, right? Or better yet, take, for instance, a monk, right? They don't get paid for that. They do it because they like it. I mean, they do it because it's important to them in this way where it's not a job, but I wouldn't call it a hobby either. Right? And, like, to me, the thing that distinguishes a hobby is something that you do, which is secondary. Like, the hobby is this thing where you relax, you unwind at the end of the day with your hobby. A well-rounded person is like, I'm into golf. Or, you know, I like, you know. I don't know about that, but okay. Like, well, whatever, like, or fishing or knitting. Or knitting. Yeah, sure. Or, you know, and these are not people who professionally fish or knit.

**Dave Jones:** But if it turns into your full-time job, why does it suddenly stop becoming a hobby just because you do it on the outside? I'm telling you, most people in the electronics industry, if they work on electronics outside of work, they will call themselves hobbyists. They will say it's their hobby. Even though they do it for work. Sure. Just the sheer numbers, that's just the way it is. In fact, you're probably the first I've heard of, perhaps. I don't know. I can't recall of another one who's making the counter-argument. But I can see where you're coming from.

**Todd Bailey:** I'm also probably the first one that you've talked to that has a degree in postmodern literature, right? No, I think you'd be surprised. No, I'm just not. So, I just, I'm all for hobbies. I think they're a healthy thing. I just don't. I think that there are some shades of gray in there that make a weirdo who does the same shit all day long, whether they're getting paid or not, different than a hobbyist. Okay, but you haven't done it. I don't think you sold us.

**Chris Gammell:** So, payment is secondary to what you want to work on. That's kind of what you're saying, right? Well, what he's saying is that Todd Bailey does not need to be paid, folks. So, give him a call today at 212.

**Todd Bailey:** And I will do your things for free.

**Dave Jones:** At this point, we're going to have to pull out the dictionary. I can't find my Aussie Macquarie dictionary here, so I'm going to have to rely on Google.

**Todd Bailey:** I know you are not going to say the... I know you're not going to start an argument, a rhetorical argument with the Oxford English dictionary.

**Speaker ?:** We have to.

**Todd Bailey:** It's gone down to that point.

**Dave Jones:** It's reached that level of...

**Chris Gammell:** I don't know, man. So, I've had this argument before with my wife about... So, is TV a hobby, right? I'm going to be in trouble for asking this. She claims that watching TV is a hobby.

**Dave Jones:** Okay, the definition is an activity done regularly in one's leisure time for pleasure. In which case, yes, TV is a hobby. It's a hobby everyone has, but...

**Todd Bailey:** What about sneezing? I don't have to enjoy sneezing, and I do it in my leisure time. I also do it while I'm working. Right. I mean, we can do... We're all people with plenty of grey cells. I think we can do better than that definition.

**Dave Jones:** No, sorry. You're not sold on me. I've always have been a hobbyist, always will be.

**Chris Gammell:** Well, I think honestly it's a definition thing, right?

**Todd Bailey:** Tell you what. I will meet you here. I will say I think the reason that you're maybe defending this so zealously is because you perhaps believe that you do this because you like it. You're like, I...

**Dave Jones:** I know I do it because I like it.

**Todd Bailey:** Right. I also do it because I like it. So I think perhaps I'm offending you by calling it something other than a hobby. I think maybe that that's your way of saying I am called to do this thing whether I'm getting paid or not. Yeah. And, you know, I'm also saying that I'm just saying that it's a little abnormal also.

**Chris Gammell:** Well, I think you're right about that. And we've seen that, right? I mean, like you mentioned, like Dave has mentioned before, right? I mean, like you compare the people that go home after work, right, and continue to work on this stuff. I think that is abnormal. Whatever it's called, hobby or calling or whatever it wants to be, right, it's not the norm, I think. I mean, I think that...

**Dave Jones:** Then what's the other word that you'd use for it? If it's not a hobby, if you just enjoy doing something that may happen to be the same or similar to what you do for your work and your spare time.

**Todd Bailey:** So I'm just going to go take it way off the deep end because I think we're probably running out of time, so why not?

**Chris Gammell:** So we just cut it off at a certain point, right?

**Todd Bailey:** So you can be like... Click. Go home. And the answer is... Where, you know, the people who are the most inspiring to me are the people who love their jobs, right? To whom the differentiation between all this stuff is gray. Like, it's not just that you do it... I can't speak for you, Dave, but I would say for me, I would... I would say that I do it because I like it, but I also hang an enormous and inordinate amount of self-worth off of it, right? Like, were I to be... Were someone to prove to me that I was a bad engineer, it would shape the way I think about myself, right? Whereas if someone were like, Todd, you're a bad cook, I would be like, I am not. And they were like, yes, you are. I would be like, eh, okay.

**Chris Gammell:** Yeah, those aren't that good.

**Todd Bailey:** Like, I would say that there is... I would... I'm trying to avoid using the word... And this is not just for electronics. This is for people who just love the stuff that they do and do it because they can't find... Like, there's nothing they'd rather do.

**Chris Gammell:** Yeah.

**Todd Bailey:** I would call it a calling.

**Chris Gammell:** I knew he was going to say it, Dave. Oh, God.

**Dave Jones:** Wake word of the week, folks. Calling.

**Chris Gammell:** No, it's fine.

**Dave Jones:** Next thing you know, we'll be going on pilgrimages and we'll be...

**Todd Bailey:** You think I didn't fly out to see Jim Williams' work? I was going to say, yeah. I went on a pilgrimage. I'll say it loud.

**Chris Gammell:** Yeah. Well, that's what I was thinking. You know, when you were saying that whole... That personality type you were talking about, right? I mean, that's kind of the archetype that I think of, right? You know that if Jim Williams wasn't working at Linear Tech when he was writing those app notes, he would have been at home in his basement doing the exact same thing, right? I mean, that's the idea is that the dude was just happy working on electronics. And that's what you're saying you aspire to, right?

**Todd Bailey:** I don't know. Well, the whole reason maybe I'm complicating this is because I don't know if I aspire to that. I happen to identify with that a whole lot, but I gain a lot of personal self-satisfaction out of being that way. But I don't know if at this point in my life I can argue that it's the best way to be.

**Chris Gammell:** Oh, so you're like tormented about it? You're like, oh, man.

**Todd Bailey:** Generally, I'm not. I mean, most hours of the day I have my head in front of an oscilloscope and I'm not thinking about weight problems, right? I'm thinking about why a circuit doesn't work.

**Chris Gammell:** So eventually when you walk up to Todd at the analog aficionado's dinner in like 10 years, he's going to be like, hey, I'm Todd. I'm a frigging engineer and I hate it. I hate that I can't stop this shit. I'm Todd and I have a problem. Engineers Anonymous. Yeah, right.

**Todd Bailey:** It's just fun to think about. Like half of the – like engineering is about solving problems, right? And one of the exciting things that I have always found about engineering is frequently in engineering there's a right and a wrong, right? Like more so than in art, more so than in a lot of humanistic disciplines, more so than in social sciences or what have you. You know, there are right answers and there are wrong answers. And you can know the right answer because something works or it doesn't work. And there's – that's so liberating. I mean that's such a great feeling to be like I know I can be right about anything in the world is a luxury that I think a lot of people don't have. So that's one of the amazingly appealing things about this one particular discipline. I'm sure there are others out there that like it. But with respect to all this other stuff, I just think it's interesting to consider what makes your head drawn to that sort of thing. And I wish I could figure it out.

**Dave Jones:** For me, the difference between electronics as a hobby and electronics as a career almost comes down to the fact that as electronics as a career is more of a means to an end. Whereas electronics as a hobby is an end unto itself, if you know what I mean. Like I don't care if my – you know, if I ever finish that project. Just the fact – you know, as a hobby. I don't care if I ever finish that project or ever makes it or I ever sell it or whatever. The fact of just dicking around on it with it is an end unto itself. That's why it's a hobby. That's why it's enjoyable. Whereas work is always different to that. You always seem to have, you know, your goal, you've got to do it. You know, you're paid to meet that goal, that deadline and et cetera. There's an end point. There's a means to an end. So anyway.

**Chris Gammell:** So Todd, are you saying that eventually the – you think that the – having the sleepier hobby after work, like having the nine to five might be a better way to – that's what you're pondering is if that's a better way to live?

**Todd Bailey:** Not necessarily. I mean, I think I'm past that. I think it's too late. Yeah, of course. Yeah, yeah. You should.

**Dave Jones:** He's got the knack. I've got other hobbies outside of, you know, outside of doing this. You know, there's – it's not my only hobby, LHRs, but I treat them all the same because I just do them for pleasure. I just like dicking around on them. So it's a hobby. That sounds very well-rounded.

**Todd Bailey:** Congratulations. Thank you.

**Chris Gammell:** See, Todd has the problem. That's the problem. So Todd, we can come back next week. We'll continue on our sessions. We'll talk more about through this.

**Todd Bailey:** You know, we can – Do you have any exercises you'd like me to complete before I come back?

**Chris Gammell:** Repeat after me. I'm an engineer, and that's okay. Okay.

**Todd Bailey:** Chris, I don't know what it is that I'm talking with you that always gets me on the couch like this about engineering. I swear. I know.

**Chris Gammell:** Me and Todd, like, we're sitting at bars, like, hunched over, like, PBR cans because for some reason I drink PBRs when Todd's around. And we're like, yeah, we're, like, talking about this crazy stuff. And then I get an email two days later. He's like, oh, we were supposed to talk about electronics too. Okay. We'll do that next time. We'll do that next time.

**Todd Bailey:** I suppose if I have a hobby, it's being, you know, it's being emo about my place in the world of electronics, right? Introspective. That's my hobby is occasionally I dabble in introspection. That's right.

**Chris Gammell:** Naval gazer extraordinaire.

**Todd Bailey:** Hold on. I got a change into my bloody Valentine t-shirt.

**Chris Gammell:** Exactly. This is the emo rocker coming out after all these years, right? So much angst. So little time. Hey, hey, hey, hey. What was the other project? There was another project I was going to ask you about. Are there any other cool projects we should know about that you've worked on? I mean, there's been a lot of cool ones.

**Todd Bailey:** I've been geeked about work stuff lately. Again, I can't talk about it too much. I've been, so there's Vec9 right now. On the bench for things I have to finish right now, where I feel like I just, oh, I just made my bed fly. I have these. And that's like, and that's like not even on the books, right? Like you can't, no one, like very few people ever actually see that. But I just, I have this real, I basically, I live in a box sort of. Uh-huh. And I have a very like open floor plan, New York-y apartment. It's not very big. Um, and because of, you know, my advanced silver years, uh, I was like, I am not, I will not, I am done climbing a ladder before I go to bed. I am not. In a loft. Right. I am not sleeping in a loft. Uh, yeah. At the same time, I, I love the amount of extra floor space that a loft affords you. Right. Uh, so, uh, in this particular apartment, I solved that by making this big, uh, this motor system, which, um, uh, you know, makes my bed go up to the ceiling. Oh, sweet. Sweet.

**Todd Bailey:** Cool.

**Todd Bailey:** Uh, and it's cool. It's actually overrated enough that you can ride on it, although it's pretty tippy. Uh, so I mean, I built that, I built that a couple of weekends ago. And, uh, uh, oh, I think maybe, uh, maybe you want, you're asking about the video synthesizer that I was working on.

**Chris Gammell:** Is that it? Yeah, I think so. Yeah. That's, I think that's, that's the one that you took to Maker Faire or something like that.

**Todd Bailey:** Yeah, that was, I got really into analog, uh, TV signals, um, which are great. I mean, if you're, if you're making something that's, that's both analog and artsy fartsy, there are a lot of great challenges to solve, um, in analog TV, right? Uh, like hue and coding is, is a great problem to solve, right? Uh, doing it all with like discrete components and stuff is a blast. So, you know, at this point I have this, this prototype of this, uh, um, this device, which takes a bunch of control voltages in, uh, has a bunch of oscillators and filters and whatnot. Um, and a bunch of sync generation and generates this goofy analog video, which most of the time just looks like a, you know, like a unicorn puke, but, uh, uh, but I'm, I'm pretty happy with it. It's, uh, you know, I'm never, I'm never totally happy with it, but this one's pretty good. So maybe one day that'll get out there too.

**Chris Gammell:** Like it's like a, another kid or something like that.

**Todd Bailey:** You're saying that one would never be a kit. Uh, that one's, you know, that one's, there's enough, there are enough, uh, Hey, I, I don't, I'm kind of over through hole.

**Chris Gammell:** Uh, welcome to the 20, 20, 10s. 2000s. All the nineties. Right.

**Todd Bailey:** So it's like, so I, part of the kit thing is you have to scale back to through hole. Um, and part of it is also like, like, uh, you know, I want to make this thing like, where's the party at was made to be of the people. This thing is made to be as bad-ass as it can be. And so the design, the design criteria are different. You know, it uses expensive parts. Uh, and so, uh, so I wouldn't necessarily want that to be a kit. Right. And I also don't still want, I, you know, I'm not that motivated to make that many of them, but I would make a few. Uh, and I think that would be fun to have them out there. I think it's, you know, I'm, I'm happy with it. I like, as far as competing analog video synth technologies go, I think this one is, is right up there with the best of them.

**Chris Gammell:** So I want to ask you about your process real quick. Do you do any assembly house stuff at all? Or do you do all self-assembly?

**Todd Bailey:** Uh, oh, I definitely do assembly house stuff when it's appropriate. Um, you know, like for this, for this thing in the house in the Hamptons, uh, hundreds of boards got made for that. And I damn sure wasn't going to build all of those by hand. Uh, you know, and, and a lot of the time though, you know, the process isn't nearly as, as tight, but it's most of the nature of what I do a lot of the time is either, um, is usually not building very many of something.

**Chris Gammell:** Uh, right, right, right. So set up charges kind of hit you in the, in the gut kind of thing.

**Todd Bailey:** Well, and, and more, more it's turn time, right? Most of these clients want something done really fast. So, uh, so, you know, you don't have very many board spins before your thing has to go out. Um, and, you know, and you don't have a ton of time for an assembly house to, to do something. And frankly, you know, there's not that much that, that a skilled, uh, assembly technician can't assemble, right? Like there's, I'm not putting together a ton of BGA boards here. Uh, you know, and there's not, you know, I wouldn't, most of the things I lay out for work don't have more than four layers. Um, and you know, an 0402 is probably the smallest thing that I would ever put down. So, uh, it's, it's the sort of thing that, that you can get done, you know, you can like in the time that you would spend shipping something away and getting it shipped back, uh, you know, it's, it's just a question of expediency most of the time.

**Chris Gammell:** Gotcha. Okay. Yeah. Cause I mean, I just wonder about that with, uh, you know, you, you talked about these, I guess the kit's a little different, but you know, these, these devices you've, you've worked on in the past too. And I think as, as some more of these, you know, one click order, quote unquote, kind of stuff comes up like the, the circuit hub guys and stuff like that. Just thinking about how, how that, how that changes your relationship with this, right? If it's a, if it, if it really was one click, which I don't think it, you know, it will be for a while yet, but if it was just one click, how does that change? You know, someone like you, who's, who's interested in solving problems and idea based design type stuff, and then just kind of offloaded that manufacturing stuff. I think that makes for an interesting change.

**Todd Bailey:** It does make for an interesting change. I mean, like, like you said, I was like, when I said something about service amount, you were like, yeah, welcome to the nineties. Um, you know, print and circuit boards, being able to get a board, uh, has been something that people have been able to do for a long time, right? It's easier now that it is.

**Dave Jones:** Oh, it's a, Hey, 10 years ago, forget about getting the cheap prototype boards you've got these days. Sure. It was just un, un, unheard of. There no work, you know, there were no cheap prototyping services. You want a board? It's 500 bucks plus. Thank you very much for one.

**Todd Bailey:** So I, what I'm talking about now is more like, um, I, I totally a hundred percent agree. Uh, but I'm saying you could get boards, right?

**Dave Jones:** Like if you were, no, no, you could, but yeah, it's, it's not, it's not trivial. Like, like kids in their garage are getting boards now, you know, 10 year old kids building a something in their garage, you're getting the PCBs made. That was unheard of 10, 15 years ago.

**Todd Bailey:** I mean, you know, my first, my first quote printed circuit board was definitely, it definitely involved some ferrant chloride, you know? Yeah, yeah, exactly. Uh, um, and a, and a crappy drill press. Uh, and we huffed it for good measure. Uphill in the snow two ways. So, you know, like that's like, for instance, maybe, maybe that's relevant to what you're asking. Uh, like I have etched some boards. I have them around here. I'm proud that I did. And I never really want to do it again. Uh, like I don't need to have, I don't need to have ferrant, ferrant chloride in my life anymore. Uh, and so, so it's possible, I suppose that assembly would get to a point like that, but you know, I mean, it's like when you order a board, right? Like your degree of confidence should be pretty high. Like when you're actually like ordering, you know, glass, uh, usually you, you have, you want to have a reasonable expectation that's at least most of the stuff on there will probably work probably. Yeah. Uh, and so ordering, um, a populated board is even more like that. Uh, so I think that there's, there's, there's, there are convenience factors that go along. Uh, but there's also for me, I think it's, it's, it has to do with time and it has to do maybe with a little bit of like, uh, like micromanagement, right? Like, like getting somebody to assemble a board, uh, for you. If it's a board for like, it's a board for like hobbyist stuff and they have like a bunch of like, they're like, we have all the 5% resistors and some five, five, fives and LM324 and like some jacks, like pick from whatever components you want and we'll put them on this board for you and send you the board. That's awesome. Right. But if you're like, I'm developing this thing for this person, I don't know whether I need a 0.1% resistor and I want to use this one because that's the one I have the data sheet for it, blah, blah, blah, blah, blah. Like I found that typically speaking, like the board house that I use for assembly will be like, Oh, you can just tell us what you need and we'll put it on the board for you. I mean, never trust them to do that. Right. You're like, I don't know what random shit you have laying around from the last job you ran is like, no, no, you can't put it on my board. Like, uh, so, so I think part of the, like part of that is, is like, um, like the more variables you introduce and when you put a ton of parts on a board, like there's a lot of variables that you introduce, uh, um, you know, the, the less well you can control exactly what it is that's coming out. And I do believe that probably, you know, like, you know, within our lifetime, someone will make a pretty good stab at solving that sort of thing. And if they did awesome. Like I, you know, like if like I would buy into it if it worked, but I have not yet encountered

**Dave Jones:** something like that, which does it's, I hate to say it, but it's almost like the chip printer. It's one of those things, which is, there's just so many subtle things involved. Dig right in. It's just, yep. Sorry, dude. It's just that utopia is, is never going to happen. Sorry.

**Todd Bailey:** Uh, maybe, I don't know. I, I, it hasn't happened yet. That's all I'm saying.

**Dave Jones:** It'll happen for some niche things, but no, it'll never be mainstream. Sorry. I'm putting it, just hanging, hanging it out there.

**Chris Gammell:** Add it to the list, huh? Things to prove Dave wrong about.

**Todd Bailey:** Yep. Go for it. What was the other thing that you were like, it's, is a pipe dream? What did you just say?

**Chris Gammell:** The chip printer.

**Todd Bailey:** What's the chip printer?

**Chris Gammell:** That's the longstanding debate. Oh, let's not get started. No, let's not get started there. That's, that's the longstanding debate that Dave and I have about, uh, the possibility of one day being able to print semiconductors in some capacity in, in the home.

**Todd Bailey:** You have your, you have, you have your tank of boron and you're like, you know, and your 7,000 degree heater hanging out on your bench. Uh, yeah, well, I mean, that would be awesome too. If they had one, I would totally buy it.

**Dave Jones:** Of course.

**Todd Bailey:** It doesn't make it viable.

**Dave Jones:** You can believe all you like, but you know, actually believing something is not enough to make it true. I would love to be proved wrong on that. Like, I'm not going to wish against that. So would I. So would I.

**Todd Bailey:** Just keep waiting.

**Dave Jones:** I'm a practical guy. Yeah. Not. Sorry.

**Todd Bailey:** I mean, also the other thing is I've learned, uh, like one of the other things about, um, it's hard for me to say, one of the things about engineers is, because usually what that means is one of the things about me is, uh, I find, uh, I find that for some things I can be like the things that I'm confident in, I can be, you know, irritatingly and obtusely cocky about, uh, and it doesn't do well to be that way about shit. You don't know that much about. And one thing I've, I've learned the hard way that I don't know that much about is, you know, market trend. And like this, the sort of weird pressures that exist on the world to make different stuff. The stuff that I think is cool or useful or valid is really not always the stuff that other people think is cool or useful or valid. So, you know, I mean, if people, if people. Like the chip printer. Uh, so I don't know. I mean, I think, I, I think that people can solve just about any problem, uh, with the right pressures. Right. So I'm not, I, I, I'm hesitant to bet against things out of, out of hand. Uh, you know, at least until a couple of beers at which point I get pretty cocky about it.

**Dave Jones:** But we're not just talking about solving a problem here. Yes. You can print your own chips or yes, you can do the one line online order and click thing, but that doesn't make it mainstream viable. Doing so being able to do something technically and being able to make it viable for the mainstream are two entirely different engineering or, you know, it doesn't even become an engineering thing at that point. Yeah. I agree. Yeah.

**Chris Gammell:** If you're going to make a profit at it, that's going to drive, it's going to drive future research as well. So yeah, you're right. There's always that hump you have to get over. Uh, if you know, no one's going to even bother to look at it. Even if it's, if there's no reason to do it in the first place. So I agree with that.

**Todd Bailey:** Technology.

**Chris Gammell:** There's also business. Yeah. So, uh, Todd, where can people, uh, where can people find you online and elsewhere if they want to, if they want to ask you about, uh, well, I guess that's a good question to start with is, is currently, uh, April of 2014, you accepting new work or no?

**Todd Bailey:** Well, I'm always accepting new work. Um, okay. Always willing to talk. Yeah. I'm always willing to talk. I mean, I, I love a fun problem. Um, and, uh, you know, at this point, like, like, uh, you know, as you can probably tell from, from the evening, you know, I'm, I'm, I'm an offensive port like point in my life right now. And I'm like, I w I would love a new exciting problem. Um, like unlike the ones that I have had previously. So, uh, by all means, uh, anybody who wants to get in touch totally should. And I'd be happy to nerd out.

**Chris Gammell:** Uh, someone should, should, uh, send Todd an email with like a Zen cone in it, you know, like send him an email that says like a pine tree stands alone in a forest and then nothing else.

**Todd Bailey:** They're like, they're like, they're like, yeah. And you have an oscilloscope and five days to solve this cone. It's more like that. That's it.

**Chris Gammell:** Exactly.

**Todd Bailey:** Go. Go. Uh, here's your, here's your plane ticket. Uh, so, uh, yeah, absolutely. My, um, my website is narrative.com. Uh, you know, like books.

**Chris Gammell:** Um, and I is not an I, it's a one. It's a one.

**Todd Bailey:** N A R R A T numeral one V E.com.

**Dave Jones:** Those pesky, uh, URLs, which are already taken. Just like you can't get that customized number car number plate you want because somebody's already taken it. So you've got to be a waker and substitute in the five, five, five timer with no E in

**Chris Gammell:** it.

**Todd Bailey:** Yeah. Yeah. Exactly. They're like East Timor. What's that? Yeah.

**Chris Gammell:** All right. Cool, man. Well, thanks for, uh, I think you're on Twitter too, right? So people can find you on Twitter.

**Todd Bailey:** Uh, my, my, it's actually my real name on Twitter. So it's at, at Todd Bailey. Um, just wait. So get at me about your nerd problems, I guess. Or, uh, if you can solve all, if you can solve all these, uh, you know, uh, deep introspective, you know, Jack Handy style thoughts, then please, uh, you know, get at me too about that. I guess.

**Chris Gammell:** One of my favorite ones came into my life recently again, and it, uh, I will recite it here. If you ever drop your watch in a volcano, just let it go. Cause man, it's gone. I love Jack Handy. It's so good. All right. All right. Thanks. It's been awesome. It's totally been awesome.

**Todd Bailey:** Thanks. Uh, thanks so much for all this stuff. Um, and, uh, yeah, best of luck with the show. Best of luck with contextual, contextual electronics. Thanks, man. Thank you very much.

**Chris Gammell:** All right. Talk to you, man. All right. Take care. Bye.

**Chris Gammell:** Bye.

**Todd Bailey:** 192.

**Todd Bailey:** 192.

**Speaker ?:** I want to know. Where do you go? Oh, I want to know.
