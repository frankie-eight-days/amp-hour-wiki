---
episode: 324
title: Mapping Out Nerdery
url: https://theamphour.com/324-mapping-out-nerdery/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded November 23rd, 2016. Episode 324. Mapping out nerdery.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Can we, like, change our intro? We've been doing that for, like, what, 300 and something episodes now.

**Chris Gammell:** Sure, try again.

**Dave Jones:** Oh, no. Don't put me on the spot like that. Welcome to the Wacky Amp Hour Hour. Somebody did me a cool intro for the EEV blog. They did it. I saw that, the 80s style, yeah. 1980s VHS. That thing, I thought that was cool.

**Chris Gammell:** It reminded me, because, so we just had Tony on last week. And he has some, like, kind of similar, like, 80s style, like, there is, like, that certain quality to it. You know, you need, like, the audio to kind of, like, slowly turn on. Yeah. Yeah, it's certain lo-fi quality to it all, right? Yep.

**Dave Jones:** I like it. I might actually put it as the intro in my retro video. So, anything, you know, if I do, like, an 80s teardown, which I'm probably going to go shoot after this, actually. I've got an 80s computer I'm going to tear down. And, yeah, I might just slip it in there, like, without comment, you know. Yeah, why not? Right. Yeah, yeah.

**Chris Gammell:** It's a great idea.

**Dave Jones:** Yeah.

**Chris Gammell:** I don't know. Those things are fun, I think. You know, I think it's, you know, I think it has, it might get old after a little while, but it's, like, right at the beginning. Why not, right? That's fun stuff.

**Dave Jones:** No, yeah, I wouldn't use it every episode. I've got, like, I had an intro for years, and I just, nah, I just don't like them anymore. I just want the content straight in, you know. Just get to it, right? Yeah, yeah, absolutely. So, it's, like, hi, bam, straight into it. Boom, go, right. Yeah.

**Chris Gammell:** Yeah, it's funny how that stuff is, like, formative, though, too, right? I mean, like, because there's so much of, like, you know, you grow up kind of watching that content, or not even content. Like, it's like, oh, the program's on now, right? Like, you kind of. Right, yes, exactly. Yeah.

**Dave Jones:** And you're getting ready for it, and you're, you know. Right, but specifically with, like, the 80. Yeah, exactly, that kind of stuff. You know, and they'll have the jingle. Yeah.

**Chris Gammell:** Yep. What did you, what did you used to want? Like, so, like, did you, so, like, for my era, it was, like, Bill Nye was the big one.

**Dave Jones:** Well, here, it was the Curiosity show. Oh, oh, oh, that's what that is.

**Chris Gammell:** Okay, yeah.

**Dave Jones:** So, yeah, so they had the intro jingle, you know. Curiosity, what in the world? You chow or white, you know, and blah, blah, blah, you know, and you got ready, you know, and it hyped you up for the thing. But, no, in today's fast-paced information world, no. I don't know.

**Chris Gammell:** I mean, I think, so, like, well, I saw that, so, you were talking about Tesla 500's video, and he even talks in his intro about, like, Mythbusters, right? And, like, that was kind of a, I'm sure that people a couple years younger than me, like.

**Dave Jones:** Oh, yeah, it'd be Mythbusters. You know, like, Mythbusters would have been the big one, too, right? Yeah, of course.

**Chris Gammell:** Yeah. Yep. And we should mention at the top of the show, we will have Tesla 500 on the show next week. I don't know if that's a spoiler, but we'll be talking to him next week. Yep. So, at least that's the plan. We'll see. We'll see how, you know, hopefully it all works out.

**Dave Jones:** And I just released a video of you in his camera. It's very cool. It's very cool.

**Chris Gammell:** That thing is. So, okay, so tell me about that real quick. I mean, we'll obviously be talking about it next week. But you mentioned, like, tens of thousands of frames.

**Dave Jones:** 21,000 frames per second is its best case. But it can only do, like, you know, 60 pixels high at that. Because it only gets, like, one strip of video. Oh, I see. So, it's great if you're, like, shooting a bullet through a balloon, you know, and you have, and you watch that bullet go horizontally across. It's great for shooting that. Gotcha. But it's not the format that you want for, you know, anything else. Cool. Yep. But no, it's. But even if you do HD, not full HD, but, you know, 1280 by 720, it'll still do 1500 frames a second.

**Dave Jones:** Yeah, that's nice. Which is very useful. Yep.

**Chris Gammell:** Yeah. And we'll talk all about. So, and if people have questions about that stuff or they want us to ask questions next week, you know, you can post the questions to our subreddit and we'll try and get those in. Yep. Yeah.

**Dave Jones:** There is on the forum about this camera. Somebody, I think it was Mike, actually, pointed to another Kickstarter. Like, it was basically competition for this. It actually got funded for, like, a couple hundred thousand euros or something. I think it's in Europe or something. And they did a similar thing. They did a high-speed camera just like this. It's not as good. It's not nearly as good. But it's sort of like, but it was much cheaper. It was like $1,000 as opposed to $2,500. And it got funded. And the interesting thing about this, which I didn't believe at the time, but I think if you go through and run the numbers, it could actually work. And it's why maybe they've got the cost down, is that they actually use, as the video frame buffer, right, because it's got to be high-speed, right? So you've got to buffer that stuff. They actually save it directly to NAND Flash.

**Chris Gammell:** Interesting. Okay.

**Dave Jones:** Yes. Whereas I thought, A, it wouldn't be fast enough, but I guess it is. If you look at the throughput and you do the calculate, the bit throughput and you look at the calculation and all that sort of stuff, they store it directly. Whereas Dave's camera, his one stores it to RAM first. It stores it to DRAM. So that's why you can only store four seconds of footage, right? Because there's a limit to how much DRAM you can, you know, actually, because you need to write to it fast and often, you know, because it's continuously looping. So it'll sit there. So once you arm the recording, it'll just sit there continually, continually recording that four-second loop, right?

**Chris Gammell:** Yeah, it's like FIFO where like you get the newest footage just pushing out the oldest footage kind of thing, right?

**Dave Jones:** Exactly. Yeah. So it's a continuous loop. And as soon as you press stop, then it will, yeah, it's captured that four seconds worth. Or you can also have a post-trigger thing as well, where once you press stop or trigger it, it'll go for, you know, half the buffer again or something like that. Right.

**Chris Gammell:** Yeah. That data throughput stuff is nuts. And I'm sure like that stuff, like that's going to be a great question for next week too, where we'll be able to ask about, you know, like you got to just, especially like with the bit widths of however much data is coming out of that sensor and everything.

**Dave Jones:** It's 1.5 gigabits per second data rate from the sensor. Yeah. Yeah. That's crazy. You know, but hey, if you, but that's serialized, right? So you whack that into a little FPGA or CPLD or something so that you can paralyze it, parallelize it.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** You know what I mean?

**Speaker ?:** Yep.

**Dave Jones:** Yeah. So what? Yeah. So the serial data coming in, but you don't store stuff serially. Right. You, you know, you, you put it into bytes and then you store it in memory. Right. So then, you know, that sounds like a high data rate, but then if you store it at byte wise, for example, then you actually divide that figure by eight and that's your byte data write rate, you know? So it's different. And then if you, if you're storing 32 bits at once, cause you've got a 32 bit wide memory, you know? So the wider you make your memory, the, you know, if, if you've got 64 bit memory, for example, then you divide that 1.5 gig bits by 64. And, uh, and actually I'm going to do that 1.5 in divided by 64 bit wide memory. You're only looking at 23 meg, right? So that is your write rate. 23 meg.

**Chris Gammell:** Yeah. It's still pretty fast, but yeah. Yeah. Yeah. I know. I know what you're getting at. Yeah.

**Dave Jones:** Anyway, so that, what I found interesting about that, uh, cheap ass camera is that, um, it was, yeah, it was storing it directly to flash. Now, not only is it, well, there's potentially speed issues there, but also, um, if you're continuously arming and writing to that, well, of course, you know, if you're continuously writing to flash, that's not a terrific thing. Although they've got, you know, wear leveling technology and everything these days for these solar state drives, but still they, they, they do have a finite lifespan. I mean, you don't want to, I mean, you get one of these, uh, modern PC solar state drives and you continually write to it 24 seven over the whole thing. It ain't going to last that long. You know, I, I, I don't know the number behind that, but yeah, yeah.

**Chris Gammell:** Usually I, I use like a thousand to 2000 erase cycles for like, you know, I mean, you get more when, when you have that other technology in there to kind of detect what actually level

**Dave Jones:** it out. So you're not always writing to the same spot. Cause if you always write to the same spot, bingo, it can, you know, be gone in like an hour, you know? So anyway, very interesting stuff.

**Chris Gammell:** We'll talk more about that next week, I'm sure too. So that'll be, people have questions right on in.

**Dave Jones:** That will be interesting. And I'll be doing a teardown of that too with Dave helping out in some.

**Chris Gammell:** Oh, awesome.

**Dave Jones:** We haven't figured out how to do that yet. Maybe a Skype call or something. So, all right.

**Chris Gammell:** So what, uh, well, no, I was going to ask more about the high speed stuff. So, yep. No, no. I'll ask, like I said, I'll ask that next week. Yeah. Yeah. Okay.

**Dave Jones:** Yeah. We've already been rattling on for 10 minutes.

**Chris Gammell:** Next. Yeah. Um, I don't know what's next.

**Dave Jones:** Where are you at the moment? Are you back home?

**Chris Gammell:** Oh, yeah. I'm, I'm at my parents' house. I'm in Buffalo. Oh, okay.

**Dave Jones:** All right.

**Chris Gammell:** Yes. Tomorrow is a holiday here. It's Thanksgiving in the U.S. So. I have no idea what that is, but okay. The following day is the real holiday, right? Is, uh, Black Friday.

**Dave Jones:** What do you mean the following day is the real holiday?

**Chris Gammell:** Oh, oh. The joke being that, uh, you know, it's the shopping holiday. Uh, so, Black Friday is.

**Dave Jones:** Oh, is that Black Friday thing, is it? Yeah. Right. Okay. Right. Maybe I should have, like, a Black Friday sale on my multimeter on Amazon. Should I?

**Chris Gammell:** Uh, sure. Why not? Okay. I don't know how that would work, but why not?

**Dave Jones:** Well, I just put in a product discount thing. Amazon's weird. Tell you what, you know, I, like, I've just listed my product on Amazon, um, Canada, right? And I thought, oh, because the Canadian, the Mexican, and the U.S. Amazon sites are linked in terms of your seller account, right? No, in terms of your logged in seller account, they're linked, right? And I copied my product, and it said, oh, do you want to sell your product in Canada? Oh, yeah. Hell yeah. You know, right? Just hit this single button, and it'll all be done for you. Great. Okay. I did that, and it listed my product, um, or it copied it over, and so I copied all the, so I didn't have to re-upload the photos and the description and all that sort of stuff. So all that sort of stuff worked, but then they said, oh, no, it's not visible. You've got to send stock to Amazon Canada, you know? Yeah, right, right, right. You know, I, oh, oh. Sometimes I do wish for, like, the world was just a flat, open trade economy, and there was no bullshit, and anyone could trade with anyone, and there were no import restrictions and tariffs, and, you know.

**Chris Gammell:** Yeah, that would be very interesting, I think. I think that would definitely be, I mean, like, because people talk about that stuff, I don't know what that would actually look like.

**Dave Jones:** Never do I, but as from a seller's point of view, it's bloody annoying. Europe is a pain in the ass to sell into for anyone outside of Europe, getting stuff in there, and shit, I can't even sell in bloody Canada from my warehouse in the U.S. I mean, you know, they're practically cousins, aren't they? Canada and the U.S.?

**Chris Gammell:** Pretty much. Yeah.

**Dave Jones:** You know, I don't see a big fence all along the border, you know? I mean... No comment. Yeah, like, it's just annoying, and, of course, I, and then I want to sell on Amazon UK as well, and get into Europe. No, that's an entirely separate website. I have to create a new account, new login, can't even, can't even download my product info from Amazon U.S., so I don't have to re-enter it all. I've got to create that I can find anyway. It's just, oh, bloody hell, so...

**Chris Gammell:** Yeah, no, there isn't, it's interesting just kind of thinking about how much, how much of industry is kind of dedicated to logistics and then the legal aspects and the accounting aspects. Like, yeah, all that stuff really, it really does start to mess with things, so...

**Dave Jones:** I mean, we're, at least here in Australia, we're pretty easy. Anything under a thousand bucks, no drama, it just comes straight in. Oh, that's good. So, yeah. Anyway. It still pays me, though, to, you know, ship my stuff from Taiwan to Australia, import it here, and then re-ship it to the U.S., to the Amazon warehouse. Yeah, I don't say... I could potentially get it, you know, all shipped directly from Taiwan to the U.S., but, you know, to the Amazon warehouse in the U.S., but it's just, yeah, it wouldn't save me a huge amount, so...

**Chris Gammell:** Yeah, yep, yep, yep.

**Dave Jones:** Because import duties here aren't much, you know, it's like, I pay GST, goods and services tax, but we actually, I can actually claim that back, so it's, you know, it's fine. So it doesn't actually, ultimately, come out of my pocket. So, yeah.

**Chris Gammell:** Awesome. Yeah. It's all good.

**Dave Jones:** Anyway.

**Chris Gammell:** Yeah. Well, I mean, it is kind of like that logistics layer that people usually don't want to think about. I mean, so we, I mean, we have, even just on this week, we have a bunch of stuff about, you know, Kickstarters and startups and all that, you know, similar kind of thing. But no one's like, no one's starting a Kickstarter, no one's starting a startup and being like, I want to get into the depths of the shipping logistics, you know, they have to, and the best ones do, are really good at it, right? But it's, you know, most of them care about things like, what's one of these things? Internet of Things standards. Yeah. We've got a thing on that. Did you put it in here? There are better examples than that. I did. Yeah. It's from Hackaday. But it's, it's just saying that there's really not a standard. That's basically the basics there.

**Dave Jones:** Oh, right. So it's an article, a rebel, the heading is a rebel alliance for Internet of Things standards. And then what? There is no standard? Well, hence it's a rebel alliance.

**Chris Gammell:** It could, one of the things was it could have been with Twitter. Twitter could have, they were actually going to attach metadata to the, to tweets for a while and then they decided to do that. Yeah. That part was actually pretty interesting. But they obviously went in a different direction and, you know, now with hindsight, it's like, oh, maybe, maybe you should have, but I don't know. It's interesting too because.

**Dave Jones:** One of my favorite bloggers, hang on, cringely, I'm going to find it. He did an interesting article on this because he did a startup company before the internet, before the World Wide Web, so like 1994 or something. Uh-huh. And anyway, it's very, let me find it. It's very interesting. And mentioned that like, because of all the, all the, all the Internet of Things attacks, like, you know, they're turning them into zombie machines and they're doing the, you know, denial of service attacks.

**Chris Gammell:** Yeah, the DDOS, yeah.

**Dave Jones:** Yeah, yeah, yeah, the DDOS attacks. And there's a way around that, you know. So his article's entitled Saving the Internet of Things. And it's really based on tech, which he did before the World Wide Web came along. So you don't use your traditional web services. You just use the internet infrastructure, but you don't use the, yeah, the layers that we're used to using these days that can be hacked so easily, you know.

**Chris Gammell:** Right, right.

**Dave Jones:** So, yeah, it's rather interesting. I'll definitely link that in. Have a read.

**Chris Gammell:** Cool. Yeah, that's great. Yeah, it's, it's, you know, there are some other standards out there too, but it's, I think, I think that's what it, like what you're saying is it comes down to like people are, especially the people that are writing software are used to using a lot of these transport layers that were, you know, that have a lot of infrastructure around them. So if you do take a little bit more time.

**Dave Jones:** And it's the not invented here syndrome, right? Right.

**Chris Gammell:** And explain what that is for people that don't know.

**Dave Jones:** Not invented here is companies generally do not like stuff that's invented somewhere else. If it's not invented here and not invented within our company, then no, we don't want to, we don't want to use it. We don't want to adopt it.

**Chris Gammell:** Right. And some, okay, so, so I think in the, in the negative case, it's basically that's ego, right? That's like people saying, oh, well, I could do it better. I would have done this and this. I might as well start from scratch.

**Dave Jones:** Or there could be technical reasons behind it. Oh, we want it to do something slightly different. So therefore we're just going to have to scrap the whole thing and do it our way, you know? Right.

**Chris Gammell:** Right. I think on the opposite end of the spectrum though, it's, there's a legit reason where it's like, I don't want to be beholden to someone else. Right. So like imagine everyone picked up Twitter as their, as their way of delivering, you know, sensor data for whatever, or if this, then that, or many of the services are already out there. Like people saying, well, that's great until, and it works now, but what, what, what about when it stops working? What about when they jack the price up? Whatever.

**Dave Jones:** And we've talked about that endlessly. Yeah.

**Chris Gammell:** Yeah. Right. And I, but I think that is still a valid argument. I mean, um, there was an article we had on the, on the list here this week about, um, about, oh, well, Nest shouldn't be a hardware company. They should be a, uh, a services company. Right. And it's like, yeah, I mean, like it's okay. So basically the idea is that the economics don't work because they're selling it for 250 bucks, but you know, only 60 of that is going towards the company. Whereas that's not enough margin to really make them survive. Yeah.

**Dave Jones:** They, they realize they can't make a killing with an internet of things, bloody hardware thermostat, you know, I mean. Right.

**Chris Gammell:** And so the author, the author is basically, um, uh, proposing that, you know, you, you really lower the price of the hardware and then you make it all up on the services on the back end. But, but again, that's the same, that's the same problem of, well, now your thermostat in three years when Google slash Nest slash whatever their alphabet is called, right? When they stopped doing it, then what, then what? You're like, your house stops working, uh, your, your heat stops working or something. I don't know.

**Dave Jones:** It does. It does. It stops working. Right. And if you don't think that's going to happen, you're an idiot. It's already happened countless times and we're not even 10 years into the internet of things, you know what I mean?

**Chris Gammell:** Right. But we say that from our perspective. I mean, for some people, it's just not an opportunity. It's not an option, right? It's not like they're going to like they're, they're buying it and either they say, I'm either going to rebuy it in three years or I'm going to just deal with it for whenever. But you know, these are.

**Dave Jones:** Most people don't think about it. They think it's not going to happen. They don't give it a moment's thought or if they do, they just brush it away. No, who cares? You know? Like, yeah, you'll care when it stops bloody working.

**Chris Gammell:** Right. Right.

**Dave Jones:** But you know, all we can do is say, I told you so.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** And with the, who wouldn't want to, what company wouldn't want to own the platform though?

**Chris Gammell:** Well, that's the main thing.

**Dave Jones:** And that's the problem, right? Why, why be tied? If you're a company that's in this internet of things, why would you want to be tied to somebody else's platform when you could make your own platform and you could be number one? And, you know, it's like, that's why these standards.

**Chris Gammell:** I control it. Yeah. Yeah.

**Dave Jones:** So, so do you see an internet of things standards ever happening? I, I can't. I.

**Chris Gammell:** Me?

**Dave Jones:** I think there's got, you know, there might be one dominant player, but they might last 10 years and then something else comes along. It's like, I can't. Yeah, you.

**Chris Gammell:** Uh, I don't, I don't think so. If anything, I think it's like what you're saying. Like if they, if it was big enough that it got taken up by everybody and they kept it open, then maybe, but I don't think that that would really happen.

**Dave Jones:** I can't see that happening as a natural part of the growth of the internet of things. It's just, no.

**Chris Gammell:** Yeah. Um, it's especially interesting. I think with the, uh, the focus on home stuff, right? Like that's, you know, you see that a lot with projects too. People are like, oh, I think it's, I think they're popular because people can envision, oh, I have this, I have blank problem in my house and I could think about, you know, solving it with blank. Right. And either people are going to solve it themselves or they're going to go and buy a solution that, that seems to solve that same kind of thing. And so it's, it's very easy to visualize like that. Um, I, yeah.

**Dave Jones:** Here's where I think cringely is possibly right on this. And probably the only way it's, I can see it happening is that it needs to be an internet layer in itself, right? Like, like we've got HTTP, right? For our, you know, web and all that, you know, and we've got all these different services, you know, and I'm not really into the actual technical details of all this stuff, but the internet in quote marks is made up of all these different layers of, of protocols and stuff, you know, the internet of things probably needs its own layer like that. Perhaps. Is it like the, um, what is it? The, um, Aussie, uh, layer, the ISO Aussie layer of, um, yes. What's kind of used to know this stuff. Um, the OSI layers, um, the OSI model. The OSI model of how, um, of how like the, the communications network. Come on, help me out.

**Chris Gammell:** I have no idea what you're talking about. I'm sorry, man.

**Dave Jones:** The, the ISO Aussie model is a seven layer architecture. It defines various network. It's a networking thing. It defines the networking architecture. You've got different layers. Like you've got the physical layer. Here we go. You've got the physical layer. The, I used to know these off by heart. The physical layer, the data link layer, the network layer, the transport layer, the session layer, the presentation, and then the application layer. It's, it's, it's actually a model that's used in all of networking. It's a standard model that everyone uses. Okay. You know, so may, you know, we've got the physical layer, right? The internet consists of this physical layer, right? There's all these routers and there's fiber optics and cables, right? And servers and everything else. There's a physical layer. And then there's going to have all these different layers on top. The internet of things requires its own layer deep down, I suspect, for it to become a standard.

**Chris Gammell:** I'm so out of my element here. You're out of your element. Okay. Well, I do know. Sorry, right.

**Dave Jones:** I do have some experience in this. Okay. Yeah. From a networking point of view. Anyway. Yes. Read the article. And I think, yeah. Okay. So it might require some standards organization like the OSI to come along. Or ISO, the International Standards Organization, to come along and ratify and go, right. But then again, that hasn't helped for other stuff.

**Chris Gammell:** Wait, I was going to say, I think I saw an article about that a couple of days ago where they were talking about the X25. Right. Yeah. And that didn't even really take hold. It was like, although this is showing them on different levels.

**Dave Jones:** And a few people used it.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** I think that's what it comes down to is like standards. You can never really tell when a standard is going to be adopted until after the fact. Right. I mean, like. Is there an XKCD for this? Probably. Yeah.

**Dave Jones:** Yeah. There's probably like for standards and like a standard exists for making another standard. And like.

**Chris Gammell:** Yeah. I think the bigger thing would be like, I mean, so it seems like. So with like the internet piece, everyone's doing it. Right. Like everyone was kind of wanting to interconnect and there's a lot of money involved in that. It seems like with the, the internet of things piece, it's a couple of big players. Right. And. I actually did see this. So let me just say I. At the application side of things, like if this, then that, I think that that's actually a really interesting service. Because it's so. It's so simplistic.

**Dave Jones:** It's not going to become a standard.

**Chris Gammell:** No, definitely not. But it's, but then if you look at like who's actually paying them for their API access and like, so who's putting devices on there? Right. There's all like the Wemo stuff and there's all the, like Samsung put a bunch of their stuff on there. GE put a bunch of their like devices on there. You know, they publish APIs towards their washing machine or whatever. Like if, if washing machine done, then. Yeah. Then send email or then call phone or something like that. I was playing with that the other day. Yeah. And, and you're like, you're right. That's not a standard, but it's just.

**Dave Jones:** It's a, it's a standard service. Can we.

**Chris Gammell:** Right. But I'm saying that there's not. Call it like that. It's not like there's, it's not like every company out there is clamoring to put their device endpoint onto if this than that. Right. There are. Right. Because it's like large scale device manufacturers versus, you know, mom and pop shop. You know, it's not connecting individual computers. It's connecting some class of, of device like Samsung washing machines. Right.

**Dave Jones:** But if you were developing an internet of things widget, wouldn't you want it on there? Wouldn't you develop a, a class, you know, an API thingy for that and have it on there? If then, then.

**Chris Gammell:** Uh, I mean, if, if I, if I could afford it and I had the developers to do that kind of thing, sure. Right. I mean, that might drive more adoption and stuff like that, but. But, well, you've got to have some service, right? It's not just, it's not washing machine. It's Samsung washing machine. It's not light switch. It's Wemo light switch or whatever, you know? Like, so it's, it's still very proprietary. And because these are companies are trying to differentiate themselves as like, I have internet connected thingy. Like, and until everybody puts internet connected thingy and there's some kind of like washing machine, like even just a generally agreed upon standard of like, uh, washing machine dot done or whatever. You know what I mean? Like, it's like, I don't know, these software layers and it gets weird.

**Dave Jones:** You've got to have some service so that people can use it. What would you choose? Would you roll your own? Would you use if, then, then that? Or would you use some other, there's been a dozen other services out there. There's the, there's the Amazon one now, right?

**Chris Gammell:** What's the Amazon one?

**Dave Jones:** Don't Amazon have a, think, oh, they've got an interface or something. You can, uh, I'm looking for it. It's not like an endpoint.

**Chris Gammell:** It's like, uh, you're talking about like Alexa and like the, the Echo Dot and stuff like that?

**Dave Jones:** No, this is the AWS Internet of Things. They've, oh, that thing. Yeah. Yeah. Whatever it's called. Amazon have like 20 million different services. Um, right. And I've mentioned on here before that if I was going to rely on an Internet of Things server, that would, stands the best chance of being around in 10 years time, I would bet on Amazon. Yeah. I would bet on the Amazon server still being, you know, being around. And we've argued that before.

**Chris Gammell:** Yeah. Some of that is preference, but I think in general, I would probably agree with that most days. I don't, I don't know. I'm, I'm not planning on putting. Okay. Yeah.

**Dave Jones:** If you're starting a, if you're doing a startup, Internet of Things startup, you've got Internet of Things widget and you're going to the VCs, you've got your pitch deck all ready to go. You know, I mean, like you're going to want to have your own platform, right? Yes. Because that's probably going to sound a lot better. You can, you know, like get people to subscribe to your, you know, access to your platform. And that makes you, and that gives you your hockey stick revenue growth, you know, adoption curve that, that you need on your pitch deck. Right. And so that's why, like, these things might never work.

**Chris Gammell:** Right. Yeah. Until there's some kind of compare. Yeah. Until it's like so splintered that they're like, oh, I guess we should work together. Then, yeah, you're right. It's never going to work.

**Dave Jones:** And even then there'll be some reason not to.

**Chris Gammell:** Yeah. Probably.

**Dave Jones:** Because insert issue here. It's too hard. I give up. Next.

**Chris Gammell:** Well, speaking of some of these big companies and speaking of, well, appliance companies too, I actually met someone that used to work at First Build. Do you remember what that was?

**Dave Jones:** No. What's First Build?

**Chris Gammell:** I think we actually talked about it on here at one point. Probably. Yeah, it was GE's thing. So it was GE Appliances. They had like some like RS-45 standard where you could basically like hack into fridges and stuff like that. They were kind of trying to open up like devices and stuff like that. So I met someone that used to work there who now lives in Chicago and she is running the Fuse, which is kind of interesting. What's the Fuse? So Fuse is like GE's new thing where like they have.

**Dave Jones:** Oh, so she's still working for GE.

**Chris Gammell:** Yes, but it's like a new program. Right. And so it's like an industrial, almost like a contest type thing, like a B2B industrial contest thing. And so they're trying to solve problems. So like these are actual internal problems at GE where they're basically turning them into contests so that like if grad students don't have fixed them, they can just kind of work together and do that kind of thing. And so one of the things was like, how do we see invisible welds in pipes? They're saying HFI pipes. I don't know what kind of pipes those are. But basically it's detecting weld seams and engine inspection for like GE aviation, like just like big problems that they, you know, have are having trouble kind of getting through, kind of throwing it out there. And I think this is an interesting model because they're also working with local motors. I don't know if you know who they are. So they're the ones who do, they do kind of like an open innovation model where they, they basically have community contributed content and then they, but they're building like cars and bikes and all these different types of vehicles. And then they actually have micro factories where you can go there and pay to go build a car basically on site.

**Dave Jones:** Oh, right. Okay. Yeah. Interesting.

**Chris Gammell:** I think it's, yeah, it's a really weird and kind of interesting. I think those guys are out of Arizona. Yeah.

**Dave Jones:** So what happened to this GE thing that she was working with before? Is that another example of a standard service that just folded?

**Chris Gammell:** No. First build. So the whole, the entire GE appliance division got sold to a Chinese company.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** Yeah. Right. So it went with that. Yeah. I think. So this is just a evolution of that same idea, but kind of taken to a broader, I mean, obviously GE is huge, but, but got a chance to talk to Amelia about it. And I don't know, it seems like a really interesting idea. Like, you know, a lot of these things where they're, you know, they're working with, they're working with maybe like a grad student who might already be doing some of this research and they kind of take that and then offer money for it and stuff like that. I mean, like there already are methods for, for working with them, obviously, but it's kind of how do you broadcast that you're looking. Right. And I would think that a contest like this, especially it's just a very specific thing where it's like welds, right? Like, so you get everybody who's looking at welds and you say, there's, there's real money here. You know, that's kind of interesting. So. That is interesting. So someone, someone knew that I met. So that's, that's nice. All right.

**Dave Jones:** Because you're in now a Chicagoite? Chicagoan. Chicagoan. Chicagoan. Yes. Yes. Chicagoan. My apologies to all you Chicagoans.

**Chris Gammell:** And I found out today I need to, I feel really stupid. Like I was, I was talking to the, some people on a, on a Slack channel that I'm on. Like I need like a nerd. Slack channel. Slack is like a, it's like an IRC client kind of. Oh, chat.

**Dave Jones:** That's a chat. Yeah. It's a chat program. Oh God.

**Chris Gammell:** It's like a modern one. But anyways, we were talking about, I was like, well, let me say this first thing here. Speaking of Chicago, I, I, I didn't even know. Yeah. I didn't even know about the museum of science and science and industry in Chicago. I didn't even know about that. And it's like, so then I started looking at this thing. I'm like, oh my God, this looks amazing. I have to go here. But I didn't even know it existed. So. Right. So what I was saying though, is that I need like, and maybe this already exists. And I just haven't found it. I need like a nerd map. So anytime I go to a new city or anything like that, it's like, here's all the, the nerd, the nerdy things you need to see. Right. So some of them are obvious, right? Like computer history museum and the HP garage and stuff like that's like obvious. Right. But I'm saying like.

**Dave Jones:** Dude, register the domain nerdmap.com and then all, then have a Google Maps plugin thing, which displays it. And then people can come along and add interesting nerdy stuff.

**Chris Gammell:** Maybe I'll do that. Yeah. Maybe I'll do that. Nerdydaytrips.com. I guess that's one thing. Is that one? Someone has that.

**Dave Jones:** Someone has that. Nerdydaytrips.com exists.

**Chris Gammell:** Yeah. These aren't very good. This isn't very good, but like, this is just a, yeah, nerdydaytrips.com. Apparently that's a thing. It just redirects you back to that map, I think. So, yeah. So that kind of thing. I need something like that. So if there are other, if there are other resources out there, because like, I feel like now that I've lived in the city for like four months, I should have probably known that. But yeah. But I'm sure there's stuff like that. You know, you and I were talking about when I visit Sydney too. It's like, you know, like there might be some hidden gem that even you don't know about, right? It's like.

**Dave Jones:** Oh, I'm sure there is. But yeah, we have hardly any tech here, but there could be.

**Chris Gammell:** But it could, I mean, it could be like, like, I mean, like, it could be like your lab is on that map. You know what I mean? Like.

**Dave Jones:** No, right. Okay.

**Chris Gammell:** You know, like it could be, it's not necessarily, but. Oh, no, this nerdy day trips is not what I wanted. Yeah. So maybe nerdmaps.com.

**Dave Jones:** I don't even get anything for that. What? Just a blank page. Nerdydaytrips.com.

**Chris Gammell:** It was, I found a, I found a, like a linked map that's like that. So. Right. Anyways, maybe, maybe that'll become a thing. Nerd maps or. Yeah. So if people know about a resource like that or they want to help build one. Yeah. That's something that's needed. Cool. So you're in Chicago. We'll see.

**Dave Jones:** We have to do it for the, how could we make money out of that? How could we monetize it?

**Chris Gammell:** Well, what we do is, is like, you, like you, you put on a headset and you're like, hello, I'm Dave, your tour guide around Sydney.

**Speaker ?:** Right.

**Chris Gammell:** Don't laugh.

**Dave Jones:** Don't laugh. Have you seen the intro to my travel YouTube channel?

**Chris Gammell:** Your travel YouTube channel?

**Dave Jones:** Oh, you haven't seen this. Oh my God.

**Chris Gammell:** Wait, is this your old intro? Yeah. I think maybe I have.

**Dave Jones:** Yeah.

**Chris Gammell:** Well, recount it for the people that are listening right now.

**Dave Jones:** I will send you the link so you can watch it in all's glory again. Okay. Here we go. I know this doesn't work on radio, but Chris can at least have a laugh. And yes, I dug it out of the archives. I found it on an old hard drive, which was an intro to a channel, a travel channel that I was going to do. And I won't say anything more than that, but I'm glad I didn't get through with it.

**Chris Gammell:** There's still time, man. There's still time. It wasn't that bad.

**Dave Jones:** The intro was the best thing about it. Yeah. Let's put it that way.

**Chris Gammell:** See, the nice thing about that, though, is like, oh, I'm traveling. It's a business expense. All right. I don't know how that works, you know? You could. Yeah. Right.

**Dave Jones:** Yeah. No, seriously. If you had a, you know.

**Chris Gammell:** Let's talk about business expenses a little bit.

**Dave Jones:** Fine.

**Chris Gammell:** Yeah. Let's go for it. I mean, so I think that.

**Dave Jones:** I was just debating this morning, actually. Yeah. Like, I got a sore neck at the moment, and I need to get it, you know, I need to get like a massage to sort of help it out. It's been lingering around for a while. So I thought, I wonder if I can claim that.

**Chris Gammell:** No. I wonder if I can claim that. If it's not the States, you could not.

**Dave Jones:** Right. Okay. Now, I don't want to ask my accountant, because my accountant always says no, and I've found that is complete and utter bullshit. Well, no.

**Chris Gammell:** That's an accountant's job to be more conservative about that stuff.

**Dave Jones:** Conservative. But, yeah, of course, they'll always say no, right? Because they're asses on the line if you get ordered. Give me another example. And they said yes. Right? Well, I, food, for example, right? Right. I found that, you know, I claim food expenses that I have. Like, if I go have a lunch now, right? I can actually claim that. With someone or by yourself? No, just on my own, right? Okay. As long as I am not entertaining myself or entertaining someone else, I can actually claim that. Now, if you go to...

**Chris Gammell:** I disagree with that, at least in the States. Again, this is just in the States. I disagree with that.

**Dave Jones:** Okay. Well, here, you would disagree with it as well. And so would most accountants. Most accountants would say, no, you cannot claim that unless you're traveling. And that's what my accountant told me, right? And that's what the tax website actually says and implies as well, the top level. But if you actually go deep down, as I did, deep down into the tax website and actually searched their rulings, which is different to their top level advice, right? To their actual tax rulings. Yes, it's actually okay. And they've even got a list of under what circumstances you can do it and everything. And I showed this to my accountant and he went, yeah, you're right. It's like, well, shit, I should be charging you, right?

**Chris Gammell:** Hold on a second. So this could be taken to extremes though, because I used to work with like one of the most brilliant firmware engineers I've ever worked with. And then like you start talking to him about, you know, whatever life and I'll call him Bob here. And Bob's like, he's like, yeah. And, you know, so like you'd be talking about, oh, and like if you do this and see, but you know, you know, put in an assembly here and it really, you really have to understand the op codes and blah, blah, blah, blah, blah. And, you know, this and that and Cisco is better than risk and whatever. And, you know, you get deep into this stuff. And then at a certain point he would just turn around and be like, he'd be like, yeah, you know, if you really look at it too, you really don't have to pay taxes.

**Dave Jones:** Right.

**Chris Gammell:** What?

**Dave Jones:** Oh, he's one of those freemen, is he? Is he a freeman? Yeah, exactly. Right. Exactly. Yeah, yeah, yeah.

**Chris Gammell:** Like, Bob, I'm pretty sure that's illegal. And then, you know, and then like in the same amount of, you know, breathless exhilaration, he'll tell you all about that too. Yeah, yeah, yeah. It's like, oh, that's why he's so good at firmware because he's crazy. Right. But he was really good at firmware.

**Dave Jones:** I claim haircuts.

**Chris Gammell:** Yeah. Well, okay. I claim haircuts.

**Dave Jones:** I'm an entity. I'm a public figure. I have to maintain a look.

**Chris Gammell:** Okay, so then what I'm going to do here is back up a second and say, we are not accountants. We are not lawyers. We are not giving any kind of legal advice, nor should you take it as such. However, we are going to give our experiences, and Dave's going to record the fact. No, I see. I claim on air that he claims haircuts. I do not claim haircuts.

**Dave Jones:** I claim haircuts. And I claim bloody meals when I eat them sustaining meals. Because, and I have the links and the proof at the tax office website to back up my claims.

**Chris Gammell:** I'm not going to argue that because I don't, and again, that's another thing. It's like, right? You and I are in very different countries. Yeah, totally. And, you know, you need to check with your local laws, too. I would never do that in the States.

**Dave Jones:** But what I'm saying here is that you, like, you have to, if you research this, you might find that, you know, don't believe top-level advice. Because it may be wrong. Okay? I believe, I pay my accountant a shitload of money, right? Sure. For advice. And he got it absolutely, totally wrong.

**Chris Gammell:** Right. Absolutely, totally wrong. But that's one case. And he's really protecting you in a lot more cases than that.

**Dave Jones:** So, yeah. Yeah, but, you know. I know what you're saying. Anyway.

**Chris Gammell:** Anyway, so let's talk about the other stuff, though. So, like, so I think it's interesting. Okay, so at least in the States. So, why were we talking about tax? So, we were talking about just business expenses in general. Yeah, why?

**Dave Jones:** Is there a point?

**Chris Gammell:** Oh, because I said, you know, if you had a travel YouTube channel, you could claim, I joke, you would claim all travel is that. And I don't know how that would refer to travel channel. But what I do know is that if you're working on, you know, prototypes for people and if you're working at, you know, if you have a business and you're building electronics and specifically you're building them for projects that are for other people that you're going to, you know, sell commercially and stuff like that.

**Dave Jones:** So, you're a commercial contractor.

**Chris Gammell:** Exactly. Like, you don't even need to be, you don't need to be incorporated in order to claim that as a business expense. Now, again, you should check with your local accountant.

**Dave Jones:** No, you can, it's the same here in Australia. You can be a sole trader. You don't have to have a company business name. Or a sole proprietor here. I say sole proprietor, same thing.

**Chris Gammell:** Right, right. I'm just making that blanket statement of you should check, you should check your local laws, blah, blah, blah. Because, well, and that's another thing to mention, right? It's like you can claim whatever you want but at a certain point you might get in trouble for it.

**Dave Jones:** No, because we, as I'm sure you do in the US, you have a self-reporting tax system.

**Chris Gammell:** Right.

**Dave Jones:** Right? Yeah. Like, you can claim anything you damn well like and you can, I could, tomorrow, I could put in a claim that I claim, you know, a fraudulent claim that, you know, the tax department owes me $100,000 in tax taxes and they would pay me. Right? There's forms I fill in and say, no, I'm readjusting my tax for the previous year and you owe me $50,000. And they would actually pay me that. Money would come into my account. But then my risk of getting audited the next year is… You get a knock on the door real quick, yeah. And the sound of that glove being snapped onto the hand as they, you know… Right. Rubber glove, yeah. Right.

**Chris Gammell:** And it's not worth it to play with fire there, personally. It's a self… Yeah, but it's a self-reporting system. Because I think that especially in electronics, if you're, you know, if you are doing this stuff anyways, you can probably make more money building stuff for people than you would ever save money on taxes and stuff like that. Right, on taxes.

**Dave Jones:** That's why I claim very little because it's just not worth, you know… Like, I know people who go, oh, my accountant's fantastic. They found that I can claim 10% of my electricity because I work from home. It's like, do you know that's worth, like, how much that's worth? Right. Like, it's not even worth your time to claim that, you know, let alone…

**Chris Gammell:** Yeah, for me, it would be like, I think I have a $30 power bill, so it would be like… Yeah, exactly. …3 bucks a month.

**Dave Jones:** It's like a three bucks. I know. It's not even worth claiming.

**Chris Gammell:** Which not all of that even goes towards, you wouldn't get a $3 rebate each month. You'd get whatever your tax rate is times that. So, like, 25% of $3. Yeah, yeah, yeah. So, 75 cents.

**Dave Jones:** Like, I used to do that, like, decades ago, right? You know, I'd claim every freaking cent because, like, these days, like, I just don't bother. Like, I just… I couldn't care. Like, it's not worth my time. Right. Seriously.

**Chris Gammell:** So, I think that it's interesting, though, because, like, so there are probably people out there that are looking at, you know, maybe starting consulting or contracting or whatever. You know, there… It is possible to go… So, I have a friend that even goes on Craigslist in the States or he goes on… What's the one? It's not called Odesk anymore. It's called Plesk, maybe. But, you know, there are people looking for contractors. Personally, like, that's kind of like an open system where you can… You know, people will bid and say, oh, I'm looking to make, like, a vaporizer and I need to… You know, they say, here's what I need and then you can bid on it and say, here's my hourly rate, that kind of thing. Like, that's never as good as, like, building up your name and starting, you know, starting where you… People seek you out and… Of course. And I think the best way to do that is to be building your own projects at first, publishing those online, you know, do it for yourself at first, publish your work. And then, eventually, people are going to come to you and say, look, I want you to do that for me. And then you'll be… Usually, that quickly turns into more opportunities than you even know what you could do with. And then you can just take the ones that will actually pay you if that's your interest. So, that's a much better way to do it, in my opinion.

**Dave Jones:** Never take a job that's unpaid.

**Chris Gammell:** Well, as someone who talked about pro bono engineering, I am bucking that trend. You are bucking that trend, yeah. It's a very conscious thing, yes.

**Dave Jones:** Right. You have to have very specific goals and reasons in mind to do that. Right.

**Chris Gammell:** But I think what it really gets back to is, like, you know, if you're interested in eventually doing that kind of thing or even interested now, I think one of the best ways to still do it is to just publish your work, you know. Go on Hackaday.io. Go on Hackster. Go on…

**Dave Jones:** Dude, I've been saying that for 30 years.

**Chris Gammell:** Well, I know. It's okay to reiterate things, Dave. You and I have been known to repeat ourselves.

**Dave Jones:** To repeat ourselves, you think? Right.

**Chris Gammell:** Yeah. Once in a while. Once in a while. We should mention our friends over at Hackster, they just got acquired by Avnet. Did you see that?

**Dave Jones:** Good. No. I was going to ask, who's been acquired this week? Yeah. There are a shitload of them. Yeah. So, is this even on the link? Is this on the… Yeah, it's there. Yeah.

**Chris Gammell:** So, Hackster was bought by Avnet. No word on how much, but I know them. They're great. They got a great… They do a lot of contests and stuff, too. They do a lot of, like, in-person contests at, like, hackathons and stuff. Right. So, that's interesting. So, yeah.

**Dave Jones:** Have we talked about Hackster before?

**Chris Gammell:** I'm not sure we have. But, you know, they're a good site. And they just got bought by Avnet. So, we'll see if that… I'm guessing they probably won't change things too much. So, we'll find out over time.

**Dave Jones:** So, Hackster is a community dedicated to learning hardware. Choose a category. Oh, that doesn't work. It just says type. Arduino. Yeah.

**Chris Gammell:** You're just browsing during our show.

**Dave Jones:** It's a community thing. It's almost like Twitter. It's almost like Facebook. Sorry. Oh. I guess so.

**Chris Gammell:** I mean, it's also kind of like… I was listening… Oh, I was watching Ask an Engineer. They were mentioning about this, too. Oh, they brought up Instructables, too. So, it's kind of like Instructables. Oh, okay. Right. So, Hackaday.io is kind of similar, too. And so, you know, it's basically a place to document your projects. It's a place to, you know, interact with people about it. So, Instructables, yeah, I guess that was a really big one. They were bought by Autodesk a while ago.

**Dave Jones:** I'm not… I don't know if I'm really a fan of publishing your projects on sites like this. If you were to ask me, I would say do your own site. Have your own website. Publish your own projects on there. You know, build up… I would say the same thing.

**Chris Gammell:** But some people can't or don't want to.

**Dave Jones:** Which is fine. Yeah, okay.

**Chris Gammell:** Right, exactly.

**Dave Jones:** But if someone came to me asking for advice, that's what I'd tell them. Start your own website. Oh, right, right. Start your own blog or whatever and publish on there. Yeah. Yeah.

**Chris Gammell:** Yeah, makes sense. Or both. Or do it both. Maybe you want to get the community aspect and you want to, you know, make sure it sticks around forever. So, yeah.

**Dave Jones:** I wonder what a website like that's worth.

**Chris Gammell:** I have no idea. To have that. But I do know that Mentor Graphics apparently is worth $4.5 billion.

**Dave Jones:** Oh, right. Yes. I knew there was an acquisition somewhere. Yes. Who bloody bought them?

**Chris Gammell:** Siemens. Siemens. Siemens. The German industrial company. Siemens. My former nemesis apparently. When I was at ABB, Siemens was one of our competitors. Oh, yeah.

**Dave Jones:** They were arch enemies, yeah. Siemens bought Mentor Graphics. If you don't know, Mentor Graphics are one of the big three in quote marks of the PCB space.

**Chris Gammell:** Yeah, but this is actually, they were not being bought for, they were being bought for the other piece, not for the PCB stuff.

**Dave Jones:** Yeah. Mentor also do, you know, the chip level tools and all that sort of stuff. Right.

**Chris Gammell:** And that's the big stuff. That's the four out of the $4.5 billion probably. So, yeah, that's the big money. And, you know, this is their software service company. Yeah. Synopsis and Cadence are their big competition. So, I don't know why Siemens did, but.

**Dave Jones:** I think, I did read the article, but is there any plans to integrate them with Siemens or are they going to continue to operate them as Mentor Graphics and they just want the revenue

**Chris Gammell:** or what? Probably. I would assume so. I mean, like, there's not like that. I mean, so it's like Siemens is a lot of, like, they're huge in the industrial space, right? Oh, they're massive. You have no idea. Unless Siemens wants to, and I think they do make some of their own chips and stuff like that, but I can't imagine they would, they wouldn't shut out the other pieces. You don't like buy a $4.5 billion business or business for $4.5 billion.

**Dave Jones:** Just because you don't want to pay the license anymore.

**Chris Gammell:** Right. Or in order to cut the business out from underneath it, right? Right. No, no, no. Of course. If they've got a billion dollars in revenue or whatever it is, you don't want to be like, oh, well, we just paid all this money. Might as well not make any money in the future, you know? So, yeah, I would think they would want to keep it going.

**Dave Jones:** But then again, if you just want to buy a company for its revenue, there are countless choices, right? I mean, so why Mentor? There's got to be some strategic technical reason for it, which will be interesting to see long term. Yep.

**Chris Gammell:** So, one other acquisition, because this is the acquisition hour.

**Dave Jones:** We should just rename the show.

**Chris Gammell:** We should just, yeah, yeah.

**Dave Jones:** Like, we could start up another podcast, you know, the acquisition hour. And like, we should feel that every week.

**Chris Gammell:** I think we should make it more like the acquisition 10 minutes. We should really just, you know.

**Dave Jones:** Yeah, no, 10 minutes. And just announce, seriously announce each week an acquisition.

**Chris Gammell:** It's like a ticker tape. Eventually, though, it should turn down a little bit, right? I can't.

**Dave Jones:** You would think that, yeah, there's going to be just one big alphabet type thing that owns everything, right? Yeah.

**Chris Gammell:** So, the last one is Silicon Labs, who is based out of my former hometown, Austin, Texas.

**Dave Jones:** Yeah, didn't we do that the other week? Is that new?

**Chris Gammell:** No. This is new.

**Dave Jones:** Silicon Labs buys Micrum. Oh, we did talk about that last week. Did we? I think, I don't know. Apologies if we did.

**Chris Gammell:** I usually make the same jokes about getting the Micrium book. Yep. The big tunnel. So, yeah, probably.

**Dave Jones:** There was a tweet. Somebody, I forget. Who's the chip company that always, Real Tech? Is it Real Tech? Or somebody who always hides their data sheets away under NDA bullshit? And then somebody, who was it?

**Chris Gammell:** Well, last time we were talking about Media Tech, and that was what the...

**Dave Jones:** Is that Media Tech? Right.

**Chris Gammell:** Did they get acquired? Who was it? Well, usually it's more like Broadcom. Broadcom is the one that you think about, like the Raspberry Pi chip. Is that...

**Dave Jones:** Anyway, somebody bought one of these companies that hides their data sheets under NDAs. As soon as they bought them, they just released all the data sheets. I thought that was brilliant.

**Chris Gammell:** Oh, I didn't know that. Okay. Yeah, yeah.

**Dave Jones:** It was on Twitter. So, somebody tweeted and I retweeted and I forget. And I could look through, but it could take a while. Yeah, I thought... I should have just added that to the Reddit. I thought that was interesting. Yep. I didn't verify it, so, you know.

**Chris Gammell:** Gotcha, gotcha, gotcha.

**Dave Jones:** Please forgive me. But, yep. I thought that was... That was cool. I would love to do that, you know. Like, buy a company and then just give away all their... You know, like, something that's pissing you off. You know, it's like...

**Chris Gammell:** That seems really stupid, Dave.

**Dave Jones:** No, but, yeah, not giving everything away. Like, you know, but, like, stuff that should be free, and it's not. And they're just tying you up with red tape NDA bullshit, right? Right.

**Chris Gammell:** Well, a lot of the guys that are buying in charge of these deals, they don't really care about openness. Or really anything other than money.

**Dave Jones:** No, I just think it's a cool thing to do, you know.

**Chris Gammell:** Well, speaking of openness, formerly discussed, but now with a new goal in mind, the OpenV is now on CrowdSupply. So people know that we've had Josh on from CrowdSupply, and they have... They actually did change the... I don't know if you saw. They did change the front page.

**Dave Jones:** Oh, they did change something based on my feedback.

**Chris Gammell:** Over twice the success rate of Kickstarter and Indiegogo. Right at the first top line. There you go, Dave. Yes. Finally enacting change in the world, buddy.

**Dave Jones:** Yeah, finally. All this year, this seven years has just been worth it building up to this one moment. Exactly. Where I enact change, you know. That's right. Love it.

**Chris Gammell:** So this is previously mentioned... We had mentioned the RISC-V. And so this is a new open source piece of silicon. It's very interesting. We had been corrected on a couple of things we said about it, and I really don't know enough about it, even still, to talk about it here. You can go read about it. But the thing that jumps out to me immediately is this is a $480,000 crowdfunding goal. Ouch. Donate now, because it's going to take a while.

**Dave Jones:** They're up to $9,900, and they've got 43 days left. They want $480,000. Because that's what it costs, right? Have they got a breakdown of how the money's spent? Because that would be interesting.

**Chris Gammell:** I don't know if it's on here, but it's almost guaranteed to be around the fabrication, right?

**Dave Jones:** If you want to get your... Yeah, of course. I'd love to know if they've got exact numbers on that, and they're publishing them. That would be cool. Anyway, is it available in DIP package?

**Chris Gammell:** I don't think so. There's a breakout board. There's a breakout board in the DIP format. I was going to back up, but now it's like... Yeah. Yeah, so let's see. So for the dev board...

**Dave Jones:** It's available in a QFN32.

**Chris Gammell:** Yeah. And if you want the dev board, it's $99. So that'll have like a SD card slot and a regulator and EEPROM and micro USB, stuff like that. So that's really the one to do. If you want to get at it, if you want to just support them, buy a chip or just give them $5. But if you want to start using it as soon as you get it, I would say go for the $99. Get the first open source chip ever. I think it's a great idea. I think it's really cool.

**Dave Jones:** But hang on.

**Chris Gammell:** That's a heavy one.

**Dave Jones:** It's all great being silicon, but have they got... Because it's open source. Does that mean that the HDL is available and you can just drop this as a process core into your FPGA?

**Chris Gammell:** I don't know.

**Dave Jones:** Because it's kind of pointless having an open source chip if you can't do that. I mean, what the hell are people going to do? Take your open code and then go, oh, I'm going to make a slight variation of this and then I'm going to go fab my own chip. You know, it's just not going to happen.

**Chris Gammell:** Right. Well, I think that is the plan to get to that point of...

**Dave Jones:** Well, that would have been my plan from day one is that like here, as soon as we make this goal, we will release the...

**Chris Gammell:** Yeah, so look, you can already go to their GitHub account. So it's github.com slash onchipuis. Onchipuis. Right. Onchipuis. And basically, these are the people. So they've got the programmer. They've got the core. They've got the processor.

**Dave Jones:** Yep, here we go. The Vato project.

**Chris Gammell:** Yeah, so you can already pull this into the Vato, which is the Xilinx thing.

**Dave Jones:** The Xilinx thing. Okay, cool. Cool.

**Chris Gammell:** Yeah.

**Dave Jones:** All right.

**Chris Gammell:** So that's good. And so what I was going to get at with this stuff is I think that... So $480,000 is a... That's a huge goal. It's definitely doable. And I definitely encourage people to at least get five bucks. It's very cool. I would think that this project is likely going to be made on other programs. So like this is really good, I think, for... Especially for college programs that are looking to be able to immediately dig into a core like this, right? And take it in. Yes, of course. Simulate it with that kind of thing. And then play around with... Yep, yep, yep. Totally. So especially if you're at a university where you're working on this kind of stuff, if you're interested, talk to your professor. Go and see if you can throw in $5,000, $10,000 toward this type of thing. Get early access. Work on the project beforehand. Maybe you can just... I think that that would be a best case scenario to really kind of supercharge this project. But like I said, I think it's also good for people that are interested in open source. Yeah. It's a big effort, right? So that's really great. Oh, it's huge. Yeah, that's great. And we'll try and talk to these folks at some point as well. So RISC-V. Yes. A risky project with RISC-V.

**Dave Jones:** Or is its name actually OpenV? RISC-V is the core.

**Chris Gammell:** Well, I think the project name is OpenV, but it's the core is RISC-V. Yeah.

**Dave Jones:** Is it called RISC-V or is it called RISC-V?

**Chris Gammell:** Yeah, they actually have it written out as RISC-V.

**Dave Jones:** Sweet.

**Chris Gammell:** Yeah.

**Dave Jones:** 32-bit. Why didn't they go to 64?

**Chris Gammell:** I don't know.

**Dave Jones:** We'll have to get them on Ask.

**Chris Gammell:** Yep. Yeah. And it's interesting too because I saw the project is listed as coming out of... I'm going to butcher this. Bucaramanga, Colombia. Oh, yes.

**Dave Jones:** Yeah. Book it. Yeah. That's probably... That's your wife. Yep.

**Chris Gammell:** Maybe that's a university there or something there.

**Dave Jones:** Send your money to Colombia. Sorry to all our Colombian listeners.

**Chris Gammell:** It looks like a big city actually, like from Google. But I don't know much about it.

**Dave Jones:** Yeah. I was going to ask, like, who is behind it?

**Chris Gammell:** More details in the future.

**Dave Jones:** Anyway, I'm sure if we watch the video, we could find out maybe.

**Chris Gammell:** No, the video actually doesn't show much. They don't have people. No, it just doesn't show people. There's people at the bottom. So...

**Dave Jones:** I like videos that show people. I want, you know... Yeah, I agree with that.

**Chris Gammell:** I want to see who's doing it. Right. You kind of want the story behind it a little bit too, but...

**Dave Jones:** Oh, no. Yeah. I don't want the solar roadway story. No, no, no.

**Chris Gammell:** You don't want a sob story, but you want...

**Dave Jones:** No, no, no, exactly. Oh, we met when we were three years old and we knew we'd be together forever. Like, bleh. Right? No. But no, I just want to see and hear the person behind a crowdfunded campaign, you know? Yeah. Star in your own videos, damn it. Otherwise, I'm not going to back you.

**Chris Gammell:** Okay. So, one last thing. This is actually an older link. I was just kind of trolling around in Reddit today looking at what's interesting on... You know, some of my subreddits are like ECE and electronics and nice chips and stuff like that. And I saw one on there and it was... The title was Building an SDR from Scratch. And it was actually from four months ago. I didn't realize. It just got reposted. But... So, you read through this thing. It's like a $300 SDR radio, blah, blah, blah, blah, blah. And then you read a couple more things about this. The guy is 18. He did a full SDR build from scratch on an Oshpark board. Figured it all out. Full FPGA on like an Artex 7.

**Dave Jones:** And he's used Altium Designer to design it. How does... At 18, how do you get an Altium Designer license?

**Chris Gammell:** I do not know. But this is... It's really good documentation too. Apparently, he's at MIT now. So, I don't know who this guy is. If he's listening... Oh, right.

**Dave Jones:** So, he's obviously got a student license of Altium Designer. Okay. Sure. Yeah. Okay. Right.

**Chris Gammell:** But very impressive.

**Dave Jones:** Nice. Nice work. Yeah. Great write-up too.

**Chris Gammell:** So, definitely worth checking out.

**Dave Jones:** It looks very comprehensive. Yeah. Impressive. There's a lot of effort which goes into producing something like that. Right.

**Chris Gammell:** So, this is a great example, right? This is like what you're talking about where it's like this is now going to live on his site forever. And this is a great portfolio piece.

**Dave Jones:** Right. Yeah. Electronics.kitchen. I didn't even know there was a .kitchen space.

**Chris Gammell:** Oh. There are so many like...

**Dave Jones:** I know. Right. TLDs now. Anyway, electronics.kitchen. Right. If... Seriously. Like... Lucas Laobayer. Lucas Laobayer. Laobayer. Laobayer. Laobayer. Laobayer. Yeah. Lucas Bayer. Yeah. If this was in your resume, I would check out your website. I look at this post and I don't even have to look further. Give it your job. You're hired. Right? Right. Like, seriously. It's that simple. Right? Because I know the amount of effort that goes into producing. You can't bullshit your way through this stuff. Right? You know, it's like, you know, he's laid out the boards, stencils, extensive photos. He's using... He knows all about measuring the spectrum and the bandwidths and everything. Like, dude, you're hired. That's all you have to do, folks. It's just one... That's all you have to do. One big... One project like that.

**Chris Gammell:** Just start with whatever you're doing. Definitely. I think that, you know, the documentation... I remember... I remember I titled an episode after something you said where you said documentation is a waste of time. I would like to refute that. And I think 2016 current date, Dave, I forgot who it was. When have I ever said documentation is a waste of time? I think it was probably tongue-in-cheek, but...

**Dave Jones:** In jest. Okay. Yeah, yeah, yeah.

**Chris Gammell:** Yeah. Let's see. It was episode... It was back in March of 2016, episode 289. I will link that in as well. Okay. I don't remember why you said it.

**Dave Jones:** Yeah, okay. Right. Documentation is a waste of time.

**Chris Gammell:** Oh, here we go. Oh, okay. That's what it is. There is fidelity loss in documentation, especially if you're relying on key designers. Dave has once been told, quote, documentation is a waste of time. Oh, okay. Right, yes. So it wasn't actually Dave. Oh, yes.

**Dave Jones:** That comes from my Altium days, yeah. Yeah. Yeah, yeah. I was probably talking about Altium. Okay. Right.

**Chris Gammell:** Okay. So it wasn't Dave saying that. But still, I just... I remember that, like, specifically because I titled an episode that. Oh, man. Right. That's funny. So we both agree documentation is not a waste of time. No. Yeah. No, it still sucks, though. You know, like, it's not easy, right? It's, like, you're making videos. Like, it's... I make videos about that stuff, too.

**Dave Jones:** It's using good documentation, is he? Yeah. Yeah. Oh, and he's done his schematics, very similar to mine with the outline block diagram, with the outline block diagrams and separating the blocks with the colors and putting headers on them.

**Chris Gammell:** I actually... He talked about... In some of his posts, he was talking about his home kit, and it was basically the EEV blog starter pack. So I would not be surprised if he's on your forum or watches your stuff or listens to this show. He could very well be under a pseudonym. Yeah. Yeah. We're everywhere, Dave. We are legion. Yep. Right. Yeah. Let's see. Anything else on this list? There's... Nah. There's car stuff. Samsung just bought a car electronics company and blah. Intel's gonna be investing in self-driving cars. Blah. Blah. LiDAR. Oh, actually, this is kind of interesting. There is a newly available LiDAR chip for five bucks. That is actually kind of interesting. So this is from... Okay. Who is it by? Oh, Osram. So basically, they're gonna be selling a standalone LiDAR chip, and that could be very interesting.

**Dave Jones:** Right. Okay. Hey.

**Chris Gammell:** I mean, some of this is...

**Speaker ?:** How does...

**Chris Gammell:** The claims are a little bit... Like, this is on TechCrunch. They're like, a $5 chip that works as well as a $70 tower system and hockey puck size $8,000 system. Oh, I'm looking at it. It's like, no, not really. It's not gonna work that well, because you probably still need external stuff, and there's no...

**Dave Jones:** Well, I was gonna say, what sensors do you have to hook up? I mean, is it... Like, it's just the chips, the smarts, right? Actually processing the stuff. It's not like shit's being emitted from the chip.

**Chris Gammell:** I don't think so. So I think it's probably like, it's probably a adjustment system, and... But, let's see. And this is an electronic announcement, too, so...

**Dave Jones:** It has four laser diodes connected together to ensure accuracy. Yeah, but the lasers aren't on the frickin' die.

**Chris Gammell:** Right, exactly. Well, yeah, and if you look at this chip, it's just the chip, but it's probably... You know, in terms of accessibility, this is a good step forward. So if you wanted to make... You know, now you just have to add the motor system and the mapping and stuff like that. So it's probably... You know, so yeah, and it's from Osram, too. So it is probably all around the laser piece, right? Because they do a lot of lasers and opto stuff. Yeah, they're totally into all that. Yeah, yeah. Yeah, so...

**Dave Jones:** But still, I mean, just this...

**Chris Gammell:** So this is not... Like, LiDAR is going to get much bigger.

**Dave Jones:** Hang on, no, no, no. They're claiming peak optical output from the chip. This is like a hybrid module that the lasers are on the chip.

**Chris Gammell:** I don't see... I'm looking at the picture and maybe...

**Dave Jones:** Okay, well, I'm... Here's the webpage. Here's the webpage.

**Chris Gammell:** But I'm just saying that, like, it looks like it's a chip. And so I don't understand how that would work. But people have to look for themselves because they obviously can't see it here. Either way, like, look, there's a cap in there, right? And it's showing... It's like a system on module, right? So they're showing, like, an enclosed cap. But people will have to check this out. At the very least, it's more accessible. So that piece is cool. Yep. Oh, yeah. 8 by 5 millimeter. 8 millimeter by 5 millimeter.

**Dave Jones:** It will be available from early summer 2017. Market launch plan for 2018. Oh, boom.

**Chris Gammell:** Right. So... Boo. I think the main thing, too, is that, like, if people are... So, like, say someone in our listening audience is interested in LiDAR and putting it on drones or something like that. Yeah. You're probably still going to buy a finished LiDAR module, right? Like a spinning...

**Dave Jones:** Oh, of course. You're not going to... Don't roll, you know. You don't roll. Nobody rolls their own anymore.

**Chris Gammell:** But this potentially, you know, this kind of technology and being available to the LiDAR module makers that can drop the cost of that. That's ultimately the... Of course. Of course. Yes. And there's probably other stuff in the pipeline, too. Yeah.

**Dave Jones:** You can buy a 10, 20 buck LiDAR module on AliExpress. You know, that's... Right.

**Chris Gammell:** That's the ultimate thing. That's what you're really hoping for at the application... Right.

**Dave Jones:** Of course.

**Chris Gammell:** ...implementation, so...

**Dave Jones:** Operating voltage, 24 volts. Jeez.

**Chris Gammell:** That makes sense. For cars, right?

**Dave Jones:** Oh, yeah. Well, okay. Yeah.

**Chris Gammell:** Maybe not cars, but I guess cars are 12, but...

**Dave Jones:** Yeah, but, well, other vehicles are 24, like trucks and stuff are 24, aren't they?

**Chris Gammell:** Yeah. Yeah. Well, there is lots of other links, and we add links to our subreddit each week, and we encourage people to add stuff, including, for next week, we will have Tesla 500 on here. So, if you have questions for him about high-speed cameras or how things are done, just add a text post to our subreddit, just say, question for Tesla 500, colon, what the question is, or be creative. You can figure it out. But if you have questions, you can ask him there.

**Dave Jones:** Cool. And thanks to all our Patreon supporters.

**Chris Gammell:** Of course. And we are thankful for them. Ha. Ha. It's Thanksgiving in the States, so thankful. Yeah. Thank you. Yeah. Anyways, to all my American brethren, have a good holiday. Dave, we'll talk next week.

**Dave Jones:** Catch you next time. Bye.

**Speaker ?:** We'll be right back.
